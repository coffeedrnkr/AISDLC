# AI Components Inventory

This document provides a comprehensive inventory of the AI Agents, Prompts, and Scripts used within the AI-Augmented SDLC.

## 1. Definitions

*   **AI Agents**: Specialized functional units (usually Python programs) that orchestrate complex tasks, often chaining multiple AI calls or interacting with the filesystem/APIs.
*   **Prompts**: Specific instructions sent to the Large Language Model (LLM). These can be:
    *   **External**: Standalone Markdown (`.md`) files that you can edit directly.
    *   **Embedded**: Hardcoded strings inside the Agent's Python code (for fixed logic).
*   **Scripts**: Utility code or entry points that run the agents or perform automation tasks without necessarily using AI (e.g., CI/CD checks).

---

## 2. Agent Inventory

There are **7 Standardized Agents** in the system. All are capable of running via CLI or being deployed as containers.

| Phase | Agent Name | Location | Role | Implementation |
| :--- | :--- | :--- | :--- | :--- |
| **01** | **PRD Agent** | `01_Requirements/prd_agent/` | Requirements Analyst | Synthesizes PRD from raw docs. |
| **02** | **Epic Agent** | `02_Elaboration/epic_agent/` | Product Owner | Decomposes PRD into Epics (SPIDR). |
| **02** | **Story Agent** | `02_Elaboration/story_agent/` | Technical BA | Generates User Stories (INVEST/Gherkin). |
| **03** | **UX Agent** | `03_UX_Design/ux_agent/` | UX Architect | Generates Personas, Reviews, Wireframes. |
| **04** | **Architecture Agent** | `04_Architecture/architecture_agent/` | Systems Architect | Generates System Design, DBML, OpenAPI, Diagrams. |
| **06** | **Test Plan Agent** | `06_Testing/test_plan_agent/` | QA Engineer | Generates Test Plans and Playwright Specs. |
| **08** | **Governance Agent** | `08_Governance/governance_agent/` | Security Champion | Runs Code Reviews and compliance checks. |

## 3. Micro-Agent Capabilities

The new **Micro-Agents** (UX, Architecture, Governance) support specific sub-tasks via the `--task` flag.

### Architecture Agent
*   `--task system_design`: Generates High-Level Design.
*   `--task dbml`: Generates Database Schema.
*   `--task openapi`: Generates API Specifications.
*   `--task diagrams`: Generates Python Diagrams-as-Code.

### UX Agent
*   `--task personas`: Generates User Personas.
*   `--task review`: conducts Heuristic Evaluations.
*   `--task wireframes`: Generates Mermaid Wireframes.

### Governance Agent
*   `--task review`: Conducts AI-driven Code Review & Security Audit.

