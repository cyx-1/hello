# Code World Model- Building World Models for Computation – Jacob Kahn, FAIR Meta

**Video URL:** https://www.youtube.com/watch?v=sYgE4ppDFOQ

---

## Full Transcript

### [00:00 - 01:00]

**[00:22]** Great to be here everyone. I'm Jacob

**[00:22]** Great to be here everyone. I'm Jacob Khan. I'm a researcher at at Farret

**[00:24]** Khan. I'm a researcher at at Farret

**[00:24]** Khan. I'm a researcher at at Farret Medai. I'm going to talk today about the

**[00:26]** Medai. I'm going to talk today about the

**[00:26]** Medai. I'm going to talk today about the code world model which I'll abbreviate

**[00:28]** code world model which I'll abbreviate

**[00:28]** code world model which I'll abbreviate as CWM and what it means to build world

**[00:31]** as CWM and what it means to build world

**[00:31]** as CWM and what it means to build world models for computation.

**[00:33]** models for computation.

**[00:33]** models for computation. This is work done by an incredible team

**[00:35]** This is work done by an incredible team

**[00:35]** This is work done by an incredible team at fair uh extends all over the world

**[00:38]** at fair uh extends all over the world

**[00:38]** at fair uh extends all over the world and I'm very grateful to be

**[00:39]** and I'm very grateful to be

**[00:39]** and I'm very grateful to be collaborating with them.

**[00:41]** collaborating with them.

**[00:41]** collaborating with them. So what's our goal with CWM? Our primary

**[00:44]** So what's our goal with CWM? Our primary

**[00:44]** So what's our goal with CWM? Our primary goal is to build models that reason,

**[00:46]** goal is to build models that reason,

**[00:46]** goal is to build models that reason, plan and make decisions. And we start

**[00:48]** plan and make decisions. And we start

**[00:48]** plan and make decisions. And we start with code because it's an interesting

**[00:50]** with code because it's an interesting

**[00:50]** with code because it's an interesting sandbox in which to think about

**[00:52]** sandbox in which to think about

**[00:52]** sandbox in which to think about reasoning, right? It's constrained. uh

**[00:54]** reasoning, right? It's constrained. uh

**[00:54]** reasoning, right? It's constrained. uh there are certain rules with code and so

**[00:56]** there are certain rules with code and so

**[00:56]** there are certain rules with code and so our our goal is to predict future

**[00:58]** our our goal is to predict future

**[00:58]** our our goal is to predict future observations given past observations and


### [01:00 - 02:00]

**[01:01]** observations given past observations and

**[01:01]** observations given past observations and actions. That's maybe what it means to

**[01:02]** actions. That's maybe what it means to

**[01:02]** actions. That's maybe what it means to build a world model in some sense. And

**[01:04]** build a world model in some sense. And

**[01:04]** build a world model in some sense. And we want to do this because we can learn

**[01:06]** we want to do this because we can learn

**[01:06]** we want to do this because we can learn good representations of things if we

**[01:08]** good representations of things if we

**[01:08]** good representations of things if we learn some sort of mapping between

**[01:09]** learn some sort of mapping between

**[01:09]** learn some sort of mapping between observations and the future. And

**[01:12]** observations and the future. And

**[01:12]** observations and the future. And eventually that leads us to planning and

**[01:13]** eventually that leads us to planning and

**[01:13]** eventually that leads us to planning and reasoning and we can consider different

**[01:15]** reasoning and we can consider different

**[01:15]** reasoning and we can consider different actions and see if we like the results

**[01:17]** actions and see if we like the results

**[01:17]** actions and see if we like the results for decisions we make. I think there's a

**[01:20]** for decisions we make. I think there's a

**[01:20]** for decisions we make. I think there's a bit of a false dichotomy right now

**[01:21]** bit of a false dichotomy right now

**[01:21]** bit of a false dichotomy right now between world models and large language

**[01:23]** between world models and large language

**[01:23]** between world models and large language models. World models are just a

**[01:25]** models. World models are just a

**[01:25]** models. World models are just a parameterization of a problem as I'll

**[01:26]** parameterization of a problem as I'll

**[01:26]** parameterization of a problem as I'll discuss. LMS are a way to to view and

**[01:30]** discuss. LMS are a way to to view and

**[01:30]** discuss. LMS are a way to to view and use that parameterization and I'll I'll

**[01:32]** use that parameterization and I'll I'll

**[01:32]** use that parameterization and I'll I'll dive into more of what that means in a

**[01:34]** dive into more of what that means in a

**[01:34]** dive into more of what that means in a bit.

**[01:36]** bit.

**[01:36]** bit. So, one of the fundamental questions

**[01:37]** So, one of the fundamental questions

**[01:38]** So, one of the fundamental questions we're asking with CWM is what does it

**[01:40]** we're asking with CWM is what does it

**[01:40]** we're asking with CWM is what does it mean to model code? Is code literally

**[01:43]** mean to model code? Is code literally

**[01:43]** mean to model code? Is code literally the syntax in your editor or is it

**[01:46]** the syntax in your editor or is it

**[01:46]** the syntax in your editor or is it something else?

**[01:47]** something else?

**[01:48]** something else? And if you think about it, all a model

**[01:50]** And if you think about it, all a model

**[01:50]** And if you think about it, all a model sees that is operating on code is just

**[01:52]** sees that is operating on code is just

**[01:52]** sees that is operating on code is just syntax, right? We tokenize the input. It

**[01:54]** syntax, right? We tokenize the input. It

**[01:54]** syntax, right? We tokenize the input. It goes into the model and we predict more

**[01:57]** goes into the model and we predict more

**[01:57]** goes into the model and we predict more code as the output. This is the starting

**[01:59]** code as the output. This is the starting

**[01:59]** code as the output. This is the starting and ending point for an analysis of a


### [02:00 - 03:00]

**[02:01]** and ending point for an analysis of a

**[02:02]** and ending point for an analysis of a program with a tokenbased autogressive

**[02:04]** program with a tokenbased autogressive

**[02:04]** program with a tokenbased autogressive model. It's just the syntax. But what if

**[02:06]** model. It's just the syntax. But what if

**[02:06]** model. It's just the syntax. But what if we instead modeled execution more

**[02:08]** we instead modeled execution more

**[02:08]** we instead modeled execution more explicitly? And what if we created a

