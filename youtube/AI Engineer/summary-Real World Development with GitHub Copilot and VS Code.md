# Real World Development with GitHub Copilot and VS Code

**Video URL:** https://www.youtube.com/watch?v=eOxOzcw70f0

---

## Executive Summary

This workshop explores "vibe coding" - a paradigm shift in software development where developers focus on outcomes rather than code, leveraging GitHub Copilot and VS Code's AI capabilities. The presenter walks through three stages of AI-assisted development: YOLO Vibes (rapid prototyping), Structured Vibes (maintainable code), and Spectrum Vibes (enterprise-scale practices), demonstrating practical techniques including auto-approval, custom modes, MCP servers, and workspace instructions to build trust with AI coding assistants.

---

## Main Topics

### [1. Introduction to Vibe Coding](https://www.youtube.com/watch?v=eOxOzcw70f0&t=17s)
**00:00 - 03:00**

- Definition of "vibe coding at scale" - focusing on output rather than code
- Embracing exponential growth and "forgetting that code exists"
- Building trust and adding guardrails to AI development
- Three stages of vibe coding journey introduced

**Key Points:**
- Shift from code-first to outcome-first mindset
- AI agents generating exponentially more code over time
- Philosophy of reviewing output while building trust in AI systems

---

### [2. YOLO Vibes - Rapid Prototyping Phase](https://www.youtube.com/watch?v=eOxOzcw70f0&t=97s)
**01:37 - 04:00**

- First stage: creativity and speed prioritized
- Use cases: rapid prototyping, proof of concepts, learning new technologies
- Natural language interaction with auto-accepting changes
- Not about shipping products, but about instant gratification and exploration

**Key Points:**
- Ideal for non-technical people communicating ideas
- UX designers creating functional mockups
- Learning new frameworks (example: 3JS) through working code
- "Fix it or go to jail" - staying in natural language flow

---

### [3. Live Demo - Creating Water Tracking App](https://www.youtube.com/watch?v=eOxOzcw70f0&t=622s)
**10:22 - 16:00**

- Using the "new" command for creating projects from scratch
- Optimized workflow for "Can it make me a water tracking app?" scenarios
- Setting up auto-approve for workspace-level safety
- Comparing Material Design vs Fluent Design implementations

**Key Points:**
- New command handles project bootstrapping
- Auto-approve setting removes manual continue buttons
- Simple browser preview for in-editor testing
- Multiple design systems yield different aesthetic results

---

### [4. VS Code UI Customization for AI Workflows](https://www.youtube.com/watch?v=eOxOzcw70f0&t=1348s)
**22:28 - 27:00**

- Moving chat panel into editor for more space
- Opening chat in separate window for multi-monitor setup
- Pinning chat windows to stay on top
- Managing multiple chat sessions with named conversations

**Key Points:**
- Chat can be moved to editor, panel, or separate window
- Window management allows for focused "exponential" viewing
- Multiple chats can run in parallel
- Named sessions for easy navigation

---

### [5. Structured Vibes - Maintainable Development](https://www.youtube.com/watch?v=eOxOzcw70f0&t=1800s)
**30:00 - 34:00**

- Second stage: balance and sustainability
- Focus on maintainability, readable code, quality control
- Using workspace instructions and custom prompts
- Preparing code for handover to other developers

**Key Points:**
- Transition from throwaway to production-ready code
- Best practices emerging from community (Reddit, blogs)
- Scale, reliability, and velocity with reduced chaos
- Wireframes and charts for structured planning

---

### [6. Copilot Instructions Deep Dive](https://www.youtube.com/watch?v=eOxOzcw70f0&t=2301s)
**38:21 - 40:00**

- Location: `.github/copilot-instructions.md`
- Included with all agent, chat, and inline chat requests
- Provides grounding foundation knowledge about codebase
- Best practice: one-liner about stack and frameworks

**Key Points:**
- Markdown file for project-wide AI context
- Avoids repetitive linting rules
- Specify frameworks and versions
- Team exercise to keep document updated

---

### [7. Custom Chat Modes](https://www.youtube.com/watch?v=eOxOzcw70f0&t=2729s)
**45:29 - 50:00**

- Creating TDD (Test-Driven Development) mode live
- Modes define "how to do it" vs prompts define "what to do"
- Can specify which tools a mode should use
- Repository-level or user-level mode storage

**Key Points:**
- Modes can enforce development techniques
- Custom agent modes with specific tool access
- TDD mode: understand problem → write tests → get confirmation → implement
- Modes ship in VS Code stable on December 11th

---

### [8. MCP (Model Context Protocol) Servers](https://www.youtube.com/watch?v=eOxOzcw70f0&t=3422s)
**57:02 - 62:00**

- Installing MCP servers via VS Code protocol
- User settings vs workspace settings for MCP
- Popular servers: GitHub, GPAD (gist-based knowledge base)
- Input system for secure token management

**Key Points:**
- Install via command palette or manual JSON configuration
- Tokens encrypted at rest using VS Code key storage (Keychain on Mac)
- Two transport types: SSE (deprecated) and HTTP (streamable, cloud-friendly)
- MCP servers provide external tools and context to AI

---

### [9. MCP Sampling and Advanced Features](https://www.youtube.com/watch?v=eOxOzcw70f0&t=3630s)
**01:00:30 - 01:11:00**

- Sampling: MCP servers can call back to client's LLM
- Use cases: summarizing large data, reducing token counts
- VS Code first to support sampling in production
- Tool calling remains non-deterministic even with hints

**Key Points:**
- Sampling allows servers to use client's AI model
- Reduce tools in custom modes for better determinism
- Can mention specific tools in chat via "Add Context"
- Modes can restrict tool access for focused workflows

---

### [10. Spectrum Vibes - Enterprise Scale](https://www.youtube.com/watch?v=eOxOzcw70f0&t=4013s)
**01:06:53 - 01:10:00**

- Third stage: scale, reliability, and velocity
- Custom modes for spec writing with Perplexity integration
- Generating specs from meeting transcripts
- Continuous refinement of instructions based on AI mistakes

**Key Points:**
- Spec-first approach: focus on specification quality
- Use markdown for spec documents
- Feed meeting transcripts to generate specs
- Keep iterating instructions as AI makes mistakes

---

### [11. Best Practices and Tooling](https://www.youtube.com/watch?v=eOxOzcw70f0&t=4286s)
**01:11:26 - 01:14:00**

- Agent has access to problems and tasks automatically
- Cross-repo search with web docs integration
- Generate commits automatically
- Fine-grain review: pause, steer, and provide feedback

**Key Points:**
- Set up linting and tasks in templates
- Point AI to external repos for reference
- Trust read-only tools selectively
- Always steer AI with feedback rather than accepting bad answers

---

### [12. Final Takeaways and Q&A](https://www.youtube.com/watch?v=eOxOzcw70f0&t=4699s)
**01:18:19 - 01:19:26**

- Experimentation is key to finding what works
- Decide between full autonomy vs spec-first approaches
- Never accept bad answers - iterate with feedback
- Use modes, prompts, and instructions to ingrain team processes

**Key Points:**
- Sweet spot: well-structured, self-explaining code
- Keep instructions updated with examples
- Different levels of planning: spec → plan → implement
- Workshop demonstrates unplanned, real-world usage

---

**Total Duration:** ~1 hour 19 minutes

**Key Technologies Mentioned:**
- GitHub Copilot
- VS Code (stable and insiders)
- MCP (Model Context Protocol)
- Material Design / Fluent Design
- Playwright (for browser automation)
- Perplexity (for research)
- GPAD (GitHub gist-based MCP server)
