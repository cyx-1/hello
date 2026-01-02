# Don't Build Agents, Build Skills Instead – Barry Zhang & Mahesh Murag, Anthropic

**Video URL:** https://www.youtube.com/watch?v=CEvIs9y1uog

---

## Executive Summary

Barry Zhang and Mahesh Murag from Anthropic present a paradigm shift in how we think about AI agents. Rather than building specialized agents for each domain, they advocate for building "skills" - organized collections of files that package procedural knowledge for general-purpose agents. Since launching five weeks before this talk, thousands of skills have been created across foundational capabilities, third-party integrations, and enterprise-specific use cases. The talk introduces skills as simple folders containing scripts and instructions that agents can progressively load, making agents more expert in specific domains while maintaining a thin, scalable architecture centered on code execution. The vision is an ecosystem where skills become the "applications" layer on top of agent "operating systems," enabling continuous learning and knowledge sharing across organizations and communities.

---

## Main Topics

### [Introduction and Context](https://www.youtube.com/watch?v=CEvIs9y1uog&t=22s)
**Time:** [00:22](https://www.youtube.com/watch?v=CEvIs9y1uog&t=22s) - [00:59](https://www.youtube.com/watch?v=CEvIs9y1uog&t=59s)

- Agents are now used daily but still have gaps - they lack domain expertise despite having intelligence and capabilities
- Since the last talk, MCP became the standard for agent connectivity, Claude Code launched, and the Claude Agent SDK now provides production-ready agents
- The new paradigm involves tighter coupling between models and runtime environments

### [Code as Universal Interface](https://www.youtube.com/watch?v=CEvIs9y1uog&t=77s)
**Time:** [01:17](https://www.youtube.com/watch?v=CEvIs9y1uog&t=77s) - [01:50](https://www.youtube.com/watch?v=CEvIs9y1uog&t=110s)

- Key insight: "Code is all we need" - code is not just a use case but the universal interface to the digital world
- Initially thought different domains would need separate agents with custom tools and scaffolding
- Realized the underlying agent can be more universal than expected
- Claude Code turned out to be a general-purpose agent capable of tasks beyond just coding

### [The Domain Expertise Problem](https://www.youtube.com/watch?v=CEvIs9y1uog&t=136s)
**Time:** [02:16](https://www.youtube.com/watch?v=CEvIs9y1uog&t=136s) - [02:56](https://www.youtube.com/watch?v=CEvIs9y1uog&t=176s)

- Analogy: Who do you want doing your taxes - a 300 IQ genius or an experienced tax professional?
- Agents today are brilliant but lack expertise - they can't absorb domain knowledge well and don't learn over time
- Thin scaffolding (bash + file system) is scalable, but agents quickly run into the domain expertise problem
- Agents can do amazing things with proper guidance but often miss important context upfront

### [What are Skills?](https://www.youtube.com/watch?v=CEvIs9y1uog&t=180s)
**Time:** [03:00](https://www.youtube.com/watch?v=CEvIs9y1uog&t=180s) - [04:59](https://www.youtube.com/watch?v=CEvIs9y1uog&t=299s)

- **Definition**: Organized collections of files that package composable procedural knowledge for agents
- In other words: they're folders - this simplicity is deliberate
- Works with existing tools: version in Git, share via Google Drive, zip and distribute to teams
- Can include scripts as tools - advantages over traditional tools:
  - Self-documenting
  - Modifiable by the agent
  - Live in file system until needed (not always in context window)
- Example: Claude writing the same Python script repeatedly for styling slides - just save it as a tool for future use

### [Progressive Disclosure and Context Management](https://www.youtube.com/watch?v=CEvIs9y1uog&t=263s)
**Time:** [04:23](https://www.youtube.com/watch?v=CEvIs9y1uog&t=263s) - [04:59](https://www.youtube.com/watch?v=CEvIs9y1uog&t=299s)

- Skills are progressively disclosed to protect context window
- At runtime, only metadata is shown to indicate the skill exists
- When needed, agent reads skill.md containing core instructions and directory structure
- This enables hundreds of skills to be truly composable without overwhelming context

### [The Growing Skills Ecosystem](https://www.youtube.com/watch?v=CEvIs9y1uog&t=301s)
**Time:** [05:01](https://www.youtube.com/watch?v=CEvIs9y1uog&t=301s) - [05:21](https://www.youtube.com/watch?v=CEvIs9y1uog&t=321s)

- Five weeks post-launch: thousands of skills created
- Three main categories:
  1. **Foundational skills** - new general or domain-specific capabilities
  2. **Third-party skills** - partner integrations
  3. **Enterprise skills** - company and team-specific implementations

### [Foundational Skills Examples](https://www.youtube.com/watch?v=CEvIs9y1uog&t=321s)
**Time:** [05:21](https://www.youtube.com/watch?v=CEvIs9y1uog&t=321s) - [05:57](https://www.youtube.com/watch?v=CEvIs9y1uog&t=357s)

- Anthropic built document skills enabling Claude to create and edit professional office documents
- Cadence built scientific research skills:
  - EHR data analysis
  - Better use of Python bioinformatics libraries
  - New capabilities Claude didn't have before

### [Third-Party Skills Examples](https://www.youtube.com/watch?v=CEvIs9y1uog&t=357s)
**Time:** [05:57](https://www.youtube.com/watch?v=CEvIs9y1uog&t=357s) - [06:31](https://www.youtube.com/watch?v=CEvIs9y1uog&t=391s)

- **Browserbase**: Skill for their open-source browser automation tool Stagehand - enables Claude to navigate web and use browsers more effectively
- **Notion**: Skills to help Claude understand workspaces and perform deep research across entire Notion environments
- Partners building skills to help Claude work better with their software and products

### [Enterprise Skills Adoption](https://www.youtube.com/watch?v=CEvIs9y1uog&t=391s)
**Time:** [06:31](https://www.youtube.com/watch?v=CEvIs9y1uog&t=391s) - [07:30](https://www.youtube.com/watch?v=CEvIs9y1uog&t=450s)

- Most excitement and traction within large enterprises
- Fortune 100 companies using skills to teach agents:
  - Organizational best practices
  - Unique ways they use bespoke internal software
- Developer productivity teams (serving thousands or tens of thousands of developers) using skills to:
  - Deploy agents like Claude Code
  - Teach code style best practices
  - Enforce internal development standards
- Common thread: anyone can create skills that give agents new capabilities

### [Emerging Trends in Skills](https://www.youtube.com/watch?v=CEvIs9y1uog&t=450s)
**Time:** [07:30](https://www.youtube.com/watch?v=CEvIs9y1uog&t=450s) - [08:10](https://www.youtube.com/watch?v=CEvIs9y1uog&t=490s)

**Trend 1: Increasing Complexity**
- Basic skills: Simple skill.md files with prompts and instructions
- Advanced skills now package: software, executables, binaries, files, code, scripts, assets
- Build time evolving from minutes/hours to potentially weeks/months (like traditional software)

### [Skills and MCP Servers](https://www.youtube.com/watch?v=CEvIs9y1uog&t=490s)
**Time:** [08:10](https://www.youtube.com/watch?v=CEvIs9y1uog&t=490s) - [08:38](https://www.youtube.com/watch?v=CEvIs9y1uog&t=518s)

**Trend 2: Complementing MCP Ecosystem**
- Skills orchestrate workflows using multiple MCP tools stitched together
- Division of responsibilities:
  - **MCP**: Provides connection to outside world
  - **Skills**: Provide the expertise
- Together they enable more complex interactions with external data and connectivity

### [Non-Technical Skill Builders](https://www.youtube.com/watch?v=CEvIs9y1uog&t=518s)
**Time:** [08:38](https://www.youtube.com/watch?v=CEvIs9y1uog&t=518s) - [09:08](https://www.youtube.com/watch?v=CEvIs9y1uog&t=548s)

**Trend 3: Skills Built by Non-Technical People**
- People in finance, recruiting, accounting, legal, and other functions building skills
- Early validation that skills make general agents more accessible for non-coding work
- Extends agents to day-to-day work across diverse functions

### [General Agent Architecture](https://www.youtube.com/watch?v=CEvIs9y1uog&t=548s)
**Time:** [09:08](https://www.youtube.com/watch?v=CEvIs9y1uog&t=548s) - [10:09](https://www.youtube.com/watch?v=CEvIs9y1uog&t=609s)

The emerging architecture converges on:
1. **Agent loop**: Manages model's internal context and token flow
2. **Runtime environment**: Provides file system and ability to read/write code
3. **MCP servers**: Tools and data from outside world for relevance and effectiveness
4. **Skills library**: Hundreds or thousands of skills pulled into context only when needed for specific tasks

**Result**: Agent capabilities in new domains = right MCP servers + right library of skills

### [Anthropic's Vertical Deployments](https://www.youtube.com/watch?v=CEvIs9y1uog&t=609s)
**Time:** [10:09](https://www.youtube.com/watch?v=CEvIs9y1uog&t=609s) - [10:38](https://www.youtube.com/watch?v=CEvIs9y1uog&t=638s)

- Five weeks after skills launch, immediately launched new offerings in:
  - Financial services
  - Life sciences
- Each came with curated sets of MCP servers and skills
- Pattern: MCP server + skill set = domain-specific agent effectiveness

### [Future: Treating Skills Like Software](https://www.youtube.com/watch?v=CEvIs9y1uog&t=638s)
**Time:** [10:38](https://www.youtube.com/watch?v=CEvIs9y1uog&t=638s) - [11:14](https://www.youtube.com/watch?v=CEvIs9y1uog&t=674s)

As skills become more complex, Anthropic wants to support builders with:

**Testing and Evaluation**
- Ensure agents load and trigger skills at the right time
- Verify output quality matches expectations

**Versioning**
- Track skill evolution clearly
- Maintain clear lineage over time as agent behavior evolves

### [Skill Dependencies and Composability](https://www.youtube.com/watch?v=CEvIs9y1uog&t=674s)
**Time:** [11:26](https://www.youtube.com/watch?v=CEvIs9y1uog&t=686s) - [11:51](https://www.youtube.com/watch?v=CEvIs9y1uog&t=711s)

**Explicit Dependencies**
- Skills that can refer to other skills, MCP servers, and packages
- Makes agents more predictable across different runtime environments
- Composability of multiple skills enables more complex and relevant agent behavior

**Goal**: Make skills easier to build and integrate into agent products (not just Claude)

### [Vision: Sharing and Distribution](https://www.youtube.com/watch?v=CEvIs9y1uog&t=724s)
**Time:** [12:04](https://www.youtube.com/watch?v=CEvIs9y1uog&t=724s) - [13:20](https://www.youtube.com/watch?v=CEvIs9y1uog&t=800s)

**Organizational Level**
- Collecting, collective, and evolving knowledge base of capabilities
- Curated by people and agents inside organizations
- As you interact with an agent and give feedback, it gets better
- All agents in your team/org benefit from improvements
- New team members get agents that already know team practices and priorities

**Community Level**
- Compounding value extends beyond your organization
- Skills built by someone across the world make your agent more capable
- Similar to how MCP servers built by others benefit your agents

### [Continuous Learning Through Skills](https://www.youtube.com/watch?v=CEvIs9y1uog&t=800s)
**Time:** [13:20](https://www.youtube.com/watch?v=CEvIs9y1uog&t=800s) - [14:35](https://www.youtube.com/watch?v=CEvIs9y1uog&t=875s)

**Design for Learning**
- Skills designed specifically as concrete steps toward continuous learning
- Standardized format guarantees: anything Claude writes can be used efficiently by future versions

**Three Phases of Skill Usage**

1. **Starting Out**
   - Transferable learning through standardized format

2. **Building Context**
   - Memory becomes more tangible (procedural knowledge for specific tasks)
   - Not everything - just what's useful for task execution

3. **Long-term Use**
   - Flexibility matters: acquire new capabilities instantly, evolve as needed, drop obsolete ones
   - In-context learning more cost-effective for daily-changing information
   - **Goal**: Claude on day 30 significantly better than Claude on day 1
   - Skill creator skill already enables Claude to create skills today

### [Computing Analogy](https://www.youtube.com/watch?v=CEvIs9y1uog&t=875s)
**Time:** [14:35](https://www.youtube.com/watch?v=CEvIs9y1uog&t=875s) - [15:42](https://www.youtube.com/watch?v=CEvIs9y1uog&t=942s)

**The Stack Comparison**

| Computing Layer | AI Equivalent | Characteristics |
|----------------|---------------|-----------------|
| **Processors** | **Models** | Massive investment, immense potential, limited utility alone |
| **Operating Systems** | **Agent Runtime** | Orchestrates processes, resources, and data; manages token flow efficiently |
| **Applications** | **Skills** | Where creativity happens; millions of developers encoding domain expertise |

**Key Insight**
- Few companies build processors and operating systems
- Millions of developers build applications that encode domain expertise and unique points of view
- Skills open up the "application layer" for everyone
- This is where we solve concrete problems for ourselves, each other, and the world - just by putting stuff in folders

### [Conclusion and Call to Action](https://www.youtube.com/watch?v=CEvIs9y1uog&t=942s)
**Time:** [15:42](https://www.youtube.com/watch?v=CEvIs9y1uog&t=942s) - [16:01](https://www.youtube.com/watch?v=CEvIs9y1uog&t=961s)

**Key Takeaways**
- Converging on general architecture for general agents
- Skills = new paradigm for shipping and sharing new capabilities
- **Main message**: Stop rebuilding agents, start building skills instead
- Invitation to work with Anthropic and start building skills

---

## Key Insights

1. **Paradigm Shift**: From building specialized agents for each domain to building skills for general-purpose agents
2. **Simplicity by Design**: Skills are just folders - intentionally simple to enable anyone (human or agent) to create and use them
3. **Progressive Disclosure**: Context window protection through metadata-first loading enables hundreds of composable skills
4. **Complementary Ecosystems**: Skills (expertise) + MCP servers (connectivity) = powerful agent capabilities
5. **Democratization**: Non-technical users building skills validates accessibility of the approach
6. **Continuous Learning**: Standardized format enables transferable learning and agent improvement over time
7. **Network Effects**: Skills create compounding value within organizations and across the broader community
8. **Application Layer**: Skills represent the "applications" layer in the agent computing stack, where domain expertise and creativity flourish

---

**Last Updated:** January 1, 2026
