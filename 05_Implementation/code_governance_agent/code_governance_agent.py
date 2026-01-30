
import os
import re
import glob
import subprocess
import argparse
import google.generativeai as genai
from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv

# Ensure standards module is importable
# Ensure standards module is importable
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../00_Introduction/standards')))

# Import Contracts Loader
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts')))
from contracts_loader import load_dod

from genai_agent_base import GenAIBaseAgent

# Handle import for confluence_utils - may not be available in all environments
try:
    from agents.utils.confluence_utils import get_page_content
except ImportError:
    def get_page_content(title, space):
        return None

console = Console()


class CodeGovernanceAgent(GenAIBaseAgent):
    def __init__(self):
        super().__init__(
            system_instruction="Role: Senior Principal Engineer & Security Architect."
        )
        # Load env from epic_agent or local
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        load_dotenv(os.path.join(base_dir, "epic_agent", ".env"))

        # Set up prompts directory path
        self.prompts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompts")

    def _load_prompt(self, prompt_filename: str) -> str:
        """Loads a prompt template from the external prompts directory."""
        prompt_path = os.path.join(self.prompts_dir, prompt_filename)
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            console.print(f"[yellow]Warning: Prompt file not found at {prompt_path}. Using fallback.[/yellow]")
            return None

    def _extract_output(self, response_text: str) -> str:
        """Extracts content from <output> tags if present."""
        match = re.search(r'<output>(.*?)</output>', response_text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return response_text.strip()

    def run_static_analysis(self, target_path: str):
        """Runs Ruff and Bandit."""
        results = {"ruff": "", "bandit": ""}

        # Ruff
        try:
            console.print("[blue]Running Ruff...[/blue]")
            ruff_res = subprocess.run(["ruff", "check", target_path, "--output-format=text"], capture_output=True, text=True)
            results["ruff"] = ruff_res.stdout + ruff_res.stderr
        except FileNotFoundError:
            results["ruff"] = "Ruff not found."

        # Bandit
        try:
            console.print("[blue]Running Bandit...[/blue]")
            bandit_res = subprocess.run(["bandit", "-r", target_path, "-f", "txt"], capture_output=True, text=True)
            results["bandit"] = bandit_res.stdout + bandit_res.stderr
        except FileNotFoundError:
            results["bandit"] = "Bandit not found."

        return results

    def fetch_governance_rules(self):
        """Fetches rules from Confluence."""
        console.print("[blue]Fetching Governance Rules from Confluence...[/blue]")
        content = get_page_content("Code Governance & Security Standards", "SD")
        if not content:
            console.print("[yellow]Could not fetch from Confluence. Using default fallback.[/yellow]")
            return "Ensure code is secure, readable, and follows PEP8."
        return content

    def review_code(self, target_path: str, output_dir: str):
        # 1. Get Static Analysis
        static_analysis = self.run_static_analysis(target_path)

        # 2. Get Governance Text
        governance_context = self.fetch_governance_rules()

        # 3. Read Code
        code_content = ""
        if os.path.isfile(target_path):
            with open(target_path, 'r') as f:
                code_content = f.read()
        else:
            # Basic folder read - limit to 5 py files for demo
            files = glob.glob(os.path.join(target_path, "**/*.py"), recursive=True)[:5]
            for f in files:
                with open(f, 'r') as r:
                    code_content += f"\n--- FILE: {f} ---\n" + r.read()

        # 4. Load external prompt template
        prompt_template = self._load_prompt("GOV_REV-review-code.md")

        if prompt_template:
            # Replace placeholders in external prompt
            prompt = prompt_template.replace("{{GOVERNANCE_CONTEXT}}", governance_context)
            prompt = prompt.replace("{{STATIC_ANALYSIS_RUFF}}", static_analysis['ruff'])
            prompt = prompt.replace("{{STATIC_ANALYSIS_BANDIT}}", static_analysis['bandit'])
            prompt = prompt.replace("{{CODE_CONTENT}}", code_content[:20000])  # Context limit safety

            # Inject Definition of Done (Contract)
            dod_instruction = load_dod("DEV")
            prompt += dod_instruction
        else:
            # Fallback to embedded prompt if external file not found
            prompt = f"""
            Task: Review the provided code against the Organization's Governance Standards.

            --- GOVERNANCE STANDARDS (Connecting to Confluence Source of Truth) ---
            {governance_context}

            --- STATIC ANALYSIS RESULTS ---
            Result from Ruff (Linting):
            {static_analysis['ruff']}

            Result from Bandit (Security):
            {static_analysis['bandit']}

            --- CODE TO REVIEW ---
            {code_content[:20000]}  # Context limit safety

            --- INSTRUCTIONS ---
            1. **Summarize Static Analysis**: Briefly mention if automated tools passed or failed.
            2. **Strategic Review**: Look for logic errors, design pattern anti-patterns, and readability issues that tools missed.
            3. **Security Deep Dive**: Highlight any potential vulnerabilities (Injection, Secrets, etc.) referenced in the Governance Standards.
            4. **Actionable Feedback**: Provide concrete code snippets for improvements.

            --- OUTPUT ---
            Markdown report. 
            """

        console.print("[blue]Generating AI Review...[/blue]")
        try:
            report_text = self.generate(prompt)
            report = self._extract_output(report_text)

            # Save
            filename = "CodeGovernanceReport.md"
            path = os.path.join(output_dir, filename)
            with open(path, "w", encoding="utf-8") as f:
                f.write(report)
            console.print(f"[green]Saved Report: {path}[/green]")
            return report

        except Exception as e:
            console.print(f"[red]Error generating review: {e}[/red]")
            return str(e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True, help="File or Directory to review")
    parser.add_argument("--output", default=".", help="Output directory")
    args = parser.parse_args()

    agent = CodeGovernanceAgent()
    agent.review_code(args.target, args.output)


if __name__ == "__main__":
    main()
