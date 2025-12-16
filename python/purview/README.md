# Microsoft Purview Python Demonstration

This project demonstrates the core capabilities of Microsoft Purview, Microsoft's unified data governance service, using Python.

## Overview

Microsoft Purview helps organizations:
- **Discover and catalog** data assets across their data estate
- **Classify and label** sensitive data automatically
- **Understand data lineage** to track data flow and transformations
- **Establish business glossaries** for common vocabulary
- **Search and browse** data assets efficiently

## Requirements

- **Python**: 3.10 or higher
- **Dependencies**: Automatically managed via inline script metadata
  - `azure-purview-catalog>=1.0.0`
  - `azure-purview-scanning>=1.0.0`
  - `azure-purview-administration>=1.0.0`
  - `azure-identity>=1.12.0`

## Running the Demonstration

```bash
uv run python main_purview.py
```

## Code Walkthrough with Output

### 1. Initialization and Authentication

**Source Code (Lines 39-48):**
```python
def __init__(self, account_name: str = "demo-purview-account"):
    """Initialize Purview demo with account details."""
    self.account_name = account_name
    self.endpoint = f"https://{account_name}.purview.azure.com"
    self.catalog_data: Dict[str, Any] = {}
    self.glossary_terms: List[Dict[str, Any]] = []
    print("[Line 42] Initialized Purview Demo")
    print(f"[Line 43] Account: {self.account_name}")
    print(f"[Line 44] Endpoint: {self.endpoint}")
```

**Output:**
```
[Line 42] Initialized Purview Demo
[Line 43] Account: contoso-purview
[Line 44] Endpoint: https://contoso-purview.purview.azure.com
```

**Annotation:** Lines 42-44 show the initialization of the Purview client, establishing the connection endpoint. In production, this would be your actual Azure Purview account endpoint.

---

**Source Code (Lines 50-60):**
```python
def authenticate(self) -> None:
    """
    Demonstrate authentication setup.

    In production, use:
    from azure.identity import DefaultAzureCredential
    credential = DefaultAzureCredential()
    """
    print("[Line 55] === AUTHENTICATION ===")
    print("[Line 56] In production, authentication would use:")
    print("[Line 57]   - DefaultAzureCredential for managed identity")
```

**Output:**
```
[Line 55] === AUTHENTICATION ===
[Line 56] In production, authentication would use:
[Line 57]   - DefaultAzureCredential for managed identity
[Line 58]   - ClientSecretCredential for service principal
[Line 59]   - InteractiveBrowserCredential for user login
```

**Annotation:** Lines 55-60 demonstrate authentication options. Azure Purview supports multiple authentication methods including managed identities (recommended for Azure resources), service principals, and interactive browser authentication.

---

### 2. Creating Data Assets

**Source Code (Lines 287-299):**
```python
# Create a SQL table asset
sql_table = purview.create_data_asset(
    asset_name="customer_data",
    asset_type="azure_sql_table",
    properties={
        "database": "SalesDB",
        "schema": "dbo",
        "columns": ["customer_id", "name", "email", "phone", "ssn"],
        "row_count": 150000
    }
)
```

**Output:**
```
[Line 75] === CREATING DATA ASSET ===
[Line 76] Asset Name: customer_data
[Line 77] Asset Type: azure_sql_table
[Line 92] Created asset with GUID: guid-0001
[Line 93] Qualified Name: contoso-purview/azure_sql_table/customer_data
[Line 94] Properties: {
  "database": "SalesDB",
  "schema": "dbo",
  "columns": [
    "customer_id",
    "name",
    "email",
    "phone",
    "ssn"
  ],
  "row_count": 150000
}
```

**Annotation:** Lines 287-299 create a SQL table asset in the catalog. The output shows the assigned GUID (Line 92) and qualified name (Line 93) - these uniquely identify the asset. The properties (Lines 94+) capture technical metadata like database schema, columns, and row count. This is the foundation of data cataloging.

---

**Source Code (Lines 301-310):**
```python
# Create a blob storage asset
blob_asset = purview.create_data_asset(
    asset_name="customer_reports",
    asset_type="azure_blob",
    properties={
        "container": "reports",
        "path": "/customer/monthly_reports/",
        "format": "parquet",
        "size_mb": 2500
    }
)
```

