# Amp Code: Next Generation AI Coding – Beyang Liu

**Video URL:** https://youtu.be/gvIAkmZUEZY

---

## Full Transcript

### [00:00 - 01:00]

**[00:22]** How's everyone doing today?

**[00:22]** How's everyone doing today? >> Yeah, cool. Pretty cool conference, huh?

**[00:25]** >> Yeah, cool. Pretty cool conference, huh?

**[00:25]** >> Yeah, cool. Pretty cool conference, huh? Um, so yeah, my name is Vang. I'm here

**[00:27]** Um, so yeah, my name is Vang. I'm here

**[00:27]** Um, so yeah, my name is Vang. I'm here to talk about AMP. AMP is an opinionated

**[00:29]** to talk about AMP. AMP is an opinionated

**[00:30]** to talk about AMP. AMP is an opinionated frontier agent. Uh so before I get into

**[00:32]** frontier agent. Uh so before I get into

**[00:32]** frontier agent. Uh so before I get into what that means, uh who are we? Uh we're

**[00:35]** what that means, uh who are we? Uh we're

**[00:35]** what that means, uh who are we? Uh we're the bunch of weirdos downstairs at the

**[00:37]** the bunch of weirdos downstairs at the

**[00:37]** the bunch of weirdos downstairs at the booth with the weird pied piper dude on

**[00:39]** booth with the weird pied piper dude on

**[00:39]** booth with the weird pied piper dude on the floating golden fish. Uh and I think

**[00:43]** the floating golden fish. Uh and I think

**[00:43]** the floating golden fish. Uh and I think that kind of captures the ethos of what

**[00:45]** that kind of captures the ethos of what

**[00:45]** that kind of captures the ethos of what we're trying to do uh with AMP. We're

**[00:47]** we're trying to do uh with AMP. We're

**[00:47]** we're trying to do uh with AMP. We're trying to lean into that sense of awe

**[00:49]** trying to lean into that sense of awe

**[00:49]** trying to lean into that sense of awe and absurdity that I think we all

**[00:51]** and absurdity that I think we all

**[00:51]** and absurdity that I think we all experience right now living in this

**[00:52]** experience right now living in this

**[00:52]** experience right now living in this weird world we're living in where agents

**[00:55]** weird world we're living in where agents

**[00:55]** weird world we're living in where agents are writing an increasingly large amount

**[00:57]** are writing an increasingly large amount

**[00:57]** are writing an increasingly large amount of of our code. Uh and it's just kind of


### [01:00 - 02:00]

**[01:00]** of of our code. Uh and it's just kind of

**[01:00]** of of our code. Uh and it's just kind of like weird and magical. Like if you

**[01:01]** like weird and magical. Like if you

**[01:01]** like weird and magical. Like if you imagine how you were working like a year

**[01:03]** imagine how you were working like a year

**[01:03]** imagine how you were working like a year ago compared to how you're working now,

**[01:05]** ago compared to how you're working now,

**[01:05]** ago compared to how you're working now, it it feels completely different. And so

**[01:07]** it it feels completely different. And so

**[01:07]** it it feels completely different. And so we're embracing that sense of change and

**[01:08]** we're embracing that sense of change and

**[01:08]** we're embracing that sense of change and we really want to be the agent research

**[01:10]** we really want to be the agent research

**[01:10]** we really want to be the agent research lab that's sort of like living one year

**[01:12]** lab that's sort of like living one year

**[01:12]** lab that's sort of like living one year in the future and figuring out how this

**[01:14]** in the future and figuring out how this

**[01:14]** in the future and figuring out how this all kind of pans out. Okay. So, what is

**[01:17]** all kind of pans out. Okay. So, what is

**[01:17]** all kind of pans out. Okay. So, what is AMP actually? Well, it's a it's a coding

**[01:19]** AMP actually? Well, it's a it's a coding

**[01:20]** AMP actually? Well, it's a it's a coding agent that you can invoke from the

**[01:21]** agent that you can invoke from the

**[01:21]** agent that you can invoke from the terminal. So, here's our terminal UI. Uh

**[01:23]** terminal. So, here's our terminal UI. Uh

**[01:24]** terminal. So, here's our terminal UI. Uh we actually ended up building a complete

**[01:25]** we actually ended up building a complete

**[01:25]** we actually ended up building a complete terminal UI framework up from scratch

**[01:27]** terminal UI framework up from scratch

**[01:27]** terminal UI framework up from scratch because we wanted to take advantage of

**[01:28]** because we wanted to take advantage of

**[01:28]** because we wanted to take advantage of all the capabilities of modern

**[01:30]** all the capabilities of modern

**[01:30]** all the capabilities of modern terminals. And one of the balances we

**[01:32]** terminals. And one of the balances we

**[01:32]** terminals. And one of the balances we tried to strike in in this UI is we try

**[01:34]** tried to strike in in this UI is we try

**[01:34]** tried to strike in in this UI is we try to show the right amount of information

**[01:35]** to show the right amount of information

**[01:35]** to show the right amount of information to the user that conveys what the agent

**[01:37]** to the user that conveys what the agent

**[01:38]** to the user that conveys what the agent is doing without overwhelming you with,

**[01:40]** is doing without overwhelming you with,

**[01:40]** is doing without overwhelming you with, you know, every single token of

**[01:41]** you know, every single token of

**[01:41]** you know, every single token of explanation uh that the model is

**[01:43]** explanation uh that the model is

**[01:43]** explanation uh that the model is generating. We stream the diffs that

**[01:45]** generating. We stream the diffs that

**[01:45]** generating. We stream the diffs that it's making. uh we show you what CLI

**[01:47]** it's making. uh we show you what CLI

**[01:47]** it's making. uh we show you what CLI commands it's using. And if you look in

**[01:49]** commands it's using. And if you look in

**[01:49]** commands it's using. And if you look in the bottom right hand corner there,

**[01:50]** the bottom right hand corner there,

**[01:50]** the bottom right hand corner there, you'll see a little Emacs 30.1 thing.

**[01:53]** you'll see a little Emacs 30.1 thing.

**[01:53]** you'll see a little Emacs 30.1 thing. This also connects to the editor that

**[01:55]** This also connects to the editor that

**[01:55]** This also connects to the editor that you're using where it collects

**[01:56]** you're using where it collects

**[01:56]** you're using where it collects diagnostics. So, Emacs, Neovim, Jet

**[01:58]** diagnostics. So, Emacs, Neovim, Jet

**[01:58]** diagnostics. So, Emacs, Neovim, Jet Brains. Uh you can connect the the CLI


### [02:00 - 03:00]

**[02:01]** Brains. Uh you can connect the the CLI

**[02:01]** Brains. Uh you can connect the the CLI to your editor uh to collect additional

**[02:04]** to your editor uh to collect additional

**[02:04]** to your editor uh to collect additional information that's relevant to the task

**[02:05]** information that's relevant to the task

**[02:05]** information that's relevant to the task at hand. And so, this particular video

**[02:07]** at hand. And so, this particular video

**[02:07]** at hand. And so, this particular video is just AMP implementing a small feature

**[02:09]** is just AMP implementing a small feature

**[02:10]** is just AMP implementing a small feature to itself. Uh we asked it actually to

**[02:12]** to itself. Uh we asked it actually to

**[02:12]** to itself. Uh we asked it actually to add a little help button in the bottom

**[02:14]** add a little help button in the bottom

**[02:14]** add a little help button in the bottom lefthand corner. Uh and so that's just a

**[02:16]** lefthand corner. Uh and so that's just a

**[02:16]** lefthand corner. Uh and so that's just a quick demo to show you that uh the agent

**[02:18]** quick demo to show you that uh the agent

**[02:18]** quick demo to show you that uh the agent is pretty good at finding the relevant

**[02:19]** is pretty good at finding the relevant

**[02:19]** is pretty good at finding the relevant context and iterating towards that. Uh

**[02:22]** context and iterating towards that. Uh

**[02:22]** context and iterating towards that. Uh we also have an editor experience. Uh so

**[02:24]** we also have an editor experience. Uh so

**[02:24]** we also have an editor experience. Uh so we've not found the motivation yet to

**[02:26]** we've not found the motivation yet to

**[02:26]** we've not found the motivation yet to fork VS Code. Maybe we will in the

**[02:28]** fork VS Code. Maybe we will in the

**[02:28]** fork VS Code. Maybe we will in the future, but right now this installs into

