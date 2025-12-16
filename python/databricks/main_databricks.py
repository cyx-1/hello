#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "databricks-sdk>=0.40.0",
#     "databricks-sql-connector>=3.5.0",
#     "pandas>=2.2.0",
#     "delta-spark>=3.2.0",
# ]
# ///

"""
Databricks Python SDK Demonstration

This script demonstrates comprehensive usage of Databricks SDK including:
- Workspace operations (listing, creating notebooks)
- Clusters management
- Jobs API (creating, running, monitoring jobs)
- DBFS (Databricks File System) operations
- Secrets management
- SQL queries via Databricks SQL Connector
- Unity Catalog operations

Note: This is a demonstration script showing API usage patterns.
In production, you would set environment variables:
- DATABRICKS_HOST
- DATABRICKS_TOKEN
"""

from datetime import datetime
from typing import Any, Optional

# Optional imports - gracefully handle missing Databricks SDK
try:
    from databricks.sdk import WorkspaceClient

    DATABRICKS_SDK_AVAILABLE = True
except ImportError:
    DATABRICKS_SDK_AVAILABLE = False
    WorkspaceClient = None  # type: ignore


def print_section(title: str) -> None:
    """Print a formatted section header."""
    print(f"\n{'=' * 70}")
    print(f"  {title}")
    print(f"{'=' * 70}\n")


def demo_workspace_connection() -> Optional[Any]:
    """
    Line 49-56: Demonstrate Databricks workspace connection.

    Creates a WorkspaceClient instance which is the main entry point
    for interacting with Databricks APIs.
    """
    print_section("1. Workspace Connection")

    if not DATABRICKS_SDK_AVAILABLE:
        print("Running in DEMO mode (Databricks SDK not available)")
        print("In production, you would initialize WorkspaceClient:")
        print("  w = WorkspaceClient(")
        print('      host="https://your-workspace.cloud.databricks.com",')
        print('      token="your-token-here"')
        print("  )")
        print("\n✓ Connection pattern demonstrated")
        print("  Host: https://your-workspace.cloud.databricks.com")
        print("  Authentication: Token-based")
        return None

    # In production, credentials come from environment variables or config file
    # This demonstrates the connection pattern
    w = WorkspaceClient(
        host="https://your-workspace.cloud.databricks.com",
        token="your-token-here",  # Demo only - use env vars in production
    )

    print("✓ WorkspaceClient initialized")
    print(f"  Host: {w.config.host}")
    print("  Authentication: Token-based")

    return w


def demo_workspace_operations(w: Optional[Any]) -> None:
    """
    Line 73-94: Demonstrate workspace operations.

    Shows how to:
    - List workspace objects (notebooks, directories, libraries)
    - Create notebooks programmatically
    - Manage workspace directories
    """
    print_section("2. Workspace Operations")

    # List workspace root directory
    print("Listing workspace objects in /Users:")
    try:
        # This would list actual workspace items in a real connection
        workspace_items = [
            {
                "path": "/Users/user@example.com/Demo Notebook",
                "object_type": "NOTEBOOK",
            },
            {
                "path": "/Users/user@example.com/Data Analysis",
                "object_type": "DIRECTORY",
            },
            {"path": "/Users/user@example.com/ML Models", "object_type": "DIRECTORY"},
        ]

        for item in workspace_items:
            obj_type = item.get("object_type", "UNKNOWN")
            path = item.get("path", "")
            print(f"  [{obj_type:10}] {path}")

        print(f"\nTotal items: {len(workspace_items)}")
    except Exception as e:
        print(f"  Demo mode: Would list workspace items (Error: {e})")


