# Development Guide

## Local Setup (target)
```bash
git clone https://github.com/unhexx/synkra.git
cd synkra
cp .env.example .env
docker compose up -d
# Temporal UI: http://localhost:8080
# API: http://localhost:8000
```

## Project Layout (target)
- `apps/api` — FastAPI gateway
- `apps/worker` — Temporal worker
- `connectors/` — connector SDK + implementations
- `workflows/` — Temporal workflow + activity definitions
- `packages/` — shared libraries (models, ontology, mapping)
- `integrations/` — Jira, OpenMetadata, etc.
- `docs/` — architecture, roadmap, agent guide, data model

## Coding Standards
- Type hints everywhere
- Pydantic models for all external data
- Activities must be idempotent
- Workflows must be deterministic (no random, no direct I/O, no non-deterministic imports inside workflow code)
- OpenTelemetry spans on every significant operation

## Testing Strategy
- Unit tests for activities and pure functions
- Temporal test environment for workflows
- Contract tests for connectors
- Integration tests with docker compose
