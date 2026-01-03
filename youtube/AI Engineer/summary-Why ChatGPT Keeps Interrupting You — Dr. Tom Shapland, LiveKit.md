# Why ChatGPT Keeps Interrupting You — Dr. Tom Shapland, LiveKit

**Video URL:** https://www.youtube.com/watch?v=1v9zBiZKlIY

---

## Executive Summary

Dr. Tom Shapland from LiveKit explores why voice AI agents like ChatGPT's Advanced Voice Mode frequently interrupt users, identifying it as the biggest problem in voice AI today. The talk contrasts the complex, predictive turn-taking mechanisms in human conversation with the relatively simple Voice Activity Detection (VAD) systems used in current AI agents. Shapland presents three approaches to solving this problem: augmenting VAD with semantic models, incorporating acoustic features, and full-duplex models that process input and generate output simultaneously. While full-duplex models show promise, he predicts the future lies in smarter VAD augmentations within cascading model architectures.

---

## Main Topics

### [Introduction: Voice AI's Interruption Problem](https://www.youtube.com/watch?v=1v9zBiZKlIY&t=16s)
**Key Points:**
- Interruptions are the biggest problem in voice AI agents today
- When ChatGPT interrupts, it's annoying; when a medical AI interrupts a patient, they hang up and businesses lose customers
- This is a collective industry problem that needs solving
- Turn-taking is fundamentally hard because it happens very fast in human conversation

### [Cultural Differences in Turn-Taking](https://www.youtube.com/watch?v=1v9zBiZKlIY&t=107s)
**Key Points:**
- There's no one-size-fits-all approach to turn-taking
- Research shows significant variation across cultures (Danish speakers wait longer vs. Japanese speakers respond almost instantaneously)
- Individual differences also exist - some people naturally take longer to respond
- Response time varies within individuals based on emotional state (anger leads to quicker responses)

### [Current Voice AI Pipeline Architecture](https://www.youtube.com/watch?v=1v9zBiZKlIY&t=146s)
**Key Points:**
- Standard pipeline: Speech input → Speech-to-text model → VAD (Voice Activity Detection) → LLM → Text-to-speech → Audio output
- VAD has two parts:
  1. Neural network detecting speech vs. non-speech
  2. Silence algorithm (e.g., if no speech for >0.5 seconds, user is done)
- This system is much simpler than human turn-taking mechanisms

### [How Humans Handle Turn-Taking](https://www.youtube.com/watch?v=1v9zBiZKlIY&t=250s)
**Key Points:**
- Turn-taking is a "psycholinguistic puzzle" - humans respond in ~200ms but generating speech takes ~600ms
- Solution: Prediction - listeners predict when the speaker will finish and start generating responses beforehand
- Primary inputs for prediction:
  - **Semantics** (most important) - what the person is saying
  - **Syntax** - sentence structure
  - **Prosody** - expressiveness and tone
  - **Visual cues** - body language and facial expressions
- Human minds are "full duplex" - processing input and generating output simultaneously

### [Three-Stage Human Turn-Taking Model](https://www.youtube.com/watch?v=1v9zBiZKlIY&t=346s)
**Key Points:**
1. **Semantic Prediction Stage**: Continuously inferring the speaker's intended message and predicting end of utterance
2. **Refinement Stage**: As you get closer to predicted endpoint, refine prediction using both semantics and syntax
3. **Finalization Stage**: Just before end of turn, finalize prediction using prosody and acoustic features
- This process happens multiple times, constantly updating predictions as the speaker continues

### [Contrasting Human vs. Current AI Systems](https://www.youtube.com/watch?v=1v9zBiZKlIY&t=508s)
**Key Points:**
- Current AI systems are much simpler: just "speech or not speech"
- AI looks backward, not making predictions
- Processing is done serially, nothing happens in parallel
- This simplicity is part of why interruptions are so problematic

