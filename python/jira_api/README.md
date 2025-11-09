# JIRA API Python Example

This example demonstrates how to interact with JIRA's REST API using Python and the `requests` library.

## Prerequisites

- Python 3.9 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- A JIRA instance (Cloud or Server)
- JIRA API credentials (email and API token)

## Running the Example

```bash
uv run python main_jira_api.py
```

The script uses inline script metadata (PEP 723) for dependency management, so `uv` will automatically install the required `requests` library.

## Source Code Overview

### Key Components

#### 1. JiraClient Class (Lines 22-166)

The `JiraClient` class encapsulates all JIRA API interactions:

```python
22: class JiraClient:
23:     """A simple JIRA API client using requests library."""
24:
25:     def __init__(self, base_url: str, email: str, api_token: str):
26:         """
27:         Initialize JIRA client with credentials.
...
31:         self.base_url = base_url.rstrip('/')
32:         self.auth = (email, api_token)
33:         self.headers = {
34:             'Accept': 'application/json',
35:             'Content-Type': 'application/json'
36:         }
```

**Lines 25-36**: The constructor initializes the client with:
- `base_url`: Your JIRA instance URL (e.g., `https://your-domain.atlassian.net`)
- `email`: Your JIRA account email
- `api_token`: API token (generated from JIRA account settings → Security → API Tokens)
- **Line 32**: Uses HTTP Basic Authentication with email and API token
- **Lines 33-36**: Sets JSON headers for all requests

#### 2. Get Issue Details (Lines 38-49)

```python
38:     def get_issue(self, issue_key: str) -> Dict[str, Any]:
39:         """
40:         Fetch details of a specific JIRA issue.
...
46:         url = f"{self.base_url}/rest/api/3/issue/{issue_key}"
47:         response = requests.get(url, headers=self.headers, auth=self.auth)
48:         response.raise_for_status()
49:         return response.json()
```

**Line 46**: Constructs the endpoint URL using JIRA REST API v3
**Line 47**: Makes a GET request with authentication and headers
**Line 48**: Raises an exception for HTTP error responses (4xx, 5xx)
**Line 49**: Parses and returns the JSON response

#### 3. Create Issue (Lines 51-82)

```python
51:     def create_issue(self, project_key: str, summary: str, description: str,
52:                      issue_type: str = "Task") -> Dict[str, Any]:
...
59:         url = f"{self.base_url}/rest/api/3/issue"
60:         payload = {
61:             "fields": {
62:                 "project": {"key": project_key},
63:                 "summary": summary,
64:                 "description": {
65:                     "type": "doc",
66:                     "version": 1,
67:                     "content": [
68:                         {
69:                             "type": "paragraph",
70:                             "content": [
71:                                 {"type": "text", "text": description}
72:                             ]
73:                         }
74:                     ]
75:                 },
76:                 "issuetype": {"name": issue_type}
77:             }
78:         }
79:         response = requests.post(url, headers=self.headers, auth=self.auth,
80:                                 data=json.dumps(payload))
81:         response.raise_for_status()
82:         return response.json()
```

**Lines 64-75**: JIRA Cloud uses Atlassian Document Format (ADF) for rich text fields
**Lines 68-73**: Creates a simple paragraph with text content
**Line 76**: Specifies the issue type (Task, Bug, Story, etc.)
**Line 79-80**: POSTs the JSON payload to create the issue

#### 4. Update Issue (Lines 84-96)

```python
84:     def update_issue(self, issue_key: str, fields: Dict[str, Any]) -> None:
...
91:         url = f"{self.base_url}/rest/api/3/issue/{issue_key}"
92:         payload = {"fields": fields}
93:         response = requests.put(url, headers=self.headers, auth=self.auth,
94:                                data=json.dumps(payload))
95:         response.raise_for_status()
```

**Line 92**: Wraps the fields to update in a `fields` object
**Line 93**: Uses PUT request to update the issue

#### 5. Search with JQL (Lines 98-115)

```python
98:     def search_issues(self, jql: str, max_results: int = 50) -> Dict[str, Any]:
99:         """
100:         Search for issues using JQL (JIRA Query Language).
...
107:         url = f"{self.base_url}/rest/api/3/search"
108:         params = {
109:             "jql": jql,
110:             "maxResults": max_results
111:         }
112:         response = requests.get(url, headers=self.headers, auth=self.auth,
113:                                params=params)
114:         response.raise_for_status()
115:         return response.json()
```

**Lines 108-111**: Passes JQL query and result limit as URL parameters
**Example JQL**: `"project = DEMO AND status = 'In Progress' ORDER BY created DESC"`

#### 6. Add Comment (Lines 117-143)

```python
117:     def add_comment(self, issue_key: str, comment_text: str) -> Dict[str, Any]:
...
124:         url = f"{self.base_url}/rest/api/3/issue/{issue_key}/comment"
125:         payload = {
126:             "body": {
127:                 "type": "doc",
128:                 "version": 1,
129:                 "content": [
130:                     {
131:                         "type": "paragraph",
132:                         "content": [
133:                             {"type": "text", "text": comment_text}
134:                         ]
135:                     }
136:                 ]
137:             }
138:         }
139:         response = requests.post(url, headers=self.headers, auth=self.auth,
140:                                 data=json.dumps(payload))
141:         response.raise_for_status()
142:         return response.json()
```

**Lines 126-137**: Comments also use ADF format
**Line 139**: POSTs the comment to the issue

### Demonstration Function (Lines 169-272)

