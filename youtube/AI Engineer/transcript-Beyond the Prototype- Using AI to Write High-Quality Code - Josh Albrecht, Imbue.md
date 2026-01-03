# Beyond the Prototype- Using AI to Write High-Quality Code - Josh Albrecht, Imbue

**Video URL:** https://www.youtube.com/watch?v=x_1EumTaXeE

---

## Full Transcript

### [00:00 - 01:00]

**[00:20]** It's great to be here. So, I'm Josh

**[00:20]** It's great to be here. So, I'm Josh Albertch. I'm the CTO of Imbue. Uh, and

**[00:23]** Albertch. I'm the CTO of Imbue. Uh, and

**[00:23]** Albertch. I'm the CTO of Imbue. Uh, and our focus is on making more robust,

**[00:26]** our focus is on making more robust,

**[00:26]** our focus is on making more robust, useful AI agents. In particular, we're

**[00:28]** useful AI agents. In particular, we're

**[00:28]** useful AI agents. In particular, we're focusing on software agents right now.

**[00:30]** focusing on software agents right now.

**[00:30]** focusing on software agents right now. And the main product that we're working

**[00:32]** And the main product that we're working

**[00:32]** And the main product that we're working on today is called Sculptor. So, the

**[00:35]** on today is called Sculptor. So, the

**[00:35]** on today is called Sculptor. So, the purpose of Sculptor is to kind of help

**[00:37]** purpose of Sculptor is to kind of help

**[00:37]** purpose of Sculptor is to kind of help us with something that we've all

**[00:38]** us with something that we've all

**[00:38]** us with something that we've all experienced. You know, we've all tried

**[00:40]** experienced. You know, we've all tried

**[00:40]** experienced. You know, we've all tried these vibe coding tools and you, you

**[00:43]** these vibe coding tools and you, you

**[00:43]** these vibe coding tools and you, you know, tell it to go off and do

**[00:45]** know, tell it to go off and do

**[00:45]** know, tell it to go off and do something. It goes off and creates a

**[00:46]** something. It goes off and creates a

**[00:46]** something. It goes off and creates a bunch of code for you. Uh, and then, you

**[00:48]** bunch of code for you. Uh, and then, you

**[00:48]** bunch of code for you. Uh, and then, you know, voila, you're done, right? Well,

**[00:51]** know, voila, you're done, right? Well,

**[00:51]** know, voila, you're done, right? Well, not quite. like at least today there's a

**[00:52]** not quite. like at least today there's a

**[00:52]** not quite. like at least today there's a big gap between kind of the stuff that

**[00:54]** big gap between kind of the stuff that

**[00:54]** big gap between kind of the stuff that comes back uh and what you want to ship

**[00:56]** comes back uh and what you want to ship

**[00:56]** comes back uh and what you want to ship to production especially as you get away

**[00:58]** to production especially as you get away

**[00:58]** to production especially as you get away from the prototyping into a larger more


### [01:00 - 02:00]

**[01:00]** from the prototyping into a larger more

**[01:00]** from the prototyping into a larger more established code bases. So today I'm

**[01:02]** established code bases. So today I'm

**[01:02]** established code bases. So today I'm going to go over some of the technical

**[01:04]** going to go over some of the technical

**[01:04]** going to go over some of the technical decisions that went into the design of

**[01:06]** decisions that went into the design of

**[01:06]** decisions that went into the design of sculpture our experimental coding agent

**[01:09]** sculpture our experimental coding agent

**[01:09]** sculpture our experimental coding agent environment uh and kind of go through

**[01:12]** environment uh and kind of go through

**[01:12]** environment uh and kind of go through some of the context and motivations for

**[01:15]** some of the context and motivations for

**[01:15]** some of the context and motivations for the various ideas that we've explored

**[01:17]** the various ideas that we've explored

**[01:17]** the various ideas that we've explored and the features that we've implemented.

**[01:18]** and the features that we've implemented.

**[01:18]** and the features that we've implemented. It's still a research preview, so these

**[01:21]** It's still a research preview, so these

**[01:21]** It's still a research preview, so these features may change before we actually

**[01:23]** features may change before we actually

**[01:23]** features may change before we actually release it. Uh, but I hope that you know

**[01:26]** release it. Uh, but I hope that you know

**[01:26]** release it. Uh, but I hope that you know whether you're an individual using these

**[01:27]** whether you're an individual using these

**[01:27]** whether you're an individual using these tools or you're someone who's developing

**[01:29]** tools or you're someone who's developing

**[01:29]** tools or you're someone who's developing the tools yourself, you'll find these uh

**[01:31]** the tools yourself, you'll find these uh

**[01:31]** the tools yourself, you'll find these uh kind of learnings from our experiments

**[01:33]** kind of learnings from our experiments

**[01:33]** kind of learnings from our experiments to be useful for yourselves. So today,

**[01:37]** to be useful for yourselves. So today,

**[01:37]** to be useful for yourselves. So today, if you're thinking about how you can

**[01:38]** if you're thinking about how you can

**[01:38]** if you're thinking about how you can make coding agents better, then there's

**[01:40]** make coding agents better, then there's

**[01:40]** make coding agents better, then there's a million different things that you

**[01:42]** a million different things that you

**[01:42]** a million different things that you could build. You could build something

**[01:43]** could build. You could build something

**[01:44]** could build. You could build something that helps improve the performance on

**[01:46]** that helps improve the performance on

**[01:46]** that helps improve the performance on really large context windows. You could

**[01:49]** really large context windows. You could

**[01:49]** really large context windows. You could make something to make it cheaper or

**[01:51]** make something to make it cheaper or

**[01:51]** make something to make it cheaper or faster. You could make something that

**[01:53]** faster. You could make something that

**[01:53]** faster. You could make something that does a better job of parsing the

**[01:54]** does a better job of parsing the

**[01:54]** does a better job of parsing the outputs. But I don't think that we

**[01:57]** outputs. But I don't think that we

**[01:57]** outputs. But I don't think that we really should be building any of these

**[01:58]** really should be building any of these

**[01:58]** really should be building any of these things. I think that what we really want


### [02:00 - 03:00]

**[02:00]** things. I think that what we really want

**[02:00]** things. I think that what we really want to be building is things that are much

**[02:04]** to be building is things that are much

**[02:04]** to be building is things that are much more specific to the use case or to like

**[02:06]** more specific to the use case or to like

**[02:06]** more specific to the use case or to like the problem domain or the thing that you

**[02:08]** the problem domain or the thing that you

**[02:08]** the problem domain or the thing that you are like really specialized in. most of

**[02:11]** are like really specialized in. most of

**[02:11]** are like really specialized in. most of the things that I just mentioned are

**[02:13]** the things that I just mentioned are

**[02:13]** the things that I just mentioned are going to get solved over the next call

**[02:14]** going to get solved over the next call

**[02:14]** going to get solved over the next call it 3 to 12 to 24 months as models get

**[02:17]** it 3 to 12 to 24 months as models get

**[02:18]** it 3 to 12 to 24 months as models get better, coding agents get better etc.

**[02:20]** better, coding agents get better etc.

**[02:20]** better, coding agents get better etc. And so I think you know just like you

**[02:22]** And so I think you know just like you

**[02:22]** And so I think you know just like you wouldn't want to make your own database

**[02:24]** wouldn't want to make your own database

