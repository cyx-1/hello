# Agents are Robots Too: What Self-Driving Taught Me About Building Agents — Jesse Hu, Abundant

**Video URL:** https://www.youtube.com/watch?v=qqXdLf3wy1E

---

## Executive Summary

Jesse Hu, an ML engineer with experience at YouTube, Google, and Waymo, shares critical insights from robotics and self-driving cars that apply to building AI agents. The talk emphasizes that successful agent development requires much more than just good models—99% of the work lies in infrastructure, tooling, and understanding the complexities of actions in the real world. Key themes include the importance of closed-loop feedback systems, the challenges of moving from predictive to action models, the necessity of simulation and evaluation frameworks, and the iterative hill-climbing process required for improvement. The parallels between physical robotics and digital agents reveal that we're still in the early stages, similar to where self-driving was years ago.

---

## Topics & Key Points

### 1. [Introduction & Background](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=0s)
**Timestamp:** 00:00 - 01:00

- Jesse Hu's background in ML engineering at YouTube, Google, and Waymo
- Work on two-tower embedding models, BERT, mixture of experts
- Focus on data, reward modeling, and evaluation in robotics
- Currently working at Abundant on datasets for foundation model labs and agentic coding models
- Talk focuses on general principles from self-driving applicable to digital agents

### 2. [The 1% vs 99% Problem](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=60s)
**Timestamp:** 01:00 - 03:00

- **Key insight**: The model is only 1% of the work; 99% goes into everything else
- **In robotics**: Hardware, sensors, actuators, integration, deployment, offline stack (simulation, training)
- **In agents**: Similar infrastructure needs exist
  - Body/embodiment: APIs, MCPs, terminal, browser, VM, persistent file systems
  - Offline stack: Continuous retraining, monitoring, human feedback loops, development tooling
- **Critical lesson**: The winning team has the best offline stack, not just the best model
- Better tooling enables developers to ship faster and more reliably

### 3. [Open Loop vs Closed Loop Systems](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=190s)
**Timestamp:** 03:10 - 04:06

- **Open loop**: Taking actions without feedback on their actual effects
- **Closed loop**: Measuring actual outcomes to recalibrate and correct
- **Robotics example**: Turning the steering wheel and measuring actual car rotation
- **Agent example**: Running bash commands without observing real-time outputs
- **Problem**: Many agent operations are currently open-loop when they should be closed-loop
- Need to measure whether commands complete, enable early exits, handle long-running processes

### 4. [Time Discretization & Sampling Rates](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=246s)
**Timestamp:** 04:06 - 05:00

- **Explicit design choice in robotics**: How to discretize input and action spaces
- Input modalities: Vision, LIDAR, radar combined in different ways
- Sampling frequencies: Every second, on-push, or 50Hz (50 times per second)
- High-frequency sampling enables quick replanning and real-time reactions
- **In agents**: Discretization happens implicitly through conversational turns
- Pros: Easy to reason about conversations, simple input/output per turn
- Cons: Can't respond in real-time to pop-ups, can't interact with long-running processes
- Current agent paradigm lacks the continuous sampling approach natural in robotics

### 5. [Input & Action Space Design](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=300s)
**Timestamp:** 05:00 - 07:31

- **Multiple input modalities available**: Tool streams, user streams, and more
- **Terminus agent example**: Uses TTY stream for character-by-character input/output
  - Enables control-C, window commands, and fine-grained control
- **Action space variations in robotics**:
  - XY planning (coarse vs continuous)
  - 2D vs 3D space
  - Acceleration vs position vs velocity
- **In agents**: Beyond MCPs and tool calls
  - Character-level interaction (Terminus)
  - Screen-level interaction at 20 FPS with mouse/keyboard (Dreamer paper)
- **Key question**: What trade-offs are we making with implicit/explicit design decisions?

### 6. [Stateless to Stateful Transitions](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=451s)
**Timestamp:** 07:31 - 08:43

- **Video game analogy**: Spawn from nothing, no concern for before/after session
- **Real world**: Cars have mass, occupy space, have persistent state and momentum
- **Agent evolution**: Moving from stateless sessions to stateful VMs
- Stateful considerations:
  - Persistent file storage
  - Running processes
  - Slack messages and communication state
  - Overall world state
- **Impact on development**: Affects both online execution and offline evaluation/simulation
- One of the most interesting developments in current agent space

### 7. [Imitation Learning vs RL: The Dagger Problem](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=523s)
**Timestamp:** 08:43 - 09:35

- **Training options**: Imitation learning (similar to SFT from human demos) vs RL (simulation or other)
- **Known issue with imitation**: Getting out of distribution leads to cascading failures
- **Browser agent example**: Pop-ups that never appeared in training data cause confusion
  - Humans naturally handle pop-ups, but agents trained on human demos never see them appear
- **Out-of-distribution problem**: Once slightly off-policy from human examples, agents become very confused
- Well-studied problem in robotics now appearing in agent development

### 8. [Actions Have Consequences](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=575s)
**Timestamp:** 09:35 - 10:03

- **Paradigm shift**: Not dealing with classification or prediction models anymore
- **New paradigm**: Predict → Act → Deal with consequences → Re-evaluate
- Actions affect the world state in complex, messy ways
- **Challenge**: Managing cascading effects of actions in the real world
- This is fundamentally tougher than pure prediction tasks

### 9. [Simulation & Counterfactuals](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=603s)
**Timestamp:** 10:03 - 10:29

