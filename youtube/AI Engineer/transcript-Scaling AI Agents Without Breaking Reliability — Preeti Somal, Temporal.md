# Scaling AI Agents Without Breaking Reliability — Preeti Somal, Temporal

**Video URL:** https://www.youtube.com/watch?v=1izYWsokr9s

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Uh my name is Prii and I am part of the

**[00:17]** Uh my name is Prii and I am part of the engineering team at Temporal. How many

**[00:19]** engineering team at Temporal. How many

**[00:19]** engineering team at Temporal. How many people here have heard of Temporal?

**[00:22]** people here have heard of Temporal?

**[00:22]** people here have heard of Temporal? Perfect. Great. So Temporal is the

**[00:24]** Perfect. Great. So Temporal is the

**[00:24]** Perfect. Great. So Temporal is the company that takes reliability

**[00:27]** company that takes reliability

**[00:27]** company that takes reliability incredibly seriously. so seriously that

**[00:29]** incredibly seriously. so seriously that

**[00:30]** incredibly seriously. so seriously that our mascot is a tardigrade. Does anybody

**[00:33]** our mascot is a tardigrade. Does anybody

**[00:33]** our mascot is a tardigrade. Does anybody know what a tardigrade is? Yes, some

**[00:37]** know what a tardigrade is? Yes, some

**[00:37]** know what a tardigrade is? Yes, some folks. Well, it is what is also called a

**[00:39]** folks. Well, it is what is also called a

**[00:39]** folks. Well, it is what is also called a water bear and is the most resilient

**[00:43]** water bear and is the most resilient

**[00:43]** water bear and is the most resilient animal known to humankind. And so that's

**[00:45]** animal known to humankind. And so that's

**[00:45]** animal known to humankind. And so that's how seriously we take reliability.

**[00:48]** how seriously we take reliability.

**[00:48]** how seriously we take reliability. Definitely stop by our booth for some

**[00:49]** Definitely stop by our booth for some

**[00:50]** Definitely stop by our booth for some stickers and some pins to just show how

**[00:52]** stickers and some pins to just show how

**[00:52]** stickers and some pins to just show how much you care about reliability.

**[00:55]** much you care about reliability.

**[00:55]** much you care about reliability. All right. So, my goal in the next 17

**[00:58]** All right. So, my goal in the next 17

**[00:58]** All right. So, my goal in the next 17 minutes or so is to convince all of you


### [01:00 - 02:00]

**[01:01]** minutes or so is to convince all of you

**[01:01]** minutes or so is to convince all of you that temporal is the right choice of

**[01:04]** that temporal is the right choice of

**[01:04]** that temporal is the right choice of platform as you go out to build agentic

**[01:07]** platform as you go out to build agentic

**[01:07]** platform as you go out to build agentic AI applications. So, let's dive right

**[01:10]** AI applications. So, let's dive right

**[01:10]** AI applications. So, let's dive right in. We've heard a lot about how uh you

**[01:14]** in. We've heard a lot about how uh you

**[01:14]** in. We've heard a lot about how uh you know agents are just software. However,

**[01:17]** know agents are just software. However,

**[01:17]** know agents are just software. However, they are complex distributed systems.

**[01:21]** they are complex distributed systems.

**[01:21]** they are complex distributed systems. They need to cope with LLMs

**[01:24]** They need to cope with LLMs

**[01:24]** They need to cope with LLMs and they must scale and provide

**[01:26]** and they must scale and provide

**[01:26]** and they must scale and provide durability and reliability. Otherwise,

**[01:28]** durability and reliability. Otherwise,

**[01:28]** durability and reliability. Otherwise, no one's going to trust your agent. Uh,

**[01:30]** no one's going to trust your agent. Uh,

**[01:30]** no one's going to trust your agent. Uh, you know, we can build like really cool

**[01:32]** you know, we can build like really cool

**[01:32]** you know, we can build like really cool stuff, but if it doesn't work, nobody's

**[01:34]** stuff, but if it doesn't work, nobody's

**[01:34]** stuff, but if it doesn't work, nobody's using it.

**[01:41]** We also know that complex systems need

**[01:41]** We also know that complex systems need orchestration. uh Dex used the word

**[01:43]** orchestration. uh Dex used the word

**[01:43]** orchestration. uh Dex used the word workflow a few times and essentially at

**[01:46]** workflow a few times and essentially at

**[01:46]** workflow a few times and essentially at the core of Agentic AI applications is a

**[01:49]** the core of Agentic AI applications is a

**[01:49]** the core of Agentic AI applications is a complicated workflow uh that

**[01:51]** complicated workflow uh that

**[01:51]** complicated workflow uh that orchestrates multiple processes

**[01:55]** orchestrates multiple processes

**[01:55]** orchestrates multiple processes uh needs to handle state potentially

**[01:57]** uh needs to handle state potentially

