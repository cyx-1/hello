# Building Agents (the hard parts!) - Rita Kozlov, Cloudflare

**Video URL:** https://www.youtube.com/watch?v=j_TKDweOsYE

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Hello everyone. Uh I'm Rita. I'm the VP

**[00:17]** Hello everyone. Uh I'm Rita. I'm the VP of product for um Cloudflare's developer

**[00:20]** of product for um Cloudflare's developer

**[00:20]** of product for um Cloudflare's developer platform. So workers and durable

**[00:22]** platform. So workers and durable

**[00:22]** platform. So workers and durable objects. Thank you for the shoutouts.

**[00:24]** objects. Thank you for the shoutouts.

**[00:24]** objects. Thank you for the shoutouts. Um, I always like to start by talking a

**[00:28]** Um, I always like to start by talking a

**[00:28]** Um, I always like to start by talking a little bit about um, Cloudflare's

**[00:30]** little bit about um, Cloudflare's

**[00:30]** little bit about um, Cloudflare's mission and especially our mission for

**[00:32]** mission and especially our mission for

**[00:32]** mission and especially our mission for developers. And I saw a couple hands

**[00:34]** developers. And I saw a couple hands

**[00:34]** developers. And I saw a couple hands here in terms of a number of people that

**[00:37]** here in terms of a number of people that

**[00:37]** here in terms of a number of people that use Cloudflare workers before. Um, but

**[00:39]** use Cloudflare workers before. Um, but

**[00:39]** use Cloudflare workers before. Um, but actually if you're sitting in this room,

**[00:42]** actually if you're sitting in this room,

**[00:42]** actually if you're sitting in this room, whether you've signed up for Cloudflare

**[00:44]** whether you've signed up for Cloudflare

**[00:44]** whether you've signed up for Cloudflare directly or not, um, you've 100% used

**[00:47]** directly or not, um, you've 100% used

**[00:47]** directly or not, um, you've 100% used Cloudflare before because about 20% of

**[00:50]** Cloudflare before because about 20% of

**[00:50]** Cloudflare before because about 20% of internet traffic flows through

**[00:52]** internet traffic flows through

**[00:52]** internet traffic flows through Cloudflare. Um, so if you've ordered an

**[00:55]** Cloudflare. Um, so if you've ordered an

**[00:55]** Cloudflare. Um, so if you've ordered an Uber recently, um, or, uh, or maybe even

**[00:58]** Uber recently, um, or, uh, or maybe even

**[00:58]** Uber recently, um, or, uh, or maybe even ordered some food, um, you've absolutely


### [01:00 - 02:00]

**[01:00]** ordered some food, um, you've absolutely

**[01:00]** ordered some food, um, you've absolutely used Cloudflare. Um, but aside from

**[01:02]** used Cloudflare. Um, but aside from

**[01:02]** used Cloudflare. Um, but aside from Cloudflare's CDN, DNS, DOS services, we

**[01:06]** Cloudflare's CDN, DNS, DOS services, we

**[01:06]** Cloudflare's CDN, DNS, DOS services, we do also offer, um, services to

**[01:08]** do also offer, um, services to

**[01:08]** do also offer, um, services to developers, including functions that

**[01:09]** developers, including functions that

**[01:10]** developers, including functions that you're able to run storage, compute, AI,

**[01:13]** you're able to run storage, compute, AI,

**[01:13]** you're able to run storage, compute, AI, inference, um, spanning many, many

**[01:14]** inference, um, spanning many, many

**[01:14]** inference, um, spanning many, many things. And our uh our vision for

**[01:17]** things. And our uh our vision for

**[01:17]** things. And our uh our vision for developers is to make it as easy as

**[01:19]** developers is to make it as easy as

**[01:19]** developers is to make it as easy as possible for someone to bring their idea

**[01:22]** possible for someone to bring their idea

**[01:22]** possible for someone to bring their idea to life from the moment that they write

**[01:24]** to life from the moment that they write

**[01:24]** to life from the moment that they write their first line of code to deploying it

**[01:27]** their first line of code to deploying it

**[01:27]** their first line of code to deploying it to production to making it live for the

**[01:30]** to production to making it live for the

**[01:30]** to production to making it live for the first user to the millions that come

**[01:33]** first user to the millions that come

**[01:33]** first user to the millions that come after that. Um so that that's what I do.

**[01:35]** after that. Um so that that's what I do.

**[01:35]** after that. Um so that that's what I do. It makes my job really exciting to wake

**[01:37]** It makes my job really exciting to wake

**[01:37]** It makes my job really exciting to wake up in the morning and see what

**[01:38]** up in the morning and see what

**[01:38]** up in the morning and see what developers are going to build.

**[01:41]** developers are going to build.

**[01:41]** developers are going to build. Um, now if you're in this room, I I

**[01:44]** Um, now if you're in this room, I I

**[01:44]** Um, now if you're in this room, I I don't need to tell you that AI is as big

**[01:47]** don't need to tell you that AI is as big

**[01:48]** don't need to tell you that AI is as big uh technological paradigm shift as um as

**[01:52]** uh technological paradigm shift as um as

**[01:52]** uh technological paradigm shift as um as cloud, mobile or social before it. Um, I

**[01:55]** cloud, mobile or social before it. Um, I

**[01:55]** cloud, mobile or social before it. Um, I think everyone here is already convinced

**[01:57]** think everyone here is already convinced

**[01:57]** think everyone here is already convinced of that. But it is interesting to see

**[01:59]** of that. But it is interesting to see

**[01:59]** of that. But it is interesting to see just how quickly things are moving


### [02:00 - 03:00]

**[02:01]** just how quickly things are moving

**[02:01]** just how quickly things are moving because I think that it's a good

**[02:02]** because I think that it's a good

**[02:02]** because I think that it's a good reflection of how quickly things are

**[02:05]** reflection of how quickly things are

**[02:05]** reflection of how quickly things are about to move next. So, um, I realized

**[02:07]** about to move next. So, um, I realized

**[02:07]** about to move next. So, um, I realized that I gave a talk about a year ago, um,

**[02:10]** that I gave a talk about a year ago, um,

**[02:10]** that I gave a talk about a year ago, um, where I was pulling up some some stats

**[02:12]** where I was pulling up some some stats

**[02:12]** where I was pulling up some some stats and looking at where we were at. And so,

**[02:15]** and looking at where we were at. And so,

**[02:15]** and looking at where we were at. And so, a year ago, um, about 44% of developers

**[02:18]** a year ago, um, about 44% of developers

**[02:18]** a year ago, um, about 44% of developers were using AI as a part of their

**[02:20]** were using AI as a part of their

**[02:20]** were using AI as a part of their day-to-day, um, to to help them write

**[02:23]** day-to-day, um, to to help them write

**[02:23]** day-to-day, um, to to help them write code. Uh, and, um, Gartner was

**[02:26]** code. Uh, and, um, Gartner was

**[02:26]** code. Uh, and, um, Gartner was predicting that about, uh, by by 2030

**[02:29]** predicting that about, uh, by by 2030

**[02:29]** predicting that about, uh, by by 2030 about 50% of knowledge workers would be

**[02:32]** about 50% of knowledge workers would be

**[02:32]** about 50% of knowledge workers would be using AI to augment their work. Um and

**[02:35]** using AI to augment their work. Um and

**[02:35]** using AI to augment their work. Um and the these numbers seem ex really really

**[02:38]** the these numbers seem ex really really

**[02:38]** the these numbers seem ex really really low now, right? Like um today um over

**[02:41]** low now, right? Like um today um over

**[02:41]** low now, right? Like um today um over 75% of knowledge workers use AI to

**[02:44]** 75% of knowledge workers use AI to

**[02:44]** 75% of knowledge workers use AI to augment their work. Um so this is

**[02:46]** augment their work. Um so this is

**[02:46]** augment their work. Um so this is already surpassing the 2030 estimates

