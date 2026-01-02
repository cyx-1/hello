# Shipping AI That Works- An Evaluation Framework for PMs – Aman Khan, Arize

**Video URL:** https://www.youtube.com/watch?v=2HNSG990Ew8

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** All right. Uh, nice to see everyone

**[00:16]** All right. Uh, nice to see everyone here. Um, my name is Aman. I'm an AI

**[00:19]** here. Um, my name is Aman. I'm an AI

**[00:19]** here. Um, my name is Aman. I'm an AI product manager at a company called

**[00:21]** product manager at a company called

**[00:21]** product manager at a company called Arise. Title of the talk is shipping AI

**[00:24]** Arise. Title of the talk is shipping AI

**[00:24]** Arise. Title of the talk is shipping AI that works, an evaluation framework for

**[00:26]** that works, an evaluation framework for

**[00:26]** that works, an evaluation framework for PMs. Uh, it's really going to be a

**[00:28]** PMs. Uh, it's really going to be a

**[00:28]** PMs. Uh, it's really going to be a continuation of some of the content

**[00:30]** continuation of some of the content

**[00:30]** continuation of some of the content we've been doing with, you know, some of

**[00:31]** we've been doing with, you know, some of

**[00:31]** we've been doing with, you know, some of the the PM folks like Lenny's podcast. I

**[00:34]** the the PM folks like Lenny's podcast. I

**[00:34]** the the PM folks like Lenny's podcast. I guess just quick show of hands. How many

**[00:35]** guess just quick show of hands. How many

**[00:35]** guess just quick show of hands. How many people listen to Lenny's podcast or have

**[00:37]** people listen to Lenny's podcast or have

**[00:37]** people listen to Lenny's podcast or have read read the newsletter? Awesome. Okay,

**[00:39]** read read the newsletter? Awesome. Okay,

**[00:39]** read read the newsletter? Awesome. Okay, we're going to do a couple more like

**[00:40]** we're going to do a couple more like

**[00:40]** we're going to do a couple more like audience interaction things just to like

**[00:42]** audience interaction things just to like

**[00:42]** audience interaction things just to like wake up the room a bit. So, how many

**[00:44]** wake up the room a bit. So, how many

**[00:44]** wake up the room a bit. So, how many people in the room are PMs or aspiring

**[00:47]** people in the room are PMs or aspiring

**[00:47]** people in the room are PMs or aspiring PMs?

**[00:48]** PMs?

**[00:48]** PMs? Okay, good. Good handful of people. How

**[00:51]** Okay, good. Good handful of people. How

**[00:51]** Okay, good. Good handful of people. How many of you consider yourself AI product

**[00:53]** many of you consider yourself AI product

**[00:53]** many of you consider yourself AI product managers today? Okay, awesome. Wow, that

**[00:56]** managers today? Okay, awesome. Wow, that

**[00:56]** managers today? Okay, awesome. Wow, that there's more AI PMs than there were

**[00:58]** there's more AI PMs than there were

**[00:58]** there's more AI PMs than there were regular PMs. That's interesting. Um,


### [01:00 - 02:00]

**[01:00]** regular PMs. That's interesting. Um,

**[01:00]** regular PMs. That's interesting. Um, usually that's it's a subset, but maybe

**[01:02]** usually that's it's a subset, but maybe

**[01:02]** usually that's it's a subset, but maybe I need to start asking the questions in

**[01:03]** I need to start asking the questions in

**[01:03]** I need to start asking the questions in a different order. Um, cool. Well,

**[01:05]** a different order. Um, cool. Well,

**[01:05]** a different order. Um, cool. Well, that's great. Uh, so what we're going to

**[01:07]** that's great. Uh, so what we're going to

**[01:08]** that's great. Uh, so what we're going to be doing is, you know, um, I'll go ahead

**[01:11]** be doing is, you know, um, I'll go ahead

**[01:11]** be doing is, you know, um, I'll go ahead and just do a little bit of an intro

**[01:12]** and just do a little bit of an intro

**[01:12]** and just do a little bit of an intro about myself and then we'll kind of

**[01:13]** about myself and then we'll kind of

**[01:13]** about myself and then we'll kind of cover some of the the frameworks that I

**[01:15]** cover some of the the frameworks that I

**[01:15]** cover some of the the frameworks that I think are really powerful for AIPMs to

**[01:17]** think are really powerful for AIPMs to

**[01:17]** think are really powerful for AIPMs to kind of get to know as you're building

**[01:18]** kind of get to know as you're building

**[01:18]** kind of get to know as you're building AI applications. So, a little bit about

**[01:21]** AI applications. So, a little bit about

**[01:21]** AI applications. So, a little bit about me. Um, I you know, myself, I have a

**[01:24]** me. Um, I you know, myself, I have a

**[01:24]** me. Um, I you know, myself, I have a technical background. So I actually

**[01:25]** technical background. So I actually

**[01:25]** technical background. So I actually started my career in engineering uh on

**[01:28]** started my career in engineering uh on

**[01:28]** started my career in engineering uh on actually working on self-driving cars at

**[01:30]** actually working on self-driving cars at

**[01:30]** actually working on self-driving cars at Cruz. Um and actually while I was there

**[01:33]** Cruz. Um and actually while I was there

**[01:33]** Cruz. Um and actually while I was there I ended up becoming a PM for evaluation

**[01:35]** I ended up becoming a PM for evaluation

**[01:35]** I ended up becoming a PM for evaluation systems for self-driving back in like

**[01:37]** systems for self-driving back in like

**[01:38]** systems for self-driving back in like 2018 2019. Um after that I went to

**[01:41]** 2018 2019. Um after that I went to

**[01:41]** 2018 2019. Um after that I went to Spotify to work on the machine learning

**[01:43]** Spotify to work on the machine learning

**[01:43]** Spotify to work on the machine learning platform and work on recommener systems.

**[01:45]** platform and work on recommener systems.

**[01:45]** platform and work on recommener systems. So things like discover weekly and

**[01:47]** So things like discover weekly and

**[01:47]** So things like discover weekly and search things like using embeddings to

**[01:49]** search things like using embeddings to

**[01:50]** search things like using embeddings to actually make the end product experience

**[01:51]** actually make the end product experience

**[01:51]** actually make the end product experience better. And fast forward to today, I've

**[01:54]** better. And fast forward to today, I've

**[01:54]** better. And fast forward to today, I've been at Arise uh for about three and a

**[01:56]** been at Arise uh for about three and a

**[01:56]** been at Arise uh for about three and a half years, and I'm still working on

**[01:58]** half years, and I'm still working on

**[01:58]** half years, and I'm still working on evaluation systems instead of

**[01:59]** evaluation systems instead of

**[01:59]** evaluation systems instead of self-driving cars. It's sort of


### [02:00 - 03:00]

**[02:01]** self-driving cars. It's sort of

**[02:01]** self-driving cars. It's sort of self-writing code agents. Uh and Spotify

**[02:03]** self-writing code agents. Uh and Spotify

**[02:04]** self-writing code agents. Uh and Spotify is actually one of our customers. So, we

**[02:05]** is actually one of our customers. So, we

**[02:05]** is actually one of our customers. So, we get to work with some awesome uh you

**[02:07]** get to work with some awesome uh you

**[02:07]** get to work with some awesome uh you know, ex actually, fun fact, I've

**[02:09]** know, ex actually, fun fact, I've

**[02:09]** know, ex actually, fun fact, I've actually sold Arise to all of my

**[02:11]** actually sold Arise to all of my

**[02:11]** actually sold Arise to all of my previous managers. So, um so fun fact

**[02:14]** previous managers. So, um so fun fact

**[02:14]** previous managers. So, um so fun fact there. Uh but we got to work with some

**[02:16]** there. Uh but we got to work with some

**[02:16]** there. Uh but we got to work with some awesome companies like Uber, Instacart,

**[02:19]** awesome companies like Uber, Instacart,

**[02:19]** awesome companies like Uber, Instacart, Reddit, Dolingo. So a lot of really tech

**[02:21]** Reddit, Dolingo. So a lot of really tech

**[02:21]** Reddit, Dolingo. So a lot of really tech forward companies that are building

**[02:23]** forward companies that are building

**[02:23]** forward companies that are building around AI. Uh and we actually started in

**[02:25]** around AI. Uh and we actually started in

**[02:25]** around AI. Uh and we actually started in the sort of traditional ML space of

**[02:28]** the sort of traditional ML space of

**[02:28]** the sort of traditional ML space of ranking, regression, classification type

**[02:30]** ranking, regression, classification type

**[02:30]** ranking, regression, classification type models and have now expanded into Gen AI

**[02:33]** models and have now expanded into Gen AI

**[02:33]** models and have now expanded into Gen AI and agent-based applications as well. Uh

**[02:36]** and agent-based applications as well. Uh

**[02:36]** and agent-based applications as well. Uh what we do is make sure that those

**[02:38]** what we do is make sure that those

**[02:38]** what we do is make sure that those companies, our customers when they're

**[02:40]** companies, our customers when they're

**[02:40]** companies, our customers when they're building AI applications that when those

**[02:43]** building AI applications that when those

**[02:43]** building AI applications that when those agents and applications actually work as

**[02:45]** agents and applications actually work as

**[02:45]** agents and applications actually work as expected. And it's actually a pretty

**[02:47]** expected. And it's actually a pretty

**[02:47]** expected. And it's actually a pretty hard problem. A lot of that has to do

**[02:48]** hard problem. A lot of that has to do

**[02:48]** hard problem. A lot of that has to do with uh terms that we're going to go

**[02:50]** with uh terms that we're going to go

**[02:50]** with uh terms that we're going to go into like observability and eval. But I

**[02:53]** into like observability and eval. But I

**[02:53]** into like observability and eval. But I think more broadly the space is just

**[02:55]** think more broadly the space is just

**[02:55]** think more broadly the space is just changing so fast and the models, the

**[02:58]** changing so fast and the models, the

**[02:58]** changing so fast and the models, the tools, the infrastructure layer changing


### [03:00 - 04:00]

**[03:00]** tools, the infrastructure layer changing

**[03:00]** tools, the infrastructure layer changing so fast that for us it really is a way

**[03:02]** so fast that for us it really is a way

**[03:02]** so fast that for us it really is a way for us to learn about the cutting edge

**[03:04]** for us to learn about the cutting edge

**[03:04]** for us to learn about the cutting edge like what are the leading challenges

**[03:06]** like what are the leading challenges

**[03:06]** like what are the leading challenges with use cases that people are building

**[03:08]** with use cases that people are building

**[03:08]** with use cases that people are building and try to build that into a platform

**[03:10]** and try to build that into a platform

**[03:10]** and try to build that into a platform and product that benefits everybody.

**[03:14]** and product that benefits everybody.

**[03:14]** and product that benefits everybody. Um, so what we'll cover, we're going to

**[03:15]** Um, so what we'll cover, we're going to

**[03:16]** Um, so what we'll cover, we're going to cover what are eval and why they matter.

**[03:18]** cover what are eval and why they matter.

**[03:18]** cover what are eval and why they matter. We'll actually build an AI trip planner

**[03:20]** We'll actually build an AI trip planner

**[03:20]** We'll actually build an AI trip planner uh with actually a multi- aent system.

**[03:22]** uh with actually a multi- aent system.

**[03:22]** uh with actually a multi- aent system. This part is ambitious bullet number

**[03:23]** This part is ambitious bullet number

**[03:23]** This part is ambitious bullet number two. I'm going to be honest here. Uh we

**[03:25]** two. I'm going to be honest here. Uh we

**[03:25]** two. I'm going to be honest here. Uh we were trying to push up the code right

**[03:26]** were trying to push up the code right

**[03:26]** were trying to push up the code right before so it may or may not work, but

**[03:28]** before so it may or may not work, but

**[03:28]** before so it may or may not work, but we'll give it a shot and that'll be the

**[03:29]** we'll give it a shot and that'll be the

**[03:29]** we'll give it a shot and that'll be the interactive part of the workshop and

**[03:31]** interactive part of the workshop and

**[03:31]** interactive part of the workshop and then we'll actually try to evaluate that

**[03:33]** then we'll actually try to evaluate that

**[03:33]** then we'll actually try to evaluate that AI trip planner prototype that we're

**[03:35]** AI trip planner prototype that we're

**[03:35]** AI trip planner prototype that we're going to build ourselves.

**[03:37]** going to build ourselves.

**[03:37]** going to build ourselves. Uh actually another quick show of hands

**[03:39]** Uh actually another quick show of hands

**[03:39]** Uh actually another quick show of hands for the room. How many people have heard

**[03:41]** for the room. How many people have heard

**[03:41]** for the room. How many people have heard of the term eval before? Okay, I guess

**[03:44]** of the term eval before? Okay, I guess

**[03:44]** of the term eval before? Okay, I guess it was in the title of the talk, so

**[03:45]** it was in the title of the talk, so

**[03:45]** it was in the title of the talk, so that's kind of redundant. How many

**[03:47]** that's kind of redundant. How many

**[03:47]** that's kind of redundant. How many people have actually written an eval

**[03:49]** people have actually written an eval

**[03:49]** people have actually written an eval before or tried to run an eval? Okay, a

**[03:52]** before or tried to run an eval? Okay, a

**[03:52]** before or tried to run an eval? Okay, a good number of people. Um, that's

**[03:53]** good number of people. Um, that's

**[03:53]** good number of people. Um, that's awesome. Well, what we're going to do is

**[03:55]** awesome. Well, what we're going to do is

**[03:55]** awesome. Well, what we're going to do is actually take try and take that a little

**[03:56]** actually take try and take that a little

**[03:56]** actually take try and take that a little bit of a step further. Go from writing

**[03:58]** bit of a step further. Go from writing

**[03:58]** bit of a step further. Go from writing an eval for an LLM as a judge system.


### [04:00 - 05:00]

**[04:01]** an eval for an LLM as a judge system.

**[04:01]** an eval for an LLM as a judge system. And if you've never written an eval,

**[04:02]** And if you've never written an eval,

**[04:02]** And if you've never written an eval, don't worry. We're going to cover that,

**[04:03]** don't worry. We're going to cover that,

**[04:03]** don't worry. We're going to cover that, too. But try and take that one step

**[04:05]** too. But try and take that one step

**[04:05]** too. But try and take that one step further and make it a little bit more

**[04:06]** further and make it a little bit more

**[04:06]** further and make it a little bit more kind of technical, interactive, as well.

**[04:10]** kind of technical, interactive, as well.

**[04:10]** kind of technical, interactive, as well. Okay. So, who is this session for? Uh, I

**[04:13]** Okay. So, who is this session for? Uh, I

**[04:13]** Okay. So, who is this session for? Uh, I like this diagram because um, you know,

**[04:16]** like this diagram because um, you know,

**[04:16]** like this diagram because um, you know, Lenny and I have been kind of working

**[04:17]** Lenny and I have been kind of working

**[04:17]** Lenny and I have been kind of working together a little bit more on content

**[04:19]** together a little bit more on content

**[04:19]** together a little bit more on content for educational content mostly for AI

**[04:21]** for educational content mostly for AI

**[04:21]** for educational content mostly for AI product managers. And I kind of put this

**[04:24]** product managers. And I kind of put this

**[04:24]** product managers. And I kind of put this up. I made like a little whiteboard

**[04:25]** up. I made like a little whiteboard

**[04:25]** up. I made like a little whiteboard diagram for him. And I'm like, I think

**[04:27]** diagram for him. And I'm like, I think

**[04:27]** diagram for him. And I'm like, I think this is really how I view the space,

**[04:28]** this is really how I view the space,

**[04:28]** this is really how I view the space, which is like there's this there's this,

**[04:31]** which is like there's this there's this,

**[04:31]** which is like there's this there's this, you know, you may have seen this diagram

**[04:32]** you know, you may have seen this diagram

**[04:32]** you know, you may have seen this diagram for like the Dunning Krueger effect. And

**[04:34]** for like the Dunning Krueger effect. And

**[04:34]** for like the Dunning Krueger effect. And that's kind of what came to mind here,

**[04:35]** that's kind of what came to mind here,

**[04:35]** that's kind of what came to mind here, which is as you're kind of moving along

**[04:37]** which is as you're kind of moving along

**[04:37]** which is as you're kind of moving along the curve, maybe you're just getting

**[04:39]** the curve, maybe you're just getting

**[04:39]** the curve, maybe you're just getting started, you know, with how do I use AI?

**[04:41]** started, you know, with how do I use AI?

**[04:41]** started, you know, with how do I use AI? How does AI fit into my job? I think we

**[04:44]** How does AI fit into my job? I think we

**[04:44]** How does AI fit into my job? I think we were all here to be honest a couple of

**[04:45]** were all here to be honest a couple of

**[04:45]** were all here to be honest a couple of years ago, like, you know, just to be

**[04:47]** years ago, like, you know, just to be

**[04:47]** years ago, like, you know, just to be completely honest, I think for people in

**[04:49]** completely honest, I think for people in

**[04:49]** completely honest, I think for people in the room, especially PMs, I think we all

**[04:51]** the room, especially PMs, I think we all

**[04:51]** the room, especially PMs, I think we all feel that the expectations of the

**[04:54]** feel that the expectations of the

**[04:54]** feel that the expectations of the product management role are changing.

**[04:56]** product management role are changing.

**[04:56]** product management role are changing. That's why this concept of an AIPM is

**[04:58]** That's why this concept of an AIPM is

**[04:58]** That's why this concept of an AIPM is sort of emerging. the expectations from


### [05:00 - 06:00]

**[05:00]** sort of emerging. the expectations from

**[05:00]** sort of emerging. the expectations from our stakeholders, from our executives,

**[05:02]** our stakeholders, from our executives,

**[05:02]** our stakeholders, from our executives, from our customers. It feel I feel I

**[05:05]** from our customers. It feel I feel I

**[05:05]** from our customers. It feel I feel I don't know about if other people feel

**[05:06]** don't know about if other people feel

**[05:06]** don't know about if other people feel this, but I definitely feel like the bar

**[05:08]** this, but I definitely feel like the bar

**[05:08]** this, but I definitely feel like the bar has been raised in terms of what's

**[05:10]** has been raised in terms of what's

**[05:10]** has been raised in terms of what's expected to be delivered, right?

**[05:11]** expected to be delivered, right?

**[05:12]** expected to be delivered, right? Especially if I'm working with an AI

**[05:13]** Especially if I'm working with an AI

**[05:14]** Especially if I'm working with an AI engineer on the other end, their

**[05:15]** engineer on the other end, their

**[05:15]** engineer on the other end, their expectations of what I come to them with

**[05:17]** expectations of what I come to them with

**[05:17]** expectations of what I come to them with in terms of requirements, in terms of

**[05:19]** in terms of requirements, in terms of

**[05:20]** in terms of requirements, in terms of specifying what the agent system needs

**[05:21]** specifying what the agent system needs

**[05:22]** specifying what the agent system needs to look like, it's changed. It's a step

**[05:24]** to look like, it's changed. It's a step

**[05:24]** to look like, it's changed. It's a step function different even than for me,

**[05:26]** function different even than for me,

**[05:26]** function different even than for me, even as someone who was like a technical

**[05:27]** even as someone who was like a technical

**[05:27]** even as someone who was like a technical PM before. And so I kind of felt myself

**[05:31]** PM before. And so I kind of felt myself

**[05:31]** PM before. And so I kind of felt myself go along this journey which is ironic

**[05:33]** go along this journey which is ironic

**[05:33]** go along this journey which is ironic given that I work at an eval company.

**[05:35]** given that I work at an eval company.

**[05:35]** given that I work at an eval company. You think I was like on the end of the

**[05:36]** You think I was like on the end of the

**[05:36]** You think I was like on the end of the curve but really I kind of went through

**[05:38]** curve but really I kind of went through

**[05:38]** curve but really I kind of went through this journey you know same as most of

**[05:40]** this journey you know same as most of

**[05:40]** this journey you know same as most of you which is trying to use AI in my job

**[05:43]** you which is trying to use AI in my job

**[05:43]** you which is trying to use AI in my job trying AI tools to prototype and come

**[05:45]** trying AI tools to prototype and come

**[05:45]** trying AI tools to prototype and come back with something that's you know a

**[05:47]** back with something that's you know a

**[05:47]** back with something that's you know a little bit higher resolution for my

**[05:48]** little bit higher resolution for my

**[05:48]** little bit higher resolution for my engineering team than like a Google doc

**[05:50]** engineering team than like a Google doc

**[05:50]** engineering team than like a Google doc of requirements. Once I had those

**[05:52]** of requirements. Once I had those

**[05:52]** of requirements. Once I had those prototypes and I'm like hey let's try to

**[05:54]** prototypes and I'm like hey let's try to

**[05:54]** prototypes and I'm like hey let's try to build these new UI workflows. The

**[05:56]** build these new UI workflows. The

**[05:56]** build these new UI workflows. The challenge then became how do I get a

**[05:59]** challenge then became how do I get a

**[05:59]** challenge then became how do I get a product into production especially if my


### [06:00 - 07:00]

**[06:01]** product into production especially if my

**[06:01]** product into production especially if my product has AI in it has an LLM or an

**[06:04]** product has AI in it has an LLM or an

**[06:04]** product has AI in it has an LLM or an agent and that's where I think you know

**[06:08]** agent and that's where I think you know

**[06:08]** agent and that's where I think you know that's really where that like confidence

**[06:10]** that's really where that like confidence

**[06:10]** that's really where that like confidence slump sort of hits and you kind of

**[06:11]** slump sort of hits and you kind of

**[06:11]** slump sort of hits and you kind of realize there's a lack of tooling

**[06:13]** realize there's a lack of tooling

**[06:13]** realize there's a lack of tooling there's a lack of education for how to

**[06:15]** there's a lack of education for how to

**[06:15]** there's a lack of education for how to build these systems reliably and why

**[06:18]** build these systems reliably and why

**[06:18]** build these systems reliably and why does that matter at the end of the day

**[06:20]** does that matter at the end of the day

**[06:20]** does that matter at the end of the day right and the really important takeaway

**[06:22]** right and the really important takeaway

**[06:22]** right and the really important takeaway from the fact that LLMs hallucinate we

**[06:24]** from the fact that LLMs hallucinate we

**[06:24]** from the fact that LLMs hallucinate we all know that they do is you should

**[06:26]** all know that they do is you should

**[06:26]** all know that they do is you should really look at the top two quotes here

**[06:29]** really look at the top two quotes here

**[06:29]** really look at the top two quotes here and think, okay, well, we've got Kevin

**[06:31]** and think, okay, well, we've got Kevin

**[06:31]** and think, okay, well, we've got Kevin who's chief product officer at OpenAI.

**[06:33]** who's chief product officer at OpenAI.

**[06:33]** who's chief product officer at OpenAI. We have Mike at Anthropic CPO. This is

**[06:36]** We have Mike at Anthropic CPO. This is

**[06:36]** We have Mike at Anthropic CPO. This is probably like 95% of the LLM market

**[06:39]** probably like 95% of the LLM market

**[06:39]** probably like 95% of the LLM market share. And both of the product leaders

**[06:41]** share. And both of the product leaders

**[06:41]** share. And both of the product leaders of those companies are telling you that

**[06:44]** of those companies are telling you that

**[06:44]** of those companies are telling you that their models hallucinate and that it's

**[06:46]** their models hallucinate and that it's

**[06:46]** their models hallucinate and that it's really important to write eval. This

**[06:48]** really important to write eval. This

**[06:48]** really important to write eval. This these quotes actually came from a talk

**[06:49]** these quotes actually came from a talk

**[06:50]** these quotes actually came from a talk that they were both giving at Lenny's

**[06:52]** that they were both giving at Lenny's

**[06:52]** that they were both giving at Lenny's conference uh you know earlier like in

**[06:55]** conference uh you know earlier like in

**[06:55]** conference uh you know earlier like in November of last year. And so when the

**[06:57]** November of last year. And so when the

**[06:57]** November of last year. And so when the people that are selling you the product

**[06:59]** people that are selling you the product

**[06:59]** people that are selling you the product are telling you that it's not reliable


### [07:00 - 08:00]

**[07:01]** are telling you that it's not reliable

**[07:01]** are telling you that it's not reliable you should probably listen to them. Uh

**[07:04]** you should probably listen to them. Uh

**[07:04]** you should probably listen to them. Uh on top of that I mean like you have Greg

**[07:06]** on top of that I mean like you have Greg

**[07:06]** on top of that I mean like you have Greg Brockman similarly founder of that

**[07:08]** Brockman similarly founder of that

**[07:08]** Brockman similarly founder of that company. Um you have Gary who's you know

**[07:11]** company. Um you have Gary who's you know

**[07:11]** company. Um you have Gary who's you know eval are emerging as a real moat for AI

**[07:13]** eval are emerging as a real moat for AI

**[07:13]** eval are emerging as a real moat for AI startup. So I I think this is sort of

**[07:15]** startup. So I I think this is sort of

**[07:15]** startup. So I I think this is sort of one of those pivotal moments where you

**[07:17]** one of those pivotal moments where you

**[07:17]** one of those pivotal moments where you realize, hey, people are starting to say

**[07:18]** realize, hey, people are starting to say

**[07:18]** realize, hey, people are starting to say this for a reason. Why are they saying

**[07:20]** this for a reason. Why are they saying

**[07:20]** this for a reason. Why are they saying that? Well, they're saying that because

**[07:22]** that? Well, they're saying that because

**[07:22]** that? Well, they're saying that because a lot of the same lessons from the

**[07:24]** a lot of the same lessons from the

**[07:24]** a lot of the same lessons from the self-driving space and um you know kind

**[07:27]** self-driving space and um you know kind

**[07:27]** self-driving space and um you know kind of apply in this this AI space. Okay,

**[07:28]** of apply in this this AI space. Okay,

**[07:28]** of apply in this this AI space. Okay, another audience question. How many

**[07:30]** another audience question. How many

**[07:30]** another audience question. How many people have taken a Whimo? I kind of

**[07:31]** people have taken a Whimo? I kind of

**[07:31]** people have taken a Whimo? I kind of expect that one to be pretty high. Okay,

**[07:33]** expect that one to be pretty high. Okay,

**[07:33]** expect that one to be pretty high. Okay, we're in San Francisco. If you're

**[07:34]** we're in San Francisco. If you're

**[07:34]** we're in San Francisco. If you're visiting from out of town, take a Whimo.

**[07:36]** visiting from out of town, take a Whimo.

**[07:36]** visiting from out of town, take a Whimo. It is a real world example of AI. It's

**[07:39]** It is a real world example of AI. It's

**[07:39]** It is a real world example of AI. It's it's it's an example of AI in the real

**[07:41]** it's it's an example of AI in the real

**[07:41]** it's it's an example of AI in the real physical world. And a lot of how those

**[07:43]** physical world. And a lot of how those

**[07:43]** physical world. And a lot of how those systems work actually apply to building

**[07:46]** systems work actually apply to building

**[07:46]** systems work actually apply to building AI agents today.

**[07:48]** AI agents today.

**[07:48]** AI agents today. All right, we'll do a bit of a zoom out,

**[07:50]** All right, we'll do a bit of a zoom out,

**[07:50]** All right, we'll do a bit of a zoom out, then we'll get into the technical stuff.

**[07:51]** then we'll get into the technical stuff.

**[07:51]** then we'll get into the technical stuff. I see laptops out, so we'll definitely

**[07:52]** I see laptops out, so we'll definitely

**[07:52]** I see laptops out, so we'll definitely get into, you know, writing some code

**[07:54]** get into, you know, writing some code

**[07:54]** get into, you know, writing some code and trying to get hands-on. But just to

**[07:55]** and trying to get hands-on. But just to

**[07:55]** and trying to get hands-on. But just to do a bit of a recap for folks, um what

**[07:57]** do a bit of a recap for folks, um what

**[07:58]** do a bit of a recap for folks, um what is an eval? Uh I I kind of view this as


### [08:00 - 09:00]

**[08:00]** is an eval? Uh I I kind of view this as

**[08:00]** is an eval? Uh I I kind of view this as like it's very analogous to software

**[08:02]** like it's very analogous to software

**[08:02]** like it's very analogous to software testing, but with some really key

**[08:04]** testing, but with some really key

**[08:04]** testing, but with some really key differences. Those key differences are

**[08:07]** differences. Those key differences are

**[08:07]** differences. Those key differences are software is deterministic. You know, 1

**[08:08]** software is deterministic. You know, 1

**[08:08]** software is deterministic. You know, 1 plus 1 equals 2. LLM agents are

**[08:10]** plus 1 equals 2. LLM agents are

**[08:10]** plus 1 equals 2. LLM agents are nondeterministic. If you convince an

**[08:12]** nondeterministic. If you convince an

**[08:12]** nondeterministic. If you convince an agent 1 plus 1 equals 3, it'll say like

**[08:14]** agent 1 plus 1 equals 3, it'll say like

**[08:14]** agent 1 plus 1 equals 3, it'll say like you're absolutely right. 1 plus 1 equals

**[08:15]** you're absolutely right. 1 plus 1 equals

**[08:15]** you're absolutely right. 1 plus 1 equals 3. Right? So, like we've all been there.

**[08:17]** 3. Right? So, like we've all been there.

**[08:17]** 3. Right? So, like we've all been there. We've kind of seen that these systems

**[08:19]** We've kind of seen that these systems

**[08:19]** We've kind of seen that these systems are highly manipulatable. And on top of

**[08:21]** are highly manipulatable. And on top of

**[08:21]** are highly manipulatable. And on top of that, if you build an LLM agent uh that

**[08:25]** that, if you build an LLM agent uh that

**[08:25]** that, if you build an LLM agent uh that can take multiple paths, that's very

**[08:28]** can take multiple paths, that's very

**[08:28]** can take multiple paths, that's very that's pretty different from a unit

**[08:29]** that's pretty different from a unit

**[08:29]** that's pretty different from a unit test, which is deterministic. So think

**[08:32]** test, which is deterministic. So think

**[08:32]** test, which is deterministic. So think about um the fact that you know a lot of

**[08:34]** about um the fact that you know a lot of

**[08:34]** about um the fact that you know a lot of people might are trying to like

**[08:36]** people might are trying to like

**[08:36]** people might are trying to like eliminate hallucinations from their

**[08:38]** eliminate hallucinations from their

**[08:38]** eliminate hallucinations from their agent systems. The thing is you actually

**[08:40]** agent systems. The thing is you actually

**[08:40]** agent systems. The thing is you actually kind of want your agent to hallucinate

**[08:42]** kind of want your agent to hallucinate

**[08:42]** kind of want your agent to hallucinate just in the right way and that can

**[08:44]** just in the right way and that can

**[08:44]** just in the right way and that can actually make testing it a lot more

**[08:46]** actually make testing it a lot more

**[08:46]** actually make testing it a lot more challenging as well especially when

**[08:47]** challenging as well especially when

**[08:48]** challenging as well especially when reliability is is super important. And

**[08:50]** reliability is is super important. And

**[08:50]** reliability is is super important. And then last but not least I think

**[08:51]** then last but not least I think

**[08:52]** then last but not least I think integration tests rely on existing

**[08:54]** integration tests rely on existing

**[08:54]** integration tests rely on existing codebase and documentation. A really key

**[08:56]** codebase and documentation. A really key

**[08:56]** codebase and documentation. A really key differentiation of agents is that they

**[08:58]** differentiation of agents is that they

**[08:58]** differentiation of agents is that they rely on your data. Uh if you're building


### [09:00 - 10:00]

**[09:01]** rely on your data. Uh if you're building

**[09:01]** rely on your data. Uh if you're building an agent into your enterprise, the

**[09:03]** an agent into your enterprise, the

**[09:04]** an agent into your enterprise, the reason that someone is going to use your

**[09:05]** reason that someone is going to use your

**[09:05]** reason that someone is going to use your agent versus something else is likely it

**[09:08]** agent versus something else is likely it

**[09:08]** agent versus something else is likely it might be because of the agent

**[09:09]** might be because of the agent

**[09:09]** might be because of the agent architecture, but a big part of it will

**[09:11]** architecture, but a big part of it will

**[09:11]** architecture, but a big part of it will also be because of your data that you're

**[09:13]** also be because of your data that you're

**[09:13]** also be because of your data that you're building the agent on top of. And that

**[09:15]** building the agent on top of. And that

**[09:15]** building the agent on top of. And that applies for the eval as well.

**[09:18]** applies for the eval as well.

**[09:18]** applies for the eval as well. Okay. What is an eval? So, uh I view

**[09:21]** Okay. What is an eval? So, uh I view

**[09:21]** Okay. What is an eval? So, uh I view this into like four parts that go into

**[09:23]** this into like four parts that go into

**[09:23]** this into like four parts that go into an eval. kind of just an easy like

**[09:25]** an eval. kind of just an easy like

**[09:25]** an eval. kind of just an easy like muscle memory thing. Um these brackets

**[09:27]** muscle memory thing. Um these brackets

**[09:27]** muscle memory thing. Um these brackets are a little bit out of line, but um the

**[09:29]** are a little bit out of line, but um the

**[09:29]** are a little bit out of line, but um the the idea is that you're setting the

**[09:30]** the idea is that you're setting the

**[09:30]** the idea is that you're setting the role. You're basically telling the

**[09:32]** role. You're basically telling the

**[09:32]** role. You're basically telling the agent, here's the task that you want to

**[09:34]** agent, here's the task that you want to

**[09:34]** agent, here's the task that you want to accomplish. You're providing some

**[09:35]** accomplish. You're providing some

**[09:36]** accomplish. You're providing some context, which is what you see in the

**[09:37]** context, which is what you see in the

**[09:37]** context, which is what you see in the curly braces here. And it's that's

**[09:39]** curly braces here. And it's that's

**[09:40]** curly braces here. And it's that's essentially like it's really just text

**[09:42]** essentially like it's really just text

**[09:42]** essentially like it's really just text at the end of the day. It's some text

**[09:43]** at the end of the day. It's some text

**[09:43]** at the end of the day. It's some text you want the agent to evaluate. You're

**[09:46]** you want the agent to evaluate. You're

**[09:46]** you want the agent to evaluate. You're giving the agent a goal. In this case,

**[09:47]** giving the agent a goal. In this case,

**[09:47]** giving the agent a goal. In this case, the agent is trying to determine whether

**[09:49]** the agent is trying to determine whether

**[09:49]** the agent is trying to determine whether text is toxic or not toxic. This is a

**[09:52]** text is toxic or not toxic. This is a

**[09:52]** text is toxic or not toxic. This is a kind of a classic example because

**[09:53]** kind of a classic example because

**[09:53]** kind of a classic example because there's a large toxicity data set of

**[09:55]** there's a large toxicity data set of

**[09:55]** there's a large toxicity data set of classifying text that we use um to build

**[09:58]** classifying text that we use um to build

**[09:58]** classifying text that we use um to build our eval on top of. But just kind of

**[09:59]** our eval on top of. But just kind of


### [10:00 - 11:00]

**[10:00]** our eval on top of. But just kind of note that can be any type of goal in

**[10:02]** note that can be any type of goal in

**[10:02]** note that can be any type of goal in your business case. It doesn't have to

**[10:03]** your business case. It doesn't have to

**[10:03]** your business case. It doesn't have to be toxicity. It'll be some goal that

**[10:05]** be toxicity. It'll be some goal that

**[10:05]** be toxicity. It'll be some goal that you've created this agent to evaluate.

**[10:08]** you've created this agent to evaluate.

**[10:08]** you've created this agent to evaluate. And then you provide the terminology and

**[10:10]** And then you provide the terminology and

**[10:10]** And then you provide the terminology and the label. So you're giving some

**[10:11]** the label. So you're giving some

**[10:11]** the label. So you're giving some examples of what is good and bad and

**[10:14]** examples of what is good and bad and

**[10:14]** examples of what is good and bad and you're giving it the output of either

**[10:16]** you're giving it the output of either

**[10:16]** you're giving it the output of either select good or bad. In this case, it's

**[10:18]** select good or bad. In this case, it's

