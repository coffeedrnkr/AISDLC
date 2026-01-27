---
title: "Getting Started with the AI-Augmented SDLC"
author: "Implementation Guide"
date: "2025-11-05"
---

# Getting Started with the AI-Augmented SDLC

## 1. Introduction

This guide provides step-by-step instructions for adopting the AI-Augmented SDLC framework in your organization. Whether you're starting a new project or migrating an existing one, this guide will help you implement the framework successfully.

## 2. Prerequisites

Before you begin, ensure you have:

### Technical Prerequisites
- **Version Control:** Git repository (GitHub, GitLab, or Bitbucket)
- **Project Management:** Jira or similar tool for epics/stories
- **Cloud Platform:** Google Cloud Platform account (or equivalent)
- **AI Access:** Access to LLM APIs (Google Gemini, Anthropic Claude, or OpenAI)
- **CI/CD:** Jenkins, GitHub Actions, or Google Cloud Build

### Team Prerequisites
- **Roles Identified:** BA, Architect, Developers, QA Engineers
- **Training Commitment:** 4-8 hours per role for initial training
- **Pilot Project:** One small-to-medium project to start with

### Organizational Prerequisites
- **Executive Sponsorship:** Leadership support for new process
- **Time for Learning:** Accept 10-20% initial productivity dip during adoption
- **Feedback Culture:** Willingness to iterate on the process

---

## 3. Phase 1: Foundation Setup (Week 1-2)

### Step 1: Create the Documentation Structure

Set up your project's documentation repository:

```bash
# Create the core directory structure
mkdir -p docs/{architecture-hub,prompt-hub,design}
mkdir -p docs/architecture-hub/{adrs,api-contracts,data-models,diagrams}
mkdir -p docs/prompt-hub/{prompt-catalog,workflow-designs,personas,evaluation,safety-guardrails}
mkdir -p docs/ux-design/{wireframes,ui-mockups,design-system}

# Copy templates from this repository
cp templates/* docs/
```

### Step 2: Configure Jira or Project Management Tool

1. **Create Custom Fields:**
   - `PRD Link` - Link to PRD section
   - `Architecture Hub Link` - Link to API contracts/data models
   - `Interaction Hub Link` - Link to prompts (if AI-powered feature)
   - `Design Hub Link` - Link to wireframes
   - `AI Collaboration Plan` - Text field for AI instructions

2. **Create Epic Template:**
   - Use the template from `docs/epic-template.md`
   - Add to Jira as default epic description

3. **Create Story Template:**
   - Include all four sections from Story Authoring Guide
   - Make "Context & Links" section required

### Step 3: Set Up AI Agent Access

**Option A: Use Existing AI Coding Assistants**
- Configure Claude Code, GitHub Copilot, or similar
- Create custom instructions based on your framework
- Point AI to documentation locations

**Option B: Build Custom Agents**
- Set up LLM API access (Gemini, Claude, GPT-4)
- Implement agents using your preferred framework (LangChain, etc.)
- Deploy agents as CLI tools, Slack bots, or IDE extensions

**Quick Start (No Custom Agents):**
For initial adoption, you can use standard AI coding assistants with clear instructions pointing to your documentation. Custom agent development can come later.

---

## 4. Phase 2: First Project Setup (Week 2-3)

### Step 1: Choose Your Pilot Project

**Good pilot project characteristics:**
- Small to medium size (3-6 month timeline)
- Clear business value
- Supportive stakeholders
- Mix of new development and existing system integration
- Not mission-critical (room for learning)

**Bad pilot project characteristics:**
- Emergency/high-pressure project
- Unclear requirements
- Requires extensive legacy system knowledge
- Politically sensitive

### Step 2: Create Your First PRD

Work with your BA to create the project's PRD:

1. **Start with the PRD Guide:** Review `docs/prd-guide.md`
2. **Fill in Key Sections:**
   - Business Intent & Objectives (the "why")
   - Functional Envelope (the "what")
   - Scope Boundaries (in/out/TBD)
   - System Impact & Integrations
   - Architectural Sketch
3. **Review with Stakeholders:** Get alignment before proceeding
4. **Store in Documentation:** `docs/prd.md` in version control

**Time estimate:** 1-2 days for BA + stakeholders

### Step 3: Build the Architecture Hub

Work with your Solution Architect:

1. **Create System Diagrams:**
   - Start with C4 Context diagram (highest level)
   - Add Container diagram showing major components
   - Store as Mermaid files in `docs/architecture-hub/diagrams/`

2. **Define API Contracts:**
   - Use OpenAPI template for REST APIs
   - Define all endpoints this project will create
   - Store in `docs/architecture-hub/api-contracts/`

3. **Define Data Models:**
   - Create SQL schemas for new tables
   - Document Firestore collections if using NoSQL
   - Store in `docs/architecture-hub/data-models/`