**[02:49]** already surpassing the 2030 estimates

**[02:49]** already surpassing the 2030 estimates that were given and more than 76% of

**[02:51]** that were given and more than 76% of

**[02:51]** that were given and more than 76% of developers use AI as a part of their

**[02:53]** developers use AI as a part of their

**[02:53]** developers use AI as a part of their development process. And um I I I think

**[02:57]** development process. And um I I I think

**[02:57]** development process. And um I I I think that honestly from the time that this

**[02:59]** that honestly from the time that this

**[02:59]** that honestly from the time that this report was pulled to now that number has


### [03:00 - 04:00]

**[03:01]** report was pulled to now that number has

**[03:01]** report was pulled to now that number has grown even more.

**[03:03]** grown even more.

**[03:04]** grown even more. Um the other interesting thing was that

**[03:06]** Um the other interesting thing was that

**[03:06]** Um the other interesting thing was that about a year ago when we were talking

**[03:08]** about a year ago when we were talking

**[03:08]** about a year ago when we were talking about um when we were talking about

**[03:10]** about um when we were talking about

**[03:10]** about um when we were talking about workloads we were primarily talking

**[03:12]** workloads we were primarily talking

**[03:12]** workloads we were primarily talking about workloads in AI that involve

**[03:14]** about workloads in AI that involve

**[03:14]** about workloads in AI that involve training um and we predicted then that

**[03:17]** training um and we predicted then that

**[03:17]** training um and we predicted then that workloads were going to shift towards

**[03:19]** workloads were going to shift towards

**[03:19]** workloads were going to shift towards inference and again we've been seeing

**[03:21]** inference and again we've been seeing

**[03:22]** inference and again we've been seeing that unfold so we saw that with open

**[03:24]** that unfold so we saw that with open

**[03:24]** that unfold so we saw that with open AI's 01 model which is shifting more and

**[03:28]** AI's 01 model which is shifting more and

**[03:28]** AI's 01 model which is shifting more and more from training to post-training and

**[03:31]** more from training to post-training and

**[03:31]** more from training to post-training and inference. We saw a similar thing

**[03:33]** inference. We saw a similar thing

**[03:33]** inference. We saw a similar thing actually with DeepSeek who optimize

**[03:35]** actually with DeepSeek who optimize

**[03:35]** actually with DeepSeek who optimize training so much that more and more

**[03:37]** training so much that more and more

**[03:37]** training so much that more and more energy is spent on the inference part of

**[03:39]** energy is spent on the inference part of

**[03:39]** energy is spent on the inference part of it. But let's talk about what's next. So

**[03:43]** it. But let's talk about what's next. So

**[03:43]** it. But let's talk about what's next. So um after training and inference comes I

**[03:46]** um after training and inference comes I

**[03:46]** um after training and inference comes I think actual automation and uh I know

**[03:48]** think actual automation and uh I know

**[03:48]** think actual automation and uh I know there's been a lot of talk about agents

**[03:50]** there's been a lot of talk about agents

**[03:50]** there's been a lot of talk about agents the past couple days but this is the

**[03:52]** the past couple days but this is the

**[03:52]** the past couple days but this is the reason that this is so exciting is that

**[03:54]** reason that this is so exciting is that

**[03:54]** reason that this is so exciting is that we have the opportunity to not just uh

**[03:57]** we have the opportunity to not just uh

**[03:57]** we have the opportunity to not just uh to not just augment people's work right


### [04:00 - 05:00]

**[04:00]** to not just augment people's work right

**[04:00]** to not just augment people's work right you've been able for some time now to go

**[04:02]** you've been able for some time now to go

**[04:02]** you've been able for some time now to go somewhere like Chad GPT and ask it like

**[04:04]** somewhere like Chad GPT and ask it like

**[04:04]** somewhere like Chad GPT and ask it like hey help me draft up an email but what's

**[04:07]** hey help me draft up an email but what's

**[04:07]** hey help me draft up an email but what's really really powerful is to be able to

**[04:09]** really really powerful is to be able to

**[04:09]** really really powerful is to be able to go and say hey I have a campaign I want

**[04:13]** go and say hey I have a campaign I want

**[04:13]** go and say hey I have a campaign I want to run. Grab me a full list of the

**[04:15]** to run. Grab me a full list of the

**[04:15]** to run. Grab me a full list of the customers that I talked to this week at

**[04:17]** customers that I talked to this week at

**[04:17]** customers that I talked to this week at the conference. Uh then draft me up the

**[04:20]** the conference. Uh then draft me up the

**[04:20]** the conference. Uh then draft me up the email. Then actually I do want to review

**[04:22]** email. Then actually I do want to review

**[04:22]** email. Then actually I do want to review it before it goes to a customer. So do

**[04:24]** it before it goes to a customer. So do

**[04:24]** it before it goes to a customer. So do send it to me for approval. And then

**[04:26]** send it to me for approval. And then

**[04:26]** send it to me for approval. And then ping me when the customer responds. Um

**[04:29]** ping me when the customer responds. Um

**[04:29]** ping me when the customer responds. Um and so these are exactly the types of

**[04:31]** and so these are exactly the types of

**[04:31]** and so these are exactly the types of agentic workflows that I think we're

**[04:32]** agentic workflows that I think we're

**[04:32]** agentic workflows that I think we're going to see more and more that are

**[04:34]** going to see more and more that are

**[04:34]** going to see more and more that are really going to unlock that next level

**[04:36]** really going to unlock that next level

**[04:36]** really going to unlock that next level of productivity.

**[04:38]** of productivity.

**[04:38]** of productivity. And we're already starting to see these

**[04:40]** And we're already starting to see these

**[04:40]** And we're already starting to see these agents out in the wild and really

**[04:42]** agents out in the wild and really

**[04:42]** agents out in the wild and really meaningfully impacting businesses. Um so

**[04:45]** meaningfully impacting businesses. Um so

**[04:45]** meaningfully impacting businesses. Um so some businesses are seeing uh 20%

**[04:48]** some businesses are seeing uh 20%

**[04:48]** some businesses are seeing uh 20% revenue increases already as a part of

**[04:51]** revenue increases already as a part of

**[04:51]** revenue increases already as a part of starting to adopt agents as a part of

**[04:53]** starting to adopt agents as a part of

**[04:53]** starting to adopt agents as a part of sales automation. Um some businesses are

**[04:56]** sales automation. Um some businesses are

**[04:56]** sales automation. Um some businesses are seeing 90% faster response times to

**[04:59]** seeing 90% faster response times to

**[04:59]** seeing 90% faster response times to support when using AI agents. Um and in


### [05:00 - 06:00]

**[05:01]** support when using AI agents. Um and in

**[05:01]** support when using AI agents. Um and in general uh people are seeing about 50 to

**[05:03]** general uh people are seeing about 50 to

**[05:03]** general uh people are seeing about 50 to 75% time savings when using agents. So

**[05:06]** 75% time savings when using agents. So

**[05:06]** 75% time savings when using agents. So agents are going to be even more

**[05:09]** agents are going to be even more

**[05:09]** agents are going to be even more meaningful but are already reshaping the

**[05:11]** meaningful but are already reshaping the

**[05:11]** meaningful but are already reshaping the way that we work.

**[05:14]** way that we work.

**[05:14]** way that we work. Um, okay. But, uh, you want to build an

**[05:16]** Um, okay. But, uh, you want to build an

**[05:16]** Um, okay. But, uh, you want to build an agent. Where do you start? What what all

**[05:19]** agent. Where do you start? What what all

**[05:19]** agent. Where do you start? What what all goes into building an an agent.

**[05:22]** goes into building an an agent.

**[05:22]** goes into building an an agent. The way that I like to think about

**[05:24]** The way that I like to think about

**[05:24]** The way that I like to think about agents really comes down to these four

**[05:26]** agents really comes down to these four

