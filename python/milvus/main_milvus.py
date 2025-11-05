#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "pymilvus>=2.4.0",
#     "milvus-lite>=2.4.0",
#     "numpy>=1.24.0",
# ]
# ///

"""
Milvus Vector Database Demonstration

This script illustrates the key features of Milvus, a cloud-native vector database:
1. Collection creation with flexible schema design
2. Vector insertion with metadata
3. Similarity search with various distance metrics
4. Hybrid search combining vector and scalar filtering
5. Index types and performance optimization
6. Batch operations and data management

Key differentiators of Milvus:
- Cloud-native architecture with separation of storage and compute
- Multiple index types (FLAT, IVF_FLAT, HNSW, etc.)
- Support for multiple distance metrics (L2, IP, COSINE)
- Hybrid search with attribute filtering
- High performance and scalability
- Open source with enterprise support
"""

import numpy as np
from pymilvus import (
    DataType,
    MilvusClient,
)


# ============================================================================
# Feature 1: Connection and Client Setup
# ============================================================================


def demo_connection():
    """
    Demonstrate connecting to Milvus.

    Milvus supports multiple deployment modes:
    - Milvus Lite: Embedded lightweight version (great for testing)
    - Milvus Standalone: Single-node deployment
    - Milvus Cluster: Distributed deployment for production
    """
    print("\n" + "=" * 70)
    print("DEMO 1: Connection Setup")
    print("=" * 70)

    # Line 58: Using MilvusClient for simplified API (Milvus 2.4+)
    # This uses Milvus Lite - an embedded version perfect for demos
    client = MilvusClient("./milvus_demo.db")

    print("\n[Line 58] Created MilvusClient with local database")
    print("  Mode: Milvus Lite (embedded)")
    print("  Storage: ./milvus_demo.db")
    print("\n  Note: For production, connect to Milvus server:")
    print("    client = MilvusClient(uri='http://localhost:19530')")
    print("    # Or use Zilliz Cloud (managed Milvus):")
    print("    # client = MilvusClient(uri='https://xxx.zillizcloud.com', token='...')")

    return client


# ============================================================================
# Feature 2: Schema Design and Collection Creation
# ============================================================================


def demo_schema_design(client: MilvusClient):
    """
    Demonstrate flexible schema design in Milvus.

    Milvus supports:
    - Auto-generated or custom primary keys
    - Multiple field types (int, float, string, JSON, array)
    - Vector fields with configurable dimensions
    - Dynamic fields for flexible metadata
    """
    print("\n" + "=" * 70)
    print("DEMO 2: Schema Design and Collection Creation")
    print("=" * 70)

    collection_name = "document_embeddings"

    # Line 95: Drop collection if it exists (cleanup)
    if client.has_collection(collection_name):
        client.drop_collection(collection_name)
        print(f"\n[Line 95] Dropped existing collection: {collection_name}")

    # Line 100: Define schema with multiple field types
    # Milvus supports rich schema with various data types
    schema = MilvusClient.create_schema(
        auto_id=False,  # We'll provide our own IDs
        enable_dynamic_field=True,  # Allow additional fields not in schema
    )

    # Line 107: Add primary key field
    schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True)

    # Line 110: Add vector field (768-dimensional embeddings)
    # Common for models like sentence-transformers
    schema.add_field(field_name="embedding", datatype=DataType.FLOAT_VECTOR, dim=768)

    # Line 116: Add scalar fields for metadata
    schema.add_field(field_name="title", datatype=DataType.VARCHAR, max_length=500)
    schema.add_field(field_name="category", datatype=DataType.VARCHAR, max_length=100)
    schema.add_field(field_name="view_count", datatype=DataType.INT64)
    schema.add_field(field_name="rating", datatype=DataType.FLOAT)

    print("\n[Line 100-121] Defined schema with multiple field types:")
    print("  - id (INT64, primary key)")
    print("  - embedding (FLOAT_VECTOR, dim=768)")
    print("  - title (VARCHAR, max_length=500)")
    print("  - category (VARCHAR, max_length=100)")
    print("  - view_count (INT64)")
    print("  - rating (FLOAT)")
    print("  - enable_dynamic_field=True (allows additional metadata)")

    # Line 130: Define index parameters
    # AUTOINDEX is a smart index that automatically chooses optimal settings
    index_params = client.prepare_index_params()

    # Line 134: Add index for vector field
    index_params.add_index(
        field_name="embedding",
        index_type="AUTOINDEX",  # Automatically selects best index
        metric_type="COSINE",  # Distance metric: COSINE, L2, or IP
    )

    print("\n[Line 134-138] Configured index parameters:")
    print("  - Index type: AUTOINDEX (automatically optimizes)")
    print("  - Metric: COSINE similarity")
    print("  - Other options: L2 (Euclidean), IP (Inner Product)")

    # Line 145: Create collection with schema and index
    client.create_collection(
        collection_name=collection_name,
        schema=schema,
        index_params=index_params,
    )

    print(f"\n[Line 145] Created collection: {collection_name}")
    print("  Status: Ready for data insertion")

    return collection_name


