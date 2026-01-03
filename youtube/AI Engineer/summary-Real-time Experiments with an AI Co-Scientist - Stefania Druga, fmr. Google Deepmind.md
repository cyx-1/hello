# Real-time Experiments with an AI Co-Scientist - Stefania Druga, fmr. Google Deepmind

**Video URL:** https://www.youtube.com/watch?v=wNH3q9pqn0U

---

## Executive Summary

Stefania Druga presents her work on real-time AI co-scientist systems - essentially a "pair programmer" for science experiments. She demonstrates an open-source platform (under $300, built in 2 weeks) that combines sensors, cameras, and AI to monitor and analyze live experiments like crystal growth and fermentation. The system uses multimodal inputs (temperature sensors, microscopes, cameras) with Gemini AI to provide real-time analysis and insights. Inspired by Google DeepMind's AI co-scientist research that replicated 12 years of gene transfer discovery work in just 2 days, Druga's vision is to move beyond analyzing existing data to formulating hypotheses based on real-time empirical observations.

---

## Main Topics

### [Live Demo: Temperature Monitoring & Tracking Camera](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=17s)
**[00:17 - 03:50]**

- Live demonstration of the AI co-scientist system
- **Temperature monitoring** using micro:bit board with Jack DAC sensors
  - Real-time data streaming to AI assistant for analysis
  - AI provides ambient condition assessments (stable, dark, quiet environments at 26°C)
- **Custom protocols**: Users can define experiment parameters and constraints for context-aware feedback
- **REC camera demonstration**: Object tracking capabilities (trained on person tracking, but can be customized for crystal growth or other objects)
- **Custom experiment pages**: Ability to monitor data and plot in real-time
- All hardware components are open-source, total cost under $300

### [Why AI Co-Scientists Matter](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=230s)
**[03:50 - 04:32]**

- **Data overload problem**: Science generates massive amounts of complex data requiring parsing and analysis
- **Fast hypothesis generation**: AI can help generate new hypotheses at scale and identify blind spots in prior work
- **Speed acceleration**: Instead of testing one hypothesis at a time, AI enables testing 100 hypotheses simultaneously

### [Google DeepMind's AI Co-Scientist Inspiration](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=272s)
**[04:32 - 07:03]**

- **DeepMind paper** (published 2 months prior to talk) demonstrated multi-agent AI orchestration for scientific research
- **Agent roles**: Multiple Gemini 2.0 agents performing different scientific tasks
  - Analyzing and summarizing papers
  - Ranking hypotheses and options
  - Online search capabilities
  - Creating research plans
- **Validation approach**: Tested against prior discoveries
  - **Gene transfer mechanisms**: Discovery that took scientists 12 years → AI replicated in 2 days (without prior knowledge)
  - **Liver fibrosis treatment**: AI generated novel drug targets that were validated in wet lab experiments by experts
- **Key insight**: Not science fiction - real discoveries happening now in drug discovery, healthcare, bacterial resistance, and materials science

### [Vision: Real-Time vs. Async Analysis](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=423s)
**[07:03 - 08:19]**

- **Current approach**: Analyzing existing data asynchronously, providing researchers with plans
- **Vision**: Real-time hypothesis formulation based on empirical data being observed in the lab
- **Era of experience**: Inspired by Silver & Sutton's paper "Welcome to the Era of Experience"
  - Moving beyond human data indexing and predictions
  - AI learning from continuous environment interaction
  - Multimodal real-time data: images, sensors, audio streams

### [System Architecture Overview](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=499s)
**[08:19 - 10:21]**

- **Simple React app** with multiple input sources:
  - Jack DAC sensors via USB
  - Multiple webcams
  - Text input
  - Voice input (bidirectional communication)
- **Information flow**:
  - Physical sensors → Web USB API → Frontend hooks
  - Context assembly checks for available modalities (text, voice, image, chat history)
  - Dynamic context injection based on connected sensors and experiment type
  - Backend communication with Gemini API
  - Real-time responses

