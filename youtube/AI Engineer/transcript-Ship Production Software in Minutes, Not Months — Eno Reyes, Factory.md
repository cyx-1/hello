# Ship Production Software in Minutes, Not Months — Eno Reyes, Factory

**Video URL:** https://www.youtube.com/watch?v=iheWKg2Tkrk

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Hi everybody, my name is Eno. I really

**[00:17]** Hi everybody, my name is Eno. I really appreciate that introduction. Um, and

**[00:20]** appreciate that introduction. Um, and

**[00:20]** appreciate that introduction. Um, and maybe I can start with a bit of

**[00:22]** maybe I can start with a bit of

**[00:22]** maybe I can start with a bit of background. Uh, I started working on

**[00:25]** background. Uh, I started working on

**[00:25]** background. Uh, I started working on LLMs about two and a half years ago. uh

**[00:27]** LLMs about two and a half years ago. uh

**[00:27]** LLMs about two and a half years ago. uh when uh GBT3.5

**[00:30]** when uh GBT3.5

**[00:30]** when uh GBT3.5 was coming out and it became

**[00:33]** was coming out and it became

**[00:33]** was coming out and it became increasingly clear that agentic systems

**[00:35]** increasingly clear that agentic systems

**[00:35]** increasingly clear that agentic systems were going to be possible with the help

**[00:37]** were going to be possible with the help

**[00:37]** were going to be possible with the help of LLMs. At factory we believe that the

**[00:41]** of LLMs. At factory we believe that the

**[00:41]** of LLMs. At factory we believe that the way that we use agents in particular to

**[00:44]** way that we use agents in particular to

**[00:44]** way that we use agents in particular to build software is going to radically

**[00:47]** build software is going to radically

**[00:47]** build software is going to radically change the field of software

**[00:48]** change the field of software

**[00:48]** change the field of software development. We're transitioning from

**[00:50]** development. We're transitioning from

**[00:50]** development. We're transitioning from the era of human-driven software

**[00:52]** the era of human-driven software

**[00:52]** the era of human-driven software development to agent-driven development.

**[00:55]** development to agent-driven development.

**[00:55]** development to agent-driven development. You can see glimpses of that today. You

**[00:57]** You can see glimpses of that today. You

**[00:57]** You can see glimpses of that today. You guys have already heard a bunch of great

**[00:59]** guys have already heard a bunch of great

**[00:59]** guys have already heard a bunch of great talks about different ways that agents


### [01:00 - 02:00]

**[01:01]** talks about different ways that agents

**[01:01]** talks about different ways that agents can help with coding in particular.

**[01:04]** can help with coding in particular.

**[01:04]** can help with coding in particular. However, it seems like right now we're

**[01:06]** However, it seems like right now we're

**[01:06]** However, it seems like right now we're still trying to find what that

**[01:08]** still trying to find what that

**[01:08]** still trying to find what that interaction pattern, what that future

**[01:10]** interaction pattern, what that future

**[01:10]** interaction pattern, what that future looks like. And a lot of what's publicly

**[01:12]** looks like. And a lot of what's publicly

**[01:12]** looks like. And a lot of what's publicly available is more or less an incremental

**[01:14]** available is more or less an incremental

**[01:14]** available is more or less an incremental improvement. The current zeitgeist is to

**[01:17]** improvement. The current zeitgeist is to

**[01:17]** improvement. The current zeitgeist is to take tools that were developed 20 years

**[01:18]** take tools that were developed 20 years

**[01:18]** take tools that were developed 20 years ago for humans to write every individual

**[01:21]** ago for humans to write every individual

**[01:21]** ago for humans to write every individual line of code. Um, and ultimately tools

**[01:24]** line of code. Um, and ultimately tools

**[01:24]** line of code. Um, and ultimately tools that were designed first and foremost

**[01:25]** that were designed first and foremost

**[01:26]** that were designed first and foremost for human beings. Uh, and you sprinkle

**[01:28]** for human beings. Uh, and you sprinkle

**[01:28]** for human beings. Uh, and you sprinkle AI on top and then you keep adding

**[01:30]** AI on top and then you keep adding

**[01:30]** AI on top and then you keep adding layers of AI and then at some point

**[01:32]** layers of AI and then at some point

**[01:32]** layers of AI and then at some point maybe there's some step function change

**[01:34]** maybe there's some step function change

**[01:34]** maybe there's some step function change that happens. But there's not a lot of

**[01:35]** that happens. But there's not a lot of

**[01:35]** that happens. But there's not a lot of clarity there in exactly what that

**[01:37]** clarity there in exactly what that

**[01:37]** clarity there in exactly what that means. You know, there's a quote that is

**[01:40]** means. You know, there's a quote that is

**[01:40]** means. You know, there's a quote that is attributed to Henry Ford. Uh, if I had

**[01:43]** attributed to Henry Ford. Uh, if I had

**[01:43]** attributed to Henry Ford. Uh, if I had asked people what they wanted, they

**[01:44]** asked people what they wanted, they

**[01:44]** asked people what they wanted, they would have said faster horses. Now, we

**[01:48]** would have said faster horses. Now, we

**[01:48]** would have said faster horses. Now, we believe that there are some

**[01:49]** believe that there are some

**[01:49]** believe that there are some fundamentally hard problems blocking

**[01:51]** fundamentally hard problems blocking

**[01:51]** fundamentally hard problems blocking organizations from accessing the true

**[01:53]** organizations from accessing the true

**[01:53]** organizations from accessing the true power of AI. This power can only be

**[01:56]** power of AI. This power can only be

**[01:56]** power of AI. This power can only be found when your team is delegating the

**[01:59]** found when your team is delegating the

**[01:59]** found when your team is delegating the majority of their tasks across the


### [02:00 - 03:00]

**[02:01]** majority of their tasks across the

**[02:01]** majority of their tasks across the software life cycle to agents.

**[02:04]** software life cycle to agents.

**[02:04]** software life cycle to agents. To do that, you need a platform that has

**[02:07]** To do that, you need a platform that has

**[02:07]** To do that, you need a platform that has an intuitive interface for managing and