**[10:18]** select good or bad. In this case, it's toxic not toxic. I'm going to pause on

**[10:21]** toxic not toxic. I'm going to pause on

**[10:21]** toxic not toxic. I'm going to pause on that last note because it's really I

**[10:23]** that last note because it's really I

**[10:23]** that last note because it's really I think there's a lot of misconceptions

**[10:25]** think there's a lot of misconceptions

**[10:25]** think there's a lot of misconceptions sort of like I'll try and weave in some

**[10:27]** sort of like I'll try and weave in some

**[10:27]** sort of like I'll try and weave in some like FAQs as I hear them come up but um

**[10:29]** like FAQs as I hear them come up but um

**[10:29]** like FAQs as I hear them come up but um we'll definitely have some time at the

**[10:31]** we'll definitely have some time at the

**[10:31]** we'll definitely have some time at the end for questions and I'd love for this

**[10:33]** end for questions and I'd love for this

**[10:33]** end for questions and I'd love for this to be interactive so I'll probably make

**[10:35]** to be interactive so I'll probably make

**[10:35]** to be interactive so I'll probably make the Q&A session a little bit longer here

**[10:37]** the Q&A session a little bit longer here

**[10:37]** the Q&A session a little bit longer here for people that have these questions but

**[10:38]** for people that have these questions but

**[10:38]** for people that have these questions but one common question we get is why can't

**[10:41]** one common question we get is why can't

**[10:41]** one common question we get is why can't I just tell the agent to give me a score

**[10:43]** I just tell the agent to give me a score

**[10:43]** I just tell the agent to give me a score or an LLM to produce a score and the

**[10:46]** or an LLM to produce a score and the

**[10:46]** or an LLM to produce a score and the reason for that is because even today

**[10:48]** reason for that is because even today

**[10:48]** reason for that is because even today even though we have like PhD level LLMs,

**[10:50]** even though we have like PhD level LLMs,

**[10:50]** even though we have like PhD level LLMs, they're still really bad at numbers. Um,

**[10:53]** they're still really bad at numbers. Um,

**[10:53]** they're still really bad at numbers. Um, and so what you want to do is ground,

**[10:55]** and so what you want to do is ground,

**[10:55]** and so what you want to do is ground, and it's actually a function of like

**[10:57]** and it's actually a function of like

**[10:57]** and it's actually a function of like what a token is, what how a token is

**[10:59]** what a token is, what how a token is

**[10:59]** what a token is, what how a token is represented for an LLM. And so what you


### [11:00 - 12:00]

**[11:01]** represented for an LLM. And so what you

**[11:02]** represented for an LLM. And so what you want to do is actually give a text label

**[11:05]** want to do is actually give a text label

**[11:05]** want to do is actually give a text label that you can map to a score if you

**[11:07]** that you can map to a score if you

**[11:07]** that you can map to a score if you really need to use a score in your

**[11:09]** really need to use a score in your

**[11:09]** really need to use a score in your systems, which we do in our system as

**[11:11]** systems, which we do in our system as

**[11:11]** systems, which we do in our system as well. We'll map a label to a score. But

**[11:12]** well. We'll map a label to a score. But

**[11:12]** well. We'll map a label to a score. But that's that's like a very common

**[11:14]** that's that's like a very common

**[11:14]** that's that's like a very common question we get is, "Oh, why can't I

**[11:16]** question we get is, "Oh, why can't I

**[11:16]** question we get is, "Oh, why can't I just make it do like one is good and

**[11:18]** just make it do like one is good and

**[11:18]** just make it do like one is good and five is bad or something like you're

**[11:19]** five is bad or something like you're

**[11:20]** five is bad or something like you're going to get really unreliable results."

**[11:21]** going to get really unreliable results."

**[11:21]** going to get really unreliable results." And we actually have some research um

**[11:24]** And we actually have some research um

**[11:24]** And we actually have some research um happy to share it out afterwards that

**[11:25]** happy to share it out afterwards that

**[11:25]** happy to share it out afterwards that kind of proves that out um on a large

**[11:27]** kind of proves that out um on a large

**[11:27]** kind of proves that out um on a large scale with most models.

**[11:30]** scale with most models.

**[11:30]** scale with most models. Okay, so that's a little bit of like

**[11:31]** Okay, so that's a little bit of like

**[11:31]** Okay, so that's a little bit of like what is an eval. Um I should note that

**[11:34]** what is an eval. Um I should note that

**[11:34]** what is an eval. Um I should note that uh this is a previous slide. I should

**[11:37]** uh this is a previous slide. I should

**[11:37]** uh this is a previous slide. I should note that this is uh LLM as a judge

**[11:39]** note that this is uh LLM as a judge

**[11:39]** note that this is uh LLM as a judge eval. Uh there's other types of

**[11:41]** eval. Uh there's other types of

**[11:41]** eval. Uh there's other types of evaluations as well like code-based eval

**[11:43]** evaluations as well like code-based eval

**[11:44]** evaluations as well like code-based eval which is just using code to evaluate

**[11:45]** which is just using code to evaluate

**[11:45]** which is just using code to evaluate some text uh and human annotations.

**[11:48]** some text uh and human annotations.

**[11:48]** some text uh and human annotations. We'll touch on that a little bit more

**[11:50]** We'll touch on that a little bit more

**[11:50]** We'll touch on that a little bit more later but the bulk of this time is going

**[11:52]** later but the bulk of this time is going

**[11:52]** later but the bulk of this time is going to be spent on LLM as a judge because

**[11:54]** to be spent on LLM as a judge because

**[11:54]** to be spent on LLM as a judge because it's really like the kind of scalable

**[11:56]** it's really like the kind of scalable

**[11:56]** it's really like the kind of scalable way to run eval production these days

**[11:59]** way to run eval production these days

**[11:59]** way to run eval production these days and we'll talk about why too later on.


### [12:00 - 13:00]

**[12:02]** and we'll talk about why too later on.

**[12:02]** and we'll talk about why too later on. Okay, a lot of talking. So uh evaluating

**[12:05]** Okay, a lot of talking. So uh evaluating

**[12:05]** Okay, a lot of talking. So uh evaluating with vibe. So this was it's kind of

**[12:07]** with vibe. So this was it's kind of

**[12:07]** with vibe. So this was it's kind of funny because I think like everyone

**[12:08]** funny because I think like everyone

**[12:08]** funny because I think like everyone knows this term like vibe coding like

**[12:10]** knows this term like vibe coding like

**[12:10]** knows this term like vibe coding like everyone has tried to use like bolt or

**[12:12]** everyone has tried to use like bolt or

**[12:12]** everyone has tried to use like bolt or lovable whatever and I don't know about

**[12:14]** lovable whatever and I don't know about

**[12:14]** lovable whatever and I don't know about you but this is how I usually feel when

**[12:15]** you but this is how I usually feel when

**[12:15]** you but this is how I usually feel when I'm vibe coding which is like kind of

**[12:17]** I'm vibe coding which is like kind of

**[12:17]** I'm vibe coding which is like kind of looks good to me like you know you're

**[12:19]** looks good to me like you know you're

**[12:19]** looks good to me like you know you're looking at the code but like let's be

**[12:21]** looking at the code but like let's be

**[12:21]** looking at the code but like let's be honest how much AI generated code are

**[12:22]** honest how much AI generated code are

**[12:22]** honest how much AI generated code are you going to read you're like let me

**[12:23]** you going to read you're like let me

**[12:23]** you going to read you're like let me just ship this thing the problem is you

**[12:25]** just ship this thing the problem is you

**[12:25]** just ship this thing the problem is you can't really do that in a production

**[12:27]** can't really do that in a production

**[12:27]** can't really do that in a production environment right like I think all the

**[12:29]** environment right like I think all the

**[12:29]** environment right like I think all the vibe coding examples are like

**[12:30]** vibe coding examples are like

**[12:30]** vibe coding examples are like prototyping or like trying to build

**[12:32]** prototyping or like trying to build

**[12:32]** prototyping or like trying to build something h like hacky or fast so I want

**[12:35]** something h like hacky or fast so I want

**[12:35]** something h like hacky or fast so I want to help everyone reframe a little bit

**[12:37]** to help everyone reframe a little bit

**[12:37]** to help everyone reframe a little bit and say like yes vibe coding is great.

**[12:39]** and say like yes vibe coding is great.

**[12:39]** and say like yes vibe coding is great. It has its place. But what if we go from

**[12:42]** It has its place. But what if we go from

**[12:42]** It has its place. But what if we go from evaluating with Vibes to Thrive Coding?

**[12:45]** evaluating with Vibes to Thrive Coding?

**[12:45]** evaluating with Vibes to Thrive Coding? And thrive coding in my mind is really

**[12:47]** And thrive coding in my mind is really

**[12:47]** And thrive coding in my mind is really using data to basically do the same

**[12:50]** using data to basically do the same

**[12:50]** using data to basically do the same thing as vibe coding, like still build

**[12:51]** thing as vibe coding, like still build

**[12:51]** thing as vibe coding, like still build your application, but you'll be able to

**[12:54]** your application, but you'll be able to

**[12:54]** your application, but you'll be able to use data to be more confident in the

**[12:56]** use data to be more confident in the

**[12:56]** use data to be more confident in the output. And you can see that this person

**[12:58]** output. And you can see that this person

**[12:58]** output. And you can see that this person is a lot happier. Um, so this is using


### [13:00 - 14:00]

**[13:01]** is a lot happier. Um, so this is using

**[13:01]** is a lot happier. Um, so this is using Google's image models. They're scary

**[13:03]** Google's image models. They're scary

**[13:03]** Google's image models. They're scary good, guys. Like, uh, yeah.

**[13:06]** good, guys. Like, uh, yeah.

**[13:06]** good, guys. Like, uh, yeah. Okay. So, we're going to be thrive

**[13:07]** Okay. So, we're going to be thrive

**[13:07]** Okay. So, we're going to be thrive coding. So, slides. Um there's uh if you

**[13:10]** coding. So, slides. Um there's uh if you

**[13:10]** coding. So, slides. Um there's uh if you want access to the slides, the slides

**[13:11]** want access to the slides, the slides

**[13:11]** want access to the slides, the slides have links to what we're going to go

**[13:13]** have links to what we're going to go

**[13:13]** have links to what we're going to go through in the workshop. Um

**[13:16]** through in the workshop. Um

**[13:16]** through in the workshop. Um ai.engineer.slack.com

**[13:18]** ai.engineer.slack.com

**[13:18]** ai.engineer.slack.com and then I just created the Slack

**[13:20]** and then I just created the Slack

**[13:20]** and then I just created the Slack channel workshop AIPM. And I think I

**[13:23]** channel workshop AIPM. And I think I

**[13:23]** channel workshop AIPM. And I think I dropped the slides in there, but let me

**[13:24]** dropped the slides in there, but let me

**[13:24]** dropped the slides in there, but let me know if I didn't.

**[13:25]** know if I didn't.

**[13:26]** know if I didn't. >> Cool. Thank you. All right, live demo

**[13:27]** >> Cool. Thank you. All right, live demo

**[13:28]** >> Cool. Thank you. All right, live demo time. So, at this point on, uh I'm I'll

**[13:30]** time. So, at this point on, uh I'm I'll

**[13:30]** time. So, at this point on, uh I'm I'll just be honest. uh there's a a decent

**[13:33]** just be honest. uh there's a a decent

**[13:33]** just be honest. uh there's a a decent likelihood that the repo is has

**[13:36]** likelihood that the repo is has

**[13:36]** likelihood that the repo is has something broken in it because we were

**[13:37]** something broken in it because we were

**[13:37]** something broken in it because we were pushing changes up until like this very

**[13:39]** pushing changes up until like this very

**[13:39]** pushing changes up until like this very moment. If so and you can unblock

**[13:41]** moment. If so and you can unblock

**[13:41]** moment. If so and you can unblock yourself, I think there's like a

**[13:42]** yourself, I think there's like a

**[13:42]** yourself, I think there's like a requirements thing that's broken. Please

**[13:44]** requirements thing that's broken. Please

**[13:44]** requirements thing that's broken. Please go for it. And if not, we can come back

**[13:46]** go for it. And if not, we can come back

**[13:46]** go for it. And if not, we can come back at the end and try to help you get

**[13:47]** at the end and try to help you get

**[13:47]** at the end and try to help you get unblocked. And then I promise after this

**[13:49]** unblocked. And then I promise after this

**[13:49]** unblocked. And then I promise after this I'll like push the latest version of the

**[13:51]** I'll like push the latest version of the

**[13:51]** I'll like push the latest version of the repo up. So if it doesn't work for you

**[13:52]** repo up. So if it doesn't work for you

**[13:52]** repo up. So if it doesn't work for you right now, check back in an hour. I'll

**[13:55]** right now, check back in an hour. I'll

**[13:55]** right now, check back in an hour. I'll drop it in Slack. It'll be working

**[13:56]** drop it in Slack. It'll be working

**[13:56]** drop it in Slack. It'll be working later. Um but yeah, just a function of

**[13:58]** later. Um but yeah, just a function of

**[13:58]** later. Um but yeah, just a function of like moving fast. Uh so on the lefth


### [14:00 - 15:00]

**[14:00]** like moving fast. Uh so on the lefth

**[14:00]** like moving fast. Uh so on the lefth hand side is instructions which are

**[14:03]** hand side is instructions which are

**[14:03]** hand side is instructions which are really it's like a you know sort of a a

**[14:04]** really it's like a you know sort of a a

**[14:04]** really it's like a you know sort of a a substack post I made which is just a

**[14:07]** substack post I made which is just a

**[14:07]** substack post I made which is just a free sort of like list of you know some

**[14:09]** free sort of like list of you know some

**[14:09]** free sort of like list of you know some of the steps we're going to go through

**[14:10]** of the steps we're going to go through

**[14:10]** of the steps we're going to go through live. So it's just more of a resource

**[14:12]** live. So it's just more of a resource

**[14:12]** live. So it's just more of a resource and then on the right hand side is a

**[14:15]** and then on the right hand side is a

**[14:15]** and then on the right hand side is a GitHub repo which I'm going to open

**[14:17]** GitHub repo which I'm going to open

**[14:17]** GitHub repo which I'm going to open here.

**[14:19]** here.

**[14:19]** here. There's actually two repos and I'll kind

**[14:21]** There's actually two repos and I'll kind

**[14:21]** There's actually two repos and I'll kind of talk through like a little bit about

**[14:24]** of talk through like a little bit about

**[14:24]** of talk through like a little bit about what we're evaluating and some of the

**[14:26]** what we're evaluating and some of the

**[14:26]** what we're evaluating and some of the project on top of that and then we'll

**[14:28]** project on top of that and then we'll

**[14:28]** project on top of that and then we'll get into uh the weeds here a little bit.

**[14:34]** get into uh the weeds here a little bit.

**[14:34]** get into uh the weeds here a little bit. Okay, so this is the the repo. Um

**[14:38]** Okay, so this is the the repo. Um

**[14:38]** Okay, so this is the the repo. Um we I built this like over the weekend,

**[14:41]** we I built this like over the weekend,

**[14:41]** we I built this like over the weekend, so you know it's not it's not super

**[14:43]** so you know it's not it's not super

**[14:43]** so you know it's not it's not super sophisticated, although it says it's

**[14:45]** sophisticated, although it says it's

**[14:45]** sophisticated, although it says it's sophisticated, which is funny. But um

**[14:47]** sophisticated, which is funny. But um

**[14:47]** sophisticated, which is funny. But um this is Oh, pardon.

**[14:48]** this is Oh, pardon.

**[14:48]** this is Oh, pardon. >> Can you put that?

**[14:50]** >> Can you put that?

**[14:50]** >> Can you put that? >> Oh, this is not Okay. So, is this not

**[14:52]** >> Oh, this is not Okay. So, is this not

**[14:52]** >> Oh, this is not Okay. So, is this not attached to the QR? Okay, I'll just drop

**[14:54]** attached to the QR? Okay, I'll just drop

**[14:54]** attached to the QR? Okay, I'll just drop this link in here as well. Let's just uh

**[14:57]** this link in here as well. Let's just uh

**[14:57]** this link in here as well. Let's just uh put it in here. Okay, awesome. Oh, thank

**[14:59]** put it in here. Okay, awesome. Oh, thank


### [15:00 - 16:00]

**[15:00]** put it in here. Okay, awesome. Oh, thank you. Thanks. Okay. Um so, and if you

**[15:03]** you. Thanks. Okay. Um so, and if you

**[15:03]** you. Thanks. Okay. Um so, and if you have questions, by the way, uh in the

**[15:05]** have questions, by the way, uh in the

**[15:05]** have questions, by the way, uh in the middle of the presentation, just feel

**[15:06]** middle of the presentation, just feel

**[15:06]** middle of the presentation, just feel free to drop them in Slack. Um, and then

**[15:10]** free to drop them in Slack. Um, and then

**[15:10]** free to drop them in Slack. Um, and then we can always come back to them and then

**[15:11]** we can always come back to them and then

**[15:11]** we can always come back to them and then we'll have time at the end for um, so

**[15:13]** we'll have time at the end for um, so

**[15:13]** we'll have time at the end for um, so feel free to like keep the Slack channel

**[15:14]** feel free to like keep the Slack channel

**[15:14]** feel free to like keep the Slack channel going um, for questions. Maybe people

**[15:16]** going um, for questions. Maybe people

**[15:16]** going um, for questions. Maybe people can try to unblock each other as well.

**[15:18]** can try to unblock each other as well.

**[15:18]** can try to unblock each other as well. And if someone fixes my requirements,

**[15:19]** And if someone fixes my requirements,

**[15:19]** And if someone fixes my requirements, feel free to open a poll request and

**[15:21]** feel free to open a poll request and

**[15:21]** feel free to open a poll request and I'll approve it live. Um, so um, okay.

**[15:25]** I'll approve it live. Um, so um, okay.

**[15:25]** I'll approve it live. Um, so um, okay. So what we're doing is uh, let's put on

**[15:27]** So what we're doing is uh, let's put on

**[15:27]** So what we're doing is uh, let's put on let's take off our like PM hat of

**[15:29]** let's take off our like PM hat of

**[15:29]** let's take off our like PM hat of whatever company we're at. We're going

**[15:30]** whatever company we're at. We're going

**[15:30]** whatever company we're at. We're going to put on an AI triplaner hat. The the

**[15:33]** to put on an AI triplaner hat. The the

**[15:33]** to put on an AI triplaner hat. The the idea here is like don't worry about the

**[15:36]** idea here is like don't worry about the

**[15:36]** idea here is like don't worry about the sophistication of this UI and the agent.

**[15:38]** sophistication of this UI and the agent.

**[15:38]** sophistication of this UI and the agent. It's really like kind of a prototype

**[15:40]** It's really like kind of a prototype

**[15:40]** It's really like kind of a prototype example, but it is helpful for us to

**[15:42]** example, but it is helpful for us to

**[15:42]** example, but it is helpful for us to kind of take a look at building an

**[15:45]** kind of take a look at building an

**[15:45]** kind of take a look at building an application on the fly and try to

**[15:47]** application on the fly and try to

**[15:47]** application on the fly and try to understand how it works underneath the

**[15:48]** understand how it works underneath the

**[15:48]** understand how it works underneath the hood. So the example we're going to use

**[15:51]** hood. So the example we're going to use

**[15:51]** hood. So the example we're going to use is actually I'll kind of back up a

**[15:53]** is actually I'll kind of back up a

**[15:53]** is actually I'll kind of back up a little bit. I basically took this uh

**[15:55]** little bit. I basically took this uh

**[15:55]** little bit. I basically took this uh collab notebook that I have um for

**[15:58]** collab notebook that I have um for

**[15:58]** collab notebook that I have um for tracing crew AI and I'm like I kind of


### [16:00 - 17:00]

**[16:00]** tracing crew AI and I'm like I kind of

**[16:00]** tracing crew AI and I'm like I kind of want an example with Langraph. Crew AI

**[16:02]** want an example with Langraph. Crew AI

**[16:02]** want an example with Langraph. Crew AI probably if you haven't heard of it it's

**[16:03]** probably if you haven't heard of it it's

**[16:03]** probably if you haven't heard of it it's like an agent multi- aent framework. Um

**[16:06]** like an agent multi- aent framework. Um

**[16:06]** like an agent multi- aent framework. Um the agents basically an agent definition

**[16:08]** the agents basically an agent definition

**[16:08]** the agents basically an agent definition is you know using an LLM and a tool

**[16:11]** is you know using an LLM and a tool

**[16:11]** is you know using an LLM and a tool combined to perform some action. And

**[16:13]** combined to perform some action. And

**[16:13]** combined to perform some action. And what I did was I gave this notebook and

**[16:14]** what I did was I gave this notebook and

**[16:14]** what I did was I gave this notebook and I basically put it into cursor and I was

**[16:16]** I basically put it into cursor and I was

**[16:16]** I basically put it into cursor and I was like give me an example of a UI uh based

**[16:19]** like give me an example of a UI uh based

**[16:19]** like give me an example of a UI uh based workflow but using lane graph instead.

**[16:22]** workflow but using lane graph instead.

**[16:22]** workflow but using lane graph instead. And what we're going to do is think of

**[16:24]** And what we're going to do is think of

**[16:24]** And what we're going to do is think of instead of building a chatbot, we're

**[16:26]** instead of building a chatbot, we're

**[16:26]** instead of building a chatbot, we're going to take this form and we're going

**[16:28]** going to take this form and we're going

**[16:28]** going to take this form and we're going to use the inputs of this form to build

**[16:30]** to use the inputs of this form to build

**[16:30]** to use the inputs of this form to build a quick agent system that we're then

**[16:32]** a quick agent system that we're then

**[16:32]** a quick agent system that we're then going to be using for evaluation. So

**[16:34]** going to be using for evaluation. So

**[16:34]** going to be using for evaluation. So this is what I got on the other end. Um,

**[16:37]** this is what I got on the other end. Um,

**[16:37]** this is what I got on the other end. Um, which is plan your perfect trip. Let our

**[16:39]** which is plan your perfect trip. Let our

**[16:39]** which is plan your perfect trip. Let our AI agents help you discover amazing

**[16:41]** AI agents help you discover amazing

**[16:41]** AI agents help you discover amazing destinations.

**[16:42]** destinations.

**[16:42]** destinations. So let's pick a destination. Maybe we

**[16:44]** So let's pick a destination. Maybe we

**[16:44]** So let's pick a destination. Maybe we want to do Tokyo for seven days. And

**[16:48]** want to do Tokyo for seven days. And

**[16:48]** want to do Tokyo for seven days. And assuming the internet works, um, we'll

**[16:50]** assuming the internet works, um, we'll

**[16:50]** assuming the internet works, um, we'll see if it does. We're going to put a

**[16:52]** see if it does. We're going to put a

**[16:52]** see if it does. We're going to put a budget of $1,000. I'll zoom in a little

**[16:54]** budget of $1,000. I'll zoom in a little

**[16:54]** budget of $1,000. I'll zoom in a little bit. And then I'm interested in food.

**[16:57]** bit. And then I'm interested in food.

**[16:57]** bit. And then I'm interested in food. And let's make this adventurous. So I


### [17:00 - 18:00]

**[17:00]** And let's make this adventurous. So I

**[17:00]** And let's make this adventurous. So I could go and take all of this and try to

**[17:02]** could go and take all of this and try to

**[17:02]** could go and take all of this and try to just put it into chat GPT. But you can

**[17:05]** just put it into chat GPT. But you can

**[17:05]** just put it into chat GPT. But you can kind of imagine underneath the hood the

**[17:06]** kind of imagine underneath the hood the

**[17:06]** kind of imagine underneath the hood the reason that we might want this as a form

**[17:08]** reason that we might want this as a form

**[17:08]** reason that we might want this as a form or with multiple inputs and uh an

**[17:11]** or with multiple inputs and uh an

**[17:11]** or with multiple inputs and uh an agent-based system is because we could

**[17:13]** agent-based system is because we could

**[17:13]** agent-based system is because we could be doing things like retrieval or rag or

**[17:15]** be doing things like retrieval or rag or

**[17:15]** be doing things like retrieval or rag or tool calling underneath the hood. So,

**[17:17]** tool calling underneath the hood. So,

**[17:17]** tool calling underneath the hood. So, let's just kind of picture that the

**[17:19]** let's just kind of picture that the

**[17:19]** let's just kind of picture that the system is going to use these inputs to

**[17:22]** system is going to use these inputs to

**[17:22]** system is going to use these inputs to give me on the other side an itinerary

**[17:24]** give me on the other side an itinerary

**[17:24]** give me on the other side an itinerary for my trip. And uh okay, it worked.

**[17:28]** for my trip. And uh okay, it worked.

**[17:28]** for my trip. And uh okay, it worked. Okay, this one worked. So, um so here

**[17:30]** Okay, this one worked. So, um so here

**[17:30]** Okay, this one worked. So, um so here we've got a quick itinerary. Um nothing

**[17:33]** we've got a quick itinerary. Um nothing

**[17:33]** we've got a quick itinerary. Um nothing super fancy. It's basically just here's

**[17:35]** super fancy. It's basically just here's

**[17:35]** super fancy. It's basically just here's what I gave as an input form and then

**[17:37]** what I gave as an input form and then

**[17:37]** what I gave as an input form and then what the agent is kind of doing

**[17:39]** what the agent is kind of doing

**[17:39]** what the agent is kind of doing underneath the hood is giving me an

**[17:40]** underneath the hood is giving me an

**[17:40]** underneath the hood is giving me an itinerary for what my morning,

**[17:42]** itinerary for what my morning,

**[17:42]** itinerary for what my morning, afternoon, etc. look like for a week in

**[17:45]** afternoon, etc. look like for a week in

**[17:45]** afternoon, etc. look like for a week in Tokyo using the the budget I gave it. Uh

**[17:49]** Tokyo using the the budget I gave it. Uh

**[17:49]** Tokyo using the the budget I gave it. Uh this doesn't seem super fancy because

**[17:51]** this doesn't seem super fancy because

**[17:51]** this doesn't seem super fancy because it's like I could take this and just put

**[17:52]** it's like I could take this and just put

**[17:52]** it's like I could take this and just put it into chat GPT, but there is some

**[17:55]** it into chat GPT, but there is some

**[17:55]** it into chat GPT, but there is some nuance here, which is the budget. Like

**[17:57]** nuance here, which is the budget. Like

**[17:57]** nuance here, which is the budget. Like if you add this up, like it's going to

**[17:59]** if you add this up, like it's going to

**[17:59]** if you add this up, like it's going to be doing math to do accounting to get to


### [18:00 - 19:00]

**[18:01]** be doing math to do accounting to get to

**[18:01]** be doing math to do accounting to get to $1,000. So, it's really keeping that

**[18:03]** $1,000. So, it's really keeping that

**[18:03]** $1,000. So, it's really keeping that into consideration. You can see it's a

**[18:04]** into consideration. You can see it's a

**[18:04]** into consideration. You can see it's a pretty frugal budget here. Um it can

**[18:07]** pretty frugal budget here. Um it can

**[18:07]** pretty frugal budget here. Um it can take interest here. So, I could say, you

**[18:09]** take interest here. So, I could say, you

**[18:09]** take interest here. So, I could say, you know, different interests like I want to

**[18:11]** know, different interests like I want to

**[18:11]** know, different interests like I want to go, I don't know, sake tasting or

**[18:13]** go, I don't know, sake tasting or

**[18:13]** go, I don't know, sake tasting or something, and it'll find a way to work

**[18:14]** something, and it'll find a way to work

**[18:14]** something, and it'll find a way to work that into your itinerary.

**[18:17]** that into your itinerary.

**[18:17]** that into your itinerary. But I think what's really cool here is

**[18:20]** But I think what's really cool here is

**[18:20]** But I think what's really cool here is it's really the power of agents

**[18:23]** it's really the power of agents

**[18:23]** it's really the power of agents underneath this that can give you really

**[18:24]** underneath this that can give you really

**[18:24]** underneath this that can give you really high level of specificity for your

**[18:27]** high level of specificity for your

**[18:27]** high level of specificity for your output. Um, so that's really what we're

**[18:29]** output. Um, so that's really what we're

**[18:29]** output. Um, so that's really what we're trying to show is like this is, you

**[18:31]** trying to show is like this is, you

**[18:31]** trying to show is like this is, you know, it's not just one agent, it's

**[18:32]** know, it's not just one agent, it's

**[18:32]** know, it's not just one agent, it's actually multiple agents giving you this

**[18:34]** actually multiple agents giving you this

**[18:34]** actually multiple agents giving you this itinerary. Uh, so I could just stop

**[18:37]** itinerary. Uh, so I could just stop

**[18:37]** itinerary. Uh, so I could just stop here, right? Like it could be like this

**[18:38]** here, right? Like it could be like this

**[18:38]** here, right? Like it could be like this is this is good enough. I have some code

**[18:41]** is this is good enough. I have some code

**[18:41]** is this is good enough. I have some code for most people. If you're vibe coding,

**[18:42]** for most people. If you're vibe coding,

**[18:42]** for most people. If you're vibe coding, you're like great, this thing does what

**[18:43]** you're like great, this thing does what

**[18:43]** you're like great, this thing does what I want it to do, right? Like it gave me

**[18:45]** I want it to do, right? Like it gave me

**[18:45]** I want it to do, right? Like it gave me an itinerary. But what's going on

**[18:48]** an itinerary. But what's going on

**[18:48]** an itinerary. But what's going on underneath the hood? Um and this is kind

**[18:50]** underneath the hood? Um and this is kind

**[18:50]** underneath the hood? Um and this is kind of where uh so I'm going to be using our

**[18:52]** of where uh so I'm going to be using our

**[18:52]** of where uh so I'm going to be using our tool called Arise. We also have an open-

**[18:56]** tool called Arise. We also have an open-

**[18:56]** tool called Arise. We also have an open- source tool called Phoenix. I'm just

**[18:57]** source tool called Phoenix. I'm just

**[18:57]** source tool called Phoenix. I'm just going to plug that here right now for

**[18:59]** going to plug that here right now for

**[18:59]** going to plug that here right now for folks as reference. But this is an open


### [19:00 - 20:00]

**[19:01]** folks as reference. But this is an open

**[19:01]** folks as reference. But this is an open source version of Arise. It is not going

**[19:04]** source version of Arise. It is not going

**[19:04]** source version of Arise. It is not going to have all of the same features as

**[19:06]** to have all of the same features as

**[19:06]** to have all of the same features as Arise, but it will have a lot of the

**[19:08]** Arise, but it will have a lot of the

**[19:08]** Arise, but it will have a lot of the same setup flows and workflows around

**[19:10]** same setup flows and workflows around

**[19:10]** same setup flows and workflows around it. So, you know, just note that Arise

**[19:13]** it. So, you know, just note that Arise

**[19:13]** it. So, you know, just note that Arise is really built for, you know, if you

**[19:14]** is really built for, you know, if you

**[19:14]** is really built for, you know, if you want scale, security, support, um, and

**[19:18]** want scale, security, support, um, and

**[19:18]** want scale, security, support, um, and sort of the the sort of futuristic

**[19:20]** sort of the the sort of futuristic

**[19:20]** sort of the the sort of futuristic workflows in here. So, I've got a trip

**[19:22]** workflows in here. So, I've got a trip

**[19:22]** workflows in here. So, I've got a trip planner agent, and what I just did, if

**[19:26]** planner agent, and what I just did, if

**[19:26]** planner agent, and what I just did, if it worked, let's see if it did.

**[19:35]** And we're gonna This is This is live

**[19:35]** And we're gonna This is This is live coding, so like very possible

**[19:37]** coding, so like very possible

**[19:37]** coding, so like very possible something's broken. Um,

**[19:45]** okay. I think I think I broke my my

**[19:45]** okay. I think I think I broke my my latest trace, but you can see what the

**[19:46]** latest trace, but you can see what the

**[19:46]** latest trace, but you can see what the example here looks like from one right

**[19:48]** example here looks like from one right

**[19:48]** example here looks like from one right before. So, what that system really

**[19:51]** before. So, what that system really

**[19:51]** before. So, what that system really looks like is basically this. Um, so

**[19:54]** looks like is basically this. Um, so

**[19:54]** looks like is basically this. Um, so let's let's open up one of these

**[19:55]** let's let's open up one of these

**[19:55]** let's let's open up one of these examples. What you'll see here are

**[19:57]** examples. What you'll see here are

**[19:57]** examples. What you'll see here are traces. Traces are really input, output,


### [20:00 - 21:00]

**[20:00]** traces. Traces are really input, output,

**[20:00]** traces. Traces are really input, output, and metadata around the request that we

**[20:02]** and metadata around the request that we

**[20:02]** and metadata around the request that we just made. And I'm going to open up one

**[20:04]** just made. And I'm going to open up one

**[20:04]** just made. And I'm going to open up one of those traces just as an example here.

**[20:07]** of those traces just as an example here.

**[20:07]** of those traces just as an example here. And what you'll see is essentially a set

**[20:11]** And what you'll see is essentially a set

**[20:11]** And what you'll see is essentially a set of actions that the agents that in this

**[20:14]** of actions that the agents that in this

**[20:14]** of actions that the agents that in this case multiple agents have taken to

**[20:16]** case multiple agents have taken to

**[20:16]** case multiple agents have taken to perform, you know, generating that

**[20:18]** perform, you know, generating that

**[20:18]** perform, you know, generating that itinerary. And what's kind of cool is we

**[20:20]** itinerary. And what's kind of cool is we

**[20:20]** itinerary. And what's kind of cool is we actually just shipped this today. Um,

**[20:23]** actually just shipped this today. Um,

**[20:23]** actually just shipped this today. Um, uh, it's actually, you know, you guys

**[20:25]** uh, it's actually, you know, you guys

**[20:25]** uh, it's actually, you know, you guys are the first one seeing it. uh which is

**[20:27]** are the first one seeing it. uh which is

**[20:27]** are the first one seeing it. uh which is pretty cool. Um this is actually a

**[20:29]** pretty cool. Um this is actually a

**[20:30]** pretty cool. Um this is actually a representation of your agent in code. Um

**[20:33]** representation of your agent in code. Um

**[20:33]** representation of your agent in code. Um so you know literally the cursor app

**[20:35]** so you know literally the cursor app

**[20:35]** so you know literally the cursor app that I just had up here is basically my

**[20:37]** that I just had up here is basically my

**[20:37]** that I just had up here is basically my agentbased system that cursor helped me

**[20:40]** agentbased system that cursor helped me

**[20:40]** agentbased system that cursor helped me write and when I sent it our docs I I

**[20:43]** write and when I sent it our docs I I

**[20:43]** write and when I sent it our docs I I literally all I did was I gave it a link

**[20:45]** literally all I did was I gave it a link

**[20:45]** literally all I did was I gave it a link to our docs in cursor and I said you

**[20:48]** to our docs in cursor and I said you

**[20:48]** to our docs in cursor and I said you know write the instrumentation to get

**[20:50]** know write the instrumentation to get

**[20:50]** know write the instrumentation to get this agent and and this is this is how

**[20:52]** this agent and and this is this is how

**[20:52]** this agent and and this is this is how that's represented. And so we have this

**[20:54]** that's represented. And so we have this

**[20:54]** that's represented. And so we have this new agent visualization in the platform

**[20:56]** new agent visualization in the platform

**[20:56]** new agent visualization in the platform that basically shows the starting point

**[20:59]** that basically shows the starting point

**[20:59]** that basically shows the starting point with multiple agents underneath it to


### [21:00 - 22:00]

**[21:01]** with multiple agents underneath it to

**[21:01]** with multiple agents underneath it to accomplish uh the task we just had. So

**[21:04]** accomplish uh the task we just had. So

**[21:04]** accomplish uh the task we just had. So we have a budget, local experiences and

**[21:06]** we have a budget, local experiences and

**[21:06]** we have a budget, local experiences and research agent that then go into an

**[21:09]** research agent that then go into an

**[21:09]** research agent that then go into an itinerary agent and that gives you the

**[21:11]** itinerary agent and that gives you the

