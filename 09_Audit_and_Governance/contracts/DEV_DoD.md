# Definition of Done: Builder Agent (Dev)
**Agent ID:** `BUILDER_AGENT` (aka `DEV_AGENT`)
**Artifact:** Source Code (`src/`, `lib/`)

## 1. Completeness Checks (The Inventory)
*   [ ] **Implementation:** Does the code actually perform the logic described in the Story?
*   [ ] **Test Coverage:** Are there corresponding Unit Tests in `tests/`?
*   [ ] **Docstrings:** Does every public function/class have a docstring?

## 2. Quality Checks (The Standard)
*   [ ] **Linter (Ruff):** Zero errors?
*   [ ] **Complexity:** No function > 10 Cyclomatic Complexity?
*   [ ] **Secrets:** No hardcoded tokens?
*   [ ] **Style:** Follows `.gemini/STYLEGUIDE.md`?

## 3. Traceability Checks (The Red Thread)
*   [ ] **The Golden Rule:** Top of file MUST have `@implements <STORY_ID>`.
    *   ```python
        """
        User Service.
        @implements STORY-123
        """
        ```
