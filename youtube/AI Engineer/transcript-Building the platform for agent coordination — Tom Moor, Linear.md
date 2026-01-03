# Building the platform for agent coordination — Tom Moor, Linear

**Video URL:** https://www.youtube.com/watch?v=UG9IAdmi2Dg

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** So yeah, I'm I'm Tom. I uh lead the

**[00:17]** So yeah, I'm I'm Tom. I uh lead the engineering team at Linear. Um, and

**[00:20]** engineering team at Linear. Um, and

**[00:20]** engineering team at Linear. Um, and today I would love to talk to you a bit

**[00:22]** today I would love to talk to you a bit

**[00:22]** today I would love to talk to you a bit about our story with AI, how we think

**[00:25]** about our story with AI, how we think

**[00:25]** about our story with AI, how we think about AI as a company, uh, some of the

**[00:27]** about AI as a company, uh, some of the

**[00:27]** about AI as a company, uh, some of the features we've built, and then how we

**[00:29]** features we've built, and then how we

**[00:29]** features we've built, and then how we see software development going from here

**[00:31]** see software development going from here

**[00:31]** see software development going from here and perhaps Linear's place in that

**[00:33]** and perhaps Linear's place in that

**[00:33]** and perhaps Linear's place in that future.

**[00:36]** future.

**[00:36]** future. Um, so just for anybody that hasn't

**[00:39]** Um, so just for anybody that hasn't

**[00:39]** Um, so just for anybody that hasn't heard of of Linear in the room, um, that

**[00:42]** heard of of Linear in the room, um, that

**[00:42]** heard of of Linear in the room, um, that you might not be familiar. So Linear is

**[00:44]** you might not be familiar. So Linear is

**[00:44]** you might not be familiar. So Linear is a product development tool. Um, it's

**[00:46]** a product development tool. Um, it's

**[00:46]** a product development tool. Um, it's disguised as an issue tracker, we like

**[00:48]** disguised as an issue tracker, we like

**[00:48]** disguised as an issue tracker, we like to say. Um, we spent the last five years

**[00:52]** to say. Um, we spent the last five years

**[00:52]** to say. Um, we spent the last five years obsessing over the speed, clarity,

**[00:55]** obsessing over the speed, clarity,

**[00:55]** obsessing over the speed, clarity, removing friction, making it just the

**[00:57]** removing friction, making it just the

**[00:57]** removing friction, making it just the best tool for IC's um to to use to work


### [01:00 - 02:00]

**[01:01]** best tool for IC's um to to use to work

**[01:01]** best tool for IC's um to to use to work every day. So yeah, it started as a

**[01:03]** every day. So yeah, it started as a

**[01:03]** every day. So yeah, it started as a simple tracker and and now we think of

**[01:05]** simple tracker and and now we think of

**[01:05]** simple tracker and and now we think of it as as an operating system for

**[01:08]** it as as an operating system for

**[01:08]** it as as an operating system for engineering and product teams to to

**[01:10]** engineering and product teams to to

**[01:10]** engineering and product teams to to build their products and we're used by

**[01:14]** build their products and we're used by

**[01:14]** build their products and we're used by openai, ramp, fcel, thousands of other

**[01:18]** openai, ramp, fcel, thousands of other

**[01:18]** openai, ramp, fcel, thousands of other modern software companies you've heard

**[01:20]** modern software companies you've heard

**[01:20]** modern software companies you've heard of um use linear to kind of keep track

**[01:22]** of um use linear to kind of keep track

**[01:22]** of um use linear to kind of keep track of their work.

**[01:25]** of their work.

**[01:25]** of their work. So just a little bit of of history uh of

**[01:28]** So just a little bit of of history uh of

**[01:28]** So just a little bit of of history uh of of our AI journey as it were. Um we spun

**[01:32]** of our AI journey as it were. Um we spun

**[01:32]** of our AI journey as it were. Um we spun up an internal like skunk works team in

**[01:34]** up an internal like skunk works team in

**[01:34]** up an internal like skunk works team in early 2023. Um which I think was about

**[01:38]** early 2023. Um which I think was about

**[01:38]** early 2023. Um which I think was about GPT3 if I remember rightly. Um our

**[01:42]** GPT3 if I remember rightly. Um our

**[01:42]** GPT3 if I remember rightly. Um our initial focus was on kind of

**[01:45]** initial focus was on kind of

**[01:45]** initial focus was on kind of summarization

**[01:46]** summarization

**[01:46]** summarization uh some similarity. We were looking at

**[01:48]** uh some similarity. We were looking at

**[01:48]** uh some similarity. We were looking at embeddings. We nobody on the team had

**[01:50]** embeddings. We nobody on the team had

**[01:50]** embeddings. We nobody on the team had any AI experience. So we're just kind of

**[01:53]** any AI experience. So we're just kind of

**[01:53]** any AI experience. So we're just kind of jumping in and figuring it out as we go.

**[01:55]** jumping in and figuring it out as we go.

**[01:55]** jumping in and figuring it out as we go. Uh one of the things we realized really

**[01:57]** Uh one of the things we realized really

**[01:57]** Uh one of the things we realized really quickly was that uh many of the features


### [02:00 - 03:00]

**[02:00]** quickly was that uh many of the features

**[02:00]** quickly was that uh many of the features that we needed to build needed a really

**[02:01]** that we needed to build needed a really

**[02:01]** that we needed to build needed a really solid search foundation. Um almost

**[02:04]** solid search foundation. Um almost

**[02:04]** solid search foundation. Um almost everything you need to first find the

**[02:06]** everything you need to first find the

**[02:06]** everything you need to first find the relevant stuff, right? So right we had

**[02:09]** relevant stuff, right? So right we had

**[02:09]** relevant stuff, right? So right we had elastic search at that time. Uh and they

**[02:11]** elastic search at that time. Uh and they

**[02:11]** elastic search at that time. Uh and they didn't have a very good vector offering.

**[02:12]** didn't have a very good vector offering.

**[02:12]** didn't have a very good vector offering. I think maybe they actually did have no

**[02:13]** I think maybe they actually did have no

**[02:13]** I think maybe they actually did have no vector offering back in uh 2023. Um so

**[02:16]** vector offering back in uh 2023. Um so

**[02:16]** vector offering back in uh 2023. Um so we looked around and this was kind of a

**[02:18]** we looked around and this was kind of a

**[02:18]** we looked around and this was kind of a moment where there was like a hundred

**[02:20]** moment where there was like a hundred

**[02:20]** moment where there was like a hundred startups suddenly came out with vector

**[02:22]** startups suddenly came out with vector

**[02:22]** startups suddenly came out with vector databases, right? like there's pine

**[02:23]** databases, right? like there's pine

**[02:23]** databases, right? like there's pine cone, there was this, there was that.

**[02:25]** cone, there was this, there was that.

**[02:25]** cone, there was this, there was that. And uh so we looked at these, we

**[02:26]** And uh so we looked at these, we

**[02:26]** And uh so we looked at these, we evaluated a few. They all had a ton of

**[02:28]** evaluated a few. They all had a ton of

**[02:28]** evaluated a few. They all had a ton of trade-offs. Um and so we we literally

**[02:31]** trade-offs. Um and so we we literally

**[02:31]** trade-offs. Um and so we we literally just ended up after experimenting with a

**[02:33]** just ended up after experimenting with a

**[02:33]** just ended up after experimenting with a bunch of things and we had like OpenAI

**[02:35]** bunch of things and we had like OpenAI

**[02:35]** bunch of things and we had like OpenAI embeddings and we stored them in PG

**[02:36]** embeddings and we stored them in PG

**[02:36]** embeddings and we stored them in PG vector and we put the PG vector on GCP

**[02:39]** vector and we put the PG vector on GCP

