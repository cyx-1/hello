# Software Development Agents- What Works and What Doesn't - Robert Brennan, AllHands_OpenHands

**Video URL:** https://www.youtube.com/watch?v=o_hhkJtlbSs

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Today I'm going to talk a little bit

**[00:16]** Today I'm going to talk a little bit about uh coding agents and how to use

**[00:18]** about uh coding agents and how to use

**[00:18]** about uh coding agents and how to use them effectively really. Um if you're

**[00:21]** them effectively really. Um if you're

**[00:21]** them effectively really. Um if you're anything like me, you found that uh you

**[00:23]** anything like me, you found that uh you

**[00:23]** anything like me, you found that uh you found a lot of things that work really

**[00:24]** found a lot of things that work really

**[00:24]** found a lot of things that work really well and a lot of things that uh don't

**[00:26]** well and a lot of things that uh don't

**[00:26]** well and a lot of things that uh don't work very well. Um,

**[00:29]** work very well. Um,

**[00:29]** work very well. Um, so a little bit about me. Uh, my name is

**[00:30]** so a little bit about me. Uh, my name is

**[00:30]** so a little bit about me. Uh, my name is Robert Brennan. I've been building, uh,

**[00:32]** Robert Brennan. I've been building, uh,

**[00:32]** Robert Brennan. I've been building, uh, open source development tools for for

**[00:34]** open source development tools for for

**[00:34]** open source development tools for for over a decade now. Uh, and my team and

**[00:36]** over a decade now. Uh, and my team and

**[00:36]** over a decade now. Uh, and my team and I, uh, have created, uh, an open-source,

**[00:39]** I, uh, have created, uh, an open-source,

**[00:39]** I, uh, have created, uh, an open-source, uh, software development agent called

**[00:41]** uh, software development agent called

**[00:41]** uh, software development agent called Open Hands, formerly known as Open

**[00:42]** Open Hands, formerly known as Open

**[00:42]** Open Hands, formerly known as Open Devon.

**[00:45]** Devon.

**[00:45]** Devon. So, to to state the obvious, in 2025,

**[00:47]** So, to to state the obvious, in 2025,

**[00:47]** So, to to state the obvious, in 2025, software development is changing. Uh,

**[00:49]** software development is changing. Uh,

**[00:49]** software development is changing. Uh, our jobs are are very different now than

**[00:51]** our jobs are are very different now than

**[00:51]** our jobs are are very different now than they were 2 years ago. Uh, and they're

**[00:53]** they were 2 years ago. Uh, and they're

**[00:53]** they were 2 years ago. Uh, and they're going to be very different two years

**[00:55]** going to be very different two years

**[00:55]** going to be very different two years from now. Uh, and the thing I want to

**[00:56]** from now. Uh, and the thing I want to

**[00:56]** from now. Uh, and the thing I want to convince you of is that coding is going

**[00:58]** convince you of is that coding is going

**[00:58]** convince you of is that coding is going away. Uh, we're going to be spending a


### [01:00 - 02:00]

**[01:00]** away. Uh, we're going to be spending a

**[01:00]** away. Uh, we're going to be spending a lot less time actually writing code. Uh,

**[01:02]** lot less time actually writing code. Uh,

**[01:02]** lot less time actually writing code. Uh, but that doesn't mean that software

**[01:03]** but that doesn't mean that software

**[01:03]** but that doesn't mean that software engineering is going away. Uh, we're

**[01:05]** engineering is going away. Uh, we're

**[01:06]** engineering is going away. Uh, we're paid not to to type on our keyboard, but

**[01:08]** paid not to to type on our keyboard, but

**[01:08]** paid not to to type on our keyboard, but to actually think critically about the

**[01:09]** to actually think critically about the

**[01:09]** to actually think critically about the problems that are in front of us. Uh,

**[01:11]** problems that are in front of us. Uh,

**[01:11]** problems that are in front of us. Uh, and so if we do AIdriven development

**[01:13]** and so if we do AIdriven development

**[01:13]** and so if we do AIdriven development correctly, um, it'll mean we spend less

**[01:16]** correctly, um, it'll mean we spend less

**[01:16]** correctly, um, it'll mean we spend less time actually like leaning forward and

**[01:17]** time actually like leaning forward and

**[01:18]** time actually like leaning forward and squinting into our IDE and more time

**[01:20]** squinting into our IDE and more time

**[01:20]** squinting into our IDE and more time kind of sitting back in our chair and

**[01:21]** kind of sitting back in our chair and

**[01:21]** kind of sitting back in our chair and thinking, you know, what does the user

**[01:23]** thinking, you know, what does the user

**[01:23]** thinking, you know, what does the user actually want here? uh what are we

**[01:25]** actually want here? uh what are we

**[01:25]** actually want here? uh what are we actually trying to build? What what

**[01:26]** actually trying to build? What what

**[01:26]** actually trying to build? What what problems are we trying to solve as an

**[01:28]** problems are we trying to solve as an

**[01:28]** problems are we trying to solve as an organization? Uh how can we architect

**[01:30]** organization? Uh how can we architect

**[01:30]** organization? Uh how can we architect this in a way that sets us up for the

**[01:31]** this in a way that sets us up for the

**[01:31]** this in a way that sets us up for the future? Uh the AI is very good at that

**[01:34]** future? Uh the AI is very good at that

**[01:34]** future? Uh the AI is very good at that at that interloop of development, the

**[01:35]** at that interloop of development, the

**[01:35]** at that interloop of development, the write code, run the code, write code,

**[01:37]** write code, run the code, write code,

**[01:37]** write code, run the code, write code, run the code. It's not very good at

**[01:38]** run the code. It's not very good at

**[01:38]** run the code. It's not very good at those kind of big picture tasks that

**[01:40]** those kind of big picture tasks that

**[01:40]** those kind of big picture tasks that have to take into account um that have

**[01:42]** have to take into account um that have

**[01:42]** have to take into account um that have to like empathize with the end user uh

**[01:44]** to like empathize with the end user uh

**[01:44]** to like empathize with the end user uh take into account business level

**[01:45]** take into account business level

**[01:45]** take into account business level objectives. Uh and that's where we come

**[01:47]** objectives. Uh and that's where we come

**[01:47]** objectives. Uh and that's where we come in as as software engineers.

**[01:53]** Uh so let's talk a little bit about what

**[01:53]** Uh so let's talk a little bit about what actually a coding agent is. Uh I think

**[01:56]** actually a coding agent is. Uh I think

**[01:56]** actually a coding agent is. Uh I think this word agent gets thrown around a lot

**[01:57]** this word agent gets thrown around a lot

**[01:57]** this word agent gets thrown around a lot these days. Uh the meaning has started

**[01:59]** these days. Uh the meaning has started

**[01:59]** these days. Uh the meaning has started to to drift over time. Uh but at the


### [02:00 - 03:00]

**[02:01]** to to drift over time. Uh but at the

**[02:01]** to to drift over time. Uh but at the core of it is this this concept of

**[02:03]** core of it is this this concept of

**[02:03]** core of it is this this concept of agency. Um it's this idea of taking

**[02:06]** agency. Um it's this idea of taking

**[02:06]** agency. Um it's this idea of taking action out in the real world. Um and

**[02:09]** action out in the real world. Um and

**[02:09]** action out in the real world. Um and these are these are the main tools of a

**[02:11]** these are these are the main tools of a

**[02:11]** these are these are the main tools of a software engineer's job, right? We have

**[02:13]** software engineer's job, right? We have

**[02:13]** software engineer's job, right? We have a a code editor to actually modify our

**[02:15]** a a code editor to actually modify our

**[02:15]** a a code editor to actually modify our codebase, navigate our codebase. uh you

**[02:17]** codebase, navigate our codebase. uh you

**[02:17]** codebase, navigate our codebase. uh you have a terminal uh to help you actually

**[02:19]** have a terminal uh to help you actually

**[02:19]** have a terminal uh to help you actually run the code that you're that you're

**[02:20]** run the code that you're that you're

