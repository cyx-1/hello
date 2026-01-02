# Agent Reinforcement Fine Tuning – Will Hang & Cathy Zhou, OpenAI

**Video URL:** https://www.youtube.com/watch?v=p1CmPZ2j6Lk

---

## Full Transcript

### [00:00 - 01:00]

**[00:22]** Hey everyone, I'm Will

**[00:22]** Hey everyone, I'm Will >> and I'm Kathy and we're on the fine

**[00:24]** >> and I'm Kathy and we're on the fine

**[00:24]** >> and I'm Kathy and we're on the fine tuning team at OpenAI

**[00:26]** tuning team at OpenAI

**[00:26]** tuning team at OpenAI >> and we're super excited to talk to you

**[00:28]** >> and we're super excited to talk to you

**[00:28]** >> and we're super excited to talk to you today about agent RF, the most powerful

**[00:30]** today about agent RF, the most powerful

**[00:30]** today about agent RF, the most powerful way to enhance the performance of your

**[00:32]** way to enhance the performance of your

**[00:32]** way to enhance the performance of your agents. So, you're probably joining us

**[00:34]** agents. So, you're probably joining us

**[00:34]** agents. So, you're probably joining us today because you're building an agent

**[00:36]** today because you're building an agent

**[00:36]** today because you're building an agent for your business and you'd like to

**[00:37]** for your business and you'd like to

**[00:37]** for your business and you'd like to improve its performance. So, let's first

**[00:40]** improve its performance. So, let's first

**[00:40]** improve its performance. So, let's first start by talking about what an agent

**[00:41]** start by talking about what an agent

**[00:41]** start by talking about what an agent actually is. What makes an agent

**[00:43]** actually is. What makes an agent

**[00:43]** actually is. What makes an agent different from a regular model is its

**[00:45]** different from a regular model is its

**[00:45]** different from a regular model is its ability to interact with the outside

**[00:47]** ability to interact with the outside

**[00:47]** ability to interact with the outside world to complete a task to get things

**[00:49]** world to complete a task to get things

**[00:49]** world to complete a task to get things done on its own without having to go

**[00:51]** done on its own without having to go

**[00:51]** done on its own without having to go through you all the time. So, this agent

**[00:53]** through you all the time. So, this agent

**[00:53]** through you all the time. So, this agent needs to have access to tools. For

**[00:54]** needs to have access to tools. For

**[00:54]** needs to have access to tools. For example, if you're building a coding

**[00:55]** example, if you're building a coding

**[00:56]** example, if you're building a coding agent, it's got to have access to a

**[00:57]** agent, it's got to have access to a

**[00:57]** agent, it's got to have access to a terminal, a code interpreter, or maybe

**[00:59]** terminal, a code interpreter, or maybe

**[00:59]** terminal, a code interpreter, or maybe even an entire codebase.


### [01:00 - 02:00]

**[01:01]** even an entire codebase.

**[01:01]** even an entire codebase. But these agents aren't just blindly

**[01:03]** But these agents aren't just blindly

**[01:03]** But these agents aren't just blindly calling tools. They're reasoning at the

**[01:05]** calling tools. They're reasoning at the

**[01:05]** calling tools. They're reasoning at the same time. The way that we think about

**[01:07]** same time. The way that we think about

**[01:07]** same time. The way that we think about these agents is that their interactions

**[01:09]** these agents is that their interactions

**[01:09]** these agents is that their interactions with the outside world, such as tool

**[01:11]** with the outside world, such as tool

**[01:11]** with the outside world, such as tool calls, are interled with their reasoning

**[01:13]** calls, are interled with their reasoning

**[01:13]** calls, are interled with their reasoning traces in the same context window. So,

**[01:16]** traces in the same context window. So,

**[01:16]** traces in the same context window. So, an example of an agent that we've built

**[01:17]** an example of an agent that we've built

**[01:17]** an example of an agent that we've built in-house using this paradigm is Codeex.

**[01:20]** in-house using this paradigm is Codeex.

**[01:20]** in-house using this paradigm is Codeex. Codeex is our flagship coding agent. has

**[01:23]** Codeex is our flagship coding agent. has

**[01:23]** Codeex is our flagship coding agent. has access to a wide range of tools to

**[01:26]** access to a wide range of tools to

**[01:26]** access to a wide range of tools to complete coding tasks end to end like

**[01:28]** complete coding tasks end to end like

**[01:28]** complete coding tasks end to end like writing unit tests or submitting large

**[01:30]** writing unit tests or submitting large

**[01:30]** writing unit tests or submitting large diffs to your codebase that are

**[01:32]** diffs to your codebase that are

**[01:32]** diffs to your codebase that are hopefully correct. Um some tools are

**[01:34]** hopefully correct. Um some tools are

**[01:34]** hopefully correct. Um some tools are exposed as terminal commands and other

**[01:36]** exposed as terminal commands and other

**[01:36]** exposed as terminal commands and other tools are custom functions a model can

**[01:38]** tools are custom functions a model can

**[01:38]** tools are custom functions a model can call to invoke say a planning workflow.

**[01:41]** call to invoke say a planning workflow.

**[01:41]** call to invoke say a planning workflow. So now how do we make our agents better?

**[01:44]** So now how do we make our agents better?

**[01:44]** So now how do we make our agents better? We're all probably pretty familiar with

**[01:46]** We're all probably pretty familiar with

**[01:46]** We're all probably pretty familiar with the frontline techniques to improve the

**[01:48]** the frontline techniques to improve the

**[01:48]** the frontline techniques to improve the performance of agents. For example, for

**[01:50]** performance of agents. For example, for

**[01:50]** performance of agents. For example, for starters, prompt engineering or prompt

**[01:52]** starters, prompt engineering or prompt

**[01:52]** starters, prompt engineering or prompt optimization. Prompting you can steer

**[01:55]** optimization. Prompting you can steer

**[01:55]** optimization. Prompting you can steer model or agent behavior to align more

**[01:57]** model or agent behavior to align more

**[01:57]** model or agent behavior to align more with your preferences. But let's say you

**[01:59]** with your preferences. But let's say you

**[01:59]** with your preferences. But let's say you still want to squeeze more juice out of


### [02:00 - 03:00]

**[02:00]** still want to squeeze more juice out of

**[02:00]** still want to squeeze more juice out of your task. Well, you can then turn to

**[02:03]** your task. Well, you can then turn to

**[02:03]** your task. Well, you can then turn to task optimization. You can simplify the

**[02:05]** task optimization. You can simplify the

