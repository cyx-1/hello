# Microsoft Fabric Python API Demonstration

This demonstration showcases how to interact with Microsoft Fabric using Python and the Fabric REST APIs. Microsoft Fabric is Microsoft's unified analytics platform that brings together data engineering, data science, real-time analytics, data warehousing, and business intelligence.

## Requirements

- **Python Version**: Python 3.10 or higher
- **Dependencies**:
  - `azure-identity>=1.15.0` (for authentication)
  - `requests>=2.31.0` (for API calls)
  - `pandas>=2.0.0` (for data handling)
  - `tabulate>=0.9.0` (for formatting)

## Running the Demo

```bash
uv run python main_microsoft_fabric.py
```

The script runs in **demo mode** by default, simulating API responses without requiring actual credentials.

## Key Features Demonstrated

1. **Authentication with Azure AD** (Lines 46-72)
2. **Workspace Management** (Lines 146-149, 192-202)
3. **Lakehouse Operations** (Lines 151-171, 213-233)
4. **Semantic Models** (Lines 173-180, 244-260)
5. **Data Pipeline Creation** (Lines 182-191, 269-276)

---

## Source Code and Output Correlation

### 1. Client Initialization (Lines 27-72)

**Source Code:**
```python
27  from typing import Any
28  import requests
29
30  # Azure imports are optional for demo mode
31  try:
32      from azure.identity import ClientSecretCredential
33      AZURE_AVAILABLE = True
34  except ImportError:
35      AZURE_AVAILABLE = False
36      ClientSecretCredential = None  # type: ignore
37
38
39  class FabricClient:
40      """Client for interacting with Microsoft Fabric APIs."""
41
42      def __init__(self, tenant_id: str = "demo", client_id: str = "demo",
43                   client_secret: str = "demo", use_demo: bool = True):
...
56          if not use_demo:
57              if not AZURE_AVAILABLE:
58                  msg = "azure-identity package required for non-demo mode"
59                  raise ImportError(msg)
60              # Line 50-53: Real authentication using Azure AD credentials
61              self.credential = ClientSecretCredential(
62                  tenant_id=tenant_id,
63                  client_id=client_id,
64                  client_secret=client_secret
65              )
66              # Get access token for Fabric API
67              self.token = self.credential.get_token(
68                  "https://analysis.windows.net/powerbi/api/.default"
69              ).token
70          else:
71              print("📋 Running in DEMO mode - simulating API responses\n")
72              self.token = "demo_token"
```

**Output:**
```
📋 Running in DEMO mode - simulating API responses
```

**Annotation:** Lines 70-72 detect demo mode and print a message indicating that the script will simulate API responses instead of making real calls to Microsoft Fabric.

---

### 2. Workspace Listing (Lines 146-149, 192-202)

**Source Code:**
```python
146  def list_workspaces(self) -> list[dict[str, Any]]:
147      """List all Fabric workspaces."""
148      # Line 136: Retrieve all workspaces in the Fabric tenant
149      response = self._make_request("GET", "/workspaces")
150      return response.get("value", [])
...
192  # Line 192: List all available workspaces
193  workspaces = client.list_workspaces()
194  print(f"\n📁 Found {len(workspaces)} workspace(s):\n")
195
196  for idx, workspace in enumerate(workspaces, 1):
197      # Line 197-200: Display workspace details
198      print(f"   {idx}. Workspace: {workspace['displayName']}")
199      print(f"      ID: {workspace['id']}")
200      print(f"      Type: {workspace['type']}")
201      print(f"      Capacity: {workspace['capacityId']}\n")
```

**Output:**
```
======================================================================
1. WORKSPACE OPERATIONS
======================================================================

📁 Found 2 workspace(s):

   1. Workspace: Analytics Workspace
      ID: ws-12345
      Type: Workspace
      Capacity: cap-67890

   2. Workspace: Data Engineering Hub
      ID: ws-23456
      Type: Workspace
      Capacity: cap-67890
```

**Annotation:** Line 149 makes a GET request to `/workspaces` endpoint. Lines 196-201 iterate through the returned workspaces and display their details. In demo mode (lines 127-143), the API returns two simulated workspaces with IDs, names, types, and capacity information.

---

### 3. Lakehouse Creation (Lines 151-165, 213-221)

**Source Code:**
```python
151  def create_lakehouse(self, workspace_id: str,
152                      lakehouse_name: str) -> dict[str, Any]:
153      """
154      Create a new Lakehouse in a workspace.
155
156      A Lakehouse in Fabric combines data lake and data warehouse capabilities.
157      """
158      # Line 147-152: Create a new lakehouse with specified name
159      endpoint = f"/workspaces/{workspace_id}/lakehouses"
160      payload = {
161          "displayName": lakehouse_name,
162          "description": "Demo lakehouse for analytics"
163      }
164      return self._make_request("POST", endpoint, payload)
...
213  # Line 213: Create a new lakehouse for data storage
214  print("\n🏗️  Creating new lakehouse...")
215  new_lakehouse = client.create_lakehouse(workspace_id,
216                                         "CustomerDataLake")
217  print(f"   ✓ Created: {new_lakehouse['displayName']}")
218  print(f"   ✓ ID: {new_lakehouse['id']}")
219  print(f"   ✓ Type: {new_lakehouse['type']}\n")
```

