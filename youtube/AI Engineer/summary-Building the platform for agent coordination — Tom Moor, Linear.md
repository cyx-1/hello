# Building the platform for agent coordination — Tom Moor, Linear

**Video URL:** https://www.youtube.com/watch?v=UG9IAdmi2Dg

---

## Executive Summary

Tom Moor, engineering lead at Linear, discusses their journey building AI features and creating a platform for agent coordination. Starting with small, pragmatic AI features in 2023 (similar issues, natural language filters), Linear evolved to building a comprehensive agent platform by late 2024. They now position Linear as the coordination hub where AI agents can work alongside human teammates, with agents being first-class users who can be assigned tasks, mentioned in comments, and perform actions transparently. The talk covers their technical evolution, current AI features, and best practices for building agents that integrate with platforms.

---

## Topics & Key Points

### [Introduction & Linear Overview](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=17s)
- Linear is a product development tool, starting as an issue tracker but evolved into an operating system for engineering teams
- Used by OpenAI, Ramp, Vercel, and thousands of modern software companies
- Focus on speed, clarity, and removing friction for individual contributors (ICs)

### [Early AI Journey (2023)](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=88s)
- Spun up internal skunkworks team in early 2023 (GPT-3 era)
- Initial focus on summarization and similarity using embeddings
- No one on team had AI experience - learning as they went
- Realized solid search foundation was critical for AI features

**Technical Stack Decision:**
- Evaluated many vector database startups (Pinecone, etc.)
- Chose pragmatic approach: OpenAI embeddings stored in PG vector on GCP
- "Most classic Linear decision ever" - prioritized solid, proven technology

### [First AI Features Shipped](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=169s)
- **Similar Issues v1:** Simple cosine similarity matching (admittedly "naive" in retrospect)
- **Natural Language Filters:** Convert queries like "bugs assigned to me in last two weeks that are closed" into filters - very useful but hidden
- **Slack to Issue Creation:** Automatically creates well-formed issues from Slack threads seamlessly
- **No Co-pilot:** Tried but quality didn't meet their bar - unclear if limitation was team imagination or model capability

**Philosophy:**
- Small, pragmatic value adds - not "slapping AI in your face"
- Users appreciated seamless, hidden AI features vs. toothbrushes claiming to have AI

### [2024 Turning Point](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=273s)
- End of 2024 felt like a major shift
- O3 planning/reasoning models, multimodal APIs, million-token context windows, DeepSeek
- Experiments became "lot less brittle" and "actually felt smart"
- Team started seeing how deep AI integration could go

### [Rebuilt Search Foundation](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=315s)
- Moved to **Turbopuffer** for hybrid search (highly recommended)
- Switched embeddings from OpenAI to **Cohere** (better for their domain)
- Backfilling hundreds of millions of embedding rows took weeks
- Just finished rolling out in last two weeks before the talk

### [Product Intelligence Feature](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=378s)
- Similar Issues v2 - much more sophisticated
- Pipeline using: query rewriting, hybrid search, reranking, deterministic rules
- Outputs: map of issue relationships with explanations of WHY they're related
- Surfaces: suggested labels, suggested assignees, possible duplicates
- Explains why certain people/projects might be right for an issue
- Critical for companies like OpenAI handling thousands of tickets

### [Customer Feedback Analysis](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=449s)
- Analyzes hundreds/thousands of customer feedback pieces
- Head of product said it "beats 90% of PM candidates in interview process"
- Suggests how to split up projects and what features to create
- Helps decide what to build from customer feedback

### [Daily/Weekly Pulse](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=503s)
- Synthesizes all workspace updates into a summary
- Produces **audio podcast version** - can listen on mobile during commute
- Not yet RSS feed but planned
- Great for catching up on team activity

### [Issue from Video](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=549s)
- Customers drop video recordings of bugs
- Analyzes video, figures out reproduction steps, creates issue automatically
- Seamless but powerful time-saver

