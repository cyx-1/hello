# Fuzzing in the GenAI Era — Leonard Tang, Haize Labs

**Video URL:** https://www.youtube.com/watch?v=OMGPvW8TBHc

---

## Executive Summary

Leonard Tang from Haize Labs presents their approach to validating and testing AI systems through "hazing" - advanced fuzzing techniques adapted for the GenAI era. The core problem addressed is AI's brittleness (Lipschitz discontinuity): similar inputs can produce wildly different outputs, making traditional eval methods insufficient. Haize Labs tackles this through two key innovations: (1) **Scaling judge-time compute** using agents-as-judges and RL-trained models to create robust evaluation systems, and (2) **Optimization-driven fuzzing** treating input generation as a discrete optimization problem. Their approach has helped major banks and voice agent companies discover critical vulnerabilities and scale their QA processes from months to minutes.

---

## Topics

### [Introduction and The Last Mile Problem](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=0s)
**Timestamp:** 00:00 - 02:00

- **The existential AI problem**: How to validate, verify, audit, and steer unstructured LLM outputs
- Haize Labs positions as QA/eval company rather than pure security, using fuzzing/property-based testing
- **The last mile problem**: Easy to build demo-ready AI apps, extremely hard to get them production-ready and enterprise-grade
- Despite 2+ years since ChatGPT launch, industry hasn't solved trust, reliability, and risk issues

**Key Points:**
- AI systems are extremely unreliable and need pressure testing before deployment
- Solution: Large-scale optimization, simulation, and search before deployment
- Easy to impress a PM over a weekend; hard to reach true enterprise robustness


### [Why Traditional Evals Fail](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=120s)
**Timestamp:** 02:00 - 04:00

- **Traditional eval approach**: Collect finite static golden dataset with expected outputs, compare actual vs expected
- This worked in deep learning era but fails for GenAI due to **brittleness** (Lipschitz discontinuity)
- **The core issue**: Ostensibly similar inputs with slight variance in syntax/semantics produce wildly different outputs
- Non-determinism isn't the main problem (set temperature to zero); brittleness is what makes building with GenAI difficult

**Key Points:**
- Real-world examples: Air Canada hallucinations, Character AI suicide incident, Chevy $1 truck exploit
- Standard evals have insufficient coverage - passing 100% of unit tests doesn't guarantee production readiness
- Need to densely cover the input space to discover edge cases


### [Two Problems with Standard Evals](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=270s)
**Timestamp:** 04:30 - 06:00

- **Problem 1: Coverage** - Static datasets only validate performance on those specific inputs; nearby variations might fail catastrophically
- **Problem 2: Quality measurement** - Difficult to measure output quality or similarity to ground truth
- Need human subject matter experts who can translate subjective criteria into quantitative metrics
- This is the core challenge in reward modeling (5-7+ years of research)

**Key Points:**
- Standard metrics (exact match, LLM-as-judge, semantic similarity) all have significant quirks
- The ideal would be constant human oversight with good taste translated to quantitative metrics
- Not trivial to solve - remains an open problem


### [Hazing: Fuzzing for AI](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=370s)
**Timestamp:** 06:10 - 07:00

- **Hazing approach**: Simulate large-scale stimuli, get responses, judge/analyze outputs, use signals to guide next search round
- Iterate until discovering bugs and corner cases, or exhaust search budget (indicating production readiness)
- Easy to describe, difficult to execute - both scoring outputs and generating input stimuli are technically challenging

**Key Points:**
- Hazing = property-based testing + fuzzing adapted for AI era
- Core loop: Generate inputs → Test application → Judge outputs → Use feedback for next iteration
- Two technical challenges: (1) How to judge outputs, (2) How to generate inputs


### [Scaling Judge-Time Compute](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=420s)
**Timestamp:** 07:00 - 09:00

- **LLM-as-judge problems**: Hallucinations, instability, uncalibrated outputs, position bias, extreme sensitivity to prompt changes
- Off-the-shelf LLM calls insufficient for reliability
- **Key question**: How to QA the judge itself?
- **Philosophy**: Apply inference-time scaling to the judging stage - "scaling judge-time compute"

**Key Points:**
- Two approaches: (1) Train reasoning models from scratch, (2) Build structured agent-as-judge systems
- Need gold-standard metrics to iterate on the underlying AI application
- Judge reliability is critical for the entire hazing pipeline


### [Verdict: Agents as Judges](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=540s)
**Timestamp:** 09:00 - 11:00

- **Verdict library**: Implements scalable oversight primitives from AI safety research
- **Scalable oversight**: How weaker models audit and steer stronger models (originally for superhuman AI control)
- **Key primitives**: LLM debate, self-verification, ensembling
- Example: Weaker LLMs debate about stronger model outputs, self-verify their reasoning

