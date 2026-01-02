# Backlog.md: Terminal Kanban Board for Managing Tasks with AI Agents — Alex Gavrilescu, Funstage

**Video URL:** https://www.youtube.com/watch?v=zMXKhhwiCIc

---

## Executive Summary

Alex Gavrilescu presents Backlog.md, an open-source terminal-based Kanban board designed for project management with AI agents and humans. The tool addresses common issues with AI agents like running out of context window or going in wrong directions by dividing big features into smaller markdown tasks. The presentation demonstrates building a new feature (task moving/reordering) using Claude Code, showcasing Backlog.md's workflow through task creation, planning, and implementation phases. The tool uses MCP (Model Context Protocol) to expose resources and tools to AI agents, enabling them to create, update, and execute tasks autonomously while maintaining clear review checkpoints for human oversight.

---

## Main Topics

### [Introduction to the Problem and Solution](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=2s)
**[00:02 - 00:33]**

- Common problem: AI agents working for an hour in the wrong direction or running out of context window
- Solution: Workflow consisting of dividing big features into smaller markdown tasks
- Introduction to Backlog.md: a tool for project management for AI agents and humans

**Key Points:**
- Addresses context window limitations of AI agents
- Prevents wasted time from agents going in wrong directions
- Provides structured approach to feature development

### [Terminal Kanban Board Demo](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=36s)
**[00:36 - 01:33]**

- First terminal Kanban board built when none existed
- Full Kanban board directly in terminal showing tasks for current project
- Three columns: To Do, In Progress, Done
- View task details including description, acceptance criteria, and implementation notes
- Desired new feature: ability to move tasks between status columns and reorder tasks within columns

**Key Points:**
- Terminal-native user interface
- Traditional Kanban workflow (To Do → In Progress → Done)
- Task details accessible directly in terminal
- Implementation notes support for tracking work

### [Defining Clear Requirements for AI Agents](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=93s)
**[01:33 - 02:23]**

- Importance of clear requirements for both humans and AI agents
- Specific requirements for move mode feature:
  - Press M to toggle move mode
  - Current task gets highlighted
  - Use arrow keys up/down to reorder within column
  - Use arrow keys left/right to change task status
  - Press M or Enter to commit the move
  - Press Esc to cancel
  - Footer shows button instructions to inform users

**Key Points:**
- Clear requirements prevent misunderstandings
- Detailed specification of user interactions
- User experience considerations (footer instructions)

### [Task Creation Workflow](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=143s)
**[02:23 - 03:35]**

- Claude creates task based on given requirements
- Agent first needs to understand what Backlog.md is (onboarding like a new developer)
- Reads documentation about Backlog.md
- Reads about how to create tasks correctly
- Creates the task with proper structure

**Key Points:**
- AI agent acts like newly onboarded developer
- Learns project context before creating tasks
- Follows documentation and guidelines

### [Markdown Task File Structure](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=194s)
**[03:14 - 04:08]**

- Tasks stored as markdown files in repository
- Front matter section with metadata: task ID, title, labels, and other fields
- Description section explaining the purpose
- Example: "Add the move mode feature in the TUI Kanban board that allows users to interactively reorder tasks within columns and move tasks between status columns using keyboard navigation"
- Provides intuitive way to reorganize without CLI commands or direct file editing

**Key Points:**
- Git-friendly markdown format
- Structured metadata in front matter
- Clear, detailed descriptions
- Agent demonstrates understanding of task purpose

### [Acceptance Criteria Section](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=248s)
**[04:08 - 04:38]**

- Critical section defining how feature should behave
- Must be testable and easily verifiable
- First review checkpoint: verify AI agent understood your intent
- Opportunity to catch misunderstandings early

**Key Points:**
- Testable criteria prevent ambiguity
- Early review point saves time
- Validates agent comprehension before implementation

### [Implementation Plan Creation](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=278s)
**[04:38 - 05:40]**

- AI agent must create implementation plan
- Agent checks documentation, internet, and existing codebase
- Determines where to place the feature
- Writes detailed implementation plan

**Key Points:**
- Research phase before coding
- Understanding existing architecture
- Planning prevents rework

### [MCP (Model Context Protocol) Architecture](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=340s)
**[05:40 - 06:57]**

- Backlog.md uses MCP server to expose information and tools
- **Resources** (special MCP feature):
  - Workflow overview: explains what Backlog.md is and what it's used for
  - Task creation guide: required and optional fields
  - Task execution guide: steps like setting status to "in progress" and assigning tasks
  - Task completion guide: checking acceptance criteria and definition of done

**Key Points:**
- MCP provides structured agent instructions
- Resources define workflow and guidelines
- Guides cover full task lifecycle

### [MCP Tools for AI Agents](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=417s)
**[06:57 - 07:41]**

- Backlog.md server exposes tools for agents to run commands natively
- Key tools:
  - Search tasks (before creating new ones)
  - View task details
  - Create tasks
  - Update tasks
  - Update acceptance criteria

**Key Points:**
- Native integration for AI agents
- Prevents duplicate task creation
- Full CRUD operations on tasks

### [Implementation Plan Review](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=461s)
**[07:41 - 08:21]**