**[02:39]** vector and we put the PG vector on GCP and it was like the most classic linear

**[02:41]** and it was like the most classic linear

**[02:41]** and it was like the most classic linear decision ever because it was so pra so

**[02:43]** decision ever because it was so pra so

**[02:43]** decision ever because it was so pra so pragmatic and just use use the solid

**[02:46]** pragmatic and just use use the solid

**[02:46]** pragmatic and just use use the solid things. Um so on that base we we shipped

**[02:49]** things. Um so on that base we we shipped

**[02:49]** things. Um so on that base we we shipped some features, right? We shipped a v1 of

**[02:51]** some features, right? We shipped a v1 of

**[02:51]** some features, right? We shipped a v1 of similar issues uh where we're kind of

**[02:53]** similar issues uh where we're kind of

**[02:53]** similar issues uh where we're kind of suggesting related issues. This was like

**[02:55]** suggesting related issues. This was like

**[02:55]** suggesting related issues. This was like in hindsight two years later so naive.

**[02:58]** in hindsight two years later so naive.

**[02:58]** in hindsight two years later so naive. Um we we were just doing simple cosign


### [03:00 - 04:00]

**[03:01]** Um we we were just doing simple cosign

**[03:01]** Um we we were just doing simple cosign embedding op uh comparisons um against

**[03:05]** embedding op uh comparisons um against

**[03:05]** embedding op uh comparisons um against the the vector database

**[03:08]** the the vector database

**[03:08]** the the vector database and we've we shipped natural language

**[03:10]** and we've we shipped natural language

**[03:10]** and we've we shipped natural language filters. I actually think this is one of

**[03:11]** filters. I actually think this is one of

**[03:11]** filters. I actually think this is one of the better ones where um you can just

**[03:13]** the better ones where um you can just

**[03:14]** the better ones where um you can just type in natural language bugs assigned

**[03:15]** type in natural language bugs assigned

**[03:15]** type in natural language bugs assigned to me in the last two weeks that are

**[03:17]** to me in the last two weeks that are

**[03:17]** to me in the last two weeks that are closed and it will produce the filter.

**[03:19]** closed and it will produce the filter.

**[03:19]** closed and it will produce the filter. So it's very oneshot, very naive in

**[03:22]** So it's very oneshot, very naive in

**[03:22]** So it's very oneshot, very naive in comparison. Yeah. But um pretty useful

**[03:25]** comparison. Yeah. But um pretty useful

**[03:25]** comparison. Yeah. But um pretty useful and kind of hidden I would say as well.

**[03:27]** and kind of hidden I would say as well.

**[03:27]** and kind of hidden I would say as well. We also have another feature where if

**[03:28]** We also have another feature where if

**[03:28]** We also have another feature where if you create an issue from a Slack thread,

**[03:31]** you create an issue from a Slack thread,

**[03:31]** you create an issue from a Slack thread, we will um not just pass the text from

**[03:33]** we will um not just pass the text from

**[03:34]** we will um not just pass the text from the Slack message, we will we will try

**[03:35]** the Slack message, we will we will try

**[03:35]** the Slack message, we will we will try and produce the right issue from that

**[03:37]** and produce the right issue from that

**[03:37]** and produce the right issue from that automatically. And that was like so

**[03:39]** automatically. And that was like so

**[03:39]** automatically. And that was like so seamless and hidden that I think a lot

**[03:40]** seamless and hidden that I think a lot

**[03:40]** seamless and hidden that I think a lot of people didn't even realize it was

**[03:41]** of people didn't even realize it was

**[03:42]** of people didn't even realize it was happening. Um and we never shipped a

**[03:44]** happening. Um and we never shipped a

**[03:44]** happening. Um and we never shipped a co-pilot. We tried. it was like it was

**[03:47]** co-pilot. We tried. it was like it was

**[03:47]** co-pilot. We tried. it was like it was co-pilot season and um we just the

**[03:50]** co-pilot season and um we just the

**[03:50]** co-pilot season and um we just the quality wasn't there. You know, we we

**[03:52]** quality wasn't there. You know, we we

**[03:52]** quality wasn't there. You know, we we have this quality bar and it did not

**[03:53]** have this quality bar and it did not

**[03:53]** have this quality bar and it did not reach it. So, um I don't know if it was

**[03:55]** reach it. So, um I don't know if it was

**[03:56]** reach it. So, um I don't know if it was a lack of imagination for our team

**[03:57]** a lack of imagination for our team

**[03:57]** a lack of imagination for our team because we weren't like AI pilled enough

**[03:59]** because we weren't like AI pilled enough

**[03:59]** because we weren't like AI pilled enough at the time or uh it was like the the


### [04:00 - 05:00]

**[04:02]** at the time or uh it was like the the

**[04:02]** at the time or uh it was like the the capability of these early models. I

**[04:03]** capability of these early models. I

**[04:04]** capability of these early models. I think a bit of both to be honest. Um so,

**[04:07]** think a bit of both to be honest. Um so,

**[04:07]** think a bit of both to be honest. Um so, you know, we uh I think this was the

**[04:09]** you know, we uh I think this was the

**[04:09]** you know, we uh I think this was the right approach at the time in a way.

**[04:10]** right approach at the time in a way.

**[04:10]** right approach at the time in a way. Like a lot of people on on Twitter kind

**[04:14]** Like a lot of people on on Twitter kind

**[04:14]** Like a lot of people on on Twitter kind of noticed. They're like, "Oh, these are

**[04:15]** of noticed. They're like, "Oh, these are

**[04:15]** of noticed. They're like, "Oh, these are very seamless features. You're not

**[04:17]** very seamless features. You're not

**[04:17]** very seamless features. You're not slapping AI in our face." Like there was

**[04:20]** slapping AI in our face." Like there was

**[04:20]** slapping AI in our face." Like there was literally toothbrushes that said they

**[04:21]** literally toothbrushes that said they

**[04:21]** literally toothbrushes that said they had AI. Um I think it's probably much

**[04:24]** had AI. Um I think it's probably much

**[04:24]** had AI. Um I think it's probably much worse now to be honest, but you know,

**[04:25]** worse now to be honest, but you know,

**[04:25]** worse now to be honest, but you know, people kind of appreciated this approach

**[04:27]** people kind of appreciated this approach

**[04:27]** people kind of appreciated this approach uh of like small pragmatic value ads.

**[04:30]** uh of like small pragmatic value ads.

**[04:30]** uh of like small pragmatic value ads. And then like fast forward to 2024 and

**[04:33]** And then like fast forward to 2024 and

**[04:33]** And then like fast forward to 2024 and you know, we we we've added a few things

**[04:35]** you know, we we we've added a few things

**[04:35]** you know, we we we've added a few things since then, but it really feels like at

**[04:37]** since then, but it really feels like at

**[04:37]** since then, but it really feels like at 2024, the end of 20 24 we hit a turning

**[04:39]** 2024, the end of 20 24 we hit a turning

**[04:39]** 2024, the end of 20 24 we hit a turning point. um you know O3 coming out the

**[04:42]** point. um you know O3 coming out the

**[04:42]** point. um you know O3 coming out the planning and reasoning models the

**[04:44]** planning and reasoning models the

**[04:44]** planning and reasoning models the multimodal capabilities became available

**[04:47]** multimodal capabilities became available

**[04:47]** multimodal capabilities became available in the APIs the context windows went

**[04:49]** in the APIs the context windows went

**[04:49]** in the APIs the context windows went through the roof uh you know have like

**[04:51]** through the roof uh you know have like

**[04:51]** through the roof uh you know have like million token context like you can do

**[04:53]** million token context like you can do

**[04:53]** million token context like you can do crazy things with that um deepseek of

