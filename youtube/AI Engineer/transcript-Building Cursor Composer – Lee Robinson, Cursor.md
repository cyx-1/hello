# Building Cursor Composer – Lee Robinson, Cursor

**Video URL:** https://www.youtube.com/watch?v=fL1iJHtl51Q

---

## Full Transcript

### [00:00 - 01:00]

**[00:22]** It's great to be back in New York and

**[00:22]** It's great to be back in New York and I'm very excited to be here and talk on

**[00:24]** I'm very excited to be here and talk on

**[00:24]** I'm very excited to be here and talk on behalf of all of our engineering and

**[00:25]** behalf of all of our engineering and

**[00:26]** behalf of all of our engineering and research teams at Curser about building

**[00:28]** research teams at Curser about building

**[00:28]** research teams at Curser about building Cursor Composer, our first agent model

**[00:30]** Cursor Composer, our first agent model

**[00:30]** Cursor Composer, our first agent model and my colleague Sasha actually gave a

**[00:32]** and my colleague Sasha actually gave a

**[00:32]** and my colleague Sasha actually gave a version of this talk recently. So I'm

**[00:34]** version of this talk recently. So I'm

**[00:34]** version of this talk recently. So I'm excited to give my own uh my own take on

**[00:36]** excited to give my own uh my own take on

**[00:36]** excited to give my own uh my own take on it. So cursor composer is a model

**[00:39]** it. So cursor composer is a model

**[00:39]** it. So cursor composer is a model designed for real world real world

**[00:41]** designed for real world real world

**[00:41]** designed for real world real world software engineering and it tries to be

**[00:43]** software engineering and it tries to be

**[00:43]** software engineering and it tries to be both fast and smart. So as we've

**[00:46]** both fast and smart. So as we've

**[00:46]** both fast and smart. So as we've measured it against our own benchmarks.

**[00:48]** measured it against our own benchmarks.

**[00:48]** measured it against our own benchmarks. It's better than the best open source

**[00:49]** It's better than the best open source

**[00:49]** It's better than the best open source models. It's like up against recent

**[00:51]** models. It's like up against recent

**[00:51]** models. It's like up against recent Frontier models but kind of slightly

**[00:53]** Frontier models but kind of slightly

**[00:53]** Frontier models but kind of slightly below the latest frontier with Sonnet 45

**[00:56]** below the latest frontier with Sonnet 45

**[00:56]** below the latest frontier with Sonnet 45 GPT 5.1 codecs. But where it really

**[00:58]** GPT 5.1 codecs. But where it really

**[00:58]** GPT 5.1 codecs. But where it really shines is it's about four times more


### [01:00 - 02:00]

**[01:01]** shines is it's about four times more

**[01:01]** shines is it's about four times more efficient at token generation than

**[01:03]** efficient at token generation than

**[01:03]** efficient at token generation than models at a similar level of

**[01:04]** models at a similar level of

**[01:04]** models at a similar level of intelligence. So we're trying to mesh

**[01:06]** intelligence. So we're trying to mesh

**[01:06]** intelligence. So we're trying to mesh speed as well as intelligence. So why

**[01:10]** speed as well as intelligence. So why

**[01:10]** speed as well as intelligence. So why did we build this model? I mean

**[01:12]** did we build this model? I mean

**[01:12]** did we build this model? I mean obviously cursor has an IDE. Why are we

**[01:14]** obviously cursor has an IDE. Why are we

**[01:14]** obviously cursor has an IDE. Why are we getting into the model space? Why do we

**[01:15]** getting into the model space? Why do we

**[01:15]** getting into the model space? Why do we care about this? Well, our research and

**[01:17]** care about this? Well, our research and

**[01:17]** care about this? Well, our research and product teams have been building a model

**[01:19]** product teams have been building a model

**[01:19]** product teams have been building a model called tab which you can use for

**[01:20]** called tab which you can use for

**[01:20]** called tab which you can use for autocomplete. Maybe some of you use that

**[01:22]** autocomplete. Maybe some of you use that

**[01:22]** autocomplete. Maybe some of you use that inside of cursor. and we wanted to take

**[01:24]** inside of cursor. and we wanted to take

**[01:24]** inside of cursor. and we wanted to take that same approach for a very low

**[01:26]** that same approach for a very low

**[01:26]** that same approach for a very low latency model and apply it to coding

**[01:28]** latency model and apply it to coding

**[01:28]** latency model and apply it to coding with agents. But honestly, we weren't

**[01:31]** with agents. But honestly, we weren't

**[01:31]** with agents. But honestly, we weren't really sure if it would work. So, we

**[01:33]** really sure if it would work. So, we

**[01:33]** really sure if it would work. So, we started prototyping some early versions

**[01:34]** started prototyping some early versions

**[01:34]** started prototyping some early versions of what this model could look like,

**[01:36]** of what this model could look like,

**[01:36]** of what this model could look like, started to put it out and get some

**[01:37]** started to put it out and get some

**[01:37]** started to put it out and get some feedback from users. And we were pretty

**[01:40]** feedback from users. And we were pretty

**[01:40]** feedback from users. And we were pretty surprised that this cheetah slug we

**[01:41]** surprised that this cheetah slug we

**[01:41]** surprised that this cheetah slug we released for this model, people actually

**[01:43]** released for this model, people actually

**[01:43]** released for this model, people actually really liked it. Uh they really like the

**[01:45]** really liked it. Uh they really like the

**[01:45]** really liked it. Uh they really like the speed, but the feedback we got was it's

**[01:48]** speed, but the feedback we got was it's

**[01:48]** speed, but the feedback we got was it's not really smart enough yet to be a

**[01:49]** not really smart enough yet to be a

**[01:50]** not really smart enough yet to be a daily driver for a lot of their coding.

**[01:52]** daily driver for a lot of their coding.

**[01:52]** daily driver for a lot of their coding. So we needed it to be smart and fast.

**[01:55]** So we needed it to be smart and fast.

**[01:55]** So we needed it to be smart and fast. Definitely needed to be smart. So we

**[01:56]** Definitely needed to be smart. So we

**[01:56]** Definitely needed to be smart. So we really worked on making this internal

**[01:58]** really worked on making this internal

**[01:58]** really worked on making this internal benchmark that represented our usage on


### [02:00 - 03:00]

**[02:00]** benchmark that represented our usage on

**[02:00]** benchmark that represented our usage on our own repos and how we actually built

**[02:02]** our own repos and how we actually built

**[02:02]** our own repos and how we actually built software. Like if we had a model that

**[02:05]** software. Like if we had a model that

**[02:05]** software. Like if we had a model that was both fast and smart and a checkpoint

**[02:07]** was both fast and smart and a checkpoint

**[02:07]** was both fast and smart and a checkpoint that our developers would use every

**[02:08]** that our developers would use every

