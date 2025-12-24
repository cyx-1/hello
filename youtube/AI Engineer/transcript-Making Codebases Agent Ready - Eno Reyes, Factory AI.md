# Making Codebases Agent Ready - Eno Reyes, Factory AI

**Video URL:** https://youtu.be/ShuJ_CN6zr4

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** Hey everybody, my name is Eno. Uh really

**[00:23]** Hey everybody, my name is Eno. Uh really pumped to talk today about uh something

**[00:26]** pumped to talk today about uh something

**[00:26]** pumped to talk today about uh something that at Factory we care a lot about. uh

**[00:28]** that at Factory we care a lot about. uh

**[00:28]** that at Factory we care a lot about. uh when we started 2 and 1/2 years ago uh

**[00:31]** when we started 2 and 1/2 years ago uh

**[00:31]** when we started 2 and 1/2 years ago uh we said that our mission is to bring

**[00:33]** we said that our mission is to bring

**[00:33]** we said that our mission is to bring autonomy to software engineering. Um and

**[00:35]** autonomy to software engineering. Um and

**[00:35]** autonomy to software engineering. Um and that is like got a ton of loaded words

**[00:38]** that is like got a ton of loaded words

**[00:38]** that is like got a ton of loaded words in it. That sounds a little buzzwordy

**[00:39]** in it. That sounds a little buzzwordy

**[00:39]** in it. That sounds a little buzzwordy right now, but I think that the my goal

**[00:42]** right now, but I think that the my goal

**[00:42]** right now, but I think that the my goal is that you guys leave this like roughly

**[00:44]** is that you guys leave this like roughly

**[00:44]** is that you guys leave this like roughly 20 minutes uh with a bunch of insights

**[00:47]** 20 minutes uh with a bunch of insights

**[00:47]** 20 minutes uh with a bunch of insights that will apply to your organization uh

**[00:49]** that will apply to your organization uh

**[00:49]** that will apply to your organization uh and the teams that you build, the

**[00:51]** and the teams that you build, the

**[00:51]** and the teams that you build, the companies you advise, um and if you're

**[00:53]** companies you advise, um and if you're

**[00:53]** companies you advise, um and if you're building products in the space, uh

**[00:54]** building products in the space, uh

**[00:54]** building products in the space, uh insight into like sort of maybe how to

**[00:56]** insight into like sort of maybe how to

**[00:56]** insight into like sort of maybe how to think about building autonomous systems

**[00:58]** think about building autonomous systems

**[00:58]** think about building autonomous systems and also making your engineering org one


### [01:00 - 02:00]

**[01:01]** and also making your engineering org one

**[01:01]** and also making your engineering org one that's able to use agents really

**[01:03]** that's able to use agents really

**[01:03]** that's able to use agents really successfully. Um, a sort of like plus of

**[01:06]** successfully. Um, a sort of like plus of

**[01:06]** successfully. Um, a sort of like plus of this is that ideally this applies to any

**[01:08]** this is that ideally this applies to any

**[01:08]** this is that ideally this applies to any tools you're using that involve AI. So

**[01:10]** tools you're using that involve AI. So

**[01:10]** tools you're using that involve AI. So it won't be specific to like our product

**[01:11]** it won't be specific to like our product

**[01:12]** it won't be specific to like our product or any of the other amazing tools out

**[01:13]** or any of the other amazing tools out

**[01:13]** or any of the other amazing tools out there. Um, I'd like to start with a

**[01:16]** there. Um, I'd like to start with a

**[01:16]** there. Um, I'd like to start with a little bit about uh, you know, Andre

**[01:17]** little bit about uh, you know, Andre

**[01:18]** little bit about uh, you know, Andre Karpathy had a very welltimed tweet. Uh,

**[01:20]** Karpathy had a very welltimed tweet. Uh,

**[01:20]** Karpathy had a very welltimed tweet. Uh, so of course I'm going to mention it.

**[01:21]** so of course I'm going to mention it.

**[01:21]** so of course I'm going to mention it. Uh, you know, he he kind of talked about

**[01:23]** Uh, you know, he he kind of talked about

**[01:23]** Uh, you know, he he kind of talked about uh, this idea of software 2.0 coming

**[01:26]** uh, this idea of software 2.0 coming

**[01:26]** uh, this idea of software 2.0 coming from auto uh, the the ability to verify

**[01:29]** from auto uh, the the ability to verify

**[01:29]** from auto uh, the the ability to verify things, right? Um, this is something

**[01:31]** things, right? Um, this is something

**[01:31]** things, right? Um, this is something that's in sort of like the the mind of

**[01:34]** that's in sort of like the the mind of

**[01:34]** that's in sort of like the the mind of Silicon Valley right now as uh the most

**[01:37]** Silicon Valley right now as uh the most

**[01:37]** Silicon Valley right now as uh the most frontier models are built with post-

**[01:38]** frontier models are built with post-

**[01:38]** frontier models are built with post- training that involve lots of like

**[01:40]** training that involve lots of like

**[01:40]** training that involve lots of like verifiable tasks. Um, and really I think

**[01:42]** verifiable tasks. Um, and really I think

**[01:42]** verifiable tasks. Um, and really I think the most interesting thing here is the

**[01:44]** the most interesting thing here is the

**[01:44]** the most interesting thing here is the sort of frontier and boundary of what

**[01:46]** sort of frontier and boundary of what

**[01:46]** sort of frontier and boundary of what can be solved by AI systems is really

**[01:48]** can be solved by AI systems is really

**[01:48]** can be solved by AI systems is really just a uh sort of an input function of

**[01:51]** just a uh sort of an input function of

**[01:51]** just a uh sort of an input function of whether or not you can specify an

**[01:53]** whether or not you can specify an

**[01:53]** whether or not you can specify an objective and search through the space

**[01:55]** objective and search through the space

**[01:55]** objective and search through the space of possible uh solutions, right? And so

**[01:58]** of possible uh solutions, right? And so

**[01:58]** of possible uh solutions, right? And so uh we are used to building software uh


### [02:00 - 03:00]

**[02:00]** uh we are used to building software uh

**[02:00]** uh we are used to building software uh purely via specification. We say like

**[02:02]** purely via specification. We say like

**[02:02]** purely via specification. We say like the algorithm does this and like input

**[02:05]** the algorithm does this and like input