**[02:24]** wouldn't want to make your own database I don't think we want to be spending a

**[02:25]** I don't think we want to be spending a

**[02:25]** I don't think we want to be spending a lot of time working on the problems that

**[02:27]** lot of time working on the problems that

**[02:27]** lot of time working on the problems that are going to get solved uh instead we

**[02:30]** are going to get solved uh instead we

**[02:30]** are going to get solved uh instead we want to focus on the particular part of

**[02:32]** want to focus on the particular part of

**[02:32]** want to focus on the particular part of the problem that really matters for for

**[02:33]** the problem that really matters for for

**[02:33]** the problem that really matters for for us for our business and so at impe

**[02:37]** us for our business and so at impe

**[02:37]** us for our business and so at impe problem that we're focusing on is

**[02:38]** problem that we're focusing on is

**[02:38]** problem that we're focusing on is basically this like what is wrong with

**[02:40]** basically this like what is wrong with

**[02:40]** basically this like what is wrong with this diff you get a coding agent output

**[02:43]** this diff you get a coding agent output

**[02:43]** this diff you get a coding agent output and it tells you like okay I've added 59

**[02:45]** and it tells you like okay I've added 59

**[02:45]** and it tells you like okay I've added 59 new lines are those good like right now

**[02:48]** new lines are those good like right now

**[02:48]** new lines are those good like right now you have an awkward choice between

**[02:50]** you have an awkward choice between

**[02:50]** you have an awkward choice between either looking at each of the lines

**[02:52]** either looking at each of the lines

**[02:52]** either looking at each of the lines yourself or just hitting merge and kind

**[02:54]** yourself or just hitting merge and kind

**[02:54]** yourself or just hitting merge and kind of hoping for the best. Uh, and neither

**[02:56]** of hoping for the best. Uh, and neither

**[02:56]** of hoping for the best. Uh, and neither of those are a really great place to be.

**[02:59]** of those are a really great place to be.

**[02:59]** of those are a really great place to be. So, we try to give you a third option.


### [03:00 - 04:00]

**[03:02]** So, we try to give you a third option.

**[03:02]** So, we try to give you a third option. Uh, the goal is to help build user trust

**[03:05]** Uh, the goal is to help build user trust

**[03:05]** Uh, the goal is to help build user trust by allowing another AI system to come

**[03:08]** by allowing another AI system to come

**[03:08]** by allowing another AI system to come and take a look at this and understand

**[03:10]** and take a look at this and understand

**[03:10]** and take a look at this and understand like, hey, are there any race

**[03:12]** like, hey, are there any race

**[03:12]** like, hey, are there any race conditions? Did you leave your API key

**[03:14]** conditions? Did you leave your API key

**[03:14]** conditions? Did you leave your API key in there, etc. So we want to think about

**[03:17]** in there, etc. So we want to think about

**[03:17]** in there, etc. So we want to think about how do we help leverage AI tools not

**[03:20]** how do we help leverage AI tools not

**[03:20]** how do we help leverage AI tools not just to generate the code but to help us

**[03:21]** just to generate the code but to help us

**[03:21]** just to generate the code but to help us build trust in that code

**[03:24]** build trust in that code

**[03:24]** build trust in that code and kind of the way that we think about

**[03:26]** and kind of the way that we think about

**[03:26]** and kind of the way that we think about it is about like identifying problems

**[03:29]** it is about like identifying problems

**[03:29]** it is about like identifying problems with the code because if there's no

**[03:31]** with the code because if there's no

**[03:31]** with the code because if there's no problems then it's probably high quality

**[03:33]** problems then it's probably high quality

**[03:33]** problems then it's probably high quality code and that's kind of the definition

**[03:35]** code and that's kind of the definition

**[03:35]** code and that's kind of the definition of high quality code. If you think about

**[03:37]** of high quality code. If you think about

**[03:37]** of high quality code. If you think about it from like an academic perspective,

**[03:40]** it from like an academic perspective,

**[03:40]** it from like an academic perspective, the way that people normally measure

**[03:43]** the way that people normally measure

**[03:43]** the way that people normally measure software quality is by looking at the

**[03:45]** software quality is by looking at the

**[03:45]** software quality is by looking at the number of defects and they look at like

**[03:47]** number of defects and they look at like

**[03:47]** number of defects and they look at like how long does it take to fix a

**[03:49]** how long does it take to fix a

**[03:49]** how long does it take to fix a particular defect or how many defects

**[03:51]** particular defect or how many defects

**[03:51]** particular defect or how many defects are caught by this particular technique.

**[03:53]** are caught by this particular technique.

**[03:53]** are caught by this particular technique. So this is sort of the definition that

**[03:54]** So this is sort of the definition that

**[03:54]** So this is sort of the definition that at least we're working on from when

**[03:56]** at least we're working on from when

**[03:56]** at least we're working on from when we're thinking about making high quality

**[03:58]** we're thinking about making high quality

**[03:58]** we're thinking about making high quality software. And then if we think about you


### [04:00 - 05:00]

**[04:01]** software. And then if we think about you

**[04:01]** software. And then if we think about you know the software development process

**[04:03]** know the software development process

**[04:03]** know the software development process what you want to be doing is getting to

**[04:05]** what you want to be doing is getting to

**[04:05]** what you want to be doing is getting to a place where you have identified these

**[04:08]** a place where you have identified these

**[04:08]** a place where you have identified these problems as early as possible. So

**[04:09]** problems as early as possible. So

**[04:10]** problems as early as possible. So sculptor does not work as like a pull

**[04:12]** sculptor does not work as like a pull

**[04:12]** sculptor does not work as like a pull request review tool because that's much

**[04:14]** request review tool because that's much

**[04:14]** request review tool because that's much much later in the process. Rather we

**[04:16]** much later in the process. Rather we

**[04:16]** much later in the process. Rather we want something that's synchronous and

**[04:18]** want something that's synchronous and

**[04:18]** want something that's synchronous and immediate and giving you immediate

**[04:19]** immediate and giving you immediate

**[04:19]** immediate and giving you immediate feedback. As soon as you've generated

**[04:21]** feedback. As soon as you've generated

**[04:21]** feedback. As soon as you've generated that code, as soon as you've changed

**[04:22]** that code, as soon as you've changed

**[04:22]** that code, as soon as you've changed that line, you want to know like is

**[04:24]** that line, you want to know like is

**[04:24]** that line, you want to know like is there something wrong with it? That's

**[04:25]** there something wrong with it? That's

**[04:25]** there something wrong with it? That's easier both for you to fix and also for

**[04:28]** easier both for you to fix and also for

**[04:28]** easier both for you to fix and also for the agent to fix.

**[04:30]** the agent to fix.

**[04:30]** the agent to fix. So what are some ways that you can

**[04:32]** So what are some ways that you can

**[04:32]** So what are some ways that you can prevent problems in AI generated code?

**[04:35]** prevent problems in AI generated code?

**[04:35]** prevent problems in AI generated code? We're going to go through five different

**[04:36]** We're going to go through five different

**[04:36]** We're going to go through five different ways. Uh the first is learning planning

**[04:40]** ways. Uh the first is learning planning

**[04:40]** ways. Uh the first is learning planning or sorry only four different ways.

**[04:42]** or sorry only four different ways.

**[04:42]** or sorry only four different ways. Learning, planning, writing specs, and

**[04:44]** Learning, planning, writing specs, and

