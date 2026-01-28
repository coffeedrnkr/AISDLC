


---

title: "Agent Inventory & Design Guide"

author: "A Guide to the AI-Augmented SDLC Agent Suite"

date: "2025-10-29"

---



# Agent Inventory & Design Guide



## 1. Introduction



This document provides an overview of the specialized agents within the AI-Augmented SDLC framework. Each agent is designed to collaborate with human team members to automate specific parts of the software development lifecycle. This guide details each agent's purpose, workflow, inputs, outputs, and limitations.



---



## 2. The Agent Suite



### Orchestrator Agent



-   **Purpose:** To serve as the primary interface for the SDLC. In the AI-Augmented SDLC, **VS Code is the Home Base**, and the developer + Gemini act as the orchestrator.

-   **Workflow:** The user stays in VS Code and invokes specialized sub-agents using slash commands or natural language. The "Orchestrator" is effectively the user's session in the IDE.

-   **Inputs:** Project documentation artifacts ("Digital Twin"), user commands.

-   **Outputs:** User guidance, sub-agent triggers.

-   **Limitations:** The Orchestrator delegates specialized tasks to sub-agents.



---



### Agent: Write-PRD



-   **Purpose:** To assist Business Analysts in creating comprehensive Project Requirements Documents (PRD).

-   **Workflow:** The agent guides the Business Analyst through the `prd-guide.md` document, asking clarifying questions and generating content based on user input.

-   **Inputs:** User input from the Business Analyst, background documents (e.g., stakeholder notes, market analysis).

-   **Outputs:** A complete `prd.md` file.

-   **Limitations:** Strategic insights are limited to provided background information. The Business Analyst remains responsible for strategic direction.



---



### Agent: Write-Architecture



-   **Purpose:** To assist Solution Architects in creating the Architecture Hub, generating technical document boilerplate, and validating designs.

-   **Workflow:** Architects can invoke the agent for tasks such as generating ADR templates, scaffolding OpenAPI specifications, or creating Mermaid diagrams from natural language descriptions.

-   **Inputs:** User commands (e.g., "Create a sequence diagram for login"), existing architectural documents.

-   **Outputs:** New or modified files in the Architecture Hub (e.g., ADRs, OpenAPI specs, Mermaid diagrams).

-   **Limitations:** The agent supports documentation and validation but does not make architectural decisions.



---



### Agent: Write-Interaction-Model



-   **Purpose:** To assist AI Interaction Designers in creating the Interaction Hub, including prompt design and agentic workflow mapping.

-   **Workflow:** The agent helps scaffold new entries in the Prompt Catalog, suggests prompt improvements, and generates visual diagrams of agentic workflows from text descriptions.

-   **Inputs:** User commands (e.g., "Scaffold a new prompt for summarization"), existing prompts.

-   **Outputs:** New or modified files in the Interaction Hub.

-   **Limitations:** The agent requires human input for desired AI personality or tone.



---



### Agent: Decompose-Epics



-   **Purpose:** To generate a draft list of Business and Enabler Epics based on the completed PRD and Architecture Hub.

-   **Workflow:** A Business Analyst or Product Owner invokes the agent, which analyzes the "Functional Envelope" and "Architecture Overview" to suggest candidate epics for human review and approval.

-   **Inputs:** The `prd.md` and `architecture-hub.md` files.

-   **Outputs:** A list of suggested epics (JSON or Markdown), which can be integrated into Jira.

-   **Limitations:** The agent's suggestions are a preliminary draft and should be reviewed and refined by a Business Analyst or Product Owner. The agent does not have access to the product roadmap or other strategic context, so it cannot make decisions about prioritization or sequencing.



---



### Agent: Write-Stories



-   **Purpose:** To decompose a selected Epic into a set of AI-Ready Stories.

-   **Workflow:** A developer or tech lead points the agent to a parent Epic. The agent reads the Epic and linked documents (PRD, Architecture Hub) to generate draft story files, pre-populating the "Context & Links" section.

-   **Inputs:** A parent Epic in Jira.

