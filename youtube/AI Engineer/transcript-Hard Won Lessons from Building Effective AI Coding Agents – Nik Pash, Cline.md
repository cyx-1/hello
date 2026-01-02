# Hard Won Lessons from Building Effective AI Coding Agents – Nik Pash, Cline

**Video URL:** https://www.youtube.com/watch?v=I8fs4omN1no

---

## Full Transcript

### [00:00 - 01:00]

**[00:24]** Wow, it's wild to be on the same stage

**[00:24]** Wow, it's wild to be on the same stage as so many people I've drawn inspiration

**[00:25]** as so many people I've drawn inspiration

**[00:25]** as so many people I've drawn inspiration from. Let's dive into it. My name is

**[00:28]** from. Let's dive into it. My name is

**[00:28]** from. Let's dive into it. My name is Nick. I'm the head of AI at Klein and

**[00:30]** Nick. I'm the head of AI at Klein and

**[00:30]** Nick. I'm the head of AI at Klein and today I'm going to share some lessons we

**[00:32]** today I'm going to share some lessons we

**[00:32]** today I'm going to share some lessons we learned along the way.

**[00:34]** learned along the way.

**[00:34]** learned along the way. So let's start with the bitter truth.

**[00:37]** So let's start with the bitter truth.

**[00:37]** So let's start with the bitter truth. For years we compensated for weak models

**[00:40]** For years we compensated for weak models

**[00:40]** For years we compensated for weak models by building clever scaffolds around

**[00:42]** by building clever scaffolds around

**[00:42]** by building clever scaffolds around them. All kinds of clever ideas like rag

**[00:45]** them. All kinds of clever ideas like rag

**[00:45]** them. All kinds of clever ideas like rag indexing systems, search trees, tool

**[00:48]** indexing systems, search trees, tool

**[00:48]** indexing systems, search trees, tool calling scaffolds, all this was invented

**[00:50]** calling scaffolds, all this was invented

**[00:50]** calling scaffolds, all this was invented to cope with weaker models. And Frontier

**[00:54]** to cope with weaker models. And Frontier

**[00:54]** to cope with weaker models. And Frontier models simply bulldoze those

**[00:55]** models simply bulldoze those

**[00:55]** models simply bulldoze those abstractions. Now, you don't really need

**[00:58]** abstractions. Now, you don't really need

**[00:58]** abstractions. Now, you don't really need your scaffolding anymore. Your

**[00:59]** your scaffolding anymore. Your

**[00:59]** your scaffolding anymore. Your scaffolding just gets in the way of


### [01:00 - 02:00]

**[01:01]** scaffolding just gets in the way of

**[01:01]** scaffolding just gets in the way of these models. And the question really

**[01:03]** these models. And the question really

**[01:03]** these models. And the question really isn't how fancy is your agent stack.

**[01:07]** isn't how fancy is your agent stack.

**[01:07]** isn't how fancy is your agent stack. Increasingly, it's how strong is the

**[01:08]** Increasingly, it's how strong is the

**[01:08]** Increasingly, it's how strong is the model driving it.

**[01:11]** model driving it.

**[01:11]** model driving it. And the lesson here is relentless. Um, a

**[01:14]** And the lesson here is relentless. Um, a

**[01:14]** And the lesson here is relentless. Um, a perfect example of what I'm talking

**[01:15]** perfect example of what I'm talking

**[01:15]** perfect example of what I'm talking about is Gemini 3.0 released this week

**[01:19]** about is Gemini 3.0 released this week

**[01:19]** about is Gemini 3.0 released this week and it immediately dominated terminal

**[01:21]** and it immediately dominated terminal

**[01:21]** and it immediately dominated terminal bench leaderboards with no aentic

**[01:24]** bench leaderboards with no aentic

**[01:24]** bench leaderboards with no aentic harness supporting it at all. In this

**[01:26]** harness supporting it at all. In this

**[01:26]** harness supporting it at all. In this chart, you can see Gemini 3.0 on

**[01:28]** chart, you can see Gemini 3.0 on

**[01:28]** chart, you can see Gemini 3.0 on Terminus scored better than the vast

**[01:30]** Terminus scored better than the vast

**[01:30]** Terminus scored better than the vast majority of model agent combinations in

**[01:32]** majority of model agent combinations in

**[01:32]** majority of model agent combinations in the world all out of the box. And what's

**[01:35]** the world all out of the box. And what's

**[01:35]** the world all out of the box. And what's remarkable is that Terminus is designed

**[01:37]** remarkable is that Terminus is designed

**[01:37]** remarkable is that Terminus is designed to be an unopinionated generic stripped

**[01:40]** to be an unopinionated generic stripped

**[01:40]** to be an unopinionated generic stripped down harness. And it has no graph

**[01:42]** down harness. And it has no graph

**[01:42]** down harness. And it has no graph search, no rag, no indexing, just here's

**[01:45]** search, no rag, no indexing, just here's

**[01:45]** search, no rag, no indexing, just here's a terminal, go figure it out. And it

**[01:48]** a terminal, go figure it out. And it

**[01:48]** a terminal, go figure it out. And it crushes. The whole point of terminus is

**[01:50]** crushes. The whole point of terminus is

**[01:50]** crushes. The whole point of terminus is that it has no clever tool calling, no

