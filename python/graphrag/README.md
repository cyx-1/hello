# Microsoft GraphRAG Python Demo

This demonstration showcases **Microsoft GraphRAG** (Graph-based Retrieval Augmented Generation), a sophisticated system that builds knowledge graphs from unstructured text and enables advanced querying capabilities.

## What is GraphRAG?

GraphRAG is Microsoft's modular RAG system that:
- **Extracts structured knowledge graphs** from unstructured text using LLMs
- **Identifies entities and relationships** automatically
- **Performs community detection** to create hierarchical organization
- **Supports two query modes**: Local (detailed) and Global (synthesized)
- **Ideal for complex analytical questions** over large document corpora

## Running the Demo

```bash
cd python/graphrag
uv run python main_graphrag.py
```

## Requirements

- **Python**: 3.11+
- **Dependencies**: `graphrag>=0.3.0`, `pandas>=2.0.0` (managed via inline script metadata)
- **Note**: This demo shows concepts and structure. Full GraphRAG execution requires:
  - OpenAI or Azure OpenAI API key
  - API credits (indexing can be expensive: ~$10-50 per MB of text with GPT-4)

---

## Source Code with Line Numbers

```python
1   # /// script
2   # requires-python = ">=3.11"
3   # dependencies = [
4   #     "graphrag>=0.3.0",
5   #     "pandas>=2.0.0",
6   # ]
7   # ///
8   """
9   Microsoft GraphRAG Example: Graph-Based Retrieval Augmented Generation
10
11  This example showcases Microsoft GraphRAG, a modular graph-based RAG system that:
12  1. Extracts structured knowledge graphs from unstructured text
13  2. Uses LLMs to build entity relationships
14  3. Enables advanced querying over graph-structured knowledge
15  4. Provides both local and global search capabilities
16
17  Key Concepts Demonstrated:
18  - GraphRAG architecture and workflow
19  - Configuration and initialization
20  - Document indexing pipeline
21  - Knowledge graph construction
22  - Query capabilities (local and global search)
23  - Community detection and hierarchical summarization
24
25  Note: This demo shows the structure and workflow. Full execution requires:
26  - OpenAI API key or Azure OpenAI credentials
27  - Sufficient API credits (indexing can be expensive)
28  """
29
30  # Example 1: GraphRAG Workflow Overview
31  print("=" * 70)
32  print("Example 1: GraphRAG Workflow Overview")
33  print("=" * 70)
34  print("""
35  GraphRAG Process Flow:
36  ┌──────────────┐
37  │   Documents  │  Raw text documents/corpus
38  └──────┬───────┘
39         │
40         ▼
41  ┌──────────────────────────┐
42  │  Text Chunking           │  Break documents into manageable chunks
43  └──────────┬───────────────┘
44             │
45             ▼
46  ┌──────────────────────────┐
47  │  Entity Extraction       │  LLM identifies entities (people, places, etc.)
48  └──────────┬───────────────┘
49             │
50             ▼
51  ┌──────────────────────────┐
52  │  Relationship Mapping    │  LLM identifies relationships between entities
53  └──────────┬───────────────┘
54             │
55             ▼
56  ┌──────────────────────────┐
57  │  Community Detection     │  Cluster related entities into communities
58  └──────────┬───────────────┘
59             │
60             ▼
61  ┌──────────────────────────┐
62  │  Community Summarization │  Generate summaries for each community
63  └──────────┬───────────────┘
64             │
65             ▼
66  ┌──────────────────────────┐
67  │  Knowledge Graph         │  Complete graph with entities, relationships,
68  │                          │  and hierarchical community structure
69  └──────────────────────────┘
70
71  Query Types:
72  1. Local Search: Detailed answers using specific entities and their relationships
73  2. Global Search: High-level answers using community summaries
74  """)
...
```

*(Full source code: [main_graphrag.py](main_graphrag.py) - 560 lines)*

---

## Program Output with Annotations

### Example 1: GraphRAG Workflow (Lines 30-74)

**Source Code (Lines 30-33)**: Prints the workflow overview header

**Output (Lines 1-44)**:
```
======================================================================
Example 1: GraphRAG Workflow Overview
======================================================================

GraphRAG Process Flow:
┌──────────────┐
│   Documents  │  Raw text documents/corpus
└──────┬───────┘
       │
       ▼
┌──────────────────────────┐
│  Text Chunking           │  Break documents into manageable chunks
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Entity Extraction       │  LLM identifies entities (people, places, etc.)
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Relationship Mapping    │  LLM identifies relationships between entities
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Community Detection     │  Cluster related entities into communities
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Community Summarization │  Generate summaries for each community
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│  Knowledge Graph         │  Complete graph with entities, relationships,
│                          │  and hierarchical community structure
└──────────────────────────┘

Query Types:
1. Local Search: Detailed answers using specific entities and their relationships
2. Global Search: High-level answers using community summaries
```

