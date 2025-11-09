# ServiceNow API Python Example

This example demonstrates how to interact with ServiceNow's REST API using Python and the `requests` library.

## Prerequisites

- Python 3.9 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- A ServiceNow instance (Developer instance or enterprise instance)
- ServiceNow credentials (username and password or API key)

## Running the Example

```bash
uv run python main_servicenow.py
```

The script uses inline script metadata (PEP 723) for dependency management, so `uv` will automatically install the required `requests` library.

## Source Code Overview

### Key Components

#### 1. ServiceNowClient Class (Lines 22-172)

The `ServiceNowClient` class encapsulates all ServiceNow API interactions:

```python
22: class ServiceNowClient:
23:     """A simple ServiceNow API client using requests library."""
24:
25:     def __init__(self, instance: str, username: str, password: str):
26:         """
27:         Initialize ServiceNow client with credentials.
...
34:         self.base_url = f"https://{instance}.service-now.com"
35:         self.auth = (username, password)
36:         self.headers = {
37:             'Accept': 'application/json',
38:             'Content-Type': 'application/json'
39:         }
```

**Lines 25-39**: The constructor initializes the client with:
- `instance`: Your ServiceNow instance name (e.g., 'dev12345' for dev12345.service-now.com)
- `username`: ServiceNow username
- `password`: ServiceNow password or API key
- **Line 34**: Constructs the full base URL for the ServiceNow instance
- **Line 35**: Uses HTTP Basic Authentication
- **Lines 36-39**: Sets JSON headers for all API requests

#### 2. Get Record (Lines 41-55)

```python
41:     def get_record(self, table: str, sys_id: str) -> Dict[str, Any]:
42:         """
43:         Fetch a specific record from a ServiceNow table.
...
51:         url = f"{self.base_url}/api/now/table/{table}/{sys_id}"
52:         response = requests.get(url, headers=self.headers, auth=self.auth)
53:         response.raise_for_status()
54:         return response.json()
```

**Line 51**: Constructs the Table API endpoint with table name and sys_id
**Line 52**: Makes a GET request with authentication headers
**Line 53**: Raises exception for HTTP errors (4xx, 5xx)
**Line 54**: Returns the parsed JSON response

#### 3. Query Records (Lines 57-83)

```python
57:     def query_records(self, table: str, query: str = "", limit: int = 10,
58:                      fields: Optional[List[str]] = None) -> Dict[str, Any]:
59:         """
60:         Query records from a ServiceNow table with optional filters.
...
69:         url = f"{self.base_url}/api/now/table/{table}"
70:         params = {
71:             "sysparm_limit": limit
72:         }
73:         if query:
74:             params["sysparm_query"] = query
75:         if fields:
76:             params["sysparm_fields"] = ",".join(fields)
77:
78:         response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
79:         response.raise_for_status()
80:         return response.json()
```

**Lines 70-76**: Builds query parameters:
- `sysparm_limit`: Maximum records to return
- `sysparm_query`: Encoded query string (e.g., 'active=true^priority=1')
- `sysparm_fields`: Comma-separated list of fields to return
**Line 78**: Makes GET request with query parameters
**Query Syntax**: Uses ServiceNow's encoded query format with `^` as AND operator

#### 4. Create Incident (Lines 85-120)

```python
85:     def create_incident(self, short_description: str, description: str,
86:                        urgency: str = "3", impact: str = "3",
87:                        caller_id: Optional[str] = None) -> Dict[str, Any]:
88:         """
89:         Create a new incident in ServiceNow.
...
98:         url = f"{self.base_url}/api/now/table/incident"
99:         payload = {
100:             "short_description": short_description,
101:             "description": description,
102:             "urgency": urgency,
103:             "impact": impact
104:         }
105:         if caller_id:
106:             payload["caller_id"] = caller_id
107:
108:         response = requests.post(url, headers=self.headers, auth=self.auth,
109:                                 data=json.dumps(payload))
110:         response.raise_for_status()
111:         return response.json()
```

**Lines 99-104**: Creates incident payload with:
- `short_description`: Brief summary of the incident
- `description`: Detailed description
- `urgency`: Urgency level (1=High, 2=Medium, 3=Low)
- `impact`: Impact level (1=High, 2=Medium, 3=Low)
**Lines 105-106**: Optionally adds caller_id if provided
**Lines 108-109**: POSTs JSON payload to create the incident

#### 5. Update Record (Lines 122-138)

```python
122:     def update_record(self, table: str, sys_id: str, fields: Dict[str, Any]) -> Dict[str, Any]:
123:         """
124:         Update an existing record in ServiceNow.
...
132:         url = f"{self.base_url}/api/now/table/{table}/{sys_id}"
133:         response = requests.patch(url, headers=self.headers, auth=self.auth,
134:                                  data=json.dumps(fields))
135:         response.raise_for_status()
136:         return response.json()
```

**Line 132**: Constructs URL with table name and record sys_id
**Line 133**: Uses PATCH method for partial updates (PUT replaces entire record)
**Line 134**: Sends only the fields to be updated

