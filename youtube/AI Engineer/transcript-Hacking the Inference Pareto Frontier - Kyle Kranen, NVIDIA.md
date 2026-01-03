# Hacking the Inference Pareto Frontier - Kyle Kranen, NVIDIA

**Video URL:** https://www.youtube.com/watch?v=Y2qc0UhDSnc

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Hey there everyone. I'm Kyle Cranon and

**[00:16]** Hey there everyone. I'm Kyle Cranon and today I'll be talking about how to break

**[00:18]** today I'll be talking about how to break

**[00:18]** today I'll be talking about how to break the inference bra frontier in your

**[00:20]** the inference bra frontier in your

**[00:20]** the inference bra frontier in your advantage. Um really the thing that

**[00:23]** advantage. Um really the thing that

**[00:23]** advantage. Um really the thing that enables the success is that a good model

**[00:25]** enables the success is that a good model

**[00:25]** enables the success is that a good model and a good system that takes into

**[00:27]** and a good system that takes into

**[00:27]** and a good system that takes into account the actual constraints for what

**[00:29]** account the actual constraints for what

**[00:29]** account the actual constraints for what you need from your deployment is

**[00:31]** you need from your deployment is

**[00:31]** you need from your deployment is actually key to the success of both your

**[00:33]** actually key to the success of both your

**[00:34]** actually key to the success of both your deployment and the application that is

**[00:35]** deployment and the application that is

**[00:35]** deployment and the application that is backed by it. Um so who am I and why am

**[00:39]** backed by it. Um so who am I and why am

**[00:39]** backed by it. Um so who am I and why am I talking about this? Uh as I said my

**[00:42]** I talking about this? Uh as I said my

**[00:42]** I talking about this? Uh as I said my name is Kyle Crane. Uh previously I work

**[00:44]** name is Kyle Crane. Uh previously I work

**[00:44]** name is Kyle Crane. Uh previously I work at or currently I work at NVIDIA. Uh

**[00:47]** at or currently I work at NVIDIA. Uh

**[00:47]** at or currently I work at NVIDIA. Uh previously at NVIDIA, I was uh leading

**[00:50]** previously at NVIDIA, I was uh leading

**[00:50]** previously at NVIDIA, I was uh leading and GMing the largest inference

**[00:51]** and GMing the largest inference

**[00:51]** and GMing the largest inference deployment at NVIDIA with a multiple

**[00:54]** deployment at NVIDIA with a multiple

**[00:54]** deployment at NVIDIA with a multiple tens of millions of dollar quarterly

**[00:56]** tens of millions of dollar quarterly

**[00:56]** tens of millions of dollar quarterly cloud bill. Uh and now I'm an architect

**[00:59]** cloud bill. Uh and now I'm an architect

**[00:59]** cloud bill. Uh and now I'm an architect and lead for a project that we just


### [01:00 - 02:00]

**[01:00]** and lead for a project that we just

**[01:00]** and lead for a project that we just released in open source called NVIDIA

**[01:02]** released in open source called NVIDIA

**[01:02]** released in open source called NVIDIA Dynamo that aims to do things like

**[01:05]** Dynamo that aims to do things like

**[01:05]** Dynamo that aims to do things like enable data center scale inference to

**[01:08]** enable data center scale inference to

**[01:08]** enable data center scale inference to manipulate your deployment and

**[01:09]** manipulate your deployment and

**[01:09]** manipulate your deployment and manipulate the paro frontier in order to

**[01:11]** manipulate the paro frontier in order to

**[01:11]** manipulate the paro frontier in order to achieve better SLAs's or achieve lower

**[01:13]** achieve better SLAs's or achieve lower

**[01:13]** achieve better SLAs's or achieve lower costs for your existing SLAs's. with

**[01:16]** costs for your existing SLAs's. with

**[01:16]** costs for your existing SLAs's. with techniques like disagregation or more

**[01:17]** techniques like disagregation or more

**[01:18]** techniques like disagregation or more techniques that I'll talk about later in

**[01:19]** techniques that I'll talk about later in

**[01:19]** techniques that I'll talk about later in the talk. Dynamo is uh the Dynamo meetup

**[01:23]** the talk. Dynamo is uh the Dynamo meetup

**[01:23]** the talk. Dynamo is uh the Dynamo meetup is linked right here. You can learn more

**[01:24]** is linked right here. You can learn more

**[01:24]** is linked right here. You can learn more about Dynamo there if you want to look

**[01:26]** about Dynamo there if you want to look

**[01:26]** about Dynamo there if you want to look it up and I'll also have that uh at the

**[01:28]** it up and I'll also have that uh at the

**[01:28]** it up and I'll also have that uh at the end of the talk as well. Um so the three

**[01:31]** end of the talk as well. Um so the three

**[01:31]** end of the talk as well. Um so the three things that we or I like to think about

**[01:33]** things that we or I like to think about

**[01:33]** things that we or I like to think about when I'm thinking about whether or not

**[01:35]** when I'm thinking about whether or not

**[01:35]** when I'm thinking about whether or not something can actually be deployed and

**[01:37]** something can actually be deployed and

**[01:37]** something can actually be deployed and used is really simple. It's quality.

**[01:40]** used is really simple. It's quality.

**[01:40]** used is really simple. It's quality. whether or not your application and the

**[01:42]** whether or not your application and the

**[01:42]** whether or not your application and the system around your model is capable of,

**[01:44]** system around your model is capable of,

**[01:44]** system around your model is capable of, you know, completing tasks with some

**[01:45]** you know, completing tasks with some

**[01:45]** you know, completing tasks with some level of accuracy or quality. Latency,

**[01:49]** level of accuracy or quality. Latency,

**[01:49]** level of accuracy or quality. Latency, whether or not the task can be completed

**[01:51]** whether or not the task can be completed

**[01:51]** whether or not the task can be completed in a fast enough envelope for, you know,

**[01:53]** in a fast enough envelope for, you know,

**[01:53]** in a fast enough envelope for, you know, either the user to be happy or to meet

**[01:55]** either the user to be happy or to meet

**[01:55]** either the user to be happy or to meet safety guarantees like for robotics, uh,

**[01:57]** safety guarantees like for robotics, uh,

**[01:58]** safety guarantees like for robotics, uh, and cost. Can the LM complete the task


### [02:00 - 03:00]

**[02:01]** and cost. Can the LM complete the task

**[02:01]** and cost. Can the LM complete the task cheaply enough per request in order for

**[02:03]** cheaply enough per request in order for

**[02:03]** cheaply enough per request in order for you to meet whatever, you know, margin

**[02:05]** you to meet whatever, you know, margin

**[02:05]** you to meet whatever, you know, margin requirements you have for your

**[02:06]** requirements you have for your

**[02:06]** requirements you have for your application?

**[02:08]** application?

**[02:08]** application? Um

**[02:09]** Um

**[02:09]** Um and one of the ways that we generally

**[02:12]** and one of the ways that we generally

**[02:12]** and one of the ways that we generally compare these three things is through a

**[02:13]** compare these three things is through a

**[02:13]** compare these three things is through a para frontier. Now uh the frontier I'm

**[02:16]** para frontier. Now uh the frontier I'm

**[02:16]** para frontier. Now uh the frontier I'm showing here is two dimensional. Uh it's

**[02:17]** showing here is two dimensional. Uh it's

**[02:18]** showing here is two dimensional. Uh it's actually really hard to plot things in

**[02:19]** actually really hard to plot things in

**[02:19]** actually really hard to plot things in 3D on a 2D slide. So I'm going to just

**[02:21]** 3D on a 2D slide. So I'm going to just

**[02:21]** 3D on a 2D slide. So I'm going to just show two dimensions. Really what this

**[02:23]** show two dimensions. Really what this

**[02:23]** show two dimensions. Really what this looks like is you have this like edge

**[02:25]** looks like is you have this like edge

**[02:25]** looks like is you have this like edge that oh is it working? uh we have this

**[02:29]** that oh is it working? uh we have this

**[02:29]** that oh is it working? uh we have this edge that sort of represents the best or

**[02:33]** edge that sort of represents the best or

**[02:33]** edge that sort of represents the best or to the top and rightmost points that we

