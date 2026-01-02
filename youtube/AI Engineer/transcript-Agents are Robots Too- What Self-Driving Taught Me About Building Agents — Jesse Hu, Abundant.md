# Agents are Robots Too- What Self-Driving Taught Me About Building Agents — Jesse Hu, Abundant

**Video URL:** https://www.youtube.com/watch?v=qqXdLf3wy1E

---

## Full Transcript

### [00:00 - 01:00]

**[00:04]** All right. So this is my talk called

**[00:04]** All right. So this is my talk called Agents of Robots 2. I've given different

**[00:07]** Agents of Robots 2. I've given different

**[00:07]** Agents of Robots 2. I've given different variants of this talk in person for

**[00:10]** variants of this talk in person for

**[00:10]** variants of this talk in person for different events, but this is the first

**[00:11]** different events, but this is the first

**[00:11]** different events, but this is the first one that I've done for coding agents.

**[00:15]** one that I've done for coding agents.

**[00:15]** one that I've done for coding agents. So to kick things off, um just a little

**[00:17]** So to kick things off, um just a little

**[00:17]** So to kick things off, um just a little bit about me. I've been a lifelong ML

**[00:21]** bit about me. I've been a lifelong ML

**[00:21]** bit about me. I've been a lifelong ML engineer and I've worked at places like

**[00:22]** engineer and I've worked at places like

**[00:22]** engineer and I've worked at places like YouTube and Google where I worked on the

**[00:25]** YouTube and Google where I worked on the

**[00:25]** YouTube and Google where I worked on the two tower embedding model as well as

**[00:27]** two tower embedding model as well as

**[00:27]** two tower embedding model as well as some early work on BERT and mixture of

**[00:29]** some early work on BERT and mixture of

**[00:29]** some early work on BERT and mixture of experts.

**[00:31]** experts.

**[00:31]** experts. I worked on ML and robotics at Whimo

**[00:33]** I worked on ML and robotics at Whimo

**[00:34]** I worked on ML and robotics at Whimo where a lot of my focus was on the data

**[00:35]** where a lot of my focus was on the data

**[00:35]** where a lot of my focus was on the data side as well as reward modeling and

**[00:38]** side as well as reward modeling and

**[00:38]** side as well as reward modeling and evaluation.

**[00:40]** evaluation.

**[00:40]** evaluation. And most recently, I've been working on

**[00:42]** And most recently, I've been working on

**[00:42]** And most recently, I've been working on a company called Abundant, where we work

**[00:44]** a company called Abundant, where we work

**[00:44]** a company called Abundant, where we work on a lot of the same concepts applied to

**[00:47]** on a lot of the same concepts applied to

**[00:47]** on a lot of the same concepts applied to data sets for Foundation Model Labs and

**[00:50]** data sets for Foundation Model Labs and

**[00:50]** data sets for Foundation Model Labs and their training for agentic coding

**[00:52]** their training for agentic coding

**[00:52]** their training for agentic coding models.

**[00:55]** models.

**[00:55]** models. Um, none of this will cover any inside

**[00:58]** Um, none of this will cover any inside

**[00:58]** Um, none of this will cover any inside information about Whimo, but we'll


### [01:00 - 02:00]

**[01:00]** information about Whimo, but we'll

**[01:00]** information about Whimo, but we'll instead cover some general topics that

**[01:03]** instead cover some general topics that

**[01:04]** instead cover some general topics that are carried over from self-driving and

**[01:06]** are carried over from self-driving and

**[01:06]** are carried over from self-driving and robotics into digital agents.

**[01:11]** robotics into digital agents.

**[01:11]** robotics into digital agents. So I'll kick things off in kind of like

**[01:13]** So I'll kick things off in kind of like

**[01:13]** So I'll kick things off in kind of like talking about what some of the parallels

**[01:15]** talking about what some of the parallels

**[01:15]** talking about what some of the parallels are. And I think one of the main things

**[01:17]** are. And I think one of the main things

**[01:17]** are. And I think one of the main things is that you sort of have this 1% versus

**[01:20]** is that you sort of have this 1% versus

**[01:20]** is that you sort of have this 1% versus 99% problem where you think that the

**[01:23]** 99% problem where you think that the

**[01:23]** 99% problem where you think that the model is doing most of the work. But

**[01:25]** model is doing most of the work. But

**[01:25]** model is doing most of the work. But when you get into real world

**[01:27]** when you get into real world

**[01:27]** when you get into real world applications, the model is only doing 1%

**[01:29]** applications, the model is only doing 1%

**[01:29]** applications, the model is only doing 1% of the work and 99% of the work goes

**[01:31]** of the work and 99% of the work goes

**[01:31]** of the work and 99% of the work goes into other things. So in robotics you

**[01:33]** into other things. So in robotics you

**[01:33]** into other things. So in robotics you have the hardware and sensors and

**[01:35]** have the hardware and sensors and

**[01:35]** have the hardware and sensors and actuators you have integration

**[01:36]** actuators you have integration

**[01:36]** actuators you have integration deployment and you have this whole

**[01:38]** deployment and you have this whole

**[01:38]** deployment and you have this whole offline stack that does simulation

**[01:41]** offline stack that does simulation

**[01:41]** offline stack that does simulation training um and other things. In agents

**[01:45]** training um and other things. In agents

**[01:45]** training um and other things. In agents you also have this. So if we take a look

**[01:46]** you also have this. So if we take a look

**[01:46]** you also have this. So if we take a look at the two stacks

**[01:48]** at the two stacks

**[01:48]** at the two stacks um so in in robotics you have hardware

**[01:51]** um so in in robotics you have hardware

**[01:51]** um so in in robotics you have hardware and you have actuators you have the

**[01:52]** and you have actuators you have the

**[01:52]** and you have actuators you have the fleet and in agents you also have um

**[01:56]** fleet and in agents you also have um

**[01:56]** fleet and in agents you also have um sort of like a body right whereas

**[01:58]** sort of like a body right whereas

**[01:58]** sort of like a body right whereas robotics is you know very obviously


### [02:00 - 03:00]

**[02:01]** robotics is you know very obviously

**[02:01]** robotics is you know very obviously embodied because you go from a brain to

**[02:03]** embodied because you go from a brain to

**[02:03]** embodied because you go from a brain to a physical body. In agents you go from a

**[02:05]** a physical body. In agents you go from a

**[02:05]** a physical body. In agents you go from a model to sort of a body of a digital

**[02:08]** model to sort of a body of a digital

**[02:08]** model to sort of a body of a digital robot that includes tools. So now we

**[02:10]** robot that includes tools. So now we

**[02:10]** robot that includes tools. So now we have APIs and MCPs as well as more

**[02:13]** have APIs and MCPs as well as more

**[02:13]** have APIs and MCPs as well as more advanced uh embodiment in terms of the

**[02:16]** advanced uh embodiment in terms of the

**[02:16]** advanced uh embodiment in terms of the terminal and the browser and the VM. So

**[02:18]** terminal and the browser and the VM. So

**[02:18]** terminal and the browser and the VM. So you're starting to see like the robots

**[02:21]** you're starting to see like the robots

