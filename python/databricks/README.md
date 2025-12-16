# Databricks Python SDK Demonstration

This project demonstrates comprehensive usage of the Databricks Python SDK for managing and interacting with Databricks workspaces, clusters, jobs, and data operations.

## Requirements

- **Python Version**: Python 3.10 or higher
- **Key Dependencies**:
  - `databricks-sdk>=0.40.0` - Official Databricks SDK for Python
  - `databricks-sql-connector>=3.5.0` - SQL connector for Databricks SQL warehouses
  - `pandas>=2.2.0` - Data manipulation library
  - `delta-spark>=3.2.0` - Delta Lake integration

## Running the Demo

```bash
uv run python main_databricks.py
```

The script uses inline script metadata (PEP 723) to automatically manage dependencies - no separate `pyproject.toml` or `requirements.txt` needed.

## Features Demonstrated

This demonstration covers the following Databricks capabilities:

1. **Workspace Connection** - Authentication and workspace client initialization
2. **Workspace Operations** - Managing notebooks, directories, and workspace objects
3. **Cluster Management** - Listing, creating, and managing Databricks clusters
4. **Jobs API** - Creating multi-task job workflows with dependencies
5. **DBFS Operations** - Working with Databricks File System
6. **SQL Operations** - Executing queries via Databricks SQL warehouses
7. **Unity Catalog** - Data governance and metadata management
8. **Delta Lake** - ACID transactions, time travel, and optimization
9. **MLflow Integration** - Experiment tracking and model registry
10. **Secrets Management** - Secure credential storage and access

## Source Code and Output Analysis

### 1. Workspace Connection (Lines 52-84)

**Source Code:**
```python
52: def demo_workspace_connection() -> Optional[Any]:
53:     """
54:     Line 49-56: Demonstrate Databricks workspace connection.
55:
56:     Creates a WorkspaceClient instance which is the main entry point
57:     for interacting with Databricks APIs.
58:     """
59:     print_section("1. Workspace Connection")
60:
61:     if not DATABRICKS_SDK_AVAILABLE:
62:         print("Running in DEMO mode (Databricks SDK not available)")
63:         print("In production, you would initialize WorkspaceClient:")
64:         print('  w = WorkspaceClient(')
65:         print('      host="https://your-workspace.cloud.databricks.com",')
66:         print('      token="your-token-here"')
67:         print('  )')
```

**Output:**
```
======================================================================
  1. Workspace Connection
======================================================================

Running in DEMO mode (Databricks SDK not available)
In production, you would initialize WorkspaceClient:
  w = WorkspaceClient(
      host="https://your-workspace.cloud.databricks.com",
      token="your-token-here"
  )

✓ Connection pattern demonstrated
  Host: https://your-workspace.cloud.databricks.com
  Authentication: Token-based
```

**Analysis:** Lines 64-67 show the standard WorkspaceClient initialization pattern. In production, credentials would come from environment variables (`DATABRICKS_HOST` and `DATABRICKS_TOKEN`).

---

### 2. Workspace Operations (Lines 87-115)

**Source Code:**
```python
 87: def demo_workspace_operations(w: Optional[Any]) -> None:
 95:     print_section("2. Workspace Operations")
 96:
 97:     # List workspace root directory
 98:     print("Listing workspace objects in /Users:")
 99:     try:
100:         # This would list actual workspace items in a real connection
101:         workspace_items = [
102:             {"path": "/Users/user@example.com/Demo Notebook", "object_type": "NOTEBOOK"},
103:             {"path": "/Users/user@example.com/Data Analysis", "object_type": "DIRECTORY"},
104:             {"path": "/Users/user@example.com/ML Models", "object_type": "DIRECTORY"},
105:         ]
106:
107:         for item in workspace_items:
108:             obj_type = item.get("object_type", "UNKNOWN")
109:             path = item.get("path", "")
110:             print(f"  [{obj_type:10}] {path}")
```

**Output:**
```
======================================================================
  2. Workspace Operations
======================================================================

Listing workspace objects in /Users:
  [NOTEBOOK  ] /Users/user@example.com/Demo Notebook
  [DIRECTORY ] /Users/user@example.com/Data Analysis
  [DIRECTORY ] /Users/user@example.com/ML Models

Total items: 3
```

**Analysis:** Lines 107-110 iterate through workspace items and display their type (NOTEBOOK or DIRECTORY) and path. The `workspace.list()` API would be used in production to retrieve actual workspace objects.

