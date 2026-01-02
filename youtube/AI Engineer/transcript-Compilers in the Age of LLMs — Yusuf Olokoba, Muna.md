# Compilers in the Age of LLMs — Yusuf Olokoba, Muna

**Video URL:** https://www.youtube.com/watch?v=q2nHsJVy4FE

---

## Full Transcript

### [00:00 - 01:00]

**[00:02]** If you're an AI engineer right now, your

**[00:02]** If you're an AI engineer right now, your day-to-day probably looks something like

**[00:05]** day-to-day probably looks something like

**[00:05]** day-to-day probably looks something like this. You've got an open client in your

**[00:07]** this. You've got an open client in your

**[00:07]** this. You've got an open client in your codebase. You've got a few hugging face

**[00:10]** codebase. You've got a few hugging face

**[00:10]** codebase. You've got a few hugging face tabs open. You've got three different

**[00:12]** tabs open. You've got three different

**[00:12]** tabs open. You've got three different repos with the word playground in them.

**[00:15]** repos with the word playground in them.

**[00:15]** repos with the word playground in them. And you've got at least one agentic

**[00:17]** And you've got at least one agentic

**[00:17]** And you've got at least one agentic workflow that's really just stringing

**[00:18]** workflow that's really just stringing

**[00:18]** workflow that's really just stringing together a bunch of HTTP calls. Right

**[00:21]** together a bunch of HTTP calls. Right

**[00:21]** together a bunch of HTTP calls. Right now, everyone is talking about voice

**[00:23]** now, everyone is talking about voice

**[00:23]** now, everyone is talking about voice agents, MCP, and these are pretty cool

**[00:26]** agents, MCP, and these are pretty cool

**[00:26]** agents, MCP, and these are pretty cool technologies, but when you peel back the

**[00:28]** technologies, but when you peel back the

**[00:28]** technologies, but when you peel back the hype a little bit, what I hear when I

**[00:31]** hype a little bit, what I hear when I

**[00:31]** hype a little bit, what I hear when I talk to a lot of engineering teams is

**[00:32]** talk to a lot of engineering teams is

**[00:32]** talk to a lot of engineering teams is that they're usually grappling with much

**[00:35]** that they're usually grappling with much

**[00:35]** that they're usually grappling with much more fundamental and boring problems.

**[00:38]** more fundamental and boring problems.

**[00:38]** more fundamental and boring problems. How do I use more models in more places

**[00:41]** How do I use more models in more places

**[00:41]** How do I use more models in more places without having to rebuild or extend my

**[00:43]** without having to rebuild or extend my

**[00:43]** without having to rebuild or extend my infrastructure every single time?

**[00:46]** infrastructure every single time?

**[00:46]** infrastructure every single time? So say you want to go try out a new open

**[00:49]** So say you want to go try out a new open

**[00:49]** So say you want to go try out a new open source model that just dropped on

**[00:51]** source model that just dropped on

**[00:51]** source model that just dropped on hugging face today. That usually means

**[00:53]** hugging face today. That usually means

**[00:53]** hugging face today. That usually means you got to go write a Docker file, spin

**[00:55]** you got to go write a Docker file, spin

**[00:55]** you got to go write a Docker file, spin up a Docker container, and then get that

**[00:57]** up a Docker container, and then get that

**[00:57]** up a Docker container, and then get that running on infrastructure that you own


### [01:00 - 02:00]

**[01:00]** running on infrastructure that you own

**[01:00]** running on infrastructure that you own or that you rent from a third party

**[01:02]** or that you rent from a third party

**[01:02]** or that you rent from a third party provider. And if you're wiring this into

**[01:05]** provider. And if you're wiring this into

**[01:05]** provider. And if you're wiring this into an AI agent, well, that's another tool

**[01:07]** an AI agent, well, that's another tool

**[01:07]** an AI agent, well, that's another tool that you have to put into the context

**[01:09]** that you have to put into the context

**[01:09]** that you have to put into the context and perhaps expose either like an MCP or

**[01:12]** and perhaps expose either like an MCP or

**[01:12]** and perhaps expose either like an MCP or something similar. A lot of this is just

**[01:15]** something similar. A lot of this is just

**[01:15]** something similar. A lot of this is just complexity that creeps in and only grows

**[01:17]** complexity that creeps in and only grows

**[01:17]** complexity that creeps in and only grows further more time you spend. What

**[01:20]** further more time you spend. What

**[01:20]** further more time you spend. What developers actually want is something

**[01:22]** developers actually want is something

**[01:22]** developers actually want is something way simpler. Just give me an open style

**[01:25]** way simpler. Just give me an open style

**[01:25]** way simpler. Just give me an open style client that just works. Let me point it

**[01:28]** client that just works. Let me point it

**[01:28]** client that just works. Let me point it to any model at all. It doesn't matter

**[01:30]** to any model at all. It doesn't matter

**[01:30]** to any model at all. It doesn't matter if it's running locally, if it's running

**[01:32]** if it's running locally, if it's running

**[01:32]** if it's running locally, if it's running remotely, if it's Llama CBP or Tensor

**[01:35]** remotely, if it's Llama CBP or Tensor

**[01:35]** remotely, if it's Llama CBP or Tensor RT. I just want something that works

**[01:37]** RT. I just want something that works

**[01:37]** RT. I just want something that works with minimal code changes. In this talk,

**[01:41]** with minimal code changes. In this talk,

**[01:41]** with minimal code changes. In this talk, I'll walk you through how we decided to

**[01:43]** I'll walk you through how we decided to

**[01:43]** I'll walk you through how we decided to build a compiler for Python that enables

**[01:47]** build a compiler for Python that enables

**[01:47]** build a compiler for Python that enables developers to write simple plain Python

**[01:49]** developers to write simple plain Python

**[01:49]** developers to write simple plain Python code and then convert that into a tiny

**[01:52]** code and then convert that into a tiny

**[01:52]** code and then convert that into a tiny self-contained binary that can then run

**[01:55]** self-contained binary that can then run

**[01:55]** self-contained binary that can then run anywhere at all. It could be the cloud,

**[01:57]** anywhere at all. It could be the cloud,

**[01:58]** anywhere at all. It could be the cloud, it could be Apple silicon, it could be

**[01:59]** it could be Apple silicon, it could be

**[01:59]** it could be Apple silicon, it could be anything else in between. Further, I'll


### [02:00 - 03:00]

**[02:02]** anything else in between. Further, I'll

