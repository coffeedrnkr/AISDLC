# Standardized Vertex AI Base Agent for AI SDLC
# This MUST be used by all agents to ensure Enterprise compliance.

import os
import vertexai
from vertexai.generative_models import GenerativeModel, SafetySetting, HarmCategory, HarmBlockThreshold
from rich.console import Console
from dotenv import load_dotenv

console = Console()

class BaseVertexAgent:
    """
    Base class for all Agents in the AI SDLC.
    Handles authentication, initialization, and standard configuration for Vertex AI.
    """
    
    def __init__(self, model_version: str = None, system_instruction: str = None):
        load_dotenv()
        
        # 1. Enterprise Configuration
        self.project_id = os.getenv("GCP_PROJECT_ID")
        self.location = os.getenv("GCP_LOCATION", "us-central1")
        
        # Default to Gemini 1.5 Pro if not specified
        self.model_version = model_version or os.getenv("GEMINI_MODEL", "gemini-1.5-pro-002")
        
        if not self.project_id:
            console.print("[red]Critical Error: GCP_PROJECT_ID not set in .env[/red]")
            raise ValueError("GCP_PROJECT_ID missing. Cannot initialize Vertex AI.")

        # 2. Initialize Vertex AI SDK (Uses Application Default Credentials)
        try:
            vertexai.init(project=self.project_id, location=self.location)
            console.print(f"[dim]Initialized Vertex AI (Project: {self.project_id}, Loc: {self.location})[/dim]")
        except Exception as e:
            console.print(f"[red]Failed to auth with Vertex AI: {e}[/red]")
            console.print("Run `gcloud auth application-default login` to fix this.")
            raise

        # 3. Standard Enterprise Safety Settings (Relaxed for Dev, Strict for Ops)
        # For development agents (PRD, Code Gen), we allow most content unless highly unsafe.
        self.safety_settings = [
            SafetySetting(
                category=HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold=HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
            SafetySetting(
                category=HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
            SafetySetting(
                category=HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                threshold=HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
            SafetySetting(
                category=HarmCategory.HARM_CATEGORY_HARASSMENT,
                threshold=HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE
            ),
        ]

        # 4. Instantiate Model
        self.model = GenerativeModel(
            self.model_version,
            system_instruction=system_instruction
        )
        console.print(f"[green]Agent Ready. Connected to {self.model_version}[/green]")

    def generate(self, prompt: str, temperature: float = 0.2) -> str:
        """Standard wrapper for generation with consistency/telemetry hooks."""
        try:
            response = self.model.generate_content(
                prompt,
                generation_config={
                    "temperature": temperature,
                    "max_output_tokens": 8192,
                    "top_p": 0.95,
                },
                safety_settings=self.safety_settings
            )
            return response.text
        except Exception as e:
            console.print(f"[red]Vertex AI Generation Error: {e}[/red]")
            # In enterprise capability, we might log this to Cloud Logging here
            return ""

    def count_tokens(self, prompt: str) -> int:
        """Helper to check costs."""
        return self.model.count_tokens(prompt).total_tokens
