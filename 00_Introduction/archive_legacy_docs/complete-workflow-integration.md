# Complete Workflow Integration
## Business Analyst → Developer → Tester with AI Agents

**Version:** 1.2
**Last Updated:** 2025-12-20
**Status:** Integrated Workflow with Governance & Release Gates

---

## Document Updates (December 2025)

This document has been updated with the latest December 2025 releases:
- ✅ **Gemini 3 Flash** (released Dec 17, 2025) - 3x faster, PhD-level reasoning
- ✅ **Gemini 2.5 Pro** - Now with 2M token context window
- ✅ **Google Antigravity** (released Nov 20, 2025) - Agentic development platform
- ✅ **NotebookLM Enterprise API** (documented Dec 17, 2025) - Programmatic access
- ✅ **Playwright MCP** - Microsoft's official Model Context Protocol server
- ✅ **Gemini Live API** - General availability on Vertex AI

**Enterprise Note:** All Google services (NotebookLM Enterprise, Vertex AI, Gemini models)
are included with Gemini Enterprise subscription.

---

## Overview

This document describes the complete, integrated workflow from requirements gathering through testing, optimized for your specific toolstack:

**Tools:**
- **Jira** - Project management, epics, stories
- **Confluence** - Design patterns, code quality guidelines, architecture documentation
- **Google Workspace** - NotebookLM, Docs, Drive
- **VS Code** - Development environment
- **Google Antigravity** - AI-powered testing
- **Playwright** - Test automation

**Workflow:**
```
Business Analyst (20+ docs) → PRD Agent → PRD
                                        ↓
Architecture Agent → Architecture Hub → Confluence
                                        ↓
Epic/Story Agents → Jira Epics/Stories
                                        ↓
Developer (VS Code) ← Jira + Confluence + AI Coding Agent
                                        ↓
Code Governance Agent (Local) → Report.md
                                        ↓
Test Agent + Antigravity + Playwright → Automated Tests
                                        ↓
Integration Agent (CI/CD) → Release Readiness Report → Deployment
```

---

## Part 1: Business Analyst Workflow (PRD Creation)

### Challenge: Synthesizing 20+ Documents

**Typical BA Scenario:**
```
Inputs (20-30 documents):
├── 5 stakeholder presentations (PowerPoint)
├── 3 business cases (PDFs)
├── 8 meeting transcripts
├── 6 email threads
├── 4 user research reports
├── 2 competitive analyses
└── 3 regulatory/compliance documents
```

**Problem:** Too many documents for simple AI prompting
- Gemini 2.5 Pro: 2M token limit ≈ 20-25 large documents
- Gemini 3 Flash (Dec 2025): 1M token limit, but 3x faster and cheaper
- Need careful memory management
- Must maintain source references
- Risk of information loss
- Even with large context, quality degrades with too many unstructured inputs

### Solution: Multi-Stage PRD Generation with NotebookLM

#### Architecture

```
┌──────────────────────────────────────────────────────────┐
│  Stage 1: NotebookLM Pre-Processing                     │
│  (BA-Driven Exploration)                                 │
└─────────────────────┬────────────────────────────────────┘
                      │
        ┌─────────────┴─────────────┐
        ↓                           ↓
  ┌─────────────┐           ┌─────────────┐
  │ NotebookLM  │           │ NotebookLM  │
  │ Notebook 1  │           │ Notebook 2  │
  │             │           │             │
  │ Business    │           │ Technical   │
  │ Docs (15)   │           │ Docs (10)   │
  └──────┬──────┘           └──────┬──────┘
         │                         │
         └────────────┬────────────┘
                      ↓
┌──────────────────────────────────────────────────────────┐
│  Stage 2: PRD Agent Synthesis                            │
│  (AI-Driven Structuring)                                 │
└─────────────────────┬────────────────────────────────────┘
                      ↓
             ┌────────────────┐
             │  Complete PRD  │
             │  with Source   │
             │  Citations     │
             └────────────────┘
```

#### Stage 1: NotebookLM Pre-Processing

**BA Actions:**

**Step 1: Organize Documents into Notebooks**
```
NotebookLM Notebook 1: "Business Context"
├── Upload: Stakeholder presentations (5)
├── Upload: Business cases (3)
├── Upload: Meeting transcripts (8)
└── Total: 16 sources

NotebookLM Notebook 2: "Technical & Research"
├── Upload: User research reports (4)
├── Upload: Competitive analyses (2)
├── Upload: Regulatory docs (3)
├── Upload: Email threads (6)
└── Total: 15 sources
```

**Why split?** NotebookLM performs better with thematically grouped sources.

**Step 2: Ask NotebookLM Exploratory Questions**

**Business Notebook Questions:**
```
BA: "What are the top 10 features mentioned across all stakeholder presentations?"

NotebookLM Response:
Based on the presentations, here are the top features:
1. Single Sign-On (SSO) - Mentioned in Stakeholder Deck 1, 3, and 5
2. Role-Based Access Control - Deck 2, 4, 5
3. Dashboard with KPIs - All 5 decks
4. Mobile app - Deck 1, 2 (conflict: Deck 3 says web-only)
5. ...

[With citations for each]
```

```
BA: "Are there any conflicting requirements across the business cases?"

NotebookLM Response:
Yes, I found 2 major conflicts:
1. Budget: Business Case 1 says $500K, Business Case 2 says $750K
   [Source: BC1 page 12, BC2 page 8]
2. Timeline: BC1 targets 6 months, Meeting Transcript #4 mentions
   9 months as "realistic"
   [Source: BC1 page 15, MT4 timestamp 12:34]
```

```
BA: "Create a timeline of how requirements evolved"

NotebookLM Response: [Generates timeline visualization]
- Jan 2025: Initial concept (Deck 1) - Focus on reporting
- Feb 2025: Expanded scope (Deck 2) - Added mobile
- Mar 2025: Revised (Meeting #3) - Mobile deprioritized to v2
- Apr 2025: Business case (BC1) - Formalized budget/timeline
```

**Step 3: Export NotebookLM Artifacts**