**[02:02]** anything else in between. Further, I'll show you how we use LLM within that

**[02:03]** show you how we use LLM within that

**[02:03]** show you how we use LLM within that compiler pipeline. a few things we

**[02:06]** compiler pipeline. a few things we

**[02:06]** compiler pipeline. a few things we tried, what worked, what didn't work,

**[02:08]** tried, what worked, what didn't work,

**[02:08]** tried, what worked, what didn't work, how we fenced them with verification and

**[02:10]** how we fenced them with verification and

**[02:10]** how we fenced them with verification and LLM power testing, and how these this

**[02:13]** LLM power testing, and how these this

**[02:13]** LLM power testing, and how these this infrastructure gives us the ability to

**[02:15]** infrastructure gives us the ability to

**[02:15]** infrastructure gives us the ability to not just run any AM model at all, but we

**[02:18]** not just run any AM model at all, but we

**[02:18]** not just run any AM model at all, but we can now run it in so many more places

**[02:19]** can now run it in so many more places

**[02:20]** can now run it in so many more places beyond just server side.

**[02:22]** beyond just server side.

**[02:22]** beyond just server side. So before we start getting our hands

**[02:24]** So before we start getting our hands

**[02:24]** So before we start getting our hands dirty with an example, I wanted to

**[02:26]** dirty with an example, I wanted to

**[02:26]** dirty with an example, I wanted to provide some motivation on why we

**[02:28]** provide some motivation on why we

**[02:28]** provide some motivation on why we thought building a Python compiler was

**[02:30]** thought building a Python compiler was

**[02:30]** thought building a Python compiler was the best way to solve AI deployment in

**[02:33]** the best way to solve AI deployment in

**[02:33]** the best way to solve AI deployment in the long run.

**[02:34]** the long run.

**[02:34]** the long run. First, we needed an extremely simple and

**[02:37]** First, we needed an extremely simple and

**[02:37]** First, we needed an extremely simple and standardized way for developers to bring

**[02:40]** standardized way for developers to bring

**[02:40]** standardized way for developers to bring their AI models, whether the ones that

**[02:42]** their AI models, whether the ones that

**[02:42]** their AI models, whether the ones that they've built internally or models that

**[02:44]** they've built internally or models that

**[02:44]** they've built internally or models that they found open source on Ugging on

**[02:46]** they found open source on Ugging on

**[02:46]** they found open source on Ugging on GitHub, and then get something that they

**[02:49]** GitHub, and then get something that they

**[02:49]** GitHub, and then get something that they could execute very easily in their

**[02:52]** could execute very easily in their

**[02:52]** could execute very easily in their codebase.

**[02:53]** codebase.

**[02:54]** codebase. So, when a new OpenAI model comes out,

**[02:56]** So, when a new OpenAI model comes out,

**[02:56]** So, when a new OpenAI model comes out, for example, all you have to do is

**[02:58]** for example, all you have to do is

**[02:58]** for example, all you have to do is simply just change the model argument


### [03:00 - 04:00]

**[03:00]** simply just change the model argument

**[03:00]** simply just change the model argument pointing it to the new model that OpenAI

**[03:02]** pointing it to the new model that OpenAI

**[03:02]** pointing it to the new model that OpenAI just dropped. We wanted to recreate

**[03:04]** just dropped. We wanted to recreate

**[03:04]** just dropped. We wanted to recreate something that tracked this experience

**[03:06]** something that tracked this experience

**[03:06]** something that tracked this experience as closely as possible. Conceptually,

**[03:10]** as closely as possible. Conceptually,

**[03:10]** as closely as possible. Conceptually, this would have to look like something

**[03:11]** this would have to look like something

**[03:11]** this would have to look like something that ingested code, Python inference

**[03:13]** that ingested code, Python inference

**[03:13]** that ingested code, Python inference code, and then spat out some other thing

**[03:16]** code, and then spat out some other thing

**[03:16]** code, and then spat out some other thing that knew how to get executed in our

**[03:18]** that knew how to get executed in our

**[03:18]** that knew how to get executed in our develop in our users uh execution

**[03:20]** develop in our users uh execution

**[03:20]** develop in our users uh execution environments. Second, we wanted to

**[03:23]** environments. Second, we wanted to

**[03:23]** environments. Second, we wanted to prepare for what we strongly believe to

**[03:25]** prepare for what we strongly believe to

**[03:25]** prepare for what we strongly believe to be the future of AI deployment, hybrid

**[03:28]** be the future of AI deployment, hybrid

**[03:28]** be the future of AI deployment, hybrid inference. We expect that in the future

**[03:31]** inference. We expect that in the future

**[03:31]** inference. We expect that in the future we will see smaller models typically

**[03:34]** we will see smaller models typically

**[03:34]** we will see smaller models typically much closer to users either locally on

**[03:36]** much closer to users either locally on

**[03:36]** much closer to users either locally on their devices or in edge locations

**[03:38]** their devices or in edge locations

**[03:38]** their devices or in edge locations working in tandem with cloud AI models

**[03:41]** working in tandem with cloud AI models

**[03:41]** working in tandem with cloud AI models that are much larger and have a bigger

**[03:43]** that are much larger and have a bigger

**[03:43]** that are much larger and have a bigger reasoning abilities and we expect that

**[03:46]** reasoning abilities and we expect that

**[03:46]** reasoning abilities and we expect that this is going to be the future of how a

**[03:47]** this is going to be the future of how a

**[03:47]** this is going to be the future of how a lot of people consume AI in their

**[03:49]** lot of people consume AI in their

**[03:49]** lot of people consume AI in their day-to-day lives. As such, this means

**[03:51]** day-to-day lives. As such, this means

**[03:51]** day-to-day lives. As such, this means that developers have to move away from,

**[03:53]** that developers have to move away from,

**[03:53]** that developers have to move away from, you know, the the cages of Python code

**[03:56]** you know, the the cages of Python code

**[03:56]** you know, the the cages of Python code and Docker containers into something

**[03:58]** and Docker containers into something

**[03:58]** and Docker containers into something that is a lot more low-level, closer to


### [04:00 - 05:00]

**[04:01]** that is a lot more low-level, closer to

**[04:01]** that is a lot more low-level, closer to the hardware, and a lot more responsive.

**[04:05]** the hardware, and a lot more responsive.

**[04:05]** the hardware, and a lot more responsive. So, let's get our hands dirty. This is a

