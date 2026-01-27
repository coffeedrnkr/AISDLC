# Epic Elaboration Agent
# Fleshes out Epic details using 9 discovery tools

import os
import sys
import argparse

# Add parent to path for shared base
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '00_Introduction', 'standards'))

from genai_agent_base import GenAIBaseAgent
from follow_up_manager import FollowUpManager
from session_state_manager import SessionStateManager

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()

SYSTEM_PROMPT = """
You are an Expert Business Analyst acting as a friendly coach.
Your job is to help elaborate an Epic by discovering missing details.

You have access to 9 discovery tools:
1. Mind Map - Visualize sub-features
2. Brainstorming / What-If - Explore related considerations
3. Roleplay / Persona Interview - Validate user experience
4. CRUD Analysis - Define data operations
5. Premortem / Edge Cases - Identify failure modes
6. Traceability Matrix - Link to PRD requirements
7. State Transition Diagram - Map entity lifecycles
8. Decision Table - Capture business rules
9. BDD / Gherkin Scenarios - Write acceptance criteria

For each Epic:
1. Analyze what's MISSING (gaps in the description).
2. RECOMMEND a tool that would help fill that gap.
3. EXPLAIN why you're recommending it in simple terms.
4. Execute the tool and show the output.
5. Ask follow-up questions to refine.
6. Suggest the next tool if appropriate.

Your goal is to produce a fully elaborated Epic ready for Story generation.
"""

TOOLS = {
    "mindmap": "Generate a Mermaid mindmap of sub-features",
    "brainstorm": "Explore what-if scenarios and related considerations",
    "roleplay": "Simulate a persona interview to validate the flow",
    "crud": "Analyze Create/Read/Update/Delete operations for data entities",
    "premortem": "Identify what could go wrong (edge cases, failures)",
    "traceability": "Link Epic back to PRD requirements",
    "state": "Generate a state transition diagram for lifecycle entities",
    "decision": "Build a decision table for complex business rules",
    "bdd": "Generate Gherkin acceptance criteria",
}