**[02:35]** to the top and rightmost points that we

**[02:35]** to the top and rightmost points that we achieve for uh you know a specific set

**[02:38]** achieve for uh you know a specific set

**[02:38]** achieve for uh you know a specific set of attributes. So in this case we have

**[02:40]** of attributes. So in this case we have

**[02:40]** of attributes. So in this case we have the TPS per GPU which is effectively a

**[02:43]** the TPS per GPU which is effectively a

**[02:43]** the TPS per GPU which is effectively a cost metric. How many requests can you

**[02:45]** cost metric. How many requests can you

**[02:45]** cost metric. How many requests can you handle per GPU per second and the user

**[02:47]** handle per GPU per second and the user

**[02:47]** handle per GPU per second and the user TPS which is a responsiveness metric

**[02:49]** TPS which is a responsiveness metric

**[02:49]** TPS which is a responsiveness metric right? So this is the the latency versus

**[02:51]** right? So this is the the latency versus

**[02:51]** right? So this is the the latency versus the cost and for different applications

**[02:54]** the cost and for different applications

**[02:54]** the cost and for different applications really you want to enable your prao

**[02:57]** really you want to enable your prao

**[02:57]** really you want to enable your prao front enable or you actually really only


### [03:00 - 04:00]

**[03:00]** front enable or you actually really only

**[03:00]** front enable or you actually really only want one point on the prao frontier it's

**[03:01]** want one point on the prao frontier it's

**[03:01]** want one point on the prao frontier it's right what is your operating latency

**[03:03]** right what is your operating latency

**[03:03]** right what is your operating latency what is the operating quality you need

**[03:04]** what is the operating quality you need

**[03:04]** what is the operating quality you need and how can you minimize cost for that

**[03:07]** and how can you minimize cost for that

**[03:07]** and how can you minimize cost for that now this really actually depends on the

**[03:09]** now this really actually depends on the

**[03:09]** now this really actually depends on the application you're talking about so one

**[03:11]** application you're talking about so one

**[03:11]** application you're talking about so one of the most important things you're

**[03:12]** of the most important things you're

**[03:12]** of the most important things you're doing when you're thinking about

**[03:14]** doing when you're thinking about

**[03:14]** doing when you're thinking about breaking the creative frontier is you're

**[03:16]** breaking the creative frontier is you're

**[03:16]** breaking the creative frontier is you're thinking about your application so for

**[03:17]** thinking about your application so for

**[03:17]** thinking about your application so for example if we're talking about personal

**[03:19]** example if we're talking about personal

**[03:19]** example if we're talking about personal cancer cures, which is a topic that's

**[03:21]** cancer cures, which is a topic that's

**[03:21]** cancer cures, which is a topic that's talked about a lot in the context of

**[03:23]** talked about a lot in the context of

**[03:23]** talked about a lot in the context of generative AI. Uh, in that situation,

**[03:27]** generative AI. Uh, in that situation,

**[03:27]** generative AI. Uh, in that situation, uh, latency and cost are pretty much no

**[03:28]** uh, latency and cost are pretty much no

**[03:28]** uh, latency and cost are pretty much no object, right? You could spend millions

**[03:30]** object, right? You could spend millions

**[03:30]** object, right? You could spend millions of dollars on proving out a single cure

**[03:32]** of dollars on proving out a single cure

**[03:32]** of dollars on proving out a single cure and if it works, the return on

**[03:33]** and if it works, the return on

**[03:33]** and if it works, the return on investment is so high that it doesn't

**[03:36]** investment is so high that it doesn't

**[03:36]** investment is so high that it doesn't really matter. Um, to take a different

**[03:39]** really matter. Um, to take a different

**[03:39]** really matter. Um, to take a different example, tab completion like those that

**[03:40]** example, tab completion like those that

**[03:40]** example, tab completion like those that you see in popular IDs like cursor all

**[03:45]** you see in popular IDs like cursor all

**[03:45]** you see in popular IDs like cursor all are very very dependent upon snappiness.

**[03:47]** are very very dependent upon snappiness.

**[03:47]** are very very dependent upon snappiness. The user expects that when they press

**[03:48]** The user expects that when they press

**[03:48]** The user expects that when they press tab, they will see a recommendation for

**[03:51]** tab, they will see a recommendation for

**[03:51]** tab, they will see a recommendation for the next line or the next set of you

**[03:53]** the next line or the next set of you

**[03:53]** the next line or the next set of you know tokens very very quickly. And then

**[03:56]** know tokens very very quickly. And then

**[03:56]** know tokens very very quickly. And then to take another code example with

**[03:58]** to take another code example with

**[03:58]** to take another code example with respect to async code commits things


### [04:00 - 05:00]

**[04:00]** respect to async code commits things

**[04:00]** respect to async code commits things like uh you know uh cursors um what's it

**[04:05]** like uh you know uh cursors um what's it

**[04:05]** like uh you know uh cursors um what's it called? agent mode and um you know other

**[04:09]** called? agent mode and um you know other

**[04:09]** called? agent mode and um you know other applications where the the chatbot or

**[04:12]** applications where the the chatbot or

**[04:12]** applications where the the chatbot or applications working next to the user

**[04:14]** applications working next to the user

**[04:14]** applications working next to the user there's not as much a consideration for

**[04:16]** there's not as much a consideration for

**[04:16]** there's not as much a consideration for latency but there is a concern for both

**[04:18]** latency but there is a concern for both

**[04:18]** latency but there is a concern for both quality and cost. Uh and this sort of

**[04:20]** quality and cost. Uh and this sort of

**[04:20]** quality and cost. Uh and this sort of breaks down how or this sort of depends

**[04:24]** breaks down how or this sort of depends

**[04:24]** breaks down how or this sort of depends upon what the user expects from the

**[04:26]** upon what the user expects from the

**[04:26]** upon what the user expects from the application. Does it do do they expect

**[04:28]** application. Does it do do they expect

**[04:28]** application. Does it do do they expect it to be fast? Do they expect it to be

**[04:30]** it to be fast? Do they expect it to be

**[04:30]** it to be fast? Do they expect it to be slow? Are they involved in the loop with

**[04:32]** slow? Are they involved in the loop with

**[04:32]** slow? Are they involved in the loop with this application?

**[04:35]** this application?

**[04:35]** this application? Now there are a series of you know

**[04:37]** Now there are a series of you know

**[04:37]** Now there are a series of you know techniques that are pretty commonly

**[04:38]** techniques that are pretty commonly

**[04:38]** techniques that are pretty commonly known about that all you know support

**[04:41]** known about that all you know support

**[04:41]** known about that all you know support the manipulation of the sprintier. For

**[04:43]** the manipulation of the sprintier. For

**[04:43]** the manipulation of the sprintier. For example, quantization speeds up your

**[04:44]** example, quantization speeds up your

**[04:44]** example, quantization speeds up your latency and it also decreases your cost

**[04:46]** latency and it also decreases your cost

**[04:46]** latency and it also decreases your cost because you can produce higher batch

**[04:48]** because you can produce higher batch

**[04:48]** because you can produce higher batch sizes. Retrieve augmented generation

**[04:50]** sizes. Retrieve augmented generation

**[04:50]** sizes. Retrieve augmented generation generally slows down your application,

**[04:52]** generally slows down your application,

**[04:52]** generally slows down your application, makes it higher latency, increases the

**[04:54]** makes it higher latency, increases the

**[04:54]** makes it higher latency, increases the cost but also increases the quality. And

**[04:57]** cost but also increases the quality. And

**[04:57]** cost but also increases the quality. And reasoning for example similar, you know,

**[04:59]** reasoning for example similar, you know,

**[04:59]** reasoning for example similar, you know, you produce more tokens to think. And


### [05:00 - 06:00]

**[05:01]** you produce more tokens to think. And

**[05:01]** you produce more tokens to think. And changing the model config allows you to

**[05:03]** changing the model config allows you to

**[05:03]** changing the model config allows you to do any of these things. If you change

**[05:04]** do any of these things. If you change

**[05:04]** do any of these things. If you change how the model is represented in a

**[05:06]** how the model is represented in a

**[05:06]** how the model is represented in a parallel manner, uh you can