# ============================================================================
# Feature 3: Data Insertion
# ============================================================================


def demo_data_insertion(client: MilvusClient, collection_name: str):
    """
    Demonstrate inserting vectors with metadata.

    Milvus supports:
    - Single and batch insertion
    - Automatic ID generation
    - Dynamic fields
    """
    print("\n" + "=" * 70)
    print("DEMO 3: Data Insertion")
    print("=" * 70)

    # Line 177: Generate sample document embeddings
    # In production, use real embeddings from models like:
    # - sentence-transformers
    # - OpenAI embeddings
    # - Cohere embeddings
    np.random.seed(42)
    num_docs = 1000

    print(f"\n[Line 177] Generating {num_docs} sample document embeddings")
    print("  Dimension: 768 (common for sentence-transformers)")
    print("  Note: In production, use real embeddings from:")
    print("    - sentence-transformers (BERT, RoBERTa)")
    print("    - OpenAI (text-embedding-3-small/large)")
    print("    - Cohere (embed-english-v3.0)")

    # Line 192: Prepare data for insertion
    # Normalize vectors for COSINE similarity (important!)
    data = []
    categories = ["technology", "science", "business", "entertainment", "sports"]

    for i in range(num_docs):
        # Generate random embedding
        embedding = np.random.randn(768).astype(np.float32)
        # Line 199: Normalize for cosine similarity
        embedding = embedding / np.linalg.norm(embedding)

        data.append(
            {
                "id": i,
                "embedding": embedding.tolist(),
                "title": f"Document {i}: Sample Title",
                "category": categories[i % len(categories)],
                "view_count": np.random.randint(0, 10000),
                "rating": round(np.random.uniform(1.0, 5.0), 2),
            }
        )

    print(f"\n[Line 192-211] Prepared {len(data)} documents with:")
    print(f"  - Categories: {categories}")
    print("  - View counts: 0-10,000")
    print("  - Ratings: 1.0-5.0")

    # Line 218: Insert data into collection
    result = client.insert(collection_name=collection_name, data=data)

    print(f"\n[Line 218] Inserted {result['insert_count']} documents")
    print(f"  Primary keys: {result['ids'][:5]}... (showing first 5)")

    # Line 223: Flush to ensure data is persisted
    # Important for immediate querying after insertion
    client.flush(collection_name)

    print("\n[Line 223] Flushed collection (data persisted to disk)")

    return data


# ============================================================================
# Feature 4: Vector Similarity Search
# ============================================================================


def demo_similarity_search(client: MilvusClient, collection_name: str, data: list):
    """
    Demonstrate vector similarity search.

    Milvus provides:
    - Fast approximate nearest neighbor (ANN) search
    - Multiple distance metrics
    - Configurable accuracy vs speed tradeoff
    """
    print("\n" + "=" * 70)
    print("DEMO 4: Vector Similarity Search")
    print("=" * 70)

    # Line 251: Create a query vector (simulate searching for similar documents)
    # In practice, this would be an embedding of a user query
    query_embedding = np.array(data[0]["embedding"])  # Use first doc as query

    print("\n[Line 251] Created query vector")
    print("  Source: Using first document as query")
    print("  In practice: Embed user query like 'machine learning tutorials'")

    # Line 258: Perform similarity search
    # Returns top_k most similar vectors
    results = client.search(
        collection_name=collection_name,
        data=[query_embedding],  # Can search multiple queries at once
        limit=5,  # Return top 5 most similar
        output_fields=["title", "category", "rating", "view_count"],
    )

    print("\n[Line 258-267] Performed similarity search")
    print("  Metric: COSINE similarity")
    print("  Query vectors: 1")
    print("  Results per query: 5")
    print("\n  Search Results:")

    for i, hit in enumerate(results[0], 1):
        print(f"\n  [{i}] ID: {hit['id']}")
        print(f"      Distance: {hit['distance']:.4f} (1.0 = identical)")
        print(f"      Title: {hit['entity']['title']}")
        print(f"      Category: {hit['entity']['category']}")
        print(f"      Rating: {hit['entity']['rating']}")
        print(f"      Views: {hit['entity']['view_count']}")


# ============================================================================
# Feature 5: Hybrid Search (Vector + Scalar Filtering)
# ============================================================================


