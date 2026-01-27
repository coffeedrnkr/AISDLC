
import os
import argparse
from rich.console import Console
from rich.panel import Panel
from epic_agent import EpicAgent

console = Console()

def main():
    parser = argparse.ArgumentParser(description="AI Agent to decompose PRD into Agile Epics.")
    parser.add_argument("--prd", required=True, help="Path to approved PRD")
    parser.add_argument("--arch", required=True, help="Path to Architecture Hub main directory (or concat file)")
    parser.add_argument("--specs", default="inputs/specifications", help="Directory for detailed business specs")
    parser.add_argument("--output", default="outputs/epics", help="Output directory")
    parser.add_argument("--model", default=None, help="Gemini model (default: env GEMINI_MODEL)")
    
    # Jira Integration Args
    parser.add_argument("--publish", action="store_true", help="Publish generated Epics to Jira")
    parser.add_argument("--project_key", help="Jira Project Key (e.g., 'MP') to publish to. Required if --publish is set.")
    
    args = parser.parse_args()
    
    os.makedirs(args.output, exist_ok=True)
    
    console.print(Panel.fit("[bold orange1]Starting Epic Decomposition Agent[/bold orange1]", subtitle="Enterprise Edition"))
    
    agent = EpicAgent(model_name=args.model)
    
    # Load inputs
    with open(args.prd, 'r', encoding='utf-8') as f:
        prd = f.read()
        
    # Determine how to load Architecture (simplification: assume user passes a summary file or we load all)
    # For now, let's assume arg.arch points to a file containing the architecture summary
    # In production, we'd walk the arch-hub directory.
    if os.path.isdir(args.arch):
         # Simplistic loading of all md files in arch dir
         arch = ""
         for fpath in glob.glob(os.path.join(args.arch, "**/*.md"), recursive=True):
             with open(fpath, 'r') as f: arch += f.read() + "\n"
    else:
        with open(args.arch, 'r', encoding='utf-8') as f:
            arch = f.read()
            
    specs = agent.load_specifications(args.specs)
    
    # Load Template
    template_path = os.path.join(os.path.dirname(__file__), "templates", "epic_template.md")
    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()

    # Run Generation
    agent.generate_epics(prd, arch, specs, template_content, args.output)
    
    console.print(Panel.fit("[bold green]Decomposition Complete![/bold green]"))

    # --- JIRA INTEGRATION START ---
    if args.publish:
        if not args.project_key:
            console.print("[bold red]Error: --project_key is required when --publish is set.[/bold red]")
            return

        from jira_integration import get_jira_client, create_epic_in_jira
        
        console.print(Panel.fit(f"[bold blue]Publishing Epics to Jira Project: {args.project_key}[/bold blue]"))
        
        jira_client = get_jira_client()
        if not jira_client:
            console.print("[red]Aborting Jira publish due to connection checks.[/red]")
            return

        # Iterate over generated files in output directory
        import glob
        import re
        
        epic_files = glob.glob(os.path.join(args.output, "*.md"))
        for file_path in sorted(epic_files):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Simple metadata extraction
            # Assuming format: "# Epic: [ID] - [Title]" or similar
            # We want the content *after* the title line for description vs *in* the title line for summary.
            lines = content.split('\n')
            title_line = lines[0].strip()
            
            # Clean title: Remove "# Epic:" prefix
            # Example: "# Epic: USR-001 - User Login" -> "USR-001 - User Login"
            summary = re.sub(r'^#\s*Epic:?\s*', '', title_line, flags=re.IGNORECASE).strip()
            
            # Description is the rest
            description = "\n".join(lines[1:]).strip()
            
            epic_data = {
                'summary': summary,
                'description': description, # Jira handles markdown mostly OK, or robust converters can be used.
                'epic_name': summary # Reuse summary for Epic Name for simplicity
            }
            
            console.print(f"Publishing: {summary}...")
            create_epic_in_jira(jira_client, args.project_key, epic_data)

    # --- JIRA INTEGRATION END ---

    console.print("[bold green]All tasks finished.[/bold green]")

if __name__ == "__main__":
    import glob
    main()
