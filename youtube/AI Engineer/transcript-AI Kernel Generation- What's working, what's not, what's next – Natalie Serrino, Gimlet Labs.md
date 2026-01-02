# AI Kernel Generation- What's working, what's not, what's next – Natalie Serrino, Gimlet Labs

**Video URL:** https://www.youtube.com/watch?v=6guQG_tGt0o

---

## Full Transcript

### [00:00 - 01:00]

**[00:24]** Hey everyone, how's it going?

**[00:24]** Hey everyone, how's it going? So, my name is Natalie. I'm a co-founder

**[00:26]** So, my name is Natalie. I'm a co-founder

**[00:26]** So, my name is Natalie. I'm a co-founder of Gimlet Labs and um yeah, just a

**[00:29]** of Gimlet Labs and um yeah, just a

**[00:29]** of Gimlet Labs and um yeah, just a little bit of background about why

**[00:30]** little bit of background about why

**[00:30]** little bit of background about why Gimlet's looking at AI generated

**[00:32]** Gimlet's looking at AI generated

**[00:32]** Gimlet's looking at AI generated kernels. Let's just get right to it. Um

**[00:34]** kernels. Let's just get right to it. Um

**[00:34]** kernels. Let's just get right to it. Um we're building an agentic inference

**[00:36]** we're building an agentic inference

**[00:36]** we're building an agentic inference cloud focused on performance and

**[00:37]** cloud focused on performance and

**[00:37]** cloud focused on performance and efficiency. And the thing that we've

**[00:39]** efficiency. And the thing that we've

**[00:39]** efficiency. And the thing that we've seen with all these talks so far is with

**[00:41]** seen with all these talks so far is with

**[00:41]** seen with all these talks so far is with agents, they're not just one chat model.

**[00:44]** agents, they're not just one chat model.

**[00:44]** agents, they're not just one chat model. They're complex pipelines of multiple

**[00:46]** They're complex pipelines of multiple

**[00:46]** They're complex pipelines of multiple models, multiple stages, tool calls, and

**[00:49]** models, multiple stages, tool calls, and

**[00:49]** models, multiple stages, tool calls, and the compute backing these is inherently

**[00:51]** the compute backing these is inherently

**[00:51]** the compute backing these is inherently should be heterogeneous. So what we do

**[00:53]** should be heterogeneous. So what we do

**[00:53]** should be heterogeneous. So what we do is we automatically split up and

**[00:55]** is we automatically split up and

**[00:55]** is we automatically split up and orchestrate these agentic workloads

**[00:57]** orchestrate these agentic workloads

**[00:58]** orchestrate these agentic workloads across optimal hardware which can be

**[00:59]** across optimal hardware which can be

**[00:59]** across optimal hardware which can be different vendors and different sizes.


### [01:00 - 02:00]

**[01:02]** different vendors and different sizes.

**[01:02]** different vendors and different sizes. This can present a problem at the kernel

**[01:04]** This can present a problem at the kernel

**[01:04]** This can present a problem at the kernel level because a lot of times you have

**[01:06]** level because a lot of times you have

**[01:06]** level because a lot of times you have models that are really optimized just

**[01:08]** models that are really optimized just

**[01:08]** models that are really optimized just for one hardware. So what we started

**[01:09]** for one hardware. So what we started

**[01:09]** for one hardware. So what we started looking at is can we use AI to help

**[01:12]** looking at is can we use AI to help

**[01:12]** looking at is can we use AI to help automatically port different segments of

**[01:14]** automatically port different segments of

**[01:14]** automatically port different segments of aentic workloads to hardware that it

**[01:17]** aentic workloads to hardware that it

**[01:17]** aentic workloads to hardware that it hasn't necessarily been optimized for.

**[01:21]** hasn't necessarily been optimized for.

**[01:21]** hasn't necessarily been optimized for. So just to clarify something really

**[01:23]** So just to clarify something really

**[01:23]** So just to clarify something really quick because we run into this a lot.

**[01:25]** quick because we run into this a lot.

**[01:25]** quick because we run into this a lot. What do I mean by kernels? I do not mean

**[01:29]** What do I mean by kernels? I do not mean

**[01:29]** What do I mean by kernels? I do not mean AI generating operating systems like the

**[01:32]** AI generating operating systems like the

**[01:32]** AI generating operating systems like the Linux kernel or things like that. What I

**[01:34]** Linux kernel or things like that. What I

**[01:34]** Linux kernel or things like that. What I mean is kernels at the sense of like

**[01:36]** mean is kernels at the sense of like

**[01:36]** mean is kernels at the sense of like transformer architecture like the

**[01:39]** transformer architecture like the

**[01:39]** transformer architecture like the individual like functions that perform

**[01:41]** individual like functions that perform

**[01:41]** individual like functions that perform like massive parallel computations

**[01:43]** like massive parallel computations

**[01:43]** like massive parallel computations leveraging like all the crazy amounts of

**[01:45]** leveraging like all the crazy amounts of

**[01:45]** leveraging like all the crazy amounts of threads that GPUs have. So yes, people

**[01:48]** threads that GPUs have. So yes, people

**[01:48]** threads that GPUs have. So yes, people be like, "Oh, how are you going to

**[01:49]** be like, "Oh, how are you going to

**[01:49]** be like, "Oh, how are you going to generate an operating system?" I think

**[01:51]** generate an operating system?" I think

**[01:51]** generate an operating system?" I think maybe we're not quite there yet, but one

**[01:52]** maybe we're not quite there yet, but one

**[01:52]** maybe we're not quite there yet, but one day.

**[01:55]** day.

**[01:55]** day. So why use AI to do this? So I think

**[01:58]** So why use AI to do this? So I think

**[01:58]** So why use AI to do this? So I think there's a few reasons. So we know that


### [02:00 - 03:00]

**[02:01]** there's a few reasons. So we know that

**[02:01]** there's a few reasons. So we know that optimizing low-level kernels can make

**[02:04]** optimizing low-level kernels can make

**[02:04]** optimizing low-level kernels can make workloads like ML workloads

**[02:06]** workloads like ML workloads

**[02:06]** workloads like ML workloads significantly faster. So here we have

**[02:07]** significantly faster. So here we have

**[02:07]** significantly faster. So here we have like it's probably too small to see but

**[02:10]** like it's probably too small to see but

**[02:10]** like it's probably too small to see but it's a blog from Nvidia where they

**[02:12]** it's a blog from Nvidia where they

**[02:12]** it's a blog from Nvidia where they implemented a different attention and it

**[02:15]** implemented a different attention and it

**[02:15]** implemented a different attention and it allowed them to like get 3x throughput

**[02:17]** allowed them to like get 3x throughput

**[02:17]** allowed them to like get 3x throughput on a llama model. So these like

**[02:19]** on a llama model. So these like

**[02:19]** on a llama model. So these like implementations can make a major

**[02:21]** implementations can make a major

**[02:21]** implementations can make a major difference from a performance

**[02:22]** difference from a performance

**[02:22]** difference from a performance perspective. But at the same time if you

**[02:24]** perspective. But at the same time if you

**[02:24]** perspective. But at the same time if you just search Twitter everyone's whining

**[02:26]** just search Twitter everyone's whining

**[02:26]** just search Twitter everyone's whining about how it's impossible to find these

**[02:27]** about how it's impossible to find these

