# 3 ingredients for building reliable enterprise agents - Harrison Chase, LangChain_LangGraph

**Video URL:** https://www.youtube.com/watch?v=kTnfJszFxCg

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** I want to talk today a little bit about

**[00:17]** I want to talk today a little bit about trying to build reliable agents in the

**[00:19]** trying to build reliable agents in the

**[00:19]** trying to build reliable agents in the enterprise. This is something we work

**[00:20]** enterprise. This is something we work

**[00:20]** enterprise. This is something we work with a bunch of people for both people

**[00:23]** with a bunch of people for both people

**[00:23]** with a bunch of people for both people building as developers inside of an

**[00:25]** building as developers inside of an

**[00:25]** building as developers inside of an enterprise looking to build agents for

**[00:27]** enterprise looking to build agents for

**[00:27]** enterprise looking to build agents for for their company but also people who

**[00:29]** for their company but also people who

**[00:29]** for their company but also people who are looking to build solutions and and

**[00:31]** are looking to build solutions and and

**[00:31]** are looking to build solutions and and and bring them and sell them into

**[00:33]** and bring them and sell them into

**[00:33]** and bring them and sell them into enterprises. Um and so I wanted to talk

**[00:36]** enterprises. Um and so I wanted to talk

**[00:36]** enterprises. Um and so I wanted to talk a little bit about some of what we see

**[00:38]** a little bit about some of what we see

**[00:38]** a little bit about some of what we see kind of being the the success tips and

**[00:40]** kind of being the the success tips and

**[00:40]** kind of being the the success tips and tricks for making this happen. So the

**[00:43]** tricks for making this happen. So the

**[00:43]** tricks for making this happen. So the the vision of the future that that I and

**[00:46]** the vision of the future that that I and

**[00:46]** the vision of the future that that I and other people I think have a have a

**[00:47]** other people I think have a have a

**[00:47]** other people I think have a have a similar view of for agents is that

**[00:49]** similar view of for agents is that

**[00:49]** similar view of for agents is that there'll be a lot of them. They'll be

**[00:50]** there'll be a lot of them. They'll be

**[00:50]** there'll be a lot of them. They'll be running around the enterprise doing

**[00:51]** running around the enterprise doing

**[00:51]** running around the enterprise doing different things. They'll they'll be you

**[00:53]** different things. They'll they'll be you

**[00:53]** different things. They'll they'll be you know an agent for every different task.

**[00:55]** know an agent for every different task.

**[00:55]** know an agent for every different task. We'll be coordinating with them. We'll

**[00:56]** We'll be coordinating with them. We'll

**[00:56]** We'll be coordinating with them. We'll be kind of like a manager, a supervisor

**[00:58]** be kind of like a manager, a supervisor

**[00:58]** be kind of like a manager, a supervisor and and so and so how do we get to that


### [01:00 - 02:00]

**[01:01]** and and so and so how do we get to that

**[01:01]** and and so and so how do we get to that vision and what uh what what parts of

**[01:05]** vision and what uh what what parts of

**[01:05]** vision and what uh what what parts of this will kind of like arrive before

**[01:08]** this will kind of like arrive before

**[01:08]** this will kind of like arrive before before the others? Um and and and so I

**[01:11]** before the others? Um and and and so I

**[01:11]** before the others? Um and and and so I was thinking about this question, what

**[01:12]** was thinking about this question, what

**[01:12]** was thinking about this question, what makes some agents kind of like succeed

**[01:15]** makes some agents kind of like succeed

**[01:15]** makes some agents kind of like succeed in the enterprise and and some fail. And

**[01:17]** in the enterprise and and some fail. And

**[01:17]** in the enterprise and and some fail. And I was chatting uh with with my friend

**[01:19]** I was chatting uh with with my friend

**[01:19]** I was chatting uh with with my friend Assaf, he's the head of AI at Monday. He

**[01:21]** Assaf, he's the head of AI at Monday. He

**[01:21]** Assaf, he's the head of AI at Monday. He also wrote GPT researcher. It's a great

**[01:23]** also wrote GPT researcher. It's a great

**[01:23]** also wrote GPT researcher. It's a great open source package. Uh I was chatting

**[01:25]** open source package. Uh I was chatting

**[01:25]** open source package. Uh I was chatting with him a few weeks ago. Um and uh a

**[01:28]** with him a few weeks ago. Um and uh a

**[01:28]** with him a few weeks ago. Um and uh a lot of the ideas here are borrowed from

**[01:29]** lot of the ideas here are borrowed from

**[01:30]** lot of the ideas here are borrowed from that conversation. He'll probably write

**[01:31]** that conversation. He'll probably write

**[01:31]** that conversation. He'll probably write a blog post about this uh with a

**[01:33]** a blog post about this uh with a

**[01:33]** a blog post about this uh with a slightly different framing which I would

**[01:35]** slightly different framing which I would

**[01:35]** slightly different framing which I would encourage everyone to to check out. So,

**[01:37]** encourage everyone to to check out. So,

**[01:37]** encourage everyone to to check out. So, I just want to give him a massive shout

**[01:38]** I just want to give him a massive shout

**[01:38]** I just want to give him a massive shout out and if you have the opportunity to

**[01:39]** out and if you have the opportunity to

**[01:39]** out and if you have the opportunity to to chat with him, you should definitely

**[01:41]** to chat with him, you should definitely

**[01:41]** to chat with him, you should definitely take that opportunity. Um, thinking

**[01:44]** take that opportunity. Um, thinking

**[01:44]** take that opportunity. Um, thinking about it from like first principles like

**[01:46]** about it from like first principles like

**[01:46]** about it from like first principles like what makes agents successful in the

**[01:49]** what makes agents successful in the

**[01:49]** what makes agents successful in the enterprise. Uh, it will make it

**[01:52]** enterprise. Uh, it will make it

**[01:52]** enterprise. Uh, it will make it successful, it will make it more likely

**[01:53]** successful, it will make it more likely

**[01:53]** successful, it will make it more likely to be adopted, the greater the value of

**[01:55]** to be adopted, the greater the value of

**[01:55]** to be adopted, the greater the value of the agent if it's right. These these

**[01:57]** the agent if it's right. These these

**[01:58]** the agent if it's right. These these probably aren't going to sound kind of

**[01:59]** probably aren't going to sound kind of

**[01:59]** probably aren't going to sound kind of like earthshattering, but hopefully


### [02:00 - 03:00]

**[02:00]** like earthshattering, but hopefully

**[02:00]** like earthshattering, but hopefully we'll get to some interesting points. If

**[02:02]** we'll get to some interesting points. If

**[02:02]** we'll get to some interesting points. If the more value it provides when it's

**[02:03]** the more value it provides when it's

**[02:03]** the more value it provides when it's right, the more likely it will be to be

**[02:05]** right, the more likely it will be to be

**[02:05]** right, the more likely it will be to be adopted.

**[02:06]** adopted.

**[02:06]** adopted. the more likely it is to have success,

**[02:09]** the more likely it is to have success,

**[02:09]** the more likely it is to have success, the more likely it will be to be

**[02:10]** the more likely it will be to be

**[02:10]** the more likely it will be to be adopted. And then the cost if it's

**[02:12]** adopted. And then the cost if it's

**[02:12]** adopted. And then the cost if it's wrong. If it if there's big costs when

**[02:14]** wrong. If it if there's big costs when

**[02:14]** wrong. If it if there's big costs when it's wrong, then it will be less likely

**[02:16]** it's wrong, then it will be less likely

**[02:16]** it's wrong, then it will be less likely to be adopted. So I think these are

**[02:18]** to be adopted. So I think these are

**[02:18]** to be adopted. So I think these are three kind of like ingredients which are

**[02:20]** three kind of like ingredients which are

**[02:20]** three kind of like ingredients which are pretty simple and pretty basic, but I

**[02:21]** pretty simple and pretty basic, but I

**[02:21]** pretty simple and pretty basic, but I think provide an interesting kind of

**[02:22]** think provide an interesting kind of

**[02:22]** think provide an interesting kind of like first principles approach for how

**[02:24]** like first principles approach for how

**[02:24]** like first principles approach for how to think about building agents and what

**[02:26]** to think about building agents and what

**[02:26]** to think about building agents and what types of agents kind of like find

**[02:28]** types of agents kind of like find

**[02:28]** types of agents kind of like find success. And and you know, I say in the

**[02:30]** success. And and you know, I say in the

**[02:30]** success. And and you know, I say in the enterprise here, but I also think this

**[02:31]** enterprise here, but I also think this

**[02:31]** enterprise here, but I also think this applies just generally within within uh

**[02:34]** applies just generally within within uh

**[02:34]** applies just generally within within uh kind of like society. Um if if we want

**[02:37]** kind of like society. Um if if we want

**[02:37]** kind of like society. Um if if we want to try to put this into a fun little

**[02:38]** to try to put this into a fun little

**[02:38]** to try to put this into a fun little equation, you know, we can multiply the

**[02:40]** equation, you know, we can multiply the

**[02:40]** equation, you know, we can multiply the the probability that something succeeds

**[02:42]** the probability that something succeeds

