# How Intuit uses LLMs to explain taxes to millions of taxpayers - Jaspreet Singh, Intuit

**Video URL:** https://www.youtube.com/watch?v=_zl_zimMRak

---

## Executive Summary

Jaspreet Singh, Senior Staff Engineer at Intuit, presents how TurboTax leverages LLMs to help millions of users understand their taxes. With 44 million tax returns processed in 2023, Intuit built GenOS, a proprietary generative AI platform designed for enterprise scale, safety, and regulatory compliance. The talk covers their journey from prompt engineering to fine-tuning Claude 3 Haiku, their evaluation framework combining human tax experts with LLM-as-a-judge, and critical learnings about latency, vendor lock-in, and the absolute necessity of comprehensive evaluation systems.

---

## Main Topics

### [Introduction and Scale](https://www.youtube.com/watch?v=_zl_zimMRak&t=17s)
**Timestamp:** 00:17 - 00:52

- Jaspreet Singh introduces his role in GenAI for TurboTax
- **Scale:** TurboTax processed 44 million tax returns for tax year 2023
- Goal: Help everyone have high confidence in their tax filing and understand they're getting the best deductions

**Key Points:**
- Massive scale requiring enterprise-grade solutions
- Focus on user confidence and understanding
- Not just filing, but explaining taxes to taxpayers

---

### [User Experience - GenAI in TurboTax](https://www.youtube.com/watch?v=_zl_zimMRak&t=61s)
**Timestamp:** 01:01 - 01:40

- Shows examples of how LLMs explain tax credits and deductions
- Helps users understand tax breaks they're receiving
- Provides overall tax outcome summaries (refunds, amounts owed)

**Key Points:**
- Contextual explanations throughout the filing process
- Breaking down complex tax concepts into understandable language
- Personalized to user's specific tax situation

---

### [GenOS Platform Architecture](https://www.youtube.com/watch?v=_zl_zimMRak&t=100s)
**Timestamp:** 01:40 - 02:50

- **GenOS:** Intuit's proprietary Generative OS platform
- Built because off-the-shelf Gen AI tooling didn't support their use cases
- Critical requirements: Safety, security, regulatory compliance

**Platform Components:**
- **GenUX:** UI layer for generative experiences
- **Orchestrator:** Routes different queries to appropriate LLM solutions across teams
- **Intuit Assist:** Overall brand for GenAI-powered experiences

**Why build custom platform:**
- Working in regulated tax industry requires special controls
- Need for enterprise-scale solutions
- Safety and security are paramount

---

### [Model Selection and Architecture](https://www.youtube.com/watch?v=_zl_zimMRak&t=170s)
**Timestamp:** 02:52 - 05:00

**Static vs Dynamic Queries:**

**Static Queries (Prepared statements):**
- Predefined use cases (e.g., tax summary explanations)
- Model: **Claude** (Anthropic) - multi-million dollar contract
- Think of it as a prepared SQL statement with dynamic tax data

**Dynamic Queries (Open-ended Q&A):**
- User-generated questions (e.g., "Can I deduct my dog?")
- Model: **GPT-4 Mini** (OpenAI) - now iterating on newer versions
- More flexible, handles unpredictable queries

**Supporting Technologies:**
- **RAG (Retrieval Augmented Generation):** For accessing tax information
- **Graph RAG:** Enhanced retrieval with relationship understanding
- **Fine-tuned Claude 3 Haiku:** Piloted for specialized use cases

**Key Points:**
- IRS changes forms every year - need dynamic knowledge retrieval
- Intuit has proprietary tax engines that provide ground truth
- Fine-tuning shows quality improvements but requires significant effort
- Models evaluated continuously as new versions release monthly

---

### [Fine-tuning Claude 3 Haiku](https://www.youtube.com/watch?v=_zl_zimMRak&t=422s)
**Timestamp:** 07:20 - 08:00

**Fine-tuning Approach:**
- Used **Claude 3 Haiku** via **AWS Bedrock**
- Focused on static queries only
- Goal: Reduce prompt size while maintaining quality

**Benefits:**
- Fewer instructions needed in prompts
- Reduced latency through smaller prompts
- Quality maintained or improved

**Findings:**
- Model became too specialized for specific use cases
- Trade-off between specialization and flexibility
- Requires effort to maintain and update

**Data Compliance:**
- Only used consented user data
- Strict adherence to privacy regulations (7216)
- Separate test AWS environments for safety

---

### [Evaluation Framework - The Foundation](https://www.youtube.com/watch?v=_zl_zimMRak&t=332s)
**Timestamp:** 05:32 - 07:20 and 08:20 - 10:10

**Three Key Pillars:**
1. **Accuracy** - Tax information must be correct
2. **Relevancy** - Answers must address the user's question
3. **Coherence** - Responses must be well-structured and understandable

**Multi-Phase Evaluation:**

**Phase 1: Human Domain Experts (Manual)**
- Tax analysts as primary evaluators
- Decode IRS changes year-over-year
- **Tax analysts as prompt engineers** - unique approach
- Creates baseline "golden dataset" via AWS Ground Truth
- Used in initial development lifecycle