NotebookLM generates:
- ✅ **Summary** - 2-page executive summary of all sources
- ✅ **FAQ** - Frequently asked questions across sources
- ✅ **Study Guide** - Key concepts and definitions
- ✅ **Timeline** - Chronological evolution
- ✅ **Source Citations** - Every fact linked to source

BA exports these to markdown files:
```
/notebooklm-artifacts/
├── business-context-summary.md
├── business-context-faq.md
├── technical-research-summary.md
├── conflicts-identified.md
└── timeline.md
```

#### Stage 2: PRD Agent Synthesis

**Inputs to PRD Agent:**
1. NotebookLM summaries (pre-synthesized, 5 files ≈ 50K tokens)
2. PRD template
3. Critical source documents (top 5-10 most important)
4. Conflict resolution from BA

**PRD Agent Process:**

**Step 1: Analyze Pre-Synthesized Content**
```python
# PRD Agent reads NotebookLM artifacts
business_summary = read("business-context-summary.md")
technical_summary = read("technical-research-summary.md")
conflicts = read("conflicts-identified.md")
timeline = read("timeline.md")

# PRD Agent has pre-digested content with citations
# Much smaller context than raw 25 documents
```

**Step 2: Map to PRD Template**
```
PRD Agent prompt:
"You are creating a PRD from pre-analyzed sources.

NOTEBOOKLM BUSINESS SUMMARY:
{business_summary with citations}

NOTEBOOKLM TECHNICAL SUMMARY:
{technical_summary with citations}

IDENTIFIED CONFLICTS:
{conflicts that need resolution}

PRD TEMPLATE:
{template structure}

Map the pre-synthesized content to the PRD template. For each section:
1. Use information from summaries
2. Maintain source citations [Source: Document X, Page Y]
3. Flag any gaps where information is missing
4. Highlight conflicts that need BA decision

Generate PRD draft with:
- All citations preserved
- Gaps clearly marked
- Conflicts flagged for resolution
```

**Step 3: Iterative Gap Filling**

```
PRD Agent: "I've generated a PRD draft with 85% completeness. Remaining gaps:

⚠️ Section 5.2: Success Metrics - Business case mentions ROI but no specific KPIs
   Questions:
   - What metrics will measure user engagement?
   - What's the target for support ticket reduction?
   - CSAT target?

⚠️ Section 6.3: Non-Functional Requirements - Performance not discussed
   Questions:
   - What's acceptable page load time?
   - Concurrent user target?
   - API response time SLA?

Would you like to address these now or mark as TODO?"

BA: "DAU +30%, support tickets -20%, CSAT 4.5/5. Page load <2s, 10K concurrent users, API <500ms p95."

PRD Agent: "✓ Added metrics and NFRs with your specifications. PRD now 98% complete."
```

**Step 4: Final PRD with Full Traceability**

```markdown
# Product Requirements Document: Customer Portal

## 2. Business Objectives

### 2.1 Primary Objectives
1. **Increase user engagement by 30%**
   - Source: [Business Case 1, p.5; Stakeholder Deck 3, slide 12]
   - Timeline: Within 6 months of launch

2. **Reduce support ticket volume by 20%**
   - Source: [Meeting Transcript #4, 15:32; Business Case 2, p.8]
   - Current volume: 500 tickets/month
   - Target: 400 tickets/month

### 2.2 Success Metrics
| Metric | Baseline | Target | Timeframe | Source |
|--------|----------|--------|-----------|--------|
| DAU | 15,000 | 19,500 (+30%) | 6 months | [BC1 p.12] |
| Support Tickets | 500/mo | 400/mo (-20%) | 3 months | [MT#4, BC2] |
| CSAT | 3.8/5.0 | 4.5/5.0 | Launch | BA input |

...
```

### Benefits of This Approach

**vs. Direct 25-Document Processing:**

| Approach | Context Size | Source Citations | Conflict Detection | BA Control |
|----------|--------------|------------------|-------------------|------------|
| **Direct** | 500K-1M tokens | Difficult to maintain | AI may miss | Low |
| **NotebookLM + Agent** | 50-100K tokens | Preserved throughout | BA-validated | High |

**Key Advantages:**
- ✅ **Manageable context** - PRD Agent works with summaries, not raw docs
- ✅ **Source citations** - Every statement traces to source document
- ✅ **BA control** - BA explores docs first, validates conflicts
- ✅ **Better quality** - Pre-synthesis reduces hallucination risk
- ✅ **Faster iteration** - Smaller context = faster agent responses

### Implementation: PRD Agent with NotebookLM Integration

**Technology Stack:**
```
NotebookLM Enterprise (Google) - Document ingestion and pre-synthesis
    ↓
Cloud Function - Exports NotebookLM artifacts (or manual export)
    ↓
PRD Agent (Vertex AI Gemini 3 Flash or 2.5 Pro) - Structures into PRD
    ↓
Git Repository (docs/PRD.md) - Version control
    ↓
Confluence - Stakeholder access
```

NOTE: With Gemini Enterprise, all tools (NotebookLM Enterprise, Vertex AI,
Gemini models) are included. Gemini 3 Flash (released Dec 17, 2025) offers
PhD-level reasoning with 3x speed improvement over 2.5 Pro.

