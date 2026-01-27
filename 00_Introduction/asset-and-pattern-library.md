# 📚 Asset & Pattern Library

## 1. Introduction

This library serves as the **central index of reusable patterns, code snippets, prompts, and design components** used throughout the AI-Augmented SDLC. Rather than reinventing solutions, developers and AI agents reference this library to ensure consistency and accelerate delivery.

> "Don't build it again. Find the pattern, use the pattern, extend the pattern."

---

## 2. Architecture Patterns

Documented patterns for system architecture decisions.

### 2.1 Service Patterns

| Pattern | When to Use | Key Files |
|:--------|:------------|:----------|
| **Microservices** | Independent scaling, team autonomy | ADR template, C4 examples |
| **Event-Driven** | Async workflows, decoupled systems | Pub/Sub patterns, SAGA |
| **API Gateway** | Unified entry, auth, rate limiting | OpenAPI patterns |
| **BFF (Backend for Frontend)** | Mobile/Web specific APIs | Separation patterns |

### 2.2 Data Patterns

| Pattern | When to Use | Reference |
|:--------|:------------|:----------|
| **CQRS** | Read/write separation at scale | Event sourcing combo |
| **Event Sourcing** | Audit trail, temporal queries | Firestore/Pub/Sub example |
| **Repository Pattern** | Clean data access abstraction | Python/TS templates |
| **Unit of Work** | Transaction management | DB session handling |

### 2.3 Resilience Patterns

| Pattern | Implementation | Library |
|:--------|:---------------|:--------|
| **Circuit Breaker** | Fail fast, prevent cascade | `tenacity` (Python) |
| **Retry with Backoff** | Transient failure handling | exponential backoff |
| **Bulkhead** | Isolate failure domains | Thread/process pools |
| **Timeout** | Prevent hung operations | Request timeouts |

---

## 3. Code Patterns

Reusable code snippets and templates.

### 3.1 Error Handling

```python
# Standard error handling pattern
from rich.console import Console
console = Console()

def safe_operation(func):
    """Decorator for consistent error handling."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            console.print(f"[yellow]Validation error: {e}[/yellow]")
            return None
        except Exception as e:
            console.print(f"[red]Unexpected error: {e}[/red]")
            raise
    return wrapper
```

### 3.2 Retry Pattern

```python
import time
from functools import wraps

def retry(max_attempts=3, backoff_factor=2):
    """Retry with exponential backoff."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_attempts - 1:
                        wait = backoff_factor ** attempt
                        time.sleep(wait)
                    else:
                        raise
        return wrapper
    return decorator
```

### 3.3 Configuration Loading

```python
import os
from pathlib import Path

def load_config(config_name: str) -> dict:
    """Load config from environment or file."""
    env_value = os.getenv(config_name.upper())
    if env_value:
        return {"source": "env", "value": env_value}
    
    config_path = Path(__file__).parent / "config" / f"{config_name}.json"
    if config_path.exists():
        import json
        return {"source": "file", "value": json.loads(config_path.read_text())}
    
    raise ValueError(f"Config not found: {config_name}")
```

---

## 4. Prompt Registry

All AI prompts organized by phase.

### 4.1 Requirements Phase

| Prompt ID | Purpose | Location |
|:----------|:--------|:---------|
| `PRD_GEN` | Generate PRD from stakeholder input | `01_Requirements/prompts/` |
| `PRD_REFINE` | Refine PRD with 9 discovery tools | `01_Requirements/prompts/` |

### 4.2 Elaboration Phase

| Prompt ID | Purpose | Location |
|:----------|:--------|:---------|
| `EPIC_GEN` | Split PRD into Epics (SPIDR) | `02_Elaboration/prompts/` |
| `EPIC_ELAB` | Elaborate Epic (CRUD, State, Edge) | `02_Elaboration/prompts/` |
| `STORY_GEN` | Generate User Stories (BDD) | `02_Elaboration/prompts/` |

### 4.3 Architecture Phase

