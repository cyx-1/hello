# Milvus Vector Database Demonstration

This example illustrates **Milvus**, a cloud-native vector database designed for high-performance similarity search at scale.

## Overview

**Milvus** is an open-source vector database built to power AI applications with:
- **High-performance similarity search** on billion-scale datasets
- **Hybrid search** combining vector similarity and scalar filtering
- **Multiple index types** (FLAT, IVF_FLAT, HNSW, SCANN, etc.)
- **Production-ready architecture** with clustering and horizontal scaling
- **Rich ecosystem** including managed cloud service (Zilliz Cloud)

## Key Features Demonstrated

1. **Connection Setup** - Using Milvus Lite (embedded mode)
2. **Schema Design** - Flexible schema with vectors and metadata
3. **Data Insertion** - Batch insertion with 1000 documents
4. **Similarity Search** - Vector search with COSINE metric
5. **Hybrid Search** - Combining vector search with attribute filters
6. **Query Operations** - SQL-like queries on scalar fields
7. **Collection Management** - Statistics and schema inspection
8. **Index Types** - Multiple indexing strategies explained
9. **Cleanup Operations** - Data deletion and management

## Running the Example

```bash
# Navigate to the milvus directory
cd python/milvus

# Run with uv (handles dependencies automatically)
uv run main_milvus.py
```

## Dependencies

This example requires:
- **Python 3.9+**
- **pymilvus >= 2.4.0** - Python SDK for Milvus
- **milvus-lite >= 2.4.0** - Embedded Milvus for local development
- **numpy >= 1.24.0** - For vector operations

Dependencies are managed via inline script metadata (PEP 723).

## Code Walkthrough

### 1. Connection Setup (Lines 58-62)

```python
# Line 58: Using MilvusClient for simplified API (Milvus 2.4+)
# This uses Milvus Lite - an embedded version perfect for demos
client = MilvusClient("./milvus_demo.db")
```

**Output:**
```
[Line 58] Created MilvusClient with local database
  Mode: Milvus Lite (embedded)
  Storage: ./milvus_demo.db

  Note: For production, connect to Milvus server:
    client = MilvusClient(uri='http://localhost:19530')
```

**Key Points:**
- Milvus Lite provides an embedded database perfect for development and testing
- For production, connect to Milvus Standalone or Cluster deployments
- Zilliz Cloud offers fully managed Milvus hosting

---

### 2. Schema Design (Lines 100-145)

```python
# Line 100: Define schema with multiple field types
schema = MilvusClient.create_schema(
    auto_id=False,  # We'll provide our own IDs
    enable_dynamic_field=True,  # Allow additional fields not in schema
)

# Line 107: Add primary key field
schema.add_field(field_name="id", datatype=DataType.INT64, is_primary=True)

# Line 110: Add vector field (768-dimensional embeddings)
schema.add_field(
    field_name="embedding", datatype=DataType.FLOAT_VECTOR, dim=768
)

# Line 116: Add scalar fields for metadata
schema.add_field(field_name="title", datatype=DataType.VARCHAR, max_length=500)
schema.add_field(field_name="category", datatype=DataType.VARCHAR, max_length=100)
schema.add_field(field_name="view_count", datatype=DataType.INT64)
schema.add_field(field_name="rating", datatype=DataType.FLOAT)
```

**Output:**
```
[Line 100-121] Defined schema with multiple field types:
  - id (INT64, primary key)
  - embedding (FLOAT_VECTOR, dim=768)
  - title (VARCHAR, max_length=500)
  - category (VARCHAR, max_length=100)
  - view_count (INT64)
  - rating (FLOAT)
  - enable_dynamic_field=True (allows additional metadata)
```

**Key Points:**
- 768-dimensional vectors are common for sentence-transformers models
- Schema supports rich metadata with various data types
- Dynamic fields allow flexibility for additional metadata

---

### 3. Index Configuration (Lines 134-145)