**[02:32]** future, but right now this installs into

**[02:32]** future, but right now this installs into VS Code or any of its derivatives,

**[02:34]** VS Code or any of its derivatives,

**[02:34]** VS Code or any of its derivatives, Cursor, Windsurf, uh anti-gravity. Um

**[02:37]** Cursor, Windsurf, uh anti-gravity. Um

**[02:37]** Cursor, Windsurf, uh anti-gravity. Um and the idea here is you really write

**[02:40]** and the idea here is you really write

**[02:40]** and the idea here is you really write all your code through this agent panel.

**[02:42]** all your code through this agent panel.

**[02:42]** all your code through this agent panel. At least I do. Um I I actually spend

**[02:44]** At least I do. Um I I actually spend

**[02:44]** At least I do. Um I I actually spend very little time, you know, actually

**[02:46]** very little time, you know, actually

**[02:46]** very little time, you know, actually manually editing code now. And one of

**[02:48]** manually editing code now. And one of

**[02:48]** manually editing code now. And one of the bottlenecks we identified in the

**[02:49]** the bottlenecks we identified in the

**[02:49]** the bottlenecks we identified in the editor is I don't know about you, but I

**[02:51]** editor is I don't know about you, but I

**[02:51]** editor is I don't know about you, but I spend most of my time effectively doing

**[02:52]** spend most of my time effectively doing

**[02:52]** spend most of my time effectively doing code review now. Um just in the editor

**[02:54]** code review now. Um just in the editor

**[02:54]** code review now. Um just in the editor trying to read through all the agent

**[02:56]** trying to read through all the agent

**[02:56]** trying to read through all the agent output. That's the thing that constrains

**[02:58]** output. That's the thing that constrains

**[02:58]** output. That's the thing that constrains me from uh fully paralyzing, you know, 2


### [03:00 - 04:00]

**[03:01]** me from uh fully paralyzing, you know, 2

**[03:01]** me from uh fully paralyzing, you know, 2 3x uh the number of agents that I can

**[03:02]** 3x uh the number of agents that I can

**[03:02]** 3x uh the number of agents that I can run at at a given time. So we built a re

**[03:05]** run at at a given time. So we built a re

**[03:05]** run at at a given time. So we built a re review reu interface that I'll talk

**[03:07]** review reu interface that I'll talk

**[03:07]** review reu interface that I'll talk about uh in more depth uh in a bit that

**[03:10]** about uh in more depth uh in a bit that

**[03:10]** about uh in more depth uh in a bit that uh kind of helps you streamline that

**[03:12]** uh kind of helps you streamline that

**[03:12]** uh kind of helps you streamline that process guides you through the process

**[03:13]** process guides you through the process

**[03:13]** process guides you through the process of understanding what the agent wrote so

**[03:15]** of understanding what the agent wrote so

**[03:15]** of understanding what the agent wrote so that you can ensure that you're not

**[03:16]** that you can ensure that you're not

**[03:16]** that you can ensure that you're not shipping something that's super sloppy

**[03:18]** shipping something that's super sloppy

**[03:18]** shipping something that's super sloppy or spaghetti. Okay, so I hear all of you

**[03:21]** or spaghetti. Okay, so I hear all of you

**[03:21]** or spaghetti. Okay, so I hear all of you thinking like, okay, yeah, yeah, it

**[03:23]** thinking like, okay, yeah, yeah, it

**[03:23]** thinking like, okay, yeah, yeah, it looks pretty, but what actually is

**[03:25]** looks pretty, but what actually is

**[03:26]** looks pretty, but what actually is different? You know, why is this better

**[03:27]** different? You know, why is this better

**[03:27]** different? You know, why is this better than the like 20 other coding agents uh

**[03:30]** than the like 20 other coding agents uh

**[03:30]** than the like 20 other coding agents uh here? And I think the best way to convey

**[03:32]** here? And I think the best way to convey

**[03:32]** here? And I think the best way to convey this is I'm not going to try to convince

**[03:33]** this is I'm not going to try to convince

**[03:34]** this is I'm not going to try to convince you that it's better. I think that is

**[03:35]** you that it's better. I think that is

**[03:35]** you that it's better. I think that is ultimately up to you trying different

**[03:37]** ultimately up to you trying different

**[03:37]** ultimately up to you trying different things out and seeing what actually

**[03:39]** things out and seeing what actually

**[03:39]** things out and seeing what actually works. But I am going to try to convince

**[03:41]** works. But I am going to try to convince

**[03:41]** works. But I am going to try to convince you that we're thinking about things in

**[03:42]** you that we're thinking about things in

**[03:42]** you that we're thinking about things in a very different, opinionated, and weird

**[03:45]** a very different, opinionated, and weird

**[03:45]** a very different, opinionated, and weird manner. So I want to take you on the

**[03:46]** manner. So I want to take you on the

**[03:46]** manner. So I want to take you on the journey of us building AMP and all the

**[03:49]** journey of us building AMP and all the

**[03:49]** journey of us building AMP and all the different sort of contrarian or spicy

**[03:51]** different sort of contrarian or spicy

**[03:51]** different sort of contrarian or spicy takes that we've made uh decision-wise

**[03:54]** takes that we've made uh decision-wise

**[03:54]** takes that we've made uh decision-wise in the architecture of of the agent

**[03:55]** in the architecture of of the agent

**[03:55]** in the architecture of of the agent along the way. Okay, so let's start at

**[03:58]** along the way. Okay, so let's start at

**[03:58]** along the way. Okay, so let's start at the beginning. Um hello agent. What is


### [04:00 - 05:00]

**[04:00]** the beginning. Um hello agent. What is

**[04:00]** the beginning. Um hello agent. What is an agent at its core? Well, all an agent

**[04:02]** an agent at its core? Well, all an agent

**[04:02]** an agent at its core? Well, all an agent is as I'm sure most of you know uh is

**[04:05]** is as I'm sure most of you know uh is

**[04:05]** is as I'm sure most of you know uh is it's a for loop uh with tool calls and a

**[04:09]** it's a for loop uh with tool calls and a

**[04:09]** it's a for loop uh with tool calls and a model uh in the middle. And the reason I

**[04:11]** model uh in the middle. And the reason I

**[04:11]** model uh in the middle. And the reason I want to present this slide is because

**[04:13]** want to present this slide is because

**[04:13]** want to present this slide is because think of it this way really tells you

**[04:15]** think of it this way really tells you

**[04:15]** think of it this way really tells you what sort of levers you have to pull as

**[04:17]** what sort of levers you have to pull as

**[04:18]** what sort of levers you have to pull as a builder of agent. Uh there there's

**[04:19]** a builder of agent. Uh there there's

**[04:19]** a builder of agent. Uh there there's certain things that you can change. You

**[04:21]** certain things that you can change. You

**[04:21]** certain things that you can change. You can change the choice of model. You can

**[04:22]** can change the choice of model. You can

**[04:22]** can change the choice of model. You can change the tool descriptions and you can

**[04:24]** change the tool descriptions and you can

**[04:24]** change the tool descriptions and you can change uh how the model iterates with

**[04:26]** change uh how the model iterates with

**[04:26]** change uh how the model iterates with those tools and those are effectively

**[04:28]** those tools and those are effectively

**[04:28]** those tools and those are effectively your levers. Seems like a few amount of

**[04:30]** your levers. Seems like a few amount of

**[04:30]** your levers. Seems like a few amount of levers but you know just like

**[04:31]** levers but you know just like

**[04:31]** levers but you know just like programming languages all those are

**[04:33]** programming languages all those are

**[04:33]** programming languages all those are syntactic sugar around if statements and

**[04:34]** syntactic sugar around if statements and

**[04:34]** syntactic sugar around if statements and for loops. You know you can get a

**[04:36]** for loops. You know you can get a

**[04:36]** for loops. You know you can get a surprisingly wide variance of behaviors

**[04:38]** surprisingly wide variance of behaviors

**[04:38]** surprisingly wide variance of behaviors and complexity out of that.

**[04:40]** and complexity out of that.

**[04:40]** and complexity out of that. And so one of the key lovers in building

**[04:42]** And so one of the key lovers in building

**[04:42]** And so one of the key lovers in building any agent is the set of tools. And these

**[04:45]** any agent is the set of tools. And these

**[04:45]** any agent is the set of tools. And these days you cannot talk about tools without

**[04:46]** days you cannot talk about tools without

