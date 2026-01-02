# Proactive Agents – Kath Korevec, Google Labs

**Video URL:** https://www.youtube.com/watch?v=v3u8xc0zLec

---

## Executive Summary

Kath Korevec from Google Labs ADA team presents the vision and implementation of proactive AI agents in their coding assistant tool, Jules. She argues that current AI developer tools are fundamentally reactive, forcing developers to maintain a "mental load" of managing agents rather than focusing on creative work. The talk introduces a three-level framework for proactive systems and demonstrates how Jules is evolving from a reactive assistant to a proactive collaborator that can automatically detect issues, learn developer preferences, and work autonomously across the full software development lifecycle.

---

## Main Topics

### [Introduction: The Mental Load Problem](https://www.youtube.com/watch?v=v3u8xc0zLec&t=23s)
**Timestamp:** [00:23](https://www.youtube.com/watch?v=v3u8xc0zLec&t=23s) - [02:00](https://www.youtube.com/watch?v=v3u8xc0zLec&t=120s)

- Uses dishwasher analogy to explain the "mental load" problem with async agents
- Even when agents handle work, developers still carry the burden of monitoring and managing them
- Humans are serial processors, not parallel - context switching costs up to 40% of productive time
- The viral Twitter post of 16 Claude Code terminals represents a dystopian developer experience we should avoid

**Key Points:**
- Agents should "do the dishes without being asked"
- Developers want to code and build, not manage agents
- Current async agents require babysitting, defeating their purpose

---

### [Four Essential Ingredients of Proactive Systems](https://www.youtube.com/watch?v=v3u8xc0zLec&t=270s)
**Timestamp:** [04:30](https://www.youtube.com/watch?v=v3u8xc0zLec&t=270s) - [05:43](https://www.youtube.com/watch?v=v3u8xc0zLec&t=343s)

The four essential ingredients for proactive AI systems:

1. **Observation** - Continually understanding code changes, patterns, and workflow
2. **Personalization** - Learning how you work, what you care about, preferences, and code you don't want touched
3. **Timeliness** - Intervening at the right moment (not too early to interrupt, not too late to miss the moment)
4. **Seamless Integration** - Working where you already are (terminal, IDE, repository) without forcing you elsewhere

**Key Points:**
- Proactive systems already exist around us (Google Nest, human body reflexes)
- Proactivity for AI is familiar and human, not futuristic
- Building tools that behave like good collaborators, not command-line utilities

---

### [Three Levels of Proactivity in Jules](https://www.youtube.com/watch?v=v3u8xc0zLec&t=414s)
**Timestamp:** [06:54](https://www.youtube.com/watch?v=v3u8xc0zLec&t=414s) - [08:59](https://www.youtube.com/watch?v=v3u8xc0zLec&t=539s)

**Level 1: Attentive Sous Chef**
- Detects missing tests, unused dependencies, unsafe patterns
- Automatically fixes issues while working on other tasks
- Keeps the "kitchen clean" so developers can focus on what's next

**Level 2: Kitchen Manager**
- Becomes contextually aware of entire project
- Observes how you work and what you need help with (backend engineer needs React help, designer needs database schema)
- Learns frameworks and deployment styles
- Anticipates what you need next

**Level 3: Collective Intelligence** (Currently being developed for December release)
- Understands not just context, but consequence
- Multiple agents working together:
  - **Jules** - Sees what's breaking in software
  - **Stitch** - Design agent understanding user interactions
  - **Insights** - Data agent connecting analytics, telemetry, conversion rates
- Proposes improvements across system boundaries
- Human stays firmly in the loop to observe, refine, and redirect

**Key Points:**
- Level 3 is about alignment to project, not just autonomy
- Agents and humans collaborate across full project lifecycle

---

### [Jules' New Proactive Features](https://www.youtube.com/watch?v=v3u8xc0zLec&t=565s)
**Timestamp:** [09:25](https://www.youtube.com/watch?v=v3u8xc0zLec&t=565s) - [11:01](https://www.youtube.com/watch?v=v3u8xc0zLec&t=661s)

Moving Jules toward system awareness with new features:

- **Memory** - Jules writes its own memories that users can edit and interact with
- **Critic Agent** - Works adversarially with Jules for code quality and full code reviews
- **Verification** - Writes Playwright scripts, takes screenshots, puts them back in trajectory for validation
- **To-Do Bot** - Scans repository for TODOs and proactively works on them with context
- **Best Practices** - Understands and suggests best practices
- **Environment Setup** - Environment agent for better understanding and automatic setup
- **Just-In-Time Context** - "Cheat sheet" for Jules when stuck on specific tasks, reducing need to ask user

---

### [Demo: Proactivity in Action](https://www.youtube.com/watch?v=v3u8xc0zLec&t=664s)
**Timestamp:** [11:04](https://www.youtube.com/watch?v=v3u8xc0zLec&t=664s) - [13:09](https://www.youtube.com/watch?v=v3u8xc0zLec&t=789s)

Demonstration of proactive Jules workflow (on ADK Python repository):

1. Jules indexes entire codebase when proactivity is enabled
2. Finds TODOs and best practice improvements automatically
3. Shows confidence levels: High (green), Medium (purple), Low (yellow)
4. Users can manually start tasks or delete suggestions
5. Can drill into tasks to see code suggestions, location, and rationale
6. Future: Automatically starting high-confidence tasks without user intervention

**Key Points:**
- Reduces cognitive load - no need to think about prompts or look at code first
- Provides transparency through rationale and confidence levels
- Coming in December 2024

---

### [Personal Story: The Animatronic Head](https://www.youtube.com/watch?v=v3u8xc0zLec&t=801s)
**Timestamp:** [13:21](https://www.youtube.com/watch?v=v3u8xc0zLec&t=801s) - [15:28](https://www.youtube.com/watch?v=v3u8xc0zLec&t=928s)

Real-world example of the problem Jules aims to solve:

- Built 6-foot animatronic head for Halloween (based on Pee-wee Herman)
- Wanted to focus on creative parts: LED animations, eye tracking, laser effects
- Instead spent most time fixing bugs, swapping libraries, debugging
- Current workflow: Prompt Jules → Wait 10 minutes → Repeat (very tedious)
- Vision: Jules does research and handles "ugly parts" so user can focus on creativity
- Ended up shipping less than desired due to time spent on maintenance tasks

**Key Points:**
- Gap between tool friction and creative freedom is what proactive agents aim to close
- This personal frustration drives the team's vision for Jules

---

### [Call to Action: Inventing the Future](https://www.youtube.com/watch?v=v3u8xc0zLec&t=932s)
**Timestamp:** [15:32](https://www.youtube.com/watch?v=v3u8xc0zLec&t=932s) - [16:34](https://www.youtube.com/watch?v=v3u8xc0zLec&t=994s)

- Products we build today won't be the products of the future
- Current patterns (Git, IDEs, how we think about code) might not exist in 6 months or a year
- We get to invent the future right now - decide how software is made and built
- Challenge: Don't be afraid to question old ways of building software
- The future is coming faster than we know (probably already here)
- We get to build it together

**Key Points:**
- Embrace radical change in developer tooling
- Be willing to reimagine fundamental workflows
- Community collaboration is key to shaping the future

---

## Notable Quotes

> "I realized that even though I wasn't physically washing the dishes, I was still carrying this mental load."

> "Humans, we are serial processors, not parallel ones... switching between tasks comes with a huge cost. It can cost up to 40% of your productive time."

> "We need collaborators in our system that we can trust. Agents that really understand context, can anticipate our needs, and they know really when to step in."

> "We want Jules to do the dishes without being asked."

> "Proactivity for AI is actually not that futuristic. It's very familiar and it is very human."

> "Level three isn't really about autonomy anymore. It's actually about alignment to your project."

> "The future is coming faster than any of us know. It's probably already here and the cool thing is we get to build it together."
