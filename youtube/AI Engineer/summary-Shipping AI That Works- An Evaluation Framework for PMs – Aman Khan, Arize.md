# Shipping AI That Works: An Evaluation Framework for PMs – Aman Khan, Arize

**Video URL:** https://www.youtube.com/watch?v=2HNSG990Ew8

---

## Executive Summary

This workshop presents a practical framework for AI Product Managers to ship reliable AI applications through systematic evaluation. Aman Khan from Arize demonstrates how to move from "vibe coding" to "thrive coding" by implementing evaluation (eval) systems for AI agents. The session includes a live demo of building and evaluating a multi-agent trip planner, showing how PMs can use observability tools and LLM-as-a-judge evals to ensure AI applications work reliably in production.

---

## Key Topics with Timestamps

### [Introduction & Context](https://www.youtube.com/watch?v=2HNSG990Ew8&t=16s)
**[00:16 - 05:00]** - Introduction and the evolving role of AI Product Managers

- Aman Khan introduces himself as an AI PM at Arize with background in self-driving cars (Cruz) and ML platforms (Spotify)
- The bar for AI PMs has been raised - expectations from stakeholders and engineers have changed significantly
- The concept of "AIPM" is emerging as a distinct role from traditional PM
- Journey from using AI tools to getting products into production is where most PMs face challenges

**Key quote:** *"I definitely feel like the bar has been raised in terms of what's expected to be delivered, right? Especially if I'm working with an AI engineer on the other end, their expectations of what I come to them with in terms of requirements, in terms of specifying what the agent system needs to look like, it's changed."*

---

### [Why Evaluations Matter](https://www.youtube.com/watch?v=2HNSG990Ew8&t=366s)
**[06:06 - 08:00]** - The reliability problem with LLMs and why evals are critical

- LLMs hallucinate - this is acknowledged by both OpenAI and Anthropic leadership
- Kevin (OpenAI CPO) and Mike (Anthropic CPO) both emphasize the importance of writing evals
- Evals are emerging as a real moat for AI startups
- Lessons from self-driving cars apply to building AI agents today

**Key quotes from industry leaders:**
- *"Their models hallucinate and that it's really important to write eval"*
- *"Evals are emerging as a real moat for AI startup"*

---

### [What is an Evaluation?](https://www.youtube.com/watch?v=2HNSG990Ew8&t=478s)
**[07:58 - 12:00]** - Understanding evals vs traditional software testing

**Key differences between software testing and AI evals:**
- **Software:** Deterministic (1 + 1 = 2)
- **LLM agents:** Non-deterministic (can be convinced 1 + 1 = 3)
- **Unit tests:** Single path, deterministic
- **Agent evals:** Multiple paths, probabilistic
- **Integration tests:** Rely on existing codebase
- **Agent evals:** Rely on your unique data

**The four components of an eval:**
1. **Role** - Tell the agent what task to accomplish
2. **Context** - Provide text/data to evaluate (in curly braces)
3. **Goal** - Define what success looks like (e.g., is text toxic or not toxic)
4. **Label** - Provide terminology and examples (good/bad, toxic/not toxic)

**Important note:** Use text labels (not numeric scores) because LLMs are still bad at numbers. Map labels to scores later if needed.

---

### [From Vibe Coding to Thrive Coding](https://www.youtube.com/watch?v=2HNSG990Ew8&t=725s)
**[12:05 - 13:07]** - Moving beyond prototyping to production-ready AI

- **Vibe coding:** Building AI prototypes quickly, checking if "it looks good to me"
- **Problem:** Can't ship vibe-coded products to production
- **Thrive coding:** Using data to build applications with confidence in the output
- The goal is to maintain the speed of vibe coding while adding reliability through data-driven evaluation

---

### [Live Demo: Building an AI Trip Planner](https://www.youtube.com/watch?v=2HNSG990Ew8&t=807s)
**[13:27 - 18:00]** - Creating a multi-agent system with LangGraph

