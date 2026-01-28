# The AI-Augmented SDLC: A Complete Guide

## About This Document

This guide provides a comprehensive explanation of the AI-Augmented Software Development Lifecycle (SDLC), designed for readers who may not have prior experience with software development methodologies, AI-assisted development, or the specific techniques referenced in this framework.

Every concept is explained from first principles, with real-world examples and practical context.

---

## Table of Contents

1. [Introduction: What is the AI-Augmented SDLC?](#1-introduction-what-is-the-ai-augmented-sdlc)
2. [The Ten Pillars](#2-the-ten-pillars)

4. [Requirements: The Three-Layer Framework](#4-requirements-the-three-layer-framework)
5. [Requirements: The States of Information](#5-requirements-the-states-of-information)
6. [Epic Decomposition: Breaking Down Large Features](#6-epic-decomposition-breaking-down-large-features)
7. [User Story Elaboration: Creating Work Packages](#7-user-story-elaboration-creating-work-packages)
8. [UX Design: The UX Architect Framework](#8-ux-design-the-ux-architect-framework)
9. [System-Wide UX: The Holistic Advantage](#9-system-wide-ux-the-holistic-advantage)
10. [Architecture: The Architecture Hub](#10-architecture-the-architecture-hub)
11. [Interfaces: The Four Layers of Integration](#11-interfaces-the-four-layers-of-integration)
12. [Implementation: Context-Driven Development](#12-implementation-context-driven-development)
13. [Testing: The Five Dimensions of Quality](#13-testing-the-five-dimensions-of-quality)
14. [Context Window Management: Getting the Best from AI](#14-context-window-management-getting-the-best-from-ai)
15. [Cross-System Coordination: Working Across Teams and Systems](#15-cross-system-coordination-working-across-teams-and-systems)
16. [AI Planning Intelligence: Continuous Dependency Management](#16-ai-planning-intelligence-continuous-dependency-management)
17. [Change Management: What-If Impact Assessment](#17-change-management-what-if-impact-assessment)

---

## 1. Introduction: What is the AI-Augmented SDLC?

### What is an SDLC?

The **Software Development Lifecycle (SDLC)** is a structured process that describes how software is planned, created, tested, and maintained. Traditional phases include:

- **Requirements** — What should the software do?
- **Design** — How should it be structured?
- **Implementation** — Writing the actual code
- **Testing** — Does it work correctly?
- **Deployment** — Making it available to users
- **Maintenance** — Fixing bugs and adding features

### What Does "AI-Augmented" Mean?

In this framework, **AI is a partner, not a replacement**. Artificial Intelligence (specifically, Large Language Models like Google's Gemini) assists humans at every phase:

| Traditional Approach | AI-Augmented Approach |
|:---------------------|:----------------------|
| Human writes all documents | AI drafts, human reviews and refines |
| Human draws all diagrams | AI generates from text descriptions |
| Human writes all code | AI suggests, human reviews and accepts |
| Human writes all tests | AI generates test cases from requirements |

**The key principle:** AI handles repetitive, time-consuming tasks so humans can focus on creative problem-solving, decision-making, and quality assurance.

### Why Does This Matter?

Studies show that developers spend significant time on repetitive tasks:
- 30-40% on writing boilerplate code
- 20-30% on writing documentation
- 15-20% on writing tests

AI assistance can dramatically reduce this time, allowing teams to:
- Deliver features faster
- Maintain higher quality documentation
- Catch more bugs before production
- Focus on innovation rather than repetition

---

## 2. The Nine Pillars

The AI-Augmented SDLC is built on nine foundational principles that govern how work is organized, tracked, and executed.

### Pillar 1: VS Code as Home Base

**What is VS Code?**

Visual Studio Code (VS Code) is a free, open-source code editor developed by Microsoft. It's the most popular development environment in the world, used by over 70% of professional developers.

**Why is this important?**

Instead of switching between multiple applications (one for writing code, another for documentation, another for chat, etc.), everything happens in one place:

| Capability | What It Does |
|:-----------|:-------------|
| **Gemini Code Assist** | AI assistant embedded in the editor that can answer questions, suggest code, and help debug problems |
| **Slash Commands** | Quick commands (like `/prd-discover`) that trigger AI agents to perform specific tasks |
| **Integrated Terminal** | Command-line interface inside VS Code for running programs and scripts |
| **Git Integration** | Version control built directly into the editor |
| **Jira Integration** | Track tickets and tasks without leaving the editor |

**Practical Example:**

A developer wants to create a new feature. Without leaving VS Code, they can:
1. Read the requirements (markdown file)
2. Ask the AI for clarification (`/prd-discover`)
3. Generate code with AI assistance
4. Run tests in the terminal
5. Commit changes to Git
6. Update the Jira ticket

### Pillar 2: Documentation as Code

**The Traditional Problem:**

Documentation often becomes outdated because:
- It's stored separately from code (in wikis, shared drives, or email)
- There's no review process for changes
- Nobody knows which version is current
- Changes aren't tracked

**The Solution: Treat Documentation Like Code**

All documentation is stored as plain text files (Markdown format) alongside the code in the same repository:

| Document Type | Traditional Storage | Documentation as Code |
|:--------------|:--------------------|:----------------------|
| Requirements (PRD) | Microsoft Word on SharePoint | `docs/PRD.md` in Git |
| Architecture Decisions | Email threads | `docs/decisions/ADR-001.md` in Git |
| API Documentation | Confluence wiki | `docs/api/openapi.yaml` in Git |

**What is Markdown?**

Markdown is a simple text format that uses symbols like `#` for headings and `*` for lists. This document is written in Markdown. Example:

```markdown
# This is a Heading

This is a paragraph with **bold text** and *italic text*.

- This is a bullet point
- This is another bullet point
```

**Why This Matters:**

- **Version Control:** Every change is tracked. You can see who changed what and when.
- **Review Process:** Documentation changes go through the same review process as code changes.
- **Single Source of Truth:** There's never confusion about which version is current.
- **AI Readability:** AI assistants can easily read and understand plain text files.

### Pillar 3: Diagrams as Code

**The Traditional Problem:**

Diagrams (flowcharts, architecture diagrams, etc.) are typically created in tools like Visio, Lucidchart, or PowerPoint. These diagrams:
- Become outdated quickly
- Are difficult to version control (binary files)
- Can't be reviewed in pull requests
- Must be manually updated

**The Solution: Generate Diagrams from Text**

Instead of drawing diagrams, we describe them in text and let tools generate the images automatically:

```mermaid
flowchart LR
    A[User] --> B[Web App]
    B --> C[Database]
```

This text produces a visual diagram showing a User connected to a Web App connected to a Database.

**Tools Used:**

| Purpose | Tool | What It Does |
|:--------|:-----|:-------------|
| **Flowcharts, Journeys** | Mermaid | Text-to-diagram tool built into many platforms |
| **System Architecture** | C4 Model + Mermaid | Standardized way to show system structure |
| **Data Models** | DBML | Text format for database schemas |
| **Infrastructure** | Python Diagrams | Python library that generates cloud architecture diagrams |
| **APIs** | OpenAPI | YAML/JSON format that generates API documentation |

### Pillar 4: Agent-Generated Artifacts

**What is an AI Agent?**

An AI Agent is a specialized AI program designed to perform a specific task. Unlike a general-purpose chatbot, an agent:
- Has a specific job (e.g., "split requirements into epics")
- Uses specialized prompts and templates
- Produces consistent, structured output
- Can integrate with other tools (Jira, Git, etc.)

**The Agents in This Framework:**

| Phase | Agent | What It Does |
|:------|:------|:-------------|
| Requirements | PRD Agent | Helps gather and organize requirements |
| Elaboration | Epic Agent | Breaks large features into manageable pieces |
| Elaboration | Story Agent | Creates detailed work packages for developers |
| UX Design | UX Agent | Creates user personas and wireframes |
| Architecture | Architecture Agent | Generates system diagrams and API specs |
| Testing | Test Plan Agent | Creates test plans and generates test code |

**Human-in-the-Loop (HITL):**

Every agent output is reviewed by a human before it becomes final. The AI drafts, the human approves (or edits and approves).

### Pillar 5: Git Version Control

**What is Git?**

Git is a version control system—a way to track changes to files over time. Think of it like "Track Changes" in Microsoft Word, but for an entire folder of files.

**Key Concepts:**

| Term | What It Means | Analogy |
|:-----|:--------------|:--------|
| **Repository (Repo)** | A folder whose history is tracked | A project folder with infinite undo |
| **Commit** | A snapshot of the entire folder at a point in time | Saving a version |
| **Branch** | A parallel version of the folder | A draft copy for experimenting |
| **Pull Request (PR)** | A request to merge changes from one branch to another | Submitting your draft for review |
| **Merge** | Combining changes from two branches | Accepting edits into the final version |

**Why Git Matters for This Framework:**

- **All artifacts in one repo:** Code, documentation, diagrams, and tests are stored together
- **Everything is reviewable:** Changes go through Pull Requests
- **Full history:** You can roll back any file to any previous version
- **AI can read it:** AI assistants can access the entire project history

### Pillar 6: AI Governance

**The Risk of Uncontrolled AI:**

AI is powerful but imperfect. Without guardrails:
- AI might generate incorrect code
- AI might expose sensitive data
- AI might hallucinate (confidently state incorrect facts)
- Changes might be applied without human review

**The Safeguards:**

| Safeguard | Type | What It Does |
|:----------|:-----|:-------------|
| **Guardrails** | Automatic | Detects PII (personal data), prevents hallucination, limits output size |
| **Human-in-the-Loop** | Always On | Every AI-generated change must be reviewed before it's saved |
| **Prompt Ops** | Automatic | Prompts are versioned and tested like code |
**The Key Principle:** AI never makes changes directly. It always proposes changes that a human must accept.

### Pillar 7: Context Management

**The Challenge:**

Even the largest AI models (2 million tokens) can't fit an entire codebase. Without strategy, AI lacks the context to give good answers.

**The Solution: Multi-Layer Context Strategy**

| Layer | Strategy | What It Does |
|:------|:---------|:-------------|
| **1. Pre-Processing** | NotebookLM | Summarizes bulk documents before development |
| **2. Hierarchical Chunking** | Index → Summary → Detail | Creates navigable document structures |
| **3. Context Drawer** | Code Assist UI | Explicitly include/exclude files for AI |
| **4. Caching** | Vertex AI API | Reuses common context (STYLEGUIDE, glossary) |
| **5. Session State** | SessionStateManager | Persists context across multi-day work |

**Key Principles:**
- **Pre-summarize:** Use NotebookLM for bulk documents
- **Reference, don't embed:** Link to documents instead of copying content
- **Progressive disclosure:** Summary always, details on-demand
- **Session persistence:** Track entities, open questions, next steps

> 📖 **Full Details:** See Chapter 14 for complete context management strategies.

### Pillar 8: AI Planning Intelligence

**The Problem:**

Jira backlogs are often incomplete:
- Stories created without dependency links
- Blockers discovered mid-sprint
- Cross-team dependencies hidden until too late
- Optimal build order is guesswork

**The Solution: Continuous AI Monitoring**

An always-on AI layer that watches, discovers, suggests, and manages dependencies across Jira:

| Capability | What It Does |
|:-----------|:-------------|
| **Watches** | Monitors backlog as items are created/edited |
| **Discovers** | Infers dependencies from story content (NLP) |
| **Suggests** | Proposes missing links for human approval |
| **Sequences** | Recommends optimal build order |
| **Alerts** | Notifies when dependency health changes |
| **Predicts** | Forecasts blockers before they occur |

**Key Principle:** This is Jira-centric — users plan backlogs and sprints in Jira, not VS Code.

> 📖 **Full Details:** See Chapter 16 for the complete AI Planning Intelligence framework.

### Pillar 9: Change Management

**The Problem:**

Requirements change constantly:
- New features requested mid-sprint
- Scope reduced due to budget/time
- Regulatory changes force modifications
- Stakeholder priorities shift

Without impact analysis, changes cause cascading problems.

**The Solution: What-If Impact Assessment**

Before any change is made, AI assesses the full blast radius:

| Change Type | AI Assesses Impact On |
|:------------|:----------------------|
| **Add Requirement** | PRD, Epics, Stories, Architecture, Timeline |
| **Modify Requirement** | Which artifacts need updates? How much rework? |
| **Remove Requirement** | What becomes orphaned? What's affected downstream? |

**Key Principle:** Assessment only — AI shows you the impact before you decide to proceed.

> 📖 **Full Details:** See Chapter 17 for the complete Change Management framework.

---

### Pillar 10: Jira Integration

### What is Jira?

Jira is the most widely used project management tool in software development. It tracks:
- **Epics** — Large features or initiatives
- **Stories** — Individual pieces of work
- **Tasks** — Specific to-do items
- **Bugs** — Problems that need fixing

### The Problem This Solves

In traditional workflows:
- Requirements live in one system (documents)
- Work tracking lives in another system (Jira)
- These systems often get out of sync
- Traceability is manual and error-prone

### The Solution: Bi-Directional Sync

This framework keeps Markdown documents and Jira tickets synchronized automatically:

| When This Happens | Jira Is Updated |
|:------------------|:----------------|
| AI generates an Epic document | A Jira Epic is created automatically |
| AI generates User Stories | Jira Stories are created and linked to the Epic |
| Status changes in Jira | The markdown document is updated |
| Description changes in markdown | The Jira ticket is updated |

### Traceability

Every artifact is linked:

```
PRD Section → Epic → Stories → Test Cases
```

This means:
- You can trace any test back to the original requirement
- You can see all stories that implement a given requirement
- You can identify which requirements are not yet implemented

---

## 3. Requirements: The Three-Layer Framework

### What Are Requirements?

Requirements describe what the software should do. They answer questions like:
- What problem are we solving?
- Who will use this software?
- What features are needed?
- How should it behave?

### The Three Layers

Requirements are organized into three distinct layers:

#### Layer 1: Strategic Vision (The "Why")

This layer focuses on business outcomes, not features:

- What problem are we solving?
- How will we measure success?
- What is the business value?

**Example:**

> ❌ Bad: "We need a login page"
> 
> ✅ Good: "Users must be able to securely access their accounts, reducing support calls by 30%"

**Output:** Program Requirements Document (PRD)

#### Layer 2: Logic & Design (The "What")

This layer describes the user experience and functional flows:

- What will users see and do?
- What are the step-by-step workflows?
- What are the screen layouts?

**Outputs:**
- Epic definitions
- User Stories with acceptance criteria
- Wireframes (visual layouts)

#### Layer 3: Technical Foundation (The "How")

This layer describes the technical constraints and architecture:

- What technology will we use?
- How will data be stored?
- What are the performance requirements?
- What are the security requirements?

**Outputs:**
- Architecture Decision Records (ADRs)
- System diagrams
- API specifications

---

## 4. Requirements: The States of Information

### The Challenge of Gathering Requirements

Requirements information comes from many sources in many forms:

- Existing documents (contracts, regulations, manuals)
- Conversations (meetings, interviews)
- Ideas that haven't been articulated yet

### The Three States of Information

This framework uses a physics analogy to categorize information sources:

#### Solid: Existing Documentation

**What it is:** Written documents that already exist

**Examples:**
- Regulatory documents
- Standard operating procedures
- Existing system documentation
- Database schemas
- Legacy code

**How AI helps:** AI tools like NotebookLM can:
- Summarize long documents
- Find conflicts between documents
- Extract key topics and requirements
- Answer questions about the content

#### Liquid: Conversations

**What it is:** Spoken information that needs to be captured

**Examples:**
- Meeting recordings
- Stakeholder interviews
- Workshop discussions

**How AI helps:**
- Transcribe audio to text automatically
- Summarize key points
- Extract action items and decisions
- Identify topics mentioned

#### Gas: Unspoken Ideas

**What it is:** Requirements that haven't been articulated yet—ideas that need to be discovered

**Examples:**
- Edge cases nobody thought about
- Assumptions that need to be validated
- "What if" scenarios

**How AI helps:**
- Mind mapping (exploring related concepts)
- Persona simulation ("What would a frustrated user do?")
- Edge case stress-testing
- Roleplay scenarios

---

## 5. Epic Decomposition: Breaking Down Large Features

### What is an Epic?

An **Epic** is a large body of work that can be broken down into smaller pieces. Think of it as a major feature or capability.

**Examples:**
- "User Registration and Login"
- "Shopping Cart and Checkout"
- "Reporting Dashboard"

### Why Break Down Epics?

Large features are difficult to:
- Estimate accurately
- Complete in a reasonable timeframe
- Test comprehensively
- Deliver incrementally

Breaking them down allows teams to:
- Deliver value faster (smaller pieces = faster delivery)
- Get feedback earlier
- Reduce risk (problems are caught sooner)
- Estimate more accurately

### Two Types of Epics

#### Business Epics (What Users See)

These deliver functionality directly to end users:
- Derived from the PRD's functional requirements
- Provide end-to-end user value
- Example: "Allow users to submit insurance claims online"

#### Enabler Epics (What Makes It Work)

These build the infrastructure needed by Business Epics:
- Derived from technical requirements
- Don't deliver direct user value, but are necessary
- Example: "Build the claims processing API"

### Vertical Slicing

**The Principle:** Each Epic should cut through all layers of the system (UI, API, Database) rather than being limited to one layer.

**Why This Matters:**

| Horizontal Slice (Bad) | Vertical Slice (Good) |
|:-----------------------|:----------------------|
| "Build the claims database" | "Submit a simple claim end-to-end" |
| Only addresses one layer | Addresses all layers |
| Can't be tested by users | Can be tested and demoed |
| No visible value | Delivers visible value |

### The SPIDR Framework

SPIDR is a methodology developed by Agile expert Mike Cohn for splitting large Epics into smaller pieces. Each letter represents a different splitting strategy:

#### S — Spike

**When to use:** When there's too much uncertainty to estimate

**What it means:** Separate the research from the implementation

**Example:**
- Original: "Integrate with payment gateway"
- Split into:
  - Spike: "Evaluate payment gateway options" (research)
  - Implementation: "Integrate with Stripe" (actual work)

#### P — Path

**When to use:** When a feature has multiple user journeys or scenarios

**What it means:** Handle the "happy path" first, then handle error cases

**Example:**
- Original: "Submit insurance claim"
- Split into:
  - "Submit simple claim successfully" (happy path)
  - "Handle claim rejection" (error path)
  - "Handle missing documents" (error path)

#### I — Interface

**When to use:** When a feature must work on multiple platforms

**What it means:** Start with one platform, add others later

**Example:**
- Original: "Mobile checkout"
- Split into:
  - "Web checkout"
  - "iOS checkout"
  - "Android checkout"

#### D — Data

**When to use:** When a feature handles multiple data types or sources

**What it means:** Start with one data type, add others later

**Example:**
- Original: "Import customer data"
- Split into:
  - "Import customer data from CSV"
  - "Import customer data from API"
  - "Import customer data from database"

#### R — Rules

**When to use:** When requirements have complex business rules

**What it means:** Start with simple rules, add complexity later

**Example:**
- Original: "Calculate insurance premium"
- Split into:
  - "Calculate premium for single driver"
  - "Calculate premium for multiple drivers"
  - "Calculate premium with discounts"

### The INVEST Criteria

Each Epic (and Story) should pass the INVEST test:

| Letter | Criterion | What It Means |
|:-------|:----------|:--------------|
| **I** | Independent | Can be developed without depending on other work |
| **N** | Negotiable | Details can be adjusted during development |
| **V** | Valuable | Delivers clear business value |
| **E** | Estimable | Team can estimate the size |
| **S** | Small | Can be completed in a reasonable time |
| **T** | Testable | Clear criteria for "done" |

---

## 6. User Story Elaboration: Creating Work Packages

### What is a User Story?

A **User Story** is a small piece of functionality that delivers value to a user. It's the smallest unit of work that developers implement.

**Traditional Format:**
> As a [type of user], I want [some goal] so that [some reason].

**Example:**
> As a customer, I want to view my order history so that I can track my purchases.

### The "Prompt Package" Concept

In this framework, a User Story is more than just a description—it's a complete "prompt package" that contains everything an AI needs to help implement it.

**Why This Matters:**

AI coding assistants work best when they have complete context. A story that says "Add login" gives the AI almost nothing to work with. A story with:
- Link to the API specification
- Link to the data model
- Link to the wireframe
- Specific acceptance criteria

...gives the AI enough context to generate useful code.

### The Five Sections of an AI-Ready Story

#### Section 1: Context & Links

Links to all related documents:
- Parent Epic
- PRD section
- API contracts
- Data models
- Wireframes

#### Section 2: Gherkin Acceptance Criteria

**What is Gherkin?**

Gherkin is a structured language for writing acceptance criteria. It uses a "Given-When-Then" format that is:
- Understandable by non-technical stakeholders
- Precise enough to be automated
- Used by testing tools (Cucumber, Playwright)

**The Given-When-Then Structure:**

| Keyword | Purpose | Example |
|:--------|:--------|:--------|
| **Given** | The starting condition | "Given I am logged in as an admin" |
| **When** | The action taken | "When I click the 'Delete User' button" |
| **Then** | The expected result | "Then the user should be removed from the system" |

**Complete Example:**

```gherkin
Given I am a logged-in customer
  And I have 3 items in my shopping cart
When I click the "Checkout" button
Then I should see the payment page
  And my cart items should be displayed
  And the total should be calculated correctly
```

**Why Gherkin Matters:**

1. **Unambiguous:** Forces precise language
2. **Testable:** Can be directly converted to automated tests
3. **Shared Understanding:** Business and technical teams use the same language
4. **AI-Ready:** AI can generate test code from Gherkin

#### Section 3: Technical Implementation Plan

A checklist of what needs to be built:
- Files to create or modify
- API endpoints to call
- Database tables to use
- Functions to implement

#### Section 4: AI Collaboration Plan

Specific instructions for how the developer should work with AI:
1. "Ask AI to generate the component structure"
2. "Review and adjust the generated code"
3. "Ask AI to generate unit tests"

#### Section 5: Manual Validation Steps

Things that must be checked by a human:
- Visual appearance
- Animation smoothness
- Accessibility (screen readers, keyboard navigation)
- "Feel" of the user experience

---

## 7. UX Design: The UX Architect Framework

### What is UX Design?

**User Experience (UX) Design** is the process of designing products that are easy to use, efficient, and enjoyable. It encompasses:
- How screens are laid out
- How users navigate between screens
- What users feel when using the product
- How errors are handled

### The Four-Step UX Workflow

This framework uses a structured four-step process:

#### Step 1: Flow Mapping

**What it is:** Documenting the complete user journey

**What it includes:**
- The "Happy Path" — What happens when everything goes right
- 3+ "Sad Paths" — What happens when things go wrong

**Example for "User Registration":**

| Path Type | Description |
|:----------|:------------|
| Happy Path | User enters valid info, clicks submit, account created |
| Sad Path 1 | Email already exists — show error, suggest login |
| Sad Path 2 | Password too weak — show requirements, let user retry |
| Sad Path 3 | Server error — show friendly message, offer retry |

#### Step 2: 3-Screen Solution

**The Principle:** Achieve the goal in the fewest possible screens

**Why This Matters:**
- Each additional screen is a chance for users to abandon the process
- Simpler flows have fewer bugs
- Less development effort

**Example:**

| Task | Traditional Approach | 3-Screen Approach |
|:-----|:---------------------|:------------------|
| Place an order | 7 screens | 3 screens (cart → payment → confirmation) |

#### Step 3: Heuristic Evaluation

**What is a Heuristic?**

A heuristic is a rule of thumb or best practice. In UX, we use Jakob Nielsen's 10 Usability Heuristics as a checklist:

| # | Heuristic | What It Means |
|:--|:----------|:--------------|
| 1 | Visibility of system status | Users should always know what's happening |
| 2 | Match between system and real world | Use language users understand |
| 3 | User control and freedom | Allow undo and cancel |
| 4 | Consistency and standards | Same action = same result everywhere |
| 5 | Error prevention | Prevent errors before they happen |
| 6 | Recognition rather than recall | Show options, don't make users remember |
| 7 | Flexibility and efficiency | Allow shortcuts for experts |
| 8 | Aesthetic and minimalist design | Remove unnecessary elements |
| 9 | Help users recognize, diagnose, and recover from errors | Clear error messages |
| 10 | Help and documentation | Provide guidance when needed |

Each screen is rated 1-5 on each heuristic.

#### Step 4: Persona Stress-Test

**What is a Persona?**

A persona is a fictional representation of a user type. Each persona has:
- A name and background
- Goals and motivations
- Pain points and frustrations
- Technical skill level

**Example Personas:**

| Persona | Description | Stress-Test Focus |
|:--------|:------------|:------------------|
| "Sarah the Rushed Parent" | Busy, distracted, using mobile while cooking | Can she complete the task quickly? |
| "Tom the Technophobe" | Older, intimidated by technology | Are the instructions clear enough? |
| "Alex the Power User" | Tech-savvy, wants efficiency | Are there shortcuts available? |

**The AI Role:**

AI can simulate these personas, asking questions like:
- "As Sarah, I'm confused by this button—what does it do?"
- "As Tom, I don't understand what 'authenticate' means"

---

## 8. System-Wide UX: The Holistic Advantage

### The Problem with Feature-by-Feature UX

When different teams design features independently:
- Navigation patterns differ between features
- Terminology is inconsistent
- Users have different experiences in different parts of the app

### The AI Advantage

AI can analyze the entire system simultaneously:

| Capability | What It Does | Benefit |
|:-----------|:-------------|:--------|
| **Information Architecture** | Ensures consistent navigation | Users always know where to find things |
| **Cross-Epic Flows** | Identifies connections between features | No orphaned or disconnected features |
| **Design System Compliance** | Checks that components are used consistently | Same button looks the same everywhere |

### The Result

Instead of designing UX one feature at a time, the AI considers the entire product and ensures everything works together coherently.

---

## 9. Architecture: The Architecture Hub

### What is Software Architecture?

**Software Architecture** describes the structure of a software system:
- What components exist
- How they communicate
- Where data is stored
- How the system is deployed

### The Architecture Hub Concept

The Architecture Hub is a centralized repository of technical decisions and specifications. It answers three questions:

#### The WHAT: Diagrams

Visual representations of the system structure.

**The C4 Model:**

The C4 Model (created by Simon Brown) provides four levels of diagrams, each at a different zoom level:

| Level | Name | Audience | What It Shows |
|:------|:-----|:---------|:--------------|
| 1 | **Context** | Everyone | How the system fits into the world (users, external systems) |
| 2 | **Container** | Technical | What deployable units exist (web app, database, API) |
| 3 | **Component** | Developers | What components exist within a container |
| 4 | **Code** | Developers | Class diagrams, detailed code structure |

**Example Context Diagram (Level 1):**

```mermaid
C4Context
    Person(customer, "Customer", "Buys products")
    System(ecommerce, "E-Commerce System", "Allows customers to browse and buy")
    System_Ext(payment, "Payment Gateway", "Processes payments")
    
    Rel(customer, ecommerce, "Uses")
    Rel(ecommerce, payment, "Sends payments to")
```

This shows:
- A Customer interacts with
- The E-Commerce System, which communicates with
- An external Payment Gateway

**Other Diagram Types:**

| Purpose | Tool | What It Shows |
|:--------|:-----|:--------------|
| Database structure | DBML | Tables, columns, relationships |
| Infrastructure | Python Diagrams | Cloud resources (servers, databases, networking) |
| Behavior | Sequence Diagrams | Step-by-step message flows |

#### The HOW: Contracts

Machine-readable specifications that describe exactly how components communicate.

**API Contracts (OpenAPI):**

OpenAPI (formerly Swagger) is a standard format for describing REST APIs:
- What endpoints exist
- What data they accept
- What data they return
- What errors can occur

**Data Models (DBML):**

DBML (Database Markup Language) describes database tables:
- What tables exist
- What columns each table has
- How tables are related

**Why Contracts Matter:**

- Developers on different teams can work in parallel
- AI can generate code from contracts
- Tests can validate that code matches contracts
- Documentation is always up-to-date

#### The WHY: Architecture Decision Records (ADRs)

**What is an ADR?**

An ADR documents an important architectural decision:
- What was decided
- Why it was decided
- What alternatives were considered
- What the consequences are

**Example ADR:**

```markdown
# ADR-001: Use PostgreSQL for the primary database

## Status
Accepted

## Context
We need a database for the e-commerce platform.
Options considered: PostgreSQL, MySQL, MongoDB

## Decision
Use PostgreSQL

## Consequences
- Pro: Strong consistency, complex queries, JSON support
- Con: Requires more operational expertise than MongoDB
```

**Why ADRs Matter:**
- Future developers understand why decisions were made
- Prevents re-debating the same decisions
- Documents trade-offs explicitly

---

## 10. Interfaces: The Four Layers of Integration

### What is an Interface?

An **Interface** is any point where our system connects to another system:
- APIs we call (outbound)
- APIs others call (inbound)
- Files we receive
- Files we send
- Events we publish or subscribe to

### Why Interfaces Matter

Most software bugs occur at system boundaries. If interfaces aren't well-documented and tested:
- Systems fail when external systems change
- Data gets corrupted during transfer
- Performance degrades due to unexpected load

### The Four Layers of Interface Management

#### Layer 1: Context (Visualization)

**What:** A visual map showing ALL external connections

**When:** During requirements and architecture

**Output:** C4 Context Diagram showing:
- Our system
- All external systems
- The connections between them

#### Layer 2: Catalog (Inventory)

**What:** A master list of ALL interfaces

**When:** During Epic decomposition

**Output:** Interface Catalog table:

| ID | External System | Type | Direction | Protocol | Frequency |
|:---|:----------------|:-----|:----------|:---------|:----------|
| INT-001 | Payment Gateway | API | Outbound | REST | Real-time |
| INT-002 | Claims Provider | File | Inbound | SFTP | Daily |
| INT-003 | Accounting | Event | Outbound | Pub/Sub | Real-time |

#### Layer 3: Specification (Details)

**What:** Detailed specification for each interface

**When:** During story writing and architecture

**Output:** Interface spec documents including:
- Endpoint URLs or file paths
- Data formats
- Authentication methods
- Error handling
- Example request/response

**Example for an API Interface:**

| Attribute | Value |
|:----------|:------|
| **Base URL** | `https://api.payment.com/v2` |
| **Auth** | OAuth 2.0 |
| **Rate Limit** | 100 req/min |
| **Retry Policy** | 3 attempts with exponential backoff |

**Example for a File Interface:**

| Attribute | Value |
|:----------|:------|
| **Protocol** | SFTP |
| **Directory** | `/outbound/claims/` |
| **Filename Pattern** | `CLAIMS_YYYYMMDD_HHMMSS.csv` |
| **Frequency** | Daily at 2:00 AM |
| **Format** | CSV, pipe-delimited |

#### Layer 4: Testing (Validation)

**What:** Automated tests that verify interfaces work correctly

**When:** During testing phase

**Output:**
- **Contract Tests** — Verify our code matches the interface specification
- **Mock Servers** — Simulate external systems for testing
- **Schema Validation** — Verify file formats are correct

---

## 11. Implementation: Context-Driven Development

### The Shift in Developer Role

| Traditional Development | Context-Driven Development |
|:------------------------|:---------------------------|
| Developer writes all code | Developer reviews AI-generated code |
| Developer memorizes patterns | AI applies patterns from Architecture Hub |
| Developer writes tests after code | AI generates tests before/during coding |

### The "Prompt Package" Approach

Instead of a vague task like "implement login," the developer receives a complete package:

1. **Jira Story** — What to build
2. **Wireframes** — What it should look like
3. **API Contracts** — How to communicate with backend
4. **Data Models** — What data to store/retrieve
5. **Gherkin ACs** — How to verify it works

This package gives the AI enough context to generate accurate, useful code.

### The AI-Assisted Development Workflow

#### Red-Green-Refactor (Test-Driven Development)

This is a proven methodology for writing high-quality code:

| Phase | What Happens | AI Role |
|:------|:-------------|:--------|
| **Red** | Write a failing test | AI generates tests from Gherkin |
| **Green** | Write minimum code to pass | AI suggests implementation |
| **Refactor** | Improve code quality | AI identifies improvements |

**The Flow:**

1. **AI generates test** from Gherkin acceptance criteria
2. Test fails (because the feature doesn't exist yet)
3. **AI generates code** to make the test pass
4. Developer reviews and accepts the code
5. All tests pass
6. **AI suggests refactoring** to improve code quality
7. Developer reviews and accepts changes

### Human-in-the-Loop

**Critical Principle:** AI never commits code directly. Every change is:
1. Proposed by AI
2. Shown as a "diff" (comparison of old vs. new)
3. Reviewed by developer
4. Accepted or rejected by developer
5. Only then saved to file

---

## 12. Testing: The Five Dimensions of Quality

### The Testing Pyramid

Traditional testing anti-patterns put most effort into slow, expensive manual testing. The Testing Pyramid inverts this:

```
        /\
       /  \
      / E2E \          ← Few, focused end-to-end tests
     /--------\
    /Integration\      ← More integration tests
   /--------------\
  /     Unit       \   ← Many fast unit tests
 /------------------\
```

**The Principle:** Invest most effort in fast, cheap tests (unit tests). Reserve expensive tests (E2E) for critical paths only.

### Testing is Continuous

In the AI-Augmented SDLC, testing happens throughout development, not just at the end:

| When | What Testing Happens |
|:-----|:---------------------|
| During Requirements | Persona simulation (edge cases) |
| During Story Writing | Gherkin ACs (behavior specs) |
| During Architecture | Contract tests (API specs) |
| During Implementation | Unit tests (TDD) |
| Before Release | Load tests, chaos tests |

### The Five Dimensions of Quality

#### Dimension 1: Simulation (Persona Testing)

**What it is:** AI simulates user personas to find edge cases

**When:** During requirements

**Example:** 
- AI acts as "Sarah the Rushed Parent"
- Tries to complete tasks quickly
- Reports confusion points and friction

#### Dimension 2: Components (Unit Testing)

**What it is:** Testing individual functions in isolation

**When:** During implementation

**Tools:** pytest (Python), Vitest (JavaScript)

**AI Role:** Generates unit tests from code and specifications

#### Dimension 3: Contracts (Integration Testing)

**What it is:** Testing that components communicate correctly

**When:** During architecture/implementation

**Tools:** OpenAPI validators, Pact (contract testing)

**AI Role:** Generates contract tests from API specifications

#### Dimension 4: Behavior (End-to-End Testing)

**What it is:** Testing complete user journeys in a real browser

**When:** During story development

**Tools:** Playwright (browser automation)

**AI Role:** Generates Playwright tests from Gherkin acceptance criteria

**Example:**

Gherkin:
```gherkin
Given I am logged in as a customer
When I add an item to my cart
Then the cart count should increase by 1
```

AI-generated Playwright:
```javascript
test('add to cart increases count', async ({ page }) => {
  await loginAsCustomer(page);
  await page.getByRole('button', { name: 'Add to Cart' }).click();
  await expect(page.getByTestId('cart-count')).toHaveText('1');
});
```

#### Dimension 5: Resilience (Performance & Chaos Testing)

**What it is:** Testing how the system behaves under stress

**When:** Before release

**Types:**

| Test Type | What It Does |
|:----------|:-------------|
| **Load Testing** | Simulates many users at once |
| **Stress Testing** | Finds the breaking point |
| **Spike Testing** | Simulates sudden traffic surges |
| **Chaos Testing** | Randomly breaks things to test recovery |

**Tools:** k6, Locust (load testing), Chaos Mesh (chaos engineering)

**AI Role:** Generates load test scripts from API specs

### Test Data Management

**The Challenge:** Tests need data to run against, but sharing data between tests causes problems.

**The Solution:**

| Strategy | What It Means |
|:---------|:--------------|
| **Ephemeral Environments** | Each test run gets a fresh, isolated database |
| **Seed Data** | Predefined test data is loaded automatically |
| **Dynamic Data** | Tests create their own data and clean up after |

**Golden Rule:** Tests never share mutable state.

### When to Test Manually

Not everything should be automated:

| Test Type | Why Manual | How Often |
|:----------|:-----------|:----------|
| **UX Feel** | Animations, transitions, "polish" | Every sprint |
| **Exploratory** | Finding unexpected bugs | 2-3 hours per sprint |
| **Accessibility** | Screen reader, keyboard navigation | Before release |
| **Usability Studies** | Watching real users | Per major feature |

**Philosophy:** Automate the repetitive. Humanize the creative.

---

## Conclusion

The AI-Augmented SDLC is not about replacing developers with AI. It's about:

1. **Eliminating repetitive work** — AI handles boilerplate, documentation
2. **Improving consistency** — Same patterns, same templates everywhere
3. **Accelerating feedback** — Errors caught earlier, delivered faster
4. **Enhancing quality** — More testing, better documentation
5. **Preserving human judgment** — Every AI output is reviewed

The framework works because it combines:
- **Structure** (clear phases, defined outputs)
- **Automation** (AI agents for repetitive tasks)
- **Governance** (human review, version control)
- **Integration** (everything connected: docs, code, tests, tickets)

This is the future of software development: humans and AI working together, each doing what they do best.

---

## Glossary

| Term | Definition |
|:-----|:-----------|
| **ADR** | Architecture Decision Record — Documented architectural decision |
| **BDD** | Behavior-Driven Development — Writing tests as specifications |
| **C4 Model** | Four-level architecture visualization (Context, Container, Component, Code) |
| **DBML** | Database Markup Language — Text format for database schemas |
| **Epic** | Large body of work that can be broken into smaller stories |
| **Gherkin** | Structured language for acceptance criteria (Given/When/Then) |
| **Git** | Version control system for tracking file changes |
| **HITL** | Human-in-the-Loop — Requiring human approval for AI actions |
| **INVEST** | Criteria for good stories (Independent, Negotiable, Valuable, Estimable, Small, Testable) |
| **Mermaid** | Text-to-diagram tool |
| **OpenAPI** | Standard format for API documentation |
| **PRD** | Program Requirements Document |
| **SPIDR** | Epic splitting framework (Spike, Path, Interface, Data, Rules) |
| **SDLC** | Software Development Lifecycle |
| **Story** | Small unit of work delivering user value |
| **UX** | User Experience — The overall experience of using a product |
| **Wireframe** | Low-fidelity visual representation of a screen layout |
| **Context Window** | The maximum amount of text an AI model can process at once |
| **RAG** | Retrieval Augmented Generation — Fetching relevant information before AI generation |
| **Token** | The basic unit of text that AI models process (roughly 4 characters) |

---

## 13. Context Window Management: Getting the Best from AI

### What is a Context Window?

When you communicate with an AI assistant like Gemini, the AI can only "see" a limited amount of text at once. This limit is called the **context window**.

**Analogy:** Think of it like the AI's short-term memory. Just like you can only keep so many things in mind at once, an AI can only consider so much text in a single interaction.

### Current Context Window Sizes (2025)

| Model | Context Window | Equivalent |
|:------|:---------------|:-----------|
| **Gemini 2.0 Pro** | 2 million tokens | ~100,000 lines of code |
| **Gemini 2.0 Flash** | 1 million tokens | ~50,000 lines of code |
| **Gemini Flash (Code Assist chat)** | 32,000 tokens | ~1,600 lines of code |
| **Gemini Flash (auto-complete)** | 8,000 tokens | ~400 lines of code |

**What is a Token?**

A token is approximately 4 characters of English text. The word "context" is 2 tokens. A typical line of code is 15-20 tokens.

### Why Context Management Matters

**The Problem:**

Even with 1 million tokens, you can't fit everything into a single prompt:
- A medium-sized codebase: 500,000+ tokens
- All documentation: 100,000+ tokens
- Full architecture specs: 50,000+ tokens

**The Larger the Context:**
- ✅ More accurate AI responses (more information available)
- ❌ Slower responses (more text to process)
- ❌ Higher costs (charged per token)
- ❌ Risk of "lost in the middle" (AI may miss information in the middle of long contexts)

### The Multi-Layer Context Strategy

This framework uses a four-layer approach to manage context effectively:

#### Layer 1: Pre-Processing (NotebookLM)

**What it does:** Converts large documents into digestible summaries before they enter the development workflow.

**Best for:**
- Regulatory documents
- Existing system documentation
- Meeting transcripts
- Legacy code analysis

**Process:**
```
Large Document (10,000+ tokens)
        ↓
    NotebookLM
        ↓
Summary Document (500-1,000 tokens)
        ↓
Saved to docs/context/
```

**Example:**
- Input: 50-page regulatory compliance document
- Output: 2-page summary with key requirements, stored as `docs/context/compliance-summary.md`

#### Layer 2: Hierarchical Chunking

**What it does:** Breaks large documents into a hierarchy of summaries and details.

**The Structure:**

| Level | Size | Purpose | Example |
|:------|:-----|:--------|:--------|
| **Index** | 200-500 tokens | Navigation and overview | Table of contents with 1-line summaries |
| **Summary** | 500-2,000 tokens | Quick reference | Key points from a section |
| **Detail** | 2,000-10,000 tokens | Deep dive | Full section content |

**Example for Architecture Documentation:**

```
docs/architecture/
├── index.md              # 300 tokens: "Auth is in auth-flow.md, Data model in data-model.md..."
├── summaries/
│   ├── auth-summary.md   # 1,000 tokens: Key auth concepts
│   └── data-summary.md   # 800 tokens: Key data concepts
└── details/
    ├── auth-flow.md      # 5,000 tokens: Complete auth specification
    └── data-model.md     # 8,000 tokens: Full DBML schema
```

**How it's used:**
1. AI always receives the **index** (small)
2. AI receives **summaries** for relevant sections
3. AI fetches **details** only when needed for specific tasks

#### Layer 3: Context Drawer (Code Assist Feature)

**What it is:** A feature in Gemini Code Assist that lets you explicitly control which files the AI can see.

**Available since:** April 2025

**How to use it:**

| Action | Result |
|:-------|:-------|
| **Add files** | Drag specific files into the context drawer |
| **Add folders** | Include entire directories (e.g., `docs/api/`) |
| **Exclude paths** | Remove irrelevant directories (e.g., `node_modules/`, `dist/`) |
| **View context** | See exactly what information the AI has access to |

**Best Practice:** Create context profiles for different types of work:

```
.gemini/context-profiles/
├── architecture-work.txt    # Files needed for architecture tasks
├── frontend-work.txt        # Files for UI development
├── api-work.txt             # Files for API development
└── testing-work.txt         # Files for test writing
```

#### Layer 4: Context Caching

**What it is:** A way to reuse common context across multiple AI requests without resending it each time.

**Types of Caching:**

| Type | How It Works | Best For |
|:-----|:-------------|:---------|
| **Implicit** | Automatic, no action needed | Repeated queries in same session |
| **Explicit** | You declare what to cache | Large system instructions, standard docs |

**Benefits:**
- Faster responses (cached content doesn't need reprocessing)
- Lower costs (cached tokens are cheaper)
- Consistent context across many queries

**What to Cache:**

| Document Type | Why Cache It |
|:--------------|:-------------|
| **STYLEGUIDE.md** | Referenced in every AI interaction |
| **Architecture Summary** | Provides critical context for all code |
| **Glossary** | Ensures consistent terminology |
| **API Index** | Needed for most implementation work |

### Practical Strategies

#### Strategy 1: Progressive Disclosure

**Principle:** Start with summaries, provide details only when needed.

**Example Workflow:**

```
Step 1: AI receives architecture-summary.md (500 tokens)
Step 2: User asks about authentication
Step 3: AI receives auth-flow.md (5,000 tokens) — on demand
Step 4: AI generates authentication code with full context
```

**Why it works:**
- Most queries don't need full context
- Details are loaded only when relevant
- Reduces cost and latency

#### Strategy 2: Reference Linking

**Instead of embedding full content:**

```markdown
# Story: User Login
<full OpenAPI spec - 2,000 tokens>
<full data model - 1,500 tokens>
<full wireframe description - 800 tokens>
```

**Use references:**

```markdown
# Story: User Login
- API Contract: [auth-api.yaml](file://docs/api/auth-api.yaml) — see POST /api/auth/login (lines 45-78)
- Data Model: [users.dbml](file://docs/data/users.dbml) — see User table
- Wireframe: [login-screen.md](file://docs/ux/wireframes/login-screen.md)
```

**Why it works:**
- Story stays small (200 tokens instead of 4,300)
- AI can fetch details when needed
- Documents stay up-to-date (no copy/paste drift)

#### Strategy 3: Semantic Chunking with Metadata

**Add metadata to each chunk for better retrieval:**

```markdown
---
id: ARCH-001-auth
title: Authentication Flow
summary: OAuth2 with Keycloak integration, JWT tokens, refresh handling
keywords: [auth, oauth, keycloak, jwt, token, login, logout]
parent: architecture-summary.md
related: [user-data-model.md, api-auth-endpoints.md]
tokens: ~5000
---

# Authentication Flow
[Full content here]
```

**Why it works:**
- AI can find relevant chunks by keywords
- Parent/related links enable navigation
- Token count helps with budget planning

#### Strategy 4: Task-Specific Context Assembly

**Match context to the task:**

| Task Type | Context Included |
|:----------|:-----------------|
| **Story Implementation** | Story doc, relevant API endpoints, relevant UI components, test patterns |
| **Architecture Review** | Architecture summary, relevant C4 diagrams, ADRs |
| **Bug Investigation** | Error logs, related code files, test results |
| **Test Writing** | Story Gherkin, API specs, existing test patterns |

**Example Context Assembly:**

```
Task: Implement "Add to Cart" story

Context Package:
├── STYLEGUIDE.md           (always included)
├── glossary.md             (always included)
├── stories/add-to-cart.md  (the task)
├── api/cart-endpoints.yaml (relevant API)
├── components/CartItem.tsx (relevant component)
└── tests/cart.spec.ts      (existing test patterns)

Total: ~8,000 tokens (fits in auto-complete context)
```

### Recommended Document Structure

Organize your documentation to support efficient context management:

```
docs/
├── context/                          # Pre-computed summaries (Layer 1)
│   ├── architecture-summary.md       # 500-1,000 tokens
│   ├── api-index.md                  # Links + 1-line descriptions
│   ├── data-model-summary.md         # Key entities, relationships
│   └── glossary.md                   # Domain terms
│
├── architecture/                     # Hierarchical chunks (Layer 2)
│   ├── index.md                      # Table of contents
│   ├── summaries/                    # Section summaries
│   │   ├── auth-summary.md
│   │   └── data-summary.md
│   └── details/                      # Full specifications
│       ├── auth-flow.md
│       └── data-model.md
│
├── api/                              # Chunked by resource
│   ├── index.md                      # All endpoints listed
│   └── endpoints/
│       ├── auth.yaml
│       ├── cart.yaml
│       └── orders.yaml
│
└── .gemini/
    └── context-profiles/             # Context Drawer profiles (Layer 3)
        ├── frontend-work.txt
        └── api-work.txt
```

### Key Principles

| Principle | What It Means |
|:----------|:--------------|
| **Pre-summarize** | Use NotebookLM to condense bulk documents |
| **Index everything** | Create index files that link to details |
| **Chunk semantically** | Break by meaning, not arbitrary size |
| **Add metadata** | Include summaries, keywords, relationships |
| **Use the Context Drawer** | Explicitly control what AI sees |
| **Cache common context** | Reduce latency and cost for frequent docs |
| **Progressive disclosure** | Load details only when needed |
| **Reference, don't embed** | Link to documents instead of copying content |

### Session State Management

Beyond managing what goes into a single AI prompt, this framework also addresses **multi-session context**—remembering what happened across multiple conversations over days or weeks.

**The Challenge:**

Real SDLC work spans multiple sessions:
- A PRD might be written over 3-4 sessions across 2 weeks
- An epic decomposition might involve multiple discussions
- Story refinement happens iteratively

Without session management, each AI conversation starts fresh with no memory of previous work.

**The Solution: Persistent Memory Per Artifact**

This framework includes a `SessionStateManager` (see `standards/session_state_manager.py`) that tracks:

| What's Tracked | Example |
|:---------------|:--------|
| **Session Log** | "Nov 3: Completed Scope Boundaries section with PRD Agent" |
| **Entity Registry** | Domain entities discovered (Users, Orders, Products) |
| **Document Versions** | Git commits for each artifact revision |
| **Next Steps** | "Continue with System Impact section" |
| **Pending Reviews** | "Awaiting stakeholder approval on Business Intent" |

**How It Works:**

```
Session 1 (Day 1):
  - User works on PRD sections 1-3
  - Agent logs: sections completed, entities found, open questions
  - Saved to session_log.md

Session 2 (Day 3):
  - User returns: "Let's continue the PRD"
  - Agent reads session_log.md
  - Agent: "Welcome back! Last time you completed sections 1-3.
           You were starting section 4. Ready to continue?"
```

**Session Log Structure:**

```markdown
## Session 2024-11-03 14:30
**Agent:** PRD Collaborator
**Tools Run:** Business Intent Analysis, Scope Boundaries
**Key Outcomes:**
- Completed section 3 (Scope Boundaries)
- Identified 3 new entities: User, Portfolio, ETF
- Open question: Integration with market data provider
**Open Questions Added:** 1

---
```

**Entity Registry:**

Entities discovered during requirements are tracked and can be injected into future prompts:

| Entity | Discovered In | CRUD | States | Notes |
|:-------|:--------------|:-----|:-------|:------|
| User | PRD Section 1 | CRUD | Active, Suspended | Core entity |
| Portfolio | PRD Section 2 | CRU | Draft, Published | Links to User |
| ETF | Epic EPA-001 | R | N/A | External data source |

> 📖 **Further Reading:** See `ai-agent-recommendation-and-workflow.md` Section 8 for detailed design of agent memory and context management.

### Measuring Context Effectiveness

**Signs your context strategy is working:**

| Indicator | Good | Needs Improvement |
|:----------|:-----|:------------------|
| **AI accuracy** | Responses align with your architecture | AI suggests patterns that don't match your system |
| **Response time** | Fast first-token time | Long delays before AI starts responding |
| **Token usage** | Consistent, predictable | Varies wildly between similar tasks |
| **Relevance** | AI uses provided context | AI hallucinates or asks for information you provided |

---

## 14. Cross-System Coordination: Working Across Teams and Systems

### The Reality of Modern Development

Most real-world requirements don't involve building isolated new systems. They involve:

| Scenario | What It Means |
|:---------|:--------------|
| **Extending legacy systems** | Adding features to existing, often older, systems |
| **Consuming other teams' APIs** | Your feature depends on another team's service |
| **Providing APIs to others** | Other teams or apps depend on your system |
| **Integrating with vendors** | Connecting to external services (payment, identity, etc.) |
| **Sharing data upstream/downstream** | Receiving data from or sending data to other systems |

This chapter provides a framework for handling these cross-system dependencies.

### The 4 Dimensions of External Dependencies

| Dimension | Question | Output |
|:----------|:---------|:-------|
| **1. Discovery** | What systems are we connected to? | Dependency Map |
| **2. Relationship** | How do we work with that team? | Team Contract |
| **3. Integration** | How do we technically connect? | Interface Contract |
| **4. Protection** | How do we isolate changes? | Anti-Corruption Layer |

---

### Dimension 1: Dependency Discovery

**Why it matters:** You can't coordinate what you don't know exists.

**The Dependency Map:**

Every project should create a visual map of all connected systems:

```mermaid
C4Context
    System(us, "Our System", "What we're building")
    
    System_Ext(upstream1, "CRM System", "Customer data source")
    System_Ext(upstream2, "Legacy Admin", "Existing data")
    
    System_Ext(peer1, "Payment Gateway", "External vendor")
    System_Ext(peer2, "Rating Engine", "Sister team")
    
    System_Ext(downstream1, "Reports", "Consumes our data")
    
    Rel(upstream1, us, "Provides data")
    Rel(upstream2, us, "Provides data")
    BiRel(us, peer1, "Payments")
    BiRel(us, peer2, "Quotes")
    Rel(us, downstream1, "Exports events")
```

**Dependency Catalog:**

| ID | System | Direction | Team | What We Need |
|:---|:-------|:----------|:-----|:-------------|
| DEP-001 | CRM | Upstream | CRM Team | Customer data |
| DEP-002 | Legacy Admin | Upstream | Core Team | Policy data |
| DEP-003 | Payment Gateway | Peer | External | Payment processing |
| DEP-004 | Reports | Downstream | BI Team | We send them events |

---

### Dimension 2: Team Relationships (Team Topologies)

Different dependencies require different collaboration styles.

**The Three Interaction Modes:**

| Mode | Description | When to Use |
|:-----|:------------|:------------|
| **Collaboration** | Close partnership, frequent communication | New integration, exploring unknowns |
| **X-as-a-Service** | Provider/Consumer relationship | Stable service with clear API |
| **Facilitating** | One team helps another | Adopting platform, learning new tools |

**Choosing the Right Mode:**

| Scenario | Mode | Why |
|:---------|:-----|:----|
| Building new API with another team | Collaboration | Need joint design decisions |
| Consuming an existing, documented API | X-as-a-Service | Just follow the contract |
| Adopting a new internal platform | Facilitating | Need guidance to use it right |
| Integrating with external vendor | X-as-a-Service | Can't change their system |

---

### The Team Contract

For each significant dependency, document the relationship:

```markdown
# Team Contract: DEP-002 Legacy Admin System

## Parties
| Role | Team | Contact |
|:-----|:-----|:--------|
| We Are | Portfolio Team | @dave |
| They Are | Core Platform Team | @jane |

## Relationship Type
- [x] Collaboration — Working closely together
- [ ] X-as-a-Service — Using their stable service
- [ ] Facilitating — They're helping us learn

## What We Need
1. New API endpoint: GET /api/policies/{id}
2. Event: POLICY_UPDATED emitted on changes
3. API: POST /api/policies/{id}/amend

## Their Commitments
| Commitment | Due Date | Status |
|:-----------|:---------|:-------|
| API design review | Feb 15 | ✅ Done |
| Staging ready | Mar 1 | 🔄 In Progress |
| Production | Mar 15 | ⏳ Pending |

## Our Commitments
| Commitment | Due Date | Status |
|:-----------|:---------|:-------|
| Share requirements | Feb 10 | ✅ Done |
| Integration testing | Mar 5 | ⏳ Pending |

## Communication
- Weekly sync: Thursdays 2pm
- Slack: #portfolio-core-integration
```

---

### Work Delegation in Jira

> ⚠️ **Important Distinction:**
> 
> **Chapter 11 (Interfaces)** covers **connecting to existing systems** — APIs and services that already exist. No work is required from the other team; you simply consume what they have.
> 
> **This section (Work Delegation)** covers a different scenario: **your requirements create work for another team**. They must **build something new** — a new API, a new event, a schema change, or significant modifications to their system. This is passing requirements (essentially Epics) to them.

When your feature requires another team to build something, this is **work delegation** — not just consuming their API. You're passing requirements to them.

**Two Types of Dependencies:**

| Type | What It Is | Work for Them | Jira Approach |
|:-----|:-----------|:--------------|:--------------|
| **Consume Only** | Use their existing API | None | Link type: "uses" |
| **Work Delegation** | They must build something new | Yes | External Dependency Issue |

---

> 💡 **Industry Reference:** SAFe (Scaled Agile Framework) formalizes this as "External Dependencies" managed via PI Planning and Program Boards. The pattern below works with or without SAFe.

---

#### Epic vs Story-Level Delegation

Work delegation can happen at different levels:

| Level | When to Use | Example | Jira Link |
|:------|:------------|:--------|:----------|
| **Epic** | Large body of work (multiple stories) | "Build new Policy API with 5 endpoints" | Epic → Epic |
| **Story** | Small, specific request | "Add `adjuster_name` field to claims export" | Story → Story |

**Choosing the Right Level:**

| Scenario | Delegate As |
|:---------|:------------|
| Needs multiple sprints on their side | **Epic** |
| Single sprint or less | **Story** |
| Requires their own breakdown into stories | **Epic** |
| Specific, well-defined change | **Story** |
| New capability or service | **Epic** |
| Modification to existing API/schema | **Story** |

**Best Practice:** Link at the same level — Epic→Epic or Story→Story — to keep tracking clean.

---

#### External Dependency Pattern (Epic or Story)

When delegating work to another team:

**Step 1: Create Epic in YOUR Project**

```
Project: PORTFOLIO
Type: Epic
Summary: [EXT-DEP] Policy API from Core Platform
Description: 
  We need the Core Platform team to expose:
  1. GET /api/policies/{id}
  2. POST /api/policies/{id}/amend
  3. POLICY_UPDATED event on Pub/Sub
  
  Acceptance Criteria:
  - [ ] API returns policy in agreed schema
  - [ ] 99.9% availability SLA
  - [ ] P95 latency < 200ms
  
  Requested By: @dave (Portfolio Team)
  Requested From: @jane (Core Platform Team)
  Needed By: March 15, 2026
```

**Step 2: Create Linked Epic in THEIR Project (or they create it)**

```
Project: CORE-PLATFORM  
Type: Epic
Summary: Policy API for Portfolio Integration
Labels: external-request
```

**Step 3: Link the Epics**

| Link Type | From | To | Meaning |
|:----------|:-----|:---|:--------|
| **Is blocked by** | Your Epic | Their Epic | Your work can't complete until theirs does |
| **Is depended on by** | Their Epic | Your Epic | Same relationship, other direction |

---

#### Jira Link Types for Work Delegation

| Link Type | When to Use | Example |
|:----------|:------------|:--------|
| **Is blocked by** | You cannot proceed until they deliver | "Portfolio ETF → is blocked by → Core Policy API" |
| **Depends on** | Planned sequential work | "Story 5 → depends on → Story 3" |
| **Relates to** | General relationship, no hard block | "Portfolio Epic → relates to → Core roadmap item" |

---

#### Cross-Project Visibility

**For Company-managed Jira Projects:**

1. **Advanced Roadmaps (Jira Plans):**
   - Add both projects to the same Plan
   - Dependencies show as lines on timeline
   - Red lines = risky (blocking issue scheduled after blocked)

2. **JQL Queries:**
   ```
   project = PORTFOLIO AND issuelinks = "is blocked by" AND status != Done
   ```

3. **Cross-Project Epic Board:**
   - Create a filter for all epics with label `external-dependency`
   - Shared board shows all cross-team work

---

#### Work Delegation Jira Fields

Add custom fields to track delegated work:

| Field | Type | Purpose |
|:------|:-----|:--------|
| **Requested From Team** | Select | Which team owns the dependency |
| **Requested By** | User picker | Who made the request |
| **Needed By Date** | Date | When we need their delivery |
| **External Status** | Select | Pending, Accepted, In Progress, Delivered |
| **Contract Link** | URL | Link to Team Contract document |

---

#### Workflow for External Dependencies

```mermaid
stateDiagram-v2
    [*] --> Identified: Discover dependency
    Identified --> Requested: Create Epic + Contact team
    Requested --> Accepted: They commit to deliver
    Accepted --> InProgress: They start work
    InProgress --> Delivered: They complete
    Delivered --> Verified: We test integration
    Verified --> [*]: Close dependency
    
    Requested --> Rejected: They can't deliver
    Rejected --> Escalated: Raise to leadership
```

---

#### Best Practices

| Do | Don't |
|:---|:------|
| Create Epic in YOUR project first | Copy their stories into your project |
| Link at Epic level (not Story) | Create sprawling story-to-story links |
| Set clear acceptance criteria | Assume they understand your needs |
| Track with "Needed By" date | Rely only on their sprint planning |
| Review dependencies weekly | Wait until your sprint to check |

---

#### AI Assistance for Work Delegation

AI can accelerate several aspects of cross-team coordination:

| Task | AI Action | How |
|:-----|:----------|:----|
| **Discover Dependencies** | Scan PRD/Epic for external system references | `/dep-discover` prompt analyzes requirements |
| **Draft External Dependency Issue** | Generate Jira issue content with acceptance criteria | AI drafts based on your requirements |
| **Generate Team Contract** | Create filled Team Contract template | AI extracts parties, commitments, dates |
| **Write Acceptance Criteria** | Define clear, testable AC for their deliverable | AI expands "need API" into specific criteria |
| **Assess Impact** | Analyze what changes other systems need | AI reviews architecture + requirements |
| **Draft Communication** | Write request email/Slack to other team | AI summarizes need professionally |

**Example AI Prompt:**

```
Analyze this Epic and identify any external dependencies:
- What systems outside our team need to change?
- What work must other teams do?
- Draft an External Dependency Issue for each.

Epic: [paste Epic description]
```

**AI Output:**
- List of identified dependencies
- Draft Jira issue content for each
- Suggested acceptance criteria
- Recommended "Needed By" dates based on our timeline

---

### Dimension 3: Interface Contracts

The technical agreement for how systems connect.

**Consumer-Driven Contracts:**

When you provide an API that others consume, use Consumer-Driven Contract Testing (Pact):

| Step | Who | What |
|:-----|:----|:-----|
| 1 | Consumer team | Writes tests defining what they need |
| 2 | Consumer team | Publishes contract to Pact Broker |
| 3 | Provider team (you) | CI fetches consumer contracts |
| 4 | Provider team (you) | CI verifies you meet all contracts |
| 5 | Both | Breaking change? CI fails before deploy |

**Why this matters:**

- Consumer defines what they actually need (not what you think they need)
- Breaking changes are caught automatically
- No more "works on my machine" integration failures

---

### Dimension 4: Protection Patterns

How to isolate your system from external changes.

**Anti-Corruption Layer (ACL):**

External systems often have different data models, naming conventions, or design philosophies. An ACL translates between their world and yours.

```
External System:              Your System:
{                             {
  "cust_no": "12345",    →      "customerId": "12345",
  "pol_eff_dt": "2025-01",      "effectiveDate": "2025-01",
  "prem_amt": 150000            "premium": { "amount": 1500.00,
}                                            "currency": "USD" }
                              }
```

**Implementation:**

```
adapters/
├── crm_adapter.py              # Translates CRM data
├── legacy_adapter.py           # Translates legacy data
└── payment_adapter.py          # Translates payment data
```

**Strangler Fig Pattern:**

For extending legacy systems without rewriting them:

```
1. Put routing layer (API Gateway) in front of legacy
2. Build new features as new service, not inside legacy
3. Route new feature traffic to new service
4. Gradually migrate old features one by one
5. Eventually decommission legacy
```

**Key Benefit:** Legacy stays running while you incrementally replace it.

---

### Dependency Impact Assessment

For each Epic, assess cross-system impact:

| Dependency | Impact | Their Effort | Risk | Mitigation |
|:-----------|:-------|:-------------|:-----|:-----------|
| DEP-002 Legacy Admin | HIGH | ~2 sprints | Their backlog is full | Escalate to leadership |
| DEP-003 Payment Gateway | LOW | None | Existing API works | None needed |
| DEP-004 Reports | MEDIUM | ~3 days | Schema compatibility | Share schema early |

**Questions to Answer:**

- What do we need from them?
- What effort does it require on their side?
- What's the risk they can't deliver?
- How do we mitigate that risk?

---

### Key Takeaways

| Principle | What It Means |
|:----------|:--------------|
| **Map all dependencies** | Know every system you connect to |
| **Choose interaction mode** | Collaboration vs X-as-a-Service vs Facilitating |
| **Document team contracts** | Explicit commitments with dates |
| **Use consumer contracts** | Let consumers define what they need |
| **Protect your domain** | Anti-Corruption Layer between you and others |
| **Assess impact per Epic** | Cross-system changes need special planning |

---

## 15. AI Planning Intelligence: Continuous Dependency Management

### The Problem: Invisible Dependencies

In most organizations:

| Issue | Impact |
|:------|:-------|
| Stories created without predecessor/successor links | Work blocked unexpectedly mid-sprint |
| Dependencies discovered too late | Rework, delays, cross-team friction |
| Manual dependency tracking | Labor-intensive, error-prone, incomplete |
| No visibility into optimal build order | Suboptimal sprint sequencing |
| Cross-team dependencies hidden | Integration failures, missed deadlines |

### The Solution: AI-Powered Continuous Monitoring

AI Planning Intelligence is an **always-on layer** that watches the Jira backlog and:

| Capability | What It Does |
|:-----------|:-------------|
| **Watches** | Monitors backlog as items are created/edited |
| **Discovers** | Infers dependencies from story/epic content |
| **Suggests** | Proposes missing links for human approval |
| **Sequences** | Recommends optimal build order |
| **Alerts** | Notifies when dependency health changes |
| **Predicts** | Forecasts blockers before they occur |

> ⚠️ **Key Principle:** This is Jira-centric. Users do sprint planning, backlog grooming, and dependency management in **Jira**, not VS Code.

---

### The 4 Dimensions of AI Planning Intelligence

| Dimension | Question | AI Capability |
|:----------|:---------|:--------------|
| **1. Discovery** | What dependencies exist? | NLP analysis of story content |
| **2. Monitoring** | What's the health right now? | Real-time status tracking |
| **3. Sequencing** | What order should we build? | Topological sort, critical path |
| **4. Prediction** | What will block us? | Forecasting from patterns |

---

### Dimension 1: Dependency Discovery

AI analyzes story/epic content to infer dependencies that humans haven't specified.

| Input | AI Analysis | Output |
|:------|:------------|:-------|
| Story text | NLP scans for references to other features, APIs, systems | Suggested "Depends on" links |
| Epic breakdown | Looks for logical sequence (can't do X before Y) | Suggested predecessor/successor |
| Architecture docs | Cross-references with interfaces, components | Technical dependency warnings |
| Historical data | Patterns from past sprints (these types always depend) | Learned dependency rules |

**Example:**
```
Story: "Update dashboard to show new policy status"

AI detects: References "policy status" 
AI scans: Jira backlog
AI finds: CORE-456 "API: Add status field to policy endpoint"
AI suggests: "This story depends on CORE-456"
```

---

### Dimension 2: Continuous Monitoring

Always-on surveillance of dependency health in Jira.

| Monitor | What It Watches | Alert Type |
|:--------|:----------------|:-----------|
| **New Item Monitor** | Every new story/epic created | "Potential dependencies detected" |
| **Edit Monitor** | Changes to existing items | "Dependency implications changed" |
| **Status Monitor** | Blocked items, stale dependencies | "Blocker risk: DEP-123 not started" |
| **Cross-Team Monitor** | External dependencies progress | "External dep at risk: no movement" |
| **Sprint Health** | Dependencies within sprint boundary | "Sprint dependency conflict detected" |

**Dependency Health Status:**

| Status | Meaning | Visual |
|:-------|:--------|:-------|
| 🟢 **Healthy** | Dependency completes before dependent work starts | Safe |
| 🟡 **Risk** | Dependency scheduled in same sprint (tight timing) | Watch |
| 🔴 **Conflict** | Dependent story scheduled before its dependency | Fix now |

---

### Dimension 3: Optimal Sequencing

AI recommends the best order to build stories based on dependency graph.

| Capability | How It Works |
|:-----------|:-------------|
| **Topological Sort** | Orders work so dependencies complete first |
| **Critical Path** | Identifies longest dependency chain (schedule risk) |
| **Parallel Opportunities** | Groups work that can be done simultaneously |
| **Sprint Fit** | Suggests which stories fit cleanly in sprint boundary |
| **Risk Balancing** | Prioritizes high-risk dependencies early |

**Example Output:**
```
Recommended Build Order for Sprint 14:

Phase 1 (Days 1-3) — Foundations (No dependencies):
  ✓ CORE-456: API: Add status field
  ✓ CORE-457: Database migration

Phase 2 (Days 4-7) — Dependent Work:
  ← PORTAL-123: Dashboard update (depends on CORE-456)
  ← PORTAL-124: Status filter (depends on CORE-456)

Phase 3 (Days 8-10) — Integration:
  ← PORTAL-125: E2E tests (depends on all above)
```

---

### Dimension 4: Predictive Intelligence

AI forecasts problems before they impact delivery.

| Prediction | Data Sources | Lead Time |
|:-----------|:-------------|:----------|
| **Blocker Forecast** | Team velocity, story complexity, history | 1-2 sprints ahead |
| **Capacity Conflict** | Team allocation, concurrent dependencies | PI planning |
| **Integration Risk** | Multi-team dependencies, external factors | 2-4 weeks |
| **Scope Creep Alert** | New items added, dependency chain growth | Real-time |

---

### Jira Integration Points

AI Planning Intelligence integrates with Jira through several patterns:

| Integration | Mechanism | Purpose |
|:------------|:----------|:--------|
| **Jira API** | Read backlog, create suggested links | Access and update Jira data |
| **Jira Automation** | Trigger notifications, status updates | Automated alerts |
| **Advanced Roadmaps** | Feed dependency data for visualization | Timeline views |
| **Slack/Teams** | Send alerts to team channels | Notifications |

---

### Implementation Patterns

**Agents still run in VS Code** — that's where you execute prompts. "Continuous monitoring" means **scheduled or event-driven**, not constant polling.

| Pattern | How It Works | Overhead | Best For |
|:--------|:-------------|:---------|:---------|
| **On-Demand** | User runs `/dep-health` manually | Low | Getting started |
| **Scheduled** | Cron/Cloud Scheduler runs nightly/weekly | Low | Regular health reports |
| **CI/CD Hook** | Analyze on PRs that touch epics/stories | Medium | Integrated workflow |
| **Webhook** | Jira pushes events to Cloud Function | Medium | Real-time (advanced) |

**Recommended Approach:**

```
Phase 1: On-Demand (VS Code)
├── User runs /dep-discover, /dep-health, /sprint-readiness
├── Agent calls Jira API → pulls sprint/backlog once
├── Analyzes locally → outputs report
└── No ongoing overhead

Phase 2: Scheduled Reports
├── Weekly cron job runs /dep-health for all sprints
├── Posts summary to Slack or email
└── Low overhead, high value

Phase 3: Event-Driven (Optional)
├── Jira Webhook → Cloud Function
├── On issue.created → suggest dependencies
└── Higher complexity, real-time value
```

**Caching Strategy:**

To reduce API overhead:
- Pull sprint/backlog **once per session**
- Cache locally for analysis
- Refresh only when user requests

---

### Health Check Reports

#### Sprint Readiness Report

Run before sprint planning to assess dependency health:

```
SPRINT 15 READINESS REPORT
Generated: 2026-02-01

Stories Planned: 12
─────────────────────────────────────────

DEPENDENCY HEALTH
  🟢 Healthy:     8 stories (no blocking issues)
  🟡 At Risk:     3 stories (tight timing)
  🔴 Conflict:    1 story (scheduled before blocker)

CONFLICTS (Fix Required):
  ⚠️ PORTAL-456 "Widget Display" 
     Blocked by: CORE-789 "Widget API" (not in sprint)
     Recommendation: Add CORE-789 to Sprint 15 or defer PORTAL-456

RISKS (Monitor):
  ⚡ PORTAL-123 depends on CORE-456 (same sprint)
  ⚡ PORTAL-124 depends on CORE-456 (same sprint)
  ⚡ REPORT-88 has external dependency (Team B)

MISSING DEPENDENCIES (Suggested):
  📎 PORTAL-125 may depend on CORE-460 (similar patterns in past)
```

#### Backlog Health Report

Run weekly to assess overall backlog health:

```
BACKLOG HEALTH REPORT
Project: PORTFOLIO
Generated: 2026-02-01

STORIES ANALYZED: 47
─────────────────────────────────────────

DEPENDENCY COVERAGE
  Stories with dependencies:     23 (49%)
  Stories without dependencies:  24 (51%)
  AI-suggested missing deps:     12

TOP SUGGESTIONS (High Confidence):
  1. PORTAL-234 → likely depends on → API-112
  2. PORTAL-567 → likely depends on → DB-045
  3. REPORT-123 → likely depends on → ETL-789

CROSS-TEAM DEPENDENCIES
  Team B:  4 dependencies (2 at risk)
  Team C:  2 dependencies (healthy)
  External: 1 dependency (vendor)

CRITICAL PATH
  Longest chain: 5 stories deep
  CORE-001 → API-002 → PORTAL-003 → TEST-004 → DEPLOY-005
```

---

### AI Prompts for Planning Intelligence

#### `/dep-discover` — Discover Dependencies

```
Analyze this story/epic and identify all potential dependencies:

Story:
[Paste story title and description]

Backlog Context:
[Optional: Paste related stories or provide Jira project key]

Output:
1. Suggested predecessors (what must complete before this)
2. Suggested successors (what this unblocks)
3. External dependencies (other teams)
4. Confidence level for each suggestion
```

#### `/dep-health` — Sprint/Backlog Health Check

```
Analyze these stories for dependency health:

Stories:
[Paste list of stories or sprint contents]

Output:
1. Dependency conflicts (fix required)
2. At-risk dependencies (tight timing)
3. Missing dependency suggestions
4. Recommended sequencing
```

#### `/dep-sequence` — Optimal Build Order

```
Given these stories, recommend optimal build sequence:

Stories:
[Paste stories with known dependencies]

Output:
1. Recommended phases/order with rationale
2. Critical path identification
3. Parallel work opportunities
4. Risk flags
```

#### `/sprint-readiness` — Sprint Readiness Check

```
Assess this sprint's readiness:

Sprint Stories:
[Paste sprint contents]

Backlog:
[Paste or reference backlog for dependency context]

Output:
1. Dependency health summary (🟢/🟡/🔴)
2. Conflicts requiring resolution
3. Risks to monitor
4. External dependency status
5. Go/No-Go recommendation
```

---

### Human-in-the-Loop (HITL)

AI suggests, humans approve. This is NOT autonomous linking.

| AI Action | Human Action |
|:----------|:-------------|
| "Detected potential dependency" | Accept / Reject / Modify |
| "Recommended build order" | Adopt / Adjust |
| "Alert: Blocker risk" | Acknowledge / Dismiss |
| "Sprint not ready" | Remediate / Override |

---

### Key Takeaways

| Principle | Description |
|:----------|:------------|
| **Always-On** | Not point-in-time; continuous monitoring of Jira |
| **Jira-Centric** | Planning happens in Jira, not VS Code |
| **Suggestive, Not Autonomous** | AI proposes, humans approve |
| **Graph-Based** | Dependency graph as core data structure |
| **Predictive** | Forecasts problems before they occur |
| **Actionable** | Reports include specific recommendations |

---

## 16. Change Management: What-If Impact Assessment

### The Problem: Uncontrolled Change

Requirements change constantly in real projects:

| Change Source | Example |
|:--------------|:--------|
| **Stakeholder Request** | "Can we also add export to PDF?" |
| **Market Response** | Competitor launched feature, we need it too |
| **Regulatory** | New compliance requirement added |
| **Budget/Time** | "We need to cut scope by 30%" |
| **Technical Discovery** | "This approach won't work, we need to pivot" |

**Without impact analysis:**
- Changes cascade unpredictably
- Effort estimates are wrong
- Downstream artifacts become outdated
- Architecture decisions get invalidated
- Sprint plans fall apart

### The Solution: What-If Impact Assessment

Before any change is made, AI assesses the **full blast radius** across all artifacts.

**Key Principle:** Assessment only — this is a "What-If" analysis, not automatic changes.

---

### The Impact Cascade

Changes flow through the artifact hierarchy:

```
Requirement Change
       ↓
   ┌───────────────────────────────────────────┐
   │ PRD Impact                                │
   │ - Goals affected?                         │
   │ - Success metrics changed?                │
   │ - Stakeholder priorities shifted?         │
   └───────────────────────────────────────────┘
       ↓
   ┌───────────────────────────────────────────┐
   │ Epic Impact                               │
   │ - New Epics needed?                       │
   │ - Existing Epics modified?                │
   │ - Epics removed/orphaned?                 │
   └───────────────────────────────────────────┘
       ↓
   ┌───────────────────────────────────────────┐
   │ Story Impact                              │
   │ - Stories added/modified/removed?         │
   │ - Acceptance criteria changed?            │
   │ - Story points affected?                  │
   └───────────────────────────────────────────┘
       ↓
   ┌───────────────────────────────────────────┐
   │ Architecture Impact                       │
   │ - New components needed?                  │
   │ - Interfaces changed?                     │
   │ - Data model affected?                    │
   │ - Non-functional requirements changed?    │
   └───────────────────────────────────────────┘
       ↓
   ┌───────────────────────────────────────────┐
   │ Timeline Impact                           │
   │ - Sprint plans affected?                  │
   │ - Dependencies changed?                   │
   │ - Delivery date at risk?                  │
   └───────────────────────────────────────────┘
```

---

### Change Type Analysis

| Change Type | What AI Assesses |
|:------------|:-----------------|
| **Add** | What new artifacts are needed? What existing work is affected? |
| **Modify** | Which artifacts need updates? How much rework? |
| **Remove** | What becomes orphaned? What's unblocked? What's now missing? |

---

### Impact Assessment Report

When you run `/impact-assess`, AI generates a comprehensive report:

```
╔══════════════════════════════════════════════════════════════╗
║               WHAT-IF IMPACT ASSESSMENT                       ║
║           "Add PDF Export to Claims Report"                   ║
╚══════════════════════════════════════════════════════════════╝

CHANGE SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Type: ADD REQUIREMENT
Description: Users should be able to export claims reports to PDF format
Requestor: Product Owner
Priority: Medium

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PRD IMPACT: 🟡 MODERATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Section | Impact |
|:--------|:-------|
| Goals | No change - aligns with existing "reporting flexibility" goal |
| Features | ADD: "PDF Export for Reports" feature bullet |
| Success Metrics | ADD: "% of users using PDF export" |
| Scope | UPDATE: Include PDF generation capability |

ARTIFACTS TO UPDATE:
  📝 PRD.md - Add feature to scope section

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EPIC IMPACT: 🟢 LOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

| Epic | Impact |
|:-----|:-------|
| EPIC-001: Claims Reporting | ADD stories for PDF export |
| EPIC-002: User Dashboard | No impact |
| EPIC-003: Admin Portal | No impact |

NEW EPIC NEEDED: No (fits in existing Epic)

ARTIFACTS TO UPDATE:
  📝 EPIC-001.md - Add PDF export stories

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STORY IMPACT: 🟡 MODERATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NEW STORIES NEEDED:
  1. [NEW] "As a user, I can export any report to PDF format"
     Estimate: 5 points
  2. [NEW] "As a user, I can customize PDF layout options"
     Estimate: 3 points
  3. [NEW] "As a user, I receive PDF via email for large reports"
     Estimate: 5 points

TOTAL NEW EFFORT: 13 story points (~1.5 sprints)

EXISTING STORIES AFFECTED:
  • STORY-045: Add "Export" button (already in Sprint 12)
    → UPDATE: Extend to include PDF option

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ARCHITECTURE IMPACT: 🟡 MODERATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

COMPONENTS AFFECTED:
  📦 ReportService (MODIFY)
     - Add PDF generation method
     - Integrate with PDF library
  
  📦 ReportController (MODIFY)
     - Add /export/pdf endpoint

NEW COMPONENTS:
  📦 PdfGenerator (NEW)
     - Wrapper for PDF library
     - Template management

INTERFACES:
  🔗 ReportAPI - Add PDF endpoint
  🔗 No external interface changes

DATA MODEL:
  💾 No schema changes required

NON-FUNCTIONAL:
  ⚡ Performance: Large reports may need async processing
  📦 Dependencies: Add PDF library (e.g., wkhtmltopdf, Puppeteer)

ARTIFACTS TO UPDATE:
  📝 C4-components.md - Add PdfGenerator
  📝 openapi.yaml - Add /export/pdf endpoint
  📝 ADR-xxx.md - Decision on PDF library choice

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TIMELINE IMPACT: 🟡 MODERATE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EFFORT ESTIMATE:
  Stories: 13 points
  Architecture: 5 points (new component + ADR)
  Testing: 5 points
  TOTAL: ~23 points (2-3 sprints)

DEPENDENCIES:
  ⚠️ Must complete after STORY-045 (Export button)
  ⚠️ PDF library selection is blocking

SPRINT IMPACT:
  • Can fit in Sprint 13-14 if prioritized
  • Would displace ~23 points of planned work

RELEASE DATE IMPACT:
  ⚠️ If on critical path: +2-3 weeks
  ✓ If parallel: No impact on release

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

RECOMMENDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

PROCEED? CONDITIONAL YES

CONDITIONS:
1. Accept 2-3 sprint delay OR reduce other scope
2. Make ADR decision on PDF library first
3. Update EPIC-001 with new stories before sprint planning

ALTERNATIVES CONSIDERED:
• Client-side PDF (reduced effort, but quality issues)
• Defer to post-MVP (no current impact, future capability)
```

---

### AI Prompts for Change Management

#### `/impact-assess` — Full Impact Assessment

```
Assess the full impact of this proposed change:

## Change Description
[Describe the requirement change, addition, or removal]

## Context
[Provide relevant artifacts: PRD, Epics, Architecture docs]

## Output Required
1. PRD Impact (sections affected)
2. Epic Impact (new, modified, removed)
3. Story Impact (effort estimate)
4. Architecture Impact (components, interfaces, data)
5. Timeline Impact (sprints, dependencies, release date)
6. Recommendation (proceed, defer, alternatives)
```

#### `/scope-change` — Scope Reduction Analysis

```
Analyze the impact of reducing scope:

## Scope Reduction
[What features/requirements are being cut?]

## Current State
[PRD, Epics, Stories in progress]

## Output Required
1. What stories can be removed?
2. What work becomes orphaned?
3. What dependencies are affected?
4. What's the effort savings?
5. What risks are introduced by cutting?
```

#### `/architecture-impact` — Architecture-Focused Assessment

```
Assess the architecture impact of this change:

## Change
[Describe the requirement change]

## Current Architecture
[Provide C4 diagrams, component docs, data model]

## Output Required
1. Components affected
2. New components needed
3. Interface changes
4. Data model changes
5. Non-functional implications
6. ADRs needed
```

---

### Human-in-the-Loop

AI assesses, humans decide:

| AI Action | Human Action |
|:----------|:-------------|
| "Impact assessment complete" | Review findings |
| "Recommend proceed with conditions" | Accept / Reject / Modify scope |
| "Timeline at risk" | Decide on trade-offs |
| "Architecture changes needed" | Approve before proceeding |

---

### Key Takeaways

| Principle | Description |
|:----------|:------------|
| **Assess Before Acting** | Never make changes without understanding blast radius |
| **Full Cascade** | Changes flow through PRD → Epic → Story → Architecture → Timeline |
| **What-If Only** | This is impact assessment, not automatic implementation |
| **Human Decision** | AI recommends, humans decide on trade-offs |
| **Three Change Types** | Add, Modify, Remove each have different impacts |

---

## Conclusion

The AI-Augmented SDLC is not about replacing developers with AI. It's about:

1. **Eliminating repetitive work** — AI handles boilerplate, documentation
2. **Improving consistency** — Same patterns, same templates everywhere
3. **Accelerating feedback** — Errors caught earlier, delivered faster
4. **Enhancing quality** — More testing, better documentation
5. **Preserving human judgment** — Every AI output is reviewed

The framework works because it combines:
- **Structure** (clear phases, defined outputs)
- **Automation** (AI agents for repetitive tasks)
- **Governance** (human review, version control)
- **Integration** (everything connected: docs, code, tests, tickets)

This is the future of software development: humans and AI working together, each doing what they do best.

---

---

## Appendix A: Agent Registry

| Pillar | Agent / Directory | Key Prompts (Slash Commands) | Purpose |
|:-------|:------------------|:-----------------------------|:--------|
| Pillar | Agent | Key Slash Commands | Purpose |
|:-------|:------|:-------------------|:--------|
| **1: Home Base** | **Orchestrator** | `(User is Orchestrator)` | Invokes all other agents |
| **4: Requirements** | **PRD Agent** | `/prd-discover` | PRD from stakeholder input |
| **4: Elaboration** | **Epic Decomposition** | `/epic-split` | Break PRD into Epics |
| **4: Elaboration** | **Story Agent** | `/story-gen` | Break Epic into Stories |
| **4: Design** | **UX Agent** | `/ux-personas` | Personas & Wireframes |
| **4: Design** | **Interface Agent** | `/interface-spec` | API/Interface contracts |
| **4: Design** | **Architecture Agent** | `/arch-design` | C4 Diagrams, ADRs |
| **4: Build** | **Code Governance** | `/code-review` | Compliance check |
| **4: Test** | **Test Plan Agent** | `/test-plan` | E2E/Unit test plans |
| **4: Test** | **Simulation Agent** | `/simulate-persona` | User behavior simulation |
| **4: Test** | **Resilience Agent** | `/chaos-test` | Load & failure testing |
| **4: Release** | **Integration Agent** | `/ci-check` | Release readiness |
| **8: Planning** | **AI Planning Agent** | `/dep-discover` <br> `/dep-health` <br> `/dep-sequence` <br> `/sprint-readiness` | Dependency & Health check |
| **9: Change** | **Change Mgmt Agent** <br> `09_Change_Management/` | `/impact-assess` <br> `/scope-change` <br> `/architecture-impact` | "What-If" analysis for changes |

> ℹ️ **Note:** This table summarizes the primary interaction points. Each agent folder contains detailed READMEs and additional prompt templates.

---

## Glossary

| Term | Definition |
|:-----|:-----------|
| **ADR** | Architecture Decision Record — Documented architectural decision |
| **BDD** | Behavior-Driven Development — Writing tests as specifications |
| **C4 Model** | Four-level architecture visualization (Context, Container, Component, Code) |
| **Context Window** | The maximum amount of text an AI model can process at once |
| **DBML** | Database Markup Language — Text format for database schemas |
| **Epic** | Large body of work that can be broken into smaller stories |
| **Gherkin** | Structured language for acceptance criteria (Given/When/Then) |
| **Git** | Version control system for tracking file changes |
| **HITL** | Human-in-the-Loop — Requiring human approval for AI actions |
| **INVEST** | Criteria for good stories (Independent, Negotiable, Valuable, Estimable, Small, Testable) |
| **Mermaid** | Text-to-diagram tool |
| **OpenAPI** | Standard format for API documentation |
| **PRD** | Program Requirements Document |
| **RAG** | Retrieval Augmented Generation — Fetching relevant information before AI generation |
| **SPIDR** | Epic splitting framework (Spike, Path, Interface, Data, Rules) |
| **SDLC** | Software Development Lifecycle |
| **Story** | Small unit of work delivering user value |
| **Token** | The basic unit of text that AI models process (roughly 4 characters) |
| **UX** | User Experience — The overall experience of using a product |
| **Wireframe** | Low-fidelity visual representation of a screen layout |