**[02:20]** run the code that you're that you're writing uh and you need a web browser in

**[02:22]** writing uh and you need a web browser in

**[02:22]** writing uh and you need a web browser in order to look up documentation and maybe

**[02:24]** order to look up documentation and maybe

**[02:24]** order to look up documentation and maybe copy and paste some code from Stack

**[02:26]** copy and paste some code from Stack

**[02:26]** copy and paste some code from Stack Overflow. So these are kind of the core

**[02:28]** Overflow. So these are kind of the core

**[02:28]** Overflow. So these are kind of the core tools of the job and these are the tools

**[02:29]** tools of the job and these are the tools

**[02:29]** tools of the job and these are the tools that we give to our agents to let them

**[02:31]** that we give to our agents to let them

**[02:32]** that we give to our agents to let them do their whole uh development loop.

**[02:35]** do their whole uh development loop.

**[02:35]** do their whole uh development loop. I also want to contrast uh you know

**[02:37]** I also want to contrast uh you know

**[02:37]** I also want to contrast uh you know coding agents from some more tactical

**[02:39]** coding agents from some more tactical

**[02:39]** coding agents from some more tactical codegen tools that are out there. Um,

**[02:41]** codegen tools that are out there. Um,

**[02:41]** codegen tools that are out there. Um, you know, we kind of started a couple

**[02:43]** you know, we kind of started a couple

**[02:43]** you know, we kind of started a couple years ago with things like, uh, GitHub

**[02:44]** years ago with things like, uh, GitHub

**[02:44]** years ago with things like, uh, GitHub Copilot's autocomplete feature where,

**[02:47]** Copilot's autocomplete feature where,

**[02:47]** Copilot's autocomplete feature where, you know, it's literally wherever your

**[02:48]** you know, it's literally wherever your

**[02:48]** you know, it's literally wherever your cursor is pointed in the codebase. Right

**[02:49]** cursor is pointed in the codebase. Right

**[02:49]** cursor is pointed in the codebase. Right now, it's just filling out two or three

**[02:51]** now, it's just filling out two or three

**[02:51]** now, it's just filling out two or three more lines of code. Um, and then over

**[02:54]** more lines of code. Um, and then over

**[02:54]** more lines of code. Um, and then over time, things have gotten more and more

**[02:55]** time, things have gotten more and more

**[02:55]** time, things have gotten more and more agentic, more and more asynchronous,

**[02:57]** agentic, more and more asynchronous,

**[02:57]** agentic, more and more asynchronous, right? Uh, so we got like AI powered

**[02:59]** right? Uh, so we got like AI powered

**[02:59]** right? Uh, so we got like AI powered idees that can maybe take a few steps at


### [03:00 - 04:00]

**[03:01]** idees that can maybe take a few steps at

**[03:01]** idees that can maybe take a few steps at a time without a developer interfering.

**[03:04]** a time without a developer interfering.

**[03:04]** a time without a developer interfering. And then uh now you've got these tools

**[03:05]** And then uh now you've got these tools

**[03:05]** And then uh now you've got these tools like Devon and Open Hands where you're

**[03:08]** like Devon and Open Hands where you're

**[03:08]** like Devon and Open Hands where you're really giving an agent, you know, one or

**[03:10]** really giving an agent, you know, one or

**[03:10]** really giving an agent, you know, one or two sentences describing what you want

**[03:11]** two sentences describing what you want

**[03:11]** two sentences describing what you want it to do. It goes off and works for 5 10

**[03:14]** it to do. It goes off and works for 5 10

**[03:14]** it to do. It goes off and works for 5 10 15 minutes on its own and then comes

**[03:16]** 15 minutes on its own and then comes

**[03:16]** 15 minutes on its own and then comes back to you with a solution. This is a

**[03:18]** back to you with a solution. This is a

**[03:18]** back to you with a solution. This is a much more powerful way of working. You

**[03:19]** much more powerful way of working. You

**[03:19]** much more powerful way of working. You can get a lot done. Uh you can send off

**[03:21]** can get a lot done. Uh you can send off

**[03:21]** can get a lot done. Uh you can send off multiple agents at once. Um you know,

**[03:24]** multiple agents at once. Um you know,

**[03:24]** multiple agents at once. Um you know, you can focus on communicating with your

**[03:26]** you can focus on communicating with your

**[03:26]** you can focus on communicating with your co-workers or goofing off on Reddit

**[03:28]** co-workers or goofing off on Reddit

**[03:28]** co-workers or goofing off on Reddit while these agents are are working for

**[03:30]** while these agents are are working for

**[03:30]** while these agents are are working for you. Um, and it's uh it's just it's a

**[03:33]** you. Um, and it's uh it's just it's a

**[03:33]** you. Um, and it's uh it's just it's a it's a very different way of working,

**[03:34]** it's a very different way of working,

**[03:34]** it's a very different way of working, but it's a much more powerful way of

**[03:35]** but it's a much more powerful way of

**[03:35]** but it's a much more powerful way of working.

**[03:37]** working.

**[03:37]** working. Uh, so I want to talk a little bit about

**[03:39]** Uh, so I want to talk a little bit about

**[03:39]** Uh, so I want to talk a little bit about how these agents work under the hood. I

**[03:41]** how these agents work under the hood. I

**[03:41]** how these agents work under the hood. I feel like uh once you understand what's

**[03:43]** feel like uh once you understand what's

**[03:43]** feel like uh once you understand what's happening under the surface, uh, it

**[03:45]** happening under the surface, uh, it

**[03:45]** happening under the surface, uh, it really helps you build an intuition for

**[03:47]** really helps you build an intuition for

**[03:47]** really helps you build an intuition for how to use agents effectively.

**[03:50]** how to use agents effectively.

**[03:50]** how to use agents effectively. Uh, and at its core, um, an agent is

**[03:52]** Uh, and at its core, um, an agent is

**[03:52]** Uh, and at its core, um, an agent is this loop between a large language model

**[03:54]** this loop between a large language model

**[03:54]** this loop between a large language model and the and the external world. So, uh,

**[03:57]** and the and the external world. So, uh,

**[03:57]** and the and the external world. So, uh, the large language model kind of serves

**[03:58]** the large language model kind of serves

**[03:58]** the large language model kind of serves as the brain. Uh and then we have to


### [04:00 - 05:00]

**[04:00]** as the brain. Uh and then we have to

**[04:00]** as the brain. Uh and then we have to repeatedly take actions in the external

**[04:02]** repeatedly take actions in the external

**[04:02]** repeatedly take actions in the external world, get some kind of feedback from

**[04:04]** world, get some kind of feedback from

**[04:04]** world, get some kind of feedback from the world and pass that back into the

**[04:06]** the world and pass that back into the

**[04:06]** the world and pass that back into the LLM. Um uh so basically at every every

**[04:10]** LLM. Um uh so basically at every every

**[04:10]** LLM. Um uh so basically at every every step of this loop, we're asking the LM

**[04:11]** step of this loop, we're asking the LM

**[04:12]** step of this loop, we're asking the LM what's the next thing you want to do in

**[04:13]** what's the next thing you want to do in

**[04:13]** what's the next thing you want to do in order to get one step closer to your

**[04:14]** order to get one step closer to your

**[04:14]** order to get one step closer to your goal. Uh it might say, okay, I want to

**[04:16]** goal. Uh it might say, okay, I want to

**[04:16]** goal. Uh it might say, okay, I want to read this file. I want to make this

**[04:18]** read this file. I want to make this

**[04:18]** read this file. I want to make this edit. I want to run this command. I want

**[04:19]** edit. I want to run this command. I want

**[04:19]** edit. I want to run this command. I want to look at this web page. uh we go out

**[04:21]** to look at this web page. uh we go out

**[04:21]** to look at this web page. uh we go out and take that action in the real world,

**[04:23]** and take that action in the real world,

**[04:23]** and take that action in the real world, get some kind of output, whether it's

**[04:24]** get some kind of output, whether it's

**[04:24]** get some kind of output, whether it's the contents of a web page, uh or the

**[04:26]** the contents of a web page, uh or the

