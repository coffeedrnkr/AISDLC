
import os
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

class StoryAgent(GenAIBaseAgent):
    """
    Enterprise Story Agent (Google Gen AI SDK / ADK Compatible).
    """
    def __init__(self):
        super().__init__(
            system_instruction="You are a Senior Technical Product Owner & QA Architect."
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

    def generate_stories(self, epic_content: str, architecture_content: str, template_content: str, output_dir: str):
        prompt_template = self._load_prompt("STORY_GEN-generate-stories.md")

        if prompt_template:
            prompt = prompt_template.replace("{{EPIC_CONTENT}}", epic_content)
            prompt = prompt.replace("{{ARCHITECTURE_CONTENT}}", architecture_content)
            prompt = prompt.replace("{{TEMPLATE_CONTENT}}", template_content)
        else:
            raise FileNotFoundError("Critical Error: STORY_GEN prompt file is missing.")

        # Inject Definition of Done (Contract)
        dod_instruction = load_dod("STORY")
        prompt += dod_instruction

        console.print("[bold blue]GenAI SDK: Generating User Stories...[/bold blue]")
        
        response_text = self.generate(prompt, temperature=0.3)
        content = self._extract_output(response_text)

        # Parsing logic
        stories = content.split("=== STORY START:")
        for story_section in stories[1:]:
            lines = story_section.strip().split("\n")
            header_line = lines[0].strip()
            safe_title = "".join([c if c.isalnum() else "_" for c in header_line])

            filename = f"Story_{safe_title}.md"
            path = os.path.join(output_dir, filename)
            
            content = f"# Story: {header_line}\n" + "\n".join(lines[1:])

            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            console.print(f"[green]Saved: {filename}[/green]")
