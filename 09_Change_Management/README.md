# Change Management Agent (Pillar 9)

## Overview

The Planning & Change Management Agent provides **What-If Impact Assessment** for requirement changes. Before any change is made, AI assesses the full blast radius across all artifacts.

**Key Principle:** Assessment only — AI shows you the impact before you decide to proceed.

## Core Capabilities

| Capability | Description |
|:-----------|:------------|
| **Cascade Analysis** | PRD → Epic → Story → Architecture → Timeline |
| **Change Types** | Add, Modify, Remove requirement analysis |
| **Effort Estimation** | Story points and sprint impact |
| **Dependency Detection** | What's affected upstream/downstream |
| **Recommendation** | Proceed, defer, or alternatives |

## Available Prompts

| Prompt | Purpose |
|:-------|:--------|
| `/impact-assess` | Full impact assessment for any requirement change |
| `/scope-change` | Analyze scope reduction (cutting features) |
| `/architecture-impact` | Architecture-focused assessment only |

## Impact Severity Legend

| Level | Meaning |
|:------|:--------|
| 🟢 LOW | Minimal changes, contained impact |
| 🟡 MODERATE | Multiple artifacts affected, manageable effort |
| 🔴 HIGH | Major changes, significant rework required |

## Human-in-the-Loop

AI assesses, humans decide:
- Impact assessment complete → Review findings
- Recommend proceed with conditions → Accept / Reject / Modify
- Timeline at risk → Decide on trade-offs
- Architecture changes needed → Approve before proceeding