**[04:26]** the contents of a web page, uh or the output of a command, and then stick that

**[04:28]** output of a command, and then stick that

**[04:28]** output of a command, and then stick that back into the LLM for the next turn of

**[04:30]** back into the LLM for the next turn of

**[04:30]** back into the LLM for the next turn of the loop.

**[04:35]** Uh just to talk a little bit about kind

**[04:35]** Uh just to talk a little bit about kind of the core tools that are at the

**[04:36]** of the core tools that are at the

**[04:36]** of the core tools that are at the agent's disposal. Uh the first one again

**[04:38]** agent's disposal. Uh the first one again

**[04:38]** agent's disposal. Uh the first one again is a is a code editor. Um you might

**[04:41]** is a is a code editor. Um you might

**[04:41]** is a is a code editor. Um you might think this is this is really simple. It

**[04:42]** think this is this is really simple. It

**[04:42]** think this is this is really simple. It actually turns out to be a fairly uh

**[04:44]** actually turns out to be a fairly uh

**[04:44]** actually turns out to be a fairly uh interesting problem. Uh the naive

**[04:46]** interesting problem. Uh the naive

**[04:46]** interesting problem. Uh the naive solution would be to just like give the

**[04:47]** solution would be to just like give the

**[04:47]** solution would be to just like give the old file to the LLM uh and then have it

**[04:50]** old file to the LLM uh and then have it

**[04:50]** old file to the LLM uh and then have it output the entire new file. That's not a

**[04:52]** output the entire new file. That's not a

**[04:52]** output the entire new file. That's not a very efficient way to work though. If

**[04:53]** very efficient way to work though. If

**[04:53]** very efficient way to work though. If you've got a thousand line uh thousand

**[04:55]** you've got a thousand line uh thousand

**[04:55]** you've got a thousand line uh thousand line of thousands of lines of code and

**[04:57]** line of thousands of lines of code and

**[04:57]** line of thousands of lines of code and you want to just change one line, uh

**[04:59]** you want to just change one line, uh

**[04:59]** you want to just change one line, uh you're going to waste a lot of tokens


### [05:00 - 06:00]

**[05:01]** you're going to waste a lot of tokens

**[05:01]** you're going to waste a lot of tokens printing out all the lines that are

**[05:02]** printing out all the lines that are

**[05:02]** printing out all the lines that are staying the same. So most uh

**[05:04]** staying the same. So most uh

**[05:04]** staying the same. So most uh contemporary um agents use uh like a a

**[05:08]** contemporary um agents use uh like a a

**[05:08]** contemporary um agents use uh like a a find and replace type editor or a diff

**[05:09]** find and replace type editor or a diff

**[05:10]** find and replace type editor or a diff based editor to allow the LLM to just

**[05:12]** based editor to allow the LLM to just

**[05:12]** based editor to allow the LLM to just make tactical edits inside the file.

**[05:14]** make tactical edits inside the file.

**[05:14]** make tactical edits inside the file. Uh, a lot of times they'll also provide

**[05:17]** Uh, a lot of times they'll also provide

**[05:17]** Uh, a lot of times they'll also provide like an abst ab ab ab ab ab ab ab ab ab

**[05:17]** like an abst ab ab ab ab ab ab ab ab ab

**[05:17]** like an abst ab ab ab ab ab ab ab ab ab ab ab ab ab ab ab ab ab ab ab ab ab ab

**[05:18]** ab ab ab ab ab ab ab ab ab ab ab ab ab ab ab ab ab abstract syntax tree or some

**[05:19]** ab ab ab ab abstract syntax tree or some

**[05:19]** ab ab ab ab abstract syntax tree or some kind of way to allow the agent to

**[05:21]** kind of way to allow the agent to

**[05:21]** kind of way to allow the agent to navigate the codebase more effectively.

**[05:24]** navigate the codebase more effectively.

**[05:24]** navigate the codebase more effectively. Uh next up is the terminal and again you

**[05:26]** Uh next up is the terminal and again you

**[05:26]** Uh next up is the terminal and again you would think text in text out should be

**[05:28]** would think text in text out should be

**[05:28]** would think text in text out should be pretty simple but there are a lot of

**[05:29]** pretty simple but there are a lot of

**[05:29]** pretty simple but there are a lot of questions that pop up here. You know

**[05:31]** questions that pop up here. You know

**[05:31]** questions that pop up here. You know what do you do when there's a longunning

**[05:32]** what do you do when there's a longunning

**[05:32]** what do you do when there's a longunning command that has no standard out for a

**[05:34]** command that has no standard out for a

**[05:34]** command that has no standard out for a long time. Do you kill it? Do you let

**[05:36]** long time. Do you kill it? Do you let

**[05:36]** long time. Do you kill it? Do you let the LLM wait? Uh what happens if you

**[05:38]** the LLM wait? Uh what happens if you

**[05:38]** the LLM wait? Uh what happens if you want to run multiple commands in

**[05:39]** want to run multiple commands in

**[05:39]** want to run multiple commands in parallel? Run commands in the

**[05:40]** parallel? Run commands in the

**[05:40]** parallel? Run commands in the background. Maybe you want to start a

**[05:41]** background. Maybe you want to start a

**[05:41]** background. Maybe you want to start a server and then run curl against that

**[05:43]** server and then run curl against that

**[05:43]** server and then run curl against that server. Uh lots of really interesting uh

**[05:45]** server. Uh lots of really interesting uh

**[05:45]** server. Uh lots of really interesting uh problems that crop up uh when you have

**[05:47]** problems that crop up uh when you have

**[05:47]** problems that crop up uh when you have an agent interacting with the terminal.

**[05:50]** an agent interacting with the terminal.

**[05:50]** an agent interacting with the terminal. Uh and then probably the most

**[05:52]** Uh and then probably the most

**[05:52]** Uh and then probably the most complicated tool is the web browser.

**[05:53]** complicated tool is the web browser.

**[05:53]** complicated tool is the web browser. Again, there's a naive solution here

**[05:55]** Again, there's a naive solution here

**[05:55]** Again, there's a naive solution here where you just uh the agent just gives

**[05:57]** where you just uh the agent just gives

**[05:57]** where you just uh the agent just gives you a URL and you give it a bunch of

**[05:58]** you a URL and you give it a bunch of

**[05:58]** you a URL and you give it a bunch of HTML. Um that's uh very expensive


### [06:00 - 07:00]

**[06:02]** HTML. Um that's uh very expensive

**[06:02]** HTML. Um that's uh very expensive because there's a bunch of croft inside

**[06:03]** because there's a bunch of croft inside

**[06:03]** because there's a bunch of croft inside that HTML that the the LLM doesn't

**[06:05]** that HTML that the the LLM doesn't

**[06:05]** that HTML that the the LLM doesn't really need to see. uh we've had a lot

**[06:07]** really need to see. uh we've had a lot

**[06:07]** really need to see. uh we've had a lot of luck passing it uh accessibility

**[06:08]** of luck passing it uh accessibility

**[06:08]** of luck passing it uh accessibility trees or converting to markdown and

**[06:10]** trees or converting to markdown and

**[06:10]** trees or converting to markdown and passing that to the LLM

**[06:12]** passing that to the LLM

**[06:12]** passing that to the LLM um or allowing the LLM to maybe scroll

**[06:14]** um or allowing the LLM to maybe scroll

**[06:14]** um or allowing the LLM to maybe scroll through the web page if there's a ton of

**[06:15]** through the web page if there's a ton of

**[06:15]** through the web page if there's a ton of content there. Um and then also if you

**[06:18]** content there. Um and then also if you

**[06:18]** content there. Um and then also if you start to add interaction things get even

**[06:20]** start to add interaction things get even

**[06:20]** start to add interaction things get even more complicated. Uh you can let the LLM

**[06:22]** more complicated. Uh you can let the LLM

**[06:22]** more complicated. Uh you can let the LLM uh write JavaScript against the page or

**[06:25]** uh write JavaScript against the page or

**[06:25]** uh write JavaScript against the page or we've actually had a lot of luck

