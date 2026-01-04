# Build Dynamic Products, and Stop the AI Sideshow — Eliza Cabrera (Workday) + Jeremy Silva (Freeplay)

**Video URL:** https://www.youtube.com/watch?v=CB-4NKDYnRs

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** All right. Well, thank you for joining

**[00:17]** All right. Well, thank you for joining us. We are here to talk AI products and

**[00:20]** us. We are here to talk AI products and

**[00:20]** us. We are here to talk AI products and specifically dynamic products which

**[00:22]** specifically dynamic products which

**[00:22]** specifically dynamic products which we'll unpack in the next 20 minutes or

**[00:24]** we'll unpack in the next 20 minutes or

**[00:24]** we'll unpack in the next 20 minutes or so. A little bit about us before we jump

**[00:28]** so. A little bit about us before we jump

**[00:28]** so. A little bit about us before we jump in. I am Alisa Cabrera. I'm a principal

**[00:31]** in. I am Alisa Cabrera. I'm a principal

**[00:31]** in. I am Alisa Cabrera. I'm a principal AI product manager at Workday. I'm

**[00:34]** AI product manager at Workday. I'm

**[00:34]** AI product manager at Workday. I'm currently building with an incredible

**[00:35]** currently building with an incredible

**[00:35]** currently building with an incredible team our financial audit agent. I also

**[00:38]** team our financial audit agent. I also

**[00:38]** team our financial audit agent. I also led go to market for our policy agent as

**[00:41]** led go to market for our policy agent as

**[00:41]** led go to market for our policy agent as well as early access for our assistant

**[00:44]** well as early access for our assistant

**[00:44]** well as early access for our assistant which is more like a co-pilot as well as

**[00:46]** which is more like a co-pilot as well as

**[00:46]** which is more like a co-pilot as well as some of our early days kind of geni uh

**[00:48]** some of our early days kind of geni uh

**[00:48]** some of our early days kind of geni uh features as well. My name is Jeremy

**[00:50]** features as well. My name is Jeremy

**[00:50]** features as well. My name is Jeremy Silva. Uh I come from a data science

**[00:52]** Silva. Uh I come from a data science

**[00:52]** Silva. Uh I come from a data science machine learning background. Been

**[00:54]** machine learning background. Been

**[00:54]** machine learning background. Been building language models since the dark

**[00:55]** building language models since the dark

**[00:55]** building language models since the dark ages preGPT3 that is. Um, and now I lead

**[00:58]** ages preGPT3 that is. Um, and now I lead

**[00:58]** ages preGPT3 that is. Um, and now I lead product at a company called Free Play,


### [01:00 - 02:00]

**[01:00]** product at a company called Free Play,

**[01:00]** product at a company called Free Play, which exists to help teams build great

**[01:02]** which exists to help teams build great

**[01:02]** which exists to help teams build great AI products. Awesome. Let's get into it.

**[01:07]** AI products. Awesome. Let's get into it.

**[01:07]** AI products. Awesome. Let's get into it. So, if there's one thing that we want

**[01:09]** So, if there's one thing that we want

**[01:09]** So, if there's one thing that we want you to take away from this session, it's

**[01:11]** you to take away from this session, it's

**[01:12]** you to take away from this session, it's to stop the AI slideshow, which I know

**[01:14]** to stop the AI slideshow, which I know

**[01:14]** to stop the AI slideshow, which I know sounds a little bit counterintuitive.

**[01:17]** sounds a little bit counterintuitive.

**[01:17]** sounds a little bit counterintuitive. We're all at an AI conference. All of us

**[01:19]** We're all at an AI conference. All of us

**[01:19]** We're all at an AI conference. All of us are talking about agents and AI. It's

**[01:22]** are talking about agents and AI. It's

**[01:22]** are talking about agents and AI. It's all over the place, right? So, what

**[01:24]** all over the place, right? So, what

**[01:24]** all over the place, right? So, what exactly are we talking about here?

**[01:27]** exactly are we talking about here?

**[01:27]** exactly are we talking about here? Having AI leading your products, your go

**[01:30]** Having AI leading your products, your go

**[01:30]** Having AI leading your products, your go to market, your strategy. This was a

**[01:33]** to market, your strategy. This was a

**[01:33]** to market, your strategy. This was a really great approach when we were all

**[01:35]** really great approach when we were all

**[01:35]** really great approach when we were all trying to communicate that we were at

**[01:36]** trying to communicate that we were at

**[01:36]** trying to communicate that we were at the forefront of this technological

**[01:38]** the forefront of this technological

**[01:38]** the forefront of this technological disruption, right? But now everyone is

**[01:42]** disruption, right? But now everyone is

**[01:42]** disruption, right? But now everyone is really kind of saying the same thing.

**[01:45]** really kind of saying the same thing.

**[01:45]** really kind of saying the same thing. And if we look at the different products

**[01:48]** And if we look at the different products

**[01:48]** And if we look at the different products that have resulted in hindsight, which

**[01:51]** that have resulted in hindsight, which

**[01:51]** that have resulted in hindsight, which hindsight's kind of 2020, right? we're

**[01:53]** hindsight's kind of 2020, right? we're

**[01:53]** hindsight's kind of 2020, right? we're able to see that what we've been doing

**[01:55]** able to see that what we've been doing

**[01:55]** able to see that what we've been doing is building product to try to figure out

**[01:58]** is building product to try to figure out

**[01:58]** is building product to try to figure out what these different technological


### [02:00 - 03:00]

**[02:00]** what these different technological

**[02:00]** what these different technological breakthroughs can do for us.

**[02:03]** breakthroughs can do for us.

**[02:03]** breakthroughs can do for us. So, let's unpack what we're talking

**[02:05]** So, let's unpack what we're talking

**[02:05]** So, let's unpack what we're talking about here a bit.

**[02:08]** about here a bit.

**[02:08]** about here a bit. So let's go back maybe post chat GPT

**[02:11]** So let's go back maybe post chat GPT

**[02:11]** So let's go back maybe post chat GPT maybe for some of us in the room preGPT

**[02:13]** maybe for some of us in the room preGPT

**[02:14]** maybe for some of us in the room preGPT but whenever your sort of aha moment was

**[02:16]** but whenever your sort of aha moment was

**[02:16]** but whenever your sort of aha moment was with LLMs trying to figure out what you

**[02:19]** with LLMs trying to figure out what you

**[02:19]** with LLMs trying to figure out what you can do with the tech what you can't what

**[02:20]** can do with the tech what you can't what

**[02:20]** can do with the tech what you can't what the boundaries are we ended up using

**[02:23]** the boundaries are we ended up using

**[02:23]** the boundaries are we ended up using chat UIs content UIs existing

**[02:26]** chat UIs content UIs existing

**[02:26]** chat UIs content UIs existing applications right to be able to really

**[02:29]** applications right to be able to really

**[02:29]** applications right to be able to really test the boundaries of these LLMs we

**[02:32]** test the boundaries of these LLMs we

**[02:32]** test the boundaries of these LLMs we were also using multimodal to see what

**[02:34]** were also using multimodal to see what

