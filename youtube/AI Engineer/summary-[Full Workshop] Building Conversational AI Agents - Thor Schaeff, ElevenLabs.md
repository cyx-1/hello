# [Full Workshop] Building Conversational AI Agents - Thor Schaeff, ElevenLabs

**Video URL:** https://www.youtube.com/watch?v=MPtCBaZn84A

---

## Executive Summary

This comprehensive workshop from ElevenLabs covers building multilingual conversational AI agents from the ground up. Thor Schaeff, Developer Experience Lead at ElevenLabs, walks through the complete architecture of voice AI systems including speech-to-text, LLM integration, and text-to-speech components, with live demonstrations of creating agents that can handle 31+ languages, perform function calling, and integrate with external systems. The session includes hands-on implementation guidance, Q&A addressing latency optimization, multi-agent orchestration, and safety considerations for production deployments.

---

## Main Topics

### [Introduction and Workshop Overview](https://www.youtube.com/watch?v=MPtCBaZn84A&t=16s)
- Workshop introduction and 11 Labs overview
- Team introductions: Thor (Developer Experience) and Paul
- Access to slides, resources, and free credits for attendees
- Audience engagement on target languages (Portuguese, Spanish, Hungarian, Mandarin, Hindi, Tamil)

**Key Points:**
- ElevenLabs offers credits for 3 months to workshop participants
- Follow @11LabsDevs on Twitter for API updates and developer-focused announcements
- Currently supports 31 languages in conversational AI, expanding to 99 with V3 multilingual models

### [ElevenLabs Product Ecosystem](https://www.youtube.com/watch?v=MPtCBaZn84A&t=321s)
- Fun demonstration of text-to-bark feature (April Fools launch that showcased sound effects model)
- Sound effects model capabilities for game development and multimedia
- 11 Labs sound board demo with drum machine functionality

**Key Points:**
- Sound effects model generates contextual audio beyond voice
- Text-to-bark was an April Fools joke but demonstrated real sound generation capabilities
- Use cases extend beyond conversation to gaming, video production, and multimedia

### [Conversational AI Architecture Overview](https://www.youtube.com/watch?v=MPtCBaZn84A&t=511s)
- Core pipeline: Speech-to-Text → LLM (Brain) → Text-to-Speech
- System tools: language detection, function calling, knowledge base integration
- Streaming architecture for minimal latency
- ElevenLabs focuses on audio components, partners with major LLM providers (GPT-4, Gemini, etc.)

**Key Points:**
- Entire pipeline is streaming to minimize response time
- Models are co-located in close geographic proximity to reduce latency
- Support for custom LLMs via OpenAI-compatible API endpoints
- Built-in RAG (Retrieval Augmented Generation) for knowledge base queries

### [Speech-to-Text (ASR) Model](https://www.youtube.com/watch?v=MPtCBaZn84A&t=660s)
- Benchmark-leading performance across 99 languages
- Word-level timestamps for precise synchronization
- Speaker diarization to identify different speakers
- Audio event tagging (coughing, laughing, etc.)
- Structured API responses

**Key Points:**
- Telegram bot demo for live transcription testing
- Robust performance even with background noise and poor audio quality
- Real-world demo with Trump press conference clip showing accurate transcription
- Free Telegram bot available for testing: forward audio clips for instant transcription

### [Text-to-Speech and Voice Library](https://www.youtube.com/watch?v=MPtCBaZn84A&t=1050s)
- Massive voice library with professional and custom voices
- Advanced filtering: language, accent, gender, age
- Voice marketplace with royalty payments (over $5M paid to voice actors)
- Professional voice cloning for brand consistency
- Multilingual voice support with accent preservation

**Key Points:**
- Voices can be filtered by specific accents (e.g., Brazilian Portuguese)
- Voice actors earn royalties when their voices are used
- Professional voice design services available
- Instant voice cloning from audio samples
- Can upload custom voices for brand-specific applications

### [Building a Multilingual Agent Demo](https://www.youtube.com/watch?v=MPtCBaZn84A&t=1263s)
- Live demonstration: Singapore conference agent supporting 4 official languages
- Agent automatically detects and switches languages mid-conversation
- Supports English, Mandarin Chinese, Malay, and Tamil
- Dashboard configuration for rapid agent setup
- Real-time language switching without explicit user commands