class EpicElaborationAgent(GenAIBaseAgent):
    def __init__(self):
        super().__init__(
            system_instruction=SYSTEM_PROMPT
        )
        # Initialize State Managers
        self.tracker = FollowUpManager(output_dir="outputs")
        self.session_mgr = SessionStateManager(output_dir="outputs")

    def analyze_epic(self, epic_content: str) -> str:
        """Analyze Epic and recommend tools."""
        prompt = f"""
Analyze this Epic and identify gaps that need elaboration.

EPIC CONTENT:
{epic_content}

For each gap you find, recommend which discovery tool would help.
Format your response as:

## Gap Analysis
1. [Gap description] → Recommend: [Tool Name]
2. [Gap description] → Recommend: [Tool Name]
...

## Suggested Starting Point
[Which tool to run first and why]
"""
        return self.generate(prompt, temperature=0.2)

    def run_tool(self, tool_name: str, epic_content: str, user_input: str = "") -> str:
        """Execute a specific discovery tool."""
        tool_prompts = {
            "mindmap": f"Generate a Mermaid mindmap for this Epic's sub-features:\n{epic_content}",
            "brainstorm": f"Run a What-If brainstorm for this Epic. What related features or considerations are missing?\n{epic_content}",
            "roleplay": f"Simulate a persona interview. Play the role of a user and walk through this Epic's functionality:\n{epic_content}",
            "crud": f"Generate a CRUD analysis table for the data entities in this Epic:\n{epic_content}",
            "premortem": f"Run a premortem analysis. What could go wrong with this Epic in production?\n{epic_content}",
            "traceability": f"Create a traceability matrix linking this Epic back to PRD requirements:\n{epic_content}",
            "state": f"Generate a Mermaid state diagram for any lifecycle entities in this Epic:\n{epic_content}",
            "decision": f"Build a decision table for any complex business rules in this Epic:\n{epic_content}",
            "bdd": f"Generate Gherkin scenarios (Given/When/Then) for this Epic:\n{epic_content}",
        }

        prompt = tool_prompts.get(tool_name.lower(), f"Analyze: {epic_content}")
        if user_input:
            prompt += f"\n\nUser clarification: {user_input}"

        return self.generate(prompt, temperature=0.3)

    def interactive_session(self, epic_path: str, output_dir: str):
        """Run an interactive elaboration session."""
        self.tracker.output_dir = output_dir # Ensure correct output dir

        with open(epic_path, 'r', encoding='utf-8') as f:
            epic_content = f.read()

        console.print(Panel.fit("[bold magenta]Epic Elaboration Agent[/bold magenta]", subtitle="Interactive Mode"))
        console.print(f"[dim]Loaded: {epic_path}[/dim]\n")

        # --- FOLLOW-UP TRACKER INTEGRATION ---
        context_updates = self.tracker.prompt_for_updates()
        if context_updates:
            epic_content += f"\n\n## Updates from Follow-Up Items\n{context_updates}"
            console.print("[blue]Updates incorporated into Epic context.[/blue]")
        # -------------------------------------

        # Initial analysis
        console.print("[bold blue]Analyzing Epic for gaps...[/bold blue]\n")
        analysis = self.analyze_epic(epic_content)
        console.print(analysis)

        # Accumulate elaborations
        elaborations = {"analysis": analysis}
        tools_run = []  # Track tools used this session

        while True:
            console.print("\n" + "="*60)
            console.print("[dim]Type 'park: <question>' in the focus prompt to save an item.[/dim]")
            
            tool_choice = Prompt.ask(
                "Which tool to run?",
                choices=list(TOOLS.keys()) + ["done", "skip"],
                default="done"
            )

            if tool_choice == "done":
                break
            elif tool_choice == "skip":
                continue

            user_input = Prompt.ask("Any specific focus? (Type 'park: <question>' to save)", default="")

            # --- PARKING LOT LOGIC ---
            if user_input.lower().startswith("park:"):
                question = user_input[5:].strip()
                if question:
                    self.tracker.add_item(question, context=f"During Elaboration of {os.path.basename(epic_path)}")
                continue
            # -------------------------
            
            console.print(f"\n[bold blue]Running {tool_choice}...[/bold blue]\n")
            result = self.run_tool(tool_choice, epic_content, user_input)
            console.print(result)

            elaborations[tool_choice] = result
            tools_run.append(tool_choice)  # Track this tool

            # Auto-register entities from CRUD/State tools
            if tool_choice in ["crud", "state"]:
                # Simple extraction: register the epic name as an entity
                entity_name = os.path.basename(epic_path).replace(".md", "").replace("EPIC-", "")
                self.session_mgr.register_entity(
                    name=entity_name,
                    discovered_in=f"Epic Elaboration ({tool_choice})",
                    operations="CRUD" if tool_choice == "crud" else "",
                    states="See State Diagram" if tool_choice == "state" else "",
                    notes=f"From {os.path.basename(epic_path)}"
                )

            # Update epic content with new findings
            epic_content += f"\n\n## {tool_choice.upper()} Analysis\n{result}"

        # Save final output
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, os.path.basename(epic_path).replace(".md", "_elaborated.md"))
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(epic_content)

        console.print(f"\n[green]Elaborated Epic saved to: {output_path}[/green]")

        # Log Session
        self.session_mgr.log_session(
            agent_name="Epic Elaboration Agent",
            tools_run=tools_run,
            outcomes=[f"Elaborated: {output_path}"],
            questions_added=len(self.tracker.get_open_items())
        )

        return output_path


def main():
    parser = argparse.ArgumentParser(description="Epic Elaboration Agent")
    parser.add_argument("--epic", required=True, help="Path to Epic file")
    parser.add_argument("--output", default="outputs", help="Output directory")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode")
    args = parser.parse_args()

    agent = EpicElaborationAgent()
    
    if args.interactive:
        agent.interactive_session(args.epic, args.output)
    else:
        # Non-interactive: just run analysis
        with open(args.epic, 'r', encoding='utf-8') as f:
            epic_content = f.read()
        analysis = agent.analyze_epic(epic_content)
        console.print(analysis)


if __name__ == "__main__":
    main()