### [Agent Platform Launch](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=584s)
- Launched platform two weeks ago (from talk date)
- **Philosophy:** Agents as "infinitely scalable cloud-based teammates"
- Linear already orchestrates humans well - agents should live in same place
- Agents are first-class users with identity, history, full audit trail

**Key Integrations Demoed:**

### [Codegen Agent](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=629s)
- Assign or mention like any user
- Produces plans and PRs
- Demo showed 4-minute process sped up
- Can interact from Linear, Slack, or other tools
- Can interrupt agents mid-work

### [Bucket Agent - Feature Flagging](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=689s)
- Mention to create feature flags
- Can roll out flags, check status
- Can give complex multi-step commands: "create flag, roll out to 30% of users"

### [Charlie Agent - Code Analysis](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=724s)
- Good at creating plans and root cause analysis
- Can analyze Sentry issues attached to Linear tickets
- Looks at recent commits and codebase
- Identifies possible causes and regression reasons
- Saves engineers time on investigation

### [Future UI for Agents](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=768s)
- Currently agents live in comment threads
- Building dedicated surfaces coming in couple weeks
- Will show agent observations, tool calls, thinking process
- "Kind of better than humans because you can see what they're thinking"
- Ability to interrupt agents
- Consistent interface across workspace

**Intercom Finn Agent Integration:**
- Coming soon
- Example: "Hey Finn, I fixed this bug, go reply to hundred customers who reported it"
- Massive time savings

### [Impact on Development](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=840s)
- Giant backlogs may become obsolete - "no excuse for that anymore"
- Can assign entire backlog to agents for first pass
- Maybe 50% fixed by end of week
- Build more, higher quality, faster with agents handling grunt work

### [Platform Architecture](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=879s)
- Agents are first-class users with identity and history
- Install via OAuth, admins manage access
- Work fully transparently
- **Mature GraphQL API** enables agents to do anything humans can
- **Granular scopes** for permissions
- **New webhooks** specific to agent events (replies, triggers, assignments)
- **Additional scopes** to opt into mentionable/assignable status

**Coming Soon:**
- New SDK to make integration easier (currently possible on existing API but requires more work)
- Abstraction layer/"sugar" for very easy platform integration

### [Best Practices for Agent Developers](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=976s)

**1. Respond Quickly & Precisely** ([16:41](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=1001s))
- Acknowledge triggers immediately (many use emoji reactions)
- Reassure user that agent understood the request
- Example: "@codegen take care of this" → "I will produce a PR for [specific thing]"

**2. Inhabit the Platform** ([17:21](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=1041s))
- Agents aren't "Linear agents" - they're cloud agents that interact through Linear
- Use the language and conventions of each platform
- In Linear: move issues to "in progress" when working (like human teammates)
- Don't confuse platform conventions

**3. Natural Behavior** ([18:13](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=1093s))
- If someone replies in a thread, agent should respond without being mentioned again
- Behave like a natural conversation participant

**4. Don't Be Clever** ([18:33](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=1113s))
- **Clarify intent before acting**
- Avoid one-shot attempts
- Common pattern: Form a plan, communicate it upfront, get clarification, then act
- Better to confirm than assume

**5. Add Value, Be Concise** ([19:00](https://www.youtube.com/watch?v=UG9IAdmi2Dg&t=1140s))
- Don't splat raw LLM output into comments/issues
- Be concise and useful
- Act like a good teammate would
- Ask: "What would a human do in this situation?"

---

## Key Takeaways

1. **Pragmatic AI adoption:** Linear started with simple, hidden features that added real value without being flashy
2. **Search is foundational:** Almost every AI feature needs good search/retrieval first
3. **Quality bar matters:** They chose not to ship features (like copilot) that didn't meet standards
4. **Agents as teammates:** The paradigm shift is treating agents as first-class team members, not separate tools
5. **Platform thinking:** Linear positioned themselves as the coordination layer for human-agent collaboration
6. **Transparency wins:** Agents should work openly with full audit trails and visible reasoning
7. **Backlog implications:** AI agents may fundamentally change what "acceptable backlog size" means

---

**Last Updated:** January 2, 2026