**[04:46]** days you cannot talk about tools without talking about MCP. So one of the early

**[04:49]** talking about MCP. So one of the early

**[04:49]** talking about MCP. So one of the early decisions we had to make in building AMP

**[04:51]** decisions we had to make in building AMP

**[04:51]** decisions we had to make in building AMP is how much do we invest in the MCP

**[04:53]** is how much do we invest in the MCP

**[04:53]** is how much do we invest in the MCP integrations? And MCP is this amazing

**[04:54]** integrations? And MCP is this amazing

**[04:54]** integrations? And MCP is this amazing new protocol that's gotten everyone and

**[04:56]** new protocol that's gotten everyone and

**[04:56]** new protocol that's gotten everyone and their mom thinking about how to provide

**[04:57]** their mom thinking about how to provide

**[04:57]** their mom thinking about how to provide context to agents. Um should we lean


### [05:00 - 06:00]

**[05:00]** context to agents. Um should we lean

**[05:00]** context to agents. Um should we lean into that or should we start building

**[05:02]** into that or should we start building

**[05:02]** into that or should we start building our own custom tool set? And our very

**[05:04]** our own custom tool set? And our very

**[05:04]** our own custom tool set? And our very opinionated take, I think this is maybe,

**[05:06]** opinionated take, I think this is maybe,

**[05:06]** opinionated take, I think this is maybe, you know, less controversial now than it

**[05:08]** you know, less controversial now than it

**[05:08]** you know, less controversial now than it was, you know, back in in April, was

**[05:10]** was, you know, back in in April, was

**[05:10]** was, you know, back in in April, was that we should really actually focus

**[05:12]** that we should really actually focus

**[05:12]** that we should really actually focus most of our attention on the core uh set

**[05:15]** most of our attention on the core uh set

**[05:15]** most of our attention on the core uh set of tools within AMP. And that's really

**[05:17]** of tools within AMP. And that's really

**[05:17]** of tools within AMP. And that's really for two reasons. One is because the more

**[05:20]** for two reasons. One is because the more

**[05:20]** for two reasons. One is because the more you work with agents, the more you find

**[05:22]** you work with agents, the more you find

**[05:22]** you work with agents, the more you find uh out that what you're trying to do is

**[05:24]** uh out that what you're trying to do is

**[05:24]** uh out that what you're trying to do is identify these feedback loops and help

**[05:26]** identify these feedback loops and help

**[05:26]** identify these feedback loops and help the agent close them. And in order to do

**[05:28]** the agent close them. And in order to do

**[05:28]** the agent close them. And in order to do that, you need a refined tool set that

**[05:30]** that, you need a refined tool set that

**[05:30]** that, you need a refined tool set that is really geared toward helping the

**[05:32]** is really geared toward helping the

**[05:32]** is really geared toward helping the agent find those loops. And you cannot

**[05:33]** agent find those loops. And you cannot

**[05:34]** agent find those loops. And you cannot do that with MCP servers. The creator of

**[05:35]** do that with MCP servers. The creator of

**[05:35]** do that with MCP servers. The creator of the MCP server doesn't know what your

**[05:37]** the MCP server doesn't know what your

**[05:37]** the MCP server doesn't know what your agent is trying to do. And so they're

**[05:38]** agent is trying to do. And so they're

**[05:38]** agent is trying to do. And so they're not going to tune the tool descriptions

**[05:40]** not going to tune the tool descriptions

**[05:40]** not going to tune the tool descriptions to what you're trying to accomplish. And

**[05:42]** to what you're trying to accomplish. And

**[05:42]** to what you're trying to accomplish. And then the second piece of this is context

**[05:44]** then the second piece of this is context

**[05:44]** then the second piece of this is context confusion. So the more tools that you

**[05:45]** confusion. So the more tools that you

**[05:45]** confusion. So the more tools that you add into the context window, uh the more

**[05:47]** add into the context window, uh the more

**[05:47]** add into the context window, uh the more things that the agent has to choose

**[05:48]** things that the agent has to choose

**[05:48]** things that the agent has to choose from. And if the tools aren't relevant

**[05:50]** from. And if the tools aren't relevant

**[05:50]** from. And if the tools aren't relevant to the task at hand, it ends up getting

**[05:52]** to the task at hand, it ends up getting

**[05:52]** to the task at hand, it ends up getting confused. So we've leaned hard into this

**[05:54]** confused. So we've leaned hard into this

**[05:54]** confused. So we've leaned hard into this uh custom tool set. And you'll see a

**[05:56]** uh custom tool set. And you'll see a

**[05:56]** uh custom tool set. And you'll see a little bit more about that in just a

**[05:57]** little bit more about that in just a

**[05:58]** little bit more about that in just a little bit. But before that, I wanted to


### [06:00 - 07:00]

**[06:00]** little bit. But before that, I wanted to

**[06:00]** little bit. But before that, I wanted to call out another issue with uh tool

**[06:02]** call out another issue with uh tool

**[06:02]** call out another issue with uh tool users, which is it's not just tool

**[06:04]** users, which is it's not just tool

**[06:04]** users, which is it's not just tool descriptions that eat up context. It's

**[06:05]** descriptions that eat up context. It's

**[06:05]** descriptions that eat up context. It's the tool calls themselves that also eat

**[06:07]** the tool calls themselves that also eat

**[06:07]** the tool calls themselves that also eat up context. And so, everyone who's built

**[06:09]** up context. And so, everyone who's built

**[06:10]** up context. And so, everyone who's built an agent has run into a context

**[06:11]** an agent has run into a context

**[06:11]** an agent has run into a context exhaustion problem where, you know, if

**[06:13]** exhaustion problem where, you know, if

**[06:13]** exhaustion problem where, you know, if you use any sort of coding agent, if

**[06:15]** you use any sort of coding agent, if

**[06:15]** you use any sort of coding agent, if it's good, it's going to go out and try

**[06:16]** it's good, it's going to go out and try

**[06:16]** it's good, it's going to go out and try to find a bunch of relevant context by

**[06:18]** to find a bunch of relevant context by

**[06:18]** to find a bunch of relevant context by grepping and reading files first. And by

**[06:19]** grepping and reading files first. And by

**[06:20]** grepping and reading files first. And by the time it gets to editing, there's

**[06:21]** the time it gets to editing, there's

**[06:21]** the time it gets to editing, there's only a small amount of context window

**[06:22]** only a small amount of context window

**[06:22]** only a small amount of context window left. And so, maybe it has to stop

**[06:23]** left. And so, maybe it has to stop

**[06:23]** left. And so, maybe it has to stop prematurely. And so the naive way to fix

**[06:26]** prematurely. And so the naive way to fix

**[06:26]** prematurely. And so the naive way to fix this is just to prompt it to, you know,

**[06:28]** this is just to prompt it to, you know,

**[06:28]** this is just to prompt it to, you know, do less reads so you can do more

**[06:29]** do less reads so you can do more

**[06:29]** do less reads so you can do more iterations on the edit side. But then

**[06:31]** iterations on the edit side. But then

**[06:31]** iterations on the edit side. But then this leads to another failure mode which

**[06:33]** this leads to another failure mode which

**[06:33]** this leads to another failure mode which I call the doom loop mode which is it

**[06:35]** I call the doom loop mode which is it

**[06:35]** I call the doom loop mode which is it doesn't gather enough context in the

**[06:36]** doesn't gather enough context in the

**[06:36]** doesn't gather enough context in the beginning and so it ends up not figuring

**[06:38]** beginning and so it ends up not figuring

**[06:38]** beginning and so it ends up not figuring out what it needs to do and just retries

**[06:40]** out what it needs to do and just retries

**[06:40]** out what it needs to do and just retries the same thing over and over again. And

**[06:42]** the same thing over and over again. And

**[06:42]** the same thing over and over again. And so the way to solve this is really with

**[06:44]** so the way to solve this is really with

**[06:44]** so the way to solve this is really with uh sub aents. So sub agents are the

**[06:45]** uh sub aents. So sub agents are the

**[06:46]** uh sub aents. So sub agents are the analog to subutine calls in regular

**[06:47]** analog to subutine calls in regular

**[06:48]** analog to subutine calls in regular programming languages. This is how you

**[06:49]** programming languages. This is how you

**[06:49]** programming languages. This is how you can factor out the context window used

**[06:50]** can factor out the context window used

**[06:50]** can factor out the context window used for a subtask into a separate context

