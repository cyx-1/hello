# AX is the only Experience that Matters - Ivan Burazin, Daytona

**Video URL:** https://www.youtube.com/watch?v=e9sLVMN76qU

---

## Executive Summary

Ivan Burazin from Daytona argues that Agent Experience (AX) is the new critical paradigm for developer tools. With 37% of Y Combinator startups building agents as products and AI writing 95% of code for 25% of YC companies, the future demands tools designed for autonomous agent operation—not human-assisted workflows. Most current developer tools break when humans are removed from the loop. Daytona addresses this by building an agent-native runtime with features like declarative image builders, shared volumes, and parallel execution capabilities. The key insight: if your tool requires human intervention, you're building for the past.

---

## Topics

### [Introduction: The Agent Future](https://www.youtube.com/watch?v=e9sLVMN76qU&t=18s)
**Key Points:**
- The number of agents will exceed humans to the power of n, creating exponentially more agents than people
- 25% of YC startups report AI writes 95% of their code
- 37% of latest YC batch are building agents as their core product (not co-pilots or autocomplete)
- Most tools built for agents today break the moment you remove humans from the loop

### [Defining Agent Experience (AX)](https://www.youtube.com/watch?v=e9sLVMN76qU&t=121s)
**Key Points:**
- Matt from Netlify coined the term "Agent Experience" as evolution of UX, CX, and DX
- Definition: How easily can agents access, understand, and operate within digital environments to achieve user-defined goals
- Tools for humans are "building for the past" - agents will be the primary developers
- Need to rethink: what happens if there are no humans to click buttons, debug errors, or intervene?

### [Current AX Implementations](https://www.youtube.com/watch?v=e9sLVMN76qU&t=187s)
**Key Points:**
- **Seamless Authentication**: Companies like Arcade solve agent login challenges - agents can fall back to users for auth without exposing passwords
- **Agent-Readable Docs**: Stripe's approach - append .md to any doc URL for clean markdown. The llm.txt standard makes docs easily consumable
- **API-First Design**: Most critical element - agents need machine-native interfaces (APIs) to access functionality. Companies like Neon, Netlify, and Supabase excel at this

### [The Missing Piece: Autonomy](https://www.youtube.com/watch?v=e9sLVMN76qU&t=344s)
**Key Points:**
- Current AX definition missing key word: "autonomously"
- Agents must autonomously access, understand, and operate without falling back to humans
- If your agent always needs human intervention, you're still "porting for the past"
- Swyx challenged that AX is just a wrapper around DX - the autonomous requirement differentiates it

### [Ivan's Background and Daytona's Mission](https://www.youtube.com/watch?v=e9sLVMN76qU&t=419s)
**Key Points:**
- Started in early 2000s building data centers, HP servers, VMware infrastructure
- Created first browser-based IDE in 2009 (pre-dating Replit by 15 years)
- Led developer experience at Infobip (multi-billion dollar Twilio competitor)
- Daytona: secure, elastic infrastructure for AI-generated code - "agent-native runtime"
- Provides sandboxes for agents to run code, data analysis, RL, computer use, even gaming

### [Building Agent-Native: Speed and APIs](https://www.youtube.com/watch?v=e9sLVMN76qU&t=547s)
**Key Points:**
- **Speed**: 27-millisecond spin-up time for interactive agent workflows
- **API-First**: Agents can turn machines on/off, clone, delete via API
- **Headless Tools**: Pre-loaded with file explorer, git client, LSP, terminal - agents don't parse terminal output, they use structured APIs
- These align with basic AX principles of fast access and machine-native interfaces

### [New Agent Primitives: Declarative Image Builder](https://www.youtube.com/watch?v=e9sLVMN76qU&t=637s)
**Key Points:**
- Problem: Agents installing 20+ dependencies repeatedly wastes time/resources
- Old approach: Human creates Docker container manually OR agent builds brittle Dockerfile
- Solution: Declarative image builder - agent specifies base image + dependencies, system builds on-the-fly
- Enables end-to-end autonomy: agent says "I need X installed" and system handles it

### [Shared Volumes for Data Efficiency](https://www.youtube.com/watch?v=e9sLVMN76qU&t=729s)
**Key Points:**
- Humans take for granted: local laptop allows sharing large datasets across Docker containers
- Agents face isolated environments - no local context to share 100GB datasets
- Problem: Downloading from S3 every time is inefficient
- Solution: Daytona volumes - agent uploads once, mounts as network drive on all machines
- Removes repetitive data transfer bottleneck

### [Parallel Execution at Scale](https://www.youtube.com/watch?v=e9sLVMN76qU&t=777s)
**Key Points:**
- Humans work on 1-2 machines max; agents can work on unlimited machines simultaneously
- Instead of sequential try-fail-retry loops, agents fork environments 5, 10, 100,000 times
- Run experiments in parallel, evaluate all outcomes, select best result
- Unique capability differentiating agent workflows from human workflows

### [The Unknown Territory](https://www.youtube.com/watch?v=e9sLVMN76qU&t=823s)
**Key Points:**
- "What else is there in agent experience? I have no idea."
- People are building agents right now - discovering requirements in real-time
- New agent needs emerge through actual usage, not theoretical planning
- If your tool needs humans in the loop, you probably haven't solved the autonomy problem yet

### [Closing: AX is the Only Experience](https://www.youtube.com/watch?v=e9sLVMN76qU&t=853s)
**Key Points:**
- Title isn't about humans disappearing - it's about agents being the largest user base
- Fewer humans will be behind screens reading logs, clicking buttons, typing terminals
- Daytona started focused on developer experience (great CLI/terminal UI) but pivoted
- Critical question for every tool builder: "Can your agent use your product end-to-end autonomously?"
- **If agents can't use your product in the future, absolutely no one will**
- Daytona is open source on GitHub with booth at Expo Hall

---

**Video Duration:** ~15 minutes
**Conference:** AI Engineer (based on channel)
**Key Takeaway:** The shift from developer experience to agent experience isn't just about APIs and documentation—it's about building tools that function autonomously without human intervention. Tools requiring humans in the loop are building for the past.
