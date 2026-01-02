# From Stateless Nightmares to Durable Agents — Samuel Colvin, Pydantic

**Video URL:** https://www.youtube.com/watch?v=flf_IKnFYnE

---

## Full Transcript

### [00:00 - 01:00]

**[00:03]** Hi, I'm Samuel from Pantic and today I'm

**[00:03]** Hi, I'm Samuel from Pantic and today I'm going to give a demo of Pyantic AI

**[00:05]** going to give a demo of Pyantic AI

**[00:05]** going to give a demo of Pyantic AI temporal and Pantic logfire. I'll also

**[00:08]** temporal and Pantic logfire. I'll also

**[00:08]** temporal and Pantic logfire. I'll also cover Pyantic evals. So we have in

**[00:12]** cover Pyantic evals. So we have in

**[00:12]** cover Pyantic evals. So we have in Pantic AI support for temporal and

**[00:14]** Pantic AI support for temporal and

**[00:14]** Pantic AI support for temporal and deboss to durable execution frameworks.

**[00:16]** deboss to durable execution frameworks.

**[00:16]** deboss to durable execution frameworks. We're actually adding a bunch more. I

**[00:18]** We're actually adding a bunch more. I

**[00:18]** We're actually adding a bunch more. I think we've had something like five pull

**[00:19]** think we've had something like five pull

**[00:19]** think we've had something like five pull requests to add other durable execution

**[00:22]** requests to add other durable execution

**[00:22]** requests to add other durable execution or like workflow orchestration backends.

**[00:25]** or like workflow orchestration backends.

**[00:25]** or like workflow orchestration backends. But at the moment it's it's these two.

**[00:26]** But at the moment it's it's these two.

**[00:26]** But at the moment it's it's these two. And I think it's fair to say temporal

**[00:27]** And I think it's fair to say temporal

**[00:27]** And I think it's fair to say temporal are like the big incumbent in this space

**[00:30]** are like the big incumbent in this space

**[00:30]** are like the big incumbent in this space and they're they're kind of I guess

**[00:32]** and they're they're kind of I guess

**[00:32]** and they're they're kind of I guess leaders leaders in how you do this to to

**[00:34]** leaders leaders in how you do this to to

**[00:34]** leaders leaders in how you do this to to demonstrate this a simple example of

**[00:36]** demonstrate this a simple example of

**[00:36]** demonstrate this a simple example of like I go ask an LLM question it replies

**[00:40]** like I go ask an LLM question it replies

**[00:40]** like I go ask an LLM question it replies mostly just works and we don't need the

**[00:41]** mostly just works and we don't need the

**[00:41]** mostly just works and we don't need the durable execution component. So, but

**[00:43]** durable execution component. So, but

**[00:43]** durable execution component. So, but once we get into longer running

**[00:45]** once we get into longer running

**[00:45]** once we get into longer running workflows, that's where it really

**[00:47]** workflows, that's where it really

**[00:47]** workflows, that's where it really becomes a problem. In particular, where

**[00:49]** becomes a problem. In particular, where

**[00:49]** becomes a problem. In particular, where we've done enough compute that we don't

**[00:50]** we've done enough compute that we don't

**[00:50]** we've done enough compute that we don't want to lose it or we've spent enough

**[00:53]** want to lose it or we've spent enough

**[00:53]** want to lose it or we've spent enough time on that compute that we really

**[00:54]** time on that compute that we really

**[00:54]** time on that compute that we really don't want to have to start again for

**[00:55]** don't want to have to start again for

**[00:55]** don't want to have to start again for the user. That's what for example I

**[00:58]** the user. That's what for example I

**[00:58]** the user. That's what for example I think OpenAI it's I think it's public


### [01:00 - 02:00]

**[01:00]** think OpenAI it's I think it's public

**[01:00]** think OpenAI it's I think it's public that OpenAI use temporal for their um

**[01:02]** that OpenAI use temporal for their um

**[01:02]** that OpenAI use temporal for their um deep research and I think some of the

**[01:04]** deep research and I think some of the

**[01:04]** deep research and I think some of the other LLM deep research do the same

**[01:06]** other LLM deep research do the same

**[01:06]** other LLM deep research do the same thing. So, I'll I'll start with a kind

**[01:08]** thing. So, I'll I'll start with a kind

**[01:08]** thing. So, I'll I'll start with a kind of toy example and then I'll move on to

**[01:09]** of toy example and then I'll move on to

**[01:09]** of toy example and then I'll move on to a more deep research type example. in

**[01:12]** a more deep research type example. in

**[01:12]** a more deep research type example. in fact a deep research example. But before

**[01:13]** fact a deep research example. But before

**[01:13]** fact a deep research example. But before we get into that, let me let me run this

**[01:15]** we get into that, let me let me run this

**[01:15]** we get into that, let me let me run this example without. So this is a uh two

**[01:18]** example without. So this is a uh two

**[01:18]** example without. So this is a uh two agents that play um 20 questions. Um so

**[01:22]** agents that play um 20 questions. Um so

**[01:22]** agents that play um 20 questions. Um so instead of just a yes no answer, they

**[01:23]** instead of just a yes no answer, they

**[01:23]** instead of just a yes no answer, they get to give a little bit more detail

**[01:25]** get to give a little bit more detail

**[01:25]** get to give a little bit more detail like yes, kind of not really, no,

**[01:27]** like yes, kind of not really, no,

**[01:27]** like yes, kind of not really, no, completely wrong. Um that was because I

**[01:29]** completely wrong. Um that was because I

**[01:29]** completely wrong. Um that was because I was getting bored of waiting for them to

**[01:30]** was getting bored of waiting for them to

**[01:30]** was getting bored of waiting for them to take ages to succeed on the with the

**[01:32]** take ages to succeed on the with the

**[01:32]** take ages to succeed on the with the just the yes no. So, we have an answer

**[01:35]** just the yes no. So, we have an answer

**[01:35]** just the yes no. So, we have an answer agent which is runs a relatively small

**[01:37]** agent which is runs a relatively small

**[01:37]** agent which is runs a relatively small model Hiku 3.5 because I didn't know 4.5

**[01:39]** model Hiku 3.5 because I didn't know 4.5

**[01:39]** model Hiku 3.5 because I didn't know 4.5 came out until about an hour ago. And

**[01:41]** came out until about an hour ago. And

**[01:41]** came out until about an hour ago. And and this basically takes a question and

**[01:43]** and this basically takes a question and

**[01:43]** and this basically takes a question and answers yes well with with one of these

**[01:45]** answers yes well with with one of these

**[01:45]** answers yes well with with one of these answers and it it gets added into its

**[01:48]** answers and it it gets added into its

**[01:48]** answers and it it gets added into its context the the like secret object that

**[01:49]** context the the like secret object that

**[01:49]** context the the like secret object that you're looking for um which in this

**[01:51]** you're looking for um which in this

**[01:51]** you're looking for um which in this example is a potato. So, and then we

**[01:54]** example is a potato. So, and then we

**[01:54]** example is a potato. So, and then we have the um questioner agent or the

**[01:57]** have the um questioner agent or the

**[01:57]** have the um questioner agent or the player agent has a bit more context on

**[01:59]** player agent has a bit more context on


### [02:00 - 03:00]

**[02:00]** player agent has a bit more context on what it's going to go and do. You don't

**[02:01]** what it's going to go and do. You don't

**[02:01]** what it's going to go and do. You don't need to read read through all of this

**[02:02]** need to read read through all of this

**[02:02]** need to read read through all of this stuff. This code is is public now. It's

**[02:05]** stuff. This code is is public now. It's

**[02:05]** stuff. This code is is public now. It's a pull request, but I'll I'll merge that

**[02:06]** a pull request, but I'll I'll merge that

**[02:06]** a pull request, but I'll I'll merge that afterwards, but you should get the idea.

**[02:08]** afterwards, but you should get the idea.

**[02:08]** afterwards, but you should get the idea. Um, and the way that the questioner

**[02:11]** Um, and the way that the questioner

**[02:12]** Um, and the way that the questioner agent gets to ask its questions is by

**[02:15]** agent gets to ask its questions is by

**[02:15]** agent gets to ask its questions is by calling a tool, ask a question. Inside

**[02:17]** calling a tool, ask a question. Inside

**[02:17]** calling a tool, ask a question. Inside that tool, we run the other agent, the

**[02:20]** that tool, we run the other agent, the

**[02:20]** that tool, we run the other agent, the answer agent to basically decide the

**[02:22]** answer agent to basically decide the

**[02:22]** answer agent to basically decide the answer to this question, and then we

**[02:24]** answer to this question, and then we

**[02:24]** answer to this question, and then we respond. And it takes a little bit of

**[02:26]** respond. And it takes a little bit of

**[02:26]** respond. And it takes a little bit of time to run. You can see in this case,

**[02:27]** time to run. You can see in this case,

**[02:27]** time to run. You can see in this case, it succeeded pretty quickly. Sometimes

**[02:30]** it succeeded pretty quickly. Sometimes

**[02:30]** it succeeded pretty quickly. Sometimes it it's amazing how even these very

**[02:32]** it it's amazing how even these very

**[02:32]** it it's amazing how even these very simple questions, even very intelligent

**[02:34]** simple questions, even very intelligent

**[02:34]** simple questions, even very intelligent LLMs get themselves completely confused

**[02:36]** LLMs get themselves completely confused

**[02:36]** LLMs get themselves completely confused and go down some weird track and and

**[02:38]** and go down some weird track and and

**[02:38]** and go down some weird track and and like get very confused. But you can see

