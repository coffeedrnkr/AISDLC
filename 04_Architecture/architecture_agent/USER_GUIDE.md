# Architecture Agent - User Guide

This guide explains how to use the **Architecture Agent** to transform an approved PRD into a complete "Architecture Hub" (Diagrams, API Specs, ADRs).

## Configuration: Architecture Guidelines

The agent uses **Architecture Guidelines** to ensure the generated design complies with your organization's standards (e.g., "Always use Cloud Run", "Enforce A2A Protocol").

### 1. Default Guidelines (Local)
We have provided sample guidelines in the `guidelines/` directory:
-   `google_cloud_standards.md`: Defines preferred GCP services.
-   `adk_agent_patterns.md`: Defines patterns for Agentic development.

**Action**: Review and edit these files to match your actual standards before running the agent.

### 2. Integration with Confluence (Future State)
The agent is designed to eventually pull these guidelines directly from Confluence.
*   **Developers**: Review `architecture_agent.py` method `load_guidelines()` for detailed code comments on how to implement the Confluence API v2 integration.
*   **BAs/Architects**: Ensure your guidelines in Confluence are kept up-to-date.

---

## How to Run

### Step 1: Prepare Inputs
1.  Ensure you have your **Approved PRD** (e.g., from the PRD Agent).
2.  Ensure your **Guidelines** are in the `guidelines/` folder.

### Step 2: Execute

**Option A: Terminal (Standard)**
```bash
cd 04_Architecture/architecture_agent
python architecture_agent.py --prd ../../01_Requirements/inputs/PRD.md --output outputs
```

**Option B: Gemini Slash Command**
```
/arch-design
```

**Option C: Natural Language (MCP)**
> "Generate system architecture for this PRD."
> "Create a DBML schema."

### Step 3: Review Outputs
Navigate to the output directory. You will find:

1.  **`diagrams/`**:
    -   `system-context.md`: Mermaid C4 Context diagram.
    -   `container-view.md`: Mermaid C4 Container diagram.
    *   *Tip*: View these using the [Mermaid Live Editor](https://mermaid.live/) or a VS Code extension.

2.  **`adrs/`**:
    -   `generated_adrs.md`: List of key architectural decisions (e.g., "Use Firestore vs SQL") with rationale.

3.  **`api-contracts/`**:
    -   `main-api.yaml`: Draft OpenAPI Specification for your services.

---

## Iteration
If the architecture doesn't fit (e.g., it chose SQL but you wanted NoSQL):
1.  **Don't just edit the output**.
2.  **Edit the Guideline**: Update `google_cloud_standards.md` to say "Prefer NoSQL for this type of app".
3.  **Re-Run**: Run the agent again. It will respect the new guideline.