**[01:53]** that it has no clever tool calling, no

**[01:53]** that it has no clever tool calling, no context engineering features. So the

**[01:55]** context engineering features. So the

**[01:55]** context engineering features. So the takeaway here is that capability beats

**[01:58]** takeaway here is that capability beats

**[01:58]** takeaway here is that capability beats scaffolding. If you get out of the

**[01:59]** scaffolding. If you get out of the

**[01:59]** scaffolding. If you get out of the model's way, it will perform just fine.


### [02:00 - 03:00]

**[02:03]** model's way, it will perform just fine.

**[02:03]** model's way, it will perform just fine. So really what I'm driving at and the

**[02:06]** So really what I'm driving at and the

**[02:06]** So really what I'm driving at and the key takeaway from this whole talk is if

**[02:08]** key takeaway from this whole talk is if

**[02:08]** key takeaway from this whole talk is if you're building agents, just relax. Cool

**[02:12]** you're building agents, just relax. Cool

**[02:12]** you're building agents, just relax. Cool it with all your clever engineering

**[02:14]** it with all your clever engineering

**[02:14]** it with all your clever engineering tricks. Stop overthinking it. That's it.

**[02:17]** tricks. Stop overthinking it. That's it.

**[02:17]** tricks. Stop overthinking it. That's it. That's the lesson. And another point on

**[02:21]** That's the lesson. And another point on

**[02:21]** That's the lesson. And another point on this, kind of like an aside, is I don't

**[02:23]** this, kind of like an aside, is I don't

**[02:23]** this, kind of like an aside, is I don't know about you guys, but we're all on

**[02:26]** know about you guys, but we're all on

**[02:26]** know about you guys, but we're all on Twitter. I'm on Twitter, and at this

**[02:29]** Twitter. I'm on Twitter, and at this

**[02:29]** Twitter. I'm on Twitter, and at this point, I just think talking about these

**[02:31]** point, I just think talking about these

**[02:31]** point, I just think talking about these like clever little context tricks and

**[02:34]** like clever little context tricks and

**[02:34]** like clever little context tricks and and hacks is a little played out. Like,

**[02:37]** and hacks is a little played out. Like,

**[02:37]** and hacks is a little played out. Like, at this point, I'm straight up tired of

**[02:39]** at this point, I'm straight up tired of

**[02:39]** at this point, I'm straight up tired of seeing some of this stuff. And like, I

**[02:42]** seeing some of this stuff. And like, I

**[02:42]** seeing some of this stuff. And like, I get it. it's free engagement and we all,

**[02:44]** get it. it's free engagement and we all,

**[02:44]** get it. it's free engagement and we all, you know, indulge in it a little bit.

**[02:45]** you know, indulge in it a little bit.

**[02:45]** you know, indulge in it a little bit. But personally, I think there's not

**[02:48]** But personally, I think there's not

**[02:48]** But personally, I think there's not really much signal there.

**[02:50]** really much signal there.

**[02:50]** really much signal there. So, if you want the full playbook for

**[02:53]** So, if you want the full playbook for

**[02:53]** So, if you want the full playbook for building an effective coding agent, like

**[02:56]** building an effective coding agent, like

**[02:56]** building an effective coding agent, like the playbook's right here. It's up on

**[02:58]** the playbook's right here. It's up on

**[02:58]** the playbook's right here. It's up on the screen. Um, there's really some


### [03:00 - 04:00]

**[03:00]** the screen. Um, there's really some

**[03:00]** the screen. Um, there's really some novelty talking about it like months

**[03:01]** novelty talking about it like months

**[03:02]** novelty talking about it like months ago, but at this point, in my opinion,

**[03:04]** ago, but at this point, in my opinion,

**[03:04]** ago, but at this point, in my opinion, it's been done to death. And we've been

**[03:06]** it's been done to death. And we've been

**[03:06]** it's been done to death. And we've been in this, you know, we're model agnostic

**[03:07]** in this, you know, we're model agnostic

**[03:07]** in this, you know, we're model agnostic at Klein. We support all the models.

**[03:09]** at Klein. We support all the models.

**[03:09]** at Klein. We support all the models. Every two weeks there's a new big model

**[03:12]** Every two weeks there's a new big model

**[03:12]** Every two weeks there's a new big model release going out and we've basically

**[03:15]** release going out and we've basically

**[03:15]** release going out and we've basically come down to the same playbook of

**[03:16]** come down to the same playbook of

**[03:16]** come down to the same playbook of supporting each model as it comes out.

**[03:19]** supporting each model as it comes out.

**[03:19]** supporting each model as it comes out. So I'm sure everyone here knows how to

**[03:21]** So I'm sure everyone here knows how to

**[03:21]** So I'm sure everyone here knows how to tune an agent from Sonnet 4 to Sonnet

**[03:24]** tune an agent from Sonnet 4 to Sonnet

**[03:24]** tune an agent from Sonnet 4 to Sonnet 4.5, from Gemini 2.5 to Gemini 3 and GBT

**[03:29]** 4.5, from Gemini 2.5 to Gemini 3 and GBT

**[03:30]** 4.5, from Gemini 2.5 to Gemini 3 and GBT 5 to GP GBT 5.1. I feel like this entire

