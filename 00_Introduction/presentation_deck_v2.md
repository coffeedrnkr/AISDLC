# AI-AUGMENTED SDLC FRAMEWORK

## Introduction: The Ten Pillars of AI-Augmented SDLC
1.  **VS Code as Home Base**
2.  **Documentation as Code**
3.  **Diagrams as Code**
4.  **Agent-Generated Artifacts**
5.  **Git Version Control**
6.  **AI Governance**
7.  **AI Planning Intelligence**
8.  **Change Management**
9.  **Context Management**
10. **Jira Integration**
11. **Prompt Engineering**
12. **Audit & Governance**

## Pillar 1: VS Code as Home Base
**One environment for everything:**
*   **Gemini Code Assist** – AI pair programmer in the editor
*   **Slash Commands** – `/prd-discover`, `/epic-split`, `/arch-design`
*   **Integrated Terminal** – Gemini CLI - Run agents directly
*   **Git Integration** – Commit, push, PR without leaving the IDE
*   **Jira Integration** – Sync without leaving the IDE


## Pillar 2: Documentation as Code
**Everything that describes the system lives in Git, as text**:
*   **`.md` files** – Markdown for all documentation (PRD, Epics, Stories, ADRs) perfect for AI to read and write
*   **Version Controlled** – Changes tracked, reviewable in PRs, rollback possible
*   **`.gemini/STYLEGUIDE.md`** – Teaches AI assistants about project conventions
*   **Content Generation** – AI generated code usingPython libraries (`python-pptx`, `python-docx`, `WeasyPrint`) automate artifact creation (Slides, Reports, PDFs)
*   **Live Integration** – Inject real-time data from databases (Jira, SQL) into docs using `Pandas` + `Jinja2` templates


## Pillar 3: Diagrams as Code
Visuals are **generated from text**, not drawn manually:
| Domain | Tool | Output |
|:-------|:-----|:-------|
| **UX** | Mermaid | User Journeys, State Diagrams, Flowcharts |
| **Architecture** | Mermaid (C4), Python Diagrams | System Structure, Infrastructure |
| **Data** | DBML | Entity-Relationship Diagrams |
| **APIs** | OpenAPI | Swagger UI, Client SDKs |
| **Logic** | Mermaid (Sequence) | Component interactions & Protocol flows |
| **Planning** | Mermaid (Gantt) | Project Timelines & Roadmaps |
| **Brainstorming** | Mermaid (Mindmap) | Requirements & Topic Visualization |

## Pillar 4: Agent-Generated Artifacts
Outputs are **created by AI Agents**, not written from scratch. They are engineered by layering **AI Capabilities** on top of **Modern Engineering Standards**.

### Key Prompt Engineering Techniques:
*   **The "Critical Friend" Persona**: Agents don't just obey; they challenge assumptions and potential risks (e.g., "This design lacks error handling").
*   **Chain-of-Thought (CoT)**: Prompts force the AI to "think step-by-step" before generating code, reducing hallucinations.
*   **Standards Injection**: Every prompt automatically receives `{{STANDARDS_AND_GUIDELINES}}` (the `STYLEGUIDE.md`), ensuring strict adherence to project conventions.
*   **Context-Aware Output**: Agents generate specific formats (Mermaid, Gherkin, JSON) ready for the next stage of the pipeline.

### Universal Engineering Standards Enforced:
*   **Planning**: **SPIDR** Decomposition, **Vertical Slicing**, **INVEST** Criteria
*   **Requirements**: **Gherkin** (Given-When-Then), **Behavior-Driven Development** (BDD)
*   **Design**: **C4 Model** (Context, Containers, Components), **12-Column Grid**, **Nielsen's Heuristics**
*   **Quality**: **Chaos Engineering** (Chaos Mesh), **Contract Testing** (Pact), **Blast Radius Analysis**
*   **Visuals**: **Mermaid.js** (Flowcharts, Sequence, State Diagrams)

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
| **Planning** | AI Planning Agent | `/dep-discover` | Dependency map, health report |
| **Planning** | Change Mgmt Agent | `/impact-assess` | Impact assessment report |

## Pillar 5: Git Version Control
**Git is the single source of truth:**
*   **All artifacts in one repo** – Docs, diagrams, code, and tests together
*   **Pull Request workflow** – Every change is reviewed (by humans AND AI)
*   **Full history** – Roll back any document to any point in time

