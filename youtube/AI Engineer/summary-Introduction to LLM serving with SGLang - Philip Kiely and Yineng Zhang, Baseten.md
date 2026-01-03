# Introduction to LLM serving with SGLang - Philip Kiely and Yineng Zhang, Baseten

**Video URL:** https://www.youtube.com/watch?v=Ahtaha9fEM0

---

## Executive Summary

This workshop provides a hands-on introduction to SGLang (Structured Generation Language), a high-performance open-source framework for serving large language models (LLMs) and vision models. Philip Kiely (Developer Advocate at Baseten) and Yineng Zhang (Co-developer of SGLang) guide participants through deploying models with SGLang, optimizing performance using CUDA graphs, implementing Eagle 3 speculative decoding, and contributing to the open-source community. The workshop demonstrates practical techniques for improving model serving performance and highlights SGLang's rapid growth from a research paper to a production-ready framework with 15,000 GitHub stars in just 18 months.

---

## Main Topics

### 1. Introduction to SGLang
**[00:16 - 04:15](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=16s)**

Philip Kiely introduces the workshop and SGLang framework:
- **What is SGLang**: An open-source fast serving framework for LLMs and vision models, typically used alongside VLLM or TensorRT-LLM
- **Why SGLang**:
  - Excellent performance on various GPUs
  - Production-ready out of the box
  - Day-zero support for new model releases (Qwen, DeepSeek)
  - Strong open-source community and ethos
- **Who uses it**: Baseten, xAI (for Grok models), various inference providers, cloud providers, research labs, and product companies like Cursor
- **Rapid growth**: From arxiv paper (December 2023) to 15,000 GitHub stars in just 18 months

**Key Quote:** "If something is broken in SGLang, if you don't like something, you can fix it. Which is a pretty huge advantage."

### 2. Team Introduction and History
**[04:15 - 06:00](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=255s)**

Yineng Zhang shares his background:
- Co-developer of SGLang project
- Software engineer at Baseten (previously at ByteDance working on click-through rate ranking)
- Co-maintainer and team member at LMSYS (creators of Chatbot Arena, recently funded $100M by A16Z)
- Works closely with Flash Infer project, which SGLang uses heavily for attention kernels and sampling

### 3. Workshop Setup and First Deployment
**[06:00 - 12:30](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=360s)**

Participants set up their environment:
- Using **Truss** to package SGLang for deployment on Baseten
- Working with **L4 GPUs** (cheap, abundant, FP8 support)
- Deploying first model using YAML configuration
- Understanding SGLang as a server command with various flags
- Connecting to deployed models using OpenAI-compatible SDK

**Important Note:** The same principles work on H100, H200, and Blackwell GPUs

### 4. CUDA Graph Optimization Demo
**[13:00 - 24:00](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=780s)**

Yineng demonstrates performance optimization using CUDA graph max batch size:

**Initial Setup:**
- Model: Llama 3 8B Instruct
- Attention backend: FA3 (default)
- Default CUDA graph max batch size: **8** on L4

**The Problem:**
- When running requests exceed batch size of 8, CUDA graph is disabled
- Example: With 10 running requests, CUDA graph = false
- Performance: ~155 tokens/sec total (~15 tokens/sec per user)

**The Solution:**
- Set `--cuda-graph-max-batch-size 32`
- Allows CUDA graph to stay enabled for larger batches
- Critical for decoding performance

