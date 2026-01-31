---
title: "AI Agent Recommendations for the AI-Augmented SDLC"
author: "Framework Design Team"
date: "2025-11-05"
status: "Draft for Discussion"
---

# AI Agent Recommendations for the AI-Augmented SDLC

## 1. Executive Summary

This document proposes a suite of **specialized AI agents** to support teams through the AI-Augmented SDLC. Each agent acts as a **collaborative peer** (not a replacement) for specific roles, helping with documentation, iteration, validation, and consistency.

### Key Principles
- **Agents are collaborators, not automators** - They work WITH humans in conversational loops
- **Iterative refinement** - Multiple sessions, revisions, and approvals
- **Role-specific expertise** - Each agent specializes in one discipline
- **Template-driven** - All agents use framework templates and examples
- **Jira integration** - Agents can create/update Jira tickets
- **Multi-user collaboration** - Support for teams working together

---

## 2. The Real-World Workflow

### Current Reality: Multi-Session, Multi-Person Process

Unlike our example (which was created in a single intensive session), real projects involve:

#### Phase 1: PRD Creation (2-4 weeks)
- **Participants:** Product Owner, Business Analysts, Stakeholders
- **Sessions:** 5-10 working sessions
- **Process:**
  1. Initial brainstorm (stakeholders present requirements)
  2. Draft PRD sections (Business Intent, Functional Envelope)
  3. Review sessions (iterate on scope, objectives)
  4. Architecture consultation (feasibility check)
  5. Stakeholder presentation (get feedback)
  6. Revisions (incorporate feedback)
  7. Final approval (sign-off)

#### Phase 2: Architecture Hub Creation (1-2 weeks)
- **Participants:** Solution Architect, Tech Leads, Security
- **Sessions:** 3-5 working sessions
- **Process:**
  1. Review approved PRD
  2. Create high-level architecture diagrams
  3. Draft API contracts (OpenAPI specs)
  4. Define data models
  5. Document key decisions (ADRs)
  6. Security review
  7. Final architecture sign-off

#### Phase 3: Epic Decomposition (1 week)
- **Participants:** Product Owner, Business Analysts, Tech Leads
- **Sessions:** 2-3 working sessions
- **Process:**
  1. Review PRD functional envelope
  2. Brainstorm candidate epics
  3. Define epic scope and acceptance criteria
  4. Create epics in Jira
  5. Link epics to PRD sections (traceability)
  6. Prioritize epics for roadmap

#### Phase 4: Portfolio Epic Breakdown (2-3 weeks per portfolio)
- **Participants:** Business Analysts (team of 3-5)
- **Sessions:** Many (ongoing work)
- **Process:**
  1. BA takes ownership of 1-2 portfolio epics
  2. Decomposes into component epics (5-10 per portfolio epic)
  3. Writes detailed epic specifications
  4. Peer review (other BAs)
  5. Creates epics in Jira with links
  6. Iterates based on feedback

#### Phase 5: Story Authoring (Ongoing throughout sprints)
- **Participants:** Business Analysts, Developers, QA Engineers
- **Sessions:** Sprint planning, backlog refinement
- **Process:**
  1. Select epic for upcoming sprint
  2. BA drafts stories with context links
  3. Dev adds technical implementation plan
  4. QA adds test scenarios (Gherkin)
  5. Team review (refinement session)
  6. Stories marked "Ready for Development"
  7. Created in Jira with proper links

#### Phase 6: Test Planning (Parallel with stories)
- **Participants:** QA Engineers
- **Process:**
  1. Review stories as they're created
  2. Analyze Gherkin acceptance criteria
  3. Identify edge cases and boundary conditions
  4. Create test strategy document
  5. Generate test cases from Gherkin
  6. Review with BA and Dev

---

## 3. Proposed AI Agent Suite

### Agent Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                   ORCHESTRATOR LAYER                         │
│  (Routes user to appropriate agent based on context)         │
└────────────────────────┬────────────────────────────────────┘
                         │
        ┌────────────────┼────────────────┬─────────────────┐
        │                │                │                 │
┌───────▼───────┐ ┌──────▼──────┐ ┌──────▼──────┐ ┌────────▼────────┐
│ Agent: PRD    │ │ Agent:      │ │ Agent:      │ │ Agent:          │
│ Collaborator  │ │ Architecture│ │ Epic        │ │ Story           │
│               │ │ Designer    │ │ Decomposer  │ │ Author          │
└───────┬───────┘ └──────┬──────┘ └──────┬──────┘ └────────┬────────┘
        │                │                │                 │
        │                │                │                 │
┌───────▼────────────────▼────────────────▼─────────────────▼────────┐
│                     SHARED CONTEXT LAYER                            │
│  • Framework Templates  • Example Documents  • Jira Integration     │
│  • Git Repository      • Organization Guidelines                    │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 4. Detailed Agent Specifications

### Agent 1: PRD Collaborator

**Role:** Assists Product Owner and BAs in creating comprehensive PRDs through iterative conversation