---

### 3. Cluster Management (Lines 118-160)

**Source Code:**
```python
118: def demo_cluster_operations(w: Optional[Any]) -> None:
129:     print("Available Databricks Clusters:")
130:
131:     demo_clusters = [
132:         {
133:             "cluster_id": "0123-456789-abc123",
134:             "cluster_name": "production-cluster",
135:             "state": "RUNNING",
136:             "spark_version": "14.3.x-scala2.12",
137:             "node_type_id": "i3.xlarge",
138:             "num_workers": 4,
139:         },
140:         {
141:             "cluster_id": "0123-456789-def456",
142:             "cluster_name": "dev-cluster",
143:             "state": "TERMINATED",
144:             "spark_version": "14.3.x-scala2.12",
145:             "node_type_id": "i3.large",
146:             "num_workers": 2,
147:         },
148:     ]
149:
150:     for cluster in demo_clusters:
151:         print(f"\nCluster: {cluster['cluster_name']}")
152:         print(f"  ID: {cluster['cluster_id']}")
153:         print(f"  State: {cluster['state']}")
154:         print(f"  Spark Version: {cluster['spark_version']}")
155:         print(f"  Node Type: {cluster['node_type_id']}")
156:         print(f"  Workers: {cluster['num_workers']}")
```

**Output:**
```
======================================================================
  3. Cluster Management
======================================================================

Available Databricks Clusters:

Cluster: production-cluster
  ID: 0123-456789-abc123
  State: RUNNING
  Spark Version: 14.3.x-scala2.12
  Node Type: i3.xlarge
  Workers: 4

Cluster: dev-cluster
  ID: 0123-456789-def456
  State: TERMINATED
  Spark Version: 14.3.x-scala2.12
  Node Type: i3.large
  Workers: 2

Total clusters: 2
```

**Analysis:** Lines 131-148 define cluster configurations showing key attributes like cluster ID, state (RUNNING/TERMINATED), Spark version, node type, and worker count. These would be retrieved via `w.clusters.list()` in production.

---

### 4. Jobs API - Multi-Task Workflows (Lines 163-242)

**Source Code:**
```python
163: def demo_jobs_api(w: Optional[Any]) -> None:
174:     print("Creating a Databricks Job definition:")
175:
176:     job_config = {
177:         "name": "Daily ETL Pipeline",
178:         "tasks": [
179:             {
180:                 "task_key": "extract_data",
181:                 "description": "Extract data from source systems",
182:                 "notebook_task": {
183:                     "notebook_path": "/Users/user@example.com/ETL/extract",
184:                     "base_parameters": {"date": "2024-01-15"},
185:                 },
186:                 "new_cluster": {
187:                     "spark_version": "14.3.x-scala2.12",
188:                     "node_type_id": "i3.xlarge",
189:                     "num_workers": 2,
190:                 },
191:             },
192:             {
193:                 "task_key": "transform_data",
194:                 "description": "Transform and clean data",
195:                 "depends_on": [{"task_key": "extract_data"}],
196:                 "notebook_task": {
197:                     "notebook_path": "/Users/user@example.com/ETL/transform",
198:                 },
199:                 "existing_cluster_id": "0123-456789-abc123",
200:             },
201:             {
202:                 "task_key": "load_data",
203:                 "description": "Load data to Delta Lake",
204:                 "depends_on": [{"task_key": "transform_data"}],
205:                 "spark_python_task": {
206:                     "python_file": "dbfs:/scripts/load_delta.py",
207:                     "parameters": ["--table", "prod.sales_data"],
208:                 },
209:                 "existing_cluster_id": "0123-456789-abc123",
210:             },
211:         ],
212:         "schedule": {
213:             "quartz_cron_expression": "0 0 2 * * ?",
214:             "timezone_id": "America/Los_Angeles",
215:         },
216:         "email_notifications": {
217:             "on_success": ["team@example.com"],
218:             "on_failure": ["oncall@example.com"],
219:         },
220:     }
222:     print(f"Job Name: {job_config['name']}")
223:     print(f"Number of Tasks: {len(job_config['tasks'])}")
224:     print(f"Schedule: {job_config['schedule']['quartz_cron_expression']}")
225:     print("\nTask Dependencies:")
226:     for task in job_config["tasks"]:
227:         task_key = task["task_key"]
228:         depends = task.get("depends_on", [])
229:         if depends:
230:             deps = ", ".join([d["task_key"] for d in depends])
231:             print(f"  {task_key} → depends on: {deps}")
232:         else:
233:             print(f"  {task_key} → no dependencies (root task)")
```

