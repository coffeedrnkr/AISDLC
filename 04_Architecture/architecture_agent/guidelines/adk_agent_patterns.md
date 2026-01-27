# Architecture Standard: Agent Development Kit (ADK) Patterns
**Status:** Draft
**Last Updated:** 2025-12-10

## 1. Agent Communication
### 1.1 Protocol
-   All AI Agents must implement the **Agent-to-Agent (A2A)** protocol v0.3.
-   Agents must expose a `discovery` endpoint.

### 1.2 Tool Definition
-   Tools must be defined using the **Model Context Protocol (MCP)** format.
-   Each tool must have a clear schema for `input` and `output`.

## 2. State Management
-   **Short-term Memory**: Context window of the LLM.
-   **Long-term Memory**: Must use Vector Search (Vertex AI Vector Search) for knowledge retrieval.
    -   Embeddings: `text-embedding-gecko` or newer.

## 3. Evaluation
-   All Agents must have a corresponding **Evaluation Dataset** (Golden Set).
-   Performance must be measured using "Antigravity Evaluation" framework before deployment.
