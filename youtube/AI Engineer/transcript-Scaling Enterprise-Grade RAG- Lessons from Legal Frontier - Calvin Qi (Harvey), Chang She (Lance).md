# Scaling Enterprise-Grade RAG- Lessons from Legal Frontier - Calvin Qi (Harvey), Chang She (Lance)

**Video URL:** https://www.youtube.com/watch?v=W1MiZChnkfA

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** All right. Uh, thank you everyone. We're

**[00:17]** All right. Uh, thank you everyone. We're excited for to be here and thank you for

**[00:19]** excited for to be here and thank you for

**[00:19]** excited for to be here and thank you for uh, coming to our talk. Uh, my name is

**[00:21]** uh, coming to our talk. Uh, my name is

**[00:21]** uh, coming to our talk. Uh, my name is Chong. I'm the CEO and co-founder of

**[00:22]** Chong. I'm the CEO and co-founder of

**[00:22]** Chong. I'm the CEO and co-founder of LANCB. I've been making data tools for

**[00:25]** LANCB. I've been making data tools for

**[00:25]** LANCB. I've been making data tools for machine learning and data science for

**[00:26]** machine learning and data science for

**[00:26]** machine learning and data science for about 20 years. I was one of the

**[00:27]** about 20 years. I was one of the

**[00:27]** about 20 years. I was one of the co-authors of pandas library and I'm

**[00:29]** co-authors of pandas library and I'm

**[00:29]** co-authors of pandas library and I'm working on LANCB today for all of that

**[00:32]** working on LANCB today for all of that

**[00:32]** working on LANCB today for all of that data that doesn't fit neatly into those

**[00:34]** data that doesn't fit neatly into those

**[00:34]** data that doesn't fit neatly into those pandas data frames. And I'm Calvin. I

**[00:37]** pandas data frames. And I'm Calvin. I

**[00:37]** pandas data frames. And I'm Calvin. I lead one of the teams at Harvey Aai

**[00:39]** lead one of the teams at Harvey Aai

**[00:39]** lead one of the teams at Harvey Aai working on rag um tough rag problems

**[00:41]** working on rag um tough rag problems

**[00:41]** working on rag um tough rag problems across massive data sets of complex

**[00:43]** across massive data sets of complex

**[00:43]** across massive data sets of complex legal docs and complex use cases.

**[00:46]** legal docs and complex use cases.

**[00:46]** legal docs and complex use cases. So yeah, our talk is about Oh,

**[00:51]** So yeah, our talk is about Oh,

**[00:51]** So yeah, our talk is about Oh, one sec. Maybe we should have used the

**[00:53]** one sec. Maybe we should have used the

**[00:53]** one sec. Maybe we should have used the other clicker. Yeah. Yeah. All right,

**[00:54]** other clicker. Yeah. Yeah. All right,

**[00:54]** other clicker. Yeah. Yeah. All right, that's okay. We use the laptop.

**[00:57]** that's okay. We use the laptop.

**[00:57]** that's okay. We use the laptop. So we're going to talk about some of the

**[00:58]** So we're going to talk about some of the

**[00:58]** So we're going to talk about some of the tough rag problems on the legal


### [01:00 - 02:00]

**[01:00]** tough rag problems on the legal

**[01:00]** tough rag problems on the legal frontier. Um sort of challenges, some

**[01:02]** frontier. Um sort of challenges, some

**[01:02]** frontier. Um sort of challenges, some solutions and learnings from our

**[01:04]** solutions and learnings from our

**[01:04]** solutions and learnings from our experiences working together on it. So

**[01:06]** experiences working together on it. So

**[01:06]** experiences working together on it. So we'll start roughly with like sort of

**[01:07]** we'll start roughly with like sort of

**[01:07]** we'll start roughly with like sort of how Harvey tackles retrieval, the types

**[01:09]** how Harvey tackles retrieval, the types

**[01:09]** how Harvey tackles retrieval, the types of problems there are and then the

**[01:10]** of problems there are and then the

**[01:10]** of problems there are and then the challenges that come up with that all

**[01:11]** challenges that come up with that all

**[01:11]** challenges that come up with that all with like retrieval quality, scaling, uh

**[01:14]** with like retrieval quality, scaling, uh

**[01:14]** with like retrieval quality, scaling, uh security, all that good stuff and then

**[01:16]** security, all that good stuff and then

**[01:16]** security, all that good stuff and then how we end up sort of creating a system

**[01:17]** how we end up sort of creating a system

**[01:17]** how we end up sort of creating a system with good infrastructure to support

**[01:19]** with good infrastructure to support

**[01:19]** with good infrastructure to support that.

**[01:25]** So first of all, a quick intro to what

**[01:25]** So first of all, a quick intro to what Harvey is. We're a legal AI assistant.

**[01:27]** Harvey is. We're a legal AI assistant.

**[01:27]** Harvey is. We're a legal AI assistant. So, we sell our sort of AI product to a

**[01:30]** So, we sell our sort of AI product to a

**[01:30]** So, we sell our sort of AI product to a bunch of law firms to help them do all

**[01:31]** bunch of law firms to help them do all

**[01:32]** bunch of law firms to help them do all kinds of legal tasks like draft, analyze

**[01:34]** kinds of legal tasks like draft, analyze

**[01:34]** kinds of legal tasks like draft, analyze documents, um sort of go through legal

**[01:37]** documents, um sort of go through legal

**[01:37]** documents, um sort of go through legal workflows and a big part of that is

**[01:39]** workflows and a big part of that is

**[01:39]** workflows and a big part of that is processing data. So, we handle data of

**[01:41]** processing data. So, we handle data of

**[01:41]** processing data. So, we handle data of all different sort of volumes and forms.

**[01:43]** all different sort of volumes and forms.

**[01:43]** all different sort of volumes and forms. Um the sort of different scales of that

**[01:45]** Um the sort of different scales of that

**[01:45]** Um the sort of different scales of that are we have an assistant product that's

**[01:47]** are we have an assistant product that's

**[01:47]** are we have an assistant product that's like on demand uploads, the same way you

**[01:48]** like on demand uploads, the same way you

**[01:48]** like on demand uploads, the same way you might like on demand upload to any AI

**[01:50]** might like on demand upload to any AI

**[01:50]** might like on demand upload to any AI assistant tool. So, that's like a

**[01:52]** assistant tool. So, that's like a

**[01:52]** assistant tool. So, that's like a smaller 1 to 50 range. We have these

