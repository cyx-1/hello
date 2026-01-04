# Mentoring the Machine — Eric Hou, Augment Code

**Video URL:** https://www.youtube.com/watch?v=Zniw5c9_jx8

---

## Executive Summary

Eric Hou from Augment Code shares a compelling personal story about how AI coding agents have fundamentally transformed software engineering work. He recounts a "terrible Tuesday" that became routine through the power of AI agents working in parallel - handling a critical design system component, resolving a staging emergency, and mentoring a new hire simultaneously. The talk emphasizes treating AI agents like junior engineers who need mentoring, not micromanagement, and highlights the organizational gaps preventing wider adoption: lack of knowledge infrastructure, evaluation culture, and trust boundaries. Eric demonstrates how Augment has addressed these challenges through context engines, systematic evaluation frameworks, and sandboxed environments, enabling engineers to accomplish in half a day what would typically take weeks.

---

## Topics

### [Introduction and Background](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=0s)
**[00:00 - 01:42]**

- Eric Hou introduces himself as a member of technical staff at Augment Code
- Background: 6 years building products for automotive industry with systems touched by tens of thousands of engineers
- Augment builds for real software engineering at scale in production
- Talk structure: personal journey (sections 1-2) and organizational gaps with AI adoption (sections 3-4)
- Key points: Augment focuses on capabilities rare in today's "vibe coded" world

### [The Terrible Tuesday: A Day in Engineering Hell](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=102s)
**[01:42 - 03:48]**

- **9:00 AM**: Behind on critical design system component due last Friday, teams waiting
- **9:30 AM**: Staging emergency - main API endpoint completely broken, blocking all QA and deployments
- **10:15 AM**: New hire engineer needs help understanding the extension system
- The familiar sinking feeling of a derailed day - working 12 hours but accomplishing nothing
- Industry statistics:
  - Every interruption costs 23 minutes of recovery time
  - 23% of time spent maintaining code vs building features
  - $300 billion annually spent on context switching and firefighting
- "We've normalized this chaos" - but it doesn't need to be this way

### [Live Demo: Augment Agent in Action](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=228s)
**[03:48 - 04:59]**

- Demonstrates Augment Extension with AI agent capabilities
- Task: Create a personality for the agent referencing AI World Fair and San Francisco energy
- Key insight: Guidelines draw boundaries for the agent rather than exact implementation instructions
- Agent runs in background while presenter continues talk
- Example of "mentoring" rather than micromanaging the AI

### [The Transformed Tuesday: Parallel AI Orchestration](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=299s)
**[04:59 - 08:52]**

- **9:00 AM**: Start scoping design component with agent before coffee - providing scaffolding, outcomes, context, and constraints
- Agent explores codebase and builds RFC while engineer takes coffee break
- **9:30 AM**: Staging emergency handled by parallelizing work:
  - Hand off component to one agent
  - Two AI agents parse logs and perform git bisect
  - Augment Slackbot manages team communications
- **10:15 AM**: Direct new hire to Augment Slackbot with access to context engine, codebase, documentation, Linear
- **11:00 AM**: Evaluation phase:
  - Design system component complete with Storybook link
  - Bad commit found and reverted
  - Postmortem doc started, remediation exploration begun
- **12:00 PM**: Lunch while agents continue working
- **Afternoon**: Complete gRPC library upgrade touching 12 services, 20,000 lines of code with tests and writeup
- Result: 3 weeks of estimated work completed in half a day of active keyboard time

### [Core Realization: AI as Junior Engineers Needing Mentorship](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=532s)
**[08:52 - 11:45]**

- Central insight: Work with AI as you would with junior engineers - through mentoring, not ticket assignment
- **Where the analogy fits**:
  - Need clear context and direction
  - Struggle with ambiguous requirements
  - Benefit from structured feedback
  - Can execute well-defined tasks independently
- **Where it breaks down**:
  - Junior engineers learn from mistakes; AI repeats them without feedback
  - Humans ask clarifying questions; AI makes assumptions
  - People grow trust over time; AI trust must be continuously verified
  - Humans have social awareness; AI lacks collaborative instincts
- Shift in mindset: From "building with my hands" to "ensuring work gets done correctly"
- Most important skill: Being clear, concise, and effective in communication

### [Gap #1: Knowledge Infrastructure](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=705s)
**[11:45 - 14:30]**

- Junior engineers rely on team knowledge; AI needs structured knowledge systems
- **What engineers have**: Tribal knowledge, onboarding buddies, documentation scattered across tools
- **What AI needs**: Centralized, searchable, structured knowledge infrastructure
- Augment's solution: Context Engine
  - Aggregates codebase, documentation, Slack, Linear, GitHub
  - Understands organizational patterns and decision history
  - Powers Slackbot for instant answers to questions like "Why did we choose React over Vue?"
- Impact: New hires productive faster, senior engineers freed from repetitive questions
- Example: New engineer asks "How do I deploy to staging?" - Slackbot provides step-by-step guide with links

### [Gap #2: Evaluation Culture](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=870s)
**[14:30 - 16:33]**