**[05:08]** parallel manner, uh you can

**[05:08]** parallel manner, uh you can significantly change the characteristics

**[05:10]** significantly change the characteristics

**[05:10]** significantly change the characteristics of uh speed, cost, and theoretically

**[05:12]** of uh speed, cost, and theoretically

**[05:12]** of uh speed, cost, and theoretically equality. If you're talking about

**[05:14]** equality. If you're talking about

**[05:14]** equality. If you're talking about non-haled context parallelism, um the

**[05:17]** non-haled context parallelism, um the

**[05:17]** non-haled context parallelism, um the thing that I want to impart upon you

**[05:19]** thing that I want to impart upon you

**[05:19]** thing that I want to impart upon you before we jump into like a lot more of

**[05:20]** before we jump into like a lot more of

**[05:20]** before we jump into like a lot more of these advanced techniques is that these

**[05:21]** these advanced techniques is that these

**[05:21]** these advanced techniques is that these techniques can be compounded. So for

**[05:23]** techniques can be compounded. So for

**[05:23]** techniques can be compounded. So for example, if you have an initial

**[05:24]** example, if you have an initial

**[05:24]** example, if you have an initial application and has some required

**[05:26]** application and has some required

**[05:26]** application and has some required performance, you can actually stack for

**[05:29]** performance, you can actually stack for

**[05:29]** performance, you can actually stack for example retrieve augmented generation in

**[05:31]** example retrieve augmented generation in

**[05:31]** example retrieve augmented generation in order to increase the quality but make

**[05:33]** order to increase the quality but make

**[05:33]** order to increase the quality but make the latency worse and you can also stack

**[05:36]** the latency worse and you can also stack

**[05:36]** the latency worse and you can also stack on top of that quantization of the model

**[05:39]** on top of that quantization of the model

**[05:39]** on top of that quantization of the model in order to speed up your latency. The

**[05:41]** in order to speed up your latency. The

**[05:41]** in order to speed up your latency. The point I'm, you know, trying to trying to

**[05:43]** point I'm, you know, trying to trying to

**[05:43]** point I'm, you know, trying to trying to make here is that you really have this

**[05:45]** make here is that you really have this

**[05:45]** make here is that you really have this toolbox of a sets of large sets of tools

**[05:47]** toolbox of a sets of large sets of tools

**[05:48]** toolbox of a sets of large sets of tools that you can use together. And the tools

**[05:50]** that you can use together. And the tools

**[05:50]** that you can use together. And the tools themselves are not independent and can

**[05:52]** themselves are not independent and can

**[05:52]** themselves are not independent and can be combined in very sometimes

**[05:54]** be combined in very sometimes

**[05:54]** be combined in very sometimes non-obvious ways in order to actually

**[05:57]** non-obvious ways in order to actually

**[05:57]** non-obvious ways in order to actually break your predo frontier or squeeze it

**[05:59]** break your predo frontier or squeeze it

**[05:59]** break your predo frontier or squeeze it in different directions in order to


### [06:00 - 07:00]

**[06:01]** in different directions in order to

**[06:01]** in different directions in order to support your application. Um so there

**[06:04]** support your application. Um so there

**[06:04]** support your application. Um so there are three things outside of those

**[06:06]** are three things outside of those

**[06:06]** are three things outside of those techniques that I I I tend I tend to

**[06:08]** techniques that I I I tend I tend to

**[06:08]** techniques that I I I tend I tend to think drive uh you know the

**[06:13]** think drive uh you know the

**[06:13]** think drive uh you know the how you can modify the parto frontier

**[06:15]** how you can modify the parto frontier

**[06:15]** how you can modify the parto frontier going forward. Those three are scale,

**[06:17]** going forward. Those three are scale,

**[06:17]** going forward. Those three are scale, structure and dynamism.

**[06:20]** structure and dynamism.

**[06:20]** structure and dynamism. Um so one of the things that is you know

**[06:23]** Um so one of the things that is you know

**[06:23]** Um so one of the things that is you know really relevant in the realm of scale is

**[06:26]** really relevant in the realm of scale is

**[06:26]** really relevant in the realm of scale is disagregation. So for those that aren't

**[06:28]** disagregation. So for those that aren't

**[06:28]** disagregation. So for those that aren't aware, uh KV caching is a technique by

**[06:31]** aware, uh KV caching is a technique by

**[06:31]** aware, uh KV caching is a technique by which you take the K K val key and value

**[06:34]** which you take the K K val key and value

**[06:34]** which you take the K K val key and value vectors that are associated with each

**[06:36]** vectors that are associated with each

**[06:36]** vectors that are associated with each token and you cache them. Uh so that

**[06:39]** token and you cache them. Uh so that

**[06:39]** token and you cache them. Uh so that when you're doing auto reggressive

**[06:40]** when you're doing auto reggressive

**[06:40]** when you're doing auto reggressive generation, you don't have to generate

**[06:41]** generation, you don't have to generate

**[06:41]** generation, you don't have to generate the entire set of key and value vectors

**[06:43]** the entire set of key and value vectors

**[06:43]** the entire set of key and value vectors for the entire sequence up to this

**[06:45]** for the entire sequence up to this

**[06:45]** for the entire sequence up to this point. You can just generate new ones

**[06:47]** point. You can just generate new ones

**[06:47]** point. You can just generate new ones and put them back into the KV cache. Uh

**[06:50]** and put them back into the KV cache. Uh

**[06:50]** and put them back into the KV cache. Uh what this actually means is that we

**[06:52]** what this actually means is that we

**[06:52]** what this actually means is that we effectively have two phases of

**[06:53]** effectively have two phases of

**[06:53]** effectively have two phases of generation. one in which you're

**[06:55]** generation. one in which you're

**[06:55]** generation. one in which you're generating the prefill or filling up

**[06:58]** generating the prefill or filling up

**[06:58]** generating the prefill or filling up your KV cache and one in which you're


### [07:00 - 08:00]

**[07:01]** your KV cache and one in which you're

**[07:01]** your KV cache and one in which you're actually generating new KV cache as well

**[07:03]** actually generating new KV cache as well

**[07:04]** actually generating new KV cache as well as new tokens and producing output. Now

**[07:06]** as new tokens and producing output. Now

**[07:06]** as new tokens and producing output. Now um disagregation as a technique

**[07:08]** um disagregation as a technique

**[07:08]** um disagregation as a technique basically allows you to have these you

**[07:11]** basically allows you to have these you

**[07:11]** basically allows you to have these you know two phases which were typically

**[07:13]** know two phases which were typically

**[07:13]** know two phases which were typically used on the same set of GPUs uh onto

**[07:16]** used on the same set of GPUs uh onto

**[07:16]** used on the same set of GPUs uh onto multiple different workers and sets of

**[07:18]** multiple different workers and sets of

**[07:18]** multiple different workers and sets of GPUs and this provides a couple key

**[07:20]** GPUs and this provides a couple key

**[07:20]** GPUs and this provides a couple key benefits that we'll go into right now.

**[07:23]** benefits that we'll go into right now.

**[07:23]** benefits that we'll go into right now. Um the three really big benefits here

**[07:25]** Um the three really big benefits here

**[07:26]** Um the three really big benefits here are that you will you can really now

**[07:28]** are that you will you can really now

**[07:28]** are that you will you can really now take two uh sort of phases that have

**[07:31]** take two uh sort of phases that have

**[07:31]** take two uh sort of phases that have very very different needs. Uh prefill is

**[07:33]** very very different needs. Uh prefill is

**[07:33]** very very different needs. Uh prefill is very computebound and decode depending

**[07:34]** very computebound and decode depending

**[07:34]** very computebound and decode depending on the application and model can be very

**[07:37]** on the application and model can be very

**[07:37]** on the application and model can be very memory bound and it allows you to do a

**[07:39]** memory bound and it allows you to do a

**[07:40]** memory bound and it allows you to do a granular load matching between those two

**[07:41]** granular load matching between those two

**[07:41]** granular load matching between those two phases. And what this means is uh you

**[07:44]** phases. And what this means is uh you

**[07:44]** phases. And what this means is uh you know compute saturates relatively early

**[07:46]** know compute saturates relatively early

