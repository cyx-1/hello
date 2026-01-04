# Building AI Products That Actually Work — Ben Hylak (Raindrop), Sid Bendre (Oleve)

**Video URL:** https://www.youtube.com/watch?v=eSvXbb2EBYc

---

## Executive Summary

Ben Hylak (CTO of Raindrop) and Sid Bendre (co-founder of Oliv) share practical frameworks for building reliable AI products that scale. Ben discusses why AI products remain challenging despite model improvements, focusing on the need for production signals rather than just evals. Sid introduces the "Trellis" framework—a systematic approach to managing AI's nondeterministic nature through discretization, prioritization, and recursive refinement of workflows. Together, they emphasize that iteration based on real-world data is critical for building AI products that actually work.

---

## Topics

### [Introduction and Background](https://www.youtube.com/watch?v=eSvXbb2EBYc&t=0s)
**[00:00 - 02:00]**

- Ben Hylak introduces himself as CTO of Raindrop, which helps companies find and fix issues in AI products
- Background includes robotics, SpaceX avionics, and Apple design team
- Sid Bendre co-founded Oliv, growing viral apps to 6M ARR with just 4 people
- Focus on building AI products through iteration rather than just evals

**Key Points:**
- Raindrop works with fastest-growing AI companies across diverse use cases
- The session will focus on practical iteration strategies for AI products
- Consumer response: "please no more evals" talks

### [The State of AI Products: Challenges Remain](https://www.youtube.com/watch?v=eSvXbb2EBYc&t=109s)
**[01:49 - 04:00]**

- It's possible to train small, focused models that excel at specific tasks
- Even OpenAI ships problematic products (e.g., Codex issues)
- Real-world examples of AI failures:
  - Virgin Money chatbot threatening customers for using "virgin"
  - Google Cloud suggesting Azure/Roblox credits
  - Grok going off-rails with inappropriate responses

**Key Points:**
- Focusing on specific use cases enables exceptional performance
- Deep Research shows what's possible when focused on one capability
- AI product failures still common across all providers

### [Will AI Products Get Easier to Build?](https://www.youtube.com/watch?v=eSvXbb2EBYc&t=362s)
**[06:02 - 08:00]**

- **Yes**: Some things are easier (e.g., JSON output now just a parameter vs. threatening GPT-4)
- **No**: Communication is fundamentally hard—even with humans
- Paul Graham's take on AGI ending prompt engineering is wrong
- More capable products = more undefined behavior and edge cases

**Key Points:**
- Can't define entire product scope upfront anymore
- Must iterate: ship → observe → refine
- MCP and new integrations create new failure modes

### [The Truth About Evals](https://www.youtube.com/watch?v=eSvXbb2EBYc&t=494s)
**[08:14 - 11:00]**

Three common eval misconceptions:

1. **Evals tell you how good your product is** - They don't (Goodhart's Law)
   - Only capture what you already know
   - Recent models score lower on evals but perform better in practice

2. **LLM-as-judge works well** - It largely doesn't
   - Best companies use highly curated datasets with autogradable evals
   - Deterministic evaluation preferred over subjective LLM scoring

3. **Move offline evals to production** - Doesn't work either
   - Too expensive or only covers small traffic percentage
   - Doesn't catch emerging patterns
   - OpenAI's own postmortem: "evals catch what we know; real-world use spots problems"

**Key Points:**
- Evals are important but have significant limitations
- Production data reveals issues evals can't predict
- Need different approach for production monitoring

### [Signals: The Key to Reliable AI Apps](https://www.youtube.com/watch?v=eSvXbb2EBYc&t=669s)
**[11:09 - 14:00]**

**Anatomy of an AI Issue:**
- Combination of signals (implicit + explicit) + user intents
- Unlike traditional apps, AI has no concrete errors/exceptions

**Explicit Signals:**
- Thumbs up/down, copy behavior (ChatGPT tracks this)
- Preference data (A/B response selection)
- Regeneration, syntax errors, sharing, suggesting