#### Responsibilities
- Guide user through PRD template sections
- Ask clarifying questions to elicit requirements
- Expand brief inputs into well-written prose
- Maintain consistency across sections
- Suggest completeness checks (missing sections)
- Reference example PRD (ETF Portfolio Analyzer)
- Track PRD version history

#### User Workflow
```
User: "I want to build a customer support ticketing system"

Agent: "Great! Let's start building your PRD. I'll guide you through
each section. First, let's establish the Business Intent.

Can you tell me:
1. What problem does this solve?
2. Who are the primary users?
3. What's the key business objective?"

User: [Provides brief answers]

Agent: "Based on what you've told me, here's a draft Business Intent
section:

[Generated prose]

Does this capture your vision? Any changes?"

User: "Yes, but add that we need to reduce support costs by 30%"

Agent: "Updated. Now let's move to the Functional Envelope. Looking
at your problem, I anticipate these major capabilities:
1. Ticket creation and management
2. User/agent assignment
3. Status tracking and workflows
4. Reporting and analytics

Do these align with your vision, or should we adjust?"

[Continues through all PRD sections]
```

#### Conversation Style
- **Interviewer mode** - Asks structured questions
- **Scribe mode** - Captures and expands user input
- **Validator mode** - Checks for completeness and consistency
- **Advisor mode** - Suggests best practices from framework

#### Key Features
1. **Section-by-section guidance** - Never overwhelms user
2. **Progressive refinement** - Multiple passes over same content
3. **Example referencing** - Shows relevant parts of ETF example
4. **Version tracking** - "You last worked on this on Nov 3rd, Section 4"
5. **Stakeholder mode** - Can explain PRD to non-technical stakeholders
6. **Export** - Generate markdown file when complete

#### Integration Points
- **Input:** User's verbal/written requirements, meeting notes, existing docs
- **Output:** PRD markdown file (prd.md)
- **Storage:** Git repository (version controlled)
- **Handoff:** Passes completed PRD to Architecture Designer agent

---

### Agent 2: Architecture Designer

**Role:** Assists Solution Architect in creating Architecture Hub through collaborative design sessions

#### Responsibilities
- Guide architect through architecture decisions
- Generate ADR drafts from decision discussions
- Create OpenAPI spec boilerplates from API descriptions
- Generate data model schemas from entity descriptions
- Create Mermaid diagrams from text descriptions
- Validate technical consistency
- Suggest architectural patterns from Asset Library

#### User Workflow
```
Architect: "I need to document my decision to use Firestore for the
portfolio data"

Agent: "Let's create an ADR. I'll guide you through it.

ADR Title: Use Firestore for Portfolio Storage

First, describe the CONTEXT - what decision needs to be made and why?"

Architect: "We need a database for user portfolios. Requirements are:
- Single user initially
- Need flexibility for nested data (ETFs with holdings)
- Want serverless (no DB management)
- Must integrate well with GCP"

Agent: "Good context. Now, what ALTERNATIVES did you consider?"

Architect: "Cloud SQL, BigQuery, Firestore"

Agent: "For each, can you briefly explain pros/cons/why rejected?"

[Architect provides input]

Agent: "Great! Here's your draft ADR:

[Generated ADR following template]

Sections complete:
✅ Context
✅ Alternatives Considered
⏳ Decision (needs your input)
⏳ Consequences

Ready to continue with Decision and Consequences?"
```

#### Specialized Capabilities

**ADR Generation:**
- Guides through template sections
- Suggests alternatives based on context
- Validates completeness
- Cross-references other ADRs

**OpenAPI Spec Generation:**
```
Architect: "I need an API for portfolio CRUD operations"

Agent: "Let's create the OpenAPI spec. What endpoints do you need?

I'm thinking:
- GET /api/portfolio (retrieve)
- POST /api/portfolio/etfs (add ETF)
- PUT /api/portfolio/etfs/{id} (update)
- DELETE /api/portfolio/etfs/{id} (remove)

Is this the right set?"

Architect: "Yes, plus we need individual stocks too"

Agent: "Got it. I'll add those. What data fields does an ETF holding need?"

Architect: "Ticker, units, current price, last updated timestamp"

Agent: "Perfect. Generating OpenAPI spec...

[Creates complete portfolio-service-api.yaml]

I've created:
- All CRUD endpoints
- Request/response schemas
- Example payloads
- Error responses

Want to review or add anything?"
```

**Data Model Generation:**
```
Architect: "I need the Firestore schema for portfolios"

Agent: "Let's design it. You mentioned:
- ETFs with ticker, units, price
- Individual stocks

Should these be:
A) Separate collections (portfolios, etfs, stocks)
B) Single collection with nested arrays
C) Hybrid approach

What's your preference?"

Architect: "Single collection, nested arrays"

Agent: "Good choice for single-user. Generating schema...

[Creates firestore-portfolio-schema.json]

Notes I've added:
- UUID for holding IDs
- Timestamp fields
- Validation rules (units > 0)
- Document size estimate

Any changes needed?"
```