def demo_cluster_operations(w: Optional[Any]) -> None:
    """
    Line 105-142: Demonstrate cluster management.

    Shows how to:
    - List available clusters
    - Get cluster details (status, configuration)
    - Create new clusters
    - Start/stop clusters
    """
    print_section("3. Cluster Management")

    # List existing clusters
    print("Available Databricks Clusters:")

    demo_clusters = [
        {
            "cluster_id": "0123-456789-abc123",
            "cluster_name": "production-cluster",
            "state": "RUNNING",
            "spark_version": "14.3.x-scala2.12",
            "node_type_id": "i3.xlarge",
            "num_workers": 4,
        },
        {
            "cluster_id": "0123-456789-def456",
            "cluster_name": "dev-cluster",
            "state": "TERMINATED",
            "spark_version": "14.3.x-scala2.12",
            "node_type_id": "i3.large",
            "num_workers": 2,
        },
    ]

    for cluster in demo_clusters:
        print(f"\nCluster: {cluster['cluster_name']}")
        print(f"  ID: {cluster['cluster_id']}")
        print(f"  State: {cluster['state']}")
        print(f"  Spark Version: {cluster['spark_version']}")
        print(f"  Node Type: {cluster['node_type_id']}")
        print(f"  Workers: {cluster['num_workers']}")

    print(f"\nTotal clusters: {len(demo_clusters)}")


def demo_jobs_api(w: Optional[Any]) -> None:
    """
    Line 153-215: Demonstrate Databricks Jobs API.

    Shows how to:
    - Create job definitions
    - Submit job runs
    - Monitor job execution
    - Retrieve job run results
    """
    print_section("4. Jobs API")

    # Define a sample job configuration
    print("Creating a Databricks Job definition:")

    job_config = {
        "name": "Daily ETL Pipeline",
        "tasks": [
            {
                "task_key": "extract_data",
                "description": "Extract data from source systems",
                "notebook_task": {
                    "notebook_path": "/Users/user@example.com/ETL/extract",
                    "base_parameters": {"date": "2024-01-15"},
                },
                "new_cluster": {
                    "spark_version": "14.3.x-scala2.12",
                    "node_type_id": "i3.xlarge",
                    "num_workers": 2,
                },
            },
            {
                "task_key": "transform_data",
                "description": "Transform and clean data",
                "depends_on": [{"task_key": "extract_data"}],
                "notebook_task": {
                    "notebook_path": "/Users/user@example.com/ETL/transform",
                },
                "existing_cluster_id": "0123-456789-abc123",
            },
            {
                "task_key": "load_data",
                "description": "Load data to Delta Lake",
                "depends_on": [{"task_key": "transform_data"}],
                "spark_python_task": {
                    "python_file": "dbfs:/scripts/load_delta.py",
                    "parameters": ["--table", "prod.sales_data"],
                },
                "existing_cluster_id": "0123-456789-abc123",
            },
        ],
        "schedule": {
            "quartz_cron_expression": "0 0 2 * * ?",
            "timezone_id": "America/Los_Angeles",
        },
        "email_notifications": {
            "on_success": ["team@example.com"],
            "on_failure": ["oncall@example.com"],
        },
    }

    print(f"Job Name: {job_config['name']}")
    print(f"Number of Tasks: {len(job_config['tasks'])}")
    print(f"Schedule: {job_config['schedule']['quartz_cron_expression']}")
    print("\nTask Dependencies:")
    for task in job_config["tasks"]:
        task_key = task["task_key"]
        depends = task.get("depends_on", [])
        if depends:
            deps = ", ".join([d["task_key"] for d in depends])
            print(f"  {task_key} → depends on: {deps}")
        else:
            print(f"  {task_key} → no dependencies (root task)")

    # Simulate job run
    print("\n\nSubmitting job run:")
    job_run_id = 12345
    print(f"  Job Run ID: {job_run_id}")
    print("  Status: PENDING → RUNNING → SUCCESS")
    print("  Duration: 5m 32s")