**[02:08]** that our developers would use every single day to build the product and to

**[02:10]** single day to build the product and to

**[02:10]** single day to build the product and to build all of our software, then we knew

**[02:12]** build all of our software, then we knew

**[02:12]** build all of our software, then we knew that we would be on to something. And

**[02:14]** that we would be on to something. And

**[02:14]** that we would be on to something. And for example, one big change here that

**[02:16]** for example, one big change here that

**[02:16]** for example, one big change here that helped actually push this towards a

**[02:17]** helped actually push this towards a

**[02:17]** helped actually push this towards a level where we had a checkpoint where

**[02:19]** level where we had a checkpoint where

**[02:19]** level where we had a checkpoint where people would use it was being able to

**[02:20]** people would use it was being able to

**[02:20]** people would use it was being able to call tools in parallel and being able to

**[02:22]** call tools in parallel and being able to

**[02:22]** call tools in parallel and being able to very effectively use our semantic search

**[02:24]** very effectively use our semantic search

**[02:24]** very effectively use our semantic search tool. And we'll talk about that a little

**[02:26]** tool. And we'll talk about that a little

**[02:26]** tool. And we'll talk about that a little bit more here later. So if you haven't

**[02:29]** bit more here later. So if you haven't

**[02:29]** bit more here later. So if you haven't seen it, uh here's cursor in cursor 2.0

**[02:31]** seen it, uh here's cursor in cursor 2.0

**[02:31]** seen it, uh here's cursor in cursor 2.0 in our new view and we're going to use

**[02:33]** in our new view and we're going to use

**[02:34]** in our new view and we're going to use the composer one model and you'll notice

**[02:36]** the composer one model and you'll notice

**[02:36]** the composer one model and you'll notice that it is doing a lot of things very

**[02:38]** that it is doing a lot of things very

**[02:38]** that it is doing a lot of things very quickly. It's calling a bunch of tools

**[02:40]** quickly. It's calling a bunch of tools

**[02:40]** quickly. It's calling a bunch of tools in parallel like gp so reading a lot of

**[02:42]** in parallel like gp so reading a lot of

**[02:42]** in parallel like gp so reading a lot of files. It's making shell commands. Uh

**[02:44]** files. It's making shell commands. Uh

**[02:44]** files. It's making shell commands. Uh it's making file edits. It's writing and

**[02:47]** it's making file edits. It's writing and

**[02:47]** it's making file edits. It's writing and managing uh a list of to-dos. And you

**[02:50]** managing uh a list of to-dos. And you

**[02:50]** managing uh a list of to-dos. And you can kind of very quickly work through

**[02:52]** can kind of very quickly work through

**[02:52]** can kind of very quickly work through tasks in the foreground here. Uh in this

**[02:54]** tasks in the foreground here. Uh in this

**[02:54]** tasks in the foreground here. Uh in this case, I'm investigating an issue in an

**[02:56]** case, I'm investigating an issue in an

**[02:56]** case, I'm investigating an issue in an open source repo. And I don't know about

**[02:58]** open source repo. And I don't know about

**[02:58]** open source repo. And I don't know about y'all, but this has been a quite


### [03:00 - 04:00]

**[03:00]** y'all, but this has been a quite

**[03:00]** y'all, but this has been a quite different programming experience for me.

**[03:02]** different programming experience for me.

**[03:02]** different programming experience for me. Uh having working with coding agents for

**[03:04]** Uh having working with coding agents for

**[03:04]** Uh having working with coding agents for a little bit of time now versus kind of

**[03:06]** a little bit of time now versus kind of

**[03:06]** a little bit of time now versus kind of firing off an agent and waiting, let's

**[03:08]** firing off an agent and waiting, let's

**[03:08]** firing off an agent and waiting, let's call it 20 minutes for it to complete

**[03:09]** call it 20 minutes for it to complete

**[03:09]** call it 20 minutes for it to complete where you can kind of context switch

**[03:11]** where you can kind of context switch

**[03:11]** where you can kind of context switch away. This really does help keep you in

**[03:12]** away. This really does help keep you in

**[03:12]** away. This really does help keep you in the flow and is a kind of a different

**[03:14]** the flow and is a kind of a different

**[03:14]** the flow and is a kind of a different style of programming I think. So I want

**[03:16]** style of programming I think. So I want

**[03:16]** style of programming I think. So I want to talk about how we did this in a way

**[03:18]** to talk about how we did this in a way

**[03:18]** to talk about how we did this in a way that's hopefully accessible for you all.

**[03:20]** that's hopefully accessible for you all.

**[03:20]** that's hopefully accessible for you all. I'm not a machine learning researcher

**[03:21]** I'm not a machine learning researcher

**[03:21]** I'm not a machine learning researcher but I do really enjoy this stuff. Uh

**[03:24]** but I do really enjoy this stuff. Uh

**[03:24]** but I do really enjoy this stuff. Uh what we learned some of the

**[03:25]** what we learned some of the

**[03:25]** what we learned some of the infrastructure challenges and then a

**[03:26]** infrastructure challenges and then a

**[03:26]** infrastructure challenges and then a little bit on where we're going uh

**[03:28]** little bit on where we're going uh

**[03:28]** little bit on where we're going uh moving forward. So in cursor a user kind

**[03:31]** moving forward. So in cursor a user kind

**[03:31]** moving forward. So in cursor a user kind of submits a query to our backend. The

**[03:33]** of submits a query to our backend. The

**[03:33]** of submits a query to our backend. The agent reads that query and then decides

**[03:35]** agent reads that query and then decides

**[03:35]** agent reads that query and then decides to make a series of tool calls. And our

**[03:37]** to make a series of tool calls. And our

**[03:37]** to make a series of tool calls. And our agent has about 10 tools give or take,

**[03:40]** agent has about 10 tools give or take,

**[03:40]** agent has about 10 tools give or take, but we're going to focus on five here.

**[03:41]** but we're going to focus on five here.

**[03:41]** but we're going to focus on five here. So reading files, editing files,

**[03:43]** So reading files, editing files,

**[03:43]** So reading files, editing files, searching your codebase, looking at

**[03:45]** searching your codebase, looking at

**[03:45]** searching your codebase, looking at lints, and then also running terminal or

**[03:47]** lints, and then also running terminal or

**[03:47]** lints, and then also running terminal or shell commands. And the agent then is

**[03:49]** shell commands. And the agent then is

**[03:49]** shell commands. And the agent then is able to autonomously decide, do we call

**[03:51]** able to autonomously decide, do we call

**[03:51]** able to autonomously decide, do we call these serially or do we run these in

**[03:53]** these serially or do we run these in

**[03:53]** these serially or do we run these in parallel? And our goal with

**[03:56]** parallel? And our goal with

**[03:56]** parallel? And our goal with reinforcement learning here is to try to

**[03:57]** reinforcement learning here is to try to

