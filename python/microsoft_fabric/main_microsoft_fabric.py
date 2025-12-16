#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "azure-identity>=1.15.0",
#     "requests>=2.31.0",
#     "pandas>=2.0.0",
#     "tabulate>=0.9.0",
# ]
# ///

"""
Microsoft Fabric Python API Demonstration

This script demonstrates key Microsoft Fabric capabilities:
1. Authentication using Azure Identity
2. Workspace Management
3. Lakehouse Operations
4. Semantic Model Interaction
5. Data Pipeline Operations
6. Real-time Analytics

Note: This is a demonstration using Microsoft Fabric REST APIs.
In production, you would use actual credentials and workspace IDs.
"""

from typing import Any
import requests

# Azure imports are optional for demo mode
try:
    from azure.identity import ClientSecretCredential
    AZURE_AVAILABLE = True
except ImportError:
    AZURE_AVAILABLE = False
    ClientSecretCredential = None  # type: ignore


class FabricClient:
    """Client for interacting with Microsoft Fabric APIs."""

    def __init__(self, tenant_id: str = "demo", client_id: str = "demo",
                 client_secret: str = "demo", use_demo: bool = True):
        """
        Initialize Fabric client with authentication.

        Args:
            tenant_id: Azure AD tenant ID
            client_id: Application (client) ID
            client_secret: Client secret
            use_demo: If True, runs in demo mode without actual API calls
        """
        self.base_url = "https://api.fabric.microsoft.com/v1"
        self.use_demo = use_demo

        if not use_demo:
            if not AZURE_AVAILABLE:
                msg = "azure-identity package required for non-demo mode"
                raise ImportError(msg)
            # Line 50-53: Real authentication using Azure AD credentials
            self.credential = ClientSecretCredential(
                tenant_id=tenant_id,
                client_id=client_id,
                client_secret=client_secret
            )
            # Get access token for Fabric API
            self.token = self.credential.get_token(
                "https://analysis.windows.net/powerbi/api/.default"
            ).token
        else:
            print("📋 Running in DEMO mode - simulating API responses\n")
            self.token = "demo_token"

    def _make_request(self, method: str, endpoint: str,
                      data: dict[str, Any] | None = None) -> dict[str, Any]:
        """Make HTTP request to Fabric API."""
        if self.use_demo:
            return self._simulate_response(endpoint, method, data)

        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        url = f"{self.base_url}{endpoint}"

        response = requests.request(method, url, headers=headers,
                                    json=data, timeout=30)
        response.raise_for_status()
        return response.json() if response.content else {}

    def _simulate_response(self, endpoint: str, method: str,
                          data: dict[str, Any] | None) -> dict[str, Any]:
        """Simulate API responses for demo mode."""
        # Line 81-124: Simulated responses for various Fabric API endpoints
        # Check more specific endpoints first
        if "lakehouses" in endpoint and method == "POST":
            return {
                "id": "lh-98765",
                "displayName": data.get("displayName", "NewLakehouse"),
                "type": "Lakehouse",
                "workspaceId": "ws-12345"
            }
        elif "lakehouses" in endpoint and method == "GET":
            return {
                "value": [
                    {
                        "id": "lh-11111",
                        "displayName": "SalesDataLakehouse",
                        "type": "Lakehouse",
                        "properties": {
                            "sqlEndpointConnectionString":
                                "sql-endpoint-12345.fabric.microsoft.com"
                        }
                    }
                ]
            }
        elif "semanticModels" in endpoint:
            return {
                "value": [
                    {
                        "id": "sm-55555",
                        "name": "Sales Analytics Model",
                        "targetStorageMode": "DirectLake"
                    }
                ]
            }
        elif "workspaces" in endpoint and method == "GET":
            return {
                "value": [
                    {
                        "id": "ws-12345",
                        "displayName": "Analytics Workspace",
                        "type": "Workspace",
                        "capacityId": "cap-67890"
                    },
                    {
                        "id": "ws-23456",
                        "displayName": "Data Engineering Hub",
                        "type": "Workspace",
                        "capacityId": "cap-67890"
                    }
                ]
            }
        return {}

    def list_workspaces(self) -> list[dict[str, Any]]:
        """List all Fabric workspaces."""
        # Line 136: Retrieve all workspaces in the Fabric tenant
        response = self._make_request("GET", "/workspaces")
        return response.get("value", [])

    def create_lakehouse(self, workspace_id: str,
                        lakehouse_name: str) -> dict[str, Any]:
        """
        Create a new Lakehouse in a workspace.

        A Lakehouse in Fabric combines data lake and data warehouse capabilities.
        """
        # Line 147-152: Create a new lakehouse with specified name
        endpoint = f"/workspaces/{workspace_id}/lakehouses"
        payload = {
            "displayName": lakehouse_name,
            "description": "Demo lakehouse for analytics"
        }
        return self._make_request("POST", endpoint, payload)

    def list_lakehouses(self, workspace_id: str) -> list[dict[str, Any]]:
        """List all lakehouses in a workspace."""
        # Line 157: Get all lakehouses within a specific workspace
        endpoint = f"/workspaces/{workspace_id}/lakehouses"
        response = self._make_request("GET", endpoint)
        return response.get("value", [])

    def get_semantic_models(self, workspace_id: str) -> list[dict[str, Any]]:
        """
        Retrieve semantic models (formerly known as datasets) from workspace.

        Semantic models define the business logic and relationships in your data.
        """
        # Line 167-168: Fetch semantic models for data analysis
        endpoint = f"/workspaces/{workspace_id}/semanticModels"
        response = self._make_request("GET", endpoint)
        return response.get("value", [])

    def create_data_pipeline(self, workspace_id: str,
                            pipeline_name: str) -> dict[str, Any]:
        """Create a data pipeline for ETL operations."""
        # Line 176-181: Define a new data pipeline with activities
        endpoint = f"/workspaces/{workspace_id}/dataPipelines"
        payload = {
            "displayName": pipeline_name,
            "description": "ETL pipeline for data ingestion"
        }
        return self._make_request("POST", endpoint, payload)


