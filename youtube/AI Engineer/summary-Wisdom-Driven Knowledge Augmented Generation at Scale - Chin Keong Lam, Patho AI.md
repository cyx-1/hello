# Wisdom-Driven Knowledge Augmented Generation at Scale - Chin Keong Lam, Patho AI

**Video URL:** https://www.youtube.com/watch?v=9AQOvT8LnMI

---

## Executive Summary

Chin Keong Lam, founder and CEO of Patho.AI, presents an approach to building AI systems that go beyond traditional RAG (Retrieval Augmented Generation) by implementing Knowledge Augmented Generation (KAG) using wisdom-driven knowledge graphs. The talk focuses on how to build expert AI systems for complex tasks like competitive analysis by mapping domain expertise into a graph structure that captures not just knowledge, but wisdom - the understanding of how to apply that knowledge. Using a practical competitive analysis use case, Lam demonstrates how to implement this architecture using Node-RED and Neo4j, achieving 91% accuracy compared to traditional vector-based RAG systems.

---

## Main Topics

### 1. Introduction to Patho.AI and Background
**[00:17](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=17s) - [01:09](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=69s)**

- Patho.AI started 2 years ago with NSF SBIR grant funding for LLM-driven drug discovery
- Now building expert AI systems for large corporations that go beyond RAG
- Clients want AI systems that perform research and advisory roles, not just retrieve information
- The talk shares lessons learned from building these systems

### 2. Defining Knowledge, Knowledge Graphs, and KAG
**[01:11](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=71s) - [02:21](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=141s)**

- **Knowledge**: Understanding and awareness gained through experience, education, and comprehension of facts
- **Knowledge Graph**: Systematic method of preserving wisdom by connecting information and creating interconnected relationships
- Represents thought processes and comprehensive taxonomy of a specific domain
- **KAG (Knowledge Augmented Generation)**: Different from RAG - enhances language models by integrating structured knowledge graphs for more accurate and insightful responses
- Key difference: "KAG doesn't just retrieve, it understands"

### 3. The Wisdom-Driven Framework: Core Concepts
**[02:21](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=141s) - [04:42](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=282s)**

- Expert thinking patterns show common decision-making processes - knowledge graphs are a perfect fit
- **State diagram components:**
  - **Wisdom Node (Core)**: Actively guides decisions, not passive
  - **Decision Making**: Wisdom guides decisions, analyzing real-world situations
  - **Knowledge → Wisdom**: Like books and encyclopedias being absorbed and synthesized by the model
  - **Insight → Wisdom**: Deriving patterns from chaos (e.g., social media sentiment analysis)
  - **Feedback Loops**: System learns from itself - situations inform future wisdom, experience deepens it

**Practical analogy (Pizza):**
- Knowledge = recipe
- Experience = knowing your oven burns crust
- Insight = adding honey to caramelize crust perfectly

### 4. Applying the Framework: Competitive Analysis Use Case
**[06:21](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=381s) - [08:39](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=519s)**

Mapping the abstract wisdom framework to a real client project:

- **Wisdom Engine** → Orchestration agent making decisions and advising
- **Decision Making** → Strategy Generator
- **Knowledge** → Market data
- **Experience** → Past campaigns
- **Insight** → Industry insights database
- **Situation** → Competitor weakness analysis

Goal: Answer sophisticated questions like "How do I win against my competitor in this market space?" - something simple RAG cannot handle

### 5. Implementation with Node-RED Multi-Agent System
**[08:40](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=520s) - [11:28](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=688s)**

- **Node-RED**: Workflow automation tool, no-code but powerful (used in IoT projects by IBM)
- Highly flexible for prototyping, uses Node.js underneath
- AI agent nodes enable implementation of complex state diagrams
- **Architecture:**
  - **Wisdom Agent**: Supervisory agent overseeing other specialized agents
  - Can use OpenAI, Anthropic, or on-premise models
  - **Insight Agent**: Collects social media sentiment, product feedback
  - All agents update a centralized Neo4j knowledge graph
  - Each agent updates their respective part of the taxonomy
- The unified knowledge graph contains the complete marketing strategy taxonomy
- Similar to organizing folders in SharePoint, but with graph relationships

### 6. Why Knowledge Graphs Over Traditional Vector RAG
**[11:38](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=698s) - [13:58](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=838s)**

Five key reasons for using knowledge graphs:

1. **Complex Relationship Modeling**: Captures interconnected relationships between entities, leading to deeper contextual understanding crucial for comparative analysis
2. **Improved Accuracy**: Leverages structured data and semantic relationships for more accurate, precise information with reduced noise - critical for contract work
3. **Scalability and Flexibility**: Easily integrates new data sources and relationships, allowing continuous improvement
4. **Rich Query Capability**: Supports complex multi-hop queries traversing multiple relationships - where simple RAG fails
5. **Enhanced Data Integration**: Seamlessly integrates diverse data sources (text, images, videos) with OCR capabilities

### 7. Vector RAG Limitations: Numerical Reasoning Example
**[14:00](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=840s) - [15:31](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=931s)**

**Problem**: Vector RAG is bad at numerical reasoning
- Vector stores excel at semantic similarity but struggle with complex numerical calculations
- Marketing analysis relies on numbers, not just text retrieval

**Example Query**: "What is Apple's revenue growth between 2021 and 2022?"
- **Vector RAG**: Returns passages of text
- **Knowledge Graph**:
  - Structured data in Neo4j (Apple financial data)
  - Query engine selects revenue figures from 2021-2022
  - Function call calculates exact result: 15.23%
  - Evidence-based decision making vs. text passage retrieval

### 8. Hybrid Architecture: RAG + KAG
**[15:31](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=931s) - [16:35](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=995s)**

**Technology options:**
- LangChain + ChromaDB for RAG
- Can combine with knowledge graphs depending on use case

**Adoption strategy:**
- **Simple queries** (product information): ChromaDB + LLM agent
- **Complex queries** ("How can I beat my competition based on current market share?"):
  - Neo4j graph DB + Cypher queries
  - Multi-hop query loops
  - Wisdom graph (shown in red in architecture diagram)

### 9. Graph Extraction Strategies
**[16:37](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=997s) - [17:16](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=1036s)**

**Three approaches:**
1. **Manual**: Human-defined schema (left side)
2. **Automated**: LLM Graph Transformer (right side)
3. **Hybrid (Recommended)**:
   - Use LLM to extract initial graph
   - Interview domain experts to build proper taxonomy
   - Prune the graph by removing unnecessary relationships
   - Results in more accurate, focused knowledge representation

### 10. Benchmark Results and Performance Metrics
**[17:16](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=1036s) - [17:41](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=1061s)**

KAG system achievements:
1. **Accuracy**: 91% (excellent at extracting structure)
2. **Flexibility**: 85%
3. **Reproducibility**: High (deterministic results)
4. **Traceability**: Strong lineage tracking
5. **Scalability**: Excellent for growing datasets

### 11. Conclusion and Resources
**[17:41](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=1061s) - [18:37](https://www.youtube.com/watch?v=9AQOvT8LnMI&t=1117s)**

**Key takeaway**: By leveraging the structured nature of domain wisdom in knowledge graphs, we can significantly enhance the capability of KAG systems to provide more accurate and insightful responses to complex queries.

**Vision**: Wisdom-driven systems can potentially surpass the intelligence of the initial expert they were meant to serve.

**Resources**:
- LLM Graph RAG Stack on GitHub (sponsored by Neo4j)
- Out-of-the-box Docker setup
- Automatically converts text to graphs
- Ready for graph pruning and customization

---

## Key Technical Insights

1. **Wisdom vs. Knowledge**: The system doesn't just store facts - it captures how experts think and make decisions through graph relationships
2. **Multi-Agent Architecture**: Specialized agents (insight, strategy, knowledge) update different parts of a unified knowledge graph
3. **Taxonomy is Critical**: The quality of decision-making depends heavily on proper graph structure, not just the LLM model
4. **Evidence-Based Decision Making**: Knowledge graphs enable quantitative, precise answers vs. text passage retrieval
5. **Scalability Through Structure**: As the system learns and feedback loops operate, wisdom grows like "a tree growing roots"

---

## Technologies Mentioned

- **Node-RED**: Workflow automation and orchestration
- **Neo4j**: Graph database
- **Cypher**: Graph query language
- **LangChain**: RAG framework
- **ChromaDB**: Vector database
- **OpenAI, Anthropic**: LLM providers
- **LLM Graph Transformer**: Automated graph extraction
- **Docker**: Containerization for deployment

---

*Total Video Length: ~18:37*
