# Ship Production Software in Minutes, Not Months — Eno Reyes, Factory

**Video URL:** https://www.youtube.com/watch?v=iheWKg2Tkrk

---

## Executive Summary

Eno Reyes, from Factory, presents a vision for agent-native software development that goes beyond incremental improvements to existing tools. He argues that true AI transformation requires delegating the majority of software lifecycle tasks to agents through a platform with intuitive task management, centralized context from all engineering tools, reliable agent outputs, and infrastructure supporting thousands of parallel agents. The talk demonstrates how Factory's "droids" handle everything from planning and design to incident response, emphasizing that the bottleneck isn't LLM capability but missing context. Rather than replacing engineers, agents amplify their capabilities by handling the "inner loop" while developers focus on higher-leverage "outer loop" activities like orchestration and system design.

---

## Topics and Key Points

### [Introduction and Vision](https://www.youtube.com/watch?v=iheWKg2Tkrk&t=0s)
**[00:00 - 02:50]**

- Eno started working on LLMs 2.5 years ago when GPT-3.5 launched and agentic systems became possible
- Factory believes agent-driven development will radically change software development
- Current approaches are mostly incremental improvements - adding AI layers on top of 20-year-old tools designed for humans
- Quote analogy: Henry Ford's "If I asked people what they wanted, they would have said faster horses"
- Organizations need to delegate the majority of software lifecycle tasks to agents to access AI's true power
- Four key requirements for agent-native development:
  - Intuitive interface for managing and delegating tasks
  - Centralized context from all engineering tools and data sources
  - Agents that consistently produce reliable, high-quality outputs
  - Infrastructure supporting thousands of agents working in parallel

### [Agent-Native Development vs. Vibe Coding](https://www.youtube.com/watch?v=iheWKg2Tkrk&t=170s)
**[02:50 - 03:50]**

- Andre Karpathy's "English is the new programming language" captured an exciting moment
- Twitter suggests you can "vibe code your way to anything" but this doesn't solve hard problems
- You can't vibe code a legacy Java 7 app running 5% of global bank transactions
- Agents should not replace human ingenuity - they're "climbing gear" and building production software is like scaling Mount Everest
- Better tools make the climb more accessible, but we still need expertise to leverage them effectively

### [Demo: Droid Task Execution](https://www.youtube.com/watch?v=iheWKg2Tkrk&t=230s)
**[03:50 - 04:52]**

- Demo shows delegating a task to Factory's "droid" agentic system
- The droid ingests the task and grounds itself in the environment
- Uses tools to search codebase, determine git branch, check available resources
- Looks through recent codebase changes and memories of interactions with users and across the organization
- Comes back with a plan and asks for clarification before proceeding
- Agents should question requirements and make developers better, not just accept instructions at face value
- After clarification, the droid executes: writes code, runs pre-commit hooks, lints, and generates a PR that passes CI

### [Context is King](https://www.youtube.com/watch?v=iheWKg2Tkrk&t=292s)
**[04:52 - 06:30]**

- Fundamental truth: AI tools are only as good as the context they receive
- Prompt engineering is really about mentally modeling an alien intelligence with a slice of real-world context
- After investigating thousands of droid-assisted sessions, AI most often fails not because LLMs aren't good enough, but because it's missing crucial context
- Better models will help, but the real solution is getting better at providing missing context
- LLMs don't know about your morning standup, meetings, or whiteboard discussions - you must transcribe notes, upload photos
- Think of AI not as tools but as something between a co-worker and a platform
- Need platforms that integrate natively with all data sources and agents that can actually use that context
- This drives the transition to agent-native development

### [Planning and Design with Agents](https://www.youtube.com/watch?v=iheWKg2Tkrk&t=390s)
**[06:30 - 07:40]**

- In agent-native development, agents are used at every stage, not just code writing
- The hardest thing about software development isn't the code - it's figuring out exactly what to build
- Demo shows droid finding up-to-date information about a new model release and integrating it into an existing chat application
- Leverages internet search, codebase knowledge, organizational memory of product goals, and technical architecture from design docs
- Planning with AI is fundamentally different from planning alone
- It's not "please build this" but delegating groundwork and research to AI agents, then using collaborative platforms to explore possibilities together
- Results can be exported to Notion, Confluence, Jira with no setup