**[02:10]** explicitly? And what if we created a

**[02:10]** explicitly? And what if we created a maybe a natural language systematic

**[02:13]** maybe a natural language systematic

**[02:13]** maybe a natural language systematic description of programs and neural

**[02:15]** description of programs and neural

**[02:15]** description of programs and neural models could ingest a more structured

**[02:16]** models could ingest a more structured

**[02:16]** models could ingest a more structured representation of what it means to

**[02:18]** representation of what it means to

**[02:18]** representation of what it means to execute code and then maybe we could

**[02:20]** execute code and then maybe we could

**[02:20]** execute code and then maybe we could emit autogressively this representation

**[02:22]** emit autogressively this representation

**[02:22]** emit autogressively this representation too.

**[02:25]** too.

**[02:25]** too. So that's one of our goals for CWM. We

**[02:27]** So that's one of our goals for CWM. We

**[02:27]** So that's one of our goals for CWM. We want to predict program execution

**[02:29]** want to predict program execution

**[02:29]** want to predict program execution because we believe it might lead to us

**[02:31]** because we believe it might lead to us

**[02:31]** because we believe it might lead to us better modeling things about code,

**[02:33]** better modeling things about code,

**[02:33]** better modeling things about code, writing code, analyzing code, and

**[02:35]** writing code, analyzing code, and

**[02:35]** writing code, analyzing code, and beyond. And so what we're going to

**[02:37]** beyond. And so what we're going to

**[02:37]** beyond. And so what we're going to implicitly do is predict a transition

**[02:39]** implicitly do is predict a transition

**[02:39]** implicitly do is predict a transition function of program states as we go

**[02:41]** function of program states as we go

**[02:41]** function of program states as we go about executing.

**[02:44]** about executing.

**[02:44]** about executing. So this is what execution tracing might

**[02:46]** So this is what execution tracing might

**[02:46]** So this is what execution tracing might look like in action. We have a program.

**[02:49]** look like in action. We have a program.

**[02:49]** look like in action. We have a program. We're going to count the number of ours

**[02:50]** We're going to count the number of ours

**[02:50]** We're going to count the number of ours in strawberry. And at each step maybe

**[02:53]** in strawberry. And at each step maybe

**[02:53]** in strawberry. And at each step maybe we'll have some frame separator which

**[02:55]** we'll have some frame separator which

**[02:55]** we'll have some frame separator which will denote distinct lines of execution.

**[02:58]** will denote distinct lines of execution.

**[02:58]** will denote distinct lines of execution. And we'll actually explicitly have local


### [03:00 - 04:00]

**[03:01]** And we'll actually explicitly have local

**[03:01]** And we'll actually explicitly have local variables. We could introduce things

**[03:03]** variables. We could introduce things

**[03:03]** variables. We could introduce things about memory in that trace and that will

**[03:06]** about memory in that trace and that will

**[03:06]** about memory in that trace and that will delineate line by line what's happening

**[03:08]** delineate line by line what's happening

**[03:08]** delineate line by line what's happening as our program executes. And this is

**[03:10]** as our program executes. And this is

**[03:10]** as our program executes. And this is something we could essentially feed to a

**[03:12]** something we could essentially feed to a

**[03:12]** something we could essentially feed to a model because each line of our execution

**[03:14]** model because each line of our execution

**[03:14]** model because each line of our execution trace maps to a corresponding line in a

**[03:16]** trace maps to a corresponding line in a

**[03:16]** trace maps to a corresponding line in a program.

**[03:18]** program.

**[03:18]** program. We don't have to stop at functions. We

**[03:20]** We don't have to stop at functions. We

**[03:20]** We don't have to stop at functions. We could think about entire repository

**[03:22]** could think about entire repository

**[03:22]** could think about entire repository level execution traces. We could think

**[03:23]** level execution traces. We could think

**[03:23]** level execution traces. We could think about distributed system level execution

**[03:25]** about distributed system level execution

**[03:25]** about distributed system level execution traces. We could think about modeling

**[03:27]** traces. We could think about modeling

**[03:27]** traces. We could think about modeling execution for code contest solutions or

**[03:30]** execution for code contest solutions or

**[03:30]** execution for code contest solutions or something more complex. programs with

**[03:31]** something more complex. programs with

**[03:31]** something more complex. programs with high complexity. We could also then

**[03:33]** high complexity. We could also then

**[03:34]** high complexity. We could also then transition that into, as I said, natural

**[03:35]** transition that into, as I said, natural

**[03:35]** transition that into, as I said, natural language tracing. And we'll see what

**[03:37]** language tracing. And we'll see what

**[03:37]** language tracing. And we'll see what that means in a moment.

**[03:39]** that means in a moment.

**[03:39]** that means in a moment. But what does it actually look like to

**[03:41]** But what does it actually look like to

**[03:41]** But what does it actually look like to model that transition function at a high

**[03:42]** model that transition function at a high

**[03:42]** model that transition function at a high level as we start to parameterize the

**[03:44]** level as we start to parameterize the

**[03:44]** level as we start to parameterize the problem? Well, we have programs or we

**[03:46]** problem? Well, we have programs or we

**[03:46]** problem? Well, we have programs or we have data. That's some state. We have an

**[03:49]** have data. That's some state. We have an

**[03:49]** have data. That's some state. We have an action executing the next line and that

**[03:53]** action executing the next line and that

**[03:53]** action executing the next line and that results in the next state. And so both

**[03:54]** results in the next state. And so both

**[03:54]** results in the next state. And so both both the program execution and the

**[03:57]** both the program execution and the

**[03:57]** both the program execution and the model's decision-m in an agentic sense


### [04:00 - 05:00]

**[04:00]** model's decision-m in an agentic sense

**[04:00]** model's decision-m in an agentic sense uh can be modeled as a transition

**[04:01]** uh can be modeled as a transition

**[04:01]** uh can be modeled as a transition function.

**[04:03]** function.

**[04:03]** function. So where are we? This broader approach,

**[04:06]** So where are we? This broader approach,

**[04:06]** So where are we? This broader approach, world modeling, we could say in an

**[04:09]** world modeling, we could say in an

**[04:09]** world modeling, we could say in an agentic reasoning setting, we have a

**[04:11]** agentic reasoning setting, we have a

**[04:11]** agentic reasoning setting, we have a problem. We have a model that thinks

**[04:13]** problem. We have a model that thinks