**[03:34]** 5 to GP GBT 5.1. I feel like this entire

**[03:34]** 5 to GP GBT 5.1. I feel like this entire conversation is a little played out. So,

**[03:36]** conversation is a little played out. So,

**[03:36]** conversation is a little played out. So, I'm not really even going to cover this

**[03:37]** I'm not really even going to cover this

**[03:37]** I'm not really even going to cover this in depth because the tweaks here are

**[03:40]** in depth because the tweaks here are

**[03:40]** in depth because the tweaks here are trivial and the gains are marginal.

**[03:43]** trivial and the gains are marginal.

**[03:43]** trivial and the gains are marginal. So, what I really want to talk about is

**[03:46]** So, what I really want to talk about is

**[03:46]** So, what I really want to talk about is something that's not actually given a

**[03:48]** something that's not actually given a

**[03:48]** something that's not actually given a lot of attention and it's the real

**[03:50]** lot of attention and it's the real

**[03:50]** lot of attention and it's the real bottleneck. And the real bottleneck is

**[03:52]** bottleneck. And the real bottleneck is

**[03:52]** bottleneck. And the real bottleneck is that you can build the cleanest agent in

**[03:54]** that you can build the cleanest agent in

**[03:54]** that you can build the cleanest agent in the world, but that doesn't improve

**[03:56]** the world, but that doesn't improve

**[03:56]** the world, but that doesn't improve model capability by even 1%. Models only


### [04:00 - 05:00]

**[04:00]** model capability by even 1%. Models only

**[04:00]** model capability by even 1%. Models only get better when labs train on something

**[04:03]** get better when labs train on something

**[04:03]** get better when labs train on something hard. And benchmarks, not agent

**[04:07]** hard. And benchmarks, not agent

**[04:07]** hard. And benchmarks, not agent cleverness, not all your clever

**[04:08]** cleverness, not all your clever

**[04:08]** cleverness, not all your clever engineering techniques, not your clever

**[04:10]** engineering techniques, not your clever

**[04:10]** engineering techniques, not your clever rag pipelines. It's benchmarks that

**[04:12]** rag pipelines. It's benchmarks that

**[04:12]** rag pipelines. It's benchmarks that determine what frontier models learn to

**[04:15]** determine what frontier models learn to

**[04:15]** determine what frontier models learn to do next. And models didn't magically get

**[04:18]** do next. And models didn't magically get

**[04:18]** do next. And models didn't magically get better at tool use.

**[04:21]** better at tool use.

**[04:21]** better at tool use. They got better because people built RL

**[04:23]** They got better because people built RL

**[04:23]** They got better because people built RL environments that forced them to

**[04:25]** environments that forced them to

**[04:25]** environments that forced them to practice certain actions. handling

**[04:28]** practice certain actions. handling

**[04:28]** practice certain actions. handling failure more handling failure modes

**[04:30]** failure more handling failure modes

**[04:30]** failure more handling failure modes retrying and for example like agents

**[04:33]** retrying and for example like agents

**[04:33]** retrying and for example like agents improve only when the model learns

**[04:35]** improve only when the model learns

**[04:35]** improve only when the model learns inside the right environment every jump

**[04:37]** inside the right environment every jump

**[04:37]** inside the right environment every jump in reasoning we've seen came from a

**[04:39]** in reasoning we've seen came from a

**[04:39]** in reasoning we've seen came from a benchmark every jump in agent

**[04:41]** benchmark every jump in agent

**[04:41]** benchmark every jump in agent reliability came from an RL environment

**[04:44]** reliability came from an RL environment

**[04:44]** reliability came from an RL environment so the real questions become what is a

**[04:47]** so the real questions become what is a

**[04:47]** so the real questions become what is a benchmark how do you turn real world

**[04:51]** benchmark how do you turn real world

**[04:51]** benchmark how do you turn real world agent coding data into an RL environment

**[04:54]** agent coding data into an RL environment

**[04:54]** agent coding data into an RL environment and what makes a good verifier how do

**[04:56]** and what makes a good verifier how do

**[04:56]** and what makes a good verifier how do you detect [clears throat] real

**[04:57]** you detect [clears throat] real

**[04:57]** you detect [clears throat] real difficult ulty and how do you train

**[04:58]** difficult ulty and how do you train

**[04:58]** difficult ulty and how do you train these models to work on the problems


### [05:00 - 06:00]

**[05:00]** these models to work on the problems

**[05:00]** these models to work on the problems that we actually care about as

**[05:01]** that we actually care about as

**[05:01]** that we actually care about as engineers? These are the questions that

**[05:04]** engineers? These are the questions that

**[05:04]** engineers? These are the questions that matter for the next frontier.

**[05:07]** matter for the next frontier.

**[05:07]** matter for the next frontier. So what is a benchmark?

**[05:09]** So what is a benchmark?

**[05:09]** So what is a benchmark? A benchmark put simply it's an

**[05:11]** A benchmark put simply it's an

**[05:11]** A benchmark put simply it's an environment. It's a so in our case it's

**[05:14]** environment. It's a so in our case it's

**[05:14]** environment. It's a so in our case it's like a docker container where you let

**[05:15]** like a docker container where you let

**[05:15]** like a docker container where you let the agent run wild. It's a starting

**[05:18]** the agent run wild. It's a starting

