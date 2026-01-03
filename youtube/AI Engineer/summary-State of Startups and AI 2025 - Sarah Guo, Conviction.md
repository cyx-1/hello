# State of Startups and AI 2025 - Sarah Guo, Conviction

**Video URL:** https://www.youtube.com/watch?v=3MZS5gNElZM

---

## Executive Summary

Sarah Guo, co-founder of Conviction (an AI-native venture fund), delivers an insightful analysis of the current AI startup landscape in 2025. She argues that while AI product development is harder than many hoped, the value creation is massive and unprecedented. The talk focuses on why coding tools like Cursor succeeded first, how to build "Cursor for X" in other domains, and emphasizes that execution—not just innovation—is the primary moat in AI. Guo challenges conventional wisdom about "thin wrappers," demonstrating that sophisticated workflow integration and domain expertise create substantial value. She encourages engineers to become "translators" who bring AI magic to industries beyond software development.

---

## Main Topics

### [Introduction and Background](https://www.youtube.com/watch?v=3MZS5gNElZM&t=107s)
**[01:47 - 04:00]**

- Sarah Guo introduces Conviction, an AI-native venture fund started ~3 years ago (just before ChatGPT)
- Portfolio includes: Cursor, Cognition, Mistral, Thinking Machines, Harvey, Open Evidence
- Key observation: Never seen user uptake as fast as in the last 2+ years
- AI product/engineering is harder than hoped, but value creation is massive
- Companies going from 0 to $10M-$100M ARR faster than any previous technology revolution
- Position on AI hype cycle: Focus on actual usage numbers rather than market sentiment

### [Capabilities: Reasoning Models](https://www.youtube.com/watch?v=3MZS5gNElZM&t=322s)
**[05:22 - 06:00]**

- Reasoning is a new vector for scaling intelligence with more compute
- Unlocks new use cases:
  - Transparent high-stakes decisions where showing work matters
  - Sequential problems requiring systematic search
  - Knowledge work problems faced daily
- Reasoning enables more sophisticated agent capabilities

### [The Rise of Agents](https://www.youtube.com/watch?v=3MZS5gNElZM&t=368s)
**[06:08 - 07:24]**

- Non-marketing definition: Software that plans, takes ownership of tasks, holds goals in memory, tries hypotheses, and backtracks
- Ranges from sophisticated to simple implementations
- May use other models or search as tools
- Looks more like a colleague than a chatbot
- Conviction's Embed grant program data: 50% increase in agent startups over the last year
- Many agent applications are working in the real world

### [Other Modalities Progress](https://www.youtube.com/watch?v=3MZS5gNElZM&t=446s)
**[07:26 - 09:00]**

- Voice, video, image generation advancing rapidly
- Companies like HeyGen, ElevenLabs, Midjourney surpassing $50M ARR
- Demo of HeyGen's avatar technology showing gestures and expressions that reflect emotion
- Multimodality will affect huge swaths of the economy
- Voice AI will see first adoption in business workflows (medical consults, lead generation)
- As modalities become more controllable and less costly, adoption will accelerate

### [Model Layer Competition](https://www.youtube.com/watch?v=3MZS5gNElZM&t=600s)
**[10:00 - 11:28]**

- Market for model capabilities getting more competitive, not less
- Sam Altman: "Last year's model is a commodity"
- GPT-4 pricing: $30/M tokens → $2/M tokens in ~18 months (distilled versions now $0.10)
- Data from OpenRouter shows real market mix: Claude cutting into OpenAI, Google roaring back with Gemini
- New credible players: SSI, Thinking Machines, DeepSeek
- Open source will compete for business as expected
- **Recommendation:** Plan for a multimodel world; use tools like OpenRouter or inference platforms like Base10

### [Application Layer: Why Code Was First](https://www.youtube.com/watch?v=3MZS5gNElZM&t=674s)
**[11:34 - 13:16]**

**Cursor's Success:**
- $1M to $100M ARR in 12 months
- 500K developers, zero sales people
- Cognition (Devin) already top committer in many companies
- Windsurf acquired by OpenAI for $3B
- Lovable and Bolt each hit $30M ARR in weeks

**Why code was first:**
1. **Structured text:** Logical language with structure; much coding is sophisticated boilerplate
2. **Deterministic validation:** Can automatically check if code works (tests, compile, execute)
3. **Research priority:** Researchers believe code is crucial for AGI, so poured resources into it
4. **Domain expertise:** Engineers built tools for engineers—understood the workflow intimately

**Key insight:** The last point is the playbook for every other industry. Winners will be customer-centric builders who understand AI and redesign workflows from first principles.

### [The "Cursor for X" Recipe](https://www.youtube.com/watch?v=3MZS5gNElZM&t=821s)
**[13:41 - 16:08]**

**What makes Cursor valuable:**
- Not a single model—multiple models for diffs, merge, embeddings
- Manipulates and packages context skillfully
- Prompts models very skillfully
- Lets engineers avoid repetitive tasks and standardize (cursor rules)
- Retrieval accuracy improves with usage (coverage and freshness)
- UX that makes sense—familiar interface, shortcuts work, safe to say yes
- Fast enough to avoid frustration

**Guo's take:** If Cursor is a "wrapper," it's a very thick $14-15B wrapper
- Analogy: 80% wrap, 20% fill, but you choose the fill and there's an open market for fill
- Value is in the execution, not just the protein (model)

