# Workday API Python Example

This example demonstrates how to interact with Workday's REST APIs using Python. It covers OAuth 2.0 authentication, WQL (Workday Query Language) queries, REST API calls for workers and organizations, and RAAS (Report as a Service).

## Prerequisites

- Python 3.9 or higher
- A Workday tenant with API Client configured
- OAuth 2.0 credentials (Client ID, Client Secret, Refresh Token)

## Running the Example

```bash
uv run python/workday_api/main_workday_api.py
```

## Important Source Code

### Lines 23-51: WorkdayClient Class Initialization

```python
class WorkdayClient:
    """A Workday API client supporting OAuth 2.0 and REST operations."""

    def __init__(
        self,
        tenant: str,
        client_id: str,
        client_secret: str,
        refresh_token: str,
        base_url: str | None = None,
    ):
        """
        Initialize Workday client with OAuth 2.0 credentials.

        Args:
            tenant: Workday tenant name (e.g., 'acme_impl1')
            client_id: OAuth 2.0 client ID from API Client registration
            client_secret: OAuth 2.0 client secret
            refresh_token: Refresh token for obtaining access tokens
            base_url: Optional custom base URL (defaults to Workday cloud)
        """
        self.tenant = tenant
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.base_url = base_url or "https://wd2-impl-services1.workday.com"
        self.token_url = f"{self.base_url}/ccx/oauth2/{tenant}/token"
        self.access_token: str | None = None
        self.token_expires: datetime | None = None
```

**Annotation**: The client stores OAuth 2.0 credentials and constructs the Workday API base URL. The `token_url` (line 49) follows Workday's OAuth endpoint pattern: `/ccx/oauth2/{tenant}/token`.

### Lines 53-83: OAuth 2.0 Token Acquisition

```python
    def _get_access_token(self) -> str:
        """Obtain or refresh OAuth 2.0 access token."""
        # Check if current token is still valid
        if self.access_token and self.token_expires:
            if datetime.now() < self.token_expires:
                return self.access_token

        # Request new access token using refresh token
        auth_string = f"{self.client_id}:{self.client_secret}"
        auth_bytes = base64.b64encode(auth_string.encode()).decode()

        headers = {
            "Authorization": f"Basic {auth_bytes}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = {"grant_type": "refresh_token", "refresh_token": self.refresh_token}

        response = requests.post(self.token_url, headers=headers, data=data)
        response.raise_for_status()

        token_data = response.json()
        self.access_token = token_data["access_token"]
```

**Annotation**:
- Lines 57-59: Token caching to avoid unnecessary API calls
- Lines 62-63: Base64 encoding of client credentials for Basic Auth header
- Line 68: Using `refresh_token` grant type as required by Workday OAuth
- Line 71: POST request to token endpoint returns access token

### Lines 92-109: WQL Query Execution

```python
    def execute_wql(
        self, query: str, limit: int = 100, offset: int = 0
    ) -> dict[str, Any]:
        """Execute a WQL (Workday Query Language) query."""
        url = f"{self.base_url}/ccx/api/wql/v1/{self.tenant}/data"
        params = {"limit": limit, "offset": offset}
        payload = {"query": query}

        response = requests.post(
            url, headers=self._get_headers(), params=params, json=payload
        )
        response.raise_for_status()
        return response.json()
```

**Annotation**:
- Line 96: WQL endpoint follows pattern `/ccx/api/wql/v1/{tenant}/data`
- Line 98: Query is passed in the request body as JSON
- Line 100-102: POST request with query in body, pagination in URL params

### Lines 111-132: Get Workers via REST API

```python
    def get_workers(
        self,
        limit: int = 100,
        offset: int = 0,
        search: str | None = None,
    ) -> dict[str, Any]:
        """Retrieve worker records from Workday."""
        url = f"{self.base_url}/ccx/api/v1/{self.tenant}/workers"
        params = {"limit": limit, "offset": offset}
        if search:
            params["search"] = search

        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()
```

**Annotation**:
- Line 118: Workers REST endpoint: `/ccx/api/v1/{tenant}/workers`
- Line 120-121: Optional search parameter for filtering workers
- Line 123: GET request returns paginated worker data

### Lines 183-218: RAAS (Report as a Service)

