# Leadership in AI Assisted Engineering – Justin Reock, DX (acq. Atlassian)

**Video URL:** https://youtu.be/PmZDupFP3UM

---

## Executive Summary

Justin Reock from DX (acquired by Atlassian) presents findings on the highly variable impact of GenAI on developer productivity. While industry averages show modest improvements (3-7%), individual companies experience wildly different results ranging from 20% increases to 20% decreases in key metrics. The presentation emphasizes that success depends on leadership strategies including psychological safety, proper education, time to learn, clear AI policies, measuring the right metrics, and integrating AI across the entire SDLC—not just code writing. Top-performing companies focus on bottlenecks beyond coding, such as legacy modernization, onboarding, and incident response.

---

## Main Topics

### 1. [Current State of GenAI Impact on Productivity](https://www.youtube.com/watch?v=PmZDupFP3UM&t=48s) (00:48)

- Google reports 10% productivity increase among developers
- METR study shows controversial 19% **decrease** in productivity with code assistance
- Paradox: Engineers **felt** more productive but data showed they were less productive
- Industry averages from DORA research show modest positive impacts:
  - 7.5% increase in documentation quality
  - 3.4% increase in code quality
  - 2.6% increase in change confidence
  - 1% reduction in change failure rate

**Key Insight:** Industry averages hide extreme variability between companies.

### 2. [The Variability Problem: Why Averages Are Misleading](https://www.youtube.com/watch?v=PmZDupFP3UM&t=140s) (02:20)

- DX's internal data revealed extreme variance when broken down per company
- Some companies see 20% **increases** in change confidence, others see 20% **decreases**
- Same pattern for code maintainability and change failure rate
- A 2% increase in change failure rate (with 4% industry benchmark) means shipping **50% more defects**

**Key Insight:** Success with AI is not guaranteed—it depends heavily on implementation approach.

### 3. [What Doesn't Work: Common Failures](https://www.youtube.com/watch?v=PmZDupFP3UM&t=216s) (03:36)

- Top-down mandates for 100% AI adoption drive compliance gaming (e.g., updating README daily)
- Lack of education and enablement leads to poor outcomes
- Just "turning on the tech" without training fails
- Difficulty measuring impact or not knowing what to measure

**Key Insight:** Mandating adoption without support creates negative results.

### 4. [What Does Work: Evidence-Based Success Factors](https://www.youtube.com/watch?v=PmZDupFP3UM&t=270s) (04:30)

DORA research identified key initiatives that drive positive outcomes:

- Clear AI policies with sharp, confident impact predictions
- Time to learn—not just materials, but actual space to experiment
- Focus on these high-impact factors rather than blanket mandates

### 5. [Reducing Fear of AI](https://www.youtube.com/watch?v=PmZDupFP3UM&t=373s) (06:13)

**Google's Project Aristotle (2012):** The overwhelming predictor of team productivity is **psychological safety**, not high performers, experienced managers, or unlimited resources.

**Current Reality:**
- SWE-bench shows agents can complete ~33% of tasks autonomously
- This means they **cannot** do 67% of tasks without human intervention
- AI is **augmenting**, not replacing engineers

**Leadership Actions:**
- Be transparent about AI's purpose: augmentation, not replacement
- Set clear intents and communicate proactively
- Don't wait for engineers to get scared—address concerns upfront

### 6. [Metrics That Matter: Speed vs. Quality](https://www.youtube.com/watch?v=PmZDupFP3UM&t=441s) (07:21)

**Two Levers:** Speed and Quality

**Three Types of Metrics:**

