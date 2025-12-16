#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "azure-purview-catalog>=1.0.0",
#     "azure-purview-scanning>=1.0.0",
#     "azure-purview-administration>=1.0.0",
#     "azure-identity>=1.12.0",
# ]
# ///

"""
Microsoft Purview Python Demonstration

This script demonstrates key capabilities of Microsoft Purview:
1. Catalog Management - Creating and managing data assets
2. Data Discovery - Searching and browsing the catalog
3. Glossary Management - Working with business terms
4. Classification - Applying data classifications
5. Lineage - Understanding data flow and relationships
"""

from typing import Dict, Any, List
import json
from datetime import datetime


class PurviewDemo:
    """
    Demonstration class for Microsoft Purview capabilities.

    Note: This is a demonstration with simulated operations.
    In production, you would use:
    - azure.purview.catalog.PurviewCatalogClient
    - azure.purview.scanning.PurviewScanningClient
    - azure.identity.DefaultAzureCredential
    """

    def __init__(self, account_name: str = "demo-purview-account"):
        """Initialize Purview demo with account details."""
        self.account_name = account_name
        self.endpoint = f"https://{account_name}.purview.azure.com"
        self.catalog_data: Dict[str, Any] = {}
        self.glossary_terms: List[Dict[str, Any]] = []
        print("[Line 42] Initialized Purview Demo")
        print(f"[Line 43] Account: {self.account_name}")
        print(f"[Line 44] Endpoint: {self.endpoint}")
        print()

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
        print("[Line 58]   - ClientSecretCredential for service principal")
        print("[Line 59]   - InteractiveBrowserCredential for user login")
        print("[Line 60] Demo: Simulating successful authentication")
        print()

    def create_data_asset(self, asset_name: str, asset_type: str,
                         properties: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a data asset in the Purview catalog.

        Args:
            asset_name: Name of the asset
            asset_type: Type (e.g., 'azure_sql_table', 'azure_blob')
            properties: Asset properties and metadata
        """
        print("[Line 75] === CREATING DATA ASSET ===")
        print(f"[Line 76] Asset Name: {asset_name}")
        print(f"[Line 77] Asset Type: {asset_type}")

        asset = {
            "name": asset_name,
            "type": asset_type,
            "guid": f"guid-{len(self.catalog_data) + 1:04d}",
            "qualifiedName": f"{self.account_name}/{asset_type}/{asset_name}",
            "properties": properties,
            "createTime": datetime.now().isoformat(),
            "classifications": []
        }

        self.catalog_data[asset["guid"]] = asset

        print(f"[Line 92] Created asset with GUID: {asset['guid']}")
        print(f"[Line 93] Qualified Name: {asset['qualifiedName']}")
        print(f"[Line 94] Properties: {json.dumps(properties, indent=2)}")
        print()

        return asset

    def apply_classification(self, asset_guid: str,
                           classification_name: str) -> None:
        """
        Apply a classification to a data asset.

        Common classifications:
        - MICROSOFT.PERSONAL.NAME
        - MICROSOFT.PERSONAL.EMAIL
        - MICROSOFT.FINANCIAL.CREDIT_CARD
        - MICROSOFT.SECURITY.COMMON_PASSWORD
        """
        print("[Line 111] === APPLYING CLASSIFICATION ===")
        print(f"[Line 112] Asset GUID: {asset_guid}")
        print(f"[Line 113] Classification: {classification_name}")

        if asset_guid in self.catalog_data:
            classification = {
                "typeName": classification_name,
                "confidence": 95,
                "source": "AutoDetect"
            }
            self.catalog_data[asset_guid]["classifications"].append(classification)
            print("[Line 122] Successfully applied classification")
            print(f"[Line 123] Confidence: {classification['confidence']}%")
        else:
            print("[Line 125] Error: Asset not found")
        print()

    def create_glossary_term(self, term_name: str, definition: str,
                            acronym: str = None) -> Dict[str, Any]:
        """
        Create a business glossary term.

        Glossary terms help establish common business vocabulary.
        """
        print("[Line 136] === CREATING GLOSSARY TERM ===")
        print(f"[Line 137] Term: {term_name}")
        print(f"[Line 138] Definition: {definition}")

        term = {
            "guid": f"term-{len(self.glossary_terms) + 1:04d}",
            "name": term_name,
            "qualifiedName": f"{term_name}@Glossary",
            "definition": definition,
            "acronym": acronym,
            "status": "Approved",
            "createTime": datetime.now().isoformat()
        }

        self.glossary_terms.append(term)

        print(f"[Line 153] Created term with GUID: {term['guid']}")
        if acronym:
            print(f"[Line 155] Acronym: {acronym}")
        print(f"[Line 156] Status: {term['status']}")
        print()

        return term

    def search_catalog(self, query: str, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Search the Purview catalog.

        Args:
            query: Search query string
            filters: Optional filters (assetType, classification, etc.)
        """
        print("[Line 170] === SEARCHING CATALOG ===")
        print(f"[Line 171] Query: '{query}'")
        if filters:
            print(f"[Line 173] Filters: {json.dumps(filters, indent=2)}")

        # Simple search simulation
        results = []
        for guid, asset in self.catalog_data.items():
            if query.lower() in asset["name"].lower():
                if not filters or self._matches_filters(asset, filters):
                    results.append(asset)

        print(f"[Line 183] Found {len(results)} result(s)")
        for i, result in enumerate(results, 1):
            print(f"[Line 185]   {i}. {result['name']} ({result['type']})")
        print()

        return results

    def _matches_filters(self, asset: Dict[str, Any],
                        filters: Dict[str, Any]) -> bool:
        """Check if asset matches the provided filters."""
        if "assetType" in filters and asset["type"] != filters["assetType"]:
            return False
        if "classification" in filters:
            classifications = [c["typeName"] for c in asset.get("classifications", [])]
            if filters["classification"] not in classifications:
                return False
        return True

    def create_lineage(self, source_guid: str, target_guid: str,
                      process_name: str) -> None:
        """
        Create data lineage showing data flow between assets.

        Args:
            source_guid: Source asset GUID
            target_guid: Target asset GUID
            process_name: Name of the process that moves data
        """
        print("[Line 213] === CREATING LINEAGE ===")
        print(f"[Line 214] Source Asset: {source_guid}")
        print(f"[Line 215] Target Asset: {target_guid}")
        print(f"[Line 216] Process: {process_name}")

        if source_guid in self.catalog_data and target_guid in self.catalog_data:
            source = self.catalog_data[source_guid]
            target = self.catalog_data[target_guid]
            print(f"[Line 221] Lineage: {source['name']} → {process_name} → {target['name']}")
            print("[Line 222] This helps track data provenance and impact analysis")
        else:
            print("[Line 224] Error: One or both assets not found")
        print()

    def get_asset_details(self, asset_guid: str) -> None:
        """Display detailed information about an asset."""
        print("[Line 230] === ASSET DETAILS ===")

        if asset_guid in self.catalog_data:
            asset = self.catalog_data[asset_guid]
            print(f"[Line 234] Name: {asset['name']}")
            print(f"[Line 235] Type: {asset['type']}")
            print(f"[Line 236] GUID: {asset['guid']}")
            print(f"[Line 237] Qualified Name: {asset['qualifiedName']}")
            print(f"[Line 238] Created: {asset['createTime']}")

            if asset["classifications"]:
                print("[Line 241] Classifications:")
                for cls in asset["classifications"]:
                    print(f"[Line 243]   - {cls['typeName']} (confidence: {cls['confidence']}%)")
            else:
                print("[Line 245] Classifications: None")

            print("[Line 247] Properties:")
            for key, value in asset["properties"].items():
                print(f"[Line 249]   - {key}: {value}")
        else:
            print("[Line 251] Error: Asset not found")
        print()

    def list_glossary_terms(self) -> None:
        """List all glossary terms."""
        print("[Line 257] === GLOSSARY TERMS ===")
        print(f"[Line 258] Total Terms: {len(self.glossary_terms)}")

        for i, term in enumerate(self.glossary_terms, 1):
            print(f"[Line 261] {i}. {term['name']}")
            print(f"[Line 262]    Definition: {term['definition']}")
            if term.get("acronym"):
                print(f"[Line 264]    Acronym: {term['acronym']}")
            print(f"[Line 265]    Status: {term['status']}")
            print()


def main():
    """Main demonstration of Microsoft Purview capabilities."""
    print("=" * 70)
    print("MICROSOFT PURVIEW PYTHON DEMONSTRATION")
    print("=" * 70)
    print()

    # Initialize Purview client
    purview = PurviewDemo(account_name="contoso-purview")

    # Step 1: Authentication
    purview.authenticate()

    # Step 2: Create data assets
    print("[Line 284] STEP 1: Creating Data Assets")
    print("-" * 70)

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

    # Step 3: Apply classifications
    print("[Line 312] STEP 2: Applying Classifications")
    print("-" * 70)

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

    # Step 4: Create glossary terms
    print("[Line 333] STEP 3: Creating Business Glossary Terms")
    print("-" * 70)

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

    # Step 5: Search the catalog
    print("[Line 357] STEP 4: Searching the Catalog")
    print("-" * 70)

    purview.search_catalog(query="customer")

    purview.search_catalog(
        query="customer",
        filters={"assetType": "azure_sql_table"}
    )

    purview.search_catalog(
        query="customer",
        filters={"classification": "MICROSOFT.PERSONAL.EMAIL"}
    )

    # Step 6: Create lineage
    print("[Line 374] STEP 5: Creating Data Lineage")
    print("-" * 70)

    purview.create_lineage(
        source_guid=sql_table["guid"],
        target_guid=blob_asset["guid"],
        process_name="Monthly ETL Job"
    )

    # Step 7: View asset details
    print("[Line 385] STEP 6: Viewing Asset Details")
    print("-" * 70)

    purview.get_asset_details(asset_guid=sql_table["guid"])

    # Step 8: List glossary terms
    print("[Line 392] STEP 7: Listing Glossary Terms")
    print("-" * 70)

    purview.list_glossary_terms()

    # Summary
    print("=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)
    print()
    print("[Line 402] Summary:")
    print(f"[Line 403] - Created {len(purview.catalog_data)} data assets")
    print("[Line 404] - Applied multiple data classifications")
    print(f"[Line 405] - Created {len(purview.glossary_terms)} glossary terms")
    print("[Line 406] - Demonstrated search and lineage capabilities")
    print()
    print("[Line 408] Key Purview Capabilities Demonstrated:")
    print("[Line 409] 1. Data Catalog - Centralized metadata repository")
    print("[Line 410] 2. Data Classification - Automatic sensitive data detection")
    print("[Line 411] 3. Business Glossary - Common business vocabulary")
    print("[Line 412] 4. Data Lineage - Track data flow and dependencies")
    print("[Line 413] 5. Data Discovery - Search and browse data assets")
    print()
    print("[Line 415] Production Usage Notes:")
    print("[Line 416] - Install: pip install azure-purview-catalog azure-identity")
    print("[Line 417] - Authentication: Use DefaultAzureCredential or service principal")
    print("[Line 418] - Endpoint: https://<account-name>.purview.azure.com")
    print("[Line 419] - Requires: Azure subscription and Purview account")
    print()


if __name__ == "__main__":
    main()
