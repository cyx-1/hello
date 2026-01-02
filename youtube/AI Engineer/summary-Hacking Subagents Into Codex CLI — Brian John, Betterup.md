# Hacking Subagents Into Codex CLI — Brian John, Betterup

**Video URL:** https://www.youtube.com/watch?v=5eJqXtevlXg

---

## Executive Summary

Brian John, Principal Fullstack Engineer at BetterUp, demonstrates how to implement subagents in OpenAI's Codex CLI to achieve workflow portability and better context management. The talk covers the motivation for avoiding tool lock-in, design architecture using wrapper scripts, navigating Codex's sandbox permissions, and provides a working proof-of-concept implementation. Key challenges include figuring out minimum required permissions and working within Codex's security constraints.

---

## Main Topics

### [Introduction & Motivation](https://www.youtube.com/watch?v=5eJqXtevlXg&t=5s)
**Timestamp:** 00:00 - 02:00

- Brian John introduces himself as Principal Fullstack Engineer at BetterUp focused on AI enablement for R&D
- **Why hack subagents into Codex CLI:**
  - Avoid lock-in to one tool or model family
  - Want to use Codex CLI models while maintaining subagent workflows from Claude Code
  - Context management benefits: subagents consume tokens separately, preventing main context window pollution
  - Credits [Dex Hory's talk](https://www.youtube.com/watch?v=5eJqXtevlXg&t=128s) for changing how he works with AI, especially for large codebases

### [Design Architecture](https://www.youtube.com/watch?v=5eJqXtevlXg&t=160s)
**Timestamp:** 02:40 - 04:00

- **Simple architecture:** Subagent is just another instance of the main agent
- **Workflow:**
  1. Parent Codex session runs a wrapper script
  2. Wrapper script determines which agent to run and builds the prompt
  3. Kicks off `codex exec` as child process
  4. Child Codex runs as subagent, does its work
  5. Subagent writes answer to a file
  6. Wrapper script reads file and prints to stdout
  7. Result returns to parent Codex session

### [Permission Challenges](https://www.youtube.com/watch?v=5eJqXtevlXg&t=208s)
**Timestamp:** 03:28 - 05:00

- **Initial assumption:** Simple design should be easy to implement - proved wrong
- **Codex sandbox restrictions:** Really doesn't want you to do this
- Can bypass with "dangerously skip permissions" but author avoids this
- **Figuring out minimum required permissions was the hardest part:**
  - **Parent process:** Needs at least `sandbox=workspace` to run codex command
  - **Child process (trickier):**
    - Sandbox prevents access to OpenAI credentials in home directory (outside workspace)
    - Needs `sandbox=workspace-write` so it can write output file
    - Must disable "rollout recorder" (logging mechanism) because parent sandbox prevents filesystem access to subcommands outside workspace

### [Security Considerations](https://www.youtube.com/watch?v=5eJqXtevlXg&t=302s)
**Timestamp:** 05:02 - 06:15

- References Meta's "Agent's Rule of Two" paper
- **Three security factors to evaluate:**
  1. Processing untrustworthy input? (No in this case)
  2. Access to sensitive systems or private data? (Yes - proprietary codebase)
  3. Can change state or communicate externally? (Yes - changes codebase, calls OpenAI API)
- **Risk assessment:** Lower risk category (not processing untrusted input)
  - State changes: Low risk in Brian's case
  - External communication: Only to OpenAI API endpoint, not major risk
- **Important caveat:** Lower risk ≠ no risk - users must make their own determination

### [Implementation Details](https://www.youtube.com/watch?v=5eJqXtevlXg&t=378s)
**Timestamp:** 06:18 - 09:00

- **Telling Codex how to run subagents (agents.md):**
  - Defines agent name, reasoning effort (light/medium/high), and prompt
  - Similar to Claude Code subagent configuration
  - Examples: word counter agent, file writer agent
- **Wrapper script:** Only 72 lines of Python
  - Takes inputs, calls AgentExecutor Python class
  - Returns agent output to stdout for parent agent
- **AgentExecutor class:** Handles the heavy lifting
  - Kicks off child subagent with proper permissions
  - Sets correct reasoning effort
  - Disables rollout recorder

### [Permission Management Trick](https://www.youtube.com/watch?v=5eJqXtevlXg&t=540s)
**Timestamp:** 09:00 - 10:09

- **Key insight:** Codex permissions are command-based
  - If command looks exactly the same, you only grant permission once
  - Different arguments = need approval every time
- **Solution:** Write agent name and query to files instead of passing as command arguments
  - Makes the bash command identical every time
  - Avoids annoying permission prompts for each subagent call
  - Only matters if NOT using "dangerously skip permissions"
- **Codex wrapper script:** Syncs Codex home files from home directory into subdirectory within workspace so child process can access them

### [Live Demo](https://www.youtube.com/watch?v=5eJqXtevlXg&t=606s)
**Timestamp:** 10:06 - 13:08

- Demonstrates proof-of-concept repository (open source)
- **First demo:** Word counter subagent
  - Shows Codex writing agent name and query to files
  - Requests permission for first run - important to say "yes and don't ask again"
  - Agent executes and returns result
- **Performance notes:**
  - Codex runs everything serially (no async like Claude Code)
  - Generally slower than Claude Code
  - Intentional design: Codex meant for hands-off/unattended work vs Claude Code's iterative style
  - Brian finds this acceptable for his use case
- **Second demo:** File writer subagent
  - Same workflow, no permission prompt this time
  - Uses 600s timeout (some agents can take 10-20 minutes on large codebases)
  - Completes in ~40 seconds for simple task
- Successfully verifies file was written

### [Conclusion & Resources](https://www.youtube.com/watch?v=5eJqXtevlXg&t=788s)
**Timestamp:** 13:08 - 13:36

- Code available at repository URL (shown in video)
- BetterUp is hiring: betterup.com
- Contact: Email or X DMs welcome
- Encourages viewers to reach out if interested in working with LLMs at BetterUp

---

## Key Takeaways

1. **Subagents enable workflow portability** across different AI coding tools while managing context efficiently
2. **Codex sandbox permissions are the main challenge** - requires careful configuration of minimum permissions
3. **Simple architecture:** Wrapper script + file-based communication between parent and child Codex sessions
4. **Permission trick:** Use identical bash commands with file-based parameters to avoid repeated permission prompts
5. **Security matters:** Evaluate using Meta's "Rule of Two" framework before implementing
6. **Performance tradeoff:** Serial execution makes Codex slower but suits hands-off workflows
7. **Open source proof-of-concept** available for anyone to try

---

**Last updated:** 2026-01-01
