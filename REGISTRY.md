# Agent Registry & Slash Commands

This document serves as the **catalog of available AI Agents** in this project.
These agents can be triggered directly from Gemini Code Assist using the slash commands defined below.

## 🟢 Requirement & Discovery Agents

| Command | Agent | Description |
| :--- | :--- | :--- |
| **`/prd-discover`** | **PRD Agent** | **Interactive Mode**. Coaches you through the 9 Discovery Tools (Mind Map, Roleplay, etc.) to build a robust PRD. |
| **`/epic-split`** | **Decomposition Agent** | Splits a PRD into Epics using **SPIDR** patterns (Spike, Path, Interface, Data, Rules). |
| **`/epic-elaborate`** | **Elaboration Agent** | **Interactive Mode**. Fleshes out a single Epic with CRUD matrices, State diagrams, and Edge cases. |
| **`/story-gen`** | **Story Agent** | BDD-style user story generation from fully elaborated Epics. |

## 🔵 Design & Architecture Agents

| Command | Agent | Description |
| :--- | :--- | :--- |
| **`/ux-personas`** | **UX Agent** | Generates detailed User Personas based on key requirements. |
| **`/ux-wireframe`** | **UX Agent** | Creates text-based wireframe descriptions for specific stories. |
| **`/arch-design`** | **Architecture Agent** | Generates High-Level System Design (HLD) documents. |
| **`/arch-dbml`** | **Architecture Agent** | Generates DBML database schemas. |

## 🟠 Implementation & Quality Agents

| Command | Agent | Description |
| :--- | :--- | :--- |
| **`/code-review`** | **Governance Agent** | Runs Static Analysis (Ruff/Bandit) + AI Governance Review against standards. |
| **`/test-plan`** | **Test Plan Agent** | Generates test strategy and test cases from user stories. |
| **`/simulate-persona`** | **Simulation Agent** | Generates persona-based edge cases and stress tests. |
| **`/load-test`** | **Resilience Agent** | Generates k6/Locust load test scripts from API specs. |
| **`/chaos-test`** | **Resilience Agent** | Generates chaos engineering scenarios (requires approval). |
| **`/ci-check`** | **Integration Agent** | Checks for missing artifacts, runs tests, and verifies release readiness. |

---

## How to Use

1.  Open **Gemini Code Assist** (Chat panel).
2.  Type the command (e.g., `/prd-discover`).
3.  Gemini will propose the terminal command.
4.  Click **"Run in Terminal"** (or press Enter).