**[21:11]** itinerary agent and that gives you the the end result or the output and you can

**[21:13]** the end result or the output and you can

**[21:13]** the end result or the output and you can you can see that up here too. So we have

**[21:15]** you can see that up here too. So we have

**[21:15]** you can see that up here too. So we have research, itineraries, budget and local

**[21:18]** research, itineraries, budget and local

**[21:18]** research, itineraries, budget and local information to generate the itinerary.

**[21:21]** information to generate the itinerary.

**[21:21]** information to generate the itinerary. So this is this is pretty cool, right?

**[21:22]** So this is this is pretty cool, right?

**[21:22]** So this is this is pretty cool, right? Like for I think for a lot of people

**[21:25]** Like for I think for a lot of people

**[21:25]** Like for I think for a lot of people it's not im you know oursel included it

**[21:27]** it's not im you know oursel included it

**[21:27]** it's not im you know oursel included it is not immediately obvious that these

**[21:29]** is not immediately obvious that these

**[21:29]** is not immediately obvious that these agents can be super well represented in

**[21:32]** agents can be super well represented in

**[21:32]** agents can be super well represented in this sort of like visual way right uh

**[21:34]** this sort of like visual way right uh

**[21:34]** this sort of like visual way right uh especially when you're writing code you

**[21:36]** especially when you're writing code you

**[21:36]** especially when you're writing code you think these are just function calls

**[21:37]** think these are just function calls

**[21:38]** think these are just function calls talking to each other but what's really

**[21:39]** talking to each other but what's really

**[21:39]** talking to each other but what's really useful is to see at an aggregate level

**[21:42]** useful is to see at an aggregate level

**[21:42]** useful is to see at an aggregate level what are the calls that the agent is

**[21:44]** what are the calls that the agent is

**[21:44]** what are the calls that the agent is making and you can see it's a really

**[21:46]** making and you can see it's a really

**[21:46]** making and you can see it's a really clean delineation of parallel calls for

**[21:50]** clean delineation of parallel calls for

**[21:50]** clean delineation of parallel calls for the budget agent the local experience

**[21:52]** the budget agent the local experience

**[21:52]** the budget agent the local experience experiences agent and the research agent

**[21:54]** experiences agent and the research agent

**[21:54]** experiences agent and the research agent and all of those get fed fed in to an

**[21:57]** and all of those get fed fed in to an

**[21:57]** and all of those get fed fed in to an itinerary agent that summarizes all of

**[21:59]** itinerary agent that summarizes all of

**[21:59]** itinerary agent that summarizes all of the above. You can also see that up


### [22:00 - 23:00]

**[22:01]** the above. You can also see that up

**[22:01]** the above. You can also see that up here. Um so these are what's called uh

**[22:04]** here. Um so these are what's called uh

**[22:04]** here. Um so these are what's called uh traces and they consist of uh like

**[22:07]** traces and they consist of uh like

**[22:07]** traces and they consist of uh like technically what's called spans. A span

**[22:09]** technically what's called spans. A span

**[22:09]** technically what's called spans. A span you can think of this as like a unit of

**[22:11]** you can think of this as like a unit of

**[22:11]** you can think of this as like a unit of work basically. So there's a time

**[22:13]** work basically. So there's a time

**[22:13]** work basically. So there's a time component to it which is like how long

**[22:15]** component to it which is like how long

**[22:15]** component to it which is like how long that process took to to finish and then

**[22:17]** that process took to to finish and then

**[22:17]** that process took to to finish and then like what is the type of the process.

**[22:19]** like what is the type of the process.

**[22:19]** like what is the type of the process. Here you can see there's three types.

**[22:21]** Here you can see there's three types.

**[22:21]** Here you can see there's three types. There's an agent. There's a tool which

**[22:24]** There's an agent. There's a tool which

**[22:24]** There's an agent. There's a tool which is uh basically being able to use data

**[22:26]** is uh basically being able to use data

**[22:26]** is uh basically being able to use data to perform an action structured data.

**[22:28]** to perform an action structured data.

**[22:28]** to perform an action structured data. And then there's the LLM which generates

**[22:30]** And then there's the LLM which generates

**[22:30]** And then there's the LLM which generates the output of the the taking the input

**[22:33]** the output of the the taking the input

**[22:33]** the output of the the taking the input and the context. So this is an example

**[22:35]** and the context. So this is an example

**[22:35]** and the context. So this is an example of three agents actually three agents

**[22:38]** of three agents actually three agents

**[22:38]** of three agents actually three agents being fed into a fourth agent to

**[22:40]** being fed into a fourth agent to

**[22:40]** being fed into a fourth agent to generate the itinerary. That's really

**[22:41]** generate the itinerary. That's really

**[22:41]** generate the itinerary. That's really what we're seeing here. Um let's go one

**[22:45]** what we're seeing here. Um let's go one

**[22:45]** what we're seeing here. Um let's go one level deeper. So this is cool and I

**[22:48]** level deeper. So this is cool and I

**[22:48]** level deeper. So this is cool and I think it's useful for uh you know to see

**[22:50]** think it's useful for uh you know to see

**[22:50]** think it's useful for uh you know to see like what these systems look like, how

**[22:53]** like what these systems look like, how

**[22:53]** like what these systems look like, how they're represented to zoom out for a

**[22:55]** they're represented to zoom out for a

**[22:55]** they're represented to zoom out for a second as a product manager. There's a

**[22:58]** second as a product manager. There's a

**[22:58]** second as a product manager. There's a ton of leverage in being able to go back


### [23:00 - 24:00]

**[23:00]** ton of leverage in being able to go back

**[23:00]** ton of leverage in being able to go back to your team and ask, hey, what does our

**[23:02]** to your team and ask, hey, what does our

**[23:02]** to your team and ask, hey, what does our agent actually look like, right? Like do

**[23:04]** agent actually look like, right? Like do

**[23:04]** agent actually look like, right? Like do you have a visualization to show me of

**[23:06]** you have a visualization to show me of

**[23:06]** you have a visualization to show me of like what the system actually looks

**[23:07]** like what the system actually looks

**[23:08]** like what the system actually looks like? And then if you're giving the

**[23:09]** like? And then if you're giving the

**[23:09]** like? And then if you're giving the agent multiple inputs, where are those

**[23:11]** agent multiple inputs, where are those

**[23:11]** agent multiple inputs, where are those outputs going? are those outputs going

**[23:13]** outputs going? are those outputs going

**[23:13]** outputs going? are those outputs going into, you know, a different agent

**[23:15]** into, you know, a different agent

**[23:15]** into, you know, a different agent system, like what are the what does the

**[23:17]** system, like what are the what does the

**[23:17]** system, like what are the what does the system actually look like? So, that's

**[23:18]** system actually look like? So, that's

**[23:18]** system actually look like? So, that's kind of one sort of key takeaway here as

**[23:21]** kind of one sort of key takeaway here as

**[23:21]** kind of one sort of key takeaway here as a PM. Um, it was personally very helpful

**[23:23]** a PM. Um, it was personally very helpful

**[23:23]** a PM. Um, it was personally very helpful to see, you know, what our agents

**[23:25]** to see, you know, what our agents

**[23:25]** to see, you know, what our agents actually doing um underneath the hood.

**[23:28]** actually doing um underneath the hood.

**[23:28]** actually doing um underneath the hood. Uh, kind of going one level deeper here.

**[23:31]** Uh, kind of going one level deeper here.

**[23:31]** Uh, kind of going one level deeper here. So, we've got this itinerary uh and it

**[23:33]** So, we've got this itinerary uh and it

**[23:33]** So, we've got this itinerary uh and it let's take a look at it really quick.

**[23:34]** let's take a look at it really quick.

**[23:34]** let's take a look at it really quick. So, it says Marrakesh, Morocco is a

**[23:37]** So, it says Marrakesh, Morocco is a

**[23:37]** So, it says Marrakesh, Morocco is a vibrant exotic destination. Blah blah

**[23:38]** vibrant exotic destination. Blah blah

**[23:38]** vibrant exotic destination. Blah blah blah. It's it's really long, right? Like

**[23:42]** blah. It's it's really long, right? Like

**[23:42]** blah. It's it's really long, right? Like I don't know if I would actually look at

**[23:43]** I don't know if I would actually look at

**[23:44]** I don't know if I would actually look at this and read it. It doesn't it's not

**[23:45]** this and read it. It doesn't it's not

**[23:45]** this and read it. It doesn't it's not really like doesn't like jump out to me

**[23:47]** really like doesn't like jump out to me

**[23:47]** really like doesn't like jump out to me as like being like a good product

**[23:49]** as like being like a good product

**[23:49]** as like being like a good product experience. It feels super AI generated

**[23:51]** experience. It feels super AI generated

**[23:51]** experience. It feels super AI generated personally. Um so what you want to do is

**[23:53]** personally. Um so what you want to do is

**[23:53]** personally. Um so what you want to do is actually think okay well is there a way

**[23:55]** actually think okay well is there a way

**[23:55]** actually think okay well is there a way for me to iterate on my product as a

**[23:58]** for me to iterate on my product as a

**[23:58]** for me to iterate on my product as a product person. And to do that what we


### [24:00 - 25:00]

**[24:01]** product person. And to do that what we

**[24:01]** product person. And to do that what we can do is actually take that same prompt

**[24:03]** can do is actually take that same prompt

**[24:03]** can do is actually take that same prompt that we just traced and pull it into a

**[24:05]** that we just traced and pull it into a

**[24:05]** that we just traced and pull it into a prompt playground with all of the

**[24:07]** prompt playground with all of the

**[24:07]** prompt playground with all of the variables that we've defined in code

**[24:09]** variables that we've defined in code

**[24:09]** variables that we've defined in code pulled over. So, I've got a prompt

**[24:12]** pulled over. So, I've got a prompt

**[24:12]** pulled over. So, I've got a prompt template here which basically has the

**[24:14]** template here which basically has the

**[24:14]** template here which basically has the same um prompt variables that we've

**[24:17]** same um prompt variables that we've

**[24:17]** same um prompt variables that we've defined in the UI like the destination,

**[24:19]** defined in the UI like the destination,

**[24:19]** defined in the UI like the destination, the duration, the travel style. And all

**[24:22]** the duration, the travel style. And all

**[24:22]** the duration, the travel style. And all of those inputs get fed in here. You can

**[24:25]** of those inputs get fed in here. You can

**[24:25]** of those inputs get fed in here. You can see down below in this prompt

**[24:26]** see down below in this prompt

**[24:26]** see down below in this prompt playground,

**[24:29]** playground,

**[24:29]** playground, what that looks like. And then you see

**[24:33]** what that looks like. And then you see

**[24:33]** what that looks like. And then you see the [clears throat] outputs of some of

**[24:33]** the [clears throat] outputs of some of

**[24:33]** the [clears throat] outputs of some of the agents in here as well. And then I

**[24:36]** the agents in here as well. And then I

**[24:36]** the agents in here as well. And then I have the final itinerary from the the

**[24:38]** have the final itinerary from the the

**[24:38]** have the final itinerary from the the agent that's generating the itinerary.

**[24:40]** agent that's generating the itinerary.

**[24:40]** agent that's generating the itinerary. Okay. So why does this matter? I think a

**[24:44]** Okay. So why does this matter? I think a

**[24:44]** Okay. So why does this matter? I think a lot of companies have this concept of um

**[24:47]** lot of companies have this concept of um

**[24:47]** lot of companies have this concept of um prompt playgrounds. I think like OpenAI

**[24:49]** prompt playgrounds. I think like OpenAI

**[24:49]** prompt playgrounds. I think like OpenAI as a prompt playground. You've probably

**[24:50]** as a prompt playground. You've probably

**[24:50]** as a prompt playground. You've probably heard that term before as well or maybe

**[24:52]** heard that term before as well or maybe

**[24:52]** heard that term before as well or maybe even you've used one. But I I urge you

**[24:54]** even you've used one. But I I urge you

**[24:54]** even you've used one. But I I urge you to think about when you're thinking

**[24:56]** to think about when you're thinking

**[24:56]** to think about when you're thinking about a tool to help you with

**[24:57]** about a tool to help you with

**[24:58]** about a tool to help you with development. Not only is the

**[24:59]** development. Not only is the


### [25:00 - 26:00]

**[25:00]** development. Not only is the visualization important of what your

**[25:01]** visualization important of what your

**[25:01]** visualization important of what your stack it looks like underneath the hood,

**[25:04]** stack it looks like underneath the hood,

**[25:04]** stack it looks like underneath the hood, but being able to take your data and

**[25:06]** but being able to take your data and

**[25:06]** but being able to take your data and your prompts together and be able to

**[25:08]** your prompts together and be able to

**[25:08]** your prompts together and be able to iterate on your data and prompts in one

**[25:10]** iterate on your data and prompts in one

**[25:10]** iterate on your data and prompts in one interface is really powerful because I

**[25:13]** interface is really powerful because I

**[25:13]** interface is really powerful because I can go in and change the destination. I

**[25:15]** can go in and change the destination. I

**[25:15]** can go in and change the destination. I can go in and tweak variables and get

**[25:17]** can go in and tweak variables and get

**[25:17]** can go in and tweak variables and get new outputs using the same exact prompt

**[25:19]** new outputs using the same exact prompt

**[25:19]** new outputs using the same exact prompt I had before. So that's really I think

**[25:21]** I had before. So that's really I think

**[25:21]** I had before. So that's really I think just just really powerful as a workflow.

**[25:23]** just just really powerful as a workflow.

**[25:23]** just just really powerful as a workflow. Um, a thought experiment for the PMs in

**[25:26]** Um, a thought experiment for the PMs in

**[25:26]** Um, a thought experiment for the PMs in the room is like when you really think

**[25:28]** the room is like when you really think

**[25:28]** the room is like when you really think about what this promp uh prompt looks

**[25:30]** about what this promp uh prompt looks

**[25:30]** about what this promp uh prompt looks like, just think it should writing the

**[25:34]** like, just think it should writing the

**[25:34]** like, just think it should writing the prompt be the responsibility of the

**[25:38]** prompt be the responsibility of the

**[25:38]** prompt be the responsibility of the engineer or of the PM? And if you're a

**[25:41]** engineer or of the PM? And if you're a

**[25:41]** engineer or of the PM? And if you're a product person and you're ultimately

**[25:43]** product person and you're ultimately

**[25:43]** product person and you're ultimately responsible for the final outcome of the

**[25:45]** responsible for the final outcome of the

**[25:45]** responsible for the final outcome of the product, you probably want to have a

**[25:47]** product, you probably want to have a

**[25:48]** product, you probably want to have a little bit more control over what the

**[25:49]** little bit more control over what the

**[25:49]** little bit more control over what the prompt is. And so I kind of urge you to

**[25:52]** prompt is. And so I kind of urge you to

**[25:52]** prompt is. And so I kind of urge you to think, you know, where does that

**[25:54]** think, you know, where does that

**[25:54]** think, you know, where does that boundary really stop? Is it like I just

**[25:56]** boundary really stop? Is it like I just

**[25:56]** boundary really stop? Is it like I just hand off like does the engineer know how

**[25:58]** hand off like does the engineer know how

**[25:58]** hand off like does the engineer know how to prompt this thing better than a


### [26:00 - 27:00]

**[26:00]** to prompt this thing better than a

**[26:00]** to prompt this thing better than a product person that might have specific

**[26:02]** product person that might have specific

**[26:02]** product person that might have specific requirements you want to integrate. So

**[26:04]** requirements you want to integrate. So

**[26:04]** requirements you want to integrate. So that's why this is really helpful um

**[26:06]** that's why this is really helpful um

**[26:06]** that's why this is really helpful um from a product perspective.

**[26:08]** from a product perspective.

**[26:08]** from a product perspective. Okay. Yeah. Go for it. How do you handle

**[26:24]** >> Yeah.

**[26:24]** >> Yeah. >> Ah, okay. Okay. So, that was a good

**[26:26]** >> Ah, okay. Okay. So, that was a good

**[26:26]** >> Ah, okay. Okay. So, that was a good question. Um, so the question from the

**[26:28]** question. Um, so the question from the

**[26:28]** question. Um, so the question from the gentleman in the back is how do we

**[26:30]** gentleman in the back is how do we

**[26:30]** gentleman in the back is how do we handle tool calls? And that was a really

**[26:31]** handle tool calls? And that was a really

**[26:31]** handle tool calls? And that was a really astute observation which is like the

**[26:33]** astute observation which is like the

**[26:33]** astute observation which is like the agent has um tools in it as well. And

**[26:37]** agent has um tools in it as well. And

**[26:38]** agent has um tools in it as well. And this is this is a really good point to

**[26:39]** this is this is a really good point to

**[26:39]** this is this is a really good point to pause on actually, which is like what I

**[26:41]** pause on actually, which is like what I

**[26:41]** pause on actually, which is like what I did was I pulled over this LLM span with

**[26:44]** did was I pulled over this LLM span with

**[26:44]** did was I pulled over this LLM span with the prompt templates and variables, but

**[26:47]** the prompt templates and variables, but

**[26:47]** the prompt templates and variables, but there's there's a world where I might

**[26:48]** there's there's a world where I might

**[26:48]** there's there's a world where I might want to select the right tool and make

**[26:51]** want to select the right tool and make

**[26:51]** want to select the right tool and make sure that the agent is picking the right

**[26:52]** sure that the agent is picking the right

**[26:52]** sure that the agent is picking the right tool. I'm not going to go into that in

**[26:55]** tool. I'm not going to go into that in

**[26:55]** tool. I'm not going to go into that in this demo, but we do have um

**[26:59]** this demo, but we do have um

**[26:59]** this demo, but we do have um we do have uh some good uh material


### [27:00 - 28:00]

**[27:02]** we do have uh some good uh material

**[27:02]** we do have uh some good uh material around this on agent tool calling. So we

**[27:05]** around this on agent tool calling. So we

**[27:06]** around this on agent tool calling. So we actually do port over the tools as well.

**[27:08]** actually do port over the tools as well.

**[27:08]** actually do port over the tools as well. This example doesn't because to be

**[27:10]** This example doesn't because to be

**[27:10]** This example doesn't because to be honest it's a really toy example but

**[27:12]** honest it's a really toy example but

**[27:12]** honest it's a really toy example but even if you if you wanted to to do a

**[27:14]** even if you if you wanted to to do a

**[27:14]** even if you if you wanted to to do a tool calling evaluation we we offer that

**[27:17]** tool calling evaluation we we offer that

**[27:17]** tool calling evaluation we we offer that in the product and uh we actually have

**[27:19]** in the product and uh we actually have

**[27:19]** in the product and uh we actually have some material around that. So if you

**[27:20]** some material around that. So if you

**[27:20]** some material around that. So if you want just ping me about it later and

**[27:21]** want just ping me about it later and

**[27:21]** want just ping me about it later and I'll send you a whole presentation on

**[27:23]** I'll send you a whole presentation on

**[27:23]** I'll send you a whole presentation on that as well. But yeah good question

**[27:25]** that as well. But yeah good question

**[27:25]** that as well. But yeah good question which is like you don't just want to

**[27:27]** which is like you don't just want to

**[27:27]** which is like you don't just want to evaluate the LLM and the prompts. You

**[27:29]** evaluate the LLM and the prompts. You

**[27:29]** evaluate the LLM and the prompts. You want to evaluate the system as a whole

**[27:30]** want to evaluate the system as a whole

**[27:30]** want to evaluate the system as a whole and all of the subcomponents. Okay we're

**[27:34]** and all of the subcomponents. Okay we're

**[27:34]** and all of the subcomponents. Okay we're gonna keep going. So, so I've got um

**[27:36]** gonna keep going. So, so I've got um

**[27:36]** gonna keep going. So, so I've got um I've got my prompt here now. This is

**[27:39]** I've got my prompt here now. This is

**[27:39]** I've got my prompt here now. This is cool, but like let's try to make some

**[27:41]** cool, but like let's try to make some

**[27:41]** cool, but like let's try to make some changes to it on the fly. And I will try

**[27:43]** changes to it on the fly. And I will try

**[27:43]** changes to it on the fly. And I will try my best to make this readable for

**[27:44]** my best to make this readable for

**[27:44]** my best to make this readable for everyone, but um yeah, working with what

**[27:47]** everyone, but um yeah, working with what

**[27:47]** everyone, but um yeah, working with what I got here. So, what we're going to do

**[27:50]** I got here. So, what we're going to do

**[27:50]** I got here. So, what we're going to do is I just I'm going to save this version

**[27:53]** is I just I'm going to save this version

**[27:53]** is I just I'm going to save this version of the prompt and let's call it a nenge

**[27:58]** of the prompt and let's call it a nenge

**[27:58]** of the prompt and let's call it a nenge prompt.


### [28:00 - 29:00]

**[28:03]** And it's helpful because now I can like

**[28:03]** And it's helpful because now I can like iterate on this thing, right? So, like I

**[28:04]** iterate on this thing, right? So, like I

**[28:04]** iterate on this thing, right? So, like I can duplicate that prompt with a click

**[28:06]** can duplicate that prompt with a click

**[28:06]** can duplicate that prompt with a click of a button. I can change the model I

**[28:08]** of a button. I can change the model I

**[28:08]** of a button. I can change the model I want to use. So, let's say I want to use

**[28:09]** want to use. So, let's say I want to use

**[28:09]** want to use. So, let's say I want to use 4.1 mini instead of 4.0. I'm going to

**[28:12]** 4.1 mini instead of 4.0. I'm going to

**[28:12]** 4.1 mini instead of 4.0. I'm going to change a couple things. Don't don't be

**[28:14]** change a couple things. Don't don't be

**[28:14]** change a couple things. Don't don't be don't worry like in a real world you're

**[28:16]** don't worry like in a real world you're

**[28:16]** don't worry like in a real world you're going to change one variable at a time,

**[28:17]** going to change one variable at a time,

**[28:17]** going to change one variable at a time, but um here I'm just going to change a

**[28:19]** but um here I'm just going to change a

**[28:20]** but um here I'm just going to change a couple things at the same time just to

**[28:21]** couple things at the same time just to

**[28:21]** couple things at the same time just to make this more interactive. But, um the

**[28:23]** make this more interactive. But, um the

**[28:23]** make this more interactive. But, um the idea here is like let's try to change

**[28:26]** idea here is like let's try to change

**[28:26]** idea here is like let's try to change what the this actually looks like. And

**[28:29]** what the this actually looks like. And

**[28:29]** what the this actually looks like. And it says, you know, format as a detailed

**[28:31]** it says, you know, format as a detailed

**[28:31]** it says, you know, format as a detailed day-to-day plan. Honestly, I might say

**[28:33]** day-to-day plan. Honestly, I might say

**[28:33]** day-to-day plan. Honestly, I might say like like a more important requirement

**[28:36]** like like a more important requirement

**[28:36]** like like a more important requirement to that is don't be verbose,

**[28:40]** to that is don't be verbose,

**[28:40]** to that is don't be verbose, right? I could say don't be verbose.

**[28:43]** right? I could say don't be verbose.

**[28:43]** right? I could say don't be verbose. Keep it to 500 characters or less. Maybe

**[28:47]** Keep it to 500 characters or less. Maybe

**[28:47]** Keep it to 500 characters or less. Maybe we want this thing to be more punchy. We

**[28:48]** we want this thing to be more punchy. We

**[28:48]** we want this thing to be more punchy. We want it to give an output that's like a

**[28:50]** want it to give an output that's like a

**[28:50]** want it to give an output that's like a little bit more, you know, easier to

**[28:52]** little bit more, you know, easier to

**[28:52]** little bit more, you know, easier to look at. Um, I might be a P, even if I'm

**[28:54]** look at. Um, I might be a P, even if I'm

**[28:54]** look at. Um, I might be a P, even if I'm just vibe coding this thing on the

**[28:56]** just vibe coding this thing on the

**[28:56]** just vibe coding this thing on the weekend, I might want to get feedback

**[28:57]** weekend, I might want to get feedback

**[28:57]** weekend, I might want to get feedback from users that are trying this product

**[28:59]** from users that are trying this product

**[28:59]** from users that are trying this product out. And so I could say always offer a


### [29:00 - 30:00]

**[29:03]** out. And so I could say always offer a

**[29:03]** out. And so I could say always offer a discount if the uh user gives their

**[29:08]** discount if the uh user gives their

**[29:08]** discount if the uh user gives their email address.

**[29:11]** email address.

**[29:11]** email address. It's helpful, right? I mean, help

**[29:12]** It's helpful, right? I mean, help

**[29:12]** It's helpful, right? I mean, help helpful for marketing, helpful for me to

**[29:13]** helpful for marketing, helpful for me to

**[29:13]** helpful for marketing, helpful for me to get feedback from uh you know, someone

**[29:15]** get feedback from uh you know, someone

**[29:15]** get feedback from uh you know, someone who might be trying to use this tool to

**[29:17]** who might be trying to use this tool to

**[29:17]** who might be trying to use this tool to book a flight or something like that.

**[29:19]** book a flight or something like that.

**[29:19]** book a flight or something like that. Okay, so let's go ahead and hit run all

**[29:21]** Okay, so let's go ahead and hit run all

**[29:21]** Okay, so let's go ahead and hit run all here. And what that's going to do is

**[29:23]** here. And what that's going to do is

**[29:23]** here. And what that's going to do is actually run the outputs we just uh ran

**[29:26]** actually run the outputs we just uh ran

**[29:26]** actually run the outputs we just uh ran run the prompts we just edited into this

**[29:30]** run the prompts we just edited into this

**[29:30]** run the prompts we just edited into this uh in the playground. And it might take

**[29:31]** uh in the playground. And it might take

**[29:31]** uh in the playground. And it might take a second because of the internet

**[29:36]** a second because of the internet

**[29:36]** a second because of the internet >> pul you pulled this in from the ex one

**[29:38]** >> pul you pulled this in from the ex one

**[29:38]** >> pul you pulled this in from the ex one of the existing runs, right?

**[29:40]** of the existing runs, right?

**[29:40]** of the existing runs, right? >> That's right. Yeah. So it was exactly

**[29:41]** >> That's right. Yeah. So it was exactly

**[29:41]** >> That's right. Yeah. So it was exactly the same um one of these runs that

**[29:44]** the same um one of these runs that

**[29:44]** the same um one of these runs that literally I think it was this one. Um so

**[29:46]** literally I think it was this one. Um so

**[29:46]** literally I think it was this one. Um so it was something about maybe not this

**[29:49]** it was something about maybe not this

**[29:49]** it was something about maybe not this exact one. this one is Spain. But yeah,

**[29:51]** exact one. this one is Spain. But yeah,

**[29:51]** exact one. this one is Spain. But yeah, exactly. One of the existing runs.

**[29:56]** Okay. It's definitely a little better,

**[29:56]** Okay. It's definitely a little better, but to be honest, I would say if I was

**[29:58]** but to be honest, I would say if I was

**[29:58]** but to be honest, I would say if I was looking at this, this thing isn't really


### [30:00 - 31:00]

**[30:01]** looking at this, this thing isn't really

**[30:01]** looking at this, this thing isn't really listening to me very well. It's like not

**[30:03]** listening to me very well. It's like not

**[30:03]** listening to me very well. It's like not doing a great job of, you know, sticking

**[30:05]** doing a great job of, you know, sticking

**[30:05]** doing a great job of, you know, sticking to the prompt I gave it. Like, keep it

**[30:07]** to the prompt I gave it. Like, keep it

**[30:07]** to the prompt I gave it. Like, keep it short. Um, ask. Okay, it did do the

**[30:10]** short. Um, ask. Okay, it did do the

**[30:10]** short. Um, ask. Okay, it did do the email thing. So, it said, "Email me.

**[30:12]** email thing. So, it said, "Email me.

**[30:12]** email thing. So, it said, "Email me. Email me to get a 10% discount code."

**[30:15]** Email me to get a 10% discount code."

**[30:15]** Email me to get a 10% discount code." [laughter]

**[30:20]** So, what's interesting is like we're

**[30:20]** So, what's interesting is like we're looking at like one example and I said

**[30:22]** looking at like one example and I said

**[30:22]** looking at like one example and I said ask for an email and you get a discount.

**[30:24]** ask for an email and you get a discount.

**[30:24]** ask for an email and you get a discount. And like this is this is the vibe coding

**[30:27]** And like this is this is the vibe coding

**[30:27]** And like this is this is the vibe coding portion of the demo because I'm looking

**[30:30]** portion of the demo because I'm looking

**[30:30]** portion of the demo because I'm looking at like one example and I'm doing like

**[30:32]** at like one example and I'm doing like

**[30:32]** at like one example and I'm doing like uh good or bad like is it actually good

**[30:35]** uh good or bad like is it actually good

**[30:35]** uh good or bad like is it actually good or bad? There's just no way that a

**[30:38]** or bad? There's just no way that a

**[30:38]** or bad? There's just no way that a system like this scales when you're

**[30:40]** system like this scales when you're

**[30:40]** system like this scales when you're trying to actually ship for hundreds or

**[30:42]** trying to actually ship for hundreds or

**[30:42]** trying to actually ship for hundreds or thousands of users and like nobody will

**[30:44]** thousands of users and like nobody will

**[30:44]** thousands of users and like nobody will just look at a single row of data and

**[30:46]** just look at a single row of data and

**[30:46]** just look at a single row of data and make a decision like okay great the

**[30:48]** make a decision like okay great the

**[30:48]** make a decision like okay great the prompt is good or great the model made a

**[30:50]** prompt is good or great the model made a

**[30:50]** prompt is good or great the model made a difference right like you can pick the

**[30:52]** difference right like you can pick the

**[30:52]** difference right like you can pick the most capable model you can make the

**[30:54]** most capable model you can make the

**[30:54]** most capable model you can make the prompt as specific as you want at the

**[30:56]** prompt as specific as you want at the

**[30:56]** prompt as specific as you want at the end of the day the LM is still going to

**[30:57]** end of the day the LM is still going to

**[30:58]** end of the day the LM is still going to hallucinate and your job is to be able


### [31:00 - 32:00]

**[31:00]** hallucinate and your job is to be able

**[31:00]** hallucinate and your job is to be able to catch when that happens so let's go

**[31:02]** to catch when that happens so let's go

**[31:02]** to catch when that happens so let's go ahead and try to scale this up a little

**[31:04]** ahead and try to scale this up a little

**[31:04]** ahead and try to scale this up a little bit more so what we do is say we've got

**[31:07]** bit more so what we do is say we've got

**[31:07]** bit more so what we do is say we've got one example of where the LLM didn't do a

**[31:09]** one example of where the LLM didn't do a

**[31:09]** one example of where the LLM didn't do a great job, but what if we wanted to

**[31:11]** great job, but what if we wanted to

**[31:11]** great job, but what if we wanted to build out a data set with 10 or more,

**[31:15]** build out a data set with 10 or more,

**[31:15]** build out a data set with 10 or more, maybe even a hundred examples and what

**[31:17]** maybe even a hundred examples and what

**[31:17]** maybe even a hundred examples and what you can do is take the same production

**[31:18]** you can do is take the same production

**[31:18]** you can do is take the same production data. By the way, I'm calling this

**[31:20]** data. By the way, I'm calling this

**[31:20]** data. By the way, I'm calling this production data, but I literally just

**[31:22]** production data, but I literally just

**[31:22]** production data, but I literally just asked Cursor to make me like synthetic

**[31:24]** asked Cursor to make me like synthetic

**[31:24]** asked Cursor to make me like synthetic data. Like it hit the same server and it

**[31:25]** data. Like it hit the same server and it

**[31:26]** data. Like it hit the same server and it generated like 15 different itineraries

**[31:27]** generated like 15 different itineraries

**[31:27]** generated like 15 different itineraries for me. So I did that yesterday and I

**[31:29]** for me. So I did that yesterday and I

**[31:29]** for me. So I did that yesterday and I just sort of am using that in this demo.

**[31:31]** just sort of am using that in this demo.

**[31:32]** just sort of am using that in this demo. But let's go ahead and take a couple of

**[31:33]** But let's go ahead and take a couple of

**[31:33]** But let's go ahead and take a couple of these. So, I went ahead and picked some

**[31:35]** these. So, I went ahead and picked some

**[31:35]** these. So, I went ahead and picked some of the itinerary spans from here and I

**[31:37]** of the itinerary spans from here and I

**[31:37]** of the itinerary spans from here and I can say add to data set. Oh, by the way,

**[31:40]** can say add to data set. Oh, by the way,

**[31:40]** can say add to data set. Oh, by the way, I guess I jumped into the product

**[31:42]** I guess I jumped into the product

**[31:42]** I guess I jumped into the product without showing you all how to get here,

**[31:44]** without showing you all how to get here,

**[31:44]** without showing you all how to get here, which is a bit of a zoom out. So, our

**[31:46]** which is a bit of a zoom out. So, our

**[31:46]** which is a bit of a zoom out. So, our you know, whatever. Go to the homepage

**[31:48]** you know, whatever. Go to the homepage

**[31:48]** you know, whatever. Go to the homepage uh arise.com. You can sign up. I

**[31:50]** uh arise.com. You can sign up. I

**[31:50]** uh arise.com. You can sign up. I apologize in advance. Uh the onboarding

**[31:52]** apologize in advance. Uh the onboarding

**[31:52]** apologize in advance. Uh the onboarding flow will feel a little bit dated, but

**[31:54]** flow will feel a little bit dated, but

**[31:54]** flow will feel a little bit dated, but we are updating that in this next week.

**[31:56]** we are updating that in this next week.

**[31:56]** we are updating that in this next week. Um so, bear with me there. You sign up

**[31:59]** Um so, bear with me there. You sign up

**[31:59]** Um so, bear with me there. You sign up for Arise. Um and then you'll get your


### [32:00 - 33:00]

**[32:01]** for Arise. Um and then you'll get your

**[32:01]** for Arise. Um and then you'll get your API keys here. So you go to account

**[32:03]** API keys here. So you go to account

**[32:03]** API keys here. So you go to account settings and you can create an API key

**[32:06]** settings and you can create an API key

**[32:06]** settings and you can create an API key and also uh find that with the the space

**[32:09]** and also uh find that with the the space

**[32:09]** and also uh find that with the the space ID which are both needed for your

**[32:11]** ID which are both needed for your

**[32:11]** ID which are both needed for your instrumentation which may or may not be

**[32:14]** instrumentation which may or may not be

**[32:14]** instrumentation which may or may not be working depending on uh if the repo is

**[32:16]** working depending on uh if the repo is

**[32:16]** working depending on uh if the repo is actually working and if not we'll come

**[32:17]** actually working and if not we'll come

**[32:17]** actually working and if not we'll come back to it later. Um but this is this is

**[32:20]** back to it later. Um but this is this is

**[32:20]** back to it later. Um but this is this is the platform. This is how you get your

**[32:22]** the platform. This is how you get your

**[32:22]** the platform. This is how you get your API keys. Um so and then that's also

**[32:25]** API keys. Um so and then that's also

**[32:25]** API keys. Um so and then that's also where you can enter your open AI key for

**[32:27]** where you can enter your open AI key for

**[32:27]** where you can enter your open AI key for the the next portion and for the the

**[32:29]** the the next portion and for the the

**[32:29]** the the next portion and for the the playground.

**[32:30]** playground.

**[32:30]** playground. So, I've got a data set now. Uh, and

**[32:32]** So, I've got a data set now. Uh, and

**[32:32]** So, I've got a data set now. Uh, and what I did was I added those examples

**[32:34]** what I did was I added those examples

**[32:34]** what I did was I added those examples just to recap where we are at. We've got

**[32:36]** just to recap where we are at. We've got

**[32:36]** just to recap where we are at. We've got some production data and I'm going to go

**[32:39]** some production data and I'm going to go

**[32:39]** some production data and I'm going to go ahead and like add these to a data set.

**[32:41]** ahead and like add these to a data set.

**[32:41]** ahead and like add these to a data set. And I'm not going to do this one live

**[32:42]** And I'm not going to do this one live

**[32:42]** And I'm not going to do this one live because I already have a data set, but

