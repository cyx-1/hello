# Vibes won't cut it — Chris Kelly, Augment Code

**Video URL:** https://www.youtube.com/watch?v=Dc3qOA9WOnE

---

## Executive Summary

Chris Kelly from Augment Code delivers a pragmatic talk challenging the hype around AI replacing software engineers. He argues that while AI coding tools are powerful, "vibe coding" (blindly accepting AI-generated code without review) won't work for production systems. Kelly emphasizes that software engineering is fundamentally about making thousands of decisions and safely changing code, not just generating it. He advocates for treating AI as a tool that requires the same engineering rigor as human developers - proper testing, code review, reproducible environments, and clear documentation. The talk provides practical tips for professional engineers to effectively adopt AI tools while maintaining production-quality standards.

---

## Topics

### 1. [Why Software Engineers Won't Be Replaced](https://www.youtube.com/watch?v=Dc3qOA9WOnE&t=17s)
*Timestamp: 00:17 - 03:00*

**Key Points:**
- Challenges the hype that half of engineers will be gone within a year
- AI-generated code is still code that needs to run in production
- Large companies work in established codebases where most architectural decisions are already made
- Complex systems have emergent behavior that don't show up in individual lines of code
- History repeats: DevOps transformation didn't eliminate sysadmins, it elevated them
- Analogy: "Tractors didn't get rid of farms, they just got rid of farm hands and horses"

### 2. [What is Vibe Coding and Why It Fails](https://www.youtube.com/watch?v=Dc3qOA9WOnE&t=194s)
*Timestamp: 03:14 - 04:47*

**Key Points:**
- Vibe coding: letting AI write all code without examination, just checking if it works
- This approach doesn't work for production systems with high uptime requirements (four nines)
- Production code serves thousands of users with gigabytes of data
- There are nuances in production code that vibes don't capture

### 3. [Code is an Artifact, Not the Job](https://www.youtube.com/watch?v=Dc3qOA9WOnE&t=251s)
*Timestamp: 04:11 - 06:00*

**Key Points:**
- Code is to software engineering what blueprints are to architecture
- Software engineers make thousands of decisions: what packages to use, performance characteristics, architectural patterns
- Quote from Jeff Atwood: "The best code is no code at all"
- Every line of code comes with a maintenance burden
- More code generation doesn't mean better - it means more code to maintain
- LLMs generate patterns, they don't make architectural decisions
- Example: choosing between monolith, microservices, or event-driven systems requires human judgment

### 4. [The Reality of Production Software](https://www.youtube.com/watch?v=Dc3qOA9WOnE&t=361s)
*Timestamp: 06:01 - 07:00*

**Key Points:**
- Real production software is often a "snowflake" with unique idiosyncrasies
- Pattern matching doesn't work when software has unique characteristics
- When software goes down at 2 AM, vibes won't fix the bug - someone needs to diagnose it
- Software engineering is fundamentally about "changing software safely"

### 5. [How to Change Software Safely](https://www.youtube.com/watch?v=Dc3qOA9WOnE&t=420s)
*Timestamp: 07:00 - 08:00*

**Key Points:**
- Traditional methods: personal knowledge, version control, testing, type systems, deployment strategies
- AI can help by understanding more codebase context
- At Augment, they believe context is the most important part of AI code generation
- But context doesn't change the need to care about production

### 6. [Why Professional Engineers Are Slow to Adopt AI](https://www.youtube.com/watch?v=Dc3qOA9WOnE&t=478s)
*Timestamp: 07:58 - 09:00*

**Key Points:**
- Professional software engineers are the last to adopt AI coding tools
- This is unusual - developers typically jump on new innovations (version control, cloud, etc.)
- Kelly worked at GitHub in early days and saw massive adoption of git
- Hypothesis: engineers are skeptical because AI doesn't meet production standards yet

### 7. [The Evolution of AI Coding Tools](https://www.youtube.com/watch?v=Dc3qOA9WOnE&t=511s)
*Timestamp: 08:31 - 09:14*

