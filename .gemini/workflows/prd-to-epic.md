# Workflow: PRD to Epic

This workflow guides you through generating Epics from a PRD.

---

## Steps

### 1. Generate PRD (if not exists)
```bash
/prd-discover
```
- Use the 9 discovery tools to mine requirements.
- Output: `outputs/PRD_Interactive_Final.md`

### 2. Review PRD
- Check `outputs/PRD_Interactive_Final.md` for gaps.
- Ensure all sections are complete.
- Get stakeholder sign-off.

### 3. Decompose PRD into Epics
```bash
/epic-split --prd outputs/PRD_Interactive_Final.md
```
- Agent uses SPIDR methodology.
- Output: `outputs/epic_breakdown.md`

### 4. Review Epic Breakdown
- Check each Epic for INVEST compliance.
- Verify dependencies make sense.
- Adjust sizes if needed.

### 5. Elaborate Each Epic
For each Epic in `epic_breakdown.md`:
```bash
/epic-elaborate --epic outputs/EPIC-001.md --interactive
```
- Use CRUD, State, BDD tools.
- Output: `outputs/EPIC-001_elaborated.md`

---

## Session State
- Open questions are saved to `outputs/open_questions.md`.
- Session summaries are logged to `outputs/session_log.md`.

---

## Next Workflow
→ See: `epic-to-story.md`