**[02:22]** you're starting to see like the robots hands and arms and legs to even more

**[02:25]** hands and arms and legs to even more

**[02:25]** hands and arms and legs to even more advanced things like the entire OS and

**[02:27]** advanced things like the entire OS and

**[02:27]** advanced things like the entire OS and persistent file systems and things like

**[02:29]** persistent file systems and things like

**[02:29]** persistent file systems and things like that. Um in addition you have the

**[02:31]** that. Um in addition you have the

**[02:31]** that. Um in addition you have the offline stacked so transfer over. So

**[02:33]** offline stacked so transfer over. So

**[02:33]** offline stacked so transfer over. So we're not just finished when we have the

**[02:35]** we're not just finished when we have the

**[02:35]** we're not just finished when we have the model. We also have to continuously

**[02:36]** model. We also have to continuously

**[02:36]** model. We also have to continuously retrain. We have to monitor these

**[02:38]** retrain. We have to monitor these

**[02:38]** retrain. We have to monitor these things. We also have human feedback

**[02:40]** things. We also have human feedback

**[02:40]** things. We also have human feedback loops and all this other stuff that we

**[02:42]** loops and all this other stuff that we

**[02:42]** loops and all this other stuff that we have to build as far as the tooling to

**[02:44]** have to build as far as the tooling to

**[02:44]** have to build as far as the tooling to even support development of the agent.

**[02:47]** even support development of the agent.

**[02:47]** even support development of the agent. And that's like sort of one of the first

**[02:49]** And that's like sort of one of the first

**[02:49]** And that's like sort of one of the first learnings that I I want to share is that

**[02:51]** learnings that I I want to share is that

**[02:51]** learnings that I I want to share is that um often times in self-driving people

**[02:53]** um often times in self-driving people

**[02:53]** um often times in self-driving people would often talk about the winning team

**[02:55]** would often talk about the winning team

**[02:56]** would often talk about the winning team not just having the best model and the

**[02:58]** not just having the best model and the

**[02:58]** not just having the best model and the best online stack but having the best


### [03:00 - 04:00]

**[03:00]** best online stack but having the best

**[03:00]** best online stack but having the best offline stack because that enables

**[03:01]** offline stack because that enables

**[03:01]** offline stack because that enables developers to be much faster and ship

**[03:03]** developers to be much faster and ship

**[03:04]** developers to be much faster and ship more much more reliably.

**[03:10]** So moving on, there's this concept I

**[03:10]** So moving on, there's this concept I want to share in robotics of open loop

**[03:12]** want to share in robotics of open loop

**[03:12]** want to share in robotics of open loop and closed loop. This is very simply uh

**[03:16]** and closed loop. This is very simply uh

**[03:16]** and closed loop. This is very simply uh being able to take an action or to uh

**[03:19]** being able to take an action or to uh

**[03:19]** being able to take an action or to uh move an actuator or a motor and then

**[03:21]** move an actuator or a motor and then

**[03:21]** move an actuator or a motor and then being able to get the feedback of how

**[03:22]** being able to get the feedback of how

**[03:22]** being able to get the feedback of how that actually uh happened in the real

**[03:25]** that actually uh happened in the real

**[03:25]** that actually uh happened in the real world so that you can close the loop on

**[03:27]** world so that you can close the loop on

**[03:27]** world so that you can close the loop on that actual action. So, for example, if

**[03:29]** that actual action. So, for example, if

**[03:29]** that actual action. So, for example, if I turn the wheel left, I want to

**[03:31]** I turn the wheel left, I want to

**[03:31]** I turn the wheel left, I want to actually measure uh how much did my car

**[03:34]** actually measure uh how much did my car

**[03:34]** actually measure uh how much did my car actually turn so that I can recalibrate

**[03:36]** actually turn so that I can recalibrate

**[03:36]** actually turn so that I can recalibrate and make sure that I'm turning exactly

**[03:38]** and make sure that I'm turning exactly

**[03:38]** and make sure that I'm turning exactly the amount I intended to because these

**[03:40]** the amount I intended to because these

**[03:40]** the amount I intended to because these things aren't perfect.

**[03:42]** things aren't perfect.

**[03:42]** things aren't perfect. In the same way, we're starting to see

**[03:44]** In the same way, we're starting to see

**[03:44]** In the same way, we're starting to see where some openloop things actually need

**[03:46]** where some openloop things actually need

**[03:46]** where some openloop things actually need to be closed. So, for example, if I run

**[03:48]** to be closed. So, for example, if I run

**[03:48]** to be closed. So, for example, if I run a bash command and I run an open-ended

**[03:51]** a bash command and I run an open-ended

**[03:51]** a bash command and I run an open-ended process, well, sometimes I can't observe

**[03:53]** process, well, sometimes I can't observe

**[03:53]** process, well, sometimes I can't observe the outputs, at least not in real time.

**[03:55]** the outputs, at least not in real time.

**[03:55]** the outputs, at least not in real time. I can't measure whether that bash

**[03:57]** I can't measure whether that bash

**[03:57]** I can't measure whether that bash command completed and I can't exit early

**[03:59]** command completed and I can't exit early

**[03:59]** command completed and I can't exit early if I need to. So that that's an example


### [04:00 - 05:00]

**[04:01]** if I need to. So that that's an example

**[04:02]** if I need to. So that that's an example of where we need to make things more

**[04:03]** of where we need to make things more

**[04:03]** of where we need to make things more closed loop.

**[04:06]** closed loop.

**[04:06]** closed loop. Another thing that's kind of nuanced is

**[04:08]** Another thing that's kind of nuanced is

**[04:08]** Another thing that's kind of nuanced is the fact that um we are implicitly

**[04:11]** the fact that um we are implicitly

**[04:11]** the fact that um we are implicitly discretizing in time. So what do I mean

**[04:13]** discretizing in time. So what do I mean

**[04:13]** discretizing in time. So what do I mean by that? There are explicit design

**[04:15]** by that? There are explicit design

**[04:16]** by that? There are explicit design choices that we need to make in robotics

**[04:18]** choices that we need to make in robotics

**[04:18]** choices that we need to make in robotics about the input space and then the

**[04:21]** about the input space and then the

**[04:21]** about the input space and then the action space. And particularly in the

**[04:23]** action space. And particularly in the

**[04:23]** action space. And particularly in the input space, you have different

**[04:24]** input space, you have different

**[04:24]** input space, you have different modalities. So you have the option to

**[04:27]** modalities. So you have the option to

**[04:27]** modalities. So you have the option to use vision, LAR, radar, all these

**[04:31]** use vision, LAR, radar, all these

**[04:31]** use vision, LAR, radar, all these different inputs and then combine them

**[04:32]** different inputs and then combine them

**[04:32]** different inputs and then combine them in different ways to get a sense for the

**[04:35]** in different ways to get a sense for the

**[04:35]** in different ways to get a sense for the world. You also have the ability to

**[04:37]** world. You also have the ability to

**[04:37]** world. You also have the ability to discretize the world in different ways.

**[04:39]** discretize the world in different ways.

**[04:39]** discretize the world in different ways. You can sample things every second. You

**[04:41]** You can sample things every second. You

