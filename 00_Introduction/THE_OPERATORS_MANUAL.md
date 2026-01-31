# THE OPERATOR'S MANUAL
## The Definitive Guide to the AI-Augmented SDLC

**Version:** 1.0 (End-to-End Execution)
**Target Audience:** Developers, Architects, BAs
**Purpose:** The single source of truth for *how to actually run* the framework, from PDF ingestion to final code delivery.

---

## Part 1: The Ingestion Phase (NotebookLM)

Before you open VS Code, you must prepare your context. We do not dump raw PDFs into the AI.

### Step 1: The Raw Dump
1.  Go to **NotebookLM** (notebooklm.google.com).
2.  Create a **New Notebook** named `Project [Name] - Raw Source`.
3.  **Upload** all stakeholder docs:
    *   Meeting Transcripts (`.txt`, `.docx`)
    *   Business Case PDFs
    *   Legacy API Docs
    *   User Research Notes
    *   *(Limit: 50 sources per notebook)*

### Step 2: The Conflict Audit (Mandatory)
You cannot code if stakeholders disagree. Run this prompt in the NotebookLM Chat:

> **Prompt:**
> "Act as a Senior Technical Program Manager. Review all uploaded meeting transcripts and business case documents.
> 
> **Goal:** Identify contradictions in project scope, timeline, budget, or technology stack.
> 
> **Steps:**
> 1. Extract every claim regarding [Deadline, Budget, Supported Browsers, Tech Stack].
> 2. Cross-reference claims between different stakeholders (e.g., 'CEO vs CTO').
> 3. Flag any discrepancies >10% or direct contradictions.
> 
> **Output Format:**
> Generate a Markdown table:
> | Conflict Topic | Source A (Claim + Citation) | Source B (Claim + Citation) | Severity (High/Med) | Recommended Resolution |"

*   **Action:** If High Severity conflicts exist, STOP. Schedule a meeting.
*   **Output:** Save table as `inputs/conflict_resolution.md`.

### Step 3: Vertical Slicing (The Context Prep)
The Application Agent cannot read 50 PDFs. You must "vertical slice" the knowledge into digestible markdown files.

Run these prompts in NotebookLM to generate your **Context Files**:

**Prompt A (The Auth Slice - Security Architect Persona):**
> "Act as a Security Architect. Extract all requirements related to **Authentication, Authorization, and User Identity**.
> 
> **Focus Areas:**
> *   Identity Providers (SSO, OAuth, etc.)
> *   Role-Based Access Control (RBAC) matrix
> *   Session management limits
> 
> **Output:** A structured Markdown document named `auth_flow.md` containing a 'Security Constraints' section and a 'User Flow' section. Do not summarize; extract specific technical constraints."

**Prompt B (The Data Slice - Lead DBA Persona):**
> "Act as a Lead Database Architect. Scan all documents for data entities.
> 
> **Task:**
> 1. Identify all Nouns/Entities (e.g., 'User', 'Order', 'Product').
> 2. Identify relationships (1-to-1, 1-to-many).
> 3. Note specific field constraints (e.g., 'must be encrypted', 'stored for 7 years').
> 
> **Output:** A Mermaid.js Risk-Appropriate Entity Relationship Diagram (text description) and a Data Dictionary table."

**Prompt C (The Business Logic Slice - Product Owner Persona):**
> "Act as a Technical Product Owner. We need to define the 'Golden Path' for [Core Feature X].
> 
> **Steps:**
> 1. Identify the trigger event.
> 2. List every logical check (If/Then) that must pass.
> 3. Define the success state and failure states.
> 
> **Output:** A Gherkin-style 'Feature' description with at least 3 Scenarios (Happy Path, Edge Case, Failure Mode)."

**Definition of Done (Ingestion):**
You have a folder `inputs/context/` containing 3-5 clean Markdown files (approx. 20kb each). No PDFs.

---

## Part 2: The Execution Phase (VS Code)

Now that context is clean, we move to the build environment.

### 2.1 Environmental Setup
1.  Open **VS Code**.
2.  Open your project terminal.
3.  Ensure your **Virtual Environment** is active:
    ```bash
    source venv/bin/activate
    ```
4.  Verify the **Antigravity** toolbelt is ready:
    ```bash
    python planning_agent.py --help
    ```

### 2.2 The Command Reference (Slash Command Mapping)

The framework uses "Slash Commands" as a shorthand for running Python agents.
*   **If you have the VS Code Extension:** Type the Slash Command directly.
*   **If you are in Terminal:** Run the corresponding `python` command.

