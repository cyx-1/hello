# Beyond the Prototype: Using AI to Write High-Quality Code - Josh Albrecht, Imbue

**Video URL:** https://www.youtube.com/watch?v=x_1EumTaXeE

---

## Executive Summary

Josh Albrecht, CTO of Imbue, presents their experimental coding agent environment called Sculptor, which focuses on bridging the gap between AI-generated prototype code and production-ready software. The talk covers technical decisions and strategies for preventing and detecting problems in AI-generated code, including planning workflows, writing specifications, enforcing style guides, running linters, automated testing, and using LLMs for code review. The core philosophy is that identifying and fixing issues early in the development process leads to higher quality code, and that AI agents can excel at this when given proper tooling and constraints.

---

## Main Topics

### [Introduction to Sculptor and the Problem](https://www.youtube.com/watch?v=x_1EumTaXeE&t=20s)
- Josh Albrecht introduces himself as CTO of Imbue, working on robust AI agents
- Introduces Sculptor, a product designed to help with AI coding tools
- **Key Problem**: There's a big gap between AI-generated code and production-ready code, especially in established codebases
- The challenge: when you get code back from an AI agent, you face an awkward choice between reviewing every line or blindly merging
- Sculptor aims to provide a third option by using AI to review and validate AI-generated code
- **Goal**: Build user trust by having AI systems check for race conditions, exposed API keys, and other issues

### [Defining High-Quality Code](https://www.youtube.com/watch?v=x_1EumTaXeE&t=182s)
- High-quality code is defined by the absence of problems and defects
- Academic measurement focuses on number of defects and time to fix them
- Early detection is crucial - Sculptor works synchronously, not as a PR review tool
- Immediate feedback allows both users and agents to fix issues more easily

### [Four Ways to Prevent Problems](https://www.youtube.com/watch?v=x_1EumTaXeE&t=275s)

**1. Learning - Research First** ([05:00](https://www.youtube.com/watch?v=x_1EumTaXeE&t=300s))
- Make it easy to ask questions and do research before coding
- Understand what technologies exist and how others have solved similar problems
- Avoid reproducing work that already exists

**2. Planning Before Coding** ([05:15](https://www.youtube.com/watch?v=x_1EumTaXeE&t=315s))
- Example workflow: Force AI agent to create a plan first without writing any code
- Change system prompt to enforce planning phase, then switch to coding phase
- System prompt changes are stronger than just asking the agent to plan
- Build customized workflows: plan first → code → run checks

**3. Writing Specs and Documentation** ([06:10](https://www.youtube.com/watch?v=x_1EumTaXeE&t=370s))
- Specs and docs should be first-class parts of the workflow
- AI agents need context since they don't have access to email, Slack, etc.
- Sculptor helps detect when code and docs become outdated
- Reduces barrier to maintaining documentation by automatically fixing inconsistencies
- Highlights conflicting specifications early in the process

**4. Strict Style Guides** ([07:12](https://www.youtube.com/watch?v=x_1EumTaXeE&t=432s))
- Enforce style guides to keep AI systems on a reasonable path
- Example: Suggestions to make classes immutable to prevent race conditions
- Developing AI-specific style guides to help agents avoid common mistakes
- Helps both coding agents and human teammates follow best practices

### [Three Ways to Detect Problems](https://www.youtube.com/watch?v=x_1EumTaXeE&t=502s)

**1. Running Linters** ([08:22](https://www.youtube.com/watch?v=x_1EumTaXeE&t=502s))
- Use automated tools like ruff, mypy, pylint, etc.
- AI systems excel at automatically fixing linter errors
- Sculptor makes it easy to detect and auto-fix these issues
- System understands what issues existed before vs. after agent runs
- Prevents AI from creating new errors, even in imperfect codebases

**2. Writing and Running Tests** ([09:54](https://www.youtube.com/watch?v=x_1EumTaXeE&t=594s))

*Why Write Tests with AI?*
- Major objection to testing (effort) disappears with AI code generation
- AI can generate tests easily, especially for correct code
- "If you liked it, you should have put a test on it" - even more important with coding agents
- Prevents agents from changing system behavior unexpectedly

*How to Write Good Tests:* ([11:02](https://www.youtube.com/watch?v=x_1EumTaXeE&t=662s))
- **Functional style code**: Write code with no side effects to make testing easier and safer
- **Two types of unit tests**:
  - Happy path tests: Show code works as expected (need only a few)
  - Unhappy path tests: Find bugs (LLMs can generate hundreds/thousands of test cases)
- **Consider throwing away tests**: Now that regenerating is easy, don't keep tests for behavior you don't care about
- **Focus on integration tests**: Test from user's perspective (e.g., "when user clicks button, item is in cart")
- **Test coverage as core metric**: Not just passing tests, but having enough tests in the first place
- **Run tests in sandboxes**: Makes it easier to fix issues and avoid flaky tests or exposing secrets

**3. Asking an LLM** ([14:47](https://www.youtube.com/watch?v=x_1EumTaXeE&t=887s))
- Check for various issues: pre-commit problems, if the task makes sense, current branch issues
- Verify compliance with style guides and architecture documents
- Check for missing spec details, unimplemented specs, inadequate testing
- Sculptor allows users to extend checks with custom best practices

### [Fixing Issues](https://www.youtube.com/watch?v=x_1EumTaXeE&t=933s)
- "A problem well-stated is half-solved" - understanding the problem makes fixing easier
- Simple strategies work well: try multiple times with different approaches
- Good sandboxing enables running many agents in parallel safely
- If any one succeeds, use that solution
- Cost is the main constraint, not safety, with proper sandboxing

### [The Future of AI Coding Tools](https://www.youtube.com/watch?v=x_1EumTaXeE&t=984s)
- Many more tools coming in the next 1-2 years
- Post-deployment tools: debugging, logging, tracing, profiling
- Automated QA: AI systems testing websites by clicking around
- Code generation from visual designs
- Better contextual search systems for both users and agents
- Improved AI models
- Imbue is interested in integrating other specialized tools into Sculptor
- Development experience will become much easier as these tools work together

### [Conclusion and Call to Action](https://www.youtube.com/watch?v=x_1EumTaXeE&t=1058s)
- Visit imbue.com to sign up and try Sculptor
- Imbue is hiring and happy to chat with interested developers

---

**Last Updated:** January 3, 2026