**[02:05]** task optimization. You can simplify the task. You can add better guard rails

**[02:07]** task. You can add better guard rails

**[02:07]** task. You can add better guard rails around the task. You can add and

**[02:09]** around the task. You can add and

**[02:09]** around the task. You can add and subtract tools. Or you can change tool

**[02:12]** subtract tools. Or you can change tool

**[02:12]** subtract tools. Or you can change tool behavior to work better for the agent.

**[02:15]** behavior to work better for the agent.

**[02:15]** behavior to work better for the agent. But let's say you still want to squeeze

**[02:16]** But let's say you still want to squeeze

**[02:16]** But let's say you still want to squeeze even more juice out of that task. you've

**[02:18]** even more juice out of that task. you've

**[02:18]** even more juice out of that task. you've tried all these approaches and you still

**[02:19]** tried all these approaches and you still

**[02:19]** tried all these approaches and you still want better performance. So that's where

**[02:21]** want better performance. So that's where

**[02:21]** want better performance. So that's where you would turn to fine-tuning.

**[02:23]** you would turn to fine-tuning.

**[02:23]** you would turn to fine-tuning. Fine-tuning is a way to train the a

**[02:25]** Fine-tuning is a way to train the a

**[02:25]** Fine-tuning is a way to train the a agent end to end on your task to achieve

**[02:28]** agent end to end on your task to achieve

**[02:28]** agent end to end on your task to achieve even better performance by changing the

**[02:31]** even better performance by changing the

**[02:31]** even better performance by changing the weights of the model. And agent

**[02:33]** weights of the model. And agent

**[02:33]** weights of the model. And agent reinforcement fine-tuning or agent RF is

**[02:36]** reinforcement fine-tuning or agent RF is

**[02:36]** reinforcement fine-tuning or agent RF is the way to do this or it's the way that

**[02:38]** the way to do this or it's the way that

**[02:38]** the way to do this or it's the way that we would like you all to do this. Um,

**[02:40]** we would like you all to do this. Um,

**[02:40]** we would like you all to do this. Um, agent RFT changes the weights of the

**[02:42]** agent RFT changes the weights of the

**[02:42]** agent RFT changes the weights of the model according to a learning signal

**[02:43]** model according to a learning signal

**[02:43]** model according to a learning signal that you specify to teach the model what

**[02:45]** that you specify to teach the model what

**[02:45]** that you specify to teach the model what good behavior and what bad behavior

**[02:47]** good behavior and what bad behavior

**[02:47]** good behavior and what bad behavior looks like. And during training, the

**[02:48]** looks like. And during training, the

**[02:48]** looks like. And during training, the agent will explore many different ways

**[02:50]** agent will explore many different ways

**[02:50]** agent will explore many different ways of calling your tools to solve your

**[02:52]** of calling your tools to solve your

**[02:52]** of calling your tools to solve your task. So, we've introduced several major

**[02:55]** task. So, we've introduced several major

**[02:55]** task. So, we've introduced several major new additions to the RFT product. Um,

**[02:57]** new additions to the RFT product. Um,

**[02:57]** new additions to the RFT product. Um, first off, the model can now call your

**[02:59]** first off, the model can now call your

**[02:59]** first off, the model can now call your tools via your endpoints that are hosted


### [03:00 - 04:00]

**[03:02]** tools via your endpoints that are hosted

**[03:02]** tools via your endpoints that are hosted in the public internet. Um, and after

**[03:04]** in the public internet. Um, and after

**[03:04]** in the public internet. Um, and after each roll out, we'll also invoke your

**[03:06]** each roll out, we'll also invoke your

**[03:06]** each roll out, we'll also invoke your custom reward signal that's hosted via

**[03:09]** custom reward signal that's hosted via

**[03:09]** custom reward signal that's hosted via an endpoint. So, these two additions

**[03:10]** an endpoint. So, these two additions

**[03:10]** an endpoint. So, these two additions actually mark the first time that we

**[03:12]** actually mark the first time that we

**[03:12]** actually mark the first time that we have we at OpenAI have allowed models to

**[03:15]** have we at OpenAI have allowed models to

**[03:15]** have we at OpenAI have allowed models to interact with the outside world during

**[03:17]** interact with the outside world during

**[03:17]** interact with the outside world during the training process. So, I think this

**[03:18]** the training process. So, I think this

**[03:18]** the training process. So, I think this is pretty cool. To summarize the

**[03:21]** is pretty cool. To summarize the

**[03:21]** is pretty cool. To summarize the benefits of agent RFT, it helps you

**[03:24]** benefits of agent RFT, it helps you

**[03:24]** benefits of agent RFT, it helps you improve the performance of your

**[03:25]** improve the performance of your

**[03:25]** improve the performance of your reasoning models, but more specifically

**[03:27]** reasoning models, but more specifically

**[03:27]** reasoning models, but more specifically the reasoning models that have to call

**[03:29]** the reasoning models that have to call

**[03:29]** the reasoning models that have to call tools and interact with the outside

**[03:31]** tools and interact with the outside

**[03:31]** tools and interact with the outside world to get things done in a multi-step

**[03:33]** world to get things done in a multi-step

**[03:33]** world to get things done in a multi-step fashion. Agent RF is also quite sample

**[03:36]** fashion. Agent RF is also quite sample

**[03:36]** fashion. Agent RF is also quite sample efficient. We've seen people get success

**[03:37]** efficient. We've seen people get success

**[03:37]** efficient. We've seen people get success from literally only using like 10

**[03:39]** from literally only using like 10

**[03:40]** from literally only using like 10 examples, which is pretty amazing. We'll

**[03:41]** examples, which is pretty amazing. We'll

**[03:41]** examples, which is pretty amazing. We'll go over specific examples of this when

**[03:43]** go over specific examples of this when

**[03:43]** go over specific examples of this when we deep dive into some of our customer

**[03:45]** we deep dive into some of our customer

**[03:45]** we deep dive into some of our customer spotlights. and it results in a model

**[03:47]** spotlights. and it results in a model

**[03:47]** spotlights. and it results in a model that has lower latency and just works

**[03:49]** that has lower latency and just works

**[03:49]** that has lower latency and just works better for your tasks.

**[03:51]** better for your tasks.

**[03:52]** better for your tasks. So now let's dive a little bit deeper

**[03:53]** So now let's dive a little bit deeper

**[03:53]** So now let's dive a little bit deeper into how all this works. One of the

**[03:55]** into how all this works. One of the

**[03:55]** into how all this works. One of the challenges with making agents work with

