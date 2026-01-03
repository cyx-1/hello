# How BlackRock Builds Custom Knowledge Apps at Scale — Vaibhav Page & Infant Vasanth, BlackRock

**Video URL:** https://www.youtube.com/watch?v=08mH36_NVos

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Hi everyone, thank you for having us.

**[00:16]** Hi everyone, thank you for having us. I'm Infant, director of engineering at

**[00:18]** I'm Infant, director of engineering at

**[00:18]** I'm Infant, director of engineering at Black Rockck. This is my colleague

**[00:19]** Black Rockck. This is my colleague

**[00:20]** Black Rockck. This is my colleague Wyber, principal engineer and we both

**[00:21]** Wyber, principal engineer and we both

**[00:22]** Wyber, principal engineer and we both work for the data teams at Black Rockck.

**[00:23]** work for the data teams at Black Rockck.

**[00:23]** work for the data teams at Black Rockck. And today we're going to talk about how

**[00:25]** And today we're going to talk about how

**[00:25]** And today we're going to talk about how we can scale building custom

**[00:27]** we can scale building custom

**[00:27]** we can scale building custom applications in Black Rockck.

**[00:28]** applications in Black Rockck.

**[00:28]** applications in Black Rockck. Specifically, we're talking about like

**[00:29]** Specifically, we're talking about like

**[00:29]** Specifically, we're talking about like AI applications and knowledge apps at

**[00:32]** AI applications and knowledge apps at

**[00:32]** AI applications and knowledge apps at Black Rockck, right? So, just to level

**[00:33]** Black Rockck, right? So, just to level

**[00:34]** Black Rockck, right? So, just to level set before I get into the uh details.

**[00:35]** set before I get into the uh details.

**[00:36]** set before I get into the uh details. So, Black Rockck is an asset management

**[00:37]** So, Black Rockck is an asset management

**[00:37]** So, Black Rockck is an asset management firm, the world's largest asset manager.

**[00:39]** firm, the world's largest asset manager.

**[00:39]** firm, the world's largest asset manager. What we do is our portfolio managers,

**[00:41]** What we do is our portfolio managers,

**[00:41]** What we do is our portfolio managers, analysts get a torrent of information on

**[00:43]** analysts get a torrent of information on

**[00:43]** analysts get a torrent of information on a daily basis. They synthesize this

**[00:45]** a daily basis. They synthesize this

**[00:45]** a daily basis. They synthesize this information, they develop an investment

**[00:47]** information, they develop an investment

**[00:47]** information, they develop an investment strategy and then they rebalance your

**[00:49]** strategy and then they rebalance your

**[00:49]** strategy and then they rebalance your portfolios uh which ultimately results

**[00:51]** portfolios uh which ultimately results

**[00:51]** portfolios uh which ultimately results in a particular trade. Now the

**[00:53]** in a particular trade. Now the

**[00:53]** in a particular trade. Now the investment operations teams you can

**[00:55]** investment operations teams you can

**[00:55]** investment operations teams you can think of that as the teams that are the

**[00:58]** think of that as the teams that are the

**[00:58]** think of that as the teams that are the backbone or the engine that makes sure


### [01:00 - 02:00]

**[01:00]** backbone or the engine that makes sure

**[01:00]** backbone or the engine that makes sure that all of the activities that the

**[01:02]** that all of the activities that the

**[01:02]** that all of the activities that the investment managers actually perform on

**[01:04]** investment managers actually perform on

**[01:04]** investment managers actually perform on a day-to-day basis like runs smoothly

**[01:06]** a day-to-day basis like runs smoothly

**[01:06]** a day-to-day basis like runs smoothly right so these teams are kind of

**[01:07]** right so these teams are kind of

**[01:08]** right so these teams are kind of responsible for like acquiring the data

**[01:10]** responsible for like acquiring the data

**[01:10]** responsible for like acquiring the data that you kind of need right uh to

**[01:12]** that you kind of need right uh to

**[01:12]** that you kind of need right uh to actually executing a trade running

**[01:13]** actually executing a trade running

**[01:13]** actually executing a trade running through compliance all the way to like

**[01:15]** through compliance all the way to like

**[01:15]** through compliance all the way to like all of the post- trading activities

**[01:17]** all of the post- trading activities

**[01:17]** all of the post- trading activities right so all of these teams actually

**[01:19]** right so all of these teams actually

**[01:19]** right so all of these teams actually have to build these internal tools that

**[01:21]** have to build these internal tools that

**[01:21]** have to build these internal tools that are actually fairly complex for each of

**[01:23]** are actually fairly complex for each of

**[01:23]** are actually fairly complex for each of their domains. Right? So building apps

**[01:26]** their domains. Right? So building apps

**[01:26]** their domains. Right? So building apps and pushing out these apps uh relatively

**[01:28]** and pushing out these apps uh relatively

**[01:28]** and pushing out these apps uh relatively quickly is like of utmost important to

**[01:30]** quickly is like of utmost important to

**[01:30]** quickly is like of utmost important to us. Right? So if you move on to the next

**[01:32]** us. Right? So if you move on to the next

**[01:32]** us. Right? So if you move on to the next slide again if you actually classify

**[01:34]** slide again if you actually classify

**[01:34]** slide again if you actually classify what kind of apps we are talking about

**[01:36]** what kind of apps we are talking about

**[01:36]** what kind of apps we are talking about what you'll see is that it kind of falls

**[01:37]** what you'll see is that it kind of falls

**[01:37]** what you'll see is that it kind of falls into like four different buckets right?

**[01:39]** into like four different buckets right?

**[01:39]** into like four different buckets right? One is everything to do with document

**[01:41]** One is everything to do with document

**[01:41]** One is everything to do with document extraction. So I have an app I kind of

**[01:43]** extraction. So I have an app I kind of

**[01:43]** extraction. So I have an app I kind of want to like extract entities out of it

**[01:45]** want to like extract entities out of it

**[01:45]** want to like extract entities out of it in that bucket. Second has to do

**[01:47]** in that bucket. Second has to do

**[01:47]** in that bucket. Second has to do everything with like hey I kind of want

**[01:48]** everything with like hey I kind of want

**[01:48]** everything with like hey I kind of want to define a complex uh workflow or an

**[01:50]** to define a complex uh workflow or an

**[01:50]** to define a complex uh workflow or an automation. So I could have a case where

**[01:53]** automation. So I could have a case where

**[01:53]** automation. So I could have a case where I kind of want to run through X number

**[01:54]** I kind of want to run through X number

**[01:54]** I kind of want to run through X number of steps and then integrate to my

**[01:56]** of steps and then integrate to my

**[01:56]** of steps and then integrate to my downstream systems and then you have the

**[01:59]** downstream systems and then you have the

**[01:59]** downstream systems and then you have the normal like Q&A type systems that you


### [02:00 - 03:00]

**[02:01]** normal like Q&A type systems that you

**[02:01]** normal like Q&A type systems that you look at like this is your chat

**[02:02]** look at like this is your chat

**[02:02]** look at like this is your chat interfaces and finally like the the

**[02:04]** interfaces and finally like the the

**[02:04]** interfaces and finally like the the agentic systems right so in each of

**[02:06]** agentic systems right so in each of

**[02:06]** agentic systems right so in each of these domains what we see is u we have

**[02:10]** these domains what we see is u we have

**[02:10]** these domains what we see is u we have this like big opportunity to leverage

**[02:12]** this like big opportunity to leverage

**[02:12]** this like big opportunity to leverage your models and LLMs to either augment

**[02:15]** your models and LLMs to either augment

**[02:15]** your models and LLMs to either augment our existing systems uh or like kind of