**[01:54]** smaller 1 to 50 range. We have these

**[01:54]** smaller 1 to 50 range. We have these vaults which are sort of uh larger scale

**[01:57]** vaults which are sort of uh larger scale

**[01:57]** vaults which are sort of uh larger scale project contacts. So if there's like a a

**[01:59]** project contacts. So if there's like a a

**[01:59]** project contacts. So if there's like a a big deal going on that the law firm's


### [02:00 - 03:00]

**[02:01]** big deal going on that the law firm's

**[02:01]** big deal going on that the law firm's working on or like a data room where

**[02:02]** working on or like a data room where

**[02:02]** working on or like a data room where they need sort of all their contracts,

**[02:03]** they need sort of all their contracts,

**[02:03]** they need sort of all their contracts, all their you know litigation documents

**[02:05]** all their you know litigation documents

**[02:05]** all their you know litigation documents and emails in one place that's a vault.

**[02:07]** and emails in one place that's a vault.

**[02:07]** and emails in one place that's a vault. And then the third is the largest scale

**[02:09]** And then the third is the largest scale

**[02:09]** And then the third is the largest scale which is data corpuses which are like

**[02:11]** which is data corpuses which are like

**[02:11]** which is data corpuses which are like knowledge bases around the world. So

**[02:12]** knowledge bases around the world. So

**[02:12]** knowledge bases around the world. So like legislation, case laws of a

**[02:14]** like legislation, case laws of a

**[02:14]** like legislation, case laws of a particular country um all the sort of

**[02:16]** particular country um all the sort of

**[02:16]** particular country um all the sort of laws, taxes, regulations that go into

**[02:18]** laws, taxes, regulations that go into

**[02:18]** laws, taxes, regulations that go into it.

**[02:24]** So yeah, some big challenges that come

**[02:24]** So yeah, some big challenges that come up come with that. Uh, one is scale.

**[02:27]** up come with that. Uh, one is scale.

**[02:27]** up come with that. Uh, one is scale. Just very large amounts of data. Uh,

**[02:29]** Just very large amounts of data. Uh,

**[02:29]** Just very large amounts of data. Uh, some of these documents are like super

**[02:30]** some of these documents are like super

**[02:30]** some of these documents are like super long and and dense and packed with

**[02:33]** long and and dense and packed with

**[02:33]** long and and dense and packed with content. Um, sparse versus dense I'm

**[02:35]** content. Um, sparse versus dense I'm

**[02:35]** content. Um, sparse versus dense I'm sure is like a sort of retrieval

**[02:37]** sure is like a sort of retrieval

**[02:37]** sure is like a sort of retrieval challenge that all of you deal with um

**[02:38]** challenge that all of you deal with um

**[02:38]** challenge that all of you deal with um of how to represent the data, how to

**[02:40]** of how to represent the data, how to

**[02:40]** of how to represent the data, how to retrieve over and index it. Uh, query

**[02:43]** retrieve over and index it. Uh, query

**[02:43]** retrieve over and index it. Uh, query complexity is a big one. We got very

**[02:45]** complexity is a big one. We got very

**[02:45]** complexity is a big one. We got very sort of difficult expert queries and

**[02:47]** sort of difficult expert queries and

**[02:47]** sort of difficult expert queries and I'll show an example of that in the next

**[02:48]** I'll show an example of that in the next

**[02:48]** I'll show an example of that in the next slide. Um the data is very domain

**[02:51]** slide. Um the data is very domain

**[02:51]** slide. Um the data is very domain specific and complex. Uh there's sort of

**[02:54]** specific and complex. Uh there's sort of

**[02:54]** specific and complex. Uh there's sort of a lot of nitty-gritty legal details that

**[02:56]** a lot of nitty-gritty legal details that

**[02:56]** a lot of nitty-gritty legal details that go into it. So we have to like work with

**[02:57]** go into it. So we have to like work with

**[02:58]** go into it. So we have to like work with domain experts and lawyers to understand

**[02:59]** domain experts and lawyers to understand

**[02:59]** domain experts and lawyers to understand it and try to like translate that into


### [03:00 - 04:00]

**[03:01]** it and try to like translate that into

**[03:01]** it and try to like translate that into how we represent the data, how we you

**[03:03]** how we represent the data, how we you

**[03:03]** how we represent the data, how we you know index, query, pre-process over it.

**[03:06]** know index, query, pre-process over it.

**[03:06]** know index, query, pre-process over it. Um data security and privacy is a big

**[03:08]** Um data security and privacy is a big

**[03:08]** Um data security and privacy is a big one. A lot of this data is sensitive for

**[03:10]** one. A lot of this data is sensitive for

**[03:10]** one. A lot of this data is sensitive for like confidential deals or confidential

**[03:12]** like confidential deals or confidential

**[03:12]** like confidential deals or confidential I don't know IPOs, financial filings,

**[03:14]** I don't know IPOs, financial filings,

**[03:14]** I don't know IPOs, financial filings, stuff like that. So we have to respect

**[03:16]** stuff like that. So we have to respect

**[03:16]** stuff like that. So we have to respect all that for our clients. And then of

**[03:17]** all that for our clients. And then of

**[03:17]** all that for our clients. And then of course evaluation of how to make sure

**[03:19]** course evaluation of how to make sure

**[03:19]** course evaluation of how to make sure systems are actually good.

**[03:22]** systems are actually good.

**[03:22]** systems are actually good. So yeah, I'll show a quick demonstration

**[03:24]** So yeah, I'll show a quick demonstration

**[03:24]** So yeah, I'll show a quick demonstration of a retrieval quality challenge. So uh

**[03:26]** of a retrieval quality challenge. So uh

**[03:26]** of a retrieval quality challenge. So uh this is just on the query side of like

**[03:28]** this is just on the query side of like

**[03:28]** this is just on the query side of like this is maybe the average complexity of

**[03:29]** this is maybe the average complexity of

**[03:29]** this is maybe the average complexity of a query someone might issue in our

**[03:31]** a query someone might issue in our

**[03:31]** a query someone might issue in our product. Um they're much more complex

**[03:33]** product. Um they're much more complex

**[03:33]** product. Um they're much more complex and maybe simpler ones, but this is

**[03:34]** and maybe simpler ones, but this is

**[03:34]** and maybe simpler ones, but this is right in the middle. And you can see

**[03:35]** right in the middle. And you can see

**[03:36]** right in the middle. And you can see that like there's a lot of different

**[03:37]** that like there's a lot of different