**[03:57]** challenges with making agents work with

**[03:57]** challenges with making agents work with your specific business context is that


### [04:00 - 05:00]

**[04:00]** your specific business context is that

**[04:00]** your specific business context is that your environment, your world might just

**[04:02]** your environment, your world might just

**[04:02]** your environment, your world might just be different from how we train our

**[04:04]** be different from how we train our

**[04:04]** be different from how we train our models in house. So this phenomenon in

**[04:06]** models in house. So this phenomenon in

**[04:06]** models in house. So this phenomenon in ML is called domain shift. And it can

**[04:09]** ML is called domain shift. And it can

**[04:09]** ML is called domain shift. And it can result in an agent that doesn't quite

**[04:11]** result in an agent that doesn't quite

**[04:11]** result in an agent that doesn't quite call your tools that that well. might

**[04:13]** call your tools that that well. might

**[04:13]** call your tools that that well. might call a tool too many times or might just

**[04:15]** call a tool too many times or might just

**[04:15]** call a tool too many times or might just straight up shove wrong inputs into your

**[04:17]** straight up shove wrong inputs into your

**[04:17]** straight up shove wrong inputs into your tools. Agent RFT can readapt the model

**[04:21]** tools. Agent RFT can readapt the model

**[04:21]** tools. Agent RFT can readapt the model to your domain through this weight

**[04:23]** to your domain through this weight

**[04:23]** to your domain through this weight changing training process that results

**[04:25]** changing training process that results

**[04:25]** changing training process that results in an agent that actually understands

**[04:27]** in an agent that actually understands

**[04:27]** in an agent that actually understands your environment. And this has some

**[04:29]** your environment. And this has some

**[04:29]** your environment. And this has some really nice properties obviously better

**[04:31]** really nice properties obviously better

**[04:31]** really nice properties obviously better ML performance. It trains the model to

**[04:34]** ML performance. It trains the model to

**[04:34]** ML performance. It trains the model to use tools better and it trains the model

**[04:35]** use tools better and it trains the model

**[04:35]** use tools better and it trains the model to reason over the outputs of those

**[04:38]** to reason over the outputs of those

**[04:38]** to reason over the outputs of those tools better. All this is learned

**[04:39]** tools better. All this is learned

**[04:39]** tools better. All this is learned organically by the model while it

**[04:41]** organically by the model while it

**[04:41]** organically by the model while it explores the search space, all the

**[04:43]** explores the search space, all the

**[04:43]** explores the search space, all the possible ways of interacting with your

**[04:45]** possible ways of interacting with your

**[04:45]** possible ways of interacting with your environment and hill climbing on your

**[04:47]** environment and hill climbing on your

**[04:47]** environment and hill climbing on your reward. Another really nice property

**[04:49]** reward. Another really nice property

**[04:49]** reward. Another really nice property that results from this is the ability to

**[04:51]** that results from this is the ability to

**[04:51]** that results from this is the ability to achieve much lower latencies by making

**[04:54]** achieve much lower latencies by making

**[04:54]** achieve much lower latencies by making sure that the model stays within a given

**[04:56]** sure that the model stays within a given

**[04:56]** sure that the model stays within a given tool called budget and doesn't go over

**[04:57]** tool called budget and doesn't go over

**[04:57]** tool called budget and doesn't go over that limit. So we can actually impose

**[04:59]** that limit. So we can actually impose

**[04:59]** that limit. So we can actually impose this penalty that you know penalizes the


### [05:00 - 06:00]

**[05:01]** this penalty that you know penalizes the

**[05:01]** this penalty that you know penalizes the model for going over that budget. What

**[05:03]** model for going over that budget. What

**[05:03]** model for going over that budget. What actually happens is the model learns to

**[05:05]** actually happens is the model learns to

**[05:05]** actually happens is the model learns to stay within that budget while preserving

**[05:07]** stay within that budget while preserving

**[05:07]** stay within that budget while preserving or exceeding the original ML

**[05:09]** or exceeding the original ML

**[05:09]** or exceeding the original ML performance.

**[05:10]** performance.

**[05:10]** performance. So to dive a little bit deeper into what

**[05:12]** So to dive a little bit deeper into what

**[05:12]** So to dive a little bit deeper into what happens at a systems level for each

**[05:14]** happens at a systems level for each

**[05:14]** happens at a systems level for each agent roll out will produce this unique

**[05:16]** agent roll out will produce this unique

**[05:16]** agent roll out will produce this unique identifier that specifies that that that

**[05:19]** identifier that specifies that that that

**[05:20]** identifier that specifies that that that particular roll out and we will

**[05:21]** particular roll out and we will

**[05:21]** particular roll out and we will associate all the tool calls that we

**[05:23]** associate all the tool calls that we

**[05:23]** associate all the tool calls that we make into your system with that UYU ID.

**[05:27]** make into your system with that UYU ID.

**[05:27]** make into your system with that UYU ID. And so we do this for every tool call so

**[05:29]** And so we do this for every tool call so

**[05:29]** And so we do this for every tool call so that you can keep track of a trajectory

**[05:31]** that you can keep track of a trajectory

**[05:31]** that you can keep track of a trajectory as it evolves. so that when we emit that

**[05:33]** as it evolves. so that when we emit that

**[05:33]** as it evolves. so that when we emit that final answer at the very end, you can

**[05:35]** final answer at the very end, you can

**[05:35]** final answer at the very end, you can then associate that final answer with

**[05:37]** then associate that final answer with

**[05:37]** then associate that final answer with all the context that you've maintained

**[05:39]** all the context that you've maintained

**[05:39]** all the context that you've maintained so far and you can just pass this whole

**[05:41]** so far and you can just pass this whole

**[05:41]** so far and you can just pass this whole thing as a holistic grading context into

**[05:43]** thing as a holistic grading context into

**[05:43]** thing as a holistic grading context into your grader. Now, we don't recommend

**[05:46]** your grader. Now, we don't recommend

**[05:46]** your grader. Now, we don't recommend everyone or anyone just use agent RFT

**[05:48]** everyone or anyone just use agent RFT

**[05:48]** everyone or anyone just use agent RFT right off the bat. Uh there's a process

**[05:50]** right off the bat. Uh there's a process

**[05:50]** right off the bat. Uh there's a process that we'd like you all to follow. You

**[05:52]** that we'd like you all to follow. You

**[05:52]** that we'd like you all to follow. You first want to make sure that your

**[05:53]** first want to make sure that your

**[05:53]** first want to make sure that your training data set and your eval data set

