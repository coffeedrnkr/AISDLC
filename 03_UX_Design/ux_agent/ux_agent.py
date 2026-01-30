
import os
import argparse
import sys
import re

# Ensure standards module is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../00_Introduction/standards')))
from genai_agent_base import GenAIBaseAgent

from rich.console import Console

console = Console()

# Import Contracts Loader
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts')))
from contracts_loader import load_dod

class UXAgent(GenAIBaseAgent):
    """
    Enterprise UX Agent (Google Gen AI SDK Compatible).
    Handles Personas, Heuristic Reviews, and Wireframing.
    """
    def __init__(self):
        super().__init__(
            system_instruction="You are a Senior UX Researcher & Product Designer."
        )
        self.prompts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompts")

    def _load_prompt(self, prompt_filename: str) -> str:
        prompt_path = os.path.join(self.prompts_dir, prompt_filename)
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            console.print(f"[yellow]Warning: Prompt file not found at {prompt_path}.[/yellow]")
            return None

    def _extract_output(self, response_text: str) -> str:
        match = re.search(r'<output>(.*?)</output>', response_text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return response_text.strip()

    def generate_artifact(self, prompt_file: str, inputs: dict, output_path: str):
        template = self._load_prompt(prompt_file)
        if not template:
            # Try to infer if filename is different or check generic names
            # For now, strict fail
             raise FileNotFoundError(f"Prompt {prompt_file} missing.")

        prompt = template
        for key, value in inputs.items():
            prompt = prompt.replace(f"{{{{{key}}}}}", value)

        # Inject Definition of Done (Contract)
        dod_instruction = load_dod("UX")
        prompt += dod_instruction

        console.print(f"[bold blue]GenAI SDK: Generating UX Artifact via {prompt_file}...[/bold blue]")
        response_text = self.generate(prompt, temperature=0.4) # Slightly creative
        content = self._extract_output(response_text)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        console.print(f"[green]Saved to: {output_path}[/green]")

def main():
    parser = argparse.ArgumentParser(description="UX Agent")
    parser.add_argument("--task", choices=['personas', 'review', 'wireframes'], required=True)
    parser.add_argument("--input", required=True, help="Input file (e.g. PRD or Screenshot description)")
    parser.add_argument("--output", required=True, help="Output file")
    
    args = parser.parse_args()
    agent = UXAgent()
    
    with open(args.input, 'r', encoding='utf-8') as f:
        input_content = f.read()

    if args.task == 'personas':
        agent.generate_artifact(
            "UX_001-generate-personas.md", 
            {"PRD_CONTENT": input_content}, 
            args.output
        )
    elif args.task == 'review':
        agent.generate_artifact(
            "UX_002-heuristic-review.md", 
            {"DESIGN_CONTENT": input_content}, 
            args.output
        )
    elif args.task == 'wireframes':
        agent.generate_artifact(
            "UX_003-generate-wireframes.md", 
            {"USER_STORY": input_content}, 
            args.output
        )

if __name__ == "__main__":
    main()