**[02:17]** our existing systems uh or like kind of

**[02:17]** our existing systems uh or like kind of like supercharge those right so that

**[02:19]** like supercharge those right so that

**[02:19]** like supercharge those right so that that is like the domain we are speaking

**[02:21]** that is like the domain we are speaking

**[02:21]** that is like the domain we are speaking about. So I'll move quickly to one

**[02:23]** about. So I'll move quickly to one

**[02:23]** about. So I'll move quickly to one particular use case. So this this is a

**[02:25]** particular use case. So this this is a

**[02:25]** particular use case. So this this is a use case that came to us like about like

**[02:27]** use case that came to us like about like

**[02:27]** use case that came to us like about like 3 to 4 months back right and we have a

**[02:30]** 3 to 4 months back right and we have a

**[02:30]** 3 to 4 months back right and we have a team within the investment operations

**[02:32]** team within the investment operations

**[02:32]** team within the investment operations space it's known as a new issue

**[02:34]** space it's known as a new issue

**[02:34]** space it's known as a new issue operations team right so this team is

**[02:37]** operations team right so this team is

**[02:37]** operations team right so this team is kind of responsible for setting up

**[02:38]** kind of responsible for setting up

**[02:38]** kind of responsible for setting up securities uh whenever there is like a

**[02:40]** securities uh whenever there is like a

**[02:40]** securities uh whenever there is like a market event right so a company goes IPO

**[02:43]** market event right so a company goes IPO

**[02:43]** market event right so a company goes IPO or like there is like a stock split for

**[02:45]** or like there is like a stock split for

**[02:45]** or like there is like a stock split for a particular organization right the team

**[02:47]** a particular organization right the team

**[02:47]** a particular organization right the team actually has to take the security and

**[02:49]** actually has to take the security and

**[02:49]** actually has to take the security and they have to set it up in our internal

**[02:50]** they have to set it up in our internal

**[02:50]** they have to set it up in our internal systems before our portfolio managers or

**[02:53]** systems before our portfolio managers or

**[02:53]** systems before our portfolio managers or traders can action upon it, right? So,

**[02:55]** traders can action upon it, right? So,

**[02:55]** traders can action upon it, right? So, we kind of have to build this tool for

**[02:58]** we kind of have to build this tool for

**[02:58]** we kind of have to build this tool for the investment operations team, right?


### [03:00 - 04:00]

**[03:00]** the investment operations team, right?

**[03:00]** the investment operations team, right? To set up a particular security. This is

**[03:02]** To set up a particular security. This is

**[03:02]** To set up a particular security. This is like actually honestly this is like a

**[03:03]** like actually honestly this is like a

**[03:03]** like actually honestly this is like a super simplified version of what

**[03:05]** super simplified version of what

**[03:05]** super simplified version of what happens. But a super high level, we have

**[03:07]** happens. But a super high level, we have

**[03:07]** happens. But a super high level, we have to build an app that is able to like

**[03:09]** to build an app that is able to like

**[03:09]** to build an app that is able to like ingest your prospectors or a term sheet.

**[03:11]** ingest your prospectors or a term sheet.

**[03:11]** ingest your prospectors or a term sheet. It pushes it through a particular

**[03:12]** It pushes it through a particular

**[03:12]** It pushes it through a particular pipeline, right? U then you talk to your

**[03:15]** pipeline, right? U then you talk to your

**[03:15]** pipeline, right? U then you talk to your domain experts and these are like your

**[03:17]** domain experts and these are like your

**[03:17]** domain experts and these are like your business teams, your equity teams, ETF

**[03:19]** business teams, your equity teams, ETF

**[03:19]** business teams, your equity teams, ETF teams, etc. They actually know how to

**[03:21]** teams, etc. They actually know how to

**[03:21]** teams, etc. They actually know how to set up these complex instruments. you

**[03:23]** set up these complex instruments. you

**[03:23]** set up these complex instruments. you get some kind of structured output and

**[03:25]** get some kind of structured output and

**[03:25]** get some kind of structured output and now that team works with the engineering

**[03:27]** now that team works with the engineering

**[03:27]** now that team works with the engineering teams to actually build this

**[03:29]** teams to actually build this

**[03:29]** teams to actually build this transformation logic and the like and

**[03:31]** transformation logic and the like and

**[03:31]** transformation logic and the like and then integrate it with your downstream

**[03:33]** then integrate it with your downstream

**[03:33]** then integrate it with your downstream applications. So you can see that this

**[03:34]** applications. So you can see that this

**[03:34]** applications. So you can see that this process actually takes a long time,

**[03:36]** process actually takes a long time,

**[03:36]** process actually takes a long time, right? So building an app and then

**[03:38]** right? So building an app and then

**[03:38]** right? So building an app and then you're introducing new model providers,

**[03:40]** you're introducing new model providers,

**[03:40]** you're introducing new model providers, you're trying to put in like new

**[03:41]** you're trying to put in like new

**[03:42]** you're trying to put in like new strategies, the lot of challenges to get

**[03:44]** strategies, the lot of challenges to get

**[03:44]** strategies, the lot of challenges to get an single app out, right? We tried this

**[03:46]** an single app out, right? We tried this

**[03:46]** an single app out, right? We tried this with agentic systems doesn't quite work

**[03:49]** with agentic systems doesn't quite work

**[03:49]** with agentic systems doesn't quite work right now because of the complexity and

**[03:51]** right now because of the complexity and

**[03:51]** right now because of the complexity and the the domain knowledge that's imbued

**[03:54]** the the domain knowledge that's imbued

**[03:54]** the the domain knowledge that's imbued in the human head, right? So the big

**[03:58]** in the human head, right? So the big

**[03:58]** in the human head, right? So the big challenges with scale are again these


### [04:00 - 05:00]

**[04:00]** challenges with scale are again these

**[04:00]** challenges with scale are again these three categories, right? One is we're

**[04:02]** three categories, right? One is we're

**[04:02]** three categories, right? One is we're spending a lot of time with our domain

**[04:05]** spending a lot of time with our domain

**[04:05]** spending a lot of time with our domain experts prompt engineering right so in

**[04:07]** experts prompt engineering right so in

**[04:07]** experts prompt engineering right so in the first phase where we have to extract

**[04:08]** the first phase where we have to extract

**[04:08]** the first phase where we have to extract these documents right they're very

**[04:11]** these documents right they're very

**[04:11]** these documents right they're very complex right your prompt itself in our

**[04:14]** complex right your prompt itself in our

**[04:14]** complex right your prompt itself in our simplest case like started with like a

**[04:16]** simplest case like started with like a

**[04:16]** simplest case like started with like a couple of sentences before you knew it

**[04:17]** couple of sentences before you knew it

**[04:17]** couple of sentences before you knew it you're trying to describe this financial

**[04:19]** you're trying to describe this financial

**[04:19]** you're trying to describe this financial instrument and it is like three

**[04:21]** instrument and it is like three

**[04:21]** instrument and it is like three paragraphs long right uh so there's this

**[04:23]** paragraphs long right uh so there's this

**[04:24]** paragraphs long right uh so there's this challenge of like hey I have to iterate

**[04:25]** challenge of like hey I have to iterate

**[04:25]** challenge of like hey I have to iterate over these prompts I have to version and

**[04:27]** over these prompts I have to version and

**[04:27]** over these prompts I have to version and compare these promps how do I manage it

**[04:29]** compare these promps how do I manage it

**[04:29]** compare these promps how do I manage it effectively and I think even the

**[04:30]** effectively and I think even the

**[04:30]** effectively and I think even the previous speaker had mentioned you kind

**[04:31]** previous speaker had mentioned you kind