**[03:57]** reinforcement learning here is to try to mirror the cursor production environment


### [04:00 - 05:00]

**[04:00]** mirror the cursor production environment

**[04:00]** mirror the cursor production environment as close as we possibly can. So this

**[04:02]** as close as we possibly can. So this

**[04:02]** as close as we possibly can. So this data that we have in training, we want

**[04:03]** data that we have in training, we want

**[04:03]** data that we have in training, we want to kind of pretend like we're actually

**[04:05]** to kind of pretend like we're actually

**[04:05]** to kind of pretend like we're actually calling real cursor queries. Uh so to do

**[04:08]** calling real cursor queries. Uh so to do

**[04:08]** calling real cursor queries. Uh so to do that, we are running a series of

**[04:09]** that, we are running a series of

**[04:09]** that, we are running a series of rollouts. Um for example, in this roll

**[04:11]** rollouts. Um for example, in this roll

**[04:11]** rollouts. Um for example, in this roll out, we're calling a series of tools

**[04:13]** out, we're calling a series of tools

**[04:13]** out, we're calling a series of tools like reading files and editing files.

**[04:16]** like reading files and editing files.

**[04:16]** like reading files and editing files. And when we run more rollouts, we can

**[04:18]** And when we run more rollouts, we can

**[04:18]** And when we run more rollouts, we can start from that same initial starting

**[04:20]** start from that same initial starting

**[04:20]** start from that same initial starting point, but we might call a completely

**[04:21]** point, but we might call a completely

**[04:21]** point, but we might call a completely different set of tools. So in this one,

**[04:23]** different set of tools. So in this one,

**[04:23]** different set of tools. So in this one, we're also doing codebase search. So we

**[04:26]** we're also doing codebase search. So we

**[04:26]** we're also doing codebase search. So we score the output, we decide which one is

**[04:28]** score the output, we decide which one is

**[04:28]** score the output, we decide which one is better and then we update the parameters

**[04:31]** better and then we update the parameters

**[04:31]** better and then we update the parameters of our model based on that change. So

**[04:33]** of our model based on that change. So

**[04:33]** of our model based on that change. So conceptually a pretty simple idea. The

**[04:36]** conceptually a pretty simple idea. The

**[04:36]** conceptually a pretty simple idea. The challenges come from when you take the

**[04:37]** challenges come from when you take the

**[04:37]** challenges come from when you take the simple idea and then you try to scale it

**[04:39]** simple idea and then you try to scale it

**[04:39]** simple idea and then you try to scale it up to a very large amount. So there's

**[04:40]** up to a very large amount. So there's

**[04:40]** up to a very large amount. So there's kind of three challenges. The first one

**[04:42]** kind of three challenges. The first one

**[04:42]** kind of three challenges. The first one is trying to match the training and

**[04:44]** is trying to match the training and

**[04:44]** is trying to match the training and inference environment. So when the model

**[04:46]** inference environment. So when the model

**[04:46]** inference environment. So when the model is actually being used in the product.

**[04:48]** is actually being used in the product.

**[04:48]** is actually being used in the product. Um, in this case with composer, we're

**[04:50]** Um, in this case with composer, we're

**[04:50]** Um, in this case with composer, we're training a large mixture of experts

**[04:51]** training a large mixture of experts

**[04:51]** training a large mixture of experts model and it's being parallelized across

**[04:54]** model and it's being parallelized across

**[04:54]** model and it's being parallelized across thousands of GPUs and if we don't speed

**[04:56]** thousands of GPUs and if we don't speed

**[04:56]** thousands of GPUs and if we don't speed that up, it's going to take forever to

**[04:58]** that up, it's going to take forever to

**[04:58]** that up, it's going to take forever to train the thing. So, we want to make it

**[04:59]** train the thing. So, we want to make it

**[04:59]** train the thing. So, we want to make it really fast and match the training and


### [05:00 - 06:00]

**[05:02]** really fast and match the training and

**[05:02]** really fast and match the training and kind of sampling version to be as close

**[05:04]** kind of sampling version to be as close

**[05:04]** kind of sampling version to be as close as possible. The second challenge is

**[05:06]** as possible. The second challenge is

**[05:06]** as possible. The second challenge is that the rollouts can get pretty complex

**[05:08]** that the rollouts can get pretty complex

**[05:08]** that the rollouts can get pretty complex when you start to look at real world

**[05:09]** when you start to look at real world

**[05:09]** when you start to look at real world data here. So, models are going to use

**[05:11]** data here. So, models are going to use

**[05:11]** data here. So, models are going to use hundreds of thousands to millions of

**[05:13]** hundreds of thousands to millions of

**[05:13]** hundreds of thousands to millions of tokens. They're going to make hundreds

**[05:15]** tokens. They're going to make hundreds

**[05:15]** tokens. They're going to make hundreds of different tool calls. And each of

**[05:16]** of different tool calls. And each of

**[05:16]** of different tool calls. And each of these rollouts could take a, you know, a

**[05:18]** these rollouts could take a, you know, a

**[05:18]** these rollouts could take a, you know, a pretty different amount of time. One

**[05:20]** pretty different amount of time. One

**[05:20]** pretty different amount of time. One might make a lot of tool calls, one

**[05:22]** might make a lot of tool calls, one

**[05:22]** might make a lot of tool calls, one might make not as many, and they'll

**[05:23]** might make not as many, and they'll

**[05:23]** might make not as many, and they'll complete a different time. So, we have

**[05:24]** complete a different time. So, we have

**[05:24]** complete a different time. So, we have to figure out how to deal with that

**[05:26]** to figure out how to deal with that

**[05:26]** to figure out how to deal with that challenge. And finally, there's this

**[05:28]** challenge. And finally, there's this

**[05:28]** challenge. And finally, there's this challenge of consistency. If we want to

**[05:30]** challenge of consistency. If we want to

**[05:30]** challenge of consistency. If we want to mimic the production cursor environment

**[05:32]** mimic the production cursor environment

**[05:32]** mimic the production cursor environment as close as possible, we need to use

**[05:34]** as close as possible, we need to use

**[05:34]** as close as possible, we need to use exactly the same tool format and the

**[05:36]** exactly the same tool format and the

**[05:36]** exactly the same tool format and the tool response. But in training, we have

**[05:39]** tool response. But in training, we have

**[05:39]** tool response. But in training, we have this really bursty amount of compute.

**[05:41]** this really bursty amount of compute.

**[05:41]** this really bursty amount of compute. Basically, we're like doing all of this

**[05:42]** Basically, we're like doing all of this

**[05:42]** Basically, we're like doing all of this training all at once, which is different

**[05:44]** training all at once, which is different

**[05:44]** training all at once, which is different than at production. So, it is really an

**[05:47]** than at production. So, it is really an

**[05:47]** than at production. So, it is really an infrastructure challenge. We have these