**[02:34]** were also using multimodal to see what different kinds of inputs and outputs we

**[02:37]** different kinds of inputs and outputs we

**[02:37]** different kinds of inputs and outputs we could use the technology for.

**[02:40]** could use the technology for.

**[02:40]** could use the technology for. Then we realized we could ground the

**[02:43]** Then we realized we could ground the

**[02:43]** Then we realized we could ground the models. We had vector databases and rag.

**[02:47]** models. We had vector databases and rag.

**[02:47]** models. We had vector databases and rag. We were trying to get to accuracy and

**[02:49]** We were trying to get to accuracy and

**[02:49]** We were trying to get to accuracy and truth, if we can agree on that. Um, we

**[02:52]** truth, if we can agree on that. Um, we

**[02:52]** truth, if we can agree on that. Um, we had larger context windows and increased

**[02:55]** had larger context windows and increased

**[02:55]** had larger context windows and increased memory. We also weren't super um, I

**[02:59]** memory. We also weren't super um, I

**[02:59]** memory. We also weren't super um, I would say comfortable with having AI do


### [03:00 - 04:00]

**[03:02]** would say comfortable with having AI do

**[03:02]** would say comfortable with having AI do work for us. So everything was a

**[03:04]** work for us. So everything was a

**[03:04]** work for us. So everything was a co-pilot, right? a buddy next to us who

**[03:07]** co-pilot, right? a buddy next to us who

**[03:07]** co-pilot, right? a buddy next to us who can help us get things done, but we

**[03:09]** can help us get things done, but we

**[03:09]** can help us get things done, but we don't want to be taking anybody's jobs

**[03:10]** don't want to be taking anybody's jobs

**[03:10]** don't want to be taking anybody's jobs away. We don't want to be um sort of

**[03:13]** away. We don't want to be um sort of

**[03:13]** away. We don't want to be um sort of automating work until we realize that

**[03:17]** automating work until we realize that

**[03:17]** automating work until we realize that might actually be kind of nice to be

**[03:20]** might actually be kind of nice to be

**[03:20]** might actually be kind of nice to be able to have agents that can do things

**[03:22]** able to have agents that can do things

**[03:22]** able to have agents that can do things for us to reason to be able to use tools

**[03:26]** for us to reason to be able to use tools

**[03:26]** for us to reason to be able to use tools and various APIs to orchestrate across

**[03:29]** and various APIs to orchestrate across

**[03:29]** and various APIs to orchestrate across different business problems. And this is

**[03:31]** different business problems. And this is

**[03:31]** different business problems. And this is the state and sort of space I would say

**[03:33]** the state and sort of space I would say

**[03:33]** the state and sort of space I would say that we're in right now.

**[03:35]** that we're in right now.

**[03:35]** that we're in right now. We're not saying that these different

**[03:38]** We're not saying that these different

**[03:38]** We're not saying that these different approaches are wrong, but they're an

**[03:41]** approaches are wrong, but they're an

**[03:41]** approaches are wrong, but they're an approach to understand the technology

**[03:43]** approach to understand the technology

**[03:43]** approach to understand the technology and it's not going to build you a

**[03:45]** and it's not going to build you a

**[03:45]** and it's not going to build you a differentiated strategy because everyone

**[03:47]** differentiated strategy because everyone

**[03:47]** differentiated strategy because everyone is doing the same thing.

**[03:50]** is doing the same thing.

**[03:50]** is doing the same thing. So, why do we see these kind of like

**[03:53]** So, why do we see these kind of like

**[03:53]** So, why do we see these kind of like bolt-on non-ifferiated AI products

**[03:56]** bolt-on non-ifferiated AI products

**[03:56]** bolt-on non-ifferiated AI products persist?

**[03:57]** persist?

**[03:58]** persist? By working across dozens of enterprise

**[03:59]** By working across dozens of enterprise

**[03:59]** By working across dozens of enterprise companies at Free Play, we've noticed a


### [04:00 - 05:00]

**[04:01]** companies at Free Play, we've noticed a

**[04:01]** companies at Free Play, we've noticed a common trend emerge, which is companies

**[04:03]** common trend emerge, which is companies

**[04:03]** common trend emerge, which is companies know they rightly need to prioritize AI.

**[04:06]** know they rightly need to prioritize AI.

**[04:06]** know they rightly need to prioritize AI. But the way they do that is by creating

**[04:07]** But the way they do that is by creating

**[04:07]** But the way they do that is by creating this sort of centralized AI strategy.

**[04:10]** this sort of centralized AI strategy.

**[04:10]** this sort of centralized AI strategy. And what happens is this centralized AI

**[04:12]** And what happens is this centralized AI

**[04:12]** And what happens is this centralized AI strategy starts running as this sort of

**[04:14]** strategy starts running as this sort of

**[04:14]** strategy starts running as this sort of sidecar of their core product strategy

**[04:16]** sidecar of their core product strategy

**[04:16]** sidecar of their core product strategy rather than the two beeply integrated.

**[04:18]** rather than the two beeply integrated.

**[04:18]** rather than the two beeply integrated. there's different initiatives, sometimes

**[04:20]** there's different initiatives, sometimes

**[04:20]** there's different initiatives, sometimes even different teams, and then naturally

**[04:22]** even different teams, and then naturally

**[04:22]** even different teams, and then naturally these sort of like bolt-on,

**[04:24]** these sort of like bolt-on,

**[04:24]** these sort of like bolt-on, non-integrated AI features and products

**[04:26]** non-integrated AI features and products

**[04:26]** non-integrated AI features and products start to proliferate.

**[04:28]** start to proliferate.

**[04:28]** start to proliferate. So, what are some of the causes of this

**[04:30]** So, what are some of the causes of this

**[04:30]** So, what are some of the causes of this sort of AI sideshow that we're talking

**[04:31]** sort of AI sideshow that we're talking

**[04:32]** sort of AI sideshow that we're talking about here? The first is that companies

**[04:34]** about here? The first is that companies

**[04:34]** about here? The first is that companies seek to mitigate the risk associated

**[04:36]** seek to mitigate the risk associated

**[04:36]** seek to mitigate the risk associated with AI by quarantining to specific

**[04:39]** with AI by quarantining to specific

**[04:39]** with AI by quarantining to specific corners of the product. Albeit there

**[04:41]** corners of the product. Albeit there

**[04:41]** corners of the product. Albeit there like is new risk here, right? there's

**[04:43]** like is new risk here, right? there's

**[04:43]** like is new risk here, right? there's this new reliability question you have

**[04:44]** this new reliability question you have

**[04:44]** this new reliability question you have to ask yourself which is like can I even

**[04:46]** to ask yourself which is like can I even

**[04:46]** to ask yourself which is like can I even get this feature to work reliably enough

**[04:48]** get this feature to work reliably enough

**[04:48]** get this feature to work reliably enough to drive value for customers.

**[04:51]** to drive value for customers.

**[04:52]** to drive value for customers. Second,

**[04:53]** Second,

**[04:53]** Second, we see teams prioritizing the technology