**[04:08]** So, let's get our hands dirty. This is a

**[04:08]** So, let's get our hands dirty. This is a Python function that runs Google's

**[04:11]** Python function that runs Google's

**[04:11]** Python function that runs Google's embedding Gemma 270 million parameter

**[04:14]** embedding Gemma 270 million parameter

**[04:14]** embedding Gemma 270 million parameter model. It's a very simple text embedding

**[04:16]** model. It's a very simple text embedding

**[04:16]** model. It's a very simple text embedding model that takes in a list of of

**[04:19]** model that takes in a list of of

**[04:19]** model that takes in a list of of sentences, just plain text, and then

**[04:22]** sentences, just plain text, and then

**[04:22]** sentences, just plain text, and then runs a model that is able to generate an

**[04:24]** runs a model that is able to generate an

**[04:24]** runs a model that is able to generate an embedding vector or a list of embedding

**[04:26]** embedding vector or a list of embedding

**[04:26]** embedding vector or a list of embedding vectors, an embedding matrix. You will

**[04:29]** vectors, an embedding matrix. You will

**[04:29]** vectors, an embedding matrix. You will typically use models like this in text,

**[04:32]** typically use models like this in text,

**[04:32]** typically use models like this in text, in text search, in retrieval augmented

**[04:34]** in text search, in retrieval augmented

**[04:34]** in text search, in retrieval augmented generation, and in other frameworks

**[04:36]** generation, and in other frameworks

**[04:36]** generation, and in other frameworks where you need to be able to retrieve

**[04:38]** where you need to be able to retrieve

**[04:38]** where you need to be able to retrieve documents or retrieve subsections of

**[04:40]** documents or retrieve subsections of

**[04:40]** documents or retrieve subsections of documents. This model from Google is

**[04:42]** documents. This model from Google is

**[04:42]** documents. This model from Google is small enough at only 270 million

**[04:44]** small enough at only 270 million

**[04:44]** small enough at only 270 million parameters that not only can it run very

**[04:46]** parameters that not only can it run very

**[04:46]** parameters that not only can it run very easily on uh GPUs in the cloud, it can

**[04:49]** easily on uh GPUs in the cloud, it can

**[04:49]** easily on uh GPUs in the cloud, it can also run very quickly on consumer

**[04:51]** also run very quickly on consumer

**[04:51]** also run very quickly on consumer hardware also. And today we will be

**[04:54]** hardware also. And today we will be

**[04:54]** hardware also. And today we will be figuring out how to take this Python

**[04:56]** figuring out how to take this Python

**[04:56]** figuring out how to take this Python function that runs the embedding model,

**[04:59]** function that runs the embedding model,

**[04:59]** function that runs the embedding model, generate equivalent C++ and Rust code


### [05:00 - 06:00]

**[05:02]** generate equivalent C++ and Rust code

**[05:02]** generate equivalent C++ and Rust code that is much lower level and is now able

**[05:04]** that is much lower level and is now able

**[05:04]** that is much lower level and is now able to run anywhere at all. And then we will

**[05:07]** to run anywhere at all. And then we will

**[05:07]** to run anywhere at all. And then we will compile a binary that contains this

**[05:09]** compile a binary that contains this

**[05:10]** compile a binary that contains this model and all the dependencies it needs.

**[05:12]** model and all the dependencies it needs.

**[05:12]** model and all the dependencies it needs. And finally we will consume this model

**[05:14]** And finally we will consume this model

**[05:14]** And finally we will consume this model using the familiar OpenAI

**[05:17]** using the familiar OpenAI

**[05:17]** using the familiar OpenAI client.bings.create

**[05:19]** client.bings.create

**[05:19]** client.bings.create experience.

**[05:20]** experience.

**[05:20]** experience. The very first step is taking our

**[05:23]** The very first step is taking our

**[05:23]** The very first step is taking our function and generating a graph

**[05:26]** function and generating a graph

**[05:26]** function and generating a graph representation that describes everything

**[05:28]** representation that describes everything

**[05:28]** representation that describes everything that happens within that function. We

**[05:31]** that happens within that function. We

**[05:31]** that happens within that function. We call this tracing.

**[05:33]** call this tracing.

**[05:33]** call this tracing. Initially our uh first prototypes of

**[05:36]** Initially our uh first prototypes of

**[05:36]** Initially our uh first prototypes of building a symbolic tracing uh solution

**[05:39]** building a symbolic tracing uh solution

**[05:39]** building a symbolic tracing uh solution was actually built off of PyTorch 2

**[05:42]** was actually built off of PyTorch 2

**[05:42]** was actually built off of PyTorch 2 which introduced Torch compile along

**[05:45]** which introduced Torch compile along

**[05:45]** which introduced Torch compile along with Torch FX

**[05:47]** with Torch FX

**[05:47]** with Torch FX uh for this purpose. So the way that

**[05:49]** uh for this purpose. So the way that

**[05:49]** uh for this purpose. So the way that torch FX works is it'll take in Python

**[05:52]** torch FX works is it'll take in Python

**[05:52]** torch FX works is it'll take in Python source code and then run it with fake

**[05:54]** source code and then run it with fake

**[05:54]** source code and then run it with fake inputs that don't allocate any memory

**[05:57]** inputs that don't allocate any memory

**[05:57]** inputs that don't allocate any memory and then give you a description a graph

**[05:59]** and then give you a description a graph

**[05:59]** and then give you a description a graph of everything that happened within that


### [06:00 - 07:00]

**[06:01]** of everything that happened within that

**[06:01]** of everything that happened within that function. We actually try to use this

**[06:03]** function. We actually try to use this

**[06:03]** function. We actually try to use this but we faced two major issues that

**[06:06]** but we faced two major issues that

**[06:06]** but we faced two major issues that caused us to build our own uh tracing

**[06:08]** caused us to build our own uh tracing

**[06:08]** caused us to build our own uh tracing infrastructure. The first was that

**[06:11]** infrastructure. The first was that

**[06:11]** infrastructure. The first was that PyTorch uh is very focused its tracer is

**[06:14]** PyTorch uh is very focused its tracer is

**[06:14]** PyTorch uh is very focused its tracer is very focused on only PyTorch code. And

**[06:17]** very focused on only PyTorch code. And

**[06:17]** very focused on only PyTorch code. And so in order to trace arbitrary code

**[06:19]** so in order to trace arbitrary code

**[06:19]** so in order to trace arbitrary code which your functions will usually have

