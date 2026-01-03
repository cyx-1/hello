# Agents vs Workflows: Why Not Both — Sam Bhagwat, Mastra.ai

**Video URL:** https://www.youtube.com/watch?v=8SUJEqQNClw

## Executive Summary

Sam Bhagwat, co-founder of Gatsby and author of "Principles of AI Agents," discusses the debate between agents and workflows in AI engineering. He critiques the tendency of major AI companies to prescribe rigid development approaches and argues that developers shouldn't need to learn graph theory to build production applications. Sam advocates for composable primitives that allow developers to combine agents and workflows flexibly, emphasizing that the real power comes from combining these patterns together. He draws parallels from web development history to warn against overly complex APIs and promotes readable, fluent syntax for workflows.

## Main Topics

### [Introduction and Agents vs Workflows Debate](https://www.youtube.com/watch?v=8SUJEqQNClw&t=16s)
- Sam introduces himself as co-founder of Gatsby and author of "Principles of AI Agents"
- References the Twitter debate sparked by OpenAI's paper that criticized workflows
- Anthropic's "Building Effective Agents" blog post (December) provided good examples
- OpenAI's April paper included controversial anti-workflow messaging that "muddied the water"
- Swyx's emergency blog post on Latent Space addressed the controversy

### [Hot Take #1: Don't Be "That Guy"](https://www.youtube.com/watch?v=8SUJEqQNClw&t=133s)
- Critique of OpenAI's prescriptive approach to development
- Historical parallel: Google engineers lecturing web developers on "the right way" to use the platform
- Anti-React coded language from major tech companies in the last decade
- Model providers hold elevated positions in the ecosystem, similar to FANG companies in web development
- Call for better quality of discourse from influential companies

### [Hot Take #2: Graph APIs Considered Harmful](https://www.youtube.com/watch?v=8SUJEqQNClw&t=222s)
- Sam's experience with Gatsby using GraphQL as the default data fetching method
- While some users loved GraphQL, many just wanted a React meta framework
- Flashback to seeing node/edge/graph terminal APIs in frameworks (like LangChain)
- **Core argument:** Developers shouldn't need to learn graph theory to write workflows for production applications
- Team members shouldn't all need to understand graph theory
- Advocates for fluent syntax where control flow is clearly visible from top to bottom

### [Getting Down to Business: Design Patterns](https://www.youtube.com/watch?v=8SUJEqQNClw&t=381s)
- Reference to Christopher Alexander's "A Pattern Language" (late 1970s)
- Alexander was a Berkeley professor who cataloged urban planning and architecture patterns
- Software engineers adopted this approach more than architects themselves
- **Key insight:** The AI community lacks commonly accepted verbiage and glossary for agentic patterns
- Need to develop a shared language for agent and workflow patterns

### [What Are Agents and Workflows?](https://www.youtube.com/watch?v=8SUJEqQNClw&t=486s)
- Credits to Nick and Zach for their Monster X workshop examples
- **Agents:** Like a turn-based game - user takes turn, agent takes turn, back and forth
- Agents can make tool calls during their turns
- **Workflows:** Like a rules engine for your tech tree (Civilization reference)
- Example: Must discover bronze working before researching iron working
- Workflows track dependency chains: can't do step B until step A is complete
- Many workflows are data pipelines: Step A → B → C → D → E

### [Emergent Properties](https://www.youtube.com/watch?v=8SUJEqQNClw&t=538s)
- **Agent properties:** Conversations have threads, memory
- Emerge from thinking about lots and lots of messages
- **Workflow properties:** Branching, parallelism, conditions, loops, suspending, resuming, replaying
- Emerge from thinking about dependencies and execution order
- Workflows becoming more popular in AI engineering due to **non-determinism**
- Tracing and debugging 10x more important in AI engineering than traditional software

### [The Power vs Control Trade-off](https://www.youtube.com/watch?v=8SUJEqQNClw&t=605s)
- Fundamental trade-off: power or control
- You can decide which parts need power vs control
- Strategy: Start with power, add control for anything that goes off the rails
- Emphasizes this is a practical trade-off, not a theoretical absolute

### [Whiteboarding Sessions and Reliability](https://www.youtube.com/watch?v=8SUJEqQNClw&t=630s)
- Example: Feeding giant PDF of medical documentation to diagnose 12 symptoms
- Agent not accurately pulling the right information
- **Key suggestion:** Break one LLM call into 12 LLM calls
- Process: Identify parts performing poorly in reliability
- Add structure to the process to increase reliability
- Encourages explaining architecture to colleagues and diagramming it out
- Often reveals better ways of using primitives together

### [Composition Patterns](https://www.youtube.com/watch?v=8SUJEqQNClw&t=709s)
- Agents have tools; workflows have steps
- **Key insight:** These can compose in multiple ways:
  - An agent can be a step
  - A workflow can be a tool
  - An agent can be a tool
  - A workflow can be a step
- The magic happens when you combine these primitives together

### [Agent Supervisor Model](https://www.youtube.com/watch?v=8SUJEqQNClw&t=732s)
- Agent calling other agents as tools
- Example: Research agent, summary agent, orchestrator agent
- Uses Mastra code examples that are simple enough to fit in slides
- Grockable implementations - can understand the pattern quickly
- Power comes from primitives being simple while combinations are sophisticated

### [Workflows as Tools](https://www.youtube.com/watch?v=8SUJEqQNClw&t=787s)
- Example: Plan location → check weather → plan trip
- Complex workflows passed to an agent to iterate and decide
- Workflows can handle agent handoffs

### [Dynamic Tool Injection](https://www.youtube.com/watch?v=8SUJEqQNClw&t=803s)
- Agents can start failing with double-digit numbers of tools
- Be thoughtful about which tools you give to an agent at a particular time
- Context-aware tool provisioning for specific tasks

### [Nested Workflows and Real Alpha](https://www.youtube.com/watch?v=8SUJEqQNClw&t=824s)
- Workflows can be steps within other workflows
- **Key message:** The real alpha comes from using these patterns together in the right way
- Quote: "Reality has a surprising amount of detail, and so do agentic workflows by the time they enter production"

### [Q&A: Practice Over Theory](https://www.youtube.com/watch?v=8SUJEqQNClw&t=862s)
- Question about agent working great with 20 tools
- **Sam's response:** "We are a community of practice more than a community of theory"
- If your agent works according to your needs, do it
- If it's not theoretically correct, the theory is probably wrong, not the practice
- This is a young field where practice is evolving faster than theory
- How to find Sam: Twitter handle @calcam (CALC like calculator, SAM like his childhood handle)

## Key Takeaways

1. **Avoid Dogmatism:** Don't let framework authors or model providers dictate "the one true way" to build
2. **Readability Matters:** Code should be readable from top to bottom without requiring graph theory knowledge
3. **Composition is Power:** Agents and workflows aren't competing - they're complementary primitives
4. **Practice First:** Build what works, let theory catch up later
5. **Design Patterns Needed:** The field needs a shared vocabulary for agentic patterns (like Christopher Alexander's pattern language)
6. **Add Control Incrementally:** Start with powerful, flexible agents and add workflow controls where reliability issues emerge
7. **Context-Aware Tooling:** Don't overwhelm agents with too many tools; inject them dynamically based on task