**[05:55]** training data set and your eval data set

**[05:55]** training data set and your eval data set closely match your production traffic.

**[05:57]** closely match your production traffic.

**[05:57]** closely match your production traffic. You do not want any drift whatsoever.


### [06:00 - 07:00]

**[06:00]** You do not want any drift whatsoever.

**[06:00]** You do not want any drift whatsoever. Then you want to ground yourself in a

**[06:02]** Then you want to ground yourself in a

**[06:02]** Then you want to ground yourself in a baseline. You want to run your base

**[06:03]** baseline. You want to run your base

**[06:04]** baseline. You want to run your base model against these data sets so that

**[06:06]** model against these data sets so that

**[06:06]** model against these data sets so that you kind of understand what to expect

**[06:08]** you kind of understand what to expect

**[06:08]** you kind of understand what to expect performance-wise so that you can then

**[06:09]** performance-wise so that you can then

**[06:09]** performance-wise so that you can then hill climb from there. And then you want

**[06:12]** hill climb from there. And then you want

**[06:12]** hill climb from there. And then you want to optimize performance using some of

**[06:14]** to optimize performance using some of

**[06:14]** to optimize performance using some of the techniques that we talked about

**[06:15]** the techniques that we talked about

**[06:15]** the techniques that we talked about prior like prompt or task optimization.

**[06:18]** prior like prompt or task optimization.

**[06:18]** prior like prompt or task optimization. And only then when you still feel like

**[06:20]** And only then when you still feel like

**[06:20]** And only then when you still feel like you squeezed all the juice out of the

**[06:22]** you squeezed all the juice out of the

**[06:22]** you squeezed all the juice out of the task, but you still want more more

**[06:24]** task, but you still want more more

**[06:24]** task, but you still want more more juice, you would turn to agent RFT to

**[06:26]** juice, you would turn to agent RFT to

**[06:26]** juice, you would turn to agent RFT to push the frontier for your task. So now

**[06:29]** push the frontier for your task. So now

**[06:29]** push the frontier for your task. So now I'm going to turn it over to Kathy to

**[06:31]** I'm going to turn it over to Kathy to

**[06:31]** I'm going to turn it over to Kathy to talk about how some of our partners have

**[06:32]** talk about how some of our partners have

**[06:32]** talk about how some of our partners have really pushed that frontier.

**[06:35]** really pushed that frontier.

**[06:35]** really pushed that frontier. >> Yeah. So now that we learned how agent

**[06:38]** >> Yeah. So now that we learned how agent

**[06:38]** >> Yeah. So now that we learned how agent RFT works and how when you should use

**[06:40]** RFT works and how when you should use

**[06:40]** RFT works and how when you should use it, I'll show you some coding related

**[06:42]** it, I'll show you some coding related

**[06:42]** it, I'll show you some coding related examples of how our customers were able

**[06:44]** examples of how our customers were able

**[06:44]** examples of how our customers were able to use agent RFT to make their agents

**[06:46]** to use agent RFT to make their agents

**[06:46]** to use agent RFT to make their agents better and also highlight some key

**[06:48]** better and also highlight some key

**[06:48]** better and also highlight some key takeaways that you can apply when

**[06:50]** takeaways that you can apply when

**[06:50]** takeaways that you can apply when optimizing your own agents. So a few

**[06:53]** optimizing your own agents. So a few

**[06:53]** optimizing your own agents. So a few months ago we partnered with Cognition

**[06:55]** months ago we partnered with Cognition

**[06:55]** months ago we partnered with Cognition who use agent RFT on their code edit

**[06:58]** who use agent RFT on their code edit

**[06:58]** who use agent RFT on their code edit planning phase. This is the part where


### [07:00 - 08:00]

**[07:00]** planning phase. This is the part where

**[07:00]** planning phase. This is the part where Devon inspects a reple and runs runs

**[07:03]** Devon inspects a reple and runs runs

**[07:03]** Devon inspects a reple and runs runs shell tools like rep and file reads to

**[07:05]** shell tools like rep and file reads to

**[07:05]** shell tools like rep and file reads to decide which exact files to edit. To

**[07:08]** decide which exact files to edit. To

**[07:08]** decide which exact files to edit. To train this behavior they build a data

**[07:10]** train this behavior they build a data

**[07:10]** train this behavior they build a data set of user queries paired with actual

**[07:12]** set of user queries paired with actual

**[07:12]** set of user queries paired with actual files that's that users has modified and

**[07:15]** files that's that users has modified and

**[07:15]** files that's that users has modified and they use the F1 score of the selected

**[07:17]** they use the F1 score of the selected

**[07:17]** they use the F1 score of the selected files as the reward. This F1 score is

**[07:20]** files as the reward. This F1 score is

**[07:20]** files as the reward. This F1 score is really great because it balances between

**[07:23]** really great because it balances between

**[07:23]** really great because it balances between the pre precision and the recall. So

**[07:25]** the pre precision and the recall. So

**[07:25]** the pre precision and the recall. So this ensures that the agent doesn't

**[07:27]** this ensures that the agent doesn't

**[07:27]** this ensures that the agent doesn't return too many inaccurate files or

**[07:29]** return too many inaccurate files or

**[07:29]** return too many inaccurate files or misses the critical ones. They also

**[07:32]** misses the critical ones. They also

**[07:32]** misses the critical ones. They also build extremely robust infrastructure to

**[07:35]** build extremely robust infrastructure to

**[07:35]** build extremely robust infrastructure to support this training. So in this case

**[07:37]** support this training. So in this case

**[07:37]** support this training. So in this case for each individual trajectory they spun

**[07:39]** for each individual trajectory they spun

**[07:39]** for each individual trajectory they spun up a VM to manage the codebase to

**[07:42]** up a VM to manage the codebase to

**[07:42]** up a VM to manage the codebase to execute the tool calls and grade the

**[07:44]** execute the tool calls and grade the

**[07:44]** execute the tool calls and grade the final answer. These VMs make sure that

**[07:46]** final answer. These VMs make sure that

**[07:46]** final answer. These VMs make sure that the environment is isolated so that the

**[07:49]** the environment is isolated so that the

**[07:49]** the environment is isolated so that the shell tools will not affect each other

**[07:51]** shell tools will not affect each other

**[07:51]** shell tools will not affect each other in different rollouts.

**[07:53]** in different rollouts.

**[07:53]** in different rollouts. We saw two important takeaways from

**[07:56]** We saw two important takeaways from

**[07:56]** We saw two important takeaways from Cognition's use case. First, data