**[03:37]** that like there's a lot of different components that go into this. Um there's

**[03:40]** components that go into this. Um there's

**[03:40]** components that go into this. Um there's sort of a sem well to read it out. like

**[03:41]** sort of a sem well to read it out. like

**[03:41]** sort of a sem well to read it out. like what is the applicable regime to covered

**[03:43]** what is the applicable regime to covered

**[03:43]** what is the applicable regime to covered bonds issued before 9 July 2022 under

**[03:46]** bonds issued before 9 July 2022 under

**[03:46]** bonds issued before 9 July 2022 under the directive EU 2019 2062 and article

**[03:49]** the directive EU 2019 2062 and article

**[03:49]** the directive EU 2019 2062 and article 129 of the CR. So, you know, that that's

**[03:52]** 129 of the CR. So, you know, that that's

**[03:52]** 129 of the CR. So, you know, that that's a handful. Um, but what goes into it is

**[03:54]** a handful. Um, but what goes into it is

**[03:54]** a handful. Um, but what goes into it is like there's a semantic aspect. There's

**[03:56]** like there's a semantic aspect. There's

**[03:56]** like there's a semantic aspect. There's sort of implicit filtering going on of

**[03:58]** sort of implicit filtering going on of

**[03:58]** sort of implicit filtering going on of like, you know, we want applicability


### [04:00 - 05:00]

**[04:00]** like, you know, we want applicability

**[04:00]** like, you know, we want applicability before a certain date. Um, there's a

**[04:02]** before a certain date. Um, there's a

**[04:02]** before a certain date. Um, there's a specialized data set being referenced,

**[04:03]** specialized data set being referenced,

**[04:03]** specialized data set being referenced, which is EU laws and directives. Um,

**[04:06]** which is EU laws and directives. Um,

**[04:06]** which is EU laws and directives. Um, there's kind of keyword matches of like

**[04:08]** there's kind of keyword matches of like

**[04:08]** there's kind of keyword matches of like the specific, you know, regulation

**[04:09]** the specific, you know, regulation

**[04:09]** the specific, you know, regulation directive ID. Um, it is multiart in that

**[04:12]** directive ID. Um, it is multiart in that

**[04:12]** directive ID. Um, it is multiart in that it's sort of asking how this applies to

**[04:14]** it's sort of asking how this applies to

**[04:14]** it's sort of asking how this applies to two different regulations, like one

**[04:15]** two different regulations, like one

**[04:15]** two different regulations, like one directive, one article. And there's like

**[04:18]** directive, one article. And there's like

**[04:18]** directive, one article. And there's like domain jargon here where this is like an

**[04:20]** domain jargon here where this is like an

**[04:20]** domain jargon here where this is like an abbreviation. Uh I forget what it was.

**[04:22]** abbreviation. Uh I forget what it was.

**[04:22]** abbreviation. Uh I forget what it was. Capital regulations something. I looked

**[04:24]** Capital regulations something. I looked

**[04:24]** Capital regulations something. I looked it up this morning. Um but yeah, it's

**[04:26]** it up this morning. Um but yeah, it's

**[04:26]** it up this morning. Um but yeah, it's very complex and we sort of need a need

**[04:29]** very complex and we sort of need a need

**[04:29]** very complex and we sort of need a need a system that can tackle all this

**[04:31]** a system that can tackle all this

**[04:31]** a system that can tackle all this complexity and sort of break down this

**[04:32]** complexity and sort of break down this

**[04:32]** complexity and sort of break down this query and um use all the appropriate

**[04:35]** query and um use all the appropriate

**[04:35]** query and um use all the appropriate technologies for the different parts of

**[04:37]** technologies for the different parts of

**[04:37]** technologies for the different parts of it.

**[04:39]** it.

**[04:39]** it. And yeah, so one common question we get

**[04:42]** And yeah, so one common question we get

**[04:42]** And yeah, so one common question we get sort of in response to this complexity

**[04:43]** sort of in response to this complexity

**[04:43]** sort of in response to this complexity is how do you evaluate your systems? How

**[04:45]** is how do you evaluate your systems? How

**[04:46]** is how do you evaluate your systems? How do you make sure they're good? Um, and

**[04:47]** do you make sure they're good? Um, and

**[04:47]** do you make sure they're good? Um, and that's actually where we spend a ton of

**[04:49]** that's actually where we spend a ton of

**[04:49]** that's actually where we spend a ton of time. It's, you know, not as much on the

**[04:51]** time. It's, you know, not as much on the

**[04:51]** time. It's, you know, not as much on the algorithms and the the fancy agentic

**[04:53]** algorithms and the the fancy agentic

**[04:53]** algorithms and the the fancy agentic techniques, but more like how to

**[04:54]** techniques, but more like how to

**[04:54]** techniques, but more like how to validate them. Um, and I'd say like

**[04:56]** validate them. Um, and I'd say like

**[04:56]** validate them. Um, and I'd say like investing in eval driven development is

**[04:58]** investing in eval driven development is

**[04:58]** investing in eval driven development is a huge huge key to building these


### [05:00 - 06:00]

**[05:01]** a huge huge key to building these

**[05:01]** a huge huge key to building these systems and making sure they're good,

**[05:02]** systems and making sure they're good,

**[05:02]** systems and making sure they're good, especially when it's a tough domain that

**[05:04]** especially when it's a tough domain that

**[05:04]** especially when it's a tough domain that like you don't inherently know much

**[05:06]** like you don't inherently know much

**[05:06]** like you don't inherently know much about as maybe an engineer or a

**[05:07]** about as maybe an engineer or a

**[05:07]** about as maybe an engineer or a researcher. Um, so I say there's no

**[05:09]** researcher. Um, so I say there's no

**[05:09]** researcher. Um, so I say there's no silver bullet eval, but we have like a

**[05:11]** silver bullet eval, but we have like a

**[05:11]** silver bullet eval, but we have like a whole range of them of like different

**[05:13]** whole range of them of like different

**[05:13]** whole range of them of like different task depths and complexities. So in sort

**[05:15]** task depths and complexities. So in sort

**[05:15]** task depths and complexities. So in sort of one dimension you have it being sort

**[05:18]** of one dimension you have it being sort

**[05:18]** of one dimension you have it being sort of higher fidelity but more costly and

**[05:20]** of higher fidelity but more costly and

**[05:20]** of higher fidelity but more costly and then the other direction it's like more

**[05:21]** then the other direction it's like more

**[05:21]** then the other direction it's like more automated evals that are faster to