**[05:26]** agents really comes down to these four components. So, first you have the

**[05:28]** components. So, first you have the

**[05:28]** components. So, first you have the client. You have the interface that the

**[05:30]** client. You have the interface that the

**[05:30]** client. You have the interface that the agent is going to be interacted through

**[05:33]** agent is going to be interacted through

**[05:33]** agent is going to be interacted through with a human, right? Um then you have

**[05:35]** with a human, right? Um then you have

**[05:35]** with a human, right? Um then you have the AI the reasoning piece the the

**[05:38]** the AI the reasoning piece the the

**[05:38]** the AI the reasoning piece the the thinking part that's going to come up

**[05:39]** thinking part that's going to come up

**[05:40]** thinking part that's going to come up with the logic of what are we about to

**[05:42]** with the logic of what are we about to

**[05:42]** with the logic of what are we about to execute what are we going to do next now

**[05:45]** execute what are we going to do next now

**[05:45]** execute what are we going to do next now the thinking part needs now it's

**[05:47]** the thinking part needs now it's

**[05:47]** the thinking part needs now it's executive branch right it needs a way to

**[05:50]** executive branch right it needs a way to

**[05:50]** executive branch right it needs a way to go and execute on the actions that it

**[05:52]** go and execute on the actions that it

**[05:52]** go and execute on the actions that it decided that it was going to take and

**[05:54]** decided that it was going to take and

**[05:54]** decided that it was going to take and then so that's the workflows and then

**[05:56]** then so that's the workflows and then

**[05:56]** then so that's the workflows and then workflows also need access to tools so

**[05:59]** workflows also need access to tools so

**[05:59]** workflows also need access to tools so it's not just enough to be like okay I'm


### [06:00 - 07:00]

**[06:01]** it's not just enough to be like okay I'm

**[06:01]** it's not just enough to be like okay I'm going to go and do this they need access

**[06:03]** going to go and do this they need access

**[06:03]** going to go and do this they need access to the tools to actually take the

**[06:05]** to the tools to actually take the

**[06:05]** to the tools to actually take the actions.

**[06:06]** actions.

**[06:06]** actions. So, let's run through a quick example of

**[06:09]** So, let's run through a quick example of

**[06:09]** So, let's run through a quick example of what would it look like that CRM agent

**[06:11]** what would it look like that CRM agent

**[06:11]** what would it look like that CRM agent that I was just showing if I were to go

**[06:13]** that I was just showing if I were to go

**[06:13]** that I was just showing if I were to go and build something that helps me

**[06:15]** and build something that helps me

**[06:15]** and build something that helps me contact people that I talk to. What

**[06:17]** contact people that I talk to. What

**[06:17]** contact people that I talk to. What would that look like? So, the first part

**[06:19]** would that look like? So, the first part

**[06:19]** would that look like? So, the first part is if I wanted to have something that

**[06:21]** is if I wanted to have something that

**[06:21]** is if I wanted to have something that works over voice where I can be like,

**[06:23]** works over voice where I can be like,

**[06:23]** works over voice where I can be like, "Hey, do this for me." Um, you need

**[06:25]** "Hey, do this for me." Um, you need

**[06:25]** "Hey, do this for me." Um, you need something that connects over WebRTC. um

**[06:27]** something that connects over WebRTC. um

**[06:27]** something that connects over WebRTC. um you then need a speech to text model to

**[06:30]** you then need a speech to text model to

**[06:30]** you then need a speech to text model to translate what you said um back

**[06:33]** translate what you said um back

**[06:33]** translate what you said um back um back into text. Um alternatively,

**[06:36]** um back into text. Um alternatively,

**[06:36]** um back into text. Um alternatively, we're all familiar with chat UIs, right?

**[06:38]** we're all familiar with chat UIs, right?

**[06:38]** we're all familiar with chat UIs, right? So you need somewhere to host that. Um

**[06:41]** So you need somewhere to host that. Um

**[06:41]** So you need somewhere to host that. Um then ideally uh you're using um some

**[06:43]** then ideally uh you're using um some

**[06:43]** then ideally uh you're using um some sort of gateway to do caching and to run

**[06:46]** sort of gateway to do caching and to run

**[06:46]** sort of gateway to do caching and to run your eval to make sure that as you're

**[06:48]** your eval to make sure that as you're

**[06:48]** your eval to make sure that as you're iterating on the overall process that

**[06:50]** iterating on the overall process that

**[06:50]** iterating on the overall process that things are getting better and better.

**[06:52]** things are getting better and better.

**[06:52]** things are getting better and better. Um, and then you need to send that

**[06:54]** Um, and then you need to send that

**[06:54]** Um, and then you need to send that response to an LLM that's going to do

**[06:56]** response to an LLM that's going to do

**[06:56]** response to an LLM that's going to do the thinking part and come up with the

**[06:58]** the thinking part and come up with the

**[06:58]** the thinking part and come up with the rest of the plan.


### [07:00 - 08:00]

**[07:00]** rest of the plan.

**[07:00]** rest of the plan. From there, you need a workflow agent.

**[07:02]** From there, you need a workflow agent.

**[07:02]** From there, you need a workflow agent. Um, so that's what's going to keep track

**[07:04]** Um, so that's what's going to keep track

**[07:04]** Um, so that's what's going to keep track of what actions have been executed and

**[07:07]** of what actions have been executed and

**[07:07]** of what actions have been executed and what actions need to take place next.

**[07:10]** what actions need to take place next.

**[07:10]** what actions need to take place next. And then again, you need to connect to

**[07:12]** And then again, you need to connect to

**[07:12]** And then again, you need to connect to uh your tools. It can be a web browser,

**[07:14]** uh your tools. It can be a web browser,

**[07:14]** uh your tools. It can be a web browser, it can be an API, it can be an internal

**[07:17]** it can be an API, it can be an internal

**[07:17]** it can be an API, it can be an internal service that you need to connect to, or

**[07:19]** service that you need to connect to, or

**[07:19]** service that you need to connect to, or it can be a vector database if you need

**[07:21]** it can be a vector database if you need

**[07:21]** it can be a vector database if you need to grab additional knowledge that that

**[07:23]** to grab additional knowledge that that

**[07:23]** to grab additional knowledge that that uh that that um agent needs uh access

**[07:26]** uh that that um agent needs uh access

**[07:26]** uh that that um agent needs uh access to. Sometimes you're also going to need

**[07:29]** to. Sometimes you're also going to need

**[07:29]** to. Sometimes you're also going to need a human in the loop to verify some of

**[07:31]** a human in the loop to verify some of

**[07:31]** a human in the loop to verify some of these actions that you're taking.

**[07:38]** So, how do you build an agent? I'm

**[07:38]** So, how do you build an agent? I'm actually going to go backwards here and

**[07:40]** actually going to go backwards here and

**[07:40]** actually going to go backwards here and start with the tools part. Um, and most

**[07:43]** start with the tools part. Um, and most

**[07:44]** start with the tools part. Um, and most recently, uh, there's been a lot of talk

**[07:46]** recently, uh, there's been a lot of talk

**[07:46]** recently, uh, there's been a lot of talk about MCP. So, the the amazing thing is

**[07:49]** about MCP. So, the the amazing thing is

**[07:49]** about MCP. So, the the amazing thing is that Anthropic introduced this new

**[07:51]** that Anthropic introduced this new

**[07:51]** that Anthropic introduced this new standard back in November. And I think

**[07:54]** standard back in November. And I think

**[07:54]** standard back in November. And I think the the really interesting thing about

**[07:56]** the the really interesting thing about

**[07:56]** the the really interesting thing about it is that it really got people thinking

**[07:58]** it is that it really got people thinking

**[07:58]** it is that it really got people thinking about, okay, how do we expose uh how do


### [08:00 - 09:00]

**[08:01]** about, okay, how do we expose uh how do