**Output:**
```
======================================================================
  4. Jobs API
======================================================================

Creating a Databricks Job definition:
Job Name: Daily ETL Pipeline
Number of Tasks: 3
Schedule: 0 0 2 * * ?

Task Dependencies:
  extract_data → no dependencies (root task)
  transform_data → depends on: extract_data
  load_data → depends on: transform_data


Submitting job run:
  Job Run ID: 12345
  Status: PENDING → RUNNING → SUCCESS
  Duration: 5m 32s
```

**Analysis:**
- **Lines 176-220**: Define a comprehensive multi-task job with three dependent tasks (extract → transform → load)
- **Line 195**: Shows `depends_on` creating task dependencies
- **Line 213**: Cron expression "0 0 2 * * ?" schedules the job daily at 2 AM
- **Lines 216-219**: Configure email notifications for success/failure
- **Lines 226-233**: Demonstrate how task dependencies form a directed acyclic graph (DAG)

---

### 5. DBFS Operations (Lines 245-283)

**Source Code:**
```python
245: def demo_dbfs_operations(w: Optional[Any]) -> None:
256:     print("DBFS is Databricks' distributed file system built on top of cloud storage.")
257:     print("\nCommon DBFS operations:")
258:
259:     # List files in DBFS
260:     print("\nListing files in /FileStore/data/:")
261:     dbfs_files = [
262:         {"path": "/FileStore/data/sales_2024.csv", "size": 15728640, "is_dir": False},
263:         {"path": "/FileStore/data/customers.parquet", "size": 8388608, "is_dir": False},
264:         {"path": "/FileStore/data/archive/", "size": 0, "is_dir": True},
265:     ]
266:
267:     for file in dbfs_files:
268:         if file["is_dir"]:
269:             print(f"  [DIR]  {file['path']}")
270:         else:
271:             size_mb = file["size"] / (1024 * 1024)
272:             print(f"  [FILE] {file['path']} ({size_mb:.2f} MB)")
```

**Output:**
```
======================================================================
  5. DBFS (Databricks File System)
======================================================================

DBFS is Databricks' distributed file system built on top of cloud storage.

Common DBFS operations:

Listing files in /FileStore/data/:
  [FILE] /FileStore/data/sales_2024.csv (15.00 MB)
  [FILE] /FileStore/data/customers.parquet (8.00 MB)
  [DIR]  /FileStore/data/archive/


Uploading file to DBFS:
  Local: ./data/new_data.csv
  DBFS: /FileStore/data/new_data.csv
  Status: ✓ Upload complete

Downloading file from DBFS:
  DBFS: /FileStore/data/sales_2024.csv
  Local: ./downloads/sales_2024.csv
  Status: ✓ Download complete
```

**Analysis:** Lines 267-272 show file listing with size calculation. DBFS paths typically start with `/FileStore/`, `/user/`, or `/databricks/`. Line 271 converts bytes to megabytes for readable output.

---

### 6. SQL Operations (Lines 286-341)

**Source Code:**
```python
295:     # Query execution example
296:     print("\n\nExecuting SQL Query:")
297:     query = """
298:     SELECT
299:         product_category,
300:         SUM(revenue) as total_revenue,
301:         COUNT(DISTINCT customer_id) as unique_customers
302:     FROM sales.transactions
303:     WHERE date >= '2024-01-01'
304:     GROUP BY product_category
305:     ORDER BY total_revenue DESC
306:     LIMIT 5
307:     """
308:
309:     print(f"Query:\n{query}")
310:
311:     # Simulated results
312:     print("\nQuery Results:")
313:     results = [
314:         {"product_category": "Electronics", "total_revenue": 1250000.50, "unique_customers": 3420},
315:         {"product_category": "Home & Garden", "total_revenue": 987500.25, "unique_customers": 2890},
316:         {"product_category": "Clothing", "total_revenue": 875200.75, "unique_customers": 4156},
317:         {"product_category": "Sports", "total_revenue": 654300.00, "unique_customers": 1987},
318:         {"product_category": "Books", "total_revenue": 432100.50, "unique_customers": 2543},
319:     ]
320:
321:     print(f"{'Category':<20} {'Revenue':>15} {'Customers':>12}")
322:     print("-" * 50)
323:     for row in results:
324:         print(f"{row['product_category']:<20} ${row['total_revenue']:>14,.2f} {row['unique_customers']:>12,}")
```

