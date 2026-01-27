# Outputs Directory

This directory contains all generated artifacts from AI agent sessions.

## Session State Files

| File | Purpose | Updated When |
|:-----|:--------|:-------------|
| `open_questions.md` | Questions parked during sessions | User says `park: <question>` |
| `session_log.md` | Log of all agent sessions | End of each interactive session |
| `entities.md` | Registry of discovered domain entities | After CRUD/State analysis |

## Generated Artifacts

| Pattern | Description |
|:--------|:------------|
| `PRD_*.md` | Generated PRD documents |
| `EPIC-*_elaborated.md` | Elaborated Epic documents |
| `stories/*.md` | Generated User Stories |

## Git Tracking

These files ARE tracked in Git to maintain an audit trail and enable collaboration.
