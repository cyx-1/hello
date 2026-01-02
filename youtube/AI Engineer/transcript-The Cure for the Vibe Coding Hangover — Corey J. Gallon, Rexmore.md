# The Cure for the Vibe Coding Hangover — Corey J. Gallon, Rexmore

**Video URL:** https://www.youtube.com/watch?v=JsKTQbT58BY

---

## Full Transcript

### [00:00 - 01:00]

**[00:18]** Inspiration strikes. You've got an idea

**[00:18]** Inspiration strikes. You've got an idea and you know exactly how you're going to

**[00:20]** and you know exactly how you're going to

**[00:20]** and you know exactly how you're going to build it.

**[00:26]** You fire up your favorite AI coding

**[00:26]** You fire up your favorite AI coding agent. You jam in those prompts and then

**[00:29]** agent. You jam in those prompts and then

**[00:29]** agent. You jam in those prompts and then you hand it over.

**[00:31]** you hand it over.

**[00:31]** you hand it over. Hey, look at him go.

**[00:35]** Hey, look at him go.

**[00:35]** Hey, look at him go. [music] He's done it. That is to say,

**[00:37]** [music] He's done it. That is to say,

**[00:37]** [music] He's done it. That is to say, you've done it. The app works. This is

**[00:40]** you've done it. The app works. This is

**[00:40]** you've done it. The app works. This is what 10x engineering really feels like.

**[00:42]** what 10x engineering really feels like.

**[00:42]** what 10x engineering really feels like. You're a genius. A rebel in the AI

**[00:45]** You're a genius. A rebel in the AI

**[00:45]** You're a genius. A rebel in the AI revolution.

**[00:47]** revolution.

**[00:47]** revolution. But then Monday rolls around. You want

**[00:50]** But then Monday rolls around. You want

**[00:50]** But then Monday rolls around. You want to add a feature or you want to change

**[00:53]** to add a feature or you want to change

**[00:53]** to add a feature or you want to change the way that it works and you realize

**[00:55]** the way that it works and you realize

**[00:55]** the way that it works and you realize that you don't understand it. You can't

**[00:57]** that you don't understand it. You can't

**[00:57]** that you don't understand it. You can't maintain it and you have to throw most


### [01:00 - 02:00]

**[01:00]** maintain it and you have to throw most

**[01:00]** maintain it and you have to throw most or all of it away.

**[01:03]** or all of it away.

**[01:03]** or all of it away. Vibe coding is the low-spec zero

**[01:06]** Vibe coding is the low-spec zero

**[01:06]** Vibe coding is the low-spec zero planning approach to AI accelerated

**[01:08]** planning approach to AI accelerated

**[01:08]** planning approach to AI accelerated development that feels productive but

**[01:11]** development that feels productive but

**[01:11]** development that feels productive but results in brittle unmaintainable demo

**[01:14]** results in brittle unmaintainable demo

**[01:14]** results in brittle unmaintainable demo wear. The hangover is the resulting

**[01:17]** wear. The hangover is the resulting

**[01:17]** wear. The hangover is the resulting despair when you try to build

**[01:19]** despair when you try to build

**[01:19]** despair when you try to build maintainable, understandable software

**[01:21]** maintainable, understandable software

**[01:21]** maintainable, understandable software this way.

**[01:24]** this way.

**[01:24]** this way. Don't worry though, there is a cure and

**[01:27]** Don't worry though, there is a cure and

**[01:27]** Don't worry though, there is a cure and it's the framework for building with AI

**[01:28]** it's the framework for building with AI

**[01:28]** it's the framework for building with AI coding agents that we're going to

**[01:30]** coding agents that we're going to

**[01:30]** coding agents that we're going to discuss today.

**[01:32]** discuss today.

**[01:32]** discuss today. So, you'll enjoy this talk if you value

**[01:34]** So, you'll enjoy this talk if you value

**[01:34]** So, you'll enjoy this talk if you value programming as a daily learning

**[01:37]** programming as a daily learning

**[01:37]** programming as a daily learning experience.

**[01:38]** experience.

**[01:38]** experience. If you want to understand and own the

**[01:41]** If you want to understand and own the

**[01:41]** If you want to understand and own the software that you write using AI coding

**[01:43]** software that you write using AI coding

**[01:43]** software that you write using AI coding agents just as you do all of the other

**[01:45]** agents just as you do all of the other

**[01:45]** agents just as you do all of the other software that you write. If you want to

**[01:48]** software that you write. If you want to

**[01:48]** software that you write. If you want to be the boss of the coding agents and not

**[01:50]** be the boss of the coding agents and not

**[01:50]** be the boss of the coding agents and not their confused intern.

**[01:52]** their confused intern.

**[01:52]** their confused intern. If working with agents makes you feel

**[01:54]** If working with agents makes you feel

**[01:54]** If working with agents makes you feel like a prompt jockey these days and no

**[01:56]** like a prompt jockey these days and no

**[01:56]** like a prompt jockey these days and no longer an AI engineer. If you're sick of

**[01:59]** longer an AI engineer. If you're sick of

**[01:59]** longer an AI engineer. If you're sick of throwing away code, burning time and


### [02:00 - 03:00]

**[02:02]** throwing away code, burning time and

**[02:02]** throwing away code, burning time and tokens, or if you want to use coding

**[02:04]** tokens, or if you want to use coding

**[02:04]** tokens, or if you want to use coding agents to build production applications

**[02:07]** agents to build production applications

**[02:07]** agents to build production applications that do real work,

**[02:09]** that do real work,

**[02:09]** that do real work, on the other hand,

**[02:17]** >> it's not for you, Jen.

**[02:17]** >> it's not for you, Jen. >> It's not for you, JEN. [laughter]

**[02:26]** >> It's not for you, Jen.

**[02:26]** >> It's not for you, Jen. This talk is not for you if programming

**[02:29]** This talk is not for you if programming

**[02:30]** This talk is not for you if programming is a job and not a craft that you're

**[02:32]** is a job and not a craft that you're

**[02:32]** is a job and not a craft that you're refining and that works for you. If

**[02:35]** refining and that works for you. If

**[02:35]** refining and that works for you. If you're satisfied just having AI do it

**[02:38]** you're satisfied just having AI do it

**[02:38]** you're satisfied just having AI do it for you without needing to understand

**[02:40]** for you without needing to understand

**[02:40]** for you without needing to understand how or why or if vibe coding gets you

**[02:43]** how or why or if vibe coding gets you

**[02:43]** how or why or if vibe coding gets you what you need and that's good enough.

**[02:45]** what you need and that's good enough.

**[02:45]** what you need and that's good enough. And these statements aren't a judgment.

**[02:49]** And these statements aren't a judgment.

**[02:49]** And these statements aren't a judgment. They're just very different paths than

**[02:51]** They're just very different paths than

**[02:51]** They're just very different paths than what we're taking today.

**[02:53]** what we're taking today.

**[02:54]** what we're taking today. I'm Corey. I run an AI native holding

**[02:56]** I'm Corey. I run an AI native holding

**[02:56]** I'm Corey. I run an AI native holding company where we're actively buying and

**[02:59]** company where we're actively buying and

**[02:59]** company where we're actively buying and building businesses in the technology


### [03:00 - 04:00]

**[03:02]** building businesses in the technology

**[03:02]** building businesses in the technology investments and education verticals.

**[03:05]** investments and education verticals.

**[03:05]** investments and education verticals. I've been feverishly building AI coding

**[03:07]** I've been feverishly building AI coding

**[03:07]** I've been feverishly building AI coding agents since 2022.

**[03:11]** agents since 2022.

**[03:11]** agents since 2022. I love and am passionate about all

**[03:13]** I love and am passionate about all

**[03:13]** I love and am passionate about all things technology. I am a massive coffee

**[03:16]** things technology. I am a massive coffee

**[03:16]** things technology. I am a massive coffee nerd. In fact, catch me in the hallway

**[03:18]** nerd. In fact, catch me in the hallway

**[03:18]** nerd. In fact, catch me in the hallway track and ask me about the Ethiopian

**[03:21]** track and ask me about the Ethiopian

**[03:21]** track and ask me about the Ethiopian yoga chef from Misty Valley that I've

**[03:24]** yoga chef from Misty Valley that I've

**[03:24]** yoga chef from Misty Valley that I've been obsessively roasting lately. And

**[03:27]** been obsessively roasting lately. And

**[03:27]** been obsessively roasting lately. And I'm a pickle ball fanatic. I'm playing

**[03:29]** I'm a pickle ball fanatic. I'm playing

**[03:29]** I'm a pickle ball fanatic. I'm playing in a tournament tomorrow. In fact,

**[03:32]** in a tournament tomorrow. In fact,

**[03:32]** in a tournament tomorrow. In fact, so let's talk about the framework in

**[03:35]** so let's talk about the framework in

**[03:35]** so let's talk about the framework in overview.

**[03:37]** overview.

**[03:37]** overview. The framework's comprised of three

**[03:39]** The framework's comprised of three

**[03:39]** The framework's comprised of three pillars. There are the principles which

**[03:41]** pillars. There are the principles which

**[03:41]** pillars. There are the principles which are the philosophy underpinning all of

**[03:44]** are the philosophy underpinning all of

**[03:44]** are the philosophy underpinning all of it.

**[03:45]** it.

**[03:45]** it. There is the process which is the

**[03:47]** There is the process which is the

**[03:47]** There is the process which is the workflow for actually getting software

**[03:49]** workflow for actually getting software

**[03:49]** workflow for actually getting software built using AI and then there are tools

**[03:53]** built using AI and then there are tools

**[03:53]** built using AI and then there are tools which are accelerators or enablers of

**[03:55]** which are accelerators or enablers of

**[03:55]** which are accelerators or enablers of the process but also reflect our

**[03:58]** the process but also reflect our

**[03:58]** the process but also reflect our principles. So you may ask what can you


### [04:00 - 05:00]

**[04:01]** principles. So you may ask what can you

**[04:01]** principles. So you may ask what can you build with the framework and the answer

**[04:03]** build with the framework and the answer

**[04:03]** build with the framework and the answer is really anything. The framework's

**[04:06]** is really anything. The framework's

**[04:06]** is really anything. The framework's adaptive to all types of software, but

**[04:08]** adaptive to all types of software, but

**[04:08]** adaptive to all types of software, but here are a few examples of working

**[04:10]** here are a few examples of working

**[04:10]** here are a few examples of working software in the wild right now that's

**[04:12]** software in the wild right now that's

**[04:12]** software in the wild right now that's been built with this approach.

**[04:14]** been built with this approach.

**[04:14]** been built with this approach. [clears throat]

**[04:16]** [clears throat]

**[04:16]** [clears throat] uh specialized litigation support

**[04:18]** uh specialized litigation support

**[04:18]** uh specialized litigation support applications for law firms,

**[04:22]** applications for law firms,

**[04:22]** applications for law firms, real-time appliance monitoring packages

**[04:24]** real-time appliance monitoring packages

**[04:24]** real-time appliance monitoring packages for cooking,

**[04:26]** for cooking,

**[04:26]** for cooking, digital publishing systems for dynamic

**[04:29]** digital publishing systems for dynamic

**[04:29]** digital publishing systems for dynamic content replatforming,

**[04:31]** content replatforming,

**[04:31]** content replatforming, and on and on and on and on. The point

**[04:36]** and on and on and on and on. The point

**[04:36]** and on and on and on and on. The point is that these aren't toys. These are

**[04:39]** is that these aren't toys. These are

**[04:39]** is that these aren't toys. These are real software applications

**[04:42]** real software applications

**[04:42]** real software applications that do real work every day. And

**[04:45]** that do real work every day. And

**[04:45]** that do real work every day. And critically they're evolved and

**[04:47]** critically they're evolved and

**[04:47]** critically they're evolved and maintained by AI engineers who apply

**[04:50]** maintained by AI engineers who apply

**[04:50]** maintained by AI engineers who apply this framework.

**[04:53]** this framework.

**[04:53]** this framework. So let's make a start and get into the

**[04:55]** So let's make a start and get into the

**[04:55]** So let's make a start and get into the principles. Principles broadly map

**[04:58]** principles. Principles broadly map

**[04:58]** principles. Principles broadly map across three categories. sort of general


### [05:00 - 06:00]

**[05:01]** across three categories. sort of general

**[05:01]** across three categories. sort of general principles that apply overarchingly and

**[05:04]** principles that apply overarchingly and

**[05:04]** principles that apply overarchingly and then principles that skew more towards

**[05:07]** then principles that skew more towards

**[05:07]** then principles that skew more towards the planning phase of the process and

**[05:10]** the planning phase of the process and

**[05:10]** the planning phase of the process and principles that skew more towards the

**[05:12]** principles that skew more towards the

**[05:12]** principles that skew more towards the implementation phase of the process. 10

**[05:15]** implementation phase of the process. 10

**[05:15]** implementation phase of the process. 10 in all. So [clears throat] let's talk

**[05:17]** in all. So [clears throat] let's talk

**[05:17]** in all. So [clears throat] let's talk about each of them. Our first overall

**[05:20]** about each of them. Our first overall

**[05:20]** about each of them. Our first overall principle is that AI engineering is

**[05:23]** principle is that AI engineering is

**[05:23]** principle is that AI engineering is accelerated learning.

**[05:25]** accelerated learning.

**[05:25]** accelerated learning. What were the problems that this came

**[05:27]** What were the problems that this came

**[05:27]** What were the problems that this came from? Well, treating AI coding agents as

**[05:30]** from? Well, treating AI coding agents as

**[05:30]** from? Well, treating AI coding agents as pure productivity tools just to crank

**[05:33]** pure productivity tools just to crank

**[05:33]** pure productivity tools just to crank out code faster, using AI to generate

**[05:36]** out code faster, using AI to generate

**[05:36]** out code faster, using AI to generate software and not learning anything from

**[05:38]** software and not learning anything from

**[05:38]** software and not learning anything from the process and then 6 months later

**[05:40]** the process and then 6 months later

**[05:40]** the process and then 6 months later being no better as engineers having

**[05:43]** being no better as engineers having

**[05:43]** being no better as engineers having plateaued or worse becoming dependent on

**[05:46]** plateaued or worse becoming dependent on

**[05:46]** plateaued or worse becoming dependent on AI for so many things, debugging,

**[05:48]** AI for so many things, debugging,

**[05:48]** AI for so many things, debugging, modifications, architectural decisions.

**[05:51]** modifications, architectural decisions.

**[05:52]** modifications, architectural decisions. That's the opposite of AI augmentation.

**[05:54]** That's the opposite of AI augmentation.

**[05:54]** That's the opposite of AI augmentation. That's AI dependency.

**[05:57]** That's AI dependency.

**[05:57]** That's AI dependency. So the big idea here is that the

**[05:58]** So the big idea here is that the

**[05:58]** So the big idea here is that the framework is not just about building


### [06:00 - 07:00]

**[06:01]** framework is not just about building

**[06:01]** framework is not just about building faster. It's about learning as we go.

**[06:05]** faster. It's about learning as we go.

**[06:05]** faster. It's about learning as we go. Every step in the framework creates

**[06:08]** Every step in the framework creates

**[06:08]** Every step in the framework creates specific learning opportunities. So that

**[06:11]** specific learning opportunities. So that

**[06:11]** specific learning opportunities. So that you're not just shipping software,

**[06:13]** you're not just shipping software,

**[06:13]** you're not just shipping software, you're building yourself.

**[06:15]** you're building yourself.

**[06:15]** you're building yourself. The software is valuable, but the

**[06:16]** The software is valuable, but the

**[06:16]** The software is valuable, but the engineer that you become is

**[06:17]** engineer that you become is

**[06:18]** engineer that you become is exponentially more valuable. And that's

**[06:21]** exponentially more valuable. And that's

**[06:21]** exponentially more valuable. And that's why we say always be learning or you may

**[06:24]** why we say always be learning or you may

**[06:24]** why we say always be learning or you may say a always b

**[06:28]** say a always b

**[06:28]** say a always b larning always be learning.

**[06:36]** Our next general principle is that you

**[06:36]** Our next general principle is that you are the architect and the agent is the

**[06:39]** are the architect and the agent is the

**[06:39]** are the architect and the agent is the implement.

**[06:41]** implement.

**[06:41]** implement. Treating AI agents as replacements for

**[06:43]** Treating AI agents as replacements for

**[06:43]** Treating AI agents as replacements for architectural thinking rather than

**[06:46]** architectural thinking rather than

**[06:46]** architectural thinking rather than implementers of your decisions when

**[06:48]** implementers of your decisions when

**[06:48]** implementers of your decisions when they're well specified is a big problem.

**[06:51]** they're well specified is a big problem.

**[06:51]** they're well specified is a big problem. So the primary idea here is keep the

**[06:54]** So the primary idea here is keep the

**[06:54]** So the primary idea here is keep the architect and implement boundary crystal

**[06:57]** architect and implement boundary crystal

**[06:57]** architect and implement boundary crystal clear. You own the thinking and that


### [07:00 - 08:00]

**[07:00]** clear. You own the thinking and that

**[07:00]** clear. You own the thinking and that means architecture and interfaces, the

**[07:03]** means architecture and interfaces, the

**[07:03]** means architecture and interfaces, the intent of the system, the structure,

**[07:06]** intent of the system, the structure,

**[07:06]** intent of the system, the structure, [clears throat]

**[07:07]** [clears throat]

**[07:07]** [clears throat] design decisions and the associated

**[07:09]** design decisions and the associated

**[07:09]** design decisions and the associated tradeoffs. And then the agent handles

**[07:12]** tradeoffs. And then the agent handles

**[07:12]** tradeoffs. And then the agent handles the doing. That's implementation, typing

**[07:15]** the doing. That's implementation, typing

**[07:15]** the doing. That's implementation, typing code, following patterns, implementing

**[07:17]** code, following patterns, implementing

**[07:17]** code, following patterns, implementing the tests that you specify, banging out

**[07:19]** the tests that you specify, banging out

**[07:20]** the tests that you specify, banging out boilerplate. That's why we say delegate

**[07:22]** boilerplate. That's why we say delegate

**[07:22]** boilerplate. That's why we say delegate the doing and not the thinking.

**[07:31]** Our third general principle is a little

