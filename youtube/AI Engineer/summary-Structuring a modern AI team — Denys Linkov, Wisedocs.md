# Structuring a modern AI team — Denys Linkov, Wisedocs

**Video URL:** https://www.youtube.com/watch?v=SbUxRluVRwk

---

## Executive Summary

Denys Linkov, ML team lead at Wisedocs, challenges the conventional wisdom about building AI teams in this thought-provoking talk. Rather than rushing to hire AI researchers, he argues that most companies need generalist engineers with domain expertise who can ship products, talk to customers, and adapt to changing requirements. He introduces "Ampere's Wager" - would you trade your current team for five top researchers? - to help leaders think critically about team composition. The key insight: 90% of technology needed to solve problems already exists; success comes from proper application, not cutting-edge research. He emphasizes building cross-functional teams with inner loops (daily technical execution) and outer loops (domain differentiation), continuous learning through weekly upskilling sessions, and hiring based on your specific bottlenecks rather than following industry trends.

---

## Main Topics

### [Introduction: The AI-First Company Trend](https://www.youtube.com/watch?v=SbUxRluVRwk&t=0s)
Denys opens by discussing how companies like Shopify, Duolingo, and Zapier have declared themselves "AI-first," creating pressure to prove you can't hire an AI agent before hiring a person. He questions what this means for teams and introduces three main themes: anatomy of an AI team, evolution of generalists, and the hiring question.

**Key Points:**
- Major tech companies claiming AI will write most code and lead to "extinction of software engineers"
- New hiring expectations in AI-first companies
- Three main discussion themes outlined

### [Company Types and Technology Adoption](https://www.youtube.com/watch?v=SbUxRluVRwk&t=73s)
Different company types face different challenges: tech companies lack domain knowledge, tech-enabled companies struggle with tech execution, and verticalized solutions companies fall somewhere in between.

**Key Points:**
- Spectrum of companies: pure tech, verticalized/services, tech-enabled
- Fax machines still a growing multi-billion dollar market
- In 2017, only 3% of US payments were contactless
- Took 40 years after personal computing for medical records to go digital
- Technology adoption is the real bottleneck, not technology capability

### [The 90% Technology Thesis](https://www.youtube.com/watch?v=SbUxRluVRwk&t=164s)
Denys argues that we already have 90% of the technology needed to solve humanity's problems - the limitation is how we use and deploy it, not the technology itself.

**Key Points:**
- Technology adoption lag illustrated by fax machines, checks, medical records
- Success depends on understanding problems, not just having cutting-edge tech
- Team structure should reflect this reality

### [Ampere's Wager: Do You Need AI Researchers?](https://www.youtube.com/watch?v=SbUxRluVRwk&t=238s)
The provocative question: Would you trade your current team (with domain knowledge and experience) for five researchers from top labs like OpenAI or Anthropic? For most companies, the answer should be no.

**Key Points:**
- Until you hit certain scale, hiring AI researchers doesn't make sense
- Pre-training or even fine-tuning large models often isn't the first value-creating step
- Lots of transformation work needed before research becomes the bottleneck
- Exception: Companies where the model IS the product (OpenAI, Anthropic, etc.)

### [What Does an AI Team Actually Need to Do?](https://www.youtube.com/watch?v=SbUxRluVRwk&t=308s)
Comprehensive list of responsibilities: define use cases, integrate with products, measure ROI, find right data, test workflows, build interfaces, sell the product, and make customers care.

**Key Points:**
- Success requires multiple roles working together
- Can't just tell researchers "go make me $10 million"
- Need comprehensive AI team structure
- Companies ship their org charts - avoid siloed AI teams

### [Identifying Your Bottleneck](https://www.youtube.com/watch?v=SbUxRluVRwk&t=376s)
Critical questions to determine what type of team you need: Are you struggling to ship features? Acquire users? Retain users? Monetize correctly? Scale? Ensure reliability and observability?

**Key Points:**
- Identify your specific bottleneck before hiring
- Different bottlenecks require different team compositions
- Only you know what kind of team you need
- Prioritize accordingly when building your AI team

### [The Generalist Approach: 2021 Case Study](https://www.youtube.com/watch?v=SbUxRluVRwk&t=411s)
Denys shares his experience building a conversational AI platform team in 2021 with a generalist-first approach supported by automation.

**Key Points:**
- Goals: serve hundreds of thousands of concurrent models, multi-domain, low cost, real-time training
- Built custom MLOps platform, fine-tuned encoder models, RAG as a service
- Team owned 6+ microservices
- Three focus areas: model training (mid-level), model serving (abstracted away complexity), business acumen (engineers on customer calls)

### [Skill Requirements and Trade-offs](https://www.youtube.com/watch?v=SbUxRluVRwk&t=475s)
You can't afford top grades in every skill area. Define minimum viable expertise: model training (upper half, general architectures, encoder fine-tuning, data engineering, HuggingFace), model serving (understand abstractions and trade-offs), business acumen (engineers must talk to customers).