**Diagram Generation:**
```
Architect: "I need a sequence diagram for the 'Refresh All' flow"

Agent: "Walk me through the flow step by step:

1. What triggers it?
2. What services are involved?
3. What happens first, second, third...?"

Architect: [Describes flow]

Agent: "Here's your Mermaid sequence diagram:

[Generates sequence-refresh-all.mmd]

Shows:
- User → Frontend → Services → External APIs
- Parallel calls to Market Data
- Sequential Holdings extractions
- Firestore updates

Accurate?"
```

#### Integration Points
- **Input:** Approved PRD, architect's requirements
- **Output:** ADRs, OpenAPI specs, data models, diagrams
- **Storage:** Git repository (docs/architecture-hub/)
- **Validation:** Checks OpenAPI syntax, schema validity
- **Handoff:** Passes Architecture Hub to Epic Decomposer

---

### Agent 3: Epic Decomposer

**Role:** Assists Product Owner/BAs in decomposing PRD into epics through collaborative analysis

#### Responsibilities
- Analyze PRD's Functional Envelope
- Propose candidate epics (both Business and Enabler)
- Help scope each epic (in/out of scope)
- Draft acceptance criteria
- Identify dependencies between epics
- Create epics in Jira with proper fields
- Maintain traceability (epic ↔ PRD section)

#### User Workflow
```
BA: "I need to break down the ETF Portfolio Analyzer PRD into epics"

Agent: "I've read the PRD. Looking at the Functional Envelope (Section 3),
I see 5 major capabilities:

1. Portfolio Management (CRUD)
2. Market Data Integration (Yahoo Finance)
3. AI-Powered Holdings Extraction (Gemini)
4. Exposure Aggregation & Analytics
5. Performance Tracking & Attribution

These map naturally to 5 Business Epics. Additionally, based on the
Architecture Hub, I recommend these Enabler Epics:

E1. Authentication & Password Protection
E2. Multi-Currency Infrastructure
E3. DevOps Pipeline Setup

Does this breakdown make sense, or should we adjust?"

BA: "Good start, but combine #4 and #5 into one epic"

Agent: "Updated. So we have:

Business Epics (4):
1. Portfolio Management
2. Market Data Integration
3. AI-Powered Holdings Extraction
4. Analytics, Performance & Attribution

Enabler Epics (3):
E1. Authentication
E2. Multi-Currency
E3. DevOps Pipeline

Let's flesh out each one. Starting with Epic 1: Portfolio Management.

What's the user story for this epic?"

BA: "As an investor, I want to manage my portfolio of ETFs and stocks"

Agent: "Good. Now let's define scope:

IN SCOPE (what I think based on PRD):
- Add ETF with ticker + units
- Add individual stock with ticker + shares
- Edit quantities
- Remove holdings
- View portfolio list

OUT OF SCOPE:
- Brokerage integration (manual entry only)
- Historical position tracking
- Tax lot management

Does this scope feel right?"

[BA confirms/adjusts]

Agent: "Great. Now acceptance criteria. I'll draft in Gherkin format:

Given I am on the portfolio page
When I click 'Add ETF'
Then I should see a form with fields: ticker, units
  And I can submit to save the ETF

[More scenarios...]

Look good?"

[Iterates until epic is complete]

Agent: "Epic 1 is ready! Should I:
A) Create it in Jira now
B) Move to Epic 2
C) Let you review the whole set first"
```

#### Specialized Capabilities

**Epic Analysis:**
- Reads PRD and identifies natural boundaries
- Distinguishes Business vs Enabler epics
- Checks for reasonable size (2-4 sprints worth)
- Validates vertical slicing

**Jira Integration:**
```
Agent: "Ready to create Epic 1 in Jira. I'll set:

- Project: ETF-ANALYZER
- Epic Name: Portfolio Management
- Description: [Generated from our conversation]
- Priority: High
- Target Release: v1.0
- PRD Link: [Link to prd.md section 3.1]

Create it?"

BA: "Yes"

Agent: "Created! Jira Epic ID: EPA-001

I've also:
- Added acceptance criteria as a comment
- Linked to PRD section 3.1 (custom field)
- Added label: business-epic
- Set status: Ready for Breakdown

URL: https://your-jira.atlassian.net/browse/EPA-001"
```

**Portfolio Epic Assignment:**
```
Agent: "You have 5 Business Analysts on your team. These 4 business epics
need to be broken down into component epics (portfolio epics).

Suggested assignment:
- BA Team 1 (Alice, Bob): EPA-001 Portfolio Management
- BA Team 2 (Carol, Dan): EPA-002 Market Data Integration
- BA Solo (Eve): EPA-003 AI Holdings Extraction
  [This is simpler, one person can handle]
- BA Team 3 (Frank, Grace): EPA-004 Analytics & Performance

Does this workload distribution make sense?"

BA: "Yes, assign it"

Agent: "Done. I've:
- Updated Jira epic assignees
- Sent Slack notifications to each BA
- Created workspace folders for collaboration
- Provided each team with:
  - Parent epic specification
  - PRD sections relevant to their epic
  - Architecture Hub relevant sections
  - Example epic (EPA-003 from examples)

Teams can now start component epic breakdown."
```

#### Integration Points
- **Input:** Approved PRD, Architecture Hub
- **Output:** Epic documents (markdown), Jira epics
- **Storage:** Git (docs/epics/), Jira
- **Handoff:** Assigns epics to BA teams for breakdown
- **Notifications:** Slack/email to assigned BAs

