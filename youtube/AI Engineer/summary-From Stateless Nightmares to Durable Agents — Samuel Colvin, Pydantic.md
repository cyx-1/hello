# From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic

**Video URL:** https://www.youtube.com/watch?v=flf_IKnFYnE

---

## Executive Summary

Samuel Colvin from Pydantic demonstrates how to build durable AI agents using Pydantic AI, Temporal, and Logfire. The talk addresses a critical challenge in AI agent development: when long-running workflows fail or get interrupted, developers typically lose all progress and must restart from scratch. By integrating Temporal's durable execution framework with Pydantic AI, agents can automatically resume from their last checkpoint without re-running expensive LLM calls. Colvin illustrates this with two examples: a 20-questions game between agents and a practical deep research system that performs parallel web searches and analysis. The demo shows how Temporal records all IO operations (activities) and can replay workflows deterministically, making agent systems resilient to failures while maintaining simple, imperative Python code.

---

## Main Topics

### [Introduction and Problem Statement](https://www.youtube.com/watch?v=flf_IKnFYnE&t=3s)
**Timestamp:** [00:03](https://www.youtube.com/watch?v=flf_IKnFYnE&t=3s)

- Introduction to Pydantic AI, Temporal, and Pydantic Logfire integration
- Pydantic AI supports Temporal and Devo as durable execution frameworks
- More durable execution backends being added via community pull requests
- Temporal is the leading incumbent in the durable execution space

**Key Points:**
- Simple LLM queries work fine without durable execution
- Problem arises with longer workflows where you've invested compute time and don't want to lose progress
- OpenAI uses Temporal for their deep research product

### [The 20 Questions Demo - Basic Example](https://www.youtube.com/watch?v=flf_IKnFYnE&t=68s)
**Timestamp:** [01:08](https://www.youtube.com/watch?v=flf_IKnFYnE&t=68s)

- Two agents play 20 questions (questioner vs answerer)
- Answer agent uses Claude Haiku 3.5 with a secret object (potato)
- Questioner agent asks questions via tool calls
- Responses are more nuanced than yes/no: "yes, kind of, not really, no, completely wrong"

**Key Points:**
- Sometimes takes 50+ steps to get the right answer
- LLMs can get confused even on simple tasks
- If the process dies mid-execution, all progress is lost
- This toy example is directly equivalent to deep research workflows

### [The Problem Without Durable Execution](https://www.youtube.com/watch?v=flf_IKnFYnE&t=180s)
**Timestamp:** [03:00](https://www.youtube.com/watch?v=flf_IKnFYnE&t=180s)

- If the system crashes due to unreliable endpoints or Kubernetes scaling, execution must restart from scratch
- As tasks get longer, restarting becomes increasingly problematic
- The 20 questions game is analogous to deep research: asking questions to find answers through iterative queries

### [Adding Temporal - Workflows and Activities](https://www.youtube.com/watch?v=flf_IKnFYnE&t=247s)
**Timestamp:** [04:07](https://www.youtube.com/watch?v=flf_IKnFYnE&t=247s)

- Wrap agents in `temporal_agent` wrapper
- Same code structure, just adding temporal wrappers
- Temporal has two core concepts: workflows and activities

**Key Points:**
- Workflows must be entirely deterministic (no IO, no random calls)
- Activities handle non-deterministic operations like IO
- Temporal records every activity's inputs and outputs
- Can replay workflows by plugging in cached activity results

### [Temporal Workflow Architecture](https://www.youtube.com/watch?v=flf_IKnFYnE&t=296s)
**Timestamp:** [04:56](https://www.youtube.com/watch?v=flf_IKnFYnE&t=296s)

- Workflows are deterministic, activities handle IO
- Temporal agent automatically converts LLM calls and tool calls into activities
- OpenAI claims Temporal support but doesn't support tool calls as activities (major limitation)
- Pydantic AI properly handles tool calls as activities

**Key Points:**
- Critical difference: Pydantic AI makes tool calls durable activities
- Without durable tool calls, the system is like a "chocolate teapot" (useless)

### [Demo: Handling Failures with Temporal](https://www.youtube.com/watch?v=flf_IKnFYnE&t=423s)
**Timestamp:** [07:03](https://www.youtube.com/watch?v=flf_IKnFYnE&t=423s)

- Added 20% failure rate to simulate unreliable systems
- Temporal automatically handles retries and continues execution
- Process can be killed mid-execution (simulating Kubernetes restart)

**Key Points:**
- Temporal handles runtime errors gracefully with automatic retries
- Retry logic is built-in without manual implementation

### [Resuming from Checkpoints](https://www.youtube.com/watch?v=flf_IKnFYnE&t=520s)
**Timestamp:** [08:40](https://www.youtube.com/watch?v=flf_IKnFYnE&t=520s)

- After killing the process, can resume with the same workflow ID
- Instantly jumps to question 6 (where it left off)
- No resume code needed in the agent itself

**Key Points:**
- Temporal automatically manages state persistence
- Resume happens transparently without application code changes

### [Logfire Integration - Observability](https://www.youtube.com/watch?v=flf_IKnFYnE&t=526s)
**Timestamp:** [08:46](https://www.youtube.com/watch?v=flf_IKnFYnE&t=526s)

- Logfire provides full visibility into workflow execution
- Shows all LLM calls, activities, and their durations
- Can inspect cached vs actual LLM calls

**Key Points:**
- Cached activities respond in ~5 milliseconds vs normal LLM latency
- Temporal returns cached results instead of re-running inference
- Can inspect workflow state and execution history

### [Fast-Forward Through Cached Activities](https://www.youtube.com/watch?v=flf_IKnFYnE&t=601s)
**Timestamp:** [10:01](https://www.youtube.com/watch?v=flf_IKnFYnE&t=601s)

- First batch of LLM calls responded in ~5ms (cached by Temporal)
- System "zooms forward" to where execution stopped
- Like having caching on every IO call without writing cache code

**Key Points:**
- Workflow code executes quickly (it's just procedural Python)
- Activities return instantly from cache until reaching new execution
- Dramatically reduces time and cost to resume

### [Pydantic Evals - Model Comparison](https://www.youtube.com/watch?v=flf_IKnFYnE&t=667s)
**Timestamp:** [11:07](https://www.youtube.com/watch?v=flf_IKnFYnE&t=667s)

- Ran evals comparing GPT-4.1, Gemini, and Claude Sonnet 4.5 on 20 questions
- Metrics: assertions passed/failed, average cost, question count

**Key Points:**
- Gemini was way cheaper and faster
- However, Gemini was faster because it invented wrong answers
- Demonstrates the importance of proper evaluation beyond speed/cost
- Not all metrics are representative of actual quality

### [Evolution of AI Agents](https://www.youtube.com/watch?v=flf_IKnFYnE&t=793s)
**Timestamp:** [13:13](https://www.youtube.com/watch?v=flf_IKnFYnE&t=793s)

- Three definitions of "agent":
  1. AI definition: LLMs calling tools in a loop
  2. Tech definition: microservice
  3. Business definition: something that can replace a human

**Key Points:**
- Beginning of 2024: one AI agent per microservice
- Evolved view: agents are the quantum of development - micro-tasks that compose into larger systems
- Deep research agents are composed of multiple smaller agents

### [Deep Research Implementation](https://www.youtube.com/watch?v=flf_IKnFYnE&t=767s)
**Timestamp:** [12:47](https://www.youtube.com/watch?v=flf_IKnFYnE&t=767s)

- Three-agent system for deep research:
  1. Plan agent: Creates research plan with executive summary and web search steps (max 5)
  2. Search agent: Executes searches in parallel using Gemini Flash
  3. Analysis agent: Synthesizes results using Claude Sonnet 4.5

**Key Points:**
- Plan defined as Pydantic model with structured data extraction
- Maximum 5 web searches to keep execution time reasonable
- Analysis instructions guide final synthesis

### [Deep Research Architecture - Agent Composition](https://www.youtube.com/watch?v=flf_IKnFYnE&t=897s)
**Timestamp:** [14:57](https://www.youtube.com/watch?v=flf_IKnFYnE&t=897s)

- Code is remarkably concise (~20 lines for core workflow)
- Run plan agent to get research plan
- Run all search agents in parallel using Python task groups
- Combine results as XML for analysis agent
- Run analysis agent with combined context

**Key Points:**
- Different models for different tasks: Gemini Flash for search, Claude for analysis
- Doesn't require a graph framework - simple imperative code
- Durable execution is better than snapshotting for granular state management

### [Deep Research Demo - Hedge Funds Query](https://www.youtube.com/watch?v=flf_IKnFYnE&t=929s)
**Timestamp:** [15:29](https://www.youtube.com/watch?v=flf_IKnFYnE&t=929s)

- Query: "Find me a list of hedge funds that write Python in London"
- Real use case for Pydantic sales
- Shows execution in Logfire with full observability

**Key Points:**
- Plan step: 9 seconds
- Search steps run in parallel
- Can inspect individual searches, queries, and results
- Total cost tracked: 8 cents for the run

### [Temporal Deep Research with Durability](https://www.youtube.com/watch?v=flf_IKnFYnE&t=1020s)
**Timestamp:** [17:00](https://www.youtube.com/watch?v=flf_IKnFYnE&t=1020s)

- Second version uses Temporal for durable execution
- Switched to OpenAI due to Vertex SDK bug with Temporal
- Using Tavily for web search instead of built-in search
- Otherwise identical code structure

**Key Points:**
- Vertex SDK currently has compatibility issues with Temporal
- Samuel plans to escalate to DeepMind to fix
- Code portability: easy to swap models and tools

### [Temporal Workflow Code](https://www.youtube.com/watch?v=flf_IKnFYnE&t=1054s)
**Timestamp:** [17:34](https://www.youtube.com/watch?v=flf_IKnFYnE&t=1054s)

- Wrap agents in `temporal_agent`
- Analysis agent configured with longer timeout (1 hour vs default)
- Workflow code looks identical to non-temporal version

**Key Points:**
- Can use Python task groups for parallelism (or asyncio.gather)
- All standard Python async patterns work
- Could add `sleep(7 days)` and Temporal would handle pausing/resuming
- No infrastructure code needed for complex orchestration

### [Durable Deep Research Demo](https://www.youtube.com/watch?v=flf_IKnFYnE&t=1122s)
**Timestamp:** [18:42](https://www.youtube.com/watch?v=flf_IKnFYnE&t=1122s)

- Query: "What's the best Python agent framework for durable execution and type safety?"
- Demonstrates killing process mid-execution and resuming

**Key Points:**
- Process killed after searches complete
- On resume: plan took 24ms, searches instant (cached)
- Only analysis step runs again (hadn't completed before)
- Activities must rerun from scratch, but workflow state preserved

### [Results - Pydantic AI Wins!](https://www.youtube.com/watch?v=flf_IKnFYnE&t=1189s)
**Timestamp:** [19:49](https://www.youtube.com/watch?v=flf_IKnFYnE&t=1189s)

- Primary recommendation: Pydantic AI with Temporal
- Comprehensive report with trade-offs of other frameworks
- Executive summary with links included

**Key Points:**
- Mentioned alternatives: LangGraph (if you love snapshotting or type-unsafe code), Temporal alone
- Quality on par with commercial deep research systems
- UI work needed for polished interface

### [Pydantic AI Gateway Announcement](https://www.youtube.com/watch?v=flf_IKnFYnE&t=1296s)
**Timestamp:** [21:36](https://www.youtube.com/watch?v=flf_IKnFYnE&t=1296s)

- Announcing Pydantic AI Gateway (coming soon)
- Direct inference purchasing from major models or open-source models
- Enterprise self-hosting with full observability

**Key Points:**
- QR codes shared for early access
- Complements Pydantic AI, Logfire ecosystem
- Targeting enterprise use cases

---

## Key Takeaways

1. **Durable Execution is Critical**: For long-running agent workflows, ability to resume from checkpoints without losing expensive compute is essential

2. **Temporal + Pydantic AI = Powerful Combination**: Temporal's workflow/activity model integrates seamlessly with Pydantic AI's agent framework

3. **Tool Calls Must Be Activities**: Unlike OpenAI's implementation, Pydantic AI properly makes tool calls durable activities

4. **Agent Composition**: Modern AI systems compose multiple specialized agents (plan, search, analyze) rather than single monolithic agents

5. **Observability Matters**: Logfire integration provides crucial visibility into agent execution, costs, and performance

6. **Model Selection by Task**: Use faster/cheaper models (Gemini Flash) for simple tasks, premium models (Claude) for complex analysis

7. **Simple Code, Complex Capabilities**: Durable execution doesn't require complex code - standard Python async patterns work

8. **Evaluation is Essential**: Speed and cost metrics can be misleading - need to verify actual output quality

9. **Automatic Retry Logic**: Temporal handles failures and retries without manual implementation

10. **Cost Efficiency**: Resuming workflows skips expensive LLM calls via cached activity results