**Output:**
```
[Line 75] === CREATING DATA ASSET ===
[Line 76] Asset Name: customer_reports
[Line 77] Asset Type: azure_blob
[Line 92] Created asset with GUID: guid-0002
[Line 93] Qualified Name: contoso-purview/azure_blob/customer_reports
[Line 94] Properties: {
  "container": "reports",
  "path": "/customer/monthly_reports/",
  "format": "parquet",
  "size_mb": 2500
}
```

**Annotation:** Lines 301-310 create a blob storage asset. Notice the different asset type (`azure_blob` vs `azure_sql_table`) and different properties (container, path, format). Purview supports many asset types including Azure SQL, Blob Storage, Data Lake, Cosmos DB, and on-premises sources.

---

### 3. Applying Data Classifications

**Source Code (Lines 315-328):**
```python
purview.apply_classification(
    asset_guid=sql_table["guid"],
    classification_name="MICROSOFT.PERSONAL.NAME"
)

purview.apply_classification(
    asset_guid=sql_table["guid"],
    classification_name="MICROSOFT.PERSONAL.EMAIL"
)

purview.apply_classification(
    asset_guid=sql_table["guid"],
    classification_name="MICROSOFT.PERSONAL.US_SOCIAL_SECURITY_NUMBER"
)
```

**Output:**
```
[Line 111] === APPLYING CLASSIFICATION ===
[Line 112] Asset GUID: guid-0001
[Line 113] Classification: MICROSOFT.PERSONAL.NAME
[Line 122] Successfully applied classification
[Line 123] Confidence: 95%

[Line 111] === APPLYING CLASSIFICATION ===
[Line 112] Asset GUID: guid-0001
[Line 113] Classification: MICROSOFT.PERSONAL.EMAIL
[Line 122] Successfully applied classification
[Line 123] Confidence: 95%

[Line 111] === APPLYING CLASSIFICATION ===
[Line 112] Asset GUID: guid-0001
[Line 113] Classification: MICROSOFT.PERSONAL.US_SOCIAL_SECURITY_NUMBER
[Line 122] Successfully applied classification
[Line 123] Confidence: 95%
```

**Annotation:** Lines 315-328 apply three sensitive data classifications to the customer_data table. Classifications help identify and protect sensitive information. Purview can automatically detect patterns matching personal names, email addresses, SSNs, credit cards, and other sensitive data types. The confidence level (Line 123) indicates the certainty of the classification. This is critical for compliance with GDPR, HIPAA, and other regulations.

---

### 4. Creating Business Glossary Terms

**Source Code (Lines 336-352):**
```python
purview.create_glossary_term(
    term_name="Customer",
    definition="An individual or organization that purchases products or services",
    acronym=None
)

purview.create_glossary_term(
    term_name="Personally Identifiable Information",
    definition="Data that can be used to identify, contact, or locate a single person",
    acronym="PII"
)

purview.create_glossary_term(
    term_name="Annual Recurring Revenue",
    definition="The value of recurring revenue normalized to a one-year period",
    acronym="ARR"
)
```

**Output:**
```
[Line 136] === CREATING GLOSSARY TERM ===
[Line 137] Term: Customer
[Line 138] Definition: An individual or organization that purchases products or services
[Line 153] Created term with GUID: term-0001
[Line 156] Status: Approved

[Line 136] === CREATING GLOSSARY TERM ===
[Line 137] Term: Personally Identifiable Information
[Line 138] Definition: Data that can be used to identify, contact, or locate a single person
[Line 153] Created term with GUID: term-0002
[Line 155] Acronym: PII
[Line 156] Status: Approved

[Line 136] === CREATING GLOSSARY TERM ===
[Line 137] Term: Annual Recurring Revenue
[Line 138] Definition: The value of recurring revenue normalized to a one-year period
[Line 153] Created term with GUID: term-0003
[Line 155] Acronym: ARR
[Line 156] Status: Approved
```

**Annotation:** Lines 336-352 create business glossary terms. Glossaries establish common business vocabulary across the organization, ensuring everyone uses the same definitions for key concepts. Notice that terms can have acronyms (Lines 155) and status tracking (Line 156). Glossary terms can be linked to data assets to provide business context for technical metadata.

---

### 5. Searching the Data Catalog

