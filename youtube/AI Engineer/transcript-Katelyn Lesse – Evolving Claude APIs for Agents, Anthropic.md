# Katelyn Lesse – Evolving Claude APIs for Agents, Anthropic

**Video URL:** https://www.youtube.com/watch?v=aqW68Is_Kj4

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** Good morning. Um, so first let's give a

**[00:23]** Good morning. Um, so first let's give a huge thank you to Swix and the whole AI

**[00:26]** huge thank you to Swix and the whole AI

**[00:26]** huge thank you to Swix and the whole AI engineer organizing team for bringing us

**[00:27]** engineer organizing team for bringing us

**[00:28]** engineer organizing team for bringing us together. [applause]

**[00:34]** I'm Caitlyn and I lead the claw

**[00:34]** I'm Caitlyn and I lead the claw developer platform team at Anthropic.

**[00:36]** developer platform team at Anthropic.

**[00:36]** developer platform team at Anthropic. Um, so let's start with a show of hands.

**[00:38]** Um, so let's start with a show of hands.

**[00:38]** Um, so let's start with a show of hands. Who here is integrated against an LLM

**[00:41]** Who here is integrated against an LLM

**[00:41]** Who here is integrated against an LLM API to build agents?

**[00:43]** API to build agents?

**[00:43]** API to build agents? Okay, I'm talking to the right people.

**[00:45]** Okay, I'm talking to the right people.

**[00:45]** Okay, I'm talking to the right people. Love it. Um, so today I want to share

**[00:47]** Love it. Um, so today I want to share

**[00:47]** Love it. Um, so today I want to share how we're evolving our platform to help

**[00:49]** how we're evolving our platform to help

**[00:49]** how we're evolving our platform to help you build really powerful agentic

**[00:51]** you build really powerful agentic

**[00:51]** you build really powerful agentic systems using claude.

**[00:54]** systems using claude.

**[00:54]** systems using claude. So, we love working with developers who

**[00:56]** So, we love working with developers who

**[00:56]** So, we love working with developers who do what we call raising the ceiling of

**[00:58]** do what we call raising the ceiling of

**[00:58]** do what we call raising the ceiling of intelligence. They're always trying to


### [01:00 - 02:00]

**[01:00]** intelligence. They're always trying to

**[01:00]** intelligence. They're always trying to be on the frontier. They're always

**[01:01]** be on the frontier. They're always

**[01:01]** be on the frontier. They're always trying to get the best out of our models

**[01:03]** trying to get the best out of our models

**[01:03]** trying to get the best out of our models and build the most high performing

**[01:05]** and build the most high performing

**[01:05]** and build the most high performing systems. Um, and so I want to walk you

**[01:08]** systems. Um, and so I want to walk you

**[01:08]** systems. Um, and so I want to walk you through how we're building a platform

**[01:09]** through how we're building a platform

**[01:09]** through how we're building a platform that helps you get the best out of

**[01:11]** that helps you get the best out of

**[01:11]** that helps you get the best out of Claude. Um, and I'm going to do that

**[01:12]** Claude. Um, and I'm going to do that

**[01:12]** Claude. Um, and I'm going to do that using a product that you hopefully have

**[01:14]** using a product that you hopefully have

**[01:14]** using a product that you hopefully have all heard of before. Um, it's an Agentic

**[01:16]** all heard of before. Um, it's an Agentic

**[01:16]** all heard of before. Um, it's an Agentic coding product. We love it a lot and

**[01:18]** coding product. We love it a lot and

**[01:18]** coding product. We love it a lot and it's called Claude Code.

**[01:22]** it's called Claude Code.

**[01:22]** it's called Claude Code. So when we think about maximizing

**[01:24]** So when we think about maximizing

**[01:24]** So when we think about maximizing performance um from our models, we think

**[01:26]** performance um from our models, we think

**[01:26]** performance um from our models, we think about building a platform that helps you

**[01:28]** about building a platform that helps you

**[01:28]** about building a platform that helps you do three things. Um so first, the

**[01:31]** do three things. Um so first, the

**[01:31]** do three things. Um so first, the platform helps you harness Claude's

**[01:32]** platform helps you harness Claude's

**[01:32]** platform helps you harness Claude's capabilities. We're training Claude to

**[01:34]** capabilities. We're training Claude to

**[01:34]** capabilities. We're training Claude to get good at a lot of stuff and we need

**[01:36]** get good at a lot of stuff and we need

**[01:36]** get good at a lot of stuff and we need to give you the tools in our API to use

**[01:38]** to give you the tools in our API to use

**[01:38]** to give you the tools in our API to use the things that Claude is actually

**[01:40]** the things that Claude is actually

**[01:40]** the things that Claude is actually getting good at. Next, we help you

**[01:43]** getting good at. Next, we help you

**[01:43]** getting good at. Next, we help you manage Claude's context window. Keeping

**[01:45]** manage Claude's context window. Keeping

**[01:45]** manage Claude's context window. Keeping the right context in the window at any

**[01:47]** the right context in the window at any

**[01:47]** the right context in the window at any given time is really really critical to

**[01:49]** given time is really really critical to

**[01:49]** given time is really really critical to getting the best outcomes from Claude.

**[01:52]** getting the best outcomes from Claude.

**[01:52]** getting the best outcomes from Claude. And third, we're really excited about

**[01:54]** And third, we're really excited about

