# How to Build Planning Agents without losing control - Yogendra Miraje, Factset

**Video URL:** https://www.youtube.com/watch?v=sl3icG-IjHo

---

## Full Transcript

### [00:00 - 01:00]

**[00:18]** Hi everyone, I'm Yogi. I work at Faxet,

**[00:18]** Hi everyone, I'm Yogi. I work at Faxet, a financial data and software company.

**[00:21]** a financial data and software company.

**[00:21]** a financial data and software company. And today I'll be sharing some of my

**[00:23]** And today I'll be sharing some of my

**[00:23]** And today I'll be sharing some of my experience while building agent.

**[00:27]** experience while building agent.

**[00:27]** experience while building agent. In last few years we have seen

**[00:28]** In last few years we have seen

**[00:28]** In last few years we have seen tremendous growth in AI and especially

**[00:32]** tremendous growth in AI and especially

**[00:32]** tremendous growth in AI and especially in last couple of years we are on

**[00:34]** in last couple of years we are on

**[00:34]** in last couple of years we are on exponential curve of intelligence growth

**[00:38]** exponential curve of intelligence growth

**[00:38]** exponential curve of intelligence growth and yet it feels like

**[00:41]** and yet it feels like

**[00:41]** and yet it feels like when we are develop AI applications

**[00:44]** when we are develop AI applications

**[00:44]** when we are develop AI applications driving a monster truck through a

**[00:46]** driving a monster truck through a

**[00:46]** driving a monster truck through a crowded mall with a tiny joysticks. So

**[00:48]** crowded mall with a tiny joysticks. So

**[00:48]** crowded mall with a tiny joysticks. So AI applications have not seen its charge

**[00:50]** AI applications have not seen its charge

**[00:50]** AI applications have not seen its charge GPD moment yet.

**[00:53]** GPD moment yet.

**[00:53]** GPD moment yet. There are many reasons why agents don't

**[00:55]** There are many reasons why agents don't

**[00:55]** There are many reasons why agents don't behave but probably one reason that

**[00:59]** behave but probably one reason that

**[00:59]** behave but probably one reason that strikes out is it misses the right


### [01:00 - 02:00]

**[01:02]** strikes out is it misses the right

**[01:02]** strikes out is it misses the right context

**[01:03]** context

**[01:03]** context and in case of enterprises often it

**[01:06]** and in case of enterprises often it

**[01:06]** and in case of enterprises often it means that it does not have knowledge of

**[01:09]** means that it does not have knowledge of

**[01:09]** means that it does not have knowledge of enterprise specific workflows

**[01:13]** enterprise specific workflows

**[01:13]** enterprise specific workflows but before that we will see some common

**[01:16]** but before that we will see some common

**[01:16]** but before that we will see some common context and just like agents human also

**[01:19]** context and just like agents human also

**[01:19]** context and just like agents human also need a common context so let's start

**[01:21]** need a common context so let's start

**[01:21]** need a common context so let's start with some key definitions

**[01:24]** with some key definitions

**[01:24]** with some key definitions So as you know LLMs are limited by their

**[01:27]** So as you know LLMs are limited by their

**[01:27]** So as you know LLMs are limited by their knowledge at the time of training. So we

**[01:30]** knowledge at the time of training. So we

**[01:30]** knowledge at the time of training. So we enhance their functionality by

**[01:34]** enhance their functionality by

**[01:34]** enhance their functionality by increase it by tool. And when you

**[01:37]** increase it by tool. And when you

**[01:37]** increase it by tool. And when you combine this LLM with tool and memory we

**[01:39]** combine this LLM with tool and memory we

**[01:39]** combine this LLM with tool and memory we call it augmented LLM. When you place

**[01:42]** call it augmented LLM. When you place

**[01:42]** call it augmented LLM. When you place this augmented LLM on a static and

**[01:44]** this augmented LLM on a static and

**[01:44]** this augmented LLM on a static and predefined path we call it a workflow.

**[01:47]** predefined path we call it a workflow.

**[01:48]** predefined path we call it a workflow. And if these augmented LLMs

**[01:51]** And if these augmented LLMs

**[01:51]** And if these augmented LLMs have high autonomy and feedback loop, we

**[01:53]** have high autonomy and feedback loop, we

**[01:53]** have high autonomy and feedback loop, we call it as an agent.

**[01:56]** call it as an agent.

**[01:56]** call it as an agent. Now workflows are controllable and

**[01:58]** Now workflows are controllable and

**[01:58]** Now workflows are controllable and reliable


### [02:00 - 03:00]

**[02:00]** reliable

**[02:00]** reliable while agents have flexibility and they

**[02:02]** while agents have flexibility and they

**[02:02]** while agents have flexibility and they are highly autonomous. So the question

**[02:05]** are highly autonomous. So the question

**[02:05]** are highly autonomous. So the question is can we get best of both worlds? So

**[02:08]** is can we get best of both worlds? So

**[02:08]** is can we get best of both worlds? So the answer is yes. With agentic