**Key Points:**
- Agent automatically detects language from user input
- Seamless switching between languages in single conversation
- No need to pre-configure or announce language preference
- 31 languages currently supported, expanding to 99 with V3 models
- Language detection is a built-in system tool

### [LLM Configuration and Integration](https://www.youtube.com/watch?v=MPtCBaZn84A&t=1320s)
- Support for major LLM providers (OpenAI, Anthropic, Google, etc.)
- Custom LLM integration via OpenAI-compatible endpoints
- Knowledge base upload (documents, websites)
- Built-in RAG with configurable context windows
- System prompt customization for agent behavior

**Key Points:**
- Choice of model impacts latency and cost trade-offs
- Can fine-tune custom models and deploy via Vertex AI or similar platforms
- Document upload supports PDFs, text files, and website scraping
- RAG automatically retrieves relevant context without bloating prompt
- Knowledge base is searchable and version-controlled

### [Function Calling and Tools](https://www.youtube.com/watch?v=MPtCBaZn84A&t=1367s)
- Standard function calling support for modern LLMs
- Server-side tools via webhook integration
- Client-side tools for local execution
- Example integrations: Cal.com for scheduling, CRM systems
- Tool reliability depends on LLM capability

**Key Points:**
- Define tools with JSON schema for parameters
- Agent determines when to invoke tools based on conversation context
- Webhooks allow integration with any external API
- Example: booking calendar appointments through conversational interface
- Some models handle function calling more reliably than others

### [Hands-on Workshop Session](https://www.youtube.com/watch?v=MPtCBaZn84A&t=1680s)
- Guided setup: Creating accounts and first agent
- Dashboard tour and configuration walkthrough
- Support agent template demonstration
- Voice selection and customization
- Testing agents in real-time

**Key Points:**
- Free tier available for getting started
- Template agents accelerate development (support, sales, etc.)
- Web-based testing interface for rapid iteration
- Can test via phone calls using dedicated numbers
- SDKs available for JavaScript, Python, React, and more

### [Advanced Features and Configuration](https://www.youtube.com/watch?v=MPtCBaZn84A&t=1590s)
- Examples repository with Next.js, Python implementations
- Raspberry Pi support for hardware deployments
- API-based agent configuration for marketplace builders
- MCP (Model Context Protocol) server for Claude Desktop integration
- Natural language agent setup through Claude Desktop

**Key Points:**
- Full API for programmatic agent creation and management
- Integration with Claude Desktop via MCP server
- Can manage agents entirely through natural language commands
- Hardware deployment examples for edge devices
- Documentation includes code examples and quickstart guides

### [Multi-Agent Orchestration](https://www.youtube.com/watch?v=MPtCBaZn84A&t=2266s)
- Agent-to-agent transfer capabilities
- Different agents for different use cases
- Silent transfers when voice remains consistent
- Team-based agent ownership and management
- Orchestration layer routes to appropriate specialized agent

**Key Points:**
- Avoid confusion by splitting complex workflows into focused agents
- Each agent can use different LLMs optimized for specific tasks
- Users don't notice transfers if voice stays the same
- Enables team collaboration on agent development
- System tool manages transfer logic automatically

### [Latency Optimization Strategies](https://www.youtube.com/watch?v=MPtCBaZn84A&t=1980s)
- Model selection: smaller/faster models (Gemini Flash, GPT-4 Mini) vs. larger models
- Minimize knowledge base size and RAG queries
- Reduce function calling complexity
- Optimize system prompts for conciseness
- Consider trade-offs between quality and response time

**Key Points:**
- Latency primarily driven by LLM processing time
- Streaming architecture helps but LLM is bottleneck
- Gemini Flash and GPT-4 Mini offer good balance
- Simple prompts and focused knowledge bases improve speed
- For high-volume calls, consider smaller specialized models

### [Handling Complex RAG and Long-Running Tasks](https://www.youtube.com/watch?v=MPtCBaZn84A&t=2340s)
- Challenge: keeping conversation flowing during slow backend operations
- Strategies: queue-based processing, background task execution
- Potential solution: WebSocket injection of context updates
- Filler responses while waiting for data retrieval
- Balance between user experience and comprehensive answers

**Key Points:**
- Large knowledge bases can slow response times
- Consider async processing for complex queries
- Agent can acknowledge request while processing in background
- WebSocket events may allow injecting results mid-conversation
- Trade-off between speed and thoroughness in enterprise scenarios

