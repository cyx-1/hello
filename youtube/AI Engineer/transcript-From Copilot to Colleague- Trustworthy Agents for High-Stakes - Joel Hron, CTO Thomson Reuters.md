# From Copilot to Colleague- Trustworthy Agents for High-Stakes - Joel Hron, CTO Thomson Reuters

**Video URL:** https://www.youtube.com/watch?v=kDEvo2__Ijg

---

## Full Transcript

### [00:00 - 01:00]

**[00:19]** [Applause]

**[00:19]** [Applause] So, uh, nice to meet you all. Thank you

**[00:21]** So, uh, nice to meet you all. Thank you

**[00:21]** So, uh, nice to meet you all. Thank you for having me. Um you know probably two

**[00:24]** for having me. Um you know probably two

**[00:24]** for having me. Um you know probably two two and a half years ago like many other

**[00:26]** two and a half years ago like many other

**[00:26]** two and a half years ago like many other companies out there you know we sort of

**[00:28]** companies out there you know we sort of

**[00:28]** companies out there you know we sort of started on this journey of of building

**[00:30]** started on this journey of of building

**[00:30]** started on this journey of of building assistants and sort of the north star

**[00:33]** assistants and sort of the north star

**[00:33]** assistants and sort of the north star that we had when we were building these

**[00:35]** that we had when we were building these

**[00:36]** that we had when we were building these assistants were that they were helpful

**[00:38]** assistants were that they were helpful

**[00:38]** assistants were that they were helpful you know and obviously we wanted them to

**[00:39]** you know and obviously we wanted them to

**[00:39]** you know and obviously we wanted them to be as accurate they could and to

**[00:42]** be as accurate they could and to

**[00:42]** be as accurate they could and to reference citations when they could and

**[00:44]** reference citations when they could and

**[00:44]** reference citations when they could and these kinds of things but at the end of

**[00:45]** these kinds of things but at the end of

**[00:45]** these kinds of things but at the end of the day we wanted it to be helpful and I

**[00:47]** the day we wanted it to be helpful and I

**[00:47]** the day we wanted it to be helpful and I think over the last two two and a half

**[00:50]** think over the last two two and a half

**[00:50]** think over the last two two and a half years and certainly like within the six

**[00:52]** years and certainly like within the six

**[00:52]** years and certainly like within the six months like that northstar has shifted

**[00:54]** months like that northstar has shifted

**[00:54]** months like that northstar has shifted from helpfulness to productive like like

**[00:58]** from helpfulness to productive like like

**[00:58]** from helpfulness to productive like like we're not asking assistants to just be


### [01:00 - 02:00]

**[01:00]** we're not asking assistants to just be

**[01:00]** we're not asking assistants to just be helpful anymore. We're asking them to

**[01:02]** helpful anymore. We're asking them to

**[01:02]** helpful anymore. We're asking them to actually like produce output um to to

**[01:05]** actually like produce output um to to

**[01:05]** actually like produce output um to to make judgments and decisions on behalf

**[01:08]** make judgments and decisions on behalf

**[01:08]** make judgments and decisions on behalf of users and uh in in the environments

**[01:11]** of users and uh in in the environments

**[01:11]** of users and uh in in the environments that we work in in the law, tax, global

**[01:15]** that we work in in the law, tax, global

**[01:16]** that we work in in the law, tax, global trade um risk and and fraud

**[01:19]** trade um risk and and fraud

**[01:19]** trade um risk and and fraud investigations like the risks of being

**[01:21]** investigations like the risks of being

**[01:22]** investigations like the risks of being wrong are are not particularly

**[01:24]** wrong are are not particularly

**[01:24]** wrong are are not particularly acceptable to our end users. So doing

**[01:27]** acceptable to our end users. So doing

**[01:27]** acceptable to our end users. So doing that in those kinds of environments I

**[01:28]** that in those kinds of environments I

**[01:28]** that in those kinds of environments I think is somewhat unique and and that's

**[01:30]** think is somewhat unique and and that's

**[01:30]** think is somewhat unique and and that's hopefully what what we'll talk about

**[01:31]** hopefully what what we'll talk about

**[01:31]** hopefully what what we'll talk about today. A little context on Thompson

**[01:34]** today. A little context on Thompson

**[01:34]** today. A little context on Thompson Reuters as a as a company. Um maybe

**[01:38]** Reuters as a as a company. Um maybe

**[01:38]** Reuters as a as a company. Um maybe maybe different from many of you who

**[01:40]** maybe different from many of you who

**[01:40]** maybe different from many of you who like started a company and grew to tens

**[01:42]** like started a company and grew to tens

**[01:42]** like started a company and grew to tens of thousands of users in a couple weeks.

**[01:44]** of thousands of users in a couple weeks.

**[01:44]** of thousands of users in a couple weeks. We we've been around for over 100 years.

**[01:47]** We we've been around for over 100 years.

**[01:47]** We we've been around for over 100 years. Um we like I said represent legal tax

**[01:50]** Um we like I said represent legal tax

**[01:50]** Um we like I said represent legal tax compliance audit risk. uh 97% of the top

**[01:54]** compliance audit risk. uh 97% of the top

**[01:54]** compliance audit risk. uh 97% of the top 100 US law firms are customers of ours.

**[01:57]** 100 US law firms are customers of ours.

**[01:57]** 100 US law firms are customers of ours. Um 99% of the Fortune 100 uh corporate


### [02:00 - 03:00]

**[02:02]** Um 99% of the Fortune 100 uh corporate

**[02:02]** Um 99% of the Fortune 100 uh corporate customers of ours uh and the top 100 US

**[02:06]** customers of ours uh and the top 100 US

**[02:06]** customers of ours uh and the top 100 US uh CPA firms. So we've had a

**[02:08]** uh CPA firms. So we've had a

**[02:08]** uh CPA firms. So we've had a long-standing and and a pretty

**[02:10]** long-standing and and a pretty

**[02:10]** long-standing and and a pretty significant presence in many of these

**[02:12]** significant presence in many of these

**[02:12]** significant presence in many of these industries for a large long time. And

**[02:14]** industries for a large long time. And

**[02:14]** industries for a large long time. And really what what it underpins that is

**[02:18]** really what what it underpins that is

**[02:18]** really what what it underpins that is our domain expertise and content. So we

**[02:20]** our domain expertise and content. So we

**[02:20]** our domain expertise and content. So we have 4,500

**[02:22]** have 4,500

**[02:22]** have 4,500 uh domain experts. I think we're the the

**[02:25]** uh domain experts. I think we're the the

**[02:25]** uh domain experts. I think we're the the the highest employer of lawyers in the

**[02:27]** the highest employer of lawyers in the

**[02:27]** the highest employer of lawyers in the world as an example and you know our

**[02:31]** world as an example and you know our

**[02:31]** world as an example and you know our proprietary content really underpins

**[02:33]** proprietary content really underpins

**[02:33]** proprietary content really underpins most of our software products uh that

**[02:35]** most of our software products uh that

**[02:35]** most of our software products uh that our customers use and it's north of one

**[02:37]** our customers use and it's north of one