**[04:31]** previous speaker had mentioned you kind of need to eval and have this data set

**[04:33]** of need to eval and have this data set

**[04:33]** of need to eval and have this data set how how good is your prompt performing

**[04:35]** how how good is your prompt performing

**[04:35]** how how good is your prompt performing so that's the first set of challenges in

**[04:37]** so that's the first set of challenges in

**[04:37]** so that's the first set of challenges in creating like AI apps itself like how

**[04:38]** creating like AI apps itself like how

**[04:38]** creating like AI apps itself like how are you going to manage this in what

**[04:40]** are you going to manage this in what

**[04:40]** are you going to manage this in what direction second set of challenges is

**[04:42]** direction second set of challenges is

**[04:42]** direction second set of challenges is around like LLM strategies right what I

**[04:44]** around like LLM strategies right what I

**[04:44]** around like LLM strategies right what I mean by this is like when you're

**[04:46]** mean by this is like when you're

**[04:46]** mean by this is like when you're building an AI app so to speak you have

**[04:50]** building an AI app so to speak you have

**[04:50]** building an AI app so to speak you have to choose what strategy am I going to

**[04:52]** to choose what strategy am I going to

**[04:52]** to choose what strategy am I going to use like a rag based approach right or

**[04:54]** use like a rag based approach right or

**[04:54]** use like a rag based approach right or am I going to use a chain of

**[04:56]** am I going to use a chain of

**[04:56]** am I going to use a chain of thought-based approach even for a simple

**[04:57]** thought-based approach even for a simple

**[04:57]** thought-based approach even for a simple task of like data extraction depending

**[04:59]** task of like data extraction depending


### [05:00 - 06:00]

**[05:00]** task of like data extraction depending on what your instrument is this actually

**[05:02]** on what your instrument is this actually

**[05:02]** on what your instrument is this actually varies uh very highly right if you take

**[05:05]** varies uh very highly right if you take

**[05:05]** varies uh very highly right if you take like an investment corporate bond like

**[05:07]** like an investment corporate bond like

**[05:07]** like an investment corporate bond like the vanilla one is fairly simple I can

**[05:08]** the vanilla one is fairly simple I can

**[05:08]** the vanilla one is fairly simple I can do this with like in context positive

**[05:11]** do this with like in context positive

**[05:11]** do this with like in context positive model I'm able to get my stuff back if

**[05:12]** model I'm able to get my stuff back if

**[05:12]** model I'm able to get my stuff back if the document size is small right some

**[05:15]** the document size is small right some

**[05:15]** the document size is small right some documents are like thousands of pages

**[05:16]** documents are like thousands of pages

**[05:16]** documents are like thousands of pages long 10,000 pages long now suddenly

**[05:18]** long 10,000 pages long now suddenly

**[05:18]** long 10,000 pages long now suddenly you're like oh okay I don't know if I

**[05:20]** you're like oh okay I don't know if I

**[05:20]** you're like oh okay I don't know if I can pass more than a million tokens into

**[05:22]** can pass more than a million tokens into

**[05:22]** can pass more than a million tokens into say uh the open AI models what do I do

**[05:25]** say uh the open AI models what do I do

**[05:25]** say uh the open AI models what do I do then right then okay I need to choose a

**[05:27]** then right then okay I need to choose a

**[05:27]** then right then okay I need to choose a different strategy and often what we do

**[05:29]** different strategy and often what we do

**[05:29]** different strategy and often what we do is we have a choose choose different

**[05:31]** is we have a choose choose different

**[05:31]** is we have a choose choose different strategies and kind of mix them with

**[05:34]** strategies and kind of mix them with

**[05:34]** strategies and kind of mix them with your prompts to kind of build this

**[05:36]** your prompts to kind of build this

**[05:36]** your prompts to kind of build this iterative process where like I have to

**[05:37]** iterative process where like I have to

**[05:37]** iterative process where like I have to play around with my prompts, I have to

**[05:38]** play around with my prompts, I have to

**[05:38]** play around with my prompts, I have to play around with the different LM

**[05:40]** play around with the different LM

**[05:40]** play around with the different LM strategies and we kind of make want to

**[05:41]** strategies and we kind of make want to

**[05:41]** strategies and we kind of make want to make that process as quickly as

**[05:42]** make that process as quickly as

**[05:42]** make that process as quickly as possible. That's a challenge, right?

**[05:43]** possible. That's a challenge, right?

**[05:44]** possible. That's a challenge, right? Then you have obviously the context

**[05:45]** Then you have obviously the context

**[05:45]** Then you have obviously the context limitations, model limitations,

**[05:47]** limitations, model limitations,

**[05:47]** limitations, model limitations, different vendors and you're trying and

**[05:49]** different vendors and you're trying and

**[05:49]** different vendors and you're trying and testing uh things uh uh for quite a

**[05:51]** testing uh things uh uh for quite a

**[05:52]** testing uh things uh uh for quite a while and this kind of goes into the

**[05:53]** while and this kind of goes into the

**[05:53]** while and this kind of goes into the month right then the biggest challenge

**[05:55]** month right then the biggest challenge

**[05:55]** month right then the biggest challenge is like okay fine I've kind of built

**[05:57]** is like okay fine I've kind of built

**[05:57]** is like okay fine I've kind of built this app now what how do I get this to

**[05:59]** this app now what how do I get this to

**[05:59]** this app now what how do I get this to deployment and it's this whole other set


### [06:00 - 07:00]

**[06:02]** deployment and it's this whole other set

**[06:02]** deployment and it's this whole other set of challenges right you have your

**[06:03]** of challenges right you have your

**[06:03]** of challenges right you have your traditional challenges which is has to

**[06:04]** traditional challenges which is has to

**[06:04]** traditional challenges which is has to do with distribution access control how

**[06:06]** do with distribution access control how

**[06:06]** do with distribution access control how am I going to fedate the app to the

**[06:08]** am I going to fedate the app to the

**[06:08]** am I going to fedate the app to the users but then in the AI space it's like

**[06:11]** users but then in the AI space it's like

**[06:11]** users but then in the AI space it's like you have this new challenge of like what

**[06:13]** you have this new challenge of like what

**[06:13]** you have this new challenge of like what type of cluster am I going to deploy

**[06:15]** type of cluster am I going to deploy

**[06:15]** type of cluster am I going to deploy this to? Right? So, our equity team

**[06:17]** this to? Right? So, our equity team

**[06:17]** this to? Right? So, our equity team would come and say something like, hey,

**[06:18]** would come and say something like, hey,

**[06:18]** would come and say something like, hey, I need to analyze, you know, 500

**[06:20]** I need to analyze, you know, 500

**[06:20]** I need to analyze, you know, 500 research reports like overnight, can you

**[06:22]** research reports like overnight, can you

**[06:22]** research reports like overnight, can you help me do this? Right? So, okay, if

**[06:24]** help me do this? Right? So, okay, if

**[06:24]** help me do this? Right? So, okay, if you're going to do that, I probably have

**[06:25]** you're going to do that, I probably have

**[06:26]** you're going to do that, I probably have to have like a GPU based inference

**[06:27]** to have like a GPU based inference

**[06:27]** to have like a GPU based inference cluster that I can kind of spin up,

**[06:29]** cluster that I can kind of spin up,

**[06:29]** cluster that I can kind of spin up, right? This is the use case that I kind

**[06:31]** right? This is the use case that I kind

**[06:31]** right? This is the use case that I kind of described is the new issue setup. In

**[06:34]** of described is the new issue setup. In

**[06:34]** of described is the new issue setup. In that case, what we do is okay, I don't

**[06:35]** that case, what we do is okay, I don't

