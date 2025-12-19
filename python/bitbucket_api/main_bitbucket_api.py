#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "requests>=2.31.0",
# ]
# ///

"""
Bitbucket Datacenter/Server API Demo

This script demonstrates how to interact with Bitbucket Datacenter/Server REST API.
It covers common operations like projects, repositories, branches, pull requests, and commits.

Note: This is a demonstration script. In production, use environment variables for credentials
and implement proper error handling.
"""

import json
from typing import Optional
import requests
from requests.auth import HTTPBasicAuth


class BitbucketServerAPI:
    """Client for Bitbucket Datacenter/Server REST API"""

    def __init__(self, base_url: str, username: str, password: str):
        """
        Initialize Bitbucket Server API client

        Args:
            base_url: Bitbucket server URL (e.g., 'https://bitbucket.example.com')
            username: Username for authentication
            password: Password or personal access token
        """
        self.base_url = base_url.rstrip('/')
        self.api_base = f"{self.base_url}/rest/api/1.0"
        self.auth = HTTPBasicAuth(username, password)
        self.session = requests.Session()
        self.session.auth = self.auth

    def _get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        """Make GET request to API"""
        url = f"{self.api_base}{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def _post(self, endpoint: str, data: dict) -> dict:
        """Make POST request to API"""
        url = f"{self.api_base}{endpoint}"
        response = self.session.post(url, json=data)
        response.raise_for_status()
        return response.json()

    def _put(self, endpoint: str, data: dict) -> dict:
        """Make PUT request to API"""
        url = f"{self.api_base}{endpoint}"
        response = self.session.put(url, json=data)
        response.raise_for_status()
        return response.json()

    def _delete(self, endpoint: str) -> bool:
        """Make DELETE request to API"""
        url = f"{self.api_base}{endpoint}"
        response = self.session.delete(url)
        response.raise_for_status()
        return response.status_code == 204

    # Project Operations
    def list_projects(self, limit: int = 25) -> dict:
        """List all projects"""
        return self._get("/projects", params={"limit": limit})

    def get_project(self, project_key: str) -> dict:
        """Get project details"""
        return self._get(f"/projects/{project_key}")

    def create_project(self, key: str, name: str, description: str = "") -> dict:
        """Create a new project"""
        data = {
            "key": key,
            "name": name,
            "description": description
        }
        return self._post("/projects", data)

    # Repository Operations
    def list_repositories(self, project_key: str, limit: int = 25) -> dict:
        """List repositories in a project"""
        return self._get(f"/projects/{project_key}/repos", params={"limit": limit})

    def get_repository(self, project_key: str, repo_slug: str) -> dict:
        """Get repository details"""
        return self._get(f"/projects/{project_key}/repos/{repo_slug}")

    def create_repository(self, project_key: str, name: str, description: str = "") -> dict:
        """Create a new repository"""
        data = {
            "name": name,
            "scmId": "git",
            "forkable": True
        }
        if description:
            data["description"] = description
        return self._post(f"/projects/{project_key}/repos", data)

    # Branch Operations
    def list_branches(self, project_key: str, repo_slug: str, limit: int = 25) -> dict:
        """List branches in a repository"""
        return self._get(
            f"/projects/{project_key}/repos/{repo_slug}/branches",
            params={"limit": limit}
        )

    def get_default_branch(self, project_key: str, repo_slug: str) -> dict:
        """Get default branch"""
        return self._get(f"/projects/{project_key}/repos/{repo_slug}/default-branch")

    # Commit Operations
    def list_commits(
        self,
        project_key: str,
        repo_slug: str,
        limit: int = 25,
        until: Optional[str] = None
    ) -> dict:
        """List commits in a repository"""
        params = {"limit": limit}
        if until:
            params["until"] = until
        return self._get(
            f"/projects/{project_key}/repos/{repo_slug}/commits",
            params=params
        )

    def get_commit(self, project_key: str, repo_slug: str, commit_id: str) -> dict:
        """Get commit details"""
        return self._get(
            f"/projects/{project_key}/repos/{repo_slug}/commits/{commit_id}"
        )

    # Pull Request Operations
    def list_pull_requests(
        self,
        project_key: str,
        repo_slug: str,
        state: str = "OPEN",
        limit: int = 25
    ) -> dict:
        """List pull requests"""
        return self._get(
            f"/projects/{project_key}/repos/{repo_slug}/pull-requests",
            params={"state": state, "limit": limit}
        )

    def get_pull_request(
        self,
        project_key: str,
        repo_slug: str,
        pr_id: int
    ) -> dict:
        """Get pull request details"""
        return self._get(
            f"/projects/{project_key}/repos/{repo_slug}/pull-requests/{pr_id}"
        )

    def create_pull_request(
        self,
        project_key: str,
        repo_slug: str,
        title: str,
        from_ref: str,
        to_ref: str,
        description: str = ""
    ) -> dict:
        """Create a pull request"""
        data = {
            "title": title,
            "description": description,
            "fromRef": {
                "id": f"refs/heads/{from_ref}",
                "repository": {
                    "slug": repo_slug,
                    "project": {"key": project_key}
                }
            },
            "toRef": {
                "id": f"refs/heads/{to_ref}",
                "repository": {
                    "slug": repo_slug,
                    "project": {"key": project_key}
                }
            }
        }
        return self._post(
            f"/projects/{project_key}/repos/{repo_slug}/pull-requests",
            data
        )

    # File Operations
    def get_file_content(
        self,
        project_key: str,
        repo_slug: str,
        file_path: str,
        at_ref: str = "main"
    ) -> str:
        """Get file content from repository"""
        url = f"{self.api_base}/projects/{project_key}/repos/{repo_slug}/browse/{file_path}"
        params = {"at": at_ref}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        data = response.json()

        # Extract lines from response
        lines = data.get("lines", [])
        return "\n".join([line.get("text", "") for line in lines])


