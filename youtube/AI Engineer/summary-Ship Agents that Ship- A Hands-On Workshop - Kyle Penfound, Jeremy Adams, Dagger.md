# Ship Agents that Ship: A Hands-On Workshop - Summary

**Video URL:** https://www.youtube.com/watch?v=Fzb1a24hF-o
**Channel:** AI Engineer
**Presenters:** Kyle Penfound & Jeremy Adams (Dagger)

---

## Executive Summary

This workshop demonstrates how to build and deploy AI coding agents using Dagger, a containerized development tool. The presenters walk through creating a software engineering agent that can read code, run tests, make changes, and even create pull requests on GitHub—all running in isolated, reproducible container environments. The key insight is leveraging existing CI/CD workflows as tools for AI agents, enabling them to execute real development tasks with proper sandboxing and guardrails.

---

## Main Topics

### 1. Introduction & Setup ([00:16](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=16s) - [10:00](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=600s))

**Key Points:**
- Workshop goal: Build an AI agent that can autonomously develop features and create pull requests
- Dagger is a containerized development tool that provides primitives for building, testing, and deploying code
- Installation requirements: Dagger CLI and a container runtime (Docker, Podman, or nerdctl)
- Documentation available at docs.dagger.io
- Slack channel available for workshop questions: "dagger-workshop ship agents that ship"

**Highlights:**
- [00:16](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=16s) - Workshop kickoff and introductions
- [02:36](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=156s) - Installation instructions overview
- [03:51](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=231s) - Mention of hack night event at Cloudflare office

### 2. Dagger Fundamentals ([10:00](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=600s) - [21:00](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=1260s))

**Key Points:**
- Dagger provides building blocks: containers, directories, and LLMs
- Interactive shell mode (`dagger shell`) vs. non-interactive command execution
- Builder pattern for chaining operations (e.g., `container.from("alpine").terminal()`)
- Dagger functions can be called from multiple language SDKs (Python, Go, TypeScript, etc.)
- Unified cache system across all operations for performance

**Highlights:**
- [10:17](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=617s) - Demonstration of creating containers with `dagger shell`
- [11:09](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=669s) - Building blocks concept explained
- [12:23](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=743s) - Using Dagger for CI/CD workflows
- [19:41](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=1181s) - Creating development tools with Dagger functions

### 3. Building the First Agent ([21:00](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=1260s) - [40:00](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=2400s))

**Key Points:**
- Agents are created by combining a Dagger LLM with an environment and a prompt
- The environment provides tools like containers with read/write file capabilities
- Agents can run actual tests using the same code as CI/CD pipelines
- The workspace provides a sandboxed environment for the agent to operate safely
- Agent prompts include instructions like "don't stop until it's done" for autonomous operation

**Highlights:**
- [21:21](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=1281s) - Adding an AI agent to an existing project
- [22:03](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=1323s) - Creating an agent for developers to interact with
- [39:09](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=2349s) - **Most important line**: Creating the agent with `dag.llm()` (line 94)
- [40:01](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=2401s) - Agent prompt structure explained

### 4. Agent Prompting & Behavior ([37:00](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=2220s) - [39:00](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=2340s))

**Key Points:**
- Prompt engineering is crucial for agent effectiveness
- Need to explicitly tell agents to read code, run tests, and verify their changes
- Different models require different prompt structures
- Dagger Cloud provides visualization of agent workflows for debugging
- Reflection agents can be implemented to "police" each other

**Highlights:**
- [37:33](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=2253s) - Using Dagger Cloud to visualize agent work
- [37:47](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=2267s) - Importance of telling agents to test their code
- [38:04](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=2284s) - Q&A about implementing reflection agents
- [38:35](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=2315s) - Google's Agent-to-Agent (A2A) pattern explanation

### 5. GitHub Integration ([56:00](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=3360s) - [58:00](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=3480s))

**Key Points:**
- Daggerverse provides pre-built modules for common tasks (e.g., GitHub issues)
- The `github-issue` module enables reading issues, creating PRs, and adding comments
- Agents can read GitHub issues as assignments and create PRs with completed work
- Pull requests automatically link to issues using "closes #issue" syntax
- Cross-language module compatibility (Go module used in Python project)

**Highlights:**
- [56:00](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=3360s) - Introduction to Daggerverse modules
- [56:10](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=3370s) - GitHub issue module capabilities
- [56:56](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=3416s) - Creating the `develop_issue` function
- [57:08](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=3428s) - Agent reads GitHub issue, develops feature, creates PR workflow

### 6. Alternative Agent SDKs & Integration ([01:15:00](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=4500s) - [01:16:42](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=4602s))

**Key Points:**
- Dagger can be integrated with other agent frameworks (OpenAI Agent SDK, Pydantic, etc.)
- Some users want Dagger primarily for sandboxing capabilities
- Using Dagger's native LLM provides automatic tool generation from function signatures
- Daggerverse modules work seamlessly when using Dagger's agent system
- Harmonization is better when using Dagger for both agents and tooling

**Highlights:**
- [01:15:19](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=4519s) - Example using OpenAI Agent SDK with Dagger containers
- [01:15:47](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=4547s) - Recreating workspace with Dagger inside OpenAI SDK
- [01:16:03](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=4563s) - Benefits of Daggerverse modules with native agents
- [01:16:25](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=4585s) - Users wanting local sandboxing without cloud vendors

### 7. Advanced Use Cases & Q&A ([01:16:45](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=4605s) - [01:18:03](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=4683s))

**Key Points:**
- Browser automation is possible with headless browsers and VNC connections
- CI/CD infrastructure can be built once and reused with guardrails for agents
- Dagger provides asynchronous AI agent capabilities with built-in safety
- Agents are "just Dagger functions" that can be composed and layered

**Highlights:**
- [01:16:52](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=4612s) - Q&A about building HTML game testing agents with browser environments
- [01:17:11](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=4631s) - Discussion of headless browser and VNC capabilities
- [01:17:42](https://www.youtube.com/watch?v=Fzb1a24hF-o&t=4662s) - Q&A about Dagger as asynchronous AI agent infrastructure with guardrails

---

## Key Takeaways

1. **Reuse CI/CD as Agent Tools**: Development workflows (build, test, publish) built for CI/CD can be directly given to agents, ensuring they use the same validated processes
2. **Sandboxing & Safety**: Container-based execution provides natural isolation and reproducibility for agent actions
3. **Composable Architecture**: Agents are functions that can call other functions, enabling reflection patterns and agent-to-agent communication
4. **Cross-Language Support**: Unified API accessible from multiple programming languages via SDKs
5. **Daggerverse Ecosystem**: Shared modules enable rapid integration with external services (GitHub, etc.)
6. **Visualization & Debugging**: Dagger Cloud provides visibility into agent workflows for prompt optimization

---

**Last Updated:** 2026-01-02
