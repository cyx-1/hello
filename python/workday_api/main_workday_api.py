#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "requests>=2.31.0",
# ]
# ///

"""
Workday API Python Example

This script demonstrates how to interact with Workday's REST APIs using Python.
It covers OAuth 2.0 authentication, WQL (Workday Query Language) queries,
REST API calls for workers and organizations, and RAAS (Report as a Service).
"""

import base64
import requests
from typing import Any
from datetime import datetime


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

    def _get_access_token(self) -> str:
        """
        Obtain or refresh OAuth 2.0 access token.

        Returns:
            Valid access token string
        """
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

        # Calculate token expiration (usually 1 hour, subtract 5 min buffer)
        expires_in = token_data.get("expires_in", 3600)
        from datetime import timedelta

        self.token_expires = datetime.now() + timedelta(seconds=expires_in - 300)

        return self.access_token

    def _get_headers(self) -> dict[str, str]:
        """Get headers with valid access token."""
        token = self._get_access_token()
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    def execute_wql(
        self, query: str, limit: int = 100, offset: int = 0
    ) -> dict[str, Any]:
        """
        Execute a WQL (Workday Query Language) query.

        Args:
            query: WQL query string
            limit: Maximum number of results to return
            offset: Number of results to skip (for pagination)

        Returns:
            Dictionary containing query results
        """
        url = f"{self.base_url}/ccx/api/wql/v1/{self.tenant}/data"
        params = {"limit": limit, "offset": offset}
        payload = {"query": query}

        response = requests.post(
            url, headers=self._get_headers(), params=params, json=payload
        )
        response.raise_for_status()
        return response.json()

    def get_workers(
        self,
        limit: int = 100,
        offset: int = 0,
        search: str | None = None,
    ) -> dict[str, Any]:
        """
        Retrieve worker records from Workday.

        Args:
            limit: Maximum number of workers to return
            offset: Number of records to skip
            search: Optional search string for filtering

        Returns:
            Dictionary containing worker data
        """
        url = f"{self.base_url}/ccx/api/v1/{self.tenant}/workers"
        params = {"limit": limit, "offset": offset}
        if search:
            params["search"] = search

        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def get_worker_by_id(self, worker_id: str) -> dict[str, Any]:
        """
        Retrieve a specific worker by their Workday ID.

        Args:
            worker_id: Workday worker ID (WID)

        Returns:
            Dictionary containing worker details
        """
        url = f"{self.base_url}/ccx/api/v1/{self.tenant}/workers/{worker_id}"

        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_organizations(
        self, org_type: str = "supervisory", limit: int = 100
    ) -> dict[str, Any]:
        """
        Retrieve organizations from Workday.

        Args:
            org_type: Type of organization (supervisory, company, cost_center, etc.)
            limit: Maximum number of results

        Returns:
            Dictionary containing organization data
        """
        url = f"{self.base_url}/ccx/api/v1/{self.tenant}/organizations"
        params = {"type": org_type, "limit": limit}

        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def get_raas_report(
        self,
        report_owner: str,
        report_name: str,
        output_format: str = "json",
        params: dict[str, str] | None = None,
    ) -> dict[str, Any] | str:
        """
        Execute a RAAS (Report as a Service) custom report.

        Args:
            report_owner: Username of the report owner
            report_name: Name of the custom report
            output_format: Output format (json, csv, xml)
            params: Optional report parameters

        Returns:
            Report data in specified format
        """
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

    def get_time_off_balances(self, worker_id: str) -> dict[str, Any]:
        """
        Retrieve time off balances for a worker.

        Args:
            worker_id: Workday worker ID

        Returns:
            Dictionary containing time off balance data
        """
        url = (
            f"{self.base_url}/ccx/api/absenceManagement/v1/{self.tenant}/"
            f"workers/{worker_id}/timeOffBalances"
        )

        response = requests.get(url, headers=self._get_headers())
        response.raise_for_status()
        return response.json()

    def get_job_profiles(self, limit: int = 100) -> dict[str, Any]:
        """
        Retrieve job profiles from Workday.

        Args:
            limit: Maximum number of results

        Returns:
            Dictionary containing job profile data
        """
        url = f"{self.base_url}/ccx/api/v1/{self.tenant}/jobProfiles"
        params = {"limit": limit}

        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def get_locations(self, limit: int = 100) -> dict[str, Any]:
        """
        Retrieve locations from Workday.

        Args:
            limit: Maximum number of results

        Returns:
            Dictionary containing location data
        """
        url = f"{self.base_url}/ccx/api/v1/{self.tenant}/locations"
        params = {"limit": limit}

        response = requests.get(url, headers=self._get_headers(), params=params)
        response.raise_for_status()
        return response.json()

    def search_workers_wql(
        self,
        first_name: str | None = None,
        last_name: str | None = None,
        department: str | None = None,
        limit: int = 100,
    ) -> dict[str, Any]:
        """
        Search for workers using WQL with optional filters.

        Args:
            first_name: Filter by first name (partial match)
            last_name: Filter by last name (partial match)
            department: Filter by department name
            limit: Maximum results

        Returns:
            Dictionary containing matching workers
        """
        # Build WQL query with filters
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