**[06:35]** that case, what we do is okay, I don't really want to use my GPU inference

**[06:37]** really want to use my GPU inference

**[06:37]** really want to use my GPU inference cluster, etc. What I do instead is I use

**[06:39]** cluster, etc. What I do instead is I use

**[06:39]** cluster, etc. What I do instead is I use like a burstable cluster, right? All

**[06:42]** like a burstable cluster, right? All

**[06:42]** like a burstable cluster, right? All those have to be kind of like uh defined

**[06:46]** those have to be kind of like uh defined

**[06:46]** those have to be kind of like uh defined so that our app deployment phase is like

**[06:48]** so that our app deployment phase is like

**[06:48]** so that our app deployment phase is like as close to like a CI/CD pipeline as

**[06:50]** as close to like a CI/CD pipeline as

**[06:50]** as close to like a CI/CD pipeline as possible. Then you have like cost

**[06:51]** possible. Then you have like cost

**[06:52]** possible. Then you have like cost controls. So these are again it's not an

**[06:54]** controls. So these are again it's not an

**[06:54]** controls. So these are again it's not an exhaustive list. I think what I'm trying

**[06:55]** exhaustive list. I think what I'm trying

**[06:55]** exhaustive list. I think what I'm trying to highlight is the challenges with kind

**[06:57]** to highlight is the challenges with kind

**[06:57]** to highlight is the challenges with kind of building AI apps. Right? So what we


### [07:00 - 08:00]

**[07:01]** of building AI apps. Right? So what we

**[07:01]** of building AI apps. Right? So what we did at Black Rockck is what I'm going to

**[07:03]** did at Black Rockck is what I'm going to

**[07:04]** did at Black Rockck is what I'm going to do is I'll kind of give you a highle

**[07:05]** do is I'll kind of give you a highle

**[07:05]** do is I'll kind of give you a highle architecture uh and then maybe wuff you

**[07:08]** architecture uh and then maybe wuff you

**[07:08]** architecture uh and then maybe wuff you can dive into the details and mechanics

**[07:09]** can dive into the details and mechanics

**[07:09]** can dive into the details and mechanics of how this works and how we are able to

**[07:12]** of how this works and how we are able to

**[07:12]** of how this works and how we are able to build apps relatively quickly right

**[07:14]** build apps relatively quickly right

**[07:14]** build apps relatively quickly right we're able to we took this uh an app

**[07:16]** we're able to we took this uh an app

**[07:16]** we're able to we took this uh an app took us close to like 8 months somewhere

**[07:18]** took us close to like 8 months somewhere

**[07:18]** took us close to like 8 months somewhere between 3 to 8 months to build a single

**[07:20]** between 3 to 8 months to build a single

**[07:20]** between 3 to 8 months to build a single app for a complex use case and we able

**[07:22]** app for a complex use case and we able

**[07:22]** app for a complex use case and we able to compress time bring it down to like a

**[07:23]** to compress time bring it down to like a

**[07:24]** to compress time bring it down to like a couple of days right we achieved that by

**[07:26]** couple of days right we achieved that by

**[07:26]** couple of days right we achieved that by building up this framework what I kind

**[07:29]** building up this framework what I kind

**[07:29]** building up this framework what I kind of want to focus on is on the top two

**[07:30]** of want to focus on is on the top two

**[07:30]** of want to focus on is on the top two boxes that you see which is your sandbox

**[07:32]** boxes that you see which is your sandbox

**[07:32]** boxes that you see which is your sandbox in your app factory right so to the uh

**[07:36]** in your app factory right so to the uh

**[07:36]** in your app factory right so to the uh the data platform and the developer

**[07:37]** the data platform and the developer

**[07:38]** the data platform and the developer platform is like the name suggest hey

**[07:40]** platform is like the name suggest hey

**[07:40]** platform is like the name suggest hey platform is someone for ingesting data

**[07:42]** platform is someone for ingesting data

**[07:42]** platform is someone for ingesting data etc right you have an orchestration

**[07:44]** etc right you have an orchestration

**[07:44]** etc right you have an orchestration layer that has a pipeline that kind of

**[07:45]** layer that has a pipeline that kind of

**[07:45]** layer that has a pipeline that kind of like transforms it brings it into some

**[07:48]** like transforms it brings it into some

**[07:48]** like transforms it brings it into some uh new format and then you kind of

**[07:49]** uh new format and then you kind of

**[07:49]** uh new format and then you kind of distribute that as a app or report what

**[07:52]** distribute that as a app or report what

**[07:52]** distribute that as a app or report what kind of accelerates at app development

**[07:55]** kind of accelerates at app development

**[07:55]** kind of accelerates at app development is like if you're able to federate out

**[07:57]** is like if you're able to federate out

**[07:57]** is like if you're able to federate out those pain points or those bottlenecks


### [08:00 - 09:00]

**[08:00]** those pain points or those bottlenecks

**[08:00]** those pain points or those bottlenecks which is like prompt creation or

**[08:01]** which is like prompt creation or

**[08:01]** which is like prompt creation or extraction templates choosing an LLM

**[08:03]** extraction templates choosing an LLM

**[08:03]** extraction templates choosing an LLM strategy right having extraction runs or

**[08:06]** strategy right having extraction runs or

**[08:06]** strategy right having extraction runs or like and then building out these logic

**[08:08]** like and then building out these logic

**[08:08]** like and then building out these logic pieces which are calling transformer and

**[08:10]** pieces which are calling transformer and

**[08:10]** pieces which are calling transformer and executors if you can get that sandbox

**[08:12]** executors if you can get that sandbox

**[08:12]** executors if you can get that sandbox out into the hands of the domain experts

**[08:14]** out into the hands of the domain experts

**[08:14]** out into the hands of the domain experts then your iteration speed becomes really

**[08:16]** then your iteration speed becomes really

**[08:16]** then your iteration speed becomes really fast right so you're kind of saying that

**[08:18]** fast right so you're kind of saying that

**[08:18]** fast right so you're kind of saying that hey I have this modular component can I

**[08:20]** hey I have this modular component can I

**[08:20]** hey I have this modular component can I move across the s iteration really

**[08:21]** move across the s iteration really

**[08:21]** move across the s iteration really quickly and then pass it along to an app

**[08:24]** quickly and then pass it along to an app

**[08:24]** quickly and then pass it along to an app factory which is like our cloudnative

**[08:26]** factory which is like our cloudnative

**[08:26]** factory which is like our cloudnative operator which takes a definition and

**[08:27]** operator which takes a definition and

**[08:27]** operator which takes a definition and spins out an app right so that's super

**[08:29]** spins out an app right so that's super

**[08:29]** spins out an app right so that's super high level with that quick demo.

**[08:33]** high level with that quick demo.

**[08:33]** high level with that quick demo. >> Perfect.

**[08:35]** >> Perfect.

**[08:35]** >> Perfect. >> All right,

**[08:37]** >> All right,

**[08:37]** >> All right, cool. So, what I'm going to show you

**[08:39]** cool. So, what I'm going to show you

**[08:39]** cool. So, what I'm going to show you guys is pretty slim down version of the

**[08:41]** guys is pretty slim down version of the

**[08:42]** guys is pretty slim down version of the actual tool we used internally. Um, so

**[08:45]** actual tool we used internally. Um, so

**[08:45]** actual tool we used internally. Um, so to start with, uh, when the operator, so

**[08:47]** to start with, uh, when the operator, so

**[08:47]** to start with, uh, when the operator, so we have like two different, uh, concore

**[08:49]** we have like two different, uh, concore

**[08:49]** we have like two different, uh, concore components. One is the sandbox, another