**[02:37]** our customers use and it's north of one and a half terabytes of of proprietary

**[02:39]** and a half terabytes of of proprietary

**[02:39]** and a half terabytes of of proprietary content across those industries that you

**[02:42]** content across those industries that you

**[02:42]** content across those industries that you know we serve to our customers through

**[02:43]** know we serve to our customers through

**[02:43]** know we serve to our customers through through our software. Uh you know we're

**[02:46]** through our software. Uh you know we're

**[02:46]** through our software. Uh you know we're heavily inquisitive as a company. We've

**[02:48]** heavily inquisitive as a company. We've

**[02:48]** heavily inquisitive as a company. We've spent over three billion and

**[02:50]** spent over three billion and

**[02:50]** spent over three billion and acquisitions over the last couple of

**[02:52]** acquisitions over the last couple of

**[02:52]** acquisitions over the last couple of years. Uh we have an applied research

**[02:55]** years. Uh we have an applied research

**[02:55]** years. Uh we have an applied research lab with uh a little more than 200

**[02:58]** lab with uh a little more than 200

**[02:58]** lab with uh a little more than 200 scientists and engineers uh that work


### [03:00 - 04:00]

**[03:00]** scientists and engineers uh that work

**[03:00]** scientists and engineers uh that work closely with our development teams and

**[03:03]** closely with our development teams and

**[03:03]** closely with our development teams and uh as a company we spend north of 200

**[03:05]** uh as a company we spend north of 200

**[03:05]** uh as a company we spend north of 200 million a year uh in capital on AI

**[03:08]** million a year uh in capital on AI

**[03:08]** million a year uh in capital on AI product development. So it's a little

**[03:10]** product development. So it's a little

**[03:10]** product development. So it's a little background on who we are as TR. Um, so

**[03:14]** background on who we are as TR. Um, so

**[03:14]** background on who we are as TR. Um, so I'll switch gears, just talk about maybe

**[03:16]** I'll switch gears, just talk about maybe

**[03:16]** I'll switch gears, just talk about maybe ground us in the evolution of of where

**[03:18]** ground us in the evolution of of where

**[03:18]** ground us in the evolution of of where AI has been and where it's come. So I

**[03:21]** AI has been and where it's come. So I

**[03:21]** AI has been and where it's come. So I think this quote from Y Combinator and

**[03:23]** think this quote from Y Combinator and

**[03:23]** think this quote from Y Combinator and their summer 2025 sort of request for

**[03:26]** their summer 2025 sort of request for

**[03:26]** their summer 2025 sort of request for startups is pretty good grounding. And

**[03:28]** startups is pretty good grounding. And

**[03:28]** startups is pretty good grounding. And they said, I'll paraphrase a little bit

**[03:30]** they said, I'll paraphrase a little bit

**[03:30]** they said, I'll paraphrase a little bit here, but this is pretty much what they

**[03:31]** here, but this is pretty much what they

**[03:31]** here, but this is pretty much what they said. They said, don't build agentic

**[03:34]** said. They said, don't build agentic

**[03:34]** said. They said, don't build agentic tools for law firms, build law firms of

**[03:36]** tools for law firms, build law firms of

**[03:36]** tools for law firms, build law firms of agents. And I think that like signifies

**[03:39]** agents. And I think that like signifies

**[03:39]** agents. And I think that like signifies like the profound shift of like moving

**[03:41]** like the profound shift of like moving

**[03:41]** like the profound shift of like moving from helpfulness to productive. Like

**[03:43]** from helpfulness to productive. Like

**[03:44]** from helpfulness to productive. Like we're asking AI systems to now produce

**[03:46]** we're asking AI systems to now produce

**[03:46]** we're asking AI systems to now produce output and produce judgments and

**[03:48]** output and produce judgments and

**[03:48]** output and produce judgments and decisions uh and not just be helpful to

**[03:51]** decisions uh and not just be helpful to

**[03:51]** decisions uh and not just be helpful to people who are doing those kinds of

**[03:53]** people who are doing those kinds of

**[03:53]** people who are doing those kinds of tasks. Um and and that's the shift that

**[03:56]** tasks. Um and and that's the shift that

**[03:56]** tasks. Um and and that's the shift that we're experiencing with agentic AI. I

**[03:59]** we're experiencing with agentic AI. I

**[03:59]** we're experiencing with agentic AI. I think you know what what does agentic AI


### [04:00 - 05:00]

**[04:02]** think you know what what does agentic AI

**[04:02]** think you know what what does agentic AI actually mean? Uh I think we've been

**[04:05]** actually mean? Uh I think we've been

**[04:05]** actually mean? Uh I think we've been talking about this a little I think we

**[04:06]** talking about this a little I think we

**[04:06]** talking about this a little I think we we like to define it more as a spectrum.

**[04:09]** we like to define it more as a spectrum.

**[04:09]** we like to define it more as a spectrum. Uh it is not that this system is agentic

**[04:12]** Uh it is not that this system is agentic

**[04:12]** Uh it is not that this system is agentic or it is not but in fact um these are

**[04:16]** or it is not but in fact um these are

**[04:16]** or it is not but in fact um these are dials that can be used to uh to to sort

**[04:21]** dials that can be used to uh to to sort

**[04:21]** dials that can be used to uh to to sort of tune what the experience and how much

**[04:24]** of tune what the experience and how much

**[04:24]** of tune what the experience and how much agency the experience has for the user

**[04:27]** agency the experience has for the user

**[04:27]** agency the experience has for the user depending on the use case. There's some

**[04:29]** depending on the use case. There's some

**[04:29]** depending on the use case. There's some use cases where it's very exploratory

**[04:32]** use cases where it's very exploratory

**[04:32]** use cases where it's very exploratory and you may want to dial these agency

**[04:34]** and you may want to dial these agency

**[04:34]** and you may want to dial these agency dials far up. Uh there are other

**[04:38]** dials far up. Uh there are other

**[04:38]** dials far up. Uh there are other situations where there's a high degree

**[04:39]** situations where there's a high degree

**[04:39]** situations where there's a high degree of precision and and there's sort of an

**[04:41]** of precision and and there's sort of an

**[04:41]** of precision and and there's sort of an expectation of certainty uh around how a

**[04:45]** expectation of certainty uh around how a

**[04:45]** expectation of certainty uh around how a certain workflow might need to be

**[04:46]** certain workflow might need to be

**[04:46]** certain workflow might need to be executed and you may not want to dial

**[04:49]** executed and you may not want to dial

**[04:49]** executed and you may not want to dial the agency up in those situations. And

**[04:51]** the agency up in those situations. And

**[04:51]** the agency up in those situations. And so we view these things as levers that

**[04:54]** so we view these things as levers that

**[04:54]** so we view these things as levers that we are able to kind of move up and down

**[04:56]** we are able to kind of move up and down

**[04:56]** we are able to kind of move up and down depending on what our users are willing

**[04:58]** depending on what our users are willing

**[04:58]** depending on what our users are willing to tolerate in terms of the the risk of


### [05:00 - 06:00]

**[05:01]** to tolerate in terms of the the risk of

