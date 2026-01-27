# UX Agent - User Guide

This guide explains how to use the **UX Agent** to generate User Personas and Wireframe descriptions from your PRD and User Stories.

---

## Capabilities

1.  **Generate Personas**: Creates detailed user personas based on the PRD's target audience.
2.  **Generate Wireframes**: Creates text-based wireframe descriptions (Mermaid/Text) for specific user stories.

---

## How to Run

### Option A: Terminal (Standard)

**Generate Personas:**
```bash
cd 03_UX_Design/ux_agent
python ux_agent.py --task personas --prd ../../01_Requirements/inputs/PRD.md --output outputs
```

**Generate Wireframes:**
```bash
cd 03_UX_Design/ux_agent
python ux_agent.py --task wireframes --story ../../02_Elaboration/outputs/stories/Story_Login.md --output outputs
```

### Option B: Gemini Slash Command

In Gemini Code Assist:
```
/ux-personas
/ux-wireframe
```

### Option C: Natural Language (MCP)

Ask Gemini:
> "Create user personas for this project."
> "Suggest a wireframe for the Login story."

---

## Artifacts Produced

-   `outputs/Personas.md`: Detailed profiles (Pain points, Goals, Bio).
-   `outputs/Wireframes.md`: Layout descriptions and Mermaid mockups.

---

## Authentication

```bash
gcloud auth application-default login
```