## Pillar 6: AI Governance
**Built-in safeguards — no guidelines to memorize:**

| Capability | Type | What It Does |
|:-----------|:-----|:-------------|
| **Guardrails** | Automatic | PII detection, hallucination prevention, output limits |
| **Human-in-the-Loop** | Always | **VS Code**: Accept/Reject diffs before file changes apply. **Agents**: Preview before saves. |
| **Human-in-the-Loop** | Always | **VS Code**: Accept/Reject diffs before file changes apply. **Agents**: Preview before saves. |

## Pillar 7: AI Planning Intelligence
**Transforms static Jira backlogs into dynamic, self-organizing delivery plans.** 

This agent proactively manages the **invisible connections** between tickets—catching missed dependencies, sequence errors, and integration gaps—by continuously analyzing the backlog graph in real-time.

| Capability | What It Does |
|:-----------|:-------------|
| **Analyzes** | Parses backlog exports (JSON/Text) |
| **Discovers** | Infers dependencies via NLP (Regex/Keywords) |
| **Suggests** | Proposes dependency links for human review |
| **Sequences** | Calculates optimal build phases (Topological Sort) |
| **Alerts** | Highlights blocked items in Console (🔴/🟡/🟢) |
| **Predicts** | Identifies Critical Path & Circular Dependencies |

**Key Insight:** This is Jira-centric — planning happens in Jira, not VS Code.

## Pillar 8: Change Management
**What-If Impact Assessment before any change:**

| Change Type | AI Assesses Impact On |
|:------------|:---------------------|
| **Add** | PRD, Epics, Stories, Architecture, Timeline |
| **Modify** | Which artifacts need updates? How much rework? |
| **Remove** | What becomes orphaned? What's affected downstream? |

## Pillar 9: Context Management (Getting the Best from AI)


AI models can only process a limited amount of text at once (the "context window"). Even with 1-2 million tokens, you can't fit everything—so strategic context management is essential.


### The 4-Layer Context Strategy

| Layer | What | When | Tool |
|:------|:-----|:-----|:-----|
| **1. Pre-Process** | Summarize bulk docs | Before development | NotebookLM |
| **2. Chunk** | Hierarchical index → summary → detail | During setup | Manual structuring |
| **3. Context Drawer** | Explicitly include/exclude files | During coding | Code Assist UI |
| **4. Caching** | Reuse common context (STYLEGUIDE, glossary) |


### Key Strategies

| Strategy | Description |
|:---------|:------------|
| **Progressive Disclosure** | Start with summaries, load details on demand |
| **Reference Linking** | Link to docs instead of embedding full content |
| **Semantic Chunking** | Add metadata (ID, summary, keywords) to chunks |
| **Task-Specific Assembly** | Match context to the type of work |

### Session State Management

For multi-session work (PRDs, Epics spanning days/weeks), the framework includes `SessionStateManager`:

| Capability | What It Tracks |
|:-----------|:---------------|
| **Session Log** | Agent used, tools run, outcomes, open questions |
| **Entity Registry** | Domain entities discovered (CRUD, states) |
| **Resumption** | Where user left off, next steps |

**Implementation:** `standards/session_state_manager.py`
**Design Details:** `ai-agent-recommendation-and-workflow.md`

## Pillar 10: Jira Integration

**Bi-directional sync between Markdown artifacts and Jira tickets:**

| Operation | Traceability |
|:---|:---|
| **Sync** | Markdown docs auto-create Jira tickets |
| **Link** | PRD -> Epic -> Story -> Test links maintained automatically |


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


## Detailed Workflow: Requirements

### The 3-Layer Framework
Requirements are organized into 3 interlocking layers:
*   **Layer 1: Strategic Vision** - Outcomes not features
*   **Layer 2: Logic & Design** - Functional flows, user experience
*   **Layer 3: Technical Foundation** - Non-functional requirements, data integrity

### The Outputs
| Layer | Artifact Type | Format |
| :--- | :--- | :--- |
| **Layer 1** | Program Requirements Document (PRD) | Markdown |
| **Layer 2** | Epic Definitions & User Stories | Markdown + Gherkin |
| **Layer 2** | Wireframes | PNG/Excalidraw |
| **Layer 3** | Architecture Constraints | ADRs, Diagrams |