**[04:13]** problem. We have a model that thinks about the problem. It takes an action in

**[04:14]** about the problem. It takes an action in

**[04:14]** about the problem. It takes an action in the world. We get some feedback. Maybe

**[04:16]** the world. We get some feedback. Maybe

**[04:16]** the world. We get some feedback. Maybe we fail. We think again. And we

**[04:18]** we fail. We think again. And we

**[04:18]** we fail. We think again. And we iteratively continue this process with

**[04:20]** iteratively continue this process with

**[04:20]** iteratively continue this process with feedback from the environment. Maybe in

**[04:21]** feedback from the environment. Maybe in

**[04:22]** feedback from the environment. Maybe in the sense of code, that environment is

**[04:23]** the sense of code, that environment is

**[04:23]** the sense of code, that environment is just an execution in a in a code

**[04:27]** just an execution in a in a code

**[04:27]** just an execution in a in a code setting, right? But with a world model,

**[04:29]** setting, right? But with a world model,

**[04:29]** setting, right? But with a world model, maybe we can actually simulate. We can

**[04:30]** maybe we can actually simulate. We can

**[04:30]** maybe we can actually simulate. We can imagine that action. we can get feedback

**[04:33]** imagine that action. we can get feedback

**[04:33]** imagine that action. we can get feedback in our imagined environment. So we could

**[04:35]** in our imagined environment. So we could

**[04:35]** in our imagined environment. So we could actually generate execution traces about

**[04:36]** actually generate execution traces about

**[04:36]** actually generate execution traces about a program without executing it. And this

**[04:39]** a program without executing it. And this

**[04:39]** a program without executing it. And this gives us the ability to be far more

**[04:41]** gives us the ability to be far more

**[04:41]** gives us the ability to be far more efficient with how we actually structure

**[04:43]** efficient with how we actually structure

**[04:43]** efficient with how we actually structure our agentic execution. We don't have to

**[04:46]** our agentic execution. We don't have to

**[04:46]** our agentic execution. We don't have to interact with the real world unless

**[04:48]** interact with the real world unless

**[04:48]** interact with the real world unless we're ready to.

**[04:51]** we're ready to.

**[04:51]** we're ready to. So let's couple this with autogressive

**[04:53]** So let's couple this with autogressive

**[04:53]** So let's couple this with autogressive large language models. Right now we have

**[04:56]** large language models. Right now we have

**[04:56]** large language models. Right now we have a state of a program. We have an action,

**[04:58]** a state of a program. We have an action,

**[04:58]** a state of a program. We have an action, maybe the next line, and then we get to


### [05:00 - 06:00]

**[05:00]** maybe the next line, and then we get to

**[05:00]** maybe the next line, and then we get to a new state. we take another action etc.

**[05:03]** a new state. we take another action etc.

**[05:03]** a new state. we take another action etc. And so we can sort of turn this with the

**[05:05]** And so we can sort of turn this with the

**[05:05]** And so we can sort of turn this with the execution tracing format I mentioned

**[05:07]** execution tracing format I mentioned

**[05:07]** execution tracing format I mentioned into almost a chain of thought that a

**[05:09]** into almost a chain of thought that a

**[05:09]** into almost a chain of thought that a model can just interpret a model can

**[05:11]** model can just interpret a model can

**[05:11]** model can just interpret a model can learn to predict the next state of an

**[05:13]** learn to predict the next state of an

**[05:13]** learn to predict the next state of an execution trace. And so an LLM can

**[05:16]** execution trace. And so an LLM can

**[05:16]** execution trace. And so an LLM can autogressively generate token by token

**[05:19]** autogressively generate token by token

**[05:19]** autogressively generate token by token the state and action to state function

**[05:22]** the state and action to state function

**[05:22]** the state and action to state function with program executions as the starting

**[05:24]** with program executions as the starting

**[05:24]** with program executions as the starting point. Okay,

**[05:27]** point. Okay,

**[05:27]** point. Okay, let's talk about data for a second.

**[05:29]** let's talk about data for a second.

**[05:29]** let's talk about data for a second. Let's talk about for CWM. We gathered a

**[05:32]** Let's talk about for CWM. We gathered a

**[05:32]** Let's talk about for CWM. We gathered a huge amount of GitHub data. We take

**[05:35]** huge amount of GitHub data. We take

**[05:35]** huge amount of GitHub data. We take GitHub events and as I said, we're

**[05:38]** GitHub events and as I said, we're

**[05:38]** GitHub events and as I said, we're interested in modeling things at the

**[05:39]** interested in modeling things at the

**[05:40]** interested in modeling things at the repo level if we can, at the systems

**[05:41]** repo level if we can, at the systems

**[05:41]** repo level if we can, at the systems level if we can. We want to have

**[05:43]** level if we can. We want to have

**[05:43]** level if we can. We want to have execution traces go outside of the scope

**[05:44]** execution traces go outside of the scope

**[05:44]** execution traces go outside of the scope of simple programs. And so we'll take a

**[05:47]** of simple programs. And so we'll take a

**[05:47]** of simple programs. And so we'll take a bunch of PRs, we'll mutate those PRs,

**[05:50]** bunch of PRs, we'll mutate those PRs,

**[05:50]** bunch of PRs, we'll mutate those PRs, predict changes,

**[05:51]** predict changes,

**[05:51]** predict changes, [snorts and clears throat] and we'll

**[05:52]** [snorts and clears throat] and we'll

**[05:52]** [snorts and clears throat] and we'll eventually have a raw PR data set. And

**[05:54]** eventually have a raw PR data set. And

**[05:54]** eventually have a raw PR data set. And we can actually run tests or CI on those

**[05:57]** we can actually run tests or CI on those

**[05:58]** we can actually run tests or CI on those GitHub repos when we know they're

**[05:59]** GitHub repos when we know they're

**[05:59]** GitHub repos when we know they're passing and then generate execution


### [06:00 - 07:00]

**[06:01]** passing and then generate execution

**[06:01]** passing and then generate execution traces from that repo level data if we

**[06:03]** traces from that repo level data if we

**[06:03]** traces from that repo level data if we want.

**[06:04]** want.

**[06:04]** want. So here we are at the artifact the code

**[06:08]** So here we are at the artifact the code

**[06:08]** So here we are at the artifact the code world model itself. I'll talk a bit

**[06:10]** world model itself. I'll talk a bit