**[02:27]** about how it's impossible to find these people and the people that exist are

**[02:29]** people and the people that exist are

**[02:29]** people and the people that exist are like really overt taxed with so much to

**[02:31]** like really overt taxed with so much to

**[02:31]** like really overt taxed with so much to do, so much work. There's just not

**[02:33]** do, so much work. There's just not

**[02:33]** do, so much work. There's just not enough experts to be able to solve every

**[02:35]** enough experts to be able to solve every

**[02:35]** enough experts to be able to solve every problem in this in this space right now.

**[02:39]** problem in this in this space right now.

**[02:39]** problem in this in this space right now. And the problem explodes because you

**[02:41]** And the problem explodes because you

**[02:41]** And the problem explodes because you have so many frameworks and so many ways

**[02:43]** have so many frameworks and so many ways

**[02:44]** have so many frameworks and so many ways to write kernels from things like CUDA

**[02:46]** to write kernels from things like CUDA

**[02:46]** to write kernels from things like CUDA and like Triton to Palace to things like

**[02:49]** and like Triton to Palace to things like

**[02:49]** and like Triton to Palace to things like that are device specific like Metal and

**[02:52]** that are device specific like Metal and

**[02:52]** that are device specific like Metal and you have different hardware platforms

**[02:53]** you have different hardware platforms

**[02:53]** you have different hardware platforms too and each of these hardware platforms

**[02:55]** too and each of these hardware platforms

**[02:55]** too and each of these hardware platforms even within a single vendor has

**[02:57]** even within a single vendor has

**[02:57]** even within a single vendor has different characteristics. We've seen

**[02:59]** different characteristics. We've seen

**[02:59]** different characteristics. We've seen for example that some of the new um like


### [03:00 - 04:00]

**[03:02]** for example that some of the new um like

**[03:02]** for example that some of the new um like hardware from Nvidia like some of the

**[03:04]** hardware from Nvidia like some of the

**[03:04]** hardware from Nvidia like some of the old kind of like DSLs weren't working as

**[03:06]** old kind of like DSLs weren't working as

**[03:06]** old kind of like DSLs weren't working as well on it because the different

**[03:08]** well on it because the different

**[03:08]** well on it because the different hardware has different properties it has

**[03:10]** hardware has different properties it has

**[03:10]** hardware has different properties it has different features it has different

**[03:11]** different features it has different

**[03:11]** different features it has different characteristics different cache sizes

**[03:13]** characteristics different cache sizes

**[03:13]** characteristics different cache sizes etc all of which impact the optimized

**[03:15]** etc all of which impact the optimized

**[03:15]** etc all of which impact the optimized implementation from a kernel perspective

**[03:20]** implementation from a kernel perspective

**[03:20]** implementation from a kernel perspective so we and many others in the space have

**[03:23]** so we and many others in the space have

**[03:23]** so we and many others in the space have thought it would be great if AI could

**[03:25]** thought it would be great if AI could

**[03:25]** thought it would be great if AI could help us with this problem where you

**[03:27]** help us with this problem where you

**[03:28]** help us with this problem where you could potent potentially give it PyTorch

**[03:29]** could potent potentially give it PyTorch

**[03:29]** could potent potentially give it PyTorch code and then generate optimized

**[03:32]** code and then generate optimized

**[03:32]** code and then generate optimized implementations for whatever hardware

**[03:33]** implementations for whatever hardware

**[03:34]** implementations for whatever hardware you're trying to run that workload on.

**[03:41]** So I think when you're trying to use an

**[03:41]** So I think when you're trying to use an agent for something, you have to start

**[03:42]** agent for something, you have to start

**[03:42]** agent for something, you have to start with what the human workflow is. And the

**[03:44]** with what the human workflow is. And the

**[03:44]** with what the human workflow is. And the human workflow today, when you have that

**[03:47]** human workflow today, when you have that

**[03:47]** human workflow today, when you have that like really hardcore kernel expert,

**[03:49]** like really hardcore kernel expert,

**[03:50]** like really hardcore kernel expert, let's say they're trying to port a new

**[03:51]** let's say they're trying to port a new

**[03:52]** let's say they're trying to port a new uh like workload over to Metal, right?

**[03:54]** uh like workload over to Metal, right?

**[03:54]** uh like workload over to Metal, right? What they'll do is they'll say, "Okay, I

**[03:57]** What they'll do is they'll say, "Okay, I

**[03:57]** What they'll do is they'll say, "Okay, I have this implementation. Maybe I have a

**[03:58]** have this implementation. Maybe I have a

**[03:58]** have this implementation. Maybe I have a CUDA version, maybe I don't. And I'm


### [04:00 - 05:00]

**[04:01]** CUDA version, maybe I don't. And I'm

**[04:01]** CUDA version, maybe I don't. And I'm going to try something. I'll see if it

**[04:03]** going to try something. I'll see if it

**[04:03]** going to try something. I'll see if it compiles." Most of the time, maybe not.

**[04:06]** compiles." Most of the time, maybe not.

**[04:06]** compiles." Most of the time, maybe not. I'll see if it runs.

**[04:08]** I'll see if it runs.

**[04:08]** I'll see if it runs. If see if it's correct, and if none of

**[04:11]** If see if it's correct, and if none of

**[04:11]** If see if it's correct, and if none of those are the case, you just pass that

**[04:12]** those are the case, you just pass that

**[04:12]** those are the case, you just pass that back into the human context, so to

**[04:14]** back into the human context, so to

**[04:14]** back into the human context, so to speak. And then once you get something

**[04:16]** speak. And then once you get something

**[04:16]** speak. And then once you get something that's working, then you start looking

**[04:17]** that's working, then you start looking

**[04:17]** that's working, then you start looking at the profiling information in depth

**[04:19]** at the profiling information in depth

**[04:19]** at the profiling information in depth and just hammering down like this is the

**[04:21]** and just hammering down like this is the

**[04:21]** and just hammering down like this is the bottleneck now. This is the bottleneck

**[04:23]** bottleneck now. This is the bottleneck

**[04:23]** bottleneck now. This is the bottleneck now. This is the bottle of the mic now.

**[04:24]** now. This is the bottle of the mic now.

**[04:24]** now. This is the bottle of the mic now. It's a very iterative process.

**[04:28]** It's a very iterative process.

**[04:28]** It's a very iterative process. So I think that you know basically the

**[04:31]** So I think that you know basically the

**[04:31]** So I think that you know basically the idea here is to put AI as the as the

**[04:34]** idea here is to put AI as the as the

**[04:34]** idea here is to put AI as the as the kind of like

**[04:36]** kind of like

**[04:36]** kind of like where the human would go in that same

**[04:38]** where the human would go in that same

**[04:38]** where the human would go in that same loop right so the agentic flow here is

**[04:40]** loop right so the agentic flow here is

**[04:40]** loop right so the agentic flow here is to make sure it compiles and it executes

**[04:43]** to make sure it compiles and it executes

**[04:43]** to make sure it compiles and it executes and it's correct and then from there

**[04:45]** and it's correct and then from there

**[04:45]** and it's correct and then from there optimizing it.

**[04:47]** optimizing it.

**[04:47]** optimizing it. So this is something that I would say is

**[04:49]** So this is something that I would say is

**[04:49]** So this is something that I would say is like very new technology. There's a lot

**[04:51]** like very new technology. There's a lot