**[02:05]** the algorithm does this and like input is x output is y. But if you sort of

**[02:07]** is x output is y. But if you sort of

**[02:07]** is x output is y. But if you sort of shift your mindset to thinking about

**[02:09]** shift your mindset to thinking about

**[02:09]** shift your mindset to thinking about automation via verification uh it is a

**[02:12]** automation via verification uh it is a

**[02:12]** automation via verification uh it is a little bit of a of of a difference in

**[02:14]** little bit of a of of a difference in

**[02:14]** little bit of a of of a difference in what is possible to build. Um and there

**[02:17]** what is possible to build. Um and there

**[02:17]** what is possible to build. Um and there is another great blog post by uh Jason

**[02:20]** is another great blog post by uh Jason

**[02:20]** is another great blog post by uh Jason where he talks about the asymmetry of

**[02:22]** where he talks about the asymmetry of

**[02:22]** where he talks about the asymmetry of verification. Uh this is like pretty

**[02:24]** verification. Uh this is like pretty

**[02:24]** verification. Uh this is like pretty intuitive to most people who know about

**[02:25]** intuitive to most people who know about

**[02:26]** intuitive to most people who know about like P versus NP. Uh it's like a a thing

**[02:28]** like P versus NP. Uh it's like a a thing

**[02:28]** like P versus NP. Uh it's like a a thing that a lot of people have talked about

**[02:29]** that a lot of people have talked about

**[02:29]** that a lot of people have talked about throughout the like history of computing

**[02:31]** throughout the like history of computing

**[02:32]** throughout the like history of computing and and software. But there are a ton of

**[02:34]** and and software. But there are a ton of

**[02:34]** and and software. But there are a ton of tasks that are much easier to verify

**[02:36]** tasks that are much easier to verify

**[02:36]** tasks that are much easier to verify than they are to solve. Um and and vice

**[02:38]** than they are to solve. Um and and vice

**[02:38]** than they are to solve. Um and and vice versa, but but the the most interesting

**[02:40]** versa, but but the the most interesting

**[02:40]** versa, but but the the most interesting sorts of uh easy to verify problems are

**[02:43]** sorts of uh easy to verify problems are

**[02:43]** sorts of uh easy to verify problems are ones where there's an objective truth.

**[02:45]** ones where there's an objective truth.

**[02:45]** ones where there's an objective truth. They're pretty quick to validate whether

**[02:47]** They're pretty quick to validate whether

**[02:47]** They're pretty quick to validate whether or not they're true. Uh they're

**[02:49]** or not they're true. Uh they're

**[02:49]** or not they're true. Uh they're scalable. So validating a bunch of these

**[02:51]** scalable. So validating a bunch of these

**[02:51]** scalable. So validating a bunch of these things maybe in parallel uh is easy. Um

**[02:54]** things maybe in parallel uh is easy. Um

**[02:54]** things maybe in parallel uh is easy. Um it's low noise so your chance of

**[02:56]** it's low noise so your chance of

**[02:56]** it's low noise so your chance of validating it is like really really

**[02:58]** validating it is like really really

**[02:58]** validating it is like really really high. Um and they have continuous sort


### [03:00 - 04:00]

**[03:01]** high. Um and they have continuous sort

**[03:01]** high. Um and they have continuous sort of signals. Uh it's not just like a

**[03:03]** of signals. Uh it's not just like a

**[03:03]** of signals. Uh it's not just like a binary yes no but like maybe you're 30%

**[03:06]** binary yes no but like maybe you're 30%

**[03:06]** binary yes no but like maybe you're 30% 70% 100% accurate or correct. Um and you

**[03:10]** 70% 100% accurate or correct. Um and you

**[03:10]** 70% 100% accurate or correct. Um and you know the reason I bring both these

**[03:11]** know the reason I bring both these

**[03:11]** know the reason I bring both these things up is software development is

**[03:14]** things up is software development is

**[03:14]** things up is software development is highly verifiable. Right? This is like

**[03:16]** highly verifiable. Right? This is like

**[03:16]** highly verifiable. Right? This is like the frontier. It's why uh software

**[03:19]** the frontier. It's why uh software

**[03:19]** the frontier. It's why uh software development agents are the most advanced

**[03:20]** development agents are the most advanced

**[03:20]** development agents are the most advanced agents in the world right now. uh and

**[03:23]** agents in the world right now. uh and

**[03:23]** agents in the world right now. uh and there are so much uh there's so much

**[03:25]** there are so much uh there's so much

**[03:26]** there are so much uh there's so much work that has been put in uh over the

**[03:27]** work that has been put in uh over the

**[03:27]** work that has been put in uh over the last you know 20 to 30 years around the

**[03:30]** last you know 20 to 30 years around the

**[03:30]** last you know 20 to 30 years around the automated validation and verification of

**[03:32]** automated validation and verification of

**[03:32]** automated validation and verification of software that you build um testing right

**[03:35]** software that you build um testing right

**[03:35]** software that you build um testing right unit tests end to end tests QA tests

**[03:38]** unit tests end to end tests QA tests

**[03:38]** unit tests end to end tests QA tests right um the frontier of this is

**[03:40]** right um the frontier of this is

**[03:40]** right um the frontier of this is expanding there's tons of cool companies

**[03:42]** expanding there's tons of cool companies

**[03:42]** expanding there's tons of cool companies like browser base and computer use

**[03:44]** like browser base and computer use

**[03:44]** like browser base and computer use agents and all these things that are

**[03:45]** agents and all these things that are

**[03:45]** agents and all these things that are making it easier to validate uh really

**[03:47]** making it easier to validate uh really

**[03:48]** making it easier to validate uh really complex visual or front-end changes um

**[03:50]** complex visual or front-end changes um

**[03:50]** complex visual or front-end changes um docs right having like an open API spec

**[03:53]** docs right having like an open API spec

**[03:53]** docs right having like an open API spec for your codebase uh is something that

**[03:55]** for your codebase uh is something that

**[03:55]** for your codebase uh is something that can be automated. It's validated. Um I I

**[03:58]** can be automated. It's validated. Um I I

**[03:58]** can be automated. It's validated. Um I I I can go through and enumerate a bunch


### [04:00 - 05:00]

**[04:00]** I can go through and enumerate a bunch

**[04:00]** I can go through and enumerate a bunch of these, but I actually think it is