**[04:41]** You can sample things every second. You can sample things only when they're

**[04:42]** can sample things only when they're

**[04:42]** can sample things only when they're pushed to you. Or you can sample things

**[04:44]** pushed to you. Or you can sample things

**[04:44]** pushed to you. Or you can sample things in this example on like 50 Hz, so 50

**[04:46]** in this example on like 50 Hz, so 50

**[04:46]** in this example on like 50 Hz, so 50 times per second.

**[04:48]** times per second.

**[04:48]** times per second. So that means I'll keep updating the

**[04:50]** So that means I'll keep updating the

**[04:50]** So that means I'll keep updating the state of the world and I'll keep

**[04:52]** state of the world and I'll keep

**[04:52]** state of the world and I'll keep replanning uh and I'll react to the

**[04:54]** replanning uh and I'll react to the

**[04:54]** replanning uh and I'll react to the world very quickly. However, in agents

**[04:57]** world very quickly. However, in agents

**[04:57]** world very quickly. However, in agents we've kind of done this implicitly. So

**[04:59]** we've kind of done this implicitly. So

**[04:59]** we've kind of done this implicitly. So in agents we often have a conversation.


### [05:00 - 06:00]

**[05:02]** in agents we often have a conversation.

**[05:02]** in agents we often have a conversation. So we wait to take our turn. We execute

**[05:05]** So we wait to take our turn. We execute

**[05:05]** So we wait to take our turn. We execute a tool, wait for the entire response.

**[05:07]** a tool, wait for the entire response.

**[05:07]** a tool, wait for the entire response. Maybe we do that in sort of weird ways,

**[05:10]** Maybe we do that in sort of weird ways,

**[05:10]** Maybe we do that in sort of weird ways, but we don't do this thing that's

**[05:12]** but we don't do this thing that's

**[05:12]** but we don't do this thing that's natural robotics where we keep sampling

**[05:13]** natural robotics where we keep sampling

**[05:13]** natural robotics where we keep sampling from the world and we keep interacting

**[05:15]** from the world and we keep interacting

**[05:15]** from the world and we keep interacting in real time. So this is an implicit

**[05:17]** in real time. So this is an implicit

**[05:17]** in real time. So this is an implicit design decision that is made that has

**[05:20]** design decision that is made that has

**[05:20]** design decision that is made that has its pros and cons. The pros are it's

**[05:22]** its pros and cons. The pros are it's

**[05:22]** its pros and cons. The pros are it's very easy to reason about when we have

**[05:23]** very easy to reason about when we have

**[05:24]** very easy to reason about when we have turns. It's very easy to reason about a

**[05:25]** turns. It's very easy to reason about a

**[05:25]** turns. It's very easy to reason about a conversation. It's really easy to reason

**[05:27]** conversation. It's really easy to reason

**[05:27]** conversation. It's really easy to reason about an input and output of a turn. Um

**[05:31]** about an input and output of a turn. Um

**[05:31]** about an input and output of a turn. Um but in in uh but the downside of that is

**[05:34]** but in in uh but the downside of that is

**[05:34]** but in in uh but the downside of that is that we don't get to do things in real

**[05:36]** that we don't get to do things in real

**[05:36]** that we don't get to do things in real time. You can't immediately respond to a

**[05:38]** time. You can't immediately respond to a

**[05:38]** time. You can't immediately respond to a pop-up. We can't immediately interact

**[05:40]** pop-up. We can't immediately interact

**[05:40]** pop-up. We can't immediately interact with a longunning process. So these are

**[05:43]** with a longunning process. So these are

**[05:43]** with a longunning process. So these are the implications of the design decisions

**[05:46]** the implications of the design decisions

**[05:46]** the implications of the design decisions that we make.

**[05:52]** So more on those uh inputs and action

**[05:52]** So more on those uh inputs and action spaces. So in inputs we actually have

**[05:55]** spaces. So in inputs we actually have

**[05:55]** spaces. So in inputs we actually have handcrafted a bunch of tools, a bunch of

**[05:58]** handcrafted a bunch of tools, a bunch of

**[05:58]** handcrafted a bunch of tools, a bunch of ways that we can stream from tools, we


### [06:00 - 07:00]

**[06:01]** ways that we can stream from tools, we

**[06:01]** ways that we can stream from tools, we can stream from the user, but there are

**[06:03]** can stream from the user, but there are

**[06:03]** can stream from the user, but there are other options out there. So one example

**[06:05]** other options out there. So one example

**[06:05]** other options out there. So one example I want to highlight is the terminus

**[06:07]** I want to highlight is the terminus

**[06:07]** I want to highlight is the terminus agent from terminal bench. Um, so this

**[06:09]** agent from terminal bench. Um, so this

**[06:09]** agent from terminal bench. Um, so this is very very awesome and unique in that

**[06:11]** is very very awesome and unique in that

**[06:11]** is very very awesome and unique in that they're actually using a T-X stream. So

**[06:14]** they're actually using a T-X stream. So

**[06:14]** they're actually using a T-X stream. So you can actually do character by

**[06:15]** you can actually do character by

**[06:15]** you can actually do character by character uh input and output if you

**[06:17]** character uh input and output if you

**[06:17]** character uh input and output if you want to where you can do things like

**[06:19]** want to where you can do things like

**[06:19]** want to where you can do things like control C or you can do various window

**[06:22]** control C or you can do various window

**[06:22]** control C or you can do various window commands if you want to. Um, and so that

**[06:24]** commands if you want to. Um, and so that

**[06:24]** commands if you want to. Um, and so that that's a very unique and more flexible

**[06:25]** that's a very unique and more flexible

**[06:25]** that's a very unique and more flexible way of interacting with our action space

**[06:29]** way of interacting with our action space

**[06:29]** way of interacting with our action space that we don't traditionally think about

**[06:30]** that we don't traditionally think about

**[06:30]** that we don't traditionally think about when designing agents.

**[06:33]** when designing agents.

**[06:33]** when designing agents. Other ways in which you could do action

**[06:35]** Other ways in which you could do action

**[06:35]** Other ways in which you could do action space and robotics. We could plan in

**[06:37]** space and robotics. We could plan in

**[06:37]** space and robotics. We could plan in purely XY. So you move up one block and

**[06:40]** purely XY. So you move up one block and

**[06:40]** purely XY. So you move up one block and then move over by two. You can do that

**[06:42]** then move over by two. You can do that

**[06:42]** then move over by two. You can do that in coarse ways. You can do that in

**[06:44]** in coarse ways. You can do that in

**[06:44]** in coarse ways. You can do that in continuous space. You can do things in

**[06:46]** continuous space. You can do things in

**[06:46]** continuous space. You can do things in 2D. You can do things in 3D. You can do

**[06:48]** 2D. You can do things in 3D. You can do

**[06:48]** 2D. You can do things in 3D. You can do things in acceleration instead of just

**[06:50]** things in acceleration instead of just

**[06:50]** things in acceleration instead of just position. You can do things in

**[06:51]** position. You can do things in

**[06:51]** position. You can do things in velocities. Um in agents we should also

**[06:54]** velocities. Um in agents we should also

