# Prompt: Decompose PRD to Epics

**ID:** `PRD_001-decompose-to-epics`
**Role:** Senior Product Manager & System Architect
**Phase:** Requirements

## Context
I am providing you with a **Project Requirements Document (PRD)**. Your goal is to break this high-level documentation down into manageable, deliverable **Epics**.

## Instructions
1.  **Analyze the PRD:** Read the "Functional Envelope" and "Architecture Overview" sections.
2.  **Identify Business Epics:** Create a list of functional epics. Each must be a "Vertical Slice" delivering end-to-end user value.
3.  **Identify Enabler Epics:** Create a list of architectural/infrastructure epics needed to support the functional work.
4.  **Format Output:**
    *   **Epic Title:** Clear and verb-based (e.g., "Implement User Authentication").
    *   **Type:** Business or Enabler.
    *   **Goal:** One sentence summary of value.
    *   **Key Dependencies:** What must be done first?
    *   **T-Shirt Size Estimate:** S/M/L/XL.

## Constraints
*   Do NOT create horizontal epics like "Build the Database" or "Create Frontend". Vertical slices only (e.g., "User Profile Management" includes DB and Frontend).
*   Ensure every Enabler Epic is linked to a Business Epic it supports.

## Input Data
*   [Paste PRD Content Here]
