
import os
import argparse
import sys
import re

# Ensure standards module is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../00_Introduction/standards')))
from genai_agent_base import GenAIBaseAgent

from rich.console import Console

console = Console()

class ArchitectureAgent(GenAIBaseAgent):
    """
    Enterprise Architecture Agent (Google Gen AI SDK Compatible).
    Handles System Design, DBML, OpenAPI, and Diagram generation.
    """
    def __init__(self):
        super().__init__(
            system_instruction="You are a Distinguished Cloud Architect & Reliability Engineer."
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

    def generate_artifact(self, task_name: str, prompt_file: str, inputs: dict, output_path: str):
        """Generic method to run an architecture task."""
        
        template = self._load_prompt(prompt_file)
        if not template:
             raise FileNotFoundError(f"Prompt {prompt_file} missing.")

        # Replace all inputs
        prompt = template
        for key, value in inputs.items():
            prompt = prompt.replace(f"{{{{{key}}}}}", value)

        console.print(f"[bold blue]GenAI SDK: Generating {task_name}...[/bold blue]")
        
        # Architecture tasks often need higher temperature for creative design, 
        # or lower for strict code specs.
        temp = 0.2
        if "openapi" in task_name.lower() or "dbml" in task_name.lower():
            temp = 0.1 # Strict
        
        response_text = self.generate(prompt, temperature=temp)
        content = self._extract_output(response_text)
        
        # Cleanup
        if content.startswith("```"):
             # Remove first line (```language) and last line (```)
             lines = content.split('\n')
             if lines[0].startswith("```"):
                 lines = lines[1:]
             if lines[-1].startswith("```"):
                 lines = lines[:-1]
             content = "\n".join(lines)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        console.print(f"[green]Saved {task_name} to: {output_path}[/green]")

def main():
    parser = argparse.ArgumentParser(description="Architecture Agent")
    parser.add_argument("--task", choices=['system_design', 'dbml', 'openapi', 'diagrams'], required=True)
    parser.add_argument("--input", required=True, help="Path to input file (e.g., PRD)")
    parser.add_argument("--output", required=True, help="Path to output file")
    
    args = parser.parse_args()
    
    agent = ArchitectureAgent()
    
    with open(args.input, 'r', encoding='utf-8') as f:
        input_content = f.read()

    if args.task == 'system_design':
        # ARCH_001
        agent.generate_artifact(
            "System Design", 
            "ARCH_001.md", # Need to confirm exact filename if it exists, or ARCH_GEN
            {"PRD_CONTENT": input_content}, 
            args.output
        )
    elif args.task == 'dbml':
        # ARCH_002
        agent.generate_artifact(
            "DBML Schema", 
            "ARCH_002-generate-dbml.md", 
            {"ARCHITECTURE_CONTENT": input_content}, 
            args.output
        )
    elif args.task == 'openapi':
        # ARCH_003
        agent.generate_artifact(
            "OpenAPI Spec", 
            "ARCH_003-generate-openapi.md", 
            {"ARCHITECTURE_CONTENT": input_content}, 
            args.output
        )
    elif args.task == 'diagrams':
        # ARCH_004
        agent.generate_artifact(
            "Python Diagrams", 
            "ARCH_004-generate-python-diagrams.md", 
            {"ARCHITECTURE_CONTENT": input_content}, 
            args.output
        )

if __name__ == "__main__":
    main()