**[08:01]** about, okay, how do we expose uh how do we expose APIs to LLMs in a way that

**[08:04]** we expose APIs to LLMs in a way that

**[08:04]** we expose APIs to LLMs in a way that allows us humans to talk to LLM over

**[08:07]** allows us humans to talk to LLM over

**[08:08]** allows us humans to talk to LLM over natural language? Um but but I think

**[08:11]** natural language? Um but but I think

**[08:11]** natural language? Um but but I think that the uh the real missed headlines of

**[08:13]** that the uh the real missed headlines of

**[08:13]** that the uh the real missed headlines of MCPs was actually that LLMs became

**[08:16]** MCPs was actually that LLMs became

**[08:16]** MCPs was actually that LLMs became really really good at tool calling. This

**[08:18]** really really good at tool calling. This

**[08:18]** really really good at tool calling. This this wasn't so much the case a few years

**[08:20]** this wasn't so much the case a few years

**[08:20]** this wasn't so much the case a few years ago if you try to play around with tool

**[08:23]** ago if you try to play around with tool

**[08:23]** ago if you try to play around with tool calling, but but now they are. And so we

**[08:25]** calling, but but now they are. And so we

**[08:25]** calling, but but now they are. And so we have this new standard for how you can

**[08:28]** have this new standard for how you can

**[08:28]** have this new standard for how you can actually write out your code in a way

**[08:30]** actually write out your code in a way

**[08:30]** actually write out your code in a way that's going to be um incredibly easy to

**[08:33]** that's going to be um incredibly easy to

**[08:33]** that's going to be um incredibly easy to consume by any uh by any MCP client. And

**[08:37]** consume by any uh by any MCP client. And

**[08:37]** consume by any uh by any MCP client. And so the again really cool thing about MCP

**[08:39]** so the again really cool thing about MCP

**[08:39]** so the again really cool thing about MCP is that it does respect a traditional

**[08:41]** is that it does respect a traditional

**[08:41]** is that it does respect a traditional client server architecture where you're

**[08:43]** client server architecture where you're

**[08:43]** client server architecture where you're able to have that conversation back and

**[08:45]** able to have that conversation back and

**[08:45]** able to have that conversation back and forth and importantly have more than one

**[08:47]** forth and importantly have more than one

**[08:47]** forth and importantly have more than one client that connects to the MCP server.

**[08:51]** client that connects to the MCP server.

**[08:51]** client that connects to the MCP server. Um so these are some of the core

**[08:52]** Um so these are some of the core

**[08:52]** Um so these are some of the core concepts that go into MCP. MCP servers

**[08:55]** concepts that go into MCP. MCP servers

**[08:55]** concepts that go into MCP. MCP servers generally have uh resources, prompts,

**[08:58]** generally have uh resources, prompts,

**[08:58]** generally have uh resources, prompts, tooling and sampling. Um resources can


### [09:00 - 10:00]

**[09:00]** tooling and sampling. Um resources can

**[09:00]** tooling and sampling. Um resources can be anything from file contents and

**[09:03]** be anything from file contents and

**[09:03]** be anything from file contents and database records. Um, prompts actually

**[09:05]** database records. Um, prompts actually

**[09:05]** database records. Um, prompts actually help you define how you want someone

**[09:08]** help you define how you want someone

**[09:08]** help you define how you want someone else to interact with your agent because

**[09:10]** else to interact with your agent because

**[09:10]** else to interact with your agent because you can actually prompt your agent

**[09:12]** you can actually prompt your agent

**[09:12]** you can actually prompt your agent probably better than anyone else can. If

**[09:15]** probably better than anyone else can. If

**[09:15]** probably better than anyone else can. If there are any nuances um about how your

**[09:18]** there are any nuances um about how your

**[09:18]** there are any nuances um about how your system works, you want to build that

**[09:20]** system works, you want to build that

**[09:20]** system works, you want to build that into it as much as possible. Um, then

**[09:22]** into it as much as possible. Um, then

**[09:22]** into it as much as possible. Um, then you want to give it access to the actual

**[09:24]** you want to give it access to the actual

**[09:24]** you want to give it access to the actual tooling, right? And connect those

**[09:26]** tooling, right? And connect those

**[09:26]** tooling, right? And connect those queries with the tools. Um, and then

**[09:28]** queries with the tools. Um, and then

**[09:28]** queries with the tools. Um, and then last but not least, sampling. Um, I

**[09:30]** last but not least, sampling. Um, I

**[09:30]** last but not least, sampling. Um, I actually think it I I haven't seen

**[09:31]** actually think it I I haven't seen

**[09:31]** actually think it I I haven't seen anyone using sampling in production yet

**[09:33]** anyone using sampling in production yet

**[09:33]** anyone using sampling in production yet in an MCP server was the interesting

**[09:36]** in an MCP server was the interesting

**[09:36]** in an MCP server was the interesting conclusion that I came to as I was

**[09:37]** conclusion that I came to as I was

**[09:37]** conclusion that I came to as I was preparing this talk. But but the idea is

**[09:40]** preparing this talk. But but the idea is

**[09:40]** preparing this talk. But but the idea is to actually allow you to kind of use

**[09:42]** to actually allow you to kind of use

**[09:42]** to actually allow you to kind of use shorthand with your uh with your LLM and

**[09:44]** shorthand with your uh with your LLM and

**[09:44]** shorthand with your uh with your LLM and allow it to um kind of complete some of

**[09:47]** allow it to um kind of complete some of

**[09:47]** allow it to um kind of complete some of the thinking behind it.

**[09:50]** the thinking behind it.

**[09:50]** the thinking behind it. Um so but but building MCP does come

**[09:53]** Um so but but building MCP does come

**[09:53]** Um so but but building MCP does come with some tricky parts and I think the

**[09:54]** with some tricky parts and I think the

**[09:54]** with some tricky parts and I think the trickiest parts of that is first of all

**[09:56]** trickiest parts of that is first of all

**[09:56]** trickiest parts of that is first of all the the transport protocol um over SSC

**[09:59]** the the transport protocol um over SSC

**[09:59]** the the transport protocol um over SSC and websockets the ooth part and the


### [10:00 - 11:00]

**[10:02]** and websockets the ooth part and the

**[10:02]** and websockets the ooth part and the memory part. Um but I'm going to share a

**[10:06]** memory part. Um but I'm going to share a

**[10:06]** memory part. Um but I'm going to share a cheat code with everyone here. Um so um

**[10:09]** cheat code with everyone here. Um so um

**[10:09]** cheat code with everyone here. Um so um get ready. I'm gonna like flash it real

**[10:11]** get ready. I'm gonna like flash it real

**[10:11]** get ready. I'm gonna like flash it real quick. Oh, you missed it.

**[10:14]** quick. Oh, you missed it.

**[10:14]** quick. Oh, you missed it. Um uh no I'm just kidding. Uh so

**[10:17]** Um uh no I'm just kidding. Uh so

**[10:17]** Um uh no I'm just kidding. Uh so Cloudflare has uh Clafler has an SDK

**[10:20]** Cloudflare has uh Clafler has an SDK

**[10:20]** Cloudflare has uh Clafler has an SDK called agents that you can install that

**[10:22]** called agents that you can install that

**[10:22]** called agents that you can install that will actually give you a lot of this

**[10:23]** will actually give you a lot of this

**[10:23]** will actually give you a lot of this functionality out of the box. Um so we

**[10:27]** functionality out of the box. Um so we

**[10:27]** functionality out of the box. Um so we released agents SDK a few months ago and

**[10:29]** released agents SDK a few months ago and

**[10:30]** released agents SDK a few months ago and yes it has the same name as the one that

**[10:31]** yes it has the same name as the one that

**[10:31]** yes it has the same name as the one that openai

**[10:33]** openai

**[10:33]** openai just released a few days ago as well. Um

**[10:35]** just released a few days ago as well. Um