def demo_hybrid_search(client: MilvusClient, collection_name: str, data: list):
    """
    Demonstrate hybrid search combining vector similarity and scalar filters.

    This is a key differentiator of Milvus - efficient filtering on both
    vector and scalar fields simultaneously.
    """
    print("\n" + "=" * 70)
    print("DEMO 5: Hybrid Search (Vector + Scalar Filtering)")
    print("=" * 70)

    query_embedding = np.array(data[100]["embedding"])

    print("\n[Line 306] Hybrid search: Vector similarity + Attribute filters")
    print("  Use case: 'Find similar technology articles with rating >= 4.0'")

    # Line 310: Define filter expression
    # Milvus supports complex boolean expressions
    filter_expr = 'category == "technology" and rating >= 4.0'

    print(f"\n  Filter expression: {filter_expr}")

    # Line 316: Search with filters
    results = client.search(
        collection_name=collection_name,
        data=[query_embedding],
        limit=5,
        output_fields=["title", "category", "rating", "view_count"],
        filter=filter_expr,  # Apply scalar filter
    )

    print("\n[Line 316-322] Search results (filtered):")
    print(f"  Found {len(results[0])} results matching criteria\n")

    for i, hit in enumerate(results[0], 1):
        print(f"  [{i}] ID: {hit['id']}")
        print(f"      Distance: {hit['distance']:.4f}")
        print(f"      Category: {hit['entity']['category']} ✓")
        print(f"      Rating: {hit['entity']['rating']} ✓ (>= 4.0)")
        print(f"      Views: {hit['entity']['view_count']}\n")

    # Line 337: Another example - filter by view count range
    print("\n[Line 337] Another filter: High-engagement content")
    filter_expr2 = "view_count > 5000 and rating >= 3.5"
    print(f"  Filter: {filter_expr2}")

    results2 = client.search(
        collection_name=collection_name,
        data=[query_embedding],
        limit=3,
        output_fields=["title", "category", "rating", "view_count"],
        filter=filter_expr2,
    )

    print(f"\n  Found {len(results2[0])} high-engagement documents:")
    for i, hit in enumerate(results2[0], 1):
        print(
            f"  [{i}] Views: {hit['entity']['view_count']}, Rating: {hit['entity']['rating']}"
        )


# ============================================================================
# Feature 6: Query Operations (Non-Vector Queries)
# ============================================================================


def demo_query_operations(client: MilvusClient, collection_name: str):
    """
    Demonstrate query operations for retrieving data by scalar fields.

    Unlike search (which uses vectors), query retrieves data using
    boolean expressions on scalar fields.
    """
    print("\n" + "=" * 70)
    print("DEMO 6: Query Operations (Scalar Queries)")
    print("=" * 70)

    print("\n[Line 371] Query vs Search:")
    print("  - Search: Find similar vectors (ANN search)")
    print("  - Query: Retrieve by scalar fields (like SQL WHERE)")

    # Line 376: Query by ID range
    results = client.query(
        collection_name=collection_name,
        filter="id >= 10 and id < 15",
        output_fields=["id", "title", "category", "rating"],
    )

    print("\n[Line 376] Query: Get documents with ID in [10, 15)")
    print("  Filter: id >= 10 and id < 15")
    print(f"  Results: {len(results)} documents\n")

    for doc in results:
        print(f"  ID {doc['id']}: {doc['category']} (rating: {doc['rating']})")

    # Line 391: Query by category
    results2 = client.query(
        collection_name=collection_name,
        filter='category == "sports"',
        output_fields=["id", "title", "category", "rating"],
        limit=5,
    )

    print("\n[Line 391] Query: Get sports documents (limit 5)")
    print(f"  Results: {len(results2)} documents")
    for doc in results2:
        print(
            f"  ID {doc['id']}: rating {doc['rating']}, views {doc.get('view_count', 'N/A')}"
        )


# ============================================================================
# Feature 7: Collection Statistics and Management
# ============================================================================


def demo_collection_stats(client: MilvusClient, collection_name: str):
    """Demonstrate collection statistics and management operations."""
    print("\n" + "=" * 70)
    print("DEMO 7: Collection Statistics")
    print("=" * 70)

    # Line 416: Get collection statistics
    stats = client.get_collection_stats(collection_name)

    print("\n[Line 416] Collection statistics:")
    print(f"  Name: {collection_name}")
    print(f"  Row count: {stats['row_count']}")

    # Line 423: Get collection details
    desc = client.describe_collection(collection_name)

    print("\n[Line 423] Collection schema:")
    for field in desc["fields"]:
        print(f"  - {field['name']}: {field['type']}", end="")
        if field.get("params"):
            print(f" (params: {field['params']})", end="")
        if field.get("is_primary"):
            print(" [PRIMARY KEY]", end="")
        print()


