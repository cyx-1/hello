# From Vibe Coding To Vibe Engineering – Kitze, Sizzy

**Video URL:** https://www.youtube.com/watch?v=JV-wY5pxXLo

## Executive Summary

Kitze, creator of Sizzy browser, delivers a humorous and insightful talk about the evolution from "vibe coding" to "vibe engineering" in the age of AI-powered development. He contrasts the experiences of developers who dismiss AI coding tools with those who embrace them, particularly focusing on the difference between casual "vibe coders" and serious "vibe engineers." Through personal examples and witty observations, he demonstrates how AI tools like Cursor's Composer have revolutionized his productivity, enabling him to accomplish in weeks what previously took months. The talk addresses common criticisms of AI-assisted coding, the importance of engineering judgment, the future of developer jobs, and why senior developers are better positioned to leverage these tools than juniors.

## Main Topics

### [Introduction and Background](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=0s)
- Kitze introduces himself and his projects: Sizzy (developer browser), Benji (life OS app), Zero to Ship (course), and Glink
- Jokes about attending conferences for "networking" and teaching
- Sets expectations for his talk style: 50% tweets, 40% pain, 30% reason to remember the name

### [The State of Frontend Development (2017-2024)](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=132s)
- Compares progress in other industries (VR, gaming, 3D) vs. frontend development
- Highlights persistent frustrations: still can't style select elements, jQuery remains popular (15M downloads), CLI tools thriving
- Jokes about the inability to agree on how to implement a simple counter
- Points out that React is still the dominant library despite its complexity

### [LLMs and React Code Quality](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=277s)
- LLMs excel at writing React because they don't care about repetitive code
- Humans have an addiction to abstraction that is often counterproductive
- "This is our brain on cocaine. This is our brain on sugar. This our brain when you realize we can abstract something."
- With Composer, you can reach the right abstraction quicker, but also the wrong abstraction quicker
- LLMs are good at React because "no one is actually good at writing React"

### [Vibe Coding vs Vibe Engineering](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=360s)
- **Vibe Coding**: Casual users who give vague prompts like "make me a million dollar app and make no mistakes"
- **Vibe Engineering**: Experienced developers who use agents strategically while maintaining technical judgment
- The casino analogy: buying tokens vs spinning slots, hitting jackpot vs garbage, "one more prompt and the bug will disappear"
- Introduces the term "vibe engineering" (coined on Twitter) as the professional evolution of vibe coding
- Lists 15+ projects he's "vibe engineered" that he wouldn't have bothered with otherwise

### [Why Vibe Coding Gets a Bad Rap](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=420s)
**Spectrum of developers:**
- Juniors love it (want to build their own SaaS)
- Super seniors love it (working on libraries/frameworks)
- Middle majority hates it ("this will never be good enough, my code is perfect")

**Common reasons for negative experiences:**
- Unlucky timing (trying a hyped model during a degraded period)
- Being overwhelmed by buzzwords and hype
- Being a "PITA dev" (Pain In The Ass Developer) - explained later
- Cheapening out on AI tool subscriptions
- Scale issues

### [Vibe Engineering Tips](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=576s)
- Use git workspaces for experimentation
- Stay chronically on Twitter to keep up with developments
- Have a solid starting point (good primitives, components, patterns, abstractions)
- Examples of vibe engineering requests vs vibe coding requests:
  - Engineering: "Make sure the TRPC implementation follows the abstraction patterns from api/users/list.ts"
  - Coding: "Make me a million dollar app"

### [Who Should NOT Use AI Coding Tools](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=742s)
- DO NOT give AI tools to interns and juniors
- "The equivalent of giving a gun to a toddler"
- Juniors can't distinguish good code from bad code
- Best results come from skeptical seniors who learn vibe engineering

### [When to Use Vibe Coding](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=762s)
- One-off scripts
- Simple features
- Code that won't be touched or seen again
- Personal tools and one-time tools
- Requires the skill of knowing which code is "good enough"

### [Why People Fail at Vibe Coding](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=786s)
**Unlucky timing:**
- Trying Claude Code right after a model degradation
- Not realizing when you're using a downgraded model

**Overwhelmed by buzzwords:**
- MCP (Model Context Protocol) - jokingly defined as "Marketing Charge Protocol, Mythical Compatibility Promise, Manufacturer Complexity Pipeline"
- Lists numerous AI buzzwords that create confusion

