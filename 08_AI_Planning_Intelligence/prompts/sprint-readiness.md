# Sprint Readiness Check Prompt

## Purpose
Comprehensive pre-sprint assessment with Go/No-Go recommendation.

## When to Use
- Before sprint starts
- After scope changes mid-sprint
- At PI boundaries

## Prompt Template

```
Assess this sprint's readiness:

## Sprint Information
[Sprint name, dates, team]

## Sprint Stories
[Paste sprint contents with dependencies]

## Backlog Context
[Related backlog items not in sprint, external dependencies]

## Output Required
1. **Dependency health summary** (🟢/🟡/🔴)
2. **Conflicts requiring resolution**
3. **Risks to monitor**
4. **External dependency status**
5. **Go/No-Go recommendation**
```

## Example Input

```
Sprint: Sprint 15
Dates: Feb 3-14, 2026
Team: Portfolio Team

Sprint Stories:
1. PORTAL-123: Dashboard status display
   - Depends on: CORE-456
2. PORTAL-124: Filter by policy status  
   - Depends on: PORTAL-123
3. PORTAL-125: E2E tests
   - Depends on: PORTAL-123, PORTAL-124
4. REPORT-200: Status CSV export
   - Depends on: CORE-456

External Context:
- CORE-456: In Core Team's Sprint 15 (parallel sprint)
- DB-078: Schema migration (completed last sprint)
- Team B: PolicyService v2 API (in progress, expected Feb 10)
```

## Example Output

```
╔══════════════════════════════════════════════════════════════╗
║               SPRINT 15 READINESS ASSESSMENT                  ║
║                      February 3-14, 2026                      ║
╚══════════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 DEPENDENCY HEALTH SUMMARY

  Total Stories:    4
  🟢 Healthy:       1 (REPORT-200)
  🟡 At Risk:       2 (PORTAL-123, PORTAL-124)
  🔴 Conflict:      1 (PORTAL-125)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔴 CONFLICTS (Must Resolve Before Sprint)

1. PORTAL-125 "E2E tests"
   ├── Issue: Scheduled but dependencies in same sprint
   ├── Risk: 80% chance of being blocked
   └── Action Required:
       OPTION A: Move to Sprint 16 (recommended)
       OPTION B: Reduce scope to partial tests

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟡 AT-RISK ITEMS (Monitor During Sprint)

1. PORTAL-123 "Dashboard status display"
   ├── External Dep: CORE-456 (Core Team's sprint)
   ├── Risk: Core Team delivering in parallel
   └── Mitigation: 
       • Daily sync with Core Team on CORE-456 status
       • Have fallback mock if API delayed

2. PORTAL-124 "Filter by policy status"
   ├── Internal Dep: PORTAL-123 (same sprint)
   ├── Risk: Can't start until Day 5+ 
   └── Mitigation:
       • Frontend team works on PORTAL-123 first
       • Daily progress check

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌐 EXTERNAL DEPENDENCY STATUS

| Dependency | Owner | Status | ETA | Risk |
|:-----------|:------|:-------|:----|:-----|
| CORE-456 | Core Team | In Progress | Feb 7 | 🟡 Medium |
| DB-078 | DBA Team | ✅ Complete | Done | 🟢 None |
| PolicyService v2 | Team B | In Progress | Feb 10 | 🟡 Medium |

⚠️ AlertTeam B's Feb 10 delivery leaves only 2 days buffer

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 PRE-SPRINT CHECKLIST

☐ Resolve PORTAL-125 conflict (move or reduce scope)
☐ Confirm CORE-456 ETA with Core Team
☐ Create mock API fallback for PORTAL-123
☐ Schedule daily External Dependency standup
☐ Verify Team B PolicyService timeline

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚦 GO / NO-GO RECOMMENDATION

                    ⚠️ CONDITIONAL GO ⚠️

CONDITION: Resolve PORTAL-125 conflict before sprint starts

RATIONALE:
✓ Core stories have clear dependencies
✓ DB-078 prerequisite is complete  
✓ External dependencies are tracked
✗ PORTAL-125 conflict unresolved
✗ Zero buffer on critical path

IF CONDITION MET: Proceed with sprint
IF NOT RESOLVED: Delay sprint start by 1 day for replanning
```

## Follow-Up Actions
1. Address all checklist items
2. Get explicit confirmation on external dependencies
3. Communicate risks to stakeholders
4. Set up monitoring for at-risk items