**[07:31]** Our third general principle is a little bit counterintuitive, but it's slow down

**[07:34]** bit counterintuitive, but it's slow down

**[07:34]** bit counterintuitive, but it's slow down and iterate in order to go fast.

**[07:39]** and iterate in order to go fast.

**[07:39]** and iterate in order to go fast. The problem is the starting over cycle.

**[07:43]** The problem is the starting over cycle.

**[07:43]** The problem is the starting over cycle. Without deliberate iteration on

**[07:46]** Without deliberate iteration on

**[07:46]** Without deliberate iteration on validated work, you end up repeatedly

**[07:48]** validated work, you end up repeatedly

**[07:48]** validated work, you end up repeatedly starting from scratch. And so 3 months

**[07:51]** starting from scratch. And so 3 months

**[07:51]** starting from scratch. And so 3 months in, you've had multiple abandoned

**[07:54]** in, you've had multiple abandoned

**[07:54]** in, you've had multiple abandoned attempts instead of consistently

**[07:56]** attempts instead of consistently

**[07:56]** attempts instead of consistently [snorts]

**[07:56]** [snorts]

**[07:56]** [snorts] improving on one single system. So the


### [08:00 - 09:00]

**[08:00]** improving on one single system. So the

**[08:00]** improving on one single system. So the big idea here is that deliberate

**[08:01]** big idea here is that deliberate

**[08:02]** big idea here is that deliberate iteration enables compounding returns on

**[08:05]** iteration enables compounding returns on

**[08:05]** iteration enables compounding returns on both understanding and on productivity.

**[08:08]** both understanding and on productivity.

**[08:08]** both understanding and on productivity. And so yeah, week one feels slow, but

**[08:12]** And so yeah, week one feels slow, but

**[08:12]** And so yeah, week one feels slow, but week two builds momentum and then week

**[08:14]** week two builds momentum and then week

**[08:14]** week two builds momentum and then week three is dramatically faster.

**[08:17]** three is dramatically faster.

**[08:17]** three is dramatically faster. We say compound progress, accelerate

**[08:20]** We say compound progress, accelerate

**[08:20]** We say compound progress, accelerate velocity.

**[08:30]** So the first of our planning related

**[08:30]** So the first of our planning related principles is that specification

**[08:33]** principles is that specification

**[08:33]** principles is that specification is far greater than prompt engineering.

**[08:37]** is far greater than prompt engineering.

**[08:37]** is far greater than prompt engineering. Prompt engineering treats AI

**[08:39]** Prompt engineering treats AI

**[08:39]** Prompt engineering treats AI interactions as an optimization problem

**[08:42]** interactions as an optimization problem

**[08:42]** interactions as an optimization problem rather than a communication problem.

**[08:45]** rather than a communication problem.

**[08:45]** rather than a communication problem. Trying to find magic words that produce

**[08:47]** Trying to find magic words that produce

**[08:47]** Trying to find magic words that produce the right output rather than clearly

**[08:50]** the right output rather than clearly

**[08:50]** the right output rather than clearly defining what right means.

**[08:53]** defining what right means.

**[08:53]** defining what right means. So the big idea here is that

**[08:55]** So the big idea here is that

**[08:55]** So the big idea here is that specifications are very different than

**[08:58]** specifications are very different than

**[08:58]** specifications are very different than prompts in the classic sense.


### [09:00 - 10:00]

**[09:00]** prompts in the classic sense.

**[09:00]** prompts in the classic sense. Specifications are structured precise

**[09:03]** Specifications are structured precise

**[09:03]** Specifications are structured precise definitions of requirements of behavior

**[09:07]** definitions of requirements of behavior

**[09:07]** definitions of requirements of behavior interfaces and acceptance criteria.

**[09:11]** interfaces and acceptance criteria.

**[09:11]** interfaces and acceptance criteria. Writing specifications forces

**[09:12]** Writing specifications forces

**[09:12]** Writing specifications forces architectural thinking. You must

**[09:15]** architectural thinking. You must

**[09:15]** architectural thinking. You must understand the problem completely and

**[09:18]** understand the problem completely and

**[09:18]** understand the problem completely and then define interfaces precisely and

**[09:21]** then define interfaces precisely and

**[09:21]** then define interfaces precisely and anticipate edge cases.

**[09:24]** anticipate edge cases.

**[09:24]** anticipate edge cases. In turn, specifications provide clear,

**[09:27]** In turn, specifications provide clear,

**[09:27]** In turn, specifications provide clear, unambiguous direction. The agent

**[09:30]** unambiguous direction. The agent

**[09:30]** unambiguous direction. The agent implements what you specified and not

**[09:33]** implements what you specified and not

**[09:33]** implements what you specified and not what it interprets from conversational

**[09:35]** what it interprets from conversational

**[09:35]** what it interprets from conversational prompts.

**[09:38]** prompts.

**[09:38]** prompts. We say write the blueprint, not the

**[09:40]** We say write the blueprint, not the

**[09:40]** We say write the blueprint, not the prompt.

**[09:47]** Our next planning related principle is

**[09:47]** Our next planning related principle is define done before implementing.

**[09:51]** define done before implementing.

**[09:51]** define done before implementing. Starting implementation without

**[09:53]** Starting implementation without

**[09:53]** Starting implementation without executable tests and observable success

**[09:55]** executable tests and observable success

**[09:56]** executable tests and observable success criteria means that agents lack clear

**[09:59]** criteria means that agents lack clear

**[09:59]** criteria means that agents lack clear completion criteria and immediate


### [10:00 - 11:00]

**[10:00]** completion criteria and immediate

**[10:00]** completion criteria and immediate feedback. They can't self- validate.

**[10:04]** feedback. They can't self- validate.

**[10:04]** feedback. They can't self- validate. They can't self-correct

**[10:06]** They can't self-correct

**[10:06]** They can't self-correct and they don't know when they're done,

**[10:07]** and they don't know when they're done,

**[10:07]** and they don't know when they're done, at least not in consistence with your

**[10:10]** at least not in consistence with your

**[10:10]** at least not in consistence with your specifications. And so the big idea here

**[10:14]** specifications. And so the big idea here

**[10:14]** specifications. And so the big idea here is defining done before implementation

**[10:17]** is defining done before implementation

**[10:17]** is defining done before implementation keeps you thinking deeply about

**[10:20]** keeps you thinking deeply about

**[10:20]** keeps you thinking deeply about requirements and then it enables the

**[10:22]** requirements and then it enables the

**[10:22]** requirements and then it enables the agent to work autonomously.

**[10:25]** agent to work autonomously.

**[10:25]** agent to work autonomously. By defining tests up front, we give

**[10:28]** By defining tests up front, we give

**[10:28]** By defining tests up front, we give agents clear stop conditions that then

**[10:31]** agents clear stop conditions that then

**[10:31]** agents clear stop conditions that then enable them to get immediate feedback

**[10:33]** enable them to get immediate feedback

**[10:33]** enable them to get immediate feedback during implementation and self-correct

**[10:36]** during implementation and self-correct

**[10:36]** during implementation and self-correct wherever necessary. We'll talk more

**[10:38]** wherever necessary. We'll talk more

**[10:38]** wherever necessary. We'll talk more about multiensory validation later.

**[10:41]** about multiensory validation later.

**[10:41]** about multiensory validation later. But we enable agents to observe through

**[10:44]** But we enable agents to observe through

**[10:44]** But we enable agents to observe through visual like what renders senses,

**[10:48]** visual like what renders senses,

**[10:48]** visual like what renders senses, auditory senses like what they can hear

**[10:50]** auditory senses like what they can hear

**[10:50]** auditory senses like what they can hear through logs and errors and tactile

**[10:52]** through logs and errors and tactile

**[10:52]** through logs and errors and tactile senses meaning how they interact with

**[10:54]** senses meaning how they interact with

**[10:54]** senses meaning how they interact with the system. Tests verify correctness of

**[10:58]** the system. Tests verify correctness of

**[10:58]** the system. Tests verify correctness of spec of implementation whilst sensors


### [11:00 - 12:00]

**[11:01]** spec of implementation whilst sensors

**[11:01]** spec of implementation whilst sensors reveal the actual behavior of the

**[11:03]** reveal the actual behavior of the

**[11:03]** reveal the actual behavior of the software as it's being implemented. And

**[11:05]** software as it's being implemented. And

**[11:05]** software as it's being implemented. And so done means that a feature is done

**[11:08]** so done means that a feature is done

**[11:08]** so done means that a feature is done when it tests pass and when the sensors

**[11:12]** when it tests pass and when the sensors

**[11:12]** when it tests pass and when the sensors come back validating that everything's

**[11:13]** come back validating that everything's

**[11:14]** come back validating that everything's working as expected.

**[11:15]** working as expected.

**[11:16]** working as expected. We say specify success then build

**[11:25]** feature atomicity is our next principle.

**[11:25]** feature atomicity is our next principle. Writing non-atomic features means

**[11:27]** Writing non-atomic features means

**[11:27]** Writing non-atomic features means leaving the decomposition work for

**[11:30]** leaving the decomposition work for

**[11:30]** leaving the decomposition work for implementation time which forces agents

**[11:33]** implementation time which forces agents

**[11:33]** implementation time which forces agents to make architectural decisions on the

**[11:35]** to make architectural decisions on the

**[11:35]** to make architectural decisions on the fly. The primary idea here is that

**[11:39]** fly. The primary idea here is that

**[11:39]** fly. The primary idea here is that feature atomicity forces us to

**[11:42]** feature atomicity forces us to

**[11:42]** feature atomicity forces us to completely decompose

**[11:44]** completely decompose

**[11:44]** completely decompose each feature during specification and

**[11:47]** each feature during specification and

**[11:47]** each feature during specification and then in turn enable the agents to

**[11:50]** then in turn enable the agents to

**[11:50]** then in turn enable the agents to implement within a manageable scope.

**[11:52]** implement within a manageable scope.

**[11:52]** implement within a manageable scope. Features in this sense become

**[11:55]** Features in this sense become

**[11:55]** Features in this sense become implementation work units. They're

**[11:57]** implementation work units. They're

**[11:58]** implementation work units. They're atomic, irreducible tasks that are ready


### [12:00 - 13:00]

**[12:00]** atomic, irreducible tasks that are ready

**[12:00]** atomic, irreducible tasks that are ready for an agent to execute completely.

**[12:03]** for an agent to execute completely.

**[12:04]** for an agent to execute completely. Keep features as small as possible to

**[12:06]** Keep features as small as possible to

**[12:06]** Keep features as small as possible to make agent implementation as successful

**[12:08]** make agent implementation as successful

**[12:08]** make agent implementation as successful as possible.

**[12:10]** as possible.

**[12:10]** as possible. We say reduce until irreducible.

**[12:21]** So the last of our planning related

**[12:22]** So the last of our planning related principles is dependencydriven

**[12:24]** principles is dependencydriven

**[12:24]** principles is dependencydriven development.

**[12:25]** development.

**[12:26]** development. Implementing without explicit dependency

**[12:28]** Implementing without explicit dependency

**[12:28]** Implementing without explicit dependency analysis means treating all features as

**[12:30]** analysis means treating all features as

**[12:30]** analysis means treating all features as independent when in fact we know that

**[12:32]** independent when in fact we know that

**[12:32]** independent when in fact we know that they form an interconnected graph. So

**[12:35]** they form an interconnected graph. So

**[12:35]** they form an interconnected graph. So the big idea here is that

**[12:36]** the big idea here is that

**[12:36]** the big idea here is that dependencydriven development forces you

**[12:38]** dependencydriven development forces you

**[12:38]** dependencydriven development forces you to understand how features relate and

**[12:41]** to understand how features relate and

**[12:41]** to understand how features relate and how they integrate and then in turn that

**[12:44]** how they integrate and then in turn that

**[12:44]** how they integrate and then in turn that he ensures that agents never implement

**[12:47]** he ensures that agents never implement

**[12:47]** he ensures that agents never implement features that depend on incomplete work.

**[12:51]** features that depend on incomplete work.

**[12:51]** features that depend on incomplete work. We say schedule implementation by

**[12:53]** We say schedule implementation by

**[12:53]** We say schedule implementation by dependencies.

**[12:59]** And so now on to our implementation


### [13:00 - 14:00]

**[13:00]** And so now on to our implementation related principles. We start with

**[13:02]** related principles. We start with

**[13:02]** related principles. We start with implement one atomic feature at a time.

**[13:06]** implement one atomic feature at a time.

**[13:06]** implement one atomic feature at a time. Working on multiple features treats

**[13:08]** Working on multiple features treats

**[13:08]** Working on multiple features treats implementation as parallel streams of

**[13:11]** implementation as parallel streams of

**[13:11]** implementation as parallel streams of work that can be context switched

**[13:13]** work that can be context switched

**[13:13]** work that can be context switched freely. But we know that implementation

**[13:16]** freely. But we know that implementation

**[13:16]** freely. But we know that implementation quality is contingent on sustained

**[13:19]** quality is contingent on sustained

**[13:19]** quality is contingent on sustained focus, complete context and very tight

**[13:22]** focus, complete context and very tight

**[13:22]** focus, complete context and very tight feedback loops.

**[13:25]** feedback loops.

**[13:25]** feedback loops. Jumping between features fragments our

**[13:27]** Jumping between features fragments our

**[13:27]** Jumping between features fragments our focus.

**[13:29]** focus.

**[13:29]** focus. So the big idea here is that agents

**[13:31]** So the big idea here is that agents

**[13:32]** So the big idea here is that agents implement one single feature that's been

**[13:34]** implement one single feature that's been

**[13:34]** implement one single feature that's been defined atomically as previous. You

**[13:37]** defined atomically as previous. You

**[13:37]** defined atomically as previous. You study it and understand it. You validate

**[13:40]** study it and understand it. You validate

**[13:40]** study it and understand it. You validate that it works. You commit it as a

**[13:42]** that it works. You commit it as a

**[13:42]** that it works. You commit it as a checkpoint and then you move on to the

**[13:45]** checkpoint and then you move on to the

**[13:45]** checkpoint and then you move on to the next feature.

**[13:46]** next feature.

**[13:46]** next feature. This rhythm creates both momentum and

**[13:49]** This rhythm creates both momentum and

**[13:49]** This rhythm creates both momentum and also deepening understanding. We stop

**[13:52]** also deepening understanding. We stop

**[13:52]** also deepening understanding. We stop juggling multiple features

**[13:54]** juggling multiple features

**[13:54]** juggling multiple features simultaneously.

**[13:56]** simultaneously.

**[13:56]** simultaneously. We implement features sequentially with

**[13:58]** We implement features sequentially with

**[13:58]** We implement features sequentially with complete focus studying each


### [14:00 - 15:00]

**[14:00]** complete focus studying each

**[14:00]** complete focus studying each implementation to maintain understanding

**[14:03]** implementation to maintain understanding

**[14:03]** implementation to maintain understanding and then commit each of them as a

**[14:05]** and then commit each of them as a

**[14:05]** and then commit each of them as a checkpoint to build both working

**[14:08]** checkpoint to build both working

**[14:08]** checkpoint to build both working software and engineering knowledge.

**[14:11]** software and engineering knowledge.

**[14:11]** software and engineering knowledge. We say complete one commit one continue.

**[14:17]** We say complete one commit one continue.

**[14:17]** We say complete one commit one continue. Our next implementation related

**[14:19]** Our next implementation related

**[14:19]** Our next implementation related principle is context engineering and

**[14:21]** principle is context engineering and

**[14:21]** principle is context engineering and management.

**[14:22]** management.

**[14:22]** management. Treating context as something that just

**[14:24]** Treating context as something that just

**[14:24]** Treating context as something that just happens automatically rather than

**[14:26]** happens automatically rather than

**[14:26]** happens automatically rather than something you actively engineer is a big

**[14:28]** something you actively engineer is a big

**[14:28]** something you actively engineer is a big problem. You let conversation history

**[14:31]** problem. You let conversation history

**[14:31]** problem. You let conversation history passively accumulate instead of curating

**[14:34]** passively accumulate instead of curating

**[14:34]** passively accumulate instead of curating actively what really matters for context

**[14:38]** actively what really matters for context

**[14:38]** actively what really matters for context and then if you don't build context

**[14:40]** and then if you don't build context

**[14:40]** and then if you don't build context resilience

**[14:42]** resilience

**[14:42]** resilience state will not persist eventually and we

**[14:46]** state will not persist eventually and we

**[14:46]** state will not persist eventually and we lose resilience and continuity to that

**[14:49]** lose resilience and continuity to that

**[14:49]** lose resilience and continuity to that matter. So the primary idea here is do

**[14:52]** matter. So the primary idea here is do

**[14:52]** matter. So the primary idea here is do not rely on conversational state

**[14:54]** not rely on conversational state

**[14:54]** not rely on conversational state persisting capture architectural

**[14:56]** persisting capture architectural

**[14:56]** persisting capture architectural decisions in persistent documents like

**[14:59]** decisions in persistent documents like

**[14:59]** decisions in persistent documents like specifications plans and design


### [15:00 - 16:00]

**[15:01]** specifications plans and design

**[15:01]** specifications plans and design documents and we'll talk about what

**[15:02]** documents and we'll talk about what

**[15:02]** documents and we'll talk about what those mean here in the process section

**[15:04]** those mean here in the process section

**[15:04]** those mean here in the process section and then build context from these

**[15:06]** and then build context from these

**[15:06]** and then build context from these artifacts not from your memory. We say

**[15:10]** artifacts not from your memory. We say

**[15:10]** artifacts not from your memory. We say curate context don't accumulate it.

**[15:14]** curate context don't accumulate it.

**[15:14]** curate context don't accumulate it. And our last principle is make it work,

**[15:18]** And our last principle is make it work,

**[15:18]** And our last principle is make it work, make it right, make it fast. And this is

**[15:21]** make it right, make it fast. And this is

**[15:21]** make it right, make it fast. And this is borrowed from the annals of software

**[15:24]** borrowed from the annals of software

**[15:24]** borrowed from the annals of software engineering. But treating all three

**[15:27]** engineering. But treating all three

**[15:27]** engineering. But treating all three phases of this as equal from the start

**[15:30]** phases of this as equal from the start

**[15:30]** phases of this as equal from the start or trying to achieve them all

**[15:32]** or trying to achieve them all