**[01:57]** uh needs to handle state potentially over long periods of time. There needs


### [02:00 - 03:00]

**[02:00]** over long periods of time. There needs

**[02:00]** over long periods of time. There needs to be human interaction for approvals or

**[02:03]** to be human interaction for approvals or

**[02:03]** to be human interaction for approvals or other reasons and of course they need to

**[02:06]** other reasons and of course they need to

**[02:06]** other reasons and of course they need to be able to be uh able to run in parallel

**[02:09]** be able to be uh able to run in parallel

**[02:10]** be able to be uh able to run in parallel for efficiency call tools. There's just

**[02:13]** for efficiency call tools. There's just

**[02:13]** for efficiency call tools. There's just a lot of things going on. You know how

**[02:15]** a lot of things going on. You know how

**[02:15]** a lot of things going on. You know how how many of you feel like building

**[02:16]** how many of you feel like building

**[02:16]** how many of you feel like building agents is really simple. You're just

**[02:18]** agents is really simple. You're just

**[02:18]** agents is really simple. You're just calling one switch statement, right?

**[02:21]** calling one switch statement, right?

**[02:21]** calling one switch statement, right? Yeah. I mean there's a lot of things

**[02:22]** Yeah. I mean there's a lot of things

**[02:22]** Yeah. I mean there's a lot of things that are interacting here and how can

**[02:25]** that are interacting here and how can

**[02:25]** that are interacting here and how can you actually keep track of that? make

**[02:27]** you actually keep track of that? make

**[02:27]** you actually keep track of that? make sure it's running reliably as well as

**[02:29]** sure it's running reliably as well as

**[02:29]** sure it's running reliably as well as tracing and looking at the visibility of

**[02:32]** tracing and looking at the visibility of

**[02:32]** tracing and looking at the visibility of all of these pieces.

**[02:34]** all of these pieces.

**[02:34]** all of these pieces. And again, you know, these systems are

**[02:36]** And again, you know, these systems are

**[02:36]** And again, you know, these systems are inherently unreliable. How many of you

**[02:39]** inherently unreliable. How many of you

**[02:39]** inherently unreliable. How many of you have called an LLM and it succeeded 100%

**[02:42]** have called an LLM and it succeeded 100%

**[02:42]** have called an LLM and it succeeded 100% of the time? Yeah, nobody's raising

**[02:46]** of the time? Yeah, nobody's raising

**[02:46]** of the time? Yeah, nobody's raising their hands. So, we've dealt with this

**[02:47]** their hands. So, we've dealt with this

**[02:48]** their hands. So, we've dealt with this as you're building these applications.

**[02:49]** as you're building these applications.

**[02:49]** as you're building these applications. You are seeing inherently how unreliable

**[02:53]** You are seeing inherently how unreliable

**[02:53]** You are seeing inherently how unreliable some of the tool chain here is.

**[02:57]** some of the tool chain here is.

**[02:57]** some of the tool chain here is. and then uh you know difficult to debug

**[02:59]** and then uh you know difficult to debug

**[02:59]** and then uh you know difficult to debug and test and Alex has been talking about


### [03:00 - 04:00]

**[03:01]** and test and Alex has been talking about

**[03:01]** and test and Alex has been talking about agent ops being kind of built around

**[03:03]** agent ops being kind of built around

**[03:03]** agent ops being kind of built around this but clearly the insight into what's

**[03:06]** this but clearly the insight into what's

**[03:06]** this but clearly the insight into what's happening has been incredibly hard to

**[03:09]** happening has been incredibly hard to

**[03:09]** happening has been incredibly hard to get. It's been incredibly difficult to

**[03:12]** get. It's been incredibly difficult to

**[03:12]** get. It's been incredibly difficult to test this in pre-production.

**[03:15]** test this in pre-production.

**[03:15]** test this in pre-production. Well, the interesting thing here is that

**[03:17]** Well, the interesting thing here is that

**[03:17]** Well, the interesting thing here is that these problems have existed for some

**[03:20]** these problems have existed for some

**[03:20]** these problems have existed for some time in building complex distributed

**[03:22]** time in building complex distributed

**[03:22]** time in building complex distributed systems and temporal is a company that

**[03:26]** systems and temporal is a company that

**[03:26]** systems and temporal is a company that was founded around solving these

**[03:29]** was founded around solving these

**[03:29]** was founded around solving these problems. Our mission really is to

**[03:31]** problems. Our mission really is to

**[03:31]** problems. Our mission really is to outsource the reliability and

**[03:33]** outsource the reliability and

**[03:33]** outsource the reliability and scalability parts of building a complex

**[03:36]** scalability parts of building a complex

**[03:36]** scalability parts of building a complex distributed

**[03:38]** distributed

**[03:38]** distributed uh uh application seamlessly. So again

**[03:41]** uh uh application seamlessly. So again

**[03:41]** uh uh application seamlessly. So again you can focus on the hard parts of