```python
173:     # Configuration (replace with your actual credentials)
174:     # For security, use environment variables in production
175:     JIRA_URL = "https://your-domain.atlassian.net"
176:     EMAIL = "your-email@example.com"
177:     API_TOKEN = "your-api-token-here"
```

**Lines 173-177**: Demo configuration - replace with actual credentials for testing

## Program Output

```
======================================================================
JIRA API Python Example
======================================================================

[1] Initializing JIRA client...
    Base URL: https://your-domain.atlassian.net
    Email: your-email@example.com

[2] Fetching project details...
    Error: 403 Client Error: Forbidden for url: https://your-domain.atlassian.net/rest/api/3/project/DEMO

[3] Fetching issue details...
    Error: 403 Client Error: Forbidden for url: https://your-domain.atlassian.net/rest/api/3/issue/DEMO-123

[4] Searching issues with JQL...
    JQL: project = DEMO AND status = 'In Progress' ORDER BY created DESC
    Error: 403 Client Error: Forbidden for url: https://your-domain.atlassian.net/rest/api/3/search?jql=project+%3D+DEMO+AND+status+%3D+%27In+Progress%27+ORDER+BY+created+DESC&maxResults=5

[5] Creating a new issue...
    Error: 403 Client Error: Forbidden for url: https://your-domain.atlassian.net/rest/api/3/issue

[6] Updating an issue...
    Error: 403 Client Error: Forbidden for url: https://your-domain.atlassian.net/rest/api/3/issue/DEMO-123

[7] Adding a comment to an issue...
    Error: 403 Client Error: Forbidden for url: https://your-domain.atlassian.net/rest/api/3/issue/DEMO-123/comment

======================================================================
API Operations Completed
======================================================================

Note: This is a demonstration. Replace credentials with actual values.
For production use:
  - Store credentials in environment variables
  - Use proper error handling
  - Implement retry logic for network failures
  - Add rate limiting to respect API quotas
```

### Output Analysis

The output shows 403 Forbidden errors because placeholder credentials are used. When you provide valid credentials:

- **Section [1]**: Shows client initialization with your JIRA URL and email
- **Section [2]**: Would display project name, key, and type
- **Section [3]**: Would show issue details including key, summary, status, and assignee
- **Section [4]**: Would list matching issues from the JQL search
- **Section [5]**: Would return the newly created issue key and URL
- **Section [6]**: Would confirm successful update
- **Section [7]**: Would return the comment ID

## API Authentication

JIRA Cloud uses **API tokens** for authentication:

1. **Generate API Token**:
   - Go to: https://id.atlassian.com/manage-profile/security/api-tokens
   - Click "Create API token"
   - Copy and save the token securely

2. **Authentication Method** (Line 32):
   ```python
   self.auth = (email, api_token)
   ```
   Uses HTTP Basic Auth with email as username and API token as password

## Key API Endpoints

| Operation | HTTP Method | Endpoint | Code Reference |
|-----------|-------------|----------|----------------|
| Get Issue | GET | `/rest/api/3/issue/{issueKey}` | Line 46 |
| Create Issue | POST | `/rest/api/3/issue` | Line 59 |
| Update Issue | PUT | `/rest/api/3/issue/{issueKey}` | Line 91 |
| Search Issues | GET | `/rest/api/3/search` | Line 107 |
| Add Comment | POST | `/rest/api/3/issue/{issueKey}/comment` | Line 124 |
| Get Project | GET | `/rest/api/3/project/{projectKey}` | Line 154 |

## Atlassian Document Format (ADF)

JIRA Cloud uses ADF for rich text fields like descriptions and comments:

```python
{
    "type": "doc",
    "version": 1,
    "content": [
        {
            "type": "paragraph",
            "content": [
                {"type": "text", "text": "Your text here"}
            ]
        }
    ]
}
```

See Lines 64-75 (issue description) and Lines 126-137 (comment) for usage examples.

## Production Best Practices

1. **Secure Credentials**: Use environment variables instead of hardcoding
   ```python
   import os
   JIRA_URL = os.getenv('JIRA_URL')
   EMAIL = os.getenv('JIRA_EMAIL')
   API_TOKEN = os.getenv('JIRA_API_TOKEN')
   ```

2. **Error Handling**: Catch specific exceptions and handle them appropriately
   ```python
   try:
       issue = client.get_issue("PROJ-123")
   except requests.exceptions.HTTPError as e:
       if e.response.status_code == 404:
           print("Issue not found")
       elif e.response.status_code == 401:
           print("Authentication failed")
   ```

3. **Rate Limiting**: JIRA Cloud has rate limits (typically 10-100 requests/second)
   - Implement exponential backoff for retries
   - Add delays between bulk operations

4. **Pagination**: For large result sets, use pagination
   ```python
   params = {
       "jql": jql,
       "startAt": 0,
       "maxResults": 50
   }
   ```

## Resources

- [JIRA REST API Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/)
- [Atlassian Document Format](https://developer.atlassian.com/cloud/jira/platform/apis/document/structure/)
- [JQL (JIRA Query Language)](https://support.atlassian.com/jira-software-cloud/docs/use-advanced-search-with-jira-query-language-jql/)
- [API Token Management](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/)

## Version Requirements

- **Python**: 3.9 or higher (for type hints support)
- **requests**: 2.31.0 or higher
- **JIRA API**: Version 3 (REST API v3)

This example works with JIRA Cloud. For JIRA Server/Data Center, authentication and some endpoints may differ.