**[05:01]** to tolerate in terms of the the risk of the situation that they they may be

**[05:03]** the situation that they they may be

**[05:03]** the situation that they they may be dealing with. And each of these dials

**[05:05]** dealing with. And each of these dials

**[05:05]** dealing with. And each of these dials you can think of um somewhat discreetly.

**[05:08]** you can think of um somewhat discreetly.

**[05:08]** you can think of um somewhat discreetly. So like the autonomy dial, this is the

**[05:12]** So like the autonomy dial, this is the

**[05:12]** So like the autonomy dial, this is the ability of an AI assistant to go do a

**[05:14]** ability of an AI assistant to go do a

**[05:14]** ability of an AI assistant to go do a discrete task like summarize this

**[05:16]** discrete task like summarize this

**[05:16]** discrete task like summarize this document

**[05:17]** document

**[05:17]** document all the way down the spectrum to uh very

**[05:21]** all the way down the spectrum to uh very

**[05:21]** all the way down the spectrum to uh very variable kind of self-evolving workflows

**[05:24]** variable kind of self-evolving workflows

**[05:24]** variable kind of self-evolving workflows where the AI assistant is planning its

**[05:27]** where the AI assistant is planning its

**[05:27]** where the AI assistant is planning its own work. It's executing its own work

**[05:29]** own work. It's executing its own work

**[05:29]** own work. It's executing its own work and it's replanning that work along the

**[05:31]** and it's replanning that work along the

**[05:31]** and it's replanning that work along the way based on what is it is observing or

**[05:33]** way based on what is it is observing or

**[05:33]** way based on what is it is observing or learning along the path. Context is also

**[05:37]** learning along the path. Context is also

**[05:37]** learning along the path. Context is also a dial like the sort of first most

**[05:40]** a dial like the sort of first most

**[05:40]** a dial like the sort of first most simple examples were like using

**[05:41]** simple examples were like using

**[05:41]** simple examples were like using parametric knowledge of the models

**[05:44]** parametric knowledge of the models

**[05:44]** parametric knowledge of the models directly and then rag became a big thing

**[05:46]** directly and then rag became a big thing

**[05:46]** directly and then rag became a big thing and we we added one uh knowledge source

**[05:48]** and we we added one uh knowledge source

**[05:48]** and we we added one uh knowledge source we added another knowledge source and

**[05:50]** we added another knowledge source and

**[05:50]** we added another knowledge source and then the models then need to sort of

**[05:52]** then the models then need to sort of

**[05:52]** then the models then need to sort of rationalize between let's say a

**[05:54]** rationalize between let's say a

**[05:54]** rationalize between let's say a controlled knowledge source and the web

**[05:56]** controlled knowledge source and the web

**[05:56]** controlled knowledge source and the web and it needs to use both of these

**[05:58]** and it needs to use both of these

**[05:58]** and it needs to use both of these sources of information and it needs to

**[05:59]** sources of information and it needs to

**[05:59]** sources of information and it needs to understand which one is better under


### [06:00 - 07:00]

**[06:02]** understand which one is better under

**[06:02]** understand which one is better under which context all the way to perhaps the

**[06:05]** which context all the way to perhaps the

**[06:05]** which context all the way to perhaps the models even permuting the data sources

**[06:07]** models even permuting the data sources

**[06:07]** models even permuting the data sources themselves and updating not just the the

**[06:10]** themselves and updating not just the the

**[06:10]** themselves and updating not just the the data but perhaps the schemas of the data

**[06:12]** data but perhaps the schemas of the data

**[06:12]** data but perhaps the schemas of the data uh to make to make better use of them

**[06:15]** uh to make to make better use of them

**[06:15]** uh to make to make better use of them for future types of of questions that

**[06:17]** for future types of of questions that

**[06:17]** for future types of of questions that may get asked. Memory is another dial

**[06:20]** may get asked. Memory is another dial

**[06:20]** may get asked. Memory is another dial like you know the the earliest systems

**[06:22]** like you know the the earliest systems

**[06:22]** like you know the the earliest systems of rag that we had were somewhat

**[06:23]** of rag that we had were somewhat

**[06:24]** of rag that we had were somewhat stateless. Uh they retrieved the context

**[06:26]** stateless. Uh they retrieved the context

**[06:26]** stateless. Uh they retrieved the context at the point in time. Uh and what we're

**[06:28]** at the point in time. Uh and what we're

**[06:28]** at the point in time. Uh and what we're seeing now is that memory needs to be

**[06:30]** seeing now is that memory needs to be

**[06:30]** seeing now is that memory needs to be shared uh throughout the workflow. uh it

**[06:34]** shared uh throughout the workflow. uh it

**[06:34]** shared uh throughout the workflow. uh it may need to be shared across a series of

**[06:38]** may need to be shared across a series of

**[06:38]** may need to be shared across a series of execution steps in that workflow and it

**[06:41]** execution steps in that workflow and it

**[06:41]** execution steps in that workflow and it may need and likely does need to be

**[06:43]** may need and likely does need to be

**[06:43]** may need and likely does need to be persistent across many sessions of

**[06:45]** persistent across many sessions of

**[06:46]** persistent across many sessions of users. And so these are also dials that

**[06:48]** users. And so these are also dials that

**[06:48]** users. And so these are also dials that we can use from a from a memory

**[06:49]** we can use from a from a memory

**[06:49]** we can use from a from a memory perspective. And then lastly,

**[06:51]** perspective. And then lastly,

**[06:51]** perspective. And then lastly, coordination. Um, coordination is the

**[06:54]** coordination. Um, coordination is the

**[06:54]** coordination. Um, coordination is the idea of uh an LLM or an AI assistant

**[06:57]** idea of uh an LLM or an AI assistant

**[06:57]** idea of uh an LLM or an AI assistant just uh atomically executing a task like


### [07:00 - 08:00]

**[07:00]** just uh atomically executing a task like

**[07:00]** just uh atomically executing a task like I mentioned summarizing documents uh to

**[07:03]** I mentioned summarizing documents uh to

**[07:03]** I mentioned summarizing documents uh to delegation to tools uh to to full agent

**[07:06]** delegation to tools uh to to full agent

**[07:06]** delegation to tools uh to to full agent systems uh collaborating with each

**[07:08]** systems uh collaborating with each

**[07:08]** systems uh collaborating with each other. So again just to sum like these

**[07:11]** other. So again just to sum like these

**[07:11]** other. So again just to sum like these are levers that we view the ability to

**[07:14]** are levers that we view the ability to

**[07:14]** are levers that we view the ability to kind of pull up and down depending on

**[07:15]** kind of pull up and down depending on

**[07:15]** kind of pull up and down depending on the type of use case and and what what

**[07:17]** the type of use case and and what what

**[07:17]** the type of use case and and what what sort of agency we want to give the

**[07:19]** sort of agency we want to give the

**[07:19]** sort of agency we want to give the system.

**[07:21]** system.

**[07:21]** system. So, I'll switch gears and just share

**[07:23]** So, I'll switch gears and just share

**[07:23]** So, I'll switch gears and just share kind of some lessons that we've learned

**[07:25]** kind of some lessons that we've learned