**[05:18]** the agent run wild. It's a starting state which is the snapshot of the code

**[05:20]** state which is the snapshot of the code

**[05:20]** state which is the snapshot of the code when you started working on a real world

**[05:23]** when you started working on a real world

**[05:23]** when you started working on a real world coding task as well as a starting

**[05:25]** coding task as well as a starting

**[05:25]** coding task as well as a starting prompt. And the last thing is a verifier

**[05:28]** prompt. And the last thing is a verifier

**[05:28]** prompt. And the last thing is a verifier at the end that checks whether an end

**[05:30]** at the end that checks whether an end

**[05:30]** at the end that checks whether an end state is correct or acceptable.

**[05:33]** state is correct or acceptable.

**[05:33]** state is correct or acceptable. So how are RL environments different?

**[05:36]** So how are RL environments different?

**[05:36]** So how are RL environments different? [clears throat]

**[05:37]** [clears throat]

**[05:37]** [clears throat] Well, here's the thing. They're not

**[05:38]** Well, here's the thing. They're not

**[05:38]** Well, here's the thing. They're not really different at all. And you might

**[05:39]** really different at all. And you might

**[05:40]** really different at all. And you might notice this chart is basically the same

**[05:42]** notice this chart is basically the same

**[05:42]** notice this chart is basically the same thing as the previous slide. The only

**[05:44]** thing as the previous slide. The only

**[05:44]** thing as the previous slide. The only real difference, the only distinction

**[05:46]** real difference, the only distinction

**[05:46]** real difference, the only distinction here is how the reward is used.

**[05:49]** here is how the reward is used.

**[05:49]** here is how the reward is used. Benchmarks measure models. RL

**[05:52]** Benchmarks measure models. RL

**[05:52]** Benchmarks measure models. RL environments improve models. The score

**[05:55]** environments improve models. The score

**[05:55]** environments improve models. The score doesn't just stop in a leaderboard where

**[05:57]** doesn't just stop in a leaderboard where

**[05:57]** doesn't just stop in a leaderboard where you publish the results. The score is

**[05:59]** you publish the results. The score is

**[05:59]** you publish the results. The score is actually used to update the weights of


### [06:00 - 07:00]

**[06:01]** actually used to update the weights of

**[06:01]** actually used to update the weights of the policy model.

**[06:03]** the policy model.

**[06:03]** the policy model. So, how do you transform real world

**[06:06]** So, how do you transform real world

**[06:06]** So, how do you transform real world coding data into useful RL environments

**[06:10]** coding data into useful RL environments

**[06:10]** coding data into useful RL environments for training?

**[06:12]** for training?

**[06:12]** for training? At Klein, we created the system called

**[06:15]** At Klein, we created the system called

**[06:15]** At Klein, we created the system called an RL environments factory. Looking for

**[06:18]** an RL environments factory. Looking for

**[06:18]** an RL environments factory. Looking for a better name there, but that's what we

**[06:20]** a better name there, but that's what we

**[06:20]** a better name there, but that's what we got so far. And the first phase in this

**[06:23]** got so far. And the first phase in this

**[06:23]** got so far. And the first phase in this pipeline is you get sub agents and you

**[06:26]** pipeline is you get sub agents and you

**[06:26]** pipeline is you get sub agents and you have them qualify tasks. And these sub

**[06:29]** have them qualify tasks. And these sub

**[06:29]** have them qualify tasks. And these sub agents, they work in parallel to decide

**[06:31]** agents, they work in parallel to decide

**[06:31]** agents, they work in parallel to decide whether or not given tasks are suitable

**[06:33]** whether or not given tasks are suitable

**[06:33]** whether or not given tasks are suitable to be turned into RL environments for

**[06:35]** to be turned into RL environments for

**[06:35]** to be turned into RL environments for the purpose of training.

**[06:37]** the purpose of training.

**[06:37]** the purpose of training. And the qualification process goes as

**[06:40]** And the qualification process goes as

**[06:40]** And the qualification process goes as follows. So you have you start with

**[06:41]** follows. So you have you start with

**[06:41]** follows. So you have you start with origins. So you have to validate does

**[06:43]** origins. So you have to validate does

**[06:43]** origins. So you have to validate does the repository actually exist. Is the

**[06:46]** the repository actually exist. Is the

**[06:46]** the repository actually exist. Is the starting commit accessible? Is it open

**[06:48]** starting commit accessible? Is it open

**[06:48]** starting commit accessible? Is it open source? The journey where you look at

**[06:52]** source? The journey where you look at

**[06:52]** source? The journey where you look at the starting prompt, the other follow-on

**[06:54]** the starting prompt, the other follow-on

**[06:54]** the starting prompt, the other follow-on prompts that the user might have

**[06:57]** prompts that the user might have

**[06:57]** prompts that the user might have followed up with with the agent. You

**[06:59]** followed up with with the agent. You

**[06:59]** followed up with with the agent. You have to try to understand what was the


### [07:00 - 08:00]

**[07:01]** have to try to understand what was the

**[07:01]** have to try to understand what was the user actually trying to accomplish, what

**[07:02]** user actually trying to accomplish, what

**[07:02]** user actually trying to accomplish, what was the spirit of their task. And

**[07:05]** was the spirit of their task. And

