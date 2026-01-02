# RL Environments at Scale – Will Brown, Prime Intellect

**Video URL:** https://www.youtube.com/watch?v=_IzZWeuTx7I

---

## Full Transcript

### [00:00 - 01:00]

**[00:22]** Today we're talking about RL

**[00:22]** Today we're talking about RL environments and how to scale them. But

**[00:25]** environments and how to scale them. But

**[00:25]** environments and how to scale them. But the title is a little bit of a red

**[00:27]** the title is a little bit of a red

**[00:27]** the title is a little bit of a red herring. We'll talk a bit about the

**[00:28]** herring. We'll talk a bit about the

**[00:28]** herring. We'll talk a bit about the engineering pieces and like running

**[00:30]** engineering pieces and like running

**[00:30]** engineering pieces and like running these with thousands of parallel

**[00:31]** these with thousands of parallel

**[00:31]** these with thousands of parallel rollouts and sandboxes on hundreds of

**[00:33]** rollouts and sandboxes on hundreds of

**[00:33]** rollouts and sandboxes on hundreds of GPUs, but I'm mostly going to focus on a

**[00:35]** GPUs, but I'm mostly going to focus on a

**[00:35]** GPUs, but I'm mostly going to focus on a different notion of scale. Uh, and what

**[00:39]** different notion of scale. Uh, and what

**[00:39]** different notion of scale. Uh, and what I mean by scaling here is we there's a

**[00:42]** I mean by scaling here is we there's a

**[00:42]** I mean by scaling here is we there's a number of different ways we talk about

**[00:43]** number of different ways we talk about

**[00:43]** number of different ways we talk about scaling in the context of AI and

**[00:45]** scaling in the context of AI and

**[00:45]** scaling in the context of AI and research. We know about scaling laws and

**[00:47]** research. We know about scaling laws and

**[00:47]** research. We know about scaling laws and we talk about how much data you need,

**[00:49]** we talk about how much data you need,

**[00:49]** we talk about how much data you need, compute and parameters and that if you

**[00:51]** compute and parameters and that if you

**[00:51]** compute and parameters and that if you pour in more data and compute and

**[00:53]** pour in more data and compute and

**[00:53]** pour in more data and compute and parameters or inference time. All of

**[00:55]** parameters or inference time. All of

**[00:55]** parameters or inference time. All of these things make models smarter or more

**[00:57]** these things make models smarter or more

**[00:57]** these things make models smarter or more performant. But there's also fuzzier

**[00:59]** performant. But there's also fuzzier

**[00:59]** performant. But there's also fuzzier side of scaling which is sometimes


### [01:00 - 02:00]

**[01:01]** side of scaling which is sometimes

**[01:01]** side of scaling which is sometimes referred to as unhobbling or algorithmic

**[01:03]** referred to as unhobbling or algorithmic

**[01:03]** referred to as unhobbling or algorithmic tricks or talent. But where does this

**[01:06]** tricks or talent. But where does this

**[01:06]** tricks or talent. But where does this come from? It's not just pouring in

**[01:08]** come from? It's not just pouring in

**[01:08]** come from? It's not just pouring in resources, but it's something that is

**[01:10]** resources, but it's something that is

**[01:10]** resources, but it's something that is more intangible, harder to put a finger

**[01:12]** more intangible, harder to put a finger

**[01:12]** more intangible, harder to put a finger on, but really it comes from a community

**[01:15]** on, but really it comes from a community

**[01:15]** on, but really it comes from a community of people, a company, an organization,

**[01:17]** of people, a company, an organization,

**[01:17]** of people, a company, an organization, universities, the world, the internet,

**[01:20]** universities, the world, the internet,

**[01:20]** universities, the world, the internet, talking about ideas and sharing them and

**[01:23]** talking about ideas and sharing them and

**[01:23]** talking about ideas and sharing them and working on different applications,

**[01:24]** working on different applications,

**[01:24]** working on different applications, having these applications inspire ideas,

**[01:26]** having these applications inspire ideas,

**[01:26]** having these applications inspire ideas, using these ideas as test beds for

**[01:29]** using these ideas as test beds for

**[01:29]** using these ideas as test beds for different techniques, and building on

**[01:31]** different techniques, and building on

**[01:31]** different techniques, and building on top of these to increase the

**[01:32]** top of these to increase the

**[01:32]** top of these to increase the accessibility for other people in the

**[01:33]** accessibility for other people in the

**[01:34]** accessibility for other people in the future to not have to reinvent the wheel

**[01:35]** future to not have to reinvent the wheel

**[01:35]** future to not have to reinvent the wheel and to be able to build from uh what has

**[01:39]** and to be able to build from uh what has

**[01:39]** and to be able to build from uh what has been done by those before them to uh do

**[01:42]** been done by those before them to uh do

**[01:42]** been done by those before them to uh do more effective research and accelerate

**[01:43]** more effective research and accelerate

**[01:44]** more effective research and accelerate the pace of innovation.

**[01:46]** the pace of innovation.

**[01:46]** the pace of innovation. And so why do we have this talent

**[01:48]** And so why do we have this talent

**[01:48]** And so why do we have this talent bottleneck? There's a big issue that we

**[01:49]** bottleneck? There's a big issue that we

**[01:49]** bottleneck? There's a big issue that we hear all about with AI labs trying to

**[01:51]** hear all about with AI labs trying to

**[01:51]** hear all about with AI labs trying to like find more talent and salaries are

**[01:53]** like find more talent and salaries are

**[01:53]** like find more talent and salaries are going through the roof and everyone

**[01:55]** going through the roof and everyone

**[01:55]** going through the roof and everyone wants to hire the best and brightest AI

**[01:57]** wants to hire the best and brightest AI

**[01:57]** wants to hire the best and brightest AI researchers. But one other approach

**[01:59]** researchers. But one other approach

**[01:59]** researchers. But one other approach besides trying to just pay the most is


### [02:00 - 03:00]

**[02:02]** besides trying to just pay the most is

**[02:02]** besides trying to just pay the most is increase the pool. Uh and so how do we

**[02:04]** increase the pool. Uh and so how do we

**[02:04]** increase the pool. Uh and so how do we increase the pool of AI researchers? How

**[02:06]** increase the pool of AI researchers? How

**[02:06]** increase the pool of AI researchers? How do we make doing AI research more

**[02:08]** do we make doing AI research more

**[02:08]** do we make doing AI research more accessible? And I want to talk a bit

**[02:10]** accessible? And I want to talk a bit

**[02:10]** accessible? And I want to talk a bit about who we are at Prime Intellect. If

**[02:11]** about who we are at Prime Intellect. If

**[02:11]** about who we are at Prime Intellect. If you haven't heard of us, we are a bunch

**[02:13]** you haven't heard of us, we are a bunch

**[02:13]** you haven't heard of us, we are a bunch of things. We're a research lab. We are

**[02:15]** of things. We're a research lab. We are

**[02:15]** of things. We're a research lab. We are a comput provider. We're a platform

**[02:17]** a comput provider. We're a platform

**[02:17]** a comput provider. We're a platform company. And we are an open source

**[02:18]** company. And we are an open source

**[02:18]** company. And we are an open source ecosystem. We do a lot of things and

**[02:20]** ecosystem. We do a lot of things and

**[02:20]** ecosystem. We do a lot of things and they all fit together in a way that I'm

**[02:22]** they all fit together in a way that I'm

**[02:22]** they all fit together in a way that I'm going to try to explain in this talk.

**[02:24]** going to try to explain in this talk.

**[02:24]** going to try to explain in this talk. But we see these as all different pieces

**[02:26]** But we see these as all different pieces

**[02:26]** But we see these as all different pieces of how we can build a business around

**[02:28]** of how we can build a business around

**[02:28]** of how we can build a business around doing exactly this, which is increasing

**[02:30]** doing exactly this, which is increasing

**[02:30]** doing exactly this, which is increasing the accessibility of AI research and

**[02:32]** the accessibility of AI research and

**[02:32]** the accessibility of AI research and making doing research more of a toolkit

**[02:35]** making doing research more of a toolkit

**[02:35]** making doing research more of a toolkit available to people at organizations

**[02:36]** available to people at organizations

