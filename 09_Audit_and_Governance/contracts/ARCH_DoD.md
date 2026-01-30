# Definition of Done: Architecture Agent
**Agent ID:** `ARCHITECTURE_AGENT`
**Artifact:** System Architecture Document / C4 Diagrams

## 1. Completeness Checks (The Inventory)
*   [ ] **C4 Levels:** Are Context, Container, and Component diagrams present?
*   [ ] **Entity Integrity:** Does every Data Entity in the Data Dictionary map to a Database Table?
*   [ ] **Tech Stack:** Are all languages, frameworks, and databases explicitly chosen?

## 2. Quality Checks (The Standard)
*   [ ] **Scalability:** Is the strategy for scale (Vertical vs Horizontal) defined?
*   [ ] **Decision Provenance:** Are key decisions (e.g., "SQL vs NoSQL") logged with "Why"?
*   [ ] **Security:** Is the Data Flow analyzed for security risks (Trust Boundaries)?

## 3. Traceability Checks (The Red Thread)
*   [ ] **Component Links:** Do Architecture Components link to Epics/Stories?
*   [ ] **Diagram Tags:** `%% @implements EPIC-123` in Mermaid files.