**[06:53]** for a subtask into a separate context

**[06:53]** for a subtask into a separate context window which is the sub agents context

**[06:54]** window which is the sub agents context

**[06:54]** window which is the sub agents context window. Uh it can do all the things it

**[06:56]** window. Uh it can do all the things it

**[06:56]** window. Uh it can do all the things it needs and then at the end of the day it

**[06:58]** needs and then at the end of the day it

**[06:58]** needs and then at the end of the day it only returns the relevant results to the

**[06:59]** only returns the relevant results to the

**[06:59]** only returns the relevant results to the main uh agent window. So sub agents are


### [07:00 - 08:00]

**[07:01]** main uh agent window. So sub agents are

**[07:01]** main uh agent window. So sub agents are effectively a way to conserve and extend

**[07:03]** effectively a way to conserve and extend

**[07:03]** effectively a way to conserve and extend the context window of your main agent.

**[07:05]** the context window of your main agent.

**[07:05]** the context window of your main agent. Uh so sub aents sub agents are great. I

**[07:08]** Uh so sub aents sub agents are great. I

**[07:08]** Uh so sub aents sub agents are great. I think everyone uh building agents has

**[07:10]** think everyone uh building agents has

**[07:10]** think everyone uh building agents has probably heard of or or use sub agents

**[07:11]** probably heard of or or use sub agents

**[07:11]** probably heard of or or use sub agents uh so far. But I think we have a unique

**[07:13]** uh so far. But I think we have a unique

**[07:13]** uh so far. But I think we have a unique take on sub agents, which is we're not

**[07:15]** take on sub agents, which is we're not

**[07:15]** take on sub agents, which is we're not really doing generic sub uh sub aents

**[07:17]** really doing generic sub uh sub aents

**[07:17]** really doing generic sub uh sub aents where you kind of tweak the system

**[07:18]** where you kind of tweak the system

**[07:18]** where you kind of tweak the system prompt and tweak the tool set a little

**[07:20]** prompt and tweak the tool set a little

**[07:20]** prompt and tweak the tool set a little bit. We've really leaned into our sub

**[07:23]** bit. We've really leaned into our sub

**[07:23]** bit. We've really leaned into our sub aents. Uh and so we have uh three to

**[07:26]** aents. Uh and so we have uh three to

**[07:26]** aents. Uh and so we have uh three to four really core sub aents that really

**[07:28]** four really core sub aents that really

**[07:28]** four really core sub aents that really extend the functionality and capability

**[07:30]** extend the functionality and capability

**[07:30]** extend the functionality and capability uh of AMP itself. The first one is

**[07:32]** uh of AMP itself. The first one is

**[07:32]** uh of AMP itself. The first one is something that we call the finder. This

**[07:34]** something that we call the finder. This

**[07:34]** something that we call the finder. This is effectively our codebase uh search

**[07:36]** is effectively our codebase uh search

**[07:36]** is effectively our codebase uh search sub aent. It's gone through an evolution

**[07:39]** sub aent. It's gone through an evolution

**[07:39]** sub aent. It's gone through an evolution of models and we've ended up at the

**[07:40]** of models and we've ended up at the

**[07:40]** of models and we've ended up at the point now where we're using a relatively

**[07:42]** point now where we're using a relatively

**[07:42]** point now where we're using a relatively small and quick model to drive a limited

**[07:44]** small and quick model to drive a limited

**[07:44]** small and quick model to drive a limited tool set that we found really is optimal

**[07:46]** tool set that we found really is optimal

**[07:46]** tool set that we found really is optimal for quickly discovering uh relevant

**[07:49]** for quickly discovering uh relevant

**[07:49]** for quickly discovering uh relevant context within the codebase.

**[07:51]** context within the codebase.

**[07:51]** context within the codebase. Another sub aent that we've implemented

**[07:52]** Another sub aent that we've implemented

**[07:52]** Another sub aent that we've implemented is the thing that we call the oracle. So

**[07:54]** is the thing that we call the oracle. So

**[07:54]** is the thing that we call the oracle. So this is how AMP does reasoning. So in

**[07:57]** this is how AMP does reasoning. So in

**[07:57]** this is how AMP does reasoning. So in contrast to most agents which uh you

**[07:59]** contrast to most agents which uh you

**[07:59]** contrast to most agents which uh you know implement reasoning in the model


### [08:00 - 09:00]

**[08:01]** know implement reasoning in the model

**[08:01]** know implement reasoning in the model selection part of the experience, we

**[08:04]** selection part of the experience, we

**[08:04]** selection part of the experience, we found the best way to implement

**[08:05]** found the best way to implement

**[08:05]** found the best way to implement reasoning models is really through a sub

**[08:07]** reasoning models is really through a sub

**[08:07]** reasoning models is really through a sub agent. What that allows you to do is

**[08:09]** agent. What that allows you to do is

**[08:09]** agent. What that allows you to do is preserve the relative like snappiness uh

**[08:12]** preserve the relative like snappiness uh

**[08:12]** preserve the relative like snappiness uh in the main agent as well as its ability

**[08:14]** in the main agent as well as its ability

**[08:14]** in the main agent as well as its ability to to use a variety of different tools

**[08:16]** to to use a variety of different tools

**[08:16]** to to use a variety of different tools and then only when you need to debug a

**[08:18]** and then only when you need to debug a

**[08:18]** and then only when you need to debug a tricky problem or plan something very

**[08:20]** tricky problem or plan something very

**[08:20]** tricky problem or plan something very nuance, it drops into this Oracle sub

**[08:22]** nuance, it drops into this Oracle sub

**[08:22]** nuance, it drops into this Oracle sub agent and figures things out. And this

**[08:25]** agent and figures things out. And this

**[08:25]** agent and figures things out. And this is something that's like kind of

**[08:26]** is something that's like kind of

**[08:26]** is something that's like kind of magical. It's like anytime the main

**[08:28]** magical. It's like anytime the main

**[08:28]** magical. It's like anytime the main agent has trouble uh figuring out

**[08:29]** agent has trouble uh figuring out

**[08:29]** agent has trouble uh figuring out something and I'm like I don't want to

**[08:30]** something and I'm like I don't want to

**[08:30]** something and I'm like I don't want to spend like one to two hours going down

**[08:32]** spend like one to two hours going down

**[08:32]** spend like one to two hours going down this rabbit hole, I just like tag the

**[08:33]** this rabbit hole, I just like tag the

**[08:34]** this rabbit hole, I just like tag the oracles like invoke the oracle, think

**[08:35]** oracles like invoke the oracle, think

**[08:35]** oracles like invoke the oracle, think really hard, I go like alt tab, check my

**[08:37]** really hard, I go like alt tab, check my

**[08:38]** really hard, I go like alt tab, check my email for a bit and sometimes it takes a

**[08:39]** email for a bit and sometimes it takes a

**[08:39]** email for a bit and sometimes it takes a few minutes because it's thinking really

**[08:40]** few minutes because it's thinking really

**[08:40]** few minutes because it's thinking really deeply, but I think like four or out of

**[08:43]** deeply, but I think like four or out of

**[08:43]** deeply, but I think like four or out of five times it just magically finds uh uh

**[08:46]** five times it just magically finds uh uh

**[08:46]** five times it just magically finds uh uh the underlying issue. We also have a

**[08:48]** the underlying issue. We also have a

**[08:48]** the underlying issue. We also have a librarian sub agent which is meant to

**[08:50]** librarian sub agent which is meant to

**[08:50]** librarian sub agent which is meant to fetch context beyond the codebase. So

**[08:51]** fetch context beyond the codebase. So

**[08:52]** fetch context beyond the codebase. So from libraries and frameworks that you

**[08:53]** from libraries and frameworks that you

**[08:53]** from libraries and frameworks that you depend on. And then there's a new

**[08:54]** depend on. And then there's a new

**[08:54]** depend on. And then there's a new experimental sub aent that we call the

**[08:56]** experimental sub aent that we call the

**[08:56]** experimental sub aent that we call the Kraken. Uh its job is it doesn't edit

**[08:58]** Kraken. Uh its job is it doesn't edit

**[08:58]** Kraken. Uh its job is it doesn't edit code files uh one by one. Uh it really


### [09:00 - 10:00]

**[09:01]** code files uh one by one. Uh it really

**[09:01]** code files uh one by one. Uh it really is all about writing code mods to do

