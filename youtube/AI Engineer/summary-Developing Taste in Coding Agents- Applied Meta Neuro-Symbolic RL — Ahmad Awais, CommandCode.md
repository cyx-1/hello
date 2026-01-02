# Developing Taste in Coding Agents: Applied Meta Neuro-Symbolic RL — Ahmad Awais, CommandCode

**Video URL:** https://www.youtube.com/watch?v=kWOQS3XPZ10

---

## Executive Summary

Ahmad Awais, creator of CommandCode and CEO of Langbase, introduces CommandCode—a coding agent that learns developers' coding preferences and "taste" through a meta neuro-symbolic reinforcement learning architecture. Unlike traditional coding agents that require constant steering through prompts or rules files, CommandCode continuously learns from how developers edit its code, capturing the "invisible architecture of choices" that define good code beyond mere correctness. The system uses a hybrid approach combining LLMs with a deterministic neuro-symbolic reasoning layer that learns and enforces personal coding preferences, from CLI library choices to version numbering conventions. Early results at Langbase show 10x increase in merged code with significantly reduced review time.

---

## Main Topics

### [Introduction and Background](https://www.youtube.com/watch?v=kWOQS3XPZ10&t=0s)
**Timestamp:** 00:00 - 02:00

- Ahmad Awais introduces CommandCode, a "coding agent with taste" developed over a year
- Background: Creator of hundreds of open source packages, contributor to NASA Mars helicopter mission
- Started working with GPT-3 in 2020 (3 years before ChatGPT, 1 year before GitHub Copilot)
- Motivation: Wanted AI to learn from his coding patterns rather than constantly requiring instruction
- Core problem: Existing coding agents don't understand individual developer preferences and style

**Key Points:**
- CommandCode features "taste is on" - continuously learning from developer patterns
- Ahmad's extensive background in CLI development and automation
- Early vision to build AI that suggests next lines of code

### [Live Demo: CLI Building Comparison](https://www.youtube.com/watch?v=kWOQS3XPZ10&t=136s)
**Timestamp:** 02:16 - 06:00

- Side-by-side comparison: Claude Code vs CommandCode building a CLI for ISO date formatting
- CommandCode automatically picks up preferences from previous CLI projects
- Claude produces basic console.log implementation while CommandCode uses:
  - TypeScript with tsx/tup
  - Commander.js for CLI framework
  - pnpm package manager
  - Lowercase version flag (-v)
  - Separate commands directory structure
  - Vitest for testing
  - Version 0.0.1 (not 1.0.0)
  - ASCII art banner
  - NPM linking

**Key Points:**
- CommandCode learns preferences without explicit instruction
- Transparent learning stored in `.commandcode/taste` files
- Preferences include project structure, tooling choices, version conventions
- None of the taste file was manually written by the developer

### [The Problem: AI is Sloppy by Default](https://www.youtube.com/watch?v=kWOQS3XPZ10&t=433s)
**Timestamp:** 07:13 - 09:50

- Journey from 2020 GPT-3 access through building Langbase (raised $5M, led by GitHub founder)
- Langbase processes 700TB and 1.2B agent runs per month
- Core observation: AI learns human laziness - produces "sloppy" code by default
- Example: "Horse on staircase banister" image generation analogy
- Problem extends to writing: generic corporate language like "power of synergistic teamwork"
- Initial attempts: Built "Chai" (later CommandNew) - agent-of-agents that provisions infrastructure
- 150,000 agents built in 5 months, but still missing something critical

**Key Points:**
- LLMs try to be "correct as soon as possible" rather than truly good
- Vibe coding is better than sloppy but not better than experienced developer choices
- Traditional approaches: rules files (claude.md, agents.md) are never enough
- Analogy: Justice system needs human interpretation beyond just rules

### [The Taste Concept: Invisible Architecture of Choices](https://www.youtube.com/watch?v=kWOQS3XPZ10&t=590s)
**Timestamp:** 09:50 - 12:21

- Beyond correctness: "Good code" embodies invisible architecture of career-built choices
- Example comparison: JavaScript function parameters
  - AI default: Multiple individual parameters
  - Developer preference: Object parameters when >2 arguments
- CLI example reinforces learned preferences:
  - TypeScript, Commander, pnpm, version flags
  - These aren't specs or rules but intuition patterns