### [Multilingual Mixed-Language Queries](https://www.youtube.com/watch?v=MPtCBaZn84A&t=2640s)
- Live test: handling questions with mixed languages
- Example: "Explain Schadenfreude in Chinese"
- Agent successfully processes mixed-language input
- Responds in requested target language
- Language model determines appropriate response language

**Key Points:**
- Agents can understand code-switching and mixed queries
- Target language detection based on explicit request or context
- LLM handles translation and language routing
- Useful for bilingual or multilingual user bases
- No special configuration needed for mixed-language support

### [Safety, Moderation, and Fraud Prevention](https://www.youtube.com/watch?v=MPtCBaZn84A&t=2940s)
- Dedicated safety page: 11labs.io/safety
- Live moderation for voice library content
- Voice actors can specify forbidden terms/content
- Audio watermarking to trace generated content back to accounts
- Account banning for fraudulent activity

**Key Points:**
- Every generated audio includes invisible watermark with account identifier
- Moderation prevents misuse of published voices
- Safety features developed in parallel with new capabilities
- Can trace fraudulent content to source account
- Voice library publishers have control over usage restrictions

### [Pronunciation Dictionaries and Customization](https://www.youtube.com/watch?v=MPtCBaZn84A&t=3480s)
- Phonetic alphabet support for custom pronunciations
- Useful for brand names, acronyms, technical terms
- Example: ensuring "tomato" vs "tomato" pronunciation
- Text-to-speech can be fine-tuned with pronunciation guides
- Limited support for speech-to-text customization (workaround via LLM normalization)

**Key Points:**
- Pronunciation dictionaries solve brand name issues
- Phone alphabet formatting for precise control
- Helps with industry-specific terminology
- For speech-to-text, LLM can normalize transcripts in system prompt
- Enterprise use cases often need custom dictionaries (e.g., SAP's "Joule" vs "jewel")

### [API Integration and Developer Resources](https://www.youtube.com/watch?v=MPtCBaZn84A&t=1560s)
- Comprehensive documentation at docs.elevenlabs.io
- Client libraries for multiple languages
- WebSocket API for streaming conversations
- RESTful API for agent management
- Example repositories and starter templates

**Key Points:**
- SDKs handle complexity of WebSocket management
- Examples cover common frameworks (Next.js, React, Python)
- API allows full programmatic control
- Webhooks for event notifications
- Active developer community and support channels

### [Q&A and Workshop Wrap-up](https://www.youtube.com/watch?v=MPtCBaZn84A&t=2820s)
- Open questions from participants
- Live troubleshooting and demos
- Discussion of edge cases and advanced scenarios
- Invitation to continue building and provide feedback
- Offers for follow-up support and guidance

**Key Points:**
- Team available for one-on-one support during workshop
- Encouraged experimentation with free tier
- Credits available via form submission
- Documentation and examples for continued learning
- Community feedback actively incorporated into product development

---

## Key Takeaways

1. **Complete Voice AI Pipeline**: ElevenLabs provides end-to-end solution from speech recognition through intelligent responses to natural-sounding voice synthesis across 31+ languages

2. **Multilingual by Default**: Agents automatically detect and switch between languages without configuration, making global deployment straightforward

3. **Flexible Architecture**: Support for any OpenAI-compatible LLM enables custom models, fine-tuning, and optimization for specific use cases

4. **Production-Ready Features**: Built-in safety, moderation, watermarking, RAG, function calling, and multi-agent orchestration for enterprise deployments

5. **Developer-Focused**: Comprehensive SDKs, documentation, examples, and API-first design enable rapid integration into existing applications

6. **Latency Optimization**: Success requires balancing model selection, knowledge base size, and prompt complexity against response time requirements

7. **Voice Marketplace**: Extensive library of professional voices with royalty system enables finding perfect voice for any brand or use case

8. **Active Development**: Regular launches of new capabilities (V3 multilingual models, additional languages, improved safety) with strong developer community engagement

---

**Workshop Duration:** ~62 minutes
**Format:** Presentation + Live Demos + Hands-on Building + Q&A
**Skill Level:** Beginner to Intermediate
**Prerequisites:** Basic understanding of APIs, LLMs, and conversational AI concepts
