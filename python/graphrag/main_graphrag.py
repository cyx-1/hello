# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "graphrag>=0.3.0",
#     "pandas>=2.0.0",
# ]
# ///
"""
Microsoft GraphRAG Example: Graph-Based Retrieval Augmented Generation

This example showcases Microsoft GraphRAG, a modular graph-based RAG system that:
1. Extracts structured knowledge graphs from unstructured text
2. Uses LLMs to build entity relationships
3. Enables advanced querying over graph-structured knowledge
4. Provides both local and global search capabilities

Key Concepts Demonstrated:
- GraphRAG architecture and workflow
- Configuration and initialization
- Document indexing pipeline
- Knowledge graph construction
- Query capabilities (local and global search)
- Community detection and hierarchical summarization

Note: This demo shows the structure and workflow. Full execution requires:
- OpenAI API key or Azure OpenAI credentials
- Sufficient API credits (indexing can be expensive)
"""

# Example 1: GraphRAG Workflow Overview
print("=" * 70)
print("Example 1: GraphRAG Workflow Overview")
print("=" * 70)
print("""
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
""")


# Example 2: Configuration Structure
print("\n" + "=" * 70)
print("Example 2: GraphRAG Configuration")
print("=" * 70)
print("""
GraphRAG requires configuration via settings.yaml or Python config object.

Key Configuration Sections:
""")

config_example = """
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
  file_pattern: ".*\\\\.txt$"

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
"""

print(config_example)
print("\nConfiguration loads from: ./settings.yaml or programmatically")


# Example 3: Sample Documents for Indexing
print("\n" + "=" * 70)
print("Example 3: Sample Documents for Knowledge Graph")
print("=" * 70)

sample_documents = {
    "doc1.txt": """
Microsoft Corporation is a technology company founded by Bill Gates and Paul Allen
in 1975. The company is headquartered in Redmond, Washington. Satya Nadella became
CEO in 2014 and has led the company through significant cloud computing growth with
Azure.
""",
    "doc2.txt": """
Azure is Microsoft's cloud computing platform that competes with AWS and Google Cloud.
It offers services including virtual machines, databases, and AI capabilities. Azure's
growth has been a major driver of Microsoft's revenue under Satya Nadella's leadership.
""",
    "doc3.txt": """
GitHub was acquired by Microsoft in 2018 for $7.5 billion. The platform hosts millions
of open source projects and is used by developers worldwide. Nat Friedman served as
GitHub's CEO after the acquisition before Thomas Dohmke took over in 2021.
""",
}

print("Sample corpus for GraphRAG indexing:")
for filename, content in sample_documents.items():
    print(f"\n{filename}:")
    print(content.strip())

print("\n[In practice, these would be stored in the 'input' directory]")


# Example 4: Indexing Process (Conceptual)
print("\n" + "=" * 70)
print("Example 4: Indexing Pipeline")
print("=" * 70)
print("""
To index documents using GraphRAG CLI:
  $ graphrag init --root ./my_project
  $ # Edit settings.yaml and add API key
  $ graphrag index --root ./my_project

Or using Python API:
""")

indexing_code = """
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
"""

print(indexing_code)
print("\nIndexing Output (example structure):")
print("""
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
""")


# Example 5: Knowledge Graph Structure
print("\n" + "=" * 70)
print("Example 5: Extracted Knowledge Graph (Example)")
print("=" * 70)
print("""
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
""")


# Example 6: Query with Local Search
print("\n" + "=" * 70)
print("Example 6: Local Search Query")
print("=" * 70)
print("""
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
""")

local_search_code = """
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
"""

print("Code example:")
print(local_search_code)


# Example 7: Query with Global Search
print("\n" + "=" * 70)
print("Example 7: Global Search Query")
print("=" * 70)
print("""
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
""")

global_search_code = """
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
"""

print("Code example:")
print(global_search_code)


# Example 8: Key Advantages of GraphRAG
print("\n" + "=" * 70)
print("Example 8: GraphRAG vs Traditional RAG")
print("=" * 70)
print("""
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
""")


# Example 9: Cost and Performance Considerations
print("\n" + "=" * 70)
print("Example 9: Cost and Performance Considerations")
print("=" * 70)
print("""
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
""")


# Example 10: Complete Workflow Example
print("\n" + "=" * 70)
print("Example 10: Complete GraphRAG Project Workflow")
print("=" * 70)
print("""
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
""")


# Example 11: Python API Usage Example
print("\n" + "=" * 70)
print("Example 11: Python API - Complete Example")
print("=" * 70)
print("""
Here's a complete Python script using GraphRAG API:
""")

complete_example = """
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
    print("\\nLocal Search Query:")
    local_result = await local_search.asearch(
        "Who founded Microsoft?"
    )
    print(f"Answer: {local_result.response}")

    print("\\nGlobal Search Query:")
    global_result = await global_search.asearch(
        "What are the main themes in the documents?"
    )
    print(f"Answer: {global_result.response}")


if __name__ == "__main__":
    asyncio.run(main())
"""

print(complete_example)


# Summary
print("\n" + "=" * 70)
print("Summary: Microsoft GraphRAG Key Takeaways")
print("=" * 70)
print("""
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

Learn More:
- GitHub: https://github.com/microsoft/graphrag
- Docs: https://microsoft.github.io/graphrag
- PyPI: https://pypi.org/project/graphrag

Note: This demonstration showed the concepts and structure.
To run GraphRAG, you need to:
1. Install graphrag package
2. Configure with API credentials
3. Provide input documents
4. Run indexing pipeline
5. Execute queries
""")

print("\n" + "=" * 70)
print("GraphRAG Demonstration Complete")
print("=" * 70)
