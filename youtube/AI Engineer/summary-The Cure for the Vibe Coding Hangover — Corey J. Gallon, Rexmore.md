# The Cure for the Vibe Coding Hangover — Corey J. Gallon, Rexmore

**Video URL:** https://www.youtube.com/watch?v=JsKTQbT58BY

---

## Executive Summary

Corey J. Gallon from Rexmore presents a comprehensive framework for building production software with AI coding agents. The talk addresses "vibe coding" - the low-spec, zero-planning approach that feels productive but results in unmaintainable code. The framework consists of 10 core principles, a structured 5-step planning phase, and a rigorous implementation loop. Rather than treating AI agents as replacements for engineering thinking, the framework positions developers as architects who delegate implementation while maintaining deep understanding and ownership of their code.

---

## Main Topics

### [Introduction: The Vibe Coding Problem](https://www.youtube.com/watch?v=JsKTQbT58BY&t=18s)
- **[00:18](https://www.youtube.com/watch?v=JsKTQbT58BY&t=18s)** - The cycle of inspiration: firing up AI coding agents, jamming in prompts, getting quick results
- **[00:50](https://www.youtube.com/watch?v=JsKTQbT58BY&t=50s)** - The Monday morning reality: can't understand, maintain, or modify the code
- **[01:06](https://www.youtube.com/watch?v=JsKTQbT58BY&t=66s)** - Definition: "Vibe coding" is low-spec, zero-planning AI development resulting in brittle, unmaintainable demoware
- **[01:17](https://www.youtube.com/watch?v=JsKTQbT58BY&t=77s)** - The "hangover" is the despair when trying to build maintainable software this way

**Key Points:**
- The talk targets developers who value programming as a learning experience
- Not for those satisfied with AI "doing it for you" without understanding
- Focus on building production applications that do real work

### [Framework Overview](https://www.youtube.com/watch?v=JsKTQbT58BY&t=217s)
- **[03:37](https://www.youtube.com/watch?v=JsKTQbT58BY&t=217s)** - Three pillars: Principles (philosophy), Process (workflow), and Tools (enablers)
- **[04:01](https://www.youtube.com/watch?v=JsKTQbT58BY&t=241s)** - Framework is adaptive to all types of software
- **[04:14](https://www.youtube.com/watch?v=JsKTQbT58BY&t=254s)** - Examples: litigation support apps, real-time appliance monitoring, digital publishing systems
- **[04:36](https://www.youtube.com/watch?v=JsKTQbT58BY&t=276s)** - These are real software applications doing real work, evolved and maintained by AI engineers

### [The 10 Principles](https://www.youtube.com/watch?v=JsKTQbT58BY&t=295s)

#### General Principles
- **[05:20](https://www.youtube.com/watch?v=JsKTQbT58BY&t=320s)** - **Principle 1: AI Engineering is Accelerated Learning**
  - Problem: Treating AI as pure productivity tool leads to dependency, not augmentation
  - Solution: Framework creates learning opportunities at every step
  - Mantra: "Always Be Learning"

- **[06:36](https://www.youtube.com/watch?v=JsKTQbT58BY&t=396s)** - **Principle 2: You are the Architect, Agent is the Implementer**
  - Keep boundaries crystal clear: you own thinking (architecture, interfaces, design)
  - Agent handles doing (typing code, following patterns, implementing tests)
  - Mantra: "Delegate the doing, not the thinking"

- **[07:31](https://www.youtube.com/watch?v=JsKTQbT58BY&t=451s)** - **Principle 3: Slow Down to Go Fast**
  - Problem: Starting over cycle without deliberate iteration
  - Solution: Deliberate iteration enables compounding returns on understanding and productivity
  - Week 1 feels slow, week 2 builds momentum, week 3 is dramatically faster
  - Mantra: "Compound progress, accelerate velocity"

#### Planning-Related Principles
- **[08:30](https://www.youtube.com/watch?v=JsKTQbT58BY&t=510s)** - **Principle 4: Specification > Prompt Engineering**
  - Specifications are structured, precise definitions vs. conversational prompts
  - Writing specs forces architectural thinking
  - Mantra: "Write the blueprint, not the prompt"

- **[09:47](https://www.youtube.com/watch?v=JsKTQbT58BY&t=587s)** - **Principle 5: Define Done Before Implementing**
  - Start with executable tests and observable success criteria
  - Agents get clear stop conditions and immediate feedback
  - Mantra: "Specify success, then build"

- **[11:25](https://www.youtube.com/watch?v=JsKTQbT58BY&t=685s)** - **Principle 6: Feature Atomicity**
  - Features must be atomic, irreducible tasks ready for complete agent execution
  - Prevents agents from making architectural decisions on the fly
  - Mantra: "Reduce until irreducible"

- **[12:21](https://www.youtube.com/watch?v=JsKTQbT58BY&t=741s)** - **Principle 7: Dependency-Driven Development**
  - Features form an interconnected graph, not independent tasks
  - Ensures agents never implement features depending on incomplete work
  - Mantra: "Schedule implementation by dependencies"

#### Implementation-Related Principles
- **[13:00](https://www.youtube.com/watch?v=JsKTQbT58BY&t=780s)** - **Principle 8: Implement One Atomic Feature at a Time**
  - Implementation quality requires sustained focus, complete context, tight feedback loops
  - Rhythm: implement → study → validate → commit → next feature
  - Mantra: "Complete one, commit one, continue"

- **[14:19](https://www.youtube.com/watch?v=JsKTQbT58BY&t=859s)** - **Principle 9: Context Engineering and Management**
  - Don't rely on conversational state persisting
  - Capture architectural decisions in persistent documents (specs, plans, design docs)
  - Mantra: "Curate context, don't accumulate it"

- **[15:14](https://www.youtube.com/watch?v=JsKTQbT58BY&t=914s)** - **Principle 10: Make It Work, Make It Right, Make It Fast**
  - Focus on "make it work" first - working software that can be shipped
  - Let real usage reveal what deserves further investment
  - Mantra: "Build, learn, improve"

### [The Planning Phase - 5 Steps](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1011s)

- **[17:00](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1020s)** - Planning transforms vague ideas into atomic, sequenced, fully-specified features
- **[17:43](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1063s)** - This is purely architect work; agent assists as thinking partner

#### Step 1: Vision Capture
- **[18:41](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1121s)** - Transform vague project idea into complete structured specification
- **[19:00](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1140s)** - Five sections to refine:
  1. **Project Purpose** - clarify problem, users, core value
  2. **Essential Functionality** - 3-5 fundamental workflows
  3. **Scope Boundaries** - "Now" (must have) vs "Not" (out of scope) vs "Next" (future)
  4. **Technical Context** - where it runs, how users interact, system connections
  5. **Workflow Details** - goal, high-level steps, expected outcomes
- **[21:07](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1267s)** - Output: Master Project Specification

#### Step 2: Feature Identification and Categorization
- **[21:43](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1303s)** - Extract all units of functionality from master spec
- **[21:57](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1317s)** - Organize into categorized feature inventory
- Prevents jumping directly from high-level vision to detailed specifications

#### Step 3: Feature Specification
- **[27:04](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1624s)** - Draft user stories (As a [user type], I want [action] so that [benefit])
- **[27:20](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1640s)** - **Implementation Contracts** - 3 levels of refinement:
  - Level 1: Plain English description of what feature does
  - Level 2: Logic flow (input → logic → output) in structured pseudo-code
  - Level 3: Formal interfaces with exact signatures, data structures, API specs
- **[28:24](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1704s)** - **Validation Contracts** - 3 levels:
  - Level 1: Plain English scenarios (happy path, error cases, edge cases)
  - Level 2: Test logic using Given-When-Then structure
  - Level 3: Formal test definitions with setup, inputs, assertions, teardown
- **[29:18](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1758s)** - Validate feature atomicity - can it be implemented in single focused session?
- **[29:53](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1793s)** - Identify dependencies - what other features must exist first?

#### Step 4: Dependency Analysis
- **[32:18](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1938s)** - Create dependency matrix: mark X where row feature depends on column feature
- **[32:25](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1945s)** - Generate graph visualization (GraphViz/Mermaid) showing features as nodes
- **[32:38](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1958s)** - Graph makes circular dependencies visible as closed loops
- **[32:49](https://www.youtube.com/watch?v=JsKTQbT58BY&t=1969s)** - Validate with binary dependency test
- **[33:31](https://www.youtube.com/watch?v=JsKTQbT58BY&t=2011s)** - Cycle resolution strategies:
  1. Dependency elimination (re-examine with binary test)
  2. Revised specification (rethink interfaces/contracts)
  3. Feature splitting (may not be atomic)
  4. Consolidation (last resort)

#### Step 5: Implementation Plan Development
- **[35:01](https://www.youtube.com/watch?v=JsKTQbT58BY&t=2101s)** - Transform dependency matrix into comprehensive phased roadmap
- **[37:05](https://www.youtube.com/watch?v=JsKTQbT58BY&t=2225s)** - Verify features work together, establish feedback loops for autonomous refinement
- **[37:27](https://www.youtube.com/watch?v=JsKTQbT58BY&t=2247s)** - Define complete execution strategy:
  - Phase gates (when is a phase complete?)
  - Task assignment guidance for agents
  - Blocker management process
  - Progress tracking (feature, phase, critical path levels)
- **[37:17](https://www.youtube.com/watch?v=JsKTQbT58BY&t=2237s)** - Binary progress tracking: feature is implemented or it's not (no "20% done")

### [The Implementation Loop](https://www.youtube.com/watch?v=JsKTQbT58BY&t=2307s)

- **[38:27](https://www.youtube.com/watch?v=JsKTQbT58BY&t=2307s)** - Planning artifacts guide transformation of specs into working software
- **[38:39](https://www.youtube.com/watch?v=JsKTQbT58BY&t=2319s)** - Unlike linear planning, implementation is a tight rapid loop executed repeatedly
- **[38:52](https://www.youtube.com/watch?v=JsKTQbT58BY&t=2332s)** - Multiensory feedback loop concept introduced

**Key Distinguishing Features:**
- Planning is linear (5 sequential steps), implementation is cyclical
- Each atomic feature goes through the complete implementation loop
- Continuous validation through tests (correctness) and sensors (actual behavior)

---

## Key Takeaways

1. **Vibe coding creates technical debt**: Fast initial results lead to unmaintainable code that must be thrown away
2. **Architect vs. Implementer separation**: Developers must retain architectural thinking while delegating implementation
3. **Specification is king**: Structured, precise specifications trump conversational prompt engineering
4. **Atomicity matters**: Features must be irreducible, single-focus units of work
5. **Dependencies drive sequencing**: Understanding feature relationships prevents wasted implementation effort
6. **Learning compounds**: The framework treats each step as a learning opportunity, building engineer capabilities
7. **Context must be engineered**: Don't rely on conversational state; capture decisions in persistent artifacts
8. **Binary validation**: Features are either done or not done - no partial completion tracking
9. **Five-phase planning**: Vision → Features → Specification → Dependencies → Plan
10. **Make it work first**: Focus on working software before elegance or performance optimization

---

## Practical Applications

The framework enables building production software including:
- Specialized litigation support applications for law firms
- Real-time appliance monitoring packages for cooking
- Digital publishing systems for dynamic content replatforming
- Any type of software requiring maintainability and evolution over time

The approach is particularly valuable for AI engineers who:
- Want to understand and own the code they build
- Need to maintain and evolve software over time
- Value programming as a craft and learning experience
- Build production applications that do real work
- Want to be "boss of the coding agents, not their confused intern"

---

**Last Updated:** 2026-01-01