**[02:36]** available to people at organizations around the world without needing to be

**[02:38]** around the world without needing to be

**[02:38]** around the world without needing to be inside of a large lab or without needing

**[02:40]** inside of a large lab or without needing

**[02:40]** inside of a large lab or without needing to spend crazy amounts on massive

**[02:42]** to spend crazy amounts on massive

**[02:42]** to spend crazy amounts on massive clusters or go do a PhD. We think that

**[02:44]** clusters or go do a PhD. We think that

**[02:44]** clusters or go do a PhD. We think that there's versions of doing AI research

**[02:46]** there's versions of doing AI research

**[02:46]** there's versions of doing AI research that really should be part of the

**[02:48]** that really should be part of the

**[02:48]** that really should be part of the breadandbut workflows of AI engineers

**[02:51]** breadandbut workflows of AI engineers

**[02:51]** breadandbut workflows of AI engineers around the world as we build

**[02:52]** around the world as we build

**[02:52]** around the world as we build applications and try to improve our

**[02:54]** applications and try to improve our

**[02:54]** applications and try to improve our systems and models and products.

**[02:57]** systems and models and products.

**[02:57]** systems and models and products. And I think a thing people are kind of

**[02:59]** And I think a thing people are kind of

**[02:59]** And I think a thing people are kind of iffy about in terms of AI is whether


### [03:00 - 04:00]

**[03:01]** iffy about in terms of AI is whether

**[03:02]** iffy about in terms of AI is whether open source models are going to work.

**[03:03]** open source models are going to work.

**[03:03]** open source models are going to work. And in my mind, that's not quite the

**[03:05]** And in my mind, that's not quite the

**[03:05]** And in my mind, that's not quite the right analogy to draw. And so when we're

**[03:07]** right analogy to draw. And so when we're

**[03:07]** right analogy to draw. And so when we're comparing like AI to traditional

**[03:08]** comparing like AI to traditional

**[03:08]** comparing like AI to traditional software, there's lots of like great

**[03:11]** software, there's lots of like great

**[03:11]** software, there's lots of like great examples of open source software

**[03:12]** examples of open source software

**[03:12]** examples of open source software ecosystems that have been thriving in

**[03:14]** ecosystems that have been thriving in

**[03:14]** ecosystems that have been thriving in the past, things like Linux and Node and

**[03:16]** the past, things like Linux and Node and

**[03:16]** the past, things like Linux and Node and Apache. But in my mind, the analogy in

**[03:19]** Apache. But in my mind, the analogy in

**[03:19]** Apache. But in my mind, the analogy in AI is not models as kind of these fixed

**[03:21]** AI is not models as kind of these fixed

**[03:22]** AI is not models as kind of these fixed checkpoints, but it's about research as

**[03:23]** checkpoints, but it's about research as

**[03:23]** checkpoints, but it's about research as a practice and research as a set of

**[03:25]** a practice and research as a set of

**[03:25]** a practice and research as a set of ideas. And it's one that's more

**[03:27]** ideas. And it's one that's more

**[03:27]** ideas. And it's one that's more intangible, but there's a lot of

**[03:29]** intangible, but there's a lot of

**[03:29]** intangible, but there's a lot of parallels in terms of the goals of the

**[03:31]** parallels in terms of the goals of the

**[03:32]** parallels in terms of the goals of the best practices of growing a research

**[03:33]** best practices of growing a research

**[03:33]** best practices of growing a research ecosystem as well as a software

**[03:34]** ecosystem as well as a software

**[03:34]** ecosystem as well as a software ecosystem where you want to uh compound

**[03:37]** ecosystem where you want to uh compound

**[03:37]** ecosystem where you want to uh compound abstractions and best practices and have

**[03:38]** abstractions and best practices and have

**[03:38]** abstractions and best practices and have better tooling and iteration efficiency

**[03:40]** better tooling and iteration efficiency

**[03:40]** better tooling and iteration efficiency and have these gains over time allow uh

**[03:44]** and have these gains over time allow uh

**[03:44]** and have these gains over time allow uh more advanced powerful complex things to

**[03:46]** more advanced powerful complex things to

**[03:46]** more advanced powerful complex things to be built by uh decreasing barriers to

**[03:49]** be built by uh decreasing barriers to

**[03:49]** be built by uh decreasing barriers to entry for any given application and

**[03:51]** entry for any given application and

**[03:51]** entry for any given application and allowing this to become more accessible.

**[03:54]** allowing this to become more accessible.

**[03:54]** allowing this to become more accessible. And so one thing that we a term we'll

**[03:56]** And so one thing that we a term we'll

**[03:56]** And so one thing that we a term we'll use to describe some of what we're

**[03:58]** use to describe some of what we're

**[03:58]** use to describe some of what we're building at Prime Elect is we like this

**[03:59]** building at Prime Elect is we like this

**[03:59]** building at Prime Elect is we like this phrase called the open super


### [04:00 - 05:00]

**[04:00]** phrase called the open super

**[04:00]** phrase called the open super intelligence stack. One because it's a

**[04:02]** intelligence stack. One because it's a

**[04:02]** intelligence stack. One because it's a fun acronym but also I think the idea of

**[04:04]** fun acronym but also I think the idea of

**[04:04]** fun acronym but also I think the idea of the stack of of all the pieces of the

**[04:06]** the stack of of all the pieces of the

**[04:06]** the stack of of all the pieces of the puzzle to build the engine to go do

**[04:08]** puzzle to build the engine to go do

**[04:08]** puzzle to build the engine to go do research. Uh there's a lot of layers to

**[04:10]** research. Uh there's a lot of layers to

**[04:10]** research. Uh there's a lot of layers to it. You need compute uh you need

**[04:12]** it. You need compute uh you need

**[04:12]** it. You need compute uh you need orchestration you need libraries for

**[04:14]** orchestration you need libraries for

**[04:14]** orchestration you need libraries for doing uh training and evaluation and you

**[04:16]** doing uh training and evaluation and you

**[04:16]** doing uh training and evaluation and you need platforms to support things like

**[04:19]** need platforms to support things like

**[04:19]** need platforms to support things like code execution and eval inference and

**[04:21]** code execution and eval inference and

**[04:21]** code execution and eval inference and fine-tuning and we're doing all these

**[04:22]** fine-tuning and we're doing all these

**[04:22]** fine-tuning and we're doing all these things. Uh but really the goal of this

**[04:24]** things. Uh but really the goal of this

**[04:24]** things. Uh but really the goal of this is to give people the tools to be able

**[04:27]** is to give people the tools to be able

**[04:27]** is to give people the tools to be able to go train models. We want people more

**[04:29]** to go train models. We want people more

**[04:29]** to go train models. We want people more people in the world. And we think I'll

**[04:30]** people in the world. And we think I'll

**[04:30]** people in the world. And we think I'll explain why in a bit. There's a lot of

**[04:32]** explain why in a bit. There's a lot of

**[04:32]** explain why in a bit. There's a lot of reasons why uh the best products are

**[04:35]** reasons why uh the best products are

**[04:35]** reasons why uh the best products are going to be the ones that are not just

**[04:38]** going to be the ones that are not just

**[04:38]** going to be the ones that are not just kind of taking the thing out of a box of

**[04:40]** kind of taking the thing out of a box of

**[04:40]** kind of taking the thing out of a box of an API and putting a thin wrapper around

**[04:42]** an API and putting a thin wrapper around

**[04:42]** an API and putting a thin wrapper around it. There's ways you can kind of improve

**[04:44]** it. There's ways you can kind of improve

**[04:44]** it. There's ways you can kind of improve around APIs. But I think in many cases

**[04:46]** around APIs. But I think in many cases

**[04:46]** around APIs. But I think in many cases people are realizing that winning

**[04:48]** people are realizing that winning

**[04:48]** people are realizing that winning products are going to be the kinds of

**[04:49]** products are going to be the kinds of

**[04:49]** products are going to be the kinds of things that whether it's a part of the

**[04:52]** things that whether it's a part of the

**[04:52]** things that whether it's a part of the model, a part of the stack, the part of

**[04:53]** model, a part of the stack, the part of

**[04:53]** model, a part of the stack, the part of the product or the whole thing, the

