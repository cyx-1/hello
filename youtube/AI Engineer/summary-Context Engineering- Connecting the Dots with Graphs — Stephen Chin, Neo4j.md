# Context Engineering: Connecting the Dots with Graphs — Stephen Chin, Neo4j

**Video URL:** https://www.youtube.com/watch?v=LLuKshphGOE

---

## Executive Summary

Stephen Chin, VP of Developer Relations at Neo4j, presents a comprehensive guide to context engineering using knowledge graphs to improve AI applications. Using a Matrix movie theme throughout, he demonstrates how to evolve from basic prompt engineering to sophisticated context engineering by leveraging graph databases. The talk covers the fundamentals of knowledge graphs, Graph RAG (Retrieval Augmented Generation), and includes two live demos: a simple Graph RAG implementation using Neo4j's Knowledge Graph Builder for security vulnerability analysis, and an advanced agentic retrieval system using Claude Code with MCP servers. The presentation makes a compelling case that combining the structured knowledge of graphs with the language reasoning of LLMs creates more reliable, explainable, and powerful AI applications.

---

## Topics

### [Introduction & Context Engineering Overview](https://www.youtube.com/watch?v=LLuKshphGOE&t=0s)

**Key Points:**
- **The Problem:** AI has created new challenges for developers - we've become "slaves" to prompt engineering and AI model management
- **The Solution:** Context engineering transforms one-shot prompt engineering into dynamic, wide-scope context feeding
- **Evolution:** Moving from clever phrasing to systematic information architecture
- **Benefits:**
  - Feed agents more context and information
  - Create dynamic, goal-driven applications
  - Selectively curate information for domain relevancy
  - Structure input to maximize signal over noise
  - Transform from "prompt engineers" to "information architects"

### [AI Memory: Short-term vs. Long-term](https://www.youtube.com/watch?v=LLuKshphGOE&t=240s)

**Key Points:**
- **Short-term Memory:**
  - Current task context
  - Recent conversation history
  - Tool results integration
  - Must compress as much relevant information as possible
  - Needs to avoid noise from excessive tool outputs
- **Long-term Memory:**
  - Episodic memory from past conversations
  - Semantic and structural meaning extraction
  - Instructions and procedures for AI guidance
  - Planning information for artificial intelligence
- **Core Principle:** "Garbage in, garbage out" - LLMs are only as good as the data quality
- **Tools Mentioned:** DSPY and BAML for dynamic prompting

### [Knowledge Graphs: Structure Meets AI](https://www.youtube.com/watch?v=LLuKshphGOE&t=420s)

**Key Points:**
- **What are Knowledge Graphs?**
  - Facts represented as nodes (people, places, events, things)
  - Relationships connect these nodes
  - Properties attach to both nodes and relationships
- **Example:** Dan and Ann know each other, live together, both drive a Volvo V70
  - Nodes: Dan (Person), Ann (Person), Volvo (Car)
  - Relationships: KNOWS, LIVES_WITH, DRIVES
  - Properties: car model, time duration, embeddings
- **Why They Matter:**
  - Fill the gap between unstructured AI creativity and structured information
  - Easy for both humans and LLMs to read
  - Can serve as digital twins of organizations/supply chains
  - Can encapsulate vector embeddings for semantic search

### [Graph RAG (Retrieval Augmented Generation)](https://www.youtube.com/watch?v=LLuKshphGOE&t=560s)

**Key Points:**
- **Definition:** Any retrieval pipeline that uses graphs as part of the retrieval process
- **How It Works:**
  1. User asks a question
  2. LLM processes query
  3. Searches knowledge graph for relevant information
  4. Passes graph data as additional context to LLM
  5. LLM provides enriched, grounded answer
- **Advantages over Vector RAG:**
  - Information about relationships between nodes
  - Community grouping and domain context
  - Factual, structured knowledge
  - Explainability - you can see what data was passed to the LLM
  - Evolvable - knowledge graph improves over time
  - Role-based access control (e.g., doctors see diagnoses, admins see contact info)

### [Explainable AI with Knowledge Graphs](https://www.youtube.com/watch?v=LLuKshphGOE&t=660s)

**Key Points:**
- Store learnings from users and agents in graph context
- Visualize conversation flows with reasoning chains
- Analyze agent system performance
- Identify improvement opportunities:
  - Quality of results
  - Relationship optimization
  - Duplicate node removal
- Provides control over AI responses
- Like training in a "dojo" - continuous improvement through visible, modifiable structure

### [Demo 1: Graph RAG with Knowledge Graph Builder](https://www.youtube.com/watch?v=LLuKshphGOE&t=720s)

**Key Points:**
- **Setup:**
  - Neo4j Aura instance (free cloud version)
  - LLM Knowledge Graph Builder (open source web application)
- **Documents Loaded:**
  - Supply chain document with artifacts and digital signatures
  - VEX (Vulnerability Exploitability eXchange) security document about Jackson library
- **Process:**
  - Drag and drop files into Knowledge Graph Builder
  - LLM ingests and automatically builds knowledge graph
  - Two-pass retrieval: vector similarity search + related node traversal