**[04:57]** we see teams prioritizing the technology

**[04:57]** we see teams prioritizing the technology over their customer needs. They become

**[04:58]** over their customer needs. They become

**[04:58]** over their customer needs. They become the hammer in search of the nail. Rather


### [05:00 - 06:00]

**[05:00]** the hammer in search of the nail. Rather

**[05:00]** the hammer in search of the nail. Rather than trying to solve their customer

**[05:01]** than trying to solve their customer

**[05:01]** than trying to solve their customer problem by harnessing the technology,

**[05:03]** problem by harnessing the technology,

**[05:03]** problem by harnessing the technology, they're just trying to find any

**[05:05]** they're just trying to find any

**[05:05]** they're just trying to find any manifestation of that technology. And we

**[05:07]** manifestation of that technology. And we

**[05:07]** manifestation of that technology. And we see this manifest in a bunch of

**[05:08]** see this manifest in a bunch of

**[05:08]** see this manifest in a bunch of predictable ways. We see teams building

**[05:10]** predictable ways. We see teams building

**[05:10]** predictable ways. We see teams building chatbots because chatbots demonstrate AI

**[05:13]** chatbots because chatbots demonstrate AI

**[05:13]** chatbots because chatbots demonstrate AI capability, not because customers are

**[05:15]** capability, not because customers are

**[05:15]** capability, not because customers are actually struggling with support. We see

**[05:17]** actually struggling with support. We see

**[05:17]** actually struggling with support. We see companies building document

**[05:18]** companies building document

**[05:18]** companies building document summarization again because it

**[05:19]** summarization again because it

**[05:19]** summarization again because it demonstrates capability, not because

**[05:21]** demonstrates capability, not because

**[05:21]** demonstrates capability, not because their users are suffering with

**[05:23]** their users are suffering with

**[05:23]** their users are suffering with information overload.

**[05:26]** information overload.

**[05:26]** information overload. And finally, we see companies creating

**[05:28]** And finally, we see companies creating

**[05:28]** And finally, we see companies creating this kind of top down the pushing

**[05:30]** this kind of top down the pushing

**[05:30]** this kind of top down the pushing solutions out from the top down rather

**[05:32]** solutions out from the top down rather

**[05:32]** solutions out from the top down rather than setting that top level strategy and

**[05:34]** than setting that top level strategy and

**[05:34]** than setting that top level strategy and letting the bottoms up discovery process

**[05:36]** letting the bottoms up discovery process

**[05:36]** letting the bottoms up discovery process um be the manifestation of that

**[05:38]** um be the manifestation of that

**[05:38]** um be the manifestation of that priority.

**[05:43]** So, how do you avoid the AI sideshow

**[05:43]** So, how do you avoid the AI sideshow here? The key is to integrate and align

**[05:46]** here? The key is to integrate and align

**[05:46]** here? The key is to integrate and align your AI and your product and integrating

**[05:49]** your AI and your product and integrating

**[05:49]** your AI and your product and integrating AI risk into planning is a critical part

**[05:51]** AI risk into planning is a critical part

**[05:51]** AI risk into planning is a critical part of that.

**[05:53]** of that.

**[05:53]** of that. There is this new risk we're talking

**[05:54]** There is this new risk we're talking

**[05:54]** There is this new risk we're talking about, but instead of being shying away

**[05:57]** about, but instead of being shying away

**[05:57]** about, but instead of being shying away from that risk and trying to quarantine

**[05:58]** from that risk and trying to quarantine

**[05:58]** from that risk and trying to quarantine AI to specific corners of the product or


### [06:00 - 07:00]

**[06:00]** AI to specific corners of the product or

**[06:00]** AI to specific corners of the product or specific teams, you need to deeply

**[06:02]** specific teams, you need to deeply

**[06:02]** specific teams, you need to deeply integrate that into your product

**[06:04]** integrate that into your product

**[06:04]** integrate that into your product planning. And this will require like

**[06:06]** planning. And this will require like

**[06:06]** planning. And this will require like some new muscles here, right? like you

**[06:07]** some new muscles here, right? like you

**[06:08]** some new muscles here, right? like you need to kind of build these systems for

**[06:09]** need to kind of build these systems for

**[06:09]** need to kind of build these systems for evaluation, for testing because if

**[06:11]** evaluation, for testing because if

**[06:11]** evaluation, for testing because if you're doing good prototyping and

**[06:12]** you're doing good prototyping and

**[06:12]** you're doing good prototyping and testing, you can at least kind of wrap

**[06:14]** testing, you can at least kind of wrap

**[06:14]** testing, you can at least kind of wrap your arms around that risk and know how

**[06:16]** your arms around that risk and know how

**[06:16]** your arms around that risk and know how to handle it. And then second, start

**[06:19]** to handle it. And then second, start

**[06:19]** to handle it. And then second, start with the customer problem. If you're

**[06:21]** with the customer problem. If you're

**[06:21]** with the customer problem. If you're inventing new problems to go solve with

**[06:22]** inventing new problems to go solve with

**[06:22]** inventing new problems to go solve with the advent of AI, you're probably going

**[06:24]** the advent of AI, you're probably going

**[06:24]** the advent of AI, you're probably going to stray here. And finally, like we

**[06:27]** to stray here. And finally, like we

**[06:27]** to stray here. And finally, like we talked about, enable that bottoms up

**[06:28]** talked about, enable that bottoms up

**[06:28]** talked about, enable that bottoms up discovery process for AI products. It's

**[06:31]** discovery process for AI products. It's

**[06:31]** discovery process for AI products. It's likely your product folks who are boots

**[06:33]** likely your product folks who are boots

**[06:33]** likely your product folks who are boots on the ground every day who understand

**[06:35]** on the ground every day who understand

**[06:35]** on the ground every day who understand the right solutions here. Give them the

**[06:38]** the right solutions here. Give them the

**[06:38]** the right solutions here. Give them the space to experiment, prototype, and

**[06:40]** space to experiment, prototype, and

**[06:40]** space to experiment, prototype, and importantly fail fast, but set that

**[06:42]** importantly fail fast, but set that

**[06:42]** importantly fail fast, but set that topline strategy and then allow the

**[06:44]** topline strategy and then allow the

**[06:44]** topline strategy and then allow the bottoms up discovery process to take

**[06:46]** bottoms up discovery process to take

**[06:46]** bottoms up discovery process to take place. This is how you ultimately

**[06:48]** place. This is how you ultimately

**[06:48]** place. This is how you ultimately manifest AI products that feel a like a

**[06:51]** manifest AI products that feel a like a

**[06:51]** manifest AI products that feel a like a natural and cohesive part of the product

**[06:53]** natural and cohesive part of the product

**[06:53]** natural and cohesive part of the product experience rather than feeling bolt-on.

**[06:56]** experience rather than feeling bolt-on.

**[06:56]** experience rather than feeling bolt-on. And that's al ultimately the like the

**[06:58]** And that's al ultimately the like the

**[06:58]** And that's al ultimately the like the hallmark of good successful AI


### [07:00 - 08:00]

**[07:00]** hallmark of good successful AI