### The AI Workflow
**Inputs:** Stakeholder docs, Meeting transcripts, Brainstorming sessions  
**AI Actions:** NotebookLM synthesizes → AI extracts epics → AI generates Gherkin → AI creates wireframes  
**Outputs:** Structured PRD, Epic docs with acceptance criteria, UX flows

### The States of Information
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


---

## Detailed Workflow: Epic Decomposition

### The Framework: Vertical Slicing + SPIDR
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

### The Outputs
| Artifact | Format | Content | Storage |
| :--- | :--- | :--- | :--- |
| **Epic Document** | Markdown | Scope, Success metrics, Dependencies, Story themes | `docs/epics/epic-*.md` |
| **Epic Acceptance Criteria** | Gherkin | High-level acceptance criteria | Inside epic doc |
| **Jira Epic** | Jira ticket | Synced from doc | Jira (linked to PRD) |

### The AI Workflow
**Inputs:** PRD (functional requirements) + Architecture Hub (technical constraints)

**AI Actions:**
1. Analyze PRD outcomes → Propose candidate epics (Business + Enabler)
2. Generate scope definition (In Scope / Out of Scope) for review
3. Validate vertical slice (check epic spans UI/API/DB)
4. Extract dependencies (flag enabler epics required first)
5. Sync to Jira with traceability links to PRD

**Outputs:** Epic documents with vertical scope, Jira epics with linked PRD sections

**Live Jira Sync:** Epic docs (markdown) ↔ Jira epics (bi-directional, auto-creates traceability links)

## Detailed Workflow: User Story Elaboration

### The Framework: Epic to Stories
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

### The Outputs
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

### The AI Workflow
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

## Detailed Workflow: UX Design

### The Framework: 4-Step Workflow


1.  **Flow Mapping:** Complete user journey (Happy Path + 3 Sad Paths)
2.  **3-Screen Solution:** Key screens optimized for minimum clicks
3.  **Heuristic Evaluation:** Nielsen's 10 principles (rated 1-5)
4.  **Persona Stress-Test:** Simulate users to find friction points

### The Outputs
| Artifact | Format | Purpose |
| :--- | :--- | :--- |
| **User Journey Maps** | Mermaid `journey` | Emotional arc of experience |
| **User Flow Diagrams** | Mermaid `flowchart` | Logical steps and decisions |
| **Wireframes** | PNG/Excalidraw | Visual layout (Mid-Fi) |
| **State Diagrams** | Mermaid `stateDiagram` | Screen states (Loading, Error, etc.) |

### The AI Workflow
**Inputs:** All Epics + PRD + Personas (loaded simultaneously)  
**AI Actions:** Maps flows → Generates wireframes → Evaluates heuristics → Tests with personas  
**Outputs:** User Journeys, Flow Diagrams, Wireframes, State Diagrams

### System-Wide UX (The Holistic Advantage)

**The AI Capability:**
*   **Information Architecture:** Consistent navigation across all features
*   **Cross-Epic Flows:** Identifies connections (e.g., "Order Tracking" links to "Checkout")
*   **Design System:** Reusable components used consistently

**The Result:** Cohesive, conflict-free UX in one shot.


## Detailed Workflow: Architecture

### The Framework
The Architecture Hub is a centralized, version-controlled repository of technical contracts covering:
*   **The WHAT:** Diagrams (visual understanding)
*   **The HOW:** API Contracts + Data Models (implementation contracts)
*   **The SAFE/SCALABLE:** IAM, Governance, Resiliency (for later)

### The Outputs - Pillar #1: The 4 Types of Diagrams
| Diagram Type | Tool | Purpose |
| :--- | :--- | :--- |
| **System Structure** | C4 Model (Mermaid) | High-level logical blocks (App, API, DB) |
| **Cloud Anatomy** | Python Diagrams | Physical resources (GCP Cloud Run, Firestore) |
| **Data Structure** | DBML | Entity-Relationship Diagrams (tables, relationships) |
| **Logic Flow** | Sequence Diagrams (Mermaid) | Step-by-step service interactions |

### The AI Workflow
**Inputs:** PRD + Architecture requirements + Standards, Guidelines and Patterns 
**AI Actions:** Reads prompt-hub/ARCH_001-004 → Generates diagrams  
**Outputs:** Mermaid (C4, Sequence), DBML (ERD), Python code (Infrastructure diagrams)