**[08:51]** components. One is the sandbox, another

**[08:51]** components. One is the sandbox, another one is the factory. So think of sandbox

**[08:53]** one is the factory. So think of sandbox

**[08:53]** one is the factory. So think of sandbox as a playground for the operators to

**[08:56]** as a playground for the operators to

**[08:56]** as a playground for the operators to sort of like quickly build and refine

**[08:57]** sort of like quickly build and refine

**[08:57]** sort of like quickly build and refine the extraction templates. Uh sort of run


### [09:00 - 10:00]

**[09:00]** the extraction templates. Uh sort of run

**[09:00]** the extraction templates. Uh sort of run extraction on the set of documents and

**[09:02]** extraction on the set of documents and

**[09:02]** extraction on the set of documents and then compare and contrast the results of

**[09:04]** then compare and contrast the results of

**[09:04]** then compare and contrast the results of these extractions. Um so it's sort of

**[09:07]** these extractions. Um so it's sort of

**[09:07]** these extractions. Um so it's sort of like to get started with the extraction

**[09:08]** like to get started with the extraction

**[09:08]** like to get started with the extraction template itself. Uh you might have seen

**[09:10]** template itself. Uh you might have seen

**[09:10]** template itself. Uh you might have seen in the other tools both closed and open

**[09:12]** in the other tools both closed and open

**[09:12]** in the other tools both closed and open source they have similar concept like

**[09:14]** source they have similar concept like

**[09:14]** source they have similar concept like prompt template management where you

**[09:16]** prompt template management where you

**[09:16]** prompt template management where you have certain fields that you want to

**[09:18]** have certain fields that you want to

**[09:18]** have certain fields that you want to extract out of the documents and you

**[09:19]** extract out of the documents and you

**[09:19]** extract out of the documents and you have their corresponding prompts and

**[09:21]** have their corresponding prompts and

**[09:21]** have their corresponding prompts and some metadata that you can associate

**[09:22]** some metadata that you can associate

**[09:22]** some metadata that you can associate with them such as the data type that you

**[09:24]** with them such as the data type that you

**[09:24]** with them such as the data type that you expect of the the final result values.

**[09:27]** expect of the the final result values.

**[09:27]** expect of the the final result values. But when these operators sort of like

**[09:29]** But when these operators sort of like

**[09:29]** But when these operators sort of like trying to run extractions on these

**[09:30]** trying to run extractions on these

**[09:30]** trying to run extractions on these documents, they need far more sort of

**[09:33]** documents, they need far more sort of

**[09:33]** documents, they need far more sort of like greater configuration capabilities

**[09:35]** like greater configuration capabilities

**[09:35]** like greater configuration capabilities than just like configuring prompts and

**[09:37]** than just like configuring prompts and

**[09:37]** than just like configuring prompts and configuring the data types that they

**[09:38]** configuring the data types that they

**[09:38]** configuring the data types that they expect for the end result. So they need

**[09:41]** expect for the end result. So they need

**[09:41]** expect for the end result. So they need like hey I need to have multiple QC

**[09:43]** like hey I need to have multiple QC

**[09:43]** like hey I need to have multiple QC checks on the result values. I need to

**[09:45]** checks on the result values. I need to

**[09:45]** checks on the result values. I need to have a lot of validations and

**[09:47]** have a lot of validations and

**[09:47]** have a lot of validations and constraints on the fields and there

**[09:49]** constraints on the fields and there

**[09:49]** constraints on the fields and there might be like a interfield dependencies

**[09:51]** might be like a interfield dependencies

**[09:51]** might be like a interfield dependencies uh what what the fields that are getting

**[09:53]** uh what what the fields that are getting

**[09:53]** uh what what the fields that are getting extracted. So as in mentioned with the

**[09:56]** extracted. So as in mentioned with the

**[09:56]** extracted. So as in mentioned with the new security operation uh issuance

**[09:59]** new security operation uh issuance

**[09:59]** new security operation uh issuance basically onboarding that stuff there


### [10:00 - 11:00]

**[10:02]** basically onboarding that stuff there

**[10:02]** basically onboarding that stuff there could be a case where uh the security or

**[10:04]** could be a case where uh the security or

**[10:04]** could be a case where uh the security or the bond is callable and you have other

**[10:07]** the bond is callable and you have other

**[10:07]** the bond is callable and you have other fields such as call data and call price

**[10:09]** fields such as call data and call price

**[10:09]** fields such as call data and call price which now needs to have a value. So

**[10:10]** which now needs to have a value. So

**[10:10]** which now needs to have a value. So there is like this inter sort of like

**[10:12]** there is like this inter sort of like

**[10:12]** there is like this inter sort of like field dependencies that operators sort

**[10:13]** field dependencies that operators sort

**[10:13]** field dependencies that operators sort of like uh need they need to take that

**[10:16]** of like uh need they need to take that

**[10:16]** of like uh need they need to take that into consideration be able to configure

**[10:17]** into consideration be able to configure

**[10:17]** into consideration be able to configure that. So here is like what a like a

**[10:20]** that. So here is like what a like a

**[10:20]** that. So here is like what a like a sample uh extraction template looks

**[10:22]** sample uh extraction template looks

**[10:22]** sample uh extraction template looks like.

**[10:24]** like.

**[10:24]** like. So here is how a again this is a example

**[10:27]** So here is how a again this is a example

**[10:28]** So here is how a again this is a example template where we have like issuer

**[10:30]** template where we have like issuer

**[10:30]** template where we have like issuer callable call price and call date these

**[10:31]** callable call price and call date these

**[10:31]** callable call price and call date these fields set up and to sort of like add

**[10:33]** fields set up and to sort of like add

**[10:33]** fields set up and to sort of like add new fields we would define the field

**[10:35]** new fields we would define the field

**[10:35]** new fields we would define the field name uh define the data type that is

**[10:37]** name uh define the data type that is

**[10:37]** name uh define the data type that is expected out of that uh define the

**[10:39]** expected out of that uh define the

**[10:39]** expected out of that uh define the source whether it's extracted or derived

**[10:41]** source whether it's extracted or derived

**[10:41]** source whether it's extracted or derived not every time you want to sort of like

**[10:44]** not every time you want to sort of like

**[10:44]** not every time you want to sort of like run an extraction for a field there

**[10:45]** run an extraction for a field there

**[10:45]** run an extraction for a field there might be a derived field that operator

**[10:47]** might be a derived field that operator

**[10:47]** might be a derived field that operator expect which is sort of like uh

**[10:49]** expect which is sort of like uh

**[10:49]** expect which is sort of like uh populated through some transformation

**[10:51]** populated through some transformation

**[10:51]** populated through some transformation downstream um and once uh again uh

**[10:54]** downstream um and once uh again uh

**[10:54]** downstream um and once uh again uh whether the field is required and the

**[10:56]** whether the field is required and the

**[10:56]** whether the field is required and the field dependencies. Here is where you

**[10:57]** field dependencies. Here is where you

**[10:57]** field dependencies. Here is where you define what sort of like dependencies

**[10:59]** define what sort of like dependencies

**[10:59]** define what sort of like dependencies this field have and sort of validations


### [11:00 - 12:00]

**[11:01]** this field have and sort of validations

**[11:01]** this field have and sort of validations right. So this is how they set up the

**[11:03]** right. So this is how they set up the

**[11:03]** right. So this is how they set up the extraction. The next thing is the

**[11:05]** extraction. The next thing is the

**[11:05]** extraction. The next thing is the document management itself. So this is

**[11:07]** document management itself. So this is

**[11:07]** document management itself. So this is where the documents are ingested uh from