**[07:46]** know compute saturates relatively early uh to use deepse as an example compute

**[07:48]** uh to use deepse as an example compute

**[07:48]** uh to use deepse as an example compute saturates relatively early and you may

**[07:50]** saturates relatively early and you may

**[07:50]** saturates relatively early and you may use uh relatively few uh GPUs for your

**[07:54]** use uh relatively few uh GPUs for your

**[07:54]** use uh relatively few uh GPUs for your prefill instances and have them handle a

**[07:56]** prefill instances and have them handle a

**[07:56]** prefill instances and have them handle a lower batch size but handle a much

**[07:58]** lower batch size but handle a much

**[07:58]** lower batch size but handle a much larger batch size with many more GPUs


### [08:00 - 09:00]

**[08:01]** larger batch size with many more GPUs

**[08:01]** larger batch size with many more GPUs for your decode instances. And this

**[08:03]** for your decode instances. And this

**[08:03]** for your decode instances. And this split and this heterogeneity between the

**[08:05]** split and this heterogeneity between the

**[08:05]** split and this heterogeneity between the two actually allows you to produce far

**[08:08]** two actually allows you to produce far

**[08:08]** two actually allows you to produce far more performance.

**[08:10]** more performance.

**[08:10]** more performance. Um the other thing is that you know one

**[08:14]** Um the other thing is that you know one

**[08:14]** Um the other thing is that you know one of the one of the problems is that if

**[08:15]** of the one of the problems is that if

**[08:15]** of the one of the problems is that if you have inflight batching you have many

**[08:17]** you have inflight batching you have many

**[08:17]** you have inflight batching you have many tokens coming in at the same time that

**[08:19]** tokens coming in at the same time that

**[08:19]** tokens coming in at the same time that are in different phases of generation

**[08:20]** are in different phases of generation

**[08:20]** are in different phases of generation right if you have a request that's doing

**[08:22]** right if you have a request that's doing

**[08:22]** right if you have a request that's doing prefill and a request that's doing

**[08:23]** prefill and a request that's doing

**[08:23]** prefill and a request that's doing decode on the same machine you get

**[08:24]** decode on the same machine you get

**[08:24]** decode on the same machine you get scheduling conflicts and theuler

**[08:26]** scheduling conflicts and theuler

**[08:26]** scheduling conflicts and theuler basically has to decide whether or not

**[08:27]** basically has to decide whether or not

**[08:27]** basically has to decide whether or not it handles new tokens uh there are some

**[08:30]** it handles new tokens uh there are some

**[08:30]** it handles new tokens uh there are some techniques to handle this like inflight

**[08:32]** techniques to handle this like inflight

**[08:32]** techniques to handle this like inflight batching and chunk piggybacking uh or

**[08:34]** batching and chunk piggybacking uh or

**[08:34]** batching and chunk piggybacking uh or sorry chunk chunk piggybacking but um

**[08:37]** sorry chunk chunk piggybacking but um

**[08:37]** sorry chunk chunk piggybacking but um generally there is a cost to doing that

**[08:38]** generally there is a cost to doing that

**[08:38]** generally there is a cost to doing that mutual scheduling so splitting this

**[08:40]** mutual scheduling so splitting this

**[08:40]** mutual scheduling so splitting this makes the scheduling simpler. Now,

**[08:42]** makes the scheduling simpler. Now,

**[08:42]** makes the scheduling simpler. Now, there's an asterisk to this, which is

**[08:43]** there's an asterisk to this, which is

**[08:44]** there's an asterisk to this, which is that uh sorry, really quickly and I I'll

**[08:46]** that uh sorry, really quickly and I I'll

**[08:46]** that uh sorry, really quickly and I I'll go over the performance numbers. I'm

**[08:47]** go over the performance numbers. I'm

**[08:47]** go over the performance numbers. I'm going to use llama 7B as an example.

**[08:49]** going to use llama 7B as an example.

**[08:49]** going to use llama 7B as an example. Right. Right here we have on our left

**[08:51]** Right. Right here we have on our left

**[08:51]** Right. Right here we have on our left axis or the our y axis we have the

**[08:53]** axis or the our y axis we have the

**[08:53]** axis or the our y axis we have the tokens per second per GPU. On our

**[08:55]** tokens per second per GPU. On our

**[08:55]** tokens per second per GPU. On our x-axis, we have the tokens per second

**[08:56]** x-axis, we have the tokens per second

**[08:56]** x-axis, we have the tokens per second per user. Right up and to the right is

**[08:58]** per user. Right up and to the right is

**[08:58]** per user. Right up and to the right is better. Um, if we choose one operating


### [09:00 - 10:00]

**[09:01]** better. Um, if we choose one operating

**[09:01]** better. Um, if we choose one operating point at latency, disagregating on the

**[09:03]** point at latency, disagregating on the

**[09:03]** point at latency, disagregating on the same number of GPUs, 16 total H100s, we

**[09:06]** same number of GPUs, 16 total H100s, we

**[09:06]** same number of GPUs, 16 total H100s, we can achieve up to two times uh the

**[09:08]** can achieve up to two times uh the

**[09:08]** can achieve up to two times uh the tokens per second per GPU at a fixed

**[09:11]** tokens per second per GPU at a fixed

**[09:11]** tokens per second per GPU at a fixed latency, which means that you're now

**[09:12]** latency, which means that you're now

**[09:12]** latency, which means that you're now paying two times less for your

**[09:14]** paying two times less for your

**[09:14]** paying two times less for your application.

**[09:16]** application.

**[09:16]** application. Um, there are some constraints though.

**[09:18]** Um, there are some constraints though.

**[09:18]** Um, there are some constraints though. Uh, the use case really does dictate

**[09:20]** Uh, the use case really does dictate

**[09:20]** Uh, the use case really does dictate performance for for disagregation. Uh,

**[09:23]** performance for for disagregation. Uh,

**[09:23]** performance for for disagregation. Uh, for example, low input length use cases

**[09:26]** for example, low input length use cases

**[09:26]** for example, low input length use cases have little to no speed up because uh

**[09:28]** have little to no speed up because uh

**[09:28]** have little to no speed up because uh you don't h actually have as much of the

**[09:31]** you don't h actually have as much of the

**[09:31]** you don't h actually have as much of the scheduling problem. They're very

**[09:31]** scheduling problem. They're very

**[09:32]** scheduling problem. They're very pre-filled light. You're basically just

**[09:33]** pre-filled light. You're basically just

**[09:33]** pre-filled light. You're basically just doing decode the entire time. Um, and

**[09:36]** doing decode the entire time. Um, and

**[09:36]** doing decode the entire time. Um, and then per the graph disagregation and

**[09:38]** then per the graph disagregation and

**[09:38]** then per the graph disagregation and I'll go back to the graph. actually

**[09:39]** I'll go back to the graph. actually

**[09:40]** I'll go back to the graph. actually disagregation is is is useful in usually

**[09:42]** disagregation is is is useful in usually

**[09:42]** disagregation is is is useful in usually in the middle of the graph. In very high

**[09:44]** in the middle of the graph. In very high

**[09:44]** in the middle of the graph. In very high high latency high throughput scenarios

**[09:46]** high latency high throughput scenarios

**[09:46]** high latency high throughput scenarios which would be the left and top of the

**[09:48]** which would be the left and top of the

**[09:48]** which would be the left and top of the graph and low latency low throughput

**[09:51]** graph and low latency low throughput

**[09:51]** graph and low latency low throughput scenarios the bottom right uh aggregated

**[09:53]** scenarios the bottom right uh aggregated

**[09:53]** scenarios the bottom right uh aggregated tends to reconfer recon converge with

**[09:55]** tends to reconfer recon converge with

**[09:55]** tends to reconfer recon converge with disagregated and produce a little bit

**[09:57]** disagregated and produce a little bit

**[09:58]** disagregated and produce a little bit more performance in those cases. Uh that


### [10:00 - 11:00]

**[10:00]** more performance in those cases. Uh that

**[10:00]** more performance in those cases. Uh that being said for a lot of user you know

**[10:03]** being said for a lot of user you know

**[10:03]** being said for a lot of user you know interactive applications disagregation

**[10:05]** interactive applications disagregation