**[04:56]** crazy things with that um deepseek of

**[04:56]** crazy things with that um deepseek of course made a splash and uh we felt like


### [05:00 - 06:00]

**[05:00]** course made a splash and uh we felt like

**[05:00]** course made a splash and uh we felt like uh some of our experiments started to

**[05:02]** uh some of our experiments started to

**[05:02]** uh some of our experiments started to become a lot less brittle and things

**[05:04]** become a lot less brittle and things

**[05:04]** become a lot less brittle and things actually felt smart um things kind of

**[05:08]** actually felt smart um things kind of

**[05:08]** actually felt smart um things kind of clicked for the team a little bit more

**[05:09]** clicked for the team a little bit more

**[05:09]** clicked for the team a little bit more the we we saw how deep this could go.

**[05:13]** the we we saw how deep this could go.

**[05:13]** the we we saw how deep this could go. So, uh the first thing we did was we

**[05:15]** So, uh the first thing we did was we

**[05:15]** So, uh the first thing we did was we started by uh rebuilding our search

**[05:18]** started by uh rebuilding our search

**[05:18]** started by uh rebuilding our search index again. Um which I don't know if

**[05:20]** index again. Um which I don't know if

**[05:20]** index again. Um which I don't know if you ever like back backfilled like

**[05:23]** you ever like back backfilled like

**[05:23]** you ever like back backfilled like million hundreds of millions of rows of

**[05:25]** million hundreds of millions of rows of

**[05:25]** million hundreds of millions of rows of embeddings. It takes a while. Um so we

**[05:28]** embeddings. It takes a while. Um so we

**[05:28]** embeddings. It takes a while. Um so we moved to a hybrid search approach. This

**[05:29]** moved to a hybrid search approach. This

**[05:29]** moved to a hybrid search approach. This was something that um we we had really

**[05:32]** was something that um we we had really

**[05:32]** was something that um we we had really felt was lacking over like the year and

**[05:34]** felt was lacking over like the year and

**[05:34]** felt was lacking over like the year and a half that we kind of had PG Vector sat

**[05:36]** a half that we kind of had PG Vector sat

**[05:36]** a half that we kind of had PG Vector sat on its own and we weren't um we didn't

**[05:39]** on its own and we weren't um we didn't

**[05:39]** on its own and we weren't um we didn't put it in our main database because it

**[05:40]** put it in our main database because it

**[05:40]** put it in our main database because it was so huge. So it was kind of sat in

**[05:42]** was so huge. So it was kind of sat in

**[05:42]** was so huge. So it was kind of sat in its own thing. So uh we moved to

**[05:44]** its own thing. So uh we moved to

**[05:44]** its own thing. So uh we moved to Turppuffer. If you've not heard of

**[05:45]** Turppuffer. If you've not heard of

**[05:45]** Turppuffer. If you've not heard of Turppuffer, really really cool uh search

**[05:47]** Turppuffer, really really cool uh search

**[05:47]** Turppuffer, really really cool uh search index. I'd highly recommend giving it a

**[05:49]** index. I'd highly recommend giving it a

**[05:49]** index. I'd highly recommend giving it a look. Um and we moved our embeddings

**[05:51]** look. Um and we moved our embeddings

**[05:52]** look. Um and we moved our embeddings over to Coher after doing kind of a

**[05:53]** over to Coher after doing kind of a

**[05:53]** over to Coher after doing kind of a comparison. and we felt that they were a

**[05:54]** comparison. and we felt that they were a

**[05:54]** comparison. and we felt that they were a lot uh a lot better for our domain at

**[05:56]** lot uh a lot better for our domain at

**[05:56]** lot uh a lot better for our domain at least um than than open ais.


### [06:00 - 07:00]

**[06:00]** least um than than open ais.

**[06:00]** least um than than open ais. Um, so this kind of filled a gap in the

**[06:02]** Um, so this kind of filled a gap in the

**[06:02]** Um, so this kind of filled a gap in the surge. Um, and this is actually just

**[06:05]** surge. Um, and this is actually just

**[06:05]** surge. Um, and this is actually just finished rolling out in like the last

**[06:07]** finished rolling out in like the last

**[06:07]** finished rolling out in like the last two weeks um because the the back fill

**[06:10]** two weeks um because the the back fill

**[06:10]** two weeks um because the the back fill took took such a while. But now we

**[06:11]** took took such a while. But now we

**[06:11]** took took such a while. But now we thought we okay, we've got a really

**[06:13]** thought we okay, we've got a really

**[06:13]** thought we okay, we've got a really solid search foundation. What are we

**[06:15]** solid search foundation. What are we

**[06:15]** solid search foundation. What are we going to do with this? Um, so first

**[06:18]** going to do with this? Um, so first

**[06:18]** going to do with this? Um, so first thing we did is like we're building this

**[06:19]** thing we did is like we're building this

**[06:19]** thing we did is like we're building this feature called product intelligence. Um,

**[06:21]** feature called product intelligence. Um,

**[06:21]** feature called product intelligence. Um, this is basically like similar issues

**[06:23]** this is basically like similar issues

**[06:23]** this is basically like similar issues v2. So instead of just doing sim simple

**[06:27]** v2. So instead of just doing sim simple

**[06:27]** v2. So instead of just doing sim simple cosign matching, we now have a pipeline.

**[06:29]** cosign matching, we now have a pipeline.

**[06:29]** cosign matching, we now have a pipeline. um that pipeline is using query

**[06:31]** um that pipeline is using query

**[06:31]** um that pipeline is using query rewriting. It's using the hybrid search

**[06:33]** rewriting. It's using the hybrid search

**[06:33]** rewriting. It's using the hybrid search engine. It's reranking the results.

**[06:35]** engine. It's reranking the results.

**[06:35]** engine. It's reranking the results. We're using deterministic rules. And

**[06:37]** We're using deterministic rules. And

**[06:37]** We're using deterministic rules. And then out the other side um what we get

**[06:40]** then out the other side um what we get

**[06:40]** then out the other side um what we get is a map of relationships from any given

**[06:43]** is a map of relationships from any given

**[06:43]** is a map of relationships from any given issue to its related issues and then how

**[06:46]** issue to its related issues and then how

**[06:46]** issue to its related issues and then how they are related

**[06:48]** they are related

**[06:48]** they are related and and the why they are related. Um and

**[06:51]** and and the why they are related. Um and

**[06:51]** and and the why they are related. Um and then what we're able to do with that is

**[06:53]** then what we're able to do with that is

**[06:53]** then what we're able to do with that is expose this in the product. I hope

**[06:55]** expose this in the product. I hope

**[06:55]** expose this in the product. I hope that's clear enough as you know we have

**[06:57]** that's clear enough as you know we have

**[06:58]** that's clear enough as you know we have suggested suggested labels suggested


### [07:00 - 08:00]

**[07:00]** suggested suggested labels suggested

**[07:00]** suggested suggested labels suggested assignees um possible duplicates and

**[07:03]** assignees um possible duplicates and

**[07:03]** assignees um possible duplicates and then on things like projects it's like

**[07:05]** then on things like projects it's like

**[07:05]** then on things like projects it's like why this might be uh uh why this might

**[07:08]** why this might be uh uh why this might

**[07:08]** why this might be uh uh why this might be the right person to work on this

**[07:09]** be the right person to work on this

**[07:09]** be the right person to work on this issue or why this might be the right

**[07:11]** issue or why this might be the right

**[07:11]** issue or why this might be the right project for this so you know we're

**[07:13]** project for this so you know we're

**[07:13]** project for this so you know we're working with like the open AIs of the

**[07:14]** working with like the open AIs of the

**[07:14]** working with like the open AIs of the world they have thousands of tickets

**[07:16]** world they have thousands of tickets