**[02:09]** an intuitive interface for managing and

**[02:09]** an intuitive interface for managing and delegating tasks, centralized context

**[02:12]** delegating tasks, centralized context

**[02:12]** delegating tasks, centralized context from across all your engineering tools

**[02:14]** from across all your engineering tools

**[02:14]** from across all your engineering tools and data sources, agents that

**[02:17]** and data sources, agents that

**[02:17]** and data sources, agents that consistently produce reliable,

**[02:19]** consistently produce reliable,

**[02:19]** consistently produce reliable, highquality outputs, and infrastructure

**[02:22]** highquality outputs, and infrastructure

**[02:22]** highquality outputs, and infrastructure that supports thousands of agents

**[02:24]** that supports thousands of agents

**[02:24]** that supports thousands of agents working in parallel. These are all hard

**[02:27]** working in parallel. These are all hard

**[02:27]** working in parallel. These are all hard problems to solve. But our team has

**[02:29]** problems to solve. But our team has

**[02:29]** problems to solve. But our team has spent the last two years partnering with

**[02:31]** spent the last two years partnering with

**[02:31]** spent the last two years partnering with large organizations to build towards

**[02:34]** large organizations to build towards

**[02:34]** large organizations to build towards this future. This talk is going to serve

**[02:37]** this future. This talk is going to serve

**[02:37]** this future. This talk is going to serve as sort of a deep dive into agentnative

**[02:39]** as sort of a deep dive into agentnative

**[02:39]** as sort of a deep dive into agentnative development and some of the and a bit of

**[02:42]** development and some of the and a bit of

**[02:42]** development and some of the and a bit of a share of some of the lessons that

**[02:43]** a share of some of the lessons that

**[02:44]** a share of some of the lessons that we've learned helping enterprise

**[02:45]** we've learned helping enterprise

**[02:45]** we've learned helping enterprise organizations make the transition to

**[02:47]** organizations make the transition to

**[02:47]** organizations make the transition to agent native development.

**[02:51]** agent native development.

**[02:51]** agent native development. When Andre Karpathy said English is the

**[02:53]** When Andre Karpathy said English is the

**[02:54]** When Andre Karpathy said English is the new programming language, he captured

**[02:55]** new programming language, he captured

**[02:55]** new programming language, he captured this very exciting moment. Right? And if

**[02:58]** this very exciting moment. Right? And if

**[02:58]** this very exciting moment. Right? And if you're to judge AI progress based on

**[02:59]** you're to judge AI progress based on

**[02:59]** you're to judge AI progress based on Twitter, you'd think that, you know, you


### [03:00 - 04:00]

**[03:01]** Twitter, you'd think that, you know, you

**[03:01]** Twitter, you'd think that, you know, you can basically vibe code your way to

**[03:03]** can basically vibe code your way to

**[03:03]** can basically vibe code your way to anything. But vibe coding isn't the

**[03:06]** anything. But vibe coding isn't the

**[03:06]** anything. But vibe coding isn't the approach to solve hard problems. You

**[03:09]** approach to solve hard problems. You

**[03:09]** approach to solve hard problems. You can't vibe code a legacy Java 7 app that

**[03:12]** can't vibe code a legacy Java 7 app that

**[03:12]** can't vibe code a legacy Java 7 app that runs 5% of the world's global bank

**[03:15]** runs 5% of the world's global bank

**[03:15]** runs 5% of the world's global bank transactions, right? You need a little

**[03:17]** transactions, right? You need a little

**[03:17]** transactions, right? You need a little bit more software engineering. So agents

**[03:20]** bit more software engineering. So agents

**[03:20]** bit more software engineering. So agents really should not be thought of as a

**[03:22]** really should not be thought of as a

**[03:22]** really should not be thought of as a replacement for human ingenuity, right?

**[03:24]** replacement for human ingenuity, right?

**[03:24]** replacement for human ingenuity, right? Agents are climbing gear and building

**[03:27]** Agents are climbing gear and building

**[03:27]** Agents are climbing gear and building production software is like scaling

**[03:29]** production software is like scaling

**[03:29]** production software is like scaling Mount Everest. And so while better tools

**[03:33]** Mount Everest. And so while better tools

**[03:33]** Mount Everest. And so while better tools have made this climb more accessible, we

**[03:36]** have made this climb more accessible, we

**[03:36]** have made this climb more accessible, we still need to think about how to

**[03:37]** still need to think about how to

**[03:37]** still need to think about how to leverage them and use our existing

**[03:40]** leverage them and use our existing

**[03:40]** leverage them and use our existing expertise in order to drive this

**[03:42]** expertise in order to drive this

**[03:42]** expertise in order to drive this transformation. I want to start with a

**[03:44]** transformation. I want to start with a

**[03:44]** transformation. I want to start with a quick video of what's possible today,

**[03:47]** quick video of what's possible today,

**[03:47]** quick video of what's possible today, right? And so in this you'll see a quick

**[03:50]** right? And so in this you'll see a quick

**[03:50]** right? And so in this you'll see a quick glimpse of what it's like to delegate a

**[03:52]** glimpse of what it's like to delegate a

**[03:52]** glimpse of what it's like to delegate a task to an agentic system. You can watch

**[03:56]** task to an agentic system. You can watch

**[03:56]** task to an agentic system. You can watch the droid as we call them ingest the

**[03:58]** the droid as we call them ingest the

**[03:58]** the droid as we call them ingest the task and start grounding itself in the


### [04:00 - 05:00]

**[04:01]** task and start grounding itself in the

**[04:01]** task and start grounding itself in the environment. It uses tools to search

**[04:03]** environment. It uses tools to search

**[04:03]** environment. It uses tools to search through the codebase, determine the git

**[04:05]** through the codebase, determine the git

**[04:05]** through the codebase, determine the git branch, check out what the machine has

**[04:08]** branch, check out what the machine has

**[04:08]** branch, check out what the machine has available to it. It looks through recent

**[04:10]** available to it. It looks through recent

**[04:10]** available to it. It looks through recent changes to the codebase. It looks at

**[04:12]** changes to the codebase. It looks at