**[06:21]** which your functions will usually have

**[06:21]** which your functions will usually have to rely on things like numpy operations

**[06:24]** to rely on things like numpy operations

**[06:24]** to rely on things like numpy operations or OpenCV or something else we would

**[06:27]** or OpenCV or something else we would

**[06:27]** or OpenCV or something else we would have had to figure out a way to like add

**[06:29]** have had to figure out a way to like add

**[06:29]** have had to figure out a way to like add support for those data types into

**[06:31]** support for those data types into

**[06:31]** support for those data types into PyTorch.

**[06:32]** PyTorch.

**[06:32]** PyTorch. The second reason why we didn't stick

**[06:34]** The second reason why we didn't stick

**[06:34]** The second reason why we didn't stick with PyTorch was in order for the tracer

**[06:37]** with PyTorch was in order for the tracer

**[06:37]** with PyTorch was in order for the tracer to work, it had to be run on fake

**[06:40]** to work, it had to be run on fake

**[06:40]** to work, it had to be run on fake inputs. And so, you know, creating a

**[06:42]** inputs. And so, you know, creating a

**[06:42]** inputs. And so, you know, creating a fake tensor is trivial. You just, you

**[06:44]** fake tensor is trivial. You just, you

**[06:44]** fake tensor is trivial. You just, you know, give it the same description and

**[06:46]** know, give it the same description and

**[06:46]** know, give it the same description and don't allocate any data. But it's a lot

**[06:49]** don't allocate any data. But it's a lot

**[06:49]** don't allocate any data. But it's a lot harder to create a fake image or a fake

**[06:52]** harder to create a fake image or a fake

**[06:52]** harder to create a fake image or a fake dictionary or a fake, you know, whatever

**[06:54]** dictionary or a fake, you know, whatever

**[06:54]** dictionary or a fake, you know, whatever type that we might encounter in the

**[06:55]** type that we might encounter in the

**[06:55]** type that we might encounter in the wild. And so, we simply decided that we

**[06:58]** wild. And so, we simply decided that we

**[06:58]** wild. And so, we simply decided that we were going to build something in house.


### [07:00 - 08:00]

**[07:00]** were going to build something in house.

**[07:00]** were going to build something in house. Our first attempt was actually using LLM

**[07:03]** Our first attempt was actually using LLM

**[07:03]** Our first attempt was actually using LLM as a way to generate traces because LLMs

**[07:06]** as a way to generate traces because LLMs

**[07:06]** as a way to generate traces because LLMs for quite some time now have had this

**[07:08]** for quite some time now have had this

**[07:08]** for quite some time now have had this capability of structured outputs. This

**[07:11]** capability of structured outputs. This

**[07:11]** capability of structured outputs. This is where you can give an LLM a prompt

**[07:13]** is where you can give an LLM a prompt

**[07:13]** is where you can give an LLM a prompt some data whether it be an image, text

**[07:15]** some data whether it be an image, text

**[07:15]** some data whether it be an image, text or audio and ask it to respond to you

**[07:17]** or audio and ask it to respond to you

**[07:18]** or audio and ask it to respond to you with a specific schema that you have

**[07:19]** with a specific schema that you have

**[07:19]** with a specific schema that you have given to the model. This actually turned

**[07:22]** given to the model. This actually turned

**[07:22]** given to the model. This actually turned out to work pretty well. Uh it had

**[07:25]** out to work pretty well. Uh it had

**[07:25]** out to work pretty well. Uh it had almost like a 100% uh accuracy rate in

**[07:27]** almost like a 100% uh accuracy rate in

**[07:27]** almost like a 100% uh accuracy rate in our own testing. The only limitation was

**[07:30]** our own testing. The only limitation was

**[07:30]** our own testing. The only limitation was it simply took way too much time. And so

**[07:33]** it simply took way too much time. And so

**[07:33]** it simply took way too much time. And so eventually we decided we're just going

**[07:34]** eventually we decided we're just going

**[07:34]** eventually we decided we're just going to do it old school. We would build a

**[07:36]** to do it old school. We would build a

**[07:36]** to do it old school. We would build a tracer by first analyzing the code

**[07:38]** tracer by first analyzing the code

**[07:38]** tracer by first analyzing the code looking at the a or the abst the

**[07:41]** looking at the a or the abst the

**[07:41]** looking at the a or the abst the abstract syntax tree of the Python code

**[07:43]** abstract syntax tree of the Python code

**[07:43]** abstract syntax tree of the Python code and then using a bunch of internal

**[07:45]** and then using a bunch of internal

**[07:45]** and then using a bunch of internal huristics to build our own internal

**[07:47]** huristics to build our own internal

**[07:47]** huristics to build our own internal representation or IR of the user's

**[07:50]** representation or IR of the user's

**[07:50]** representation or IR of the user's function. So for this function that

**[07:52]** function. So for this function that

**[07:52]** function. So for this function that we've written up, the IR is actually

**[07:54]** we've written up, the IR is actually

**[07:54]** we've written up, the IR is actually incredibly simple. I'm not going to show

**[07:55]** incredibly simple. I'm not going to show

**[07:56]** incredibly simple. I'm not going to show you the entire thing, but I'll just show

**[07:57]** you the entire thing, but I'll just show

**[07:57]** you the entire thing, but I'll just show you the parts that are relevant to look

**[07:59]** you the parts that are relevant to look

**[07:59]** you the parts that are relevant to look at. As you can see, there's input nodes


### [08:00 - 09:00]

**[08:02]** at. As you can see, there's input nodes

**[08:02]** at. As you can see, there's input nodes for the actual uh inputs to the

**[08:04]** for the actual uh inputs to the

**[08:04]** for the actual uh inputs to the function. So like that's a list of the

**[08:05]** function. So like that's a list of the

**[08:06]** function. So like that's a list of the strings. There's a function call to

**[08:08]** strings. There's a function call to

**[08:08]** strings. There's a function call to calling out to the tokenizer. Another

**[08:09]** calling out to the tokenizer. Another

**[08:10]** calling out to the tokenizer. Another one's calling out to the model. And then

**[08:11]** one's calling out to the model. And then

**[08:12]** one's calling out to the model. And then we return those outputs so that the user

**[08:14]** we return those outputs so that the user

**[08:14]** we return those outputs so that the user can then get their embedding vectors.

**[08:16]** can then get their embedding vectors.

**[08:16]** can then get their embedding vectors. Now that we have a high-level