**Output:**
```
======================================================================
  6. Databricks SQL Operations
======================================================================

Databricks SQL Connector enables SQL query execution on Databricks SQL warehouses.

Connecting to SQL Warehouse:
  Server hostname: your-workspace.cloud.databricks.com
  HTTP path: /sql/1.0/warehouses/abc123def456
  Status: ✓ Connected


Executing SQL Query:
Query:

    SELECT
        product_category,
        SUM(revenue) as total_revenue,
        COUNT(DISTINCT customer_id) as unique_customers
    FROM sales.transactions
    WHERE date >= '2024-01-01'
    GROUP BY product_category
    ORDER BY total_revenue DESC
    LIMIT 5


Query Results:
Category                     Revenue    Customers
--------------------------------------------------
Electronics          $  1,250,000.50        3,420
Home & Garden        $    987,500.25        2,890
Clothing             $    875,200.75        4,156
Sports               $    654,300.00        1,987
Books                $    432,100.50        2,543

Rows returned: 5
```

**Analysis:** Lines 297-307 demonstrate a typical analytical SQL query using aggregations, filtering, and grouping. Lines 321-324 format results into a readable table with proper alignment and thousand separators.

---

### 7. Unity Catalog (Lines 344-403)

**Source Code:**
```python
356:     # Catalog hierarchy
357:     print("\nCatalog Hierarchy:")
358:     print("  Catalog: production")
359:     print("    └─ Schema: sales")
360:     print("       ├─ Table: transactions (Delta)")
361:     print("       ├─ Table: customers (Delta)")
362:     print("       └─ View: monthly_summary")
363:     print("    └─ Schema: marketing")
364:     print("       ├─ Table: campaigns (Delta)")
365:     print("       └─ Table: leads (Delta)")
366:
367:     # Table details
368:     print("\n\nTable Details: production.sales.transactions")
369:     table_info = {
370:         "catalog": "production",
371:         "schema": "sales",
372:         "name": "transactions",
373:         "type": "MANAGED",
374:         "format": "DELTA",
375:         "location": "s3://databricks-prod/catalog/sales/transactions",
376:         "created_at": "2024-01-15 10:30:00",
377:         "owner": "data-engineering-team",
378:         "size_bytes": 52428800,
379:         "num_rows": 1500000,
380:     }
387:     permissions = [
388:         {"principal": "data-engineering-team", "privilege": "ALL PRIVILEGES"},
389:         {"principal": "analysts-group", "privilege": "SELECT"},
390:         {"principal": "data-scientists-group", "privilege": "SELECT"},
391:     ]
```

**Output:**
```
======================================================================
  7. Unity Catalog
======================================================================

Unity Catalog provides centralized governance for data and AI assets.

Catalog Hierarchy:
  Catalog: production
    └─ Schema: sales
       ├─ Table: transactions (Delta)
       ├─ Table: customers (Delta)
       └─ View: monthly_summary
    └─ Schema: marketing
       ├─ Table: campaigns (Delta)
       └─ Table: leads (Delta)


Table Details: production.sales.transactions
  Catalog        : production
  Schema         : sales
  Name           : transactions
  Type           : MANAGED
  Format         : DELTA
  Location       : s3://databricks-prod/catalog/sales/transactions
  Created At     : 2024-01-15 10:30:00
  Owner          : data-engineering-team
  Size Bytes     : 52428800
  Num Rows       : 1500000


Table Permissions:
  data-engineering-team     → ALL PRIVILEGES
  analysts-group            → SELECT
  data-scientists-group     → SELECT
```

**Analysis:**
- **Lines 357-365**: Unity Catalog uses three-level namespace: `catalog.schema.table`
- **Lines 369-380**: Table metadata includes ownership, format (Delta), and storage location
- **Lines 387-391**: Fine-grained permissions allow different access levels per principal/group

---

### 8. Delta Lake Operations (Lines 406-465)

