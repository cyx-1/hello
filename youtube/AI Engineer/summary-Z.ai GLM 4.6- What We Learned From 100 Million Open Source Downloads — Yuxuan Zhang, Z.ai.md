# Z.ai GLM 4.6: What We Learned From 100 Million Open Source Downloads — Yuxuan Zhang, Z.ai

**Video URL:** https://www.youtube.com/watch?v=m6MF1OR_9kM

---

## Executive Summary

Yuxuan Zhang from Z.ai presents the GLM 4.6 model series, Z.ai's latest flagship open-source language model that has achieved competitive performance with commercial models. The presentation covers Z.ai's journey from 2022 to reaching 100 million downloads across 65+ models, with GLM 4.6 ranking #1 on LM Arena alongside GPT-4o and Claude Opus 4.5. The talk dives deep into training methodologies including a multi-stage pre-training approach (15 trillion general tokens + 7 trillion reasoning tokens), long-context training up to 128K-200K tokens, and their custom reinforcement learning framework "Slide." Key innovations include single-stage RL at 64K tokens, token-wise loss computation for code, and curriculum learning. The presentation also covers GLM 4.5-V for multimodal understanding and deployment options through open-source frameworks and Z.ai's platform.

---

## Main Topics

### [Introduction to GLM Series and Open Source Journey](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=0s)
- Z.ai has been committed to open source since 2022, starting with GLM-130B
- Released 65+ models across different domains: language (GLM series), vision understanding (CogVLM/GLM-V), image generation, and video generation
- Achieved 100 million downloads across platforms like Hugging Face and ModelScope
- 10,500+ community projects on GitHub using GLM or CogVideo models
- 2025 declared as their "open source year" with significant model releases

### [GLM 4.6 Performance and Benchmarks](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=137s)
- GLM 4.6 is Z.ai's latest flagship model showing clear improvements over GLM 4.5
- Outperforms other open-source models like DeepSeek V3.2 in math and coding benchmarks
- Beats some commercial models like Claude Sonnet 4 on several benchmarks
- Tied for #1 on LM Arena with GPT-4o and Claude Opus 4.5 (only open-source model in top tier)
- Still a noticeable gap compared to Claude 4.5 Opus, but "getting close and close"

### [CCBench: Real-World Agent Coding Benchmark](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=216s)
- Z.ai built CCBench (Cloud Code Bench) v1.1 to test agent-style coding in real-world scenarios
- Platform based on Claude Code with 74 tasks covering frontend, internal tools, data analysis, and algorithms
- Added 22 hard coding tasks in v1.1
- Tests models like Claude Sonnet 4, GPT-4o, GLM 4.5, DeepSeek R1, and Llama 3.1
- Records full agent traces: planning, tool calls, code edits, execution
- GLM 4.6 achieved 68.6% win rate vs Claude Sonnet 4, significantly better than open-source baselines
- All benchmarks fully open-source for community use

### [GLM 4.6 Training Pipeline - General Pre-training](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=308s)
- Started with 15 trillion tokens of general-purpose data
- Includes web pages, books, Wikipedia, and multilingual content
- Context length: 4,000 tokens
- Goal: building a strong all-rounder base model

### [Reasoning Continue Training](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=343s)
- Added 7 trillion tokens of code and reasoning data on top of base
- Two main components:
  - High-quality open-source code repositories
  - Math, science, and programming content with step-by-step reasoning

### [Mid Training - Real Repository Understanding](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=368s)
- Trained on real GitHub repositories with multiple files, issues, and pull requests
- Differences from same project packed into long context sequences
- Teaches model to follow code files, understand change chains, and read real project structure end-to-end
- Context extended to 32,000 tokens
- Model can see key files of medium-sized repositories in one shot

### [Synthetic Reasoning Data](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=410s)
- Added 500 billion tokens of synthetic reasoning data
- Covers math, science, and algorithms with explicit thinking traces
- Lays groundwork for future agent behaviors: task breakdown, reflection on mistakes, long-chain reasoning

### [Long Context and Agent Training](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=431s)
- Used 100 billion tokens of long-context and agent data
- Context length pushed to 128,000 tokens for GLM 4.6 (200,000 for some variants)
- Model can handle full documents, whole code bases, and very long conversations
- Fed lots of agent trajectories: multi-step tool calls, search, code execution
- Improves both long-context capability and agent capability

### [Slide: Custom Reinforcement Learning Framework](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=471s)
- Open-sourced RL framework based on existing inference stack
- Different tasks need very different system designs:
  - **Short reasoning tasks** (math, code completion): Coupled architecture with average throughput - train and inference on same GPU, next batch immediately samples from latest policy
  - **Agent tasks** (software engineering with many steps): Decoupled asynchronous mode - rollout workers talk directly to real environments, generate trajectories, write to buffer; training consumes data at own pace, periodically pushes new weights