**[07:25]** kind of some lessons that we've learned along the way from the last two and a

**[07:26]** along the way from the last two and a

**[07:26]** along the way from the last two and a half years of of building this. And and

**[07:29]** half years of of building this. And and

**[07:29]** half years of of building this. And and some of this may be obvious, some of it

**[07:31]** some of this may be obvious, some of it

**[07:31]** some of this may be obvious, some of it may not. Um, the first is going to be on

**[07:33]** may not. Um, the first is going to be on

**[07:33]** may not. Um, the first is going to be on eval.

**[07:35]** eval.

**[07:35]** eval. Evals is maybe the hardest thing that we

**[07:37]** Evals is maybe the hardest thing that we

**[07:37]** Evals is maybe the hardest thing that we do and I think for our users um one of

**[07:41]** do and I think for our users um one of

**[07:41]** do and I think for our users um one of the things that is most challenging is

**[07:43]** the things that is most challenging is

**[07:43]** the things that is most challenging is that like to build trust in the system

**[07:45]** that like to build trust in the system

**[07:45]** that like to build trust in the system they almost expect a determinism like

**[07:48]** they almost expect a determinism like

**[07:48]** they almost expect a determinism like like sort of by definition trust comes

**[07:50]** like sort of by definition trust comes

**[07:50]** like sort of by definition trust comes through like you know having certainty

**[07:53]** through like you know having certainty

**[07:53]** through like you know having certainty and and an expected outcome when you

**[07:55]** and and an expected outcome when you

**[07:55]** and and an expected outcome when you give a certain input and that is just

**[07:57]** give a certain input and that is just

**[07:57]** give a certain input and that is just not the way that these systems work and


### [08:00 - 09:00]

**[08:00]** not the way that these systems work and

**[08:00]** not the way that these systems work and uh that has been I think a really

**[08:02]** uh that has been I think a really

**[08:02]** uh that has been I think a really challenging bar not just to climb for

**[08:04]** challenging bar not just to climb for

**[08:04]** challenging bar not just to climb for our users but also for our own

**[08:07]** our users but also for our own

**[08:07]** our users but also for our own internalsmemes who evaluate these

**[08:09]** internalsmemes who evaluate these

**[08:09]** internalsmemes who evaluate these systems alongside of us. Um what we see

**[08:13]** systems alongside of us. Um what we see

**[08:13]** systems alongside of us. Um what we see in our own development is that even with

**[08:15]** in our own development is that even with

**[08:15]** in our own development is that even with highly trained domain experts in legal I

**[08:18]** highly trained domain experts in legal I

**[08:18]** highly trained domain experts in legal I could give the same set of data like

**[08:20]** could give the same set of data like

**[08:20]** could give the same set of data like question response to the same people a

**[08:24]** question response to the same people a

**[08:24]** question response to the same people a week later and we see 10 plus percent

**[08:26]** week later and we see 10 plus percent

**[08:26]** week later and we see 10 plus percent swings in accuracy by the same people on

**[08:28]** swings in accuracy by the same people on

**[08:28]** swings in accuracy by the same people on the same questions. And so their own

**[08:31]** the same questions. And so their own

**[08:31]** the same questions. And so their own judgments are highly variable as well.

**[08:33]** judgments are highly variable as well.

**[08:33]** judgments are highly variable as well. And it's it's quite difficult to to sort

**[08:36]** And it's it's quite difficult to to sort

**[08:36]** And it's it's quite difficult to to sort of uh understand whether you're climbing

**[08:38]** of uh understand whether you're climbing

**[08:38]** of uh understand whether you're climbing that hill or not. Uh the the other

**[08:42]** that hill or not. Uh the the other

**[08:42]** that hill or not. Uh the the other challenge is that you know it's quite

**[08:43]** challenge is that you know it's quite

**[08:43]** challenge is that you know it's quite expensive. These are highly trained uh

**[08:45]** expensive. These are highly trained uh

**[08:45]** expensive. These are highly trained uh lawyers or tax professionals whatever it

**[08:48]** lawyers or tax professionals whatever it

**[08:48]** lawyers or tax professionals whatever it may be. Uh and if you're iterating on a

**[08:51]** may be. Uh and if you're iterating on a

**[08:52]** may be. Uh and if you're iterating on a system every week like you know it's

**[08:53]** system every week like you know it's

**[08:53]** system every week like you know it's quite expensive to to to leverage this

**[08:56]** quite expensive to to to leverage this

**[08:56]** quite expensive to to to leverage this amount of of uh human judgment.

**[08:59]** amount of of uh human judgment.

**[08:59]** amount of of uh human judgment. um we see these challenges sort of


### [09:00 - 10:00]

**[09:01]** um we see these challenges sort of

**[09:01]** um we see these challenges sort of amplified by agentic systems. Some of

**[09:04]** amplified by agentic systems. Some of

**[09:04]** amplified by agentic systems. Some of the challenges are that uh referencing

**[09:08]** the challenges are that uh referencing

**[09:08]** the challenges are that uh referencing to source material which is probably one

**[09:10]** to source material which is probably one

**[09:10]** to source material which is probably one of the most important things for any of

**[09:11]** of the most important things for any of

**[09:11]** of the most important things for any of our applications becomes more

**[09:14]** our applications becomes more

**[09:14]** our applications becomes more challenging as you start to build these

**[09:15]** challenging as you start to build these

**[09:16]** challenging as you start to build these systems with higher levels of agency. we

**[09:18]** systems with higher levels of agency. we

**[09:18]** systems with higher levels of agency. we see these agents sort of drift and and

**[09:21]** see these agents sort of drift and and

**[09:21]** see these agents sort of drift and and identifying why they have drift drifted

**[09:24]** identifying why they have drift drifted

**[09:24]** identifying why they have drift drifted and where they have drifted along the

**[09:26]** and where they have drifted along the

**[09:26]** and where they have drifted along the trajectory becomes more challenging and

**[09:29]** trajectory becomes more challenging and

**[09:29]** trajectory becomes more challenging and building the guardrail systems

**[09:31]** building the guardrail systems

**[09:31]** building the guardrail systems themselves require you know a deep level

**[09:33]** themselves require you know a deep level

**[09:33]** themselves require you know a deep level of expert knowledge I think you know as

**[09:36]** of expert knowledge I think you know as

**[09:36]** of expert knowledge I think you know as we've approached our evals like we have

**[09:39]** we've approached our evals like we have

**[09:39]** we've approached our evals like we have really focused on uh developing pretty

**[09:41]** really focused on uh developing pretty

**[09:41]** really focused on uh developing pretty rigorous rubrics for how we eval but at

**[09:44]** rigorous rubrics for how we eval but at

**[09:44]** rigorous rubrics for how we eval but at the end of the day I do think we need

**[09:46]** the end of the day I do think we need

**[09:46]** the end of the day I do think we need sort of north stars that guide And in

**[09:48]** sort of north stars that guide And in

**[09:48]** sort of north stars that guide And in many ways like we really look at

**[09:50]** many ways like we really look at

**[09:50]** many ways like we really look at preference at the end of the day to