**[04:55]** the product or the whole thing, the

**[04:55]** the product or the whole thing, the ability to do research and have at least

**[04:57]** ability to do research and have at least

**[04:57]** ability to do research and have at least the option of deciding where in your

**[04:59]** the option of deciding where in your

**[04:59]** the option of deciding where in your product you might want to customize a


### [05:00 - 06:00]

**[05:01]** product you might want to customize a

**[05:01]** product you might want to customize a model or improve a model gives you a lot

**[05:02]** model or improve a model gives you a lot

**[05:02]** model or improve a model gives you a lot more flexibility to really u make the

**[05:05]** more flexibility to really u make the

**[05:05]** more flexibility to really u make the best user experience. Um,

**[05:09]** best user experience. Um,

**[05:09]** best user experience. Um, and so we have heard the phrase in the

**[05:11]** and so we have heard the phrase in the

**[05:11]** and so we have heard the phrase in the past that the model is the product. And

**[05:13]** past that the model is the product. And

**[05:13]** past that the model is the product. And I think we're starting to see now this

**[05:15]** I think we're starting to see now this

**[05:15]** I think we're starting to see now this change a little bit to a lot of winning

**[05:16]** change a little bit to a lot of winning

**[05:16]** change a little bit to a lot of winning applications have the product kind of be

**[05:18]** applications have the product kind of be

**[05:18]** applications have the product kind of be the model. And I think the two notable

**[05:20]** the model. And I think the two notable

**[05:20]** the model. And I think the two notable examples of this that I'm big fans of

**[05:22]** examples of this that I'm big fans of

**[05:22]** examples of this that I'm big fans of and heavy users of are Cursor's new

**[05:24]** and heavy users of are Cursor's new

**[05:24]** and heavy users of are Cursor's new composer model as well as uh OpenAI's

**[05:26]** composer model as well as uh OpenAI's

**[05:26]** composer model as well as uh OpenAI's codeex. And I think these are both good

**[05:28]** codeex. And I think these are both good

**[05:28]** codeex. And I think these are both good examples of models that really are where

**[05:31]** examples of models that really are where

**[05:31]** examples of models that really are where the product kind of is the model very

**[05:33]** the product kind of is the model very

**[05:33]** the product kind of is the model very directly where the the model was trained

**[05:35]** directly where the the model was trained

**[05:35]** directly where the the model was trained to be the model for that product and the

**[05:37]** to be the model for that product and the

**[05:37]** to be the model for that product and the experience of using the model is the

**[05:39]** experience of using the model is the

**[05:39]** experience of using the model is the experience of using the product. And the

**[05:41]** experience of using the product. And the

**[05:41]** experience of using the product. And the way that [clears throat] this is done is

**[05:42]** way that [clears throat] this is done is

**[05:42]** way that [clears throat] this is done is by taking a harness that represents the

**[05:44]** by taking a harness that represents the

**[05:44]** by taking a harness that represents the product and training the model in the

**[05:46]** product and training the model in the

**[05:46]** product and training the model in the harness in essentially an environment,

**[05:48]** harness in essentially an environment,

**[05:48]** harness in essentially an environment, an RL environment. And environments

**[05:50]** an RL environment. And environments

**[05:50]** an RL environment. And environments really are just a harness with a

**[05:52]** really are just a harness with a

**[05:52]** really are just a harness with a collection of tasks and rewards. But

**[05:55]** collection of tasks and rewards. But

**[05:55]** collection of tasks and rewards. But they also have many other parallels

**[05:57]** they also have many other parallels

**[05:57]** they also have many other parallels throughout the ecosystem. Environments

**[05:58]** throughout the ecosystem. Environments

**[05:58]** throughout the ecosystem. Environments are not just for RL. Environments are


### [06:00 - 07:00]

**[06:00]** are not just for RL. Environments are

**[06:00]** are not just for RL. Environments are also essentially the same thing as

**[06:02]** also essentially the same thing as

**[06:02]** also essentially the same thing as evals. Environments can also be engines

**[06:04]** evals. Environments can also be engines

**[06:04]** evals. Environments can also be engines for synthetic data which then you can

**[06:05]** for synthetic data which then you can

**[06:05]** for synthetic data which then you can use for SFT or distillation. You can do

**[06:07]** use for SFT or distillation. You can do

**[06:08]** use for SFT or distillation. You can do RL in them directly. But also the agents

**[06:09]** RL in them directly. But also the agents

**[06:10]** RL in them directly. But also the agents were actually deploying and monitoring

**[06:11]** were actually deploying and monitoring

**[06:11]** were actually deploying and monitoring out in the world. These are

**[06:12]** out in the world. These are

**[06:12]** out in the world. These are environments. The product of these

**[06:14]** environments. The product of these

**[06:14]** environments. The product of these things, the tasks, the harness, and the

**[06:16]** things, the tasks, the harness, and the

**[06:16]** things, the tasks, the harness, and the rewards, whether this is a data set

**[06:18]** rewards, whether this is a data set

**[06:18]** rewards, whether this is a data set offline or the stream of user tasks

**[06:20]** offline or the stream of user tasks

**[06:20]** offline or the stream of user tasks coming in to a product is an

**[06:22]** coming in to a product is an

**[06:22]** coming in to a product is an environment. And so this as an

**[06:24]** environment. And so this as an

**[06:24]** environment. And so this as an abstraction I think is a very useful way

**[06:26]** abstraction I think is a very useful way

**[06:26]** abstraction I think is a very useful way of framing what it might look like to

**[06:28]** of framing what it might look like to

**[06:28]** of framing what it might look like to start having uh research become more of

**[06:31]** start having uh research become more of

**[06:31]** start having uh research become more of a a practice that is adopted more

**[06:33]** a a practice that is adopted more

**[06:33]** a a practice that is adopted more broadly beyond just large AI labs. And I

**[06:37]** broadly beyond just large AI labs. And I

**[06:37]** broadly beyond just large AI labs. And I also think that there's a sense in which

**[06:38]** also think that there's a sense in which

**[06:38]** also think that there's a sense in which they're a really accessible entry point.

**[06:39]** they're a really accessible entry point.

**[06:39]** they're a really accessible entry point. Uh and so I like the analogy of

**[06:41]** Uh and so I like the analogy of

**[06:41]** Uh and so I like the analogy of environments as kind of like the web

**[06:42]** environments as kind of like the web

**[06:42]** environments as kind of like the web apps of AI research. And what I mean by

**[06:43]** apps of AI research. And what I mean by

**[06:44]** apps of AI research. And what I mean by this is that they're very simple.

**[06:46]** this is that they're very simple.

**[06:46]** this is that they're very simple. They're self-contained. They can they

**[06:47]** They're self-contained. They can they

**[06:47]** They're self-contained. They can they start simple but they can also get quite

**[06:49]** start simple but they can also get quite

**[06:49]** start simple but they can also get quite complex. They can get very elaborate

**[06:51]** complex. They can get very elaborate

**[06:51]** complex. They can get very elaborate representing the full complexity of a

**[06:52]** representing the full complexity of a

**[06:52]** representing the full complexity of a large product. They're also pedagogical

**[06:54]** large product. They're also pedagogical

**[06:54]** large product. They're also pedagogical in nature and that you can start simple

**[06:56]** in nature and that you can start simple

**[06:56]** in nature and that you can start simple and as you build complexity, you start

**[06:59]** and as you build complexity, you start

**[06:59]** and as you build complexity, you start bumping into these walls where you have


### [07:00 - 08:00]

**[07:00]** bumping into these walls where you have

**[07:00]** bumping into these walls where you have to start learning new concepts,

**[07:02]** to start learning new concepts,

**[07:02]** to start learning new concepts, understanding more about scaling the

**[07:03]** understanding more about scaling the

**[07:03]** understanding more about scaling the system side, understanding more about

**[07:05]** system side, understanding more about

**[07:05]** system side, understanding more about the hyperparameters and the algorithms

**[07:06]** the hyperparameters and the algorithms

**[07:06]** the hyperparameters and the algorithms and they kind of open this door where

**[07:08]** and they kind of open this door where

**[07:08]** and they kind of open this door where you can by playing around with them

**[07:11]** you can by playing around with them