**[05:49]** infrastructure challenge. We have these

**[05:50]** infrastructure challenge. We have these three machine learning challenges and

**[05:52]** three machine learning challenges and

**[05:52]** three machine learning challenges and all of the solutions coincidentally are

**[05:54]** all of the solutions coincidentally are

**[05:54]** all of the solutions coincidentally are actually infrastructure problems. So,

**[05:56]** actually infrastructure problems. So,

**[05:56]** actually infrastructure problems. So, let's talk through a few of these

**[05:57]** let's talk through a few of these

**[05:57]** let's talk through a few of these problems and how we solved it at the

**[05:59]** problems and how we solved it at the

**[05:59]** problems and how we solved it at the infrastructure layer. So, our


### [06:00 - 07:00]

**[06:01]** infrastructure layer. So, our

**[06:01]** infrastructure layer. So, our architecture is probably familiar for

**[06:03]** architecture is probably familiar for

**[06:03]** architecture is probably familiar for some of you who have been involved in

**[06:05]** some of you who have been involved in

**[06:05]** some of you who have been involved in this space a little bit, but I still

**[06:06]** this space a little bit, but I still

**[06:06]** this space a little bit, but I still think it's really interesting to talk

**[06:07]** think it's really interesting to talk

**[06:07]** think it's really interesting to talk about at kind of a high level. Uh, we

**[06:09]** about at kind of a high level. Uh, we

**[06:09]** about at kind of a high level. Uh, we have three different servers. We have an

**[06:11]** have three different servers. We have an

**[06:11]** have three different servers. We have an inference server. We have kind of the

**[06:12]** inference server. We have kind of the

**[06:12]** inference server. We have kind of the standard ML stack with PyTorch. We have

**[06:15]** standard ML stack with PyTorch. We have

**[06:15]** standard ML stack with PyTorch. We have an inference server. So the rollouts

**[06:17]** an inference server. So the rollouts

**[06:17]** an inference server. So the rollouts that I just talked about, that's where

**[06:18]** that I just talked about, that's where

**[06:18]** that I just talked about, that's where we use Ray. And then we have environment

**[06:21]** we use Ray. And then we have environment

**[06:21]** we use Ray. And then we have environment servers. And these are the ones where

**[06:22]** servers. And these are the ones where

**[06:22]** servers. And these are the ones where we're kind of simulating that cursor

**[06:23]** we're kind of simulating that cursor

**[06:23]** we're kind of simulating that cursor environment that I talked about. And all

**[06:25]** environment that I talked about. And all

**[06:26]** environment that I talked about. And all these servers talk to each other. So for

**[06:28]** these servers talk to each other. So for

**[06:28]** these servers talk to each other. So for example, the inference server can

**[06:29]** example, the inference server can

**[06:30]** example, the inference server can basically send these advantages back to

**[06:32]** basically send these advantages back to

**[06:32]** basically send these advantages back to the trainer, which is like nudging it up

**[06:34]** the trainer, which is like nudging it up

**[06:34]** the trainer, which is like nudging it up or down uh based on the roll out and

**[06:36]** or down uh based on the roll out and

**[06:36]** or down uh based on the roll out and then updating the model and getting new

**[06:39]** then updating the model and getting new

**[06:39]** then updating the model and getting new parameters.

**[06:40]** parameters.

**[06:40]** parameters. So this this one is a bit more on the ML

**[06:42]** So this this one is a bit more on the ML

**[06:42]** So this this one is a bit more on the ML side, but we're we're trying to train a

**[06:43]** side, but we're we're trying to train a

**[06:44]** side, but we're we're trying to train a model that's very very large and to do

**[06:46]** model that's very very large and to do

**[06:46]** model that's very very large and to do it as fast as possible. And one way that

**[06:48]** it as fast as possible. And one way that

**[06:48]** it as fast as possible. And one way that our team was able to do this on the

**[06:49]** our team was able to do this on the

**[06:50]** our team was able to do this on the research side was to develop a library

**[06:52]** research side was to develop a library

**[06:52]** research side was to develop a library of custom kernels that allowed for very

**[06:54]** of custom kernels that allowed for very

**[06:54]** of custom kernels that allowed for very low precision training. And basically

**[06:56]** low precision training. And basically

**[06:56]** low precision training. And basically this allows us to just speed up the

**[06:58]** this allows us to just speed up the

**[06:58]** this allows us to just speed up the training process in a big way and also

**[06:59]** training process in a big way and also

**[06:59]** training process in a big way and also make it much easier to ship to our


### [07:00 - 08:00]

**[07:02]** make it much easier to ship to our

**[07:02]** make it much easier to ship to our inference server. So, if you're the type

**[07:03]** inference server. So, if you're the type

**[07:03]** inference server. So, if you're the type of person who loves this, we wrote a

**[07:05]** of person who loves this, we wrote a

**[07:05]** of person who loves this, we wrote a blog post going way in depth on all of

**[07:07]** blog post going way in depth on all of

**[07:07]** blog post going way in depth on all of this that talks about our custom

**[07:08]** this that talks about our custom

**[07:08]** this that talks about our custom kernels. Uh, if you're interested, the

**[07:10]** kernels. Uh, if you're interested, the

**[07:10]** kernels. Uh, if you're interested, the TLDDR here is we found for the mixture

**[07:12]** TLDDR here is we found for the mixture

**[07:12]** TLDDR here is we found for the mixture of experts layer was about three and a

**[07:14]** of experts layer was about three and a

**[07:14]** of experts layer was about three and a half times faster uh a speed up on

**[07:17]** half times faster uh a speed up on

**[07:17]** half times faster uh a speed up on Nvidia Blackwell chips. So, it made a

**[07:19]** Nvidia Blackwell chips. So, it made a

**[07:19]** Nvidia Blackwell chips. So, it made a pretty significant uh impact on our

**[07:21]** pretty significant uh impact on our

**[07:21]** pretty significant uh impact on our training runs. So, once we update the

**[07:24]** training runs. So, once we update the

**[07:24]** training runs. So, once we update the weights, we need to send them back over

**[07:26]** weights, we need to send them back over

**[07:26]** weights, we need to send them back over to the inference server uh during this

**[07:28]** to the inference server uh during this

**[07:28]** to the inference server uh during this training process. and the inference

**[07:29]** training process. and the inference

**[07:29]** training process. and the inference server is the one that's doing all the

**[07:31]** server is the one that's doing all the

**[07:31]** server is the one that's doing all the rollouts that I talked about calling the

**[07:32]** rollouts that I talked about calling the

**[07:32]** rollouts that I talked about calling the tools and kind of managing um what we

**[07:34]** tools and kind of managing um what we

**[07:34]** tools and kind of managing um what we sent. The challenge here uh is that they

**[07:37]** sent. The challenge here uh is that they

