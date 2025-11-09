# Confluence Wiki API Python Example

This example demonstrates how to interact with Confluence Wiki's REST API using Python's `requests` library. It covers common operations like managing spaces, creating/updating pages, searching content, and handling page hierarchies.

## Requirements

- **Python**: >= 3.9
- **Dependencies**: requests >= 2.31.0
- **Confluence**: Works with Atlassian Confluence Cloud

## Running the Example

```bash
uv run python main_confluence_wiki.py
```

The script uses inline script metadata (PEP 723), so `uv` will automatically install dependencies.

## Source Code Overview

### 1. Client Initialization (Lines 22-42)

```python
22: class ConfluenceClient:
23:     """A simple Confluence API client using requests library."""
24:
25:     def __init__(self, base_url: str, email: str, api_token: str):
26:         """
27:         Initialize Confluence client with credentials.
28:         """
34:         self.base_url = base_url.rstrip('/')
35:         self.auth = (email, api_token)
36:         self.headers = {
37:             'Accept': 'application/json',
38:             'Content-Type': 'application/json'
39:         }
```

**Purpose**: Initializes the client with authentication credentials using HTTP Basic Auth (email + API token).

### 2. Get Space Information (Lines 44-69)

```python
44:     def get_space(self, space_key: str) -> Dict[str, Any]:
45:         """Get details of a specific Confluence space."""
51:         url = f"{self.base_url}/rest/api/space/{space_key}"
52:         response = requests.get(url, headers=self.headers, auth=self.auth)
53:         response.raise_for_status()
54:         return response.json()
56:     def get_all_spaces(self, limit: int = 25) -> Dict[str, Any]:
57:         """Get all spaces in the Confluence instance."""
64:         url = f"{self.base_url}/rest/api/space"
65:         params = {"limit": limit}
66:         response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
```

**Purpose**: Retrieves space information. Spaces are top-level containers in Confluence that organize pages.

### 3. Get Page Information (Lines 71-112)

```python
71:     def get_page(self, page_id: str, expand: Optional[List[str]] = None) -> Dict[str, Any]:
72:         """Get details of a specific page."""
80:         url = f"{self.base_url}/rest/api/content/{page_id}"
81:         params = {}
82:         if expand:
83:             params['expand'] = ','.join(expand)
84:         response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
```

**Purpose**: Retrieves page details by ID. The `expand` parameter allows fetching additional properties like content body, version, and space information.

### 4. Get Page by Title (Lines 88-112)

```python
88:     def get_page_by_title(self, space_key: str, title: str) -> Optional[Dict[str, Any]]:
89:         """Get a page by its title within a space."""
97:         url = f"{self.base_url}/rest/api/content"
98:         params = {
99:             "spaceKey": space_key,
100:            "title": title,
101:            "expand": "body.storage,version"
102:        }
103:        response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
```

**Purpose**: Finds a page by its title within a specific space. Useful when you don't know the page ID.

### 5. Create Page (Lines 114-144)

```python
114:    def create_page(self, space_key: str, title: str, body: str,
115:                    parent_id: Optional[str] = None) -> Dict[str, Any]:
116:        """Create a new Confluence page."""
123:        url = f"{self.base_url}/rest/api/content"
124:        payload = {
125:            "type": "page",
126:            "title": title,
127:            "space": {"key": space_key},
128:            "body": {
129:                "storage": {
130:                    "value": body,
131:                    "representation": "storage"
132:                }
133:            }
134:        }
135:        if parent_id:
136:            "ancestors": [{"id": parent_id}]
```

**Purpose**: Creates a new page in a specified space. Content is provided in HTML format (storage representation). Optionally, a parent page can be specified to create a child page.

### 6. Update Page (Lines 146-169)

```python
146:    def update_page(self, page_id: str, title: str, body: str, version: int) -> Dict[str, Any]:
147:        """Update an existing Confluence page."""
156:        url = f"{self.base_url}/rest/api/content/{page_id}"
157:        payload = {
158:            "type": "page",
159:            "title": title,
160:            "body": {
161:                "storage": {
162:                    "value": body,
163:                    "representation": "storage"
164:                }
165:            },
166:            "version": {"number": version}
167:        }
```

**Purpose**: Updates an existing page. Requires the new version number (current version + 1) for optimistic locking.

### 7. Search Content (Lines 182-197)

```python
182:    def search_content(self, cql: str, limit: int = 25) -> Dict[str, Any]:
183:        """Search for content using CQL (Confluence Query Language)."""
191:        url = f"{self.base_url}/rest/api/content/search"
192:        params = {
193:            "cql": cql,
194:            "limit": limit
195:        }
196:        response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
```

**Purpose**: Searches for content using CQL. Example CQL: `"type=page AND space=DEMO ORDER BY created DESC"`.

## Program Output

```
======================================================================
Confluence Wiki API Python Example
======================================================================

[1] Initializing Confluence client...
    Base URL: https://your-domain.atlassian.net/wiki
    Email: your-email@example.com
```

**Lines 234-238**: The program initializes the ConfluenceClient with the base URL and credentials. In production, these should be environment variables.