**[07:05]** was the spirit of their task. And lastly, it's the outcome. So, can we

**[07:08]** lastly, it's the outcome. So, can we

**[07:08]** lastly, it's the outcome. So, can we find the actual commits or PRs that fix

**[07:11]** find the actual commits or PRs that fix

**[07:11]** find the actual commits or PRs that fix the problem in real life? Like, did they

**[07:13]** the problem in real life? Like, did they

**[07:13]** the problem in real life? Like, did they actually commit the solution to their

**[07:15]** actually commit the solution to their

**[07:15]** actually commit the solution to their problem later on in the timeline? And

**[07:18]** problem later on in the timeline? And

**[07:18]** problem later on in the timeline? And we're actively looking for easy

**[07:20]** we're actively looking for easy

**[07:20]** we're actively looking for easy disqualifiers as part of this. So,

**[07:22]** disqualifiers as part of this. So,

**[07:22]** disqualifiers as part of this. So, things like vibecoded slop, we don't

**[07:23]** things like vibecoded slop, we don't

**[07:24]** things like vibecoded slop, we don't need another benchmark that tests for,

**[07:26]** need another benchmark that tests for,

**[07:26]** need another benchmark that tests for, you know, build the next.js app uh from

**[07:28]** you know, build the next.js app uh from

**[07:28]** you know, build the next.js app uh from scratch. We're looking we're looking to

**[07:31]** scratch. We're looking we're looking to

**[07:31]** scratch. We're looking we're looking to disqualify trivial tasks that are too

**[07:33]** disqualify trivial tasks that are too

**[07:33]** disqualify trivial tasks that are too easy and tasks that have no reliable

**[07:36]** easy and tasks that have no reliable

**[07:36]** easy and tasks that have no reliable start or end states.

**[07:38]** start or end states.

**[07:38]** start or end states. And lastly, what makes a good RL

**[07:40]** And lastly, what makes a good RL

**[07:40]** And lastly, what makes a good RL environment good? How do we actually

**[07:42]** environment good? How do we actually

**[07:42]** environment good? How do we actually make an RL environment and what makes a

**[07:44]** make an RL environment and what makes a

**[07:44]** make an RL environment and what makes a good test or verifier?

**[07:47]** good test or verifier?

**[07:47]** good test or verifier? So phase two of this pipeline is

**[07:49]** So phase two of this pipeline is

**[07:49]** So phase two of this pipeline is building the actual RL environment. So

**[07:52]** building the actual RL environment. So

**[07:52]** building the actual RL environment. So you start out with archaeology where you

**[07:54]** you start out with archaeology where you

**[07:54]** you start out with archaeology where you actually reconstruct both states

**[07:56]** actually reconstruct both states

**[07:56]** actually reconstruct both states locally. You pull down the code, you see

**[07:58]** locally. You pull down the code, you see

**[07:58]** locally. You pull down the code, you see if you can implement it yourself,


### [08:00 - 09:00]

**[08:01]** if you can implement it yourself,

**[08:01]** if you can implement it yourself, reconstruct it, build it, and verify

**[08:03]** reconstruct it, build it, and verify

**[08:03]** reconstruct it, build it, and verify that the bug that the user was

**[08:05]** that the bug that the user was

**[08:05]** that the bug that the user was referencing and the solution actually

**[08:07]** referencing and the solution actually

**[08:07]** referencing and the solution actually exists. You document every obstacle and

**[08:10]** exists. You document every obstacle and

**[08:10]** exists. You document every obstacle and dependency. You containerize it with

**[08:12]** dependency. You containerize it with

**[08:12]** dependency. You containerize it with Docker, removing Git obviously, so

**[08:15]** Docker, removing Git obviously, so

**[08:15]** Docker, removing Git obviously, so agents can't reward hack. And lastly,

**[08:17]** agents can't reward hack. And lastly,

**[08:17]** agents can't reward hack. And lastly, you define the verifier at the end. And

**[08:19]** you define the verifier at the end. And

**[08:19]** you define the verifier at the end. And this is where it gets into like a little

**[08:21]** this is where it gets into like a little

**[08:21]** this is where it gets into like a little bit of the art of building a good

**[08:24]** bit of the art of building a good

**[08:24]** bit of the art of building a good verifier. And I want to talk about this

**[08:25]** verifier. And I want to talk about this

**[08:26]** verifier. And I want to talk about this because the analogy that I typically

**[08:28]** because the analogy that I typically

**[08:28]** because the analogy that I typically give is a teac kettle. So let's say the

**[08:33]** give is a teac kettle. So let's say the

**[08:33]** give is a teac kettle. So let's say the user's goal is I want to boil water.

**[08:36]** user's goal is I want to boil water.

**[08:36]** user's goal is I want to boil water. A really good example of a verifier to

**[08:38]** A really good example of a verifier to

**[08:38]** A really good example of a verifier to test whether or not the water is boiling

**[08:41]** test whether or not the water is boiling

**[08:41]** test whether or not the water is boiling is a little whistle attachment that goes

**[08:43]** is a little whistle attachment that goes

**[08:43]** is a little whistle attachment that goes inside your teac kettle. And the whistle

**[08:46]** inside your teac kettle. And the whistle

**[08:46]** inside your teac kettle. And the whistle is a pure outcome verification. And it's