**[02:42]** the probability that something succeeds times the value that you get when it

**[02:44]** times the value that you get when it

**[02:44]** times the value that you get when it succeeds and then and then do the

**[02:45]** succeeds and then and then do the

**[02:45]** succeeds and then and then do the opposite for the cost when it's wrong.

**[02:47]** opposite for the cost when it's wrong.

**[02:47]** opposite for the cost when it's wrong. And of course, like this needs to be

**[02:48]** And of course, like this needs to be

**[02:48]** And of course, like this needs to be greater than than the cost of running

**[02:50]** greater than than the cost of running

**[02:50]** greater than than the cost of running the agent for you to want to put it into

**[02:51]** the agent for you to want to put it into

**[02:52]** the agent for you to want to put it into production. And so, uh yeah, fun fun

**[02:54]** production. And so, uh yeah, fun fun

**[02:54]** production. And so, uh yeah, fun fun little kind of like stats math formula.

**[02:58]** little kind of like stats math formula.

**[02:58]** little kind of like stats math formula. So, how can we build agents that score


### [03:00 - 04:00]

**[03:01]** So, how can we build agents that score

**[03:01]** So, how can we build agents that score higher on this? Because this is this

**[03:02]** higher on this? Because this is this

**[03:02]** higher on this? Because this is this hasn't been anything kind of like

**[03:03]** hasn't been anything kind of like

**[03:03]** hasn't been anything kind of like earthshattering so far. Hopefully, we'll

**[03:05]** earthshattering so far. Hopefully, we'll

**[03:05]** earthshattering so far. Hopefully, we'll get to some fun insights when we talk

**[03:06]** get to some fun insights when we talk

**[03:06]** get to some fun insights when we talk about how to make that make that

**[03:07]** about how to make that make that

**[03:07]** about how to make that make that equation kind of like go up. So, how can

**[03:11]** equation kind of like go up. So, how can

**[03:11]** equation kind of like go up. So, how can we increase the the the value of or of

**[03:15]** we increase the the the value of or of

**[03:15]** we increase the the the value of or of of things um when they go right and and

**[03:18]** of things um when they go right and and

**[03:18]** of things um when they go right and and what types of agents have higher value?

**[03:20]** what types of agents have higher value?

**[03:20]** what types of agents have higher value? So, so part of this is uh choosing kind

**[03:23]** So, so part of this is uh choosing kind

**[03:23]** So, so part of this is uh choosing kind of like problems where there is there is

**[03:25]** of like problems where there is there is

**[03:25]** of like problems where there is there is really high kind of like value. So a lot

**[03:27]** really high kind of like value. So a lot

**[03:27]** really high kind of like value. So a lot of the agents that have been successful

**[03:29]** of the agents that have been successful

**[03:29]** of the agents that have been successful so far, Harvey in the legal space is one

**[03:32]** so far, Harvey in the legal space is one

**[03:32]** so far, Harvey in the legal space is one of them. Um in the finance space we see

**[03:35]** of them. Um in the finance space we see

**[03:35]** of them. Um in the finance space we see stuff around research and summarization.

**[03:37]** stuff around research and summarization.

**[03:37]** stuff around research and summarization. These are high value work tasks. People

**[03:39]** These are high value work tasks. People

**[03:39]** These are high value work tasks. People pay a lot of money for for lawyers uh

**[03:42]** pay a lot of money for for lawyers uh

**[03:42]** pay a lot of money for for lawyers uh and and and for and for research and

**[03:44]** and and and for and for research and

**[03:44]** and and and for and for research and investment research. And so these are

**[03:46]** investment research. And so these are

**[03:46]** investment research. And so these are examples of what I would say kind of

**[03:47]** examples of what I would say kind of

**[03:47]** examples of what I would say kind of like high value tasks are.

**[03:51]** like high value tasks are.

**[03:51]** like high value tasks are. there's other ways to kind of like

**[03:52]** there's other ways to kind of like

**[03:52]** there's other ways to kind of like improve the value of what you're working

**[03:54]** improve the value of what you're working

**[03:54]** improve the value of what you're working on besides just switching kind of like

**[03:55]** on besides just switching kind of like

**[03:56]** on besides just switching kind of like the vertical completely and I think

**[03:57]** the vertical completely and I think

**[03:57]** the vertical completely and I think we're starting to see some of this

**[03:58]** we're starting to see some of this

**[03:58]** we're starting to see some of this especially more recently. So if we think


### [04:00 - 05:00]

**[04:00]** especially more recently. So if we think

**[04:00]** especially more recently. So if we think about rag or if we think about kind of

**[04:02]** about rag or if we think about kind of

**[04:02]** about rag or if we think about kind of like existing question or old older

**[04:05]** like existing question or old older

**[04:05]** like existing question or old older school question answering solutions they

**[04:07]** school question answering solutions they

**[04:07]** school question answering solutions they would often respond kind of like quickly

**[04:08]** would often respond kind of like quickly

**[04:08]** would often respond kind of like quickly ideally within 5 seconds and give you a

**[04:10]** ideally within 5 seconds and give you a

**[04:10]** ideally within 5 seconds and give you a quick answer and we're starting to see a

**[04:12]** quick answer and we're starting to see a

**[04:12]** quick answer and we're starting to see a trend towards things like deep research

**[04:14]** trend towards things like deep research

**[04:14]** trend towards things like deep research which go and run for an extended period

**[04:17]** which go and run for an extended period

**[04:17]** which go and run for an extended period of time. We're seeing the same with

**[04:18]** of time. We're seeing the same with

**[04:18]** of time. We're seeing the same with code. We start with cursor. It has kind

**[04:20]** code. We start with cursor. It has kind

**[04:20]** code. We start with cursor. It has kind of like inline autocomplete. Maybe some

**[04:22]** of like inline autocomplete. Maybe some

**[04:22]** of like inline autocomplete. Maybe some chat question answering there. In the

**[04:24]** chat question answering there. In the

**[04:24]** chat question answering there. In the past like three weeks, there's been what

**[04:26]** past like three weeks, there's been what

**[04:26]** past like three weeks, there's been what seven different examples of these

**[04:27]** seven different examples of these

**[04:27]** seven different examples of these ambient agents that run in the

**[04:29]** ambient agents that run in the

**[04:29]** ambient agents that run in the background for like hours at time. And I

**[04:31]** background for like hours at time. And I

**[04:31]** background for like hours at time. And I think this speaks to ways that people

**[04:32]** think this speaks to ways that people

**[04:32]** think this speaks to ways that people are trying to get their agents to

**[04:34]** are trying to get their agents to

**[04:34]** are trying to get their agents to provide more value. They're getting them

**[04:35]** provide more value. They're getting them

**[04:36]** provide more value. They're getting them to do more work. Um pretty pretty basic,

**[04:39]** to do more work. Um pretty pretty basic,

**[04:39]** to do more work. Um pretty pretty basic, but I do think that like as we have as

**[04:41]** but I do think that like as we have as

**[04:41]** but I do think that like as we have as we think about this future of agents

**[04:43]** we think about this future of agents

**[04:43]** we think about this future of agents working and what that means, that

**[04:44]** working and what that means, that

**[04:44]** working and what that means, that doesn't mean a co-pilot. That means

**[04:46]** doesn't mean a co-pilot. That means

**[04:46]** doesn't mean a co-pilot. That means something working more autonomously in

**[04:48]** something working more autonomously in

**[04:48]** something working more autonomously in the background doing more amounts of

**[04:50]** the background doing more amounts of

**[04:50]** the background doing more amounts of work. So besides kind of like focusing

**[04:54]** work. So besides kind of like focusing

**[04:54]** work. So besides kind of like focusing on areas or verticals that provide

**[04:56]** on areas or verticals that provide

**[04:56]** on areas or verticals that provide value, I think you can also absolutely

**[04:59]** value, I think you can also absolutely

**[04:59]** value, I think you can also absolutely reshift the the UI UX the interaction


### [05:00 - 06:00]

**[05:02]** reshift the the UI UX the interaction

**[05:02]** reshift the the UI UX the interaction pattern of what you're building to be

**[05:04]** pattern of what you're building to be

**[05:04]** pattern of what you're building to be kind of like more long-term and do more

**[05:06]** kind of like more long-term and do more

**[05:06]** kind of like more long-term and do more kind of like substantial patterns of

**[05:08]** kind of like substantial patterns of

**[05:08]** kind of like substantial patterns of work.

**[05:11]** work.

**[05:11]** work. Let's talk about now the probability of

**[05:12]** Let's talk about now the probability of

**[05:12]** Let's talk about now the probability of success. How do we make this go up? So

**[05:15]** success. How do we make this go up? So

**[05:15]** success. How do we make this go up? So the the the there's a few there's two

**[05:18]** the the the there's a few there's two

**[05:18]** the the the there's a few there's two different aspects I want to talk about

**[05:19]** different aspects I want to talk about

**[05:19]** different aspects I want to talk about here. One I think is about the

**[05:21]** here. One I think is about the

**[05:21]** here. One I think is about the reliability of agents. If you've built

**[05:23]** reliability of agents. If you've built

**[05:23]** reliability of agents. If you've built uh agents before, it's easy to get

