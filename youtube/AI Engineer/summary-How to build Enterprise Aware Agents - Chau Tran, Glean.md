# How to build Enterprise Aware Agents - Chau Tran, Glean

**Video URL:** https://www.youtube.com/watch?v=hxFpUcvWPcU

---

## Executive Summary

Chau Tran from Glean presents a practical framework for building enterprise-aware AI agents that understand company-specific workflows and processes. The talk explores the workflows vs. agents debate, proposing that instead of choosing between them, they can work synergistically. Key insights include: agents generate workflows dynamically, workflows can evaluate and train agents, and dynamic prompting through search provides better personalization than fine-tuning alone. The approach enables AI systems to bridge the gap between acceptable and great outputs by incorporating enterprise-specific knowledge and best practices.

---

## Main Topics

### 1. [Workflows vs Agents: The Core Trade-off](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=47s)
**Time:** [00:47](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=47s) - [05:11](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=311s)

**Key Points:**
- **Workflows** = "Toyota of AI systems"
  - LLMs and tools orchestrated through predefined code paths
  - Two representations: imperative code-based or declarative graphs
  - Predictable, lower cost/latency, easier to debug
  - Humans in control - can engineer solutions even with imperfect LLMs
  - Good for automating repetitive tasks and encoding best practices

- **Agents** = "Tesla of AI systems"
  - LLMs dynamically direct their own processes
  - Core loop: receive task → plan → execute → read results → iterate
  - Open-ended, better at unsolved problems
  - AI in control - automatically improves as LLMs get better
  - Higher cost/latency but less logic to maintain
  - Shows "hints of brilliance" but can still "take wrong exit on highway"

- **The Dilemma:** Decision depends highly on current LLM capabilities; what doesn't work in agents now might work in a few months

### 2. [The Synergy: Don't Choose, Use Both](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=316s)
**Time:** [05:16](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=316s) - [09:20](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=560s)

**Key Insight:** An agent taking a task and executing it produces a trace - that trace IS a workflow

**Three Powerful Synergies:**

1. **Workflows as Evaluation for Agents** ([06:18](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=378s))
   - Collect "golden workflows" - known good task→steps mappings
   - Evaluate agents not just on end response, but on whether they followed the right steps
   - Different from end-to-end evaluation

2. **Workflows as Training Data for Agents** ([07:14](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=434s))
   - Best of both worlds approach
   - Agents execute exact workflows from library for known tasks
   - But can also compose different workflows together for new tasks
   - Can extend and improve on what they were taught using internal reasoning

3. **Agents as Workflow Discovery Engine** ([08:51](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=531s))
   - Ship an agent to users
   - When users accomplish new tasks successfully, save those workflows
   - Over time, builds library of company-specific workflows
   - Feeds back into training data to help agents improve

**Additional Use Case:** Agents can generate workflows for workflow-building platforms ([08:07](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=487s))
- User provides natural language description
- Agent implementation figures out needed steps
- User can then edit/refine the generated workflow

### 3. [Training Methods: Fine-tuning vs Dynamic Prompting](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=674s)
**Time:** [11:14](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=674s) - [16:24](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=984s)

#### Fine-tuning (SFT & RLHF)
**Pros:**
- Learns very well with lots of data
- Can generalize across different tasks and combine workflows

**Cons:**
- Creates a fork from frontier LLM - outdated when new models arrive
- Any training data change requires retraining (new tools, changed business processes)
- Not flexible for personalization (different teams may need different workflows for same task)
- Analogy: Like building custom hardware - optimized but costly to change

#### Dynamic Prompting Through Search ([13:21](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=801s))
**How it works:**
- Build search engine for task→workflow mappings
- At runtime, find most similar tasks in training data
- Feed those workflow examples to LLM as context
- Spectrum from determinism to creativity:
  - No match → AI generates new workflow using creativity
  - High confidence match → LLM follows similar workflow from training data

**Example:** Competitor analysis query ([14:24](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=864s))
- Retrieves: how to analyze each competitor + how to find recent customer calls
- LLM composes: read customer calls + read internal messages + extract competitors + run analysis for each

**Pros:**
- More flexible, better interpretability
- Can inspect exact examples affecting outputs
- Good for customized behaviors and rapidly changing requirements
- Analogy: Like writing software - less optimized but quickly changeable

**When to use each:**
- Fine-tuning: Generalized behaviors, stable labels over time/users
- Dynamic prompting: Customized behaviors, last-mile quality gap, changing requirements

### 4. [Building Workflow Search](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=987s)
**Time:** [16:27](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=987s) - [18:18](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=1098s)

**Two Main Components:**

1. **Textual Similarity** ([16:46](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=1006s))
   - Standard approaches: hybrid search (lexical + vector embeddings), reranking, late interaction
   - Find similar-sounding tasks in training data

2. **Authoritativeness** ([17:35](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=1055s))
   - **Critical for enterprise:** Pure text similarity insufficient
   - Problem: Hundreds/thousands of similar-looking workflows - which is the RIGHT one?
   - Solution: Knowledge graph signals
     - Created by someone you work closely with
     - Has high success rate
     - People posted about it on Slack
   - Recommendation system tricks apply here
   - Hard to encode directly into LLM → requires separate search system

### 5. [Enterprise Awareness Beyond AGI](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=574s)
**Time:** [09:34](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=574s) - [11:03](https://www.youtube.com/watch?v=hxFpUcvWPcU&t=663s)

**Thought Experiment:**
- AGI = super intelligent employee who just joined
- Still needs onboarding, needs to know:
  - How company works
  - Business practices
  - Who to talk to when blocked
  - Nuanced ways of doing things in the enterprise

**Enterprise-Aware AGI:** Fully onboarded, very intelligent, knows the company's ways

**Key Insight:** Gap between acceptable vs. great output
- Example: Competitor analysis
  - Acceptable: Basic Google search and external notes
  - Great: Follows company protocols, addresses metrics executives care about

**Many acceptable ways to achieve a task, but enterprise awareness enables the GREAT way**

---

## Key Takeaways

1. **Don't choose between workflows and agents** - they're synergistic
   - Workflows: deterministic, human in control
   - Agents: open-ended, AI in control
   - Workflows can evaluate/train agents; agents can discover workflows

2. **Training approaches serve different needs:**
   - Fine-tuning: Generalized, stable behaviors (custom hardware)
   - Dynamic prompting: Personalized, rapidly changing needs (software)

3. **Enterprise awareness requires two components:**
   - Textual similarity (standard search techniques)
   - Authoritativeness (knowledge graph signals for the RIGHT workflow)

4. **Even with AGI, enterprise-specific knowledge matters**
   - Bridges gap from acceptable to great outputs
   - Encodes company-specific protocols, processes, and preferences

5. **Practical implementation pattern:**
   - Ship agents to discover workflows
   - Build library of golden workflows
   - Use search to dynamically prompt with relevant examples
   - Continuously improve as users accomplish new tasks

---

**Speaker:** Chau Tran, Glean
**Event:** AI Engineer Conference
**Duration:** ~19 minutes
