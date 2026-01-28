# Optimal Sequencing Prompt

## Purpose
Determine the best order to build stories based on dependencies.

## When to Use
- Sprint planning
- PI planning
- Replanning after scope changes

## Prompt Template

```
Given these stories, recommend the optimal build sequence:

## Stories with Dependencies
[Paste stories with known dependencies]

## Constraints (Optional)
[Any fixed dates, resource constraints, or priorities]

## Output Required
1. **Recommended phases** with rationale
2. **Critical path** — longest dependency chain
3. **Parallel opportunities** — work that can happen simultaneously
4. **Risk flags** — potential bottlenecks
```

## Example Input

```
Stories for Sprint 15:

1. CORE-456: API: Add status field
   - No dependencies
   - Estimate: 3 days
   
2. PORTAL-123: Dashboard status display
   - Depends on: CORE-456
   - Estimate: 3 days
   
3. PORTAL-124: Filter by policy status
   - Depends on: PORTAL-123
   - Estimate: 2 days
   
4. PORTAL-125: E2E tests
   - Depends on: PORTAL-123, PORTAL-124
   - Estimate: 2 days
   
5. REPORT-200: Status CSV export
   - Depends on: CORE-456
   - Estimate: 2 days
```

## Example Output

```
OPTIMAL BUILD SEQUENCE
Sprint 15 | 10 Working Days
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PHASE 1: FOUNDATIONS (Days 1-3)
┌────────────────────────────────┐
│ CORE-456: API status field     │ ← Critical path start
│ 📊 No dependencies             │
│ ⏱️  3 days                      │
│ 👤 Backend team                │
└────────────────────────────────┘

PHASE 2: DEPENDENT WORK (Days 4-7)
┌────────────────────────────────┐
│ PORTAL-123: Dashboard display  │ ← Critical path
│ 📊 Depends on: CORE-456        │
│ ⏱️  3 days                      │
│ 👤 Frontend team               │
├────────────────────────────────┤
│ REPORT-200: CSV export         │ ← PARALLEL
│ 📊 Depends on: CORE-456        │
│ ⏱️  2 days                      │
│ 👤 Reports team                │
└────────────────────────────────┘

PHASE 3: FEATURES (Days 7-9)
┌────────────────────────────────┐
│ PORTAL-124: Filter feature     │ ← Critical path
│ 📊 Depends on: PORTAL-123      │
│ ⏱️  2 days                      │
│ 👤 Frontend team               │
└────────────────────────────────┘

PHASE 4: VALIDATION (Days 9-10)
┌────────────────────────────────┐
│ PORTAL-125: E2E tests          │ ← Critical path end
│ 📊 Depends on: PORTAL-123, 124 │
│ ⏱️  2 days                      │
│ 👤 QA team                     │
└────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 CRITICAL PATH ANALYSIS

CORE-456 → PORTAL-123 → PORTAL-124 → PORTAL-125
Total: 10 days (matches sprint length!)

⚠️ WARNING: Zero buffer on critical path
   - Any slip on critical path stories delays sprint
   - Consider: Add scope buffer or reduce scope

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔀 PARALLEL OPPORTUNITIES

REPORT-200 can run parallel to PORTAL-123
✓ Both depend on CORE-456
✓ No overlap between teams
✓ 2-day efficiency gain

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️ RISK FLAGS

1. Critical path = sprint length (no buffer)
2. Frontend team has 3 back-to-back stories
3. E2E tests at end - if tests fail, no time to fix

RECOMMENDATIONS:
• Start CORE-456 immediately on Day 1
• Daily check-ins on critical path progress
• Consider moving 1 story to next sprint for buffer
```