**[09:52]** preference at the end of the day to

**[09:52]** preference at the end of the day to really drive an understanding of are we

**[09:55]** really drive an understanding of are we

**[09:55]** really drive an understanding of are we getting better or are we getting worse.

**[09:57]** getting better or are we getting worse.

**[09:57]** getting better or are we getting worse. But we do have like deeper levels of

**[09:58]** But we do have like deeper levels of

**[09:58]** But we do have like deeper levels of rubric that we use to sort of hill climb


### [10:00 - 11:00]

**[10:01]** rubric that we use to sort of hill climb

**[10:01]** rubric that we use to sort of hill climb on certain components of the system.

**[10:04]** on certain components of the system.

**[10:04]** on certain components of the system. The other thing we've learned is that

**[10:05]** The other thing we've learned is that

**[10:05]** The other thing we've learned is that our legacy applications are you know in

**[10:07]** our legacy applications are you know in

**[10:07]** our legacy applications are you know in in many ways they're handicapped to be

**[10:09]** in many ways they're handicapped to be

**[10:09]** in many ways they're handicapped to be honest with you but in a lot of ways I

**[10:11]** honest with you but in a lot of ways I

**[10:11]** honest with you but in a lot of ways I think they're really enabling. And I'll

**[10:13]** think they're really enabling. And I'll

**[10:13]** think they're really enabling. And I'll show you a couple demos of that in in

**[10:15]** show you a couple demos of that in in

**[10:15]** show you a couple demos of that in in just a minute. But we've have 100 plus

**[10:17]** just a minute. But we've have 100 plus

**[10:17]** just a minute. But we've have 100 plus years of building software systems that

**[10:19]** years of building software systems that

**[10:19]** years of building software systems that have highly tuned domain logic. Uh and

**[10:22]** have highly tuned domain logic. Uh and

**[10:22]** have highly tuned domain logic. Uh and and our users expect this sort of logic

**[10:25]** and our users expect this sort of logic

**[10:25]** and our users expect this sort of logic in the way that they work. And you know

**[10:28]** in the way that they work. And you know

**[10:28]** in the way that they work. And you know early on in the age of building

**[10:29]** early on in the age of building

**[10:29]** early on in the age of building assistance, you know, we were kind of

**[10:31]** assistance, you know, we were kind of

**[10:31]** assistance, you know, we were kind of just starting over. We were leaving all

**[10:32]** just starting over. We were leaving all

**[10:32]** just starting over. We were leaving all that behind us and building something

**[10:34]** that behind us and building something

**[10:34]** that behind us and building something new somewhat from scratch. But what

**[10:37]** new somewhat from scratch. But what

**[10:37]** new somewhat from scratch. But what agents have allowed us to do is to

**[10:39]** agents have allowed us to do is to

**[10:39]** agents have allowed us to do is to really decompose these legacy

**[10:40]** really decompose these legacy

**[10:40]** really decompose these legacy applications and decompose the

**[10:42]** applications and decompose the

**[10:42]** applications and decompose the components of them as tools that agents

**[10:46]** components of them as tools that agents

**[10:46]** components of them as tools that agents can now use. And so we're we're finding

**[10:48]** can now use. And so we're we're finding

**[10:48]** can now use. And so we're we're finding new ways to leverage a lot of these

**[10:50]** new ways to leverage a lot of these

**[10:50]** new ways to leverage a lot of these legacy applications and infrastructure

**[10:52]** legacy applications and infrastructure

**[10:52]** legacy applications and infrastructure that um you know previously we might

**[10:55]** that um you know previously we might

**[10:55]** that um you know previously we might have thought of as baggage but I think

**[10:56]** have thought of as baggage but I think

**[10:56]** have thought of as baggage but I think are really unique assets for us uh to

**[10:59]** are really unique assets for us uh to

**[10:59]** are really unique assets for us uh to build on going forward. And then the


### [11:00 - 12:00]

**[11:01]** build on going forward. And then the

**[11:01]** build on going forward. And then the last thing I would say as a learning is

**[11:03]** last thing I would say as a learning is

**[11:03]** last thing I would say as a learning is uh which may be somewhat non-intuitive

**[11:07]** uh which may be somewhat non-intuitive

**[11:07]** uh which may be somewhat non-intuitive is you know this whole idea of MVPs

**[11:09]** is you know this whole idea of MVPs

**[11:09]** is you know this whole idea of MVPs which sort of like centers in

**[11:11]** which sort of like centers in

**[11:11]** which sort of like centers in everybody's mind when they're building a

**[11:12]** everybody's mind when they're building a

**[11:12]** everybody's mind when they're building a new product. I think I think in many

**[11:15]** new product. I think I think in many

**[11:15]** new product. I think I think in many times we've overindexed on the word

**[11:17]** times we've overindexed on the word

**[11:17]** times we've overindexed on the word minimal like and we've sort of like

**[11:19]** minimal like and we've sort of like

**[11:19]** minimal like and we've sort of like chased rabbit holes in development

**[11:21]** chased rabbit holes in development

**[11:21]** chased rabbit holes in development trying to optimize what we thought of as

**[11:23]** trying to optimize what we thought of as

**[11:24]** trying to optimize what we thought of as like sort of the smallest most valuable

**[11:26]** like sort of the smallest most valuable

**[11:26]** like sort of the smallest most valuable piece of you know code that we could

**[11:28]** piece of you know code that we could

**[11:28]** piece of you know code that we could build. And it wasn't until we actually

**[11:30]** build. And it wasn't until we actually

**[11:30]** build. And it wasn't until we actually like built the whole system that we

**[11:32]** like built the whole system that we

**[11:32]** like built the whole system that we could see the whole system operate and

**[11:34]** could see the whole system operate and

**[11:34]** could see the whole system operate and we could understand you know what

**[11:37]** we could understand you know what

**[11:38]** we could understand you know what components of that system do we go need

**[11:39]** components of that system do we go need

**[11:39]** components of that system do we go need to go spend time on versus what is just

**[11:41]** to go spend time on versus what is just

**[11:41]** to go spend time on versus what is just healed by the agentic uh sort of nature

**[11:44]** healed by the agentic uh sort of nature

**[11:44]** healed by the agentic uh sort of nature of the system itself. And it was really,

**[11:47]** of the system itself. And it was really,

**[11:47]** of the system itself. And it was really, I would say, like a mindset shift for

**[11:49]** I would say, like a mindset shift for

**[11:49]** I would say, like a mindset shift for many of our teams to not ground

**[11:51]** many of our teams to not ground

**[11:51]** many of our teams to not ground themselves in this MVP concept, but to

**[11:53]** themselves in this MVP concept, but to

**[11:53]** themselves in this MVP concept, but to try to just go build the the whole thing

**[11:55]** try to just go build the the whole thing

**[11:55]** try to just go build the the whole thing first and then learn from there rather

**[11:58]** first and then learn from there rather

**[11:58]** first and then learn from there rather than starting at a smaller component.


### [12:00 - 13:00]

**[12:01]** than starting at a smaller component.

**[12:01]** than starting at a smaller component. So with that, I'll show you just a

**[12:02]** So with that, I'll show you just a