#### 6. Delete Record (Lines 140-151)

```python
140:     def delete_record(self, table: str, sys_id: str) -> None:
141:         """
142:         Delete a record from ServiceNow.
...
148:         url = f"{self.base_url}/api/now/table/{table}/{sys_id}"
149:         response = requests.delete(url, headers=self.headers, auth=self.auth)
150:         response.raise_for_status()
```

**Line 149**: Uses DELETE method to remove the record
**Note**: Deleted records may still be retrievable from ServiceNow's audit tables

#### 7. Get Table Schema (Lines 153-165)

```python
153:     def get_table_schema(self, table: str) -> Dict[str, Any]:
154:         """
155:         Fetch the schema/metadata for a ServiceNow table.
...
161:         url = f"{self.base_url}/api/now/table/sys_db_object"
162:         params = {"sysparm_query": f"name={table}"}
163:         response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
164:         response.raise_for_status()
165:         return response.json()
```

**Line 161**: Queries the `sys_db_object` table which contains table metadata
**Line 162**: Filters by table name to get schema information
**Use Case**: Useful for discovering table structure and available fields

### Demonstration Function (Lines 168-312)

```python
172:     # Configuration (replace with your actual credentials)
173:     # For security, use environment variables in production
174:     INSTANCE = "dev12345"  # Your instance name (without .service-now.com)
175:     USERNAME = "admin"
176:     PASSWORD = "your-password-here"
```

**Lines 172-176**: Demo configuration - replace with your actual ServiceNow instance details

## Program Output

```
======================================================================
ServiceNow API Python Example
======================================================================

[1] Initializing ServiceNow client...
    Instance: dev12345.service-now.com
    Username: admin

[2] Querying active incidents...
    Query: active=true^priority=1
    Error: 401 Client Error: Unauthorized for url: https://dev12345.service-now.com/api/now/table/incident?sysparm_limit=5&sysparm_query=active%3Dtrue%5Epriority%3D1&sysparm_fields=number%2Cshort_description%2Cstate%2Cpriority%2Cassigned_to

[3] Creating a new incident...
    Error: 401 Client Error: Unauthorized for url: https://dev12345.service-now.com/api/now/table/incident

[4] Fetching incident details...
    (Skipped due to previous error)

[5] Updating incident...
    (Skipped due to previous error)

[6] Querying user records...
    Error: 401 Client Error: Unauthorized for url: https://dev12345.service-now.com/api/now/table/sys_user?sysparm_limit=3&sysparm_query=active%3Dtrue&sysparm_fields=user_name%2Cname%2Cemail%2Ctitle

[7] Querying recent change requests...
    Error: 401 Client Error: Unauthorized for url: https://dev12345.service-now.com/api/now/table/change_request?sysparm_limit=3&sysparm_query=active%3Dtrue&sysparm_fields=number%2Cshort_description%2Cstate%2Crisk%2Ctype

[8] Fetching incident table schema...
    Error: 401 Client Error: Unauthorized for url: https://dev12345.service-now.com/api/now/table/sys_db_object?sysparm_query=name%3Dincident

======================================================================
API Operations Completed
======================================================================

Note: This is a demonstration. Replace credentials with actual values.
For production use:
  - Store credentials in environment variables
  - Use OAuth 2.0 for authentication when possible
  - Implement proper error handling and logging
  - Add retry logic for transient failures
  - Respect ServiceNow API rate limits
```

### Output Analysis

The output shows 401 Unauthorized errors because placeholder credentials are used. When you provide valid credentials:

- **Section [1]**: Shows client initialization with instance URL and username
- **Section [2]**: Would display active high-priority incidents with their numbers, descriptions, and states
- **Section [3]**: Would return the newly created incident number and sys_id
- **Section [4]**: Would show detailed information about the incident including creation time
- **Section [5]**: Would confirm successful update with new state
- **Section [6]**: Would list active users with names, emails, and titles
- **Section [7]**: Would display recent change requests with risk levels
- **Section [8]**: Would show table schema metadata

## API Authentication

ServiceNow supports multiple authentication methods:

### 1. Basic Authentication (Used in this example)

```python
35: self.auth = (username, password)
```

**Pros**: Simple to implement
**Cons**: Less secure, credentials sent with every request
**Use Case**: Development, testing, quick scripts

### 2. OAuth 2.0 (Recommended for production)

ServiceNow supports OAuth 2.0 for more secure authentication. You'll need to:
1. Register an OAuth application in ServiceNow
2. Obtain client credentials
3. Use token-based authentication

### 3. API Keys

ServiceNow also supports API keys for service-to-service authentication.

## Key API Endpoints

| Operation | HTTP Method | Endpoint | Code Reference |
|-----------|-------------|----------|----------------|
| Get Record | GET | `/api/now/table/{table}/{sys_id}` | Line 51 |
| Query Records | GET | `/api/now/table/{table}` | Line 69 |
| Create Record | POST | `/api/now/table/{table}` | Line 98 |
| Update Record | PATCH | `/api/now/table/{table}/{sys_id}` | Line 132 |
| Delete Record | DELETE | `/api/now/table/{table}/{sys_id}` | Line 148 |
| Get Schema | GET | `/api/now/table/sys_db_object` | Line 161 |