**[01:54]** And third, we're really excited about this lately. We think you should just

**[01:55]** this lately. We think you should just

**[01:55]** this lately. We think you should just give Claude a computer and let it do its

**[01:57]** give Claude a computer and let it do its

**[01:57]** give Claude a computer and let it do its thing. So I'll talk about how we're

**[01:59]** thing. So I'll talk about how we're

**[01:59]** thing. So I'll talk about how we're we're evolving the platform to give you


### [02:00 - 03:00]

**[02:01]** we're evolving the platform to give you

**[02:01]** we're evolving the platform to give you the infrastructure and otherwise that

**[02:02]** the infrastructure and otherwise that

**[02:02]** the infrastructure and otherwise that you need to actually let Claude do that.

**[02:09]** So starting with harnessing Claude's

**[02:10]** So starting with harnessing Claude's capabilities. Um, so we're getting

**[02:11]** capabilities. Um, so we're getting

**[02:12]** capabilities. Um, so we're getting Claude really good at a bunch of stuff

**[02:13]** Claude really good at a bunch of stuff

**[02:13]** Claude really good at a bunch of stuff and here are the ways that we expose

**[02:15]** and here are the ways that we expose

**[02:15]** and here are the ways that we expose that to you um in our API as ideally

**[02:17]** that to you um in our API as ideally

**[02:18]** that to you um in our API as ideally customizable features. So here's a first

**[02:20]** customizable features. So here's a first

**[02:20]** customizable features. So here's a first example um relatively basic. Claude got

**[02:23]** example um relatively basic. Claude got

**[02:23]** example um relatively basic. Claude got good at thinking um and Claude's

**[02:25]** good at thinking um and Claude's

**[02:25]** good at thinking um and Claude's performance on various tasks um scales

**[02:28]** performance on various tasks um scales

**[02:28]** performance on various tasks um scales with the amount of time you give it to

**[02:29]** with the amount of time you give it to

**[02:29]** with the amount of time you give it to reason through those problems. Um, and

**[02:32]** reason through those problems. Um, and

**[02:32]** reason through those problems. Um, and so, uh, we expose this to you as an API

**[02:34]** so, uh, we expose this to you as an API

**[02:34]** so, uh, we expose this to you as an API feature that you can decide, do you want

**[02:36]** feature that you can decide, do you want

**[02:36]** feature that you can decide, do you want Claude to think longer for something

**[02:38]** Claude to think longer for something

**[02:38]** Claude to think longer for something more complex or do you want Claude to

**[02:40]** more complex or do you want Claude to

**[02:40]** more complex or do you want Claude to just give you a quick answer? Um, we

**[02:42]** just give you a quick answer? Um, we

**[02:42]** just give you a quick answer? Um, we also expose this with a budget. Um, so

**[02:45]** also expose this with a budget. Um, so

**[02:45]** also expose this with a budget. Um, so you can tell Claude how many tokens to

**[02:47]** you can tell Claude how many tokens to

**[02:47]** you can tell Claude how many tokens to essentially spend on thinking. Um, and

**[02:49]** essentially spend on thinking. Um, and

**[02:49]** essentially spend on thinking. Um, and so for cloud code, um, pretty good

**[02:52]** so for cloud code, um, pretty good

**[02:52]** so for cloud code, um, pretty good example. Obviously, you're often

**[02:53]** example. Obviously, you're often

**[02:53]** example. Obviously, you're often debugging pretty complex systems with

**[02:55]** debugging pretty complex systems with

**[02:55]** debugging pretty complex systems with cloud code or sometimes you just want a

**[02:58]** cloud code or sometimes you just want a

**[02:58]** cloud code or sometimes you just want a quick, um, answer to the thing you're

**[02:59]** quick, um, answer to the thing you're


### [03:00 - 04:00]

**[03:00]** quick, um, answer to the thing you're trying to do. And so, um, Claude Code

**[03:02]** trying to do. And so, um, Claude Code

**[03:02]** trying to do. And so, um, Claude Code takes advantage of this feature in our

**[03:03]** takes advantage of this feature in our

**[03:03]** takes advantage of this feature in our API to decide whether or not to have

**[03:06]** API to decide whether or not to have

**[03:06]** API to decide whether or not to have Claude think longer.

**[03:09]** Claude think longer.

**[03:10]** Claude think longer. Another basic example is tool use.

**[03:12]** Another basic example is tool use.

**[03:12]** Another basic example is tool use. Claude has gotten really good at

**[03:13]** Claude has gotten really good at

**[03:13]** Claude has gotten really good at reliably calling tools. Um, so we expose

**[03:16]** reliably calling tools. Um, so we expose

**[03:16]** reliably calling tools. Um, so we expose this in our API with both our own

**[03:18]** this in our API with both our own

**[03:18]** this in our API with both our own built-in tools like our web search tool,

**[03:21]** built-in tools like our web search tool,

**[03:21]** built-in tools like our web search tool, um, as well as the ability to create

**[03:23]** um, as well as the ability to create

**[03:23]** um, as well as the ability to create your own custom tools. You just define a

**[03:25]** your own custom tools. You just define a

**[03:25]** your own custom tools. You just define a name, a description, and an input

**[03:27]** name, a description, and an input

**[03:27]** name, a description, and an input schema. Um, and Claude is pretty good at

**[03:29]** schema. Um, and Claude is pretty good at