**[04:44]** Learning, planning, writing specs, and having a really strict style guide. And

**[04:46]** having a really strict style guide. And

**[04:46]** having a really strict style guide. And we'll see how those manifest in

**[04:47]** we'll see how those manifest in

**[04:47]** we'll see how those manifest in Sculptor.

**[04:53]** So the first thing you want to do when

**[04:53]** So the first thing you want to do when you're using coding agents if you're

**[04:55]** you're using coding agents if you're

**[04:55]** you're using coding agents if you're trying to prevent problems is learn

**[04:56]** trying to prevent problems is learn

**[04:56]** trying to prevent problems is learn what's out there. We try to make this as

**[04:58]** what's out there. We try to make this as

**[04:58]** what's out there. We try to make this as easy as possible in sculpture by letting


### [05:00 - 06:00]

**[05:00]** easy as possible in sculpture by letting

**[05:00]** easy as possible in sculpture by letting you ask questions,

**[05:02]** you ask questions,

**[05:02]** you ask questions, have it do research, get answers about

**[05:04]** have it do research, get answers about

**[05:04]** have it do research, get answers about what are the technologies, etc. that

**[05:06]** what are the technologies, etc. that

**[05:06]** what are the technologies, etc. that exist, what are the ways that other

**[05:07]** exist, what are the ways that other

**[05:07]** exist, what are the ways that other people have solved similar problems so

**[05:09]** people have solved similar problems so

**[05:09]** people have solved similar problems so that you don't end up reproducing a

**[05:11]** that you don't end up reproducing a

**[05:11]** that you don't end up reproducing a bunch of work for what's already out

**[05:12]** bunch of work for what's already out

**[05:12]** bunch of work for what's already out there.

**[05:15]** there.

**[05:15]** there. Next, we want to think about how we can

**[05:17]** Next, we want to think about how we can

**[05:17]** Next, we want to think about how we can encourage people to start by planning.

**[05:19]** encourage people to start by planning.

**[05:19]** encourage people to start by planning. Here's a little example workflow where

**[05:22]** Here's a little example workflow where

**[05:22]** Here's a little example workflow where you can, you know, kick off the agent to

**[05:24]** you can, you know, kick off the agent to

**[05:24]** you can, you know, kick off the agent to go do something simple like, you know,

**[05:25]** go do something simple like, you know,

**[05:25]** go do something simple like, you know, implement this Scrabble solver and

**[05:27]** implement this Scrabble solver and

**[05:27]** implement this Scrabble solver and change the system prompt here to force

**[05:30]** change the system prompt here to force

**[05:30]** change the system prompt here to force the AI agent to first make a plan

**[05:32]** the AI agent to first make a plan

**[05:32]** the AI agent to first make a plan without writing any code at all. Then

**[05:35]** without writing any code at all. Then

**[05:35]** without writing any code at all. Then you can wait a little while. It'll

**[05:36]** you can wait a little while. It'll

**[05:36]** you can wait a little while. It'll generate the plan. Uh, and then you can

**[05:39]** generate the plan. Uh, and then you can

**[05:39]** generate the plan. Uh, and then you can go and change the system prompt again to

**[05:41]** go and change the system prompt again to

**[05:41]** go and change the system prompt again to say like, okay, now we can actually

**[05:43]** say like, okay, now we can actually

**[05:43]** say like, okay, now we can actually create some code. So we make it really

**[05:45]** create some code. So we make it really

**[05:45]** create some code. So we make it really easy to kind of change these types of

**[05:46]** easy to kind of change these types of

**[05:46]** easy to kind of change these types of meta parameters of the coding agent

**[05:48]** meta parameters of the coding agent

**[05:48]** meta parameters of the coding agent itself. Of course you can just tell the

**[05:50]** itself. Of course you can just tell the

**[05:50]** itself. Of course you can just tell the agent to do that. But by changing its

**[05:52]** agent to do that. But by changing its

**[05:52]** agent to do that. But by changing its system prompt you sort of force it in a

**[05:54]** system prompt you sort of force it in a

**[05:54]** system prompt you sort of force it in a much stronger way to uh change its

**[05:56]** much stronger way to uh change its

**[05:56]** much stronger way to uh change its behavior. And you can build up larger

**[05:58]** behavior. And you can build up larger

**[05:58]** behavior. And you can build up larger workflows by making sort of customized


### [06:00 - 07:00]

**[06:00]** workflows by making sort of customized

**[06:00]** workflows by making sort of customized agents for always plan first then always

**[06:03]** agents for always plan first then always

**[06:03]** agents for always plan first then always do the code then always run the checks

**[06:05]** do the code then always run the checks

**[06:05]** do the code then always run the checks etc.

**[06:10]** Third, you want to think about writing

**[06:10]** Third, you want to think about writing specs and docs as a kind of first class

**[06:12]** specs and docs as a kind of first class

**[06:12]** specs and docs as a kind of first class part of the workflow. One of the main

**[06:15]** part of the workflow. One of the main

**[06:15]** part of the workflow. One of the main reasons why, at least I don't normally

**[06:17]** reasons why, at least I don't normally

**[06:17]** reasons why, at least I don't normally write lots of specs and docs in the past

**[06:20]** write lots of specs and docs in the past

**[06:20]** write lots of specs and docs in the past has been that it's kind of annoying to

**[06:21]** has been that it's kind of annoying to

**[06:22]** has been that it's kind of annoying to keep them all up to date to spend all

**[06:23]** keep them all up to date to spend all

**[06:23]** keep them all up to date to spend all this time kind of typing everything out

**[06:25]** this time kind of typing everything out

**[06:25]** this time kind of typing everything out if I already know what the code is

**[06:26]** if I already know what the code is

**[06:26]** if I already know what the code is supposed to be. But this is really

**[06:29]** supposed to be. But this is really

**[06:29]** supposed to be. But this is really important to do if you want the coding

**[06:31]** important to do if you want the coding

**[06:31]** important to do if you want the coding agents to actually have context on the

**[06:33]** agents to actually have context on the

**[06:33]** agents to actually have context on the project that you're trying to do because

**[06:34]** project that you're trying to do because

**[06:34]** project that you're trying to do because they don't have access to your email,

**[06:36]** they don't have access to your email,

**[06:36]** they don't have access to your email, your Slack, etc. necessarily. And even

**[06:38]** your Slack, etc. necessarily. And even

**[06:38]** your Slack, etc. necessarily. And even if they did, they might not know exactly

**[06:40]** if they did, they might not know exactly

**[06:40]** if they did, they might not know exactly how to turn that into code. So in

**[06:43]** how to turn that into code. So in

**[06:43]** how to turn that into code. So in Sculptor, uh, one of the ways that we

**[06:45]** Sculptor, uh, one of the ways that we

**[06:46]** Sculptor, uh, one of the ways that we try to make this easier is by helping

**[06:48]** try to make this easier is by helping

**[06:48]** try to make this easier is by helping detect if the code and the docs have

**[06:51]** detect if the code and the docs have

**[06:52]** detect if the code and the docs have become outdated. So it reduces the

**[06:54]** become outdated. So it reduces the

**[06:54]** become outdated. So it reduces the barrier to writing and maintaining

**[06:56]** barrier to writing and maintaining

**[06:56]** barrier to writing and maintaining documentation and dock strings because

**[06:58]** documentation and dock strings because