## Common ServiceNow Tables

| Table Name | Description | Example Fields |
|------------|-------------|----------------|
| `incident` | Incident management | number, short_description, state, priority, assigned_to |
| `problem` | Problem management | number, short_description, state, impact |
| `change_request` | Change management | number, short_description, risk, type, state |
| `sys_user` | User records | user_name, name, email, title, active |
| `cmdb_ci` | Configuration items | name, asset_tag, manufacturer, model |
| `sc_request` | Service catalog requests | number, request_state, requested_for |

## ServiceNow Query Syntax

ServiceNow uses encoded queries with specific operators:

| Operator | Meaning | Example |
|----------|---------|---------|
| `^` | AND | `active=true^priority=1` |
| `^OR` | OR | `state=1^ORstate=2` |
| `=` | Equals | `priority=1` |
| `!=` | Not equals | `state!=7` |
| `>` | Greater than | `priority>2` |
| `<` | Less than | `priority<3` |
| `STARTSWITH` | Starts with | `numberSTARTSWITHINC` |
| `ENDSWITH` | Ends with | `emailENDSWITH@example.com` |
| `LIKE` | Contains | `short_descriptionLIKEnetwork` |

**Example Query** (Line 210):
```python
query = "active=true^priority=1"  # Active incidents with high priority
```

## Production Best Practices

### 1. Secure Credentials

Use environment variables instead of hardcoding:

```python
import os

INSTANCE = os.getenv('SERVICENOW_INSTANCE')
USERNAME = os.getenv('SERVICENOW_USERNAME')
PASSWORD = os.getenv('SERVICENOW_PASSWORD')
```

### 2. Error Handling

Implement comprehensive error handling:

```python
try:
    incident = client.get_record("incident", sys_id)
except requests.exceptions.HTTPError as e:
    if e.response.status_code == 404:
        print("Record not found")
    elif e.response.status_code == 401:
        print("Authentication failed")
    elif e.response.status_code == 403:
        print("Insufficient permissions")
except requests.exceptions.ConnectionError:
    print("Network connection failed")
```

### 3. Rate Limiting

ServiceNow enforces rate limits:
- Personal Developer Instances: ~100 requests per minute
- Enterprise instances: Varies by configuration

Implement retry logic with exponential backoff:

```python
import time
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504]
)
adapter = HTTPAdapter(max_retries=retry_strategy)
session = requests.Session()
session.mount("https://", adapter)
```

### 4. Pagination

For large datasets, use pagination:

```python
offset = 0
limit = 100

while True:
    params = {
        "sysparm_limit": limit,
        "sysparm_offset": offset,
        "sysparm_query": "active=true"
    }
    response = client.query_records("incident", **params)
    results = response.get("result", [])

    if not results:
        break

    # Process results
    for record in results:
        print(record)

    offset += limit
```

### 5. Field Selection

Request only needed fields to improve performance:

```python
# Instead of getting all fields:
incident = client.get_record("incident", sys_id)

# Request specific fields:
fields = ["number", "short_description", "state", "priority"]
incident = client.query_records("incident", sys_id, fields=fields)
```

## Getting a ServiceNow Developer Instance

1. Visit: https://developer.servicenow.com/
2. Sign up for a free developer account
3. Request a Personal Developer Instance (PDI)
4. Instance will be available at: `https://devXXXXX.service-now.com`
5. Login credentials will be provided via email

## Resources

- [ServiceNow REST API Documentation](https://developer.servicenow.com/dev.do#!/reference/api/latest/rest/)
- [Table API Reference](https://developer.servicenow.com/dev.do#!/reference/api/latest/rest/c_TableAPI)
- [ServiceNow Developer Portal](https://developer.servicenow.com/)
- [Encoded Query Strings](https://docs.servicenow.com/bundle/vancouver-platform-user-interface/page/use/using-lists/concept/c_EncodedQueryStrings.html)
- [OAuth 2.0 Setup](https://docs.servicenow.com/bundle/vancouver-platform-security/page/administer/security/task/t_SettingUpOAuth.html)

## Version Requirements

- **Python**: 3.9 or higher (for type hints and modern features)
- **requests**: 2.31.0 or higher
- **ServiceNow**: Works with all current ServiceNow versions (Table API is stable)

## Troubleshooting

### Common Issues

**401 Unauthorized**:
- Verify credentials are correct
- Check if user account is active
- Ensure user has appropriate roles (e.g., `rest_api_explorer`, `admin`)

**403 Forbidden**:
- User lacks necessary ACL permissions for the table
- Check user roles and table ACLs in ServiceNow

**404 Not Found**:
- Verify table name is correct
- Check if sys_id exists
- Ensure table is accessible to your user

**Rate Limiting (429)**:
- Implement exponential backoff
- Reduce request frequency
- Consider batching operations