**[06:26]** we've actually had a lot of luck

**[06:26]** we've actually had a lot of luck basically giving it a screenshot of the

**[06:28]** basically giving it a screenshot of the

**[06:28]** basically giving it a screenshot of the page with labeled nodes and it can say

**[06:30]** page with labeled nodes and it can say

**[06:30]** page with labeled nodes and it can say what it wants to click on. Uh this is an

**[06:32]** what it wants to click on. Uh this is an

**[06:32]** what it wants to click on. Uh this is an area of active research. Uh we just had

**[06:34]** area of active research. Uh we just had

**[06:34]** area of active research. Uh we just had a contribution about a month ago that

**[06:36]** a contribution about a month ago that

**[06:36]** a contribution about a month ago that doubled our accuracy on web browsing. Uh

**[06:38]** doubled our accuracy on web browsing. Uh

**[06:38]** doubled our accuracy on web browsing. Uh I would say this is uh this is

**[06:40]** I would say this is uh this is

**[06:40]** I would say this is uh this is definitely a space to watch.

**[06:43]** definitely a space to watch.

**[06:43]** definitely a space to watch. Uh and then I also want to talk about

**[06:44]** Uh and then I also want to talk about

**[06:44]** Uh and then I also want to talk about about sandboxing. Uh this is a really

**[06:46]** about sandboxing. Uh this is a really

**[06:46]** about sandboxing. Uh this is a really important thing for agents because if

**[06:48]** important thing for agents because if

**[06:48]** important thing for agents because if they're going to run autonomously for

**[06:50]** they're going to run autonomously for

**[06:50]** they're going to run autonomously for several minutes on their own without you

**[06:52]** several minutes on their own without you

**[06:52]** several minutes on their own without you watching everything they're doing, you

**[06:53]** watching everything they're doing, you

**[06:53]** watching everything they're doing, you want to make sure that they're not doing

**[06:54]** want to make sure that they're not doing

**[06:54]** want to make sure that they're not doing anything dangerous. Uh and so all of our

**[06:57]** anything dangerous. Uh and so all of our

**[06:57]** anything dangerous. Uh and so all of our agents run inside of a Docker container

**[06:59]** agents run inside of a Docker container

**[06:59]** agents run inside of a Docker container by default. um they're they're totally


### [07:00 - 08:00]

**[07:02]** by default. um they're they're totally

**[07:02]** by default. um they're they're totally separated out from your workstation, so

**[07:03]** separated out from your workstation, so

**[07:03]** separated out from your workstation, so there's no chance of it running RMRF on

**[07:05]** there's no chance of it running RMRF on

**[07:06]** there's no chance of it running RMRF on your home directory. Um increasingly

**[07:08]** your home directory. Um increasingly

**[07:08]** your home directory. Um increasingly though, we're giving agents access to

**[07:11]** though, we're giving agents access to

**[07:11]** though, we're giving agents access to thirdparty APIs, right? So you might

**[07:12]** thirdparty APIs, right? So you might

**[07:12]** thirdparty APIs, right? So you might give it access to a GitHub token or

**[07:14]** give it access to a GitHub token or

**[07:14]** give it access to a GitHub token or access to your AWS account. Super super

**[07:17]** access to your AWS account. Super super

**[07:17]** access to your AWS account. Super super important to make sure that those

**[07:18]** important to make sure that those

**[07:18]** important to make sure that those credentials are tightly scoped and that

**[07:20]** credentials are tightly scoped and that

**[07:20]** credentials are tightly scoped and that you're following uh the principle of

**[07:21]** you're following uh the principle of

**[07:21]** you're following uh the principle of lease privilege as you're granting

**[07:23]** lease privilege as you're granting

**[07:23]** lease privilege as you're granting agents access to do these things.

**[07:27]** agents access to do these things.

**[07:27]** agents access to do these things. All right, I want to move into some best

**[07:29]** All right, I want to move into some best

**[07:29]** All right, I want to move into some best practices.

**[07:31]** practices.

**[07:31]** practices. Uh my my biggest advice for folks who

**[07:33]** Uh my my biggest advice for folks who

**[07:33]** Uh my my biggest advice for folks who are just getting started is to start

**[07:34]** are just getting started is to start

**[07:34]** are just getting started is to start small. Um the best tasks are things that

**[07:38]** small. Um the best tasks are things that

**[07:38]** small. Um the best tasks are things that can be completed pretty quickly. You

**[07:39]** can be completed pretty quickly. You

**[07:39]** can be completed pretty quickly. You know, a single commit uh where there's a

**[07:41]** know, a single commit uh where there's a

**[07:41]** know, a single commit uh where there's a clear definition of done. You know, you

**[07:43]** clear definition of done. You know, you

**[07:43]** clear definition of done. You know, you want the agent to be able to verify,

**[07:44]** want the agent to be able to verify,

**[07:44]** want the agent to be able to verify, okay, the tests are passing, I must have

**[07:46]** okay, the tests are passing, I must have

**[07:46]** okay, the tests are passing, I must have done it correctly. Um or, you know, the

**[07:48]** done it correctly. Um or, you know, the

**[07:48]** done it correctly. Um or, you know, the merge conflicts have been solved, etc.

**[07:50]** merge conflicts have been solved, etc.

**[07:50]** merge conflicts have been solved, etc. Um and tasks that are easy for you as an

**[07:52]** Um and tasks that are easy for you as an

**[07:52]** Um and tasks that are easy for you as an engineer to verify uh were done

**[07:54]** engineer to verify uh were done

**[07:54]** engineer to verify uh were done completely and correctly. Um I like to

**[07:57]** completely and correctly. Um I like to

**[07:57]** completely and correctly. Um I like to tell people to start with small chores.

**[07:58]** tell people to start with small chores.

**[07:58]** tell people to start with small chores. Uh very frequently you might have a poll


### [08:00 - 09:00]

**[08:00]** Uh very frequently you might have a poll

**[08:00]** Uh very frequently you might have a poll request where there's, you know, one

**[08:01]** request where there's, you know, one

**[08:01]** request where there's, you know, one test that's failing or there's some lint

**[08:03]** test that's failing or there's some lint

**[08:03]** test that's failing or there's some lint errors or there's merge conflicts. Uh

**[08:05]** errors or there's merge conflicts. Uh

**[08:05]** errors or there's merge conflicts. Uh bits of toil that you don't really like

**[08:07]** bits of toil that you don't really like

**[08:07]** bits of toil that you don't really like doing as a developer. Those are great

**[08:08]** doing as a developer. Those are great

**[08:08]** doing as a developer. Those are great tasks to just shove off to the AI.

**[08:10]** tasks to just shove off to the AI.

**[08:10]** tasks to just shove off to the AI. They're tend to be tend to be very rote.

**[08:11]** They're tend to be tend to be very rote.

**[08:12]** They're tend to be tend to be very rote. Uh the AI does does them very well. Um

**[08:14]** Uh the AI does does them very well. Um

**[08:14]** Uh the AI does does them very well. Um but as your intuition grows here, as you

**[08:16]** but as your intuition grows here, as you

**[08:16]** but as your intuition grows here, as you get used to working with an agent,

**[08:17]** get used to working with an agent,

**[08:18]** get used to working with an agent, you'll find that you can give it bigger

**[08:19]** you'll find that you can give it bigger

**[08:19]** you'll find that you can give it bigger and bigger tasks. Uh you'll you'll

**[08:20]** and bigger tasks. Uh you'll you'll

**[08:20]** and bigger tasks. Uh you'll you'll understand how to communicate with the

**[08:22]** understand how to communicate with the

**[08:22]** understand how to communicate with the agent effectively. Um, and I would say

**[08:24]** agent effectively. Um, and I would say

**[08:24]** agent effectively. Um, and I would say for for me, for my co-founders, and for

**[08:26]** for for me, for my co-founders, and for

**[08:26]** for for me, for my co-founders, and for our for our biggest power users, uh, for

**[08:28]** our for our biggest power users, uh, for