**[07:11]** you can by playing around with them start entering into a world of research

**[07:13]** start entering into a world of research

**[07:14]** start entering into a world of research without needing to kind of build a whole

**[07:15]** without needing to kind of build a whole

**[07:15]** without needing to kind of build a whole training infrastructure system from

**[07:17]** training infrastructure system from

**[07:17]** training infrastructure system from scratch. Um, and they also require

**[07:19]** scratch. Um, and they also require

**[07:20]** scratch. Um, and they also require experimentation. And so I think the key

**[07:21]** experimentation. And so I think the key

**[07:21]** experimentation. And so I think the key different uh differentiation between

**[07:24]** different uh differentiation between

**[07:24]** different uh differentiation between just an agent harness and an agent

**[07:26]** just an agent harness and an agent

**[07:26]** just an agent harness and an agent environment is that the environment

**[07:28]** environment is that the environment

**[07:28]** environment is that the environment forces you to also have your tasks and

**[07:30]** forces you to also have your tasks and

**[07:30]** forces you to also have your tasks and your rewards predefined to be able to do

**[07:32]** your rewards predefined to be able to do

**[07:32]** your rewards predefined to be able to do this experimentation. It's a proper

**[07:33]** this experimentation. It's a proper

**[07:33]** this experimentation. It's a proper eval. And what this means is that you

**[07:36]** eval. And what this means is that you

**[07:36]** eval. And what this means is that you can't just vibe check it. You can't just

**[07:39]** can't just vibe check it. You can't just

**[07:39]** can't just vibe check it. You can't just like build it and test it out a bit and

**[07:40]** like build it and test it out a bit and

**[07:40]** like build it and test it out a bit and say, "Hey, it's good. We're going to

**[07:41]** say, "Hey, it's good. We're going to

**[07:41]** say, "Hey, it's good. We're going to ship it." It forces you to say, "Okay,

**[07:44]** ship it." It forces you to say, "Okay,

**[07:44]** ship it." It forces you to say, "Okay, let's think about this a little more

**[07:45]** let's think about this a little more

**[07:45]** let's think about this a little more scientifically. Let's do some

**[07:46]** scientifically. Let's do some

**[07:46]** scientifically. Let's do some experiments. lets try out different

**[07:47]** experiments. lets try out different

**[07:48]** experiments. lets try out different models, try different hyperparameters.

**[07:49]** models, try different hyperparameters.

**[07:49]** models, try different hyperparameters. Uh, and it also gets you to the point

**[07:51]** Uh, and it also gets you to the point

**[07:51]** Uh, and it also gets you to the point where you can start doing more advanced

**[07:54]** where you can start doing more advanced

**[07:54]** where you can start doing more advanced research in terms of RL training or

**[07:55]** research in terms of RL training or

**[07:55]** research in terms of RL training or distillation or fine-tuning. And uh, so

**[07:58]** distillation or fine-tuning. And uh, so

**[07:58]** distillation or fine-tuning. And uh, so to really facilitate this, we wanted to


### [08:00 - 09:00]

**[08:01]** to really facilitate this, we wanted to

**[08:01]** to really facilitate this, we wanted to make the environment as an entry point

**[08:03]** make the environment as an entry point

**[08:03]** make the environment as an entry point much more accessible. A few months back,

**[08:04]** much more accessible. A few months back,

**[08:04]** much more accessible. A few months back, we launched what we called the

**[08:06]** we launched what we called the

**[08:06]** we launched what we called the environments hub, which is a open source

**[08:07]** environments hub, which is a open source

**[08:08]** environments hub, which is a open source community platform for creating,

**[08:09]** community platform for creating,

**[08:09]** community platform for creating, discovering, and sharing RL environments

**[08:12]** discovering, and sharing RL environments

**[08:12]** discovering, and sharing RL environments and evals. And so far, we've had a lot

**[08:14]** and evals. And so far, we've had a lot

**[08:14]** and evals. And so far, we've had a lot of fun kind of seeing everyone build

**[08:15]** of fun kind of seeing everyone build

**[08:15]** of fun kind of seeing everyone build here. We've had hundreds of builders and

**[08:17]** here. We've had hundreds of builders and

**[08:17]** here. We've had hundreds of builders and environments come create either their

**[08:19]** environments come create either their

**[08:19]** environments come create either their own ideas or re-implement papers. Uh

**[08:22]** own ideas or re-implement papers. Uh

**[08:22]** own ideas or re-implement papers. Uh there's a bunch of examples here I can

**[08:23]** there's a bunch of examples here I can

**[08:24]** there's a bunch of examples here I can show you, but really it's just a bunch

**[08:25]** show you, but really it's just a bunch

**[08:25]** show you, but really it's just a bunch of people who have wanted to do research

**[08:28]** of people who have wanted to do research

**[08:28]** of people who have wanted to do research and found this as an entry point to

**[08:30]** and found this as an entry point to

**[08:30]** and found this as an entry point to start digging a little deeper. Whether

**[08:32]** start digging a little deeper. Whether

**[08:32]** start digging a little deeper. Whether this was investigating some benchmark

**[08:33]** this was investigating some benchmark

**[08:33]** this was investigating some benchmark and figuring out how to reimplement it

**[08:35]** and figuring out how to reimplement it

**[08:35]** and figuring out how to reimplement it or modify it to be appropriate for an RL

**[08:37]** or modify it to be appropriate for an RL

**[08:37]** or modify it to be appropriate for an RL context in terms of like new data or new

**[08:39]** context in terms of like new data or new

**[08:39]** context in terms of like new data or new examples or whether [snorts] this is

**[08:41]** examples or whether [snorts] this is

**[08:41]** examples or whether [snorts] this is some game that they'd been thinking

**[08:42]** some game that they'd been thinking

**[08:42]** some game that they'd been thinking about or some other task. But having

**[08:45]** about or some other task. But having

**[08:45]** about or some other task. But having this as an abstraction for encapsulating

**[08:47]** this as an abstraction for encapsulating

**[08:47]** this as an abstraction for encapsulating the the thing you want a model to do is

**[08:49]** the the thing you want a model to do is

**[08:50]** the the thing you want a model to do is a way of allowing yourself to start

**[08:51]** a way of allowing yourself to start

**[08:52]** a way of allowing yourself to start experimenting with ways of improving it

**[08:53]** experimenting with ways of improving it

**[08:53]** experimenting with ways of improving it without needing to have the answers. So

**[08:55]** without needing to have the answers. So

**[08:55]** without needing to have the answers. So I think people talk a lot about how

**[08:57]** I think people talk a lot about how

**[08:57]** I think people talk a lot about how fine-tuning never really took off in the

**[08:58]** fine-tuning never really took off in the

**[08:58]** fine-tuning never really took off in the SFT regime. And I think a big part of


### [09:00 - 10:00]

**[09:00]** SFT regime. And I think a big part of

**[09:00]** SFT regime. And I think a big part of this is that getting data was really

**[09:02]** this is that getting data was really

**[09:02]** this is that getting data was really hard of the actual like solutions. I

**[09:04]** hard of the actual like solutions. I

**[09:04]** hard of the actual like solutions. I think having labeled examples of what

**[09:06]** think having labeled examples of what

**[09:06]** think having labeled examples of what you want the model to do is a very

**[09:08]** you want the model to do is a very

**[09:08]** you want the model to do is a very difficult thing to ask someone to go

**[09:10]** difficult thing to ask someone to go

**[09:10]** difficult thing to ask someone to go create. But if you can just think about

**[09:12]** create. But if you can just think about

**[09:12]** create. But if you can just think about the the settings it might be in without

**[09:14]** the the settings it might be in without

**[09:14]** the the settings it might be in without having the answers up front, if you can

**[09:16]** having the answers up front, if you can

**[09:16]** having the answers up front, if you can measure the answers, now you kind of can

**[09:18]** measure the answers, now you kind of can

**[09:18]** measure the answers, now you kind of can start creating data on the fly. And this

**[09:20]** start creating data on the fly. And this

**[09:20]** start creating data on the fly. And this engine is really what the environment is

**[09:22]** engine is really what the environment is

**[09:22]** engine is really what the environment is about unlocking. Um, and so actually 9

