"""
Prompt Registry and Operations

Provides:
- Versioned prompt management
- Prompt testing against test cases
- A/B comparison between prompt versions
- Evaluation metrics
"""

import os
import json
import hashlib
from typing import Dict, List, Optional, Any, Callable
from pathlib import Path
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()


class PromptRegistry:
    """
    Central registry for versioned prompts.
    Treats prompts as code: versioned, tested, evaluated.
    """

    def __init__(self, registry_path: str = None, prompts_base: str = None):
        self.registry_path = registry_path or "prompts/registry.json"
        self.prompts_base = prompts_base or "."
        self.registry = self._load_registry()

    def _load_registry(self) -> Dict:
        """Load the prompt registry from JSON."""
        if os.path.exists(self.registry_path):
            try:
                with open(self.registry_path, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                console.print(f"[yellow]Warning: Invalid registry file, starting fresh[/yellow]")
        return {"prompts": {}}

    def _save_registry(self):
        """Save the registry to disk."""
        os.makedirs(os.path.dirname(self.registry_path) or ".", exist_ok=True)
        with open(self.registry_path, 'w') as f:
            json.dump(self.registry, f, indent=2)

    def register_prompt(
        self,
        name: str,
        file_path: str,
        version: str = "v1",
        description: str = "",
        test_cases_path: str = None
    ):
        """Register a new prompt or version."""
        if name not in self.registry["prompts"]:
            self.registry["prompts"][name] = {
                "latest": version,
                "description": description,
                "versions": {},
                "test_cases": test_cases_path
            }
        
        self.registry["prompts"][name]["versions"][version] = {
            "path": file_path,
            "created_at": datetime.now().isoformat(),
            "hash": self._hash_file(file_path)
        }
        self.registry["prompts"][name]["latest"] = version
        
        self._save_registry()
        console.print(f"[green]Registered {name} {version}[/green]")

    def get_prompt(self, name: str, version: str = "latest") -> str:
        """
        Get a prompt by name and version.
        
        Args:
            name: The prompt identifier (e.g., "PRD_GEN")
            version: Version string or "latest"
        
        Returns:
            The prompt content as a string
        """
        if name not in self.registry["prompts"]:
            raise ValueError(f"Prompt '{name}' not found in registry")
        
        prompt_info = self.registry["prompts"][name]
        
        if version == "latest":
            version = prompt_info["latest"]
        
        if version not in prompt_info["versions"]:
            raise ValueError(f"Version '{version}' not found for prompt '{name}'")
        
        file_path = prompt_info["versions"][version]["path"]
        full_path = os.path.join(self.prompts_base, file_path)
        
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Prompt file not found: {full_path}")
        
        with open(full_path, 'r') as f:
            return f.read()

    def list_prompts(self) -> List[Dict]:
        """List all registered prompts with their versions."""
        prompts = []
        for name, info in self.registry["prompts"].items():
            prompts.append({
                "name": name,
                "latest": info["latest"],
                "versions": list(info["versions"].keys()),
                "description": info.get("description", "")
            })
        return prompts

    def _hash_file(self, path: str) -> str:
        """Generate a hash of a file's contents."""
        full_path = os.path.join(self.prompts_base, path)
        if os.path.exists(full_path):
            with open(full_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()[:8]
        return "unknown"

    def check_for_changes(self) -> List[Dict]:
        """Check if any registered prompts have changed since registration."""
        changes = []
        for name, info in self.registry["prompts"].items():
            for version, version_info in info["versions"].items():
                current_hash = self._hash_file(version_info["path"])
                if current_hash != version_info.get("hash"):
                    changes.append({
                        "name": name,
                        "version": version,
                        "original_hash": version_info.get("hash"),
                        "current_hash": current_hash
                    })
        return changes


class PromptEvaluator:
    """
    Evaluates prompts against test cases and metrics.
    Enables prompt testing like unit testing.
    """

    def __init__(self, generator_fn: Callable[[str], str] = None):
        """
        Args:
            generator_fn: Function that takes a prompt and returns AI output
        """
        self.generator_fn = generator_fn
        self.results = []

    def run_test_case(
        self,
        prompt: str,
        test_case: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Run a single test case against a prompt.
        
        Test case format:
        {
            "name": "Test description",
            "input": "Variables to inject into prompt",
            "expected_contains": ["phrases that should appear"],
            "expected_not_contains": ["phrases that should NOT appear"],
            "max_length": 1000
        }
        """
        if not self.generator_fn:
            return {"error": "No generator function provided"}

        # Format prompt with test input
        formatted_prompt = prompt.format(**test_case.get("input", {})) if test_case.get("input") else prompt
        
        # Generate output
        try:
            output = self.generator_fn(formatted_prompt)
        except Exception as e:
            return {
                "name": test_case.get("name", "unknown"),
                "passed": False,
                "error": str(e)
            }

        # Evaluate
        issues = []
        
        # Check expected phrases
        for phrase in test_case.get("expected_contains", []):
            if phrase.lower() not in output.lower():
                issues.append(f"Missing expected phrase: '{phrase}'")
        
        # Check forbidden phrases
        for phrase in test_case.get("expected_not_contains", []):
            if phrase.lower() in output.lower():
                issues.append(f"Contains forbidden phrase: '{phrase}'")
        
        # Check length
        max_length = test_case.get("max_length")
        if max_length and len(output) > max_length:
            issues.append(f"Output too long: {len(output)} > {max_length}")

        result = {
            "name": test_case.get("name", "unknown"),
            "passed": len(issues) == 0,
            "issues": issues,
            "output_length": len(output),
            "output_preview": output[:200] + "..." if len(output) > 200 else output
        }
        
        self.results.append(result)
        return result

    def run_test_suite(
        self,
        prompt: str,
        test_cases: List[Dict]
    ) -> Dict[str, Any]:
        """Run all test cases and return summary."""
        results = []
        for test_case in test_cases:
            result = self.run_test_case(prompt, test_case)
            results.append(result)
        
        passed = sum(1 for r in results if r.get("passed", False))
        total = len(results)
        
        return {
            "passed": passed,
            "total": total,
            "success_rate": passed / total if total > 0 else 0,
            "results": results
        }

    def compare_prompts(
        self,
        prompt_a: str,
        prompt_b: str,
        test_cases: List[Dict]
    ) -> Dict[str, Any]:
        """A/B compare two prompt versions."""
        results_a = self.run_test_suite(prompt_a, test_cases)
        self.results = []  # Reset for B
        results_b = self.run_test_suite(prompt_b, test_cases)
        
        return {
            "prompt_a": {
                "success_rate": results_a["success_rate"],
                "passed": results_a["passed"],
                "total": results_a["total"]
            },
            "prompt_b": {
                "success_rate": results_b["success_rate"],
                "passed": results_b["passed"],
                "total": results_b["total"]
            },
            "winner": "A" if results_a["success_rate"] > results_b["success_rate"] else "B" if results_b["success_rate"] > results_a["success_rate"] else "TIE"
        }

    def print_report(self):
        """Print a formatted test report."""
        table = Table(title="Prompt Evaluation Results")
        table.add_column("Test", style="cyan")
        table.add_column("Passed", style="green")
        table.add_column("Issues", style="red")

        for result in self.results:
            passed = "✓" if result.get("passed") else "✗"
            issues = ", ".join(result.get("issues", []))[:50]
            table.add_row(result.get("name", "?"), passed, issues or "-")

        console.print(table)


def create_test_case(
    name: str,
    input_vars: Dict = None,
    expected_contains: List[str] = None,
    expected_not_contains: List[str] = None,
    max_length: int = None
) -> Dict:
    """Helper to create a test case dict."""
    return {
        "name": name,
        "input": input_vars or {},
        "expected_contains": expected_contains or [],
        "expected_not_contains": expected_not_contains or [],
        "max_length": max_length
    }
