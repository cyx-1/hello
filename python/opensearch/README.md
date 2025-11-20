# OpenSearch Python: Retrieving Logs via Queries

This example demonstrates how to use Python to interact with OpenSearch for storing and querying application logs. It showcases various query techniques including match queries, range filters, boolean queries, and aggregations.

## Requirements

- **Python**: >=3.10
- **OpenSearch**: 2.x or later
- **Dependencies**: opensearch-py>=2.4.0 (automatically managed via inline script metadata)

## Running the Example

### Prerequisites

Start OpenSearch locally using Docker:

```bash
docker run -p 9200:9200 -p 9600:9600 \
  -e "discovery.type=single-node" \
  -e OPENSEARCH_INITIAL_ADMIN_PASSWORD=Admin123! \
  opensearchproject/opensearch:latest
```

### Execute the Script

```bash
uv run python main_opensearch_logs.py
```

## Source Code Highlights

### 1. Creating OpenSearch Client (Lines 26-30)

```python
client = OpenSearch(
    hosts=[{"host": "localhost", "port": 9200}],
    http_compress=True,
    use_ssl=False,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)
```

This creates a connection to a local OpenSearch instance. For production environments, you should enable SSL and use proper authentication.

### 2. Index Mapping for Logs (Lines 42-68)

```python
index_body = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
    },
    "mappings": {
        "properties": {
            "timestamp": {"type": "date"},
            "level": {"type": "keyword"},
            "message": {"type": "text"},
            "service": {"type": "keyword"},
            "host": {"type": "keyword"},
            "user_id": {"type": "keyword"},
            "request_id": {"type": "keyword"},
            "duration_ms": {"type": "integer"},
            "status_code": {"type": "integer"},
            "ip_address": {"type": "ip"},
        }
    },
}
```

The mapping defines the structure of log documents. Using `keyword` type for fields like `level` and `service` enables efficient filtering and aggregations, while `text` type for `message` enables full-text search.

### 3. Sample Log Entries (Lines 84-145)

The script indexes 8 sample log entries with various scenarios:
- INFO logs for successful operations
- ERROR logs for failures (database timeout, payment failure, auth failure)
- WARN logs for warnings (high memory usage)
- DEBUG logs for debugging information

### 4. Query 1: Match Query by Log Level (Lines 190-196)

```python
query = {"query": {"match": {"level": level}}}
response = client.search(index=index_name, body=query)
```

This simple match query retrieves all logs with a specific severity level (e.g., ERROR).

### 5. Query 2: Bool Query with Time Range (Lines 209-223)

```python
query = {
    "query": {
        "bool": {
            "must": [{"match": {"service": service}}],
            "filter": [{"range": {"timestamp": {"gte": time_threshold}}}],
        }
    },
    "sort": [{"timestamp": {"order": "desc"}}],
}
```

This combines multiple conditions: matching a specific service AND filtering by time range, sorted by most recent first.

### 6. Query 3: Aggregations for Statistics (Lines 241-257)

```python
query = {
    "size": 0,  # We only want aggregations, not individual documents
    "aggs": {
        "by_level": {
            "terms": {"field": "level", "size": 10},
        },
        "by_service": {
            "terms": {"field": "service", "size": 10},
        },
        "avg_duration": {
            "avg": {"field": "duration_ms"},
        },
    },
}
```

Aggregations provide statistical summaries: count of logs by level, count by service, and average duration.

### 7. Query 4: User-Specific Logs (Lines 285-289)

```python
query = {
    "query": {"match": {"user_id": user_id}},
    "sort": [{"timestamp": {"order": "desc"}}],
}
```

Retrieves all logs associated with a specific user, useful for troubleshooting user-specific issues.

### 8. Query 5: Complex Bool Query (Lines 306-318)

```python
query = {
    "query": {
        "bool": {
            "must": [{"match": {"level": "ERROR"}}],
            "filter": [{"range": {"duration_ms": {"gte": 1000}}}],
        }
    },
    "sort": [{"duration_ms": {"order": "desc"}}],
}
```

Finds ERROR logs that took longer than 1000ms, sorted by duration. This helps identify slow-performing errors.

## Program Output

