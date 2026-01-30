---
id: {{ ID }}
type: System_Design
parent: {{ PARENT_ID }}
---
# System Design: {{ SYSTEM_NAME }}

## 1. Context (Level 1)
{{ CONTEXT_DESCRIPTION }}

## 2. Containers (Level 2)
*   [ ] **Web App:** ...
*   [ ] **API Service:** ...
*   [ ] **Database:** ...

## 3. Database Schema
```mermaid
erDiagram
    USER ||--o{ ORDER : places
```

## 4. API Contract
*   `GET /resource`: ...

## 5. Decision Records (ADRs)
*   **Decision:** ...
*   **Rationale:** ...