**[09:26]** about unlocking. Um, and so actually 9

**[09:26]** about unlocking. Um, and so actually 9 months ago, I was right here in this

**[09:27]** months ago, I was right here in this

**[09:27]** months ago, I was right here in this room. I had just released a library

**[09:29]** room. I had just released a library

**[09:29]** room. I had just released a library called verifiers, which I'm still

**[09:31]** called verifiers, which I'm still

**[09:31]** called verifiers, which I'm still working on today. Um, it's come a long

**[09:33]** working on today. Um, it's come a long

**[09:33]** working on today. Um, it's come a long way, but it's a toolkit for building

**[09:35]** way, but it's a toolkit for building

**[09:35]** way, but it's a toolkit for building these things. And it's been a lot of fun

**[09:38]** these things. And it's been a lot of fun

**[09:38]** these things. And it's been a lot of fun over this past year just playing with it

**[09:40]** over this past year just playing with it

**[09:40]** over this past year just playing with it and extending it to support more

**[09:42]** and extending it to support more

**[09:42]** and extending it to support more features and kinds of environments. But

**[09:43]** features and kinds of environments. But

**[09:44]** features and kinds of environments. But the idea with verifiers is to give

**[09:45]** the idea with verifiers is to give

**[09:45]** the idea with verifiers is to give people a toolkit that is uh essentially

**[09:47]** people a toolkit that is uh essentially

**[09:48]** people a toolkit that is uh essentially a bunch of components that you can mix

**[09:49]** a bunch of components that you can mix

**[09:49]** a bunch of components that you can mix and match and compose to do things like

**[09:51]** and match and compose to do things like

**[09:51]** and match and compose to do things like from simple evals or QA or games to

**[09:54]** from simple evals or QA or games to

**[09:54]** from simple evals or QA or games to things like tool use or using sandboxes

**[09:55]** things like tool use or using sandboxes

**[09:55]** things like tool use or using sandboxes or agent frameworks or uh uh like CLI

**[09:58]** or agent frameworks or uh uh like CLI

**[09:58]** or agent frameworks or uh uh like CLI coding agents or math problems. There's


### [10:00 - 11:00]

**[10:00]** coding agents or math problems. There's

**[10:00]** coding agents or math problems. There's all sorts of things you might want

**[10:01]** all sorts of things you might want

**[10:01]** all sorts of things you might want models to do or agents to do. And it's a

**[10:04]** models to do or agents to do. And it's a

**[10:04]** models to do or agents to do. And it's a toolkit for building environments that

**[10:05]** toolkit for building environments that

**[10:05]** toolkit for building environments that is then uh ready to be automatically

**[10:07]** is then uh ready to be automatically

**[10:07]** is then uh ready to be automatically trained with reinforcement learning. And

**[10:10]** trained with reinforcement learning. And

**[10:10]** trained with reinforcement learning. And the way we thought about this design,

**[10:12]** the way we thought about this design,

**[10:12]** the way we thought about this design, it's been a lot of fun and also a big

**[10:14]** it's been a lot of fun and also a big

**[10:14]** it's been a lot of fun and also a big challenge to think like okay, how do you

**[10:15]** challenge to think like okay, how do you

**[10:16]** challenge to think like okay, how do you make a toolkit for this stuff that

**[10:18]** make a toolkit for this stuff that

**[10:18]** make a toolkit for this stuff that actually covers all the bases? And I

**[10:19]** actually covers all the bases? And I

**[10:19]** actually covers all the bases? And I think there's a lot of different

**[10:21]** think there's a lot of different

**[10:21]** think there's a lot of different approaches I've seen people go about and

**[10:23]** approaches I've seen people go about and

**[10:23]** approaches I've seen people go about and I I think they all make sense depending

**[10:24]** I I think they all make sense depending

**[10:24]** I I think they all make sense depending on what sorts of things you're wanting

**[10:26]** on what sorts of things you're wanting

**[10:26]** on what sorts of things you're wanting to work on. But we took a very kind of a

**[10:29]** to work on. But we took a very kind of a

**[10:29]** to work on. But we took a very kind of a general approach where we tried to say

**[10:31]** general approach where we tried to say

**[10:31]** general approach where we tried to say we are not going to know all the answers

**[10:33]** we are not going to know all the answers

**[10:33]** we are not going to know all the answers right away. There are going to be lots

**[10:34]** right away. There are going to be lots

**[10:34]** right away. There are going to be lots of pattern. There's going to be lots of

**[10:36]** of pattern. There's going to be lots of

**[10:36]** of pattern. There's going to be lots of special cases. There's going to be

**[10:38]** special cases. There's going to be

**[10:38]** special cases. There's going to be hierarchies of complexity. There's going

**[10:39]** hierarchies of complexity. There's going

**[10:39]** hierarchies of complexity. There's going to be patterns. And we really wanted to

**[10:41]** to be patterns. And we really wanted to

**[10:41]** to be patterns. And we really wanted to prioritize extensibility. So we think

**[10:43]** prioritize extensibility. So we think

**[10:43]** prioritize extensibility. So we think about these things hierarchically where

**[10:45]** about these things hierarchically where

**[10:45]** about these things hierarchically where let's say you want to do a a coding

**[10:46]** let's say you want to do a a coding

**[10:46]** let's say you want to do a a coding agent environment for client bench. uh

**[10:49]** agent environment for client bench. uh

**[10:49]** agent environment for client bench. uh this which is an instance of the harbor

**[10:51]** this which is an instance of the harbor

**[10:51]** this which is an instance of the harbor framework which is a example of a CLI

**[10:54]** framework which is a example of a CLI

**[10:54]** framework which is a example of a CLI agent which is a multi-turn environment

**[10:56]** agent which is a multi-turn environment

**[10:56]** agent which is a multi-turn environment which is an environment uh similar for

**[10:58]** which is an environment uh similar for

**[10:58]** which is an environment uh similar for text arrina and Wordle or for search


### [11:00 - 12:00]

**[11:00]** text arrina and Wordle or for search

**[11:00]** text arrina and Wordle or for search with MCP or for giving a model a Python

**[11:02]** with MCP or for giving a model a Python

**[11:02]** with MCP or for giving a model a Python ripple in a sandbox and so thinking of

**[11:04]** ripple in a sandbox and so thinking of

**[11:04]** ripple in a sandbox and so thinking of these things hierarchically allows us to

**[11:06]** these things hierarchically allows us to

**[11:06]** these things hierarchically allows us to kind of really determine like what are

**[11:07]** kind of really determine like what are

**[11:08]** kind of really determine like what are the foundational pieces what is generic

**[11:09]** the foundational pieces what is generic

**[11:09]** the foundational pieces what is generic across all environments and then how do

**[11:11]** across all environments and then how do

**[11:11]** across all environments and then how do you build up the stack towards

**[11:13]** you build up the stack towards

**[11:13]** you build up the stack towards applications

**[11:14]** applications

**[11:14]** applications and so for one like example of this that

**[11:16]** and so for one like example of this that

**[11:16]** and so for one like example of this that I'll kind of walk through the whole

**[11:17]** I'll kind of walk through the whole

**[11:17]** I'll kind of walk through the whole process end to And we we call this one

**[11:19]** process end to And we we call this one

**[11:19]** process end to And we we call this one wiki search, but it's basically a simple

**[11:21]** wiki search, but it's basically a simple

**[11:21]** wiki search, but it's basically a simple search setting where we give an agent

**[11:23]** search setting where we give an agent

**[11:23]** search setting where we give an agent the ability to uh call some tools to

**[11:26]** the ability to uh call some tools to

**[11:26]** the ability to uh call some tools to search over Wikipedia pages and find

**[11:28]** search over Wikipedia pages and find

**[11:28]** search over Wikipedia pages and find some answers. And so here is the

**[11:29]** some answers. And so here is the

**[11:29]** some answers. And so here is the environments hub page. So the

**[11:30]** environments hub page. So the

**[11:30]** environments hub page. So the environments hub is a kind of full stack

**[11:32]** environments hub is a kind of full stack

**[11:32]** environments hub is a kind of full stack uh code management package registry. So

**[11:36]** uh code management package registry. So

**[11:36]** uh code management package registry. So every environment is a Python project