**[06:54]** velocities. Um in agents we should also think about this although it's less

**[06:55]** think about this although it's less

**[06:55]** think about this although it's less relevant. You can you don't have to

**[06:57]** relevant. You can you don't have to

**[06:57]** relevant. You can you don't have to think about just interacting with uh

**[06:59]** think about just interacting with uh

**[06:59]** think about just interacting with uh MCPS and tool calls. Like I mentioned


### [07:00 - 08:00]

**[07:01]** MCPS and tool calls. Like I mentioned

**[07:01]** MCPS and tool calls. Like I mentioned with Terminus, you can interact with the

**[07:04]** with Terminus, you can interact with the

**[07:04]** with Terminus, you can interact with the computer at a character level. You can

**[07:05]** computer at a character level. You can

**[07:06]** computer at a character level. You can even do things like the dreamer paper

**[07:08]** even do things like the dreamer paper

**[07:08]** even do things like the dreamer paper where you interact with the computer

**[07:10]** where you interact with the computer

**[07:10]** where you interact with the computer purely by interacting at 20 frames per

**[07:13]** purely by interacting at 20 frames per

**[07:13]** purely by interacting at 20 frames per second with the mouse clicks and

**[07:14]** second with the mouse clicks and

**[07:14]** second with the mouse clicks and keyboard. So the question is what

**[07:17]** keyboard. So the question is what

**[07:17]** keyboard. So the question is what trade-offs are we making and what

**[07:18]** trade-offs are we making and what

**[07:18]** trade-offs are we making and what implicit or explicit design decisions

**[07:20]** implicit or explicit design decisions

**[07:20]** implicit or explicit design decisions have we made that either enable us to do

**[07:22]** have we made that either enable us to do

**[07:22]** have we made that either enable us to do more or is limiting what we can do with

**[07:25]** more or is limiting what we can do with

**[07:25]** more or is limiting what we can do with our agent.

**[07:31]** The next thing I want to talk about is

**[07:31]** The next thing I want to talk about is how we're going from stateless processes

**[07:33]** how we're going from stateless processes

**[07:33]** how we're going from stateless processes to stateful processes. If you think

**[07:35]** to stateful processes. If you think

**[07:36]** to stateful processes. If you think about driving in a video game, you can

**[07:38]** about driving in a video game, you can

**[07:38]** about driving in a video game, you can spawn from nothing. And you don't have

**[07:39]** spawn from nothing. And you don't have

**[07:39]** spawn from nothing. And you don't have to worry about where I came from and

**[07:41]** to worry about where I came from and

**[07:41]** to worry about where I came from and where I go after I terminate the

**[07:42]** where I go after I terminate the

**[07:42]** where I go after I terminate the session. You just have to worry about

**[07:43]** session. You just have to worry about

**[07:43]** session. You just have to worry about what I do during that session. But

**[07:45]** what I do during that session. But

**[07:45]** what I do during that session. But that's obviously not true in the real

**[07:46]** that's obviously not true in the real

**[07:46]** that's obviously not true in the real world. In the real world, you have a

**[07:48]** world. In the real world, you have a

**[07:48]** world. In the real world, you have a real car. That car takes up mass. It

**[07:51]** real car. That car takes up mass. It

**[07:51]** real car. That car takes up mass. It takes up space. And so, you do have to

**[07:53]** takes up space. And so, you do have to

**[07:53]** takes up space. And so, you do have to worry about where that car ends up. And

**[07:55]** worry about where that car ends up. And

**[07:55]** worry about where that car ends up. And you have to worry about how we got into

**[07:56]** you have to worry about how we got into

**[07:56]** you have to worry about how we got into the scene, right? everything is moving.

**[07:58]** the scene, right? everything is moving.

**[07:58]** the scene, right? everything is moving. There are implications to how fast


### [08:00 - 09:00]

**[08:00]** There are implications to how fast

**[08:00]** There are implications to how fast you're moving and how fast everyone else

**[08:01]** you're moving and how fast everyone else

**[08:01]** you're moving and how fast everyone else is moving. Similarly, we're going from

**[08:03]** is moving. Similarly, we're going from

**[08:03]** is moving. Similarly, we're going from these stateless agents to more stateful

**[08:06]** these stateless agents to more stateful

**[08:06]** these stateless agents to more stateful agents. Right? Before we just had to

**[08:08]** agents. Right? Before we just had to

**[08:08]** agents. Right? Before we just had to spin up a session and the session, get

**[08:10]** spin up a session and the session, get

**[08:10]** spin up a session and the session, get an artifact out of it. That's great.

**[08:12]** an artifact out of it. That's great.

**[08:12]** an artifact out of it. That's great. Now, we have VMs. VMs that are stateful

**[08:15]** Now, we have VMs. VMs that are stateful

**[08:15]** Now, we have VMs. VMs that are stateful both in terms of what's running, but

**[08:17]** both in terms of what's running, but

**[08:17]** both in terms of what's running, but also the persistent file store. And so,

**[08:20]** also the persistent file store. And so,

**[08:20]** also the persistent file store. And so, now when we have agents and we spin them

**[08:22]** now when we have agents and we spin them

**[08:22]** now when we have agents and we spin them up, we have to consider, hey, what is

**[08:24]** up, we have to consider, hey, what is

**[08:24]** up, we have to consider, hey, what is the entire space that we're running

**[08:25]** the entire space that we're running

**[08:25]** the entire space that we're running into? What are all the Slack messages

**[08:27]** into? What are all the Slack messages

**[08:27]** into? What are all the Slack messages that are currently going on? What is the

**[08:28]** that are currently going on? What is the

**[08:28]** that are currently going on? What is the state of the world? What are all of the

**[08:30]** state of the world? What are all of the

**[08:30]** state of the world? What are all of the things that I have to interact with? And

**[08:32]** things that I have to interact with? And

**[08:32]** things that I have to interact with? And not only how we do that, deal with that

**[08:33]** not only how we do that, deal with that

**[08:33]** not only how we do that, deal with that online, but how does that impact how we

**[08:35]** online, but how does that impact how we

**[08:35]** online, but how does that impact how we do evaluation and simulation? So these

**[08:38]** do evaluation and simulation? So these

**[08:38]** do evaluation and simulation? So these are this is one of the more interesting

**[08:39]** are this is one of the more interesting

**[08:39]** are this is one of the more interesting things that's happening in agent space

**[08:41]** things that's happening in agent space

**[08:41]** things that's happening in agent space right now.

**[08:43]** right now.

**[08:43]** right now. One of the more nuanced things more

**[08:45]** One of the more nuanced things more

**[08:45]** One of the more nuanced things more familiar to the people that are working

**[08:46]** familiar to the people that are working

**[08:46]** familiar to the people that are working on modeling and training is a sort of

**[08:49]** on modeling and training is a sort of

**[08:49]** on modeling and training is a sort of like dagger and out of distribution

**[08:50]** like dagger and out of distribution

**[08:50]** like dagger and out of distribution problem. So just like in robotics and

**[08:52]** problem. So just like in robotics and

**[08:52]** problem. So just like in robotics and agents, we have options of training our

**[08:55]** agents, we have options of training our

