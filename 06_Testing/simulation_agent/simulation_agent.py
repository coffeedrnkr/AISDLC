# Simulation Agent
# Persona-based testing and edge case generation (Dimension 1)

import os
import sys
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '00_Introduction', 'standards'))

from genai_agent_base import GenAIBaseAgent
from rich.console import Console

console = Console()

SYSTEM_PROMPT = """
You are a QA Analyst specializing in persona-based testing.
You simulate how different user types interact with the system,
identifying edge cases and failure modes specific to each persona.

For each persona, you test across:
- Behavioral patterns (typical, unusual, error recovery)
- Technical constraints (devices, network, accessibility)
- Domain-specific contexts (experience level, permissions, data volumes)

Output comprehensive simulation reports with prioritized findings.
"""


class SimulationAgent(GenAIBaseAgent):
    """
    Simulation Agent for Dimension 1: Persona Testing.
    Generates edge cases and stress tests per user persona.
    """
    
    def __init__(self):
        super().__init__(system_instruction=SYSTEM_PROMPT)
        self.prompts_dir = os.path.join(os.path.dirname(__file__), '..', 'prompts')
    
    def _load_prompt(self, filename: str) -> str:
        path = os.path.join(self.prompts_dir, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            console.print(f"[yellow]Warning: Prompt not found: {path}[/yellow]")
            return None
    
    def simulate_personas(self, personas_path: str, stories_path: str, output_dir: str) -> str:
        """Generate simulation report for all personas against user stories."""
        
        with open(personas_path, 'r', encoding='utf-8') as f:
            personas = f.read()
        
        with open(stories_path, 'r', encoding='utf-8') as f:
            stories = f.read()
        
        prompt_template = self._load_prompt("SIM_001-persona-simulation.md")
        
        if prompt_template:
            prompt = prompt_template.replace("{{PERSONA_CONTENT}}", personas)
            prompt = prompt.replace("{{USER_STORIES}}", stories)
        else:
            prompt = f"""
Analyze these personas and generate simulation test scenarios:

PERSONAS:
{personas}

USER STORIES TO TEST:
{stories}

For each persona, generate:
1. Happy path scenarios
2. Edge case scenarios (at least 3 per persona)
3. Stress test scenarios
4. Accessibility scenarios

Prioritize findings by severity.
"""
        
        console.print("[bold blue]Simulating persona interactions...[/bold blue]")
        response = self.generate(prompt, temperature=0.3)
        
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "simulation_report.md")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Persona Simulation Report\n\n")
            f.write(f"Generated from: {personas_path}\n\n")
            f.write("---\n\n")
            f.write(response)
        
        console.print(f"[green]Saved: {output_path}[/green]")
        return output_path


def main():
    parser = argparse.ArgumentParser(description="Simulation Agent - Persona Testing")
    parser.add_argument("--personas", required=True, help="Path to personas file")
    parser.add_argument("--stories", required=True, help="Path to user stories file")
    parser.add_argument("--output", default="outputs", help="Output directory")
    args = parser.parse_args()
    
    agent = SimulationAgent()
    agent.simulate_personas(args.personas, args.stories, args.output)


if __name__ == "__main__":
    main()