**[08:18]** Now that we have a high-level

**[08:18]** Now that we have a high-level intermediate representation of our

**[08:20]** intermediate representation of our

**[08:20]** intermediate representation of our Python function, the next step is to

**[08:22]** Python function, the next step is to

**[08:22]** Python function, the next step is to figure out how to translate that somehow

**[08:25]** figure out how to translate that somehow

**[08:25]** figure out how to translate that somehow into lower level C++ or Rust code. But

**[08:29]** into lower level C++ or Rust code. But

**[08:29]** into lower level C++ or Rust code. But before jumping into that, I wanted to

**[08:30]** before jumping into that, I wanted to

**[08:30]** before jumping into that, I wanted to talk about one major difference between

**[08:33]** talk about one major difference between

**[08:33]** talk about one major difference between Python as a language and C++ or other

**[08:36]** Python as a language and C++ or other

**[08:36]** Python as a language and C++ or other lower level languages that we will run

**[08:38]** lower level languages that we will run

**[08:38]** lower level languages that we will run into and have to solve. Python is a very

**[08:41]** into and have to solve. Python is a very

**[08:41]** into and have to solve. Python is a very dynamic language. So one variable X

**[08:45]** dynamic language. So one variable X

**[08:46]** dynamic language. So one variable X could be assigned to an integer and then

**[08:48]** could be assigned to an integer and then

**[08:48]** could be assigned to an integer and then immediately after assigned to say a

**[08:50]** immediately after assigned to say a

**[08:50]** immediately after assigned to say a string. There is full dynamism in

**[08:53]** string. There is full dynamism in

**[08:53]** string. There is full dynamism in anything goes. Whereas in lower level

**[08:55]** anything goes. Whereas in lower level

**[08:55]** anything goes. Whereas in lower level languages like C++ and Rust if you

**[08:57]** languages like C++ and Rust if you

**[08:57]** languages like C++ and Rust if you declare a variable you must give it a

**[08:59]** declare a variable you must give it a

**[08:59]** declare a variable you must give it a type and that type can never change.


### [09:00 - 10:00]

**[09:02]** type and that type can never change.

**[09:02]** type and that type can never change. This gives us quite a bit of a challenge

**[09:04]** This gives us quite a bit of a challenge

**[09:04]** This gives us quite a bit of a challenge because we need to figure out how to

**[09:07]** because we need to figure out how to

**[09:07]** because we need to figure out how to attach or constrain the types in the

**[09:10]** attach or constrain the types in the

**[09:10]** attach or constrain the types in the code that we will be generating from our

**[09:12]** code that we will be generating from our

**[09:12]** code that we will be generating from our Python highle code.

**[09:15]** Python highle code.

**[09:15]** Python highle code. So let's look at the first line of our

**[09:17]** So let's look at the first line of our

**[09:17]** So let's look at the first line of our function. The very first node if you

**[09:20]** function. The very first node if you

**[09:20]** function. The very first node if you call it of our IR. As you can see

**[09:23]** call it of our IR. As you can see

**[09:23]** call it of our IR. As you can see prompts is this list that is being

**[09:25]** prompts is this list that is being

**[09:25]** prompts is this list that is being generated by a comprehension statement.

**[09:28]** generated by a comprehension statement.

**[09:28]** generated by a comprehension statement. and we're effectively just adding a set

**[09:30]** and we're effectively just adding a set

**[09:30]** and we're effectively just adding a set of prefixes for every sentence that has

**[09:33]** of prefixes for every sentence that has

**[09:33]** of prefixes for every sentence that has been passed in by the user. And so let's

**[09:36]** been passed in by the user. And so let's

**[09:36]** been passed in by the user. And so let's just focus in on that addition operation

**[09:38]** just focus in on that addition operation

**[09:38]** just focus in on that addition operation that's happening within that

**[09:40]** that's happening within that

**[09:40]** that's happening within that comprehension. As you can see, well, we

**[09:43]** comprehension. As you can see, well, we

**[09:43]** comprehension. As you can see, well, we know that every item in text is a string

**[09:46]** know that every item in text is a string

**[09:46]** know that every item in text is a string because we have pretty much annotated

**[09:48]** because we have pretty much annotated

**[09:48]** because we have pretty much annotated our function as such, right? The input

**[09:50]** our function as such, right? The input

**[09:50]** our function as such, right? The input text is a list of strings. And we also

**[09:53]** text is a list of strings. And we also

**[09:53]** text is a list of strings. And we also know that the text prefix map just

**[09:55]** know that the text prefix map just

**[09:55]** know that the text prefix map just contains a bunch of strings. Each prefix

**[09:57]** contains a bunch of strings. Each prefix

**[09:58]** contains a bunch of strings. Each prefix is itself a string. And so the question


### [10:00 - 11:00]

**[10:00]** is itself a string. And so the question

**[10:00]** is itself a string. And so the question then becomes how do we know or how do we

**[10:02]** then becomes how do we know or how do we

**[10:02]** then becomes how do we know or how do we figure out the C++ type on the output of

**[10:05]** figure out the C++ type on the output of

**[10:06]** figure out the C++ type on the output of that operation. And this is where the

**[10:08]** that operation. And this is where the

**[10:08]** that operation. And this is where the compiler comes in specifically a

**[10:10]** compiler comes in specifically a

**[10:10]** compiler comes in specifically a technique we call type propagation. And

**[10:13]** technique we call type propagation. And

**[10:13]** technique we call type propagation. And so here we will take one string the

**[10:16]** so here we will take one string the

**[10:16]** so here we will take one string the prefix the other string the actual input

**[10:18]** prefix the other string the actual input

**[10:18]** prefix the other string the actual input text that was provided to the function.

**[10:21]** text that was provided to the function.

**[10:21]** text that was provided to the function. And we now know that there is some

**[10:23]** And we now know that there is some

**[10:23]** And we now know that there is some addition operation happening to these

**[10:25]** addition operation happening to these

**[10:25]** addition operation happening to these two. So we can simply write or generate

**[10:30]** two. So we can simply write or generate

**[10:30]** two. So we can simply write or generate a C++ function that takes in two strings

**[10:33]** a C++ function that takes in two strings

**[10:33]** a C++ function that takes in two strings and performs the operator.add operation

**[10:36]** and performs the operator.add operation

**[10:36]** and performs the operator.add operation from Python.

**[10:38]** from Python.

**[10:38]** from Python. The output of that function that we