**[09:03]** is all about writing code mods to do

**[09:03]** is all about writing code mods to do these kind of like large scale

**[09:04]** these kind of like large scale

**[09:04]** these kind of like large scale refactors. So we're leaning hard into

**[09:06]** refactors. So we're leaning hard into

**[09:06]** refactors. So we're leaning hard into the sub agents and uh that's really in

**[09:09]** the sub agents and uh that's really in

**[09:09]** the sub agents and uh that's really in contrast to a lot of the existing coding

**[09:11]** contrast to a lot of the existing coding

**[09:11]** contrast to a lot of the existing coding agents. I think almost every other

**[09:13]** agents. I think almost every other

**[09:13]** agents. I think almost every other coding agent implements a model selector

**[09:15]** coding agent implements a model selector

**[09:15]** coding agent implements a model selector as one of the core uh UX components and

**[09:18]** as one of the core uh UX components and

**[09:18]** as one of the core uh UX components and we just don't think that this is the

**[09:19]** we just don't think that this is the

**[09:19]** we just don't think that this is the architecture of the future. I get that,

**[09:21]** architecture of the future. I get that,

**[09:21]** architecture of the future. I get that, you know, developers like choice or at

**[09:22]** you know, developers like choice or at

**[09:22]** you know, developers like choice or at least the the possibility of choice. But

**[09:25]** least the the possibility of choice. But

**[09:25]** least the the possibility of choice. But the problem with choice is that there's

**[09:26]** the problem with choice is that there's

**[09:26]** the problem with choice is that there's also a paradox of choice. The more

**[09:28]** also a paradox of choice. The more

**[09:28]** also a paradox of choice. The more choices that you have, the more uh kind

**[09:29]** choices that you have, the more uh kind

**[09:30]** choices that you have, the more uh kind of like cognitive burden it is to choose

**[09:31]** of like cognitive burden it is to choose

**[09:31]** of like cognitive burden it is to choose from these different models. And that

**[09:34]** from these different models. And that

**[09:34]** from these different models. And that means at the architectural level, if you

**[09:36]** means at the architectural level, if you

**[09:36]** means at the architectural level, if you have n different models and one agent

**[09:38]** have n different models and one agent

**[09:38]** have n different models and one agent harness that you can only lightly

**[09:39]** harness that you can only lightly

**[09:39]** harness that you can only lightly customize each model, it means you're

**[09:41]** customize each model, it means you're

**[09:41]** customize each model, it means you're never really optimizing for what any one

**[09:44]** never really optimizing for what any one

**[09:44]** never really optimizing for what any one given model uh can do. And so AMP's

**[09:46]** given model uh can do. And so AMP's

**[09:46]** given model uh can do. And so AMP's architecture is much more

**[09:48]** architecture is much more

**[09:48]** architecture is much more agent-oriented. We have two top level

**[09:50]** agent-oriented. We have two top level

**[09:50]** agent-oriented. We have two top level agents, a smart agent and a rush agent.

**[09:52]** agents, a smart agent and a rush agent.

**[09:52]** agents, a smart agent and a rush agent. And the smart agent is the one that has

**[09:54]** And the smart agent is the one that has

**[09:54]** And the smart agent is the one that has access to all those fancy sub aents and

**[09:56]** access to all those fancy sub aents and

**[09:56]** access to all those fancy sub aents and can do a lot of things. It's it's a

**[09:57]** can do a lot of things. It's it's a

**[09:57]** can do a lot of things. It's it's a little bit slower, but you can hand it

**[09:59]** little bit slower, but you can hand it

**[09:59]** little bit slower, but you can hand it more complex instructions. And then the


### [10:00 - 11:00]

**[10:01]** more complex instructions. And then the

**[10:01]** more complex instructions. And then the rush agent is for uh those kind of like

**[10:04]** rush agent is for uh those kind of like

**[10:04]** rush agent is for uh those kind of like in the loop tasks where you want to be

**[10:05]** in the loop tasks where you want to be

**[10:06]** in the loop tasks where you want to be tight in the loop and you're making

**[10:07]** tight in the loop and you're making

**[10:07]** tight in the loop and you're making quick targeted uh edits to to the code.

**[10:11]** quick targeted uh edits to to the code.

**[10:11]** quick targeted uh edits to to the code. And why do we have two top agents? It's

**[10:14]** And why do we have two top agents? It's

**[10:14]** And why do we have two top agents? It's really we're trying to kind of like pick

**[10:16]** really we're trying to kind of like pick

**[10:16]** really we're trying to kind of like pick points along the frontier of

**[10:17]** points along the frontier of

**[10:17]** points along the frontier of intelligence and speed that are

**[10:20]** intelligence and speed that are

**[10:20]** intelligence and speed that are meaningful to the user experience. So in

**[10:22]** meaningful to the user experience. So in

**[10:22]** meaningful to the user experience. So in in talking to our users, we found that

**[10:24]** in talking to our users, we found that

**[10:24]** in talking to our users, we found that there's kind of two modalities for

**[10:25]** there's kind of two modalities for

**[10:25]** there's kind of two modalities for invoking agents. Now one is you kind of

**[10:28]** invoking agents. Now one is you kind of

**[10:28]** invoking agents. Now one is you kind of like spin off a task and have it run and

**[10:30]** like spin off a task and have it run and

**[10:30]** like spin off a task and have it run and then review the code when it's finished

**[10:31]** then review the code when it's finished

**[10:31]** then review the code when it's finished asynchronously. Uh or you want to be in

**[10:33]** asynchronously. Uh or you want to be in

**[10:34]** asynchronously. Uh or you want to be in the loop, you know, quickly having the

**[10:35]** the loop, you know, quickly having the

**[10:35]** the loop, you know, quickly having the agent make edits while you quickly

**[10:37]** agent make edits while you quickly

**[10:37]** agent make edits while you quickly review them one by one. Kind of like

**[10:38]** review them one by one. Kind of like

**[10:38]** review them one by one. Kind of like babysitting the agent uh in the inner

**[10:41]** babysitting the agent uh in the inner

**[10:41]** babysitting the agent uh in the inner loop.

**[10:43]** loop.

**[10:43]** loop. And we're very intentional about the

**[10:44]** And we're very intentional about the

**[10:44]** And we're very intentional about the model choice here. We've only switched

**[10:45]** model choice here. We've only switched

**[10:45]** model choice here. We've only switched the smart model once and that was

**[10:46]** the smart model once and that was

**[10:46]** the smart model once and that was actually two days ago uh when Gemini 3

**[10:49]** actually two days ago uh when Gemini 3

**[10:49]** actually two days ago uh when Gemini 3 uh was released. And I think you know

**[10:51]** uh was released. And I think you know

**[10:51]** uh was released. And I think you know the the reaction Gemini 3 has been

**[10:52]** the the reaction Gemini 3 has been

**[10:52]** the the reaction Gemini 3 has been really interesting to watch. I think

**[10:53]** really interesting to watch. I think

**[10:53]** really interesting to watch. I think you'll see widely different behavior

**[10:55]** you'll see widely different behavior

**[10:55]** you'll see widely different behavior from Gemini 3 in different uh agent

**[10:58]** from Gemini 3 in different uh agent

**[10:58]** from Gemini 3 in different uh agent settings. So for those of you who've

**[10:59]** settings. So for those of you who've

**[10:59]** settings. So for those of you who've tried it out in other settings, I highly


### [11:00 - 12:00]

**[11:01]** tried it out in other settings, I highly

**[11:01]** tried it out in other settings, I highly encourage you to uh try AMP. We did a

**[11:03]** encourage you to uh try AMP. We did a

**[11:03]** encourage you to uh try AMP. We did a lot of testing in the week before the

**[11:05]** lot of testing in the week before the

**[11:05]** lot of testing in the week before the release to optimize the smart agent to

**[11:08]** release to optimize the smart agent to

**[11:08]** release to optimize the smart agent to take full advantage of of its

**[11:09]** take full advantage of of its

**[11:09]** take full advantage of of its capabilities. And uh we're absolutely

**[11:11]** capabilities. And uh we're absolutely

**[11:11]** capabilities. And uh we're absolutely loving it. We're still working through

**[11:12]** loving it. We're still working through

**[11:12]** loving it. We're still working through some kinks obviously because it's a a

**[11:14]** some kinks obviously because it's a a

**[11:14]** some kinks obviously because it's a a new model, but we feel confident that it