def print_section(title: str):
    """Print section header"""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def demo_with_mock_data():
    """
    Demonstration using mock API (for illustration purposes)

    In a real scenario, replace with actual Bitbucket Server credentials:
    - base_url: Your Bitbucket Server URL
    - username: Your username
    - password: Your password or personal access token
    """

    print_section("Bitbucket Datacenter/Server API Demo")

    # Example configuration (Line 257-260)
    base_url = "https://bitbucket.example.com"
    username = "demo-user"
    password = "demo-token"

    print("Configuration:")
    print(f"  Base URL: {base_url}")
    print(f"  Username: {username}")
    print(f"  API Endpoint: {base_url}/rest/api/1.0")

    # Initialize API client (Line 268)
    _client = BitbucketServerAPI(base_url, username, password)
    print("\n✓ Bitbucket API client initialized")

    # Example 1: Project Operations (Line 272-285)
    print_section("1. Project Operations")

    print("Creating sample project data structure:")
    project_data = {
        "key": "DEMO",
        "name": "Demo Project",
        "description": "Demonstration project for API examples",
        "public": False,
        "type": "NORMAL"
    }
    print(f"  Project Key: {project_data['key']}")
    print(f"  Project Name: {project_data['name']}")
    print(f"  Description: {project_data['description']}")

    # Example API endpoint
    print("\nAPI Call: POST /rest/api/1.0/projects")
    print(f"Request Body: {json.dumps(project_data, indent=2)}")

    # Example 2: Repository Operations (Line 294-310)
    print_section("2. Repository Operations")

    print("Creating sample repository data:")
    repo_data = {
        "name": "example-repo",
        "scmId": "git",
        "forkable": True,
        "description": "Example repository for API demo"
    }
    print(f"  Repository: {repo_data['name']}")
    print(f"  SCM Type: {repo_data['scmId']}")
    print(f"  Forkable: {repo_data['forkable']}")

    print("\nAPI Call: POST /rest/api/1.0/projects/DEMO/repos")
    print(f"Request Body: {json.dumps(repo_data, indent=2)}")

    # Example listing repositories
    print("\nAPI Call: GET /rest/api/1.0/projects/DEMO/repos?limit=25")

    # Example 3: Branch Operations (Line 317-328)
    print_section("3. Branch Operations")

    print("Listing branches in repository:")
    print("API Call: GET /rest/api/1.0/projects/DEMO/repos/example-repo/branches")

    # Sample branch data
    branch_data = {
        "displayId": "main",
        "type": "BRANCH",
        "latestCommit": "abc123def456",
        "isDefault": True
    }
    print("\nExample Branch Response:")
    print(f"  Branch: {branch_data['displayId']}")
    print(f"  Type: {branch_data['type']}")
    print(f"  Latest Commit: {branch_data['latestCommit']}")
    print(f"  Is Default: {branch_data['isDefault']}")

    # Example 4: Commit Operations (Line 335-349)
    print_section("4. Commit Operations")

    print("Getting commit information:")
    print("API Call: GET /rest/api/1.0/projects/DEMO/repos/example-repo/commits")

    # Sample commit data
    commit_data = {
        "id": "abc123def456",
        "displayId": "abc123d",
        "author": {
            "name": "Dave Chen",
            "emailAddress": "yexinchen@gmail.com"
        },
        "authorTimestamp": 1702998000000,
        "message": "Initial commit"
    }
    print("\nExample Commit Response:")
    print(f"  Commit ID: {commit_data['displayId']}")
    print(f"  Author: {commit_data['author']['name']} <{commit_data['author']['emailAddress']}>")
    print(f"  Message: {commit_data['message']}")

    # Example 5: Pull Request Operations (Line 356-380)
    print_section("5. Pull Request Operations")

    print("Creating a pull request:")
    pr_data = {
        "title": "Feature: Add new API endpoint",
        "description": "This PR adds a new REST API endpoint for user management",
        "fromRef": {
            "id": "refs/heads/feature-branch",
            "repository": {
                "slug": "example-repo",
                "project": {"key": "DEMO"}
            }
        },
        "toRef": {
            "id": "refs/heads/main",
            "repository": {
                "slug": "example-repo",
                "project": {"key": "DEMO"}
            }
        }
    }

    print(f"  Title: {pr_data['title']}")
    print(f"  From: {pr_data['fromRef']['id']}")
    print(f"  To: {pr_data['toRef']['id']}")

    print("\nAPI Call: POST /rest/api/1.0/projects/DEMO/repos/example-repo/pull-requests")
    print(f"Request Body: {json.dumps(pr_data, indent=2)}")

    # Example 6: File Operations (Line 387-399)
    print_section("6. File Operations")

    print("Reading file content from repository:")
    file_path = "README.md"
    ref = "main"
    print(f"  File: {file_path}")
    print(f"  Branch/Ref: {ref}")

    print(f"\nAPI Call: GET /rest/api/1.0/projects/DEMO/repos/example-repo/browse/{file_path}?at={ref}")

    # Sample file content response
    print("\nExample File Content Response:")
    print("  Lines returned: 3")
    print("  Content preview:")
    print("    # Example Repository")
    print("    This is a demo repository for Bitbucket API")

    # Example 7: Advanced Query Operations (Line 406-424)
    print_section("7. Advanced Query Operations")

    print("Query Parameters Examples:\n")

    # Pagination
    print("a) Pagination:")
    print("   GET /rest/api/1.0/projects/DEMO/repos?start=0&limit=25")
    print("   - 'start': Starting index (default: 0)")
    print("   - 'limit': Max results per page (default: 25, max: 1000)")

    # Filtering
    print("\nb) Filtering Pull Requests by State:")
    print("   GET /rest/api/1.0/projects/DEMO/repos/example-repo/pull-requests?state=OPEN")
    print("   - States: OPEN, MERGED, DECLINED, ALL")

    # Searching
    print("\nc) Searching Projects:")
    print("   GET /rest/api/1.0/projects?name=Demo&permission=PROJECT_ADMIN")
    print("   - Filter by name and permission level")

    # Summary (Line 431-437)
    print_section("Summary")

    print("Common Bitbucket Server API Endpoints:")
    print("  • Projects:      /rest/api/1.0/projects")
    print("  • Repositories:  /rest/api/1.0/projects/{projectKey}/repos")
    print("  • Branches:      /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/branches")
    print("  • Commits:       /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/commits")
    print("  • Pull Requests: /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/pull-requests")
    print("  • Files:         /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/browse/{path}")

    print("\nAuthentication Methods:")
    print("  • HTTP Basic Auth (username + password)")
    print("  • Personal Access Tokens (recommended)")
    print("  • OAuth 2.0 (for third-party applications)")

    print("\nBest Practices:")
    print("  ✓ Use personal access tokens instead of passwords")
    print("  ✓ Implement proper error handling for production code")
    print("  ✓ Respect rate limits and use pagination for large datasets")
    print("  ✓ Store credentials in environment variables, not in code")
    print("  ✓ Use HTTPS for all API communications")

    print("\n" + "=" * 70)
    print("  Demo completed successfully!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    # Run demonstration (Line 463)
    demo_with_mock_data()