**Key Points:**
- Budget constraints require choosing skill levels strategically
- Built abstractions so engineers didn't need deep Kubernetes knowledge
- Engineers needed to get on customer calls, not hide in basement coding
- Multiple people can share responsibilities if team works well together

### [2024 Evolution: Open Source Changes the Game](https://www.youtube.com/watch?v=SbUxRluVRwk&t=558s)
Building a new team in 2024, Denys found that open source tools and commercial models had advanced, changing team requirements.

**Key Points:**
- Shadow deployments and A/B testing now available in platforms
- Commercial API usage, prompt tuning, fine-tuning commercial models became important
- Using both decoder and encoder models with different nuances
- Open source offerings eliminated need to build custom platforms
- Higher bar for domain knowledge in medical record processing

### [Inner and Outer Loops Framework](https://www.youtube.com/watch?v=SbUxRluVRwk&t=658s)
Inner loops are daily activities the team needs to accomplish together. Outer loops are broader activities that differentiate your company (not requiring constant interaction but crucial for success).

**Key Points:**
- Inner loop: model training, prompting, product requirements, model serving, domain expertise, building business cases
- Outer loop: specialized knowledge that sets you apart
- Weak technical loop = struggle with execution
- Weak domain loop = no product-market fit
- Must understand feedback and collaboration loops within company

### [Generalists vs Specialists: When to Use Each](https://www.youtube.com/watch?v=SbUxRluVRwk&t=720s)
Most companies in AI transformation win with generalists who are adaptable. Specialists become necessary only when you've exhausted general knowledge and need that extra 5% performance.

**Key Points:**
- Generalists are adaptable and good enough for most transformation work
- Specialists needed to push the extra 5% at advanced stages
- Context determines which approach works
- Generally prefer generalists who can do more than just write code

### [Upskilling, Reskilling, and Learning](https://www.youtube.com/watch?v=SbUxRluVRwk&t=768s)
Three critical areas for the AI wave: learn to build (vibe coding, functional prototypes), become domain experts (writing evals, defining use cases), and be human-facing (engineers on customer calls, someone to sell).

**Key Points:**
- Shift from static requirements to functional prototypes
- Domain experts should write evaluations and use cases directly, not just provide feedback
- Engineers must be willing to talk to customers - if they refuse, it's a learning opportunity
- Weekly 30-minute learning cadences on team priorities
- Consequences of not upskilling are higher than the effort required

### [When and Who to Hire](https://www.youtube.com/watch?v=SbUxRluVRwk&t=849s)
People are hired for two reasons: to hold context and to act on context. You need expertise to verify AI execution, and humans should remain accountable for the systems we build.

**Key Points:**
- Too few people means things get dropped and priorities can't be executed
- AI agents with massive context windows can't fully replace human expertise
- Humans need context to have expertise, and must remain accountable
- Hiring on a budget requires knowing team composition and needs
- Top researchers are expensive; generalist AI engineers are cheaper

### [Avoiding Hiring Trends and Fads](https://www.youtube.com/watch?v=SbUxRluVRwk&t=911s)
Don't follow trends blindly. The "don't hire junior engineers, just use AI agents" trend contradicts YC bringing 2,000 young people to San Francisco for AI school.

**Key Points:**
- Verify trends before following them
- Think from first principles about your needs
- Consider team composition: new grads vs 30-year veterans
- Explore retraining opportunities
- Many ways to build great teams

### [Relevant Interview Questions](https://www.youtube.com/watch?v=SbUxRluVRwk&t=961s)
Stop putting candidates through LeetCode problems unrelated to the actual job, especially now that LLMs can solve them.

**Key Points:**
- Ask questions relevant to the actual job
- LeetCode is no longer an effective evaluation method
- Focus on skills that matter for your specific needs

### [Final Decision: Ampere's Wager Revisited](https://www.youtube.com/watch?v=SbUxRluVRwk&t=974s)
For Wisedocs, Denys would choose the domain-focused team with expertise, sales ability, and customer empathy over five top researchers. Also introduces "Blackwell's Wager" - GPUs or a team?

**Key Points:**
- Domain expertise, ability to sell, empathy with customers beats pure research talent
- Team structure depends on your company's specific domain
- Cross-functional teams will continue to be effective but built differently
- Greater overlap between roles, everyone works with AI systems
- Continuous learning is mandatory in fast-moving field

### [Conclusion: Three Main Lessons](https://www.youtube.com/watch?v=SbUxRluVRwk&t=1008s)
Know what team you need to win, build effective cross-functional teams with greater overlap, and make continuous learning part of your culture.

**Key Points:**
- Start by understanding what team you need to win
- Cross-functional teams built differently but still effective
- Everyone has opportunity to work with and contribute to AI products
- World moves too quickly to stop learning (Pelican evals now cover 6 months not a year)
- Keep up to date, make learning part of your culture
