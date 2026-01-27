# Epic Decomposition Agent - User Guide

This guide describes how to use the **Epic Decomposition Agent** to break down a PRD into well-sized Epics using the SPIDR methodology.

---

## Purpose

This agent takes a complete PRD and **splits it into Epics**. It focuses purely on *structure*—deciding how to divide the work—not on elaborating details.

**Input**: Approved PRD
**Output**: List of Epic shells with size estimates and dependencies

---

## Methodology: SPIDR

The agent uses **SPIDR** to decide how to split features:

| Letter | Strategy | Example |
| :--- | :--- | :--- |
| **S**pike | Separate research from implementation | "Research Payment Gateway" vs "Implement Payments" |
| **P**ath | Split by user paths | "Happy Path" vs "Error Handling" |
| **I**nterface | Split by platform or complexity | "Mobile" vs "Web" |
| **D**ata | Split by data types | "Local Data" vs "Synced Data" |
| **R**ules | Split by business logic | "Basic Validation" vs "Fraud Rules" |

---

## Quality Check: INVEST

After proposing Epics, the agent validates each against **INVEST**:

| Criterion | Question |
| :--- | :--- |
| **I**ndependent | Can this be worked on without waiting for others? |
| **N**egotiable | Is scope open to refinement? |
| **V**aluable | Does this deliver value to users? |
| **E**stimable | Can the team size this? |
| **S**mall | Does it fit in a release cycle? |
| **T**estable | Is there a clear "Done" criteria? |

---

## How to Run

### Step 1: Prepare Inputs
Ensure you have an approved PRD:
```
inputs/PRD.md
```

### Step 2: Run the Agent

**Option A: Terminal (Standard)**
```bash
cd 02_Elaboration/epic_decomposition_agent
python epic_decomposition_agent.py --prd ../inputs/PRD.md --output outputs
```

**Option B: Gemini Slash Command**
In Gemini Code Assist chat, type:
```
/epic-split
```

**Option C: Natural Language (MCP)**
Just ask Gemini:
> "Split this PRD into Epics using SPIDR."
> "Decompose requirements into features."

### Step 3: Review Output
The agent generates:
```
outputs/
└── epic_breakdown.md   # List of all proposed Epics
```

Each Epic includes:
- **Description**: What it delivers
- **SPIDR Justification**: Why it was split this way
- **INVEST Check**: Pass/Fail for each criterion
- **Dependencies**: Blockers
- **Size Estimate**: S/M/L/XL

---

## Example Output

```markdown
## EPIC-001: User Authentication (SSO)

### Description
Implement Single Sign-On authentication using corporate identity provider.

### SPIDR Justification
- Split by PATH: This covers only the "Happy Path" (successful login).
- Error handling (locked accounts, expired sessions) is in EPIC-002.

### INVEST Check
| Criterion | Pass/Fail | Notes |
|:---|:---|:---|
| Independent | ✓ Pass | No blockers |
| Negotiable | ✓ Pass | SSO provider TBD |
| Valuable | ✓ Pass | Enables secure access |
| Estimable | ✓ Pass | Team knows SSO |
| Small | ✓ Pass | 2-3 sprints |
| Testable | ✓ Pass | User can log in |

### Dependencies
- None

### Estimated Size
M (Medium)
```

---

## Next Step: Epic Elaboration

After decomposition, each Epic shell goes to the **Epic Elaboration Agent** to be fleshed out with:
- CRUD Analysis
- State Diagrams
- Decision Tables
- Edge Cases
- etc.

```bash
python ../epic_elaboration_agent/epic_elaboration_agent.py --epic outputs/EPIC-001.md
```

---

## Authentication

```bash
gcloud auth application-default login
```

Ensure `.env` contains:
```
GCP_PROJECT_ID=your-project-id
GCP_LOCATION=us-central1
```