**[03:43]** you can focus on the hard parts of

**[03:43]** you can focus on the hard parts of writing your business logic. The way

**[03:46]** writing your business logic. The way

**[03:46]** writing your business logic. The way that temporal works is that we we've

**[03:49]** that temporal works is that we we've

**[03:49]** that temporal works is that we we've built uh language idiomatic SDKs. We've

**[03:53]** built uh language idiomatic SDKs. We've

**[03:53]** built uh language idiomatic SDKs. We've the languages are available there and in

**[03:56]** the languages are available there and in

**[03:56]** the languages are available there and in in fact one of the fun facts here is

**[03:58]** in fact one of the fun facts here is

**[03:58]** in fact one of the fun facts here is that Python has overtaken all the other


### [04:00 - 05:00]

**[04:01]** that Python has overtaken all the other

**[04:01]** that Python has overtaken all the other languages in the month of January and

**[04:04]** languages in the month of January and

**[04:04]** languages in the month of January and and that sort of is showing how much of

**[04:06]** and that sort of is showing how much of

**[04:06]** and that sort of is showing how much of Python is being used in building these

**[04:08]** Python is being used in building these

**[04:08]** Python is being used in building these applications.

**[04:10]** applications.

**[04:10]** applications. We handle all the plumbing code for you,

**[04:13]** We handle all the plumbing code for you,

**[04:13]** We handle all the plumbing code for you, making sure that every process executes

**[04:15]** making sure that every process executes

**[04:15]** making sure that every process executes reliably and providing you guardrails.

**[04:19]** reliably and providing you guardrails.

**[04:19]** reliably and providing you guardrails. And this is a battle tested product.

**[04:21]** And this is a battle tested product.

**[04:22]** And this is a battle tested product. Temporal has been in production for over

**[04:24]** Temporal has been in production for over

**[04:24]** Temporal has been in production for over a decade. Temporal is used in mission

**[04:28]** a decade. Temporal is used in mission

**[04:28]** a decade. Temporal is used in mission critical applications. These are just a

**[04:30]** critical applications. These are just a

**[04:30]** critical applications. These are just a few examples of our customers using

**[04:33]** few examples of our customers using

**[04:33]** few examples of our customers using temporal in production today. So we feel

**[04:36]** temporal in production today. So we feel

**[04:36]** temporal in production today. So we feel that using temporal for running these

**[04:39]** that using temporal for running these

**[04:39]** that using temporal for running these for building your agentic uh AI

**[04:41]** for building your agentic uh AI

**[04:41]** for building your agentic uh AI applications gives you reliability

**[04:44]** applications gives you reliability

**[04:44]** applications gives you reliability out of box. But you know I can stand

**[04:47]** out of box. But you know I can stand

**[04:47]** out of box. But you know I can stand here and talk all day about it. You you

**[04:49]** here and talk all day about it. You you

**[04:49]** here and talk all day about it. You you probably don't believe me. Uh so we have

**[04:52]** probably don't believe me. Uh so we have

**[04:52]** probably don't believe me. Uh so we have some customer quotes here that will help

**[04:54]** some customer quotes here that will help

**[04:54]** some customer quotes here that will help you understand this. Uh, one of them is

**[04:57]** you understand this. Uh, one of them is

**[04:57]** you understand this. Uh, one of them is from a customer called Dust that is

**[04:59]** from a customer called Dust that is

**[04:59]** from a customer called Dust that is building their agents on top of Temporal


### [05:00 - 06:00]

**[05:01]** building their agents on top of Temporal

**[05:01]** building their agents on top of Temporal and the other is a company you may have

**[05:04]** and the other is a company you may have

**[05:04]** and the other is a company you may have heard of that recently talked about the

**[05:07]** heard of that recently talked about the

**[05:07]** heard of that recently talked about the tech stack they use and Temporal is very

**[05:10]** tech stack they use and Temporal is very

**[05:10]** tech stack they use and Temporal is very clearly featured there as well.

**[05:14]** clearly featured there as well.

**[05:14]** clearly featured there as well. We also have a number of use cases

**[05:16]** We also have a number of use cases

**[05:16]** We also have a number of use cases published. So, Gorgeous for instance is

**[05:18]** published. So, Gorgeous for instance is

**[05:18]** published. So, Gorgeous for instance is using AI agents today in production

**[05:23]** using AI agents today in production

**[05:23]** using AI agents today in production built on temporal. This is the company

**[05:25]** built on temporal. This is the company

**[05:25]** built on temporal. This is the company that does customer service for brands

**[05:27]** that does customer service for brands

**[05:27]** that does customer service for brands like Reebok or Timbuktu or Glossier.

**[05:31]** like Reebok or Timbuktu or Glossier.

**[05:31]** like Reebok or Timbuktu or Glossier. These are all household names. And and

**[05:34]** These are all household names. And and

