# Interface Agent
# Discovers, documents, and generates tests for system interfaces

import os
import sys
import argparse

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '00_Introduction', 'standards'))

from genai_agent_base import GenAIBaseAgent
from rich.console import Console

console = Console()

SYSTEM_PROMPT = """
You are an Enterprise Integration Architect specializing in interface management.

You help teams:
1. Discover all system interfaces (APIs, files, events)
2. Document interface specifications
3. Generate interface contract tests

You understand:
- REST, gRPC, SOAP, GraphQL APIs
- File-based integrations (SFTP, S3, FTP, email)
- Event-driven architectures (Pub/Sub, Kafka, webhooks)
- Data mapping and transformation
- Error handling and retry patterns
"""


class InterfaceAgent(GenAIBaseAgent):
    """
    Interface Agent for discovering and documenting system integrations.
    Handles APIs, file-based transfers, and event-driven interfaces.
    """
    
    def __init__(self):
        super().__init__(system_instruction=SYSTEM_PROMPT)
        self.prompts_dir = os.path.join(os.path.dirname(__file__), 'prompts')
    
    def _load_prompt(self, filename: str) -> str:
        path = os.path.join(self.prompts_dir, filename)
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            console.print(f"[yellow]Warning: Prompt not found: {path}[/yellow]")
            return None
    
    def discover_interfaces(self, prd_path: str, output_dir: str, architecture_path: str = None) -> str:
        """Discover all interfaces from PRD and architecture docs."""
        
        with open(prd_path, 'r', encoding='utf-8') as f:
            prd_content = f.read()
        
        arch_content = ""
        if architecture_path and os.path.exists(architecture_path):
            with open(architecture_path, 'r', encoding='utf-8') as f:
                arch_content = f.read()
        
        prompt_template = self._load_prompt("INT_DISCOVER-interface-discovery.md")
        
        if prompt_template:
            prompt = prompt_template.replace("{{PRD_CONTENT}}", prd_content)
            prompt = prompt.replace("{{ARCHITECTURE_CONTENT}}", arch_content or "Not provided")
        else:
            prompt = f"""
Analyze this PRD and discover all system interfaces:

PRD:
{prd_content}

Architecture (if available):
{arch_content or "Not provided"}

Generate:
1. A Mermaid C4 Context Diagram showing all external systems
2. An Interface Catalog table with ID, System, Type, Direction, Protocol, Frequency, Owner
3. Discovery notes identifying unknowns

Interface types to look for:
- APIs (REST, gRPC, SOAP)
- File-based (SFTP, S3, FTP)
- Events (Pub/Sub, Kafka, webhooks)
"""
        
        console.print("[bold blue]Discovering system interfaces...[/bold blue]")
        response = self.generate(prompt, temperature=0.2)
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Save context diagram
        context_path = os.path.join(output_dir, "context-diagram.md")
        catalog_path = os.path.join(output_dir, "interface-catalog.md")
        
        # Extract and save catalog
        with open(catalog_path, 'w', encoding='utf-8') as f:
            f.write("# Interface Catalog\n\n")
            f.write(f"Source: {prd_path}\n\n")
            f.write("---\n\n")
            f.write(response)
        
        console.print(f"[green]Saved: {catalog_path}[/green]")
        return catalog_path
    
    def generate_spec(self, interface_id: str, system_name: str, existing_docs_path: str, output_dir: str) -> str:
        """Generate detailed interface specification."""
        
        existing_docs = ""
        if existing_docs_path and os.path.exists(existing_docs_path):
            with open(existing_docs_path, 'r', encoding='utf-8') as f:
                existing_docs = f.read()
        
        prompt_template = self._load_prompt("INT_SPEC-interface-specification.md")
        
        if prompt_template:
            prompt = prompt_template.replace("{{INTERFACE_ID}}", interface_id)
            prompt = prompt.replace("{{SYSTEM_NAME}}", system_name)
            prompt = prompt.replace("{{EXISTING_DOCS}}", existing_docs or "Not provided")
        else:
            prompt = f"""
Generate a detailed interface specification for:

Interface ID: {interface_id}
System: {system_name}

Existing Documentation:
{existing_docs or "Not provided"}

Include:
- Overview (type, direction, protocol, auth)
- Endpoints OR File Schema OR Event Schema
- Data Mapping
- Error Handling
- Changes Required in other system
"""
        
        console.print(f"[bold blue]Generating spec for {interface_id}: {system_name}...[/bold blue]")
        response = self.generate(prompt, temperature=0.2)
        
        os.makedirs(output_dir, exist_ok=True)
        safe_name = system_name.lower().replace(" ", "-")
        output_path = os.path.join(output_dir, f"{interface_id}-{safe_name}.md")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(response)
        
        console.print(f"[green]Saved: {output_path}[/green]")
        return output_path
    
    def generate_tests(self, spec_path: str, output_dir: str) -> str:
        """Generate contract tests from interface specification."""
        
        with open(spec_path, 'r', encoding='utf-8') as f:
            spec_content = f.read()
        
        prompt_template = self._load_prompt("INT_TEST-interface-tests.md")
        
        if prompt_template:
            prompt = prompt_template.replace("{{INTERFACE_SPEC}}", spec_content)
        else:
            prompt = f"""
Generate contract tests for this interface specification:

{spec_content}

Include:
- Contract tests (Pact for APIs, pandera for files)
- Mock configuration
- Integration test patterns
- Error handling tests
"""
        
        console.print("[bold blue]Generating contract tests...[/bold blue]")
        response = self.generate(prompt, temperature=0.2)
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Extract interface ID from spec path
        spec_name = os.path.basename(spec_path).replace(".md", "")
        output_path = os.path.join(output_dir, f"test_{spec_name}.md")
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Interface Contract Tests\n\n")
            f.write(f"Source: {spec_path}\n\n")
            f.write("---\n\n")
            f.write(response)
        
        console.print(f"[green]Saved: {output_path}[/green]")
        return output_path


def main():
    parser = argparse.ArgumentParser(description="Interface Agent - Discover, Spec, Test")
    parser.add_argument("--task", choices=['discover', 'spec', 'test'], required=True)
    parser.add_argument("--input", required=True, help="Input file (PRD, existing docs, or spec)")
    parser.add_argument("--arch", help="Architecture docs (for discover task)")
    parser.add_argument("--id", help="Interface ID (for spec task)")
    parser.add_argument("--system", help="System name (for spec task)")
    parser.add_argument("--output", default="docs/interfaces", help="Output directory")
    args = parser.parse_args()
    
    agent = InterfaceAgent()
    
    if args.task == 'discover':
        agent.discover_interfaces(args.input, args.output, args.arch)
    elif args.task == 'spec':
        if not args.id or not args.system:
            console.print("[red]Error: --id and --system required for spec task[/red]")
            return
        agent.generate_spec(args.id, args.system, args.input, args.output)
    elif args.task == 'test':
        agent.generate_tests(args.input, args.output)


if __name__ == "__main__":
    main()