**[07:58]** Cognition's use case. First, data

**[07:58]** Cognition's use case. First, data quality and the volume really matters.


### [08:00 - 09:00]

**[08:00]** quality and the volume really matters.

**[08:00]** quality and the volume really matters. So, at first they fine-tuned on a data

**[08:03]** So, at first they fine-tuned on a data

**[08:03]** So, at first they fine-tuned on a data set of around 100 examples and were able

**[08:05]** set of around 100 examples and were able

**[08:06]** set of around 100 examples and were able to get a fivepoint improvement. But when

**[08:08]** to get a fivepoint improvement. But when

**[08:08]** to get a fivepoint improvement. But when they scaled to a thousand examples, the

**[08:10]** they scaled to a thousand examples, the

**[08:10]** they scaled to a thousand examples, the improvement jumped to 10 points. So the

**[08:12]** improvement jumped to 10 points. So the

**[08:12]** improvement jumped to 10 points. So the number of highquality examples you

**[08:15]** number of highquality examples you

**[08:15]** number of highquality examples you provide can very directly translate to a

**[08:18]** provide can very directly translate to a

**[08:18]** provide can very directly translate to a better agent behavior. Second, we also

**[08:21]** better agent behavior. Second, we also

**[08:21]** better agent behavior. Second, we also learned that RFT is really good for

**[08:24]** learned that RFT is really good for

**[08:24]** learned that RFT is really good for learning to call tools in parallel. So

**[08:26]** learning to call tools in parallel. So

**[08:26]** learning to call tools in parallel. So in this case, the model would initially

**[08:29]** in this case, the model would initially

**[08:29]** in this case, the model would initially take 8 to 10 steps alternating between

**[08:32]** take 8 to 10 steps alternating between

**[08:32]** take 8 to 10 steps alternating between generating tokens in its reasoning to

**[08:35]** generating tokens in its reasoning to

**[08:35]** generating tokens in its reasoning to actually calling the tools. After RFT,

**[08:38]** actually calling the tools. After RFT,

**[08:38]** actually calling the tools. After RFT, the agent launches many tool calls in

**[08:40]** the agent launches many tool calls in

**[08:40]** the agent launches many tool calls in parallel. at the very first step. So

**[08:43]** parallel. at the very first step. So

**[08:43]** parallel. at the very first step. So this was able to reduce that number down

**[08:45]** this was able to reduce that number down

**[08:45]** this was able to reduce that number down to four. And in this use case, the speed

**[08:48]** to four. And in this use case, the speed

**[08:48]** to four. And in this use case, the speed up was especially important because they

**[08:50]** up was especially important because they

**[08:50]** up was especially important because they wanted Devon to start producing edits

**[08:53]** wanted Devon to start producing edits

**[08:53]** wanted Devon to start producing edits quickly.

**[08:55]** quickly.

**[08:55]** quickly. And now I want to highlight a different

**[08:57]** And now I want to highlight a different

**[08:57]** And now I want to highlight a different use case. Codto is building a code

**[08:59]** use case. Codto is building a code

**[08:59]** use case. Codto is building a code review agent and a key piece of that is


### [09:00 - 10:00]

**[09:02]** review agent and a key piece of that is

**[09:02]** review agent and a key piece of that is a deep research agent that answers

**[09:04]** a deep research agent that answers

**[09:04]** a deep research agent that answers developer questions on large code bases.

**[09:07]** developer questions on large code bases.

**[09:07]** developer questions on large code bases. To improve this deep research agent,

**[09:10]** To improve this deep research agent,

**[09:10]** To improve this deep research agent, they train GPD5 to answer coding

**[09:13]** they train GPD5 to answer coding

**[09:13]** they train GPD5 to answer coding questions by calling tools like search

**[09:15]** questions by calling tools like search

**[09:15]** questions by calling tools like search and retrieve over the repository. They

**[09:18]** and retrieve over the repository. They

**[09:18]** and retrieve over the repository. They assembled around a thousand authentic

**[09:21]** assembled around a thousand authentic

**[09:21]** assembled around a thousand authentic question answer pairs from eight

**[09:23]** question answer pairs from eight

**[09:23]** question answer pairs from eight different uh repositories and rewarded

**[09:26]** different uh repositories and rewarded

**[09:26]** different uh repositories and rewarded the model using the recall of how many

**[09:28]** the model using the recall of how many

**[09:28]** the model using the recall of how many relevant facts the agent were able to

**[09:30]** relevant facts the agent were able to

**[09:30]** relevant facts the agent were able to retrieve.

**[09:32]** retrieve.

**[09:32]** retrieve. [clears throat]

**[09:33]** [clears throat]

**[09:33]** [clears throat] With RFT, the agent improved by 6% and

**[09:37]** With RFT, the agent improved by 6% and

**[09:37]** With RFT, the agent improved by 6% and it was using fewer tool calls and output

**[09:39]** it was using fewer tool calls and output

**[09:40]** it was using fewer tool calls and output tokens. And what we found most

**[09:41]** tokens. And what we found most

**[09:41]** tokens. And what we found most interesting is this graph where it shows

**[09:44]** interesting is this graph where it shows

**[09:44]** interesting is this graph where it shows how RFT shifted the distribution of the

**[09:47]** how RFT shifted the distribution of the

**[09:47]** how RFT shifted the distribution of the number of tool calls. So with BBD5, the

**[09:50]** number of tool calls. So with BBD5, the

**[09:50]** number of tool calls. So with BBD5, the agent will occasionally fall into these

**[09:53]** agent will occasionally fall into these

**[09:53]** agent will occasionally fall into these bad runs where there were more than 15

**[09:55]** bad runs where there were more than 15

**[09:55]** bad runs where there were more than 15 tool calls in a single sample. This is

**[09:58]** tool calls in a single sample. This is

**[09:58]** tool calls in a single sample. This is very slow and also can lead to some


### [10:00 - 11:00]

**[10:00]** very slow and also can lead to some

**[10:00]** very slow and also can lead to some inconsistent behaviors. So after RFT

**[10:03]** inconsistent behaviors. So after RFT

**[10:03]** inconsistent behaviors. So after RFT these tool calls that are very longtail

**[10:06]** these tool calls that are very longtail

**[10:06]** these tool calls that are very longtail um disappeared and the the distribution

**[10:09]** um disappeared and the the distribution

**[10:09]** um disappeared and the the distribution center to just around two to four tool

**[10:11]** center to just around two to four tool

**[10:11]** center to just around two to four tool calls. In this setup RFT didn't just