**[02:10]** the answer is yes. With agentic

**[02:10]** the answer is yes. With agentic workflows we can plan and execute the

**[02:13]** workflows we can plan and execute the

**[02:13]** workflows we can plan and execute the workflows based on the goal, context and

**[02:15]** workflows based on the goal, context and

**[02:15]** workflows based on the goal, context and feedback.

**[02:21]** I see these terms being used very

**[02:21]** I see these terms being used very loosely and at times interchangeably.

**[02:24]** loosely and at times interchangeably.

**[02:24]** loosely and at times interchangeably. So I would like to make a key

**[02:26]** So I would like to make a key

**[02:26]** So I would like to make a key distinction between workflow agent and

**[02:28]** distinction between workflow agent and

**[02:28]** distinction between workflow agent and agentic workflow.

**[02:35]** Workflow agent is a predefined workflow

**[02:35]** Workflow agent is a predefined workflow run by agent

**[02:37]** run by agent

**[02:37]** run by agent while agentic workflow is a workflow

**[02:40]** while agentic workflow is a workflow

**[02:40]** while agentic workflow is a workflow planned and run by an agent.

**[02:43]** planned and run by an agent.

**[02:43]** planned and run by an agent. I know these terms are like quite

**[02:45]** I know these terms are like quite

**[02:45]** I know these terms are like quite confusing and in AI we are very bad at

**[02:48]** confusing and in AI we are very bad at

**[02:48]** confusing and in AI we are very bad at naming things. So if you are confused

**[02:52]** naming things. So if you are confused

**[02:52]** naming things. So if you are confused don't worry in case of workflow agent

**[02:54]** don't worry in case of workflow agent

**[02:54]** don't worry in case of workflow agent just remember that workflow is in

**[02:55]** just remember that workflow is in

**[02:55]** just remember that workflow is in control and workflow is static. In case

**[02:58]** control and workflow is static. In case

**[02:58]** control and workflow is static. In case of agentic workflow agent is always in


### [03:00 - 04:00]

**[03:01]** of agentic workflow agent is always in

**[03:01]** of agentic workflow agent is always in control and the workflow is dynamic.

**[03:09]** It is also important to view these

**[03:09]** It is also important to view these systems as agentic system. As Andrew

**[03:12]** systems as agentic system. As Andrew

**[03:12]** systems as agentic system. As Andrew pointed out correctly

**[03:14]** pointed out correctly

**[03:14]** pointed out correctly on agentic spectrum, agentic workflows

**[03:18]** on agentic spectrum, agentic workflows

**[03:18]** on agentic spectrum, agentic workflows have more agenticness than workflow

**[03:20]** have more agenticness than workflow

**[03:20]** have more agenticness than workflow agents. Generally speaking,

**[03:28]** so why all of this matter?

**[03:28]** so why all of this matter? Apart from control, reliability,

**[03:31]** Apart from control, reliability,

**[03:31]** Apart from control, reliability, predictability

**[03:33]** predictability

**[03:33]** predictability for enterprises,

**[03:35]** for enterprises,

**[03:35]** for enterprises, agentic workflows provide a way to

**[03:37]** agentic workflows provide a way to

**[03:37]** agentic workflows provide a way to automate the workflows at scale.

**[03:40]** automate the workflows at scale.

**[03:40]** automate the workflows at scale. And perhaps most important thing is

**[03:44]** And perhaps most important thing is

**[03:44]** And perhaps most important thing is enterprises can use their existing

**[03:47]** enterprises can use their existing

**[03:47]** enterprises can use their existing enterprises uh microservices to build on

**[03:51]** enterprises uh microservices to build on

**[03:51]** enterprises uh microservices to build on top of it. And in some cases

**[03:55]** top of it. And in some cases

**[03:55]** top of it. And in some cases these enterprises have invested years

**[03:57]** these enterprises have invested years

**[03:57]** these enterprises have invested years not if not decades.


### [04:00 - 05:00]

**[04:03]** So before diving deep I would like to

**[04:03]** So before diving deep I would like to say that even though I'm speaking in

**[04:05]** say that even though I'm speaking in

**[04:05]** say that even though I'm speaking in terms of enterprise context here the

**[04:07]** terms of enterprise context here the

**[04:07]** terms of enterprise context here the concepts are generally applicable.

**[04:14]** So where do we begin? In last few years

**[04:14]** So where do we begin? In last few years the focus really has been on the react

**[04:17]** the focus really has been on the react

**[04:17]** the focus really has been on the react based agent and in building agentic

**[04:20]** based agent and in building agentic

**[04:20]** based agent and in building agentic workflow we need to move on from react

**[04:23]** workflow we need to move on from react

**[04:23]** workflow we need to move on from react based agent to proactive agents. By the

**[04:25]** based agent to proactive agents. By the

**[04:25]** based agent to proactive agents. By the way great philosophy for life as well.

**[04:32]** So for building agent workflows you need

**[04:32]** So for building agent workflows you need tools, memory and reflection. But more

