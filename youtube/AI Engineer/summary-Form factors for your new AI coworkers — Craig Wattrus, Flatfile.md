# Form factors for your new AI coworkers — Craig Wattrus, Flatfile

**Video URL:** https://www.youtube.com/watch?v=CiMVKnX-CNI

---

## Executive Summary

Craig Wattrus from Flatfile explores different form factors for AI agents in product design, categorizing them into four types: invisible, ambient, inline, and conversational. Drawing from Flatfile's data migration platform, he demonstrates how AI can work at different levels of user interaction - from background automation to direct conversation. The talk emphasizes the importance of "playing" with new AI capabilities to discover emergent behaviors rather than simply automating tedious tasks, and advocates for designing AI agents with specific character traits like being "forward-leaning" (curious, excitable, focused, and completion-oriented).

---

## Topics & Timestamps

### [Introduction: Tools Enabling Collaborative Building](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=17s)
**[00:17 - 01:01]**

- Tools like V0 and Claude Code are making it easier for designers, product people, and engineers to build together
- Removes traditional divides between roles and eliminates need for mockups and click-through prototypes
- Shifts from planning whether something is "worth the engineering effort" to jumping in and feeling the material

### [Flatfile's AI Stack Overview](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=65s)
**[01:05 - 01:55]**

- Flatfile is a developer platform for migrating data between systems
- AI stack components include: customer applications, real-time context (data + validation outcomes), AI agents with tools, and user-facing interfaces
- Four form factor categories: invisible, ambient, inline, and conversational

### [Form Factor 1: Invisible AI](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=118s)
**[01:58 - 02:46]**

- Works completely in the background without user awareness
- Example: When users sign up, AI agents automatically analyze their company, determine their use case (e.g., HR), and generate a customized demo application
- Users don't need to know AI is working behind the scenes

### [Form Factor 2: Ambient AI](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=166s)
**[02:46 - 03:09]**

- Working in the space but not directly in the user's workflow
- Example: Agent analyzing data in background, sparkles appear on columns when opportunities to fix data are found
- User is aware of AI presence but not actively engaging with it

### [Form Factor 3: Inline AI](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=189s)
**[03:09 - 03:32]**

- Integrated directly into the workflow where users are working
- Example: AI agents write code that runs on datasets while user is actively working with the data
- Can handle large datasets (million rows, 50+ columns) with fast execution
- Also applicable to conversational interfaces in some cases

### [Form Factor 4: Conversational AI](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=212s)
**[03:32 - 03:55]**

- Traditional chat-based interfaces users are familiar with
- Example: "Build mode" - a no-code/low-code agentic system that writes Flatfile applications
- Previously required engineers, now accessible to non-technical users

### [Character Coaching vs. Controlling AI](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=235s)
**[03:55 - 04:35]**

- Inspired by Amanda Askell from Anthropic on Lex Fridman podcast about building Claude's character
- Shift from treating AI prompts like design copy (controlling) to being a character coach
- Building the nature and personality of AI agents rather than just controlling their outputs

### [Chat Tuner Prototype: Finding AI Character](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=275s)
**[04:35 - 05:30]**

- Built a "chat tuner" using V0 to experiment with AI character traits
- Focus was on the character development, not the UI
- Creating different personalities and testing how they interact
- Experimentation platform for finding the right agent characteristics

### [Seeking Forward-Leaning AI Characteristics](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=330s)
**[05:30 - 07:00]**

- Goal: Create agents that are "forward-leaning"
- Characteristics: curious, excitable, likes getting things done, very focused
- Balance: Proactive without going too far (avoiding runaway LLM behavior)
- Important to maintain user trust and control

### [Emergence Through Play: Multi-File Processing](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=420s)
**[07:00 - 08:30]**

- Playing with tools to discover emergent behaviors rather than just automating tedious tasks
- Example: Dropped JSON and CSV files into system
- Agent autonomously decided to combine files because data looked similar
- Generated analysis report identifying duplicates and suggesting next steps
- Discovered forward-leaning characteristics through experimentation with Claude 4

### [Knowledge Base Integration Discovery](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=510s)
**[08:30 - 10:30]**

- Gave agents knowledge base of customer call transcripts and documentation
- Expected better/more suggestions from contextual data
- Emergent behavior: Agent recognized when it couldn't fix an issue but knew the solution
- Agent suggested user contact HR to generate missing employee IDs
- Unexpected capability: Helping humans execute tasks the AI couldn't do directly

### [Claude Computer Use Demo](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=630s)
**[10:30 - 10:52]**

- Demonstrated AI agent using computer to accomplish tasks
- Example likely showing autonomous task completion capabilities

### [Cross-Form-Factor Application](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=652s)
**[10:52 - 11:12]**

- Discovered implementations can fit multiple form factors
- Originally conversational flow features work inline as well
- Being integrated into inline transform functionality
- Flexibility in how AI capabilities are surfaced to users

### [Beyond Automation: Seeking Emergence](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=672s)
**[11:12 - 11:48]**

- Risk: Just automating tedious tasks without discovering new possibilities
- Excitement about previous conference talks showing emergent behaviors
- Comparing to early internet days (CSS3, HTML5) when there was lots of experimentation
- Current moment feels like a return to that playful exploration period

### [Pelican on a Bicycle: Future Experiments](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=708s)
**[11:48 - 15:00]**

- "Pelican on a bicycle" = seemingly impractical ideas worth exploring
- Example: LLM-backed autocomplete (probably inefficient but interesting to test)
- Built benchmark comparing 100 different suggestions for data fixes
- Challenge: Finding models that are both fast and accurate for this use case
- Philosophy: Design practice should include building test applications for future form factors
- Importance of feeling materials and testing ideas even if they seem impractical

### [Conclusion: Building New Form Factors](https://www.youtube.com/watch?v=CiMVKnX-CNI&t=920s)
**[15:20 - 15:30]**

- Excitement about discovering new AI form factors
- Encouragement to explore and experiment with AI tools
- Future of product design involves playing with capabilities to see what emerges

---

## Key Takeaways

1. **Four AI Form Factors**: Invisible (background), Ambient (present but not engaged), Inline (integrated in workflow), Conversational (chat-based)

2. **Character Over Control**: Design AI agents through character coaching rather than trying to control every output like traditional UX copy

3. **Forward-Leaning Agents**: Best AI coworkers are curious, excitable, focused, and completion-oriented without going too far

4. **Play to Discover Emergence**: Don't just automate tedious tasks - experiment to find unexpected capabilities and new interaction patterns

5. **Cross-Form-Factor Thinking**: AI capabilities can often work across multiple form factors, not just the original design

6. **Build Test Platforms**: Create your own benchmarks and test applications to feel new materials and design for future capabilities

7. **Knowledge Enables New Behaviors**: Giving agents context (like customer transcripts) can lead to emergent behaviors like helping humans complete tasks the AI can't do directly
