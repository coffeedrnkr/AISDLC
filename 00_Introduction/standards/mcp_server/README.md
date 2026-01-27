# Model Context Protocol (MCP) Server for Agents

This folder contains the **MCP Server** that exposes our local Python agents as tools to Gemini Code Assist.
This enables **Auto-Selection**: Gemini can decide to call these tools automatically based on conversation context.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Configure Gemini Code Assist**:
    Add this configuration to your **VS Code Settings** (`settings.json`) or **Gemini Config**:

    ```json
    "gemini.codeAssist.mcpServers": {
        "aisdlc-agents": {
            "command": "python",
            "args": [
                "/absolute/path/to/00_Introduction/standards/mcp_server/server.py"
            ]
        }
    }
    ```

## Available Tools

| Tool Name | Description | Agent Invoked |
| :--- | :--- | :--- |
| **`generate_prd_interactive`** | Start PRD discovery session | `01_Requirements/prd_agent.py` |
| **`decompose_prd_to_epics`** | Split PRD into Epics | `02_Elaboration/epic_decomposition_agent.py` |
| **`elaborate_epic_interactive`** | Start Epic elaboration session | `02_Elaboration/epic_elaboration_agent.py` |
| **`generate_user_stories`** | Create User Stories | `02_Elaboration/story_agent.py` |

## How it Works

1.  You type: *"I need to break down this PRD into epics."*
2.  Gemini analyzes the request.
3.  Gemini sees the `decompose_prd_to_epics` tool description matches your intent.
4.  Gemini **automatically runs** the tool (or asks for confirmation) without you needing to remember the path or command.