**[06:10]** world model itself. I'll talk a bit about what we did with it, how we

**[06:11]** about what we did with it, how we

**[06:12]** about what we did with it, how we trained it and then what we can do with

**[06:13]** trained it and then what we can do with

**[06:13]** trained it and then what we can do with some of these interesting execution

**[06:14]** some of these interesting execution

**[06:14]** some of these interesting execution trace capabilities. But first it's a 32

**[06:17]** trace capabilities. But first it's a 32

**[06:17]** trace capabilities. But first it's a 32 billion parameter dense transformer.

**[06:18]** billion parameter dense transformer.

**[06:18]** billion parameter dense transformer. This is a model for research. This is

**[06:20]** This is a model for research. This is

**[06:20]** This is a model for research. This is not a huge you can't play with. uh you

**[06:23]** not a huge you can't play with. uh you

**[06:23]** not a huge you can't play with. uh you can play with it right now. It has a

**[06:26]** can play with it right now. It has a

**[06:26]** can play with it right now. It has a nice long context length for some

**[06:27]** nice long context length for some

**[06:27]** nice long context length for some reasoning tasks and we train it end to

**[06:30]** reasoning tasks and we train it end to

**[06:30]** reasoning tasks and we train it end to end. We do all the pre-training and

**[06:31]** end. We do all the pre-training and

**[06:31]** end. We do all the pre-training and post- training ourselves

**[06:34]** post- training ourselves

**[06:34]** post- training ourselves processes. We pre-train on a few

**[06:37]** processes. We pre-train on a few

**[06:37]** processes. We pre-train on a few trillion tokens. We mid-train on some

**[06:38]** trillion tokens. We mid-train on some

**[06:38]** trillion tokens. We mid-train on some more domain specific data. We do some

**[06:41]** more domain specific data. We do some

**[06:41]** more domain specific data. We do some long context mid-training. We fine-tune

**[06:43]** long context mid-training. We fine-tune

**[06:43]** long context mid-training. We fine-tune further uh on some instruction following

**[06:46]** further uh on some instruction following

**[06:46]** further uh on some instruction following and reasoning tokens. And then we do

**[06:48]** and reasoning tokens. And then we do

**[06:48]** and reasoning tokens. And then we do this joint RL and agentic reasoning

**[06:50]** this joint RL and agentic reasoning

**[06:50]** this joint RL and agentic reasoning setup.

**[06:52]** setup.

**[06:52]** setup. So let's parameterize the problem even

**[06:55]** So let's parameterize the problem even

**[06:55]** So let's parameterize the problem even more broadly with CWM. We have a prompt.

**[06:58]** more broadly with CWM. We have a prompt.

**[06:58]** more broadly with CWM. We have a prompt. We have an agent. We do some reasoning.


### [07:00 - 08:00]

**[07:00]** We have an agent. We do some reasoning.

**[07:00]** We have an agent. We do some reasoning. We take an action. We can use a tool. We

**[07:02]** We take an action. We can use a tool. We

**[07:02]** We take an action. We can use a tool. We can emit text which is code that goes

**[07:05]** can emit text which is code that goes

**[07:05]** can emit text which is code that goes into the environment. We take a step.

**[07:06]** into the environment. We take a step.

**[07:06]** into the environment. We take a step. And from that environment, we get a few

**[07:08]** And from that environment, we get a few

**[07:08]** And from that environment, we get a few things back. We get tokens. We get

**[07:10]** things back. We get tokens. We get

**[07:10]** things back. We get tokens. We get rewards. We get log probabilities. We

**[07:12]** rewards. We get log probabilities. We

**[07:12]** rewards. We get log probabilities. We might get compiler output. So with CWM,

**[07:16]** might get compiler output. So with CWM,

**[07:16]** might get compiler output. So with CWM, we're also taking a big step back with

**[07:18]** we're also taking a big step back with

**[07:18]** we're also taking a big step back with how we interact with the environment. C

**[07:19]** how we interact with the environment. C

**[07:19]** how we interact with the environment. C CWM is a very bashoriented model. It has

**[07:23]** CWM is a very bashoriented model. It has

**[07:23]** CWM is a very bashoriented model. It has fewer tools than do other models and it

**[07:26]** fewer tools than do other models and it

**[07:26]** fewer tools than do other models and it has to learn how to use the terminal

**[07:28]** has to learn how to use the terminal

**[07:28]** has to learn how to use the terminal pretty well to solve a lot of the tasks

**[07:29]** pretty well to solve a lot of the tasks

**[07:29]** pretty well to solve a lot of the tasks we give it.

**[07:31]** we give it.

**[07:31]** we give it. And this starts with SRL and with SWRL

**[07:35]** And this starts with SRL and with SWRL

**[07:35]** And this starts with SRL and with SWRL we take a GitHub issue. We feed it to

**[07:37]** we take a GitHub issue. We feed it to

**[07:37]** we take a GitHub issue. We feed it to the agent starting with that repository

**[07:39]** the agent starting with that repository

**[07:39]** the agent starting with that repository level data set from before and we just

**[07:42]** level data set from before and we just

**[07:42]** level data set from before and we just use bash, right? We learn commands uh in

**[07:45]** use bash, right? We learn commands uh in

**[07:45]** use bash, right? We learn commands uh in bash and that lets us mutate our

**[07:47]** bash and that lets us mutate our

**[07:47]** bash and that lets us mutate our environment that lets us mutate the

**[07:49]** environment that lets us mutate the

**[07:49]** environment that lets us mutate the state of files. We can maybe use an edit

**[07:52]** state of files. We can maybe use an edit

**[07:52]** state of files. We can maybe use an edit tool eventually or create content and

**[07:54]** tool eventually or create content and

**[07:54]** tool eventually or create content and then submit things. But ultimately,

**[07:56]** then submit things. But ultimately,

**[07:56]** then submit things. But ultimately, we're trying to put the model in an

**[07:58]** we're trying to put the model in an

**[07:58]** we're trying to put the model in an environment that's very very similar to


### [08:00 - 09:00]

**[08:00]** environment that's very very similar to

**[08:00]** environment that's very very similar to what an engineer would be in and and

**[08:02]** what an engineer would be in and and

**[08:02]** what an engineer would be in and and learn end to end in a bashbased setting.

**[08:05]** learn end to end in a bashbased setting.