**[02:40]** like get very confused. But you can see

**[02:40]** like get very confused. But you can see in the last run that it asked a bunch of

**[02:42]** in the last run that it asked a bunch of

**[02:42]** in the last run that it asked a bunch of questions, got down to like is this a

**[02:45]** questions, got down to like is this a

**[02:45]** questions, got down to like is this a fruit or vegetable? Is it a fruit? No.

**[02:47]** fruit or vegetable? Is it a fruit? No.

**[02:47]** fruit or vegetable? Is it a fruit? No. So it knew it was a vegetable, is it

**[02:49]** So it knew it was a vegetable, is it

**[02:49]** So it knew it was a vegetable, is it orange? And it worked out the answer was

**[02:51]** orange? And it worked out the answer was

**[02:51]** orange? And it worked out the answer was was potato. But obviously and here it is

**[02:53]** was potato. But obviously and here it is

**[02:53]** was potato. But obviously and here it is running again. I don't know how many

**[02:55]** running again. I don't know how many

**[02:55]** running again. I don't know how many steps it's going to take. Sometimes it

**[02:56]** steps it's going to take. Sometimes it

**[02:56]** steps it's going to take. Sometimes it can take up to like 50 steps to get this

**[02:59]** can take up to like 50 steps to get this

**[02:59]** can take up to like 50 steps to get this question right. And obviously the


### [03:00 - 04:00]

**[03:00]** question right. And obviously the

**[03:00]** question right. And obviously the problem is if this dies either because

**[03:03]** problem is if this dies either because

**[03:03]** problem is if this dies either because we have some unreliable uh endpoint

**[03:07]** we have some unreliable uh endpoint

**[03:07]** we have some unreliable uh endpoint within our system or because we're

**[03:09]** within our system or because we're

**[03:09]** within our system or because we're running in the cloud and Kubernetes

**[03:11]** running in the cloud and Kubernetes

**[03:11]** running in the cloud and Kubernetes decides it wants to scale or whatever it

**[03:13]** decides it wants to scale or whatever it

**[03:13]** decides it wants to scale or whatever it might be. If we run this again, we

**[03:15]** might be. If we run this again, we

**[03:15]** might be. If we run this again, we obviously have to start from scratch.

**[03:17]** obviously have to start from scratch.

**[03:17]** obviously have to start from scratch. That is problematic in this case. Um but

**[03:20]** That is problematic in this case. Um but

**[03:20]** That is problematic in this case. Um but you can imagine as the tasks get longer

**[03:22]** you can imagine as the tasks get longer

**[03:22]** you can imagine as the tasks get longer and longer just restarting it gets more

**[03:24]** and longer just restarting it gets more

**[03:24]** and longer just restarting it gets more and more problematic. So um I think the

**[03:27]** and more problematic. So um I think the

**[03:27]** and more problematic. So um I think the other thing to say about this this like

**[03:30]** other thing to say about this this like

**[03:30]** other thing to say about this this like um 20 questions example is although it's

**[03:32]** um 20 questions example is although it's

**[03:32]** um 20 questions example is although it's pretty simple to understand and it feels

**[03:34]** pretty simple to understand and it feels

**[03:34]** pretty simple to understand and it feels like a toy, it is actually directly

**[03:36]** like a toy, it is actually directly

**[03:36]** like a toy, it is actually directly equivalent to a deep research case where

**[03:38]** equivalent to a deep research case where

**[03:38]** equivalent to a deep research case where effectively the agent is is like going

**[03:41]** effectively the agent is is like going

**[03:41]** effectively the agent is is like going off on a quest to go and find an answer

**[03:43]** off on a quest to go and find an answer

**[03:43]** off on a quest to go and find an answer to a question where it needs to ask the

**[03:45]** to a question where it needs to ask the

**[03:45]** to a question where it needs to ask the like you know troll at the bottom of the

**[03:48]** like you know troll at the bottom of the

**[03:48]** like you know troll at the bottom of the garden the other the like question to

**[03:50]** garden the other the like question to

**[03:50]** garden the other the like question to the next riddle to get to the next

**[03:51]** the next riddle to get to the next

**[03:52]** the next riddle to get to the next endpoint, right? like deep research is

**[03:53]** endpoint, right? like deep research is

**[03:53]** endpoint, right? like deep research is effectively this 20 questions just with

**[03:56]** effectively this 20 questions just with

**[03:56]** effectively this 20 questions just with like web like web search or rag or

**[03:59]** like web like web search or rag or

**[03:59]** like web like web search or rag or whatever it might be is your


### [04:00 - 05:00]

**[04:00]** whatever it might be is your

**[04:00]** whatever it might be is your intermediate steps. So let's turn that

**[04:03]** intermediate steps. So let's turn that

**[04:03]** intermediate steps. So let's turn that 20 questions into a durable agent. Um

**[04:07]** 20 questions into a durable agent. Um

**[04:07]** 20 questions into a durable agent. Um so this is mostly the same code for

**[04:09]** so this is mostly the same code for

**[04:09]** so this is mostly the same code for simplicity. I've actually copied it here

**[04:10]** simplicity. I've actually copied it here

**[04:10]** simplicity. I've actually copied it here but you see we have our answer agent. We

**[04:13]** but you see we have our answer agent. We

**[04:13]** but you see we have our answer agent. We need to wrap it in this temporal agent

**[04:15]** need to wrap it in this temporal agent

**[04:15]** need to wrap it in this temporal agent which gives us another thing that

**[04:16]** which gives us another thing that

**[04:16]** which gives us another thing that behaves like an agent like a pantic AI

**[04:19]** behaves like an agent like a pantic AI

**[04:19]** behaves like an agent like a pantic AI agent. So it's also a subclass of

**[04:20]** agent. So it's also a subclass of

**[04:20]** agent. So it's also a subclass of abstract agent. We do the same with our

**[04:23]** abstract agent. We do the same with our

**[04:23]** abstract agent. We do the same with our questionnaire agent. To keep things

**[04:25]** questionnaire agent. To keep things

**[04:25]** questionnaire agent. To keep things simple, we aren't doing the same um

**[04:27]** simple, we aren't doing the same um

**[04:27]** simple, we aren't doing the same um stuff about passing around the answer in

**[04:30]** stuff about passing around the answer in

**[04:30]** stuff about passing around the answer in context. We've just hardcoded the answer

**[04:32]** context. We've just hardcoded the answer

**[04:32]** context. We've just hardcoded the answer into the system prompt here for the for

**[04:34]** into the system prompt here for the for

**[04:34]** into the system prompt here for the for the answer agent. But apart from these

**[04:37]** the answer agent. But apart from these

**[04:37]** the answer agent. But apart from these like adding the temporal wrappers, you

**[04:39]** like adding the temporal wrappers, you

**[04:39]** like adding the temporal wrappers, you can as I will show later just um apply

**[04:42]** can as I will show later just um apply

**[04:42]** can as I will show later just um apply durable execution later. But here's

**[04:44]** durable execution later. But here's

**[04:44]** durable execution later. But here's where the the temporal bit comes in. And

**[04:47]** where the the temporal bit comes in. And

**[04:47]** where the the temporal bit comes in. And I'm not a salesperson for temporal. And

**[04:48]** I'm not a salesperson for temporal. And

**[04:48]** I'm not a salesperson for temporal. And although the underlying stuff they do is

**[04:50]** although the underlying stuff they do is

**[04:50]** although the underlying stuff they do is amazing, I do think some of their Python

**[04:52]** amazing, I do think some of their Python

**[04:52]** amazing, I do think some of their Python abstractions are kind of ugly. But

**[04:54]** abstractions are kind of ugly. But

**[04:54]** abstractions are kind of ugly. But anyway, the the principle of temporal is

**[04:56]** anyway, the the principle of temporal is

**[04:56]** anyway, the the principle of temporal is that you have workflows and activities.


### [05:00 - 06:00]

**[05:00]** that you have workflows and activities.

**[05:00]** that you have workflows and activities. And workflows need to be entirely

**[05:02]** And workflows need to be entirely

**[05:02]** And workflows need to be entirely deterministic and activities then need

**[05:05]** deterministic and activities then need

**[05:05]** deterministic and activities then need to do anything that is non-deterministic

**[05:08]** to do anything that is non-deterministic

**[05:08]** to do anything that is non-deterministic like IO in particular. So you can

**[05:10]** like IO in particular. So you can

**[05:10]** like IO in particular. So you can basically do anything inside a workflow

**[05:11]** basically do anything inside a workflow

**[05:11]** basically do anything inside a workflow other than IO and calling random. And if

**[05:14]** other than IO and calling random. And if

**[05:14]** other than IO and calling random. And if you're if if that's the case, then you

**[05:15]** you're if if that's the case, then you

**[05:15]** you're if if that's the case, then you have a deterministic system. And what

**[05:19]** have a deterministic system. And what

**[05:19]** have a deterministic system. And what you can think of what temporal is doing

**[05:20]** you can think of what temporal is doing

**[05:20]** you can think of what temporal is doing in the background as it's running that

**[05:23]** in the background as it's running that

**[05:23]** in the background as it's running that workflow and it's basically recording

**[05:25]** workflow and it's basically recording

**[05:25]** workflow and it's basically recording the every activity that runs and both

**[05:28]** the every activity that runs and both

**[05:28]** the every activity that runs and both the the inputs to that and the outputs.

**[05:29]** the the inputs to that and the outputs.

**[05:30]** the the inputs to that and the outputs. And so if you want to rerun it from like

**[05:33]** And so if you want to rerun it from like