**[11:10]** where the documents are ingested uh from

**[11:10]** where the documents are ingested uh from the uh the data platform. They are

**[11:12]** the uh the data platform. They are

**[11:12]** the uh the data platform. They are tagged according to the business

**[11:14]** tagged according to the business

**[11:14]** tagged according to the business category uh and they are labeled they're

**[11:16]** category uh and they are labeled they're

**[11:16]** category uh and they are labeled they're embedded all of that stuff.

**[11:19]** embedded all of that stuff.

**[11:19]** embedded all of that stuff. >> Okay. While I think while Viber kind of

**[11:21]** >> Okay. While I think while Viber kind of

**[11:21]** >> Okay. While I think while Viber kind of brings it up. So I think what in essence

**[11:22]** brings it up. So I think what in essence

**[11:22]** brings it up. So I think what in essence what we're saying is we kind of built

**[11:24]** what we're saying is we kind of built

**[11:24]** what we're saying is we kind of built this tool which has like a UI component

**[11:26]** this tool which has like a UI component

**[11:26]** this tool which has like a UI component and like a framework that actually lets

**[11:28]** and like a framework that actually lets

**[11:28]** and like a framework that actually lets you take these different pieces and

**[11:30]** you take these different pieces and

**[11:30]** you take these different pieces and these modular components and give it to

**[11:32]** these modular components and give it to

**[11:32]** these modular components and give it to the hands of like the domain expert to

**[11:36]** the hands of like the domain expert to

**[11:36]** the hands of like the domain expert to build out their app really quickly.

**[11:38]** build out their app really quickly.

**[11:38]** build out their app really quickly. Right?

**[11:39]** Right?

**[11:39]** Right? >> I think something happened just so let

**[11:41]** >> I think something happened just so let

**[11:41]** >> I think something happened just so let me just sort of walk you guys the what

**[11:43]** me just sort of walk you guys the what

**[11:43]** me just sort of walk you guys the what happens next. Um so like once you have

**[11:45]** happens next. Um so like once you have

**[11:46]** happens next. Um so like once you have set up the extraction templates and

**[11:47]** set up the extraction templates and

**[11:47]** set up the extraction templates and documents management the operators

**[11:48]** documents management the operators

**[11:48]** documents management the operators basically run the extractions. That's

**[11:50]** basically run the extractions. That's

**[11:50]** basically run the extractions. That's where they basically see the values that

**[11:53]** where they basically see the values that

**[11:53]** where they basically see the values that they expect from these documents and

**[11:55]** they expect from these documents and

**[11:55]** they expect from these documents and sort of like review them. Uh the thing

**[11:57]** sort of like review them. Uh the thing

**[11:58]** sort of like review them. Uh the thing with we have seen with these operators


### [12:00 - 13:00]

**[12:00]** with we have seen with these operators

**[12:00]** with we have seen with these operators trying to use other tools. Uh no this is

**[12:02]** trying to use other tools. Uh no this is

**[12:02]** trying to use other tools. Uh no this is just saying um

**[12:04]** just saying um

**[12:04]** just saying um >> yeah I did uh the thing we have seen uh

**[12:07]** >> yeah I did uh the thing we have seen uh

**[12:07]** >> yeah I did uh the thing we have seen uh with these operators is that most of the

**[12:08]** with these operators is that most of the

**[12:08]** with these operators is that most of the tools tools that they have used in past

**[12:11]** tools tools that they have used in past

**[12:11]** tools tools that they have used in past uh these tools basically does extraction

**[12:14]** uh these tools basically does extraction

**[12:14]** uh these tools basically does extraction uh the they do a pretty good job at

**[12:15]** uh the they do a pretty good job at

**[12:15]** uh the they do a pretty good job at extraction but when it comes to like uh

**[12:18]** extraction but when it comes to like uh

**[12:18]** extraction but when it comes to like uh hey I need to now use this result that

**[12:20]** hey I need to now use this result that

**[12:20]** hey I need to now use this result that has been uh presented to me and pass it

**[12:23]** has been uh presented to me and pass it

**[12:23]** has been uh presented to me and pass it to the downstream processes. The process

**[12:25]** to the downstream processes. The process

**[12:25]** to the downstream processes. The process right now is very manual where they have

**[12:27]** right now is very manual where they have

**[12:27]** right now is very manual where they have to like download a CSV or a JSON file,

**[12:29]** to like download a CSV or a JSON file,

**[12:29]** to like download a CSV or a JSON file, run manual or add a transformation and

**[12:32]** run manual or add a transformation and

**[12:32]** run manual or add a transformation and then push it to the downstream process.

**[12:34]** then push it to the downstream process.

**[12:34]** then push it to the downstream process. So what we have done and again I can't

**[12:36]** So what we have done and again I can't

**[12:36]** So what we have done and again I can't show you but what we have done is like

**[12:38]** show you but what we have done is like

**[12:38]** show you but what we have done is like build this sort of like low code no code

**[12:40]** build this sort of like low code no code

**[12:40]** build this sort of like low code no code framework where the operators can

**[12:42]** framework where the operators can

**[12:42]** framework where the operators can basically essentially uh run the uh sort

**[12:46]** basically essentially uh run the uh sort

**[12:46]** basically essentially uh run the uh sort of build this transformation and

**[12:47]** of build this transformation and

**[12:47]** of build this transformation and execution workflows and uh sort of like

**[12:51]** execution workflows and uh sort of like

**[12:51]** execution workflows and uh sort of like have this end toend uh pipeline running

**[12:53]** have this end toend uh pipeline running

**[12:54]** have this end toend uh pipeline running uh and I I think yeah so I think we'll

**[12:56]** uh and I I think yeah so I think we'll

**[12:56]** uh and I I think yeah so I think we'll conclude by saying that our key

**[12:57]** conclude by saying that our key

**[12:57]** conclude by saying that our key takeaways of this right I would say that

**[12:59]** takeaways of this right I would say that

**[12:59]** takeaways of this right I would say that are like three key takeaways invest


### [13:00 - 14:00]

**[13:01]** are like three key takeaways invest

**[13:01]** are like three key takeaways invest heavily on your like prompt engineering

**[13:02]** heavily on your like prompt engineering

**[13:02]** heavily on your like prompt engineering skills for your domain experts

**[13:04]** skills for your domain experts

**[13:04]** skills for your domain experts especially in like the financial space

**[13:06]** especially in like the financial space

**[13:06]** especially in like the financial space and world. Uh defining and describing

**[13:08]** and world. Uh defining and describing

**[13:08]** and world. Uh defining and describing these documents is really hard, right? A

**[13:10]** these documents is really hard, right? A

**[13:10]** these documents is really hard, right? A second is like educating the firm and

**[13:12]** second is like educating the firm and

**[13:12]** second is like educating the firm and the company on what an LLM strategy

**[13:14]** the company on what an LLM strategy

**[13:14]** the company on what an LLM strategy means uh and how to actually fix these

**[13:16]** means uh and how to actually fix these

**[13:16]** means uh and how to actually fix these different pieces for your particular use

**[13:18]** different pieces for your particular use

**[13:18]** different pieces for your particular use case. And I think the third one I would

**[13:21]** case. And I think the third one I would

**[13:21]** case. And I think the third one I would say is hey uh the key takeaway that we

**[13:22]** say is hey uh the key takeaway that we

**[13:22]** say is hey uh the key takeaway that we had is all of this is great in

**[13:24]** had is all of this is great in

**[13:24]** had is all of this is great in experimentation and prototyping mode but

**[13:26]** experimentation and prototyping mode but

**[13:26]** experimentation and prototyping mode but if you kind of want to bring this you