#### Phase 1: Planning & Requirements

| Slash Command | Terminal Command | Purpose | Input Needed |
|:---|:---|:---|:---|
| `/prd-discover` | `python prd_agent.py generate` | **Draft PRD** from context files | `inputs/context/*.md` |
| `/prd-interactive` | `python prd_agent.py interactive` | **Interview Mode** to refine specific sections | Human input |
| `/epic-split` | `python epic_agent.py decompose` | **Split PRD** into 5-10 Epics | `docs/PRD.md` |
| `/dep-discover` | `python planning_agent.py discover` | **Map Dependencies** between epics | `docs/epics/*.md` |

#### Phase 2: Design & Architecture

| Slash Command | Terminal Command | Purpose | Input Needed |
|:---|:---|:---|:---|
| `/arch-design` | `python architecture_agent.py system_design` | **Create System Architecture** (C4) | `docs/PRD.md` |
| `/interface-spec` | `python architecture_agent.py openapi` | **Generate OpenAPI** Specs (YAML) | `docs/architecture/` |
| `/db-schema` | `python architecture_agent.py dbml` | **Generate DB Schema** (DBML) | `docs/architecture/` |
| `/ux-wireframe` | `python ux_agent.py generate` | **Create Wireframe** Descriptions | `docs/stories/*.md` |

#### Phase 3: Build & Code

| Slash Command | Terminal Command | Purpose | Input Needed |
|:---|:---|:---|:---|
| `/story-gen` | `python story_agent.py generate` | **Create User Stories** (Gherkin) | `docs/epics/*.md` |
| `/code-scaffold` | `python dev_agent.py scaffold` | **Create Boilerplate** code structure | `docs/architecture/` |
| `/code-impl` | `python dev_agent.py implement --story [ID]` | **Implement a Story** | Story ID (e.g., `STORY-101`) |
| `/code-review` | `python code_governance_agent.py review` | **Static Analysis** & Standards Check | Source code |

#### Phase 4: Test & Release

| Slash Command | Terminal Command | Purpose | Input Needed |
|:---|:---|:---|:---|
| `/test-plan` | `python test_plan_agent.py generate` | **Generate Test Cases** (Pytest/Playwright) | `docs/stories/*.md` |
| `/chaos-test` | `python resilience_agent.py run` | **Run Chaos Experiments** | Running app URL |
| `/ci-check` | `python integration_agent.py audit` | **Release Readiness Audit** | Full Repo |
| `/impact-assess` | `python change_agent.py assess` | **What-If Analysis** for new changes | Proposed Change Text |

---

## Part 3: The Audit & Governance Loop

You are not done until the Dashboard is Green.

### 3.1 The Dashboard Check
Run the autonomous project auditor:

```bash
python project_dashboard_agent.py
```

Open `PROJECT_DASHBOARD.md`. You will see a matrix of **Traceability**.

*   ❌ **RED DOT:** A Story exists in `docs/` but has no corresponding code with an `@implements` tag.
    *   **Fix:** Run `/code-impl` for that story.
*   ⚠️ **YELLOW DOT:** Code exists but lacks tests.
    *   **Fix:** Run `/test-plan` and commit the tests.
*   ✅ **GREEN DOT:** Story = Code = Tests.

### 3.2 The Decision Registry
Every architectural choice must be logged.
*   Check `docs/decision_log.json`.
*   If you made a manual decision (e.g., "Switched to Postgres"), you **must** manually allow the agent to log it or add an ADR:
    ```bash
    python architecture_agent.py adr --title "Use Postgres" --status "Accepted"
    ```

---

## Part 4: Troubleshooting Common Flows

### "The Agent Hallucinated a Library"
**Cause:** It didn't read `STYLEGUIDE.md` or `package.json`.
**Fix:**
1.  Check `docs/standards/STYLEGUIDE.md` exists.
2.  Run `/code-review` to force a standards alignment pass.

### "The PRD is too vague"
**Cause:** Vertical Slicing was skipped.
**Fix:**
1.  Go back to Part 1 (NotebookLM).
2.  Generate a more specific `inputs/context/deep_dive_feature_x.md`.
3.  Re-run `/prd-discover`.

### "Dependencies are Circular"
**Cause:** Epics were split arbitrarily.
**Fix:**
1.  Run `python planning_agent.py sequence`.
2.  It will output a logical build order.
3.  Re-order your implementation plan to match.

---

**End of Manual.**