```
[Line 335] ===== OpenSearch Python Logs Example =====

[Line 338] Connecting to OpenSearch...
[Line 343] Connected to OpenSearch 2.11.0

[Line 70] Deleted existing index: application-logs
[Line 74] Created index: application-logs

[Line 183] Indexed 8 log entries

[Line 193] === Query 1: Logs with level 'ERROR' ===
[Line 196] Found 3 results
[Line 199]   [2025-11-20T11:18:00.123456] ERROR: Database connection timeout (service: api-service)
[Line 199]   [2025-11-20T11:22:00.123456] ERROR: Failed to process payment: insufficient funds (service: payment-service)
[Line 199]   [2025-11-20T11:25:00.123456] ERROR: Authentication failed: invalid token (service: auth-service)

[Line 224] === Query 2: Logs from 'api-service' in last 10 minutes ===
[Line 229] Found 3 results
[Line 232]   [2025-11-20T11:25:00.123456] DEBUG: SQL query executed (host: server-02)
[Line 232]   [2025-11-20T11:20:00.123456] INFO: API request processed successfully (host: server-02)
[Line 232]   [2025-11-20T11:18:00.123456] ERROR: Database connection timeout (host: server-02)

[Line 259] === Query 3: Log Statistics (Aggregations) ===
[Line 263] Log count by level:
[Line 265]   INFO: 3
[Line 265]   ERROR: 3
[Line 265]   WARN: 1
[Line 265]   DEBUG: 1

[Line 268] Log count by service:
[Line 270]   api-service: 3
[Line 270]   auth-service: 2
[Line 270]   payment-service: 1
[Line 270]   cache-service: 1
[Line 270]   monitoring-service: 1

[Line 275] Average duration: 1916.25 ms

[Line 291] === Query 4: All logs for user 'user_123' ===
[Line 294] Found 2 results
[Line 297]   [2025-11-20T11:22:00.123456] ERROR: Failed to process payment: insufficient funds (status: 402)
[Line 297]   [2025-11-20T11:17:00.123456] INFO: User login successful (status: 200)

[Line 319] === Query 5: ERROR logs with duration >= 1000ms ===
[Line 322] Found 2 results
[Line 325]   [2025-11-20T11:18:00.123456] Database connection timeout (duration: 5000ms, service: api-service)
[Line 325]   [2025-11-20T11:22:00.123456] Failed to process payment: insufficient funds (duration: 2500ms, service: payment-service)

[Line 361] ===== All queries completed successfully =====
```

## Output Annotation

### Connection and Setup (Lines 335-343)
The program starts by connecting to OpenSearch and displaying the version number. This confirms the connection is successful.

### Index Creation (Lines 70-74)
The existing index is deleted (if present) and recreated with the proper mapping schema for log storage.

### Data Ingestion (Line 183)
8 sample log entries are indexed, simulating real application logs with timestamps spanning 10 minutes.

### Query 1 Results (Lines 193-199)
**Demonstrates**: Simple match query filtering by log level
- Retrieves only ERROR-level logs
- Shows 3 error events: database timeout, payment failure, and authentication failure
- Each result includes timestamp, level, message, and service name

### Query 2 Results (Lines 224-232)
**Demonstrates**: Bool query with service match + time range filter
- Filters logs from 'api-service' within the last 10 minutes
- Results sorted by timestamp (most recent first)
- Shows 3 logs: DEBUG query execution, INFO successful API request, and ERROR database timeout

### Query 3 Results (Lines 259-277)
**Demonstrates**: Aggregations for statistical analysis
- **By Level**: Shows distribution of log severity (3 INFO, 3 ERROR, 1 WARN, 1 DEBUG)
- **By Service**: Shows which services generate most logs (api-service: 3, auth-service: 2, etc.)
- **Average Duration**: Calculates mean response time (1916.25ms) across logs with duration data
- Note: `size: 0` means no individual documents returned, only aggregation results

### Query 4 Results (Lines 291-297)
**Demonstrates**: User activity tracking
- Retrieves all logs for user 'user_123'
- Useful for user-specific troubleshooting
- Shows 2 events: a failed payment and a successful login

### Query 5 Results (Lines 319-325)
**Demonstrates**: Complex filtering for performance analysis
- Combines two conditions: ERROR level AND duration >= 1000ms
- Identifies slow errors that need investigation
- Sorted by duration (slowest first)
- Shows database timeout (5000ms) and payment failure (2500ms)

## Key Concepts Illustrated

1. **Match Queries**: Simple text/keyword matching for fields
2. **Range Filters**: Time-based or numeric range filtering
3. **Bool Queries**: Combining multiple conditions with `must`, `should`, `filter`
4. **Sorting**: Ordering results by timestamp or other fields
5. **Aggregations**: Statistical analysis (terms, avg) without retrieving individual documents
6. **Index Mapping**: Proper field types for efficient querying
7. **Bulk Operations**: Indexing multiple documents efficiently

## Use Cases

This example demonstrates patterns for:
- **Error Tracking**: Finding all ERROR or WARN logs
- **Service Monitoring**: Tracking logs per microservice
- **User Activity**: Audit trails for specific users
- **Performance Analysis**: Identifying slow operations
- **Time-Range Queries**: Recent logs or specific time windows
- **Statistical Analysis**: Log volume trends and averages

## Production Considerations

For production use, consider:
1. **Authentication**: Enable security plugin and use credentials
2. **SSL/TLS**: Enable encrypted communication
3. **Index Lifecycle**: Implement ILM policies for log rotation
4. **Bulk Indexing**: Use bulk API for high-throughput ingestion
5. **Index Templates**: Apply consistent mappings across time-based indices
6. **Replica Shards**: Configure replicas for high availability
7. **Data Streams**: Use data streams for time-series log data