**[05:33]** And so if you want to rerun it from like from the beginning to a certain point,

**[05:34]** from the beginning to a certain point,

**[05:34]** from the beginning to a certain point, it can basically plug in those answers.

**[05:36]** it can basically plug in those answers.

**[05:36]** it can basically plug in those answers. And I'll show what that looks like. So

**[05:38]** And I'll show what that looks like. So

**[05:38]** And I'll show what that looks like. So this is how we define our workflow. The

**[05:40]** this is how we define our workflow. The

**[05:40]** this is how we define our workflow. The activities here are implicit. The point

**[05:42]** activities here are implicit. The point

**[05:42]** activities here are implicit. The point is that this temporal agent takes care

**[05:45]** is that this temporal agent takes care

**[05:45]** is that this temporal agent takes care of turning all of the IO that you need

**[05:48]** of turning all of the IO that you need

**[05:48]** of turning all of the IO that you need to do to call an LLM into activities in

**[05:50]** to do to call an LLM into activities in

**[05:50]** to do to call an LLM into activities in the background, including tool calls.

**[05:52]** the background, including tool calls.

**[05:52]** the background, including tool calls. So, OpenAI claim to have temporal

**[05:54]** So, OpenAI claim to have temporal

**[05:54]** So, OpenAI claim to have temporal support, but they don't support tool

**[05:56]** support, but they don't support tool

**[05:56]** support, but they don't support tool calls as activities, which to me makes

**[05:58]** calls as activities, which to me makes

**[05:58]** calls as activities, which to me makes it slightly a chocolate teapot. Like,


### [06:00 - 07:00]

**[06:00]** it slightly a chocolate teapot. Like,

**[06:00]** it slightly a chocolate teapot. Like, there's actually no point in having any

**[06:01]** there's actually no point in having any

**[06:01]** there's actually no point in having any of these things without without tool

**[06:03]** of these things without without tool

**[06:03]** of these things without without tool calling or little little point. But we

**[06:05]** calling or little little point. But we

**[06:05]** calling or little little point. But we define our workflow like this. I think

**[06:08]** define our workflow like this. I think

**[06:08]** define our workflow like this. I think you can for the most part just copy

**[06:09]** you can for the most part just copy

**[06:09]** you can for the most part just copy paste their their definitions of how to

**[06:11]** paste their their definitions of how to

**[06:11]** paste their their definitions of how to do it. Here we have our play mechanism.

**[06:13]** do it. Here we have our play mechanism.

**[06:14]** do it. Here we have our play mechanism. The point here is we're going to we're

**[06:15]** The point here is we're going to we're

**[06:15]** The point here is we're going to we're going to connect to the temporal server

**[06:17]** going to connect to the temporal server

**[06:17]** going to connect to the temporal server which is what's going to record the

**[06:19]** which is what's going to record the

**[06:19]** which is what's going to record the state of our task or our agent as it's

**[06:22]** state of our task or our agent as it's

**[06:22]** state of our task or our agent as it's executing and be able to resume and

**[06:23]** executing and be able to resume and

**[06:23]** executing and be able to resume and stuff. I have temporal running locally

**[06:26]** stuff. I have temporal running locally

**[06:26]** stuff. I have temporal running locally here. This is just the open source

**[06:27]** here. This is just the open source

**[06:27]** here. This is just the open source version of temporal which runs as a

**[06:29]** version of temporal which runs as a

**[06:29]** version of temporal which runs as a separate process and I can restart that

**[06:31]** separate process and I can restart that

**[06:31]** separate process and I can restart that to kind of kill the state and that's why

**[06:33]** to kind of kill the state and that's why

**[06:33]** to kind of kill the state and that's why we're connecting to local host. In

**[06:35]** we're connecting to local host. In

**[06:35]** we're connecting to local host. In production you use temporal's cloud.

**[06:37]** production you use temporal's cloud.

**[06:37]** production you use temporal's cloud. that's why they make so much money. Um,

**[06:39]** that's why they make so much money. Um,

**[06:39]** that's why they make so much money. Um, and here we we run the worker. This is

**[06:42]** and here we we run the worker. This is

**[06:42]** and here we we run the worker. This is where we're actually going to kick off

**[06:43]** where we're actually going to kick off

**[06:43]** where we're actually going to kick off our workflow. In general, we just kick

**[06:45]** our workflow. In general, we just kick

**[06:45]** our workflow. In general, we just kick off our workflow with execute workflow.

**[06:48]** off our workflow with execute workflow.

**[06:48]** off our workflow with execute workflow. We pl pass in the the workflow that we

**[06:50]** We pl pass in the the workflow that we

**[06:50]** We pl pass in the the workflow that we want to run. We pass the inputs. There

**[06:53]** want to run. We pass the inputs. There

**[06:53]** want to run. We pass the inputs. There aren't any inputs in this case because

**[06:54]** aren't any inputs in this case because

**[06:54]** aren't any inputs in this case because we just start. So, there aren't any

**[06:56]** we just start. So, there aren't any

**[06:56]** we just start. So, there aren't any here. And it will then go and run. And

**[06:58]** here. And it will then go and run. And

**[06:58]** here. And it will then go and run. And so, if I run this, we will you will see


### [07:00 - 08:00]

**[07:03]** so, if I run this, we will you will see

**[07:03]** so, if I run this, we will you will see it start to to execute.

**[07:06]** it start to to execute.

**[07:06]** it start to to execute. You'll see it running. The only couple

**[07:08]** You'll see it running. The only couple

**[07:08]** You'll see it running. The only couple of things to note, there's a couple of

**[07:09]** of things to note, there's a couple of

**[07:09]** of things to note, there's a couple of log messages. Ah, and we immediately

**[07:11]** log messages. Ah, and we immediately

**[07:12]** log messages. Ah, and we immediately have this exception broken. And that was

**[07:14]** have this exception broken. And that was

**[07:14]** have this exception broken. And that was because to simulate some system that's

**[07:17]** because to simulate some system that's

**[07:17]** because to simulate some system that's unreliable inside the tool I added 20%

**[07:20]** unreliable inside the tool I added 20%

**[07:20]** unreliable inside the tool I added 20% of the time it's going to it's going to

**[07:21]** of the time it's going to it's going to

**[07:21]** of the time it's going to it's going to break. What you will see is that

**[07:23]** break. What you will see is that

**[07:23]** break. What you will see is that temporal has immediately taken care of

**[07:25]** temporal has immediately taken care of

**[07:25]** temporal has immediately taken care of continuing after that. So even though

**[07:28]** continuing after that. So even though

**[07:28]** continuing after that. So even though this broke, it will continue to run. And

**[07:31]** this broke, it will continue to run. And

**[07:31]** this broke, it will continue to run. And I may have set 20% to be too high um

**[07:33]** I may have set 20% to be too high um

**[07:33]** I may have set 20% to be too high um because it's now failing all the time,

**[07:35]** because it's now failing all the time,

**[07:35]** because it's now failing all the time, but it's actually going to continue and

**[07:37]** but it's actually going to continue and

**[07:37]** but it's actually going to continue and deal with those runtime errors and just

**[07:38]** deal with those runtime errors and just

**[07:38]** deal with those runtime errors and just continue to operate absolutely fine. Let

**[07:41]** continue to operate absolutely fine. Let

**[07:41]** continue to operate absolutely fine. Let me However, I think I dialed up 20% too

**[07:43]** me However, I think I dialed up 20% too

**[07:43]** me However, I think I dialed up 20% too high just before. So, I'm going to

**[07:46]** high just before. So, I'm going to

**[07:46]** high just before. So, I'm going to actually see if this is going to

**[07:47]** actually see if this is going to

**[07:47]** actually see if this is going to continue to operate.

**[07:49]** continue to operate.

**[07:49]** continue to operate. Obviously, when you give a demo,

**[07:50]** Obviously, when you give a demo,

**[07:50]** Obviously, when you give a demo, everything suddenly grinds to a halt.

**[07:52]** everything suddenly grinds to a halt.

**[07:52]** everything suddenly grinds to a halt. Someone recently said they hate demos

**[07:53]** Someone recently said they hate demos

**[07:53]** Someone recently said they hate demos where everything goes to plan, and I

**[07:55]** where everything goes to plan, and I

**[07:55]** where everything goes to plan, and I said you'll never need to worry about

**[07:56]** said you'll never need to worry about

**[07:56]** said you'll never need to worry about that with me. Um, I don't know why that

**[07:59]** that with me. Um, I don't know why that

**[07:59]** that with me. Um, I don't know why that has actually ground to a complete halt.


### [08:00 - 09:00]

**[08:00]** has actually ground to a complete halt.

**[08:00]** has actually ground to a complete halt. I don't know whether that's it just

**[08:02]** I don't know whether that's it just

**[08:02]** I don't know whether that's it just repeatedly failing.

**[08:08]** Let me I'm going to kill temporal server

**[08:08]** Let me I'm going to kill temporal server here and restart it so that we don't

**[08:10]** here and restart it so that we don't

**[08:10]** here and restart it so that we don't have the state stored. And I will clear

**[08:13]** have the state stored. And I will clear

**[08:13]** have the state stored. And I will clear this and run it again. And you should

**[08:16]** this and run it again. And you should

**[08:16]** this and run it again. And you should now see it succeeding most of the time

**[08:17]** now see it succeeding most of the time

**[08:17]** now see it succeeding most of the time and failing 10% of the time. So yeah,

**[08:19]** and failing 10% of the time. So yeah,

**[08:19]** and failing 10% of the time. So yeah, you see it now asking questions and