**PRD Agent Code Pattern:**
```python
# /services/prd-agent/main.py

class PRDAgentWithNotebookLM:
    def __init__(self):
        # Use Gemini 3 Flash (Dec 2025) for speed, or 2.5 Pro for max context
        self.model = GenerativeModel("gemini-3-flash")  # or "gemini-2.5-pro"
        self.storage_client = storage.Client()

    async def generate_prd_from_notebooklm(
        self,
        notebooklm_artifacts: List[str],
        prd_template: str,
        source_documents: Optional[List[str]] = None
    ) -> Dict:
        """
        Generate PRD from NotebookLM pre-synthesized artifacts.

        Args:
            notebooklm_artifacts: List of paths to NotebookLM exports
                - business-summary.md
                - technical-summary.md
                - conflicts.md
                - timeline.md
            prd_template: PRD template structure
            source_documents: Optional list of critical source docs to reference

        Returns:
            Generated PRD with citations
        """

        # Step 1: Load NotebookLM artifacts (small context)
        artifacts = {}
        for artifact_path in notebooklm_artifacts:
            content = self._load_from_storage(artifact_path)
            artifacts[artifact_path] = content

        # Step 2: Optionally load critical source documents
        critical_sources = {}
        if source_documents:
            for doc_path in source_documents[:5]:  # Limit to top 5
                critical_sources[doc_path] = self._load_document(doc_path)

        # Step 3: Generate PRD with maintained citations
        prompt = self._build_prd_prompt(
            artifacts=artifacts,
            critical_sources=critical_sources,
            template=prd_template
        )

        # Gemini 3 Flash (Dec 2025) or 2.5 Pro - using pre-synthesized input
        # Gemini 3 Flash: 3x faster, PhD-level reasoning, $0.50/1M tokens
        response = self.model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.2,  # Low temp for factual synthesis
                "max_output_tokens": 8192
            }
        )

        prd_content = response.text

        # Step 4: Extract gaps and conflicts that need resolution
        gaps = self._identify_gaps(prd_content, prd_template)

        return {
            "prd": prd_content,
            "gaps": gaps,
            "coverage_score": self._calculate_coverage(prd_content, prd_template),
            "citations_count": self._count_citations(prd_content)
        }

    def _build_prd_prompt(self, artifacts, critical_sources, template):
        """Build prompt with NotebookLM artifacts and citations."""
        return f"""
You are generating a Product Requirements Document from pre-analyzed sources.

NOTEBOOKLM SUMMARIES (Pre-synthesized by NotebookLM):

Business Context Summary:
{artifacts['business-summary.md']}

Technical & Research Summary:
{artifacts['technical-summary.md']}

Identified Conflicts:
{artifacts['conflicts.md']}

Timeline of Requirements Evolution:
{artifacts['timeline.md']}

CRITICAL SOURCE DOCUMENTS (for additional context):
{self._format_critical_sources(critical_sources)}

PRD TEMPLATE:
{template}

INSTRUCTIONS:
1. Map pre-synthesized content to PRD template sections
2. PRESERVE ALL SOURCE CITATIONS from NotebookLM summaries
   Format: [Source: Document Name, Page/Location]
3. Identify gaps where information is missing
4. Flag conflicts that need human resolution
5. Generate complete PRD in markdown format

IMPORTANT: NotebookLM has already validated these summaries against
25+ source documents. Trust the summaries but maintain all citations.

Generate the PRD now:
"""
```

### Reference: NotebookLM Citation Format

NotebookLM automatically maintains citations like:
```
"The system must support SSO authentication" [Source: Stakeholder Deck 1, Slide 8]
"Budget approved at $750K" [Source: Business Case 2, Page 12]
"Mobile app deprioritized to v2" [Source: Meeting Transcript #4, 15:32]
```

PRD Agent preserves these in final PRD, ensuring full traceability.

---

## Part 2: Developer Workflow (VS Code Integration)

### The Developer's Environment

**What Developers Need:**
1. **Epics/Stories from Jira** - What to build
2. **Architecture docs from Confluence** - How to build
3. **Design patterns from Confluence** - Best practices
4. **Code quality guidelines from Confluence** - Standards
5. **AI coding assistant** - Implementation help

### Architecture: VS Code as Central Hub

```
┌──────────────────────────────────────────────────────────┐
│                    VS Code IDE                           │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │  Editor                                            │ │
│  │  - Code files                                      │ │
│  │  - Gemini Code Assist (inline)                    │ │
│  │  - GitHub Copilot (if preferred)                  │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │  Sidebar: Jira Extension                          │ │
│  │  - View assigned epics/stories                     │ │
│  │  - Pull epic details                               │ │
│  │  - Update story status                             │ │
│  │  - Add work logs                                   │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │  Sidebar: Confluence Extension                     │ │
│  │  - Search design patterns                          │ │
│  │  - View code quality guidelines                    │ │
│  │  - Access architecture docs                        │ │
│  │  - Quick reference lookup                          │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │  Sidebar: Git/GitHub                               │ │
│  │  - Commits, branches, PRs                          │ │
│  └────────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

### Recommended VS Code Extensions

**1. Jira Integration**
```
Extension: "Jira and Bitbucket (Official)"
Publisher: Atlassian
Features:
- View Jira issues in sidebar
- Create branches from issues
- Transition issue status
- Add work logs
- Smart commits (auto-link commits to issues)
```

**2. Confluence Integration**
```
Extension: "Confluence Viewer" or build custom MCP server
Features:
- Search Confluence from VS Code
- View pages in sidebar
- Quick access to design patterns
- Code quality guidelines lookup
```

**3. AI Coding Assistants**
```
Primary: Gemini Code Assist (recommended for your Google stack)
- Inline completions
- Chat interface
- Context-aware suggestions
- Understands your codebase

Alternative: GitHub Copilot
- If team prefers
- Excellent code completion
```

### Developer Workflow: From Epic to Code

**Step 1: Pull Epic from Jira**

Developer in VS Code:
```
1. Open Jira sidebar
2. Filter: "Assigned to Me" + "Status: To Do"
3. Click epic: "Epic 003: User Dashboard"
4. VS Code displays:
   ┌─────────────────────────────────────────────┐
   │ Epic 003: User Dashboard                    │
   │                                             │
   │ Description:                                │
   │ Build user dashboard with KPIs, charts,    │
   │ and activity feed.                          │
   │                                             │
   │ Stories in this Epic:                       │
   │ ☐ PROJ-45: Dashboard layout                │
   │ ☐ PROJ-46: KPI widgets                     │
   │ ☐ PROJ-47: Activity feed                   │
   │ ☐ PROJ-48: Chart components                │
   │                                             │
   │ Architecture Reference:                     │
   │ See: Confluence/Architecture/Dashboard      │
   │                                             │
   │ [View in Jira] [Create Branch]             │
   └─────────────────────────────────────────────┘