**Key Points:**
- A few years ago: AI coding was "a pile of bricks" - barely worked
- About a year ago: Claude Sonnet 3.5 caused a massive explosion in AI coding quality
- Four weeks ago: Every AI coding tool announced agents as the future
- The transformation has happened very quickly

### 8. [How to Build Software That's Easy for AI to Write](https://www.youtube.com/watch?v=Dc3qOA9WOnE&t=557s)
*Timestamp: 09:17 - 10:53*

**Key Points:**
- **Document standards and practices**: Which packages to use, document the direction of your codebase
- **Reproducible environments**: Make it easy to spin up developer environments
- **Easy testing**: Can you run tests locally? Is it fast?
- **Clear boundaries**: Don't give vague tasks like "extract this module using the strangler pattern"
- **Clearly defined tasks**: You wouldn't give a human engineer vague instructions, don't give them to AI

**Key Insight:** "This just sounds like software engineering" - if your stack has these qualities, productivity is already better. AI needs the same tools engineers need because it's doing the same job.

### 9. [The Importance of Code Review](https://www.youtube.com/watch?v=Dc3qOA9WOnE&t=680s)
*Timestamp: 11:20 - 12:09*

**Key Points:**
- Code review is the most important skill for the AI era
- Industry has probably forgotten this skill
- Should be interviewing for code review ability, not esoteric LeetCode problems
- Current code review tools are inadequate: lexicographically sorted file lists don't reflect how software actually changes
- Expect a "big explosion" in code review tooling innovation
- This is the skill to brush up on

### 10. [Practical Tips for Using AI Coding Tools](https://www.youtube.com/watch?v=Dc3qOA9WOnE&t=744s)
*Timestamp: 12:24 - 15:26*

**Key Tips:**

1. **AI talks like a human but is a machine** (12:27)
   - Example: AI said "I just scanned the file, I didn't read it" - this isn't how software works
   - LLMs are trained on human communication patterns (emails, excuses)
   - Don't trust everything the LLM says it's doing - it's generating text, not necessarily performing the described action

2. **Sometimes code is just different** (13:26)
   - It's okay if the LLM writes code differently than you would
   - Your coworkers also write code differently
   - Know the difference: is the code *better* or just *different*?
   - This is why we have linters, style guides, and formatters

3. **Write a rules file** (14:06)
   - Start projects with a file describing your stack and guidelines
   - Always include this in the context sent to the LLM
   - Helps ensure consistency

4. **Create-refine loop** (14:23)
   - Create a plan document (markdown)
   - Have the LLM help generate it
   - Save as a markdown file
   - Use that in your context
   - Have the agent work against that file
   - Make your edits and refine
   - Use code completions to tweak specific things
   - Repeat: plan → create → refine
   - More efficient and helps you learn how to prompt effectively

### 11. [Closing Thoughts](https://www.youtube.com/watch?v=Dc3qOA9WOnE&t=915s)
*Timestamp: 15:15 - 15:26*

**Key Points:**
- Augment is available in the expo hall for discussions
- Kelly believes software engineering jobs "aren't going anywhere"
- The role will evolve, not disappear
- Encourages "happy coding" with AI as a tool

---

## Key Takeaways

1. **Vibe coding doesn't work for production** - You need rigorous engineering practices
2. **Software engineering is about decisions, not just code generation** - Architecture, packages, trade-offs
3. **Treat AI like any other engineer** - It needs the same infrastructure, testing, and review processes
4. **Code review is the critical skill** - More important than ever as AI generates more code
5. **AI needs proper context** - Document your standards, practices, and architectural decisions
6. **Accept different coding styles** - Focus on whether code is better, not just different from your style
7. **Use create-refine loops** - Plan first, generate, then iteratively refine
8. **Don't trust AI's explanations blindly** - It generates human-like text but is still a machine

---

## Production Notes

**Speaker:** Chris Kelly, Augment Code
**Event:** AI Engineer Conference
**Duration:** ~15 minutes
**Target Audience:** Professional software engineers considering AI coding tools
**Tone:** Pragmatic, skeptical of hype, focused on production realities