| Prompt ID | Purpose | Location |
|:----------|:--------|:---------|
| `ARCH_001` | C4 System Context Diagram | `04_Architecture/prompts/` |
| `ARCH_002` | DBML Data Model | `04_Architecture/prompts/` |
| `ARCH_003` | OpenAPI Spec | `04_Architecture/prompts/` |
| `ARCH_004` | Sequence Diagrams | `04_Architecture/prompts/` |
| `INT_DISCOVER` | Interface Discovery | `04_Architecture/prompts/` |
| `INT_SPEC` | Interface Specification | `04_Architecture/prompts/` |
| `INT_TEST` | Interface Contract Tests | `04_Architecture/prompts/` |

### 4.4 UX Phase

| Prompt ID | Purpose | Location |
|:----------|:--------|:---------|
| `UX_001` | User Personas | `03_UX_Design/prompts/` |
| `UX_002` | User Journeys | `03_UX_Design/prompts/` |
| `UX_003` | Wireframe Descriptions | `03_UX_Design/prompts/` |

### 4.5 Testing Phase

| Prompt ID | Purpose | Location |
|:----------|:--------|:---------|
| `TEST_GEN` | Test Plan from Stories | `06_Testing/prompts/` |
| `SIM_001` | Persona Simulation | `06_Testing/prompts/` |
| `LOAD_001` | Load Test Scripts | `06_Testing/prompts/` |
| `CHAOS_001` | Chaos Engineering | `06_Testing/prompts/` |

---

## 5. Agent Patterns

Reusable patterns for building AI agents.

### 5.1 Base Agent Structure

All agents inherit from `GenAIBaseAgent`:

```python
from genai_agent_base import GenAIBaseAgent

class MyAgent(GenAIBaseAgent):
    def __init__(self):
        super().__init__(system_instruction="...")
    
    def process(self, input_data: str) -> str:
        return self.generate(input_data)
```

### 5.2 HITL (Human-in-the-Loop) Pattern

For high-risk actions:

```python
def require_approval(action_name: str):
    """Require explicit human approval before proceeding."""
    console.print(f"[yellow]⚠️ APPROVAL REQUIRED: {action_name}[/yellow]")
    response = input("Type 'YES' to proceed: ")
    if response.upper() != 'YES':
        console.print("[red]Action cancelled.[/red]")
        return False
    return True
```

### 5.3 ADK Agent Communication

Agents use A2A protocol:

```python
# Agent must expose discovery endpoint
# Tools defined using MCP format
# State: Short-term (context window), Long-term (Vector Search)
```

---

## 6. Design System Components

UI component library for consistent interfaces.

| Component | Purpose | Variants |
|:----------|:--------|:---------|
| **Button** | Actions | Primary, Secondary, Danger |
| **Card** | Content containers | Elevated, Outlined |
| **Form** | User input | Text, Select, Checkbox |
| **Table** | Data display | Sortable, Paginated |
| **Modal** | Overlays | Dialog, Sheet |
| **Toast** | Notifications | Success, Error, Warning |

Reference: [`03_UX_Design/design-system-guide.md`](file:///Users/davidarthurs/Projects/AISDLC/03_UX_Design/design-system-guide.md)

---

## 7. Quick Reference

### Find Patterns By Need

| Need | Pattern | Section |
|:-----|:--------|:--------|
| "Handle API failures gracefully" | Circuit Breaker, Retry | §2.3, §3.2 |
| "Generate a new agent" | Base Agent Structure | §5.1 |
| "Find a prompt for X" | Prompt Registry | §4 |
| "Standard error handling" | Error Handling Pattern | §3.1 |
| "UI component for Y" | Design System | §6 |
| "High-risk action approval" | HITL Pattern | §5.2 |

---

## 8. Contributing

To add a new pattern:

1. Create a PR with the pattern documented
2. Include: When to use, Code example, Reference implementation
3. Add entry to appropriate section in this library
4. Link from relevant agent prompts