**[10:36]** just released a few days ago as well. Um but and the two actually work uh play

**[10:38]** but and the two actually work uh play

**[10:38]** but and the two actually work uh play with each other really really well. But

**[10:40]** with each other really really well. But

**[10:40]** with each other really really well. But um I'll tell you a little bit about what

**[10:41]** um I'll tell you a little bit about what

**[10:41]** um I'll tell you a little bit about what it does and and you can um so you can

**[10:43]** it does and and you can um so you can

**[10:44]** it does and and you can um so you can use uh agents SDK first of all to run

**[10:47]** use uh agents SDK first of all to run

**[10:47]** use uh agents SDK first of all to run MCP servers and it comes with a class

**[10:49]** MCP servers and it comes with a class

**[10:49]** MCP servers and it comes with a class builtin called MCP agents that allows

**[10:52]** builtin called MCP agents that allows

**[10:52]** builtin called MCP agents that allows you to host your remote MCP servers with

**[10:55]** you to host your remote MCP servers with

**[10:56]** you to host your remote MCP servers with OOTH with uh transport with HTTP

**[10:59]** OOTH with uh transport with HTTP

**[10:59]** OOTH with uh transport with HTTP streaming all built in. Um, so if uh if


### [11:00 - 12:00]

**[11:02]** streaming all built in. Um, so if uh if

**[11:02]** streaming all built in. Um, so if uh if you're one of those people that never

**[11:03]** you're one of those people that never

**[11:04]** you're one of those people that never wants to touch OOTH again, um this

**[11:06]** wants to touch OOTH again, um this

**[11:06]** wants to touch OOTH again, um this allows you to do that. Um the really

**[11:08]** allows you to do that. Um the really

**[11:08]** allows you to do that. Um the really cool thing is that it has state

**[11:10]** cool thing is that it has state

**[11:10]** cool thing is that it has state management built into it because

**[11:11]** management built into it because

**[11:11]** management built into it because Cloudflare has this primitive called

**[11:13]** Cloudflare has this primitive called

**[11:13]** Cloudflare has this primitive called durable objects. And so uh durable

**[11:16]** durable objects. And so uh durable

**[11:16]** durable objects. And so uh durable objects, the idea is basically it's kind

**[11:18]** objects, the idea is basically it's kind

**[11:18]** objects, the idea is basically it's kind of like a serverless function but with

**[11:20]** of like a serverless function but with

**[11:20]** of like a serverless function but with state attached directly to it. So, if

**[11:23]** state attached directly to it. So, if

**[11:23]** state attached directly to it. So, if you've ever wanted to um write some code

**[11:25]** you've ever wanted to um write some code

**[11:25]** you've ever wanted to um write some code but then save the state of it without

**[11:27]** but then save the state of it without

**[11:27]** but then save the state of it without ever having to set up a database or

**[11:30]** ever having to set up a database or

**[11:30]** ever having to set up a database or anything like that, this is a really

**[11:31]** anything like that, this is a really

**[11:31]** anything like that, this is a really really great way to do it and makes it

**[11:33]** really great way to do it and makes it

**[11:33]** really great way to do it and makes it really easy to build these MCP servers.

**[11:36]** really easy to build these MCP servers.

**[11:36]** really easy to build these MCP servers. Um, it comes with real-time websocket

**[11:38]** Um, it comes with real-time websocket

**[11:38]** Um, it comes with real-time websocket communication. So, that makes the whole

**[11:40]** communication. So, that makes the whole

**[11:40]** communication. So, that makes the whole chat interface thing really really easy.

**[11:42]** chat interface thing really really easy.

**[11:42]** chat interface thing really really easy. React integration hooks so you can build

**[11:45]** React integration hooks so you can build

**[11:45]** React integration hooks so you can build uh you can integrate it into your front

**[11:46]** uh you can integrate it into your front

**[11:46]** uh you can integrate it into your front end really easily and basic chat

**[11:49]** end really easily and basic chat

**[11:49]** end really easily and basic chat capabilities.

**[11:51]** capabilities.

**[11:51]** capabilities. So let's walk through what it would

**[11:52]** So let's walk through what it would

**[11:52]** So let's walk through what it would actually look like to deploy an MCP

**[11:55]** actually look like to deploy an MCP

**[11:55]** actually look like to deploy an MCP server on Cloudflare. Um so first I can

**[11:59]** server on Cloudflare. Um so first I can

**[11:59]** server on Cloudflare. Um so first I can define my MCP class that extends MCP


### [12:00 - 13:00]

**[12:01]** define my MCP class that extends MCP

**[12:01]** define my MCP class that extends MCP agent which I was just talking about.

**[12:04]** agent which I was just talking about.

**[12:04]** agent which I was just talking about. And this MCP server is going to be kind

**[12:07]** And this MCP server is going to be kind

**[12:07]** And this MCP server is going to be kind of like a good readads uh server that's

**[12:10]** of like a good readads uh server that's

**[12:10]** of like a good readads uh server that's going to recommend different books to

**[12:12]** going to recommend different books to

**[12:12]** going to recommend different books to us. So it we're going to set an initial

**[12:15]** us. So it we're going to set an initial

**[12:15]** us. So it we're going to set an initial state that's empty. Uh then I can add

**[12:19]** state that's empty. Uh then I can add

**[12:19]** state that's empty. Uh then I can add different I can give it a tool uh that's

**[12:22]** different I can give it a tool uh that's

**[12:22]** different I can give it a tool uh that's called add genre. So I can start to

**[12:24]** called add genre. So I can start to

**[12:24]** called add genre. So I can start to specify my preferences. I'm a big

**[12:26]** specify my preferences. I'm a big

**[12:26]** specify my preferences. I'm a big Patricia Highmith fan. So I can say you

**[12:29]** Patricia Highmith fan. So I can say you

**[12:29]** Patricia Highmith fan. So I can say you know I really like uh thrillers. And

**[12:32]** know I really like uh thrillers. And

**[12:32]** know I really like uh thrillers. And it's going to it's going to save it and

**[12:34]** it's going to it's going to save it and

**[12:34]** it's going to it's going to save it and persist it for future interactions.

**[12:37]** persist it for future interactions.

**[12:37]** persist it for future interactions. And so when I then ask it um for I I can

**[12:41]** And so when I then ask it um for I I can

**[12:42]** And so when I then ask it um for I I can then have a separate tool called get

**[12:43]** then have a separate tool called get

**[12:43]** then have a separate tool called get recommendations that's going to get book

**[12:46]** recommendations that's going to get book

**[12:46]** recommendations that's going to get book recommendations.

**[12:47]** recommendations.

**[12:47]** recommendations. And uh you can have uh so we were

**[12:50]** And uh you can have uh so we were

**[12:50]** And uh you can have uh so we were talking about MCP prompts before. You

**[12:52]** talking about MCP prompts before. You

**[12:52]** talking about MCP prompts before. You can have a personalized pro prompt for

**[12:55]** can have a personalized pro prompt for

**[12:55]** can have a personalized pro prompt for recommending books to someone who likes

**[12:57]** recommending books to someone who likes

**[12:57]** recommending books to someone who likes the genres, right? Um and has read the


### [13:00 - 14:00]

**[13:00]** the genres, right? Um and has read the

**[13:00]** the genres, right? Um and has read the books that you've previously specified

**[13:02]** books that you've previously specified

**[13:02]** books that you've previously specified that you read. And so it's a really good

**[13:04]** that you read. And so it's a really good

**[13:04]** that you read. And so it's a really good way to get these personalized

**[13:05]** way to get these personalized

**[13:05]** way to get these personalized recommendations. And every time that you

**[13:08]** recommendations. And every time that you

**[13:08]** recommendations. And every time that you interact with this tool, it's going to

**[13:10]** interact with this tool, it's going to

**[13:10]** interact with this tool, it's going to persist the memory over every single

**[13:12]** persist the memory over every single