**[04:51]** like very new technology. There's a lot of interest here, but there's some

**[04:53]** of interest here, but there's some

**[04:53]** of interest here, but there's some things that it's good at and some things

**[04:55]** things that it's good at and some things

**[04:55]** things that it's good at and some things that it's still kind of in development

**[04:57]** that it's still kind of in development

**[04:57]** that it's still kind of in development for. And so, let's dive into some of the

**[04:59]** for. And so, let's dive into some of the

**[04:59]** for. And so, let's dive into some of the specifics.


### [05:00 - 06:00]

**[05:01]** specifics.

**[05:01]** specifics. So, this is a quick demo of our system.

**[05:03]** So, this is a quick demo of our system.

**[05:03]** So, this is a quick demo of our system. It the font's kind of small, but we're

**[05:05]** It the font's kind of small, but we're

**[05:05]** It the font's kind of small, but we're passing into a CLI tool, a PyTorch

**[05:08]** passing into a CLI tool, a PyTorch

**[05:08]** passing into a CLI tool, a PyTorch workload, targeting it to an H100, and

**[05:11]** workload, targeting it to an H100, and

**[05:11]** workload, targeting it to an H100, and the system had explored a bunch of

**[05:13]** the system had explored a bunch of

**[05:13]** the system had explored a bunch of candidate optimizations. It's comparing

**[05:15]** candidate optimizations. It's comparing

**[05:15]** candidate optimizations. It's comparing to eager mode and torch compile and it

**[05:17]** to eager mode and torch compile and it

**[05:17]** to eager mode and torch compile and it found one uh candidate that was 22%

**[05:20]** found one uh candidate that was 22%

**[05:20]** found one uh candidate that was 22% faster than the torch compile baseline.

**[05:23]** faster than the torch compile baseline.

**[05:23]** faster than the torch compile baseline. So this was a real case. It just sped up

**[05:25]** So this was a real case. It just sped up

**[05:25]** So this was a real case. It just sped up because it actually took about 20

**[05:27]** because it actually took about 20

**[05:27]** because it actually took about 20 minutes.

**[05:31]** So there's some challenges though with

**[05:31]** So there's some challenges though with measuring these agents at kernel

**[05:33]** measuring these agents at kernel

**[05:33]** measuring these agents at kernel synthesis. So um like first of all you

**[05:36]** synthesis. So um like first of all you

**[05:36]** synthesis. So um like first of all you have to figure out what your definition

**[05:37]** have to figure out what your definition

**[05:37]** have to figure out what your definition of correct is when you're dealing with

**[05:39]** of correct is when you're dealing with

**[05:39]** of correct is when you're dealing with floating point. This is always a

**[05:40]** floating point. This is always a

**[05:40]** floating point. This is always a question. You can do different types of

**[05:42]** question. You can do different types of

**[05:42]** question. You can do different types of tolerances, but you also need to make

**[05:44]** tolerances, but you also need to make

**[05:44]** tolerances, but you also need to make sure your input sizes are well selected.

**[05:46]** sure your input sizes are well selected.

**[05:46]** sure your input sizes are well selected. If you're only passing in really small

**[05:48]** If you're only passing in really small

**[05:48]** If you're only passing in really small input sizes, it can cause problems with

**[05:50]** input sizes, it can cause problems with

**[05:50]** input sizes, it can cause problems with the benchmarking where you're measuring

**[05:51]** the benchmarking where you're measuring

**[05:51]** the benchmarking where you're measuring the overhead, not the actual kernel as

**[05:53]** the overhead, not the actual kernel as

**[05:53]** the overhead, not the actual kernel as the critical path.

**[05:55]** the critical path.

**[05:56]** the critical path. You also have to make sure you're

**[05:57]** You also have to make sure you're

**[05:57]** You also have to make sure you're reliably measuring performance. So, if

**[05:59]** reliably measuring performance. So, if

**[05:59]** reliably measuring performance. So, if you just do a naive timer start on your


### [06:00 - 07:00]

**[06:02]** you just do a naive timer start on your

**[06:02]** you just do a naive timer start on your implementation, it's probably going to

**[06:04]** implementation, it's probably going to

**[06:04]** implementation, it's probably going to be wrong. And there was a great blog

**[06:06]** be wrong. And there was a great blog

**[06:06]** be wrong. And there was a great blog that had a diagram for this because

**[06:08]** that had a diagram for this because

**[06:08]** that had a diagram for this because you're basically measuring the launch

**[06:10]** you're basically measuring the launch

**[06:10]** you're basically measuring the launch time, not the execution time. So there's

**[06:12]** time, not the execution time. So there's

**[06:12]** time, not the execution time. So there's a bunch of kind of gotchas like that

**[06:14]** a bunch of kind of gotchas like that

**[06:14]** a bunch of kind of gotchas like that that when you're building an agentic

**[06:15]** that when you're building an agentic

**[06:15]** that when you're building an agentic system like this, you have to be really

**[06:17]** system like this, you have to be really

**[06:17]** system like this, you have to be really really careful about catching doing

**[06:19]** really careful about catching doing

**[06:19]** really careful about catching doing things like warm-ups and cache clearing

**[06:21]** things like warm-ups and cache clearing

**[06:21]** things like warm-ups and cache clearing because a lot of times you'll have

**[06:23]** because a lot of times you'll have

**[06:23]** because a lot of times you'll have you'll have the original implementation

**[06:24]** you'll have the original implementation

**[06:24]** you'll have the original implementation run and then the new implementation run

**[06:26]** run and then the new implementation run

**[06:26]** run and then the new implementation run and then the original one's result is

**[06:28]** and then the original one's result is

**[06:28]** and then the original one's result is cached and the new one fetches it. So

**[06:30]** cached and the new one fetches it. So

**[06:30]** cached and the new one fetches it. So you have all kinds of things like that

**[06:31]** you have all kinds of things like that

**[06:31]** you have all kinds of things like that that you have to be really neurotic

**[06:32]** that you have to be really neurotic

**[06:32]** that you have to be really neurotic about otherwise you might get bad

**[06:34]** about otherwise you might get bad

**[06:34]** about otherwise you might get bad results.

**[06:35]** results.

**[06:35]** results. You also need great benchmarks for this.

**[06:37]** You also need great benchmarks for this.

**[06:37]** You also need great benchmarks for this. I think that someone said earlier that

**[06:39]** I think that someone said earlier that

**[06:39]** I think that someone said earlier that there's not a ton of examples of

**[06:40]** there's not a ton of examples of

**[06:40]** there's not a ton of examples of low-level kernels across all these

**[06:42]** low-level kernels across all these

**[06:42]** low-level kernels across all these different hardware platforms. And so the

**[06:44]** different hardware platforms. And so the

**[06:44]** different hardware platforms. And so the input data is a challenge and also

**[06:46]** input data is a challenge and also

**[06:46]** input data is a challenge and also benchmarking it is a challenge. Like how

**[06:48]** benchmarking it is a challenge. Like how

**[06:48]** benchmarking it is a challenge. Like how do you know if your agent is better? You

**[06:50]** do you know if your agent is better? You

**[06:50]** do you know if your agent is better? You change the prompt to it. How do you

**[06:51]** change the prompt to it. How do you

**[06:51]** change the prompt to it. How do you know? It's the same story we hear with

**[06:53]** know? It's the same story we hear with