**[08:55]** agents, we have options of training our models with imitation uh imitation

**[08:57]** models with imitation uh imitation

**[08:57]** models with imitation uh imitation learning being similar to the SFT from


### [09:00 - 10:00]

**[09:00]** learning being similar to the SFT from

**[09:00]** learning being similar to the SFT from human demonstrations versus RL. And RL

**[09:03]** human demonstrations versus RL. And RL

**[09:03]** human demonstrations versus RL. And RL can be in simulation or it can be in

**[09:05]** can be in simulation or it can be in

**[09:05]** can be in simulation or it can be in other ways as well. But one of the known

**[09:07]** other ways as well. But one of the known

**[09:07]** other ways as well. But one of the known issues with imitation is that as soon as

**[09:10]** issues with imitation is that as soon as

**[09:10]** issues with imitation is that as soon as you get a little bit out of distribution

**[09:12]** you get a little bit out of distribution

**[09:12]** you get a little bit out of distribution or off policy in relation to the human

**[09:15]** or off policy in relation to the human

**[09:15]** or off policy in relation to the human examples, you get really out of

**[09:16]** examples, you get really out of

**[09:16]** examples, you get really out of distribution. And you can start to see

**[09:18]** distribution. And you can start to see

**[09:18]** distribution. And you can start to see this in agents such as browser agents.

**[09:20]** this in agents such as browser agents.

**[09:20]** this in agents such as browser agents. When you see a pop-up that never

**[09:21]** When you see a pop-up that never

**[09:21]** When you see a pop-up that never happened in training because humans

**[09:23]** happened in training because humans

**[09:23]** happened in training because humans actually interact with pop-ups quite

**[09:25]** actually interact with pop-ups quite

**[09:25]** actually interact with pop-ups quite naturally, it gets confused and it gets

**[09:26]** naturally, it gets confused and it gets

**[09:26]** naturally, it gets confused and it gets really confused. So this is an issue of

**[09:28]** really confused. So this is an issue of

**[09:28]** really confused. So this is an issue of cascading issues that you can see has

**[09:30]** cascading issues that you can see has

**[09:30]** cascading issues that you can see has been studied for quite a while in

**[09:32]** been studied for quite a while in

**[09:32]** been studied for quite a while in robotics.

**[09:35]** robotics.

**[09:35]** robotics. And the general theme around this is

**[09:36]** And the general theme around this is

**[09:36]** And the general theme around this is that actions have consequences. We're

**[09:39]** that actions have consequences. We're

**[09:39]** that actions have consequences. We're not just dealing with classification

**[09:41]** not just dealing with classification

**[09:41]** not just dealing with classification models. We're not just dealing with

**[09:43]** models. We're not just dealing with

**[09:43]** models. We're not just dealing with prediction models or sequences. We're

**[09:45]** prediction models or sequences. We're

**[09:45]** prediction models or sequences. We're dealing with a whole new paradigm in

**[09:47]** dealing with a whole new paradigm in

**[09:47]** dealing with a whole new paradigm in which you predict, you act, and then you

**[09:49]** which you predict, you act, and then you

**[09:49]** which you predict, you act, and then you deal with the consequences of that

**[09:51]** deal with the consequences of that

**[09:51]** deal with the consequences of that action and then re-evaluate everything

**[09:53]** action and then re-evaluate everything

**[09:53]** action and then re-evaluate everything you've done before. And that's really

**[09:55]** you've done before. And that's really

**[09:55]** you've done before. And that's really tough because actions have consequences

**[09:57]** tough because actions have consequences

**[09:57]** tough because actions have consequences and actions have consequences in a very

**[09:59]** and actions have consequences in a very

**[09:59]** and actions have consequences in a very messy real world.


### [10:00 - 11:00]

**[10:03]** messy real world.

**[10:03]** messy real world. And as a result of the complexity of the

**[10:05]** And as a result of the complexity of the

**[10:05]** And as a result of the complexity of the real world, that's where simulation

**[10:07]** real world, that's where simulation

**[10:07]** real world, that's where simulation comes into play such that you can

**[10:09]** comes into play such that you can

**[10:09]** comes into play such that you can represent all of these complexities and

**[10:11]** represent all of these complexities and

**[10:11]** represent all of these complexities and all the messiness of the real world into

**[10:13]** all the messiness of the real world into

**[10:13]** all the messiness of the real world into your starting state and you can play

**[10:15]** your starting state and you can play

**[10:15]** your starting state and you can play through uh the real world not just in a

**[10:18]** through uh the real world not just in a

**[10:18]** through uh the real world not just in a single path but all the paths that you

**[10:20]** single path but all the paths that you

**[10:20]** single path but all the paths that you could possibly take as your agent

**[10:22]** could possibly take as your agent

**[10:22]** could possibly take as your agent changes. So we call that playing out

**[10:24]** changes. So we call that playing out

**[10:24]** changes. So we call that playing out counterfactuals.

**[10:29]** The other thing to be aware about, and

**[10:29]** The other thing to be aware about, and this is sort of like classic

**[10:31]** this is sort of like classic

**[10:31]** this is sort of like classic reinforcement learning or robotics, is

**[10:32]** reinforcement learning or robotics, is

**[10:32]** reinforcement learning or robotics, is the concept of an MDP. And so that's

**[10:35]** the concept of an MDP. And so that's

**[10:35]** the concept of an MDP. And so that's where there's an agent that takes into

**[10:37]** where there's an agent that takes into

**[10:37]** where there's an agent that takes into account a state and a reward and then

**[10:40]** account a state and a reward and then

**[10:40]** account a state and a reward and then we'll take actions on an environment or

**[10:42]** we'll take actions on an environment or

**[10:42]** we'll take actions on an environment or a world. And this is just sort of a

**[10:44]** a world. And this is just sort of a

**[10:44]** a world. And this is just sort of a formalism about how to conceptualize how

**[10:47]** formalism about how to conceptualize how

**[10:47]** formalism about how to conceptualize how you're running the agent loop. And these

**[10:49]** you're running the agent loop. And these

**[10:49]** you're running the agent loop. And these are just useful primitives to have on

**[10:51]** are just useful primitives to have on

**[10:51]** are just useful primitives to have on hand so that you can describe and you

**[10:53]** hand so that you can describe and you

**[10:53]** hand so that you can describe and you can communicate what's going on.

**[10:57]** can communicate what's going on.

**[10:57]** can communicate what's going on. The reason this is important is because

**[10:59]** The reason this is important is because

**[10:59]** The reason this is important is because we're moving from just plain chat models


### [11:00 - 12:00]

**[11:02]** we're moving from just plain chat models

**[11:02]** we're moving from just plain chat models to agent models that take action. For

**[11:05]** to agent models that take action. For

**[11:05]** to agent models that take action. For context, a lot of self-driving uh

**[11:07]** context, a lot of self-driving uh

**[11:07]** context, a lot of self-driving uh initially seemed really fast but was

**[11:09]** initially seemed really fast but was

**[11:09]** initially seemed really fast but was really slow in progress because it was

**[11:11]** really slow in progress because it was

**[11:11]** really slow in progress because it was sort of the same issues. So everybody in

