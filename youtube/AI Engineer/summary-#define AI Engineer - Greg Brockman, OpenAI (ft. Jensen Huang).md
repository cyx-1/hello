# #define AI Engineer - Greg Brockman, OpenAI (ft. Jensen Huang)

**Video URL:** https://www.youtube.com/watch?v=avWhreBUYF0

---

## Executive Summary

In this 41-minute fireside chat at the AI Engineer conference, Greg Brockman (President and Co-Founder of OpenAI) discusses his journey from building a chemistry website in high school to leading one of the world's most influential AI companies. The conversation spans his Stripe days, the founding philosophy of OpenAI, the explosive launches of ChatGPT and DALL-E, the evolution of coding with AI, and insights into AGI development. Jensen Huang (NVIDIA CEO) makes two video appearances asking questions about AI infrastructure and the future of development workflows. Key themes include the equal value of engineering and research, the importance of first-principles thinking, the shift toward agentic AI systems, and how AI will fundamentally reshape the economy.

---

## Main Topics

### 1. [Early Life and Career Origins](https://www.youtube.com/watch?v=avWhreBUYF0&t=0s)
**[00:00 - 05:00]**

Greg shares his unconventional path into technology:
- **Background:** Theater, chemistry, and math enthusiast who thought he'd be a mathematician
- **First code:** Built a chemistry textbook website after a friend suggested it was easier than self-publishing
- **The magic moment:** Creating a table-sorting widget that worked exactly as imagined - "that was magic"
- **Key insight:** In math, three people will ever care about your proof. In programming, everyone gets the benefit even if only three people read the code
- **Stripe journey:** Got cold-emailed while at MIT after mutual friends recommended him. Met Patrick Collison late at night during a storm and just talked about code. Dropped out of MIT to join when they were just 4 people, stayed until 250 people as first CTO
- **Parents' reaction:** Never gave up on the dream of him finishing his degree (question from his brother Matthew, now CTO of Julius AI)

**Memorable quote:** "In programming, you write it down in an obscure way, we call a program. And then maybe only three people ever read that program and care about the code. But everyone gets the benefit. No one has to understand the details. That thing that was in your head, it's real. It's in the world."

---

### 2. [Stripe Culture: Speed and First Principles](https://www.youtube.com/watch?v=avWhreBUYF0&t=300s)
**[05:00 - 08:00]**

The infamous "install on customer laptops" story is actually an urban legend, but Greg shares what Stripe culture was really like:
- **Customer obsession:** Added all customers on Gchat for constant contact
- **The Wells Fargo story:** Told a technical integration would take 9 months. Completed it in 24 hours by treating it like a college problem set
  - John tested from top down, Daryl from bottom up, Greg implemented
  - When errors occurred during certification, Patrick kept the certifier on the phone while Greg frantically fixed code
  - Got 5 attempts, failed but rescheduled 2 hours later and passed
  - "Six weeks worth of normal dev work done in that moment"
- **First principles thinking:** Find where constraints are unnecessary overhead that no longer applies to your specific circumstance
- **Relevance to AI:** This mindset is especially valuable now with AI accelerating productivity

---

### 3. [Independent Study and Self-Learning Philosophy](https://www.youtube.com/watch?v=avWhreBUYF0&t=480s)
**[08:00 - 12:00]**

Greg's approach to learning has been consistent throughout his life:
- **Math acceleration:** In 6th grade, his dad taught him algebra. In 7th grade, tried to skip to 8th grade math but teacher said "every parent believes their child is special." After a month of not paying attention and acing questions, teacher relented
- **Breaking constraints:** In 8th grade, ran out of math at middle school. Did online courses and completed 3 years of high school math in 1 year
- **Compound effects:** By high school finished all math, then drove to University of North Dakota to take any classes wanted
- **GPU rig:** In 2015, built a GPU machine in New York for Kaggle competitions using Titan X cards. "This is what computers are meant to be"
- **Advice:** If you have an opportunity to explore and you have a passion you're enjoying, just go deep. It's not always fun - push through the boredom hurdles

**Key insight:** When you're excited about something independently, you can break the constraints and accelerate far beyond normal timelines.

---

### 4. [Discovering Deep Learning: The Turing Epiphany](https://www.youtube.com/watch?v=avWhreBUYF0&t=720s)
**[12:00 - 16:00]**

