# Pillar 11: Audit & Governance System Design
**Status:** Approved for Implementation
**Agent ID:** `AUDIT_001` (Project Dashboard)

## 1. Core Mission
To provide a mathematical proof of project state ("Completeness") and adherence to standards ("Quality") without human intervention.
*   **Completeness:** "Is every requirement implemented, tested, and linked?"
*   **Quality:** "Does the work meet the Definition of Done and organizational Standards?"
*   **Traceability:** "Can we trace every line of code back to a PRD Requirement?"

---

## 2. Core Mechanisms

### A. Universal Traceability Standards (The "Red Thread")
Every artifact must be explicitly linked to its parent.
*   **Python (`src/`):** `""" @implements <ID> """` in docstrings.
*   **Markdown (`docs/`):** YAML Frontmatter `id: <ID>` and `parent: <ID>`.
*   **Tests (`tests/`):** Gherkin tags `@<ID>` or Pytest markers.
*   **Diagrams (Mermaid):** `%% @implements <ID>` metadata + `Node["Name (<ID>)"]` visual.
*   **SQL (`db/`):** `-- @implements <ID>` comments.

### B. The Contract System (Definition of Done)
Every agent must contextually "know" its quality gates.
*   **Mechanism:** `scripts/contracts_loader.py`
*   **Usage:** Agents import this script to inject the specific `*_DoD.md` file into their System Prompt at runtime.
*   **Enforcement:** "You must verify your output against the following Contract before submitting."

### C. Integrity Checks
*   **Template Integrity:** Scans for `[INSERT]`, `TBD`, `{{ val }}`, or `TODO`.
*   **Decision Provenance:** Large decisions must be logged in `decision_log.json` (Why X over Y?).

---

## 3. The Project Dashboard Agent (`project_dashboard_agent.py`)
This is the "Single Source of Truth." It runs nightly or on-demand.

### Logic Flow
1.  **Inventory Scan:**
    *   Crawl `src/`, `tests/`, `docs/`.
    *   Parse **Traceability Tags** to build a `DependencyGraph`.
2.  **Completeness Audit:**
    *   Check: `PRD -> Epic -> Story -> Code -> Test`.
    *   Flag "Orphans" (Code with no Story) or "Broken Chains" (Story with no Code).
3.  **Quality Audit:**
    *   Run Linter (Ruff).
    *   Run Security Scan (Bandit).
    *   Check Template Integrity (Regex).
4.  **Jira Sync (Placeholder):**
    *   *Note: Jira integration is not yet ready.*
    *   Logic: `def check_jira(id): # TODO: Implement Jira API call`
    *   For now, report "Jira Status: Unknown (API Pending)".
5.  **Report Generation:**
    *   Output: `PROJECT_DASHBOARD.md` (Markdown Table).
    *   Columns: `Artifact ID` | `Type` | `Parent` | `Code Linked?` | `Tests Passing?` | `Status`

---

## 4. Implementation Scope

### A. The Contracts (`09_Audit_and_Governance/contracts/`)
We will create `*_DoD.md` files for every agent pillar, separated into **Completeness** and **Quality** sections.
*   `PRD_DoD.md`
*   `EPIC_DoD.md`
*   `STORY_DoD.md`
*   `UX_DoD.md` (Check for Screens)
*   `ARCH_DoD.md` (Check for Entities/APIs)
*   `CODE_DoD.md` (Linter/Complexity)
*   `TEST_DoD.md` (Negative Scenarios)
*   `INTEGRATION_DoD.md`
*   `CHANGE_DoD.md`
*   `SIM_DoD.md`

### B. The Guidelines & Templates
Ensure every agent has a corresponding `guidelines/` folder if missing.
*   Create sample templates where they don't exist to ensure the "Template Integrity" check has a baseline.

### C. Agent Updates
Modify **ALL** existing agents to use `contracts_loader.py`.
*   `planning_agent.py`
*   `architecture_agent.py`
*   `requirements_agent.py` (if exists)
*   *etc.*