**💡 Key Concept**: GraphRAG follows a multi-stage pipeline that transforms raw documents into a queryable knowledge graph. Unlike traditional RAG which retrieves text chunks, GraphRAG builds an explicit graph of entities and relationships.

---

### Example 2: Configuration Structure (Lines 77-92)

**Source Code (Lines 80-88)**: Demonstrates the YAML configuration structure for GraphRAG

**Output (Lines 47-91)**:
```yaml
# Minimal settings.yaml example
llm:
  api_key: ${GRAPHRAG_API_KEY}  # Environment variable
  type: openai_chat              # or azure_openai_chat
  model: gpt-4-turbo-preview
  max_tokens: 4000
  temperature: 0.0

embeddings:
  llm:
    api_key: ${GRAPHRAG_API_KEY}
    type: openai_embedding
    model: text-embedding-3-small

input:
  type: file
  file_type: text
  base_dir: "input"
  file_pattern: ".*\\.txt$"

storage:
  type: file
  base_dir: "output"

chunks:
  size: 1200
  overlap: 100

entity_extraction:
  prompt: "prompts/entity_extraction.txt"
  max_gleanings: 1

community_reports:
  prompt: "prompts/community_report.txt"
```

**💡 Configuration Explained**:
- **llm**: Specifies the LLM for entity extraction and summarization (GPT-4 recommended)
- **embeddings**: Used for vector similarity searches
- **chunks**: Text is split into 1200-token chunks with 100-token overlap
- **entity_extraction**: Controls how entities are identified from text
- **community_reports**: Controls hierarchical summarization

---

### Example 3: Sample Documents (Lines 95-114)

**Source Code (Lines 97-111)**: Defines sample documents about Microsoft for knowledge graph extraction

**Output (Lines 96-114)**:
```
Sample corpus for GraphRAG indexing:

doc1.txt:
Microsoft Corporation is a technology company founded by Bill Gates and Paul Allen
in 1975. The company is headquartered in Redmond, Washington. Satya Nadella became
CEO in 2014 and has led the company through significant cloud computing growth with
Azure.

doc2.txt:
Azure is Microsoft's cloud computing platform that competes with AWS and Google Cloud.
It offers services including virtual machines, databases, and AI capabilities. Azure's
growth has been a major driver of Microsoft's revenue under Satya Nadella's leadership.

doc3.txt:
GitHub was acquired by Microsoft in 2018 for $7.5 billion. The platform hosts millions
of open source projects and is used by developers worldwide. Nat Friedman served as
GitHub's CEO after the acquisition before Thomas Dohmke took over in 2021.
```

**💡 Document Structure**: These documents contain rich relational information that GraphRAG will extract, including entities (Microsoft, Bill Gates, Azure), relationships (founded by, competes with, acquired), and temporal data (dates and timelines).

---

### Example 4: Indexing Pipeline (Lines 117-157)

**Source Code (Lines 119-143)**: Shows how to run the indexing pipeline using CLI or Python API

**Output (Lines 117-157)**:
```
======================================================================
Example 4: Indexing Pipeline
======================================================================

To index documents using GraphRAG CLI:
  $ graphrag init --root ./my_project
  $ # Edit settings.yaml and add API key
  $ graphrag index --root ./my_project

Or using Python API:

from pathlib import Path
from graphrag.config import load_config
from graphrag.index import run_pipeline_with_config

# Load configuration
config_path = Path("./settings.yaml")
config = load_config(config_path)

# Run indexing pipeline
result = await run_pipeline_with_config(config)

print(f"Indexing completed: {result.status}")
print(f"Entities extracted: {len(result.entities)}")
print(f"Relationships found: {len(result.relationships)}")
print(f"Communities detected: {len(result.communities)}")

Indexing Output (example structure):

output/
├── artifacts/
│   ├── create_base_text_units.parquet    # Text chunks
│   ├── create_base_extracted_entities.parquet  # Entities
│   ├── create_summarized_entities.parquet      # Entity descriptions
│   ├── create_base_entity_graph.parquet        # Entity relationships
│   ├── create_final_communities.parquet        # Community structure
│   └── create_final_community_reports.parquet  # Community summaries
└── cache/
    └── [LLM response cache files]
```

**💡 Indexing Process**: The pipeline creates several parquet files storing entities, relationships, and hierarchical communities. This preprocessing is expensive but enables fast querying later.