How Greg became convinced AGI was possible:
- **The Turing paper (1950):** Read "Computing Machinery and Intelligence" - fewer hands in audience had read it than had used W3 Schools
- **The revelation:** Turing proposed not writing down all the rules, but building a "child machine that learns like a human child" with rewards and punishments
- **The programmer's limit:** As a programmer you have to understand everything and write down all the rules. But what if the machine can understand and solve problems you yourself cannot understand?
- **Disillusionment (2008):** Asked NLP professor to do research, got handed parse trees. "This is not what Turing was talking about"
- **Deep learning emergence:** Reading Hacker News posts about deep learning in 2013-2014. Started meeting people in the field and realized all his smartest college friends had ended up there
- **AlexNet (2012):** Alex Krizhevsky's fast convolutional kernels + Ilya Sutskever's vision = blew everyone out of the water in ImageNet
- **The pattern:** People said it would never work in their field (machine translation, NLP, etc.), then it became the best in all those areas. Walls between departments torn down
- **Historical perspective:** Neural nets date back to McCulloch-Pitts neuron paper (1943). "These neural net people have no new ideas. They just want to build bigger computers. And I'm like yes, that's what we need to do."

**Memorable quote:** "What if the machine can understand things and solve problems that you yourself cannot understand. Like that feels fundamental, right? That feels like how you actually solve problems that are important to humanity."

---

### 5. [Engineering and Research Partnership at OpenAI](https://www.youtube.com/watch?v=avWhreBUYF0&t=960s)
**[16:00 - 21:00]**

On the relationship between great engineers and great researchers:
- **2022 thesis:** "It's time to be an ML engineer" - great engineers can contribute at same level as great researchers
- **Still true:** If anything, even more true now
- **AlexNet example:** Fundamentally about engineering fast convolutional kernels on GPU. Alex had the engineering, Ilya had the idea to apply it to ImageNet. "The combination of great engineering together with the idea of what to do with it - that's what makes the magic work"
- **Evolution:** Now it's not just build some kernels, it's build systems that scale to 100,000 GPUs and complex RL orchestration
- **Both essential:** Without the idea, you're dead in the water. Without the engineering, the idea won't see the light of day
- **OpenAI philosophy:** Engineering and research valued and working as partners from day one

**Early friction between mindsets:**
- **Engineers:** "If I've got an interface, you should not care what's behind it"
- **Researchers:** "If there's a bug anywhere in the system, all I get is slightly degraded performance. No exception, no indication of where. I'm responsible for understanding everything"
- **Failed approach:** Engineers write code, then big debate over every single line - "never going to move, going to be so slow"
- **Successful approach:** Greg would propose 5 ideas, researcher would say 4 are bad, Greg would say "great that's all I wanted"
- **Never fully solved:** "You never fully solve it right, you just sort of solve the current level of problem then move on to the next level of sophistication"

---

### 6. [ChatGPT and DALL-E Launch Stories](https://www.youtube.com/watch?v=avWhreBUYF0&t=1260s)
**[21:00 - 26:00]**

The explosive launches that changed everything:
- **ChatGPT (Nov 30, 2022):** 1 million users in 5 days
  - Supposed to be a low-key research preview
  - Had to pull compute from research to meet demand
  - Moment of "oh this is really happening"

- **DALL-E / Image Generation (2024):** 100 million image generation users in 5 days
  - Also supposed to be low-key research preview
  - 20x faster growth than ChatGPT
  - Infrastructure challenge: kept having to pull more compute

**Key lessons:**
- Both were research previews that exploded beyond expectations
- The pattern: underestimating how much people would want to use the technology
- Infrastructure scaling became critical challenge

---

### 7. [GPT-4 Launch and the Birth of "Vibe Coding"](https://www.youtube.com/watch?v=avWhreBUYF0&t=1560s)
**[26:00 - 32:00]**

The famous GPT-4 demo and its impact:
- **The sketch demo:** Greg's wife drew the joke website sketch. He took a photo and fed it to GPT-4 which generated the code
- **First vibe coding:** First time the world saw you could just describe what you want and get working code
- **"Is this AGI?"** After first talking to GPT-4: "It's clearly not an AGI but it's really hard to say why"
- **The vision shift:** Moved from interactive loops (Codex) to agentic systems
  - Codex: You describe, it writes, you iterate
  - Agents: Give high-level task, it breaks down, executes, debugs itself

**Codex impact on OpenAI:**
- Low double-digit percentage of OpenAI PRs now written entirely by Codex
- Anecdote: Needed to add image embedding feature on Friday. Junior engineer had Codex do it. Senior engineer reviewed Monday. "This is great, ship it" - shipped by 10am
- **GitHub scale:** 24,000 PRs merged in one day in public repositories using AI assistance