4. **Document Key Decisions:**
   - Create ADRs for major architectural choices
   - Use the ADR template
   - Store in `docs/architecture-hub/adrs/`

**Time estimate:** 2-3 days for Architect

### Step 4: Build the Interaction Hub (If AI-Powered Features)

If your project includes AI-powered features:

1. **Define AI Persona:** What's the tone/style of the AI?
2. **Create Prompt Catalog Entries:** One per major AI interaction
3. **Map Agentic Workflows:** Flowcharts for multi-step AI behaviors
4. **Define Evaluation Criteria:** How will you measure AI quality?

**Time estimate:** 1-2 days for AI Interaction Designer

**Skip if:** Your project doesn't include user-facing AI features

### Step 5: Build the Design Hub

Work with your UX Designer:

1. **Create Wireframes:** Low-fidelity sketches of key screens
2. **Document Design System:** Colors, typography, components
3. **Link to Stories:** Ensure each wireframe is linked to future stories

**Time estimate:** 2-3 days for Designer

---

## 5. Phase 3: Epic and Story Creation (Week 3-4)

### Step 1: Decompose PRD into Epics

**With `Agent: Decompose-Epics` (If Available):**
1. Point agent to PRD and Architecture Hub
2. Review agent's proposed epics
3. Refine and approve each epic
4. Agent creates epics in Jira with traceability links

**Without Agent (Manual Process):**
1. Review PRD's "Functional Envelope"
2. Create 3-7 Business Epics (one per major capability)
3. Review Architecture Hub's components
4. Create 2-4 Enabler Epics (infrastructure/services needed)
5. Create each epic in Jira using epic template
6. Manually add traceability links to PRD sections

**Time estimate:** 1 day for BA + Tech Lead

### Step 2: Create AI-Ready Stories for First Sprint

**With `Agent: Write-Stories` (If Available):**
1. Select 2-3 epics for first sprint
2. Point agent to each epic
3. Review agent's draft stories
4. Fill in Technical Implementation Plans
5. Add AI Collaboration Plans

**Without Agent (Manual Process):**
1. For each epic, identify user journey steps
2. Create story for each step using story template
3. Fill in all four required sections:
   - Context & Links (most critical!)
   - Gherkin Acceptance Criteria
   - Technical Implementation Plan
   - AI Collaboration Plan
4. Review with team to ensure vertical slicing

**Key Success Criteria for Stories:**
- Every story has links to PRD, Architecture Hub, Design Hub
- Gherkin AC is specific and measurable
- Story is vertically sliced (UI → API → DB)
- AI Collaboration Plan is clear and actionable

**Time estimate:** 2-3 days for first sprint's stories

---

## 6. Phase 4: Development Sprint (Week 4-6)

### Step 1: Sprint Planning with AI-Ready Stories

In your sprint planning meeting:

1. **Review Stories:** Team reviews AI-Ready Stories
2. **Estimate:** Team estimates effort (AI assistance reduces boilerplate time)
3. **Commit:** Team commits to realistic sprint goal
4. **Identify Risks:** Call out any missing context or unclear requirements

### Step 2: Development with AI Assistance

For each story, developers:

1. **Read Full Context:** Review all linked documents (PRD, Architecture, Design)
2. **Follow AI Collaboration Plan:** Use AI assistant as specified in story
3. **Generate Boilerplate:** Let AI create API endpoints, data access, UI scaffolding
4. **Implement Business Logic:** Developer writes complex/novel logic
5. **Review & Refine:** Don't blindly accept AI code—review and improve

**Example Developer Workflow:**
```bash
# 1. Read the story and all linked documents
open docs/prd.md
open docs/architecture-hub/api-contracts/user-service-api.yaml
open docs/design/wireframes/user-profile.png

# 2. Use AI to generate boilerplate
# "Generate a React component for user profile that calls GET /api/users/{id}"

# 3. Review AI-generated code
# 4. Implement complex business logic manually
# 5. Run tests

# 6. Commit with reference to story
git commit -m "Implement user profile view - PROJ-123"
```

### Step 3: Testing with AI Assistance

For each story, QA engineers:

1. **Read Gherkin AC:** These are your test cases
2. **Generate Test Stubs:** Use `Agent: Generate-Tests` or manual Playwright setup
3. **Implement Test Steps:** Write step definitions
4. **Execute Tests:** Run in local/ephemeral environments
5. **Report Results:** Link test results to story in Jira

### Step 4: Code Review with Context

Reviewers have access to full context:

1. **Check Story Completion:** Does code implement all Gherkin AC?
2. **Verify Architecture Compliance:** Does it match API contracts?
3. **Review AI-Generated Code:** Is it production-quality?
4. **Check Test Coverage:** Are all AC covered by tests?

---

## 7. Phase 5: Continuous Improvement (Ongoing)

### Week 6-8: First Retrospective

