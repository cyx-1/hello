# 3 ingredients for building reliable enterprise agents - Harrison Chase, LangChain/LangGraph

**Video URL:** https://www.youtube.com/watch?v=kTnfJszFxCg

---

## Executive Summary

Harrison Chase, founder of LangChain, presents a framework for building successful enterprise agents based on three core ingredients: maximizing value when right, increasing probability of success, and minimizing cost when wrong. He argues that the future involves many agents working in the background (ambient agents) rather than just chat-based co-pilots. Success depends on choosing high-value verticals (legal, finance), making agents deterministic for reliability, providing observability to reduce perceived risk, implementing human-in-the-loop patterns, and making actions reversible. The talk emphasizes a progression from synchronous chat agents to asynchronous "ambient agents" triggered by events, with real-world examples like deep research, code generation, and email automation.

---

## Main Topics

### [Introduction and Framework](https://www.youtube.com/watch?v=kTnfJszFxCg&t=17s)
Harrison introduces the vision of many agents working across enterprises and presents a first-principles framework for agent success. The formula for adoption is: (Probability of Success × Value When Right) - (Probability of Failure × Cost When Wrong) > Cost of Running Agent.

**Key Points:**
- Future vision: Multiple specialized agents working autonomously, with humans acting as managers/supervisors
- Credits conversation with Assaf (head of AI at Monday, creator of GPT Researcher) for inspiring these ideas
- Three fundamental ingredients determine enterprise agent success

### [Ingredient 1: Maximizing Value When Right](https://www.youtube.com/watch?v=kTnfJszFxCg&t=311s)
The first ingredient focuses on choosing high-value problems and increasing the amount of work agents perform.

**Key Points:**
- **High-value verticals:** Harvey (legal), finance research/summarization - people pay substantial money for these services
- **Shift from quick responses to deep work:** Moving from 5-second RAG responses to extended deep research sessions
- **Ambient coding agents:** From inline autocomplete to agents running for hours in the background (7+ examples emerged in 3 weeks)
- **Key insight:** Agents providing more value means reshifting UI/UX to support longer-term, autonomous work patterns rather than co-pilot interactions

### [Ingredient 2: Increasing Probability of Success](https://www.youtube.com/watch?v=kTnfJszFxCg&t=311s)
Making agents more reliable and reducing uncertainty about their performance.

**Key Points:**
- **Challenge:** Easy to build a prototype that works once (good for Twitter demos), hard to make it work reliably in production
- **Solution 1 - Deterministic workflows:** Make more of the agent deterministic rather than relying solely on prompting
  - Anthropic's "workflows vs agents" distinction - Chase argues it's "workflows AND agents"
  - LangGraph framework allows positioning anywhere on the spectrum from fully deterministic to fully agentic
  - Example: If you want step A always followed by step B, code it deterministically (100% reliability) rather than prompting (90% reliability)
- **Solution 2 - Observability & Evals:** Reduce perceived uncertainty through transparency
  - LangSmith provides observability into every agent step
  - Originally built for developers, but proves crucial for communicating with stakeholders
  - Success story: User showed LangSmith to review panel, finished meeting early (rare), got approval
  - Helps communicate performance patterns, where agents succeed/fail

### [Ingredient 3: Minimizing Cost When Wrong](https://www.youtube.com/watch?v=kTnfJszFxCg&t=596s)
Addressing the outsized perception of risk in enterprise environments.

**Key Points:**
- **Problem:** Stories of "agents going wild" create fear of brand damage or financial loss
- **Solution 1 - Make changes reversible:**
  - Code example: Replit Agent creates a new commit for every file change, enabling easy rollback
  - Git provides natural reversibility - part of why coding is an early success area
- **Solution 2 - Human-in-the-loop:**
  - Open PRs instead of merging directly to main
  - Changes cost calculation in people's minds: now reversible AND prevented by human approval
  - Multiple HITL patterns: approve/reject, edit tool calls, agent asks questions, time travel (rewind to step 10 of 100 and resume differently)
- **Important distinction:** Ambient ≠ fully autonomous - human-in-the-loop patterns remain critical even in background agents