**[05:34]** These are all household names. And and the reason I'm bringing this up is just

**[05:35]** the reason I'm bringing this up is just

**[05:36]** the reason I'm bringing this up is just to help you understand that customers

**[05:39]** to help you understand that customers

**[05:39]** to help you understand that customers are today running agents on Temporal at

**[05:42]** are today running agents on Temporal at

**[05:42]** are today running agents on Temporal at scale in production. And what's this

**[05:46]** scale in production. And what's this

**[05:46]** scale in production. And what's this what what temporal is bringing to them

**[05:48]** what what temporal is bringing to them

**[05:48]** what what temporal is bringing to them is incredible agility and speed because

**[05:51]** is incredible agility and speed because

**[05:51]** is incredible agility and speed because they can focus on writing their business

**[05:54]** they can focus on writing their business

**[05:54]** they can focus on writing their business logic and don't need to worry about

**[05:56]** logic and don't need to worry about

**[05:56]** logic and don't need to worry about reliability. The reason I put up the

**[05:59]** reliability. The reason I put up the

**[05:59]** reliability. The reason I put up the payments example here is to show you how


### [06:00 - 07:00]

**[06:02]** payments example here is to show you how

**[06:02]** payments example here is to show you how missionritical some of the workloads

**[06:05]** missionritical some of the workloads

**[06:05]** missionritical some of the workloads that are running on temporal are. And

**[06:08]** that are running on temporal are. And

**[06:08]** that are running on temporal are. And finally, you know, some more quotes here

**[06:10]** finally, you know, some more quotes here

**[06:10]** finally, you know, some more quotes here from customers, developers using

**[06:13]** from customers, developers using

**[06:13]** from customers, developers using temporal around building agent

**[06:15]** temporal around building agent

**[06:15]** temporal around building agent applications. I hope some of this is

**[06:17]** applications. I hope some of this is

**[06:17]** applications. I hope some of this is resonating in terms of the issues that

**[06:19]** resonating in terms of the issues that

**[06:19]** resonating in terms of the issues that you are seeing as well as you're going

**[06:21]** you are seeing as well as you're going

**[06:21]** you are seeing as well as you're going out and building these applications.

**[06:25]** out and building these applications.

**[06:25]** out and building these applications. All right, let's talk a little bit about

**[06:27]** All right, let's talk a little bit about

**[06:27]** All right, let's talk a little bit about architecture and code because no talk

**[06:29]** architecture and code because no talk

**[06:29]** architecture and code because no talk here can be complete if we don't talk

**[06:31]** here can be complete if we don't talk

**[06:31]** here can be complete if we don't talk architecture and code, right? All right,

**[06:34]** architecture and code, right? All right,

**[06:34]** architecture and code, right? All right, I was hoping I would get some clap. So

**[06:36]** I was hoping I would get some clap. So

**[06:36]** I was hoping I would get some clap. So let's get this going.

**[06:39]** let's get this going.

**[06:39]** let's get this going. All right.

**[06:41]** All right.

**[06:41]** All right. So this is this is an example of an

**[06:43]** So this is this is an example of an

**[06:43]** So this is this is an example of an architecture before temporal. What what

**[06:46]** architecture before temporal. What what

**[06:46]** architecture before temporal. What what we're seeing here is there is a lot of

**[06:50]** we're seeing here is there is a lot of

**[06:50]** we're seeing here is there is a lot of interaction and error handling that

**[06:53]** interaction and error handling that

**[06:53]** interaction and error handling that developers are being forced to code. And

**[06:56]** developers are being forced to code. And

**[06:56]** developers are being forced to code. And when you use code using temporal

**[06:58]** when you use code using temporal

**[06:58]** when you use code using temporal essentially we can abstract all of that


### [07:00 - 08:00]

**[07:00]** essentially we can abstract all of that

**[07:00]** essentially we can abstract all of that out into this concept of a workflow. A

**[07:04]** out into this concept of a workflow. A

**[07:04]** out into this concept of a workflow. A workflow is something that you write.

**[07:06]** workflow is something that you write.

**[07:06]** workflow is something that you write. This is this is very much a developer

**[07:09]** This is this is very much a developer

**[07:09]** This is this is very much a developer focused tool. This is not a tool that a

**[07:11]** focused tool. This is not a tool that a

**[07:11]** focused tool. This is not a tool that a business user or a non-technical per

**[07:13]** business user or a non-technical per

**[07:13]** business user or a non-technical per person would use. This is a developer

**[07:16]** person would use. This is a developer

**[07:16]** person would use. This is a developer going in and coding and building their

**[07:18]** going in and coding and building their

**[07:18]** going in and coding and building their applications using these SDKs around the

**[07:22]** applications using these SDKs around the

**[07:22]** applications using these SDKs around the concept of a workflow abstraction. And

**[07:25]** concept of a workflow abstraction. And

**[07:25]** concept of a workflow abstraction. And at the end of the day when you think