**[11:13]** sort of the same issues. So everybody in

**[11:14]** sort of the same issues. So everybody in the space from 2017 to 2020 was really

**[11:18]** the space from 2017 to 2020 was really

**[11:18]** the space from 2017 to 2020 was really focused on perception models and

**[11:19]** focused on perception models and

**[11:19]** focused on perception models and thinking that all you really needed to

**[11:21]** thinking that all you really needed to

**[11:21]** thinking that all you really needed to do was uh take the state of the world

**[11:23]** do was uh take the state of the world

**[11:23]** do was uh take the state of the world and make boxes and then you can drive

**[11:25]** and make boxes and then you can drive

**[11:25]** and make boxes and then you can drive around the boxes really easily. It turns

**[11:28]** around the boxes really easily. It turns

**[11:28]** around the boxes really easily. It turns out that assumption wasn't necessarily

**[11:29]** out that assumption wasn't necessarily

**[11:29]** out that assumption wasn't necessarily true and there's a lot of hidden

**[11:31]** true and there's a lot of hidden

**[11:31]** true and there's a lot of hidden complexity in creating action models and

**[11:34]** complexity in creating action models and

**[11:34]** complexity in creating action models and not just predictive models. Similarly in

**[11:37]** not just predictive models. Similarly in

**[11:38]** not just predictive models. Similarly in language models we can see that we can

**[11:40]** language models we can see that we can

**[11:40]** language models we can see that we can understand basically everything about

**[11:42]** understand basically everything about

**[11:42]** understand basically everything about the world that comes in via text. We can

**[11:44]** the world that comes in via text. We can

**[11:44]** the world that comes in via text. We can generate really long sophisticated

**[11:46]** generate really long sophisticated

**[11:46]** generate really long sophisticated reasoning traces.

**[11:49]** reasoning traces.

**[11:49]** reasoning traces. But when you take these really

**[11:51]** But when you take these really

**[11:51]** But when you take these really sophisticated plans, really

**[11:53]** sophisticated plans, really

**[11:53]** sophisticated plans, really sophisticated chains of tool calls and

**[11:54]** sophisticated chains of tool calls and

**[11:54]** sophisticated chains of tool calls and you implement them in the real world,

**[11:56]** you implement them in the real world,

**[11:56]** you implement them in the real world, you can see things go wrong all the

**[11:57]** you can see things go wrong all the

**[11:58]** you can see things go wrong all the time. You can see the tool calls fail


### [12:00 - 13:00]

**[12:00]** time. You can see the tool calls fail

**[12:00]** time. You can see the tool calls fail and the agent failed to progress. You

**[12:02]** and the agent failed to progress. You

**[12:02]** and the agent failed to progress. You can see the agent failed to correct from

**[12:04]** can see the agent failed to correct from

**[12:04]** can see the agent failed to correct from its own mistakes. This is sort of the

**[12:07]** its own mistakes. This is sort of the

**[12:07]** its own mistakes. This is sort of the loop that is deceptively tricky about

**[12:10]** loop that is deceptively tricky about

**[12:10]** loop that is deceptively tricky about when you get into actions from

**[12:11]** when you get into actions from

**[12:11]** when you get into actions from predictive models. This is really where

**[12:14]** predictive models. This is really where

**[12:14]** predictive models. This is really where the bulk of the work had been and where

**[12:17]** the bulk of the work had been and where

**[12:17]** the bulk of the work had been and where a bulk of the work will continue to be

**[12:19]** a bulk of the work will continue to be

**[12:19]** a bulk of the work will continue to be in agents as well.

**[12:22]** in agents as well.

**[12:22]** in agents as well. I also want to point out in both of

**[12:23]** I also want to point out in both of

**[12:23]** I also want to point out in both of these cases in self-driving when it

**[12:25]** these cases in self-driving when it

**[12:25]** these cases in self-driving when it comes to robotics

**[12:27]** comes to robotics

**[12:27]** comes to robotics and in code when it comes to digital

**[12:29]** and in code when it comes to digital

**[12:29]** and in code when it comes to digital agents we're actually very lucky in

**[12:31]** agents we're actually very lucky in

**[12:31]** agents we're actually very lucky in both. Like why are we lucky? I you can

**[12:33]** both. Like why are we lucky? I you can

**[12:33]** both. Like why are we lucky? I you can see self-driving working really well in

**[12:35]** see self-driving working really well in

**[12:35]** see self-driving working really well in production today in limited cases

**[12:37]** production today in limited cases

**[12:37]** production today in limited cases whereas the rest of robotics is still

**[12:39]** whereas the rest of robotics is still

**[12:39]** whereas the rest of robotics is still limited to demos and this is because of

**[12:42]** limited to demos and this is because of

**[12:42]** limited to demos and this is because of how we have this machine that's

**[12:45]** how we have this machine that's

**[12:46]** how we have this machine that's predefined with human controls that's

**[12:48]** predefined with human controls that's

**[12:48]** predefined with human controls that's been really well refined over the last

**[12:50]** been really well refined over the last

**[12:50]** been really well refined over the last few decades and then it has electronic

**[12:53]** few decades and then it has electronic

**[12:53]** few decades and then it has electronic controls and it has built-in telemetry

**[12:55]** controls and it has built-in telemetry

**[12:55]** controls and it has built-in telemetry right so it's something that you already

**[12:57]** right so it's something that you already

**[12:57]** right so it's something that you already have a predefined interface to take


### [13:00 - 14:00]

**[13:00]** have a predefined interface to take

**[13:00]** have a predefined interface to take actions with and you have predefined

**[13:01]** actions with and you have predefined

**[13:01]** actions with and you have predefined interfaces to collect the data from.

**[13:05]** interfaces to collect the data from.

**[13:05]** interfaces to collect the data from. So that makes it really convenient to

**[13:08]** So that makes it really convenient to

**[13:08]** So that makes it really convenient to operate through code and it makes it

**[13:10]** operate through code and it makes it

**[13:10]** operate through code and it makes it really convenient to perform machine

**[13:12]** really convenient to perform machine

**[13:12]** really convenient to perform machine learning and learning in general on. We

**[13:14]** learning and learning in general on. We

**[13:14]** learning and learning in general on. We have this predefined interface with

**[13:16]** have this predefined interface with

**[13:16]** have this predefined interface with predefined actions and predefined

**[13:18]** predefined actions and predefined

**[13:18]** predefined actions and predefined telemetry and that makes it much much

**[13:21]** telemetry and that makes it much much

**[13:21]** telemetry and that makes it much much easier of a task than going into some of

**[13:23]** easier of a task than going into some of

**[13:23]** easier of a task than going into some of these other knowledge work tasks that

**[13:25]** these other knowledge work tasks that

**[13:25]** these other knowledge work tasks that require the full desktop and things that

**[13:28]** require the full desktop and things that

**[13:28]** require the full desktop and things that are less easy to codify.

**[13:31]** are less easy to codify.

**[13:31]** are less easy to codify. So when we explore new domains, these

**[13:34]** So when we explore new domains, these

**[13:34]** So when we explore new domains, these are some of the things we want to