# ============================================================================
# Feature 8: Advanced Index Types
# ============================================================================


def demo_index_types():
    """
    Demonstrate different index types available in Milvus.

    Milvus supports various index types for different use cases.
    """
    print("\n" + "=" * 70)
    print("DEMO 8: Index Types and Trade-offs")
    print("=" * 70)

    index_types = [
        (
            "FLAT",
            "Brute force search",
            "100% accuracy, slow for large datasets",
            "Small datasets, highest accuracy needed",
        ),
        (
            "IVF_FLAT",
            "Inverted file with flat compression",
            "Fast search, good accuracy (configurable)",
            "Large datasets, balanced accuracy/speed",
        ),
        (
            "IVF_SQ8",
            "IVF with scalar quantization",
            "Fast + memory efficient, slight accuracy loss",
            "Large datasets, memory constrained",
        ),
        (
            "IVF_PQ",
            "IVF with product quantization",
            "Very memory efficient, more accuracy loss",
            "Huge datasets, aggressive compression",
        ),
        (
            "HNSW",
            "Hierarchical navigable small world",
            "Very fast search, high accuracy, high memory",
            "Low latency requirements, memory available",
        ),
        (
            "SCANN",
            "Google's ScaNN algorithm",
            "Excellent speed/accuracy trade-off",
            "Production workloads, balanced requirements",
        ),
        (
            "AUTOINDEX",
            "Automatic index selection",
            "Milvus chooses optimal index automatically",
            "Quick start, let Milvus optimize",
        ),
    ]

    print("\n[Line 446] Available Index Types:\n")
    for name, description, tradeoff, usecase in index_types:
        print(f"  {name}")
        print(f"    Description: {description}")
        print(f"    Trade-off: {tradeoff}")
        print(f"    Best for: {usecase}\n")

    print("  Distance Metrics:")
    print("    - L2: Euclidean distance (geometric distance)")
    print("    - IP: Inner product (higher = more similar)")
    print("    - COSINE: Cosine similarity (direction, not magnitude)")
    print("\n  Tip: For normalized vectors, COSINE and IP are equivalent")


# ============================================================================
# Feature 9: Cleanup
# ============================================================================


def demo_cleanup(client: MilvusClient, collection_name: str):
    """Demonstrate data deletion and cleanup operations."""
    print("\n" + "=" * 70)
    print("DEMO 9: Cleanup Operations")
    print("=" * 70)

    # Line 521: Delete specific entities
    print("\n[Line 521] Deleting documents with ID < 5")
    client.delete(collection_name=collection_name, filter="id < 5")
    print("  Deleted successfully")

    # Line 526: Verify deletion with query
    remaining = client.query(
        collection_name=collection_name,
        filter="id < 5",
        output_fields=["id"],
    )
    print(f"  Verification: {len(remaining)} documents remain with ID < 5")

    # Note: To drop entire collection, use:
    # client.drop_collection(collection_name)
    # print(f"\n[Line 535] Dropped collection: {collection_name}")


# ============================================================================
# Main Execution
# ============================================================================


def main():
    """Run all demonstrations."""
    print("=" * 70)
    print("MILVUS VECTOR DATABASE DEMONSTRATION")
    print("=" * 70)
    print("\nMilvus is a cloud-native vector database designed for:")
    print("- Large-scale vector similarity search")
    print("- Hybrid search (vectors + scalar filters)")
    print("- High performance and scalability")
    print("- Multiple index types and distance metrics")
    print("- Production-ready with enterprise features")

    # Initialize
    client = demo_connection()

    # Schema and collection
    collection_name = demo_schema_design(client)

    # Data operations
    data = demo_data_insertion(client, collection_name)

    # Search operations
    demo_similarity_search(client, collection_name, data)
    demo_hybrid_search(client, collection_name, data)

    # Query operations
    demo_query_operations(client, collection_name)

    # Collection management
    demo_collection_stats(client, collection_name)

    # Advanced features
    demo_index_types()

    # Cleanup
    demo_cleanup(client, collection_name)

    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("1. Milvus provides high-performance vector similarity search")
    print("2. Hybrid search combines vector and scalar filtering efficiently")
    print("3. Multiple index types for different performance/accuracy needs")
    print("4. Rich schema support with various data types")
    print("5. Production-ready with clustering, backup, and monitoring")
    print("\nDeployment Options:")
    print("  - Milvus Lite: Embedded (great for development)")
    print("  - Milvus Standalone: Single-node (small-medium workloads)")
    print("  - Milvus Cluster: Distributed (large-scale production)")
    print("  - Zilliz Cloud: Fully managed Milvus (https://zilliz.com)")
    print("\nLearn more: https://milvus.io/docs")


if __name__ == "__main__":
    main()