```

**Step 2: Access Architecture from Confluence**

Developer clicks "Architecture Reference" link:
```
VS Code opens Confluence sidebar:

┌─────────────────────────────────────────────┐
│ Confluence: Dashboard Architecture          │
│                                             │
│ Component Structure:                        │
│ src/components/Dashboard/                   │
│ ├── Dashboard.tsx (container)              │
│ ├── KPIWidget.tsx                          │
│ ├── ActivityFeed.tsx                       │
│ └── ChartComponent.tsx                     │
│                                             │
│ State Management:                           │
│ - Use React Context for dashboard state    │
│ - Redux for KPI data caching                │
│                                             │
│ Design Patterns:                            │
│ - Compound component pattern for widgets   │
│ - Observer pattern for real-time updates   │
│                                             │
│ API Endpoints:                              │
│ GET /api/dashboard/kpis                    │
│ GET /api/dashboard/activity                │
│                                             │
│ [Open Full Page] [Search Patterns]         │
└─────────────────────────────────────────────┘
```

**Step 3: Reference Code Quality Guidelines**

Developer types Command+Shift+P → "Search Confluence: code quality"
```
┌─────────────────────────────────────────────┐
│ Search Results: "code quality"              │
│                                             │
│ 1. Code Quality Guidelines - React          │
│    • Use TypeScript for all components     │
│    • Props must have interfaces            │
│    • Test coverage >80%                    │
│    • ESLint rules must pass                │
│                                             │
│ 2. Design Patterns - Component Architecture│
│    • Compound components for flexibility   │
│    • Custom hooks for logic reuse          │
│    • Atomic design principles              │
│                                             │
│ 3. API Best Practices                       │
│    • Use React Query for data fetching     │
│    • Error boundaries for fault tolerance  │
│                                             │
│ [View Page 1] [View Page 2] [View Page 3]  │
└─────────────────────────────────────────────┘
```

**Step 4: Implement with AI Coding Assistant**

Developer starts coding with Gemini Code Assist:
```typescript
// src/components/Dashboard/Dashboard.tsx

// Developer types comment:
// Create a dashboard component following our architecture

// Gemini Code Assist (inline suggestion):
import React, { useState, useEffect } from 'react';
import { KPIWidget } from './KPIWidget';
import { ActivityFeed } from './ActivityFeed';
import { ChartComponent } from './ChartComponent';
import { useDashboardData } from '@/hooks/useDashboardData';

interface DashboardProps {
  userId: string;
}

export const Dashboard: React.FC<DashboardProps> = ({ userId }) => {
  const { kpis, activity, loading, error } = useDashboardData(userId);

  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorBoundary error={error} />;

  return (
    <div className="dashboard-container">
      <header>
        <h1>Dashboard</h1>
      </header>

      <div className="dashboard-grid">
        <KPIWidget data={kpis} />
        <ChartComponent data={kpis.trends} />
        <ActivityFeed activities={activity} />
      </div>
    </div>
  );
};
```

**Gemini Code Assist context includes:**
- ✅ Current file and related files in project
- ✅ Git history (recent commits, PRs)
- ✅ Jira epic/story description (via extension)
- ✅ Architecture docs (if integrated via MCP)

**Step 5: Update Jira as You Work**

Developer in VS Code:
```
1. Start story: Click "PROJ-45" in Jira sidebar → "Start Progress"
2. Code implementation
3. Commit with smart commit message:
   "PROJ-45: Implement dashboard layout

   - Created Dashboard.tsx with grid layout
   - Added KPI widget placeholder
   - Integrated with useDashboardData hook

   Follows architecture from Confluence/Dashboard
   "
4. Jira automatically:
   - Links commit to PROJ-45
   - Adds work log
   - Updates story with commit details
```

### Enhanced Developer Workflow with MCP Integration

**Model Context Protocol (MCP)** allows AI coding assistants to access external context:

#### Confluence MCP Server

**What it enables:**
```python
# Custom MCP Server for Confluence

@mcp.tool()
def search_design_patterns(query: str) -> str:
    """Search Confluence for design patterns."""
    results = confluence_api.search(query, space="DESIGN")
    return format_results(results)

@mcp.tool()
def get_code_quality_guidelines(language: str) -> str:
    """Get code quality guidelines for a language."""
    page = confluence_api.get_page(f"Code Quality - {language}")
    return page.content

@mcp.tool()
def get_architecture_doc(component: str) -> str:
    """Get architecture documentation for a component."""
    page = confluence_api.get_page(f"Architecture - {component}")
    return page.content
```

**Developer workflow with MCP:**
```
Developer in VS Code:
"@gemini I need to implement the dashboard. Show me the architecture."

Gemini Code Assist:
[Calls MCP: get_architecture_doc("Dashboard")]
[Receives Confluence page content]

"Based on the architecture documentation in Confluence, here's the recommended structure:

[Shows architecture from Confluence]

I'll generate the component following these patterns:
[Generates code matching architecture]
"
```

**Benefits:**
- ✅ AI assistant has access to Confluence knowledge
- ✅ No manual copying of docs
- ✅ Always references latest guidelines
- ✅ Enforces organizational standards

#### Jira MCP Server

**What it enables:**
```python
@mcp.tool()
def get_current_story_details() -> dict:
    """Get details of currently selected Jira story."""
    return jira_api.get_issue(current_issue_key)

@mcp.tool()
def get_epic_acceptance_criteria(epic_key: str) -> list:
    """Get acceptance criteria for an epic."""
    epic = jira_api.get_epic(epic_key)
    return epic.acceptance_criteria

@mcp.tool()
def get_related_stories(story_key: str) -> list:
    """Get related stories (dependencies, sub-tasks)."""
    return jira_api.get_related_issues(story_key)
```

**Developer workflow with MCP:**
```
Developer: "@gemini What are the acceptance criteria for this story?"

Gemini:
[Calls MCP: get_current_story_details()]
[Gets PROJ-45 details from Jira]

"For story PROJ-45 'Dashboard layout', the acceptance criteria are:
1. Dashboard displays in responsive grid layout
2. Grid adapts to mobile, tablet, desktop breakpoints
3. Loading state shows spinner
4. Error state shows friendly error message
5. KPI widgets load data from API

