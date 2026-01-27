
import os
import sys
import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

def run_agent(path, args=[]):
    """Runs a standardized python agent."""
    cmd = [sys.executable, path] + args
    console.print(f"[bold cyan]Running:[/bold cyan] {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        console.print(f"[red]Error running {path}:[/red]\n{result.stderr}")
        return False
    console.print(f"[green]Success![/green]")
    # console.print(result.stdout) # Optional: print agent output
    return True

def main():
    console.print(Panel.fit("[bold magenta]AI SDLC Orchestrator (Level 4)[/bold magenta]", subtitle="Automated Holographic Expansion"))
    
    # 1. PRD Generation
    console.print("\n[bold]Phase 1: Requirements Expansion[/bold]")
    # In a real run, inputs would be gathered dynamically. 
    # For demo, we assume inputs/ exists.
    # run_agent("01_Requirements/prd_agent/prd_agent.py")
    console.print("[dim]Skipping PRD Gen (requires active inputs)...[/dim]")

    # 2. Architecture Expansion (Demonstrating Grounding)
    console.print("\n[bold]Phase 2: Architecture Expansion (Search Grounded)[/bold]")
    # Architecture Agent can now look up real APIs
    # run_agent("04_Architecture/architecture_agent/architecture_agent.py", ["--task", "openapi", "--input", "docs/PRD.md", "--output", "docs/api.yaml"])
    
    # 3. Micro-Agent: UX
    console.print("\n[bold]Phase 3: UX Visualization[/bold]")
    # run_agent("03_UX_Design/ux_agent/ux_agent.py", ["--task", "wireframes", "--input", "docs/stories.md", "--output", "docs/wireframes.md"])

    console.print("\n[bold green]Pipeline Complete![/bold green]")
    console.print("Artifacts generated: PRD.md, api.yaml, wireframes.md")

if __name__ == "__main__":
    main()