**[08:28]** our for our biggest power users, uh, for me, like 90% of my code now goes through

**[08:30]** me, like 90% of my code now goes through

**[08:30]** me, like 90% of my code now goes through the agent, and it's only maybe 10% of

**[08:32]** the agent, and it's only maybe 10% of

**[08:32]** the agent, and it's only maybe 10% of the time that I have to drop back into

**[08:34]** the time that I have to drop back into

**[08:34]** the time that I have to drop back into my IDE and kind of get my hands dirty in

**[08:36]** my IDE and kind of get my hands dirty in

**[08:36]** my IDE and kind of get my hands dirty in the codebase again.

**[08:39]** the codebase again.

**[08:39]** the codebase again. Uh, being very clear with the agent

**[08:41]** Uh, being very clear with the agent

**[08:41]** Uh, being very clear with the agent about what you want is super important.

**[08:43]** about what you want is super important.

**[08:43]** about what you want is super important. Uh, I specifically like to say, you

**[08:45]** Uh, I specifically like to say, you

**[08:45]** Uh, I specifically like to say, you know, you need to tell it not just what

**[08:46]** know, you need to tell it not just what

**[08:46]** know, you need to tell it not just what you want, but you need to tell it how

**[08:48]** you want, but you need to tell it how

**[08:48]** you want, but you need to tell it how you want it to do it. You know, mention

**[08:49]** you want it to do it. You know, mention

**[08:49]** you want it to do it. You know, mention specific frameworks that you want it to

**[08:50]** specific frameworks that you want it to

**[08:50]** specific frameworks that you want it to use. Uh if you wanted to do like a

**[08:52]** use. Uh if you wanted to do like a

**[08:52]** use. Uh if you wanted to do like a test-driven development strategy, tell

**[08:54]** test-driven development strategy, tell

**[08:54]** test-driven development strategy, tell it that. Um mention any specific files

**[08:57]** it that. Um mention any specific files

**[08:57]** it that. Um mention any specific files or function names that it can that it

**[08:58]** or function names that it can that it

**[08:58]** or function names that it can that it can go for. Um this not only uh helps it


### [09:00 - 10:00]

**[09:02]** can go for. Um this not only uh helps it

**[09:02]** can go for. Um this not only uh helps it be more accurate and uh you know more

**[09:04]** be more accurate and uh you know more

**[09:04]** be more accurate and uh you know more clear as to what exactly you want the

**[09:05]** clear as to what exactly you want the

**[09:06]** clear as to what exactly you want the output to be um it also makes it go

**[09:07]** output to be um it also makes it go

**[09:08]** output to be um it also makes it go faster, right? It doesn't have to spend

**[09:09]** faster, right? It doesn't have to spend

**[09:09]** faster, right? It doesn't have to spend as long exploring the codebase if you

**[09:11]** as long exploring the codebase if you

**[09:11]** as long exploring the codebase if you tell it I want you to edit this exact

**[09:12]** tell it I want you to edit this exact

**[09:12]** tell it I want you to edit this exact file. Um this can save you a bunch of

**[09:15]** file. Um this can save you a bunch of

**[09:15]** file. Um this can save you a bunch of time and energy and it can save uh a lot

**[09:18]** time and energy and it can save uh a lot

**[09:18]** time and energy and it can save uh a lot of a lot of tokens, a lot of actual like

**[09:19]** of a lot of tokens, a lot of actual like

**[09:19]** of a lot of tokens, a lot of actual like inference costs.

**[09:22]** inference costs.

**[09:22]** inference costs. Uh, I also like to remind folks that in

**[09:24]** Uh, I also like to remind folks that in

**[09:24]** Uh, I also like to remind folks that in an AIdriven development world, code is

**[09:26]** an AIdriven development world, code is

**[09:26]** an AIdriven development world, code is cheap. Um, you can throw code away. You

**[09:28]** cheap. Um, you can throw code away. You

**[09:28]** cheap. Um, you can throw code away. You can you can experiment and prototype.

**[09:30]** can you can experiment and prototype.

**[09:30]** can you can experiment and prototype. Uh, I love if I if I have an idea, like

**[09:32]** Uh, I love if I if I have an idea, like

**[09:32]** Uh, I love if I if I have an idea, like on my walk to work, I'll just like uh,

**[09:35]** on my walk to work, I'll just like uh,

**[09:35]** on my walk to work, I'll just like uh, you know, tell open hands with my voice,

**[09:37]** you know, tell open hands with my voice,

**[09:37]** you know, tell open hands with my voice, like do X, Y, and Z, and then when I get

**[09:39]** like do X, Y, and Z, and then when I get

**[09:39]** like do X, Y, and Z, and then when I get to work, I'll I'll have a PR waiting for

**[09:41]** to work, I'll I'll have a PR waiting for

**[09:41]** to work, I'll I'll have a PR waiting for me. 50% of the time, I'll just throw it

**[09:43]** me. 50% of the time, I'll just throw it

**[09:43]** me. 50% of the time, I'll just throw it away. It didn't really work. 50% of the

**[09:45]** away. It didn't really work. 50% of the

**[09:45]** away. It didn't really work. 50% of the time it looks great, and I just merge

**[09:46]** time it looks great, and I just merge

**[09:46]** time it looks great, and I just merge it, and it's and it's awesome. Um, it's

**[09:49]** it, and it's and it's awesome. Um, it's

**[09:49]** it, and it's and it's awesome. Um, it's uh it's really fun to be able to just

**[09:50]** uh it's really fun to be able to just

**[09:50]** uh it's really fun to be able to just rapidly prototype using AIdriven

**[09:52]** rapidly prototype using AIdriven

**[09:52]** rapidly prototype using AIdriven development. Um, and I would also say,

**[09:55]** development. Um, and I would also say,

**[09:55]** development. Um, and I would also say, you know, if you if you try to try to

**[09:58]** you know, if you if you try to try to

**[09:58]** you know, if you if you try to try to work with the agent on a particular task

**[09:59]** work with the agent on a particular task

**[09:59]** work with the agent on a particular task and it gets it wrong, maybe it's close


### [10:00 - 11:00]

**[10:01]** and it gets it wrong, maybe it's close

**[10:01]** and it gets it wrong, maybe it's close and you can just keep iterating within

**[10:02]** and you can just keep iterating within

**[10:02]** and you can just keep iterating within the same conversation and has already

**[10:04]** the same conversation and has already

**[10:04]** the same conversation and has already built up some context. If it's way off

**[10:06]** built up some context. If it's way off

**[10:06]** built up some context. If it's way off though, just throw away that work. Start

**[10:08]** though, just throw away that work. Start

**[10:08]** though, just throw away that work. Start fresh with a new prompt based on uh what

**[10:10]** fresh with a new prompt based on uh what

**[10:10]** fresh with a new prompt based on uh what you learned from the last one. Um, it's

**[10:12]** you learned from the last one. Um, it's

**[10:12]** you learned from the last one. Um, it's really really uh I think uh it's a new

**[10:15]** really really uh I think uh it's a new

**[10:15]** really really uh I think uh it's a new new sort of muscle memory you have to

**[10:16]** new sort of muscle memory you have to

**[10:16]** new sort of muscle memory you have to develop to just throw things away.

**[10:18]** develop to just throw things away.

**[10:18]** develop to just throw things away. Sometimes it's uh hard to throw away

**[10:21]** Sometimes it's uh hard to throw away

**[10:21]** Sometimes it's uh hard to throw away tens of lines tens of thousands of lines

**[10:23]** tens of lines tens of thousands of lines

**[10:23]** tens of lines tens of thousands of lines of code that uh have been generated

**[10:25]** of code that uh have been generated

**[10:25]** of code that uh have been generated because you're used to that being a very

**[10:26]** because you're used to that being a very

**[10:26]** because you're used to that being a very expensive uh bunch of code. Uh these

**[10:28]** expensive uh bunch of code. Uh these

**[10:28]** expensive uh bunch of code. Uh these days it's it's very easy to kind of just

**[10:30]** days it's it's very easy to kind of just