**[13:27]** if you kind of want to bring this you

**[13:28]** if you kind of want to bring this you have to really evaluate what your ROI is

**[13:30]** have to really evaluate what your ROI is

**[13:30]** have to really evaluate what your ROI is and as is it going to be like more

**[13:31]** and as is it going to be like more

**[13:31]** and as is it going to be like more expensive actually spinning up an AI app

**[13:33]** expensive actually spinning up an AI app

**[13:33]** expensive actually spinning up an AI app versus just having like an offtheshelf

**[13:36]** versus just having like an offtheshelf

**[13:36]** versus just having like an offtheshelf product that does it quicker and faster.

**[13:38]** product that does it quicker and faster.

**[13:38]** product that does it quicker and faster. Right? So those are the three key

**[13:40]** Right? So those are the three key

**[13:40]** Right? So those are the three key takeaways in terms of like uh building

**[13:42]** takeaways in terms of like uh building

**[13:42]** takeaways in terms of like uh building apps at scale. And what we realized was

**[13:44]** apps at scale. And what we realized was

**[13:44]** apps at scale. And what we realized was like hey uh this notion of like human in

**[13:47]** like hey uh this notion of like human in

**[13:47]** like hey uh this notion of like human in the loop and the one more thing I'll add

**[13:49]** the loop and the one more thing I'll add

**[13:49]** the loop and the one more thing I'll add is human in the loop is super important

**[13:50]** is human in the loop is super important

**[13:50]** is human in the loop is super important right we all are like really tempted

**[13:52]** right we all are like really tempted

**[13:52]** right we all are like really tempted like let's go all agent tech with this

**[13:54]** like let's go all agent tech with this

**[13:54]** like let's go all agent tech with this uh but in the financial space with

**[13:56]** uh but in the financial space with

**[13:56]** uh but in the financial space with compliance with regulations you kind of

**[13:58]** compliance with regulations you kind of

**[13:58]** compliance with regulations you kind of need those four eyes check and you kind


### [14:00 - 15:00]

**[14:00]** need those four eyes check and you kind

**[14:00]** need those four eyes check and you kind of need the human loop so design for

**[14:01]** of need the human loop so design for

**[14:01]** of need the human loop so design for human in the loop first uh if you're in

**[14:03]** human in the loop first uh if you're in

**[14:03]** human in the loop first uh if you're in a highly regulated environment

**[14:05]** a highly regulated environment

**[14:05]** a highly regulated environment >> yeah and as info said one thing we

**[14:06]** >> yeah and as info said one thing we

**[14:06]** >> yeah and as info said one thing we couldn't show is the whole app factory

**[14:08]** couldn't show is the whole app factory

**[14:08]** couldn't show is the whole app factory sort of like uh component which is all

**[14:11]** sort of like uh component which is all

**[14:11]** sort of like uh component which is all the things that operators do through

**[14:13]** the things that operators do through

**[14:14]** the things that operators do through this iteration cycle of through the

**[14:15]** this iteration cycle of through the

**[14:15]** this iteration cycle of through the sandbox. They take all that knowledge,

**[14:17]** sandbox. They take all that knowledge,

**[14:17]** sandbox. They take all that knowledge, the extraction templates, the transform

**[14:19]** the extraction templates, the transform

**[14:19]** the extraction templates, the transform it transformers and executors they build

**[14:21]** it transformers and executors they build

**[14:21]** it transformers and executors they build through this workflow pipeline and

**[14:23]** through this workflow pipeline and

**[14:23]** through this workflow pipeline and through our app uh ecosystem within uh

**[14:26]** through our app uh ecosystem within uh

**[14:26]** through our app uh ecosystem within uh BlackRock they sort of like build this

**[14:29]** BlackRock they sort of like build this

**[14:29]** BlackRock they sort of like build this uh custom applications that are then

**[14:31]** uh custom applications that are then

**[14:31]** uh custom applications that are then exposed to the users where users of this

**[14:33]** exposed to the users where users of this

**[14:33]** exposed to the users where users of this app don't have to worry about how to

**[14:35]** app don't have to worry about how to

**[14:35]** app don't have to worry about how to configure templates or how to basically

**[14:37]** configure templates or how to basically

**[14:37]** configure templates or how to basically figure out how to integrate the result

**[14:38]** figure out how to integrate the result

**[14:38]** figure out how to integrate the result values into final downstream processes.

**[14:40]** values into final downstream processes.

**[14:40]** values into final downstream processes. they are presented with this whole end

**[14:42]** they are presented with this whole end

**[14:42]** they are presented with this whole end to end app where they can just go and

**[14:44]** to end app where they can just go and

**[14:44]** to end app where they can just go and like sort of like upload documents and

**[14:46]** like sort of like upload documents and

**[14:46]** like sort of like upload documents and run extraction and sort of uh get the

**[14:48]** run extraction and sort of uh get the

**[14:48]** run extraction and sort of uh get the whole pipeline set uh running.

**[14:51]** whole pipeline set uh running.

**[14:51]** whole pipeline set uh running. >> Yeah. With that we'll open up for

**[14:52]** >> Yeah. With that we'll open up for

**[14:52]** >> Yeah. With that we'll open up for questions. I think we have like a minute

**[14:53]** questions. I think we have like a minute

**[14:53]** questions. I think we have like a minute or two left.

**[14:55]** or two left.

**[14:55]** or two left. >> Yeah. Uh so I have a question which may


### [15:00 - 16:00]

**[15:00]** >> Yeah. Uh so I have a question which may

**[15:00]** >> Yeah. Uh so I have a question which may directly be related to

**[15:12]** >> Good morning. I have a question which

**[15:12]** >> Good morning. I have a question which may directly be related to the uh

**[15:16]** may directly be related to the uh

**[15:16]** may directly be related to the uh architecture that you developed.

**[15:18]** architecture that you developed.

**[15:18]** architecture that you developed. >> You can tell me I can discuss later. But

**[15:20]** >> You can tell me I can discuss later. But

**[15:20]** >> You can tell me I can discuss later. But the question is going to be

**[15:23]** the question is going to be

**[15:23]** the question is going to be you you have developed uh um the key

**[15:27]** you you have developed uh um the key

**[15:27]** you you have developed uh um the key takeaways. One of those key takeaways

**[15:29]** takeaways. One of those key takeaways

**[15:30]** takeaways. One of those key takeaways had been in invest heavily on prompt

**[15:33]** had been in invest heavily on prompt

**[15:33]** had been in invest heavily on prompt engineering. So you have essentially

**[15:37]** engineering. So you have essentially

**[15:37]** engineering. So you have essentially automated the process from the leaf

**[15:40]** automated the process from the leaf

**[15:40]** automated the process from the leaf level for example a company's coming to

**[15:44]** level for example a company's coming to

**[15:44]** level for example a company's coming to an IPO from that level all the way to

**[15:48]** an IPO from that level all the way to

**[15:48]** an IPO from that level all the way to cataloging through ETL processes and

**[15:51]** cataloging through ETL processes and

**[15:51]** cataloging through ETL processes and then to finally to the data analytics.

**[15:54]** then to finally to the data analytics.

**[15:54]** then to finally to the data analytics. So now your CEO who looks at the balance

**[15:58]** So now your CEO who looks at the balance

**[15:58]** So now your CEO who looks at the balance sheet, assets and liability will be


### [16:00 - 17:00]

**[16:02]** sheet, assets and liability will be

**[16:02]** sheet, assets and liability will be using your AI the most

**[16:05]** using your AI the most

**[16:05]** using your AI the most and for C uh your CEO. Now what are the

**[16:09]** and for C uh your CEO. Now what are the