def demonstrate_workspace_operations(client: FabricClient) -> None:
    """Demonstrate workspace listing and management."""
    print("=" * 70)
    print("1. WORKSPACE OPERATIONS")
    print("=" * 70)

    # Line 192: List all available workspaces
    workspaces = client.list_workspaces()
    print(f"\n📁 Found {len(workspaces)} workspace(s):\n")

    for idx, workspace in enumerate(workspaces, 1):
        # Line 197-200: Display workspace details
        print(f"   {idx}. Workspace: {workspace['displayName']}")
        print(f"      ID: {workspace['id']}")
        print(f"      Type: {workspace['type']}")
        print(f"      Capacity: {workspace['capacityId']}\n")


def demonstrate_lakehouse_operations(client: FabricClient,
                                    workspace_id: str) -> None:
    """Demonstrate lakehouse creation and listing."""
    print("\n" + "=" * 70)
    print("2. LAKEHOUSE OPERATIONS")
    print("=" * 70)

    # Line 213: Create a new lakehouse for data storage
    print("\n🏗️  Creating new lakehouse...")
    new_lakehouse = client.create_lakehouse(workspace_id,
                                           "CustomerDataLake")
    print(f"   ✓ Created: {new_lakehouse['displayName']}")
    print(f"   ✓ ID: {new_lakehouse['id']}")
    print(f"   ✓ Type: {new_lakehouse['type']}\n")

    # Line 222: List all lakehouses in the workspace
    print("📊 Listing all lakehouses in workspace:")
    lakehouses = client.list_lakehouses(workspace_id)

    for idx, lh in enumerate(lakehouses, 1):
        # Line 227-231: Display lakehouse details including SQL endpoint
        print(f"\n   {idx}. {lh['displayName']}")
        print(f"      ID: {lh['id']}")
        if 'properties' in lh:
            sql_endpoint = lh['properties'].get('sqlEndpointConnectionString',
                                               'N/A')
            print(f"      SQL Endpoint: {sql_endpoint}")


def demonstrate_semantic_model_operations(client: FabricClient,
                                         workspace_id: str) -> None:
    """Demonstrate semantic model retrieval and analysis."""
    print("\n" + "=" * 70)
    print("3. SEMANTIC MODEL OPERATIONS")
    print("=" * 70)

    # Line 244: Retrieve semantic models for business intelligence
    print("\n🎯 Retrieving semantic models...")
    models = client.get_semantic_models(workspace_id)

    if models:
        print(f"   Found {len(models)} semantic model(s):\n")
        for idx, model in enumerate(models, 1):
            # Line 251-254: Display model details and storage mode
            print(f"   {idx}. Model: {model['name']}")
            print(f"      ID: {model['id']}")
            print(f"      Storage Mode: {model.get('targetStorageMode', 'N/A')}")
            print()
    else:
        print("   No semantic models found.")


