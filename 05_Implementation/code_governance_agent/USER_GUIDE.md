# Code Governance Agent User Guide

## Overview
The **Code Governance Agent (Agent 6)** automates code quality and security reviews. It combines traditional static analysis tools with AI reasoning to provide a comprehensive review against your organization's standards (fetched from Confluence).

## Core Capabilities
1.  **Static Analysis**:
    *   **Ruff**: Extremely fast Python linter and formatter. Checks for PEP8, unused imports, etc.
    *   **Bandit**: Security linter. Checks for common vulnerabilities like SQL injection and hardcoded secrets.
2.  **Context-Aware AI Review**:
    *   Fetches the "Code Governance & Security Standards" directly from your Confluence Space (`SD`).
    *   Uses **Gemini 3.0** (`gemini-3-flash-preview`) to review your code in the context of these specific rules.
    *   Provides actionable refactoring advice.

## Prerequisites
*   **Environment**: Ensure `.env` contains:
    *   `GEMINI_API_KEY`
    *   `CONFLUENCE_URL`, `CONFLUENCE_USER_EMAIL`, `CONFLUENCE_API_TOKEN`
    *   `GEMINI_MODEL=gemini-3-flash-preview`
*   **Dependencies**: `pip install ruff bandit atlassian-python-api markdown`

## Usage

### Option A: Terminal (Standard)
```bash
cd 05_Implementation/code_governance_agent
python code_governance_agent.py --target ../path/to/code
```

### Option B: Gemini Slash Command
```
/code-review
```

### Option C: Natural Language (MCP)
> "Review this code for security vulnerabilities."
> "Run governance check on this file."

## Output
The agent prints progress to the console and saves a detailed report:
- `CodeGovernanceReport.md`: Contains the Static Analysis summary and the full AI Strategic Review.

## Troubleshooting
- **Confluence Error**: Ensure your API Token is valid and the Space Key (`SD`) exists.
- **Model Error**: Confirm `GEMINI_MODEL` is set to a valid model version in `.env`.