**Phase 2: Automated Evaluation**
- **LLM-as-a-Judge** approach
- Uses GPT-4 series (until recently) to evaluate responses
- Operates on prompts trained with golden dataset from experts
- Minor iterations can use auto-eval without manual review

**Phase 3: Production Monitoring**
- Real-time sampling of LLM responses to actual users
- Automated systems continuously monitor quality
- Broad monitoring across all interactions

**Benefits of Tax Analysts as Prompt Engineers:**
- Data science/ML teams focus on metrics and quality frameworks
- Domain experts provide tax expertise directly
- Enables faster iteration and better prompt quality
- Automated prompt chaining tools help update LLM-as-a-judge

**Evaluation for Model Changes:**
- Moving from Claude Instant to Claude 3 Haiku required full re-evaluation
- Model changes are NOT smooth - require extensive testing
- Clear eval framework makes model migrations possible
- Tax year changes (23 to 24) trigger major re-evaluation cycles

---

### [Major Learnings and Challenges](https://www.youtube.com/watch?v=_zl_zimMRak&t=614s)
**Timestamp:** 10:14 - 12:10

**1. Vendor Costs and Lock-in:**
- Contracts are expensive (multi-million dollar commitments)
- Only slightly cheaper with long-term contracts
- Results in vendor lock-in
- Importance of strong vendor partnerships for iteration
- **Prompts themselves create lock-in** - not portable across vendors
- Even upgrading models from same vendor is difficult

**2. Latency Challenges:**
- LLMs don't have traditional backend SLAs (100-200ms)
- Dealing with 3-10+ second response times
- Prompts balloon with complex tax situations (homeowner, stocks, spouse, etc.)
- **Peak season (April 15 tax day):** Latency shoots through the roof
- Must design product around latency constraints

**Solutions:**
- Fallback mechanisms for slow responses
- User experience design accommodates wait times
- Product design ensures explanations are helpful above all

**3. Hallucination Prevention:**
- Numbers come from tax knowledge engine, NOT LLMs
- LLMs only explain pre-calculated ground truth
- Safety guardrails validate LLM output before user delivery
- ML models check for hallucinated numbers
- Never let LLMs do calculations

**4. Evaluation is Mandatory:**
- **"Evals are a must to launch"** - emphasized multiple times
- Clear guidelines on what you're building
- Clear golden dataset from domain experts
- Cannot launch without comprehensive evaluation framework

---

### [Q&A Highlights](https://www.youtube.com/watch?v=_zl_zimMRak&t=733s)
**Timestamp:** 12:17 - 18:52

**When to use different evaluation types:**
- Initial development: Manual evaluations with tax experts
- Minor prompt tweaks: Automated evaluations with LLM-as-a-judge
- Major changes (new tax year, model switches): Return to manual evaluations
- Creates baseline that enables automated evals

**Types of user questions:**
- Product questions: "How do I do this in TurboTax?"
- Tax situation questions: "Can I claim tuition paid for my grandchild?"
- Different teams handle different question types
- **Planner component** routes queries to appropriate solutions

**Number verification:**
- Tax knowledge engine provides all calculations
- LLMs never calculate numbers
- Safety guardrails prevent hallucinated numbers in final answers
- ML models validate output before user sees it

**RAG vs Graph RAG:**
- Graph RAG shows better response quality than traditional RAG
- **Personalization outperforms both** - most important factor
- Key is answering based on user's specific tax situation

**Future model evaluation:**
- Constantly evaluating new models (Claude 4, in-house models)
- Post-tax season is evaluation and improvement time
- No definitive answer yet for next tax year's model selection

**Legal and compliance:**
- Heavy focus on legal and privacy controls
- Static queries reduce risk through testing and validation
- Tax experts craft and validate all prompts
- Numbers always sourced from validated tax knowledge engine

---

## Key Takeaways

1. **Scale Requires Custom Infrastructure:** 44M users drove need for GenOS platform
2. **Domain Experts as Prompt Engineers:** Tax analysts directly craft prompts, enabling ML teams to focus on quality metrics
3. **Hybrid Model Strategy:** Claude for static, GPT-4 Mini for dynamic, constant evaluation of alternatives
4. **Evaluation is Non-Negotiable:** Manual + automated + production monitoring across accuracy, relevancy, coherence
5. **Never Let LLMs Calculate:** Use LLMs to explain ground truth from tax engines, not generate numbers
6. **Design Around Latency:** Product must accommodate 3-10+ second responses, especially during peak season
7. **Vendor Lock-in is Real:** Even model upgrades within same vendor require significant re-work
8. **Personalization Wins:** Graph RAG is good, but personalized answers based on user situation are best
9. **Regulatory Compliance First:** Privacy, safety, and legal controls are built into the platform foundation
10. **Continuous Re-evaluation:** Tax law changes yearly, models change monthly - evaluation is continuous

---

**Last Updated:** January 3, 2026