- Core insight: Programmers talk about code that is readable, maintainable, humane, and "more like you"

**Key Points:**
- Taste = invisible architecture of choices made throughout career
- Rules alone can't capture this (would spend all time writing rules instead of code)
- Goal: Generate thousands of PRs merged to main with 90-99% reduced review time
- Can't manually teach all rules - need continuous learning from actual coding behavior

### [Technical Architecture: Meta Neuro-Symbolic RL](https://www.youtube.com/watch?v=kWOQS3XPZ10&t=843s)
**Timestamp:** 14:03 - 16:00

- Neuro-symbolic architecture: More deterministic and explainable than pure transformers
- Transformers are generative and probabilistic; neuro-symbolic adds deterministic layer
- Formula components:
  - LLMs (Claude, GPT, etc.) remain the base
  - Meta neuro-symbolic space: "Redux of choices" in Petri net form
  - KL divergence loop for error correction
  - Continuous learning from explicit and implicit feedback
- Creates deterministic enforcement of invisible logic around developer choices

**Key Points:**
- LLMs are "good enough" - enhancement comes from taste layer
- Reflective context engineering: Self-aware and continuously adapting
- Example: Automatically detects switch from "meow" to "commander" CLI library
- No manual teaching required - learns from observing code edits
- Over time develops "skill of intuition"

### [Taste Sharing and Ecosystem](https://www.youtube.com/watch?v=kWOQS3XPZ10&t=984s)
**Timestamp:** 16:24 - 18:40

- Vision: Marketplace for developer taste profiles
- Use cases:
  - Borrow React patterns from developers like Tanner Linsley (TanStack)
  - Team member specialization: Use design engineer's taste for frontend work
  - All margins, paddings, tiny design details captured in taste model
- Enterprise applications: Enforce company-wide coding standards
- Open source vs. team-private taste models
- Combined approach: LLM + meta neuro-symbolic design taste + developer request

**Key Points:**
- Taste is shareable and composable
- Can combine multiple taste profiles (e.g., personal + design engineer)
- Potential for "npx taste install" workflow
- Democratizes expert-level patterns across teams
- World's knowledge (LLMs) + world's intuition (taste models)

### [Launch and Results](https://www.youtube.com/watch?v=kWOQS3XPZ10&t=1048s)
**Timestamp:** 17:28 - 20:48

- Launching at commandcode.ai
- Current implementation: Transparent markdown files in projects
- Exploring best format for meta-learning integration
- Internal Langbase results:
  - 10x increase in code merged to main branch
  - Significantly reduced PR review time
  - Increased confidence in code quality during reviews
- Vision: Next frontier of coding through taste models
- Call to action: Try CommandCode and share what you build

**Key Points:**
- Very early stage product - seeking community feedback
- Taste currently stored as transparent markdown
- Could evolve into any format for the meta-symbolic model
- Dramatic productivity improvements demonstrated internally
- Focus on learning from developer's actual coding behavior

---

## Technical Concepts Explained

**Neuro-Symbolic Architecture:**
- Combines neural networks (LLMs) with symbolic AI (logic rules)
- More deterministic and explainable than pure neural approaches
- Captures patterns that can't be easily expressed as explicit rules

**Meta-Learning:**
- Learning how to learn from developer edits and choices
- Builds models of developer preferences over time
- Applies learned patterns to new situations

**Reinforcement Learning (RL):**
- System improves through feedback loops
- Explicit feedback: Developer edits to AI-generated code
- Implicit feedback: Choices made in context

**Taste Models:**
- Representation of developer's "invisible architecture of choices"
- Goes beyond correctness to capture style, preferences, and patterns
- Shareable and composable across teams

---

## Key Quotes

> "AI is lazy by default. It's very sloppy. The best thing AI has learned from humans is that humans are lazy."

> "When programmers talk about good code, they're not talking about code that is correct. They're talking about this invisible architecture of choices that they have made throughout the course of their career."

> "I can either write code or I can teach it to write code. I cannot be the one who's telling it every time."

> "Large language models have captured the world's knowledge... what we are building with taste models is the world's intuition."

---

## Resources

- **Product:** commandcode.ai
- **Company:** Langbase
- **Research:** stateofiagents.com
- **Twitter:** @MrAhmadAwais (implied from presentation style)

---

*Summary created from AI Engineer conference talk*