**[06:58]** documentation and dock strings because now you have a way of more automatically

**[06:59]** now you have a way of more automatically


### [07:00 - 08:00]

**[07:00]** now you have a way of more automatically fixing the inconsistencies. It can also

**[07:03]** fixing the inconsistencies. It can also

**[07:03]** fixing the inconsistencies. It can also highlight inconsistencies or parts of

**[07:05]** highlight inconsistencies or parts of

**[07:05]** highlight inconsistencies or parts of the specifications that conflict with

**[07:07]** the specifications that conflict with

**[07:07]** the specifications that conflict with each other, making it easier to make

**[07:09]** each other, making it easier to make

**[07:09]** each other, making it easier to make sure that your system makes sense from

**[07:10]** sure that your system makes sense from

**[07:10]** sure that your system makes sense from the very beginning.

**[07:12]** the very beginning.

**[07:12]** the very beginning. And finally, you want to have a really

**[07:14]** And finally, you want to have a really

**[07:14]** And finally, you want to have a really strict style guide and try to enforce

**[07:16]** strict style guide and try to enforce

**[07:16]** strict style guide and try to enforce it. This is important even if you're

**[07:18]** it. This is important even if you're

**[07:18]** it. This is important even if you're just doing regular coding without AI

**[07:20]** just doing regular coding without AI

**[07:20]** just doing regular coding without AI agents, just with other human software

**[07:21]** agents, just with other human software

**[07:21]** agents, just with other human software engineers. But one of the things that is

**[07:24]** engineers. But one of the things that is

**[07:24]** engineers. But one of the things that is special in sculptor is that we make

**[07:25]** special in sculptor is that we make

**[07:25]** special in sculptor is that we make suggestions which you can see towards

**[07:27]** suggestions which you can see towards

**[07:27]** suggestions which you can see towards the bottom here uh that help keep the AI

**[07:30]** the bottom here uh that help keep the AI

**[07:30]** the bottom here uh that help keep the AI system on a reasonable path. So here

**[07:34]** system on a reasonable path. So here

**[07:34]** system on a reasonable path. So here it's highlighting that you could you

**[07:36]** it's highlighting that you could you

**[07:36]** it's highlighting that you could you know make this particular class

**[07:37]** know make this particular class

**[07:37]** know make this particular class immutable to prevent race conditions.

**[07:39]** immutable to prevent race conditions.

**[07:39]** immutable to prevent race conditions. Was this something that comes from our

**[07:40]** Was this something that comes from our

**[07:40]** Was this something that comes from our style guide where we try to encourage

**[07:43]** style guide where we try to encourage

**[07:43]** style guide where we try to encourage both the coding agents and our teammates

**[07:45]** both the coding agents and our teammates

**[07:45]** both the coding agents and our teammates to write things in a more functional

**[07:47]** to write things in a more functional

**[07:47]** to write things in a more functional immutable style to prevent certain

**[07:49]** immutable style to prevent certain

**[07:49]** immutable style to prevent certain classes of errors. We're also working on

**[07:52]** classes of errors. We're also working on

**[07:52]** classes of errors. We're also working on developing a style guide that's sort of

**[07:54]** developing a style guide that's sort of

**[07:54]** developing a style guide that's sort of customtailored to AI agents to make it

**[07:56]** customtailored to AI agents to make it

**[07:56]** customtailored to AI agents to make it even easier for them to avoid some of

**[07:59]** even easier for them to avoid some of

**[07:59]** even easier for them to avoid some of the most egregious mistakes that they


### [08:00 - 09:00]

**[08:00]** the most egregious mistakes that they

**[08:00]** the most egregious mistakes that they normally make.

**[08:03]** normally make.

**[08:03]** normally make. But no matter how many uh things you do

**[08:06]** But no matter how many uh things you do

**[08:06]** But no matter how many uh things you do to prevent the AI system from making

**[08:08]** to prevent the AI system from making

**[08:08]** to prevent the AI system from making mistakes in the first place, it's going

**[08:10]** mistakes in the first place, it's going

**[08:10]** mistakes in the first place, it's going to make some mistakes. And there are

**[08:13]** to make some mistakes. And there are

**[08:13]** to make some mistakes. And there are many things that we can do to prevent or

**[08:16]** many things that we can do to prevent or

**[08:16]** many things that we can do to prevent or to detect those problems and prevent

**[08:17]** to detect those problems and prevent

**[08:17]** to detect those problems and prevent them from getting into production. So

**[08:19]** them from getting into production. So

**[08:19]** them from getting into production. So we'll go through three here.

**[08:22]** we'll go through three here.

**[08:22]** we'll go through three here. Uh first running llinters, second

**[08:25]** Uh first running llinters, second

**[08:25]** Uh first running llinters, second writing and running tests, third asking

**[08:27]** writing and running tests, third asking

**[08:27]** writing and running tests, third asking an LLM. Uh and we'll dig into each and

**[08:29]** an LLM. Uh and we'll dig into each and

**[08:29]** an LLM. Uh and we'll dig into each and see how that manifests in sculpture. So

**[08:32]** see how that manifests in sculpture. So

**[08:32]** see how that manifests in sculpture. So for the first one for running llinters,

**[08:34]** for the first one for running llinters,

**[08:34]** for the first one for running llinters, there are many automated tools that are

**[08:36]** there are many automated tools that are

**[08:36]** there are many automated tools that are out there like rough or my pylind py etc

**[08:40]** out there like rough or my pylind py etc

**[08:40]** out there like rough or my pylind py etc that you can use to automatically detect

**[08:43]** that you can use to automatically detect

**[08:43]** that you can use to automatically detect certain classes of errors.

**[08:46]** certain classes of errors.

**[08:46]** certain classes of errors. In normal development, this is sort of

**[08:48]** In normal development, this is sort of

**[08:48]** In normal development, this is sort of obnoxious because you have to go fix all

**[08:50]** obnoxious because you have to go fix all

**[08:50]** obnoxious because you have to go fix all these like really small errors that

**[08:52]** these like really small errors that

**[08:52]** these like really small errors that don't necessarily cause problems. It's a

**[08:54]** don't necessarily cause problems. It's a

**[08:54]** don't necessarily cause problems. It's a lot of like churn and extra work. But

**[08:57]** lot of like churn and extra work. But

**[08:57]** lot of like churn and extra work. But one of the great things about AI systems

**[08:58]** one of the great things about AI systems

**[08:58]** one of the great things about AI systems is that they're really good at fixing

**[08:59]** is that they're really good at fixing


### [09:00 - 10:00]

**[09:00]** is that they're really good at fixing these. So, one of the things that we've

**[09:02]** these. So, one of the things that we've

**[09:02]** these. So, one of the things that we've built into Sculptor is the ability for

**[09:04]** built into Sculptor is the ability for

**[09:04]** built into Sculptor is the ability for the system to very easily detect these

**[09:07]** the system to very easily detect these

**[09:07]** the system to very easily detect these types of issues and automatically fix

**[09:09]** types of issues and automatically fix

**[09:09]** types of issues and automatically fix them for you without you having to get

**[09:10]** them for you without you having to get

**[09:10]** them for you without you having to get involved. Another thing that we've done

**[09:13]** involved. Another thing that we've done

**[09:13]** involved. Another thing that we've done is make it easy to use these tools in

**[09:17]** is make it easy to use these tools in

