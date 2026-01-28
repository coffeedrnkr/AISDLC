#!/usr/bin/env python3
"""
Change Management Agent (Pillar 9)
----------------------------------
This agent performs "What-If" Impact Assessment for requirement changes.
It analyzes the "blast radius" across PRDs, Epics, Stories, Architecture, and Timelines.

Usage:
    python change_agent.py assess <change_description_or_file>
    python change_agent.py scope <reduction_description_or_file>
    python change_agent.py architecture <change_description_or_file>
"""

import argparse
import sys
import time

class ChangeAgent:
    def __init__(self):
        self.colors = {
            "RED": "\033[91m",
            "YELLOW": "\033[93m",
            "GREEN": "\033[92m",
            "RESET": "\033[0m",
            "BOLD": "\033[1m"
        }

    def _print_header(self, title):
        print(f"\n{'='*60}")
        print(f" {title}")
        print(f"{'='*60}\n")

    def assess_impact(self, change_desc):
        """
        Performs full cascade impact assessment.
        """
        self._print_header("WHAT-IF IMPACT ASSESSMENT")
        
        print(f"Analyzing change: \"{change_desc[:50]}...\"")
        print("Reading context artifacts (PRD, Epics, Architecture)...\n")
        time.sleep(1) # Simulate processing
        
        # Mock Assessment Logic based on keywords
        impact_level = "LOW"
        if "add" in change_desc.lower() or "new" in change_desc.lower():
            impact_level = "MODERATE"
        if "remove" in change_desc.lower() or "delete" in change_desc.lower():
            impact_level = "HIGH"
            
        color = self.colors["GREEN"]
        if impact_level == "MODERATE": color = self.colors["YELLOW"]
        if impact_level == "HIGH": color = self.colors["RED"]
            
        print(f"OVERALL SEVERITY: {color}{impact_level}{self.colors['RESET']}\n")
        
        # PRD Impact
        print(f"{self.colors['BOLD']}PRD IMPACT:{self.colors['RESET']}")
        print("• Goals: No change")
        print("• Scope: Updated to include new requirement")
        print("• Metrics: Added success metric for new feature\n")
        
        # Epic Impact
        print(f"{self.colors['BOLD']}EPIC IMPACT:{self.colors['RESET']}")
        print("• EPIC-001: Modified (2 new stories)")
        print("• EPIC-002: No impact\n")
        
        # Architecture Impact
        print(f"{self.colors['BOLD']}ARCHITECTURE IMPACT:{self.colors['RESET']}")
        if impact_level == "HIGH":
             print(f"{self.colors['RED']}• 🔴 Major Component Change: PaymentService{self.colors['RESET']}")
             print("  - Requires DB schema migration")
             print("  - Impact on external API contract")
        else:
             print(f"{self.colors['YELLOW']}• 🟡 Component Modified: ReportService{self.colors['RESET']}")
             print("  - New method added")
             print("  - No schema changes")
             
        # Timeline Impact
        print(f"\n{self.colors['BOLD']}TIMELINE IMPACT:{self.colors['RESET']}")
        print("• Estimated Effort: 13 Story Points")
        print(f"• Schedule Risk: {color}+3 days delay to Release v1.2{self.colors['RESET']}")
        
        print(f"\n{self.colors['BOLD']}RECOMMENDATION:{self.colors['RESET']}")
        print("PROCEED with conditions:")
        print("1. Update EPIC-001 before sprint planning")
        print("2. Accept 3-day schedule slip")

    def analyze_scope_reduction(self, scope_desc):
        """
        Analyzes impact of cutting features.
        """
        self._print_header("SCOPE REDUCTION ANALYSIS")
        print(f"Analyzing removal of: \"{scope_desc[:50]}...\"\n")
        
        print(f"{self.colors['BOLD']}STORIES TO REMOVE:{self.colors['RESET']}")
        print("• S-045: Feature Implementation (5 pts)")
        print("• S-046: Unit Tests (3 pts)")
        print(f"{self.colors['GREEN']}TOTAL SAVINGS: 8 Story Points (~1 Sprint){self.colors['RESET']}\n")
        
        print(f"{self.colors['BOLD']}ORPHANED WORK:{self.colors['RESET']}")
        print("• S-050: Integration Tests (Depends on S-045)")
        print("  -> Recommendation: Remove S-050 as well\n")
        
        print(f"{self.colors['BOLD']}RISKS:{self.colors['RESET']}")
        print("• User Experience: Missing requested feature")
        print("• Competitive: Parity gap with Competitor X")

    def architecture_impact(self, change_desc):
        """
        Focused architecture assessment.
        """
        self._print_header("ARCHITECTURE IMPACT ONLY")
        print(f"Analyzing technical impact for: \"{change_desc[:50]}...\"\n")
        
        print("COMPONENTS AFFECTED:")
        print("1. API Gateway (Config change)")
        print("2. Auth Service (New scope needed)")
        
        print("\nDATA MODEL:")
        print("• User Table: Add 'preferences' JSONB column")
        
        print("\nADRs NEEDED:")
        print("• ADR-015: Storage format for preferences")

# --- CLI ENTRY POINT ---

def main():
    parser = argparse.ArgumentParser(description="Change Management Agent")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Assess Command
    assess_parser = subparsers.add_parser("assess", help="Full impact assessment")
    assess_parser.add_argument("input", help="Change description or file path")
    
    # Scope Command
    scope_parser = subparsers.add_parser("scope", help="Scope reduction analysis")
    scope_parser.add_argument("input", help="Description of features to cut")
    
    # Architecture Command
    arch_parser = subparsers.add_parser("architecture", help="Architecture-focused assessment")
    arch_parser.add_argument("input", help="Change description")

    args = parser.parse_args()
    agent = ChangeAgent()
    
    # Helper to read file or raw text
    content = ""
    if args.input:
        content = args.input
        try:
            with open(args.input, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            pass # Treat as raw text

    if args.command == "assess":
        agent.assess_impact(content)
        
    elif args.command == "scope":
        agent.analyze_scope_reduction(content)
        
    elif args.command == "architecture":
        agent.architecture_impact(content)
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
