
import os
import argparse
import glob
from rich.console import Console
from rich.panel import Panel
from story_agent import StoryAgent

console = Console()

def main():
    parser = argparse.ArgumentParser(description="AI Agent to generate User Stories from Epics.")
    parser.add_argument("--epic", required=True, help="Path to Epic file or directory")
    parser.add_argument("--arch", required=True, help="Path to Architecture docs")
    parser.add_argument("--output", default="outputs/stories", help="Output directory")
    parser.add_argument("--model", default=None, help="Gemini model (default: env GEMINI_MODEL)")
    
    # Sync Args
    parser.add_argument("--sync", action="store_true", help="Sync to Jira")
    parser.add_argument("--project_key", help="Jira Project Key (Required for sync)")

    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)
    
    console.print(Panel.fit("[bold magenta]Starting Story Writing Agent[/bold magenta]"))

    # 1. Load Inputs
    files_to_process = []
    if os.path.isfile(args.epic):
        files_to_process.append(args.epic)
    else:
        files_to_process = glob.glob(os.path.join(args.epic, "*.md"))
        
    # Arch loading (simple)
    arch_content = ""
    if os.path.isfile(args.arch):
         with open(args.arch, 'r') as f: arch_content = f.read()
    else:
         for f in glob.glob(os.path.join(args.arch, "**/*.md"), recursive=True):
             with open(f, 'r') as r: arch_content += r.read() + "\n"

    # Template
    template_path = os.path.join(os.path.dirname(__file__), "templates", "story_template.md")
    with open(template_path, 'r') as f:
        template_content = f.read()

    agent = StoryAgent(model_name=args.model)

    # 2. Generate Stories
    for epic_file in files_to_process:
        console.print(f"Processing Epic: {epic_file}")
        with open(epic_file, 'r') as f:
            epic_content = f.read()
            
        agent.generate_stories(epic_content, arch_content, template_content, args.output)

    # 3. Sync (if requested)
    if args.sync:
        if not args.project_key:
            console.print("[red]Error: --project_key required for sync[/red]")
            return
            
        from jira_sync import sync_story_to_jira
        console.print("[bold blue]Starting Jira Sync...[/bold blue]")
        
        # Iterate over all stories in output dir
        story_files = glob.glob(os.path.join(args.output, "*.md"))
        for story_file in sorted(story_files):
            sync_story_to_jira(story_file, args.project_key)

    console.print(Panel.fit("[bold green]Story Agent Finished[/bold green]"))

if __name__ == "__main__":
    main()
