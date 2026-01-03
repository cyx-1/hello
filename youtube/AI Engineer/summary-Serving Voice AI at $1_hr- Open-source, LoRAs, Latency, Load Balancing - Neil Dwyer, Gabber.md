# Serving Voice AI at $1/hr: Open-source, LoRAs, Latency, Load Balancing

**Video URL:** https://www.youtube.com/watch?v=rD23-VZZHOo

**Channel:** AI Engineer

---

## Executive Summary

Neil Dwyer, CTO of Gabber, presents how his team built cost-effective real-time voice AI infrastructure using open-source tools, achieving $1/hour costs on L40S GPUs. The talk covers their journey from relying on expensive voice platforms ($5/hour) to self-hosting Orpheus voice models with LoRA fine-tuning, solving latency challenges, and implementing efficient load balancing. Key technical innovations include fine-tuning away "head of line silence" to reduce latency by 500ms, using vLLM's FP8 quantization for 2x speedup, and implementing consistent hash ring load balancing for multi-tenant LoRA serving.

---

## Topics

### [Introduction and Background](https://www.youtube.com/watch?v=rD23-VZZHOo&t=0s)
**[00:00 - 02:00]**

- Neil Dwyer's background in real-time media (Bibo/Amazon, LiveKit)
- Built ML pipeline for game streaming, worked on LiveKit agents platform
- Co-founded Gabber with brother Jack - focusing on real-time AI personas for consumer apps
- Key difference: targeting consumer use cases vs. enterprise (call centers, AI SDR)

### [Why Consumer Voice AI and Cost Challenges](https://www.youtube.com/watch?v=rD23-VZZHOo&t=120s)
**[02:00 - 04:00]**

- Vision: Real-time synchronous AI experiences will be as ubiquitous as websites in 2-5 years
- Use cases: AI girlfriends, NPCs, therapists, personal trainers, toys for kids
- AI girlfriends emerged first because users pay credits (can justify $5/hour costs)
- Most consumer apps need costs "pretty close to free" - existing platforms at $5/hour won't work
- Realization: Must self-host voice models on own GPUs to achieve vision

### [Orpheus: The Game-Changing Voice Model](https://www.youtube.com/watch?v=rD23-VZZHOo&t=240s)
**[04:00 - 06:00]**

- Before Orpheus: No good open-source real-time streaming voice models
- Orpheus based on Llama 3B, pre-trained on 100K hours of voice + text data
- Outputs Snack audio codec tokens at 24kHz (85 tokens/second = 1 second audio)
- Requires 90-100 tokens/sec throughput to maintain real-time performance
- Company trajectory: "Before Orpheus and after Orpheus"
- Immediately deployed on H100, went viral with Jack's tweet

### [Voice Cloning with LoRA Fine-Tuning](https://www.youtube.com/watch?v=rD23-VZZHOo&t=360s)
**[06:00 - 08:00]**

- Consumer use cases require emotive, high-fidelity voice cloning
- One-shot cloning doesn't work well (needs 1M+ hours training for zero-shot)
- Solution: Low-Rank Adaptation (LoRA) fine-tuning
- Example: Cloned Jack's voice with rank 16, alpha 32 on all projections
- Used only 10 minutes of data (ideally 30+ minutes), trained 5 epochs
- Result: Emotionally expressive, picks up on language cues despite overfit

### [Latency Optimization: Four Critical Factors](https://www.youtube.com/watch?v=rD23-VZZHOo&t=460s)
**[07:40 - 10:00]**

Four factors affecting latency:
1. Time to first token
2. Tokens per second throughput
3. Network latency
4. **Head of line silence** (biggest issue)

**Latency budget concept:**
- Human speaks → endpoint detection → snooze period (1.5s threshold)
- Generate LLM response → produce audio during snooze window
- Goal: First audio packet within snooze period = "in the money"
- Above 1.5s sounds bad; at or below is acceptable

### [Solving Head of Line Silence Problem](https://www.youtube.com/watch?v=rD23-VZZHOo&t=480s)
**[08:00 - 10:00]**

- Orpheus model had 600ms silence at beginning (voice actors pausing before reading)
- At 100 tokens/sec on L40S, 600ms = ~50 wasted tokens = half second latency
- Even filtering silence only saves 10% (barely faster than real-time)
- **Solution: Fine-tune the silence away**
- Customer LoRA clones achieved ~100ms P50 latency (500ms improvement)
- Critical for giving LLM more time to generate tokens within latency budget

### [Infrastructure: vLLM and Batch Inference](https://www.youtube.com/watch?v=rD23-VZZHOo&t=600s)
**[10:55 - 12:30]**

Requirements for scrappy team:
- Batch inference to save money
- Multiple LoRAs in same batch on same GPU
- One load balancer for multiple models/languages
- "Black box" solution that just works

**vLLM to the rescue:**
- Supports batch inference with LoRAs simultaneously
- FP16 model slower than real-time on L40S (worked on H100)
- FP8 dynamic quantization: zero-effort, automatic scaling
- Result: 105 tokens/sec (base voices), 95 tokens/sec (LoRA voices) at batch size 10
- "Well in the money" on margins

### [Load Balancing with Consistent Hash Ring](https://www.youtube.com/watch?v=rD23-VZZHOo&t=750s)
**[12:30 - 15:00]**

**Why load balancing matters:**
- LoRAs are 100-200MB each
- Need sticky sessions to hit GPU with LoRA already in memory
- Support streaming input (LLM may not finish before audio generation)
- Support arbitrarily long generation (storytelling use cases)
- Must stay on same GPU for entire session

**Consistent hash ring solution:**
- Hash servers multiple times as "virtual nodes" around ring
- Hash incoming request with same algorithm
- Pick nearest server on ring
- Advantages: Minimal rebalancing when servers added/removed
- Easy scaling for popular LoRAs: just add to more servers

**Architecture:**
- WebRTC backend → WebSockets → GPUs → Redis
- Session starts → connects any GPU → asks Redis for correct GPU → proxies via TCP
- Low latency within same data center private network

### [Conclusion and Acknowledgments](https://www.youtube.com/watch?v=rD23-VZZHOo&t=900s)
**[15:00 - 16:01]**

**Key takeaway:** Scrappy teams can self-host voice models and build infrastructure
- Open source enables consumer voice AI use cases
- Will unlock ton of cool applications

**Shoutouts:**
- Swix (supporter, co-organizer)
- Canopy Labs (created Orpheus)
- Open source ecosystem: Llama, Snack codec
- LiveKit (WebRTC infrastructure foundation)
- vLLM (inference optimization)

---

## Key Technical Achievements

- **Cost reduction:** From $5/hour (third-party) to ~$1/hour (self-hosted L40S)
- **Latency improvement:** 600ms → 100ms P50 via LoRA fine-tuning
- **Throughput:** 95-105 tokens/sec with batch size 10 on L40S (FP8 quantization)
- **Multi-tenancy:** Multiple LoRAs in single batch with consistent hash ring routing

## Technology Stack

- **Voice Model:** Orpheus (Llama 3B base, 100K hours voice training)
- **Audio Codec:** Snack (24kHz, 85 tokens/second)
- **Inference:** vLLM with FP8 dynamic quantization
- **Fine-tuning:** LoRA (rank 16, alpha 32)
- **GPU:** L40S machines
- **Real-time:** WebRTC (LiveKit-based)
- **Load Balancing:** Consistent hash ring + Redis