**[07:27]** at the end of the day when you think

**[07:27]** at the end of the day when you think about agents you essentially are just

**[07:29]** about agents you essentially are just

**[07:29]** about agents you essentially are just orchestrating

**[07:31]** orchestrating

**[07:31]** orchestrating a number of pieces around the

**[07:33]** a number of pieces around the

**[07:33]** a number of pieces around the interaction the large language models

**[07:36]** interaction the large language models

**[07:36]** interaction the large language models the chat history database and the tools

**[07:39]** the chat history database and the tools

**[07:39]** the chat history database and the tools right these are are the key abstractions

**[07:41]** right these are are the key abstractions

**[07:41]** right these are are the key abstractions that are in play and you're

**[07:43]** that are in play and you're

**[07:43]** that are in play and you're orchestrating that using temporal.

**[07:47]** orchestrating that using temporal.

**[07:47]** orchestrating that using temporal. What's the impact? You know, everybody's

**[07:49]** What's the impact? You know, everybody's

**[07:49]** What's the impact? You know, everybody's going to tell you they've got the best

**[07:50]** going to tell you they've got the best

**[07:50]** going to tell you they've got the best platform here, but what what is the

**[07:53]** platform here, but what what is the

**[07:53]** platform here, but what what is the impact for engineers? What we really are

**[07:56]** impact for engineers? What we really are

**[07:56]** impact for engineers? What we really are able to do is accelerate development.


### [08:00 - 09:00]

**[08:00]** able to do is accelerate development.

**[08:00]** able to do is accelerate development. And you what you can do is take temporal

**[08:03]** And you what you can do is take temporal

**[08:03]** And you what you can do is take temporal and you can put applications out in

**[08:06]** and you can put applications out in

**[08:06]** and you can put applications out in production in weeks. We've had customers

**[08:09]** production in weeks. We've had customers

**[08:09]** production in weeks. We've had customers with case studies where we've sped up

**[08:11]** with case studies where we've sped up

**[08:11]** with case studies where we've sped up their ve feature delivery velocity by

**[08:14]** their ve feature delivery velocity by

**[08:14]** their ve feature delivery velocity by over 6x once they've started using

**[08:17]** over 6x once they've started using

**[08:17]** over 6x once they've started using temporal. You can reach greater scale.

**[08:20]** temporal. You can reach greater scale.

**[08:20]** temporal. You can reach greater scale. Um, one of our customers is a consumer

**[08:24]** Um, one of our customers is a consumer

**[08:24]** Um, one of our customers is a consumer application that is scaling with events

**[08:27]** application that is scaling with events

**[08:27]** application that is scaling with events and and they don't need to worry about

**[08:29]** and and they don't need to worry about

**[08:29]** and and they don't need to worry about handling any of that scale logic at all.

**[08:32]** handling any of that scale logic at all.

**[08:32]** handling any of that scale logic at all. So we we our cloud will handle the scale

**[08:35]** So we we our cloud will handle the scale

**[08:35]** So we we our cloud will handle the scale for you. Uh, of course, you know, once

**[08:38]** for you. Uh, of course, you know, once

**[08:38]** for you. Uh, of course, you know, once you've got reliability nailed, you can

**[08:41]** you've got reliability nailed, you can

**[08:41]** you've got reliability nailed, you can sleep better at night, and that's always

**[08:43]** sleep better at night, and that's always

**[08:43]** sleep better at night, and that's always important. Uh, and with reliable

**[08:45]** important. Uh, and with reliable

**[08:46]** important. Uh, and with reliable applications, customers are happier.

**[08:48]** applications, customers are happier.

**[08:48]** applications, customers are happier. Now, I've talked a lot. I wanted to walk

**[08:52]** Now, I've talked a lot. I wanted to walk

**[08:52]** Now, I've talked a lot. I wanted to walk through a example. I I'm not doing a

**[08:55]** through a example. I I'm not doing a

**[08:55]** through a example. I I'm not doing a demo because of all the various issues.

**[08:57]** demo because of all the various issues.

**[08:57]** demo because of all the various issues. Uh, and it also seems like for some

**[08:59]** Uh, and it also seems like for some

**[08:59]** Uh, and it also seems like for some reason travel is like the the classic


### [09:00 - 10:00]

**[09:02]** reason travel is like the the classic

**[09:02]** reason travel is like the the classic use case everybody seems to be demoing.

**[09:04]** use case everybody seems to be demoing.

**[09:04]** use case everybody seems to be demoing. So, let's dive right in.

**[09:06]** So, let's dive right in.

**[09:06]** So, let's dive right in. So, we've got a demo of a ticket booking

**[09:08]** So, we've got a demo of a ticket booking

**[09:08]** So, we've got a demo of a ticket booking agent. This demo is live at our booth as

**[09:11]** agent. This demo is live at our booth as