**[03:29]** schema. Um, and Claude is pretty good at reliably knowing when to actually go um,

**[03:31]** reliably knowing when to actually go um,

**[03:31]** reliably knowing when to actually go um, and call those tools and pass the right

**[03:34]** and call those tools and pass the right

**[03:34]** and call those tools and pass the right arguments. So, this is relevant for

**[03:36]** arguments. So, this is relevant for

**[03:36]** arguments. So, this is relevant for cloud code. Cloud code has many, many,

**[03:38]** cloud code. Cloud code has many, many,

**[03:38]** cloud code. Cloud code has many, many, many tools and it's calling them all the

**[03:40]** many tools and it's calling them all the

**[03:40]** many tools and it's calling them all the time to do things like read files,

**[03:42]** time to do things like read files,

**[03:42]** time to do things like read files, search for files, write to files, um,

**[03:45]** search for files, write to files, um,

**[03:45]** search for files, write to files, um, and do stuff like rerun tests and

**[03:47]** and do stuff like rerun tests and

**[03:47]** and do stuff like rerun tests and otherwise.

**[03:51]** So, the next way we're evolving the

**[03:51]** So, the next way we're evolving the platform to help you ma maximize

**[03:53]** platform to help you ma maximize

**[03:53]** platform to help you ma maximize intelligence from claude um, is helping

**[03:55]** intelligence from claude um, is helping

**[03:55]** intelligence from claude um, is helping you manage Claude's context window.

**[03:57]** you manage Claude's context window.

**[03:57]** you manage Claude's context window. Getting the right context at the right

**[03:59]** Getting the right context at the right

**[03:59]** Getting the right context at the right time in the window is one of the most


### [04:00 - 05:00]

**[04:01]** time in the window is one of the most

**[04:01]** time in the window is one of the most important things that you can do to

**[04:02]** important things that you can do to

**[04:02]** important things that you can do to maximize performance.

**[04:05]** maximize performance.

**[04:05]** maximize performance. But context management is really complex

**[04:07]** But context management is really complex

**[04:07]** But context management is really complex to get right. Um especially for a coding

**[04:10]** to get right. Um especially for a coding

**[04:10]** to get right. Um especially for a coding agent like Claude Code. You've got your

**[04:12]** agent like Claude Code. You've got your

**[04:12]** agent like Claude Code. You've got your technical designs, you've got your

**[04:13]** technical designs, you've got your

**[04:13]** technical designs, you've got your entire codebase. Um you've got

**[04:15]** entire codebase. Um you've got

**[04:15]** entire codebase. Um you've got instructions, you've got tool calls. All

**[04:17]** instructions, you've got tool calls. All

**[04:17]** instructions, you've got tool calls. All these things might be in the window at

**[04:19]** these things might be in the window at

**[04:19]** these things might be in the window at any given time. And so how do you make

**[04:21]** any given time. And so how do you make

**[04:21]** any given time. And so how do you make sure the right set of those things are

**[04:23]** sure the right set of those things are

**[04:23]** sure the right set of those things are in the window? Um, so getting that

**[04:25]** in the window? Um, so getting that

**[04:25]** in the window? Um, so getting that context right and keeping it optimized

**[04:27]** context right and keeping it optimized

**[04:27]** context right and keeping it optimized over time is something that we've

**[04:28]** over time is something that we've

**[04:28]** over time is something that we've thought a lot about.

**[04:31]** thought a lot about.

**[04:31]** thought a lot about. So let's start with MCP model context

**[04:34]** So let's start with MCP model context

**[04:34]** So let's start with MCP model context protocol. We introduced this a year ago

**[04:36]** protocol. We introduced this a year ago

**[04:36]** protocol. We introduced this a year ago and it's been really cool to see the

**[04:37]** and it's been really cool to see the

**[04:37]** and it's been really cool to see the community swarm around adopting um MCP

**[04:41]** community swarm around adopting um MCP

**[04:41]** community swarm around adopting um MCP as a standardized way for agents to

**[04:43]** as a standardized way for agents to

**[04:43]** as a standardized way for agents to interact with external systems. Um, and

**[04:46]** interact with external systems. Um, and

**[04:46]** interact with external systems. Um, and so for cloud code, you might imagine

**[04:49]** so for cloud code, you might imagine

**[04:49]** so for cloud code, you might imagine GitHub or Century. there are plenty of

**[04:51]** GitHub or Century. there are plenty of

**[04:51]** GitHub or Century. there are plenty of places kind of outside of the agent's

**[04:53]** places kind of outside of the agent's

**[04:53]** places kind of outside of the agent's context where there might be additional

**[04:55]** context where there might be additional

**[04:55]** context where there might be additional information or tools or otherwise that

**[04:58]** information or tools or otherwise that

**[04:58]** information or tools or otherwise that you want your agent to be able to

**[04:59]** you want your agent to be able to

**[04:59]** you want your agent to be able to interact with or the cloud code agent to


### [05:00 - 06:00]

**[05:01]** interact with or the cloud code agent to

**[05:01]** interact with or the cloud code agent to be able to interact with. Um, and so

**[05:03]** be able to interact with. Um, and so

**[05:03]** be able to interact with. Um, and so this will obviously get you much better

**[05:04]** this will obviously get you much better

**[05:04]** this will obviously get you much better performance than an agent that only sees

**[05:07]** performance than an agent that only sees

**[05:07]** performance than an agent that only sees the things that are in its window as a

