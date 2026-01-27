
import os
import sys
from typing import Dict, Any, Optional
from rich.console import Console

# Import the JIRA library
try:
    from jira import JIRA
except ImportError:
    JIRA = None

console = Console()

def get_jira_client() -> Optional[Any]:
    """
    Returns an authenticated Jira client using API Token.
    Checks environment variables: JIRA_SERVER_URL, JIRA_USER_EMAIL, JIRA_API_TOKEN.
    """
    if JIRA is None:
        console.print("[red]Error: 'jira' library not installed. Please run: pip install jira[/red]")
        return None

    server_url = os.getenv("JIRA_SERVER_URL")
    email = os.getenv("JIRA_USER_EMAIL")
    token = os.getenv("JIRA_API_TOKEN")
    
    if not all([server_url, email, token]):
        console.print("[red]Missing JIRA environment variables (JIRA_SERVER_URL, JIRA_USER_EMAIL, JIRA_API_TOKEN).[/red]")
        return None
        
    try:
        jira = JIRA(server=server_url, basic_auth=(email, token))
        # Simple existence check
        user = jira.myself()
        console.print(f"[green]Connected to Jira as: {user['displayName']}[/green]")
        return jira
    except Exception as e:
        console.print(f"[red]Failed to connect to Jira: {e}[/red]")
        return None

def create_epic_in_jira(client, project_key: str, epic_data: Dict[str, Any]) -> Optional[str]:
    """
    Creates an Epic issue in Jira.
    
    Args:
        client: Authenticated JIRA client object.
        project_key: The Project Key (e.g., 'PROJ') where the Epic should be created.
        epic_data: Dict containing 'summary', 'description'.
                   Optional: 'epic_name' (if different from summary).
    
    Returns:
        The Key of the created Epic (e.g., 'PROJ-123') or None if failed.
    """
    if not client:
        return None
    
    summary = epic_data.get('summary')
    description = epic_data.get('description', '')
    # For Epics, 'Epic Name' is often required and distinct from Summary. Default to Summary if missing.
    epic_name = epic_data.get('epic_name', summary) 

    # --- Epic Name Field Discovery ---
    # In Jira Cloud Next-Gen, 'Epic Name' might not be needed (uses Summary).
    # In Classic, it is a custom field. We try to find it or use a user-provided env var.
    epic_name_field_id = os.getenv("JIRA_EPIC_NAME_FIELD_ID")
    
    # If not provided, try to find it (simple heuristic)
    if not epic_name_field_id:
        # Common IDs, but dangerous to guess. 
        # Better heuristic: Let's defer strict field finding for now to keep it simple.
        # If creation fails, we warn the user.
        # However, for Classic projects, it IS required.
        pass

    issue_dict = {
        'project': {'key': project_key},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Epic'},
    }

    # Add Epic Name if we have the field ID
    if epic_name_field_id:
        issue_dict[epic_name_field_id] = epic_name

    try:
        new_issue = client.create_issue(fields=issue_dict)
        console.print(f"[bold green]Successfully created Epic: {new_issue.key} ({server_url}/browse/{new_issue.key})[/bold green]")
        return new_issue.key
    except Exception as e:
        # Fallback: Maybe it failed because of the Epic Name field?
        if "Epic Name" in str(e) and not epic_name_field_id:
             console.print("[yellow]Failed. Retrying: Attempting to find 'Epic Name' custom field...[/yellow]")
             found_field_id = _find_epic_name_field(client)
             if found_field_id:
                 issue_dict[found_field_id] = epic_name
                 try:
                     new_issue = client.create_issue(fields=issue_dict)
                     console.print(f"[bold green]Successfully created Epic: {new_issue.key}[/bold green]")
                     return new_issue.key
                 except Exception as e2:
                     console.print(f"[red]Retry failed: {e2}[/red]")
             else:
                 console.print(f"[red]Could not find 'Epic Name' field. Error: {e}[/red]")
        else:
            console.print(f"[red]Failed to create Epic '{summary}': {e}[/red]")
        return None

def _find_epic_name_field(client) -> Optional[str]:
    """Helper to search for the custom field 'Epic Name'."""
    try:
        fields = client.fields()
        for field in fields:
            if field['name'] == 'Epic Name':
                return field['id']
    except Exception:
        pass
    return None

# Access global server_url for printing link
server_url = os.getenv("JIRA_SERVER_URL", "")