**[09:11]** agent. This demo is live at our booth as well. So, if you're interested, you can

**[09:13]** well. So, if you're interested, you can

**[09:13]** well. So, if you're interested, you can go look at that at the booth. Um, and

**[09:16]** go look at that at the booth. Um, and

**[09:16]** go look at that at the booth. Um, and what we'll do is I'll quickly walk you

**[09:18]** what we'll do is I'll quickly walk you

**[09:18]** what we'll do is I'll quickly walk you through a little bit of the architecture

**[09:20]** through a little bit of the architecture

**[09:20]** through a little bit of the architecture and how temporal would work here. And so

**[09:23]** and how temporal would work here. And so

**[09:23]** and how temporal would work here. And so clearly you know some of the key pieces

**[09:25]** clearly you know some of the key pieces

**[09:25]** clearly you know some of the key pieces here are around the user the system

**[09:28]** here are around the user the system

**[09:28]** here are around the user the system which is temporal and AI your language

**[09:32]** which is temporal and AI your language

**[09:32]** which is temporal and AI your language models goals and tools and the way that

**[09:36]** models goals and tools and the way that

**[09:36]** models goals and tools and the way that temporal works here is um essentially

**[09:41]** temporal works here is um essentially

**[09:41]** temporal works here is um essentially going to be able to take this flow and

**[09:44]** going to be able to take this flow and

**[09:44]** going to be able to take this flow and in wrap pieces of this in temporal

**[09:47]** in wrap pieces of this in temporal

**[09:47]** in wrap pieces of this in temporal concepts. So for instance, the workflow

**[09:51]** concepts. So for instance, the workflow

**[09:52]** concepts. So for instance, the workflow defines the flow of the application and

**[09:54]** defines the flow of the application and

**[09:54]** defines the flow of the application and it's written as code. So this is where

**[09:57]** it's written as code. So this is where

**[09:57]** it's written as code. So this is where you would orchestrate the interactive


### [10:00 - 11:00]

**[10:00]** you would orchestrate the interactive

**[10:00]** you would orchestrate the interactive loops. You would receive we have this

**[10:02]** loops. You would receive we have this

**[10:02]** loops. You would receive we have this notion of a signal which is how the

**[10:04]** notion of a signal which is how the

**[10:04]** notion of a signal which is how the workflow gets input. We have a notion of

**[10:07]** workflow gets input. We have a notion of

**[10:07]** workflow gets input. We have a notion of a query. So there's a a rich set of

**[10:09]** a query. So there's a a rich set of

**[10:09]** a query. So there's a a rich set of abstractions that you program against to

**[10:12]** abstractions that you program against to

**[10:12]** abstractions that you program against to build that workflow that will

**[10:15]** build that workflow that will

**[10:15]** build that workflow that will essentially take kind of all of the

**[10:17]** essentially take kind of all of the

**[10:17]** essentially take kind of all of the pieces of this model that I'm showing

**[10:20]** pieces of this model that I'm showing

**[10:20]** pieces of this model that I'm showing you and translate that into code. And

**[10:23]** you and translate that into code. And

**[10:23]** you and translate that into code. And nowhere in there will you have any

**[10:26]** nowhere in there will you have any

**[10:26]** nowhere in there will you have any statements or code that we call plumbing

**[10:29]** statements or code that we call plumbing

**[10:29]** statements or code that we call plumbing code. That is you you nowhere in there

**[10:32]** code. That is you you nowhere in there

**[10:32]** code. That is you you nowhere in there will there be statements like if

**[10:34]** will there be statements like if

**[10:34]** will there be statements like if something fails you know keep retrying

**[10:37]** something fails you know keep retrying

**[10:37]** something fails you know keep retrying it. All of those pieces are handled by

**[10:39]** it. All of those pieces are handled by

**[10:40]** it. All of those pieces are handled by temporal.

**[10:42]** temporal.

**[10:42]** temporal. We also store all of the workflow

**[10:45]** We also store all of the workflow

**[10:45]** We also store all of the workflow history uh so that you can go in and you

**[10:47]** history uh so that you can go in and you

**[10:47]** history uh so that you can go in and you can look at the visibility of what is

**[10:50]** can look at the visibility of what is

**[10:50]** can look at the visibility of what is happening as your agent is navigating

**[10:54]** happening as your agent is navigating

**[10:54]** happening as your agent is navigating this complex set of interactions.

**[10:57]** this complex set of interactions.

**[10:57]** this complex set of interactions. Temporal has the notion of activities


### [11:00 - 12:00]

**[11:00]** Temporal has the notion of activities

**[11:00]** Temporal has the notion of activities and so the tools that you use can be

**[11:03]** and so the tools that you use can be

**[11:03]** and so the tools that you use can be wrapped into activities

**[11:05]** wrapped into activities

**[11:05]** wrapped into activities and again this is just code

**[11:09]** and again this is just code