**[15:32]** or trying to achieve them all simultaneously is a big problem. The

**[15:35]** simultaneously is a big problem. The

**[15:35]** simultaneously is a big problem. The framework focuses on getting to make it

**[15:37]** framework focuses on getting to make it

**[15:38]** framework focuses on getting to make it work. working software that can be

**[15:40]** work. working software that can be

**[15:40]** work. working software that can be shipped and used and then only after

**[15:42]** shipped and used and then only after

**[15:42]** shipped and used and then only after real usage reveals what matters do we

**[15:45]** real usage reveals what matters do we

**[15:45]** real usage reveals what matters do we selectively invest in make it right and

**[15:49]** selectively invest in make it right and

**[15:49]** selectively invest in make it right and make it fast. So the big idea here is

**[15:52]** make it fast. So the big idea here is

**[15:52]** make it fast. So the big idea here is stop pursuing elegance and performance

**[15:53]** stop pursuing elegance and performance

**[15:53]** stop pursuing elegance and performance upfront. Explicitly direct the agents to

**[15:57]** upfront. Explicitly direct the agents to

**[15:57]** upfront. Explicitly direct the agents to make it work and we'll talk about how to


### [16:00 - 17:00]

**[16:00]** make it work and we'll talk about how to

**[16:00]** make it work and we'll talk about how to define that. But we want simple

**[16:03]** define that. But we want simple

**[16:03]** define that. But we want simple functional implementation that passes

**[16:05]** functional implementation that passes

**[16:05]** functional implementation that passes tests and enables us to ship quickly and

**[16:07]** tests and enables us to ship quickly and

**[16:07]** tests and enables us to ship quickly and then let real usage reveal what deserves

**[16:11]** then let real usage reveal what deserves

**[16:11]** then let real usage reveal what deserves further investment. We say burn sorry we

**[16:14]** further investment. We say burn sorry we

**[16:14]** further investment. We say burn sorry we say build, learn,

**[16:17]** say build, learn,

**[16:17]** say build, learn, improve. So there we have them. our 10

**[16:20]** improve. So there we have them. our 10

**[16:20]** improve. So there we have them. our 10 principles,

**[16:27]** the philosophy that makes the framework

**[16:27]** the philosophy that makes the framework work.

**[16:30]** work.

**[16:30]** work. Now, let's check back in with our hung

**[16:32]** Now, let's check back in with our hung

**[16:32]** Now, let's check back in with our hung over vibe coder as he's been exposed to

**[16:35]** over vibe coder as he's been exposed to

**[16:35]** over vibe coder as he's been exposed to the principles of the framework.

**[16:39]** the principles of the framework.

**[16:39]** the principles of the framework. Yeah, mind sufficiently blown yet? Well,

**[16:43]** Yeah, mind sufficiently blown yet? Well,

**[16:43]** Yeah, mind sufficiently blown yet? Well, stick with us, mate. It gets even

**[16:44]** stick with us, mate. It gets even

**[16:44]** stick with us, mate. It gets even better.

**[16:46]** better.

**[16:46]** better. All right. Now, let's transition to

**[16:49]** All right. Now, let's transition to

**[16:49]** All right. Now, let's transition to process.

**[16:50]** process.

**[16:50]** process. The process is where we put all of the

**[16:53]** The process is where we put all of the

**[16:53]** The process is where we put all of the principles to work. You can think about

**[16:55]** principles to work. You can think about

**[16:55]** principles to work. You can think about this as principles in action. The

**[16:58]** this as principles in action. The

**[16:58]** this as principles in action. The framework process has two distinct


### [17:00 - 18:00]

**[17:00]** framework process has two distinct

**[17:00]** framework process has two distinct phases. There's the planning phase where

**[17:03]** phases. There's the planning phase where

**[17:03]** phases. There's the planning phase where you do all of the architectural thinking

**[17:05]** you do all of the architectural thinking

**[17:05]** you do all of the architectural thinking to define what to build and then the

**[17:07]** to define what to build and then the

**[17:07]** to define what to build and then the implementation phase where the agent

**[17:09]** implementation phase where the agent

**[17:10]** implementation phase where the agent executes your specifications with both

**[17:12]** executes your specifications with both

**[17:12]** executes your specifications with both your oversight and validation.

**[17:15]** your oversight and validation.

**[17:15]** your oversight and validation. Planning produces the artifacts that

**[17:17]** Planning produces the artifacts that

**[17:17]** Planning produces the artifacts that enable autonomous agent implementation.

**[17:21]** enable autonomous agent implementation.

**[17:21]** enable autonomous agent implementation. Implementation then uses those artifacts

**[17:23]** Implementation then uses those artifacts

**[17:24]** Implementation then uses those artifacts to build working software feature by

**[17:26]** to build working software feature by

**[17:26]** to build working software feature by feature.

**[17:28]** feature.

**[17:28]** feature. All right, on to the planning phase.

**[17:31]** All right, on to the planning phase.

**[17:31]** All right, on to the planning phase. Planning is where you complete your

**[17:32]** Planning is where you complete your

**[17:32]** Planning is where you complete your architectural thinking. You transform a

**[17:35]** architectural thinking. You transform a

**[17:36]** architectural thinking. You transform a vague project idea into atomic sequenced

**[17:40]** vague project idea into atomic sequenced

**[17:40]** vague project idea into atomic sequenced fully specified features ready for

**[17:42]** fully specified features ready for

**[17:42]** fully specified features ready for implementation.

**[17:43]** implementation.

**[17:43]** implementation. This is purely your work. Architectural

**[17:46]** This is purely your work. Architectural

**[17:46]** This is purely your work. Architectural decisions, decomposition, specification

**[17:49]** decisions, decomposition, specification

**[17:49]** decisions, decomposition, specification writing, dependency analysis. The agent

**[17:53]** writing, dependency analysis. The agent

**[17:53]** writing, dependency analysis. The agent can assist as a thinking partner, but

**[17:55]** can assist as a thinking partner, but

**[17:55]** can assist as a thinking partner, but you make every decision.

**[17:58]** you make every decision.

**[17:58]** you make every decision. The five planning steps are sequential


### [18:00 - 19:00]

**[18:01]** The five planning steps are sequential

**[18:01]** The five planning steps are sequential and build on each other. Vision,

**[18:04]** and build on each other. Vision,

**[18:04]** and build on each other. Vision, features, specification, dependencies,

**[18:08]** features, specification, dependencies,

**[18:08]** features, specification, dependencies, plan.

**[18:11]** plan.

**[18:11]** plan. You'll notice that this is a highly

**[18:13]** You'll notice that this is a highly

**[18:13]** You'll notice that this is a highly iterative process of extracting and

**[18:15]** iterative process of extracting and

**[18:15]** iterative process of extracting and refining thinking into tangible

**[18:17]** refining thinking into tangible

**[18:17]** refining thinking into tangible artifacts that can be used to build

**[18:19]** artifacts that can be used to build

**[18:19]** artifacts that can be used to build software with the agent. The inputs and

**[18:23]** software with the agent. The inputs and

**[18:23]** software with the agent. The inputs and outputs of each step in the planning

**[18:25]** outputs of each step in the planning

**[18:25]** outputs of each step in the planning phase are templates and completed

**[18:27]** phase are templates and completed

**[18:28]** phase are templates and completed templates respectively. Heaps of work

**[18:30]** templates respectively. Heaps of work

**[18:30]** templates respectively. Heaps of work has been done in advance to create

**[18:33]** has been done in advance to create

**[18:33]** has been done in advance to create well-thought well ststructured templates

**[18:36]** well-thought well ststructured templates

**[18:36]** well-thought well ststructured templates to both guide thinking and capture the

**[18:39]** to both guide thinking and capture the

**[18:39]** to both guide thinking and capture the results.

**[18:41]** results.

**[18:41]** results. So the first step of planning is vision

**[18:44]** So the first step of planning is vision

**[18:44]** So the first step of planning is vision capture. And the purpose of this step is

**[18:46]** capture. And the purpose of this step is

**[18:46]** capture. And the purpose of this step is to transform your vague project idea

**[18:49]** to transform your vague project idea

**[18:49]** to transform your vague project idea into a complete structured master

**[18:52]** into a complete structured master

**[18:52]** into a complete structured master project specification that articulates

**[18:54]** project specification that articulates

**[18:54]** project specification that articulates the problem, the users, functionality,

**[18:58]** the problem, the users, functionality,

**[18:58]** the problem, the users, functionality, scope and workflows.


### [19:00 - 20:00]

**[19:00]** scope and workflows.

**[19:00]** scope and workflows. So the problem that this step in the

**[19:02]** So the problem that this step in the

**[19:02]** So the problem that this step in the planning phase solves is that your

**[19:04]** planning phase solves is that your

**[19:04]** planning phase solves is that your initial project idea exists only in your

**[19:07]** initial project idea exists only in your

**[19:07]** initial project idea exists only in your head usually and it's incomplete. When

**[19:09]** head usually and it's incomplete. When

**[19:09]** head usually and it's incomplete. When we start, this is typically the case.

**[19:11]** we start, this is typically the case.

**[19:11]** we start, this is typically the case. You have some general sense of the

**[19:13]** You have some general sense of the

**[19:13]** You have some general sense of the problem and an approach, but details are

**[19:15]** problem and an approach, but details are

**[19:15]** problem and an approach, but details are fuzzy. Implicit assumptions are

**[19:17]** fuzzy. Implicit assumptions are

**[19:17]** fuzzy. Implicit assumptions are unexamined and critical aspects are

**[19:19]** unexamined and critical aspects are

**[19:19]** unexamined and critical aspects are uninformed.

**[19:20]** uninformed.

**[19:20]** uninformed. So without structured exploration and

**[19:23]** So without structured exploration and

**[19:23]** So without structured exploration and refinement, you can't communicate your

**[19:25]** refinement, you can't communicate your

**[19:25]** refinement, you can't communicate your thinking, you can't articulate

**[19:27]** thinking, you can't articulate

**[19:27]** thinking, you can't articulate requirements clearly, and you can't

**[19:29]** requirements clearly, and you can't

**[19:29]** requirements clearly, and you can't create a shared foundation that agents

**[19:31]** create a shared foundation that agents

**[19:31]** create a shared foundation that agents can build upon. You need to examine and

**[19:34]** can build upon. You need to examine and

**[19:34]** can build upon. You need to examine and refine your thinking before you can

**[19:35]** refine your thinking before you can

**[19:36]** refine your thinking before you can decompose it into features or

**[19:37]** decompose it into features or

**[19:37]** decompose it into features or architecture. And so what we're going to

**[19:40]** architecture. And so what we're going to

**[19:40]** architecture. And so what we're going to do here is think out loud with an agent.

**[19:43]** do here is think out loud with an agent.

**[19:43]** do here is think out loud with an agent. Optionally, but strongly recommended to

**[19:46]** Optionally, but strongly recommended to

**[19:46]** Optionally, but strongly recommended to refine and capture your vision through

**[19:48]** refine and capture your vision through

**[19:48]** refine and capture your vision through five sections.

**[19:51]** five sections.

**[19:51]** five sections. Project purpose. So we clarify the pro

**[19:54]** Project purpose. So we clarify the pro

**[19:54]** Project purpose. So we clarify the pro the problem that you're solving, who

**[19:56]** the problem that you're solving, who

**[19:56]** the problem that you're solving, who experiences it, and the core value that

**[19:58]** experiences it, and the core value that

**[19:58]** experiences it, and the core value that your software delivers.


### [20:00 - 21:00]

**[20:01]** your software delivers.

**[20:01]** your software delivers. Essential functionality.

**[20:03]** Essential functionality.

**[20:03]** Essential functionality. Identify the three to five fundamental

**[20:06]** Identify the three to five fundamental

**[20:06]** Identify the three to five fundamental workflows that solve the problem. Scope

**[20:09]** workflows that solve the problem. Scope

**[20:09]** workflows that solve the problem. Scope boundaries. Make explicit decisions. And

**[20:12]** boundaries. Make explicit decisions. And

**[20:12]** boundaries. Make explicit decisions. And we call these now, not next. So now as

**[20:16]** we call these now, not next. So now as

**[20:16]** we call these now, not next. So now as in must have it for the make it work

**[20:19]** in must have it for the make it work

**[20:19]** in must have it for the make it work version. Not meaning it's out of scope

**[20:22]** version. Not meaning it's out of scope

**[20:22]** version. Not meaning it's out of scope and next meaning future enhancements.

**[20:26]** and next meaning future enhancements.

**[20:26]** and next meaning future enhancements. Then technical context.

**[20:29]** Then technical context.

**[20:29]** Then technical context. answer basic questions like where does

**[20:31]** answer basic questions like where does

**[20:31]** answer basic questions like where does it run? How do users interact? What

**[20:33]** it run? How do users interact? What

**[20:33]** it run? How do users interact? What systems does it connect to? And then

**[20:35]** systems does it connect to? And then

**[20:35]** systems does it connect to? And then lastly, workflow details. So for each of

**[20:38]** lastly, workflow details. So for each of

**[20:38]** lastly, workflow details. So for each of those three to five core workflows,

**[20:40]** those three to five core workflows,

**[20:40]** those three to five core workflows, document the goal, document the highle

**[20:43]** document the goal, document the highle

**[20:43]** document the goal, document the highle steps for each of the the workflows and

**[20:45]** steps for each of the the workflows and

**[20:45]** steps for each of the the workflows and then the expected outcome.

**[20:47]** then the expected outcome.

**[20:47]** then the expected outcome. And we iterate through these sections

**[20:50]** And we iterate through these sections

**[20:50]** And we iterate through these sections until your vision is clear and complete.

**[20:54]** until your vision is clear and complete.

**[20:54]** until your vision is clear and complete. Working with an agent here is really

**[20:55]** Working with an agent here is really

**[20:55]** Working with an agent here is really great because it can help surface gaps,

**[20:57]** great because it can help surface gaps,

**[20:57]** great because it can help surface gaps, suggest edge cases and probe

**[20:59]** suggest edge cases and probe

**[20:59]** suggest edge cases and probe assumptions. But critically, you make


### [21:00 - 22:00]

**[21:01]** assumptions. But critically, you make

**[21:01]** assumptions. But critically, you make all decisions about the vision.

**[21:04]** all decisions about the vision.

**[21:04]** all decisions about the vision. The primary output of this step

**[21:07]** The primary output of this step

**[21:07]** The primary output of this step [clears throat] is the master project

**[21:08]** [clears throat] is the master project

**[21:08]** [clears throat] is the master project specification.

**[21:10]** specification.

**[21:10]** specification. And this is a structured artifact that

**[21:11]** And this is a structured artifact that

**[21:12]** And this is a structured artifact that captures your complete vision for the

**[21:14]** captures your complete vision for the

**[21:14]** captures your complete vision for the software in its make it work version.

**[21:16]** software in its make it work version.

**[21:16]** software in its make it work version. This becomes the foundation for

**[21:18]** This becomes the foundation for

**[21:18]** This becomes the foundation for extracting features in planning step

**[21:21]** extracting features in planning step

**[21:21]** extracting features in planning step two. And as we go through every step in

**[21:25]** two. And as we go through every step in

**[21:25]** two. And as we go through every step in the process, you can see down here on

**[21:28]** the process, you can see down here on

**[21:28]** the process, you can see down here on the bottom left corner which of the

**[21:30]** the bottom left corner which of the

**[21:30]** the bottom left corner which of the principles are applied in that step. We

**[21:33]** principles are applied in that step. We

**[21:33]** principles are applied in that step. We won't talk through each of the

**[21:34]** won't talk through each of the

**[21:34]** won't talk through each of the principles, but this demonstrates the

**[21:36]** principles, but this demonstrates the

**[21:36]** principles, but this demonstrates the cohesiveness of the framework.

**[21:43]** All right, step two in planning is

**[21:43]** All right, step two in planning is feature identification and

**[21:45]** feature identification and

**[21:45]** feature identification and categorization.

**[21:46]** categorization.

**[21:46]** categorization. And the purpose of this step is to

**[21:48]** And the purpose of this step is to

**[21:48]** And the purpose of this step is to systematically extract all units of

**[21:50]** systematically extract all units of

**[21:50]** systematically extract all units of functionality from your master project

**[21:52]** functionality from your master project

**[21:52]** functionality from your master project specification and then organize them

**[21:54]** specification and then organize them

**[21:54]** specification and then organize them into a categorized feature inventory.

**[21:57]** into a categorized feature inventory.

**[21:58]** into a categorized feature inventory. The problem that this solves is you

**[21:59]** The problem that this solves is you

**[21:59]** The problem that this solves is you don't jump directly from highle vision


### [22:00 - 23:00]

**[22:01]** don't jump directly from highle vision

**[22:02]** don't jump directly from highle vision to detailed feature specifications.

**[22:04]** to detailed feature specifications.

**[22:04]** to detailed feature specifications. That's too big of a leap. Your master

**[22:07]** That's too big of a leap. Your master

**[22:07]** That's too big of a leap. Your master project specification captures what the

**[22:10]** project specification captures what the

**[22:10]** project specification captures what the software does at a high level, but you

**[22:12]** software does at a high level, but you

**[22:12]** software does at a high level, but you need an intermediate step that

**[22:13]** need an intermediate step that

**[22:13]** need an intermediate step that progressively refineses this thinking

**[22:15]** progressively refineses this thinking

**[22:15]** progressively refineses this thinking into concrete, manageable units of

**[22:17]** into concrete, manageable units of

**[22:17]** into concrete, manageable units of functionality.

**[22:19]** functionality.

**[22:19]** functionality. Without systematic extraction and

**[22:21]** Without systematic extraction and

**[22:21]** Without systematic extraction and categorization, you're trying to specify

**[22:24]** categorization, you're trying to specify

**[22:24]** categorization, you're trying to specify features without a complete inventory of

**[22:25]** features without a complete inventory of

**[22:25]** features without a complete inventory of what needs to be built, and you can't

**[22:28]** what needs to be built, and you can't

**[22:28]** what needs to be built, and you can't see natural groupings and relationships.

**[22:31]** see natural groupings and relationships.

**[22:31]** see natural groupings and relationships. You lack the structured artifact that's

**[22:32]** You lack the structured artifact that's

