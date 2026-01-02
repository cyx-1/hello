# Memory in LLMs: Weights and Activations - Jack Morris, Cornell

**Video URL:** https://youtu.be/Jty4s9-Jb78

---

## Executive Summary

Jack Morris from Cornell presents a comprehensive analysis of how LLMs store and access knowledge, comparing three main approaches: full context, RAG (retrieval-augmented generation), and training knowledge into model weights. He argues that while full context and RAG are currently dominant, they have fundamental limitations that will necessitate a shift toward training knowledge directly into model weights for future AI systems. The talk covers the technical challenges, trade-offs, and emerging solutions for each approach, with particular emphasis on why embeddings-based RAG systems won't scale for enterprise applications.

---

## Main Topics

### [Introduction: LLM Knowledge Limitations](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=22s)

**[00:22 - 02:30]**
- ChatGPT's impressive general knowledge vs. its blind spots
- Knowledge cutoff dates prevent access to recent information
- Long-tail tasks (niche/specialized domains) are difficult for general LLMs
- Examples: AMD GPU optimization, company-specific data, personal preferences
- The fundamental problem: How do we inject new knowledge into LLMs?

**Key points:**
- LLMs can't learn or practice - they have fixed knowledge
- Private/proprietary data isn't in training sets
- Specialized domains lack sufficient training data

### [Three Approaches to Knowledge Injection](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=142s)

