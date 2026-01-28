# Scope Change Analysis Prompt

## Purpose
Analyze the impact of reducing scope (cutting features or requirements).

## When to Use
- Budget reduction
- Timeline compression
- Resource constraints
- Feature prioritization

## Prompt Template

```
Analyze the impact of reducing scope:

## Scope Reduction
What's being cut:
[List features/requirements being removed]

Reason:
[Budget / Timeline / Priority shift / Other]

## Current State
[Provide current PRD, Epics, Stories in progress]

## Output Required
1. **Stories to Remove**
   - List with IDs and effort saved
   - Total points freed up
   
2. **Orphaned Work**
   - Work that no longer makes sense without cut features
   - Dependencies on removed features
   
3. **Dependencies Affected**
   - What other work depends on cut features?
   - External dependencies impacted?
   
4. **Effort Savings**
   - Story points saved
   - Sprints freed up
   - Cost reduction estimate
   
5. **Risks Introduced**
   - What capability gaps remain?
   - User experience impacts?
   - Technical debt created?
   - Future work made harder?
   
6. **Recommendation**
   - Proceed with cut?
   - Partial cut alternative?
   - Defer instead of cut?
```

## Example Input

```
Scope Reduction:
- Cut "PDF Export" feature (EPIC-003)
- Cut "Advanced Filtering" (Stories 45-48)
- Reduce "Reporting" to basic reports only

Reason: Timeline compression - need to hit Q2 release

Current State:
- Sprint 12: 5 stories in progress
- Sprint 13-14: Planned with all features
- Total planned: 45 story points
```

## Example Output

```
SCOPE REDUCTION ANALYSIS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STORIES TO REMOVE: 12 stories, 23 points
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Story | Title | Points | Status |
|:------|:------|:-------|:-------|
| S-045 | PDF Export button | 3 | Not started |
| S-046 | PDF generation service | 8 | Not started |
| S-047 | PDF templates | 5 | Not started |
| S-048 | Advanced filter UI | 3 | Not started |
| S-049 | Filter persistence | 2 | Not started |
| S-050 | Filter sharing | 2 | Not started |

ORPHANED WORK: 2 stories
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Story | Issue |
|:------|:------|
| S-051 | E2E tests for PDF (depends on cut feature) |
| S-052 | Export analytics (depends on PDF + other) |

Recommendation: Remove S-051, keep S-052 (still useful for CSV)

EFFORT SAVINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Story Points: 23 points saved
Sprints: ~2.5 sprints freed
Dev Cost: ~$45K saved (at loaded rate)

RISKS INTRODUCED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟡 User Experience: Power users expect PDF export
🟡 Competitive: Competitors have this feature  
🟢 Technical Debt: None - clean cut
🟡 Future Work: Will need to add back post-MVP

RECOMMENDATION: PROCEED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Cut is clean with minimal ripple effects.
Add to post-MVP roadmap to restore capability.
```
