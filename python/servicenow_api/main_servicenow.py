#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "requests>=2.31.0",
# ]
# ///

"""
ServiceNow API Python Example

This script demonstrates how to interact with ServiceNow's REST API using Python.
It covers common operations like authentication, fetching records, creating incidents,
updating records, and querying data from various ServiceNow tables.
"""

import json
import requests
from typing import Dict, Any, List, Optional


class ServiceNowClient:
    """A simple ServiceNow API client using requests library."""

    def __init__(self, instance: str, username: str, password: str):
        """
        Initialize ServiceNow client with credentials.

        Args:
            instance: ServiceNow instance name (e.g., 'dev12345' for dev12345.service-now.com)
            username: ServiceNow username
            password: ServiceNow password or API key
        """
        self.base_url = f"https://{instance}.service-now.com"
        self.auth = (username, password)
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_record(self, table: str, sys_id: str) -> Dict[str, Any]:
        """
        Fetch a specific record from a ServiceNow table.

        Args:
            table: Table name (e.g., 'incident', 'problem', 'change_request')
            sys_id: Unique system ID of the record

        Returns:
            Dictionary containing record details
        """
        url = f"{self.base_url}/api/now/table/{table}/{sys_id}"
        response = requests.get(url, headers=self.headers, auth=self.auth)
        response.raise_for_status()
        return response.json()

    def query_records(self, table: str, query: str = "", limit: int = 10,
                     fields: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Query records from a ServiceNow table with optional filters.

        Args:
            table: Table name (e.g., 'incident', 'problem')
            query: Encoded query string (e.g., 'active=true^priority=1')
            limit: Maximum number of records to return
            fields: List of fields to return (if None, returns all)

        Returns:
            Dictionary containing list of records
        """
        url = f"{self.base_url}/api/now/table/{table}"
        params = {
            "sysparm_limit": limit
        }
        if query:
            params["sysparm_query"] = query
        if fields:
            params["sysparm_fields"] = ",".join(fields)

        response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
        response.raise_for_status()
        return response.json()

    def create_incident(self, short_description: str, description: str,
                       urgency: str = "3", impact: str = "3",
                       caller_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a new incident in ServiceNow.

        Args:
            short_description: Brief summary of the incident
            description: Detailed description of the incident
            urgency: Urgency level (1=High, 2=Medium, 3=Low)
            impact: Impact level (1=High, 2=Medium, 3=Low)
            caller_id: sys_id of the caller (optional)

        Returns:
            Dictionary containing created incident details
        """
        url = f"{self.base_url}/api/now/table/incident"
        payload = {
            "short_description": short_description,
            "description": description,
            "urgency": urgency,
            "impact": impact
        }
        if caller_id:
            payload["caller_id"] = caller_id

        response = requests.post(url, headers=self.headers, auth=self.auth,
                                data=json.dumps(payload))
        response.raise_for_status()
        return response.json()

    def update_record(self, table: str, sys_id: str, fields: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update an existing record in ServiceNow.

        Args:
            table: Table name (e.g., 'incident', 'problem')
            sys_id: Unique system ID of the record
            fields: Dictionary of fields to update

        Returns:
            Dictionary containing updated record details
        """
        url = f"{self.base_url}/api/now/table/{table}/{sys_id}"
        response = requests.patch(url, headers=self.headers, auth=self.auth,
                                 data=json.dumps(fields))
        response.raise_for_status()
        return response.json()

    def delete_record(self, table: str, sys_id: str) -> None:
        """
        Delete a record from ServiceNow.

        Args:
            table: Table name (e.g., 'incident', 'problem')
            sys_id: Unique system ID of the record
        """
        url = f"{self.base_url}/api/now/table/{table}/{sys_id}"
        response = requests.delete(url, headers=self.headers, auth=self.auth)
        response.raise_for_status()

    def get_table_schema(self, table: str) -> Dict[str, Any]:
        """
        Fetch the schema/metadata for a ServiceNow table.

        Args:
            table: Table name (e.g., 'incident')

        Returns:
            Dictionary containing table schema information
        """
        url = f"{self.base_url}/api/now/table/sys_db_object"
        params = {"sysparm_query": f"name={table}"}
        response = requests.get(url, headers=self.headers, auth=self.auth, params=params)
        response.raise_for_status()
        return response.json()


def demonstrate_servicenow_api():
    """Demonstrate various ServiceNow API operations."""

    # Configuration (replace with your actual credentials)
    # For security, use environment variables in production
    INSTANCE = "dev12345"  # Your instance name (without .service-now.com)
    USERNAME = "admin"
    PASSWORD = "your-password-here"

    print("=" * 70)
    print("ServiceNow API Python Example")
    print("=" * 70)

    # Initialize the ServiceNow client
    print("\n[1] Initializing ServiceNow client...")
    print(f"    Instance: {INSTANCE}.service-now.com")
    print(f"    Username: {USERNAME}")
    client = ServiceNowClient(INSTANCE, USERNAME, PASSWORD)

    # Example 1: Query incidents
    print("\n[2] Querying active incidents...")
    try:
        # Query for active incidents with high priority
        query = "active=true^priority=1"
        print(f"    Query: {query}")

        results = client.query_records(
            table="incident",
            query=query,
            limit=5,
            fields=["number", "short_description", "state", "priority", "assigned_to"]
        )

        incidents = results.get("result", [])
        print(f"    Found {len(incidents)} incidents")

        for idx, incident in enumerate(incidents, 1):
            print(f"    [{idx}] {incident.get('number')}: {incident.get('short_description')}")
            print(f"        State: {incident.get('state')}, Priority: {incident.get('priority')}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 2: Create a new incident
    print("\n[3] Creating a new incident...")
    try:
        new_incident = client.create_incident(
            short_description="API Test: Network connectivity issue",
            description="This is a test incident created via the ServiceNow REST API. "
                       "Users are reporting intermittent network connectivity issues.",
            urgency="2",  # Medium urgency
            impact="2"    # Medium impact
        )

        incident_data = new_incident.get("result", {})
        incident_number = incident_data.get("number")
        incident_sys_id = incident_data.get("sys_id")

        print(f"    Created incident: {incident_number}")
        print(f"    Sys ID: {incident_sys_id}")
        print(f"    URL: {client.base_url}/nav_to.do?uri=incident.do?sys_id={incident_sys_id}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")
        incident_sys_id = None

    # Example 3: Get specific incident details
    if incident_sys_id:
        print("\n[4] Fetching incident details...")
        try:
            incident = client.get_record("incident", incident_sys_id)
            incident_data = incident.get("result", {})

            print(f"    Number: {incident_data.get('number')}")
            print(f"    Short Description: {incident_data.get('short_description')}")
            print(f"    State: {incident_data.get('state')}")
            print(f"    Priority: {incident_data.get('priority')}")
            print(f"    Created: {incident_data.get('sys_created_on')}")
        except requests.exceptions.RequestException as e:
            print(f"    Error: {e}")

        # Example 4: Update the incident
        print("\n[5] Updating incident...")
        try:
            client.update_record(
                table="incident",
                sys_id=incident_sys_id,
                fields={
                    "state": "2",  # In Progress
                    "assigned_to": "admin",
                    "work_notes": "Investigation started. Checking network logs."
                }
            )
            print(f"    Incident {incident_number} updated successfully")
            print("    New state: In Progress")
        except requests.exceptions.RequestException as e:
            print(f"    Error: {e}")

    # Example 5: Query users
    print("\n[6] Querying user records...")
    try:
        users = client.query_records(
            table="sys_user",
            query="active=true",
            limit=3,
            fields=["user_name", "name", "email", "title"]
        )

        user_list = users.get("result", [])
        print(f"    Found {len(user_list)} users (showing first 3)")

        for idx, user in enumerate(user_list, 1):
            print(f"    [{idx}] {user.get('name')} ({user.get('user_name')})")
            print(f"        Email: {user.get('email')}, Title: {user.get('title')}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 6: Query change requests
    print("\n[7] Querying recent change requests...")
    try:
        changes = client.query_records(
            table="change_request",
            query="active=true",
            limit=3,
            fields=["number", "short_description", "state", "risk", "type"]
        )

        change_list = changes.get("result", [])
        print(f"    Found {len(change_list)} change requests")

        for idx, change in enumerate(change_list, 1):
            print(f"    [{idx}] {change.get('number')}: {change.get('short_description')}")
            print(f"        Risk: {change.get('risk')}, Type: {change.get('type')}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    # Example 7: Get table schema
    print("\n[8] Fetching incident table schema...")
    try:
        schema = client.get_table_schema("incident")
        schema_data = schema.get("result", [])

        if schema_data:
            table_info = schema_data[0]
            print(f"    Table Name: {table_info.get('name')}")
            print(f"    Label: {table_info.get('label')}")
            print(f"    Super Class: {table_info.get('super_class')}")
    except requests.exceptions.RequestException as e:
        print(f"    Error: {e}")

    print("\n" + "=" * 70)
    print("API Operations Completed")
    print("=" * 70)
    print("\nNote: This is a demonstration. Replace credentials with actual values.")
    print("For production use:")
    print("  - Store credentials in environment variables")
    print("  - Use OAuth 2.0 for authentication when possible")
    print("  - Implement proper error handling and logging")
    print("  - Add retry logic for transient failures")
    print("  - Respect ServiceNow API rate limits")


if __name__ == "__main__":
    demonstrate_servicenow_api()