**[02:24 - 03:30]**
1. **Full Context**: Cramming everything into the context window
2. **RAG**: Retrieval-augmented generation using vector databases
3. **Training into Weights**: The emerging approach (talk's main focus)

---

## Full Context Approach

### [Limitations of Full Context](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=253s)

**[04:10 - 05:10]**
- **Expensive**: High cost in US dollars and compute
- **Slow**: Orders of magnitude slowdown with large contexts
  - 1K tokens context: 10,000 tokens/second output
  - 128K tokens context: 130 tokens/second output
- Personal example: Pasting 80-page thesis into Claude caused 10x slowdown

### [Technical Constraints](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=320s)

**[05:20 - 07:00]**
- Transformer architecture's quadratic attention complexity
- Self-attention requires all tokens to "look at" each other
- Memory bottleneck becomes infeasible at scale
- Long context windows (Grok 4: 2M tokens, Gemini 3: 1M tokens) exist but don't work well

**[06:19 - 07:00]**
- Difference between "model not breaking" vs "properly reasoning"
- Models haven't learned to truly reason across millions of tokens

### [Context Bloat Problem](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=419s)

**[07:00 - 08:00]**
- Chroma's "Context Bloat" research shows performance degradation
- More irrelevant context = worse performance
- Claude performs best among models but still degrades significantly
- At 10K tokens of context, models become unreliable even with relevant data

### [Alternative Architectures](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=492s)

**[08:12 - 09:30]**
- Efficient architectures explored: Mamba, state space models, linear attention, hybrid attention, sparse attention, sliding window
- All have trade-offs in performance vs efficiency
- Minimax M2 example: Chinese labs tried hybrid architectures but reverted to standard quadratic attention
- **Conclusion**: No architectural silver bullet yet

---

## RAG (Retrieval-Augmented Generation)

### [How RAG Works](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=619s)

**[10:19 - 12:00]**
- Most attendees use RAG weekly (show of hands)
- Vector databases store embeddings (Turbopuffer, Pinecone, Chroma, etc.)
- Andre Karpathy's vision: "Embeddings are the file system of LLMs"
- **Easy to use**: Only 5 lines of code to implement
- Speaker's perspective: "Embeddings are the file system of today, not the future"

### [Problem 1: Security Vulnerabilities](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=743s)

**[12:24 - 14:40]**
- **No security through obscurity**: Embeddings look random but are reversible
- Morris's research: Built system to decode embeddings back to text
- Can recover 90% of original text from embeddings
- **Implication**: Vector databases provide no security benefits for sensitive data
- Embeddings are analogous to text, not encrypted data

### [Problem 2: Non-Adaptive Embeddings](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=886s)

**[14:46 - 17:00]**
- Embeddings represent one universal semantic space
- Example: Visa vs Mastercard documents cluster too closely together
- Can't differentiate between similar but distinct categories
- **Solution attempted**: Contextual embeddings (Morris's research)
  - Feed surrounding documents as context when creating embeddings
  - Dynamically adjusts embeddings based on domain
  - Adopted by OpenAI and Anthropic
  - Works better on niche/long-tail domains

### [Problem 3: Fundamental Limitations](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=1106s)

**[18:26 - 19:50]**
- Fixed-dimensional vectors can't capture all possible relationships
- Combinatorial explosion of relationships
- Questions requiring reasoning across multiple documents fail
- Implicit information not explicitly stated in documents is lost
- **Chunking problem**: Can never retrieve everything needed

### [Audience Satisfaction](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=750s)

**[12:30]**
- Show of hands: Almost no one completely satisfied with RAG systems
- General agreement: "There must be something better"

---

## Training Knowledge into Weights

### [The Case for Weight-Based Memory](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=1357s)

**[22:37 - 24:00]**
- **Goal**: Inject knowledge into model parameters, not just context
- Models should forget irrelevant information (e.g., Tajikistan's smallest province)
- Fixed capacity in LLMs: ~3.6 bits per parameter
- Example: 1B parameter model ≈ 4GB of information storage
- Want to delete useless knowledge and replace with domain-specific data

### [Three Key Questions](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=1492s)

**[24:52 - 25:20]**
1. **How to train**: RL vs SFT (supervised fine-tuning)?
2. **What data to use**: Raw data vs synthetic/augmented data?
3. **Architecture choices**: Which model architecture is best for continual learning?

---

## Learning Methods

### [Supervised Fine-Tuning (SFT) vs Reinforcement Learning](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=1555s)

**[25:55 - 32:00]**
- Traditional approach: Fine-tune on question-answer pairs
- **Data augmentation is critical**: Generate QA pairs from raw documents
- Models trained on augmented data significantly outperform raw document fine-tuning
- Example: 100 raw documents → 3,000 synthetic QA pairs = much better performance

### [Why RL is Superior to SFT](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=2640s)

**[44:00 - 44:30]**
- RL (specifically GRPO - Group Relative Policy Optimization) uses sparse rewards
- **Key finding**: RL achieves same performance with 1000x fewer parameters trained
- SFT provides rich signal (cross-entropy on all tokens) but requires many more parameters
- RL gives binary reward (correct/incorrect) but is more parameter-efficient
- Trade-off: Information density vs parameter efficiency

---

## Architecture Considerations

### [Modular vs Integrated Memory](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=2200s)

**[36:40 - 40:00]**

**Option 1: Full Fine-Tuning**
- Train all model parameters on new data
- Risk: Catastrophic forgetting of original capabilities
- Expensive and slow

**Option 2: Adapters/LoRA**
- Add small adapter layers, freeze base model
- ~1% of model parameters
- Fast to train but limited capacity
- Only works for small amounts of new knowledge

**Option 3: Mixture of Experts (MoE)**
- Multiple "expert" modules, router selects which to use
- Allows specialization without forgetting
- Can swap experts for different domains
- More complex but scalable

### [Trade-offs Summary](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=2350s)

**[39:10 - 40:30]**
- Adapters: Fast and cheap but limited capacity
- Full fine-tuning: High capacity but expensive and risky
- MoE: Balanced approach, emerging as preferred solution
- Architecture matters again (unlike the transformer monopoly era)

---

## Hybrid Approaches

### [Combining Methods](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=2760s)

**[46:00 - 47:00]**
- We'll always use some combination of context, RAG, and weight-based memory
- Weight training for stable, frequently-accessed knowledge
- RAG for rapidly changing or rarely-accessed information
- Context for user-specific, session-level data

**Comparison with Deep Research:**
- Deep Research: Low training cost, high inference cost
- Weight training: High training cost, low inference cost
- Different trade-offs for different use cases

---

## Key Insights and Recommendations

### [When to Use Each Approach](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=2730s)

**Full Context:**
- Small, temporary datasets
- Real-time, session-specific information
- When training isn't worth the overhead

**RAG:**
- Large, slowly-changing document repositories
- When you need semantic search capabilities
- As a complement to other methods

**Weight Training:**
- Stable, domain-specific knowledge
- High-value, frequently-accessed information
- When you can afford upfront training costs
- Enterprise applications with proprietary data

### [Future Predictions](https://www.youtube.com/watch?v=Jty4s9-Jb78&t=2655s)

**[44:15 - 46:30]**
- **"No one is doing this [weight training] right now, but people will start"**
- Every user/company will have personalized models
- Models will be continuously updated with new knowledge
- Architecture will matter more as personalization increases
- The field will shift from inference-time compute (RAG, agents) to training-time compute

---

## Open Questions

1. **Economic thresholds**: How much data is needed for weight training to be economically feasible vs RAG?
2. **Frequency effects**: How does information frequency affect the training vs RAG trade-off?
3. **Scaling personalization**: Can we handle millions of personalized models (B2C scale)?
4. **Catastrophic forgetting**: How to prevent models from losing capabilities while learning new information?
5. **Knowledge graphs**: Could they augment or replace embeddings for certain use cases?

---

## Recommended Resources

- **Chroma's "Context Bloat" Report**: Research on performance degradation with large contexts
- **Morris et al.**: Contextual embedding research (adopted by OpenAI, Anthropic)
- **Embedding inversion attacks**: Security implications for vector databases

---

## Conclusion

The future of LLM memory systems will involve a sophisticated orchestration of three approaches:
1. **Context** for ephemeral, user-specific data
2. **RAG** as a transitional technology for search and retrieval
3. **Weight-based memory** as the primary knowledge store for important, stable information

The key insight is that better performance always requires more compute—either at training time or inference time. The industry is beginning to shift toward training-time investment (weight-based memory) for better inference-time efficiency and capability.

