#!/usr/bin/env python3
"""
Audit Agent (Project Dashboard)
-------------------------------
Agent ID: AUDIT_001
Mission: "One Board to Rule Them All."

This agent scans the entire project to build a "Proof of State".
It does NOT rely on human reporting. It relies on:
1. File Existence (Is the code there?)
2. Traceability Tags (Is it linked?)
3. Tests (Does it pass?)
4. Linter/Stat Analysis (Is it consistent?)

Usage:
    python3 09_Audit_and_Governance/project_dashboard_agent.py

Output:
    PROJECT_DASHBOARD.md
"""

import os
import re
import sys
import glob
from datetime import datetime

# --- CONFIGURATION ---
PROJECT_ROOT = "." # Assumes run from root
DASHBOARD_FILE = "PROJECT_DASHBOARD.md"

class Artifact:
    def __init__(self, filepath, type):
        self.filepath = filepath
        self.type = type
        self.id = self._extract_id()
        self.parent_id = self._extract_parent()
        self.status = "UNKNOWN"
        self.quality_score = 0
        self.issues = []

    def _extract_id(self):
        """Extracts ID based on file type standard."""
        try:
            with open(self.filepath, 'r') as f:
                content = f.read()
                
            if self.type == "PY":
                # Look for @implements <ID> (Primary) or just defining the ID if it's not code? 
                # Actually code implements a Requirement. It doesn't usually HAVE an ID itself unless it's a module.
                # Let's say Code ID is the filename
                return os.path.basename(self.filepath)
            
            elif self.type in ["PRD", "EPIC", "STORY"]:
                 # YAML frontmatter: id: <ID>
                 match = re.search(r"^id:\s*([\w-]+)", content, re.MULTILINE)
                 if match: return match.group(1)
                 
        except Exception:
            pass
        return "MISSING_ID"

    def _extract_parent(self):
        """Extracts Parent ID based on traceability standard."""
        try:
            with open(self.filepath, 'r') as f:
                content = f.read()

            if self.type == "PY":
                 # Match: @implements <ID>
                 match = re.search(r"@implements\s+([\w-]+)", content)
                 if match: return match.group(1)

            elif self.type in ["EPIC", "STORY"]:
                 # YAML: parent: <ID>
                 match = re.search(r"^parent:\s*([\w-]+)", content, re.MULTILINE)
                 if match: return match.group(1)
                 
        except Exception:
            pass
        return None

class AuditEngine:
    def __init__(self):
        self.artifacts = []
        self.orhpans = []
        
    def scan_workspace(self):
        """Inventories the system."""
        print("Scanning Workspace...")
        
        # 1. Scan Requirements (Docs)
        doc_files = glob.glob("01_Requirements/**/*.md", recursive=True) + \
                    glob.glob("02_Elaboration/**/*.md", recursive=True)
        
        for f in doc_files:
            if "DoD" in f: continue
            if "guidelines" in f: continue
            
            type_guess = "DOC"
            if "01_Requirements" in f: type_guess = "PRD"
            if "02_Elaboration" in f: 
                if "Story" in f: type_guess = "STORY"
                else: type_guess = "EPIC"
                
            self.artifacts.append(Artifact(f, type_guess))

        # 2. Scan Code
        code_files = glob.glob("src/**/*.py", recursive=True)
        for f in code_files:
            self.artifacts.append(Artifact(f, "PY"))
            
        print(f"Found {len(self.artifacts)} artifacts.")

    def run_quality_checks(self):
        """Mocking quality checks for now (Real linting comes later)."""
        pass

    def check_jira_sync(self):
        """
        Placeholder for Jira Synchronization.
        TODO: Implement Jira API call here.
        """
        return "SYNC_PENDING"

    def generate_report(self):
        print("Generating Dashboard...")
        
        with open(DASHBOARD_FILE, 'w') as f:
            f.write("# Project Audit Dashboard\n")
            f.write(f"**Last Scanned:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("## 1. Traceability Matrix\n")
            f.write("| Artifact ID | Type | Parent (Trace) | Status | Issues |\n")
            f.write("|---|---|---|---|---|\n")
            
            for a in self.artifacts:
                icon = "✅"
                if a.id == "MISSING_ID" and a.type != "PY": icon = "❌"
                if a.parent_id is None and a.type not in ["PRD"]: 
                    # PRD has no parent logic usually, but code MUST have @implements
                    if a.type == "PY": icon = "⚠️ (Orphan)"
                
                f.write(f"| {a.id} | {a.type} | {a.parent_id or '-'} | {icon} | {', '.join(a.issues)} |\n")
            
            f.write("\n## 2. Decision Provenance\n")
            if os.path.exists("decision_log.json"):
                 with open("decision_log.json") as f:
                     log = json.load(f)
                 f.write(f"> ✅ **Decisions Logged:** {len(log)}\n")
            else:
                 f.write("> ⚠️ **No Decisions Logged Yet.** (Audit Risk)\n")

            f.write("\n## 3. Jira Synchronization Status\n")
            f.write("> ⚠️ **Status:** Integration Pending. (Using placeholder logic).\n")

        print(f"Report written to {DASHBOARD_FILE}")

if __name__ == "__main__":
    engine = AuditEngine()
    engine.scan_workspace()
    engine.run_quality_checks()
    engine.generate_report()
