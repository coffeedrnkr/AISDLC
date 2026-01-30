# Definition of Done: Change Management Agent
**Agent ID:** `CHANGE_AGENT`
**Artifact:** Change Request / Impact Analysis

## 1. Completeness Checks (The Inventory)
*   [ ] **Impact Analysis:** What services are affected? (The "Blast Radius")
*   [ ] **Migration Plan:** Is there a plan for Data Migration?
*   [ ] **Rollback Strategy:** If this breaks production, how do we undo it in < 5 mins?

## 2. Quality Checks (The Standard)
*   [ ] **Safety Check:** No destructive Database changes (DROP TABLE) without VP approval exception.
*   [ ] **Downtime:** Is estimated downtime < SLA?

## 3. Traceability Checks (The Red Thread)
*   [ ] **Root Cause:** Linked to the Bug/Story causing the change.
