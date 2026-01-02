# Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI

**Video URL:** https://www.youtube.com/watch?v=wVl6ZjELpBk

---

## Executive Summary

Bill Chen and Brian Fioca from OpenAI's Applied AI Startups team present strategies for building future-proof coding agents. They explain the anatomy of coding agents (UI, model, and harness), with focus on the harness as the critical interface layer. The talk introduces **Codeex** (both a model and harness) as OpenAI's solution to the challenge of constantly adapting agents to new model releases. Key insights include understanding model "habits" alongside capabilities, avoiding over-prompting, and using Codeex as an abstraction layer that lets developers focus on product differentiation rather than prompt engineering. The presentation demonstrates how Codeex can be integrated via SDK into various products, from IDEs to CI/CD pipelines, and positions it as a "computer use agent for the terminal."

---

## Topics

### [Introduction to Coding Agents](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=23s)
- Bill and Brian introduce themselves from OpenAI's Applied AI Startups team
- Coding agents represent a signal of how close we are to AGI
- Software engineering as a universal medium for problem solving
- Challenge: ground keeps shifting with new model releases requiring constant agent rebuilding
- Talk outline: anatomy of coding agents, lessons learned, emerging patterns, future of Codeex

### [Anatomy of a Coding Agent](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=129s)
- Three components: User Interface, Model, and Harness
- **Interface**: CLI tool, IDE, or cloud/background agent
- **Model**: Latest models like GPT-4.5.1, Codeex Max, or other providers
- **Harness**: The interesting part - collection of prompts and tools in a core agent loop
- Harness provides input/output from model and is the focus of this talk

### [Why Harnesses Are Challenging](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=204s)
- Harness = interface layer to the model
- Surface area for model to talk to users, code, and perform actions
- Multiple challenges:
  - **Tool adoption**: Custom tools model hasn't seen in training
  - **Latency**: Managing thinking time and UX exposure
  - **Context window management**: Compaction is challenging (Codeex Max handles this automatically)
  - **API changes**: Completions, responses, future formats
- Fitting a model into a harness requires extensive prompting

### [Intelligence Plus Habit: Understanding Model Behavior](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=367s)
- Model training has side effects beyond just intelligence
- **Intelligence**: What the model is good at (languages, frameworks)
- **Habits**: How the model learned to solve problems
- OpenAI models trained with habits: planning, gathering context, thinking before coding, testing
- Developing "feel" for these habits is key to prompt engineering
- **Real example**: GPT-5 users porting prompts from other models experienced slowness
  - Other models needed explicit instructions to examine context thoroughly
  - GPT-5 already does this naturally - over-prompting caused excessive thoroughness
  - Solution: Let the model use its natural behaviors, don't over-prompt
- Learning by asking: "What can I do differently in your instructions to help you get there faster?"
- Model responded: "You're telling me to look at everything and I don't really need to"

### [Codeex: Combined Model and Harness](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=494s)
- Advantage of building model and harness together: intimate knowledge of capabilities
- Codeex is both a model AND a harness combined
- Built to be an agent for everywhere you code: VS Code plugin, CLI, cloud, ChatGPT, phone
- Core capabilities:
  - Turn specs into runnable code
  - Navigate repo to edit files
  - Run commands and execute tasks
  - Call from Slack or review PRs on GitHub

### [Codeex as a Computer Use Agent](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=616s)
- More powerful than "just" a coding agent
- Pre-GUI computing: writing code and chaining commands in CLI
- **If you can express tasks in command line and files, Codeex can handle it**
- Examples:
  - Organizing photos from desktop into folders
  - Analyzing huge CSV files for data analysis
  - Not limited to coding tasks - any CLI-accessible task

### [Harness Complexity: What's Under the Hood](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=554s)
- Team member's response: "It's way harder than you think"
- Managing parallel tool calls, thread merging
- Security: sandboxing, prompt forwarding, permissions, port management
- **Compaction**: When to trigger, when to reinject, cache optimization
- MCP (Model Context Protocol) support plumbing
- Image handling: resolution compression for model input
- All this work needed to keep updated as new features come online

### [Using Codeex to Build Your Own Agents](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=687s)
- Codeex can write its own tools to solve new problems
- Use Codeex agent inside your own agent
- Pattern: Harness as the new abstraction layer
- **Benefits**: No need to optimize prompts/tools with every model upgrade
- Response to "just building a wrapper": Focus efforts on differentiating your product - that's where value lies
- Like infrastructure layer on top of models

### [Integration Patterns and SDK](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=774s)
- **Codeex is an SDK** callable through:
  - TypeScript library
  - Python exec (programmatically)
  - GitHub Action (auto-merge PR conflicts)
  - Agents SDK with MCP connectors
- Evolution: Chatbots → Chatbots with tools → Tools that make other tools
- **Enterprise software that writes its own plugin connectors** to API level per customer
- Replaces professional services team work
- Example: Kanban board that can fix its own bugs

### [Partner Examples](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=849s)
- **Zed**: Wrapped Codeex with IDE interface layer
  - Focuses on building best code editor
  - OpenAI handles staying current with capabilities
- **GitHub**: Direct SDK integration with Codeex
- **Cursor**: Aligned tools with model training distribution
  - Used open-source Codeex CLI implementation
  - All publicly available - can fork repo and use source code
- **CI/CD integration**: Control Codeex as part of pipelines

### [Future of Codeex](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=937s)
- Hasn't been out for a year yet
- Codeex Max launched yesterday (at time of talk)
- **Fastest growing model in usage**: Serving dozens of trillions of tokens per week
- Usage has doubled since Dev Day
- Safe assumptions:
  - Models will get better
  - Work on much longer horizon tasks unsupervised
  - **Trust ceiling will keep rising**
- Future focus: Sprawling codebases, non-standard libraries, closed source environments
- Matching existing templates and practices
- SDK will evolve to:
  - Let models learn as they go
  - Not repeat mistakes
  - Provide more surface area for code writing and terminal use

### [Key Takeaways](https://www.youtube.com/watch?v=wVl6ZjELpBk&t=1016s)
- Harnesses are complicated and require significant maintenance work
- OpenAI built one for you inside Codeex
- Use off-the-shelf or examine the source
- Build new things outside of coding while OpenAI maintains the most capable computer agent
- Let developers focus on building differentiated products

---

**Last Updated:** 2026-01-01