**[04:38]** tools, memory and reflection. But more

**[04:38]** tools, memory and reflection. But more importantly you will need a design

**[04:40]** importantly you will need a design

**[04:40]** importantly you will need a design pattern called planning by sub goal divi

**[04:43]** pattern called planning by sub goal divi

**[04:43]** pattern called planning by sub goal divi sub goal division.

**[04:46]** sub goal division.

**[04:46]** sub goal division. Sometimes also referred as a task

**[04:47]** Sometimes also referred as a task

**[04:47]** Sometimes also referred as a task decomposition and it is just a fancy way

**[04:50]** decomposition and it is just a fancy way

**[04:50]** decomposition and it is just a fancy way of saying that take your goal and break

**[04:53]** of saying that take your goal and break

**[04:53]** of saying that take your goal and break it down into simpler steps.

**[04:57]** it down into simpler steps.

**[04:57]** it down into simpler steps. Here are some specific agentic

**[04:59]** Here are some specific agentic

**[04:59]** Here are some specific agentic architecture and research papers that


### [05:00 - 06:00]

**[05:01]** architecture and research papers that

**[05:01]** architecture and research papers that you will find useful and each of that

**[05:04]** you will find useful and each of that

**[05:04]** you will find useful and each of that has like its own pro and cons and langun

**[05:07]** has like its own pro and cons and langun

**[05:07]** has like its own pro and cons and langun has done fantastic job of uh creating a

**[05:10]** has done fantastic job of uh creating a

**[05:10]** has done fantastic job of uh creating a blog from this and uh also given the

**[05:14]** blog from this and uh also given the

**[05:14]** blog from this and uh also given the code. So I highly recommend checking it

**[05:16]** code. So I highly recommend checking it

**[05:16]** code. So I highly recommend checking it out.

**[05:18]** out.

**[05:18]** out. So how does it look in practice?

**[05:21]** So how does it look in practice?

**[05:21]** So how does it look in practice? So what in in fact that what we have

**[05:23]** So what in in fact that what we have

**[05:23]** So what in in fact that what we have done is we are taking this LLM compiler

**[05:25]** done is we are taking this LLM compiler

**[05:25]** done is we are taking this LLM compiler architecture and trying to adop for our

**[05:28]** architecture and trying to adop for our

**[05:28]** architecture and trying to adop for our problems

**[05:29]** problems

**[05:29]** problems and you can see some components here uh

**[05:32]** and you can see some components here uh

**[05:32]** and you can see some components here uh that you also find that in your

**[05:33]** that you also find that in your

**[05:33]** that you also find that in your organization uh microservices

**[05:37]** organization uh microservices

**[05:37]** organization uh microservices and you build tools around those

**[05:38]** and you build tools around those

**[05:38]** and you build tools around those microservices and when a user question

**[05:41]** microservices and when a user question

**[05:41]** microservices and when a user question ask it goes to blueprint generator and I

**[05:43]** ask it goes to blueprint generator and I

**[05:43]** ask it goes to blueprint generator and I will get to that in a bit but consider

**[05:45]** will get to that in a bit but consider

**[05:46]** will get to that in a bit but consider it as like a high level plan

**[05:49]** it as like a high level plan

**[05:49]** it as like a high level plan what we call it is a blueprint print

**[05:51]** what we call it is a blueprint print

**[05:51]** what we call it is a blueprint print that gets fed to planner. Planner is

**[05:54]** that gets fed to planner. Planner is

**[05:54]** that gets fed to planner. Planner is your low level task. Planner it gives

**[05:58]** your low level task. Planner it gives

**[05:58]** your low level task. Planner it gives the plan to the executor and executor is


### [06:00 - 07:00]

**[06:01]** the plan to the executor and executor is

**[06:01]** the plan to the executor and executor is supposed to execute it and joiner

**[06:05]** supposed to execute it and joiner

**[06:05]** supposed to execute it and joiner combines the outputs from different

**[06:07]** combines the outputs from different

**[06:07]** combines the outputs from different tasks

**[06:09]** tasks

**[06:09]** tasks based on your replanning logic. Either

**[06:11]** based on your replanning logic. Either

**[06:11]** based on your replanning logic. Either you do replanning again or you just like

**[06:13]** you do replanning again or you just like

**[06:13]** you do replanning again or you just like terminate and give the response back to

**[06:16]** terminate and give the response back to

**[06:16]** terminate and give the response back to the user.

**[06:17]** the user.

**[06:18]** the user. Sometimes you also set some recussion

**[06:19]** Sometimes you also set some recussion

**[06:19]** Sometimes you also set some recussion limit so that your agent just like

**[06:21]** limit so that your agent just like

**[06:21]** limit so that your agent just like doesn't go into loop.

**[06:24]** doesn't go into loop.

**[06:24]** doesn't go into loop. On lang graph we are using each of these

**[06:27]** On lang graph we are using each of these

**[06:27]** On lang graph we are using each of these component as a nodes. So blueprint

