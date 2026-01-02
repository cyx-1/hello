# Code World Model: Building World Models for Computation – Jacob Kahn, FAIR Meta

**Video URL:** https://www.youtube.com/watch?v=sYgE4ppDFOQ

---

## Executive Summary

Jacob Kahn from Meta FAIR presents the Code World Model (CWM), a 32B parameter research model that predicts program execution traces rather than just code syntax. The key innovation is modeling code execution as a world model - predicting future program states based on past observations and actions. This enables the model to "imagine" running code without actually executing it, leading to better reasoning about programs, debugging capabilities, and solving traditionally difficult computer science problems like approximating solutions to the halting problem. CWM uses a bash-oriented agentic approach with scaled-up asynchronous RL post-training to achieve strong performance despite its relatively small size.

---

## Main Topics

### [Introduction and Motivation](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=22s)
**[00:22 - 02:25]**

Jacob introduces CWM with the fundamental question: what does it mean to model code? He argues that traditional token-based autoregressive models only see syntax, but code is really about execution.

**Key Points:**
- CWM aims to build models that reason, plan, and make decisions
- Code provides a constrained sandbox for studying reasoning
- World models predict future observations given past observations and actions
- There's a false dichotomy between world models and LLMs - world models are a problem parameterization, LLMs are a way to use that parameterization
- Instead of just predicting syntax, CWM models execution traces explicitly

### [Execution Tracing Fundamentals](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=145s)
**[02:25 - 03:39]**

The core concept: create natural language systematic descriptions of program execution that neural models can learn to generate autoregressively.

**Key Points:**
- Example: counting 'r's in "strawberry" - trace shows frame separators, local variables, and line-by-line execution
- Can scale beyond functions to repository-level, distributed system-level, or code contest solution traces
- Transition to natural language tracing format
- Each execution line maps to corresponding program line

### [World Model Transition Functions](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=219s)
**[03:39 - 05:27]**

How to parameterize the problem: programs/data represent state, executing the next line is an action, resulting in the next state.

**Key Points:**
- Both program execution and model decisions can be modeled as transition functions
- With world models, you can simulate actions and get imagined feedback without real execution
- This enables far more efficient agentic execution - no need to interact with real world until ready
- LLMs can autoregressively generate token-by-token the state-action-to-state function
- Execution tracing becomes like chain-of-thought for the model

### [Data Collection Strategy](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=327s)
**[05:27 - 06:04]**

CWM uses massive GitHub data at repository and systems level.

**Key Points:**
- Gather GitHub events, PRs, mutations
- Run tests/CI on passing repos
- Generate execution traces from repo-level data
- Goal: execution traces that go beyond simple programs

### [Model Architecture and Training](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=364s)
**[06:04 - 06:52]**

The CWM artifact itself and training pipeline.

**Key Points:**
- 32B parameter dense transformer (research model)
- Long context length for reasoning tasks
- End-to-end training: pre-training (few trillion tokens) → mid-training (domain-specific data) → long context mid-training → fine-tuning (instruction following, reasoning tokens) → joint RL and agentic reasoning

### [Bash-Oriented Agentic Approach](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=412s)
**[06:52 - 08:06]**

CWM's unique interaction model with fewer tools than other models.

**Key Points:**
- Prompt → agent reasoning → action → tool use → environment step
- Get back: tokens, rewards, log probabilities, compiler output
- Very bash-oriented model with fewer tools
- Must learn terminal usage well to solve tasks
- Uses SWE-bench with GitHub issues, repository-level datasets
- Learns bash commands to mutate environment/file state
- Puts model in engineer-like environment for end-to-end learning

### [Bootstrapping with SFT and Rejection Sampling](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=486s)
**[08:06 - 08:43]**

Pre-RL optimization strategies.

**Key Points:**
- Do supervised fine-tuning (SFT) before RL
- Find failure modes and rejection sample
- Feed failed agentic reasoning traces back to model
- Example: thinking traces about instantiation logic, calling grep functions
- Emphasis on fewer tools, larger emphasis on bash

