# How Claude Code Works - Jared Zoneraich, PromptLayer

**Video URL:** https://www.youtube.com/watch?v=RFKCzGlAU6Q

---

## Executive Summary

Jared Zoneraich, founder of PromptLayer, delivers an in-depth analysis of how Claude Code and other coding agents work, revealing that the breakthrough isn't complex engineering but rather simple architecture combined with better models. The core philosophy is "give it tools and get out of the way" - relying on a simple master while loop with tool calls instead of complex DAGs and scaffolding. Claude Code's success comes from trusting the model's capabilities, using bash as a universal adapter, managing context efficiently, and implementing simple structures like to-do lists for steerability. The talk emphasizes that different coding agents (Claude Code, Codex, Cursor, AMP, Droid) take different philosophical approaches, and there's no single winner - each excels at different use cases.

---

## Major Topics

### 1. Introduction & Speaker Background
**[00:23 - 02:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=23s)**

- Jared Zoneraich introduces himself as founder of PromptLayer, a workbench for AI engineering based in New York
- PromptLayer focuses on rigorous prompt engineering and believes in involving product teams, engineering teams, and domain experts
- The company has rebuilt their engineering organization around Claude Code with a rule: if something can be done in under an hour with Claude Code, just do it without prioritizing
- Talk is not officially endorsed by Anthropic but focuses on understanding what made coding agents finally work

### 2. The Evolution of Coding Assistants
**[04:00 - 05:40](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=240s)**

- Started with copy-pasting code from ChatGPT back and forth
- Evolved to Cursor with Command K functionality
- Then Cursor assistant with back-and-forth interaction
- Finally arrived at Claude Code and the new paradigm of not even touching code
- The big question: What was the breakthrough that made coding agents finally good?

### 3. The Core Breakthrough: Simple Architecture + Better Models
**[05:40 - 09:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=340s)**

- Two main innovations: simplified architecture and better models
- Philosophy: "Give it tools and then get out of the way"
- The breakthrough is somewhat boring - it's just Anthropic releasing better models that work better for tool calling
- Key principle: Less scaffolding, more model - don't try to overengineer around model flaws
- Models are getting better at tool calling and running autonomously

### 4. Philosophy: The Zen of Python for Agents
**[09:00 - 10:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=540s)**

- Simple is better than complex, complex is better than complicated, flat is better than nested
- This is the whole philosophy of why Claude Code works
- Going back to engineering principles: simple design is better design
- Applies whether building a database schema or autonomous coding agents

### 5. The Constitution: CLAUDE.md
**[10:00 - 11:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=600s)**

- CLAUDE.md (or AGENTS.md) provides instructions for the agent
- Simple approach: just a markdown file that users and agents can modify
- No need to overengineer with vector databases or complex research systems
- Everything is context engineering - adapting general purpose models for your usage

### 6. The Simple Master Loop
**[11:00 - 12:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=660s)**

- Revolutionary simplicity: just one while loop with tool calls
- All coding agents today use: while there are tool calls → run tool → give results to model → repeat
- Called "N0" internally (based on research)
- Four lines of code conceptually
- Models are surprisingly good at knowing when to keep calling tools and when to fix mistakes

### 7. Core Tools in Claude Code
**[12:00 - 15:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=720s)**

- **Read**: Handles token limits for large files
- **Grep/Glob**: Uses grep instead of RAG and vectors - mimics human actions at terminal
- **Edit**: Uses diffs instead of rewriting entire files - faster, less context, fewer mistakes
- **Bash**: The most important tool - could arguably replace all others
- **Web Search/Fetch**: Moves to cheaper/faster model for web operations
- **To-dos**: Keeps model on track with steerability
- **Tasks**: Context management for long processes without cluttering

### 8. Bash is All You Need
**[15:00 - 17:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=900s)**

- Two amazing things about bash: it's simple and robust, does everything
- Massive training data because that's what developers use
- Models are better at common languages/tools (Python, JavaScript) vs. less common ones (Rust) due to training data
- Universal adapter with thousands of capabilities
- Example: Creates Python file, runs it, deletes it - the beauty of the system
- Lets the model try things and explore

