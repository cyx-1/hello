# Waymo's EMMA: Teaching Cars to Think - Summary

**Video URL:** https://www.youtube.com/watch?v=iS9YFW28XyM
**Speaker:** Jyh Jing Hwang, Waymo
**Channel:** AI Engineer

---

## Executive Summary

This talk presents EMMA (End-to-end Multimodal Model for Autonomous Driving), Waymo's research into leveraging foundation models like Gemini for autonomous driving. The speaker traces the evolution from early 1980s neural networks to today's modular L4 systems, explaining why Waymo's production system outperforms end-to-end models. EMMA demonstrates how multimodal large language models can handle rare "long tail" scenarios through generalization, achieving state-of-the-art performance on benchmarks while maintaining explainability through chain-of-thought reasoning. The research also explores using generative video models for simulation-based testing.

---

## Main Topics

### 1. History and Evolution of Autonomous Driving (00:00 - 02:40)
[**Start: 00:17**](https://www.youtube.com/watch?v=iS9YFW28XyM&t=17s)

- **Autonomous driving timeline**: Research began in 1980s with simple 3-layer neural networks; evolved to deeper networks; around 2020, NVIDIA and other labs published end-to-end driving models
- **L2 vs L4 systems**: Early end-to-end models showed poor performance (drifting, unsafe); Waymo's L4 system drives safely in complex urban environments
- **Waymo's modular approach**: System breaks down into perception (understanding the world), prediction (forecasting future states), and planning (determining driving actions like acceleration and steering)
- **Current deployment**: Waymo operates rider-only service in Phoenix, San Francisco, Austin, and Los Angeles

### 2. Scaling Challenges and Long-Tail Problems (02:40 - 04:25)
[**Start: 02:40**](https://www.youtube.com/watch?v=iS9YFW28XyM&t=160s)

- **Expansion plans**: 2024 road trip visiting ~10 cities including Tokyo, Japan - demonstrating global scaling ambitions
- **Long-tail scenarios**: Rare but critical events that individual drivers may never encounter, but Waymo sees regularly at scale
- **Example scenario**: Marathon runners on the road, construction cones, and a traffic controller waving the car through a red light - highly confusing situations requiring contextual understanding
- **Challenge**: These edge cases are very challenging to solve but essential for safe scaling

### 3. Foundation Models for Autonomous Driving (04:25 - 07:00)
[**Start: 04:25**](https://www.youtube.com/watch?v=iS9YFW28XyM&t=265s)

- **Gemini's generalization capability**: When shown video of "angry birds" (flock suddenly taking flight in front of car), Gemini correctly identifies the scenario and recommends slowing down and remaining alert
- **Second example**: Scooter rider slipping on wet road at night - Gemini accurately identifies all elements including a distant gas station
- **Key insight**: Foundation models generalize well to rare events that traditional systems struggle with
- **Research question**: How to leverage multimodal large language models for autonomous driving?

### 4. EMMA Architecture - Simple End-to-End Model (06:30 - 09:00)
[**Start: 06:43**](https://www.youtube.com/watch?v=iS9YFW28XyM&t=403s)

- **Input**: Route information (like Google Maps - "turn left at next intersection") converted to text + 8 surround-view cameras covering 360 degrees
- **Processing**: Video and routing text fed into EMMA (built on top of Gemini)
- **Output**: Future waypoints - predicted locations where the car should be in the next few seconds
- **Three key traits**:
  1. **Self-supervised**: Every driving log provides training labels (where the car actually went), making it highly scalable
  2. **Camera-only**: No LiDAR needed since Gemini is a vision model
  3. **HD map-free**: Only requires basic Google Maps, not detailed high-definition maps like production Waymo
- **Performance**: Achieves state-of-the-art quality on nuScenes benchmark, outperforming all customized models

### 5. Chain-of-Thought Reasoning for Explainability (09:00 - 11:30)
[**Start: 09:19**](https://www.youtube.com/watch?v=iS9YFW28XyM&t=559s)

- **Addressing explainability**: End-to-end models lack transparency - you only see outputs, not internal reasoning
- **Solution**: Chain-of-thought process before outputting the plan
  - Model identifies critical objects (e.g., cyclist, vehicle)
  - Explains expected behaviors of those objects
  - States driving meta-decision (e.g., "keep normal speed", "yield", "slow down")
- **Performance improvement**: Achieves even better results on Waymo Open Motion Dataset (100K scenarios, 100x larger than nuScenes)
- **Strong baselines**: Outperforms specialized models like Wayformer and MotionLM that use oracle perception systems, HD maps, and traffic light states

### 6. Scaling Laws and Multi-Task Training (11:30 - 14:00)
[**Start: 11:39**](https://www.youtube.com/watch?v=iS9YFW28XyM&t=699s)

- **Scaling laws validation**: Quality continues improving with larger models and more data (demonstrated on dataset magnitudes larger than public academic datasets)
- **Perplexity metric**: Lower perplexity = better planner results; clear improvement trend as training data increases
- **Multi-task capability**: Vision-language model core enables flexible task formulation
- **Tasks demonstrated**:
  - End-to-end driving (planning)
  - 3D object detection
  - Road graph estimation
  - Free-form VQA (visual question answering)
- **Detection quality**: Achieves similar quality to state-of-the-art specialized models on Waymo Open Dataset

### 7. Evaluation and Generative Simulation (14:00 - 17:22)
[**Start: 14:00**](https://www.youtube.com/watch?v=iS9YFW28XyM&t=840s)

- **Evaluation hierarchy**: Open-loop (replay logs) < Simulation < Real-world testing; simulation is more trustworthy than open-loop
- **Generative video simulation**: Leveraging Google DeepMind's V2 video generation model for realistic sensor simulation
- **Benefits**: Can control weather, time of day, and other conditions to systematically test EMMA
- **Results align with intuition**:
  - Rain/bad weather → worse performance (camera-only system affected by visibility)
  - Night → worse performance than daytime
  - Noon/afternoon → best performance
- **Waymo advantage**: Access to Google's foundation models (Gemini, video generation) due to shared Alphabet ownership
- **Vision**: Improve generalization to help Waymo scale to the next level

---

## Key Takeaways

1. **Foundation models show promise for handling long-tail autonomous driving scenarios** through superior generalization compared to specialized models
2. **EMMA achieves state-of-the-art results** with a simple architecture: camera-only, HD map-free, self-supervised training
3. **Chain-of-thought reasoning** addresses the explainability problem of end-to-end models while improving performance
4. **Multi-task training** demonstrates the flexibility of vision-language models for various autonomous driving tasks
5. **Generative simulation** using video foundation models offers a promising path for systematic evaluation
6. **Scaling laws apply**: Performance continues improving with more data and larger models
7. **Production deployment still requires modular systems**, but foundation models may help solve scaling challenges

---

**Last Updated:** 2026-01-03