**[12:02]** So with that, I'll show you just a couple quick demos of some applications

**[12:06]** couple quick demos of some applications

**[12:06]** couple quick demos of some applications that sort of do this work. So the first

**[12:07]** that sort of do this work. So the first

**[12:07]** that sort of do this work. So the first one is a tax use case. This is like uh

**[12:10]** one is a tax use case. This is like uh

**[12:10]** one is a tax use case. This is like uh obviously fake data but you know you can

**[12:12]** obviously fake data but you know you can

**[12:12]** obviously fake data but you know you can imagine a tax professional getting a

**[12:14]** imagine a tax professional getting a

**[12:14]** imagine a tax professional getting a bunch of documents going through those

**[12:15]** bunch of documents going through those

**[12:15]** bunch of documents going through those documents extracting data you know

**[12:17]** documents extracting data you know

**[12:18]** documents extracting data you know mapping it to a tax calculation engine

**[12:20]** mapping it to a tax calculation engine

**[12:20]** mapping it to a tax calculation engine etc etc etc. So what what this product

**[12:24]** etc etc etc. So what what this product

**[12:24]** etc etc etc. So what what this product does now is basically take source

**[12:27]** does now is basically take source

**[12:27]** does now is basically take source documents like a W2 or 1099 or whatever

**[12:30]** documents like a W2 or 1099 or whatever

**[12:30]** documents like a W2 or 1099 or whatever and you know end to end does the process

**[12:33]** and you know end to end does the process

**[12:33]** and you know end to end does the process of of generating tax return. So we use

**[12:37]** of of generating tax return. So we use

**[12:37]** of of generating tax return. So we use AI to extract data from the particular

**[12:40]** AI to extract data from the particular

**[12:40]** AI to extract data from the particular documents. We use AI to take that data

**[12:42]** documents. We use AI to take that data

**[12:42]** documents. We use AI to take that data and understand how to map it to what

**[12:45]** and understand how to map it to what

**[12:45]** and understand how to map it to what fields in a tax engine. Uh what the sort

**[12:47]** fields in a tax engine. Uh what the sort

**[12:48]** fields in a tax engine. Uh what the sort of tax laws say about the rules and

**[12:50]** of tax laws say about the rules and

**[12:50]** of tax laws say about the rules and conditions of those numerical values and

**[12:53]** conditions of those numerical values and

**[12:53]** conditions of those numerical values and whether they should apply in this case

**[12:55]** whether they should apply in this case

**[12:55]** whether they should apply in this case or that case or to this line or to that

**[12:57]** or that case or to this line or to that

**[12:57]** or that case or to this line or to that line and generate a a tax return end to


### [13:00 - 14:00]

**[13:01]** line and generate a a tax return end to

**[13:01]** line and generate a a tax return end to end. And this is a good example of a

**[13:03]** end. And this is a good example of a

**[13:03]** end. And this is a good example of a couple things I just mentioned. First is

**[13:05]** couple things I just mentioned. First is

**[13:06]** couple things I just mentioned. First is you know this is really only possible

**[13:07]** you know this is really only possible

**[13:07]** you know this is really only possible because we have the tools like a tax

**[13:11]** because we have the tools like a tax

**[13:11]** because we have the tools like a tax engine to be able to give to the model

**[13:14]** engine to be able to give to the model

**[13:14]** engine to be able to give to the model to leverage to to do these calculations.

**[13:17]** to leverage to to do these calculations.

**[13:17]** to leverage to to do these calculations. Uh we also have a validation engine

**[13:19]** Uh we also have a validation engine

**[13:19]** Uh we also have a validation engine that's built into that tax engine that

**[13:21]** that's built into that tax engine that

**[13:22]** that's built into that tax engine that the the AI system can use to validate

**[13:24]** the the AI system can use to validate

**[13:24]** the the AI system can use to validate the work that it's doing can inspect the

**[13:27]** the work that it's doing can inspect the

**[13:27]** the work that it's doing can inspect the errors. It can go look for more

**[13:28]** errors. It can go look for more

**[13:28]** errors. It can go look for more information from the documents when it

**[13:30]** information from the documents when it

**[13:30]** information from the documents when it needs it and and resolve to finish the

**[13:33]** needs it and and resolve to finish the

**[13:33]** needs it and and resolve to finish the the workflow. Um, so I think this is a

**[13:36]** the workflow. Um, so I think this is a

**[13:36]** the workflow. Um, so I think this is a good example of how we're able to

**[13:37]** good example of how we're able to

**[13:37]** good example of how we're able to decompose our legacy systems and kind of

**[13:41]** decompose our legacy systems and kind of

**[13:41]** decompose our legacy systems and kind of bring new life to them and and and

**[13:43]** bring new life to them and and and

**[13:43]** bring new life to them and and and leverage them in in a unique way. Um,

**[13:46]** leverage them in in a unique way. Um,

**[13:46]** leverage them in in a unique way. Um, the second will be uh an example of

**[13:50]** the second will be uh an example of

**[13:50]** the second will be uh an example of legal. This is like a legal research use

**[13:52]** legal. This is like a legal research use

**[13:52]** legal. This is like a legal research use case like uh where a lawyer might go in

**[13:54]** case like uh where a lawyer might go in

**[13:54]** case like uh where a lawyer might go in and prepare for litigation. And so uh as

**[13:58]** and prepare for litigation. And so uh as

**[13:58]** and prepare for litigation. And so uh as I mentioned we have one and a half plus


### [14:00 - 15:00]

**[14:00]** I mentioned we have one and a half plus

**[14:00]** I mentioned we have one and a half plus terabytes of proprietary content that we

**[14:02]** terabytes of proprietary content that we

**[14:02]** terabytes of proprietary content that we build uh our products on. And so this is

**[14:05]** build uh our products on. And so this is

**[14:05]** build uh our products on. And so this is really like a deep research

**[14:06]** really like a deep research

**[14:06]** really like a deep research implementation that is tuned for uh

**[14:09]** implementation that is tuned for uh

**[14:09]** implementation that is tuned for uh legal. And what we're doing in this

**[14:12]** legal. And what we're doing in this

**[14:12]** legal. And what we're doing in this particular case uh is uh having an AI

**[14:15]** particular case uh is uh having an AI

**[14:15]** particular case uh is uh having an AI assistant that uses the tools of our

**[14:19]** assistant that uses the tools of our

**[14:19]** assistant that uses the tools of our litigation research product. So those

**[14:21]** litigation research product. So those

**[14:21]** litigation research product. So those things would be like searching for

**[14:22]** things would be like searching for

**[14:22]** things would be like searching for documents, fetching documents, uh

**[14:25]** documents, fetching documents, uh

**[14:25]** documents, fetching documents, uh comparing citations across cases,

**[14:27]** comparing citations across cases,

**[14:27]** comparing citations across cases, validating citations within cases and is

**[14:30]** validating citations within cases and is

**[14:30]** validating citations within cases and is using the components of that application

**[14:32]** using the components of that application

**[14:32]** using the components of that application as tools to go out and search content,

**[14:36]** as tools to go out and search content,

