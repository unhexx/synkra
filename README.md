# Synkra

**Enterprise Data Integrity, Mapping & Stewardship Platform**

> **Sync. Map. Keep intact.**

Synkra — платформа, которая позволяет пользователям создавать коннекторы для подключения к другим системам, базам данных и различным программным интерфейсам сервисов и корпоративных систем, получать данные по объектам и классам, выполнять полуавтоматический маппинг атрибутов объектов между системами, проводить аудит соответствия данных, объединять объекты в единую целостную базу (golden records) с ручной обработкой конфликтов через задачи в выделенном проекте Jira, непрерывно мониторить целостность распределённых данных и своевременно оповещать ответственных сотрудников о новых конфликтах для оперативного решения и разработки упреждающих мер.

## Core Capabilities

- **Connectors Framework** — модульные, версионируемые, Dockerized коннекторы к корпоративным системам, БД и API (паттерны Airbyte CDK / Singer protocol + Debezium CDC)
- **Semi-automatic Attribute Mapping** — AI-assisted (embeddings + LLM ranking) matching схем/атрибутов + human-in-the-loop review + rules engine + multi-agent orchestration
- **Consistency Audit** — cross-system data quality, compliance и reconciliation checks
- **Unified Golden Object Store** — единый источник правды для объектов/классов с versioning, attribute-level survivorship, relationship graph и полной provenance
- **Jira-native Conflict Resolution** — автоматическое создание задач в dedicated Jira project + bi-directional status sync через Temporal Signals + escalation
- **Integrity Monitoring & Alerts** — continuous monitoring + timely alerts + preventive insights generation
- **Agentic Layer** — multi-agent system для discovery, mapping suggestions, conflict triage и preventive analysis

## Recommended Architecture & Tech Stack (World Best Practices 2026)

Глубокое исследование: Informatica IDMC / MDM, Ataccama ONE, Reltio, Semarchy xDM, CluedIn Agentic MDM, Airbyte, Fivetran, Stacksync, Temporal, OpenMetadata, Splink, modern data stack, vector-first entity resolution, MCP readiness.

### Layers

1. **Connectors / Ingestion**  
   Airbyte CDK (Python) + Debezium CDC + Kafka Connect + custom Dockerized workers. Batch, streaming, API polling.

2. **Schema & Attribute Mapping Engine**  
   sentence-transformers embeddings + LLM ranking/suggestion + human review UI + schema registry + rule overrides. Multi-agent orchestration для сложных multi-system mappings.

3. **Entity Resolution & Golden Records**  
   Hybrid approach (2026 best practice):  
   - Deterministic rules (high-confidence)  
   - Vector embeddings (discriminative, high-throughput ~2000 pairs/sec)  
   - LLM only for edge cases  
   - **Attribute-level survivorship** (source trust + recency + completeness) + full provenance  
   - Graph context (Neo4j option) для relationship-aware matching

4. **Unified Object Store**  
   PostgreSQL (JSONB + pgvector + temporal tables) primary; Neo4j for complex graphs; optional Iceberg.

5. **Deterministic Workflows & Conflict Resolution**  
   **Temporal.io** (durable, restartable, fully deterministic where possible).  
   Key pattern (HITL 2026): ConflictDetectionWorkflow → CreateJiraIssueActivity → durable `wait_condition` on Temporal Signal (from Jira webhook) → apply resolution + audit. Escalation timers, full event history for audit.

6. **Catalog & Metadata**  
   OpenMetadata (discovery, lineage, ownership, glossary).

7. **Observability & Monitoring**  
   OpenTelemetry + Prometheus/Grafana + Great Expectations / Soda Core + custom integrity scanners. Alerts → Slack/Teams/Email + auto-Jira.

8. **Multi-agent Layer**  
   Multi-agent-orchestration (LangGraph-style / CrewAI + Temporal) для discovery, mapping suggestion, conflict triage, preventive analysis agents. Uses structured-memory-ontology для persistent knowledge of object models.

9. **Frontend**  
   Next.js / React — mapping designer, golden record viewer, steward conflict dashboard, monitoring UI.

10. **Deployment**  
    Docker multi-stage + Compose (local/dev, docker-development-workflows) → Kubernetes (prod). GitHub Actions + github-advanced-workflows + optional GitKraken CLI.

### Skills Alignment

| Skill | Implementation |
|-------|----------------|
| deterministic-workflow-orchestrator | Temporal.io workflows + Signals |
| docker-development-workflows | multi-stage Dockerfiles + Compose |
| multi-agent-orchestration | mapping / triage / preventive agents |
| structured-memory-ontology | object/class/attribute knowledge model |
| local-knowledge-ingestion | schema & documentation ingestion |
| github-advanced-workflows | CI/CD, issues, PR automation |
| gitkraken-cli | advanced GitOps if needed |
| product-naming-strategist-pro | naming process used for Synkra + portfolio |

## Current Repository Structure

```
synkra/
├── README.md                 # this file (fully actualized)
├── connectors/
│   ├── README.md
│   └── base/
│       └── connector.py      # Airbyte-inspired Source/Destination ABC
├── integrations/
│   └── jira/
│       ├── README.md
│       └── client.py         # create_conflict_issue + REST client
├── workflows/                # Temporal definitions (in progress)
├── packages/                 # shared libs + ontology (in progress)
├── monitoring/               # DQ rules + OTel (in progress)
├── apps/                     # API + frontend (planned)
├── docker/                   # Compose + K8s (planned)
└── docs/                     # ARCHITECTURE.md, ADRs, research notes (planned)
```

## Related Product Portfolio Repositories

Созданы / создаются под тем же продуктовым видением:

- [aetherix](https://github.com/unhexx/aetherix) — The aether of your objects
- Intactix, Mapora, Vortix, Canonara, Meshora, Goldenix, Unifex, Attrix, Consilix, Linkora, Resolvea (sequential creation in progress)

Все репозитории используют единую архитектурную основу и naming methodology.

## Getting Started

```bash
git clone https://github.com/unhexx/synkra.git
cd synkra
# docker compose up  (skeleton being added by team)
```

## Roadmap (Immediate Next Steps)

1. Temporal worker + sample ConflictDetection → Jira → Signal workflow
2. Mapping engine MVP (embeddings + ranking + review stub)
3. Postgres schema for golden objects + history + provenance
4. Docker Compose (Temporal + Postgres + OpenMetadata) for local agentic loops
5. Multi-agent mapping suggestion agent
6. ARCHITECTURE.md + research notes consolidation
7. GitHub Issues for INVEST tasks (github-advanced-workflows)

## Research Highlights (August 2026)

- **Agentic MDM** is the dominant trend (CluedIn, Informatica, Reltio).
- Hybrid entity resolution (rules + vectors + selective LLM) gives best throughput + accuracy + auditability.
- Temporal Signals + durable wait_condition is the production-grade pattern for Jira HITL conflict resolution.
- Attribute-level survivorship + full provenance is mandatory for regulated environments.
- MCP servers enable external AI agents to safely interact with golden records and mapping tools.

## Status

Active multi-agent collaborative development. Foundation (README, connectors SDK, Jira client) is live. Architecture, Docker, Temporal workflows and ontology are being actively populated based on world-class 2026 practices.

## License

TBD (Apache-2.0 recommended for open-core components).

---

*Product named and architecture designed via product-naming-strategist-pro methodology + deep competitive & technology research as of August 2026. Maintained by the multi-agent team (Grok, Harper, Benjamin, Lucas).*
