# A2A & MCP Workshop: Automating Business Processes with LLMs — Damien Murphy, Bench

**Video URL:** https://www.youtube.com/watch?v=wXVvfFMTyzY

---

## Executive Summary

This workshop by Damien Murphy from Bench Computing provides a hands-on introduction to building multi-agent systems using A2A (Agent-to-Agent) protocol and MCP (Model Context Protocol). The session demonstrates how to create autonomous agents that communicate over the web, integrate with various tools through MCP servers, and automate complex business workflows. Key topics include practical implementation of A2A/MCP integration, prompt caching strategies for cost optimization, context management techniques, and real-world examples of agent orchestration for tasks like GitHub issue triage and Slack notifications.

---

## Main Topics

### [Introduction and Speaker Background](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=17s)
- Damien Murphy introduces himself: 15 years as full-stack developer, 5 years in solutions engineering
- Currently at Bench Computing (pre-revenue startup backed by Sutter Hill Ventures)
- Building an autonomous AI agent platform focused on sub-parallel task automation
- Workshop focus: building multi-agent systems with A2A and MCP

### [Workshop Overview and Objectives](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=107s)
- Building a multi-agent system using A2A agents
- Integrating agents with MCP (Model Context Protocol)
- Making agents work together with web hooks
- Covering when to use A2A vs MCP
- Discussion of prompt caching and context management strategies

### [Understanding A2A (Agent-to-Agent Protocol)](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=165s)
- A2A protocol released by Google for agent communication over the web
- Purpose: enables remote agent discovery and communication
- Key benefit: service discoverability for agents you have no prior knowledge of
- Difference from MCP: A2A is for remote agents, MCP is for local tool/resource access
- Use case: isolating context for specialized agents to improve speed and reduce context size

### [MCP (Model Context Protocol) Overview](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=225s)
- Coined as "USB-C for AI agents" - standardized interface
- Approximately 10,000 MCP tools available (7,000+ from Zapier MCP alone)
- Zapier integration enables connection to disparate systems
- MCP provides standardized way for agents to access tools and resources
- Critical for building scalable agent systems

### [A2A vs MCP: When to Use Each](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=361s)
- MCP: For local tool/resource access within your own agent system
- A2A: For remote agent discovery and communication
- A2A hides complexity from calling agents
- Service discoverability is key tenant of A2A
- Can combine both: MCP for tools, A2A for inter-agent communication

### [Setup and Prerequisites](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=724s)
- Clone repository and run npm install
- Need MCP server URL (Zapier MCP server recommended)
- Requires API keys for Zapier and AI models
- Setup instructions included in slide deck
- Free Zapier account available for testing

### [Agent Discovery and Orchestration](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=963s)
- Host agent handles agent discovery and delegation
- Sub-agents specialize in specific tasks
- Orchestration layer brings everything together
- Example: delegating tasks to Slack, GitHub, and JIRA agents

### [Real-World Example: GitHub Issue Triage](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=1082s)
- Demo of multi-agent system for bug triage
- AI misclassified bug severity during trial
- Engineers need to investigate and fix issues
- Shows practical business process automation
- Demonstrates agent coordination across platforms

### [Architecture Discussion: Host and Sub-Agents](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=1687s)
- All agents (Slack, GitHub, JIRA) are A2A agents
- Host agent orchestrates and delegates tasks
- Sub-agents handle specialized functionality
- Question about sub-agent to sub-agent communication
- Architecture pattern for complex workflows

### [Security and Authentication](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=1808s)
- A2A spec includes authentication mechanisms
- Managing security across different vendor endpoints
- Need agreements with service providers for compliance (HIPAA, financial data)
- Security posture depends on implementation and service providers
- Important for enterprise deployments

### [Context Management and Token Optimization](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=2044s)
- Tool definitions can consume massive tokens (10,000+ for Slack, 11,000+ for Asana)
- MCP servers can be verbose with tool definitions
- Need strategies to manage context size
- A2A helps by isolating context in sub-agents
- Critical for scaling multi-agent systems

