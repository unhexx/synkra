# Synkra Data Model (Golden Objects)

## Core Entities

### GoldenObject
- id (UUID)
- class_name / object_type (from ontology)
- version
- created_at / updated_at
- status (active, merged, deprecated)
- relationships (graph edges)

### AttributeValue (attribute-level)
- golden_object_id
- attribute_name
- value (JSONB)
- source_system
- source_record_id
- confidence / trust_score
- survivorship_rule_applied
- decided_at
- decided_by (rule / agent / human)
- provenance (full chain)

### MappingProposal
- source_schema_id / target_schema_id
- attribute_pairs + confidence
- status (proposed, accepted, rejected)
- proposed_by (agent)
- reviewed_by

### Conflict
- golden_object_id / attribute_name
- conflicting_values[]
- jira_issue_key
- status (open, resolved, escalated)
- resolution

### OntologyClass / OntologyAttribute
- versioned definitions of allowed classes and attributes
- used by mapping engine and agents

## Survivorship Policy (non-negotiable)
Survivorship is always decided **per attribute**, never only per record.
Priority factors (configurable):
1. Source system trust score
2. Recency
3. Completeness / validation status
4. Explicit business rules
5. Human override (via Jira)

Every decision is stored with full provenance.