**[13:12]** persist the memory over every single time. So the recommendation are going to

**[13:14]** time. So the recommendation are going to

**[13:14]** time. So the recommendation are going to keep getting better and better. And

**[13:16]** keep getting better and better. And

**[13:16]** keep getting better and better. And because this MCP server is standalone

**[13:19]** because this MCP server is standalone

**[13:19]** because this MCP server is standalone and can be interacted with through

**[13:20]** and can be interacted with through

**[13:20]** and can be interacted with through various uh through various clients, the

**[13:23]** various uh through various clients, the

**[13:23]** various uh through various clients, the memory is actually going to persist

**[13:25]** memory is actually going to persist

**[13:25]** memory is actually going to persist regardless of the tool that you're using

**[13:27]** regardless of the tool that you're using

**[13:27]** regardless of the tool that you're using to call into it.

**[13:29]** to call into it.

**[13:29]** to call into it. Um now, why is this great? Um it's

**[13:31]** Um now, why is this great? Um it's

**[13:32]** Um now, why is this great? Um it's amazing because traditionally you would

**[13:33]** amazing because traditionally you would

**[13:33]** amazing because traditionally you would have to separately set up a database,

**[13:35]** have to separately set up a database,

**[13:35]** have to separately set up a database, manage connections, handle scaling.

**[13:38]** manage connections, handle scaling.

**[13:38]** manage connections, handle scaling. There would be added latency in the

**[13:39]** There would be added latency in the

**[13:39]** There would be added latency in the setup. Um versus with MCP agent because

**[13:42]** setup. Um versus with MCP agent because

**[13:42]** setup. Um versus with MCP agent because the memory part is built into it. Um you

**[13:45]** the memory part is built into it. Um you

**[13:45]** the memory part is built into it. Um you don't have to do any of that and it's

**[13:47]** don't have to do any of that and it's

**[13:47]** don't have to do any of that and it's going to scale automatically. It's going

**[13:49]** going to scale automatically. It's going

**[13:49]** going to scale automatically. It's going to run close to your AI agent and you

**[13:51]** to run close to your AI agent and you

**[13:51]** to run close to your AI agent and you don't really need to think about

**[13:52]** don't really need to think about

**[13:52]** don't really need to think about infrastructure at all. You just get all

**[13:54]** infrastructure at all. You just get all

**[13:54]** infrastructure at all. You just get all of that out of the box.

**[13:57]** of that out of the box.

**[13:57]** of that out of the box. Um you can actually so we have a blog

**[13:59]** Um you can actually so we have a blog

**[13:59]** Um you can actually so we have a blog post up. You can go and deploy your


### [14:00 - 15:00]

**[14:01]** post up. You can go and deploy your

**[14:01]** post up. You can go and deploy your first MCP server today. It's really

**[14:03]** first MCP server today. It's really

**[14:04]** first MCP server today. It's really really easy. There is literally a deploy

**[14:05]** really easy. There is literally a deploy

**[14:05]** really easy. There is literally a deploy to Cloudflare button. Takes um less than

**[14:08]** to Cloudflare button. Takes um less than

**[14:08]** to Cloudflare button. Takes um less than a minute to get your initial MCP server

**[14:11]** a minute to get your initial MCP server

**[14:11]** a minute to get your initial MCP server up and running. Uh and what's been

**[14:13]** up and running. Uh and what's been

**[14:13]** up and running. Uh and what's been really cool is working with some of the

**[14:15]** really cool is working with some of the

**[14:15]** really cool is working with some of the brands that we respect so so much and

**[14:17]** brands that we respect so so much and

**[14:17]** brands that we respect so so much and seeing companies like Atlassian, Asana,

**[14:20]** seeing companies like Atlassian, Asana,

**[14:20]** seeing companies like Atlassian, Asana, Stripe, Intercom building their own MCP

**[14:22]** Stripe, Intercom building their own MCP

**[14:22]** Stripe, Intercom building their own MCP servers in this exact way. So you're

**[14:24]** servers in this exact way. So you're

**[14:24]** servers in this exact way. So you're actually going down a really really

**[14:26]** actually going down a really really

**[14:26]** actually going down a really really welltrodden path here.

**[14:29]** welltrodden path here.

**[14:29]** welltrodden path here. Okay. So that was the tools part. Um so

**[14:32]** Okay. So that was the tools part. Um so

**[14:32]** Okay. So that was the tools part. Um so let's uh keep working backwards from

**[14:34]** let's uh keep working backwards from

**[14:34]** let's uh keep working backwards from from there. So we're we're giving our

**[14:36]** from there. So we're we're giving our

**[14:36]** from there. So we're we're giving our agents access to tools, but now we need

**[14:38]** agents access to tools, but now we need

**[14:38]** agents access to tools, but now we need a coordination component, right? Um a

**[14:41]** a coordination component, right? Um a

**[14:41]** a coordination component, right? Um a workflow that's going to maintain uh

**[14:44]** workflow that's going to maintain uh

**[14:44]** workflow that's going to maintain uh state not through just that one tool

**[14:46]** state not through just that one tool

**[14:46]** state not through just that one tool interaction, but through the entire

**[14:47]** interaction, but through the entire

**[14:48]** interaction, but through the entire chain with perhaps a human in the loop.

**[14:52]** chain with perhaps a human in the loop.

**[14:52]** chain with perhaps a human in the loop. Um, so human in the loop workflows

**[14:55]** Um, so human in the loop workflows

**[14:55]** Um, so human in the loop workflows require long uh require you to have

**[14:58]** require long uh require you to have

**[14:58]** require long uh require you to have really uh long running tasks that


### [15:00 - 16:00]

**[15:00]** really uh long running tasks that

**[15:00]** really uh long running tasks that sometimes need to talk to an LLM. It

**[15:02]** sometimes need to talk to an LLM. It

**[15:02]** sometimes need to talk to an LLM. It might be a reasoning LLM that takes

**[15:04]** might be a reasoning LLM that takes

**[15:04]** might be a reasoning LLM that takes several minutes to come up with a

**[15:06]** several minutes to come up with a

**[15:06]** several minutes to come up with a response. Um, and similarly, if you're

**[15:08]** response. Um, and similarly, if you're

**[15:08]** response. Um, and similarly, if you're talking to a human in the loop, a human

**[15:10]** talking to a human in the loop, a human

**[15:10]** talking to a human in the loop, a human could take minutes, hours, days, months

**[15:13]** could take minutes, hours, days, months

**[15:13]** could take minutes, hours, days, months to respond. Uh, and so you need

**[15:15]** to respond. Uh, and so you need

**[15:15]** to respond. Uh, and so you need something that's going to be able to

**[15:16]** something that's going to be able to

**[15:16]** something that's going to be able to come back and resume its flow after that

**[15:19]** come back and resume its flow after that

**[15:19]** come back and resume its flow after that task is completed. Um, you also still

**[15:21]** task is completed. Um, you also still

**[15:21]** task is completed. Um, you also still need to consider things like websocket

**[15:23]** need to consider things like websocket

**[15:23]** need to consider things like websocket servers, stay persistent, retries,

**[15:25]** servers, stay persistent, retries,

**[15:25]** servers, stay persistent, retries, horizontal scaling. These things can get

**[15:27]** horizontal scaling. These things can get

**[15:27]** horizontal scaling. These things can get white quite tricky. So again, let's walk

**[15:29]** white quite tricky. So again, let's walk

**[15:29]** white quite tricky. So again, let's walk through a real use case that uh we built

**[15:32]** through a real use case that uh we built

**[15:32]** through a real use case that uh we built out with a customer. Um, there's a

**[15:34]** out with a customer. Um, there's a

**[15:34]** out with a customer. Um, there's a company called Knock. They do

**[15:35]** company called Knock. They do

**[15:35]** company called Knock. They do notification management and they needed

**[15:38]** notification management and they needed