---

### Agent 4: Portfolio Epic Breakdown Assistant

**Role:** Assists BA teams in decomposing large portfolio epics into component epics

**Note:** This is a specialized version of Epic Decomposer focused on portfolio epic → component epic breakdown (not PRD → epic).

#### Responsibilities
- Analyze parent portfolio epic
- Identify natural component boundaries
- Help scope each component epic
- Ensure vertical slicing
- Maintain consistency across component epics
- Create component epics in Jira as children
- Facilitate peer review between BAs

#### User Workflow
```
BA Alice: "I need to break down EPA-001 Portfolio Management into
component epics"

Agent: "I've read EPA-001. The scope is quite large:
- ETF management
- Individual stock management
- Portfolio settings (currency)
- Portfolio viewing/summary

I recommend 3 component epics:

EPA-001-A: ETF Holdings Management
EPA-001-B: Individual Stock Holdings Management
EPA-001-C: Portfolio Settings & Display

Each would be 1-2 sprints. Sound right?"

BA Alice: "Yes, but also add a fourth for bulk import"

Agent: "Good idea for v2, but checking the parent epic scope...
bulk import is marked 'Out of Scope' in EPA-001.

Should we:
A) Keep it out of scope (add to backlog for v2)
B) Add it to EPA-001 scope (requires Product Owner approval)
C) Create a separate epic for it"

BA Alice: "A - keep it out"

Agent: "Got it. Let's flesh out EPA-001-A: ETF Holdings Management.

User story?"

[Conversation continues similar to Epic Decomposer]
```

#### Key Difference from Epic Decomposer
- Works at lower granularity (epic → component epics)
- Focuses on implementation details
- Coordinates multiple BAs working in parallel
- Peer review facilitation

#### Peer Review Mode
```
BA Alice: "I've completed EPA-001-A. Can you get Bob to review?"

Agent: "I'll facilitate. [Notifies Bob]

Bob, Alice has completed EPA-001-A: ETF Holdings Management.

Key points for review:
- 8 user stories planned
- Vertical slice (UI → API → DB)
- Links to Architecture Hub API contract
- Gherkin AC provided

[Shows summary]

Please review for:
✓ Consistent with parent epic EPA-001?
✓ Scope reasonable for 1-2 sprints?
✓ Dependencies clear?
✓ Any overlap with EPA-001-B?

Your feedback?"

BA Bob: "Looks good, but story 5 should move to EPA-001-B"

Agent: "Alice, Bob suggests story 5 belongs in EPA-001-B (Stock management).

Story 5: 'Allow user to filter portfolio view by holding type'

I agree - this is a display concern, not specific to ETFs.

Move it?"

BA Alice: "Yes"

Agent: "Moved. EPA-001-A updated. Marking as Peer Reviewed ✓"
```

---

### Agent 5: Story Author

**Role:** Assists BAs, Devs, and QA in creating AI-Ready Stories through collaborative authoring

#### Responsibilities
- Guide user through all 4 story sections
- Populate "Context & Links" automatically from epic/PRD/Architecture Hub
- Help write specific Gherkin acceptance criteria
- Collaborate with Dev on technical implementation plan
- Collaborate with QA on test scenarios
- Validate story is vertically sliced
- Create story in Jira with all links
- Ensure story is "Ready for Development"

#### User Workflow (Multi-Role Collaboration)

**Phase 1: BA Creates Story Skeleton**
```
BA: "I need a story for adding an ETF to the portfolio"

Agent: "Let's create it. Starting with Context & Links - I'll populate
this automatically:

Context & Links:
✅ Parent Epic: EPA-001-A (ETF Holdings Management)
✅ PRD: Section 3.1 Portfolio Management
✅ Architecture Hub:
  ✅ API Contract: portfolio-service-api.yaml, POST /api/portfolio/etfs
  ✅ Data Model: firestore-portfolio-schema.json
✅ Design Hub: [Checking...] No wireframe yet. Should there be one?

BA: "Yes, we need a wireframe for the Add ETF form"

Agent: "Noted. I'll add a TODO:
⏳ Design Hub: Wireframe needed - Add ETF form

Now let's write the user story title. How about:
'Add ETF to Portfolio'

And the story:
'As an investor, I want to add an ETF to my portfolio by entering the
ticker and number of units, so that I can track my holdings.'

Accurate?"

BA: "Yes"

Agent: "Great. Now Gherkin acceptance criteria. I'll start with the
happy path:

Scenario 1: Successfully add ETF

Given I am on the Portfolio page
  And I have no ETFs in my portfolio yet
When I click the 'Add ETF' button
Then I should see a form with fields:
  | Field | Type | Required |
  | Ticker | Text input | Yes |
  | Units | Number input | Yes |
And when I enter 'QQQ' and '100'
  And I click 'Save'
Then the ETF should be added to my portfolio
  And I should see 'QQQ - 100 units' in my portfolio list
  And I should see a success message 'ETF added successfully'

Sound right?"

BA: "Yes, but also add validation scenarios"

Agent: "Good call. Adding:

Scenario 2: Validation - Empty ticker

Given I am on the Add ETF form
When I leave Ticker empty
  And I enter '100' for Units
  And I click 'Save'
Then I should see error 'Ticker is required'
  And the ETF should NOT be saved

Scenario 3: Validation - Invalid ticker format

Given I am on the Add ETF form
When I enter 'qqq' (lowercase) for Ticker
  And I click 'Save'
Then I should see error 'Ticker must be uppercase'

[3 more validation scenarios...]

How's that?"

BA: "Perfect. Story draft is done. Ready for Dev to add technical plan."

Agent: "Saving story EPA-001-A-001 as draft. I'll notify Dev team."
```

