# MCP Server for AI SDLC Agents
# Wraps local Python agents as MCP Tools for Gemini Code Assist

import os
import sys
import asyncio
import subprocess
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("AI-SDLC-Agents")

# Paths to Agents
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
PRD_AGENT_SCRIPT = os.path.join(BASE_DIR, "01_Requirements/prd_agent/prd_agent.py")
DECOMP_AGENT_SCRIPT = os.path.join(BASE_DIR, "02_Elaboration/epic_decomposition_agent/epic_decomposition_agent.py")
ELAB_AGENT_SCRIPT = os.path.join(BASE_DIR, "02_Elaboration/epic_elaboration_agent/epic_elaboration_agent.py")
STORY_AGENT_SCRIPT = os.path.join(BASE_DIR, "02_Elaboration/story_agent/story_agent.py")

@mcp.tool()
async def generate_prd_interactive(input_dir: str = "inputs", output_dir: str = "outputs") -> str:
    """
    Run the PRD Discovery Agent in Interactive Mode.
    Use this when the user needs to generate a new Product Requirements Document (PRD) 
    from raw notes, or needs help discovering requirements.
    """
    cmd = [sys.executable, PRD_AGENT_SCRIPT, "--interactive", "--input", input_dir, "--output", output_dir]
    try:
        # We run interactive agents in a new terminal window for user interaction
        # Note: This is a platform-specific (MacOS) conceptual implementation for "Interactive" tools
        subprocess.Popen(["open", "-a", "Terminal", "."] + cmd) 
        return "Launched PRD Agent in a new terminal window for interactive session."
    except Exception as e:
        return f"Error launching agent: {e}"

@mcp.tool()
async def decompose_prd_to_epics(prd_path: str, output_dir: str = "outputs") -> str:
    """
    Split a PRD into Epics using SPIDR methodology.
    Use this when the user has a PRD and needs to break it down into high-level features/epics.
    """
    cmd = [sys.executable, DECOMP_AGENT_SCRIPT, "--prd", prd_path, "--output", output_dir]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return f"Encoposition Complete.\nOutput:\n{result.stdout}"
    else:
        return f"Error decomposing PRD:\n{result.stderr}"

@mcp.tool()
async def elaborate_epic_interactive(epic_path: str) -> str:
    """
    Run the Epic Elaboration Agent (9 Discovery Tools).
    Use this when the user wants to flesh out specific details of an Epic (CRUD, State diagrams, etc.).
    """
    cmd = [sys.executable, ELAB_AGENT_SCRIPT, "--epic", epic_path, "--interactive"]
    try:
         subprocess.Popen(["open", "-a", "Terminal", "."] + cmd)
         return f"Launched Epic Elaboration for {os.path.basename(epic_path)} in terminal."
    except Exception as e:
        return f"Error launching agent: {e}"

@mcp.tool()
async def generate_user_stories(epic_path: str, arch_path: str, output_dir: str = "outputs") -> str:
    """
    Generate User Stories from a fully elaborated Epic.
    Use this when the Epic is ready and needs to be broken down into dev-ready stories.
    """
    cmd = [sys.executable, STORY_AGENT_SCRIPT, "--epic", epic_path, "--arch", arch_path, "--output", output_dir]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout + result.stderr

if __name__ == "__main__":
    mcp.run()
