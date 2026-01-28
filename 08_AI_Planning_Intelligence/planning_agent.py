#!/usr/bin/env python3
"""
AI Planning Intelligence Agent (Pillar 8)
-----------------------------------------
This agent provides continuous monitoring and management of dependencies across Jira backlogs.
It implements the 4 Dimensions of AI Planning Intelligence:
1. Discovery
2. Monitoring
3. Sequencing
4. Prediction

Usage:
    python planning_agent.py discover <story_file_or_text>
    python planning_agent.py health <sprint_id_or_file>
    python planning_agent.py sequence <stories_file>
    python planning_agent.py readiness <sprint_id>
"""

import argparse
import sys
import json
import time
import random
from datetime import datetime, timedelta

# --- MOCK JIRA INTEGRATION ---

class MockJiraService:
    """
    Simulates interaction with a Jira instance.
    In a real implementation, this would use the Jira REST API.
    """
    
    def __init__(self):
        self.stories = {
            "CORE-456": {"summary": "API: Add status field", "status": "In Progress", "points": 3},
            "DB-078": {"summary": "Database: Schema migration", "status": "Done", "points": 2},
            "PORTAL-123": {"summary": "Dashboard status display", "status": "To Do", "points": 3, "dependencies": ["CORE-456"]},
            "PORTAL-124": {"summary": "Filter by policy status", "status": "To Do", "points": 2, "dependencies": ["PORTAL-123"]},
        }
        
    def get_story(self, issue_key):
        return self.stories.get(issue_key)
        
    def search_issues(self, jql):
        # Simulate a search returning relevant stories
        return list(self.stories.values())

# --- AGENT LOGIC ---