**[10:05]** interactive applications disagregation makes the most sense because users tend

**[10:07]** makes the most sense because users tend

**[10:08]** makes the most sense because users tend to read that between or care about

**[10:10]** to read that between or care about

**[10:10]** to read that between or care about things in the realm of 20 to 200 tokens

**[10:14]** things in the realm of 20 to 200 tokens

**[10:14]** things in the realm of 20 to 200 tokens per second. Um

**[10:17]** per second. Um

**[10:17]** per second. Um the other thing that's kind of a caveat

**[10:18]** the other thing that's kind of a caveat

**[10:18]** the other thing that's kind of a caveat about this is that configuration is

**[10:20]** about this is that configuration is

**[10:20]** about this is that configuration is really important. Um since you're

**[10:22]** really important. Um since you're

**[10:22]** really important. Um since you're separating these two phases into

**[10:24]** separating these two phases into

**[10:24]** separating these two phases into pre-fill and generation, the balance

**[10:25]** pre-fill and generation, the balance

**[10:26]** pre-fill and generation, the balance between the number of workers for

**[10:27]** between the number of workers for

**[10:27]** between the number of workers for prefill and decoding dictates the

**[10:29]** prefill and decoding dictates the

**[10:30]** prefill and decoding dictates the performance. So for example, if you have

**[10:31]** performance. So for example, if you have

**[10:31]** performance. So for example, if you have too many decode workers, you're pre

**[10:33]** too many decode workers, you're pre

**[10:33]** too many decode workers, you're pre you're you're basically going to have uh

**[10:35]** you're you're basically going to have uh

**[10:35]** you're you're basically going to have uh decode workers that are starving for

**[10:36]** decode workers that are starving for

**[10:36]** decode workers that are starving for work. And if you prefill workers, uh

**[10:39]** work. And if you prefill workers, uh

**[10:39]** work. And if you prefill workers, uh they're going to be generating work for

**[10:40]** they're going to be generating work for

**[10:40]** they're going to be generating work for the decode workers and the decode

**[10:41]** the decode workers and the decode

**[10:42]** the decode workers and the decode workers are going to be being pushed

**[10:43]** workers are going to be being pushed

**[10:43]** workers are going to be being pushed down by, you know, just an increasing

**[10:45]** down by, you know, just an increasing

**[10:46]** down by, you know, just an increasing amount of load and increasing Q depth.

**[10:48]** amount of load and increasing Q depth.

**[10:48]** amount of load and increasing Q depth. Um, and the other thing is that mo

**[10:51]** Um, and the other thing is that mo

**[10:51]** Um, and the other thing is that mo modifying this is kind of expensive and

**[10:53]** modifying this is kind of expensive and

**[10:53]** modifying this is kind of expensive and hard because the balance between prefill

**[10:55]** hard because the balance between prefill

**[10:55]** hard because the balance between prefill and decode depends on the par the

**[10:57]** and decode depends on the par the

**[10:57]** and decode depends on the par the parallel configs of each. So it's like

**[10:58]** parallel configs of each. So it's like

**[10:58]** parallel configs of each. So it's like this really wide configuration space.


### [11:00 - 12:00]

**[11:01]** this really wide configuration space.

**[11:01]** this really wide configuration space. One other thing that we talk about with

**[11:03]** One other thing that we talk about with

**[11:03]** One other thing that we talk about with respect to scale is routing. So we

**[11:05]** respect to scale is routing. So we

**[11:05]** respect to scale is routing. So we talked about how this KV is important.

**[11:07]** talked about how this KV is important.

**[11:07]** talked about how this KV is important. Um, one of the things that we have to do

**[11:09]** Um, one of the things that we have to do

**[11:09]** Um, one of the things that we have to do for pre uh pre-filled decode

**[11:11]** for pre uh pre-filled decode

**[11:11]** for pre uh pre-filled decode disagregation is that we need to

**[11:13]** disagregation is that we need to

**[11:13]** disagregation is that we need to actually transfer the KV between

**[11:15]** actually transfer the KV between

**[11:15]** actually transfer the KV between machines. And uh in some sense there's

**[11:18]** machines. And uh in some sense there's

**[11:18]** machines. And uh in some sense there's actually an affinity for some mean

**[11:19]** actually an affinity for some mean

**[11:19]** actually an affinity for some mean machines to do some work since the KV

**[11:21]** machines to do some work since the KV

**[11:21]** machines to do some work since the KV cache of previous requests is actually

**[11:23]** cache of previous requests is actually

**[11:23]** cache of previous requests is actually stored on those GPUs or offloaded onto

**[11:26]** stored on those GPUs or offloaded onto

**[11:26]** stored on those GPUs or offloaded onto uh system memory host or external

**[11:29]** uh system memory host or external

**[11:29]** uh system memory host or external storage uh during the course of of

**[11:32]** storage uh during the course of of

**[11:32]** storage uh during the course of of inference. So um I actually labeled this

**[11:35]** inference. So um I actually labeled this

**[11:35]** inference. So um I actually labeled this wrong. Uh this is not the smart router.

**[11:37]** wrong. Uh this is not the smart router.

**[11:37]** wrong. Uh this is not the smart router. Um uh this in in in a naive case you

**[11:41]** Um uh this in in in a naive case you

**[11:41]** Um uh this in in in a naive case you would route pretty much exclusively

**[11:43]** would route pretty much exclusively

**[11:43]** would route pretty much exclusively randomly, right? um or or towards uh you

**[11:47]** randomly, right? um or or towards uh you

**[11:47]** randomly, right? um or or towards uh you know any anything right so in this case

**[11:51]** know any anything right so in this case

**[11:51]** know any anything right so in this case we're biasing towards we're not biasing

**[11:53]** we're biasing towards we're not biasing

**[11:53]** we're biasing towards we're not biasing towards anything we're sampling randomly

**[11:55]** towards anything we're sampling randomly

**[11:55]** towards anything we're sampling randomly alternatively you know if we're talking

**[11:56]** alternatively you know if we're talking

**[11:56]** alternatively you know if we're talking about this uh routing to worker three in

**[11:58]** about this uh routing to worker three in

**[11:58]** about this uh routing to worker three in this case it could also be that you're


### [12:00 - 13:00]

**[12:00]** this case it could also be that you're

**[12:00]** this case it could also be that you're optimizing for purely your KV match um

**[12:03]** optimizing for purely your KV match um

**[12:03]** optimizing for purely your KV match um if you're doing a this is actually

**[12:05]** if you're doing a this is actually

**[12:05]** if you're doing a this is actually inverted if you're doing a a KV based

**[12:08]** inverted if you're doing a a KV based

**[12:08]** inverted if you're doing a a KV based router um uh you uh may end up biasing

**[12:12]** router um uh you uh may end up biasing

**[12:12]** router um uh you uh may end up biasing towards machines that have too high KV

**[12:14]** towards machines that have too high KV

**[12:14]** towards machines that have too high KV reload and therefore we're not going to

**[12:15]** reload and therefore we're not going to

**[12:15]** reload and therefore we're not going to be able to handle the request and you

**[12:16]** be able to handle the request and you

**[12:16]** be able to handle the request and you end up with queuing. Uh in a smart case,

**[12:18]** end up with queuing. Uh in a smart case,

**[12:18]** end up with queuing. Uh in a smart case, you actually want to minimize the uh

**[12:21]** you actually want to minimize the uh

**[12:22]** you actually want to minimize the uh sort of this cost function that includes

**[12:23]** sort of this cost function that includes

**[12:23]** sort of this cost function that includes both the amount of prefix match that you

**[12:25]** both the amount of prefix match that you

**[12:25]** both the amount of prefix match that you can get from uh or maximize the prefix

**[12:29]** can get from uh or maximize the prefix

**[12:29]** can get from uh or maximize the prefix match that you can get from uh the work

**[12:31]** match that you can get from uh the work

**[12:31]** match that you can get from uh the work that's already been done on that node

**[12:33]** that's already been done on that node

**[12:33]** that's already been done on that node and the amount of load that already

**[12:35]** and the amount of load that already

**[12:35]** and the amount of load that already exists on that node. Um, and as you

**[12:38]** exists on that node. Um, and as you

