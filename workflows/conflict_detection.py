"""Temporal ConflictDetectionWorkflow skeleton (HITL via Jira Signal).

This is the canonical pattern for Synkra conflict resolution.
Agents should extend this rather than invent new HITL approaches.
"""
from datetime import timedelta
from temporalio import workflow, activity
from temporalio.common import RetryPolicy
from typing import Optional

with workflow.unsafe.imports_passed_through():
    from integrations.jira.client import JiraClient  # activity only

@activity.defn
async def create_jira_conflict_issue(summary: str, description: str, labels: list[str]) -> str:
    """Activity: create Jira issue and return issue key."""
    client = JiraClient()
    result = client.create_conflict_issue(summary, description, labels)
    return result["key"]

@workflow.defn
class ConflictDetectionWorkflow:
    def __init__(self):
        self.resolution: Optional[str] = None
        self.jira_key: Optional[str] = None

    @workflow.signal
    def resolve_conflict(self, resolution: str):
        """Called when Jira webhook / steward resolves the issue."""
        self.resolution = resolution

    @workflow.run
    async def run(self, conflict_payload: dict) -> dict:
        # 1. Create Jira issue
        self.jira_key = await workflow.execute_activity(
            create_jira_conflict_issue,
            args=[
                f"[Synkra] Conflict on {conflict_payload.get('object_id')}",
                str(conflict_payload),
                ["synkra", "data-conflict"],
            ],
            start_to_close_timeout=timedelta(seconds=30),
            retry_policy=RetryPolicy(maximum_attempts=3),
        )

        # 2. Durable wait for human resolution (or timeout)
        try:
            await workflow.wait_condition(
                lambda: self.resolution is not None,
                timeout=timedelta(days=7),
            )
        except TimeoutError:
            # escalation logic can go here
            return {"status": "escalated", "jira_key": self.jira_key}

        # 3. Apply resolution to golden store (activity)
        # await workflow.execute_activity(apply_resolution, ...)

        return {
            "status": "resolved",
            "jira_key": self.jira_key,
            "resolution": self.resolution,
        }
