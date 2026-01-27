# The AI UX Architect: Holistic Design Workflow

## 1. Introduction

The **AI UX Architect** is a specialized role where AI does not just "draw screens" but "designs systems." It moves beyond the pixel-pushing of wireframing into the strategic logic of User Flows and Information Architecture.

## 2. The Holistic Context: System-Wide Design

**Traditional UX design is sequential:**
- Designer works on Epic 1, then Epic 2, then discovers conflicts
- Navigation patterns are inconsistent
- Design systems are created retroactively

**AI UX Architect is holistic:**
- Loads **ALL epics + PRD + Personas** simultaneously
- Designs for the **entire system** in one pass
- Ensures:
  - Consistent navigation across all features
  - Cross-epic flows are connected properly
  - Design system components are reusable
  - Foundation screens are prioritized correctly

**Example:**
```
Input Context:
- PRD.md
- epic-001-user-management.md
- epic-002-checkout.md
- epic-003-order-tracking.md
- epic-004-admin-dashboard.md
- personas/busy-mom.md

AI Analysis:
→ "Order Tracking (Epic 3) needs navigation link to Checkout (Epic 2)"
→ "Admin Dashboard (Epic 4) requires User Management (Epic 1) as foundation"
→ "All 4 epics will use shared Header component with consistent navigation"
```

## 3. The 4-Step Architect Workflow
To act as an architect, the AI needs the full picture. It cannot design a "Login Screen" in isolation; it must design the "Authentication Journey."

**Required Inputs:**
1.  **The PRD (North Star):** To understand the "Why" and the Business Goals.
2.  **The Epics (The Logic):** To understand the specific functional groups (e.g., "Checkout," "Profile Management").
3.  **The User Personas:** To simulate empathy (e.g., "The Power User" vs "The Novice").

## 3. The 4-Step Architect Workflow

### Step 1: Flow Mapping (The "Happy Path" & "Sad Path")
*   **Prompt:** *"Act as a Lead Information Architect. Read Epic-101 ('Checkout'). Map the User Flow diagram for the Happy Path. Then, identify 3 'Sad Paths' (e.g., declined card, timeout) and map those. Output as Mermaid flowchart."*
*   **Goal:** Logic validation before visual design.

### Step 2: The "3-Screen" Solution
*   **Concept:** Design standardizes on flows of 3 screens (Start -> Action -> Result).
*   **Prompt:** *"Based on the flow above, generate wireframes for the 3 key screens. Use common UI patterns (e.g., bottom sheets for mobile actions). Optimize for minimum clicks."*

### Step 3: Heuristic Evaluation (Nielsen's 10)
*   **Concept:** AI critiques its own work or human work.
*   **Prompt:** *"Act as a Nielsen Group researcher. Audit this proposed flow against the 10 Usability Heuristics. Specifically check for 'Visibility of System Status' and 'Error Prevention'. Rate functionality 1-5."*

### Step 4: The Persona Stress-Test
*   **Concept:** Simulation of user friction.
*   **Prompt:** *"Act as 'Grandma Betty' (low tech literacy, bad eyesight). Walk through this wireframe flow. Where do you get stuck? What text is confusing?"*

## 5. UX Diagrams as Code
We don't just want static images; we want version-controlled logic.

1.  **Mermaid User Journeys:** Use the `journey` syntax to map emotional highs and lows.
    ```mermaid
    journey
      title Checkout Experience
      section Payment
        Enter Card: 5: User
        Error "Declined": 1: User
        Retry with PayPal: 4: User
    ```
2.  **Mermaid Flowcharts:** For the logic tree of the flow (e.g., `If Logged In --> Go to Dashboard`).
3.  **State Diagrams:** For defining screen states (e.g., `Loading`, `Empty`, `Error`, `Populated`).

## 6. Artifacts Produced
*   **Mermaid Flowcharts:** (Logic Layer)
*   **Wireframe Sketches:** (Visual Layer)
*   **Heuristic Audit Report:** (Quality Layer)