**[09:17]** is make it easy to use these tools in practice. A lot of tools end up like

**[09:20]** practice. A lot of tools end up like

**[09:20]** practice. A lot of tools end up like these. You know, how many people here,

**[09:22]** these. You know, how many people here,

**[09:22]** these. You know, how many people here, maybe a show of hands, how many people

**[09:24]** maybe a show of hands, how many people

**[09:24]** maybe a show of hands, how many people have a llinter set up at all?

**[09:28]** have a llinter set up at all?

**[09:28]** have a llinter set up at all? Okay. How many people have zero linting

**[09:30]** Okay. How many people have zero linting

**[09:30]** Okay. How many people have zero linting errors in their codebase? Two. Great.

**[09:33]** errors in their codebase? Two. Great.

**[09:34]** errors in their codebase? Two. Great. We'll hire you. Okay, cool. Uh but you

**[09:36]** We'll hire you. Okay, cool. Uh but you

**[09:36]** We'll hire you. Okay, cool. Uh but you know it's it's not it's not easy. But

**[09:38]** know it's it's not it's not easy. But

**[09:38]** know it's it's not it's not easy. But one of the things that we've done in

**[09:39]** one of the things that we've done in

**[09:39]** one of the things that we've done in sculpture is make it so that the AI

**[09:41]** sculpture is make it so that the AI

**[09:42]** sculpture is make it so that the AI system understands what issues were

**[09:43]** system understands what issues were

**[09:43]** system understands what issues were there before it started and then what

**[09:45]** there before it started and then what

**[09:45]** there before it started and then what issues were there after it ran. So at

**[09:47]** issues were there after it ran. So at

**[09:47]** issues were there after it ran. So at least you can prevent the AI system from

**[09:49]** least you can prevent the AI system from

**[09:49]** least you can prevent the AI system from creating more errors without you even if

**[09:51]** creating more errors without you even if

**[09:51]** creating more errors without you even if it doesn't work in a perfectly clean

**[09:52]** it doesn't work in a perfectly clean

**[09:52]** it doesn't work in a perfectly clean codebase.

**[09:54]** codebase.

**[09:54]** codebase. Okay. Third, testing. So why should you

**[09:58]** Okay. Third, testing. So why should you

**[09:58]** Okay. Third, testing. So why should you write tests at all? I think I was pretty


### [10:00 - 11:00]

**[10:01]** write tests at all? I think I was pretty

**[10:01]** write tests at all? I think I was pretty lazy as a developer for a long time and

**[10:03]** lazy as a developer for a long time and

**[10:03]** lazy as a developer for a long time and did not want to write tests because it

**[10:04]** did not want to write tests because it

**[10:04]** did not want to write tests because it took a you know a lot of effort. You

**[10:06]** took a you know a lot of effort. You

**[10:06]** took a you know a lot of effort. You have to maintain them. I already wrote

**[10:08]** have to maintain them. I already wrote

**[10:08]** have to maintain them. I already wrote the code. It works. Okay. But one of the

**[10:12]** the code. It works. Okay. But one of the

**[10:12]** the code. It works. Okay. But one of the major objections to writing tests has

**[10:13]** major objections to writing tests has

**[10:13]** major objections to writing tests has kind of disappeared now that we have AI

**[10:15]** kind of disappeared now that we have AI

**[10:15]** kind of disappeared now that we have AI systems. The ability to generate tests

**[10:18]** systems. The ability to generate tests

**[10:18]** systems. The ability to generate tests is now so easy that you might as well

**[10:20]** is now so easy that you might as well

**[10:20]** is now so easy that you might as well write tests. Especially if you have

**[10:21]** write tests. Especially if you have

**[10:21]** write tests. Especially if you have correct code. You can tell the agent,

**[10:23]** correct code. You can tell the agent,

**[10:23]** correct code. You can tell the agent, hey, just write a bunch of tests, throw

**[10:25]** hey, just write a bunch of tests, throw

**[10:25]** hey, just write a bunch of tests, throw out the ones that don't pass, and just

**[10:26]** out the ones that don't pass, and just

**[10:26]** out the ones that don't pass, and just keep the rest. So there's no real reason

**[10:28]** keep the rest. So there's no real reason

**[10:28]** keep the rest. So there's no real reason to not write tests at all. Uh and B at

**[10:33]** to not write tests at all. Uh and B at

**[10:33]** to not write tests at all. Uh and B at as they say at Google, if you liked it,

**[10:35]** as they say at Google, if you liked it,

**[10:35]** as they say at Google, if you liked it, you should have put a test on it. This

**[10:37]** you should have put a test on it. This

**[10:37]** you should have put a test on it. This becomes much more important with coding

**[10:38]** becomes much more important with coding

**[10:38]** becomes much more important with coding agents. The reason is that you don't

**[10:41]** agents. The reason is that you don't

**[10:41]** agents. The reason is that you don't want your coding agent to go change the

**[10:43]** want your coding agent to go change the

**[10:43]** want your coding agent to go change the behavior of your system in a way that

**[10:44]** behavior of your system in a way that

**[10:44]** behavior of your system in a way that you don't understand and don't expect

**[10:46]** you don't understand and don't expect

**[10:46]** you don't understand and don't expect and don't want to see happen. So at

**[10:49]** and don't want to see happen. So at

**[10:49]** and don't want to see happen. So at Google, this matters a lot for their

**[10:50]** Google, this matters a lot for their

**[10:50]** Google, this matters a lot for their infrastructure because they don't want

**[10:51]** infrastructure because they don't want

**[10:51]** infrastructure because they don't want their site to crash when someone changes

**[10:53]** their site to crash when someone changes

**[10:53]** their site to crash when someone changes something. But if you really care about

**[10:55]** something. But if you really care about

**[10:55]** something. But if you really care about the behavior of your system, you want to

**[10:57]** the behavior of your system, you want to

**[10:57]** the behavior of your system, you want to make sure that it's fully tested.

**[10:59]** make sure that it's fully tested.

**[10:59]** make sure that it's fully tested. So how do we actually write good tests?


### [11:00 - 12:00]

**[11:02]** So how do we actually write good tests?

**[11:02]** So how do we actually write good tests? I'll go through a bunch of different uh

**[11:03]** I'll go through a bunch of different uh

**[11:03]** I'll go through a bunch of different uh components to this. So first, one of the

**[11:06]** components to this. So first, one of the

**[11:06]** components to this. So first, one of the things that you can do is write code in

**[11:09]** things that you can do is write code in

**[11:09]** things that you can do is write code in a functional style. By this I mean code

**[11:11]** a functional style. By this I mean code

**[11:12]** a functional style. By this I mean code that has no side effects. This makes it

**[11:14]** that has no side effects. This makes it

**[11:14]** that has no side effects. This makes it much much easier to run LLM and

**[11:17]** much much easier to run LLM and

**[11:17]** much much easier to run LLM and understand if the code is actually

**[11:19]** understand if the code is actually

**[11:19]** understand if the code is actually successful. You really don't want to be

**[11:21]** successful. You really don't want to be

**[11:21]** successful. You really don't want to be running a test that has access to say

**[11:23]** running a test that has access to say

**[11:23]** running a test that has access to say your live Gmail environment where if you

**[11:26]** your live Gmail environment where if you

**[11:26]** your live Gmail environment where if you make a single mistake you can delete all

