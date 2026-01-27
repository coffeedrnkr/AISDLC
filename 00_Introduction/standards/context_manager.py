"""
Context Manager for AI Agents

Handles large document loading with:
- Smart chunking by function/class
- Token counting and limits
- Summarization fallback for oversized content
- Caching for repeated access
"""

import os
import re
import hashlib
from typing import List, Dict, Optional, Tuple
from pathlib import Path
from rich.console import Console

console = Console()


class ContextManager:
    """
    Manages context loading for AI agents.
    Prevents context window overflow and optimizes token usage.
    """

    def __init__(
        self,
        max_tokens: int = 100000,
        cache_dir: str = ".context_cache"
    ):
        self.max_tokens = max_tokens
        self.cache_dir = cache_dir
        self._cache = {}

    def estimate_tokens(self, text: str) -> int:
        """
        Estimate token count for text.
        Rough heuristic: ~4 characters per token for English.
        """
        return len(text) // 4

    def load_documents(
        self,
        paths: List[str],
        prioritize: List[str] = None,
        max_per_file: int = 10000
    ) -> str:
        """
        Load multiple documents with smart handling.
        
        Args:
            paths: List of file paths to load
            prioritize: Keywords to prioritize (files containing these load first)
            max_per_file: Maximum characters per file (truncate larger files)
        
        Returns:
            Combined document content as a string
        """
        documents = []
        total_tokens = 0
        
        # Sort by priority if specified
        if prioritize:
            paths = self._prioritize_paths(paths, prioritize)
        
        for path in paths:
            if not os.path.exists(path):
                console.print(f"[yellow]Warning: {path} not found, skipping[/yellow]")
                continue
            
            content = self._load_file(path, max_per_file)
            file_tokens = self.estimate_tokens(content)
            
            # Check if we're approaching the limit
            if total_tokens + file_tokens > self.max_tokens:
                console.print(f"[yellow]Token limit approaching, summarizing {path}[/yellow]")
                content = self._summarize_content(content, self.max_tokens - total_tokens)
                file_tokens = self.estimate_tokens(content)
            
            documents.append(f"## File: {path}\n\n{content}\n\n---\n")
            total_tokens += file_tokens
            
            if total_tokens >= self.max_tokens:
                console.print(f"[yellow]Token limit reached, stopping at {len(documents)} files[/yellow]")
                break
        
        combined = "\n".join(documents)
        console.print(f"[dim]Loaded {len(documents)} documents (~{total_tokens} tokens)[/dim]")
        
        return combined

    def _load_file(self, path: str, max_chars: int) -> str:
        """Load a single file, truncating if necessary."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if len(content) > max_chars:
                # Smart truncation: try to find a good break point
                truncated = content[:max_chars]
                last_newline = truncated.rfind('\n')
                if last_newline > max_chars * 0.8:
                    truncated = truncated[:last_newline]
                return truncated + f"\n\n[TRUNCATED: {len(content) - len(truncated)} chars omitted]"
            
            return content
        except Exception as e:
            return f"[Error loading file: {e}]"

    def _prioritize_paths(self, paths: List[str], keywords: List[str]) -> List[str]:
        """Sort paths by relevance to keywords."""
        def score(path: str) -> int:
            name = os.path.basename(path).lower()
            return sum(1 for kw in keywords if kw.lower() in name)
        
        return sorted(paths, key=score, reverse=True)

    def _summarize_content(self, content: str, max_tokens: int) -> str:
        """
        Create a summary of content to fit within token limit.
        This is a simple extractive summary - could be enhanced with AI.
        """
        max_chars = max_tokens * 4
        
        if len(content) <= max_chars:
            return content
        
        # Extract key sections (headings and first lines)
        lines = content.split('\n')
        summary_lines = []
        char_count = 0
        
        for line in lines:
            # Prioritize headings
            if line.startswith('#') or line.startswith('def ') or line.startswith('class '):
                if char_count + len(line) < max_chars:
                    summary_lines.append(line)
                    char_count += len(line)
            # Include some context
            elif len(summary_lines) < 50 and char_count + len(line) < max_chars:
                summary_lines.append(line)
                char_count += len(line)
        
        return '\n'.join(summary_lines) + "\n\n[SUMMARIZED: Original was much longer]"

    def chunk_by_structure(self, content: str, file_type: str = "python") -> List[Dict]:
        """
        Split content into logical chunks (functions, classes, sections).
        
        Returns list of dicts with {name, content, tokens}
        """
        chunks = []
        
        if file_type == "python":
            # Split by function/class definitions
            pattern = r'^((?:def |class |async def )\w+.*?)(?=^(?:def |class |async def )|\Z)'
            matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
            
            for match in matches:
                chunks.append({
                    "name": self._extract_name(match),
                    "content": match.strip(),
                    "tokens": self.estimate_tokens(match)
                })
        
        elif file_type == "markdown":
            # Split by headings
            pattern = r'^(#{1,3} .+?)(?=^#{1,3} |\Z)'
            matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
            
            for match in matches:
                chunks.append({
                    "name": match.split('\n')[0].strip('#').strip(),
                    "content": match.strip(),
                    "tokens": self.estimate_tokens(match)
                })
        
        return chunks

    def _extract_name(self, code: str) -> str:
        """Extract function/class name from code."""
        match = re.match(r'(?:def |class |async def )(\w+)', code)
        return match.group(1) if match else "unknown"

    def get_relevant_chunks(
        self,
        chunks: List[Dict],
        query: str,
        max_tokens: int = 50000
    ) -> List[Dict]:
        """
        Select most relevant chunks for a query.
        Simple keyword matching - could be enhanced with embeddings.
        """
        # Score chunks by query relevance
        query_words = set(query.lower().split())
        
        for chunk in chunks:
            chunk_words = set(chunk["content"].lower().split())
            chunk["relevance"] = len(query_words & chunk_words)
        
        # Sort by relevance
        sorted_chunks = sorted(chunks, key=lambda x: x["relevance"], reverse=True)
        
        # Select top chunks within token limit
        selected = []
        total_tokens = 0
        
        for chunk in sorted_chunks:
            if total_tokens + chunk["tokens"] <= max_tokens:
                selected.append(chunk)
                total_tokens += chunk["tokens"]
        
        return selected


class TokenBudget:
    """Track and manage token usage across a session."""

    def __init__(self, budget: int = 500000):
        self.budget = budget
        self.used = 0
        self.history = []

    def spend(self, tokens: int, description: str = ""):
        """Record token usage."""
        self.used += tokens
        self.history.append({
            "tokens": tokens,
            "description": description,
            "remaining": self.budget - self.used
        })

    def remaining(self) -> int:
        """Get remaining token budget."""
        return self.budget - self.used

    def check(self, needed: int) -> bool:
        """Check if we have enough budget for an operation."""
        return self.used + needed <= self.budget

    def report(self) -> str:
        """Generate usage report."""
        return f"Token Budget: {self.used:,} / {self.budget:,} ({100 * self.used / self.budget:.1f}% used)"