**[04:01]** of these, but I actually think it is

**[04:01]** of these, but I actually think it is sort of a nice checklist for yourself,

**[04:03]** sort of a nice checklist for yourself,

**[04:03]** sort of a nice checklist for yourself, right? Do you have some automated

**[04:05]** right? Do you have some automated

**[04:05]** right? Do you have some automated validation for the format of your code?

**[04:08]** validation for the format of your code?

**[04:08]** validation for the format of your code? Uh do you have llinters? These things

**[04:10]** Uh do you have llinters? These things

**[04:10]** Uh do you have llinters? These things for professional software engineers are

**[04:11]** for professional software engineers are

**[04:12]** for professional software engineers are sort of like, yeah, of course we do. But

**[04:13]** sort of like, yeah, of course we do. But

**[04:13]** sort of like, yeah, of course we do. But I think you can go a step further,

**[04:15]** I think you can go a step further,

**[04:15]** I think you can go a step further, right? This is where that continuous

**[04:17]** right? This is where that continuous

**[04:17]** right? This is where that continuous validation component comes in. Um, do

**[04:19]** validation component comes in. Um, do

**[04:19]** validation component comes in. Um, do you have llinters that are so

**[04:21]** you have llinters that are so

**[04:21]** you have llinters that are so opinionated that a coding agent will

**[04:23]** opinionated that a coding agent will

**[04:23]** opinionated that a coding agent will always make code that is exactly at the

**[04:26]** always make code that is exactly at the

**[04:26]** always make code that is exactly at the level of what your senior engineers will

**[04:27]** level of what your senior engineers will

**[04:27]** level of what your senior engineers will produce? How do you do that? What does

**[04:29]** produce? How do you do that? What does

**[04:29]** produce? How do you do that? What does that even mean? Right? Do you have tests

**[04:32]** that even mean? Right? Do you have tests

**[04:32]** that even mean? Right? Do you have tests that will fail when AI slop has been

**[04:34]** that will fail when AI slop has been

**[04:34]** that will fail when AI slop has been introduced? Uh, and when highquality AI

**[04:37]** introduced? Uh, and when highquality AI

**[04:37]** introduced? Uh, and when highquality AI code is introduced, those tests pass,

**[04:39]** code is introduced, those tests pass,

**[04:39]** code is introduced, those tests pass, right? These additional layers of

**[04:41]** right? These additional layers of

**[04:41]** right? These additional layers of validators are things that most code

**[04:44]** validators are things that most code

**[04:44]** validators are things that most code bases actually lack because humans are

**[04:46]** bases actually lack because humans are

**[04:46]** bases actually lack because humans are pretty good at handling most of this

**[04:49]** pretty good at handling most of this

**[04:49]** pretty good at handling most of this stuff without the automated validation.

**[04:51]** stuff without the automated validation.

**[04:51]** stuff without the automated validation. Right? Your company may be at some test

**[04:53]** Right? Your company may be at some test

**[04:53]** Right? Your company may be at some test coverage rate that's like 50% or 60%.

**[04:56]** coverage rate that's like 50% or 60%.

**[04:56]** coverage rate that's like 50% or 60%. And that's good enough because humans

**[04:57]** And that's good enough because humans

**[04:58]** And that's good enough because humans will test manually. Um you may have a


### [05:00 - 06:00]

**[05:00]** will test manually. Um you may have a

**[05:00]** will test manually. Um you may have a flaky build that every third build it

**[05:02]** flaky build that every third build it

**[05:02]** flaky build that every third build it sort of fails and everyone at your

**[05:03]** sort of fails and everyone at your

**[05:03]** sort of fails and everyone at your company secretly hates it but no one

**[05:05]** company secretly hates it but no one

**[05:05]** company secretly hates it but no one says anything, right? These are the

**[05:07]** says anything, right? These are the

**[05:07]** says anything, right? These are the sorts of things that we know are true

**[05:08]** sorts of things that we know are true

**[05:08]** sorts of things that we know are true about large code bases. And as you scale

**[05:11]** about large code bases. And as you scale

**[05:11]** about large code bases. And as you scale out to extremely large code bases,

**[05:12]** out to extremely large code bases,

**[05:12]** out to extremely large code bases, organizations with 44,000 plus

**[05:15]** organizations with 44,000 plus

**[05:15]** organizations with 44,000 plus engineers, right? Uh this starts to

**[05:17]** engineers, right? Uh this starts to

**[05:17]** engineers, right? Uh this starts to become a very accepted norm that the bar

**[05:19]** become a very accepted norm that the bar

**[05:19]** become a very accepted norm that the bar is sort of maybe at 50% or 60%. Um and

**[05:23]** is sort of maybe at 50% or 60%. Um and

**[05:23]** is sort of maybe at 50% or 60%. Um and the reality is is most software orgs can

**[05:25]** the reality is is most software orgs can

**[05:25]** the reality is is most software orgs can actually scale like that. uh it's sort

**[05:27]** actually scale like that. uh it's sort

**[05:27]** actually scale like that. uh it's sort of fine to be at that lower uh barrier,

**[05:30]** of fine to be at that lower uh barrier,

**[05:30]** of fine to be at that lower uh barrier, but when you start introducing AI agents

**[05:32]** but when you start introducing AI agents

**[05:32]** but when you start introducing AI agents into your software development life

**[05:34]** into your software development life

**[05:34]** into your software development life cycle, and I don't just mean in

**[05:35]** cycle, and I don't just mean in

**[05:35]** cycle, and I don't just mean in interactive coding, but really across

**[05:37]** interactive coding, but really across

**[05:37]** interactive coding, but really across the board, right? Uh review,

**[05:38]** the board, right? Uh review,

**[05:38]** the board, right? Uh review, documentation, testing, all this stuff.

**[05:41]** documentation, testing, all this stuff.

**[05:41]** documentation, testing, all this stuff. Um this breaks their capabilities. Most

**[05:43]** Um this breaks their capabilities. Most

**[05:43]** Um this breaks their capabilities. Most of you have probably only seen an AI

**[05:45]** of you have probably only seen an AI

**[05:45]** of you have probably only seen an AI agent that operates in a codebase that

**[05:47]** agent that operates in a codebase that

**[05:47]** agent that operates in a codebase that has uh a decent amount of validation. Um

