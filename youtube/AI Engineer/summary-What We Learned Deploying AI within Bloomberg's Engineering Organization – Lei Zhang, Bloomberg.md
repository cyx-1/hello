# What We Learned Deploying AI within Bloomberg's Engineering Organization – Lei Zhang, Bloomberg

**Video URL:** https://www.youtube.com/watch?v=Q81AzlA-VE8

---

## Executive Summary

Lei Zhang, who leads Bloomberg's Technology Infrastructure department, shares insights from deploying AI tools across Bloomberg's 9,000+ engineers over the past two years. The talk covers their journey from overwhelming AI tooling options to focused deployment strategies, highlighting successes with uplift agents for code refactoring and incident response agents. Key lessons include: the importance of deterministic verification for AI-generated code, managing increased PR volumes, the shift from "how" to "what" in development workflows, and the critical need for comprehensive telemetry and data platform infrastructure. Bloomberg found the greatest ROI in automating maintenance tasks, incident response, and code migrations rather than greenfield development.

---

## Main Topics

### [Introduction to Bloomberg's Engineering Organization](https://www.youtube.com/watch?v=Q81AzlA-VE8&t=0s)
- **[00:29]** Lei Zhang leads the Technology Infrastructure department at Bloomberg
- **[01:09]** Bloomberg has 9,000+ engineers, mostly software engineers
- **[01:17]** Handles 600+ billion market ticks
- **[01:32]** 500+ employees focused on AI products and research
- **[01:48]** Bloomberg Terminal: flagship product supporting thousands of functions
- **[02:07]** One of the largest private networks in the world
- **[02:12]** One of the largest JavaScript codebases in the world
- **Key Point**: Bloomberg is a massive software organization with complex infrastructure needs

### [The AI Tooling Landscape & Initial Challenges](https://www.youtube.com/watch?v=Q81AzlA-VE8&t=212s)
- **[03:32]** Started AI for coding journey about 2+ years ago
- **[03:49]** Faced overwhelming number of AI coding tools in the market
- **[03:58]** Didn't initially know which AI solutions would help most
- **[04:15]** Key philosophy: "Unless we deploy and try, we wouldn't know what's best"
- **[04:26]** Quickly formed a team to release capabilities for iteration
- **[04:54]** Ran surveys to measure impact on developer productivity
- **Key Point**: Bloomberg took an experimental, measurement-driven approach to AI adoption

### [Early Wins & Limitations](https://www.youtube.com/watch?v=Q81AzlA-VE8&t=296s)
- **[04:56]** Strong results for proof of concepts and test generation
- **[05:05]** Great for one-time scripts
- **[05:09]** Productivity measurements dropped quickly beyond greenfield projects
- **[05:17]** Needed to identify specific use cases for meaningful impact
- **[05:36]** Recognized need to be thoughtful about unleashing powerful tools
- **[05:52]** With hundreds of millions of lines of code, system complexity grows exponentially
- **Key Point**: AI tools worked well for simple tasks but struggled with complex, existing codebases

### [Uplift Agents for Code Evolution](https://www.youtube.com/watch?v=Q81AzlA-VE8&t=409s)
- **[06:56]** Vision: Get a patch PR automatically when a ticket is created
- **[07:13]** Deployed "uplift agents" to scan codebase and apply patches
- **[07:27]** Had regex-based refactoring tools, but LLMs work much better
- **[07:40]** Three main challenges identified:
  - **[07:48]** Need for deterministic verification (tests, linters)
  - **[08:11]** Increased average open PRs and time to merge
  - **[08:29]** Shift from "how" to "what" we want to achieve
- **Key Point**: AI-powered code refactoring shows promise but requires strong verification infrastructure

### [Incident Response Agents](https://www.youtube.com/watch?v=Q81AzlA-VE8&t=531s)
- **[08:58]** Deployed incident response agents for reliability
- **[09:03]** AI tools are fast and unbiased in troubleshooting
- **[09:10]** Can quickly scan: codebase, telemetry, feature flags, call traces
- **[09:24]** Humans often have biased views during troubleshooting
- **[09:32]** Many benefits from deploying agents for incident response
- **[09:37]** Critical challenges:
  - **[09:40]** Need comprehensive telemetry infrastructure
  - **[09:52]** Must ensure agent has access to all relevant data
  - **[10:10]** Requires robust data platform as foundation
