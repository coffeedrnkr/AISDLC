
import os
import glob
import subprocess
import datetime
from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv

# Import sibling agents (assuming PYTHONPATH is set correctly)
# We might need to adjust imports if running as script vs module
try:
    from agents.code_governance_agent.code_governance_agent import CodeGovernanceAgent
except ImportError:
    # Fallback for local dev without package install
    import sys
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from agents.code_governance_agent.code_governance_agent import CodeGovernanceAgent

# Ensure standards module is importable
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../00_Introduction/standards')))

# Import Contracts Loader
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../scripts')))
from contracts_loader import load_dod

console = Console()

class IntegrationAgent:
    def __init__(self):
        # Load env (mainly for Governance Agent which needs keys)
        load_dotenv()
        self.report = []
        self.status = "GREEN"

    def log(self, message: str, status: str = "INFO"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.report.append(f"| {timestamp} | {status} | {message} |")
        
        color = "white"
        if status == "SUCCESS": color = "green"
        elif status == "WARNING": color = "yellow"
        elif status == "ERROR": color = "red"
        
        console.print(f"[{color}][{status}] {message}[/{color}]")

    def check_pipeline_artifacts(self, base_dir: str):
        """Checks for existence of standard artifacts."""
        self.log(f"Checking artifacts in {base_dir}...", "INFO")
        
        checks = {
            "Epics": os.path.join(base_dir, "outputs/epics/*.md"),
            "Stories": os.path.join(base_dir, "outputs/stories/*.md"),
            "Test Plans": os.path.join(base_dir, "outputs/test_plans/*.md"),
            "PRD": os.path.join(base_dir, "outputs/prd/*.md")
        }
        
        for name, pattern in checks.items():
            files = glob.glob(pattern)
            if files:
                self.log(f"Found {len(files)} {name}.", "SUCCESS")
            else:
                self.log(f"Missing {name} artifacts.", "WARNING")
                self.status = "YELLOW"

    def run_tests(self, test_dir: str = "tests"):
        """Runs pytest."""
        self.log("Running Automated Tests...", "INFO")
        if not os.path.exists(test_dir):
            self.log(f"Test directory '{test_dir}' not found. Skipping.", "WARNING")
            return

        try:
            result = subprocess.run(["pytest", test_dir], capture_output=True, text=True)
            if result.returncode == 0:
                self.log("All Tests Passed.", "SUCCESS")
            else:
                self.log("Tests Failed.", "ERROR")
                self.log(result.stdout[:500] + "...", "ERROR") # Snippet
                self.status = "RED"
        except FileNotFoundError:
            self.log("Pytest not found.", "ERROR")
            self.status = "RED"

    def run_governance(self, target_dir: str):
        """Triggers the Code Governance Agent."""
        self.log("Running Code Governance...", "INFO")
        try:
            agent = CodeGovernanceAgent() # Uses env GEMINI_MODEL
            # We'll run it on the target dir and save report to integration output
            output_dir = os.path.join(os.path.dirname(__file__), "output")
            os.makedirs(output_dir, exist_ok=True)
            
            report = agent.review_code(target_dir, output_dir)
            
            # Simple heuristic check of report content for "FAILED" keyword from Bandit
            if "FAILED" in report:
                 self.log("Governance Review detected potential issues.", "WARNING")
                 self.status = "YELLOW"
            else:
                 self.log("Governance Review completed.", "SUCCESS")
                 
        except Exception as e:
            self.log(f"Governance Check failed: {e}", "ERROR")
            self.status = "RED"

    def generate_release_report(self):
        """Generates a Markdown report."""
        report_path = os.path.join(os.path.dirname(__file__), "output", "ReleaseReadiness.md")
        
        markdown = f"""# Release Readiness Report
**Date:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Overall Status:** {self.status}

## Check Log
| Timestamp | Status | Message |
|-----------|--------|---------|
"""
        markdown += "\n".join(self.report)
        
        # Inject Definition of Done (Contract) Verify
        dod_instruction = load_dod("INTEGRATION_DOD")
        markdown += f"\n\n## Audit Contract (INTEGRATION_DOD)\nExecuted against:\n{dod_instruction}\n"

        markdown += f"\n\n## Recommendation\n"
        if self.status == "GREEN":
            markdown += "✅ **READY FOR DEPLOYMENT**"
        elif self.status == "YELLOW":
            markdown += "⚠️ **PROCEED WITH CAUTION** (Review Warnings)"
        else:
            markdown += "🛑 **BLOCKED** (Fix Errors)"

        with open(report_path, "w") as f:
            f.write(markdown)
            
        self.log(f"Report saved to {report_path}", "SUCCESS")