**[05:23]** automated evals that are faster to

**[05:23]** automated evals that are faster to iterate on. So as an example like the um

**[05:26]** iterate on. So as an example like the um

**[05:26]** iterate on. So as an example like the um sort of high fidelity would be like

**[05:28]** sort of high fidelity would be like

**[05:28]** sort of high fidelity would be like expert reviews of just having them

**[05:30]** expert reviews of just having them

**[05:30]** expert reviews of just having them directly review outputs and analyze them

**[05:32]** directly review outputs and analyze them

**[05:32]** directly review outputs and analyze them and write reports. Um so that's like

**[05:34]** and write reports. Um so that's like

**[05:34]** and write reports. Um so that's like super expensive but super high quality.

**[05:37]** super expensive but super high quality.

**[05:37]** super expensive but super high quality. And then maybe something in between is

**[05:38]** And then maybe something in between is

**[05:38]** And then maybe something in between is like an expert labeled like set of

**[05:41]** like an expert labeled like set of

**[05:41]** like an expert labeled like set of criteria that you can maybe evaluate

**[05:43]** criteria that you can maybe evaluate

**[05:43]** criteria that you can maybe evaluate synthetically or evaluate in some

**[05:44]** synthetically or evaluate in some

**[05:44]** synthetically or evaluate in some automated way. So it's still expensive

**[05:46]** automated way. So it's still expensive

**[05:46]** automated way. So it's still expensive to curate, maybe a little expensive to

**[05:47]** to curate, maybe a little expensive to

**[05:47]** to curate, maybe a little expensive to run but more um more tractable. And then

**[05:51]** run but more um more tractable. And then

**[05:51]** run but more um more tractable. And then the third is sort of the fastest

**[05:52]** the third is sort of the fastest

**[05:52]** the third is sort of the fastest iteration which is um sort of more

**[05:54]** iteration which is um sort of more

**[05:54]** iteration which is um sort of more automated quantitative metrics like just

**[05:56]** automated quantitative metrics like just

**[05:56]** automated quantitative metrics like just you know retrieval, precision and recall

**[05:58]** you know retrieval, precision and recall

**[05:58]** you know retrieval, precision and recall sort of different more deterministic


### [06:00 - 07:00]

**[06:01]** sort of different more deterministic

**[06:01]** sort of different more deterministic success criteria of like am I pulling

**[06:02]** success criteria of like am I pulling

**[06:02]** success criteria of like am I pulling documents from the right folder? Is it

**[06:04]** documents from the right folder? Is it

**[06:04]** documents from the right folder? Is it the right section? Do they have the

**[06:06]** the right section? Do they have the

**[06:06]** the right section? Do they have the right keywords in them? things like that

**[06:13]** and yeah give you a quick sense also of

**[06:13]** and yeah give you a quick sense also of sort of the scale and complexity on the

**[06:15]** sort of the scale and complexity on the

**[06:15]** sort of the scale and complexity on the data side not only on the query side. So

**[06:18]** data side not only on the query side. So

**[06:18]** data side not only on the query side. So the data sets we integrate with are

**[06:20]** the data sets we integrate with are

**[06:20]** the data sets we integrate with are pretty massive. Um as you can see we

**[06:22]** pretty massive. Um as you can see we

**[06:22]** pretty massive. Um as you can see we support like you know data sets across

**[06:25]** support like you know data sets across

**[06:25]** support like you know data sets across all different kinds of countries and for

**[06:26]** all different kinds of countries and for

**[06:26]** all different kinds of countries and for each one there's sort of complex

**[06:28]** each one there's sort of complex

**[06:28]** each one there's sort of complex filtering and organization and

**[06:29]** filtering and organization and

**[06:30]** filtering and organization and categorization that goes into it. Um, so

**[06:32]** categorization that goes into it. Um, so

**[06:32]** categorization that goes into it. Um, so we sort of work with domain experts for

**[06:34]** we sort of work with domain experts for

**[06:34]** we sort of work with domain experts for all of this, but also try to apply

**[06:36]** all of this, but also try to apply

**[06:36]** all of this, but also try to apply automation whenever possible, like use

**[06:37]** automation whenever possible, like use

**[06:38]** automation whenever possible, like use their guidance to maybe come up with

**[06:39]** their guidance to maybe come up with

**[06:39]** their guidance to maybe come up with heristics or LLM processing techniques

**[06:42]** heristics or LLM processing techniques

**[06:42]** heristics or LLM processing techniques um to be able to categorize all this.

**[06:44]** um to be able to categorize all this.

**[06:44]** um to be able to categorize all this. Um, and I'd say that the performance

**[06:47]** Um, and I'd say that the performance

**[06:47]** Um, and I'd say that the performance implications are are pretty significant

**[06:49]** implications are are pretty significant

**[06:49]** implications are are pretty significant as well. Um, we need very good

**[06:52]** as well. Um, we need very good

**[06:52]** as well. Um, we need very good performance both online and offline.

**[06:54]** performance both online and offline.

**[06:54]** performance both online and offline. online being like querying over this.

**[06:56]** online being like querying over this.

**[06:56]** online being like querying over this. You want good latency and then offline

**[06:57]** You want good latency and then offline

**[06:57]** You want good latency and then offline being like ingestion, reingestion,


### [07:00 - 08:00]

**[07:00]** being like ingestion, reingestion,

**[07:00]** being like ingestion, reingestion, running ML experiments for different

**[07:01]** running ML experiments for different

**[07:01]** running ML experiments for different variations and such. Um and I say

**[07:03]** variations and such. Um and I say

**[07:03]** variations and such. Um and I say generally one of these corpuses can be

**[07:05]** generally one of these corpuses can be

**[07:05]** generally one of these corpuses can be like yeah tens of millions of docs. Uh

**[07:08]** like yeah tens of millions of docs. Uh

**[07:08]** like yeah tens of millions of docs. Uh so yeah pretty large scale and each

**[07:10]** so yeah pretty large scale and each

**[07:10]** so yeah pretty large scale and each document is often quite large.

**[07:18]** So I can talk quickly about kind of

**[07:18]** So I can talk quickly about kind of infrastructure needs to support this. So

**[07:21]** infrastructure needs to support this. So

**[07:21]** infrastructure needs to support this. So at this scale of course we you know we

**[07:24]** at this scale of course we you know we

**[07:24]** at this scale of course we you know we want infrastructure to be reliable

**[07:27]** want infrastructure to be reliable