**[07:37]** sent. The challenge here uh is that they all complete at different times. So kind

**[07:39]** all complete at different times. So kind

**[07:39]** all complete at different times. So kind of a naive version of this there will be

**[07:41]** of a naive version of this there will be

**[07:41]** of a naive version of this there will be a lot of wasted time. So what we were

**[07:44]** a lot of wasted time. So what we were

**[07:44]** a lot of wasted time. So what we were able to do is do load balancing across

**[07:46]** able to do is do load balancing across

**[07:46]** able to do is do load balancing across the different threads and processes to

**[07:48]** the different threads and processes to

**[07:48]** the different threads and processes to basically shift the work around and and

**[07:50]** basically shift the work around and and

**[07:50]** basically shift the work around and and not have a bunch of idle time. So if one

**[07:52]** not have a bunch of idle time. So if one

**[07:52]** not have a bunch of idle time. So if one roll out for example makes a ton of tool

**[07:54]** roll out for example makes a ton of tool

**[07:54]** roll out for example makes a ton of tool calls, maybe it installs some packages,

**[07:56]** calls, maybe it installs some packages,

**[07:56]** calls, maybe it installs some packages, installs some library, we're not just

**[07:58]** installs some library, we're not just

**[07:58]** installs some library, we're not just sitting there waiting for all of the

**[07:59]** sitting there waiting for all of the

**[07:59]** sitting there waiting for all of the other ones to finish. The inference


### [08:00 - 09:00]

**[08:02]** other ones to finish. The inference

**[08:02]** other ones to finish. The inference server is spending all this time going

**[08:03]** server is spending all this time going

**[08:03]** server is spending all this time going back and forth making the tool calls to

**[08:05]** back and forth making the tool calls to

**[08:05]** back and forth making the tool calls to the environment uh and getting the tool

**[08:07]** the environment uh and getting the tool

**[08:07]** the environment uh and getting the tool results back. So again, communicating

**[08:09]** results back. So again, communicating

**[08:09]** results back. So again, communicating between these servers and we want that

**[08:11]** between these servers and we want that

**[08:11]** between these servers and we want that environment to be as close as possible

**[08:13]** environment to be as close as possible

**[08:13]** environment to be as close as possible to the cursor product. One thing that's

**[08:15]** to the cursor product. One thing that's

**[08:15]** to the cursor product. One thing that's nice about having both the coding agent,

**[08:18]** nice about having both the coding agent,

**[08:18]** nice about having both the coding agent, the IDE, as well as what we're doing

**[08:20]** the IDE, as well as what we're doing

**[08:20]** the IDE, as well as what we're doing with the model research and training our

**[08:21]** with the model research and training our

**[08:21]** with the model research and training our own models is we can kind of co-design

**[08:23]** own models is we can kind of co-design

**[08:23]** own models is we can kind of co-design these things together. So, as we were

**[08:25]** these things together. So, as we were

**[08:25]** these things together. So, as we were building out a lot of our RL work for

**[08:27]** building out a lot of our RL work for

**[08:27]** building out a lot of our RL work for this model, we were also building our

**[08:29]** this model, we were also building our

**[08:29]** this model, we were also building our cloud agents product. Um, this is how

**[08:31]** cloud agents product. Um, this is how

**[08:31]** cloud agents product. Um, this is how you can run a cursor agent kind of

**[08:33]** you can run a cursor agent kind of

**[08:33]** you can run a cursor agent kind of offline. You can run it from your phone

**[08:35]** offline. You can run it from your phone

**[08:35]** offline. You can run it from your phone or on the web or kick it off from Slack,

**[08:37]** or on the web or kick it off from Slack,

**[08:37]** or on the web or kick it off from Slack, for example. And to do this, we spin up

**[08:39]** for example. And to do this, we spin up

**[08:39]** for example. And to do this, we spin up virtual machines in the cloud. So each

**[08:41]** virtual machines in the cloud. So each

**[08:41]** virtual machines in the cloud. So each one of these VMs loads up the user's

**[08:43]** one of these VMs loads up the user's

**[08:43]** one of these VMs loads up the user's code. It allows the agent to kind of

**[08:45]** code. It allows the agent to kind of

**[08:45]** code. It allows the agent to kind of like make file changes, run tools, and

**[08:48]** like make file changes, run tools, and

**[08:48]** like make file changes, run tools, and edit code in a secure sandbox. And

**[08:50]** edit code in a secure sandbox. And

**[08:50]** edit code in a secure sandbox. And coincidentally, this is the perfect

**[08:52]** coincidentally, this is the perfect

**[08:52]** coincidentally, this is the perfect Impra for RL and our use in training. So

**[08:55]** Impra for RL and our use in training. So

**[08:55]** Impra for RL and our use in training. So we have this like fleet of cloud VMs and

**[08:58]** we have this like fleet of cloud VMs and

**[08:58]** we have this like fleet of cloud VMs and we have an environment that very closely


### [09:00 - 10:00]

**[09:01]** we have an environment that very closely

**[09:01]** we have an environment that very closely matches the production cursor

**[09:02]** matches the production cursor

**[09:02]** matches the production cursor environment and we can then use that for

**[09:04]** environment and we can then use that for

**[09:04]** environment and we can then use that for training. This does still have some

**[09:06]** training. This does still have some

**[09:06]** training. This does still have some challenges though. I kind of talked

**[09:07]** challenges though. I kind of talked

**[09:07]** challenges though. I kind of talked about how the training workload is very

**[09:09]** about how the training workload is very

**[09:09]** about how the training workload is very spiky and it's different than the kind

**[09:11]** spiky and it's different than the kind

**[09:11]** spiky and it's different than the kind of standard inference when you're

**[09:13]** of standard inference when you're

**[09:13]** of standard inference when you're running the cloud agents product. So we

**[09:15]** running the cloud agents product. So we

**[09:15]** running the cloud agents product. So we needed to build infrastructure to

**[09:16]** needed to build infrastructure to

**[09:16]** needed to build infrastructure to support all of these VMs and

**[09:19]** support all of these VMs and

**[09:19]** support all of these VMs and orchestrating between them. So you know

**[09:21]** orchestrating between them. So you know

**[09:21]** orchestrating between them. So you know we have many different clusters,

**[09:23]** we have many different clusters,

**[09:23]** we have many different clusters, hundreds of thousands of VMs here and

**[09:25]** hundreds of thousands of VMs here and

**[09:25]** hundreds of thousands of VMs here and you can see behind me one of the

**[09:26]** you can see behind me one of the

**[09:26]** you can see behind me one of the internal dashboards we built uh with

**[09:28]** internal dashboards we built uh with

**[09:28]** internal dashboards we built uh with composer actually to visualize uh all of

**[09:30]** composer actually to visualize uh all of

**[09:30]** composer actually to visualize uh all of the different VMs in the fleet.

**[09:33]** the different VMs in the fleet.