**[05:51]** has uh a decent amount of validation. Um

**[05:51]** has uh a decent amount of validation. Um I think a lot of the best companies in

**[05:52]** I think a lot of the best companies in

**[05:52]** I think a lot of the best companies in the world right now actually have

**[05:54]** the world right now actually have

**[05:54]** the world right now actually have introduced very rigorous validation

**[05:56]** introduced very rigorous validation

**[05:56]** introduced very rigorous validation criteria and it means that their ability

**[05:58]** criteria and it means that their ability

**[05:58]** criteria and it means that their ability to use agents is significantly greater


### [06:00 - 07:00]

**[06:01]** to use agents is significantly greater

**[06:01]** to use agents is significantly greater than that your like average uh

**[06:03]** than that your like average uh

**[06:03]** than that your like average uh developer.

**[06:05]** developer.

**[06:05]** developer. Uh you know and and if you think about

**[06:07]** Uh you know and and if you think about

**[06:07]** Uh you know and and if you think about it this like traditional loop of

**[06:09]** it this like traditional loop of

**[06:09]** it this like traditional loop of understanding a problem, designing a

**[06:11]** understanding a problem, designing a

**[06:11]** understanding a problem, designing a solution to the problem, coding it out

**[06:13]** solution to the problem, coding it out

**[06:13]** solution to the problem, coding it out and then testing it uh sort of shifts if

**[06:16]** and then testing it uh sort of shifts if

**[06:16]** and then testing it uh sort of shifts if you have really rigorous validation. Uh

**[06:18]** you have really rigorous validation. Uh

**[06:18]** you have really rigorous validation. Uh it becomes a process of when you're

**[06:20]** it becomes a process of when you're

**[06:20]** it becomes a process of when you're using agents specifying the constraints

**[06:23]** using agents specifying the constraints

**[06:23]** using agents specifying the constraints by which you would like to be validated

**[06:25]** by which you would like to be validated

**[06:25]** by which you would like to be validated and what should be built. Uh generating

**[06:27]** and what should be built. Uh generating

**[06:27]** and what should be built. Uh generating solutions to that outcome verifying uh

**[06:30]** solutions to that outcome verifying uh

**[06:30]** solutions to that outcome verifying uh both with your automated validation as

**[06:32]** both with your automated validation as

**[06:32]** both with your automated validation as well as with your your own intuition. Um

**[06:34]** well as with your your own intuition. Um

**[06:34]** well as with your your own intuition. Um and then iteration where you continue to

**[06:36]** and then iteration where you continue to

**[06:36]** and then iteration where you continue to iterate on that loop. This move from

**[06:39]** iterate on that loop. This move from

**[06:39]** iterate on that loop. This move from sort of like traditional development to

**[06:41]** sort of like traditional development to

**[06:41]** sort of like traditional development to spec specificationdriven development is

**[06:43]** spec specificationdriven development is

**[06:43]** spec specificationdriven development is one that we're starting to see sort of

**[06:45]** one that we're starting to see sort of

**[06:45]** one that we're starting to see sort of bleed into all of the different tools.

**[06:46]** bleed into all of the different tools.

**[06:46]** bleed into all of the different tools. Different tools have spec mode. Droids

**[06:49]** Different tools have spec mode. Droids

**[06:49]** Different tools have spec mode. Droids have like our Droid is our coding agent

**[06:51]** have like our Droid is our coding agent

**[06:51]** have like our Droid is our coding agent have like specification mode, plan mode.

**[06:53]** have like specification mode, plan mode.

**[06:53]** have like specification mode, plan mode. Uh there are entire idees that orient

**[06:56]** Uh there are entire idees that orient

**[06:56]** Uh there are entire idees that orient you around this like specificationdriven

**[06:58]** you around this like specificationdriven

**[06:58]** you around this like specificationdriven flow. Um and if you combine these two


### [07:00 - 08:00]

**[07:01]** flow. Um and if you combine these two

**[07:01]** flow. Um and if you combine these two things together, this is really how you

**[07:03]** things together, this is really how you

**[07:03]** things together, this is really how you build reliable and highquality

**[07:05]** build reliable and highquality

**[07:05]** build reliable and highquality solutions. So if you think about it,

**[07:07]** solutions. So if you think about it,

**[07:07]** solutions. So if you think about it, what is like the best decision for you

**[07:09]** what is like the best decision for you

**[07:09]** what is like the best decision for you to make as an organization? Is it

**[07:12]** to make as an organization? Is it

**[07:12]** to make as an organization? Is it spending 45 days comparing every single

**[07:14]** spending 45 days comparing every single

**[07:14]** spending 45 days comparing every single possible coding tool in the space and

**[07:15]** possible coding tool in the space and

**[07:16]** possible coding tool in the space and then determining that one tool is

**[07:17]** then determining that one tool is

**[07:17]** then determining that one tool is slightly better because it's 10% more

**[07:20]** slightly better because it's 10% more

**[07:20]** slightly better because it's 10% more accurate at Swebench or is it making

**[07:22]** accurate at Swebench or is it making

**[07:22]** accurate at Swebench or is it making changes to your organizational practices

**[07:24]** changes to your organizational practices

**[07:24]** changes to your organizational practices that enable all of these coding agents

**[07:26]** that enable all of these coding agents

**[07:26]** that enable all of these coding agents to succeed and then picking one that

**[07:28]** to succeed and then picking one that

**[07:28]** to succeed and then picking one that you're, you know, developers like or

**[07:30]** you're, you know, developers like or

**[07:30]** you're, you know, developers like or honestly letting people choose from the

**[07:32]** honestly letting people choose from the

**[07:32]** honestly letting people choose from the tons of amazing tools out there.

**[07:35]** tons of amazing tools out there.

**[07:35]** tons of amazing tools out there. And when you have these validation

**[07:37]** And when you have these validation

**[07:37]** And when you have these validation criteria, you can actually introduce way

**[07:40]** criteria, you can actually introduce way

**[07:40]** criteria, you can actually introduce way more complex AI workflows to your

**[07:42]** more complex AI workflows to your

**[07:42]** more complex AI workflows to your organization, right? Uh if you cannot

**[07:44]** organization, right? Uh if you cannot

**[07:44]** organization, right? Uh if you cannot automatically validate whether or not a

**[07:47]** automatically validate whether or not a