**[08:48]** is a pure outcome verification. And it's

**[08:48]** is a pure outcome verification. And it's an example of a pure outcome driven

**[08:51]** an example of a pure outcome driven

**[08:51]** an example of a pure outcome driven verifier where the water either reached

**[08:54]** verifier where the water either reached

**[08:54]** verifier where the water either reached the boiling point or it didn't. Either

**[08:56]** the boiling point or it didn't. Either

**[08:56]** the boiling point or it didn't. Either it's whistling or it's not. The kettle

**[08:58]** it's whistling or it's not. The kettle

**[08:58]** it's whistling or it's not. The kettle doesn't care how you achieved it,


### [09:00 - 10:00]

**[09:00]** doesn't care how you achieved it,

**[09:00]** doesn't care how you achieved it, whether you used a gas stove, an

**[09:02]** whether you used a gas stove, an

**[09:02]** whether you used a gas stove, an electric induction stove, or a campfire.

**[09:04]** electric induction stove, or a campfire.

**[09:04]** electric induction stove, or a campfire. It just signals the result. And in the

**[09:07]** It just signals the result. And in the

**[09:07]** It just signals the result. And in the process of doing this, all these weird

**[09:09]** process of doing this, all these weird

**[09:09]** process of doing this, all these weird bad tests can emerge. So you might have

**[09:12]** bad tests can emerge. So you might have

**[09:12]** bad tests can emerge. So you might have noticed like that the sub agent might

**[09:14]** noticed like that the sub agent might

**[09:14]** noticed like that the sub agent might have noticed like oh in the ground truth

**[09:16]** have noticed like oh in the ground truth

**[09:16]** have noticed like oh in the ground truth solution like in a previous run the

**[09:18]** solution like in a previous run the

**[09:18]** solution like in a previous run the burner was set to high so maybe we

**[09:20]** burner was set to high so maybe we

**[09:20]** burner was set to high so maybe we should be checking for that but we all

**[09:22]** should be checking for that but we all

**[09:22]** should be checking for that but we all know that water can boil at a low

**[09:24]** know that water can boil at a low

**[09:24]** know that water can boil at a low setting on the burner or was it on the

**[09:27]** setting on the burner or was it on the

**[09:27]** setting on the burner or was it on the front left burner has 5 minutes elapsed

**[09:29]** front left burner has 5 minutes elapsed

**[09:29]** front left burner has 5 minutes elapsed like all kinds of weird bad tests and

**[09:30]** like all kinds of weird bad tests and

**[09:30]** like all kinds of weird bad tests and the key point here is don't

**[09:34]** the key point here is don't

**[09:34]** the key point here is don't overprescribe based on the ground truth

**[09:36]** overprescribe based on the ground truth

**[09:36]** overprescribe based on the ground truth test for the spirit of the task test for

**[09:39]** test for the spirit of the task test for

**[09:39]** test for the spirit of the task test for the outcome of the task.

**[09:41]** the outcome of the task.

**[09:41]** the outcome of the task. And the outcome at the end of all this

**[09:43]** And the outcome at the end of all this

**[09:43]** And the outcome at the end of all this is a containerized benchmark or

**[09:46]** is a containerized benchmark or

**[09:46]** is a containerized benchmark or environment for that task. Agent work is

**[09:49]** environment for that task. Agent work is

**[09:49]** environment for that task. Agent work is recorded so you can see the traces the

**[09:51]** recorded so you can see the traces the

**[09:51]** recorded so you can see the traces the trajectory that the agent took to

**[09:52]** trajectory that the agent took to

**[09:52]** trajectory that the agent took to complete the task and you can reliably

**[09:55]** complete the task and you can reliably

**[09:55]** complete the task and you can reliably score it and verify it and it's fully

**[09:57]** score it and verify it and it's fully

**[09:57]** score it and verify it and it's fully portable. You can run it on any device.


### [10:00 - 11:00]

**[10:01]** portable. You can run it on any device.

**[10:01]** portable. You can run it on any device. So the path to automation that we've

**[10:04]** So the path to automation that we've

**[10:04]** So the path to automation that we've been undertaking as part of this is can

**[10:07]** been undertaking as part of this is can

**[10:07]** been undertaking as part of this is can we fully automate the process of

**[10:09]** we fully automate the process of

**[10:09]** we fully automate the process of converting real world coding data into

**[10:13]** converting real world coding data into

**[10:13]** converting real world coding data into RL environments for the purpose of

**[10:14]** RL environments for the purpose of

**[10:14]** RL environments for the purpose of training models.

**[10:16]** training models.

**[10:16]** training models. And this work largely started out manual

**[10:19]** And this work largely started out manual

**[10:19]** And this work largely started out manual but then the first time in the RL

**[10:21]** but then the first time in the RL

**[10:21]** but then the first time in the RL environment was like about 16 hours of

**[10:23]** environment was like about 16 hours of

**[10:23]** environment was like about 16 hours of my time. And what used to take 16 hours

**[10:25]** my time. And what used to take 16 hours

**[10:25]** my time. And what used to take 16 hours now takes less than 20 minutes per task.

**[10:29]** now takes less than 20 minutes per task.

**[10:29]** now takes less than 20 minutes per task. And we're building towards a fully