### [Standardizing Organizational Thinking](https://www.youtube.com/watch?v=iheWKg2Tkrk&t=460s)
**[07:40 - 09:59]**

- The real unlock for AI transformation is standardizing how your organization thinks
- Example: Planning a cloud development environment feature at Factory
  - Collected 3 months of user transcripts from enterprises and individuals
  - Factory transcribes every single interaction and meeting
  - Combined notes with droid having access to their architecture
  - Used Granola notes from ad hoc engineering meetings
  - Asked the knowledge droid to find patterns in customer feedback, highlight technical constraints
  - Generated 4-5 intermediate documents used to iterate on final PRD
- PRDs can be turned into roadmaps with tools to create Linear/Jira tickets and epics
- Work can be parallelized among multiple code droids
- Software evolution: moving from executing to orchestrating systems that work on our behalf

### [Documentation as Knowledge Base](https://www.youtube.com/watch?v=iheWKg2Tkrk&t=599s)
**[09:59 - 10:49]**

- Important artifacts: PRDs, design docs, RCA templates, quarterly roadmaps, meeting transcriptions
- What's normally seen as a burden becomes a knowledge base and map for droids to learn and imitate how your team thinks
- Documentation and process is a conversation with both future developers and future AI systems
- Communicating the "why" behind decisions provides crucial context
- This creates a huge lift in agents' ability to work the way your team actually works

### [Site Reliability Engineering and Incident Response](https://www.youtube.com/watch?v=iheWKg2Tkrk&t=649s)
**[10:49 - 13:43]**

- While you can't fully automate all SRE and RCA work today, there's a different AI agent-driven approach
- Demo shows droid taking a Sentry incident and converting it to full RCA and mitigation plan
- Traditional incident response is solving a puzzle with pieces scattered across dozens of systems: logs, metrics, historical context, team knowledge
- Droids fundamentally change this by pulling context from system logs, past incidents, runbooks in Notion/Confluence, team discussions from Slack
- Condenses search effort from hours to minutes
- Acceptable time to act should be zero - the moment an incident happens, a droid should tell you what happened and how to fix it
- With user and organization-level memory, builds a model of team's response patterns and common issues
- Not just generating runbooks for one incident, but creating new processes to solve these issues
- Can generate runbooks for new patterns, update response workflows, capture team knowledge automatically
- Part of a larger learning cycle when agents are integrated into workflow
- Results: Cut incident response time in half, reduce repeat incidents, improve team collaboration
- Shift from reactive to predictive operations by seeing patterns across entire operational history
- Each incident becomes an opportunity to make the entire system more reliable

### [Amplifying Engineers, Not Replacing Them](https://www.youtube.com/watch?v=iheWKg2Tkrk&t=823s)
**[13:43 - 14:47]**

- AI agents are not replacing software engineers - they're significantly amplifying individual capabilities
- Best developers are spending far less time in IDE writing lines of code - it's not high leverage
- They're managing agents that can do multiple things at once, organizing systems, building patterns
- Moving from "inner loop" of software development to "outer loop"
- These developers aren't worried about agents taking their jobs - they're too busy using agents to become better
- The future belongs to developers who understand how to work with agents, not those who hope AI will just do the work
- The skill that matters most is not technical knowledge or ability to optimize a specific system, but ability to think clearly and communicate effectively with both humans and AI

### [Try Factory Droids + Enterprise Considerations](https://www.youtube.com/watch?v=iheWKg2Tkrk&t=887s)
**[14:47 - 15:59]**

- QR code available for conference attendees to sign up for account
- Mobile experience not optimized yet (droids are working on it) - recommend using laptop
- 20 million free tokens credited to account
- Factory is first and foremost an enterprise platform
- Important enterprise questions: security, audit logs, responsibility when agents make mistakes (e.g., rm -rf recursive)
- Droids don't do that, but whose responsibility would it be?
- For security professionals, consider: ownership, auditability, indemnification
- "YOLO mode" is probably not the best thing to run inside your enterprise
- Encourages checking out the controls Factory has built
- Contact available via email for questions

---

**Last Updated:** January 3, 2026
