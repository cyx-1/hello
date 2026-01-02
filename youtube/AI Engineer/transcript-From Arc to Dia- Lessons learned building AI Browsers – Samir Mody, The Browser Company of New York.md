# From Arc to Dia- Lessons learned building AI Browsers – Samir Mody, The Browser Company of New York

**Video URL:** https://www.youtube.com/watch?v=o4scJaQgnFA

---

## Full Transcript

### [00:00 - 01:00]

**[00:24]** My name is Samir and I'm the head of AI

**[00:24]** My name is Samir and I'm the head of AI engineering at the browser company of

**[00:26]** engineering at the browser company of

**[00:26]** engineering at the browser company of New York. And today I'm going to talk a

**[00:28]** New York. And today I'm going to talk a

**[00:28]** New York. And today I'm going to talk a little bit about how we transitioned

**[00:30]** little bit about how we transitioned

**[00:30]** little bit about how we transitioned from building ARC to DIA and the lessons

**[00:33]** from building ARC to DIA and the lessons

**[00:33]** from building ARC to DIA and the lessons we learned in building an AI browser.

**[00:37]** we learned in building an AI browser.

**[00:37]** we learned in building an AI browser. But first, a little about the browser

**[00:38]** But first, a little about the browser

**[00:38]** But first, a little about the browser company.

**[00:40]** company.

**[00:40]** company. So we started with a mission to rethink

**[00:43]** So we started with a mission to rethink

**[00:43]** So we started with a mission to rethink how people use the internet. At its

**[00:45]** how people use the internet. At its

**[00:45]** how people use the internet. At its core, we believe that the browser is one

**[00:48]** core, we believe that the browser is one

**[00:48]** core, we believe that the browser is one of the most important pieces of software

**[00:50]** of the most important pieces of software

**[00:50]** of the most important pieces of software in your life and it wasn't getting the

**[00:52]** in your life and it wasn't getting the

**[00:52]** in your life and it wasn't getting the attention it deserved. Simply put, the

**[00:56]** attention it deserved. Simply put, the

**[00:56]** attention it deserved. Simply put, the way we've used a browser has changed

**[00:58]** way we've used a browser has changed

**[00:58]** way we've used a browser has changed over the last couple decades, but the


### [01:00 - 02:00]

**[01:00]** over the last couple decades, but the

**[01:00]** over the last couple decades, but the browser itself hadn't. And think about

**[01:02]** browser itself hadn't. And think about

**[01:02]** browser itself hadn't. And think about this. We we started this company in

**[01:04]** this. We we started this company in

**[01:04]** this. We we started this company in 2019. Um, and so this is a screen cap of

**[01:08]** 2019. Um, and so this is a screen cap of

**[01:08]** 2019. Um, and so this is a screen cap of Josh, our CEO, sharing a little bit

**[01:11]** Josh, our CEO, sharing a little bit

**[01:11]** Josh, our CEO, sharing a little bit about our idea on the internet a few

**[01:13]** about our idea on the internet a few

**[01:13]** about our idea on the internet a few years ago, which we endearingly called

**[01:15]** years ago, which we endearingly called

**[01:15]** years ago, which we endearingly called the internet computer. So our mission

**[01:18]** the internet computer. So our mission

**[01:18]** the internet computer. So our mission has been to build a browser that

**[01:20]** has been to build a browser that

**[01:20]** has been to build a browser that reflects how people use the internet

**[01:22]** reflects how people use the internet

**[01:22]** reflects how people use the internet today and how we think the browser

**[01:25]** today and how we think the browser

**[01:25]** today and how we think the browser should be used tomorrow.

**[01:28]** should be used tomorrow.

**[01:28]** should be used tomorrow. So through years of discovery, trial and

**[01:33]** So through years of discovery, trial and

**[01:33]** So through years of discovery, trial and error, and some ups and downs, we

**[01:36]** error, and some ups and downs, we

**[01:36]** error, and some ups and downs, we shipped our first browser, Arc, in 2022.

**[01:40]** shipped our first browser, Arc, in 2022.

**[01:40]** shipped our first browser, Arc, in 2022. It was a browser we felt was an

**[01:42]** It was a browser we felt was an

**[01:42]** It was a browser we felt was an improvement over the browsers of that

**[01:44]** improvement over the browsers of that

**[01:44]** improvement over the browsers of that time. It made the internet more

**[01:46]** time. It made the internet more

**[01:46]** time. It made the internet more personal, more organized, and to us, a

**[01:49]** personal, more organized, and to us, a

**[01:49]** personal, more organized, and to us, a little more delightful with a little

**[01:51]** little more delightful with a little

**[01:51]** little more delightful with a little more craft.

**[01:52]** more craft.

**[01:52]** more craft. And it was a browser that was loved by

**[01:54]** And it was a browser that was loved by

**[01:54]** And it was a browser that was loved by many. It still is by millions, many of

**[01:57]** many. It still is by millions, many of

**[01:57]** many. It still is by millions, many of whom are probably in this audience

**[01:58]** whom are probably in this audience

**[01:58]** whom are probably in this audience today. I've gotten a lot of questions


### [02:00 - 03:00]

**[02:00]** today. I've gotten a lot of questions

**[02:00]** today. I've gotten a lot of questions about Arc today. Um, and uh, it's great,

**[02:05]** about Arc today. Um, and uh, it's great,

**[02:05]** about Arc today. Um, and uh, it's great, but um, if we took a step back, we felt

**[02:08]** but um, if we took a step back, we felt

**[02:08]** but um, if we took a step back, we felt that ARC was still just an incremental

**[02:10]** that ARC was still just an incremental

**[02:10]** that ARC was still just an incremental improvement over the browsers of that

**[02:12]** improvement over the browsers of that

**[02:12]** improvement over the browsers of that time. And it didn't really hit the

**[02:14]** time. And it didn't really hit the

**[02:14]** time. And it didn't really hit the vision that we set out to create. And

**[02:17]** vision that we set out to create. And

**[02:17]** vision that we set out to create. And so, uh, we kept building and then in

**[02:21]** so, uh, we kept building and then in

**[02:21]** so, uh, we kept building and then in 2022, we got access to LLMs like the GPT

**[02:24]** 2022, we got access to LLMs like the GPT

**[02:24]** 2022, we got access to LLMs like the GPT models. And so, we started like we

**[02:27]** models. And so, we started like we

**[02:27]** models. And so, we started like we always do with prototyping. We started

**[02:29]** always do with prototyping. We started

**[02:29]** always do with prototyping. We started trying new ideas um and eventually

**[02:32]** trying new ideas um and eventually

**[02:32]** trying new ideas um and eventually shipped a few of them in ARC. But what