### 9. Tool Usage Best Practices
**[17:00 - 18:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=1020s)**

- System prompt guides which tools to use when
- Read before editing to avoid errors
- Use grep tool instead of bash grep for security and token limits
- Run independent operations in parallel
- Handle common edge cases like quoting paths with spaces
- Dog fooding at Anthropic helps find and fix common issues

### 10. To-Do Lists for Steerability
**[18:00 - 20:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=1080s)**

- Structured but not structurally enforced - purely prompt-based
- Rules: One task at a time, mark completed, keep working on in-progress if blocked
- Not enforced deterministically - relies on model instruction following
- Would not have worked a year or two ago
- Structure: version, ID (hash), title, evidence blobs
- Four benefits: forces planning, enables resume after crashes, provides UX feedback, enables steerability

### 11. Context Management: The Biggest Enemy
**[20:00 - 22:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=1200s)**

- Async buffer (H2A) decouples IO from reasoning
- Context compaction: at ~92% capacity, drops middle, summarizes head and tail
- Sandbox enables long-term memory storage via files
- Shorter context = quicker and smarter agent
- All chat windows will likely come with sandboxes in the future

### 12. Eliminating DAGs
**[22:00 - 24:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=1320s)**

- Customer support agents used to build hundreds of nodes with complex routing
- Classifying prompts helped prevent hallucinations and prompt injection
- But now: models are good enough to explore and figure it out
- 10x easier to develop, 10x more maintainable
- Trade-off: brings back some attack vectors but major benefit in simplicity
- Rely on the model to explore rather than engineering every edge case

### 13. System Prompt Insights
**[32:00 - 33:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=1920s)**

- Concise outputs - don't be verbose
- No "here is" or "I will" - just do the task
- Use tools instead of text explanations
- Match existing code style, avoid adding comments
- Run commands in parallel extensively
- Manage to-dos effectively
- Many prompts feel like they came from dog fooding: "if only it did this a little less"

### 14. Skills: Extendable System Prompt
**[33:00 - 37:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=1980s)**

- Think of skills as extendable system prompts for different task types
- Examples: docs updates with writing style, Microsoft Office editing, design style guides, deep research
- Provides context without cluttering the main system prompt
- Not perfect yet - sometimes Claude ignores skills and needs manual invocation
- May be a model training problem to better recognize when to call skills

### 15. Unified Diffing
**[34:50 - 35:32](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=2090s)**

- Makes everything better: shorter token usage, faster, fewer mistakes
- Like marking essay with red line vs. rewriting entire essay
- Highly recommended for any agents being built
- Some agents built custom variations, but unified diff is the standard

### 16. Sandboxing and Permissions
**[27:00 - 29:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=1620s)**

- Most boring but important part for production use
- Prompt injection from internet is major attack vector when agent has shell access
- Containerization and URL blocking for security
- Different agents handle differently: Claude Code uses permission gating, Codex uses kernel-based (macOS Seatbelt, Linux seccomp)
- YOLO mode exists but be careful - some team members dropped local databases

### 17. Sub-Agents for Context Management
**[29:00 - 32:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=1740s)**

- Use sub-agents for specific tasks with their own context
- Only feed back results, not full context
- Examples: researcher, docs reader, test runner, code reviewer
- Task tool call structure: description (user-facing) and prompt (long string for the sub-agent)
- Agent prompts its own sub-agents dynamically
- Can stuff as much information as needed into the prompt string

### 18. The AI Therapist Problem
**[39:00 - 41:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=2340s)**

- No global maximum for most interesting AI problems
- Like therapists - different strategies for same goal (meditation, CBT, etc.)
- Taste and design architecture matter significantly
- Five coding agents all amazing, nobody knows which is best
- Different ones excel at different things: Claude Code for git/local environments, Codex for hard problems, Cursor Composer for speed

### 19. Comparing Coding Agents

#### Claude Code [41:00 - 42:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=2460s)
- Wins in user friendliness and simplicity
- Best for applications requiring git, bash, human-like terminal actions
- Excellent context management
- Feels powerful (though hard to prove objectively)