**[12:38]** exists on that node. Um, and as you scale out, as you get get more and more

**[12:40]** scale out, as you get get more and more

**[12:40]** scale out, as you get get more and more GPUs um, in a in a in a deployment, you

**[12:43]** GPUs um, in a in a in a deployment, you

**[12:43]** GPUs um, in a in a in a deployment, you actually end up with more and more

**[12:45]** actually end up with more and more

**[12:45]** actually end up with more and more represented KV space that's local to

**[12:48]** represented KV space that's local to

**[12:48]** represented KV space that's local to those machines. And because of that,

**[12:50]** those machines. And because of that,

**[12:50]** those machines. And because of that, having a larger and larger deployment

**[12:51]** having a larger and larger deployment

**[12:51]** having a larger and larger deployment means that you get an asmtoically

**[12:53]** means that you get an asmtoically

**[12:53]** means that you get an asmtoically increasing uh, KV cache hit rate, which

**[12:56]** increasing uh, KV cache hit rate, which

**[12:56]** increasing uh, KV cache hit rate, which means that you're doing less and less

**[12:59]** means that you're doing less and less

**[12:59]** means that you're doing less and less prefill work over time.


### [13:00 - 14:00]

**[13:01]** prefill work over time.

**[13:01]** prefill work over time. So routing, you know, here to give it a

**[13:03]** So routing, you know, here to give it a

**[13:03]** So routing, you know, here to give it a report card increases your speed and

**[13:05]** report card increases your speed and

**[13:05]** report card increases your speed and cost and doesn't really have an effect

**[13:06]** cost and doesn't really have an effect

**[13:06]** cost and doesn't really have an effect upon quality because it's it's doing the

**[13:08]** upon quality because it's it's doing the

**[13:08]** upon quality because it's it's doing the same work that it would normally do. Um,

**[13:11]** same work that it would normally do. Um,

**[13:11]** same work that it would normally do. Um, now we talk about structure. Structure

**[13:13]** now we talk about structure. Structure

**[13:13]** now we talk about structure. Structure is really important because we have a

**[13:15]** is really important because we have a

**[13:15]** is really important because we have a lot of these workloads that you guys

**[13:16]** lot of these workloads that you guys

**[13:16]** lot of these workloads that you guys have probably seen at the AI engineers

**[13:18]** have probably seen at the AI engineers

**[13:18]** have probably seen at the AI engineers world fair like agents for example. Um,

**[13:21]** world fair like agents for example. Um,

**[13:21]** world fair like agents for example. Um, agents impart a structure on the

**[13:23]** agents impart a structure on the

**[13:23]** agents impart a structure on the workload in that they have moderately

**[13:25]** workload in that they have moderately

**[13:25]** workload in that they have moderately predictable usage patterns between

**[13:27]** predictable usage patterns between

**[13:27]** predictable usage patterns between concurrent requests. So an example here

**[13:29]** concurrent requests. So an example here

**[13:29]** concurrent requests. So an example here is inference time scaling. This is a

**[13:31]** is inference time scaling. This is a

**[13:31]** is inference time scaling. This is a cool graph I'll go over really quickly.

**[13:32]** cool graph I'll go over really quickly.

**[13:32]** cool graph I'll go over really quickly. For example, we have three models here.

**[13:34]** For example, we have three models here.

**[13:34]** For example, we have three models here. In green we have an 8B model. In yellow

**[13:37]** In green we have an 8B model. In yellow

**[13:37]** In green we have an 8B model. In yellow we have a 49B model. And in red we have

**[13:39]** we have a 49B model. And in red we have

**[13:39]** we have a 49B model. And in red we have a 235B model. We find that with

**[13:41]** a 235B model. We find that with

**[13:41]** a 235B model. We find that with inference time scaling that is to

**[13:43]** inference time scaling that is to

**[13:43]** inference time scaling that is to re-query the model and to you know

**[13:45]** re-query the model and to you know

**[13:45]** re-query the model and to you know prompt it to reconsider its results or

**[13:47]** prompt it to reconsider its results or

**[13:47]** prompt it to reconsider its results or reason more about its results, we can

**[13:49]** reason more about its results, we can

**[13:49]** reason more about its results, we can produce better and better results. And

**[13:51]** produce better and better results. And

**[13:51]** produce better and better results. And you actually see this really interesting

**[13:52]** you actually see this really interesting

**[13:52]** you actually see this really interesting trend where uh with about three or four

**[13:56]** trend where uh with about three or four

**[13:56]** trend where uh with about three or four times of requering, we can see that the

**[13:58]** times of requering, we can see that the

**[13:58]** times of requering, we can see that the 8B model is basically on par with


### [14:00 - 15:00]

**[14:01]** 8B model is basically on par with

**[14:01]** 8B model is basically on par with respect to quality as the 49B model. And

**[14:04]** respect to quality as the 49B model. And

**[14:04]** respect to quality as the 49B model. And the 49B is almost on par with respect to

**[14:06]** the 49B is almost on par with respect to

**[14:06]** the 49B is almost on par with respect to quality as the 235B model. Um and we

**[14:11]** quality as the 235B model. Um and we

**[14:11]** quality as the 235B model. Um and we note here that like the cost of quering

**[14:14]** note here that like the cost of quering

**[14:14]** note here that like the cost of quering that AP model you know uh even quering

**[14:18]** that AP model you know uh even quering

**[14:18]** that AP model you know uh even quering it multiple times is actually lower than

**[14:20]** it multiple times is actually lower than

**[14:20]** it multiple times is actually lower than quering the uh the larger model right

**[14:24]** quering the uh the larger model right

**[14:24]** quering the uh the larger model right and in this sense you know we we b we

**[14:28]** and in this sense you know we we b we

**[14:28]** and in this sense you know we we b we basically see that inference time

**[14:29]** basically see that inference time

**[14:29]** basically see that inference time scaling can be considered sort of as you

**[14:32]** scaling can be considered sort of as you

**[14:32]** scaling can be considered sort of as you know increasing quality at the cost of

**[14:34]** know increasing quality at the cost of

**[14:34]** know increasing quality at the cost of speed and at the cost of uh cost right

**[14:37]** speed and at the cost of uh cost right

**[14:37]** speed and at the cost of uh cost right because you're you're requerering

**[14:39]** because you're you're requerering

**[14:39]** because you're you're requerering But alternatively, if you keep quality

**[14:41]** But alternatively, if you keep quality

**[14:41]** But alternatively, if you keep quality fixed, um you can basically get lower

**[14:46]** fixed, um you can basically get lower

**[14:46]** fixed, um you can basically get lower latency and lower cost by using a

**[14:49]** latency and lower cost by using a

**[14:49]** latency and lower cost by using a smaller model and requering it multiple

**[14:51]** smaller model and requering it multiple

**[14:51]** smaller model and requering it multiple times. And the structure that we infer

**[14:54]** times. And the structure that we infer

**[14:54]** times. And the structure that we infer or from doing that requiring allows us

**[14:57]** or from doing that requiring allows us

**[14:57]** or from doing that requiring allows us to do better scheduling. So in this

**[14:58]** to do better scheduling. So in this

**[14:58]** to do better scheduling. So in this graph we have a series of curves that


### [15:00 - 16:00]

**[15:00]** graph we have a series of curves that

**[15:00]** graph we have a series of curves that represent basically uh the runtime of a

**[15:03]** represent basically uh the runtime of a

**[15:04]** represent basically uh the runtime of a of a given reasoning example uh from the

**[15:06]** of a given reasoning example uh from the

**[15:06]** of a given reasoning example uh from the natural plan data set and the uh

**[15:09]** natural plan data set and the uh

**[15:09]** natural plan data set and the uh basically the the um concurrency. So

**[15:12]** basically the the um concurrency. So

**[15:12]** basically the the um concurrency. So this is like a graph of like how many

**[15:13]** this is like a graph of like how many

**[15:13]** this is like a graph of like how many you can how many in concurrent instances

**[15:15]** you can how many in concurrent instances

**[15:15]** you can how many in concurrent instances you can run at once and uh we sample

**[15:18]** you can run at once and uh we sample

**[15:18]** you can run at once and uh we sample across all this this concurrency. We see