- **Key Point**: AI excels at unbiased, rapid incident analysis but depends on comprehensive observability

### [Development Flows & Workflow Optimization](https://www.youtube.com/watch?v=Q81AzlA-VE8&t=628s)
- **[10:28]** Addressed how developers build, test, and deploy
- **[10:40]** Code review and PR management improvements
- **[10:47]** Automated PR summarization for easier reviews
- **[11:00]** Implemented automated test suggestions
- **[11:08]** Focused on improving overall development workflow efficiency
- **Key Point**: AI can streamline development workflows through automation of routine tasks

### [Infrastructure Requirements: Telemetry](https://www.youtube.com/watch?v=Q81AzlA-VE8&t=670s)
- **[11:10]** Two critical infrastructure foundations needed
- **[11:18]** First: Comprehensive telemetry system
- **[11:24]** Must collect metrics, logs, traces across all systems
- **[11:35]** Telemetry enables both incident response and productivity insights
- **[11:45]** Without good telemetry, AI agents have limited effectiveness
- **Key Point**: Comprehensive observability is a prerequisite for effective AI agent deployment

### [Infrastructure Requirements: Data Platform](https://www.youtube.com/watch?v=Q81AzlA-VE8&t=708s)
- **[11:48]** Second foundation: Robust data platform
- **[11:55]** Need to store and query large volumes of telemetry data
- **[12:08]** Data platform enables historical analysis
- **[12:18]** Supports both real-time and batch processing
- **[12:28]** Critical for training and improving AI models
- **Key Point**: A scalable data platform is essential for AI-powered engineering workflows

### [Organizational & Cultural Challenges](https://www.youtube.com/watch?v=Q81AzlA-VE8&t=750s)
- **[12:30]** Developer adoption and trust is critical
- **[12:42]** Need clear guidelines on when to use AI tools
- **[12:55]** Importance of transparency in AI-generated code
- **[13:08]** Training developers to work effectively with AI
- **[13:20]** Managing expectations about AI capabilities and limitations
- **Key Point**: Cultural change and developer education are as important as the technology itself

### [Lessons Learned & Best Practices](https://www.youtube.com/watch?v=Q81AzlA-VE8&t=805s)
- **[13:25]** Start with maintenance and migration tasks, not greenfield
- **[13:38]** Invest in verification infrastructure first
- **[13:50]** Focus on "what" to achieve rather than "how"
- **[14:02]** Measure everything: productivity, PR velocity, merge times
- **[14:15]** Be prepared for increased PR volume
- **[14:28]** Deploy and iterate rather than overthinking upfront
- **Key Point**: Pragmatic, measurement-driven deployment yields better results than perfectionism

### [Future Directions & Q&A](https://www.youtube.com/watch?v=Q81AzlA-VE8&t=870s)
- **[14:30]** Continuing to expand AI agent capabilities
- **[14:45]** Exploring more sophisticated code understanding
- **[14:58]** Looking at AI for architectural decisions
- **[15:10]** Q&A session begins
- **Key Point**: Bloomberg continues to expand AI use cases based on proven successes

---

## Key Takeaways

1. **Start Small, Measure Everything**: Bloomberg took an experimental approach, deploying tools and measuring impact rather than trying to predict success upfront

2. **Infrastructure First**: Comprehensive telemetry and data platforms are prerequisites for successful AI agent deployment

3. **Right Use Cases Matter**: AI excels at maintenance tasks, migrations, and incident response more than greenfield development

4. **Verification is Critical**: Need deterministic verification (tests, linters) to trust AI-generated code at scale

5. **Cultural Shift**: The focus changes from "how to implement" to "what to achieve" when AI handles implementation details

6. **Manage the Downsides**: Be prepared for increased PR volume and longer merge times as AI generates more code

7. **Unbiased Analysis**: AI's lack of bias makes it excellent for incident troubleshooting and code analysis

8. **Iterate Rapidly**: Deploy and learn rather than waiting for perfect solutions

---

**Video Duration:** ~16 minutes
**Speaker:** Lei Zhang, Bloomberg
**Event:** AI Engineer Conference
