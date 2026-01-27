
import os
import re
from rich.console import Console

try:
    from jira import JIRA
except ImportError:
    JIRA = None

console = Console()

def get_jira_client():
    if JIRA is None:
        console.print("[red]Error: 'jira' library not installed.[/red]")
        return None
    
    server = os.getenv("JIRA_SERVER_URL")
    email = os.getenv("JIRA_USER_EMAIL")
    token = os.getenv("JIRA_API_TOKEN")
    
    if not all([server, email, token]):
        console.print("[red]Missing JIRA env vars.[/red]")
        return None
        
    return JIRA(server=server, basic_auth=(email, token))

def sync_story_to_jira(file_path: str, project_key: str):
    """
    Syncs a single markdown story file to Jira.
    1. Reads file.
    2. Checks for 'Jira Key' metadata.
    3. If Key exists -> Update Issue.
    4. If Key missing -> Create Issue -> Update File with Key.
    """
    client = get_jira_client()
    if not client:
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Parse Content
    lines = content.split('\n')
    
    # Metadata extraction
    jira_key = None
    epic_link = None
    summary = None
    
    # 1. Extract Header info
    # Format expected: # Story: [ID] - [Title]
    if lines[0].startswith("# Story:"):
        raw_summary = lines[0].replace("# Story:", "").replace("#", "").strip()
        summary = raw_summary
    
    # 2. Extract Metadata lines
    for line in lines:
        if line.startswith("**Jira Key**:") or line.startswith("Jira Key:"):
            val = line.split(":", 1)[1].strip()
            # If val looks like [JIRA-123], remove brackets
            val = val.replace("[", "").replace("]", "")
            if val and val.lower() != "pending" and val.lower() != "none" and "-" in val:
                jira_key = val
        
        if line.startswith("**Epic Link**:") or line.startswith("Epic Link:"):
             val = line.split(":", 1)[1].strip()
             if val and "-" in val:
                 epic_link = val # Note: Requires valid Jira Epic Key, not file path

    description = _extract_description(content)

    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Story'},
    }
    
    # Note: Epic Link field ID varies by instance. 
    # For MVP, we skip strictly linking unless we know the field ID or use 'parent' for Next-Gen.
    
    if jira_key:
        # UPDATE
        console.print(f"[blue]Updating existing issue {jira_key}...[/blue]")
        try:
            issue = client.issue(jira_key)
            issue.update(summary=summary, description=description)
            console.print(f"[green]Updated {jira_key}[/green]")
        except Exception as e:
            console.print(f"[red]Failed to update {jira_key}: {e}[/red]")
    else:
        # CREATE
        console.print(f"[blue]Creating new issue for '{summary}'...[/blue]")
        try:
            new_issue = client.create_issue(fields=issue_dict)
            new_key = new_issue.key
            console.print(f"[green]Created {new_key}[/green]")
            
            # WRITE BACK TO FILE
            _update_file_with_key(file_path, content, new_key)
            
        except Exception as e:
            console.print(f"[red]Failed to create issue: {e}[/red]")

def _extract_description(content):
    # Heuristic: Everything after the metadata block
    # We'll just return the whole thing for now, Jira handles Markdown 
    return content

def _update_file_with_key(file_path, original_content, new_key):
    """
    Replaces '**Jira Key**: [Pending]' (or similar) with '**Jira Key**: [PROJ-123]'
    """
    # Regex to find the Jira Key line
    # Matches: **Jira Key**: ... newline
    pattern = r"(\*\*Jira Key\*\*:)(.*)"
    
    if re.search(pattern, original_content):
        # Replace existing line
        new_content = re.sub(pattern, f"\\1 [{new_key}]", original_content)
    else:
        # Insert after title? Or just fail soft. 
        # Template has it, so we expect it.
        # Fallback: Insert after line 2
        lines = original_content.split('\n')
        lines.insert(2, f"**Jira Key**: [{new_key}]")
        new_content = "\n".join(lines)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    console.print(f"[yellow]Updated file {os.path.basename(file_path)} with key {new_key}[/yellow]")
