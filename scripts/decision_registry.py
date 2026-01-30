"""
Decision Registry (The "Black Box")
-----------------------------------
This module provides a standardized way for Agents to log "Key Decisions" (ADRs).
It ensures that we can trace *WHY* a decision was made, not just *WHAT* was done.

Usage:
    from scripts.decision_registry import log_decision
    
    log_decision(
        agent_id="ARCH_AGENT",
        topic="Database Selection",
        options=["Postgres", "Mongo", "Redis"],
        selected="Postgres",
        rationale="We need strong ACID compliance for financial transactions."
    )

Output:
    Appends to decision_log.json in the project root.
"""

import json
import os
from datetime import datetime

LOG_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "decision_log.json")

def log_decision(agent_id, topic, options, selected, rationale):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "agent_id": agent_id,
        "topic": topic,
        "options": options,
        "selected": selected,
        "rationale": rationale
    }
    
    # Load existing
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, 'r') as f:
                log = json.load(f)
        except:
            log = []
    else:
        log = []
        
    log.append(entry)
    
    with open(LOG_FILE, 'w') as f:
        json.dump(log, f, indent=2)
    
    print(f"[AUDIT] Decision logged: {topic} -> {selected}")

def get_decisions():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    return []