**[05:08]** the things that are in its window as a

**[05:08]** the things that are in its window as a result of your prompting.

**[05:15]** Uh, so the next thing is memory. So, if

**[05:15]** Uh, so the next thing is memory. So, if you can use tools like MCP to get

**[05:17]** you can use tools like MCP to get

**[05:17]** you can use tools like MCP to get context into your window, we introduced

**[05:19]** context into your window, we introduced

**[05:19]** context into your window, we introduced a memory tool to help you actually keep

**[05:21]** a memory tool to help you actually keep

**[05:21]** a memory tool to help you actually keep context outside of the window that

**[05:23]** context outside of the window that

**[05:23]** context outside of the window that Claude knows how to pull back into the

**[05:25]** Claude knows how to pull back into the

**[05:25]** Claude knows how to pull back into the window only when it actually needs it.

**[05:27]** window only when it actually needs it.

**[05:27]** window only when it actually needs it. Um, and so we introduced the first

**[05:29]** Um, and so we introduced the first

**[05:29]** Um, and so we introduced the first iteration of our memory tool as

**[05:31]** iteration of our memory tool as

**[05:31]** iteration of our memory tool as essentially a clientside file system.

**[05:33]** essentially a clientside file system.

**[05:33]** essentially a clientside file system. So, you control your data, but Claude is

**[05:36]** So, you control your data, but Claude is

**[05:36]** So, you control your data, but Claude is good at knowing, oh, this is like a good

**[05:37]** good at knowing, oh, this is like a good

**[05:37]** good at knowing, oh, this is like a good thing that I should store away for

**[05:39]** thing that I should store away for

**[05:39]** thing that I should store away for later. And then, uh, it knows when to

**[05:41]** later. And then, uh, it knows when to

**[05:41]** later. And then, uh, it knows when to pull that context back in.

**[05:43]** pull that context back in.

**[05:43]** pull that context back in. [clears throat] So for cloud code, you

**[05:44]** [clears throat] So for cloud code, you

**[05:44]** [clears throat] So for cloud code, you could imagine um your patterns for your

**[05:47]** could imagine um your patterns for your

**[05:47]** could imagine um your patterns for your codebase or maybe your preferences for

**[05:49]** codebase or maybe your preferences for

**[05:49]** codebase or maybe your preferences for your git workflows. These are all things

**[05:51]** your git workflows. These are all things

**[05:51]** your git workflows. These are all things that claude can store away in memory and

**[05:53]** that claude can store away in memory and

**[05:53]** that claude can store away in memory and pull back in only when they're actually

**[05:55]** pull back in only when they're actually

**[05:55]** pull back in only when they're actually relevant.

**[05:59]** And so the third thing is context

**[05:59]** And so the third thing is context editing. If memory helps you keep stuff


### [06:00 - 07:00]

**[06:02]** editing. If memory helps you keep stuff

**[06:02]** editing. If memory helps you keep stuff outside the window and pull it back in

**[06:04]** outside the window and pull it back in

**[06:04]** outside the window and pull it back in when it makes sense, context editing

**[06:06]** when it makes sense, context editing

**[06:06]** when it makes sense, context editing helps you clear stuff out that's not

**[06:08]** helps you clear stuff out that's not

**[06:08]** helps you clear stuff out that's not relevant right now and shouldn't be in

**[06:09]** relevant right now and shouldn't be in

**[06:09]** relevant right now and shouldn't be in the window. Um, so our first iteration

**[06:11]** the window. Um, so our first iteration

**[06:11]** the window. Um, so our first iteration of our context editing is just clearing

**[06:13]** of our context editing is just clearing

**[06:13]** of our context editing is just clearing out old tool results. Um, and we did

**[06:16]** out old tool results. Um, and we did

**[06:16]** out old tool results. Um, and we did this because tool results can actually

**[06:17]** this because tool results can actually

**[06:17]** this because tool results can actually just be really large and take up a lot

**[06:19]** just be really large and take up a lot

**[06:19]** just be really large and take up a lot of space in the window. And we found

**[06:21]** of space in the window. And we found

**[06:21]** of space in the window. And we found that tool results from past calls are

**[06:23]** that tool results from past calls are

**[06:23]** that tool results from past calls are not necessarily super relevant to help

**[06:25]** not necessarily super relevant to help

**[06:25]** not necessarily super relevant to help claude get good responses later on in a

**[06:28]** claude get good responses later on in a

**[06:28]** claude get good responses later on in a session. And so you can think about for

**[06:30]** session. And so you can think about for

**[06:30]** session. And so you can think about for cloud code, cloud code is calling

**[06:32]** cloud code, cloud code is calling

**[06:32]** cloud code, cloud code is calling hundreds of tools. Um, those files that

**[06:34]** hundreds of tools. Um, those files that

**[06:34]** hundreds of tools. Um, those files that it read otherwise, all these things are

**[06:36]** it read otherwise, all these things are

**[06:36]** it read otherwise, all these things are taking up space within the window. Um so

**[06:39]** taking up space within the window. Um so

**[06:39]** taking up space within the window. Um so they take advantage of um context

**[06:41]** they take advantage of um context

**[06:41]** they take advantage of um context management to clear those things out of

**[06:43]** management to clear those things out of

**[06:43]** management to clear those things out of the window.

**[06:48]** And so um we found that if we combined

**[06:48]** And so um we found that if we combined our memory tool with context editing, we