1. **Telemetry Metrics** (from APIs)
   - Accept vs. suggest rates—but flawed (requires clicking "accept", doesn't show if code was rewritten)
   - Provides context but incomplete picture

2. **Experience Sampling**
   - Add fields to PR forms: "I used AI for this PR" or "I enjoyed using AI"
   - Captures usage in workflow

3. **Self-Reported/Survey Data**
   - Must achieve 90%+ participation rates
   - Engineer questions against systems, not people (per W. Edwards Deming: 90-95% of productivity is determined by the system, not the worker)

**Foundational Metrics Still Matter Most:**
- Traditional developer experience and productivity metrics tell whether AI initiatives are actually working
- AI-specific metrics (utilization) tell what's happening with the tech, but core metrics show true outcomes

### 7. [What Top Companies Measure](https://www.youtube.com/watch?v=PmZDupFP3UM&t=569s) (09:29)

- **Microsoft:** Adoption metrics, "bad developer day" metric (telemetry-based)
- **Dropbox:** Weekly/daily active users, change failure rate
- **Booking:** Similar quality and adoption metrics

**DX AI Measurement Framework:**
1. **Utilization** (entry level): Who's using it? What % of PRs are AI-assisted?
2. **Impact** (mature): How does usage correlate to velocity and quality?
3. **Cost** (optimization): Understanding and optimizing spend

### 8. [Building Trust and Compliance](https://www.youtube.com/watch?v=PmZDupFP3UM&t=666s) (11:06)

**Establish Feedback Loops for System Prompts:**
- System prompts/cursor rules/agent markdown control model behavior
- Example: Models providing outdated Spring Boot 2 code when Spring Boot 3 is needed
- **Key:** Have a gatekeeper (person/group) who receives feedback and continuously improves system prompts

**Understanding Temperature Settings:**
- Temperature controls randomness/creativity (0-1, don't use exact 0 or 1)
- **Low temperature (0.001):** Same input = identical output (deterministic)
- **High temperature (0.9):** Same input = wildly different approaches (creative)
- Choose temperature based on use case needs

### 9. [Employee Success: Education and Time](https://www.youtube.com/watch?v=PmZDupFP3UM&t=813s) (13:33)

**DX's Study of High-Value Use Cases:**
- Sampled developers saving at least 1 hour/week
- Asked them to stack-rank top 5 most valuable use cases
- Created a guide with code examples and prompting strategies

**Top 5 Use Cases:**
1. **Stack trace analysis** (interpretive, not generative!)
2. Code generation
3. Test writing
4. Documentation
5. Code review assistance

**Key:** The #1 use case is **interpretive** (understanding errors), not generative—challenges common assumptions.

### 10. [Unblocking Usage Creatively](https://www.youtube.com/watch?v=PmZDupFP3UM&t=875s) (14:35)

- Leverage self-hosted and private models (easier with services like Bedrock, Fireworks AI)
- Partner with compliance **on day one**—you may be making false assumptions about what's blocked
- Think creatively around barriers instead of accepting them

### 11. [Integrating Across the SDLC](https://www.youtube.com/watch?v=PmZDupFP3UM&t=901s) (15:01)

**Theory of Constraints (Eli Goldratt):** "An hour saved on something that isn't the bottleneck is worthless."

**Data from 140,000 engineers shows:**
- AI provides good annualized time savings on coding
- BUT those savings are eclipsed by losses from:
  - Context switching and interruptions
  - Meeting-heavy days
  - Other bottlenecks

**Real-World Examples:**

**[Morgan Stanley's DevGenAI](https://www.youtube.com/watch?v=PmZDupFP3UM&t=940s) (15:40)**
- Analyzes legacy code (COBOL, mainframe, Perl)
- Creates specs for modernization
- Saves developers from reverse engineering
- **Result:** 300,000 hours saved annually

**[Zapier's Multi-Bot Approach](https://www.youtube.com/watch?v=PmZDupFP3UM&t=970s) (16:10)**
- Bots/agents assist with onboarding
- Engineers effective in **2 weeks** vs. industry benchmark of 30-90 days
- **Strategic decision:** Instead of maintaining headcount, they're hiring **faster** because each engineer delivers more value
- Increasing competitive edge through growth, not cost-cutting

**[Spotify's Incident Response](https://www.youtube.com/watch?v=PmZDupFP3UM&t=1017s) (16:57)**
- AI pulls together context when incidents detected
- Pushes runbooks, documentation directly into SRE Slack channels
- Eliminates critical minutes of information gathering
- Significantly improved MTTR (mean time to recovery)

### 12. [Next Steps for Leaders](https://www.youtube.com/watch?v=PmZDupFP3UM&t=1047s) (17:27)

1. **Distribute the AI strategy playbook** as reference for integrating AI into workflows
2. **Determine measurement methods** for evaluating GenAI impact
3. **Track and measure AI adoption** and correlate to overall impact metrics
4. **Iterate on best practices and use cases** based on data

---

## Key Takeaways

1. **Averages lie:** Industry averages of 3-7% improvement mask 40-point swings between best and worst performers
2. **Psychology matters more than tech:** Psychological safety (Google's Project Aristotle) is the top predictor of success
3. **Focus on bottlenecks:** Writing code is rarely the bottleneck—look at onboarding, legacy modernization, incident response, meetings
4. **Measure properly:** Combine telemetry, experience sampling, and surveys focused on systems (not people)
5. **Don't mandate—enable:** Top-down adoption mandates fail; education + time to learn + clear policies succeed
6. **Think strategically:** Companies like Zapier use AI to hire **more** (not replace), gaining competitive advantage

---

## Resources

- **AI Strategy Playbook for Senior Executives** (mentioned at start): Available via QR code in presentation
- **DX AI Measurement Framework:** Utilization → Impact → Cost maturity curve
- **Top Developer Use Cases Guide:** Based on survey of developers saving 1+ hour/week

---

**Presentation Length:** ~18 minutes
**Target Audience:** Engineering leaders, CTOs, VPs of Engineering
**Core Message:** AI's impact on productivity is highly variable and depends on leadership strategy, not just technology adoption.
