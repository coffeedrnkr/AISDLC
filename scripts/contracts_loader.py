#!/usr/bin/env python3
"""
Contracts Loader (The "Syringe")
--------------------------------
This utility is responsible for injecting the "Definition of Done (DoD)" 
into the System Prompt of every Agent.

It ensures that:
1. The Agent knows its specific quality gates.
2. The Agent is forced to self-verify against the contract.

Usage:
    from scripts.contracts_loader import load_dod
    
    # In agent code:
    dod_instruction = load_dod("PRD") 
    system_prompt += f"\n\n{dod_instruction}"
"""

import os
import sys

# Define the root of the project relative to this script
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTRACTS_DIR = os.path.join(PROJECT_ROOT, "09_Audit_and_Governance", "contracts")

def load_dod(agent_role: str) -> str:
    """
    Loads the Definition of Done (DoD) for a specific agent role.
    
    Args:
        agent_role (str): The role ID, corresponding to the filename prefix (e.g., 'PRD', 'ARCH', 'STORY').
        
    Returns:
        str: A formatted string containing the DoD instructions to be appended to the System Prompt.
    """
    filename = f"{agent_role.upper()}_DoD.md"
    file_path = os.path.join(CONTRACTS_DIR, filename)
    
    if not os.path.exists(file_path):
        return f"\n[WARNING: AUDIT SYSTEM]\nNo Definition of Done found for '{agent_role}'. Proceed with caution."
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
        instruction = (
            f"\n\n{'='*40}\n"
            f"!!! CRITICAL INSTRUCTION: AUDIT CONTRACT !!!\n"
            f"{'='*40}\n"
            f"You are strictly bound by the following Definition of Done (DoD).\n"
            f"Before generating your final output, you MUST verify it against every item in this checklist.\n"
            f"If you fail any check, you must correct it immediately.\n\n"
            f"{content}\n"
            f"{'='*40}\n"
        )
        return instruction
        
    except Exception as e:
        return f"\n[ERROR: AUDIT SYSTEM]\nFailed to load contract: {e}"

if __name__ == "__main__":
    # Test run
    if len(sys.argv) > 1:
        print(load_dod(sys.argv[1]))
    else:
        print("Usage: python contracts_loader.py <AGENT_ROLE>")
        print("Example: python contracts_loader.py PRD")
