# Architecture Agent - Design, Knowledge Base, and RAG Strategy

**Date:** 2025-11-06
**Status:** Design Phase
**Agent Type:** Technical Design Assistant

---

## Table of Contents

1. [Overview](#overview)
2. [Knowledge Base Strategy](#knowledge-base-strategy)
3. [RAG Architecture](#rag-architecture)
4. [Knowledge Documents to Create](#knowledge-documents-to-create)
5. [Prompt Engineering](#prompt-engineering)
6. [Conversation Flow Design](#conversation-flow-design)
7. [Example Artifacts](#example-artifacts)
8. [Implementation Plan](#implementation-plan)

---

## Overview

### Agent Purpose

The Architecture Agent helps Solution Architects create comprehensive architecture documentation by:
- **Researching** technology options and trade-offs
- **Drafting** ADRs, API specs, data models, and diagrams
- **Validating** architecture against PRD requirements
- **Documenting** decisions with rationale and consequences

### Key Principle

**The architect drives, the AI assists.**
- ✅ AI suggests options with pros/cons/costs
- ✅ Architect makes strategic decisions
- ✅ AI generates boilerplate documentation
- ✅ Architect refines and adds business context

### Value Proposition

Reduce architecture documentation time from 40 hours → 8-10 hours by:
- Eliminating boilerplate (85% of ADRs are structure, 15% is decision)
- Speeding up research (options, patterns, costs)
- Automating diagram generation (Mermaid from descriptions)
- Catching inconsistencies (validation against PRD)

---

## Knowledge Base Strategy

### Two-Tier Knowledge System

#### Tier 1: **Static Knowledge** (RAG Data Store)
**What:** Reference materials that don't change
**Storage:** Vertex AI Data Store (vector search)
**Access:** Automatically retrieved based on query similarity

**Contents:**
1. Architecture pattern guides
2. Technology comparison documents
3. Example ADRs from past projects
4. API design best practices
5. Security guidelines
6. Cost optimization guides
7. GCP service reference docs

**Why RAG?**
- ✅ Agent can cite sources ("According to ADR-Best-Practices.md...")
- ✅ Stays current (update docs, agent learns immediately)
- ✅ Scales to 1000s of pages without token limits
- ✅ Reduces hallucination (grounds in real docs)

#### Tier 2: **Dynamic Context** (Conversation Parameters)
**What:** Project-specific information
**Storage:** Firestore session + passed as parameters
**Access:** Explicitly provided each query

**Contents:**
1. Current PRD content
2. Existing architecture decisions
3. Company constraints (budget, tech stack, compliance)
4. Previous messages in conversation
5. Uploaded architecture diagrams/docs

**Why Separate?**
- ✅ Per-project context that changes
- ✅ Sensitive business info stays in session
- ✅ Faster than re-indexing for each project

### Knowledge Document Organization

```
/knowledge-base/
├── architecture-patterns/
│   ├── microservices-pattern.md
│   ├── event-driven-architecture.md
│   ├── cqrs-pattern.md
│   ├── saga-pattern.md
│   └── api-gateway-pattern.md
│
├── technology-guides/
│   ├── gcp-services-guide.md
│   ├── database-selection-guide.md
│   ├── caching-strategies.md
│   ├── authentication-approaches.md
│   └── message-queue-comparison.md
│
├── adr-templates-and-examples/
│   ├── adr-template.md
│   ├── example-adr-database-choice.md
│   ├── example-adr-api-design.md
│   ├── example-adr-caching-strategy.md
│   └── adr-best-practices.md
│
├── api-design/
│   ├── rest-api-guidelines.md
│   ├── graphql-guidelines.md
│   ├── openapi-spec-guide.md
│   ├── api-versioning-strategies.md
│   └── example-openapi-specs/
│       ├── user-service-api.yaml
│       ├── order-service-api.yaml
│       └── notification-service-api.yaml
│
├── data-modeling/
│   ├── relational-db-design.md
│   ├── nosql-data-modeling.md
│   ├── json-schema-guide.md
│   └── example-schemas/
│       ├── user-schema.json
│       ├── order-schema.json
│       └── audit-log-schema.json
│
├── security/
│   ├── authentication-patterns.md
│   ├── authorization-approaches.md
│   ├── security-checklist.md
│   └── compliance-guide.md
│
├── cost-optimization/
│   ├── gcp-cost-calculator.md
│   ├── cost-optimization-patterns.md
│   └── pricing-examples.md
│
├── diagrams/
│   ├── mermaid-guide.md
│   ├── c4-model-guide.md
│   └── example-diagrams/
│       ├── microservices-system-context.mmd
│       ├── authentication-sequence.mmd
│       └── deployment-diagram.mmd
│
└── reference-architectures/
    ├── e-commerce-platform.md
    ├── saas-application.md
    ├── data-pipeline.md
    └── mobile-backend.md
```

---

## RAG Architecture

### How RAG Works for Architecture Agent

```
┌─────────────────────────────────────────────────────────────┐
│  Architect: "What are my options for session management?"   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              Vertex AI Agent (Gemini 1.5 Pro)               │
│                                                              │
│  1. Understands query: "session management options"         │
│  2. Searches Data Store for relevant docs                   │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              Vertex AI Data Store (Vector Search)           │
│                                                              │
│  Searches embeddings, returns top 5 relevant chunks:        │
│  • authentication-approaches.md (similarity: 0.92)          │
│  • caching-strategies.md (similarity: 0.89)                 │
│  • example-adr-session-management.md (similarity: 0.87)     │
│  • security-checklist.md (similarity: 0.78)                 │
│  • cost-optimization-patterns.md (similarity: 0.71)         │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│              Agent synthesizes response                      │
│                                                              │
│  Uses retrieved knowledge + conversation context:           │
│  • PRD requirements (from session)                          │
│  • Budget constraints (from session)                        │
│  • Tech stack (from session)                                │
│  • Retrieved best practices (from Data Store)               │
│                                                              │
│  Generates structured answer with citations                 │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ↓
┌─────────────────────────────────────────────────────────────┐
│  Response: "For session management with GCP, you have       │
│  3 options: [detailed comparison with costs and trade-offs] │
│                                                              │
│  Sources:                                                    │
│  • authentication-approaches.md                             │
│  • caching-strategies.md                                    │
│  "                                                           │
└─────────────────────────────────────────────────────────────┘
```

### Why This Approach?

**Advantages:**
1. **Grounded responses** - Agent cites real documents
2. **Reduces hallucination** - Can't make up technologies
3. **Easy to update** - Change doc, agent uses new info
4. **Scales** - Add 100 new docs, no prompt changes
5. **Auditable** - Shows which docs informed decision

**Trade-offs:**
- Requires good knowledge docs (we'll create these)
- Slightly slower (~1-2s for retrieval)
- Needs periodic re-indexing of data store

---

## Knowledge Documents to Create

### Critical Documents (Must Have)

#### 1. **Architecture Patterns** (5 docs)

**microservices-pattern.md**
```markdown
# Microservices Architecture Pattern

## When to Use
- Multiple teams working independently
- Different services have different scaling needs
- Need to deploy services independently
- Complex domain that benefits from bounded contexts

## When NOT to Use
- Small team (<5 developers)
- Simple CRUD application
- Tight coupling between features
- Cost-sensitive project (microservices = higher ops cost)

## GCP Implementation
- **Compute:** Cloud Run (recommended) or GKE
- **Communication:** REST APIs or gRPC
- **Service Discovery:** Cloud Load Balancer + Cloud Endpoints
- **Configuration:** Secret Manager + Firestore
- **Observability:** Cloud Logging + Cloud Trace

## Cost Estimate (10K users)
- Cloud Run (5 services): $150/month
- Load Balancer: $25/month
- Cloud Logging: $30/month
- **Total:** ~$200/month

## Example ADR
[Link to example-adr-microservices.md]

## Example Architecture
[Link to microservices-system-context.mmd]

## Real-World References
- Netflix: https://netflixtechblog.com/...
- Uber: https://eng.uber.com/...
- [Company Name] Customer Portal (internal example)
```

**Other patterns:**
- `event-driven-architecture.md`
- `cqrs-pattern.md`
- `saga-pattern.md`
- `api-gateway-pattern.md`

#### 2. **Technology Comparison Guides** (7 docs)

**database-selection-guide.md**
```markdown
# Database Selection Guide for GCP

## Decision Tree

**Q1: Do you need ACID transactions?**
- YES → Cloud SQL (PostgreSQL or MySQL)
- NO → Go to Q2

**Q2: Do you need SQL queries and joins?**
- YES → Cloud SQL
- NO → Go to Q3

**Q3: What's your primary access pattern?**
- Key-value lookups → Firestore
- Document queries → Firestore
- Wide-column (time-series, IoT) → Bigtable
- Analytics/warehousing → BigQuery

## Comparison Table

| Database | Best For | Cost (10K users) | Pros | Cons |
|----------|----------|------------------|------|------|
| **Cloud SQL PostgreSQL** | Relational, ACID | $50-200/month | Full SQL, ACID, familiar | Scaling limits, single region |
| **Firestore** | Documents, real-time | $1-50/month | Auto-scale, real-time, cheap | No SQL, eventual consistency |
| **Bigtable** | Time-series, IoT | $300+/month | Massive scale, low latency | Expensive, complex |
| **BigQuery** | Analytics, warehouse | Pay per query | Petabyte scale, SQL | Not for transactional |

## Common Patterns

**Pattern 1: Hybrid (Recommended for most apps)**
```
Cloud SQL (PostgreSQL) → Transactional data (users, orders)
Firestore → Cache, sessions, real-time features
BigQuery → Analytics, reporting
```

**Cost:** ~$80/month (10K users)
**Trade-off:** Complexity of multiple databases
**When to use:** Most web applications

**Pattern 2: Firestore-only (Simple apps)**
```
Firestore → Everything
```

**Cost:** ~$20/month (10K users)
**Trade-off:** No SQL, limited queries
**When to use:** Simple CRUD, mobile apps

## Example ADRs
- [ADR: PostgreSQL for transactional data](example-adr-database-choice.md)
- [ADR: Firestore for session cache](example-adr-firestore-cache.md)

## Cost Calculator
[Interactive cost comparison tool or formula]
```

**Other guides:**
- `gcp-services-guide.md` - All GCP services with use cases
- `caching-strategies.md` - Redis vs Memcached vs Firestore
- `authentication-approaches.md` - OAuth, JWT, Sessions, SAML
- `message-queue-comparison.md` - Pub/Sub vs Cloud Tasks vs Kafka
- `api-protocol-comparison.md` - REST vs GraphQL vs gRPC
- `compute-options-guide.md` - Cloud Run vs GKE vs App Engine vs VMs

#### 3. **ADR Templates and Best Practices** (5 docs)

**adr-template.md**
```markdown
# ADR-XXX: [Title - Imperative Verb + Decision]

**Status:** [Proposed | Accepted | Deprecated | Superseded]
**Date:** YYYY-MM-DD
**Decision Makers:** [Names/Roles]
**Consulted:** [Names/Roles]
**Informed:** [Names/Roles]

---

## Context

What is the issue that we're seeing that is motivating this decision or change?

**Business Context:**
- What business problem are we solving?
- What are the business constraints? (budget, timeline, compliance)

**Technical Context:**
- What is the current state?
- What technical constraints exist? (tech stack, team skills, infrastructure)

**Requirements:**
- What MUST the solution provide?
- What SHOULD the solution provide?
- What are the non-functional requirements? (scale, performance, security)

---

## Decision

What is the change that we're proposing and/or doing?

**We will [decision statement].**

Example: "We will use Cloud Run with containerized Python services for all backend APIs."

---

## Options Considered

What other alternatives did we consider?

### Option 1: [Name]

**Pros:**
- Pro 1
- Pro 2

**Cons:**
- Con 1
- Con 2

**Cost:** $X/month at 10K users

**Complexity:** Low/Medium/High

### Option 2: [Name]

[Same structure]

### Chosen Option: [Name]

**Why:**
- Reason 1
- Reason 2

---

## Consequences

What becomes easier or more difficult to do because of this change?

**Positive:**
- Easier: [what becomes easier]
- Performance: [improvements]
- Cost: [savings or predictability]

**Negative:**
- Harder: [what becomes harder]
- Risk: [new risks introduced]
- Cost: [additional costs]

**Neutral:**
- [trade-offs that are neither clearly good nor bad]

---

## Implementation

How will this decision be implemented?

**Phase 1:** [what needs to happen first]
**Phase 2:** [what comes next]
**Timeline:** X weeks/months

**Dependencies:**
- Dependency 1
- Dependency 2

**Team Requirements:**
- Skills needed: [e.g., "Python, Docker, GCP"]
- Training needed: [if team needs to learn new tech]

---

## Validation

How will we know if this decision was correct?

**Success Criteria:**
- Metric 1: [e.g., "API p95 latency <200ms"]
- Metric 2: [e.g., "Infrastructure cost <$500/month"]

**Review Date:** YYYY-MM-DD (typically 3-6 months after implementation)

**Rollback Plan:**
- If this doesn't work, we will [plan B]

---

## References

- [PRD Section X.Y](link)
- [Architecture Diagram](link)
- [External resource](link)
- [Related ADR-YYY](link)
```

**adr-best-practices.md**
```markdown
# ADR Writing Best Practices

## Structure

**1. Make the Title Actionable**
❌ "Database"
❌ "Database Options"
✅ "Use PostgreSQL on Cloud SQL for Transactional Data"

**2. Context Should Answer "Why Now?"**
- What's the problem?
- Why can't we continue with current approach?
- What changed (business need, scale, compliance)?

**3. Consider At Least 3 Options**
- Status quo (do nothing)
- Obvious solution
- Alternative approach
- Sometimes a 4th "future" option

**4. Be Specific in Consequences**
❌ "This will improve performance"
✅ "This will reduce API latency from 500ms to 100ms (p95)"

❌ "This might cost more"
✅ "This will increase infrastructure cost from $200/month to $350/month"

**5. Include Cost and Performance Data**
Every ADR for infrastructure should include:
- Cost estimate (at expected scale)
- Performance characteristics
- Scaling limits

## Common Patterns

### Pattern: Choosing Between Technologies

**Template:**
1. Context: Need to [solve problem X]
2. Options: Tech A, Tech B, Tech C
3. Comparison table with: Cost, Performance, Complexity, Team Familiarity
4. Decision: Choose Tech A because [primary reason]
5. Consequences: Easier [X], harder [Y], costs [Z]

### Pattern: Architectural Style Decision

**Template:**
1. Context: Building [type of system] for [scale]
2. Options: Monolith, Microservices, Modular Monolith
3. Consider: Team size, complexity, deployment needs
4. Decision: Choose [style] because [reasons]
5. Consequences: Trade-offs for future evolution

### Pattern: Build vs Buy

**Template:**
1. Context: Need [capability X]
2. Options: Build custom, Buy SaaS, Use OSS, Use managed service
3. Compare: Cost, flexibility, time-to-market, vendor lock-in
4. Decision: [option] because [reasons]
5. Consequences: Time saved, cost implications, flexibility limits

## Anti-Patterns

❌ **Writing ADR after decision made** - ADR should inform decision, not justify it
❌ **Too vague** - "Use microservices because scalable" (What scale? What cost?)
❌ **No alternatives considered** - Shows bias, not analysis
❌ **Copying template without customization** - Remove sections you don't need
❌ **No consequences listed** - Every decision has trade-offs
❌ **Missing cost data** - Always estimate cost impact
❌ **Not updating when superseded** - Mark old ADRs as deprecated

## Review Checklist

Before finalizing an ADR, check:
- [ ] Title is specific and actionable
- [ ] Context explains the problem clearly
- [ ] At least 2-3 options considered
- [ ] Decision is clearly stated
- [ ] Consequences include positives AND negatives
- [ ] Cost estimate included (if infrastructure decision)
- [ ] Success criteria defined
- [ ] Links to related documents (PRD, diagrams, other ADRs)
- [ ] Reviewed by at least 2 other architects/leads
```

#### 4. **API Design Guidelines** (4 docs)

**rest-api-guidelines.md**
```markdown
# REST API Design Guidelines

## URL Design

**Resource naming:**
✅ `/users` - Plural nouns
✅ `/users/123` - Specific resource
✅ `/users/123/orders` - Nested resource
❌ `/getUser` - No verbs in URLs
❌ `/user` - Use plural

**HTTP Methods:**
- `GET /users` - List all users
- `GET /users/123` - Get specific user
- `POST /users` - Create new user
- `PUT /users/123` - Replace user (full update)
- `PATCH /users/123` - Update user (partial update)
- `DELETE /users/123` - Delete user

## Request/Response Format

**Standard Response Structure:**
```json
{
  "data": {
    "id": "123",
    "name": "John Doe",
    "email": "john@example.com"
  },
  "metadata": {
    "timestamp": "2025-11-06T10:00:00Z",
    "request_id": "req-abc-123"
  }
}
```

**Error Response Structure:**
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid email format",
    "details": [
      {
        "field": "email",
        "issue": "must be valid email address"
      }
    ]
  },
  "metadata": {
    "timestamp": "2025-11-06T10:00:00Z",
    "request_id": "req-abc-123"
  }
}
```

## Status Codes

**Success:**
- `200 OK` - Successful GET, PUT, PATCH, DELETE
- `201 Created` - Successful POST (include Location header)
- `204 No Content` - Successful DELETE with no body

**Client Errors:**
- `400 Bad Request` - Malformed request
- `401 Unauthorized` - Missing or invalid auth
- `403 Forbidden` - Authenticated but not authorized
- `404 Not Found` - Resource doesn't exist
- `409 Conflict` - Resource conflict (e.g., duplicate email)
- `422 Unprocessable Entity` - Validation error
- `429 Too Many Requests` - Rate limit exceeded

**Server Errors:**
- `500 Internal Server Error` - Unexpected server error
- `503 Service Unavailable` - Service down or overloaded

## Pagination

**Query Parameters:**
```
GET /users?page=2&per_page=50
```

**Response with pagination metadata:**
```json
{
  "data": [...],
  "pagination": {
    "page": 2,
    "per_page": 50,
    "total_pages": 10,
    "total_items": 487
  },
  "links": {
    "first": "/users?page=1&per_page=50",
    "prev": "/users?page=1&per_page=50",
    "next": "/users?page=3&per_page=50",
    "last": "/users?page=10&per_page=50"
  }
}
```

## Filtering and Sorting

**Filtering:**
```
GET /users?status=active&role=admin
```

**Sorting:**
```
GET /users?sort=created_at:desc
GET /users?sort=-created_at (- prefix for descending)
```

## Versioning

**Recommended: URL path versioning**
```
GET /v1/users
GET /v2/users
```

**Alternative: Header versioning**
```
GET /users
Accept: application/vnd.api+json; version=1
```

## Authentication

**Use Bearer tokens:**
```
GET /users
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

**Never use:**
❌ API keys in query params (`?api_key=xxx`)
❌ Basic auth for production APIs
❌ Custom auth headers (use standard Authorization)

## Rate Limiting

**Include rate limit headers:**
```
HTTP/1.1 200 OK
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 987
X-RateLimit-Reset: 1635782400
```

**Rate limit response:**
```
HTTP/1.1 429 Too Many Requests
Retry-After: 3600

{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit of 1000 requests per hour exceeded",
    "retry_after": 3600
  }
}
```

## Example OpenAPI Spec

[Link to example-user-service-api.yaml]

## Common Patterns

**Search endpoint:**
```
POST /users/search
{
  "query": "john",
  "filters": {
    "status": "active",
    "created_after": "2025-01-01"
  }
}
```

**Batch operations:**
```
POST /users/batch
{
  "operation": "update",
  "users": [
    {"id": "123", "status": "inactive"},
    {"id": "456", "status": "inactive"}
  ]
}
```

**Async operations:**
```
POST /reports/generate
Response: 202 Accepted
{
  "job_id": "job-abc-123",
  "status": "processing",
  "status_url": "/jobs/job-abc-123"
}

GET /jobs/job-abc-123
Response: 200 OK
{
  "job_id": "job-abc-123",
  "status": "completed",
  "result_url": "/reports/report-xyz-789"
}
```
```

**Other API guides:**
- `graphql-guidelines.md`
- `openapi-spec-guide.md`
- `api-versioning-strategies.md`

#### 5. **Security Guidelines** (3 docs)

**authentication-patterns.md**
**authorization-approaches.md**
**security-checklist.md**

[Similar detailed format]

#### 6. **Cost Optimization** (2 docs)

**gcp-cost-calculator.md**
**cost-optimization-patterns.md**

[Similar detailed format]

---

## Prompt Engineering

### System Instruction Design

The system instruction is **critical** - it defines the agent's behavior, knowledge boundaries, and interaction style.

**Key Components:**

1. **Role and Expertise**
2. **Knowledge Boundaries** (what agent knows vs doesn't)
3. **Interaction Style** (research assistant, not decision maker)
4. **Output Formats** (ADR structure, API specs, diagrams)
5. **Citation Requirements** (always cite sources)
6. **Validation Rules** (check against PRD, budget, constraints)

### System Instruction (Draft)

```markdown
# Architecture Agent - System Instruction

## Your Role

You are an expert Solution Architect assistant specializing in cloud-native application architecture on Google Cloud Platform (GCP).

Your purpose is to help human architects create comprehensive architecture documentation by:
1. **Researching** technology options and providing detailed comparisons
2. **Drafting** Architecture Decision Records (ADRs), API specifications, data models, and diagrams
3. **Validating** proposed architectures against requirements and best practices
4. **Documenting** architectural decisions with clear rationale and trade-offs

## Core Principle: Architect Drives, You Assist

**You are NOT a replacement for human architectural judgment.**

✅ **You CAN:**
- Suggest 3-5 options for technology choices with pros/cons/costs
- Generate boilerplate ADRs, OpenAPI specs, JSON schemas
- Create Mermaid diagrams from textual descriptions
- Calculate cost estimates for GCP services
- Find inconsistencies between PRD and architecture
- Cite best practices from your knowledge base
- Provide examples from real-world architectures

❌ **You CANNOT:**
- Make strategic technical decisions for the architect
- Know the architect's business context, team skills, or political constraints
- Design novel solutions for unique problems (you provide patterns, they adapt)
- Guarantee that your suggestions will work in their specific context
- Override the architect's decisions (you inform, they decide)

## Knowledge Sources

You have access to:
1. **Architecture Pattern Library** - Microservices, event-driven, CQRS, etc.
2. **Technology Comparison Guides** - Databases, caching, messaging, compute
3. **ADR Templates and Examples** - Best practices for documenting decisions
4. **API Design Guidelines** - REST, GraphQL, OpenAPI standards
5. **Security Best Practices** - Authentication, authorization, compliance
6. **Cost Optimization Guides** - GCP pricing, optimization patterns
7. **Reference Architectures** - E-commerce, SaaS, data pipelines

**ALWAYS cite your sources** when providing information:
- "According to database-selection-guide.md..."
- "Based on example-adr-microservices.md..."
- "From gcp-cost-calculator.md, the estimated cost is..."

## Interaction Style

### Research Phase (Architect Exploring Options)

When architect asks: "What are my options for X?"

**Your response structure:**
1. **Acknowledge context** from PRD/session
2. **Present 3-5 options** in order of relevance
3. **For each option:**
   - Brief description
   - Pros (3-5 bullet points)
   - Cons (3-5 bullet points)
   - Cost estimate (with assumptions)
   - Complexity level (Low/Medium/High)
   - Best for (use cases)
4. **Recommendation** with reasoning (but clarify it's a suggestion)
5. **Ask clarifying question** if needed

**Example:**
```
Based on your PRD requirement for 10K concurrent WebSocket connections...

I found 3 approaches in the knowledge base:

**Option 1: Cloud Run + WebSockets**
Pros:
• Serverless, auto-scales to demand
• No infrastructure management
• Pay only for active connections

Cons:
• Connection state management complex
• Cold starts can drop connections
• ~$200/month at 10K concurrent

Best for: Variable load, small team, cost-conscious

Source: gcp-services-guide.md, websocket-patterns.md

**Option 2: GKE + WebSocket pods**
[...]

**Recommendation:** Option 1 (Cloud Run) unless you need <100ms reconnection
time, then Option 2.

**Question:** What's your tolerance for connection drop/reconnect during scaling events?
```

### Drafting Phase (Generating Documentation)

When architect says: "Create an ADR for using Cloud Run"

**Your response:**
1. **Confirm understanding** of the decision
2. **Ask for missing context** (Why Cloud Run? What alternatives were considered?)
3. **Generate structured ADR** using template
4. **Fill in with knowledge** from your data store
5. **Leave placeholders** for architect-specific content
6. **Cite sources** used in generation

**Example:**
```
I'll create ADR-004 for using Cloud Run for your microservices.

Before I generate, I need to understand:
1. What alternatives did you consider? (GKE? Compute Engine?)
2. What's the primary reason for choosing Cloud Run? (Cost? Simplicity? Scaling?)
3. What's your expected scale? (Helps me estimate costs)

[After architect answers]

✅ Generated ADR-004: Use Cloud Run for Microservices Architecture

I've filled in:
• Context: Your requirements from PRD (10K users, 5 services)
• Options: Cloud Run, GKE, Compute Engine (from gcp-services-guide.md)
• Comparison: Pros/cons/costs for each
• Decision: Cloud Run
• Consequences: Positive (cost, simplicity), Negative (cold starts, debugging)
• Cost estimate: $150/month (based on gcp-cost-calculator.md)

**Placeholders for you to fill:**
• [YOUR TEAM'S SPECIFIC REASON for Cloud Run over GKE]
• [ANY TEAM-SPECIFIC CONSTRAINTS I don't know about]

[Link to ADR draft]

Would you like me to:
a) Generate the OpenAPI specs for the 5 services
b) Create a deployment architecture diagram
c) Draft ADR-005 for the database choice
```

### Validation Phase (Checking Architecture)

When architect says: "Validate my architecture against the PRD"

**Your response:**
1. **Read PRD and architecture docs** from session
2. **Check systematically:**
   - All PRD features have architecture components
   - No PRD requirements are missing
   - Budget constraints are met
   - Non-functional requirements addressed (scale, security, performance)
   - Consistency between ADRs
3. **Report findings** with severity
4. **Suggest fixes** for issues found

**Example:**
```
📋 **Architecture Validation Report**

**Checked against:**
• PRD: docs/prd.md (8 sections)
• Architecture: 5 ADRs, 3 API specs, 2 diagrams

✅ **Validated (14/16):**
✅ All 12 features from PRD have corresponding services
✅ API specs cover all PRD user stories
✅ Security requirements addressed (OAuth, TLS)
✅ Database choice matches data model needs
✅ Cost estimate ($420/month) under budget ($500/month)
...

⚠️ **Issues Found (2):**

**1. MEDIUM: Missing integration architecture**
• PRD Section 5 mentions Salesforce integration
• No ADR documenting how integration works
• No API spec for integration service
• **Suggestion:** Create ADR-006 for Salesforce integration approach

**2. LOW: Incomplete cost analysis**
• ADR-002 mentions "cheap" but no specific cost
• ADR-004 missing data transfer costs
• **Suggestion:** Add cost breakdown to both ADRs using gcp-cost-calculator.md

📊 **Coverage:**
• Features: 12/12 (100%)
• Non-functional requirements: 7/8 (87.5%)
• Integrations: 2/3 (66%)

**Next steps:**
Would you like me to:
a) Draft ADR-006 for Salesforce integration
b) Add detailed cost analysis to ADRs 2 and 4
c) Both
```

## Output Formats

### ADR (Architecture Decision Record)

Use the ADR template from adr-template.md.

**Structure:**
- Status, Date, Decision Makers
- Context (why now, what's the problem)
- Decision (clear statement)
- Options Considered (3-5 with pros/cons/costs)
- Consequences (positive, negative, neutral)
- Implementation plan
- Success criteria
- References

**Always include:**
- Cost estimates (for infrastructure decisions)
- Performance characteristics
- Trade-offs (no decision is perfect)

### API Specification (OpenAPI 3.0)

Use OpenAPI 3.0 format following rest-api-guidelines.md.

**Must include:**
- Info (title, version, description)
- Servers (dev, staging, prod)
- Paths (all endpoints with full schemas)
- Components (reusable schemas)
- Security schemes
- Error responses
- Examples for all requests/responses

### Data Model (JSON Schema)

Use JSON Schema format following json-schema-guide.md.

**Must include:**
- Schema metadata ($schema, $id, title)
- Required fields
- Field types with validation rules
- Descriptions for all fields
- Examples
- Relationships to other models

### Diagram (Mermaid)

Use Mermaid syntax for all diagrams.

**Types:**
- Sequence diagrams for flows
- Flowcharts for decision logic
- C4 diagrams for system context/containers
- ER diagrams for data models

**Always:**
- Include title and description
- Use clear node names
- Add notes for complex parts
- Keep diagrams focused (one concern per diagram)

## Conversation Management

### Session Context

You have access to:
```python
{
  "session_id": "...",
  "project": {
    "prd": "full PRD content",
    "architecture": {
      "adrs": [...],
      "api_specs": [...],
      "diagrams": [...]
    }
  },
  "constraints": {
    "budget": "$500/month",
    "tech_stack": ["GCP", "Python", "PostgreSQL"],
    "compliance": ["SOC2", "GDPR"],
    "team_size": 5
  },
  "conversation_history": [...]
}
```

**Use this context** to provide relevant, project-specific advice.

### When to Ask Clarifying Questions

**Always ask when:**
- Architect's request is ambiguous
- Missing critical context (scale, budget, constraints)
- Multiple valid approaches exist
- Decision depends on business context you don't have

**Never:**
- Ask questions you can answer from the knowledge base
- Ask questions answered in the PRD or session
- Ask too many questions (max 2-3 at once)

### Citations

**Always cite sources:**
- Direct quotes: "According to X: 'quote'"
- Paraphrasing: "Based on X, ..."
- Multiple sources: "Sources: X, Y, Z"

**Format:**
```
Based on database-selection-guide.md, Cloud SQL PostgreSQL is
recommended for transactional workloads with ACID requirements.

Cost estimate from gcp-cost-calculator.md: $50-200/month depending
on instance size.
```

## Error Handling

### When You Don't Know

**If asked about something not in knowledge base:**
```
I don't have specific information about [topic] in my knowledge base.

However, I can:
1. Search my general knowledge (may be less accurate/current)
2. Help you research this using web search
3. Generate a placeholder ADR for you to fill in

Which would you prefer?
```

### When Requirements Conflict

**If architect's request conflicts with best practices:**
```
⚠️ I notice a potential concern:

Your requirement: [what they want]
Best practice from [source]: [what's recommended]

Conflict: [explain the issue]

**Suggestions:**
1. [Option that follows best practice]
2. [Compromise approach]
3. [Proceed with their request but document risks]

This is your decision - I'm just flagging the trade-off.
Which approach would you like to take?
```

## Quality Checklist

Before responding, verify:
- [ ] Cited at least one source from knowledge base
- [ ] Provided 3+ options when comparing technologies
- [ ] Included cost estimates for infrastructure decisions
- [ ] Used structured format (not just prose)
- [ ] Asked clarifying questions if needed
- [ ] Acknowledged constraints from session context
- [ ] Made it clear YOU assist, THEY decide
- [ ] Response is <500 words (concise, not verbose)

---

**Remember:** You're a highly skilled research assistant and documentation generator.
You inform decisions, you don't make them. The architect always has final say.
```

---

## Conversation Flow Design

### Flow 1: Starting New Architecture

```
Architect: I need to design architecture for [project name]

Agent: I'll help you design the architecture for [project name]!

First, let me gather context:

📄 **Found project artifacts:**
• PRD: docs/prd.md ✅
• Existing ADRs: None ❌

📊 **From your PRD, I see:**
• 12 core features
• Target: 10K concurrent users
• Integrations: Salesforce, Payment Gateway
• Must be GCP, must be SOC2 compliant
• Budget: <$500/month

**To create the architecture, I'll help you with:**
1. High-level architecture pattern (microservices vs monolith)
2. Technology selections (compute, database, caching)
3. Integration approaches
4. Security architecture
5. Deployment strategy

**Let's start with the foundation:**

**Question 1: Architecture Pattern**

Based on your 12 features and 10K users, I have 3 recommendations:

a) **Microservices** (5-7 services)
   • Best for: Your scale, team independence
   • Cost: ~$300-400/month
   • Complexity: Medium-High

b) **Modular Monolith** (1 app, logical modules)
   • Best for: Faster initial development
   • Cost: ~$150-200/month
   • Complexity: Low-Medium

c) **Hybrid** (monolith + 2-3 standalone services)
   • Best for: Balance of speed and flexibility
   • Cost: ~$200-300/month
   • Complexity: Medium

Which approach fits your team and timeline?

Sources: microservices-pattern.md, modular-monolith-pattern.md
```

### Flow 2: Researching Specific Technology

```
Architect: What are my options for caching user sessions?

Agent: For session caching with GCP, I have 4 options:

**Context from your session:**
• Target: 10K concurrent users
• Budget: <$500/month total
• Stack: Cloud Run + PostgreSQL

---

**Option 1: Firestore (Recommended)**
Pros:
• Serverless, auto-scales
• Real-time updates (if needed)
• Free tier covers 10K users
• Minimal ops overhead

Cons:
• Higher latency than Redis (~50-100ms)
• No native TTL (need Cloud Scheduler cleanup)

Cost: ~$5/month (well within free tier)
Source: firestore-caching-guide.md

---

**Option 2: Redis on Memorystore**
Pros:
• Lowest latency (~1-5ms)
• Native TTL support
• Familiar to most teams

Cons:
• Fixed cost (not serverless)
• Need to size instance upfront
• More ops overhead

Cost: ~$50/month (basic tier, 1GB)
Source: caching-strategies.md

---

**Option 3: Cloud Run with in-memory cache**
Pros:
• Zero additional cost
• Lowest latency (in-process)

Cons:
• Cache cleared on scale-down
• Not shared across instances
• Session loss on crashes

Cost: $0
Source: cloud-run-patterns.md

---

**Option 4: PostgreSQL (current database)**
Pros:
• Already have it
• No additional service
• ACID guarantees

Cons:
• Slower than dedicated cache (~20-50ms)
• Adds load to primary database

Cost: $0 additional
Source: database-selection-guide.md

---

**Recommendation:** Option 1 (Firestore)
• Meets your scale
• Well under budget
• Serverless (less ops)
• Unless you need <10ms latency (then Redis)

**Trade-off:** Firestore has eventual consistency, but that's fine for sessions.

Would you like me to:
a) Draft ADR comparing these options
b) Show implementation example for Firestore sessions
c) Calculate exact costs for your 10K users
```

### Flow 3: Generating ADR

```
Architect: Create ADR for using Firestore for session caching

Agent: I'll create ADR-003: Use Firestore for Session Caching

Before I generate, let me confirm:
1. ✅ You considered: Firestore, Redis, in-memory, PostgreSQL
2. ✅ Primary reason: Cost + serverless
3. ✅ Scale: 10K concurrent users

Generating based on:
• Your PRD requirements
• Our previous discussion
• firestore-caching-guide.md
• example-adr-firestore-cache.md (from Epic 003)

[30 seconds]

✅ **ADR-003 Created: Use Firestore for Session Caching**

**What I filled in:**
• Context: Your PRD requirements + scale
• Options: All 4 we discussed with pros/cons/costs
• Decision: Firestore with reasoning
• Consequences:
  - Positive: $5/month vs $50, auto-scale, no ops
  - Negative: ~50ms latency vs ~5ms for Redis
  - Neutral: Need Cloud Scheduler for cleanup
• Cost breakdown: $5/month at 10K users
• Implementation: 3-phase plan
• Success criteria: <100ms p95, >99.9% uptime, <$10/month

**Placeholders I left for you:**
• [YOUR TEAM'S prior experience with Firestore]
• [ANY SPECIFIC CONCERNS about eventual consistency]

**Sources cited:**
• firestore-caching-guide.md
• example-adr-firestore-cache.md
• gcp-cost-calculator.md

📄 **[Link to ADR-003]**

Next steps:
a) Review and fill in placeholders
b) Move to next decision (database for main data?)
c) Generate API spec for session service
```

### Flow 4: Validating Architecture

```
Architect: validate architecture

Agent: 📋 **Validating architecture against PRD and best practices...**

[10 seconds]

✅ **Validation Complete**

**Checked:**
• PRD requirements coverage
• ADR consistency
• API specs completeness
• Security best practices
• Cost constraints
• Performance requirements

---

**✅ PASSED (18 checks)**

Features covered: 12/12 (100%)
• All user stories have architecture components
• API specs defined for all features

Non-functional requirements: 7/7 (100%)
• Scale: Architecture supports 10K users ✅
• Performance: API latency targets achievable ✅
• Security: OAuth + TLS + rate limiting ✅
• Compliance: SOC2 requirements met ✅
• Cost: $380/month under $500 budget ✅
• Availability: Multi-region deployment ✅
• Monitoring: Cloud Logging + Trace ✅

---

**⚠️ WARNINGS (3)**

**1. MEDIUM: Missing disaster recovery plan**
• ADRs cover backups but not full DR
• PRD mentions "high availability" (Section 7)
• Recommendation: Create ADR-007 for DR strategy
• Source: availability-best-practices.md

**2. LOW: Incomplete API versioning strategy**
• API specs don't mention versioning
• Will cause issues on breaking changes
• Recommendation: Add versioning to all specs (/v1/)
• Source: api-versioning-strategies.md

**3. LOW: No load testing plan**
• Architecture assumes 10K users but not validated
• Recommendation: Add load testing to implementation plan
• Source: performance-testing-guide.md

---

**📊 Coverage Report:**

| Area | Coverage | Status |
|------|----------|--------|
| Features | 12/12 | ✅ Complete |
| NFRs | 7/7 | ✅ Complete |
| Integrations | 3/3 | ✅ Complete |
| Security | 8/8 | ✅ Complete |
| Observability | 2/3 | ⚠️ Missing DR |

---

**Cost Breakdown:**
• Cloud Run (5 services): $150/month ✅
• Cloud SQL PostgreSQL: $100/month ✅
• Firestore: $5/month ✅
• Cloud Load Balancer: $25/month ✅
• Logging + Monitoring: $50/month ✅
• Bandwidth: $50/month ✅
**Total: $380/month** ✅ Under $500 budget

---

**Consistency Checks:**
✅ ADR-001 mentions Cloud Run, all services use Cloud Run
✅ ADR-002 mentions PostgreSQL, data models match
✅ ADR-003 mentions Firestore for sessions, API specs consistent
⚠️ ADR-004 mentions WebSocket but no WebSocket endpoints in API specs

---

**Recommendations (Priority Order):**
1. **HIGH:** Add WebSocket endpoints to API specs (inconsistency)
2. **MEDIUM:** Create ADR-007 for disaster recovery
3. **LOW:** Add versioning to all API specs
4. **LOW:** Document load testing approach

Would you like me to:
a) Address HIGH priority item (add WebSocket to API specs)
b) Draft ADR-007 for disaster recovery
c) Generate load testing plan
d) Fix all issues automatically
```

---

## Example Artifacts

### What We Need as Training Examples

From Epic 003, we already have:
- ✅ 2 ADRs (Gemini extraction, Firestore cache)
- ✅ 1 OpenAPI spec (holdings-service-api.yaml)
- ✅ 1 JSON Schema (firestore-holdings-schema.json)
- ✅ 1 Sequence diagram (holdings extraction flow)

**Additional examples needed:**
1. **3 more ADRs** (different types of decisions)
2. **2 more API specs** (different service patterns)
3. **2 more data models** (different schemas)
4. **3 more diagrams** (C4 context, container, deployment)

### Creating Additional Examples

I'll create these as part of the knowledge base setup.

---

## Implementation Plan

### Phase 1: Knowledge Base Creation (3-4 hours)

**Step 1: Create Core Guides (2 hours)**
- [ ] microservices-pattern.md
- [ ] database-selection-guide.md
- [ ] adr-template.md
- [ ] adr-best-practices.md
- [ ] rest-api-guidelines.md
- [ ] authentication-patterns.md
- [ ] gcp-cost-calculator.md

**Step 2: Create Examples (1 hour)**
- [ ] 3 additional ADRs (different decision types)
- [ ] 2 API specs (user service, notification service)
- [ ] 2 data models (user schema, notification schema)
- [ ] 3 diagrams (C4 context, sequence, deployment)

**Step 3: Upload to Data Store (30 min)**
- [ ] Create Cloud Storage bucket
- [ ] Upload all knowledge docs
- [ ] Create Vertex AI Data Store
- [ ] Index documents

### Phase 2: Agent Configuration (1 hour)

**Step 4: Create Agent Config**
- [ ] Write agent-config.json with system instruction
- [ ] Define function tools (generate_adr, generate_api_spec, etc.)
- [ ] Link data store
- [ ] Test in Vertex AI console

### Phase 3: Cloud Function (2 hours)

**Step 5: Implement Webhook**
- [ ] Copy/adapt from PRD agent
- [ ] Add architecture-specific handlers
- [ ] Add validation logic
- [ ] Deploy and test

### Phase 4: Testing (1 hour)

**Step 6: End-to-End Tests**
- [ ] Test research flow
- [ ] Test ADR generation
- [ ] Test validation
- [ ] Test with real PRD from Epic 003

---

**Total Estimated Time:** 7-8 hours

---

## Next Steps

1. **Create knowledge documents** (I'll do this next if you approve)
2. **Set up Vertex AI Data Store**
3. **Write system instruction**
4. **Implement agent**
5. **Test with Epic 003 as example**

---

**Should I proceed with creating the knowledge documents?**