**[08:05]** learn end to end in a bashbased setting. Okay.

**[08:06]** Okay.

**[08:06]** Okay. So we can bootstrap this setup further.

**[08:09]** So we can bootstrap this setup further.

**[08:09]** So we can bootstrap this setup further. We can do some SFT before RL and we can

**[08:12]** We can do some SFT before RL and we can

**[08:12]** We can do some SFT before RL and we can find some failure modes for the model.

**[08:14]** find some failure modes for the model.

**[08:14]** find some failure modes for the model. We can rejection sample. So we can take

**[08:17]** We can rejection sample. So we can take

**[08:17]** We can rejection sample. So we can take a bunch of agentic reasoning traces on

**[08:19]** a bunch of agentic reasoning traces on

**[08:19]** a bunch of agentic reasoning traces on code tasks that failed and we can

**[08:22]** code tasks that failed and we can

**[08:22]** code tasks that failed and we can basically feed those back into the

**[08:24]** basically feed those back into the

**[08:24]** basically feed those back into the model. So in this example here, we have

**[08:27]** model. So in this example here, we have

**[08:27]** model. So in this example here, we have a thinking trace where we're thinking

**[08:28]** a thinking trace where we're thinking

**[08:28]** a thinking trace where we're thinking about instantiation logic for some code.

**[08:31]** about instantiation logic for some code.

**[08:31]** about instantiation logic for some code. And I can look for that code. I can call

**[08:32]** And I can look for that code. I can call

**[08:32]** And I can look for that code. I can call an explicit grab function. And this is

**[08:35]** an explicit grab function. And this is

**[08:35]** an explicit grab function. And this is something we did with CWM again with

**[08:37]** something we did with CWM again with

**[08:37]** something we did with CWM again with fewer tools and a larger emphasis on

**[08:40]** fewer tools and a larger emphasis on

**[08:40]** fewer tools and a larger emphasis on bash as a starting point.

**[08:43]** bash as a starting point.

**[08:43]** bash as a starting point. Let's talk about post- training for a

**[08:44]** Let's talk about post- training for a

**[08:44]** Let's talk about post- training for a moment. We want to scale post- training

**[08:46]** moment. We want to scale post- training

**[08:46]** moment. We want to scale post- training quite a bit. This is the trend we see

**[08:49]** quite a bit. This is the trend we see

**[08:49]** quite a bit. This is the trend we see and we're getting a lot of excellent

**[08:50]** and we're getting a lot of excellent

**[08:50]** and we're getting a lot of excellent returns out of uh from a reasoning

**[08:52]** returns out of uh from a reasoning

**[08:52]** returns out of uh from a reasoning perspective when we post train. So part

**[08:56]** perspective when we post train. So part

**[08:56]** perspective when we post train. So part of solving this for CWM because we have

**[08:58]** of solving this for CWM because we have

**[08:58]** of solving this for CWM because we have a small model is an opportunity to


### [09:00 - 10:00]

**[09:00]** a small model is an opportunity to

**[09:00]** a small model is an opportunity to really scale up how we do post training

**[09:02]** really scale up how we do post training

**[09:02]** really scale up how we do post training and in particular to improve the

**[09:04]** and in particular to improve the

**[09:04]** and in particular to improve the throughput of the system and we're doing

**[09:07]** throughput of the system and we're doing

**[09:07]** throughput of the system and we're doing an asynchronous RLbased setup. We have

**[09:09]** an asynchronous RLbased setup. We have

**[09:09]** an asynchronous RLbased setup. We have samplers. We have an environment where

**[09:10]** samplers. We have an environment where

**[09:10]** samplers. We have an environment where we can execute in the terminal and get

**[09:12]** we can execute in the terminal and get

**[09:12]** we can execute in the terminal and get output. We have a bunch of trajectories

**[09:14]** output. We have a bunch of trajectories

**[09:14]** output. We have a bunch of trajectories reasoning trajectories we output. We

**[09:16]** reasoning trajectories we output. We

**[09:16]** reasoning trajectories we output. We have a trainer where we compute

**[09:18]** have a trainer where we compute

**[09:18]** have a trainer where we compute gradients and score trajectories. We

**[09:20]** gradients and score trajectories. We

**[09:20]** gradients and score trajectories. We have a source of truth for the model and

**[09:22]** have a source of truth for the model and

**[09:22]** have a source of truth for the model and then that loop repeats.

**[09:25]** then that loop repeats.

**[09:25]** then that loop repeats. So what's the challenge here? We have

**[09:28]** So what's the challenge here? We have

**[09:28]** So what's the challenge here? We have this loop, right? We have samplers

**[09:29]** this loop, right? We have samplers

**[09:29]** this loop, right? We have samplers predicting trajectories. We have scoring

**[09:31]** predicting trajectories. We have scoring

**[09:31]** predicting trajectories. We have scoring trajectories. We're executing in the

**[09:32]** trajectories. We're executing in the

**[09:32]** trajectories. We're executing in the environment. As we're doing this, we're

**[09:34]** environment. As we're doing this, we're

**[09:34]** environment. As we're doing this, we're going to update a model. Eventually, we

**[09:36]** going to update a model. Eventually, we

**[09:36]** going to update a model. Eventually, we have a produce consumed pipeline

**[09:37]** have a produce consumed pipeline

**[09:37]** have a produce consumed pipeline problem. And so samplers are producing

**[09:39]** problem. And so samplers are producing

**[09:39]** problem. And so samplers are producing lots of trajectories that are consumed

**[09:41]** lots of trajectories that are consumed

**[09:41]** lots of trajectories that are consumed by those trainers. We need to

**[09:42]** by those trainers. We need to

**[09:42]** by those trainers. We need to synchronize weights. And so we solve

**[09:45]** synchronize weights. And so we solve

**[09:45]** synchronize weights. And so we solve this in CWM with a very very

**[09:48]** this in CWM with a very very

**[09:48]** this in CWM with a very very asynchronous model. So of course we have

**[09:52]** asynchronous model. So of course we have

**[09:52]** asynchronous model. So of course we have a trainer that's sending a model

**[09:53]** a trainer that's sending a model

**[09:53]** a trainer that's sending a model checkpoint to a sampler very very

**[09:56]** checkpoint to a sampler very very

**[09:56]** checkpoint to a sampler very very eagerly.

**[09:58]** eagerly.

