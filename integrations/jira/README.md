# Jira Integration for Conflict Resolution

Automatic creation of tasks in a dedicated Jira project when data conflicts are detected.

## Features
- Create Issue on conflict (with object IDs, attribute diffs, source systems, severity)
- Bi-directional status sync via webhooks + Temporal signals
- Custom fields for golden record link, mapping version, steward assignment
- Preventive recommendations as comments / linked issues

## Configuration
JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN, JIRA_PROJECT_KEY (env or secrets)

## Temporal Workflow Integration
ConflictDetectionWorkflow → CreateJiraIssueActivity → await resolution signal → update golden record + audit log.

See /workflows for full deterministic workflow definitions.