**[02:35]** shipped a few of them in ARC. But what

**[02:35]** shipped a few of them in ARC. But what started as a you know a basic

**[02:37]** started as a you know a basic

**[02:37]** started as a you know a basic exploration turned into a fully formed

**[02:39]** exploration turned into a fully formed

**[02:39]** exploration turned into a fully formed thesis. In the beginning of 2024 uh our

**[02:43]** thesis. In the beginning of 2024 uh our

**[02:43]** thesis. In the beginning of 2024 uh our company put out what we called act 2 a

**[02:45]** company put out what we called act 2 a

**[02:45]** company put out what we called act 2 a video on YouTube where we shared that

**[02:48]** video on YouTube where we shared that

**[02:48]** video on YouTube where we shared that thesis that we believe that AI is going

**[02:51]** thesis that we believe that AI is going

**[02:51]** thesis that we believe that AI is going to transform how people use the internet

**[02:53]** to transform how people use the internet

**[02:53]** to transform how people use the internet and in turn fundamentally change the

**[02:56]** and in turn fundamentally change the

**[02:56]** and in turn fundamentally change the browser itself. And so with that we

**[02:59]** browser itself. And so with that we

**[02:59]** browser itself. And so with that we started building again but this time we


### [03:00 - 04:00]

**[03:01]** started building again but this time we

**[03:01]** started building again but this time we built a new browser with AI speed and

**[03:04]** built a new browser with AI speed and

**[03:04]** built a new browser with AI speed and security in mind and from the ground up.

**[03:08]** security in mind and from the ground up.

**[03:08]** security in mind and from the ground up. And later and sorry earlier this year we

**[03:10]** And later and sorry earlier this year we

**[03:10]** And later and sorry earlier this year we shipped DIA our AI native browser.

**[03:14]** shipped DIA our AI native browser.

**[03:14]** shipped DIA our AI native browser. It allows you to have an assistant

**[03:16]** It allows you to have an assistant

**[03:16]** It allows you to have an assistant alongside you in all the work you do in

**[03:17]** alongside you in all the work you do in

**[03:17]** alongside you in all the work you do in the browser. It gets to know you,

**[03:20]** the browser. It gets to know you,

**[03:20]** the browser. It gets to know you, personalizes, helps you get work done

**[03:22]** personalizes, helps you get work done

**[03:22]** personalizes, helps you get work done with your tabs, and effectively get more

**[03:25]** with your tabs, and effectively get more

**[03:25]** with your tabs, and effectively get more work done through the apps you use. And

**[03:29]** work done through the apps you use. And

**[03:29]** work done through the apps you use. And while it hasn't achieved our vision yet,

**[03:31]** while it hasn't achieved our vision yet,

**[03:31]** while it hasn't achieved our vision yet, we fully believe it's well on the way,

**[03:33]** we fully believe it's well on the way,

**[03:33]** we fully believe it's well on the way, too.

**[03:41]** So, it is not easy to build a product.

**[03:41]** So, it is not easy to build a product. You all know that. Let alone two, the

**[03:43]** You all know that. Let alone two, the

**[03:43]** You all know that. Let alone two, the latter of which an AI native one. We've

**[03:46]** latter of which an AI native one. We've

**[03:46]** latter of which an AI native one. We've had a lot of years of iteration, trial

**[03:48]** had a lot of years of iteration, trial

**[03:48]** had a lot of years of iteration, trial and error and through that we've learned

**[03:50]** and error and through that we've learned

**[03:50]** and error and through that we've learned a lot and I'm going to just talk about a

**[03:53]** a lot and I'm going to just talk about a

**[03:53]** a lot and I'm going to just talk about a few of those things uh here today.

**[03:57]** few of those things uh here today.

**[03:57]** few of those things uh here today. The first I want to talk about is

**[03:59]** The first I want to talk about is

**[03:59]** The first I want to talk about is optimizing your tools and process for


### [04:00 - 05:00]

**[04:01]** optimizing your tools and process for

**[04:01]** optimizing your tools and process for faster iteration. From the beginning,

**[04:03]** faster iteration. From the beginning,

**[04:03]** faster iteration. From the beginning, browser company has believed that we're

**[04:05]** browser company has believed that we're

**[04:05]** browser company has believed that we're not going to win unless we build the

**[04:07]** not going to win unless we build the

**[04:07]** not going to win unless we build the tools, the process, the platform, and

**[04:10]** tools, the process, the platform, and

**[04:10]** tools, the process, the platform, and the mindset to iterate, build, ship, and

**[04:13]** the mindset to iterate, build, ship, and

**[04:13]** the mindset to iterate, build, ship, and learn faster than everyone else. And

**[04:15]** learn faster than everyone else. And

**[04:15]** learn faster than everyone else. And that of course holds true today but the

**[04:17]** that of course holds true today but the

**[04:17]** that of course holds true today but the form it takes with AI and an AI native

**[04:20]** form it takes with AI and an AI native

**[04:20]** form it takes with AI and an AI native product has changed.

**[04:22]** product has changed.

**[04:22]** product has changed. So even as a small company where are we

**[04:25]** So even as a small company where are we

**[04:25]** So even as a small company where are we investing in tooling these days? First

**[04:28]** investing in tooling these days? First

**[04:28]** investing in tooling these days? First is prototyping for AI product features.

**[04:30]** is prototyping for AI product features.

**[04:30]** is prototyping for AI product features. Second is building and running evals.

**[04:33]** Second is building and running evals.

**[04:33]** Second is building and running evals. Third is collecting data for training

**[04:35]** Third is collecting data for training

**[04:35]** Third is collecting data for training and for eval

**[04:37]** and for eval

**[04:37]** and for eval uh last but definitely not least

**[04:38]** uh last but definitely not least

**[04:38]** uh last but definitely not least automation for hill climbing.

**[04:42]** automation for hill climbing.

**[04:42]** automation for hill climbing. So let's start with tools. Initially uh

**[04:45]** So let's start with tools. Initially uh

**[04:45]** So let's start with tools. Initially uh as we always do, we built some tools.

**[04:47]** as we always do, we built some tools.

**[04:47]** as we always do, we built some tools. The first was a very rudimentary uh

**[04:49]** The first was a very rudimentary uh

**[04:49]** The first was a very rudimentary uh prompt editor and it was only in dev

**[04:51]** prompt editor and it was only in dev

**[04:51]** prompt editor and it was only in dev builds. What did what did this mean for

**[04:54]** builds. What did what did this mean for

**[04:54]** builds. What did what did this mean for us? Well, it meant a few things. One,

**[04:56]** us? Well, it meant a few things. One,

