# How to Build Planning Agents without losing control - Yogendra Miraje, Factset

**Video URL:** https://www.youtube.com/watch?v=sl3icG-IjHo

---

## Executive Summary

Yogendra Miraje from FactSet presents a comprehensive framework for building agentic workflows in enterprise environments. He distinguishes between workflow agents (predefined workflows run by agents) and agentic workflows (workflows planned and run by agents dynamically). The talk introduces a novel "Blueprint" architecture that provides high-level planning while maintaining control and reliability. Key architectural components include blueprint generators, planners, executors, and joiners built on LangGraph. The presentation emphasizes building tools around existing enterprise microservices, implementing proper evaluations, and using planning by subgoal division as the core design pattern. Miraje demonstrates the concept through a financial research use case for preparing NVIDIA earnings call reports.

---

## Topics and Key Points

### [Introduction and Context](https://www.youtube.com/watch?v=sl3icG-IjHo&t=0s)
**Timestamp:** 00:00 - 01:24

- Speaker introduces himself as Yogi from FactSet, a financial data and software company
- Despite exponential AI intelligence growth, developing AI applications still feels like "driving a monster truck through a crowded mall with tiny joysticks"
- AI applications haven't had their "ChatGPT moment" yet
- Main problem: agents often miss the right context, especially enterprise-specific workflows

### [Key Definitions: LLMs, Agents, and Workflows](https://www.youtube.com/watch?v=sl3icG-IjHo&t=84s)
**Timestamp:** 01:24 - 03:09

- **Augmented LLM**: LLM + tools + memory
- **Workflow**: Augmented LLM on a static and predefined path
- **Agent**: Augmented LLM with high autonomy and feedback loops
- **Workflow Agent**: Predefined workflow run by agent (workflow is in control, static)
- **Agentic Workflow**: Workflow planned and run by agent (agent is in control, dynamic)
- Key distinction: "If you are confused don't worry - in workflow agent, workflow is in control and workflow is static. In agentic workflow, agent is always in control and the workflow is dynamic"
- On the agentic spectrum, agentic workflows have more "agenticness" than workflow agents

### [Why Agentic Workflows Matter for Enterprises](https://www.youtube.com/watch?v=sl3icG-IjHo&t=189s)
**Timestamp:** 03:09 - 04:14

- Beyond control, reliability, and predictability, agentic workflows enable automation at scale
- Most important: enterprises can leverage their existing microservices infrastructure
- Many enterprises have invested years or even decades in these systems
- Concepts are generally applicable beyond just enterprise context

### [Moving from React to Proactive Agents](https://www.youtube.com/watch?v=sl3icG-IjHo&t=254s)
**Timestamp:** 04:14 - 05:18

- Need to move beyond React-based agents to proactive agents
- "Great philosophy for life as well"
- Core requirements for agentic workflows:
  - Tools
  - Memory
  - Reflection
- **Key design pattern**: Planning by subgoal division (also called task decomposition)
- Simply: "Take your goal and break it down into simpler steps"

### [Specific Agentic Architectures and Research](https://www.youtube.com/watch?v=sl3icG-IjHo&t=299s)
**Timestamp:** 04:59 - 06:41

- LangChain has created excellent blogs and code implementations for various agentic architectures
- Each architecture has its own pros and cons
- FactSet adopted the **LLM Compiler architecture** for their problems
- **Architecture components**:
  - Microservices with tools built around them
  - Blueprint generator (high-level plan)
  - Planner (low-level tasks)
  - Executor (executes the plan)
  - Joiner (combines outputs from different tasks)
- Replanning logic decides whether to replan or terminate and respond
- Recursion limits prevent agents from looping infinitely
- On LangGraph, each component (blueprint generator, planner, executor, joiner) is a node

### [Building Tools Around Enterprise Microservices](https://www.youtube.com/watch?v=sl3icG-IjHo&t=401s)
**Timestamp:** 06:41 - 08:02

- This is where you'll spend most of your time
- Relationship between tools and microservices is **N to N** (not one-to-one)
- Design tools so agents understand how to use them
- **Critical point**: "Put yourself into agent's shoes so that agent really understands what tool to use"
- Best practices:
  - Follow standards like MCP (Model Context Protocol)
  - Build MCP tool servers for your tools
  - Provide from agent's perspective:
    - **Tool purpose**: What tools to select
    - **Tool description**: When tools need to be invoked
    - **Input/output contracts**: How to use the tool
  - Add validation checks as "breaks" for your agent

### [Blueprint Architecture Deep Dive](https://www.youtube.com/watch?v=sl3icG-IjHo&t=482s)
**Timestamp:** 08:02 - 09:34