#### Codex [43:00 - 44:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=2580s)
- Similar master while loop architecture (written in Rust)
- Open source - can use Codex to understand how Codex works
- More event-driven with concurrent threading
- Submission queues and event outputs for IO buffering
- Different sandboxing approach (kernel-based)
- Main difference: the model itself

#### AMP (SourceGraph) [44:00 - 46:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=2640s)
- Free tier with ads (interesting business model)
- No model selector - abstracts away which model is used
- Enables faster iteration since users don't have exact expectations
- Vision: build agent-friendly environments, hermetically sealed repos
- Focus on feedback loops and self-improvement
- "Agent perspective" - how to let it look at its own design
- Context management: "handoff" instead of "compact" - switching weapons is faster than reloading
- Model choice: Fast, Smart, Oracle (willing to switch what Oracle is)

#### Cursor [46:00 - 48:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=2760s)
- UI-first, not CLI
- Extremely fast with distilled Composer model
- Made fine-tuning interesting again - showed defensibility through data
- Built iteratively - first version was bad but kept improving
- Almost too fast - can accidentally push to master
- OpenAI's Codex models are also fast and distilled, catching up

### 20. Evaluation and Testing
**[48:00 - 53:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=2880s)**

- Benchmarks are pretty useless - become marketing for model providers
- Simple while loop architecture makes evaluation harder (relies on model flexibility)
- Three approaches:
  - End-to-end tests: Does it fix the problem?
  - Point-in-time snapshots: Give context mid-conversation, check tool calls
  - Back tests: Capture historical data and rerun
- "Agent smell": Surface metrics like number of tool calls, retries, time taken
- Rigorous tools can be tested like functions (input/output)
- For specific deliverables (emails, blog posts), use structured workflows with LLM assertions

### 21. Headless Claude Code SDK
**[54:00 - 55:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=3240s)**

- Keep an eye on this future development
- Simple prompt becomes part of your pipeline
- Example: GitHub action that updates docs daily by reading commits across repos
- Possibility of building agents at higher order of abstraction
- Relies on Claude Code for orchestration instead of custom agent code

### 22. Future Directions
**[37:00 - 39:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=2220s)**

- Two schools: hundreds of tool calls vs. reduce to just bash
- Jared believes in reducing tool calls, going back to simple bash
- Adaptive budgets for reasoning (think, think hard, ultra think)
- Reasoning models as tools - trade-off between speed and capability
- New first-class paradigms beyond to-dos and skills
- Mixture of experts - running multiple agents (Claude Code, Codex, etc.) and having them collaborate

### 23. Key Takeaways
**[55:00 - 57:00](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=3300s)**

1. **Trust in the model** - When in doubt, rely on the model when building agents
2. **Simple design wins** - Don't over-engineer
3. **Bash is all you need** - Go simple with tools, have 5-10 not 40
4. **Context management matters** - The boogeyman we're always running from
5. **Different perspectives matter** - No global maximum, different approaches excel at different things

### 24. Building the Presentation with Claude Code
**[56:40 - 57:20](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=3400s)**

- Built a SlidesDev skill to research how the library works
- Built a deep research skill to research all the coding agents
- Built a design skill for aesthetic improvements (accent colors, better boxes)
- Demonstrates practical use of Claude Code skills system

### 25. Q&A Session
**[57:25 - 01:05:26](https://www.youtube.com/watch?v=RFKCzGlAU6Q&t=3445s)**

- **DAGs vs. loops**: General purpose agents don't need specific steps, so rely on model. Specific deliverables (travel itinerary) might benefit from DAGs for output formatting
- **Future of API calls**: May move toward headless agent endpoints (like reasoning models), but some tasks need more control. Similar to completions → chat transition
- **Test-driven development**: Return to good engineering practices. If tests work for your workflow, use them. Test-driven helps coding agents work better
- **System prompt location**: On your machine, can be found if determined
- **PromptLayer hiring**: Based in New York, looking for engineers. Platform for building and testing AI products with prompt management, logging, and evals

---

**Last Updated:** January 2025 (Video from AI Engineer conference)