**[04:56]** us? Well, it meant a few things. One, limited access as only engineers were

**[04:58]** limited access as only engineers were

**[04:58]** limited access as only engineers were able to access this. Two, slow iteration


### [05:00 - 06:00]

**[05:01]** able to access this. Two, slow iteration

**[05:01]** able to access this. Two, slow iteration speeds. And three, none of your personal

**[05:04]** speeds. And three, none of your personal

**[05:04]** speeds. And three, none of your personal context. And as you all know with an AI

**[05:05]** context. And as you all know with an AI

**[05:06]** context. And as you all know with an AI product, the context is what matters. It

**[05:07]** product, the context is what matters. It

**[05:07]** product, the context is what matters. It what gives you the feel for whether a

**[05:09]** what gives you the feel for whether a

**[05:09]** what gives you the feel for whether a product is good or not.

**[05:11]** product is good or not.

**[05:11]** product is good or not. So we evolved and since then we built

**[05:14]** So we evolved and since then we built

**[05:14]** So we evolved and since then we built all of our tools into our product, the

**[05:16]** all of our tools into our product, the

**[05:16]** all of our tools into our product, the product that we as a company internally

**[05:17]** product that we as a company internally

**[05:18]** product that we as a company internally use every day. And that includes the

**[05:20]** use every day. And that includes the

**[05:20]** use every day. And that includes the prompts, the tools, the context, the

**[05:22]** prompts, the tools, the context, the

**[05:22]** prompts, the tools, the context, the models, every parameter. Um, which has

**[05:25]** models, every parameter. Um, which has

**[05:25]** models, every parameter. Um, which has not only allowed us to 10x our speed of

**[05:27]** not only allowed us to 10x our speed of

**[05:27]** not only allowed us to 10x our speed of ideating, iterating and refining our

**[05:29]** ideating, iterating and refining our

**[05:29]** ideating, iterating and refining our products. But it has also widened the

**[05:31]** products. But it has also widened the

**[05:32]** products. But it has also widened the number of people who can access and

**[05:33]** number of people who can access and

**[05:33]** number of people who can access and iterate on our products themselves. from

**[05:35]** iterate on our products themselves. from

**[05:35]** iterate on our products themselves. from our CEO to our newest hire can ideate

**[05:37]** our CEO to our newest hire can ideate

**[05:37]** our CEO to our newest hire can ideate and create a new product in DIA and also

**[05:39]** and create a new product in DIA and also

**[05:40]** and create a new product in DIA and also refine an existing one all with their

**[05:42]** refine an existing one all with their

**[05:42]** refine an existing one all with their full context.

**[05:44]** full context.

**[05:44]** full context. And this holds true with all of our

**[05:46]** And this holds true with all of our

**[05:46]** And this holds true with all of our major product protocols. We have tools

**[05:48]** major product protocols. We have tools

**[05:48]** major product protocols. We have tools for optimizing our memory knowledge

**[05:49]** for optimizing our memory knowledge

**[05:49]** for optimizing our memory knowledge graph which all of us use and we have

**[05:52]** graph which all of us use and we have

**[05:52]** graph which all of us use and we have tools for creating iterating on our

**[05:54]** tools for creating iterating on our

**[05:54]** tools for creating iterating on our computer use mechanism. We actually

**[05:56]** computer use mechanism. We actually

**[05:56]** computer use mechanism. We actually tried tens of different types of

**[05:58]** tried tens of different types of

**[05:58]** tried tens of different types of computer use strategies before landing


### [06:00 - 07:00]

**[06:00]** computer use strategies before landing

**[06:00]** computer use strategies before landing on one before even building it into the

**[06:02]** on one before even building it into the

**[06:02]** on one before even building it into the product itself.

**[06:05]** product itself.

**[06:05]** product itself. And I'll say and I'll end this part with

**[06:08]** And I'll say and I'll end this part with

**[06:08]** And I'll say and I'll end this part with uh it actually is a lot of fun. People

**[06:10]** uh it actually is a lot of fun. People

**[06:10]** uh it actually is a lot of fun. People don't talk about that a lot but uh

**[06:12]** don't talk about that a lot but uh

**[06:12]** don't talk about that a lot but uh actually building these tools into our

**[06:14]** actually building these tools into our

**[06:14]** actually building these tools into our product has enabled so much creativity.

**[06:16]** product has enabled so much creativity.

**[06:16]** product has enabled so much creativity. It has enabled our PMs, our designers,

**[06:19]** It has enabled our PMs, our designers,

**[06:19]** It has enabled our PMs, our designers, uh customer service and strategy and ops

**[06:21]** uh customer service and strategy and ops

**[06:21]** uh customer service and strategy and ops to try out new ideas that are tailored

**[06:23]** to try out new ideas that are tailored

**[06:23]** to try out new ideas that are tailored to their use cases. And that ultimately

**[06:26]** to their use cases. And that ultimately

**[06:26]** to their use cases. And that ultimately is what we're trying to do.

**[06:28]** is what we're trying to do.

**[06:28]** is what we're trying to do. The next thing I want to talk about is

**[06:30]** The next thing I want to talk about is

**[06:30]** The next thing I want to talk about is how we evolve and optimize our prompts

**[06:33]** how we evolve and optimize our prompts

**[06:33]** how we evolve and optimize our prompts through a mechanism called Jeba. This

**[06:35]** through a mechanism called Jeba. This

**[06:35]** through a mechanism called Jeba. This for us is very nent but an important

**[06:38]** for us is very nent but an important

**[06:38]** for us is very nent but an important learning nevertheless.

**[06:40]** learning nevertheless.

**[06:40]** learning nevertheless. How we heel climb and refine our AI

**[06:42]** How we heel climb and refine our AI

**[06:42]** How we heel climb and refine our AI products is just as important as

**[06:43]** products is just as important as

**[06:44]** products is just as important as ideulating them in the first place. So

**[06:46]** ideulating them in the first place. So

**[06:46]** ideulating them in the first place. So we're investing in mechanisms to help

**[06:47]** we're investing in mechanisms to help

**[06:48]** we're investing in mechanisms to help with this to enable faster hill climbing

**[06:50]** with this to enable faster hill climbing

**[06:50]** with this to enable faster hill climbing and one of those being Jeepa. And this

**[06:52]** and one of those being Jeepa. And this

**[06:52]** and one of those being Jeepa. And this is based on a paper from earlier this

**[06:54]** is based on a paper from earlier this

**[06:54]** is based on a paper from earlier this year from a few smart folks.

**[06:57]** year from a few smart folks.

**[06:57]** year from a few smart folks. So the key motivation here is simple.

**[06:59]** So the key motivation here is simple.