**[08:22]** you see it now asking questions and

**[08:22]** you see it now asking questions and occasionally breaking. Good timing, but

**[08:24]** occasionally breaking. Good timing, but

**[08:24]** occasionally breaking. Good timing, but continuing. Um, so that's one of the

**[08:26]** continuing. Um, so that's one of the

**[08:26]** continuing. Um, so that's one of the things Temporal does. It just does the

**[08:28]** things Temporal does. It just does the

**[08:28]** things Temporal does. It just does the like retry logic that is like you could

**[08:31]** like retry logic that is like you could

**[08:31]** like retry logic that is like you could implement without temporal, but they do

**[08:32]** implement without temporal, but they do

**[08:32]** implement without temporal, but they do it very nicely. But there are more

**[08:34]** it very nicely. But there are more

**[08:34]** it very nicely. But there are more powerful things. So let's say this

**[08:35]** powerful things. So let's say this

**[08:35]** powerful things. So let's say this process that's in the middle of running

**[08:37]** process that's in the middle of running

**[08:37]** process that's in the middle of running gets killed by Kubernetes. Now, so we go

**[08:40]** gets killed by Kubernetes. Now, so we go

**[08:40]** gets killed by Kubernetes. Now, so we go across here and we we just like kill it.

**[08:42]** across here and we we just like kill it.

**[08:42]** across here and we we just like kill it. Process gets killed. Now, what I didn't

**[08:44]** Process gets killed. Now, what I didn't

**[08:44]** Process gets killed. Now, what I didn't show you is I also instrumented this

**[08:46]** show you is I also instrumented this

**[08:46]** show you is I also instrumented this with logfire. So if we look at our our

**[08:49]** with logfire. So if we look at our our

**[08:49]** with logfire. So if we look at our our workflow, we can see exactly what was

**[08:51]** workflow, we can see exactly what was

**[08:51]** workflow, we can see exactly what was going on here. Um, and we we can see

**[08:53]** going on here. Um, and we we can see

**[08:53]** going on here. Um, and we we can see what's going on here. So we have the

**[08:55]** what's going on here. So we have the

**[08:55]** what's going on here. So we have the different calls to claude and then

**[08:56]** different calls to claude and then

**[08:56]** different calls to claude and then inside that we have we're running the

**[08:58]** inside that we have we're running the

**[08:58]** inside that we have we're running the activity which is then running the um


### [09:00 - 10:00]

**[09:01]** activity which is then running the um

**[09:01]** activity which is then running the um other agent. But in particular if we

**[09:03]** other agent. But in particular if we

**[09:03]** other agent. But in particular if we come to the top level start for the

**[09:04]** come to the top level start for the

**[09:04]** come to the top level start for the workflow I can take the the workflow ID

**[09:07]** workflow I can take the the workflow ID

**[09:07]** workflow I can take the the workflow ID if we come back over to code here you'll

**[09:10]** if we come back over to code here you'll

**[09:10]** if we come back over to code here you'll see I had some some code in here to

**[09:12]** see I had some some code in here to

**[09:12]** see I had some some code in here to basically allow me to continue with a

**[09:13]** basically allow me to continue with a

**[09:13]** basically allow me to continue with a given uh resume ID and to continue a

**[09:16]** given uh resume ID and to continue a

**[09:16]** given uh resume ID and to continue a workflow. Now for the most part you

**[09:18]** workflow. Now for the most part you

**[09:18]** workflow. Now for the most part you wouldn't have to do this. This is just

**[09:19]** wouldn't have to do this. This is just

**[09:19]** wouldn't have to do this. This is just for the sake of the demo. If I just

**[09:21]** for the sake of the demo. If I just

**[09:21]** for the sake of the demo. If I just reran the script again, it would kick

**[09:23]** reran the script again, it would kick

**[09:23]** reran the script again, it would kick off this workflow again and it would run

**[09:24]** off this workflow again and it would run

**[09:24]** off this workflow again and it would run the two in parallel. That would look

**[09:26]** the two in parallel. That would look

**[09:26]** the two in parallel. That would look really confusing. So instead of doing

**[09:28]** really confusing. So instead of doing

**[09:28]** really confusing. So instead of doing that, I'm I'm specifically hanging on a

**[09:30]** that, I'm I'm specifically hanging on a

**[09:30]** that, I'm I'm specifically hanging on a particular workflow to finish. So you

**[09:32]** particular workflow to finish. So you

**[09:32]** particular workflow to finish. So you can see what's going on. So if I if I

**[09:35]** can see what's going on. So if I if I

**[09:35]** can see what's going on. So if I if I run my script again, but I give it the

**[09:37]** run my script again, but I give it the

**[09:37]** run my script again, but I give it the workflow that was ongoing. Now you see

**[09:40]** workflow that was ongoing. Now you see

**[09:40]** workflow that was ongoing. Now you see it's already whizzed forward to question

**[09:42]** it's already whizzed forward to question

**[09:42]** it's already whizzed forward to question six and it's continuing to operate. So,

**[09:44]** six and it's continuing to operate. So,

**[09:44]** six and it's continuing to operate. So, we've got it to basically resume without

**[09:46]** we've got it to basically resume without

**[09:46]** we've got it to basically resume without having to add any resume code anywhere

**[09:48]** having to add any resume code anywhere

**[09:48]** having to add any resume code anywhere in our actual agent code. We just set up

**[09:51]** in our actual agent code. We just set up

**[09:51]** in our actual agent code. We just set up temporal and it works. And you can see

**[09:53]** temporal and it works. And you can see

**[09:53]** temporal and it works. And you can see exactly what's happened if you um look

**[09:56]** exactly what's happened if you um look

**[09:56]** exactly what's happened if you um look at logfire. What you will see is that

**[09:58]** at logfire. What you will see is that

**[09:58]** at logfire. What you will see is that that whole that first bunch of um calls


### [10:00 - 11:00]

**[10:01]** that whole that first bunch of um calls

**[10:02]** that whole that first bunch of um calls to the LLM responded in like 5

**[10:04]** to the LLM responded in like 5

**[10:04]** to the LLM responded in like 5 milliseconds. So, these were not

**[10:05]** milliseconds. So, these were not

**[10:06]** milliseconds. So, these were not actually sent to the LLM. Temporal just

**[10:08]** actually sent to the LLM. Temporal just

**[10:08]** actually sent to the LLM. Temporal just returned the result, the kind of cached

**[10:10]** returned the result, the kind of cached

**[10:10]** returned the result, the kind of cached result that it already had for each of

**[10:11]** result that it already had for each of

**[10:11]** result that it already had for each of these cases. So we're able to

**[10:13]** these cases. So we're able to

**[10:13]** these cases. So we're able to effectively zoom forward to the point

**[10:16]** effectively zoom forward to the point

**[10:16]** effectively zoom forward to the point where it then continues to to call the

**[10:18]** where it then continues to to call the

**[10:18]** where it then continues to to call the LLM. It's it's as if you've gone through

**[10:20]** LLM. It's it's as if you've gone through

**[10:20]** LLM. It's it's as if you've gone through everywhere that you're doing IO and

**[10:22]** everywhere that you're doing IO and

**[10:22]** everywhere that you're doing IO and you've set up uh caching on each

**[10:24]** you've set up uh caching on each

**[10:24]** you've set up uh caching on each individual call so that you can run your

**[10:25]** individual call so that you can run your

**[10:26]** individual call so that you can run your code. Uh I see some people nodding which

**[10:28]** code. Uh I see some people nodding which

**[10:28]** code. Uh I see some people nodding which is making me feel a bit better about

**[10:29]** is making me feel a bit better about

**[10:29]** is making me feel a bit better about explaining this. But we don't have to do

**[10:31]** explaining this. But we don't have to do

**[10:31]** explaining this. But we don't have to do the inference. We don't have to wait the

**[10:32]** the inference. We don't have to wait the

**[10:32]** the inference. We don't have to wait the time. We can basically run our workflow

**[10:34]** time. We can basically run our workflow

**[10:34]** time. We can basically run our workflow code that's generally very fast because

**[10:36]** code that's generally very fast because

**[10:36]** code that's generally very fast because it's no IO. It's just procedural. and it

**[10:39]** it's no IO. It's just procedural. and it

**[10:39]** it's no IO. It's just procedural. and it will just keep getting results instantly

**[10:40]** will just keep getting results instantly

**[10:40]** will just keep getting results instantly until it gets to the point where it

**[10:41]** until it gets to the point where it

**[10:41]** until it gets to the point where it needs to needs to continue. And you see

**[10:44]** needs to needs to continue. And you see

**[10:44]** needs to needs to continue. And you see in this case, it's got itself completely

**[10:46]** in this case, it's got itself completely

**[10:46]** in this case, it's got itself completely confused and it's off um wondering about

**[10:48]** confused and it's off um wondering about

**[10:48]** confused and it's off um wondering about whether this thing is a salad bowl. So,

**[10:50]** whether this thing is a salad bowl. So,

**[10:50]** whether this thing is a salad bowl. So, you see how sometimes the LLM does well,

**[10:52]** you see how sometimes the LLM does well,

**[10:52]** you see how sometimes the LLM does well, sometimes it does does terribly. Um I'm

**[10:55]** sometimes it does does terribly. Um I'm

**[10:55]** sometimes it does does terribly. Um I'm going to actually I'll leave that

**[10:57]** going to actually I'll leave that

**[10:57]** going to actually I'll leave that running to see whether it you see it's

**[10:58]** running to see whether it you see it's