- Architecture overview provided
- Implementation steps enumerated
- Files to be modified listed with explanations
- Second and most important review checkpoint
- Senior software engineer can verify agent is going in right direction
- Critical to double-check everything before implementation

**Key Points:**
- Detailed technical plan before coding
- Human oversight prevents costly mistakes
- File-level change planning

### [Implementation Phase](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=501s)
**[08:21 - 09:04]**

- Agents (Claude, Gemini, Kusso) work with Backlog.md
- Agent learns: task description, acceptance criteria, and plan
- "Develop the feature" means: implement all acceptance criteria and move task to Done when definition of done is fulfilled
- Implementation takes time (video paused during this phase)

**Key Points:**
- Multiple AI agents supported
- Clear definition of "done"
- Autonomous implementation with defined scope

### [Backlog Workflow Overview](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=544s)
**[09:04 - 09:59]**

- Humans create tasks (can use AI agents to help)
- Human provides description of what to implement
- AI agent runs Backlog commands to create task and fill sections
- Once created, simple instruction: "Hey Claude, can you please implement task 316?"
- Agent executes autonomously

**Key Points:**
- Human-AI collaboration model
- Natural language task assignment
- Simplified task execution

### [Live Demo of Implemented Feature](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=599s)
**[10:02 - 10:58]**

- New Kanban board shows "M to move" command
- Press M: task gets highlighted
- Arrow keys up/down: move within column
- Arrow keys left/right: change status column
- Can commit or cancel moves
- Successfully moved task 316 back to "In Progress"

**Key Points:**
- Feature works as specified
- Intuitive keyboard navigation
- Visual feedback (highlighting)

### [Why This Approach Works Well](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=658s)
**[11:00 - 12:20]**

- **Context engineering**: Markdown tasks allow defining how much AI should implement in single task
- Prevents context window overflow
- Exact control over what gets implemented (no unwanted extra features)
- **Atomic tasks**: Easy rollback if something goes wrong
- Can change specs/acceptance criteria and restart from implementation plan
- **Well-defined scope**: Acceptance criteria clearly define what's in/out of scope
- **Unit tests**: Check if acceptance criteria are met

**Key Points:**
- Context management through task sizing
- Scope control prevents feature creep
- Easy iteration and refinement
- Testing aligned with acceptance criteria

### [Three Review Checkpoints](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=740s)
**[12:20 - 12:41]**

1. **After task creation**: Check description and acceptance criteria - did agent understand your intent?
2. **Implementation plan**: Is agent going in right direction?
3. **Code review**: Final review of implemented code

**Key Points:**
- Early detection of misunderstandings
- Progressive validation
- Human oversight at critical points

### [Parallel Task Execution](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=761s)
**[12:43 - 12:51]**

- Can work on multiple tasks in parallel using Git worktrees
- Works when there are no dependencies between tasks

**Key Points:**
- Scalable workflow
- Git integration for parallel work
- Dependency awareness

### [Backlog.md Features and Characteristics](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=771s)
**[12:51 - 13:45]**

- Open-source MIT license
- CLI tool with terminal UI and web interface
- AI agents can interact via:
  - CLI commands (legacy support)
  - MCP (preferred native way)
- Cross-platform (works on most operating systems)
- No extra APIs, tools, databases, or accounts needed
- Tasks hosted in Git repository
- Team sharing and sync capabilities
- Checks task status across branches

**Key Points:**
- Free and open source
- Multiple interaction methods
- Simple deployment (no infrastructure)
- Git-based collaboration
- Branch-aware task tracking

### [AI-Generated Codebase](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=825s)
**[13:45 - 13:57]**

- 99% of Backlog.md code written by AI agents
- Author only wrote: instructions and first three tasks
- Self-demonstrating example of the workflow's effectiveness

**Key Points:**
- Dogfooding the product
- Proves viability of AI-assisted development
- Minimal human coding required

### [Call to Action and Resources](https://www.youtube.com/watch?v=zMXKhhwiCIc&t=837s)
**[13:57 - 14:13]**

- Visit backlog.md to learn more and experiment
- Author available to help with onboarding

**Key Points:**
- Active community support
- Website: backlog.md
- Open to feedback and questions

---

## Key Takeaways

1. **Problem Solved**: Backlog.md addresses AI agent context window limitations and direction drift by breaking features into atomic markdown tasks
2. **Workflow**: Three-phase process (task creation → implementation planning → execution) with three review checkpoints
3. **Technology**: Uses MCP to expose resources and tools to AI agents for native integration
4. **Collaboration**: Enables human-AI collaboration where humans define requirements and AI agents execute tasks autonomously
5. **Control**: Acceptance criteria and scope definition prevent feature creep and ensure testability
6. **Simplicity**: Git-based storage, no external dependencies, cross-platform support
7. **Proven Approach**: 99% of Backlog.md itself was built using this workflow with AI agents

---

## Target Audience

- Software engineers working with AI coding agents (Claude Code, Cursor, etc.)
- Teams looking to integrate AI into development workflows
- Developers seeking better task management for AI-assisted coding
- Project managers interested in AI-human collaboration tools