**[22:32]** You lack the structured artifact that's needed for the next refinement step and

**[22:35]** needed for the next refinement step and

**[22:35]** needed for the next refinement step and you're forced to hold all functionality

**[22:37]** you're forced to hold all functionality

**[22:37]** you're forced to hold all functionality in your head rather than externalizing

**[22:39]** in your head rather than externalizing

**[22:39]** in your head rather than externalizing it for analysis.

**[22:41]** it for analysis.

**[22:41]** it for analysis. The input to this step is the master

**[22:43]** The input to this step is the master

**[22:43]** The input to this step is the master project specification from the previous

**[22:45]** project specification from the previous

**[22:45]** project specification from the previous step. And so what we're going to do here

**[22:47]** step. And so what we're going to do here

**[22:47]** step. And so what we're going to do here is systematically analyze the master

**[22:49]** is systematically analyze the master

**[22:49]** is systematically analyze the master project specification to extract all

**[22:51]** project specification to extract all

**[22:51]** project specification to extract all units of functionality and then

**[22:53]** units of functionality and then

**[22:53]** units of functionality and then categorize them.

**[22:55]** categorize them.

**[22:55]** categorize them. [clears throat and cough] H so work

**[22:57]** [clears throat and cough] H so work

**[22:57]** [clears throat and cough] H so work through the master project specification

**[22:59]** through the master project specification


### [23:00 - 24:00]

**[23:00]** through the master project specification step by step or section by section

**[23:02]** step by step or section by section

**[23:02]** step by step or section by section rather with targeted extraction

**[23:05]** rather with targeted extraction

**[23:05]** rather with targeted extraction questions. So it's like for project

**[23:07]** questions. So it's like for project

**[23:07]** questions. So it's like for project purpose what foundational capabilities

**[23:10]** purpose what foundational capabilities

**[23:10]** purpose what foundational capabilities does this system need for essential

**[23:13]** does this system need for essential

**[23:13]** does this system need for essential functionality what discrete capabilities

**[23:15]** functionality what discrete capabilities

**[23:15]** functionality what discrete capabilities are required for each of the workflows

**[23:17]** are required for each of the workflows

**[23:17]** are required for each of the workflows for scope boundaries. What

**[23:19]** for scope boundaries. What

**[23:19]** for scope boundaries. What infrastructure is needed to make the

**[23:22]** infrastructure is needed to make the

**[23:22]** infrastructure is needed to make the make it work version work now for

**[23:26]** make it work version work now for

**[23:26]** make it work version work now for technical context? What platform

**[23:28]** technical context? What platform

**[23:28]** technical context? What platform integration and interface features are

**[23:30]** integration and interface features are

**[23:30]** integration and interface features are needed for each of the key workflows?

**[23:34]** needed for each of the key workflows?

**[23:34]** needed for each of the key workflows? What handles input? What processing

**[23:36]** What handles input? What processing

**[23:36]** What handles input? What processing occurs? What output is there? Which

**[23:38]** occurs? What output is there? Which

**[23:38]** occurs? What output is there? Which errors should we anticipate? And how do

**[23:40]** errors should we anticipate? And how do

**[23:40]** errors should we anticipate? And how do we feed back? And then cross cutting

**[23:43]** we feed back? And then cross cutting

**[23:43]** we feed back? And then cross cutting needs across all of this. what security

**[23:46]** needs across all of this. what security

**[23:46]** needs across all of this. what security logging configuration and testing

**[23:48]** logging configuration and testing

**[23:48]** logging configuration and testing features span the entire system. We're

**[23:50]** features span the entire system. We're

**[23:50]** features span the entire system. We're going to document each feature source

**[23:53]** going to document each feature source

**[23:53]** going to document each feature source for traceability and that's where it

**[23:55]** for traceability and that's where it

**[23:55]** for traceability and that's where it came from in the master project

**[23:56]** came from in the master project

**[23:56]** came from in the master project specification.

**[23:58]** specification.

**[23:58]** specification. Next, we build the raw feature list. So,


### [24:00 - 25:00]

**[24:01]** Next, we build the raw feature list. So,

**[24:01]** Next, we build the raw feature list. So, we capture every capability [sighs] that

**[24:04]** we capture every capability [sighs] that

**[24:04]** we capture every capability [sighs] that you identify, but we're not going to

**[24:05]** you identify, but we're not going to

**[24:05]** you identify, but we're not going to organize these just yet. Just ensure

**[24:07]** organize these just yet. Just ensure

**[24:07]** organize these just yet. Just ensure that we have comprehensive extraction.

**[24:14]** We want to challenge completeness with

**[24:14]** We want to challenge completeness with questions like what handles errors or

**[24:16]** questions like what handles errors or

**[24:16]** questions like what handles errors or what validates input? What provides

**[24:18]** what validates input? What provides

**[24:18]** what validates input? What provides feedback?

**[24:20]** feedback?

**[24:20]** feedback? Next, we move on to analyzing those

**[24:22]** Next, we move on to analyzing those

**[24:22]** Next, we move on to analyzing those features. So, we analyze the entire

**[24:24]** features. So, we analyze the entire

**[24:24]** features. So, we analyze the entire feature list to start identifying

**[24:26]** feature list to start identifying

**[24:26]** feature list to start identifying natural groupings based on your features

**[24:29]** natural groupings based on your features

**[24:29]** natural groupings based on your features and your project type. You identify,

**[24:32]** and your project type. You identify,

**[24:32]** and your project type. You identify, it's not a hard rule, but three to seven

**[24:34]** it's not a hard rule, but three to seven

**[24:34]** it's not a hard rule, but three to seven categories that kind of reflect how your

**[24:37]** categories that kind of reflect how your

**[24:37]** categories that kind of reflect how your specific software is structured. And

**[24:39]** specific software is structured. And

**[24:39]** specific software is structured. And then we move on to categorization.

**[24:41]** then we move on to categorization.

**[24:41]** then we move on to categorization. Determine the categories. We assign each

**[24:44]** Determine the categories. We assign each

**[24:44]** Determine the categories. We assign each feature to its best fit category. And

**[24:46]** feature to its best fit category. And

**[24:46]** feature to its best fit category. And then we create a unique feature ID like

**[24:49]** then we create a unique feature ID like

**[24:49]** then we create a unique feature ID like for example core 001 or API 101. These

**[24:55]** for example core 001 or API 101. These

**[24:55]** for example core 001 or API 101. These categories emerge from analyzing your

**[24:57]** categories emerge from analyzing your

**[24:57]** categories emerge from analyzing your actual features and not from

**[24:58]** actual features and not from

**[24:58]** actual features and not from predetermined category templates.


### [25:00 - 26:00]

**[25:01]** predetermined category templates.

**[25:01]** predetermined category templates. And then [clears throat] lastly, we

**[25:03]** And then [clears throat] lastly, we

**[25:03]** And then [clears throat] lastly, we estimate feature complexity. And this is

**[25:04]** estimate feature complexity. And this is

**[25:04]** estimate feature complexity. And this is just an initial estimate of how complex

**[25:06]** just an initial estimate of how complex

**[25:06]** just an initial estimate of how complex each extracted feature is. Is it easy?

**[25:09]** each extracted feature is. Is it easy?

**[25:09]** each extracted feature is. Is it easy? Is it medium? Is it hard? So the output

**[25:12]** Is it medium? Is it hard? So the output

**[25:12]** Is it medium? Is it hard? So the output from this step is the feature inventory.

**[25:15]** from this step is the feature inventory.

**[25:15]** from this step is the feature inventory. It's a complete categorized list of all

**[25:18]** It's a complete categorized list of all

**[25:18]** It's a complete categorized list of all discrete units of functionality. Each

**[25:20]** discrete units of functionality. Each

**[25:20]** discrete units of functionality. Each feature includes a unique ID, a

**[25:22]** feature includes a unique ID, a

**[25:22]** feature includes a unique ID, a description, a complexity estimate, and

**[25:24]** description, a complexity estimate, and

**[25:24]** description, a complexity estimate, and we're able to trace it back to its

**[25:26]** we're able to trace it back to its

**[25:26]** we're able to trace it back to its source section in the MPS.

**[25:35]** Step three is iterative specification

**[25:35]** Step three is iterative specification development.

**[25:36]** development.

**[25:36]** development. >> [clears throat]

**[25:37]** >> [clears throat]

**[25:37]** >> [clears throat] >> The purpose of this step is to transform

**[25:39]** >> The purpose of this step is to transform

**[25:39]** >> The purpose of this step is to transform each feature from your feature inventory

**[25:42]** each feature from your feature inventory

**[25:42]** each feature from your feature inventory into a complete atomic implementation

**[25:46]** into a complete atomic implementation

**[25:46]** into a complete atomic implementation ready specification that defines exactly

**[25:48]** ready specification that defines exactly

**[25:48]** ready specification that defines exactly what needs to be built, how it will be

**[25:51]** what needs to be built, how it will be

**[25:51]** what needs to be built, how it will be validated and what it depends on. The

**[25:54]** validated and what it depends on. The

**[25:54]** validated and what it depends on. The problem that this critical step solves

**[25:56]** problem that this critical step solves

**[25:56]** problem that this critical step solves is you can't jump directly from a

**[25:58]** is you can't jump directly from a

**[25:58]** is you can't jump directly from a feature inventory to feature

**[25:59]** feature inventory to feature

**[25:59]** feature inventory to feature implementation. That's again too big of


### [26:00 - 27:00]

**[26:02]** implementation. That's again too big of

**[26:02]** implementation. That's again too big of a leap. So your feature inventory lists

**[26:05]** a leap. So your feature inventory lists

**[26:05]** a leap. So your feature inventory lists discrete capabilities, but each feature

**[26:07]** discrete capabilities, but each feature

**[26:07]** discrete capabilities, but each feature still needs to be fully specified before

**[26:10]** still needs to be fully specified before

**[26:10]** still needs to be fully specified before a coding agent can implement it. Without

**[26:13]** a coding agent can implement it. Without

**[26:13]** a coding agent can implement it. Without iterative features,

**[26:15]** iterative features,

**[26:15]** iterative features, [clears throat and cough]

**[26:15]** [clears throat and cough]

**[26:15]** [clears throat and cough] sorry, without iterative specification

**[26:18]** sorry, without iterative specification

**[26:18]** sorry, without iterative specification development, you're giving coding agents

**[26:20]** development, you're giving coding agents

**[26:20]** development, you're giving coding agents highle descriptions and hoping that they

**[26:22]** highle descriptions and hoping that they

**[26:22]** highle descriptions and hoping that they infer details correctly. You can't

**[26:25]** infer details correctly. You can't

**[26:25]** infer details correctly. You can't validate that features are truly atomic

**[26:27]** validate that features are truly atomic

**[26:27]** validate that features are truly atomic until you try to specify them. You have

**[26:30]** until you try to specify them. You have

**[26:30]** until you try to specify them. You have no systematic way to identify

**[26:32]** no systematic way to identify

**[26:32]** no systematic way to identify dependencies.

**[26:34]** dependencies.

**[26:34]** dependencies. You lack the implementation blueprints

**[26:36]** You lack the implementation blueprints

**[26:36]** You lack the implementation blueprints that enable autonomous agent work. And

**[26:40]** that enable autonomous agent work. And

**[26:40]** that enable autonomous agent work. And ultimately, you're relying on prompt

**[26:42]** ultimately, you're relying on prompt

**[26:42]** ultimately, you're relying on prompt engineering instead of comprehensive

**[26:43]** engineering instead of comprehensive

**[26:44]** engineering instead of comprehensive specifications.

**[26:46]** specifications.

**[26:46]** specifications. The input to this step is the feature

**[26:49]** The input to this step is the feature

**[26:49]** The input to this step is the feature inventory from the previous step. And so

**[26:51]** inventory from the previous step. And so

**[26:51]** inventory from the previous step. And so what we're going to do here is

**[26:53]** what we're going to do here is

**[26:53]** what we're going to do here is collaborate with an agent to transform

**[26:55]** collaborate with an agent to transform

**[26:55]** collaborate with an agent to transform each feature using a three-level

**[26:57]** each feature using a three-level

**[26:57]** each feature using a three-level refinement pattern.


### [27:00 - 28:00]

**[27:00]** refinement pattern.

**[27:00]** refinement pattern. So first we draft a user story in the

**[27:04]** So first we draft a user story in the

**[27:04]** So first we draft a user story in the typical user story fashion. As a user

**[27:07]** typical user story fashion. As a user

**[27:07]** typical user story fashion. As a user type, I want to perform some action so

**[27:10]** type, I want to perform some action so

**[27:10]** type, I want to perform some action so that I can obtain some benefit. This

**[27:13]** that I can obtain some benefit. This

**[27:13]** that I can obtain some benefit. This captures who needs this, what they're

**[27:14]** captures who needs this, what they're

**[27:14]** captures who needs this, what they're doing, and why it matters.

**[27:17]** doing, and why it matters.

**[27:17]** doing, and why it matters. Next, we def determine our

**[27:20]** Next, we def determine our

**[27:20]** Next, we def determine our implementation contracts, and

**[27:22]** implementation contracts, and

**[27:22]** implementation contracts, and [clears throat] these exist in three

**[27:25]** [clears throat] these exist in three

**[27:25]** [clears throat] these exist in three iterative levels of refinement. So we

**[27:27]** iterative levels of refinement. So we

**[27:27]** iterative levels of refinement. So we start at level one in plain English.

**[27:31]** start at level one in plain English.

**[27:31]** start at level one in plain English. Just describe what the feature does in

**[27:32]** Just describe what the feature does in

**[27:32]** Just describe what the feature does in natural language. Walk through what

**[27:34]** natural language. Walk through what

**[27:34]** natural language. Walk through what happens, what it receives, what it does,

**[27:37]** happens, what it receives, what it does,

**[27:37]** happens, what it receives, what it does, and what it produces. We then take that

**[27:41]** and what it produces. We then take that

**[27:41]** and what it produces. We then take that [clears throat] and refine it further to

**[27:43]** [clears throat] and refine it further to

**[27:43]** [clears throat] and refine it further to level two to logic flow. Kind of the

**[27:46]** level two to logic flow. Kind of the

**[27:46]** level two to logic flow. Kind of the input, logic, output. We translate the

**[27:49]** input, logic, output. We translate the

**[27:49]** input, logic, output. We translate the description into structured pseudo code

**[27:52]** description into structured pseudo code

**[27:52]** description into structured pseudo code with clear input, step-by-step logic,

**[27:55]** with clear input, step-by-step logic,

**[27:55]** with clear input, step-by-step logic, and then defined output. And this really

**[27:58]** and then defined output. And this really

**[27:58]** and then defined output. And this really forces clarity about what comes in, what


### [28:00 - 29:00]

**[28:01]** forces clarity about what comes in, what

**[28:01]** forces clarity about what comes in, what happens, and what goes out.

**[28:04]** happens, and what goes out.

**[28:04]** happens, and what goes out. And then we refine further to level

**[28:06]** And then we refine further to level

**[28:06]** And then we refine further to level three, which is formal interfaces. And

**[28:08]** three, which is formal interfaces. And

**[28:08]** three, which is formal interfaces. And here's where we define and formalize

**[28:10]** here's where we define and formalize

**[28:10]** here's where we define and formalize contracts with exact signatures, data

**[28:13]** contracts with exact signatures, data

**[28:13]** contracts with exact signatures, data structures, and API specifications.

**[28:16]** structures, and API specifications.

**[28:16]** structures, and API specifications. We define exact input types, return

**[28:19]** We define exact input types, return

**[28:19]** We define exact input types, return types, and errors for each component.

**[28:23]** types, and errors for each component.

**[28:23]** types, and errors for each component. Next, we move on to specifying

**[28:24]** Next, we move on to specifying

**[28:24]** Next, we move on to specifying validation contracts.

**[28:27]** validation contracts.

**[28:27]** validation contracts. And again, we do this in three levels.

**[28:31]** And again, we do this in three levels.

**[28:31]** And again, we do this in three levels. Level one is once again plain English.

**[28:33]** Level one is once again plain English.

**[28:33]** Level one is once again plain English. So, we describe the scenarios, identify

**[28:36]** So, we describe the scenarios, identify

**[28:36]** So, we describe the scenarios, identify all situations that need validation,

**[28:39]** all situations that need validation,

**[28:39]** all situations that need validation, happy path, error cases, edge cases,

**[28:42]** happy path, error cases, edge cases,

**[28:42]** happy path, error cases, edge cases, security properties. We then refine that

**[28:45]** security properties. We then refine that

**[28:45]** security properties. We then refine that to level two which is our test logic and

**[28:48]** to level two which is our test logic and

**[28:48]** to level two which is our test logic and we use given when then structure for

**[28:51]** we use given when then structure for

**[28:51]** we use given when then structure for that. So we translate each scenario into

**[28:54]** that. So we translate each scenario into

**[28:54]** that. So we translate each scenario into structured verification logic with setup

**[28:56]** structured verification logic with setup

**[28:56]** structured verification logic with setup trigger and expected outcomes.


### [29:00 - 30:00]

**[29:00]** trigger and expected outcomes.

**[29:00]** trigger and expected outcomes. We further then refine that to our third

**[29:02]** We further then refine that to our third

**[29:02]** We further then refine that to our third level which is once or analogous to the

**[29:04]** level which is once or analogous to the

**[29:04]** level which is once or analogous to the previous step formal test definition.

**[29:06]** previous step formal test definition.

**[29:06]** previous step formal test definition. And so this is where we define exact

**[29:08]** And so this is where we define exact

**[29:08]** And so this is where we define exact test interfaces with setup inputs

**[29:11]** test interfaces with setup inputs

**[29:11]** test interfaces with setup inputs precise assertions and any tear down.

**[29:15]** precise assertions and any tear down.

**[29:15]** precise assertions and any tear down. And at this point we need to validate

**[29:18]** And at this point we need to validate

**[29:18]** And at this point we need to validate the atomicity of the feature. We need to

**[29:20]** the atomicity of the feature. We need to

**[29:20]** the atomicity of the feature. We need to make sure that the feature can be

**[29:22]** make sure that the feature can be

**[29:22]** make sure that the feature can be implemented in a single focused session

**[29:25]** implemented in a single focused session

**[29:25]** implemented in a single focused session and that it is truly one atomic feature.

