# AI-Augmented SDLC Framework

> **Documentation-Driven Development with AI Agents**

A complete framework for building software using AI agents at every phase of the SDLC, with documentation and diagrams as code.

---

## Quick Start

```bash
# 1. Clone
git clone https://github.com/coffeedrnkr/AISDLC.git
cd AISDLC

# 2. Setup environment
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Configure
cp .env.example .env
# Add your GEMINI_API_KEY or GCP_PROJECT_ID

# 4. Run an agent
python 01_Requirements/prd_agent/main.py --interactive
```

---

## The 4 Pillars

| Pillar | Description |
|:-------|:------------|
| **📄 Documentation as Code** | All docs in Markdown, version-controlled in Git |
| **📊 Diagrams as Code** | Mermaid, DBML, OpenAPI — no manual drawing |
| **🤖 Agent-Generated Artifacts** | AI agents produce outputs, not humans typing |
| **🔄 Session State** | Agents persist context across sessions |

---

## Agent Inventory

| Phase | Agent | Slash Command | Purpose |
|:------|:------|:--------------|:--------|
| **Requirements** | PRD Agent | `/prd-discover` | Interactive requirements discovery (9 tools) |
| **Elaboration** | Epic Decomposition | `/epic-split` | Decompose PRD into Epics (SPIDR) |
| **Elaboration** | Epic Elaboration | `/epic-elaborate` | Flesh out Epics with CRUD, State, BDD |
| **Elaboration** | Story Agent | `/story-gen` | Generate User Stories from Epics |
| **UX Design** | UX Agent | `/ux-personas` | Generate Personas and Wireframes |
| **Architecture** | Architecture Agent | `/arch-design` | Generate C4, DBML, OpenAPI |
| **Implementation** | Code Governance | `/code-review` | Static Analysis + AI Review |
| **Integration** | Integration Agent | `/ci-check` | Pre-release readiness check |

---

## Project Structure

```
AISDLC/
├── 00_Introduction/     # Standards, base classes, concepts
│   ├── standards/       # Python modules (GenAIBaseAgent, Guardrails, etc.)
│   └── concepts/        # AI development concepts
├── 01_Requirements/     # PRD Agent
├── 02_Elaboration/      # Epic & Story Agents
├── 03_UX_Design/        # UX Agent
├── 04_Architecture/     # Architecture Agent
├── 05_Implementation/   # Code Governance
├── 06_Testing/          # Test Plan Agent
├── .gemini/             # Gemini Code Assist configuration
├── prompts/             # Prompt registry
└── outputs/             # Session state & generated artifacts
```

---

## Built-in Automation

The framework doesn't just document best practices — it **enforces them through code**:

| Concept | Automation |
|:--------|:-----------|
| **Human-in-the-Loop** | `ApprovalGate` requires confirmation for critical actions |
| **AI Guardrails** | `OutputGuardrails` validates all AI output (PII, hallucinations) |
| **Context Management** | `ContextManager` handles large docs with smart chunking |
| **Prompt-Ops** | `PromptRegistry` versions and tests prompts like code |
| **Session State** | Agents persist questions, logs, entities across sessions |

---

## Documentation

| Document | Purpose |
|:---------|:--------|
| [Presentation Deck](00_Introduction/presentation_deck_v2.md) | Visual overview of the methodology |
| [Developer Playbook](05_Implementation/developer-playbook.md) | Step-by-step implementation guide |
| [Agent Registry](REGISTRY.md) | Complete agent inventory |
| [Concepts](00_Introduction/concepts/) | Deep dives into AI development patterns |

---

## Getting Help

- Use `/help` in Gemini Code Assist for available commands
- Check `USER_GUIDE.md` in each agent folder
- View `.gemini/STYLEGUIDE.md` for project conventions

---

## License

MIT

---

**Built with ❤️ and AI**
