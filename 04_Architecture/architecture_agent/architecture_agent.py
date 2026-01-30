
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

    def _load_template(self, template_path: str) -> str:
        """Loads a template file relative to the agent."""
        path = os.path.join(os.path.dirname(__file__), template_path)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception:
            return ""

    def _extract_output(self, response_text: str) -> str:
        match = re.search(r'<output>(.*?)</output>', response_text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return response_text.strip()

    def _load_standards(self) -> str:
        """Loads project standards and local guidelines."""
        standards_content = []
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # 1. Project Global Styleguide (.gemini/STYLEGUIDE.md)
        # Path relative to here: ../../.gemini/STYLEGUIDE.md
        project_root = os.path.abspath(os.path.join(base_dir, "../../"))
        styleguide_path = os.path.join(project_root, ".gemini", "STYLEGUIDE.md")
        
        if os.path.exists(styleguide_path):
            try:
                with open(styleguide_path, "r", encoding="utf-8") as f:
                    standards_content.append(f"--- PROJECT STYLEGUIDE ---\n{f.read()}")
                console.print(f"[green]Loaded Styleguide: .gemini/STYLEGUIDE.md[/green]")
            except Exception as e:
                console.print(f"[yellow]Warning: Could not read STYLEGUIDE.md: {e}[/yellow]")
        else:
             console.print(f"[dim]Styleguide not found at {styleguide_path}[/dim]")

        # 2. Local Guidelines (guidelines/*.md)
        guidelines_dir = os.path.join(base_dir, "guidelines")
        if os.path.exists(guidelines_dir):
            for filename in os.listdir(guidelines_dir):
                if filename.endswith(".md"):
                    path = os.path.join(guidelines_dir, filename)
                    try:
                        with open(path, "r", encoding="utf-8") as f:
                            standards_content.append(f"--- GUIDELINE: {filename} ---\n{f.read()}")
                        console.print(f"[green]Loaded Guideline: {filename}[/green]")
                    except Exception as e:
                        console.print(f"[yellow]Warning: Could not read guideline {filename}: {e}[/yellow]")
        
        return "\n\n".join(standards_content)

    def generate_artifact(self, task_name: str, prompt_file: str, inputs: dict, output_path: str):
        """Generic method to run an architecture task."""
        
        template = self._load_prompt(prompt_file)
        if not template:
             raise FileNotFoundError(f"Prompt {prompt_file} missing.")

        # Replace all inputs
        prompt = template
        for key, value in inputs.items():
            prompt = prompt.replace(f"{{{{{key}}}}}", value)

        # Inject Standards
        standards = self._load_standards()
        if standards:
            prompt += "\n\n# STANDARDS, GUIDELINES AND PATTERNS\nThe following standards must be followed when generating this artifact:\n" + standards

        # Inject Definition of Done (Contract)
        dod_role = "ARCH"
        if "openapi" in task_name.lower():
            dod_role = "INTERFACE"
        
        dod_instruction = load_dod(dod_role)
        prompt += dod_instruction


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
            "ARCH_001.md",
            {
                "PRD_CONTENT": input_content,
                "TEMPLATE_CONTENT": self._load_template("templates/system_design_template.md")
            }, 
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
