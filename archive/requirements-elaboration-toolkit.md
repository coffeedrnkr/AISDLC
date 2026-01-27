---
title: "The Requirements Elaboration Toolkit"
author: "Engineering Enablement"
date: "2026-01-26"
---

# 🧰 The Requirements Elaboration Toolkit

## 1. Introduction

This toolkit defines the methodology for extracting "hidden" requirements. It goes beyond simple questionnaires and uses AI as an Archaeologist, miner, and Simulator to ensure no requirement is missed.

---

## 2. The 3 States of Information

Requirements are not just in documents. We categorize information into three states of matter, and AI assists uniquely in each.

| State | Description | AI Role | Tools |
| :--- | :--- | :--- | :--- |
| **SOLID (Documentation)** | Static regulations, SOPs, Legal text, Legacy Code, DB Schemas. | **The Auditor / Archaeologist** | **NotebookLM** (Synthesis), **DocAI** (Scanning) |
| **LIQUID (Conversation)** | Meetings, Slack threads, Transcripts, Brainstorming sessions. | **The Scribe / Miner** | **Gemini** (Transcript Analysis), **NotebookLM** (Audio Overviews) |
| **GAS (Unspoken Ideas)** | Latent thoughts, "what if" scenarios, edge cases not yet articulated. | **The Simulator** | **Gemini** (Persona Simulation, Edge Case Stress Testing) |

### Drilling for Gas (Unspoken Ideas)
The "Gas" state is where most requirements are missed. We use AI to extract these:
1.  **Brainstorming & Mind Mapping:** Open conversation with AI drawing out branches of thought (e.g., "If I add a payment, what about refunds? Receipts? Tax?").
2.  **Persona Simulation:** AI plays a persona (e.g., "70-year-old user", "Malicious Hacker") to stress-test the flow.
3.  **Edge Case Stress-Testing:** Generating "what if" failure modes (e.g., "Internet cuts out mid-sync").

---

## 3. The 3 Layers of Requirements

Requirements are organized into interlocking layers to ensure alignment from vision to code.

### Layer 1: The Strategic Vision (The North Star)
*   **Focus:** Outcomes, not features.
*   **Artifacts:** Pitch Deck, Business Case.
*   **AI Role:** Alignment check (Phase 1.5).

### Layer 2: The Logic Epic (Refinement)
*   **Focus:** Functional flow and user experience.
*   **The Artifact Pair:**
    1.  **The Text Spec:** The Epic Definition (Gherkin/Logic).
    2.  **The Visual Twin:** **Wireframes (UX Design Hub)**. *Note: Logic without visuals is invisible to AI.*
*   **AI Method:** **Form Filling** (AI acts as Expert BA), **BDD Translation**, **Wireframe Generation** (Technique D).

### Layer 3: The Technical Foundation (The Floor)
*   **Focus:** Non-functional requirements and data integrity.
*   **Artifacts:** API Contracts, DB Schemas, Compliance Rules.
*   **AI Role:** CRUD Analysis (finding orphaned states), Security Scanning.

---

## 4. Rethinking Document Format

To maximize AI collaboration, we shift from "Document-First" to **"Docs-as-Code"**.

1.  **Use Markdown (.md):** Easier and more compact for AI to read/write than Word/PDF.
2.  **Auto Sync:** Docs should live in the repo and sync with Jira.
3.  **Standard Style Guide:** Use `.gemini/` folder to store style guides that agents read.
4.  **Diagrams as Code:**
    *   **Logic Flow:** Mermaid.js (Sequence diagrams, flowcharts).
    *   **Infrastructure:** Python Diagrams Library (Architecture diagrams).
    *   **Data:** DBML (Database Markup Language).
    *   **API:** OpenAPI/Swagger.
