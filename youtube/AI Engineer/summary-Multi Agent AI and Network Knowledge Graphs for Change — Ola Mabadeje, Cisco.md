# Multi Agent AI and Network Knowledge Graphs for Change — Ola Mabadeje, Cisco

**Video URL:** https://www.youtube.com/watch?v=m0dxZ-NDKHo

---

## Executive Summary

Ola Mabadeje from Cisco's Outshift incubation group presents a production-level multi-agent AI system designed to reduce failures in network change management. The solution combines three core components: (1) a natural language interface for interaction with IT service management systems, (2) a multi-agent system with specialized agents for impact assessment, testing, and reasoning, and (3) a network knowledge graph built as a digital twin using ArangoDB with OpenConfig schema. The system demonstrates how agents can autonomously analyze change requests, generate test plans, execute tests in a digital twin environment, and deliver comprehensive reports—all while adhering to open standards through the agency.org collective framework for interoperable AI agents.

---

## Topics with Timestamps

### 1. Introduction and Problem Statement
[**00:17**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=17s) - Introduction and background on Cisco's Outshift incubation group
[**01:47**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=107s) - Customer problem: reducing failures in network change management
[**01:58**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=118s) - Identifying where AI agents can add value in the workflow

**Key Points:**
- Ola Mabadeje works in Cisco's Outshift, an incubation group focused on emerging technologies like AI and quantum networking
- Customer challenge: frequent production failures during network change management
- Identified specific workflow steps (steps 3, 4, and 5) where AI agents could reduce pain points
- Goal: determine if AI truly has a role beyond rule-based automation

### 2. Solution Architecture Overview
[**02:34**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=154s) - Three-bucket solution architecture
[**02:41**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=161s) - Natural language interface for network operations teams
[**03:02**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=182s) - Multi-agent system with specialized agents
[**03:20**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=200s) - Network knowledge graph and digital twin concept

**Key Points:**
- **Component 1:** Natural language interface enabling both engineers and systems (like ServiceNow) to interact with the platform
- **Component 2:** Multi-agent system with specialized agents for impact assessment, testing, and reasoning about potential failures
- **Component 3:** Network knowledge graph serving as a digital twin of production network, including tools for testing
- Agents communicate between ServiceNow ITSM tool and the AI system

### 3. Building the Network Knowledge Graph
[**03:47**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=227s) - Challenge of representing complex network environments
[**03:52**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=232s) - Complexity: multiple vendors, devices, and data formats
[**04:08**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=248s) - Creating agent-understandable data schema
[**04:32**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=272s) - Three considerations: data sources, data formats, and delivery methods

**Key Points:**
- Networks involve multiple vendors (firewalls, switches, routers) outputting data in different formats
- Challenge: create a knowledge graph representation that agents can understand and act upon
- Data sources include: controllers, network devices, device agents, configuration management systems
- Data formats: YANG, JSON, and other networking-specific languages
- Delivery methods: streaming telemetry, configuration files, various data forms

### 4. Knowledge Graph Requirements and Technology Selection
[**05:16**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=316s) - Product requirements for knowledge graph system
[**05:23**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=323s) - Multi-model flexibility (key-value pairs, JSON, relationships)
[**05:38**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=338s) - Performance requirements for instant access
[**05:58**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=358s) - Graph RAG and vector indexing for semantic search
[**06:29**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=389s) - Technology evaluation: Neo4j vs ArangoDB vs others
[**06:57**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=417s) - Selected ArangoDB for historical and use case reasons

**Key Points:**
- **Requirements:** Multi-model flexibility, high performance, operational flexibility, vector indexing capability, ecosystem stability, multi-vendor support
- Evaluated Neo4j (market leader) and various open-source tools
- Chose ArangoDB due to existing security use cases (recommendation systems)
- Still exploring Neo4j for future use cases in the project

### 5. Knowledge Graph Implementation with OpenConfig Schema
[**07:24**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=444s) - Overall solution architecture diagram
[**07:37**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=457s) - Ingestion service performing ETL transformations
[**07:44**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=464s) - OpenConfig schema as unified networking standard
[**07:54**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=474s) - LLMs understand OpenConfig well due to internet documentation
[**08:17**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=497s) - Layered graph structure for efficient queries

**Key Points:**
- Production data sources: controllers, Splunk (SIEM), traffic telemetry
- Ingestion service transforms all data into OpenConfig schema
- OpenConfig chosen because it's networking-focused with extensive online documentation that LLMs can understand
- Graph structured in layers: allows agents to query only necessary layers (e.g., raw config for drift detection, multiple layers for reachability tests)
- Layered approach optimizes agent performance by reducing unnecessary data access

### 6. Open Standards and the agency.org Collective
[**09:32**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=572s) - Building on open standards for interoperability
[**09:47**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=587s) - agency.org collective and partner ecosystem
[**10:12**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=612s) - Framework components: identity, schema, directory, composition, observability
[**10:30**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=630s) - Resources: agency.org, GitHub repo, documentation, sample applications
[**10:56**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=656s) - Integration with MCP, A2A, and other protocols

