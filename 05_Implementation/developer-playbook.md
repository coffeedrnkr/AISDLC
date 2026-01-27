# 💻 The Developer Playbook: Mastering Agentic AI

> **The Paradigm Shift:** You're no longer typing code—you're orchestrating an AI collaborator that can read, write, and execute across your entire codebase.

---

## 1. The Agentic Mindset

### From Helper to Collaborator

| Traditional AI Assist | Agentic AI Collaboration |
|----------------------|--------------------------|
| "Write a function for X" | "Implement feature X across all needed files" |
| Copy/paste suggestions | Review and approve file changes |
| Single-turn Q&A | Multi-turn conversations with memory |
| You debug, AI explains | AI runs tests, proposes fixes, you approve |
| You manage context | AI understands your workspace |

### The Three Laws of Agentic Development

1. **Describe Intent, Not Steps**
   - ❌ "First create a file, then add imports, then..."
   - ✅ "Implement user authentication using our existing auth patterns"

2. **Verify, Don't Trust**
   - Review every file change before accepting
   - Run tests after AI modifications
   - Question decisions that seem off

3. **Feed Context Relentlessly**
   - The AI only knows what you show it
   - More context = better output
   - Stale context = wrong output

---

## 2. Context Mastery

### The Context Hierarchy

```
┌─────────────────────────────────────────────┐
│  1. Workspace Rules (.gemini/ folder)       │  ← Always Active
│     coding-standards.md, tech-stack.md      │
├─────────────────────────────────────────────┤
│  2. Conversation Context                    │  ← This Session
│     Files you've @mentioned, chat history   │
├─────────────────────────────────────────────┤
│  3. Active File Context                     │  ← Right Now
│     The file open in your editor            │
└─────────────────────────────────────────────┘
```

### Context Commands

| Command | When to Use | Example |
|---------|-------------|---------|
| `@workspace` | Codebase-wide questions | "Where is user auth handled?" |
| `@file.ts` | Focus on specific file | "Refactor this using @auth.service.ts pattern" |
| `@folder/` | Scope to directory | "Find all API routes in @routes/" |
| Fresh chat | Context is muddled | Start new session after ~30 turns |

### Context Loading Checklist

Before starting a task, ensure the AI knows:

- [ ] **The requirement** (Story, Epic, or PRD reference)
- [ ] **The patterns** (link to similar existing code)
- [ ] **The constraints** (tech stack, security requirements)
- [ ] **The tests** (expected behavior from Gherkin ACs)

**Pro Tip:** Open relevant files in tabs before chatting. Code Assist reads your open files.

---

## 3. The Development Workflow

### Phase 1: Understand (5 min)

```
Human: I'm working on [STORY-123]. Here's the requirement:
[Paste story details]

The related API contract is in @api/policies.yaml
Our existing pattern is in @services/quote.service.ts

Before we code, explain your understanding of what needs to be built.
```

**Why This Works:** Forces the AI to confirm understanding before acting. Catches misalignment early.

### Phase 2: Scaffold (Red)

```
Human: Scaffold the files needed for this feature.
Then generate failing tests based on this Gherkin:
[Paste acceptance criteria]
```

**Verify:**
- Check file structure makes sense
- Run tests → they should fail (Red)
- Review test assertions for correctness

### Phase 3: Implement (Green)

```
Human: Implement the feature to make all tests pass.
Follow the error handling pattern in @services/base.service.ts
```

**Verify:**
- Run tests → they should pass (Green)
- Review diff carefully (Cmd+D to see changes)
- Don't accept blindly—read the code

### Phase 4: Refactor

```
Human: Refactor for readability. Ensure:
- Function names are descriptive
- Error messages are user-friendly
- Matches patterns in .gemini/coding-standards.md
```

**Verify:**
- Tests still pass
- Code is cleaner, not just different

---

## 4. Prompt Patterns for Developers

### The Anatomy of a Good Prompt

```
[CONTEXT] - What does the AI need to know?
[TASK]    - What should it do?
[FORMAT]  - How should it respond?
[EXAMPLE] - What does good look like?
```

### Pattern Library

#### Implement Feature
```
Implement [feature name] that:
- Does X when Y happens
- Handles error case Z by [behavior]
- Follows the pattern in @services/existing.service.ts
- Uses [library/framework] for [reason]
```

#### Debug Issue
```
This code throws [error] when [condition].
Expected: [behavior]
Actual: [behavior]
Relevant logs: [paste]

Find the root cause, explain it, then propose a fix.
```

#### Refactor Code
```
Refactor this to:
- Extract [logic] into a separate function
- Match naming conventions in .gemini/coding-standards.md
- Improve testability by [approach]

Show me the before/after diff.
```

