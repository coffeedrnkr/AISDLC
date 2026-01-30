# NotebookLM Context Engineering Playbook
**"The Ingestion Engine" by Antigravity**

## Overview
This document defines the process for using **Google NotebookLM** as the generic "Ingestion Engine" for the AI-Augmented SDLC. NotebookLM is uniquely suited for this role because of its ability to "ground" answers strictly in uploaded sources, minimizing hallucinations before the data ever reaches our Code Agents.

## 1. The Input Strategy ("Solid Materials")
Upload the following artifacts into a single NotebookLM "Notebook". Use consistent naming conventions for better citation.

| Source Type | Examples | Naming Convention |
|:---|:---|:---|
| **Transcripts** | Google Meet/Zoom transcripts, Slack threads | `TRN_Meeting_{Date}_{Topic}` |
| **Legacy Docs** | Old User Guides, Database Schemas, API Docs | `LEG_{System}_{DocName}` |
| **Directives** | Regulatory PDFs, Security Standards, Compliance | `GOV_{StandardName}` |
| **Visuals** | Screenshots of Whiteboards, LucidChart PDFs | `VIS_{DiagramName}` |
| **Strategy** | Pitch Decks, Executive Briefs, Emails | `STR_{DocName}` |

---

## 2. The Prompt Sequence (Chain-of-Thought)
Do not ask for everything at once. Run these prompts in sequence to "Refine and Chunk" the knowledge.

### Phase 1: Conflict Detection ("The Auditor")
**Goal:** Identify contradictions and generate a **Stakeholder Meeting Agenda** to resolve them.

> **Copy-Paste this Prompt:**
> "Act as a Lead Systems Auditor. Review all uploaded sources.
>
> **Part A: The Analysis**
> 1.  **Direct Contradictions:** Where does Source A say 'X' but Source B says 'Y'?
> 2.  **Missing Context:** What critical logical links are missing?
>
> **Part B: The Meeting Agenda (Stakeholder Questions)**
> *Create a separate list specifically for a clarifying meeting.*
> *   **Format:** `[Topic] Question? (Source context)`
> *   Example: `[Payments] Do we support Crypto? Strategy Deck says 'Yes', Compliance Doc says 'No'.`
> "

---

### Phase 2: Domain Modeling ("The Architect")
**Goal:** Establish the "Nouns" and "Verbs" of the system with strict traceability.

> **Copy-Paste this Prompt:**
> "Act as a Data Modeler. Based *strictly* on the sources, identifying the Core Domain Entities and their relationships.
>
> 1. **Visual Model:** Output a **Mermaid Class Diagram** code block.
>    *   Syntax: `classDiagram`
>    *   Define properties with type (e.g., `+String name`) ONLY if found in text.
>    *   Define relationships (e.g., `User "1" --> "*" Order`).
>
> 2. **Vocabulary Dictionary:** Define key terms.
>    *   **CRITICAL:** Every definition MUST cite its source file in brackets.
>    *   Example: `**User**: A registered customer with an active subscription. [Source: LEG_UserGuide.pdf]`"

---

### Phase 3: The Topic Chunking Strategy ("Vertical Slicing")
**Goal:** Create "Feature Pods" (separate files) rather than one giant blob, to respect the Agent's Context Window.

> **Copy-Paste this Prompt:**
> "Act as a Product Owner. We will now extract the specs by Topic.
>
> **Step 1: The Topics**
> Review the Matrix you just made. Group the rows into logical 'Topics' (e.g., Topic 1: User Management, Topic 2: Payments).
>
> **Step 2: The Vertical Slice**
> For EACH Topic, output a separate Markdown block. The header must be `--- TOPIC: [Name] ---`.
> Inside, list the full specs for that topic (User Stories, Rules, Constraints) using the Source citations.
> "

---

### Phase 4: The Validator ("The Red Team")
**Goal:** Force the AI to audit its own work for hallucinations before you export.

> **Copy-Paste this Prompt:**
> "Review the Vertical Slices you just generated.
>
> 1.  **Citation Check:** Did you include a source (`[Source: ...]`) for every single business rule?
> 2.  **Hallucination Check:** Did you invent any features not explicitly mentioned in the text?
>
> **Output:**
> *   If clean: 'Validation Passed.'
> *   If issues found: List the corrections required."
> "

---

## 3. The Export Workflow (Getting it into VS Code)
**NotebookLM Export Options:**
*   **Preferred (Data):** Use NotebookLM's **"Data Tables"** feature to export the Matrix to Google Sheets -> CSV.
*   **Preferred (Text):** Use **"Copy to Clipboard"** for the Topic Blocks.

**Steps:**
1.  **Run Phase 1 (Audit):**
    *   **Export:** Copy the "Meeting Agenda" section to `01_Requirements/inputs/gap_agenda.md`.
    *   **Action:** Have the meeting. Upload the answers as `TRN_Clarification_Meeting.txt` (See "Delta Flow").
2.  **Run Phase 2 (Domain):** Copy Mermaid Code -> VS Code (`04_Architecture/models/domain.mmd`).
3.  **Run Phase 3 (Vertical Slicing):**
    *   Export the Matrix to `01_Requirements/inputs/matrix.csv` (Audit Trail).
    *   Copy *each* Topic Block into a SEPARATE file in `01_Requirements/inputs/`:
        *   `01_Requirements/inputs/context_users.md`
        *   `01_Requirements/inputs/context_payments.md`
4.  **Execute:** Run the PRD Agent:
    `python prd_agent.py generate --input 01_Requirements/inputs/`
    *(The Agent automatically reads ALL files in the input folder).*

## 4. Handling Incremental Updates (The "Delta" Flow)
*Problem: New meeting transcripts (`TRN_Meeting_02`) arrive after we've already chunked the initial data.*

**Do NOT re-generate everything. Use the "Delta" Strategy:**

1.  **Upload:** Add the new file to the existing Notebook.
2.  **Prompt:** Run this specific "Delta Prompt":
    > "Focus ONLY on the newly uploaded source: [Filename].
    > 1. Does this new information **contradict** anything we previously established?
    > 2. Does it add **NEW features** not previously discussed?
    > 3. Does it **modify** existing Business Rules?
    >
    > Output specific 'Update Instructions' for the Product Owner:
    > - 'feature_x': Update Rule 3 to say [New Rule].
    > - 'New Feature': Add [Feature Y]."
3.  **Apply:** Manually update your `raw_context_chunked.md` (or let the PRD Agent `interactive` mode handle the merge).

## 5. Why This Works
*   **NotebookLM (Grounding):** Prevents the "blank page hallucination" by forcing the AI to look at the docs.
*   **The Conflict Check:** Humans often give contradictory requirements in meetings. Catching this *before* generating Code saves weeks of refactoring.
*   **Atomic Chunking:** The "Feature Blocks" are perfectly sized for the PRD Agent's context window, allowing it to elaborate fully on each feature without losing focus.