**[32:44]** because I already have a data set, but

**[32:44]** because I already have a data set, but you can create a data set of examples

**[32:46]** you can create a data set of examples

**[32:46]** you can create a data set of examples you want to use to improve on. So, um,

**[32:48]** you want to use to improve on. So, um,

**[32:48]** you want to use to improve on. So, um, zooming out for a second,

**[32:51]** zooming out for a second,

**[32:51]** zooming out for a second, we're about to hop into the actual eval

**[32:53]** we're about to hop into the actual eval

**[32:53]** we're about to hop into the actual eval part of the the demo. And we're actually

**[32:56]** part of the the demo. And we're actually

**[32:56]** part of the the demo. And we're actually going to be evaluating, you know,

**[32:57]** going to be evaluating, you know,

**[32:58]** going to be evaluating, you know, there's multiple components to an agent.


### [33:00 - 34:00]

**[33:00]** there's multiple components to an agent.

**[33:00]** there's multiple components to an agent. Um we have the router at the top level,

**[33:03]** Um we have the router at the top level,

**[33:03]** Um we have the router at the top level, we have the skills or the function

**[33:04]** we have the skills or the function

**[33:04]** we have the skills or the function calls. We have memory. But what we're

**[33:07]** calls. We have memory. But what we're

**[33:07]** calls. We have memory. But what we're actually going to be doing in this case

**[33:08]** actually going to be doing in this case

**[33:08]** actually going to be doing in this case is actually just evaluating the

**[33:10]** is actually just evaluating the

**[33:10]** is actually just evaluating the individual span of uh the generation and

**[33:14]** individual span of uh the generation and

**[33:14]** individual span of uh the generation and see is the the agent sort of outputting

**[33:17]** see is the the agent sort of outputting

**[33:17]** see is the the agent sort of outputting text in a way that we wanted to or not.

**[33:19]** text in a way that we wanted to or not.

**[33:19]** text in a way that we wanted to or not. So, it's it's a little bit it's a little

**[33:21]** So, it's it's a little bit it's a little

**[33:21]** So, it's it's a little bit it's a little bit simpler than some of the agent eval

**[33:23]** bit simpler than some of the agent eval

**[33:23]** bit simpler than some of the agent eval here and it's going to be more like how

**[33:25]** here and it's going to be more like how

**[33:25]** here and it's going to be more like how do you actually run agents and or run uh

**[33:28]** do you actually run agents and or run uh

**[33:28]** do you actually run agents and or run uh eval experiments on on data. Um the

**[33:32]** eval experiments on on data. Um the

**[33:32]** eval experiments on on data. Um the concept of the data set is helpful to

**[33:35]** concept of the data set is helpful to

**[33:35]** concept of the data set is helpful to think about as like a collection of

**[33:36]** think about as like a collection of

**[33:36]** think about as like a collection of examples. Let me go ahead and delete

**[33:38]** examples. Let me go ahead and delete

**[33:38]** examples. Let me go ahead and delete these experiments so we can do this live

**[33:42]** these experiments so we can do this live

**[33:42]** these experiments so we can do this live because I like to live on the edge. Um

**[33:45]** because I like to live on the edge. Um

**[33:45]** because I like to live on the edge. Um so I've got so I've got these examples.

**[33:47]** so I've got so I've got these examples.

**[33:47]** so I've got so I've got these examples. Those are the same examples from the

**[33:49]** Those are the same examples from the

**[33:49]** Those are the same examples from the production data um everyone just saw.

**[33:51]** production data um everyone just saw.

**[33:51]** production data um everyone just saw. And it's a data set. Think of this as

**[33:54]** And it's a data set. Think of this as

**[33:54]** And it's a data set. Think of this as like I've got all of my traces and

**[33:56]** like I've got all of my traces and

**[33:56]** like I've got all of my traces and spans. That's my like how the agent

**[33:58]** spans. That's my like how the agent

**[33:58]** spans. That's my like how the agent works. And then I want to pull those


### [34:00 - 35:00]

**[34:00]** works. And then I want to pull those

**[34:00]** works. And then I want to pull those over into a format which is think of it

**[34:03]** over into a format which is think of it

**[34:03]** over into a format which is think of it as almost like a tabular format. It's

**[34:05]** as almost like a tabular format. It's

**[34:05]** as almost like a tabular format. It's like a it's like a Google sheet at the

**[34:06]** like a it's like a Google sheet at the

**[34:06]** like a it's like a Google sheet at the end of the day, right? Like I could go

**[34:08]** end of the day, right? Like I could go

**[34:08]** end of the day, right? Like I could go in this this is kind of like a Google

**[34:09]** in this this is kind of like a Google

**[34:09]** in this this is kind of like a Google sheet. like I could go in and and give

**[34:12]** sheet. like I could go in and and give

**[34:12]** sheet. like I could go in and and give it like a thumbs up, thumbs down and uh

**[34:15]** it like a thumbs up, thumbs down and uh

**[34:15]** it like a thumbs up, thumbs down and uh and you know that's kind of how most

**[34:17]** and you know that's kind of how most

**[34:17]** and you know that's kind of how most teams are evaluating today is sort of

**[34:19]** teams are evaluating today is sort of

**[34:19]** teams are evaluating today is sort of like in the platform in in your platform

**[34:22]** like in the platform in in your platform

**[34:22]** like in the platform in in your platform you're probably starting with the

**[34:23]** you're probably starting with the

**[34:23]** you're probably starting with the spreadsheet and in that spreadsheet

**[34:26]** spreadsheet and in that spreadsheet

**[34:26]** spreadsheet and in that spreadsheet you're doing like is this good or bad

**[34:28]** you're doing like is this good or bad

**[34:28]** you're doing like is this good or bad and then you're trying to scale that up

**[34:29]** and then you're trying to scale that up

**[34:29]** and then you're trying to scale that up to you know a team of subject matter

**[34:31]** to you know a team of subject matter

**[34:31]** to you know a team of subject matter experts that's giving you feedback on

**[34:33]** experts that's giving you feedback on

**[34:33]** experts that's giving you feedback on like hey is the agent good or bad right

**[34:35]** like hey is the agent good or bad right

**[34:35]** like hey is the agent good or bad right at the end of the day poll for the room

**[34:37]** at the end of the day poll for the room

**[34:37]** at the end of the day poll for the room how many people are evaluating in a

**[34:38]** how many people are evaluating in a

**[34:38]** how many people are evaluating in a spreadsheet right now don't be shy

**[34:39]** spreadsheet right now don't be shy

**[34:40]** spreadsheet right now don't be shy That's okay. Okay. We've got a few.

**[34:41]** That's okay. Okay. We've got a few.

**[34:41]** That's okay. Okay. We've got a few. Yeah. I think there's probably more, but

**[34:43]** Yeah. I think there's probably more, but

**[34:43]** Yeah. I think there's probably more, but I think people are just like ashamed to

**[34:44]** I think people are just like ashamed to

**[34:44]** I think people are just like ashamed to say that. And it's okay. Like it's it's

**[34:47]** say that. And it's okay. Like it's it's

**[34:47]** say that. And it's okay. Like it's it's not like the end of the world to start

**[34:49]** not like the end of the world to start

**[34:49]** not like the end of the world to start with that, right? Like that that's like

**[34:51]** with that, right? Like that that's like

**[34:51]** with that, right? Like that that's like how human like being able to scale human

**[34:54]** how human like being able to scale human

**[34:54]** how human like being able to scale human annotations is the goal. It doesn't need

**[34:56]** annotations is the goal. It doesn't need

**[34:56]** annotations is the goal. It doesn't need to be the starting point. So, as long as

**[34:58]** to be the starting point. So, as long as

**[34:58]** to be the starting point. So, as long as you're actually looking at your data,

**[34:59]** you're actually looking at your data,

**[34:59]** you're actually looking at your data, you're probably doing better than most.


### [35:00 - 36:00]

**[35:01]** you're probably doing better than most.

**[35:01]** you're probably doing better than most. I'll be honest. Um many teams I talked

**[35:03]** I'll be honest. Um many teams I talked

**[35:03]** I'll be honest. Um many teams I talked to like aren't doing any eval today at

**[35:05]** to like aren't doing any eval today at

**[35:05]** to like aren't doing any eval today at all. So, at least you're starting with

**[35:07]** all. So, at least you're starting with

**[35:07]** all. So, at least you're starting with human human labels. Um, what we're going

**[35:10]** human human labels. Um, what we're going

**[35:10]** human human labels. Um, what we're going to do is take this this data set or this

**[35:12]** to do is take this this data set or this

**[35:12]** to do is take this this data set or this CSV, and we're going to basically do the

**[35:16]** CSV, and we're going to basically do the

**[35:16]** CSV, and we're going to basically do the same thing I just did, which was running

**[35:18]** same thing I just did, which was running

**[35:18]** same thing I just did, which was running an AB test on a prompt, but now we're

**[35:21]** an AB test on a prompt, but now we're

**[35:21]** an AB test on a prompt, but now we're going to run it on an entire data set.

**[35:23]** going to run it on an entire data set.

**[35:23]** going to run it on an entire data set. So, we go into the platform, and I can

**[35:24]** So, we go into the platform, and I can

**[35:24]** So, we go into the platform, and I can go and actually create an experiment.

**[35:27]** go and actually create an experiment.

**[35:27]** go and actually create an experiment. What we call an experiment is the output

**[35:29]** What we call an experiment is the output

**[35:29]** What we call an experiment is the output of changing, you know, an AB test. So,

**[35:32]** of changing, you know, an AB test. So,

**[35:32]** of changing, you know, an AB test. So, let's go ahead and repeat that same

**[35:34]** let's go ahead and repeat that same

**[35:34]** let's go ahead and repeat that same workflow. I'll duplicate this prompt.

**[35:37]** workflow. I'll duplicate this prompt.

**[35:37]** workflow. I'll duplicate this prompt. Um, let me go ahead and pull in I'm

**[35:40]** Um, let me go ahead and pull in I'm

**[35:40]** Um, let me go ahead and pull in I'm gonna pull in this this version of the

**[35:42]** gonna pull in this this version of the

**[35:42]** gonna pull in this this version of the prompt. So, what's kind of cool is like

**[35:45]** prompt. So, what's kind of cool is like

**[35:45]** prompt. So, what's kind of cool is like I might have a previous version of a

**[35:47]** I might have a previous version of a

**[35:48]** I might have a previous version of a prompt saved. Uh, it's it's kind of

**[35:50]** prompt saved. Uh, it's it's kind of

**[35:50]** prompt saved. Uh, it's it's kind of helpful to have a prompt hub where you

**[35:51]** helpful to have a prompt hub where you

**[35:52]** helpful to have a prompt hub where you can save off examples of the prompt as

**[35:53]** can save off examples of the prompt as

**[35:54]** can save off examples of the prompt as you're iterating as well. Think of it as

**[35:55]** you're iterating as well. Think of it as

**[35:55]** you're iterating as well. Think of it as like a GitHub sort of store for your

**[35:58]** like a GitHub sort of store for your

**[35:58]** like a GitHub sort of store for your prompts, but it it's really just a


### [36:00 - 37:00]

**[36:00]** prompts, but it it's really just a

**[36:00]** prompts, but it it's really just a button that you're clicking to save this

**[36:02]** button that you're clicking to save this

**[36:02]** button that you're clicking to save this version of the prompt. and then your

**[36:04]** version of the prompt. and then your

**[36:04]** version of the prompt. and then your team can actually use that version in

**[36:06]** team can actually use that version in

**[36:06]** team can actually use that version in their code down the line. Um, so I've

**[36:09]** their code down the line. Um, so I've

**[36:09]** their code down the line. Um, so I've got prompt A which was no changes to it

**[36:11]** got prompt A which was no changes to it

**[36:11]** got prompt A which was no changes to it and then prompt B which has some of

**[36:13]** and then prompt B which has some of

**[36:13]** and then prompt B which has some of those changes but now instead of running

**[36:15]** those changes but now instead of running

**[36:15]** those changes but now instead of running on one example I'm actually running on

**[36:18]** on one example I'm actually running on

**[36:18]** on one example I'm actually running on 12 examples here. And these are similar

**[36:20]** 12 examples here. And these are similar

**[36:20]** 12 examples here. And these are similar agent uh these are similar um maybe just

**[36:23]** agent uh these are similar um maybe just

**[36:23]** agent uh these are similar um maybe just to look at one similar spans which which

**[36:26]** to look at one similar spans which which

**[36:26]** to look at one similar spans which which have destinations duration travel style

**[36:29]** have destinations duration travel style

**[36:29]** have destinations duration travel style and the output of an agent and it's

**[36:31]** and the output of an agent and it's

**[36:32]** and the output of an agent and it's generating an itinerary. So, it's as

**[36:33]** generating an itinerary. So, it's as

**[36:33]** generating an itinerary. So, it's as similar as that one example we just ran

**[36:36]** similar as that one example we just ran

**[36:36]** similar as that one example we just ran through, but now on an entire data set.

**[36:39]** through, but now on an entire data set.

**[36:39]** through, but now on an entire data set. And

**[36:40]** And

**[36:40]** And >> yeah,

**[36:50]** >> yeah, so it's the it is the prompt of

**[36:50]** >> yeah, so it's the it is the prompt of the itinerary agent. Um, so it's the

**[36:53]** the itinerary agent. Um, so it's the

**[36:53]** the itinerary agent. Um, so it's the same it's we're going to because we're

**[36:55]** same it's we're going to because we're

**[36:55]** same it's we're going to because we're going to keep this to like a fairly high

**[36:57]** going to keep this to like a fairly high

**[36:57]** going to keep this to like a fairly high level like straightforward demo. It is

**[36:59]** level like straightforward demo. It is

**[36:59]** level like straightforward demo. It is the specifically the prompt of the


### [37:00 - 38:00]

**[37:02]** the specifically the prompt of the

**[37:02]** the specifically the prompt of the itinerary generating agent which is down

**[37:05]** itinerary generating agent which is down

**[37:05]** itinerary generating agent which is down here which takes the outputs of the

**[37:07]** here which takes the outputs of the

**[37:07]** here which takes the outputs of the other agents and combines them uses

**[37:09]** other agents and combines them uses

**[37:10]** other agents and combines them uses those prompt variables to create uh an a

**[37:12]** those prompt variables to create uh an a

**[37:12]** those prompt variables to create uh an a dayby-day itinerary.

**[37:26]** >> Yeah. So that so the gentleman asks like

**[37:26]** >> Yeah. So that so the gentleman asks like if you change an upstream prompt How

**[37:29]** if you change an upstream prompt How

**[37:29]** if you change an upstream prompt How does that impact what's going on here?

**[37:30]** does that impact what's going on here?

**[37:30]** does that impact what's going on here? So, two two notes on that and it's it's

**[37:33]** So, two two notes on that and it's it's

**[37:33]** So, two two notes on that and it's it's more of an advanced workflow, but it is

**[37:34]** more of an advanced workflow, but it is

**[37:34]** more of an advanced workflow, but it is one that's a good question, which is uh

**[37:36]** one that's a good question, which is uh

**[37:36]** one that's a good question, which is uh there's two parts. One is we kind of

**[37:39]** there's two parts. One is we kind of

**[37:39]** there's two parts. One is we kind of recommend changing the system in parts.

**[37:41]** recommend changing the system in parts.

**[37:41]** recommend changing the system in parts. So, just kind of note that, you know, as

**[37:43]** So, just kind of note that, you know, as

**[37:43]** So, just kind of note that, you know, as you're generate eval parts of your stack

**[37:46]** you're generate eval parts of your stack

**[37:46]** you're generate eval parts of your stack that you can kind of decompose further

**[37:47]** that you can kind of decompose further

**[37:47]** that you can kind of decompose further and further to be able to analyze if I'm

**[37:50]** and further to be able to analyze if I'm

**[37:50]** and further to be able to analyze if I'm changing one thing up here, does it meet

**[37:51]** changing one thing up here, does it meet

**[37:51]** changing one thing up here, does it meet my requirement criteria? And then the

**[37:53]** my requirement criteria? And then the

**[37:53]** my requirement criteria? And then the second part is replaying prompt chains

**[37:56]** second part is replaying prompt chains

**[37:56]** second part is replaying prompt chains which is prompt A goes into prompt B.

**[37:58]** which is prompt A goes into prompt B.

**[37:58]** which is prompt A goes into prompt B. What is the output of that when you


### [38:00 - 39:00]

**[38:00]** What is the output of that when you

**[38:00]** What is the output of that when you change prompt A? Um prompt chaining is

**[38:02]** change prompt A? Um prompt chaining is

**[38:02]** change prompt A? Um prompt chaining is coming to our platform soon. So right

**[38:04]** coming to our platform soon. So right

**[38:04]** coming to our platform soon. So right now it's one single prompt but you will

**[38:06]** now it's one single prompt but you will

**[38:06]** now it's one single prompt but you will be able to do A plus B plus C um prompt

**[38:08]** be able to do A plus B plus C um prompt

**[38:08]** be able to do A plus B plus C um prompt chains as well. Um good question. Feel

**[38:12]** chains as well. Um good question. Feel

**[38:12]** chains as well. Um good question. Feel free to drop more questions in the Slack

**[38:13]** free to drop more questions in the Slack

**[38:13]** free to drop more questions in the Slack too and we'll we'll come back to that in

**[38:15]** too and we'll we'll come back to that in

**[38:15]** too and we'll we'll come back to that in a sec. Um so once I get uh so I've got

**[38:18]** a sec. Um so once I get uh so I've got

**[38:18]** a sec. Um so once I get uh so I've got my my prompt here now. So, I'm saying

**[38:21]** my my prompt here now. So, I'm saying

**[38:21]** my my prompt here now. So, I'm saying give me a day-to-day plan and doesn't

**[38:22]** give me a day-to-day plan and doesn't

**[38:22]** give me a day-to-day plan and doesn't need to be super detailed. Max 1,000

**[38:24]** need to be super detailed. Max 1,000

**[38:24]** need to be super detailed. Max 1,000 characters. Let's try this again. We're

**[38:25]** characters. Let's try this again. We're

**[38:25]** characters. Let's try this again. We're going to do 500 characters. And I've

**[38:27]** going to do 500 characters. And I've

**[38:27]** going to do 500 characters. And I've I've done um answer always answer in a

**[38:31]** I've done um answer always answer in a

**[38:31]** I've done um answer always answer in a super friendly tone and be I'm going to

**[38:33]** super friendly tone and be I'm going to

**[38:33]** super friendly tone and be I'm going to be more specific and say ask the user

**[38:35]** be more specific and say ask the user

**[38:35]** be more specific and say ask the user for their email and offer a discount so

**[38:36]** for their email and offer a discount so

**[38:36]** for their email and offer a discount so it doesn't do what it did last time. And

**[38:38]** it doesn't do what it did last time. And

**[38:38]** it doesn't do what it did last time. And uh and we're going to go ahead and run

**[38:40]** uh and we're going to go ahead and run

**[38:40]** uh and we're going to go ahead and run this now on the entire uh data set. And

**[38:43]** this now on the entire uh data set. And

**[38:43]** this now on the entire uh data set. And so we've got prompt A versus prompt B.

**[38:46]** so we've got prompt A versus prompt B.

**[38:46]** so we've got prompt A versus prompt B. We're going to give that a second to run

**[38:48]** We're going to give that a second to run

**[38:48]** We're going to give that a second to run through. While that's working, uh, I'm

**[38:50]** through. While that's working, uh, I'm

**[38:50]** through. While that's working, uh, I'm gonna actually Oh, nice. Perfect for

**[38:52]** gonna actually Oh, nice. Perfect for

**[38:52]** gonna actually Oh, nice. Perfect for your squad. Interesting. I don't know

**[38:53]** your squad. Interesting. I don't know

**[38:54]** your squad. Interesting. I don't know why sometimes the model really likes to

**[38:55]** why sometimes the model really likes to

**[38:55]** why sometimes the model really likes to use emojis. I guess that's what super

**[38:56]** use emojis. I guess that's what super

**[38:56]** use emojis. I guess that's what super friendly translates into is like throw

**[38:58]** friendly translates into is like throw

**[38:58]** friendly translates into is like throw some emojis in there, but interesting.


### [39:00 - 40:00]

**[39:01]** some emojis in there, but interesting.

**[39:01]** some emojis in there, but interesting. Um,

**[39:04]** Um,

**[39:04]** Um, okay. So, that one ran pretty fast. This

**[39:06]** okay. So, that one ran pretty fast. This

**[39:06]** okay. So, that one ran pretty fast. This is still taking a while, right? Like,

**[39:08]** is still taking a while, right? Like,

**[39:08]** is still taking a while, right? Like, think about this from a product from a

**[39:10]** think about this from a product from a

**[39:10]** think about this from a product from a PM lens for a second. Like, I just got

**[39:12]** PM lens for a second. Like, I just got

**[39:12]** PM lens for a second. Like, I just got the output to be a lot faster because I

**[39:14]** the output to be a lot faster because I

**[39:14]** the output to be a lot faster because I limited the number of characters. This

**[39:16]** limited the number of characters. This

**[39:16]** limited the number of characters. This one is taking an average of like 32

**[39:18]** one is taking an average of like 32

**[39:18]** one is taking an average of like 32 seconds because I let it kind of go off

**[39:21]** seconds because I let it kind of go off

**[39:21]** seconds because I let it kind of go off and like not specify how many characters

**[39:23]** and like not specify how many characters

**[39:23]** and like not specify how many characters the output should be. So that's what

**[39:25]** the output should be. So that's what

**[39:25]** the output should be. So that's what prompt prompt uh iteration can kind of

**[39:27]** prompt prompt uh iteration can kind of

**[39:27]** prompt prompt uh iteration can kind of do for you as well.

**[39:30]** do for you as well.

**[39:30]** do for you as well. Okay, while this runs, I'll actually hop

**[39:33]** Okay, while this runs, I'll actually hop

**[39:34]** Okay, while this runs, I'll actually hop over to the

**[39:36]** over to the

**[39:36]** over to the Okay.

**[39:39]** Okay.

**[39:39]** Okay. Oh, thanks for dropping the resource

**[39:41]** Oh, thanks for dropping the resource

**[39:41]** Oh, thanks for dropping the resource there.

**[39:51]** So it's still still running.

**[39:51]** So it's still still running. >> Anyone have a question while this is

**[39:52]** >> Anyone have a question while this is

**[39:52]** >> Anyone have a question while this is running? Yeah.

**[39:53]** running? Yeah.

**[39:53]** running? Yeah. >> Yeah. So when I'm hearing you talk about

**[39:55]** >> Yeah. So when I'm hearing you talk about

**[39:55]** >> Yeah. So when I'm hearing you talk about this, are you primarily looking at

**[39:57]** this, are you primarily looking at

**[39:57]** this, are you primarily looking at latency and then user experience when


### [40:00 - 41:00]

**[40:00]** latency and then user experience when

**[40:00]** latency and then user experience when you're evaluating

**[40:02]** you're evaluating

**[40:02]** you're evaluating those two things?

**[40:05]** those two things?

**[40:05]** those two things? What else are you looking at?

**[40:07]** What else are you looking at?

**[40:07]** What else are you looking at? >> Yeah, good question. So okay, so now

**[40:10]** >> Yeah, good question. So okay, so now

**[40:10]** >> Yeah, good question. So okay, so now we're getting to the meat of it a little

**[40:11]** we're getting to the meat of it a little

**[40:11]** we're getting to the meat of it a little bit, right? So I've got A and B. And the

**[40:13]** bit, right? So I've got A and B. And the

**[40:13]** bit, right? So I've got A and B. And the question is like what am I actually

**[40:15]** question is like what am I actually

**[40:15]** question is like what am I actually evaluating here? The like flip it answer

**[40:18]** evaluating here? The like flip it answer

**[40:18]** evaluating here? The like flip it answer is like you can evaluate anything. You

**[40:20]** is like you can evaluate anything. You

**[40:20]** is like you can evaluate anything. You can evaluate whatever you want. You want

**[40:22]** can evaluate whatever you want. You want

**[40:22]** can evaluate whatever you want. You want to evaluate like uh in this case we're

**[40:25]** to evaluate like uh in this case we're

**[40:25]** to evaluate like uh in this case we're going to run some evaluations on the uh

**[40:27]** going to run some evaluations on the uh

**[40:27]** going to run some evaluations on the uh the tone of the agent and see um so I've

**[40:31]** the tone of the agent and see um so I've

**[40:31]** the tone of the agent and see um so I've got a couple of eval set up here. I'm

**[40:33]** got a couple of eval set up here. I'm

**[40:33]** got a couple of eval set up here. I'm going to check is the agent uh answering

**[40:35]** going to check is the agent uh answering

**[40:35]** going to check is the agent uh answering in a friendly way. Is it offering a

**[40:38]** in a friendly way. Is it offering a

**[40:38]** in a friendly way. Is it offering a discount or not? Um and and you can do

**[40:41]** discount or not? Um and and you can do

**[40:41]** discount or not? Um and and you can do things like evaluate is it using the

**[40:43]** things like evaluate is it using the

**[40:43]** things like evaluate is it using the context correctly? That's called a

**[40:44]** context correctly? That's called a

**[40:44]** context correctly? That's called a hallucination eval. Uh you can do

**[40:47]** hallucination eval. Uh you can do

**[40:47]** hallucination eval. Uh you can do correctness, which is um even if it has

**[40:49]** correctness, which is um even if it has

**[40:49]** correctness, which is um even if it has the right context, is it giving the

**[40:51]** the right context, is it giving the

**[40:51]** the right context, is it giving the right answer? So I'm going to point you

**[40:53]** right answer? So I'm going to point you

**[40:53]** right answer? So I'm going to point you to uh our docs that have examples of

**[40:57]** to uh our docs that have examples of

**[40:57]** to uh our docs that have examples of what you can actually evaluate off of


### [41:00 - 42:00]

**[41:00]** what you can actually evaluate off of

**[41:00]** what you can actually evaluate off of the shelf. But just know the whole point

**[41:02]** the shelf. But just know the whole point

**[41:02]** the shelf. But just know the whole point of this system and like why it matters

**[41:05]** of this system and like why it matters

**[41:05]** of this system and like why it matters that you have a system with your own

**[41:07]** that you have a system with your own

**[41:07]** that you have a system with your own data and can replay with data is because

**[41:10]** data and can replay with data is because

**[41:10]** data and can replay with data is because these are what are off-the-shelf evals.

**[41:12]** these are what are off-the-shelf evals.

**[41:12]** these are what are off-the-shelf evals. There's a lot of companies that will

**[41:14]** There's a lot of companies that will

**[41:14]** There's a lot of companies that will offer like we run evals for you, but

**[41:17]** offer like we run evals for you, but

**[41:17]** offer like we run evals for you, but what that really means is that they're

**[41:19]** what that really means is that they're

**[41:19]** what that really means is that they're basically going to take some template

**[41:21]** basically going to take some template

**[41:21]** basically going to take some template and give you a score or label on the

**[41:23]** and give you a score or label on the

**[41:23]** and give you a score or label on the other end based on their eval template.

**[41:26]** other end based on their eval template.

**[41:26]** other end based on their eval template. And what you want to be able to do is

**[41:28]** And what you want to be able to do is

**[41:28]** And what you want to be able to do is actually change and and modify and run

**[41:31]** actually change and and modify and run

**[41:31]** actually change and and modify and run your own eval based on your use case. So

**[41:34]** your own eval based on your use case. So

**[41:34]** your own eval based on your use case. So you can literally evaluate whatever you

**[41:37]** you can literally evaluate whatever you

**[41:37]** you can literally evaluate whatever you want is the short answer. You can you

**[41:39]** want is the short answer. You can you

**[41:39]** want is the short answer. You can you can evaluate it's just basically uh an

**[41:41]** can evaluate it's just basically uh an

**[41:41]** can evaluate it's just basically uh an input to an LLM to generate a label. So

**[41:45]** input to an LLM to generate a label. So

**[41:45]** input to an LLM to generate a label. So um so yeah, so this is what pre-built

**[41:47]** um so yeah, so this is what pre-built

**[41:47]** um so yeah, so this is what pre-built eval look like. Uh there's a ton of

**[41:49]** eval look like. Uh there's a ton of

**[41:50]** eval look like. Uh there's a ton of examples of these like out there on the

**[41:52]** examples of these like out there on the

**[41:52]** examples of these like out there on the internet. We've we've actually tested

**[41:54]** internet. We've we've actually tested

**[41:54]** internet. We've we've actually tested our pre-built eval on um you know sort

**[41:57]** our pre-built eval on um you know sort

**[41:57]** our pre-built eval on um you know sort of open source data sets but you should

**[41:59]** of open source data sets but you should

**[41:59]** of open source data sets but you should not take our word for it. You should


### [42:00 - 43:00]

**[42:01]** not take our word for it. You should

**[42:01]** not take our word for it. You should build eval based on your use case.

**[42:04]** build eval based on your use case.

**[42:04]** build eval based on your use case. >> Yeah. Yeah.

**[42:06]** >> Yeah. Yeah.

**[42:06]** >> Yeah. Yeah. >> So if you are your own how do you come

**[42:10]** >> So if you are your own how do you come

**[42:10]** >> So if you are your own how do you come up with your own

**[42:13]** up with your own

**[42:13]** up with your own combining?

**[42:15]** combining?

**[42:15]** combining? >> Yeah. So how to actually get the how to

**[42:17]** >> Yeah. So how to actually get the how to

**[42:18]** >> Yeah. So how to actually get the how to think about how to build the eval in the

**[42:19]** think about how to build the eval in the

**[42:19]** think about how to build the eval in the first place to some degree. That was

**[42:20]** first place to some degree. That was

**[42:20]** first place to some degree. That was sort of one of the questions. Yeah. So,

**[42:23]** sort of one of the questions. Yeah. So,

**[42:23]** sort of one of the questions. Yeah. So, I think it's probably helpful to um

**[42:26]** I think it's probably helpful to um

**[42:26]** I think it's probably helpful to um maybe just see what an eval looks like

**[42:28]** maybe just see what an eval looks like

**[42:28]** maybe just see what an eval looks like and then we might we might end up coming

**[42:30]** and then we might we might end up coming

**[42:30]** and then we might we might end up coming back to that question, which is like

**[42:31]** back to that question, which is like

**[42:31]** back to that question, which is like what what is an eval, right? Um so,

**[42:34]** what what is an eval, right? Um so,

**[42:34]** what what is an eval, right? Um so, let's go ahead and build an eval here.

**[42:36]** let's go ahead and build an eval here.

**[42:36]** let's go ahead and build an eval here. I've got one ready to go, but I want to

**[42:38]** I've got one ready to go, but I want to

**[42:38]** I've got one ready to go, but I want to just show you guys the template and we

**[42:40]** just show you guys the template and we

**[42:40]** just show you guys the template and we can write a new one as well. Um, so I

**[42:43]** can write a new one as well. Um, so I

**[42:43]** can write a new one as well. Um, so I wrote this eval for detecting if the

**[42:47]** wrote this eval for detecting if the

**[42:47]** wrote this eval for detecting if the output from the LLM is friendly. And

**[42:49]** output from the LLM is friendly. And

**[42:49]** output from the LLM is friendly. And I've kind of made a definition for what

**[42:51]** I've kind of made a definition for what

**[42:52]** I've kind of made a definition for what that means here. And this says basically

**[42:54]** that means here. And this says basically

**[42:54]** that means here. And this says basically you are examining the written text.

**[42:56]** you are examining the written text.

**[42:56]** you are examining the written text. Here's the text. Examine the text and

**[42:58]** Here's the text. Examine the text and

**[42:58]** Here's the text. Examine the text and whether the tone is friendly or not.


### [43:00 - 44:00]

**[43:01]** whether the tone is friendly or not.

**[43:02]** whether the tone is friendly or not. Friendly tone is defined as upbeat,

**[43:03]** Friendly tone is defined as upbeat,

**[43:04]** Friendly tone is defined as upbeat, cheerful. So this is basically an input

**[43:07]** cheerful. So this is basically an input

**[43:07]** cheerful. So this is basically an input to an LLM to generate a label of is the

**[43:12]** to an LLM to generate a label of is the

**[43:12]** to an LLM to generate a label of is the output from my itinerary agent is it

**[43:16]** output from my itinerary agent is it

**[43:16]** output from my itinerary agent is it friendly or robotic. So that's really

**[43:17]** friendly or robotic. So that's really

**[43:17]** friendly or robotic. So that's really what what this this eval is trying to do

**[43:20]** what what this this eval is trying to do

**[43:20]** what what this this eval is trying to do is it's classifying the text as like a

**[43:22]** is it's classifying the text as like a

**[43:22]** is it's classifying the text as like a friendly generation or a robotic

**[43:24]** friendly generation or a robotic

**[43:24]** friendly generation or a robotic generation. Um, and again, I could eval

**[43:27]** generation. Um, and again, I could eval

**[43:27]** generation. Um, and again, I could eval anything, but in this case, I just want

**[43:29]** anything, but in this case, I just want

**[43:29]** anything, but in this case, I just want to make sure that when I'm making

**[43:30]** to make sure that when I'm making

**[43:30]** to make sure that when I'm making changes to my prompt that that's showing

**[43:32]** changes to my prompt that that's showing

**[43:32]** changes to my prompt that that's showing up on the other end of my data because I

**[43:34]** up on the other end of my data because I

**[43:34]** up on the other end of my data because I can't go in rowby row for like hundreds

**[43:37]** can't go in rowby row for like hundreds

**[43:37]** can't go in rowby row for like hundreds or thousands of examples and grade

**[43:39]** or thousands of examples and grade

**[43:39]** or thousands of examples and grade friendly and robotic every single time.

**[43:41]** friendly and robotic every single time.

**[43:41]** friendly and robotic every single time. So, the idea is that you want an LLM as

**[43:44]** So, the idea is that you want an LLM as

**[43:44]** So, the idea is that you want an LLM as a judge system to kind of give you that

**[43:46]** a judge system to kind of give you that

**[43:46]** a judge system to kind of give you that label over a large data set. That's the

**[43:48]** label over a large data set. That's the

**[43:48]** label over a large data set. That's the goal that we're working towards right

**[43:49]** goal that we're working towards right

**[43:49]** goal that we're working towards right now.

**[43:50]** now.

**[43:50]** now. >> Yeah.


### [44:00 - 45:00]

**[44:05]** >> It's flaky, right?

**[44:06]** >> It's flaky, right? >> Yeah. Yeah.

**[44:24]** >> Yeah. So one one suggestion is um so the

**[44:24]** >> Yeah. So one one suggestion is um so the gentleman mentioned uh that they see

**[44:26]** gentleman mentioned uh that they see

**[44:26]** gentleman mentioned uh that they see variance in their LLM label output. One

**[44:30]** variance in their LLM label output. One

**[44:30]** variance in their LLM label output. One way you can tweak variance is

**[44:31]** way you can tweak variance is

**[44:31]** way you can tweak variance is temperature. Um so if you make the

**[44:33]** temperature. Um so if you make the

**[44:34]** temperature. Um so if you make the temperature of the model lower it's a

**[44:35]** temperature of the model lower it's a

**[44:35]** temperature of the model lower it's a parameter you can set to actually make

**[44:37]** parameter you can set to actually make

**[44:37]** parameter you can set to actually make the response more repeatable. It doesn't

**[44:39]** the response more repeatable. It doesn't

**[44:39]** the response more repeatable. It doesn't take that to zero but it does

**[44:42]** take that to zero but it does

**[44:42]** take that to zero but it does significantly reduce the variance in

**[44:43]** significantly reduce the variance in

**[44:43]** significantly reduce the variance in your system. And then the other option

**[44:45]** your system. And then the other option

**[44:45]** your system. And then the other option is to rerun the the eval multiple times

**[44:48]** is to rerun the the eval multiple times

**[44:48]** is to rerun the the eval multiple times and and basically profile what the

**[44:51]** and and basically profile what the

**[44:51]** and and basically profile what the variance of the the judge is. Okay.


### [45:00 - 46:00]