**[15:20]** across all this this concurrency. We see

**[15:20]** across all this this concurrency. We see that implementing disagregation gives us

**[15:22]** that implementing disagregation gives us

**[15:22]** that implementing disagregation gives us a small benefit uh mostly because this

**[15:24]** a small benefit uh mostly because this

**[15:24]** a small benefit uh mostly because this data set is very ISL uh short ISL long

**[15:27]** data set is very ISL uh short ISL long

**[15:27]** data set is very ISL uh short ISL long OSL um you don't get a whole ton of

**[15:29]** OSL um you don't get a whole ton of

**[15:29]** OSL um you don't get a whole ton of benefit from disagregation in this case

**[15:32]** benefit from disagregation in this case

**[15:32]** benefit from disagregation in this case basically making uh you know removing a

**[15:34]** basically making uh you know removing a

**[15:34]** basically making uh you know removing a round trip by making the requeries come

**[15:37]** round trip by making the requeries come

**[15:37]** round trip by making the requeries come from the router instead of coming from

**[15:39]** from the router instead of coming from

**[15:39]** from the router instead of coming from the user or the client on the outside

**[15:41]** the user or the client on the outside

**[15:41]** the user or the client on the outside allows you to really decrease these

**[15:43]** allows you to really decrease these

**[15:43]** allows you to really decrease these round trips with respect to latency and

**[15:45]** round trips with respect to latency and

**[15:45]** round trips with respect to latency and then on top of that making the router

**[15:46]** then on top of that making the router

**[15:46]** then on top of that making the router aware and making the LMuler aware that

**[15:49]** aware and making the LMuler aware that

**[15:49]** aware and making the LMuler aware that you are doing you know repeat work

**[15:52]** you are doing you know repeat work

**[15:52]** you are doing you know repeat work you're requiring it actually gives you

**[15:54]** you're requiring it actually gives you

**[15:54]** you're requiring it actually gives you an increased benefit that is the red

**[15:56]** an increased benefit that is the red

**[15:56]** an increased benefit that is the red line to the green line that is to say

**[15:59]** line to the green line that is to say

**[15:59]** line to the green line that is to say amongst of a wide variety of models if


### [16:00 - 17:00]

**[16:01]** amongst of a wide variety of models if

**[16:01]** amongst of a wide variety of models if we assume that the quality is fixed we

**[16:04]** we assume that the quality is fixed we

**[16:04]** we assume that the quality is fixed we can actually use inference time scaling

**[16:06]** can actually use inference time scaling

**[16:06]** can actually use inference time scaling and some smart techniques in order to

**[16:07]** and some smart techniques in order to

**[16:07]** and some smart techniques in order to significantly decrease latency and

**[16:09]** significantly decrease latency and

**[16:09]** significantly decrease latency and increase throughput while maintaining

**[16:11]** increase throughput while maintaining

**[16:11]** increase throughput while maintaining the same quality

**[16:13]** the same quality

**[16:13]** the same quality one last thing and I'm going to go

**[16:14]** one last thing and I'm going to go

**[16:14]** one last thing and I'm going to go through this really quick because I'm

**[16:15]** through this really quick because I'm

**[16:15]** through this really quick because I'm getting low on time is manipulating K K

**[16:18]** getting low on time is manipulating K K

**[16:18]** getting low on time is manipulating K K and V values Right? We've sort of talked

**[16:21]** and V values Right? We've sort of talked

**[16:21]** and V values Right? We've sort of talked about how before there's this work that

**[16:22]** about how before there's this work that

**[16:22]** about how before there's this work that we do in prefill that we don't want to

**[16:24]** we do in prefill that we don't want to

**[16:24]** we do in prefill that we don't want to lose. We we do routing to ensure that we

**[16:27]** lose. We we do routing to ensure that we

**[16:27]** lose. We we do routing to ensure that we uh don't lose this KV and you know if we

**[16:32]** uh don't lose this KV and you know if we

**[16:32]** uh don't lose this KV and you know if we have like a workflow where we know the

**[16:33]** have like a workflow where we know the

**[16:34]** have like a workflow where we know the runtimes of things. So for example, if

**[16:36]** runtimes of things. So for example, if

**[16:36]** runtimes of things. So for example, if we do a, you know, a

**[16:40]** we do a, you know, a

**[16:40]** we do a, you know, a tool call, for example, and we know this

**[16:42]** tool call, for example, and we know this

**[16:42]** tool call, for example, and we know this tool call takes a moderately

**[16:44]** tool call takes a moderately

**[16:44]** tool call takes a moderately deterministic amount of time, we

**[16:46]** deterministic amount of time, we

**[16:46]** deterministic amount of time, we basically end up with this this KV

**[16:47]** basically end up with this this KV

**[16:47]** basically end up with this this KV eviction, right? If we have a tool call

**[16:49]** eviction, right? If we have a tool call

**[16:49]** eviction, right? If we have a tool call that takes 30 seconds, the KV is going

**[16:50]** that takes 30 seconds, the KV is going

**[16:50]** that takes 30 seconds, the KV is going to be swept out from HPM and you're not

**[16:52]** to be swept out from HPM and you're not

**[16:52]** to be swept out from HPM and you're not going to be able to use it in the future

**[16:54]** going to be able to use it in the future

**[16:54]** going to be able to use it in the future because it's no longer being cached. But

**[16:56]** because it's no longer being cached. But

**[16:56]** because it's no longer being cached. But if we know that it's going to be used

**[16:58]** if we know that it's going to be used

**[16:58]** if we know that it's going to be used again, why not just offload it, right?


### [17:00 - 18:00]

**[17:02]** again, why not just offload it, right?

**[17:02]** again, why not just offload it, right? Basically inference time scaling gives

**[17:04]** Basically inference time scaling gives

**[17:04]** Basically inference time scaling gives you structure to manipulate your KV.

**[17:06]** you structure to manipulate your KV.

**[17:06]** you structure to manipulate your KV. Tool calling gives you structure to

**[17:07]** Tool calling gives you structure to

**[17:07]** Tool calling gives you structure to manipulate your KV. So instead of doing

**[17:10]** manipulate your KV. So instead of doing

**[17:10]** manipulate your KV. So instead of doing another prefill uh the second time you

**[17:13]** another prefill uh the second time you

**[17:13]** another prefill uh the second time you might for example do prefill once do uh

**[17:17]** might for example do prefill once do uh

**[17:17]** might for example do prefill once do uh you know the LM call the decode once uh

**[17:20]** you know the LM call the decode once uh

**[17:20]** you know the LM call the decode once uh move it to host memory and then you know

**[17:22]** move it to host memory and then you know

**[17:22]** move it to host memory and then you know at the time at which you expect the tool

**[17:23]** at the time at which you expect the tool

**[17:23]** at the time at which you expect the tool to complete you move it right back into

**[17:25]** to complete you move it right back into

**[17:25]** to complete you move it right back into me into GPU memory so that's ready for

**[17:27]** me into GPU memory so that's ready for

**[17:27]** me into GPU memory so that's ready for the next LM call that will include this

**[17:29]** the next LM call that will include this

**[17:29]** the next LM call that will include this added context from the tool. So KV

**[17:31]** added context from the tool. So KV

**[17:31]** added context from the tool. So KV manipulation you know again increases

**[17:34]** manipulation you know again increases

**[17:34]** manipulation you know again increases your speed and decreases your cost while

**[17:36]** your speed and decreases your cost while

**[17:36]** your speed and decreases your cost while also you know improving your quality or

**[17:39]** also you know improving your quality or

**[17:39]** also you know improving your quality or not improving quality keeping quality

**[17:40]** not improving quality keeping quality

**[17:40]** not improving quality keeping quality constant. Um the last thing that we have

**[17:42]** constant. Um the last thing that we have

**[17:42]** constant. Um the last thing that we have to talk about here is dynamism. Um

**[17:45]** to talk about here is dynamism. Um

**[17:45]** to talk about here is dynamism. Um worker specialization is really

**[17:46]** worker specialization is really

**[17:46]** worker specialization is really important. As I said, since you have uh

**[17:49]** important. As I said, since you have uh