**[10:40]** The output of that function that we

**[10:40]** The output of that function that we generate in C++ as you can see here well

**[10:43]** generate in C++ as you can see here well

**[10:43]** generate in C++ as you can see here well it's just a string and that's how we

**[10:45]** it's just a string and that's how we

**[10:45]** it's just a string and that's how we know that whatever the output of this

**[10:47]** know that whatever the output of this

**[10:47]** know that whatever the output of this addition operation uh we're doing is

**[10:50]** addition operation uh we're doing is

**[10:50]** addition operation uh we're doing is must itself be a string. So in that way

**[10:54]** must itself be a string. So in that way

**[10:54]** must itself be a string. So in that way zooming out we've been able to take the

**[10:57]** zooming out we've been able to take the

**[10:57]** zooming out we've been able to take the input information the input type

**[10:59]** input information the input type

**[10:59]** input information the input type information from just the signature of


### [11:00 - 12:00]

**[11:01]** information from just the signature of

**[11:01]** information from just the signature of our Python function along with the C++

**[11:04]** our Python function along with the C++

**[11:04]** our Python function along with the C++ type information or the the native type

**[11:06]** type information or the the native type

**[11:06]** type information or the the native type information of this global constant task

**[11:10]** information of this global constant task

**[11:10]** information of this global constant task prefix map and then we've been able to

**[11:12]** prefix map and then we've been able to

**[11:12]** prefix map and then we've been able to use that to propagate into the output of

**[11:15]** use that to propagate into the output of

**[11:16]** use that to propagate into the output of the concatenation of these two things.

**[11:18]** the concatenation of these two things.

**[11:18]** the concatenation of these two things. We now know that if I concatenate one

**[11:20]** We now know that if I concatenate one

**[11:20]** We now know that if I concatenate one prefix with one input string, the result

**[11:22]** prefix with one input string, the result

**[11:22]** prefix with one input string, the result itself is a string. And so we can then

**[11:25]** itself is a string. And so we can then

**[11:25]** itself is a string. And so we can then do this propagation for every

**[11:27]** do this propagation for every

**[11:27]** do this propagation for every intermediate variable or every operation

**[11:30]** intermediate variable or every operation

**[11:30]** intermediate variable or every operation within our original Python function. And

**[11:32]** within our original Python function. And

**[11:32]** within our original Python function. And that's how we can kind of like flow type

**[11:34]** that's how we can kind of like flow type

**[11:34]** that's how we can kind of like flow type information through. And so at this

**[11:36]** information through. And so at this

**[11:36]** information through. And so at this point you might be wondering well your

**[11:39]** point you might be wondering well your

**[11:39]** point you might be wondering well your compiler if you're doing this

**[11:41]** compiler if you're doing this

**[11:41]** compiler if you're doing this propagation thing that requires us

**[11:42]** propagation thing that requires us

**[11:42]** propagation thing that requires us manually implementing some operation in

**[11:44]** manually implementing some operation in

**[11:44]** manually implementing some operation in C++ or in RS code we would have to

**[11:47]** C++ or in RS code we would have to

**[11:47]** C++ or in RS code we would have to literally rewrite this for every unique

**[11:52]** literally rewrite this for every unique

**[11:52]** literally rewrite this for every unique function call or operation that we ever

**[11:54]** function call or operation that we ever

**[11:54]** function call or operation that we ever encounter in Python. And you'll be

**[11:56]** encounter in Python. And you'll be

**[11:56]** encounter in Python. And you'll be correct you'll be 100% correct that is

**[11:58]** correct you'll be 100% correct that is

**[11:58]** correct you'll be 100% correct that is in fact what we would have to do. But


### [12:00 - 13:00]

**[12:00]** in fact what we would have to do. But

**[12:00]** in fact what we would have to do. But that is now tractable and it's an easier

**[12:03]** that is now tractable and it's an easier

**[12:03]** that is now tractable and it's an easier problem to solve now for two reasons.

**[12:07]** problem to solve now for two reasons.

**[12:07]** problem to solve now for two reasons. The first reason is that all the variety

**[12:10]** The first reason is that all the variety

**[12:10]** The first reason is that all the variety you'll ever see in source code in the

**[12:12]** you'll ever see in source code in the

**[12:12]** you'll ever see in source code in the wild is not because there's such a giant

**[12:15]** wild is not because there's such a giant

**[12:15]** wild is not because there's such a giant volume of these operations. The volume

**[12:18]** volume of these operations. The volume

**[12:18]** volume of these operations. The volume is actually because you can combine

**[12:19]** is actually because you can combine

**[12:19]** is actually because you can combine operations in so many different ways.

**[12:22]** operations in so many different ways.

**[12:22]** operations in so many different ways. You can permute them in so many

**[12:23]** You can permute them in so many

**[12:23]** You can permute them in so many different ways. in each of these

**[12:24]** different ways. in each of these

**[12:24]** different ways. in each of these permutations is what forms a unique

**[12:27]** permutations is what forms a unique

**[12:27]** permutations is what forms a unique Python function or Python code. And so

**[12:30]** Python function or Python code. And so

**[12:30]** Python function or Python code. And so we really only need to cover that base

**[12:33]** we really only need to cover that base

**[12:33]** we really only need to cover that base level or that base number of elementary

**[12:35]** level or that base number of elementary

**[12:35]** level or that base number of elementary functions. And we could just stack them

**[12:37]** functions. And we could just stack them

**[12:37]** functions. And we could just stack them or combine them in different ways in C++

**[12:39]** or combine them in different ways in C++

**[12:39]** or combine them in different ways in C++ the same way we do in Python. But you

**[12:42]** the same way we do in Python. But you

**[12:42]** the same way we do in Python. But you might even say to that that wait that

**[12:45]** might even say to that that wait that

**[12:45]** might even say to that that wait that elementary set of functions, it's still

**[12:46]** elementary set of functions, it's still

**[12:46]** elementary set of functions, it's still pretty large. And you would be 100%

**[12:48]** pretty large. And you would be 100%

**[12:48]** pretty large. And you would be 100% right. We need to cover everything from

**[12:51]** right. We need to cover everything from

**[12:51]** right. We need to cover everything from you know adding two things to like you

**[12:53]** you know adding two things to like you

**[12:53]** you know adding two things to like you know subtracting them to exponentiation

**[12:55]** know subtracting them to exponentiation

**[12:56]** know subtracting them to exponentiation to like you know some stuff that is like

