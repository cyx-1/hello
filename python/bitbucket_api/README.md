# Bitbucket Datacenter/Server API - Python Example

This example demonstrates how to interact with the Bitbucket Datacenter/Server REST API using Python.

## Requirements

- Python 3.10 or higher
- `requests` library (automatically installed via inline metadata)

## Running the Code

```bash
uv run python main_bitbucket_api.py
```

## Source Code Overview

### 1. API Client Class Definition (Lines 21-157)

```python
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
```

**Purpose**: This class encapsulates all Bitbucket API interactions. It initializes with server URL and credentials, setting up HTTP Basic Authentication for all subsequent requests.

### 2. HTTP Method Wrappers (Lines 49-68)

```python
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
```

**Purpose**: These private methods abstract HTTP operations, providing a consistent interface for GET, POST, PUT, and DELETE requests. They automatically handle JSON serialization and error checking.

### 3. Project Operations (Lines 71-86)

```python
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
```

**Output Reference** (Lines 272-285 in source, Output Lines 9-23):
```
======================================================================
  1. Project Operations
======================================================================

Creating sample project data structure:
  Project Key: DEMO
  Project Name: Demo Project
  Description: Demonstration project for API examples

API Call: POST /rest/api/1.0/projects
Request Body: {
  "key": "DEMO",
  "name": "Demo Project",
  "description": "Demonstration project for API examples",
  "public": false,
  "type": "NORMAL"
}
```

**Annotation**: The `create_project` method sends a POST request to create a new Bitbucket project. The API endpoint is `/rest/api/1.0/projects` and requires a unique project key, name, and optional description.

### 4. Repository Operations (Lines 88-106)

```python
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
```

**Output Reference** (Lines 294-310 in source, Output Lines 25-39):
```
======================================================================
  2. Repository Operations
======================================================================

Creating sample repository data:
  Repository: example-repo
  SCM Type: git
  Forkable: True

API Call: POST /rest/api/1.0/projects/DEMO/repos
Request Body: {
  "name": "example-repo",
  "scmId": "git",
  "forkable": true,
  "description": "Example repository for API demo"
}

API Call: GET /rest/api/1.0/projects/DEMO/repos?limit=25
```

**Annotation**: Repository operations are scoped within a project. The `create_repository` method specifies `scmId` as "git" (required) and sets the repository as forkable by default.

### 5. Branch Operations (Lines 108-119)

```python
def list_branches(self, project_key: str, repo_slug: str, limit: int = 25) -> dict:
    """List branches in a repository"""
    return self._get(
        f"/projects/{project_key}/repos/{repo_slug}/branches",
        params={"limit": limit}
    )

def get_default_branch(self, project_key: str, repo_slug: str) -> dict:
    """Get default branch"""
    return self._get(f"/projects/{project_key}/repos/{repo_slug}/default-branch")
```

**Output Reference** (Lines 317-328 in source, Output Lines 41-51):
```
======================================================================
  3. Branch Operations
======================================================================

Listing branches in repository:
API Call: GET /rest/api/1.0/projects/DEMO/repos/example-repo/branches

Example Branch Response:
  Branch: main
  Type: BRANCH
  Latest Commit: abc123def456
  Is Default: True
```

**Annotation**: Branch operations provide access to all branches in a repository. The response includes branch metadata such as display name, type, latest commit hash, and default branch status.

### 6. Commit Operations (Lines 121-145)

```python
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
```

**Output Reference** (Lines 335-349 in source, Output Lines 53-63):
```
======================================================================
  4. Commit Operations
======================================================================

Getting commit information:
API Call: GET /rest/api/1.0/projects/DEMO/repos/example-repo/commits

Example Commit Response:
  Commit ID: abc123d
  Author: Dave Chen <yexinchen@gmail.com>
  Message: Initial commit
```

**Annotation**: Commit operations allow you to retrieve commit history. The `until` parameter can be used to fetch commits up to a specific branch or commit hash. Responses include commit ID, author information, timestamp, and commit message.

### 7. Pull Request Operations (Lines 147-196)

```python
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
```

