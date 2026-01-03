# Vision AI in 2025 — Peter Robicheaux, Roboflow

**Video URL:** https://www.youtube.com/watch?v=IQc05eCvNYE

---

## Executive Summary

Peter Robicheaux, ML Lead at Roboflow, presents a critical analysis of the state of computer vision in 2025. He argues that while large language models have made tremendous progress, vision AI significantly lags behind - vision models "aren't smart" compared to their language counterparts. The core issues are: (1) vision evaluation benchmarks like ImageNet and COCO are saturated and don't measure true visual intelligence, (2) vision models don't leverage large-scale pre-training effectively the way LLMs do, and (3) vision-language models fail at basic visual perception tasks despite strong linguistic capabilities.

To address these gaps, Roboflow introduces two key contributions: **RF-DETR**, a real-time object detection model that leverages DINOv2's powerful pre-trained vision features, and **RF100VL**, a new benchmark dataset of 100 diverse object detection tasks designed to measure true visual intelligence across different domains, camera angles, and specialized imaging modalities. The results show that current vision-language models are "absolutely hopeless" at visual generalization, while specialized models fine-tuned on minimal data (10 examples per class) consistently outperform massive general-purpose VLMs.

---

## Main Topics

### 1. Why Computer Vision Matters and Its Current Limitations
[https://www.youtube.com/watch?v=IQc05eCvNYE&t=17s](https://www.youtube.com/watch?v=IQc05eCvNYE&t=17s)

**Key Points:**
- Systems that interact with the real world require vision as a primary input because the built world is organized around visual primitives
- The gap between human vision and computer vision is larger than the gap between human speech and computer speech
- Computer vision has distinct problems from LLMs: latency matters (need multiple frames per second), requires edge deployment, can't centralize computation without introducing too much latency
- Vision evals like ImageNet and COCO are saturated - they measure pattern matching rather than visual intelligence
- Vision models don't leverage big pre-training the way language models do

### 2. Evidence That Vision Models "Aren't Smart"
[https://www.youtube.com/watch?v=IQc05eCvNYE&t=204s](https://www.youtube.com/watch?v=IQc05eCvNYE&t=204s)

**Key Points:**
- Claude 3.5 and Claude 4 cannot tell time from a watch image - they just guess random times, even failing to identify the common 10:10 stock time
- Models have good conceptual understanding of what a watch is but are "hopeless" at identifying watch hand locations and numbers
- The MMVP dataset exposes this blindness: LLMs fail at obvious visual tasks like determining which direction a school bus is facing
- Models hallucinate details to support wrong conclusions, showing they lack actual visual perception
- This is evidence that even the most intelligent models "cannot see"

### 3. The CLIP vs DINOv2 Problem: Vision-Language Pre-training Failures
[https://www.youtube.com/watch?v=IQc05eCvNYE&t=245s](https://www.youtube.com/watch?v=IQc05eCvNYE&t=245s)

**Key Points:**
- MMVP dataset found image pairs that are close in CLIP space but far apart in DINOv2 space
- CLIP (vision-language model trained contrastively on captioned images) cannot discriminate between visually distinct images
- The problem: captions don't describe fine-grained visual details like dog pose or orientation, so the loss function can't distinguish these images
- DINOv2 (pure vision model, self-supervised) discovers rich visual features including object masks, segments, and even analogous parts across different objects (e.g., dog legs vs human legs)
- Vision-only pre-training works better for visual fidelity, but vision-language alignment remains an open problem

### 4. Why Transformers Beat CNNs for Vision: The Pre-training Advantage
[https://www.youtube.com/watch?v=IQc05eCvNYE&t=413s](https://www.youtube.com/watch?v=IQc05eCvNYE&t=413s)

**Key Points:**
- YOLOv8 (convolutional detector) gains only 0.2 mAP from Objects365 pre-training (1.6M images) - essentially no improvement
- LW-DETR (transformer-based detector) gains 5-7 mAP from the same pre-training - a "gigantic" improvement
- This mirrors the language world: transformers can leverage big pre-training effectively while CNNs cannot
- The vision world is "just now catching up" to this realization
- 1.6 million image pre-training is considered "large" in vision but would be a "tiny challenge dataset for undergrads" in the LLM world

### 5. Introducing RF-DETR: Leveraging DINOv2 for Real-Time Detection
[https://www.youtube.com/watch?v=IQc05eCvNYE&t=521s](https://www.youtube.com/watch?v=IQc05eCvNYE&t=521s)

**Key Points:**
- Roboflow's answer to the pre-training gap: RF-DETR uses DINOv2 pre-trained backbone in real-time object detection
- Swapped LW-DETR backbone with DINOv2 backbone
- Achieves decent improvements on COCO benchmark (second state-of-the-art, below DeFINE)
- More impressive results on RF100VL dataset showing strong domain adaptability
- COCO is "too easily solvable" - it measures bounding box precision rather than visual intelligence
- COCO has common classes (humans, coffee cups) that don't test a model's true understanding

### 6. RF100VL: A New Benchmark for Visual Intelligence
[https://www.youtube.com/watch?v=IQc05eCvNYE&t=597s](https://www.youtube.com/watch?v=IQc05eCvNYE&t=597s)

**Key Points:**
- Collection of 100 diverse object detection datasets from Roboflow Universe (750,000+ datasets available)
- Hand-curated for difficulty and community engagement
- Includes diverse camera poses (aerial, microscope, X-ray) uncommon in COCO
- Tests model's ability to understand different views and imaging domains
- Measures richness of learned features more comprehensively than COCO
- It's a vision-language benchmark requiring contextual understanding of class names
- Example: "block" must be understood as a volleyball action, "thunderbolt" as a cable defect type
- Broader class vocabulary tests world knowledge (e.g., detecting "fibrosis" vs just "dog" or "cat")

### 7. Vision-Language Models Fail at Visual Generalization
[https://www.youtube.com/watch?v=IQc05eCvNYE&t=780s](https://www.youtube.com/watch?v=IQc05eCvNYE&t=780s)

**Key Points:**
- YOLOv8 trained on just 10 examples per class outperforms Qwen2.5-VL 72B (state-of-the-art gigantic VLM)
- VLMs are "really good right now at generalizing out of distribution in the linguistic domain"
- VLMs are "absolutely hopeless when it comes to generalizing in the visual domain"
- RF-DETR with DINOv2 embeddings performs much better on RF100VL than models using Objects365 embeddings
- No current model can effectively leverage all three inputs: class names, visual examples, and annotator instructions

### 8. Benchmark Details and Model Performance
[https://www.youtube.com/watch?v=IQc05eCvNYE&t=901s](https://www.youtube.com/watch?v=IQc05eCvNYE&t=901s)

**Key Points:**
- Dataset publicly available at rf100vl.org and on Hugging Face
- Data comes from researchers using Roboflow's free platform who contribute back to open source
- Includes data from papers published in Nature and other prestigious venues
- Few-shot track: canonical 10-shot splits with class names, annotator instructions, and 10 visual examples per class
- Grounding DINO zero-shot: 19 mAP average (worse than YOLO V8 nano trained from scratch on 10 shots: 25 mAP)
- Grounding DINO fine-tuned with federated loss: highest performing model on the dataset
- Roboflow's strategy: free platform for researchers in exchange for open-sourcing their labeled data

---

## Key Takeaways

1. **Vision models lag significantly behind language models** in intelligence and ability to leverage pre-training
2. **Current benchmarks (ImageNet, COCO) are saturated** and don't measure true visual intelligence
3. **Vision-language pre-training (CLIP) fails at visual fidelity** while vision-only pre-training (DINOv2) succeeds
4. **Transformers are essential** for leveraging large-scale pre-training in vision (CNNs can't do this effectively)
5. **RF-DETR + DINOv2** demonstrates the value of strong visual embeddings for downstream tasks
6. **RF100VL provides a better benchmark** for visual intelligence across diverse domains, poses, and modalities
7. **VLMs are blind**: they excel at linguistic generalization but fail catastrophically at visual generalization
8. **The open question**: How to create vision features that are well-aligned with language features, usable by VLMs, and maintain visual fidelity

---

**Presentation Length:** ~17 minutes
**Dataset:** RF100VL available at https://rf100vl.org
**Model:** RF-DETR (leveraging DINOv2 backbone)