**Recipe to generalize:**
1. **Don't build generic text boxes** (OpenAI already won that)
2. **Domain knowledge is the bootstrap** - show up informed, don't make users explain
3. **Collect and package context automatically** - from other sources, not just natural language
4. **Use the right models at the right time** (orchestration)
5. **Present outputs thoughtfully** to users
6. **Not the end of GUI** - can capture and enable workflow with taste and work

**Key principle:** "The prompt is a bug, not a feature" - don't make users think; best AI products feel like mind reading because they are

### [Where to Apply This: Beyond Code](https://www.youtube.com/watch?v=3MZS5gNElZM&t=974s)
**[16:14 - 17:41]**

**The AI Leapfrog Effect:**
Counterintuitively, the most conservative, low-tech industries are adopting AI fastest.

**Portfolio company examples:**
- **Sierra:** Resolves 70% of customer service queries (SiriusXM, ADT)
- **Harvey:** 2 years in, $70M+ ARR; AI now essential to being competitive in legal industry
- **Open Evidence:** Helps doctors stay up-to-date with medical research; reaches 1/3 of US doctors weekly; average user uses it daily

**Common thread:** Companies that know their customers and solve real problems

**Insight:** Brett (Sierra) is chairman of OpenAI board; OpenAI was Harvey's seed investor—these people aren't worried about "thin wrappers"

### [Co-pilots vs. Full Automation](https://www.youtube.com/watch?v=3MZS5gNElZM&t=1086s)
**[18:06 - 19:05]**

**The Iron Man Analogy:**
- Tony Stark's suit augments him (can do amazing things)
- Suit can also fly around on command and do basic tasks without Tony
- Human tolerance for failure/hallucinations reduces dramatically as latency increases
- Path of least frustration: Build great augmentation, then ride the wave of capability

**Data insight:** Despite 50% increase in agent startups, co-pilots are still underrated in terms of what's driving revenue

**Advice:** Build the suit (co-pilot), and you can extend to the suit that flies on its own once capability improves

### [Opportunities in Hard Problems](https://www.youtube.com/watch?v=3MZS5gNElZM&t=1158s)
**[19:18 - 20:51]**

**Categories of opportunities:**
1. Good fit for purpose (e.g., law = lots of text generation)
2. Weren't possible before AI (machines interrogating humans)
   - Talk to every customer, not just top 5% by contract value
   - Root cause every alert proactively vs. firefighting
   - Mental model: Build as if you had an army of compliant, infinitely patient knowledge workers

**Hard problems where answers aren't in common crawl:**
- Robotics, biology, material science, physics, simulation
- Require clever data collection and interaction with atoms, not just bits
- Scary for software people, but juice is worth the squeeze
- Same reasoning that crushes math olympiads can navigate molecular space
- Fundamental questions for human society can be answered

### [Defensibility: Execution is the Moat](https://www.youtube.com/watch?v=3MZS5gNElZM&t=1266s)
**[21:06 - 22:25]**

**Uncomfortable truth:** Execution is the moat in AI, and that's available to all of us.

**Cursor example:**
- Did not invent code completion, the model, or their product surface area
- They just out-executed on every dimension
- Shipped great experience faster than competitors could copy
- Captured hearts and minds of developers

**Counter-example - Jasper:**
- Had first-mover advantage and brand
- Raised $125M
- First product was series of prompts, text box, and good SEO
- ChatGPT crushed it pretty quickly

**Advice from the trenches:**
- Build something thick and stay ahead
- No domains are out of question
- Magical AI experiences build customer trust and drive adoption
- Much of the data/context needed is not easily available today—advantage is open for taking, not for the labs

### [Conclusion: The Opportunity Ahead](https://www.youtube.com/watch?v=3MZS5gNElZM&t=1347s)
**[22:27 - 23:45]**

**We're in the dial-up era of AI**, moving quickly to broadband

**Historical perspective:**
- Instagram came 4 years after iPhone
- Uber 5 years, DoorDash 6 years
- Transformative companies weren't necessarily first to recognize opportunity—they reimagined experiences

**What's different this time:**
- Game board keeps getting shaken up
- Like getting a new iPhone that's actually different every 12 months
- New model release, new capability breakthrough, 1/10th the cost
- Every time game board turns, there's opportunity to win again

**Final message:**
- Engineers got the magic first (Anthropic data: 40% of usage still coding)
- But that's not 40% of economic opportunity in the world
- **It's the job of everyone in this room to be translators for the rest of the world**
- Build something revolutionary

---

## Key Quotes

> "This time it's different—this is the largest technology revolution that we get to be a part of."

> "AI product and AI engineering is quite a bit harder than people had hoped, but the value creation is massive."

> "Last year's model is a commodity." - Sam Altman

> "Cursor, if it's a wrapper, it's like a very nice thick perhaps 14 or 15 billion dollar wrapper."

> "The prompt is a bug, not a feature. Don't make me think as a user."

> "Execution is the moat in AI. And that's available to all of us."

> "We're in the dial-up era of AI and we're moving pretty quickly to broadband."

> "It is the job of everyone in this room to be the translators for the rest of the world."

---

**Talk Duration:** ~24 minutes
**Speaker:** Sarah Guo, Co-founder, Conviction
**Event:** AI Engineer Conference