**[07:27]** want infrastructure to be reliable available um for all our users at all

**[07:29]** available um for all our users at all

**[07:29]** available um for all our users at all times. I'm sure that's something that

**[07:30]** times. I'm sure that's something that

**[07:30]** times. I'm sure that's something that you know all all products need. Um, we

**[07:32]** you know all all products need. Um, we

**[07:32]** you know all all products need. Um, we also want smooth sort of onboarding and

**[07:35]** also want smooth sort of onboarding and

**[07:35]** also want smooth sort of onboarding and scaling where, you know, we definitely

**[07:37]** scaling where, you know, we definitely

**[07:37]** scaling where, you know, we definitely want our ML and data teams to be able to

**[07:39]** want our ML and data teams to be able to

**[07:39]** want our ML and data teams to be able to focus more on the sort of the business

**[07:41]** focus more on the sort of the business

**[07:42]** focus more on the sort of the business logic and the quality um, and spinning

**[07:45]** logic and the quality um, and spinning

**[07:45]** logic and the quality um, and spinning up new applications and products for

**[07:46]** up new applications and products for

**[07:46]** up new applications and products for customers and, you know, not too much

**[07:48]** customers and, you know, not too much

**[07:48]** customers and, you know, not too much about like the nitty-gritty details of

**[07:49]** about like the nitty-gritty details of

**[07:49]** about like the nitty-gritty details of the database or tuning that or manually

**[07:52]** the database or tuning that or manually

**[07:52]** the database or tuning that or manually scaling. Um, and of course there's

**[07:53]** scaling. Um, and of course there's

**[07:53]** scaling. Um, and of course there's always some in between where you you

**[07:54]** always some in between where you you

**[07:54]** always some in between where you you want to have awareness of it. It can't

**[07:56]** want to have awareness of it. It can't

**[07:56]** want to have awareness of it. It can't be like fully thousand% automated. Um

**[07:59]** be like fully thousand% automated. Um

**[07:59]** be like fully thousand% automated. Um likewise we we need sort of flexibility


### [08:00 - 09:00]

**[08:01]** likewise we we need sort of flexibility

**[08:01]** likewise we we need sort of flexibility and capabilities around data privacy and

**[08:03]** and capabilities around data privacy and

**[08:03]** and capabilities around data privacy and data retention. Um like I mentioned with

**[08:07]** data retention. Um like I mentioned with

**[08:07]** data retention. Um like I mentioned with some uh storage needing to be like

**[08:09]** some uh storage needing to be like

**[08:10]** some uh storage needing to be like segregated depending on the customer

**[08:11]** segregated depending on the customer

**[08:11]** segregated depending on the customer depending on the use case sort of

**[08:13]** depending on the use case sort of

**[08:13]** depending on the use case sort of retention policies on some docs that we

**[08:15]** retention policies on some docs that we

**[08:15]** retention policies on some docs that we might only be allowed to store for

**[08:17]** might only be allowed to store for

**[08:17]** might only be allowed to store for certain amounts of time for legal

**[08:18]** certain amounts of time for legal

**[08:18]** certain amounts of time for legal reasons. Uh we want good sort of

**[08:21]** reasons. Uh we want good sort of

**[08:21]** reasons. Uh we want good sort of telemetry and usage around the database.

**[08:24]** telemetry and usage around the database.

**[08:24]** telemetry and usage around the database. And then of course any sort of vector or

**[08:27]** And then of course any sort of vector or

**[08:27]** And then of course any sort of vector or or keyword or any filtering database we

**[08:29]** or keyword or any filtering database we

**[08:29]** or keyword or any filtering database we need we want to support good performance

**[08:32]** need we want to support good performance

**[08:32]** need we want to support good performance query flexibility scale especially for

**[08:34]** query flexibility scale especially for

**[08:34]** query flexibility scale especially for all the different kinds of query

**[08:35]** all the different kinds of query

**[08:35]** all the different kinds of query patterns I mentioned before where it's

**[08:37]** patterns I mentioned before where it's

**[08:37]** patterns I mentioned before where it's like you need exact matches you want

**[08:39]** like you need exact matches you want

**[08:39]** like you need exact matches you want semantic matches you want filters you

**[08:41]** semantic matches you want filters you

**[08:42]** semantic matches you want filters you might want sort of to sort of navigate

**[08:44]** might want sort of to sort of navigate

**[08:44]** might want sort of to sort of navigate it maybe yeah agentically or like in

**[08:47]** it maybe yeah agentically or like in

**[08:47]** it maybe yeah agentically or like in some dynamic way. Um so yeah all that

**[08:50]** some dynamic way. Um so yeah all that

**[08:50]** some dynamic way. Um so yeah all that flexibility is important to us at scale.

**[08:55]** flexibility is important to us at scale.

**[08:55]** flexibility is important to us at scale. And that's where Lance TV comes in.

**[08:57]** And that's where Lance TV comes in.

**[08:57]** And that's where Lance TV comes in. Cool. Thank you. Awesome. So,


### [09:00 - 10:00]

**[09:01]** Cool. Thank you. Awesome. So,

**[09:02]** Cool. Thank you. Awesome. So, sorry.

**[09:08]** Okay. I'm going to try to hold this here

**[09:08]** Okay. I'm going to try to hold this here maybe so there's no echo. Okay. Um,

**[09:12]** maybe so there's no echo. Okay. Um,

**[09:12]** maybe so there's no echo. Okay. Um, yeah. So uh as I was saying um so you

**[09:17]** yeah. So uh as I was saying um so you

**[09:17]** yeah. So uh as I was saying um so you know I I work at LANC DB and what we are

**[09:21]** know I I work at LANC DB and what we are

**[09:21]** know I I work at LANC DB and what we are delivering for um AI is uh beyond what I

**[09:25]** delivering for um AI is uh beyond what I

**[09:25]** delivering for um AI is uh beyond what I call just a vector database but what we

**[09:28]** call just a vector database but what we

**[09:28]** call just a vector database but what we call an AI native multimodal lakehouse

**[09:30]** call an AI native multimodal lakehouse

**[09:30]** call an AI native multimodal lakehouse and so if you think about back to maybe

**[09:33]** and so if you think about back to maybe

**[09:33]** and so if you think about back to maybe Jerry's talk right in addition to search

**[09:36]** Jerry's talk right in addition to search

**[09:36]** Jerry's talk right in addition to search you also need um a good foundation good

**[09:40]** you also need um a good foundation good

**[09:40]** you also need um a good foundation good platform for you to do all of the other