```python
    def get_raas_report(
        self,
        report_owner: str,
        report_name: str,
        output_format: str = "json",
        params: dict[str, str] | None = None,
    ) -> dict[str, Any] | str:
        """Execute a RAAS (Report as a Service) custom report."""
        url = (
            f"{self.base_url}/ccx/service/customreport2/{self.tenant}/"
            f"{report_owner}/{report_name}"
        )

        query_params = {"format": output_format}
        if params:
            query_params.update(params)

        response = requests.get(url, headers=self._get_headers(), params=query_params)
        response.raise_for_status()

        if output_format == "json":
            return response.json()
        return response.text
```

**Annotation**:
- Lines 191-193: RAAS URL pattern includes report owner and report name
- Line 195: Format parameter controls output (json, csv, xml)
- Lines 201-203: Return type depends on requested format

### Lines 255-280: WQL Search with Dynamic Conditions

```python
    def search_workers_wql(
        self,
        first_name: str | None = None,
        last_name: str | None = None,
        department: str | None = None,
        limit: int = 100,
    ) -> dict[str, Any]:
        """Search for workers using WQL with optional filters."""
        query = """
        SELECT worker, worker.firstName, worker.lastName,
               worker.primaryWorkEmail, worker.businessTitle,
               worker.supervisoryOrganization
        FROM allWorkers
        """

        conditions = []
        if first_name:
            conditions.append(f"worker.firstName LIKE '%{first_name}%'")
        if last_name:
            conditions.append(f"worker.lastName LIKE '%{last_name}%'")
        if department:
            conditions.append(
                f"worker.supervisoryOrganization.name LIKE '%{department}%'"
            )

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        return self.execute_wql(query, limit=limit)
```

**Annotation**:
- Lines 263-267: WQL SELECT statement with navigation to related objects
- Lines 269-276: Dynamic WHERE clause construction with LIKE patterns
- Line 278: AND operator to combine multiple conditions

## Expected Output

```
======================================================================
Workday API Python Example
======================================================================

[1] Initializing Workday client...
    Tenant: acme_impl1
    Client ID: your-cli...

[2] Authenticating with OAuth 2.0...
    Access token obtained: eyJhbGciOiJSUzI1Ni...
    Token expires: 2024-01-15 15:30:00.123456

[3] Executing WQL query for workers...
    Query: SELECT worker, worker.firstName, worker.lastName...
    Found 5 workers
    [1] John Smith
        Title: Software Engineer
    [2] Jane Doe
        Title: Product Manager
    [3] Bob Johnson
        Title: Data Analyst
    [4] Alice Williams
        Title: UX Designer
    [5] Charlie Brown
        Title: DevOps Engineer

[4] Fetching workers via REST API...
    Total workers: 1250
    Retrieved: 5
    [1] John Smith (WID: 3aa5550b7fe348b98d7b5741afc65534)
    [2] Jane Doe (WID: 4bb6661c8gf459c09e8c6852bgd76645)
    [3] Bob Johnson (WID: 5cc7772d9hg56ad10f9d7963che87756)
    [4] Alice Williams (WID: 6dd8883e0ih67be21g0e8074dif98867)
    [5] Charlie Brown (WID: 7ee9994f1ji78cf32h1f9185ejg09978)

[5] Fetching supervisory organizations...
    Found 5 organizations
    [1] Engineering
        ID: org_eng_001
    [2] Product Management
        ID: org_pm_002
    [3] Human Resources
        ID: org_hr_003
    [4] Finance
        ID: org_fin_004
    [5] Sales
        ID: org_sales_005

[6] Fetching locations...
    Found 5 locations
    [1] San Francisco HQ (ID: loc_sf_001)
    [2] New York Office (ID: loc_ny_002)
    [3] London Office (ID: loc_lon_003)
    [4] Tokyo Office (ID: loc_tok_004)
    [5] Sydney Office (ID: loc_syd_005)

[7] Fetching job profiles...
    Found 5 job profiles
    [1] Software Engineer
        ID: jp_swe_001
    [2] Product Manager
        ID: jp_pm_002
    [3] Data Analyst
        ID: jp_da_003
    [4] UX Designer
        ID: jp_ux_004
    [5] DevOps Engineer
        ID: jp_devops_005

[8] Searching workers by department using WQL...
    Found 3 workers in Engineering
    [1] John Smith
        Email: john.smith@company.com
    [2] Charlie Brown
        Email: charlie.brown@company.com
    [3] Eva Martinez
        Email: eva.martinez@company.com

[9] Executing RAAS custom report...
    Report returned 3 entries
    [1] John Smith
    [2] Jane Doe
    [3] Bob Johnson

[10] Fetching time off balances...
    Worker ID: 3aa5550b7fe348b98d7b5741afc65534
    Found 3 time off plans
    [1] Vacation: 120 hours
    [2] Sick Leave: 40 hours
    [3] Personal Time: 16 hours

======================================================================
API Operations Completed
======================================================================

Note: This is a demonstration. Replace credentials with actual values.
For production use:
  - Store credentials in environment variables
  - Register an API Client in Workday tenant
  - Configure OAuth 2.0 scopes appropriately
  - Implement proper error handling and logging
  - Respect Workday API rate limits
  - Use HTTPS for all connections
```