**[06:59]** So the key motivation here is simple. It's a sample efficient way to improve a


### [07:00 - 08:00]

**[07:00]** It's a sample efficient way to improve a

**[07:00]** It's a sample efficient way to improve a complex LLM system without having to

**[07:03]** complex LLM system without having to

**[07:03]** complex LLM system without having to leverage RL or other fine-tuning

**[07:04]** leverage RL or other fine-tuning

**[07:04]** leverage RL or other fine-tuning techniques. And for us as a small

**[07:07]** techniques. And for us as a small

**[07:07]** techniques. And for us as a small company, that's hugely critical.

**[07:09]** company, that's hugely critical.

**[07:09]** company, that's hugely critical. And how it works is you're able to seed

**[07:11]** And how it works is you're able to seed

**[07:11]** And how it works is you're able to seed the system with a set of prompts, then

**[07:13]** the system with a set of prompts, then

**[07:13]** the system with a set of prompts, then execute it across a set of tasks and

**[07:15]** execute it across a set of tasks and

**[07:15]** execute it across a set of tasks and score them. Then leverage a mechanism

**[07:18]** score them. Then leverage a mechanism

**[07:18]** score them. Then leverage a mechanism called PA selection to select the best

**[07:20]** called PA selection to select the best

**[07:20]** called PA selection to select the best ones. And then leverage an LLM on top of

**[07:22]** ones. And then leverage an LLM on top of

**[07:22]** ones. And then leverage an LLM on top of that to reflect on what went well and

**[07:24]** that to reflect on what went well and

**[07:24]** that to reflect on what went well and what didn't and then generate new

**[07:26]** what didn't and then generate new

**[07:26]** what didn't and then generate new prompts and then repeat with the key

**[07:28]** prompts and then repeat with the key

**[07:28]** prompts and then repeat with the key innovations here being around that

**[07:30]** innovations here being around that

**[07:30]** innovations here being around that reflective prompt mutation technique.

**[07:32]** reflective prompt mutation technique.

**[07:32]** reflective prompt mutation technique. the selection process which allows you

**[07:34]** the selection process which allows you

**[07:34]** the selection process which allows you to explore more of the space of

**[07:35]** to explore more of the space of

**[07:35]** to explore more of the space of prompting rather than one avenue and the

**[07:38]** prompting rather than one avenue and the

**[07:38]** prompting rather than one avenue and the ability to tune text and not weights.

**[07:42]** ability to tune text and not weights.

**[07:42]** ability to tune text and not weights. And here's a modest uh example of this

**[07:45]** And here's a modest uh example of this

**[07:45]** And here's a modest uh example of this at work for us. You know, you can

**[07:47]** at work for us. You know, you can

**[07:47]** at work for us. You know, you can provide it a very simple uh a simple

**[07:49]** provide it a very simple uh a simple

**[07:50]** provide it a very simple uh a simple simple prompt and run it through JPA and

**[07:52]** simple prompt and run it through JPA and

**[07:52]** simple prompt and run it through JPA and it's able to optimize it uh along the

**[07:54]** it's able to optimize it uh along the

**[07:54]** it's able to optimize it uh along the metrics and scoring mechanisms that we

**[07:57]** metrics and scoring mechanisms that we

**[07:57]** metrics and scoring mechanisms that we uh created to refine that prompt.


### [08:00 - 09:00]

**[08:04]** And so if I take a step back and talk

**[08:04]** And so if I take a step back and talk about kind of how we build uh for

**[08:07]** about kind of how we build uh for

**[08:07]** about kind of how we build uh for certain types of features, I would buck

**[08:09]** certain types of features, I would buck

**[08:09]** certain types of features, I would buck it into a couple different phases. The

**[08:11]** it into a couple different phases. The

**[08:11]** it into a couple different phases. The first is that prototyping and ideation

**[08:13]** first is that prototyping and ideation

**[08:13]** first is that prototyping and ideation phase where we have widened the breadth

**[08:15]** phase where we have widened the breadth

**[08:16]** phase where we have widened the breadth of number of ideas at the top of the

**[08:17]** of number of ideas at the top of the

**[08:17]** of number of ideas at the top of the funnel um and lower the threshold on who

**[08:19]** funnel um and lower the threshold on who

**[08:20]** funnel um and lower the threshold on who can build them and how. And so we try

**[08:22]** can build them and how. And so we try

**[08:22]** can build them and how. And so we try out a bunch of ideas every week, every

**[08:23]** out a bunch of ideas every week, every

**[08:23]** out a bunch of ideas every week, every day from all types of people and we dog

**[08:25]** day from all types of people and we dog

**[08:25]** day from all types of people and we dog food those. And if we feel like there's

**[08:27]** food those. And if we feel like there's

**[08:28]** food those. And if we feel like there's actually real utility there, it's

**[08:29]** actually real utility there, it's

**[08:29]** actually real utility there, it's solving a real problem for us and there

**[08:32]** solving a real problem for us and there

**[08:32]** solving a real problem for us and there is a path towards actually hitting the

**[08:34]** is a path towards actually hitting the

**[08:34]** is a path towards actually hitting the quality threshold that we believe we

**[08:35]** quality threshold that we believe we

**[08:35]** quality threshold that we believe we need to hit, then we'll move on to this

**[08:37]** need to hit, then we'll move on to this

**[08:37]** need to hit, then we'll move on to this next phase where we collect and refine

**[08:39]** next phase where we collect and refine

**[08:39]** next phase where we collect and refine eval to clarify product requirements and

**[08:42]** eval to clarify product requirements and

**[08:42]** eval to clarify product requirements and then hill climb through code through

**[08:44]** then hill climb through code through

**[08:44]** then hill climb through code through prompting and automated techniques like

**[08:46]** prompting and automated techniques like

**[08:46]** prompting and automated techniques like Jeba and then dog food as we always do

**[08:48]** Jeba and then dog food as we always do

**[08:48]** Jeba and then dog food as we always do internally and then chip

**[08:51]** internally and then chip

**[08:51]** internally and then chip and I do want to kind of double down on

**[08:54]** and I do want to kind of double down on

**[08:54]** and I do want to kind of double down on these phases. The ideation phase is

**[08:57]** these phases. The ideation phase is

**[08:57]** these phases. The ideation phase is extremely important just as much as that

**[08:59]** extremely important just as much as that

**[08:59]** extremely important just as much as that refinement phase.


### [09:00 - 10:00]

**[09:05]** And our goal is to enable faster

**[09:05]** And our goal is to enable faster ideation and a more efficient path to

**[09:07]** ideation and a more efficient path to

**[09:07]** ideation and a more efficient path to shipping. Because with all these AI

