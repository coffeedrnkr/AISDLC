# Definition of Done: PRD Agent
**Agent ID:** `PRD_AGENT`
**Artifact:** Product Requirements Document (PRD)

## 1. Completeness Checks (The Inventory)
*   [ ] **Vision Statement:** Is there a clear, high-level summary of "What" and "Why"?
*   [ ] **Target Audience:** Are specific User Personas identified?
*   [ ] **Functional Requirements:** Listed with MoSCoW prioritization (Must/Should/Could/Won't)?
*   [ ] **Non-Functional Requirements:** Defined (Speed, Security, Scale)?
*   [ ] **Success Metrics:** Are KPIs defined (e.g., "Latency < 200ms")?

## 2. Quality Checks (The Standard)
*   [ ] **Ambiguity Check:**
    *   No vague terms without metrics (e.g., "fast", "robust", "easy").
    *   *Bad:* "The system should be fast."
    *   *Good:* "The system should respond in < 200ms."
*   [ ] **Template Integrity:**
    *   No placeholders like `[Insert Here]`, `TBD`, `TODO`, or `{{ variable }}`.
*   **Traceability:**
    *   Does the document frontmatter include a unique `id` (e.g., `id: PRD-001`)?