- Trust with humans builds gradually; AI requires systematic verification
- Traditional code review assumes good intentions; AI output needs validation
- Three-tier evaluation approach at Augment:
  1. **Syntax-level**: Does code compile? Do tests pass? Linting checks?
  2. **Semantic-level**: Does it follow architectural patterns? Meet requirements? Handle edge cases?
  3. **Business-level**: Does it solve the actual problem? Create technical debt? Align with goals?
- Real example: Agent implemented feature flag system but didn't update feature flag documentation
- Systematic eval catches issues humans miss in traditional reviews
- Culture shift: Make evaluation central to development process, not afterthought

### [Gap #3: Trust Boundaries and Sandboxing](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=993s)
**[16:33 - 18:40]**

- Junior engineer mistake: Edit wrong file, break staging - reversible with human oversight
- AI agent mistake: Same actions but at machine speed and scale - potentially catastrophic
- Need technical guardrails beyond cultural norms
- **Augment's sandbox approach**:
  - Isolated ephemeral development environments for each agent task
  - Changes only promoted to main environment after approval
  - Multi-layer verification: automated checks + human review
  - Clear scope definitions prevent agents from touching unrelated code
- Real example: Agent fixed bug but also "optimized" unrelated authentication code
- Without sandboxes: Production-breaking change
- With sandboxes: Caught in review, only bug fix merged
- Security benefit: Even if agent compromised, damage contained to sandbox

### [The Bigger Picture: Augment's Integration Strategy](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=1120s)
**[18:40 - 20:20]**

- These three elements (knowledge infrastructure, evaluation culture, trust boundaries) work together
- Knowledge infrastructure gives agents context to make good decisions
- Evaluation culture provides systematic feedback to verify decisions
- Trust boundaries ensure mistakes stay contained
- Result: AI becomes reliable multiplier of engineering capacity
- **Not a hypothetical future** - this is how Augment engineers work today
- Real productivity gains: Work that took weeks now takes days or hours
- Quality remains high due to evaluation and sandboxing
- Teams handle more complexity with same headcount

### [Practical Advice for Implementation](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=1220s)
**[20:20 - 22:03]**

- **Start small**: Pick one high-friction area (documentation Q&A, log analysis)
- **Build knowledge infrastructure first**: Centralize documentation before deploying agents
- **Establish evaluation checkpoints**: Define what "good" looks like before automating
- **Create safe experimentation spaces**: Sandboxes let teams learn without risk
- **Treat it as culture change, not tool adoption**: Requires new workflows and mental models
- **Measure and iterate**: Track what works, what doesn't, and why
- Most important: Get engineers comfortable with the "mentor" mindset

### [The Future of Engineering Work](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=1323s)
**[22:03 - 23:45]**

- Shift from "Can AI replace engineers?" to "How do engineers work with AI?"
- Answer: By being better mentors, evaluators, and architects
- Engineers become force multipliers instead of individual contributors
- Still requires deep technical expertise - but applied differently
- Junior engineers entering industry will expect this workflow as default
- Organizations not adapting will face competitive disadvantage
- The $300 billion wasted on context switching can be redirected to innovation
- "Terrible Tuesdays" become routine productivity wins

### [Closing Thoughts and Q&A](https://www.youtube.com/watch?v=Zniw5c9_jx8&t=1425s)
**[23:45 - End]**

- Journey from individual coding to team orchestration
- AI agents are tools that require organizational support systems
- Success requires: knowledge infrastructure + evaluation culture + trust boundaries
- This isn't about working less - it's about accomplishing more
- The future of engineering is collaborative intelligence between humans and AI
- Visit augmentcode.com or booth for more information
- Invitation for questions and discussion

---

## Key Takeaways

1. **Treat AI as a junior engineer who needs mentoring** - provide context, scaffolding, and boundaries rather than exact instructions
2. **Build knowledge infrastructure first** - centralize organizational knowledge into searchable systems before deploying AI agents
3. **Establish systematic evaluation culture** - verify AI output at syntax, semantic, and business levels
4. **Implement trust boundaries through sandboxing** - isolate agent work in ephemeral environments to contain mistakes
5. **Parallel work orchestration is the superpower** - handle multiple complex tasks simultaneously by delegating to AI agents
6. **The mental shift is from builder to mentor/evaluator** - deep technical knowledge still required but applied differently
7. **Real productivity gains are possible today** - 3 weeks of work in half a day is achievable with proper setup
8. **This requires organizational change, not just tools** - culture, processes, and infrastructure must evolve together

---

## Notable Quotes

- "Every single interruption costs us 23 minutes of recovery time. And as an industry, we're spending 23% of our time maintaining code instead of building new features. That translates to $300 billion annually spent on context switching and firefighting."

- "To make the most use out of AI, we need to work with it as we would work with junior engineers. Not assigning tickets, but mentoring."

- "Junior engineers learn from mistakes; AI repeats them without feedback. Humans ask clarifying questions; AI makes assumptions."

- "The real transformation here is not just that I've completed this work in parallel. The real transformation is that I've unlocked time that I previously did not have."

- "This scenario that I just described, all three of these challenges was something that I personally had to face and solved in around half a day of active keyboard time. Same problems, same complexity, same time pressure, but instead of it being one of those days, it became a normal Tuesday."