**[10:58]** running to see whether it you see it's it knows it's related to food, but it's


### [11:00 - 12:00]

**[11:00]** it knows it's related to food, but it's

**[11:00]** it knows it's related to food, but it's got itself really confused. Um I will

**[11:02]** got itself really confused. Um I will

**[11:02]** got itself really confused. Um I will just say as as it might interest you

**[11:05]** just say as as it might interest you

**[11:05]** just say as as it might interest you just before this I was wondering how the

**[11:07]** just before this I was wondering how the

**[11:07]** just before this I was wondering how the different models would perform and so I

**[11:10]** different models would perform and so I

**[11:10]** different models would perform and so I I ran some evals with padantic evals on

**[11:12]** I ran some evals with padantic evals on

**[11:12]** I ran some evals with padantic evals on these different cases and you can see

**[11:14]** these different cases and you can see

**[11:14]** these different cases and you can see here we have it's a bit hard to read on

**[11:16]** here we have it's a bit hard to read on

**[11:16]** here we have it's a bit hard to read on the screen but uh GPT 4.1 Gemini and

**[11:20]** the screen but uh GPT 4.1 Gemini and

**[11:20]** the screen but uh GPT 4.1 Gemini and Claude Sonnet 4.5 and you can see the

**[11:25]** Claude Sonnet 4.5 and you can see the

**[11:25]** Claude Sonnet 4.5 and you can see the different assertions for each case

**[11:27]** different assertions for each case

**[11:27]** different assertions for each case whether they passed or failed here and

**[11:29]** whether they passed or failed here and

**[11:29]** whether they passed or failed here and you can see the the average cost. You

**[11:32]** you can see the the average cost. You

**[11:32]** you can see the the average cost. You can see Gemini was way way cheaper, way

**[11:34]** can see Gemini was way way cheaper, way

**[11:34]** can see Gemini was way way cheaper, way way faster. And somewhere we should

**[11:37]** way faster. And somewhere we should

**[11:37]** way faster. And somewhere we should have, if we look at an individual case,

**[11:39]** have, if we look at an individual case,

**[11:39]** have, if we look at an individual case, we have a a metric for how many steps it

**[11:42]** we have a a metric for how many steps it

**[11:42]** we have a a metric for how many steps it took to succeed. I think maybe we have

**[11:43]** took to succeed. I think maybe we have

**[11:44]** took to succeed. I think maybe we have to scroll over. Yeah. Question count.

**[11:45]** to scroll over. Yeah. Question count.

**[11:45]** to scroll over. Yeah. Question count. You can see here Gemini was way quicker

**[11:48]** You can see here Gemini was way quicker

**[11:48]** You can see here Gemini was way quicker each time. I discovered subsequently

**[11:50]** each time. I discovered subsequently

**[11:50]** each time. I discovered subsequently having having checked the results that

**[11:52]** having having checked the results that

**[11:52]** having having checked the results that actually the reason Gemini is way faster

**[11:54]** actually the reason Gemini is way faster

**[11:54]** actually the reason Gemini is way faster and answers much more quickly is it just

**[11:56]** and answers much more quickly is it just

**[11:56]** and answers much more quickly is it just invents an answer that's wrong and I

**[11:57]** invents an answer that's wrong and I

**[11:57]** invents an answer that's wrong and I wasn't checking it. So, this is not

**[11:59]** wasn't checking it. So, this is not

**[11:59]** wasn't checking it. So, this is not perfect yet, but like it's uh the the EV


### [12:00 - 13:00]

**[12:02]** perfect yet, but like it's uh the the EV

**[12:02]** perfect yet, but like it's uh the the EV this is definitely an interesting case

**[12:03]** this is definitely an interesting case

**[12:03]** this is definitely an interesting case for evals and seeing and like working

**[12:05]** for evals and seeing and like working

**[12:05]** for evals and seeing and like working out which model is actually better

**[12:06]** out which model is actually better

**[12:06]** out which model is actually better because they're definitely not

**[12:07]** because they're definitely not

**[12:07]** because they're definitely not particularly good at it by default. But

**[12:09]** particularly good at it by default. But

**[12:09]** particularly good at it by default. But yeah, in my naive case, Gemini did way

**[12:11]** yeah, in my naive case, Gemini did way

**[12:11]** yeah, in my naive case, Gemini did way better, but that's not representative.

**[12:13]** better, but that's not representative.

**[12:13]** better, but that's not representative. Anyway, I'm going to leave that because

**[12:15]** Anyway, I'm going to leave that because

**[12:15]** Anyway, I'm going to leave that because it's got 46 steps in and it's still

**[12:17]** it's got 46 steps in and it's still

**[12:17]** it's got 46 steps in and it's still failing to work out that that thing's a

**[12:18]** failing to work out that that thing's a

**[12:18]** failing to work out that that thing's a potato. I I can show the evals case if

**[12:20]** potato. I I can show the evals case if

**[12:20]** potato. I I can show the evals case if you want, but I think it might be more

**[12:22]** you want, but I think it might be more

**[12:22]** you want, but I think it might be more interesting to look at a deep research

**[12:25]** interesting to look at a deep research

**[12:25]** interesting to look at a deep research case, which is a kind of more meaningful

**[12:27]** case, which is a kind of more meaningful

**[12:27]** case, which is a kind of more meaningful example of where you would run durable

**[12:29]** example of where you would run durable

**[12:29]** example of where you would run durable execution. Um, and also doing stuff in

**[12:31]** execution. Um, and also doing stuff in

**[12:31]** execution. Um, and also doing stuff in parallel, which is also one of the

**[12:33]** parallel, which is also one of the

**[12:33]** parallel, which is also one of the things that like just works out of the

**[12:34]** things that like just works out of the

**[12:34]** things that like just works out of the box with temporal without you having to

**[12:35]** box with temporal without you having to

**[12:36]** box with temporal without you having to write any any code. So, this is my very

**[12:39]** write any any code. So, this is my very

**[12:39]** write any any code. So, this is my very quick last night hours attempt at

**[12:41]** quick last night hours attempt at

**[12:41]** quick last night hours attempt at building deep research. I honestly think

**[12:43]** building deep research. I honestly think

**[12:43]** building deep research. I honestly think it's as good as lots of the actual deep

**[12:46]** it's as good as lots of the actual deep

**[12:46]** it's as good as lots of the actual deep research systems. So we have we define

**[12:48]** research systems. So we have we define

**[12:48]** research systems. So we have we define our plan for deep research and this is

**[12:52]** our plan for deep research and this is

**[12:52]** our plan for deep research and this is this is effectively our deep research

**[12:54]** this is effectively our deep research

**[12:54]** this is effectively our deep research plan. So it has an executive summary

**[12:56]** plan. So it has an executive summary

**[12:56]** plan. So it has an executive summary what you would effectively pump out to

**[12:57]** what you would effectively pump out to

**[12:57]** what you would effectively pump out to the user about what I'm going to go and

**[12:59]** the user about what I'm going to go and

**[12:59]** the user about what I'm going to go and do. Then we have a list of web search


### [13:00 - 14:00]

**[13:02]** do. Then we have a list of web search

**[13:02]** do. Then we have a list of web search steps. We maximum we have a maximum of

**[13:04]** steps. We maximum we have a maximum of

**[13:04]** steps. We maximum we have a maximum of five here so it doesn't take forever and

**[13:06]** five here so it doesn't take forever and

**[13:06]** five here so it doesn't take forever and then we have analysis instructions. And

**[13:09]** then we have analysis instructions. And

**[13:09]** then we have analysis instructions. And the point is that like I think this is

**[13:11]** the point is that like I think this is

**[13:11]** the point is that like I think this is one of the big change in AI this year

**[13:13]** one of the big change in AI this year

**[13:13]** one of the big change in AI this year answering a bit the question I had on

**[13:14]** answering a bit the question I had on

**[13:14]** answering a bit the question I had on the other zoom. I think we've moved from

**[13:16]** the other zoom. I think we've moved from

**[13:16]** the other zoom. I think we've moved from thinking that like agents in the sense

**[13:18]** thinking that like agents in the sense

**[13:18]** thinking that like agents in the sense of so there are three definitions of

**[13:20]** of so there are three definitions of

**[13:20]** of so there are three definitions of agents. There is the like AI definition

**[13:22]** agents. There is the like AI definition

**[13:22]** agents. There is the like AI definition which is LLM's calling tools in a loop.

**[13:25]** which is LLM's calling tools in a loop.

**[13:26]** which is LLM's calling tools in a loop. There is the tech definition which is a

**[13:28]** There is the tech definition which is a

**[13:28]** There is the tech definition which is a micros service and then there is the

**[13:30]** micros service and then there is the

**[13:30]** micros service and then there is the business definition which is something

**[13:32]** business definition which is something

**[13:32]** business definition which is something that can replace a human. Um ignoring

**[13:34]** that can replace a human. Um ignoring

**[13:34]** that can replace a human. Um ignoring the business definition for a minute. If

**[13:36]** the business definition for a minute. If

**[13:36]** the business definition for a minute. If you think about the AI and the like

**[13:37]** you think about the AI and the like

**[13:37]** you think about the AI and the like engineering definitions, we thought at

**[13:40]** engineering definitions, we thought at

**[13:40]** engineering definitions, we thought at the beginning of this year you would

**[13:41]** the beginning of this year you would

**[13:41]** the beginning of this year you would have one AI agent, one LLM calling tools

**[13:45]** have one AI agent, one LLM calling tools

**[13:45]** have one AI agent, one LLM calling tools in the loop within each microser. I