**[06:53]** know? It's the same story we hear with every agent here basically.


### [07:00 - 08:00]

**[07:00]** So we have some preliminary results on

**[07:00]** So we have some preliminary results on that we're sharing right now on Apple's

**[07:02]** that we're sharing right now on Apple's

**[07:02]** that we're sharing right now on Apple's um M4 uh using the metal framework. Um

**[07:05]** um M4 uh using the metal framework. Um

**[07:05]** um M4 uh using the metal framework. Um and this is on the kernel bench

**[07:06]** and this is on the kernel bench

**[07:06]** and this is on the kernel bench benchmark the v0.1 version of it which

**[07:09]** benchmark the v0.1 version of it which

**[07:09]** benchmark the v0.1 version of it which is the latest one. So what we can see

**[07:12]** is the latest one. So what we can see

**[07:12]** is the latest one. So what we can see here is results across 250 problems and

**[07:15]** here is results across 250 problems and

**[07:15]** here is results across 250 problems and it compares to either torch compile or

**[07:18]** it compares to either torch compile or

**[07:18]** it compares to either torch compile or eager mode depending on which one of

**[07:20]** eager mode depending on which one of

**[07:20]** eager mode depending on which one of those is faster. So with the kernel

**[07:22]** those is faster. So with the kernel

**[07:22]** those is faster. So with the kernel bench data set, we have different tiers

**[07:25]** bench data set, we have different tiers

**[07:25]** bench data set, we have different tiers of problems with L1 being the easiest or

**[07:28]** of problems with L1 being the easiest or

**[07:28]** of problems with L1 being the easiest or simplest rather and L3 being like more

**[07:30]** simplest rather and L3 being like more

**[07:30]** simplest rather and L3 being like more complex. So what we can see for the

**[07:32]** complex. So what we can see for the

**[07:32]** complex. So what we can see for the standalone agent is that we see an

**[07:34]** standalone agent is that we see an

**[07:34]** standalone agent is that we see an average speed up of about 25% or 24%.

**[07:39]** average speed up of about 25% or 24%.

**[07:39]** average speed up of about 25% or 24%. And the sweet spot is those moderately

**[07:41]** And the sweet spot is those moderately

**[07:41]** And the sweet spot is those moderately complex problems. It seems honestly the

**[07:43]** complex problems. It seems honestly the

**[07:43]** complex problems. It seems honestly the same as like a lot of coding problems

**[07:45]** same as like a lot of coding problems

**[07:45]** same as like a lot of coding problems where it's good at moderately complex

**[07:46]** where it's good at moderately complex

**[07:46]** where it's good at moderately complex things, but then you push it too far and

**[07:48]** things, but then you push it too far and

**[07:48]** things, but then you push it too far and the performance drops off. So, an

**[07:51]** the performance drops off. So, an

**[07:51]** the performance drops off. So, an interesting challenge here is going to

**[07:52]** interesting challenge here is going to

**[07:52]** interesting challenge here is going to be how do we make these agents perform

**[07:54]** be how do we make these agents perform

**[07:54]** be how do we make these agents perform better on more complex problems that

**[07:56]** better on more complex problems that

**[07:56]** better on more complex problems that they're going to have to break down and

**[07:58]** they're going to have to break down and

**[07:58]** they're going to have to break down and execute.


### [08:00 - 09:00]

**[08:05]** There we go. Um, let's talk about a

**[08:05]** There we go. Um, let's talk about a couple of examples because I love to

**[08:07]** couple of examples because I love to

**[08:07]** couple of examples because I love to just see example code. So, this was a

**[08:09]** just see example code. So, this was a

**[08:09]** just see example code. So, this was a success case where the model found a

**[08:12]** success case where the model found a

**[08:12]** success case where the model found a case where we could do kernel fusion. So

**[08:14]** case where we could do kernel fusion. So

**[08:14]** case where we could do kernel fusion. So for those that aren't that familiar with

**[08:15]** for those that aren't that familiar with

**[08:15]** for those that aren't that familiar with GPU kernels, kernel fusion is one of the

**[08:18]** GPU kernels, kernel fusion is one of the

**[08:18]** GPU kernels, kernel fusion is one of the most go-to techniques in kernel

**[08:19]** most go-to techniques in kernel

**[08:19]** most go-to techniques in kernel optimization where you say I have two

**[08:21]** optimization where you say I have two

**[08:21]** optimization where you say I have two kernels. Let's say in this case it was

**[08:23]** kernels. Let's say in this case it was

**[08:23]** kernels. Let's say in this case it was like a convolution softmax bias scaling

**[08:27]** like a convolution softmax bias scaling

**[08:27]** like a convolution softmax bias scaling and sigmoid. So those were five ops and

**[08:30]** and sigmoid. So those were five ops and

**[08:30]** and sigmoid. So those were five ops and what the agent did was it took four of

**[08:32]** what the agent did was it took four of

**[08:32]** what the agent did was it took four of those ops and instead of running

**[08:34]** those ops and instead of running

**[08:34]** those ops and instead of running individual functions for those it made a

**[08:36]** individual functions for those it made a

**[08:36]** individual functions for those it made a mega function that compacted them all

**[08:38]** mega function that compacted them all

**[08:38]** mega function that compacted them all together. So kernel fusion isn't new.

**[08:41]** together. So kernel fusion isn't new.

**[08:41]** together. So kernel fusion isn't new. It's something that torch compile

**[08:42]** It's something that torch compile

**[08:42]** It's something that torch compile already does quite well, but it's a

**[08:45]** already does quite well, but it's a

**[08:45]** already does quite well, but it's a common way that we found agents can

**[08:46]** common way that we found agents can

**[08:46]** common way that we found agents can speed up these workloads because you can

**[08:48]** speed up these workloads because you can

**[08:48]** speed up these workloads because you can really customize it to the specific use

**[08:49]** really customize it to the specific use

**[08:49]** really customize it to the specific use case. So, this result achieved a 40%

**[08:53]** case. So, this result achieved a 40%

**[08:53]** case. So, this result achieved a 40% speed up over the baseline on the M4.

**[08:57]** speed up over the baseline on the M4.

**[08:57]** speed up over the baseline on the M4. And just kind of like zooming into what

**[08:59]** And just kind of like zooming into what


### [09:00 - 10:00]

**[09:00]** And just kind of like zooming into what happened, the agent wrote a fused op. So

**[09:03]** happened, the agent wrote a fused op. So

**[09:04]** happened, the agent wrote a fused op. So it basically wrote like C++ code that it

**[09:06]** it basically wrote like C++ code that it

**[09:06]** it basically wrote like C++ code that it put as kind of an inline string with the

**[09:08]** put as kind of an inline string with the

**[09:08]** put as kind of an inline string with the PyTorch code and then it called that

**[09:12]** PyTorch code and then it called that

**[09:12]** PyTorch code and then it called that fused operation in the forward pass of

**[09:15]** fused operation in the forward pass of

**[09:15]** fused operation in the forward pass of the model and then that fused

**[09:17]** the model and then that fused

**[09:17]** the model and then that fused implementation we can see a snippet of

**[09:19]** implementation we can see a snippet of

**[09:19]** implementation we can see a snippet of it up here where it's basically taking

**[09:22]** it up here where it's basically taking

**[09:22]** it up here where it's basically taking those four ops and putting them together