**[13:35]** are some of the things we want to

**[13:35]** are some of the things we want to consider. Is there somewhere where we

**[13:38]** consider. Is there somewhere where we

**[13:38]** consider. Is there somewhere where we already get a predefined human interface

**[13:40]** already get a predefined human interface

**[13:40]** already get a predefined human interface that makes it easy to do those two

**[13:41]** that makes it easy to do those two

**[13:42]** that makes it easy to do those two things?

**[13:44]** things?

**[13:44]** things? Finally, I want to talk about one of the

**[13:46]** Finally, I want to talk about one of the

**[13:46]** Finally, I want to talk about one of the things that we face from day-to-day and

**[13:47]** things that we face from day-to-day and

**[13:48]** things that we face from day-to-day and that's the hill climbing process. And if

**[13:49]** that's the hill climbing process. And if

**[13:50]** that's the hill climbing process. And if you're not familiar with hill climbing,

**[13:51]** you're not familiar with hill climbing,

**[13:51]** you're not familiar with hill climbing, it's basically this iterative process of

**[13:54]** it's basically this iterative process of

**[13:54]** it's basically this iterative process of building or iterating on a complex

**[13:57]** building or iterating on a complex

**[13:57]** building or iterating on a complex system such as an LM or an agent. when


### [14:00 - 15:00]

**[14:00]** system such as an LM or an agent. when

**[14:00]** system such as an LM or an agent. when you don't always make forward progress.

**[14:02]** you don't always make forward progress.

**[14:02]** you don't always make forward progress. So before when we were working on full

**[14:04]** So before when we were working on full

**[14:04]** So before when we were working on full stack web applications or working on

**[14:05]** stack web applications or working on

**[14:05]** stack web applications or working on more simple systems, you implement a

**[14:07]** more simple systems, you implement a

**[14:07]** more simple systems, you implement a feature and you probably guarantee that

**[14:09]** feature and you probably guarantee that

**[14:09]** feature and you probably guarantee that feature will arrive into prod. Nowadays

**[14:12]** feature will arrive into prod. Nowadays

**[14:12]** feature will arrive into prod. Nowadays you have this sort of like nebulous

**[14:14]** you have this sort of like nebulous

**[14:14]** you have this sort of like nebulous metric that you're trying to hit. And

**[14:15]** metric that you're trying to hit. And

**[14:15]** metric that you're trying to hit. And the only way you can do that is by

**[14:17]** the only way you can do that is by

**[14:17]** the only way you can do that is by guessing and checking. So you have a

**[14:19]** guessing and checking. So you have a

**[14:19]** guessing and checking. So you have a metric like a benchmark, then you make

**[14:21]** metric like a benchmark, then you make

**[14:21]** metric like a benchmark, then you make some guess, you run some experiment and

**[14:23]** some guess, you run some experiment and

**[14:23]** some guess, you run some experiment and you hope you go up, sometimes you go

**[14:24]** you hope you go up, sometimes you go

**[14:24]** you hope you go up, sometimes you go down, but as long as you keep going up

**[14:26]** down, but as long as you keep going up

**[14:26]** down, but as long as you keep going up and up and up, then you can eventually

**[14:28]** and up and up, then you can eventually

**[14:28]** and up and up, then you can eventually reach your goal. And that's the concept

**[14:29]** reach your goal. And that's the concept

**[14:29]** reach your goal. And that's the concept of hill climbing. But how we do it in

**[14:32]** of hill climbing. But how we do it in

**[14:32]** of hill climbing. But how we do it in the self-driving way is a little bit

**[14:34]** the self-driving way is a little bit

**[14:34]** the self-driving way is a little bit more sophisticated. We actually start by

**[14:36]** more sophisticated. We actually start by

**[14:36]** more sophisticated. We actually start by learning and then going through

**[14:37]** learning and then going through

**[14:37]** learning and then going through simulation. Simulation helps you deploy

**[14:39]** simulation. Simulation helps you deploy

**[14:39]** simulation. Simulation helps you deploy with confidence and it also helps your

**[14:41]** with confidence and it also helps your

**[14:41]** with confidence and it also helps your learning. But then once you deploy, you

**[14:43]** learning. But then once you deploy, you

**[14:43]** learning. But then once you deploy, you can actually get logs from the real

**[14:45]** can actually get logs from the real

**[14:45]** can actually get logs from the real world that feed back into your

**[14:46]** world that feed back into your

**[14:46]** world that feed back into your simulation engine. That's really

**[14:48]** simulation engine. That's really

**[14:48]** simulation engine. That's really important because you want to ground

**[14:49]** important because you want to ground

**[14:49]** important because you want to ground your simulation on something. And so you

**[14:51]** your simulation on something. And so you

**[14:51]** your simulation on something. And so you start to get this full loop. The logs

**[14:53]** start to get this full loop. The logs

**[14:53]** start to get this full loop. The logs actually become a much more important

**[14:55]** actually become a much more important

**[14:55]** actually become a much more important part of the process than they are today.

**[14:57]** part of the process than they are today.

**[14:57]** part of the process than they are today. you can get a lot more insights than

**[14:59]** you can get a lot more insights than


### [15:00 - 16:00]

**[15:00]** you can get a lot more insights than just your numbers, right? So like a 70%

**[15:02]** just your numbers, right? So like a 70%

**[15:02]** just your numbers, right? So like a 70% at a benchmark will tell you a little

**[15:03]** at a benchmark will tell you a little

**[15:04]** at a benchmark will tell you a little bit, but if you start to break them down

**[15:05]** bit, but if you start to break them down

**[15:05]** bit, but if you start to break them down into different categories, different

**[15:07]** into different categories, different

**[15:07]** into different categories, different cities, different ways you can mess up,

**[15:09]** cities, different ways you can mess up,

**[15:09]** cities, different ways you can mess up, start to triage the individual failures,

**[15:11]** start to triage the individual failures,

**[15:11]** start to triage the individual failures, you can get a lot more insights about

**[15:13]** you can get a lot more insights about

**[15:13]** you can get a lot more insights about how to improve your system and on where

**[15:16]** how to improve your system and on where

**[15:16]** how to improve your system and on where to improve. And that's a lot of what

**[15:18]** to improve. And that's a lot of what

**[15:18]** to improve. And that's a lot of what we've developed our tooling around and a

**[15:20]** we've developed our tooling around and a

**[15:20]** we've developed our tooling around and a lot of what we've developed our

**[15:21]** lot of what we've developed our

**[15:21]** lot of what we've developed our processes around that help some of our

**[15:23]** processes around that help some of our

**[15:23]** processes around that help some of our customers with their hill climbing.

**[15:25]** customers with their hill climbing.

**[15:25]** customers with their hill climbing. Finally, like you know, we're only part

**[15:27]** Finally, like you know, we're only part

**[15:27]** Finally, like you know, we're only part of the way there. At least this is a

**[15:28]** of the way there. At least this is a

**[15:28]** of the way there. At least this is a metric from the remote labor benchmark.

**[15:31]** metric from the remote labor benchmark.

**[15:31]** metric from the remote labor benchmark. And you know, I'd like to compare this

**[15:33]** And you know, I'd like to compare this