**Phase 2: Developer Adds Technical Implementation Plan**
```
Developer: "I need to add technical plan to EPA-001-A-001"

Agent: "Welcome! BA has completed sections 1-2. Here's what we have:
[Shows Context & Links, Gherkin AC]

Now let's build Section 3: Technical Implementation Plan.

Based on the API contract (POST /api/portfolio/etfs), I suggest:

Files to Modify:
1. frontend/src/pages/Portfolio.tsx
   - Add 'Add ETF' button
   - Create AddETFModal component

2. frontend/src/components/AddETFModal.tsx (NEW FILE)
   - Form with ticker + units fields
   - Validation logic
   - API call to POST /api/portfolio/etfs

3. backend/services/portfolio/routes.py
   - Endpoint already exists in API contract ✓
   - Just implement according to spec

4. backend/services/portfolio/firestore_client.py
   - Function: save_etf_to_portfolio(user_id, etf_data)

Does this match your mental model?"

Dev: "Yes, but I also need to handle duplicate ETFs"

Agent: "Good catch. The API returns 409 Conflict if ETF already exists
(per OpenAPI spec). I'll add:

5. frontend/src/components/AddETFModal.tsx
   - Handle 409 response
   - Show error: 'QQQ already in portfolio. Use Edit instead.'

Updated. Now, key functions to implement?"

Dev: "Just the save function in Firestore"

Agent: "Got it:

Key Functions:
- save_etf_to_portfolio(user_id, ticker, units)
  → Validates ticker format
  → Checks for duplicates
  → Creates UUID for holding
  → Saves to Firestore portfolios/{user_id}.etfs[]
  → Returns ETFHolding object

Environment variables needed?"

Dev: "FIRESTORE_PROJECT, FIRESTORE_DATABASE"

Agent: "Added. Technical plan complete. Ready for QA to add
collaboration plan."
```

**Phase 3: QA Adds AI Collaboration Plan & Test Scenarios**
```
QA Engineer: "I need to add testing details to EPA-001-A-001"

Agent: "Welcome! BA and Dev have completed sections 1-3.

I've analyzed the Gherkin AC (6 scenarios). For Section 4
(AI Collaboration Plan), I recommend:

Phase 1: Dev implements form UI
Phase 2: AI generates Firestore save function
Phase 3: AI generates Playwright test stubs from Gherkin
Phase 4: QA fills in test implementation

Make sense?"

QA: "Yes, but I want AI to also generate negative test cases"

Agent: "Adding:

Phase 3b: AI generates additional edge case tests:
- Boundary conditions (units = 0, units = negative)
- Ticker with special characters
- Network failure scenarios
- Firestore write failures

Good?"

QA: "Perfect"

Agent: "Story EPA-001-A-001 is now COMPLETE! All 4 sections done.

Ready to:
✅ Mark as 'Ready for Development'
✅ Create in Jira
✅ Link all architecture artifacts
✅ Add to Sprint backlog

Shall I proceed?"

BA/Dev/QA: "Yes"

Agent: "Created!

Jira Story: EPA-001-A-001
URL: https://your-jira.atlassian.net/browse/EPA-001-A-001
Status: Ready for Development
Sprint: [Awaiting assignment]

Story is complete and ready for sprint planning! 🎉"
```

#### Key Features

**Auto-Population of Context:**
- Reads parent epic, PRD, Architecture Hub
- Finds relevant API contracts, data models
- Identifies missing artifacts (wireframes)
- Creates proper links in story

**Vertical Slice Validation:**
```
Agent: "Let me check if this story is vertically sliced...

✓ Frontend component (AddETFModal)
✓ API endpoint (POST /api/portfolio/etfs)
✓ Backend logic (save function)
✓ Database (Firestore write)

Yes, this is vertically sliced! ✓"
```

**Completeness Checker:**
```
Agent: "Story readiness check:

Section 1: Context & Links
✅ Parent epic linked
✅ PRD section linked
✅ API contract linked
✅ Data model linked
⚠️  No wireframe (marked as TODO)

Section 2: Gherkin AC
✅ 6 scenarios (happy path + validations)
✅ Specific and measurable

Section 3: Technical Implementation Plan
✅ Files listed
✅ Functions specified
✅ Environment variables documented

Section 4: AI Collaboration Plan
✅ Clear dev+AI workflow
✅ QA test generation plan

Overall: 95% ready (waiting on wireframe)
Can proceed without wireframe if needed."
```