**[05:26]** uh agents before, it's easy to get

**[05:26]** uh agents before, it's easy to get something that works in a prototype. It

**[05:27]** something that works in a prototype. It

**[05:28]** something that works in a prototype. It runs once great. You can make a video,

**[05:29]** runs once great. You can make a video,

**[05:29]** runs once great. You can make a video, put it on Twitter, but it's hard to make

**[05:30]** put it on Twitter, but it's hard to make

**[05:30]** put it on Twitter, but it's hard to make it work reliably, put it in in in

**[05:32]** it work reliably, put it in in in

**[05:32]** it work reliably, put it in in in production. And I think the the core

**[05:36]** production. And I think the the core

**[05:36]** production. And I think the the core thing that we've seen and and and by the

**[05:37]** thing that we've seen and and and by the

**[05:37]** thing that we've seen and and and by the way, for some parts of of of so for some

**[05:41]** way, for some parts of of of so for some

**[05:41]** way, for some parts of of of so for some types of agents, that's totally fine.

**[05:42]** types of agents, that's totally fine.

**[05:42]** types of agents, that's totally fine. Um, you can have agents that that run

**[05:46]** Um, you can have agents that that run

**[05:46]** Um, you can have agents that that run for a while and and kind of like you

**[05:49]** for a while and and kind of like you

**[05:49]** for a while and and kind of like you don't know what they do and and that's

**[05:50]** don't know what they do and and that's

**[05:50]** don't know what they do and and that's totally fine. Especially in the

**[05:52]** totally fine. Especially in the

**[05:52]** totally fine. Especially in the enterprise, we see often times that

**[05:54]** enterprise, we see often times that

**[05:54]** enterprise, we see often times that people want more predictability, more

**[05:56]** people want more predictability, more

**[05:56]** people want more predictability, more control over what steps actually happen

**[05:58]** control over what steps actually happen

**[05:58]** control over what steps actually happen inside the agents. Maybe they always


### [06:00 - 07:00]

**[06:00]** inside the agents. Maybe they always

**[06:00]** inside the agents. Maybe they always want to do step A after step B. And so

**[06:02]** want to do step A after step B. And so

**[06:02]** want to do step A after step B. And so if you prompt an agent to do that,

**[06:05]** if you prompt an agent to do that,

**[06:05]** if you prompt an agent to do that, great. It might do that like 90% of the

**[06:06]** great. It might do that like 90% of the

**[06:06]** great. It might do that like 90% of the time. You don't know what the LLM will

**[06:08]** time. You don't know what the LLM will

**[06:08]** time. You don't know what the LLM will do. If you put that in a deterministic

**[06:10]** do. If you put that in a deterministic

**[06:10]** do. If you put that in a deterministic kind of like workflow or code, then it

**[06:12]** kind of like workflow or code, then it

**[06:12]** kind of like workflow or code, then it will always do that. And so, especially

**[06:14]** will always do that. And so, especially

**[06:14]** will always do that. And so, especially in the enterprise, we see that there are

**[06:17]** in the enterprise, we see that there are

**[06:17]** in the enterprise, we see that there are workflow like things where you need more

**[06:19]** workflow like things where you need more

**[06:19]** workflow like things where you need more controllability, more predictability

**[06:21]** controllability, more predictability

**[06:21]** controllability, more predictability than you get by just prompting. And so,

**[06:23]** than you get by just prompting. And so,

**[06:23]** than you get by just prompting. And so, what we've seen is more the solution for

**[06:26]** what we've seen is more the solution for

**[06:26]** what we've seen is more the solution for this is basically make more and more of

**[06:27]** this is basically make more and more of

**[06:27]** this is basically make more and more of your agent deterministic.

**[06:30]** your agent deterministic.

**[06:30]** your agent deterministic. There's this concept of kind of like

**[06:31]** There's this concept of kind of like

**[06:31]** There's this concept of kind of like workflows versus agents. Anthropic wrote

**[06:33]** workflows versus agents. Anthropic wrote

**[06:33]** workflows versus agents. Anthropic wrote a great blog post on this that I'd

**[06:35]** a great blog post on this that I'd

**[06:35]** a great blog post on this that I'd encourage you to check out. Um I I would

**[06:38]** encourage you to check out. Um I I would

**[06:38]** encourage you to check out. Um I I would argue that instead of workflows versus

**[06:39]** argue that instead of workflows versus

**[06:39]** argue that instead of workflows versus agents, it's it's oftentimes workflows

**[06:41]** agents, it's it's oftentimes workflows

**[06:41]** agents, it's it's oftentimes workflows and agents. Uh we see that parts of an

**[06:45]** and agents. Uh we see that parts of an

**[06:45]** and agents. Uh we see that parts of an agentic system are sometimes looping

**[06:47]** agentic system are sometimes looping

**[06:47]** agentic system are sometimes looping calling a tool and sometimes they're

**[06:49]** calling a tool and sometimes they're

**[06:49]** calling a tool and sometimes they're just doing A after B after C. An example

**[06:51]** just doing A after B after C. An example

**[06:51]** just doing A after B after C. An example of this is when you think about

**[06:52]** of this is when you think about

**[06:52]** of this is when you think about multi-agent architectures. If you think

**[06:54]** multi-agent architectures. If you think

**[06:54]** multi-agent architectures. If you think about an architecture that has agent A

**[06:56]** about an architecture that has agent A

**[06:56]** about an architecture that has agent A and then after agent A finishes, you

**[06:58]** and then after agent A finishes, you

**[06:58]** and then after agent A finishes, you always call agent B. Is is that a


### [07:00 - 08:00]

**[07:00]** always call agent B. Is is that a

**[07:00]** always call agent B. Is is that a workflow? Is that an agent? It's it's

**[07:02]** workflow? Is that an agent? It's it's

**[07:02]** workflow? Is that an agent? It's it's this middle ground. And so as we think

**[07:04]** this middle ground. And so as we think

**[07:04]** this middle ground. And so as we think about building tools for this this this

**[07:06]** about building tools for this this this

**[07:06]** about building tools for this this this future, uh, one of the one of the things

**[07:08]** future, uh, one of the one of the things

**[07:08]** future, uh, one of the one of the things that we've released is Langraph.

**[07:10]** that we've released is Langraph.

**[07:10]** that we've released is Langraph. Langraph is an agent framework. It's

**[07:12]** Langraph is an agent framework. It's

**[07:12]** Langraph is an agent framework. It's very different from other agent

**[07:13]** very different from other agent

**[07:13]** very different from other agent frameworks where it really leans in to

**[07:15]** frameworks where it really leans in to

**[07:15]** frameworks where it really leans in to this spectrum of workflows and agents

**[07:18]** this spectrum of workflows and agents

**[07:18]** this spectrum of workflows and agents and allows you to be wherever wherever

**[07:20]** and allows you to be wherever wherever

**[07:20]** and allows you to be wherever wherever is best for your application on that on

**[07:22]** is best for your application on that on

**[07:22]** is best for your application on that on that kind of like curve. And where where

**[07:24]** that kind of like curve. And where where

**[07:24]** that kind of like curve. And where where on that curve is best totally depends on

**[07:26]** on that curve is best totally depends on

**[07:26]** on that curve is best totally depends on kind of like the application that you're

**[07:27]** kind of like the application that you're

**[07:28]** kind of like the application that you're building.

**[07:30]** building.

**[07:30]** building. There there there's another thing um

**[07:32]** There there there's another thing um

**[07:32]** There there there's another thing um that that is different from just

**[07:33]** that that is different from just

**[07:34]** that that is different from just building and changing the agent. And I

**[07:35]** building and changing the agent. And I

**[07:35]** building and changing the agent. And I think there's uh there's oftentimes

**[07:37]** think there's uh there's oftentimes

**[07:37]** think there's uh there's oftentimes really high error bars that people have

**[07:41]** really high error bars that people have

**[07:41]** really high error bars that people have when they think about how likely an

**[07:42]** when they think about how likely an

**[07:42]** when they think about how likely an agent is to work. I think this

**[07:44]** agent is to work. I think this

**[07:44]** agent is to work. I think this technology is new um when when uh trying

**[07:47]** technology is new um when when uh trying

**[07:47]** technology is new um when when uh trying to get something built or approved or

**[07:49]** to get something built or approved or

**[07:49]** to get something built or approved or put into production inside an

**[07:50]** put into production inside an

**[07:50]** put into production inside an enterprise. think there's a lot of um

**[07:52]** enterprise. think there's a lot of um

**[07:52]** enterprise. think there's a lot of um uncertainty and and and and fear around

**[07:55]** uncertainty and and and and fear around

**[07:55]** uncertainty and and and and fear around this um and and I think that relates to

**[07:58]** this um and and I think that relates to

**[07:58]** this um and and I think that relates to this fundamental kind of like


### [08:00 - 09:00]

**[08:01]** this fundamental kind of like

**[08:01]** this fundamental kind of like uncertainty around how this agent is

**[08:02]** uncertainty around how this agent is

**[08:02]** uncertainty around how this agent is kind of like performing and so besides

**[08:04]** kind of like performing and so besides

