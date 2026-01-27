# Standardized Google Gen AI SDK Base Agent
# Compliant with Google Agent Development Kit (ADK) standards (2025+)
# Enhanced with: Guardrails, Context Management, HITL, Prompt-Ops

import os
from google import genai
from google.genai import types
from rich.console import Console
from dotenv import load_dotenv

# Import new capabilities
from guardrails import OutputGuardrails, ApprovalGate
from context_manager import ContextManager, TokenBudget

console = Console()


class GenAIBaseAgent:
    """
    Base class for all Agents in the AI SDLC using the unified google-genai SDK.
    Compatible with both Vertex AI (Enterprise) and Gemini Developer API.
    
    Includes:
    - Output Guardrails (PII detection, hallucination prevention)
    - Approval Gates (Human-in-the-loop for critical actions)
    - Context Management (smart document loading)
    - Token Budget tracking
    """
    
    def __init__(
        self, 
        model_version: str = None, 
        system_instruction: str = None,
        enable_guardrails: bool = True,
        require_approval: bool = False
    ):
        load_dotenv()
        
        # 1. Configuration
        self.project_id = os.getenv("GCP_PROJECT_ID")
        self.location = os.getenv("GCP_LOCATION", "us-central1")
        
        # Default to Gemini 1.5 Pro
        self.model_version = model_version or os.getenv("GEMINI_MODEL", "gemini-1.5-pro-002")
        
        # 2. Initialize Unified Client (Vertex AI Mode)
        if self.project_id:
            try:
                self.client = genai.Client(
                    vertexai=True, 
                    project=self.project_id, 
                    location=self.location
                )
                console.print(f"[dim]Initialized Google Gen AI Client (Vertex Mode: {self.project_id})[/dim]")
            except Exception as e:
                console.print(f"[red]Failed to init Vertex AI client: {e}[/red]")
                raise
        else:
            # Fallback for non-enterprise usage (API Key)
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("Neither GCP_PROJECT_ID nor GEMINI_API_KEY found.")
            self.client = genai.Client(api_key=api_key)
            console.print("[dim]Initialized Google Gen AI Client (API Key Mode)[/dim]")

        # 3. Standard Safety Settings (ADK Standard)
        self.safety_settings = [
            types.SafetySetting(
                category="HARM_CATEGORY_HATE_SPEECH",
                threshold="BLOCK_MEDIUM_AND_ABOVE",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_DANGEROUS_CONTENT",
                threshold="BLOCK_MEDIUM_AND_ABOVE",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
                threshold="BLOCK_MEDIUM_AND_ABOVE",
            ),
            types.SafetySetting(
                category="HARM_CATEGORY_HARASSMENT",
                threshold="BLOCK_MEDIUM_AND_ABOVE",
            ),
        ]
        
        self.system_instruction = system_instruction
        
        # 4. Initialize Enhanced Capabilities
        self.guardrails = OutputGuardrails() if enable_guardrails else None
        self.approval_gate = ApprovalGate(auto_approve=not require_approval)
        self.context_manager = ContextManager()
        self.token_budget = TokenBudget()
        
        console.print(f"[green]Agent Ready. Model: {self.model_version}[/green]")
        if enable_guardrails:
            console.print("[dim]Guardrails: Enabled | Context Manager: Active[/dim]")

    def generate(
        self, 
        prompt: str, 
        temperature: float = 0.2, 
        use_grounding: bool = False,
        validate_output: bool = True,
        context: dict = None
    ) -> str:
        """
        Wrapper for generate_content using the unified SDK pattern.
        
        Args:
            prompt: The prompt to send to the model
            temperature: Creativity setting (0.0-1.0)
            use_grounding: Enable Google Search grounding
            validate_output: Run guardrails on output
            context: Optional context for guardrail validation
        
        Returns:
            Generated text, or empty string on error
        """
        tools = []
        if use_grounding:
            tools.append(types.Tool(google_search=types.GoogleSearch()))
            console.print("[yellow]Using Google Search Grounding for this request...[/yellow]")

        try:
            # Track token usage
            prompt_tokens = self.count_tokens(prompt)
            self.token_budget.spend(prompt_tokens, "input prompt")
            
            response = self.client.models.generate_content(
                model=self.model_version,
                contents=prompt,
                config=types.GenerateContentConfig(
                    temperature=temperature,
                    top_p=0.95,
                    max_output_tokens=8192,
                    system_instruction=self.system_instruction,
                    safety_settings=self.safety_settings,
                    tools=tools
                )
            )
            
            output = response.text
            
            # Track output tokens
            output_tokens = self.count_tokens(output)
            self.token_budget.spend(output_tokens, "output")
            
            # Run guardrails if enabled
            if validate_output and self.guardrails:
                is_valid, issues = self.guardrails.validate(output, context or {})
                if not is_valid:
                    console.print(f"[yellow]⚠️ Guardrail warnings: {issues}[/yellow]")
                    # Optionally sanitize
                    output = self.guardrails.sanitize(output)
            
            return output

        except Exception as e:
            console.print(f"[red]Gen AI Generation Error: {e}[/red]")
            return ""

    def generate_with_approval(
        self,
        prompt: str,
        action_description: str,
        **kwargs
    ) -> str:
        """
        Generate content but require human approval before returning.
        Use for critical outputs like saving files or creating tickets.
        """
        output = self.generate(prompt, **kwargs)
        
        if not output:
            return output
        
        if self.approval_gate.require_approval(action_description, output):
            return output
        else:
            return ""  # Rejected

    def load_context(
        self,
        paths: list,
        prioritize: list = None
    ) -> str:
        """
        Load documents using the context manager.
        Handles large files, prioritization, and token limits.
        """
        return self.context_manager.load_documents(
            paths=paths,
            prioritize=prioritize
        )

    def count_tokens(self, prompt: str) -> int:
        """Helper to check costs."""
        try:
            response = self.client.models.count_tokens(
                model=self.model_version,
                contents=prompt
            )
            return response.total_tokens
        except:
            # Fallback estimate
            return len(prompt) // 4

    def get_token_report(self) -> str:
        """Get token usage report for this session."""
        return self.token_budget.report()

    def get_approval_audit(self) -> list:
        """Get audit log of all approval decisions."""
        return self.approval_gate.get_audit_log()

