# Dependency Discovery Prompt

## Purpose
Analyze stories/epics to identify hidden or missing dependencies.

## When to Use
- After creating new stories
- During backlog grooming
- When breaking down epics into stories

## Prompt Template

```
Analyze this story/epic and identify all potential dependencies:

## Story/Epic Content
[Paste story title and description]

## Backlog Context (Optional)
[Paste related stories or provide Jira project key for context]

## Output Required
1. **Suggested predecessors** — What must complete before this work
2. **Suggested successors** — What this work unblocks
3. **External dependencies** — Work from other teams
4. **Technical dependencies** — Shared components, APIs, databases
5. **Confidence level** — High/Medium/Low for each suggestion
```

## Example Input

```
Story: Update dashboard to show new policy status

As a portfolio manager, I want to see the current status of each policy 
in the dashboard so that I can quickly identify policies requiring attention.

Acceptance Criteria:
- Display status badge for each policy row
- Status options: Active, Pending, Lapsed, Cancelled
- Badge colors match status type
```

## Example Output

```
DEPENDENCY ANALYSIS

SUGGESTED PREDECESSORS (Must complete first):
1. 🔴 HIGH: API: Add status field to policy endpoint
   - This story displays status but needs the API to return it
   - Look for: Story updating PolicyController or PolicyService
   
2. 🟡 MEDIUM: Database: Add status column to policies table
   - If status doesn't exist in DB, migration needed first
   - Check: Is there a schema migration planned?

SUGGESTED SUCCESSORS (This unblocks):
1. E2E Tests: Policy status display
2. Filter stories: Filter by policy status

EXTERNAL DEPENDENCIES:
- None detected

TECHNICAL DEPENDENCIES:
- Policy API contract (needs status field)
- Dashboard component library (StatusBadge component)

RECOMMENDED JIRA LINKS:
| This Story | Link Type | Target |
|:-----------|:----------|:-------|
| PORTAL-123 | Depends on | CORE-456 (Policy API update) |
| PORTAL-123 | Depends on | DB-078 (Schema migration) |
```

## Follow-Up Actions
1. Review suggestions with team
2. Create linked issues in Jira if accepted
3. Update sprint planning based on dependencies