**[29:28]** and that it is truly one atomic feature.

**[29:28]** and that it is truly one atomic feature. We've defined feature atomicity

**[29:30]** We've defined feature atomicity

**[29:30]** We've defined feature atomicity previously. But if this feels at this

**[29:33]** previously. But if this feels at this

**[29:33]** previously. But if this feels at this point like the specification is

**[29:34]** point like the specification is

**[29:34]** point like the specification is scattered or it defines or describes

**[29:37]** scattered or it defines or describes

**[29:37]** scattered or it defines or describes multiple capabilities, we're going to

**[29:39]** multiple capabilities, we're going to

**[29:39]** multiple capabilities, we're going to split the feature into multiple features

**[29:43]** split the feature into multiple features

**[29:43]** split the feature into multiple features and then repeat the process.

**[29:46]** and then repeat the process.

**[29:46]** and then repeat the process. Then lastly, after we've determined that

**[29:49]** Then lastly, after we've determined that

**[29:49]** Then lastly, after we've determined that the feature is atomic, we're going to

**[29:52]** the feature is atomic, we're going to

**[29:52]** the feature is atomic, we're going to identify dependencies. And this is now

**[29:53]** identify dependencies. And this is now

**[29:54]** identify dependencies. And this is now where we really determine what other

**[29:55]** where we really determine what other

**[29:55]** where we really determine what other features must exist before this one can

**[29:58]** features must exist before this one can

**[29:58]** features must exist before this one can be implemented. We document explicit


### [30:00 - 31:00]

**[30:01]** be implemented. We document explicit

**[30:01]** be implemented. We document explicit binary dependencies meaning this either

**[30:03]** binary dependencies meaning this either

**[30:03]** binary dependencies meaning this either depends on another feature or it

**[30:06]** depends on another feature or it

**[30:06]** depends on another feature or it doesn't. There's no partial dependency.

**[30:09]** doesn't. There's no partial dependency.

**[30:09]** doesn't. There's no partial dependency. The output for this step in the process

**[30:12]** The output for this step in the process

**[30:12]** The output for this step in the process is a complete atomic feature

**[30:15]** is a complete atomic feature

**[30:15]** is a complete atomic feature specification for every single feature

**[30:18]** specification for every single feature

**[30:18]** specification for every single feature in the feature inventory.

**[30:20]** in the feature inventory.

**[30:20]** in the feature inventory. And that spec defines the user story,

**[30:23]** And that spec defines the user story,

**[30:23]** And that spec defines the user story, the technical blueprint which again is

**[30:25]** the technical blueprint which again is

**[30:25]** the technical blueprint which again is comprised of those three levels, the

**[30:28]** comprised of those three levels, the

**[30:28]** comprised of those three levels, the validation strategy and its three

**[30:30]** validation strategy and its three

**[30:30]** validation strategy and its three levels, all of the dependencies and any

**[30:33]** levels, all of the dependencies and any

**[30:33]** levels, all of the dependencies and any implementation notes.

**[30:39]** Step four in the planning process is

**[30:39]** Step four in the planning process is dependency analysis. And so here the

**[30:43]** dependency analysis. And so here the

**[30:43]** dependency analysis. And so here the purpose is to transform our complete set

**[30:45]** purpose is to transform our complete set

**[30:45]** purpose is to transform our complete set of feature specifications into a

**[30:46]** of feature specifications into a

**[30:46]** of feature specifications into a validated dependency matrix that will

**[30:49]** validated dependency matrix that will

**[30:49]** validated dependency matrix that will then define the exact order in which

**[30:51]** then define the exact order in which

**[30:51]** then define the exact order in which features can be implemented. This

**[30:53]** features can be implemented. This

**[30:54]** features can be implemented. This eliminates circular dependencies and

**[30:55]** eliminates circular dependencies and

**[30:55]** eliminates circular dependencies and reveals very natural phases of

**[30:58]** reveals very natural phases of

**[30:58]** reveals very natural phases of implementation.


### [31:00 - 32:00]

**[31:00]** implementation.

**[31:00]** implementation. The problem that this step in the

**[31:02]** The problem that this step in the

**[31:02]** The problem that this step in the process solves is severalfold. that your

**[31:05]** process solves is severalfold. that your

**[31:05]** process solves is severalfold. that your feature specifications contain accurate

**[31:08]** feature specifications contain accurate

**[31:08]** feature specifications contain accurate dependency declarations, but these

**[31:10]** dependency declarations, but these

**[31:10]** dependency declarations, but these dependencies are scattered across

**[31:11]** dependencies are scattered across

**[31:11]** dependencies are scattered across individual documents. So you've got a

**[31:13]** individual documents. So you've got a

**[31:13]** individual documents. So you've got a local picture like feature X depends on

**[31:16]** local picture like feature X depends on

**[31:16]** local picture like feature X depends on feature Y, but we don't have the global

**[31:18]** feature Y, but we don't have the global

**[31:18]** feature Y, but we don't have the global picture yet. And without this global

**[31:20]** picture yet. And without this global

**[31:20]** picture yet. And without this global view synthesized into a dependency

**[31:22]** view synthesized into a dependency

**[31:22]** view synthesized into a dependency matrix, you can't see the complete

**[31:25]** matrix, you can't see the complete

**[31:25]** matrix, you can't see the complete dependency graph, detect circular

**[31:28]** dependency graph, detect circular

**[31:28]** dependency graph, detect circular dependencies that span multiple

**[31:29]** dependencies that span multiple

**[31:29]** dependencies that span multiple features, identify the natural

**[31:32]** features, identify the natural

**[31:32]** features, identify the natural implementation phases where groups of

**[31:34]** implementation phases where groups of

**[31:34]** implementation phases where groups of features can be built together, or

**[31:36]** features can be built together, or

**[31:36]** features can be built together, or determine which features must be

**[31:37]** determine which features must be

**[31:38]** determine which features must be implemented first versus which can wait.

**[31:42]** implemented first versus which can wait.

**[31:42]** implemented first versus which can wait. So the input to this step is the feature

**[31:45]** So the input to this step is the feature

**[31:45]** So the input to this step is the feature specifications or sorry are the feature

**[31:48]** specifications or sorry are the feature

**[31:48]** specifications or sorry are the feature specifications with dependency

**[31:49]** specifications with dependency

**[31:49]** specifications with dependency declarations that have come out of the

**[31:51]** declarations that have come out of the

**[31:51]** declarations that have come out of the prior step.

**[31:53]** prior step.

**[31:53]** prior step. So what we're going to do here is

**[31:55]** So what we're going to do here is

**[31:55]** So what we're going to do here is synthesize scattered dependency

**[31:56]** synthesize scattered dependency

**[31:56]** synthesize scattered dependency declarations into one unified matrix and

**[31:59]** declarations into one unified matrix and

**[31:59]** declarations into one unified matrix and then we're going to validate it. So we


### [32:00 - 33:00]

**[32:01]** then we're going to validate it. So we

**[32:02]** then we're going to validate it. So we start by extracting the matrix. Here we

**[32:04]** start by extracting the matrix. Here we

**[32:04]** start by extracting the matrix. Here we gather all dependencies from individual

**[32:06]** gather all dependencies from individual

**[32:06]** gather all dependencies from individual feature specifications into a visual

**[32:08]** feature specifications into a visual

**[32:08]** feature specifications into a visual grid. So each row is a feature and each

**[32:11]** grid. So each row is a feature and each

**[32:12]** grid. So each row is a feature and each column is also a feature. And then we go

**[32:15]** column is also a feature. And then we go

**[32:15]** column is also a feature. And then we go row by row and mark an X where a row

**[32:18]** row by row and mark an X where a row

**[32:18]** row by row and mark an X where a row feature depends on a column feature.

**[32:22]** feature depends on a column feature.

**[32:22]** feature depends on a column feature. Next we generate a graph. So we create a

**[32:25]** Next we generate a graph. So we create a

**[32:25]** Next we generate a graph. So we create a visual diagram using graph viz or

**[32:27]** visual diagram using graph viz or

**[32:27]** visual diagram using graph viz or mermaid or you pick it from the matrix

**[32:30]** mermaid or you pick it from the matrix

**[32:30]** mermaid or you pick it from the matrix showing features as nodes and

**[32:33]** showing features as nodes and

**[32:33]** showing features as nodes and dependencies as edges.

**[32:36]** dependencies as edges.

**[32:36]** dependencies as edges. The graph makes circular dependencies

**[32:38]** The graph makes circular dependencies

**[32:38]** The graph makes circular dependencies immediately visible as closed loops and

**[32:40]** immediately visible as closed loops and

**[32:40]** immediately visible as closed loops and reveals the natural layered structure of

**[32:43]** reveals the natural layered structure of

**[32:43]** reveals the natural layered structure of the dependencies of the application.

**[32:47]** the dependencies of the application.

**[32:47]** the dependencies of the application. Next, we validate and clean. So, we

**[32:49]** Next, we validate and clean. So, we

**[32:49]** Next, we validate and clean. So, we apply the binary dependency test to

**[32:51]** apply the binary dependency test to

**[32:51]** apply the binary dependency test to every mark dependency and that goes

**[32:54]** every mark dependency and that goes

**[32:54]** every mark dependency and that goes something like does the row feature

**[32:57]** something like does the row feature

**[32:57]** something like does the row feature require the column features specific

**[32:59]** require the column features specific

**[32:59]** require the column features specific output configuration or functionality to


### [33:00 - 34:00]

**[33:02]** output configuration or functionality to

**[33:02]** output configuration or functionality to work? If yes, then yes, it's a

**[33:05]** work? If yes, then yes, it's a

**[33:05]** work? If yes, then yes, it's a dependency. If no,

**[33:08]** dependency. If no,

**[33:08]** dependency. If no, then remove it. And we track changes in

**[33:11]** then remove it. And we track changes in

**[33:11]** then remove it. And we track changes in the matrix. And so like it may be a

**[33:13]** the matrix. And so like it may be a

**[33:13]** the matrix. And so like it may be a technical dependency.

**[33:15]** technical dependency.

**[33:16]** technical dependency. This this step helps us clarify things

**[33:17]** This this step helps us clarify things

**[33:17]** This this step helps us clarify things like maybe coordination only or tool

**[33:19]** like maybe coordination only or tool

**[33:19]** like maybe coordination only or tool sharing, right? Like not true hard

**[33:22]** sharing, right? Like not true hard

**[33:22]** sharing, right? Like not true hard formal dependencies. And then we go to

**[33:24]** formal dependencies. And then we go to

**[33:24]** formal dependencies. And then we go to the next step. We we regenerate the

**[33:26]** the next step. We we regenerate the

**[33:26]** the next step. We we regenerate the graph, right? We're going to kind of

**[33:27]** graph, right? We're going to kind of

**[33:27]** graph, right? We're going to kind of iterate this way. And last, we detect

**[33:31]** iterate this way. And last, we detect

**[33:31]** iterate this way. And last, we detect cycles. So we're going to visually

**[33:33]** cycles. So we're going to visually

**[33:33]** cycles. So we're going to visually inspect the graph and the agent can help

**[33:34]** inspect the graph and the agent can help

**[33:34]** inspect the graph and the agent can help us here with this too. Uh for circular

**[33:37]** us here with this too. Uh for circular

**[33:37]** us here with this too. Uh for circular dependencies

**[33:39]** dependencies

**[33:39]** dependencies and if we find them we apply resolution

**[33:42]** and if we find them we apply resolution

**[33:42]** and if we find them we apply resolution strategies across one of four but really

**[33:46]** strategies across one of four but really

**[33:46]** strategies across one of four but really three steps. First we try dependency

**[33:49]** three steps. First we try dependency

**[33:49]** three steps. First we try dependency elimination meaning let's go back and

**[33:51]** elimination meaning let's go back and

**[33:51]** elimination meaning let's go back and reexamine it with the binary test. If

**[33:53]** reexamine it with the binary test. If

**[33:53]** reexamine it with the binary test. If that doesn't work then we try revised

**[33:55]** that doesn't work then we try revised

**[33:55]** that doesn't work then we try revised specification. So let's revise the

**[33:57]** specification. So let's revise the

**[33:58]** specification. So let's revise the interfaces. We can rethink contracts. So


### [34:00 - 35:00]

**[34:00]** interfaces. We can rethink contracts. So

**[34:00]** interfaces. We can rethink contracts. So features don't need each other's output.

**[34:03]** features don't need each other's output.

**[34:03]** features don't need each other's output. Thirdly, we try feature splitting. And

**[34:05]** Thirdly, we try feature splitting. And

**[34:05]** Thirdly, we try feature splitting. And so that's try and fe split it down

**[34:07]** so that's try and fe split it down

**[34:07]** so that's try and fe split it down again. May this feature may not be

**[34:09]** again. May this feature may not be

**[34:09]** again. May this feature may not be atomic. And then it's a last resort. And

**[34:11]** atomic. And then it's a last resort. And

**[34:11]** atomic. And then it's a last resort. And this is where it gets messy. The

**[34:12]** this is where it gets messy. The

**[34:12]** this is where it gets messy. The consolidation is like the last resort

**[34:14]** consolidation is like the last resort

**[34:14]** consolidation is like the last resort strategy here. But we're not going to

**[34:15]** strategy here. But we're not going to

**[34:15]** strategy here. But we're not going to touch too much on that today. And then

**[34:18]** touch too much on that today. And then

**[34:18]** touch too much on that today. And then we iterate after each cycle. We update

**[34:20]** we iterate after each cycle. We update

**[34:20]** we iterate after each cycle. We update the matrix. We regenerate the graph. And

**[34:22]** the matrix. We regenerate the graph. And

**[34:22]** the matrix. We regenerate the graph. And we recheck for cyclical dependencies

**[34:25]** we recheck for cyclical dependencies

**[34:25]** we recheck for cyclical dependencies until zero remain.

**[34:28]** until zero remain.

**[34:28]** until zero remain. The outputs for this step are twofold.

**[34:31]** The outputs for this step are twofold.

**[34:31]** The outputs for this step are twofold. We [clears throat] have a validated

**[34:31]** We [clears throat] have a validated

**[34:32]** We [clears throat] have a validated dependency matrix which is again our

**[34:33]** dependency matrix which is again our

**[34:33]** dependency matrix which is again our visual grid that shows complete

**[34:36]** visual grid that shows complete

**[34:36]** visual grid that shows complete dependency graph with all circular

**[34:38]** dependency graph with all circular

**[34:38]** dependency graph with all circular dependencies resolved, all dependencies

**[34:40]** dependencies resolved, all dependencies

**[34:40]** dependencies resolved, all dependencies validated as technically necessary and

**[34:43]** validated as technically necessary and

**[34:43]** validated as technically necessary and clear implementation layers defined.

**[34:46]** clear implementation layers defined.

**[34:46]** clear implementation layers defined. And then we have the dependency graph

**[34:48]** And then we have the dependency graph

**[34:48]** And then we have the dependency graph which is a visual diagram showing

**[34:49]** which is a visual diagram showing

**[34:50]** which is a visual diagram showing features as nodes and dependencies as

**[34:52]** features as nodes and dependencies as

**[34:52]** features as nodes and dependencies as edges making structure and layers

**[34:55]** edges making structure and layers

**[34:55]** edges making structure and layers immediately visible.

**[34:58]** immediately visible.

**[34:58]** immediately visible. The fifth and final step of the planning


### [35:00 - 36:00]

**[35:01]** The fifth and final step of the planning

**[35:01]** The fifth and final step of the planning phase is implementation plan

**[35:03]** phase is implementation plan

**[35:03]** phase is implementation plan development. The purpose is to transform

**[35:05]** development. The purpose is to transform

**[35:06]** development. The purpose is to transform your validated dependency matrix into a

**[35:08]** your validated dependency matrix into a

**[35:08]** your validated dependency matrix into a comprehensive phase organized

**[35:10]** comprehensive phase organized

**[35:10]** comprehensive phase organized implementation road map that sequences

**[35:12]** implementation road map that sequences

**[35:12]** implementation road map that sequences features into dependency layers,

**[35:15]** features into dependency layers,

**[35:15]** features into dependency layers, identifies parallel development

**[35:16]** identifies parallel development

**[35:16]** identifies parallel development opportunities, defines phase completion

**[35:19]** opportunities, defines phase completion

**[35:19]** opportunities, defines phase completion criteria, and establishes the validation

**[35:22]** criteria, and establishes the validation

**[35:22]** criteria, and establishes the validation strategies that enable the

**[35:23]** strategies that enable the

**[35:23]** strategies that enable the implementation loop.

**[35:26]** implementation loop.

**[35:26]** implementation loop. The problems that this step solves are

**[35:29]** The problems that this step solves are

**[35:29]** The problems that this step solves are that without a comprehensive

**[35:31]** that without a comprehensive

**[35:31]** that without a comprehensive implementation plan, you face

**[35:33]** implementation plan, you face

**[35:33]** implementation plan, you face implementation chaos. Despite having

**[35:35]** implementation chaos. Despite having

**[35:35]** implementation chaos. Despite having complete specifications

**[35:37]** complete specifications

**[35:37]** complete specifications and a validated dependency matrix, you

**[35:39]** and a validated dependency matrix, you

**[35:39]** and a validated dependency matrix, you can't answer which features should be

**[35:41]** can't answer which features should be

**[35:41]** can't answer which features should be implemented first and in what order.

**[35:43]** implemented first and in what order.

**[35:43]** implemented first and in what order. Which can be developed in parallel. Now,

**[35:45]** Which can be developed in parallel. Now,

**[35:45]** Which can be developed in parallel. Now, we won't talk about that at all today,

**[35:47]** we won't talk about that at all today,

**[35:47]** we won't talk about that at all today, but it is a feasible accelerator.

**[35:49]** but it is a feasible accelerator.

**[35:49]** but it is a feasible accelerator. How do you validate that a group of

**[35:50]** How do you validate that a group of

**[35:50]** How do you validate that a group of features works together before moving

**[35:52]** features works together before moving

**[35:52]** features works together before moving forward? and when is it safe to begin

**[35:55]** forward? and when is it safe to begin

**[35:55]** forward? and when is it safe to begin implementing features that depend on

**[35:56]** implementing features that depend on

**[35:56]** implementing features that depend on earlier work. The input to this step is

