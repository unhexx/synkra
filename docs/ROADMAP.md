# Synkra Roadmap

**Goal:** Make the repository self-sufficient for autonomous agentic development loops.

## Phase 0 — Foundation (Current / Done)
- [x] Product vision & naming
- [x] README + ARCHITECTURE.md
- [x] Connectors base SDK (Airbyte-inspired)
- [x] Jira integration client
- [x] High-level stack decisions (Temporal, hybrid ER, attribute-level survivorship)

## Phase 1 — Runnable Skeleton (Priority for agents)
**INVEST tasks:**

1. **T-001** Docker Compose full local environment  
   - Temporal (server + UI) + PostgreSQL + Redis + OpenMetadata (or minimal)  
   - Acceptance: `docker compose up` starts all services; Temporal UI accessible.

2. **T-002** Temporal worker + ConflictDetectionWorkflow skeleton  
   - Workflow that detects conflict → calls CreateJiraIssueActivity → waits on Signal → applies resolution  
   - Acceptance: unit + integration test with mock Jira + Signal.

3. **T-003** Postgres schema for GoldenObject + AttributeHistory + Provenance  
   - Tables with temporal support or explicit history  
   - Acceptance: migration runs, basic CRUD works.

4. **T-004** MappingSuggestionWorkflow (multi-agent ready)  
   - Input: two schemas → output ranked attribute mappings + confidence  
   - Use embeddings + simple ranking first (LLM later).

## Phase 2 — Core Value
5. Human review UI stub (Next.js) for mapping proposals and conflict resolution  
6. Real connector examples (Postgres source + generic REST)  
7. Basic integrity monitoring rules (Great Expectations style)  
8. OpenMetadata integration for catalog

## Phase 3 — Agentic Maturity
9. Full multi-agent system (discovery, mapping, triage, preventive)  
10. MCP server for external agents  
11. Graph capabilities (Neo4j option)  
12. Production K8s manifests + GitOps

## How agents should work
- Always start from ROADMAP.md and AGENT_GUIDE.md
- Prefer small, testable PRs / commits
- Update this ROADMAP when completing tasks
- Use Temporal patterns for any long-running / HITL logic
- Keep attribute-level survivorship and full provenance as non-negotiable