**[11:17]** new model, but we feel confident that it

**[11:17]** new model, but we feel confident that it it's again moved the frontier of what's

**[11:18]** it's again moved the frontier of what's

**[11:18]** it's again moved the frontier of what's possible.

**[11:21]** possible.

**[11:21]** possible. Okay, so we talked a lot about like

**[11:22]** Okay, so we talked a lot about like

**[11:22]** Okay, so we talked a lot about like agent construction, the behavior. I want

**[11:24]** agent construction, the behavior. I want

**[11:24]** agent construction, the behavior. I want to talk a little bit about the UI layer

**[11:25]** to talk a little bit about the UI layer

**[11:25]** to talk a little bit about the UI layer of agents as well. So, you know, editor

**[11:28]** of agents as well. So, you know, editor

**[11:28]** of agents as well. So, you know, editor versus terminal, we're doing both. Um,

**[11:29]** versus terminal, we're doing both. Um,

**[11:30]** versus terminal, we're doing both. Um, and I think that's because both of them

**[11:31]** and I think that's because both of them

**[11:32]** and I think that's because both of them tackle kind of like different modalities

**[11:33]** tackle kind of like different modalities

**[11:33]** tackle kind of like different modalities of working. Uh, but we do have opinated

**[11:35]** of working. Uh, but we do have opinated

**[11:36]** of working. Uh, but we do have opinated takes uh in each interface. So, in the

**[11:38]** takes uh in each interface. So, in the

**[11:38]** takes uh in each interface. So, in the editor, I think of my editor now more as

**[11:40]** editor, I think of my editor now more as

**[11:40]** editor, I think of my editor now more as a reader uh uh more than anything else

**[11:43]** a reader uh uh more than anything else

**[11:43]** a reader uh uh more than anything else because uh I don't know like if you're

**[11:45]** because uh I don't know like if you're

**[11:45]** because uh I don't know like if you're using agents heavily, I don't think

**[11:47]** using agents heavily, I don't think

**[11:47]** using agents heavily, I don't think you're really editing all that much uh

**[11:49]** you're really editing all that much uh

**[11:49]** you're really editing all that much uh in your editor anymore. You're mainly

**[11:51]** in your editor anymore. You're mainly

**[11:51]** in your editor anymore. You're mainly driving edits through the agent panel,

**[11:53]** driving edits through the agent panel,

**[11:53]** driving edits through the agent panel, which is what you see on the right hand

**[11:54]** which is what you see on the right hand

**[11:54]** which is what you see on the right hand side or the right hand side here. And

**[11:57]** side or the right hand side here. And

**[11:57]** side or the right hand side here. And then what I do in in my editor is I pop


### [12:00 - 13:00]

**[12:00]** then what I do in in my editor is I pop

**[12:00]** then what I do in in my editor is I pop over to the side panel, which is

**[12:02]** over to the side panel, which is

**[12:02]** over to the side panel, which is optimized for reviewing different diffs.

**[12:04]** optimized for reviewing different diffs.

**[12:04]** optimized for reviewing different diffs. So we actually built a custom diff

**[12:05]** So we actually built a custom diff

**[12:05]** So we actually built a custom diff viewer for the way that people are

**[12:07]** viewer for the way that people are

**[12:07]** viewer for the way that people are consuming agentic output. You can select

**[12:09]** consuming agentic output. You can select

**[12:09]** consuming agentic output. You can select any arbitrary commit range quickly view

**[12:12]** any arbitrary commit range quickly view

**[12:12]** any arbitrary commit range quickly view through the file level diffs. All the

**[12:14]** through the file level diffs. All the

**[12:14]** through the file level diffs. All the diffs are editable and you have full

**[12:16]** diffs are editable and you have full

**[12:16]** diffs are editable and you have full code navigation. So go to definition

**[12:17]** code navigation. So go to definition

**[12:18]** code navigation. So go to definition find references and there's a feature at

**[12:20]** find references and there's a feature at

**[12:20]** find references and there's a feature at the bottom that gives you a tour of the

**[12:22]** the bottom that gives you a tour of the

**[12:22]** the bottom that gives you a tour of the change. So it actually guides you

**[12:23]** change. So it actually guides you

**[12:23]** change. So it actually guides you through which files you should read

**[12:24]** through which files you should read

**[12:24]** through which files you should read first because I find half the battle

**[12:26]** first because I find half the battle

**[12:26]** first because I find half the battle when reviewing a large change is

**[12:27]** when reviewing a large change is

**[12:27]** when reviewing a large change is figuring out where to start. So the guey

**[12:31]** figuring out where to start. So the guey

**[12:31]** figuring out where to start. So the guey aspect of the editor allows us to build

**[12:33]** aspect of the editor allows us to build

**[12:33]** aspect of the editor allows us to build a very rich uh experience uh for for

**[12:35]** a very rich uh experience uh for for

**[12:35]** a very rich uh experience uh for for this type of thing. And then meanwhile

**[12:37]** this type of thing. And then meanwhile

**[12:37]** this type of thing. And then meanwhile in the terminal um we really want to

**[12:39]** in the terminal um we really want to

**[12:39]** in the terminal um we really want to take advantage full advantage of the the

**[12:42]** take advantage full advantage of the the

**[12:42]** take advantage full advantage of the the features and rendering capabilities of

**[12:43]** features and rendering capabilities of

**[12:43]** features and rendering capabilities of modern terminals. So uh we actually have

**[12:45]** modern terminals. So uh we actually have

**[12:45]** modern terminals. So uh we actually have one of the core contributors to Ghosty

**[12:47]** one of the core contributors to Ghosty

**[12:47]** one of the core contributors to Ghosty uh the open source uh terminal uh that

**[12:50]** uh the open source uh terminal uh that

**[12:50]** uh the open source uh terminal uh that built a uh a TUI framework from scratch

**[12:52]** built a uh a TUI framework from scratch

**[12:52]** built a uh a TUI framework from scratch to power the AMPU. So one of the nice

**[12:54]** to power the AMPU. So one of the nice

**[12:54]** to power the AMPU. So one of the nice things that we can do is just to point

**[12:56]** things that we can do is just to point

**[12:56]** things that we can do is just to point out a little detail the the green color

**[12:59]** out a little detail the the green color

**[12:59]** out a little detail the the green color of the diff rendering on the left hand


### [13:00 - 14:00]

**[13:01]** of the diff rendering on the left hand

**[13:01]** of the diff rendering on the left hand side terminal that's actually we can

**[13:03]** side terminal that's actually we can

**[13:03]** side terminal that's actually we can have the terminal mix in the color green

**[13:05]** have the terminal mix in the color green

**[13:05]** have the terminal mix in the color green with whatever background color it's

**[13:06]** with whatever background color it's

**[13:06]** with whatever background color it's using. So that allows for a much nicer

**[13:09]** using. So that allows for a much nicer

**[13:09]** using. So that allows for a much nicer display. At the same time we know that

**[13:11]** display. At the same time we know that

**[13:11]** display. At the same time we know that people use all sorts of terminals uh

**[13:13]** people use all sorts of terminals uh

**[13:13]** people use all sorts of terminals uh including like terminals in Jet Brains

**[13:15]** including like terminals in Jet Brains

**[13:15]** including like terminals in Jet Brains or VS Code and other editors. And so

**[13:17]** or VS Code and other editors. And so

**[13:17]** or VS Code and other editors. And so we've added the ability to gracefully

**[13:19]** we've added the ability to gracefully

**[13:19]** we've added the ability to gracefully degrade. So even if you're using AMP in

**[13:21]** degrade. So even if you're using AMP in

**[13:21]** degrade. So even if you're using AMP in like the default Mac OS terminal, it

**[13:23]** like the default Mac OS terminal, it

**[13:24]** like the default Mac OS terminal, it falls back to the capabilities that uh

**[13:26]** falls back to the capabilities that uh

**[13:26]** falls back to the capabilities that uh are uh available in in that setting.

**[13:30]** are uh available in in that setting.

**[13:30]** are uh available in in that setting. Another aspect about how we're thinking

**[13:32]** Another aspect about how we're thinking

**[13:32]** Another aspect about how we're thinking about coding agents is really from the

**[13:33]** about coding agents is really from the

**[13:33]** about coding agents is really from the how do we get people to learn this new

**[13:35]** how do we get people to learn this new

**[13:35]** how do we get people to learn this new craft? Like we think that uh human