-   **Outputs:** A set of `story-XXX.md` files, formatted according to the AI-Ready Story template.



-   **Limitations:** The agent generates the story structure. Developers are responsible for reviewing and adding detailed "Technical Implementation Plans" and "AI Collaboration Plans."



---



### Agent: Generate-Code



-   **Purpose:** To accelerate development by generating boilerplate code based on the context provided in an AI-Ready Story.

-   **Workflow:** Developers invoke the agent with a completed story file. The agent uses the story, PRD, Architecture Hub, and Interaction Hub to generate code according to the "AI Collaboration Plan" in the story.

-   **Inputs:** A completed `story-XXX.md` file.

-   **Outputs:** New or modified source code files (e.g., `.py`, `.tsx`), unit test files, and other code artifacts.

-   **Limitations:** The agent is highly effective at generating boilerplate and connecting to APIs, but it may not be able to generate complex or novel business logic. Developers are responsible for reviewing, refining, and testing the generated code, and for implementing any complex business logic that is beyond the scope of the agent.



---



### Agent: Generate-Tests



-   **Purpose:** To automatically generate skeleton E2E test files from Gherkin Acceptance Criteria in a story.

-   **Workflow:** This agent is triggered when a story is "Ready for Development." It parses Gherkin AC and generates a corresponding, tagged test file in the Playwright codebase.

-   **Inputs:** A Jira story containing Gherkin AC.

-   **Outputs:** A new `*.spec.ts` file in the E2E test suite.

-   **Limitations:** The agent generates a complete Playwright test file. However, the generated code may require review and refinement by a QA Engineer to ensure it is robust and covers all edge cases.



---



### Agent: Govern-Code



-   **Purpose:** To enforce code compliance with defined standards within the CI/CD pipeline.

-   **Workflow:** This non-interactive agent runs as part of the Cloud Build pipeline on every pull request. It scans code for adherence to Architecture Hub patterns and DevOps guide policies.

-   **Inputs:** A pull request, `architecture-hub.md`, and other policy files.

-   **Outputs:** Comments on the pull request with findings. Failures can block PR merges.

-   **Limitations:** The agent can only enforce policies that are explicitly defined in the Architecture Hub and DevOps guide. It cannot detect unforeseen architectural issues, and it may not be able to understand the intent behind all code changes. Human oversight is still required.



---

### Agent: AI-Planning-Intelligence (Pillar 8)

-   **Purpose:** To continuously monitor and manage dependencies across the Jira backlog (Jira-centric).

-   **Workflow:** This agent can be run on-demand in VS Code or triggered by scheduled jobs. It analyzes story content to discover hidden dependencies, checks sprint readiness, and recommends optimal build sequences.

-   **Inputs:** Jira backlog/sprint data, story content.

-   **Outputs:** Dependency graphs, Health Check Reports (Sprint Readiness, Backlog Health), sequenced build plans.

-   **Prompts:**
    -   `/dep-discover`: Find hidden dependencies
    -   `/dep-health`: Assess sprint/backlog health
    -   `/dep-sequence`: Optimal build order
    -   `/sprint-readiness`: Go/No-Go assessment

-   **Limitations:** It suggests links and sequences but requires human approval to update Jira. It does not replace the Product Owner's prioritization but optimizes execution order.

---

### Agent: Change Management (Pillar 9)

-   **Purpose:** To perform "What-If" Impact Assessment for requirement changes before they are implemented.

-   **Workflow:** Triggered when a requirement addition, modification, or removal is proposed. The agent analyzes the "blast radius" across PRDs, Epics, Stories, Architecture, and Timelines.

-   **Inputs:** Proposed change description, current artifacts (PRD, Epics, Architecture docs).

-   **Outputs:** Impact Assessment Report with severity ratings (Low/Mod/High) and recommendations.

-   **Prompts:**
    -   `/impact-assess`: Full cascade analysis
    -   `/scope-change`: Scope reduction analysis
    -   `/architecture-impact`: Technical impact only

-   **Limitations:** Assessment only. The agent does not execute the changes; it informs the human decision-maker of the consequences.