- Prevents slow tasks from dragging down GPU utilization
- Supports both synchronous and asynchronous modes flexibly

### [RL Optimization Techniques](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=631s)
- Main training chain runs in FP16 for stability
- After each policy update, performs blockwise FP8 quantization on latest weights
- Sends FP8 version for rollout/data generation (most expensive part)
- Training keeps BF16 precision for accuracy
- Gets benefits of both accuracy and speed

### [Two-Stage Curriculum Learning](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=663s)
- Don't use fixed dataset from start to finish
- Stage 1: Medium difficulty problems - rewards have variance, gradients are meaningful
- Stage 2: Switch to extremely hard problems once model gets stronger
- With 512 samples, can still occasionally get correct solutions
- Demonstrated superior performance compared to staying with medium difficulty throughout

### [Single-Stage RL at 64K Tokens](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=714s)
- Previous multi-stage approaches: 16K → 32K → 48K → 64K tokens
- Z.ai found this causes models to "forget" long-context ability
- Direct training at 64,000 tokens in one single stage clearly outperforms multi-stage approach
- Final 64K stage in multi-stage can't fully recover the lost capability

### [Token-Wise Loss for Code](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=778s)
- Compared two loss computation methods:
  - Classic sequence-wise loss (one loss value per sequence)
  - Token-wise loss (average over tokens instead of sequences)
- Token-wise version converges faster and more steadily
- Reduces chances of generating very short, templated answers just to get rewards

### [Data Quality Over Quantity for Scientific Reasoning](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=810s)
- Tested RL on GPQA (scientific reasoning benchmark)
- Small, expert-verified, high-quality multiple-choice questions significantly outperformed mixed-quality data
- Message: "For scientific reasoning, data quality really matters more than raw size"

### [GLM 4.5-V: Multimodal Understanding](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=849s)
- Supports both image and video understanding
- Latest visual understanding model with strong grounding capabilities
- Shows clear advantages over other open-source models released around the same time
- Architecture: Vision Transformer encoder → MLP projector → GLM 4.5 base model
- Keeps visual input as original as possible: native resolution and aspect ratio (no forcing to fixed square)
- Important for screenshots, long vertical images, PowerPoint slides

### [Video Understanding with Temporal Tokens](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=912s)
- Inserts time index tokens after each frame
- Tells model "this is frame 1, this is frame 2," etc.
- Helps understand temporal order and sequence
- Crucial for action understanding and step-by-step procedures

### [GUI Agent Capabilities](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=935s)
- Method researched in CogAgent now supported on GLM 4.5-V
- Can control computers, websites, browsers using mouse, keyboard, and touch interactions
- Works across browser, computer, and mobile environments

### [Deployment Options](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=962s)
- **Open-source weights:** Available on release day with vLLM and SGLang integration ready
- Third-party frameworks: LLaMA Factory, MS Swift
- **Z.ai Platform:** z.ai website for direct use (writing code, generating PowerPoints, etc.)
- Demo: Google search agent built with one command
- **GLM Coding Plan:** Connects GLM with tools and plugins like Claude Code and other development tools
- Demo video showing how to replace model in Claude Code with GLM 4.6

### [Community and Resources](https://www.youtube.com/watch?v=m6MF1OR_9kM&t=1111s)
- Regular community events (online and offline) after each model release
- AMAs on Reddit
- Offline tech-sharing sessions
- Important links:
  - Try models: z.ai website and API
  - Technical reports: GLM 4.6 and GLM 4.5-V papers
  - Community: Discord server
  - GitHub: Open-source models with deployment guides

---

## Key Takeaways

1. **Scale and Impact:** Z.ai has built a significant open-source AI ecosystem with 100M+ downloads across 65+ models
2. **Competitive Performance:** GLM 4.6 achieves top-tier performance, ranking #1 on LM Arena alongside GPT-4o and Claude Opus 4.5
3. **Training Innovation:** Multi-stage approach combining 15T general tokens + 7T reasoning tokens + 500B synthetic data + 100B agent data
4. **Long Context Mastery:** Successfully trained models up to 128K-200K context length through single-stage RL
5. **Custom Infrastructure:** "Slide" framework flexibly handles both short reasoning tasks and complex agent workflows
6. **Quality > Quantity:** For scientific reasoning, small high-quality datasets outperform larger mixed-quality data
7. **Real-World Testing:** CCBench provides agent-style coding evaluation on real-world tasks, not just isolated problems
8. **Multimodal Capabilities:** GLM 4.5-V supports images/videos with native resolution, temporal understanding, and GUI control
9. **Accessibility:** Models available via open-source weights, cloud platform, and easy integration with existing tools
10. **Community First:** Strong commitment to open source with regular events, documentation, and third-party framework support