**[07:16]** world they have thousands of tickets coming in and they really have to have

**[07:17]** coming in and they really have to have

**[07:17]** coming in and they really have to have as much help as possible to to kind of

**[07:19]** as much help as possible to to kind of

**[07:19]** as much help as possible to to kind of churn through them and and get them into

**[07:21]** churn through them and and get them into

**[07:21]** churn through them and and get them into the right the hands of the right

**[07:22]** the right the hands of the right

**[07:22]** the right the hands of the right engineers

**[07:24]** engineers

**[07:24]** engineers Um, oh, I think I skipped one. Yeah. So,

**[07:26]** Um, oh, I think I skipped one. Yeah. So,

**[07:26]** Um, oh, I think I skipped one. Yeah. So, the next one was uh customer feedback

**[07:29]** the next one was uh customer feedback

**[07:29]** the next one was uh customer feedback analysis. This is something we're

**[07:30]** analysis. This is something we're

**[07:30]** analysis. This is something we're working on right now. Um, so one of the

**[07:33]** working on right now. Um, so one of the

**[07:33]** working on right now. Um, so one of the other features of Linear is you can

**[07:34]** other features of Linear is you can

**[07:34]** other features of Linear is you can bring in all of the customer feedback um

**[07:36]** bring in all of the customer feedback um

**[07:36]** bring in all of the customer feedback um from all of your channels and then use

**[07:38]** from all of your channels and then use

**[07:38]** from all of your channels and then use that to help to decide what you're going

**[07:41]** that to help to decide what you're going

**[07:41]** that to help to decide what you're going to build. Um, and so obviously one of

**[07:44]** to build. Um, and so obviously one of

**[07:44]** to build. Um, and so obviously one of the steps there is, okay, we have

**[07:45]** the steps there is, okay, we have

**[07:45]** the steps there is, okay, we have hundreds of pieces of feedback.

**[07:48]** hundreds of pieces of feedback.

**[07:48]** hundreds of pieces of feedback. How do we figure out what to build from

**[07:49]** How do we figure out what to build from

**[07:49]** How do we figure out what to build from this? Right? So uh of course LLMs are

**[07:51]** this? Right? So uh of course LLMs are

**[07:51]** this? Right? So uh of course LLMs are are great at analyzing text and we found

**[07:54]** are great at analyzing text and we found

**[07:54]** are great at analyzing text and we found that um I think our head of product

**[07:57]** that um I think our head of product

**[07:57]** that um I think our head of product actually said that uh our analysis was


### [08:00 - 09:00]

**[08:00]** actually said that uh our analysis was

**[08:00]** actually said that uh our analysis was able to beat 90% of the candidates he

**[08:03]** able to beat 90% of the candidates he

**[08:03]** able to beat 90% of the candidates he talks to in the interview process um for

**[08:05]** talks to in the interview process um for

**[08:05]** talks to in the interview process um for what they're able to do in terms of uh

**[08:07]** what they're able to do in terms of uh

**[08:07]** what they're able to do in terms of uh analysis. So um we're able to yes churn

**[08:10]** analysis. So um we're able to yes churn

**[08:10]** analysis. So um we're able to yes churn through hundreds or thousands of

**[08:11]** through hundreds or thousands of

**[08:11]** through hundreds or thousands of customer requests and then figure out

**[08:12]** customer requests and then figure out

**[08:12]** customer requests and then figure out for this given project like how might we

**[08:15]** for this given project like how might we

**[08:15]** for this given project like how might we split this up? What what features might

**[08:17]** split this up? What what features might

**[08:17]** split this up? What what features might be created from this? um which is pretty

**[08:19]** be created from this? um which is pretty

**[08:19]** be created from this? um which is pretty cool.

**[08:21]** cool.

**[08:21]** cool. Uh another feature we've already shipped

**[08:23]** Uh another feature we've already shipped

**[08:23]** Uh another feature we've already shipped is a daily or weekly pulse. This uh

**[08:25]** is a daily or weekly pulse. This uh

**[08:25]** is a daily or weekly pulse. This uh synthesizes all of the updates that are

**[08:28]** synthesizes all of the updates that are

**[08:28]** synthesizes all of the updates that are happening in your workspace. Um creates

**[08:31]** happening in your workspace. Um creates

**[08:31]** happening in your workspace. Um creates a a pulse from it. Uh like a summarized

**[08:34]** a a pulse from it. Uh like a summarized

**[08:34]** a a pulse from it. Uh like a summarized pulse. Um and then we also produce like

**[08:37]** pulse. Um and then we also produce like

**[08:37]** pulse. Um and then we also produce like an audio podcast version which is pretty

**[08:38]** an audio podcast version which is pretty

**[08:38]** an audio podcast version which is pretty cool because you can uh pull open our

**[08:40]** cool because you can uh pull open our

**[08:40]** cool because you can uh pull open our mobile app and then listen to that on

**[08:41]** mobile app and then listen to that on

**[08:42]** mobile app and then listen to that on your commute. Uh I hope we have an RSS

**[08:43]** your commute. Uh I hope we have an RSS

**[08:44]** your commute. Uh I hope we have an RSS feed for it soon. I really want to just

**[08:45]** feed for it soon. I really want to just

**[08:45]** feed for it soon. I really want to just subscribe to it in a podcast player. Uh,

**[08:47]** subscribe to it in a podcast player. Uh,

**[08:47]** subscribe to it in a podcast player. Uh, so although I put podcasts here, it's

**[08:49]** so although I put podcasts here, it's

**[08:49]** so although I put podcasts here, it's not quite a podcast. You have to have a

**[08:50]** not quite a podcast. You have to have a

**[08:50]** not quite a podcast. You have to have a mobile app or the desktop app. Uh, but

**[08:53]** mobile app or the desktop app. Uh, but

**[08:53]** mobile app or the desktop app. Uh, but this is great. You just like over

**[08:54]** this is great. You just like over

**[08:54]** this is great. You just like over breakfast like what has the team been up

**[08:55]** breakfast like what has the team been up

**[08:55]** breakfast like what has the team been up to? Well, I was asleep. Um,

**[08:59]** to? Well, I was asleep. Um,

**[08:59]** to? Well, I was asleep. Um, oh, that was a uh sorry, that's the


### [09:00 - 10:00]

**[09:01]** oh, that was a uh sorry, that's the

**[09:01]** oh, that was a uh sorry, that's the that's the visual of it. Apologies.

**[09:04]** that's the visual of it. Apologies.

**[09:04]** that's the visual of it. Apologies. Um,

**[09:07]** Um,

**[09:07]** Um, uh, and then yeah, so one other feature

**[09:09]** uh, and then yeah, so one other feature

**[09:09]** uh, and then yeah, so one other feature I'll go through here is um this issue

**[09:13]** I'll go through here is um this issue

**[09:13]** I'll go through here is um this issue from video. So literally

**[09:15]** from video. So literally

**[09:16]** from video. So literally so many bugs can come in as video

**[09:17]** so many bugs can come in as video

**[09:17]** so many bugs can come in as video recordings from customers, right? Drop

**[09:19]** recordings from customers, right? Drop

**[09:19]** recordings from customers, right? Drop the video. Um we'll analyze it. We'll

**[09:22]** the video. Um we'll analyze it. We'll

**[09:22]** the video. Um we'll analyze it. We'll figure out the reproduction steps and

**[09:24]** figure out the reproduction steps and

**[09:24]** figure out the reproduction steps and then we'll create the issue for you uh

**[09:26]** then we'll create the issue for you uh

**[09:26]** then we'll create the issue for you uh from that. Maybe not the finest example

**[09:28]** from that. Maybe not the finest example

**[09:28]** from that. Maybe not the finest example of that feature, but um another kind of

