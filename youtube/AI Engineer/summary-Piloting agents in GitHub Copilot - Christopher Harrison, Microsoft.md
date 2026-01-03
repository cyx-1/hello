# Piloting agents in GitHub Copilot - Christopher Harrison, Microsoft

**Video URL:** https://www.youtube.com/watch?v=DdaAABdAqZY

**Duration:** ~59 minutes

---

## Executive Summary

Christopher Harrison from Microsoft leads a hands-on workshop on GitHub Copilot's agent capabilities, focusing on the new "coding agent" feature (currently in pilot). The session covers the fundamentals of working with AI assistants through proper context management, explores the different GitHub Copilot workloads (code completion, chat, and coding agent), and demonstrates how to leverage the coding agent to autonomously handle complex multi-file tasks. Key themes include the importance of providing context, understanding how coding agent operates (using GitHub Actions in isolated environments), security considerations, and practical implementation patterns like using .github/copilot-instructions.md files and MCP servers for external integrations.

---

## Main Topics

### [Introduction and Setup](https://www.youtube.com/watch?v=DdaAABdAqZY&t=0s)
**[00:00 - 05:30]**

- Workshop logistics: Same lab running at 3:30 PM
- Participants need to accept GitHub organization invitation for Copilot access
- Emphasis on hands-on participation in the workshop
- Setting expectations for the session structure

**Key Points:**
- Lab will be repeated later in the day for those who can't attend
- Access to GitHub Copilot provided through organization membership
- Interactive workshop format with live demonstrations

---

### [Understanding Context in AI Interactions](https://www.youtube.com/watch?v=DdaAABdAqZY&t=317s)
**[05:17 - 10:16]**

- The brunch analogy: Demonstrating how context shapes AI responses
- Why context is critical when working with any AI tool including GitHub Copilot
- Iterative refinement through conversational context building
- Three pillars of good prompts: Clarity, Verbosity, and Specificity

**Key Points:**
- Context helps AI understand constraints and preferences
- Human conversation naturally builds context through back-and-forth
- Don't use AI like a command-line interface - be conversational and verbose
- Specificity ensures the AI delivers what you actually want

---

### [GitHub Copilot Workloads Overview](https://www.youtube.com/watch?v=DdaAABdAqZY&t=616s)
**[10:16 - 14:00]**

- **Code Completion**: Original inline suggestions while typing
- **Chat**: Interactive conversation for explaining, refactoring, or generating code
- **Coding Agent** (NEW): Autonomous multi-file task execution

**Key Points:**
- Code completion best for developers "in the zone" who know what they're doing
- Chat provides flexibility for exploration and understanding
- Coding agent handles complex tasks that span multiple files
- Each mode serves different development scenarios

---

### [Lab Setup and Environment Configuration](https://www.youtube.com/watch?v=DdaAABdAqZY&t=923s)
**[15:23 - 21:00]**

- Accessing the workshop lab materials
- Using GitHub Codespaces (no local installation required)
- Creating repository from template
- Configuring GitHub Copilot access
- Understanding the lab structure and objectives

**Key Points:**
- Everything runs in the cloud via Codespaces
- Lab includes: setting up environment, assigning issues, configuring external services
- Participants will interact with Copilot, complete sitewide updates, and review Copilot's work

---

### [Discussion: Vibe Coding and Agent-Driven Development](https://www.youtube.com/watch?v=DdaAABdAqZY&t=1271s)
**[21:11 - 22:20]**

- Question about "vibe coding" and its relationship to Copilot modes
- Agent-driven workflows where Copilot drives the operation
- Personal preferences and approaches to AI-assisted development

**Key Points:**
- Coding agent represents a form of agent-driven development
- Different developers will have different comfort levels with delegation
- No strong prescriptive stance - use what works for your workflow

---

### [Providing Context with .github/copilot-instructions.md](https://www.youtube.com/watch?v=DdaAABdAqZY&t=1983s)
**[33:03 - 33:49]**

- Creating standardized coding guidelines for Copilot
- Documenting coding standards, language preferences, and repository structure
- How Copilot reads and applies these instructions

**Key Points:**
- Place coding standards and conventions in `.github/copilot-instructions.md`
- Include language-specific guidance (Python/Flask, Svelte/Astro, etc.)
- Document repository structure and available scripts
- Coding agent and chat both consider these instructions
- Most projects should already have this documentation

---

### [How Coding Agent Works: GitHub Actions Architecture](https://www.youtube.com/watch?v=DdaAABdAqZY&t=2037s)
**[33:57 - 45:15]**

- Coding agent runs on GitHub Actions infrastructure
- Creates isolated, ephemeral runner environments
- Can execute terminal commands locally within the runner
- Demonstrates running tests and viewing test results

**Key Points:**
- Coding agent uses GitHub Actions runners (same infrastructure as CI/CD)
- Each session gets a clean, isolated environment
- Can run commands like `pytest`, `npm test`, etc.
- Terminal output is visible and agent can respond to test failures

---

### [Security Considerations and Constraints](https://www.youtube.com/watch?v=DdaAABdAqZY&t=2704s)
**[45:04 - 46:00]**

- Coding agent built with security as primary consideration
- Cannot modify GitHub Actions workflows
- Cannot access external resources by default
- Runs in isolated GitHub Actions environment

**Key Points:**
- Security-first design prevents unauthorized access
- Workflow files (.github/workflows/) are protected from modification
- No external network access without explicit configuration
- Isolation protects both your code and external services

---

### [MCP Servers for External Integrations](https://www.youtube.com/watch?v=DdaAABdAqZY&t=3476s)
**[57:56 - 58:06]**

- Using Model Context Protocol (MCP) servers for controlled external access
- Provides granular control over what Copilot can access
- Useful for distinguishing between "good" and "bad" parts of codebase

**Key Points:**
- MCP servers enable controlled external integrations
- Can specify which parts of codebase to expose or hide
- Helps train Copilot on preferred patterns and code sections

---

### [Closing and Additional Resources](https://www.youtube.com/watch?v=DdaAABdAqZY&t=3537s)
**[58:57 - 59:01]**

- Workshop wrap-up
- Reminder about accessing lab materials
- Network issues acknowledgment

---

## Key Takeaways

1. **Context is King**: The most important aspect of working with AI is providing clear, verbose, and specific context
2. **Three Copilot Modes**: Code completion, chat, and coding agent each serve different purposes in the development workflow
3. **Security by Design**: Coding agent runs in isolated GitHub Actions environments with limited external access
4. **Standardize with Instructions**: Use `.github/copilot-instructions.md` to provide consistent coding standards
5. **MCP for Integration**: Model Context Protocol servers enable controlled access to external resources and selective codebase exposure
6. **Autonomous Multi-File Work**: Coding agent can handle complex tasks spanning multiple files with proper context
7. **Test-Driven Workflow**: Coding agent can run tests and respond to failures autonomously

---

## Additional Context

- **Target Audience**: Developers interested in GitHub Copilot's advanced features, particularly the new coding agent
- **Format**: Hands-on workshop with live demonstrations and participant exercises
- **Prerequisites**: GitHub account, basic familiarity with development workflows
- **Technology Stack**: GitHub Copilot, GitHub Actions, GitHub Codespaces
- **Pilot Feature**: Coding agent is in pilot/preview at the time of this workshop

---

**Last Updated:** January 3, 2026
