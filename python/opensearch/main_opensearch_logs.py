#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "opensearch-py>=2.4.0",
# ]
# ///

"""
OpenSearch Python Example: Retrieving Logs via Queries

This example demonstrates how to:
1. Connect to OpenSearch (using a local instance or demo)
2. Create an index for storing logs
3. Index sample log entries
4. Query logs using various search methods
5. Retrieve and display results
"""

from datetime import datetime, timedelta
from opensearchpy import OpenSearch


def create_opensearch_client():
    """Create and return an OpenSearch client."""
    # Line 26-30: Configure connection to OpenSearch
    # Note: This uses default local settings. For production, use proper auth.
    client = OpenSearch(
        hosts=[{"host": "localhost", "port": 9200}],
        http_compress=True,
        use_ssl=False,
        verify_certs=False,
        ssl_assert_hostname=False,
        ssl_show_warn=False,
    )
    return client


def create_logs_index(client, index_name="application-logs"):
    """Create an index with mapping optimized for log storage."""
    # Line 42-68: Define index mapping for log documents
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

    # Delete index if it exists (for demo purposes)
    if client.indices.exists(index=index_name):
        client.indices.delete(index=index_name)
        print(f"[Line 70] Deleted existing index: {index_name}")

    # Line 73: Create the index
    response = client.indices.create(index=index_name, body=index_body)
    print(f"[Line 74] Created index: {index_name}")
    return response


def index_sample_logs(client, index_name="application-logs"):
    """Index sample log entries for demonstration."""
    base_time = datetime.now()

    # Line 84-145: Sample log entries with various scenarios
    sample_logs = [
        {
            "timestamp": (base_time - timedelta(minutes=10)).isoformat(),
            "level": "INFO",
            "message": "User login successful",
            "service": "auth-service",
            "host": "server-01",
            "user_id": "user_123",
            "request_id": "req_001",
            "status_code": 200,
            "ip_address": "192.168.1.100",
        },
        {
            "timestamp": (base_time - timedelta(minutes=9)).isoformat(),
            "level": "ERROR",
            "message": "Database connection timeout",
            "service": "api-service",
            "host": "server-02",
            "user_id": "user_456",
            "request_id": "req_002",
            "duration_ms": 5000,
            "status_code": 500,
            "ip_address": "192.168.1.101",
        },
        {
            "timestamp": (base_time - timedelta(minutes=8)).isoformat(),
            "level": "WARN",
            "message": "High memory usage detected",
            "service": "monitoring-service",
            "host": "server-03",
            "request_id": "req_003",
            "ip_address": "192.168.1.102",
        },
        {
            "timestamp": (base_time - timedelta(minutes=7)).isoformat(),
            "level": "INFO",
            "message": "API request processed successfully",
            "service": "api-service",
            "host": "server-02",
            "user_id": "user_789",
            "request_id": "req_004",
            "duration_ms": 120,
            "status_code": 200,
            "ip_address": "192.168.1.103",
        },
        {
            "timestamp": (base_time - timedelta(minutes=5)).isoformat(),
            "level": "ERROR",
            "message": "Failed to process payment: insufficient funds",
            "service": "payment-service",
            "host": "server-04",
            "user_id": "user_123",
            "request_id": "req_005",
            "duration_ms": 2500,
            "status_code": 402,
            "ip_address": "192.168.1.100",
        },
        {
            "timestamp": (base_time - timedelta(minutes=3)).isoformat(),
            "level": "INFO",
            "message": "Cache invalidated for user session",
            "service": "cache-service",
            "host": "server-01",
            "user_id": "user_456",
            "request_id": "req_006",
            "ip_address": "192.168.1.101",
        },
        {
            "timestamp": (base_time - timedelta(minutes=2)).isoformat(),
            "level": "DEBUG",
            "message": "SQL query executed",
            "service": "api-service",
            "host": "server-02",
            "duration_ms": 45,
            "request_id": "req_007",
            "ip_address": "192.168.1.104",
        },
        {
            "timestamp": (base_time - timedelta(minutes=1)).isoformat(),
            "level": "ERROR",
            "message": "Authentication failed: invalid token",
            "service": "auth-service",
            "host": "server-01",
            "user_id": "user_999",
            "request_id": "req_008",
            "status_code": 401,
            "ip_address": "192.168.1.105",
        },
    ]

    # Line 179-182: Bulk index all log entries
    for i, log in enumerate(sample_logs):
        client.index(index=index_name, body=log, id=i + 1, refresh=True)

    print(f"[Line 183] Indexed {len(sample_logs)} log entries")
    return len(sample_logs)


def query_logs_by_level(client, index_name, level):
    """Query logs by severity level."""
    # Line 190-196: Simple match query for log level
    query = {"query": {"match": {"level": level}}}

    print(f"\n[Line 193] === Query 1: Logs with level '{level}' ===")
    response = client.search(index=index_name, body=query)

    print(f"[Line 196] Found {response['hits']['total']['value']} results")
    for hit in response["hits"]["hits"]:
        log = hit["_source"]
        print(
            f"[Line 199]   [{log['timestamp']}] {log['level']}: "
            f"{log['message']} (service: {log.get('service', 'N/A')})"
        )
    return response