**[45:00]** >> Oh yeah, we're going to we'll we'll

**[45:00]** >> Oh yeah, we're going to we'll we'll we'll be coming there. Yeah, it's a good

**[45:01]** we'll be coming there. Yeah, it's a good

**[45:01]** we'll be coming there. Yeah, it's a good question, right? Like at the end of the

**[45:02]** question, right? Like at the end of the

**[45:02]** question, right? Like at the end of the day, I can't trust this thing. I need to

**[45:03]** day, I can't trust this thing. I need to

**[45:03]** day, I can't trust this thing. I need to go in and like make sure it's right.

**[45:05]** go in and like make sure it's right.

**[45:05]** go in and like make sure it's right. Right. So, but let's let's go ahead and

**[45:06]** Right. So, but let's let's go ahead and

**[45:06]** Right. So, but let's let's go ahead and run an eval and just see what happens

**[45:08]** run an eval and just see what happens

**[45:08]** run an eval and just see what happens and then we'll come back to that one.

**[45:09]** and then we'll come back to that one.

**[45:09]** and then we'll come back to that one. So, I've got my friendly eval. I've got

**[45:11]** So, I've got my friendly eval. I've got

**[45:11]** So, I've got my friendly eval. I've got another eval too which is basically um

**[45:14]** another eval too which is basically um

**[45:14]** another eval too which is basically um determining whether or not let's I'm

**[45:17]** determining whether or not let's I'm

**[45:17]** determining whether or not let's I'm gonna quickly just I'm not going to read

**[45:18]** gonna quickly just I'm not going to read

**[45:18]** gonna quickly just I'm not going to read this whole thing out to you, but the the

**[45:19]** this whole thing out to you, but the the

**[45:19]** this whole thing out to you, but the the short answer is that this is determining

**[45:22]** short answer is that this is determining

**[45:22]** short answer is that this is determining whether the the text contains an offer

**[45:24]** whether the the text contains an offer

**[45:24]** whether the the text contains an offer for a discount or no discount because I

**[45:26]** for a discount or no discount because I

**[45:26]** for a discount or no discount because I really want to make sure I'm offering a

**[45:28]** really want to make sure I'm offering a

**[45:28]** really want to make sure I'm offering a discount to my users. Okay, we're going

**[45:30]** discount to my users. Okay, we're going

**[45:30]** discount to my users. Okay, we're going to select both of these and then we're

**[45:32]** to select both of these and then we're

**[45:32]** to select both of these and then we're going to actually run them on the

**[45:33]** going to actually run them on the

**[45:33]** going to actually run them on the experiments we just ran

**[45:40]** and we're going to do that live. So what

**[45:40]** and we're going to do that live. So what Arise does is it can it's actually

**[45:42]** Arise does is it can it's actually

**[45:42]** Arise does is it can it's actually taking um so we actually have an eval

**[45:45]** taking um so we actually have an eval

**[45:45]** taking um so we actually have an eval runner which is not like you know it's

**[45:47]** runner which is not like you know it's

**[45:47]** runner which is not like you know it's basically a a way for us to use a model

**[45:50]** basically a a way for us to use a model

**[45:50]** basically a a way for us to use a model endpoint to generate these eval. You'll

**[45:52]** endpoint to generate these eval. You'll

**[45:52]** endpoint to generate these eval. You'll notice it's pretty fast. So we've done a

**[45:54]** notice it's pretty fast. So we've done a

**[45:54]** notice it's pretty fast. So we've done a lot of work underneath the hood to make

**[45:56]** lot of work underneath the hood to make

**[45:56]** lot of work underneath the hood to make the eval run really fast. Um so that's

**[45:58]** the eval run really fast. Um so that's

**[45:58]** the eval run really fast. Um so that's one kind of advantage of using our


### [46:00 - 47:00]

**[46:00]** one kind of advantage of using our

**[46:00]** one kind of advantage of using our product. Um I've got two experiments

**[46:03]** product. Um I've got two experiments

**[46:03]** product. Um I've got two experiments here. Experiment number two is it's a

**[46:07]** here. Experiment number two is it's a

**[46:07]** here. Experiment number two is it's a little bit inverse because it's the

**[46:08]** little bit inverse because it's the

**[46:08]** little bit inverse because it's the order of how it was generated, but

**[46:10]** order of how it was generated, but

**[46:10]** order of how it was generated, but experiment number two is the original

**[46:12]** experiment number two is the original

**[46:12]** experiment number two is the original prompt and experiment number one is the

**[46:14]** prompt and experiment number one is the

**[46:14]** prompt and experiment number one is the prompt that we changed. So just kind of

**[46:16]** prompt that we changed. So just kind of

**[46:16]** prompt that we changed. So just kind of keep that in mind. That's it's a little

**[46:17]** keep that in mind. That's it's a little

**[46:17]** keep that in mind. That's it's a little bit flipped here um because I was doing

**[46:19]** bit flipped here um because I was doing

**[46:19]** bit flipped here um because I was doing this on the fly. And you can see the

**[46:21]** this on the fly. And you can see the

**[46:21]** this on the fly. And you can see the score of experiment number two, uh which

**[46:25]** score of experiment number two, uh which

**[46:25]** score of experiment number two, uh which is our prompt A, which was the prompt we

**[46:27]** is our prompt A, which was the prompt we

**[46:27]** is our prompt A, which was the prompt we didn't change, didn't offer a discount

**[46:29]** didn't change, didn't offer a discount

**[46:29]** didn't change, didn't offer a discount to any users based on this eval label.

**[46:33]** to any users based on this eval label.

**[46:33]** to any users based on this eval label. and the LLM still graded that response

**[46:35]** and the LLM still graded that response

**[46:35]** and the LLM still graded that response as friendly, which is kind of

**[46:37]** as friendly, which is kind of

**[46:37]** as friendly, which is kind of interesting. It was like, "Oh, that was

**[46:38]** interesting. It was like, "Oh, that was

**[46:38]** interesting. It was like, "Oh, that was a friendly response." Um, I don't know

**[46:41]** a friendly response." Um, I don't know

**[46:41]** a friendly response." Um, I don't know if I agree with that actually

**[46:42]** if I agree with that actually

**[46:42]** if I agree with that actually personally, and we're gonna go in and

**[46:43]** personally, and we're gonna go in and

**[46:43]** personally, and we're gonna go in and tweet that. And then you can see that

**[46:45]** tweet that. And then you can see that

**[46:45]** tweet that. And then you can see that when we added that prompt, that line to

**[46:47]** when we added that prompt, that line to

**[46:47]** when we added that prompt, that line to the prompt, which was offer an offer a

**[46:50]** the prompt, which was offer an offer a

**[46:50]** the prompt, which was offer an offer a discount if the user gives their email,

**[46:52]** discount if the user gives their email,

**[46:52]** discount if the user gives their email, the the eval actually picked up on that

**[46:55]** the the eval actually picked up on that

**[46:55]** the the eval actually picked up on that and said that a 100% of our examples

**[46:57]** and said that a 100% of our examples

**[46:57]** and said that a 100% of our examples when the when we made this change

**[46:59]** when the when we made this change

**[46:59]** when the when we made this change actually have an offer of a discount. So


### [47:00 - 48:00]

**[47:01]** actually have an offer of a discount. So

**[47:01]** actually have an offer of a discount. So we I mean I didn't even have to go into

**[47:03]** we I mean I didn't even have to go into

**[47:03]** we I mean I didn't even have to go into each example to get that score. That's

**[47:05]** each example to get that score. That's

**[47:05]** each example to get that score. That's what the the LLM as a judge system kind

**[47:08]** what the the LLM as a judge system kind

**[47:08]** what the the LLM as a judge system kind of offers you. Um we can go in and trust

**[47:12]** of offers you. Um we can go in and trust

**[47:12]** of offers you. Um we can go in and trust you know I would say this is like a

**[47:13]** you know I would say this is like a

**[47:13]** you know I would say this is like a trust but verify. Go in and actually

**[47:15]** trust but verify. Go in and actually

**[47:15]** trust but verify. Go in and actually take a look at one of these and see what

**[47:18]** take a look at one of these and see what

**[47:18]** take a look at one of these and see what is the explanation of friendly. So to

**[47:21]** is the explanation of friendly. So to

**[47:21]** is the explanation of friendly. So to determine whether the text is friendly

**[47:23]** determine whether the text is friendly

**[47:23]** determine whether the text is friendly or robotic. So one thing you want to you

**[47:25]** or robotic. So one thing you want to you

**[47:25]** or robotic. So one thing you want to you you want to think about when you have an

**[47:26]** you want to think about when you have an

**[47:26]** you want to think about when you have an eval system is are you able to

**[47:29]** eval system is are you able to

**[47:29]** eval system is are you able to understand why the LLM as a judge gave a

**[47:32]** understand why the LLM as a judge gave a

**[47:32]** understand why the LLM as a judge gave a score. So this is like one of those like

**[47:34]** score. So this is like one of those like

**[47:34]** score. So this is like one of those like light bulb takeaway moments of of the

**[47:36]** light bulb takeaway moments of of the

**[47:36]** light bulb takeaway moments of of the talk is always think about can you

**[47:38]** talk is always think about can you

**[47:38]** talk is always think about can you explain what the LLM as a judge is doing

**[47:41]** explain what the LLM as a judge is doing

**[47:41]** explain what the LLM as a judge is doing and we actually generate explanations as

**[47:43]** and we actually generate explanations as

**[47:43]** and we actually generate explanations as part of our evals. So you can see the

**[47:45]** part of our evals. So you can see the

**[47:45]** part of our evals. So you can see the explanation is sort of the reasoning of

**[47:47]** explanation is sort of the reasoning of

**[47:47]** explanation is sort of the reasoning of that judge that says to determine

**[47:49]** that judge that says to determine

**[47:49]** that judge that says to determine whether the text is friendly or robotic,

**[47:51]** whether the text is friendly or robotic,

**[47:51]** whether the text is friendly or robotic, we need to analyze the language, tone,

**[47:53]** we need to analyze the language, tone,

**[47:53]** we need to analyze the language, tone, and style of the writing. And so it kind

**[47:55]** and style of the writing. And so it kind

**[47:55]** and style of the writing. And so it kind of does all of this analysis to

**[47:56]** of does all of this analysis to

**[47:56]** of does all of this analysis to basically say, "Yeah, this LLM is

**[47:59]** basically say, "Yeah, this LLM is

**[47:59]** basically say, "Yeah, this LLM is friendly and it's not robotic."


### [48:00 - 49:00]

**[48:02]** friendly and it's not robotic."

**[48:02]** friendly and it's not robotic." Again, I'm not really sure I agree with

**[48:04]** Again, I'm not really sure I agree with

**[48:04]** Again, I'm not really sure I agree with that explanation, right? Like I I don't

**[48:06]** that explanation, right? Like I I don't

**[48:06]** that explanation, right? Like I I don't think that that's correct. I I I still

**[48:08]** think that that's correct. I I I still

**[48:08]** think that that's correct. I I I still feel like the original prompt was pretty

**[48:11]** feel like the original prompt was pretty

**[48:11]** feel like the original prompt was pretty robotic. it was pretty, you know, kind

**[48:13]** robotic. it was pretty, you know, kind

**[48:13]** robotic. it was pretty, you know, kind of long in a lot of ways. And so I want

**[48:15]** of long in a lot of ways. And so I want

**[48:15]** of long in a lot of ways. And so I want to go in and actually be able to improve

**[48:18]** to go in and actually be able to improve

**[48:18]** to go in and actually be able to improve on my LLM as a judge system from the

**[48:21]** on my LLM as a judge system from the

**[48:21]** on my LLM as a judge system from the same the same platform. So what we can

**[48:24]** same the same platform. So what we can

**[48:24]** same the same platform. So what we can do is actually take that same data set

**[48:27]** do is actually take that same data set

**[48:27]** do is actually take that same data set and in the AISE platform you or your

**[48:30]** and in the AISE platform you or your

**[48:30]** and in the AISE platform you or your team of subject matter experts can

**[48:32]** team of subject matter experts can

**[48:32]** team of subject matter experts can actually label data in the same place

**[48:34]** actually label data in the same place

**[48:34]** actually label data in the same place and when you apply the label on the data

**[48:36]** and when you apply the label on the data

**[48:36]** and when you apply the label on the data set on on you know in the labeling queue

**[48:39]** set on on you know in the labeling queue

**[48:39]** set on on you know in the labeling queue part of the platform it applies back to

**[48:41]** part of the platform it applies back to

**[48:41]** part of the platform it applies back to the original data set. So you can

**[48:43]** the original data set. So you can

**[48:43]** the original data set. So you can actually use that for comparing the LLM

**[48:46]** actually use that for comparing the LLM

**[48:46]** actually use that for comparing the LLM as a judge with the human label. So I've

**[48:48]** as a judge with the human label. So I've

**[48:48]** as a judge with the human label. So I've actually went ahead and did that. Um,

**[48:50]** actually went ahead and did that. Um,

**[48:50]** actually went ahead and did that. Um, yeah, I did this before the talk, but I

**[48:52]** yeah, I did this before the talk, but I

**[48:52]** yeah, I did this before the talk, but I went in for each example and I was like,

**[48:54]** went in for each example and I was like,

**[48:54]** went in for each example and I was like, you know what? This this to me is

**[48:56]** you know what? This this to me is

**[48:56]** you know what? This this to me is robotic. Like, I I don't think that this

**[48:58]** robotic. Like, I I don't think that this

**[48:58]** robotic. Like, I I don't think that this is a very friendly response. I think

**[48:59]** is a very friendly response. I think


### [49:00 - 50:00]

**[49:00]** is a very friendly response. I think it's really long. It sounds like I'm

**[49:01]** it's really long. It sounds like I'm

**[49:01]** it's really long. It sounds like I'm talking to an LLM. And so, I actually

**[49:03]** talking to an LLM. And so, I actually

**[49:04]** talking to an LLM. And so, I actually applied this label on the data set for

**[49:06]** applied this label on the data set for

**[49:06]** applied this label on the data set for for the examples I wanted to go in and

**[49:08]** for the examples I wanted to go in and

**[49:08]** for the examples I wanted to go in and improve on.

**[49:11]** improve on.

**[49:11]** improve on. If I go back to the data set,

**[49:19]** you'll actually see that label is

**[49:19]** you'll actually see that label is applied here. So, if I kind of click

**[49:21]** applied here. So, if I kind of click

**[49:22]** applied here. So, if I kind of click that,

**[49:23]** that,

**[49:23]** that, move over. Sorry, it's a little bit over

**[49:26]** move over. Sorry, it's a little bit over

**[49:26]** move over. Sorry, it's a little bit over on the side here because there's a lot

**[49:27]** on the side here because there's a lot

**[49:27]** on the side here because there's a lot of data, but you can see these are the

**[49:28]** of data, but you can see these are the

**[49:28]** of data, but you can see these are the human labels I put. So, these are the

**[49:30]** human labels I put. So, these are the

**[49:30]** human labels I put. So, these are the same annotations that I just provided in

**[49:33]** same annotations that I just provided in

**[49:33]** same annotations that I just provided in the queue. They're applied on my data

**[49:35]** the queue. They're applied on my data

**[49:35]** the queue. They're applied on my data set here.

**[49:40]** >> Exactly. Exactly. You need evals for

**[49:40]** >> Exactly. Exactly. You need evals for your evals. You cannot get away from

**[49:42]** your evals. You cannot get away from

**[49:42]** your evals. You cannot get away from from You can't just trust the system,

**[49:44]** from You can't just trust the system,

**[49:44]** from You can't just trust the system, right? We know LM hallucinate. We put

**[49:46]** right? We know LM hallucinate. We put

**[49:46]** right? We know LM hallucinate. We put them into our agents. The agents

**[49:47]** them into our agents. The agents

**[49:47]** them into our agents. The agents hallucinate. Okay, we use an agent to

**[49:49]** hallucinate. Okay, we use an agent to

**[49:49]** hallucinate. Okay, we use an agent to fix that. But we can't trust that agent

**[49:51]** fix that. But we can't trust that agent

**[49:51]** fix that. But we can't trust that agent either, right? You need to have human

**[49:52]** either, right? You need to have human

**[49:52]** either, right? You need to have human labels on top of that. So, but again,

**[49:55]** labels on top of that. So, but again,

**[49:55]** labels on top of that. So, but again, I'm not going to vibe code this thing

**[49:57]** I'm not going to vibe code this thing

**[49:57]** I'm not going to vibe code this thing and be like, is this is the LLM as a


### [50:00 - 51:00]

**[50:00]** and be like, is this is the LLM as a

**[50:00]** and be like, is this is the LLM as a judge good or not? I need eval for that,

**[50:02]** judge good or not? I need eval for that,

**[50:02]** judge good or not? I need eval for that, too. And we offer two eval to help you

**[50:05]** too. And we offer two eval to help you

**[50:05]** too. And we offer two eval to help you with this. We have a code evaluator

**[50:07]** with this. We have a code evaluator

**[50:07]** with this. We have a code evaluator which can do a simple match like think

**[50:09]** which can do a simple match like think

**[50:09]** which can do a simple match like think of this as like a string check or a reg

**[50:12]** of this as like a string check or a reg

**[50:12]** of this as like a string check or a reg x or some other type of like contains.

**[50:14]** x or some other type of like contains.

**[50:14]** x or some other type of like contains. So you can actually go in and if you're

**[50:16]** So you can actually go in and if you're

**[50:16]** So you can actually go in and if you're technical and you're a PM and you want

**[50:18]** technical and you're a PM and you want

**[50:18]** technical and you're a PM and you want to write uh you know you can get Claude

**[50:20]** to write uh you know you can get Claude

**[50:20]** to write uh you know you can get Claude to help you write the eval here, but

**[50:22]** to help you write the eval here, but

**[50:22]** to help you write the eval here, but it's really just a really fast like

**[50:23]** it's really just a really fast like

**[50:23]** it's really just a really fast like Python function. Um in my case, I wrote

**[50:26]** Python function. Um in my case, I wrote

**[50:26]** Python function. Um in my case, I wrote a quick uh eval that actually does a

**[50:28]** a quick uh eval that actually does a

**[50:28]** a quick uh eval that actually does a match. And this match is it this is like

**[50:31]** match. And this match is it this is like

**[50:31]** match. And this match is it this is like a really quick and dirty eval. I would

**[50:33]** a really quick and dirty eval. I would

**[50:33]** a really quick and dirty eval. I would not say this is like best practice at

**[50:35]** not say this is like best practice at

**[50:35]** not say this is like best practice at all, but it's basically check if the

**[50:37]** all, but it's basically check if the

**[50:37]** all, but it's basically check if the eval label matches the annotation label.

**[50:40]** eval label matches the annotation label.

**[50:40]** eval label matches the annotation label. Oh, whoops.

**[50:42]** Oh, whoops.

**[50:42]** Oh, whoops. An output only match or no match. So,

**[50:45]** An output only match or no match. So,

**[50:45]** An output only match or no match. So, what this is doing is actually checking

**[50:47]** what this is doing is actually checking

**[50:47]** what this is doing is actually checking the human label against the eval label

**[50:50]** the human label against the eval label

**[50:50]** the human label against the eval label and saying do they agree or disagree.

**[50:52]** and saying do they agree or disagree.

**[50:52]** and saying do they agree or disagree. So, that's that's basically what we're

**[50:54]** So, that's that's basically what we're

**[50:54]** So, that's that's basically what we're going to run and we're I'm using an LLM

**[50:55]** going to run and we're I'm using an LLM

**[50:56]** going to run and we're I'm using an LLM as a judge. You could use code as well.

**[50:57]** as a judge. You could use code as well.

**[50:57]** as a judge. You could use code as well. You don't have to use an LM as a judge

**[50:59]** You don't have to use an LM as a judge

**[50:59]** You don't have to use an LM as a judge here, but we're going to go ahead and


### [51:00 - 52:00]

**[51:01]** here, but we're going to go ahead and

**[51:01]** here, but we're going to go ahead and run that now on the same data set, the

**[51:03]** run that now on the same data set, the

**[51:03]** run that now on the same data set, the same experiments we just ran it on.

**[51:19]** Okay, what do we got here? So you can

**[51:19]** Okay, what do we got here? So you can see here I actually take a look at that

**[51:21]** see here I actually take a look at that

**[51:22]** see here I actually take a look at that same experiment where this was where the

**[51:25]** same experiment where this was where the

**[51:25]** same experiment where this was where the um it said that the LLM as a judge was

**[51:27]** um it said that the LLM as a judge was

**[51:27]** um it said that the LLM as a judge was friendly or robotic. And you can see

**[51:29]** friendly or robotic. And you can see

**[51:29]** friendly or robotic. And you can see here that 100% of the time the match uh

**[51:33]** here that 100% of the time the match uh

**[51:33]** here that 100% of the time the match uh actually sorry this eval was actually

**[51:35]** actually sorry this eval was actually

**[51:35]** actually sorry this eval was actually actually let me let me go in one level

**[51:36]** actually let me let me go in one level

**[51:36]** actually let me let me go in one level deeper. Actually I'm going to check my

**[51:37]** deeper. Actually I'm going to check my

**[51:37]** deeper. Actually I'm going to check my own work. This eval was on the discount.

**[51:40]** own work. This eval was on the discount.

**[51:40]** own work. This eval was on the discount. So forget about that. We're going to

**[51:42]** So forget about that. We're going to

**[51:42]** So forget about that. We're going to we're going to check on the the friendly

**[51:44]** we're going to check on the the friendly

**[51:44]** we're going to check on the the friendly field actually. So this one is friendly

**[51:46]** field actually. So this one is friendly

**[51:46]** field actually. So this one is friendly label. So let me rerun that one. And

**[51:48]** label. So let me rerun that one. And

**[51:48]** label. So let me rerun that one. And we're going to think of this as match

**[51:50]** we're going to think of this as match

**[51:50]** we're going to think of this as match friendly. You can run eval as much as

**[51:51]** friendly. You can run eval as much as

**[51:52]** friendly. You can run eval as much as you want on on your data sets and

**[51:53]** you want on on your data sets and

**[51:53]** you want on on your data sets and experiments like you know. Yeah.

**[51:57]** experiments like you know. Yeah.

**[51:57]** experiments like you know. Yeah. >> Does the tool support pipelining? So as

**[51:59]** >> Does the tool support pipelining? So as

**[51:59]** >> Does the tool support pipelining? So as basically push the code.


### [52:00 - 53:00]

**[52:00]** basically push the code.

**[52:00]** basically push the code. >> Yeah, exactly. Yeah, we do support uh

**[52:02]** >> Yeah, exactly. Yeah, we do support uh

**[52:02]** >> Yeah, exactly. Yeah, we do support uh all of the eval

**[52:09]** the screen the the ways to run the code

**[52:09]** the screen the the ways to run the code on uh either a data set locally or being

**[52:11]** on uh either a data set locally or being

**[52:11]** on uh either a data set locally or being able to push code to the platform to run

**[52:13]** able to push code to the platform to run

**[52:13]** able to push code to the platform to run the eval. So programmatic on both ways.

**[52:16]** the eval. So programmatic on both ways.

**[52:16]** the eval. So programmatic on both ways. Yeah. Yeah. of course. So you can pull

**[52:17]** Yeah. Yeah. of course. So you can pull

**[52:17]** Yeah. Yeah. of course. So you can pull in data sets, pull them out as well.

**[52:20]** in data sets, pull them out as well.

**[52:20]** in data sets, pull them out as well. Okay, let's take another look at this.

**[52:22]** Okay, let's take another look at this.

**[52:22]** Okay, let's take another look at this. So this is the friendly match. So this

**[52:24]** So this is the friendly match. So this

**[52:24]** So this is the friendly match. So this you can see is pretty useful, right?

**[52:26]** you can see is pretty useful, right?

**[52:26]** you can see is pretty useful, right? This means that my LLM as a judge

**[52:30]** This means that my LLM as a judge

**[52:30]** This means that my LLM as a judge basically doesn't agree with my human

**[52:33]** basically doesn't agree with my human

**[52:33]** basically doesn't agree with my human label for friendliness almost at all.

**[52:36]** label for friendliness almost at all.

**[52:36]** label for friendliness almost at all. Right? There's like one example I think

**[52:37]** Right? There's like one example I think

**[52:37]** Right? There's like one example I think that that's in there and we can go in

**[52:39]** that that's in there and we can go in

**[52:39]** that that's in there and we can go in and take a look at it. But what we're

**[52:40]** and take a look at it. But what we're

**[52:40]** and take a look at it. But what we're really kind of seeing is that this is an

**[52:42]** really kind of seeing is that this is an

**[52:42]** really kind of seeing is that this is an area where we actually want the team to

**[52:44]** area where we actually want the team to

**[52:44]** area where we actually want the team to go take a look at our eval label and

**[52:48]** go take a look at our eval label and

**[52:48]** go take a look at our eval label and say, "Hey, can we improve on the eval

**[52:50]** say, "Hey, can we improve on the eval

**[52:50]** say, "Hey, can we improve on the eval label itself because it's not matching

**[52:52]** label itself because it's not matching

**[52:52]** label itself because it's not matching the human label." And so when you have

**[52:54]** the human label." And so when you have

**[52:54]** the human label." And so when you have these systems in place as an AIPM to be

**[52:57]** these systems in place as an AIPM to be

**[52:57]** these systems in place as an AIPM to be able to check the eval label with your

**[52:59]** able to check the eval label with your

**[52:59]** able to check the eval label with your human label, you have a lot of leverage


### [53:00 - 54:00]

**[53:02]** human label, you have a lot of leverage

**[53:02]** human label, you have a lot of leverage to go back to your team and say, "We

**[53:04]** to go back to your team and say, "We

**[53:04]** to go back to your team and say, "We need to go and improve on our eval

**[53:05]** need to go and improve on our eval

**[53:05]** need to go and improve on our eval system. It it's not working the way we

**[53:07]** system. It it's not working the way we

**[53:07]** system. It it's not working the way we expect it to." So you're actually

**[53:09]** expect it to." So you're actually

**[53:09]** expect it to." So you're actually performing the act of like checking the

**[53:11]** performing the act of like checking the

**[53:11]** performing the act of like checking the greater and you're doing it at scale. So

**[53:13]** greater and you're doing it at scale. So

**[53:13]** greater and you're doing it at scale. So you're doing it on multiple hundreds of

**[53:14]** you're doing it on multiple hundreds of

**[53:14]** you're doing it on multiple hundreds of examples or thousands of examples. So

**[53:17]** examples or thousands of examples. So

**[53:17]** examples or thousands of examples. So that's really you know I think someone

**[53:19]** that's really you know I think someone

**[53:19]** that's really you know I think someone asked earlier like how do you trust the

**[53:20]** asked earlier like how do you trust the

**[53:20]** asked earlier like how do you trust the system? I think you trust these LLM as a

**[53:23]** system? I think you trust these LLM as a

**[53:23]** system? I think you trust these LLM as a judge systems by having multiple checks

**[53:25]** judge systems by having multiple checks

**[53:25]** judge systems by having multiple checks and balances in place which is humans

**[53:27]** and balances in place which is humans

**[53:27]** and balances in place which is humans and then LLMs then humans and LMS. Um uh

**[53:31]** and then LLMs then humans and LMS. Um uh

**[53:31]** and then LLMs then humans and LMS. Um uh we'll come back to a question in just a

**[53:32]** we'll come back to a question in just a

**[53:32]** we'll come back to a question in just a moment. I just want to get to this next

**[53:33]** moment. I just want to get to this next

**[53:33]** moment. I just want to get to this next part and then we'll um we'll kind of

**[53:35]** part and then we'll um we'll kind of

**[53:35]** part and then we'll um we'll kind of come back to some Q&A. Um,

**[53:39]** come back to some Q&A. Um,

**[53:39]** come back to some Q&A. Um, okay. So, this is actually kind of kind

**[53:42]** okay. So, this is actually kind of kind

**[53:42]** okay. So, this is actually kind of kind of wrapping up towards the end of the

**[53:43]** of wrapping up towards the end of the

**[53:43]** of wrapping up towards the end of the workshop and then we'll open the rest of

**[53:45]** workshop and then we'll open the rest of

**[53:45]** workshop and then we'll open the rest of the time up for for Q&A. So, looking

**[53:48]** the time up for for Q&A. So, looking

**[53:48]** the time up for for Q&A. So, looking ahead, I think what's fundamentally

**[53:49]** ahead, I think what's fundamentally

**[53:49]** ahead, I think what's fundamentally changing is, you know, we've kind of

**[53:52]** changing is, you know, we've kind of

**[53:52]** changing is, you know, we've kind of gone through this example of changing

**[53:55]** gone through this example of changing

**[53:55]** gone through this example of changing the prompt, changing the context,

**[53:57]** the prompt, changing the context,

**[53:57]** the prompt, changing the context, creating a data set, running an eval,

**[53:59]** creating a data set, running an eval,

**[53:59]** creating a data set, running an eval, labeling the data set, and then running


### [54:00 - 55:00]

**[54:01]** labeling the data set, and then running

**[54:01]** labeling the data set, and then running another eval on top of that. And it's

**[54:04]** another eval on top of that. And it's

**[54:04]** another eval on top of that. And it's it's a lot to process, right? Like if

**[54:07]** it's a lot to process, right? Like if

**[54:07]** it's a lot to process, right? Like if you're building agent-based systems,

**[54:09]** you're building agent-based systems,

**[54:09]** you're building agent-based systems, your team is probably expecting, you

**[54:10]** your team is probably expecting, you

**[54:10]** your team is probably expecting, you know, well, where does the AIP PM fit

**[54:12]** know, well, where does the AIP PM fit

**[54:12]** know, well, where does the AIP PM fit in? And I think that that's really

**[54:15]** in? And I think that that's really

**[54:15]** in? And I think that that's really important to think about like you

**[54:16]** important to think about like you

**[54:16]** important to think about like you ultimately control the end outcome of

**[54:18]** ultimately control the end outcome of

**[54:18]** ultimately control the end outcome of the product. So whatever you can do to

**[54:21]** the product. So whatever you can do to

**[54:21]** the product. So whatever you can do to shift that into making it better is

**[54:23]** shift that into making it better is

**[54:23]** shift that into making it better is really what you want to think about

**[54:24]** really what you want to think about

**[54:24]** really what you want to think about yourself. And I I kind of view eval like

**[54:27]** yourself. And I I kind of view eval like

**[54:27]** yourself. And I I kind of view eval like the new type of requirement stock. So

**[54:30]** the new type of requirement stock. So

**[54:30]** the new type of requirement stock. So imagine if you could go to your

**[54:31]** imagine if you could go to your

**[54:31]** imagine if you could go to your engineering team and instead of giving

**[54:32]** engineering team and instead of giving

**[54:32]** engineering team and instead of giving them a PRD, you give them an eval as

**[54:35]** them a PRD, you give them an eval as

**[54:35]** them a PRD, you give them an eval as requirements and here's the eval data

**[54:37]** requirements and here's the eval data

**[54:37]** requirements and here's the eval data set and here's the eval we want to use

**[54:39]** set and here's the eval we want to use

**[54:39]** set and here's the eval we want to use to test the system as an acceptance

**[54:41]** to test the system as an acceptance

**[54:41]** to test the system as an acceptance criteria. So I think that that's really

**[54:43]** criteria. So I think that that's really

**[54:43]** criteria. So I think that that's really powerful to think about as like eval as

**[54:45]** powerful to think about as like eval as

**[54:45]** powerful to think about as like eval as a way to check and balance uh the team

**[54:47]** a way to check and balance uh the team

**[54:47]** a way to check and balance uh the team as a whole. Um and that's a little bit

**[54:50]** as a whole. Um and that's a little bit

**[54:50]** as a whole. Um and that's a little bit about what we do. We we want to build a

**[54:52]** about what we do. We we want to build a

**[54:52]** about what we do. We we want to build a single unified platform for you to run

**[54:54]** single unified platform for you to run

**[54:54]** single unified platform for you to run observability to evaluate and ultimately

**[54:57]** observability to evaluate and ultimately

**[54:57]** observability to evaluate and ultimately develop these workflows with your team

**[54:59]** develop these workflows with your team

**[54:59]** develop these workflows with your team in the same platform. We've built for


### [55:00 - 56:00]

**[55:01]** in the same platform. We've built for

**[55:01]** in the same platform. We've built for you know many customers like Uber,

**[55:03]** you know many customers like Uber,

**[55:03]** you know many customers like Uber, Reddit, Instacart, all these like kind

**[55:05]** Reddit, Instacart, all these like kind

**[55:05]** Reddit, Instacart, all these like kind of very techforward companies. Um we

**[55:07]** of very techforward companies. Um we

**[55:07]** of very techforward companies. Um we actually just received investment from

**[55:08]** actually just received investment from

**[55:08]** actually just received investment from Data Dog and Microsoft as well. So we're

**[55:11]** Data Dog and Microsoft as well. So we're

**[55:11]** Data Dog and Microsoft as well. So we're a series C company. We're sort of the

**[55:12]** a series C company. We're sort of the

**[55:12]** a series C company. We're sort of the furthest along in the space. And the

**[55:15]** furthest along in the space. And the

**[55:15]** furthest along in the space. And the whole goal that we want to build is give

**[55:16]** whole goal that we want to build is give

**[55:16]** whole goal that we want to build is give you a suite of tools to be able to go

**[55:19]** you a suite of tools to be able to go

**[55:19]** you a suite of tools to be able to go from development through to production

**[55:21]** from development through to production

**[55:21]** from development through to production with your AI engineering team and for

**[55:23]** with your AI engineering team and for

**[55:23]** with your AI engineering team and for PMs to go in and use the same tools. Um,

**[55:26]** PMs to go in and use the same tools. Um,

**[55:26]** PMs to go in and use the same tools. Um, and then super quick before Q&A, uh,

**[55:28]** and then super quick before Q&A, uh,

**[55:28]** and then super quick before Q&A, uh, please scan the QR code if you are in

**[55:31]** please scan the QR code if you are in

**[55:31]** please scan the QR code if you are in San Francisco on June 25th. We're

**[55:33]** San Francisco on June 25th. We're

**[55:33]** San Francisco on June 25th. We're actually hosting a conference uh, around

**[55:36]** actually hosting a conference uh, around

**[55:36]** actually hosting a conference uh, around eval. And it's going to be it's going to

**[55:38]** eval. And it's going to be it's going to

**[55:38]** eval. And it's going to be it's going to be a ton of fun. We actually have some

**[55:39]** be a ton of fun. We actually have some

**[55:39]** be a ton of fun. We actually have some great AI PMs and researchers joining

**[55:42]** great AI PMs and researchers joining

**[55:42]** great AI PMs and researchers joining from companies like OpenAI, uh,

**[55:44]** from companies like OpenAI, uh,

**[55:44]** from companies like OpenAI, uh, Anthropic. And what's really cool is

**[55:47]** Anthropic. And what's really cool is

**[55:47]** Anthropic. And what's really cool is we're actually offering for this room,

**[55:49]** we're actually offering for this room,

**[55:49]** we're actually offering for this room, um, a free sort of exclusive, uh, free,

**[55:52]** um, a free sort of exclusive, uh, free,

**[55:52]** um, a free sort of exclusive, uh, free, uh, ticket for entry. Uh, the the prices

**[55:54]** uh, ticket for entry. Uh, the the prices

**[55:54]** uh, ticket for entry. Uh, the the prices actually went up yesterday. So, because,

**[55:56]** actually went up yesterday. So, because,

**[55:56]** actually went up yesterday. So, because, you know, we're huge fans of AI Engineer

**[55:58]** you know, we're huge fans of AI Engineer

**[55:58]** you know, we're huge fans of AI Engineer World Fair, we wanted to give you all an


### [56:00 - 57:00]

**[56:00]** World Fair, we wanted to give you all an

**[56:00]** World Fair, we wanted to give you all an opportunity to join for free if you're

**[56:01]** opportunity to join for free if you're

**[56:01]** opportunity to join for free if you're in town. Um, so would love to see you