**[16:09]** and for C uh your CEO. Now what are the features involved here at the lowest

**[16:12]** features involved here at the lowest

**[16:12]** features involved here at the lowest level for example term maturity duration

**[16:16]** level for example term maturity duration

**[16:16]** level for example term maturity duration there are so many metrics at the L

**[16:18]** there are so many metrics at the L

**[16:18]** there are so many metrics at the L level. How are you transforming those

**[16:22]** level. How are you transforming those

**[16:22]** level. How are you transforming those features from the lowest level to

**[16:25]** features from the lowest level to

**[16:25]** features from the lowest level to highest level? I'm looking for an answer

**[16:27]** highest level? I'm looking for an answer

**[16:27]** highest level? I'm looking for an answer in reference to decentralized data.

**[16:30]** in reference to decentralized data.

**[16:30]** in reference to decentralized data. >> Yeah, I mean I can give you a quick

**[16:31]** >> Yeah, I mean I can give you a quick

**[16:32]** >> Yeah, I mean I can give you a quick answer and then we can discuss uh in

**[16:33]** answer and then we can discuss uh in

**[16:33]** answer and then we can discuss uh in detail like offline. I think real

**[16:35]** detail like offline. I think real

**[16:35]** detail like offline. I think real quickly like the the framework that we

**[16:37]** quickly like the the framework that we

**[16:37]** quickly like the the framework that we built was specifically targeting like

**[16:39]** built was specifically targeting like

**[16:39]** built was specifically targeting like the investment operation domain experts

**[16:41]** the investment operation domain experts

**[16:41]** the investment operation domain experts who are trying to build applications. To

**[16:43]** who are trying to build applications. To

**[16:43]** who are trying to build applications. To your question of like hey what does the

**[16:44]** your question of like hey what does the

**[16:44]** your question of like hey what does the CEO care about? Can I construct a memo

**[16:47]** CEO care about? Can I construct a memo

**[16:47]** CEO care about? Can I construct a memo that gives me my asset liabilities XYZ?

**[16:50]** that gives me my asset liabilities XYZ?

**[16:50]** that gives me my asset liabilities XYZ? Those would be like different

**[16:51]** Those would be like different

**[16:51]** Those would be like different initiatives which may or may not use our

**[16:53]** initiatives which may or may not use our

**[16:53]** initiatives which may or may not use our particular framework. But uh yes, there

**[16:55]** particular framework. But uh yes, there

**[16:55]** particular framework. But uh yes, there are many reusable components in here

**[16:57]** are many reusable components in here

**[16:57]** are many reusable components in here that people can use. Yeah.


### [17:00 - 18:00]

**[17:13]** >> Yeah. So I do like a lot of document

**[17:13]** >> Yeah. So I do like a lot of document processing for insurance company. Pretty

**[17:15]** processing for insurance company. Pretty

**[17:15]** processing for insurance company. Pretty much same problems as you guys run into.

**[17:18]** much same problems as you guys run into.

**[17:18]** much same problems as you guys run into. So I wonder how do you build a wall

**[17:19]** So I wonder how do you build a wall

**[17:20]** So I wonder how do you build a wall around your information extraction from

**[17:21]** around your information extraction from

**[17:22]** around your information extraction from the documents right because there are so

**[17:23]** the documents right because there are so

**[17:23]** the documents right because there are so many things that can go wrong starting

**[17:25]** many things that can go wrong starting

**[17:25]** many things that can go wrong starting from a CR like doesn't understand what

**[17:28]** from a CR like doesn't understand what

**[17:28]** from a CR like doesn't understand what all these terms actually mean no matter

**[17:30]** all these terms actually mean no matter

**[17:30]** all these terms actually mean no matter how you prompt it right all this stuff.

**[17:33]** how you prompt it right all this stuff.

**[17:33]** how you prompt it right all this stuff. So that's kind of what's for the reason

**[17:34]** So that's kind of what's for the reason

**[17:34]** So that's kind of what's for the reason >> again I mean we had all of that that we

**[17:37]** >> again I mean we had all of that that we

**[17:37]** >> again I mean we had all of that that we wanted to show but yeah

**[17:39]** wanted to show but yeah

**[17:39]** wanted to show but yeah >> I think a short answer short answer to

**[17:41]** >> I think a short answer short answer to

**[17:41]** >> I think a short answer short answer to your question is in terms of like

**[17:42]** your question is in terms of like

**[17:42]** your question is in terms of like information security and what are the

**[17:44]** information security and what are the

**[17:44]** information security and what are the boundaries uh that we're putting in

**[17:46]** boundaries uh that we're putting in

**[17:46]** boundaries uh that we're putting in terms of like hey we are not having data

**[17:47]** terms of like hey we are not having data

**[17:47]** terms of like hey we are not having data leakage or errors or understanding of

**[17:50]** leakage or errors or understanding of

**[17:50]** leakage or errors or understanding of like in terms of security you can think

**[17:51]** like in terms of security you can think

**[17:51]** like in terms of security you can think of it as different layers all the way

**[17:53]** of it as different layers all the way

**[17:53]** of it as different layers all the way from like your infra platform

**[17:55]** from like your infra platform

**[17:55]** from like your infra platform application right and the user levels

**[17:58]** application right and the user levels

**[17:58]** application right and the user levels there are different controls and

**[17:59]** there are different controls and


### [18:00 - 19:00]

**[18:00]** there are different controls and policies in place uh and it's also

**[18:02]** policies in place uh and it's also

**[18:02]** policies in place uh and it's also within SD network like I think there are

**[18:04]** within SD network like I think there are

**[18:04]** within SD network like I think there are policies across the stack that we can

**[18:05]** policies across the stack that we can

**[18:06]** policies across the stack that we can get into in detail later that kind of uh

**[18:08]** get into in detail later that kind of uh

**[18:08]** get into in detail later that kind of uh addresses your um concerns

**[18:10]** addresses your um concerns

**[18:10]** addresses your um concerns >> and also also to your point um I think

**[18:13]** >> and also also to your point um I think

**[18:13]** >> and also also to your point um I think we have like different sort of like uh

**[18:16]** we have like different sort of like uh

**[18:16]** we have like different sort of like uh strategies that we use based on uh the

**[18:18]** strategies that we use based on uh the

**[18:18]** strategies that we use based on uh the sort of like the use case at hand. Uh so

**[18:21]** sort of like the use case at hand. Uh so

**[18:21]** sort of like the use case at hand. Uh so it's not just like hey one rag versus

**[18:23]** it's not just like hey one rag versus

**[18:23]** it's not just like hey one rag versus this there are multiple model providers

**[18:25]** this there are multiple model providers

**[18:25]** this there are multiple model providers that we use uh multiple different

**[18:27]** that we use uh multiple different

**[18:27]** that we use uh multiple different strategies etc. uh different like like

**[18:30]** strategies etc. uh different like like

**[18:30]** strategies etc. uh different like like engineering sort of tweaks. Uh so it's a

**[18:33]** engineering sort of tweaks. Uh so it's a

**[18:33]** engineering sort of tweaks. Uh so it's a quite complex sort of yeah process.

**[18:35]** quite complex sort of yeah process.

**[18:35]** quite complex sort of yeah process. >> All right.

**[18:35]** >> All right.

**[18:35]** >> All right. >> Very cool.

**[18:36]** >> Very cool.

**[18:36]** >> Very cool. >> Awesome.

**[18:36]** >> Awesome.

**[18:36]** >> Awesome. >> Thank you.

**[18:38]** >> Thank you.

**[18:38]** >> Thank you. >> All right.

**[18:41]** >> All right.

**[18:41]** >> All right. [Music]