**[09:33]** the different VMs in the fleet. So why spend all this time trying to

**[09:36]** So why spend all this time trying to

**[09:36]** So why spend all this time trying to match the environment to be as close as

**[09:38]** match the environment to be as close as

**[09:38]** match the environment to be as close as possible to cursor production. I've kind

**[09:40]** possible to cursor production. I've kind

**[09:40]** possible to cursor production. I've kind of mentioned that a few times. We could

**[09:42]** of mentioned that a few times. We could

**[09:42]** of mentioned that a few times. We could mock it, we could simulate it out. Um,

**[09:44]** mock it, we could simulate it out. Um,

**[09:44]** mock it, we could simulate it out. Um, but one of the really nice benefits is

**[09:46]** but one of the really nice benefits is

**[09:46]** but one of the really nice benefits is we get to give the model uh specific

**[09:48]** we get to give the model uh specific

**[09:48]** we get to give the model uh specific tools that we think are very valuable

**[09:50]** tools that we think are very valuable

**[09:50]** tools that we think are very valuable inside of the agent. So, one of those is

**[09:53]** inside of the agent. So, one of those is

**[09:53]** inside of the agent. So, one of those is that we've trained our own embedding

**[09:54]** that we've trained our own embedding

**[09:54]** that we've trained our own embedding model that allows you to do semantic

**[09:56]** model that allows you to do semantic

**[09:56]** model that allows you to do semantic search. So when you use cursor, we go

**[09:58]** search. So when you use cursor, we go

**[09:58]** search. So when you use cursor, we go and index your codebase and then it


### [10:00 - 11:00]

**[10:00]** and index your codebase and then it

**[10:00]** and index your codebase and then it allows the agent to make natural langu

**[10:03]** allows the agent to make natural langu

**[10:03]** allows the agent to make natural langu natural language queries to find files

**[10:05]** natural language queries to find files

**[10:05]** natural language queries to find files that it might want to edit. And we did

**[10:08]** that it might want to edit. And we did

**[10:08]** that it might want to edit. And we did some research on this recently. We found

**[10:10]** some research on this recently. We found

**[10:10]** some research on this recently. We found that semantic search not only helped

**[10:12]** that semantic search not only helped

**[10:12]** that semantic search not only helped basically every single model inside of

**[10:13]** basically every single model inside of

**[10:13]** basically every single model inside of the cursor agent harness, but it was

**[10:15]** the cursor agent harness, but it was

**[10:15]** the cursor agent harness, but it was particularly helpful with composer,

**[10:17]** particularly helpful with composer,

**[10:18]** particularly helpful with composer, which kind of makes sense when you think

**[10:19]** which kind of makes sense when you think

**[10:19]** which kind of makes sense when you think about it. Like we trained composer in

**[10:21]** about it. Like we trained composer in

**[10:21]** about it. Like we trained composer in the exact same environment that we're

**[10:23]** the exact same environment that we're

**[10:23]** the exact same environment that we're using at inference time. And so the

**[10:25]** using at inference time. And so the

**[10:25]** using at inference time. And so the model kind of becomes a power user of

**[10:27]** model kind of becomes a power user of

**[10:27]** model kind of becomes a power user of this tool which is really effective.

**[10:30]** this tool which is really effective.

**[10:30]** this tool which is really effective. So let's talk about uh how the release

**[10:32]** So let's talk about uh how the release

**[10:32]** So let's talk about uh how the release has been going and kind of where we're

**[10:34]** has been going and kind of where we're

**[10:34]** has been going and kind of where we're going next. Um as we were doing the

**[10:37]** going next. Um as we were doing the

**[10:37]** going next. Um as we were doing the training process we kind of knew that RL

**[10:40]** training process we kind of knew that RL

**[10:40]** training process we kind of knew that RL was working when we were able to

**[10:42]** was working when we were able to

**[10:42]** was working when we were able to continuously improve the model and start

**[10:44]** continuously improve the model and start

**[10:44]** continuously improve the model and start to see more and more improvements after

**[10:46]** to see more and more improvements after

**[10:46]** to see more and more improvements after more and more rollouts. So we started

**[10:48]** more and more rollouts. So we started

**[10:48]** more and more rollouts. So we started about kind of the same performance as

**[10:50]** about kind of the same performance as

**[10:50]** about kind of the same performance as the best open model and then as we

**[10:52]** the best open model and then as we

**[10:52]** the best open model and then as we trained and kind of threw more compute

**[10:54]** trained and kind of threw more compute

**[10:54]** trained and kind of threw more compute at it the performance continued to

**[10:56]** at it the performance continued to

**[10:56]** at it the performance continued to increase and to a point today where

**[10:57]** increase and to a point today where

**[10:57]** increase and to a point today where we're close to the frontier in terms of

**[10:59]** we're close to the frontier in terms of

**[10:59]** we're close to the frontier in terms of kind of the best coding agents that are


### [11:00 - 12:00]

**[11:01]** kind of the best coding agents that are

**[11:01]** kind of the best coding agents that are available and personally I think this is

**[11:03]** available and personally I think this is

**[11:03]** available and personally I think this is a great sign just for being able to take

**[11:05]** a great sign just for being able to take

**[11:05]** a great sign just for being able to take and scale RL and apply it to these very

**[11:08]** and scale RL and apply it to these very

**[11:08]** and scale RL and apply it to these very hard specialized tasks like in our

**[11:09]** hard specialized tasks like in our

**[11:10]** hard specialized tasks like in our example coding but it could be applied

**[11:11]** example coding but it could be applied

**[11:12]** example coding but it could be applied to other domains as well. uh RL also

**[11:15]** to other domains as well. uh RL also

**[11:15]** to other domains as well. uh RL also allowed us to kind of change properties

**[11:18]** allowed us to kind of change properties

**[11:18]** allowed us to kind of change properties of the model in a way that was very

**[11:20]** of the model in a way that was very

**[11:20]** of the model in a way that was very useful for the cursor product. We wanted

**[11:22]** useful for the cursor product. We wanted

**[11:22]** useful for the cursor product. We wanted the model to be both kind of fast at

**[11:24]** the model to be both kind of fast at

**[11:24]** the model to be both kind of fast at generating tokens but also the end toend

**[11:26]** generating tokens but also the end toend

**[11:26]** generating tokens but also the end toend experience of getting a result that's

**[11:28]** experience of getting a result that's

**[11:28]** experience of getting a result that's helpful. So for example, instead of

**[11:30]** helpful. So for example, instead of

**[11:30]** helpful. So for example, instead of reading a file one by one, you can read

**[11:32]** reading a file one by one, you can read

**[11:32]** reading a file one by one, you can read 10 files in parallel with tool calling.

**[11:35]** 10 files in parallel with tool calling.

**[11:35]** 10 files in parallel with tool calling. And as you saw in the demo earlier, it