**[08:04]** kind of like performing and so besides just like making it better a really

**[08:07]** just like making it better a really

**[08:07]** just like making it better a really important thing that we see to do inside

**[08:09]** important thing that we see to do inside

**[08:09]** important thing that we see to do inside the enterprise whether you're you're

**[08:11]** the enterprise whether you're you're

**[08:11]** the enterprise whether you're you're you're bringing a third party agent and

**[08:13]** you're bringing a third party agent and

**[08:13]** you're bringing a third party agent and selling it as a service or whether

**[08:15]** selling it as a service or whether

**[08:15]** selling it as a service or whether you're building inside uh uh the

**[08:17]** you're building inside uh uh the

**[08:17]** you're building inside uh uh the enterprise yourself is to work to kind

**[08:19]** enterprise yourself is to work to kind

**[08:20]** enterprise yourself is to work to kind of reduce the the the way that people

**[08:22]** of reduce the the the way that people

**[08:22]** of reduce the the the way that people see the error bars of how this agent

**[08:24]** see the error bars of how this agent

**[08:24]** see the error bars of how this agent performs. Um, so what I mean by that

**[08:26]** performs. Um, so what I mean by that

**[08:26]** performs. Um, so what I mean by that specifically is that this is where

**[08:28]** specifically is that this is where

**[08:28]** specifically is that this is where observability and eval plays a slightly

**[08:31]** observability and eval plays a slightly

**[08:32]** observability and eval plays a slightly different role than than we would maybe

**[08:34]** different role than than we would maybe

**[08:34]** different role than than we would maybe think or we would maybe intend. So we we

**[08:37]** think or we would maybe intend. So we we

**[08:37]** think or we would maybe intend. So we we have a we have an observability and eval

**[08:38]** have a we have an observability and eval

**[08:38]** have a we have an observability and eval solution called Lang Smith. We built it

**[08:40]** solution called Lang Smith. We built it

**[08:40]** solution called Lang Smith. We built it for developers so that they could see

**[08:41]** for developers so that they could see

**[08:41]** for developers so that they could see what's going on inside their agent. It's

**[08:43]** what's going on inside their agent. It's

**[08:43]** what's going on inside their agent. It's also proved really really valuable for

**[08:46]** also proved really really valuable for

**[08:46]** also proved really really valuable for communicating to ex external

**[08:47]** communicating to ex external

**[08:48]** communicating to ex external shareholders what's going on inside the

**[08:50]** shareholders what's going on inside the

**[08:50]** shareholders what's going on inside the agent and and how the agent performs and

**[08:53]** agent and and how the agent performs and

**[08:53]** agent and and how the agent performs and where it messes up and where it doesn't

**[08:54]** where it messes up and where it doesn't

**[08:54]** where it messes up and where it doesn't mess up and and basically communicate

**[08:56]** mess up and and basically communicate

**[08:56]** mess up and and basically communicate these kind of like patterns. Um and so

**[08:59]** these kind of like patterns. Um and so

**[08:59]** these kind of like patterns. Um and so and so again like the observability part


### [09:00 - 10:00]

**[09:00]** and so again like the observability part

**[09:00]** and so again like the observability part you can just see every step that's

**[09:02]** you can just see every step that's

**[09:02]** you can just see every step that's happening inside the agent. This reduces

**[09:04]** happening inside the agent. This reduces

**[09:04]** happening inside the agent. This reduces the kind of like uncertainty that people

**[09:05]** the kind of like uncertainty that people

**[09:05]** the kind of like uncertainty that people have around what the agent and what it's

**[09:07]** have around what the agent and what it's

**[09:07]** have around what the agent and what it's actually doing. They can see that it's

**[09:08]** actually doing. They can see that it's

**[09:08]** actually doing. They can see that it's making three five LM calls. It's not

**[09:11]** making three five LM calls. It's not

**[09:11]** making three five LM calls. It's not just one. they're actually being really

**[09:12]** just one. they're actually being really

**[09:12]** just one. they're actually being really thoughtful about the steps that are

**[09:13]** thoughtful about the steps that are

**[09:13]** thoughtful about the steps that are happening and then you can benchmark it

**[09:15]** happening and then you can benchmark it

**[09:15]** happening and then you can benchmark it against different things. Um, and so

**[09:18]** against different things. Um, and so

**[09:18]** against different things. Um, and so there there's a a great story of a user

**[09:20]** there there's a a great story of a user

**[09:20]** there there's a a great story of a user of ours who used Lang Smith initially to

**[09:23]** of ours who used Lang Smith initially to

**[09:23]** of ours who used Lang Smith initially to build the agent, but then but then

**[09:24]** build the agent, but then but then

**[09:24]** build the agent, but then but then brought it and showed it to the review

**[09:26]** brought it and showed it to the review

**[09:26]** brought it and showed it to the review panel as they were trying to get their

**[09:27]** panel as they were trying to get their

**[09:27]** panel as they were trying to get their agent approved to go into production.

**[09:29]** agent approved to go into production.

**[09:29]** agent approved to go into production. and they they ended the meeting under

**[09:31]** and they they ended the meeting under

**[09:31]** and they they ended the meeting under time, which almost never happens uh if

**[09:33]** time, which almost never happens uh if

**[09:33]** time, which almost never happens uh if if you've been to these review panels.

**[09:35]** if you've been to these review panels.

**[09:35]** if you've been to these review panels. And and and they showed them basically

**[09:37]** And and and they showed them basically

**[09:37]** And and and they showed them basically everything everything inside Linkmith

**[09:39]** everything everything inside Linkmith

**[09:39]** everything everything inside Linkmith and it helped reduce kind of like the

**[09:41]** and it helped reduce kind of like the

**[09:41]** and it helped reduce kind of like the the perception or the risk that people

**[09:43]** the perception or the risk that people

**[09:43]** the perception or the risk that people had um of of of these agents.

**[09:48]** had um of of of these agents.

**[09:48]** had um of of of these agents. And then uh the the the last thing I

**[09:50]** And then uh the the the last thing I

**[09:50]** And then uh the the the last thing I want about talk about is is kind of like

**[09:52]** want about talk about is is kind of like

**[09:52]** want about talk about is is kind of like the cost of something if it's wrong. Um

**[09:56]** the cost of something if it's wrong. Um

**[09:56]** the cost of something if it's wrong. Um there's similar to kind of like the

**[09:58]** there's similar to kind of like the

**[09:58]** there's similar to kind of like the probability of things being right. This


### [10:00 - 11:00]

**[10:00]** probability of things being right. This

**[10:00]** probability of things being right. This this plays an outsized kind of like role

**[10:03]** this plays an outsized kind of like role

**[10:03]** this plays an outsized kind of like role in especially in larger enterprises

**[10:05]** in especially in larger enterprises

**[10:05]** in especially in larger enterprises among review boards and and and

**[10:06]** among review boards and and and

**[10:06]** among review boards and and and managers. People's like perception of

**[10:08]** managers. People's like perception of

**[10:08]** managers. People's like perception of these agents. People hear stories of

**[10:09]** these agents. People hear stories of

**[10:09]** these agents. People hear stories of agents going wild and causing kind of

**[10:11]** agents going wild and causing kind of

**[10:11]** agents going wild and causing kind of like brain uh brand damage or or you

**[10:14]** like brain uh brand damage or or you

**[10:14]** like brain uh brand damage or or you know giving away things for free.

**[10:15]** know giving away things for free.

**[10:15]** know giving away things for free. there's this I think there's an outsized

**[10:18]** there's this I think there's an outsized

**[10:18]** there's this I think there's an outsized perception of of of kind of like what

**[10:21]** perception of of of kind of like what

**[10:21]** perception of of of kind of like what could be what could happen if things go

**[10:24]** could be what could happen if things go

**[10:24]** could be what could happen if things go bad and and so I think there's a few

**[10:28]** bad and and so I think there's a few

**[10:28]** bad and and so I think there's a few kind of like UI UX tricks that people

**[10:31]** kind of like UI UX tricks that people

**[10:31]** kind of like UI UX tricks that people are doing and that successful agents

**[10:32]** are doing and that successful agents

**[10:32]** are doing and that successful agents have to kind of like just make this a a

**[10:35]** have to kind of like just make this a a

**[10:35]** have to kind of like just make this a a non-issue. So so one is just make it

**[10:37]** non-issue. So so one is just make it

**[10:37]** non-issue. So so one is just make it easy to reverse the changes that the

**[10:39]** easy to reverse the changes that the

**[10:39]** easy to reverse the changes that the agent makes. So if you think about code

**[10:41]** agent makes. So if you think about code

**[10:41]** agent makes. So if you think about code and this is a screenshot of of of replet

**[10:43]** and this is a screenshot of of of replet

**[10:43]** and this is a screenshot of of of replet agent it's it's a it's a it's a diff

**[10:45]** agent it's it's a it's a it's a diff

**[10:46]** agent it's it's a it's a it's a diff that it generates a PR code's really

**[10:47]** that it generates a PR code's really

**[10:48]** that it generates a PR code's really easy to revert you you go back to the

**[10:49]** easy to revert you you go back to the

**[10:49]** easy to revert you you go back to the previous commit and so I think I think