class PlanningAgent:
    def __init__(self):
        self.jira = MockJiraService()
        self.colors = {
            "RED": "\033[91m",
            "YELLOW": "\033[93m",
            "GREEN": "\033[92m",
            "RESET": "\033[0m"
        }

    def _print_header(self, title):
        print(f"\n{'='*60}")
        print(f" {title}")
        print(f"{'='*60}\n")

    def discover_dependencies(self, content):
        """
        Analyzes text to infer dependencies using simulated NLP.
        """
        self._print_header("DEPENDENCY DISCOVERY")
        print(f"Analyzing content: \"{content[:50]}...\"\n")
        
        # Simulated NLP findings
        findings = []
        if "policy status" in content.lower():
            findings.append({
                "type": "Predecessor",
                "issue": "CORE-456",
                "summary": "API: Add status field",
                "confidence": "High",
                "reason": "Content mentions 'policy status' which requires the API update in CORE-456"
            })
        if "dashboard" in content.lower():
             findings.append({
                "type": "Technical",
                "issue": "LIB-001",
                "summary": "Dashboard Component Library",
                "confidence": "Medium",
                "reason": "UI work typically requires component library update"
            })
            
        if not findings:
            print("No obvious dependencies found in simulated analysis.")
            return

        print("POTENTIAL DEPENDENCIES DETECTED:\n")
        for f in findings:
            color = self.colors["RED"] if f["confidence"] == "High" else self.colors["YELLOW"]
            print(f"{color}[{f['confidence']}] {f['type']}: {f['issue']} - {f['summary']}{self.colors['RESET']}")
            print(f"   Reason: {f['reason']}\n")

    def check_health(self, sprint_id):
        """
        Checks the dependency health of a sprint.
        """
        self._print_header(f"HEALTH CHECK: {sprint_id}")
        
        # Simulate sprint data
        sprint_stories = ["PORTAL-123", "PORTAL-124", "CORE-456"]
        
        print(f"Analyzing {len(sprint_stories)} stories in {sprint_id}...\n")
        time.sleep(1) # Simulate simulation
        
        conflicts = []
        risks = []
        healthy = []
        
        # Hardcoded analysis logic for demo
        # PORTAL-124 depends on 123 (same sprint -> Risk)
        risks.append({
            "story": "PORTAL-124", 
            "dep": "PORTAL-123", 
            "reason": "Dependency in same sprint (tight coupling)"
        })
        
        # CORE-456 depends on DB-078 (Done -> Healthy)
        healthy.append({
            "story": "CORE-456",
            "dep": "DB-078",
            "reason": "Dependency is Status: Done"
        })
        
        # Simulated Conflict
        conflicts.append({
            "story": "PORTAL-123",
            "dep": "EXT-999",
            "reason": "External dependency EXT-999 is BLOCKED"
        })

        # Output
        print(f"{self.colors['RED']}🔴 CONFLICTS (Action Required):{self.colors['RESET']}")
        for c in conflicts:
            print(f"  • {c['story']} blocked by {c['dep']}: {c['reason']}")
            
        print(f"\n{self.colors['YELLOW']}🟡 RISKS (Monitor Closely):{self.colors['RESET']}")
        for r in risks:
            print(f"  • {r['story']} depends on {r['dep']}: {r['reason']}")
            
        print(f"\n{self.colors['GREEN']}🟢 HEALTHY:{self.colors['RESET']}")
        for h in healthy:
            print(f"  • {h['story']} -> {h['dep']}: {h['reason']}")

    def sequence_work(self, stories_file):
        """
        Recommends optimal build order via topological sort simulation.
        """
        self._print_header("OPTIMAL SEQUENCING")
        
        # Normally would read file, here we mock
        print("Building dependency graph...")
        print("Calculating critical path...\n")
        
        phases = [
            {"phase": 1, "days": "1-3", "stories": ["CORE-456 (API)", "DB-Migrate"]},
            {"phase": 2, "days": "4-6", "stories": ["PORTAL-123 (UI)", "REPORT-Gen"]},
            {"phase": 3, "days": "7-10", "stories": ["PORTAL-124 (Filter)", "E2E-Tests"]}
        ]
        
        for p in phases:
            print(f"PHASE {p['phase']} (Days {p['days']}):")
            for s in p['stories']:
                print(f"  [ ] {s}")
            print("")
            
        print(f"{self.colors['YELLOW']}CRITICAL PATH:{self.colors['RESET']} DB-Migrate -> CORE-456 -> PORTAL-123 -> E2E-Tests")

    def check_readiness(self, sprint_id):
        """
        Go/No-Go assessment for a sprint.
        """
        self._print_header(f"SPRINT READINESS: {sprint_id}")
        
        print("Checking prerequisites...")
        print("Validating external commitments...")
        print("Analyzing team capacity...\n")
        
        print(f"{self.colors['YELLOW']}⚠️  RECOMMENDATION: CONDITIONAL GO{self.colors['RESET']}")
        print("\nConditions:")
        print("1. Confirm EXT-999 unblocked date with Platform Team")
        print("2. Move PORTAL-124 to end of sprint to allow buffer")

# --- CLI ENTRY POINT ---

def main():
    parser = argparse.ArgumentParser(description="AI Planning Intelligence Agent")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Discover Command
    discover_parser = subparsers.add_parser("discover", help="Discover dependencies in text/story")
    discover_parser.add_argument("input", help="Text content or file path to analyze")
    
    # Health Command
    health_parser = subparsers.add_parser("health", help="Check sprint/backlog health")
    health_parser.add_argument("sprint_id", help="Jira Sprint ID or Name")
    
    # Sequence Command
    seq_parser = subparsers.add_parser("sequence", help="Recommend build sequence")
    seq_parser.add_argument("file", help="List of stories to sequence")
    
    # Readiness Command
    ready_parser = subparsers.add_parser("readiness", help="Assess sprint readiness")
    ready_parser.add_argument("sprint_id", help="Jira Sprint ID")

    args = parser.parse_args()
    agent = PlanningAgent()

    if args.command == "discover":
        # Check if input is a file
        content = args.input
        try:
            with open(args.input, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            pass # Treat as raw text
        agent.discover_dependencies(content)
        
    elif args.command == "health":
        agent.check_health(args.sprint_id)
        
    elif args.command == "sequence":
        agent.sequence_work(args.file)
        
    elif args.command == "readiness":
        agent.check_readiness(args.sprint_id)
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