**[06:29]** component as a nodes. So blueprint

**[06:29]** component as a nodes. So blueprint generator, planner, executor and joiner

**[06:32]** generator, planner, executor and joiner

**[06:32]** generator, planner, executor and joiner are all nodes on the langraph.

**[06:41]** When building this uh tools in in your

**[06:41]** When building this uh tools in in your enterprises around microservices,

**[06:43]** enterprises around microservices,

**[06:43]** enterprises around microservices, probably this is where you will spend

**[06:45]** probably this is where you will spend

**[06:45]** probably this is where you will spend most of your time.

**[06:47]** most of your time.

**[06:47]** most of your time. And it's important to consider how this

**[06:50]** And it's important to consider how this

**[06:50]** And it's important to consider how this relation between tools and microservices

**[06:53]** relation between tools and microservices

**[06:53]** relation between tools and microservices goes. And here the relationship is

**[06:55]** goes. And here the relationship is

**[06:56]** goes. And here the relationship is definitely not one to one or end to end.

**[06:57]** definitely not one to one or end to end.

**[06:57]** definitely not one to one or end to end. It's end to end. It's up to you how you


### [07:00 - 08:00]

**[07:00]** It's end to end. It's up to you how you

**[07:00]** It's end to end. It's up to you how you want to design your tools according to

**[07:03]** want to design your tools according to

**[07:03]** want to design your tools according to your microservices so that your agent

**[07:06]** your microservices so that your agent

**[07:06]** your microservices so that your agent knows how to use this tool. Perhaps this

**[07:08]** knows how to use this tool. Perhaps this

**[07:08]** knows how to use this tool. Perhaps this is like the most key point here that you

**[07:11]** is like the most key point here that you

**[07:11]** is like the most key point here that you need to make really put yourself into

**[07:13]** need to make really put yourself into

**[07:13]** need to make really put yourself into agent's shoes so that agent really

**[07:16]** agent's shoes so that agent really

**[07:16]** agent's shoes so that agent really understand what tool to use and it has

**[07:18]** understand what tool to use and it has

**[07:18]** understand what tool to use and it has that knowledge of your microservices.

**[07:22]** that knowledge of your microservices.

**[07:22]** that knowledge of your microservices. Always follow standard. I know MCP is

**[07:24]** Always follow standard. I know MCP is

**[07:24]** Always follow standard. I know MCP is everyone's favorite. So build the MCP

**[07:26]** everyone's favorite. So build the MCP

**[07:26]** everyone's favorite. So build the MCP tool server for your tools. And for

**[07:30]** tool server for your tools. And for

**[07:30]** tool server for your tools. And for providing the tool details just think

**[07:32]** providing the tool details just think

**[07:32]** providing the tool details just think from agent's point of view that you need

**[07:34]** from agent's point of view that you need

**[07:34]** from agent's point of view that you need to provide it tool purpose description

**[07:37]** to provide it tool purpose description

**[07:38]** to provide it tool purpose description and input output contracts. So tool

**[07:41]** and input output contracts. So tool

**[07:41]** and input output contracts. So tool purpose will help you what tools to be

**[07:43]** purpose will help you what tools to be

**[07:43]** purpose will help you what tools to be selected. Tool detail description will

**[07:46]** selected. Tool detail description will

**[07:46]** selected. Tool detail description will tell you when these tools need to be

**[07:48]** tell you when these tools need to be

**[07:48]** tell you when these tools need to be invoked and input output contracts will

**[07:50]** invoked and input output contracts will

**[07:50]** invoked and input output contracts will tell you how to use this tool. And

**[07:53]** tell you how to use this tool. And

**[07:53]** tell you how to use this tool. And lastly add some validation checks which

**[07:56]** lastly add some validation checks which

**[07:56]** lastly add some validation checks which acts as a break for your agent.


### [08:00 - 09:00]

**[08:02]** Now I would like to little bit zoom in

**[08:02]** Now I would like to little bit zoom in into this blueprint uh because this is

**[08:05]** into this blueprint uh because this is

**[08:05]** into this blueprint uh because this is like one of the key architecture change

**[08:07]** like one of the key architecture change

**[08:07]** like one of the key architecture change that we made. Uh blueprint is just a

**[08:10]** that we made. Uh blueprint is just a

**[08:10]** that we made. Uh blueprint is just a series of steps for workflow as per tool

**[08:12]** series of steps for workflow as per tool

**[08:12]** series of steps for workflow as per tool capabilities in natural language and

**[08:17]** capabilities in natural language and

**[08:17]** capabilities in natural language and it gets fed to planner. But why we are

**[08:19]** it gets fed to planner. But why we are

**[08:19]** it gets fed to planner. But why we are doing it? So what we realized was

**[08:23]** doing it? So what we realized was

**[08:23]** doing it? So what we realized was planner really gets cognitively uh

**[08:26]** planner really gets cognitively uh

**[08:26]** planner really gets cognitively uh loaded uh when you try to just put too

**[08:29]** loaded uh when you try to just put too