**[06:51]** our memory tool with context editing, we

**[06:51]** our memory tool with context editing, we saw a 39% bump in performance over o

**[06:55]** saw a 39% bump in performance over o

**[06:55]** saw a 39% bump in performance over o over the benchmark on our own internal

**[06:57]** over the benchmark on our own internal

**[06:57]** over the benchmark on our own internal evals. Um which was really really huge.


### [07:00 - 08:00]

**[07:00]** evals. Um which was really really huge.

**[07:00]** evals. Um which was really really huge. And so it just kind of shows you the

**[07:01]** And so it just kind of shows you the

**[07:01]** And so it just kind of shows you the importance of keeping things in the

**[07:03]** importance of keeping things in the

**[07:03]** importance of keeping things in the window that are only relevant at any

**[07:05]** window that are only relevant at any

**[07:05]** window that are only relevant at any given time. And we're expanding on this

**[07:07]** given time. And we're expanding on this

**[07:07]** given time. And we're expanding on this by giving you larger context windows. So

**[07:09]** by giving you larger context windows. So

**[07:09]** by giving you larger context windows. So for some of our models, you can have a

**[07:11]** for some of our models, you can have a

**[07:11]** for some of our models, you can have a million token context window. Combining

**[07:13]** million token context window. Combining

**[07:13]** million token context window. Combining that larger window with the tools to

**[07:15]** that larger window with the tools to

**[07:15]** that larger window with the tools to actually edit what's in your window

**[07:17]** actually edit what's in your window

**[07:17]** actually edit what's in your window maximizes your performance. Um, and over

**[07:20]** maximizes your performance. Um, and over

**[07:20]** maximizes your performance. Um, and over time we're teaching Claude to get better

**[07:21]** time we're teaching Claude to get better

**[07:21]** time we're teaching Claude to get better and better at actually understanding

**[07:23]** and better at actually understanding

**[07:23]** and better at actually understanding what's in its context window. So maybe

**[07:25]** what's in its context window. So maybe

**[07:25]** what's in its context window. So maybe it has a lot of room to run, maybe it's

**[07:27]** it has a lot of room to run, maybe it's

**[07:27]** it has a lot of room to run, maybe it's almost out of space. Um, and Claude will

**[07:29]** almost out of space. Um, and Claude will

**[07:29]** almost out of space. Um, and Claude will respond accordingly depending on how

**[07:31]** respond accordingly depending on how

**[07:31]** respond accordingly depending on how much time uh or how much room it has

**[07:33]** much time uh or how much room it has

**[07:33]** much time uh or how much room it has left in the window.

**[07:39]** So, here's the third thing. Um, we think

**[07:39]** So, here's the third thing. Um, we think you should give Claude a computer and

**[07:41]** you should give Claude a computer and

**[07:41]** you should give Claude a computer and just let it do its thing. We're really

**[07:43]** just let it do its thing. We're really

**[07:43]** just let it do its thing. We're really excited about this one. Um, because

**[07:44]** excited about this one. Um, because

**[07:44]** excited about this one. Um, because there's a lot of discourse right now

**[07:46]** there's a lot of discourse right now

**[07:46]** there's a lot of discourse right now around agent harnesses. Um, you know,

**[07:49]** around agent harnesses. Um, you know,

**[07:49]** around agent harnesses. Um, you know, how much scaffolding should you have?

**[07:50]** how much scaffolding should you have?

**[07:50]** how much scaffolding should you have? How opinionated should it be? Should it

**[07:52]** How opinionated should it be? Should it

**[07:52]** How opinionated should it be? Should it be heavy? Should it be light? Um, and I

**[07:55]** be heavy? Should it be light? Um, and I

**[07:55]** be heavy? Should it be light? Um, and I think at the end of the day, Claude has

**[07:58]** think at the end of the day, Claude has

**[07:58]** think at the end of the day, Claude has access to writing code. And if Claude


### [08:00 - 09:00]

**[08:00]** access to writing code. And if Claude

**[08:00]** access to writing code. And if Claude has access to running that same code, it

**[08:02]** has access to running that same code, it

**[08:02]** has access to running that same code, it can accomplish anything. you can get

**[08:03]** can accomplish anything. you can get

**[08:03]** can accomplish anything. you can get really great professional outputs for

**[08:05]** really great professional outputs for

**[08:05]** really great professional outputs for the things that you're doing just by

**[08:06]** the things that you're doing just by

**[08:06]** the things that you're doing just by giving Claude runway to go and do that.

**[08:09]** giving Claude runway to go and do that.

**[08:09]** giving Claude runway to go and do that. But the challenge for letting you do

**[08:10]** But the challenge for letting you do

**[08:10]** But the challenge for letting you do that is actually the infrastructure as

**[08:13]** that is actually the infrastructure as

**[08:13]** that is actually the infrastructure as well as stuff like expertise like how do

**[08:14]** well as stuff like expertise like how do

**[08:14]** well as stuff like expertise like how do you give cloud access to things that um

**[08:16]** you give cloud access to things that um

**[08:16]** you give cloud access to things that um when it's using a computer it will get

**[08:18]** when it's using a computer it will get

**[08:18]** when it's using a computer it will get you better results.

**[08:21]** you better results.

**[08:21]** you better results. So a fun story is we recently launched

**[08:23]** So a fun story is we recently launched

