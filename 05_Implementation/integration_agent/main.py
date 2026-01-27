
import argparse
from integration_agent import IntegrationAgent
from rich.console import Console
from rich.panel import Panel

console = Console()

def main():
    parser = argparse.ArgumentParser(description="Integration Agent: AI CI/CD Orchestrator")
    parser.add_argument("--check-all", action="store_true", help="Run all checks (Artifacts, Tests, Governance)")
    parser.add_argument("--target", default=".", help="Target codebase directory (for Governance/Tests)")
    parser.add_argument("--artifacts-dir", default="../../", help="Base directory where agent outputs (epics, stories) are stored relative to this script")

    args = parser.parse_args()
    
    console.print(Panel.fit("[bold cyan]Starting Integration Agent[/bold cyan]", subtitle="CI/CD Orchestrator"))
    
    agent = IntegrationAgent()
    
    if args.check_all:
        # 1. Pipeline Artifacts
        # Adjust artifacts path. If main.py is in agents/integration_agent, ../../ is ai-development-methodology
        # But our outputs are usually in agents/XYZ/outputs. 
        # Let's assume the user runs this from project root or passes correct path.
        # For this demo, let's look at the 'outputs' directory in sibling agents.
        # Check logic in integration_agent expects "outputs/epics", etc.
        # We need to point it to where those actually live. 
        # Actually, our architecture has been scattering outputs: 
        # agents/epic_agent/outputs, agents/story_agent/outputs.
        # The check_pipeline_artifacts method assumes a single base with "outputs/epics". 
        # We might need to update that logic or provide a smarter path.
        # For now, let's pass the 'agents' directory and update logic to look recursively? 
        # Or just check specific known locations.
        pass
    
    # Let's actually execute the agent methods
    # Need to be clearer about paths.
    # Current structure:
    # agents/epic_agent/outputs/epics
    # agents/story_agent/outputs/stories
    
    # We will update the agent logic to be smarter, but for now let's invoke:
    
    import os
    base_dir = os.path.abspath(args.artifacts_dir) # Should be 'agents' folder roughly
    
    # 1. Artifact Check (We will need to subclass or custom pathing since outputs are scattered)
    # Let's just run it and let the user see the path warnings if paths are wrong.
    # To make it work for our specific folder structure:
    # We can perform checks on known relative paths from the 'agents' root.
    
    # Let's define the paths explicitly for this project structure
    # agents/epic_agent/outputs/epics
    
    agent.log("Starting Full Pipeline Check...", "INFO")
    
    # Custom artifact checking for our distributed agent structure
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # agents/
    
    epics = os.path.join(project_root, "epic_agent", "outputs", "epics", "*.md")
    stories = os.path.join(project_root, "story_agent", "outputs", "stories", "*.md")
    test_plans = os.path.join(project_root, "test_plan_agent", "outputs", "test_plans", "*.md")
    
    import glob
    if glob.glob(epics): agent.log(f"Found Epics.", "SUCCESS") 
    else: agent.log("Missing Epics.", "WARNING")
    
    if glob.glob(stories): agent.log(f"Found Stories.", "SUCCESS")
    else: agent.log("Missing Stories.", "WARNING")
    
    if glob.glob(test_plans): agent.log(f"Found Test Plans.", "SUCCESS")
    else: agent.log("Missing Test Plans.", "WARNING")

    # 2. Run Tests
    agent.run_tests(os.path.join(args.target, "tests"))
    
    # 3. Governance
    agent.run_governance(args.target)
    
    # 4. Report
    agent.generate_release_report()
    
    console.print(Panel.fit("[bold green]Integration Check Complete[/bold green]"))

if __name__ == "__main__":
    main()