### [Scaling Post-Training with Asynchronous RL](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=523s)
**[08:43 - 10:37]**

The key to CWM's efficiency: highly asynchronous producer-consumer pipeline.

**Key Points:**
- Trend: scale post-training significantly for reasoning improvements
- Small model = opportunity to really scale post-training throughput
- Asynchronous setup: samplers → environment execution → trajectories → trainer (compute gradients/score) → model updates → repeat
- Challenge: producer-consumer pipeline - samplers produce trajectories consumed by trainers
- Solution: queues for models and trajectories, very eager sending
- Stays relatively on-policy despite high asynchronicity
- Achieves very strong throughput

### [Mid-Trajectory Model Updates](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=637s)
**[10:37 - 11:34]**

An aggressive optimization: updating models while they're still generating trajectories.

**Key Points:**
- Can update model mid-trajectory while interacting with environment
- Swap in new checkpoint during execution
- Trajectory becomes slightly off-policy but throughput gains are worth it
- Strong guarantees due to high throughput and data volume
- Very few bottlenecks overall - no waiting

### [Training Scale and Results](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=694s)
**[11:34 - 12:18]**

Post-training outcomes.

**Key Points:**
- Relatively small number of steps at large scale
- ~200+ billion tokens processed
- Produces strong open model despite small size
- Punches above its weight
- Very versatile, uses tools in bash very well

### [Neural Debugger Capability](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=738s)
**[12:18 - 13:57]**

First major application: code completion with execution understanding.

**Key Points:**
- CWM traces code extremely well - can trace functions line-by-line with high accuracy
- Shows values of local variables with precision
- Traditional approach: use natural language to describe what you want
- CWM approach: express semantics in-line with code using question marks/placeholders
- Model understands program shape, simulates execution, fills in the rest
- Can express code structure loosely but precisely
- Helps compose code side-by-side, not just generating it

### [Approximating the Halting Problem](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=837s)
**[14:04 - 15:43]**

An ambitious theoretical application that will "make theoreticians bristle."

**Key Points:**
- Halting problem: can't know if a program will terminate without simulating entire execution (which could be infinite)
- Question: can CWM approximate solutions by understanding high-level patterns?
- By simulating execution, model might understand really high-level patterns
- Use case: debug huge distributed systems or expensive functions without actual execution
- Implicit world model internally simulates what's happening
- Enables reasoning without executing expensive operations
- Can approximate solutions to otherwise impossible problems in computer science

### [Broader Applications](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=901s)
**[15:01 - 15:43]**

Additional use cases beyond debugging.

**Key Points:**
- Debugging distributed systems where execution is very expensive
- Expensive single-machine functions
- Any scenario where implicit world model simulation is cheaper than real execution

### [Conclusion and Resources](https://www.youtube.com/watch?v=sYgE4ppDFOQ&t=943s)
**[15:43 - 16:23]**

Jacob wraps up with a meta-joke and encourages community engagement.

**Key Points:**
- "This talk does halt. This talk does terminate."
- Model available on Hugging Face
- Code on GitHub for inference
- Technical report with excruciating detail on post-training setup, data, and capabilities
- Encourages everyone to build on CWM

---

## Key Takeaways

1. **Paradigm Shift**: CWM moves from modeling code syntax to modeling code execution, treating programs as dynamic systems with state transitions rather than static text

2. **World Models for Code**: By learning to predict execution traces, the model develops an internal simulation capability - it can "imagine" running code without executing it

3. **Bash-First Philosophy**: Unlike tool-heavy agents, CWM emphasizes terminal/bash mastery with fewer specialized tools, creating a more engineer-like interaction model

4. **Asynchronous RL at Scale**: The aggressive asynchronous post-training approach with mid-trajectory updates and queuing enables unprecedented throughput despite the model's relatively small 32B parameter size

5. **Novel Applications**: From neural debugging to approximating solutions to undecidable problems like the halting problem, execution modeling opens new computational capabilities

6. **Open Research**: Meta FAIR is releasing the model, code, and detailed technical reports to encourage community building on these foundations

---

**Last Updated:** January 1, 2026