**[09:41]** platform for you to do all of the other

**[09:41]** platform for you to do all of the other tasks um that you need to do with your

**[09:44]** tasks um that you need to do with your

**[09:44]** tasks um that you need to do with your AI data. So, this can be feature

**[09:47]** AI data. So, this can be feature

**[09:47]** AI data. So, this can be feature extraction, um, generating summaries,

**[09:50]** extraction, um, generating summaries,

**[09:50]** extraction, um, generating summaries, generating text descriptions from

**[09:52]** generating text descriptions from

**[09:52]** generating text descriptions from images, managing all that data, and you

**[09:55]** images, managing all that data, and you

**[09:55]** images, managing all that data, and you want to be able to do that all together.

**[09:56]** want to be able to do that all together.

**[09:56]** want to be able to do that all together. So, what you really need is sort of this

**[09:58]** So, what you really need is sort of this

**[09:58]** So, what you really need is sort of this lakehouse architecture where all the


### [10:00 - 11:00]

**[10:00]** lakehouse architecture where all the

**[10:00]** lakehouse architecture where all the data can be stored in one place on

**[10:03]** data can be stored in one place on

**[10:03]** data can be stored in one place on object store. Um, you can run search and

**[10:07]** object store. Um, you can run search and

**[10:07]** object store. Um, you can run search and retrieval workloads, you can run

**[10:09]** retrieval workloads, you can run

**[10:09]** retrieval workloads, you can run analytical workloads, you can train off

**[10:11]** analytical workloads, you can train off

**[10:11]** analytical workloads, you can train off of that data, and of course, you can

**[10:13]** of that data, and of course, you can

**[10:13]** of that data, and of course, you can pre-process that data to iterate on new

**[10:16]** pre-process that data to iterate on new

**[10:16]** pre-process that data to iterate on new features that you can experiment for

**[10:17]** features that you can experiment for

**[10:17]** features that you can experiment for your applications and models.

**[10:20]** your applications and models.

**[10:20]** your applications and models. Um specifically to uh sort of in

**[10:24]** Um specifically to uh sort of in

**[10:24]** Um specifically to uh sort of in addition to these like large batch

**[10:27]** addition to these like large batch

**[10:27]** addition to these like large batch offline use cases um you know lakehouse

**[10:30]** offline use cases um you know lakehouse

**[10:30]** offline use cases um you know lakehouse architectures generally are good for

**[10:31]** architectures generally are good for

**[10:32]** architectures generally are good for that but not necessarily for online

**[10:34]** that but not necessarily for online

**[10:34]** that but not necessarily for online serving and this is where LANC DB u

**[10:37]** serving and this is where LANC DB u

**[10:38]** serving and this is where LANC DB u distributed architecture comes in and uh

**[10:41]** distributed architecture comes in and uh

**[10:41]** distributed architecture comes in and uh it's actually good for both offline and

**[10:43]** it's actually good for both offline and

**[10:43]** it's actually good for both offline and online context so that we can serve at

**[10:46]** online context so that we can serve at

**[10:46]** online context so that we can serve at massive scale from cloud uh object store

**[10:49]** massive scale from cloud uh object store

**[10:49]** massive scale from cloud uh object store uh we can deliver cloud uh compute,

**[10:51]** uh we can deliver cloud uh compute,

**[10:51]** uh we can deliver cloud uh compute, memory and storage separation and we

**[10:54]** memory and storage separation and we

**[10:54]** memory and storage separation and we give you a simple API for sophisticated

**[10:57]** give you a simple API for sophisticated

**[10:57]** give you a simple API for sophisticated retrieval whether you want to combine

**[10:59]** retrieval whether you want to combine

**[10:59]** retrieval whether you want to combine multiple vector columns uh vector and uh


### [11:00 - 12:00]

**[11:03]** multiple vector columns uh vector and uh

**[11:03]** multiple vector columns uh vector and uh full text search and then do re-ranking

**[11:05]** full text search and then do re-ranking

**[11:05]** full text search and then do re-ranking on top of that. Those are all available

**[11:08]** on top of that. Those are all available

**[11:08]** on top of that. Those are all available with an API in Python or TypeScript that

**[11:12]** with an API in Python or TypeScript that

**[11:12]** with an API in Python or TypeScript that feels um what you know folks have told

**[11:15]** feels um what you know folks have told

**[11:15]** feels um what you know folks have told me feels kind of like pandas or polar

**[11:17]** me feels kind of like pandas or polar

**[11:18]** me feels kind of like pandas or polar like very familiar to data workers

**[11:20]** like very familiar to data workers

**[11:20]** like very familiar to data workers who've uh are used to dataf frame me

**[11:23]** who've uh are used to dataf frame me

**[11:23]** who've uh are used to dataf frame me type of APIs and of course for large

**[11:26]** type of APIs and of course for large

**[11:26]** type of APIs and of course for large tables uh we support GPU indexing so I

**[11:29]** tables uh we support GPU indexing so I

**[11:29]** tables uh we support GPU indexing so I think the our our record has been around

**[11:31]** think the our our record has been around

**[11:31]** think the our our record has been around something like three or four billion

**[11:34]** something like three or four billion

**[11:34]** something like three or four billion vectors in a single table um that can in

**[11:38]** vectors in a single table um that can in

**[11:38]** vectors in a single table um that can in index in under uh two or three hours.

**[11:42]** index in under uh two or three hours.

**[11:42]** index in under uh two or three hours. So um all of that is to say like LANCB

**[11:46]** So um all of that is to say like LANCB

**[11:46]** So um all of that is to say like LANCB excels at massive scale and it's this is

**[11:49]** excels at massive scale and it's this is

**[11:49]** excels at massive scale and it's this is happening at a fraction of the cost

**[11:51]** happening at a fraction of the cost

**[11:51]** happening at a fraction of the cost because of the uh compute storage

**[11:53]** because of the uh compute storage

**[11:54]** because of the uh compute storage separation and because we take advantage

**[11:56]** separation and because we take advantage

**[11:56]** separation and because we take advantage of object store and um so of course uh


### [12:00 - 13:00]

**[12:01]** of object store and um so of course uh

**[12:01]** of object store and um so of course uh and I talked about sort of having one

**[12:03]** and I talked about sort of having one

**[12:03]** and I talked about sort of having one place to put all of your AI data. So

**[12:05]** place to put all of your AI data. So

**[12:05]** place to put all of your AI data. So this is the only database where you can

