# Synkra Product Roadmap

**Version:** 0.2  
**Last updated:** 2026-08-13  
**Status:** Living — maintained by multi-agent team for autonomous development cycles

This roadmap is written so that any agent (or human) can pick the next INVEST-sized task without additional context.

## Guiding Principles

- Prefer narrow, independently valuable, testable slices (INVEST).
- Every significant change produces evidence (tests, screenshots, logs, or .agent/ markers).
- Temporal workflows are the source of truth for long-running processes.
- Human judgment (via Jira) remains mandatory for conflict resolution.
- Docker Compose must always allow a full local agentic loop.

## Phase 0 — Foundation (Current)

**Goal:** Repository is agentic-ready; any competent agent can continue development.

- [x] Product vision & naming (product-naming-strategist-pro)
- [x] Core README + Architecture
- [x] Connectors base SDK (Airbyte-inspired)
- [x] Jira client for conflict issues
- [x] Initial docs package (ARCHITECTURE, ROADMAP, AGENT_GUIDE, DATA_MODEL)
- [ ] Docker Compose + local Temporal + Postgres stack
- [ ] First Temporal ConflictDetection → Jira → Signal workflow (skeleton)
- [ ] Basic golden object Postgres schema

## Phase 1 — MVP Integrity Loop (Target: 2–4 weeks of focused agent work)

**Outcome:** End-to-end conflict detection → Jira task → human resolution → golden store update works in local Compose.

### INVEST Tasks (ordered)

1. **TEMP-001** — Temporal worker skeleton + ConflictDetectionWorkflow that creates a Jira issue via existing client and waits for Signal.
2. **STORE-001** — Postgres schema for `golden_objects`, `golden_attributes`, `provenance`, `source_records` with temporal history support.
3. **DOCKER-001** — docker-compose.yml that brings up Postgres, Temporal, OpenMetadata (or lightweight substitute), and worker. One-command local start.
4. **INT-001** — Jira webhook receiver that sends Temporal Signal on issue resolution/status change.
5. **AUDIT-001** — Simple integrity scanner that compares two sources and produces conflict candidates.
6. **UI-001** — Minimal steward dashboard page that lists open conflicts (can be static or basic Next.js).

**Definition of Done for Phase 1:**  
Agent can run `docker compose up`, trigger a synthetic conflict, see a Jira issue created, resolve it in Jira, and observe the golden store updated with full provenance.

## Phase 2 — Mapping Engine

- Mapping suggestion agent (embeddings + ranking)
- Human review UI for proposed attribute mappings
- Rule engine + persistence of approved mappings
- Multi-system mapping campaigns orchestrated by Temporal

## Phase 3 — Multi-Agent & Ontology

- Full Discovery / Mapping Suggestion / Conflict Triage / Preventive agents
- structured-memory-ontology model of objects, classes, attributes, relationships
- Continuous learning from steward decisions
- MCP server exposing golden record lookup + mapping tools

## Phase 4 — Production Hardening

- Kubernetes manifests + GitOps
- Advanced monitoring & alerting
- Performance, security, multi-tenancy
- Reference connectors (Postgres, Salesforce, REST, one ERP)

## How Agents Should Use This Roadmap

1. Always read `docs/AGENT_GUIDE.md` first.
2. Pick the highest-priority open task in the current Phase that matches your capabilities.
3. Create a branch `feat/<task-id>-short-description`.
4. Implement narrowly, add evidence, open PR.
5. Update this ROADMAP (check the box or move task) only after merge.
6. If blocked, create a GitHub Issue with label `blocked` and clear description.

## Success Metrics (MVP)

- Time from conflict detection to Jira issue < 30s
- Steward can resolve in Jira and see golden record updated < 2 min
- Full local loop starts with one `docker compose up`
- 100% of golden attributes carry provenance

---

Maintained for autonomous agentic cycles. Update after every significant merge.