**[11:09]** and again this is just code and of course with LLMs you can use

**[11:12]** and of course with LLMs you can use

**[11:12]** and of course with LLMs you can use whatever provider you need. We are able

**[11:15]** whatever provider you need. We are able

**[11:15]** whatever provider you need. We are able to help you validate the inputs and

**[11:18]** to help you validate the inputs and

**[11:18]** to help you validate the inputs and drive towards the goal. Um and again

**[11:21]** drive towards the goal. Um and again

**[11:21]** drive towards the goal. Um and again failures are handled transparently by

**[11:23]** failures are handled transparently by

**[11:23]** failures are handled transparently by temporal

**[11:26]** temporal

**[11:26]** temporal Um, and then interactions are managed

**[11:29]** Um, and then interactions are managed

**[11:29]** Um, and then interactions are managed through temporal signals and queries.

**[11:32]** through temporal signals and queries.

**[11:32]** through temporal signals and queries. Um, and they're stored in the workflow

**[11:34]** Um, and they're stored in the workflow

**[11:34]** Um, and they're stored in the workflow history. So there's a very clear sort of

**[11:38]** history. So there's a very clear sort of

**[11:38]** history. So there's a very clear sort of record of how your agent is executing

**[11:41]** record of how your agent is executing

**[11:41]** record of how your agent is executing and you can go in and look at that. You

**[11:44]** and you can go in and look at that. You

**[11:44]** and you can go in and look at that. You can also export that. One of the things

**[11:46]** can also export that. One of the things

**[11:46]** can also export that. One of the things we are hearing is customers want access

**[11:49]** we are hearing is customers want access

**[11:49]** we are hearing is customers want access to that history for compliance reasons

**[11:52]** to that history for compliance reasons

**[11:52]** to that history for compliance reasons or for the for kind of being able to go

**[11:55]** or for the for kind of being able to go

**[11:55]** or for the for kind of being able to go and debug in their testdev environment.

**[11:58]** and debug in their testdev environment.

**[11:58]** and debug in their testdev environment. So we allow the capability to export


### [12:00 - 13:00]

**[12:00]** So we allow the capability to export

**[12:00]** So we allow the capability to export that entire history and you can use it

**[12:03]** that entire history and you can use it

**[12:03]** that entire history and you can use it for whatever sort of purpose you might

**[12:05]** for whatever sort of purpose you might

**[12:05]** for whatever sort of purpose you might need.

**[12:08]** need.

**[12:08]** need. Uh and finally here you know you can

**[12:10]** Uh and finally here you know you can

**[12:10]** Uh and finally here you know you can kind of look at the fact that we've got

**[12:13]** kind of look at the fact that we've got

**[12:13]** kind of look at the fact that we've got the ability to have loops. we can, you

**[12:16]** the ability to have loops. we can, you

**[12:16]** the ability to have loops. we can, you know, it's a it's a very rich

**[12:18]** know, it's a it's a very rich

**[12:18]** know, it's a it's a very rich programming model where you can take the

**[12:21]** programming model where you can take the

**[12:21]** programming model where you can take the various uh sort of uh use case patterns

**[12:24]** various uh sort of uh use case patterns

**[12:24]** various uh sort of uh use case patterns for your agent and you can build them as

**[12:27]** for your agent and you can build them as

**[12:27]** for your agent and you can build them as a workflow pretty quickly and get up and

**[12:29]** a workflow pretty quickly and get up and

**[12:29]** a workflow pretty quickly and get up and running. Uh and then temporal cloud of

**[12:32]** running. Uh and then temporal cloud of

**[12:32]** running. Uh and then temporal cloud of course is where we do all of the heavy

**[12:35]** course is where we do all of the heavy

**[12:36]** course is where we do all of the heavy lifting around the reliability and

**[12:38]** lifting around the reliability and

**[12:38]** lifting around the reliability and scalability pieces for you. So your

**[12:40]** scalability pieces for you. So your

**[12:40]** scalability pieces for you. So your agent, your workflow, the code actually

**[12:43]** agent, your workflow, the code actually

**[12:43]** agent, your workflow, the code actually runs in your environment. And temporal

**[12:46]** runs in your environment. And temporal

**[12:46]** runs in your environment. And temporal cloud is where all of the execution

**[12:49]** cloud is where all of the execution

**[12:49]** cloud is where all of the execution state, the call stack, the you know

**[12:53]** state, the call stack, the you know

**[12:53]** state, the call stack, the you know looking at all of the failures and

**[12:56]** looking at all of the failures and

**[12:56]** looking at all of the failures and retries, all of that is happening within

**[12:58]** retries, all of that is happening within

**[12:58]** retries, all of that is happening within temporal cloud.


### [13:00 - 14:00]

**[13:01]** temporal cloud.

**[13:01]** temporal cloud. I know I'm speeding through a lot here,

**[13:03]** I know I'm speeding through a lot here,

