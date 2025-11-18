#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "cognee>=0.1.0",
#     "python-dotenv>=1.0.0",
# ]
# ///

"""
Cognee AI Memory Demonstration
This script illustrates how Cognee handles AI memory by:
1. Adding data to the memory system
2. Building a knowledge graph (cognify)
3. Querying the memory with semantic search
4. Demonstrating persistent memory across sessions
"""

import asyncio
import os
from datetime import datetime


async def main():
    """Main demonstration of Cognee AI memory capabilities."""

    # Line 25: Import cognee after dependencies are installed
    import cognee

    print("=" * 70)
    print("COGNEE AI MEMORY DEMONSTRATION")
    print("=" * 70)
    print()

    # Line 34: Configure LLM provider (using OpenAI as example)
    # In production, use environment variables or .env file
    # os.environ["LLM_API_KEY"] = "your-api-key-here"

    # Line 38: Check if API key is configured
    has_api_key = bool(os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY"))

    if not has_api_key:
        print("⚠️  WARNING: No LLM_API_KEY or OPENAI_API_KEY found in environment")
        print("   Running in demonstration mode without actual API calls")
        print("   To run fully: export OPENAI_API_KEY='your-key-here'")
        print()

    # =========================================================================
    # STEP 1: ADDING DATA TO MEMORY
    # =========================================================================
    print("STEP 1: Adding data to AI memory")
    print("-" * 70)

    # Line 52: Add factual information about Cognee
    data_points = [
        "Cognee is a Python library for building AI memory systems.",
        "Cognee transforms documents into structured knowledge graphs.",
        "The library supports vector search and graph-based retrieval.",
        "Cognee was created to solve the context limitation problem in AI agents.",
        "AI agents can use Cognee to remember past conversations and documents.",
        "Cognee combines embeddings with knowledge graphs for better reasoning.",
    ]

    for idx, data in enumerate(data_points, 1):
        print(f"  [{idx}] Adding: {data[:60]}...")
        if has_api_key:
            # Line 67: Add data to Cognee's memory system
            try:
                await cognee.add(data)
            except Exception as e:
                print(f"      Error: {e}")
                has_api_key = False
        else:
            print(f"      → Would call: await cognee.add('{data[:40]}...')")

    print()
    if has_api_key:
        print("✓ Successfully added 6 data points to memory")
    else:
        print("ℹ  In actual usage, these would be stored in Cognee's memory")
    print()

    # =========================================================================
    # STEP 2: COGNIFYING - BUILDING THE KNOWLEDGE GRAPH
    # =========================================================================
    print("STEP 2: Building knowledge graph (cognifying)")
    print("-" * 70)

    # Line 84: Process data into knowledge graph with embeddings
    print("  Processing data into knowledge graph...")
    print("  - Extracting entities and relationships")
    print("  - Creating vector embeddings")
    print("  - Building graph connections")
    print()

    if has_api_key:
        try:
            # Line 92: Cognify builds the semantic memory structure
            await cognee.cognify()
            print("✓ Knowledge graph built successfully")
        except Exception as e:
            print(f"⚠️  Cognify error: {str(e)[:80]}...")
            has_api_key = False
    else:
        print("  → Would call: await cognee.cognify()")
        print("  ℹ  This would:")
        print("     1. Extract entities (e.g., 'Cognee', 'AI agents', 'knowledge graphs')")
        print("     2. Identify relationships (e.g., 'Cognee' -> 'transforms' -> 'documents')")
        print("     3. Create vector embeddings for semantic similarity")
        print("     4. Store in persistent vector + graph databases")

    print()

    # =========================================================================
    # STEP 3: SEARCHING THE AI MEMORY
    # =========================================================================
    print("STEP 3: Querying AI memory with semantic search")
    print("-" * 70)

    queries = [
        "What is Cognee?",
        "How does Cognee help AI agents?",
        "What technologies does Cognee use?",
    ]

    for query_num, query in enumerate(queries, 1):
        print(f"\nQuery {query_num}: '{query}'")
        print("  " + "─" * 66)

        if has_api_key:
            try:
                # Line 121: Search the knowledge graph
                results = await cognee.search(query)

                if results:
                    print(f"  Found {len(results)} relevant results:")
                    for idx, result in enumerate(results[:3], 1):
                        # Line 127: Display search results
                        result_text = str(result)[:100]
                        print(f"    [{idx}] {result_text}...")
                else:
                    print("  No results found")
            except Exception as e:
                print(f"  ⚠️  Search error: {str(e)[:60]}...")
                has_api_key = False
        else:
            print(f"  → Would call: await cognee.search('{query}')")
            print("  ℹ  Expected results based on our data:")

            if query_num == 1:
                print("     • 'Cognee is a Python library for building AI memory systems.'")
                print("     • 'Cognee transforms documents into structured knowledge graphs.'")
            elif query_num == 2:
                print("     • 'AI agents can use Cognee to remember past conversations...'")
                print("     • 'Cognee was created to solve the context limitation problem...'")
            else:
                print("     • 'The library supports vector search and graph-based retrieval.'")
                print("     • 'Cognee combines embeddings with knowledge graphs...'")

    print()

    # =========================================================================
    # STEP 4: MEMORY PERSISTENCE DEMONSTRATION
    # =========================================================================
    print("STEP 4: Memory persistence")
    print("-" * 70)

    print("  Cognee stores data in persistent storage:")
    print("  - Vector embeddings in vector database (LanceDB by default)")
    print("  - Knowledge graph in graph database (Kùzu by default)")
    print("  - Memory persists across Python sessions")
    print("  - Can be queried anytime without re-processing")
    print()

    # Line 159: Demonstrate additional Cognee operations
    print("  Additional memory management operations:")
    print("  - await cognee.prune.prune_data()  # Clean up old data")
    print("  - await cognee.prune.prune_system()  # Reset entire system")
    print("  - await cognee.status()  # Check memory status")
    print()

    if has_api_key:
        # Line 166: Check memory status
        try:
            print("  Cleaning up demo data...")
            await cognee.prune.prune_data()
            print("  ✓ Memory pruned successfully")
        except Exception as e:
            print(f"  Note: {str(e)[:60]}...")

    print()

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print("=" * 70)
    print("SUMMARY: How Cognee Handles AI Memory")
    print("=" * 70)
    print("""
1. DATA INGESTION (.add())
   - Accepts text, documents, conversations
   - Chunks and preprocesses content
   - Prepares for knowledge extraction

2. KNOWLEDGE GRAPH BUILDING (.cognify())
   - Extracts entities and relationships
   - Creates vector embeddings for semantic search
   - Builds interconnected knowledge graph
   - Stores in persistent databases

3. MEMORY RETRIEVAL (.search())
   - Semantic search using vector similarity
   - Graph traversal for contextual connections
   - Returns relevant information with context
   - Combines multiple retrieval strategies

4. PERSISTENCE
   - Memory stored in local/remote databases
   - Survives application restarts
   - Can be shared across AI agent instances
   - Supports incremental updates

KEY ADVANTAGES:
✓ Goes beyond simple RAG (Retrieval Augmented Generation)
✓ Understands relationships between information
✓ Provides context-aware memory for AI agents
✓ Scales to large document collections
✓ Enables long-term memory for conversational AI
""")

    print("=" * 70)
    print(f"Demo completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)


if __name__ == "__main__":
    # Line 198: Run the async main function
    asyncio.run(main())