**[11:37]** every environment is a Python project

**[11:37]** every environment is a Python project where you can have dependencies and

**[11:39]** where you can have dependencies and

**[11:39]** where you can have dependencies and versions and uploading your evals and

**[11:41]** versions and uploading your evals and

**[11:41]** versions and uploading your evals and whatnot. Um but the environments are

**[11:43]** whatnot. Um but the environments are

**[11:43]** whatnot. Um but the environments are very simple. They start simple. They can

**[11:45]** very simple. They start simple. They can

**[11:45]** very simple. They start simple. They can get really complicated, but this one's

**[11:46]** get really complicated, but this one's

**[11:46]** get really complicated, but this one's pretty simple where we just kind of

**[11:48]** pretty simple where we just kind of

**[11:48]** pretty simple where we just kind of define our tools as async Python

**[11:49]** define our tools as async Python

**[11:49]** define our tools as async Python functions. We have our data set and we

**[11:52]** functions. We have our data set and we

**[11:52]** functions. We have our data set and we have what we call a rubric. And so a

**[11:53]** have what we call a rubric. And so a

**[11:53]** have what we call a rubric. And so a rubric is the abstraction for managing

**[11:55]** rubric is the abstraction for managing

**[11:55]** rubric is the abstraction for managing the different pieces of your rewards

**[11:57]** the different pieces of your rewards

**[11:57]** the different pieces of your rewards where you can kind of compose different

**[11:58]** where you can kind of compose different

**[11:58]** where you can kind of compose different things. You can also have metrics that


### [12:00 - 13:00]

**[12:00]** things. You can also have metrics that

**[12:00]** things. You can also have metrics that are just a zero award but are for in uh

**[12:03]** are just a zero award but are for in uh

**[12:03]** are just a zero award but are for in uh observability of what's going on. And

**[12:05]** observability of what's going on. And

**[12:05]** observability of what's going on. And then the other piece of doing training

**[12:07]** then the other piece of doing training

**[12:07]** then the other piece of doing training will be a config. And so the config here

**[12:08]** will be a config. And so the config here

**[12:08]** will be a config. And so the config here is for our prime RL trainer, which is

**[12:10]** is for our prime RL trainer, which is

**[12:10]** is for our prime RL trainer, which is our kind of large scale training stack,

**[12:12]** our kind of large scale training stack,

**[12:12]** our kind of large scale training stack, which has been our uh culmination of all

**[12:15]** which has been our uh culmination of all

**[12:15]** which has been our uh culmination of all the best practices from the research

**[12:16]** the best practices from the research

**[12:16]** the best practices from the research literature for large scale asynchronous

**[12:18]** literature for large scale asynchronous

**[12:18]** literature for large scale asynchronous RL training. Um, but the config files

**[12:20]** RL training. Um, but the config files

**[12:20]** RL training. Um, but the config files are intended to expose kind of the

**[12:21]** are intended to expose kind of the

**[12:21]** are intended to expose kind of the pieces that people need to think about

**[12:23]** pieces that people need to think about

**[12:23]** pieces that people need to think about in ways that are starting to get you

**[12:25]** in ways that are starting to get you

**[12:25]** in ways that are starting to get you more into the algorithm, but are also

**[12:27]** more into the algorithm, but are also

**[12:27]** more into the algorithm, but are also still designed to be pretty high level,

**[12:30]** still designed to be pretty high level,

**[12:30]** still designed to be pretty high level, pretty self-contained, and with with

**[12:31]** pretty self-contained, and with with

**[12:31]** pretty self-contained, and with with defaults that we think are going to be

**[12:32]** defaults that we think are going to be

**[12:32]** defaults that we think are going to be sensible for a lot of people. And so

**[12:35]** sensible for a lot of people. And so

**[12:35]** sensible for a lot of people. And so running this is just kind of running a

**[12:37]** running this is just kind of running a

**[12:37]** running this is just kind of running a command line with uh you specify the

**[12:39]** command line with uh you specify the

**[12:39]** command line with uh you specify the environment and if it's in the

**[12:40]** environment and if it's in the

**[12:40]** environment and if it's in the environment hub it'll automatically

**[12:42]** environment hub it'll automatically

**[12:42]** environment hub it'll automatically install it and start your training run

**[12:43]** install it and start your training run

**[12:43]** install it and start your training run and then you can if you're lucky see

**[12:45]** and then you can if you're lucky see

**[12:45]** and then you can if you're lucky see your reward curve just shoot right up.

**[12:47]** your reward curve just shoot right up.

**[12:47]** your reward curve just shoot right up. Um and sometimes it doesn't go this

**[12:49]** Um and sometimes it doesn't go this

**[12:50]** Um and sometimes it doesn't go this nicely but the process of doing this is

**[12:52]** nicely but the process of doing this is

**[12:52]** nicely but the process of doing this is iterating on your environment on your

**[12:54]** iterating on your environment on your

**[12:54]** iterating on your environment on your rewards and your data and your tasks to

**[12:57]** rewards and your data and your tasks to

**[12:57]** rewards and your data and your tasks to understand what makes this task

**[12:59]** understand what makes this task

**[12:59]** understand what makes this task holistically actually tangible in


### [13:00 - 14:00]

**[13:01]** holistically actually tangible in

**[13:01]** holistically actually tangible in practice. How do you tune the

**[13:02]** practice. How do you tune the

**[13:02]** practice. How do you tune the parameters? How do you look at your

**[13:03]** parameters? How do you look at your

**[13:03]** parameters? How do you look at your data? How do you define your rewards?

**[13:05]** data? How do you define your rewards?

**[13:05]** data? How do you define your rewards? Uh, and if you do this right, you can

**[13:06]** Uh, and if you do this right, you can

**[13:06]** Uh, and if you do this right, you can get really good improvements, especially

**[13:08]** get really good improvements, especially

**[13:08]** get really good improvements, especially from really small models, but also for

**[13:09]** from really small models, but also for

**[13:09]** from really small models, but also for much larger models. And so in this

**[13:11]** much larger models. And so in this

**[13:11]** much larger models. And so in this example for the the wiki search one, we

**[13:13]** example for the the wiki search one, we

**[13:13]** example for the the wiki search one, we started with a a Quen 3 4B model, which

**[13:15]** started with a a Quen 3 4B model, which

**[13:15]** started with a a Quen 3 4B model, which was about 55%. And after training, it

**[13:17]** was about 55%. And after training, it

**[13:17]** was about 55%. And after training, it was at 89% on par with uh much larger

**[13:20]** was at 89% on par with uh much larger

**[13:20]** was at 89% on par with uh much larger models like GPT4.1 as well as reasoning

**[13:22]** models like GPT4.1 as well as reasoning

**[13:22]** models like GPT4.1 as well as reasoning models like uh GBD5 mini. And so I think

**[13:25]** models like uh GBD5 mini. And so I think

**[13:25]** models like uh GBD5 mini. And so I think this practice of taking small models and

**[13:27]** this practice of taking small models and

**[13:27]** this practice of taking small models and being able to make them much better is a

**[13:29]** being able to make them much better is a

**[13:30]** being able to make them much better is a big win for a lot of applications where

**[13:31]** big win for a lot of applications where

**[13:31]** big win for a lot of applications where you either you want a really fast model,

**[13:33]** you either you want a really fast model,

**[13:33]** you either you want a really fast model, you want a really cheap model, you want

**[13:34]** you want a really cheap model, you want

**[13:34]** you want a really cheap model, you want a really really powerful model because

**[13:35]** a really really powerful model because

**[13:35]** a really really powerful model because the best models out there just aren't

**[13:37]** the best models out there just aren't

**[13:37]** the best models out there just aren't quite good enough. These are all the

**[13:38]** quite good enough. These are all the

**[13:38]** quite good enough. These are all the different things you can do with model

**[13:39]** different things you can do with model

**[13:40]** different things you can do with model customization. And this practice of

**[13:42]** customization. And this practice of

**[13:42]** customization. And this practice of doing of creating environments isn't

**[13:44]** doing of creating environments isn't

**[13:44]** doing of creating environments isn't only for customization, but it gives you

**[13:46]** only for customization, but it gives you

**[13:46]** only for customization, but it gives you this option. And so if you need to do