**[07:00]** hallmark of good successful AI integration are AI products that need

**[07:02]** integration are AI products that need

**[07:02]** integration are AI products that need not announce themselves as AI but rather

**[07:05]** not announce themselves as AI but rather

**[07:05]** not announce themselves as AI but rather just solve the customer problem better

**[07:07]** just solve the customer problem better

**[07:07]** just solve the customer problem better than what came before.

**[07:09]** than what came before.

**[07:09]** than what came before. So the north star that Eliza and I are

**[07:10]** So the north star that Eliza and I are

**[07:10]** So the north star that Eliza and I are talking about today are AI products that

**[07:13]** talking about today are AI products that

**[07:13]** talking about today are AI products that are deeply and dynamically integrated

**[07:15]** are deeply and dynamically integrated

**[07:15]** are deeply and dynamically integrated into your product ecosystem. But the

**[07:17]** into your product ecosystem. But the

**[07:17]** into your product ecosystem. But the only way you get there is by aligning

**[07:19]** only way you get there is by aligning

**[07:19]** only way you get there is by aligning your your strategy, your teams, and your

**[07:21]** your your strategy, your teams, and your

**[07:21]** your your strategy, your teams, and your road maps accordingly

**[07:23]** road maps accordingly

**[07:23]** road maps accordingly and importantly avoiding the AI

**[07:25]** and importantly avoiding the AI

**[07:25]** and importantly avoiding the AI sideshow.

**[07:27]** sideshow.

**[07:27]** sideshow. This is admittedly like an audacious

**[07:29]** This is admittedly like an audacious

**[07:29]** This is admittedly like an audacious northstar and especially if you're kind

**[07:31]** northstar and especially if you're kind

**[07:31]** northstar and especially if you're kind of stuck in this sideshow model like how

**[07:33]** of stuck in this sideshow model like how

**[07:33]** of stuck in this sideshow model like how do you find your way out? This is where

**[07:35]** do you find your way out? This is where

**[07:35]** do you find your way out? This is where we think this crawl, walk, run approach

**[07:37]** we think this crawl, walk, run approach

**[07:37]** we think this crawl, walk, run approach comes into play.

**[07:40]** comes into play.

**[07:40]** comes into play. We're all new to building generative AI

**[07:42]** We're all new to building generative AI

**[07:42]** We're all new to building generative AI products. Like to some degree or

**[07:43]** products. Like to some degree or

**[07:43]** products. Like to some degree or another, we're all building the plane

**[07:45]** another, we're all building the plane

**[07:45]** another, we're all building the plane while we're flying it. The most

**[07:47]** while we're flying it. The most

**[07:47]** while we're flying it. The most successful teams we see here are those

**[07:50]** successful teams we see here are those

**[07:50]** successful teams we see here are those that crawl, walk, run their way into

**[07:52]** that crawl, walk, run their way into

**[07:52]** that crawl, walk, run their way into this new era of kind of generative AI

**[07:55]** this new era of kind of generative AI

**[07:55]** this new era of kind of generative AI products. Because what that allows you

**[07:57]** products. Because what that allows you

**[07:57]** products. Because what that allows you to do is it allows you to sort of build

**[07:59]** to do is it allows you to sort of build

**[07:59]** to do is it allows you to sort of build the capability iteratively while laying


### [08:00 - 09:00]

**[08:01]** the capability iteratively while laying

**[08:01]** the capability iteratively while laying the fun the foundation of that AI

**[08:03]** the fun the foundation of that AI

**[08:04]** the fun the foundation of that AI functionality throughout your product

**[08:05]** functionality throughout your product

**[08:05]** functionality throughout your product suite. So I want to like walk through an

**[08:08]** suite. So I want to like walk through an

**[08:08]** suite. So I want to like walk through an example here um with an example. We'll

**[08:10]** example here um with an example. We'll

**[08:10]** example here um with an example. We'll take like an a customer support SAS

**[08:12]** take like an a customer support SAS

**[08:12]** take like an a customer support SAS company. Let's say they have like a

**[08:13]** company. Let's say they have like a

**[08:13]** company. Let's say they have like a shared inbox feature um that customer

**[08:16]** shared inbox feature um that customer

**[08:16]** shared inbox feature um that customer support teams come on to work out of

**[08:18]** support teams come on to work out of

**[08:18]** support teams come on to work out of mature product um but they want to start

**[08:20]** mature product um but they want to start

**[08:20]** mature product um but they want to start integrating AI. So in this crawl phase

**[08:23]** integrating AI. So in this crawl phase

**[08:23]** integrating AI. So in this crawl phase you're starting to build embedded AI

**[08:25]** you're starting to build embedded AI

**[08:25]** you're starting to build embedded AI experiences.

**[08:27]** experiences.

**[08:27]** experiences. You're likely in this phase not building

**[08:29]** You're likely in this phase not building

**[08:29]** You're likely in this phase not building a whole lot of new product surface area.

**[08:31]** a whole lot of new product surface area.

**[08:31]** a whole lot of new product surface area. Rather you're just like adding AI on the

**[08:33]** Rather you're just like adding AI on the

**[08:33]** Rather you're just like adding AI on the back end and starting to kind of

**[08:34]** back end and starting to kind of

**[08:34]** back end and starting to kind of accentuate and accelerate the existing

**[08:36]** accentuate and accelerate the existing

**[08:36]** accentuate and accelerate the existing functionality you have. If we take that

**[08:38]** functionality you have. If we take that

**[08:38]** functionality you have. If we take that customer support example, that might

**[08:40]** customer support example, that might

**[08:40]** customer support example, that might look something like, you know, building

**[08:41]** look something like, you know, building

**[08:41]** look something like, you know, building a feature that uses semantic search to

**[08:43]** a feature that uses semantic search to

**[08:43]** a feature that uses semantic search to like surface previous similar questions

**[08:46]** like surface previous similar questions

**[08:46]** like surface previous similar questions to help the c the user ground when they

**[08:48]** to help the c the user ground when they

**[08:48]** to help the c the user ground when they like are responding to their customer.

**[08:50]** like are responding to their customer.

**[08:50]** like are responding to their customer. And then in the walk phase,

**[08:53]** And then in the walk phase,

**[08:53]** And then in the walk phase, this is where we're starting to build

**[08:54]** this is where we're starting to build

**[08:54]** this is where we're starting to build more contextual and personalized AI

**[08:56]** more contextual and personalized AI

**[08:56]** more contextual and personalized AI experiences. Here we might actually we

**[08:59]** experiences. Here we might actually we

**[08:59]** experiences. Here we might actually we are starting to build like new product


### [09:00 - 10:00]

**[09:01]** are starting to build like new product

**[09:01]** are starting to build like new product surface area but we're probably not at

**[09:03]** surface area but we're probably not at

**[09:03]** surface area but we're probably not at the point yet where we need to like

**[09:04]** the point yet where we need to like

**[09:04]** the point yet where we need to like fundamentally rethink our core app

**[09:06]** fundamentally rethink our core app

**[09:06]** fundamentally rethink our core app architecture and our UX. If we go back

