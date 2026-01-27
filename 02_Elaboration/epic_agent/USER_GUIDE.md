# Epic Decomposition Agent - User Guide

This guide describes how to use the **Epic Decomposition Agent** to break down PRD features into enterprise-grade Agile Epics using an **interactive discovery process**.

---

## The Methodology: Interactive Elaboration

This agent doesn't just "split" requirements—it **coaches you through professional BA techniques** to ensure every Epic is complete, testable, and implementable.

### The 5-Step Elaboration Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│ 1. DATA INGESTION                                               │
│    Load PRD + Architecture + any detailed specs.                │
└─────────────────────────────────────┬───────────────────────────┘
                                      ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2. GAP ANALYSIS                                                 │
│    Agent identifies weak areas in the PRD OR user picks Epic.   │
└─────────────────────────────────────┬───────────────────────────┘
                                      ↓
┌─────────────────────────────────────────────────────────────────┐
│ 3. TOOL SELECTION                                               │
│    Agent recommends a Discovery Tool based on the Epic's needs. │
└─────────────────────────────────────┬───────────────────────────┘
                                      ↓
┌─────────────────────────────────────────────────────────────────┐
│ 4. TOOL EXECUTION                                               │
│    Run the tool interactively until complete. Show output.      │
└─────────────────────────────────────┬───────────────────────────┘
                                      ↓
┌─────────────────────────────────────────────────────────────────┐
│ 5. INCORPORATE FINDINGS                                         │
│    Merge discoveries into the Epic. Repeat from Step 2.         │
└─────────────────────────────────────────────────────────────────┘
```

---

## The 9 Discovery Tools

The agent has access to these professional BA techniques. It will **recommend** a tool based on what it sees is missing:

| # | Tool | When AI Suggests It | Output |
| :--- | :--- | :--- | :--- |
| 1 | **Mind Map** | Epic scope unclear, need to visualize sub-features | `epic_mindmap.mmd` |
| 2 | **Brainstorming / What-If** | Feature needs related considerations explored | `epic_brainstorm.md` |
| 3 | **Roleplay / Persona Interview** | Need to validate user flow for this Epic | `epic_roleplay.md` |
| 4 | **CRUD Analysis** | Data entities in this Epic need operations defined | `epic_crud.md` |
| 5 | **Premortem / Edge Cases** | Error handling for this Epic not discussed | `epic_risks.md` |
| 6 | **Traceability Matrix** | Need to link Epic to PRD requirements | `epic_rtm.md` |
| 7 | **State Transition Diagram** | Epic involves entity lifecycle (e.g., Quote Status) | `epic_state.mmd` |
| 8 | **Decision Table** | Epic has complex business rules | `epic_decisions.md` |
| 9 | **BDD / Gherkin Scenarios** | Stories in this Epic need acceptance criteria | `epic_scenarios.feature` |

---

## Part 1: Data Ingestion

### Required Inputs
1. **PRD** (`inputs/PRD.md`) - The approved Product Requirements Document.
2. **Architecture** (`inputs/architecture/`) - System design docs from Architecture Agent.

### Optional Inputs
3. **Detailed Specifications** (`inputs/specs/`) - Deep-dive rules from BAs or NotebookLM.

---

## Part 2: Running the Agent (Interactive Mode)

### Step 1: Start the Agent
```bash
cd 02_Elaboration/epic_agent
python epic_agent.py --interactive --prd inputs/PRD.md
```

### Step 2: Agent Proposes Initial Epics
The agent reads the PRD and proposes an initial Epic breakdown:

```
Agent: I've analyzed the PRD.

Proposed Epics (Initial Cut):
1. EPIC-001: User Authentication (SSO)
2. EPIC-002: Quote Creation
3. EPIC-003: Quote Lifecycle Management
4. EPIC-004: Policy Binding
5. EPIC-005: Claims Submission
6. EPIC-006: Admin Dashboard

⚠️ GAP: EPIC-002 (Quote Creation) mentions "Rating Engine" but no rules defined.
⚠️ GAP: EPIC-003 (Quote Lifecycle) has state transitions not fully mapped.

I recommend:
1. [CRUD Analysis] for EPIC-002 - To define data operations.
2. [State Diagram] for EPIC-003 - To map Quote states.

Which Epic would you like to elaborate first?
```

### Step 3: Elaborate a Specific Epic
```
User: EPIC-002

Agent: Let's elaborate "Quote Creation".

First, I'll run a [CRUD Analysis] to understand data operations.

What data entities are involved in creating a quote?

User: Driver, Vehicle, Coverage, Quote itself.

Agent: For each entity, what operations happen during Quote Creation?

| Entity | Create | Read | Update | Delete |
|:---|:---|:---|:---|:---|
| Driver | ✓ (Add new) | ✓ (Lookup) | ✓ (Edit) | ✗ |
| Vehicle | ✓ | ✓ | ✓ | ✗ |
| Coverage | ✗ | ✓ (Options) | ✓ (Select) | ✗ |
| Quote | ✓ | ✓ | ✓ (Modify) | ✓ (Abandon) |

Does this look right? Any missing operations?

User: Add "Delete" for Vehicle—users should be able to remove a vehicle.

Agent: ✓ Updated.

Now, I notice "Rating Engine" is mentioned but no rules are defined.
I recommend a [Decision Table] to capture the rating logic.

Ready? (yes/no/skip)
```

### Step 4: Iterate Until Complete
After each tool, the agent will:
1. Show the output.
2. Ask follow-up questions.
3. Suggest the next tool.
4. Update the Epic definition.

---

## Part 3: Epic Quality Checks

Before finalizing an Epic, the agent runs two quality checks:

### SPIDR (Splitting Strategy)
If an Epic is too large, the agent suggests splitting it:
- **S**pike: Separate research from implementation.
- **P**ath: Split by user paths (Happy Path vs. Error Handling).
- **I**nterface: Split by platform (Mobile vs. Web).
- **D**ata: Split by data types.
- **R**ules: Split by business logic complexity.

### INVEST (Quality Check)
The agent validates each Epic meets:
- **I**ndependent: Minimal dependencies.
- **N**egotiable: Open to clarification.
- **V**aluable: Delivers clear value.
- **E**stimable: Team can size it.
- **S**mall: Fits within a release.
- **T**estable: Clear "Done" criteria.

---

## Part 4: Incorporating Findings

After running discovery tools, the agent generates:

1. **`outputs/epics/EPIC-001.md`** - Full Epic definition with CRUD, States, etc.
2. **`outputs/epics/EPIC-002.md`** - ...
3. **`outputs/artifacts/`** - All tool outputs (diagrams, matrices).
4. **`outputs/epic_summary.md`** - Overview of all Epics with dependencies.

### The Iteration Cycle
1. Review each Epic file.
2. If gaps remain, run the agent again focusing on that Epic.
3. When all Epics pass INVEST, proceed to Story generation.

---

## Part 5: Handoff to Story Agent

Once Epics are complete:
```bash
python ../story_agent/story_agent.py --epic outputs/epics/EPIC-002.md
```

---

## Authentication

This agent uses the `google-genai` SDK with **Vertex AI** mode.

```bash
gcloud auth application-default login
```

Ensure your `.env` file contains:
```
GCP_PROJECT_ID=your-project-id
GCP_LOCATION=us-central1
```

---

## Troubleshooting

- **Epic too big**: Ask the agent to apply SPIDR splitting.
- **Missing business rules**: Add specs to `inputs/specs/` and re-run.
- **Want to re-run a tool**: Type the tool name (e.g., `CRUD`).