### [Hardware Components & Constraints](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=621s)
**[10:21 - 11:01]**

- **"Cooking" approach**: Cataloging available components (inputs, outputs, cameras, cables, boards)
- **Experiment constraints**:
  - Measurable in real-time for the presentation
  - Safe for home experimentation
  - Travel-friendly
- **Cost**: All parts under $300
- **Development time**: 2 weeks to build
- **Status**: Open-source (will be released)

### [Experiment 1: Crystal Growth](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=661s)
**[11:01 - 14:30]**

- **Chemistry basics**: Oversaturating salt solution in hot water, then gradual cooling creates nucleation and crystal growth
- **Key factors for beautiful crystals**:
  - Gradual cooling rate
  - Minimal movement/vibration
  - Humidity control
- **Measurements**:
  - Salt dissolution curves
  - Nucleation sites (where crystals form)
  - Crystal growth rate
  - Temperature and concentration tracking
- **Setup**: Microscope recording with fan blowing cool air from ice for temperature control
- **Data analysis**: CSV export of sensor values for visualization and analysis
- **Control groups**: Samples at different temperatures (room, fridge) for comparison
- **Key insight discovered**: Crystal formation happens in **bursts**, not gradually - sudden crystal growth occurs once critical saturation is reached

### [Experiment 2: Fermentation](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=870s)
**[14:30 - 15:16]**

- **Variables controlled**:
  - Salt and sugar concentrations in different dough samples
  - Temperature variations
- **Measurements**: Growth rate, CO2 production
- **Time-lapse recording** of data collection

### [Educational Version & Accessibility](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=916s)
**[15:16 - 16:01]**

- **Mobile-friendly**: Runs on phone
- **Camera testing**: Available for experimentation
- **Micro:bit integration**: Can connect and test sensors
- **API requirement**: Users need to provide their own API key
- **Target audience**: Teaching kids about science experiments
- **Demo availability**: Full lab version not yet deployed but coming soon with open-source code

### [Open-Source Ecosystem for Lab Automation](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=961s)
**[16:01 - 17:09]**

- **Lab equipment**: Entire ecosystem for recreating lab equipment in open-source
- **Jubilee motion platform** (University of Washington): Open-source automation platform
- **Open bioreactor**: Available for experiments
- **Workshop example** (April at UW): Week-long hackathon for automating scientific experiments
  - Droplet manipulation
  - Robot handling/mixing liquids
  - Vial manipulation
- **Goal**: Move beyond demo to real solutions for scientists and builders

### [Future: Simulations Based on Real Data](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=1029s)
**[17:09 - 18:03]**

- **Vision**: Real-time data (cameras, sensors, voice) → realistic simulations
- **Workflow**:
  1. Real-life experiments inform simulation parameters
  2. Run simulations with actual lab conditions
  3. Identify optimal experimental conditions
  4. Recreate those conditions in real life
- **Applications**: Crystal growth, bacteria colony growth, and beyond
- **Integration**: Combining real-time experimentation with simulation for accelerated discovery

### [Closing & Resources](https://www.youtube.com/watch?v=wNH3q9pqn0U&t=1083s)
**[18:03 - 18:36]**

- **Website**: Contains all projects, papers, and open-source resources
- **Education focus**: Passionate about AI education
- **Upcoming**: AI Education Summit announcement
- **Call to action**: Audience encouraged to explore the platform and join the education initiative

---

## Key Takeaways

1. **Real-time AI co-scientists** can accelerate scientific discovery by analyzing experiments as they happen, not just historical data
2. **Accessible science**: Complete system built for under $300 in 2 weeks using open-source components
3. **Proven concept**: DeepMind showed AI can replicate 12 years of research in 2 days and generate novel validated discoveries
4. **Multimodal integration**: Combining sensors, cameras, and AI enables dynamic, context-aware experimental assistance
5. **Future direction**: Integration of real-time data collection with simulation for optimal experiment design
6. **Open-source movement**: Growing ecosystem of tools (Jubilee, open bioreactors) supporting accessible lab automation
