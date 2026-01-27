
import os
import argparse
import glob
from rich.console import Console
from rich.panel import Panel
from test_plan_agent import TestPlanAgent

console = Console()

def main():
    parser = argparse.ArgumentParser(description="AI Agent to generate Test Plans from User Stories.")
    parser.add_argument("--story", required=True, help="Path to User Story file or directory")
    parser.add_argument("--arch", required=True, help="Path to Architecture docs")
    parser.add_argument("--output", default="outputs/test_plans", help="Output directory")
    parser.add_argument("--model", default=None, help="Gemini model (default: GEMINI_MODEL env)")

    args = parser.parse_args()
    os.makedirs(args.output, exist_ok=True)
    
    console.print(Panel.fit("[bold magenta]Starting Test Plan Generation Agent[/bold magenta]"))

    # 1. Load Inputs
    files_to_process = []
    if os.path.isfile(args.story):
        files_to_process.append(args.story)
    else:
        files_to_process = glob.glob(os.path.join(args.story, "*.md"))
        
    # Arch loading
    arch_content = ""
    if os.path.isfile(args.arch):
         with open(args.arch, 'r') as f: arch_content = f.read()
    else:
         for f in glob.glob(os.path.join(args.arch, "**/*.md"), recursive=True):
             with open(f, 'r') as r: arch_content += r.read() + "\n"

    # Template
    template_path = os.path.join(os.path.dirname(__file__), "templates", "test_plan_template.md")
    with open(template_path, 'r') as f:
        template_content = f.read()

    agent = TestPlanAgent(model_name=args.model)

    # 2. Generate Plans
    for story_file in files_to_process:
        console.print(f"Processing Story: {story_file}")
        with open(story_file, 'r') as f:
            story_content = f.read()
            
        agent.generate_test_plan(story_content, arch_content, template_content, args.output)

    console.print(Panel.fit("[bold green]Test Plan Agent Finished[/bold green]"))

if __name__ == "__main__":
    main()