### API Contracts
*   Machine-readable specifications: OpenAPI (REST), .proto files (gRPC)

### Data Models & Schemas
*   Database schemas (Cloud SQL), Firestore models, JSON schemas (message queues)

### The AI Workflow
**Inputs:** PRD + Architecture requirements  
**AI Actions:** Uses prompt-hub/ARCH_002-003 → Generates contracts  
**Outputs:** OpenAPI YAML files, DBML schemas, JSON Schema definitions

### The SAFE/SCALABLE: Decisions & Infrastructure
**Architecture is not just diagrams—it's decisions and deployment code.**

| Artifact | Purpose | AI Action | Output |
| :--- | :--- | :--- | :--- |
| **ADRs** | Records *why* a decision was made (e.g., "Use Postgres vs. Spanner") | `/arch-decide` | Markdown ADRs (Madr format) |
| **IaC** | Defines physical infrastructure (Cloud Run, VPCs, IAM) | `/arch-infra` | Terraform / Pulumi / YAML |

**Comprehensive Base:**
*   The **WHAT** (Diagrams)
*   The **HOW** (API & Data)
*   The **WHY** (ADRs)
*   The **WHERE** (IaC)

## Detailed Workflow: Interfaces

### AI Discovers, Documents, and Tests Interfaces

All system connections must be discovered, documented, tested, and tracked.

### The 4 Layers

| Layer | What | When | AI Command | Output |
|:------|:-----|:-----|:-----------|:-------|
| **1. Context** | Visual map of ALL connections | PRD/Architecture | `/interface-discover` | C4 Context Diagram |
| **2. Catalog** | Master inventory | Epic Decomposition | `/interface-discover` | Interface Catalog |
| **3. Specification** | Detailed per-interface | Story/Architecture | `/interface-spec` | INT-*.md specs |
| **4. Testing** | Contract tests | Testing | `/interface-test` | Pact/pandera tests |

### Protection Patterns (Architecture Defense)
*   **Anti-Corruption Layer (ACL)**: Isolates your clean domain model from messy external systems using Adapters/Translators.
*   **Strangler Fig Pattern**: Strategy for migrating legacy systems by gradually replacing functionality with new microservices behind a routing facade.
*   **Circuit Breaker**: Prevents cascading failures when external dependencies go down.

---

### Interface Types

| Type | Direction | Examples | Protocol |
|:-----|:----------|:---------|:---------|
| **API** | In/Out/Both | REST, gRPC, SOAP | HTTPS, HTTP/2 |
| **File - Inbound** | We receive | SFTP pickup, S3 drop | SFTP, S3 |
| **File - Outbound** | We send | SFTP push, S3 upload | SFTP, S3, FTP |
| **Event** | Publish/Subscribe | Pub/Sub, Kafka, webhooks | Various |


### AI Workflow

1. 🤖 **Discover:** Parse PRD/code → Generate Context Diagram + Catalog
2. 🤖 **Specify:** Generate detailed specs (endpoints, schemas, mapping, errors)
3. 🤖 **Test:** Generate contract tests, schema validation, mocks

**HITL:** Interface specs reviewed before implementation

## Detailed Workflow: Implementation (The Context-Driven Developer)

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

## Detailed Workflow: Testing

### AI Generates, Tools Execute

**🤖 AI (Gemini) generates:** Test plans, test code, load scripts, chaos scenarios  
**🔧 Tools execute:** pytest, Playwright, k6, Locust run the generated tests

---

### Testing is Continuous — Not a Phase

| Lifecycle Stage | Testing Type | Input | AI Action | Output |
|:---|:---|:---|:---|:---|
| **Requirements** | **Simulation** | Personas | Simulates user edge cases | Persona Reports |
| **Architecture** | **Contract Tests** | OpenAPI Specs | Generates contract consumers | Pact/Pandera Suites |
| **Implementation** | **Unit Tests** | Code | Generates isolated logic tests | Pytest/Vitest |
| **Story** | **Behavior (E2E)** | Gherkin ACs | Generates user flow scripts | Playwright Scripts |
| **Release** | **Resilience** | System Arch | Generates load & chaos plans | k6 & Chaos Mesh |

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


### Test Lifecycle & Tracking