#### Integration Points
- **Input:** Epic, PRD, Architecture Hub, Design Hub
- **Output:** Story markdown file, Jira story ticket
- **Collaboration:** Supports multi-role (BA → Dev → QA)
- **Notifications:** Alerts next person in workflow
- **Validation:** Checks completeness, vertical slicing

---

### Agent 6: Test Planning Assistant

**Role:** Assists QA Engineers in creating comprehensive test strategies from stories

#### Responsibilities
- Analyze Gherkin acceptance criteria
- Identify edge cases and boundary conditions
- Generate test case lists
- Create test data requirements
- Suggest automation approach
- Generate Playwright test stubs
- Link tests to stories (traceability)

#### User Workflow
```
QA: "I need to create tests for EPA-001-A-001 (Add ETF)"

Agent: "I've read the story. It has 6 Gherkin scenarios covering:
- Happy path (add ETF successfully)
- Validation errors (5 scenarios)

I recommend this test strategy:

Unit Tests (for backend):
1. test_save_etf_to_firestore_success()
2. test_save_etf_duplicate_returns_409()
3. test_save_etf_invalid_ticker_format()

Integration Tests:
4. test_api_endpoint_add_etf()
5. test_firestore_write_and_read()

E2E Tests (Playwright, from Gherkin):
6. Scenario 1: Successfully add ETF
7. Scenario 2: Validation - Empty ticker
8. Scenario 3: Validation - Invalid ticker format
9. Scenario 4: Validation - Zero units
10. Scenario 5: Validation - Negative units
11. Scenario 6: Duplicate ETF shows error

Additionally, I suggest these edge cases:
12. Network timeout during API call
13. Firestore write failure
14. Concurrent add (two users add same ETF)
15. Very large units value (boundary test)

Total: 15 test cases. Sound comprehensive?"

QA: "Yes, generate the Playwright tests"

Agent: "Generating from Gherkin...

[Creates test-add-etf.spec.ts]

Done! I've created 6 E2E test functions matching your Gherkin scenarios.
Each includes:
- Descriptive test name
- Arrange/Act/Assert structure
- Page object pattern
- Assertions matching Given/When/Then

Stubs are ready for you to fill in locators and complete implementation.

Want me to also generate the unit test stubs?"

QA: "No, Dev will do those"

Agent: "Got it. Test plan documented. Shall I:
A) Add test case links to Jira story EPA-001-A-001
B) Create test execution checklist
C) Both"

QA: "Both"

Agent: "Done! Jira story updated with 'Test Cases' section linking to:
- test-add-etf.spec.ts (E2E)
- Test case IDs: TC-001 through TC-015

And I've created a test execution checklist in your QA workspace."
```

#### Specialized Capabilities

**Edge Case Generation:**
```
Agent: "Analyzing your Gherkin scenarios, I notice some missing edge cases:

Your scenarios cover:
✓ Empty ticker
✓ Invalid format
✓ Zero units
✓ Duplicate ETF

Missing edge cases:
❌ Ticker too long (>5 characters)
❌ Units with decimals (should we allow 100.5 units?)
❌ Ticker with numbers (should 'VOO3' be valid?)
❌ Network failure during submit
❌ Session timeout during form interaction
❌ Browser back button after submit

Shall I add scenarios for these?"
```

**Test Data Management:**
```
Agent: "For these tests, you'll need test data. I recommend:

Valid Test Data:
- Tickers: QQQ, SPY, IUSG (known to exist)
- Units: 100, 50, 25.5 (if decimals allowed)

Invalid Test Data:
- Empty ticker: ''
- Lowercase: 'qqq'
- Too long: 'TOOLONG'
- Special chars: 'Q@Q'
- Zero units: 0
- Negative units: -50

Should I create a test-data.json file with these?"

QA: "Yes"

Agent: "Created test-data.json in test fixtures folder."
```

#### Integration Points
- **Input:** Stories with Gherkin AC
- **Output:** Test plans, Playwright stubs, test data
- **Traceability:** Links tests to stories in Jira
- **CI/CD:** Test files ready for pipeline integration

