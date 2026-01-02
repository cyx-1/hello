# Defying Gravity - Kevin Hou, Google DeepMind

**Video URL:** https://www.youtube.com/watch?v=HN-F-OQe6j0

---

## Executive Summary

Kevin Hou, product engineering lead for Google Anti-gravity at DeepMind, unveils Google's groundbreaking AI developer platform called "Anti-gravity." This presentation reveals how Anti-gravity represents the next evolution in AI-assisted development, moving beyond autocomplete and chat to a fully agent-first IDE. The platform integrates three surfaces: an AI editor (VS Code fork), an agent-controlled Chrome browser, and an innovative "agent manager" interface that provides a higher-level view of development work. Launched alongside Gemini 3 Pro, Anti-gravity leverages Google's multimodal AI capabilities, computer use functionality, and introduces a novel "artifacts" system for human-agent collaboration. The presentation details the product's architecture, demonstrates its unique features, and explains the research-product flywheel that gives Google a competitive advantage in building the future of AI-assisted development.

---

## Main Topics

### 1. [Introduction and Product Overview](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=0s)
**Timestamps: 00:00 - 02:00**

- Anti-gravity is Google DeepMind's first IDE from a foundational AI lab
- Launched Tuesday alongside Gemini 3 Pro
- Platform is "unapologetically agent first"
- Three main surfaces: Editor, Browser, and Agent Manager
- Product is brand new and still being actively developed
- Playful reference to "Wicked 2" - both defying gravity this week

### 2. [The Three Surfaces of Anti-gravity](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=120s)
**Timestamps: 02:00 - 05:00**

**Agent Manager:**
- Central hub that provides agent-first view, one level higher than just looking at code
- Single window that manages all agent activity
- Pulls developers to a higher level than viewing diffs

**AI Editor:**
- VS Code fork with lightning-fast autocomplete
- Agent sidebar that mirrors the agent manager
- Command/Control+E for instant switching to agent manager (under 100ms)
- Handles the 80-100% completion work when agents can't fully automate

**Agent-controlled Browser:**
- Chrome browser that agents can control
- Two main capabilities:
  - Context retrieval with same authentication as user's Chrome
  - Agent control: clicking, scrolling, running JavaScript
- Can access Google Docs, GitHub dashboards, and other authenticated services
- Provides verifiable results through screen recordings

**Additional Features:**
- Inbox system for managing tasks requiring user attention (e.g., terminal commands)
- OS-level notifications for multi-threading across tasks

### 3. [Launch Challenges and Success](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=300s)
**Timestamps: 05:00 - 06:00**

- Strong user response created capacity constraints shortly after launch
- Humorous acknowledgment of "global chip shortage"
- Product launched in conjunction with Gemini 3 Pro
- Team excitement about getting product into users' hands

### 4. [Model Evolution and Product Paradigms](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=360s)
**Timestamps: 06:00 - 08:00**

**Evolution of AI coding assistance:**
- Autocomplete → Chat → Agents → [Next paradigm]
- Product capability is only as good as the underlying models

**Google's Advantage:**
- Team embedded in DeepMind with early access to Gemini models
- Access months before public release
- Collaborative relationship with research team
- Early exploration of model strengths, exploitable features, and gaps

### 5. [Four Categories of Model Improvements](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=420s)
**Timestamps: 07:00 - 08:00**

1. **Intelligence and Reasoning**: Better instruction following, tool use nuance, longer-running tasks
2. **Extended Time**: Tasks now take longer, can run in background
3. **Multimodal**: Off-the-charts multimodal functionality in Gemini 3
4. **Integration**: Combined with models like Nano Banana Pro for magical results

### 6. [Raising the Capability Ceiling](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=480s)
**Timestamps: 08:00 - 09:00**

- Goal: Aim higher with more ambitious agent capabilities
- Access to cutting-edge DeepMind research teams
- Three aspects of development:
  - What to build
  - How to build it
  - Actually building it