**[09:08]** architecture and our UX. If we go back

**[09:08]** architecture and our UX. If we go back to that example that might look

**[09:10]** to that example that might look

**[09:10]** to that example that might look something like um you know building a

**[09:12]** something like um you know building a

**[09:12]** something like um you know building a feature that will like suggest a draft

**[09:15]** feature that will like suggest a draft

**[09:15]** feature that will like suggest a draft ahead of time so that when the the user

**[09:16]** ahead of time so that when the the user

**[09:16]** ahead of time so that when the the user comes in there's already a draft there

**[09:18]** comes in there's already a draft there

**[09:18]** comes in there's already a draft there ready to go for them to start from. And

**[09:20]** ready to go for them to start from. And

**[09:20]** ready to go for them to start from. And then finally where we land when we

**[09:22]** then finally where we land when we

**[09:22]** then finally where we land when we really start to run. This is where we're

**[09:23]** really start to run. This is where we're

**[09:24]** really start to run. This is where we're building those dynamic interoperable and

**[09:26]** building those dynamic interoperable and

**[09:26]** building those dynamic interoperable and integrated AI experiences throughout our

**[09:29]** integrated AI experiences throughout our

**[09:29]** integrated AI experiences throughout our product suite. This is the stage where

**[09:31]** product suite. This is the stage where

**[09:31]** product suite. This is the stage where you do start needing to like re

**[09:33]** you do start needing to like re

**[09:33]** you do start needing to like re fundamentally rethink your UI, your UX

**[09:35]** fundamentally rethink your UI, your UX

**[09:36]** fundamentally rethink your UI, your UX and your app architecture because now

**[09:38]** and your app architecture because now

**[09:38]** and your app architecture because now your AI features like if we go back to

**[09:40]** your AI features like if we go back to

**[09:40]** your AI features like if we go back to our customer support example, it might

**[09:42]** our customer support example, it might

**[09:42]** our customer support example, it might look like an autonomous agent that can

**[09:43]** look like an autonomous agent that can

**[09:44]** look like an autonomous agent that can triage issues, respond to customers, but

**[09:45]** triage issues, respond to customers, but

**[09:45]** triage issues, respond to customers, but importantly it's operating across the

**[09:47]** importantly it's operating across the

**[09:47]** importantly it's operating across the product and and feature set. And in

**[09:50]** product and and feature set. And in

**[09:50]** product and and feature set. And in order to incorporate that kind of

**[09:51]** order to incorporate that kind of

**[09:51]** order to incorporate that kind of functionality, you do need to start

**[09:53]** functionality, you do need to start

**[09:53]** functionality, you do need to start rebuilding core surface area and like

**[09:55]** rebuilding core surface area and like

**[09:55]** rebuilding core surface area and like starting to revisit your UX. But

**[09:58]** starting to revisit your UX. But

**[09:58]** starting to revisit your UX. But importantly along the way, you're not

**[09:59]** importantly along the way, you're not

**[09:59]** importantly along the way, you're not throwing out functionality. It's


### [10:00 - 11:00]

**[10:02]** throwing out functionality. It's

**[10:02]** throwing out functionality. It's building on top of each other. It's that

**[10:04]** building on top of each other. It's that

**[10:04]** building on top of each other. It's that functionality is building as you go,

**[10:05]** functionality is building as you go,

**[10:06]** functionality is building as you go, right? You're just extending on it. And

**[10:07]** right? You're just extending on it. And

**[10:07]** right? You're just extending on it. And importantly, even at the crawl phase,

**[10:09]** importantly, even at the crawl phase,

**[10:09]** importantly, even at the crawl phase, you're still building embedded

**[10:11]** you're still building embedded

**[10:11]** you're still building embedded functionality, not this sort of like

**[10:13]** functionality, not this sort of like

**[10:13]** functionality, not this sort of like bolt-on non-integrated functionality. So

**[10:16]** bolt-on non-integrated functionality. So

**[10:16]** bolt-on non-integrated functionality. So I'll pass it to Alisa now. Yeah. So

**[10:19]** I'll pass it to Alisa now. Yeah. So

**[10:19]** I'll pass it to Alisa now. Yeah. So let's walk through a tangible example

**[10:21]** let's walk through a tangible example

**[10:21]** let's walk through a tangible example here because it there's a lot to unpack.

**[10:24]** here because it there's a lot to unpack.

**[10:24]** here because it there's a lot to unpack. So this problem space, I feel like

**[10:26]** So this problem space, I feel like

**[10:26]** So this problem space, I feel like everyone knows this. I've been living

**[10:27]** everyone knows this. I've been living

**[10:28]** everyone knows this. I've been living and breathing it for a few years, but HR

**[10:30]** and breathing it for a few years, but HR

**[10:30]** and breathing it for a few years, but HR service delivery or employee

**[10:32]** service delivery or employee

**[10:32]** service delivery or employee self-service is all of us work in jobs

**[10:35]** self-service is all of us work in jobs

**[10:35]** self-service is all of us work in jobs or you're running a company. Your

**[10:36]** or you're running a company. Your

**[10:36]** or you're running a company. Your employees need to be able to get their

**[10:38]** employees need to be able to get their

**[10:38]** employees need to be able to get their questions answered quickly. And if they

**[10:40]** questions answered quickly. And if they

**[10:40]** questions answered quickly. And if they can't get those questions answered, they

**[10:42]** can't get those questions answered, they

**[10:42]** can't get those questions answered, they need help from a a a support person. So

**[10:45]** need help from a a a support person. So

**[10:45]** need help from a a a support person. So through a case, this could be a live

**[10:46]** through a case, this could be a live

**[10:46]** through a case, this could be a live agent, etc. So we've spent a lot of time

**[10:49]** agent, etc. So we've spent a lot of time

**[10:49]** agent, etc. So we've spent a lot of time working in this space. This is also

**[10:51]** working in this space. This is also

**[10:51]** working in this space. This is also where some products have found product

**[10:53]** where some products have found product

**[10:53]** where some products have found product market fit especially with early sort of

**[10:55]** market fit especially with early sort of

**[10:55]** market fit especially with early sort of genai solutions.

**[10:57]** genai solutions.

**[10:57]** genai solutions. So where we started to I would say crawl


### [11:00 - 12:00]

**[11:00]** So where we started to I would say crawl

**[11:00]** So where we started to I would say crawl with the technology um this was within

**[11:03]** with the technology um this was within

**[11:03]** with the technology um this was within our help product. So help has two

**[11:05]** our help product. So help has two

**[11:06]** our help product. So help has two components. There's a knowledgebased

**[11:07]** components. There's a knowledgebased

**[11:07]** components. There's a knowledgebased solution. There's also a case management

**[11:09]** solution. There's also a case management

**[11:09]** solution. There's also a case management solution. And so early days we took a

**[11:11]** solution. And so early days we took a

**[11:11]** solution. And so early days we took a look at the tech and said where can we

**[11:13]** look at the tech and said where can we

**[11:13]** look at the tech and said where can we use Gen AI really to affect change with

**[11:16]** use Gen AI really to affect change with