**[09:23]** those four ops and putting them together

**[09:23]** those four ops and putting them together in one mega op. And so this was done

**[09:27]** in one mega op. And so this was done

**[09:27]** in one mega op. And so this was done automatically.

**[09:32]** Sometimes though like writing low-level

**[09:32]** Sometimes though like writing low-level kernels isn't the best optimization that

**[09:33]** kernels isn't the best optimization that

**[09:33]** kernels isn't the best optimization that we can get. We had another case which

**[09:35]** we can get. We had another case which

**[09:36]** we can get. We had another case which was on a level one problem which

**[09:37]** was on a level one problem which

**[09:38]** was on a level one problem which basically improved the performance by

**[09:39]** basically improved the performance by

**[09:39]** basically improved the performance by 80%. And the the insight the agent had

**[09:43]** 80%. And the the insight the agent had

**[09:43]** 80%. And the the insight the agent had in this case was the operation in metal

**[09:47]** in this case was the operation in metal

**[09:47]** in this case was the operation in metal for average pool 1D was not as optimized

**[09:50]** for average pool 1D was not as optimized

**[09:50]** for average pool 1D was not as optimized as some other ops that are much more

**[09:52]** as some other ops that are much more

**[09:52]** as some other ops that are much more optimized on metal. So what it did was

**[09:55]** optimized on metal. So what it did was

**[09:55]** optimized on metal. So what it did was it actually rewrote the pietorch code to

**[09:57]** it actually rewrote the pietorch code to

**[09:57]** it actually rewrote the pietorch code to use the more optimized op and reexpress

**[09:59]** use the more optimized op and reexpress

**[09:59]** use the more optimized op and reexpress the same problem in a different way.


### [10:00 - 11:00]

**[10:03]** the same problem in a different way.

**[10:03]** the same problem in a different way. So to dive into this um the average pool

**[10:06]** So to dive into this um the average pool

**[10:06]** So to dive into this um the average pool 1D is basically taking averages across

**[10:08]** 1D is basically taking averages across

**[10:08]** 1D is basically taking averages across like one dimension. So like you can see

**[10:11]** like one dimension. So like you can see

**[10:11]** like one dimension. So like you can see that that input vector could produce the

**[10:14]** that that input vector could produce the

**[10:14]** that that input vector could produce the output vector with five and seven

**[10:16]** output vector with five and seven

**[10:16]** output vector with five and seven averaging to six and so on.

**[10:19]** averaging to six and so on.

**[10:19]** averaging to six and so on. So if you express that same thing as a

**[10:21]** So if you express that same thing as a

**[10:21]** So if you express that same thing as a convolution, you can get the same

**[10:23]** convolution, you can get the same

**[10:23]** convolution, you can get the same result.

**[10:25]** result.

**[10:25]** result. So if you do the math, it will lead to

**[10:26]** So if you do the math, it will lead to

**[10:26]** So if you do the math, it will lead to that same result. And so that's what the

**[10:28]** that same result. And so that's what the

**[10:28]** that same result. And so that's what the agent did. Basically what it did was it

**[10:31]** agent did. Basically what it did was it

**[10:31]** agent did. Basically what it did was it said, hey, instead of doing the original

**[10:33]** said, hey, instead of doing the original

**[10:33]** said, hey, instead of doing the original call to the baseline op, let's generate

**[10:36]** call to the baseline op, let's generate

**[10:36]** call to the baseline op, let's generate that weights matrix and execute this as

**[10:38]** that weights matrix and execute this as

**[10:38]** that weights matrix and execute this as a convolution because I know that that's

**[10:40]** a convolution because I know that that's

**[10:40]** a convolution because I know that that's really fast on metal.

**[10:46]** There's also an interesting algorithmic

**[10:46]** There's also an interesting algorithmic optimization case. This was for a level

**[10:48]** optimization case. This was for a level

**[10:48]** optimization case. This was for a level three problem. So it was more complex

**[10:50]** three problem. So it was more complex

**[10:50]** three problem. So it was more complex where basically the agent figured out

**[10:51]** where basically the agent figured out

**[10:51]** where basically the agent figured out that it could combine two operations

**[10:54]** that it could combine two operations

**[10:54]** that it could combine two operations into a single operation at the PyTorch

**[10:56]** into a single operation at the PyTorch

**[10:56]** into a single operation at the PyTorch level, not even using low-level kernels.


### [11:00 - 12:00]

**[11:04]** So what we can see is that basically it

**[11:04]** So what we can see is that basically it fused it, it rewrote it as Python code

**[11:07]** fused it, it rewrote it as Python code

**[11:07]** fused it, it rewrote it as Python code and calls that single convolution and

**[11:09]** and calls that single convolution and

**[11:09]** and calls that single convolution and that's a lot more efficient because you

**[11:10]** that's a lot more efficient because you

**[11:10]** that's a lot more efficient because you don't have to launch as many ops.

**[11:16]** But this does not always work. This is

**[11:16]** But this does not always work. This is not a silver bullet and I think that's

**[11:18]** not a silver bullet and I think that's

**[11:18]** not a silver bullet and I think that's really important to emphasize. So a case

**[11:20]** really important to emphasize. So a case

**[11:20]** really important to emphasize. So a case where the agent totally faceplanted was

**[11:22]** where the agent totally faceplanted was

**[11:22]** where the agent totally faceplanted was on matrix multiplication and it was it

**[11:26]** on matrix multiplication and it was it

**[11:26]** on matrix multiplication and it was it wrote a custom CUDA kernel for this but

**[11:27]** wrote a custom CUDA kernel for this but

**[11:27]** wrote a custom CUDA kernel for this but it was a lot slower than the baseline.

**[11:30]** it was a lot slower than the baseline.

**[11:30]** it was a lot slower than the baseline. And the thing is with this is matrix

**[11:31]** And the thing is with this is matrix

**[11:31]** And the thing is with this is matrix multiply is one of the most hand

**[11:34]** multiply is one of the most hand

**[11:34]** multiply is one of the most hand optimized ops that exists. So it's not

**[11:37]** optimized ops that exists. So it's not

**[11:37]** optimized ops that exists. So it's not that surprising that an agent would not

**[11:40]** that surprising that an agent would not

**[11:40]** that surprising that an agent would not do as well as something that a human

**[11:41]** do as well as something that a human

**[11:41]** do as well as something that a human expert spent a long time on. So, this is

**[11:44]** expert spent a long time on. So, this is

**[11:44]** expert spent a long time on. So, this is an area that it did not work.

**[11:48]** an area that it did not work.

**[11:48]** an area that it did not work. Another case was a case that we saw

**[11:51]** Another case was a case that we saw

**[11:51]** Another case was a case that we saw which had a 71,000x speed up. And

**[11:53]** which had a 71,000x speed up. And

**[11:54]** which had a 71,000x speed up. And anything like that should trigger your

**[11:55]** anything like that should trigger your

**[11:55]** anything like that should trigger your suspicion brain.

**[11:57]** suspicion brain.

**[11:57]** suspicion brain. Wow. 71,000. Great. We're done. It's,

**[11:59]** Wow. 71,000. Great. We're done. It's,


### [12:00 - 13:00]

**[12:00]** Wow. 71,000. Great. We're done. It's, you know, this technology is worth

**[12:01]** you know, this technology is worth

**[12:01]** you know, this technology is worth billions of dollars, right? No. So,

