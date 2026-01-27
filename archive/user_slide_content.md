# User Slide Content (Transcription)

## Slide 1: RETHINKING DOCUMENT FORMAT & GENERATION
*From Static Docs to Living Code*

*   **Use .md files** - easier and more compact for AI and human to exchange information.
*   **Auto Sync** - Can be synced with Jira or other storage types/locations.
*   **.gemini/** - can create a standard style guide.
*   **Diagrams as code** – allow AI to easily create and update diagrams across all domains:
    *   **UX:** Mermaid (User Journeys, State Diagrams, Flowcharts)
    *   **Architecture:** Mermaid (C4), Python Diagrams (Infrastructure), DBML (Data), OpenAPI (APIs)
    *   **Testing:** Mermaid (Sequence Diagrams, Dependency Maps)

## Slide 2: REQUIREMENTS (The 3 Layers)
*   Requirements are organized into 3 interlocking layers.
*   **Layer 1: The Strategic Vision (the north star)**
    *   Focus – Outcomes not features. The Program Requirements document - initial cut created via NotebookLM extracts and AI summary
*   **Layer 2 – The Logic Epic (refinement) & Design**
    *   Focus – Functional flow, user experience - Expaned and elorboration into Epics
    **Wireframes (The Visual Twin)**.
    *   *AI Role:* The UX Architect (Holistic Flow).
*   **Layer 3 – The Technical Foundation (the floor)**
    *   Focus – non-functional requirements and data integrity. - Architecture Hub


## Slide 3: REQUIREMENTS (The States of Matter) 
*   Information usually hides in 3 states: Liquid (conversation), Solid (documentation), and Gas (unspoken ideas). AI can assist in each of these.
*   **(Solid) Documentation – NotebookLM:**
    *   Main repository for original material and artifact, summarize, look for conflicting information, extract smaller topics that fit into LLM context window in Code Assist.
    *   Includes regulatory & compliance documents, existing documentation such as SOPs. Also AI summaries of legacy code, database schemas.
*   **Liquid (Conversation) – meeting transcripts taken by AI.**
## Slide 4: REQUIREMENTS (Gas - Unspoken Ideas)
*   **Gas – (unspoken ideas):**
    *   **Brainstorming:** AI does edge case stress-testing generating 'what if' failure modes.
    *   **Persona Simulation:** AI plays a persona such as customer.cvcvcvs
    *   **Mind Map:** Open conversation with AI drawing out branches of thought in real time if you add a payment note, the AI suggest 'refunds', 'receipts' and tax branches.
    *   **Form filing:** AI has an epic template and has a conversation to fill out using a prompt as a 'expert business analyst', AI assisted CRUD analysis – point the AI at a business process description.
    *   **BDD/Gherkin:** AI converts requirements into BDD syntax which bridges the gap between the "business idea" and the "developers test case".
    *   **Traceability:** The laborous and often incomplete process of requirements tracibility can be done by AI.



## Slide 4.5: THE DESIGN LAYER (The UX Architect Framework)
*   **The "Middle Plane" of Development:**
    *   **Problem Plane:** Requirements (Static Rules).
    *   **Solution Plane:** Design (Human Behavior in Time).
    *   **Construction Plane:** Architecture (System Implementation).

### The 4-Step UX Architect Workflow
**AI acts as a Lead UX Designer with holistic view across all requirements:**

1.  **Flow Mapping (Happy/Sad Paths):** AI maps the complete user journey, identifying the "Happy Path" + 3 "Sad Paths" (e.g., declined card, timeout). Output: Mermaid flowchart.
2.  **The "3-Screen" Solution:** AI generates wireframes for the 3 key screens (Start → Action → Result), optimizing for minimum clicks using common UI patterns.
3.  **Heuristic Evaluation (Nielsen's 10):** AI critiques the proposed flow against usability heuristics (Visibility of System Status, Error Prevention, etc.). Rates 1-5.
4.  **Persona Stress-Test:** AI simulates user personas (e.g., "Grandma Betty" - low tech literacy) to identify friction points.

**Result:** Professional, persona-driven, efficient flows validated before a single pixel is coded.

## Slide 4.6: SYSTEM-WIDE UX (The Holistic Advantage)
**AI designs for the entire system, not one screen at a time.**

**The Input:** All Epics + PRD + Personas loaded simultaneously

**The AI Capability:**
*   **Information Architecture:** Analyzes all epics to design consistent navigation (e.g., 3-level hierarchy: Public → Authenticated → Admin)
*   **Cross-Epic Flows:** Identifies connections between features (e.g., "Order Tracking" links back to "Checkout")
*   **Design System:** Creates reusable components (buttons, cards, forms) used consistently across all screens
*   **Prioritization:** Determines foundational screens (e.g., "User Management" must be designed before "Dashboard")

**The Result:** A cohesive, well-thought-out user interface in one shot, not fragmented designs that conflict later.

**Traditional UX:** Designer does Epic 1, then Epic 2, then realizes they conflict.  
**AI UX:** Holds all epics in context, designs for the whole system simultaneously.

## Slide 5: ARCHITECTURE (Part 1 - The Hub)
*   **The 'Architecture Hub'**
    *   The Architecture Hub is a centralized, version-controlled repository of the system's technical contracts created according to published architectural guidelines and patterns and is a collection of linked, version-controlled documents. It starts with the 4 essential views of software architecture using the 'diagrams as code' paradigm.

### Pillar #1: The 4 Types of Diagrams
| Diagram Type | Tool | Purpose |
| :--- | :--- | :--- |
| **System Structure** | C4 Model (Mermaid.js) | Shows the high-level logical blocks (App, API, DB) and boundaries. |
| **Cloud Anatomy** | Python Diagrams | Shows the concrete physical resources (GCP Cloud Run, Firestore, Queues). |
| **Data Structure** | DBML | Entity-Relationship Diagrams - the "Diagram of Truth" for data. |
| **Logic Flow** | Sequence Diagrams (Mermaid.js) | Shows the step-by-step interaction between services for specific features. |

## Slide 6: ARCHITECTURE (Part 2 - The Contracts)
*   **AI also creates the following:**

**Pillar #2: API Contracts**
*   The definitive, machine-readable specification for all APIs. For RESTful services, this is an OpenAPI (Swagger) specification. For gRPC, it's the .proto files.

**Pillar #3: Data Models & Schemas**
*   Defines the structure of all data. Includes detailed database schemas for Cloud SQL, data models for Firestore, and JSON schemas for message queues.

**The following could also be added** forming a **comprehensive, modern architectural base** covering:
*   The **WHAT** (Diagrams)
*   The **HOW** (API & Data)
*   The **SAFE/SCALABLE** (IAM, Governance, Resiliency)

*Additional Pillars (for later):*
*   **Identity & Access Management (IAM), Security & Networking.**
*   **Data Governance & Privacy.**
*   **Cross cutting concerns:** such as observability, error handling and caching.
*   **Resiliency & Disaster Recovery:**

## Slide 7: TESTING (The 5 Dimensions of Quality)
**AI-Native Quality Model:**

| Dimension | Focus | AI Role | Key Innovation |
| :--- | :--- | :--- | :--- |
| **1. Simulation** | Requirements (Pre-Code) | The Simulator | Persona simulation finds bugs before code exists ($1 vs $10k cost). |
| **2. Components** | Functions/Classes | The Pair Programmer | AI writes unit tests simultaneously with feature code (80%+ coverage, zero friction). |
| **3. Contracts** | APIs/Integrations | The Diplomat | Spec-driven generation from OpenAPI creates contract tests automatically. |
| **4. Behavior** | User Flows (E2E) | The User Proxy | **AC-to-Playwright:** AI reads Gherkin ACs + Wireframes → generates semantic Playwright tests. |
| **5. Resilience** | Security/Performance | The Sentry | Self-healing tests, synthetic data factories, chaos agents. |

**The "Abstract-First" Strategy:** Tests can be written before screens exist using Semantic Locators (`getByRole('button', { name: 'Save' })`), enabling true TDD. 
