
import os
import argparse
from rich.console import Console
from rich.panel import Panel
from prd_agent import PRDAgent

console = Console()

def main():
    parser = argparse.ArgumentParser(description="AI Agent to generate PRDs from source documents.")
    parser.add_argument("--input", default="inputs", help="Directory containing source documents (default: inputs)")
    parser.add_argument("--output", default="outputs", help="Directory to save outputs (default: outputs)")
    parser.add_argument("--template", default="templates/prd_template.md", help="Path to PRD template")
    parser.add_argument("--model", default=None, help="Gemini model to use (default: env GEMINI_MODEL)")
    
    args = parser.parse_args()
    
    # Ensure output directory exists
    os.makedirs(args.output, exist_ok=True)
    
    console.print(Panel.fit("[bold green]Starting PRD Generation Agent[/bold green]", subtitle="v1.0"))
    
    try:
        agent = PRDAgent(model_name=args.model)
        
        # 1. Load Documents
        console.print(f"Reading documents from: [bold]{args.input}[/bold]")
        docs_content = agent.load_documents(args.input)
        
        if not docs_content:
            console.print("[red]No document content loaded. Exiting.[/red]")
            return

        # 2. Generate PRD
        prd_content = agent.generate_prd(docs_content, args.template)
        
        prd_path = os.path.join(args.output, "draft_prd.md")
        with open(prd_path, "w", encoding="utf-8") as f:
            f.write(prd_content)
        console.print(f"[bold green]PRD generated successfully![/bold green] Saved to: {prd_path}")
        
        # 3. Gap Analysis
        gap_report = agent.identify_gaps(prd_content)
        
        gap_path = os.path.join(args.output, "gap_analysis.md")
        with open(gap_path, "w", encoding="utf-8") as f:
            f.write(gap_report)
        console.print(f"[bold green]Gap analysis completed![/bold green] Saved to: {gap_path}")
        
        console.print(Panel.fit("[bold green]Workflow Complete![/bold green]"))

    except Exception as e:
        console.print(f"[bold red]An error occurred:[/bold red] {e}")

if __name__ == "__main__":
    main()