- Models now reasonably handle the "building it" part given proper context

### 7. [Browser Use - Context Retrieval](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=540s)
**Timestamps: 09:00 - 10:00**

- Software engineering extends beyond code
- Agent accesses institutional knowledge through browser:
  - Bug dashboards
  - Experiment results
  - Documentation
  - Design specifications
- Uses same authentication as user's normal Chrome
- Can access Google Docs, GitHub, and other authenticated services

### 8. [Browser Use - Verification and Testing](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=540s)
**Timestamps: 09:00 - 11:00**

**Agent Browser Capabilities:**
- Click, scroll, retrieve DOM, run JavaScript
- Blue border indicates when agent has control

**Demo: Flight Tracker App**
- Tested entirely by Gemini computer use variant
- Instead of just showing diffs, produces screen recordings
- Blue circle shows mouse movements
- Provides verifiable results of what agent actually did

**Visual Understanding:**
- Model can understand images and iterate based on visual feedback
- Can identify issues from screenshots and make corrections

### 9. [Multimodal Capabilities for Developers](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=600s)
**Timestamps: 10:00 - 12:00**

**Why Multimodal Matters:**
- Development is inherently multimodal:
  - Websites
  - Architecture diagrams
  - Not just text

**Two Key Capabilities:**
1. **Image Understanding**: Verifying screenshots and recordings
2. **Image Generation**: Using Nano Banana models

**Model Synergy:**
- Gemini 3 Pro + Nano Banana Pro work together
- Nano Banana Pro available day one in Anti-gravity editor
- Creates magical results through model integration

### 10. [Design Workflow with Mockups](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=660s)
**Timestamps: 11:00 - 12:00**

**New Design Process:**
- Prediction: Design processes will change with AI
- Can iterate in image space first before writing code
- Comment system similar to Google Docs/GitHub for mockups
- Agent updates designs based on batched comments
- Natural iteration cycle in visual domain before implementation

### 11. [New Interaction Pattern: Artifacts](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=720s)
**Timestamps: 12:00 - 14:00**

**Artifact Definition:**
- Dynamic representation of information the agent generates for user's use case

**Four Key Purposes:**
1. Keep agent organized
2. Enable agent self-reflection
3. Communicate with user
4. Work across agents

**Why Artifacts Matter:**
- Replaces scrolling through massive token streams
- Visual representation more comprehensible than text-based chain of thought
- Analogy: PowerPoint is the speaker's artifact - helps organize thoughts and communicate with audience

### 12. [Artifact Types and Dynamics](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=840s)
**Timestamps: 14:00 - 16:00**

**Dynamic Creation:**
- Model dynamically decides IF it needs an artifact and WHAT TYPE
- System is scalable - new artifact types can emerge naturally

**Common Artifact Types:**
1. **Markdown Plans**: Implementation plans with open questions and feedback sections
2. **Task Lists**: Monitor agent progress in real-time
3. **Architecture Diagrams**: Visual representations of system design
4. **Walkthroughs**: Proof of correct implementation (like PR descriptions)
5. **Images and Screen Recordings**: Visual artifacts
6. **Mermaid Diagrams**: Technical diagrams

**Auto-Continue Feature:**
- Model decides if it can proceed without user input
- Enables autonomous operation when appropriate

### 13. [Artifact Usage and Sharing](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=960s)
**Timestamps: 16:00 - 18:00**

**Purpose Communication:**
- Agent explicitly explains artifact purpose to users

**Sharing Controls:**
- Sub-agents
- Other agents
- Other conversations
- Memory bank

**Example Use Case:**
- API schema research stored in memory
- Reusable across future conversations
- Agent proactively notifies user when relevant

**Lifecycle Feedback:**
- Enables feedback throughout task execution
- Not just at completion
- Notification system for proactive agent communication

