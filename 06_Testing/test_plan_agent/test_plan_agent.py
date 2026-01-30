
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

class TestPlanAgent(GenAIBaseAgent):
    """
    Enterprise Test Plan Agent (Google Gen AI SDK / ADK Compatible).
    """
    def __init__(self):
        super().__init__(
            system_instruction="You are a Senior SDET & Automation Architect."
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

    def generate_test_plan(self, story_content: str, architecture_content: str, template_content: str, output_dir: str):
        prompt_template = self._load_prompt("TEST_GEN-generate-test-plan.md")

        if prompt_template:
            prompt = prompt_template.replace("{{STORY_CONTENT}}", story_content)
            prompt = prompt.replace("{{ARCHITECTURE_CONTENT}}", architecture_content)
            prompt = prompt.replace("{{TEMPLATE_CONTENT}}", template_content)
        else:
             raise FileNotFoundError("Critical Error: TEST_GEN prompt file is missing.")
        
        # Inject Definition of Done (Contract)
        dod_instruction = load_dod("TEST")
        prompt += dod_instruction

        console.print("[bold blue]GenAI SDK: Generating Test Plan...[/bold blue]")
        
        response_text = self.generate(prompt, temperature=0.2)
        content = self._extract_output(response_text)

        # Cleanup markdown blocks
        if content.startswith("```markdown"):
            content = content.replace("```markdown", "", 1)
        if content.startswith("```"):
            content = content.replace("```", "", 1)
        if content.endswith("```"):
            content = content[:-3]
        content = content.strip()

        # Filename generation
        match = re.search(r"(USR-\d+|Story-\w+)", story_content)
        if match:
            safe_id = match.group(1)
        else:
            lines = story_content.split('\n')
            header = lines[0] if lines else "TestPlan"
            safe_id = "".join([c if c.isalnum() else "_" for c in header])[:30]

        filename = f"TestPlan_{safe_id}.md"
        path = os.path.join(output_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        console.print(f"[green]Saved: {filename}[/green]")