**[12:03]** billions of dollars, right? No. So,

**[12:03]** billions of dollars, right? No. So, basically, what happened? So, this

**[12:07]** basically, what happened? So, this

**[12:07]** basically, what happened? So, this operation is basically saying, give me

**[12:09]** operation is basically saying, give me

**[12:09]** operation is basically saying, give me inputs and I'm going to make sure they

**[12:10]** inputs and I'm going to make sure they

**[12:10]** inputs and I'm going to make sure they fall betweengative -1 and one. Okay,

**[12:13]** fall betweengative -1 and one. Okay,

**[12:13]** fall betweengative -1 and one. Okay, that's what the operation being tested

**[12:15]** that's what the operation being tested

**[12:16]** that's what the operation being tested was.

**[12:18]** was.

**[12:18]** was. So the agent figured out that for all of

**[12:21]** So the agent figured out that for all of

**[12:21]** So the agent figured out that for all of the test cases, this was already the

**[12:23]** the test cases, this was already the

**[12:23]** the test cases, this was already the case. So it wrote a nice long comment

**[12:25]** case. So it wrote a nice long comment

**[12:25]** case. So it wrote a nice long comment saying this is actually not necessary,

**[12:27]** saying this is actually not necessary,

**[12:27]** saying this is actually not necessary, so just output the input.

**[12:30]** so just output the input.

**[12:30]** so just output the input. [laughter]

**[12:32]** [laughter]

**[12:32]** [laughter] So [snorts] you could argue this is the

**[12:34]** So [snorts] you could argue this is the

**[12:34]** So [snorts] you could argue this is the agent being smart because it's pruning

**[12:35]** agent being smart because it's pruning

**[12:35]** agent being smart because it's pruning unnecessary work, but I think a lot of

**[12:37]** unnecessary work, but I think a lot of

**[12:37]** unnecessary work, but I think a lot of us would agree that it's not in the

**[12:39]** us would agree that it's not in the

**[12:39]** us would agree that it's not in the spirit of what we're trying to benchmark

**[12:41]** spirit of what we're trying to benchmark

**[12:41]** spirit of what we're trying to benchmark here. So we've excluded cases like this

**[12:43]** here. So we've excluded cases like this

**[12:43]** here. So we've excluded cases like this from our analysis, but it is interesting

**[12:45]** from our analysis, but it is interesting

**[12:45]** from our analysis, but it is interesting because maybe some of the times you

**[12:46]** because maybe some of the times you

**[12:46]** because maybe some of the times you would want it to do something like that.

**[12:48]** would want it to do something like that.

**[12:48]** would want it to do something like that. And I think this is part of where the

**[12:50]** And I think this is part of where the

**[12:50]** And I think this is part of where the human element comes in with these

**[12:51]** human element comes in with these

**[12:51]** human element comes in with these agents. Sometimes the agent does

**[12:53]** agents. Sometimes the agent does

**[12:53]** agents. Sometimes the agent does something that depending on your

**[12:54]** something that depending on your

**[12:54]** something that depending on your definition of what you want to see could

**[12:56]** definition of what you want to see could

**[12:56]** definition of what you want to see could be good or it could be bad. And so

**[12:58]** be good or it could be bad. And so

**[12:58]** be good or it could be bad. And so that's where the human part kind of


### [13:00 - 14:00]

**[13:00]** that's where the human part kind of

**[13:00]** that's where the human part kind of weighs in.

**[13:02]** weighs in.

**[13:02]** weighs in. So, like I keep drawing parallels to

**[13:04]** So, like I keep drawing parallels to

**[13:04]** So, like I keep drawing parallels to other kinds of coding agents because

**[13:06]** other kinds of coding agents because

**[13:06]** other kinds of coding agents because even though this is like kind of a niche

**[13:08]** even though this is like kind of a niche

**[13:08]** even though this is like kind of a niche like low-level domain, I don't think

**[13:10]** like low-level domain, I don't think

**[13:10]** like low-level domain, I don't think that the story is fundamentally

**[13:12]** that the story is fundamentally

**[13:12]** that the story is fundamentally different. We see standalone agents are

**[13:15]** different. We see standalone agents are

**[13:15]** different. We see standalone agents are really good at cheaply generating like

**[13:17]** really good at cheaply generating like

**[13:17]** really good at cheaply generating like lots of different ideas and lots of

**[13:18]** lots of different ideas and lots of

**[13:18]** lots of different ideas and lots of possibilities to explore. They're good

**[13:21]** possibilities to explore. They're good

**[13:21]** possibilities to explore. They're good at slurping in a ton of different

**[13:22]** at slurping in a ton of different

**[13:22]** at slurping in a ton of different context and seeing what helps. And

**[13:25]** context and seeing what helps. And

**[13:25]** context and seeing what helps. And they're really good at doing these like

**[13:26]** they're really good at doing these like

**[13:26]** they're really good at doing these like level one and level two tasks. Like for

**[13:29]** level one and level two tasks. Like for

**[13:29]** level one and level two tasks. Like for example, we're still not asking AI

**[13:30]** example, we're still not asking AI

**[13:30]** example, we're still not asking AI agents to write the Linux kernel, but

**[13:33]** agents to write the Linux kernel, but

**[13:33]** agents to write the Linux kernel, but what is still needed is robust and

**[13:36]** what is still needed is robust and

**[13:36]** what is still needed is robust and robust quality and performance

**[13:37]** robust quality and performance

**[13:37]** robust quality and performance validation. We need to make sure that

**[13:39]** validation. We need to make sure that

**[13:39]** validation. We need to make sure that the agents aren't cheating and we need

**[13:41]** the agents aren't cheating and we need

**[13:41]** the agents aren't cheating and we need to make sure that the results are

**[13:42]** to make sure that the results are

**[13:42]** to make sure that the results are actually correct. We need empirical data

**[13:45]** actually correct. We need empirical data

**[13:45]** actually correct. We need empirical data from hardware in the loop to guide the

**[13:47]** from hardware in the loop to guide the

**[13:47]** from hardware in the loop to guide the search and optimization because it's

**[13:49]** search and optimization because it's

**[13:49]** search and optimization because it's actually really hard to look at

**[13:51]** actually really hard to look at

**[13:51]** actually really hard to look at low-level code and know how it's going

**[13:52]** low-level code and know how it's going

**[13:52]** low-level code and know how it's going to perform on the hardware. We still

**[13:54]** to perform on the hardware. We still

**[13:54]** to perform on the hardware. We still heavily rely on looking on profiling

**[13:56]** heavily rely on looking on profiling

**[13:56]** heavily rely on looking on profiling data and things like that. And we also

**[13:59]** data and things like that. And we also

**[13:59]** data and things like that. And we also need the human in the loop to supervise


### [14:00 - 15:00]

**[14:00]** need the human in the loop to supervise

**[14:00]** need the human in the loop to supervise the results and guide the work. So

**[14:02]** the results and guide the work. So

**[14:02]** the results and guide the work. So design of a modern agent, you have

**[14:05]** design of a modern agent, you have

**[14:05]** design of a modern agent, you have multiple sub aents that are working

**[14:06]** multiple sub aents that are working

**[14:06]** multiple sub aents that are working together. You have that human in the

**[14:09]** together. You have that human in the

**[14:09]** together. You have that human in the loop and a purpose-built harness for

