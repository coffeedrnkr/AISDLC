# Full Impact Assessment Prompt

## Purpose
Assess the complete blast radius of a requirement change across all artifacts.

## When to Use
- New feature request
- Requirement modification
- Feature removal
- Scope change request

## Prompt Template

```
Assess the full impact of this proposed change:

## Change Description
Type: [ADD / MODIFY / REMOVE]
Description: [What is changing?]
Requestor: [Who requested this?]
Priority: [High / Medium / Low]

## Current Context
[Provide or reference: PRD, relevant Epics, Architecture docs]

## Output Required
1. **PRD Impact**
   - Sections affected
   - Goals/metrics changed
   
2. **Epic Impact**
   - New Epics needed?
   - Existing Epics modified?
   - Epics orphaned?
   
3. **Story Impact**
   - New stories needed (with estimates)
   - Existing stories affected
   - Stories to remove
   - Total effort change
   
4. **Architecture Impact**
   - Components affected
   - New components needed
   - Interface changes
   - Data model changes
   - Non-functional implications
   - ADRs needed
   
5. **Timeline Impact**
   - Sprints affected
   - Dependencies changed
   - Release date impact
   
6. **Recommendation**
   - Proceed / Defer / Alternative?
   - Conditions for proceeding
   - Risks to accept
```

## Example Output

See Chapter 17 in the Complete Framework Guide for a full example report showing:
- Change summary
- Impact by layer (PRD → Epic → Story → Architecture → Timeline)
- Severity ratings (🟢/🟡/🔴)
- Artifacts to update
- Recommendations with conditions

## Follow-Up Actions
1. Review impact assessment with stakeholders
2. Make go/no-go decision
3. If proceeding, update artifacts in order:
   - PRD first
   - Then Epics
   - Then Stories
   - Then Architecture docs
4. Update sprint planning