**[35:59]** earlier work. The input to this step is

**[35:59]** earlier work. The input to this step is the validated dependency matrix and


### [36:00 - 37:00]

**[36:01]** the validated dependency matrix and

**[36:01]** the validated dependency matrix and dependency graph from step four. And so

**[36:04]** dependency graph from step four. And so

**[36:04]** dependency graph from step four. And so what we're going to do here is transform

**[36:06]** what we're going to do here is transform

**[36:06]** what we're going to do here is transform the dependency matrix into an executable

**[36:09]** the dependency matrix into an executable

**[36:09]** the dependency matrix into an executable implementation strategy.

**[36:11]** implementation strategy.

**[36:11]** implementation strategy. And that begins with us organizing the

**[36:14]** And that begins with us organizing the

**[36:14]** And that begins with us organizing the phases of implementation via a top

**[36:16]** phases of implementation via a top

**[36:16]** phases of implementation via a top topological sort. So we organize

**[36:20]** topological sort. So we organize

**[36:20]** topological sort. So we organize features into implementation phases

**[36:21]** features into implementation phases

**[36:21]** features into implementation phases based on their depth in the dependency

**[36:24]** based on their depth in the dependency

**[36:24]** based on their depth in the dependency map. Features with no dependencies

**[36:27]** map. Features with no dependencies

**[36:27]** map. Features with no dependencies become phase one. Features depending

**[36:30]** become phase one. Features depending

**[36:30]** become phase one. Features depending only on phase one become phase 2. And we

**[36:33]** only on phase one become phase 2. And we

**[36:33]** only on phase one become phase 2. And we continue this pattern creating phases

**[36:35]** continue this pattern creating phases

**[36:35]** continue this pattern creating phases where each phase depends only on

**[36:37]** where each phase depends only on

**[36:37]** where each phase depends only on previous phases. We then verify that no

**[36:40]** previous phases. We then verify that no

**[36:40]** previous phases. We then verify that no features within the same phase depend on

**[36:42]** features within the same phase depend on

**[36:42]** features within the same phase depend on each other. And lastly we identify the

**[36:44]** each other. And lastly we identify the

**[36:44]** each other. And lastly we identify the critical path which is the longest

**[36:46]** critical path which is the longest

**[36:46]** critical path which is the longest dependency chain.

**[36:48]** dependency chain.

**[36:48]** dependency chain. Next it comes parallel analysis, but

**[36:51]** Next it comes parallel analysis, but

**[36:51]** Next it comes parallel analysis, but we're going to skip that for today.

**[36:53]** we're going to skip that for today.

**[36:53]** we're going to skip that for today. Next is validation strategy planning. So

**[36:56]** Next is validation strategy planning. So

**[36:56]** Next is validation strategy planning. So for each phase, we define binary success

**[36:58]** for each phase, we define binary success

**[36:58]** for each phase, we define binary success criteria. What tests must pass, what


### [37:00 - 38:00]

**[37:01]** criteria. What tests must pass, what

**[37:01]** criteria. What tests must pass, what integration points must work, how you'll

**[37:03]** integration points must work, how you'll

**[37:03]** integration points must work, how you'll verify that features work together, and

**[37:05]** verify that features work together, and

**[37:05]** verify that features work together, and then we establish feedback loops that

**[37:07]** then we establish feedback loops that

**[37:07]** then we establish feedback loops that enable autonomous agent refinement and

**[37:09]** enable autonomous agent refinement and

**[37:09]** enable autonomous agent refinement and binary progress tracking. Right? Is a

**[37:11]** binary progress tracking. Right? Is a

**[37:11]** binary progress tracking. Right? Is a feature implemented or is it not? There

**[37:13]** feature implemented or is it not? There

**[37:13]** feature implemented or is it not? There is no 20% implementation tracking.

**[37:17]** is no 20% implementation tracking.

**[37:17]** is no 20% implementation tracking. Think through what could go wrong when

**[37:18]** Think through what could go wrong when

**[37:18]** Think through what could go wrong when features combine and what validation

**[37:20]** features combine and what validation

**[37:20]** features combine and what validation provides confidence for dependent

**[37:22]** provides confidence for dependent

**[37:22]** provides confidence for dependent features in later phases. And then last

**[37:25]** features in later phases. And then last

**[37:25]** features in later phases. And then last we move on to implementation sequencing.

**[37:27]** we move on to implementation sequencing.

**[37:27]** we move on to implementation sequencing. This is where we define the complete

**[37:29]** This is where we define the complete

**[37:29]** This is where we define the complete execution strategy. So we have phase

**[37:31]** execution strategy. So we have phase

**[37:31]** execution strategy. So we have phase gates meaning how is it we determine

**[37:33]** gates meaning how is it we determine

**[37:33]** gates meaning how is it we determine we're ready and completely implemented a

**[37:35]** we're ready and completely implemented a

**[37:35]** we're ready and completely implemented a given phase and ready to move on to the

**[37:37]** given phase and ready to move on to the

**[37:37]** given phase and ready to move on to the next one. We have task assignment

**[37:39]** next one. We have task assignment

**[37:39]** next one. We have task assignment guidance for the agents. how we need to

**[37:42]** guidance for the agents. how we need to

**[37:42]** guidance for the agents. how we need to tell them how it is they're going to

**[37:43]** tell them how it is they're going to

**[37:43]** tell them how it is they're going to select the next feature to work on. In

**[37:45]** select the next feature to work on. In

**[37:45]** select the next feature to work on. In the event that they get blocked, we have

**[37:47]** the event that they get blocked, we have

**[37:47]** the event that they get blocked, we have blocker management process where we

**[37:48]** blocker management process where we

**[37:48]** blocker management process where we explain how it is that they handle and

**[37:50]** explain how it is that they handle and

**[37:50]** explain how it is that they handle and resolve these blockers. And last, we

**[37:52]** resolve these blockers. And last, we

**[37:52]** resolve these blockers. And last, we have progress tracking mechanisms that

**[37:53]** have progress tracking mechanisms that

**[37:54]** have progress tracking mechanisms that we define. These are at the feature

**[37:55]** we define. These are at the feature

**[37:55]** we define. These are at the feature level, at the phase level and also

**[37:57]** level, at the phase level and also

**[37:57]** level, at the phase level and also monitoring the critical path. The output


### [38:00 - 39:00]

**[38:00]** monitoring the critical path. The output

**[38:00]** monitoring the critical path. The output of this phase or sorry this step is the

**[38:02]** of this phase or sorry this step is the

**[38:02]** of this phase or sorry this step is the implementation plan and that's a

**[38:05]** implementation plan and that's a

**[38:05]** implementation plan and that's a comprehensive phased organized execution

**[38:07]** comprehensive phased organized execution

**[38:07]** comprehensive phased organized execution strategy that sequences all features

**[38:10]** strategy that sequences all features

**[38:10]** strategy that sequences all features into dependency layers identifies

**[38:12]** into dependency layers identifies

**[38:12]** into dependency layers identifies parallel development opportunities

**[38:14]** parallel development opportunities

**[38:14]** parallel development opportunities develops binary validation gates for

**[38:16]** develops binary validation gates for

**[38:16]** develops binary validation gates for each phase and provides the guidance

**[38:18]** each phase and provides the guidance

**[38:18]** each phase and provides the guidance needed for autonomous agent

**[38:20]** needed for autonomous agent

**[38:20]** needed for autonomous agent implementation sessions.

**[38:27]** All right. And with that, we're now

**[38:27]** All right. And with that, we're now ready to talk about the implementation

**[38:28]** ready to talk about the implementation

**[38:28]** ready to talk about the implementation loop.

**[38:30]** loop.

**[38:30]** loop. Implementation is where your planning

**[38:32]** Implementation is where your planning

**[38:32]** Implementation is where your planning artifacts guide the transformation of

**[38:34]** artifacts guide the transformation of

**[38:34]** artifacts guide the transformation of specifications into working tested

**[38:36]** specifications into working tested

**[38:36]** specifications into working tested software. Unlike planning, which is

**[38:39]** software. Unlike planning, which is

**[38:39]** software. Unlike planning, which is linear and proceeds through five

**[38:41]** linear and proceeds through five

**[38:41]** linear and proceeds through five distinct steps, implementation is a

**[38:44]** distinct steps, implementation is a

**[38:44]** distinct steps, implementation is a tight rapid loop executed repeatedly for

**[38:48]** tight rapid loop executed repeatedly for

**[38:48]** tight rapid loop executed repeatedly for each atomic feature.

**[38:50]** each atomic feature.

**[38:50]** each atomic feature. Before we get too far into that though,

**[38:52]** Before we get too far into that though,

**[38:52]** Before we get too far into that though, we need to understand and unpack the

**[38:54]** we need to understand and unpack the

**[38:54]** we need to understand and unpack the multiensory feedback loop. This is a

**[38:56]** multiensory feedback loop. This is a

**[38:56]** multiensory feedback loop. This is a really key idea in the framework.


### [39:00 - 40:00]

**[39:00]** really key idea in the framework.

**[39:00]** really key idea in the framework. The agent implements code and then it

**[39:02]** The agent implements code and then it

**[39:02]** The agent implements code and then it executes it while gathering feedback

**[39:03]** executes it while gathering feedback

**[39:03]** executes it while gathering feedback through these digital senses.

**[39:06]** through these digital senses.

**[39:06]** through these digital senses. The visual sense and you can think about

**[39:08]** The visual sense and you can think about

**[39:08]** The visual sense and you can think about that as what renders

**[39:10]** that as what renders

**[39:10]** that as what renders the auditory sense what the system

**[39:13]** the auditory sense what the system

**[39:13]** the auditory sense what the system reports and the tactile sense how

**[39:17]** reports and the tactile sense how

**[39:17]** reports and the tactile sense how interactions respond.

**[39:19]** interactions respond.

**[39:19]** interactions respond. This sensory feedback provides rich

**[39:21]** This sensory feedback provides rich

**[39:21]** This sensory feedback provides rich diagnostic information about what's

**[39:23]** diagnostic information about what's

**[39:23]** diagnostic information about what's actually happening in the application.

**[39:25]** actually happening in the application.

**[39:25]** actually happening in the application. The agent runs formal tests to validate

**[39:27]** The agent runs formal tests to validate

**[39:27]** The agent runs formal tests to validate against acceptance criteria. But by

**[39:30]** against acceptance criteria. But by

**[39:30]** against acceptance criteria. But by correlating sensory feedback with test

**[39:32]** correlating sensory feedback with test

**[39:32]** correlating sensory feedback with test results, the agent both understands what

**[39:35]** results, the agent both understands what

**[39:35]** results, the agent both understands what failed from the tests and why it failed

**[39:38]** failed from the tests and why it failed

**[39:38]** failed from the tests and why it failed from the sensors. This loop continues

**[39:41]** from the sensors. This loop continues

**[39:41]** from the sensors. This loop continues until all acceptance criteria pass and

**[39:44]** until all acceptance criteria pass and

**[39:44]** until all acceptance criteria pass and all sensors report clean execution.

**[39:48]** all sensors report clean execution.

**[39:48]** all sensors report clean execution. So step one in the implementation loop

**[39:50]** So step one in the implementation loop

**[39:50]** So step one in the implementation loop is context assembly.

**[39:53]** is context assembly.

**[39:53]** is context assembly. And the purpose here is to transform

**[39:55]** And the purpose here is to transform

**[39:55]** And the purpose here is to transform planning artifacts into a curated

**[39:57]** planning artifacts into a curated

**[39:57]** planning artifacts into a curated context package that enables autonomous

**[39:59]** context package that enables autonomous

**[39:59]** context package that enables autonomous feature implementation with a single


### [40:00 - 41:00]

**[40:01]** feature implementation with a single

**[40:01]** feature implementation with a single coding session for the agent. The

**[40:05]** coding session for the agent. The

**[40:05]** coding session for the agent. The problem that this solves is that you

**[40:07]** problem that this solves is that you

**[40:07]** problem that this solves is that you have atomic features fully specified and

**[40:09]** have atomic features fully specified and

**[40:09]** have atomic features fully specified and sequenced, but you can't just throw

**[40:11]** sequenced, but you can't just throw

**[40:11]** sequenced, but you can't just throw everything at the agent and hope it

**[40:12]** everything at the agent and hope it

**[40:12]** everything at the agent and hope it figures out what to do. Without

**[40:14]** figures out what to do. Without

**[40:14]** figures out what to do. Without systematic context assembly, you're

**[40:16]** systematic context assembly, you're

**[40:16]** systematic context assembly, you're dumping entire planning documents into

**[40:19]** dumping entire planning documents into

**[40:19]** dumping entire planning documents into agent sessions, which wastes context

**[40:21]** agent sessions, which wastes context

**[40:21]** agent sessions, which wastes context window on irrelevant information. This

**[40:24]** window on irrelevant information. This

**[40:24]** window on irrelevant information. This results typically in the agent making

**[40:27]** results typically in the agent making

**[40:27]** results typically in the agent making decisions without critical context and

**[40:29]** decisions without critical context and

**[40:29]** decisions without critical context and without you or less less frequently

**[40:31]** without you or less less frequently

**[40:32]** without you or less less frequently stopping and asking for guidance. And

**[40:34]** stopping and asking for guidance. And

**[40:34]** stopping and asking for guidance. And ultimately though, this turns what

**[40:36]** ultimately though, this turns what

**[40:36]** ultimately though, this turns what should be relatively autonomous

**[40:38]** should be relatively autonomous

**[40:38]** should be relatively autonomous implementation sessions into a constant

**[40:40]** implementation sessions into a constant

**[40:40]** implementation sessions into a constant back and forth. It wastes context window

**[40:43]** back and forth. It wastes context window

**[40:44]** back and forth. It wastes context window and it results in validation gaps. So

**[40:46]** and it results in validation gaps. So

**[40:46]** and it results in validation gaps. So the input to context assembly is the

**[40:50]** the input to context assembly is the

**[40:50]** the input to context assembly is the implementation plan again only sections

**[40:53]** implementation plan again only sections

**[40:53]** implementation plan again only sections that are relevant for the specific

**[40:55]** that are relevant for the specific

**[40:55]** that are relevant for the specific atomic feature that's going to be

**[40:56]** atomic feature that's going to be

**[40:56]** atomic feature that's going to be implemented. The feature specification


### [41:00 - 42:00]

**[41:01]** implemented. The feature specification

**[41:01]** implemented. The feature specification and all of the referenced dependencies

**[41:04]** and all of the referenced dependencies

**[41:04]** and all of the referenced dependencies that are specified in that that

**[41:07]** that are specified in that that

**[41:07]** that are specified in that that specification.

**[41:10]** specification.

**[41:10]** specification. And what we're going to do here is

**[41:11]** And what we're going to do here is

**[41:11]** And what we're going to do here is curate the exact information that's

**[41:13]** curate the exact information that's

**[41:13]** curate the exact information that's needed for this one atomic feature

**[41:16]** needed for this one atomic feature

**[41:16]** needed for this one atomic feature through four steps. We start with

**[41:18]** through four steps. We start with

**[41:18]** through four steps. We start with feature specification assembly. And this

**[41:20]** feature specification assembly. And this

**[41:20]** feature specification assembly. And this is where we include the complete feature

**[41:22]** is where we include the complete feature

**[41:22]** is where we include the complete feature specification. And you'll recall that

**[41:24]** specification. And you'll recall that

**[41:24]** specification. And you'll recall that that's the user story, the technical

**[41:26]** that's the user story, the technical

**[41:26]** that's the user story, the technical contracts, acceptance criteria, and we

**[41:29]** contracts, acceptance criteria, and we

**[41:29]** contracts, acceptance criteria, and we at reference using the that at symbol,

**[41:31]** at reference using the that at symbol,

**[41:31]** at reference using the that at symbol, right? All dependencies. This is the

**[41:34]** right? All dependencies. This is the

**[41:34]** right? All dependencies. This is the primary blueprint that the agent will

**[41:36]** primary blueprint that the agent will

**[41:36]** primary blueprint that the agent will follow. Our next step is dependency

**[41:40]** follow. Our next step is dependency

**[41:40]** follow. Our next step is dependency context gathering. So we follow all of

**[41:43]** context gathering. So we follow all of

**[41:43]** context gathering. So we follow all of the at references in our feature

**[41:44]** the at references in our feature

**[41:44]** the at references in our feature specification.

**[41:46]** specification.

**[41:46]** specification. And each at reference points to a depend

**[41:49]** And each at reference points to a depend

**[41:49]** And each at reference points to a depend a dependency feature specification and

**[41:52]** a dependency feature specification and

**[41:52]** a dependency feature specification and the actual implemented code. And that's

**[41:54]** the actual implemented code. And that's

**[41:54]** the actual implemented code. And that's critical to note because per the

**[41:57]** critical to note because per the

**[41:57]** critical to note because per the framework definition all dependencies

**[41:59]** framework definition all dependencies

**[41:59]** framework definition all dependencies must be implemented previously. So this


### [42:00 - 43:00]

**[42:01]** must be implemented previously. So this

**[42:01]** must be implemented previously. So this is both specification and code. We pull

**[42:03]** is both specification and code. We pull

**[42:04]** is both specification and code. We pull these in so that the agent understands

**[42:06]** these in so that the agent understands

**[42:06]** these in so that the agent understands exactly what it needs to integrate with.

**[42:09]** exactly what it needs to integrate with.

**[42:09]** exactly what it needs to integrate with. Next, we move on to implementation

**[42:11]** Next, we move on to implementation

**[42:11]** Next, we move on to implementation guidance. And this is where we extract

**[42:13]** guidance. And this is where we extract

**[42:13]** guidance. And this is where we extract relevant sections from the

**[42:14]** relevant sections from the

**[42:14]** relevant sections from the implementation plan. So, we don't just

**[42:16]** implementation plan. So, we don't just

**[42:16]** implementation plan. So, we don't just dump the whole implementation plan in.

**[42:18]** dump the whole implementation plan in.

**[42:18]** dump the whole implementation plan in. The agent needs to know things like what

**[42:20]** The agent needs to know things like what

**[42:20]** The agent needs to know things like what phase is this feature in? What are the

**[42:23]** phase is this feature in? What are the

**[42:23]** phase is this feature in? What are the phase completion criteria? What's the