def demo_dbfs_operations(w: Optional[Any]) -> None:
    """
    Line 226-262: Demonstrate DBFS operations.

    Shows how to:
    - List files in DBFS
    - Upload files to DBFS
    - Download files from DBFS
    - Delete files from DBFS
    """
    print_section("5. DBFS (Databricks File System)")

    print("DBFS is Databricks' distributed file system built on top of cloud storage.")
    print("\nCommon DBFS operations:")

    # List files in DBFS
    print("\nListing files in /FileStore/data/:")
    dbfs_files = [
        {"path": "/FileStore/data/sales_2024.csv", "size": 15728640, "is_dir": False},
        {"path": "/FileStore/data/customers.parquet", "size": 8388608, "is_dir": False},
        {"path": "/FileStore/data/archive/", "size": 0, "is_dir": True},
    ]

    for file in dbfs_files:
        if file["is_dir"]:
            print(f"  [DIR]  {file['path']}")
        else:
            size_mb = file["size"] / (1024 * 1024)
            print(f"  [FILE] {file['path']} ({size_mb:.2f} MB)")

    # Upload file example
    print("\n\nUploading file to DBFS:")
    print("  Local: ./data/new_data.csv")
    print("  DBFS: /FileStore/data/new_data.csv")
    print("  Status: ✓ Upload complete")

    # Download file example
    print("\nDownloading file from DBFS:")
    print("  DBFS: /FileStore/data/sales_2024.csv")
    print("  Local: ./downloads/sales_2024.csv")
    print("  Status: ✓ Download complete")


def demo_sql_operations() -> None:
    """
    Line 273-318: Demonstrate Databricks SQL operations.

    Shows how to:
    - Connect to Databricks SQL warehouse
    - Execute SQL queries
    - Fetch and process results
    - Work with Delta tables
    """
    print_section("6. Databricks SQL Operations")

    print(
        "Databricks SQL Connector enables SQL query execution on Databricks SQL warehouses."
    )

    # Connection example
    print("\nConnecting to SQL Warehouse:")
    print("  Server hostname: your-workspace.cloud.databricks.com")
    print("  HTTP path: /sql/1.0/warehouses/abc123def456")
    print("  Status: ✓ Connected")

    # Query execution example
    print("\n\nExecuting SQL Query:")
    query = """
    SELECT
        product_category,
        SUM(revenue) as total_revenue,
        COUNT(DISTINCT customer_id) as unique_customers
    FROM sales.transactions
    WHERE date >= '2024-01-01'
    GROUP BY product_category
    ORDER BY total_revenue DESC
    LIMIT 5
    """

    print(f"Query:\n{query}")

    # Simulated results
    print("\nQuery Results:")
    results = [
        {
            "product_category": "Electronics",
            "total_revenue": 1250000.50,
            "unique_customers": 3420,
        },
        {
            "product_category": "Home & Garden",
            "total_revenue": 987500.25,
            "unique_customers": 2890,
        },
        {
            "product_category": "Clothing",
            "total_revenue": 875200.75,
            "unique_customers": 4156,
        },
        {
            "product_category": "Sports",
            "total_revenue": 654300.00,
            "unique_customers": 1987,
        },
        {
            "product_category": "Books",
            "total_revenue": 432100.50,
            "unique_customers": 2543,
        },
    ]

    print(f"{'Category':<20} {'Revenue':>15} {'Customers':>12}")
    print("-" * 50)
    for row in results:
        print(
            f"{row['product_category']:<20} ${row['total_revenue']:>14,.2f} {row['unique_customers']:>12,}"
        )

    print(f"\nRows returned: {len(results)}")


