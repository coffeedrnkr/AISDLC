# Prompt: Generate Playwright Tests

**ID:** `QA_001-generate-playwright`
**Role:** QA Automation Engineer (SDET)
**Phase:** Testing

## Context
I need to automate the testing for a User Story. I have the **Gherkin Acceptance Criteria** and the **HTML Source** (or Semantic Locator descriptions) of the page.

## Instructions
1.  **Parse Gherkin:** Each `Scenario` becomes a `test()` block.
2.  **Map Steps:** `Given` -> `beforeEach` or setup. `When` -> Actions (click, fill). `Then` -> Assertions (expect).
3.  **Use Locators:** Use accessible locators (`getByRole`, `getByText`) rather than CSS/XPath where possible.
4.  **Resilience:** Add auto-waiting (Playwright does this by default, but ensure no hard sleeps).

## Output
*   Full `*.spec.ts` file content using Playwright test runner.

## Input Data
*   [Paste Gherkin ACs]
*   [Paste HTML Snippet or Wireframe Description]