**[09:09]** shipping. Because with all these AI

**[09:09]** shipping. Because with all these AI advancements every week, new

**[09:11]** advancements every week, new

**[09:11]** advancements every week, new possibilities are unlocked in DIA. And

**[09:13]** possibilities are unlocked in DIA. And

**[09:13]** possibilities are unlocked in DIA. And it's up to us as a browser, as a product

**[09:16]** it's up to us as a browser, as a product

**[09:16]** it's up to us as a browser, as a product to get as many at bats with these new

**[09:18]** to get as many at bats with these new

**[09:18]** to get as many at bats with these new ideas and try out as many of them and

**[09:20]** ideas and try out as many of them and

**[09:20]** ideas and try out as many of them and explore as many of them as possible. At

**[09:22]** explore as many of them as possible. At

**[09:22]** explore as many of them as possible. At the same time though not underestimating

**[09:24]** the same time though not underestimating

**[09:24]** the same time though not underestimating the path it takes to ship some of these

**[09:26]** the path it takes to ship some of these

**[09:26]** the path it takes to ship some of these ideas to productions as a high quality

**[09:28]** ideas to productions as a high quality

**[09:28]** ideas to productions as a high quality experience.

**[09:34]** Next uh I want to talk about treating

**[09:34]** Next uh I want to talk about treating model behavior as a craft and

**[09:36]** model behavior as a craft and

**[09:36]** model behavior as a craft and discipline.

**[09:37]** discipline.

**[09:37]** discipline. So what is model behavior to us? It's

**[09:40]** So what is model behavior to us? It's

**[09:40]** So what is model behavior to us? It's the function that defines evaluates and

**[09:42]** the function that defines evaluates and

**[09:42]** the function that defines evaluates and ships the desired behavior models. It's

**[09:45]** ships the desired behavior models. It's

**[09:45]** ships the desired behavior models. It's turning principles into product

**[09:46]** turning principles into product

**[09:46]** turning principles into product requirements, prompts, and evals, and

**[09:49]** requirements, prompts, and evals, and

**[09:49]** requirements, prompts, and evals, and ultimately shaping the behavior and the

**[09:51]** ultimately shaping the behavior and the

**[09:51]** ultimately shaping the behavior and the personality of our LLM products, and

**[09:53]** personality of our LLM products, and

**[09:53]** personality of our LLM products, and ultimately for us, our DIA assistant.

**[09:57]** ultimately for us, our DIA assistant.

**[09:57]** ultimately for us, our DIA assistant. So, I'd buck it into a few different

**[09:58]** So, I'd buck it into a few different

**[09:58]** So, I'd buck it into a few different areas. First, it's that behavior design,


### [10:00 - 11:00]

**[10:00]** areas. First, it's that behavior design,

**[10:00]** areas. First, it's that behavior design, defining the product experience we

**[10:02]** defining the product experience we

**[10:02]** defining the product experience we actually want, the style, the tone, the

**[10:04]** actually want, the style, the tone, the

**[10:04]** actually want, the style, the tone, the shape of responses in some cases. Then,

**[10:07]** shape of responses in some cases. Then,

**[10:07]** shape of responses in some cases. Then, it's collecting that data for

**[10:08]** it's collecting that data for

**[10:08]** it's collecting that data for measurement and training, clarifying

**[10:10]** measurement and training, clarifying

**[10:10]** measurement and training, clarifying those product requirements through eval.

**[10:13]** those product requirements through eval.

**[10:13]** those product requirements through eval. And last but not least, it's the model

**[10:14]** And last but not least, it's the model

**[10:14]** And last but not least, it's the model steering. It's the building of the

**[10:15]** steering. It's the building of the

**[10:16]** steering. It's the building of the product itself. It's the prompting. It's

**[10:18]** product itself. It's the prompting. It's

**[10:18]** product itself. It's the prompting. It's the model selection. It's defining the

**[10:19]** the model selection. It's defining the

**[10:19]** the model selection. It's defining the what's in the context window, the

**[10:21]** what's in the context window, the

**[10:21]** what's in the context window, the parameters, etc. Um, and so much more.

**[10:25]** parameters, etc. Um, and so much more.

**[10:25]** parameters, etc. Um, and so much more. And to us, that that process is

**[10:27]** And to us, that that process is

**[10:28]** And to us, that that process is iterative, very iterative. We build,

**[10:31]** iterative, very iterative. We build,

**[10:31]** iterative, very iterative. We build, refine, we create evals, and then we

**[10:33]** refine, we create evals, and then we

**[10:33]** refine, we create evals, and then we ship, and then we collect more feedback

**[10:36]** ship, and then we collect more feedback

**[10:36]** ship, and then we collect more feedback and feed that into our iterative

**[10:38]** and feed that into our iterative

**[10:38]** and feed that into our iterative building process. That could be internal

**[10:40]** building process. That could be internal

**[10:40]** building process. That could be internal feedback, and that could be also uh

**[10:41]** feedback, and that could be also uh

**[10:41]** feedback, and that could be also uh external feedback.

**[10:43]** external feedback.

**[10:43]** external feedback. And so if I move on for a second, one

**[10:46]** And so if I move on for a second, one

**[10:46]** And so if I move on for a second, one analogy we've thought about uh is for

**[10:48]** analogy we've thought about uh is for

**[10:48]** analogy we've thought about uh is for model behaviors that to product design

**[10:51]** model behaviors that to product design

**[10:51]** model behaviors that to product design through the evolution of the internet.

**[10:53]** through the evolution of the internet.

**[10:53]** through the evolution of the internet. At first websites were functional. They

**[10:55]** At first websites were functional. They

**[10:55]** At first websites were functional. They got the job done. But over time that

**[10:58]** got the job done. But over time that

**[10:58]** got the job done. But over time that evolved as we tried to achieve more on


### [11:00 - 12:00]

**[11:00]** evolved as we tried to achieve more on

**[11:00]** evolved as we tried to achieve more on the internet and technology advanced. Uh

**[11:03]** the internet and technology advanced. Uh

**[11:03]** the internet and technology advanced. Uh product design and the craft of the

**[11:05]** product design and the craft of the

**[11:05]** product design and the craft of the internet itself grew as well as well as

**[11:07]** internet itself grew as well as well as

**[11:07]** internet itself grew as well as well as the complexity.

**[11:09]** the complexity.

**[11:09]** the complexity. And so what might that be for model

**[11:11]** And so what might that be for model

**[11:11]** And so what might that be for model behavior? Well, at first it was

**[11:13]** behavior? Well, at first it was

**[11:13]** behavior? Well, at first it was functional. We had prompts. We had