**[04:12]** changes to the codebase. It looks at memories of its recent interactions with

**[04:14]** memories of its recent interactions with

**[04:14]** memories of its recent interactions with users as well as memories from its

**[04:17]** users as well as memories from its

**[04:17]** users as well as memories from its interactions across the entire

**[04:18]** interactions across the entire

**[04:18]** interactions across the entire organization. And then the droid comes

**[04:21]** organization. And then the droid comes

**[04:21]** organization. And then the droid comes back with a plan and says, "Here's

**[04:23]** back with a plan and says, "Here's

**[04:23]** back with a plan and says, "Here's exactly what I'm going to do, but I'd

**[04:24]** exactly what I'm going to do, but I'd

**[04:24]** exactly what I'm going to do, but I'd like you to clarify a couple of things.

**[04:27]** like you to clarify a couple of things.

**[04:27]** like you to clarify a couple of things. Right? We need to expect our agents to

**[04:29]** Right? We need to expect our agents to

**[04:29]** Right? We need to expect our agents to not just take what we say at face value,

**[04:31]** not just take what we say at face value,

**[04:31]** not just take what we say at face value, but instead question it and make us

**[04:33]** but instead question it and make us

**[04:33]** but instead question it and make us better software developers." And so

**[04:35]** better software developers." And so

**[04:35]** better software developers." And so after the user comes back with that

**[04:36]** after the user comes back with that

**[04:36]** after the user comes back with that info, the droid comes, it executes on

**[04:39]** info, the droid comes, it executes on

**[04:39]** info, the droid comes, it executes on that task. It leverages its tools to

**[04:42]** that task. It leverages its tools to

**[04:42]** that task. It leverages its tools to write code, runs pre-commit hooks,

**[04:44]** write code, runs pre-commit hooks,

**[04:44]** write code, runs pre-commit hooks, lints, and ultimately generates a pull

**[04:46]** lints, and ultimately generates a pull

**[04:46]** lints, and ultimately generates a pull request that passes CI.

**[04:52]** But how can you achieve outcomes like

**[04:52]** But how can you achieve outcomes like this on a regular basis? Right? It's

**[04:54]** this on a regular basis? Right? It's

**[04:54]** this on a regular basis? Right? It's nice when it works, but what about when

**[04:56]** nice when it works, but what about when

**[04:56]** nice when it works, but what about when it fails? At the heart of effective AI

**[04:59]** it fails? At the heart of effective AI

**[04:59]** it fails? At the heart of effective AI assisted development lies a very


### [05:00 - 06:00]

**[05:00]** assisted development lies a very

**[05:00]** assisted development lies a very fundamental truth. AI tools are only as

**[05:03]** fundamental truth. AI tools are only as

**[05:03]** fundamental truth. AI tools are only as good as the context that they receive.

**[05:06]** good as the context that they receive.

**[05:06]** good as the context that they receive. So much of what people are calling

**[05:07]** So much of what people are calling

**[05:07]** So much of what people are calling prompt engineering is really mentally

**[05:10]** prompt engineering is really mentally

**[05:10]** prompt engineering is really mentally modeling this alien intelligence that

**[05:12]** modeling this alien intelligence that

**[05:12]** modeling this alien intelligence that has a slice of context of the real

**[05:14]** has a slice of context of the real

**[05:14]** has a slice of context of the real world. And if you start thinking about

**[05:16]** world. And if you start thinking about

**[05:16]** world. And if you start thinking about your AI tools this way, you're going to

**[05:18]** your AI tools this way, you're going to

**[05:18]** your AI tools this way, you're going to start to get a lot better at interacting

**[05:20]** start to get a lot better at interacting

**[05:20]** start to get a lot better at interacting with them. We've investigated thousands

**[05:22]** with them. We've investigated thousands

**[05:22]** with them. We've investigated thousands of droid assisted development sessions

**[05:25]** of droid assisted development sessions

**[05:25]** of droid assisted development sessions and you see this sort of heristic emerge

**[05:27]** and you see this sort of heristic emerge

**[05:27]** and you see this sort of heristic emerge where AI is most likely failing to solve

**[05:30]** where AI is most likely failing to solve

**[05:30]** where AI is most likely failing to solve the problem. Not because the LLMs aren't

**[05:33]** the problem. Not because the LLMs aren't

**[05:33]** the problem. Not because the LLMs aren't good enough, but because it's missing

**[05:34]** good enough, but because it's missing

**[05:34]** good enough, but because it's missing crucial context that's required to truly

**[05:37]** crucial context that's required to truly

**[05:37]** crucial context that's required to truly solve it. And better models are going to

**[05:39]** solve it. And better models are going to

**[05:39]** solve it. And better models are going to make this happen less often. But the

**[05:41]** make this happen less often. But the

**[05:41]** make this happen less often. But the real solution is not just making the AI

**[05:43]** real solution is not just making the AI

**[05:43]** real solution is not just making the AI smarter. It's going to be getting better

**[05:46]** smarter. It's going to be getting better

**[05:46]** smarter. It's going to be getting better at providing these systems with that

**[05:48]** at providing these systems with that

**[05:48]** at providing these systems with that missing context.

**[05:50]** missing context.

**[05:50]** missing context. LM don't know about your morning

**[05:52]** LM don't know about your morning

**[05:52]** LM don't know about your morning standup. They don't know about the

**[05:54]** standup. They don't know about the

**[05:54]** standup. They don't know about the meeting that you had at Hawk and the

**[05:56]** meeting that you had at Hawk and the

**[05:56]** meeting that you had at Hawk and the whiteboard that you did, right? But you

**[05:58]** whiteboard that you did, right? But you

**[05:58]** whiteboard that you did, right? But you can give those things to the LLM if you


### [06:00 - 07:00]

**[06:00]** can give those things to the LLM if you

**[06:00]** can give those things to the LLM if you transcribe your notes, if you take a

**[06:02]** transcribe your notes, if you take a

**[06:02]** transcribe your notes, if you take a photo and you upload it, right? You have

**[06:05]** photo and you upload it, right? You have

**[06:05]** photo and you upload it, right? You have to start thinking about these things not

