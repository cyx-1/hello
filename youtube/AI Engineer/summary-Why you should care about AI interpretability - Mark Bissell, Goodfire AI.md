# Summary: Why you should care about AI interpretability - Mark Bissell, Goodfire AI

**Video URL:** https://www.youtube.com/watch?v=6AVMHZPjpTQ

---

## Executive Summary

Mark Bissell from Goodfire AI presents a compelling case for AI interpretability, explaining how reverse-engineering neural networks enables developers to debug, steer, and understand AI models at the neuron level. The talk demonstrates practical applications through live demos of Goodfire's Ember platform, showing how interpretability has moved from research labs to real-world use cases. Key applications include neural programming for guardrails, dynamic prompting, PII detection, and novel user interfaces like painting with concepts. The presentation emphasizes that interpretability is becoming essential for AI engineers as it provides unprecedented control over model behavior and unlocks new capabilities.

---

## Key Topics

### 1. **Introduction to Mechanistic Interpretability**
[https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=60s](https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=60s)

- Definition: Reverse engineering neural networks to understand their internal workings
- Growing focus at major AI labs (Anthropic, etc.)
- Famous example: Golden Gate Claude - manipulating neurons to make Claude obsessed with the Golden Gate Bridge
- Moving from lab demos to real-world practical applications

**Key Points:**
- Interpretability techniques allow "opening the black box" of AI models
- Anthropic's team found neurons representing Claude's concept of the Golden Gate Bridge
- By keeping those neurons always active, they created "Golden Gate Claude" that brings up the bridge in every conversation

---

### 2. **Challenges in AI Development**
[https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=248s](https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=248s)

- Traditional approaches have limitations:
  - **Prompt engineering**: "Whack-a-mole" problem - fixing one issue breaks another
  - **LLM-as-a-judge**: Expensive, not scalable, requires monitoring another system
  - **Fine-tuning**: Requires domain-specific data, models learn spurious correlations, mode collapse, reward hacking

**Key Points:**
- Working with AI lacks the rigor of traditional software development
- Models are non-deterministic and unpredictable
- Need for more precise control over model behavior

---

### 3. **Demo: Neural Programming with Ember Platform**
[https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=427s](https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=427s)

**PII Protection Example:**
- User tells model to keep email confidential, but model immediately reveals it when asked
- Attribution feature shows what the model was "thinking" when generating each token
- Identified feature: "discussions of sensitive and protected information"
- By turning up this feature 60%, model successfully refuses to share the email

**Dynamic Prompting Example:**
[https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=600s](https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=600s)
- Set conditional listener: when "beverages and consumer brands" feature fires
- Automatically inject context-specific prompt (e.g., "recommend Coca-Cola")
- Model seamlessly switches recommendations in real-time without user seeing the intervention

**Key Points:**
- Can see internal features/neurons active during token generation
- Can steer model behavior by adjusting feature activation levels
- Enables precise, surgical control over model outputs

---

### 4. **Real-World Applications**
[https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=681s](https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=681s)

Current customers using Ember:
- **Racketton**: Multilingual PII detection in chatbots
- **Hayes Labs**: Red teaming and guardrail testing

Research directions:
- **Model diffs**: Git-like diffs for models showing which features changed during post-training
- Detect unwanted changes (e.g., sycophancy) before deployment
- Quality assurance for model training

---

### 5. **Demo: Paint with Ember - Novel UI for Image Models**
[https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=767s](https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=767s)

- Interactive canvas instead of text prompts for image generation
- Paint directly with concepts (pyramid, wave, lion face)
- Control positioning, strength, and combinations of concepts
- Explore sub-features: lion face = main feature + sub-features
- Discover model's internal logic: "tiger ≈ lion - mane"
- Try it at: paint.goodfire.ai

**Key Points:**
- Completely new interaction paradigm for generative models
- Familiar tools: drag, erase, adjust intensity
- Fine-grained control over generated images
- Reveals how models conceptualize relationships between concepts

---

### 6. **Long-Tail Use Cases**
[https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=997s](https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=997s)

**Explainable Outputs:**
- Critical for regulated industries (finance, healthcare, law)
- Understand why models make specific decisions

**Scientific Knowledge Extraction:**
[https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=1012s](https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=1012s)
- Partnership with ARC Institute on EVO2 genomics model
- Extract biological concepts superhuman models learned that humans don't know
- Working with major health system to identify novel biomarkers of disease
- Applications in genomics, biology, and precision medicine

**Efficiency Gains:**
[https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=1083s](https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=1083s)
- Identify wasted weights (e.g., memorized data)
- Prune models for specific tasks (e.g., coding-only Claude)
- More efficient deployment

---

### 7. **Philosophical Argument for Interpretability**
[https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=1120s](https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=1120s)

- Engineers naturally want to understand how systems work
- Frustrating but fascinating: we don't know how models do what they do
- Interpretability is one of the most important and interesting problems in AI
- Essential for AI engineers to stay current with this field

**Key Points:**
- Combines practical value with intellectual curiosity
- Moving from research curiosity to engineering necessity
- Right time for AI engineers to care about interpretability

---

### 8. **Q&A: How Are Features Found?**
[https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=1217s](https://www.youtube.com/watch?v=6AVMHZPjpTQ&t=1217s)

- Current best practice: **Sparse autoencoders** (SAE)
- Trade-offs exist, other methods being explored
- Field rapidly developing - expect new techniques in coming years
- Recommend researching sparse autoencoders to understand Golden Gate Claude example

---

## Resources

- **Paint with Ember Demo:** paint.goodfire.ai
- **Goodfire Website:** goodfire.ai (blog posts, jobs)
- **Technical Blog Post:** Detailed explanation of how Paint with Ember works
- **Hiring:** Goodfire is actively hiring for interpretability roles

---

## Conclusion

AI interpretability has transitioned from academic curiosity to practical engineering tool. The ability to inspect, understand, and steer neural networks at the feature level enables:
- More reliable and controllable AI systems
- Novel user interfaces and interaction paradigms
- Scientific knowledge discovery from superhuman models
- Better debugging and quality assurance for production AI

For AI engineers, interpretability represents a new category of "power user tools" that will become increasingly essential as AI systems become more capable and widely deployed.

---

**Last Updated:** 2026-01-03