**[11:15]** functional. We had prompts. We had

**[11:15]** functional. We had prompts. We had evals. We had instructions in and output

**[11:17]** evals. We had instructions in and output

**[11:17]** evals. We had instructions in and output out. Now we frame it through agent

**[11:19]** out. Now we frame it through agent

**[11:19]** out. Now we frame it through agent behaviors. It's goal- directed

**[11:21]** behaviors. It's goal- directed

**[11:21]** behaviors. It's goal- directed reasoning, the shaping of autonomous

**[11:23]** reasoning, the shaping of autonomous

**[11:23]** reasoning, the shaping of autonomous tasks, selfcorrection and learning, and

**[11:25]** tasks, selfcorrection and learning, and

**[11:26]** tasks, selfcorrection and learning, and even shaping the personality of the LM

**[11:28]** even shaping the personality of the LM

**[11:28]** even shaping the personality of the LM models themselves.

**[11:30]** models themselves.

**[11:30]** models themselves. And so, what might the future hold? I'm

**[11:32]** And so, what might the future hold? I'm

**[11:32]** And so, what might the future hold? I'm excited to see. But what we believe is

**[11:35]** excited to see. But what we believe is

**[11:35]** excited to see. But what we believe is that we are in the early days of

**[11:36]** that we are in the early days of

**[11:36]** that we are in the early days of building AI products and model behavior

**[11:39]** building AI products and model behavior

**[11:39]** building AI products and model behavior will continue to evolve and into a

**[11:41]** will continue to evolve and into a

**[11:41]** will continue to evolve and into a specialized and prevalent function of

**[11:43]** specialized and prevalent function of

**[11:43]** specialized and prevalent function of its own even at product companies.

**[11:46]** its own even at product companies.

**[11:46]** its own even at product companies. And the last thing I'll leave you with

**[11:47]** And the last thing I'll leave you with

**[11:47]** And the last thing I'll leave you with here is that the best people for it

**[11:49]** here is that the best people for it

**[11:50]** here is that the best people for it might just surprise you. One of my

**[11:52]** might just surprise you. One of my

**[11:52]** might just surprise you. One of my favorite stories about building DIA

**[11:54]** favorite stories about building DIA

**[11:54]** favorite stories about building DIA these last couple years has been uh the

**[11:56]** these last couple years has been uh the

**[11:56]** these last couple years has been uh the formation of actually this model

**[11:58]** formation of actually this model

**[11:58]** formation of actually this model behavior team. As I mentioned earlier,


### [12:00 - 13:00]

**[12:00]** behavior team. As I mentioned earlier,

**[12:00]** behavior team. As I mentioned earlier, uh engineers were writing the prompts at

**[12:01]** uh engineers were writing the prompts at

**[12:01]** uh engineers were writing the prompts at first and then we built these prompt

**[12:03]** first and then we built these prompt

**[12:03]** first and then we built these prompt tools to enable more people at the

**[12:04]** tools to enable more people at the

**[12:04]** tools to enable more people at the company to actually prompt and iterate.

**[12:07]** company to actually prompt and iterate.

**[12:07]** company to actually prompt and iterate. And there was a person on our team on

**[12:08]** And there was a person on our team on

**[12:08]** And there was a person on our team on the strategy and ops team and he

**[12:10]** the strategy and ops team and he

**[12:10]** the strategy and ops team and he actually leveraged these prompt tools

**[12:12]** actually leveraged these prompt tools

**[12:12]** actually leveraged these prompt tools one weekend to rewrite all our prompts.

**[12:14]** one weekend to rewrite all our prompts.

**[12:14]** one weekend to rewrite all our prompts. And he came in on a Monday morning and

**[12:16]** And he came in on a Monday morning and

**[12:16]** And he came in on a Monday morning and dropped a loom video sharing what he

**[12:19]** dropped a loom video sharing what he

**[12:19]** dropped a loom video sharing what he did, how he did it, and why. and a set

**[12:21]** did, how he did it, and why. and a set

**[12:21]** did, how he did it, and why. and a set of prompts and those prompts alone

**[12:23]** of prompts and those prompts alone

**[12:23]** of prompts and those prompts alone unlocked a new level of capability and

**[12:26]** unlocked a new level of capability and

**[12:26]** unlocked a new level of capability and quality and experience in our product

**[12:28]** quality and experience in our product

**[12:28]** quality and experience in our product and consequentially uh it was the

**[12:30]** and consequentially uh it was the

**[12:30]** and consequentially uh it was the formation of our model behavior team and

**[12:33]** formation of our model behavior team and

**[12:33]** formation of our model behavior team and so one thing I'd emphasize to you all is

**[12:36]** so one thing I'd emphasize to you all is

**[12:36]** so one thing I'd emphasize to you all is to think about who are those people at

**[12:37]** to think about who are those people at

**[12:37]** to think about who are those people at the company agnostic of their role who

**[12:39]** the company agnostic of their role who

**[12:39]** the company agnostic of their role who can help shape your product and help

**[12:41]** can help shape your product and help

**[12:41]** can help shape your product and help shape and steer the model itself it

**[12:43]** shape and steer the model itself it

**[12:43]** shape and steer the model itself it might not be an engineer or it might be

**[12:45]** might not be an engineer or it might be

**[12:45]** might not be an engineer or it might be it could also be someone on the strategy

**[12:47]** it could also be someone on the strategy

**[12:47]** it could also be someone on the strategy and ops team

**[12:50]** and ops team

**[12:50]** and ops team next I want to talk about AI security as

**[12:52]** next I want to talk about AI security as

**[12:52]** next I want to talk about AI security as an emergent property of product

**[12:53]** an emergent property of product

**[12:54]** an emergent property of product building. And today I'm going to focus

**[12:55]** building. And today I'm going to focus

**[12:55]** building. And today I'm going to focus specifically on prompt injections.

**[12:58]** specifically on prompt injections.

**[12:58]** specifically on prompt injections. So what is a prompt injection? Well,


### [13:00 - 14:00]

**[13:01]** So what is a prompt injection? Well,

**[13:01]** So what is a prompt injection? Well, it's a prompt attack in which a third

**[13:03]** it's a prompt attack in which a third

**[13:03]** it's a prompt attack in which a third party can override the instructions of

**[13:04]** party can override the instructions of

**[13:04]** party can override the instructions of an LLM to cause harm. That might be data

**[13:07]** an LLM to cause harm. That might be data

**[13:07]** an LLM to cause harm. That might be data exfiltration, the execution of malicious

**[13:09]** exfiltration, the execution of malicious

**[13:09]** exfiltration, the execution of malicious commands, or ignoring safety rules.