**[09:58]** eagerly. We have trajectories which are being

**[09:59]** We have trajectories which are being


### [10:00 - 11:00]

**[10:00]** We have trajectories which are being sampled and then sent back to trainers

**[10:02]** sampled and then sent back to trainers

**[10:02]** sampled and then sent back to trainers very eagerly. But in particular we have

**[10:05]** very eagerly. But in particular we have

**[10:05]** very eagerly. But in particular we have cues. So we actually will have many

**[10:07]** cues. So we actually will have many

**[10:07]** cues. So we actually will have many models queued up to be input into a

**[10:10]** models queued up to be input into a

**[10:10]** models queued up to be input into a sampling system. will have many

**[10:12]** sampling system. will have many

**[10:12]** sampling system. will have many trajectories queued up to be scored and

**[10:15]** trajectories queued up to be scored and

**[10:15]** trajectories queued up to be scored and then added visav gradients to the train

**[10:18]** then added visav gradients to the train

**[10:18]** then added visav gradients to the train model. And so this setup stays

**[10:22]** model. And so this setup stays

**[10:22]** model. And so this setup stays relatively on policy even though it's

**[10:23]** relatively on policy even though it's

**[10:23]** relatively on policy even though it's highly asynchronous and we're not really

**[10:26]** highly asynchronous and we're not really

**[10:26]** highly asynchronous and we're not really waiting for much with this setup. We're

**[10:28]** waiting for much with this setup. We're

**[10:28]** waiting for much with this setup. We're able to achieve very very strong

**[10:30]** able to achieve very very strong

**[10:30]** able to achieve very very strong throughput uh because of the

**[10:31]** throughput uh because of the

**[10:31]** throughput uh because of the asynchronicity.

**[10:37]** So one interesting feature of this which

**[10:37]** So one interesting feature of this which is increasingly common is that we're

**[10:40]** is increasingly common is that we're

**[10:40]** is increasingly common is that we're actually updating models mid trajectory.

**[10:42]** actually updating models mid trajectory.

**[10:42]** actually updating models mid trajectory. So I have a model which we're sampling

**[10:44]** So I have a model which we're sampling

**[10:44]** So I have a model which we're sampling from. It's interacting with the

**[10:46]** from. It's interacting with the

**[10:46]** from. It's interacting with the environment. It's generating data. It's

**[10:49]** environment. It's generating data. It's

**[10:49]** environment. It's generating data. It's executing bash commands. It's executing

**[10:51]** executing bash commands. It's executing

**[10:51]** executing bash commands. It's executing code. It's getting output. And I might

**[10:53]** code. It's getting output. And I might

**[10:53]** code. It's getting output. And I might actually update that model while it's

**[10:56]** actually update that model while it's

**[10:56]** actually update that model while it's interacting with the environment. So

**[10:58]** interacting with the environment. So

**[10:58]** interacting with the environment. So mid- trajectory I could totally swap out

**[10:59]** mid- trajectory I could totally swap out

**[10:59]** mid- trajectory I could totally swap out the model with the new checkpoint and


### [11:00 - 12:00]

**[11:02]** the model with the new checkpoint and

**[11:02]** the model with the new checkpoint and the trajectory will change a little bit.

**[11:05]** the trajectory will change a little bit.

**[11:05]** the trajectory will change a little bit. Uh theoretically that trajectory is a

**[11:07]** Uh theoretically that trajectory is a

**[11:07]** Uh theoretically that trajectory is a bit off policy but the guarantees we

**[11:11]** bit off policy but the guarantees we

**[11:11]** bit off policy but the guarantees we have with this system are quite strong

**[11:12]** have with this system are quite strong

**[11:12]** have with this system are quite strong still in that because of the throughput

**[11:15]** still in that because of the throughput

**[11:15]** still in that because of the throughput and because of the amount of data we see

**[11:17]** and because of the amount of data we see

**[11:17]** and because of the amount of data we see we're able to make a lot of guarantees

**[11:19]** we're able to make a lot of guarantees

**[11:19]** we're able to make a lot of guarantees around and take a lot of risk with

**[11:21]** around and take a lot of risk with

**[11:21]** around and take a lot of risk with updating the model on the fly. And this

**[11:24]** updating the model on the fly. And this

**[11:24]** updating the model on the fly. And this gives us really a system where there are

**[11:25]** gives us really a system where there are

**[11:25]** gives us really a system where there are very very few bottlenecks overall

**[11:28]** very very few bottlenecks overall

**[11:28]** very very few bottlenecks overall because we're queuing models, we're

**[11:29]** because we're queuing models, we're

**[11:29]** because we're queuing models, we're queuing trajectories. We don't have to

**[11:30]** queuing trajectories. We don't have to

**[11:30]** queuing trajectories. We don't have to wait until anything is done.

**[11:34]** wait until anything is done.

**[11:34]** wait until anything is done. Okay, so overall we post train on still

**[11:38]** Okay, so overall we post train on still

**[11:38]** Okay, so overall we post train on still a relatively small number of steps at

**[11:40]** a relatively small number of steps at

**[11:40]** a relatively small number of steps at pretty large scale and we process about

**[11:44]** pretty large scale and we process about

**[11:44]** pretty large scale and we process about 200 and some billion tokens. And this

**[11:48]** 200 and some billion tokens. And this

**[11:48]** 200 and some billion tokens. And this scale works really well. It produces a

**[11:50]** scale works really well. It produces a

**[11:50]** scale works really well. It produces a strong model, a strong open model. It's

**[11:53]** strong model, a strong open model. It's

**[11:53]** strong model, a strong open model. It's a pretty small model. It punches above

**[11:54]** a pretty small model. It punches above

**[11:54]** a pretty small model. It punches above its weight. It's very nice. It's pretty

**[11:56]** its weight. It's very nice. It's pretty

**[11:56]** its weight. It's very nice. It's pretty versatile. It uses tools in bash very

**[11:59]** versatile. It uses tools in bash very

**[11:59]** versatile. It uses tools in bash very well. [clears throat]


### [12:00 - 13:00]

**[12:01]** well. [clears throat]

**[12:01]** well. [clears throat] But what can you what can we actually do

**[12:02]** But what can you what can we actually do

**[12:02]** But what can you what can we actually do with uh with this model, right? What can

**[12:04]** with uh with this model, right? What can

**[12:04]** with uh with this model, right? What can we do with a model that understands

