# The Rise of Open Models in the Enterprise — Amir Haghighat, Baseten

**Video URL:** https://www.youtube.com/watch?v=3WV1vT0B0cg

---

## Executive Summary

Amir Haghighat, CTO of Baseten, shares insights from talking to 100+ enterprises about AI adoption. He challenges the narrative that enterprises are slow to adopt AI, revealing a significant shift in 2025 where companies are moving beyond closed frontier models (OpenAI, Anthropic) toward open source models. The key drivers are quality for specialized tasks, latency requirements, unit economics in agentic workflows, and competitive differentiation. However, building production-grade inference infrastructure is far more complex than simply combining a model, GPUs, and an inference engine - requiring sophisticated optimizations for performance, reliability, scalability, and observability.

---

## Main Topics

### [Introduction: Why Enterprise AI Adoption Matters](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=0s)
- Baseten's unique position: selling horizontal AI tooling to enterprises from Fortune 50 to software companies
- Why enterprise adoption matters: massive reach, capital, and paradigm shift potential
- The misconception that slow enterprise adoption means AI is overhyped

### [The Enterprise AI Journey (2023-2025)](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=137s)
- **2023**: "Toying around" phase - CIOs dismissively letting engineers experiment with dedicated OpenAI/Anthropic deployments
- **2024**: Production use cases emerge - 40-50% of enterprises had something in production using closed models
- **2025**: Paradigm shift - cracks appearing in the "just use closed models" assumption

### [Why Enterprises Start with Closed Models](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=196s)
- Easy to get started with OpenAI and Anthropic
- Dedicated deployments on Azure/AWS for security and privacy
- ML teams transitioning to AI teams building on top of these models
- Strong inertia to stick with closed models if they work

### [The Four Cracks in the Closed Model Assumption](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=297s)

**What the cracks are NOT:**
- Not vendor lock-in (multiple interoperable options exist with OpenAI specs)
- Not ballooning costs (price per token was plummeting in 2024)
- Not compliance/privacy/security (handled by frontier companies + CSPs)

**The REAL cracks:**

#### [1. Quality for Specialized Tasks](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=416s)
- Frontier models aren't necessarily the right tool for specific use cases
- Example: Health plans doing medical document extraction (CPT codes, diagnosis codes, prescriptions)
- Organizations have proprietary labeled data and can do better than generic Claude/GPT
- Example: Medical transcription understanding healthcare jargon

#### [2. Latency Requirements](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=498s)
- Frontier model APIs optimized for high throughput and QPS at expense of latency
- AI voice calls and phone systems require critical time-to-first-token and time-to-first-sentence
- Need different optimization strategy than what shared APIs provide

#### [3. Unit Economics in Agentic Workflows](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=547s)
- 2025 brought explosion of agentic use cases
- Single user action can result in 50+ inference calls
- Cost problem that was "taking care of itself" suddenly isn't
- Running models on owned compute cheaper than per-token pricing with someone else's margins
- Moving from price taker to price maker

#### [4. Competitive Differentiation](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=609s)
- CIOs/CTOs asking: "If we and our competitors use the same frontier models, what's our advantage?"
- Desire to differentiate at the AI level, not just workflow/application level
- Need for proprietary AI capabilities as competitive moat

### [The Complexity of Production Inference ("Here Be Dragons")](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=656s)

The misconception: Model + vLLM/SGLang/TRTLM + GPUs = Production inference

**Performance Layer Challenges:**
- Speculative decoding: choosing between draft models, Medusa heads, Eagle 3, MTP
- New techniques emerging constantly (Eagle 3 paper only 6 months old but already production-critical)
- Need to stay on top of research - not just flipping switches in inference engines
- Prefix caching optimization for agentic use cases with large, similar prompts
- Disaggregated serving architecture

**Infrastructure Layer Challenges:**

#### [Reliability](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=824s)
- Guaranteeing four nines (99.99%) uptime for mission-critical inference
- Handling hardware failures gracefully
- Managing vLLM and Triton crashes without tail latency spikes
- Not over-provisioning (which destroys unit economics)

#### [Scalability](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=873s)
- Handling traffic bursts effectively
- One enterprise example: 8 minutes to bring up new replica
- Tail latencies spike during traffic surges with slow scaling

#### [Developer Velocity](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=902s)
- Tooling for engineers to move fast
- Model lifecycle management
- Observability (not just "logs and metrics" - much deeper iceberg)
- Enterprise controls and audits

### [The Build vs Buy Decision](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=933s)
- Enterprises face choice: build inference infrastructure or buy platform
- Amir's challenge: convincing enterprises to buy this layer rather than build
- Trade-offs between control and speed to market

### [Closing Offers](https://www.youtube.com/watch?v=3WV1vT0B0cg&t=963s)
- For enterprises: discuss resonant challenges
- For startups: share lessons on building for enterprise deployment
- Invitation to Baseten happy hour

---

## Key Insights

1. **The 2025 Inflection Point**: Enterprises are actively moving from closed models to open source due to real technical and economic constraints, not ideology

2. **Agentic Workflows Changed Everything**: The explosion of agentic use cases fundamentally broke the unit economics that made closed model APIs attractive

3. **Specialization Beats Generalization**: For domain-specific tasks with proprietary data, specialized fine-tuned models outperform frontier general models

4. **Infrastructure Complexity is Underestimated**: Production inference requires far more than model + inference engine + GPUs - reliability, performance optimization, and observability are massive undertakings

5. **Competitive Moats Require Proprietary AI**: Enterprises realize that using the same models as competitors provides no differentiation

6. **The Real Blockers Aren't What You Think**: Vendor lock-in, cost, and compliance aren't driving the shift - quality, latency, economics, and differentiation are

---

## Target Audience

- Enterprise AI leaders and CTOs considering open source model adoption
- Startups building AI infrastructure for enterprise deployment
- Engineers responsible for production AI systems
- Anyone interested in the real-world challenges of enterprise AI adoption