**[08:29]** loaded uh when you try to just put too much onto it. So introducing a blueprint

**[08:33]** much onto it. So introducing a blueprint

**[08:33]** much onto it. So introducing a blueprint which is just a natural language of

**[08:35]** which is just a natural language of

**[08:35]** which is just a natural language of breaking down of a task is very helpful

**[08:38]** breaking down of a task is very helpful

**[08:38]** breaking down of a task is very helpful but we also noticed that it brings lot

**[08:41]** but we also noticed that it brings lot

**[08:41]** but we also noticed that it brings lot of other benefits as well. For example,

**[08:44]** of other benefits as well. For example,

**[08:44]** of other benefits as well. For example, it achieves the final control over task

**[08:46]** it achieves the final control over task

**[08:46]** it achieves the final control over task planning. it limits the in context tool

**[08:49]** planning. it limits the in context tool

**[08:49]** planning. it limits the in context tool for the planner. So when blueprint you

**[08:52]** for the planner. So when blueprint you

**[08:52]** for the planner. So when blueprint you can select what tools to be need to be

**[08:55]** can select what tools to be need to be

**[08:55]** can select what tools to be need to be given to the planner and sometimes this

**[08:58]** given to the planner and sometimes this

**[08:58]** given to the planner and sometimes this uh planners has lot of tool description


### [09:00 - 10:00]

**[09:01]** uh planners has lot of tool description

**[09:01]** uh planners has lot of tool description and you run all sort of problems as

**[09:03]** and you run all sort of problems as

**[09:04]** and you run all sort of problems as context window limit and planner game uh

**[09:07]** context window limit and planner game uh

**[09:07]** context window limit and planner game uh getting very much overloaded. So using

**[09:10]** getting very much overloaded. So using

**[09:10]** getting very much overloaded. So using blueprint you can limit what tools

**[09:12]** blueprint you can limit what tools

**[09:12]** blueprint you can limit what tools really goes to the uh planner and thus

**[09:17]** really goes to the uh planner and thus

**[09:18]** really goes to the uh planner and thus uh it really helps in in the planning.

**[09:21]** uh it really helps in in the planning.

**[09:21]** uh it really helps in in the planning. It also helps interpreting the agentic

**[09:23]** It also helps interpreting the agentic

**[09:23]** It also helps interpreting the agentic behavior and lastly when you need to

**[09:26]** behavior and lastly when you need to

**[09:26]** behavior and lastly when you need to collaborate with nontechnical

**[09:28]** collaborate with nontechnical

**[09:28]** collaborate with nontechnical uh people it's like really helpful

**[09:31]** uh people it's like really helpful

**[09:31]** uh people it's like really helpful because natural language is less

**[09:32]** because natural language is less

**[09:32]** because natural language is less intimidating.

**[09:34]** intimidating.

**[09:34]** intimidating. Let's see a concrete example. So in

**[09:37]** Let's see a concrete example. So in

**[09:37]** Let's see a concrete example. So in financial research preparing for an uh

**[09:40]** financial research preparing for an uh

**[09:40]** financial research preparing for an uh company's earning call is a common

**[09:42]** company's earning call is a common

**[09:42]** company's earning call is a common workflow. So this is a very very

**[09:45]** workflow. So this is a very very

**[09:45]** workflow. So this is a very very simplified version of

**[09:47]** simplified version of

**[09:47]** simplified version of uh workflow of preparing for a company's

**[09:50]** uh workflow of preparing for a company's

**[09:50]** uh workflow of preparing for a company's earning call. And for example we are

**[09:51]** earning call. And for example we are

**[09:51]** earning call. And for example we are showing you preparing for NVIDIA as an

**[09:53]** showing you preparing for NVIDIA as an

**[09:53]** showing you preparing for NVIDIA as an call.

**[09:55]** call.

**[09:55]** call. Now you can see in the blueprint there

**[09:57]** Now you can see in the blueprint there

**[09:57]** Now you can see in the blueprint there is a tool and there is task and in the

**[09:59]** is a tool and there is task and in the


### [10:00 - 11:00]

**[10:00]** is a tool and there is task and in the plan there is a tool and the function

**[10:01]** plan there is a tool and the function

**[10:01]** plan there is a tool and the function call. So how does it look in in the

**[10:05]** call. So how does it look in in the

**[10:05]** call. So how does it look in in the blueprint is you have two tools and then

**[10:08]** blueprint is you have two tools and then

**[10:08]** blueprint is you have two tools and then you are first step as summarizing the

**[10:10]** you are first step as summarizing the

**[10:10]** you are first step as summarizing the NVIDIA's previous earning call and the

**[10:12]** NVIDIA's previous earning call and the

**[10:12]** NVIDIA's previous earning call and the next step is retrieval gathering some of

**[10:14]** next step is retrieval gathering some of

**[10:14]** next step is retrieval gathering some of the financial data from uh for NVDI and

**[10:17]** the financial data from uh for NVDI and