---
 
 ### Agent 7: Infrastructure Engineer
 
 **Role:** Automates the creation of "Infrastructure as Code" (IaC) and CI/CD pipelines to deploy the Architect's designs.
 
 #### Responsibilities
 - Analyze Architecture Hub (API Contracts, Data Models, Diagrams)
 - Generate Terraform/Pulumi code for cloud resources
 - Create Dockerfiles for containerized services
 - Configure CI/CD pipelines (GitHub Actions, Cloud Build)
 - Estimate cloud costs
 - Implement security best practices (IAM, Secrets)
 
 #### User Workflow
 ```
 DevOps Lead: "I need to deploy the Clothes Picker to Google Cloud"
 
 Agent: "I've analyzed the Architecture Hub:
 1. Compute: Cloud Run (for Python Backend)
 2. Data: Firestore (from DBML)
 3. Auth: Firebase Auth
 
 I will now generate the Terraform configuration to provision these.
 
 > Generating infra/main.tf...
 > Generating infra/variables.tf...
 > Generating infra/iam.tf...
 
 I have defined:
 - google_cloud_run_service (with IAM for public access)
 - google_firestore_database
 - google_service_account (for the backend identity)
 
 Would you like me to also create the GitHub Actions workflow?"
 
 DevOps Lead: "Yes, for staging and prod"
 
 Agent: "Generating .github/workflows/deploy.yml...
 
 Pipeline features:
 - Triggers on push to main
 - Builds Docker image
 - Pushes to Artifact Registry
 - Deploys to Cloud Run (Staging)
 - Awaits Manual Approval -> Deploys to Cloud Run (Prod)"
 ```
 
 #### Specialized Capabilities
 - **Terraform Generation:** Knows the latest GCP providers and resources.
 - **Containerization:** Writes optimized multi-stage Dockerfiles.
 - **Security Scanning:** Can audit IaC for common vulnerabilities (e.g., public buckets).
 
 #### Integration Points
 - **Input:** Architecture Hub, Application Source Code
 - **Output:** Terraform files (`.tf`), Dockerfiles, CI/CD YAML
 - **Handoff:** Passes deploy URL back to QA Agent for E2E testing
 
 ---
 
 ## 5. Agent Interaction Patterns

### Pattern 1: Sequential Handoff
```
PRD Collaborator → Architecture Designer → Epic Decomposer → Story Author
```
Each agent completes its phase and passes artifacts to the next.

### Pattern 2: Parallel Collaboration
```
Multiple Story Authors working on different epics simultaneously
Multiple Portfolio Epic Breakdown Assistants with different BA teams
```

### Pattern 3: Iterative Refinement
```
User ↔ Agent (multiple rounds)
- Draft
- Review
- Revise
- Review again
- Approve
```

### Pattern 4: Multi-Role Story Building
```
BA (Context + Gherkin) → Dev (Technical Plan) → QA (Test Plan) → Review Loop
```

---

## 6. Implementation Recommendations

### Phase 1: MVP Agents (Weeks 1-4)
**Priority:** Build these first
1. **PRD Collaborator** - Most value, used earliest
2. **Story Author** - High usage, impacts entire team
3. **Epic Decomposer** - Bridges PRD to Stories

### Phase 2: Specialized Agents (Weeks 5-8)
4. **Architecture Designer** - Complex but high value
5. **Portfolio Epic Breakdown** - Supports BA teams
6. **Test Planning Assistant** - QA efficiency

### Phase 3: Integration & Polish (Weeks 9-12)
- Jira integration (bi-directional)
- Slack notifications
- Git commits for documents
- Agent-to-agent handoffs
- User feedback and iteration

---

## 7. Technical Architecture

### Recommended Stack

**Agent Platform:**
- **Option A:** Custom (Python + LangChain/LlamaIndex)
- **Option B:** Vertex AI Agent Builder
- **Option C:** Microsoft Copilot Studio

**LLM:**
- Gemini 1.5 Pro (for GCP-native approach)
- Claude Sonnet 3.5 (for best reasoning)
- GPT-4 (for broad ecosystem support)

**Storage:**
- Git for documentation (version control)
- Jira for work items
- Firestore for agent state/memory
- Cloud Storage for generated artifacts

**Interfaces:**
- **Web UI:** Chat interface (React)
- **Slack:** Conversational commands
- **VS Code Extension:** For developers
- **CLI:** For power users/automation

---

## 8. Agent Memory & Context Management

### Challenge
Real PRD/Epic/Story creation spans multiple sessions over days/weeks. Agents need to:
- Remember previous conversations
- Track document version history
- Know where user left off
- Resume work seamlessly

### Solution: Persistent Memory Per Artifact

```json
{
  "artifact_type": "PRD",
  "artifact_id": "etf-portfolio-analyzer",
  "user_id": "product-owner-123",
  "sessions": [
    {
      "session_id": "sess-001",
      "date": "2025-11-01",
      "sections_worked": ["Business Intent", "Functional Envelope"],
      "status": "In Progress",
      "next_section": "Scope Boundaries"
    },
    {
      "session_id": "sess-002",
      "date": "2025-11-03",
      "sections_worked": ["Scope Boundaries", "System Impact"],
      "status": "In Progress",
      "next_section": "Architecture Sketch"
    }
  ],
  "document_versions": [
    {
      "version": "0.1",
      "date": "2025-11-01",
      "git_commit": "abc123",
      "status": "Draft"
    }
  ],
  "pending_reviews": [
    {
      "reviewer": "stakeholder-456",
      "section": "Business Intent",
      "status": "Approved"
    }
  ]
}
```

### Resumption Example
```
User: "Let's continue working on the PRD"

Agent: "Welcome back! Last time (Nov 3), we completed the Scope
Boundaries section. You were working on Section 5: System Impact.

I see you have feedback from your stakeholder on Business Intent -
they approved it ✓

Would you like to:
A) Continue with System Impact (Section 5)
B) Review/revise based on stakeholder feedback
C) Work on a different section"
```

---

## 9. Jira Integration Requirements

### Core Capabilities Needed

**Read Operations:**
- Fetch epic details by ID
- Query stories in epic
- Get custom field values (PRD link, Architecture link)
- Read comments/description