def query_logs_by_service_and_time(client, index_name, service, minutes_ago):
    """Query logs for a specific service within a time range."""
    # Line 209-223: Bool query combining service match and time range
    time_threshold = (datetime.now() - timedelta(minutes=minutes_ago)).isoformat()

    query = {
        "query": {
            "bool": {
                "must": [{"match": {"service": service}}],
                "filter": [{"range": {"timestamp": {"gte": time_threshold}}}],
            }
        },
        "sort": [{"timestamp": {"order": "desc"}}],
    }

    print(
        f"\n[Line 224] === Query 2: Logs from '{service}' "
        f"in last {minutes_ago} minutes ==="
    )
    response = client.search(index=index_name, body=query)

    print(f"[Line 229] Found {response['hits']['total']['value']} results")
    for hit in response["hits"]["hits"]:
        log = hit["_source"]
        print(
            f"[Line 232]   [{log['timestamp']}] {log['level']}: "
            f"{log['message']} (host: {log.get('host', 'N/A')})"
        )
    return response


def query_logs_with_aggregations(client, index_name):
    """Query logs with aggregations to get statistics."""
    # Line 241-257: Aggregation query to count logs by level and service
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

    print("\n[Line 259] === Query 3: Log Statistics (Aggregations) ===")
    response = client.search(index=index_name, body=query)

    # Line 263-266: Display log count by level
    print("[Line 263] Log count by level:")
    for bucket in response["aggregations"]["by_level"]["buckets"]:
        print(f"[Line 265]   {bucket['key']}: {bucket['doc_count']}")

    # Line 268-271: Display log count by service
    print("\n[Line 268] Log count by service:")
    for bucket in response["aggregations"]["by_service"]["buckets"]:
        print(f"[Line 270]   {bucket['key']}: {bucket['doc_count']}")

    # Line 273-276: Display average duration
    avg_duration = response["aggregations"]["avg_duration"]["value"]
    if avg_duration:
        print(f"\n[Line 275] Average duration: {avg_duration:.2f} ms")
    else:
        print("\n[Line 277] Average duration: N/A (no duration data)")

    return response


def query_logs_by_user(client, index_name, user_id):
    """Query all logs for a specific user."""
    # Line 285-289: Query logs by user_id
    query = {
        "query": {"match": {"user_id": user_id}},
        "sort": [{"timestamp": {"order": "desc"}}],
    }

    print(f"\n[Line 291] === Query 4: All logs for user '{user_id}' ===")
    response = client.search(index=index_name, body=query)

    print(f"[Line 294] Found {response['hits']['total']['value']} results")
    for hit in response["hits"]["hits"]:
        log = hit["_source"]
        print(
            f"[Line 297]   [{log['timestamp']}] {log['level']}: "
            f"{log['message']} (status: {log.get('status_code', 'N/A')})"
        )
    return response


def query_error_logs_with_high_duration(client, index_name):
    """Query error logs that took longer than a threshold."""
    # Line 306-318: Complex bool query for errors with high duration
    query = {
        "query": {
            "bool": {
                "must": [{"match": {"level": "ERROR"}}],
                "filter": [{"range": {"duration_ms": {"gte": 1000}}}],
            }
        },
        "sort": [{"duration_ms": {"order": "desc"}}],
    }

    print("\n[Line 319] === Query 5: ERROR logs with duration >= 1000ms ===")
    response = client.search(index=index_name, body=query)

    print(f"[Line 322] Found {response['hits']['total']['value']} results")
    for hit in response["hits"]["hits"]:
        log = hit["_source"]
        print(
            f"[Line 325]   [{log['timestamp']}] {log['message']} "
            f"(duration: {log.get('duration_ms', 'N/A')}ms, "
            f"service: {log.get('service', 'N/A')})"
        )
    return response


def main():
    """Main function to demonstrate OpenSearch log querying."""
    print("[Line 335] ===== OpenSearch Python Logs Example =====\n")

    try:
        # Line 338-339: Create client and connect to OpenSearch
        print("[Line 338] Connecting to OpenSearch...")
        client = create_opensearch_client()

        # Line 342: Verify connection
        info = client.info()
        print(f"[Line 343] Connected to OpenSearch {info['version']['number']}\n")

        # Line 346-347: Create index for logs
        index_name = "application-logs"
        create_logs_index(client, index_name)

        # Line 350: Index sample log entries
        print()
        index_sample_logs(client, index_name)

        # Line 354: Execute various log queries
        query_logs_by_level(client, index_name, "ERROR")
        query_logs_by_service_and_time(client, index_name, "api-service", 10)
        query_logs_with_aggregations(client, index_name)
        query_logs_by_user(client, index_name, "user_123")
        query_error_logs_with_high_duration(client, index_name)

        print("\n[Line 361] ===== All queries completed successfully =====")

    except Exception as e:
        print(f"[Line 364] Error: {e}")
        print(
            "\n[Line 365] Note: This example requires OpenSearch running "
            "on localhost:9200"
        )
        print(
            "[Line 367] You can start OpenSearch with Docker:\n"
            "  docker run -p 9200:9200 -p 9600:9600 -e "
            '"discovery.type=single-node" '
            "-e OPENSEARCH_INITIAL_ADMIN_PASSWORD=Admin123! "
            "opensearchproject/opensearch:latest"
        )


if __name__ == "__main__":
    main()
