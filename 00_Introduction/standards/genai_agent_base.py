# Standardized Google Gen AI SDK Base Agent
# Compliant with Google Agent Development Kit (ADK) standards (2025+)

import os
from google import genai
from google.genai import types
from rich.console import Console
from dotenv import load_dotenv

console = Console()

class GenAIBaseAgent:
    """
    Base class for all Agents in the AI SDLC using the unified google-genai SDK.
    Compatible with both Vertex AI (Enterprise) and Gemini Developer API.
    """
    
    def __init__(self, model_version: str = None, system_instruction: str = None):
        load_dotenv()
        
        # 1. Configuration
        self.project_id = os.getenv("GCP_PROJECT_ID")
        self.location = os.getenv("GCP_LOCATION", "us-central1")
        
        # Default to Gemini 1.5 Pro
        self.model_version = model_version or os.getenv("GEMINI_MODEL", "gemini-1.5-pro-002")
        
        # 2. Initialize Unified Client (Vertex AI Mode)
        # Setting vertexai=True uses Cloud Logging and IAM Auth automatically
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
        console.print(f"[green]Agent Ready. Model: {self.model_version}[/green]")

    def generate(self, prompt: str, temperature: float = 0.2, use_grounding: bool = False) -> str:
        """Wrapper for generate_content using the unified SDK pattern."""
        tools = []
        if use_grounding:
            # Enable Google Search Grounding
            tools.append(types.Tool(google_search=types.GoogleSearch()))
            console.print("[yellow]Using Google Search Grounding for this request...[/yellow]")

        try:
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
            # if response.candidates[0].content.parts[0].text:
            return response.text

            return response.text
        except Exception as e:
            console.print(f"[red]Gen AI Generation Error: {e}[/red]")
            return ""

    def count_tokens(self, prompt: str) -> int:
        """Helper to check costs."""
        # Note: Token counting syntax varies slightly in v1; implementing safe fallback
        try:
            response = self.client.models.count_tokens(
                model=self.model_version,
                contents=prompt
            )
            return response.total_tokens
        except:
            return 0
