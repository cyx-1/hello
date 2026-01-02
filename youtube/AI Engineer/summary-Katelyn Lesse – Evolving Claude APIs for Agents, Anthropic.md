# Katelyn Lesse – Evolving Claude APIs for Agents, Anthropic

**Video URL:** https://www.youtube.com/watch?v=aqW68Is_Kj4

---

## Executive Summary

Katelyn Lesse, who leads the Claude developer platform team at Anthropic, presents how Anthropic is evolving its platform to help developers build powerful agentic systems using Claude. The talk focuses on three core pillars: harnessing Claude's capabilities through API features, managing Claude's context window effectively, and giving Claude computational autonomy. Using Claude Code as a primary example throughout, she demonstrates how these platform improvements translate to real-world agent performance, including a 39% performance boost from combining memory and context editing features.

---

## Main Topics

### [Introduction and Overview](https://www.youtube.com/watch?v=aqW68Is_Kj4&t=23s)
**Timestamp: [00:23 - 02:00]**

- Katelyn Lesse introduces herself as the lead of Claude's developer platform team at Anthropic
- Target audience: developers building agents using LLM APIs
- Focus on helping developers "raise the ceiling of intelligence" - getting the best performance from Claude
- Claude Code serves as the main example throughout the presentation
- Three main areas of platform evolution:
  1. Harnessing Claude's capabilities
  2. Managing Claude's context window
  3. Giving Claude a computer to work autonomously

### [Harnessing Claude's Capabilities](https://www.youtube.com/watch?v=aqW68Is_Kj4&t=129s)
**Timestamp: [02:09 - 03:51]**

**Extended Thinking Feature:**
- Claude's performance scales with the amount of time given to reason through problems
- Exposed as an API feature with customizable "thinking budget" (token limit for reasoning)
- Developers can choose between quick answers or deeper reasoning for complex tasks
- Claude Code uses this to decide when to think longer (e.g., debugging complex systems vs. quick responses)

**Tool Use:**
- Claude is trained to reliably call tools and pass correct arguments
- Built-in tools (like web search) available through API
- Custom tools supported - just define name, description, and input schema
- Claude Code leverages this extensively: reads files, searches files, writes files, reruns tests
- Critical for agentic workflows with many tool calls

### [Managing Claude's Context Window](https://www.youtube.com/watch?v=aqW68Is_Kj4&t=237s)
**Timestamp: [03:57 - 07:39]**

**Why Context Management Matters:**
- Getting the right context at the right time is critical for maximizing performance
- Particularly complex for coding agents with technical designs, entire codebases, instructions, and tool calls
- Goal: Keep context optimized over time

**Model Context Protocol (MCP):**
- Introduced a year ago as a standardized way for agents to interact with external systems
- Strong community adoption
- Enables agents to access information and tools outside their context window
- Examples for Claude Code: GitHub, Sentry integrations
- Significantly better performance than agents limited to in-window context

**Memory Tool:**
- Helps keep context outside the window that Claude can pull back when needed
- First iteration: client-side file system (users control their data)
- Claude autonomously decides what to store and when to retrieve
- Examples for Claude Code: codebase patterns, git workflow preferences
- Stores away information and retrieves only when relevant

**Context Editing:**
- Clears out irrelevant content from the window
- First iteration: clearing old tool results
- Tool results can be large and take up significant space
- Past tool results often not relevant for future responses
- Claude Code calls hundreds of tools - files read, etc. take up space
- **Performance Impact: 39% performance improvement** when combining memory tool with context editing

**Larger Context Windows:**
- Some Claude models support up to 1 million token context windows
- Combining larger windows with context management tools maximizes performance
- Claude is being trained to understand its context window status (room to run vs. almost full)
- Claude responds accordingly based on available context space

### [Giving Claude a Computer](https://www.youtube.com/watch?v=aqW68Is_Kj4&t=459s)
**Timestamp: [07:39 - 10:01]**

**Philosophy:**
- Discourse around agent harnesses: how much scaffolding? How opinionated?
- Anthropic's view: If Claude can write code AND run that code, it can accomplish anything
- Challenge: Infrastructure and expertise needed to enable this safely

**Claude Code on Web and Mobile:**
- Recent launch presented interesting challenges
- Locally: Claude Code uses the user's machine
- On web/mobile: Need infrastructure for Claude to work when users walk away
- Key problems solved:
  1. Secure environment for writing and running unapproved code
  2. Container orchestration at scale
  3. Session persistence (sessions continue when users walk away)

**Code Execution Tool:**
- Released in the API
- Allows Claude to write and run code in secure sandboxed environments
- Platform handles containers, security - running on Anthropic's servers
- Developers don't have to think about infrastructure
- Examples: "Make an animation more sparkly" - Claude can write and immediately run the code
- **Vision: Future of agents is models working autonomously within sandbox environments**

### [Agent Skills](https://www.youtube.com/watch?v=aqW68Is_Kj4&t=609s)
**Timestamp: [10:09 - 11:23]**

**What Are Skills:**
- Folders of scripts, instructions, and resources
- Claude has access and can decide to run within sandbox environment
- Decision based on user request and skill description
- Claude knows when to pull skills into context

**How Skills Work with Other Tools:**
- MCP provides access to tools and context
- Skills provide the expertise to use those tools and context effectively
- Example for Claude Code: Web design skill
  - When building landing pages for new products/features
  - Ensures adherence to design system and established patterns
  - Claude recognizes "build a landing page" triggers web design skill

**Additional Information:**
- Barry and Mahesh from Anthropic team giving deeper talk on skills the next day

### [Future Platform Evolution](https://www.youtube.com/watch?v=aqW68Is_Kj4&t=715s)
**Timestamp: [11:55 - 12:44]**

**Three Areas of Continued Development:**

1. **Capability Exposure:**
   - As Claude gains new capabilities and improves existing ones
   - API will evolve to expose these capabilities
   - Goal: Keep developers on the frontier with best Claude has to offer

2. **Context and Memory Evolution:**
   - Enhanced tools for Claude to decide:
     - What to pull into context
     - What to store for later
     - What to clean out of context window
   - Improving autonomous context management

3. **Agent Infrastructure:**
   - Biggest challenge: orchestration, secure environments, sandboxing
   - Continued investment in infrastructure to support "give Claude a computer" vision
   - Making these capabilities ready for developer use

### [Hiring and Closing](https://www.youtube.com/watch?v=aqW68Is_Kj4&t=764s)
**Timestamp: [12:44 - 13:07]**

- Anthropic is actively hiring and growing the team
- Looking for people who love building delightful developer products
- Roles across product design, DevRel, and other functions
- Invitation to reach out if interested

---

## Key Takeaways

1. **Three Pillars of Claude Platform**: Harnessing capabilities (extended thinking, tool use), managing context (MCP, memory, context editing), and providing computational autonomy (code execution, skills)

2. **Significant Performance Gains**: 39% improvement when combining memory tools with context editing demonstrates the importance of proper context management

3. **Vision for Agent Future**: Models should work autonomously within sandbox environments, with platforms providing the infrastructure (security, orchestration, persistence)

4. **Claude Code as Reference Implementation**: Used throughout as a practical example of how platform features enable complex agentic systems

5. **Developer-Centric Approach**: Anthropic focuses on providing API features that match Claude's trained capabilities, making advanced functionality accessible to developers

6. **Ecosystem Growth**: MCP adoption by community, skills system for domain expertise, and infrastructure investments signal long-term commitment to agent development platform
