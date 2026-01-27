# Workflow: Epic to Story

This workflow guides you through generating User Stories from elaborated Epics.

---

## Prerequisites
- Elaborated Epic file (e.g., `outputs/EPIC-001_elaborated.md`)
- Architecture documentation (optional, for technical context)

---

## Steps

### 1. Generate Stories
```bash
/story-gen --epic outputs/EPIC-001_elaborated.md
```
- Agent uses INVEST criteria.
- Generates BDD/Gherkin acceptance criteria.
- Output: `outputs/stories/Story-001-*.md`

### 2. Review Stories
For each story:
- [ ] Is it Independent?
- [ ] Is it Negotiable?
- [ ] Is it Valuable?
- [ ] Is it Estimable?
- [ ] Is it Small?
- [ ] Is it Testable?

### 3. Refine Acceptance Criteria
- Ensure Given/When/Then scenarios are realistic.
- Add edge cases discovered during elaboration.

### 4. Sync to Jira (Optional)
```bash
/story-gen --epic outputs/EPIC-001_elaborated.md --sync --project_key MYPROJ
```

---

## Next Workflow
→ Architecture Design: `/arch-design`
→ Implementation: Start coding with stories as context.
