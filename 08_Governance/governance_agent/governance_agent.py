
import os
import argparse
import sys
import re

# Ensure standards module is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../00_Introduction/standards')))
from genai_agent_base import GenAIBaseAgent

from rich.console import Console

console = Console()

class GovernanceAgent(GenAIBaseAgent):
    """
    Enterprise Governance Agent (Google Gen AI SDK Compatible).
    Handles Code Reviews and Compliance Checks.
    """
    def __init__(self):
        super().__init__(
            system_instruction="You are a Principal Software Engineer & Security Auditor."
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
        # Governance usually outputs a report. If structured, use regex.
        match = re.search(r'<output>(.*?)</output>', response_text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return response_text.strip()

    def run_code_review(self, code_file: str, output_path: str):
        template = self._load_prompt("GOV_REV-code-review.md")
        if not template:
            raise FileNotFoundError("GOV_REV prompt missing.")
            
        with open(code_file, 'r', encoding='utf-8') as f:
            code_content = f.read()
            
        prompt = template.replace("{{CODE_CONTENT}}", code_content)
        
        console.print(f"[bold blue]GenAI SDK: Auditing {os.path.basename(code_file)}...[/bold blue]")
        
        # Security reviews need low temp for precision
        response_text = self.generate(prompt, temperature=0.1)
        content = self._extract_output(response_text)
        
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)
        console.print(f"[green]Review saved to: {output_path}[/green]")

def main():
    parser = argparse.ArgumentParser(description="Governance Agent")
    parser.add_argument("--task", choices=['review'], default='review')
    parser.add_argument("--input", required=True, help="Code file to review")
    parser.add_argument("--output", required=True, help="Output report file")
    
    args = parser.parse_args()
    agent = GovernanceAgent()
    
    if args.task == 'review':
        agent.run_code_review(args.input, args.output)

if __name__ == "__main__":
    main()