**[42:25]** phase completion criteria? What's the

**[42:25]** phase completion criteria? What's the validation strategy for this phase? We

**[42:27]** validation strategy for this phase? We

**[42:27]** validation strategy for this phase? We just bring in the sections that

**[42:29]** just bring in the sections that

**[42:29]** just bring in the sections that contextualize this features

**[42:30]** contextualize this features

**[42:30]** contextualize this features implementation and its validation. And

**[42:33]** implementation and its validation. And

**[42:33]** implementation and its validation. And then last we enable sensory

**[42:36]** then last we enable sensory

**[42:36]** then last we enable sensory capabilities. So we read the features

**[42:38]** capabilities. So we read the features

**[42:38]** capabilities. So we read the features acceptance criteria to identify which

**[42:40]** acceptance criteria to identify which

**[42:40]** acceptance criteria to identify which digital sensors are required.

**[42:43]** digital sensors are required.

**[42:43]** digital sensors are required. Visual validation language like sees,

**[42:45]** Visual validation language like sees,

**[42:46]** Visual validation language like sees, displays, renders that requires the

**[42:48]** displays, renders that requires the

**[42:48]** displays, renders that requires the visual sense tools. Logging or error

**[42:51]** visual sense tools. Logging or error

**[42:51]** visual sense tools. Logging or error language requires auditory sense tools.

**[42:53]** language requires auditory sense tools.

**[42:53]** language requires auditory sense tools. Interaction language like clicks,

**[42:55]** Interaction language like clicks,

**[42:55]** Interaction language like clicks, submits, completes requires tactile

**[42:58]** submits, completes requires tactile

**[42:58]** submits, completes requires tactile sense tools. So we're going to at


### [43:00 - 44:00]

**[43:00]** sense tools. So we're going to at

**[43:00]** sense tools. So we're going to at reference the appropriate tool usage

**[43:02]** reference the appropriate tool usage

**[43:02]** reference the appropriate tool usage guides that we've written by the way and

**[43:04]** guides that we've written by the way and

**[43:04]** guides that we've written by the way and we'll talk about this in the tool

**[43:05]** we'll talk about this in the tool

**[43:05]** we'll talk about this in the tool section but once per tool so that it's

**[43:07]** section but once per tool so that it's

**[43:07]** section but once per tool so that it's reusable across all features so that the

**[43:09]** reusable across all features so that the

**[43:09]** reusable across all features so that the agent knows how to gather the required

**[43:11]** agent knows how to gather the required

**[43:11]** agent knows how to gather the required sensory feedback.

**[43:13]** sensory feedback.

**[43:13]** sensory feedback. The output from this step is the curated

**[43:16]** The output from this step is the curated

**[43:16]** The output from this step is the curated context package and this is a focused

**[43:19]** context package and this is a focused

**[43:19]** context package and this is a focused assembly of exactly what the agent

**[43:21]** assembly of exactly what the agent

**[43:21]** assembly of exactly what the agent needs. The feature specification,

**[43:24]** needs. The feature specification,

**[43:24]** needs. The feature specification, dependency code, the for any and all

**[43:27]** dependency code, the for any and all

**[43:27]** dependency code, the for any and all features that uh this feature integrates

**[43:29]** features that uh this feature integrates

**[43:29]** features that uh this feature integrates with

**[43:31]** with

**[43:31]** with relevant implementation guidance and

**[43:33]** relevant implementation guidance and

**[43:33]** relevant implementation guidance and sensory tool instructions for

**[43:35]** sensory tool instructions for

**[43:35]** sensory tool instructions for validation.

**[43:41]** And now we're finally here.

**[43:41]** And now we're finally here. And note that this is the only one step

**[43:44]** And note that this is the only one step

**[43:44]** And note that this is the only one step in this entire framework that is the AI

**[43:47]** in this entire framework that is the AI

**[43:47]** in this entire framework that is the AI writes code. But now we get to the

**[43:49]** writes code. But now we get to the

**[43:49]** writes code. But now we get to the implementation loop [sighs]

**[43:51]** implementation loop [sighs]

**[43:51]** implementation loop [sighs] which is the last step of

**[43:53]** which is the last step of

**[43:53]** which is the last step of implementation. And the purpose is to

**[43:55]** implementation. And the purpose is to

**[43:55]** implementation. And the purpose is to transform an atomic feature

**[43:57]** transform an atomic feature

**[43:57]** transform an atomic feature specification into working tested code.


### [44:00 - 45:00]

**[44:00]** specification into working tested code.

**[44:00]** specification into working tested code. This solves a specific set of problems.

**[44:02]** This solves a specific set of problems.

**[44:02]** This solves a specific set of problems. Without structured implementation,

**[44:05]** Without structured implementation,

**[44:05]** Without structured implementation, agents will either write all code before

**[44:07]** agents will either write all code before

**[44:07]** agents will either write all code before testing anything and that accumulates

**[44:09]** testing anything and that accumulates

**[44:09]** testing anything and that accumulates problems that compound or they write and

**[44:11]** problems that compound or they write and

**[44:11]** problems that compound or they write and test ad hoc without systematic feedback

**[44:14]** test ad hoc without systematic feedback

**[44:14]** test ad hoc without systematic feedback and that makes refinement a bit of a

**[44:16]** and that makes refinement a bit of a

**[44:16]** and that makes refinement a bit of a guessing game.

**[44:18]** guessing game.

**[44:18]** guessing game. The write everything then test approach

**[44:20]** The write everything then test approach

**[44:20]** The write everything then test approach fails because problems accumulate

**[44:22]** fails because problems accumulate

**[44:22]** fails because problems accumulate undetected and you're ultimately

**[44:24]** undetected and you're ultimately

**[44:24]** undetected and you're ultimately debugging multiple interconnected issues

**[44:26]** debugging multiple interconnected issues

**[44:26]** debugging multiple interconnected issues at once. The ad hoc approach fails

**[44:28]** at once. The ad hoc approach fails

**[44:28]** at once. The ad hoc approach fails because without comprehensive sensory

**[44:30]** because without comprehensive sensory

**[44:30]** because without comprehensive sensory feedback, you miss problems that tests

**[44:33]** feedback, you miss problems that tests

**[44:33]** feedback, you miss problems that tests don't catch.

**[44:34]** don't catch.

**[44:34]** don't catch. Tests pass, for example, but the UI

**[44:36]** Tests pass, for example, but the UI

**[44:36]** Tests pass, for example, but the UI doesn't render correctly or the workflow

**[44:39]** doesn't render correctly or the workflow

**[44:39]** doesn't render correctly or the workflow completes but errors fill the logs. The

**[44:42]** completes but errors fill the logs. The

**[44:42]** completes but errors fill the logs. The feature quote works but user

**[44:44]** feature quote works but user

**[44:44]** feature quote works but user interactions are broken.

**[44:46]** interactions are broken.

**[44:46]** interactions are broken. So this step solves all these problems

**[44:49]** So this step solves all these problems

**[44:49]** So this step solves all these problems through a single multiensory

**[44:52]** through a single multiensory

**[44:52]** through a single multiensory implementation loop because features are

**[44:55]** implementation loop because features are

**[44:55]** implementation loop because features are atomic. The complete imple

**[44:57]** atomic. The complete imple

**[44:57]** atomic. The complete imple implementation fits in one context

**[44:59]** implementation fits in one context

**[44:59]** implementation fits in one context window. The agent maintains full


### [45:00 - 46:00]

**[45:01]** window. The agent maintains full

**[45:01]** window. The agent maintains full understanding from start to finish.

**[45:03]** understanding from start to finish.

**[45:03]** understanding from start to finish. There's no context loss, no

**[45:05]** There's no context loss, no

**[45:05]** There's no context loss, no reconstruction, and no degraded

**[45:06]** reconstruction, and no degraded

**[45:06]** reconstruction, and no degraded fidelity.

**[45:08]** fidelity.

**[45:08]** fidelity. The input to the implementation loop is

**[45:10]** The input to the implementation loop is

**[45:10]** The input to the implementation loop is the context package that was assembled

**[45:12]** the context package that was assembled

**[45:12]** the context package that was assembled previously. And so what we're going to

**[45:14]** previously. And so what we're going to

**[45:14]** previously. And so what we're going to do here is execute the tight multiensory

**[45:18]** do here is execute the tight multiensory

**[45:18]** do here is execute the tight multiensory feedback loop, which starts by writing

**[45:20]** feedback loop, which starts by writing

**[45:20]** feedback loop, which starts by writing code. The agent implements the code

**[45:23]** code. The agent implements the code

**[45:23]** code. The agent implements the code following the feature specifications

**[45:24]** following the feature specifications

**[45:24]** following the feature specifications technical contracts.

**[45:27]** technical contracts.

**[45:27]** technical contracts. It translates all three levels of

**[45:28]** It translates all three levels of

**[45:28]** It translates all three levels of contracts into working code ensuring

**[45:30]** contracts into working code ensuring

**[45:30]** contracts into working code ensuring interfaces, inputs, outputs, and error

**[45:33]** interfaces, inputs, outputs, and error

**[45:33]** interfaces, inputs, outputs, and error handling match the specification

**[45:35]** handling match the specification

**[45:35]** handling match the specification exactly. Then we move on to execute and

**[45:38]** exactly. Then we move on to execute and

**[45:38]** exactly. Then we move on to execute and sense. This is where we get

**[45:39]** sense. This is where we get

**[45:39]** sense. This is where we get comprehensive digital feedback. The

**[45:42]** comprehensive digital feedback. The

**[45:42]** comprehensive digital feedback. The agent immediately executes the code

**[45:44]** agent immediately executes the code

**[45:44]** agent immediately executes the code that's been written and gathers

**[45:46]** that's been written and gathers

**[45:46]** that's been written and gathers comprehensive sensory feedback through

**[45:47]** comprehensive sensory feedback through

**[45:48]** comprehensive sensory feedback through the three digital sensors based on

**[45:49]** the three digital sensors based on

**[45:49]** the three digital sensors based on acceptance criteria requirements. And

**[45:51]** acceptance criteria requirements. And

**[45:52]** acceptance criteria requirements. And we've talked about the visual, auditory,

**[45:54]** we've talked about the visual, auditory,

**[45:54]** we've talked about the visual, auditory, and tactile senses that are at play

**[45:56]** and tactile senses that are at play

**[45:56]** and tactile senses that are at play there. The agent captures rich

**[45:59]** there. The agent captures rich

**[45:59]** there. The agent captures rich diagnostic information about what's


### [46:00 - 47:00]

**[46:01]** diagnostic information about what's

**[46:01]** diagnostic information about what's actually happening during execution and

**[46:03]** actually happening during execution and

**[46:03]** actually happening during execution and then moves on to test and validate. And

**[46:06]** then moves on to test and validate. And

**[46:06]** then moves on to test and validate. And this is where the agent runs all test

**[46:08]** this is where the agent runs all test

**[46:08]** this is where the agent runs all test scenarios from the validation contract

**[46:09]** scenarios from the validation contract

**[46:09]** scenarios from the validation contract section of the specification and tests

**[46:12]** section of the specification and tests

**[46:12]** section of the specification and tests provide binary pass fail spec uh signals

**[46:15]** provide binary pass fail spec uh signals

**[46:15]** provide binary pass fail spec uh signals against the specification's

**[46:16]** against the specification's

**[46:16]** against the specification's requirements.

**[46:18]** requirements.

**[46:18]** requirements. So now we take the output of the last

**[46:21]** So now we take the output of the last

**[46:21]** So now we take the output of the last two steps of the loop and we correlate

**[46:24]** two steps of the loop and we correlate

**[46:24]** two steps of the loop and we correlate them all. So the agent correlates

**[46:26]** them all. So the agent correlates

**[46:26]** them all. So the agent correlates signals across all active sensors and

**[46:29]** signals across all active sensors and

**[46:29]** signals across all active sensors and all of the test results. Multiple

**[46:31]** all of the test results. Multiple

**[46:31]** all of the test results. Multiple sensors reporting the same issue

**[46:32]** sensors reporting the same issue

**[46:32]** sensors reporting the same issue confirms a diagnosis.

**[46:34]** confirms a diagnosis.

**[46:34]** confirms a diagnosis. Conflicting signals behind sensors may

**[46:36]** Conflicting signals behind sensors may

**[46:36]** Conflicting signals behind sensors may reveal hidden complexity. But this

**[46:38]** reveal hidden complexity. But this

**[46:38]** reveal hidden complexity. But this integrated analysis reveals both what

**[46:41]** integrated analysis reveals both what

**[46:41]** integrated analysis reveals both what failed from the tests and why it failed

**[46:44]** failed from the tests and why it failed

**[46:44]** failed from the tests and why it failed from sensory feedback which enables

**[46:46]** from sensory feedback which enables

**[46:46]** from sensory feedback which enables targeted refinement by the agent.

**[46:50]** targeted refinement by the agent.

**[46:50]** targeted refinement by the agent. And we loop and loop and loop until the

**[46:54]** And we loop and loop and loop until the

**[46:54]** And we loop and loop and loop until the feature is complete. And the feature is

**[46:55]** feature is complete. And the feature is

**[46:55]** feature is complete. And the feature is complete if all tests pass and all

**[46:58]** complete if all tests pass and all

**[46:58]** complete if all tests pass and all sensors report clean execution. So


### [47:00 - 48:00]

**[47:01]** sensors report clean execution. So

**[47:01]** sensors report clean execution. So there's no errors in blogs, there are no

**[47:03]** there's no errors in blogs, there are no

**[47:03]** there's no errors in blogs, there are no UI rendering issues, interactions work

**[47:06]** UI rendering issues, interactions work

**[47:06]** UI rendering issues, interactions work properly. At that point, the feature is

**[47:08]** properly. At that point, the feature is

**[47:08]** properly. At that point, the feature is complete. Otherwise, the agent refineses

**[47:10]** complete. Otherwise, the agent refineses

**[47:10]** complete. Otherwise, the agent refineses based on the diagnostic information

**[47:12]** based on the diagnostic information

**[47:12]** based on the diagnostic information that's been gathered and loops through

**[47:14]** that's been gathered and loops through

**[47:14]** that's been gathered and loops through the loop again.

**[47:20]** When we determine that these convergence

**[47:20]** When we determine that these convergence criteria are met, then the feature is

**[47:23]** criteria are met, then the feature is

**[47:23]** criteria are met, then the feature is complete and the agent creates an atomic

**[47:26]** complete and the agent creates an atomic

**[47:26]** complete and the agent creates an atomic git commit containing only this features

**[47:28]** git commit containing only this features

**[47:28]** git commit containing only this features changes with a structured commit message

**[47:30]** changes with a structured commit message

**[47:30]** changes with a structured commit message including feature ID, specification

**[47:32]** including feature ID, specification

**[47:32]** including feature ID, specification summary, validation confirmation, and

**[47:35]** summary, validation confirmation, and

**[47:35]** summary, validation confirmation, and implementation nodes. And at that point,

**[47:37]** implementation nodes. And at that point,

**[47:37]** implementation nodes. And at that point, the feature is fully complete and the

**[47:40]** the feature is fully complete and the

**[47:40]** the feature is fully complete and the codebase is ready for the next feature.

**[47:43]** codebase is ready for the next feature.

**[47:43]** codebase is ready for the next feature. So the output here is we've finally got

**[47:45]** So the output here is we've finally got

**[47:45]** So the output here is we've finally got there. We've got a fully working tested

**[47:49]** there. We've got a fully working tested

**[47:49]** there. We've got a fully working tested feature that's passed all acceptance

**[47:51]** feature that's passed all acceptance

**[47:51]** feature that's passed all acceptance criteria, all tests and has been

**[47:54]** criteria, all tests and has been

**[47:54]** criteria, all tests and has been validated by all three digital sensors

**[47:56]** validated by all three digital sensors

**[47:56]** validated by all three digital sensors and the feature is ready for integration

**[47:59]** and the feature is ready for integration

**[47:59]** and the feature is ready for integration into the broader codebase.


### [48:00 - 49:00]

**[48:01]** into the broader codebase.

**[48:02]** into the broader codebase. So, let's check back in with our Vibe

**[48:04]** So, let's check back in with our Vibe

**[48:04]** So, let's check back in with our Vibe coding dev and see how he's fairing now

**[48:06]** coding dev and see how he's fairing now

**[48:06]** coding dev and see how he's fairing now that he's been exposed to both the

**[48:10]** that he's been exposed to both the

**[48:10]** that he's been exposed to both the principles and the process of the

**[48:12]** principles and the process of the

**[48:12]** principles and the process of the framework.

**[48:15]** framework.

**[48:15]** framework. Well, it seems that we've even roused

**[48:17]** Well, it seems that we've even roused

**[48:17]** Well, it seems that we've even roused the tiger's attention and astonishment

**[48:19]** the tiger's attention and astonishment

**[48:19]** the tiger's attention and astonishment here. Minds have been blown. Minds have

**[48:22]** here. Minds have been blown. Minds have

**[48:22]** here. Minds have been blown. Minds have been expanded. Well, we're rounding the

**[48:25]** been expanded. Well, we're rounding the

**[48:25]** been expanded. Well, we're rounding the corner now. Let's move into tools.

**[48:34]** The framework requires four foundational

**[48:34]** The framework requires four foundational capabilities that enable work done via

**[48:37]** capabilities that enable work done via

**[48:37]** capabilities that enable work done via the process.


### [49:00 - 50:00]

**[49:26]** So let's talk about the coding

**[49:26]** So let's talk about the coding environment.

**[49:28]** environment.

**[49:28]** environment. The coding environment is a complete

**[49:29]** The coding environment is a complete

**[49:29]** The coding environment is a complete development workspace that supports two

**[49:31]** development workspace that supports two

**[49:31]** development workspace that supports two fundamentally different types of work

**[49:33]** fundamentally different types of work

**[49:33]** fundamentally different types of work that are happening simultaneously.

**[49:35]** that are happening simultaneously.

**[49:35]** that are happening simultaneously. your architectural thinking and planning

**[49:38]** your architectural thinking and planning

**[49:38]** your architectural thinking and planning and the agents autonomous cap uh

**[49:40]** and the agents autonomous cap uh

**[49:40]** and the agents autonomous cap uh implementation and testing. And so there

