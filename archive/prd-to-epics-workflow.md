---
title: "From Spec to Slices: The PRD-to-Epics Workflow"
author: "Engineering Enablement"
date: "2025-01-24"
---

# 🍰 From Spec to Slices: The PRD-to-Epics Workflow

## 1. Introduction

A common failure mode in software planning is **Horizontal Slicing** (e.g., "Build the Database," "Build the UI"). This leads to integration hell. The **PRD-to-Epics Workflow** uses the `Agent: Epic Decomposer` to force **Vertical Slicing**—breaking a project into end-to-end features that deliver value independently.

**The Magic:** The AI reads the *functional intent* and ignores the *technical layer*, naturally grouping things by "User Value" rather than "Code Location."

---

## 2. Step 1: The Monolith (Process Input)

The input is the **PRD** (created in the previous workflow) + the **Architecture Hub**.

> **Input PRD:** "The system must allow users to upload clothes, view them, and get recommendations."
> **Input Arch:** "React Frontend, Python Backend, Firestore DB."

A human might look at this and say "Okay, Task 1: Setup React. Task 2: Setup Python." This is wrong.

---

## 3. Step 2: The Decomposition (The "Analyzer Mode")

The `Agent: Epic Decomposer` reads the documents and scans for **Functional Boundaries**.

**Agent Logic:**
1.  It sees "Upload Clothes" involves UI (Upload Form), API (`POST /item`), and DB (Save Item). -> **Epic Candidate 1**
2.  It sees "Get Recommendations" involves UI (Daily Page), API (`GET /recommend`), and AI (Gemini integration). -> **Epic Candidate 2**

**Agent Output (The Proposal):**
> "Based on the PRD, I recommend decomposing this project into 3 Vertical Epics:
> 
> 1.  **Clothing Management** (Upload, Edit, Delete items)
> 2.  **Recommendation Engine** (Weather integration, Outfit generation)
> 3.  **User Profiles** (Preferences, Account settings)
> 
> *Constraint Check:* 'Authentication' is required for all of these. I propose an 'Enabler Epic': **Identity Infrastructure**."

---

## 4. Step 3: The Refinement (Scope & Boundaries)

The user reviews the proposal.

**Agent Query:**
> "In **Clothing Management**, do you want 'Image Resizing' included in the first slice, or should we push that to a later 'Optimization' epic?"

**User Response:**
> "Push it to later. MVP just needs raw uploads."

**Agent Action:** The agent explicitly marks "Image Resizing" as `[OUT OF SCOPE]` in the Epic definition, preventing scope creep.

---

## 5. Step 4: The Output (The "Jira Ready" Epics)

The agent generates the Epic documentation, ready to be pasted into Jira.

**Output Fragment:**
```markdown
# Epic: Clothing Management (EPA-001)

## 1. Business Value
Allows users to build their digital closet, which is the prerequisite data for recommendations.

## 2. In Scope
*   Upload photo from camera/gallery
*   Tagging (Warmth, Formality)
*   List view of all items

## 3. Out of Scope
*   Image editing/cropping (Moved to EPA-004)
*   Automatic background removal
```

## 6. Summary

| Input | Process | Output |
| :--- | :--- | :--- |
| **Monolithic PRD** | Agent identifies **Value Streams** | **Vertical Slices** |
| **Technical Stack** | Agent maps **Dependencies** | **Enabler Epics** |
| **Feature List** | Agent negotiates **MVP Boundaries** | **Scoped Epics** |
