# Synkra Roadmap

**Last updated:** 2026-08-13  
**Goal:** Self-sufficient repository for autonomous agentic development loops with full delivery to production.

## Timebox Legend
- **Target Start** / **Target Done** based on current date 2026-08-13
- Estimates assume parallel multi-agent work

## Phase 0 — Foundation (Done)
- [x] Product vision & naming — Done 2026-08-13
- [x] README + ARCHITECTURE.md — Done 2026-08-13
- [x] Connectors base SDK — Done 2026-08-13
- [x] Jira integration client — Done 2026-08-13
- [x] High-level stack decisions — Done 2026-08-13

## Phase 1 — Runnable Skeleton (P0)
**Overall Target:** 2026-08-15 → 2026-08-20

| ID | Task | Target Start | Target Done | Est. Effort | Status |
|----|------|--------------|-------------|-------------|--------|
| T-001 | Docker Compose full local environment (Temporal + Postgres + Redis) | 2026-08-13 | 2026-08-14 | 4h | In progress (#1) |
| T-002 | Temporal worker + complete ConflictDetectionWorkflow (HITL + Jira Signal) | 2026-08-14 | 2026-08-16 | 1–2d | Open |
| T-003 | Postgres schema + migrations (GoldenObject + AttributeHistory + Provenance) | 2026-08-14 | 2026-08-16 | 1d | Open |
| T-004 | MappingSuggestionWorkflow (embeddings + ranking) | 2026-08-16 | 2026-08-18 | 1–2d | Open |

## Phase 2 — Core Value
**Overall Target:** 2026-08-18 → 2026-08-28

| ID | Task | Target Start | Target Done | Est. Effort |
|----|------|--------------|-------------|-------------|
| T-005 | Human review UI stub (Next.js) | 2026-08-18 | 2026-08-22 | 2–3d |
| T-006 | Real connectors (Postgres source + generic REST) | 2026-08-19 | 2026-08-23 | 2d |
| T-007 | Integrity monitoring rules (Great Expectations / Soda) | 2026-08-21 | 2026-08-25 | 1–2d |
| T-008 | OpenMetadata integration | 2026-08-22 | 2026-08-26 | 2d |

## Phase 3 — Production & Agentic Maturity
**Overall Target:** 2026-08-25 → 2026-09-10

| ID | Task | Target Start | Target Done | Est. Effort |
|----|------|--------------|-------------|-------------|
| T-009 | Full multi-agent system (discovery / mapping / triage / preventive) | 2026-08-25 | 2026-09-02 | 4–5d |
| T-010 | MCP server for external agents | 2026-08-28 | 2026-09-03 | 2d |
| T-011 | Graph capabilities (Neo4j option) | 2026-09-01 | 2026-09-05 | 2d |
| T-012 | Production K8s manifests + GitOps | 2026-08-26 | 2026-09-05 | 3d |
| T-013 | Full CI/CD + release + production deploy of new version | 2026-09-01 | 2026-09-10 | 3–4d |

## How agents should work
- Always start from this ROADMAP.md and docs/AGENT_GUIDE.md
- Prefer small, testable PRs / commits
- Update this ROADMAP (checkboxes + actual dates) when completing tasks
- Use Temporal patterns for any long-running / HITL logic
- Keep attribute-level survivorship and full provenance as non-negotiable
