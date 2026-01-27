import os
import re
import datetime
from typing import List, Dict, Any
from rich.console import Console

console = Console()

class FollowUpManager:
    """
    Manages a persistent list of 'Open Questions' or 'Follow-Up Items' 
    across agent sessions.
    
    Uses MARKDOWN (.md) format for human readability AND machine parsing.
    """
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        self.filepath = os.path.join(output_dir, "open_questions.md")
        self.items = self._load()

    def _load(self) -> List[Dict]:
        """Parses the Markdown table into a list of dicts."""
        if not os.path.exists(self.filepath):
            return []
        
        items = []
        try:
            with open(self.filepath, 'r') as f:
                content = f.read()
            
            # Parse table rows (skip header and separator)
            lines = content.strip().split('\n')
            for line in lines:
                if line.startswith('|') and not line.startswith('| ID') and '---' not in line:
                    parts = [p.strip() for p in line.split('|')[1:-1]]  # Remove first/last empty
                    if len(parts) >= 4:
                        items.append({
                            "id": int(parts[0]),
                            "question": parts[1],
                            "status": parts[2],
                            "context": parts[3],
                            "created_at": parts[4] if len(parts) > 4 else ""
                        })
        except Exception as e:
            console.print(f"[yellow]Warning: Could not load {self.filepath}: {e}[/yellow]")
        return items

    def _save(self):
        """Saves items as a Markdown table."""
        os.makedirs(self.output_dir, exist_ok=True)
        
        lines = [
            "# Open Questions (Follow-Up Items)",
            "",
            "| ID | Question | Status | Context | Created |",
            "|----|----------|--------|---------|---------|"
        ]
        for item in self.items:
            lines.append(f"| {item['id']} | {item['question']} | {item['status']} | {item.get('context', '')} | {item.get('created_at', '')} |")
        
        with open(self.filepath, 'w') as f:
            f.write('\n'.join(lines) + '\n')

    def add_item(self, question: str, context: str = ""):
        """Adds a new question to the parking lot."""
        item = {
            "id": len(self.items) + 1,
            "question": question,
            "status": "🟡 Open",
            "context": context,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d")
        }
        self.items.append(item)
        self._save()
        console.print(f"[green]✓ Parked question:[/green] '{question}'")

    def get_open_items(self) -> List[Dict]:
        return [i for i in self.items if 'Open' in i.get('status', '')]

    def resolve_item(self, item_id: int, answer: str):
        """Marks an item as resolved."""
        for item in self.items:
            if item['id'] == item_id:
                item['status'] = '✅ Resolved'
                item['answer'] = answer
                self._save()
                return item
        return None

    def prompt_for_updates(self) -> str:
        """
        Interactive prompt to ask user about open items.
        Returns a context string of resolved items to be fed into the AI.
        """
        open_items = self.get_open_items()
        if not open_items:
            return ""

        console.print(f"\n[bold yellow]🔔 You have {len(open_items)} Open Questions from previous sessions.[/bold yellow]")
        console.print(f"[dim]See: {self.filepath}[/dim]")
        if console.input("[bold]Review them now? (y/n): [/bold]").lower() != 'y':
            return ""

        updates = []
        for item in open_items:
            console.print(f"\n[cyan]Q: {item['question']}[/cyan]")
            console.print(f"[dim]Context: {item.get('context', 'N/A')}[/dim]")
            ans = console.input("[bold]Enter answer (or Press Enter to skip): [/bold]")
            
            if ans.strip():
                self.resolve_item(item['id'], ans)
                updates.append(f"Q: {item['question']}\nA: {ans} (Resolved)")
                console.print("[green]✓ Marked as resolved.[/green]")
        
        if updates:
            return "\n\n*** UPDATES TO FOLLOW-UP ITEMS ***\n" + "\n".join(updates) + "\n"
        return ""