**[10:51]** previous commit and so I think I think

**[10:51]** previous commit and so I think I think that's part of the reason why we see

**[10:53]** that's part of the reason why we see

**[10:53]** that's part of the reason why we see code being one of the first uh kind of

**[10:55]** code being one of the first uh kind of

**[10:55]** code being one of the first uh kind of like real places that you can apply

**[10:57]** like real places that you can apply

**[10:57]** like real places that you can apply agents besides the fact that the models

**[10:59]** agents besides the fact that the models

**[10:59]** agents besides the fact that the models are trained on it is also that when you


### [11:00 - 12:00]

**[11:01]** are trained on it is also that when you

**[11:01]** are trained on it is also that when you when you use these agents you create all

**[11:03]** when you use these agents you create all

**[11:03]** when you use these agents you create all these commits and and and and well it

**[11:05]** these commits and and and and well it

**[11:06]** these commits and and and and well it depends how you do it replet does it in

**[11:07]** depends how you do it replet does it in

**[11:07]** depends how you do it replet does it in a very clever way where every time they

**[11:09]** a very clever way where every time they

**[11:09]** a very clever way where every time they change a file they save it as a new

**[11:10]** change a file they save it as a new

**[11:10]** change a file they save it as a new commit. So you can always go back, you

**[11:11]** commit. So you can always go back, you

**[11:11]** commit. So you can always go back, you can always revert kind of like what the

**[11:13]** can always revert kind of like what the

**[11:13]** can always revert kind of like what the agent does. Um and then and then the

**[11:15]** agent does. Um and then and then the

**[11:15]** agent does. Um and then and then the second part is is having a human in the

**[11:17]** second part is is having a human in the

**[11:17]** second part is is having a human in the loop. So rather than uh you know merging

**[11:21]** loop. So rather than uh you know merging

**[11:21]** loop. So rather than uh you know merging uh code changes into into main directly,

**[11:24]** uh code changes into into main directly,

**[11:24]** uh code changes into into main directly, open up PR that's putting the human in

**[11:25]** open up PR that's putting the human in

**[11:25]** open up PR that's putting the human in the loop. And so then the the the effect

**[11:28]** the loop. And so then the the the effect

**[11:28]** the loop. And so then the the the effect of the agent is it's not kind of like

**[11:30]** of the agent is it's not kind of like

**[11:30]** of the agent is it's not kind of like making changes. There's the human who's

**[11:31]** making changes. There's the human who's

**[11:32]** making changes. There's the human who's kind of like approving what the agent

**[11:33]** kind of like approving what the agent

**[11:33]** kind of like approving what the agent does. And this seems uh uh uh maybe a

**[11:36]** does. And this seems uh uh uh maybe a

**[11:36]** does. And this seems uh uh uh maybe a little subtle, but I think it completely

**[11:38]** little subtle, but I think it completely

**[11:38]** little subtle, but I think it completely changes the cost calculations in

**[11:40]** changes the cost calculations in

**[11:40]** changes the cost calculations in people's minds about what the costs of

**[11:41]** people's minds about what the costs of

**[11:42]** people's minds about what the costs of the agent doing something bad is because

**[11:44]** the agent doing something bad is because

**[11:44]** the agent doing something bad is because now it's reversible and you have a human

**[11:46]** now it's reversible and you have a human

**[11:46]** now it's reversible and you have a human who's going to prevent it from even

**[11:47]** who's going to prevent it from even

**[11:47]** who's going to prevent it from even going in in the first place if it's bad.

**[11:50]** going in in the first place if it's bad.

**[11:50]** going in in the first place if it's bad. Um and and so human in the loop is one

**[11:51]** Um and and so human in the loop is one

**[11:52]** Um and and so human in the loop is one of the big things that we see uh people

**[11:54]** of the big things that we see uh people

**[11:54]** of the big things that we see uh people selling into enterprises and building

**[11:56]** selling into enterprises and building

**[11:56]** selling into enterprises and building inside enterprises really leaning into.

**[11:59]** inside enterprises really leaning into.

**[11:59]** inside enterprises really leaning into. So to make this a little bit more


### [12:00 - 13:00]

**[12:01]** So to make this a little bit more

**[12:01]** So to make this a little bit more concrete, what are some examples of

**[12:02]** concrete, what are some examples of

**[12:02]** concrete, what are some examples of this? I think deep research is a pretty

**[12:05]** this? I think deep research is a pretty

**[12:05]** this? I think deep research is a pretty good example of this. If we think about

**[12:06]** good example of this. If we think about

**[12:06]** good example of this. If we think about this, there is a period of time up front

**[12:10]** this, there is a period of time up front

**[12:10]** this, there is a period of time up front when you're messaging with deep research

**[12:11]** when you're messaging with deep research

**[12:12]** when you're messaging with deep research that you go back and forth. It asks you

**[12:13]** that you go back and forth. It asks you

**[12:13]** that you go back and forth. It asks you follow-up questions and you kind of like

**[12:14]** follow-up questions and you kind of like

**[12:14]** follow-up questions and you kind of like calibrate on what you want to research.

**[12:16]** calibrate on what you want to research.

**[12:16]** calibrate on what you want to research. That puts kind of like the human in the

**[12:18]** That puts kind of like the human in the

**[12:18]** That puts kind of like the human in the loop. It also it makes sure that it gets

**[12:20]** loop. It also it makes sure that it gets

**[12:20]** loop. It also it makes sure that it gets a better result. So, it increases kind

**[12:22]** a better result. So, it increases kind

**[12:22]** a better result. So, it increases kind of like the value that you're going to

**[12:23]** of like the value that you're going to

**[12:23]** of like the value that you're going to get from the report because it's more

**[12:24]** get from the report because it's more

**[12:24]** get from the report because it's more aligned with what you actually want. And

**[12:26]** aligned with what you actually want. And

**[12:26]** aligned with what you actually want. And then dur deep research it doesn't you

**[12:28]** then dur deep research it doesn't you

**[12:28]** then dur deep research it doesn't you know take this and publish it as a blog

**[12:30]** know take this and publish it as a blog

**[12:30]** know take this and publish it as a blog out in the internet or doesn't take it

**[12:32]** out in the internet or doesn't take it

**[12:32]** out in the internet or doesn't take it and email it to your clients. It

**[12:33]** and email it to your clients. It

**[12:33]** and email it to your clients. It produces just you know a report that you

**[12:35]** produces just you know a report that you

**[12:35]** produces just you know a report that you can read and decide what to do with. So

**[12:37]** can read and decide what to do with. So

**[12:37]** can read and decide what to do with. So it's not actually doing anything. It's

**[12:38]** it's not actually doing anything. It's

**[12:38]** it's not actually doing anything. It's up to you to take that and and and do

**[12:40]** up to you to take that and and and do

**[12:40]** up to you to take that and and and do things. I think similarly when you think

**[12:42]** things. I think similarly when you think

**[12:42]** things. I think similarly when you think about uh code it's it's it's another

**[12:45]** about uh code it's it's it's another

**[12:45]** about uh code it's it's it's another great example of uh so claude code also

**[12:48]** great example of uh so claude code also

**[12:48]** great example of uh so claude code also has uh this ability where it asks

**[12:50]** has uh this ability where it asks

**[12:50]** has uh this ability where it asks questions. It clarifies things. um this

**[12:53]** questions. It clarifies things. um this

**[12:53]** questions. It clarifies things. um this is to kind of like uh both keep the

**[12:54]** is to kind of like uh both keep the

**[12:54]** is to kind of like uh both keep the human in the loop but also make sure

**[12:55]** human in the loop but also make sure

**[12:55]** human in the loop but also make sure that it yields better results and then

**[12:57]** that it yields better results and then

**[12:57]** that it yields better results and then again with code maybe you're not making

**[12:59]** again with code maybe you're not making

**[12:59]** again with code maybe you're not making a commit every time you change things


### [13:00 - 14:00]

**[13:01]** a commit every time you change things

**[13:01]** a commit every time you change things but it's it's on a separate branch you

**[13:02]** but it's it's on a separate branch you

**[13:02]** but it's it's on a separate branch you open a PR you're not pushing kind of

**[13:03]** open a PR you're not pushing kind of

**[13:04]** open a PR you're not pushing kind of like directly to master and so I think

**[13:06]** like directly to master and so I think

**[13:06]** like directly to master and so I think these are these are examples of things

**[13:08]** these are these are examples of things

**[13:08]** these are these are examples of things in the general industry that kind of

**[13:10]** in the general industry that kind of

**[13:10]** in the general industry that kind of like follow some of of of these patterns

**[13:14]** like follow some of of of these patterns

**[13:14]** like follow some of of of these patterns so okay so we've figured out a few

**[13:15]** so okay so we've figured out a few

**[13:16]** so okay so we've figured out a few levers that we can kind of like pull to

**[13:17]** levers that we can kind of like pull to

**[13:17]** levers that we can kind of like pull to to kind of like try to make our agents

**[13:20]** to kind of like try to make our agents

**[13:20]** to kind of like try to make our agents more interesting to to be deployed in in

**[13:23]** more interesting to to be deployed in in