**[13:48]** this option. And so if you need to do

**[13:48]** this option. And so if you need to do eval anyways, it's useful to think of

**[13:50]** eval anyways, it's useful to think of

**[13:50]** eval anyways, it's useful to think of them as environments because the

**[13:51]** them as environments because the

**[13:51]** them as environments because the environment opens a lot of doors for

**[13:55]** environment opens a lot of doors for

**[13:55]** environment opens a lot of doors for whether this is prompt tuning or whether

**[13:56]** whether this is prompt tuning or whether

**[13:56]** whether this is prompt tuning or whether it's model selection or whether it's

**[13:59]** it's model selection or whether it's

**[13:59]** it's model selection or whether it's just getting a better sense of how your


### [14:00 - 15:00]

**[14:01]** just getting a better sense of how your

**[14:01]** just getting a better sense of how your system could work at scale with many

**[14:03]** system could work at scale with many

**[14:03]** system could work at scale with many many users in parallel. It's a design

**[14:05]** many users in parallel. It's a design

**[14:05]** many users in parallel. It's a design process that really forces you to kind

**[14:06]** process that really forces you to kind

**[14:06]** process that really forces you to kind of pin down what is the thing I care

**[14:08]** of pin down what is the thing I care

**[14:08]** of pin down what is the thing I care about? What is my agent? What is my

**[14:10]** about? What is my agent? What is my

**[14:10]** about? What is my agent? What is my product? What is my harness? What am I

**[14:12]** product? What is my harness? What am I

**[14:12]** product? What is my harness? What am I optimizing for? Um, and so to kind of

**[14:15]** optimizing for? Um, and so to kind of

**[14:15]** optimizing for? Um, and so to kind of fully stress test this, we've been

**[14:16]** fully stress test this, we've been

**[14:16]** fully stress test this, we've been training a large model which will be out

**[14:18]** training a large model which will be out

**[14:18]** training a large model which will be out into the world quite soon called

**[14:19]** into the world quite soon called

**[14:19]** into the world quite soon called Intellect 3 with our full primal L

**[14:21]** Intellect 3 with our full primal L

**[14:21]** Intellect 3 with our full primal L stack. And this has been us really kind

**[14:23]** stack. And this has been us really kind

**[14:23]** stack. And this has been us really kind of validating the efficiency and

**[14:25]** of validating the efficiency and

**[14:25]** of validating the efficiency and performance at a very large scale. So

**[14:27]** performance at a very large scale. So

**[14:27]** performance at a very large scale. So this is a 100B plus model trained on 500

**[14:29]** this is a 100B plus model trained on 500

**[14:29]** this is a 100B plus model trained on 500 GPUs where we've kind of done the

**[14:31]** GPUs where we've kind of done the

**[14:31]** GPUs where we've kind of done the endtoend uh post train of SFT and RL

**[14:33]** endtoend uh post train of SFT and RL

**[14:34]** endtoend uh post train of SFT and RL which the primaril stack also has SFT if

**[14:36]** which the primaril stack also has SFT if

**[14:36]** which the primaril stack also has SFT if people want to do that. But it's also

**[14:38]** people want to do that. But it's also

**[14:38]** people want to do that. But it's also been about just understanding all the

**[14:39]** been about just understanding all the

**[14:39]** been about just understanding all the best practices. We love reading papers

**[14:41]** best practices. We love reading papers

**[14:41]** best practices. We love reading papers and we try to kind of try out all the

**[14:43]** and we try to kind of try out all the

**[14:43]** and we try to kind of try out all the tricks and see which ones work and see

**[14:45]** tricks and see which ones work and see

**[14:45]** tricks and see which ones work and see which ones don't and then distill this

**[14:47]** which ones don't and then distill this

**[14:47]** which ones don't and then distill this into a library with Primaril that can

**[14:49]** into a library with Primaril that can

**[14:49]** into a library with Primaril that can then be kind of consumed by the end user

**[14:51]** then be kind of consumed by the end user

**[14:51]** then be kind of consumed by the end user without needing to do all this uh

**[14:53]** without needing to do all this uh

**[14:53]** without needing to do all this uh implementation themselves. And so for us

**[14:55]** implementation themselves. And so for us

**[14:56]** implementation themselves. And so for us it being open is very important. So

**[14:57]** it being open is very important. So

**[14:57]** it being open is very important. So Primaril is on GitHub. You can go find

**[14:59]** Primaril is on GitHub. You can go find

**[14:59]** Primaril is on GitHub. You can go find it. Verifiers is on GitHub if you want


### [15:00 - 16:00]

**[15:01]** it. Verifiers is on GitHub if you want

**[15:01]** it. Verifiers is on GitHub if you want to check it out. And for us, this is

**[15:03]** to check it out. And for us, this is

**[15:03]** to check it out. And for us, this is really about opening the door for more

**[15:05]** really about opening the door for more

**[15:05]** really about opening the door for more people to start learning about these

**[15:07]** people to start learning about these

**[15:07]** people to start learning about these things and for incorporating it into

**[15:08]** things and for incorporating it into

**[15:08]** things and for incorporating it into their workflows for optimizing their

**[15:10]** their workflows for optimizing their

**[15:10]** their workflows for optimizing their models and their products. Um, and

**[15:13]** models and their products. Um, and

**[15:13]** models and their products. Um, and [clears throat] the only way to do this

**[15:14]** [clears throat] the only way to do this

**[15:14]** [clears throat] the only way to do this that we've what we see as the best way

**[15:16]** that we've what we see as the best way

**[15:16]** that we've what we see as the best way to do this is through growing community.

**[15:17]** to do this is through growing community.

**[15:17]** to do this is through growing community. And so for us, it's been really

**[15:18]** And so for us, it's been really

**[15:18]** And so for us, it's been really important to really think about getting

**[15:21]** important to really think about getting

**[15:21]** important to really think about getting good feedback loops from the people who

**[15:23]** good feedback loops from the people who

**[15:23]** good feedback loops from the people who are building with this and understanding

**[15:25]** are building with this and understanding

**[15:25]** are building with this and understanding what they want, understanding what's

**[15:26]** what they want, understanding what's

**[15:26]** what they want, understanding what's going well, understanding what's

**[15:28]** going well, understanding what's

**[15:28]** going well, understanding what's painful, and addressing those problems.

**[15:29]** painful, and addressing those problems.

**[15:30]** painful, and addressing those problems. And so we've done a number of community

**[15:31]** And so we've done a number of community

**[15:31]** And so we've done a number of community programs in terms of sponsoring

**[15:33]** programs in terms of sponsoring

**[15:33]** programs in terms of sponsoring different kind of small tasks to uh a

**[15:35]** different kind of small tasks to uh a

**[15:35]** different kind of small tasks to uh a research residency program with uh grad

**[15:37]** research residency program with uh grad

**[15:37]** research residency program with uh grad students around the world uh and

**[15:39]** students around the world uh and

**[15:39]** students around the world uh and collecting like uh a smaller subset of

**[15:41]** collecting like uh a smaller subset of

**[15:41]** collecting like uh a smaller subset of the environment hub ones where we'll

**[15:42]** the environment hub ones where we'll

**[15:42]** the environment hub ones where we'll actually review them manually. And so

**[15:44]** actually review them manually. And so

**[15:44]** actually review them manually. And so this repo here, the prime environments

**[15:45]** this repo here, the prime environments

**[15:45]** this repo here, the prime environments repo is the ones where we are doing

**[15:47]** repo is the ones where we are doing

**[15:47]** repo is the ones where we are doing these directly where we're kind of

**[15:49]** these directly where we're kind of

**[15:49]** these directly where we're kind of offering to look over someone's kind of

**[15:51]** offering to look over someone's kind of

**[15:51]** offering to look over someone's kind of example. And so we've had hundreds of

**[15:54]** example. And so we've had hundreds of

**[15:54]** example. And so we've had hundreds of these come in and there will be hundreds

**[15:55]** these come in and there will be hundreds

**[15:55]** these come in and there will be hundreds more. And uh it's been a great learning

**[15:57]** more. And uh it's been a great learning

**[15:57]** more. And uh it's been a great learning process because it's forced us to fix a