I'll implement each of these. Let me start with the grid layout..."
```

### Summary: Developer's Integrated Environment

```
VS Code (Single Interface)
├── Code Editor
│   └── Gemini Code Assist (inline suggestions + chat)
│       ├── Understands codebase
│       ├── MCP → Jira (story details, acceptance criteria)
│       └── MCP → Confluence (architecture, patterns, guidelines)
├── Jira Extension (Sidebar)
│   ├── View assigned stories
│   ├── Pull epic/story details
│   ├── Update status
│   └── Smart commits
├── Confluence Extension (Sidebar)
│   ├── Search documentation
│   ├── View pages
│   └── Quick reference
└── Git/GitHub (Built-in)
    ├── Commits linked to Jira
    └── PRs with story context
```

**Step 6: Automated Governance Check**

Before pushing to CI/CD, the developer runs the Code Governance Agent locally to ensure their code meets organizational standards.

```bash
# Developer runs agent in terminal
python3 code_governance_agent/main.py --target ./src/components/Dashboard

# Output:
# [INFO] Running Static Analysis (Ruff, Bandit)...
# [INFO] Running AI Strategic Review (Gemini 3 Flash)...
# [SUCCESS] No critical issues found.
# Report generated: CodeGovernanceReport.md
```

**Everything developers need in one place:**
- ✅ **What to build** - Jira stories
- ✅ **How to build** - Confluence architecture
- ✅ **Standards to follow** - Confluence guidelines
- ✅ **Quality Check** - Governance Agent
- ✅ **AI assistance** - Gemini Code Assist with full context

---

## Part 3: Testing Workflow (Google Antigravity + Playwright)

**Latest Information (December 2025):**
- **Google Antigravity** - Released November 20, 2025 as Google's free agentic development platform
- **Browser Integration** - Chrome extension enables autonomous testing, UI interaction, and verification
- **Playwright MCP** - Microsoft's official Model Context Protocol server for self-healing tests
- **Gemini 3 Integration** - Antigravity now uses Gemini 3 models for improved reasoning

### The Testing Challenge

**Traditional Testing:**
- QA writes test cases manually (days/weeks)
- Developers write Playwright scripts manually
- Tests break when UI changes (maintenance burden)
- Coverage gaps (edge cases missed)

**AI-Augmented Testing Goals:**
1. Auto-generate test cases from requirements
2. Auto-generate Playwright scripts
3. Execute tests automatically
4. Self-healing tests (adapt to UI changes)

### Solution: Google Antigravity + Playwright MCP

#### Architecture

```
┌──────────────────────────────────────────────────────────┐
│              Requirements (Input)                        │
│  • User Stories (from Jira)                              │
│  • Acceptance Criteria                                   │
│  • Architecture Docs                                     │
└─────────────────────┬────────────────────────────────────┘
                      │
                      ↓
┌──────────────────────────────────────────────────────────┐
│         Test Plan Agent (Vertex AI)                      │
│  Generates:                                              │
│  • Test cases (what to test)                             │
│  • Test scenarios (happy path, edge cases, errors)       │
│  • Test data (inputs, expected outputs)                  │
└─────────────────────┬────────────────────────────────────┘
                      │
                      ↓
┌──────────────────────────────────────────────────────────┐
│       Google Antigravity (Test Implementation)           │
│  • Reads test cases                                      │
│  • Generates Playwright scripts                          │
│  • Executes tests in browser                             │
│  • Records video of test execution                       │
│  • Captures screenshots                                  │
│  • Auto-fixes simple failures                            │
└─────────────────────┬────────────────────────────────────┘
                      │
                      ↓
┌──────────────────────────────────────────────────────────┐
│           Test Results & Artifacts                       │
│  • Pass/Fail status                                      │
│  • Video recordings                                      │
│  • Screenshots                                           │
│  • Execution logs                                        │
│  • Coverage report                                       │
└──────────────────────────────────────────────────────────┘
```

### Workflow: From Story to Automated Test

#### Stage 1: Test Case Generation (Test Plan Agent)

**Input:** Jira Story
```
Story PROJ-46: KPI Widgets

Description:
As a user, I want to see KPI widgets on my dashboard so that I can
monitor key metrics at a glance.

Acceptance Criteria:
1. Dashboard displays 4 KPI widgets: Revenue, Users, Conversion Rate, CSAT
2. Each widget shows current value and trend (up/down/flat)
3. Widgets update every 30 seconds
4. Loading state shows skeleton loader
5. Error state shows "Unable to load" message
6. Clicking widget opens detail modal

Technical Notes:
- API: GET /api/dashboard/kpis
- Component: src/components/Dashboard/KPIWidget.tsx
```

**Test Plan Agent Processing:**
```python
# Test Plan Agent
test_cases = generate_test_cases(story)

Output:
- 8 test cases generated
- 3 happy path scenarios
- 3 edge case scenarios
- 2 error scenarios
```

**Generated Test Cases:**
```yaml
# test-cases/PROJ-46-kpi-widgets.yaml

test_suite: "KPI Widgets"
story: "PROJ-46"