**[09:31]** of that feature, but um another kind of

**[09:31]** of that feature, but um another kind of like seamless but but very powerful and

**[09:33]** like seamless but but very powerful and

**[09:33]** like seamless but but very powerful and saves a bunch of time.

**[09:37]** saves a bunch of time.

**[09:37]** saves a bunch of time. Um so of course we're we're baking as

**[09:39]** Um so of course we're we're baking as

**[09:39]** Um so of course we're we're baking as much into the platform as we can um in

**[09:42]** much into the platform as we can um in

**[09:42]** much into the platform as we can um in terms of these things but uh there's a

**[09:44]** terms of these things but uh there's a

**[09:44]** terms of these things but uh there's a limit to that right we can't put put in

**[09:46]** limit to that right we can't put put in

**[09:46]** limit to that right we can't put put in everything we don't know every team is

**[09:48]** everything we don't know every team is

**[09:48]** everything we don't know every team is different every team is shaped

**[09:49]** different every team is shaped

**[09:49]** different every team is shaped differently so we want to make this

**[09:50]** differently so we want to make this

**[09:50]** differently so we want to make this pluggable um and this is kind of where

**[09:52]** pluggable um and this is kind of where

**[09:52]** pluggable um and this is kind of where agents come in so the way we're thinking

**[09:55]** agents come in so the way we're thinking

**[09:55]** agents come in so the way we're thinking about agents is as infinitely scalable

**[09:57]** about agents is as infinitely scalable

**[09:58]** about agents is as infinitely scalable cloud-based teammates um this is a so we


### [10:00 - 11:00]

**[10:00]** cloud-based teammates um this is a so we

**[10:00]** cloud-based teammates um this is a so we launched a platform for this two weeks

**[10:02]** launched a platform for this two weeks

**[10:02]** launched a platform for this two weeks ago um we figure you know we're already

**[10:05]** ago um we figure you know we're already

**[10:05]** ago um we figure you know we're already doing a pretty good job of orchestrating

**[10:07]** doing a pretty good job of orchestrating

**[10:07]** doing a pretty good job of orchestrating humans. Um, we are a communication tool

**[10:10]** humans. Um, we are a communication tool

**[10:10]** humans. Um, we are a communication tool for humans after all. Um, and if agents

**[10:12]** for humans after all. Um, and if agents

**[10:12]** for humans after all. Um, and if agents are going to be members of your team

**[10:14]** are going to be members of your team

**[10:14]** are going to be members of your team going forward, then they should also

**[10:16]** going forward, then they should also

**[10:16]** going forward, then they should also live in the same place where all of the

**[10:17]** live in the same place where all of the

**[10:17]** live in the same place where all of the the human communication happens. Um, so

**[10:21]** the human communication happens. Um, so

**[10:21]** the human communication happens. Um, so first hopefully if the internet stands

**[10:22]** first hopefully if the internet stands

**[10:22]** first hopefully if the internet stands up, I'm tethering. Um, I'll I'll do some

**[10:25]** up, I'm tethering. Um, I'll I'll do some

**[10:26]** up, I'm tethering. Um, I'll I'll do some I've got some some videos. Uh, yeah. So,

**[10:29]** I've got some some videos. Uh, yeah. So,

**[10:29]** I've got some some videos. Uh, yeah. So, Codegen is one of the first um coding

**[10:32]** Codegen is one of the first um coding

**[10:32]** Codegen is one of the first um coding agents that integrated with us. Um

**[10:36]** agents that integrated with us. Um

**[10:36]** agents that integrated with us. Um so they can is this gonna play? Cool.

**[10:39]** so they can is this gonna play? Cool.

**[10:39]** so they can is this gonna play? Cool. Yeah. So codegen you can assign it, you

**[10:41]** Yeah. So codegen you can assign it, you

**[10:41]** Yeah. So codegen you can assign it, you can mention it um inside of linear like

**[10:43]** can mention it um inside of linear like

**[10:43]** can mention it um inside of linear like any other c any other user and it will

**[10:46]** any other c any other user and it will

**[10:46]** any other c any other user and it will produce plans. It will produce PRs. You

**[10:49]** produce plans. It will produce PRs. You

**[10:49]** produce plans. It will produce PRs. You can see here it's going to pop in. Uh

**[10:52]** can see here it's going to pop in. Uh

**[10:52]** can see here it's going to pop in. Uh this is a sped up by the way that took

**[10:53]** this is a sped up by the way that took

**[10:54]** this is a sped up by the way that took four minutes not 20 seconds. Uh but yes

**[10:56]** four minutes not 20 seconds. Uh but yes

**[10:56]** four minutes not 20 seconds. Uh but yes it will produce the PR. Then you can go

**[10:58]** it will produce the PR. Then you can go

**[10:58]** it will produce the PR. Then you can go and review it like you would any other


### [11:00 - 12:00]

**[11:00]** and review it like you would any other

**[11:00]** and review it like you would any other any other worker uh any other team

**[11:03]** any other worker uh any other team

**[11:03]** any other worker uh any other team member.

**[11:08]** Um this is really powerful by the way

**[11:08]** Um this is really powerful by the way and you can because it's uh an agentic

**[11:11]** and you can because it's uh an agentic

**[11:11]** and you can because it's uh an agentic system in the background you can also

**[11:12]** system in the background you can also

**[11:12]** system in the background you can also interact with it from not just from

**[11:15]** interact with it from not just from

**[11:15]** interact with it from not just from within linear but from within slack or

**[11:17]** within linear but from within slack or

**[11:17]** within linear but from within slack or from other communication tools and you

**[11:19]** from other communication tools and you

**[11:19]** from other communication tools and you can say go and fix this ticket uh and

**[11:21]** can say go and fix this ticket uh and

**[11:21]** can say go and fix this ticket uh and give it a linear issue and it will know

**[11:23]** give it a linear issue and it will know

**[11:23]** give it a linear issue and it will know how to connect it all up um or you'll be

**[11:25]** how to connect it all up um or you'll be

**[11:25]** how to connect it all up um or you'll be able to interrupt it uh part way

**[11:29]** able to interrupt it uh part way

**[11:29]** able to interrupt it uh part way um bucket is a feature flagging platform

**[11:31]** um bucket is a feature flagging platform

**[11:31]** um bucket is a feature flagging platform that that integrated with our the first

**[11:33]** that that integrated with our the first

**[11:33]** that that integrated with our the first version of our um agents uh platform

**[11:36]** version of our um agents uh platform

**[11:36]** version of our um agents uh platform here. Let's see is this going to Oh no.

**[11:40]** here. Let's see is this going to Oh no.

**[11:40]** here. Let's see is this going to Oh no. All righty. Yeah. So in this case you

**[11:42]** All righty. Yeah. So in this case you

**[11:42]** All righty. Yeah. So in this case you can just mention the bucket agent, tell

**[11:43]** can just mention the bucket agent, tell

**[11:44]** can just mention the bucket agent, tell it to create a flag. It will create a

**[11:45]** it to create a flag. It will create a

**[11:45]** it to create a flag. It will create a feature flag for you. You can roll it

**[11:47]** feature flag for you. You can roll it

**[11:47]** feature flag for you. You can roll it out. Um you can check the status of

**[11:49]** out. Um you can check the status of

**[11:50]** out. Um you can check the status of things um all within here. And of course

**[11:52]** things um all within here. And of course

**[11:52]** things um all within here. And of course because it's Aentic, you don't have to

**[11:53]** because it's Aentic, you don't have to

**[11:53]** because it's Aentic, you don't have to go command by command. You could say

**[11:55]** go command by command. You could say

**[11:55]** go command by command. You could say create a new flag, roll it out to 30% of

**[11:57]** create a new flag, roll it out to 30% of