```python
# Line 134: Add index for vector field
index_params.add_index(
    field_name="embedding",
    index_type="AUTOINDEX",  # Automatically selects best index
    metric_type="COSINE",    # Distance metric: COSINE, L2, or IP
)

# Line 145: Create collection with schema and index
client.create_collection(
    collection_name=collection_name,
    schema=schema,
    index_params=index_params,
)
```

**Output:**
```
[Line 134-138] Configured index parameters:
  - Index type: AUTOINDEX (automatically optimizes)
  - Metric: COSINE similarity
  - Other options: L2 (Euclidean), IP (Inner Product)

[Line 145] Created collection: document_embeddings
  Status: Ready for data insertion
```

**Key Points:**
- AUTOINDEX automatically selects the optimal index type
- COSINE similarity measures directional similarity (0-1 range)
- Other metrics: L2 (Euclidean distance), IP (Inner Product)

---

### 4. Data Insertion (Lines 192-223)

```python
# Line 192: Prepare data for insertion
for i in range(num_docs):
    # Generate random embedding
    embedding = np.random.randn(768).astype(np.float32)
    # Line 199: Normalize for cosine similarity
    embedding = embedding / np.linalg.norm(embedding)

    data.append({
        "id": i,
        "embedding": embedding.tolist(),
        "title": f"Document {i}: Sample Title",
        "category": categories[i % len(categories)],
        "view_count": np.random.randint(0, 10000),
        "rating": round(np.random.uniform(1.0, 5.0), 2),
    })

# Line 218: Insert data into collection
result = client.insert(collection_name=collection_name, data=data)
```

**Output:**
```
[Line 177] Generating 1000 sample document embeddings
  Dimension: 768 (common for sentence-transformers)

[Line 192-211] Prepared 1000 documents with:
  - Categories: ['technology', 'science', 'business', 'entertainment', 'sports']
  - View counts: 0-10,000
  - Ratings: 1.0-5.0

[Line 218] Inserted 1000 documents
  Primary keys: [0, 1, 2, 3, 4]... (showing first 5)

[Line 223] Flushed collection (data persisted to disk)
```

**Key Points:**
- Vector normalization is crucial for COSINE similarity
- Batch insertion is efficient for large datasets
- Flush ensures data is persisted immediately

---

### 5. Vector Similarity Search (Lines 258-267)

```python
# Line 258: Perform similarity search
results = client.search(
    collection_name=collection_name,
    data=[query_embedding],  # Can search multiple queries at once
    limit=5,                 # Return top 5 most similar
    output_fields=["title", "category", "rating", "view_count"],
)
```

**Output:**
```
[Line 258-267] Performed similarity search
  Metric: COSINE similarity
  Query vectors: 1
  Results per query: 5

  Search Results:

  [1] ID: 0
      Distance: 1.0000 (1.0 = identical)
      Title: Document 0: Sample Title
      Category: technology
      Rating: 3.39
      Views: 9130

  [2] ID: 511
      Distance: 0.1397 (1.0 = identical)
      Title: Document 511: Sample Title
      Category: science
      Rating: 3.85
      Views: 7649

  [3] ID: 831
      Distance: 0.1339 (1.0 = identical)
      Title: Document 831: Sample Title
      Category: science
      Rating: 3.38
      Views: 8542
```

**Key Points:**
- Distance of 1.0 means identical vectors (for COSINE metric)
- Lower distances indicate less similarity
- Can search multiple query vectors in a single request

---

### 6. Hybrid Search - Vector + Scalar Filtering (Lines 316-322)

```python
# Line 310: Define filter expression
filter_expr = 'category == "technology" and rating >= 4.0'

# Line 316: Search with filters
results = client.search(
    collection_name=collection_name,
    data=[query_embedding],
    limit=5,
    output_fields=["title", "category", "rating", "view_count"],
    filter=filter_expr,  # Apply scalar filter
)
```