**[11:16]** use Gen AI really to affect change with customers? And so I know knowledge base

**[11:18]** customers? And so I know knowledge base

**[11:18]** customers? And so I know knowledge base has become like the backend for GPTs and

**[11:20]** has become like the backend for GPTs and

**[11:20]** has become like the backend for GPTs and just a best practice, but at the time we

**[11:23]** just a best practice, but at the time we

**[11:23]** just a best practice, but at the time we said, okay, we've got content gen in

**[11:24]** said, okay, we've got content gen in

**[11:24]** said, okay, we've got content gen in here. We've got translations in here.

**[11:26]** here. We've got translations in here.

**[11:26]** here. We've got translations in here. This is the content that's fueling the

**[11:28]** This is the content that's fueling the

**[11:28]** This is the content that's fueling the answers to all of those questions that

**[11:30]** answers to all of those questions that

**[11:30]** answers to all of those questions that employees are asking. And so there were

**[11:32]** employees are asking. And so there were

**[11:32]** employees are asking. And so there were two key features. So one was actually

**[11:34]** two key features. So one was actually

**[11:34]** two key features. So one was actually content authors. So they might come into

**[11:36]** content authors. So they might come into

**[11:36]** content authors. So they might come into an editor like this. They are going to

**[11:38]** an editor like this. They are going to

**[11:38]** an editor like this. They are going to upload say a policy doc. So imagine a

**[11:40]** upload say a policy doc. So imagine a

**[11:40]** upload say a policy doc. So imagine a benefits policy like 20 plus pages long.

**[11:43]** benefits policy like 20 plus pages long.

**[11:43]** benefits policy like 20 plus pages long. They don't want to necessarily write

**[11:45]** They don't want to necessarily write

**[11:45]** They don't want to necessarily write that article, right? but they could have

**[11:46]** that article, right? but they could have

**[11:46]** that article, right? but they could have the AI ingest it, create an employee

**[11:49]** the AI ingest it, create an employee

**[11:49]** the AI ingest it, create an employee FAQ. In this case, we had talking points

**[11:51]** FAQ. In this case, we had talking points

**[11:51]** FAQ. In this case, we had talking points for managers and they're able to get a

**[11:53]** for managers and they're able to get a

**[11:53]** for managers and they're able to get a consistent format. So, the other thing I

**[11:55]** consistent format. So, the other thing I

**[11:55]** consistent format. So, the other thing I would mention is we're thinking about

**[11:57]** would mention is we're thinking about

**[11:57]** would mention is we're thinking about content at scale. So, this isn't for

**[11:59]** content at scale. So, this isn't for

**[11:59]** content at scale. So, this isn't for small sort of SMBs. This is large


### [12:00 - 13:00]

**[12:01]** small sort of SMBs. This is large

**[12:01]** small sort of SMBs. This is large enterprise who have content teams of say

**[12:04]** enterprise who have content teams of say

**[12:04]** enterprise who have content teams of say like three to 15 people. And so, that

**[12:06]** like three to 15 people. And so, that

**[12:06]** like three to 15 people. And so, that you need to have united sort of voice

**[12:08]** you need to have united sort of voice

**[12:08]** you need to have united sort of voice around that content that's coming out.

**[12:10]** around that content that's coming out.

**[12:10]** around that content that's coming out. So on top of that other feature, we put

**[12:13]** So on top of that other feature, we put

**[12:13]** So on top of that other feature, we put this translations which you can see in

**[12:15]** this translations which you can see in

**[12:15]** this translations which you can see in the GIF here. In just a couple of

**[12:17]** the GIF here. In just a couple of

**[12:17]** the GIF here. In just a couple of clicks, I can go in and translate into

**[12:20]** clicks, I can go in and translate into

**[12:20]** clicks, I can go in and translate into one of the 34 different languages that

**[12:22]** one of the 34 different languages that

**[12:22]** one of the 34 different languages that we support. And you see we added on the

**[12:25]** we support. And you see we added on the

**[12:25]** we support. And you see we added on the lefth hand panel here and the ability to

**[12:27]** lefth hand panel here and the ability to

**[12:27]** lefth hand panel here and the ability to actually manage versions as well. So I

**[12:29]** actually manage versions as well. So I

**[12:29]** actually manage versions as well. So I might have my base article. I'm

**[12:31]** might have my base article. I'm

**[12:31]** might have my base article. I'm generating talking points in English and

**[12:33]** generating talking points in English and

**[12:33]** generating talking points in English and then I want to translate into French and

**[12:35]** then I want to translate into French and

**[12:35]** then I want to translate into French and Spanish um maybe Japanese. And you can

**[12:38]** Spanish um maybe Japanese. And you can

**[12:38]** Spanish um maybe Japanese. And you can see that you're managing those versions

**[12:40]** see that you're managing those versions

**[12:40]** see that you're managing those versions as well.

**[12:42]** as well.

**[12:42]** as well. A couple things I want to call out here.

**[12:44]** A couple things I want to call out here.

**[12:44]** A couple things I want to call out here. Yes, we're using Gen AI and

**[12:46]** Yes, we're using Gen AI and

**[12:46]** Yes, we're using Gen AI and translations, but this isn't in your

**[12:49]** translations, but this isn't in your

**[12:49]** translations, but this isn't in your face sparkles and chat bots and text

**[12:52]** face sparkles and chat bots and text

**[12:52]** face sparkles and chat bots and text fields all over the place. This was

**[12:54]** fields all over the place. This was

**[12:54]** fields all over the place. This was built for users who didn't know about

**[12:56]** built for users who didn't know about

**[12:56]** built for users who didn't know about Gen AI. This is 2023. Wanted to be able


### [13:00 - 14:00]

**[13:00]** Gen AI. This is 2023. Wanted to be able

**[13:00]** Gen AI. This is 2023. Wanted to be able to kind of get in and use the features

**[13:02]** to kind of get in and use the features

**[13:02]** to kind of get in and use the features without actually understanding the

**[13:03]** without actually understanding the

**[13:04]** without actually understanding the functionality. And it also, you know,

**[13:06]** functionality. And it also, you know,

**[13:06]** functionality. And it also, you know, keeping that human in the loop. We want

**[13:08]** keeping that human in the loop. We want

**[13:08]** keeping that human in the loop. We want to have the disclaimer around AI and so

**[13:10]** to have the disclaimer around AI and so

**[13:10]** to have the disclaimer around AI and so we make sure that we've got enough

**[13:12]** we make sure that we've got enough

**[13:12]** we make sure that we've got enough little purple sparkles to let them know

**[13:14]** little purple sparkles to let them know

**[13:14]** little purple sparkles to let them know what they're using. Um, but it's not the

**[13:17]** what they're using. Um, but it's not the

**[13:17]** what they're using. Um, but it's not the entire experience here. So this allowed

**[13:19]** entire experience here. So this allowed

**[13:19]** entire experience here. So this allowed us to go GA um in uh 2024

**[13:23]** us to go GA um in uh 2024

**[13:23]** us to go GA um in uh 2024 um R2 or August I should say um and sort