**[08:23]** So a fun story is we recently launched cloud code on web and mobile. Um and

**[08:26]** cloud code on web and mobile. Um and

**[08:26]** cloud code on web and mobile. Um and this was a fun project for our team

**[08:28]** this was a fun project for our team

**[08:28]** this was a fun project for our team because we had a lot of problems to

**[08:29]** because we had a lot of problems to

**[08:29]** because we had a lot of problems to solve. When you're running cloud code

**[08:31]** solve. When you're running cloud code

**[08:31]** solve. When you're running cloud code locally, cloud code is essentially using

**[08:33]** locally, cloud code is essentially using

**[08:33]** locally, cloud code is essentially using your machine as its computer. But if

**[08:36]** your machine as its computer. But if

**[08:36]** your machine as its computer. But if you're starting a session on the web or

**[08:38]** you're starting a session on the web or

**[08:38]** you're starting a session on the web or on mobile and then you're walking away,

**[08:40]** on mobile and then you're walking away,

**[08:40]** on mobile and then you're walking away, what's happening? Like where is that

**[08:42]** what's happening? Like where is that

**[08:42]** what's happening? Like where is that where is um cloud code running? Where is

**[08:43]** where is um cloud code running? Where is

**[08:44]** where is um cloud code running? Where is it doing its work? Um and so we had some

**[08:46]** it doing its work? Um and so we had some

**[08:46]** it doing its work? Um and so we had some hard problems to solve. We needed a

**[08:48]** hard problems to solve. We needed a

**[08:48]** hard problems to solve. We needed a secure environment for cloud to be able

**[08:50]** secure environment for cloud to be able

**[08:50]** secure environment for cloud to be able to write and run code that's not

**[08:51]** to write and run code that's not

**[08:52]** to write and run code that's not necessarily like approved code by you.

**[08:54]** necessarily like approved code by you.

**[08:54]** necessarily like approved code by you. Um we needed to solve or container

**[08:57]** Um we needed to solve or container

**[08:57]** Um we needed to solve or container orchestration at scale. Um and we needed

**[08:59]** orchestration at scale. Um and we needed

**[08:59]** orchestration at scale. Um and we needed session persistence um because uh we


### [09:00 - 10:00]

**[09:02]** session persistence um because uh we

**[09:02]** session persistence um because uh we launched this and many of you were

**[09:03]** launched this and many of you were

**[09:03]** launched this and many of you were excited about it and started many many

**[09:04]** excited about it and started many many

**[09:04]** excited about it and started many many sessions and walked away and we had to

**[09:06]** sessions and walked away and we had to

**[09:06]** sessions and walked away and we had to make sure that um all of these things

**[09:08]** make sure that um all of these things

**[09:08]** make sure that um all of these things were ready to go when you came back and

**[09:10]** were ready to go when you came back and

**[09:10]** were ready to go when you came back and um wanted to see the results of what

**[09:12]** um wanted to see the results of what

**[09:12]** um wanted to see the results of what Claude did.

**[09:14]** Claude did.

**[09:14]** Claude did. So one key primitive in this is our code

**[09:17]** So one key primitive in this is our code

**[09:17]** So one key primitive in this is our code execution tool. Um so we released our

**[09:19]** execution tool. Um so we released our

**[09:19]** execution tool. Um so we released our code execution tool in the API um which

**[09:22]** code execution tool in the API um which

**[09:22]** code execution tool in the API um which allows Claude to run write code and run

**[09:24]** allows Claude to run write code and run

**[09:24]** allows Claude to run write code and run that code in a secure sandboxed

**[09:26]** that code in a secure sandboxed

**[09:26]** that code in a secure sandboxed environment. Um, so our platform handles

**[09:29]** environment. Um, so our platform handles

**[09:29]** environment. Um, so our platform handles containers, it handles security, and you

**[09:31]** containers, it handles security, and you

**[09:31]** containers, it handles security, and you don't have to think about these things

**[09:32]** don't have to think about these things

**[09:32]** don't have to think about these things because they're running on our servers.

**[09:34]** because they're running on our servers.

**[09:34]** because they're running on our servers. Um, so you can imagine deciding that um,

**[09:37]** Um, so you can imagine deciding that um,

**[09:37]** Um, so you can imagine deciding that um, you you want Claude to write some code

**[09:39]** you you want Claude to write some code

**[09:39]** you you want Claude to write some code and you want Claude to go and be able to

**[09:41]** and you want Claude to go and be able to

**[09:41]** and you want Claude to go and be able to run that code. And for cloud code,

**[09:43]** run that code. And for cloud code,

**[09:43]** run that code. And for cloud code, there's plenty of examples here. Um,

**[09:45]** there's plenty of examples here. Um,

**[09:45]** there's plenty of examples here. Um, like make an animation more sparkly that

**[09:48]** like make an animation more sparkly that

**[09:48]** like make an animation more sparkly that uh, you want Claude to actually be able

**[09:49]** uh, you want Claude to actually be able

**[09:49]** uh, you want Claude to actually be able to run that code. Um, so we really think

**[09:51]** to run that code. Um, so we really think

**[09:51]** to run that code. Um, so we really think the future of agents is letting the

**[09:53]** the future of agents is letting the

**[09:53]** the future of agents is letting the model work pretty autonomously within a

**[09:55]** model work pretty autonomously within a

**[09:55]** model work pretty autonomously within a sandbox environment and we're giving you

