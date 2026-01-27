
---
title: "Epic Crafting Guide"
author: "A Practical Guide for Business Analysts and Product Owners"
date: "2025-10-29"
---

# Epic Crafting Guide

## 1. Introduction

An epic is a container for a significant, measurable business capability. Its purpose is to break down a large strategic initiative, as defined in the **Project Requirements Document (PRD)**, into a manageable chunk of work that can be delivered by a development team over several sprints.

This guide provides a step-by-step process for Business Analysts (BAs) to translate a high-level PRD into well-structured, valuable, and AI-friendly epics.

---

## 2. Epic Types

Every initiative is composed of two kinds of work, which translate into two types of epics.

### Business Epics (Functional)

These epics are focused on delivering a tangible piece of functionality directly to the end-user.

-   **Source:** Derived from the **"Functional Envelope"** section of the PRD.
-   **Focus:** Delivering a complete, end-to-end user journey or capability.
-   **Example:** If the PRD calls for a "new user onboarding experience," a Business Epic might be "Implement Self-Service User Registration."

### Enabler Epics (Non-Functional / Architectural)

Enabler Epics build the foundational infrastructure and services needed to support future Business Epics.

-   **Source:** Derived from the **"Architecture Overview"** and **"Cross-Cutting Concerns"** sections of the Architecture Hub document.
-   **Focus:** Building a reusable service, a piece of infrastructure, or implementing a core technical capability.
-   **Example:** To support the "Implement Self-Service User Registration" Business Epic, you might first need an Enabler Epic called "Build the User Authentication Microservice."

A successful project requires a balance of both Business and Enabler Epics.

---

## 3. Vertical Slicing

Effective epics and their child stories are "vertically sliced," meaning each slice delivers a small, recognizable piece of end-to-end value, cutting through all layers of the tech stack (UI, API, Database).

**Benefits of Vertical Slicing:**

-   **Testability:** A vertical slice can be tested from the user's perspective, enabling the QA Agent to generate meaningful end-to-end tests.
-   **Clarity:** It provides richer context for the Dev Agent when it generates code.
-   **Incremental Value:** Each slice can be deployed independently, allowing for faster feedback.

When crafting epics, always think vertically. The epic "Implement User Profile Management" is a good vertical epic because it can be broken down into smaller vertical stories like "View Profile," "Edit Profile," and "Upload Avatar."

---

## 4. PRD to Epic Workflow with `Agent: Decompose-Epics`

Decomposing a PRD into epics is an interactive, collaborative process between the Business Analyst and the `Agent: Decompose-Epics`.

### Step 1: Initiation & Analysis

The BA invokes the `Agent: Decompose-Epics`, providing the completed **PRD** and **Architecture Hub** as context. The agent analyzes these documents to identify and propose candidate epics.

> **BA Prompt:** *"Based on the provided PRD and Architecture Hub, propose a list of 3-5 candidate epics, separating them into Business and Enabler epics."*

### Step 2: Collaborative Refinement

The agent returns a list of suggested epics. The BA then collaborates with the agent to refine the details of each epic:

-   **Defining Scope:** The BA can ask the agent to propose "In Scope" and "Out of Scope" items for review and editing.
-   **Setting Success Metrics:** The BA provides key business objectives, and the agent helps formulate them into specific, measurable success metrics.
-   **Drafting Acceptance Criteria:** The BA describes high-level goals, and the agent drafts clear, business-facing acceptance criteria.

### Step 3: Finalization and Handoff

Once the BA is satisfied with an epic's definition, they approve it. The `Agent: Decompose-Epics` then performs the final handoff:

-   Creates the epic in Jira, populating all defined fields.
-   Updates the **PRD**'s "Traceability & Status" section with the new Jira Epic ID to establish a traceability link.

This workflow ensures that every epic is well-structured, aligned with standards, and created efficiently.