# From Arc to Dia: Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York

**Video URL:** https://www.youtube.com/watch?v=o4scJaQgnFA

---

## Executive Summary

Samir Mody, Head of AI Engineering at The Browser Company of New York, shares lessons learned from building Arc browser and transitioning to Dia, their AI-native browser. The talk covers three main areas: optimizing tools and processes for faster iteration, treating model behavior as a craft and discipline, and implementing AI security as an emergent property of product building. Key insights include building prototyping tools directly into the product (enabling non-engineers to iterate on AI features), using automated prompt optimization techniques like JEPA, forming specialized model behavior teams from unexpected roles, and designing products with prompt injection protection through user confirmation flows. The overarching lesson is that AI transformation requires company-wide evolution, not just product changes.

---

## Topics

### [Introduction and Company Background](https://www.youtube.com/watch?v=o4scJaQgnFA&t=24s)
**Timeline:** 00:24 - 03:14

- Samir introduces himself as head of AI engineering at The Browser Company
- Company mission: rethink how people use the internet, founded in 2019
- Arc browser shipped in 2022 - made internet more personal, organized, and delightful
- Arc viewed as incremental improvement, not the full vision
- 2022: Got access to LLMs (GPT models), began prototyping AI features
- Early 2024: Released "Act 2" video announcing AI would transform the browser
- Shipped Dia - AI native browser with assistant that personalizes and helps with work

### [Optimizing Tools and Process for Faster Iteration](https://www.youtube.com/watch?v=o4scJaQgnFA&t=241s)
**Timeline:** 04:01 - 09:00

**Key Investment Areas:**
- Prototyping for AI product features
- Building and running evals
- Collecting data for training and evaluation
- Automation for hill climbing

**Initial Challenges:**
- First tool: rudimentary prompt editor only in dev builds
- Limited access (only engineers could use it)
- Slow iteration speeds
- No personal context available

**Evolution:**
- Built all tools directly into their product (Dia)
- Everyone uses Dia internally daily - dogfooding with full context
- Tools include: prompts, context, models, parameters - all exposed
- 10x speed improvement in ideating, iterating, and refining
- Widened access from CEO to newest hire - anyone can create/refine products
- Tools for optimizing memory knowledge graph
- Tools for computer use mechanism (tried tens of strategies before choosing one)
- Enabled creativity across PMs, designers, customer service, strategy & ops

### [JEPA: Automated Prompt Optimization](https://www.youtube.com/watch?v=o4scJaQgnFA&t=388s)
**Timeline:** 06:28 - 09:00

**What is JEPA:**
- Based on a 2024 research paper
- Sample-efficient way to improve complex LLM systems without RL or fine-tuning
- Critical for small companies with limited resources

**How it Works:**
1. Seed system with set of prompts
2. Execute across tasks and score them
3. Use PA selection to select best ones
4. Leverage LLM to reflect on what went well/didn't
5. Generate new prompts and repeat

**Key Innovations:**
- Reflective prompt mutation technique
- Selection process explores more prompt space (not just one avenue)
- Tunes text, not weights

**Two-Phase Build Process:**
1. **Prototyping/Ideation Phase:** Widen breadth of ideas, lower threshold for who can build them, try many ideas weekly from diverse people, dogfood internally
2. **Refinement Phase:** Collect and refine evals to clarify requirements, hill climb through code/prompting/automated techniques like JEPA, dogfood internally, then ship

### [Model Behavior as Craft and Discipline](https://www.youtube.com/watch?v=o4scJaQgnFA&t=574s)
**Timeline:** 09:34 - 12:50

**What is Model Behavior:**
- Function that defines, evaluates, and ships desired model behavior
- Turning principles into product requirements, prompts, and evals
- Shaping behavior and personality of LLM products (Dia assistant)

**Four Key Areas:**
1. **Behavior Design:** Defining product experience, style, tone, shape of responses
2. **Data Collection:** For measurement and training
3. **Product Requirements:** Clarifying through evals
4. **Model Steering:** Building the product - prompting, model selection, context window, parameters

**Evolution Analogy (Websites → Model Behavior):**
- Past: Websites were functional → Now: Complex design craft
- AI Past: Functional prompts, evals, instructions → Now: Agent behaviors, goal-directed reasoning, autonomous tasks, self-correction, personality shaping
- Future: Early days - will evolve into specialized, prevalent function at product companies

**Surprising Team Formation Story:**
- Initially engineers wrote prompts
- Built prompt tools enabling more people to iterate
- Strategy & ops team member rewrote all prompts over one weekend
- Came in Monday with Loom video explaining approach
- Unlocked new level of capability and quality
- Led to formation of dedicated model behavior team
- Lesson: Best people might not be engineers - could be from strategy/ops or other roles

### [AI Security as Emergent Property of Product Building](https://www.youtube.com/watch?v=o4scJaQgnFA&t=772s)
**Timeline:** 12:50 - 16:34

**Focus: Prompt Injections**

**What is Prompt Injection:**
- Attack where third party overrides LLM instructions to cause harm
- Can lead to: data exfiltration, malicious command execution, ignoring safety rules

**Example Attack:**
- User asks LLM to summarize website
- Hidden prompt injection in website HTML
- Instead of summarizing, LLM opens new website
- Extracts personal information
- Embeds data as GET parameters in URL
- Effectively exfiltrates user data

**Why Critical for Browsers - "Lethal Trifecta":**
1. Access to private data
2. Exposure to untrusted content
3. Ability to externally communicate (open websites, send emails, schedule events)

**Technical Approaches (Insufficient Alone):**
1. **Wrapping untrusted context in tags:** Tell LLM to listen to instructions around tags, not content - easily escapable
2. **Separating data and instructions:** Assign system role for instructions, user role for third-party content, add random tags - helps but no guarantees

**Solution: Product Design Integration:**
- Blend technology + UX + design into cohesive story
- Build security from the ground up

**Practical Example - Autofill Tool:**
- Uses LLM with context, memory, details to fill forms
- Vulnerability: Prompt injection could extract data onto form
- Mitigation: Before writing form, user reads and confirms data in plain text
- Doesn't prevent injection but gives user control, awareness, trust

**Similar Confirmation Steps:**
- Scheduling events in Dia
- Writing emails in Dia

### [Conclusion: Company-Wide Transformation](https://www.youtube.com/watch?v=o4scJaQgnFA&t=998s)
**Timeline:** 16:34 - 17:30

**Three Main Lessons:**
1. Optimizing tools and process for fast iteration
2. Treating model behavior as craft and discipline
3. AI security as emergent property of product building

**Core Realization:**
- Started with: "How can we leverage AI to make Arc better?"
- Learned: Not just product evolution - **company evolution**
- Affects: How they build, team structure, how they train, how they hire, how they communicate, how they collaborate

**Final Message:**
When you recognize a technology shift, you must embrace it with conviction.

---

**Last Updated:** December 31, 2024