**[11:57]** create a new flag, roll it out to 30% of users. Um and things like that.


### [12:00 - 13:00]

**[12:02]** users. Um and things like that.

**[12:02]** users. Um and things like that. And then Charlie is another coding agent

**[12:04]** And then Charlie is another coding agent

**[12:04]** And then Charlie is another coding agent with access uh to your repository. It's

**[12:06]** with access uh to your repository. It's

**[12:06]** with access uh to your repository. It's really good at creating plans um and

**[12:09]** really good at creating plans um and

**[12:09]** really good at creating plans um and doing like root cause analysis of bugs.

**[12:11]** doing like root cause analysis of bugs.

**[12:11]** doing like root cause analysis of bugs. So in this case uh we have an issue

**[12:14]** So in this case uh we have an issue

**[12:14]** So in this case uh we have an issue here. It has a sentry uh issue attached.

**[12:17]** here. It has a sentry uh issue attached.

**[12:17]** here. It has a sentry uh issue attached. Um we can just uh mention Charlie ask it

**[12:19]** Um we can just uh mention Charlie ask it

**[12:19]** Um we can just uh mention Charlie ask it to do some research. So it can go and

**[12:22]** to do some research. So it can go and

**[12:22]** to do some research. So it can go and look at your recent commits. Um it can

**[12:25]** look at your recent commits. Um it can

**[12:25]** look at your recent commits. Um it can go look through the codebase and it can

**[12:27]** go look through the codebase and it can

**[12:27]** go look through the codebase and it can kind of figure out uh the cause of this

**[12:29]** kind of figure out uh the cause of this

**[12:29]** kind of figure out uh the cause of this issue. And you can imagine immediately

**[12:31]** issue. And you can imagine immediately

**[12:31]** issue. And you can imagine immediately right like this has saved a lot of um of

**[12:34]** right like this has saved a lot of um of

**[12:34]** right like this has saved a lot of um of minutes of engineers time. They can come

**[12:36]** minutes of engineers time. They can come

**[12:36]** minutes of engineers time. They can come in here and immediately see uh possible

**[12:39]** in here and immediately see uh possible

**[12:39]** in here and immediately see uh possible causes and regression reasons for for

**[12:40]** causes and regression reasons for for

**[12:40]** causes and regression reasons for for this issue.

**[12:43]** this issue.

**[12:43]** this issue. Um so the examples I've shown so far

**[12:46]** Um so the examples I've shown so far

**[12:46]** Um so the examples I've shown so far have been uh kind of living in the

**[12:48]** have been uh kind of living in the

**[12:48]** have been uh kind of living in the common area of an issue. Obviously

**[12:50]** common area of an issue. Obviously

**[12:50]** common area of an issue. Obviously that's uh not quite where we want to be

**[12:52]** that's uh not quite where we want to be

**[12:52]** that's uh not quite where we want to be in the long term. So, you know, we're

**[12:54]** in the long term. So, you know, we're

**[12:54]** in the long term. So, you know, we're working uh on build building uh uh

**[12:57]** working uh on build building uh uh

**[12:57]** working uh on build building uh uh additional surfaces for this in the

**[12:59]** additional surfaces for this in the

**[12:59]** additional surfaces for this in the product. Um so that agents aren't just


### [13:00 - 14:00]

**[13:02]** product. Um so that agents aren't just

**[13:02]** product. Um so that agents aren't just like the same as as users on the team.

**[13:04]** like the same as as users on the team.

**[13:04]** like the same as as users on the team. They're they're kind of better because

**[13:06]** They're they're kind of better because

**[13:06]** They're they're kind of better because you can see what they're thinking. Uh

**[13:08]** you can see what they're thinking. Uh

**[13:08]** you can see what they're thinking. Uh and I can't see what my teammates are

**[13:09]** and I can't see what my teammates are

**[13:09]** and I can't see what my teammates are thinking a lot of the time. Um so yeah,

**[13:11]** thinking a lot of the time. Um so yeah,

**[13:12]** thinking a lot of the time. Um so yeah, so we'll we'll have this surface where

**[13:13]** so we'll we'll have this surface where

**[13:13]** so we'll we'll have this surface where the agents can send you their

**[13:14]** the agents can send you their

**[13:14]** the agents can send you their observations. They can send you the

**[13:16]** observations. They can send you the

**[13:16]** observations. They can send you the their tool calls. You're able to kind of

**[13:18]** their tool calls. You're able to kind of

**[13:18]** their tool calls. You're able to kind of go behind the scenes of the agent.

**[13:20]** go behind the scenes of the agent.

**[13:20]** go behind the scenes of the agent. you'll be able to um interrupt it. Um

**[13:23]** you'll be able to um interrupt it. Um

**[13:23]** you'll be able to um interrupt it. Um and then this is kind of consistent

**[13:25]** and then this is kind of consistent

**[13:25]** and then this is kind of consistent across the whole workspace, right? So

**[13:28]** across the whole workspace, right? So

**[13:28]** across the whole workspace, right? So you have different coding agents, you

**[13:30]** you have different coding agents, you

**[13:30]** you have different coding agents, you have PM uh PM agents. Um one other

**[13:33]** have PM uh PM agents. Um one other

**[13:33]** have PM uh PM agents. Um one other company that's building an integration

**[13:35]** company that's building an integration

**[13:35]** company that's building an integration with us right now is intercom with their

**[13:36]** with us right now is intercom with their

**[13:36]** with us right now is intercom with their Finn agent. So you'll be able to do

**[13:38]** Finn agent. So you'll be able to do

**[13:38]** Finn agent. So you'll be able to do things like just say, "Hey Finn, I fixed

**[13:40]** things like just say, "Hey Finn, I fixed

**[13:40]** things like just say, "Hey Finn, I fixed this bug. Can you go and uh can you go

**[13:42]** this bug. Can you go and uh can you go

**[13:42]** this bug. Can you go and uh can you go and reply to the hundred customers that

**[13:43]** and reply to the hundred customers that

**[13:43]** and reply to the hundred customers that reported it?" And you know, how much

**[13:46]** reported it?" And you know, how much

**[13:46]** reported it?" And you know, how much time did that just save? So, we're

**[13:48]** time did that just save? So, we're

**[13:48]** time did that just save? So, we're building this this interface out right

**[13:49]** building this this interface out right

**[13:50]** building this this interface out right now and expect to have it in a couple of

**[13:51]** now and expect to have it in a couple of

**[13:51]** now and expect to have it in a couple of weeks. Um, but I've been really using

**[13:54]** weeks. Um, but I've been really using

**[13:54]** weeks. Um, but I've been really using these features a ton and uh I've been

**[13:57]** these features a ton and uh I've been

**[13:57]** these features a ton and uh I've been hammering this for months and I I I

**[13:58]** hammering this for months and I I I

**[13:58]** hammering this for months and I I I think it it really changes the game and


### [14:00 - 15:00]

**[14:00]** think it it really changes the game and

**[14:00]** think it it really changes the game and we'll expect kind of the amount of bugs

**[14:02]** we'll expect kind of the amount of bugs

**[14:02]** we'll expect kind of the amount of bugs sitting in companies backlogs which we

**[14:04]** sitting in companies backlogs which we

**[14:04]** sitting in companies backlogs which we kind of take for granted that you have

**[14:06]** kind of take for granted that you have

**[14:06]** kind of take for granted that you have this giant backlog that you're never

**[14:07]** this giant backlog that you're never

**[14:07]** this giant backlog that you're never going to get to the bottom of. Um, I

**[14:09]** going to get to the bottom of. Um, I

**[14:09]** going to get to the bottom of. Um, I think there's just not going to be an

**[14:10]** think there's just not going to be an

**[14:10]** think there's just not going to be an excuse for that anymore. Um, the the