**[07:47]** automatically validate whether or not a uh a PR is like reasonably successful or

**[07:50]** uh a PR is like reasonably successful or

**[07:50]** uh a PR is like reasonably successful or has code that won't definitely break

**[07:52]** has code that won't definitely break

**[07:52]** has code that won't definitely break prod, uh you are not going to be

**[07:54]** prod, uh you are not going to be

**[07:54]** prod, uh you are not going to be parallelizing several like agents at

**[07:56]** parallelizing several like agents at

**[07:56]** parallelizing several like agents at once, right? you are not going to be

**[07:58]** once, right? you are not going to be

**[07:58]** once, right? you are not going to be decomposing a large-scale modernization


### [08:00 - 09:00]

**[08:01]** decomposing a large-scale modernization

**[08:01]** decomposing a large-scale modernization project uh into a bunch of different

**[08:03]** project uh into a bunch of different

**[08:03]** project uh into a bunch of different subtasks like that is that is a very

**[08:06]** subtasks like that is that is a very

**[08:06]** subtasks like that is that is a very frontier style task to use AI for and if

**[08:09]** frontier style task to use AI for and if

**[08:09]** frontier style task to use AI for and if the single task execution right the

**[08:11]** the single task execution right the

**[08:11]** the single task execution right the simple I would like to get this done

**[08:13]** simple I would like to get this done

**[08:13]** simple I would like to get this done here's exactly how I'd like it to be

**[08:15]** here's exactly how I'd like it to be

**[08:15]** here's exactly how I'd like it to be done and here's how you should validate

**[08:16]** done and here's how you should validate

**[08:16]** done and here's how you should validate if that does not work nearly 100% of the

**[08:19]** if that does not work nearly 100% of the

**[08:19]** if that does not work nearly 100% of the time you can sort of forget successfully

**[08:22]** time you can sort of forget successfully

**[08:22]** time you can sort of forget successfully using these other things at scale in

**[08:23]** using these other things at scale in

**[08:24]** using these other things at scale in your company um when you get into other

**[08:26]** your company um when you get into other

**[08:26]** your company um when you get into other tools like code review, right? Uh if you

**[08:28]** tools like code review, right? Uh if you

**[08:28]** tools like code review, right? Uh if you want a really highquality AI generated

**[08:30]** want a really highquality AI generated

**[08:30]** want a really highquality AI generated code review, you need documentation for

**[08:33]** code review, you need documentation for

**[08:33]** code review, you need documentation for your AI systems. Uh and yes, uh agents

**[08:36]** your AI systems. Uh and yes, uh agents

**[08:36]** your AI systems. Uh and yes, uh agents will get better at, you know, picking

**[08:38]** will get better at, you know, picking

**[08:38]** will get better at, you know, picking out, you know, whether or not to run

**[08:40]** out, you know, whether or not to run

**[08:40]** out, you know, whether or not to run lint or test. They will get better at

**[08:42]** lint or test. They will get better at

**[08:42]** lint or test. They will get better at finding solutions when you don't have

**[08:45]** finding solutions when you don't have

**[08:45]** finding solutions when you don't have explicit pointers. They'll get better at

**[08:47]** explicit pointers. They'll get better at

**[08:47]** explicit pointers. They'll get better at search, but they won't get better at

**[08:49]** search, but they won't get better at

**[08:49]** search, but they won't get better at just randomly creating this validation

**[08:51]** just randomly creating this validation

**[08:51]** just randomly creating this validation criteria out of thin air. Right? This is

**[08:53]** criteria out of thin air. Right? This is

**[08:53]** criteria out of thin air. Right? This is why we believe software developers, by

**[08:55]** why we believe software developers, by

**[08:55]** why we believe software developers, by the way, are going to continue to be

**[08:56]** the way, are going to continue to be

**[08:56]** the way, are going to continue to be heavily involved in the process of

**[08:58]** heavily involved in the process of

**[08:58]** heavily involved in the process of building software because your role


### [09:00 - 10:00]

**[09:00]** building software because your role

**[09:00]** building software because your role starts to shift to curating the sort of

**[09:03]** starts to shift to curating the sort of

**[09:03]** starts to shift to curating the sort of environment and garden that your

**[09:04]** environment and garden that your

**[09:04]** environment and garden that your software is built from. You're setting

**[09:06]** software is built from. You're setting

**[09:06]** software is built from. You're setting the constraints. You're building these

**[09:08]** the constraints. You're building these

**[09:08]** the constraints. You're building these automations and introducing continued

**[09:10]** automations and introducing continued

**[09:10]** automations and introducing continued opinionatedness

**[09:12]** opinionatedness

**[09:12]** opinionatedness uh into the uh into these automations.

**[09:14]** uh into the uh into these automations.

**[09:14]** uh into the uh into these automations. Um, and you know, if your company

**[09:17]** Um, and you know, if your company

**[09:17]** Um, and you know, if your company doesn't have at least all of these,

**[09:18]** doesn't have at least all of these,

**[09:18]** doesn't have at least all of these, right? Then that means that there's a

**[09:20]** right? Then that means that there's a

**[09:20]** right? Then that means that there's a lot of work that you can do totally

**[09:22]** lot of work that you can do totally

**[09:22]** lot of work that you can do totally absent of a procurement cycle or buying

**[09:24]** absent of a procurement cycle or buying

**[09:24]** absent of a procurement cycle or buying one tool or trying out another one. Uh,

**[09:27]** one tool or trying out another one. Uh,

**[09:27]** one tool or trying out another one. Uh, and so plug is that we help

**[09:30]** and so plug is that we help

**[09:30]** and so plug is that we help organizations do this, right? I think

**[09:32]** organizations do this, right? I think

**[09:32]** organizations do this, right? I think that it's great to have tools that allow

**[09:34]** that it's great to have tools that allow

**[09:34]** that it's great to have tools that allow you to uh go in and assess this stuff.

**[09:37]** you to uh go in and assess this stuff.

**[09:37]** you to uh go in and assess this stuff. They have ROI analytics that let you

**[09:39]** They have ROI analytics that let you

**[09:39]** They have ROI analytics that let you interact. Um but I think that for most

**[09:42]** interact. Um but I think that for most

**[09:42]** interact. Um but I think that for most organizations uh there is actually like

**[09:44]** organizations uh there is actually like

**[09:44]** organizations uh there is actually like a very clear way to do this right you