**[12:08]** this is the only database where you can

**[12:08]** this is the only database where you can put you know images and uh videos and

**[12:11]** put you know images and uh videos and

**[12:11]** put you know images and uh videos and audio track next to your embeddings next

**[12:14]** audio track next to your embeddings next

**[12:14]** audio track next to your embeddings next to text data next to your um tabular

**[12:17]** to text data next to your um tabular

**[12:17]** to text data next to your um tabular data uh time series data. You can put

**[12:20]** data uh time series data. You can put

**[12:20]** data uh time series data. You can put all of that in a single table.

**[12:22]** all of that in a single table.

**[12:22]** all of that in a single table. Um and then you can of course use that

**[12:24]** Um and then you can of course use that

**[12:24]** Um and then you can of course use that as the single source of truth for all

**[12:26]** as the single source of truth for all

**[12:26]** as the single source of truth for all the different workloads that you want to

**[12:28]** the different workloads that you want to

**[12:28]** the different workloads that you want to do that do on that data from search to

**[12:31]** do that do on that data from search to

**[12:31]** do that do on that data from search to analytics to training and of course

**[12:32]** analytics to training and of course

**[12:32]** analytics to training and of course pre-processing or feature engineering. A

**[12:35]** pre-processing or feature engineering. A

**[12:35]** pre-processing or feature engineering. A lot of that um is possible because of

**[12:39]** lot of that um is possible because of

**[12:39]** lot of that um is possible because of the open source lance format that we

**[12:41]** the open source lance format that we

**[12:41]** the open source lance format that we built from the ground up. Um so you know

**[12:45]** built from the ground up. Um so you know

**[12:45]** built from the ground up. Um so you know if you're working with multimmodal data

**[12:47]** if you're working with multimmodal data

**[12:47]** if you're working with multimmodal data whether it's documents um you know PDF

**[12:50]** whether it's documents um you know PDF

**[12:50]** whether it's documents um you know PDF scan slides or just large even large

**[12:52]** scan slides or just large even large

**[12:52]** scan slides or just large even large scale videos uh if you're doing that in

**[12:55]** scale videos uh if you're doing that in

**[12:55]** scale videos uh if you're doing that in let's say like web data set or iceberg

**[12:57]** let's say like web data set or iceberg

**[12:57]** let's say like web data set or iceberg parquet you're missing out on a lot of


### [13:00 - 14:00]

**[13:00]** parquet you're missing out on a lot of

**[13:00]** parquet you're missing out on a lot of features um and things like you know

**[13:03]** features um and things like you know

**[13:03]** features um and things like you know lack of random access or the inability

**[13:06]** lack of random access or the inability

**[13:06]** lack of random access or the inability to support large blob data or not being

**[13:09]** to support large blob data or not being

**[13:09]** to support large blob data or not being very efficient about schema evolution.

**[13:12]** very efficient about schema evolution.

**[13:12]** very efficient about schema evolution. Uh so LAN's format by giving you uh

**[13:16]** Uh so LAN's format by giving you uh

**[13:16]** Uh so LAN's format by giving you uh giving you all of those right it makes

**[13:19]** giving you all of those right it makes

**[13:19]** giving you all of those right it makes it so that you can store all of your

**[13:21]** it so that you can store all of your

**[13:21]** it so that you can store all of your data in one place rather than split up

**[13:23]** data in one place rather than split up

**[13:23]** data in one place rather than split up across multiple parts. And so this is

**[13:27]** across multiple parts. And so this is

**[13:27]** across multiple parts. And so this is the I would say like the the

**[13:29]** the I would say like the the

**[13:29]** the I would say like the the foundational innovation in LANC DB where

**[13:33]** foundational innovation in LANC DB where

**[13:33]** foundational innovation in LANC DB where um without it what we see a lot of AI

**[13:35]** um without it what we see a lot of AI

**[13:35]** um without it what we see a lot of AI teams doing is they they have to have

**[13:37]** teams doing is they they have to have

**[13:37]** teams doing is they they have to have different copies of different parts of

**[13:39]** different copies of different parts of

**[13:39]** different copies of different parts of their data in different places and

**[13:40]** their data in different places and

**[13:40]** their data in different places and they're spending a lot of their time and

**[13:41]** they're spending a lot of their time and

**[13:41]** they're spending a lot of their time and effort just sort of keeping those um

**[13:44]** effort just sort of keeping those um

**[13:44]** effort just sort of keeping those um pieces glued together and in sync with

**[13:47]** pieces glued together and in sync with

**[13:47]** pieces glued together and in sync with each other.

**[13:49]** each other.

**[13:49]** each other. Right? So um kind of to to basically you

**[13:53]** Right? So um kind of to to basically you

**[13:53]** Right? So um kind of to to basically you can think about uh lance format as sort

**[13:56]** can think about uh lance format as sort

**[13:56]** can think about uh lance format as sort of parquet plus iceberg plus secondary

**[13:59]** of parquet plus iceberg plus secondary

**[13:59]** of parquet plus iceberg plus secondary indices but for AI data and that gives


### [14:00 - 15:00]

**[14:02]** indices but for AI data and that gives

**[14:02]** indices but for AI data and that gives you fast random access which is good for

**[14:05]** you fast random access which is good for

**[14:05]** you fast random access which is good for search and shuffle. Uh it still gives

**[14:07]** search and shuffle. Uh it still gives

**[14:07]** search and shuffle. Uh it still gives you fast scans which is so good for

**[14:09]** you fast scans which is so good for

**[14:09]** you fast scans which is so good for analytics and you know data loading and

**[14:11]** analytics and you know data loading and

**[14:11]** analytics and you know data loading and training and um it's the only one out of

**[14:14]** training and um it's the only one out of

**[14:14]** training and um it's the only one out of this this set that is uniquely good for

**[14:17]** this this set that is uniquely good for

**[14:17]** this this set that is uniquely good for storing blob data or or more importantly

**[14:20]** storing blob data or or more importantly

**[14:20]** storing blob data or or more importantly a mix of uh large blob data and small

**[14:24]** a mix of uh large blob data and small

**[14:24]** a mix of uh large blob data and small like scalar data.

**[14:27]** like scalar data.

**[14:27]** like scalar data. Um and by using Apache arrow as the main

**[14:30]** Um and by using Apache arrow as the main

**[14:30]** Um and by using Apache arrow as the main interface lens format is already

**[14:32]** interface lens format is already

**[14:32]** interface lens format is already compatible with your current data