**[06:06]** to start thinking about these things not

**[06:06]** to start thinking about these things not as tools, but as something in between a

**[06:10]** as tools, but as something in between a

**[06:10]** as tools, but as something in between a co-worker and uh and and a platform,

**[06:13]** co-worker and uh and and a platform,

**[06:13]** co-worker and uh and and a platform, right? And if you can get that context

**[06:16]** right? And if you can get that context

**[06:16]** right? And if you can get that context that lies in the cracks between systems,

**[06:18]** that lies in the cracks between systems,

**[06:18]** that lies in the cracks between systems, you use platforms that integrate

**[06:20]** you use platforms that integrate

**[06:20]** you use platforms that integrate natively with all of your data sources

**[06:22]** natively with all of your data sources

**[06:22]** natively with all of your data sources and you have agents that can actually

**[06:24]** and you have agents that can actually

**[06:24]** and you have agents that can actually make use of those things, you can start

**[06:26]** make use of those things, you can start

**[06:26]** make use of those things, you can start actually driving this transition to

**[06:28]** actually driving this transition to

**[06:28]** actually driving this transition to agent native development.

**[06:30]** agent native development.

**[06:30]** agent native development. I want to talk a bit as well about

**[06:32]** I want to talk a bit as well about

**[06:32]** I want to talk a bit as well about planning and design. When your agent I

**[06:35]** planning and design. When your agent I

**[06:35]** planning and design. When your agent I mean sorry when your organization is

**[06:37]** mean sorry when your organization is

**[06:37]** mean sorry when your organization is doing agent native development then you

**[06:39]** doing agent native development then you

**[06:39]** doing agent native development then you are using agents at every stage. Droids

**[06:42]** are using agents at every stage. Droids

**[06:42]** are using agents at every stage. Droids don't just write code. They can help

**[06:45]** don't just write code. They can help

**[06:45]** don't just write code. They can help with that part, but the hardest thing

**[06:47]** with that part, but the hardest thing

**[06:47]** with that part, but the hardest thing about software development is not the

**[06:48]** about software development is not the

**[06:48]** about software development is not the code. It's about figuring out exactly

**[06:50]** code. It's about figuring out exactly

**[06:50]** code. It's about figuring out exactly what to build. Here you can watch a

**[06:53]** what to build. Here you can watch a

**[06:53]** what to build. Here you can watch a droid as it's tasked with trying to find

**[06:56]** droid as it's tasked with trying to find

**[06:56]** droid as it's tasked with trying to find the most up-to-date information about a

**[06:57]** the most up-to-date information about a

**[06:57]** the most up-to-date information about a new model release and integrate that

**[06:59]** new model release and integrate that

**[06:59]** new model release and integrate that into an existing chat application. It's


### [07:00 - 08:00]

**[07:02]** into an existing chat application. It's

**[07:02]** into an existing chat application. It's going to leverage internet search, its

**[07:04]** going to leverage internet search, its

**[07:04]** going to leverage internet search, its knowledge of your codebase, its

**[07:05]** knowledge of your codebase, its

**[07:06]** knowledge of your codebase, its understanding of your product goals from

**[07:07]** understanding of your product goals from

**[07:07]** understanding of your product goals from its organ uh memory, and its

**[07:10]** its organ uh memory, and its

**[07:10]** its organ uh memory, and its understanding of your technical

**[07:11]** understanding of your technical

**[07:11]** understanding of your technical architecture from the design doc you

**[07:13]** architecture from the design doc you

**[07:13]** architecture from the design doc you wrote last week. Planning with AI is

**[07:16]** wrote last week. Planning with AI is

**[07:16]** wrote last week. Planning with AI is fundamentally different from planning

**[07:18]** fundamentally different from planning

**[07:18]** fundamentally different from planning alone. It's not necessarily just asking

**[07:21]** alone. It's not necessarily just asking

**[07:21]** alone. It's not necessarily just asking please build this thing for me or give

**[07:23]** please build this thing for me or give

**[07:23]** please build this thing for me or give me the design doc but instead it's about

**[07:26]** me the design doc but instead it's about

**[07:26]** me the design doc but instead it's about delegating the groundwork and the

**[07:28]** delegating the groundwork and the

**[07:28]** delegating the groundwork and the research to AI agents then using a

**[07:31]** research to AI agents then using a

**[07:31]** research to AI agents then using a collaborative platform to interact and

**[07:33]** collaborative platform to interact and

**[07:34]** collaborative platform to interact and explore possibilities together. That is

**[07:36]** explore possibilities together. That is

**[07:36]** explore possibilities together. That is how you get better at planning with

**[07:38]** how you get better at planning with

**[07:38]** how you get better at planning with agents.

**[07:40]** agents.

**[07:40]** agents. Now you can see here we have a nice

**[07:42]** Now you can see here we have a nice

**[07:42]** Now you can see here we have a nice document, a nice plan. You could export

**[07:44]** document, a nice plan. You could export

**[07:44]** document, a nice plan. You could export that to notion, Confluence, Jira, any of

**[07:47]** that to notion, Confluence, Jira, any of

**[07:47]** that to notion, Confluence, Jira, any of your integrations with no setup because

**[07:49]** your integrations with no setup because

**[07:49]** your integrations with no setup because MCP is great, but having every developer

**[07:51]** MCP is great, but having every developer

**[07:51]** MCP is great, but having every developer have to install a bunch of servers,

**[07:53]** have to install a bunch of servers,

**[07:53]** have to install a bunch of servers, click a bunch of things, pass around the

**[07:55]** click a bunch of things, pass around the

**[07:55]** click a bunch of things, pass around the API key is not necessarily ideal. And so

**[07:58]** API key is not necessarily ideal. And so

**[07:58]** API key is not necessarily ideal. And so platforms are going to evolve and solve


### [08:00 - 09:00]

**[08:00]** platforms are going to evolve and solve

**[08:00]** platforms are going to evolve and solve a lot of these problems. But in the

**[08:02]** a lot of these problems. But in the

**[08:02]** a lot of these problems. But in the meantime, you do have droids. And now a

**[08:06]** meantime, you do have droids. And now a