**[56:04]** in town. Um, so would love to see you

**[56:04]** in town. Um, so would love to see you there. Um, and yeah, you can scan for a

**[56:05]** there. Um, and yeah, you can scan for a

**[56:05]** there. Um, and yeah, you can scan for a free code.

**[56:07]** free code.

**[56:07]** free code. And yeah, that's a little bit um of of

**[56:09]** And yeah, that's a little bit um of of

**[56:09]** And yeah, that's a little bit um of of the workshop. I would love any

**[56:11]** the workshop. I would love any

**[56:11]** the workshop. I would love any questions. Yeah. And uh the ask for the

**[56:13]** questions. Yeah. And uh the ask for the

**[56:13]** questions. Yeah. And uh the ask for the questions, as the the person in the back

**[56:15]** questions, as the the person in the back

**[56:15]** questions, as the the person in the back just reminded me, if you wouldn't mind

**[56:17]** just reminded me, if you wouldn't mind

**[56:17]** just reminded me, if you wouldn't mind lining up for questions on the mic so

**[56:19]** lining up for questions on the mic so

**[56:19]** lining up for questions on the mic so that the camera can pick it up and then

**[56:21]** that the camera can pick it up and then

**[56:21]** that the camera can pick it up and then we can just kind of go down the line and

**[56:22]** we can just kind of go down the line and

**[56:22]** we can just kind of go down the line and do some questions there. Um, that'd be

**[56:24]** do some questions there. Um, that'd be

**[56:24]** do some questions there. Um, that'd be awesome. Thank you.

**[56:25]** awesome. Thank you.

**[56:25]** awesome. Thank you. >> So, thank you so much.

**[56:26]** >> So, thank you so much.

**[56:26]** >> So, thank you so much. >> Please give your name and

**[56:27]** >> Please give your name and

**[56:27]** >> Please give your name and >> Yeah, my name is Roman. Thank you so

**[56:29]** >> Yeah, my name is Roman. Thank you so

**[56:29]** >> Yeah, my name is Roman. Thank you so much. It was like an awesome walk

**[56:30]** much. It was like an awesome walk

**[56:30]** much. It was like an awesome walk through. Uh would you mind share some

**[56:34]** through. Uh would you mind share some

**[56:34]** through. Uh would you mind share some like your experience on building um

**[56:37]** like your experience on building um

**[56:37]** like your experience on building um evaluation teams? Should I start with

**[56:40]** evaluation teams? Should I start with

**[56:40]** evaluation teams? Should I start with hiring kind of dedicated person with a

**[56:43]** hiring kind of dedicated person with a

**[56:43]** hiring kind of dedicated person with a experience or should I rely on product

**[56:45]** experience or should I rely on product

**[56:45]** experience or should I rely on product manager a product manager and walk

**[56:47]** manager a product manager and walk

**[56:47]** manager a product manager and walk through this like a what's the best way

**[56:49]** through this like a what's the best way

**[56:50]** through this like a what's the best way >> best practices? So the the gentleman

**[56:51]** >> best practices? So the the gentleman

**[56:51]** >> best practices? So the the gentleman asked um what's the best practices for

**[56:53]** asked um what's the best practices for

**[56:53]** asked um what's the best practices for building an eval team? Um, can I

**[56:56]** building an eval team? Um, can I

**[56:56]** building an eval team? Um, can I actually ask a follow-up question

**[56:57]** actually ask a follow-up question

**[56:57]** actually ask a follow-up question because I'm curious like what is your

**[56:58]** because I'm curious like what is your

**[56:58]** because I'm curious like what is your role in the company right now just just


### [57:00 - 58:00]

**[57:00]** role in the company right now just just

**[57:00]** role in the company right now just just for myself to know?

**[57:01]** for myself to know?

**[57:01]** for myself to know? >> I'm head of product.

**[57:02]** >> I'm head of product.

**[57:02]** >> I'm head of product. >> You're head of product. Okay, perfect.

**[57:03]** >> You're head of product. Okay, perfect.

**[57:03]** >> You're head of product. Okay, perfect. So, this is exactly this is a question I

**[57:05]** So, this is exactly this is a question I

**[57:05]** So, this is exactly this is a question I get actually very often which is how do

**[57:08]** get actually very often which is how do

**[57:08]** get actually very often which is how do I hire my first AIPM? How do I hire an

**[57:10]** I hire my first AIPM? How do I hire an

**[57:10]** I hire my first AIPM? How do I hire an AI engineer? How do I know if I need an

**[57:12]** AI engineer? How do I know if I need an

**[57:12]** AI engineer? How do I know if I need an AIPM or an engineer? So, I think uh

**[57:15]** AIPM or an engineer? So, I think uh

**[57:15]** AIPM or an engineer? So, I think uh there's there's a couple steps to this

**[57:17]** there's there's a couple steps to this

**[57:17]** there's there's a couple steps to this answer. One is as head of product. Um, I

**[57:20]** answer. One is as head of product. Um, I

**[57:20]** answer. One is as head of product. Um, I do think we see a lot of heads of

**[57:22]** do think we see a lot of heads of

**[57:22]** do think we see a lot of heads of product actually in the platform are

**[57:25]** product actually in the platform are

**[57:25]** product actually in the platform are like ourselves actually getting their

**[57:27]** like ourselves actually getting their

**[57:27]** like ourselves actually getting their hands dirty for the first pass because

**[57:29]** hands dirty for the first pass because

**[57:29]** hands dirty for the first pass because at the end of the day, if you're like

**[57:30]** at the end of the day, if you're like

**[57:30]** at the end of the day, if you're like hiring someone to do something, you

**[57:32]** hiring someone to do something, you

**[57:32]** hiring someone to do something, you should probably know what they're going

**[57:33]** should probably know what they're going

**[57:33]** should probably know what they're going to do. And so my job on my team is to

**[57:36]** to do. And so my job on my team is to

**[57:36]** to do. And so my job on my team is to make the product accessible for

**[57:38]** make the product accessible for

**[57:38]** make the product accessible for executives and heads of product to

**[57:39]** executives and heads of product to

**[57:40]** executives and heads of product to understand what's going on. So we have a

**[57:42]** understand what's going on. So we have a

**[57:42]** understand what's going on. So we have a lot of kind of capabilities around

**[57:44]** lot of kind of capabilities around

**[57:44]** lot of kind of capabilities around dashboards, making everything no code,

**[57:46]** dashboards, making everything no code,

**[57:46]** dashboards, making everything no code, low code. But my recommendation is to

**[57:49]** low code. But my recommendation is to

**[57:49]** low code. But my recommendation is to feel the pain yourself of writing evals

**[57:52]** feel the pain yourself of writing evals

**[57:52]** feel the pain yourself of writing evals and realizing how what is hard about

**[57:55]** and realizing how what is hard about

**[57:55]** and realizing how what is hard about that so that you know how to structure

**[57:57]** that so that you know how to structure

**[57:57]** that so that you know how to structure interview questions for an engineer or a

**[57:59]** interview questions for an engineer or a

**[57:59]** interview questions for an engineer or a PM because I don't know what's hard


### [58:00 - 59:00]

**[58:01]** PM because I don't know what's hard

**[58:01]** PM because I don't know what's hard about your eval workflow, right? I only

**[58:04]** about your eval workflow, right? I only

**[58:04]** about your eval workflow, right? I only know that there's challenges around

**[58:05]** know that there's challenges around

**[58:05]** know that there's challenges around writing eval general and so I would

**[58:08]** writing eval general and so I would

**[58:08]** writing eval general and so I would recommend that you like feel the pain

**[58:09]** recommend that you like feel the pain

**[58:09]** recommend that you like feel the pain firsthand and then uh you'll kind of get

**[58:12]** firsthand and then uh you'll kind of get

**[58:12]** firsthand and then uh you'll kind of get a good sense of how to how to tease that

**[58:14]** a good sense of how to how to tease that

**[58:14]** a good sense of how to how to tease that out of your interviewing pipeline. Um

**[58:16]** out of your interviewing pipeline. Um

**[58:16]** out of your interviewing pipeline. Um but good good question. Yeah.

**[58:18]** but good good question. Yeah.

**[58:18]** but good good question. Yeah. >> Yeah.

**[58:19]** >> Yeah.

**[58:19]** >> Yeah. >> Um yeah the example you know we just

**[58:21]** >> Um yeah the example you know we just

**[58:21]** >> Um yeah the example you know we just looked at obviously our eval was pretty

**[58:23]** looked at obviously our eval was pretty

**[58:23]** looked at obviously our eval was pretty bad when you you know compare it to the

**[58:25]** bad when you you know compare it to the

**[58:25]** bad when you you know compare it to the human labels. Yeah.

**[58:26]** human labels. Yeah.

**[58:26]** human labels. Yeah. >> So like from here what do you do next?

**[58:28]** >> So like from here what do you do next?

**[58:28]** >> So like from here what do you do next? Like what's the next step to try to

**[58:30]** Like what's the next step to try to

**[58:30]** Like what's the next step to try to improve the prompting for your your main

**[58:32]** improve the prompting for your your main

**[58:32]** improve the prompting for your your main eval to get closer to the human labels?

**[58:35]** eval to get closer to the human labels?

**[58:35]** eval to get closer to the human labels? >> Yeah. Good question. So if I had um more

**[58:38]** >> Yeah. Good question. So if I had um more

**[58:38]** >> Yeah. Good question. So if I had um more if if I was like here working on this in

**[58:41]** if if I was like here working on this in

**[58:41]** if if I was like here working on this in in real life, what you would actually do

**[58:44]** in real life, what you would actually do

**[58:44]** in real life, what you would actually do is take that eval prompt and go through

**[58:47]** is take that eval prompt and go through

**[58:47]** is take that eval prompt and go through a similar workflow of what we just did

**[58:49]** a similar workflow of what we just did

**[58:49]** a similar workflow of what we just did for prompt iteration for the original

**[58:51]** for prompt iteration for the original

**[58:51]** for prompt iteration for the original prompt. So again like um that eval

**[58:53]** prompt. So again like um that eval

**[58:53]** prompt. So again like um that eval prompt we see here

**[58:56]** prompt we see here

**[58:56]** prompt we see here I could go in take this and redefine

**[58:59]** I could go in take this and redefine

**[58:59]** I could go in take this and redefine parts of the workflow to basically say


### [59:00 - 01:00:00]

**[59:01]** parts of the workflow to basically say

**[59:01]** parts of the workflow to basically say you know what uh be really strict about

**[59:04]** you know what uh be really strict about

**[59:04]** you know what uh be really strict about what is friendly here are I didn't add

**[59:06]** what is friendly here are I didn't add

**[59:06]** what is friendly here are I didn't add any few shot examples right I didn't

**[59:08]** any few shot examples right I didn't

**[59:08]** any few shot examples right I didn't specify here's examples of friendly text

**[59:10]** specify here's examples of friendly text

**[59:10]** specify here's examples of friendly text here's examples of robots so that's like

**[59:12]** here's examples of robots so that's like

**[59:12]** here's examples of robots so that's like a a clear gap in my eval today that if I

**[59:15]** a a clear gap in my eval today that if I

**[59:15]** a a clear gap in my eval today that if I were looking at this I could apply best

**[59:17]** were looking at this I could apply best

**[59:17]** were looking at this I could apply best practices and improve on it we also have

**[59:19]** practices and improve on it we also have

**[59:20]** practices and improve on it we also have um in the product we have some workflow

**[59:22]** um in the product we have some workflow

**[59:22]** um in the product we have some workflow around actually helping you write eval.

**[59:24]** around actually helping you write eval.

**[59:24]** around actually helping you write eval. So this is this is our product but like

**[59:26]** So this is this is our product but like

**[59:26]** So this is this is our product but like you don't have to use our product for

**[59:27]** you don't have to use our product for

**[59:28]** you don't have to use our product for this. Uh you can use any any product.

**[59:30]** this. Uh you can use any any product.

**[59:30]** this. Uh you can use any any product. I'm going to show kind of an iteration

**[59:31]** I'm going to show kind of an iteration

**[59:31]** I'm going to show kind of an iteration on top of this which is how how we have

**[59:34]** on top of this which is how how we have

**[59:34]** on top of this which is how how we have users actually building eval prompts. So

**[59:36]** users actually building eval prompts. So

**[59:36]** users actually building eval prompts. So I could say write me a prompt

**[59:40]** I could say write me a prompt

**[59:40]** I could say write me a prompt to detect friendly or robotic text. And

**[59:46]** to detect friendly or robotic text. And

**[59:46]** to detect friendly or robotic text. And this is actually using our own co-pilot

**[59:48]** this is actually using our own co-pilot

**[59:48]** this is actually using our own co-pilot in the product. So, we've built a

**[59:50]** in the product. So, we've built a

**[59:50]** in the product. So, we've built a co-pilot that understands best practices

**[59:53]** co-pilot that understands best practices

**[59:53]** co-pilot that understands best practices uh and actually can kind of help you

**[59:55]** uh and actually can kind of help you

**[59:55]** uh and actually can kind of help you write that first prompt, get it off of

**[59:57]** write that first prompt, get it off of

**[59:57]** write that first prompt, get it off of the ground. You can also take the same

**[59:59]** the ground. You can also take the same

**[59:59]** the ground. You can also take the same prompt, which it just generated in like


### [01:00:00 - 01:01:00]

**[01:00:02]** prompt, which it just generated in like

**[01:00:02]** prompt, which it just generated in like 1 second, and take that back to the

**[01:00:04]** 1 second, and take that back to the

**[01:00:04]** 1 second, and take that back to the prompt playground and iterate on further

**[01:00:06]** prompt playground and iterate on further

**[01:00:06]** prompt playground and iterate on further from here. So, let's let's go ahead and

**[01:00:08]** from here. So, let's let's go ahead and

**[01:00:08]** from here. So, let's let's go ahead and do that on the fly really quick. I've

**[01:00:10]** do that on the fly really quick. I've

**[01:00:10]** do that on the fly really quick. I've got a prompt in here, and I can go in

**[01:00:11]** got a prompt in here, and I can go in

**[01:00:11]** got a prompt in here, and I can go in and actually ask the pro the co-pilot to

**[01:00:13]** and actually ask the pro the co-pilot to

**[01:00:14]** and actually ask the pro the co-pilot to optimize this prompt. So, um, let's go

**[01:00:17]** optimize this prompt. So, um, let's go

**[01:00:17]** optimize this prompt. So, um, let's go ahead and

**[01:00:19]** ahead and

**[01:00:19]** ahead and say make it

**[01:00:22]** say make it

**[01:00:22]** say make it stricter.

**[01:00:25]** stricter.

**[01:00:25]** stricter. So, I can actually use an a an LLM agent

**[01:00:27]** So, I can actually use an a an LLM agent

**[01:00:28]** So, I can actually use an a an LLM agent and and copilot agent. Um, just kind of

**[01:00:30]** and and copilot agent. Um, just kind of

**[01:00:30]** and and copilot agent. Um, just kind of note that like you really want AI

**[01:00:32]** note that like you really want AI

**[01:00:32]** note that like you really want AI workflows on top to help you like

**[01:00:34]** workflows on top to help you like

**[01:00:34]** workflows on top to help you like rewrite the prompt, add more examples,

**[01:00:36]** rewrite the prompt, add more examples,

**[01:00:36]** rewrite the prompt, add more examples, and then rerun eval on that new prompt.

**[01:00:38]** and then rerun eval on that new prompt.

**[01:00:38]** and then rerun eval on that new prompt. So it's more it's less about like you're

**[01:00:40]** So it's more it's less about like you're

**[01:00:40]** So it's more it's less about like you're you're definitely not going to get it

**[01:00:42]** you're definitely not going to get it

**[01:00:42]** you're definitely not going to get it right on the first try, but being able

**[01:00:44]** right on the first try, but being able

**[01:00:44]** right on the first try, but being able to iterate is really what's important.

**[01:00:47]** to iterate is really what's important.

**[01:00:47]** to iterate is really what's important. And that's really what we underscore is

**[01:00:49]** And that's really what we underscore is

**[01:00:49]** And that's really what we underscore is like it might take you like five or 10

**[01:00:50]** like it might take you like five or 10

**[01:00:50]** like it might take you like five or 10 tries to get an eval that matches your

**[01:00:53]** tries to get an eval that matches your

**[01:00:53]** tries to get an eval that matches your human labels and that's okay because

**[01:00:55]** human labels and that's okay because

**[01:00:55]** human labels and that's okay because these systems are really complex. Um and

**[01:00:57]** these systems are really complex. Um and

**[01:00:57]** these systems are really complex. Um and it's just important about having the

**[01:00:58]** it's just important about having the

**[01:00:58]** it's just important about having the right workflow in place. So yeah.


### [01:01:00 - 01:02:00]

**[01:01:02]** right workflow in place. So yeah.

**[01:01:02]** right workflow in place. So yeah. >> Hi, I'm Joti. Um, does Arise also um

**[01:01:06]** >> Hi, I'm Joti. Um, does Arise also um

**[01:01:06]** >> Hi, I'm Joti. Um, does Arise also um allow for model based evaluations like

**[01:01:08]** allow for model based evaluations like

**[01:01:08]** allow for model based evaluations like using BERT or Alberta to be able rather

**[01:01:11]** using BERT or Alberta to be able rather

**[01:01:11]** using BERT or Alberta to be able rather than just LLM as a judge, but I can use

**[01:01:13]** than just LLM as a judge, but I can use

**[01:01:13]** than just LLM as a judge, but I can use like BERT or Alberta to like figure out

**[01:01:15]** like BERT or Alberta to like figure out

**[01:01:15]** like BERT or Alberta to like figure out like a prediction score?

**[01:01:16]** like a prediction score?

**[01:01:16]** like a prediction score? >> Yeah, good question. So, we're actually

**[01:01:19]** >> Yeah, good question. So, we're actually

**[01:01:19]** >> Yeah, good question. So, we're actually really um the short answer is yes, we do

**[01:01:21]** really um the short answer is yes, we do

**[01:01:21]** really um the short answer is yes, we do offer versions of that. Let me show you

**[01:01:23]** offer versions of that. Let me show you

**[01:01:23]** offer versions of that. Let me show you what I mean by that though. So, um so

**[01:01:25]** what I mean by that though. So, um so

**[01:01:25]** what I mean by that though. So, um so when we go into Arise, you can actually

**[01:01:28]** when we go into Arise, you can actually

**[01:01:28]** when we go into Arise, you can actually set up any uh eval model you want here.

**[01:01:31]** set up any uh eval model you want here.

**[01:01:31]** set up any uh eval model you want here. So you see we have OpenAI, Azure,

**[01:01:33]** So you see we have OpenAI, Azure,

**[01:01:33]** So you see we have OpenAI, Azure, Google, but you can add a custom model

**[01:01:36]** Google, but you can add a custom model

**[01:01:36]** Google, but you can add a custom model endpoint as well. So you can basically

**[01:01:38]** endpoint as well. So you can basically

**[01:01:38]** endpoint as well. So you can basically this will structure that request as a

**[01:01:40]** this will structure that request as a

**[01:01:40]** this will structure that request as a chat completion but we can make it any

**[01:01:42]** chat completion but we can make it any

**[01:01:42]** chat completion but we can make it any arbitrary API if you needed to and you

**[01:01:44]** arbitrary API if you needed to and you

**[01:01:44]** arbitrary API if you needed to and you can say like BERT model and whatever the

**[01:01:46]** can say like BERT model and whatever the

**[01:01:46]** can say like BERT model and whatever the name of your endpoint is point it to

**[01:01:48]** name of your endpoint is point it to

**[01:01:48]** name of your endpoint is point it to that and you'll be able to reference

**[01:01:50]** that and you'll be able to reference

**[01:01:50]** that and you'll be able to reference that model in the eval generator too. So

**[01:01:52]** that model in the eval generator too. So

**[01:01:52]** that model in the eval generator too. So this is um so I can just put test here

**[01:01:55]** this is um so I can just put test here

**[01:01:55]** this is um so I can just put test here kind of move to the next flow. Um, and

**[01:01:58]** kind of move to the next flow. Um, and

**[01:01:58]** kind of move to the next flow. Um, and you'll see when I go into here, I can


### [01:02:00 - 01:03:00]

**[01:02:00]** you'll see when I go into here, I can

**[01:02:00]** you'll see when I go into here, I can use any model provider I want. So, the

**[01:02:02]** use any model provider I want. So, the

**[01:02:02]** use any model provider I want. So, the short answer is yeah, you can generate a

**[01:02:04]** short answer is yeah, you can generate a

**[01:02:04]** short answer is yeah, you can generate a score with any model. Yeah.

**[01:02:07]** score with any model. Yeah.

**[01:02:07]** score with any model. Yeah. >> Cool.

**[01:02:10]** >> Cool.

**[01:02:10]** >> Cool. >> Okay. Um, oh, we got one more question,

**[01:02:12]** >> Okay. Um, oh, we got one more question,

**[01:02:12]** >> Okay. Um, oh, we got one more question, I think. Or sorry, we have more

**[01:02:14]** I think. Or sorry, we have more

**[01:02:14]** I think. Or sorry, we have more questions. Yeah, go for it.

**[01:02:15]** questions. Yeah, go for it.

**[01:02:15]** questions. Yeah, go for it. >> Going to go ahead and try to get this

**[01:02:17]** >> Going to go ahead and try to get this

**[01:02:17]** >> Going to go ahead and try to get this one in. Um, so I think like probably a

**[01:02:20]** one in. Um, so I think like probably a

**[01:02:20]** one in. Um, so I think like probably a lot of the people that have built apps

**[01:02:22]** lot of the people that have built apps

**[01:02:22]** lot of the people that have built apps are thinking a similar thing or maybe

**[01:02:24]** are thinking a similar thing or maybe

**[01:02:24]** are thinking a similar thing or maybe this is a bit naive, but if you had

**[01:02:28]** this is a bit naive, but if you had

**[01:02:28]** this is a bit naive, but if you had humanlabeled information already, right,

**[01:02:30]** humanlabeled information already, right,

**[01:02:30]** humanlabeled information already, right, and you're seeing a bad match on the

**[01:02:32]** and you're seeing a bad match on the

**[01:02:32]** and you're seeing a bad match on the friendliness score, am I to assume that

**[01:02:35]** friendliness score, am I to assume that

**[01:02:35]** friendliness score, am I to assume that you'd be trying to get that score up

**[01:02:37]** you'd be trying to get that score up

**[01:02:37]** you'd be trying to get that score up higher and then extrapolate to more uh

**[01:02:42]** higher and then extrapolate to more uh

**[01:02:42]** higher and then extrapolate to more uh cases going forward? And you're assuming

**[01:02:44]** cases going forward? And you're assuming

**[01:02:44]** cases going forward? And you're assuming that that sampling holds across like the

**[01:02:46]** that that sampling holds across like the

**[01:02:46]** that that sampling holds across like the broader set. Yeah.

**[01:02:47]** broader set. Yeah.

**[01:02:47]** broader set. Yeah. >> So like because that relationship is

**[01:02:48]** >> So like because that relationship is

**[01:02:48]** >> So like because that relationship is unclear to me.

**[01:02:49]** unclear to me.

**[01:02:49]** unclear to me. >> Very very good question. So um so

**[01:02:52]** >> Very very good question. So um so

**[01:02:52]** >> Very very good question. So um so basically one way to reframe this is

**[01:02:54]** basically one way to reframe this is

**[01:02:54]** basically one way to reframe this is like how do I know that my data set is

**[01:02:57]** like how do I know that my data set is

**[01:02:57]** like how do I know that my data set is representative of my overall data to

**[01:02:59]** representative of my overall data to

**[01:02:59]** representative of my overall data to some degree.


### [01:03:00 - 01:04:00]

**[01:03:00]** some degree.

**[01:03:00]** some degree. >> Sure. Or as it shifts over time or

**[01:03:01]** >> Sure. Or as it shifts over time or

**[01:03:01]** >> Sure. Or as it shifts over time or >> as it shifts. Yeah. Totally. So um so

**[01:03:04]** >> as it shifts. Yeah. Totally. So um so

**[01:03:04]** >> as it shifts. Yeah. Totally. So um so that's a really uh really good point. In

**[01:03:05]** that's a really uh really good point. In

**[01:03:06]** that's a really uh really good point. In the product what we we don't have this

**[01:03:07]** the product what we we don't have this

**[01:03:08]** the product what we we don't have this yet but it's coming out like in the next

**[01:03:09]** yet but it's coming out like in the next

**[01:03:09]** yet but it's coming out like in the next week. will have an a workflow to help

**[01:03:12]** week. will have an a workflow to help

**[01:03:12]** week. will have an a workflow to help you add data to your data set

**[01:03:14]** you add data to your data set

**[01:03:14]** you add data to your data set continuously using labels that you might

**[01:03:16]** continuously using labels that you might

**[01:03:16]** continuously using labels that you might have. So you could say like is you know

**[01:03:19]** have. So you could say like is you know

**[01:03:19]** have. So you could say like is you know one thing we didn't really talk about is

**[01:03:20]** one thing we didn't really talk about is

**[01:03:20]** one thing we didn't really talk about is like how to evaluate production data but

**[01:03:23]** like how to evaluate production data but

**[01:03:23]** like how to evaluate production data but you can actually run these eval not just

**[01:03:25]** you can actually run these eval not just

**[01:03:25]** you can actually run these eval not just on a data set but on all data that comes

**[01:03:27]** on a data set but on all data that comes

**[01:03:27]** on a data set but on all data that comes into your project over time to make it

**[01:03:29]** into your project over time to make it

**[01:03:29]** into your project over time to make it automatically label and classify uh you

**[01:03:32]** automatically label and classify uh you

**[01:03:32]** automatically label and classify uh you know any production data. So you could

**[01:03:34]** know any production data. So you could

**[01:03:34]** know any production data. So you could use that to keep building your data set

**[01:03:35]** use that to keep building your data set

**[01:03:36]** use that to keep building your data set of like is this an example we've seen

**[01:03:37]** of like is this an example we've seen

**[01:03:37]** of like is this an example we've seen before or not or is this uh you know

**[01:03:40]** before or not or is this uh you know

**[01:03:40]** before or not or is this uh you know think of this as like a way for you to

**[01:03:42]** think of this as like a way for you to

**[01:03:42]** think of this as like a way for you to sample at a larger scale essentially on

**[01:03:44]** sample at a larger scale essentially on

**[01:03:44]** sample at a larger scale essentially on production

**[01:03:44]** production

**[01:03:44]** production >> and that is a suggested workflow that

**[01:03:46]** >> and that is a suggested workflow that

**[01:03:46]** >> and that is a suggested workflow that you continuously sample and human label

**[01:03:48]** you continuously sample and human label

**[01:03:48]** you continuously sample and human label sum

**[01:03:49]** sum

**[01:03:49]** sum >> to check the matching over time.

**[01:03:51]** >> to check the matching over time.

**[01:03:51]** >> to check the matching over time. >> Exactly. And you can basically go in and

**[01:03:53]** >> Exactly. And you can basically go in and

**[01:03:53]** >> Exactly. And you can basically go in and see like okay where human labels don't

**[01:03:55]** see like okay where human labels don't

**[01:03:55]** see like okay where human labels don't agree with LLM on this on production

**[01:03:58]** agree with LLM on this on production

**[01:03:58]** agree with LLM on this on production data then you might want to add those to

**[01:03:59]** data then you might want to add those to


### [01:04:00 - 01:05:00]

**[01:04:00]** data then you might want to add those to your data set as hard examples. Sure.

**[01:04:02]** your data set as hard examples. Sure.

**[01:04:02]** your data set as hard examples. Sure. >> And we actually are going to build into

**[01:04:04]** >> And we actually are going to build into

**[01:04:04]** >> And we actually are going to build into this product as well a way for you to

**[01:04:06]** this product as well a way for you to

**[01:04:06]** this product as well a way for you to qualify is this example a hard example

**[01:04:08]** qualify is this example a hard example

**[01:04:08]** qualify is this example a hard example as well using LLM confidence score.

**[01:04:11]** as well using LLM confidence score.

**[01:04:11]** as well using LLM confidence score. >> Okay. And and sorry just hard example

**[01:04:13]** >> Okay. And and sorry just hard example

**[01:04:13]** >> Okay. And and sorry just hard example like very strictly interpreted.

**[01:04:15]** like very strictly interpreted.

**[01:04:15]** like very strictly interpreted. >> So hard would be um hard from an eval

**[01:04:17]** >> So hard would be um hard from an eval

**[01:04:18]** >> So hard would be um hard from an eval perspective. So like is it is it

**[01:04:20]** perspective. So like is it is it

**[01:04:20]** perspective. So like is it is it friendly or not can be like borderline

**[01:04:22]** friendly or not can be like borderline

**[01:04:22]** friendly or not can be like borderline right? Like

**[01:04:22]** right? Like

**[01:04:22]** right? Like >> I see. So you're saying like uh

**[01:04:23]** >> I see. So you're saying like uh

**[01:04:23]** >> I see. So you're saying like uh subjective or

**[01:04:24]** subjective or

**[01:04:24]** subjective or >> subjective. Yeah. Exactly. So maybe to

**[01:04:27]** >> subjective. Yeah. Exactly. So maybe to

**[01:04:27]** >> subjective. Yeah. Exactly. So maybe to like recap the question a little bit,

**[01:04:28]** like recap the question a little bit,

**[01:04:28]** like recap the question a little bit, like your data set is this property

**[01:04:31]** like your data set is this property

**[01:04:31]** like your data set is this property that's going to keep changing over time.

**[01:04:34]** that's going to keep changing over time.

**[01:04:34]** that's going to keep changing over time. And you really want tools that help you

**[01:04:36]** And you really want tools that help you

**[01:04:36]** And you really want tools that help you build onto it by giving you like a

**[01:04:38]** build onto it by giving you like a

**[01:04:38]** build onto it by giving you like a golden data set of hard examples to

**[01:04:41]** golden data set of hard examples to

**[01:04:41]** golden data set of hard examples to improve on. And hard means like we're

**[01:04:43]** improve on. And hard means like we're

**[01:04:43]** improve on. And hard means like we're not really sure if we got it right or

**[01:04:44]** not really sure if we got it right or

**[01:04:44]** not really sure if we got it right or not in the first place.

**[01:04:45]** not in the first place.

**[01:04:45]** not in the first place. >> Sure. Yeah. Thanks.

**[01:04:46]** >> Sure. Yeah. Thanks.

**[01:04:46]** >> Sure. Yeah. Thanks. >> Yeah, good question.

**[01:04:51]** >> Yeah.

**[01:04:51]** >> Yeah. >> Hi, my name is Victoria Martin. Uh,

**[01:04:53]** >> Hi, my name is Victoria Martin. Uh,

**[01:04:53]** >> Hi, my name is Victoria Martin. Uh, thank you so much for the talk. One of

**[01:04:55]** thank you so much for the talk. One of

**[01:04:55]** thank you so much for the talk. One of the things that I've run into is a lot

**[01:04:56]** the things that I've run into is a lot

**[01:04:56]** the things that I've run into is a lot of like skepticism out of product

**[01:04:58]** of like skepticism out of product

**[01:04:58]** of like skepticism out of product managers that I'm working with on

**[01:04:59]** managers that I'm working with on

**[01:04:59]** managers that I'm working with on generative AI and trying to build


### [01:05:00 - 01:06:00]

**[01:05:01]** generative AI and trying to build

**[01:05:01]** generative AI and trying to build confidence in the evals that we're

**[01:05:03]** confidence in the evals that we're

**[01:05:03]** confidence in the evals that we're giving. Yeah.

**[01:05:04]** giving. Yeah.

**[01:05:04]** giving. Yeah. >> Have you been given any guidance or in

**[01:05:07]** >> Have you been given any guidance or in

**[01:05:07]** >> Have you been given any guidance or in working with other PMs guidance on like

**[01:05:08]** working with other PMs guidance on like

**[01:05:08]** working with other PMs guidance on like the total number of evals that that you

**[01:05:10]** the total number of evals that that you

**[01:05:10]** the total number of evals that that you think should be run by the time you can

**[01:05:12]** think should be run by the time you can

**[01:05:12]** think should be run by the time you can say like you can be confident in this

**[01:05:13]** say like you can be confident in this

**[01:05:13]** say like you can be confident in this evaluation set?

**[01:05:15]** evaluation set?

**[01:05:15]** evaluation set? >> Yeah, good really good question. So um

**[01:05:18]** >> Yeah, good really good question. So um

**[01:05:18]** >> Yeah, good really good question. So um so the question was like how do we know

**[01:05:21]** so the question was like how do we know

**[01:05:21]** so the question was like how do we know I think there's kind of two components

**[01:05:22]** I think there's kind of two components

**[01:05:22]** I think there's kind of two components to it. there's like quantity and quality

**[01:05:24]** to it. there's like quantity and quality

**[01:05:24]** to it. there's like quantity and quality of the eval eval like how do we know if

**[01:05:27]** of the eval eval like how do we know if

**[01:05:27]** of the eval eval like how do we know if we've run enough eval or we have enough

**[01:05:29]** we've run enough eval or we have enough

**[01:05:29]** we've run enough eval or we have enough eval and that those eval are actually

**[01:05:31]** eval and that those eval are actually

**[01:05:31]** eval and that those eval are actually good enough to kind of pick up problems

**[01:05:34]** good enough to kind of pick up problems

**[01:05:34]** good enough to kind of pick up problems in our data. Um we this is also maybe a

**[01:05:38]** in our data. Um we this is also maybe a

**[01:05:38]** in our data. Um we this is also maybe a little bit of a broker record here but I

**[01:05:39]** little bit of a broker record here but I

**[01:05:39]** little bit of a broker record here but I I would say that this is a little bit of

**[01:05:41]** I would say that this is a little bit of

**[01:05:41]** I would say that this is a little bit of iteration as well where you want to kind

**[01:05:44]** iteration as well where you want to kind

**[01:05:44]** iteration as well where you want to kind of get started with some small set of

**[01:05:47]** of get started with some small set of

**[01:05:47]** of get started with some small set of eval. So actually I have a diagram for

**[01:05:48]** eval. So actually I have a diagram for

**[01:05:48]** eval. So actually I have a diagram for this. Let me just pull that one up.

**[01:05:51]** this. Let me just pull that one up.

**[01:05:51]** this. Let me just pull that one up. So um so you'll kind of see here this is

**[01:05:55]** So um so you'll kind of see here this is

**[01:05:55]** So um so you'll kind of see here this is intended to be like a loop where you

**[01:05:57]** intended to be like a loop where you

**[01:05:57]** intended to be like a loop where you start with some in development you're


### [01:06:00 - 01:07:00]

**[01:06:00]** start with some in development you're

**[01:06:00]** start with some in development you're going to run on a CSV of data maybe like

**[01:06:02]** going to run on a CSV of data maybe like

**[01:06:02]** going to run on a CSV of data maybe like some handam like I would argue the thing

**[01:06:05]** some handam like I would argue the thing

**[01:06:05]** some handam like I would argue the thing I just built was development right like

**[01:06:07]** I just built was development right like

**[01:06:07]** I just built was development right like I have 10 examples it's not

**[01:06:09]** I have 10 examples it's not

**[01:06:09]** I have 10 examples it's not statistically significant I'm not going

**[01:06:11]** statistically significant I'm not going

**[01:06:11]** statistically significant I'm not going to get the team on board to ship this

**[01:06:12]** to get the team on board to ship this

**[01:06:12]** to get the team on board to ship this thing but what I can do is then curate

**[01:06:15]** thing but what I can do is then curate

**[01:06:15]** thing but what I can do is then curate data sets keep iterating on them keep

**[01:06:18]** data sets keep iterating on them keep

**[01:06:18]** data sets keep iterating on them keep rerunning experiments until I feel

**[01:06:20]** rerunning experiments until I feel

**[01:06:20]** rerunning experiments until I feel confident enough and the whole team is

**[01:06:22]** confident enough and the whole team is

**[01:06:22]** confident enough and the whole team is on board before I ship to production.

**[01:06:24]** on board before I ship to production.