**[15:38]** notification management and they needed to provision uh an an agent that would

**[15:41]** to provision uh an an agent that would

**[15:41]** to provision uh an an agent that would do um approval when uh you you could

**[15:44]** do um approval when uh you you could

**[15:44]** do um approval when uh you you could request a new credit card, right? And

**[15:46]** request a new credit card, right? And

**[15:46]** request a new credit card, right? And then you know your boss needs to go and

**[15:48]** then you know your boss needs to go and

**[15:48]** then you know your boss needs to go and approve it through you know it can be um

**[15:51]** approve it through you know it can be um

**[15:51]** approve it through you know it can be um an email slack um inapp uh notification.

**[15:56]** an email slack um inapp uh notification.

**[15:56]** an email slack um inapp uh notification. So what do we need to do in order to do

**[15:58]** So what do we need to do in order to do

**[15:58]** So what do we need to do in order to do that? Um first we need to allow users to


### [16:00 - 17:00]

**[16:01]** that? Um first we need to allow users to

**[16:01]** that? Um first we need to allow users to request a new card through a chat

**[16:02]** request a new card through a chat

**[16:02]** request a new card through a chat interface. Uh so you can see that here

**[16:05]** interface. Uh so you can see that here

**[16:05]** interface. Uh so you can see that here we're importing use agent from um the

**[16:09]** we're importing use agent from um the

**[16:09]** we're importing use agent from um the from the agents react library and then

**[16:12]** from the agents react library and then

**[16:12]** from the agents react library and then we're going to have uh we're going to

**[16:14]** we're going to have uh we're going to

**[16:14]** we're going to have uh we're going to create a new instance of chat that's

**[16:16]** create a new instance of chat that's

**[16:16]** create a new instance of chat that's going to have all of these things

**[16:18]** going to have all of these things

**[16:18]** going to have all of these things instantiated on our behalf and this is

**[16:20]** instantiated on our behalf and this is

**[16:20]** instantiated on our behalf and this is all part of agents SDK. Um then we need

**[16:23]** all part of agents SDK. Um then we need

**[16:23]** all part of agents SDK. Um then we need to give it an ability to issue cards

**[16:26]** to give it an ability to issue cards

**[16:26]** to give it an ability to issue cards through this um issue card action. um

**[16:29]** through this um issue card action. um

**[16:30]** through this um issue card action. um but we need to wrap it in the require

**[16:32]** but we need to wrap it in the require

**[16:32]** but we need to wrap it in the require human input tool in order to delegate

**[16:35]** human input tool in order to delegate

**[16:35]** human input tool in order to delegate that piece to knock. So um we want to

**[16:37]** that piece to knock. So um we want to

**[16:37]** that piece to knock. So um we want to make sure that the issue card tool is

**[16:40]** make sure that the issue card tool is

**[16:40]** make sure that the issue card tool is always always requires the human input.

**[16:44]** always always requires the human input.

**[16:44]** always always requires the human input. Um then we need to invite no to send our

**[16:47]** Um then we need to invite no to send our

**[16:47]** Um then we need to invite no to send our approval notifications and defer the

**[16:49]** approval notifications and defer the

**[16:49]** approval notifications and defer the tool call to issue the card until there

**[16:52]** tool call to issue the card until there

**[16:52]** tool call to issue the card until there is approval. Right? Um, so we have a

**[16:54]** is approval. Right? Um, so we have a

**[16:54]** is approval. Right? Um, so we have a tool call to get a new car provision,

**[16:57]** tool call to get a new car provision,

**[16:57]** tool call to get a new car provision, but we want to stall that on the actual


### [17:00 - 18:00]

**[17:01]** but we want to stall that on the actual

**[17:01]** but we want to stall that on the actual approval. Um, so you can see that in

**[17:03]** approval. Um, so you can see that in

**[17:03]** approval. Um, so you can see that in here, um, where we're going to route the

**[17:06]** here, um, where we're going to route the

**[17:06]** here, um, where we're going to route the messages to approve something.

**[17:14]** Um, now once once something is approved,

**[17:14]** Um, now once once something is approved, we need to then route it back to the

**[17:16]** we need to then route it back to the

**[17:16]** we need to then route it back to the appropriate agent. And this is going to

**[17:18]** appropriate agent. And this is going to

**[17:18]** appropriate agent. And this is going to automatically be handled by the durable

**[17:20]** automatically be handled by the durable

**[17:20]** automatically be handled by the durable object and in instantly routed to the

**[17:23]** object and in instantly routed to the

**[17:23]** object and in instantly routed to the correct agent back. Um so you can see in

**[17:26]** correct agent back. Um so you can see in

**[17:26]** correct agent back. Um so you can see in here um that I'm going to find the user

**[17:28]** here um that I'm going to find the user

**[17:28]** here um that I'm going to find the user ID from the tool called for the calling

**[17:31]** ID from the tool called for the calling

**[17:31]** ID from the tool called for the calling user. Um and then I'm going to be able

**[17:34]** user. Um and then I'm going to be able

**[17:34]** user. Um and then I'm going to be able to look it up so I can get the agent by

**[17:36]** to look it up so I can get the agent by

**[17:36]** to look it up so I can get the agent by name by the user ID in here. And so then

**[17:40]** name by the user ID in here. And so then

**[17:40]** name by the user ID in here. And so then if it's an existing agent, we're going

**[17:41]** if it's an existing agent, we're going

**[17:41]** if it's an existing agent, we're going to route it to the correct durable

**[17:43]** to route it to the correct durable

**[17:43]** to route it to the correct durable object and make sure that we're handling

**[17:45]** object and make sure that we're handling

**[17:45]** object and make sure that we're handling it um with a correct uh web hook.

**[17:49]** it um with a correct uh web hook.

**[17:49]** it um with a correct uh web hook. We then need to resume the pause tool

**[17:52]** We then need to resume the pause tool

**[17:52]** We then need to resume the pause tool call, issue the card and let the user

**[17:54]** call, issue the card and let the user

**[17:54]** call, issue the card and let the user know that the card was approved, right?

**[17:56]** know that the card was approved, right?

**[17:56]** know that the card was approved, right? Um so in here, if we received an

**[17:58]** Um so in here, if we received an

**[17:58]** Um so in here, if we received an approved status, then we can move on


### [18:00 - 19:00]

**[18:01]** approved status, then we can move on

**[18:01]** approved status, then we can move on with the deferred uh tool execution uh

**[18:04]** with the deferred uh tool execution uh

**[18:04]** with the deferred uh tool execution uh that that we uh that we defined earlier.

**[18:07]** that that we uh that we defined earlier.

**[18:07]** that that we uh that we defined earlier. And then last but not least, we need to

**[18:09]** And then last but not least, we need to

**[18:09]** And then last but not least, we need to make sure the duplicate actions don't

**[18:10]** make sure the duplicate actions don't

**[18:10]** make sure the duplicate actions don't occur, right? So if two things happen

**[18:12]** occur, right? So if two things happen

**[18:12]** occur, right? So if two things happen out of sync, we can't approve the card

**[18:15]** out of sync, we can't approve the card

**[18:15]** out of sync, we can't approve the card twice. Uh or we can't provision the card

**[18:18]** twice. Uh or we can't provision the card

**[18:18]** twice. Uh or we can't provision the card twice. Um and so this is where again

**[18:20]** twice. Um and so this is where again

**[18:20]** twice. Um and so this is where again that state management becomes really

**[18:22]** that state management becomes really

**[18:22]** that state management becomes really really important. Um and we're able to

**[18:25]** really important. Um and we're able to

**[18:25]** really important. Um and we're able to store all of this directly in the state

**[18:28]** store all of this directly in the state

**[18:28]** store all of this directly in the state here. Um, so you can see if um, you

**[18:31]** here. Um, so you can see if um, you

**[18:31]** here. Um, so you can see if um, you know, the if the card has been request