**[10:30]** days it's it's very easy to kind of just start from scratch. Again,

**[10:34]** start from scratch. Again,

**[10:34]** start from scratch. Again, this is probably the most important bit

**[10:35]** this is probably the most important bit

**[10:35]** this is probably the most important bit of advice I can give folks. Uh you need

**[10:37]** of advice I can give folks. Uh you need

**[10:38]** of advice I can give folks. Uh you need to review the code that the AI writes.

**[10:40]** to review the code that the AI writes.

**[10:40]** to review the code that the AI writes. Uh I've seen more than one organization

**[10:42]** Uh I've seen more than one organization

**[10:42]** Uh I've seen more than one organization run into trouble uh thinking that they

**[10:44]** run into trouble uh thinking that they

**[10:44]** run into trouble uh thinking that they could just vibe code their way to a

**[10:45]** could just vibe code their way to a

**[10:45]** could just vibe code their way to a production application uh and just you

**[10:47]** production application uh and just you

**[10:47]** production application uh and just you know automatically merging everything

**[10:49]** know automatically merging everything

**[10:49]** know automatically merging everything that came out of the AI. Um but uh if

**[10:53]** that came out of the AI. Um but uh if

**[10:53]** that came out of the AI. Um but uh if you just you know don't review anything

**[10:54]** you just you know don't review anything

**[10:54]** you just you know don't review anything you'll find that your codebase just

**[10:56]** you'll find that your codebase just

**[10:56]** you'll find that your codebase just grows and grows with this tech debt.

**[10:57]** grows and grows with this tech debt.

**[10:57]** grows and grows with this tech debt. You'll find duplicate code everywhere.

**[10:59]** You'll find duplicate code everywhere.


### [11:00 - 12:00]

**[11:00]** You'll find duplicate code everywhere. Uh things get out of hand very quickly.

**[11:01]** Uh things get out of hand very quickly.

**[11:02]** Uh things get out of hand very quickly. Uh so make sure you're reviewing the

**[11:03]** Uh so make sure you're reviewing the

**[11:03]** Uh so make sure you're reviewing the code that it outputs and make sure

**[11:04]** code that it outputs and make sure

**[11:04]** code that it outputs and make sure you're pulling the code and running it

**[11:05]** you're pulling the code and running it

**[11:05]** you're pulling the code and running it on your workstation or running it inside

**[11:07]** on your workstation or running it inside

**[11:07]** on your workstation or running it inside of an ephemeral environment. uh just to

**[11:10]** of an ephemeral environment. uh just to

**[11:10]** of an ephemeral environment. uh just to make sure that you know the agent has

**[11:11]** make sure that you know the agent has

**[11:11]** make sure that you know the agent has actually solved the problem that you

**[11:12]** actually solved the problem that you

**[11:12]** actually solved the problem that you asked it to solve.

**[11:15]** asked it to solve.

**[11:15]** asked it to solve. Uh and I like to say you know trust but

**[11:17]** Uh and I like to say you know trust but

**[11:17]** Uh and I like to say you know trust but verify. You know as you work with agents

**[11:18]** verify. You know as you work with agents

**[11:18]** verify. You know as you work with agents over time you'll build an intuition for

**[11:20]** over time you'll build an intuition for

**[11:20]** over time you'll build an intuition for for what they do well and what they

**[11:21]** for what they do well and what they

**[11:21]** for what they do well and what they don't do well and you can generally

**[11:23]** don't do well and you can generally

**[11:23]** don't do well and you can generally trust them to to um you know operate the

**[11:26]** trust them to to um you know operate the

**[11:26]** trust them to to um you know operate the same way today that they did yesterday.

**[11:28]** same way today that they did yesterday.

**[11:28]** same way today that they did yesterday. Um but you really you really do need a

**[11:30]** Um but you really you really do need a

**[11:30]** Um but you really you really do need a human in the loop. Um, you know, one of

**[11:32]** human in the loop. Um, you know, one of

**[11:32]** human in the loop. Um, you know, one of our big learnings, uh, with Open Hands,

**[11:34]** our big learnings, uh, with Open Hands,

**[11:34]** our big learnings, uh, with Open Hands, in the early days, if you opened up a

**[11:36]** in the early days, if you opened up a

**[11:36]** in the early days, if you opened up a poll poll request with Open Hands, uh,

**[11:39]** poll poll request with Open Hands, uh,

**[11:39]** poll poll request with Open Hands, uh, that that poll request would show up as

**[11:41]** that that poll request would show up as

**[11:41]** that that poll request would show up as owned by Open Hands, it would be the

**[11:42]** owned by Open Hands, it would be the

**[11:42]** owned by Open Hands, it would be the little hands logo uh, next to the poll

**[11:44]** little hands logo uh, next to the poll

**[11:44]** little hands logo uh, next to the poll request. Uh, and that caused two

**[11:46]** request. Uh, and that caused two

**[11:46]** request. Uh, and that caused two problems. One, it meant that the human

**[11:48]** problems. One, it meant that the human

**[11:48]** problems. One, it meant that the human who had triggered that poll request

**[11:50]** who had triggered that poll request

**[11:50]** who had triggered that poll request could then approve it and basically

**[11:51]** could then approve it and basically

**[11:51]** could then approve it and basically bypass our whole code review system. You

**[11:53]** bypass our whole code review system. You

**[11:53]** bypass our whole code review system. You didn't need a second human in the loop

**[11:54]** didn't need a second human in the loop

**[11:54]** didn't need a second human in the loop to uh, before merging. Uh, and two,

**[11:57]** to uh, before merging. Uh, and two,

**[11:57]** to uh, before merging. Uh, and two, often times those poll requests would

**[11:58]** often times those poll requests would

**[11:58]** often times those poll requests would just languish. uh nobody would really


### [12:00 - 13:00]

**[12:01]** just languish. uh nobody would really

**[12:01]** just languish. uh nobody would really take ownership for them. Uh if there was

**[12:02]** take ownership for them. Uh if there was

**[12:02]** take ownership for them. Uh if there was like a failing unit test, nobody was

**[12:04]** like a failing unit test, nobody was

**[12:04]** like a failing unit test, nobody was like jumping in to make sure the test

**[12:06]** like jumping in to make sure the test

**[12:06]** like jumping in to make sure the test passed. Um and those they would just

**[12:08]** passed. Um and those they would just

**[12:08]** passed. Um and those they would just kind of like sit there and not get

**[12:09]** kind of like sit there and not get

**[12:09]** kind of like sit there and not get merged or if they did get merged and

**[12:11]** merged or if they did get merged and

**[12:11]** merged or if they did get merged and something went wrong, the code didn't

**[12:12]** something went wrong, the code didn't

**[12:12]** something went wrong, the code didn't actually work. We didn't really know who

**[12:13]** actually work. We didn't really know who

**[12:14]** actually work. We didn't really know who to go to and be like, you know, who

**[12:15]** to go to and be like, you know, who

**[12:15]** to go to and be like, you know, who caused this? There was nobody we could

**[12:16]** caused this? There was nobody we could

**[12:16]** caused this? There was nobody we could hold accountable for that breakage. Um

**[12:19]** hold accountable for that breakage. Um

**[12:19]** hold accountable for that breakage. Um and so now if you open up a poll request

**[12:20]** and so now if you open up a poll request

**[12:20]** and so now if you open up a poll request with open hands, your face is on that

**[12:22]** with open hands, your face is on that

**[12:22]** with open hands, your face is on that poll request. You're responsible for

**[12:23]** poll request. You're responsible for

**[12:23]** poll request. You're responsible for getting it merged. You're responsible

**[12:25]** getting it merged. You're responsible

**[12:25]** getting it merged. You're responsible for any breakage it might cause down the

**[12:27]** for any breakage it might cause down the

**[12:27]** for any breakage it might cause down the line. Cool.

**[12:30]** line. Cool.

**[12:30]** line. Cool. And then uh I do want to just close just

**[12:32]** And then uh I do want to just close just

**[12:32]** And then uh I do want to just close just by going through a handful of use cases.

