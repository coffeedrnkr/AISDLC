# User Slide Content V2 (Framework-Consistent Edition)

## Slide 1: THE SIX PILLARS OF AI-AUGMENTED SDLC

### Pillar 1: VS Code as Home Base
**One environment for everything:**
*   **Gemini Code Assist** – AI pair programmer in the editor
*   **Slash Commands** – `/prd-discover`, `/epic-split`, `/arch-design`
*   **Integrated Terminal** – Gemini CLI - Run agents directly
*   **Git Integration** – Commit, push, PR without leaving the IDE
*   **Jira Integration** – Sync without leaving the IDE


### Pillar 2: Documentation as Code
Everything that describes the system lives **in Git, as text**:
*   **`.md` files** – Markdown for all documentation (PRD, Epics, Stories, ADRs)
*   **Version Controlled** – Changes tracked, reviewable in PRs, rollback possible
*   **`.gemini/STYLEGUIDE.md`** – Teaches AI assistants about project conventions

### Pillar 3: Diagrams as Code
Visuals are **generated from text**, not drawn manually:
| Domain | Tool | Output |
|:-------|:-----|:-------|
| **UX** | Mermaid | User Journeys, State Diagrams, Flowcharts |
| **Architecture** | Mermaid (C4), Python Diagrams | System Structure, Infrastructure |
| **Data** | DBML | Entity-Relationship Diagrams |
| **APIs** | OpenAPI | Swagger UI, Client SDKs |

### Pillar 4: Agent-Generated Artifacts
Outputs are **created by AI Agents**, not written from scratch:

| Phase | Agent | Slash Command | Output |
|:------|:------|:--------------|:-------|
| **Requirements** | PRD Agent | `/prd-discover` | PRD from stakeholder input |
| **Elaboration** | Epic Decomposition | `/epic-split` | Epics using SPIDR |
| **Elaboration** | Epic Elaboration | `/epic-elaborate` | CRUD, State, Edge cases |
| **Elaboration** | Story Agent | `/story-gen` | Jira-ready User Stories |
| **UX Design** | UX Agent | `/ux-personas` | Personas, Wireframes |
| **Interfaces** | Interface Agent | `/interface-discover` | Context diagram, Interface catalog |
| **Interfaces** | Interface Agent | `/interface-spec` | Detailed interface specs |
| **Architecture** | Architecture Agent | `/arch-design` | C4, DBML, OpenAPI |
| **Implementation** | Code Governance | `/code-review` | Static analysis + AI review |
| **Testing** | Test Plan Agent | `/test-plan` | Test plans, unit/E2E stubs |
| **Testing** | Simulation Agent | `/simulate-persona` | Persona edge cases |
| **Testing** | Resilience Agent | `/load-test`, `/chaos-test` | Load scripts, chaos scenarios |
| **Testing** | Interface Agent | `/interface-test` | Contract tests from specs |
| **Integration** | Integration Agent | `/ci-check` | Release readiness check |

**Session State:** Agents persist context across sessions (`open_questions.md`, `session_log.md`, `entities.md`).

### Pillar 5: Git Version Control
**Git is the single source of truth:**
*   **All artifacts in one repo** – Docs, diagrams, code, and tests together
*   **Pull Request workflow** – Every change is reviewed (by humans AND AI)
*   **Full history** – Roll back any document to any point in time

### Pillar 6: AI Governance
**Built-in safeguards — no guidelines to memorize:**

| Capability | Type | What It Does |
|:-----------|:-----|:-------------|
| **Guardrails** | Automatic | PII detection, hallucination prevention, output limits |
| **Human-in-the-Loop** | Always | **VS Code**: Accept/Reject diffs before file changes apply. **Agents**: Preview before saves. |
| **Prompt-Ops** | Automatic | Versioned prompts, testing, A/B comparison |
| **Context Management** | Automatic | Smart chunking, token tracking, summarization |

```mermaid
flowchart LR
    A[Human Input] --> B[VS Code + Gemini]
    B --> C[AI Agent]
    C --> D{Guardrails}
    D --> E[Markdown Artifacts]
    E --> F[Git Repository]
    F --> G[CI/CD Pipeline]
    C --> H[Session State]
    H --> C
```


## Slide 2: JIRA INTEGRATION (Required API Calls)

**Bi-directional sync between Markdown artifacts and Jira tickets:**