### [Approach #1: Augmenting VAD with Semantic Models](https://www.youtube.com/watch?v=1v9zBiZKlIY&t=533s)
**Key Points:**
- LiveKit's text-based semantic model takes last 4 turns of conversation as input
- Uses transformer model to predict end-of-utterance token
- If model predicts turn isn't finished, it extends the silence threshold
- Works in concert with traditional VAD
- **Demo Results**: Night and day difference - semantic model prevents inappropriate interruptions during natural pauses

### [Approach #2: Audio-Based Models with Acoustic Features](https://www.youtube.com/watch?v=1v9zBiZKlIY&t=781s)
**Key Points:**
- These models look at both text semantics AND audio signal/acoustic features
- Input: Audio tokens → Output: Probability that user has finished speaking
- Examples:
  - **Daily's Smart Turn Model**: Open-weight model combining transformer with acoustic characteristics
  - **AssemblyAI's Streaming STT**: Single model that outputs both transcript and likelihood speaker is done
  - **Kyutai**: Also released a model with similar approach
- **Limitation**: Speech-to-text built-in models only see user input, not agent's responses (missing half the context)
- Despite limitation, these approaches work remarkably well and are easy to implement

### [Approach #3: Full-Duplex Models](https://www.youtube.com/watch?v=1v9zBiZKlIY&t=968s)
**Key Points:**
- More like human minds - process input and generate output simultaneously
- Trained on raw audio data (not handwritten rules)
- Analogy to computer vision: Like giving neural nets raw image data instead of handcrafted feature detection
- **Moshi Model**: Always listening to input AND always generating output (even emits natural silence when not speaking)
- **Meta's SyncLLM**: Full-duplex experimental model that forecasts user speech ~5 tokens (200ms) ahead, similar to human prediction
- **Downsides**:
  - Not commercially viable yet
  - Optimized for turn-taking but "dumb LLMs"
  - Small models with limited training data
  - Poor instruction-following capabilities
  - Lack control needed for production use cases (e.g., brand name pronunciation)

### [Why ChatGPT Keeps Interrupting (Answer to Title)](https://www.youtube.com/watch?v=1v9zBiZKlIY&t=921s)
**Key Points:**
- OpenAI's real-time API still uses basic VAD internally (speech or not speech)
- Can optionally turn on "semantic VAD" (paradoxical term) that augments with semantic model
- Interrupts based on how long since last word OR based on previous utterances
- Not sophisticated enough yet - problem not totally solved
- OpenAI uses LiveKit for audio transport layer but not LiveKit's end-of-utterance model

### [Future Predictions](https://www.youtube.com/watch?v=1v9zBiZKlIY&t=1094s)
**Key Points:**
- Full-duplex models are interesting but won't solve the problem for production use
- Production systems need more control (e.g., brand names, compliance requirements)
- **Predicted solution**: Smarter and smarter VAD augmentations + faster models in cascade pipelines
- More computational budget will enable better turn-taking within traditional architecture

---

## Key Takeaways

1. **The Problem**: Voice AI interruptions happen because current systems use simple VAD (silence detection) rather than predictive, context-aware turn-taking
2. **The Gap**: Humans use complex, multi-stage prediction involving semantics, syntax, prosody, and visual cues; AI currently just detects speech vs. silence
3. **The Solutions**: Three emerging approaches - semantic augmentation, acoustic feature analysis, and full-duplex models
4. **Best Practices**: If building voice AI agents, implement semantic/acoustic VAD augmentation (LiveKit, Daily, AssemblyAI, Kyutai all offer solutions)
5. **The Future**: Likely evolution toward smarter VAD augmentations in cascade architectures rather than pure full-duplex models
6. **Current State**: Problem remains unsolved - all approaches still have limitations and none have perfected natural turn-taking

---

**Talk Duration**: ~19 minutes
**Speaker**: Dr. Tom Shapland, LiveKit
**Event**: AI Engineer Conference