**[11:28]** make a single mistake you can delete all

**[11:28]** make a single mistake you can delete all of your email. You really want to

**[11:29]** of your email. You really want to

**[11:29]** of your email. You really want to isolate those types of side effects and

**[11:31]** isolate those types of side effects and

**[11:31]** isolate those types of side effects and be able to focus most of the code uh on

**[11:34]** be able to focus most of the code uh on

**[11:34]** be able to focus most of the code uh on the kind of functional transformations

**[11:35]** the kind of functional transformations

**[11:35]** the kind of functional transformations that matter for your program.

**[11:38]** that matter for your program.

**[11:38]** that matter for your program. Second, you can try and write two

**[11:40]** Second, you can try and write two

**[11:40]** Second, you can try and write two different types of unit tests. Happy

**[11:43]** different types of unit tests. Happy

**[11:43]** different types of unit tests. Happy path unit tests are those that are ones

**[11:45]** path unit tests are those that are ones

**[11:45]** path unit tests are those that are ones that show you that your code is working.

**[11:47]** that show you that your code is working.

**[11:47]** that show you that your code is working. It's happy. Hooray, it worked. uh you

**[11:49]** It's happy. Hooray, it worked. uh you

**[11:49]** It's happy. Hooray, it worked. uh you don't need that many of those. You just

**[11:50]** don't need that many of those. You just

**[11:50]** don't need that many of those. You just need a small number to show that things

**[11:52]** need a small number to show that things

**[11:52]** need a small number to show that things are working as you hope. The unhappy

**[11:54]** are working as you hope. The unhappy

**[11:54]** are working as you hope. The unhappy unit tests are the ones that help us

**[11:56]** unit tests are the ones that help us

**[11:56]** unit tests are the ones that help us find bugs. And here LLMs can be really,

**[11:59]** find bugs. And here LLMs can be really,

**[11:59]** find bugs. And here LLMs can be really, really helpful. So, especially if you've


### [12:00 - 13:00]

**[12:01]** really helpful. So, especially if you've

**[12:01]** really helpful. So, especially if you've written your code in a functional style,

**[12:03]** written your code in a functional style,

**[12:03]** written your code in a functional style, you can have the LLM generate hundreds

**[12:05]** you can have the LLM generate hundreds

**[12:05]** you can have the LLM generate hundreds or even thousands of potential inputs,

**[12:07]** or even thousands of potential inputs,

**[12:07]** or even thousands of potential inputs, see what happens to those inputs, and

**[12:09]** see what happens to those inputs, and

**[12:09]** see what happens to those inputs, and then ask the LLM, does that look weird?

**[12:12]** then ask the LLM, does that look weird?

**[12:12]** then ask the LLM, does that look weird? And often when it says yes, that will be

**[12:14]** And often when it says yes, that will be

**[12:14]** And often when it says yes, that will be a bug. And so now you have a perfect

**[12:15]** a bug. And so now you have a perfect

**[12:15]** a bug. And so now you have a perfect test case replicating a bug.

**[12:18]** test case replicating a bug.

**[12:18]** test case replicating a bug. Third, after you've written your unit

**[12:20]** Third, after you've written your unit

**[12:20]** Third, after you've written your unit tests, it's maybe a good idea to throw

**[12:23]** tests, it's maybe a good idea to throw

**[12:23]** tests, it's maybe a good idea to throw them away in some cases. This is a

**[12:25]** them away in some cases. This is a

**[12:25]** them away in some cases. This is a little bit counterintuitive.

**[12:27]** little bit counterintuitive.

**[12:27]** little bit counterintuitive. In the past, it spent we took all this

**[12:29]** In the past, it spent we took all this

**[12:29]** In the past, it spent we took all this effort and spent all this time trying to

**[12:31]** effort and spent all this time trying to

**[12:31]** effort and spent all this time trying to write good unit tests and so we feel

**[12:33]** write good unit tests and so we feel

**[12:33]** write good unit tests and so we feel some aversion to throwing them away. But

**[12:35]** some aversion to throwing them away. But

**[12:35]** some aversion to throwing them away. But now that it's so easy to run LLM and

**[12:38]** now that it's so easy to run LLM and

**[12:38]** now that it's so easy to run LLM and generate the test suite again from

**[12:39]** generate the test suite again from

**[12:39]** generate the test suite again from scratch, there's a reason a good reason

**[12:42]** scratch, there's a reason a good reason

**[12:42]** scratch, there's a reason a good reason to not keep around too many unit tests

**[12:44]** to not keep around too many unit tests

**[12:44]** to not keep around too many unit tests of behavior you don't care about too

**[12:46]** of behavior you don't care about too

**[12:46]** of behavior you don't care about too much. You might also want to just

**[12:48]** much. You might also want to just

**[12:48]** much. You might also want to just refactor the ones that you generated

**[12:49]** refactor the ones that you generated

**[12:49]** refactor the ones that you generated into something that's slightly more

**[12:50]** into something that's slightly more

**[12:50]** into something that's slightly more maintainable. But when you do keep them

**[12:52]** maintainable. But when you do keep them

**[12:52]** maintainable. But when you do keep them around, it does kind of confuse the LLM

**[12:54]** around, it does kind of confuse the LLM

**[12:54]** around, it does kind of confuse the LLM when you come back and change this

**[12:55]** when you come back and change this

**[12:55]** when you come back and change this behavior. So it's something that's at

**[12:56]** behavior. So it's something that's at

**[12:56]** behavior. So it's something that's at least worth thinking about whether you

**[12:58]** least worth thinking about whether you

**[12:58]** least worth thinking about whether you want to keep the tests that were

**[12:59]** want to keep the tests that were

**[12:59]** want to keep the tests that were originally generated, clean them up, how


### [13:00 - 14:00]

**[13:01]** originally generated, clean them up, how

**[13:01]** originally generated, clean them up, how many of them should you keep, etc.

**[13:04]** many of them should you keep, etc.

**[13:04]** many of them should you keep, etc. Fourth, you should probably focus on

**[13:05]** Fourth, you should probably focus on

**[13:05]** Fourth, you should probably focus on integration tests uh as opposed to

**[13:08]** integration tests uh as opposed to

**[13:08]** integration tests uh as opposed to testing only the kind of code level

**[13:11]** testing only the kind of code level

**[13:11]** testing only the kind of code level functional uh behavior of your program.

**[13:14]** functional uh behavior of your program.

**[13:14]** functional uh behavior of your program. Integration tests are those that show

**[13:15]** Integration tests are those that show

**[13:15]** Integration tests are those that show you that your program actually works.

**[13:17]** you that your program actually works.

**[13:17]** you that your program actually works. Like from the user's perspective, like

**[13:18]** Like from the user's perspective, like

**[13:18]** Like from the user's perspective, like when the user clicks on this thing, does

**[13:21]** when the user clicks on this thing, does

**[13:21]** when the user clicks on this thing, does this other thing happen? AI systems can

**[13:24]** this other thing happen? AI systems can

**[13:24]** this other thing happen? AI systems can be extremely good at writing these,

**[13:25]** be extremely good at writing these,

**[13:25]** be extremely good at writing these, especially if you create nice test plans

**[13:28]** especially if you create nice test plans

**[13:28]** especially if you create nice test plans where you can write, okay, when the user

**[13:30]** where you can write, okay, when the user

