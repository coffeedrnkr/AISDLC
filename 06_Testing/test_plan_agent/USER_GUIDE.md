# Test Plan Generation Agent - User Guide

This guide describes how to use the **Test Plan Generation Agent** to convert User Stories into comprehensive, automation-ready Test Plans effectively "Shifting Left" the QA process.

## Methodology

### 1. Shift-Left Testing
We define tests *before* implementation details are finalized. This ensures:
*   **Clarity**: Edge cases are discovered early.
*   **Testability**: The design considers testing requirements from the start.

### 2. Testing Pyramid Strategy
The agent generates a plan covering three levels:
1.  **Unit Tests**: Low-level logic verification (e.g., "CalculateTotal returns correct sum").
2.  **Integration Tests**: Verifying boundaries (e.g., "API endpoint saves to DB").
3.  **E2E Tests (Playwright)**: Full user journeys mimicking real behavior.

## Inputs

1.  **User Story**: A Markdown file containing the Story and Gherkin Acceptance Criteria.
2.  **Architecture**: Technical context (optional but recommended for integration tests).

## Outputs

*   **Test Plan Markdown**: `outputs/test_plans/TestPlan-[StoryID].md`
    *   Detailed test cases with steps and expected results.
    *   Automation strategy for each case.

## How to Run

```bash
python test_plan_agent/main.py --story agents/story_agent/outputs/stories/Story_USR_001.md --output agents/test_plan_agent/outputs
```

## Review Workflow
1.  **Generate**: Run the agent.
2.  **Review**: Open the generated Test Plan.
3.  **Automate**: Use the plan as a blueprint for writing Playwright scripts and Unit tests.