**Output:**
```
[Line 306] Hybrid search: Vector similarity + Attribute filters
  Use case: 'Find similar technology articles with rating >= 4.0'

  Filter expression: category == "technology" and rating >= 4.0

[Line 316-322] Search results (filtered):
  Found 5 results matching criteria

  [1] ID: 190
      Distance: 0.0966
      Category: technology ✓
      Rating: 4.02 ✓ (>= 4.0)
      Views: 3165

  [2] ID: 695
      Distance: 0.0673
      Category: technology ✓
      Rating: 4.40 ✓ (>= 4.0)
      Views: 5285

  [3] ID: 880
      Distance: 0.0653
      Category: technology ✓
      Rating: 4.34 ✓ (>= 4.0)
      Views: 9575
```

**Key Points:**
- **Hybrid search** is a key differentiator of Milvus
- Efficiently combines vector similarity with scalar filtering
- Supports complex boolean expressions (AND, OR, NOT, ranges)
- Ideal for recommendation systems and semantic search with filters

---

### 7. Query Operations (Lines 376-391)

```python
# Line 376: Query by ID range
results = client.query(
    collection_name=collection_name,
    filter="id >= 10 and id < 15",
    output_fields=["id", "title", "category", "rating"],
)

# Line 391: Query by category
results2 = client.query(
    collection_name=collection_name,
    filter='category == "sports"',
    output_fields=["id", "title", "category", "rating"],
    limit=5,
)
```

**Output:**
```
[Line 371] Query vs Search:
  - Search: Find similar vectors (ANN search)
  - Query: Retrieve by scalar fields (like SQL WHERE)

[Line 376] Query: Get documents with ID in [10, 15)
  Filter: id >= 10 and id < 15
  Results: 5 documents

  ID 10: technology (rating: 1.78)
  ID 11: science (rating: 4.88)
  ID 12: business (rating: 3.37)
  ID 13: entertainment (rating: 4.60)
  ID 14: sports (rating: 4.34)

[Line 391] Query: Get sports documents (limit 5)
  Results: 5 documents
  ID 4: rating 4.32
  ID 9: rating 1.17
  ID 14: rating 4.34
```

**Key Points:**
- **Query** retrieves by scalar fields (no vector comparison)
- **Search** uses vector similarity
- Query is like SQL WHERE clause

---

### 8. Index Types (Lines 446+)

**Output:**
```
[Line 446] Available Index Types:

  FLAT
    Description: Brute force search
    Trade-off: 100% accuracy, slow for large datasets
    Best for: Small datasets, highest accuracy needed

  IVF_FLAT
    Description: Inverted file with flat compression
    Trade-off: Fast search, good accuracy (configurable)
    Best for: Large datasets, balanced accuracy/speed

  IVF_SQ8
    Description: IVF with scalar quantization
    Trade-off: Fast + memory efficient, slight accuracy loss
    Best for: Large datasets, memory constrained

  HNSW
    Description: Hierarchical navigable small world
    Trade-off: Very fast search, high accuracy, high memory
    Best for: Low latency requirements, memory available

  SCANN
    Description: Google's ScaNN algorithm
    Trade-off: Excellent speed/accuracy trade-off
    Best for: Production workloads, balanced requirements

  AUTOINDEX
    Description: Automatic index selection
    Trade-off: Milvus chooses optimal index automatically
    Best for: Quick start, let Milvus optimize

  Distance Metrics:
    - L2: Euclidean distance (geometric distance)
    - IP: Inner product (higher = more similar)
    - COSINE: Cosine similarity (direction, not magnitude)
```

**Key Points:**
- Multiple index types for different performance/accuracy trade-offs
- AUTOINDEX is recommended for getting started
- HNSW provides best performance for most use cases
- IVF_SQ8/IVF_PQ for memory-constrained environments

---

### 9. Cleanup (Lines 521-526)

```python
# Line 521: Delete specific entities
client.delete(collection_name=collection_name, filter="id < 5")

# Line 526: Verify deletion
remaining = client.query(
    collection_name=collection_name,
    filter="id < 5",
    output_fields=["id"],
)
```

**Output:**
```
[Line 521] Deleting documents with ID < 5
  Deleted successfully
  Verification: 0 documents remain with ID < 5
```

**Key Points:**
- Supports deletion by filter expression
- Can drop entire collections with `drop_collection()`