**[12:06]** we do with a model that understands

**[12:06]** we do with a model that understands program execution traces that maybe has

**[12:08]** program execution traces that maybe has

**[12:08]** program execution traces that maybe has a good understanding of how how a

**[12:10]** a good understanding of how how a

**[12:10]** a good understanding of how how a program will run and predicting future

**[12:13]** program will run and predicting future

**[12:13]** program will run and predicting future state of a program.

**[12:18]** CWM traces code really well, right? We

**[12:18]** CWM traces code really well, right? We know that. we've showed it execution

**[12:20]** know that. we've showed it execution

**[12:20]** know that. we've showed it execution traces and I can actually give it a

**[12:22]** traces and I can actually give it a

**[12:22]** traces and I can actually give it a function and then it can go and trace

**[12:25]** function and then it can go and trace

**[12:25]** function and then it can go and trace line by line that function with very

**[12:27]** line by line that function with very

**[12:27]** line by line that function with very very high accuracy. It can show me the

**[12:29]** very high accuracy. It can show me the

**[12:30]** very high accuracy. It can show me the values of local variables at certain

**[12:31]** values of local variables at certain

**[12:31]** values of local variables at certain points again with a lot of precision

**[12:35]** points again with a lot of precision

**[12:35]** points again with a lot of precision and this gives us some pretty

**[12:38]** and this gives us some pretty

**[12:38]** and this gives us some pretty interesting capabilities.

**[12:39]** interesting capabilities.

**[12:39]** interesting capabilities. I can think about a neural debugger on

**[12:42]** I can think about a neural debugger on

**[12:42]** I can think about a neural debugger on top of a model. Traditionally, right, I

**[12:45]** top of a model. Traditionally, right, I

**[12:45]** top of a model. Traditionally, right, I have a piece of code. I don't know what

**[12:47]** have a piece of code. I don't know what

**[12:47]** have a piece of code. I don't know what I want to write. I put some question

**[12:48]** I want to write. I put some question

**[12:48]** I want to write. I put some question marks.

**[12:50]** marks.

**[12:50]** marks. Historically, I might prompt a model

**[12:52]** Historically, I might prompt a model

**[12:52]** Historically, I might prompt a model with natural language. I want to set the

**[12:54]** with natural language. I want to set the

**[12:54]** with natural language. I want to set the valuable uh the variable left and right

**[12:57]** valuable uh the variable left and right

**[12:57]** valuable uh the variable left and right to be something in particular. I don't

**[12:58]** to be something in particular. I don't

**[12:58]** to be something in particular. I don't know what it is. Uh now I need to


### [13:00 - 14:00]

**[13:00]** know what it is. Uh now I need to

**[13:00]** know what it is. Uh now I need to specify very fully the ambiguity that

**[13:02]** specify very fully the ambiguity that

**[13:02]** specify very fully the ambiguity that I'm experiencing with how to complete my

**[13:05]** I'm experiencing with how to complete my

**[13:05]** I'm experiencing with how to complete my program. With CWM, I can express those

**[13:08]** program. With CWM, I can express those

**[13:08]** program. With CWM, I can express those things very naturally in line with code.

**[13:11]** things very naturally in line with code.

**[13:11]** things very naturally in line with code. And I can actually express the shape of

**[13:13]** And I can actually express the shape of

**[13:13]** And I can actually express the shape of the program I want with code and the

**[13:15]** the program I want with code and the

**[13:15]** the program I want with code and the model will fill in the rest. And the

**[13:17]** model will fill in the rest. And the

**[13:17]** model will fill in the rest. And the model fills in the rest by understanding

**[13:19]** model fills in the rest by understanding

**[13:19]** model fills in the rest by understanding that the user wrote a for loop here. The

**[13:21]** that the user wrote a for loop here. The

**[13:21]** that the user wrote a for loop here. The user wrote a condition here. The user

**[13:24]** user wrote a condition here. The user

**[13:24]** user wrote a condition here. The user left a variable and assigned. Well, if I

**[13:27]** left a variable and assigned. Well, if I

**[13:27]** left a variable and assigned. Well, if I were to go execute that, I could

**[13:28]** were to go execute that, I could

**[13:28]** were to go execute that, I could simulate the execution of that loop and

**[13:32]** simulate the execution of that loop and

**[13:32]** simulate the execution of that loop and understand better what it is the user is

**[13:34]** understand better what it is the user is

**[13:34]** understand better what it is the user is really after. And so a neural debugger

**[13:37]** really after. And so a neural debugger

**[13:37]** really after. And so a neural debugger is something that helps you compose with

**[13:40]** is something that helps you compose with

**[13:40]** is something that helps you compose with code side by side. It's not just

**[13:41]** code side by side. It's not just

**[13:42]** code side by side. It's not just generating code and it allows you to

**[13:44]** generating code and it allows you to

**[13:44]** generating code and it allows you to again express the semantics of code very

**[13:46]** again express the semantics of code very

**[13:46]** again express the semantics of code very very loosely but also very very

**[13:48]** very loosely but also very very

**[13:48]** very loosely but also very very precisely. So if I have a piece of code

**[13:50]** precisely. So if I have a piece of code

**[13:50]** precisely. So if I have a piece of code where I I want a certain structure I can

**[13:53]** where I I want a certain structure I can

**[13:53]** where I I want a certain structure I can ensure that the model understands that

**[13:55]** ensure that the model understands that

**[13:55]** ensure that the model understands that structure and and can implicitly trace

**[13:57]** structure and and can implicitly trace

**[13:57]** structure and and can implicitly trace the execution.


### [14:00 - 15:00]

**[14:04]** This will make theoreticians bristle.

**[14:04]** This will make theoreticians bristle. But I can also think about some really

**[14:05]** But I can also think about some really

**[14:05]** But I can also think about some really ambitious things in computer science.

**[14:08]** ambitious things in computer science.

**[14:08]** ambitious things in computer science. The halting problem we know is this very

**[14:10]** The halting problem we know is this very

**[14:10]** The halting problem we know is this very fundamental problem where we don't know

**[14:13]** fundamental problem where we don't know

**[14:13]** fundamental problem where we don't know if a if a program is going to to halt to

**[14:16]** if a if a program is going to to halt to

**[14:16]** if a if a program is going to to halt to stop executing to terminate. And in

**[14:19]** stop executing to terminate. And in

