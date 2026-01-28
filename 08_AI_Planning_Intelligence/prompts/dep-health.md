# Dependency Health Check Prompt

## Purpose
Assess the health of dependencies in a sprint or backlog.

## When to Use
- Before sprint planning
- Weekly backlog review
- When blockers are suspected

## Prompt Template

```
Analyze these stories for dependency health:

## Stories
[Paste list of stories with titles, descriptions, and any known dependencies]

## Analysis Required
1. **Dependency conflicts** — Dependent work scheduled before its blocker
2. **At-risk dependencies** — Tight timing, same sprint
3. **Missing dependencies** — Stories that likely need links
4. **Cross-team status** — External dependencies at risk
5. **Recommended sequencing** — Optimal order within sprint
```

## Example Input

```
Sprint 15 Stories:

1. PORTAL-123: Dashboard status display
   Depends on: CORE-456
   
2. PORTAL-124: Filter by policy status
   Depends on: PORTAL-123
   
3. CORE-456: API: Add status field
   Depends on: DB-078
   
4. PORTAL-125: E2E tests for status
   No dependencies listed
   
5. REPORT-200: Status export to CSV
   No dependencies listed
```

## Example Output

```
SPRINT 15 DEPENDENCY HEALTH REPORT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUMMARY
  🟢 Healthy:     2 stories
  🟡 At Risk:     2 stories  
  🔴 Conflict:    1 story

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 CONFLICTS (Fix Required)

PORTAL-124 "Filter by policy status"
├── Depends on: PORTAL-123
├── Issue: PORTAL-123 also in this sprint
└── Risk: If PORTAL-123 slips, PORTAL-124 blocked
    RECOMMENDATION: Sequence PORTAL-123 early in sprint

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟡 AT RISK (Monitor)

PORTAL-123 "Dashboard status display"
├── Depends on: CORE-456
├── Issue: CORE-456 also in this sprint  
└── Risk: Tight timing if API work runs long
    RECOMMENDATION: Complete CORE-456 in first half

CORE-456 "API: Add status field"
├── Depends on: DB-078
├── Issue: DB-078 NOT in sprint!
└── Risk: Missing prerequisite
    RECOMMENDATION: Add DB-078 to sprint or verify complete

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📎 MISSING DEPENDENCIES (Suggested)

PORTAL-125 "E2E tests for status"
├── No dependencies listed
├── Likely depends on: PORTAL-123, PORTAL-124
└── RECOMMENDATION: Add links to upstream stories

REPORT-200 "Status export to CSV"
├── No dependencies listed  
├── Likely depends on: CORE-456 (needs API status field)
└── RECOMMENDATION: Verify with team, add link if confirmed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 RECOMMENDED SEQUENCING

Phase 1 (Days 1-3):
  ✓ DB-078: Schema migration (if not done)
  ✓ CORE-456: API status field

Phase 2 (Days 4-7):
  ← PORTAL-123: Dashboard display
  ← REPORT-200: CSV export

Phase 3 (Days 8-10):
  ← PORTAL-124: Filter feature
  ← PORTAL-125: E2E tests
```

## Follow-Up Actions
1. Resolve 🔴 conflicts before sprint starts
2. Monitor 🟡 at-risk items daily
3. Review suggested missing dependencies with team