**Source Code:**
```python
415:     # Create Delta table
416:     print("\nCreating Delta Table:")
417:     create_sql = """
418:     CREATE TABLE sales.customer_orders (
419:         order_id BIGINT,
420:         customer_id BIGINT,
421:         order_date DATE,
422:         total_amount DECIMAL(10,2),
423:         status STRING
424:     )
425:     USING DELTA
426:     PARTITIONED BY (order_date)
427:     LOCATION 's3://databricks-prod/delta/customer_orders'
428:     """
429:     print(create_sql)
430:     print("  Status: ✓ Table created")
431:
432:     # Insert data
433:     print("\n\nInserting data (ACID transaction):")
434:     print("  INSERT INTO sales.customer_orders VALUES ...")
435:     print("  Rows inserted: 10,000")
436:     print("  Transaction: COMMITTED")
437:
438:     # Update operation
439:     print("\n\nUpdate operation (ACID transaction):")
440:     update_sql = "UPDATE sales.customer_orders SET status = 'SHIPPED' WHERE status = 'PENDING'"
441:     print(f"  {update_sql}")
442:     print("  Rows updated: 1,234")
443:
444:     # Time travel query
445:     print("\n\nTime Travel Query:")
446:     print("  SELECT * FROM sales.customer_orders VERSION AS OF 5")
447:     print("  → Querying table state from version 5")
448:     print("  Rows returned: 8,500 (before recent updates)")
449:
450:     # Optimize
451:     print("\n\nOptimize Delta Table:")
452:     print("  OPTIMIZE sales.customer_orders")
453:     print("  Files compacted: 150 → 12")
454:     print("  Space saved: 2.3 GB")
```

**Output:**
```
======================================================================
  8. Delta Lake Operations
======================================================================

Delta Lake provides ACID transactions and time travel for data lakes.

Creating Delta Table:

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

  Status: ✓ Table created


Inserting data (ACID transaction):
  INSERT INTO sales.customer_orders VALUES ...
  Rows inserted: 10,000
  Transaction: COMMITTED


Update operation (ACID transaction):
  UPDATE sales.customer_orders SET status = 'SHIPPED' WHERE status = 'PENDING'
  Rows updated: 1,234


Time Travel Query:
  SELECT * FROM sales.customer_orders VERSION AS OF 5
  → Querying table state from version 5
  Rows returned: 8,500 (before recent updates)


Optimize Delta Table:
  OPTIMIZE sales.customer_orders
  Files compacted: 150 → 12
  Space saved: 2.3 GB
```

**Analysis:**
- **Line 425**: `USING DELTA` specifies Delta Lake format
- **Line 426**: Partitioning by date improves query performance
- **Lines 433-436**: Delta Lake provides ACID guarantees for inserts/updates
- **Lines 445-448**: Time travel allows querying historical versions
- **Lines 451-454**: OPTIMIZE compacts small files for better performance

---

### 9. MLflow Integration (Lines 468-520)

**Source Code:**
```python
477:     print("\nExperiment: Customer Churn Prediction")
478:     print("  Experiment ID: 123456789")
479:     print("  Location: /Users/user@example.com/experiments/churn-prediction")
480:
481:     print("\n\nRecent Runs:")
482:     runs = [
483:         {
484:             "run_id": "abc123",
485:             "model": "RandomForest",
486:             "accuracy": 0.8523,
487:             "f1_score": 0.8234,
488:             "parameters": {"n_estimators": 100, "max_depth": 10},
489:         },
490:         {
491:             "run_id": "def456",
492:             "model": "XGBoost",
493:             "accuracy": 0.8756,
494:             "f1_score": 0.8512,
495:             "parameters": {"max_depth": 6, "learning_rate": 0.1},
496:         },
497:         {
498:             "run_id": "ghi789",
499:             "model": "LightGBM",
500:             "accuracy": 0.8891,
501:             "f1_score": 0.8698,
502:             "parameters": {"num_leaves": 31, "learning_rate": 0.05},
503:         },
504:     ]
505:
506:     print(f"{'Run ID':<10} {'Model':<15} {'Accuracy':>10} {'F1 Score':>10}")
507:     print("-" * 50)
508:     for run in runs:
509:         print(f"{run['run_id']:<10} {run['model']:<15} {run['accuracy']:>10.4f} {run['f1_score']:>10.4f}")
```