**[13:14]** commands, or ignoring safety rules.

**[13:14]** commands, or ignoring safety rules. And so here's an example in which you

**[13:16]** And so here's an example in which you

**[13:16]** And so here's an example in which you give uh the context of a website to an

**[13:19]** give uh the context of a website to an

**[13:19]** give uh the context of a website to an LLM and instruct it to summarize it.

**[13:21]** LLM and instruct it to summarize it.

**[13:22]** LLM and instruct it to summarize it. Little did you know that there was a

**[13:23]** Little did you know that there was a

**[13:23]** Little did you know that there was a prompt injection hidden in that

**[13:24]** prompt injection hidden in that

**[13:24]** prompt injection hidden in that website's uh HTML.

**[13:27]** website's uh HTML.

**[13:27]** website's uh HTML. So instead of actually summarizing the

**[13:29]** So instead of actually summarizing the

**[13:29]** So instead of actually summarizing the web page, the LM actually gets directed

**[13:31]** web page, the LM actually gets directed

**[13:31]** web page, the LM actually gets directed to open a new website, extracting your

**[13:33]** to open a new website, extracting your

**[13:33]** to open a new website, extracting your personal information and embedding it as

**[13:34]** personal information and embedding it as

**[13:34]** personal information and embedding it as get parameters in the website's URL,

**[13:37]** get parameters in the website's URL,

**[13:37]** get parameters in the website's URL, effectively exfiltrating that data.

**[13:40]** effectively exfiltrating that data.

**[13:40]** effectively exfiltrating that data. So, as a browser, prompt injections are

**[13:43]** So, as a browser, prompt injections are

**[13:43]** So, as a browser, prompt injections are extremely crucial for us to prevent.

**[13:45]** extremely crucial for us to prevent.

**[13:46]** extremely crucial for us to prevent. They're critical to prevent

**[13:48]** They're critical to prevent

**[13:48]** They're critical to prevent because browsers sit at the middle of

**[13:51]** because browsers sit at the middle of

**[13:51]** because browsers sit at the middle of what we can call a lethal trifecta.

**[13:54]** what we can call a lethal trifecta.

**[13:54]** what we can call a lethal trifecta. It has access to your private data. It

**[13:56]** It has access to your private data. It

**[13:56]** It has access to your private data. It has exposure to untrusted content and it

**[13:59]** has exposure to untrusted content and it

**[13:59]** has exposure to untrusted content and it has the ability to externally


### [14:00 - 15:00]

**[14:01]** has the ability to externally

**[14:01]** has the ability to externally communicate and for us that means

**[14:03]** communicate and for us that means

**[14:03]** communicate and for us that means opening websites, sending emails,

**[14:05]** opening websites, sending emails,

**[14:05]** opening websites, sending emails, scheduling events, etc. So, how do we

**[14:08]** scheduling events, etc. So, how do we

**[14:08]** scheduling events, etc. So, how do we prevent this? Well, there's some

**[14:11]** prevent this? Well, there's some

**[14:11]** prevent this? Well, there's some technical strategies we can try. First

**[14:13]** technical strategies we can try. First

**[14:13]** technical strategies we can try. First is wrapping that untrusted context in

**[14:15]** is wrapping that untrusted context in

**[14:15]** is wrapping that untrusted context in tags. You can tell the LM, listen to

**[14:17]** tags. You can tell the LM, listen to

**[14:17]** tags. You can tell the LM, listen to these instructions around these tags and

**[14:19]** these instructions around these tags and

**[14:19]** these instructions around these tags and don't listen to the content around these

**[14:20]** don't listen to the content around these

**[14:20]** don't listen to the content around these tags. But this is easily escapable and

**[14:24]** tags. But this is easily escapable and

**[14:24]** tags. But this is easily escapable and quite trivy, an attacker could still uh

**[14:27]** quite trivy, an attacker could still uh

**[14:27]** quite trivy, an attacker could still uh leverage a prompt injection on your

**[14:29]** leverage a prompt injection on your

**[14:29]** leverage a prompt injection on your browser.

**[14:30]** browser.

**[14:30]** browser. Well, another solution we could try is

**[14:32]** Well, another solution we could try is

**[14:32]** Well, another solution we could try is separating that data and that

**[14:34]** separating that data and that

**[14:34]** separating that data and that instructions. We can assign uh the

**[14:38]** instructions. We can assign uh the

**[14:38]** instructions. We can assign uh the operating instructions to a system role

**[14:40]** operating instructions to a system role

**[14:40]** operating instructions to a system role and we can assign a user role for the

**[14:42]** and we can assign a user role for the

**[14:42]** and we can assign a user role for the content of the third party and even

**[14:44]** content of the third party and even

**[14:44]** content of the third party and even layer on randomly generated tags to wrap

**[14:46]** layer on randomly generated tags to wrap

**[14:46]** layer on randomly generated tags to wrap that user content to be extra sure that

**[14:49]** that user content to be extra sure that

**[14:49]** that user content to be extra sure that the LM listens to the instructions and

**[14:51]** the LM listens to the instructions and

**[14:51]** the LM listens to the instructions and not the content. And while this can

**[14:53]** not the content. And while this can

**[14:53]** not the content. And while this can help, there are no guarantees and prompt

**[14:56]** help, there are no guarantees and prompt

**[14:56]** help, there are no guarantees and prompt injections will still happen.


### [15:00 - 16:00]

**[15:01]** injections will still happen.

**[15:01]** injections will still happen. So what do we do? Well, it's on us to

**[15:03]** So what do we do? Well, it's on us to

**[15:03]** So what do we do? Well, it's on us to design a product with that in mind. We

**[15:06]** design a product with that in mind. We

**[15:06]** design a product with that in mind. We have to blend technology approaches and

**[15:08]** have to blend technology approaches and

**[15:08]** have to blend technology approaches and user experience and design into a

**[15:10]** user experience and design into a

**[15:10]** user experience and design into a cohesive story that actually builds them

**[15:13]** cohesive story that actually builds them

**[15:13]** cohesive story that actually builds them from the ground up and solves it

**[15:14]** from the ground up and solves it

**[15:14]** from the ground up and solves it together.

**[15:16]** together.

**[15:16]** together. So, what that might what that excuse me

**[15:18]** So, what that might what that excuse me

**[15:18]** So, what that might what that excuse me what might that be for a feature in DIA?

**[15:21]** what might that be for a feature in DIA?

**[15:21]** what might that be for a feature in DIA? Well, let's take the autofill tool in

**[15:23]** Well, let's take the autofill tool in

**[15:23]** Well, let's take the autofill tool in DIA. The autofill tool allows you to

**[15:25]** DIA. The autofill tool allows you to

