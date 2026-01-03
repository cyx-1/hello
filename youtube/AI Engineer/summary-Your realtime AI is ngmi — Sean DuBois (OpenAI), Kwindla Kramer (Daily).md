# Your realtime AI is ngmi — Sean DuBois (OpenAI), Kwindla Kramer (Daily)

**Video URL:** https://www.youtube.com/watch?v=E71YtNbCFXY

---

## Executive Summary

Sean DuBois from OpenAI and Kwindla Kramer from Daily present a comprehensive guide on building fast, natural voice AI experiences. The talk centers on a critical thesis: if you're building real-time voice AI and using websockets instead of WebRTC for edge-to-cloud audio, your application is "not going to make it" (ngmi). They explain why latency is the make-or-break factor for voice AI, demonstrate the technical superiority of WebRTC over websockets for real-time audio, and showcase practical applications including Squabbert (a Raspberry Pi-based voice agent) and a bilingual language learning app for children. The presentation emphasizes that we're in the early days of voice AI (analogous to 2007 in mobile), making this knowledge crucial for developers building the next generation of voice interfaces.

---

## Topics & Key Points

### [Introduction & Latency Fundamentals](https://www.youtube.com/watch?v=E71YtNbCFXY&t=0s)

**Key Points:**
- Sean DuBois works on WebRTC at OpenAI (real-time API, 1-800-CHATGPT)
- Kwindla Kramer works at Daily on real-time infrastructure and Pipecat (open source voice agent framework)
- **Latency is everything** in voice AI - nothing else matters if response times are too slow
- Natural human conversation: ~500ms response time feels natural
- Voice-to-voice latency over 1 second leads to low completion rates, low NPS scores, and hang-ups
- Voice-to-voice latency = time between when human stops talking and first audio response from LLM

### [Latency Breakdown in Real Applications](https://www.youtube.com/watch?v=E71YtNbCFXY&t=167s)

**Key Points:**
- Example: Real voice AI app in web browser on macOS talking to cloud-based Pipecat agent
- Voice latency just under 1 second - "good, but not great"
- Can optimize further but involves trade-offs (lower quality or higher cost)
- **Biggest mistake:** Using the wrong network protocol (websockets instead of WebRTC)
- Other latency killers: slower LLMs, network issues, **Bluetooth** (especially problematic)

### [WebRTC vs Websockets - The Critical Comparison](https://www.youtube.com/watch?v=E71YtNbCFXY&t=212s)

**Key Points:**
- **Websockets:**
  - Great for prototyping across platforms
  - Easy to implement
  - Good for server-to-server connections
  - Good for small amounts of structured data
  - **Problem:** Uses TCP, which guarantees in-order delivery - wrong for real-time audio

- **WebRTC:**
  - Purpose-built for high-quality, low-latency audio/video
  - Essential for edge-to-cloud real-time streams
  - More complex but specialized for the use case
  - **Key advantage:** Handles packet loss gracefully without blocking

**TL;DR:** Use websockets for server-to-server and structured data. Use WebRTC for audio/video streams from web apps or native apps to the cloud.

### [Why TCP/Websockets Fail for Real-Time Audio](https://www.youtube.com/watch?v=E71YtNbCFXY&t=301s)

**Key Points:**
- Websockets use TCP, which guarantees in-order packet delivery
- TCP keeps retrying to send packets until acknowledged or connection times out
- Perfect for web requests, **terrible for conversational latency**
- In real-time audio, you don't care about packets from a second ago
- Packet loss with websockets causes audio glitchiness, high latency, or unexpected disconnections
- **Real-world impact:** 10-15% of network connections will experience problems with websockets

### [WebRTC's Technical Advantages](https://www.youtube.com/watch?v=E71YtNbCFXY&t=362s)

**Key Points:**
- Sends packets as fast as possible, ignores packets that miss the tight latency budget
- "Super fast, best effort networking"
- Even if WebRTC only solved the TCP problem, it would be worth using
- **You literally cannot implement this on top of TCP/websockets**
- Additional built-in features WebRTC provides:
  - Audio resampling
  - Packetization
  - Bandwidth estimation (networks constantly change)
  - Standard APIs for stats and observability
- Code comparison: WebRTC code is much simpler than equivalent websockets implementation
- OpenAI's real-time API offers both options for developers

### [Live Demo - Squabbert the Voice Agent](https://www.youtube.com/watch?v=E71YtNbCFXY&t=618s)

**Key Points:**
- Squabbert: Raspberry Pi-based voice agent named by builder's daughter Ella
- Tech stack: MLX Whisper, Gemma 3, custom logic sampler
- Unique capability: Can count syllables (something large cloud LLMs struggle with)
- Demonstrated generating poems with two-syllable words only
- **Connection architecture:** Peer-to-peer WebRTC from Raspberry Pi directly to laptop over local network (serverless)
- Shows flexibility: local connections, cloud servers, or multi-party via Pipecat

### [WebRTC Use Cases & Platform Vision](https://www.youtube.com/watch?v=E71YtNbCFXY&t=468s)

**Key Points:**
- WebRTC is already ubiquitous: Facebook Messenger, WhatsApp, Zoom, Discord
- Advanced use cases: remote surgery, vehicle teleoperation
- WebRTC = "standard language of the real-time world"
- **Voice as the next platform shift:** We're in "late 2007" - have the first iPhone but haven't invented "pull to refresh" yet
- Voice = "bicycle for the mind" - adds new modality beyond eyes and hands
- Enables computing in situations where hands aren't available
- Small devices can access powerful cloud computing remotely

### [Real-World Application - Bilingual Language Learning](https://www.youtube.com/watch?v=E71YtNbCFXY&t=813s)

**Key Points:**
- Built by Yashin, a non-technical mom of two bilingual children
- Problem: Raising bilingual kids is expensive, time-consuming, feels like a chore
- Solution: Voice AI to make language education natural and fun
- Demonstrated teaching Mandarin with natural conversation
- **Key insight:** With a little guidance, non-programmers can build voice AI applications
- Already has group of parent testers eager to try it
- Represents democratization of voice AI development

### [Call to Action & Resources](https://www.youtube.com/watch?v=E71YtNbCFXY&t=913s)

**Key Points:**
- Vision: Make voice AI accessible to anyone with ideas, regardless of programming experience
- Pipecat (open source voice agent framework) and other tools making development easier
- Sean's book on WebRTC available in conference bags
- Community support available on Discord, Twitter, LinkedIn
- "We're here to support you" - whether you're experienced or just getting started

---

## Technical Takeaways

1. **Protocol Selection is Critical:** WebRTC for edge-to-cloud audio is non-negotiable for production applications
2. **Latency Budget:** Target under 500ms for natural feel, must stay under 1 second
3. **TCP vs UDP:** Real-time audio needs UDP-based protocols (WebRTC) that can drop packets, not TCP's guaranteed delivery
4. **Platform Flexibility:** WebRTC works across web, iOS, Android, embedded devices with consistent performance
5. **Development Complexity Trade-off:** WebRTC is more complex to implement but handles crucial details (resampling, bandwidth estimation, packet management) automatically

---

## Inspirational Quotes

- "Your realtime AI is ngmi" - If you're using websockets for edge-to-cloud audio
- "We are in late 2007 now. We have the first iPhones, but we haven't yet invented pull to refresh."
- "Voice is going to be the core building block of the next generation of UIs for the generative AI era."
- "Voice is the next bicycle for the mind."
- "If we can make this easy enough, people that have really innovative, inspirational ideas can go and do stuff themselves."
