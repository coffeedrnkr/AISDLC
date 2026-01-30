import os
import requests
import json
import base64
from typing import Dict, List, Optional
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class JiraClient:
    """
    A specific wrapper for the Jira Cloud REST API v3.
    """
    def __init__(self):
        self.email = os.getenv("JIRA_EMAIL")
        self.token = os.getenv("JIRA_API_TOKEN")
        self.domain = os.getenv("JIRA_DOMAIN")  # e.g., "your-domain.atlassian.net"
        
        # Validation
        if not self.email or not self.token or not self.domain:
            print("⚠️  Jira Credentials missing in .env. Jira Sync will fail.")
            self.enabled = False
        else:
            self.enabled = True
            
        self.base_url = f"https://{self.domain}/rest/api/3"
        
        # Auth header
        if self.enabled:
            auth_str = f"{self.email}:{self.token}"
            self.auth_header = {
                "Authorization": f"Basic {base64.b64encode(auth_str.encode()).decode()}",
                "Content-Type": "application/json",
                "Accept": "application/json"
            }

    def _post(self, endpoint: str, data: Dict) -> Optional[Dict]:
        if not self.enabled: return None
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.post(url, headers=self.auth_header, json=data)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Jira POST Error ({endpoint}): {e}")
            if response: print(response.text)
            return None

    def _get(self, endpoint: str, params: Dict = None) -> Optional[Dict]:
        if not self.enabled: return None
        try:
            url = f"{self.base_url}/{endpoint}"
            response = requests.get(url, headers=self.auth_header, params=params)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"❌ Jira GET Error ({endpoint}): {e}")
            return None

    def create_issue(self, project_key: str, summary: str, description: str, issue_type: str, parent_key: str = None) -> Optional[str]:
        """Creates an issue and returns its KEY (e.g. PROJ-123)."""
        payload = {
            "fields": {
                "project": {"key": project_key},
                "summary": summary,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [{
                        "type": "paragraph",
                        "content": [{"type": "text", "text": description}] # Simplified for V3
                    }]
                },
                "issuetype": {"name": issue_type}
            }
        }
        
        if parent_key:
            # For Sub-tasks or Epic Links (Standard Jira Cloud structure)
            if issue_type == "Sub-task":
                 payload["fields"]["parent"] = {"key": parent_key}
            else:
                # Linking to Epic might vary by setup, but 'parent' field is standard in V3 for Team-Managed
                payload["fields"]["parent"] = {"key": parent_key} 

        response = self._post("issue", payload)
        if response:
            print(f"✅ Created Jira Issue: {response['key']}")
            return response['key']
        return None

    def link_issues(self, outward_key: str, inward_key: str, link_type: str = "Relates"):
        """Links two issues."""
        payload = {
            "type": {"name": link_type},
            "inwardIssue": {"key": inward_key},
            "outwardIssue": {"key": outward_key}
        }
        self._post("issueLink", payload)
        print(f"🔗 Linked {outward_key} -> {inward_key}")

    def search_issue(self, jql: str) -> List[Dict]:
        """Runs JQL and returns list of issues."""
        params = {"jql": jql, "fields": "key,summary,status"}
        response = self._get("search", params)
        if response and "issues" in response:
            return response["issues"]
        return []