**[13:23]** more interesting to to be deployed in in the enterprise, what next? What next is

**[13:24]** the enterprise, what next? What next is

**[13:24]** the enterprise, what next? What next is kind of like how how do we scale that?

**[13:27]** kind of like how how do we scale that?

**[13:27]** kind of like how how do we scale that? So if if this kind of like has has kind

**[13:29]** So if if this kind of like has has kind

**[13:29]** So if if this kind of like has has kind of like positive value, then what we

**[13:31]** of like positive value, then what we

**[13:31]** of like positive value, then what we really want to do is just multiply this

**[13:33]** really want to do is just multiply this

**[13:33]** really want to do is just multiply this a bunch and scale it up a bunch. And I

**[13:35]** a bunch and scale it up a bunch. And I

**[13:35]** a bunch and scale it up a bunch. And I think this speaks to the the concept of

**[13:37]** think this speaks to the the concept of

**[13:37]** think this speaks to the the concept of kind of like ambient agents. Um which is

**[13:41]** kind of like ambient agents. Um which is

**[13:41]** kind of like ambient agents. Um which is uh when we think about agents working uh

**[13:43]** uh when we think about agents working uh

**[13:43]** uh when we think about agents working uh you know this futuristic view, agents

**[13:45]** you know this futuristic view, agents

**[13:45]** you know this futuristic view, agents working in an enterprise doing things in

**[13:47]** working in an enterprise doing things in

**[13:47]** working in an enterprise doing things in the background, they're doing things in

**[13:48]** the background, they're doing things in

**[13:48]** the background, they're doing things in the background. They're not being kicked

**[13:49]** the background. They're not being kicked

**[13:49]** the background. They're not being kicked off by humans kind of like still in the

**[13:52]** off by humans kind of like still in the

**[13:52]** off by humans kind of like still in the loop. They're being triggered by by by

**[13:54]** loop. They're being triggered by by by

**[13:54]** loop. They're being triggered by by by by different events. Um, and I think the

**[13:57]** by different events. Um, and I think the

**[13:57]** by different events. Um, and I think the reason that this is so powerful is that

**[13:58]** reason that this is so powerful is that

**[13:58]** reason that this is so powerful is that it scales up this positive expected


### [14:00 - 15:00]

**[14:01]** it scales up this positive expected

**[14:01]** it scales up this positive expected value thing even more um than than we

**[14:03]** value thing even more um than than we

**[14:03]** value thing even more um than than we can. Like I can only really have one

**[14:05]** can. Like I can only really have one

**[14:05]** can. Like I can only really have one maybe I can have two chat boxes open at

**[14:07]** maybe I can have two chat boxes open at

**[14:07]** maybe I can have two chat boxes open at the same time, but now there can be

**[14:09]** the same time, but now there can be

**[14:09]** the same time, but now there can be there can be, you know, hundreds of

**[14:10]** there can be, you know, hundreds of

**[14:10]** there can be, you know, hundreds of these running in the background. And so

**[14:12]** these running in the background. And so

**[14:12]** these running in the background. And so when we think about the difference

**[14:13]** when we think about the difference

**[14:13]** when we think about the difference between chat agents, which I would argue

**[14:15]** between chat agents, which I would argue

**[14:15]** between chat agents, which I would argue we've we've mostly seen, and ambient

**[14:17]** we've we've mostly seen, and ambient

**[14:17]** we've we've mostly seen, and ambient agents, one one big difference is

**[14:19]** agents, one one big difference is

**[14:19]** agents, one one big difference is ambient agents are triggered by events

**[14:21]** ambient agents are triggered by events

**[14:21]** ambient agents are triggered by events that lets us scale ourselves. Instead of

**[14:22]** that lets us scale ourselves. Instead of

**[14:22]** that lets us scale ourselves. Instead of a onetoone, it's now a one to many

**[14:24]** a onetoone, it's now a one to many

**[14:24]** a onetoone, it's now a one to many conversation that we can be happening.

**[14:26]** conversation that we can be happening.

**[14:26]** conversation that we can be happening. Um and and so the concurrencies of these

**[14:28]** Um and and so the concurrencies of these

**[14:28]** Um and and so the concurrencies of these agents that can be running goes from one

**[14:29]** agents that can be running goes from one

**[14:29]** agents that can be running goes from one to to unlimited.

**[14:31]** to to unlimited.

**[14:31]** to to unlimited. Um the latency requirements also change.

**[14:34]** Um the latency requirements also change.

**[14:34]** Um the latency requirements also change. So when chat you have this kind of like

**[14:36]** So when chat you have this kind of like

**[14:36]** So when chat you have this kind of like UX expectation that it responds really

**[14:39]** UX expectation that it responds really

**[14:39]** UX expectation that it responds really really quickly and that's not the case

**[14:41]** really quickly and that's not the case

**[14:41]** really quickly and that's not the case with with ambient agents because they're

**[14:42]** with with ambient agents because they're

**[14:42]** with with ambient agents because they're triggered without you even knowing. So

**[14:44]** triggered without you even knowing. So

**[14:44]** triggered without you even knowing. So like how how do you how do you know how

**[14:46]** like how how do you how do you know how

**[14:46]** like how how do you how do you know how do you even care how long it's running?

**[14:47]** do you even care how long it's running?

**[14:47]** do you even care how long it's running? And so you can what does this let you

**[14:49]** And so you can what does this let you

**[14:49]** And so you can what does this let you do? Why does this matter? This lets you

**[14:50]** do? Why does this matter? This lets you

**[14:50]** do? Why does this matter? This lets you do more complex operations. So you can

**[14:53]** do more complex operations. So you can

**[14:53]** do more complex operations. So you can do more things. So you can start to

**[14:54]** do more things. So you can start to

**[14:54]** do more things. So you can start to build build up kind of like a bigger

**[14:56]** build build up kind of like a bigger

**[14:56]** build build up kind of like a bigger body of work. You can go from kind of

**[14:58]** body of work. You can go from kind of

**[14:58]** body of work. You can go from kind of like changing one line of code to

**[14:59]** like changing one line of code to

**[14:59]** like changing one line of code to changing a whole file or making a new


### [15:00 - 16:00]

**[15:01]** changing a whole file or making a new

**[15:01]** changing a whole file or making a new kind of like repo or or any of that. And

**[15:03]** kind of like repo or or any of that. And

**[15:03]** kind of like repo or or any of that. And so instead of this agent just responding

**[15:05]** so instead of this agent just responding

**[15:05]** so instead of this agent just responding directly or calling like a single tool

**[15:06]** directly or calling like a single tool

**[15:06]** directly or calling like a single tool call, which usually happens in these

**[15:07]** call, which usually happens in these

**[15:07]** call, which usually happens in these chat applications because of the latency

**[15:09]** chat applications because of the latency

**[15:09]** chat applications because of the latency requirements, it can now do these more

**[15:11]** requirements, it can now do these more

**[15:11]** requirements, it can now do these more complex things. And so the value can

**[15:13]** complex things. And so the value can

**[15:13]** complex things. And so the value can start kind of like increasing in terms

**[15:14]** start kind of like increasing in terms

**[15:14]** start kind of like increasing in terms of what you're doing. And then the the

**[15:17]** of what you're doing. And then the the

**[15:17]** of what you're doing. And then the the the other thing that I want to emphasize

**[15:19]** the other thing that I want to emphasize

**[15:19]** the other thing that I want to emphasize is that there there's still kind of like

**[15:21]** is that there there's still kind of like

**[15:21]** is that there there's still kind of like a UX for interacting with these agents.

**[15:24]** a UX for interacting with these agents.

**[15:24]** a UX for interacting with these agents. Um so ambient does not mean fully

**[15:26]** Um so ambient does not mean fully

**[15:26]** Um so ambient does not mean fully autonomous. And this is really really

**[15:28]** autonomous. And this is really really

**[15:28]** autonomous. And this is really really important because autonomous when people

**[15:29]** important because autonomous when people

**[15:29]** important because autonomous when people hear autonomous they think the the cost

**[15:31]** hear autonomous they think the the cost

**[15:31]** hear autonomous they think the the cost of this thing doing something bad is is

**[15:33]** of this thing doing something bad is is

**[15:33]** of this thing doing something bad is is is is really high because I'm not going

**[15:35]** is is really high because I'm not going

**[15:35]** is is really high because I'm not going to be able to to oversee it. I don't

**[15:37]** to be able to to oversee it. I don't

**[15:37]** to be able to to oversee it. I don't know what's going on. How do I it could

**[15:39]** know what's going on. How do I it could

**[15:39]** know what's going on. How do I it could go out there and like run wild. And so

**[15:40]** go out there and like run wild. And so

**[15:40]** go out there and like run wild. And so ambient does not mean fully autonomous.

**[15:43]** ambient does not mean fully autonomous.

**[15:43]** ambient does not mean fully autonomous. And so there are a lot of different kind

**[15:44]** And so there are a lot of different kind

**[15:44]** And so there are a lot of different kind of like human in the loop interaction

**[15:46]** of like human in the loop interaction

**[15:46]** of like human in the loop interaction patterns that you can bring into these

**[15:48]** patterns that you can bring into these

