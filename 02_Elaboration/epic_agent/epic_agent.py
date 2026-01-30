
import os
import glob
import re
import sys

# Ensure standards module is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../00_Introduction/standards')))
from genai_agent_base import GenAIBaseAgent

# Import Contracts Loader
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts')))
from contracts_loader import load_dod

from rich.console import Console

console = Console()

class EpicAgent(GenAIBaseAgent):
    """
    Enterprise Epic Agent (Google Gen AI SDK / ADK Compatible).
    """
    def __init__(self):
        super().__init__(
            system_instruction="You are a Senior Technical Product Manager and Agile Coach."
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

    def load_specifications(self, spec_dir: str) -> str:
        content = ""
        files = glob.glob(os.path.join(spec_dir, "*.md"))
        for file_path in files:
            with open(file_path, 'r', encoding='utf-8') as f:
                content += f"\n\n--- DETAILED SPEC: {os.path.basename(file_path)} ---\n{f.read()}"
        return content

    def generate_epics(self, prd_content: str, architecture_content: str, detailed_specs: str, template_content: str, output_dir: str):
        prompt_template = self._load_prompt("EPIC_GEN-decompose-epics.md")

        if prompt_template:
            prompt = prompt_template.replace("{{PRD_CONTENT}}", prd_content)
            prompt = prompt.replace("{{ARCHITECTURE_CONTENT}}", architecture_content)
            prompt = prompt.replace("{{DETAILED_SPECS}}", detailed_specs)
            prompt = prompt.replace("{{TEMPLATE_CONTENT}}", template_content)
        else:
             raise FileNotFoundError("Critical Error: EPIC_GEN prompt file is missing.")

        # Inject Definition of Done (Contract)
        dod_instruction = load_dod("EPIC")
        prompt += dod_instruction

        console.print("[bold blue]GenAI SDK: Generating Epics with SPIDR strategy...[/bold blue]")
        
        response_text = self.generate(prompt, temperature=0.3)
        content = self._extract_output(response_text)

        # Parsing logic
        epics = content.split("=== EPIC START:")
        for epic_section in epics[1:]:
            lines = epic_section.strip().split("\n")
            title_line = lines[0].strip()
            
            safe_title = "".join([c if c.isalnum() else "_" for c in title_line])
            filename = f"epic_{safe_title}.md"
            path = os.path.join(output_dir, filename)

            with open(path, "w", encoding="utf-8") as f:
                f.write(f"# Epic: {title_line}\n" + "\n".join(lines[1:]))
            console.print(f"[green]Saved: {filename}[/green]")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Epic Agent")
    subparsers = parser.add_subparsers(dest="command", help="Command to run", required=True)

    gen_parser = subparsers.add_parser("generate", help="Generate Epics")
    gen_parser.add_argument("--prd", required=True, help="Path to PRD file")
    gen_parser.add_argument("--arch", required=True, help="Path to Architecture file")
    gen_parser.add_argument("--specs", required=True, help="Directory containing detailed specs")
    gen_parser.add_argument("--output", default="outputs/epics", help="Output directory")

    args = parser.parse_args()
    agent = EpicAgent()

    if args.command == "generate":
        try:
             with open(args.prd, "r", encoding="utf-8") as f: prd = f.read()
             with open(args.arch, "r", encoding="utf-8") as f: arch = f.read()
             specs = agent.load_specifications(args.specs)
             
             # Load Template
             template_path = os.path.join(os.path.dirname(__file__), "templates/epic_template.md")
             if os.path.exists(template_path):
                  with open(template_path, "r", encoding="utf-8") as f: template = f.read()
             else:
                  template = ""

             agent.generate_epics(prd, arch, specs, template, args.output)
        except Exception as e:
             console.print(f"[red]Error: {e}[/red]")

if __name__ == "__main__":
    main()
