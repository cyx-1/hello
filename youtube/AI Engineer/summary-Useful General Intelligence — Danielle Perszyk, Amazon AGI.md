# Useful General Intelligence — Danielle Perszyk, Amazon AGI

**Video URL:** https://www.youtube.com/watch?v=Dj0b_cEBHBI

---

## Executive Summary

Danielle Perszyk, a cognitive scientist at Amazon's AGI SF lab, presents a provocative vision for building AI agents that augment human intelligence rather than replace it. She challenges the conventional "AGI as smarter machines" narrative by arguing that general intelligence is inherently social and distributed, not something that exists within individual minds or models. Drawing from evolutionary neuroscience, she explains how humans co-evolved with cognitive technologies (language, writing, computers) to become smarter collectively. Nova Act, Amazon's agent framework, represents the first step in this vision—a research preview that makes browser automation accessible through simple API calls. The talk emphasizes that achieving reliable, aligned agents requires grounding them in shared environments (UIs), enabling human-agent interaction loops, and ultimately building agents with models of human minds.

---

## Key Topics

### [Introduction: The Hallucinating Brain](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=16s)
**[00:16 - 02:00]**

- Introduces the concept that all human perception is "controlled hallucination"—our brains make predictions and reconcile them with sensory input
- Draws parallel to LLM hallucinations: hallucinations are features, not bugs, enabling flexibility to go beyond training data
- Current chatbots can brainstorm and generate content but can't yet "think, learn, or act in a reliable general purpose way"
- Challenges the standard AGI vision focused solely on making AI smarter

**Key Quote:** "We're all hallucinating right now. Our brains don't have direct access to reality... perception is controlled hallucination."

---

### [Two Historical Visions for Intelligence](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=238s)
**[03:58 - 06:00]**

- **1956 Dartmouth Conference:** Engineers aimed to build "thinking machines" to solve intelligence (led to AI field founding)
- **Douglas Engelbart's Alternative:** Focused on augmenting human intelligence rather than replicating it—invented computer mouse and GUI
- Introduces "technosocial co-evolution": humans invent technologies that reshape our cognition
- Presents the crossroads: build AI as smart as us, or build AI that makes us smarter

**Key Insight:** Engelbart's vision proved correct—computers did make us smarter by enabling us to offload computation and distribute cognition across digital environments

---

### [Automation vs. Augmentation](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=360s)
**[06:00 - 07:00]**

- Automation isn't inherently augmentation—sometimes it reduces agency (e.g., scrolling addiction, echo chambers, autocomplete shutting down thinking)
- Things become useful by either simplifying our lives (offloading) or giving us leverage
- With precise control and active tailoring, automation can increase our agency
- The talk's central proposition: build AI that "unhobles humans" rather than just "unhobbling AI"

**Critical Distinction:** Making AI smarter doesn't guarantee it will be useful to us—we need to optimize for human augmentation

---

### [Nova Act: Meeting Models and Builders Where They Are](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=428s)
**[07:08 - 08:00]**

- Amazon AGI's vision: the atomic unit of digital interactions will be agent calls
- Current problem: most websites lack APIs, built for visual UIs instead
- Solution: train foundation models to interact with UIs like humans do
- Nova Act combines a specialized Amazon Nova model with an SDK for building/deploying agents

---

### [Nova Act Demo and Technical Overview](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=484s)
**[08:04 - 10:06]**

- Demo: apartment hunting in Redwood City—agent searches listings, extracts structured data (Pydantic schemas), uses Google Maps to calculate biking distances to CalTrain in parallel
- Technical approach: just 3 lines of code to get started
- Model improvements ship every few weeks
- Example code available in GitHub repo samples folder

**Developer Experience:** Focus on making agent development frictionless with simple APIs while continuously improving underlying models

---

### [The Challenge of Computer Use](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=606s)
**[10:06 - 11:00]**

- Even basic computer use is "deceptively challenging"—interpreting unlabeled icons, understanding UI conventions
- Can't teach agents every possible icon or interaction pattern
- Solution: reinforcement learning (RL) allows agents to explore and discover novel computer use methods
- Agents may eventually use computers differently than humans (complementary, not identical)

**Implication:** If agents diverge in computer use methods, their perception of the digital world must remain aligned with ours

---

### [Current Agent Limitations](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=676s)
**[11:16 - 12:00]**

- Most current agents are "LLM wrappers" functioning as read-only assistants
- They can use tools and some excel at code, but lack environmental grounding
- They lack world models
- Computer use agents are different: they see pixels and interact with UIs (early form of embodiment)

**Nova Act's Differentiator:** Focusing on making smallest units of interaction reliable with granular control—atomic actions can compose into infinitely complex workflows

---

### [What Makes Human Intelligence General?](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=739s)
**[12:19 - 14:00]**

- Computer use (shared environment) is necessary but not sufficient for aligned general-purpose agents
- Scientists learned over decades: general intelligence didn't start with computers
- The real story began 6 million years ago when our ancestors faced environment changes
- Feedback loop: bigger brains → social connections → fine-tuning to social information → even bigger brains
- The other half of the story: offloading computation to each other's minds, distributing cognition across social environments