**Implicit Signals:**
- Detecting (not judging): refusals, task failures, user frustration
- Clustering reveals patterns (e.g., Grok's tweet search issues)

**Process:**
1. **Define** signals (explicit + implicit)
2. **Explore** via tags, metadata, properties, keywords, intents
3. **Refine** continuously based on patterns

**Key Points:**
- Need constant monitoring ("IV drip of your app's data")
- Signals + intents define AI issues
- Used for RL and continuous improvement

### [Trellis Framework Introduction](https://www.youtube.com/watch?v=eSvXbb2EBYc&t=850s)
**[14:10 - 15:30]**

**Challenge:** Viral AI products need:
1. Wow factor for virality
2. Reliable, consistent experiences
3. But AI is chaotic and nondeterministic

**Trellis Solution:**
Systematic approach to continuously improve AI experiences at scale while preserving the "magic"

**Three Core Axioms:**
1. **Discretization** - Break infinite output space into specific buckets
2. **Prioritization** - Rank buckets by business impact
3. **Recursive Refinement** - Repeat process within buckets to create order

**Key Points:**
- Guide chaos instead of eliminating it
- Designed around virality engine for consumer products
- Enables scaling to millions of users

### [Trellis: Six-Step Process](https://www.youtube.com/watch?v=eSvXbb2EBYc&t=936s)
**[15:36 - 17:00]**

**Step 1: Initialize Output Space**
- Launch MVP agent informed by product priors
- Goal: collect massive user data

**Step 2: Classify Intents**
- Group user data into intents based on usage patterns
- Understand why users stick to your product

**Step 3: Convert to Workflows**
- Create semi-deterministic workflows for each intent
- Broad enough to be useful, narrow enough to be reliable

**Step 4: Prioritize Workflows**
- Score based on company KPIs

**Step 5: Analyze from Within**
- Understand failure patterns and sub-intents

**Step 6: Recursive Refinement**
- Keep recursing into workflows

**Key Points:**
- Start broad, then systematically narrow focus
- Workflows must balance flexibility and reliability
- Continuous iteration based on real usage

### [Prioritization Strategies](https://www.youtube.com/watch?v=eSvXbb2EBYc&t=1024s)
**[17:04 - 18:00]**

**Naive Approach:**
- Volume only - focus on highest volume workflows
- Leaves satisfaction gains on table

**Better Approach:**
- Volume × Negative Sentiment Score
- Expected lift from fixing high-volume pain points

**Most Informed Approach:**
- Negative Sentiment × Volume × Estimated Achievable Delta × Strategic Relevance
- Achievable delta considers implementation feasibility
- Example: if foundational model training needed, delta ≈ 0 for most companies

**Key Points:**
- Prioritization must tie to company KPIs
- Consider both impact and achievability
- Strategic alignment matters

### [Workflow Benefits and Conclusion](https://www.youtube.com/watch?v=eSvXbb2EBYc&t=1082s)
**[18:02 - 18:35]**

**Workflow Properties:**
- Self-attributable
- Deterministic (within bounds)
- Self-bound (changes contained)

**Benefits:**
- Teams move faster
- Changes don't spill across workflows
- Reliable, repeatable improvements

**Final Result:**
Magic that is engineered, repeatable, testable, and attributable—not accidental

**Key Points:**
- Structure enables velocity at scale
- Containment prevents regression
- AI "magic" becomes systematically reproducible
- Blog post with full Trellis framework available via QR code

---

## Key Takeaways

1. **AI products won't automatically get easier** - Communication is hard, and capability increases complexity
2. **Evals have limits** - They're important but don't replace production monitoring and real-world signals
3. **Signals > Evals** - Track explicit (thumbs up/down, copy, regenerate) and implicit (refusals, frustration) signals
4. **Anatomy of AI issues** = Signals + Intent
5. **Trellis Framework** - Discretize → Prioritize → Recursively Refine
6. **Iteration is key** - Ship → Collect data → Identify intents → Build workflows → Analyze → Repeat
7. **Prioritize smartly** - Volume × Negative Sentiment × Achievable Delta × Strategic Relevance
8. **Workflows enable scale** - Self-contained, deterministic-ish workflows let teams move fast reliably

---

**Last Updated:** 2026-01-03