### [Concrete Examples: Deep Research and Code](https://www.youtube.com/watch?v=kTnfJszFxCg&t=725s)
Real-world applications demonstrating all three ingredients.

**Key Points:**
- **Deep Research:**
  - Human-in-the-loop at start: back-and-forth questions to calibrate what to research
  - Increases value (better aligned results) AND reduces risk (human validates direction)
  - Doesn't auto-publish - produces report you decide what to do with
- **Claude Code:**
  - Asks clarifying questions before acting
  - Keeps human in loop while ensuring better results
  - Works on separate branches, opens PRs rather than pushing to master
- Both follow the "first draft" UX pattern - agents do substantial work but humans review before final action

### [Scaling Success: Ambient Agents](https://www.youtube.com/watch?v=kTnfJszFxCg&t=795s)
The progression toward event-driven, background agents that multiply value.

**Key Points:**
- **Definition:** Agents triggered by events rather than human chat, running in the background
- **Why powerful:** Scales positive expected value beyond 1:1 human-agent ratio
  - Can have hundreds running concurrently vs. 1-2 chat boxes
- **Key differences from chat agents:**
  - Triggered by events (enable one-to-many relationships)
  - Relaxed latency requirements (can run for hours)
  - Enables complex operations and greater value delivery
- **Progression spectrum:**
  - Past: Synchronous chat agents
  - Present: **Sync-to-async agents** (human triggers, agent works asynchronously) - examples: Deep Research, Claude Code, Factory
  - Future: Fully ambient agents (event-triggered, human-on-the-loop)
- **UX patterns for ambient agents:**
  - **Agent inbox:** Surface all actions needing approval in one place
  - Approve/reject/provide feedback workflows
  - Time travel: Rewind and resume with different instructions

### [Email Agent Example](https://www.youtube.com/watch?v=kTnfJszFxCg&t=1065s)
Harrison's concrete implementation of an ambient agent.

**Key Points:**
- Listens to incoming emails (event-driven triggers)
- Can run on unlimited concurrent emails (scalability)
- User approves outgoing emails and calendar events before they're sent (HITL)
- Open source implementation available via QR code in presentation
- Used internally at LangChain to test ambient agent patterns

### [Q&A: Why Code Agents Get More Funding](https://www.youtube.com/watch?v=kTnfJszFxCg&t=1128s)
Discussion of why coding agents see more success and investment.

**Key Points:**
- **Verifiable domains:** Code and math are verifiable (code compiles/runs, math has correct answers)
  - Enables bootstrapping large amounts of training data
  - Models are inherently better at these domains
- **Essay writing is non-verifiable:** No clear "correct" answer, harder to train on
- **First draft UX is generalizable:**
  - Beyond code: legal documents, writing, research - anything with draft concepts
  - Sweet spot: Agent does substantial work, human reviews at key points
  - Avoid: Human-in-the-loop at every tiny step (provides no value)
- **Key mental model:** Find UX patterns where agents do significant work while keeping humans in the loop at strategic points

---

## Key Takeaways

1. **Success formula:** Enterprise agent adoption = (P(success) × Value) - (P(failure) × Cost) > Running Cost
2. **Choose wisely:** Focus on high-value verticals (legal, finance) and design for substantial work (hours, not seconds)
3. **Deterministic core:** Make critical paths deterministic (workflows) while keeping agentic exploration where beneficial
4. **Transparency matters:** Observability reduces perceived risk as much as actual performance improvements
5. **Reversibility is critical:** Enable easy rollback (commits, drafts) and human approval before final actions
6. **The future is ambient:** Event-driven background agents will scale value beyond 1:1 human-agent ratios
7. **Sync-to-async is the bridge:** Current successful agents (Deep Research, Claude Code) represent intermediate stage between chat and fully autonomous
8. **First drafts unlock value:** The draft/review pattern works across domains and balances autonomy with control
9. **Human-in-the-loop ≠ blocking:** Strategic placement at calibration (start) and approval (end) points, not every step
10. **Verifiable domains win early:** Code and math succeed because models train better on verifiable tasks, but patterns generalize

---

**Last Updated:** 2026-01-03