**Source Code (Lines 360-371):**
```python
purview.search_catalog(query="customer")

purview.search_catalog(
    query="customer",
    filters={"assetType": "azure_sql_table"}
)

purview.search_catalog(
    query="customer",
    filters={"classification": "MICROSOFT.PERSONAL.EMAIL"}
)
```

**Output:**
```
[Line 170] === SEARCHING CATALOG ===
[Line 171] Query: 'customer'
[Line 183] Found 2 result(s)
[Line 185]   1. customer_data (azure_sql_table)
[Line 185]   2. customer_reports (azure_blob)

[Line 170] === SEARCHING CATALOG ===
[Line 171] Query: 'customer'
[Line 173] Filters: {
  "assetType": "azure_sql_table"
}
[Line 183] Found 1 result(s)
[Line 185]   1. customer_data (azure_sql_table)

[Line 170] === SEARCHING CATALOG ===
[Line 171] Query: 'customer'
[Line 173] Filters: {
  "classification": "MICROSOFT.PERSONAL.EMAIL"
}
[Line 183] Found 1 result(s)
[Line 185]   1. customer_data (azure_sql_table)
```

**Annotation:** Lines 360-371 demonstrate catalog search capabilities. The first search (Line 360) finds all assets with "customer" in the name, returning 2 results (Line 183). The second search (Lines 362-365) adds a filter for only SQL tables, narrowing to 1 result. The third search (Lines 367-370) filters by classification, finding only assets containing email addresses. This shows how Purview enables data discovery through both keyword search and metadata filtering.

---

### 6. Creating Data Lineage

**Source Code (Lines 377-381):**
```python
purview.create_lineage(
    source_guid=sql_table["guid"],
    target_guid=blob_asset["guid"],
    process_name="Monthly ETL Job"
)
```

**Output:**
```
[Line 213] === CREATING LINEAGE ===
[Line 214] Source Asset: guid-0001
[Line 215] Target Asset: guid-0002
[Line 216] Process: Monthly ETL Job
[Line 221] Lineage: customer_data → Monthly ETL Job → customer_reports
[Line 222] This helps track data provenance and impact analysis
```

**Annotation:** Lines 377-381 establish data lineage between the SQL table and blob storage. Line 221 shows the data flow: customer_data (source) → Monthly ETL Job (process) → customer_reports (target). Lineage tracking is essential for understanding data provenance (where data comes from), impact analysis (what breaks if you change something), and compliance auditing (how data moves through your systems).

---

### 7. Viewing Asset Details

**Source Code (Lines 388):**
```python
purview.get_asset_details(asset_guid=sql_table["guid"])
```

**Output:**
```
[Line 230] === ASSET DETAILS ===
[Line 234] Name: customer_data
[Line 235] Type: azure_sql_table
[Line 236] GUID: guid-0001
[Line 237] Qualified Name: contoso-purview/azure_sql_table/customer_data
[Line 238] Created: 2025-12-16T16:06:22.980901
[Line 241] Classifications:
[Line 243]   - MICROSOFT.PERSONAL.NAME (confidence: 95%)
[Line 243]   - MICROSOFT.PERSONAL.EMAIL (confidence: 95%)
[Line 243]   - MICROSOFT.PERSONAL.US_SOCIAL_SECURITY_NUMBER (confidence: 95%)
[Line 247] Properties:
[Line 249]   - database: SalesDB
[Line 249]   - schema: dbo
[Line 249]   - columns: ['customer_id', 'name', 'email', 'phone', 'ssn']
[Line 249]   - row_count: 150000
```

**Annotation:** Line 388 retrieves complete details for an asset. The output shows all metadata including identification (Lines 234-237), creation timestamp (Line 238), applied classifications (Lines 241-243), and technical properties (Lines 247-249). This comprehensive view helps data stewards, analysts, and engineers understand what data exists and how it's classified.

---

### 8. Listing Glossary Terms

**Source Code (Lines 395):**
```python
purview.list_glossary_terms()
```