def demonstrate_workday_api():
    """Demonstrate various Workday API operations."""

    # Configuration (replace with your actual credentials)
    # For security, use environment variables in production
    TENANT = "acme_impl1"
    CLIENT_ID = "your-client-id"
    CLIENT_SECRET = "your-client-secret"
    REFRESH_TOKEN = "your-refresh-token"

    print("=" * 70)
    print("Workday API Python Example")
    print("=" * 70)

    # Initialize the Workday client
    print("\n[1] Initializing Workday client...")
    print(f"    Tenant: {TENANT}")
    print(f"    Client ID: {CLIENT_ID[:8]}...")
    client = WorkdayClient(TENANT, CLIENT_ID, CLIENT_SECRET, REFRESH_TOKEN)

    # Example 1: OAuth 2.0 Authentication
    print("\n[2] Authenticating with OAuth 2.0...")
    try:
        token = client._get_access_token()
        print(f"    Access token obtained: {token[:20]}...")
        print(f"    Token expires: {client.token_expires}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 2: Execute WQL Query
    print("\n[3] Executing WQL query for workers...")
    try:
        wql_query = """
        SELECT worker, worker.firstName, worker.lastName,
               worker.primaryWorkEmail, worker.businessTitle
        FROM allWorkers
        LIMIT 5
        """
        print(f"    Query: {wql_query.strip()[:50]}...")

        results = client.execute_wql(wql_query, limit=5)
        data = results.get("data", [])
        print(f"    Found {len(data)} workers")

        for idx, worker in enumerate(data, 1):
            first_name = worker.get("firstName", "N/A")
            last_name = worker.get("lastName", "N/A")
            title = worker.get("businessTitle", "N/A")
            print(f"    [{idx}] {first_name} {last_name}")
            print(f"        Title: {title}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 3: Get Workers via REST API
    print("\n[4] Fetching workers via REST API...")
    try:
        workers_response = client.get_workers(limit=5)
        workers = workers_response.get("data", [])
        total = workers_response.get("total", 0)

        print(f"    Total workers: {total}")
        print(f"    Retrieved: {len(workers)}")

        for idx, worker in enumerate(workers, 1):
            descriptor = worker.get("descriptor", "Unknown")
            wid = worker.get("id", "N/A")
            print(f"    [{idx}] {descriptor} (WID: {wid})")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 4: Get Organizations
    print("\n[5] Fetching supervisory organizations...")
    try:
        orgs_response = client.get_organizations(org_type="supervisory", limit=5)
        orgs = orgs_response.get("data", [])

        print(f"    Found {len(orgs)} organizations")

        for idx, org in enumerate(orgs, 1):
            name = org.get("descriptor", "Unknown")
            org_id = org.get("id", "N/A")
            print(f"    [{idx}] {name}")
            print(f"        ID: {org_id}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 5: Get Locations
    print("\n[6] Fetching locations...")
    try:
        locations_response = client.get_locations(limit=5)
        locations = locations_response.get("data", [])

        print(f"    Found {len(locations)} locations")

        for idx, location in enumerate(locations, 1):
            name = location.get("descriptor", "Unknown")
            loc_id = location.get("id", "N/A")
            print(f"    [{idx}] {name} (ID: {loc_id})")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 6: Get Job Profiles
    print("\n[7] Fetching job profiles...")
    try:
        profiles_response = client.get_job_profiles(limit=5)
        profiles = profiles_response.get("data", [])

        print(f"    Found {len(profiles)} job profiles")

        for idx, profile in enumerate(profiles, 1):
            name = profile.get("descriptor", "Unknown")
            profile_id = profile.get("id", "N/A")
            print(f"    [{idx}] {name}")
            print(f"        ID: {profile_id}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 7: Search Workers with WQL
    print("\n[8] Searching workers by department using WQL...")
    try:
        search_results = client.search_workers_wql(department="Engineering", limit=3)
        data = search_results.get("data", [])

        print(f"    Found {len(data)} workers in Engineering")

        for idx, worker in enumerate(data, 1):
            first_name = worker.get("firstName", "N/A")
            last_name = worker.get("lastName", "N/A")
            email = worker.get("primaryWorkEmail", "N/A")
            print(f"    [{idx}] {first_name} {last_name}")
            print(f"        Email: {email}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 8: Execute Custom RAAS Report
    print("\n[9] Executing RAAS custom report...")
    try:
        report_data = client.get_raas_report(
            report_owner="admin",
            report_name="Active_Employees_Report",
            output_format="json",
            params={"effective_date": "2024-01-01"},
        )

        if isinstance(report_data, dict):
            report_entry = report_data.get("Report_Entry", [])
            print(f"    Report returned {len(report_entry)} entries")

            for idx, entry in enumerate(report_entry[:3], 1):
                employee = entry.get("Employee", "Unknown")
                print(f"    [{idx}] {employee}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 9: Get Time Off Balances
    print("\n[10] Fetching time off balances...")
    try:
        # Using a sample worker ID
        worker_id = "3aa5550b7fe348b98d7b5741afc65534"
        balances = client.get_time_off_balances(worker_id)
        balance_data = balances.get("data", [])

        print(f"    Worker ID: {worker_id}")
        print(f"    Found {len(balance_data)} time off plans")

        for idx, balance in enumerate(balance_data[:3], 1):
            plan = balance.get("timeOffPlan", {}).get("descriptor", "Unknown")
            current_balance = balance.get("balance", 0)
            print(f"    [{idx}] {plan}: {current_balance} hours")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    print("\n" + "=" * 70)
    print("API Operations Completed")
    print("=" * 70)
    print("\nNote: This is a demonstration. Replace credentials with actual values.")
    print("For production use:")
    print("  - Store credentials in environment variables")
    print("  - Register an API Client in Workday tenant")
    print("  - Configure OAuth 2.0 scopes appropriately")
    print("  - Implement proper error handling and logging")
    print("  - Respect Workday API rate limits")
    print("  - Use HTTPS for all connections")


if __name__ == "__main__":
    demonstrate_workday_api()