**[14:36]** as tools to go out and search content, retrieve content. It's looking at

**[14:38]** retrieve content. It's looking at

**[14:38]** retrieve content. It's looking at various different sources of content,

**[14:40]** various different sources of content,

**[14:40]** various different sources of content, whether that be case law or statutes or

**[14:42]** whether that be case law or statutes or

**[14:42]** whether that be case law or statutes or regulations or legal know-how, you know,

**[14:46]** regulations or legal know-how, you know,

**[14:46]** regulations or legal know-how, you know, articles that we have or other blogs or

**[14:48]** articles that we have or other blogs or

**[14:48]** articles that we have or other blogs or other content that we've we've licensed

**[14:50]** other content that we've we've licensed

**[14:50]** other content that we've we've licensed in some way to reason to an appropriate

**[14:53]** in some way to reason to an appropriate

**[14:53]** in some way to reason to an appropriate answer to uh to a legal research type

**[14:56]** answer to uh to a legal research type

**[14:56]** answer to uh to a legal research type question. And what you're seeing here is

**[14:58]** question. And what you're seeing here is

**[14:58]** question. And what you're seeing here is not necessarily just the the product,


### [15:00 - 16:00]

**[15:00]** not necessarily just the the product,

**[15:00]** not necessarily just the the product, but these are sort of like under the

**[15:03]** but these are sort of like under the

**[15:03]** but these are sort of like under the product of like the trajectories that

**[15:05]** product of like the trajectories that

**[15:05]** product of like the trajectories that the model would be following along its

**[15:07]** the model would be following along its

**[15:07]** the model would be following along its path of answering this particular type

**[15:09]** path of answering this particular type

**[15:09]** path of answering this particular type of of legal question.

**[15:12]** of of legal question.

**[15:12]** of of legal question. And at the end of the flow, uh the model

**[15:15]** And at the end of the flow, uh the model

**[15:15]** And at the end of the flow, uh the model will or along the flow rather, the model

**[15:17]** will or along the flow rather, the model

**[15:17]** will or along the flow rather, the model will write notes to itself about what it

**[15:18]** will write notes to itself about what it

**[15:18]** will write notes to itself about what it is learning, what it's finding. And at

**[15:20]** is learning, what it's finding. And at

**[15:20]** is learning, what it's finding. And at the end of the flow, we'll sort of

**[15:22]** the end of the flow, we'll sort of

**[15:22]** the end of the flow, we'll sort of rationalize those notes together into

**[15:24]** rationalize those notes together into

**[15:24]** rationalize those notes together into like a a final report that sort of sums

**[15:27]** like a a final report that sort of sums

**[15:27]** like a a final report that sort of sums up all of the information that was found

**[15:30]** up all of the information that was found

**[15:30]** up all of the information that was found uh throughout the research. And I think

**[15:31]** uh throughout the research. And I think

**[15:31]** uh throughout the research. And I think most importantly, what you'll see is uh

**[15:34]** most importantly, what you'll see is uh

**[15:34]** most importantly, what you'll see is uh it it links to hard citations in our

**[15:37]** it it links to hard citations in our

**[15:37]** it it links to hard citations in our product. So every sort of blue hyperlink

**[15:40]** product. So every sort of blue hyperlink

**[15:40]** product. So every sort of blue hyperlink links to like a true case or a true

**[15:43]** links to like a true case or a true

**[15:43]** links to like a true case or a true statute. Uh and it flags the the sort of

**[15:46]** statute. Uh and it flags the the sort of

**[15:46]** statute. Uh and it flags the the sort of risk associated with that with with with

**[15:49]** risk associated with that with with with

**[15:49]** risk associated with that with with with these flags that you can see. So uh

**[15:52]** these flags that you can see. So uh

**[15:52]** these flags that you can see. So uh these are two examples that I think kind

**[15:53]** these are two examples that I think kind

**[15:53]** these are two examples that I think kind of highlight pretty well uh some of

**[15:56]** of highlight pretty well uh some of

**[15:56]** of highlight pretty well uh some of those lessons learned that I say around

**[15:58]** those lessons learned that I say around

**[15:58]** those lessons learned that I say around around decomposing applications trying


### [16:00 - 17:00]

**[16:00]** around decomposing applications trying

**[16:00]** around decomposing applications trying to build the whole product at once. Uh,

**[16:03]** to build the whole product at once. Uh,

**[16:03]** to build the whole product at once. Uh, and these are really things, like I

**[16:04]** and these are really things, like I

**[16:04]** and these are really things, like I said, that that we've we've learned the

**[16:06]** said, that that we've we've learned the

**[16:06]** said, that that we've we've learned the hard way in many cases. So, I think just

**[16:09]** hard way in many cases. So, I think just

**[16:09]** hard way in many cases. So, I think just to wrap up, I've got a few minutes and

**[16:11]** to wrap up, I've got a few minutes and

**[16:11]** to wrap up, I've got a few minutes and and we can take a couple questions as

**[16:12]** and we can take a couple questions as

**[16:12]** and we can take a couple questions as well. But, uh, I I think beginning with

**[16:15]** well. But, uh, I I think beginning with

**[16:15]** well. But, uh, I I think beginning with the whole problem in mind is is is the

**[16:18]** the whole problem in mind is is is the

**[16:18]** the whole problem in mind is is is the right strategy when you're thinking

**[16:19]** right strategy when you're thinking

**[16:19]** right strategy when you're thinking about agentic systems. Uh I think the

**[16:22]** about agentic systems. Uh I think the

**[16:22]** about agentic systems. Uh I think the way to think about a agency is is not as

**[16:25]** way to think about a agency is is not as

**[16:25]** way to think about a agency is is not as a binary thing but as a lever that you

**[16:27]** a binary thing but as a lever that you

**[16:28]** a binary thing but as a lever that you can dial up or down depending on uh the

**[16:31]** can dial up or down depending on uh the

**[16:31]** can dial up or down depending on uh the risk or the use case or the tolerance uh

**[16:33]** risk or the use case or the tolerance uh

**[16:33]** risk or the use case or the tolerance uh of your users for for certain

**[16:35]** of your users for for certain

**[16:35]** of your users for for certain situations.

**[16:37]** situations.

**[16:37]** situations. I think one way to think about agents is

**[16:38]** I think one way to think about agents is

**[16:38]** I think one way to think about agents is to to bring life back to old systems and

**[16:42]** to to bring life back to old systems and

**[16:42]** to to bring life back to old systems and and to sort of break those old systems

**[16:44]** and to sort of break those old systems

**[16:44]** and to sort of break those old systems down into components that can be

**[16:46]** down into components that can be

**[16:46]** down into components that can be leveraged uniquely uh by an agentic

**[16:49]** leveraged uniquely uh by an agentic

**[16:49]** leveraged uniquely uh by an agentic system.

**[16:51]** system.

**[16:51]** system. uh I I think focusing on where humans

**[16:53]** uh I I think focusing on where humans

**[16:54]** uh I I think focusing on where humans are in the loop in terms of evaluation

**[16:55]** are in the loop in terms of evaluation

**[16:55]** are in the loop in terms of evaluation like I said those thosemesmemes that we

