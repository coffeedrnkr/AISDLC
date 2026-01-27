# Epic Decomposition Agent
# Splits PRD features into Epics using SPIDR methodology

import os
import sys
import argparse

# Add parent to path for shared base
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '00_Introduction', 'standards'))

from genai_agent_base import GenAIBaseAgent
from rich.console import Console
from rich.panel import Panel

console = Console()

SYSTEM_PROMPT = """
You are an Expert Agile Coach and Business Analyst specializing in Epic decomposition.

Your job is to take a Product Requirements Document (PRD) and break it into Epics.

Use the SPIDR methodology for splitting:
- Spike: Separate research/unknowns from implementation
- Path: Split by user paths (Happy Path vs Error Handling)
- Interface: Split by platform (Mobile vs Web) or complexity
- Data: Split by data types or sources
- Rules: Split by business logic complexity

After proposing Epics, run an INVEST quality check on each:
- Independent: Minimal dependencies
- Negotiable: Open to clarification
- Valuable: Delivers clear value
- Estimable: Team can size it
- Small: Fits within a release
- Testable: Clear "Done" criteria

Output format for each Epic:
## EPIC-XXX: [Title]
### Description
[What this Epic delivers]
### SPIDR Justification
[Why this was split this way]
### INVEST Check
| Criterion | Pass/Fail | Notes |
### Dependencies
[List any blockers]
### Estimated Size
[T-shirt size: S/M/L/XL]
"""

class EpicDecompositionAgent(GenAIBaseAgent):
    def __init__(self):
        super().__init__(
            system_instruction=SYSTEM_PROMPT
        )
        self.prompts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompts")

    def decompose_prd(self, prd_path: str, output_dir: str) -> str:
        """Decompose PRD into Epics."""
        with open(prd_path, 'r', encoding='utf-8') as f:
            prd_content = f.read()

        prompt = f"""
Analyze this PRD and decompose it into Epics.

PRD CONTENT:
{prd_content}

INSTRUCTIONS:
1. Identify the major features/capabilities in the PRD.
2. For each, decide if it should be ONE Epic or SPLIT using SPIDR.
3. For each proposed Epic, run the INVEST check.
4. Output a list of Epics with their details.
5. Flag any Epics that are too large (XL) and suggest further splits.

Begin decomposition:
"""

        console.print("[bold blue]Decomposing PRD into Epics...[/bold blue]")
        response = self.generate(prompt, temperature=0.2)

        # Save output
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "epic_breakdown.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Epic Breakdown\n\n")
            f.write(f"Source: {prd_path}\n\n")
            f.write("---\n\n")
            f.write(response)

        console.print(f"[green]Epic breakdown saved to: {output_path}[/green]")
        return output_path


def main():
    parser = argparse.ArgumentParser(description="Epic Decomposition Agent")
    parser.add_argument("--prd", required=True, help="Path to PRD file")
    parser.add_argument("--output", default="outputs", help="Output directory")
    args = parser.parse_args()

    agent = EpicDecompositionAgent()
    agent.decompose_prd(args.prd, args.output)


if __name__ == "__main__":
    main()