**[14:13]** excuse for that anymore. Um, the the

**[14:13]** excuse for that anymore. Um, the the agents can tackle it for you. Um,

**[14:16]** agents can tackle it for you. Um,

**[14:16]** agents can tackle it for you. Um, there's nothing to stop you assigning

**[14:17]** there's nothing to stop you assigning

**[14:17]** there's nothing to stop you assigning every single issue in your backlog out

**[14:19]** every single issue in your backlog out

**[14:19]** every single issue in your backlog out to nation. Have it do a first pass.

**[14:21]** to nation. Have it do a first pass.

**[14:21]** to nation. Have it do a first pass. Maybe 50% of them will be fixed by the

**[14:22]** Maybe 50% of them will be fixed by the

**[14:22]** Maybe 50% of them will be fixed by the end of the week. Um, so I think yes,

**[14:25]** end of the week. Um, so I think yes,

**[14:25]** end of the week. Um, so I think yes, we're really in this world now where you

**[14:27]** we're really in this world now where you

**[14:27]** we're really in this world now where you can build more, you can build higher

**[14:29]** can build more, you can build higher

**[14:29]** can build more, you can build higher quality because more of the grunt work

**[14:31]** quality because more of the grunt work

**[14:31]** quality because more of the grunt work is being done and you can build faster.

**[14:39]** How much time we got? So, uh, I'll just

**[14:39]** How much time we got? So, uh, I'll just talk a little bit about like the

**[14:40]** talk a little bit about like the

**[14:40]** talk a little bit about like the architecture of this. Um so yeah in

**[14:44]** architecture of this. Um so yeah in

**[14:44]** architecture of this. Um so yeah in linear agents are first class users um

**[14:46]** linear agents are first class users um

**[14:46]** linear agents are first class users um they have identity they have history you

**[14:48]** they have identity they have history you

**[14:48]** they have identity they have history you can see everything they do there's a

**[14:50]** can see everything they do there's a

**[14:50]** can see everything they do there's a full audit trail um of those events uh

**[14:53]** full audit trail um of those events uh

**[14:53]** full audit trail um of those events uh you install them via oorthth um and then

**[14:56]** you install them via oorthth um and then

**[14:56]** you install them via oorthth um and then once they're installed kind of any admin

**[14:58]** once they're installed kind of any admin

**[14:58]** once they're installed kind of any admin on the team can manage uh manage that


### [15:00 - 16:00]

**[15:01]** on the team can manage uh manage that

**[15:01]** on the team can manage uh manage that that agent and its access and they work

**[15:04]** that agent and its access and they work

**[15:04]** that agent and its access and they work fully transparently.

**[15:07]** fully transparently.

**[15:07]** fully transparently. Um so we have a very mature GraphQL API

**[15:11]** Um so we have a very mature GraphQL API

**[15:11]** Um so we have a very mature GraphQL API at this point um which basically enables

**[15:14]** at this point um which basically enables

**[15:14]** at this point um which basically enables agents to do anything in the product

**[15:16]** agents to do anything in the product

**[15:16]** agents to do anything in the product that a human could do. Um and granular

**[15:19]** that a human could do. Um and granular

**[15:19]** that a human could do. Um and granular scopes and then we added brand new web

**[15:21]** scopes and then we added brand new web

**[15:21]** scopes and then we added brand new web hooks for this specifically where if you

**[15:23]** hooks for this specifically where if you

**[15:24]** hooks for this specifically where if you are developing an agent with linear um

**[15:27]** are developing an agent with linear um

**[15:27]** are developing an agent with linear um you will get web hooks when events

**[15:29]** you will get web hooks when events

**[15:29]** you will get web hooks when events happen that are specific to your agent.

**[15:31]** happen that are specific to your agent.

**[15:31]** happen that are specific to your agent. So somebody replied to your agent your

**[15:33]** So somebody replied to your agent your

**[15:33]** So somebody replied to your agent your agent was triggered on this issue.

**[15:36]** agent was triggered on this issue.

**[15:36]** agent was triggered on this issue. Uh we also added some additional scopes

**[15:38]** Uh we also added some additional scopes

**[15:38]** Uh we also added some additional scopes that you can opt into to choose whether

**[15:40]** that you can opt into to choose whether

**[15:40]** that you can opt into to choose whether your agent is mentionable or assignable.

**[15:47]** And then as part of that kind of future

**[15:47]** And then as part of that kind of future UI that I just uh showed uh we're also

**[15:50]** UI that I just uh showed uh we're also

**[15:50]** UI that I just uh showed uh we're also working on a new SDK to be released at

**[15:52]** working on a new SDK to be released at

**[15:52]** working on a new SDK to be released at the same time which will just make uh

**[15:54]** the same time which will just make uh

**[15:54]** the same time which will just make uh that really really easy where you can so

**[15:56]** that really really easy where you can so

**[15:56]** that really really easy where you can so right now you can build all this stuff.

**[15:57]** right now you can build all this stuff.

**[15:57]** right now you can build all this stuff. It's on our existing API um and you kind


### [16:00 - 17:00]

**[16:00]** It's on our existing API um and you kind

**[16:00]** It's on our existing API um and you kind of have to figure out a bit more I would

**[16:02]** of have to figure out a bit more I would

**[16:02]** of have to figure out a bit more I would say. So we're kind of building this

**[16:03]** say. So we're kind of building this

**[16:04]** say. So we're kind of building this abstraction layer, this sugar where you

**[16:05]** abstraction layer, this sugar where you

**[16:05]** abstraction layer, this sugar where you can uh very very easily uh integrate

**[16:08]** can uh very very easily uh integrate

**[16:08]** can uh very very easily uh integrate with the platform.

**[16:16]** Uh yeah, I'll finish with some some of

**[16:16]** Uh yeah, I'll finish with some some of the best best practices um that we we

**[16:19]** the best best practices um that we we

**[16:19]** the best best practices um that we we found working with these partners over

**[16:21]** found working with these partners over

**[16:21]** found working with these partners over the last couple of months. Um you know,

**[16:24]** the last couple of months. Um you know,

**[16:24]** the last couple of months. Um you know, it really felt like we're kind of on the

**[16:26]** it really felt like we're kind of on the

**[16:26]** it really felt like we're kind of on the cutting edge here and we're building it

**[16:28]** cutting edge here and we're building it

**[16:28]** cutting edge here and we're building it as the agents themselves still haven't

**[16:30]** as the agents themselves still haven't

**[16:30]** as the agents themselves still haven't launched in a lot of ways. um you know

**[16:32]** launched in a lot of ways. um you know

**[16:32]** launched in a lot of ways. um you know like Google and Codex only just launched

**[16:34]** like Google and Codex only just launched

**[16:34]** like Google and Codex only just launched theirs within the last couple of weeks.

**[16:37]** theirs within the last couple of weeks.

**[16:37]** theirs within the last couple of weeks. Um so first is to be to respond very

**[16:41]** Um so first is to be to respond very

**[16:41]** Um so first is to be to respond very quickly and very precisely um when folks

**[16:45]** quickly and very precisely um when folks

**[16:45]** quickly and very precisely um when folks uh trigger your agent. So if I if I

**[16:47]** uh trigger your agent. So if I if I

**[16:47]** uh trigger your agent. So if I if I mention your agent, it should respond as

**[16:49]** mention your agent, it should respond as

**[16:49]** mention your agent, it should respond as fast as possible. A lot of what we've

**[16:51]** fast as possible. A lot of what we've

**[16:51]** fast as possible. A lot of what we've seen is people using emoji reactions for

**[16:53]** seen is people using emoji reactions for

**[16:53]** seen is people using emoji reactions for that right now. Um excuse me, I have to