**[09:57]** sandbox environment and we're giving you

**[09:57]** sandbox environment and we're giving you the infrastructure to be able to do

**[09:58]** the infrastructure to be able to do

**[09:58]** the infrastructure to be able to do that.


### [10:00 - 11:00]

**[10:01]** that.

**[10:01]** that. And this gets really powerful once you

**[10:03]** And this gets really powerful once you

**[10:03]** And this gets really powerful once you think about giving the model actual

**[10:05]** think about giving the model actual

**[10:05]** think about giving the model actual domain expertise in the things that

**[10:07]** domain expertise in the things that

**[10:07]** domain expertise in the things that you're trying to do. So we recently

**[10:09]** you're trying to do. So we recently

**[10:09]** you're trying to do. So we recently released agent skills which you can use

**[10:11]** released agent skills which you can use

**[10:11]** released agent skills which you can use in combination with our code execution

**[10:13]** in combination with our code execution

**[10:13]** in combination with our code execution tool. Skills are basically just folders

**[10:15]** tool. Skills are basically just folders

**[10:15]** tool. Skills are basically just folders of scripts, instructions, and resources

**[10:18]** of scripts, instructions, and resources

**[10:18]** of scripts, instructions, and resources that Claude has access to and can decide

**[10:20]** that Claude has access to and can decide

**[10:20]** that Claude has access to and can decide to run within its sandbox environment.

**[10:23]** to run within its sandbox environment.

**[10:23]** to run within its sandbox environment. Um, it decides to do that based on the

**[10:25]** Um, it decides to do that based on the

**[10:26]** Um, it decides to do that based on the request that you gave it as well as the

**[10:27]** request that you gave it as well as the

**[10:27]** request that you gave it as well as the description of a skill. Um, and Claude

**[10:29]** description of a skill. Um, and Claude

**[10:30]** description of a skill. Um, and Claude is really good at knowing like this is

**[10:31]** is really good at knowing like this is

**[10:31]** is really good at knowing like this is the right time to pull this skill into

**[10:33]** the right time to pull this skill into

**[10:33]** the right time to pull this skill into context and go ahead and use it. And you

**[10:35]** context and go ahead and use it. And you

**[10:35]** context and go ahead and use it. And you can combine skills with tools like MCP.

**[10:38]** can combine skills with tools like MCP.

**[10:38]** can combine skills with tools like MCP. So MCP gives you access to tools and

**[10:40]** So MCP gives you access to tools and

**[10:40]** So MCP gives you access to tools and access to context. Um, and then skills

**[10:43]** access to context. Um, and then skills

**[10:43]** access to context. Um, and then skills give you the expertise to actually make

**[10:44]** give you the expertise to actually make

**[10:44]** give you the expertise to actually make use of those tools and make use of that

**[10:46]** use of those tools and make use of that

**[10:46]** use of those tools and make use of that context. Um, and so for cloud code, a

**[10:49]** context. Um, and so for cloud code, a

**[10:49]** context. Um, and so for cloud code, a good example is web design. Maybe

**[10:51]** good example is web design. Maybe

**[10:51]** good example is web design. Maybe whenever you launch a new product or a

**[10:53]** whenever you launch a new product or a

**[10:53]** whenever you launch a new product or a new feature, um, you build landing

**[10:55]** new feature, um, you build landing

**[10:55]** new feature, um, you build landing pages. And when you build those landing

**[10:57]** pages. And when you build those landing

**[10:57]** pages. And when you build those landing pages, you want them to follow your

**[10:59]** pages, you want them to follow your

**[10:59]** pages, you want them to follow your design system and you want them to


### [11:00 - 12:00]

**[11:00]** design system and you want them to

**[11:00]** design system and you want them to follow the patterns that you've set out.

**[11:02]** follow the patterns that you've set out.

**[11:02]** follow the patterns that you've set out. Um, and so Claude will know, okay, I'm

**[11:05]** Um, and so Claude will know, okay, I'm

**[11:05]** Um, and so Claude will know, okay, I'm being told to build a landing page. This

**[11:07]** being told to build a landing page. This

**[11:07]** being told to build a landing page. This is a good time to pull in the web design

**[11:08]** is a good time to pull in the web design

**[11:08]** is a good time to pull in the web design skill. um and use the right patterns and

**[11:11]** skill. um and use the right patterns and

**[11:11]** skill. um and use the right patterns and and design system for that landing page.

**[11:13]** and design system for that landing page.

**[11:13]** and design system for that landing page. Uh tomorrow Barry and Mahes from our

**[11:15]** Uh tomorrow Barry and Mahes from our

**[11:15]** Uh tomorrow Barry and Mahes from our team are giving a talk on skills.

**[11:17]** team are giving a talk on skills.

**[11:17]** team are giving a talk on skills. They'll go much deeper and I definitely

**[11:19]** They'll go much deeper and I definitely

**[11:19]** They'll go much deeper and I definitely recommend checking that out.

**[11:23]** recommend checking that out.

**[11:23]** recommend checking that out. So these are the ways that we're

**[11:24]** So these are the ways that we're

**[11:24]** So these are the ways that we're evolving our platform um to help you

**[11:26]** evolving our platform um to help you

**[11:26]** evolving our platform um to help you take advantage of everything that Claude

**[11:28]** take advantage of everything that Claude

**[11:28]** take advantage of everything that Claude can do to get the absolute best