**Output:**
```
======================================================================
2. LAKEHOUSE OPERATIONS
======================================================================

🏗️  Creating new lakehouse...
   ✓ Created: CustomerDataLake
   ✓ ID: lh-98765
   ✓ Type: Lakehouse
```

**Annotation:** Lines 159-164 create a POST request to create a new lakehouse named "CustomerDataLake" in the specified workspace. Lines 217-219 display the returned lakehouse details including its ID and type. The simulated response (lines 96-102) returns a lakehouse object with ID "lh-98765".

---

### 4. Lakehouse Listing (Lines 166-171, 222-233)

**Source Code:**
```python
166  def list_lakehouses(self, workspace_id: str) -> list[dict[str, Any]]:
167      """List all lakehouses in a workspace."""
168      # Line 157: Get all lakehouses within a specific workspace
169      endpoint = f"/workspaces/{workspace_id}/lakehouses"
170      response = self._make_request("GET", endpoint)
171      return response.get("value", [])
...
222  # Line 222: List all lakehouses in the workspace
223  print("📊 Listing all lakehouses in workspace:")
224  lakehouses = client.list_lakehouses(workspace_id)
225
226  for idx, lh in enumerate(lakehouses, 1):
227      # Line 227-231: Display lakehouse details including SQL endpoint
228      print(f"\n   {idx}. {lh['displayName']}")
229      print(f"      ID: {lh['id']}")
230      if 'properties' in lh:
231          sql_endpoint = lh['properties'].get('sqlEndpointConnectionString',
232                                             'N/A')
233          print(f"      SQL Endpoint: {sql_endpoint}")
```

**Output:**
```
📊 Listing all lakehouses in workspace:

   1. SalesDataLakehouse
      ID: lh-11111
      SQL Endpoint: sql-endpoint-12345.fabric.microsoft.com
```

**Annotation:** Line 169 makes a GET request to list all lakehouses in a workspace. Lines 226-233 iterate through the returned lakehouses and display their details, including the SQL endpoint connection string for querying data. The simulated response (lines 103-116) returns a lakehouse with SQL endpoint information.

---

### 5. Semantic Models (Lines 173-180, 244-260)

**Source Code:**
```python
173  def get_semantic_models(self, workspace_id: str) -> list[dict[str, Any]]:
174      """
175      Retrieve semantic models (formerly known as datasets) from workspace.
176
177      Semantic models define the business logic and relationships in your data.
178      """
179      # Line 167-168: Fetch semantic models for data analysis
180      endpoint = f"/workspaces/{workspace_id}/semanticModels"
181      response = self._make_request("GET", endpoint)
182      return response.get("value", [])
...
244  # Line 244: Retrieve semantic models for business intelligence
245  print("\n🎯 Retrieving semantic models...")
246  models = client.get_semantic_models(workspace_id)
247
248  if models:
249      print(f"   Found {len(models)} semantic model(s):\n")
250      for idx, model in enumerate(models, 1):
251          # Line 251-254: Display model details and storage mode
252          print(f"   {idx}. Model: {model['name']}")
253          print(f"      ID: {model['id']}")
254          print(f"      Storage Mode: {model.get('targetStorageMode', 'N/A')}")
255          print()
```

**Output:**
```
======================================================================
3. SEMANTIC MODEL OPERATIONS
======================================================================

🎯 Retrieving semantic models...
   Found 1 semantic model(s):

   1. Model: Sales Analytics Model
      ID: sm-55555
      Storage Mode: DirectLake
```

**Annotation:** Line 180 requests semantic models from the workspace. Lines 250-255 display model details including the storage mode. The "DirectLake" storage mode (line 254) is a key Fabric feature that enables direct querying of data in the lakehouse without importing it, providing real-time analytics capabilities.

---

### 6. Data Pipeline Creation (Lines 182-191, 269-276)

**Source Code:**
```python
182  def create_data_pipeline(self, workspace_id: str,
183                          pipeline_name: str) -> dict[str, Any]:
184      """Create a data pipeline for ETL operations."""
185      # Line 176-181: Define a new data pipeline with activities
186      endpoint = f"/workspaces/{workspace_id}/dataPipelines"
187      payload = {
188          "displayName": pipeline_name,
189          "description": "ETL pipeline for data ingestion"
190      }
191      return self._make_request("POST", endpoint, payload)
...
269  # Line 269: Create ETL pipeline for data processing
270  print("\n⚙️  Creating data pipeline...")
271  pipeline = client.create_data_pipeline(workspace_id,
272                                        "DailyDataIngestionPipeline")
273  print(f"   ✓ Pipeline Created: {pipeline.get('displayName', 'N/A')}")
274  print(f"   ✓ Description: {pipeline.get('description', 'N/A')}")
```

