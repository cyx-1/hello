# Latent Space Paper Club: AI Engineer World's Fair Special Edition Summary
## DeepSeek R1/V3 & Test of Time Paper Club Launch

**Video URL:** https://www.youtube.com/watch?v=9k3xPh-40mo

---

## Executive Summary

This special edition of the Latent Space Paper Club, presented at AI Engineer World's Fair, covers two major announcements: the launch of a new "Test of Time" Paper Club and a comprehensive deep dive into DeepSeek's R1 and V3 models, including the latest May 28th update.

The session celebrates over a year of consistent weekly paper club meetings, attracting an average of 100 attendees (300 for the DeepSeek V3 session). The presentation reveals how DeepSeek achieved O3-level reasoning performance through pure reinforcement learning (RL), scaled inference-time compute, and innovative distillation techniques - all while remaining fully open source.

The new Test of Time Paper Club will run for 6 months (July-December), covering 50-100 foundational AI papers across topics like deep learning foundations, LLM architecture, scaling laws, optimization, and more. It will feature both in-person SF sessions and remote participation.

---

## Key Announcements

### Test of Time Paper Club Launch
**[Timestamp: 01:20](https://www.youtube.com/watch?v=9k3xPh-40mo&t=80s)**

- **Launch Timeline**: Starting June/July 2025, running through December (6 months)
- **Format**:
  - Weekly sessions covering 2-4 foundational papers per week
  - In-person sessions in San Francisco + Remote sessions via Zoom
  - Curriculum-based approach covering ~50-100 essential AI papers
  - Presentation + Discussion format (not a hands-on course)

**Topics to be Covered:**
- **[02:00](https://www.youtube.com/watch?v=9k3xPh-40mo&t=120s)** Foundations of Deep Learning: attention mechanisms, optimizers (Adam, gradient descent), ReLU, basic RL
- **[04:06](https://www.youtube.com/watch?v=9k3xPh-40mo&t=246s)** LLM Foundations: RNNs, LSTMs, bidirectional RNNs, BERT, GPT-2
- **[04:39](https://www.youtube.com/watch?v=9k3xPh-40mo&t=279s)** Generative LLMs: Llama 3, DeepSeek core models
- **[04:50](https://www.youtube.com/watch?v=9k3xPh-40mo&t=290s)** Pre-training & Post-training: Scaling laws (Chinchilla), distillation, overtraining
- **[05:30](https://www.youtube.com/watch?v=9k3xPh-40mo&t=330s)** Generative Models: CLIP, Sora, Segment Anything, Stable Diffusion
- **[05:37](https://www.youtube.com/watch?v=9k3xPh-40mo&t=337s)** Fine-tuning: LoRA, QLoRA, DPO, RL, GRPO
- **[05:44](https://www.youtube.com/watch?v=9k3xPh-40mo&t=344s)** Optimization & Voice: Speculative decoding, Flash Attention, Whisper
- **[05:48](https://www.youtube.com/watch?v=9k3xPh-40mo&t=348s)** Evaluation Tracks

---

## DeepSeek May 28th Update (Latest Release)

### DeepSeek R1 May 28th - Major Performance Leap
**[Timestamp: 08:58](https://www.youtube.com/watch?v=9k3xPh-40mo&t=538s)**

**Key Improvements:**
- **[10:05](https://www.youtube.com/watch?v=9k3xPh-40mo&t=605s)** AIME 2024 score jumped from 70% → 87.5% (17.5% improvement)
- **[10:32](https://www.youtube.com/watch?v=9k3xPh-40mo&t=632s)** Now matches O3 and Gemini 2.5 Pro performance levels
- **[11:00](https://www.youtube.com/watch?v=9k3xPh-40mo&t=660s)** Average reasoning tokens doubled: 12,000 → 25,000 tokens
- **[11:57](https://www.youtube.com/watch?v=9k3xPh-40mo&t=717s)** Better at JSON output, function calling, and reasoning
- **[12:39](https://www.youtube.com/watch?v=9k3xPh-40mo&t=759s)** Humanity's Last Exam performance dramatically improved

**How They Did It:**
- **[09:53](https://www.youtube.com/watch?v=9k3xPh-40mo&t=593s)** More post-training on DeepSeek V3 base model
- **[11:08](https://www.youtube.com/watch?v=9k3xPh-40mo&t=668s)** Extended RL training to enable longer reasoning chains
- **[11:34](https://www.youtube.com/watch?v=9k3xPh-40mo&t=694s)** Models now trained to reason for twice as long

### New Distillation Model: DeepSeek R1 Qwen2.5 8B
**[Timestamp: 12:42](https://www.youtube.com/watch?v=9k3xPh-40mo&t=762s)**

**Breakthrough Achievement:**
- **[13:10](https://www.youtube.com/watch?v=9k3xPh-40mo&t=790s)** Took Qwen 2.5 8B and distilled from new R1 model
- **[13:26](https://www.youtube.com/watch?v=9k3xPh-40mo&t=806s)** 10% performance boost over previous 8B distillation
- **[13:53](https://www.youtube.com/watch?v=9k3xPh-40mo&t=833s)** **8B dense model matches Qwen3 235B (20B active) thinking model**
- **[14:47](https://www.youtube.com/watch?v=9k3xPh-40mo&t=887s)** Chain of thought improvements distill down remarkably well
- **[15:51](https://www.youtube.com/watch?v=9k3xPh-40mo&t=951s)** Shows reasoning distillation is incredibly efficient for small models

---

## Original DeepSeek V3 & R1 Deep Dive

### What is Test-Time Compute Scaling?
**[Timestamp: 18:22](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1102s)**

**The Scaling Problem:**
- **[18:28](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1108s)** Models were overtrained (Chinchilla optimal → inference optimal)
- **[19:07](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1147s)** Llama evolved: 1B tokens → 1T tokens → 15T tokens → 45T tokens
- **[19:56](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1196s)** Training compute hitting limits - can't keep 10x-ing token counts
- **[20:25](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1225s)** Hundreds of millions of dollars per training run - not sustainable

**The Solution:**
- **[20:43](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1243s)** Unlock new scaling dimension: reasoning/test-time training
- **[21:07](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1267s)** Pure RL approach for reasoning capabilities without supervised data
- **[21:24](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1284s)** Goal: self-evolution through pure RL process
- **[27:15](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1635s)** Increase chain of thought, allow models to spend more time thinking

### DeepSeek V3 Architecture
**[Timestamp: 28:59](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1739s)**

**Model Specs:**
- **[29:07](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1747s)** 671B parameters total, 37B active (MoE architecture)
- **[29:31](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1771s)** Trained for ~$5 million (remarkably cost-effective)
- **[30:20](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1820s)** 15 trillion tokens of training data
- **[30:25](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1825s)** Multi-headed latent attention mechanism
- **[30:35](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1835s)** Multi-token prediction for sample efficiency
- **[30:50](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1850s)** Long context extension: trained at 32K, extended to 128K

**Chinese Labs' Advantage:**
- **[29:39](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1779s)** GPU trade restrictions forced innovation and efficiency
- **[29:50](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1790s)** Had to get creative with limited resources
- **[30:09](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1809s)** Couldn't scale training runs like US labs, so focused on RL instead

### DeepSeek R1-Zero: Pure RL Experiment
**[Timestamp: 31:20](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1880s)**

**What is R1-Zero:**
- **[31:24](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1884s)** Take pure base model (no SFT) → Apply pure RL
- **[31:42](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1902s)** Base models just predict next token (completion, not chat)
- **[31:59](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1919s)** Uses GRPO (Group Relative Policy Optimization) for RL
- **[32:07](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1927s)** Rewards based on accuracy AND format
- **[32:24](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1944s)** Responses must be verifiably correct (math answers, code compilation)

**Training Process:**
- **[32:38](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1958s)** RL on math and code with verifiable outputs
- **[32:53](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1973s)** Thinking formatted between <think> tags
- **[33:05](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1985s)** Good at reasoning but not trained to be useful assistant

**Performance:**
- **[33:55](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2035s)** AIME: passes O1 mini level
- **[34:05](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2045s)** MATH-500: on par with O1
- **[34:35](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2075s)** Ranges from hundreds to thousands of reasoning tokens

### Emergence of "Aha Moments"
**[Timestamp: 35:05](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2105s)**

**Emergent Behaviors:**
- **[35:18](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2118s)** As test-time compute increases, interesting behaviors emerge
- **[35:31](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2131s)** Models learn they're not forced to output immediately
- **[35:46](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2146s)** Begin to reflect, re-evaluate previous steps
- **[35:53](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2153s)** Explore alternative solution paths spontaneously
- **[36:29](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2189s)** Aha moments: models realize new approaches during reasoning

**Key Paper Quote:**
- **[36:31](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2191s)** "Aha moment for the model AND the researchers"
- **[36:39](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2199s)** "Power and beauty of reinforcement learning"
- **[36:46](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2206s)** Rather than teaching explicitly, provide right incentives
- **[36:56](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2216s)** Model autonomously develops advanced problem-solving strategies

**Example Aha Moment:**
- **[37:46](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2266s)** Math problem: square root equations
- **[38:13](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2293s)** Model says "Wait, wait, wait. That's an aha moment."
- **[38:17](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2297s)** Self-initiates re-evaluation of approach
- **[38:22](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2302s)** Finds better solution path: "square both sides"

### DeepSeek R1: Full Production Model
**[Timestamp: 39:04](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2344s)**

**4-Stage Training Pipeline:**

**Stage 1 - Cold Start (SFT):**
- **[39:23](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2363s)** Base model + some SFT prevents instability
- **[40:16](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2416s)** Long chain-of-thought style training data
- **[40:33](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2433s)** Human annotators for better readability
- **[40:43](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2443s)** Thinking formatted in <think> tags
- **[40:47](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2447s)** Couple thousand examples of SFT

**Stage 2 - RL for Reasoning:**
- **[39:41](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2381s)** Heavy RL on very hard code/math questions
- **[40:56](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2456s)** Same RL process as R1-Zero
- **[41:03](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2463s)** Math and LeetCode-style problems with verifiable outputs

**Stage 3 - Rejection Sampling:**
- **[39:53](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2393s)** Filter out negative behaviors
- **[41:13](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2473s)** Generate completions, rank with reward model
- **[41:18](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2478s)** Llama 3 introduced this concept
- **[41:27](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2487s)** 800K samples generated (600K reasoning, 200K general chat)
- **[41:32](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2492s)** Rank and filter samples

**Stage 4 - Final RL Polish:**
- **[40:04](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2404s)** Another round of RL for general use
- **[41:41](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2501s)** Similar to RLHF (Reinforcement Learning from Human Feedback)
- **[41:46](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2506s)** Make model helpful, harmless, and reason well
- **[41:55](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2515s)** Capture human preferences for nuanced situations
- **[42:09](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2529s)** Balance reasoning capability with chat quality

**Result:**
- **[42:12](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2532s)** Model good at chat, thinking, AND reasoning
- **[42:17](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2537s)** Aha moment emergent behaviors preserved

### Distillation Results
**[Timestamp: 44:17](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2657s)**

**Models Distilled (Original Release):**
- **[45:12](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2712s)** Qwen 1.5B, 7B, 14B, 32B
- **[45:16](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2716s)** Llama 8B, 70B
- **[45:05](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2705s)** Pure SFT-style distillation (not RL)
- **[45:33](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2733s)** Match logits, distill reasoning traces

**Performance:**
- **[45:18](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2718s)** Killed all base model benchmarks
- **[45:28](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2728s)** All distills on par with GPT-4o
- **[45:34](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2734s)** New 8B distill much better than GPT-4o

**RL on Small Models vs Distillation:**
- **[45:49](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2749s)** Tested RL on Qwen 32B for 10K steps
- **[45:52](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2752s)** **RL actually WORSE than distillation for small models**
- **[45:59](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2759s)** Small models need cold start, can't do pure RL from base
- **[46:24](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2784s)** Qwen had QWQ 32B reasoning model
- **[46:31](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2791s)** DeepSeek distillation on chat model performed much better

### Future Work & Limitations (Original)
**[Timestamp: 46:40](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2800s)**

**Original R1 Limitations:**
- **[46:42](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2802s)** Worse than V3 at function calling, multi-turn, JSON
- **[46:51](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2811s)** **Fixed in May 28th update - now has native function calling & JSON**
- **[46:57](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2817s)** Language mixing struggles (unknown if fixed)
- **[47:16](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2836s)** Sensitive to prompting - industry-wide problem
- **[47:18](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2838s)** "If still doing scaffolding with reasoning models, we're failing as labs"
- **[47:27](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2847s)** Not much better at engineering tasks than V3 (old news)

**Open Recreations:**
- **[47:36](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2856s)** Hugging Face has version
- **[47:40](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2860s)** Bespoke Labs working on it
- **[47:45](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2865s)** Several groups now have reproductions

### DeepSeek API & Adoption
**[Timestamp: 25:56](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1556s)**

**Initial Hype:**
- **[26:00](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1560s)** 10x faster and 10x cheaper than competitors at launch
- **[26:04](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1564s)** **"Fake news" - API super unreliable**
- **[26:07](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1567s)** API registration broken, almost always down

**Real Impact:**
- **[26:15](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1575s)** Takes 10% of OpenRouter API traffic
- **[26:24](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1584s)** Sparked significant adoption despite API issues
- **[26:30](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1590s)** Reopened the scaling race - "not done scaling"

---

## Follow-up Papers & Related Work

**[Timestamp: 23:47](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1427s)**

**Key Developments Post-DeepSeek:**
- **54 Models**: Showed RL effectiveness with just 6,000 samples
- **[24:08](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1448s)** Took 54 mini, made reasoning variant with tiny dataset
- **[24:27](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1467s)** Qwen thinking models followed
- **[24:34](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1474s)** Fi models (5 series) for small model RL
- **[37:32](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2252s)** Microsoft: scaling laws for RL on small models
- **[37:34](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2254s)** Qwen team: excellent thinking models (online talk available)

**[47:07](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2827s)** Latent Space podcast: interviews with reasoning experts from OpenAI

---

## Paper Club Community

### History & Impact
**[Timestamp: 00:16](https://www.youtube.com/watch?v=9k3xPh-40mo&t=16s)**

- **[00:16](https://www.youtube.com/watch?v=9k3xPh-40mo&t=16s)** Over a year of weekly sessions, no missed weeks
- **[00:48](https://www.youtube.com/watch?v=9k3xPh-40mo&t=48s)** Average 100 attendees per session (Wednesday noon)
- **[01:02](https://www.youtube.com/watch?v=9k3xPh-40mo&t=62s)** DeepSeek V3: 300 live attendees, 1000+ YouTube views
- **[01:14](https://www.youtube.com/watch?v=9k3xPh-40mo&t=74s)** All volunteer-run
- **[08:39](https://www.youtube.com/watch?v=9k3xPh-40mo&t=519s)** One of biggest open-source paper discussions

**Key Contributors:**
- **[52:36](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3156s)** Vibhu Sapra (presenter)
- **[52:38](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3158s)** Eugene Yan, Era, R.J., Flo (regulars)
- **[53:00](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3180s)** Swyx (Latent Space organizer)
- **[53:05](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3185s)** Hundreds join weekly on weekdays at noon

**Guest Speakers:**
- **[00:34](https://www.youtube.com/watch?v=9k3xPh-40mo&t=34s)** Authors from Nvidia, Meta, Allen AI, Amazon, Together, Writer
- **[00:41](https://www.youtube.com/watch?v=9k3xPh-40mo&t=41s)** Direct 1-hour sessions with paper authors

---

## Key Technical Insights

### Why RL Works So Well
**[Timestamp: 23:00](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1380s)**

- **[23:07](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1387s)** Native RL instead of supervised chain-of-thought data
- **[23:14](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1394s)** New dimension for scaling models
- **[23:35](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1415s)** Few months: O1 level → O3 level just with more RL
- **[28:43](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1723s)** Pure, beautiful, scaled-up RL - not hacks
- **[37:00](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2220s)** Not explicit teaching, just right incentives

### Why Previous Approaches Failed
**[Timestamp: 28:04](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1684s)**

- **[28:09](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1689s)** Process-based reward modeling didn't scale
- **[28:12](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1692s)** Beam search, MCTS were all hacks
- **[28:26](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1706s)** Twitter demos, fundraising, but nothing close to O1
- **[28:41](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1721s)** What worked: native pure RL

### Distillation as Post-Training Strategy
**[Timestamp: 14:51](https://www.youtube.com/watch?v=9k3xPh-40mo&t=891s)**

- **[14:56](https://www.youtube.com/watch?v=9k3xPh-40mo&t=896s)** Better recipe for small models: distill from big reasoning models
- **[15:48](https://www.youtube.com/watch?v=9k3xPh-40mo&t=948s)** Reasoning models make distillation even more efficient
- **[23:52](https://www.youtube.com/watch?v=9k3xPh-40mo&t=1432s)** Two key findings: (1) Pure RL from base works (2) Distillation really works
- **[44:06](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2646s)** Microsoft work: good distillation scaling laws

---

## Resources & Links

- **Test of Time Paper Club Sign-up:** QR code provided in presentation (details in Discord)
- **Discord:** Latent Space Discord - paper club channel
- **Video:** https://www.youtube.com/watch?v=9k3xPh-40mo
- **Original DeepSeek Paper Reading:** 1000+ views on YouTube
- **Pelican Bench:** Simon Willison's benchmark for foundation models
- **Qwen Reasoning Talk:** Online presentation available

---

## Final Recap

**[Timestamp: 49:52](https://www.youtube.com/watch?v=9k3xPh-40mo&t=2992s)**

**Main Takeaways:**

1. **New DeepSeek R1 (May 28th)**:
   - **[50:06](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3006s)** Reasons for twice as long (12K → 25K tokens)
   - **[50:10](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3010s)** Significantly better performance
   - **[50:15](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3015s)** Native structured JSON, function calling
   - **[50:20](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3020s)** Less hallucination
   - **[50:30](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3030s)** On par with O3 and Gemini 2.5

2. **New 8B Distillation**:
   - **[50:42](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3042s)** DeepSeek R1 Qwen2.5 8B
   - **[50:50](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3050s)** Distilled from longer reasoning traces
   - **[51:17](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3077s)** On-device, open-source
   - **[51:22](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3082s)** On par with Gemini 2.5 Flash Thinking, O3 Mini
   - **[51:29](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3089s)** Better than 54 models
   - **[51:33](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3093s)** 8B reasoner better than Qwen 32B

3. **Core Innovation:**
   - **[52:08](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3128s)** Aha moments through emergence
   - **[52:12](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3132s)** Inference-time scaling instead of next-token prediction
   - **[52:15](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3135s)** Train models to think longer

---

**Session Conclusion:** [52:25](https://www.youtube.com/watch?v=9k3xPh-40mo&t=3145s)

Special thanks to all Paper Club volunteers, attendees, and the AI Engineer World's Fair community. Join the Test of Time Paper Club launching June 2025!