**[13:47]** in the loop within each microser. I

**[13:47]** in the loop within each microser. I think we've moved more and more to think

**[13:48]** think we've moved more and more to think

**[13:48]** think we've moved more and more to think that the agents are actually the kind of

**[13:51]** that the agents are actually the kind of

**[13:51]** that the agents are actually the kind of quantum of development. They are the the

**[13:53]** quantum of development. They are the the

**[13:53]** quantum of development. They are the the micro tasks that are doing that you

**[13:56]** micro tasks that are doing that you

**[13:56]** micro tasks that are doing that you build up to to form a like what most

**[13:58]** build up to to form a like what most

**[13:58]** build up to to form a like what most people would think of as an agent,

**[13:59]** people would think of as an agent,


### [14:00 - 15:00]

**[14:00]** people would think of as an agent, something that actually goes and

**[14:00]** something that actually goes and

**[14:00]** something that actually goes and autonomously completes a task. And so

**[14:03]** autonomously completes a task. And so

**[14:03]** autonomously completes a task. And so our deep research agent is actually made

**[14:04]** our deep research agent is actually made

**[14:04]** our deep research agent is actually made up of multiple agents. So we have this

**[14:07]** up of multiple agents. So we have this

**[14:07]** up of multiple agents. So we have this plan agent which goes off with a prompt

**[14:09]** plan agent which goes off with a prompt

**[14:09]** plan agent which goes off with a prompt and it returns an instance structured

**[14:11]** and it returns an instance structured

**[14:11]** and it returns an instance structured data extraction gives you an instance of

**[14:13]** data extraction gives you an instance of

**[14:13]** data extraction gives you an instance of this pyantic model which is your plan to

**[14:14]** this pyantic model which is your plan to

**[14:14]** this pyantic model which is your plan to run it. Then you have the search agent

**[14:17]** run it. Then you have the search agent

**[14:17]** run it. Then you have the search agent which has access in this case to search

**[14:19]** which has access in this case to search

**[14:19]** which has access in this case to search tool or I'll show using tavilli in the

**[14:21]** tool or I'll show using tavilli in the

**[14:21]** tool or I'll show using tavilli in the other case um which is using a a faster

**[14:24]** other case um which is using a a faster

**[14:24]** other case um which is using a a faster model gemini flash uh in this case and

**[14:26]** model gemini flash uh in this case and

**[14:26]** model gemini flash uh in this case and then you're using in this case I'm using

**[14:29]** then you're using in this case I'm using

**[14:29]** then you're using in this case I'm using claude son 4.5 for the final analysis

**[14:32]** claude son 4.5 for the final analysis

**[14:32]** claude son 4.5 for the final analysis stage. So I suppose this is a bit what

**[14:34]** stage. So I suppose this is a bit what

**[14:34]** stage. So I suppose this is a bit what people talk about when they're leaning

**[14:35]** people talk about when they're leaning

**[14:35]** people talk about when they're leaning towards graphs. I haven't built this in

**[14:37]** towards graphs. I haven't built this in

**[14:37]** towards graphs. I haven't built this in a graph although I could because it

**[14:38]** a graph although I could because it

**[14:38]** a graph although I could because it doesn't need a graph. It's not complex

**[14:40]** doesn't need a graph. It's not complex

**[14:40]** doesn't need a graph. It's not complex enough to need a graph. And durable

**[14:42]** enough to need a graph. And durable

**[14:42]** enough to need a graph. And durable execution is a way better way of getting

**[14:44]** execution is a way better way of getting

**[14:44]** execution is a way better way of getting snapshotting, but like much more

**[14:46]** snapshotting, but like much more

**[14:46]** snapshotting, but like much more granular support for for durable

**[14:48]** granular support for for durable

**[14:48]** granular support for for durable execution. We added a tool that allowed

**[14:50]** execution. We added a tool that allowed

**[14:50]** execution. We added a tool that allowed the analysis agent to do a bit more web

**[14:52]** the analysis agent to do a bit more web

**[14:52]** the analysis agent to do a bit more web search if it really wanted to. I don't

**[14:53]** search if it really wanted to. I don't

**[14:53]** search if it really wanted to. I don't think it uses it, but this is the actual

**[14:55]** think it uses it, but this is the actual

**[14:55]** think it uses it, but this is the actual deep research code. So you can see how

**[14:57]** deep research code. So you can see how

**[14:58]** deep research code. So you can see how concise it is. We run the plan agent. We


### [15:00 - 16:00]

**[15:01]** concise it is. We run the plan agent. We

**[15:01]** concise it is. We run the plan agent. We get back our plan. We run in parallel

**[15:04]** get back our plan. We run in parallel

**[15:04]** get back our plan. We run in parallel all of the search agents. So, we're just

**[15:06]** all of the search agents. So, we're just

**[15:06]** all of the search agents. So, we're just using a task group from Python to run

**[15:09]** using a task group from Python to run

**[15:09]** using a task group from Python to run all of these. We get those results,

**[15:10]** all of these. We get those results,

**[15:10]** all of these. We get those results, which will all be the text results of

**[15:13]** which will all be the text results of

**[15:13]** which will all be the text results of the different bits of search. We use

**[15:15]** the different bits of search. We use

**[15:15]** the different bits of search. We use format as XML to basically smash all of

**[15:17]** format as XML to basically smash all of

**[15:17]** format as XML to basically smash all of that into a massive lump of reasonably

**[15:19]** that into a massive lump of reasonably

**[15:19]** that into a massive lump of reasonably readable data for the analysis agent.

**[15:21]** readable data for the analysis agent.

**[15:21]** readable data for the analysis agent. Then we go off and run the agent. And we

**[15:23]** Then we go off and run the agent. And we

**[15:23]** Then we go off and run the agent. And we run the kind of question that I'm asking

**[15:25]** run the kind of question that I'm asking

**[15:25]** run the kind of question that I'm asking AI relatively regularly for sales, which

**[15:28]** AI relatively regularly for sales, which

**[15:28]** AI relatively regularly for sales, which is find me a list of hedge funds that

**[15:29]** is find me a list of hedge funds that

**[15:29]** is find me a list of hedge funds that write Python in London. And if I go and

**[15:31]** write Python in London. And if I go and

**[15:31]** write Python in London. And if I go and run this uh UV run deep research,

**[15:42]** we'll see it starting to churn away. We

**[15:42]** we'll see it starting to churn away. We can see it in the terminal with logfire.

**[15:45]** can see it in the terminal with logfire.

**[15:45]** can see it in the terminal with logfire. But we can also

**[15:48]** But we can also

**[15:48]** But we can also come over here to log fire. Let me clear

**[15:52]** come over here to log fire. Let me clear

**[15:52]** come over here to log fire. Let me clear that. Um go to the bottom here and we

**[15:55]** that. Um go to the bottom here and we

**[15:55]** that. Um go to the bottom here and we can see this this run here as it's going

**[15:58]** can see this this run here as it's going

**[15:58]** can see this this run here as it's going on. It's it's run the plan step in nine


### [16:00 - 17:00]

**[16:00]** on. It's it's run the plan step in nine

**[16:00]** on. It's it's run the plan step in nine seconds and you can see all of the

**[16:02]** seconds and you can see all of the

**[16:02]** seconds and you can see all of the search steps going on in parallel. Once

**[16:05]** search steps going on in parallel. Once

**[16:05]** search steps going on in parallel. Once they've finished, it will start. You can

**[16:06]** they've finished, it will start. You can

**[16:06]** they've finished, it will start. You can see the analysis agent has just started.

**[16:09]** see the analysis agent has just started.

**[16:09]** see the analysis agent has just started. We can look at the individual searches.

**[16:11]** We can look at the individual searches.

**[16:11]** We can look at the individual searches. So, you get a pretty good idea of what

**[16:13]** So, you get a pretty good idea of what

**[16:13]** So, you get a pretty good idea of what happened, the question it got asked, uh

**[16:15]** happened, the question it got asked, uh

**[16:15]** happened, the question it got asked, uh the queries it decided to run, bunch of

**[16:19]** the queries it decided to run, bunch of

**[16:19]** the queries it decided to run, bunch of data from medium, different sites,

**[16:21]** data from medium, different sites,

**[16:21]** data from medium, different sites, structured data, and then like the agent

**[16:24]** structured data, and then like the agent

**[16:24]** structured data, and then like the agent also bangs in quite a lot of context,

**[16:26]** also bangs in quite a lot of context,

**[16:26]** also bangs in quite a lot of context, right? So this is each individual one of

**[16:28]** right? So this is each individual one of

**[16:28]** right? So this is each individual one of our like 10 parallel searches. And now

**[16:31]** our like 10 parallel searches. And now

**[16:31]** our like 10 parallel searches. And now the analysis is going to go and run with

**[16:33]** the analysis is going to go and run with

**[16:33]** the analysis is going to go and run with all of that input. You can see so far

**[16:36]** all of that input. You can see so far

**[16:36]** all of that input. You can see so far we've sent spent 8 cents on this

**[16:38]** we've sent spent 8 cents on this

**[16:38]** we've sent spent 8 cents on this particular run. We'll see what it gets

**[16:41]** particular run. We'll see what it gets

**[16:41]** particular run. We'll see what it gets to by the time it finishes. But

**[16:43]** to by the time it finishes. But

**[16:43]** to by the time it finishes. But obviously the problem with this is if I

**[16:44]** obviously the problem with this is if I

**[16:44]** obviously the problem with this is if I kill this now, it's just going to die

**[16:46]** kill this now, it's just going to die

