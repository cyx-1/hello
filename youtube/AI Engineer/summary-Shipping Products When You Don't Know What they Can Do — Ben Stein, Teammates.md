# Shipping Products When You Don't Know What they Can Do — Ben Stein, Teammates

**Video URL:** https://www.youtube.com/watch?v=PthmdT92qNg

---

## Executive Summary

Ben Stein, founder of Teammates, shares the fundamental challenges of building and shipping AI agent products when you can't predict what they'll do. He discusses how product management is undergoing a profound transformation in the age of LLMs - from defining specific features to thinking in affordances, from deterministic specs to probabilistic evals, and from prescriptive roadmaps to discovering emergent behaviors. Through practical examples with "Stacy" (their AI teammate), Ben explores new tools and mindsets needed: using evals as product specs, vibe coding for prototyping experiences, accepting probabilistic outcomes, and co-creating the future with customers who understand the experimental nature of autonomous agents.

---

## Main Topics

### [Introduction and The Google Doc Comment Problem](https://www.youtube.com/watch?v=PthmdT92qNg&t=16s)
- Introduces Teammates platform for designing digital workforces
- Stacy the AI teammate who has Google Workspace and Slack accounts
- Customer asks: "Can I tag my teammate in a Google doc comment?"
- Ben realizes he doesn't know what will happen - this becomes the talk's impetus
- Core question: How do you ship products when you don't know what they can do?

### [Why Product Management Must Transform](https://www.youtube.com/watch?v=PthmdT92qNg&t=218s)
- Two fundamental reasons for uncertainty:
  1. Products built on LLMs - we can never fully know what LLMs know
  2. Customer expectations are boundless with free text interfaces
- This creates "boundless surface area built on a product we don't understand"
- Traditional PM practices won't work in this new paradigm

### [Mindset Shift #1: Think in Affordances, Not Features](https://www.youtube.com/watch?v=PthmdT92qNg&t=362s)
- Stop speccing out "if user does X, then Y happens"
- Instead think: "She has affordances to communicate, to collaborate"
- Trust the LLMs and agentic workflows to figure out implementation
- Example: Not "reply to Google Doc comments" but "affordances to comment/email/collaborate"
- Product people must think about capabilities, not individual features

### [Mindset Shift #2: Behavior is Emergent](https://www.youtube.com/watch?v=PthmdT92qNg&t=407s)
- Functionality emerges in unexpected ways
- Job becomes discovering what's possible, not prescribing it
- Focus on providing the right "Lego bricks" for composition
- "Building things and then discovering what they can do themselves"
- Most exciting time to build because of emergent discoveries

### [Mindset Shift #3: New Communication Challenges](https://www.youtube.com/watch?v=PthmdT92qNg&t=460s)
- How to communicate product behavior to engineering teams?
- Traditional specs (Figma, PRDs) lack affordances for probabilistic behavior
- Can't specify "talk less Gen Alpha" or "be appropriately snarky"
- Need new ways to express behavioral expectations

### [Practical Tool #1: Evals as Product Specs](https://www.youtube.com/watch?v=PthmdT92qNg&t=488s)
- Survey reveals: Many engineers write evals, fewer PMs have visibility
- Evals = testing framework for probabilistic AI agents
- Example: "She should be snarky but not mean 80% of the time"
- **Key insight: Evals are the only way we know what our software can do**
- Evals become the new product specification
- Product people should be looking at and writing evals
- Reminiscent of behavior-driven development, but this time it's actually necessary

### [Practical Tool #2: Vibe Coding for Prototyping](https://www.youtube.com/watch?v=PthmdT92qNg&t=649s)
- Hard to write specs for agent experiences on blank paper
- Human-computer interaction is visceral - you have to feel it
- Example: "Ask many clarifying questions" sounded good but users hated it
- Vibe coding lets you prototype and experience the interaction quickly
- **Warning**: Don't use vibe coding to shame engineering ("I built it in the meeting, why does it take you 2 weeks?")
- It's for feeling the experience, never for production
- Example: Claude's "certainly" repetition - seemed good at first, annoying after repeated use

### [Practical Tool #3: Discovering Functionality](https://www.youtube.com/watch?v=PthmdT92qNg&t=780s)
- Classic QA joke: Engineer tests ordering beers (1, 2, 0, -1, lizard, emoji) - bar ready to open
- First customer asks "where's the bathroom?" - bar explodes
- Similar experience with AI agents - try crazy ideas, discover emergent behavior
- Examples: Posting to LinkedIn, reacting to Spotify tracks
- Growth mindset: "Let's experiment" rather than "write the requirements"

### [Challenge: What Counts as a Bug?](https://www.youtube.com/watch?v=PthmdT92qNg&t=853s)
- "She used too many emojis" - is that a bug?
- "Show me in the spec where you said not to use too many emojis"
- Need new ticket status: "Closed - LLMs be crazy, yo"
- Probabilistically generated output makes right/wrong unclear
- Solution: Make evals the spec with clear thresholds (e.g., "must pass 90% of time")
- Need to build credibility around probabilistic acceptance criteria
- This was totally unexpected - even debugging becomes controversial

### [Challenge: Talking to Customers](https://www.youtube.com/watch?v=PthmdT92qNg&t=962s)
- Traditional PM roles in customer meetings:
  1. **Visionary**: Share roadmap and future vision
  2. **Honest broker**: Tell them what's real vs. vaporware
- Problem: Future sounds like witchcraft, present is "I don't know"
- Can't play either traditional role effectively
- **2025 Solution**: "We're inventing the future together"
- Position as co-creation, pulling the future forward
- Not false flattery - genuinely need to figure it out together
- If customers expect something different, it's not time for them to adopt yet

### [Conclusion: The New World of Product Development](https://www.youtube.com/watch?v=PthmdT92qNg&t=1097s)
- Never had more fun building, never felt more inept and excited simultaneously
- Jaw-dropping moments when agents do unexpected things
- Models get smarter automatically when upgraded - agents start checking their own work
- Product discipline changing faster than we expect
- Core ideas still apply (listen to customers, solve real problems)
- But tools and techniques we've relied on are getting upended
- Need to forget much of what we knew and adapt to probabilistic products

---

## Key Takeaways

1. **Shift from features to affordances** - Think about capabilities and trust the AI to figure out implementation
2. **Evals are your new specs** - They're the only way to know what probabilistic products can do
3. **Vibe code to prototype experiences** - You can't design AI interactions on paper; you must feel them
4. **Embrace emergent behavior** - Build blocks and discover what's possible rather than prescribing everything
5. **Co-create with customers** - Position as inventing the future together, not selling a known product
6. **Accept probabilistic outcomes** - 80-90% success rates may be acceptable depending on use case
7. **Redefine "bugs"** - Need new frameworks for what's fixable vs. inherent in probabilistic systems

---

**Last updated:** January 2, 2026
