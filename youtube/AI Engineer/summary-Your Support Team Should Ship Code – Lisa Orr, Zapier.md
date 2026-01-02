# Your Support Team Should Ship Code – Lisa Orr, Zapier

**Video URL:** https://www.youtube.com/watch?v=RmJ4rTLV_x4

---

## Executive Summary

Lisa Orr from Zapier shares how they empowered their support team to ship code using AI-powered tools. Facing a backlog crisis from "app erosion" (8,000+ third-party API integrations constantly changing), Zapier ran two parallel experiments: (1) enabling support to fix bugs directly, and (2) building AI code generation tools. These experiments converged into "Scout Agent," an AI system that generates merge requests automatically. The result: support team velocity doubled from 1-2 to 3-4 tickets per week, with 40% of their app fixes now AI-generated. The talk emphasizes support's unique superpowers—closest to customer pain, real-time troubleshooting, and best validation—making them ideal candidates for AI-assisted code shipping.

---

## Main Topics

### [Introduction: Grand Canyon Analogy](https://www.youtube.com/watch?v=RmJ4rTLV_x4&t=23s)
- Lisa connects her 18-day Grand Canyon rafting trip to Zapier's challenges
- Both experience "erosion": natural vs. app erosion from 8,000+ integrations
- API changes and deprecations create constant reliability issues
- Support team flows through "Zapier Canyon" watching for app erosion

**Key Points:**
- Zapier has been around 14 years with constantly changing third-party APIs
- App erosion never stops, creating ongoing maintenance burden
- Backlog crisis: tickets coming in faster than they could handle

### [The Backlog Crisis & Two Experiments](https://www.youtube.com/watch?v=RmJ4rTLV_x4&t=127s)
- Integration reliability issues led to poor customer experience and churn
- **Experiment 1:** Move support from triaging to fixing bugs (started 2 years ago)
- **Experiment 2:** Can AI help solve app erosion faster?

**Key Points:**
- Needed buy-in to empower support team to ship code
- Support was eager—many wanted to transition to engineering
- Many support members were already unofficially helping maintain apps
- Started with guardrails: 4 target apps, engineering review, focus on app fixes

### [Experiment 2: Building Scout (AI Code Generation)](https://www.youtube.com/watch?v=RmJ4rTLV_x4&t=151s)
- Project named "Scout" (ties into Grand Canyon experience)
- Discovery phase: dog fooding, shadowing engineers and support, mapping pain points
- **Major discovery:** Huge time spent gathering context (API docs, logs, internet searches)

**Key Points:**
- Built multiple APIs to solve individual pain points
- Some use LLMs (diagnosis tool), some don't (test case finder uses search)
- Tools included: diagnosis, unit test generator, test case finder

### [First Phase Challenges: APIs Without Adoption](https://www.youtube.com/watch?v=RmJ4rTLV_x4&t=341s)
- APIs not embedded in engineers' process
- Created "autocode" playground but it was just another window to visit
- Team spread thin across too many APIs
- Cursor launched simultaneously, making some tools unnecessary

**Key Points:**
- **Major win:** Diagnosis API became a "support darling"
- Support embedded diagnosis into their Zapier workflow via Zap integration
- Key insight: **embedding tools is the key to usage**

### [MCP Revolution: Embedding Tools in Workflow](https://www.youtube.com/watch?v=RmJ4rTLV_x4&t=428s)
- Model Context Protocol (MCP) solved the embedding problem
- Engineers can now use Scout MCP tools directly in Cursor
- Builders leave IDE less, spend more time in one window

**Key Points:**
- Still faced challenges: diagnosis takes long to run (frustrating in IDE)
- Customization needs not met—engineers used Zapier MCP instead
- Scattered adoption: not every engineer used all tools
- Hypothesis: true value comes from tying tools together

### [Scout Agent: Orchestrating AI Tools](https://www.youtube.com/watch?v=RmJ4rTLV_x4&t=546s)
- Shifted from "suite of tools" to owned orchestration via Scout Agent
- Combines diagnosis → codegen → merge request generation
- Target customer: support team (handling emergent bugs fresh off the queue)
- **Two experiments merge:** AI tools + support shipping code = Scout Agent

**Key Points:**
- Support team identified as best beneficiary of orchestration
- They handle small bugs that are emergent and coming hot off the queue

### [Scout Agent Workflow](https://www.youtube.com/watch?v=RmJ4rTLV_x4&t=612s)
**Flow:**
1. Support submits issue to Scout Agent
2. Categorize the issue
3. Assess fixability
4. Generate merge request (if fixable)
5. Support reviews and tests
6. Request adjustments in GitLab if needed
7. Scout does another pass
8. Submit MR for engineering review

**Technical Implementation:**
- All kicked off by Zaps (heavy dog fooding)
- Runs diagnosis first, posts to Jira ticket
- Triggers GitLab CI/CD pipeline with 3 phases: plan, execute, validate
- Uses Scout MCP tools + Cursor SDK
- Latest: rapid iteration via chat in GitLab

### [Measuring Success: Evaluation & Impact](https://www.youtube.com/watch?v=RmJ4rTLV_x4&t=761s)
**Three evaluation questions:**
1. Is categorization right?
2. Was it actually fixable?
3. Was the code fix accurate?

**Results:**
- 75% accuracy for categorization and fixability
- More tickets → more test cases → continuous improvement

**Impact:**
- **40% of support team's app fixes now generated by Scout**
- **Velocity doubled:** from 1-2 tickets/week to 3-4 tickets/week
- Process improvement: Scout surfaces fixable tickets in triage flow
- Reduces friction of searching backlog

### [Why Support Teams Have Superpowers](https://www.youtube.com/watch?v=RmJ4rTLV_x4&t=854s)
**Three superpowers support has:**

1. **Closest to customer pain** → closest to context that matters for solving problems
2. **Troubleshooting in real time** → fresh context, logs not missing (vs. stale backlog tickets)
3. **Best at validation** → ensure solution fits actual customer need, not just technical fix

**Additional benefit:**
- Support team members from this experiment have transitioned to become engineers

### [Conclusion & Takeaways](https://www.youtube.com/watch?v=RmJ4rTLV_x4&t=902s)
- Engineering benefits too: "allows us to stay focused on more complex stuff"
- **Key message:** Powerful magic in empowering support with codegen
- Zapier is hiring
- Recommendation: raft the Grand Canyon with ORS (life-changing!)

---

**Last Updated:** 2026-01-01