**[11:37]** And as you saw in the demo earlier, it

**[11:37]** And as you saw in the demo earlier, it makes composer feel much faster when you

**[11:39]** makes composer feel much faster when you

**[11:39]** makes composer feel much faster when you have that. And we think this is kind of

**[11:40]** have that. And we think this is kind of

**[11:40]** have that. And we think this is kind of just the start. there's a lot more we

**[11:42]** just the start. there's a lot more we

**[11:42]** just the start. there's a lot more we can do in this area to speed up the

**[11:43]** can do in this area to speed up the

**[11:43]** can do in this area to speed up the model. Uh, and the second one is the

**[11:45]** model. Uh, and the second one is the

**[11:45]** model. Uh, and the second one is the model learned how to behave better as an

**[11:48]** model learned how to behave better as an

**[11:48]** model learned how to behave better as an agent. So, in the beginning, the model

**[11:50]** agent. So, in the beginning, the model

**[11:50]** agent. So, in the beginning, the model was was kind of making too many edits.

**[11:52]** was was kind of making too many edits.

**[11:52]** was was kind of making too many edits. Sometimes the edits were made

**[11:54]** Sometimes the edits were made

**[11:54]** Sometimes the edits were made unnecessarily, but as we trained more

**[11:56]** unnecessarily, but as we trained more

**[11:56]** unnecessarily, but as we trained more and more, the model actually got

**[11:58]** and more, the model actually got

**[11:58]** and more, the model actually got surprisingly better at learning to

**[11:59]** surprisingly better at learning to

**[11:59]** surprisingly better at learning to search and read files more. So, it would


### [12:00 - 13:00]

**[12:02]** search and read files more. So, it would

**[12:02]** search and read files more. So, it would go and find the right thing before it

**[12:03]** go and find the right thing before it

**[12:03]** go and find the right thing before it tried to make edits. Overall, just

**[12:05]** tried to make edits. Overall, just

**[12:05]** tried to make edits. Overall, just being, you know, a bit more effective.

**[12:08]** being, you know, a bit more effective.

**[12:08]** being, you know, a bit more effective. So, we released composer last month in

**[12:10]** So, we released composer last month in

**[12:10]** So, we released composer last month in comp uh cursor 2.0 and so far seems like

**[12:13]** comp uh cursor 2.0 and so far seems like

**[12:13]** comp uh cursor 2.0 and so far seems like people seem to like it. Has anyone here

**[12:15]** people seem to like it. Has anyone here

**[12:15]** people seem to like it. Has anyone here tried the model by chance? Okay, that's

**[12:17]** tried the model by chance? Okay, that's

**[12:18]** tried the model by chance? Okay, that's pretty great. That's more than I

**[12:18]** pretty great. That's more than I

**[12:18]** pretty great. That's more than I expected. So, that's great to hear. I

**[12:20]** expected. So, that's great to hear. I

**[12:20]** expected. So, that's great to hear. I think from my perspective using this

**[12:22]** think from my perspective using this

**[12:22]** think from my perspective using this model and using coding agents for some

**[12:24]** model and using coding agents for some

**[12:24]** model and using coding agents for some time. I kind of describe this problem as

**[12:26]** time. I kind of describe this problem as

**[12:26]** time. I kind of describe this problem as like airplane Wi-Fi. So, when you're on

**[12:29]** like airplane Wi-Fi. So, when you're on

**[12:29]** like airplane Wi-Fi. So, when you're on airplane Wi-Fi, uh it works, but it's

**[12:32]** airplane Wi-Fi, uh it works, but it's

**[12:32]** airplane Wi-Fi, uh it works, but it's kind of frustrating. you really want to

**[12:34]** kind of frustrating. you really want to

**[12:34]** kind of frustrating. you really want to do whatever you're trying to do, but

**[12:35]** do whatever you're trying to do, but

**[12:35]** do whatever you're trying to do, but it's just it's a little slow almost to

**[12:36]** it's just it's a little slow almost to

**[12:36]** it's just it's a little slow almost to where sometimes you wish that you just

**[12:38]** where sometimes you wish that you just

**[12:38]** where sometimes you wish that you just didn't have Wi-Fi at all. And I think

**[12:40]** didn't have Wi-Fi at all. And I think

**[12:40]** didn't have Wi-Fi at all. And I think for some of us who adopted coding agents

**[12:42]** for some of us who adopted coding agents

**[12:42]** for some of us who adopted coding agents very early, it kind of feels like

**[12:44]** very early, it kind of feels like

**[12:44]** very early, it kind of feels like airplane Wi-Fi sometimes cuz if it's

**[12:46]** airplane Wi-Fi sometimes cuz if it's

**[12:46]** airplane Wi-Fi sometimes cuz if it's taking 10 or 20 minutes, you're in this

**[12:48]** taking 10 or 20 minutes, you're in this

**[12:48]** taking 10 or 20 minutes, you're in this weird I think Swiss called it semi async

**[12:51]** weird I think Swiss called it semi async

**[12:51]** weird I think Swiss called it semi async valley of death where you either want

**[12:52]** valley of death where you either want

**[12:52]** valley of death where you either want something that's really fast or you want

**[12:54]** something that's really fast or you want

**[12:54]** something that's really fast or you want the most powerful most intelligent model

**[12:56]** the most powerful most intelligent model

**[12:56]** the most powerful most intelligent model that can run for you know a

**[12:58]** that can run for you know a

**[12:58]** that can run for you know a significantly long amount of time maybe

**[12:59]** significantly long amount of time maybe


### [13:00 - 14:00]

**[13:00]** significantly long amount of time maybe in the background maybe you know 30

**[13:01]** in the background maybe you know 30

**[13:01]** in the background maybe you know 30 minutes days and I think when you're

**[13:04]** minutes days and I think when you're

**[13:04]** minutes days and I think when you're stuck in the middle that's that's very

**[13:05]** stuck in the middle that's that's very

**[13:05]** stuck in the middle that's that's very very painful. So for me composer and I

**[13:08]** very painful. So for me composer and I

**[13:08]** very painful. So for me composer and I think other people it's brought a lot of

**[13:10]** think other people it's brought a lot of

**[13:10]** think other people it's brought a lot of joy back to coding with agents that felt

**[13:12]** joy back to coding with agents that felt

**[13:12]** joy back to coding with agents that felt more like when you were writing code by

**[13:14]** more like when you were writing code by

**[13:14]** more like when you were writing code by hand where you're very in the loop very

**[13:16]** hand where you're very in the loop very

**[13:16]** hand where you're very in the loop very synchronous. So I'm excited to see more

**[13:18]** synchronous. So I'm excited to see more

**[13:18]** synchronous. So I'm excited to see more people exploring this space as well. For

**[13:20]** people exploring this space as well. For

**[13:20]** people exploring this space as well. For me daily uh I'm writing a lot of plans