**[13:30]** where you can write, okay, when the user clicks on the button to add the item to

**[13:31]** clicks on the button to add the item to

**[13:31]** clicks on the button to add the item to the shopping cart, then the item is in

**[13:33]** the shopping cart, then the item is in

**[13:33]** the shopping cart, then the item is in the shopping cart. If you write that out

**[13:35]** the shopping cart. If you write that out

**[13:35]** the shopping cart. If you write that out and then you write the test, then you

**[13:37]** and then you write the test, then you

**[13:37]** and then you write the test, then you can write another test plan like if the

**[13:39]** can write another test plan like if the

**[13:39]** can write another test plan like if the user clicks to remove the button, the

**[13:41]** user clicks to remove the button, the

**[13:41]** user clicks to remove the button, the thing from the shopping cart, then it is

**[13:43]** thing from the shopping cart, then it is

**[13:43]** thing from the shopping cart, then it is gone. that systems can almost always get

**[13:45]** gone. that systems can almost always get

**[13:45]** gone. that systems can almost always get this right and so it allows you to work

**[13:47]** this right and so it allows you to work

**[13:47]** this right and so it allows you to work at the level of meaning for your testing

**[13:49]** at the level of meaning for your testing

**[13:49]** at the level of meaning for your testing which can be much more efficient. Uh

**[13:52]** which can be much more efficient. Uh

**[13:52]** which can be much more efficient. Uh fifth, you want to think about test

**[13:53]** fifth, you want to think about test

**[13:54]** fifth, you want to think about test coverage as a core part of your testing

**[13:56]** coverage as a core part of your testing

**[13:56]** coverage as a core part of your testing suite. So if you're having cloud code

**[13:59]** suite. So if you're having cloud code

**[13:59]** suite. So if you're having cloud code write things for you then you don't care


### [14:00 - 15:00]

**[14:02]** write things for you then you don't care

**[14:02]** write things for you then you don't care just about the tests working on their

**[14:04]** just about the tests working on their

**[14:04]** just about the tests working on their own but you also care are there enough

**[14:05]** own but you also care are there enough

**[14:05]** own but you also care are there enough tests in the first place. If you think

**[14:08]** tests in the first place. If you think

**[14:08]** tests in the first place. If you think back to the original screenshot where we

**[14:09]** back to the original screenshot where we

**[14:10]** back to the original screenshot where we get back our PR of you know how many

**[14:12]** get back our PR of you know how many

**[14:12]** get back our PR of you know how many lines have changed. If I tell you how

**[14:13]** lines have changed. If I tell you how

**[14:13]** lines have changed. If I tell you how many lines have changed, it's not that

**[14:15]** many lines have changed, it's not that

**[14:15]** many lines have changed, it's not that helpful. If I tell you so many lines

**[14:18]** helpful. If I tell you so many lines

**[14:18]** helpful. If I tell you so many lines have changed and also there's 100% test

**[14:21]** have changed and also there's 100% test

**[14:21]** have changed and also there's 100% test coverage and also all the tests pass and

**[14:23]** coverage and also all the tests pass and

**[14:23]** coverage and also all the tests pass and also a thing looked at the tests and

**[14:24]** also a thing looked at the tests and

**[14:24]** also a thing looked at the tests and thought they were reasonable. Now you

**[14:26]** thought they were reasonable. Now you

**[14:26]** thought they were reasonable. Now you can probably click on that merge button

**[14:28]** can probably click on that merge button

**[14:28]** can probably click on that merge button without quite as much fear. Uh and sixth

**[14:31]** without quite as much fear. Uh and sixth

**[14:31]** without quite as much fear. Uh and sixth uh we try to make it easy to run tests

**[14:33]** uh we try to make it easy to run tests

**[14:33]** uh we try to make it easy to run tests in sandboxes and without secrets as much

**[14:35]** in sandboxes and without secrets as much

**[14:35]** in sandboxes and without secrets as much as possible.

**[14:37]** as possible.

**[14:37]** as possible. This uh makes it a lot easier to

**[14:39]** This uh makes it a lot easier to

**[14:39]** This uh makes it a lot easier to actually fix things and makes it a lot

**[14:42]** actually fix things and makes it a lot

**[14:42]** actually fix things and makes it a lot easier to make sure that you're not

**[14:43]** easier to make sure that you're not

**[14:43]** easier to make sure that you're not accidentally causing problems or making

**[14:45]** accidentally causing problems or making

**[14:45]** accidentally causing problems or making flaky tests.

**[14:47]** flaky tests.

**[14:47]** flaky tests. The third thing that we can do to detect

**[14:49]** The third thing that we can do to detect

**[14:49]** The third thing that we can do to detect errors is ask an LLM. There are many

**[14:53]** errors is ask an LLM. There are many

**[14:53]** errors is ask an LLM. There are many different things that we can check for,

**[14:54]** different things that we can check for,

**[14:54]** different things that we can check for, including if there are issues before you

**[14:56]** including if there are issues before you

**[14:56]** including if there are issues before you commit with your current change, if the

**[14:58]** commit with your current change, if the

**[14:58]** commit with your current change, if the thing that you're trying to do even

**[14:59]** thing that you're trying to do even


### [15:00 - 16:00]

**[15:00]** thing that you're trying to do even makes sense, if there are issues in the

**[15:01]** makes sense, if there are issues in the

**[15:02]** makes sense, if there are issues in the current branch you're working on, if

**[15:03]** current branch you're working on, if

**[15:03]** current branch you're working on, if there are violations of rules in your

**[15:05]** there are violations of rules in your

**[15:05]** there are violations of rules in your style guide or in your architecture

**[15:06]** style guide or in your architecture

**[15:06]** style guide or in your architecture documents, if there are details that are

**[15:08]** documents, if there are details that are

**[15:08]** documents, if there are details that are missing from the specs, if the specs

**[15:10]** missing from the specs, if the specs

**[15:10]** missing from the specs, if the specs aren't implemented, if they're not well

**[15:12]** aren't implemented, if they're not well

**[15:12]** aren't implemented, if they're not well tested, or whatever other custom things

**[15:15]** tested, or whatever other custom things

**[15:15]** tested, or whatever other custom things that you want to check for. One of the

**[15:17]** that you want to check for. One of the

**[15:17]** that you want to check for. One of the things that we're trying to enable in

**[15:18]** things that we're trying to enable in

**[15:18]** things that we're trying to enable in Sculptor is for people to extend the

**[15:19]** Sculptor is for people to extend the

**[15:19]** Sculptor is for people to extend the checks that we have so that they can add

**[15:21]** checks that we have so that they can add

**[15:21]** checks that we have so that they can add their own types of best practices into

**[15:24]** their own types of best practices into

**[15:24]** their own types of best practices into the codebase and make sure that they are

**[15:26]** the codebase and make sure that they are

**[15:26]** the codebase and make sure that they are continually checked.

**[15:33]** After you've found issues, then you have

**[15:33]** After you've found issues, then you have to fix them. Very little of this talk is

**[15:35]** to fix them. Very little of this talk is

**[15:35]** to fix them. Very little of this talk is about fixing the issues because it ends

**[15:37]** about fixing the issues because it ends

**[15:37]** about fixing the issues because it ends up being a lot easier for the systems to

**[15:39]** up being a lot easier for the systems to

**[15:40]** up being a lot easier for the systems to fix issues than you would expect. I