**Output:**
```
======================================================================
  9. MLflow Integration
======================================================================

MLflow on Databricks provides managed ML lifecycle management.

Experiment: Customer Churn Prediction
  Experiment ID: 123456789
  Location: /Users/user@example.com/experiments/churn-prediction


Recent Runs:
Run ID     Model             Accuracy   F1 Score
--------------------------------------------------
abc123     RandomForest        0.8523     0.8234
def456     XGBoost             0.8756     0.8512
ghi789     LightGBM            0.8891     0.8698

Total runs: 3
Best model: LightGBM (run_id: ghi789)


Model Registry:
  Model Name: customer_churn_predictor
  Version: 3
  Stage: Production
  Status: ✓ Deployed to REST endpoint
```

**Analysis:**
- **Lines 482-504**: MLflow tracks experiments with metrics (accuracy, F1), parameters, and model types
- **Lines 506-509**: Formatted comparison of different model runs
- The LightGBM model (line 498-502) shows the best performance (accuracy: 0.8891)

---

### 10. Secrets Management (Lines 523-567)

**Source Code:**
```python
535:     print("\nSecret Scopes:")
536:     scopes = [
537:         {"scope": "production-keys", "backend_type": "DATABRICKS"},
538:         {"scope": "aws-credentials", "backend_type": "DATABRICKS"},
539:         {"scope": "api-tokens", "backend_type": "AZURE_KEYVAULT"},
540:     ]
541:
542:     for scope in scopes:
543:         print(f"  Scope: {scope['scope']:<20} Backend: {scope['backend_type']}")
544:
545:     # List secrets in a scope
546:     print("\n\nSecrets in 'production-keys' scope:")
547:     secrets = ["database-password", "api-key", "encryption-key", "oauth-token"]
548:     for secret in secrets:
549:         print(f"  • {secret}")
550:
551:     # Access pattern
552:     print("\n\nAccessing secrets in code:")
553:     print('  dbutils.secrets.get(scope="production-keys", key="database-password")')
554:     print("  → Returns: ••••••••••••••••")
555:     print("  Note: Secrets are redacted in logs and notebooks")
```

**Output:**
```
======================================================================
  10. Secrets Management
======================================================================

Databricks Secrets API securely stores and manages sensitive credentials.

Secret Scopes:
  Scope: production-keys      Backend: DATABRICKS
  Scope: aws-credentials      Backend: DATABRICKS
  Scope: api-tokens           Backend: AZURE_KEYVAULT


Secrets in 'production-keys' scope:
  • database-password
  • api-key
  • encryption-key
  • oauth-token


Accessing secrets in code:
  dbutils.secrets.get(scope="production-keys", key="database-password")
  → Returns: ••••••••••••••••
  Note: Secrets are redacted in logs and notebooks
```

**Analysis:**
- **Lines 536-540**: Secret scopes can use either Databricks-managed or external backends (Azure Key Vault)
- **Line 553**: `dbutils.secrets.get()` is the standard way to retrieve secrets in notebooks
- **Line 555**: Databricks automatically redacts secret values in logs for security

---

## Production Usage

For production environments, set these environment variables:

```bash
export DATABRICKS_HOST="https://your-workspace.cloud.databricks.com"
export DATABRICKS_TOKEN="your-personal-access-token"
```

Or use a Databricks configuration file at `~/.databrickscfg`:

```ini
[DEFAULT]
host = https://your-workspace.cloud.databricks.com
token = your-personal-access-token
```

## Key Takeaways

1. **WorkspaceClient** is the main entry point for all Databricks SDK operations (line 52)
2. **Jobs API** supports complex multi-task workflows with dependencies (lines 176-220)
3. **Unity Catalog** provides three-level namespace and fine-grained permissions (lines 357-391)
4. **Delta Lake** enables ACID transactions and time travel on data lakes (lines 417-454)
5. **MLflow** integrates seamlessly for experiment tracking and model management (lines 482-504)
6. **Secrets** are automatically redacted in logs and should be accessed via `dbutils.secrets.get()` (line 553)

## Additional Resources

- [Databricks SDK for Python Documentation](https://docs.databricks.com/dev-tools/python-sql-connector.html)
- [Unity Catalog Documentation](https://docs.databricks.com/data-governance/unity-catalog/index.html)
- [Delta Lake Documentation](https://docs.databricks.com/delta/index.html)
- [MLflow on Databricks](https://docs.databricks.com/mlflow/index.html)
- [Databricks Jobs Documentation](https://docs.databricks.com/workflows/jobs/jobs.html)
