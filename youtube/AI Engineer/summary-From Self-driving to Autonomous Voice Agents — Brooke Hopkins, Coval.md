# From Self-driving to Autonomous Voice Agents — Brooke Hopkins, Coval

**Video URL:** https://www.youtube.com/watch?v=kDczF4wBh8s

---

## Executive Summary

Brooke Hopkins, founder of Coval and former leader of Waymo's eval infrastructure team, shares insights on applying self-driving evaluation methodologies to voice AI agents. The talk explores why voice agents struggle to scale to production despite their promise, introducing a framework for building reliable autonomous voice agents through large-scale simulation and probabilistic evaluation. Hopkins argues that voice will be the next major platform after web and mobile, with every enterprise expected to launch voice experiences within three years, making robust evaluation infrastructure critical for success.

---

## Topics and Key Points

### [Introduction: The Problem with Voice Agents](https://www.youtube.com/watch?v=kDczF4wBh8s&t=17s)
**Timestamp:** 00:17 - 01:00

- Brooke Hopkins is founder of Coval, building evals for voice agents
- Previously led eval infrastructure team at Waymo for self-driving simulations
- Voice agents have massive promise but aren't deployed everywhere
- **Main problem:** Trust - enterprises are scared to deploy voice agents to customer-facing workflows

**Key insight:** We're paradoxically overestimating (trying to automate everything at once) and underestimating (scoping problems too small) what voice agents can do today.

### [The False Choice: Deterministic vs. Autonomous](https://www.youtube.com/watch?v=kDczF4wBh8s&t=95s)
**Timestamp:** 01:35 - 02:32

Two current approaches to voice agents:
1. **Conservative but deterministic:** Force agents down specific paths (essentially expensive IVR trees)
2. **Autonomous but unpredictable:** Flexible to new scenarios but hard to scale to production

**Hopkins' thesis:** This is a false choice - you can have both reliability and autonomy, just like Waymo achieved.

### [The Waymo Analogy: Large-Scale Simulation](https://www.youtube.com/watch?v=kDczF4wBh8s&t=155s)
**Timestamp:** 02:35 - 04:00