**[16:58]** like I said those thosemesmemes that we

**[16:58]** like I said those thosemesmemes that we have internally are extremely important


### [17:00 - 18:00]

**[17:01]** have internally are extremely important

**[17:01]** have internally are extremely important for us and then lastly I think you know

**[17:04]** for us and then lastly I think you know

**[17:04]** for us and then lastly I think you know the reason we've done what we've done is

**[17:05]** the reason we've done what we've done is

**[17:05]** the reason we've done what we've done is because we looked at our company we said

**[17:07]** because we looked at our company we said

**[17:07]** because we looked at our company we said what are the assets that we have that

**[17:08]** what are the assets that we have that

**[17:08]** what are the assets that we have that nobody else has and it's 4500 you know

**[17:11]** nobody else has and it's 4500 you know

**[17:11]** nobody else has and it's 4500 you know domain experts terabytes of content we

**[17:14]** domain experts terabytes of content we

**[17:14]** domain experts terabytes of content we really ask ourselves like how can we use

**[17:16]** really ask ourselves like how can we use

**[17:16]** really ask ourselves like how can we use those to create the most amount of

**[17:18]** those to create the most amount of

**[17:18]** those to create the most amount of differentiation in in our products and

**[17:20]** differentiation in in our products and

**[17:20]** differentiation in in our products and so I would I would you know certainly

**[17:22]** so I would I would you know certainly

**[17:22]** so I would I would you know certainly challenge you guys to do the same for

**[17:24]** challenge you guys to do the same for

**[17:24]** challenge you guys to do the same for yourselves. What are the unique assets

**[17:25]** yourselves. What are the unique assets

**[17:25]** yourselves. What are the unique assets that you have and how can you perhaps

**[17:28]** that you have and how can you perhaps

**[17:28]** that you have and how can you perhaps best leverage those to to build

**[17:29]** best leverage those to to build

**[17:29]** best leverage those to to build uniqueness into whatever applications

**[17:32]** uniqueness into whatever applications

**[17:32]** uniqueness into whatever applications uh it is that you may be doing. So with

**[17:34]** uh it is that you may be doing. So with

**[17:34]** uh it is that you may be doing. So with that I think we've got a couple minutes

**[17:36]** that I think we've got a couple minutes

**[17:36]** that I think we've got a couple minutes for a couple questions and some mics.

**[17:42]** So great.

**[17:42]** So great. You want to use use the mic.

**[17:57]** A great presentation Mr. Joel Harren and

**[17:57]** A great presentation Mr. Joel Harren and uh my name is Prab Bala. I'm a PhD

**[17:59]** uh my name is Prab Bala. I'm a PhD


### [18:00 - 19:00]

**[18:00]** uh my name is Prab Bala. I'm a PhD student and I work for Department of

**[18:02]** student and I work for Department of

**[18:02]** student and I work for Department of Defense who sponsor me. Um so my

**[18:05]** Defense who sponsor me. Um so my

**[18:05]** Defense who sponsor me. Um so my questions are um if I it's it's a great

**[18:10]** questions are um if I it's it's a great

**[18:10]** questions are um if I it's it's a great product. If I have to take the product

**[18:13]** product. If I have to take the product

**[18:13]** product. If I have to take the product to my firm who is department of defense

**[18:17]** to my firm who is department of defense

**[18:17]** to my firm who is department of defense or any financial firms,

**[18:20]** or any financial firms,

**[18:20]** or any financial firms, how would you describe the cyber

**[18:23]** how would you describe the cyber

**[18:23]** how would you describe the cyber security postures

**[18:25]** security postures

**[18:25]** security postures uh which are mandated by CISA and

**[18:29]** uh which are mandated by CISA and

**[18:29]** uh which are mandated by CISA and government recently such as LLM firewall

**[18:33]** government recently such as LLM firewall

**[18:34]** government recently such as LLM firewall or LLM guard rails or uh automated uh

**[18:38]** or LLM guard rails or uh automated uh

**[18:38]** or LLM guard rails or uh automated uh agents for scanning

**[18:40]** agents for scanning

**[18:40]** agents for scanning vulnerabilities or any SCM security

**[18:43]** vulnerabilities or any SCM security

**[18:43]** vulnerabilities or any SCM security posture me management. How would you

**[18:46]** posture me management. How would you

**[18:46]** posture me management. How would you define the uh cyber security posture for

**[18:50]** define the uh cyber security posture for

**[18:50]** define the uh cyber security posture for the entire architecture? Yeah, I mean

**[18:53]** the entire architecture? Yeah, I mean

**[18:53]** the entire architecture? Yeah, I mean there's certainly a lot of technical

**[18:55]** there's certainly a lot of technical

**[18:55]** there's certainly a lot of technical documentation on this that I could point

**[18:56]** documentation on this that I could point

**[18:56]** documentation on this that I could point you to online, but I would just say that

**[18:58]** you to online, but I would just say that

**[18:58]** you to online, but I would just say that like, you know, we're heavily focused on


### [19:00 - 20:00]

**[19:02]** like, you know, we're heavily focused on

**[19:02]** like, you know, we're heavily focused on uh not just compliance with the

**[19:03]** uh not just compliance with the

**[19:04]** uh not just compliance with the standards of like like Fed Ramp and

**[19:05]** standards of like like Fed Ramp and

**[19:05]** standards of like like Fed Ramp and these other things when we work with the

**[19:07]** these other things when we work with the

**[19:07]** these other things when we work with the government, but also like really trying

**[19:10]** government, but also like really trying

**[19:10]** government, but also like really trying to conform to the the latest standards

**[19:12]** to conform to the the latest standards

**[19:12]** to conform to the the latest standards that are coming out like the ISO uh

**[19:14]** that are coming out like the ISO uh

**[19:14]** that are coming out like the ISO uh standard that uh recently came out.

**[19:16]** standard that uh recently came out.

**[19:16]** standard that uh recently came out. Several of our products are now uh sort

**[19:19]** Several of our products are now uh sort

**[19:19]** Several of our products are now uh sort of compliant with with with that as

**[19:21]** of compliant with with with that as

**[19:21]** of compliant with with with that as well. It's a It's a pretty quickly

**[19:23]** well. It's a It's a pretty quickly

**[19:23]** well. It's a It's a pretty quickly evolving space though, so I would say

**[19:25]** evolving space though, so I would say

**[19:25]** evolving space though, so I would say we're quite adaptable to it.

**[19:28]** we're quite adaptable to it.

**[19:28]** we're quite adaptable to it. Anyway, I think I'm getting the hand,

**[19:30]** Anyway, I think I'm getting the hand,

**[19:30]** Anyway, I think I'm getting the hand, but I appreciate the time. Thank you

**[19:32]** but I appreciate the time. Thank you

**[19:32]** but I appreciate the time. Thank you very much. And and we have a booth as

**[19:33]** very much. And and we have a booth as

**[19:33]** very much. And and we have a booth as well, so so come come say hi. Thanks.

**[19:39]** well, so so come come say hi. Thanks.

**[19:39]** well, so so come come say hi. Thanks. [Music]