### [The "PITA Dev" Problem](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=1028s)
**Pain In The Ass Developer characteristics:**
- Code must be perfectly DRY (Don't Repeat Yourself)
- Everything must follow exact company conventions
- Obsessed with "best practices" regardless of context
- Can't distinguish between code that matters and code that doesn't
- Will bikeshed over trivial details

**Why this matters with AI:**
- Faster models (like Haiku) work well for vibe engineers who can judge output
- PITA devs can't use fast models because they can't tell if code is "good enough"

### [Kitze's Personal Success Stories](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=900s)
**Achieved in 2 weeks more than in the last year:**
- Benji: Moved from abandoned Blitz.js to Next 16 with App Router, TRPC, Monorepo, Turbo Repo, React Native app, 90% of features in less than a week
- Glink: Revived from near-death, complete refactor
- Sizzy: Migrated complex Electron/MobX spaghetti code successfully
- Zero to Ship: Refactored to monorepo

**His AI tool evolution:**
- Copy/paste → Tab completion → WebStorm with Super Maven → Cursor with tab → Agents (Devin) → Claude Code with GPT-5 codex → Back to Cursor (for Composer)
- Composer was the game-changer that brought him back to Cursor

### [Essential Vibe Engineering Skills](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=1128s)
A mix of multiple competencies:
- Knowing the limits of the model
- Understanding agent capabilities
- Managing context and context limits
- Writing effective rules and prompts (but don't call it "prompt engineering")
- Being chronically on Twitter
- Having all the technical knowledge to steer models correctly
- Judging which code is good enough for the job

### [Clean Code in the AI Era](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=1173s)
- Definition of clean code is changing
- New standard: "cleanish enough for the agents to be able to continue working on it"
- If you keep accepting slop, you'll eventually hit a roadblock even with engineering skills
- Balance between perfectionism and pragmatism

### [Should You Study Computer Science?](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=1194s)
- **Absolutely yes** - now is the best time to learn
- Kitze learned with the "slowest LLM ever" (a friend who would reply 45 minutes later while playing Counter-Strike)
- Modern learners have instant feedback from AI tools
- Having fundamentals makes you a better vibe engineer

### [The Future of Developer Jobs](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=1228s)
- Shows examples of fearmongers claiming "AI will take our jobs"
- "Let's just say they're fine for now. I don't know when will that 'for now' end"
- Companies like Shopify have vibe coding leaderboards tracking token usage
- Most productive employees are using AI tools heavily

**The "PITA dev" obsolescence:**
- Cloud agents can now do what perfectionist devs do, but faster
- May not be as perfect, but speed matters more at scale
- Roles in companies are becoming more AI-augmented

**Model progression:**
- Every time people claim plateaus, new models drop (GPT-5 codex, Claude 3.0)
- Claude 3.0 can "vibe code MacOS and iOS from one prompt"
- PITA devs still claim "I can do that in 3 weeks with a team of five"

### [New Job Opportunities](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=1386s)
- "Vibe code fixer" - people who finish the last 20% after AI gets you 80% there
- This is becoming a real service/business
- Historical parallel: highest-paid engineers have always been those maintaining legacy systems
- **Cobol Cowboys** example: Company in business for "237 years" with extremely senior engineers maintaining critical legacy systems
- Dark humor about the future job market for developers

### [Closing Thoughts](https://www.youtube.com/watch?v=JV-wY5pxXLo&t=1461s)
- Encourages embracing vibe engineering while maintaining engineering judgment
- The tools are getting better rapidly
- Senior developers with good judgment are best positioned to thrive
- Balance between adoption and skepticism is key

## Key Takeaways

1. **Vibe Engineering ≠ Vibe Coding**: Engineering requires technical judgment, understanding of architecture, and the ability to steer AI tools effectively

2. **Experience Matters**: Senior developers get 10x results with AI tools because they can judge code quality; juniors should not be given AI tools as their primary development method

3. **The "Good Enough" Skill**: Knowing when code is adequate for its purpose is crucial for productive AI-assisted development

4. **Abstractions Cut Both Ways**: AI tools make it easier to create both good and bad abstractions - judgment is essential

5. **Speed vs Perfection**: Fast iteration with "good enough" code often beats perfect code delivered slowly

6. **Stay Current**: Being "chronically on Twitter" and keeping up with AI developments is necessary for effective vibe engineering

7. **Jobs Are Safe (For Now)**: While AI is transformative, developers with strong fundamentals and good judgment remain highly valuable

8. **Learn Computer Science**: Fundamentals matter more than ever because they enable better use of AI tools