**[13:23]** me daily uh I'm writing a lot of plans

**[13:23]** me daily uh I'm writing a lot of plans with kind of the latest uh model like

**[13:25]** with kind of the latest uh model like

**[13:25]** with kind of the latest uh model like the the highest frontier. So GPT 5.1

**[13:27]** the the highest frontier. So GPT 5.1

**[13:27]** the the highest frontier. So GPT 5.1 codec is is really great for plans. uh

**[13:29]** codec is is really great for plans. uh

**[13:29]** codec is is really great for plans. uh and then I'm using composer to actually

**[13:31]** and then I'm using composer to actually

**[13:31]** and then I'm using composer to actually take that plan kind of like what Dex

**[13:32]** take that plan kind of like what Dex

**[13:32]** take that plan kind of like what Dex talked about like take the context

**[13:34]** talked about like take the context

**[13:34]** talked about like take the context engineering work and then actually go

**[13:36]** engineering work and then actually go

**[13:36]** engineering work and then actually go and build the thing with it. So uh a few

**[13:39]** and build the thing with it. So uh a few

**[13:39]** and build the thing with it. So uh a few reflections from our research and

**[13:41]** reflections from our research and

**[13:41]** reflections from our research and products team on building composer. The

**[13:44]** products team on building composer. The

**[13:44]** products team on building composer. The first is that RL can work surprisingly

**[13:46]** first is that RL can work surprisingly

**[13:46]** first is that RL can work surprisingly well for training very specific models

**[13:50]** well for training very specific models

**[13:50]** well for training very specific models and you know giving it this high quality

**[13:52]** and you know giving it this high quality

**[13:52]** and you know giving it this high quality data and a decent amount of compute. You

**[13:55]** data and a decent amount of compute. You

**[13:55]** data and a decent amount of compute. You know at cursor we're not trying to build

**[13:57]** know at cursor we're not trying to build

**[13:57]** know at cursor we're not trying to build general intelligence. We're not trying

**[13:58]** general intelligence. We're not trying

**[13:58]** general intelligence. We're not trying to build AGI. We're trying to build very


### [14:00 - 15:00]

**[14:01]** to build AGI. We're trying to build very

**[14:01]** to build AGI. We're trying to build very good coding models and RL RL has worked

**[14:04]** good coding models and RL RL has worked

**[14:04]** good coding models and RL RL has worked surprisingly well for that. The second

**[14:06]** surprisingly well for that. The second

**[14:06]** surprisingly well for that. The second one is uh how much tools AI tools like

**[14:09]** one is uh how much tools AI tools like

**[14:09]** one is uh how much tools AI tools like cursor it doesn't have to be cursor but

**[14:11]** cursor it doesn't have to be cursor but

**[14:11]** cursor it doesn't have to be cursor but like cursor really helps speed up

**[14:13]** like cursor really helps speed up

**[14:13]** like cursor really helps speed up research and development. You know of

**[14:15]** research and development. You know of

**[14:15]** research and development. You know of course our entire team uses cursor to

**[14:17]** course our entire team uses cursor to

**[14:17]** course our entire team uses cursor to help them write code and debug code more

**[14:20]** help them write code and debug code more

**[14:20]** help them write code and debug code more efficiently but that speed up that

**[14:22]** efficiently but that speed up that

**[14:22]** efficiently but that speed up that increase really compounds across all of

**[14:24]** increase really compounds across all of

**[14:24]** increase really compounds across all of our engineering efforts. So we're able

**[14:26]** our engineering efforts. So we're able

**[14:26]** our engineering efforts. So we're able to try more ideas, ship product faster,

**[14:29]** to try more ideas, ship product faster,

**[14:29]** to try more ideas, ship product faster, try new research. Um, so it's been

**[14:31]** try new research. Um, so it's been

**[14:31]** try new research. Um, so it's been really really helpful there. And the

**[14:32]** really really helpful there. And the

**[14:32]** really really helpful there. And the last one that's, you know, personally

**[14:34]** last one that's, you know, personally

**[14:34]** last one that's, you know, personally pretty interesting for me is that

**[14:36]** pretty interesting for me is that

**[14:36]** pretty interesting for me is that it was interesting to see how much of

**[14:38]** it was interesting to see how much of

**[14:38]** it was interesting to see how much of the ML work and the training process was

**[14:40]** the ML work and the training process was

**[14:40]** the ML work and the training process was actually also an infrastructure problem.

**[14:42]** actually also an infrastructure problem.

**[14:42]** actually also an infrastructure problem. They were very correlated. And going

**[14:45]** They were very correlated. And going

**[14:45]** They were very correlated. And going back to my time at Verscell, we saw a

**[14:47]** back to my time at Verscell, we saw a

**[14:47]** back to my time at Verscell, we saw a very similar thing where a lot of the

**[14:49]** very similar thing where a lot of the

**[14:49]** very similar thing where a lot of the magic moments that you can have in

**[14:51]** magic moments that you can have in

**[14:51]** magic moments that you can have in working in frameworks in the JavaScript

**[14:52]** working in frameworks in the JavaScript

**[14:52]** working in frameworks in the JavaScript or Python space, you also need to think

**[14:54]** or Python space, you also need to think

**[14:54]** or Python space, you also need to think a little bit about the infrastructure of

**[14:56]** a little bit about the infrastructure of

**[14:56]** a little bit about the infrastructure of where they're actually deployed. So

**[14:57]** where they're actually deployed. So

**[14:57]** where they're actually deployed. So these things are are more related than

**[14:59]** these things are are more related than

**[14:59]** these things are are more related than people might think. So those are some of


### [15:00 - 16:00]

**[15:01]** people might think. So those are some of

**[15:01]** people might think. So those are some of our reflections. Uh sounds like some of

**[15:03]** our reflections. Uh sounds like some of

**[15:03]** our reflections. Uh sounds like some of you have tried it out. If this is

**[15:04]** you have tried it out. If this is

**[15:04]** you have tried it out. If this is something that you're interested in and

**[15:05]** something that you're interested in and

**[15:05]** something that you're interested in and working on, we're hiring pretty much

**[15:07]** working on, we're hiring pretty much

**[15:07]** working on, we're hiring pretty much across the board at Cursor right now. We

**[15:09]** across the board at Cursor right now. We

**[15:09]** across the board at Cursor right now. We just opened up an office in New York if

**[15:11]** just opened up an office in New York if

**[15:11]** just opened up an office in New York if you're here based in New York. and we'd

**[15:12]** you're here based in New York. and we'd

**[15:12]** you're here based in New York. and we'd love to talk to you about building the

**[15:13]** love to talk to you about building the

**[15:13]** love to talk to you about building the best coding models in the world. Thank

**[15:15]** best coding models in the world. Thank

**[15:15]** best coding models in the world. Thank you.