| Operation | Jira API Call | When Used |
|:----------|:--------------|:----------|
| **Create Epic** | `POST /rest/api/3/issue` (type: Epic) | After Epic decomposition |
| **Create Story** | `POST /rest/api/3/issue` (type: Story) | After story generation |
| **Link to Parent** | `POST /rest/api/3/issueLink` | Link Story → Epic → PRD |
| **Update Status** | `PUT /rest/api/3/issue/{id}/transitions` | On status change |
| **Add Attachment** | `POST /rest/api/3/issue/{id}/attachments` | Attach Gherkin, diagrams |
| **Sync Description** | `PUT /rest/api/3/issue/{id}` | Update from markdown |
| **Read Issue** | `GET /rest/api/3/issue/{id}` | Sync back to local |
| **Search Issues** | `GET /rest/api/3/search` (JQL) | Find related items |

**Traceability Links:**
- PRD Section → Epic (via `issueLink` type: "relates to")
- Epic → Stories (via `issueLink` type: "parent of")
- Story → Test Cases (via custom link type)

**Existing Tools Used:**
- VS Code: Atlassian for VS Code extension
- CLI: `jira-cli` or custom Python wrapper
- CI: GitHub Actions with Jira Issue to Markdown Action


## Slide 3: REQUIREMENTS (The 3-Layer Framework)

### 1. The Framework
Requirements are organized into 3 interlocking layers:
*   **Layer 1: Strategic Vision** - Outcomes not features
*   **Layer 2: Logic & Design** - Functional flows, user experience
*   **Layer 3: Technical Foundation** - Non-functional requirements, data integrity

### 2. The Outputs
| Layer | Artifact Type | Format |
| :--- | :--- | :--- |
| **Layer 1** | Program Requirements Document (PRD) | Markdown |
| **Layer 2** | Epic Definitions & User Stories | Markdown + Gherkin |
| **Layer 2** | Wireframes | PNG/Excalidraw |
| **Layer 3** | Architecture Constraints | ADRs, Diagrams |

### 3. The AI Workflow
**Inputs:** Stakeholder docs, Meeting transcripts, Brainstorming sessions  
**AI Actions:** NotebookLM synthesizes → AI extracts epics → AI generates Gherkin → AI creates wireframes  
**Outputs:** Structured PRD, Epic docs with acceptance criteria, UX flows

## Slide 4: REQUIREMENTS (The States of Information)
**How AI processes information in 3 states:**

*   **(Solid) Documentation – NotebookLM:**
    *   Summarizes existing docs, finds conflicts, extracts topics
    *   Includes regulatory docs, SOPs, legacy code summaries, database schemas
*   **(Liquid) Conversation – AI Transcription:**
    *   Meeting transcripts captured by AI
    *   AI synthesis of stakeholder discussions (from transcripts)
*   **(Gas) Unspoken Ideas – AI Brainstorming:**
    *   Edge case stress-testing, persona simulation
    *   Mind mapping, form-filling, BDD/Gherkin translation
    *   Requirements traceability automation

## Slide 5: EPIC DECOMPOSITION (Vertical Value Streams)

### 1. The Framework: Vertical Slicing + SPIDR
**Two types of epics:**
*   **Business Epics:** User-facing capability that delivers end-to-end value (from PRD functional requirements)
*   **Enabler Epics:** Infrastructure or services needed to support business epics (from Architecture Hub)

**Vertical Slicing Rule:**
*   Every epic cuts through all layers: **UI → API → Database**
*   **Why for AI:** Provides complete context for code generation (user click → data persistence)

**SPIDR Splitting Patterns:**
| Pattern | When to Use | Example |
|:--------|:------------|:--------|
| **Spike** | Unknowns need research first | "Evaluate payment gateways" |
| **Path** | Happy path vs. error handling | "Submit claim" vs. "Handle rejection" |
| **Interface** | Different platforms/complexities | "Mobile checkout" vs. "Web checkout" |
| **Data** | Different data sources/types | "Import CSV" vs. "API sync" |
| **Rules** | Complex business logic splits | "Simple quote" vs. "Multi-car quote" |

**Quality Gate: INVEST Check**
Each epic is validated: Independent, Negotiable, Valuable, Estimable, Small, Testable

### 2. The Outputs
| Artifact | Format | Content | Storage |
| :--- | :--- | :--- | :--- |
| **Epic Document** | Markdown | Scope, Success metrics, Dependencies, Story themes | `docs/epics/epic-*.md` |
| **Epic Acceptance Criteria** | Gherkin | High-level acceptance criteria | Inside epic doc |
| **Jira Epic** | Jira ticket | Synced from doc | Jira (linked to PRD) |

### 3. The AI Workflow
**Inputs:** PRD (functional requirements) + Architecture Hub (technical constraints)