**Demo setup:**
- Built over a weekend using Cursor AI
- Form-based input (destination, duration, budget, interests, travel style)
- Multi-agent architecture underneath using LangGraph
- Example: Tokyo trip for 7 days, $1,000 budget, food interest, adventurous style

**Why agents vs simple chatbot:**
- Agents can do retrieval, RAG, and tool calling
- Budget constraints require math/accounting
- Interest matching requires sophisticated reasoning
- Provides high level of specificity in outputs

---

### [Observability & Tracing](https://www.youtube.com/watch?v=2HNSG990Ew8&t=1078s)
**[17:58 - 23:00]** - Understanding what's happening under the hood

**Traces and Spans:**
- **Traces:** Input, output, and metadata around each request
- **Spans:** Units of work with time components and types

**Three types of spans:**
1. **Agent** - High-level orchestration
2. **Tool** - Using structured data to perform actions
3. **LLM** - Generating outputs from inputs and context

**Multi-agent architecture visualized:**
- Budget Agent (parallel)
- Local Experiences Agent (parallel)
- Research Agent (parallel)
- All three feed into → Itinerary Agent → Final Output

**PM leverage:** Being able to ask "What does our agent actually look like?" and get a clear visualization provides massive value for team alignment.

---

### [Prompt Playground & Iteration](https://www.youtube.com/watch?v=2HNSG990Ew8&t=1424s)
**[23:44 - 26:08]** - Iterating on prompts without touching code

**Key workflow:**
1. Pull production trace into prompt playground
2. All prompt variables are preserved
3. Iterate on prompt and see immediate results
4. Compare outputs side-by-side

**PM ownership question:** Should writing prompts be the responsibility of engineers or PMs? If PMs are responsible for final product outcomes, they should have control over prompts.

**Prompt Hub:** Save versioned prompts like Git for code, enable team reuse

---

### [Handling Tool Calls](https://www.youtube.com/watch?v=2HNSG990Ew8&t=1584s)
**[26:24 - 27:00]** - Working with agent tools and function calls

- Agents have tools in addition to prompts
- Can pull over specific LLM spans with prompt templates and variables
- May want to select the right tool and ensure agent picks correct tools
- Advanced workflow involves testing tool selection and usage

---

### [Creating Datasets from Production](https://www.youtube.com/watch?v=2HNSG990Ew8&t=1897s)
**[31:37 - 34:00]** - Building eval datasets from real usage

**Process:**
1. Review production traces
2. Add specific spans to datasets (like the itinerary outputs)
3. Create collections of examples for testing
4. Think of datasets as "Google sheets" of test cases

**Platform access:**
- Sign up at arize.com
- Get API keys from account settings
- Need Space ID for instrumentation
- Open source alternative: Phoenix (has similar workflows but not all features)

**Current state of evals:** Many teams still evaluate in spreadsheets with thumbs up/down - this is okay as a starting point, but needs to scale.

---

### [Running Experiments at Scale](https://www.youtube.com/watch?v=2HNSG990Ew8&t=2112s)
**[35:12 - 39:00]** - A/B testing prompts across entire datasets

**Experiment setup:**
- **Prompt A:** Original prompt (no constraints)
- **Prompt B:** Modified prompt with improvements
  - Max 500 characters (vs unlimited)
  - Super friendly tone
  - Ask for email and offer discount

**Running on 12 examples instead of 1:**
- Same workflow as single example, but scaled
- Each example has destination, duration, travel style inputs
- Outputs are itineraries from the agent

**Performance insights discovered:**
- Prompt B runs much faster (~5-8 sec vs ~32 sec average)
- Character limits significantly impact latency
- Can observe real-time execution across dataset

---

### [What to Evaluate](https://www.youtube.com/watch?v=2HNSG990Ew8&t=2385s)
**[39:45 - 41:05]** - Defining your evaluation criteria

**The short answer:** You can evaluate anything you want.

