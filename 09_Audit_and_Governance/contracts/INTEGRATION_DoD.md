# Definition of Done: Integration Agent (CI/CD)
**Agent ID:** `INTEGRATION_AGENT`
**Artifact:** Build Pipeline / Release Manifest

## 1. Completeness Checks (The Inventory)
*   [ ] **Pipeline Config:** Valid `.github/workflows` or equivalent YAML?
*   [ ] **Stages:** Are Build, Test, and Deploy stages defined?
*   [ ] **Artifacts:** Are build artifacts (Docker images, JARs) generated?

## 2. Quality Checks (The Standard)
*   [ ] **Speed:** Is the critical path optimized (parallel jobs)?
*   [ ] **Resilience:** Are retries configured for flaky network steps?
*   [ ] **Rollback:** Is there a defined rollback step if Deploy fails?
*   [ ] **Release Notes:** Generated automatically from Epic/Story links?

## 3. Traceability Checks (The Red Thread)
*   [ ] **Commit Trace:** Do commit messages follow Conventional Commits (`feat: ...`) linking to Stories?