**[11:30]** can do to get the absolute best

**[11:30]** can do to get the absolute best performance for the things that you're

**[11:31]** performance for the things that you're

**[11:31]** performance for the things that you're building. First, harnessing Claude's

**[11:33]** building. First, harnessing Claude's

**[11:34]** building. First, harnessing Claude's capabilities. So, as our research team

**[11:36]** capabilities. So, as our research team

**[11:36]** capabilities. So, as our research team trains Claude, we give you the API

**[11:38]** trains Claude, we give you the API

**[11:38]** trains Claude, we give you the API features to take advantage of those

**[11:39]** features to take advantage of those

**[11:40]** features to take advantage of those things. Next, managing Claude's context,

**[11:42]** things. Next, managing Claude's context,

**[11:42]** things. Next, managing Claude's context, it's really, really important to keep

**[11:44]** it's really, really important to keep

**[11:44]** it's really, really important to keep your context window clean with the right

**[11:46]** your context window clean with the right

**[11:46]** your context window clean with the right context at the right time. And third,

**[11:49]** context at the right time. And third,

**[11:49]** context at the right time. And third, giving Claude a computer and just

**[11:50]** giving Claude a computer and just

**[11:50]** giving Claude a computer and just letting it do its thing.

**[11:55]** So, we're going to keep evolving our

**[11:55]** So, we're going to keep evolving our platform. Um, as Claude gets better and

**[11:58]** platform. Um, as Claude gets better and

**[11:58]** platform. Um, as Claude gets better and has more capabilities and gets better at


### [12:00 - 13:00]

**[12:00]** has more capabilities and gets better at

**[12:00]** has more capabilities and gets better at the capabilities it already has, we'll

**[12:02]** the capabilities it already has, we'll

**[12:02]** the capabilities it already has, we'll continue to evolve the API around that

**[12:04]** continue to evolve the API around that

**[12:04]** continue to evolve the API around that so that you can stay on the frontier and

**[12:06]** so that you can stay on the frontier and

**[12:06]** so that you can stay on the frontier and take advantage of the best that Claude

**[12:08]** take advantage of the best that Claude

**[12:08]** take advantage of the best that Claude has to offer. Um, second, as uh, memory

**[12:13]** has to offer. Um, second, as uh, memory

**[12:13]** has to offer. Um, second, as uh, memory and context evolve, we're going to up

**[12:15]** and context evolve, we're going to up

**[12:15]** and context evolve, we're going to up the ante on the tools that we give you

**[12:17]** the ante on the tools that we give you

**[12:17]** the ante on the tools that we give you in order to let Claude decide what to

**[12:19]** in order to let Claude decide what to

**[12:19]** in order to let Claude decide what to pull in, what to store away for later,

**[12:21]** pull in, what to store away for later,

**[12:21]** pull in, what to store away for later, and what to clean out of the context

**[12:22]** and what to clean out of the context

**[12:22]** and what to clean out of the context window. [clears throat] And third, we're

**[12:24]** window. [clears throat] And third, we're

**[12:24]** window. [clears throat] And third, we're really going to keep leaning into agent

**[12:26]** really going to keep leaning into agent

**[12:26]** really going to keep leaning into agent infrastructure. Some of the biggest

**[12:28]** infrastructure. Some of the biggest

**[12:28]** infrastructure. Some of the biggest problems with the idea of just let

**[12:29]** problems with the idea of just let

**[12:29]** problems with the idea of just let Claude have a computer and do its thing

**[12:31]** Claude have a computer and do its thing

**[12:31]** Claude have a computer and do its thing are those problems that I talked about

**[12:33]** are those problems that I talked about

**[12:33]** are those problems that I talked about around orchestration, secure

**[12:35]** around orchestration, secure

**[12:35]** around orchestration, secure environments, and sandboxing. And so

**[12:37]** environments, and sandboxing. And so

**[12:37]** environments, and sandboxing. And so we're going to keep working um to make

**[12:38]** we're going to keep working um to make

**[12:38]** we're going to keep working um to make sure that those are um ready for you to

**[12:41]** sure that those are um ready for you to

**[12:42]** sure that those are um ready for you to take advantage of.

**[12:44]** take advantage of.

**[12:44]** take advantage of. Um and I'm hiring. We're hiring at

**[12:47]** Um and I'm hiring. We're hiring at

**[12:47]** Um and I'm hiring. We're hiring at Anthropic. We're really growing our

**[12:48]** Anthropic. We're really growing our

**[12:48]** Anthropic. We're really growing our team. Um, and so if you're someone who

**[12:50]** team. Um, and so if you're someone who

**[12:50]** team. Um, and so if you're someone who loves um, building delightful developer

**[12:53]** loves um, building delightful developer

**[12:53]** loves um, building delightful developer products um, and if you're excited about

**[12:55]** products um, and if you're excited about

**[12:55]** products um, and if you're excited about what we're doing with Claude, we would

**[12:57]** what we're doing with Claude, we would

**[12:57]** what we're doing with Claude, we would love to work with you across end product

**[12:59]** love to work with you across end product

**[12:59]** love to work with you across end product design um, Devril, lots of functions. So


### [13:00 - 14:00]

**[13:02]** design um, Devril, lots of functions. So

**[13:02]** design um, Devril, lots of functions. So please reach out to us

**[13:05]** please reach out to us

**[13:05]** please reach out to us and thank you [applause]