| Stage | What Happens | AI Role | Human Role |
|:------|:-------------|:--------|:-----------|
| **Plan** | Test strategy created | 🤖 AI drafts | ✅ Human reviews |
| **Script** | Test code generated | 🤖 AI writes | ✅ Human reviews |
| **Execute** | Tests run in CI | - | 🔧 Automated |
| **Defects** | Failures tracked | - | ✅ Human triages |
| **Automation** | CI pipeline maintained | - | 🔧 GitOps |




### Test Data Management

| Strategy | What | When |
|:---------|:-----|:-----|
| **Ephemeral Environments** | Pristine, isolated DB per test run | Every PR |
| **Seed Data** | Version-controlled synthetic data | Environment creation |
| **Dynamic Data** | Tests create/teardown own data via API | During execution |

> Golden Rule: Tests never share mutable state.


---


## Pillar 11: Prompt Engineering & Intelligent Methodologies
**Smart Prompts: Encoding Proven, Modern Methodologies**

We didn't just write instructions. We used AI to research the most **proven, widely used, modern techniques** for every stage of the SDLC and baked them into the prompts.

### 1. The "Work" (AI-Selected Methodologies)
The prompt acts as a *Senior Engineer*, enforcing the best way to do the job:

| Role | Proven Methodology | Why We Selected It |
|:---|:---|:---|
| **Requirements** | **SPIDR** (Spike, Path, Interface, Data, Rules) | The industry standard for splitting large Epics without breaking logic. |
| **User Stories** | **INVEST** (Independent, Negotiable...) | Ensures stories are small and testable by default. |
| **Architecture** | **C4 Model** (Context, Containers...) | The modern standard for visualizing software architecture hierarchically. |
| **Testing** | **Gherkin** (Given-When-Then) | The leading format for Behavior Driven Development (BDD). |
| **UX Design** | **Nielsen's 10 Heuristics** | The gold standard for usability auditing. |

### 2. The "Engineering" (Structure)
How we ensure the AI follows these methodologies reliably:

*   **Critical Friend Logic:** We explicitly program a "persona" that challenges assumptions ("Are you sure about this?") rather than blindly complying.
*   **Chain-of-Thought (CoT):** We force the AI to "plan its logic" step-by-step before generating code, reducing logic errors.
*   **Standards Injection:** Every prompt automatically injects the project's `STYLEGUIDE.md` so code matches the team's style.
*   **Traceability Regulations:** Agents are forbidden from hallucinating; they must cite sources (e.g., `[SOURCE: meeting.txt]`).

### 3. The "Safety" (Prompt-Ops)
Prompts are treated as **Code**, not text:
*   **Golden Datasets:** Every prompt is regression-tested against a "Gold Standard" output to ensure upgrades don't break capabilities.
*   **Versioning:** Prompts are stored in Git (`prompts/v3/`), strictly versioned, and rolled back if metrics drop.

---

## Pillar 12: Audit & Governance
**The "Definition of Done" Engine**

We don't trust the AI to "just do it." We enforce a rigorous system of Contracts and Audits.

### 1. The Contract Registry (Definitions of Done)
We have formalized the criteria for success into **12 Immutable Contracts** stored in `contracts/`:
*   **PRD_DoD.md:** Must include "Success Metrics" and "User Personas".
*   **ARCH_DoD.md:** Must include "C4 Diagrams" and "Decision Records".
*   **DEV_DoD.md:** Must include `@implements` tags linking back to Stories.
*   **INT_DoD.md:** Must include "Contract Tests" for every API.

### 2. Runtime Policy Enforcement
We don't rely on the Agent remembering to check the contract.
*   **`scripts/contracts_loader.py`**: A dedicated utility that **physically loads** the correct DoD into the Agent's system prompt at runtime.
*   *Result:* The Agent cannot physically answer without seeing the rules.

### 3. The Project Dashboard (The "Truth")
An autonomous agents (`project_dashboard_agent.py`) scans the entire codebase to generate `PROJECT_DASHBOARD.md`.
*   **Traceability Audit:** Finds every Requirement ID and checks if a file implements it.
*   **Decision Audit:** checks `decision_log.json` for Architectural Decision Records (ADRs).
*   **Guideline Audit:** Ensures every pillar has a `guidelines/` folder.

> **Status:** 🔴 Red (Missing) / 🟢 Green (Complete). No nuance.