**[14:19]** stop executing to terminate. And in particular, this is tough because in

**[14:20]** particular, this is tough because in

**[14:20]** particular, this is tough because in order to know if a program halts, we

**[14:22]** order to know if a program halts, we

**[14:22]** order to know if a program halts, we would have to simulate the entire

**[14:23]** would have to simulate the entire

**[14:23]** would have to simulate the entire execution of the program which if it

**[14:25]** execution of the program which if it

**[14:25]** execution of the program which if it didn't halt would take forever. So the

**[14:28]** didn't halt would take forever. So the

**[14:28]** didn't halt would take forever. So the halting problem is in some sense a

**[14:31]** halting problem is in some sense a

**[14:31]** halting problem is in some sense a difficult problem to simulate or decide.

**[14:34]** difficult problem to simulate or decide.

**[14:34]** difficult problem to simulate or decide. And so the question we can ask with CWM

**[14:37]** And so the question we can ask with CWM

**[14:37]** And so the question we can ask with CWM is can I approximate some of these

**[14:38]** is can I approximate some of these

**[14:38]** is can I approximate some of these things? Can I concretely reason about

**[14:42]** things? Can I concretely reason about

**[14:42]** things? Can I concretely reason about program execution dynamics in this

**[14:45]** program execution dynamics in this

**[14:45]** program execution dynamics in this sense? So can I say here's a program

**[14:47]** sense? So can I say here's a program

**[14:47]** sense? So can I say here's a program does it halt? Maybe the model by

**[14:50]** does it halt? Maybe the model by

**[14:50]** does it halt? Maybe the model by simulating execution can understand

**[14:53]** simulating execution can understand

**[14:53]** simulating execution can understand really really high level patterns.

**[14:56]** really really high level patterns.

**[14:56]** really really high level patterns. In the same way the model can understand

**[14:59]** In the same way the model can understand

**[14:59]** In the same way the model can understand high level patterns in broader systems,


### [15:00 - 16:00]

**[15:01]** high level patterns in broader systems,

**[15:01]** high level patterns in broader systems, right? I could use this to debug a huge

**[15:03]** right? I could use this to debug a huge

**[15:03]** right? I could use this to debug a huge distributed system where executing code

**[15:06]** distributed system where executing code

**[15:06]** distributed system where executing code is very very expensive or even an

**[15:08]** is very very expensive or even an

**[15:08]** is very very expensive or even an expensive function on a single machine.

**[15:10]** expensive function on a single machine.

**[15:10]** expensive function on a single machine. Right? But the ability to have an

**[15:13]** Right? But the ability to have an

**[15:13]** Right? But the ability to have an implicit world model internally where

**[15:15]** implicit world model internally where

**[15:15]** implicit world model internally where I'm simulating what's happening with a

**[15:17]** I'm simulating what's happening with a

**[15:17]** I'm simulating what's happening with a piece of code or a broader system gives

**[15:20]** piece of code or a broader system gives

**[15:20]** piece of code or a broader system gives me the ability to reason about it

**[15:22]** me the ability to reason about it

**[15:22]** me the ability to reason about it without executing otherwise expensive

**[15:23]** without executing otherwise expensive

**[15:24]** without executing otherwise expensive things.

**[15:25]** things.

**[15:25]** things. So we can make some progress with the

**[15:27]** So we can make some progress with the

**[15:27]** So we can make some progress with the halting problem by building a model that

**[15:29]** halting problem by building a model that

**[15:29]** halting problem by building a model that simulates it that simulates execution

**[15:32]** simulates it that simulates execution

**[15:32]** simulates it that simulates execution and from there we can simulate and

**[15:35]** and from there we can simulate and

**[15:35]** and from there we can simulate and approximate what it means to solve

**[15:37]** approximate what it means to solve

**[15:37]** approximate what it means to solve otherwise impossible problems in

**[15:39]** otherwise impossible problems in

**[15:39]** otherwise impossible problems in computer science. So this is pretty

**[15:41]** computer science. So this is pretty

**[15:41]** computer science. So this is pretty interesting.

**[15:43]** interesting.

**[15:43]** interesting. With that I want to encourage everyone

**[15:45]** With that I want to encourage everyone

**[15:45]** With that I want to encourage everyone to go build on CWM.

**[15:49]** to go build on CWM.

**[15:49]** to go build on CWM. Uh this talk does halt. This talk does

**[15:52]** Uh this talk does halt. This talk does

**[15:52]** Uh this talk does halt. This talk does terminate. Um, and the model's available

**[15:55]** terminate. Um, and the model's available

**[15:55]** terminate. Um, and the model's available on hugging face. We have some [snorts]

**[15:57]** on hugging face. We have some [snorts]

**[15:57]** on hugging face. We have some [snorts] code on GitHub which will help you get

**[15:59]** code on GitHub which will help you get

**[15:59]** code on GitHub which will help you get started with inference in a fashion


### [16:00 - 17:00]

**[16:01]** started with inference in a fashion

**[16:01]** started with inference in a fashion where you can twiddle bits a bit more.

**[16:03]** where you can twiddle bits a bit more.

**[16:03]** where you can twiddle bits a bit more. We also have a technical report again

**[16:05]** We also have a technical report again

**[16:05]** We also have a technical report again where we really try to be as open as

**[16:06]** where we really try to be as open as

**[16:06]** where we really try to be as open as possible with all of these details

**[16:08]** possible with all of these details

**[16:08]** possible with all of these details around training. This post-raining setup

**[16:10]** around training. This post-raining setup

**[16:10]** around training. This post-raining setup I mentioned is explained in even more

**[16:12]** I mentioned is explained in even more

**[16:12]** I mentioned is explained in even more excruciating detail as well as some of

**[16:14]** excruciating detail as well as some of

**[16:14]** excruciating detail as well as some of the data that we use for execution

**[16:16]** the data that we use for execution

**[16:16]** the data that we use for execution training and some of what we imagine a

**[16:18]** training and some of what we imagine a

**[16:18]** training and some of what we imagine a model with these capabilities could be

**[16:19]** model with these capabilities could be

**[16:19]** model with these capabilities could be used for. Thanks for your time. Have

**[16:22]** used for. Thanks for your time. Have

**[16:22]** used for. Thanks for your time. Have fun.

**[16:23]** fun.

**[16:23]** fun. >> [applause and cheering]