**[12:58]** to like you know some stuff that is like

**[12:58]** to like you know some stuff that is like in native libraries like numpy


### [13:00 - 14:00]

**[13:00]** in native libraries like numpy

**[13:00]** in native libraries like numpy operations or pyarch operations and so

**[13:02]** operations or pyarch operations and so

**[13:02]** operations or pyarch operations and so yeah so you have a perfectly valid

**[13:04]** yeah so you have a perfectly valid

**[13:04]** yeah so you have a perfectly valid point. The only reason why that's

**[13:06]** point. The only reason why that's

**[13:06]** point. The only reason why that's tractable now is well we don't have to

**[13:08]** tractable now is well we don't have to

**[13:08]** tractable now is well we don't have to sit down and write the equivalent native

**[13:11]** sit down and write the equivalent native

**[13:11]** sit down and write the equivalent native code that does the same thing in Python

**[13:13]** code that does the same thing in Python

**[13:13]** code that does the same thing in Python anymore. we can simply have LLMs

**[13:15]** anymore. we can simply have LLMs

**[13:16]** anymore. we can simply have LLMs generate all the code that we need that

**[13:19]** generate all the code that we need that

**[13:19]** generate all the code that we need that translates a function from Python right

**[13:21]** translates a function from Python right

**[13:22]** translates a function from Python right into C++ and Rust. And so this gives us

**[13:25]** into C++ and Rust. And so this gives us

**[13:25]** into C++ and Rust. And so this gives us the ability to basically massroduce a

**[13:28]** the ability to basically massroduce a

**[13:28]** the ability to basically massroduce a lot of the operations that we we would

**[13:29]** lot of the operations that we we would

**[13:29]** lot of the operations that we we would otherwise have had to manually rewrite

**[13:32]** otherwise have had to manually rewrite

**[13:32]** otherwise have had to manually rewrite ourselves in native code. And so now

**[13:35]** ourselves in native code. And so now

**[13:35]** ourselves in native code. And so now that we've been able to propagate type

**[13:37]** that we've been able to propagate type

**[13:37]** that we've been able to propagate type information through our Python IR graph,

**[13:41]** information through our Python IR graph,

**[13:41]** information through our Python IR graph, we basically have all we need to simply

**[13:44]** we basically have all we need to simply

**[13:44]** we basically have all we need to simply generate actual C++ code that is correct

**[13:48]** generate actual C++ code that is correct

**[13:48]** generate actual C++ code that is correct and will compile. So here's what it

**[13:51]** and will compile. So here's what it

**[13:51]** and will compile. So here's what it actually looks like side by side. As you

**[13:53]** actually looks like side by side. As you

**[13:53]** actually looks like side by side. As you can see, I'm l just walking through and

**[13:55]** can see, I'm l just walking through and

**[13:55]** can see, I'm l just walking through and you can see where we're doing that, you

**[13:57]** you can see where we're doing that, you

**[13:57]** you can see where we're doing that, you know, list comprehension to add the

**[13:59]** know, list comprehension to add the

**[13:59]** know, list comprehension to add the prefixes to each string. You can see


### [14:00 - 15:00]

**[14:01]** prefixes to each string. You can see

**[14:01]** prefixes to each string. You can see where we are running the tokenizer to

**[14:03]** where we are running the tokenizer to

**[14:03]** where we are running the tokenizer to tokenize those input text into IDs. And

**[14:06]** tokenize those input text into IDs. And

**[14:06]** tokenize those input text into IDs. And you can now see we're running the model

**[14:08]** you can now see we're running the model

**[14:08]** you can now see we're running the model and returning the output embedding

**[14:10]** and returning the output embedding

**[14:10]** and returning the output embedding vectors or the embedding matrix. At this

**[14:13]** vectors or the embedding matrix. At this

**[14:13]** vectors or the embedding matrix. At this point, because we now have C++ source

**[14:15]** point, because we now have C++ source

**[14:15]** point, because we now have C++ source code, we can now compile this to run

**[14:18]** code, we can now compile this to run

**[14:18]** code, we can now compile this to run natively on any device or platform that

**[14:21]** natively on any device or platform that

**[14:21]** natively on any device or platform that we would ever want to run on. Simply

**[14:24]** we would ever want to run on. Simply

**[14:24]** we would ever want to run on. Simply because every piece of technology that

**[14:25]** because every piece of technology that

**[14:25]** because every piece of technology that you've ever touched has a C or C++

**[14:29]** you've ever touched has a C or C++

**[14:29]** you've ever touched has a C or C++ compiler. This is what gives us the

**[14:31]** compiler. This is what gives us the

**[14:31]** compiler. This is what gives us the ability to take high-level Python code

**[14:33]** ability to take high-level Python code

**[14:33]** ability to take high-level Python code and convert it into a form that is

**[14:35]** and convert it into a form that is

**[14:35]** and convert it into a form that is self-contained and that can now run

**[14:37]** self-contained and that can now run

**[14:37]** self-contained and that can now run anywhere at all. So let's go ahead and

**[14:39]** anywhere at all. So let's go ahead and

**[14:40]** anywhere at all. So let's go ahead and do that. And then what we're going to

**[14:41]** do that. And then what we're going to

**[14:41]** do that. And then what we're going to end up with on the other end is simply a

**[14:43]** end up with on the other end is simply a

**[14:43]** end up with on the other end is simply a uh dynamic library uh a shared object if

**[14:47]** uh dynamic library uh a shared object if

**[14:47]** uh dynamic library uh a shared object if you call it that that we can then load

**[14:49]** you call it that that we can then load

**[14:49]** you call it that that we can then load into a process and execute like any

**[14:51]** into a process and execute like any

**[14:51]** into a process and execute like any other code. Now comes the fun part.

**[14:54]** other code. Now comes the fun part.

**[14:54]** other code. Now comes the fun part. Let's figure out how to actually invoke

**[14:56]** Let's figure out how to actually invoke

**[14:56]** Let's figure out how to actually invoke or use our compiled embedding model from

**[14:59]** or use our compiled embedding model from

**[14:59]** or use our compiled embedding model from any language on any device. We're going


### [15:00 - 16:00]

**[15:02]** any language on any device. We're going

**[15:02]** any language on any device. We're going to go with JavaScript running on Node.js

**[15:04]** to go with JavaScript running on Node.js

**[15:04]** to go with JavaScript running on Node.js for this example. And so the very first

**[15:07]** for this example. And so the very first