---

### Example 5: Knowledge Graph Structure (Lines 160-209)

**Source Code (Lines 162-209)**: Illustrates the extracted entities, relationships, and communities

**Output (Lines 160-209)**:
```
======================================================================
Example 5: Extracted Knowledge Graph (Example)
======================================================================

Based on our sample documents, GraphRAG would extract:

ENTITIES:
┌──────────────────────┬────────────────┬─────────────────────────────┐
│ Entity               │ Type           │ Description                 │
├──────────────────────┼────────────────┼─────────────────────────────┤
│ Microsoft            │ Organization   │ Technology company          │
│ Bill Gates           │ Person         │ Microsoft co-founder        │
│ Paul Allen           │ Person         │ Microsoft co-founder        │
│ Satya Nadella        │ Person         │ Microsoft CEO since 2014    │
│ Azure                │ Product        │ Cloud computing platform    │
│ GitHub               │ Organization   │ Developer platform          │
│ Redmond, Washington  │ Location       │ Microsoft headquarters      │
│ AWS                  │ Product        │ Competing cloud platform    │
│ Google Cloud         │ Product        │ Competing cloud platform    │
│ Nat Friedman         │ Person         │ Former GitHub CEO           │
│ Thomas Dohmke        │ Person         │ Current GitHub CEO          │
└──────────────────────┴────────────────┴─────────────────────────────┘

RELATIONSHIPS:
┌──────────────┬─────────────────┬──────────────┬────────────────────┐
│ Source       │ Relationship    │ Target       │ Description        │
├──────────────┼─────────────────┼──────────────┼────────────────────┤
│ Bill Gates   │ FOUNDED         │ Microsoft    │ Co-founded in 1975 │
│ Paul Allen   │ FOUNDED         │ Microsoft    │ Co-founded in 1975 │
│ Satya Nadella│ LEADS           │ Microsoft    │ CEO since 2014     │
│ Microsoft    │ DEVELOPS        │ Azure        │ Cloud platform     │
│ Azure        │ COMPETES_WITH   │ AWS          │ Cloud competition  │
│ Azure        │ COMPETES_WITH   │ Google Cloud │ Cloud competition  │
│ Microsoft    │ ACQUIRED        │ GitHub       │ $7.5B in 2018     │
│ Nat Friedman │ LED             │ GitHub       │ CEO after acquire  │
│ Thomas Dohmke│ LEADS           │ GitHub       │ Current CEO        │
└──────────────┴─────────────────┴──────────────┴────────────────────┘

COMMUNITIES (hierarchical clustering):
Community 1: Microsoft Leadership
  - Members: Microsoft, Bill Gates, Paul Allen, Satya Nadella
  - Summary: Core Microsoft organization and founding/current leadership

Community 2: Cloud Computing Ecosystem
  - Members: Azure, AWS, Google Cloud, Satya Nadella
  - Summary: Cloud platform competitive landscape and Microsoft's position

Community 3: Developer Platform Acquisition
  - Members: GitHub, Microsoft, Nat Friedman, Thomas Dohmke
  - Summary: GitHub acquisition and leadership transition
```

**💡 Graph Structure**:
- **Entities**: 11 extracted entities with types (Person, Organization, Product, Location)
- **Relationships**: 9 explicit relationships forming the knowledge graph
- **Communities**: 3 detected communities representing cohesive topic clusters

This structured representation enables sophisticated queries that traditional RAG cannot handle.

---

### Example 6: Local Search (Lines 212-249)

**Source Code (Lines 218-248)**: Demonstrates local search for detailed, entity-focused queries

**Output (Lines 212-249)**:
```
======================================================================
Example 6: Local Search Query
======================================================================

Local Search: Provides detailed answers using specific entities and their
immediate relationships from the knowledge graph.

Query: "Who are the founders of Microsoft and what did they create?"

Process:
1. Identify relevant entities: Microsoft, Bill Gates, Paul Allen
2. Retrieve direct relationships and descriptions
3. Synthesize answer from local graph neighborhood

Expected Answer:
"Microsoft was founded by Bill Gates and Paul Allen in 1975. The company,
headquartered in Redmond, Washington, is a technology company that has developed
various products including Azure, their cloud computing platform. The company is
currently led by CEO Satya Nadella, who took over leadership in 2014."

Code example:

from graphrag.query import LocalSearch

# Initialize local search
local_search = LocalSearch(
    config=config,
    context_builder=context_builder,
    token_encoder=token_encoder,
)

# Execute query
result = await local_search.asearch(
    "Who are the founders of Microsoft and what did they create?"
)

print(f"Answer: {result.response}")
print(f"Context data: {len(result.context_data)} items")
```

