---
title: "The AI-Ready Story Authoring Guide: From Epic to Executable Work"
author: "A Guide for Developers, Tech Leads, and BAs"
date: "2025-10-29"
---

# ✍️ The AI-Ready Story Authoring Guide: From Epic to Executable Work

## 1. Introduction: The Story as a "Prompt Package"

In the rapidly evolving landscape of AI-augmented software development, the user story has transcended its traditional role. It is no longer merely a description of a requirement; it is a **highly-structured "prompt package"** designed to be executed by a human developer paired with an AI coding assistant like the Gemini CLI. The quality, clarity, and structure of the story directly determine the quality and accuracy of the AI-generated code.

This guide provides a definitive standard for authoring stories optimized for this new paradigm. Following this guide is not optional; it is a core tenet of our engineering process, ensuring that our AI partners receive the precise, unambiguous instructions they need to accelerate delivery and enhance quality.

---

## 2. The Prime Directive: Vertical Slicing for AI Efficiency

As emphasized in the **Epic Crafting Guide**, every story must be a "vertical slice" of functionality. This means it must deliver a complete, testable piece of end-to-end value, no matter how small. A story that only describes a change to the UI, or only to the database, is not a valid story in our AI-augmented SDLC.

> "An AI coding assistant thrives on context. A horizontal slice provides only partial context, leading to fragmented code, integration issues, and more human intervention. A vertical slice gives the AI the full picture, from user interaction to data persistence."

- **Why it's critical for AI:** An AI assistant can only generate meaningful, integrated code when it understands the full context of a feature, from the user's click in the UI to the data being saved in the database. A vertical slice provides this complete context, enabling the AI to generate code that spans layers and integrates seamlessly.

---

## 3. From Epic to Stories: A Decomposition Strategy for AI-First Development

Decomposing an epic into stories is a collaborative effort between the BA, the Tech Lead, and the development team. The process is as follows:

1.  **Review the Core Documents:** Every story authoring session must begin by reviewing the parent **Epic**, the **PRD**, the **Architecture Hub**, and the **Interaction Hub**. These documents provide the essential context for the AI.
2.  **Map the User Journey:** For the epic, trace the step-by-step user journey required to achieve the business objective. Each distinct step in the user journey becomes a candidate for a user story.
3.  **Apply the "INVEST" Criteria (AI-Augmented):** Every story must be:
    - **I**ndependent: It can be developed and deployed on its own.
    - **N**egotiable: It is not a rigid contract; details can be adjusted.
    - **V**aluable: It delivers tangible value to the end-user.
    - **E**stimable: Its size can be roughly estimated.
    - **S**mall: It can be completed in a few days.
    - **T**estable: It can be verified with objective acceptance criteria.
    *AI agents can assist in validating these criteria, flagging stories that are too large or lack clear value.*

---

## 4. The `Agent: Write-Stories` and `Agent: Generate-Code`: Your AI-Powered Development Partners

The developer's AI-augmented workflow is a two-stage process, involving two distinct but related agents:

### Stage 1: Story Scaffolding with `Agent: Write-Stories`
Before the manual work of authoring a story begins, a developer or tech lead can invoke the **`Agent: Write-Stories`**. 

> **Developer Prompt:** *"Using the 'User Profile Management' Epic, generate a draft of all the necessary AI-ready stories."*

This agent will read the parent Epic and its linked documents and generate a set of draft stories, each with the "Context & Links" section pre-populated and a skeleton for the other sections. This saves the developer the significant manual effort of creating these stories from scratch and ensures no context is missed.

### Stage 2: Code Generation with `Agent: Generate-Code`
After a story has been fully reviewed, detailed, and marked as "Ready for Development," the developer invokes the **`Agent: Generate-Code`**. This agent reads the completed, AI-ready story (our "prompt package") and performs the actions outlined in the "AI Collaboration Plan," such as generating boilerplate code, creating unit test files, and scaffolding UI components.

This two-agent approach separates the task of *structuring the work* from the task of *executing the work*, allowing for a clean and highly efficient development process.

---

## 5. Anatomy of an AI-Ready Story: The Ultimate Prompt Package

This is the standard, mandatory template for all user stories. A story is not considered "Ready for Development" unless it contains all of these sections, providing the maximum possible context to our AI coding assistants.