- **Blueprint**: Series of steps for workflow in natural language based on tool capabilities
- Why introduce blueprints?
  - Planners get cognitively overloaded when given too much information
  - Provides high-level task breakdown in natural language
- **Benefits of blueprints**:
  - Achieves finer control over task planning
  - Limits in-context tools for the planner (prevents context window issues and overload)
  - Helps interpret agentic behavior
  - Less intimidating for non-technical stakeholders (natural language)

### [Concrete Example: NVIDIA Earnings Call Preparation](https://www.youtube.com/watch?v=sl3icG-IjHo&t=574s)
**Timestamp:** 09:34 - 10:48

- Use case: Preparing for a company's earnings call (simplified workflow for NVIDIA)
- **Blueprint structure** (tool + task):
  1. Summarizing: Summarize NVIDIA's previous earning call
  2. Retrieval: Gather financial data for NVIDIA
  3. Reasoning: Suggest questions for the earning call
  4. Reporting: Generate comprehensive report from all information
- **Plan structure** (tool + function call):
  - Corresponding function calls with context being fed between tasks
- Results: Before agentic workflows, responses were "vanilla"; after implementation, easily captures workflows and provides structured responses

### [Evaluations (Evals) Framework](https://www.youtube.com/watch?v=sl3icG-IjHo&t=648s)
**Timestamp:** 10:48 - 11:55

- "None of this will really work without writing proper evals"
- Must invest in building and maintaining eval frameworks
- Required eval types:
  - Component evals
  - End-to-end evals
- **Evaluation techniques**:
  - Code-based evals
  - LLM as judge
  - Human in the loop
- **Aspect-based eval examples**:
  - Blueprint quality: Does it resemble golden blueprint? (Use LLM as judge)
  - Tool selection: Are correct tools selected? (Use code-based evals)
  - Plan alignment: Is plan aligned with blueprint? (Use LLM as judge)
  - Report formatting: Best handled by human in the loop
- Write evals for metrics you actually care about

### [When NOT to Use Agentic Workflows](https://www.youtube.com/watch?v=sl3icG-IjHo&t=715s)
**Timestamp:** 11:55 - 12:32

Agentic workflows don't make sense for:
- **Fixed and repetitive tasks**: Use ETL pipelines instead
- **Non-workflow use cases**: If you can't capture the use case in workflows
- **Deterministic outcomes required**: Strict compliance and safety-critical contexts
- **Low latency and cost environments**: Agentic workflows add overhead

### [Key Learnings and Best Practices](https://www.youtube.com/watch?v=sl3icG-IjHo&t=752s)
**Timestamp:** 12:32 - 13:54

- Start with simple blueprints and work your way up
- Build complex RAG systems for blueprints
- Use blueprints to reduce in-context tools and provide high-level plans to planners
- Design tools from the agent's point of view
- Always aim for tool usage simplicity
- Implement safety guardrails
- Prioritize evals, observability, and good software engineering practices
- **Key takeaways**:
  - Agentic workflow is planned and run by agent
  - Agentic workflows bring reliability at scale
  - Planning by subgoal division is the key design pattern
  - Plan and execute is the key agentic architecture
  - Build tools to complement your microservices
  - Always leverage existing microservices in tools
  - Don't shy away from modifying architecture or experimenting with research papers
  - Treat evals like first-class citizens

### [Q&A Session](https://www.youtube.com/watch?v=sl3icG-IjHo&t=842s)
**Timestamp:** 14:02 - 15:50

- **Reference resources**: LangChain has code implementations for research papers on plan-and-execute agents
- **MCP and orchestration**: MCP provides standards across architecture ("build once, use everywhere"). LangGraph is great for orchestration but choice depends on use case
- Multiple frameworks will coexist; optimal choice depends on specific requirements

---

## Key Technical Concepts

**Blueprint Generator → Planner → Executor → Joiner** workflow architecture built on LangGraph

**Planning by Subgoal Division**: Breaking complex goals into simpler, manageable steps

**N-to-N relationship**: Between enterprise microservices and agent tools

**MCP (Model Context Protocol)**: Standard for building tool servers

**Aspect-based Evaluations**: Measuring specific aspects like blueprint quality, tool selection accuracy, plan alignment

---

## Recommended Resources

- LangChain blog posts and code implementations for agentic architectures
- Research papers on plan-and-execute agents
- LLM Compiler architecture

---

**Video Duration:** ~15 minutes
**Speaker:** Yogendra Miraje (Yogi), FactSet
**Event:** AI Engineer conference