**💡 Local Search**: Focuses on a specific part of the graph, retrieving entities and their immediate connections. Best for questions about specific people, places, or things.

---

### Example 7: Global Search (Lines 252-291)

**Source Code (Lines 258-290)**: Demonstrates global search for broad, analytical queries

**Output (Lines 252-291)**:
```
======================================================================
Example 7: Global Search Query
======================================================================

Global Search: Provides high-level answers using community summaries,
ideal for broad questions requiring synthesis across many entities.

Query: "What are Microsoft's major strategic initiatives?"

Process:
1. Identify relevant communities across the knowledge graph
2. Use pre-generated community summaries (not individual entities)
3. Synthesize answer from hierarchical community reports

Expected Answer:
"Microsoft's major strategic initiatives include: (1) Cloud computing growth through
Azure platform, competing with AWS and Google Cloud; (2) Expanding developer ecosystem
through the GitHub acquisition for $7.5 billion; (3) Leadership transformation under
CEO Satya Nadella who has driven cloud-first strategy since 2014."

This answer synthesizes information across all three communities identified earlier.

Code example:

from graphrag.query import GlobalSearch

# Initialize global search
global_search = GlobalSearch(
    config=config,
    context_builder=context_builder,
    token_encoder=token_encoder,
)

# Execute query
result = await global_search.asearch(
    "What are Microsoft's major strategic initiatives?"
)

print(f"Answer: {result.response}")
print(f"Reports used: {len(result.reports)}")
```

**💡 Global Search**: Uses pre-generated community summaries rather than individual entities. Ideal for "what are the main themes?" or "what are the major trends?" type questions requiring synthesis.

---

### Example 8: GraphRAG vs Traditional RAG (Lines 294-322)

**Output (Lines 294-322)**:
```
======================================================================
Example 8: GraphRAG vs Traditional RAG
======================================================================

Traditional RAG (Retrieval Augmented Generation):
- Retrieves relevant text chunks based on similarity
- Limited understanding of relationships
- Struggles with questions requiring synthesis across documents
- Example: "Find mentions of Azure"

GraphRAG Advantages:
- Understands entity relationships explicitly
- Community detection enables hierarchical organization
- Global search synthesizes across entire corpus
- Better for exploratory and analytical questions
- Example: "How are Microsoft's products competing in cloud market?"

When to use GraphRAG:
✓ Complex multi-document question answering
✓ Domain exploration and discovery
✓ Questions about relationships and connections
✓ Analytical queries requiring synthesis
✓ Corporate intelligence and research

When to use Traditional RAG:
✓ Simple fact retrieval
✓ Looking for specific passages
✓ Lower cost requirements
✓ Smaller, simpler document sets
```

**💡 Key Distinction**: Traditional RAG is like keyword search with semantic understanding. GraphRAG is like having a researcher who understands the relationships and can synthesize insights.

---

### Example 9: Cost Considerations (Lines 325-351)

**Output (Lines 325-351)**:
```
======================================================================
Example 9: Cost and Performance Considerations
======================================================================

Indexing Costs (example for 1MB of text):
- Entity extraction: 50-100 LLM calls
- Relationship extraction: 50-100 LLM calls
- Community summarization: 20-50 LLM calls
- Using GPT-4: ~$10-50 per MB of text
- Using GPT-3.5: ~$2-10 per MB of text

Query Costs:
- Local search: 1-2 LLM calls per query (~$0.01-0.05)
- Global search: 2-5 LLM calls per query (~$0.05-0.20)

Performance Tips:
1. Use prompt tuning to improve extraction quality
2. Cache LLM responses (built-in support)
3. Start with smaller corpus for testing
4. Use GPT-3.5 for initial development
5. Adjust chunk size based on document structure

Storage Requirements:
- Input: 1 MB text
- Output artifacts: 5-10 MB (parquet files)
- Vector embeddings: 2-5 MB
- Total: ~8-16x input size
```

**💡 Cost Warning**: GraphRAG indexing is expensive due to many LLM calls. Budget $10-50 per MB with GPT-4. However, querying is cheap once indexed. Cache responses and start small.

---

### Example 10: Complete Workflow (Lines 354-398)