**Development philosophy with AI:**
- Make smaller, well-tested modules
- The model will fill in the details
- Structure code so AI can work with it effectively

---

### 8. [Infrastructure and Scaling (Jensen Huang's First Question)](https://www.youtube.com/watch?v=avWhreBUYF0&t=1905s)
**[31:45 - 36:00]**

**Jensen Huang appears via video** asking about AI infrastructure challenges:

**Jensen's question [31:45](https://www.youtube.com/watch?v=avWhreBUYF0&t=1905s):** How does OpenAI think about infrastructure for diverse AI workloads (long compute/agents vs real-time/R2-D2 companions, prefill vs decode, low latency vs high throughput)?

**Greg's response:**
- **Two workload types:**
  - Agents: Long compute, reasoning loops, can take minutes/hours
  - Real-time companions: Sub-second latency requirement (like R2-D2)

- **Homogeneity as default:** Better to have general-purpose accelerators than over-specialize
- **Mixture of experts example:** Can utilize misbalanced resources (memory vs compute)
- **The bottlenecks:** Compute, data, algorithms, power, and money
  - All of these matter
  - "Basic research is back" - algorithms matter again, not just scale
  - Can't just throw money at the problem

**Key insight:** While infrastructure needs are diverse, maintaining flexibility through homogeneous systems often beats premature specialization.

---

### 9. [Future of Development and Domain-Specific Agents (Jensen's Second Question)](https://www.youtube.com/watch?v=avWhreBUYF0&t=2278s)
**[37:59 - 41:00]**

**Jensen Huang's second question [37:59](https://www.youtube.com/watch?v=avWhreBUYF0&t=2278s):** How will development workflows change as AGIs become more capable? Will we see domain-specific agents with reasoning, planning, tools, memory?

**Greg's response on the future:**
- **Menagerie of models:** Evidence shifting toward diverse collection of different models rather than "one AI in the sky"
- **Distillation works:** Models using other models, learning from each other
- **Economic transformation:** Economy will be fundamentally powered by AI
  - Question isn't "will AI take jobs?" but "how do we get 10x more economic output?"
  - Healthcare: AI to help doctors serve more patients better
  - Education: AI to help teachers provide better personalized instruction

**Domain-specific considerations:**
- Healthcare and education require deep domain expertise
- Can't just ship fast and break things
- Need careful thought about how to integrate AI
- But the potential is enormous: 10x more activity, 10x more economic output

**On code structure for AI era:**
- Make smaller modules that are well-tested
- Let models fill in the details
- Design systems so AI can work with them effectively

**Closing thought:** We're at the beginning of a fundamental economic transformation where AI augments human capabilities across every domain.

---

## Key Takeaways

1. **First principles thinking beats arbitrary constraints** - Stripe's 24-hour Wells Fargo integration vs 9-month timeline
2. **Engineering and research are equally essential** - The AlexNet story exemplifies this partnership
3. **Self-directed learning compounds rapidly** - Greg's pattern of independent study from middle school through GPU rigs
4. **The vision was always AGI** - Turing's 1950 paper laid out the path 75 years ago
5. **Launches exceeded all expectations** - ChatGPT and DALL-E were both "low-key research previews"
6. **We're heading toward a menagerie of AI models** - Not one AGI but many specialized systems working together
7. **Basic research matters again** - Can't just scale with money; algorithms are back in focus
8. **Economic transformation is coming** - Question is how to 10x output, not whether AI takes jobs

---

## Jensen Huang Appearances

**Note:** Despite being mentioned in the title "ft. Jensen Huang," Jensen does NOT appear in person. He makes two video appearances:

1. **[31:45](https://www.youtube.com/watch?v=avWhreBUYF0&t=1905s)** - Question about AI infrastructure for diverse workloads
2. **[37:59](https://www.youtube.com/watch?v=avWhreBUYF0&t=2278s)** - Question about future of development workflows with AGI

Both are pre-recorded video questions, not live conversation.

---

## Additional Context

**Other guest questions in the video:**
- Matthew Brockman (Greg's brother, CTO of Julius AI) - about finishing his degree
- Dylan Patel - questions about technical details (not analyzed in detail here)

**Video length:** Approximately 41 minutes

**Key people mentioned:**
- Patrick Collison (Stripe co-founder)
- Ilya Sutskever (OpenAI co-founder, chief scientist)
- Alex Krizhevsky (AlexNet)
- Alan Turing
- Geoffrey Hinton
- Jeff Dean

---

*Summary generated on 2026-01-01*