**[10:31]** And we're building towards a fully

**[10:31]** And we're building towards a fully automated RL environment factory where

**[10:32]** automated RL environment factory where

**[10:32]** automated RL environment factory where the bottleneck shifts from engineering

**[10:35]** the bottleneck shifts from engineering

**[10:35]** the bottleneck shifts from engineering to collecting high quality tasks. And an

**[10:38]** to collecting high quality tasks. And an

**[10:38]** to collecting high quality tasks. And an interesting kind of point here, the

**[10:40]** interesting kind of point here, the

**[10:40]** interesting kind of point here, the natural endpoint of all this is what if

**[10:43]** natural endpoint of all this is what if

**[10:44]** natural endpoint of all this is what if we actually built RL environments and

**[10:45]** we actually built RL environments and

**[10:46]** we actually built RL environments and this is like a question for everyone in

**[10:47]** this is like a question for everyone in

**[10:47]** this is like a question for everyone in the audience is what if we built RL

**[10:49]** the audience is what if we built RL

**[10:49]** the audience is what if we built RL environments to test how well agents can

**[10:51]** environments to test how well agents can

**[10:51]** environments to test how well agents can actually make RL environments kind of

**[10:53]** actually make RL environments kind of

**[10:53]** actually make RL environments kind of like a meta benchmark. What would hill

**[10:55]** like a meta benchmark. What would hill

**[10:55]** like a meta benchmark. What would hill climbing on that look like? And you can

**[10:58]** climbing on that look like? And you can

**[10:58]** climbing on that look like? And you can kind of start imagining that as models


### [11:00 - 12:00]

**[11:00]** kind of start imagining that as models

**[11:00]** kind of start imagining that as models get really really good at making their

**[11:02]** get really really good at making their

**[11:02]** get really really good at making their own RL environments to train on based on

**[11:04]** own RL environments to train on based on

**[11:04]** own RL environments to train on based on real world user data, you kind of

**[11:06]** real world user data, you kind of

**[11:06]** real world user data, you kind of complete that loop. Something to think

**[11:08]** complete that loop. Something to think

**[11:08]** complete that loop. Something to think about. So, okay. Um, this next part is

**[11:13]** about. So, okay. Um, this next part is

**[11:13]** about. So, okay. Um, this next part is the truth nuke. Um, also known as TRO.

**[11:17]** the truth nuke. Um, also known as TRO.

**[11:17]** the truth nuke. Um, also known as TRO. Um,

**[11:19]** Um,

**[11:19]** Um, an unspoken fact is that we're not alone

**[11:23]** an unspoken fact is that we're not alone

**[11:23]** an unspoken fact is that we're not alone at Klein building this kind of system.

**[11:26]** at Klein building this kind of system.

**[11:26]** at Klein building this kind of system. Every major agent lab captures this

**[11:29]** Every major agent lab captures this

**[11:29]** Every major agent lab captures this data. They all do some version of this

**[11:31]** data. They all do some version of this

**[11:31]** data. They all do some version of this behind the scenes, but no one really

**[11:32]** behind the scenes, but no one really

**[11:32]** behind the scenes, but no one really talks about it. And I don't even need to

**[11:35]** talks about it. And I don't even need to

**[11:36]** talks about it. And I don't even need to name them. If you know, you know. And

**[11:37]** name them. If you know, you know. And

**[11:37]** name them. If you know, you know. And realistically, you all know. These same

**[11:40]** realistically, you all know. These same

**[11:40]** realistically, you all know. These same companies site internal benchmarks to

**[11:43]** companies site internal benchmarks to

**[11:43]** companies site internal benchmarks to justify legacy systems that they spent

**[11:45]** justify legacy systems that they spent

**[11:46]** justify legacy systems that they spent months maintaining. But curiously,

**[11:48]** months maintaining. But curiously,

**[11:48]** months maintaining. But curiously, you'll never be able to study or inspect

**[11:49]** you'll never be able to study or inspect

**[11:49]** you'll never be able to study or inspect them because they don't publish them

**[11:51]** them because they don't publish them

**[11:51]** them because they don't publish them openly. And this data is so valuable yet

**[11:55]** openly. And this data is so valuable yet

**[11:55]** openly. And this data is so valuable yet no one shares it. It's the only thing

**[11:57]** no one shares it. It's the only thing

**[11:57]** no one shares it. It's the only thing that actually moves the needle.


### [12:00 - 13:00]

**[12:00]** that actually moves the needle.

**[12:00]** that actually moves the needle. And here's the heart of my argument is

**[12:03]** And here's the heart of my argument is

**[12:03]** And here's the heart of my argument is by standing between real world engineers

**[12:06]** by standing between real world engineers

**[12:06]** by standing between real world engineers working on real world tasks and the

**[12:08]** working on real world tasks and the

**[12:08]** working on real world tasks and the models agent labs have a unique role in

**[12:10]** models agent labs have a unique role in

**[12:10]** models agent labs have a unique role in history. We can build better prompts. We

**[12:12]** history. We can build better prompts. We

**[12:12]** history. We can build better prompts. We can build better tools. But none of that

**[12:14]** can build better tools. But none of that

**[12:14]** can build better tools. But none of that improves the underlying models. We

**[12:16]** improves the underlying models. We

