# Software Development Agents: What Works and What Doesn't - Robert Brennan, AllHands/OpenHands

**Video URL:** https://www.youtube.com/watch?v=o_hhkJtlbSs

---

## Executive Summary

Robert Brennan, creator of OpenHands (formerly OpenDevin), shares practical insights on using AI coding agents effectively. The talk covers how coding agents work under the hood, best practices for using them, and specific use cases where they excel. Key takeaway: coding is going away, but software engineering isn't—developers will spend less time writing code and more time thinking critically about architecture, user needs, and business objectives. Brennan emphasizes starting small with routine tasks, being explicit with instructions, and always reviewing AI-generated code before merging.

---

## Topics

### [Introduction and Context](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=16s)
**[00:16 - 01:00]**

- Robert Brennan introduces himself as a builder of open-source development tools for over a decade
- His team created OpenHands, an open-source software development agent
- Software development is changing rapidly—jobs are different than 2 years ago and will be different 2 years from now

**Key Points:**
- Coding is going away, but software engineering is not
- Developers are paid to think critically, not just type
- AI is excellent at the inner loop of development (write code → run code → repeat)

### [The Future of Software Engineering](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=58s)
**[00:58 - 01:53]**

- AI-driven development means less time "leaning forward and squinting into our IDE"
- More time sitting back and thinking about what users actually want
- Focus shifts to architecture, business objectives, and empathy for end users
- AI struggles with big-picture tasks requiring business context and user empathy

### [What Is a Coding Agent?](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=113s)
**[01:53 - 02:35]**

- The term "agent" has drifted over time, but core concept is **agency**—taking action in the real world
- Main tools of software engineering that agents use:
  - **Code editor** - to modify and navigate codebase
  - **Terminal** - to run code
  - **Web browser** - to look up documentation, copy from Stack Overflow

### [Agents vs. Tactical Code Generation Tools](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=155s)
**[02:35 - 03:37]**

- Evolution of AI coding tools:
  - **GitHub Copilot autocomplete** - fills out 2-3 lines wherever cursor is pointed
  - **AI-powered IDEs** - take a few steps without developer interference
  - **Full agents (Devon/OpenHands)** - work autonomously for 5-15 minutes on 1-2 sentence prompts

**Benefits of agents:**
- Can run multiple agents in parallel
- Frees developers to communicate with coworkers or focus on other tasks
- Much more powerful way of working

### [How Agents Work Under the Hood](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=219s)
**[03:39 - 04:35]**

- At core: a loop between a large language model (LLM) and the external world
- LLM serves as the "brain"
- Each step: LLM decides next action → execute in real world → feed results back to LLM
- Actions include: read file, make edit, run command, look at web page

### [Core Tools: Code Editor](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=275s)
**[04:35 - 05:24]**

- **Naive approach:** Give LLM entire old file, output entire new file
  - Wasteful for large files with small changes (thousands of tokens for one-line change)
- **Modern approach:** Find-and-replace or diff-based editor
  - Allows tactical edits inside files
  - Often provide abstract syntax tree (AST) for better code navigation

### [Core Tools: Terminal](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=324s)
**[05:24 - 05:50]**

- Text in/text out seems simple but raises complex questions:
  - What to do with long-running commands with no stdout?
  - How to handle parallel commands or background processes?
  - Example: Starting a server, then running curl against it

### [Core Tools: Web Browser](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=350s)
**[05:50 - 06:43]**

- **Naive approach:** Agent provides URL, gets HTML back
  - Expensive due to unnecessary HTML cruft
- **Better approaches:**
  - Pass accessibility trees or convert to markdown
  - Allow LLM to scroll through pages with lots of content
  - For interaction: LLM writes JavaScript or uses screenshot with labeled nodes to click
- **Recent progress:** Contribution doubled web browsing accuracy about a month ago
- This is an active area of research

### [Sandboxing and Security](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=403s)
**[06:43 - 07:27]**

- Critical for autonomous operation without constant supervision
- All OpenHands agents run inside Docker containers by default
  - Completely separated from workstation
  - No risk of `rm -rf` on home directory
- Increasingly giving agents access to third-party APIs (GitHub tokens, AWS)
  - **Important:** Tightly scope credentials and follow principle of least privilege

### [Best Practice: Start Small](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=447s)
**[07:27 - 08:39]**

- Best tasks for beginners:
  - Can be completed quickly (single commit)
  - Clear definition of done (tests passing, merge conflicts solved)
  - Easy for engineers to verify correctness
- **Start with small chores:** Failing tests, lint errors, merge conflicts
  - Rote tasks developers don't enjoy
  - AI does them very well
- As intuition grows, give bigger and bigger tasks
- **Brennan's experience:** 90% of his code goes through the agent now, only 10% requires hands-on IDE work

### [Best Practice: Be Clear and Specific](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=519s)
**[08:39 - 09:22]**

- Tell the agent **what** you want AND **how** to do it:
  - Mention specific frameworks
  - Specify development strategies (e.g., test-driven development)
  - Reference specific files or function names
- **Benefits:**
  - More accurate results
  - Faster execution (less codebase exploration)
  - Lower token costs

### [Best Practice: Code Is Cheap—Experiment Freely](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=562s)
**[09:22 - 10:34]**