**Output:**
```
======================================================================
4. DATA PIPELINE OPERATIONS
======================================================================

⚙️  Creating data pipeline...
   ✓ Pipeline Created: N/A
   ✓ Description: N/A
```

**Annotation:** Lines 186-191 create a POST request to define a new data pipeline. Data pipelines in Fabric orchestrate ETL/ELT operations for data movement and transformation. In production environments, these pipelines would contain activities for copying data, transforming it, and loading it into destination systems.

---

### 7. Fabric Architecture Overview (Lines 285-313)

**Source Code:**
```python
285  # Line 285-313: Visual representation of Fabric's unified platform
286  print(architecture)
```

**Output:**
```
======================================================================
5. MICROSOFT FABRIC ARCHITECTURE OVERVIEW
======================================================================

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
```

**Annotation:** Lines 285-313 display a visual representation of Microsoft Fabric's architecture, showing how it unifies multiple analytics workloads (data engineering, data science, real-time analytics, data warehousing, and business intelligence) on a single platform with OneLake as the unified storage layer.

---

### 8. Key Concepts and Production Setup

**Output:**
```
======================================================================
KEY FABRIC CONCEPTS
======================================================================

    🏢 Workspace: Container for Fabric items (lakehouses, notebooks, etc.)
    🗄️  Lakehouse: Combines data lake and warehouse capabilities
    🎯 Semantic Model: Business logic layer for analytics (formerly Dataset)
    ⚙️  Data Pipeline: ETL/ELT orchestration for data movement
    📊 OneLake: Unified data lake built on Azure Data Lake Storage Gen2
    ⚡ Capacity: Compute resources allocated for Fabric workloads


======================================================================
AUTHENTICATION IN PRODUCTION
======================================================================

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
```

**Annotation:** The script concludes by explaining key Microsoft Fabric concepts and providing instructions for setting up authentication in production environments. To use the real Fabric APIs, you need to register an application in Azure AD, grant it appropriate permissions, and provide credentials through environment variables.

---

## Microsoft Fabric Key Capabilities

### 1. **OneLake (Unified Storage)**
All data in Microsoft Fabric is stored in OneLake, a unified data lake based on Azure Data Lake Storage Gen2. OneLake uses Delta Lake format for ACID transactions and time travel capabilities.

### 2. **Lakehouses**
Lakehouses combine the flexibility of data lakes with the performance of data warehouses. They support:
- Structured and unstructured data
- SQL querying through SQL endpoints
- Apache Spark for data processing
- Direct Lake mode for Power BI semantic models

### 3. **Semantic Models (formerly Datasets)**
Semantic models provide a business logic layer on top of your data, defining:
- Relationships between tables
- Calculated columns and measures
- Row-level security
- Direct Lake connectivity for real-time analytics

### 4. **Data Pipelines**
Data pipelines orchestrate data movement and transformation:
- Copy data from various sources
- Transform data using dataflows or notebooks
- Schedule recurring data refreshes
- Monitor and manage data workflows

### 5. **Workspaces**
Workspaces are containers that organize related Fabric items:
- Lakehouses
- Data pipelines
- Notebooks
- Reports and dashboards
- Semantic models

---

## Version Requirements

**This code requires Python 3.10 or higher** due to:
- Modern type hint syntax (`dict[str, Any]` instead of `Dict[str, Any]`)
- Improved pattern matching capabilities
- Enhanced error messages

For production use with real Microsoft Fabric APIs:
- Azure AD tenant with Microsoft Fabric enabled
- Fabric capacity (F SKU or Power BI Premium P SKU)
- Service principal with appropriate Fabric permissions

---

## Additional Resources

- **Official Documentation**: https://learn.microsoft.com/fabric/
- **Fabric REST API Reference**: https://learn.microsoft.com/rest/api/fabric/
- **Python SDK (Coming Soon)**: https://github.com/microsoft/semantic-link-labs
- **Fabric Community**: https://community.fabric.microsoft.com/

---

## Summary

This demonstration illustrates the core capabilities of Microsoft Fabric through Python:

1. **Lines 46-72**: Authentication setup with Azure AD
2. **Lines 146-150, 192-202**: Workspace management and listing
3. **Lines 151-165, 213-221**: Creating lakehouses for unified storage
4. **Lines 166-171, 222-233**: Listing lakehouses with SQL endpoints
5. **Lines 173-182, 244-260**: Retrieving semantic models for BI
6. **Lines 182-191, 269-276**: Creating data pipelines for ETL
7. **Lines 285-313**: Understanding Fabric's unified architecture

The script runs in demo mode by default, making it easy to understand Fabric's API structure without requiring actual credentials.