**Common evaluation types:**
- **Tone:** Is the agent answering in a friendly way?
- **Compliance:** Is it offering a discount as requested?
- **Hallucination:** Is it using context correctly?
- **Correctness:** Even with right context, is it giving the right answer?
- **Latency:** How fast is the response?
- **User experience:** Does it meet product requirements?

**Types of evals:**
1. **LLM-as-a-judge:** Most scalable for production (focus of this workshop)
2. **Code-based evals:** Using code to evaluate text
3. **Human annotations:** Manual review and labeling

**Why your own eval system matters:** Industry benchmarks (like MMLU) don't reflect your specific use case. You need evals tailored to your product and data.

---

### [Prompt Chaining (Advanced)](https://www.youtube.com/watch?v=2HNSG990Ew8&t=2266s)
**[37:46 - 38:15]** - Testing complex multi-prompt workflows

**Two recommendations:**
1. **Decompose systems:** Eval parts of your stack that can be decomposed to analyze component changes
2. **Prompt chaining:** Testing Prompt A → Prompt B → Prompt C workflows
   - What happens when you change Prompt A?
   - How does it affect downstream prompts?
   - Coming soon to Arize platform

---

### [Key Workflow Summary](https://www.youtube.com/watch?v=2HNSG990Ew8&t=1952s)
**[32:32 - 33:00]** - The complete eval process

1. **Instrument your code** - Send traces to observability platform
2. **Review production data** - Look at actual agent behavior
3. **Create datasets** - Pull examples worth testing into collections
4. **Define evals** - Specify what "good" means for your use case
5. **Run experiments** - A/B test prompts/models across datasets
6. **Iterate** - Use prompt playground to refine based on results
7. **Deploy** - Ship improved versions with confidence

---

## Practical Takeaways for AI Product Managers

1. **Set up observability first** - You can't improve what you can't see. Instrument your agents to capture traces and spans.

2. **Own the prompts** - As a PM, you're responsible for product outcomes. Don't delegate prompt writing entirely to engineers.

3. **Build eval datasets from production** - Real user data is more valuable than synthetic test cases.

4. **Start simple, then scale** - Manual review in spreadsheets is fine initially, but plan to scale with LLM-as-a-judge evals.

5. **Evaluate continuously** - Don't wait until launch. Eval should be part of your development workflow.

6. **Focus on your data** - Industry benchmarks don't matter as much as performance on your specific use cases.

7. **Decompose complex agents** - Break down multi-agent systems into components you can test independently.

8. **Measure what matters** - Latency, tone, correctness, hallucination - define metrics that align with user needs.

---

## Resources & Links

- **Slides and workshop materials:** ai.engineer.slack.com #workshop-AIPM channel
- **Arize Platform:** arize.com (sign up for hosted version)
- **Phoenix:** Open source alternative with similar workflows
- **GitHub repo:** Demo code for trip planner (pushed after workshop)
- **Previous content:** Lenny's Podcast episodes on AI PM topics

---

## Related Concepts

- **LLM-as-a-judge:** Using language models to evaluate other language model outputs at scale
- **Observability:** Monitoring and understanding AI system behavior through traces and spans
- **Prompt engineering:** Iterative refinement of prompts to improve outputs
- **Multi-agent systems:** Architectures using multiple specialized agents working together
- **Hallucination detection:** Evaluating whether AI outputs are grounded in provided context

---

## Technology Stack Mentioned

- **LangGraph:** Framework for building multi-agent systems
- **Crew AI:** Alternative multi-agent framework
- **Cursor AI:** AI-powered code editor used for building the demo
- **Arize/Phoenix:** Observability and evaluation platforms
- **OpenAI/Anthropic:** LLM providers mentioned for reliability concerns

---

*Workshop conducted at AI Engineer conference*
*Speaker: Aman Khan, AI Product Manager at Arize*
*Topics: AI evaluation, product management, multi-agent systems, observability*