How Waymo became reliable and smooth:
- **Large-scale simulation** has been the huge unlock for self-driving and robotics
- Evolution of evaluation approaches:
  1. Manual eval: Running cars on streets, noting failures (doesn't scale)
  2. Specific tests: Expecting exact outcomes for scenarios (brittle, expensive to maintain)
  3. **Large-scale evaluation:** Measuring how often event types happen across many simulations

**Key principle:** Instead of saying "for this specific instance I want X to happen," run large-scale simulations to reliably show how the agent is performing.

### [Similarities Between Self-Driving and Voice Agents](https://www.youtube.com/watch?v=kDczF4wBh8s&t=254s)
**Timestamp:** 04:14 - 05:32

Both are interactive systems where:
- You interact with the real world
- Each step requires responding to the environment
- You go back and forth continuously

**Why simulations are critical:**
- Enable testing all possible scenarios
- Create durable tests (don't break immediately)
- Provide coverage across large areas
- **LLM non-determinism is actually useful:** Shows all possible user responses and their probabilities

### [Probabilistic Evals vs. Input-Output Evals](https://www.youtube.com/watch?v=kDczF4wBh8s&t=334s)
**Timestamp:** 05:34 - 06:36

**Traditional LLM evals:** Run inputs through prompt → evaluate if output matches expected result (golden dataset approach)

**Conversational evals require reference-free evaluation:**
- Don't need exact expected outcomes for specific inputs
- Instead, define metrics across scenarios:
  - How often does the agent resolve user inquiries?
  - How often does it repeat itself?
  - How often does it say things it shouldn't?

**This approach:** Scales evals and applies metrics to many scenarios (learned from Waymo).

### [Constant Eval Loops for Scalability](https://www.youtube.com/watch?v=kDczF4wBh8s&t=398s)
**Timestamp:** 06:38 - 08:05

Voice agents are expensive to maintain in production without proper processes (can become 80% professional services work).

**Autonomous vehicle eval workflow:**
1. **Engineer iteration:** Find bug → run evals to reproduce → fix issue → verify fix
2. **Regression testing:** Run larger test sets to ensure you didn't break other functionality
3. **CI/CD workflows:** Pre-submit and post-submit checks before and after pushing to production
4. **Large-scale release:** Manual + automated evals before new releases
5. **Live monitoring:** Feed production issues back into the system

**Key lesson:** Goal is not to automate all evals, but leverage auto-evals for speed/scale and use manual time for nuanced judgment calls.

### [The Virtuous Cycle for Voice Agents](https://www.youtube.com/watch?v=kDczF4wBh8s&t=513s)
**Timestamp:** 08:33 - 09:18

Recommended process:
1. Start with simulated conversations (happy paths like "book an appointment")
2. Run simulations and analyze data
3. Identify failure patterns
4. Set up automated metrics
5. Iterate through this loop several times
6. Ship to production
7. Run evals again in production
8. **Virtuous cycle:** Simulate → flag for human review → feed back into simulations

### [Realism: How Much Do You Actually Need?](https://www.youtube.com/watch?v=kDczF4wBh8s&t=561s)
**Timestamp:** 09:21 - 11:26

Common question: "Are your simulated voice agents exactly like my customers?"

**Answer:** Realism level depends on what you're testing (like scientific method - control variables, test what matters).

**Hierarchy of realism for voice:**
1. **Workflows, tool calls, instruction following:** Don't even need voice - text testing is fastest and cheapest
2. **Interruptions, latency, pauses:** Basic/simple voices are sufficient
3. **Accents, background noise, audio quality:** Only need hyperrealistic voices when testing these specific production issues

**Self-driving parallel:** You don't need photorealistic simulations; just need to know "this is a dog, this is a person crossing the street" to test decision-making.

### [Denoising: Understanding Probability of Failure](https://www.youtube.com/watch?v=kDczF4wBh8s&t=693s)
**Timestamp:** 11:33 - 12:18

When you find a failed eval:
- It's not the end of the world if it fails once
- **Key question:** What's the probability of this failing overall?

**Approach:** Re-simulate the scenario 100 times
- Failing 50/100 times? It's a coin flip
- Failing 99/100 times? Definitely always failing
- Failing 1/100 times? Might be acceptable for your application

**Analogy to cloud infrastructure:** Like targeting "9s of reliability" - define reliability goals for different parts of your voice product.

### [Metrics: Keeping It Simple](https://www.youtube.com/watch?v=kDczF4wBh8s&t=738s)
**Timestamp:** 12:18 - 13:38

Example simple metric: **Conversation success**
- Did the conversation end successfully?
- No need for complex annotation or detailed criteria initially

**Evolution of metrics:**
1. Start simple with yes/no success metrics
2. Get more sophisticated over time as you iterate
3. Balance sophistication with team velocity

**Warning:** Don't boil the ocean with metrics - choose what matters for your specific use case.

### [Benchmarking vs. Custom Evals](https://www.youtube.com/watch?v=kDczF4wBh8s&t=818s)
**Timestamp:** 13:38 - 14:45

**Golden datasets and benchmarks:**
- Useful for directional guidance
- Help improve performance on specific metrics
- **Limitation:** Don't tell you if your agent will actually work in production with real users

**Better approach:** Combine both
- Use benchmarks for rough direction
- Build custom evals with real production data
- Iterate based on actual user conversations

### [Determining Your Eval Process](https://www.youtube.com/watch?v=kDczF4wBh8s&t=885s)
**Timestamp:** 14:45 - 15:16

Questions to answer:
- How confident do you need to be about agent performance?
- What level of reliability are you targeting?
- Maybe labeling just 10 conversations is enough
- Or maybe you need to dial it in more precisely

**Key insight:** Being thoughtful about reliability requirements upfront makes the workflow powerful.

### [Recommended Approach to Voice AI Evals](https://www.youtube.com/watch?v=kDczF4wBh8s&t=918s)
**Timestamp:** 15:18 - 16:01

Four-tier evaluation strategy:

1. **Public benchmarks:** Rough dial for direction
2. **Custom benchmarking:** Use your domain-specific data (e.g., medical terms for healthcare companies)
3. **Task-based evals:** Test specific modules (text-based or smaller components) - don't need to enable every module to test one thing
4. **End-to-end evals:** Run everything at scale as it would in production

### [Building Your Eval Infrastructure](https://www.youtube.com/watch?v=kDczF4wBh8s&t=1003s)
**Timestamp:** 16:43 - 17:38

Steps to implementation:

1. **Benchmark voice stack components:**
   - Test different voices for your conversation types
   - Test different LLMs for your specific tasks
   - Voice has many model choices - benchmark each part

2. **Establish baseline performance:**
   - Where are problem areas?
   - Where is it working?
   - Where could it be better?

3. **Create eval process:**
   - Continuous monitoring setup
   - Bug handling workflow from production
   - Test set hierarchy (customer-specific, workflow-specific, feature-specific)
   - Dashboards and processes for continuous check-ins

**Underestimated piece:** Having a continuous eval process vs. just checking "does it work during the pilot period?"

### [The Future: Voice as the Next Platform](https://www.youtube.com/watch?v=kDczF4wBh8s&t=1078s)
**Timestamp:** 17:58 - 18:51

**Platform evolution:** Web → Mobile → Voice

Each platform shift changed:
- What companies let you do
- Where in the workflow you meet users
- Baseline user expectations

**Bold prediction:** In the next 3 years, every enterprise will launch a voice experience
- Will become like mobile apps - a baseline expectation
- An airline without good voice experience will be like one without a good mobile app
- User expectations for "magical voice AI experiences" will rapidly increase

### [Closing Thoughts](https://www.youtube.com/watch?v=kDczF4wBh8s&t=1134s)
**Timestamp:** 18:54 - 19:24

- Coval is building the next generation of scalable voice AI with integrated evals
- The field is technically fascinating: work with every model across the stack
- Many different model types, problems, scalability challenges
- New frontiers in infrastructure where "no one knows the answers"
- Company is hiring for those interested in the space

---

## Key Takeaways

1. **Reliability + Autonomy is possible:** Don't settle for the false choice between deterministic IVR trees and unpredictable autonomous agents

2. **Large-scale simulation unlocks scalability:** Just as it did for self-driving, simulation enables testing scenarios that would be impossible to cover manually

3. **Think probabilistically, not deterministically:** Focus on "how often does this fail across 100 runs?" rather than "did this one test pass?"

4. **Match realism to what you're testing:** Text for workflows, basic voice for latency, hyperrealistic only for audio quality issues

5. **Build continuous eval loops:** Make evaluation integral to development workflow, not a one-time gate before launch

6. **Start simple, iterate:** Begin with basic success metrics and get more sophisticated over time based on real data

7. **Voice is the next platform:** Prepare for a world where voice AI is a baseline enterprise expectation within 3 years
