# Prompt: Generate AI-Ready Stories

**ID:** `EPIC_001-generate-stories`
**Role:** Technical Product Owner
**Phase:** Planning

## Context
I am providing you with an **Epic** description and relevant architectural context. Your task is to decompose this Epic into **AI-Ready User Stories**.

## Instructions
1.  **Decompose:** Break the Epic into 3-7 independent User Stories.
2.  **Apply INVEST:** Ensure each story is Independent, Negotiable, Valuable, Estimable, Small, and Testable.
3.  **Output Format (For Each Story):**
    *   **Title:** Action-oriented.
    *   **Context Section:** Placeholders for PRD/Design links.
    *   **Gherkin ACs:** 3-5 scenarios using `Given/When/Then` syntax.
    *   **Tech Plan:** Bullet points of files/functions to touch.
    *   **AI Plan:** Which agents will help build this?

## Constraints
*   **Vertical Slicing:** Each story must touch UI, API, and Data if applicable.
*   **Gherkin Quality:** ACs must be testable (no vague terms like "easy to use").

## Input Data
*   [Paste Epic Description Here]
*   [Paste Architecture Context Here]
