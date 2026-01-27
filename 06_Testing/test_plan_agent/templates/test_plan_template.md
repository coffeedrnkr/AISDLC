# Test Plan: [Story ID]

**Story Link**: [Link to User Story]
**Date**: [YYYY-MM-DD]

## 1. Test Strategy
*   **Scope**: [What is being tested]
*   **Out of Scope**: [What is NOT being tested]
*   **Risk Analysis**: [Potential risks/complexities]

## 2. Test Cases

### 2.1 Unit Tests (Logic & Components)
| ID | Description | Input Data | Expected Output | Automation Strategy |
|----|-------------|------------|-----------------|---------------------|
| UT-01 | [Description] | [Input] | [Expected] | [Jest/PyTest Mocking?] |

### 2.2 Integration Tests (API & Database)
| ID | Description | Pre-conditions | Steps | Expected Result |
|----|-------------|----------------|-------|-----------------|
| IT-01 | [Description] | [State] | 1. Call API... | 200 OK, DB updated |

### 2.3 End-to-End Tests (Playwright / UI)
*   **Scenario**: [Happy Path / Edge Case]
*   **Test Data**: [User accounts, etc.]
*   **Steps**:
    1.  Navigate to...
    2.  Click...
    3.  Assert...
*   **Playwright Locators Strategy**: [e.g., Use `data-testid` or accessible role]

## 3. Test Data Requirements
*   [ ] User with role "Admin"
*   [ ] Product with inventory > 0