**[15:48]** patterns that you can bring into these kind of like background these ambient

**[15:50]** kind of like background these ambient

**[15:50]** kind of like background these ambient agents. Um there can be like an approve

**[15:52]** agents. Um there can be like an approve

**[15:52]** agents. Um there can be like an approve reject pattern where for certain tools

**[15:54]** reject pattern where for certain tools

**[15:54]** reject pattern where for certain tools you want to explicitly say yes it's okay

**[15:56]** you want to explicitly say yes it's okay

**[15:56]** you want to explicitly say yes it's okay to call this tool. You might want to

**[15:57]** to call this tool. You might want to

**[15:57]** to call this tool. You might want to edit the tool that it's calling. So if

**[15:59]** edit the tool that it's calling. So if

**[15:59]** edit the tool that it's calling. So if it messes up a tool call you can


### [16:00 - 17:00]

**[16:00]** it messes up a tool call you can

**[16:00]** it messes up a tool call you can actually just correct it in the UI. You

**[16:03]** actually just correct it in the UI. You

**[16:03]** actually just correct it in the UI. You might want to give it the ability to

**[16:04]** might want to give it the ability to

**[16:04]** might want to give it the ability to kind of like ask questions so that you

**[16:06]** kind of like ask questions so that you

**[16:06]** kind of like ask questions so that you can answer them. You can provide more

**[16:07]** can answer them. You can provide more

**[16:07]** can answer them. You can provide more info if it gets stuck kind of like

**[16:09]** info if it gets stuck kind of like

**[16:09]** info if it gets stuck kind of like halfway through. And then time travel is

**[16:11]** halfway through. And then time travel is

**[16:11]** halfway through. And then time travel is something that we call uh human on the

**[16:13]** something that we call uh human on the

**[16:13]** something that we call uh human on the loop as well. So this is after the

**[16:14]** loop as well. So this is after the

**[16:14]** loop as well. So this is after the agents run. if it messed up on step like

**[16:16]** agents run. if it messed up on step like

**[16:16]** agents run. if it messed up on step like 10 out of 100, you can reverse back to

**[16:19]** 10 out of 100, you can reverse back to

**[16:19]** 10 out of 100, you can reverse back to step 10 and say, "Hey, no, like resume

**[16:21]** step 10 and say, "Hey, no, like resume

**[16:21]** step 10 and say, "Hey, no, like resume from here, but do this other thing like

**[16:22]** from here, but do this other thing like

**[16:22]** from here, but do this other thing like slightly differently." And so, so human

**[16:25]** slightly differently." And so, so human

**[16:25]** slightly differently." And so, so human loop, we think is is super super

**[16:26]** loop, we think is is super super

**[16:26]** loop, we think is is super super important. The the other thing that I

**[16:28]** important. The the other thing that I

**[16:28]** important. The the other thing that I want to call out just briefly is I think

**[16:30]** want to call out just briefly is I think

**[16:30]** want to call out just briefly is I think there's this there's this uh

**[16:32]** there's this there's this uh

**[16:32]** there's this there's this uh intermediary state where where we're

**[16:34]** intermediary state where where we're

**[16:34]** intermediary state where where we're starting to be right now. I like I

**[16:36]** starting to be right now. I like I

**[16:36]** starting to be right now. I like I wouldn't call deep research or uh or

**[16:38]** wouldn't call deep research or uh or

**[16:38]** wouldn't call deep research or uh or claude code or any of these coding

**[16:40]** claude code or any of these coding

**[16:40]** claude code or any of these coding agents ambient agents because they're

**[16:41]** agents ambient agents because they're

**[16:42]** agents ambient agents because they're still triggered by a human and but I

**[16:43]** still triggered by a human and but I

**[16:43]** still triggered by a human and but I think these are good examples of kind of

**[16:45]** think these are good examples of kind of

**[16:45]** think these are good examples of kind of like sync to async agents. Um and so so

**[16:48]** like sync to async agents. Um and so so

**[16:48]** like sync to async agents. Um and so so factory uh is a coding agent. They they

**[16:51]** factory uh is a coding agent. They they

**[16:51]** factory uh is a coding agent. They they use a term kind of like async coding

**[16:52]** use a term kind of like async coding

**[16:52]** use a term kind of like async coding agents and I I really like that. Um but

**[16:54]** agents and I I really like that. Um but

**[16:54]** agents and I I really like that. Um but but I think this this kind of like sync

**[16:56]** but I think this this kind of like sync

**[16:56]** but I think this this kind of like sync to async agents is a natural progression

**[16:58]** to async agents is a natural progression

**[16:58]** to async agents is a natural progression if you think about it like right now to


### [17:00 - 18:00]

**[17:00]** if you think about it like right now to

**[17:00]** if you think about it like right now to start or you know a year ago everything

**[17:02]** start or you know a year ago everything

**[17:02]** start or you know a year ago everything was a sync agent. We were chatting with

**[17:03]** was a sync agent. We were chatting with

**[17:04]** was a sync agent. We were chatting with it. is very much in the moment. The

**[17:05]** it. is very much in the moment. The

**[17:05]** it. is very much in the moment. The future is probably these autonomous

**[17:06]** future is probably these autonomous

**[17:06]** future is probably these autonomous agents working in the background and

**[17:08]** agents working in the background and

**[17:08]** agents working in the background and still pinging us when they need help.

**[17:09]** still pinging us when they need help.

**[17:09]** still pinging us when they need help. But there's this intermediate state

**[17:10]** But there's this intermediate state

**[17:10]** But there's this intermediate state where where the human kicks it off, uses

**[17:13]** where where the human kicks it off, uses

**[17:13]** where where the human kicks it off, uses that kind of like human in the loop at

**[17:14]** that kind of like human in the loop at

**[17:14]** that kind of like human in the loop at the start to calibrate on what you want

**[17:15]** the start to calibrate on what you want

**[17:15]** the start to calibrate on what you want it to do. And so I I think that that

**[17:18]** it to do. And so I I think that that

**[17:18]** it to do. And so I I think that that table I showed of like chat and and

**[17:20]** table I showed of like chat and and

**[17:20]** table I showed of like chat and and ambient is actually probably missing a

**[17:22]** ambient is actually probably missing a

**[17:22]** ambient is actually probably missing a column in the middle that's like these

**[17:23]** column in the middle that's like these

**[17:23]** column in the middle that's like these sync to async agents. Um, anyways, an

**[17:26]** sync to async agents. Um, anyways, an

**[17:26]** sync to async agents. Um, anyways, an example of some of the UX's that we

**[17:28]** example of some of the UX's that we

**[17:28]** example of some of the UX's that we think can be interesting for these

**[17:29]** think can be interesting for these

**[17:29]** think can be interesting for these ambient agents are are basically what we

**[17:31]** ambient agents are are basically what we

**[17:31]** ambient agents are are basically what we call agent inbox, which is where you

**[17:32]** call agent inbox, which is where you

**[17:32]** call agent inbox, which is where you surface all the actions that the agent

**[17:34]** surface all the actions that the agent

**[17:34]** surface all the actions that the agent wants to take that need your approval

**[17:35]** wants to take that need your approval

**[17:35]** wants to take that need your approval and then you can go in and approve,

**[17:37]** and then you can go in and approve,

**[17:37]** and then you can go in and approve, reject, leave feedback, things like

**[17:38]** reject, leave feedback, things like

**[17:38]** reject, leave feedback, things like that. Just kind of tie this together and

**[17:41]** that. Just kind of tie this together and

**[17:41]** that. Just kind of tie this together and make uh really concrete what I mean by

**[17:43]** make uh really concrete what I mean by

**[17:43]** make uh really concrete what I mean by ambient agents. Uh, email I think is a

**[17:45]** ambient agents. Uh, email I think is a

**[17:45]** ambient agents. Uh, email I think is a really natural place for ambient agents.

**[17:47]** really natural place for ambient agents.

**[17:47]** really natural place for ambient agents. These these agents can listen to

**[17:48]** These these agents can listen to

**[17:48]** These these agents can listen to incoming emails. Those are events. They

**[17:50]** incoming emails. Those are events. They

**[17:50]** incoming emails. Those are events. They can run on however many emails come in.

**[17:53]** can run on however many emails come in.

**[17:53]** can run on however many emails come in. So that's, you know, in theory

**[17:54]** So that's, you know, in theory

**[17:54]** So that's, you know, in theory unlimited, but you still probably want

**[17:57]** unlimited, but you still probably want

**[17:57]** unlimited, but you still probably want in agent or you still probably want the

**[17:59]** in agent or you still probably want the

**[17:59]** in agent or you still probably want the human, the user to approve any emails


### [18:00 - 19:00]

**[18:01]** human, the user to approve any emails

**[18:01]** human, the user to approve any emails that go out or any calendar events that

**[18:03]** that go out or any calendar events that

**[18:03]** that go out or any calendar events that get sent. Um, depending on your level of

**[18:05]** get sent. Um, depending on your level of

**[18:05]** get sent. Um, depending on your level of comfort. And so, uh, this is a concrete

**[18:07]** comfort. And so, uh, this is a concrete

