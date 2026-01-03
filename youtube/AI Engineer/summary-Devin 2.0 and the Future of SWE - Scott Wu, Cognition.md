# Devin 2.0 and the Future of SWE - Scott Wu, Cognition

**Video URL:** https://www.youtube.com/watch?v=MI83buT_23o

---

## Executive Summary

Scott Wu, CEO of Cognition, presents the evolution of Devin, an AI coding agent, over the past 18 months. He introduces the concept of "Moore's Law for AI Agents" - the capacity of AI agents doubles every 70 days in coding tasks, translating to 16-64x improvement annually. The talk traces Devin's progression through distinct capability tiers: from repetitive migrations (2023), to isolated bug fixes (fall 2024), to broader multi-file changes (spring 2025), and finally to autonomous backlog processing (June 2025). Each tier required different technological breakthroughs including instruction following, repository setup, codebase intelligence, iterative workflows, confidence calibration, and autonomous testing capabilities.

---

## Topics

### [Introduction and Moore's Law for AI Agents](https://www.youtube.com/watch?v=MI83buT_23o&t=0s)
- Scott returns to AI Engineer conference one year later
- **Moore's Law for AI Agents**: Capacity measured by uninterrupted work duration
- General AI: doubling time every 7 months
- **Code-specific AI: doubling every 70 days (2-3 months)**
- This means **16-64x improvement per year** in coding capacity
- Evolution from GPT-3 (few words) to GPT-4 to current agents handling hours of human work
- Interface and capabilities requirements change every 2-3 months

### [Tier 1: Repetitive Migrations (End of 2023)](https://www.youtube.com/watch?v=MI83buT_23o&t=203s)
- First major use case: repetitive migrations
- Examples: JavaScript to TypeScript, Angular version upgrades, Java version migrations
- Tasks requiring file-by-file application of clear steps
- Not routine enough for deterministic programs, but follows clear patterns
- **Key capability solved: Instruction following**
- Built **Playbooks system** for step-by-step execution
- Also developed **knowledge/memory systems** for learning from feedback
- Aligned with what was most annoying for humans - boilerplate and repetitive work

### [Tier 2: Isolated Bugs and Features (Fall 2024)](https://www.youtube.com/watch?v=MI83buT_23o&t=378s)
- Evolution to "intern-level" tasks
- Example: "In this repo select dropdown, list currently selected ones at the top"
- Changes typically isolated to 1-2 files
- **Key capabilities built:**
  - Repository setup and snapshot systems
  - Clean remote VM for running CI and linters
  - Ability to rollback changes
- Broader value beyond migrations - Devon as a "junior buddy"

### [Tier 3: Broader Bugs and Multi-File Changes (Fall 2024)](https://www.youtube.com/watch?v=MI83buT_23o&t=496s)
- Tasks spanning multiple files (hundreds of lines)
- Requires diagnosis across files and cross-file consistency
- **Key technological breakthrough: Code as hierarchy, not just text**
  - Call hierarchies and language server integration
  - Git commit history analysis
  - Cross-file reference capabilities
- **Slack integration** became major workflow component
- Led to GA (General Availability) launch around this time

### [Tier 4: Complex Exploratory Tasks (Spring 2025)](https://www.youtube.com/watch?v=MI83buT_23o&t=642s)
- Tasks where humans don't know full requirements upfront
- Examples: "Improve architecture," "Profile slow function," "Handle error cases better"
- Two-line prompts no longer sufficient
- **New paradigm: Iterative workflow**
  - Released **Deep Wiki** - Devon's internal codebase representation made human-accessible
  - **Search capability** for asking questions about codebase
  - L2 experience: Explore codebase WITH agent, then set it to execute
- **Devon 2.0 and in-IDE experience launched**
  - 10-20% close monitoring, 80-90% autonomous work

### [Tier 5: Autonomous Backlog Processing (June 2025)](https://www.youtube.com/watch?v=MI83buT_23o&t=773s)
- "Kill your backlog" - handle multiple tasks simultaneously
- Integration with Linear, Jira, and other project management tools
- **Key requirements:**
  - **Confidence calibration**: Know when to ask for help vs. proceed
  - Understanding which repo/codebase section needs changes
  - Deciding when to seek human approval
- **Asynchronous testing became critical**
  - Agent must test itself iteratively
  - Needs to know what to test and what to look for
  - Higher context problem - must run code locally

### [Current State and Future (Now)](https://www.youtube.com/watch?v=MI83buT_23o&t=874s)
- Moving from single tasks to **entire projects**
- Each 2x improvement is qualitatively different, not just quantitative
- Evolution beyond pure text problem to complex integration:
  - Human collaboration (Linear, Slack)
  - Feedback incorporation and steering
  - Planning assistance
  - Autonomous testing and debugging
  - Long-term decision making
- **Prediction: Another 16-64x improvement expected in next 12 months**

### [Key Insights on Evolution](https://www.youtube.com/watch?v=MI83buT_23o&t=902s)
- Started from tab completion (pure text prediction on single file)
- Now requires:
  - Multi-system integration
  - Human-AI collaboration patterns
  - Advanced tooling (testing, debugging, shell commands)
  - Long-term autonomous decision making
- Every 2-3 month doubling brings different bottlenecks and requirements
- Interface and capability priorities completely shift at each tier

---

## Key Takeaways

1. **Exponential Growth**: AI coding agents are improving 16-64x per year, with capabilities doubling every 70 days
2. **Qualitative Changes**: Each improvement tier requires fundamentally different technologies and interfaces
3. **From Boilerplate to Projects**: 18-month journey from simple migrations to autonomous project completion
4. **Testing is Critical**: Asynchronous, autonomous testing capabilities essential for higher-tier performance
5. **Human-AI Workflow**: Evolution from simple prompts to iterative exploration and selective monitoring
6. **Next Frontier**: Moving beyond individual tasks to entire project orchestration