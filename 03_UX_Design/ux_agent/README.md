# UX Agent Specification

## Purpose
The UX Agent automates the generation of visual artifacts and quality reviews for the design phase of the SDLC. It serves the **UX Architect Framework** defined in `docs/frameworks/ux-architect-framework.md`.

## Core Capabilities
1.  **Flow Mapping:** Generates Mermaid.js `journey` and `flowchart` diagrams from User Stories.
2.  **Heuristic Review:** Audits wireframe descriptions against Nielsen's 10 Usability Heuristics.
3.  **Persona Simulation:** Simulates user interaction paths to stress-test designs.

## Integration Points
- **Input:** User Stories (from Story Agent), Wireframes (from Design Hub).
- **Output:** Mermaid Diagrams (to Design Hub), Review Reports.
- **Tools:** Mermaid CLI, LLM Vision Capabilities (for wireframe analysis).

## Prompts
- `UX_001-flow-mapping`
- `UX_002-heuristic-review`