**Core Concept:** "Technosocial co-evolution"—we invent technologies that shape us, which drives further invention

---

### [Representational Alignment Through Evolution](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=840s)
**[14:00 - 15:00]**

- Through evolutionary flywheels, humans developed "representational alignment"—reproducing mental contents to cooperate
- Intelligence upgrading didn't start with computers but with using each other's minds as tools
- **Fundamental insight:** What makes human intelligence general is inferring the existence of other minds

**Controversial Claim:** A standalone AI model, no matter how advanced, cannot be general intelligence—intelligence emerges through interactions

---

### [Measuring What Matters](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=900s)
**[15:00 - 15:30]**

- Intelligence is social, distributed, ever-evolving
- Can't just measure model capabilities or "time spent on platform"
- Must measure human outcomes: creativity, productivity, strategic thinking, states of flow
- Need to optimize for interactions, not just agent performance

**Paradigm Shift:** Success metrics must center on human augmentation, not agent benchmarks

---

### [Language: The Original Cognitive Technology](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=936s)
**[15:36 - 17:00]**

- Language co-evolved with models of minds in another flywheel integrating communication and representation
- Language was both cause and effect of mind modeling
- **Big bang moment:** Models of mind became the original placeholder concept—the first variable for representing any concept (true generalization)
- Distinction from other systems:
  - Other animal communication lacks models of mind
  - Programming languages don't negotiate meaning in real-time (hence easily verifiable)
  - LLMs don't understand that words refer to things minds make up

**Profound Insight:** "What's in a word? Quite literally a mind."

---

### [Cognitive Technologies as Flywheels](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=1019s)
**[17:00 - 18:00]**

- Language triggered series of "cognitive technologies" (writing, mathematics, computers)
- Each foundation for the next, enabling increasingly abstract thoughts
- They evolve within communities to become useful
- Early computers weren't useful until Engelbart improved interfaces
- Now computers get in our way with distractions despite unprecedented information access
- Agents can fix this: do repetitive tasks, learn from us, redistribute skills, teach new knowledge

**Vision:** Agents as our "collective subconscious"—but only if built to reflect larger co-evolutionary patterns

---

### [How Cognitive Technologies Control Hallucinations](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=1080s)
**[18:00 - 18:30]**

- Cognitive technologies stabilize thinking, reorganize brains, control hallucinations
- They direct attention to same environmental features, filter signals from noise
- Result: co-created shared world models

**Connection to Nova Act:** Building primitives for a cognitive technology that aligns agent and human representations

---

### [The Path to Reliable Agents](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=1110s)
**[18:30 - 19:40]**

- Reliability isn't just about clicking the same place—it's understanding larger goals
- Agents will eventually need models of our minds (we don't build these directly—we set preconditions for emergence)
- Requirements:
  1. Common language for humans and computers
  2. Model of shared environment
  3. Intuitive interaction interfaces
- These enable reciprocal intelligence leveling between humans and agents

**Flywheel for Useful General Intelligence:**
- Need human-agent interaction data to advance models
- Need useful products to motivate usage
- More useful products → smarter humans → better data → better models → more useful products

---

### [Conclusion and Call to Action](https://www.youtube.com/watch?v=Dj0b_cEBHBI&t=1182s)
**[19:42 - 19:46]**

- Invitation to learn more at the upcoming Nova Act workshop
- Emphasis on builder community's central role in co-evolving these technologies

---

## Key Takeaways

1. **Reframe AGI:** General intelligence is not a property of individual models but emerges through social interactions and shared environments

2. **Augmentation over Replacement:** The goal is AI that makes humans smarter and increases human agency, not AI that replaces human intelligence

3. **Evolutionary Lens:** Understanding how humans co-evolved with cognitive technologies (language, writing, computers) provides a blueprint for agent development

4. **Nova Act's Approach:** Focus on reliable atomic interactions with granular control, grounded in shared UI environments

5. **Models of Minds:** Eventually, agents will need to model human minds—but this emerges through human-agent interaction loops, not direct programming

6. **Measure Human Outcomes:** Success metrics should focus on human creativity, productivity, and flow states—not just agent benchmarks

7. **Community-Driven Evolution:** Like all cognitive technologies, agents must evolve within diverse builder communities to become truly useful

---

## Technical Notes

- Nova Act uses a specialized version of Amazon Nova foundation model trained for high reliability on UI tasks
- SDK allows simple agent calls that translate natural language to screen actions
- Supports Python integrations with parallel browser execution
- Model improvements ship every few weeks
- Code samples available in GitHub repo

---

## Philosophical Implications

This talk challenges Silicon Valley's dominant AGI narrative by grounding it in evolutionary neuroscience and cognitive science. The provocative claim that "intelligence cannot exist in individual models" contradicts the industry's focus on scaling individual models to superintelligence. Instead, Perszyk argues for a fundamentally relational view of intelligence that has profound implications for how we build, evaluate, and deploy AI systems. If she's right, the path to AGI isn't through bigger models but through better human-agent interaction loops that mirror the social-cognitive flywheels that made humans intelligent in the first place.
