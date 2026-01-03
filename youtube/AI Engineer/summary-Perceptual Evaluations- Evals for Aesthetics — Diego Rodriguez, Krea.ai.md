# Perceptual Evaluations: Evals for Aesthetics — Diego Rodriguez, Krea.ai

**Video URL:** https://www.youtube.com/watch?v=h5ItAJuB3Fc

---

## Executive Summary

Diego Rodriguez, co-founder of Krea.ai, presents a compelling talk about the challenges of evaluating AI-generated media when human perception and aesthetics matter. He demonstrates how current AI models, including GPT-4o, struggle with perceptual evaluation tasks that humans find trivial (like identifying a malformed AI-generated hand). The talk explores the deep connection between information theory, compression (JPEG, MP3), and human perception, arguing that traditional metrics (like FID scores) fail to capture aesthetic quality and subjective human preferences. Rodriguez advocates for training specialized perceptual classifiers that can understand aesthetic quality the way humans do, emphasizing that machine learning excels precisely at these subjective "you know it when you see it" evaluations.

---

## Main Topics

### 1. The Perceptual Evaluation Problem ([00:17](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=17s) - [02:00](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=120s))

**Key Points:**
- Diego introduces himself as co-founder of Krea.ai, a generative media/multimedia startup
- Demonstrates the failure of GPT-4o (O3) to evaluate a malformed AI-generated hand image
- The model "thought for 17 seconds," used Python/OpenCV analysis, and incorrectly assessed the image as "mostly natural"
- Humans instantly recognize the image as unnatural, highlighting a fundamental gap in AI perception
- The paradox: AI models are trained on human data, human preferences, yet fail at perceptual tasks
- This talk addresses questions about evaluations when human perception, opinion, and aesthetics are critical

### 2. Information Theory and Human Perception ([02:18](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=138s) - [06:00](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=360s))

**Key Points:**
- Claude Shannon's foundational work in information theory (originally "Mathematical Foundation for Communication Theory")
- Shannon's communication model: source → encoder → channel (with noise) → decoder → destination
- Parallels between classic information theory and modern neural networks (variational autoencoders)
- JPEG compression exploits human perception: humans are very sensitive to brightness but not to color
- The checkerboard illusion demonstrates perceptual limitations (squares A and B are the same color)
- JPEG workflow: RGB → YCbCr color space → downsample color channels → 50% less information, imperceptible to humans
- Same principle applies to MP3 (audio) and MP4 (video) - all exploit human perceptual limitations

### 3. The Compression Contagion Problem ([06:00](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=360s) - [07:00](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=420s))

**Key Points:**
- Personal revelation: coding compression algorithms and seeing the same image despite deleting information
- "Philosophers always tell you we are limited by our senses, but this is the first time I was seeing it"
- Critical question: If AI training data comes from the internet, and internet images are compressed, are we transferring human perceptual flaws to AI?
- The "contagion" of human limitations into AI systems through compressed training data

### 4. The Failure of Traditional Metrics ([07:00](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=420s) - [09:00](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=540s))

**Key Points:**
- FID (Fréchet Inception Distance) scores are standard metrics for evaluating diffusion models
- Example from "Clean FID" paper: adding JPEG artifacts dramatically worsens FID scores, yet images look perceptually the same to humans
- Question: Why use FID scores to evaluate generative AI if they don't match human perception?
- Current focus on "easy to measure" metrics: CLIP adherence, object counting, color accuracy
- Salvador Dalí's melting clocks example: metrics would fail this as "bad" (clocks don't look like that), but it's celebrated art
- Metrics miss the relativity and subjectivity of aesthetics - meaning that humans understand but algorithms don't capture
- The core business challenge: how to help creatives and artists express themselves if metrics don't capture aesthetic quality?

### 5. Predicting the Future of Perception ([09:12](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=552s) - [11:00](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=660s))

**Key Points:**
- Quote from Changloo (Mid Journey): "Predicting the car back when everything was horses wasn't that hard, but predicting the road system? That's hard."
- The real challenge isn't predicting the next innovation, but predicting how it changes everything else
- Applied to AI: maybe we won't even need to evaluate perceptual quality in the future
- Perhaps we need to stop thinking about traditional evaluation frameworks and imagine entirely new paradigms
- The question isn't just "how do we evaluate better?" but "should we even evaluate this way?"

### 6. Krea.ai's Approach to User-Driven Evaluation ([11:00](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=660s) - [13:30](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=810s))

**Key Points:**
- Krea.ai provides real-time image/video generation tools for creatives
- Users vote, rate, and provide feedback on generated outputs
- This creates valuable ground truth data about what users actually prefer
- Example: comparing two image generation methods (different samplers, models, etc.)
- Can collect thousands of user preferences to determine which approach users prefer
- Ground truth comes from actual user behavior, not synthetic metrics
- This data enables training better models aligned with real human preferences

### 7. Building Perceptual Evaluation Models ([13:30](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=810s) - [16:20](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=980s))

**Key Points:**
- Traditional image quality metrics (PSNR, SSIM, LPIPS) often fail perceptual tests
- Example: flipping an image upside down barely changes these metrics, yet clearly degrades quality
- Many traditional metrics were designed for video encoding compression, not generative AI evaluation
- The invitation: we can train classifiers/continuous classifiers to understand perceptual quality
- Show the model examples: "these five images are all good" despite having different artifacts (not just JPEG)
- Machine learning excels at subjective evaluations: "you'll know it when you see it"
- This is precisely where AI shines - learning patterns from opinions and preferences

### 8. Q&A Insights ([16:30](https://www.youtube.com/watch?v=h5ItAJuB3Fc&t=990s) onwards)

**Key Points:**
- Discussion about using VLMs (Vision-Language Models) as judges for perceptual evaluation
- Challenge: VLMs may hallucinate or provide inconsistent evaluations
- Importance of test-time compute and structured evaluation approaches
- The value of combining automated metrics with human feedback loops
- Need for domain-specific evaluation criteria (what works for one creative domain may not work for another)

---

## Key Takeaways

1. **Perception Gap**: Current state-of-the-art AI models fail at perceptual evaluation tasks that humans find trivial
2. **Compression Legacy**: Human perceptual limitations embedded in compression standards (JPEG, MP3) may be contaminating AI training data
3. **Metric Mismatch**: Traditional metrics (FID, PSNR, SSIM) don't align with human aesthetic preferences and subjective quality
4. **Subjective Excellence**: Machine learning excels at learning subjective patterns - we should leverage this for perceptual evaluation
5. **User-Driven Truth**: Real user preferences and behavior provide the most valuable ground truth for training perceptual models
6. **Paradigm Shift**: Instead of improving traditional evaluation methods, we may need entirely new frameworks for aesthetic evaluation

---

## Relevance

This talk is essential for anyone building generative AI systems for creative applications (image, video, audio generation), working on evaluation frameworks for subjective quality, or interested in the intersection of human perception, information theory, and machine learning. Rodriguez challenges fundamental assumptions about how we measure AI success in domains where aesthetics and human preference are paramount.