**[10:14]** calls. In this setup RFT didn't just

**[10:14]** calls. In this setup RFT didn't just improve uh accuracy. It also stabilized

**[10:17]** improve uh accuracy. It also stabilized

**[10:17]** improve uh accuracy. It also stabilized the agents behavior in eliminating these

**[10:20]** the agents behavior in eliminating these

**[10:20]** the agents behavior in eliminating these P95 longtail cases. And this is very

**[10:24]** P95 longtail cases. And this is very

**[10:24]** P95 longtail cases. And this is very important for production use cases where

**[10:26]** important for production use cases where

**[10:26]** important for production use cases where your latency will matter.

**[10:29]** your latency will matter.

**[10:29]** your latency will matter. Next, I want to share how cosign build

**[10:32]** Next, I want to share how cosign build

**[10:32]** Next, I want to share how cosign build coding agents for large and complex

**[10:35]** coding agents for large and complex

**[10:35]** coding agents for large and complex enterprise code uh enterprise co code

**[10:38]** enterprise code uh enterprise co code

**[10:38]** enterprise code uh enterprise co code bases with agent rft. To make this work,

**[10:41]** bases with agent rft. To make this work,

**[10:41]** bases with agent rft. To make this work, they train the agent on a very

**[10:43]** they train the agent on a very

**[10:43]** they train the agent on a very comprehensive set of 30 tools such as

**[10:46]** comprehensive set of 30 tools such as

**[10:46]** comprehensive set of 30 tools such as fry, keyword search, session terminal,

**[10:48]** fry, keyword search, session terminal,

**[10:48]** fry, keyword search, session terminal, browser sessions, etc. And they also

**[10:52]** browser sessions, etc. And they also

**[10:52]** browser sessions, etc. And they also built a very strict raider. So they

**[10:54]** built a very strict raider. So they

**[10:54]** built a very strict raider. So they observed that the model um originally

**[10:57]** observed that the model um originally

**[10:57]** observed that the model um originally when they were providing the model with

**[10:59]** when they were providing the model with

**[10:59]** when they were providing the model with partial credits and uh points for just


### [11:00 - 12:00]

**[11:02]** partial credits and uh points for just

**[11:02]** partial credits and uh points for just trying out things um it didn't get

**[11:04]** trying out things um it didn't get

**[11:04]** trying out things um it didn't get really good results because the model

**[11:05]** really good results because the model

**[11:06]** really good results because the model would start to optimize things on coding

**[11:08]** would start to optimize things on coding

**[11:08]** would start to optimize things on coding style and tone. Um so at first they want

**[11:11]** style and tone. Um so at first they want

**[11:11]** style and tone. Um so at first they want to really make sure the agent ships

**[11:14]** to really make sure the agent ships

**[11:14]** to really make sure the agent ships working code and so based on that they

**[11:17]** working code and so based on that they

**[11:17]** working code and so based on that they give the model the reward only when the

**[11:20]** give the model the reward only when the

**[11:20]** give the model the reward only when the final code passes the test. And because

**[11:22]** final code passes the test. And because

**[11:22]** final code passes the test. And because the greater is very strict, it can

**[11:24]** the greater is very strict, it can

**[11:24]** the greater is very strict, it can sometimes give sparse rewards. In that

**[11:27]** sometimes give sparse rewards. In that

**[11:27]** sometimes give sparse rewards. In that case, um, GBD5 is also like is actually

**[11:30]** case, um, GBD5 is also like is actually

**[11:30]** case, um, GBD5 is also like is actually very great because it can give us some

**[11:32]** very great because it can give us some

**[11:32]** very great because it can give us some samples that work. So, um, Cosine also

**[11:36]** samples that work. So, um, Cosine also

**[11:36]** samples that work. So, um, Cosine also boosted the batch size and they increase

**[11:38]** boosted the batch size and they increase

**[11:38]** boosted the batch size and they increase the amount of compute so that there is

**[11:41]** the amount of compute so that there is

**[11:41]** the amount of compute so that there is even more samples that can give us

**[11:42]** even more samples that can give us

**[11:42]** even more samples that can give us positive rewards. So, it's not like

**[11:45]** positive rewards. So, it's not like

**[11:45]** positive rewards. So, it's not like every single sample in the batch will

**[11:47]** every single sample in the batch will

**[11:47]** every single sample in the batch will give us zero reward once the code is

**[11:49]** give us zero reward once the code is

**[11:49]** give us zero reward once the code is correct. Um, they also have a custom LLM

**[11:52]** correct. Um, they also have a custom LLM

**[11:52]** correct. Um, they also have a custom LLM that would judge by the score and tone.

**[11:54]** that would judge by the score and tone.

**[11:54]** that would judge by the score and tone. So, it will panalyze verbosity, emojis

**[11:57]** So, it will panalyze verbosity, emojis

**[11:57]** So, it will panalyze verbosity, emojis or anything that feels unprofessional.

**[11:59]** or anything that feels unprofessional.

**[11:59]** or anything that feels unprofessional. Finally, the grader will reward the


### [12:00 - 13:00]

**[12:01]** Finally, the grader will reward the

**[12:01]** Finally, the grader will reward the agents that validate their own work. So,

**[12:04]** agents that validate their own work. So,

**[12:04]** agents that validate their own work. So, this means running tests, inspecting

**[12:06]** this means running tests, inspecting

**[12:06]** this means running tests, inspecting terminal outputs, and also checking

**[12:08]** terminal outputs, and also checking

**[12:08]** terminal outputs, and also checking linting before calling out a success.

**[12:12]** linting before calling out a success.

**[12:12]** linting before calling out a success. And after training with this very

**[12:15]** And after training with this very

**[12:15]** And after training with this very thoughtful set of tools and graders,

**[12:17]** thoughtful set of tools and graders,

**[12:17]** thoughtful set of tools and graders, cosine was able to reach the

**[12:19]** cosine was able to reach the

**[12:19]** cosine was able to reach the state-of-the-art on a lot of different

**[12:22]** state-of-the-art on a lot of different

**[12:22]** state-of-the-art on a lot of different benchmarks over here. And they also got

**[12:25]** benchmarks over here. And they also got

**[12:25]** benchmarks over here. And they also got a much much faster agent. So like in

**[12:28]** a much much faster agent. So like in

**[12:28]** a much much faster agent. So like in earlier examples, RFT shifted this

**[12:31]** earlier examples, RFT shifted this

**[12:31]** earlier examples, RFT shifted this distribution of tool calls and the agent