**[10:17]** the financial data from uh for NVDI and then your reasoning suggesting some

**[10:19]** then your reasoning suggesting some

**[10:19]** then your reasoning suggesting some questions for the earning call and

**[10:20]** questions for the earning call and

**[10:20]** questions for the earning call and finally reporting uh generate a

**[10:23]** finally reporting uh generate a

**[10:23]** finally reporting uh generate a comprehensive report from the all the

**[10:24]** comprehensive report from the all the

**[10:24]** comprehensive report from the all the information

**[10:26]** information

**[10:26]** information and there are corresponding function

**[10:27]** and there are corresponding function

**[10:27]** and there are corresponding function calls and as you can see context is

**[10:29]** calls and as you can see context is

**[10:29]** calls and as you can see context is being fed from uh task

**[10:37]** A a concrete uh example of the response

**[10:37]** A a concrete uh example of the response is before you implement agentic workflow

**[10:39]** is before you implement agentic workflow

**[10:39]** is before you implement agentic workflow the response is pretty much vanilla but

**[10:42]** the response is pretty much vanilla but

**[10:42]** the response is pretty much vanilla but after this it can easily capture your

**[10:45]** after this it can easily capture your

**[10:45]** after this it can easily capture your workflow and give a very structured

**[10:47]** workflow and give a very structured

**[10:47]** workflow and give a very structured response.

**[10:48]** response.

**[10:48]** response. So whatever we talked about none of this

**[10:51]** So whatever we talked about none of this

**[10:51]** So whatever we talked about none of this will really work without writing a

**[10:53]** will really work without writing a

**[10:53]** will really work without writing a proper evals. So always make sure to

**[10:57]** proper evals. So always make sure to

**[10:57]** proper evals. So always make sure to invest and build and maintain your eval

**[10:59]** invest and build and maintain your eval

**[10:59]** invest and build and maintain your eval framework. You should have at least


### [11:00 - 12:00]

**[11:01]** framework. You should have at least

**[11:01]** framework. You should have at least component and end to-end evals.

**[11:04]** component and end to-end evals.

**[11:04]** component and end to-end evals. You should really use the correct

**[11:06]** You should really use the correct

**[11:06]** You should really use the correct techniques like codebased LMS judge

**[11:08]** techniques like codebased LMS judge

**[11:08]** techniques like codebased LMS judge human in the loop and more importantly

**[11:11]** human in the loop and more importantly

**[11:12]** human in the loop and more importantly write evals for metrics that you really

**[11:14]** write evals for metrics that you really

**[11:14]** write evals for metrics that you really care for. Aspect bus eval is something

**[11:17]** care for. Aspect bus eval is something

**[11:17]** care for. Aspect bus eval is something like we should really uh think about and

**[11:20]** like we should really uh think about and

**[11:20]** like we should really uh think about and for example for blueprint

**[11:23]** for example for blueprint

**[11:23]** for example for blueprint uh you can check an aspect like how many

**[11:26]** uh you can check an aspect like how many

**[11:26]** uh you can check an aspect like how many uh blueprint whether resembles a golden

**[11:27]** uh blueprint whether resembles a golden

**[11:27]** uh blueprint whether resembles a golden blueprint or not and you can use LM as a

**[11:30]** blueprint or not and you can use LM as a

**[11:30]** blueprint or not and you can use LM as a judge. If you want to see whether tools

**[11:33]** judge. If you want to see whether tools

**[11:33]** judge. If you want to see whether tools are selected correct or not you should

**[11:34]** are selected correct or not you should

**[11:34]** are selected correct or not you should leverage code based evals.

**[11:37]** leverage code based evals.

**[11:37]** leverage code based evals. If you want to check whether plan is in

**[11:39]** If you want to check whether plan is in

**[11:39]** If you want to check whether plan is in line with the blueprint or not, LLM as a

**[11:41]** line with the blueprint or not, LLM as a

**[11:41]** line with the blueprint or not, LLM as a judge probably the right technique. And

**[11:44]** judge probably the right technique. And

**[11:44]** judge probably the right technique. And for some cases, leveraging human in the

**[11:47]** for some cases, leveraging human in the

**[11:47]** for some cases, leveraging human in the loop is good because report formatting

**[11:49]** loop is good because report formatting

**[11:50]** loop is good because report formatting uh that's the best approach to deal with

**[11:52]** uh that's the best approach to deal with

**[11:52]** uh that's the best approach to deal with report formatting.

**[11:55]** report formatting.

**[11:55]** report formatting. So when not to use agentic workflows. So

**[11:58]** So when not to use agentic workflows. So

**[11:58]** So when not to use agentic workflows. So in some cases definitely agentic

**[11:59]** in some cases definitely agentic

**[11:59]** in some cases definitely agentic workflow doesn't make sense. In case of


### [12:00 - 13:00]

**[12:01]** workflow doesn't make sense. In case of

**[12:01]** workflow doesn't make sense. In case of fixed and repetitive task just probably

**[12:03]** fixed and repetitive task just probably