After your first sprint or two:

1. **What Worked Well:**
   - Which parts of the framework helped?
   - Where did AI assistance save time?
   - What documentation was most valuable?

2. **What Didn't Work:**
   - Where was documentation unclear?
   - Where did AI produce poor results?
   - What slowed the team down?

3. **Action Items:**
   - Update templates based on learnings
   - Add missing documentation
   - Refine AI collaboration patterns

### Ongoing: Metrics and Measurement

Track these metrics to measure framework adoption impact:

| Metric | Baseline | Target | Current |
|--------|----------|--------|---------|
| Story cycle time | ? | -30% | ? |
| Test coverage | ? | >80% | ? |
| Production defects | ? | -50% | ? |
| Time spent on boilerplate | ? | -60% | ? |
| Developer satisfaction | ? | +20% | ? |

### Scaling Beyond the Pilot

Once pilot succeeds:

1. **Document Lessons Learned:** Update guides with team insights
2. **Train Additional Teams:** Use pilot team as champions
3. **Build Custom Agents:** If needed, invest in specialized agents
4. **Standardize Across Organization:** Make framework the default

---

## 8. Common Pitfalls and How to Avoid Them

### Pitfall 1: "Too Much Documentation"
**Symptom:** Team spends more time documenting than coding
**Solution:** Start minimal—PRD + Architecture Hub only. Add other hubs as needed.

### Pitfall 2: "AI Generated Bad Code"
**Symptom:** AI produces low-quality or incorrect code
**Solution:** Ensure stories have complete context links. Don't skip the "Context & Links" section.

### Pitfall 3: "Documentation Gets Stale"
**Symptom:** Docs don't reflect reality after a few sprints
**Solution:** Make doc updates part of Definition of Done. Review quarterly.

### Pitfall 4: "Team Resists Change"
**Symptom:** Team sees framework as bureaucracy
**Solution:** Show value quickly with pilot. Gather feedback. Iterate based on team input.

### Pitfall 5: "Over-Reliance on AI"
**Symptom:** Developers stop thinking critically
**Solution:** Emphasize AI as assistant, not replacement. Code review catches issues.

---

## 9. Quick Reference: Minimum Viable Implementation

**If you need to start even faster, here's the absolute minimum:**

### Week 1:
- ✅ Create `docs/prd.md` for your project
- ✅ Create `docs/architecture-hub/api-contracts/` with OpenAPI specs
- ✅ Add "Context & Links" section to your Jira story template

### Week 2:
- ✅ Create 3-5 epics linked to PRD sections
- ✅ Create 5-8 stories with full context links for first sprint

### Week 3-4:
- ✅ Run first sprint using AI-Ready Stories
- ✅ Have developers use AI assistants with context links

### Week 5:
- ✅ Retrospective: What worked? What needs improvement?
- ✅ Iterate on templates and process

**Everything else can be added incrementally as needed.**

---

## 10. Resources and Support

### Documentation Library
- [AI-Augmented SDLC Vision](00_Introduction/the-ai-augmented-sdlc-vision.md)
- [PRD Guide](01_Requirements/prd-guide.md)
- [Epic Crafting Guide](02_Elaboration/epic-crafting-guide.md)
- [Story Authoring Guide](02_Elaboration/story-authoring-guide.md)
- [UX Architect Framework](03_UX_Design/ux-architect-framework.md)
- [Architecture Hub Guide](04_Architecture/architecture-hub-guide.md)
- [Developer Playbook](05_Implementation/developer-playbook.md)
- [Quality & Testing Strategy](06_Testing/quality-and-testing-strategy-guide.md)
- [DevOps & CI/CD Strategy](00_Introduction/devops-and-cicd-strategy-guide.md)

### Templates
- [Epic Template](epic-template.md)
- [ADR Template](architecture-hub/adrs/adr-template.md)
- [OpenAPI Template](architecture-hub/api-contracts/openapi-template.yaml)
- [Prompt Template](prompt-hub/prompt-catalog/prompt-template.md)

### Need Help?
- **Internal Support:** [Add your team's Slack channel or email]
- **Framework Updates:** [Link to changelog or update process]
- **Feedback:** [How to submit feedback on the framework]

---

## 11. Success Stories

*(To be populated as teams adopt the framework)*

**Team Name | Project | Key Metric**
- Team Alpha | User Profile Redesign | 40% reduction in story cycle time
- Team Beta | Payment Service | 95% test coverage (up from 65%)
- Team Gamma | AI Chatbot | Zero production incidents in first 3 months

---

## Conclusion

Adopting the AI-Augmented SDLC is a journey, not a destination. Start small, measure impact, gather feedback, and iterate. The framework is designed to evolve with your team's needs.

**Remember:** The goal is not perfect documentation—it's enabling human-AI collaboration to deliver better software faster.

Good luck with your implementation! 🚀