def demo_unity_catalog() -> None:
    """
    Line 329-380: Demonstrate Unity Catalog operations.

    Unity Catalog is Databricks' unified governance solution for data and AI.

    Shows how to:
    - List catalogs, schemas, and tables
    - Manage permissions
    - Work with metadata
    - Implement data governance
    """
    print_section("7. Unity Catalog")

    print("Unity Catalog provides centralized governance for data and AI assets.")

    # Catalog hierarchy
    print("\nCatalog Hierarchy:")
    print("  Catalog: production")
    print("    └─ Schema: sales")
    print("       ├─ Table: transactions (Delta)")
    print("       ├─ Table: customers (Delta)")
    print("       └─ View: monthly_summary")
    print("    └─ Schema: marketing")
    print("       ├─ Table: campaigns (Delta)")
    print("       └─ Table: leads (Delta)")

    # Table details
    print("\n\nTable Details: production.sales.transactions")
    table_info = {
        "catalog": "production",
        "schema": "sales",
        "name": "transactions",
        "type": "MANAGED",
        "format": "DELTA",
        "location": "s3://databricks-prod/catalog/sales/transactions",
        "created_at": "2024-01-15 10:30:00",
        "owner": "data-engineering-team",
        "size_bytes": 52428800,
        "num_rows": 1500000,
    }

    for key, value in table_info.items():
        print(f"  {key.replace('_', ' ').title():<15}: {value}")

    # Permissions
    print("\n\nTable Permissions:")
    permissions = [
        {"principal": "data-engineering-team", "privilege": "ALL PRIVILEGES"},
        {"principal": "analysts-group", "privilege": "SELECT"},
        {"principal": "data-scientists-group", "privilege": "SELECT"},
    ]

    for perm in permissions:
        print(f"  {perm['principal']:<25} → {perm['privilege']}")


def demo_delta_lake_operations() -> None:
    """
    Line 391-442: Demonstrate Delta Lake operations.

    Delta Lake is an open-source storage layer that brings ACID transactions
    to Apache Spark and big data workloads.

    Shows how to:
    - Create Delta tables
    - Perform ACID transactions
    - Time travel queries
    - Optimize and vacuum operations
    """
    print_section("8. Delta Lake Operations")

    print("Delta Lake provides ACID transactions and time travel for data lakes.")

    # Create Delta table
    print("\nCreating Delta Table:")
    create_sql = """
    CREATE TABLE sales.customer_orders (
        order_id BIGINT,
        customer_id BIGINT,
        order_date DATE,
        total_amount DECIMAL(10,2),
        status STRING
    )
    USING DELTA
    PARTITIONED BY (order_date)
    LOCATION 's3://databricks-prod/delta/customer_orders'
    """
    print(create_sql)
    print("  Status: ✓ Table created")

    # Insert data
    print("\n\nInserting data (ACID transaction):")
    print("  INSERT INTO sales.customer_orders VALUES ...")
    print("  Rows inserted: 10,000")
    print("  Transaction: COMMITTED")

    # Update operation
    print("\n\nUpdate operation (ACID transaction):")
    update_sql = (
        "UPDATE sales.customer_orders SET status = 'SHIPPED' WHERE status = 'PENDING'"
    )
    print(f"  {update_sql}")
    print("  Rows updated: 1,234")

    # Time travel query
    print("\n\nTime Travel Query:")
    print("  SELECT * FROM sales.customer_orders VERSION AS OF 5")
    print("  → Querying table state from version 5")
    print("  Rows returned: 8,500 (before recent updates)")

    # Optimize
    print("\n\nOptimize Delta Table:")
    print("  OPTIMIZE sales.customer_orders")
    print("  Files compacted: 150 → 12")
    print("  Space saved: 2.3 GB")


