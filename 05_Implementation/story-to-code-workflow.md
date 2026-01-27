---
title: "The Perfect Handoff: The Story-to-Code Workflow"
author: "Engineering Enablement"
date: "2025-01-24"
---

# 👷 The Perfect Handoff: The Story-to-Code Workflow

## 1. Introduction

Documentation often talks about the "Idea" (PM) and the "Execution" (Dev), but it glosses over the critical **Setup Phase**. How do we ensure a developer has *everything* they need before they even write a line of code?

The **Story-to-Code Workflow** uses the `Agent: Story Author` to compile a complete "Prompt Package," eliminating the "What was that API again?" delays.

**The Magic:** The agent pre-fetches all context (API specs, Designs, DB Schemas) so the Developer's first interaction with their AI coding assistant is 100% informed.

---

## 2. Step 1: The Context Gathering (Process Input)

The developer (or Tech Lead) starts with a Jira Ticket that is just a title: `[EPA-001] Add ETF to Portfolio`.

The developer invokes the `Agent: Story Author` with a simple command:
> "Setup story EPA-001."

**Agent Action (The "Fetcher"):**
1.  **Read Epic:** Finds `EPA-001` in the docs/Jira.
2.  **Trace Links:** Finds the linked **PRD Section** and **Architecture Hub** entries.
3.  **Fetch Content:** It doesn't just link them; it *reads* `portfolio-service-api.yaml` and `firestore-schema.json` into its context window.

---

## 3. Step 2: The Technical Scaffolding (The "Architect Mode")

The agent now acts as a Senior Architect, drafting the **Technical Implementation Plan** for the developer to review.

**Agent Query:**
> "I see we need to call `POST /api/portfolio/etfs`.
> 
> *   **Frontend:** I will specify creating a new formatted `AddETFModal` using the `ModalDialog` component.
> *   **Backend:** I will specify a new `FirestoreClient` method `add_holding()`.
> *   **State:** I will specify using the `usePortfolio` React hook for state updates.
> 
> Does this sound like the right approach?"

**Developer Response:**
> "Yes, but make sure to handle the 409 Conflict error if the ETF exists."

**Agent Action:** The agent adds a specific checklist item: `[ ] Handle 409 Conflict in AddETFModal`.

---

## 4. Step 3: The "Prompt Package" Assembly

The agent compiles the final **AI-Ready Story**. This is the "Developer Setup" artifact.

**The "Package" Includes:**
1.  **The Goal:** (User Story text)
2.  **The Test:** (Gherkin Acceptance Criteria)
3.  **The Map:** (Technical Implementation Plan)
4.  **The Tools:** (Exact Component/Function names to use)
5.  **The Context:** (In-context snippets of the API/DB specs)

---

## 5. Step 4: The Handover (Development Start)

Now, the developer sits down to code. They simply open their IDE and their AI assistant (e.g., Gemini Code Assist).

**Developer Prompt:**
> "Implement [EPA-001] based on the active story file."

**The Result:**
Because the agent prepared the "Package," the AI assistant:
*   Generates the correct API call payload (because it "read" the OpenAPI spec).
*   Uses the correct `ModalDialog` (because it "read" the Component Library ref).
*   Writes the correct Test (because it "read" the Gherkin).

**Zero Hallucination Development:** The developer is effectively "filling in the blanks" of a perfectly defined spec, rather than inventing from scratch.

## 6. Summary

| Input | Process | Output |
| :--- | :--- | :--- |
| **Ticket Title** | Agent **Fetches Context** | **Context-Rich Story** |
| **API/DB Docs** | Agent **Drafts Plan** | **Technical Checklist** |
| **Dev Feedback** | Agent **Refines Constraints** | **The "Prompt Package"** |

## 7. Next Steps: Execution

Once the "Prompt Package" is ready, the developer moves to the **Implementation Phase**.

👉 **[Go to the Developer Playbook](../doc_info/developer-playbook.md)** for the practical guide on executing this story in VS Code.