**[15:25]** DIA. The autofill tool allows you to leverage an LLM with context, memory,

**[15:28]** leverage an LLM with context, memory,

**[15:28]** leverage an LLM with context, memory, and your details to fill forms on the

**[15:30]** and your details to fill forms on the

**[15:30]** and your details to fill forms on the internet. It's extremely powerful, but

**[15:33]** internet. It's extremely powerful, but

**[15:33]** internet. It's extremely powerful, but as you can imagine, it has some

**[15:35]** as you can imagine, it has some

**[15:35]** as you can imagine, it has some vulnerabilities. A prompt injection here

**[15:37]** vulnerabilities. A prompt injection here

**[15:37]** vulnerabilities. A prompt injection here could extract your data and put it on a

**[15:40]** could extract your data and put it on a

**[15:40]** could extract your data and put it on a form, and once it's on that form, it's

**[15:42]** form, and once it's on that form, it's

**[15:42]** form, and once it's on that form, it's out of your hands. So, we try to build

**[15:44]** out of your hands. So, we try to build

**[15:44]** out of your hands. So, we try to build with that in mind.

**[15:47]** with that in mind.

**[15:47]** with that in mind. In this case, before the form is written

**[15:48]** In this case, before the form is written

**[15:48]** In this case, before the form is written to, we actually let the user read and

**[15:50]** to, we actually let the user read and

**[15:50]** to, we actually let the user read and confirm that data in plain text. This

**[15:53]** confirm that data in plain text. This

**[15:53]** confirm that data in plain text. This doesn't prevent a prompt injection, but

**[15:55]** doesn't prevent a prompt injection, but

**[15:56]** doesn't prevent a prompt injection, but it gives the user control, awareness,

**[15:57]** it gives the user control, awareness,

**[15:57]** it gives the user control, awareness, and trust in what is happening. And this


### [16:00 - 17:00]

**[16:00]** and trust in what is happening. And this

**[16:00]** and trust in what is happening. And this is a framing we carry throughout our

**[16:02]** is a framing we carry throughout our

**[16:02]** is a framing we carry throughout our product and how we build every single

**[16:04]** product and how we build every single

**[16:04]** product and how we build every single feature. So here are some examples.

**[16:06]** feature. So here are some examples.

**[16:06]** feature. So here are some examples. Scheduling events in DIA, we have a

**[16:08]** Scheduling events in DIA, we have a

**[16:08]** Scheduling events in DIA, we have a similar confirmation step. Writing

**[16:11]** similar confirmation step. Writing

**[16:11]** similar confirmation step. Writing emails India, we also have a similar

**[16:14]** emails India, we also have a similar

**[16:14]** emails India, we also have a similar confirmation step.

**[16:19]** So I've talked about three different

**[16:19]** So I've talked about three different things here today. First is optimizing

**[16:21]** things here today. First is optimizing

**[16:21]** things here today. First is optimizing your tools and process for fast

**[16:23]** your tools and process for fast

**[16:23]** your tools and process for fast iteration. Second, treating model

**[16:25]** iteration. Second, treating model

**[16:25]** iteration. Second, treating model behavior as a craft and discipline. And

**[16:28]** behavior as a craft and discipline. And

**[16:28]** behavior as a craft and discipline. And third, AI security as an emergent

**[16:30]** third, AI security as an emergent

**[16:30]** third, AI security as an emergent property of building products.

**[16:33]** property of building products.

**[16:34]** property of building products. But uh the last thing I want to leave

**[16:36]** But uh the last thing I want to leave

**[16:36]** But uh the last thing I want to leave you with, when we started on this

**[16:38]** you with, when we started on this

**[16:38]** you with, when we started on this journey to building DIA, we recognized a

**[16:40]** journey to building DIA, we recognized a

**[16:40]** journey to building DIA, we recognized a technology shift and we sought to evolve

**[16:43]** technology shift and we sought to evolve

**[16:43]** technology shift and we sought to evolve our product of Arc. We initially came at

**[16:45]** our product of Arc. We initially came at

**[16:45]** our product of Arc. We initially came at it from a hey, how can we leverage AI to

**[16:48]** it from a hey, how can we leverage AI to

**[16:48]** it from a hey, how can we leverage AI to make ARC better, make the browser

**[16:50]** make ARC better, make the browser

**[16:50]** make ARC better, make the browser better? But what we quickly learned and

**[16:53]** better? But what we quickly learned and

**[16:53]** better? But what we quickly learned and adapted to was that it wasn't just a

**[16:55]** adapted to was that it wasn't just a

**[16:55]** adapted to was that it wasn't just a product evolution. It was a company one

**[16:58]** product evolution. It was a company one

**[16:58]** product evolution. It was a company one and today I shared a glimpse of that.


### [17:00 - 18:00]

**[17:00]** and today I shared a glimpse of that.

**[17:00]** and today I shared a glimpse of that. How we build and how it's changed a team

**[17:03]** How we build and how it's changed a team

**[17:03]** How we build and how it's changed a team we've literally created around this and

**[17:05]** we've literally created around this and

**[17:05]** we've literally created around this and how we think about security for AI

**[17:06]** how we think about security for AI

**[17:06]** how we think about security for AI products. But really it's so much more.

**[17:08]** products. But really it's so much more.

**[17:08]** products. But really it's so much more. It goes beyond that. It's how we train

**[17:10]** It goes beyond that. It's how we train

**[17:10]** It goes beyond that. It's how we train everyone here. It's how we hire. It's

**[17:12]** everyone here. It's how we hire. It's

**[17:12]** everyone here. It's how we hire. It's how we communicate. It's how we

**[17:13]** how we communicate. It's how we

**[17:13]** how we communicate. It's how we collaborate and so much more. And if

**[17:16]** collaborate and so much more. And if

**[17:16]** collaborate and so much more. And if there's one thing I'll leave you all

**[17:17]** there's one thing I'll leave you all

**[17:17]** there's one thing I'll leave you all with, if there's one thing we've learned

**[17:19]** with, if there's one thing we've learned

**[17:19]** with, if there's one thing we've learned over the last couple years, it's that

**[17:21]** over the last couple years, it's that

**[17:21]** over the last couple years, it's that when when you recognize that technology

**[17:23]** when when you recognize that technology

**[17:23]** when when you recognize that technology shift, you have to embrace it. And you

**[17:25]** shift, you have to embrace it. And you

**[17:25]** shift, you have to embrace it. And you have to embrace it with conviction.

**[17:28]** have to embrace it with conviction.

**[17:28]** have to embrace it with conviction. Thank you.

**[17:30]** Thank you.

**[17:30]** Thank you. [applause and music]