**Output (Lines 354-398)**:
```
Step-by-Step GraphRAG Implementation:

1. SETUP
   $ pip install graphrag
   $ graphrag init --root ./my_graphrag_project
   $ cd my_graphrag_project

2. CONFIGURE
   Edit settings.yaml:
   - Add your OpenAI/Azure OpenAI API key
   - Configure model settings (gpt-4-turbo recommended)
   - Set chunk size (1200 tokens is default)
   - Configure entity extraction prompts

3. PREPARE DATA
   $ mkdir input
   $ cp /path/to/documents/*.txt input/
   [Place your text documents in the input directory]

4. INDEX (BUILD KNOWLEDGE GRAPH)
   $ graphrag index --root .
   [This runs the full pipeline: chunking, entity extraction,
    relationship mapping, community detection, summarization]

   Expected time: 5-30 minutes depending on corpus size
   Expected cost: $10-100+ depending on corpus size

5. QUERY
   # Using CLI
   $ graphrag query --root . --method local "What is...?"
   $ graphrag query --root . --method global "What are...?"

   # Using Python API
   from graphrag.query import LocalSearch, GlobalSearch
   # ... (see examples above)

6. ITERATE
   - Review extraction quality
   - Tune prompts if needed (graphrag prompt-tune)
   - Adjust chunk size and overlap
   - Re-index with improvements
```

**💡 Production Workflow**: Shows the complete end-to-end process from installation to iteration. The prompt tuning step (6) is critical for good results.

---

### Example 11: Complete Python API Example (Lines 401-443)

**Output (Lines 407-443)**:
```python
import asyncio
from pathlib import Path
from graphrag.config import load_config
from graphrag.index import run_pipeline_with_config
from graphrag.query import LocalSearch, GlobalSearch


async def main():
    # 1. Load configuration
    config = load_config(Path("./settings.yaml"))

    # 2. Run indexing pipeline
    print("Starting indexing pipeline...")
    result = await run_pipeline_with_config(config)
    print(f"Indexing complete: {result.status}")

    # 3. Setup search engines
    local_search = LocalSearch(config=config)
    global_search = GlobalSearch(config=config)

    # 4. Perform queries
    print("\nLocal Search Query:")
    local_result = await local_search.asearch(
        "Who founded Microsoft?"
    )
    print(f"Answer: {local_result.response}")

    print("\nGlobal Search Query:")
    global_result = await global_search.asearch(
        "What are the main themes in the documents?"
    )
    print(f"Answer: {global_result.response}")


if __name__ == "__main__":
    asyncio.run(main())
```

**💡 Python API**: Shows how to use GraphRAG programmatically. Note the async/await pattern - GraphRAG operations are asynchronous for performance.

---

## Summary: Key Takeaways (Output Lines 446-493)

```
Microsoft GraphRAG is a sophisticated RAG system that:

✓ Builds knowledge graphs from unstructured text
✓ Uses LLMs for entity and relationship extraction
✓ Performs community detection for hierarchical organization
✓ Supports both local (detailed) and global (synthesized) search
✓ Ideal for complex analytical questions over large corpora

Key Components:
1. Configuration: settings.yaml with LLM and storage config
2. Indexing: Multi-stage pipeline creating knowledge graph
3. Query: Local and global search over graph structure
4. Storage: Parquet files for entities, relationships, communities

Requirements:
- Python 3.11+
- OpenAI or Azure OpenAI API access
- Budget for LLM calls (indexing is expensive)
- Understanding of graph concepts

Best For:
- Corporate intelligence
- Research corpus analysis
- Complex multi-document Q&A
- Domain exploration
- Relationship discovery
```

---

## Version Requirements

- **Python**: 3.11 or higher (required for modern async features and type hints)
- **graphrag**: 0.3.0 or higher
- **LLM API**: Requires OpenAI (GPT-4 or GPT-3.5) or Azure OpenAI
- **Note**: This demonstration runs without API keys and shows the conceptual structure

---

## Learn More

- **GitHub**: https://github.com/microsoft/graphrag
- **Documentation**: https://microsoft.github.io/graphrag
- **PyPI Package**: https://pypi.org/project/graphrag

---

## Architecture Diagram

```
┌─────────────────┐
│  Raw Documents  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐     ┌──────────────┐
│ Text Chunking   │────>│  LLM (GPT-4) │
└────────┬────────┘     └──────────────┘
         │                      │
         ▼                      ▼
┌─────────────────┐     ┌──────────────┐
│ Entity Extract  │<────┤  Embeddings  │
└────────┬────────┘     └──────────────┘
         │
         ▼
┌─────────────────┐
│ Relationship    │
│ Mapping         │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Community       │
│ Detection       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Knowledge Graph │
│   (Parquet)     │
└────────┬────────┘
         │
         ├────────> Local Search (Detailed queries)
         │
         └────────> Global Search (Synthesis queries)
```

---

**Created**: 2025-11-05
**GraphRAG Version**: 0.3.0+
**Python Version**: 3.11+