test_cases:
  - id: TC-001
    name: "Dashboard displays all 4 KPI widgets"
    type: happy_path
    priority: critical
    steps:
      - Navigate to dashboard
      - Wait for page load
      - Verify Revenue widget is visible
      - Verify Users widget is visible
      - Verify Conversion Rate widget is visible
      - Verify CSAT widget is visible
    expected_result: "All 4 widgets displayed"

  - id: TC-002
    name: "KPI widgets show current values and trends"
    type: happy_path
    priority: high
    steps:
      - Navigate to dashboard
      - Wait for KPIs to load
      - Verify Revenue widget shows numerical value
      - Verify Revenue widget shows trend icon (up/down/flat)
      - Verify trend icon matches data direction
    expected_result: "Values and trends displayed correctly"

  - id: TC-003
    name: "KPI widgets auto-refresh every 30 seconds"
    type: happy_path
    priority: medium
    steps:
      - Navigate to dashboard
      - Note initial Revenue value
      - Wait 30 seconds
      - Verify API called again (network monitoring)
      - Verify Revenue value updated (if changed)
    expected_result: "Widgets refresh automatically"

  - id: TC-004
    name: "Loading state shows skeleton loader"
    type: happy_path
    priority: high
    steps:
      - Mock slow API response (3 second delay)
      - Navigate to dashboard
      - Verify skeleton loaders visible
      - Wait for data load
      - Verify skeleton loaders replaced with actual data
    expected_result: "Skeleton loaders shown during load"

  - id: TC-005
    name: "Error state shows friendly message"
    type: error_scenario
    priority: high
    steps:
      - Mock API to return 500 error
      - Navigate to dashboard
      - Verify error message "Unable to load" displayed
      - Verify error styling (red/warning color)
      - Verify retry button present
    expected_result: "Error state displayed correctly"

  - id: TC-006
    name: "Clicking widget opens detail modal"
    type: happy_path
    priority: high
    steps:
      - Navigate to dashboard
      - Wait for widgets to load
      - Click Revenue widget
      - Verify modal opens
      - Verify modal shows detailed Revenue data
      - Verify modal has close button
    expected_result: "Detail modal opens with correct data"

  - id: TC-007
    name: "Dashboard handles empty data gracefully"
    type: edge_case
    priority: medium
    steps:
      - Mock API to return empty data
      - Navigate to dashboard
      - Verify widgets display "No data" message
      - Verify no JavaScript errors
    expected_result: "Empty state handled gracefully"

  - id: TC-008
    name: "Dashboard handles partial API failures"
    type: edge_case
    priority: medium
    steps:
      - Mock Revenue API to fail, others succeed
      - Navigate to dashboard
      - Verify Revenue widget shows error
      - Verify other 3 widgets load normally
      - Verify page remains functional
    expected_result: "Partial failures don't break entire dashboard"
```

#### Stage 2: Playwright Script Generation (Google Antigravity)

**Input to Antigravity:** Test case YAML files

**Developer in Antigravity:**
```
Developer: "@antigravity Generate Playwright scripts for test cases in
test-cases/PROJ-46-kpi-widgets.yaml"

Antigravity:
"I'll generate Playwright scripts for all 8 test cases. Starting with TC-001..."

[Antigravity browser extension launches]
[Antigravity navigates to dashboard]
[Antigravity explores the UI]
[Antigravity generates Playwright script]

✓ Generated: tests/PROJ-46/tc-001-all-widgets-display.spec.ts

Let me run it to verify...
[Antigravity executes test]
[Captures video recording]

✓ Test TC-001 passed (2.3s)
📹 Video: tests/PROJ-46/recordings/tc-001.mp4

Continuing with TC-002...
```

**Generated Playwright Script:**
```typescript
// tests/PROJ-46/tc-001-all-widgets-display.spec.ts
// Auto-generated by Google Antigravity from Test Case TC-001

import { test, expect } from '@playwright/test';

test.describe('KPI Widgets - All widgets display', () => {
  test('TC-001: Dashboard displays all 4 KPI widgets', async ({ page }) => {
    // Navigate to dashboard
    await page.goto('http://localhost:3000/dashboard');

    // Wait for page load
    await page.waitForLoadState('networkidle');

    // Verify Revenue widget is visible
    const revenueWidget = page.locator('[data-testid="kpi-widget-revenue"]');
    await expect(revenueWidget).toBeVisible();

    // Verify Users widget is visible
    const usersWidget = page.locator('[data-testid="kpi-widget-users"]');
    await expect(usersWidget).toBeVisible();

    // Verify Conversion Rate widget is visible
    const conversionWidget = page.locator('[data-testid="kpi-widget-conversion"]');
    await expect(conversionWidget).toBeVisible();

    // Verify CSAT widget is visible
    const csatWidget = page.locator('[data-testid="kpi-widget-csat"]');
    await expect(csatWidget).toBeVisible();

    // Take screenshot for verification
    await page.screenshot({
      path: 'tests/PROJ-46/screenshots/tc-001-all-widgets.png',
      fullPage: true
    });
  });
});
```

**Antigravity's Key Capabilities:**

1. **Smart Locator Selection**
   - Prefers `data-testid` attributes (most stable)
   - Falls back to semantic HTML (role, aria-label)
   - Avoids brittle selectors (CSS classes, XPath)

2. **Automatic Waiting**
   - Waits for elements to be visible
   - Waits for network to be idle
   - Retries assertions (auto-healing)

3. **Visual Verification**
   - Captures screenshots at key steps
   - Records full video of test execution
   - Compares visual diffs (optional)

4. **Error Handling**
   - Detects test failures
   - Suggests fixes
   - Can auto-fix simple issues

#### Stage 3: Test Execution with Playwright MCP

**Playwright MCP** allows AI agents to control browser during test execution:

```python
# Playwright MCP Server integration

@mcp.tool()
def run_playwright_test(test_file: str) -> dict:
    """Execute a Playwright test and return results."""
    result = subprocess.run(
        ["npx", "playwright", "test", test_file],
        capture_output=True
    )
    return parse_test_results(result)

@mcp.tool()
def debug_test_failure(test_file: str, line_number: int) -> str:
    """Debug a failing test by inspecting the page state."""
    # Playwright MCP can control browser to inspect failure
    trace = get_playwright_trace(test_file)
    return analyze_failure(trace, line_number)
```

**Antigravity with Playwright MCP:**
```
Developer: "@antigravity Run all tests for PROJ-46 and fix any failures"

Antigravity:
"Running 8 tests for PROJ-46...

✓ TC-001: All widgets display (2.3s)
✓ TC-002: Values and trends (1.8s)
✓ TC-003: Auto-refresh (32.1s)
✓ TC-004: Loading state (3.5s)
✗ TC-005: Error state (FAILED)

Error: Expected error message not found
Expected: 'Unable to load'
Actual: 'Error loading data'

Let me debug this...
[Antigravity inspects failure in browser]
[Antigravity checks component code]