**[15:59]** process because it's forced us to fix a

**[15:59]** process because it's forced us to fix a lot of things. We kind of understand the


### [16:00 - 17:00]

**[16:00]** lot of things. We kind of understand the

**[16:00]** lot of things. We kind of understand the rough edges. We understand what we need

**[16:02]** rough edges. We understand what we need

**[16:02]** rough edges. We understand what we need to add. And we're kind of then

**[16:05]** to add. And we're kind of then

**[16:05]** to add. And we're kind of then distilling [clears throat] all of these

**[16:06]** distilling [clears throat] all of these

**[16:06]** distilling [clears throat] all of these learnings into what will be our kind of

**[16:08]** learnings into what will be our kind of

**[16:08]** learnings into what will be our kind of upcoming uh platform product which we're

**[16:10]** upcoming uh platform product which we're

**[16:10]** upcoming uh platform product which we're calling lab. And the idea of lab is to

**[16:13]** calling lab. And the idea of lab is to

**[16:13]** calling lab. And the idea of lab is to give people an interface, a platform

**[16:15]** give people an interface, a platform

**[16:15]** give people an interface, a platform where they can browse environments, they

**[16:17]** where they can browse environments, they

**[16:17]** where they can browse environments, they can run their evals, they can do their

**[16:18]** can run their evals, they can do their

**[16:18]** can run their evals, they can do their inference, they can do their fine-tuning

**[16:20]** inference, they can do their fine-tuning

**[16:20]** inference, they can do their fine-tuning and they can have research be more

**[16:23]** and they can have research be more

**[16:23]** and they can have research be more accessible in a way that it hasn't been

**[16:25]** accessible in a way that it hasn't been

**[16:25]** accessible in a way that it hasn't been historically because I think a lot of

**[16:27]** historically because I think a lot of

**[16:27]** historically because I think a lot of people find infrastructure very painful.

**[16:29]** people find infrastructure very painful.

**[16:29]** people find infrastructure very painful. They find dealing with torch versions

**[16:32]** They find dealing with torch versions

**[16:32]** They find dealing with torch versions painful, flash attention and VLM and

**[16:33]** painful, flash attention and VLM and

**[16:34]** painful, flash attention and VLM and getting all these things to work. We are

**[16:36]** getting all these things to work. We are

**[16:36]** getting all these things to work. We are happy to do that, but we understand that

**[16:38]** happy to do that, but we understand that

**[16:38]** happy to do that, but we understand that a lot of people may not want to. Um, and

**[16:40]** a lot of people may not want to. Um, and

**[16:40]** a lot of people may not want to. Um, and so the idea with this is that if you

**[16:42]** so the idea with this is that if you

**[16:42]** so the idea with this is that if you want to go read the code, you can go

**[16:44]** want to go read the code, you can go

**[16:44]** want to go read the code, you can go read the code, but you don't have to run

**[16:46]** read the code, but you don't have to run

**[16:46]** read the code, but you don't have to run it. We can run it for you. Um, and so

**[16:48]** it. We can run it for you. Um, and so

**[16:48]** it. We can run it for you. Um, and so this has been our version, which will be

**[16:50]** this has been our version, which will be

**[16:50]** this has been our version, which will be kind of out into the world in the near

**[16:52]** kind of out into the world in the near

**[16:52]** kind of out into the world in the near future of trying to allow people to

**[16:55]** future of trying to allow people to

**[16:55]** future of trying to allow people to really focus on the environment where

**[16:56]** really focus on the environment where

**[16:56]** really focus on the environment where the entry point to lab will be the

**[16:59]** the entry point to lab will be the

**[16:59]** the entry point to lab will be the environment. If you want to do synthetic


### [17:00 - 18:00]

**[17:00]** environment. If you want to do synthetic

**[17:00]** environment. If you want to do synthetic data and SFT build, let's build an

**[17:02]** data and SFT build, let's build an

**[17:02]** data and SFT build, let's build an environment. If you want to do your

**[17:03]** environment. If you want to do your

**[17:03]** environment. If you want to do your evals, you build that as an environment.

**[17:04]** evals, you build that as an environment.

**[17:04]** evals, you build that as an environment. If you want to do RL, you build an

**[17:05]** If you want to do RL, you build an

**[17:05]** If you want to do RL, you build an environment. And I think building an

**[17:08]** environment. And I think building an

**[17:08]** environment. And I think building an environment is the kind of thing that

**[17:11]** environment is the kind of thing that

**[17:11]** environment is the kind of thing that I imagine a lot more people are going to

**[17:13]** I imagine a lot more people are going to

**[17:13]** I imagine a lot more people are going to want to be doing as we start really

**[17:17]** want to be doing as we start really

**[17:17]** want to be doing as we start really seeing where models are headed. In some

**[17:19]** seeing where models are headed. In some

**[17:19]** seeing where models are headed. In some cases, this will be we're going to use

**[17:20]** cases, this will be we're going to use

**[17:20]** cases, this will be we're going to use fine-tuning services from the labs

**[17:21]** fine-tuning services from the labs

**[17:21]** fine-tuning services from the labs because they're going to offer this

**[17:23]** because they're going to offer this

**[17:23]** because they're going to offer this because people want it. In some cases,

**[17:24]** because people want it. In some cases,

**[17:24]** because people want it. In some cases, this will be we really care about the

**[17:26]** this will be we really care about the

**[17:26]** this will be we really care about the smallest model we can run on prem at the

**[17:28]** smallest model we can run on prem at the

**[17:28]** smallest model we can run on prem at the lowest latency and we're really just

**[17:30]** lowest latency and we're really just

**[17:30]** lowest latency and we're really just going to optimize for our one thing. or

**[17:32]** going to optimize for our one thing. or

**[17:32]** going to optimize for our one thing. or it could just be research for the sake

**[17:34]** it could just be research for the sake

**[17:34]** it could just be research for the sake of research and advancing our kind of

**[17:36]** of research and advancing our kind of

**[17:36]** of research and advancing our kind of collective understanding of how this

**[17:37]** collective understanding of how this

**[17:37]** collective understanding of how this stuff all works. And I think that's

**[17:38]** stuff all works. And I think that's

**[17:38]** stuff all works. And I think that's really our goal is to have a world where

**[17:41]** really our goal is to have a world where

**[17:41]** really our goal is to have a world where there's going to be a lot of AI and

**[17:43]** there's going to be a lot of AI and

**[17:43]** there's going to be a lot of AI and where we can all kind of talk about it

**[17:45]** where we can all kind of talk about it

**[17:45]** where we can all kind of talk about it and understand it and look at it and

**[17:46]** and understand it and look at it and

**[17:46]** and understand it and look at it and poke at it and tweak it and have a

**[17:50]** poke at it and tweak it and have a

**[17:50]** poke at it and tweak it and have a better sense of what we're actually

**[17:51]** better sense of what we're actually

**[17:51]** better sense of what we're actually building because I think there's a lot

**[17:52]** building because I think there's a lot

**[17:52]** building because I think there's a lot of times when it feels like we're just

**[17:53]** of times when it feels like we're just

**[17:53]** of times when it feels like we're just kind of the model is a black box and

**[17:56]** kind of the model is a black box and

**[17:56]** kind of the model is a black box and digging into the research and going

**[17:58]** digging into the research and going

**[17:58]** digging into the research and going under the hood and changing things and


### [18:00 - 19:00]

**[18:00]** under the hood and changing things and

**[18:00]** under the hood and changing things and breaking things tells you a lot about

**[18:02]** breaking things tells you a lot about

**[18:02]** breaking things tells you a lot about how these models work. It tells you a

**[18:03]** how these models work. It tells you a

**[18:03]** how these models work. It tells you a lot about understanding where they came

**[18:05]** lot about understanding where they came

**[18:05]** lot about understanding where they came from, where they could be going, where

**[18:06]** from, where they could be going, where

**[18:06]** from, where they could be going, where they might be headed, and preparing for

**[18:09]** they might be headed, and preparing for

**[18:09]** they might be headed, and preparing for that future. Thanks.

**[18:11]** that future. Thanks.

**[18:11]** that future. Thanks. [applause]

**[18:13]** [applause]

**[18:13]** [applause] [music]