**[15:07]** for this example. And so the very first step we want to do is figure out how to

**[15:09]** step we want to do is figure out how to

**[15:09]** step we want to do is figure out how to call in to our compiled library from

**[15:13]** call in to our compiled library from

**[15:13]** call in to our compiled library from JavaScript in Node.js. We can use FFI

**[15:16]** JavaScript in Node.js. We can use FFI

**[15:16]** JavaScript in Node.js. We can use FFI for this for this purpose. And so this

**[15:18]** for this for this purpose. And so this

**[15:18]** for this for this purpose. And so this is where you're able to effectively

**[15:20]** is where you're able to effectively

**[15:20]** is where you're able to effectively design bindings and declare that hey I'm

**[15:23]** design bindings and declare that hey I'm

**[15:23]** design bindings and declare that hey I'm loading this native library which has

**[15:26]** loading this native library which has

**[15:26]** loading this native library which has been compiled for my system and my

**[15:28]** been compiled for my system and my

**[15:28]** been compiled for my system and my architecture. It has this function with

**[15:31]** architecture. It has this function with

**[15:31]** architecture. It has this function with some name. In our case we already have a

**[15:33]** some name. In our case we already have a

**[15:33]** some name. In our case we already have a a function name and that function that

**[15:36]** a function name and that function that

**[15:36]** a function name and that function that native function has this signature. And

**[15:39]** native function has this signature. And

**[15:39]** native function has this signature. And so we're able to write a bunch of

**[15:40]** so we're able to write a bunch of

**[15:40]** so we're able to write a bunch of scaffolding code. this we figured out a

**[15:42]** scaffolding code. this we figured out a

**[15:42]** scaffolding code. this we figured out a way to standardize this across different

**[15:44]** way to standardize this across different

**[15:44]** way to standardize this across different different uh compiled functions to make

**[15:46]** different uh compiled functions to make

**[15:46]** different uh compiled functions to make it very easy for ourselves but this is

**[15:48]** it very easy for ourselves but this is

**[15:48]** it very easy for ourselves but this is pretty open-ended once you do you can

**[15:51]** pretty open-ended once you do you can

**[15:51]** pretty open-ended once you do you can basically point NodeJS or your

**[15:53]** basically point NodeJS or your

**[15:53]** basically point NodeJS or your JavaScript application to the location

**[15:55]** JavaScript application to the location

**[15:55]** JavaScript application to the location of that compiled library load it in and

**[15:58]** of that compiled library load it in and

**[15:58]** of that compiled library load it in and simply just invoke it like any other


### [16:00 - 17:00]

**[16:00]** simply just invoke it like any other

**[16:00]** simply just invoke it like any other thing when we do guess what we get our

**[16:03]** thing when we do guess what we get our

**[16:03]** thing when we do guess what we get our embedding matrix right there and for the

**[16:06]** embedding matrix right there and for the

**[16:06]** embedding matrix right there and for the final piece of the puzzle let's take it

**[16:08]** final piece of the puzzle let's take it

**[16:08]** final piece of the puzzle let's take it back to the top let's figure out how to

**[16:10]** back to the top let's figure out how to

**[16:10]** back to the top let's figure out how to expose our compiled embedding model

**[16:12]** expose our compiled embedding model

**[16:12]** expose our compiled embedding model through our OpenAI style client. So what

**[16:16]** through our OpenAI style client. So what

**[16:16]** through our OpenAI style client. So what we're going to do is create a class,

**[16:18]** we're going to do is create a class,

**[16:18]** we're going to do is create a class, just call it client. Within it, we'll

**[16:20]** just call it client. Within it, we'll

**[16:20]** just call it client. Within it, we'll create a nested class called embeddings.

**[16:22]** create a nested class called embeddings.

**[16:22]** create a nested class called embeddings. And within that, we will create a create

**[16:24]** And within that, we will create a create

**[16:24]** And within that, we will create a create function mirroring the official OpenAI

**[16:27]** function mirroring the official OpenAI

**[16:27]** function mirroring the official OpenAI client.create

**[16:29]** client.create

**[16:29]** client.create path. And so within that function, when

**[16:32]** path. And so within that function, when

**[16:32]** path. And so within that function, when the user passes in the model name, all

**[16:34]** the user passes in the model name, all

**[16:34]** the user passes in the model name, all we're going to do is simply just go from

**[16:36]** we're going to do is simply just go from

**[16:36]** we're going to do is simply just go from the name of that model to a path to the

**[16:40]** the name of that model to a path to the

**[16:40]** the name of that model to a path to the compiled binary that we just created

**[16:42]** compiled binary that we just created

**[16:42]** compiled binary that we just created from our C++ code generation. And with

**[16:46]** from our C++ code generation. And with

**[16:46]** from our C++ code generation. And with that, with the rest of all the uh FFI

**[16:48]** that, with the rest of all the uh FFI

**[16:48]** that, with the rest of all the uh FFI that we just implemented, we now have a

**[16:50]** that we just implemented, we now have a

**[16:50]** that we just implemented, we now have a way of taking the model, resolving it to

**[16:53]** way of taking the model, resolving it to

**[16:53]** way of taking the model, resolving it to a path to the library, loading that

**[16:54]** a path to the library, loading that

**[16:54]** a path to the library, loading that library in library in, and simply just

**[16:56]** library in library in, and simply just

**[16:56]** library in library in, and simply just executing it to get out our embedding

**[16:58]** executing it to get out our embedding

**[16:58]** executing it to get out our embedding matrix.


### [17:00 - 18:00]

**[17:00]** matrix.

**[17:00]** matrix. The final step is to simply massage the

**[17:02]** The final step is to simply massage the

**[17:02]** The final step is to simply massage the outputs so that it looks just like the

**[17:05]** outputs so that it looks just like the

**[17:05]** outputs so that it looks just like the outputs that the official OpenAI client

**[17:07]** outputs that the official OpenAI client

**[17:07]** outputs that the official OpenAI client gives you. And with this entire system

**[17:09]** gives you. And with this entire system

**[17:09]** gives you. And with this entire system in place, we have just recreated the

**[17:13]** in place, we have just recreated the

**[17:13]** in place, we have just recreated the official OpenAI client, but given it

**[17:15]** official OpenAI client, but given it

**[17:15]** official OpenAI client, but given it access to any open-source model that we

**[17:18]** access to any open-source model that we

**[17:18]** access to any open-source model that we can get into a Python function.


