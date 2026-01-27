# Architecture Agent

The Architecture Agent is an "Active Agent" - a runnable Python utility that automates the creation of the system's technical blueprint.

## The Active Agent Pattern
Unlike passive chat bots, this agent runs as a script:
```bash
python3 architecture_agent.py
```
It reads the `PRD.md` and procedurally generates the 6 Pillars of the Architecture Hub.

## The 6 Pillars of Architecture
The agent generates artifacts covering these distinct areas:

1.  **Diagrams ("The What"):** Visual understanding (C4 Models via Mermaid, Infrastructure via Python Diagrams).
2.  **API Contracts ("The How"):** OpenAPI/Swagger specifications.
3.  **Data Models ("The How"):** Database schemas (DBML/SQL).
4.  **IAM & Security ("The Safe"):** Access control policies.
5.  **Governance ("The Safe"):** Compliance and privacy rules.
6.  **Resiliency ("The Scalable"):** Uptime and recovery strategies.

See `../../concepts/diagrams-as-code-guide.md` for details on the "Diagrams as Code" tools used.
