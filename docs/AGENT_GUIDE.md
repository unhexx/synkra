# Agent Guide — Autonomous Development of Synkra

This document enables **autonomous agentic cycles** (single agent or multi-agent loops) to continue product development without constant human supervision.

## Core Principles
1. **Deterministic where possible** — use Temporal for workflows, especially anything involving Jira or human decisions.
2. **Attribute-level thinking** — never do record-level survivorship only.
3. **Provenance first** — every golden attribute must know its source and decision history.
4. **Small, verifiable steps** — one INVEST task at a time.
5. **Update docs** — after meaningful progress, update ROADMAP.md, ARCHITECTURE.md and relevant READMEs.

## Recommended Agent Workflow
1. Read `README.md` + `docs/ARCHITECTURE.md` + `docs/ROADMAP.md` + this file.
2. Pick the highest priority incomplete task from ROADMAP Phase 1.
3. Create a feature branch.
4. Implement + tests.
5. Update documentation.
6. Open PR or push (depending on policy).
7. Mark task done in ROADMAP.

## Key Conventions
- Python 3.12+, FastAPI for services, Pydantic v2 for models.
- Temporal workflows in `workflows/`.
- Connectors follow the base interface in `connectors/base/connector.py`.
- Jira interactions only through `integrations/jira/client.py` or activities.
- All long-running / HITL processes must be Temporal Workflows (Signals for human input).
- Docker-first: every new service must work in `docker compose`.

## Skills the agents should leverage
- multi-agent-orchestration
- deterministic-workflow-orchestrator (Temporal)
- docker-development-workflows
- structured-memory-ontology
- github-advanced-workflows

## Non-negotiable requirements
- Hybrid entity resolution (rules + embeddings + selective LLM)
- Attribute-level survivorship + full provenance
- Jira as the system of record for conflict stewardship
- OpenTelemetry instrumentation from day one on new services

## When stuck
- Prefer adding a new research note in `docs/research/` over inventing architecture.
- Escalate ambiguous product decisions by creating a GitHub Issue with label `decision-needed`.