**[08:06]** meantime, you do have droids. And now a little bit more on this. The real unlock

**[08:09]** little bit more on this. The real unlock

**[08:09]** little bit more on this. The real unlock for AI transforming your organization in

**[08:13]** for AI transforming your organization in

**[08:13]** for AI transforming your organization in with respect to planning is going to be

**[08:15]** with respect to planning is going to be

**[08:15]** with respect to planning is going to be when you start standardizing the way

**[08:17]** when you start standardizing the way

**[08:17]** when you start standardizing the way that your organization thinks, right?

**[08:19]** that your organization thinks, right?

**[08:19]** that your organization thinks, right? And so there's a bit of a of an example

**[08:22]** And so there's a bit of a of an example

**[08:22]** And so there's a bit of a of an example that we just had a couple of weeks ago

**[08:23]** that we just had a couple of weeks ago

**[08:24]** that we just had a couple of weeks ago while we were planning out uh a feature

**[08:26]** while we were planning out uh a feature

**[08:26]** while we were planning out uh a feature related to our cloud development

**[08:27]** related to our cloud development

**[08:27]** related to our cloud development environments. We got a lot of feedback

**[08:30]** environments. We got a lot of feedback

**[08:30]** environments. We got a lot of feedback from users and so we had about three

**[08:32]** from users and so we had about three

**[08:32]** from users and so we had about three months of user transcripts, people from

**[08:34]** months of user transcripts, people from

**[08:34]** months of user transcripts, people from enterprises, uh, individuals that we

**[08:37]** enterprises, uh, individuals that we

**[08:37]** enterprises, uh, individuals that we knew. Uh, we transcribe every single

**[08:39]** knew. Uh, we transcribe every single

**[08:39]** knew. Uh, we transcribe every single interaction and meeting at factory. We

**[08:41]** interaction and meeting at factory. We

**[08:41]** interaction and meeting at factory. We take those notes and we combine them

**[08:43]** take those notes and we combine them

**[08:43]** take those notes and we combine them with a droid that has access to our

**[08:45]** with a droid that has access to our

**[08:46]** with a droid that has access to our architecture. We take a ad hoc meeting

**[08:49]** architecture. We take a ad hoc meeting

**[08:49]** architecture. We take a ad hoc meeting that one of our engineers took a granola

**[08:51]** that one of our engineers took a granola

**[08:51]** that one of our engineers took a granola of. If you guys use granola, I love that

**[08:53]** of. If you guys use granola, I love that

**[08:53]** of. If you guys use granola, I love that tool. Um, and we throw that all to the

**[08:56]** tool. Um, and we throw that all to the

**[08:56]** tool. Um, and we throw that all to the knowledge droid and we say, we don't

**[08:58]** knowledge droid and we say, we don't

**[08:58]** knowledge droid and we say, we don't say, "Let's plan the feature out." We


### [09:00 - 10:00]

**[09:01]** say, "Let's plan the feature out." We

**[09:01]** say, "Let's plan the feature out." We say, "Could you find any patterns in the

**[09:03]** say, "Could you find any patterns in the

**[09:03]** say, "Could you find any patterns in the customer feedback that map up to our

**[09:05]** customer feedback that map up to our

**[09:05]** customer feedback that map up to our assumptions? Can you highlight any

**[09:08]** assumptions? Can you highlight any

**[09:08]** assumptions? Can you highlight any technical constraints with what we have

**[09:09]** technical constraints with what we have

**[09:10]** technical constraints with what we have today that might help us make this

**[09:12]** today that might help us make this

**[09:12]** today that might help us make this better?" And then we take all of that

**[09:14]** better?" And then we take all of that

**[09:14]** better?" And then we take all of that output, those documents, there's maybe

**[09:17]** output, those documents, there's maybe

**[09:17]** output, those documents, there's maybe four or five intermediate results here,

**[09:19]** four or five intermediate results here,

**[09:19]** four or five intermediate results here, and that's what we use to start

**[09:21]** and that's what we use to start

**[09:21]** and that's what we use to start iterating on a final PRD that helps us

**[09:23]** iterating on a final PRD that helps us

**[09:24]** iterating on a final PRD that helps us outline the full feature.

**[09:26]** outline the full feature.

**[09:26]** outline the full feature. You can take that PRD and if you have a

**[09:29]** You can take that PRD and if you have a

**[09:29]** You can take that PRD and if you have a droid that has access to linear and Jira

**[09:31]** droid that has access to linear and Jira

**[09:31]** droid that has access to linear and Jira with tools to create tickets, create

**[09:33]** with tools to create tickets, create

**[09:34]** with tools to create tickets, create epics, modify those things, then that

**[09:36]** epics, modify those things, then that

**[09:36]** epics, modify those things, then that PRD can be turned into a road map. eight

**[09:40]** PRD can be turned into a road map. eight

**[09:40]** PRD can be turned into a road map. eight tickets. This ticket's dependent on that

**[09:42]** tickets. This ticket's dependent on that

**[09:42]** tickets. This ticket's dependent on that ticket, but ultimately work that can be

**[09:45]** ticket, but ultimately work that can be

**[09:45]** ticket, but ultimately work that can be parallelized amongst a group of eight

**[09:47]** parallelized amongst a group of eight

**[09:47]** parallelized amongst a group of eight code droids, right? And so this is how

**[09:51]** code droids, right? And so this is how

**[09:51]** code droids, right? And so this is how software is going to evolve. We're going

**[09:52]** software is going to evolve. We're going

**[09:52]** software is going to evolve. We're going to move from executing to orchestrating

**[09:55]** to move from executing to orchestrating

**[09:56]** to move from executing to orchestrating systems that work on our behalf.

**[09:59]** systems that work on our behalf.

**[09:59]** systems that work on our behalf. I tal I talked about a couple of these.


### [10:00 - 11:00]

**[10:01]** I tal I talked about a couple of these.

**[10:01]** I tal I talked about a couple of these. I think PRDs, edge design docs, RCA

**[10:04]** I think PRDs, edge design docs, RCA

**[10:04]** I think PRDs, edge design docs, RCA templates, quarterly engine and product