**Output Reference** (Lines 356-380 in source, Output Lines 65-90):
```
======================================================================
  5. Pull Request Operations
======================================================================

Creating a pull request:
  Title: Feature: Add new API endpoint
  From: refs/heads/feature-branch
  To: refs/heads/main

API Call: POST /rest/api/1.0/projects/DEMO/repos/example-repo/pull-requests
Request Body: {
  "title": "Feature: Add new API endpoint",
  "description": "This PR adds a new REST API endpoint for user management",
  "fromRef": {
    "id": "refs/heads/feature-branch",
    "repository": {
      "slug": "example-repo",
      "project": {
        "key": "DEMO"
      }
    }
  },
  "toRef": {
    "id": "refs/heads/main",
    "repository": {
      "slug": "example-repo",
      "project": {
        "key": "DEMO"
      }
    }
  }
}
```

**Annotation**: Pull requests require specifying source (`fromRef`) and target (`toRef`) branches with full repository context. The API supports filtering by state (OPEN, MERGED, DECLINED, ALL).

### 8. File Operations (Lines 198-220)

```python
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
```

**Output Reference** (Lines 387-399 in source, Output Lines 92-103):
```
======================================================================
  6. File Operations
======================================================================

Reading file content from repository:
  File: README.md
  Branch/Ref: main

API Call: GET /rest/api/1.0/projects/DEMO/repos/example-repo/browse/README.md?at=main

Example File Content Response:
  Lines returned: 3
  Content preview:
    # Example Repository
    This is a demo repository for Bitbucket API
```

**Annotation**: The `get_file_content` method retrieves file content from a specific branch or commit. The response is structured as an array of line objects, which are joined to reconstruct the file content.

### 9. Advanced Query Operations (Lines 406-424)

**Output Reference** (Output Lines 105-119):
```
======================================================================
  7. Advanced Query Operations
======================================================================

Query Parameters Examples:

a) Pagination:
   GET /rest/api/1.0/projects/DEMO/repos?start=0&limit=25
   - 'start': Starting index (default: 0)
   - 'limit': Max results per page (default: 25, max: 1000)

b) Filtering Pull Requests by State:
   GET /rest/api/1.0/projects/DEMO/repos/example-repo/pull-requests?state=OPEN
   - States: OPEN, MERGED, DECLINED, ALL

c) Searching Projects:
   GET /rest/api/1.0/projects?name=Demo&permission=PROJECT_ADMIN
   - Filter by name and permission level
```

**Annotation**: The Bitbucket API supports pagination using `start` and `limit` parameters. All list endpoints follow this pattern, allowing efficient retrieval of large datasets. State filtering is available for pull requests and other stateful resources.

## Key Concepts

### Authentication (Lines 257-268)

The API client uses HTTP Basic Authentication with either:
- Username and password
- Username and personal access token (recommended)

```python
base_url = "https://bitbucket.example.com"
username = "demo-user"
password = "demo-token"

client = BitbucketServerAPI(base_url, username, password)
```

### API Endpoint Structure

All endpoints follow the pattern: `/rest/api/1.0/{resource}/{identifier}`

Common endpoints (Output Lines 121-139):
```
Common Bitbucket Server API Endpoints:
  • Projects:      /rest/api/1.0/projects
  • Repositories:  /rest/api/1.0/projects/{projectKey}/repos
  • Branches:      /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/branches
  • Commits:       /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/commits
  • Pull Requests: /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/pull-requests
  • Files:         /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/browse/{path}

Authentication Methods:
  • HTTP Basic Auth (username + password)
  • Personal Access Tokens (recommended)
  • OAuth 2.0 (for third-party applications)

Best Practices:
  ✓ Use personal access tokens instead of passwords
  ✓ Implement proper error handling for production code
  ✓ Respect rate limits and use pagination for large datasets
  ✓ Store credentials in environment variables, not in code
  ✓ Use HTTPS for all API communications
```

## Complete Program Output