**[16:55]** that right now. Um excuse me, I have to

**[16:55]** that right now. Um excuse me, I have to cough.


### [17:00 - 18:00]

**[17:01]** Um yeah so and then respond in a way

**[17:01]** Um yeah so and then respond in a way that kind of like reassures

**[17:04]** that kind of like reassures

**[17:04]** that kind of like reassures uh the user that you the the agent

**[17:07]** uh the user that you the the agent

**[17:07]** uh the user that you the the agent understood the request you know so it's

**[17:08]** understood the request you know so it's

**[17:08]** understood the request you know so it's like if you say at codegen can you take

**[17:11]** like if you say at codegen can you take

**[17:11]** like if you say at codegen can you take care of this the response should be like

**[17:13]** care of this the response should be like

**[17:13]** care of this the response should be like something I will produce a PR for for

**[17:15]** something I will produce a PR for for

**[17:15]** something I will produce a PR for for this specific thing you asked me it's

**[17:17]** this specific thing you asked me it's

**[17:17]** this specific thing you asked me it's like okay you understood what I meant

**[17:18]** like okay you understood what I meant

**[17:18]** like okay you understood what I meant great

**[17:21]** great

**[17:21]** great um inhabit the platform this is like

**[17:23]** um inhabit the platform this is like

**[17:24]** um inhabit the platform this is like linear specific a little bit but um in

**[17:27]** linear specific a little bit but um in

**[17:27]** linear specific a little bit but um in this example but I think it applies

**[17:28]** this example but I think it applies

**[17:28]** this example but I think it applies anywhere. We we really expect that these

**[17:30]** anywhere. We we really expect that these

**[17:30]** anywhere. We we really expect that these agents are not linear agents. They are

**[17:32]** agents are not linear agents. They are

**[17:32]** agents are not linear agents. They are they agents that live in the cloud and

**[17:35]** they agents that live in the cloud and

**[17:35]** they agents that live in the cloud and one of the ways that they interact is

**[17:37]** one of the ways that they interact is

**[17:37]** one of the ways that they interact is through linear, right? Uh it's just

**[17:38]** through linear, right? Uh it's just

**[17:38]** through linear, right? Uh it's just another it's a window into their

**[17:40]** another it's a window into their

**[17:40]** another it's a window into their behavior and hopefully like a a really

**[17:42]** behavior and hopefully like a a really

**[17:42]** behavior and hopefully like a a really well structured one where they get a lot

**[17:44]** well structured one where they get a lot

**[17:44]** well structured one where they get a lot of context. Um but we really think that

**[17:47]** of context. Um but we really think that

**[17:47]** of context. Um but we really think that you know if you're if you're working

**[17:48]** you know if you're if you're working

**[17:48]** you know if you're if you're working within if you're working within Slack,

**[17:49]** within if you're working within Slack,

**[17:50]** within if you're working within Slack, you should use the language of those

**[17:51]** you should use the language of those

**[17:51]** you should use the language of those platforms and and not confuse things and

**[17:53]** platforms and and not confuse things and

**[17:53]** platforms and and not confuse things and put great effort into that. And then um

**[17:57]** put great effort into that. And then um

**[17:57]** put great effort into that. And then um things like one of the things that we

**[17:59]** things like one of the things that we

**[17:59]** things like one of the things that we expect to happen inside of linear is if


### [18:00 - 19:00]

**[18:01]** expect to happen inside of linear is if

**[18:01]** expect to happen inside of linear is if you're working on an issue, you should

**[18:03]** you're working on an issue, you should

**[18:03]** you're working on an issue, you should move that issue to in progress. Don't

**[18:04]** move that issue to in progress. Don't

**[18:04]** move that issue to in progress. Don't just leave it in the backlog. Um you

**[18:06]** just leave it in the backlog. Um you

**[18:06]** just leave it in the backlog. Um you expect that of your teammates and we

**[18:08]** expect that of your teammates and we

**[18:08]** expect that of your teammates and we expect that of agents as well. Um and

**[18:11]** expect that of agents as well. Um and

**[18:11]** expect that of agents as well. Um and then just again like natural behavior.

**[18:13]** then just again like natural behavior.

**[18:13]** then just again like natural behavior. So if if somebody triggered you and then

**[18:16]** So if if somebody triggered you and then

**[18:16]** So if if somebody triggered you and then they replied in that thread, you

**[18:18]** they replied in that thread, you

**[18:18]** they replied in that thread, you shouldn't need to mention the agent

**[18:20]** shouldn't need to mention the agent

**[18:20]** shouldn't need to mention the agent again to get a response. It should be a

**[18:22]** again to get a response. It should be a

**[18:22]** again to get a response. It should be a natural behavior that if you reply to

**[18:24]** natural behavior that if you reply to

**[18:24]** natural behavior that if you reply to them, they will they will respond.

**[18:33]** Um yeah, don't be clever. Uh a lot

**[18:33]** Um yeah, don't be clever. Uh a lot clarify your intent before acting. I

**[18:36]** clarify your intent before acting. I

**[18:36]** clarify your intent before acting. I think we see a lot of like attempts at

**[18:38]** think we see a lot of like attempts at

**[18:38]** think we see a lot of like attempts at oneshots. Um one pattern that we're

**[18:41]** oneshots. Um one pattern that we're

**[18:41]** oneshots. Um one pattern that we're seeing right now coming out of a lot of

**[18:42]** seeing right now coming out of a lot of

**[18:42]** seeing right now coming out of a lot of the coding agents is they'll form a plan

**[18:45]** the coding agents is they'll form a plan

**[18:45]** the coding agents is they'll form a plan um before doing anything um and

**[18:47]** um before doing anything um and

**[18:47]** um before doing anything um and communicate that plan up front and get

**[18:49]** communicate that plan up front and get

**[18:49]** communicate that plan up front and get clarification on it. Uh, so that's

**[18:54]** clarification on it. Uh, so that's

**[18:54]** clarification on it. Uh, so that's something that we definitely expect to

**[18:55]** something that we definitely expect to

**[18:55]** something that we definitely expect to happen.


### [19:00 - 20:00]

**[19:00]** And finally, you know, be sure you're

**[19:00]** And finally, you know, be sure you're you're adding value. Um, I I think, you

**[19:03]** you're adding value. Um, I I think, you

**[19:03]** you're adding value. Um, I I think, you know, LLMs, they they love to just

**[19:05]** know, LLMs, they they love to just

**[19:05]** know, LLMs, they they love to just produce tons of text. We don't want to

**[19:08]** produce tons of text. We don't want to

**[19:08]** produce tons of text. We don't want to see splats straight out of OpenAI into

**[19:11]** see splats straight out of OpenAI into

**[19:11]** see splats straight out of OpenAI into comments, into issues, into any other

**[19:13]** comments, into issues, into any other

**[19:13]** comments, into issues, into any other services. Um, be concise, be useful, be

**[19:16]** services. Um, be concise, be useful, be

**[19:16]** services. Um, be concise, be useful, be like a good teammate would be. Um, you

**[19:19]** like a good teammate would be. Um, you

**[19:19]** like a good teammate would be. Um, you can always fall back on asking like what

**[19:21]** can always fall back on asking like what

**[19:21]** can always fall back on asking like what would a human do in this situation and

**[19:23]** would a human do in this situation and

**[19:24]** would a human do in this situation and try your best to achieve achieve that.

**[19:31]** Cool. That's it. Uh, thanks for

**[19:31]** Cool. That's it. Uh, thanks for listening and if you're interested in

**[19:32]** listening and if you're interested in

**[19:32]** listening and if you're interested in working with us on this platform or uh

**[19:35]** working with us on this platform or uh

**[19:35]** working with us on this platform or uh integrating with Linear, let me know.