**[09:47]** a very clear way to do this right you

**[09:47]** a very clear way to do this right you can go and analyze where are you across

**[09:50]** can go and analyze where are you across

**[09:50]** can go and analyze where are you across those eight different pillars of like

**[09:52]** those eight different pillars of like

**[09:52]** those eight different pillars of like automated validation do you have a

**[09:54]** automated validation do you have a

**[09:54]** automated validation do you have a llinter how good is the llinter do you

**[09:55]** llinter how good is the llinter do you

**[09:55]** llinter how good is the llinter do you have agents MD files an open standard

**[09:58]** have agents MD files an open standard

**[09:58]** have agents MD files an open standard that almost every single coding agent


### [10:00 - 11:00]

**[10:00]** that almost every single coding agent

**[10:00]** that almost every single coding agent supports um you can improve uh and

**[10:03]** supports um you can improve uh and

**[10:03]** supports um you can improve uh and systematically enhance uh these

**[10:05]** systematically enhance uh these

**[10:05]** systematically enhance uh these different validation criteria uh and you

**[10:08]** different validation criteria uh and you

**[10:08]** different validation criteria uh and you can go through and say Well, we're

**[10:10]** can go through and say Well, we're

**[10:10]** can go through and say Well, we're seeing that coding agents are reliable

**[10:12]** seeing that coding agents are reliable

**[10:12]** seeing that coding agents are reliable enough for a senior developer to use,

**[10:14]** enough for a senior developer to use,

**[10:14]** enough for a senior developer to use, but our junior developers, if you have

**[10:16]** but our junior developers, if you have

**[10:16]** but our junior developers, if you have the tooling to to tell, by the way, like

**[10:18]** the tooling to to tell, by the way, like

**[10:18]** the tooling to to tell, by the way, like which developer is using what tools, you

**[10:20]** which developer is using what tools, you

**[10:20]** which developer is using what tools, you you you can ask questions like maybe our

**[10:22]** you you can ask questions like maybe our

**[10:22]** you you can ask questions like maybe our junior developers are actually totally

**[10:25]** junior developers are actually totally

**[10:25]** junior developers are actually totally unable to use these coding agents. And

**[10:27]** unable to use these coding agents. And

**[10:27]** unable to use these coding agents. And you'll learn that the reason why is not

**[10:28]** you'll learn that the reason why is not

**[10:28]** you'll learn that the reason why is not because they're like more incompetent or

**[10:30]** because they're like more incompetent or

**[10:30]** because they're like more incompetent or they don't know how to use the tool, but

**[10:31]** they don't know how to use the tool, but

**[10:31]** they don't know how to use the tool, but because there's these niche practices

**[10:33]** because there's these niche practices

**[10:33]** because there's these niche practices that you don't have automated validation

**[10:35]** that you don't have automated validation

**[10:35]** that you don't have automated validation for, right? And if you think about what

**[10:37]** for, right? And if you think about what

**[10:37]** for, right? And if you think about what what is the difference between a like

**[10:39]** what is the difference between a like

**[10:39]** what is the difference between a like Google or a meta and a uh a still large

**[10:43]** Google or a meta and a uh a still large

**[10:43]** Google or a meta and a uh a still large but like 2,000 person engineering or the

**[10:46]** but like 2,000 person engineering or the

**[10:46]** but like 2,000 person engineering or the difference is that a newrad with

**[10:47]** difference is that a newrad with

**[10:47]** difference is that a newrad with effectively zero context can go and ship

**[10:50]** effectively zero context can go and ship

**[10:50]** effectively zero context can go and ship a change to make YouTube's like boundary

**[10:52]** a change to make YouTube's like boundary

**[10:52]** a change to make YouTube's like boundary like slightly more round and it won't

**[10:54]** like slightly more round and it won't

**[10:54]** like slightly more round and it won't with some degree of confidence take down

**[10:56]** with some degree of confidence take down

**[10:56]** with some degree of confidence take down YouTube for like a billion users, right?

**[10:58]** YouTube for like a billion users, right?

**[10:58]** YouTube for like a billion users, right? And the reason that's possible is


### [11:00 - 12:00]

**[11:00]** And the reason that's possible is

**[11:00]** And the reason that's possible is because of the insane amounts of

**[11:01]** because of the insane amounts of

**[11:01]** because of the insane amounts of validation that have to happen on that

**[11:03]** validation that have to happen on that

**[11:03]** validation that have to happen on that code for it to be shipped. The big

**[11:06]** code for it to be shipped. The big

**[11:06]** code for it to be shipped. The big difference that we now have is we have

**[11:07]** difference that we now have is we have

**[11:07]** difference that we now have is we have coding agents that can go and identify

**[11:10]** coding agents that can go and identify

**[11:10]** coding agents that can go and identify exactly where these gaps are and they

**[11:12]** exactly where these gaps are and they

**[11:12]** exactly where these gaps are and they can actually remediate those fixes.

**[11:14]** can actually remediate those fixes.

**[11:14]** can actually remediate those fixes. Right? So you can ask a coding agent,

**[11:16]** Right? So you can ask a coding agent,

**[11:16]** Right? So you can ask a coding agent, could you figure out where we're not

**[11:18]** could you figure out where we're not

**[11:18]** could you figure out where we're not being opinionated enough about our

**[11:19]** being opinionated enough about our

**[11:19]** being opinionated enough about our llinters. You can ask a coding agent to

**[11:22]** llinters. You can ask a coding agent to

**[11:22]** llinters. You can ask a coding agent to generate tests. We have an engineer

**[11:23]** generate tests. We have an engineer

**[11:23]** generate tests. We have an engineer named Alvin who I love this quote. He

**[11:25]** named Alvin who I love this quote. He

**[11:26]** named Alvin who I love this quote. He said a slop test is better than no test.

**[11:28]** said a slop test is better than no test.

**[11:28]** said a slop test is better than no test. Uh and I think that that's slightly

**[11:30]** Uh and I think that that's slightly

**[11:30]** Uh and I think that that's slightly controversial, but the thing that I

**[11:31]** controversial, but the thing that I

**[11:31]** controversial, but the thing that I would argue here is that just having

**[11:33]** would argue here is that just having

**[11:33]** would argue here is that just having something there, right, that it passes

**[11:36]** something there, right, that it passes