**[16:46]** kill this now, it's just going to die and I'd have to restart from the

**[16:47]** and I'd have to restart from the

**[16:47]** and I'd have to restart from the beginning if I wanted to to run it

**[16:49]** beginning if I wanted to to run it

**[16:49]** beginning if I wanted to to run it again. So, while that churns away, let

**[16:53]** again. So, while that churns away, let

**[16:53]** again. So, while that churns away, let me start introducing you to the durable

**[16:55]** me start introducing you to the durable

**[16:55]** me start introducing you to the durable execution example, spoiler, it's going

**[16:58]** execution example, spoiler, it's going

**[16:58]** execution example, spoiler, it's going to be pretty similar. I discovered last


### [17:00 - 18:00]

**[17:00]** to be pretty similar. I discovered last

**[17:00]** to be pretty similar. I discovered last night that there's a bug with the Vertex

**[17:03]** night that there's a bug with the Vertex

**[17:03]** night that there's a bug with the Vertex SDK. That means that you can't use it

**[17:04]** SDK. That means that you can't use it

**[17:04]** SDK. That means that you can't use it with temporal right now. So, I've

**[17:06]** with temporal right now. So, I've

**[17:06]** with temporal right now. So, I've swapped out uh I think we should fix

**[17:08]** swapped out uh I think we should fix

**[17:08]** swapped out uh I think we should fix that, or at least I'll be winging at uh

**[17:11]** that, or at least I'll be winging at uh

**[17:11]** that, or at least I'll be winging at uh Deep Mind today to go and fix that. So,

**[17:14]** Deep Mind today to go and fix that. So,

**[17:14]** Deep Mind today to go and fix that. So, I've switched it out to OpenAI responses

**[17:15]** I've switched it out to OpenAI responses

**[17:16]** I've switched it out to OpenAI responses here and I'm using Tavilli instead of

**[17:19]** here and I'm using Tavilli instead of

**[17:19]** here and I'm using Tavilli instead of the built-in search. Yeah, but other

**[17:21]** the built-in search. Yeah, but other

**[17:21]** the built-in search. Yeah, but other than that, this is all pretty similar

**[17:22]** than that, this is all pretty similar

**[17:22]** than that, this is all pretty similar code. I could have probably imported the

**[17:25]** code. I could have probably imported the

**[17:25]** code. I could have probably imported the code from the other module. I just

**[17:26]** code from the other module. I just

**[17:26]** code from the other module. I just decided to duplicate it just to keep

**[17:29]** decided to duplicate it just to keep

**[17:29]** decided to duplicate it just to keep things easy. But you see again, we do

**[17:31]** things easy. But you see again, we do

**[17:31]** things easy. But you see again, we do the same thing. We wrap uh our agents in

**[17:33]** the same thing. We wrap uh our agents in

**[17:33]** the same thing. We wrap uh our agents in temporal agent. This analysis one can

**[17:35]** temporal agent. This analysis one can

**[17:35]** temporal agent. This analysis one can take more than I think whatever the

**[17:37]** take more than I think whatever the

**[17:37]** take more than I think whatever the default activity duration is because

**[17:39]** default activity duration is because

**[17:39]** default activity duration is because it's a long basically build up a a

**[17:42]** it's a long basically build up a a

**[17:42]** it's a long basically build up a a summary. And so I give it I think it was

**[17:44]** summary. And so I give it I think it was

**[17:44]** summary. And so I give it I think it was taking longer than 2 minutes or whatever

**[17:46]** taking longer than 2 minutes or whatever

**[17:46]** taking longer than 2 minutes or whatever the default is. So I just gave it an

**[17:47]** the default is. So I just gave it an

**[17:47]** the default is. So I just gave it an hour so it's not going to fail. Um and

**[17:49]** hour so it's not going to fail. Um and

**[17:49]** hour so it's not going to fail. Um and then the the for me the most powerful

**[17:51]** then the the for me the most powerful

**[17:51]** then the the for me the most powerful bit is everything here inside my

**[17:54]** bit is everything here inside my

**[17:54]** bit is everything here inside my workflow looks exactly the same. I don't

**[17:56]** workflow looks exactly the same. I don't

**[17:56]** workflow looks exactly the same. I don't have to do any crazy stuff to do

**[17:57]** have to do any crazy stuff to do

**[17:57]** have to do any crazy stuff to do parallelism. I just use uh task group


### [18:00 - 19:00]

**[18:01]** parallelism. I just use uh task group

**[18:01]** parallelism. I just use uh task group exactly the same. I could use async.io

**[18:04]** exactly the same. I could use async.io

**[18:04]** exactly the same. I could use async.io gather. It's all just imperative Python

**[18:06]** gather. It's all just imperative Python

**[18:06]** gather. It's all just imperative Python code as you would be used to. I could

**[18:08]** code as you would be used to. I could

**[18:08]** code as you would be used to. I could have a if I wanted to run this

**[18:09]** have a if I wanted to run this

**[18:09]** have a if I wanted to run this periodically, I could sleep for seven

**[18:11]** periodically, I could sleep for seven

**[18:12]** periodically, I could sleep for seven days in here. Temporal would take care

**[18:14]** days in here. Temporal would take care

**[18:14]** days in here. Temporal would take care of pausing everything. Again, I'm not

**[18:15]** of pausing everything. Again, I'm not

**[18:15]** of pausing everything. Again, I'm not here to be a temporal salesperson. I

**[18:17]** here to be a temporal salesperson. I

**[18:17]** here to be a temporal salesperson. I don't love everything about what they

**[18:18]** don't love everything about what they

**[18:18]** don't love everything about what they do, but it's a pretty powerful way of

**[18:20]** do, but it's a pretty powerful way of

**[18:20]** do, but it's a pretty powerful way of thinking about code. We don't have to do

**[18:22]** thinking about code. We don't have to do

**[18:22]** thinking about code. We don't have to do all the infra stuff. And then

**[18:24]** all the infra stuff. And then

**[18:24]** all the infra stuff. And then ultimately, again, smash all my context

**[18:27]** ultimately, again, smash all my context

**[18:27]** ultimately, again, smash all my context into the last agent and run it. And

**[18:30]** into the last agent and run it. And

**[18:30]** into the last agent and run it. And again, there's a bit of plug-in stuff. I

**[18:32]** again, there's a bit of plug-in stuff. I

**[18:32]** again, there's a bit of plug-in stuff. I have to plug in log add some plugins,

**[18:33]** have to plug in log add some plugins,

**[18:34]** have to plug in log add some plugins, add the agents as plugins. But again, my

**[18:36]** add the agents as plugins. But again, my

**[18:36]** add the agents as plugins. But again, my code to actually go and kick it off is

**[18:37]** code to actually go and kick it off is

**[18:37]** code to actually go and kick it off is just execute workflow. Simple as that.

**[18:40]** just execute workflow. Simple as that.

**[18:40]** just execute workflow. Simple as that. And I asked it here slightly more

**[18:42]** And I asked it here slightly more

**[18:42]** And I asked it here slightly more controversial question of what's the

**[18:44]** controversial question of what's the

**[18:44]** controversial question of what's the best Python agent framework to use for

**[18:46]** best Python agent framework to use for

**[18:46]** best Python agent framework to use for durable execution and type safety. And

**[18:48]** durable execution and type safety. And

**[18:48]** durable execution and type safety. And we will pray to God it gives the right

**[18:50]** we will pray to God it gives the right

**[18:50]** we will pray to God it gives the right answer when we run it in front of

**[18:52]** answer when we run it in front of

**[18:52]** answer when we run it in front of everyone. If I go and kick that off and

**[18:54]** everyone. If I go and kick that off and

**[18:54]** everyone. If I go and kick that off and run this

**[18:56]** run this

**[18:56]** run this again, we should see it. If we come over

**[18:58]** again, we should see it. If we come over

**[18:58]** again, we should see it. If we come over here, we should see it running in


### [19:00 - 20:00]

**[19:00]** here, we should see it running in

**[19:00]** here, we should see it running in Logfire. You can see we have the stuff

**[19:02]** Logfire. You can see we have the stuff

**[19:02]** Logfire. You can see we have the stuff related to kicking off the agent. It's

**[19:05]** related to kicking off the agent. It's

**[19:05]** related to kicking off the agent. It's kicking off the workflow, excuse me,

**[19:06]** kicking off the workflow, excuse me,

**[19:06]** kicking off the workflow, excuse me, here. And we have the searches beginning

**[19:09]** here. And we have the searches beginning

**[19:09]** here. And we have the searches beginning to happen happen. But the the powerful

**[19:12]** to happen happen. But the the powerful

**[19:12]** to happen happen. But the the powerful bit here is again imagine that we're

**[19:15]** bit here is again imagine that we're

**[19:15]** bit here is again imagine that we're halfway through running all these

**[19:16]** halfway through running all these

**[19:16]** halfway through running all these searches. We're about to start the final

**[19:17]** searches. We're about to start the final

**[19:17]** searches. We're about to start the final step and something comes along and kills

**[19:20]** step and something comes along and kills

**[19:20]** step and something comes along and kills the process. And by in general, you'd

**[19:23]** the process. And by in general, you'd

**[19:23]** the process. And by in general, you'd have to go and completely restart this

**[19:25]** have to go and completely restart this

**[19:25]** have to go and completely restart this process and run your deep deep research

**[19:27]** process and run your deep deep research

**[19:27]** process and run your deep deep research all over again with temporal

**[19:30]** all over again with temporal

**[19:30]** all over again with temporal it will just go and rerun that workflow

**[19:32]** it will just go and rerun that workflow