---

## Key Differentiators of Milvus

### 1. Cloud-Native Architecture
- **Separation of storage and compute** for elastic scaling
- **Distributed architecture** handles billion-scale datasets
- **Horizontal scaling** by adding nodes

### 2. Hybrid Search Excellence
- **Efficient filtering** on both vector and scalar fields
- **Complex boolean expressions** (AND, OR, NOT, ranges)
- **Production-proven** in recommendation and search systems

### 3. Performance & Scalability
- **Multiple index types** optimized for different scenarios
- **GPU acceleration** support for massive throughput
- **Sub-millisecond latency** for million-scale datasets

### 4. Production-Ready Features
- **High availability** with replication and failover
- **ACID transactions** for data consistency
- **Time Travel** - query historical data snapshots
- **Multi-tenancy** support

### 5. Rich Ecosystem
- **20+ SDKs** (Python, Java, Go, Node.js, etc.)
- **Integrations** with LangChain, LlamaIndex, Haystack
- **Zilliz Cloud** - fully managed Milvus service
- **Active community** with 25k+ GitHub stars

## Version Requirements

This example works with:
- **Milvus 2.4+** (uses AUTOINDEX and simplified MilvusClient API)
- **Python 3.9+**

For earlier Milvus versions, use the legacy `connections.connect()` API.

## Deployment Options

### 1. Milvus Lite (Development)
```python
client = MilvusClient("./milvus_demo.db")
```
- Embedded in Python process
- Perfect for development and testing
- Single-machine deployment

### 2. Milvus Standalone (Single Node)
```python
client = MilvusClient(uri="http://localhost:19530")
```
- Single server deployment
- Suitable for small to medium workloads
- Easy to set up with Docker

### 3. Milvus Cluster (Distributed)
```python
client = MilvusClient(uri="http://milvus-proxy:19530")
```
- Distributed deployment for production
- Horizontal scaling
- High availability and fault tolerance

### 4. Zilliz Cloud (Managed)
```python
client = MilvusClient(
    uri="https://xxx.zillizcloud.com",
    token="your-api-token"
)
```
- Fully managed Milvus service
- Automatic scaling and backups
- Enterprise support

## Real-World Use Cases

1. **Semantic Search** - Find documents by meaning, not just keywords
2. **Recommendation Systems** - "Users who liked X also liked Y"
3. **Image Similarity** - Reverse image search, duplicate detection
4. **Anomaly Detection** - Identify outliers in high-dimensional data
5. **Question Answering** - RAG (Retrieval Augmented Generation) systems
6. **Deduplication** - Find near-duplicate content at scale

## Learn More

- **Official Documentation**: https://milvus.io/docs
- **GitHub Repository**: https://github.com/milvus-io/milvus
- **Zilliz Cloud**: https://zilliz.com
- **Community Slack**: https://milvusio.slack.com
- **Tutorials**: https://milvus.io/bootcamp

## Comparison with Alternatives

| Feature | Milvus | Pinecone | Weaviate | Qdrant |
|---------|--------|----------|----------|--------|
| Open Source | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Self-Hosted | ✅ Yes | ❌ No | ✅ Yes | ✅ Yes |
| Billion+ Scale | ✅ Yes | ✅ Yes | ⚠️ Limited | ⚠️ Limited |
| GPU Support | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| Hybrid Search | ✅ Rich | ⚠️ Basic | ✅ Rich | ✅ Good |
| Multi-Tenancy | ✅ Yes | ✅ Yes | ✅ Yes | ⚠️ Limited |
| Managed Service | ✅ Zilliz | ✅ Native | ✅ Native | ✅ Cloud |

## Summary

Milvus excels at:
- ✅ **Billion-scale vector search** with sub-millisecond latency
- ✅ **Hybrid search** combining vectors and metadata filtering
- ✅ **Production deployments** with enterprise features
- ✅ **Open source** with commercial support options
- ✅ **Rich ecosystem** and integrations

Perfect for building production-grade AI applications that require fast, scalable similarity search.