**[13:03]** I know I'm speeding through a lot here, but um definitely come by our booth as

**[13:05]** but um definitely come by our booth as

**[13:06]** but um definitely come by our booth as well. Uh the worker is what I was just

**[13:08]** well. Uh the worker is what I was just

**[13:08]** well. Uh the worker is what I was just talking about. This is your code. It

**[13:10]** talking about. This is your code. It

**[13:10]** talking about. This is your code. It runs in your environment. It is

**[13:13]** runs in your environment. It is

**[13:13]** runs in your environment. It is essentially fitting into any of your own

**[13:16]** essentially fitting into any of your own

**[13:16]** essentially fitting into any of your own CI/CD practices. A big part of the

**[13:20]** CI/CD practices. A big part of the

**[13:20]** CI/CD practices. A big part of the temporal focus has been on meeting

**[13:23]** temporal focus has been on meeting

**[13:23]** temporal focus has been on meeting developers where they are. We don't want

**[13:25]** developers where they are. We don't want

**[13:25]** developers where they are. We don't want you to change how you write code. We

**[13:27]** you to change how you write code. We

**[13:27]** you to change how you write code. We just want you to get more efficient and

**[13:30]** just want you to get more efficient and

**[13:30]** just want you to get more efficient and help you focus on writing your business

**[13:33]** help you focus on writing your business

**[13:33]** help you focus on writing your business logic and not having having to worry

**[13:35]** logic and not having having to worry

**[13:35]** logic and not having having to worry about all of the reliability and

**[13:38]** about all of the reliability and

**[13:38]** about all of the reliability and scalability issues here.

**[13:42]** scalability issues here.

**[13:42]** scalability issues here. And this for instance is uh the the

**[13:45]** And this for instance is uh the the

**[13:45]** And this for instance is uh the the worker code for the um uh use case that

**[13:48]** worker code for the um uh use case that

**[13:48]** worker code for the um uh use case that I was just showing. I know this is a

**[13:51]** I was just showing. I know this is a

**[13:51]** I was just showing. I know this is a screenshot. I what I wanted to show here

**[13:54]** screenshot. I what I wanted to show here

**[13:54]** screenshot. I what I wanted to show here is we've got this concept of co code

**[13:56]** is we've got this concept of co code

**[13:56]** is we've got this concept of co code exchange temporal if you weren't aware

**[13:59]** exchange temporal if you weren't aware

**[13:59]** exchange temporal if you weren't aware is an open-source product as well. So


### [14:00 - 15:00]

**[14:02]** is an open-source product as well. So

**[14:02]** is an open-source product as well. So you can go in and I know this conference

**[14:05]** you can go in and I know this conference

**[14:05]** you can go in and I know this conference loves QR codes for some reason. So you

**[14:07]** loves QR codes for some reason. So you

**[14:07]** loves QR codes for some reason. So you can go in and you can actually look at

**[14:09]** can go in and you can actually look at

**[14:09]** can go in and you can actually look at the code at the code exchange and see

**[14:13]** the code at the code exchange and see

**[14:13]** the code at the code exchange and see how temporal operates there.

**[14:16]** how temporal operates there.

**[14:16]** how temporal operates there. Finally, temporal cloud is available uh

**[14:20]** Finally, temporal cloud is available uh

**[14:20]** Finally, temporal cloud is available uh you can go sign up. We are giving away

**[14:22]** you can go sign up. We are giving away

**[14:22]** you can go sign up. We are giving away credits. So getting started and kicking

**[14:25]** credits. So getting started and kicking

**[14:25]** credits. So getting started and kicking the tires on using temporal is fairly

**[14:28]** the tires on using temporal is fairly

**[14:28]** the tires on using temporal is fairly easy. You can go to code exchange. You

**[14:31]** easy. You can go to code exchange. You

**[14:31]** easy. You can go to code exchange. You can look at any example you want. You

**[14:35]** can look at any example you want. You

**[14:35]** can look at any example you want. You can run that in your local dev

**[14:36]** can run that in your local dev

**[14:36]** can run that in your local dev environment. You can run it against

**[14:38]** environment. You can run it against

**[14:38]** environment. You can run it against cloud and you can be up and running

**[14:40]** cloud and you can be up and running

**[14:40]** cloud and you can be up and running pretty quickly here. And we are like I

**[14:43]** pretty quickly here. And we are like I

**[14:43]** pretty quickly here. And we are like I said we are on the uh on the expo floor.

**[14:47]** said we are on the uh on the expo floor.

**[14:47]** said we are on the uh on the expo floor. Come by and chat with us. We are booth

**[14:49]** Come by and chat with us. We are booth

**[14:49]** Come by and chat with us. We are booth G3.

**[14:52]** G3.

**[14:52]** G3. Perfect. Thank you.

**[14:55]** Perfect. Thank you.

**[14:55]** Perfect. Thank you. [Music]