**AI Actions:**
1. Analyze PRD outcomes → Propose candidate epics (Business + Enabler)
2. Generate scope definition (In Scope / Out of Scope) for review
3. Validate vertical slice (check epic spans UI/API/DB)
4. Extract dependencies (flag enabler epics required first)
5. Sync to Jira with traceability links to PRD

**Outputs:** Epic documents with vertical scope, Jira epics with linked PRD sections

**Live Jira Sync:** Epic docs (markdown) ↔ Jira epics (bi-directional, auto-creates traceability links)

## Slide 6: USER STORY ELABORATION (The AI-Ready Prompt Package)

### 1. The Framework: Epic to Stories
**Story Decomposition:**
*   Break epic into small vertical slices (each = 1-3 days of work)
*   Each story delivers testable, end-to-end value (UI → API → DB)

**Decomposition Steps:**
1. Map the user journey for the epic
2. Identify each distinct step or action
3. Turn each step into a story
4. Validate using INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)

**Story Planning Session:**
1. Define the user need in one sentence
2. List business rules and constraints
3. Create concrete examples of how it works
4. Convert examples into Gherkin scenarios

### 2. The Outputs
| Artifact | Format | Purpose | Generated By |
| :--- | :--- | :--- | :--- |
| **Story Ticket** | Jira | Complete context for dev + AI | AI scaffolded / Human refined |
| **Gherkin ACs** | `.feature` file | Executable specifications | AI from examples |
| **E2E Test Stub** | Playwright `.spec.ts` | Test automation | AI from Gherkin + Wireframes |
| **Implementation Checklist** | Markdown | Files, APIs, functions to modify | AI from Architecture Hub |

**Story Structure (5 Sections):**
1. **Context Links:** Epic, PRD, API contracts, Data models, Wireframes
2. **Gherkin ACs:** Given/When/Then scenarios
3. **Technical Brief:** Files to modify, API endpoints, Environment vars
4. **AI Collaboration Plan:** Step-by-step AI generation instructions
5. **Manual Validation:** UI aesthetics, accessibility checks