**[12:03]** fixed and repetitive task just probably go for ETL pipelines.

**[12:06]** go for ETL pipelines.

**[12:06]** go for ETL pipelines. If your workflow cannot be really

**[12:07]** If your workflow cannot be really

**[12:07]** If your workflow cannot be really captured, uh you cannot really capture

**[12:09]** captured, uh you cannot really capture

**[12:09]** captured, uh you cannot really capture use case in workflows, agentic workflows

**[12:11]** use case in workflows, agentic workflows

**[12:12]** use case in workflows, agentic workflows are probably not worth and if

**[12:14]** are probably not worth and if

**[12:14]** are probably not worth and if deterministic outcome is paramount in

**[12:16]** deterministic outcome is paramount in

**[12:16]** deterministic outcome is paramount in cases of strict compliance and safety

**[12:19]** cases of strict compliance and safety

**[12:19]** cases of strict compliance and safety critical context, uh you should probably

**[12:21]** critical context, uh you should probably

**[12:21]** critical context, uh you should probably should not go with agentic workflow and

**[12:24]** should not go with agentic workflow and

**[12:24]** should not go with agentic workflow and in case of low latency and cost

**[12:26]** in case of low latency and cost

**[12:26]** in case of low latency and cost environment also uh you should probably

**[12:29]** environment also uh you should probably

**[12:29]** environment also uh you should probably try to avoid agentic workflow.

**[12:32]** try to avoid agentic workflow.

**[12:32]** try to avoid agentic workflow. So wrapping up some learnings um start

**[12:36]** So wrapping up some learnings um start

**[12:36]** So wrapping up some learnings um start with simple blueprints work way work uh

**[12:39]** with simple blueprints work way work uh

**[12:39]** with simple blueprints work way work uh work your way way up uh building a

**[12:41]** work your way way up uh building a

**[12:42]** work your way way up uh building a complex rack system for the blueprints

**[12:45]** complex rack system for the blueprints

**[12:45]** complex rack system for the blueprints use blueprint to reduce the in context

**[12:48]** use blueprint to reduce the in context

**[12:48]** use blueprint to reduce the in context uh tools and provide the high level plan

**[12:50]** uh tools and provide the high level plan

**[12:50]** uh tools and provide the high level plan to the planner

**[12:52]** to the planner

**[12:52]** to the planner design tools from agent point of view u

**[12:55]** design tools from agent point of view u

**[12:55]** design tools from agent point of view u always aim for the tool usage simplicity

**[12:58]** always aim for the tool usage simplicity

**[12:58]** always aim for the tool usage simplicity implement safety guardrails


### [13:00 - 14:00]

**[13:01]** implement safety guardrails

**[13:01]** implement safety guardrails and eval observability and all the good

**[13:05]** and eval observability and all the good

**[13:05]** and eval observability and all the good software engineering. Uh that should uh

**[13:08]** software engineering. Uh that should uh

**[13:08]** software engineering. Uh that should uh help you a lot.

**[13:11]** help you a lot.

**[13:11]** help you a lot. And from the whole uh presentation, the

**[13:13]** And from the whole uh presentation, the

**[13:13]** And from the whole uh presentation, the key takeaways are agentic workflow is

**[13:15]** key takeaways are agentic workflow is

**[13:15]** key takeaways are agentic workflow is planned and run by agent. Agentic

**[13:18]** planned and run by agent. Agentic

**[13:18]** planned and run by agent. Agentic workflows bring the reliability

**[13:21]** workflows bring the reliability

**[13:21]** workflows bring the reliability at scale and planning by subgoal

**[13:24]** at scale and planning by subgoal

**[13:24]** at scale and planning by subgoal division is a key design pattern. Plan

**[13:27]** division is a key design pattern. Plan

**[13:27]** division is a key design pattern. Plan and execute is a key agentic

**[13:28]** and execute is a key agentic

**[13:28]** and execute is a key agentic architecture.

**[13:30]** architecture.

**[13:30]** architecture. and build your tools to complement your

**[13:34]** and build your tools to complement your

**[13:34]** and build your tools to complement your microservices.

**[13:35]** microservices.

**[13:36]** microservices. Always try to leverage your

**[13:37]** Always try to leverage your

**[13:37]** Always try to leverage your microservices in the tools and modify

**[13:40]** microservices in the tools and modify

**[13:40]** microservices in the tools and modify your architecture to solve the problems.

**[13:43]** your architecture to solve the problems.

**[13:43]** your architecture to solve the problems. Don't really shy away from changing

**[13:45]** Don't really shy away from changing

**[13:46]** Don't really shy away from changing taking research paper and experimenting

**[13:48]** taking research paper and experimenting

**[13:48]** taking research paper and experimenting on it. And finally, treat your evals

**[13:51]** on it. And finally, treat your evals

**[13:51]** on it. And finally, treat your evals like first class citizen.

**[13:54]** like first class citizen.

**[13:54]** like first class citizen. And with that, thank you very much for