**[19:32]** it will just go and rerun that workflow automatically. In this case, I'm

**[19:34]** automatically. In this case, I'm

**[19:34]** automatically. In this case, I'm restarting it and just running that one

**[19:35]** restarting it and just running that one

**[19:35]** restarting it and just running that one workflow. But in general, it would just

**[19:37]** workflow. But in general, it would just

**[19:37]** workflow. But in general, it would just automatically go and be restarted and on

**[19:41]** automatically go and be restarted and on

**[19:41]** automatically go and be restarted and on the the next time that Kubernetes comes

**[19:42]** the the next time that Kubernetes comes

**[19:42]** the the next time that Kubernetes comes up, the workflow will run as it would

**[19:45]** up, the workflow will run as it would

**[19:45]** up, the workflow will run as it would have done before, but it will get

**[19:47]** have done before, but it will get

**[19:47]** have done before, but it will get answers to each individual question

**[19:49]** answers to each individual question

**[19:49]** answers to each individual question basically instantly. And so

**[19:52]** basically instantly. And so

**[19:52]** basically instantly. And so if it's not going to fail for me, which

**[19:55]** if it's not going to fail for me, which

**[19:55]** if it's not going to fail for me, which it seems to be, there we are. It started

**[19:57]** it seems to be, there we are. It started

**[19:57]** it seems to be, there we are. It started again. You see a plan took 24


### [20:00 - 21:00]

**[20:00]** again. You see a plan took 24

**[20:00]** again. You see a plan took 24 milliseconds. Search all took no time at

**[20:03]** milliseconds. Search all took no time at

**[20:03]** milliseconds. Search all took no time at all in the grand scheme of things

**[20:04]** all in the grand scheme of things

**[20:04]** all in the grand scheme of things because it just got the result back from

**[20:06]** because it just got the result back from

**[20:06]** because it just got the result back from temporal immediately. And then the

**[20:08]** temporal immediately. And then the

**[20:08]** temporal immediately. And then the analysis that was the the task we needed

**[20:11]** analysis that was the the task we needed

**[20:11]** analysis that was the the task we needed to that we hadn't run yet. Obviously

**[20:13]** to that we hadn't run yet. Obviously

**[20:13]** to that we hadn't run yet. Obviously that needs to go and start again because

**[20:14]** that needs to go and start again because

**[20:14]** that needs to go and start again because that's an activity and you can't

**[20:16]** that's an activity and you can't

**[20:16]** that's an activity and you can't activities obviously have to run again

**[20:17]** activities obviously have to run again

**[20:17]** activities obviously have to run again from scratch. And so once that finishes

**[20:21]** from scratch. And so once that finishes

**[20:21]** from scratch. And so once that finishes I think it does take quite a long time.

**[20:24]** I think it does take quite a long time.

**[20:24]** I think it does take quite a long time. Maybe I can show the previous output. Or

**[20:26]** Maybe I can show the previous output. Or

**[20:26]** Maybe I can show the previous output. Or did we not get to displaying the

**[20:28]** did we not get to displaying the

**[20:28]** did we not get to displaying the previous output? Did it ironically

**[20:29]** previous output? Did it ironically

**[20:29]** previous output? Did it ironically actually fail the time before? But

**[20:31]** actually fail the time before? But

**[20:31]** actually fail the time before? But hopefully once this finishes, we should

**[20:33]** hopefully once this finishes, we should

**[20:33]** hopefully once this finishes, we should be able to see uh its analysis, which

**[20:36]** be able to see uh its analysis, which

**[20:36]** be able to see uh its analysis, which you know, I think is on a par with what

**[20:38]** you know, I think is on a par with what

**[20:38]** you know, I think is on a par with what I see from the other deep research

**[20:39]** I see from the other deep research

**[20:39]** I see from the other deep research things. Obviously, there will be some

**[20:41]** things. Obviously, there will be some

**[20:41]** things. Obviously, there will be some there's some UI work to do to display

**[20:42]** there's some UI work to do to display

**[20:42]** there's some UI work to do to display this in a nice deep deep research

**[20:44]** this in a nice deep deep research

**[20:44]** this in a nice deep deep research interface. There we are. It's completed

**[20:47]** interface. There we are. It's completed

**[20:47]** interface. There we are. It's completed and it has primary recommendation is

**[20:49]** and it has primary recommendation is

**[20:49]** and it has primary recommendation is pantic AI with temporal. So, it it it

**[20:51]** pantic AI with temporal. So, it it it

**[20:52]** pantic AI with temporal. So, it it it did what I hoped it would do. And you

**[20:53]** did what I hoped it would do. And you

**[20:53]** did what I hoped it would do. And you see it's given a reasonable report here

**[20:55]** see it's given a reasonable report here

**[20:55]** see it's given a reasonable report here of like the relative trade-offs of the

**[20:58]** of like the relative trade-offs of the

**[20:58]** of like the relative trade-offs of the other inferior agent frameworks and it


### [21:00 - 22:00]

**[21:00]** other inferior agent frameworks and it

**[21:00]** other inferior agent frameworks and it should have done an executive summary at

**[21:02]** should have done an executive summary at

**[21:02]** should have done an executive summary at the beginning with with links. Yeah. So

**[21:04]** the beginning with with links. Yeah. So

**[21:04]** the beginning with with links. Yeah. So it said podantic AI langraph obviously

**[21:07]** it said podantic AI langraph obviously

**[21:07]** it said podantic AI langraph obviously if you love snapshotting or writing

**[21:09]** if you love snapshotting or writing

**[21:09]** if you love snapshotting or writing unsafe code type unsafe code temporal on

**[21:11]** unsafe code type unsafe code temporal on

**[21:11]** unsafe code type unsafe code temporal on its own which makes sense. Yeah. So

**[21:13]** its own which makes sense. Yeah. So

**[21:13]** its own which makes sense. Yeah. So there's a there's the summary. That is

**[21:16]** there's a there's the summary. That is

**[21:16]** there's a there's the summary. That is the main stuff I had to show. I will

**[21:18]** the main stuff I had to show. I will

**[21:18]** the main stuff I had to show. I will merge the the durable execution stuff in

**[21:20]** merge the the durable execution stuff in

**[21:20]** merge the the durable execution stuff in here. So go here. I just other thing I

**[21:22]** here. So go here. I just other thing I

**[21:22]** here. So go here. I just other thing I want to just say quickly while I have I

**[21:24]** want to just say quickly while I have I

**[21:24]** want to just say quickly while I have I can't work out how to post a comment but

**[21:26]** can't work out how to post a comment but

**[21:26]** can't work out how to post a comment but like you'll find it on Pantic if you if

**[21:28]** like you'll find it on Pantic if you if

**[21:28]** like you'll find it on Pantic if you if you if you look for it. Um oh I have I

**[21:31]** you if you look for it. Um oh I have I

**[21:31]** you if you look for it. Um oh I have I can do that if anyone wants to take a

**[21:32]** can do that if anyone wants to take a

**[21:32]** can do that if anyone wants to take a picture of that QR code. The other thing

**[21:34]** picture of that QR code. The other thing

**[21:34]** picture of that QR code. The other thing I just wanted to mention we're about to

**[21:35]** I just wanted to mention we're about to

**[21:36]** I just wanted to mention we're about to announce uh Pantic AI gateway. So if

**[21:38]** announce uh Pantic AI gateway. So if

**[21:38]** announce uh Pantic AI gateway. So if anyone wants to try it early let us

**[21:41]** anyone wants to try it early let us

**[21:41]** anyone wants to try it early let us know. Um but yeah that platform will be

**[21:43]** know. Um but yeah that platform will be

**[21:43]** know. Um but yeah that platform will be landing soon. You'll be able to use

**[21:45]** landing soon. You'll be able to use

**[21:45]** landing soon. You'll be able to use panic gateway directly to buy inference

**[21:48]** panic gateway directly to buy inference

**[21:48]** panic gateway directly to buy inference from any of the big models or most of

**[21:50]** from any of the big models or most of

**[21:50]** from any of the big models or most of the open source models and self-hosting

**[21:52]** the open source models and self-hosting

**[21:52]** the open source models and self-hosting for enterprise all the observability

**[21:54]** for enterprise all the observability

**[21:54]** for enterprise all the observability stuff. But I I'll I'll save you the full

**[21:56]** stuff. But I I'll I'll save you the full

**[21:56]** stuff. But I I'll I'll save you the full spiel, but that's coming soon. I think

**[21:57]** spiel, but that's coming soon. I think

**[21:57]** spiel, but that's coming soon. I think some of you will find it interesting.

**[21:59]** some of you will find it interesting.

**[21:59]** some of you will find it interesting. That's it. Thanks so much for watching.


### [22:00 - 23:00]

**[22:01]** That's it. Thanks so much for watching.

**[22:01]** That's it. Thanks so much for watching. If you want to learn more about Padantic

**[22:03]** If you want to learn more about Padantic

**[22:03]** If you want to learn more about Padantic AI, Padantic AI gateway or padantic

**[22:05]** AI, Padantic AI gateway or padantic

**[22:05]** AI, Padantic AI gateway or padantic logfire, please scan these QR codes. If

**[22:07]** logfire, please scan these QR codes. If

**[22:07]** logfire, please scan these QR codes. If you have any feedback, uh please come

**[22:09]** you have any feedback, uh please come

**[22:09]** you have any feedback, uh please come and talk to us. Thanks so much for

**[22:11]** and talk to us. Thanks so much for

**[22:11]** and talk to us. Thanks so much for listening.