### 4. The Sign-off Protocol (Stop-and-Wait)
We debunked the myth of "Autonomous Execution." Our system is designed to **PAUSE**.
*   **The Workflow:** AI Generates -> System Stops -> Human Reviews -> AI Resumes.
*   **The Reason:** A small error in Requirements becomes a catastrophic error in Code. We catch it at the source.
*   **The Rule:** No agent can wake up the next agent without a human "GO" signal (Artifact Approval).

---

## Appendix A: Agent Registry

**Master inventory of 17 Specialized Agents offering 27 Agentic Capabilities:**

| Pillar | Agent | Key Slash Commands | Output/Purpose |
|:-------|:------|:-------------------|:---------------|
| **1: Home Base** | **Orchestrator** | `(User is Orchestrator)` | Invokes all other agents |
| **5: Requirements** | **PRD Agent** | `/prd-discover` | PRD from stakeholder input |
| **5: Elaboration** | **Epic Decomposition** | `/epic-split` | Break PRD into Epics |
| **5: Elaboration** | **Story Agent** | `/story-gen` | Break Epic into Stories |
| **5: Design** | **UX Agent** | `/ux-personas` | Personas & Wireframes |
| **5: Design** | **Interface Agent** | `/interface-spec` | API/Interface contracts |
| **5: Design** | **Architecture Agent** | `/arch-design` | C4 Diagrams, ADRs |
| **5: Build** | **Code Governance** | `/code-review` | Compliance check |
| **5: Test** | **Test Plan Agent** | `/test-plan` | E2E/Unit test plans |
| **5: Test** | **Simulation Agent** | `/simulate-persona` | User behavior simulation |
| **5: Test** | **Resilience Agent** | `/chaos-test` | Load & failure testing |
| **5: Release** | **Integration Agent** | `/ci-check` | Release readiness |
| **8: Planning** | **AI Planning Agent** | `/dep-discover` <br> `/dep-health` <br> `/dep-sequence` <br> `/sprint-readiness` | Dependency & Health check |
| **9: Change** | **Change Mgmt Agent** | `/impact-assess` <br> `/scope-change` <br> `/architecture-impact` | What-If Impact Analysis |

> ℹ️ **Note:** All agents are run from VS Code terminal or chat.

---

## Appendix B: Prompt Registry

### Requirements Prompts (2)

| Prompt ID | File | Purpose | Technique / Output |
|:----------|:-----|:--------|:-------------------|
| `PRD_GEN` | `PRD_GEN-synthesize-prd.md` | Synthesize PRD | **NotebookLM** Synthesis |
| `PRD_GAP` | `PRD_GAP-identify-gaps.md` | Identify gaps | **Gap Analysis** Matrix |

### Elaboration Prompts (2)

| Prompt ID | File | Purpose | Technique / Output |
|:----------|:-----|:--------|:-------------------|
| `EPIC_GEN` | `EPIC_GEN-decompose-epics.md` | Decompose PRD | **SPIDR** & **Vertical Slicing** |
| `STORY_GEN` | `STORY_GEN-generate-stories.md` | Generate Stories | **Gherkin** (BDD) & **Prompt Package** |

### UX Design Prompts (3)

| Prompt ID | File | Purpose | Technique / Output |
|:----------|:-----|:--------|:-------------------|
| `UX_001` | `UX_001-flow-mapping.md` | User flows | **Mermaid** Flowchart & **Happy/Sad Paths** |
| `UX_002` | `UX_002-heuristic-review.md` | Usability review | **Nielsen's 10 Heuristics** Scorecard |
| `UX_003` | `UX_003-generate-wireframe.md` | Wireframes | **12-Column Grid** & Component Specs |

### Architecture Prompts (7)

| Prompt ID | File | Purpose | Technique / Output |
|:----------|:-----|:--------|:-------------------|
| `ARCH_001` | `ARCH_001-generate-c4.md` | C4 Diagrams | **Mermaid C4Context** |
| `ARCH_002` | `ARCH_002-generate-dbml.md` | Data Models | **DBML** Schema |
| `ARCH_003` | `ARCH_003-generate-openapi.md` | API Specs | **OpenAPI 3.0** (YAML) |
| `ARCH_004` | `ARCH_004-generate-python-diagrams.md` | Infrastructure | **Diagrams as Code** (Python) |
| `INT_DISCOVER`| `INT_DISCOVER-interface-discovery.md` | Interface Discovery | **Context Mapping** |
| `INT_SPEC` | `INT_SPEC-interface-specification.md` | Interface Spec | **Contract Definition** |
| `INT_TEST` | `INT_TEST-interface-tests.md` | Contract Tests | **Pact / Pandera** |