**Output:**
```
[Line 257] === GLOSSARY TERMS ===
[Line 258] Total Terms: 3
[Line 261] 1. Customer
[Line 262]    Definition: An individual or organization that purchases products or services
[Line 265]    Status: Approved

[Line 261] 2. Personally Identifiable Information
[Line 262]    Definition: Data that can be used to identify, contact, or locate a single person
[Line 264]    Acronym: PII
[Line 265]    Status: Approved

[Line 261] 3. Annual Recurring Revenue
[Line 262]    Definition: The value of recurring revenue normalized to a one-year period
[Line 264]    Acronym: ARR
[Line 265]    Status: Approved
```

**Annotation:** Line 395 lists all glossary terms with their definitions. Notice how each term (Lines 261-265) includes its definition and status. Terms like "PII" (Line 264) show acronyms for common business terminology. This creates a shared business vocabulary across teams.

---

### 9. Summary and Key Capabilities

**Output:**
```
[Line 402] Summary:
[Line 403] - Created 2 data assets
[Line 404] - Applied multiple data classifications
[Line 405] - Created 3 glossary terms
[Line 406] - Demonstrated search and lineage capabilities

[Line 408] Key Purview Capabilities Demonstrated:
[Line 409] 1. Data Catalog - Centralized metadata repository
[Line 410] 2. Data Classification - Automatic sensitive data detection
[Line 411] 3. Business Glossary - Common business vocabulary
[Line 412] 4. Data Lineage - Track data flow and dependencies
[Line 413] 5. Data Discovery - Search and browse data assets

[Line 415] Production Usage Notes:
[Line 416] - Install: pip install azure-purview-catalog azure-identity
[Line 417] - Authentication: Use DefaultAzureCredential or service principal
[Line 418] - Endpoint: https://<account-name>.purview.azure.com
[Line 419] - Requires: Azure subscription and Purview account
```

**Annotation:** The summary (Lines 402-419) recaps what was demonstrated and provides production deployment guidance. To use Purview in production, you need an Azure subscription, a Purview account provisioned in Azure, and proper authentication credentials.

---

## Key Features Demonstrated

### 1. **Data Catalog Management**
- Creating assets for different data sources (SQL, Blob Storage)
- Capturing technical metadata (schemas, columns, properties)
- Organizing assets with qualified names and GUIDs

### 2. **Data Classification**
- Applying Microsoft's built-in classifications
- Identifying sensitive data (PII, emails, SSNs)
- Confidence scoring for classifications

### 3. **Business Glossary**
- Defining business terms and acronyms
- Establishing common vocabulary
- Linking business context to technical assets

### 4. **Data Lineage**
- Tracking data flow between systems
- Understanding ETL processes
- Impact analysis and data provenance

### 5. **Data Discovery**
- Keyword-based search
- Filtered search by asset type
- Classification-based filtering

## Production Deployment

### Prerequisites
1. **Azure Subscription**: Active Azure account
2. **Purview Account**: Create a Purview account in Azure Portal
3. **Permissions**: Data Curator or Data Reader role in Purview

### Real-World Code Example
```python
from azure.purview.catalog import PurviewCatalogClient
from azure.identity import DefaultAzureCredential

# Production authentication
credential = DefaultAzureCredential()
endpoint = "https://your-account.purview.azure.com"
client = PurviewCatalogClient(endpoint=endpoint, credential=credential)

# Search for assets
results = client.discovery.query(
    keywords="customer",
    limit=100
)

# Get asset details
asset = client.entity.get_by_guid(guid="...")
```

## Use Cases

1. **Compliance & Governance**
   - Identify where sensitive data (PII, PHI) lives
   - Track data lineage for audit trails
   - Enforce data classification policies

2. **Data Discovery**
   - Help analysts find relevant datasets
   - Understand what data is available
   - Browse data catalogs by business terms

3. **Impact Analysis**
   - Understand downstream dependencies before changes
   - Track data flow through ETL pipelines
   - Identify affected systems

4. **Data Quality**
   - Document data schemas and definitions
   - Establish business glossaries
   - Create consistent metadata standards

## Additional Resources

- [Microsoft Purview Documentation](https://docs.microsoft.com/azure/purview/)
- [Python SDK Reference](https://docs.microsoft.com/python/api/overview/azure/purview)
- [REST API Documentation](https://docs.microsoft.com/rest/api/purview/)

---

**Note**: This demonstration uses simulated operations for educational purposes. In production, you would connect to a real Azure Purview account and work with actual data sources registered in your data catalog.
