# 🏛️ The Architecture Hub Guide: Technical Contracts as Code

## 1. Introduction
The Architecture Hub is not a static PDF. It is a live, version-controlled repository of **Technical Contracts**. It answers "HOW" the system works so developers don't have to guess.

**Core Principle:** Architecture is code. It lives in the repo, evolves with PRs, and is machine-readable.

---

## 2. The Hub Structure

The Architecture Hub consists of three pillars:
1.  **The WHAT (Visuals):** Diagrams that explain system structure and flow.
2.  **The HOW (Contracts):** Strict definitions of APIs and Data.
3.  **The RULES (Decisions):** Records of why we made certain choices (ADRs).

---

## 3. Pillar 1: The Diagrams (Visual Understanding)
We use "Diagrams as Code" to ensure documentation never goes stale.

| Diagram Type | Tool | Purpose |
| :--- | :--- | :--- |
| **System Structure** | Mermaid (C4) | **Context:** High-level logical blocks (App, API, Database). Shows boundaries. |
| **Cloud Anatomy** | Python Diagrams | **Infrastructure:** Physical resources (GCP Cloud Run, Pub/Sub, Firestore). Maps to Terraform. |
| **Data Structure** | DBML | **Schema:** Entity-Relationship Diagrams (ERD). Shows tables, keys, relationships. |
| **Logic Flow** | Mermaid Sequence | **Interaction:** Step-by-step service calls for complex features. |

---

## 4. Pillar 2: The Contracts (Implementation Specs)
These are legally binding for the codebase. Code must match contract.

### API Contracts (OpenAPI / gRPC)
*   **Format:** `openapi.yaml` or `.proto`
*   **Required:** All endpoints, request/response bodies, error codes (4xx/5xx).
*   **Usage:** Used to auto-generate client SDKs and mock servers for testing.

### Data Models (Schema)
*   **Format:** `schema.json` (Firestore), `models.sql` (SQL), or DBML.
*   **Required:** Field names, data types, nullability, foreign keys.
*   **Usage:** Used to validate data integrity and generate Typescript interfaces.

---

## 5. Pillar 3: The Rules (ADRs)
**Architecture Decision Records (ADRs)** explain the "Why".
*   **Format:** Markdown (`001-use-firestore.md`)
*   **Template:** Context, Decision, Consequences (Pros/Cons), Status (Accepted/Deprecated).

---

## 6. The AI Workflow (How to Execute)
1.  **Inputs:** PRD (Functional Requirements) + Tech Stack Rules.
2.  **Prompt:** *"Based on the requirement for [Feature X], generate a Mermaid Sequence Diagram showing the flow between the Frontend, API, and Database."*
3.  **Refine:** *"Update the diagram to handle the 409 Conflict error state."*
4.  **Contract:** *"Generate the OpenAPI spec YAML for the API endpoints defined in this sequence."*

---

## 7. Definition of Done (Architectural Readiness)
A feature is ready for the "Epic Breakdown" phase only when:
*   [ ] C4 Diagram updated.
*   [ ] ERD (DBML) updated with new entities.
*   [ ] OpenAPI spec defined for new endpoints.
*   [ ] Key flows mapped in Sequence Diagrams.