**[15:42]** fix issues than you would expect. I

**[15:42]** fix issues than you would expect. I think this quote captures it relatively

**[15:44]** think this quote captures it relatively

**[15:44]** think this quote captures it relatively well. And a problem wellstated is

**[15:46]** well. And a problem wellstated is

**[15:46]** well. And a problem wellstated is halfsolved. What this means is that if

**[15:49]** halfsolved. What this means is that if

**[15:49]** halfsolved. What this means is that if you really understand what went wrong,

**[15:51]** you really understand what went wrong,

**[15:51]** you really understand what went wrong, then it's much easier to solve the

**[15:53]** then it's much easier to solve the

**[15:53]** then it's much easier to solve the problem. This is especially true for

**[15:55]** problem. This is especially true for

**[15:55]** problem. This is especially true for coding agents because the really simple

**[15:58]** coding agents because the really simple

**[15:58]** coding agents because the really simple strategies work really well. So even


### [16:00 - 17:00]

**[16:00]** strategies work really well. So even

**[16:00]** strategies work really well. So even just try multiple times, try a hund

**[16:03]** just try multiple times, try a hund

**[16:03]** just try multiple times, try a hund times with a different agent, it

**[16:05]** times with a different agent, it

**[16:05]** times with a different agent, it actually ends up like working out quite

**[16:07]** actually ends up like working out quite

**[16:07]** actually ends up like working out quite well. And one of the things that enables

**[16:09]** well. And one of the things that enables

**[16:09]** well. And one of the things that enables this is having really good sandboxing.

**[16:12]** this is having really good sandboxing.

**[16:12]** this is having really good sandboxing. If you have agents that can run safely,

**[16:14]** If you have agents that can run safely,

**[16:14]** If you have agents that can run safely, then you can run an almost unlimited

**[16:15]** then you can run an almost unlimited

**[16:15]** then you can run an almost unlimited number subject to cost constraints uh in

**[16:19]** number subject to cost constraints uh in

**[16:19]** number subject to cost constraints uh in parallel. And then if any one of them

**[16:21]** parallel. And then if any one of them

**[16:21]** parallel. And then if any one of them succeeds, then you can use that

**[16:22]** succeeds, then you can use that

**[16:22]** succeeds, then you can use that solution.

**[16:24]** solution.

**[16:24]** solution. And this is really just the beginning.

**[16:27]** And this is really just the beginning.

**[16:27]** And this is really just the beginning. There are going to be so many more tools

**[16:29]** There are going to be so many more tools

**[16:29]** There are going to be so many more tools that are released over the next year or

**[16:31]** that are released over the next year or

**[16:31]** that are released over the next year or two and many of the people in this room

**[16:33]** two and many of the people in this room

**[16:33]** two and many of the people in this room are working on those tools. There will

**[16:35]** are working on those tools. There will

**[16:35]** are working on those tools. There will be things that are not just for writing

**[16:37]** be things that are not just for writing

**[16:37]** be things that are not just for writing code like we've been talking about, but

**[16:39]** code like we've been talking about, but

**[16:39]** code like we've been talking about, but for after deployment, for debugging,

**[16:41]** for after deployment, for debugging,

**[16:41]** for after deployment, for debugging, logging, tracing, profiling, etc. There

**[16:44]** logging, tracing, profiling, etc. There

**[16:44]** logging, tracing, profiling, etc. There are tools for doing automated quality

**[16:47]** are tools for doing automated quality

**[16:47]** are tools for doing automated quality assurance where you can have an AI

**[16:48]** assurance where you can have an AI

**[16:48]** assurance where you can have an AI system click around on your website and

**[16:50]** system click around on your website and

**[16:50]** system click around on your website and check if it can actually do the thing

**[16:52]** check if it can actually do the thing

**[16:52]** check if it can actually do the thing that you want the user to do. There are

**[16:54]** that you want the user to do. There are

**[16:54]** that you want the user to do. There are tools for generating code from visual

**[16:56]** tools for generating code from visual

**[16:56]** tools for generating code from visual designs. There are tons of de dev tools

**[16:59]** designs. There are tons of de dev tools

**[16:59]** designs. There are tons of de dev tools coming out every week. you will have


### [17:00 - 18:00]

**[17:01]** coming out every week. you will have

**[17:01]** coming out every week. you will have much better contextual search systems

**[17:03]** much better contextual search systems

**[17:03]** much better contextual search systems that are useful for both you and for the

**[17:05]** that are useful for both you and for the

**[17:05]** that are useful for both you and for the agent. Uh and of course we'll get better

**[17:07]** agent. Uh and of course we'll get better

**[17:07]** agent. Uh and of course we'll get better AI based models as well. If anyone is

**[17:10]** AI based models as well. If anyone is

**[17:10]** AI based models as well. If anyone is working on these other sorts of tools

**[17:13]** working on these other sorts of tools

**[17:13]** working on these other sorts of tools that that are kind of adjacent to

**[17:16]** that that are kind of adjacent to

**[17:16]** that that are kind of adjacent to developer experience and helping you fix

**[17:18]** developer experience and helping you fix

**[17:18]** developer experience and helping you fix this like much smaller piece of the

**[17:20]** this like much smaller piece of the

**[17:20]** this like much smaller piece of the process, we would love to work together

**[17:21]** process, we would love to work together

**[17:21]** process, we would love to work together and find out a way to integrate that

**[17:23]** and find out a way to integrate that

**[17:23]** and find out a way to integrate that into Sculptor so that people can take

**[17:25]** into Sculptor so that people can take

**[17:25]** into Sculptor so that people can take advantage of that. I think what we'll

**[17:26]** advantage of that. I think what we'll

**[17:26]** advantage of that. I think what we'll see over the next year or two is that

**[17:28]** see over the next year or two is that

**[17:28]** see over the next year or two is that most of these things will be accessible.

**[17:30]** most of these things will be accessible.

**[17:30]** most of these things will be accessible. Uh, and it'll make the development

**[17:32]** Uh, and it'll make the development

**[17:32]** Uh, and it'll make the development experience just a lot easier once all

**[17:34]** experience just a lot easier once all

**[17:34]** experience just a lot easier once all these things are working together.

**[17:37]** these things are working together.

**[17:37]** these things are working together. So, that's pretty much all that I have

**[17:38]** So, that's pretty much all that I have

**[17:38]** So, that's pretty much all that I have for today. If you're interested, feel

**[17:40]** for today. If you're interested, feel

**[17:40]** for today. If you're interested, feel free to take a look at the QR code, go

**[17:42]** free to take a look at the QR code, go

**[17:42]** free to take a look at the QR code, go to our website at imbue.com and sign up

**[17:44]** to our website at imbue.com and sign up

**[17:44]** to our website at imbue.com and sign up to try out Sculptor. And of course, if

**[17:47]** to try out Sculptor. And of course, if

**[17:47]** to try out Sculptor. And of course, if you're interested in working on things

**[17:48]** you're interested in working on things

**[17:48]** you're interested in working on things like this, we're always hiring. We're

**[17:49]** like this, we're always hiring. We're

**[17:49]** like this, we're always hiring. We're always happy to chat, so feel free to

**[17:51]** always happy to chat, so feel free to

**[17:51]** always happy to chat, so feel free to reach out. Thank you.

**[17:54]** reach out. Thank you.

**[17:54]** reach out. Thank you. [Music]