I see the issue. The component shows 'Error loading data' but the test
expects 'Unable to load'.

Options:
1. Update test to expect 'Error loading data'
2. Update component to show 'Unable to load'

Which would you prefer?"

Developer: "Update the test"

Antigravity:
"✓ Updated test TC-005 to expect 'Error loading data'
✓ Re-running TC-005... PASSED (2.1s)

Continuing...
✓ TC-006: Detail modal (2.7s)
✓ TC-007: Empty data (1.9s)
✓ TC-008: Partial failures (3.2s)

All tests passed! 🎉

Summary:
- 8 tests executed
- 8 passed
- 0 failed
- Total time: 52.3s
- Coverage: 94% (components/Dashboard/KPIWidget.tsx)

📹 Recordings: tests/PROJ-46/recordings/
📸 Screenshots: tests/PROJ-46/screenshots/
📊 Report: tests/PROJ-46/report.html
```

#### Stage 4: Self-Healing Tests

**Problem:** UI changes break tests (brittleness)

**Example:** Developer changes button text "Submit" → "Save Changes"

**Traditional Playwright:**
```typescript
// This test breaks:
await page.click('button:has-text("Submit")');
// Error: Button not found
```

**Antigravity + Playwright MCP (Self-Healing):**
```
Test execution:
[Test fails: Button "Submit" not found]

Antigravity:
"Test TC-006 failed. Analyzing...

Expected button text: 'Submit'
Actual button text: 'Save Changes'

Recommendation: Update test locator
  From: 'button:has-text("Submit")'
  To: 'button:has-text("Save Changes")'

Auto-fixing? [Y/n]"

Auto: Y

"✓ Test updated and re-run
✓ TC-006 now passes
✓ Committed fix to tests/PROJ-46/tc-006-detail-modal.spec.ts"
```

**How it works:**
1. Playwright MCP detects failure
2. Antigravity inspects actual page state
3. Compares expected vs actual
4. Proposes fix
5. Updates test
6. Re-runs test
7. Commits if passes

### Testing Stack Summary

```
Test Generation:
  Test Plan Agent (Vertex AI)
  └── Generates test cases from stories

Test Implementation:
  Google Antigravity
  ├── Generates Playwright scripts
  ├── Executes tests in browser
  ├── Records videos
  └── Captures screenshots

Test Execution & Healing:
  Playwright + Playwright MCP
  ├── Cross-browser testing
  ├── Parallel execution
  ├── Auto-retry on failure
  └── Self-healing via Antigravity

Test Infrastructure:
  GitHub Actions or Cloud Build
  ├── Run tests on every PR
  ├── Run tests on schedule (nightly)
  └── Report results to team
```

**Complete Test Workflow:**
```
1. Story created in Jira (PROJ-46)
2. Test Plan Agent generates test cases (8 test cases)
3. Developer: "@antigravity Generate tests for PROJ-46"
4. Antigravity generates Playwright scripts (8 scripts)
5. Antigravity executes tests (captures videos)
6. Tests run on every PR (CI/CD)
7. Failures analyzed by Antigravity
8. Self-healing fixes applied automatically
9. Coverage report generated
10. Results posted to Jira story

---

## Part 4: Release & Integration Workflow (Integration Agent)

### The Release Gatekeeper

**The Problem:**
Even with great dev and test tools, releases often fail because:
- Documentation wasn't updated
- A critical epic was missed
- Security tests weren't run
- Latest changes weren't merged

**Solution: The Integration Agent**
This agent acts as the automated "Release Manager", ensuring all previous steps in the SDLC were completed successfully.

### Workflow: release-readiness-check

**Triggers:**
- Scheduled nightly build
- Manual invocation before deployment
- Pull Request to `main`

**Process:**
```bash
# CI/CD Pipeline executes:
python3 integration_agent/main.py --check-all --target ./project_root
```

**Checks Performed:**
1.  **Artifact Validation**:
    - Does `docs/PRD.md` exist?
    - Are Epics defined in `docs/epics/`?
    - Do they trace back to the PRD?
2.  **Code Governance**:
    - Runs `code_governance_agent` (audit mode)
    - Fails if `RED` flags are found (e.g. hardcoded secrets)
3.  **Test Results**:
    - Parses latest Playwright test reports
    - Checks pass rate > 95%
4.  **Documentation Consistency**:
    - Verifies Architecture Hub matches Code structure (high-level check)

**Output: ReleaseReadiness.md**
```markdown
# Release Readiness Report
**Status**: 🟢 GO
**Score**: 98/100

## Checks
- [x] PRD Exists (v1.2)
- [x] Epics Defined (10 count)
- [x] Governance Check: Passed (0 critical issues)
- [x] Test Suite: 145/145 Passed

## Recommendation
Proceed with deployment to Staging.
```

---

```

---

## Complete Integration: End-to-End Example

### Scenario: Building Customer Portal Dashboard

**Week 1: Requirements (Business Analyst)**
```
1. BA uploads 25 documents to NotebookLM (2 notebooks)
2. BA explores with NotebookLM:
   - "What features are mentioned?"
   - "Any conflicting requirements?"
   - "Create timeline"
3. BA exports NotebookLM artifacts (5 files)
4. BA provides artifacts to PRD Agent
5. PRD Agent generates draft PRD (1,200 lines)
6. BA fills 3 gaps via conversation
7. PRD approved and published to:
   - Git: docs/PRD.md
   - Confluence: Customer Portal/PRD
```

**Week 2: Architecture**
```
1. Architecture Agent reads PRD
2. Generates architecture hub:
   - C4 diagrams
   - Data models
   - API contracts (OpenAPI)
   - 4 ADRs
3. Architect reviews, adds domain expertise
4. Architecture approved and published to:
   - Git: docs/architecture-hub/
   - Confluence: Customer Portal/Architecture
```

**Week 3: Planning**
```
1. Epic Agent decomposes PRD → 7 epics
2. Story Agent generates 45 stories from epics
3. Integration Agent syncs to Jira:
   - 7 epics created
   - 45 stories created
   - Stories linked to epics