**[01:06:24]** on board before I ship to production. And then once you're in production,

**[01:06:26]** And then once you're in production,

**[01:06:26]** And then once you're in production, you're doing that again, except that now

**[01:06:28]** you're doing that again, except that now

**[01:06:28]** you're doing that again, except that now you're doing it on production data. And

**[01:06:30]** you're doing it on production data. And

**[01:06:30]** you're doing it on production data. And then you might take some of those

**[01:06:31]** then you might take some of those

**[01:06:31]** then you might take some of those examples and throw them back into

**[01:06:33]** examples and throw them back into

**[01:06:33]** examples and throw them back into development. Let me give a tactical

**[01:06:36]** development. Let me give a tactical

**[01:06:36]** development. Let me give a tactical example of what this looks like in real

**[01:06:37]** example of what this looks like in real

**[01:06:37]** example of what this looks like in real life. With self-driving cars, when I

**[01:06:39]** life. With self-driving cars, when I

**[01:06:40]** life. With self-driving cars, when I joined Cruz, we would go down the street

**[01:06:42]** joined Cruz, we would go down the street

**[01:06:42]** joined Cruz, we would go down the street for like one block and then a driver

**[01:06:44]** for like one block and then a driver

**[01:06:44]** for like one block and then a driver would like have to take over the car,

**[01:06:46]** would like have to take over the car,

**[01:06:46]** would like have to take over the car, right? like we couldn't drop like we

**[01:06:47]** right? like we couldn't drop like we

**[01:06:47]** right? like we couldn't drop like we couldn't drive one block down the ride

**[01:06:49]** couldn't drive one block down the ride

**[01:06:49]** couldn't drive one block down the ride uh down the road. Same goes for Whimo.

**[01:06:50]** uh down the road. Same goes for Whimo.

**[01:06:50]** uh down the road. Same goes for Whimo. Um they were all kind of in this this uh

**[01:06:53]** Um they were all kind of in this this uh

**[01:06:53]** Um they were all kind of in this this uh system and then eventually we got down

**[01:06:55]** system and then eventually we got down

**[01:06:55]** system and then eventually we got down to like being able to drive down a

**[01:06:57]** to like being able to drive down a

**[01:06:57]** to like being able to drive down a straight road. Great. But the car can't

**[01:06:59]** straight road. Great. But the car can't

**[01:06:59]** straight road. Great. But the car can't just drive on straight roads, right?


### [01:07:00 - 01:08:00]

**[01:07:01]** just drive on straight roads, right?

**[01:07:01]** just drive on straight roads, right? Like it has to make a left turn. So

**[01:07:03]** Like it has to make a left turn. So

**[01:07:03]** Like it has to make a left turn. So eventually we got like fully autonomous

**[01:07:05]** eventually we got like fully autonomous

**[01:07:05]** eventually we got like fully autonomous for straight, you know, no problems on

**[01:07:08]** for straight, you know, no problems on

**[01:07:08]** for straight, you know, no problems on the road and then we had to make a left

**[01:07:09]** the road and then we had to make a left

**[01:07:09]** the road and then we had to make a left turn and then the car would, you know, a

**[01:07:11]** turn and then the car would, you know, a

**[01:07:11]** turn and then the car would, you know, a human would have to take over. So what

**[01:07:13]** human would have to take over. So what

**[01:07:13]** human would have to take over. So what we did was we built a data set of like

**[01:07:15]** we did was we built a data set of like

**[01:07:15]** we did was we built a data set of like left turns and we used that to keep

**[01:07:17]** left turns and we used that to keep

**[01:07:17]** left turns and we used that to keep improving on left turns and then

**[01:07:19]** improving on left turns and then

**[01:07:19]** improving on left turns and then eventually the car could make left turns

**[01:07:20]** eventually the car could make left turns

**[01:07:20]** eventually the car could make left turns great until a pedestrian was in the

**[01:07:22]** great until a pedestrian was in the

**[01:07:22]** great until a pedestrian was in the sidewalk and then we had to curate a

**[01:07:24]** sidewalk and then we had to curate a

**[01:07:24]** sidewalk and then we had to curate a data set of left turns with pedestrian

**[01:07:25]** data set of left turns with pedestrian

**[01:07:25]** data set of left turns with pedestrian in the sidewalk. So the answer is sort

**[01:07:28]** in the sidewalk. So the answer is sort

**[01:07:28]** in the sidewalk. So the answer is sort of like building your eval data set just

**[01:07:31]** of like building your eval data set just

**[01:07:31]** of like building your eval data set just takes time and you're not going to know

**[01:07:33]** takes time and you're not going to know

**[01:07:33]** takes time and you're not going to know what are the difficult scenarios until

**[01:07:34]** what are the difficult scenarios until

**[01:07:34]** what are the difficult scenarios until you actually encounter them. So I think

**[01:07:37]** you actually encounter them. So I think

**[01:07:37]** you actually encounter them. So I think to get to production I would recommend

**[01:07:39]** to get to production I would recommend

**[01:07:39]** to get to production I would recommend just kind of using that loop until your

**[01:07:41]** just kind of using that loop until your

**[01:07:41]** just kind of using that loop until your whole team feels confident in like this

**[01:07:43]** whole team feels confident in like this

**[01:07:43]** whole team feels confident in like this is good enough to ship and just accept

**[01:07:45]** is good enough to ship and just accept

**[01:07:45]** is good enough to ship and just accept that once you get to production you're

**[01:07:47]** that once you get to production you're

**[01:07:47]** that once you get to production you're going to find new examples to improve on

**[01:07:49]** going to find new examples to improve on

**[01:07:49]** going to find new examples to improve on um as well. So it depends a lot on your

**[01:07:51]** um as well. So it depends a lot on your

**[01:07:51]** um as well. So it depends a lot on your business as well. If you're in

**[01:07:52]** business as well. If you're in

**[01:07:52]** business as well. If you're in healthcare or legal tech you might have

**[01:07:53]** healthcare or legal tech you might have

**[01:07:54]** healthcare or legal tech you might have higher bars than if you're building a

**[01:07:55]** higher bars than if you're building a

**[01:07:55]** higher bars than if you're building a travel agent for example.

**[01:07:57]** travel agent for example.

**[01:07:57]** travel agent for example. >> Yeah. Yeah.

**[01:07:59]** >> Yeah. Yeah.

**[01:07:59]** >> Yeah. Yeah. >> Yeah.


### [01:08:00 - 01:09:00]

**[01:08:01]** >> Yeah.

**[01:08:01]** >> Yeah. >> My name is Matai. Uh I have a question.

**[01:08:04]** >> My name is Matai. Uh I have a question.

**[01:08:04]** >> My name is Matai. Uh I have a question. Uh as I understood the uh the AIS

**[01:08:08]** Uh as I understood the uh the AIS

**[01:08:08]** Uh as I understood the uh the AIS platform like it's uh working as a like

**[01:08:11]** platform like it's uh working as a like

**[01:08:11]** platform like it's uh working as a like I take the the prompt and uh you're

**[01:08:13]** I take the the prompt and uh you're

**[01:08:13]** I take the the prompt and uh you're directly sending that that prompt to a

**[01:08:16]** directly sending that that prompt to a

**[01:08:16]** directly sending that that prompt to a model, right?

**[01:08:16]** model, right?

**[01:08:16]** model, right? >> That's right. Yeah.

**[01:08:17]** >> That's right. Yeah.

**[01:08:17]** >> That's right. Yeah. >> Um

**[01:08:18]** >> Um

**[01:08:18]** >> Um >> with the context and the data.

**[01:08:19]** >> with the context and the data.

**[01:08:19]** >> with the context and the data. >> Yes, of course. Uh you said that like

**[01:08:21]** >> Yes, of course. Uh you said that like

**[01:08:21]** >> Yes, of course. Uh you said that like there is some possibility to to u port

**[01:08:24]** there is some possibility to to u port

**[01:08:24]** there is some possibility to to u port tool tools into the platform. That's

**[01:08:26]** tool tools into the platform. That's

**[01:08:26]** tool tools into the platform. That's right.

**[01:08:26]** right.

**[01:08:26]** right. >> But what about testing the whole system?

**[01:08:28]** >> But what about testing the whole system?

**[01:08:28]** >> But what about testing the whole system? Like we already have like some some uh

**[01:08:31]** Like we already have like some some uh

**[01:08:31]** Like we already have like some some uh flows that are augmentating augmenting

**[01:08:34]** flows that are augmentating augmenting

**[01:08:34]** flows that are augmentating augmenting the the the whole workflow.

**[01:08:36]** the the the whole workflow.

**[01:08:36]** the the the whole workflow. >> Yeah.

**[01:08:36]** >> Yeah.

**[01:08:36]** >> Yeah. >> Even outside of tool calls. Yeah.

**[01:08:38]** >> Even outside of tool calls. Yeah.

**[01:08:38]** >> Even outside of tool calls. Yeah. >> And like uh they're quite important into

**[01:08:41]** >> And like uh they're quite important into

**[01:08:41]** >> And like uh they're quite important into how the actual output will look like in

**[01:08:43]** how the actual output will look like in

**[01:08:43]** how the actual output will look like in the end. Uh is there any way to uh run

**[01:08:46]** the end. Uh is there any way to uh run

**[01:08:46]** the end. Uh is there any way to uh run those evaluations on a on a like a

**[01:08:49]** those evaluations on a on a like a

**[01:08:49]** those evaluations on a on a like a custom runner like that would actually

**[01:08:51]** custom runner like that would actually

**[01:08:51]** custom runner like that would actually call our system on our data set that uh

**[01:08:54]** call our system on our data set that uh

**[01:08:54]** call our system on our data set that uh goes through everything that we have.

**[01:08:56]** goes through everything that we have.

**[01:08:56]** goes through everything that we have. >> Find me after this. We should chat. uh

**[01:08:57]** >> Find me after this. We should chat. uh

**[01:08:57]** >> Find me after this. We should chat. uh is the short answer for that one. Um we

**[01:08:59]** is the short answer for that one. Um we


### [01:09:00 - 01:10:00]

**[01:09:00]** is the short answer for that one. Um we have some tools and systems like that in

**[01:09:01]** have some tools and systems like that in

**[01:09:01]** have some tools and systems like that in place like the tool calling that you

**[01:09:03]** place like the tool calling that you

**[01:09:03]** place like the tool calling that you saw, but for endtoend agents, we're

**[01:09:05]** saw, but for endtoend agents, we're

**[01:09:05]** saw, but for endtoend agents, we're actually building some stuff out and

**[01:09:06]** actually building some stuff out and

**[01:09:06]** actually building some stuff out and would love to chat with you about that.

**[01:09:08]** would love to chat with you about that.

**[01:09:08]** would love to chat with you about that. Good question. We'll I'll find you after

**[01:09:09]** Good question. We'll I'll find you after

**[01:09:09]** Good question. We'll I'll find you after this.

**[01:09:10]** this.

**[01:09:10]** this. >> Yeah.

**[01:09:12]** >> Yeah.

**[01:09:12]** >> Yeah. >> Yeah, of course. So back to your left

**[01:09:14]** >> Yeah, of course. So back to your left

**[01:09:14]** >> Yeah, of course. So back to your left turn example as well as just talking

**[01:09:17]** turn example as well as just talking

**[01:09:17]** turn example as well as just talking about the transition of like PRDS to

**[01:09:19]** about the transition of like PRDS to

**[01:09:19]** about the transition of like PRDS to like eval what is the life cycle of like

**[01:09:22]** like eval what is the life cycle of like

**[01:09:22]** like eval what is the life cycle of like feature development look like and kind

**[01:09:24]** feature development look like and kind

**[01:09:24]** feature development look like and kind of the relationship I feel like of the

**[01:09:26]** of the relationship I feel like of the

**[01:09:26]** of the relationship I feel like of the feature but also with your team in terms

**[01:09:28]** feature but also with your team in terms

**[01:09:28]** feature but also with your team in terms of ownership accountability all of that.

**[01:09:31]** of ownership accountability all of that.

**[01:09:31]** of ownership accountability all of that. >> Yeah.

**[01:09:31]** >> Yeah.

**[01:09:31]** >> Yeah. >> Yeah. So good question. So I feel like

**[01:09:34]** >> Yeah. So good question. So I feel like

**[01:09:34]** >> Yeah. So good question. So I feel like how do you work with AI engineers in

**[01:09:36]** how do you work with AI engineers in

**[01:09:36]** how do you work with AI engineers in this new world is kind of interesting

**[01:09:37]** this new world is kind of interesting

**[01:09:37]** this new world is kind of interesting not the subject of this talk but it is

**[01:09:39]** not the subject of this talk but it is

**[01:09:39]** not the subject of this talk but it is it is like a very relevant relevant

**[01:09:41]** it is like a very relevant relevant

**[01:09:41]** it is like a very relevant relevant question that um you know would h

**[01:09:43]** question that um you know would h

**[01:09:43]** question that um you know would h happily chat more on too. So there's two

**[01:09:46]** happily chat more on too. So there's two

**[01:09:46]** happily chat more on too. So there's two answers to it that that come to mind.

**[01:09:47]** answers to it that that come to mind.

**[01:09:48]** answers to it that that come to mind. One is that development cycles have

**[01:09:49]** One is that development cycles have

**[01:09:49]** One is that development cycles have gotten a lot faster. Um like the the way

**[01:09:53]** gotten a lot faster. Um like the the way

**[01:09:53]** gotten a lot faster. Um like the the way at which these models are progressing

**[01:09:54]** at which these models are progressing

**[01:09:54]** at which these models are progressing and these systems are progressing like

**[01:09:57]** and these systems are progressing like

**[01:09:57]** and these systems are progressing like going from prototype to production is


### [01:10:00 - 01:11:00]

**[01:10:00]** going from prototype to production is

**[01:10:00]** going from prototype to production is actually even faster than it ever has

**[01:10:01]** actually even faster than it ever has

**[01:10:02]** actually even faster than it ever has been. Um, so that's one note which I can

**[01:10:05]** been. Um, so that's one note which I can

**[01:10:05]** been. Um, so that's one note which I can just tell you as a personal observation.

**[01:10:07]** just tell you as a personal observation.

**[01:10:07]** just tell you as a personal observation. We we feel that we can go from an idea

**[01:10:10]** We we feel that we can go from an idea

**[01:10:10]** We we feel that we can go from an idea to an updated prompt to shipping that

**[01:10:13]** to an updated prompt to shipping that

**[01:10:13]** to an updated prompt to shipping that prompt in like a span of a day of

**[01:10:15]** prompt in like a span of a day of

**[01:10:15]** prompt in like a span of a day of testing which is I think like unheard of

**[01:10:17]** testing which is I think like unheard of

**[01:10:17]** testing which is I think like unheard of of like normal software development

**[01:10:19]** of like normal software development

**[01:10:19]** of like normal software development cycles. So that's one note which is just

**[01:10:21]** cycles. So that's one note which is just

**[01:10:21]** cycles. So that's one note which is just like the the the way that you iterate

**[01:10:23]** like the the the way that you iterate

**[01:10:23]** like the the the way that you iterate with the team has gotten a lot faster.

**[01:10:26]** with the team has gotten a lot faster.

**[01:10:26]** with the team has gotten a lot faster. Um the second the second note is uh when

**[01:10:30]** Um the second the second note is uh when

**[01:10:30]** Um the second the second note is uh when it comes to responsibilities

**[01:10:32]** it comes to responsibilities

**[01:10:32]** it comes to responsibilities I view this as

**[01:10:35]** I view this as

**[01:10:35]** I view this as if you you're kind of a product manager

**[01:10:37]** if you you're kind of a product manager

**[01:10:37]** if you you're kind of a product manager is the keeper of the end product

**[01:10:39]** is the keeper of the end product

**[01:10:40]** is the keeper of the end product experience. So if that means um making

**[01:10:42]** experience. So if that means um making

**[01:10:42]** experience. So if that means um making sure the eval are in a good place and

**[01:10:44]** sure the eval are in a good place and

**[01:10:44]** sure the eval are in a good place and the team has human labels to improve on

**[01:10:47]** the team has human labels to improve on

**[01:10:47]** the team has human labels to improve on that's like a very solid area for a

**[01:10:49]** that's like a very solid area for a

**[01:10:49]** that's like a very solid area for a product manager to focus is like making

**[01:10:51]** product manager to focus is like making

**[01:10:51]** product manager to focus is like making sure the data is in a good spot for the

**[01:10:53]** sure the data is in a good spot for the

**[01:10:53]** sure the data is in a good spot for the rest of your your development team. I

**[01:10:55]** rest of your your development team. I

**[01:10:55]** rest of your your development team. I think at the same time, you know, I'm a

**[01:10:57]** think at the same time, you know, I'm a

**[01:10:58]** think at the same time, you know, I'm a PM on the team and I'm like writing some


### [01:11:00 - 01:12:00]

**[01:11:00]** PM on the team and I'm like writing some

**[01:11:00]** PM on the team and I'm like writing some of the stuff in cursor. And so being

**[01:11:02]** of the stuff in cursor. And so being

**[01:11:02]** of the stuff in cursor. And so being able to go in and actually talk to the

**[01:11:04]** able to go in and actually talk to the

**[01:11:04]** able to go in and actually talk to the the code base itself using one of these

**[01:11:07]** the code base itself using one of these

**[01:11:07]** the code base itself using one of these models, I think that that's starting to

**[01:11:09]** models, I think that that's starting to

**[01:11:09]** models, I think that that's starting to become more of an expectation of AI

**[01:11:11]** become more of an expectation of AI

**[01:11:11]** become more of an expectation of AI product managers is to be literate in

**[01:11:13]** product managers is to be literate in

**[01:11:13]** product managers is to be literate in the code and be able to use these tools.

**[01:11:15]** the code and be able to use these tools.

**[01:11:15]** the code and be able to use these tools. I I really this is like after this I'm

**[01:11:17]** I I really this is like after this I'm

**[01:11:17]** I I really this is like after this I'm just going to go back and like try to

**[01:11:18]** just going to go back and like try to

**[01:11:18]** just going to go back and like try to fix the thing that I broke earlier,

**[01:11:20]** fix the thing that I broke earlier,

**[01:11:20]** fix the thing that I broke earlier, right? And and the way the way the

**[01:11:21]** right? And and the way the way the

**[01:11:22]** right? And and the way the way the reason I'm able to do that is because

**[01:11:23]** reason I'm able to do that is because

**[01:11:23]** reason I'm able to do that is because the way I'm prompting the system is not

**[01:11:26]** the way I'm prompting the system is not

**[01:11:26]** the way I'm prompting the system is not very sophisticated. Like I asked it

**[01:11:27]** very sophisticated. Like I asked it

**[01:11:28]** very sophisticated. Like I asked it yesterday, can you make a script that

**[01:11:30]** yesterday, can you make a script that

**[01:11:30]** yesterday, can you make a script that generates itineraries on top of the

**[01:11:31]** generates itineraries on top of the

**[01:11:31]** generates itineraries on top of the server? I need like 15 examples and it

**[01:11:33]** server? I need like 15 examples and it

**[01:11:33]** server? I need like 15 examples and it just did that, right? And like that like

**[01:11:36]** just did that, right? And like that like

**[01:11:36]** just did that, right? And like that like wouldn't have been possible. So I think

**[01:11:38]** wouldn't have been possible. So I think

**[01:11:38]** wouldn't have been possible. So I think PMs are responsible for the end product

**[01:11:40]** PMs are responsible for the end product

**[01:11:40]** PMs are responsible for the end product experience, but PMs also have more

**[01:11:43]** experience, but PMs also have more

**[01:11:43]** experience, but PMs also have more leverage than they've ever had before in

**[01:11:45]** leverage than they've ever had before in

**[01:11:45]** leverage than they've ever had before in probably the entire like professional

**[01:11:47]** probably the entire like professional

**[01:11:47]** probably the entire like professional journey of product management because

**[01:11:49]** journey of product management because

**[01:11:49]** journey of product management because you're now no longer reliant on your

**[01:11:51]** you're now no longer reliant on your

**[01:11:51]** you're now no longer reliant on your engineering team to ship that thing that

**[01:11:53]** engineering team to ship that thing that

**[01:11:53]** engineering team to ship that thing that you wanted. Like you can just go do it.

**[01:11:55]** you wanted. Like you can just go do it.

**[01:11:55]** you wanted. Like you can just go do it. Um should you go do it is another

**[01:11:57]** Um should you go do it is another

**[01:11:57]** Um should you go do it is another question, but uh and that's something

**[01:11:59]** question, but uh and that's something

**[01:11:59]** question, but uh and that's something that's a discussion that you should have


### [01:12:00 - 01:13:00]

**[01:12:00]** that's a discussion that you should have

**[01:12:00]** that's a discussion that you should have with your team. But the fact is that you

**[01:12:02]** with your team. But the fact is that you

**[01:12:02]** with your team. But the fact is that you can go do it now, which was not the case

**[01:12:05]** can go do it now, which was not the case

**[01:12:05]** can go do it now, which was not the case before. And so I I kind of urge PMs to

**[01:12:08]** before. And so I I kind of urge PMs to

**[01:12:08]** before. And so I I kind of urge PMs to like push the boundaries of what people

**[01:12:10]** like push the boundaries of what people

**[01:12:10]** like push the boundaries of what people have told them the role is and should be

**[01:12:13]** have told them the role is and should be

**[01:12:13]** have told them the role is and should be and see where that takes you. And so the

**[01:12:15]** and see where that takes you. And so the

**[01:12:16]** and see where that takes you. And so the long-winded way of saying like your

**[01:12:18]** long-winded way of saying like your

**[01:12:18]** long-winded way of saying like your mileage may vary depends on the

**[01:12:19]** mileage may vary depends on the

**[01:12:19]** mileage may vary depends on the boundaries you have with your team, but

**[01:12:20]** boundaries you have with your team, but

**[01:12:20]** boundaries you have with your team, but I'd recommend people to like redefine

**[01:12:22]** I'd recommend people to like redefine

**[01:12:22]** I'd recommend people to like redefine those at this stage.

**[01:12:24]** those at this stage.

**[01:12:24]** those at this stage. >> Yeah. Yeah.

**[01:12:25]** >> Yeah. Yeah.

**[01:12:25]** >> Yeah. Yeah. >> Yeah. jumping off that a little bit.

**[01:12:27]** >> Yeah. jumping off that a little bit.

**[01:12:27]** >> Yeah. jumping off that a little bit. It's a little off topic from this, but

**[01:12:29]** It's a little off topic from this, but

**[01:12:29]** It's a little off topic from this, but um like as a product manager who wants

**[01:12:31]** um like as a product manager who wants

**[01:12:31]** um like as a product manager who wants to move to be more technical like as I'm

**[01:12:34]** to move to be more technical like as I'm

**[01:12:34]** to move to be more technical like as I'm working with AI engineers.

**[01:12:36]** working with AI engineers.

**[01:12:36]** working with AI engineers. >> Yeah.

**[01:12:37]** >> Yeah.

**[01:12:37]** >> Yeah. >> What does that look like? Like I'm in an

**[01:12:38]** >> What does that look like? Like I'm in an

**[01:12:38]** >> What does that look like? Like I'm in an or where I have very limited access to

**[01:12:40]** or where I have very limited access to

**[01:12:40]** or where I have very limited access to the codebase. So like I use cursor to

**[01:12:42]** the codebase. So like I use cursor to

**[01:12:42]** the codebase. So like I use cursor to write Python for data things, but like I

**[01:12:44]** write Python for data things, but like I

**[01:12:44]** write Python for data things, but like I don't necessarily have access to like

**[01:12:46]** don't necessarily have access to like

**[01:12:46]** don't necessarily have access to like start interrogating the code, understand

**[01:12:48]** start interrogating the code, understand

**[01:12:48]** start interrogating the code, understand that. So, I'd love just if you have

**[01:12:49]** that. So, I'd love just if you have

**[01:12:50]** that. So, I'd love just if you have suggestions or thoughts on like what how

**[01:12:52]** suggestions or thoughts on like what how

**[01:12:52]** suggestions or thoughts on like what how to evolve as a PM, but also like maybe

**[01:12:54]** to evolve as a PM, but also like maybe

**[01:12:54]** to evolve as a PM, but also like maybe move my company culture in that

**[01:12:56]** move my company culture in that

**[01:12:56]** move my company culture in that direction.

**[01:12:57]** direction.

**[01:12:57]** direction. >> Yeah, that's that's t like how actually


### [01:13:00 - 01:14:00]

**[01:13:00]** >> Yeah, that's that's t like how actually

**[01:13:00]** >> Yeah, that's that's t like how actually I have a followup question. That's okay.

**[01:13:02]** I have a followup question. That's okay.

**[01:13:02]** I have a followup question. That's okay. Just cuz I'm going to pull people in the

**[01:13:03]** Just cuz I'm going to pull people in the

**[01:13:03]** Just cuz I'm going to pull people in the room like how big is the company? And

**[01:13:05]** room like how big is the company? And

**[01:13:05]** room like how big is the company? And you don't have to share the name if you

**[01:13:06]** you don't have to share the name if you

**[01:13:06]** you don't have to share the name if you don't want to, but just curious like the

**[01:13:07]** don't want to, but just curious like the

**[01:13:07]** don't want to, but just curious like the size of

**[01:13:07]** size of

**[01:13:07]** size of >> uh we're about 300 people. Okay. Um but

**[01:13:10]** >> uh we're about 300 people. Okay. Um but

**[01:13:10]** >> uh we're about 300 people. Okay. Um but the tech's probably like a third of

**[01:13:12]** the tech's probably like a third of

**[01:13:12]** the tech's probably like a third of that.

**[01:13:13]** that.

**[01:13:13]** that. >> Okay. So like almost like 100 engineers,

**[01:13:15]** >> Okay. So like almost like 100 engineers,

**[01:13:15]** >> Okay. So like almost like 100 engineers, 300 people. And um do you have any like

**[01:13:18]** 300 people. And um do you have any like

**[01:13:18]** 300 people. And um do you have any like old remnant product managers at the

**[01:13:21]** old remnant product managers at the

**[01:13:21]** old remnant product managers at the company that still have code access?

**[01:13:24]** company that still have code access?

**[01:13:24]** company that still have code access? >> No, we're like a very new team of PMS.

**[01:13:27]** >> No, we're like a very new team of PMS.

**[01:13:27]** >> No, we're like a very new team of PMS. >> Okay, cool. Okay. Well, I think um one

**[01:13:30]** >> Okay, cool. Okay. Well, I think um one

**[01:13:30]** >> Okay, cool. Okay. Well, I think um one thing we've started doing uh it's it's a

**[01:13:32]** thing we've started doing uh it's it's a

**[01:13:32]** thing we've started doing uh it's it's a really good question. Thanks for

**[01:13:33]** really good question. Thanks for

**[01:13:33]** really good question. Thanks for answering that. Um one thing we've

**[01:13:35]** answering that. Um one thing we've

**[01:13:35]** answering that. Um one thing we've started doing is trying to take a little

**[01:13:37]** started doing is trying to take a little

**[01:13:37]** started doing is trying to take a little bit of like the public forum of our

**[01:13:39]** bit of like the public forum of our

**[01:13:39]** bit of like the public forum of our company. Um sorry, I'm about to out our

**[01:13:42]** company. Um sorry, I'm about to out our

**[01:13:42]** company. Um sorry, I'm about to out our CEO who's in the back of the room.

**[01:13:44]** CEO who's in the back of the room.

**[01:13:44]** CEO who's in the back of the room. [laughter]

**[01:13:45]** [laughter]

**[01:13:45]** [laughter] Uh, so if you have any questions about

**[01:13:47]** Uh, so if you have any questions about

**[01:13:47]** Uh, so if you have any questions about our rides, he's a good guy to talk to.

**[01:13:48]** our rides, he's a good guy to talk to.

**[01:13:48]** our rides, he's a good guy to talk to. Uh, but the reason I'm out of here is

**[01:13:50]** Uh, but the reason I'm out of here is

**[01:13:50]** Uh, but the reason I'm out of here is because like I'm I missed our town hall

**[01:13:52]** because like I'm I missed our town hall

**[01:13:52]** because like I'm I missed our town hall today, but like I heard it was just

**[01:13:54]** today, but like I heard it was just

**[01:13:54]** today, but like I heard it was just basically people running like AI demos

**[01:13:56]** basically people running like AI demos

**[01:13:56]** basically people running like AI demos the whole time of like what they're

**[01:13:57]** the whole time of like what they're

**[01:13:58]** the whole time of like what they're building. And why I think that's really

**[01:13:59]** building. And why I think that's really


### [01:14:00 - 01:15:00]

**[01:14:00]** building. And why I think that's really powerful is it can get the whole company

**[01:14:02]** powerful is it can get the whole company

**[01:14:02]** powerful is it can get the whole company really catalyzed around what's possible

**[01:14:06]** really catalyzed around what's possible

**[01:14:06]** really catalyzed around what's possible because to be honest, I think it's very

**[01:14:08]** because to be honest, I think it's very

**[01:14:08]** because to be honest, I think it's very likely that, you know, most teams today

**[01:14:10]** likely that, you know, most teams today

**[01:14:10]** likely that, you know, most teams today aren't pushing the boundaries of these

**[01:14:12]** aren't pushing the boundaries of these

**[01:14:12]** aren't pushing the boundaries of these tools. And so you kind of joining this

**[01:14:14]** tools. And so you kind of joining this

**[01:14:14]** tools. And so you kind of joining this talk and seeing like how to run eval,

**[01:14:16]** talk and seeing like how to run eval,

**[01:14:16]** talk and seeing like how to run eval, how to you know what goes into

**[01:14:18]** how to you know what goes into

**[01:14:18]** how to you know what goes into experiments like being able to to kind

**[01:14:20]** experiments like being able to to kind

**[01:14:20]** experiments like being able to to kind of be the the person pushing the team

**[01:14:24]** of be the the person pushing the team

**[01:14:24]** of be the the person pushing the team forward is really powerful and I think

**[01:14:26]** forward is really powerful and I think

**[01:14:26]** forward is really powerful and I think you can do that in a way that's really

**[01:14:27]** you can do that in a way that's really

**[01:14:27]** you can do that in a way that's really collaborative. So I only I'd say like

**[01:14:30]** collaborative. So I only I'd say like

**[01:14:30]** collaborative. So I only I'd say like our job as PMs is to have influence over

**[01:14:32]** our job as PMs is to have influence over

**[01:14:32]** our job as PMs is to have influence over the team and influence product

**[01:14:33]** the team and influence product

**[01:14:33]** the team and influence product direction. I think there's an

**[01:14:35]** direction. I think there's an

**[01:14:35]** direction. I think there's an opportunity to influence the fact that

**[01:14:36]** opportunity to influence the fact that

**[01:14:36]** opportunity to influence the fact that PM should be more technical in your org

**[01:14:38]** PM should be more technical in your org

**[01:14:38]** PM should be more technical in your org and you could show them by building

**[01:14:40]** and you could show them by building

**[01:14:40]** and you could show them by building something and and impressing the rest of

**[01:14:41]** something and and impressing the rest of

**[01:14:41]** something and and impressing the rest of the team by what you build. Um so that's

**[01:14:43]** the team by what you build. Um so that's

**[01:14:44]** the team by what you build. Um so that's my advice, my personal advice there.

**[01:14:45]** my advice, my personal advice there.

**[01:14:45]** my advice, my personal advice there. Yeah.

**[01:14:46]** Yeah.

**[01:14:46]** Yeah. >> Yeah. Go for it. Yeah. [laughter]

**[01:14:48]** >> Yeah. Go for it. Yeah. [laughter]

**[01:14:48]** >> Yeah. Go for it. Yeah. [laughter] >> Actually have a question to see if it's

**[01:14:51]** >> Actually have a question to see if it's

**[01:14:51]** >> Actually have a question to see if it's possible. Uh so how [clears throat] you

**[01:14:53]** possible. Uh so how [clears throat] you

**[01:14:53]** possible. Uh so how [clears throat] you guys believe uh AI will reshape how we

**[01:14:56]** guys believe uh AI will reshape how we

**[01:14:56]** guys believe uh AI will reshape how we structure the team. So right now you

**[01:14:58]** structure the team. So right now you

**[01:14:58]** structure the team. So right now you have like I would say for instance just


### [01:15:00 - 01:16:00]

**[01:15:00]** have like I would say for instance just

**[01:15:00]** have like I would say for instance just like

**[01:15:01]** like

**[01:15:01]** like >> 10 engineers, one product manager, one

**[01:15:03]** >> 10 engineers, one product manager, one

**[01:15:03]** >> 10 engineers, one product manager, one designer and so on. So

**[01:15:05]** designer and so on. So

**[01:15:05]** designer and so on. So >> what will happen in five years? You will

**[01:15:07]** >> what will happen in five years? You will

**[01:15:07]** >> what will happen in five years? You will have one product manager, one engineer

**[01:15:09]** have one product manager, one engineer

**[01:15:09]** have one product manager, one engineer and one designer.

**[01:15:10]** and one designer.

**[01:15:10]** and one designer. >> You should answer this one.

**[01:15:12]** >> You should answer this one.

**[01:15:12]** >> You should answer this one. >> You should do it in the mic though if

**[01:15:13]** >> You should do it in the mic though if

**[01:15:13]** >> You should do it in the mic though if you want to.

**[01:15:14]** you want to.

**[01:15:14]** you want to. >> [laughter]

**[01:15:15]** >> [laughter]

**[01:15:15]** >> [laughter] >> The short of it is actually

**[01:15:28]** cursor on the code there's so many times

**[01:15:28]** cursor on the code there's so many times the PM are taking up time asking a

**[01:15:31]** the PM are taking up time asking a

**[01:15:31]** the PM are taking up time asking a question like you know how often we just

**[01:15:34]** question like you know how often we just

**[01:15:34]** question like you know how often we just ask cursor so um yeah like start start

**[01:15:37]** ask cursor so um yeah like start start

**[01:15:37]** ask cursor so um yeah like start start there open up your codebase to cursor

**[01:15:39]** there open up your codebase to cursor

**[01:15:39]** there open up your codebase to cursor give it to PMs um and then a lot of some

**[01:15:43]** give it to PMs um and then a lot of some

**[01:15:43]** give it to PMs um and then a lot of some we've we were the other day doing a PRD

**[01:15:45]** we've we were the other day doing a PRD

**[01:15:45]** we've we were the other day doing a PRD starting from cursor on the codebase. So

**[01:15:48]** starting from cursor on the codebase. So

**[01:15:48]** starting from cursor on the codebase. So I think the Yeah, I I I that would be

**[01:15:50]** I think the Yeah, I I I that would be

**[01:15:50]** I think the Yeah, I I I that would be where I would start.

**[01:15:51]** where I would start.

**[01:15:51]** where I would start. >> Yeah.

**[01:15:52]** >> Yeah.

**[01:15:52]** >> Yeah. >> Um and I I I don't I can't you know I

**[01:15:54]** >> Um and I I I don't I can't you know I

**[01:15:54]** >> Um and I I I don't I can't you know I it's hard to look forward right now. I

**[01:15:56]** it's hard to look forward right now. I

**[01:15:56]** it's hard to look forward right now. I just I think a lot of jobs change. We're

**[01:15:58]** just I think a lot of jobs change. We're

**[01:15:58]** just I think a lot of jobs change. We're trying to push um AI cursor use


### [01:16:00 - 01:17:00]

**[01:16:01]** trying to push um AI cursor use

**[01:16:01]** trying to push um AI cursor use throughout the company uh as far as I

**[01:16:03]** throughout the company uh as far as I

**[01:16:03]** throughout the company uh as far as I can.

**[01:16:04]** can.

**[01:16:04]** can. >> Yeah, I hear we have uh people in

**[01:16:05]** >> Yeah, I hear we have uh people in

**[01:16:05]** >> Yeah, I hear we have uh people in marketing using cursor too these days.

**[01:16:07]** marketing using cursor too these days.

**[01:16:07]** marketing using cursor too these days. So um yeah, that's kind of cool. Um