**[17:49]** important. As I said, since you have uh different charact characteristics of

**[17:50]** different charact characteristics of

**[17:50]** different charact characteristics of disagregation at different infant

**[17:52]** disagregation at different infant

**[17:52]** disagregation at different infant sequence links and output sequence

**[17:54]** sequence links and output sequence

**[17:54]** sequence links and output sequence links, you actually want to have a mix

**[17:56]** links, you actually want to have a mix

**[17:56]** links, you actually want to have a mix of aggregated and disagregated workers

**[17:58]** of aggregated and disagregated workers

**[17:58]** of aggregated and disagregated workers based on where you are in the OSL ISL


### [18:00 - 19:00]

**[18:00]** based on where you are in the OSL ISL

**[18:00]** based on where you are in the OSL ISL histogram. So at, you know, lower input

**[18:03]** histogram. So at, you know, lower input

**[18:03]** histogram. So at, you know, lower input sequence links and higher output

**[18:05]** sequence links and higher output

**[18:05]** sequence links and higher output sequence links, you might want to do

**[18:06]** sequence links, you might want to do

**[18:06]** sequence links, you might want to do aggregated with a higher tensor

**[18:07]** aggregated with a higher tensor

**[18:07]** aggregated with a higher tensor parallelism. In the middle of the range,

**[18:09]** parallelism. In the middle of the range,

**[18:09]** parallelism. In the middle of the range, you may want to use in the middle of the

**[18:10]** you may want to use in the middle of the

**[18:10]** you may want to use in the middle of the input sequence range, you may may want

**[18:12]** input sequence range, you may may want

**[18:12]** input sequence range, you may may want to use disagregated. And in the you know

**[18:15]** to use disagregated. And in the you know

**[18:15]** to use disagregated. And in the you know long context uh you know regime you may

**[18:19]** long context uh you know regime you may

**[18:19]** long context uh you know regime you may want to use disagregated with context

**[18:21]** want to use disagregated with context

**[18:21]** want to use disagregated with context parallelism. Now uh again this differs

**[18:23]** parallelism. Now uh again this differs

**[18:23]** parallelism. Now uh again this differs model to model uh and this is just an

**[18:25]** model to model uh and this is just an

**[18:25]** model to model uh and this is just an exemplary graph but um generally if you

**[18:29]** exemplary graph but um generally if you

**[18:29]** exemplary graph but um generally if you specialize workers you can also increase

**[18:31]** specialize workers you can also increase

**[18:32]** specialize workers you can also increase uh increase your speed decrease your

**[18:33]** uh increase your speed decrease your

**[18:33]** uh increase your speed decrease your cost while keeping quality the same

**[18:35]** cost while keeping quality the same

**[18:35]** cost while keeping quality the same because again you're not actually

**[18:36]** because again you're not actually

**[18:36]** because again you're not actually touching the execution what the model is

**[18:38]** touching the execution what the model is

**[18:38]** touching the execution what the model is executing you're not touching the math

**[18:40]** executing you're not touching the math

**[18:40]** executing you're not touching the math it's doing. Um, one last thing about

**[18:43]** it's doing. Um, one last thing about

**[18:43]** it's doing. Um, one last thing about dynamism is load balance is quite

**[18:45]** dynamism is load balance is quite

**[18:45]** dynamism is load balance is quite important. As I mentioned earlier, doing

**[18:48]** important. As I mentioned earlier, doing

**[18:48]** important. As I mentioned earlier, doing looking at the amount of P and D workers

**[18:51]** looking at the amount of P and D workers

**[18:51]** looking at the amount of P and D workers is really important to determine whether

**[18:53]** is really important to determine whether

**[18:53]** is really important to determine whether or not your disagregated deployment is

**[18:55]** or not your disagregated deployment is

**[18:55]** or not your disagregated deployment is going to be successful. So for example,

**[18:56]** going to be successful. So for example,

**[18:56]** going to be successful. So for example, if you have a histogram that you

**[18:58]** if you have a histogram that you

**[18:58]** if you have a histogram that you initially create your configuration

**[18:59]** initially create your configuration

**[18:59]** initially create your configuration based off of, for example, if you have


### [19:00 - 20:00]

**[19:01]** based off of, for example, if you have

**[19:01]** based off of, for example, if you have app A and app B that have like these two

**[19:03]** app A and app B that have like these two

**[19:03]** app A and app B that have like these two input sequence length and output

**[19:05]** input sequence length and output

**[19:05]** input sequence length and output sequence links, you may end up with this

**[19:07]** sequence links, you may end up with this

**[19:07]** sequence links, you may end up with this scenario where a change in user

**[19:09]** scenario where a change in user

**[19:09]** scenario where a change in user distribution causes significant issues

**[19:12]** distribution causes significant issues

**[19:12]** distribution causes significant issues with your deployment. You're de in this

**[19:14]** with your deployment. You're de in this

**[19:14]** with your deployment. You're de in this case by when you increase your input

**[19:17]** case by when you increase your input

**[19:17]** case by when you increase your input sequence length and output sequence

**[19:18]** sequence length and output sequence

**[19:18]** sequence length and output sequence length by a little bit more your input

**[19:20]** length by a little bit more your input

**[19:20]** length by a little bit more your input sequence length, you might create more

**[19:22]** sequence length, you might create more

**[19:22]** sequence length, you might create more demand for prefill workers than you do

**[19:24]** demand for prefill workers than you do

**[19:24]** demand for prefill workers than you do for decode workers. So your balance will

**[19:26]** for decode workers. So your balance will

**[19:26]** for decode workers. So your balance will change over time and this has been

**[19:28]** change over time and this has been

**[19:28]** change over time and this has been empirically proven by a wide variety of

**[19:30]** empirically proven by a wide variety of

**[19:30]** empirically proven by a wide variety of people that publish data. Um and you

**[19:34]** people that publish data. Um and you

**[19:34]** people that publish data. Um and you actually have to do autoscaling across

**[19:37]** actually have to do autoscaling across

**[19:37]** actually have to do autoscaling across these two you know types of instances in

**[19:39]** these two you know types of instances in

**[19:39]** these two you know types of instances in real time to account for changes in user

**[19:41]** real time to account for changes in user

**[19:42]** real time to account for changes in user usage distribution of your platform. Um

**[19:45]** usage distribution of your platform. Um

**[19:45]** usage distribution of your platform. Um so in this case dynamic load balancing

**[19:47]** so in this case dynamic load balancing

**[19:47]** so in this case dynamic load balancing uh increases your speed and keeps your

**[19:50]** uh increases your speed and keeps your

**[19:50]** uh increases your speed and keeps your cost low but mostly it's it's really

**[19:53]** cost low but mostly it's it's really

**[19:53]** cost low but mostly it's it's really just essential to ensuring that disagre

**[19:55]** just essential to ensuring that disagre

**[19:55]** just essential to ensuring that disagre disagre disagregation actually works to

**[19:58]** disagre disagregation actually works to

**[19:58]** disagre disagregation actually works to maximum potential. Um okay last things.


### [20:00 - 21:00]

**[20:01]** maximum potential. Um okay last things.

**[20:01]** maximum potential. Um okay last things. Uh here is the uh Dynamo repo. It's

**[20:03]** Uh here is the uh Dynamo repo. It's

**[20:03]** Uh here is the uh Dynamo repo. It's right here. Um it's github.com.

**[20:07]** right here. Um it's github.com.

**[20:07]** right here. Um it's github.com. Um we also have a Dynamo meetup that is

**[20:09]** Um we also have a Dynamo meetup that is

**[20:09]** Um we also have a Dynamo meetup that is being hosted tomorrow Thursday from 5 to

**[20:11]** being hosted tomorrow Thursday from 5 to

**[20:11]** being hosted tomorrow Thursday from 5 to 8:00 p.m. here in San Francisco. uh

**[20:14]** 8:00 p.m. here in San Francisco. uh

**[20:14]** 8:00 p.m. here in San Francisco. uh please come. We're going to be talking a

**[20:15]** please come. We're going to be talking a

**[20:15]** please come. We're going to be talking a lot more about how we actually implement

**[20:16]** lot more about how we actually implement

**[20:16]** lot more about how we actually implement these things at the event.