```
[2] Fetching all spaces...
    Total spaces: 3
    - DEMO: Demo Space
    - TECH: Technical Documentation
    - PROJ: Project Wiki
```

**Lines 241-248**: Calls `get_all_spaces()` (line 56) to retrieve all spaces in the Confluence instance. Each space has a key (e.g., "DEMO") and a name.

```
[3] Fetching space details...
    Space Key: DEMO
    Space Name: Demo Space
    Space Type: global
    Space URL: https://your-domain.atlassian.net/wiki/spaces/DEMO
```

**Lines 251-259**: Calls `get_space("DEMO")` (line 44) to get detailed information about a specific space.

```
[4] Searching content with CQL...
    CQL: type=page AND space=DEMO ORDER BY created DESC
    Total found: 15
    Returned: 5
    [1] 123456: Home
    [2] 123457: Getting Started
    [3] 123458: API Documentation
    [4] 123459: Best Practices
    [5] 123460: FAQ
```

**Lines 262-272**: Uses `search_content()` (line 182) with CQL query to find pages. CQL allows powerful queries similar to SQL.

```
[5] Fetching page by title...
    Page ID: 123456
    Page Title: Home
    Page Version: 5
    Last Modified: 2024-01-15T10:30:45.123Z
    Modified By: John Doe
```

**Lines 275-286**: Uses `get_page_by_title()` (line 88) to find a page by its title within a space. Returns page metadata including version information.

```
[6] Creating a new page...
    Created page ID: 789012
    Page Title: API Test Page - Python Example
    Page URL: https://your-domain.atlassian.net/wiki/pages/viewpage.action?pageId=789012
```

**Lines 289-311**: Calls `create_page()` (line 114) to create a new page with HTML content. The method returns the newly created page's ID and URL.

```
[7] Fetching page with expanded properties...
    Page ID: 123456
    Page Title: Home
    Space: Demo Space
    Version: 5
    Content length: 2543 characters
```

**Lines 314-323**: Uses `get_page()` (line 71) with expanded properties to fetch the page body, version, and space information.

```
[8] Updating an existing page...
    Updated page ID: 789012
    New version: 2
```

**Lines 326-348**: First fetches the current page to get its version number (line 332), then calls `update_page()` (line 146) with incremented version number. Version management prevents conflicting updates.

```
[9] Fetching child pages...
    Total child pages: 3
    - 234567: Subpage 1
    - 234568: Subpage 2
    - 234569: Subpage 3
```

**Lines 351-359**: Uses `get_page_children()` (line 199) to retrieve all child pages of a parent page, showing the hierarchical structure.

```
[10] Deleting a page...
    Page 'API Test Page - Python Example' deleted successfully
```

**Lines 362-373**: First finds the page by title, then calls `delete_page()` (line 171) to remove it from Confluence.

```
======================================================================
API Operations Completed
======================================================================

Note: This is a demonstration. Replace credentials with actual values.
For production use:
  - Store credentials in environment variables
  - Use proper error handling
  - Implement retry logic for network failures
  - Add rate limiting to respect API quotas
  - Validate content before creating/updating pages
```

**Lines 375-386**: Completion message with best practices reminder.

## Key Features Demonstrated

1. **Authentication**: HTTP Basic Auth using email and API token (lines 25-39)
2. **Space Management**: List and get space details (lines 44-69)
3. **Page Operations**:
   - Create pages with HTML content (lines 114-144)
   - Update pages with version management (lines 146-169)
   - Delete pages (lines 171-179)
   - Get pages by ID or title (lines 71-112)
4. **Search**: CQL-based content search (lines 182-197)
5. **Hierarchy**: Get child pages (lines 199-211)
6. **Error Handling**: Uses `raise_for_status()` to catch HTTP errors

## Authentication Setup

To use this example with real credentials:

1. Generate an API token from Atlassian account settings:
   - Go to https://id.atlassian.com/manage-profile/security/api-tokens
   - Click "Create API token"
   - Copy the token

2. Set environment variables (recommended):
   ```bash
   export CONFLUENCE_URL="https://your-domain.atlassian.net/wiki"
   export CONFLUENCE_EMAIL="your-email@example.com"
   export CONFLUENCE_API_TOKEN="your-api-token"
   ```

3. Update the script to use environment variables:
   ```python
   import os
   CONFLUENCE_URL = os.getenv("CONFLUENCE_URL")
   EMAIL = os.getenv("CONFLUENCE_EMAIL")
   API_TOKEN = os.getenv("CONFLUENCE_API_TOKEN")
   ```

## CQL Query Examples

Confluence Query Language (CQL) examples for searching:

- Find all pages in a space: `type=page AND space=DEMO`
- Find recent pages: `type=page AND created >= now()-7d`
- Search by text: `type=page AND text ~ "documentation"`
- Find pages by label: `type=page AND label = "important"`
- Combine conditions: `type=page AND space=DEMO AND creator=currentUser() ORDER BY created DESC`

## Notes

- The example uses placeholder credentials and will show connection errors when run
- All API operations return JSON responses that can be parsed for additional details
- Version management is crucial for updates to prevent conflicting changes
- Content is stored in "storage format" (HTML-like markup)
- Rate limits apply to Confluence Cloud API (check Atlassian documentation)