**[18:07]** comfort. And so, uh, this is a concrete thing. Um, uh, I actually built one, uh,

**[18:10]** thing. Um, uh, I actually built one, uh,

**[18:10]** thing. Um, uh, I actually built one, uh, that I have myself. Uh, we've used it to

**[18:12]** that I have myself. Uh, we've used it to

**[18:12]** that I have myself. Uh, we've used it to kind of like test out a lot of these

**[18:13]** kind of like test out a lot of these

**[18:13]** kind of like test out a lot of these things. Um, if people want to try it

**[18:15]** things. Um, if people want to try it

**[18:15]** things. Um, if people want to try it out, there is a QR code that you can

**[18:16]** out, there is a QR code that you can

**[18:16]** out, there is a QR code that you can scan and get the GitHub repo. It's all

**[18:18]** scan and get the GitHub repo. It's all

**[18:18]** scan and get the GitHub repo. It's all open source. Um, and I think this is uh

**[18:21]** open source. Um, and I think this is uh

**[18:21]** open source. Um, and I think this is uh it's not the only example of ambient

**[18:23]** it's not the only example of ambient

**[18:23]** it's not the only example of ambient agents. Um, but it's one that that I've

**[18:25]** agents. Um, but it's one that that I've

**[18:25]** agents. Um, but it's one that that I've built myself and so we we talk a lot

**[18:27]** built myself and so we we talk a lot

**[18:27]** built myself and so we we talk a lot about internally. Um, that's all I have.

**[18:30]** about internally. Um, that's all I have.

**[18:30]** about internally. Um, that's all I have. Uh, I'm not sure if there's time for

**[18:32]** Uh, I'm not sure if there's time for

**[18:32]** Uh, I'm not sure if there's time for questions or not. One or two questions

**[18:34]** questions or not. One or two questions

**[18:34]** questions or not. One or two questions if if people have them. Um, yeah.

**[18:48]** So my question is uh although

**[18:48]** So my question is uh although everybody's talking about agents uh but

**[18:51]** everybody's talking about agents uh but

**[18:51]** everybody's talking about agents uh but only codegenerating agents are the one

**[18:53]** only codegenerating agents are the one

**[18:53]** only codegenerating agents are the one who are getting funding is it because uh

**[18:55]** who are getting funding is it because uh

**[18:55]** who are getting funding is it because uh you can measure what you have done and

**[18:57]** you can measure what you have done and

**[18:57]** you can measure what you have done and you can reverse what you have done but

**[18:59]** you can reverse what you have done but

**[18:59]** you can reverse what you have done but for all other agents you can do lot of


### [19:00 - 20:00]

**[19:01]** for all other agents you can do lot of

**[19:01]** for all other agents you can do lot of stuff but you cannot measure what you

**[19:03]** stuff but you cannot measure what you

**[19:03]** stuff but you cannot measure what you have done you cannot reverse what you

**[19:05]** have done you cannot reverse what you

**[19:05]** have done you cannot reverse what you have done. Yeah, I I I I think those are

**[19:07]** have done. Yeah, I I I I think those are

**[19:08]** have done. Yeah, I I I I think those are Yeah, I think there's a variety of

**[19:09]** Yeah, I think there's a variety of

**[19:09]** Yeah, I think there's a variety of reasons. I think those two measure and

**[19:11]** reasons. I think those two measure and

**[19:11]** reasons. I think those two measure and and well, okay, so the measure thing I

**[19:14]** and well, okay, so the measure thing I

**[19:14]** and well, okay, so the measure thing I think probably more so like you can a

**[19:16]** think probably more so like you can a

**[19:16]** think probably more so like you can a lot of the large model labs train on a

**[19:18]** lot of the large model labs train on a

**[19:18]** lot of the large model labs train on a lot of coding data because you can test

**[19:20]** lot of coding data because you can test

**[19:20]** lot of coding data because you can test whether it's correct or not. You can run

**[19:21]** whether it's correct or not. You can run

**[19:21]** whether it's correct or not. You can run it, see if it compiles. Same with math

**[19:23]** it, see if it compiles. Same with math

**[19:23]** it, see if it compiles. Same with math data. Math is very it's verifiable,

**[19:25]** data. Math is very it's verifiable,

**[19:25]** data. Math is very it's verifiable, right? So math and code are two examples

**[19:27]** right? So math and code are two examples

**[19:27]** right? So math and code are two examples of verifiable domains. Essay writing is

**[19:29]** of verifiable domains. Essay writing is

**[19:29]** of verifiable domains. Essay writing is less verifiable. What does it mean for

**[19:30]** less verifiable. What does it mean for

**[19:30]** less verifiable. What does it mean for an essay to be correct? That's far more

**[19:32]** an essay to be correct? That's far more

**[19:32]** an essay to be correct? That's far more ambiguous. And so because of these

**[19:34]** ambiguous. And so because of these

**[19:34]** ambiguous. And so because of these verifiable things, uh you're able to

**[19:36]** verifiable things, uh you're able to

**[19:36]** verifiable things, uh you're able to bootstrap a lot of training data. And so

**[19:37]** bootstrap a lot of training data. And so

**[19:37]** bootstrap a lot of training data. And so there's a lot of training data in the

**[19:39]** there's a lot of training data in the

**[19:39]** there's a lot of training data in the models already about code. And so the

**[19:40]** models already about code. And so the

**[19:40]** models already about code. And so the models are better at that. That makes

**[19:42]** models are better at that. That makes

**[19:42]** models are better at that. That makes the agents that use those models better

**[19:43]** the agents that use those models better

**[19:43]** the agents that use those models better at that. Then the second part, uh I I do

**[19:46]** at that. Then the second part, uh I I do

**[19:46]** at that. Then the second part, uh I I do think code lends itself naturally to

**[19:48]** think code lends itself naturally to

**[19:48]** think code lends itself naturally to kind of like this commit and this draft

**[19:50]** kind of like this commit and this draft

**[19:50]** kind of like this commit and this draft and this preview thing. I think that's

**[19:52]** and this preview thing. I think that's

**[19:52]** and this preview thing. I think that's more generalizable. So like legal is a

**[19:54]** more generalizable. So like legal is a

**[19:54]** more generalizable. So like legal is a great example. Legal, you can you can

**[19:55]** great example. Legal, you can you can

**[19:55]** great example. Legal, you can you can have first drafts of things. That's very

**[19:57]** have first drafts of things. That's very

**[19:57]** have first drafts of things. That's very common. Same with essay writing. I think

**[19:59]** common. Same with essay writing. I think

**[19:59]** common. Same with essay writing. I think the concept of like a first draft is


### [20:00 - 21:00]

**[20:01]** the concept of like a first draft is

**[20:01]** the concept of like a first draft is actually a really good UX to aim for. It

**[20:03]** actually a really good UX to aim for. It

**[20:03]** actually a really good UX to aim for. It lets you do far more. It also puts the

**[20:05]** lets you do far more. It also puts the

**[20:05]** lets you do far more. It also puts the human in the loop and so you kind of get

**[20:07]** human in the loop and so you kind of get

**[20:07]** human in the loop and so you kind of get you get this dual kind of like like if

**[20:09]** you get this dual kind of like like if

**[20:09]** you get this dual kind of like like if you put the human in the loop at every

**[20:10]** you put the human in the loop at every

**[20:10]** you put the human in the loop at every step like that doesn't provide any

**[20:12]** step like that doesn't provide any

**[20:12]** step like that doesn't provide any value. Like each step is so small. So

**[20:14]** value. Like each step is so small. So

**[20:14]** value. Like each step is so small. So the key is like finding these UX

**[20:15]** the key is like finding these UX

**[20:15]** the key is like finding these UX patterns where the agent does a ton of

**[20:18]** patterns where the agent does a ton of

**[20:18]** patterns where the agent does a ton of work but the human still in the loop at

**[20:20]** work but the human still in the loop at

**[20:20]** work but the human still in the loop at key points and first drafts I think are

**[20:22]** key points and first drafts I think are

**[20:22]** key points and first drafts I think are a great kind of like mental model for

**[20:23]** a great kind of like mental model for

**[20:23]** a great kind of like mental model for that. And so anything where there's like

**[20:25]** that. And so anything where there's like

**[20:25]** that. And so anything where there's like first drafts, legal, writing, code, I

**[20:28]** first drafts, legal, writing, code, I

**[20:28]** first drafts, legal, writing, code, I think I think that's a little bit more

**[20:29]** think I think that's a little bit more

**[20:30]** think I think that's a little bit more generalizable. The

**[20:32]** generalizable. The

**[20:32]** generalizable. The verifiable stuff that's a little bit

**[20:34]** verifiable stuff that's a little bit

**[20:34]** verifiable stuff that's a little bit tougher. Um, yeah.

**[20:42]** Yeah. Oh, no. Good. I'll talk to you

**[20:42]** Yeah. Oh, no. Good. I'll talk to you afterwards.

**[20:43]** afterwards.

**[20:43]** afterwards. Cool. Yeah, more than happy to chat

**[20:44]** Cool. Yeah, more than happy to chat

**[20:44]** Cool. Yeah, more than happy to chat after. Thank you all.