**[10:06]** templates, quarterly engine and product

**[10:06]** templates, quarterly engine and product road maps, right? transcriptions of your

**[10:09]** road maps, right? transcriptions of your

**[10:09]** road maps, right? transcriptions of your meetings. Normally, you might see this

**[10:11]** meetings. Normally, you might see this

**[10:11]** meetings. Normally, you might see this stuff as a burden, but when your company

**[10:13]** stuff as a burden, but when your company

**[10:13]** stuff as a burden, but when your company is doing agentnative software

**[10:15]** is doing agentnative software

**[10:15]** is doing agentnative software development, your process and your

**[10:17]** development, your process and your

**[10:17]** development, your process and your documentation is a knowledge base and a

**[10:19]** documentation is a knowledge base and a

**[10:19]** documentation is a knowledge base and a map for your droids to learn and imitate

**[10:22]** map for your droids to learn and imitate

**[10:22]** map for your droids to learn and imitate the way that your team thinks. This

**[10:25]** the way that your team thinks. This

**[10:25]** the way that your team thinks. This documentation and process is a

**[10:28]** documentation and process is a

**[10:28]** documentation and process is a conversation with both future developers

**[10:30]** conversation with both future developers

**[10:30]** conversation with both future developers as well as future AI systems. And so if

**[10:34]** as well as future AI systems. And so if

**[10:34]** as well as future AI systems. And so if you can communicate that why behind the

**[10:36]** you can communicate that why behind the

**[10:36]** you can communicate that why behind the decision, that context for those future

**[10:39]** decision, that context for those future

**[10:39]** decision, that context for those future developers and agents, then you'll start

**[10:41]** developers and agents, then you'll start

**[10:41]** developers and agents, then you'll start to see that there's a huge lift in their

**[10:43]** to see that there's a huge lift in their

**[10:43]** to see that there's a huge lift in their ability to natively work the way that

**[10:45]** ability to natively work the way that

**[10:46]** ability to natively work the way that your team actually works.

**[10:49]** your team actually works.

**[10:49]** your team actually works. I want to talk about uh agent-driven

**[10:52]** I want to talk about uh agent-driven

**[10:52]** I want to talk about uh agent-driven development with respect to site

**[10:53]** development with respect to site

**[10:53]** development with respect to site reliability engineering.

**[10:56]** reliability engineering.

**[10:56]** reliability engineering. There is a lot that goes in to a real

**[10:59]** There is a lot that goes in to a real

**[10:59]** There is a lot that goes in to a real incident response. It would be crazy for


### [11:00 - 12:00]

**[11:02]** incident response. It would be crazy for

**[11:02]** incident response. It would be crazy for me to go up here and say you could

**[11:03]** me to go up here and say you could

**[11:03]** me to go up here and say you could actually just automate all of S and RCA

**[11:06]** actually just automate all of S and RCA

**[11:06]** actually just automate all of S and RCA work today, but there is a difference in

**[11:08]** work today, but there is a difference in

**[11:08]** work today, but there is a difference in the AI agent-driven approach. Right

**[11:11]** the AI agent-driven approach. Right

**[11:11]** the AI agent-driven approach. Right here, we're watching a droid take a

**[11:13]** here, we're watching a droid take a

**[11:13]** here, we're watching a droid take a sentry incident and convert it into a

**[11:15]** sentry incident and convert it into a

**[11:15]** sentry incident and convert it into a full RCA and mitigation plan.

**[11:18]** full RCA and mitigation plan.

**[11:18]** full RCA and mitigation plan. Traditional incident response is

**[11:20]** Traditional incident response is

**[11:20]** Traditional incident response is effectively solving a puzzle. The pieces

**[11:23]** effectively solving a puzzle. The pieces

**[11:23]** effectively solving a puzzle. The pieces are scattered across dozens of systems,

**[11:25]** are scattered across dozens of systems,

**[11:25]** are scattered across dozens of systems, logs in one place, metrics in another,

**[11:28]** logs in one place, metrics in another,

**[11:28]** logs in one place, metrics in another, historical context somewhere else.

**[11:30]** historical context somewhere else.

**[11:30]** historical context somewhere else. There's knowledge in your team's head.

**[11:32]** There's knowledge in your team's head.

**[11:32]** There's knowledge in your team's head. Droids in your organization

**[11:34]** Droids in your organization

**[11:34]** Droids in your organization fundamentally change this, right? When

**[11:36]** fundamentally change this, right? When

**[11:36]** fundamentally change this, right? When an alert triggers, you can pull in

**[11:38]** an alert triggers, you can pull in

**[11:38]** an alert triggers, you can pull in context from relevant system logs, past

**[11:40]** context from relevant system logs, past

**[11:40]** context from relevant system logs, past incident, runbooks in notion or

**[11:43]** incident, runbooks in notion or

**[11:43]** incident, runbooks in notion or confluence, team discussions from Slack.

**[11:45]** confluence, team discussions from Slack.

**[11:45]** confluence, team discussions from Slack. And you can see that a droid that has

**[11:47]** And you can see that a droid that has

**[11:47]** And you can see that a droid that has the tools and the ability to access this

**[11:50]** the tools and the ability to access this

**[11:50]** the tools and the ability to access this can condense that search effort from

**[11:53]** can condense that search effort from

**[11:53]** can condense that search effort from hours to minutes. And so really the

**[11:55]** hours to minutes. And so really the

**[11:55]** hours to minutes. And so really the acceptable time to act for a standard

**[11:59]** acceptable time to act for a standard

**[11:59]** acceptable time to act for a standard enterprise organization should really


### [12:00 - 13:00]

**[12:01]** enterprise organization should really

**[12:01]** enterprise organization should really it's really going to be zero. Right? The

**[12:03]** it's really going to be zero. Right? The

**[12:03]** it's really going to be zero. Right? The moment that an incident happens, you

**[12:04]** moment that an incident happens, you

**[12:04]** moment that an incident happens, you should have a droid that's telling you

**[12:06]** should have a droid that's telling you

**[12:06]** should have a droid that's telling you exactly what happened, exactly how to