**[49:42]** implementation and testing. And so there

**[49:42]** implementation and testing. And so there are four core components of the coding

**[49:45]** are four core components of the coding

**[49:45]** are four core components of the coding environment. The first is an AI coding

**[49:47]** environment. The first is an AI coding

**[49:47]** environment. The first is an AI coding agent obviously. Next is an execution

**[49:50]** agent obviously. Next is an execution

**[49:50]** agent obviously. Next is an execution sandbox and this is a safe isolated

**[49:54]** sandbox and this is a safe isolated

**[49:54]** sandbox and this is a safe isolated environment where all agent written code

**[49:56]** environment where all agent written code

**[49:56]** environment where all agent written code executes and tests are run. Autonomous


### [50:00 - 51:00]

**[50:01]** executes and tests are run. Autonomous

**[50:01]** executes and tests are run. Autonomous implementation requires the freedom to

**[50:03]** implementation requires the freedom to

**[50:03]** implementation requires the freedom to experiment, iterate, and occasionally

**[50:06]** experiment, iterate, and occasionally

**[50:06]** experiment, iterate, and occasionally break things. And the sandbox provides

**[50:08]** break things. And the sandbox provides

**[50:08]** break things. And the sandbox provides complete development capabilities in a

**[50:10]** complete development capabilities in a

**[50:10]** complete development capabilities in a disposable, risk-free environment with

**[50:13]** disposable, risk-free environment with

**[50:13]** disposable, risk-free environment with easy reset and no consequences for

**[50:15]** easy reset and no consequences for

**[50:15]** easy reset and no consequences for failure.

**[50:17]** failure.

**[50:17]** failure. Next, we need an IDE or a text editor if

**[50:19]** Next, we need an IDE or a text editor if

**[50:20]** Next, we need an IDE or a text editor if you must. And I'm going to avoid the

**[50:21]** you must. And I'm going to avoid the

**[50:21]** you must. And I'm going to avoid the holy wars of IDE versus text editor

**[50:23]** holy wars of IDE versus text editor

**[50:23]** holy wars of IDE versus text editor here. You pick the one that suits you.

**[50:26]** here. You pick the one that suits you.

**[50:26]** here. You pick the one that suits you. And last is voice input. And this is the

**[50:29]** And last is voice input. And this is the

**[50:29]** And last is voice input. And this is the rapid capture system that converts

**[50:32]** rapid capture system that converts

**[50:32]** rapid capture system that converts speech to text at thinking speed.

**[50:36]** speech to text at thinking speed.

**[50:36]** speech to text at thinking speed. Planning work involves externalizing

**[50:37]** Planning work involves externalizing

**[50:37]** Planning work involves externalizing architectural thinking and that's often

**[50:40]** architectural thinking and that's often

**[50:40]** architectural thinking and that's often incomplete, exploratory, and iterative.

**[50:43]** incomplete, exploratory, and iterative.

**[50:43]** incomplete, exploratory, and iterative. Voice input removes the typing

**[50:45]** Voice input removes the typing

**[50:45]** Voice input removes the typing bottleneck, letting you think out loud

**[50:47]** bottleneck, letting you think out loud

**[50:47]** bottleneck, letting you think out loud and capture ideas much faster than

**[50:49]** and capture ideas much faster than

**[50:49]** and capture ideas much faster than typing. I really can't oversell just how

**[50:53]** typing. I really can't oversell just how

**[50:53]** typing. I really can't oversell just how massively impactful a good voice input

**[50:55]** massively impactful a good voice input

**[50:55]** massively impactful a good voice input tool is in applying the framework.

**[50:58]** tool is in applying the framework.

**[50:58]** tool is in applying the framework. Next we have the multiensory feedback


### [51:00 - 52:00]

**[51:00]** Next we have the multiensory feedback

**[51:00]** Next we have the multiensory feedback system. This is a comprehensive

**[51:03]** system. This is a comprehensive

**[51:03]** system. This is a comprehensive validation infrastructure that gives

**[51:04]** validation infrastructure that gives

**[51:04]** validation infrastructure that gives agents the ability to observe their

**[51:06]** agents the ability to observe their

**[51:06]** agents the ability to observe their implementations through three

**[51:08]** implementations through three

**[51:08]** implementations through three complimentary digital sensors. Those

**[51:10]** complimentary digital sensors. Those

**[51:10]** complimentary digital sensors. Those being visual, auditory and tactile and

**[51:13]** being visual, auditory and tactile and

**[51:13]** being visual, auditory and tactile and it enables autonomous refinement through

**[51:15]** it enables autonomous refinement through

**[51:15]** it enables autonomous refinement through an analogous breadth of observation that

**[51:18]** an analogous breadth of observation that

**[51:18]** an analogous breadth of observation that humans use during development. The core

**[51:21]** humans use during development. The core

**[51:21]** humans use during development. The core components here are visual sense tools

**[51:24]** components here are visual sense tools

**[51:24]** components here are visual sense tools which enable direct observation of what

**[51:27]** which enable direct observation of what

**[51:27]** which enable direct observation of what was produced and what exists. They

**[51:29]** was produced and what exists. They

**[51:29]** was produced and what exists. They capture UI rendering like screenshots or

**[51:32]** capture UI rendering like screenshots or

**[51:32]** capture UI rendering like screenshots or layout styling system state so database

**[51:35]** layout styling system state so database

**[51:35]** layout styling system state so database contents configuration session data and

**[51:38]** contents configuration session data and

**[51:38]** contents configuration session data and code structure which is the actual

**[51:40]** code structure which is the actual

**[51:40]** code structure which is the actual implementation. Visual observation

**[51:43]** implementation. Visual observation

**[51:43]** implementation. Visual observation catches problems that logs and tests

**[51:45]** catches problems that logs and tests

**[51:45]** catches problems that logs and tests miss broken rendering incorrect state

**[51:48]** miss broken rendering incorrect state

**[51:48]** miss broken rendering incorrect state and structural issues.

**[51:50]** and structural issues.

**[51:50]** and structural issues. Auditory sense tools. These tools

**[51:52]** Auditory sense tools. These tools

**[51:52]** Auditory sense tools. These tools monitor what the system reports. They

**[51:55]** monitor what the system reports. They

**[51:55]** monitor what the system reports. They capture logs and that's the system

**[51:57]** capture logs and that's the system

**[51:57]** capture logs and that's the system narrating its oper operations if you

**[51:59]** narrating its oper operations if you

**[51:59]** narrating its oper operations if you will, errors and warnings, that's


### [52:00 - 53:00]

**[52:02]** will, errors and warnings, that's

**[52:02]** will, errors and warnings, that's problems the system detects and API

**[52:04]** problems the system detects and API

**[52:04]** problems the system detects and API responses so interystem communications

**[52:07]** responses so interystem communications

**[52:07]** responses so interystem communications and critically stack traces like

**[52:09]** and critically stack traces like

**[52:09]** and critically stack traces like detailed failure information. This

**[52:11]** detailed failure information. This

**[52:11]** detailed failure information. This diagnostic information explains why

**[52:13]** diagnostic information explains why

**[52:13]** diagnostic information explains why things fail, not just that they failed.

**[52:16]** things fail, not just that they failed.

**[52:16]** things fail, not just that they failed. And lastly, tactile sensors. These tools

**[52:19]** And lastly, tactile sensors. These tools

**[52:19]** And lastly, tactile sensors. These tools enable active interaction testing. They

**[52:23]** enable active interaction testing. They

**[52:23]** enable active interaction testing. They simulate and execute user workflows. So

**[52:26]** simulate and execute user workflows. So

**[52:26]** simulate and execute user workflows. So that's completing tasks end to end. API

**[52:29]** that's completing tasks end to end. API

**[52:29]** that's completing tasks end to end. API interactions, think request response

**[52:32]** interactions, think request response

**[52:32]** interactions, think request response cycles, performance validation like

**[52:34]** cycles, performance validation like

**[52:34]** cycles, performance validation like response times and resource usage,

**[52:37]** response times and resource usage,

**[52:37]** response times and resource usage, security checks and integration testing.

**[52:40]** security checks and integration testing.

**[52:40]** security checks and integration testing. These interactions reveal whether

**[52:41]** These interactions reveal whether

**[52:41]** These interactions reveal whether software behaves correctly under actual

**[52:43]** software behaves correctly under actual

**[52:43]** software behaves correctly under actual use, not just in isolated test

**[52:46]** use, not just in isolated test

**[52:46]** use, not just in isolated test scenarios.

**[52:48]** scenarios.

**[52:48]** scenarios. Next we talk about context engineering

**[52:50]** Next we talk about context engineering

**[52:50]** Next we talk about context engineering and assembly tools. And this is a

**[52:52]** and assembly tools. And this is a

**[52:52]** and assembly tools. And this is a systematic approach to assembling

**[52:54]** systematic approach to assembling

**[52:54]** systematic approach to assembling focused complete context packages for AI

**[52:57]** focused complete context packages for AI

**[52:57]** focused complete context packages for AI agents through deliberate cross

**[52:59]** agents through deliberate cross

**[52:59]** agents through deliberate cross references. Think declarative linking


### [53:00 - 54:00]

**[53:02]** references. Think declarative linking

**[53:02]** references. Think declarative linking slash commands for process automation

**[53:05]** slash commands for process automation

**[53:05]** slash commands for process automation templates for structural predictability

**[53:08]** templates for structural predictability

**[53:08]** templates for structural predictability and markdown documentation for efficient

**[53:11]** and markdown documentation for efficient

**[53:11]** and markdown documentation for efficient passable documents. So let's talk about

**[53:15]** passable documents. So let's talk about

**[53:15]** passable documents. So let's talk about the cross referencing system here. This

**[53:16]** the cross referencing system here. This

**[53:16]** the cross referencing system here. This is a declarative linking mechanism that

**[53:18]** is a declarative linking mechanism that

**[53:18]** is a declarative linking mechanism that allows documents to explicitly reference

**[53:21]** allows documents to explicitly reference

**[53:21]** allows documents to explicitly reference other documents or code files or

**[53:23]** other documents or code files or

**[53:23]** other documents or code files or sections that enables automatic context

**[53:26]** sections that enables automatic context

**[53:26]** sections that enables automatic context assembly by following these dependency

**[53:28]** assembly by following these dependency

**[53:28]** assembly by following these dependency chains. Most good coding agents will

**[53:34]** chains. Most good coding agents will

**[53:34]** chains. Most good coding agents will understand and follow these. Then we

**[53:37]** understand and follow these. Then we

**[53:37]** understand and follow these. Then we talk slash commands or whatever the

**[53:39]** talk slash commands or whatever the

**[53:39]** talk slash commands or whatever the equivalent is in your selected coding

**[53:41]** equivalent is in your selected coding

**[53:41]** equivalent is in your selected coding agent environment. But these are process

**[53:44]** agent environment. But these are process

**[53:44]** agent environment. But these are process automation mechanisms that trigger

**[53:46]** automation mechanisms that trigger

**[53:46]** automation mechanisms that trigger multi-step framework workflows through a

**[53:48]** multi-step framework workflows through a

**[53:48]** multi-step framework workflows through a single invocation. And it's so useful

**[53:51]** single invocation. And it's so useful

**[53:51]** single invocation. And it's so useful for things like context assembly, for

**[53:53]** for things like context assembly, for

**[53:53]** for things like context assembly, for instantiating a template, for

**[53:55]** instantiating a template, for

**[53:55]** instantiating a template, for implementing sessions uh for


### [54:00 - 55:00]

**[54:03]** sorry for uh implementation session

**[54:03]** sorry for uh implementation session initialization

**[54:06]** initialization

**[54:06]** initialization and then the template system. And these

**[54:09]** and then the template system. And these

**[54:09]** and then the template system. And these are the structured document templates

**[54:11]** are the structured document templates

**[54:11]** are the structured document templates for every single framework artifact.

**[54:13]** for every single framework artifact.

**[54:13]** for every single framework artifact. Master project specification, the

**[54:15]** Master project specification, the

**[54:15]** Master project specification, the feature specification, dependency

**[54:17]** feature specification, dependency

**[54:17]** feature specification, dependency matrix, implementation plan,

**[54:19]** matrix, implementation plan,

**[54:19]** matrix, implementation plan, implementation record. And these ensure

**[54:21]** implementation record. And these ensure

**[54:21]** implementation record. And these ensure consistent format and completeness.

**[54:23]** consistent format and completeness.

**[54:23]** consistent format and completeness. Without templates, you reinvent

**[54:25]** Without templates, you reinvent

**[54:25]** Without templates, you reinvent specification structure every time. And

**[54:29]** specification structure every time. And

**[54:29]** specification structure every time. And starting from scratch is exhausting.

**[54:32]** starting from scratch is exhausting.

**[54:32]** starting from scratch is exhausting. And lastly, markdown documentation

**[54:34]** And lastly, markdown documentation

**[54:34]** And lastly, markdown documentation format. We all know what it is. Uh, but

**[54:36]** format. We all know what it is. Uh, but

**[54:36]** format. We all know what it is. Uh, but agents are so literate in it that it's

**[54:38]** agents are so literate in it that it's

**[54:38]** agents are so literate in it that it's vital to have tooling that rapidly

**[54:39]** vital to have tooling that rapidly

**[54:39]** vital to have tooling that rapidly converts inputs to markdown. Basically,

**[54:42]** converts inputs to markdown. Basically,

**[54:42]** converts inputs to markdown. Basically, anything that you want to communicate to

**[54:43]** anything that you want to communicate to

**[54:43]** anything that you want to communicate to an agent should be instantly convertible

**[54:45]** an agent should be instantly convertible

**[54:45]** an agent should be instantly convertible to markdown in the tool chain.

**[54:48]** to markdown in the tool chain.

**[54:48]** to markdown in the tool chain. Lastly, version control and progress

**[54:51]** Lastly, version control and progress

**[54:51]** Lastly, version control and progress tracking. This is a dual mechanism

**[54:53]** tracking. This is a dual mechanism

**[54:53]** tracking. This is a dual mechanism system that uses I'm just going to say

**[54:56]** system that uses I'm just going to say

**[54:56]** system that uses I'm just going to say it git for implementation history

**[54:58]** it git for implementation history

**[54:58]** it git for implementation history through atomic feature commits and


### [55:00 - 56:00]

**[55:01]** through atomic feature commits and

**[55:01]** through atomic feature commits and secondly the implementation plan for

**[55:03]** secondly the implementation plan for

**[55:04]** secondly the implementation plan for feature completion tracking. These work

**[55:06]** feature completion tracking. These work

**[55:06]** feature completion tracking. These work together to provide complete project

**[55:08]** together to provide complete project

**[55:08]** together to provide complete project provenence and current state visibility.

**[55:11]** provenence and current state visibility.

**[55:11]** provenence and current state visibility. And I will say that this is the simplest

**[55:13]** And I will say that this is the simplest

**[55:13]** And I will say that this is the simplest form of project tracking. It can get

**[55:16]** form of project tracking. It can get

**[55:16]** form of project tracking. It can get certainly more

**[55:18]** certainly more

**[55:18]** certainly more complex and integrated with other

**[55:21]** complex and integrated with other

**[55:21]** complex and integrated with other systems than this.

**[55:23]** systems than this.

**[55:23]** systems than this. But uh for version control, git or the

**[55:25]** But uh for version control, git or the

**[55:25]** But uh for version control, git or the equivalent, I think that goes without

**[55:27]** equivalent, I think that goes without

**[55:27]** equivalent, I think that goes without saying. It's like saving progress in a

**[55:29]** saying. It's like saving progress in a

**[55:29]** saying. It's like saving progress in a video game. It's obvious and essential.

**[55:32]** video game. It's obvious and essential.

**[55:32]** video game. It's obvious and essential. And then the implementation plan with

**[55:34]** And then the implementation plan with

**[55:34]** And then the implementation plan with progress tracking, we take that same

**[55:36]** progress tracking, we take that same

**[55:36]** progress tracking, we take that same planning artifact created from a

**[55:38]** planning artifact created from a

**[55:38]** planning artifact created from a template earlier and we use it for

**[55:40]** template earlier and we use it for

**[55:40]** template earlier and we use it for feature tracking. Oh, sorry, for

**[55:42]** feature tracking. Oh, sorry, for

**[55:42]** feature tracking. Oh, sorry, for progress tracking. So, Git will show us

**[55:44]** progress tracking. So, Git will show us

**[55:44]** progress tracking. So, Git will show us what changed and when, but it doesn't

**[55:46]** what changed and when, but it doesn't

**[55:46]** what changed and when, but it doesn't show us the project state. And the

**[55:49]** show us the project state. And the

**[55:49]** show us the project state. And the implementation plan fills that gap. It's

**[55:51]** implementation plan fills that gap. It's

**[55:51]** implementation plan fills that gap. It's a planning artifact that also serves as

**[55:54]** a planning artifact that also serves as

**[55:54]** a planning artifact that also serves as the progress tracker.


### [56:00 - 57:00]

**[56:01]** So, here's a quick look at my tool

**[56:01]** So, here's a quick look at my tool stack. I won't spend time talking

**[56:03]** stack. I won't spend time talking

**[56:03]** stack. I won't spend time talking through it in detail, but uh catch me in

**[56:06]** through it in detail, but uh catch me in

**[56:06]** through it in detail, but uh catch me in the hallway and I'm happy to go through

**[56:07]** the hallway and I'm happy to go through

**[56:07]** the hallway and I'm happy to go through it.

**[56:33]** [music]

**[56:33]** [music] >> All right. Well, if you've enjoyed this

**[56:35]** >> All right. Well, if you've enjoyed this

**[56:35]** >> All right. Well, if you've enjoyed this talk and you want the slides from it and

**[56:38]** talk and you want the slides from it and

**[56:38]** talk and you want the slides from it and other resources, including the

**[56:40]** other resources, including the

**[56:40]** other resources, including the soundtrack, I built a site just for this

**[56:42]** soundtrack, I built a site just for this

**[56:42]** soundtrack, I built a site just for this talk. So, check it out at

**[56:44]** talk. So, check it out at

**[56:44]** talk. So, check it out at vibecodinghangover.com.

**[56:47]** vibecodinghangover.com.

**[56:47]** vibecodinghangover.com. [music]