**[12:34]** by going through a handful of use cases.

**[12:34]** by going through a handful of use cases. Uh this is always kind of a tricky topic

**[12:36]** Uh this is always kind of a tricky topic

**[12:36]** Uh this is always kind of a tricky topic because agents are great generalists.

**[12:37]** because agents are great generalists.

**[12:37]** because agents are great generalists. They can they can hypothetically do

**[12:39]** They can they can hypothetically do

**[12:39]** They can they can hypothetically do anything as as long as you kind of like

**[12:41]** anything as as long as you kind of like

**[12:41]** anything as as long as you kind of like break things down into bite-sized steps

**[12:43]** break things down into bite-sized steps

**[12:43]** break things down into bite-sized steps that they can take on. Um but in that in

**[12:45]** that they can take on. Um but in that in

**[12:45]** that they can take on. Um but in that in that um in the spirit of starting small,

**[12:48]** that um in the spirit of starting small,

**[12:48]** that um in the spirit of starting small, I think there are a bunch of use cases

**[12:49]** I think there are a bunch of use cases

**[12:50]** I think there are a bunch of use cases that are like really great day one use

**[12:52]** that are like really great day one use

**[12:52]** that are like really great day one use cases for agents. My favorite is

**[12:54]** cases for agents. My favorite is

**[12:54]** cases for agents. My favorite is resolving merge conflicts. This is like

**[12:55]** resolving merge conflicts. This is like

**[12:55]** resolving merge conflicts. This is like the biggest chore as a part of my job.

**[12:57]** the biggest chore as a part of my job.

**[12:57]** the biggest chore as a part of my job. Uh, OpenHands itself is a very

**[12:59]** Uh, OpenHands itself is a very

**[12:59]** Uh, OpenHands itself is a very fastmoving codebase. Uh, I say there's


### [13:00 - 14:00]

**[13:02]** fastmoving codebase. Uh, I say there's

**[13:02]** fastmoving codebase. Uh, I say there's probably no PR that I make that uh, I

**[13:04]** probably no PR that I make that uh, I

**[13:04]** probably no PR that I make that uh, I get away with zero merge conflicts. Um,

**[13:06]** get away with zero merge conflicts. Um,

**[13:06]** get away with zero merge conflicts. Um, and I love just being able to jump in

**[13:07]** and I love just being able to jump in

**[13:07]** and I love just being able to jump in and say at Open Hands, fix the merge

**[13:09]** and say at Open Hands, fix the merge

**[13:09]** and say at Open Hands, fix the merge conflicts on this PR. Uh, it comes in

**[13:11]** conflicts on this PR. Uh, it comes in

**[13:11]** conflicts on this PR. Uh, it comes in and, you know, it's such a rope task.

**[13:13]** and, you know, it's such a rope task.

**[13:13]** and, you know, it's such a rope task. It's usually very obvious, you know,

**[13:14]** It's usually very obvious, you know,

**[13:14]** It's usually very obvious, you know, what changed before, what changed in

**[13:16]** what changed before, what changed in

**[13:16]** what changed before, what changed in this PR, what's the intention behind

**[13:18]** this PR, what's the intention behind

**[13:18]** this PR, what's the intention behind those changes? And Open Hands knocks

**[13:19]** those changes? And Open Hands knocks

**[13:19]** those changes? And Open Hands knocks this out, you know, 99% of the time.

**[13:23]** this out, you know, 99% of the time.

**[13:23]** this out, you know, 99% of the time. Uh addressing PR feedback is also a

**[13:25]** Uh addressing PR feedback is also a

**[13:25]** Uh addressing PR feedback is also a favorite. Uh this one's great because

**[13:27]** favorite. Uh this one's great because

**[13:27]** favorite. Uh this one's great because somebody else has already taken the time

**[13:29]** somebody else has already taken the time

**[13:29]** somebody else has already taken the time to clearly articulate what they want

**[13:31]** to clearly articulate what they want

**[13:31]** to clearly articulate what they want changed and all you have to do is say at

**[13:33]** changed and all you have to do is say at

**[13:33]** changed and all you have to do is say at open hands do what that guy said. Uh and

**[13:35]** open hands do what that guy said. Uh and

**[13:35]** open hands do what that guy said. Uh and again like you can see in this example

**[13:37]** again like you can see in this example

**[13:37]** again like you can see in this example uh open hands did exactly what this

**[13:39]** uh open hands did exactly what this

**[13:39]** uh open hands did exactly what this person wanted. I don't know react super

**[13:40]** person wanted. I don't know react super

**[13:40]** person wanted. I don't know react super well and uh our front end engineer was

**[13:43]** well and uh our front end engineer was

**[13:43]** well and uh our front end engineer was like do x y and z and he mentioned a

**[13:44]** like do x y and z and he mentioned a

**[13:44]** like do x y and z and he mentioned a whole bunch of buzzwords that I don't I

**[13:46]** whole bunch of buzzwords that I don't I

**[13:46]** whole bunch of buzzwords that I don't I don't know. Open hands knew all of it

**[13:48]** don't know. Open hands knew all of it

**[13:48]** don't know. Open hands knew all of it and uh was able to address his feedback

**[13:50]** and uh was able to address his feedback

**[13:50]** and uh was able to address his feedback exactly how he wanted.

**[13:53]** exactly how he wanted.

**[13:53]** exactly how he wanted. uh fixing quick little bugs. Um you

**[13:55]** uh fixing quick little bugs. Um you

**[13:55]** uh fixing quick little bugs. Um you know, you can see in this example, we

**[13:56]** know, you can see in this example, we

**[13:56]** know, you can see in this example, we had an input uh that, you know, was a

**[13:58]** had an input uh that, you know, was a

**[13:58]** had an input uh that, you know, was a text input. Should have been a number

**[13:59]** text input. Should have been a number


### [14:00 - 15:00]

**[14:00]** text input. Should have been a number input. Uh if I wasn't lazy, I could have

**[14:02]** input. Uh if I wasn't lazy, I could have

**[14:02]** input. Uh if I wasn't lazy, I could have like dug through my codebase, found the

**[14:03]** like dug through my codebase, found the

**[14:03]** like dug through my codebase, found the right file. Um but it was really easy

**[14:05]** right file. Um but it was really easy

**[14:06]** right file. Um but it was really easy for me to just like quickly I think I

**[14:07]** for me to just like quickly I think I

**[14:07]** for me to just like quickly I think I did this one from directly inside of

**[14:09]** did this one from directly inside of

**[14:09]** did this one from directly inside of Slack, uh just add open hands, fix this

**[14:11]** Slack, uh just add open hands, fix this

**[14:11]** Slack, uh just add open hands, fix this thing we were just talking about. Uh and

**[14:13]** thing we were just talking about. Uh and

**[14:14]** thing we were just talking about. Uh and uh it's just, you know, really I don't

**[14:15]** uh it's just, you know, really I don't

**[14:15]** uh it's just, you know, really I don't even have to like fire up my IDE. Um

**[14:18]** even have to like fire up my IDE. Um

**[14:18]** even have to like fire up my IDE. Um it's just it's a really really fun way

**[14:20]** it's just it's a really really fun way

**[14:20]** it's just it's a really really fun way to work.

**[14:22]** to work.

**[14:22]** to work. uh infrastructure changes I really like.

**[14:24]** uh infrastructure changes I really like.

**[14:24]** uh infrastructure changes I really like. Uh usually these involve looking up some

**[14:25]** Uh usually these involve looking up some

**[14:26]** Uh usually these involve looking up some like really esoteric syntax inside of

**[14:28]** like really esoteric syntax inside of

**[14:28]** like really esoteric syntax inside of like the Terraform docs or something

**[14:29]** like the Terraform docs or something

**[14:29]** like the Terraform docs or something like that. Um open hands and you know

**[14:31]** like that. Um open hands and you know

**[14:31]** like that. Um open hands and you know the underlying LLMs tend to just like

**[14:33]** the underlying LLMs tend to just like

**[14:33]** the underlying LLMs tend to just like know uh the right terraform syntax and