- **Purpose of simulation**: Represent real-world complexity and messiness
- **Starting state**: Capture all complexities of the real world
- **Playing out scenarios**: Not just single paths, but all possible paths
- **Counterfactuals**: Exploring what could happen as the agent changes
- Essential for handling the complexity of real-world consequences

### 10. [MDP Framework (Markov Decision Process)](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=629s)
**Timestamp:** 10:29 - 11:02

- **MDP components**: Agent considers state and reward, takes actions on environment/world
- **Formalism**: Conceptual framework for understanding agent loops
- **Useful primitives**: Helps describe and communicate what's happening
- Classic reinforcement learning and robotics concept

### 11. [From Chat Models to Action Models](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=662s)
**Timestamp:** 11:02 - 12:22

- **Self-driving parallel (2017-2020)**: Focus on perception models, assuming boxes solve driving
  - Hidden complexity in action models vs predictive models
- **Current language models**: Can understand text-based world, generate sophisticated reasoning
- **The gap**: Plans look good but implementation in real world fails
  - Tool calls fail
  - Agents fail to progress
  - Agents can't self-correct from mistakes
- **Deceptively tricky**: Transition from prediction to action is where most work remains
- This is where bulk of past work has been and where future work will continue

### 12. [Why Code & Self-Driving Are Lucky](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=742s)
**Timestamp:** 12:22 - 13:44

- **Self-driving success**: Working in production today (limited cases) vs general robotics (still demos)
- **Key advantage**: Pre-defined machine with human controls
  - Well-refined over decades
  - Electronic controls with built-in telemetry
  - Pre-defined interface for actions and data collection
- **Makes it easier**: Convenient for code operation and machine learning
- **Contrast with general robotics**: Desktop work is less codified and harder
- **Lesson for new domains**: Look for areas with pre-defined human interfaces

### 13. [Hill Climbing & Iterative Development](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=824s)
**Timestamp:** 13:44 - 15:00

- **Traditional development**: Implement feature → guaranteed to reach production
- **Agent development**: Nebulous metrics requiring guess-and-check
- **Process**: Benchmark → Hypothesis → Experiment → Hope for improvement
- Not always forward progress, sometimes metrics go down
- **Self-driving approach (more sophisticated)**:
  1. Learning
  2. Simulation (deploy with confidence, improve learning)
  3. Deployment
  4. Logs from real world feed back to simulation
- **Importance of logs**: Ground simulation in reality, create full feedback loop
- Logs become more important than current practice

### 14. [Getting More from Logs & Metrics](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=900s)
**Timestamp:** 15:00 - 15:27

- **Beyond aggregate numbers**: 70% on benchmark tells you little
- **Break down by**:
  - Different categories
  - Different cities/contexts
  - Different failure modes
- **Triage individual failures**: Get specific insights on where and how to improve
- **Tooling & processes**: Developed to help customers with hill climbing
- Much richer insights than single metrics

### 15. [Current State: We're Only Partway There](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=927s)
**Timestamp:** 15:27 - 15:53

- **Comparison to early self-driving**: Great demos and predictive models
- **Not yet at**: End-to-end work completion
- **Reasons**: Actions having consequences, real-world complexity
- Similar stage to where robotics was years ago

### 16. [Recap & The Birth of "Agentics"](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=933s)
**Timestamp:** 15:53 - 17:34

- **Key parallels covered**:
  - Closed-loop systems and feedback
  - System discretization
  - Action and input space design
  - Stateless to stateful transitions
  - Predictive to action models
  - Simulation in deployment and training
  - Infrastructure importance to development
- **Coining "Agentics"**: Making agent development as legitimate as robotics
  - Moving from hacking to dedicated science
  - Establishing real practices and principles
- **Recommended reading**:
  - Open-loop and closed-loop control
  - MDPs (fully vs partially observable environments)
  - Dagger (Dataset Aggregation)
  - Offline RL
  - Introduction to Reinforcement Learning book
  - Recent robotics literature (fields are converging)
- **Final message**: Agents are robots too—they act in the real world, make mistakes, must recover
- All the little details really matter

### 17. [Q&A & Contact](https://www.youtube.com/watch?v=qqXdLf3wy1E&t=1054s)
**Timestamp:** 17:34 - 17:36

- Contact: jesse@abund.ai
- Open to thoughts and feedback

---

## Key Takeaways

1. **Model ≠ Product**: The foundation model is only 1% of building production agents; 99% is infrastructure, tooling, and systems
2. **Close the Loop**: Move from open-loop to closed-loop systems with real-time feedback and error correction
3. **Design Matters**: Explicit choices about time discretization, input/output modalities, and action spaces have major implications
4. **State is Complex**: Transitioning from stateless to stateful agents introduces real-world complexity in evaluation and deployment
5. **Actions ≠ Predictions**: Building action models is fundamentally harder than predictive models due to cascading consequences
6. **Simulate Everything**: Robust simulation frameworks are essential for training, evaluation, and building confidence before deployment
7. **Logs are Gold**: Detailed logging and failure analysis provide far more insight than aggregate metrics
8. **We're Early**: Current agent capabilities are comparable to early self-driving—great demos but far from end-to-end reliability
9. **Learn from Robotics**: Decades of robotics research provides proven frameworks (MDPs, dagger, offline RL) directly applicable to agents
10. **Infrastructure Wins**: The best offline stack (tooling, simulation, evaluation) matters more than marginal model improvements

---

**Last Updated:** 2026-01-01