### [Prompt Caching Strategies](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=2167s)
- Ran simulations to find optimal caching strategy
- Based on actual usage data patterns
- Tested linear growth, exponential growth, and fixed strategies
- Limited public information on best practices
- Important for cost optimization at scale

### [Benefits of Lean Context in Sub-Agents](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=2283s)
- Sub-agents maintain isolated context
- Allows for super-focused agent functionality
- Reduces token usage and improves performance
- Better than monolithic agents with all tools
- Scales better for complex workflows

### [System Architecture Deep Dive](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=2403s)
- Spawns new instance for each communication
- System prompt loading and configuration
- Demonstration of actual code implementation
- Shows how agents are initialized and configured
- Practical walkthrough of architecture

### [Salesforce Integration Example](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=2525s)
- Example of how big context can get with enterprise APIs
- Salesforce has extensive API surface area
- In many cases, only subset of APIs needed
- Types and packages not yet exposed in MCP
- Importance of selective tool exposure

### [Webhook Server Implementation](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=2648s)
- Webhook server for triggering agents
- Code walkthrough of webhook setup
- Integration with external systems
- Event-driven architecture pattern
- Enables real-time agent responses

### [Caching Simulation Methodology](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=2763s)
- Limited information available on optimal strategies
- Used linear growth, exponential growth, fixed models
- Simulations based on actual usage patterns
- Data-driven approach to optimization
- Shared findings for community benefit

### [Transport Protocols Discussion](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=2882s)
- Socket.IO for local interactions
- SSE (Server-Sent Events) deprecated in favor of streamable HTTP
- Different protocols for different use cases
- Evolution of MCP transport mechanisms
- Important for implementation decisions

### [Compliance and Data Security](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=3004s)
- HIPAA compliance considerations
- Financial data handling
- Agreements with service providers required
- Security depends on provider capabilities
- Critical for regulated industries

### [Orchestrator Design Patterns](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=3124s)
- How much logic should orchestrator handle?
- Interpreting responses from sub-agents
- Decision-making patterns in multi-agent systems
- Host agent vs direct sub-agent communication
- Architectural trade-offs discussed

### [Agent Communication Flow](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=3248s)
- Host agent delegates to specialized agents
- Example: GitHub agent handles repository tasks
- Decision routing through host for coordination
- Prevents direct sub-agent to sub-agent calls
- Maintains clear orchestration hierarchy

### [MCP Server Instructions](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=3362s)
- How to provide instructions to MCP servers
- Body and title formatting
- Zapier recently added mandatory instruction fields
- Improves tool discoverability and usage
- Best practices for tool documentation

### [Model Selection for Different Tasks](https://www.youtube.com/watch?v=wXVvfFMTyzY&t=3484s)
- Gemini Flash for simple tasks like summarization
- Claude Haiku as alternative
- Google leading in price-performance ratio
- Different models for different complexity levels
- Cost optimization through model selection

---

## Key Takeaways

1. **A2A and MCP are complementary**: Use MCP for local tools and A2A for remote agent communication
2. **Context management is critical**: Tool definitions can consume 10,000+ tokens; use sub-agents to isolate context
3. **Prompt caching saves costs**: Implement data-driven caching strategies based on usage patterns
4. **Security requires planning**: Enterprise deployments need proper authentication and service agreements
5. **Architecture matters**: Clear host/sub-agent patterns prevent complexity and improve maintainability
6. **Model selection impacts cost**: Use cheaper models (Gemini Flash, Claude Haiku) for simple tasks
7. **Zapier MCP is powerful**: Provides 7,000+ tool integrations through single MCP server
8. **Lean agents perform better**: Specialized sub-agents with focused context outperform monolithic agents

---

**Workshop Materials**: Repository and code examples provided for hands-on implementation