**[12:16]** improves the underlying models. We possess the single richest data set of

**[12:19]** possess the single richest data set of

**[12:19]** possess the single richest data set of real engineering work anywhere in the

**[12:22]** real engineering work anywhere in the

**[12:22]** real engineering work anywhere in the world. Models don't improve without this

**[12:25]** world. Models don't improve without this

**[12:25]** world. Models don't improve without this data and keeping them closed is slowing

**[12:27]** data and keeping them closed is slowing

**[12:27]** data and keeping them closed is slowing down Frontier Research.

**[12:29]** down Frontier Research.

**[12:29]** down Frontier Research. So today we're announcing client bench.

**[12:32]** So today we're announcing client bench.

**[12:32]** So today we're announcing client bench. This is our attempt to finally create a

**[12:33]** This is our attempt to finally create a

**[12:33]** This is our attempt to finally create a benchmark that isn't cosplay

**[12:35]** benchmark that isn't cosplay

**[12:35]** benchmark that isn't cosplay engineering. It's not write me a server

**[12:38]** engineering. It's not write me a server

**[12:38]** engineering. It's not write me a server that generates Fibonacci sequences. This

**[12:40]** that generates Fibonacci sequences. This

**[12:40]** that generates Fibonacci sequences. This is real software development captured

**[12:43]** is real software development captured

**[12:43]** is real software development captured and packaged into standardized RL and

**[12:44]** and packaged into standardized RL and

**[12:44]** and packaged into standardized RL and inval and eval environments and this is

**[12:47]** inval and eval environments and this is

**[12:47]** inval and eval environments and this is the benchmark that we always wanted

**[12:49]** the benchmark that we always wanted

**[12:49]** the benchmark that we always wanted someone else to build. No one did. So

**[12:51]** someone else to build. No one did. So

**[12:51]** someone else to build. No one did. So we're doing it and anyone can

**[12:54]** we're doing it and anyone can

**[12:54]** we're doing it and anyone can participate. So here's how it works. The

**[12:57]** participate. So here's how it works. The

**[12:58]** participate. So here's how it works. The whole thing is open source. There's no

**[12:59]** whole thing is open source. There's no

**[12:59]** whole thing is open source. There's no secret sauce, no locked away data sets.


### [13:00 - 14:00]

**[13:03]** secret sauce, no locked away data sets.

**[13:03]** secret sauce, no locked away data sets. You can openly run it yourself and

**[13:05]** You can openly run it yourself and

**[13:05]** You can openly run it yourself and inspect it to see how it works. Anyone

**[13:07]** inspect it to see how it works. Anyone

**[13:07]** inspect it to see how it works. Anyone can use these environments for SFT, RL,

**[13:10]** can use these environments for SFT, RL,

**[13:10]** can use these environments for SFT, RL, eval, whatever. The point is is to just

**[13:12]** eval, whatever. The point is is to just

**[13:12]** eval, whatever. The point is is to just give the entire ecosystem a real

**[13:14]** give the entire ecosystem a real

**[13:14]** give the entire ecosystem a real substrate to measure and improve models

**[13:16]** substrate to measure and improve models

**[13:16]** substrate to measure and improve models on, not just leak code puzzles. And this

**[13:20]** on, not just leak code puzzles. And this

**[13:20]** on, not just leak code puzzles. And this only works if the community contributes.

**[13:22]** only works if the community contributes.

**[13:22]** only works if the community contributes. And the good news is you don't actually

**[13:23]** And the good news is you don't actually

**[13:24]** And the good news is you don't actually need to do anything special. Just work

**[13:26]** need to do anything special. Just work

**[13:26]** need to do anything special. Just work on your open source project with the

**[13:28]** on your open source project with the

**[13:28]** on your open source project with the client provider turned on and opt into

**[13:30]** client provider turned on and opt into

**[13:30]** client provider turned on and opt into the client bench initiative. If a

**[13:31]** the client bench initiative. If a

**[13:32]** the client bench initiative. If a frontier model gets stuck and you step

**[13:34]** frontier model gets stuck and you step

**[13:34]** frontier model gets stuck and you step in to fix it, that's actually a ideal

**[13:37]** in to fix it, that's actually a ideal

**[13:37]** in to fix it, that's actually a ideal task for to be a candidate for a

**[13:40]** task for to be a candidate for a

**[13:40]** task for to be a candidate for a benchmark and that's it. Just use the

**[13:43]** benchmark and that's it. Just use the

**[13:43]** benchmark and that's it. Just use the climb provider, see where the model

**[13:45]** climb provider, see where the model

**[13:45]** climb provider, see where the model struggles and we'll pick it up and

**[13:47]** struggles and we'll pick it up and

**[13:47]** struggles and we'll pick it up and introduce it into this open-source

**[13:49]** introduce it into this open-source

**[13:49]** introduce it into this open-source benchmark. So, client bench will always

**[13:52]** benchmark. So, client bench will always

**[13:52]** benchmark. So, client bench will always remain free, fully open source and

**[13:55]** remain free, fully open source and

**[13:55]** remain free, fully open source and freely accessible.

**[13:57]** freely accessible.

**[13:57]** freely accessible. Thank you all. If you want to

**[13:58]** Thank you all. If you want to

**[13:58]** Thank you all. If you want to contribute,


