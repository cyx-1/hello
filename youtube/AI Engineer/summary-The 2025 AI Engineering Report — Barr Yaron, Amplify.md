# The 2025 AI Engineering Report — Barr Yaron, Amplify

**Video URL:** https://www.youtube.com/watch?v=mQ7_Zje7WKE

---

## Executive Summary

Barr Yaron from Amplify presents findings from the 2025 State of AI Engineering survey with 500 respondents. Key insights reveal that AI engineering is a rapidly growing field with diverse practitioner titles and experience levels. The survey shows widespread adoption of LLMs across multiple use cases, with RAG being the most popular customization method. Fine-tuning is more prevalent than expected, especially among researchers. The field faces a "multimodal production gap" where text dominates while image, video, and audio lag significantly. Agents are emerging but not yet working well for most, though adoption intent is high. The biggest pain point is evaluation, and the community relies heavily on human review for quality assessment.

---

## Topics and Key Points

### [Introduction and Survey Overview](https://www.youtube.com/watch?v=mQ7_Zje7WKE&t=0s)
- 500 respondents participated in the survey
- Diverse mix of titles and roles (engineers, researchers, founders, VCs)
- Most people doing AI engineering work don't have "AI engineer" as their official title
- AI engineering as a search term barely registered before late 2022 (ChatGPT launch)
- Interest has not slowed since

### [Experience Levels and Demographics](https://www.youtube.com/watch?v=mQ7_Zje7WKE&t=156s)
- Wide variety of experience levels in the community
- Among software engineers with 10+ years of experience, nearly half have been working with AI for 3 years or less
- 1 in 10 seasoned developers started with AI just this past year
- Change is the only constant, even for veterans

### [What People Are Building](https://www.youtube.com/watch?v=mQ7_Zje7WKE&t=198s)
- More than half use LLMs for both internal and external use cases
- 3 out of top 5 models for customer-facing products are from OpenAI
- Half of top 10 models for external use are from OpenAI
- Top use cases: code generation, code intelligence, writing assistants, content generation
- 94% using LLMs for at least 2 use cases
- 82% using for at least 3 use cases
- High heterogeneity in applications

### [Customization Methods and Fine-tuning](https://www.youtube.com/watch?v=mQ7_Zje7WKE&t=248s)
- RAG is the most popular customization method (70% of respondents)
- Fine-tuning adoption was higher than expected across the board
- Researchers and research engineers do the most fine-tuning
- 40% of fine-tuners mentioned LoRA or QLoRA (parameter-efficient methods)
- Popular techniques: DPO, reinforcement fine-tuning, supervised fine-tuning
- Many hybrid approaches being used

### [Model and Prompt Updates](https://www.youtube.com/watch?v=mQ7_Zje7WKE&t=316s)
- More than 50% update models at least monthly
- 17% update models weekly
- 70% update prompts at least monthly
- 10% update prompts daily
- 31% of respondents have no way of managing their prompts

### [The Multimodal Production Gap](https://www.youtube.com/watch?v=mQ7_Zje7WKE&t=369s)
- Image, video, and audio usage all lag text usage by significant margins
- Text dominates production deployments
- Among non-users, audio has the highest intent to adopt (37%)
- "Get ready to see an audio wave"
- As models improve and become more accessible, adoption numbers expected to increase

### [Agents: Coming But Not Yet Working Well](https://www.youtube.com/watch?v=mQ7_Zje7WKE&t=450s)
- Survey defined AI agent as: "a system where an LLM controls the core decision-making or workflow"
- 80% say LLMs are working well at work
- Less than 20% say the same about agents
- Majority plan to use agents even if not currently using them
- Fewer than 1 in 10 say they will never use agents
- Majority of agents in production have write access (typically with human in the loop)
- Some agents can take actions independently

### [Monitoring, Observability, and Evaluation](https://www.youtube.com/watch?v=mQ7_Zje7WKE&t=534s)
- Most use multiple methods to monitor systems
- 60% use standard observability
- Over 50% rely on offline eval
- Human review is still the most popular evaluation method
- Most respondents rely on internal metrics for monitoring usage
- Evaluation is the #1 most painful thing about AI engineering today

### [Vector Databases and Storage](https://www.youtube.com/watch?v=mQ7_Zje7WKE&t=575s)
- 65% use a dedicated vector database
- Specialized vector databases provide enough value over general-purpose databases with vector extensions
- 35% primarily self-host
- 30% primarily use a third-party provider

### [Fun Stuff: Community Opinions](https://www.youtube.com/watch?v=mQ7_Zje7WKE&t=604s)
- Most think agents should disclose when they're AI and not human
- Slight majority willing to pay more for inference time compute (but not by wide margin)
- People believe transformer-based models will be dominant in 2030 ("attention is all we'll need")
- Majority think open source and closed source models are going to converge
- Average guess: 26% of US Gen Z will have AI girlfriends/boyfriends

### [Popular Content and Wrap-up](https://www.youtube.com/watch?v=mQ7_Zje7WKE&t=695s)
- Top 10 podcasts and newsletters that AI engineers learn from listed
- Many creators are in the room at the conference
- Swix/Latent Space appears in both top newsletters and top podcasts
- Full report to be published the following week with more details including favorite models and tools

---

## Key Statistics

- **500 respondents** participated in the survey
- **94%** of LLM users apply them to at least 2 use cases
- **70%** use RAG for customization
- **50%+** update models at least monthly
- **70%** update prompts at least monthly
- **31%** have no prompt management system
- **80%** say LLMs work well, but only **<20%** say the same for agents
- **65%** use dedicated vector databases
- **Evaluation** is the #1 pain point

---

## Takeaways

1. The AI engineering field is experiencing explosive growth with practitioners from diverse backgrounds
2. OpenAI models dominate customer-facing production use cases
3. Multi-use case adoption is the norm, not the exception
4. Fine-tuning is more widespread than many expected
5. There's a significant "multimodal production gap" with text far ahead of other modalities
6. Agents are the future but not yet reliable in production
7. Evaluation remains the biggest challenge facing AI engineers
8. Human review is still the gold standard for quality assessment