**Write Operations:**
- Create epics with fields populated
- Create stories linked to epics
- Update epic/story fields
- Add comments
- Update status
- Add links (PRD, Architecture, tests)

**Synchronization:**
- Two-way sync: Jira ↔ Git markdown files
- Jira is source of truth for status/assignment
- Git is source of truth for detailed content

### Example Jira Integration Flow
```
Agent creates story markdown → Saves to Git → Creates Jira ticket → Links Git file in ticket

User updates Jira status → Agent detects change → Updates local tracking

User updates story markdown in Git → Agent detects → Syncs description to Jira
```

---

## 10. Cost & Resource Estimates

### LLM API Costs (Monthly, per team of 10)

| Agent | Sessions/Month | Tokens/Session | Cost/Month |
|-------|---------------|----------------|-----------|
| PRD Collaborator | 20 | 50,000 | $50 |
| Architecture Designer | 15 | 40,000 | $30 |
| Epic Decomposer | 10 | 30,000 | $15 |
| Story Author | 100 | 20,000 | $100 |
| Test Planning | 50 | 15,000 | $38 |
| **Total** | | | **~$233/month** |

*(Based on Gemini 1.5 Pro pricing: ~$0.005/1K tokens)*

### Development Effort

| Agent | Complexity | Effort (weeks) |
|-------|-----------|---------------|
| PRD Collaborator | High | 3-4 |
| Architecture Designer | Very High | 4-5 |
| Epic Decomposer | Medium | 2-3 |
| Story Author | High | 3-4 |
| Portfolio Epic Breakdown | Medium | 2 |
| Test Planning | Medium | 2 |
| Infrastructure (Jira, Git, UI) | High | 4 |
| **Total** | | **20-26 weeks** |

**Team Size:** 2-3 engineers

---

## 11. Success Metrics

### Efficiency Metrics
| Metric | Baseline (Manual) | Target (With Agents) | Improvement |
|--------|------------------|---------------------|-------------|
| PRD Creation Time | 4 weeks | 2 weeks | 50% faster |
| Epic Decomposition | 1 week | 2 days | 70% faster |
| Story Authoring (per story) | 2 hours | 45 min | 62% faster |
| Test Plan Creation | 1 hour | 20 min | 67% faster |

### Quality Metrics
- **Completeness:** Stories have all 4 sections (target: 100%)
- **Traceability:** All stories link to PRD/Architecture (target: 100%)
- **Consistency:** Documentation follows templates (target: 95%+)
- **Review Cycles:** Reduce revisions by 40%

### Adoption Metrics
- **Agent Usage Rate:** % of artifacts created with agent help (target: 80%)
- **User Satisfaction:** Survey rating (target: 4.5/5)
- **Time to Proficiency:** New team members productive (target: < 1 week)

---

## 12. Risks & Mitigation

| Risk | Impact | Mitigation |
|------|--------|-----------|
| **Agents produce low-quality output** | High | Human review required, feedback loop for improvement |
| **Users over-rely on agents** | Medium | Training emphasizes "collaborative peer" not "automation" |
| **Jira integration breaks** | High | Fallback to manual Jira entry, agent still useful for docs |
| **LLM API costs exceed budget** | Medium | Token usage monitoring, alerts, rate limiting |
| **Agents can't handle edge cases** | Medium | Always allow manual override/editing |
| **Team rejects agents (change resistance)** | High | Pilot with willing team, show ROI, iterate based on feedback |

---

## 13. Next Steps & Action Items

### For Our Next Working Session

1. **Review this document** - Discuss agent priorities
2. **Decide on implementation approach**:
   - Build custom agents (more control)
   - Use Vertex AI Agent Builder (faster)
   - Hybrid approach
3. **Choose pilot agent** - Which to build first?
   - Recommendation: **PRD Collaborator** (most impactful)
4. **Define MVP scope** - What's minimum viable?
5. **Assign roles** - Who builds what?
6. **Set timeline** - When do we want pilot agent ready?

### Preparation for Next Session
- [ ] Stakeholder buy-in on agent approach
- [ ] Jira API access credentials
- [ ] Git repository structure finalized
- [ ] LLM API quota approved (Gemini/Claude/GPT-4)
- [ ] Example conversational flows drafted
- [ ] UI mockups for agent interface (optional)

---

## 14. Conclusion

This agent suite transforms the AI-Augmented SDLC from a **documentation framework** into an **interactive, collaborative system**. Each agent acts as a specialized peer, guiding teams through complex processes with the consistency of templates and the intelligence of AI.

**Key Advantages:**
- ✅ Faster documentation creation (50-70% time savings)
- ✅ Higher consistency (templates enforced)
- ✅ Better traceability (automatic linking)
- ✅ Easier onboarding (agents teach the framework)
- ✅ Scalable (agents don't burn out)

**The Vision:**
Teams working WITH AI agents to produce high-quality, traceable, AI-ready documentation that enables even faster downstream development with AI coding assistants.

---

**Document Status:** Draft for discussion
**Next Review:** [To be scheduled]
**Feedback:** [To be collected in next session]