**[18:33]** know, the if the card has been request

**[18:33]** know, the if the card has been request requested or processed already and then

**[18:36]** requested or processed already and then

**[18:36]** requested or processed already and then if it's been approved, we're going to

**[18:38]** if it's been approved, we're going to

**[18:38]** if it's been approved, we're going to set the status so when a new web hookup

**[18:41]** set the status so when a new web hookup

**[18:41]** set the status so when a new web hookup comes in, we can't reapprove the same

**[18:43]** comes in, we can't reapprove the same

**[18:43]** comes in, we can't reapprove the same exact one.

**[18:45]** exact one.

**[18:45]** exact one. Um, so we talked about uh we talked

**[18:47]** Um, so we talked about uh we talked

**[18:47]** Um, so we talked about uh we talked about tools, we talked about workflows.

**[18:49]** about tools, we talked about workflows.

**[18:49]** about tools, we talked about workflows. Um, next you need the uh the reasoning

**[18:51]** Um, next you need the uh the reasoning

**[18:51]** Um, next you need the uh the reasoning piece of this and need to choose the

**[18:53]** piece of this and need to choose the

**[18:53]** piece of this and need to choose the diff the right model to run this. Um,

**[18:56]** diff the right model to run this. Um,

**[18:56]** diff the right model to run this. Um, I'm actually going to skip this part

**[18:59]** I'm actually going to skip this part

**[18:59]** I'm actually going to skip this part because there's an entire conference


### [19:00 - 20:00]

**[19:00]** because there's an entire conference

**[19:00]** because there's an entire conference that's dedicated to this today um of

**[19:03]** that's dedicated to this today um of

**[19:03]** that's dedicated to this today um of people that are going to cover this way

**[19:04]** people that are going to cover this way

**[19:04]** people that are going to cover this way better than I will. Um, actually Logan's

**[19:07]** better than I will. Um, actually Logan's

**[19:07]** better than I will. Um, actually Logan's talk this morning about everything

**[19:08]** talk this morning about everything

**[19:08]** talk this morning about everything that's happening with Gemini was really

**[19:10]** that's happening with Gemini was really

**[19:10]** that's happening with Gemini was really really good. There's a bunch of people

**[19:11]** really good. There's a bunch of people

**[19:12]** really good. There's a bunch of people talking about eval. Um, but then uh but

**[19:15]** talking about eval. Um, but then uh but

**[19:15]** talking about eval. Um, but then uh but then you need you still need a client in

**[19:17]** then you need you still need a client in

**[19:17]** then you need you still need a client in order to connect to your server, right?

**[19:19]** order to connect to your server, right?

**[19:19]** order to connect to your server, right? And and again, this is the really

**[19:21]** And and again, this is the really

**[19:21]** And and again, this is the really beautiful thing about MCP is that once

**[19:24]** beautiful thing about MCP is that once

**[19:24]** beautiful thing about MCP is that once you built out your MCP server once, uh

**[19:27]** you built out your MCP server once, uh

**[19:27]** you built out your MCP server once, uh you can have uh you can truly meet your

**[19:29]** you can have uh you can truly meet your

**[19:29]** you can have uh you can truly meet your users where they are. Um and

**[19:32]** users where they are. Um and

**[19:32]** users where they are. Um and realistically, the nice thing is you

**[19:34]** realistically, the nice thing is you

**[19:34]** realistically, the nice thing is you actually you don't have to build a UI

**[19:36]** actually you don't have to build a UI

**[19:36]** actually you don't have to build a UI yourself at all. Um if you're if your

**[19:39]** yourself at all. Um if you're if your

**[19:39]** yourself at all. Um if you're if your users are developers, most likely

**[19:41]** users are developers, most likely

**[19:41]** users are developers, most likely they're already using Cursor. Uh and so

**[19:44]** they're already using Cursor. Uh and so

**[19:44]** they're already using Cursor. Uh and so now that cursor supports remote MCP

**[19:47]** now that cursor supports remote MCP

**[19:47]** now that cursor supports remote MCP servers, you just import your MCP server

**[19:50]** servers, you just import your MCP server

**[19:50]** servers, you just import your MCP server and have your clients be able to

**[19:51]** and have your clients be able to

**[19:51]** and have your clients be able to interact with it. Similarly, Claude and

**[19:53]** interact with it. Similarly, Claude and

**[19:53]** interact with it. Similarly, Claude and Chat GPT, they both support remote MCPs.

**[19:56]** Chat GPT, they both support remote MCPs.

**[19:56]** Chat GPT, they both support remote MCPs. So your users again can start using your

**[19:59]** So your users again can start using your

**[19:59]** So your users again can start using your agents instantly directly through there.


### [20:00 - 21:00]

**[20:03]** agents instantly directly through there.

**[20:03]** agents instantly directly through there. But you can also build your own app and

**[20:05]** But you can also build your own app and

**[20:06]** But you can also build your own app and your own MCP client. And I think this is

**[20:08]** your own MCP client. And I think this is

**[20:08]** your own MCP client. And I think this is where you can build really really

**[20:10]** where you can build really really

**[20:10]** where you can build really really interesting agentic workflows when you

**[20:12]** interesting agentic workflows when you

**[20:12]** interesting agentic workflows when you do have more control over both the

**[20:14]** do have more control over both the

**[20:14]** do have more control over both the client and the server uh and connecting

**[20:17]** client and the server uh and connecting

**[20:17]** client and the server uh and connecting these two pieces together. And not only

**[20:20]** these two pieces together. And not only

**[20:20]** these two pieces together. And not only that, but your app doesn't actually have

**[20:21]** that, but your app doesn't actually have

**[20:21]** that, but your app doesn't actually have to be limited to just being a user

**[20:24]** to be limited to just being a user

**[20:24]** to be limited to just being a user interface. You can also talk to your MCP

**[20:27]** interface. You can also talk to your MCP

**[20:27]** interface. You can also talk to your MCP a uh your MCP client over voice. um

**[20:31]** a uh your MCP client over voice. um

**[20:31]** a uh your MCP client over voice. um especially with um some of the

**[20:32]** especially with um some of the

**[20:32]** especially with um some of the Cloudflare tools that we have built out

**[20:35]** Cloudflare tools that we have built out

**[20:35]** Cloudflare tools that we have built out uh that help translate WebRTC to

**[20:37]** uh that help translate WebRTC to

**[20:37]** uh that help translate WebRTC to websocket in a way that really uh makes

**[20:39]** websocket in a way that really uh makes

**[20:39]** websocket in a way that really uh makes it easy to build out these applications

**[20:41]** it easy to build out these applications

**[20:41]** it easy to build out these applications because the MCB client can easily

**[20:43]** because the MCB client can easily

**[20:43]** because the MCB client can easily understand those connections.

**[20:47]** understand those connections.

**[20:47]** understand those connections. So yeah, how do you build an agent? Um

**[20:50]** So yeah, how do you build an agent? Um

**[20:50]** So yeah, how do you build an agent? Um these are the four different pieces you

**[20:51]** these are the four different pieces you

**[20:51]** these are the four different pieces you need. Your client, your AI, your

**[20:53]** need. Your client, your AI, your

**[20:53]** need. Your client, your AI, your workflows, your tools. Um, and if you

**[20:56]** workflows, your tools. Um, and if you

**[20:56]** workflows, your tools. Um, and if you want to get started and don't know where

**[20:57]** want to get started and don't know where

**[20:57]** want to get started and don't know where to start, I really, really highly

**[20:59]** to start, I really, really highly

**[20:59]** to start, I really, really highly recommend the agents SDK. You'll be able


### [21:00 - 22:00]

**[21:01]** recommend the agents SDK. You'll be able

**[21:01]** recommend the agents SDK. You'll be able to get up and running in just a few

**[21:03]** to get up and running in just a few

**[21:03]** to get up and running in just a few minutes. Um, yeah. So, thank you