#### Write Tests
```
Generate tests for @file.ts that cover:
- Happy path: [scenario]
- Error case: [scenario]
- Edge case: [scenario]

Use Vitest and follow patterns in @__tests__/example.test.ts
```

### Anti-Patterns (Avoid These)

| ❌ Bad Prompt | ✅ Better Prompt |
|---------------|------------------|
| "Fix this" | "Fix the null pointer on line 42 when user is undefined" |
| "Make it work" | "Make the API return 400 with message 'Email required' when email is missing" |
| "Write tests" | "Write Vitest tests covering happy path, validation error, and timeout" |
| "Refactor this" | "Extract the validation logic into a validateUser() helper" |

---

## 5. The Trust Boundary

### When AI Hallucinates

The AI will confidently write code that:
- Calls APIs that don't exist
- Uses library methods that were deprecated
- Invents configuration options
- Misremembers function signatures

### Verification Checkpoints

| Change Type | Verification Level |
|-------------|-------------------|
| New file creation | Quick review |
| Modifying existing logic | Line-by-line review |
| Security-related code | Manual + security scan |
| Database migrations | Never auto-accept |
| Dependency changes | Check docs manually |

### The "Wait, Really?" Test

If the AI suggests something that seems too easy or too clever, pause:

```
Human: That solution seems simpler than expected. 
Are there edge cases I'm missing? 
What could go wrong with this approach?
```

### Red Flags to Watch For

⚠️ **Scope Creep:** AI adds features you didn't ask for
⚠️ **Silent Failures:** Changes that compile but break behavior
⚠️ **Over-Engineering:** Complex solutions for simple problems
⚠️ **Wrong Patterns:** Using a pattern that doesn't match your codebase

---

## 6. Recovery & Rollback

### When Things Go Wrong

#### Agent Made Too Many Changes
```bash
# Review what changed
git diff

# Revert all unstaged changes
git checkout .

# Or selectively revert
git checkout -- path/to/file.ts
```

#### Conversation Is Confused
- **Symptom:** AI references things incorrectly, repeats mistakes
- **Fix:** Start a fresh chat session, re-establish context

#### AI Is Stuck in a Loop
- **Symptom:** Same error, same "fix" repeated
- **Fix:** Stop. Describe the problem differently. Or solve it manually.

### The Escape Hatch

When AI can't solve it:

1. **Ask for explanation:** "Don't write code. Explain the problem and possible approaches."
2. **Search manually:** Stack Overflow, library docs
3. **Simplify scope:** Break the problem into smaller pieces
4. **Take a break:** Fresh perspective helps

---

## 7. The GCP Power Pair

### Tool Selection Guide

| Task | Tool | Why |
|------|------|-----|
| Write/edit code | **Code Assist** (IDE) | Has your codebase context |
| Run tests | **Terminal** | Direct feedback |
| Deploy to Cloud Run | **Gemini CLI** | Built-in deploy commands |
| Debug production | **Code Assist** + Logs | Explain errors with context |
| Create infrastructure | **Gemini CLI** | Terraform/gcloud integration |

### Daily Workflow Integration

```
Morning:
├── Pull latest changes
├── Open Code Assist chat
└── "What changed in yesterday's commits that affects my work?"

During Development:
├── @workspace "Find where user profiles are validated"
├── Implement feature with inline assist (Cmd+I)
├── Generate tests with chat
└── /review before committing

Deployment:
├── gemini /deploy (CLI)
└── Verify in Cloud Console
```

### Slash Commands Quick Reference

| Command | Purpose |
|---------|---------|
| `/doc` | Generate documentation for selection |
| `/explain` | Explain how code works |
| `/fix` | Propose fix for errors |
| `/test` | Generate unit tests |
| `/review` | Pre-commit code review |
| **`/prd-discover`** | **Run Interactive PRD Agent** |
| **`/epic-split`** | **Split PRD into Epics (SPIDR)** |
| **`/epic-elaborate`** | **Detailed Epic Elaboration** |
| **`/story-gen`** | **Generate User Stories** |


---

## 8. Quick Reference Card

### Starting a New Task
```
1. Open relevant files in IDE tabs
2. Start fresh chat if needed
3. Establish context: requirement + patterns + constraints
4. Ask AI to confirm understanding before coding
```

### Reviewing AI Changes
```
1. Read the diff (Cmd+D)
2. Check for scope creep
3. Verify patterns match codebase
4. Run tests before accepting
```

### When Stuck
```
1. Rephrase the problem
2. Break into smaller tasks
3. Ask AI to explain, not fix
4. Check docs manually
5. Start fresh chat
```

---

## Next Steps

Your code is written, tested, and reviewed. Time to verify quality gates:

👉 **[Quality & Testing Strategy Guide](quality-and-testing-strategy-guide.md)**