**[13:28]** um R2 or August I should say um and sort

**[13:28]** um R2 or August I should say um and sort of I would say kind of crawling with the

**[13:30]** of I would say kind of crawling with the

**[13:30]** of I would say kind of crawling with the functionality.

**[13:31]** functionality.

**[13:31]** functionality. So on top of that, so that's our our

**[13:34]** So on top of that, so that's our our

**[13:34]** So on top of that, so that's our our content teams. So then we moved into

**[13:37]** content teams. So then we moved into

**[13:37]** content teams. So then we moved into what I would say is walking. This was

**[13:40]** what I would say is walking. This was

**[13:40]** what I would say is walking. This was now we have our content drafted, but we

**[13:43]** now we have our content drafted, but we

**[13:43]** now we have our content drafted, but we actually need to solve the self-service

**[13:44]** actually need to solve the self-service

**[13:44]** actually need to solve the self-service problem. So as a manager, I might need

**[13:47]** problem. So as a manager, I might need

**[13:47]** problem. So as a manager, I might need to come in. Elaine in this case is

**[13:49]** to come in. Elaine in this case is

**[13:49]** to come in. Elaine in this case is trying to do a location change to San

**[13:51]** trying to do a location change to San

**[13:51]** trying to do a location change to San Francisco and she knows a lot of the

**[13:53]** Francisco and she knows a lot of the

**[13:53]** Francisco and she knows a lot of the fields but not all of them. And so she

**[13:56]** fields but not all of them. And so she

**[13:56]** fields but not all of them. And so she now has this sort of contextually aware

**[13:58]** now has this sort of contextually aware

**[13:58]** now has this sort of contextually aware co-pilot, workday assistant that lives


### [14:00 - 15:00]

**[14:00]** co-pilot, workday assistant that lives

**[14:00]** co-pilot, workday assistant that lives across workday that she can sort of

**[14:03]** across workday that she can sort of

**[14:03]** across workday that she can sort of prompt. A lot of us are familiar with

**[14:05]** prompt. A lot of us are familiar with

**[14:05]** prompt. A lot of us are familiar with this functionality. But a couple points

**[14:07]** this functionality. But a couple points

**[14:07]** this functionality. But a couple points I want to make here. One, we have the

**[14:09]** I want to make here. One, we have the

**[14:09]** I want to make here. One, we have the contextually aware suggestions. So it

**[14:11]** contextually aware suggestions. So it

**[14:11]** contextually aware suggestions. So it knows what's happening when I'm on the

**[14:12]** knows what's happening when I'm on the

**[14:12]** knows what's happening when I'm on the page. Also around the data processing,

**[14:15]** page. Also around the data processing,

**[14:15]** page. Also around the data processing, if you're looking at a help article,

**[14:17]** if you're looking at a help article,

**[14:17]** if you're looking at a help article, it's generally customer content, which

**[14:19]** it's generally customer content, which

**[14:19]** it's generally customer content, which is sensitive but not nearly as sensitive

**[14:21]** is sensitive but not nearly as sensitive

**[14:21]** is sensitive but not nearly as sensitive as PII or personally identifiable

**[14:23]** as PII or personally identifiable

**[14:23]** as PII or personally identifiable information. Think about these tasks

**[14:25]** information. Think about these tasks

**[14:26]** information. Think about these tasks more on say pay or compensation things

**[14:28]** more on say pay or compensation things

**[14:28]** more on say pay or compensation things that are really sensitive where

**[14:29]** that are really sensitive where

**[14:29]** that are really sensitive where employees are putting really sensitive

**[14:31]** employees are putting really sensitive

**[14:31]** employees are putting really sensitive information in. So this is a next level

**[14:34]** information in. So this is a next level

**[14:34]** information in. So this is a next level of um sort of walking with the

**[14:37]** of um sort of walking with the

**[14:37]** of um sort of walking with the capabilities. The other piece I'd

**[14:38]** capabilities. The other piece I'd

**[14:38]** capabilities. The other piece I'd mention is that this was a platform

**[14:40]** mention is that this was a platform

**[14:40]** mention is that this was a platform capability meaning that we had to be

**[14:42]** capability meaning that we had to be

**[14:42]** capability meaning that we had to be working across our suite. So we have HCM

**[14:45]** working across our suite. So we have HCM

**[14:45]** working across our suite. So we have HCM and financials think benefits

**[14:47]** and financials think benefits

**[14:47]** and financials think benefits procurement um core HCM etc. And so

**[14:51]** procurement um core HCM etc. And so

**[14:51]** procurement um core HCM etc. And so there's a higher level of sort of top

**[14:52]** there's a higher level of sort of top

**[14:52]** there's a higher level of sort of top down and bottoms up alignment that had

**[14:54]** down and bottoms up alignment that had

**[14:54]** down and bottoms up alignment that had to happen to get these capabilities out

**[14:57]** to happen to get these capabilities out

**[14:57]** to happen to get these capabilities out the door.

**[14:59]** the door.

**[14:59]** the door. Then finally um running. So extending


### [15:00 - 16:00]

**[15:02]** Then finally um running. So extending

**[15:02]** Then finally um running. So extending the same use case here. You may have

**[15:04]** the same use case here. You may have

**[15:04]** the same use case here. You may have seen a few months back we announced our

**[15:07]** seen a few months back we announced our

**[15:07]** seen a few months back we announced our agent system of record. A subset of that

**[15:10]** agent system of record. A subset of that

**[15:10]** agent system of record. A subset of that functionality targeted towards again

**[15:12]** functionality targeted towards again

**[15:12]** functionality targeted towards again those employees and managers was really

**[15:14]** those employees and managers was really

**[15:14]** those employees and managers was really around the agentic capabilities behind

**[15:17]** around the agentic capabilities behind

**[15:17]** around the agentic capabilities behind the workday assistant. So again, our

**[15:19]** the workday assistant. So again, our

**[15:19]** the workday assistant. So again, our users don't necessarily want to know or

**[15:22]** users don't necessarily want to know or

**[15:22]** users don't necessarily want to know or have the sort of technical expertise

**[15:25]** have the sort of technical expertise

**[15:25]** have the sort of technical expertise around agents, but we still have that

**[15:27]** around agents, but we still have that

**[15:27]** around agents, but we still have that work happening behind the scenes where

**[15:30]** work happening behind the scenes where

**[15:30]** work happening behind the scenes where our assistant becomes a lot more

**[15:31]** our assistant becomes a lot more

**[15:32]** our assistant becomes a lot more autonomous, proactive, listening to

**[15:34]** autonomous, proactive, listening to

**[15:34]** autonomous, proactive, listening to policy changes, notifying us with

**[15:36]** policy changes, notifying us with

**[15:36]** policy changes, notifying us with suggestions as well. And so you can see

**[15:39]** suggestions as well. And so you can see

**[15:39]** suggestions as well. And so you can see just thinking through this at scale,

**[15:41]** just thinking through this at scale,

**[15:41]** just thinking through this at scale, there's a much higher level of I would

**[15:43]** there's a much higher level of I would

