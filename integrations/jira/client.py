"""Minimal Jira Cloud REST client for Synkra conflict stewardship."""
import os
from typing import Any, Dict, Optional
import httpx
from pydantic import BaseModel

class JiraConfig(BaseModel):
    url: str = os.getenv("JIRA_URL", "")
    email: str = os.getenv("JIRA_EMAIL", "")
    token: str = os.getenv("JIRA_API_TOKEN", "")
    project_key: str = os.getenv("JIRA_PROJECT_KEY", "DATA")

class JiraClient:
    def __init__(self, config: Optional[JiraConfig] = None):
        self.config = config or JiraConfig()
        self.auth = (self.config.email, self.config.token)
        self.base = f"{self.config.url.rstrip('/')}/rest/api/3"

    def create_conflict_issue(self, summary: str, description: str, labels: list[str] = None, custom_fields: Dict = None) -> Dict[str, Any]:
        payload = {
            "fields": {
                "project": {"key": self.config.project_key},
                "summary": summary,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [{"type": "paragraph", "content": [{"type": "text", "text": description}]}]
                },
                "issuetype": {"name": "Task"},
                "labels": labels or ["data-conflict", "synkra"],
            }
        }
        if custom_fields:
            payload["fields"].update(custom_fields)
        with httpx.Client() as client:
            r = client.post(f"{self.base}/issue", json=payload, auth=self.auth)
            r.raise_for_status()
            return r.json()