**[12:32]** distribution of tool calls and the agent

**[12:32]** distribution of tool calls and the agent stopped taking these extremely long

**[12:35]** stopped taking these extremely long

**[12:35]** stopped taking these extremely long trajectories. In this case, there were

**[12:36]** trajectories. In this case, there were

**[12:36]** trajectories. In this case, there were sometimes more than a 100 messages in a

**[12:39]** sometimes more than a 100 messages in a

**[12:39]** sometimes more than a 100 messages in a single trajectory and it converged to a

**[12:41]** single trajectory and it converged to a

**[12:41]** single trajectory and it converged to a much tighter and more efficient sequence

**[12:44]** much tighter and more efficient sequence

**[12:44]** much tighter and more efficient sequence of steps.

**[12:46]** of steps.

**[12:46]** of steps. Lastly, Macco is a very interesting use

**[12:49]** Lastly, Macco is a very interesting use

**[12:49]** Lastly, Macco is a very interesting use case. They're building agents that write

**[12:51]** case. They're building agents that write

**[12:51]** case. They're building agents that write high highly performant GPU kernels which

**[12:54]** high highly performant GPU kernels which

**[12:54]** high highly performant GPU kernels which is traditionally very hard for LMS

**[12:57]** is traditionally very hard for LMS

**[12:57]** is traditionally very hard for LMS because in normal use cases there's a


### [13:00 - 14:00]

**[13:00]** because in normal use cases there's a

**[13:00]** because in normal use cases there's a lot more examples but in this case

**[13:01]** lot more examples but in this case

**[13:01]** lot more examples but in this case there's not a lot of example for kernels

**[13:04]** there's not a lot of example for kernels

**[13:04]** there's not a lot of example for kernels especially if you're using new hardware

**[13:07]** especially if you're using new hardware

**[13:07]** especially if you're using new hardware platforms like Nvidia B200's with Asian

**[13:10]** platforms like Nvidia B200's with Asian

**[13:10]** platforms like Nvidia B200's with Asian RFT macro trained GBD5 to write fast

**[13:13]** RFT macro trained GBD5 to write fast

**[13:13]** RFT macro trained GBD5 to write fast kernels using only about 100 PyTorch

**[13:16]** kernels using only about 100 PyTorch

**[13:16]** kernels using only about 100 PyTorch prompts and this was a major unlock. So

**[13:19]** prompts and this was a major unlock. So

**[13:19]** prompts and this was a major unlock. So we don't actually need that many samples

**[13:22]** we don't actually need that many samples

**[13:22]** we don't actually need that many samples and kernel data set in order to train a

**[13:25]** and kernel data set in order to train a

**[13:25]** and kernel data set in order to train a good model that produces kernels and we

**[13:28]** good model that produces kernels and we

**[13:28]** good model that produces kernels and we just have to specify a good reward

**[13:29]** just have to specify a good reward

**[13:30]** just have to specify a good reward function. In this case specifying a good

**[13:33]** function. In this case specifying a good

**[13:33]** function. In this case specifying a good reward function is also very hard. Early

**[13:36]** reward function is also very hard. Early

**[13:36]** reward function is also very hard. Early in training they observed that the model

**[13:38]** in training they observed that the model

**[13:38]** in training they observed that the model was reward hacking. So what they did was

**[13:41]** was reward hacking. So what they did was

**[13:41]** was reward hacking. So what they did was that they inspected the rollouts and

**[13:43]** that they inspected the rollouts and

**[13:44]** that they inspected the rollouts and they found seven different cases where

**[13:46]** they found seven different cases where

**[13:46]** they found seven different cases where the model was hacking and this include

**[13:48]** the model was hacking and this include

**[13:48]** the model was hacking and this include things like just uh returning the

**[13:50]** things like just uh returning the

**[13:50]** things like just uh returning the reference code or returning no kernels

**[13:53]** reference code or returning no kernels

**[13:53]** reference code or returning no kernels or identity kernels and they built a

**[13:56]** or identity kernels and they built a

**[13:56]** or identity kernels and they built a judge LM to catch all of these seven

**[13:58]** judge LM to catch all of these seven

**[13:58]** judge LM to catch all of these seven cases and reward them with a zero. They


### [14:00 - 15:00]

**[14:02]** cases and reward them with a zero. They

**[14:02]** cases and reward them with a zero. They also added a static analysis tool with a

**[14:05]** also added a static analysis tool with a

**[14:05]** also added a static analysis tool with a abstract syntax tree to verify that the

**[14:07]** abstract syntax tree to verify that the

**[14:07]** abstract syntax tree to verify that the generated kernels actually exist and

**[14:10]** generated kernels actually exist and

**[14:10]** generated kernels actually exist and they're actually being launched. So

**[14:12]** they're actually being launched. So

**[14:12]** they're actually being launched. So after the they made sure that there was

**[14:14]** after the they made sure that there was

**[14:14]** after the they made sure that there was no reward hacking, they also scored on

**[14:16]** no reward hacking, they also scored on

**[14:16]** no reward hacking, they also scored on correctness and real speed up compared

**[14:18]** correctness and real speed up compared

**[14:18]** correctness and real speed up compared to the partorch baseline.

**[14:21]** to the partorch baseline.

**[14:22]** to the partorch baseline. Once all of these protections were in

**[14:23]** Once all of these protections were in

**[14:23]** Once all of these protections were in place, the agent got significantly

**[14:25]** place, the agent got significantly

**[14:26]** place, the agent got significantly better than GPD5.

**[14:27]** better than GPD5.

**[14:28]** better than GPD5. And uh ML also used a really smart

**[14:31]** And uh ML also used a really smart

**[14:31]** And uh ML also used a really smart technique here to improve the

**[14:32]** technique here to improve the

**[14:32]** technique here to improve the performance even more. They ran three

**[14:34]** performance even more. They ran three

**[14:34]** performance even more. They ran three different samples and they took the best

**[14:36]** different samples and they took the best

**[14:36]** different samples and they took the best one out of the three. This allowed them

**[14:38]** one out of the three. This allowed them

**[14:38]** one out of the three. This allowed them to beat the state-of-the-art by 72%.

**[14:41]** to beat the state-of-the-art by 72%.

**[14:41]** to beat the state-of-the-art by 72%. And yeah, I'll hand it back to Will.

**[14:45]** And yeah, I'll hand it back to Will.

**[14:45]** And yeah, I'll hand it back to Will. >> Thanks a lot, Kathy. So, uh, now we want

