
import os
import argparse
from rich.console import Console
from rich.panel import Panel
from architecture_agent import ArchitectureAgent

console = Console()

def main():
    parser = argparse.ArgumentParser(description="AI Agent to generate Architecture Artifacts from PRD.")
    parser.add_argument("--prd", required=True, help="Path to the approved PRD file")
    parser.add_argument("--guidelines", default="guidelines", help="Directory containing architecture guidelines")
    parser.add_argument("--output", default="outputs/architecture-hub", help="Directory to save architecture artifacts")
    parser.add_argument("--model", default=None, help="Gemini model to use (default: env GEMINI_MODEL)")
    parser.add_argument("--publish", action="store_true", help="Publish artifacts to Confluence")
    
    args = parser.parse_args()
    
    console.print(Panel.fit("[bold purple]Starting Architecture Agent[/bold purple]", subtitle="v1.0"))
    
    try:
        agent = ArchitectureAgent(model_name=args.model)
        
        # 1. Load PRD
        console.print(f"Reading PRD from: [bold]{args.prd}[/bold]")
        with open(args.prd, 'r', encoding='utf-8') as f:
            prd_content = f.read()

        # 2. Load Guidelines
        console.print(f"Reading Guidelines from: [bold]{args.guidelines}[/bold]")
        guidelines_content = agent.load_guidelines(args.guidelines)
        
        # 3. Generate Artifacts
        agent.analyze_prd_and_generate_artifacts(prd_content, guidelines_content, args.output)
        
        # 4. Publish to Confluence (Optional)
        if args.publish:
            console.print("[bold blue]Publishing artifacts to Confluence...[/bold blue]")
            try:
                # Add agents module to path for import
                import sys
                sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
                from agents.utils.confluence_utils import create_page
                
                import glob
                for md_file in glob.glob(os.path.join(args.output, "**", "*.md"), recursive=True):
                    with open(md_file, 'r') as f:
                        content = f.read()
                    title = os.path.basename(md_file).replace(".md", "").replace("-", " ").title()
                    create_page(title, content, "SD")
                    console.print(f"Published: {title}")
            except Exception as e:
                console.print(f"[red]Failed to publish to Confluence: {e}[/red]")

        console.print(Panel.fit("[bold green]Architecture Definition Complete![/bold green]"))

    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")

if __name__ == "__main__":
    main()