def demonstrate_data_pipeline_operations(client: FabricClient,
                                        workspace_id: str) -> None:
    """Demonstrate data pipeline creation."""
    print("\n" + "=" * 70)
    print("4. DATA PIPELINE OPERATIONS")
    print("=" * 70)

    # Line 269: Create ETL pipeline for data processing
    print("\n⚙️  Creating data pipeline...")
    pipeline = client.create_data_pipeline(workspace_id,
                                          "DailyDataIngestionPipeline")
    print(f"   ✓ Pipeline Created: {pipeline.get('displayName', 'N/A')}")
    print(f"   ✓ Description: {pipeline.get('description', 'N/A')}")


def demonstrate_fabric_architecture() -> None:
    """Display Microsoft Fabric architecture overview."""
    print("\n" + "=" * 70)
    print("5. MICROSOFT FABRIC ARCHITECTURE OVERVIEW")
    print("=" * 70)

    architecture = """
    Microsoft Fabric Components:

    ┌─────────────────────────────────────────────────────────────┐
    │                    MICROSOFT FABRIC                         │
    ├─────────────────────────────────────────────────────────────┤
    │                                                             │
    │  📊 Data Engineering    🏭 Data Factory                     │
    │     • Lakehouses           • Data Pipelines                 │
    │     • Notebooks            • Dataflows Gen2                 │
    │     • Spark Jobs                                            │
    │                                                             │
    │  🔬 Data Science        📈 Power BI                         │
    │     • Experiments          • Semantic Models                │
    │     • Models               • Reports                        │
    │     • ML Experiments       • Dashboards                     │
    │                                                             │
    │  ⚡ Real-time Analytics  🗄️  Data Warehouse                │
    │     • KQL Databases        • SQL Analytics                  │
    │     • Event Streams        • T-SQL Support                  │
    │                                                             │
    ├─────────────────────────────────────────────────────────────┤
    │              OneLake (Unified Data Lake)                    │
    │         All data stored in Delta Lake format                │
    └─────────────────────────────────────────────────────────────┘
    """
    # Line 285-313: Visual representation of Fabric's unified platform
    print(architecture)


def main() -> None:
    """Main execution function demonstrating Microsoft Fabric capabilities."""
    print("\n" + "=" * 70)
    print("   MICROSOFT FABRIC PYTHON API DEMONSTRATION")
    print("=" * 70)
    print("\nMicrosoft Fabric is a unified analytics platform that brings")
    print("together data engineering, data science, real-time analytics,")
    print("data warehousing, and business intelligence.\n")

    # Line 327: Initialize Fabric client in demo mode
    client = FabricClient(use_demo=True)

    # Line 330: Demonstrate workspace management
    demonstrate_workspace_operations(client)

    # Use the first workspace for subsequent demos
    # Line 334: Get workspace ID for lakehouse operations
    workspaces = client.list_workspaces()
    if workspaces:
        workspace_id = workspaces[0]["id"]

        # Line 339: Demonstrate lakehouse creation and management
        demonstrate_lakehouse_operations(client, workspace_id)

        # Line 342: Demonstrate semantic model retrieval
        demonstrate_semantic_model_operations(client, workspace_id)

        # Line 345: Demonstrate data pipeline creation
        demonstrate_data_pipeline_operations(client, workspace_id)

    # Line 348: Display Fabric architecture overview
    demonstrate_fabric_architecture()

    print("\n" + "=" * 70)
    print("KEY FABRIC CONCEPTS")
    print("=" * 70)
    print("""
    🏢 Workspace: Container for Fabric items (lakehouses, notebooks, etc.)
    🗄️  Lakehouse: Combines data lake and warehouse capabilities
    🎯 Semantic Model: Business logic layer for analytics (formerly Dataset)
    ⚙️  Data Pipeline: ETL/ELT orchestration for data movement
    📊 OneLake: Unified data lake built on Azure Data Lake Storage Gen2
    ⚡ Capacity: Compute resources allocated for Fabric workloads
    """)

    print("\n" + "=" * 70)
    print("AUTHENTICATION IN PRODUCTION")
    print("=" * 70)
    print("""
    For production use, you need:

    1. Azure AD App Registration:
       - Register app in Azure Portal
       - Grant Fabric API permissions
       - Create client secret

    2. Environment Variables:
       export AZURE_TENANT_ID="your-tenant-id"
       export AZURE_CLIENT_ID="your-client-id"
       export AZURE_CLIENT_SECRET="your-client-secret"

    3. Initialize client:
       client = FabricClient(
           tenant_id=os.getenv("AZURE_TENANT_ID"),
           client_id=os.getenv("AZURE_CLIENT_ID"),
           client_secret=os.getenv("AZURE_CLIENT_SECRET"),
           use_demo=False
       )

    Documentation: https://learn.microsoft.com/fabric/
    """)

    print("=" * 70)
    print("Demonstration completed successfully!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