**[14:11]** loop and a purpose-built harness for

**[14:11]** loop and a purpose-built harness for that task. And I think this is the

**[14:12]** that task. And I think this is the

**[14:12]** that task. And I think this is the pattern we've seen throughout this

**[14:14]** pattern we've seen throughout this

**[14:14]** pattern we've seen throughout this conference.

**[14:17]** conference.

**[14:17]** conference. So just to get a little bit into kind of

**[14:19]** So just to get a little bit into kind of

**[14:19]** So just to get a little bit into kind of like what that architecture looks like

**[14:21]** like what that architecture looks like

**[14:21]** like what that architecture looks like and this is what we're you know what

**[14:23]** and this is what we're you know what

**[14:23]** and this is what we're you know what we're building at Gimlet you have a

**[14:25]** we're building at Gimlet you have a

**[14:25]** we're building at Gimlet you have a supervisor agent which takes in input

**[14:28]** supervisor agent which takes in input

**[14:28]** supervisor agent which takes in input code target hardware and then also human

**[14:31]** code target hardware and then also human

**[14:31]** code target hardware and then also human prompting because humans still can

**[14:32]** prompting because humans still can

**[14:32]** prompting because humans still can really guide the best path for

**[14:33]** really guide the best path for

**[14:33]** really guide the best path for optimization that supervisor is in

**[14:36]** optimization that supervisor is in

**[14:36]** optimization that supervisor is in charge of managing the work. It deploys

**[14:40]** charge of managing the work. It deploys

**[14:40]** charge of managing the work. It deploys the synthesis agentic swarm which

**[14:42]** the synthesis agentic swarm which

**[14:42]** the synthesis agentic swarm which collectively work together to come up

**[14:43]** collectively work together to come up

**[14:43]** collectively work together to come up with ideas for optimizations and they

**[14:46]** with ideas for optimizations and they

**[14:46]** with ideas for optimizations and they are basically the idea factory coming up

**[14:49]** are basically the idea factory coming up

**[14:49]** are basically the idea factory coming up with new techniques. Those ideas get

**[14:51]** with new techniques. Those ideas get

**[14:51]** with new techniques. Those ideas get sent to the verification agent which is

**[14:53]** sent to the verification agent which is

**[14:53]** sent to the verification agent which is running them in on actual hardware in a

**[14:56]** running them in on actual hardware in a

**[14:56]** running them in on actual hardware in a hardware in the loop system to see how

**[14:57]** hardware in the loop system to see how

**[14:58]** hardware in the loop system to see how they do and that verification agent


### [15:00 - 16:00]

**[15:00]** they do and that verification agent

**[15:00]** they do and that verification agent needs to be extremely strict about

**[15:02]** needs to be extremely strict about

**[15:02]** needs to be extremely strict about making sure that no funny business is

**[15:03]** making sure that no funny business is

**[15:04]** making sure that no funny business is happening. And that's a major part of

**[15:05]** happening. And that's a major part of

**[15:05]** happening. And that's a major part of the challenge.

**[15:11]** So just a couple more realistic case

**[15:11]** So just a couple more realistic case studies that are not benchmarks. We got

**[15:13]** studies that are not benchmarks. We got

**[15:13]** studies that are not benchmarks. We got really excited because we ran this on a

**[15:15]** really excited because we ran this on a

**[15:15]** really excited because we ran this on a vision transformer model and I don't

**[15:17]** vision transformer model and I don't

**[15:17]** vision transformer model and I don't know if you can see but basically the

**[15:19]** know if you can see but basically the

**[15:19]** know if you can see but basically the original uh vanilla implementation using

**[15:22]** original uh vanilla implementation using

**[15:22]** original uh vanilla implementation using torch compile and our generated code

**[15:24]** torch compile and our generated code

**[15:24]** torch compile and our generated code using torch compile ours was twice as

**[15:27]** using torch compile ours was twice as

**[15:27]** using torch compile ours was twice as fast. So this was like a hoay moment.

**[15:30]** fast. So this was like a hoay moment.

**[15:30]** fast. So this was like a hoay moment. So the speedups were promising, but then

**[15:33]** So the speedups were promising, but then

**[15:33]** So the speedups were promising, but then it turned out the optimization was just

**[15:35]** it turned out the optimization was just

**[15:35]** it turned out the optimization was just swapping out the original attention

**[15:37]** swapping out the original attention

**[15:37]** swapping out the original attention module for SDPA, which is a more

**[15:40]** module for SDPA, which is a more

**[15:40]** module for SDPA, which is a more optimized attention module. And this is

**[15:42]** optimized attention module. And this is

**[15:42]** optimized attention module. And this is the kind of thing that yes, that's true.

**[15:45]** the kind of thing that yes, that's true.

**[15:45]** the kind of thing that yes, that's true. That is a valid optimization, but I

**[15:46]** That is a valid optimization, but I

**[15:46]** That is a valid optimization, but I wouldn't necessarily call it rocket

**[15:48]** wouldn't necessarily call it rocket

**[15:48]** wouldn't necessarily call it rocket science. So we consider that to be a

**[15:50]** science. So we consider that to be a

**[15:50]** science. So we consider that to be a trivial case study where if you're not

**[15:53]** trivial case study where if you're not

**[15:53]** trivial case study where if you're not using a more optimized attention module,

**[15:54]** using a more optimized attention module,

**[15:54]** using a more optimized attention module, maybe you haven't actually optimized

**[15:56]** maybe you haven't actually optimized

**[15:56]** maybe you haven't actually optimized your workload that much yet.

**[15:59]** your workload that much yet.

**[15:59]** your workload that much yet. But we do still see interesting results


### [16:00 - 17:00]

**[16:01]** But we do still see interesting results

**[16:02]** But we do still see interesting results for full models when we have human

**[16:03]** for full models when we have human

**[16:03]** for full models when we have human prompting. And one case for this was an

**[16:06]** prompting. And one case for this was an

**[16:06]** prompting. And one case for this was an audioenccoder model where it generated

**[16:08]** audioenccoder model where it generated

**[16:08]** audioenccoder model where it generated six custom kernels for the workload

**[16:10]** six custom kernels for the workload

**[16:10]** six custom kernels for the workload specialized for the RTX 6000 Blackwell.

**[16:13]** specialized for the RTX 6000 Blackwell.

**[16:14]** specialized for the RTX 6000 Blackwell. And the results were strong. It was

**[16:16]** And the results were strong. It was

**[16:16]** And the results were strong. It was about 70% faster. Both implementations

**[16:19]** about 70% faster. Both implementations

**[16:19]** about 70% faster. Both implementations using torch compile.

**[16:21]** using torch compile.

**[16:22]** using torch compile. So just to kind of show an example, we

**[16:24]** So just to kind of show an example, we

**[16:24]** So just to kind of show an example, we load in line six different fused kernels

**[16:28]** load in line six different fused kernels

**[16:28]** load in line six different fused kernels and then call them in the code. And the

**[16:30]** and then call them in the code. And the

**[16:30]** and then call them in the code. And the nice thing about this approach, even

**[16:32]** nice thing about this approach, even

**[16:32]** nice thing about this approach, even though it's a little weird declaring

**[16:33]** though it's a little weird declaring

**[16:33]** though it's a little weird declaring these as strings, is that you have like

**[16:35]** these as strings, is that you have like

