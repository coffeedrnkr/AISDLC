---
title: "From Spark to Spec: The Idea-to-PRD Workflow"
author: "Engineering Enablement"
date: "2025-01-24"
---

# 💡 From Spark to Spec: The Idea-to-PRD Workflow

## 1. Introduction

The hardest part of software development is often **ambiguity**. "I want a clothes picker" can mean a million different things. The **Idea-to-PRD Workflow** leverages the `Agent: PRD Collaborator` to act as an unwearied interviewer, forcing clarity through structured dialogue.

**The Magic:** The AI doesn't just write what you say; it asks what you *didn't* say.

---

## 2. Step 1: The Spark (Process Input)

The workflow begins with a **Vague Input** from a Product Owner or Stakeholder.

> **User Input:** "I want to build an app that picks my outfit for the day based on the weather."

In a traditional process, a BA would spend days scheduling meetings to clarify this. In our AI-Augmented SDLC, this is the "Seed Prompt."

---

## 3. Step 2: The Interrogation (The "Interviewer Mode")

The user invokes the `Agent: PRD Collaborator`. The agent initializes the **Enterprise PRD Template** and begins a section-by-section interview.

### 2.1 Business Intent & Problem Framing
The agent parses the "Spark" and immediately identifies missing context.

**Agent Query:**
> "That sounds useful. To define the **Business Intent**, I need to know:
> 1.  **Target Audience:** Is this for fashionistas who own 500 items, or busy professionals who just want to be presentable?
> 2.  **Success Metric:** How do we know if the app is working? Is it 'Time saved getting dressed' or 'Number of compliments received'?"

**User Response:**
> "It's for busy professionals. Success is time saved."

**Agent Action:** The agent synthesizes this into professional prose for Section 1 of the PRD.

### 2.2 The Functional Envelope (Scope Definition)
The agent now proposes a scope based on similar apps in its training data.

**Agent Proposal:**
> "For a 'Weather-Based Outfit Picker', I recommend the following scope (Functional Envelope):
> *   **Weather API Integration:** Real-time checking.
> *   **Digital Closet:** User uploads photos of clothes.
> *   **Recommendation Engine:** Matching weather data to fabric types (e.g., No linen in winter).
> 
> *Constraint Check:* Do we need to handle laundry status? (i.e., Don't pick dirty clothes?)"

**User Response:**
> "Yes, that's critical. Add a 'Dirty Hamper' status."

**The Magic:** The user didn't think of laundry. The AI did, preventing a major functional gap later.

---

## 4. Step 3: The Refinement (NFRs & Compliance)

The agent moves to the "boring" sections that humans often skip.

### Non-Functional Requirements (NFRs)
**Agent Query:**
> "You mentioned 'Time Saved'. Does the recommendation need to appear instantly (<200ms) or is a daily morning notification acceptable?"

### Compliance & Data
**Agent Query:**
> "You are uploading user photos. We must add a **Privacy & Data Classification** section. I will mark user photos as 'PII - Sensitive'. Do you agree?"

---

## 5. Step 4: The Output (The "Golden" PRD)

The agent compiles the dialogue into a structured Markdown document (`doc_info/PRD.md`).

**Output Fragment:**
```markdown
# Project Requirements Document: Daily Stylist

## 1. Business Intent
**Goal:** Reduce decision fatigue for busy professionals by automating daily outfit selection.
**Primary Metric:** Reduce "getting ready" time from 15 minutes to 2 minutes.

## 2. Functional Envelope
...
### 2.3 Clothing Management
*   **[MUST]** Support properties: Warmth Rating, Water Resistance, Formality.
*   **[MUST]** Laundry Status Tracking (Clean vs. Dirty).
...
```

## 6. Summary

| Input | Process | Output |
| :--- | :--- | :--- |
| **Vague Idea** | Agent asks **Clarifying Questions** | **Structured Intent** |
| **Implicit Assumptions** | Agent proposes **Scope & Edges** | **Explicit Envelope** |
| **Forgotten NFRs** | Agent enforces **Templates** | **Compliant Spec** |