**[13:37]** craft? Like we think that uh human

**[13:37]** craft? Like we think that uh human developers are going to be around for a

**[13:38]** developers are going to be around for a

**[13:38]** developers are going to be around for a long long time, but we essentially have

**[13:40]** long long time, but we essentially have

**[13:40]** long long time, but we essentially have to relearn the craft of how to code uh

**[13:43]** to relearn the craft of how to code uh

**[13:43]** to relearn the craft of how to code uh together. And so one of the first

**[13:44]** together. And so one of the first

**[13:44]** together. And so one of the first features that we built in AMP was the

**[13:46]** features that we built in AMP was the

**[13:46]** features that we built in AMP was the ability to share threads with your

**[13:48]** ability to share threads with your

**[13:48]** ability to share threads with your teammates. So, if you're using AMP on

**[13:49]** teammates. So, if you're using AMP on

**[13:49]** teammates. So, if you're using AMP on your team, you can go and see like how

**[13:52]** your team, you can go and see like how

**[13:52]** your team, you can go and see like how much code people are changing with AMP

**[13:53]** much code people are changing with AMP

**[13:53]** much code people are changing with AMP over a given period of time. And you can

**[13:55]** over a given period of time. And you can

**[13:55]** over a given period of time. And you can poke into specific threads to see how

**[13:57]** poke into specific threads to see how

**[13:57]** poke into specific threads to see how they're doing things. And people love

**[13:58]** they're doing things. And people love

**[13:58]** they're doing things. And people love this feature because essentially like


### [14:00 - 15:00]

**[14:00]** this feature because essentially like

**[14:00]** this feature because essentially like link threads to AMP and say like, "Hey,

**[14:02]** link threads to AMP and say like, "Hey,

**[14:02]** link threads to AMP and say like, "Hey, here's a cool prompting technique that I

**[14:03]** here's a cool prompting technique that I

**[14:03]** here's a cool prompting technique that I discovered. Try it like this." Or, "Hey,

**[14:05]** discovered. Try it like this." Or, "Hey,

**[14:05]** discovered. Try it like this." Or, "Hey, here it got stuck here. Can you help me,

**[14:07]** here it got stuck here. Can you help me,

**[14:07]** here it got stuck here. Can you help me, you know, uh think through how better to

**[14:09]** you know, uh think through how better to

**[14:09]** you know, uh think through how better to to connect the agent with the feedback

**[14:11]** to connect the agent with the feedback

**[14:11]** to connect the agent with the feedback loop to get further?"

**[14:14]** loop to get further?"

**[14:14]** loop to get further?" uh another aspect of of uh enabling more

**[14:17]** uh another aspect of of uh enabling more

**[14:17]** uh another aspect of of uh enabling more people to experience uh coding agents

**[14:19]** people to experience uh coding agents

**[14:19]** people to experience uh coding agents and learn how they work is by making it

**[14:21]** and learn how they work is by making it

**[14:21]** and learn how they work is by making it more accessible from an economic

**[14:23]** more accessible from an economic

**[14:23]** more accessible from an economic perspective. So um you know remember the

**[14:26]** perspective. So um you know remember the

**[14:26]** perspective. So um you know remember the smart and uh rush uh agents at the top

**[14:29]** smart and uh rush uh agents at the top

**[14:29]** smart and uh rush uh agents at the top level. You know smart models remain

**[14:30]** level. You know smart models remain

**[14:30]** level. You know smart models remain relatively expensive today but rush

**[14:33]** relatively expensive today but rush

**[14:33]** relatively expensive today but rush models are getting cheaper and cheaper

**[14:34]** models are getting cheaper and cheaper

**[14:34]** models are getting cheaper and cheaper but not yet free. And so we're thinking

**[14:36]** but not yet free. And so we're thinking

**[14:36]** but not yet free. And so we're thinking about you know more and more like one of

**[14:38]** about you know more and more like one of

**[14:38]** about you know more and more like one of the the biggest barriers to using agents

**[14:41]** the the biggest barriers to using agents

**[14:41]** the the biggest barriers to using agents fully is actually cost right now. Like

**[14:43]** fully is actually cost right now. Like

**[14:43]** fully is actually cost right now. Like if you go to like college campuses uh

**[14:45]** if you go to like college campuses uh

**[14:45]** if you go to like college campuses uh and talk to students, the actual number

**[14:46]** and talk to students, the actual number

**[14:46]** and talk to students, the actual number of people who have used a coding agent

**[14:48]** of people who have used a coding agent

**[14:48]** of people who have used a coding agent is actually much smaller than I would

**[14:50]** is actually much smaller than I would

**[14:50]** is actually much smaller than I would have thought given you know young

**[14:51]** have thought given you know young

**[14:51]** have thought given you know young people's uh propensity to adopt new

**[14:53]** people's uh propensity to adopt new

**[14:53]** people's uh propensity to adopt new technology. A lot of this cost. So

**[14:55]** technology. A lot of this cost. So

**[14:55]** technology. A lot of this cost. So someone had the crazy idea on our team

**[14:57]** someone had the crazy idea on our team

**[14:57]** someone had the crazy idea on our team like hey you know what we could do we

**[14:59]** like hey you know what we could do we

**[14:59]** like hey you know what we could do we could ship ads in your terminal. And at


### [15:00 - 16:00]

**[15:02]** could ship ads in your terminal. And at

**[15:02]** could ship ads in your terminal. And at first it was like nah that'll never

**[15:05]** first it was like nah that'll never

**[15:05]** first it was like nah that'll never work. But the more and more we thought

**[15:06]** work. But the more and more we thought

**[15:06]** work. But the more and more we thought about it and the more and more like

**[15:07]** about it and the more and more like

**[15:07]** about it and the more and more like inference costs started declining we're

**[15:09]** inference costs started declining we're

**[15:09]** inference costs started declining we're like yeah maybe. So, we actually shipped

**[15:11]** like yeah maybe. So, we actually shipped

**[15:11]** like yeah maybe. So, we actually shipped uh a mini ad network that delivers ads

**[15:13]** uh a mini ad network that delivers ads

**[15:13]** uh a mini ad network that delivers ads for other developer tools uh in in AMP

**[15:16]** for other developer tools uh in in AMP

**[15:16]** for other developer tools uh in in AMP in the terminal and in the editor. Uh

**[15:18]** in the terminal and in the editor. Uh

**[15:18]** in the terminal and in the editor. Uh they're very subtle. So, I don't know if

**[15:20]** they're very subtle. So, I don't know if

**[15:20]** they're very subtle. So, I don't know if you can spot the ad in this screenshot,

**[15:21]** you can spot the ad in this screenshot,

**[15:22]** you can spot the ad in this screenshot, but we try to make them non-intrusive.

**[15:23]** but we try to make them non-intrusive.

**[15:23]** but we try to make them non-intrusive. But this effectively allows us to

**[15:25]** But this effectively allows us to

**[15:25]** But this effectively allows us to sponsor inference uh in in the Rush uh

**[15:29]** sponsor inference uh in in the Rush uh

**[15:29]** sponsor inference uh in in the Rush uh agent so that uh more people are able to

**[15:31]** agent so that uh more people are able to

**[15:31]** agent so that uh more people are able to experience this on you know their side

**[15:32]** experience this on you know their side

**[15:32]** experience this on you know their side projects and such.

**[15:35]** projects and such.

**[15:35]** projects and such. Okay. So, AMP is AMP. Uh we are like I

**[15:39]** Okay. So, AMP is AMP. Uh we are like I

**[15:39]** Okay. So, AMP is AMP. Uh we are like I said a we think of ourselves as like an

**[15:41]** said a we think of ourselves as like an

**[15:41]** said a we think of ourselves as like an agentic research lab. So we're not about

**[15:44]** agentic research lab. So we're not about

**[15:44]** agentic research lab. So we're not about uh hype. We don't do any sort of like

**[15:46]** uh hype. We don't do any sort of like

**[15:46]** uh hype. We don't do any sort of like paid developer influencer marketing. But

**[15:49]** paid developer influencer marketing. But

**[15:49]** paid developer influencer marketing. But I like to call out some cool people that

**[15:50]** I like to call out some cool people that

**[15:50]** I like to call out some cool people that I think are using AMP. Um because it it

**[15:53]** I think are using AMP. Um because it it

**[15:53]** I think are using AMP. Um because it it shows for the type of people that we're