**[15:33]** And you know, I'd like to compare this to where self-driving was back in the

**[15:35]** to where self-driving was back in the

**[15:35]** to where self-driving was back in the beginning. And it's because we have

**[15:37]** beginning. And it's because we have

**[15:37]** beginning. And it's because we have really great demos and we have really

**[15:38]** really great demos and we have really

**[15:38]** really great demos and we have really great predictive models, but we're not

**[15:40]** great predictive models, but we're not

**[15:40]** great predictive models, but we're not nearly there as far as endto-end work

**[15:42]** nearly there as far as endto-end work

**[15:42]** nearly there as far as endto-end work completion. A lot of the reasons are

**[15:44]** completion. A lot of the reasons are

**[15:44]** completion. A lot of the reasons are because of the things I brought up

**[15:46]** because of the things I brought up

**[15:46]** because of the things I brought up before with actions having consequences

**[15:48]** before with actions having consequences

**[15:48]** before with actions having consequences and the complexity of the real world. To

**[15:51]** and the complexity of the real world. To

**[15:51]** and the complexity of the real world. To recap, we've covered the parallels

**[15:53]** recap, we've covered the parallels

**[15:53]** recap, we've covered the parallels between robotics and agents. Some of

**[15:55]** between robotics and agents. Some of

**[15:55]** between robotics and agents. Some of those are having to do closed loop

**[15:57]** those are having to do closed loop

**[15:57]** those are having to do closed loop systems, getting closed loop feedback,

**[15:59]** systems, getting closed loop feedback,

**[15:59]** systems, getting closed loop feedback, how we discretize systems, how we pick


### [16:00 - 17:00]

**[16:01]** how we discretize systems, how we pick

**[16:01]** how we discretize systems, how we pick action and input spaces, how we can go

**[16:04]** action and input spaces, how we can go

**[16:04]** action and input spaces, how we can go from stateless to stateful, how we're

**[16:06]** from stateless to stateful, how we're

**[16:06]** from stateless to stateful, how we're going from predictive models to action

**[16:08]** going from predictive models to action

**[16:08]** going from predictive models to action models, how we utilize simulation in

**[16:11]** models, how we utilize simulation in

**[16:11]** models, how we utilize simulation in deployment and in training, um, and how

**[16:13]** deployment and in training, um, and how

**[16:13]** deployment and in training, um, and how infrastructure is really important to

**[16:14]** infrastructure is really important to

**[16:14]** infrastructure is really important to the entire development process. If

**[16:17]** the entire development process. If

**[16:17]** the entire development process. If you've gotten this far, I'd like to say

**[16:19]** you've gotten this far, I'd like to say

**[16:19]** you've gotten this far, I'd like to say congrats and you've become a master in

**[16:22]** congrats and you've become a master in

**[16:22]** congrats and you've become a master in this new topic that we're calling

**[16:23]** this new topic that we're calling

**[16:23]** this new topic that we're calling agentics because why not? Because, you

**[16:25]** agentics because why not? Because, you

**[16:25]** agentics because why not? Because, you know, robotics sounds cool. Why not make

**[16:28]** know, robotics sounds cool. Why not make

**[16:28]** know, robotics sounds cool. Why not make the this agent development stuff just as

**[16:30]** the this agent development stuff just as

**[16:30]** the this agent development stuff just as cool? Um because I think it takes a lot

**[16:32]** cool? Um because I think it takes a lot

**[16:32]** cool? Um because I think it takes a lot of these core concepts and abstractions

**[16:34]** of these core concepts and abstractions

**[16:34]** of these core concepts and abstractions to really make this go from something

**[16:37]** to really make this go from something

**[16:37]** to really make this go from something that we hack on to something that has

**[16:39]** that we hack on to something that has

**[16:39]** that we hack on to something that has dedicated real science and really

**[16:41]** dedicated real science and really

**[16:41]** dedicated real science and really becomes a practice. And so if any of

**[16:43]** becomes a practice. And so if any of

**[16:43]** becomes a practice. And so if any of these concepts are useful for you like a

**[16:45]** these concepts are useful for you like a

**[16:45]** these concepts are useful for you like a lot of these things are pretty easy to

**[16:47]** lot of these things are pretty easy to

**[16:47]** lot of these things are pretty easy to understand and read about. You can read

**[16:49]** understand and read about. You can read

**[16:49]** understand and read about. You can read about openloop and closed loop control

**[16:51]** about openloop and closed loop control

**[16:51]** about openloop and closed loop control MDPs fully versus partially observable

**[16:54]** MDPs fully versus partially observable

**[16:54]** MDPs fully versus partially observable environments. You can read about dagger

**[16:56]** environments. You can read about dagger

**[16:56]** environments. You can read about dagger uh offline RL is a really cool topic

**[16:58]** uh offline RL is a really cool topic

**[16:58]** uh offline RL is a really cool topic that is featured in more recent robotics


### [17:00 - 18:00]

**[17:00]** that is featured in more recent robotics

**[17:00]** that is featured in more recent robotics work. And then just like the intro

**[17:02]** work. And then just like the intro

**[17:02]** work. And then just like the intro reinforcement learning book is all

**[17:04]** reinforcement learning book is all

**[17:04]** reinforcement learning book is all great. You probably will understand

**[17:06]** great. You probably will understand

**[17:06]** great. You probably will understand these things natively because the

**[17:08]** these things natively because the

**[17:08]** these things natively because the problems are really obvious and easier

**[17:09]** problems are really obvious and easier

**[17:10]** problems are really obvious and easier to understand in agent space. And

**[17:11]** to understand in agent space. And

**[17:11]** to understand in agent space. And finally, you can read up on a lot of the

**[17:13]** finally, you can read up on a lot of the

**[17:13]** finally, you can read up on a lot of the recent robotics literature as well since

**[17:16]** recent robotics literature as well since

**[17:16]** recent robotics literature as well since a lot of the field is converging. So you

**[17:18]** a lot of the field is converging. So you

**[17:18]** a lot of the field is converging. So you can just start from the papers.

**[17:20]** can just start from the papers.

**[17:20]** can just start from the papers. Just as a recap, you know, agents are

**[17:23]** Just as a recap, you know, agents are

**[17:23]** Just as a recap, you know, agents are robots too. They act in the real world.

**[17:24]** robots too. They act in the real world.

**[17:24]** robots too. They act in the real world. They make mistakes. They have to

**[17:25]** They make mistakes. They have to

**[17:25]** They make mistakes. They have to recover. And all of these little things

**[17:28]** recover. And all of these little things

**[17:28]** recover. And all of these little things really matter. Thanks. You can feel free

**[17:30]** really matter. Thanks. You can feel free

**[17:30]** really matter. Thanks. You can feel free to get in touch. Here's my email,

**[17:31]** to get in touch. Here's my email,

**[17:31]** to get in touch. Here's my email, jesseabund.ai.

**[17:33]** jesseabund.ai.

**[17:33]** jesseabund.ai. Feel free to send me any thoughts or

**[17:34]** Feel free to send me any thoughts or

**[17:34]** Feel free to send me any thoughts or feedback. Thanks.