## Output Annotations

| Output Line | Source Code Reference | Description |
|-------------|----------------------|-------------|
| `[1] Initializing...` | Lines 292-296 | Client initialization with tenant and credentials |
| `[2] Authenticating...` | Lines 299-304 | OAuth 2.0 token acquisition using refresh token flow |
| `[3] Executing WQL...` | Lines 307-326 | WQL query execution with pagination support |
| `[4] Fetching workers...` | Lines 329-344 | REST API call to `/workers` endpoint |
| `[5] Fetching organizations...` | Lines 347-361 | Query supervisory organizations |
| `[6] Fetching locations...` | Lines 364-376 | Get all configured locations |
| `[7] Fetching job profiles...` | Lines 379-393 | Retrieve job profile definitions |
| `[8] Searching workers...` | Lines 396-410 | Dynamic WQL with WHERE clause |
| `[9] Executing RAAS...` | Lines 413-427 | Custom report execution via RAAS |
| `[10] Fetching time off...` | Lines 430-444 | Absence management API call |

## Key Workday API Concepts

### API Endpoints

| API Type | URL Pattern | Description |
|----------|-------------|-------------|
| OAuth Token | `/ccx/oauth2/{tenant}/token` | Obtain access tokens |
| WQL | `/ccx/api/wql/v1/{tenant}/data` | Execute WQL queries |
| REST Workers | `/ccx/api/v1/{tenant}/workers` | Worker CRUD operations |
| REST Orgs | `/ccx/api/v1/{tenant}/organizations` | Organization data |
| RAAS | `/ccx/service/customreport2/{tenant}/{owner}/{name}` | Custom reports |
| Absence | `/ccx/api/absenceManagement/v1/{tenant}/...` | Time off management |

### WQL (Workday Query Language)

WQL is a SQL-like query language for Workday data:
- Uses data sources like `allWorkers`, `allOrganizations`
- Supports navigation syntax: `worker.supervisoryOrganization.name`
- Supports LIKE, IN, AND, OR operators
- Pagination via `limit` and `offset` parameters

### Authentication

Workday uses OAuth 2.0 with refresh tokens:
1. Register API Client in Workday tenant
2. Configure scopes and integrations
3. Obtain refresh token via authorization flow
4. Exchange refresh token for access token (valid ~1 hour)

## Configuration Requirements

Before running this example, you need to set up:

1. **API Client Registration** in Workday:
   - Navigate to: View API Clients for Integrations
   - Register a new API Client
   - Note the Client ID and Client Secret

2. **OAuth 2.0 Scopes**:
   - Configure appropriate scopes for your use case
   - Common scopes: `workers:read`, `organizations:read`

3. **Refresh Token**:
   - Complete OAuth authorization flow
   - Store the refresh token securely

4. **Environment Variables** (recommended for production):
   ```bash
   export WORKDAY_TENANT="your_tenant"
   export WORKDAY_CLIENT_ID="your_client_id"
   export WORKDAY_CLIENT_SECRET="your_client_secret"
   export WORKDAY_REFRESH_TOKEN="your_refresh_token"
   ```

## Error Handling

Common errors and solutions:

| Error | Cause | Solution |
|-------|-------|----------|
| 401 Unauthorized | Invalid or expired token | Check credentials, refresh token |
| 403 Forbidden | Insufficient scopes | Configure API Client scopes |
| 404 Not Found | Invalid endpoint or ID | Verify tenant name and resource IDs |
| 429 Too Many Requests | Rate limit exceeded | Implement backoff and retry |

## Security Best Practices

- Never hardcode credentials in source code
- Use environment variables or secure vaults
- Rotate refresh tokens periodically
- Limit API Client scopes to minimum required
- Monitor API usage for anomalies
- Use HTTPS for all API calls