**[13:56]** And with that, thank you very much for

**[13:56]** And with that, thank you very much for your time.


### [14:00 - 15:00]

**[14:02]** All right.

**[14:02]** All right. Uh, thank you. Any questions? We have a

**[14:05]** Uh, thank you. Any questions? We have a

**[14:05]** Uh, thank you. Any questions? We have a little bit of time to spare.

**[14:08]** little bit of time to spare.

**[14:08]** little bit of time to spare. I have a question. Um,

**[14:11]** I have a question. Um,

**[14:11]** I have a question. Um, do you on have um in top of our mind any

**[14:15]** do you on have um in top of our mind any

**[14:15]** do you on have um in top of our mind any like a GitHub project or reference that

**[14:18]** like a GitHub project or reference that

**[14:18]** like a GitHub project or reference that we can follow?

**[14:19]** we can follow?

**[14:20]** we can follow? Sure. Sure. So if you just go back here

**[14:23]** Sure. Sure. So if you just go back here

**[14:23]** Sure. Sure. So if you just go back here um I kind of shared some of the

**[14:28]** um I kind of shared some of the

**[14:28]** um I kind of shared some of the links um

**[14:31]** links um

**[14:31]** links um for the lang chain it it should have all

**[14:33]** for the lang chain it it should have all

**[14:33]** for the lang chain it it should have all the code for these research paper and

**[14:36]** the code for these research paper and

**[14:36]** the code for these research paper and that's probably the most you know best

**[14:39]** that's probably the most you know best

**[14:39]** that's probably the most you know best place to start with this plan and

**[14:41]** place to start with this plan and

**[14:41]** place to start with this plan and execute kind of agents.

**[14:42]** execute kind of agents.

**[14:42]** execute kind of agents. Thank you.

**[14:43]** Thank you.

**[14:43]** Thank you. Yeah.

**[14:50]** Any other questions?

**[14:50]** Any other questions? Uh all right. Um I guess one question I

**[14:52]** Uh all right. Um I guess one question I

**[14:52]** Uh all right. Um I guess one question I would have for you is

**[14:54]** would have for you is

**[14:54]** would have for you is the when you talk about MCP and other

**[14:57]** the when you talk about MCP and other

**[14:57]** the when you talk about MCP and other forms of orchestration, what do you

**[14:59]** forms of orchestration, what do you

**[14:59]** forms of orchestration, what do you foresee being the the primary method of


### [15:00 - 16:00]

**[15:01]** foresee being the the primary method of

**[15:01]** foresee being the the primary method of orchestration going forward? Is it going

**[15:03]** orchestration going forward? Is it going

**[15:03]** orchestration going forward? Is it going to be langraph or some other?

**[15:07]** to be langraph or some other?

**[15:07]** to be langraph or some other? Yeah, I think the answer is probably

**[15:09]** Yeah, I think the answer is probably

**[15:09]** Yeah, I think the answer is probably like everything. MCP you use it so that

**[15:12]** like everything. MCP you use it so that

**[15:12]** like everything. MCP you use it so that you provide a standard across the arc

**[15:15]** you provide a standard across the arc

**[15:15]** you provide a standard across the arc and MCP will really help for

**[15:17]** and MCP will really help for

**[15:17]** and MCP will really help for organization to you know build once use

**[15:19]** organization to you know build once use

**[15:19]** organization to you know build once use it everywhere. uh you can have oftenimes

**[15:22]** it everywhere. uh you can have oftenimes

**[15:22]** it everywhere. uh you can have oftenimes in organizations we see that uh people

**[15:25]** in organizations we see that uh people

**[15:25]** in organizations we see that uh people just like trying to just use this

**[15:27]** just like trying to just use this

**[15:27]** just like trying to just use this functionality in different AI apps but

**[15:29]** functionality in different AI apps but

**[15:29]** functionality in different AI apps but if you can build an MCP around it you

**[15:32]** if you can build an MCP around it you

**[15:32]** if you can build an MCP around it you can keep using it and obviously for

**[15:34]** can keep using it and obviously for

**[15:34]** can keep using it and obviously for orchestration langraph is great and

**[15:37]** orchestration langraph is great and

**[15:37]** orchestration langraph is great and whatever the other tools that you find

**[15:39]** whatever the other tools that you find

**[15:39]** whatever the other tools that you find to solve your problem that will be also

**[15:41]** to solve your problem that will be also

**[15:41]** to solve your problem that will be also u so the answer is probably there will

**[15:43]** u so the answer is probably there will

**[15:43]** u so the answer is probably there will be like multiple things that is useful

**[15:45]** be like multiple things that is useful

**[15:45]** be like multiple things that is useful it depends on your use case what is the

**[15:48]** it depends on your use case what is the

**[15:48]** it depends on your use case what is the uh most optimal framework that you want

**[15:49]** uh most optimal framework that you want

**[15:49]** uh most optimal framework that you want to use

**[15:50]** to use

**[15:50]** to use amazing Thank you so much, Yuri.


