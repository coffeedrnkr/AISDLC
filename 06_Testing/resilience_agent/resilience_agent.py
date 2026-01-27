# Resilience Agent
# Load testing and chaos engineering (Dimension 5)

import os
import sys
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '00_Introduction', 'standards'))

from genai_agent_base import GenAIBaseAgent
from rich.console import Console

console = Console()

SYSTEM_PROMPT = """
You are a Performance Engineer and Site Reliability Engineer (SRE).
You specialize in:
1. Load testing - Generating k6 and Locust scripts
2. Chaos engineering - Designing controlled failure experiments
3. Performance baselines - Establishing SLA thresholds

Always include:
- Hypothesis for each experiment
- Blast radius and rollback plan
- Success/failure criteria
- Approval requirements for destructive tests
"""


class ResilienceAgent(GenAIBaseAgent):
    """
    Resilience Agent for Dimension 5: Load & Chaos Testing.
    Generates load test scripts and chaos engineering scenarios.
    """
    
    def __init__(self):
        super().__init__(
            system_instruction=SYSTEM_PROMPT,
            require_approval=True  # Chaos tests need HITL
        )
        self.prompts_dir = os.path.join(os.path.dirname(__file__), '..', 'prompts')
    
    def _load_prompt(self, filename: str) -> str:
        path = os.path.join(self.prompts_dir, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            console.print(f"[yellow]Warning: Prompt not found: {path}[/yellow]")
            return None
    
    def generate_load_tests(self, api_spec_path: str, output_dir: str) -> str:
        """Generate load test scripts from API specification."""
        
        with open(api_spec_path, 'r', encoding='utf-8') as f:
            api_spec = f.read()
        
        prompt_template = self._load_prompt("LOAD_001-generate-load-tests.md")
        
        if prompt_template:
            prompt = prompt_template.replace("{{API_ENDPOINTS}}", api_spec)
        else:
            prompt = f"""
Generate load test scripts for these API endpoints:

{api_spec}

Generate both:
1. k6 script (JavaScript) with stages: ramp up, steady, peak, ramp down
2. Locust script (Python) with weighted tasks
3. Performance baseline template

Include thresholds for P95 < 500ms and error rate < 1%.
"""
        
        console.print("[bold blue]Generating load test scripts...[/bold blue]")
        response = self.generate(prompt, temperature=0.2)
        
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "load_tests.md")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Load Test Scripts\n\n")
            f.write(f"Generated from: {api_spec_path}\n\n")
            f.write("---\n\n")
            f.write(response)
        
        console.print(f"[green]Saved: {output_path}[/green]")
        return output_path
    
    def generate_chaos_scenarios(self, architecture_path: str, output_dir: str) -> str:
        """Generate chaos engineering scenarios with approval gates."""
        
        with open(architecture_path, 'r', encoding='utf-8') as f:
            architecture = f.read()
        
        prompt_template = self._load_prompt("CHAOS_001-chaos-scenarios.md")
        
        if prompt_template:
            prompt = prompt_template.replace("{{ARCHITECTURE_DOCS}}", architecture)
        else:
            prompt = f"""
Generate chaos engineering scenarios for this architecture:

{architecture}

For each scenario include:
1. Hypothesis (If X fails, then Y because Z)
2. Blast radius (what's affected)
3. Rollback plan
4. Success criteria
5. Approval required (Yes/No)

Generate Chaos Mesh YAML for Kubernetes environments.
"""
        
        console.print("[bold blue]Generating chaos scenarios...[/bold blue]")
        console.print("[yellow]⚠️  Chaos scenarios require approval before execution[/yellow]")
        
        response = self.generate_with_approval(
            prompt,
            action_description="Generate chaos engineering scenarios (destructive tests)"
        )
        
        if response is None:
            console.print("[red]Chaos scenario generation cancelled by user.[/red]")
            return None
        
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "chaos_scenarios.md")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Chaos Engineering Scenarios\n\n")
            f.write("⚠️ **WARNING:** These scenarios are destructive. Require approval before execution.\n\n")
            f.write(f"Generated from: {architecture_path}\n\n")
            f.write("---\n\n")
            f.write(response)
        
        console.print(f"[green]Saved: {output_path}[/green]")
        return output_path


def main():
    parser = argparse.ArgumentParser(description="Resilience Agent - Load & Chaos Testing")
    parser.add_argument("--task", choices=['load', 'chaos'], required=True, help="Task type")
    parser.add_argument("--input", required=True, help="Input file (API spec or architecture)")
    parser.add_argument("--output", default="outputs", help="Output directory")
    args = parser.parse_args()
    
    agent = ResilienceAgent()
    
    if args.task == 'load':
        agent.generate_load_tests(args.input, args.output)
    elif args.task == 'chaos':
        agent.generate_chaos_scenarios(args.input, args.output)


if __name__ == "__main__":
    main()