- **Test Queries:**
  - Query 1: "Vulnerabilities in Jasper library" → No results (not in knowledge base)
  - Query 2: "Vulnerabilities in Jackson library" → Detailed response about XML injection vulnerability, affected versions (Jackson databind), and remediation
- **Demonstration of Grounding:** AI refuses to answer when data isn't in knowledge graph, answers comprehensively when it is

### [Graph Memory & Advanced Retrieval](https://www.youtube.com/watch?v=LLuKshphGOE&t=960s)

**Key Points:**
- **Graph Memory Capabilities:**
  - Capture knowledge as entities and relationships
  - Store properties: text details, embeddings, time, location
  - Enable vector-based semantic search on graph projections
- **Graph Data Science Algorithms:**
  - K-Approximate Nearest Neighbors (k-ANN)
  - Community groupings
  - Page Rank
  - Bubble up most relevant results into context
- **MCP Server:** Open source tool for graph memory retrieval
- **Example Use Case:** "Update this presentation from the last time I presented with Sid"
  - Multi-hop query: finds presenter (Stephen), finds collaborator (Sid), finds event (GIDS Bangalore), retrieves temporal memory
  - Demonstrates when graphs excel: 2+ degrees of separation, relationship-dependent queries

### [Types of Graph Retrievers](https://www.youtube.com/watch?v=LLuKshphGOE&t=1260s)

**Key Points:**
1. **Explicit Retrieval Queries:**
   - Direct Cypher queries
   - Programmatic, deterministic
2. **Text-to-Cypher:**
   - Fine-tune LLM with graph schema
   - LLM generates Cypher from natural language
   - Single-pass approach
3. **Agentic Traversal:**
   - Iterative navigation of the graph
   - Multiple queries to explore relationships
   - Most comprehensive results

### [Demo 2: Agentic Retrieval with Claude Code](https://www.youtube.com/watch?v=LLuKshphGOE&t=1320s)

**Key Points:**
- **Setup:**
  - Claude Code connected to Neo4j via MCP Cypher server
  - Agentic multi-step query process
- **Query:** "What do you know about the Jackson vulnerability based on your graph database?"
- **Agent Process:**
  1. Retrieves graph schema first
  2. Fires multiple Cypher queries to explore
  3. Pulls related text chunks for context
  4. Synthesizes comprehensive response
- **Enhanced Results vs. Demo 1:**
  - CVE number identification
  - Vulnerability type classification
  - Attack type details (XML injection)
  - Severity levels
  - Technical descriptions
  - Specific version remediation
  - Advisory information
- **Key Insight:** Agentic approach with multiple traversals provides significantly more comprehensive and nuanced results than single-pass retrieval

### [Resources & Learning Path](https://www.youtube.com/watch?v=LLuKshphGOE&t=1480s)

**Key Points:**
- **Graph Academy:** Free courses on Cypher query language and Graph RAG
- **Cypher/GQL:** Now an ISO standard graph query language
- **Nodes AI 2026:** Annual conference (May 5, San Francisco; virtual available)
- **GraphRAG.com:** Community resource for Graph RAG patterns and implementations
- **Neo4j MCP Cypher Server:** Open source MCP extension for Claude integration

---

## Technologies & Tools Referenced

- **Neo4j** - Graph database platform
- **Neo4j Aura** - Free cloud-hosted graph database
- **LLM Knowledge Graph Builder** - Open source tool for building knowledge graphs from documents
- **Cypher/GQL** - Graph query language (ISO standard)
- **MCP (Model Context Protocol)** - Protocol for connecting AI agents to data sources
- **Neo4j MCP Cypher Server** - Open source MCP server implementation
- **Claude Code** - AI coding assistant
- **DSPY & BAML** - Dynamic prompting frameworks
- **VEX** - Vulnerability Exploitability eXchange standard
- **SBOM** - Software Bill of Materials

---

## Key Takeaways

1. **Context Engineering > Prompt Engineering:** The future of AI applications lies in systematically engineering the context, not just crafting clever prompts
2. **Graphs + LLMs = Powerful Combination:** Knowledge graphs provide structure, facts, and relationships while LLMs provide language understanding and creativity
3. **Memory is Essential:** Both short-term (current task) and long-term (historical) memory dramatically improve AI application quality
4. **Graph RAG > Vector RAG:** When relationships and structure matter (2+ degrees of separation), Graph RAG significantly outperforms pure vector similarity search
5. **Agentic Retrieval is Most Powerful:** Multi-step, iterative graph exploration yields the most comprehensive results
6. **Explainability Matters:** Knowledge graphs make AI decisions visible and controllable, crucial for enterprise applications
7. **Role-Based Access Built-In:** Graphs naturally support fine-grained access control and data governance
8. **Continuous Improvement:** Graph-based systems can be refined over time by improving relationships, removing duplicates, and enhancing structure

---

## Practical Applications Demonstrated

- **Security Vulnerability Analysis:** Querying software vulnerabilities with CVE databases
- **Supply Chain Management:** Tracking artifacts, dependencies, and digital signatures
- **Presentation Memory:** Temporal memory of past presentations and collaborations
- **Enterprise Knowledge Management:** Domain-specific, grounded AI responses
- **Multi-Agent Collaboration:** Agents sharing structured memory and context

---

**Last Updated:** 2026-01-01
