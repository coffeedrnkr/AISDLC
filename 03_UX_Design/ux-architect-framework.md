# 🎨 The UX Architect Framework: Designing for the Whole System

## 1. Introduction
Modern UX isn't just about pretty screens; it's about system coherence. This guide defines the "UX Architect Framework," our methodology for designing user experiences that are consistent, validated, and technically feasible before a single pixel is coded.

**The Goal:** Move from "screen-by-screen" design to "system-level" architecture.

---

## 2. The 4-Step Workflow

### Step 1: Flow Mapping (The Journey)
*Before drawing screens, map the path.*
*   **Input:** User Epics + Personas
*   **Action:** Create a Mermaid `journey` diagram mapping the user's emotional and logical path.
*   **Requirement:** Must cover the "Happy Path" (success) AND at least 3 "Sad Paths" (errors, edge cases).

### Step 2: The 3-Screen Solution (The Core)
*Simplify the complexity.*
*   **Philosophy:** If it takes more than 3 distinct screens to solve the core problem, it's too complex.
*   **Action:** Sketch key screens (Mid-Fi wireframes) focusing on layout and data hierarchy.
*   **Tool:** Excalidraw or hand-sketches (AI-generated).

### Step 3: Heuristic Evaluation (The Review)
*Audit against standards.*
*   **Standard:** Nielsen's 10 Usability Heuristics.
*   **Action:** AI critiques the design against these 10 points (e.g., "Visibility of system status," "Error prevention").
*   **Output:** A scored report (1-5 scale) with remediation steps.

### Step 4: Persona Stress-Test (The Simulation)
*Verify with virtual users.*
*   **Action:** "Roleplay" the design with specific personas (e.g., "The Power User," "The Novice," "The Skeptic").
*   **Prompt:** *"Act as 'Busy Bob'. Try to complete this flow while distracted. Where do you get stuck?"*

---

## 3. The Outputs (Artifacts)

| Artifact | Format | Purpose |
| :--- | :--- | :--- |
| **User Journey Map** | Mermaid `journey` | Captures the emotional arc and high-level steps. |
| **User Flow Diagram** | Mermaid `flowchart` | Defines the logical routing, decision points, and error states. |
| **State Diagram** | Mermaid `stateDiagram` | Defines screen states (Loading, Success, Error, Empty). |
| **Wireframes** | PNG / Excalidraw | Visual blueprint for the developer (Structure, not style). |

---

## 4. The AI Workflow (How to Execute)
*   **Inputs:** All Epics + PRD + Personas (loaded into context).
*   **Prompt:** *"Analyze all Business Epics. Create a unified User Flow that covers the requirements for [Persona A]. Then, identify the top 3 screens needed."*
*   **Validation:** *"Critique this flow using Nielsen's heuristics. Identifying potential friction points for a mobile user."*

---

## 5. Prerequisite for Deployment
A story cannot move to "Ready for Dev" until:
1.  All 4 artifacts exist.
2.  Heuristic score > 4/5.
3.  Design is linked in the Jira Story.
