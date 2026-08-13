# Synkra Architecture

**Version:** 0.1 (August 2026)  
**Status:** Living document — updated by multi-agent team

## 1. Product Context

Synkra is an operational MDM + data integrity platform focused on:
- Connector-driven ingestion of objects/classes from heterogeneous systems
- Semi-automatic attribute mapping
- Consistency audit
- Golden record unification with attribute-level survivorship
- Human conflict resolution via dedicated Jira project
- Continuous integrity monitoring + proactive alerts

## 2. High-Level Architecture

```
[Source Systems / DBs / APIs]
          │
          ▼
[Connectors Layer] ── Dockerized, Airbyte-CDK style, CDC capable
          │
          ▼
[Staging + Schema Registry]
          │
          ▼
[Mapping Engine] ── embeddings + LLM ranking + multi-agent + human review
          │
          ▼
[Entity Resolution] ── hybrid (rules + vectors + selective LLM) + graph context
          │
          ▼
[Golden Object Store] ── Postgres (JSONB/pgvector/temporal) ± Neo4j
          │
          ├──► [OpenMetadata Catalog]
          │
          ▼
[Temporal Workflows] ── deterministic orchestration of mapping, audit, conflict, monitoring
          │
          ├── Create/Update Jira Issue (conflict)
          ├── Signal from Jira webhook (resolution)
          └── Alerts + preventive recommendations
          │
          ▼
[Steward UI + Mapping Designer + Monitoring Dashboards] (Next.js)
```

## 3. Key Design Decisions (2026 Best Practices)

### 3.1 Deterministic Workflows (Temporal)
- All long-running and human-in-the-loop processes run as Temporal Workflows.
- Conflict resolution: durable wait on Signal from Jira webhook.
- Full event history provides audit trail.
- Escalation timers and retries are native.

### 3.2 Hybrid Entity Resolution
- High-confidence matches → deterministic rules
- Volume matching → vector embeddings (discriminative, high throughput)
- Ambiguous / semantic cases → selective LLM
- Survivorship is always **attribute-level** with source trust scoring, recency, completeness and full provenance.

### 3.3 Multi-Agent Layer
- Discovery Agent
- Mapping Suggestion Agent
- Conflict Triage Agent
- Preventive Analysis Agent
- Orchestrated via Temporal + multi-agent framework; non-deterministic LLM calls isolated as Activities.

### 3.4 Ontology & Knowledge
- Structured object/class/attribute ontology (structured-memory-ontology skill)
- Versioned, linked to OpenMetadata
- Used by agents and mapping engine for consistency.

## 4. Technology Choices

| Layer                    | Primary Choice                  | Alternatives / Notes                  |
|--------------------------|---------------------------------|---------------------------------------|
| Workflows                | Temporal.io                     | -                                     |
| Connectors               | Airbyte CDK + custom            | Singer, Meltano                       |
| Entity Resolution        | Splink + embeddings + rules     | Zingg, custom                         |
| Store                    | PostgreSQL + pgvector           | Neo4j for graphs                      |
| Catalog                  | OpenMetadata                    | DataHub                               |
| Observability            | OpenTelemetry + Prometheus      | -                                     |
| DQ Rules                 | Great Expectations / Soda       | -                                     |
| Frontend                 | Next.js                         | -                                     |
| Deployment               | Docker Compose → Kubernetes     | -                                     |

## 5. Security & Governance

- Credentials in secrets managers
- Full lineage and provenance on every golden attribute
- Role-based access for stewards
- Audit of all mapping decisions and conflict resolutions
- MCP servers (future) for controlled agent access

## 6. Evolution Path

1. MVP: connectors + Temporal conflict→Jira + basic golden store
2. Mapping engine + human review UI
3. Full multi-agent + ontology
4. Graph capabilities + advanced monitoring
5. MCP + external agent integration

---

Maintained collaboratively. Last major update: August 2026 (research on Temporal HITL, hybrid ER, agentic MDM).