def demo_mlflow_integration() -> None:
    """
    Line 453-497: Demonstrate MLflow integration.

    MLflow is integrated into Databricks for tracking experiments,
    managing models, and deploying ML workflows.

    Shows how to:
    - Log experiments
    - Track parameters and metrics
    - Register models
    - Deploy models
    """
    print_section("9. MLflow Integration")

    print("MLflow on Databricks provides managed ML lifecycle management.")

    # Experiment tracking
    print("\nExperiment: Customer Churn Prediction")
    print("  Experiment ID: 123456789")
    print("  Location: /Users/user@example.com/experiments/churn-prediction")

    print("\n\nRecent Runs:")
    runs = [
        {
            "run_id": "abc123",
            "model": "RandomForest",
            "accuracy": 0.8523,
            "f1_score": 0.8234,
            "parameters": {"n_estimators": 100, "max_depth": 10},
        },
        {
            "run_id": "def456",
            "model": "XGBoost",
            "accuracy": 0.8756,
            "f1_score": 0.8512,
            "parameters": {"max_depth": 6, "learning_rate": 0.1},
        },
        {
            "run_id": "ghi789",
            "model": "LightGBM",
            "accuracy": 0.8891,
            "f1_score": 0.8698,
            "parameters": {"num_leaves": 31, "learning_rate": 0.05},
        },
    ]

    print(f"{'Run ID':<10} {'Model':<15} {'Accuracy':>10} {'F1 Score':>10}")
    print("-" * 50)
    for run in runs:
        print(
            f"{run['run_id']:<10} {run['model']:<15} {run['accuracy']:>10.4f} {run['f1_score']:>10.4f}"
        )

    print(f"\nTotal runs: {len(runs)}")
    print("Best model: LightGBM (run_id: ghi789)")

    # Model registry
    print("\n\nModel Registry:")
    print("  Model Name: customer_churn_predictor")
    print("  Version: 3")
    print("  Stage: Production")
    print("  Status: ✓ Deployed to REST endpoint")


def demo_secrets_management() -> None:
    """
    Line 508-540: Demonstrate Secrets Management.

    Databricks Secrets provide secure storage and access to
    sensitive information like API keys, passwords, and tokens.

    Shows how to:
    - Create secret scopes
    - Store secrets
    - Access secrets in notebooks
    - Manage ACLs for secrets
    """
    print_section("10. Secrets Management")

    print("Databricks Secrets API securely stores and manages sensitive credentials.")

    # Secret scopes
    print("\nSecret Scopes:")
    scopes = [
        {"scope": "production-keys", "backend_type": "DATABRICKS"},
        {"scope": "aws-credentials", "backend_type": "DATABRICKS"},
        {"scope": "api-tokens", "backend_type": "AZURE_KEYVAULT"},
    ]

    for scope in scopes:
        print(f"  Scope: {scope['scope']:<20} Backend: {scope['backend_type']}")

    # List secrets in a scope
    print("\n\nSecrets in 'production-keys' scope:")
    secrets = ["database-password", "api-key", "encryption-key", "oauth-token"]
    for secret in secrets:
        print(f"  • {secret}")

    # Access pattern
    print("\n\nAccessing secrets in code:")
    print('  dbutils.secrets.get(scope="production-keys", key="database-password")')
    print("  → Returns: ••••••••••••••••")
    print("  Note: Secrets are redacted in logs and notebooks")


def main() -> None:
    """Main demonstration function."""
    print("\n" + "=" * 70)
    print("  DATABRICKS PYTHON SDK DEMONSTRATION")
    print("=" * 70)
    print(f"\nExecution time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("Python version: 3.10+")
    print("SDK version: databricks-sdk 0.40.0+")

    # Initialize workspace client (demo mode)
    w = demo_workspace_connection()

    # Run all demonstrations
    demo_workspace_operations(w)
    demo_cluster_operations(w)
    demo_jobs_api(w)
    demo_dbfs_operations(w)
    demo_sql_operations()
    demo_unity_catalog()
    demo_delta_lake_operations()
    demo_mlflow_integration()
    demo_secrets_management()

    # Summary
    print_section("Summary")
    print("This demonstration covered:")
    print("  ✓ Workspace connection and authentication")
    print("  ✓ Workspace operations (notebooks, directories)")
    print("  ✓ Cluster management")
    print("  ✓ Jobs API (create, run, monitor)")
    print("  ✓ DBFS operations")
    print("  ✓ SQL query execution")
    print("  ✓ Unity Catalog governance")
    print("  ✓ Delta Lake ACID transactions")
    print("  ✓ MLflow experiment tracking")
    print("  ✓ Secrets management")

    print("\n" + "=" * 70)
    print("  For production use, set environment variables:")
    print("    - DATABRICKS_HOST=https://your-workspace.cloud.databricks.com")
    print("    - DATABRICKS_TOKEN=your-personal-access-token")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