### Testing Prompts (4)

| Prompt ID | File | Purpose | Technique / Output |
|:----------|:-----|:--------|:-------------------|
| `TEST_GEN` | `TEST_GEN-generate-test-plan.md` | Test Plans | **Playwright** & **Gherkin** |
| `SIM_001` | `SIM_001-persona-simulation.md` | Persona Sim | **Persona Roleplay** & **WCAG Audit** |
| `LOAD_001` | `LOAD_001-generate-load-tests.md` | Load Tests | **k6** Scripts & **Thresholds** |
| `CHAOS_001` | `CHAOS_001-chaos-scenarios.md` | Chaos Eng | **Chaos Mesh** YAML & **Blast Radius** |

### Supported Stacks
**Polyglot Testing Support:**
*   **Frontend**: JavaScript/TypeScript (Jest, Playwright, Vitest)
*   **Backend**: Python (Pytest, Pandera), Node.js (Jest)

---


---

## Appendix C: Modern Techniques Glossary

**A guide to the industry-leading techniques used throughout this framework.**

### Prompt Engineering Techniques

| Technique | Description | Where Used |
|:----------|:------------|:-----------|
| **Critical Friend** | AI persona that challenges assumptions, points out risks, and offers constructive critique rather than blind compliance. | All V3 Prompts (Role Section) |
| **Chain-of-Thought (CoT)** | Prompting method that forces AI to "think step-by-step" and plan its logic before generating content, reducing hallucinations. | All V3 Prompts (Instructions) |
| **Standards Injection** | Automatically inserting the project's `STYLEGUIDE.md` into every prompt context to ensure code consistency. | Architecture & Implementation Agents |
| **Persona Simulation** | Using AI to roleplay specifically defined user personas (e.g., "The Frustrated Novice") to stress-test UX. | Testing Agent (`SIM_001`) |

### Architecture & Design Techniques

| Technique | Description | Where Used |
|:----------|:------------|:-----------|
| **C4 Model** | Hierarchical approach to software architecture diagrams (Context, Containers, Components, Code). | Architecture Agent (`ARCH_001`) |
| **Diagrams as Code** | Generating visuals from text (Mermaid, DBML) to ensure diagrams are version-controlled and editable. | Architecture Pillar |
| **Anti-Corruption Layer (ACL)** | Pattern for isolating a new system from the domain model of a legacy system it integrates with. | Interface Agent |
| **Strangler Fig** | Migration pattern of gradually creating a new system around the edges of the old, growing until the old system is choked off. | Interface Agent |
| **Circuit Breaker** | Resilience pattern that detects failures and encapsulates the logic of preventing a failure from constantly recurring. | Architecture / Resilience |

### Planning & Agile Techniques

| Technique | Description | Where Used |
|:----------|:------------|:-----------|
| **SPIDR** | Method for splitting Epics: **S**pike, **P**ath, **I**nterface, **D**ata, **R**ules. | Epic Agent (`EPIC_GEN`) |
| **Vertical Slicing** | Delivering work that cuts through all layers (UI, API, DB) rather than building complete horizontal layers one by one. | Epic & Story Agents |
| **Gherkin (BDD)** | Structured "Given-When-Then" language for defining requirements that can be automatically tested. | Story Agent (`STORY_GEN`) |
| **INVEST** | Criteria for quality User Stories: **I**ndependent, **N**egotiable, **V**aluable, **E**stimable, **S**mall, **T**estable. | Story Agent |

### Quality & Testing Techniques

| Technique | Description | Where Used |
|:----------|:------------|:-----------|
| **Chaos Engineering** | Controlled experiments on a distributed system (e.g., injecting latency) to build confidence in its resilience. | Resilience Agent (`CHAOS_001`) |
| **Contract Testing** | Verifying that services communicate correctly by checking against a shared "contract" (e.g., OpenAPI spec). | Interface Agent (`INT_TEST`) |
| **Heuristic Evaluation** | Inspection method using Nielsen's 10 Usability Heuristics to identify usability problems. | UX Agent (`UX_002`) |
| **Blast Radius Analysis** | Assessing the full impact of a change across documentation, code, and tests before execution. | Change Management Agent |