### 14. [Commenting System on Artifacts](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=1080s)
**Timestamps: 18:00 - 19:00**

**Inspired by Familiar Workflows:**
- Google Docs commenting
- GitHub review workflows

**Two Comment Types:**
1. **Text-based Comments**:
   - Highlight sections
   - Batch multiple comments
   - Send all at once

2. **Image-based Comments**:
   - Figma-style highlighting
   - For visual mockups

**Mid-execution Feedback:**
- Can provide input while agent is working
- Non-interrupting: Agent incorporates feedback into ongoing task
- Notifications when agent finishes processing comments

### 15. [Agent Manager Benefits](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=1140s)
**Timestamps: 19:00 - 21:00**

**Key Advantages:**
- Pulls developers to higher-level view above code
- Beautiful artifact review system
- Handles parallelism and orchestration

**Parallel Task Management:**
- Multiple projects simultaneously
- Multiple tasks in same project
- Examples:
  - Design mockup generation
  - API research
  - App building
  - All running in parallel

**Workflow:**
- Artifacts provide feedback mechanism
- Notifications indicate when attention needed
- Command+E to drop into editor for final 80-100% completion work

### 16. [The Research-Product Flywheel](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=1200s)
**Timestamps: 20:00 - 23:00**

**Secret: "Be Your Biggest User"**
- Anti-gravity used internally by Google engineers and DeepMind researchers
- Real-world usage reveals model gaps that evals cannot

**Example: Computer Use Team Collaboration**
- Identified gaps in model capabilities
- Identified gaps in agent harness
- Bidirectional improvement cycle

**Example: Artifacts Training**
- Required custom data distribution work
- Collaboration with research team
- Model needed to learn when and what type of artifacts to create

**Competitive Advantage:**
- Integration of product and research teams
- Internal usage drives continuous improvement
- Flywheel creates compounding benefits

### 17. [Three-Step Process for Building Anti-gravity](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=1380s)
**Timestamps: 23:00 - 24:00**

**The Formula:**
1. **Push the Ceiling**: Higher ambition, higher capability
2. **Agent-First Experience**: Artifacts and agent manager paradigm
3. **Research-Product Flywheel**: Internal usage drives improvement

### 18. [Closing and Vision](https://www.youtube.com/watch?v=HN-F-OQe6j0&t=1440s)
**Timestamps: 24:00 - 24:51**

- Gratitude to AI Engineer Summit organizers (Swix and Ben)
- Team excited to have product in the wild
- Welcoming user feedback
- Humorous note: "You too can adopt a TPU" to help with capacity issues
- Vision: Anti-gravity as the most advanced product on market because the team builds it for themselves

---

## Notable Technical Details

- **Speed**: Context switching between Agent Manager and Editor takes under 100ms
- **Models Used**:
  - Gemini 3 Pro (main reasoning model)
  - Nano Banana Pro (image generation)
  - Gemini computer use variants (browser control)
- **Architecture**: VS Code fork for editor component
- **Authentication**: Agent browser inherits user's Chrome authentication state
- **Capacity**: Initial launch overwhelmed by demand, leading to rate limiting

---

## Key Takeaways

1. **Agent-First Philosophy**: Anti-gravity fundamentally reimagines the IDE as an agent-centric rather than code-centric tool
2. **Artifacts as Communication Layer**: New interaction pattern for human-agent collaboration that goes beyond chat
3. **Multimodal Development**: Leverages image understanding and generation for design workflows
4. **Browser Integration**: Agents can access authenticated web services and test applications visually
5. **Research-Product Synergy**: Internal usage by Google engineers and DeepMind researchers creates a powerful feedback loop for improvement
6. **Higher-Level Abstraction**: The agent manager pulls developers away from line-by-line code review toward task and outcome management

Anti-gravity represents a fundamental paradigm shift in how developers interact with AI assistance, moving from augmentation tools to true collaboration with autonomous agents.