4. PM prioritizes in Jira
```

**Week 4-8: Development**
```
Developer (Alice) assigned: Epic 003 - User Dashboard

Day 1:
1. Alice opens VS Code
2. Jira sidebar shows assigned epic
3. Alice clicks epic → pulls details
4. Alice clicks "View Architecture" → Confluence sidebar opens
5. Alice reviews architecture and design patterns
6. Alice creates branch: "feature/dashboard"

Day 2-5:
1. Alice implements Dashboard.tsx
2. Gemini Code Assist provides suggestions:
   - References Jira story (via MCP)
   - References Confluence architecture (via MCP)
   - Follows code quality guidelines
3. Alice commits: "PROJ-45: Implement dashboard layout"
4. Jira automatically links commit to story

Day 5:
1. Test Plan Agent generates 8 test cases for dashboard
2. Alice: "@antigravity Generate tests for dashboard epic"
3. Antigravity generates 8 Playwright scripts
4. Antigravity executes all tests
5. 7 pass, 1 fails (minor issue)
6. Antigravity suggests fix
7. Alice approves fix
8. All tests pass

Day 6:
1. Alice opens PR
2. CI/CD runs:
   - Linting
   - Unit tests
   - Playwright tests (Antigravity-generated)
3. All checks pass
4. PR approved and merged
5. Jira story auto-transitioned to "Done"
```

**Week 9: Testing**
```
QA Engineer (Bob):
1. Opens Antigravity
2. Reviews all test recordings
3. Runs full regression suite
4. 142 tests pass
5. 3 tests fail (legitimate bugs)
6. Bob creates Jira tickets for bugs
7. Antigravity generates bug reproduction videos
```

**Result:**
- ⏱️ Planning: 3 weeks (vs. 8 weeks manual)
- 💻 Development: 5 weeks (4 developers)
- ✅ Testing: 1 week (vs. 3 weeks manual)
- 📊 Test Coverage: 94% (vs. 60-70% typical)
- 🎯 Quality: 3 bugs found (vs. 15-20 typical)

---

## Implementation Roadmap

### Phase 1: BA Workflow (Months 1-2)
**Goal:** Enable BAs to handle 20+ documents efficiently

1. **NotebookLM Setup** (Week 1)
   - Train BAs on NotebookLM
   - Create notebook templates
   - Establish export workflow

2. **PRD Agent Integration** (Week 2-4)
   - Build PRD Agent with NotebookLM integration
   - Implement citation preservation
   - Test with pilot project (5-10 documents)

3. **Scale Testing** (Week 5-6)
   - Test with real project (20-25 documents)
   - Measure quality and time savings
   - Refine based on feedback

4. **Confluence Publishing** (Week 7-8)
   - Build Integration Agent for Confluence
   - Automate PRD publishing
   - Set up stakeholder access

**Success Metrics:**
- PRD creation time: <5 days (target)
- Citation coverage: >95% of statements
- Completeness: >90% of template

### Phase 2: Developer Workflow (Months 3-4)
**Goal:** Integrate Jira + Confluence + VS Code

1. **Jira Integration** (Week 1-2)
   - Set up Jira VS Code extension
   - Configure smart commits
   - Build MCP server for Jira

2. **Confluence Integration** (Week 3-4)
   - Set up Confluence VS Code extension
   - Build MCP server for Confluence
   - Test with pilot team (2-3 developers)

3. **AI Coding Assistant** (Week 5-6)
   - Set up Gemini Code Assist
   - Configure MCP servers
   - Train developers

4. **Full Workflow Test** (Week 7-8)
   - End-to-end test with real epic
   - Measure developer productivity
   - Refine based on feedback

**Success Metrics:**
- Developer satisfaction: >4.0/5.0
- Context switching: -50% (less tool switching)
- Code quality: Maintained or improved

### Phase 3: Testing Workflow (Months 5-6)
**Goal:** Automate test generation and execution

1. **Test Plan Agent** (Week 1-2)
   - Build Test Plan Agent
   - Integrate with Jira stories
   - Generate test cases for pilot

2. **Antigravity Setup** (Week 3-4)
   - Install Antigravity
   - Configure for project
   - Generate first Playwright scripts

3. **Playwright MCP** (Week 5)
   - Set up Playwright MCP server
   - Integrate with Antigravity
   - Test self-healing capabilities

4. **CI/CD Integration** (Week 6)
   - Add Playwright tests to CI/CD
   - Configure test reporting
   - Set up automated runs

**Success Metrics:**
- Test generation time: <2 hours for 10 tests
- Test coverage: >80%
- False positive rate: <10%

---

## Summary

This complete workflow integration provides:

**For Business Analysts:**
- ✅ Handle 20+ documents efficiently with NotebookLM pre-processing
- ✅ Maintain full citation traceability
- ✅ Generate comprehensive PRDs in days, not weeks

**For Developers:**
- ✅ Everything in VS Code (Jira + Confluence + AI coding)
- ✅ Full context from requirements through architecture
- ✅ AI assistant with organizational knowledge

**For QA/Testing:**
- ✅ Auto-generated test cases from requirements
- ✅ Auto-generated Playwright scripts with Antigravity
- ✅ Self-healing tests that adapt to UI changes
- ✅ Video recordings for every test execution

**Overall Benefits:**
- ⏱️ 50-60% faster project delivery
- 📈 30-40% better quality (fewer defects)
- 💰 Significant cost savings (less manual work)
- 😊 Higher team satisfaction (less tedious work)

**Tech Stack:**
- NotebookLM (document synthesis)
- Vertex AI (PRD/Architecture/Epic/Story/Test Plan agents)
- Jira (project management)
- Confluence (documentation portal)
- VS Code (development)
- Gemini Code Assist (AI coding)
- Google Antigravity (test implementation)
- Playwright + MCP (test execution and healing)

---

**Next Steps:**
1. Review this comprehensive integration plan
2. Prioritize which workflow to implement first
3. Set up pilot project to validate approach
4. Measure results and iterate

**Recommendation:** Start with BA workflow (Phase 1) as it provides foundation for all downstream work.