### 3. The AI Workflow
**Inputs:** 
- Parent Epic
- Architecture Hub (API contracts, data models)
- UX Design Hub (wireframes for this story's screens)

**AI Actions:**
1. Generate story ticket structure with context links pre-populated
2. Convert business examples to Gherkin Given/When/Then scenarios
3. Extract implementation details from Architecture Hub (API endpoints, data fields, files)
4. Generate Playwright test stub using Gherkin + Wireframes for semantic selectors
5. Sync to Jira with all artifacts linked

**Outputs:** 
- Jira story (ready for development)
- Gherkin `.feature` file
- Playwright test stub (before code exists)
- Implementation checklist

**Integration Points:**
*   **From Architecture:** API contracts → Technical brief, Data models → Test data
*   **From UX:** Wireframes → Semantic selectors (`getByRole`), Flows → Test scenarios
*   **To Testing:** Gherkin ACs → E2E tests (Dimension 4), Implementation plan → Unit tests (Dimension 2)

**Live Jira Sync:** Story docs ↔ Jira tickets (bi-directional, all context links auto-populated)

## Slide 7: UX DESIGN (The UX Architect Framework)

### 1. The Framework: 4-Step Workflow


1.  **Flow Mapping:** Complete user journey (Happy Path + 3 Sad Paths)
2.  **3-Screen Solution:** Key screens optimized for minimum clicks
3.  **Heuristic Evaluation:** Nielsen's 10 principles (rated 1-5)
4.  **Persona Stress-Test:** Simulate users to find friction points

### 2. The Outputs
| Artifact | Format | Purpose |
| :--- | :--- | :--- |
| **User Journey Maps** | Mermaid `journey` | Emotional arc of experience |
| **User Flow Diagrams** | Mermaid `flowchart` | Logical steps and decisions |
| **Wireframes** | PNG/Excalidraw | Visual layout (Mid-Fi) |
| **State Diagrams** | Mermaid `stateDiagram` | Screen states (Loading, Error, etc.) |

### 3. The AI Workflow
**Inputs:** All Epics + PRD + Personas (loaded simultaneously)  
**AI Actions:** Maps flows → Generates wireframes → Evaluates heuristics → Tests with personas  
**Outputs:** User Journeys, Flow Diagrams, Wireframes, State Diagrams

## Slide 8: SYSTEM-WIDE UX (The Holistic Advantage)

**The AI Capability:**
*   **Information Architecture:** Consistent navigation across all features
*   **Cross-Epic Flows:** Identifies connections (e.g., "Order Tracking" links to "Checkout")
*   **Design System:** Reusable components used consistently

**The Result:** Cohesive, conflict-free UX in one shot.


## Slide 9: ARCHITECTURE (The Architecture Hub)

### 1. The Framework
The Architecture Hub is a centralized, version-controlled repository of technical contracts covering:
*   **The WHAT:** Diagrams (visual understanding)
*   **The HOW:** API Contracts + Data Models (implementation contracts)
*   **The SAFE/SCALABLE:** IAM, Governance, Resiliency (for later)

### 2. The Outputs - Pillar #1: The 4 Types of Diagrams
| Diagram Type | Tool | Purpose |
| :--- | :--- | :--- |
| **System Structure** | C4 Model (Mermaid) | High-level logical blocks (App, API, DB) |
| **Cloud Anatomy** | Python Diagrams | Physical resources (GCP Cloud Run, Firestore) |
| **Data Structure** | DBML | Entity-Relationship Diagrams (tables, relationships) |
| **Logic Flow** | Sequence Diagrams (Mermaid) | Step-by-step service interactions |

### 3. The AI Workflow
**Inputs:** PRD + Architecture requirements  
**AI Actions:** Reads prompt-hub/ARCH_001-004 → Generates diagrams  
**Outputs:** Mermaid (C4, Sequence), DBML (ERD), Python code (Infrastructure diagrams)

## Slide 10: ARCHITECTURE (Pillars #2 & #3)

### 2. The Outputs (continued)

**Pillar #2: API Contracts**
*   Machine-readable specifications: OpenAPI (REST), .proto files (gRPC)

**Pillar #3: Data Models & Schemas**
*   Database schemas (Cloud SQL), Firestore models, JSON schemas (message queues)

### 3. The AI Workflow
**Inputs:** PRD + Architecture requirements  
**AI Actions:** Uses prompt-hub/ARCH_002-003 → Generates contracts  
**Outputs:** OpenAPI YAML files, DBML schemas, JSON Schema definitions

---

**Comprehensive Base:**
*   The **WHAT** (Diagrams)
*   The **HOW** (API & Data)
*   The **SAFE/SCALABLE** (IAM, Governance, Resiliency) - *for later*

## Slide 11: INTERFACES (The 4 Layers of Integration)

### AI Discovers, Documents, and Tests Interfaces

> "All system connections must be discovered, documented, tested, and tracked."

### The 4 Layers

| Layer | What | When | AI Command | Output |
|:------|:-----|:-----|:-----------|:-------|
| **1. Context** | Visual map of ALL connections | PRD/Architecture | `/interface-discover` | C4 Context Diagram |
| **2. Catalog** | Master inventory | Epic Decomposition | `/interface-discover` | Interface Catalog |
| **3. Specification** | Detailed per-interface | Story/Architecture | `/interface-spec` | INT-*.md specs |
| **4. Testing** | Contract tests | Testing | `/interface-test` | Pact/pandera tests |

---

### Interface Types

| Type | Direction | Examples | Protocol |
|:-----|:----------|:---------|:---------|
| **API** | In/Out/Both | REST, gRPC, SOAP | HTTPS, HTTP/2 |
| **File - Inbound** | We receive | SFTP pickup, S3 drop | SFTP, S3 |
| **File - Outbound** | We send | SFTP push, S3 upload | SFTP, S3, FTP |
| **Event** | Publish/Subscribe | Pub/Sub, Kafka, webhooks | Various |

---

### Interface Catalog Example

| ID | System | Type | Direction | Protocol | Frequency | Owner |
|:---|:-------|:-----|:----------|:---------|:----------|:------|
| INT-001 | Payment Gateway | API | Outbound | REST | Real-time | Platform |
| INT-002 | Claims Feed | File-In | Inbound | SFTP/CSV | Daily 2am | Claims |
| INT-003 | Accounting Export | File-Out | Outbound | S3/Parquet | Hourly | Finance |
| INT-004 | Policy Events | Event | Outbound | Pub/Sub | Real-time | Platform |

---

### AI Workflow

1. 🤖 **Discover:** Parse PRD/code → Generate Context Diagram + Catalog
2. 🤖 **Specify:** Generate detailed specs (endpoints, schemas, mapping, errors)
3. 🤖 **Test:** Generate contract tests, schema validation, mocks

**HITL:** Interface specs reviewed before implementation

## Slide 12: IMPLEMENTATION (The Context-Driven Developer)

### 1. The Framework: AI-Paired Workflow
**Philosophy:** Context-Driven Development (The "Prompt Package" Approach)
*   **The Shift:** Developer moves from "Code Author" to "Reviewer & Architect"
*   **The Input:** Not just a text story, but a pre-assembled context packet (The Prompt Package)
*   **The Environment:** 
    - Development: VS Code + Gemini Code Assist (Chat, Inline, Agent Mode, Code Review)
    - Deployment: Gemini CLI (Cloud Run `/deploy`, Vertex AI MLOps)

### 2. The Outputs
| Artifact | Content | Verified By |
| :--- | :--- | :--- |
| **Test Suite** | Unit tests + E2E Stubs (Playwright) | Automated CI (Vitest/Playwright) |
| **Source Code** | Implementation matching patterns | Linter + Peer Review + Gemini Code Review |
| **Deployed Service** | Cloud Run / Cloud Functions | Gemini CLI deployment |
| **Pull Request** | Context-linked PR description | AI summarizer |

### 3. The AI Workflow
**Inputs:** The Prompt Package (Jira Story + Wireframes + API Contracts + Data Models)

**AI Actions (Development Phase - Code Assist):**
1.  **Scaffold:** Agent Mode creates file structure from Technical Brief
2.  **Test (Red):** Generate failing tests from Gherkin ACs
3.  **Code (Green):** Write code to pass tests using Design System
4.  **Refactor:** Optimize and clean up code

**AI Actions (Deployment Phase - CLI):**
5.  **Deploy:** CLI `/deploy` command (Cloud Run/Functions)
6.  **MLOps:** Deploy models to Vertex AI (if applicable)

**Jira Sync:** Status updates, time logging, and PR linking

---

## Slide 13: TESTING (The 5 Dimensions of Quality)

### AI Generates, Tools Execute

**🤖 AI (Gemini) generates:** Test plans, test code, load scripts, chaos scenarios  
**🔧 Tools execute:** pytest, Playwright, k6, Locust run the generated tests

---

### Testing is Continuous — Not a Phase

| When | Dimension | AI Does |
|:-----|:----------|:--------|
| **During Requirements** | 1. Simulation | AI simulates personas, finds edge cases |
| **During Story Writing** | 4. Behavior | AI generates E2E scripts from Gherkin |
| **During Architecture** | 3. Contracts | AI generates contract tests from OpenAPI |
| **During Implementation** | 2. Components | AI generates unit tests (TDD support) |
| **Before Release** | 5. Resilience | AI generates load scripts, chaos experiments |

---

### AI-Generated Test Artifacts

| Artifact | AI Agent | Command | What AI Generates |
|:---------|:---------|:--------|:------------------|
| **Test Plans** | Test Plan Agent | `/test-plan` | Coverage matrix, test IDs, traceability |
| **Unit Tests** | Test Plan Agent | `/test-plan` | pytest / Vitest code with assertions |
| **E2E Scripts** | Test Plan Agent | `/test-plan` | Playwright `.spec.ts` with semantic locators |
| **Simulation Reports** | Simulation Agent | `/simulate-persona` | Edge cases, accessibility tests per persona |
| **Load Scripts** | Resilience Agent | `/load-test` | k6 / Locust scripts with thresholds |
| **Chaos YAML** | Resilience Agent | `/chaos-test` | Chaos Mesh configs (requires approval) |

---

### The 5 Dimensions

| Dimension | Input | AI Action | Output |
|:----------|:------|:----------|:-------|
| **1. Simulation** | Personas | 🤖 AI simulates user behaviors | Persona test reports |
| **2. Components** | Code | 🤖 AI generates unit tests | pytest / Vitest |
| **3. Contracts** | OpenAPI specs | 🤖 AI generates contract tests | Contract suites |
| **4. Behavior** | Gherkin ACs | 🤖 AI generates E2E scripts | Playwright scripts |
| **5. Resilience** | Architecture | 🤖 AI generates load/chaos tests | k6, Locust, Chaos Mesh |

---

### Test Lifecycle & Tracking

| Stage | What Happens | AI Role | Human Role |
|:------|:-------------|:--------|:-----------|
| **Plan** | Test strategy created | 🤖 AI drafts | ✍️ Human reviews |
| **Script** | Test code generated | 🤖 AI writes | ✍️ Human reviews |
| **Execute** | Tests run in CI | - | 🔧 Automated |
| **Defects** | Failures tracked | - | ✍️ Human triages |
| **Automation** | CI pipeline maintained | - | 🔧 GitOps |