**Key Insight:** [https://www.youtube.com/watch?v=Ahtaha9fEM0&t=956s](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=956s) - "We want CUDA graph to be true during decode because this is very important for the decoding performance."

**Benchmarking Tool:**
- **LM Eval** (LMSYS Eval) - Industry standard benchmarking tool
- Simulates traffic to the running server
- Parameters shown:
  - Model name
  - URL (localhost:8000 for local setup)
  - Batch size: 128
  - Max generation tokens
  - Dataset: GSM8K
  - Limit: 0.15 (~200 prompts)

### 5. Eagle 3 Speculative Decoding
**[24:00 - 29:40](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=1440s)**

Introduction to Eagle 3, a new speculative decoding algorithm:

**What is Eagle 3:**
- Recently released speculative decoding framework
- Supported natively by SGLang
- Higher token acceptance rate compared to traditional draft-target approaches

**How it Differs:**
- Instead of using separate smaller model (like Llama 1B + Llama 8B)
- Eagle pulls multiple layers from the target model itself to build draft model
- Draft model is derived directly from target model

**Configuration Parameters:**
- `--speculative-algorithm eagle`
- `--speculative-draft-model-path` (path to Eagle draft model)
- `--speculative-num-steps` (depth of drafting, e.g., 0, 1, 3, 5, 7)
- `--speculative-eagle-topk` (top-k parameter, e.g., 1)
- `--speculative-num-draft-tokens` (max tokens, e.g., 4)

**Tuning Process:**
[https://www.youtube.com/watch?v=Ahtaha9fEM0&t=1636s](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=1636s) - SGLang provides benchmarking scripts in the playground:
- Script location: `benchmark/bench_speculative_decoding.py`
- Tests different combinations of batch sizes, steps, top-k, and token counts
- Outputs speed and acceptance rate metrics
- Use results to determine optimal parameters for production

**Critical Consideration:**
[https://www.youtube.com/watch?v=Ahtaha9fEM0&t=1733s](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=1733s) - "Speculation is very topic and content dependent. Benchmark on data representative of your actual inputs and outputs, or you'll end up with wrong parameters."

### 6. Community and Getting Involved
**[29:40 - 35:05](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=1780s)**

**Ways to Participate:**
- ⭐ Star the project on GitHub
- 📝 File issues and bug reports
- 💬 Join the Slack community: **slack.sglang.ai**
- 🐦 Follow [@SGLangAI](https://twitter.com/SGLangAI) on Twitter
- 👥 Attend online and in-person meetups

**Good First Issues:**
[https://www.youtube.com/watch?v=Ahtaha9fEM0&t=1908s](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=1908s) - GitHub has labeled **26 "good first issue"** and "help wanted" issues:
- Support for new VLM models
- Various feature requests
- Check the development roadmap

**Best Way to Start Contributing:**
1. Use SGLang in your own projects
2. Find issues or missing features
3. Raise a new issue or pick from existing ones
4. Submit pull requests

### 7. Codebase Overview
**[31:00 - 35:00](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=1860s)**

**Main Components:**

1. **SGLang Kernel Library (`sgl_kernel/`)**
   - CUDA kernel implementations
   - Attention, normalization, activation, Gemm operations
   - Contribution area for those familiar with CUDA programming

2. **SGLang Router (`sgl_router/`)**
   - Cache-aware routing
   - Supports the frontend DSL (Domain Specific Language)

3. **SGLang Runtime (`python/sglang/srt/`)**
   - Core inference runtime (Python)
   - Features:
     - Disaggregation support
     - Constrained decoding
     - Function calling
     - OpenAI-compatible server
     - Wide model support

**Model Support:**
- Reference implementation: Llama (in `models/` directory)
- Most popular open-source models have similar architectures
- Easy to add new models by modifying existing implementations

**Documentation Resources:**
- [Deep Wiki Page](https://github.com/sgl-project/sglang/wiki) - Comprehensive codebase tour
- Architecture diagrams showing how components work together

### 8. Q&A Highlights
**[36:44 - 40:00](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=2204s)**

**Why use SGLang over other runtimes?**
- Highly configurable and extensible
- Well-documented codebase
- Easy to contribute fixes back to the project
- Can unblock yourself instead of waiting for core developers
- Day-zero support for new models

**Security considerations:**
- Runtime choice doesn't significantly affect security protocols
- Package in containers with standard security practices
- Focus on least privilege and isolation at infrastructure level
- Same security considerations as VLLM or other runtimes

**On-premise deployment for DoD/financial applications:**
- SGLang enables full in-house product development
- No need to connect to external APIs like OpenAI
- Self-hosted models within secure subnets
- Meets compliance requirements (e.g., CMMC cybersecurity certifications)

---

## Technical Details

### Hardware Used in Demo
- **GPU**: L4 (cheap, abundant, FP8 support)
- Also works on: H100, H200, Blackwell (coming soon)

### Key Performance Flags
- `--cuda-graph-max-batch-size` - Critical for maintaining CUDA graph during decode
- `--speculative-algorithm` - Enable speculative decoding
- `--attention-backend` - Default is FA3 (Flash Attention 3)
- `--model` - Model path
- `--port` - Server port (default 8000)

### Installation
```bash
pip install sglang
# or install from source
```

### Launch Command Example
```bash
python -m sglang.launch_server \
  --model meta-llama/Llama-3-8B-Instruct \
  --attention-backend fa3 \
  --cuda-graph-max-batch-size 32
```

---

## Additional Resources

- **Workshop Repository**: Contains all examples, slides, and code
- **SGLang GitHub**: [sgl-project/sglang](https://github.com/sgl-project/sglang)
- **Community Slack**: slack.sglang.ai
- **Twitter**: [@SGLangAI](https://twitter.com/SGLangAI)
- **Baseten**: Hosting platform used in workshop (offers free GPUs for employees!)

---

## Related Announcements

**Happy Hour with Oxen AI:**
Mentioned at [35:31](https://www.youtube.com/watch?v=Ahtaha9fEM0&t=2131s) - Demo of fine-tuning Qwen 0.6B (less than 1B parameters) to beat GPT-4.1 on SQL generation benchmarks - a model that can run on a 3-year-old iPhone!

**Baseten Job Opportunities:**
Open roles for infrastructure and model performance engineering for those interested in CUDA programming and LLM inference optimization.

---

*Workshop conducted at AI Engineer conference*
*Speakers: Philip Kiely (Baseten Developer Advocate) and Yineng Zhang (SGLang Co-developer, Baseten Software Engineer)*