**[11:36]** something there, right, that it passes uh when changes are correct and somewhat

**[11:39]** uh when changes are correct and somewhat

**[11:39]** uh when changes are correct and somewhat accurately uh matches to the spec of

**[11:41]** accurately uh matches to the spec of

**[11:41]** accurately uh matches to the spec of what you want built, uh people will

**[11:43]** what you want built, uh people will

**[11:43]** what you want built, uh people will enhance it. They'll upgrade it and other

**[11:45]** enhance it. They'll upgrade it and other

**[11:45]** enhance it. They'll upgrade it and other agents will actually notice these tests.

**[11:48]** agents will actually notice these tests.

**[11:48]** agents will actually notice these tests. They will follow the patterns. So the

**[11:50]** They will follow the patterns. So the

**[11:50]** They will follow the patterns. So the more opinionated you get, the faster the

**[11:52]** more opinionated you get, the faster the

**[11:52]** more opinionated you get, the faster the cycle continues. So I think that what

**[11:54]** cycle continues. So I think that what

**[11:54]** cycle continues. So I think that what you guys should be thinking about is

**[11:55]** you guys should be thinking about is

**[11:55]** you guys should be thinking about is what are the feedback loops in our

**[11:56]** what are the feedback loops in our

**[11:56]** what are the feedback loops in our organization that we are catering

**[11:58]** organization that we are catering

**[11:58]** organization that we are catering towards. If you have better agents, they


### [12:00 - 13:00]

**[12:01]** towards. If you have better agents, they

**[12:01]** towards. If you have better agents, they will make the environment better which

**[12:03]** will make the environment better which

**[12:03]** will make the environment better which will make the agents better which will

**[12:04]** will make the agents better which will

**[12:04]** will make the agents better which will mean you have more time to make the

**[12:05]** mean you have more time to make the

**[12:05]** mean you have more time to make the environment better. And this is sort of

**[12:07]** environment better. And this is sort of

**[12:07]** environment better. And this is sort of the new DevX loop as well that

**[12:09]** the new DevX loop as well that

**[12:09]** the new DevX loop as well that organizations can invest in uh that will

**[12:11]** organizations can invest in uh that will

**[12:11]** organizations can invest in uh that will enhance all of the tools that you're

**[12:13]** enhance all of the tools that you're

**[12:13]** enhance all of the tools that you're procuring, right? So no matter whether

**[12:15]** procuring, right? So no matter whether

**[12:15]** procuring, right? So no matter whether it's a code review tool, a coding agent,

**[12:17]** it's a code review tool, a coding agent,

**[12:17]** it's a code review tool, a coding agent, etc., they will all benefit. Um and I

**[12:19]** etc., they will all benefit. Um and I

**[12:19]** etc., they will all benefit. Um and I would argue that it sort of shifts your

**[12:21]** would argue that it sort of shifts your

**[12:21]** would argue that it sort of shifts your mental model about what you're as a

**[12:22]** mental model about what you're as a

**[12:22]** mental model about what you're as a leader investing in when you're

**[12:24]** leader investing in when you're

**[12:24]** leader investing in when you're investing in your software work right

**[12:26]** investing in your software work right

**[12:26]** investing in your software work right now. The idea of uh you know opex as

**[12:30]** now. The idea of uh you know opex as

**[12:30]** now. The idea of uh you know opex as like the input to engineering projects

**[12:31]** like the input to engineering projects

**[12:31]** like the input to engineering projects like we are investing in we want more

**[12:33]** like we are investing in we want more

**[12:33]** like we are investing in we want more people in order to solve this problem.

**[12:35]** people in order to solve this problem.

**[12:35]** people in order to solve this problem. we need 10 more people. Um, I would I

**[12:37]** we need 10 more people. Um, I would I

**[12:37]** we need 10 more people. Um, I would I would argue that uh the other thing that

**[12:39]** would argue that uh the other thing that

**[12:39]** would argue that uh the other thing that you can now start investing in is this

**[12:40]** you can now start investing in is this

**[12:40]** you can now start investing in is this environment feedback loop that enables

**[12:42]** environment feedback loop that enables

**[12:42]** environment feedback loop that enables these additional people to be

**[12:44]** these additional people to be

**[12:44]** these additional people to be significantly more successful, right?

**[12:46]** significantly more successful, right?

**[12:46]** significantly more successful, right? And I think that that's the feedback

**[12:48]** And I think that that's the feedback

**[12:48]** And I think that that's the feedback loop that can actually take quite a lot

**[12:49]** loop that can actually take quite a lot

**[12:49]** loop that can actually take quite a lot of value because coding agents can just

**[12:51]** of value because coding agents can just

**[12:51]** of value because coding agents can just scale this out. So you know all of this

**[12:54]** scale this out. So you know all of this

**[12:54]** scale this out. So you know all of this is to say there's a lot that can be done

**[12:56]** is to say there's a lot that can be done

**[12:56]** is to say there's a lot that can be done outside of the like product itself uh to

**[12:59]** outside of the like product itself uh to

**[12:59]** outside of the like product itself uh to enable these systems and the best coding


### [13:00 - 14:00]

**[13:01]** enable these systems and the best coding

**[13:01]** enable these systems and the best coding agents will actually take advantage of

**[13:03]** agents will actually take advantage of

**[13:03]** agents will actually take advantage of these validation loops right so if your

**[13:05]** these validation loops right so if your

**[13:05]** these validation loops right so if your coding agent isn't proactively seeking

**[13:08]** coding agent isn't proactively seeking

**[13:08]** coding agent isn't proactively seeking llinters tests etc then you know at the

**[13:11]** llinters tests etc then you know at the

**[13:11]** llinters tests etc then you know at the end of the day it's not going to be as

**[13:13]** end of the day it's not going to be as

**[13:13]** end of the day it's not going to be as good as one that will seek those

**[13:15]** good as one that will seek those

**[13:15]** good as one that will seek those validation criteria and in addition to

**[13:17]** validation criteria and in addition to

**[13:17]** validation criteria and in addition to that when organizations uh uh think

**[13:20]** that when organizations uh uh think

**[13:20]** that when organizations uh uh think about these sorts of things if you're

**[13:22]** about these sorts of things if you're

**[13:22]** about these sorts of things if you're the person who's able to say, "Here's my

**[13:24]** the person who's able to say, "Here's my