**[14:36]** know uh the right terraform syntax and

**[14:36]** know uh the right terraform syntax and if not they can they can look up the

**[14:38]** if not they can they can look up the

**[14:38]** if not they can they can look up the documentation using the browser. Um so

**[14:40]** documentation using the browser. Um so

**[14:40]** documentation using the browser. Um so this stuff is uh is really great.

**[14:41]** this stuff is uh is really great.

**[14:41]** this stuff is uh is really great. Sometimes we'll just get like an out of

**[14:42]** Sometimes we'll just get like an out of

**[14:42]** Sometimes we'll just get like an out of memory exception in Slack and

**[14:44]** memory exception in Slack and

**[14:44]** memory exception in Slack and immediately say okay open hands increase

**[14:46]** immediately say okay open hands increase

**[14:46]** immediately say okay open hands increase the memory.

**[14:48]** the memory.

**[14:48]** the memory. Uh database migrations are another great

**[14:50]** Uh database migrations are another great

**[14:50]** Uh database migrations are another great one. Uh this is one where I find uh I

**[14:52]** one. Uh this is one where I find uh I

**[14:52]** one. Uh this is one where I find uh I often leave best practices behind. I

**[14:54]** often leave best practices behind. I

**[14:54]** often leave best practices behind. I won't put indexes on the right things. I

**[14:56]** won't put indexes on the right things. I

**[14:56]** won't put indexes on the right things. I won't set up foreign keys the right way.

**[14:58]** won't set up foreign keys the right way.

**[14:58]** won't set up foreign keys the right way. Uh the LLM tends to be really great


### [15:00 - 16:00]

**[15:00]** Uh the LLM tends to be really great

**[15:00]** Uh the LLM tends to be really great about following all best practices

**[15:01]** about following all best practices

**[15:01]** about following all best practices around database migrations. So again,

**[15:03]** around database migrations. So again,

**[15:03]** around database migrations. So again, it's kind of like a rote task for

**[15:05]** it's kind of like a rote task for

**[15:05]** it's kind of like a rote task for developers. It's not very fun. Um uh the

**[15:09]** developers. It's not very fun. Um uh the

**[15:09]** developers. It's not very fun. Um uh the LLM's great at it. uh fixing failing

**[15:12]** LLM's great at it. uh fixing failing

**[15:12]** LLM's great at it. uh fixing failing tests uh like on a PR. Uh if you've

**[15:14]** tests uh like on a PR. Uh if you've

**[15:14]** tests uh like on a PR. Uh if you've already got the code 90% of the way

**[15:15]** already got the code 90% of the way

**[15:15]** already got the code 90% of the way there and there's just a unit test

**[15:17]** there and there's just a unit test

**[15:17]** there and there's just a unit test failing because there was a breaking API

**[15:18]** failing because there was a breaking API

**[15:18]** failing because there was a breaking API change, very easy to call in an agent to

**[15:21]** change, very easy to call in an agent to

**[15:21]** change, very easy to call in an agent to just clean up the the failing tests.

**[15:24]** just clean up the the failing tests.

**[15:24]** just clean up the the failing tests. Uh expanding test coverage is another

**[15:26]** Uh expanding test coverage is another

**[15:26]** Uh expanding test coverage is another one I love because uh it's a very um

**[15:28]** one I love because uh it's a very um

**[15:28]** one I love because uh it's a very um safe task, right? As long as the tests

**[15:31]** safe task, right? As long as the tests

**[15:31]** safe task, right? As long as the tests are passing, it's uh generally safe to

**[15:32]** are passing, it's uh generally safe to

**[15:32]** are passing, it's uh generally safe to just merge that. So, if you notice a

**[15:34]** just merge that. So, if you notice a

**[15:34]** just merge that. So, if you notice a spot in your codebase where you're like,

**[15:35]** spot in your codebase where you're like,

**[15:35]** spot in your codebase where you're like, "Hey, we have really low coverage here."

**[15:37]** "Hey, we have really low coverage here."

**[15:37]** "Hey, we have really low coverage here." Just ask uh ask your agent to uh expand

**[15:40]** Just ask uh ask your agent to uh expand

**[15:40]** Just ask uh ask your agent to uh expand your test coverage in that area of the

**[15:41]** your test coverage in that area of the

**[15:41]** your test coverage in that area of the codebase. Uh it's a great quick win uh

**[15:43]** codebase. Uh it's a great quick win uh

**[15:44]** codebase. Uh it's a great quick win uh to make your codebase a little bit

**[15:45]** to make your codebase a little bit

**[15:45]** to make your codebase a little bit safer.

**[15:47]** safer.

**[15:47]** safer. Then, everybody's favorite building apps

**[15:48]** Then, everybody's favorite building apps

**[15:48]** Then, everybody's favorite building apps from scratch. Um you know, I would say

**[15:51]** from scratch. Um you know, I would say

**[15:51]** from scratch. Um you know, I would say if you're shipping production code,

**[15:53]** if you're shipping production code,

**[15:53]** if you're shipping production code, again, don't just like vibe code your

**[15:54]** again, don't just like vibe code your

**[15:54]** again, don't just like vibe code your way to a production application. Uh but

**[15:56]** way to a production application. Uh but

**[15:56]** way to a production application. Uh but we're finding increasingly internally at

**[15:58]** we're finding increasingly internally at

**[15:58]** we're finding increasingly internally at our company, a lot of times there's like


### [16:00 - 17:00]

**[16:00]** our company, a lot of times there's like

**[16:00]** our company, a lot of times there's like a little internal app we want to build.

**[16:02]** a little internal app we want to build.

**[16:02]** a little internal app we want to build. Uh like for instance, we built a way to

**[16:04]** Uh like for instance, we built a way to

**[16:04]** Uh like for instance, we built a way to uh debug openhand trajectories, debug

**[16:06]** uh debug openhand trajectories, debug

**[16:06]** uh debug openhand trajectories, debug openhand sessions. Um uh we built like a

**[16:09]** openhand sessions. Um uh we built like a

**[16:09]** openhand sessions. Um uh we built like a whole web application that since it's

**[16:11]** whole web application that since it's

**[16:11]** whole web application that since it's just an internal application, we can

**[16:12]** just an internal application, we can

**[16:12]** just an internal application, we can vibe code it a little bit. We don't

**[16:14]** vibe code it a little bit. We don't

**[16:14]** vibe code it a little bit. We don't really need to review every line of

**[16:15]** really need to review every line of

**[16:15]** really need to review every line of code. It's not really facing end users.

**[16:17]** code. It's not really facing end users.

**[16:17]** code. It's not really facing end users. Uh this has been a really really fun

**[16:19]** Uh this has been a really really fun

**[16:19]** Uh this has been a really really fun thing for our business to just be able

**[16:20]** thing for our business to just be able

**[16:20]** thing for our business to just be able to turn out these really quick

**[16:21]** to turn out these really quick

**[16:21]** to turn out these really quick applications uh just to serve our own

**[16:23]** applications uh just to serve our own

**[16:23]** applications uh just to serve our own internal needs. Um so yeah, uh

**[16:26]** internal needs. Um so yeah, uh

**[16:26]** internal needs. Um so yeah, uh Greenfield is a great great use case for

**[16:28]** Greenfield is a great great use case for

**[16:28]** Greenfield is a great great use case for agents. U that's all I've got. Uh would

**[16:31]** agents. U that's all I've got. Uh would

**[16:31]** agents. U that's all I've got. Uh would love to have you all join the the OpenHS

**[16:33]** love to have you all join the the OpenHS

**[16:33]** love to have you all join the the OpenHS community. You can find us on GitHub,

**[16:34]** community. You can find us on GitHub,

**[16:34]** community. You can find us on GitHub, all handsaihands.

**[16:36]** all handsaihands.

**[16:36]** all handsaihands. Um join us on Slack, Discord. Uh we'd

**[16:39]** Um join us on Slack, Discord. Uh we'd

**[16:39]** Um join us on Slack, Discord. Uh we'd love to build with you.