```
======================================================================
  Bitbucket Datacenter/Server API Demo
======================================================================

Configuration:
  Base URL: https://bitbucket.example.com
  Username: demo-user
  API Endpoint: https://bitbucket.example.com/rest/api/1.0

✓ Bitbucket API client initialized

======================================================================
  1. Project Operations
======================================================================

Creating sample project data structure:
  Project Key: DEMO
  Project Name: Demo Project
  Description: Demonstration project for API examples

API Call: POST /rest/api/1.0/projects
Request Body: {
  "key": "DEMO",
  "name": "Demo Project",
  "description": "Demonstration project for API examples",
  "public": false,
  "type": "NORMAL"
}

======================================================================
  2. Repository Operations
======================================================================

Creating sample repository data:
  Repository: example-repo
  SCM Type: git
  Forkable: True

API Call: POST /rest/api/1.0/projects/DEMO/repos
Request Body: {
  "name": "example-repo",
  "scmId": "git",
  "forkable": true,
  "description": "Example repository for API demo"
}

API Call: GET /rest/api/1.0/projects/DEMO/repos?limit=25

======================================================================
  3. Branch Operations
======================================================================

Listing branches in repository:
API Call: GET /rest/api/1.0/projects/DEMO/repos/example-repo/branches

Example Branch Response:
  Branch: main
  Type: BRANCH
  Latest Commit: abc123def456
  Is Default: True

======================================================================
  4. Commit Operations
======================================================================

Getting commit information:
API Call: GET /rest/api/1.0/projects/DEMO/repos/example-repo/commits

Example Commit Response:
  Commit ID: abc123d
  Author: Dave Chen <yexinchen@gmail.com>
  Message: Initial commit

======================================================================
  5. Pull Request Operations
======================================================================

Creating a pull request:
  Title: Feature: Add new API endpoint
  From: refs/heads/feature-branch
  To: refs/heads/main

API Call: POST /rest/api/1.0/projects/DEMO/repos/example-repo/pull-requests
Request Body: {
  "title": "Feature: Add new API endpoint",
  "description": "This PR adds a new REST API endpoint for user management",
  "fromRef": {
    "id": "refs/heads/feature-branch",
    "repository": {
      "slug": "example-repo",
      "project": {
        "key": "DEMO"
      }
    }
  },
  "toRef": {
    "id": "refs/heads/main",
    "repository": {
      "slug": "example-repo",
      "project": {
        "key": "DEMO"
      }
    }
  }
}

======================================================================
  6. File Operations
======================================================================

Reading file content from repository:
  File: README.md
  Branch/Ref: main

API Call: GET /rest/api/1.0/projects/DEMO/repos/example-repo/browse/README.md?at=main

Example File Content Response:
  Lines returned: 3
  Content preview:
    # Example Repository
    This is a demo repository for Bitbucket API

======================================================================
  7. Advanced Query Operations
======================================================================

Query Parameters Examples:

a) Pagination:
   GET /rest/api/1.0/projects/DEMO/repos?start=0&limit=25
   - 'start': Starting index (default: 0)
   - 'limit': Max results per page (default: 25, max: 1000)

b) Filtering Pull Requests by State:
   GET /rest/api/1.0/projects/DEMO/repos/example-repo/pull-requests?state=OPEN
   - States: OPEN, MERGED, DECLINED, ALL

c) Searching Projects:
   GET /rest/api/1.0/projects?name=Demo&permission=PROJECT_ADMIN
   - Filter by name and permission level

======================================================================
  Summary
======================================================================

Common Bitbucket Server API Endpoints:
  • Projects:      /rest/api/1.0/projects
  • Repositories:  /rest/api/1.0/projects/{projectKey}/repos
  • Branches:      /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/branches
  • Commits:       /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/commits
  • Pull Requests: /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/pull-requests
  • Files:         /rest/api/1.0/projects/{projectKey}/repos/{repoSlug}/browse/{path}

Authentication Methods:
  • HTTP Basic Auth (username + password)
  • Personal Access Tokens (recommended)
  • OAuth 2.0 (for third-party applications)

Best Practices:
  ✓ Use personal access tokens instead of passwords
  ✓ Implement proper error handling for production code
  ✓ Respect rate limits and use pagination for large datasets
  ✓ Store credentials in environment variables, not in code
  ✓ Use HTTPS for all API communications

======================================================================
  Demo completed successfully!
======================================================================
```

## Notes

- This is a demonstration script using mock data. In a production environment, replace the credentials with actual Bitbucket Server credentials.
- Store credentials securely using environment variables or a secrets management system.
- The Bitbucket Server REST API version used is 1.0, which is the stable API version for Bitbucket Datacenter/Server.
- Error handling in this example uses `raise_for_status()` which raises HTTPError for bad responses (4XX or 5XX).
- For production use, implement comprehensive error handling, retry logic, and rate limiting.
