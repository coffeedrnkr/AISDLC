# Definition of Done: Test Plan Agent
**Agent ID:** `TEST_PLAN_AGENT`
**Artifact:** Test Plan / Feature Files

## 1. Completeness Checks (The Inventory)
*   [ ] **Coverage:** Is there a Test Scenario for every Acceptance Criterion in the Story?
*   [ ] **Scenarios:**
    *   **Happy Path:** Does it work when everything goes right?
    *   **Negative Path:** Does it fail gracefully when inputs are wrong?
    *   **Edge Case:** Does it handle boundaries (min/max/empty)?
*   [ ] **Test Data:** Is the strategy defined (Mock vs Seed)?

## 2. Quality Checks (The Standard)
*   [ ] **Independence:** Can tests run in parallel (no shared state)?
*   [ ] **Clarity:** Are steps written in plain English (Gherkin)?

## 3. Traceability Checks (The Red Thread)
*   [ ] **Tagging:** `@implements STORY-123` at the top of the specific Feature.