**[16:35]** these as strings, is that you have like a completely a API compatible swap in

**[16:38]** a completely a API compatible swap in

**[16:38]** a completely a API compatible swap in replacement for the original module in

**[16:39]** replacement for the original module in

**[16:39]** replacement for the original module in PyTorch.

**[16:45]** So where are we with AIdriven kernel

**[16:45]** So where are we with AIdriven kernel optimization? I think like I said before

**[16:47]** optimization? I think like I said before

**[16:47]** optimization? I think like I said before this is not a silver bullet but it is a

**[16:49]** this is not a silver bullet but it is a

**[16:49]** this is not a silver bullet but it is a promising new tool in the toolbox. The

**[16:52]** promising new tool in the toolbox. The

**[16:52]** promising new tool in the toolbox. The best applications that we see are things

**[16:55]** best applications that we see are things

**[16:55]** best applications that we see are things like searching across many bags of

**[16:57]** like searching across many bags of

**[16:57]** like searching across many bags of tricks. We know that fusion works. We

**[16:59]** tricks. We know that fusion works. We

**[16:59]** tricks. We know that fusion works. We know that tiling works and we can run


### [17:00 - 18:00]

**[17:02]** know that tiling works and we can run

**[17:02]** know that tiling works and we can run lots of experiments really quickly this

**[17:04]** lots of experiments really quickly this

**[17:04]** lots of experiments really quickly this way by launching them with agents and

**[17:05]** way by launching them with agents and

**[17:05]** way by launching them with agents and see what actually performs the best on

**[17:07]** see what actually performs the best on

**[17:07]** see what actually performs the best on the workload. It's also good at porting

**[17:10]** the workload. It's also good at porting

**[17:10]** the workload. It's also good at porting existing implementations to new hardware

**[17:12]** existing implementations to new hardware

**[17:12]** existing implementations to new hardware where it takes the insights from that

**[17:14]** where it takes the insights from that

**[17:14]** where it takes the insights from that original implementation and specializes

**[17:16]** original implementation and specializes

**[17:16]** original implementation and specializes them to the hardware available features

**[17:18]** them to the hardware available features

**[17:18]** them to the hardware available features on the new target

**[17:21]** on the new target

**[17:21]** on the new target and also about translating existing

**[17:23]** and also about translating existing

**[17:23]** and also about translating existing optimizations to new scenarios. You can

**[17:26]** optimizations to new scenarios. You can

**[17:26]** optimizations to new scenarios. You can quickly adopt new optimizations like

**[17:28]** quickly adopt new optimizations like

**[17:28]** quickly adopt new optimizations like let's say you're changing the

**[17:29]** let's say you're changing the

**[17:29]** let's say you're changing the quantization of your model. You can

**[17:31]** quantization of your model. You can

**[17:31]** quantization of your model. You can still look at differently quantized

**[17:34]** still look at differently quantized

**[17:34]** still look at differently quantized implementations to guide that

**[17:35]** implementations to guide that

**[17:35]** implementations to guide that optimization.

**[17:37]** optimization.

**[17:38]** optimization. In terms of the worst applications,

**[17:39]** In terms of the worst applications,

**[17:39]** In terms of the worst applications, we're still not at the point where

**[17:40]** we're still not at the point where

**[17:40]** we're still not at the point where they're writing the N plus1 for flash

**[17:43]** they're writing the N plus1 for flash

**[17:43]** they're writing the N plus1 for flash attention, coming up with like those

**[17:44]** attention, coming up with like those

**[17:44]** attention, coming up with like those genius algorithmic advances. And they're

**[17:47]** genius algorithmic advances. And they're

**[17:47]** genius algorithmic advances. And they're not currently outperforming a human

**[17:49]** not currently outperforming a human

**[17:49]** not currently outperforming a human expert who bang their head on this

**[17:50]** expert who bang their head on this

**[17:50]** expert who bang their head on this problem for months. And we shouldn't

**[17:52]** problem for months. And we shouldn't

**[17:52]** problem for months. And we shouldn't expect them to be. I think that the most

**[17:54]** expect them to be. I think that the most

**[17:54]** expect them to be. I think that the most exciting part of this work is allowing

**[17:57]** exciting part of this work is allowing

**[17:57]** exciting part of this work is allowing those people to focus on the most

**[17:58]** those people to focus on the most

**[17:58]** those people to focus on the most interesting optimizations and getting us


### [18:00 - 19:00]

**[18:00]** interesting optimizations and getting us

**[18:00]** interesting optimizations and getting us better than baseline on all the problems

**[18:02]** better than baseline on all the problems

**[18:02]** better than baseline on all the problems that they don't have time for.

**[18:06]** that they don't have time for.

**[18:06]** that they don't have time for. So what's next in the work? We want to

**[18:09]** So what's next in the work? We want to

**[18:09]** So what's next in the work? We want to build uh abstract models of different

**[18:11]** build uh abstract models of different

**[18:11]** build uh abstract models of different machines to help the agents further

**[18:13]** machines to help the agents further

**[18:13]** machines to help the agents further specialize code to individual hardware.

**[18:16]** specialize code to individual hardware.

**[18:16]** specialize code to individual hardware. We're also interested in generating

**[18:18]** We're also interested in generating

**[18:18]** We're also interested in generating basically what is like NVIDIA assembly

**[18:20]** basically what is like NVIDIA assembly

**[18:20]** basically what is like NVIDIA assembly such as PTX. You can see an example here

**[18:23]** such as PTX. You can see an example here

**[18:23]** such as PTX. You can see an example here because the thought is that we can

**[18:25]** because the thought is that we can

**[18:25]** because the thought is that we can basically do that better with AI than

**[18:27]** basically do that better with AI than

**[18:27]** basically do that better with AI than humans because it's so cumbersome. And

**[18:29]** humans because it's so cumbersome. And

**[18:29]** humans because it's so cumbersome. And then also looking at academic formal

**[18:32]** then also looking at academic formal

**[18:32]** then also looking at academic formal verification methods for correctness.

**[18:36]** verification methods for correctness.

**[18:36]** verification methods for correctness. Um, also want to give a huge shout out

**[18:37]** Um, also want to give a huge shout out

**[18:38]** Um, also want to give a huge shout out to my colleagues. Um, they are the

**[18:40]** to my colleagues. Um, they are the

**[18:40]** to my colleagues. Um, they are the silent unspoken heroes here and um, you

**[18:43]** silent unspoken heroes here and um, you

**[18:43]** silent unspoken heroes here and um, you know, I love talking about this with

**[18:45]** know, I love talking about this with

**[18:45]** know, I love talking about this with people. So, please feel free to give me

**[18:46]** people. So, please feel free to give me

**[18:46]** people. So, please feel free to give me an email if you want to talk about

**[18:48]** an email if you want to talk about

**[18:48]** an email if you want to talk about kernel generation or anything that I

**[18:50]** kernel generation or anything that I

**[18:50]** kernel generation or anything that I covered. And we are hiring. So, if this

**[18:52]** covered. And we are hiring. So, if this

**[18:52]** covered. And we are hiring. So, if this problem interests you, we'd love to

**[18:53]** problem interests you, we'd love to

**[18:53]** problem interests you, we'd love to chat.

**[18:55]** chat.

**[18:55]** chat. Thanks.

**[18:57]** Thanks.

**[18:57]** Thanks. [music]