**[12:08]** exactly what happened, exactly how to

**[12:08]** exactly what happened, exactly how to fix it. And the thing that gets

**[12:10]** fix it. And the thing that gets

**[12:10]** fix it. And the thing that gets interesting is when you have user and

**[12:12]** interesting is when you have user and

**[12:12]** interesting is when you have user and organization level memory, you really

**[12:14]** organization level memory, you really

**[12:14]** organization level memory, you really start to build a model of what your

**[12:16]** start to build a model of what your

**[12:16]** start to build a model of what your team's response patterns and common

**[12:18]** team's response patterns and common

**[12:18]** team's response patterns and common issues are. And so it's not just

**[12:20]** issues are. And so it's not just

**[12:20]** issues are. And so it's not just generating runbooks or generating a

**[12:22]** generating runbooks or generating a

**[12:22]** generating runbooks or generating a mitigation for one incident, right? but

**[12:24]** mitigation for one incident, right? but

**[12:24]** mitigation for one incident, right? but creating new processes that help solve

**[12:27]** creating new processes that help solve

**[12:27]** creating new processes that help solve some of these issues.

**[12:29]** some of these issues.

**[12:29]** some of these issues. And once you've written that RCA, right,

**[12:32]** And once you've written that RCA, right,

**[12:32]** And once you've written that RCA, right, you you can move on to generate runbooks

**[12:35]** you you can move on to generate runbooks

**[12:35]** you you can move on to generate runbooks for those new learned patterns, update

**[12:37]** for those new learned patterns, update

**[12:37]** for those new learned patterns, update existing response workflows,

**[12:40]** existing response workflows,

**[12:40]** existing response workflows, capture team knowledge that gets shared

**[12:42]** capture team knowledge that gets shared

**[12:42]** capture team knowledge that gets shared automatically without without the need

**[12:44]** automatically without without the need

**[12:44]** automatically without without the need for manual curation.

**[12:46]** for manual curation.

**[12:46]** for manual curation. And this is why all these things are

**[12:48]** And this is why all these things are

**[12:48]** And this is why all these things are connected. Agentnative incident response

**[12:51]** connected. Agentnative incident response

**[12:51]** connected. Agentnative incident response is a part of a larger learning cycle

**[12:54]** is a part of a larger learning cycle

**[12:54]** is a part of a larger learning cycle that happens when you start to integrate

**[12:56]** that happens when you start to integrate

**[12:56]** that happens when you start to integrate agents into the workflow. We're seeing

**[12:58]** agents into the workflow. We're seeing

**[12:58]** agents into the workflow. We're seeing teams that are able to cut incident


### [13:00 - 14:00]

**[13:00]** teams that are able to cut incident

**[13:00]** teams that are able to cut incident response time in half because context is

**[13:03]** response time in half because context is

**[13:03]** response time in half because context is immediate. They're able to reduce repeat

**[13:06]** immediate. They're able to reduce repeat

**[13:06]** immediate. They're able to reduce repeat incidents because the third time

**[13:07]** incidents because the third time

**[13:07]** incidents because the third time something happens, the droid starts to

**[13:09]** something happens, the droid starts to

**[13:09]** something happens, the droid starts to say, "Maybe we should fix this." And

**[13:12]** say, "Maybe we should fix this." And

**[13:12]** say, "Maybe we should fix this." And they're able to improve team

**[13:13]** they're able to improve team

**[13:13]** they're able to improve team collaboration because when a new

**[13:16]** collaboration because when a new

**[13:16]** collaboration because when a new engineer joins the team and says, "How

**[13:18]** engineer joins the team and says, "How

**[13:18]** engineer joins the team and says, "How do we do this?" It's already in memory.

**[13:20]** do we do this?" It's already in memory.

**[13:20]** do we do this?" It's already in memory. They can just ask the droid how we do

**[13:22]** They can just ask the droid how we do

**[13:22]** They can just ask the droid how we do this. And so, most importantly, what

**[13:25]** this. And so, most importantly, what

**[13:25]** this. And so, most importantly, what we're seeing in general is a shift from

**[13:27]** we're seeing in general is a shift from

**[13:27]** we're seeing in general is a shift from reactive to predictive operations

**[13:30]** reactive to predictive operations

**[13:30]** reactive to predictive operations because you can now start to really see

**[13:32]** because you can now start to really see

**[13:32]** because you can now start to really see the patterns across the entire

**[13:33]** the patterns across the entire

**[13:33]** the patterns across the entire operational history. And agentic systems

**[13:36]** operational history. And agentic systems

**[13:36]** operational history. And agentic systems turn each of these incidents into an

**[13:39]** turn each of these incidents into an

**[13:39]** turn each of these incidents into an opportunity to make the entire system

**[13:41]** opportunity to make the entire system

**[13:41]** opportunity to make the entire system more reliable.

**[13:43]** more reliable.

**[13:43]** more reliable. AI agents are not replacing software

**[13:46]** AI agents are not replacing software

**[13:46]** AI agents are not replacing software engineers. They're significantly

**[13:48]** engineers. They're significantly

**[13:48]** engineers. They're significantly amplifying their individual

**[13:50]** amplifying their individual

**[13:50]** amplifying their individual capabilities. The best developers I know

**[13:53]** capabilities. The best developers I know

**[13:53]** capabilities. The best developers I know are spending far less time in the IDE

**[13:56]** are spending far less time in the IDE

**[13:56]** are spending far less time in the IDE writing lines of code. It's just not

**[13:58]** writing lines of code. It's just not

**[13:58]** writing lines of code. It's just not high leverage. They're managing agents


### [14:00 - 15:00]

**[14:00]** high leverage. They're managing agents

**[14:00]** high leverage. They're managing agents that can do multiple things at once that

**[14:03]** that can do multiple things at once that

**[14:03]** that can do multiple things at once that are capable of organizing the systems

**[14:05]** are capable of organizing the systems

**[14:05]** are capable of organizing the systems and they're building out patterns that

**[14:07]** and they're building out patterns that

**[14:07]** and they're building out patterns that supersede the inner loop of software

**[14:09]** supersede the inner loop of software