**[15:55]** shows for the type of people that we're

**[15:55]** shows for the type of people that we're really selecting for. I I don't think

**[15:56]** really selecting for. I I don't think

**[15:56]** really selecting for. I I don't think AMP is for everyone uh at this point.

**[15:58]** AMP is for everyone uh at this point.

**[15:58]** AMP is for everyone uh at this point. We're really trying to target the the


### [16:00 - 17:00]

**[16:00]** We're really trying to target the the

**[16:00]** We're really trying to target the the like small percentage of people who want

**[16:01]** like small percentage of people who want

**[16:01]** like small percentage of people who want to live a little bit in the future. Um,

**[16:03]** to live a little bit in the future. Um,

**[16:03]** to live a little bit in the future. Um, and so we have folks like Mitchell

**[16:04]** and so we have folks like Mitchell

**[16:04]** and so we have folks like Mitchell Hashimoto, the uh the founder and and

**[16:07]** Hashimoto, the uh the founder and and

**[16:07]** Hashimoto, the uh the founder and and excepting

**[16:09]** excepting

**[16:09]** excepting Ghosty now. Uh, that's his uh kind of

**[16:11]** Ghosty now. Uh, that's his uh kind of

**[16:11]** Ghosty now. Uh, that's his uh kind of passion project and he's using AMP to

**[16:13]** passion project and he's using AMP to

**[16:13]** passion project and he's using AMP to drive a lot of the changes that he makes

**[16:15]** drive a lot of the changes that he makes

**[16:15]** drive a lot of the changes that he makes uh to that terminal. And then we also

**[16:17]** uh to that terminal. And then we also

**[16:17]** uh to that terminal. And then we also have folks like Hamill Hussein who's I

**[16:19]** have folks like Hamill Hussein who's I

**[16:19]** have folks like Hamill Hussein who's I think probably like the leading

**[16:20]** think probably like the leading

**[16:20]** think probably like the leading authority on AI evals. Um, and at least

**[16:23]** authority on AI evals. Um, and at least

**[16:23]** authority on AI evals. Um, and at least as of a couple weeks ago uh he was

**[16:25]** as of a couple weeks ago uh he was

**[16:25]** as of a couple weeks ago uh he was saying that AMP was his favorite coding

**[16:27]** saying that AMP was his favorite coding

**[16:27]** saying that AMP was his favorite coding agent. And so, uh, neither of them are

**[16:30]** agent. And so, uh, neither of them are

**[16:30]** agent. And so, uh, neither of them are on the team or, you know, have invested

**[16:32]** on the team or, you know, have invested

**[16:32]** on the team or, you know, have invested us in any way, but we're just thrilled

**[16:34]** us in any way, but we're just thrilled

**[16:34]** us in any way, but we're just thrilled that, you know, they seem to like like

**[16:36]** that, you know, they seem to like like

**[16:36]** that, you know, they seem to like like what we're building.

**[16:39]** what we're building.

**[16:39]** what we're building. And then if other folks are interested

**[16:41]** And then if other folks are interested

**[16:41]** And then if other folks are interested in in kind of like coming along with us

**[16:43]** in in kind of like coming along with us

**[16:43]** in in kind of like coming along with us in in in this journey and trying to push

**[16:46]** in in in this journey and trying to push

**[16:46]** in in in this journey and trying to push the frontier of what agents can do, uh,

**[16:49]** the frontier of what agents can do, uh,

**[16:49]** the frontier of what agents can do, uh, we've also started a community of

**[16:50]** we've also started a community of

**[16:50]** we've also started a community of builders. Um, and using AMP is not a

**[16:53]** builders. Um, and using AMP is not a

**[16:53]** builders. Um, and using AMP is not a requirement to join this community. It's

**[16:55]** requirement to join this community. It's

**[16:55]** requirement to join this community. It's run by uh Ryan Carson whose former

**[16:57]** run by uh Ryan Carson whose former

**[16:58]** run by uh Ryan Carson whose former startup uh Treehouse taught over a

**[16:59]** startup uh Treehouse taught over a

**[16:59]** startup uh Treehouse taught over a million people to code and now this is


### [17:00 - 18:00]

**[17:01]** million people to code and now this is

**[17:01]** million people to code and now this is his passion project. It's essentially

**[17:03]** his passion project. It's essentially

**[17:03]** his passion project. It's essentially like if you're building with agents and

**[17:05]** like if you're building with agents and

**[17:05]** like if you're building with agents and you're you're experimenting with how to

**[17:06]** you're you're experimenting with how to

**[17:06]** you're you're experimenting with how to push them further and further. There's

**[17:08]** push them further and further. There's

**[17:08]** push them further and further. There's Ryan right there. Um it it's all about

**[17:11]** Ryan right there. Um it it's all about

**[17:11]** Ryan right there. Um it it's all about kind of like tapping into that sense of

**[17:13]** kind of like tapping into that sense of

**[17:13]** kind of like tapping into that sense of awe and wonder with a peer group uh that

**[17:17]** awe and wonder with a peer group uh that

**[17:18]** awe and wonder with a peer group uh that is also uh leaning into that uh sense of

**[17:20]** is also uh leaning into that uh sense of

**[17:20]** is also uh leaning into that uh sense of of strangeness and and experimentation.

**[17:23]** of strangeness and and experimentation.

**[17:23]** of strangeness and and experimentation. So um what does this involve? It

**[17:26]** So um what does this involve? It

**[17:26]** So um what does this involve? It involves uh like regular interviews with

**[17:29]** involves uh like regular interviews with

**[17:30]** involves uh like regular interviews with people. We like to feature people who

**[17:31]** people. We like to feature people who

**[17:31]** people. We like to feature people who are building interesting things or using

**[17:32]** are building interesting things or using

**[17:32]** are building interesting things or using agents in interesting ways. Uh and we

**[17:35]** agents in interesting ways. Uh and we

**[17:35]** agents in interesting ways. Uh and we also do inerson events. We had a very

**[17:37]** also do inerson events. We had a very

**[17:37]** also do inerson events. We had a very nice dinner last night where we got a

**[17:38]** nice dinner last night where we got a

**[17:38]** nice dinner last night where we got a bunch of people together and had very

**[17:40]** bunch of people together and had very

**[17:40]** bunch of people together and had very interesting conversations spanning from

**[17:42]** interesting conversations spanning from

**[17:42]** interesting conversations spanning from you know actually building with coding

**[17:43]** you know actually building with coding

**[17:43]** you know actually building with coding agents to you know more philosophical

**[17:45]** agents to you know more philosophical

**[17:45]** agents to you know more philosophical discussions about uh the nature of AI

**[17:47]** discussions about uh the nature of AI

**[17:47]** discussions about uh the nature of AI and things like that. So um that's it

**[17:51]** and things like that. So um that's it

**[17:51]** and things like that. So um that's it for me. Uh hopefully this has in

**[17:53]** for me. Uh hopefully this has in

**[17:53]** for me. Uh hopefully this has in intrigued you. Again, I I don't expect

**[17:55]** intrigued you. Again, I I don't expect

**[17:55]** intrigued you. Again, I I don't expect all of you to be convinced that we are

**[17:57]** all of you to be convinced that we are

**[17:57]** all of you to be convinced that we are building the best Frontier coding agent,

**[17:58]** building the best Frontier coding agent,

**[17:58]** building the best Frontier coding agent, but at the very least, I hope I've kind


### [18:00 - 19:00]

**[18:01]** but at the very least, I hope I've kind

**[18:01]** but at the very least, I hope I've kind of demonstrated how we're leaning into

**[18:02]** of demonstrated how we're leaning into

**[18:02]** of demonstrated how we're leaning into the weird and thinking about things uh

**[18:04]** the weird and thinking about things uh

**[18:04]** the weird and thinking about things uh differently. So, if that's interesting

**[18:06]** differently. So, if that's interesting

**[18:06]** differently. So, if that's interesting to you, come say hi at our booth. Just

**[18:08]** to you, come say hi at our booth. Just

**[18:08]** to you, come say hi at our booth. Just look for the weird pipe piper man riding

**[18:10]** look for the weird pipe piper man riding

**[18:10]** look for the weird pipe piper man riding the golden fish. Thank you.

**[18:13]** the golden fish. Thank you.

**[18:13]** the golden fish. Thank you. [music]

**[18:29]** >> [music]

**[18:29]** >> [music] >> Heat.


