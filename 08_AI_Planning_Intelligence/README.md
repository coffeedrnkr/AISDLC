# AI Planning Intelligence Agent

## Overview

The AI Planning Intelligence Agent provides continuous monitoring and management of dependencies across Jira backlogs. This is a **Jira-centric** agent — users do planning in Jira, not VS Code.

## Core Capabilities

| Capability | Description |
|:-----------|:------------|
| **Discovery** | Infers dependencies from story/epic content using NLP |
| **Monitoring** | Tracks dependency health in real-time |
| **Sequencing** | Recommends optimal build order |
| **Prediction** | Forecasts blockers before they occur |

## Available Prompts

| Prompt | Purpose |
|:-------|:--------|
| `/dep-discover` | Analyze stories/epics to find hidden dependencies |
| `/dep-health` | Run health check on sprint or backlog |
| `/dep-sequence` | Get optimal build order recommendation |
| `/sprint-readiness` | Assess sprint readiness with Go/No-Go |

## Health Status Legend

| Status | Meaning |
|:-------|:--------|
| 🟢 | Healthy — dependency completes before dependent work |
| 🟡 | At Risk — tight timing, same sprint |
| 🔴 | Conflict — dependent scheduled before its blocker |

## Jira Integration

This agent works with Jira through:
- **Webhooks**: Listen for `issue.created`, `issue.updated`
- **Jira API**: Read backlog, suggest links
- **Jira Automation**: Trigger notifications
- **Advanced Roadmaps**: Visualize dependencies

## Human-in-the-Loop

AI suggests, humans approve:
- Detected dependency → Accept / Reject / Modify
- Recommended order → Adopt / Adjust
- Alert: Blocker risk → Acknowledge / Dismiss
