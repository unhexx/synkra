# Further Project Development Planning — Agents, Orchestrator & Tools (2026 Best Practices)

**Initiated:** 2026-08-13

## 1. Recommended Multi-Agent Topology for Synkra

### Core Agents (to be implemented in Phase 3 / T-009)
1. **Orchestrator Agent** (Temporal + multi-agent-orchestration skill)  
   - Owns the high-level DAG of work  
   - Spawns specialist agents  
   - Handles retries, escalations, human-in-the-loop via Signals

2. **Design / Architecture Agent**  
   - Maintains ARCHITECTURE.md, ADRs, DATA_MODEL  
   - Reviews PRs for architectural fitness  
   - Proposes new design decisions

3. **Connector Agent**  
   - Implements and maintains connectors  
   - Discovers schemas  
   - Generates mapping candidates

4. **Mapping & Entity-Resolution Agent**  
   - Runs embeddings + ranking  
   - Applies / proposes survivorship rules  
   - Explains decisions

5. **Conflict / Stewardship Agent**  
   - Detects conflicts  
   - Creates and monitors Jira issues  
   - Applies resolutions back to golden store

6. **SRE / Observability Agent**  
   - Owns OTel, dashboards, alerting rules  
   - Detects degradation and opens issues

7. **GitOps / Release Agent**  
   - Manages Kustomize/Helm, Flux/Argo  
   - Creates release PRs and tags

8. **QA / Test Agent**  
   - Maintains and expands test suite  
   - Runs regression after every significant change

### Supporting Roles
- **Research Agent** — keeps up with 2026 MDM / data-integration best practices
- **Security / Compliance Agent** — provenance, access control, audit

## 2. Recommended Tools & Platforms (World Best Practices 2026)

| Domain | Recommended Tools |
|--------|-------------------|
| Orchestration | Temporal.io (already chosen) + LangGraph / CrewAI for multi-agent |
| GitOps | Flux CD (primary) or Argo CD |
| CI/CD | GitHub Actions + GHCR |
| Observability | OpenTelemetry + Prometheus + Grafana + Tempo |
| Schema / Catalog | OpenMetadata |
| Entity Resolution | Splink + sentence-transformers + selective LLM |
| UI | Next.js + shadcn/ui |
| Policy | Kyverno or OPA |
| Secrets | External Secrets Operator + Sealed Secrets |
| Local K8s | kind / k3d |
| MCP | Official MCP servers for tools exposure to external agents |
| Knowledge | structured-memory-ontology + vector store (pgvector) |

## 3. Next Planning Actions (for agents)
1. After T-001–T-004 close → create detailed agent interface contracts (OpenAPI or MCP tools)
2. Design Agent should produce first ADR set
3. Orchestrator Agent should own a “Synkra Delivery Workflow” that runs the full cycle
4. Continuously update this document and ROADMAP

## 4. Success Metrics for Agentic Maturity
- An agent can pick any open Phase 1/2 issue and close it with a green CI PR without human intervention
- A new version can be released and deployed to a production-like environment via pure GitOps
- Full conflict → Jira → resolution → golden store path is demonstrated end-to-end by agents