**[15:43]** there's a much higher level of I would say sort of top- down strategy with

**[15:45]** say sort of top- down strategy with

**[15:45]** say sort of top- down strategy with bottoms up execution that then happens

**[15:48]** bottoms up execution that then happens

**[15:48]** bottoms up execution that then happens threading the needle across um these

**[15:50]** threading the needle across um these

**[15:50]** threading the needle across um these different product experiences.

**[15:52]** different product experiences.

**[15:52]** different product experiences. So you can see here we've kind of gone

**[15:54]** So you can see here we've kind of gone

**[15:54]** So you can see here we've kind of gone from a single product within a skew all

**[15:56]** from a single product within a skew all

**[15:56]** from a single product within a skew all the way across our sort of core platform

**[15:59]** the way across our sort of core platform

**[15:59]** the way across our sort of core platform which um some of you may know or not,


### [16:00 - 17:00]

**[16:02]** which um some of you may know or not,

**[16:02]** which um some of you may know or not, but we serve uh like 60% of the S&P 500.

**[16:05]** but we serve uh like 60% of the S&P 500.

**[16:05]** but we serve uh like 60% of the S&P 500. So, a a pretty broad group. So, where we

**[16:09]** So, a a pretty broad group. So, where we

**[16:09]** So, a a pretty broad group. So, where we would land with all of this when we talk

**[16:11]** would land with all of this when we talk

**[16:11]** would land with all of this when we talk about not making AI a sideshow, we're

**[16:15]** about not making AI a sideshow, we're

**[16:15]** about not making AI a sideshow, we're not telling you to stop working on

**[16:17]** not telling you to stop working on

**[16:17]** not telling you to stop working on agents or stop caring about AI, but

**[16:20]** agents or stop caring about AI, but

**[16:20]** agents or stop caring about AI, but understand that these are stepping

**[16:22]** understand that these are stepping

**[16:22]** understand that these are stepping stones in terms of teaching your

**[16:24]** stones in terms of teaching your

**[16:24]** stones in terms of teaching your organization, training up your

**[16:26]** organization, training up your

**[16:26]** organization, training up your organization on what it means to

**[16:28]** organization on what it means to

**[16:28]** organization on what it means to actually be building impactful AI

**[16:31]** actually be building impactful AI

**[16:31]** actually be building impactful AI experiences. And so as you sort of I

**[16:34]** experiences. And so as you sort of I

**[16:34]** experiences. And so as you sort of I would say mature as an organization

**[16:36]** would say mature as an organization

**[16:36]** would say mature as an organization ideally where we want to get to is

**[16:39]** ideally where we want to get to is

**[16:39]** ideally where we want to get to is building dynamic products. I'm hearing

**[16:41]** building dynamic products. I'm hearing

**[16:41]** building dynamic products. I'm hearing some of this today in some of the talks

**[16:43]** some of this today in some of the talks

**[16:43]** some of this today in some of the talks if you heard Sarah or Brian talking

**[16:45]** if you heard Sarah or Brian talking

**[16:45]** if you heard Sarah or Brian talking earlier about building purposeful sort

**[16:48]** earlier about building purposeful sort

**[16:48]** earlier about building purposeful sort of vertical specific um products. I

**[16:52]** of vertical specific um products. I

**[16:52]** of vertical specific um products. I think it's really interesting when we

**[16:53]** think it's really interesting when we

**[16:53]** think it's really interesting when we start thinking about dynamic products in

**[16:55]** start thinking about dynamic products in

**[16:56]** start thinking about dynamic products in terms of new problem spaces. I don't

**[16:58]** terms of new problem spaces. I don't

**[16:58]** terms of new problem spaces. I don't know if anyone else feels this way, but

**[16:59]** know if anyone else feels this way, but


### [17:00 - 18:00]

**[17:00]** know if anyone else feels this way, but sometimes I feel like we're solving

**[17:01]** sometimes I feel like we're solving

**[17:01]** sometimes I feel like we're solving yesterday's roadmap with just like a

**[17:03]** yesterday's roadmap with just like a

**[17:03]** yesterday's roadmap with just like a much more powerful technology. And so as

**[17:06]** much more powerful technology. And so as

**[17:06]** much more powerful technology. And so as we digitize new data, new inputs in

**[17:09]** we digitize new data, new inputs in

**[17:09]** we digitize new data, new inputs in terms of our environment and spaces, we

**[17:12]** terms of our environment and spaces, we

**[17:12]** terms of our environment and spaces, we can see the problem space of the

**[17:13]** can see the problem space of the

**[17:13]** can see the problem space of the products that we're creating really sort

**[17:15]** products that we're creating really sort

**[17:16]** products that we're creating really sort of extend. Um I think especially with

**[17:18]** of extend. Um I think especially with

**[17:18]** of extend. Um I think especially with multimodal, this is where this gets

**[17:20]** multimodal, this is where this gets

**[17:20]** multimodal, this is where this gets really compelling as well. when we have

**[17:22]** really compelling as well. when we have

**[17:22]** really compelling as well. when we have frictionless multimodal experiences that

**[17:25]** frictionless multimodal experiences that

**[17:25]** frictionless multimodal experiences that interoperate I would say

**[17:26]** interoperate I would say

**[17:26]** interoperate I would say interoperability and RL are still pretty

**[17:28]** interoperability and RL are still pretty

**[17:28]** interoperability and RL are still pretty relevant within the agent sphere but

**[17:31]** relevant within the agent sphere but

**[17:31]** relevant within the agent sphere but when we think about dynamic products

**[17:33]** when we think about dynamic products

**[17:33]** when we think about dynamic products that are sort of responsive to your

**[17:35]** that are sort of responsive to your

**[17:35]** that are sort of responsive to your environment um this is where we really

**[17:38]** environment um this is where we really

**[17:38]** environment um this is where we really start to see I would say the next

**[17:39]** start to see I would say the next

**[17:39]** start to see I would say the next generation of products come into play.

**[17:42]** generation of products come into play.

**[17:42]** generation of products come into play. So hopefully this sparked a few thoughts

**[17:45]** So hopefully this sparked a few thoughts

**[17:45]** So hopefully this sparked a few thoughts maybe some questions. Um, if you want to

**[17:48]** maybe some questions. Um, if you want to

**[17:48]** maybe some questions. Um, if you want to connect, feel free to, um, scan our QR

**[17:51]** connect, feel free to, um, scan our QR

**[17:51]** connect, feel free to, um, scan our QR codes. Happy to, uh, connect if you want

**[17:53]** codes. Happy to, uh, connect if you want

**[17:53]** codes. Happy to, uh, connect if you want to drop us a note. We'll also be around

**[17:55]** to drop us a note. We'll also be around

**[17:55]** to drop us a note. We'll also be around the rest of the week, so happy to chat.

**[17:58]** the rest of the week, so happy to chat.

**[17:58]** the rest of the week, so happy to chat. And we are right at time. Look at that.


### [18:00 - 19:00]

**[18:01]** And we are right at time. Look at that.

**[18:01]** And we are right at time. Look at that. Okay, thanks everyone.


