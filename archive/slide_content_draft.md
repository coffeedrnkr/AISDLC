# Presentation Slides Draft

## Slide 1: The Modern Testing Framework (Dimensions 1-3)
**Title:** The 5 Dimensions of AI-Native Quality

Just as our Architecture has "6 Pillars", our Quality Strategy has "5 Dimensions". It moves beyond "Unit vs E2E" to testing the **Physics of Software**.

*   **1. Simulation (Pre-Code):**
    *   **Concept:** Testing the *idea* before the code.
    *   **AI Method:** Persona Simulation ("Act as a hacker trying to break this rule").
*   **2. Component Verification (The Pieces):**
    *   **Concept:** Ensuring isolated blocks don't leak.
    *   **AI Method:** Parallel Unit Testing (AI pairs with Dev to hit 80% coverage instantly).
*   **3. Contract Assurance (The Seams):**
    *   **Concept:** Verifying microservice interruptions.
    *   **AI Method:** Spec-Driven Generation (AI reads OpenAPI and writes contract tests).

---

## Slide 2: Behavioral Validation (Dimension 4)
**Title:** The "AC-to-Playwright" Pipeline

Dimension 4 is where we test **Value**.

*   **The Input:** Gherkin ACs ("The Logic") + UX Design Hub Wireframes ("The Map").
*   **The Bridge:** `Agent: Generate-Tests` reads both.
*   **The Output:** Executable Playwright scripts.
*   **Why it works:** The AI uses the wireframe to "see" the selectors that the Gherkin implies.
*   *(Note: Dimension 5 is Resilience, ensuring safeguards are in place).*

---

## Slide 2: The Developer's "Context Cockpit"
**Title:** Information at Your Fingertips: The 360° Context View

*   **The Challenge:** Developers usually start a task by hunting for info: "Where is the design? What's the API? What are the requirements?"
*   **The Solution:** When an AI Coding Assistant starts a ticket, it pre-loads the **3 Layers of Context**:
    1.  **The Code (Liquid):** The current codebase structure and patterns.
    2.  **The Specs (Solid):** The User Story and PRD sections.
    3.  **The Visuals (Wireframes):** *This is where Wireframes fit.* They are not just for humans; they give the AI "eyes" to see the intended layout before writing a single line of CSS.
*   **The Result:** "Zero-Context Switching." The developer validates the AI's plan rather than gathering ingredients.

**Visual Concept:**
A central "Developer/IDE" icon surrounded by 3 inputs feeding into it:
1.  **PRD** (Text)
2.  **Wireframes** (Visual/Pixels)
3.  **Architecture Hub** (Diagrams/Rules)
All converging to generate "Production Ready Code."
