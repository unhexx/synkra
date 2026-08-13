# Synkra Connectors SDK

Modular, versioned connectors for systems, databases, and APIs.

## Design Principles (best practices 2026)
- Inspired by Airbyte CDK / Singer protocol
- Dockerized workers for isolation
- Schema discovery + CDC support (Debezium patterns)
- Declarative config + extensible Python/Go base classes
- Observability via OpenTelemetry out of the box

## Structure
- `base/` — abstract Connector, Source, Destination interfaces
- `examples/` — reference connectors (Postgres, Salesforce, REST, Jira itself)
- `sdk/` — shared utilities, schema inference, rate limiting, auth helpers

## Quick Start
```bash
# Develop a new connector
cd connectors
python -m sdk.create_connector my_system
```

See ARCHITECTURE.md for integration with mapping engine and Temporal workflows.