**[14:34]** compatible with your current data

**[14:34]** compatible with your current data lakeink and and uh lakehouse tools. So

**[14:36]** lakeink and and uh lakehouse tools. So

**[14:36]** lakeink and and uh lakehouse tools. So you can use spark and ray to write very

**[14:40]** you can use spark and ray to write very

**[14:40]** you can use spark and ray to write very large amounts of lance data in a

**[14:42]** large amounts of lance data in a

**[14:42]** large amounts of lance data in a distributed fashion very quickly. U you

**[14:44]** distributed fashion very quickly. U you

**[14:44]** distributed fashion very quickly. U you can use pietorrch to load that data for

**[14:48]** can use pietorrch to load that data for

**[14:48]** can use pietorrch to load that data for training or fine-tuning. Um you can

**[14:50]** training or fine-tuning. Um you can

**[14:50]** training or fine-tuning. Um you can certainly query it using tools like you

**[14:52]** certainly query it using tools like you

**[14:52]** certainly query it using tools like you know p pandas and polars.

**[14:55]** know p pandas and polars.

**[14:55]** know p pandas and polars. All right so

**[14:58]** All right so

**[14:58]** All right so you take back yeah so


### [15:00 - 16:00]

**[15:02]** you take back yeah so

**[15:02]** you take back yeah so we back. Okay. So, uh just wanted to

**[15:06]** we back. Okay. So, uh just wanted to

**[15:06]** we back. Okay. So, uh just wanted to share some general take-home messages

**[15:07]** share some general take-home messages

**[15:08]** share some general take-home messages about building rag for these sort of

**[15:09]** about building rag for these sort of

**[15:09]** about building rag for these sort of large scale domain specific use cases.

**[15:11]** large scale domain specific use cases.

**[15:11]** large scale domain specific use cases. So, the first is that these domain

**[15:13]** So, the first is that these domain

**[15:13]** So, the first is that these domain specific challenges require very

**[15:15]** specific challenges require very

**[15:15]** specific challenges require very creative solutions around understanding

**[15:17]** creative solutions around understanding

**[15:17]** creative solutions around understanding the data and also choosing sort of

**[15:19]** the data and also choosing sort of

**[15:19]** the data and also choosing sort of modeling and infrastructure around that

**[15:20]** modeling and infrastructure around that

**[15:20]** modeling and infrastructure around that like I mentioned about like trying to

**[15:21]** like I mentioned about like trying to

**[15:22]** like I mentioned about like trying to understand structure of your data, what

**[15:23]** understand structure of your data, what

**[15:23]** understand structure of your data, what the use cases are, what the explicit and

**[15:25]** the use cases are, what the explicit and

**[15:25]** the use cases are, what the explicit and implicit query patterns are. Um so,

**[15:27]** implicit query patterns are. Um so,

**[15:28]** implicit query patterns are. Um so, definitely spend time with that, work

**[15:29]** definitely spend time with that, work

**[15:29]** definitely spend time with that, work with domain experts and try to sort of

**[15:31]** with domain experts and try to sort of

**[15:31]** with domain experts and try to sort of immerse yourself as much as possible in

**[15:33]** immerse yourself as much as possible in

**[15:33]** immerse yourself as much as possible in that. Um the second is to make sure

**[15:36]** that. Um the second is to make sure

**[15:36]** that. Um the second is to make sure you're building for iteration speed and

**[15:37]** you're building for iteration speed and

**[15:37]** you're building for iteration speed and flexibility. I think this is a very new

**[15:40]** flexibility. I think this is a very new

**[15:40]** flexibility. I think this is a very new technology, very new industry and a lot

**[15:41]** technology, very new industry and a lot

**[15:41]** technology, very new industry and a lot of things are changing. New tools are

**[15:43]** of things are changing. New tools are

**[15:43]** of things are changing. New tools are coming out, new paradigms, new model

**[15:44]** coming out, new paradigms, new model

**[15:44]** coming out, new paradigms, new model context windows and everything. So you

**[15:46]** context windows and everything. So you

**[15:46]** context windows and everything. So you kind of want to set yourself up for

**[15:48]** kind of want to set yourself up for

**[15:48]** kind of want to set yourself up for flexibility um and iteration speed and

**[15:51]** flexibility um and iteration speed and

**[15:51]** flexibility um and iteration speed and you can kind of ground that in

**[15:52]** you can kind of ground that in

**[15:52]** you can kind of ground that in evaluation where if you have good

**[15:54]** evaluation where if you have good

**[15:54]** evaluation where if you have good evaluation sets or either procedures or

**[15:56]** evaluation sets or either procedures or

**[15:56]** evaluation sets or either procedures or automation around that then you can

**[15:58]** automation around that then you can

**[15:58]** automation around that then you can iterate much faster and just get good


### [16:00 - 17:00]

**[16:00]** iterate much faster and just get good

**[16:00]** iterate much faster and just get good signal on whether your systems are good

**[16:01]** signal on whether your systems are good

**[16:01]** signal on whether your systems are good or accurate. Um so definitely invest

**[16:03]** or accurate. Um so definitely invest

**[16:03]** or accurate. Um so definitely invest time in the evaluation to enable that

**[16:05]** time in the evaluation to enable that

**[16:05]** time in the evaluation to enable that iteration speed. And then yeah the third

**[16:08]** iteration speed. And then yeah the third

**[16:08]** iteration speed. And then yeah the third which John covered is that new data

**[16:10]** which John covered is that new data

**[16:10]** which John covered is that new data infrastructure has to recognize that

**[16:12]** infrastructure has to recognize that

**[16:12]** infrastructure has to recognize that there's sort of this new world we're

**[16:13]** there's sort of this new world we're

**[16:13]** there's sort of this new world we're entering with multimodal data a lot

**[16:16]** entering with multimodal data a lot

**[16:16]** entering with multimodal data a lot heavier on you know vectors and

**[16:18]** heavier on you know vectors and

**[16:18]** heavier on you know vectors and embeddings workloads are very diverse

**[16:20]** embeddings workloads are very diverse

**[16:20]** embeddings workloads are very diverse and the scale is just going to keep

**[16:21]** and the scale is just going to keep

**[16:22]** and the scale is just going to keep getting larger and larger as we try to

**[16:23]** getting larger and larger as we try to

**[16:23]** getting larger and larger as we try to sort of ingest and uh query over all the

**[16:26]** sort of ingest and uh query over all the

**[16:26]** sort of ingest and uh query over all the data that exists public and private.


