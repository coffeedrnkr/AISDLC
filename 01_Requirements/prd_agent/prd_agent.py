
import os
import glob
import re
import sys

# Ensure standards module is importable
# Ensure standards module is importable
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../00_Introduction/standards')))
# Import Contracts Loader
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts')))
from contracts_loader import load_dod
from genai_agent_base import GenAIBaseAgent
from follow_up_manager import FollowUpManager
from session_state_manager import SessionStateManager

from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv

console = Console()

class PRDAgent(GenAIBaseAgent):
    """
    Enterprise PRD Agent (Google Gen AI SDK / ADK Compatible).
    """
    def __init__(self):
        # Initialize the base class
        super().__init__(
            system_instruction="Role: Expert Product Owner & Business Analyst."
        )
        # Load env from local directory or parent
        load_dotenv()
        
        # Set up prompts directory path
        self.prompts_dir = os.path.join(os.path.dirname(__file__), "../prompts")
        
        # Initialize State Managers
        self.tracker = FollowUpManager(output_dir="outputs")
        self.session_mgr = SessionStateManager(output_dir="outputs")

    def _load_prompt(self, prompt_filename: str) -> str:
        """Loads a prompt template from the external prompts directory."""
        prompt_path = os.path.join(self.prompts_dir, prompt_filename)
        try:
            with open(prompt_path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            console.print(f"[yellow]Warning: Prompt file not found at {prompt_path}.[/yellow]")
            return None

    def _extract_output(self, response_text: str) -> str:
        """Extracts content from <output> tags if present."""
        match = re.search(r'<output>(.*?)</output>', response_text, re.DOTALL)
        if match:
            return match.group(1).strip()
        return response_text.strip()

    def load_documents(self, input_dir: str) -> str:
        """Loads all text/markdown files from the input directory."""
        documents_content = ""
        files = glob.glob(os.path.join(input_dir, "**/*.*"), recursive=True)

        valid_extensions = ['.md', '.txt', '.csv', '.json']
        loaded_count = 0

        for file_path in files:
            if any(file_path.endswith(ext) for ext in valid_extensions):
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        documents_content += f"\n\n--- DOCUMENT START: {os.path.basename(file_path)} ---\n"
                        documents_content += content
                        documents_content += f"\n--- DOCUMENT END: {os.path.basename(file_path)} ---\n"
                        loaded_count += 1
                        console.print(f"Loaded: {os.path.basename(file_path)}")
                except Exception as e:
                    console.print(f"[yellow]Failed to read {file_path}: {e}[/yellow]")
        return documents_content

    def generate_prd(self, documents_content: str, template_path: str) -> str:
        """Generates the PRD based on the loaded documents and template."""
        try:
            with open(template_path, 'r', encoding='utf-8') as f:
                template_content = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Template not found at {template_path}")

        prompt_template = self._load_prompt("PRD_GEN-synthesize-prd.md")
        
        if prompt_template:
            prompt = prompt_template.replace("{{DOCUMENTS_CONTENT}}", documents_content)
            prompt = prompt.replace("{{TEMPLATE_CONTENT}}", template_content)
        else:
            raise FileNotFoundError("Critical Error: PRD_GEN prompt file is missing.")

        # Inject Definition of Done (Contract)
        dod_instruction = load_dod("PRD")
        prompt += dod_instruction

        console.print("[bold blue]GenAI SDK: Generating PRD...[/bold blue]")
        
        response_text = self.generate(prompt, temperature=0.3)
        return self._extract_output(response_text)

    def identify_gaps(self, prd_content: str) -> str:
        """Analyzes the generated PRD to identify gaps and conflicts."""
        prompt_template = self._load_prompt("PRD_GAP-identify-gaps.md")
        
        if prompt_template:
            prompt = prompt_template.replace("{{PRD_CONTENT}}", prd_content)
        else:
            # Fallback prompt if file missing
            prompt = f"Identify gaps in this PRD:\n{prd_content}"

        console.print("[bold blue]GenAI SDK: Analyzing gaps...[/bold blue]")
        response_text = self.generate(prompt, temperature=0.2)
        return self._extract_output(response_text)

    def run_discovery_tool(self, tool_name: str, prd_content: str, user_input: str = "") -> str:
        """Runs a specific discovery tool on the PRD content."""
        tool_prompts = {
            "mindmap": f"Generate a Mermaid mindmap for the features in this PRD. Focus on scope visualization.\n{prd_content}",
            "brainstorm": f"Run a 'What-If' brainstorming session on this PRD. Expand on features and suggest related capabilities.\n{prd_content}",
            "roleplay": f"Simulate a User Roleplay. Create a dialogue between a Persona and the System to validate requirements.\n{prd_content}",
            "crud": f"Perform a CRUD Analysis on the data entities implied in this PRD. List Create, Read, Update, Delete operations.\n{prd_content}",
            "premortem": f"Run a Premortem Analysis. Identify potential edge cases, failures, and risks for this product.\n{prd_content}",
            "traceability": f"Generate a Traceability Matrix linking Business Goals to Functional Requirements.\n{prd_content}",
            "state": f"Generate a Mermaid State Diagram for key lifecycle entities (e.g., Status fields) in this PRD.\n{prd_content}",
            "decision": f"Create a Decision Table for complex business rules found in this PRD.\n{prd_content}",
            "bdd": f"Generate high-level BDD/Gherkin scenarios to validate the key user stories in this PRD.\n{prd_content}",
        }
        
        base_prompt = tool_prompts.get(tool_name.lower())
        if not base_prompt:
            return "Tool not found."
            
        if user_input:
            base_prompt += f"\n\nUser Context/Focus: {user_input}"
            
        console.print(f"[bold blue]Running {tool_name}...[/bold blue]")
        return self.generate(base_prompt, temperature=0.4)

    def interactive_session(self, input_dir: str, output_dir: str):
        """Runs the PRD Agent in Interactive Discovery Mode."""
        from rich.prompt import Prompt
        
        # 1. Load & Initial Synthesis
        documents_content = self.load_documents(input_dir)
        if not documents_content:
            console.print("[red]No documents found in inputs/.[/red]")
            return

        console.print(Panel.fit("[bold magenta]PRD Discovery Agent[/bold magenta]", subtitle="Interactive Mode"))

        # --- FOLLOW-UP TRACKER INTEGRATION ---
        # Check for Open Questions from previous sessions
        context_updates = self.tracker.prompt_for_updates()
        if context_updates:
            documents_content += context_updates  # Inject answers into current session context
            console.print("[blue]Updates incorporated into session context.[/blue]")
        # -------------------------------------

        console.print("[bold blue]Synthesizing initial Draft...[/bold blue]")
        
        # Initial Draft
        # We use a default string if template is missing to avoid crash
        try:
           draft_prd = self.generate_prd(documents_content, "templates/prd_template.md")
        except:
           draft_prd = self.generate(f"Synthesize these documents into a PRD Draft:\n{documents_content}")

        # Initial Gap Analysis
        gaps = self.identify_gaps(draft_prd)
        console.print(Panel(gaps, title="Initial Gap Analysis"))

        # Discovery Loop
        TOOLS = ["mindmap", "brainstorm", "roleplay", "crud", "premortem", "traceability", "state", "decision", "bdd"]
        tools_run = []  # Track which tools were used this session
        
        while True:
            console.print("\n" + "="*60)
            console.print("[bold]Available Discovery Tools:[/bold]")
            console.print(", ".join(TOOLS))
            console.print("[dim]Type 'park: <question>' to save a follow-up item.[/dim]")
            
            tool_choice = Prompt.ask(
                "Which tool to run? (or 'done' to finish)",
                choices=TOOLS + ["done", "skip"],
                default="done"
            )

            if tool_choice == "done":
                break
            
            # --- PARKING LOT LOGIC ---
            if tool_choice.lower().startswith("park:"):
                # This branch won't be hit because Prompt.ask restricts choices.
                # We need to relax the Prompt validation or handle it differently.
                # Changing strategy below to ask input separately if strictly needed, 
                # OR we instruct user to enter tool name, then inside asking for focus we allow parking.
                pass 
            # -------------------------
            
            user_input = Prompt.ask("Any specific focus? (Type 'park: <question>' to save an item)", default="")

            # --- PARKING LOT LOGIC (Inside focus prompt) ---
            if user_input.lower().startswith("park:"):
                question = user_input[5:].strip()
                if question:
                    self.tracker.add_item(question, context=f"During {tool_choice}")
                continue
            # -----------------------------------------------
            
            result = self.run_discovery_tool(tool_choice, draft_prd, user_input)
            tools_run.append(tool_choice)  # Track this tool
            console.print(Panel(result, title=f"Output: {tool_choice.upper()}"))
            
            # Auto-incorporate
            console.print("[dim] Incorporating findings into PRD...[/dim]")
            update_prompt = f"""
            You are refining a PRD. 
            Review this new discovery aid ({tool_choice}) and UPDATE the PRD with any new findings, edge cases, or requirements.
            
            CURRENT PRD:
            {draft_prd}
            
            NEW DISCOVERY INFO:
            {result}
            
            Output the FULLY UPDATED PRD.
            """
            draft_prd = self.generate(update_prompt, temperature=0.2)
            console.print("[green]PRD Updated.[/green]")

        # Final Save
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "PRD_Interactive_Final.md")
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(draft_prd)
        console.print(f"[bold green]Final PRD saved to {output_path}[/bold green]")

        # Log Session
        self.session_mgr.log_session(
            agent_name="PRD Discovery Agent",
            tools_run=tools_run,
            outcomes=[f"Generated PRD: {output_path}"],
            questions_added=len(self.tracker.get_open_items())
        )

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--interactive", action="store_true", help="Run in interactive discovery mode")
    parser.add_argument("--input", default="inputs", help="Input directory")
    parser.add_argument("--output", default="outputs", help="Output directory")
    args = parser.parse_args()
    
    agent = PRDAgent()
    
    if args.interactive:
        agent.interactive_session(args.input, args.output)
    else:
        # Classic Batch Mode
        documents = agent.load_documents(args.input)
        if documents:
            prd = agent.generate_prd(documents, "templates/prd_template.md")
            gaps = agent.identify_gaps(prd)
            
            os.makedirs(args.output, exist_ok=True)
            with open(os.path.join(args.output, "PRD_Draft.md"), "w") as f:
                f.write(prd)
            with open(os.path.join(args.output, "gaps.md"), "w") as f:
                f.write(gaps)
            console.print("[green]Batch generation complete.[/green]")

if __name__ == "__main__":
    main()

