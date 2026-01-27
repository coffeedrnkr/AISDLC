"""
Output Guardrails for AI-Generated Content

Validates AI outputs to prevent:
- Hallucinated file paths or APIs
- PII exposure (emails, SSNs, phone numbers)
- Excessive output length
- Invalid structured data (JSON, YAML)
"""

import re
import os
import json
from typing import Tuple, List, Dict, Any
from rich.console import Console

console = Console()


class OutputGuardrails:
    """
    Validates AI-generated outputs before they are saved or presented to users.
    Integrated into GenAIBaseAgent.generate() for automatic enforcement.
    """

    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {
            "max_output_length": 50000,
            "check_pii": True,
            "check_paths": True,
            "check_json": True,
        }
        
        # PII patterns
        self.pii_patterns = {
            "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            "ssn": r'\b\d{3}-\d{2}-\d{4}\b',
            "phone": r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
            "credit_card": r'\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b',
        }

    def validate(self, output: str, context: Dict[str, Any] = None) -> Tuple[bool, List[str]]:
        """
        Validate AI output. Returns (is_valid, list_of_issues).
        
        Args:
            output: The AI-generated text to validate
            context: Optional context with known_paths, expected_format, etc.
        
        Returns:
            Tuple of (is_valid: bool, issues: list of issue descriptions)
        """
        context = context or {}
        issues = []

        # Check output length
        if len(output) > self.config.get("max_output_length", 50000):
            issues.append(f"Output exceeds maximum length ({len(output)} > {self.config['max_output_length']})")

        # Check for PII
        if self.config.get("check_pii", True):
            pii_found = self._check_pii(output)
            if pii_found:
                issues.append(f"Potential PII detected: {', '.join(pii_found)}")

        # Check for hallucinated paths
        if self.config.get("check_paths", True):
            known_paths = context.get("known_paths", [])
            fake_paths = self._check_fake_paths(output, known_paths)
            if fake_paths:
                issues.append(f"Potentially hallucinated paths: {fake_paths[:3]}")

        # Validate JSON if expected
        if context.get("expected_format") == "json":
            json_issues = self._validate_json(output)
            if json_issues:
                issues.append(f"Invalid JSON: {json_issues}")

        return len(issues) == 0, issues

    def _check_pii(self, text: str) -> List[str]:
        """Check for potential PII in text."""
        found = []
        for pii_type, pattern in self.pii_patterns.items():
            if re.search(pattern, text):
                found.append(pii_type)
        return found

    def _check_fake_paths(self, text: str, known_paths: List[str]) -> List[str]:
        """Check for file paths that don't exist."""
        # Extract paths from text (simple heuristic)
        path_pattern = r'(?:/[\w.-]+)+(?:\.\w+)?'
        found_paths = re.findall(path_pattern, text)
        
        fake_paths = []
        for path in found_paths:
            # Skip common patterns that aren't real paths
            if path.startswith('/api/') or path.startswith('/v1/'):
                continue
            # If we have known paths and this isn't one of them, flag it
            if known_paths and path not in known_paths and not os.path.exists(path):
                fake_paths.append(path)
        
        return fake_paths[:5]  # Limit to first 5

    def _validate_json(self, text: str) -> str:
        """Validate that text is valid JSON."""
        try:
            # Try to extract JSON from markdown code blocks
            json_match = re.search(r'```json\s*([\s\S]*?)\s*```', text)
            if json_match:
                json.loads(json_match.group(1))
            else:
                json.loads(text)
            return ""
        except json.JSONDecodeError as e:
            return str(e)

    def sanitize(self, output: str) -> str:
        """Remove or mask sensitive content from output."""
        sanitized = output
        
        # Mask emails
        sanitized = re.sub(
            self.pii_patterns["email"],
            "[EMAIL REDACTED]",
            sanitized
        )
        
        # Mask SSNs
        sanitized = re.sub(
            self.pii_patterns["ssn"],
            "[SSN REDACTED]",
            sanitized
        )
        
        # Mask credit cards
        sanitized = re.sub(
            self.pii_patterns["credit_card"],
            "[CARD REDACTED]",
            sanitized
        )
        
        return sanitized


class ApprovalGate:
    """
    Human-in-the-Loop approval gate for critical actions.
    Use before saving files, creating Jira tickets, or other side effects.
    """

    def __init__(self, auto_approve: bool = False):
        self.auto_approve = auto_approve
        self.approval_log = []

    def require_approval(
        self,
        action: str,
        content: str,
        preview_length: int = 500
    ) -> bool:
        """
        Pause and ask user to approve before proceeding.
        
        Args:
            action: Description of what will happen (e.g., "Save PRD to outputs/")
            content: The content being approved
            preview_length: How much of the content to show
        
        Returns:
            True if approved, False if rejected
        """
        if self.auto_approve:
            self._log_decision(action, "auto-approved")
            return True

        # Show preview
        preview = content[:preview_length]
        if len(content) > preview_length:
            preview += f"\n... [{len(content) - preview_length} more characters]"

        console.print("\n" + "="*60)
        console.print(f"[bold yellow]⚠️ APPROVAL REQUIRED: {action}[/bold yellow]")
        console.print("-"*60)
        console.print(preview)
        console.print("-"*60)
        
        response = console.input("[bold]Approve this action? (y/n/v=view all): [/bold]").lower()
        
        if response == 'v':
            console.print(content)
            response = console.input("[bold]Approve? (y/n): [/bold]").lower()
        
        approved = response == 'y'
        self._log_decision(action, "approved" if approved else "rejected")
        
        if not approved:
            console.print("[red]Action rejected by user.[/red]")
        
        return approved

    def _log_decision(self, action: str, decision: str):
        """Log approval decisions for audit trail."""
        import datetime
        self.approval_log.append({
            "timestamp": datetime.datetime.now().isoformat(),
            "action": action,
            "decision": decision
        })

    def get_audit_log(self) -> List[Dict]:
        """Return the approval audit log."""
        return self.approval_log