**[13:24]** the person who's able to say, "Here's my opinion. Here's how I want software to

**[13:26]** opinion. Here's how I want software to

**[13:26]** opinion. Here's how I want software to be built." It scales your capabilities

**[13:29]** be built." It scales your capabilities

**[13:29]** be built." It scales your capabilities out greater than ever before. Like one

**[13:31]** out greater than ever before. Like one

**[13:31]** out greater than ever before. Like one opinionated engineer can actually

**[13:33]** opinionated engineer can actually

**[13:33]** opinionated engineer can actually meaningfully change the velocity of the

**[13:35]** meaningfully change the velocity of the

**[13:35]** meaningfully change the velocity of the entire business if you take this to

**[13:37]** entire business if you take this to

**[13:37]** entire business if you take this to heart. Uh and you have a way to measure

**[13:39]** heart. Uh and you have a way to measure

**[13:39]** heart. Uh and you have a way to measure and systematically improve. Um so that's

**[13:42]** and systematically improve. Um so that's

**[13:42]** and systematically improve. Um so that's uh you know the the majority of uh what

**[13:45]** uh you know the the majority of uh what

**[13:45]** uh you know the the majority of uh what I came here to say. I think that the the

**[13:47]** I came here to say. I think that the the

**[13:47]** I came here to say. I think that the the the only thing that I'd leave you with

**[13:49]** the only thing that I'd leave you with

**[13:49]** the only thing that I'd leave you with uh is that when you think about where AI

**[13:52]** uh is that when you think about where AI

**[13:52]** uh is that when you think about where AI is going and like where we're at today,

**[13:54]** is going and like where we're at today,

**[13:54]** is going and like where we're at today, we are still really earn early in our

**[13:57]** we are still really earn early in our

**[13:57]** we are still really earn early in our journey of using software development

**[13:58]** journey of using software development

**[13:58]** journey of using software development agents. If you want a world where the


### [14:00 - 15:00]

**[14:02]** agents. If you want a world where the

**[14:02]** agents. If you want a world where the moment a customer issue comes in, a bug

**[14:04]** moment a customer issue comes in, a bug

**[14:04]** moment a customer issue comes in, a bug is filed, that ticket is picked up, a

**[14:07]** is filed, that ticket is picked up, a

**[14:07]** is filed, that ticket is picked up, a coding agent executes on that, that

**[14:10]** coding agent executes on that, that

**[14:10]** coding agent executes on that, that feedback is presented to a developer,

**[14:12]** feedback is presented to a developer,

**[14:12]** feedback is presented to a developer, they click approve, that code is merged

**[14:15]** they click approve, that code is merged

**[14:15]** they click approve, that code is merged and deployed to production in a feedback

**[14:17]** and deployed to production in a feedback

**[14:17]** and deployed to production in a feedback loop that takes maybe an hour, 2 hours.

**[14:20]** loop that takes maybe an hour, 2 hours.

**[14:20]** loop that takes maybe an hour, 2 hours. That will be possible, right? We all are

**[14:23]** That will be possible, right? We all are

**[14:23]** That will be possible, right? We all are sort of skeptical about that fully

**[14:24]** sort of skeptical about that fully

**[14:24]** sort of skeptical about that fully autonomous flow. That is technically

**[14:27]** autonomous flow. That is technically

**[14:27]** autonomous flow. That is technically feasible today. The limiter is not the

**[14:29]** feasible today. The limiter is not the

**[14:29]** feasible today. The limiter is not the capability of the coding agent. The

**[14:31]** capability of the coding agent. The

**[14:31]** capability of the coding agent. The limit is your organization's validation

**[14:33]** limit is your organization's validation

**[14:33]** limit is your organization's validation criteria. So this is like an investment

**[14:35]** criteria. So this is like an investment

**[14:35]** criteria. So this is like an investment that made today will make your

**[14:37]** that made today will make your

**[14:37]** that made today will make your organization not 1.5x, not 2x, but that

**[14:42]** organization not 1.5x, not 2x, but that

**[14:42]** organization not 1.5x, not 2x, but that is where the real like 5x, 6x, 7x comes

**[14:45]** is where the real like 5x, 6x, 7x comes

**[14:45]** is where the real like 5x, 6x, 7x comes from. Um, and it's sort of a an easy

**[14:47]** from. Um, and it's sort of a an easy

**[14:47]** from. Um, and it's sort of a an easy thing to say and it's an unfortunate

**[14:49]** thing to say and it's an unfortunate

**[14:49]** thing to say and it's an unfortunate story because what that means is you

**[14:51]** story because what that means is you

**[14:51]** story because what that means is you have to invest in this. It's not

**[14:52]** have to invest in this. It's not

**[14:52]** have to invest in this. It's not something that like AI will just

**[14:54]** something that like AI will just

**[14:54]** something that like AI will just magically give to you. Uh it's a choice

**[14:56]** magically give to you. Uh it's a choice

**[14:56]** magically give to you. Uh it's a choice that you as an organization have. Uh and

**[14:58]** that you as an organization have. Uh and

**[14:58]** that you as an organization have. Uh and if you make it now, I can guarantee you


### [15:00 - 16:00]

**[15:00]** if you make it now, I can guarantee you

**[15:00]** if you make it now, I can guarantee you that you will be in the top 1 5% of

**[15:03]** that you will be in the top 1 5% of

**[15:03]** that you will be in the top 1 5% of organizations in terms of edge velocity.

**[15:05]** organizations in terms of edge velocity.

**[15:05]** organizations in terms of edge velocity. Um and you will out compete everybody

**[15:06]** Um and you will out compete everybody

**[15:06]** Um and you will out compete everybody else in the field. So highly recommend

**[15:09]** else in the field. So highly recommend

**[15:09]** else in the field. So highly recommend investing in this sort of stuff and

**[15:10]** investing in this sort of stuff and

**[15:10]** investing in this sort of stuff and hopefully you found this helpful and

**[15:12]** hopefully you found this helpful and

**[15:12]** hopefully you found this helpful and have some lessons to take home. Thanks.

**[15:14]** have some lessons to take home. Thanks.

**[15:14]** have some lessons to take home. Thanks. [applause]

**[15:16]** [applause]

**[15:16]** [applause] [music]

**[15:32]** [music]

**[15:32]** [music] >> Heat.