**[14:47]** >> Thanks a lot, Kathy. So, uh, now we want

**[14:47]** >> Thanks a lot, Kathy. So, uh, now we want all of you, all of you in this room and

**[14:49]** all of you, all of you in this room and

**[14:49]** all of you, all of you in this room and beyond to be as successful as the

**[14:51]** beyond to be as successful as the

**[14:51]** beyond to be as successful as the partners that Kathy just mentioned with

**[14:53]** partners that Kathy just mentioned with

**[14:54]** partners that Kathy just mentioned with agent RFD. So, here are four key

**[14:55]** agent RFD. So, here are four key

**[14:55]** agent RFD. So, here are four key principles to ensure your success. First

**[14:57]** principles to ensure your success. First

**[14:57]** principles to ensure your success. First of all, you want to make sure that your

**[14:59]** of all, you want to make sure that your

**[14:59]** of all, you want to make sure that your task is well defined, well constrained.


### [15:00 - 16:00]

**[15:01]** task is well defined, well constrained.

**[15:01]** task is well defined, well constrained. There should be a clear, unambiguous

**[15:03]** There should be a clear, unambiguous

**[15:04]** There should be a clear, unambiguous definition of success. You should have

**[15:05]** definition of success. You should have

**[15:05]** definition of success. You should have removed all subjectivity out of your

**[15:07]** removed all subjectivity out of your

**[15:07]** removed all subjectivity out of your task. Taste should not be a requirement

**[15:09]** task. Taste should not be a requirement

**[15:09]** task. Taste should not be a requirement to grade your task properly. Next, you

**[15:12]** to grade your task properly. Next, you

**[15:12]** to grade your task properly. Next, you do not want the model to feel surprised

**[15:14]** do not want the model to feel surprised

**[15:14]** do not want the model to feel surprised in production. You want to make sure

**[15:15]** in production. You want to make sure

**[15:16]** in production. You want to make sure that your train and eval data sets

**[15:17]** that your train and eval data sets

**[15:17]** that your train and eval data sets mirror your production traffic. So, no

**[15:20]** mirror your production traffic. So, no

**[15:20]** mirror your production traffic. So, no none of that domain shift that we talked

**[15:21]** none of that domain shift that we talked

**[15:21]** none of that domain shift that we talked about. You do not want to introduce that

**[15:23]** about. You do not want to introduce that

**[15:23]** about. You do not want to introduce that domain shift on your own. Um, next, and

**[15:26]** domain shift on your own. Um, next, and

**[15:26]** domain shift on your own. Um, next, and this is a really important part, you

**[15:28]** this is a really important part, you

**[15:28]** this is a really important part, you want to make sure that through

**[15:29]** want to make sure that through

**[15:30]** want to make sure that through exploration, the model actually achieves

**[15:32]** exploration, the model actually achieves

**[15:32]** exploration, the model actually achieves better performance on a given data point

**[15:34]** better performance on a given data point

**[15:34]** better performance on a given data point if it samples more so that it can learn

**[15:36]** if it samples more so that it can learn

**[15:36]** if it samples more so that it can learn from itself. So what this means is if

**[15:37]** from itself. So what this means is if

**[15:38]** from itself. So what this means is if you take the maximum performance on a

**[15:39]** you take the maximum performance on a

**[15:39]** you take the maximum performance on a given data set, that should improve as

**[15:41]** given data set, that should improve as

**[15:42]** given data set, that should improve as you sample more from the model. So

**[15:44]** you sample more from the model. So

**[15:44]** you sample more from the model. So because of this, you should be able to

**[15:45]** because of this, you should be able to

**[15:45]** because of this, you should be able to see the these variances from a given

**[15:48]** see the these variances from a given

**[15:48]** see the these variances from a given data point. So the model can learn from

**[15:49]** data point. So the model can learn from

**[15:49]** data point. So the model can learn from itself, learn what the difference

**[15:51]** itself, learn what the difference

**[15:51]** itself, learn what the difference between a good and a bad rollout is for

**[15:53]** between a good and a bad rollout is for

**[15:53]** between a good and a bad rollout is for a given data point.

**[15:54]** a given data point.

**[15:54]** a given data point. And uh lastly, you want to make sure

**[15:56]** And uh lastly, you want to make sure

**[15:56]** And uh lastly, you want to make sure that your reward function is not

**[15:58]** that your reward function is not

**[15:58]** that your reward function is not hackable. Hopefully you've plugged up


### [16:00 - 17:00]

**[16:00]** hackable. Hopefully you've plugged up

**[16:00]** hackable. Hopefully you've plugged up all the corner cases, all the edge

**[16:01]** all the corner cases, all the edge

**[16:01]** all the corner cases, all the edge cases. Um but also hopefully you've

**[16:04]** cases. Um but also hopefully you've

**[16:04]** cases. Um but also hopefully you've framed your task so that the reward is

**[16:07]** framed your task so that the reward is

**[16:07]** framed your task so that the reward is more continuous than binary. The

**[16:09]** more continuous than binary. The

**[16:09]** more continuous than binary. The continuous reward actually allows the

**[16:11]** continuous reward actually allows the

**[16:11]** continuous reward actually allows the model to kind of inch up closer and

**[16:13]** model to kind of inch up closer and

**[16:13]** model to kind of inch up closer and closer to optimal performance. Sort of

**[16:15]** closer to optimal performance. Sort of

**[16:15]** closer to optimal performance. Sort of like giving giving a student partial

**[16:17]** like giving giving a student partial

**[16:17]** like giving giving a student partial credit. um rather than you know slapping

**[16:20]** credit. um rather than you know slapping

**[16:20]** credit. um rather than you know slapping them all in the face or giving it a

**[16:21]** them all in the face or giving it a

**[16:21]** them all in the face or giving it a cookie uh if it gets stuff wrong or gets

**[16:23]** cookie uh if it gets stuff wrong or gets

**[16:23]** cookie uh if it gets stuff wrong or gets stuff right. So now in order to get

**[16:26]** stuff right. So now in order to get

**[16:26]** stuff right. So now in order to get started with agent RFT, please contact

**[16:28]** started with agent RFT, please contact

**[16:28]** started with agent RFT, please contact your friendly neighborhood account

**[16:29]** your friendly neighborhood account

**[16:29]** your friendly neighborhood account director and we're really excited to see

**[16:31]** director and we're really excited to see

**[16:31]** director and we're really excited to see what you all build with us. Thank you so

**[16:33]** what you all build with us. Thank you so

**[16:33]** what you all build with us. Thank you so much. [applause]


