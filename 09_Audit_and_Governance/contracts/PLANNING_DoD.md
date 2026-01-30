# Definition of Done: Planning Agent
**Agent ID:** `PLANNING_AGENT`
**Artifact:** Project Plan / Dependency Graph

## 1. Completeness Checks (The Inventory)
*   [ ] **Task Assignment:** Every task assigned to an Agent/Human?
*   [ ] **Estimates:** Every task has a fibonacci estimate?

## 2. Quality Checks (The Standard)
*   [ ] **Acyclic:** No circular dependencies (A -> B -> A).
*   [ ] **Resource Check:** No single agent assigned > 3 parallel tasks?
*   [ ] **Critical Path:** Is the longest path identified?

## 3. Traceability Checks (The Red Thread)
*   [ ] **Alignment:** Plan links to High-Level Roadmap/OkRs.
