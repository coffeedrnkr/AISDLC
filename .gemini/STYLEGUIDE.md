# AISDLC Project Context

> **This file teaches Gemini Code Assist about this project.**

---

## Purpose

This is an **AI-Augmented SDLC (Software Development Lifecycle)** framework.
We practice **Documentation-Driven Development**: documentation is written *first*, reviewed, and then used to generate code.

---

## Key Concepts

| Concept | Description |
|:--------|:------------|
| **Docs as Code** | All documentation (PRD, Epics, Architecture) is Markdown in Git. |
| **Diagrams as Code** | Mermaid, DBML, OpenAPI for visual artifacts. |
| **Agents** | Python-based AI agents that assist at each SDLC phase. |
| **Session State** | Agents persist state in `outputs/` for continuity. |

---

## Available Agents

| Phase | Agent | Command | Purpose |
|:------|:------|:--------|:--------|
| Requirements | PRD Agent | `/prd-discover` | Interactive requirements discovery (9 tools) |
| Elaboration | Epic Decomposition | `/epic-split` | Split PRD into Epics (SPIDR) |
| Elaboration | Epic Elaboration | `/epic-elaborate` | Flesh out Epics with CRUD, State, BDD |
| Elaboration | Story Agent | `/story-gen` | Generate User Stories from Epics |
| UX Design | UX Agent | `/ux-personas` | Generate Personas and Wireframes |
| Architecture | Architecture Agent | `/arch-design` | Generate System Design, DBML, OpenAPI |
| Implementation | Code Governance | `/code-review` | Static Analysis + AI Review |
| Integration | Integration Agent | `/ci-check` | Pre-release readiness check |

---

## Session State Files

These files persist agent state across sessions. **They are Git-tracked.**

| File | Location | Updated When |
|:-----|:---------|:-------------|
| Open Questions | `outputs/open_questions.md` | User parks a question during session |
| Session Log | `outputs/session_log.md` | At end of each interactive session |
| Entity Registry | `outputs/entities.md` | After CRUD/State analysis |

---

## Project Structure

```
AISDLC/
├── 00_Introduction/     ← Standards, base classes, concepts
├── 01_Requirements/     ← PRD Agent, prompts
├── 02_Elaboration/      ← Epic & Story Agents
├── 03_UX_Design/        ← UX Agent, wireframes
├── 04_Architecture/     ← Architecture Agent, DBML, OpenAPI
├── 05_Implementation/   ← Code Governance, Integration
├── 06_Testing/          ← Test Plan Agent
├── .gemini/             ← This config
└── outputs/             ← Session state, generated artifacts
```

---

## Conventions

1. **All documentation is Markdown** (`.md`).
2. **Diagrams use Mermaid** (embedded in Markdown or `.mmd` files).
3. **Database schemas use DBML** (`.dbml`).
4. **APIs are documented with OpenAPI 3.0** (`.yaml`).
5. **Decisions are recorded as ADRs** in `docs/adrs/`.
6. **Templates exist for PRD, Epic, Story** in `templates/`.

---

## When Assisting in This Project

1. **Follow the agents' guidance.** Each agent has a specific methodology (SPIDR, INVEST, CRUD, etc.).
2. **Update session state files** when appropriate (questions, entities, logs).
3. **Use Docs-as-Code patterns.** Prefer Mermaid over static images. Prefer Markdown over Word docs.
4. **Trace back to requirements.** All features should link to PRD sections.
