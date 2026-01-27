import os
import datetime
from typing import List, Dict, Optional
from rich.console import Console

console = Console()


class SessionStateManager:
    """
    Manages persistent session state in Markdown files.
    - session_log.md: Appended at end of each session.
    - entities.md: Updated when entities are discovered.
    """

    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        self.session_log_path = os.path.join(output_dir, "session_log.md")
        self.entities_path = os.path.join(output_dir, "entities.md")

    # ─────────────────────────────────────────────────────────────
    # SESSION LOG
    # ─────────────────────────────────────────────────────────────

    def log_session(
        self,
        agent_name: str,
        tools_run: List[str],
        outcomes: List[str],
        questions_added: int = 0
    ):
        """
        Appends a session summary to session_log.md.
        Called at the END of an interactive session.
        """
        os.makedirs(self.output_dir, exist_ok=True)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        entry = f"""
## Session {timestamp}
**Agent:** {agent_name}
**Tools Run:** {', '.join(tools_run) if tools_run else 'None'}
**Key Outcomes:**
{chr(10).join(f'- {o}' for o in outcomes) if outcomes else '- No significant outcomes recorded.'}
**Open Questions Added:** {questions_added}

---
"""
        # Append to file (create with header if doesn't exist)
        if not os.path.exists(self.session_log_path):
            with open(self.session_log_path, 'w') as f:
                f.write("# Session Log\n\nThis file tracks all interactive agent sessions.\n\n---\n")

        with open(self.session_log_path, 'a') as f:
            f.write(entry)

        console.print(f"[green]✓ Session logged to {self.session_log_path}[/green]")

    # ─────────────────────────────────────────────────────────────
    # ENTITY REGISTRY
    # ─────────────────────────────────────────────────────────────

    def register_entity(
        self,
        name: str,
        discovered_in: str,
        operations: str = "",
        states: str = "",
        notes: str = ""
    ):
        """
        Adds or updates an entity in the entity registry.
        Called after CRUD or State analysis tools.
        """
        os.makedirs(self.output_dir, exist_ok=True)

        # Load existing entities
        entities = self._load_entities()

        # Check if entity already exists
        existing = next((e for e in entities if e['name'].lower() == name.lower()), None)
        if existing:
            # Update existing
            existing['operations'] = operations or existing.get('operations', '')
            existing['states'] = states or existing.get('states', '')
            existing['notes'] = notes or existing.get('notes', '')
            console.print(f"[yellow]✓ Updated entity: {name}[/yellow]")
        else:
            # Add new
            entities.append({
                'name': name,
                'discovered_in': discovered_in,
                'operations': operations,
                'states': states,
                'notes': notes
            })
            console.print(f"[green]✓ Registered new entity: {name}[/green]")

        self._save_entities(entities)

    def _load_entities(self) -> List[Dict]:
        """Parses entities.md into a list of dicts."""
        if not os.path.exists(self.entities_path):
            return []

        entities = []
        try:
            with open(self.entities_path, 'r') as f:
                content = f.read()

            lines = content.strip().split('\n')
            for line in lines:
                if line.startswith('|') and not line.startswith('| Entity') and '---' not in line:
                    parts = [p.strip() for p in line.split('|')[1:-1]]
                    if len(parts) >= 5:
                        entities.append({
                            'name': parts[0],
                            'discovered_in': parts[1],
                            'operations': parts[2],
                            'states': parts[3],
                            'notes': parts[4]
                        })
        except Exception as e:
            console.print(f"[yellow]Warning: Could not parse entities: {e}[/yellow]")

        return entities

    def _save_entities(self, entities: List[Dict]):
        """Saves entities as a Markdown table."""
        lines = [
            "# Entity Registry",
            "",
            "Domain entities discovered during requirements and elaboration sessions.",
            "",
            "| Entity | Discovered In | CRUD | States | Notes |",
            "|:-------|:--------------|:-----|:-------|:------|"
        ]
        for e in entities:
            lines.append(
                f"| {e['name']} | {e['discovered_in']} | {e['operations']} | {e['states']} | {e['notes']} |"
            )

        with open(self.entities_path, 'w') as f:
            f.write('\n'.join(lines) + '\n')

    def get_all_entities(self) -> List[Dict]:
        """Returns all registered entities (for context injection)."""
        return self._load_entities()