- In AI-driven development, code is cheap—you can throw it away
- Brennan's workflow: Give instructions on walk to work, PR ready when he arrives
  - 50% of the time: throw it away, didn't work
  - 50% of the time: looks great, merge immediately
- **When agent gets it wrong:**
  - If close: iterate within same conversation
  - If way off: throw away, start fresh with improved prompt
- New muscle memory needed: being willing to discard thousands of lines of AI-generated code

### [Best Practice: ALWAYS Review the Code](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=634s)
**[10:34 - 11:32]**

- **Most important advice:** Review AI-generated code before merging
- Organizations that "vibe code" to production without review face trouble:
  - Codebase grows with tech debt
  - Duplicate code everywhere
  - Things get out of hand quickly
- **Actions required:**
  - Review code outputs
  - Pull and run code on workstation or ephemeral environment
  - Verify the problem was actually solved

### [Best Practice: Trust But Verify](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=695s)
**[11:15 - 12:30]**

- Build intuition over time for what agents do well vs. poorly
- Generally trust agents to operate consistently
- **Need human in the loop:**
- **OpenHands early learning:** PRs initially showed up as owned by OpenHands bot
  - **Problem 1:** Creator could approve their own PR, bypassing code review
  - **Problem 2:** PRs would languish with no clear owner for failing tests or issues
  - **Solution:** Now PRs show developer's face—they're responsible for merging and any breakage

### [Use Case 1: Resolving Merge Conflicts](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=752s)
**[12:32 - 13:23]**

- Brennan's favorite use case—"biggest chore as a part of my job"
- OpenHands codebase is fast-moving; no PR escapes without merge conflicts
- Simply comment: `@OpenHands fix the merge conflicts on this PR`
- Such a rote task—usually obvious what changed and why
- **Success rate:** OpenHands resolves correctly 99% of the time

### [Use Case 2: Addressing PR Feedback](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=803s)
**[13:23 - 13:53]**

- Someone else has already articulated what they want changed
- Just say: `@OpenHands do what that guy said`
- **Example:** Frontend engineer mentioned React buzzwords Brennan didn't know
  - OpenHands knew all of it and addressed feedback exactly as requested
- Works great because context is already well-defined

### [Use Case 3: Fixing Quick Bugs](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=833s)
**[13:53 - 14:22]**

- **Example:** Text input should have been number input
- Instead of digging through codebase to find right file:
  - Message directly from Slack: `@OpenHands fix this thing we were just talking about`
- Don't even need to fire up IDE—really fun way to work

### [Use Case 4: Infrastructure Changes](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=862s)
**[14:22 - 14:48]**

- Usually involves esoteric syntax in Terraform docs or similar
- LLMs tend to know the right syntax, or can look up documentation via browser
- **Example:** Out of memory exception in Slack → `@OpenHands increase the memory`

### [Use Case 5: Database Migrations](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=888s)
**[14:48 - 15:09]**

- Brennan admits he often leaves best practices behind:
  - Forgets indexes on the right things
  - Doesn't set up foreign keys correctly
- LLMs are great at following all best practices for database migrations
- Rote task for developers, not very fun—LLM excels at it

### [Use Case 6: Fixing Failing Tests](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=909s)
**[15:09 - 15:24]**

- Code is 90% done, unit test failing due to breaking API change
- Very easy to call in an agent to clean up failing tests

### [Use Case 7: Expanding Test Coverage](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=924s)
**[15:24 - 15:47]**

- **Why this is great:** Very safe task
  - As long as tests are passing, generally safe to merge
- Notice low coverage area in codebase
- Ask agent to expand test coverage in that area
- Quick win to make codebase safer

### [Use Case 8: Building Apps from Scratch](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=947s)
**[15:47 - 16:36]**

- **Production code:** Don't "vibe code" your way to production
- **Internal tools:** Great for quick internal apps
  - **Example:** OpenHands built web app to debug trajectories/sessions
  - Since it's internal, can "vibe code" a bit—don't need to review every line
  - Not facing end users
- Ability to quickly turn out applications for internal needs is powerful
- **Greenfield is a great use case for agents**

### [Closing](https://www.youtube.com/watch?v=o_hhkJtlbSs&t=991s)
**[16:31 - 16:39]**

- Join the OpenHands community:
  - **GitHub:** allhands-ai/hands
  - **Slack/Discord:** Available for collaboration
- Invitation to build together

---

## Key Takeaways

1. **Coding ≠ Software Engineering:** AI handles the typing; humans handle strategy, architecture, and empathy
2. **Start Small:** Begin with chores (merge conflicts, lint errors) before tackling larger features
3. **Be Explicit:** Tell agents what AND how—mention frameworks, files, strategies
4. **Code Is Cheap:** Experiment freely, throw away what doesn't work, iterate rapidly
5. **Always Review:** Never auto-merge AI code without human verification
6. **Human in the Loop:** Developers must own PRs—responsible for merging and any breakage
7. **Best Use Cases:** Rote tasks (migrations, conflicts, tests), infrastructure, internal tools
8. **90% AI, 10% Manual:** Power users now route most code through agents, only dropping into IDE for edge cases

---

**Last Updated:** 2026-01-03