**Key Points:**
- Verdict powered by GPT-4o-mini backbone beats O1/O3-mini at 1/3 cost and 1/3 latency
- Self-verified debate ensemble architecture carefully designed with intelligent priors
- Achieves superior accuracy on expert QA verification tasks
- Demonstrates that structured agents with compute scaling can beat larger models


### [RL-Trained Judges](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=660s)
**Timestamp:** 11:00 - 14:00

- **Alternative approach**: Train models from scratch via RL for judging tasks
- Solves two problems: (1) Lack of coherent rationale, (2) Generic criteria vs task-specific needs
- **SPCT (Self-Principled Critique Tuning)** from DeepSeek: Propose instance-specific criteria, then critique against each
- GRPO tuning on 600M and 1.7B parameter models achieves competitive performance with Claude 3 Opus and GPT-4 mini

**Key Points:**
- J1 micro (1.7B params): 80.7% accuracy on RewardBench, matching Claude 3 Opus at 80%
- Instance-specific rubrics like unit tests for each data point
- Judge-time scaling via RL gets better performance from smaller models with more compute
- More fun approach in Leonard's opinion compared to agent-based methods


### [Input Generation: Fuzzing as Optimization](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=840s)
**Timestamp:** 14:00 - 16:00

- **Two fuzzing modes**: (1) General fuzzing - reasonable in-distribution user inputs, (2) Adversarial testing - emulate prompt injection/jailbreaking
- **Key insight**: AI fuzzing is more structured and optimization-driven than classical security fuzzing
- Impossible to brute-force search natural language space (128K tokens per input × millions = infeasible)
- **Formulation**: Discrete optimization problem over natural language search space

**Key Points:**
- Objective: Minimize judge score to find inputs that break the application
- Leverage 60-70 years of discrete math optimization research
- Techniques: Gradient-based methods (backprop through model to input), tree search/MCTS, embedding space search, DSPI
- Must be clever, guided, and prune search space effectively


### [Case Study: Hungarian Bank](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=960s)
**Timestamp:** 16:00 - 17:05

- **Client**: Largest bank in Hungary with loan calculation AI application
- **Requirements**: Follow 18-line code of conduct for customer-facing application
- **Results**: Discovered numerous prompt injections, jailbreaks, and unexpected corner cases not covered in code of conduct
- Successfully patched vulnerabilities and unblocked production deployment

**Key Points:**
- Threw "everything under the sun" from optimization and scoring platform
- Emulated adversaries to discover security vulnerabilities
- Enabled production release for regulated financial services


### [Case Study: Fortune 500 Bank Voice Agents](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=1025s)
**Timestamp:** 17:05 - 17:47

- **Client**: Fortune 500 bank deploying voice agents for outbound debt collection
- **Complexity**: Testing beyond text space - introducing variance in audio signals
- **Audio variations**: Background noise, static, frequency changes
- **Results**: What took internal ops team 3 months took Haize platform 5 minutes

**Key Points:**
- Still an optimization problem despite audio complexity
- Demonstrates scalability of adversary emulation approach
- Massive time savings: 3 months → 5 minutes


### [Case Study: Voice Agent Company Eval Suite](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=1067s)
**Timestamp:** 17:47 - 18:25

- **Client**: Voice agent company scaling eval suite
- **Focus**: Scaling up subjective human annotators through Verdict
- **Results**: 38% increase in ground truth human agreement vs internal ops teams
- **Architecture**: Rubric fanout - propose individual unit test criteria, critique, self-verify, aggregate

**Key Points:**
- Not adversarial hazing but eval scaling
- Tried-and-true Verdict architecture
- Significant improvement in matching human judgment quality


### [Closing Thoughts and Hiring](https://www.youtube.com/watch?v=OMGPvW8TBHc&t=1107s)
**Timestamp:** 18:25 - 19:06

- Hazing is critical for the new era of software being built
- **Team**: Only 4 people facing "insurmountable enterprise demand"
- Aggressively hiring, based in New York
- Supports single-turn, multi-turn, and persistent conversations across modalities

**Key Points:**
- Small team with massive demand signals market validation
- Open to hiring for expansion
- Platform handles diverse input types (text, voice, multi-turn conversations)

---

## Key Takeaways

1. **AI brittleness is the real problem**, not non-determinism - similar inputs yield wildly different outputs
2. **Traditional evals are insufficient** due to coverage gaps and difficulty measuring output quality
3. **Scaling judge-time compute** creates reliable evaluation through agents-as-judges and RL-trained models
4. **Fuzzing AI systems** requires optimization-driven approaches, not brute force
5. **Real-world impact**: 3-month QA processes reduced to 5 minutes, enabling production releases for regulated industries
6. **Haize Labs' approach**: Combining scalable oversight primitives, discrete optimization, and domain-specific RL training

---

**Last Updated:** January 1, 2026