| Section | Purpose & Content |
|:---|:---|
| **1. Context & Links** | Provides the essential context for the developer and AI. **This is the most critical section.** It must contain direct, non-negotiable links to: <br> - The parent **Jira Epic**. <br> - The relevant section of the **PRD**. <br> - The specific **API Contracts** in the Architecture Hub. <br> - The specific **Data Models** in the Architecture Hub. <br> - The specific **Prompt Designs** in the Interaction Hub. <br> - The relevant **Wireframes** in the Design Hub. |
| **2. Gherkin Acceptance Criteria** | The detailed, BDD-style AC that will be used to generate tests. Each AC must be specific, measurable, and written in the `Given/When/Then` format as defined in the **Quality & Testing Strategy Guide**. *This is the AI's "test plan."* |
| **3. Technical Implementation Plan** | A checklist for the developer and AI. This is not a full design, but a set of clear instructions. It must include: <br> - A list of **files to be created or modified**. <br> - The names of key **functions or classes** to be implemented. <br> - The specific **UI Components** to be used (e.g., `PrimaryButton`, `UserCard`) from the Component Library. <br> - The specific **API endpoints** to be called. <br> - Any required **environment variables or secrets**. *This is the AI's "coding brief."* |
| **4. Manual Validation Steps** | A checklist of visual or experiential checks that cannot be easily automated. <br> - UI aesthetics (colors, spacing, animations). <br> - User "feel" and responsiveness. <br> - Accessibility checks (screen reader, keyboard nav). |
| **5. AI Collaboration Plan** | Explicit, actionable instructions on how the developer should partner with their AI assistant for this story. This guides the developer on how to best leverage the AI. <br> - **Prompt Library:** Link to [Shared Prompt Library] for standard tasks. *This is the AI's "workflow instructions."* |

---

## 5. Case Studies: The Impact of AI-Ready Stories

### Case Study 1: Boilerplate Annihilation
A development team adopted AI-Ready Stories for a new microservice. By providing explicit links to OpenAPI specs and data models, their AI coding assistant was able to generate 80% of the API controller, service layer, and data access boilerplate code automatically. **Result: Developers spent 60% more time on complex business logic and 40% less time on repetitive tasks.**

### Case Study 2: Test-Driven AI
A team struggling with test coverage began using AI-Ready Stories with Gherkin AC. Their AI assistant, integrated with Playwright, generated initial E2E test stubs directly from the AC. **Result: Test coverage for new features increased from 65% to 95%, and the time spent writing initial tests decreased by 75%.**

### Case Study 3: Contextual Refactoring
During a major refactoring effort, developers used AI-Ready Stories that linked to specific Architecture Decision Records (ADRs). When asked to refactor a module, the AI assistant was able to understand the original design intent and propose changes that aligned with the architectural principles, preventing architectural drift.

---

## 6. Example of a Well-Authored, AI-Ready Story

**Title:** `Allow a logged-in user to view their profile information`

### 1. Context & Links
- **Parent Epic:** `[PROJ-123] User Profile Management`
- **PRD:** `[Link to PRD section on User Profiles]`
- **Architecture Hub:**
  - **API Contract:** `[Link to GET /api/users/{id} in OpenAPI spec]`
  - **Data Model:** `[Link to Users table schema]`
- **Interaction Hub:** N/A for this story.
- **Design Hub:**
  - **Wireframes:** `[Link to Wireframe for User Profile Page]`

### 2. Gherkin Acceptance Criteria
```gherkin
Given I am a logged-in user with ID "user-123"
When I navigate to the "/profile" page
Then the page title should be "My Profile"
And the "Name" field should contain "John Doe"
And the "Email" field should contain "john.doe@example.com"
```

### 3. Technical Implementation Plan
- **Modify file:** `client/src/pages/Profile.tsx`
- **Implement:** A React component that fetches user data on mount.
- **API Call:** Make a `GET` request to `/api/users/{id}` using the logged-in user's ID.
- **Environment Variable:** The base URL for the API is available as `process.env.REACT_APP_API_URL`.

### 4. AI Collaboration Plan
1.  **You (the developer):** Write the initial JSX structure for the Profile page component.
2.  **AI Assistant:** Ask the AI to generate the `useEffect` hook to fetch data from the `/api/users/{id}` endpoint and handle loading/error states.
3.  **You:** Review and refine the AI-generated code, ensuring it meets our coding standards.
4.  **AI Assistant:** Ask the AI to generate a skeleton for the Playwright E2E test based on the Gherkin AC above.

---

By adhering to this structured approach, we ensure that every story is a complete, self-contained, and perfectly-formed "prompt package," enabling our human-AI development teams to build features with unprecedented speed and accuracy.

## 7. Next Steps & Related Frameworks

Ready to build?
👉 **[Go to the Developer Playbook](developer-playbook.md)** for the practical "Day in the Life" guide to implementing this story in VS Code.

**Related Reference Guides:**
*   **Design:** [UX Architect Framework](ux-architect-framework.md) (For Step 1: Context)
*   **Architecture:** [Architecture Hub Guide](architecture-hub-guide.md) (For Step 1: Context)
*   **Testing:** [Quality & Testing Strategy Guide](quality-and-testing-strategy-guide.md) (For Step 2: Gherkin ACs)