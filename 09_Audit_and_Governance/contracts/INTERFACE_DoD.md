# Definition of Done: Interface Agent
**Agent ID:** `INTERFACE_AGENT`
**Artifact:** API Specification / Contract

## 1. Completeness Checks (The Inventory)
*   [ ] **Endpoint Definition:** Are Method (GET/POST), Path (`/api/v1/...`), and Status Codes (200, 400, 500) defined?
*   [ ] **Payload Definition:** Are Request and Response bodies fully specified (JSON Schema)?
*   [ ] **Coverage:** Does every Backend Component in the Architecture have defined Interfaces?

## 2. Quality Checks (The Standard)
*   [ ] **Restful Standards:** Do paths use nouns (not verbs)? e.g., `/users` not `/getUsers`.
*   [ ] **Security:** Is Authentication (AuthZ/AuthN) specified for the endpoint?
*   [ ] **Idempotency:** Are generally safe methods (GET) actually safe?

## 3. Traceability Checks (The Red Thread)
*   [ ] **Parent Link:** Does the spec link to the Architecture Component and Story?
*   [ ] **Tagging:** `description: "@implements STORY-123"` in Swagger/OpenAPI.
