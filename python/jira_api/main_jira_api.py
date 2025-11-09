#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "requests>=2.31.0",
# ]
# ///

"""
JIRA API Python Example

This script demonstrates how to interact with JIRA's REST API using Python.
It covers common operations like authentication, fetching issues, creating issues,
updating issues, searching with JQL, and adding comments.
"""

import json
import requests
from typing import Dict, Any


class JiraClient:
    """A simple JIRA API client using requests library."""

    def __init__(self, base_url: str, email: str, api_token: str):
        """
        Initialize JIRA client with credentials.

        Args:
            base_url: JIRA instance URL (e.g., 'https://your-domain.atlassian.net')
            email: Your JIRA account email
            api_token: API token generated from JIRA account settings
        """
        self.base_url = base_url.rstrip('/')
        self.auth = (email, api_token)
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_issue(self, issue_key: str) -> Dict[str, Any]:
        """
        Fetch details of a specific JIRA issue.

        Args:
            issue_key: Issue key (e.g., 'PROJ-123')

        Returns:
            Dictionary containing issue details
        """
        url = f"{self.base_url}/rest/api/3/issue/{issue_key}"
        response = requests.get(url, headers=self.headers, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def create_issue(self, project_key: str, summary: str, description: str,
                     issue_type: str = "Task") -> Dict[str, Any]:
        """
        Create a new JIRA issue.

        Args:
            project_key: Project key (e.g., 'PROJ')
            summary: Issue summary/title
            description: Issue description
            issue_type: Type of issue (e.g., 'Task', 'Bug', 'Story')

        Returns:
            Dictionary containing created issue details
        """
        url = f"{self.base_url}/rest/api/3/issue"
        payload = {
            "fields": {
                "project": {"key": project_key},
                "summary": summary,
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [
                        {
                            "type": "paragraph",
                            "content": [
                                {"type": "text", "text": description}
                            ]
                        }
                    ]
                },
                "issuetype": {"name": issue_type}
            }
        }
        response = requests.post(url, headers=self.headers, auth=self.auth,
                                data=json.dumps(payload))
        response.raise_for_status()
        return response.json()

    def update_issue(self, issue_key: str, fields: Dict[str, Any]) -> None:
        """
        Update an existing JIRA issue.

        Args:
            issue_key: Issue key (e.g., 'PROJ-123')
            fields: Dictionary of fields to update
        """
        url = f"{self.base_url}/rest/api/3/issue/{issue_key}"
        payload = {"fields": fields}
        response = requests.put(url, headers=self.headers, auth=self.auth,
                               data=json.dumps(payload))
        response.raise_for_status()

    def search_issues(self, jql: str, max_results: int = 50) -> Dict[str, Any]:
        """
        Search for issues using JQL (JIRA Query Language).

        Args:
            jql: JQL query string
            max_results: Maximum number of results to return

        Returns:
            Dictionary containing search results
        """
        url = f"{self.base_url}/rest/api/3/search"
        params = {
            "jql": jql,
            "maxResults": max_results
        }
        response = requests.get(url, headers=self.headers, auth=self.auth,
                               params=params)
        response.raise_for_status()
        return response.json()

    def add_comment(self, issue_key: str, comment_text: str) -> Dict[str, Any]:
        """
        Add a comment to a JIRA issue.

        Args:
            issue_key: Issue key (e.g., 'PROJ-123')
            comment_text: Comment text to add

        Returns:
            Dictionary containing created comment details
        """
        url = f"{self.base_url}/rest/api/3/issue/{issue_key}/comment"
        payload = {
            "body": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {"type": "text", "text": comment_text}
                        ]
                    }
                ]
            }
        }
        response = requests.post(url, headers=self.headers, auth=self.auth,
                                data=json.dumps(payload))
        response.raise_for_status()
        return response.json()

    def get_project(self, project_key: str) -> Dict[str, Any]:
        """
        Get details of a specific project.

        Args:
            project_key: Project key (e.g., 'PROJ')

        Returns:
            Dictionary containing project details
        """
        url = f"{self.base_url}/rest/api/3/project/{project_key}"
        response = requests.get(url, headers=self.headers, auth=self.auth)
        response.raise_for_status()
        return response.json()


def demonstrate_jira_api():
    """Demonstrate various JIRA API operations."""

    # Configuration (replace with your actual credentials)
    # For security, use environment variables in production
    JIRA_URL = "https://your-domain.atlassian.net"
    EMAIL = "your-email@example.com"
    API_TOKEN = "your-api-token-here"

    print("=" * 70)
    print("JIRA API Python Example")
    print("=" * 70)

    # Initialize the JIRA client
    print("\n[1] Initializing JIRA client...")
    print(f"    Base URL: {JIRA_URL}")
    print(f"    Email: {EMAIL}")
    client = JiraClient(JIRA_URL, EMAIL, API_TOKEN)

    # Example 1: Get project details
    print("\n[2] Fetching project details...")
    try:
        project = client.get_project("DEMO")
        print(f"    Project Name: {project.get('name')}")
        print(f"    Project Key: {project.get('key')}")
        print(f"    Project Type: {project.get('projectTypeKey')}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 2: Get issue details
    print("\n[3] Fetching issue details...")
    try:
        issue = client.get_issue("DEMO-123")
        print(f"    Issue Key: {issue['key']}")
        print(f"    Summary: {issue['fields']['summary']}")
        print(f"    Status: {issue['fields']['status']['name']}")
        print(f"    Assignee: {issue['fields'].get('assignee', {}).get('displayName', 'Unassigned')}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 3: Search issues with JQL
    print("\n[4] Searching issues with JQL...")
    try:
        jql_query = "project = DEMO AND status = 'In Progress' ORDER BY created DESC"
        print(f"    JQL: {jql_query}")
        results = client.search_issues(jql_query, max_results=5)
        print(f"    Total found: {results['total']}")
        print(f"    Returned: {len(results['issues'])}")
        for idx, issue in enumerate(results['issues'], 1):
            print(f"    [{idx}] {issue['key']}: {issue['fields']['summary']}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 4: Create a new issue
    print("\n[5] Creating a new issue...")
    try:
        new_issue = client.create_issue(
            project_key="DEMO",
            summary="Test issue created via API",
            description="This issue was created using the JIRA REST API from Python.",
            issue_type="Task"
        )
        print(f"    Created issue: {new_issue['key']}")
        print(f"    Issue URL: {JIRA_URL}/browse/{new_issue['key']}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 5: Update an issue
    print("\n[6] Updating an issue...")
    try:
        client.update_issue("DEMO-123", {
            "summary": "Updated summary via API"
        })
        print("    Issue DEMO-123 updated successfully")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 6: Add a comment
    print("\n[7] Adding a comment to an issue...")
    try:
        comment = client.add_comment(
            "DEMO-123",
            "This comment was added via the JIRA REST API using Python."
        )
        print("    Comment added successfully")
        print(f"    Comment ID: {comment.get('id')}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    print("\n" + "=" * 70)
    print("API Operations Completed")
    print("=" * 70)
    print("\nNote: This is a demonstration. Replace credentials with actual values.")
    print("For production use:")
    print("  - Store credentials in environment variables")
    print("  - Use proper error handling")
    print("  - Implement retry logic for network failures")
    print("  - Add rate limiting to respect API quotas")


if __name__ == "__main__":
    demonstrate_jira_api()
