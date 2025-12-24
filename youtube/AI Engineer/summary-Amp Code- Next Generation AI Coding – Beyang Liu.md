# Amp Code: Next Generation AI Coding – Beyang Liu

**Channel**: AI Engineer  
**Video**: https://youtu.be/gvIAkmZUEZY

## Executive Summary

Beyang Liu, CEO and co-founder of Sourcegraph, presents AMP - an opinionated frontier coding agent designed for developers who want to "live in the future." The talk covers AMP's unique design philosophy, including custom-built terminal and editor interfaces, specialized sub-agents (Finder, Oracle, Librarian, Kraken), and innovative approaches to model selection and cost management. Rather than trying to be everything for everyone, AMP targets developers willing to embrace experimental workflows, featuring novel solutions like terminal ads to subsidize inference costs and a team learning system for continuous improvement.

## Topics

- [Introduction and Philosophy](https://www.youtube.com/watch?v=gvIAkmZUEZY&t=0s) - AMP as an opinionated frontier coding agent, not trying to be for everyone but targeting developers who want to experiment with the future of AI-assisted coding

- [Terminal Interface Design](https://www.youtube.com/watch?v=gvIAkmZUEZY&t=85s) - Custom terminal framework built from scratch (not using existing terminal emulators) to enable new interactions impossible with traditional terminal UIs, including collapsible headers, file previews, and direct file navigation

- [Editor vs Terminal Trade-offs](https://www.youtube.com/watch?v=gvIAkmZUEZY&t=180s) - Why AMP chose terminal-first rather than editor-first approach: terminals allow safer, sandboxed experimentation while editors require more trust; discussion of progressive disclosure and the path to eventual editor integration

- [Sub-Agent Architecture](https://www.youtube.com/watch?v=gvIAkmZUEZY&t=360s) - Four specialized sub-agents working together: Finder (search), Oracle (reasoning), Librarian (external context from Stack Overflow/GitHub), and Kraken (code modifications with unified diff review interface)

- [Model Selection Strategy](https://www.youtube.com/watch?v=gvIAkmZUEZY&t=570s) - Smart agent (Claude 3.7 Sonnet) vs Rush agent (Gemini Flash 2.0) philosophy: using fast, cheaper models for interactive iterations and slower, smarter models for complex planning when users are away

- [Review Interface Optimization](https://www.youtube.com/watch?v=gvIAkmZUEZY&t=720s) - Kraken agent's unified diff view and single-button approval system to minimize developer fatigue from reviewing AI-generated changes; focus on reducing cognitive load

- [Team Learning and Feedback](https://www.youtube.com/watch?v=gvIAkmZUEZY&t=840s) - Innovative feedback system where positive/negative reactions from one developer improve model performance for entire team; crowd-sourced learning from collective developer interactions

- [Cost and Accessibility](https://www.youtube.com/watch?v=gvIAkmZUEZY&t=891s) - Creative solution to inference cost barriers: shipping subtle ads in terminal/editor to sponsor Rush agent inference, making advanced AI coding accessible to students and side projects

- [Community and Target Audience](https://www.youtube.com/watch?v=gvIAkmZUEZY&t=939s) - AMP's focus on frontier developers (Mitchell Hashimoto, Hamill Hussein mentioned as users); Builder community led by Ryan Carson for those experimenting with agents

- [Closing Thoughts](https://www.youtube.com/watch?v=gvIAkmZUEZY&t=1081s) - Invitation to explore AMP's weird and unconventional approach to coding agents; emphasis on thinking differently about AI-assisted development

## Key Takeaways

1. **Opinionated Design**: AMP deliberately targets a small percentage of developers who want to experiment with frontier technology rather than building for mass adoption
2. **Custom UI Framework**: Built their own terminal from scratch to enable interactions impossible with traditional terminal emulators
3. **Specialized Sub-Agents**: Four distinct agents (Finder, Oracle, Librarian, Kraken) each handle specific tasks rather than one monolithic agent
4. **Smart vs Fast Models**: Strategic use of Gemini Flash for interactive work and Claude Sonnet for complex planning when latency is acceptable
5. **Review UX Focus**: Single-button unified diff approvals to combat review fatigue from AI-generated changes
6. **Team Learning**: Individual feedback improves the entire team's model performance through crowd-sourced learning
7. **Ad-Supported Inference**: Novel approach to accessibility - terminal ads subsidize inference costs for students and side projects
8. **Terminal-First Philosophy**: Chose terminals over editors for initial interface due to safety, sandboxing, and lower trust requirements