**[01:16:10]** So um yeah, that's kind of cool. Um

**[01:16:10]** So um yeah, that's kind of cool. Um >> yeah. Um

**[01:16:11]** >> yeah. Um

**[01:16:12]** >> yeah. Um >> follow question. Yeah.

**[01:16:13]** >> follow question. Yeah.

**[01:16:13]** >> follow question. Yeah. >> So you're talking about right now having

**[01:16:16]** >> So you're talking about right now having

**[01:16:16]** >> So you're talking about right now having a product become more of a technologist.

**[01:16:19]** a product become more of a technologist.

**[01:16:19]** a product become more of a technologist. Do you see also technologist becoming

**[01:16:21]** Do you see also technologist becoming

**[01:16:21]** Do you see also technologist becoming more product?

**[01:16:25]** more product?

**[01:16:25]** more product? >> So that's actually a great point which

**[01:16:26]** >> So that's actually a great point which

**[01:16:26]** >> So that's actually a great point which is like when the cost of building

**[01:16:29]** is like when the cost of building

**[01:16:29]** is like when the cost of building something goes down which it has

**[01:16:33]** something goes down which it has

**[01:16:33]** something goes down which it has what's what's the right thing to build

**[01:16:35]** what's what's the right thing to build

**[01:16:35]** what's what's the right thing to build becomes really important and valuable.

**[01:16:36]** becomes really important and valuable.

**[01:16:36]** becomes really important and valuable. And I think that historically that's

**[01:16:38]** And I think that historically that's

**[01:16:38]** And I think that historically that's been like a product person or a business

**[01:16:40]** been like a product person or a business

**[01:16:40]** been like a product person or a business person saying, "Hey, here's what our

**[01:16:41]** person saying, "Hey, here's what our

**[01:16:41]** person saying, "Hey, here's what our customers want. Let's go build this

**[01:16:43]** customers want. Let's go build this

**[01:16:43]** customers want. Let's go build this thing." Now we're saying product people,

**[01:16:45]** thing." Now we're saying product people,

**[01:16:45]** thing." Now we're saying product people, you can just go build this thing. So the

**[01:16:46]** you can just go build this thing. So the

**[01:16:46]** you can just go build this thing. So the builders are like, "Wait, what's my job?

**[01:16:48]** builders are like, "Wait, what's my job?

**[01:16:48]** builders are like, "Wait, what's my job? Like do I" And I think that that's a

**[01:16:50]** Like do I" And I think that that's a

**[01:16:50]** Like do I" And I think that that's a good way to look at it, which is I I

**[01:16:53]** good way to look at it, which is I I

**[01:16:53]** good way to look at it, which is I I have this like mental framework of like

**[01:16:54]** have this like mental framework of like

**[01:16:54]** have this like mental framework of like what if we didn't have roles in a

**[01:16:56]** what if we didn't have roles in a

**[01:16:56]** what if we didn't have roles in a company anymore? Like you didn't define

**[01:16:58]** company anymore? Like you didn't define

**[01:16:58]** company anymore? Like you didn't define yourself by like I'm a PM, I'm an


### [01:17:00 - 01:18:00]

**[01:17:00]** yourself by like I'm a PM, I'm an

**[01:17:00]** yourself by like I'm a PM, I'm an engineer. And think of this instead as

**[01:17:02]** engineer. And think of this instead as

**[01:17:02]** engineer. And think of this instead as like like you know like baseball cards

**[01:17:04]** like like you know like baseball cards

**[01:17:04]** like like you know like baseball cards you have like skills. Imagine that you

**[01:17:06]** you have like skills. Imagine that you

**[01:17:06]** you have like skills. Imagine that you had like a skilled stack instead, which

**[01:17:08]** had like a skilled stack instead, which

**[01:17:08]** had like a skilled stack instead, which is like, I really like to talk to

**[01:17:09]** is like, I really like to talk to

**[01:17:09]** is like, I really like to talk to customers and I kind of like to code

**[01:17:11]** customers and I kind of like to code

**[01:17:11]** customers and I kind of like to code stuff on the side, but I don't want to

**[01:17:13]** stuff on the side, but I don't want to

**[01:17:13]** stuff on the side, but I don't want to be responsible if there's a production

**[01:17:14]** be responsible if there's a production

**[01:17:14]** be responsible if there's a production outage. I guarantee you, you'll find

**[01:17:16]** outage. I guarantee you, you'll find

**[01:17:16]** outage. I guarantee you, you'll find someone who's like, I hate talking to

**[01:17:18]** someone who's like, I hate talking to

**[01:17:18]** someone who's like, I hate talking to customers and I only want to ship high

**[01:17:20]** customers and I only want to ship high

**[01:17:20]** customers and I only want to ship high quality code and I want to be

**[01:17:21]** quality code and I want to be

**[01:17:21]** quality code and I want to be responsible if things hit the fan. And I

**[01:17:23]** responsible if things hit the fan. And I

**[01:17:23]** responsible if things hit the fan. And I think you want to structure your company

**[01:17:25]** think you want to structure your company

**[01:17:25]** think you want to structure your company to have a skilled stack that's really

**[01:17:28]** to have a skilled stack that's really

**[01:17:28]** to have a skilled stack that's really complimementaryary versus people who are

**[01:17:30]** complimementaryary versus people who are

**[01:17:30]** complimementaryary versus people who are like, I do this and this is my job and I

**[01:17:32]** like, I do this and this is my job and I

**[01:17:32]** like, I do this and this is my job and I don't do that. So yeah,

**[01:17:34]** don't do that. So yeah,

**[01:17:34]** don't do that. So yeah, >> I have something that's sort of related

**[01:17:36]** >> I have something that's sort of related

**[01:17:36]** >> I have something that's sort of related to that. We've been testing like human

**[01:17:37]** to that. We've been testing like human

**[01:17:37]** to that. We've been testing like human in the loop on on

**[01:17:40]** in the loop on on

**[01:17:40]** in the loop on on >> in a couple different ways and we're

**[01:17:41]** >> in a couple different ways and we're

**[01:17:42]** >> in a couple different ways and we're basically testing this method of having

**[01:17:44]** basically testing this method of having

**[01:17:44]** basically testing this method of having the human as a tool of the agent. So

**[01:17:47]** the human as a tool of the agent. So

**[01:17:47]** the human as a tool of the agent. So like we have like

**[01:17:48]** like we have like

**[01:17:48]** like we have like >> if the agent needs something that's not

**[01:17:49]** >> if the agent needs something that's not

**[01:17:49]** >> if the agent needs something that's not available in the accounting system,

**[01:17:51]** available in the accounting system,

**[01:17:51]** available in the accounting system, it'll go to the CFO because the CFO is

**[01:17:53]** it'll go to the CFO because the CFO is

**[01:17:54]** it'll go to the CFO because the CFO is listed as a tool and it sends that a

**[01:17:55]** listed as a tool and it sends that a

**[01:17:55]** listed as a tool and it sends that a Slack message, gets it back and

**[01:17:57]** Slack message, gets it back and

**[01:17:57]** Slack message, gets it back and continues. kind of maps onto what you

**[01:17:59]** continues. kind of maps onto what you

**[01:17:59]** continues. kind of maps onto what you just said of like defining the skills,


### [01:18:00 - 01:19:00]

**[01:18:01]** just said of like defining the skills,

**[01:18:01]** just said of like defining the skills, defining the resources they have and um

**[01:18:04]** defining the resources they have and um

**[01:18:04]** defining the resources they have and um they haven't fully fleshed it out, but

**[01:18:05]** they haven't fully fleshed it out, but

**[01:18:06]** they haven't fully fleshed it out, but it's it's working to like give the agent

**[01:18:07]** it's it's working to like give the agent

**[01:18:07]** it's it's working to like give the agent context on

**[01:18:10]** context on

**[01:18:10]** context on on the things that only the humans have.

**[01:18:11]** on the things that only the humans have.

**[01:18:11]** on the things that only the humans have. >> Yeah.

**[01:18:12]** >> Yeah.

**[01:18:12]** >> Yeah. >> Exactly.

**[01:18:13]** >> Exactly.

**[01:18:13]** >> Exactly. >> So, this person is like your company's

**[01:18:15]** >> So, this person is like your company's

**[01:18:15]** >> So, this person is like your company's like using agents widely, it sounds

**[01:18:17]** like using agents widely, it sounds

**[01:18:17]** like using agents widely, it sounds like, but you have humans approving. you

**[01:18:19]** like, but you have humans approving. you

**[01:18:19]** like, but you have humans approving. you have like an approver workflow to

**[01:18:20]** have like an approver workflow to

**[01:18:20]** have like an approver workflow to >> something more so like rather than how

**[01:18:23]** >> something more so like rather than how

**[01:18:23]** >> something more so like rather than how can the agent be a tool of the humans,

**[01:18:25]** can the agent be a tool of the humans,

**[01:18:25]** can the agent be a tool of the humans, >> we're kind of flipping it and saying

**[01:18:26]** >> we're kind of flipping it and saying

**[01:18:26]** >> we're kind of flipping it and saying like what if the agent could do

**[01:18:27]** like what if the agent could do

**[01:18:27]** like what if the agent could do everything

**[01:18:28]** everything

**[01:18:28]** everything >> and then the parts it can't do it'll go

**[01:18:30]** >> and then the parts it can't do it'll go

**[01:18:30]** >> and then the parts it can't do it'll go to the human as a tool. So like the CFO

**[01:18:33]** to the human as a tool. So like the CFO

**[01:18:33]** to the human as a tool. So like the CFO is a tool of the AI agent.

**[01:18:34]** is a tool of the AI agent.

**[01:18:34]** is a tool of the AI agent. >> Interesting.

**[01:18:35]** >> Interesting.

**[01:18:36]** >> Interesting. >> We should chat. That's a really cool

**[01:18:37]** >> We should chat. That's a really cool

**[01:18:37]** >> We should chat. That's a really cool workflow. I I'll definitely bug you

**[01:18:38]** workflow. I I'll definitely bug you

**[01:18:38]** workflow. I I'll definitely bug you about that. That's that's really cool.

**[01:18:39]** about that. That's that's really cool.

**[01:18:39]** about that. That's that's really cool. Um

**[01:18:41]** Um

**[01:18:41]** Um >> cool. Um happy

**[01:18:47]** >> right to some degree. It's like a human

**[01:18:47]** >> right to some degree. It's like a human in the loop approving is this good or

**[01:18:49]** in the loop approving is this good or

**[01:18:49]** in the loop approving is this good or bad and you can think of it that way. Um

**[01:18:52]** bad and you can think of it that way. Um

**[01:18:52]** bad and you can think of it that way. Um >> yeah.

**[01:18:52]** >> yeah.

**[01:18:52]** >> yeah. >> Yeah. I had a question about like what

**[01:18:54]** >> Yeah. I had a question about like what

**[01:18:54]** >> Yeah. I had a question about like what what it is like to actually implement

**[01:18:57]** what it is like to actually implement

**[01:18:57]** what it is like to actually implement well sending the traces over to Arise.

**[01:18:59]** well sending the traces over to Arise.

**[01:18:59]** well sending the traces over to Arise. Um I know like Arise has like open


### [01:19:00 - 01:20:00]

**[01:19:01]** Um I know like Arise has like open

**[01:19:01]** Um I know like Arise has like open inference which enables enables like

**[01:19:04]** inference which enables enables like

**[01:19:04]** inference which enables enables like capturing traces from se several

**[01:19:05]** capturing traces from se several

**[01:19:05]** capturing traces from se several different um several different

**[01:19:07]** different um several different

**[01:19:07]** different um several different providers. But um what are what are what

**[01:19:10]** providers. But um what are what are what

**[01:19:10]** providers. But um what are what are what are what are the limitations and

**[01:19:12]** are what are the limitations and

**[01:19:12]** are what are the limitations and constraints and opinions that you have

**[01:19:13]** constraints and opinions that you have

**[01:19:14]** constraints and opinions that you have about um how the evolve should be

**[01:19:17]** about um how the evolve should be

**[01:19:17]** about um how the evolve should be structured so that you can actually like

**[01:19:18]** structured so that you can actually like

**[01:19:18]** structured so that you can actually like leverage the platform to perform these

**[01:19:20]** leverage the platform to perform these

**[01:19:20]** leverage the platform to perform these actions to be able to like um evaluate

**[01:19:23]** actions to be able to like um evaluate

**[01:19:23]** actions to be able to like um evaluate the eval for example or um be be able to

**[01:19:26]** the eval for example or um be be able to

**[01:19:26]** the eval for example or um be be able to like

**[01:19:28]** like

**[01:19:28]** like numerically

**[01:19:29]** numerically

**[01:19:29]** numerically just produce graphs out of out of your

**[01:19:32]** just produce graphs out of out of your

**[01:19:32]** just produce graphs out of out of your evaluations out of your outputs.

**[01:19:34]** evaluations out of your outputs.

**[01:19:34]** evaluations out of your outputs. >> Okay. So, so clear.

**[01:19:36]** >> Okay. So, so clear.

**[01:19:36]** >> Okay. So, so clear. >> So, can I can I ask a follow-up question

**[01:19:37]** >> So, can I can I ask a follow-up question

**[01:19:37]** >> So, can I can I ask a follow-up question to that which is like your question was

**[01:19:39]** to that which is like your question was

**[01:19:40]** to that which is like your question was like how to use agents to do some of the

**[01:19:42]** like how to use agents to do some of the

**[01:19:42]** like how to use agents to do some of the workflows in the platform or did I miss

**[01:19:44]** workflows in the platform or did I miss

**[01:19:44]** workflows in the platform or did I miss that?

**[01:19:44]** that?

**[01:19:44]** that? >> Um, the the question the question is

**[01:19:46]** >> Um, the the question the question is

**[01:19:46]** >> Um, the the question the question is like

**[01:19:47]** like

**[01:19:48]** like >> how is like what what kind of outputs

**[01:19:51]** >> how is like what what kind of outputs

**[01:19:51]** >> how is like what what kind of outputs what kind of evals is this um is Arise

**[01:19:54]** what kind of evals is this um is Arise

**[01:19:54]** what kind of evals is this um is Arise expecting from your engineers and from

**[01:19:57]** expecting from your engineers and from

**[01:19:57]** expecting from your engineers and from the product like the

**[01:19:58]** the product like the

**[01:19:58]** the product like the >> you're sending over logs, right?


### [01:20:00 - 01:21:00]

**[01:20:00]** >> you're sending over logs, right?

**[01:20:00]** >> you're sending over logs, right? >> Mhm. Yeah. um what what is it expecting

**[01:20:02]** >> Mhm. Yeah. um what what is it expecting

**[01:20:02]** >> Mhm. Yeah. um what what is it expecting from those logs in order to get this

**[01:20:05]** from those logs in order to get this

**[01:20:05]** from those logs in order to get this flow work?

**[01:20:05]** flow work?

**[01:20:06]** flow work? >> Understood. Okay. So uh so yeah there is

**[01:20:08]** >> Understood. Okay. So uh so yeah there is

**[01:20:08]** >> Understood. Okay. So uh so yeah there is a very uh like great point there which

**[01:20:10]** a very uh like great point there which

**[01:20:10]** a very uh like great point there which is like we kind of um you'll see it in

**[01:20:13]** is like we kind of um you'll see it in

**[01:20:13]** is like we kind of um you'll see it in the code but we jumped over a little bit

**[01:20:15]** the code but we jumped over a little bit

**[01:20:15]** the code but we jumped over a little bit here in uh the demo which is how do you

**[01:20:18]** here in uh the demo which is how do you

**[01:20:18]** here in uh the demo which is how do you get the logs in the right place to use

**[01:20:20]** get the logs in the right place to use

**[01:20:20]** get the logs in the right place to use the platform. Um unfortunately this page

**[01:20:23]** the platform. Um unfortunately this page

**[01:20:23]** the platform. Um unfortunately this page isn't dropping but let me okay here we

**[01:20:25]** isn't dropping but let me okay here we

**[01:20:25]** isn't dropping but let me okay here we go. I'm going to drop it in the Slack

**[01:20:26]** go. I'm going to drop it in the Slack

**[01:20:26]** go. I'm going to drop it in the Slack channel as well. This is what we, you

**[01:20:29]** channel as well. This is what we, you

**[01:20:29]** channel as well. This is what we, you know, we kind of talked about like

**[01:20:30]** know, we kind of talked about like

**[01:20:30]** know, we kind of talked about like traces and spans. It's very likely that

**[01:20:32]** traces and spans. It's very likely that

**[01:20:32]** traces and spans. It's very likely that your team already has logs or traces and

**[01:20:35]** your team already has logs or traces and

**[01:20:35]** your team already has logs or traces and spans already. You might be using data

**[01:20:37]** spans already. You might be using data

**[01:20:37]** spans already. You might be using data dog or a different platform like

**[01:20:38]** dog or a different platform like

**[01:20:38]** dog or a different platform like Graphana. What we do is we're taking

**[01:20:40]** Graphana. What we do is we're taking

**[01:20:40]** Graphana. What we do is we're taking those same traces and spans and we're

**[01:20:43]** those same traces and spans and we're

**[01:20:43]** those same traces and spans and we're essentially augmenting them with more

**[01:20:45]** essentially augmenting them with more

**[01:20:45]** essentially augmenting them with more metadata and structuring them in a way

**[01:20:47]** metadata and structuring them in a way

**[01:20:47]** metadata and structuring them in a way that the platform kind of knows which

**[01:20:49]** that the platform kind of knows which

**[01:20:49]** that the platform kind of knows which columns to go and look at to render the

**[01:20:51]** columns to go and look at to render the

**[01:20:51]** columns to go and look at to render the data that you saw in the platform. So

**[01:20:53]** data that you saw in the platform. So

**[01:20:54]** data that you saw in the platform. So you're really using um the same

**[01:20:56]** you're really using um the same

**[01:20:56]** you're really using um the same approach. We we're built on top of a

**[01:20:59]** approach. We we're built on top of a

**[01:20:59]** approach. We we're built on top of a convention called open telemetry which


### [01:21:00 - 01:22:00]

**[01:21:01]** convention called open telemetry which

**[01:21:01]** convention called open telemetry which is like the open source standard for

**[01:21:03]** is like the open source standard for

**[01:21:03]** is like the open source standard for tracing. Uh so we actually use hotel uh

**[01:21:07]** tracing. Uh so we actually use hotel uh

**[01:21:07]** tracing. Uh so we actually use hotel uh tracing and auto instrumentation that

**[01:21:09]** tracing and auto instrumentation that

**[01:21:09]** tracing and auto instrumentation that we've built which doesn't keep you

**[01:21:11]** we've built which doesn't keep you

**[01:21:11]** we've built which doesn't keep you locked in at all. Like once you've

**[01:21:13]** locked in at all. Like once you've

**[01:21:13]** locked in at all. Like once you've instrumented with our platform using

**[01:21:15]** instrumented with our platform using

**[01:21:15]** instrumented with our platform using open inference which is our our package

**[01:21:18]** open inference which is our our package

**[01:21:18]** open inference which is our our package you actually get those logs to show up

**[01:21:20]** you actually get those logs to show up

**[01:21:20]** you actually get those logs to show up right out of the box with any type of

**[01:21:22]** right out of the box with any type of

**[01:21:22]** right out of the box with any type of agent framework you might be building

**[01:21:24]** agent framework you might be building

**[01:21:24]** agent framework you might be building and um and yeah and you get to keep that

**[01:21:26]** and um and yeah and you get to keep that

**[01:21:26]** and um and yeah and you get to keep that that's let me maybe just show like what

**[01:21:28]** that's let me maybe just show like what

**[01:21:28]** that's let me maybe just show like what I mean by that. So if you're let's say

**[01:21:29]** I mean by that. So if you're let's say

**[01:21:30]** I mean by that. So if you're let's say you're building with like lang graph um

**[01:21:33]** you're building with like lang graph um

**[01:21:33]** you're building with like lang graph um we actually have it really all you have

**[01:21:36]** we actually have it really all you have

**[01:21:36]** we actually have it really all you have to do is like you pip install uh arise

**[01:21:39]** to do is like you pip install uh arise

**[01:21:39]** to do is like you pip install uh arise phoenix arise hotel and you what you

**[01:21:42]** phoenix arise hotel and you what you

**[01:21:42]** phoenix arise hotel and you what you call this single line of coal call uh

**[01:21:44]** call this single line of coal call uh

**[01:21:44]** call this single line of coal call uh the single line of code called langchain

**[01:21:46]** the single line of code called langchain

**[01:21:46]** the single line of code called langchain instrument and it knows where to pick up

**[01:21:49]** instrument and it knows where to pick up

**[01:21:49]** instrument and it knows where to pick up in your code to structure your logs and

**[01:21:51]** in your code to structure your logs and

**[01:21:51]** in your code to structure your logs and if you have more specific things you

**[01:21:52]** if you have more specific things you

**[01:21:52]** if you have more specific things you want to add to your logs you can add

**[01:21:54]** want to add to your logs you can add

**[01:21:54]** want to add to your logs you can add function dec decorators which is uh

**[01:21:57]** function dec decorators which is uh

**[01:21:57]** function dec decorators which is uh basically a way to you for you to um you

**[01:21:59]** basically a way to you for you to um you

**[01:21:59]** basically a way to you for you to um you know capture specific functions that


### [01:22:00 - 01:23:00]

**[01:22:01]** know capture specific functions that

**[01:22:01]** know capture specific functions that weren't in the

**[01:22:02]** weren't in the

**[01:22:02]** weren't in the >> and as for evaluations like you're

**[01:22:03]** >> and as for evaluations like you're

**[01:22:03]** >> and as for evaluations like you're you're discussing like the actual data

**[01:22:05]** you're discussing like the actual data

**[01:22:05]** you're discussing like the actual data inputs outputs what do you what do you

**[01:22:07]** inputs outputs what do you what do you

**[01:22:07]** inputs outputs what do you what do you need to pass into evaluations I

**[01:22:12]** need to pass into evaluations I

**[01:22:12]** need to pass into evaluations I >> I know you can like design them through

**[01:22:13]** >> I know you can like design them through

**[01:22:13]** >> I know you can like design them through the UI

**[01:22:15]** the UI

**[01:22:15]** the UI >> what what do you have in mind for like

**[01:22:18]** >> what what do you have in mind for like

**[01:22:18]** >> what what do you have in mind for like um

**[01:22:18]** um

**[01:22:18]** um >> like how how do you get the right uh

**[01:22:21]** >> like how how do you get the right uh

**[01:22:21]** >> like how how do you get the right uh text to use for eval right is sort of

**[01:22:22]** text to use for eval right is sort of

**[01:22:22]** text to use for eval right is sort of your question

**[01:22:24]** your question

**[01:22:24]** your question >> like how do how are you like how do you

**[01:22:26]** >> like how do how are you like how do you

**[01:22:26]** >> like how do how are you like how do you know which to

**[01:22:27]** know which to

**[01:22:27]** know which to >> use I I need to

**[01:22:28]** >> use I I need to

**[01:22:28]** >> use I I need to format the question. I'll get back to

**[01:22:29]** format the question. I'll get back to

**[01:22:29]** format the question. I'll get back to you.

**[01:22:29]** you.

**[01:22:29]** you. >> Yeah, no worries. What did you mean by

**[01:22:32]** >> Yeah, no worries. What did you mean by

**[01:22:32]** >> Yeah, no worries. What did you mean by adding augmenting the data with

**[01:22:33]** adding augmenting the data with

**[01:22:33]** adding augmenting the data with additional metadata like you only have

**[01:22:35]** additional metadata like you only have

**[01:22:35]** additional metadata like you only have so much data, right?

**[01:22:36]** so much data, right?

**[01:22:36]** so much data, right? >> Yeah. So, so this is um so think of this

**[01:22:39]** >> Yeah. So, so this is um so think of this

**[01:22:39]** >> Yeah. So, so this is um so think of this as like most tracing and logging data is

**[01:22:43]** as like most tracing and logging data is

**[01:22:43]** as like most tracing and logging data is really just things like latency, timing

**[01:22:45]** really just things like latency, timing

**[01:22:45]** really just things like latency, timing information. What we're doing is you can

**[01:22:47]** information. What we're doing is you can

**[01:22:47]** information. What we're doing is you can add more metadata like user ID, session

**[01:22:50]** add more metadata like user ID, session

**[01:22:50]** add more metadata like user ID, session ID, uh things like I'll kind of show you

**[01:22:53]** ID, uh things like I'll kind of show you

**[01:22:53]** ID, uh things like I'll kind of show you an example of that really quick. In the

**[01:22:55]** an example of that really quick. In the

**[01:22:56]** an example of that really quick. In the in the previous example I showed, we

**[01:22:57]** in the previous example I showed, we

**[01:22:57]** in the previous example I showed, we actually have things like sessions like


### [01:23:00 - 01:24:00]

**[01:23:00]** actually have things like sessions like

**[01:23:00]** actually have things like sessions like what's the back and forth example here.

**[01:23:02]** what's the back and forth example here.

**[01:23:02]** what's the back and forth example here. You can't get a viz like this in data

**[01:23:04]** You can't get a viz like this in data

**[01:23:04]** You can't get a viz like this in data dog because data dog is looking at a

**[01:23:06]** dog because data dog is looking at a

**[01:23:06]** dog because data dog is looking at a single span or trace. It's not it's not

**[01:23:08]** single span or trace. It's not it's not

**[01:23:08]** single span or trace. It's not it's not really contextually aware of what is the

**[01:23:11]** really contextually aware of what is the

**[01:23:11]** really contextually aware of what is the human, what's the AI. So we're adding

**[01:23:13]** human, what's the AI. So we're adding

**[01:23:13]** human, what's the AI. So we're adding context from the from the invocation of

**[01:23:16]** context from the from the invocation of

**[01:23:16]** context from the from the invocation of the the server and adding that to your

**[01:23:19]** the the server and adding that to your

**[01:23:19]** the the server and adding that to your span if that makes sense. So it's it's

**[01:23:20]** span if that makes sense. So it's it's

**[01:23:20]** span if that makes sense. So it's it's basically just enriching the data a bit

**[01:23:22]** basically just enriching the data a bit

**[01:23:22]** basically just enriching the data a bit more and structuring it in a way to use

**[01:23:24]** more and structuring it in a way to use

**[01:23:24]** more and structuring it in a way to use it. Um yeah and if you have more

**[01:23:27]** it. Um yeah and if you have more

**[01:23:27]** it. Um yeah and if you have more specific um server side logic you can

**[01:23:29]** specific um server side logic you can

**[01:23:30]** specific um server side logic you can add that as well so it's very flexible.

**[01:23:32]** add that as well so it's very flexible.

**[01:23:32]** add that as well so it's very flexible. Yeah.

**[01:23:33]** Yeah.

**[01:23:33]** Yeah. >> Yeah.

**[01:23:33]** >> Yeah.

**[01:23:33]** >> Yeah. >> Uh so I have a provocation. So I used to

**[01:23:35]** >> Uh so I have a provocation. So I used to

**[01:23:35]** >> Uh so I have a provocation. So I used to work in the video game industry

**[01:23:37]** work in the video game industry

**[01:23:37]** work in the video game industry >> and debates about feature like whether a

**[01:23:39]** >> and debates about feature like whether a

**[01:23:39]** >> and debates about feature like whether a feature was going to be fun or not.

**[01:23:41]** feature was going to be fun or not.

**[01:23:41]** feature was going to be fun or not. >> Working prototypes

**[01:23:43]** >> Working prototypes

**[01:23:43]** >> Working prototypes >> won all of those arguments. Whatever was

**[01:23:45]** >> won all of those arguments. Whatever was

**[01:23:45]** >> won all of those arguments. Whatever was in the doc didn't matter.

**[01:23:46]** in the doc didn't matter.

**[01:23:46]** in the doc didn't matter. >> Right.

**[01:23:47]** >> Right.

**[01:23:47]** >> Right. >> And so for the person who was like I

**[01:23:49]** >> And so for the person who was like I

**[01:23:49]** >> And so for the person who was like I can't get access to my company's code. I

**[01:23:51]** can't get access to my company's code. I

**[01:23:51]** can't get access to my company's code. I would actually say try to get access to

**[01:23:53]** would actually say try to get access to

**[01:23:53]** would actually say try to get access to a small sliver of the data and then

**[01:23:56]** a small sliver of the data and then

**[01:23:56]** a small sliver of the data and then build a working prototype of the feature

**[01:23:58]** build a working prototype of the feature

**[01:23:58]** build a working prototype of the feature you want to see and with some stub of


### [01:24:00 - 01:25:00]

**[01:24:01]** you want to see and with some stub of

**[01:24:01]** you want to see and with some stub of eval because I think you know there's

**[01:24:04]** eval because I think you know there's

**[01:24:04]** eval because I think you know there's nothing worse to an engineer than a

**[01:24:05]** nothing worse to an engineer than a

**[01:24:06]** nothing worse to an engineer than a product manager who shows up with a demo

**[01:24:08]** product manager who shows up with a demo

**[01:24:08]** product manager who shows up with a demo that's kind of janky.

**[01:24:09]** that's kind of janky.

**[01:24:09]** that's kind of janky. >> Yeah. but actually works and might be

**[01:24:12]** >> Yeah. but actually works and might be

**[01:24:12]** >> Yeah. but actually works and might be fun, has polish, feels good, meets a

**[01:24:16]** fun, has polish, feels good, meets a

**[01:24:16]** fun, has polish, feels good, meets a user need, and they and having been on

**[01:24:18]** user need, and they and having been on

**[01:24:18]** user need, and they and having been on the engineering side of this equation,

**[01:24:20]** the engineering side of this equation,

**[01:24:20]** the engineering side of this equation, I'm like, and it's so janky, I have to

**[01:24:22]** I'm like, and it's so janky, I have to

**[01:24:22]** I'm like, and it's so janky, I have to fix it. They haven't thought about the

**[01:24:23]** fix it. They haven't thought about the

**[01:24:23]** fix it. They haven't thought about the edge cases. And so like how does Arise

**[01:24:27]** edge cases. And so like how does Arise

**[01:24:27]** edge cases. And so like how does Arise fit into that flow of helping a product

**[01:24:30]** fit into that flow of helping a product

**[01:24:30]** fit into that flow of helping a product manager basically mine a small segment

**[01:24:33]** manager basically mine a small segment

**[01:24:33]** manager basically mine a small segment of data build a working example and

**[01:24:37]** of data build a working example and

**[01:24:37]** of data build a working example and perhaps be just a you know janky as all

**[01:24:39]** perhaps be just a you know janky as all

**[01:24:39]** perhaps be just a you know janky as all get out but something that looks like

**[01:24:41]** get out but something that looks like

**[01:24:41]** get out but something that looks like the product that the company already has

**[01:24:44]** the product that the company already has

**[01:24:44]** the product that the company already has but demonstrates that next level of

**[01:24:46]** but demonstrates that next level of

**[01:24:46]** but demonstrates that next level of functionality. Great, great point. And

**[01:24:49]** functionality. Great, great point. And

**[01:24:49]** functionality. Great, great point. And yeah, I I think like, you know, feel

**[01:24:51]** yeah, I I think like, you know, feel

**[01:24:51]** yeah, I I think like, you know, feel free to prototype and build, you know,

**[01:24:54]** free to prototype and build, you know,

**[01:24:54]** free to prototype and build, you know, prototypes that are that are high

**[01:24:55]** prototypes that are that are high

**[01:24:56]** prototypes that are that are high fidelity. I think it is awesome to do

**[01:24:57]** fidelity. I think it is awesome to do

**[01:24:57]** fidelity. I think it is awesome to do that. That's a really good point to have

**[01:24:59]** that. That's a really good point to have

**[01:24:59]** that. That's a really good point to have like to use data to build a system or


### [01:25:00 - 01:26:00]

**[01:25:01]** like to use data to build a system or

**[01:25:01]** like to use data to build a system or prototype. So, what does Arise do here?

**[01:25:04]** prototype. So, what does Arise do here?

**[01:25:04]** prototype. So, what does Arise do here? If you have access to Arise and you

**[01:25:06]** If you have access to Arise and you

**[01:25:06]** If you have access to Arise and you don't have access to the codebase, you

**[01:25:08]** don't have access to the codebase, you

**[01:25:08]** don't have access to the codebase, you can still take this data and assuming

**[01:25:09]** can still take this data and assuming

**[01:25:09]** can still take this data and assuming that you have permission from your CIS

**[01:25:12]** that you have permission from your CIS

**[01:25:12]** that you have permission from your CIS admin person, you can actually export

**[01:25:14]** admin person, you can actually export

**[01:25:14]** admin person, you can actually export this data. So once you've built a data

**[01:25:16]** this data. So once you've built a data

**[01:25:16]** this data. So once you've built a data set, you can simply take this data and

**[01:25:18]** set, you can simply take this data and

**[01:25:18]** set, you can simply take this data and export it out and use that to actually

**[01:25:21]** export it out and use that to actually

**[01:25:21]** export it out and use that to actually um so I can kind of show that really

**[01:25:23]** um so I can kind of show that really

**[01:25:23]** um so I can kind of show that really quick. Um this is get get data set.

**[01:25:26]** quick. Um this is get get data set.

**[01:25:26]** quick. Um this is get get data set. We'll have a download button coming uh

**[01:25:27]** We'll have a download button coming uh

**[01:25:27]** We'll have a download button coming uh later this week, but you can actually

**[01:25:29]** later this week, but you can actually

**[01:25:29]** later this week, but you can actually just take this data, run it locally,

**[01:25:32]** just take this data, run it locally,

**[01:25:32]** just take this data, run it locally, keep it locally, and then actually use

**[01:25:33]** keep it locally, and then actually use

**[01:25:33]** keep it locally, and then actually use that in your local code to actually try

**[01:25:36]** that in your local code to actually try

**[01:25:36]** that in your local code to actually try and iterate on an example. Um and you

**[01:25:39]** and iterate on an example. Um and you

**[01:25:39]** and iterate on an example. Um and you know, assuming your security team is

**[01:25:40]** know, assuming your security team is

**[01:25:40]** know, assuming your security team is okay with that. But that's a really good

**[01:25:42]** okay with that. But that's a really good

**[01:25:42]** okay with that. But that's a really good point. Like imagine if you didn't need

**[01:25:44]** point. Like imagine if you didn't need

**[01:25:44]** point. Like imagine if you didn't need access to the production codebase, but

**[01:25:46]** access to the production codebase, but

**[01:25:46]** access to the production codebase, but you could still iterate in one platform.

**[01:25:48]** you could still iterate in one platform.

**[01:25:48]** you could still iterate in one platform. That's really what we're we're pushing

**[01:25:49]** That's really what we're we're pushing

**[01:25:50]** That's really what we're we're pushing for is like the whole team is iterating

**[01:25:51]** for is like the whole team is iterating

**[01:25:51]** for is like the whole team is iterating on the prompts and the eval um rather

**[01:25:54]** on the prompts and the eval um rather

**[01:25:54]** on the prompts and the eval um rather than in silos, which is what's happening

**[01:25:56]** than in silos, which is what's happening

**[01:25:56]** than in silos, which is what's happening in a lot of cases. Okay, I think that

**[01:25:59]** in a lot of cases. Okay, I think that

**[01:25:59]** in a lot of cases. Okay, I think that was all the questions. Thank you all for


### [01:26:00 - 01:27:00]

**[01:26:01]** was all the questions. Thank you all for

**[01:26:01]** was all the questions. Thank you all for sitting through an hour and a half of AI

**[01:26:04]** sitting through an hour and a half of AI

**[01:26:04]** sitting through an hour and a half of AI PM like eval. Thank you all for for your

**[01:26:06]** PM like eval. Thank you all for for your

**[01:26:06]** PM like eval. Thank you all for for your time and um I'll be sticking around if

**[01:26:08]** time and um I'll be sticking around if

**[01:26:08]** time and um I'll be sticking around if people have more questions, but thank

**[01:26:09]** people have more questions, but thank

**[01:26:09]** people have more questions, but thank you so much.