**[14:09]** supersede the inner loop of software development and they're moving to the

**[14:10]** development and they're moving to the

**[14:10]** development and they're moving to the outer loop of software development.

**[14:13]** outer loop of software development.

**[14:13]** outer loop of software development. They aren't worried about agents taking

**[14:15]** They aren't worried about agents taking

**[14:15]** They aren't worried about agents taking their jobs. They're too busy using the

**[14:17]** their jobs. They're too busy using the

**[14:17]** their jobs. They're too busy using the agents to become even better at what

**[14:19]** agents to become even better at what

**[14:19]** agents to become even better at what they do. The future belongs to

**[14:21]** they do. The future belongs to

**[14:21]** they do. The future belongs to developers who understand how to work

**[14:23]** developers who understand how to work

**[14:23]** developers who understand how to work with agents, not those who hope that AI

**[14:26]** with agents, not those who hope that AI

**[14:26]** with agents, not those who hope that AI will just do the work for them. And in

**[14:28]** will just do the work for them. And in

**[14:28]** will just do the work for them. And in that future, the skill that matters most

**[14:31]** that future, the skill that matters most

**[14:31]** that future, the skill that matters most is not technical knowledge or your

**[14:33]** is not technical knowledge or your

**[14:33]** is not technical knowledge or your ability to optimize a specific system,

**[14:35]** ability to optimize a specific system,

**[14:35]** ability to optimize a specific system, but your ability to think clearly and

**[14:38]** but your ability to think clearly and

**[14:38]** but your ability to think clearly and communicate effectively with both humans

**[14:41]** communicate effectively with both humans

**[14:41]** communicate effectively with both humans and AI.

**[14:47]** Now, if you find any of this interesting

**[14:47]** Now, if you find any of this interesting and you want to try the droids, I'm

**[14:49]** and you want to try the droids, I'm

**[14:49]** and you want to try the droids, I'm happy to share that everyone here uh at

**[14:51]** happy to share that everyone here uh at

**[14:51]** happy to share that everyone here uh at this talk can use this QR code uh to

**[14:54]** this talk can use this QR code uh to

**[14:54]** this talk can use this QR code uh to sign up for an account. Our mobile

**[14:56]** sign up for an account. Our mobile

**[14:56]** sign up for an account. Our mobile experience is not optimized yet, but the

**[14:59]** experience is not optimized yet, but the

**[14:59]** experience is not optimized yet, but the droids are on that. And so I'd recommend


### [15:00 - 16:00]

**[15:01]** droids are on that. And so I'd recommend

**[15:01]** droids are on that. And so I'd recommend trying this on a laptop, but you will

**[15:03]** trying this on a laptop, but you will

**[15:03]** trying this on a laptop, but you will get 20 million free tokens uh credited

**[15:05]** get 20 million free tokens uh credited

**[15:05]** get 20 million free tokens uh credited your account. Um, and I also want to add

**[15:07]** your account. Um, and I also want to add

**[15:07]** your account. Um, and I also want to add that uh you know, first and foremost,

**[15:09]** that uh you know, first and foremost,

**[15:09]** that uh you know, first and foremost, Factory is an enterprise platform,

**[15:11]** Factory is an enterprise platform,

**[15:11]** Factory is an enterprise platform, right? And so if you're if you're

**[15:13]** right? And so if you're if you're

**[15:13]** right? And so if you're if you're thinking about security, if you're

**[15:15]** thinking about security, if you're

**[15:15]** thinking about security, if you're thinking about where are the audit logs,

**[15:17]** thinking about where are the audit logs,

**[15:17]** thinking about where are the audit logs, whose responsibility is it when an agent

**[15:19]** whose responsibility is it when an agent

**[15:19]** whose responsibility is it when an agent goes and runs remove RF recursive on

**[15:22]** goes and runs remove RF recursive on

**[15:22]** goes and runs remove RF recursive on your codebase, right? Droids don't do

**[15:24]** your codebase, right? Droids don't do

**[15:24]** your codebase, right? Droids don't do that. But if it were to, right, whose

**[15:26]** that. But if it were to, right, whose

**[15:26]** that. But if it were to, right, whose responsibility is that? Then these are

**[15:28]** responsibility is that? Then these are

**[15:28]** responsibility is that? Then these are the types of questions that we're

**[15:29]** the types of questions that we're

**[15:29]** the types of questions that we're interested in and that we're helping

**[15:31]** interested in and that we're helping

**[15:31]** interested in and that we're helping large organizations solve today. And so

**[15:34]** large organizations solve today. And so

**[15:34]** large organizations solve today. And so if you're a security professional, if

**[15:36]** if you're a security professional, if

**[15:36]** if you're a security professional, if you're thinking about ownership,

**[15:38]** you're thinking about ownership,

**[15:38]** you're thinking about ownership, auditability, indemnification, if you're

**[15:40]** auditability, indemnification, if you're

**[15:40]** auditability, indemnification, if you're a lawyer, right? These are the types of

**[15:42]** a lawyer, right? These are the types of

**[15:42]** a lawyer, right? These are the types of questions that you should start asking

**[15:44]** questions that you should start asking

**[15:44]** questions that you should start asking today because yolo mode is probably not

**[15:47]** today because yolo mode is probably not

**[15:47]** today because yolo mode is probably not the best thing to be running inside your

**[15:49]** the best thing to be running inside your

**[15:49]** the best thing to be running inside your enterprise, right? And so give it a

**[15:51]** enterprise, right? And so give it a

**[15:51]** enterprise, right? And so give it a scan, give it a try, check out some of

**[15:53]** scan, give it a try, check out some of

**[15:53]** scan, give it a try, check out some of the controls we have. Um, and if you

**[15:55]** the controls we have. Um, and if you

**[15:55]** the controls we have. Um, and if you have any questions, feel free to reach

**[15:56]** have any questions, feel free to reach

**[15:56]** have any questions, feel free to reach out via email. Thanks.

**[15:59]** out via email. Thanks.

**[15:59]** out via email. Thanks. [Applause]


### [16:00 - 17:00]

**[16:00]** [Applause]

**[16:00]** [Applause] [Music]