**Key Points:**
- **Vision:** Enable agents worldwide to communicate without heavy integration work
- **Partners:** Outshift (Cisco), LangChain, Galileo, and other collective members
- **Framework includes:** Agent identity, schema for defining skills/capabilities, agent directory, semantic/synthetic composition, observability
- **Resources available:** agency.org website, GitHub repository, documentation, sample applications
- Integrates with Model Context Protocol (MCP), Agent-to-Agent (A2A), and other emerging protocols
- Goal: open system accessible to everyone, not bespoke/proprietary

### 7. Multi-Agent System Implementation
[**11:17**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=677s) - Five specialized agents in the application
[**11:25**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=685s) - Assistant agent as orchestrator/planner
[**11:32**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=692s) - React reasoning loops for specialized agents
[**11:36**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=696s) - Query agent for knowledge graph interaction
[**11:47**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=707s) - Fine-tuning the query agent for better performance
[**12:05**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=725s) - Fine-tuning results: reduced tokens and faster response times

**Key Points:**
- **Five agents total:**
  1. Assistant agent (orchestrator/planner)
  2. Impact assessment agent
  3. Testing agent
  4. Reasoning agent
  5. Query agent (knowledge graph specialist)
- Most agents use React (Reasoning and Acting) loops
- **Query agent specialization:** Direct interaction with knowledge graph
- Initially tried RAG approach but switched to fine-tuning for better results
- Fine-tuning process used schema information and example queries
- **Benefits of fine-tuning:** Dramatically reduced token consumption and query response time

### 8. Live Demo: Firewall Change Management Workflow
[**12:33**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=753s) - Demo introduction
[**12:51**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=771s) - Scenario: adding firewall rule for new server
[**13:03**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=783s) - Starting from ServiceNow ITSM ticket
[**13:22**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=802s) - Agents ingest and synthesize ticket information
[**13:42**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=822s) - Impact assessment creation and attachment to ticket

**Key Points:**
- **Scenario:** Network engineer needs to modify firewall rule to accommodate new server
- Workflow starts with ServiceNow ticket submission
- System UI shows natural language ticket ingestion
- Agents synthesize and summarize information automatically
- Impact assessment analyzes potential implications beyond immediate target area
- Results automatically attached back to ITSM ticket for approval board review

### 9. Test Plan Generation and Execution
[**14:15**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=855s) - Test plan generation as critical pain point
[**14:23**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=863s) - Agents reason through internet knowledge to create comprehensive test plans
[**14:43**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=883s) - Generated test cases with expected results
[**15:15**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=915s) - Configuration file from GitHub repo
[**15:42**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=942s) - Test execution begins

**Key Points:**
- **Major customer pain point:** Running tests but missing the RIGHT tests
- Agents analyze test plan knowledge from internet sources
- Test plan based on intent collected from ServiceNow ticket
- Lists all necessary tests with expected outcomes to prevent production failures
- Configuration changes stored in GitHub repository
- Pull request link added to ticket for executor agent to use

### 10. Digital Twin Test Execution
[**16:06**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=966s) - Executor agent workflow
[**16:15**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=975s) - Snapshot of current network state from knowledge graph
[**16:28**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=988s) - Computing snapshot + configuration change
[**16:36**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=996s) - Digital twin definition: knowledge graph + testing tools
[**16:44**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=1004s) - Testing tools examples: Batfish, Routenet
[**16:57**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=1017s) - Test report generation with results and recommendations

**Key Points:**
- **Executor agent process:**
  1. Reviews test cases
  2. Takes snapshot of network from knowledge graph
  3. Pulls configuration change from GitHub
  4. Computes combined state
  5. Runs all tests sequentially
- **Digital twin = Knowledge graph + Testing tools** (Batfish, Routenet, etc.)
- Tests run in safe digital twin environment, not production
- Comprehensive report generated: passed tests, failed tests, recommendations for failures
- Report attached to ITSM ticket for review

### 11. Evaluation Metrics and Lessons Learned
[**17:48**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=1068s) - Importance of evaluation for customer value
[**18:06**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=1086s) - Measuring agents, knowledge graph, and digital twin
[**18:09**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=1089s) - Focus on extrinsic metrics tied to use case
[**18:21**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=1101s) - MVP status: still learning
[**18:28**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=1108s) - Key building blocks: knowledge graph and open agent framework
[**18:33**](https://www.youtube.com/watch?v=m0dxZ-NDKHo&t=1113s) - Critical for scalable customer systems

**Key Points:**
- Evaluation critical to demonstrate customer value
- Measuring three components: agents, knowledge graph, digital twin
- **Extrinsic metrics preferred** over intrinsic ones—mapped directly to customer use cases
- Current status: MVP in production, continuous learning phase
- **Two critical building blocks identified:**
  1. Network knowledge graph as digital twin
  2. Open framework for agent development (agency.org)
- These foundations enable scalable, production-ready systems for enterprise customers

---

## Additional Resources

- **agency.org:** Open collective for agent interoperability standards
- **GitHub repository:** Available for contributions and implementation reference
- **OpenConfig schema:** Industry-standard networking configuration framework
- **ArangoDB:** Multi-model database chosen for knowledge graph implementation
- **Testing tools:** Batfish, Routenet for network verification

---

**Last Updated:** 2026-01-01
