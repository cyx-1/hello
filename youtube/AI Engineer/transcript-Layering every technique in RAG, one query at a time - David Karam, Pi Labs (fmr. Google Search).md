# Layering every technique in RAG, one query at a time - David Karam, Pi Labs (fmr. Google Search)

**Video URL:** https://www.youtube.com/watch?v=w9u11ioHGA0

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** I'll I'll just give you all a little bit

**[00:16]** I'll I'll just give you all a little bit of context. So uh my co-founder and I

**[00:18]** of context. So uh my co-founder and I

**[00:18]** of context. So uh my co-founder and I and a lot of our team were actually

**[00:19]** and a lot of our team were actually

**[00:19]** and a lot of our team were actually working on Google search and then we

**[00:21]** working on Google search and then we

**[00:21]** working on Google search and then we left and like started Pyabs and uh I I

**[00:23]** left and like started Pyabs and uh I I

**[00:23]** left and like started Pyabs and uh I I loved I love the exit talk and like

**[00:25]** loved I love the exit talk and like

**[00:25]** loved I love the exit talk and like we're all nerds for information

**[00:26]** we're all nerds for information

**[00:26]** we're all nerds for information retrieval and search and uh so this is

**[00:29]** retrieval and search and uh so this is

**[00:29]** retrieval and search and uh so this is going to be a little bit of that. Uh

**[00:30]** going to be a little bit of that. Uh

**[00:30]** going to be a little bit of that. Uh just going to go through a whole bunch

**[00:31]** just going to go through a whole bunch

**[00:32]** just going to go through a whole bunch of ways you can actually show up and

**[00:33]** of ways you can actually show up and

**[00:33]** of ways you can actually show up and improve your rack systems. Uh I think

**[00:35]** improve your rack systems. Uh I think

**[00:35]** improve your rack systems. Uh I think one thing that I personally uh sometimes

**[00:37]** one thing that I personally uh sometimes

**[00:37]** one thing that I personally uh sometimes struggle with is there's a lot of talk

**[00:39]** struggle with is there's a lot of talk

**[00:39]** struggle with is there's a lot of talk about things sometimes like too much in

**[00:41]** about things sometimes like too much in

**[00:41]** about things sometimes like too much in the buzzed like oh specific techniques

**[00:43]** the buzzed like oh specific techniques

**[00:43]** the buzzed like oh specific techniques and you can do RL this way and you can

**[00:44]** and you can do RL this way and you can

**[00:44]** and you can do RL this way and you can tune the model this way and it's like

**[00:46]** tune the model this way and it's like

**[00:46]** tune the model this way and it's like doesn't help me orient in the space like

**[00:47]** doesn't help me orient in the space like

**[00:47]** doesn't help me orient in the space like what are all these things and how do I

**[00:49]** what are all these things and how do I

**[00:49]** what are all these things and how do I like hang on them uh or you have the

**[00:51]** like hang on them uh or you have the

**[00:51]** like hang on them uh or you have the complete opposite which is like a whole

**[00:53]** complete opposite which is like a whole

**[00:53]** complete opposite which is like a whole bunch of buzzwords and hype and such and

**[00:54]** bunch of buzzwords and hype and such and

**[00:54]** bunch of buzzwords and hype and such and like rag is dead no rag is not dead is

**[00:56]** like rag is dead no rag is not dead is

**[00:56]** like rag is dead no rag is not dead is like agents like wait what like uh so

**[00:59]** like agents like wait what like uh so

**[00:59]** like agents like wait what like uh so just you know I think a lot of what I'll


### [01:00 - 02:00]

**[01:01]** just you know I think a lot of what I'll

**[01:01]** just you know I think a lot of what I'll do today is just uh what I call like

**[01:02]** do today is just uh what I call like

**[01:02]** do today is just uh what I call like plain English uh just trying to like set

**[01:05]** plain English uh just trying to like set

**[01:05]** plain English uh just trying to like set up a framework right like very centered

**[01:07]** up a framework right like very centered

**[01:07]** up a framework right like very centered around like okay if you are trying to

**[01:08]** around like okay if you are trying to

**[01:08]** around like okay if you are trying to show up the quality of your system how

**[01:09]** show up the quality of your system how

**[01:10]** show up the quality of your system how do you do that and then where do all the

**[01:11]** do you do that and then where do all the

**[01:11]** do you do that and then where do all the things you hear about like day in day

**[01:13]** things you hear about like day in day

**[01:13]** things you hear about like day in day out like fit uh and then just how to

**[01:15]** out like fit uh and then just how to

**[01:15]** out like fit uh and then just how to approach that and give a lot of examples

**[01:17]** approach that and give a lot of examples

**[01:17]** approach that and give a lot of examples I think one thing that I always love and

**[01:19]** I think one thing that I always love and

**[01:19]** I think one thing that I always love and we always did in Google we always do in

**[01:20]** we always did in Google we always do in

**[01:20]** we always did in Google we always do in pyabs uh is just like look at things

**[01:23]** pyabs uh is just like look at things

**[01:23]** pyabs uh is just like look at things look at cases look at queries see what's

**[01:25]** look at cases look at queries see what's

**[01:25]** look at cases look at queries see what's working see what's not working and

**[01:26]** working see what's not working and

**[01:26]** working see what's not working and that's really the essence of like

**[01:27]** that's really the essence of like

**[01:27]** that's really the essence of like quality engineering as we used to call

**[01:29]** quality engineering as we used to call

**[01:29]** quality engineering as we used to call it at Google if you do want the slides

**[01:31]** it at Google if you do want the slides

**[01:31]** it at Google if you do want the slides there's like 50 slides and I said my a

**[01:33]** there's like 50 slides and I said my a

**[01:33]** there's like 50 slides and I said my a challenge for myself to go through 50

**[01:34]** challenge for myself to go through 50

**[01:34]** challenge for myself to go through 50 slides in 19 minutes. Uh but you can

**[01:36]** slides in 19 minutes. Uh but you can

**[01:36]** slides in 19 minutes. Uh but you can catch the slides here if you want. Uh

**[01:37]** catch the slides here if you want. Uh

**[01:37]** catch the slides here if you want. Uh I'll flash this towards the end as well

**[01:39]** I'll flash this towards the end as well

**[01:39]** I'll flash this towards the end as well with pi.ai-talk.

**[01:42]** with pi.ai-talk.

**[01:42]** with pi.ai-talk. Uh it should point to the slides that

**[01:43]** Uh it should point to the slides that

**[01:43]** Uh it should point to the slides that we're going through. And as I mentioned,

**[01:45]** we're going through. And as I mentioned,

**[01:45]** we're going through. And as I mentioned, plain English, no hype, no buzz, uh no

**[01:47]** plain English, no hype, no buzz, uh no

**[01:47]** plain English, no hype, no buzz, uh no debates, no like all right. So how to

**[01:49]** debates, no like all right. So how to

**[01:49]** debates, no like all right. So how to think about techniques before we go

**[01:50]** think about techniques before we go

**[01:50]** think about techniques before we go techniques and get into the weeds of it

**[01:52]** techniques and get into the weeds of it

**[01:52]** techniques and get into the weeds of it like why does this even matter and the

**[01:54]** like why does this even matter and the

**[01:54]** like why does this even matter and the way we always think about it is like

**[01:55]** way we always think about it is like

**[01:56]** way we always think about it is like always start with outcomes. You're

**[01:57]** always start with outcomes. You're

**[01:57]** always start with outcomes. You're always trying to solve some product

**[01:58]** always trying to solve some product

**[01:58]** always trying to solve some product problem. Uh and generally the best way


### [02:00 - 03:00]

**[02:00]** problem. Uh and generally the best way

**[02:00]** problem. Uh and generally the best way to visualize something like this. you

**[02:02]** to visualize something like this. you

**[02:02]** to visualize something like this. you have a certain quality bar you want to

**[02:03]** have a certain quality bar you want to

**[02:03]** have a certain quality bar you want to reach and there were a very interesting

**[02:05]** reach and there were a very interesting

**[02:05]** reach and there were a very interesting talk this this week about like you know

**[02:07]** talk this this week about like you know

**[02:07]** talk this this week about like you know benchmarks aren't really helpful and

**[02:08]** benchmarks aren't really helpful and

**[02:08]** benchmarks aren't really helpful and absolutely eval are helpful you're

**[02:10]** absolutely eval are helpful you're

**[02:10]** absolutely eval are helpful you're trying to launch a CRM agent and you

**[02:12]** trying to launch a CRM agent and you

**[02:12]** trying to launch a CRM agent and you sort of have a launch bar like a place

**[02:13]** sort of have a launch bar like a place

**[02:13]** sort of have a launch bar like a place where you feel comfortable that you can

**[02:14]** where you feel comfortable that you can

**[02:14]** where you feel comfortable that you can actually put it out into the world uh

**[02:16]** actually put it out into the world uh

**[02:16]** actually put it out into the world uh and techniques fit somewhere here you

**[02:19]** and techniques fit somewhere here you

**[02:19]** and techniques fit somewhere here you have that like kind of end metric and

**[02:21]** have that like kind of end metric and

**[02:21]** have that like kind of end metric and you're trying to like come up with

**[02:22]** you're trying to like come up with

**[02:22]** you're trying to like come up with different ways to shore up the quality

**[02:24]** different ways to shore up the quality

**[02:24]** different ways to shore up the quality and those ways are like sort of the

**[02:25]** and those ways are like sort of the

**[02:25]** and those ways are like sort of the techniques there and you know this is

**[02:27]** techniques there and you know this is

**[02:27]** techniques there and you know this is sort of your own personal benchmark you

**[02:29]** sort of your own personal benchmark you

**[02:29]** sort of your own personal benchmark you start with some of the easy the easy the

**[02:31]** start with some of the easy the easy the

**[02:31]** start with some of the easy the easy the easy bars you want to hit and then

**[02:32]** easy bars you want to hit and then

**[02:32]** easy bars you want to hit and then there's like medium benchmarks and hard

**[02:34]** there's like medium benchmarks and hard

**[02:34]** there's like medium benchmarks and hard benchmarks. So these are query sets

**[02:35]** benchmarks. So these are query sets

**[02:35]** benchmarks. So these are query sets you're setting up. Uh and then you know

**[02:37]** you're setting up. Uh and then you know

**[02:37]** you're setting up. Uh and then you know depending on what you want to reach and

**[02:39]** depending on what you want to reach and

**[02:39]** depending on what you want to reach and in at what time frame uh then you end up

**[02:42]** in at what time frame uh then you end up

**[02:42]** in at what time frame uh then you end up trying different things. Uh and this is

**[02:43]** trying different things. Uh and this is

**[02:43]** trying different things. Uh and this is what we call like quality engineering

**[02:45]** what we call like quality engineering

**[02:45]** what we call like quality engineering loop. You sort of like baseline

**[02:46]** loop. You sort of like baseline

**[02:46]** loop. You sort of like baseline yourself. Okay you want to achieve you

**[02:48]** yourself. Okay you want to achieve you

**[02:48]** yourself. Okay you want to achieve you know you want CRM and this is the easy

**[02:50]** know you want CRM and this is the easy

**[02:50]** know you want CRM and this is the easy query set and your quality is there. Uh

**[02:52]** query set and your quality is there. Uh

**[02:52]** query set and your quality is there. Uh just through the simplest way you can

**[02:53]** just through the simplest way you can

**[02:54]** just through the simplest way you can try it. Do a loss analysis. Okay what's

**[02:56]** try it. Do a loss analysis. Okay what's

**[02:56]** try it. Do a loss analysis. Okay what's broken? There were a lot of eval talks

**[02:57]** broken? There were a lot of eval talks

**[02:57]** broken? There were a lot of eval talks this week and then what we call quality

**[02:59]** this week and then what we call quality

**[02:59]** this week and then what we call quality engineering. Now the reason I I I I say


### [03:00 - 04:00]

**[03:01]** engineering. Now the reason I I I I say

**[03:01]** engineering. Now the reason I I I I say this is because like okay techniques fit

**[03:03]** this is because like okay techniques fit

**[03:03]** this is because like okay techniques fit this in this last bucket and one of the

**[03:05]** this in this last bucket and one of the

**[03:05]** this in this last bucket and one of the things that I think biggest problems is

**[03:07]** things that I think biggest problems is

**[03:07]** things that I think biggest problems is like people sometimes start there and it

**[03:09]** like people sometimes start there and it

**[03:09]** like people sometimes start there and it doesn't make any sense because you say

**[03:10]** doesn't make any sense because you say

**[03:10]** doesn't make any sense because you say oh do I need BM25 or do I need like uh

**[03:12]** oh do I need BM25 or do I need like uh

**[03:12]** oh do I need BM25 or do I need like uh vector vector rich people it's like I

**[03:14]** vector vector rich people it's like I

**[03:14]** vector vector rich people it's like I don't know what what are you trying to

**[03:15]** don't know what what are you trying to

**[03:16]** don't know what what are you trying to do and what is your query says and where

**[03:17]** do and what is your query says and where

**[03:17]** do and what is your query says and where are things failing because many times

**[03:19]** are things failing because many times

**[03:19]** are things failing because many times you actually don't need these things and

**[03:20]** you actually don't need these things and

**[03:20]** you actually don't need these things and you end up implementing them it doesn't

**[03:21]** you end up implementing them it doesn't

**[03:21]** you end up implementing them it doesn't make a lot of sense anyway so usually

**[03:24]** make a lot of sense anyway so usually

**[03:24]** make a lot of sense anyway so usually the thing I say is like what I call

**[03:25]** the thing I say is like what I call

**[03:26]** the thing I say is like what I call complexity adjusted impact or you know

**[03:27]** complexity adjusted impact or you know

**[03:28]** complexity adjusted impact or you know stay lazy uh in a sense like always look

**[03:30]** stay lazy uh in a sense like always look

**[03:30]** stay lazy uh in a sense like always look at what's broken and if it's not broken

**[03:31]** at what's broken and if it's not broken

**[03:31]** at what's broken and if it's not broken don't fix it and if it is broken do fix

**[03:33]** don't fix it and if it is broken do fix

**[03:33]** don't fix it and if it is broken do fix it. Uh and we'll go through a lot of

**[03:35]** it. Uh and we'll go through a lot of

**[03:35]** it. Uh and we'll go through a lot of techniques today but like this is a good

**[03:37]** techniques today but like this is a good

**[03:37]** techniques today but like this is a good way to think about them. It's just a

**[03:38]** way to think about them. It's just a

**[03:38]** way to think about them. It's just a cluster. It's a catalog of stuff. The

**[03:40]** cluster. It's a catalog of stuff. The

**[03:40]** cluster. It's a catalog of stuff. The most important two columns are the ones

**[03:42]** most important two columns are the ones

**[03:42]** most important two columns are the ones to the right difficulty and impact and

**[03:44]** to the right difficulty and impact and

**[03:44]** to the right difficulty and impact and if it's easy go ahead and try it. And

**[03:45]** if it's easy go ahead and try it. And

**[03:46]** if it's easy go ahead and try it. And most times like BM25 BM25 is pretty

**[03:48]** most times like BM25 BM25 is pretty

**[03:48]** most times like BM25 BM25 is pretty easy. You should absolutely try it and

**[03:49]** easy. You should absolutely try it and

**[03:49]** easy. You should absolutely try it and does like you know show up your quality

**[03:51]** does like you know show up your quality

**[03:51]** does like you know show up your quality quite a bit. Um but you know should I

**[03:53]** quite a bit. Um but you know should I

**[03:53]** quite a bit. Um but you know should I build like custom embeddings for

**[03:54]** build like custom embeddings for

**[03:54]** build like custom embeddings for retrieval? Like I don't know. Let's take

**[03:56]** retrieval? Like I don't know. Let's take

**[03:56]** retrieval? Like I don't know. Let's take a look. This is actually really really

**[03:57]** a look. This is actually really really

**[03:57]** a look. This is actually really really hard. Uh Harvey gave a talk. They build

**[03:59]** hard. Uh Harvey gave a talk. They build

**[03:59]** hard. Uh Harvey gave a talk. They build custom embeddings but you know they have


### [04:00 - 05:00]

**[04:01]** custom embeddings but you know they have

**[04:01]** custom embeddings but you know they have a really hard problem space and just you

**[04:02]** a really hard problem space and just you

**[04:02]** a really hard problem space and just you know relevance embeddings don't don't do

**[04:04]** know relevance embeddings don't don't do

**[04:04]** know relevance embeddings don't don't do enough for them uh and then they're

**[04:06]** enough for them uh and then they're

**[04:06]** enough for them uh and then they're willing to put all that work and effort.

**[04:08]** willing to put all that work and effort.

**[04:08]** willing to put all that work and effort. All right queries examples let's stuff

**[04:10]** All right queries examples let's stuff

**[04:10]** All right queries examples let's stuff let's first technique in memory

**[04:11]** let's first technique in memory

**[04:12]** let's first technique in memory retrieval uh easiest thing bring all

**[04:14]** retrieval uh easiest thing bring all

**[04:14]** retrieval uh easiest thing bring all your documents shove them all to the

**[04:15]** your documents shove them all to the

**[04:16]** your documents shove them all to the LLM. Uh this is the whole like is rag

**[04:17]** LLM. Uh this is the whole like is rag

**[04:18]** LLM. Uh this is the whole like is rag dead is rag not dead context windows.

**[04:19]** dead is rag not dead context windows.

**[04:19]** dead is rag not dead context windows. Well context windows are pretty easy so

**[04:21]** Well context windows are pretty easy so

**[04:21]** Well context windows are pretty easy so you should definitely start there. Uh

**[04:22]** you should definitely start there. Uh

**[04:22]** you should definitely start there. Uh one example notebook LM uh very nice

**[04:25]** one example notebook LM uh very nice

**[04:25]** one example notebook LM uh very nice product. You actually you know put in

**[04:26]** product. You actually you know put in

**[04:26]** product. You actually you know put in five documents just ask questions about

**[04:28]** five documents just ask questions about

**[04:28]** five documents just ask questions about them. you don't need any rag just shove

**[04:29]** them. you don't need any rag just shove

**[04:29]** them. you don't need any rag just shove the whole thing in. Now questions might

**[04:31]** the whole thing in. Now questions might

**[04:31]** the whole thing in. Now questions might get cut too long and this is where it

**[04:33]** get cut too long and this is where it

**[04:33]** get cut too long and this is where it breaks right maybe things don't fit in

**[04:35]** breaks right maybe things don't fit in

**[04:35]** breaks right maybe things don't fit in memory uh or maybe you just pull the

**[04:37]** memory uh or maybe you just pull the

**[04:37]** memory uh or maybe you just pull the context window too much so this is where

**[04:39]** context window too much so this is where

**[04:39]** context window too much so this is where you start to think things like oh okay

**[04:41]** you start to think things like oh okay

**[04:41]** you start to think things like oh okay that's what's happening I have too many

**[04:42]** that's what's happening I have too many

**[04:42]** that's what's happening I have too many documents oh that's what's happening the

**[04:44]** documents oh that's what's happening the

**[04:44]** documents oh that's what's happening the documents are not attended properly by

**[04:46]** documents are not attended properly by

**[04:46]** documents are not attended properly by the LLM and here are like the five

**[04:48]** the LLM and here are like the five

**[04:48]** the LLM and here are like the five things that are breaking okay great

**[04:49]** things that are breaking okay great

**[04:49]** things that are breaking okay great let's move to the next one so now you

**[04:51]** let's move to the next one so now you

**[04:51]** let's move to the next one so now you try something very simple which is can I

**[04:53]** try something very simple which is can I

**[04:53]** try something very simple which is can I retrieve just based on terms so BM25

**[04:55]** retrieve just based on terms so BM25

**[04:55]** retrieve just based on terms so BM25 what is BM25 BM25 is kind of like four

**[04:57]** what is BM25 BM25 is kind of like four

**[04:57]** what is BM25 BM25 is kind of like four things um query terms frequency of those

**[04:59]** things um query terms frequency of those

**[04:59]** things um query terms frequency of those query terms


### [05:00 - 06:00]

**[05:00]** query terms

**[05:00]** query terms uh length of the document and just how r

**[05:03]** uh length of the document and just how r

**[05:03]** uh length of the document and just how r where a certain term is. It's a very

**[05:05]** where a certain term is. It's a very

**[05:05]** where a certain term is. It's a very nice thing. It actually works pretty

**[05:06]** nice thing. It actually works pretty

**[05:06]** nice thing. It actually works pretty well and it's very easy to try and um it

**[05:11]** well and it's very easy to try and um it

**[05:11]** well and it's very easy to try and um it has a problem that like when things are

**[05:13]** has a problem that like when things are

**[05:13]** has a problem that like when things are not have that nature like the exa as exa

**[05:15]** not have that nature like the exa as exa

**[05:15]** not have that nature like the exa as exa was saying when they don't have that

**[05:16]** was saying when they don't have that

**[05:16]** was saying when they don't have that nature of like a keyword based search

**[05:17]** nature of like a keyword based search

**[05:17]** nature of like a keyword based search they don't work and this is where you

**[05:19]** they don't work and this is where you

**[05:19]** they don't work and this is where you bring in something like relevance

**[05:20]** bring in something like relevance

**[05:20]** bring in something like relevance embeddings and relevance embeddings are

**[05:22]** embeddings and relevance embeddings are

**[05:22]** embeddings and relevance embeddings are pretty interesting because now you're in

**[05:23]** pretty interesting because now you're in

**[05:23]** pretty interesting because now you're in vector space and vector space can handle

**[05:25]** vector space and vector space can handle

**[05:25]** vector space and vector space can handle way more nuance uh than like keyword

**[05:27]** way more nuance uh than like keyword

**[05:27]** way more nuance uh than like keyword space uh but you know they also fail in

**[05:30]** space uh but you know they also fail in

**[05:30]** space uh but you know they also fail in certain ways especially when you're

**[05:31]** certain ways especially when you're

**[05:31]** certain ways especially when you're looking for keyword matching and it's

**[05:33]** looking for keyword matching and it's

**[05:33]** looking for keyword matching and it's actually pretty easy to know when things

**[05:34]** actually pretty easy to know when things

**[05:34]** actually pretty easy to know when things work and when they Actually, this was

**[05:36]** work and when they Actually, this was

**[05:36]** work and when they Actually, this was queried like I went to Chad Gypt and I

**[05:37]** queried like I went to Chad Gypt and I

**[05:37]** queried like I went to Chad Gypt and I asked like, "Hey, give me a bunch of

**[05:38]** asked like, "Hey, give me a bunch of

**[05:38]** asked like, "Hey, give me a bunch of keywords. Ones that work for like

**[05:40]** keywords. Ones that work for like

**[05:40]** keywords. Ones that work for like standard term matching and ones that

**[05:41]** standard term matching and ones that

**[05:41]** standard term matching and ones that work for relevance embedding." And you

**[05:43]** work for relevance embedding." And you

**[05:43]** work for relevance embedding." And you can see like exactly what's going on

**[05:44]** can see like exactly what's going on

**[05:44]** can see like exactly what's going on here, right? If your query stream looks

**[05:46]** here, right? If your query stream looks

**[05:46]** here, right? If your query stream looks like iPhone battery life, then you don't

**[05:49]** like iPhone battery life, then you don't

**[05:49]** like iPhone battery life, then you don't need vector

**[05:51]** need vector

**[05:51]** need vector search. But if they look something like,

**[05:52]** search. But if they look something like,

**[05:52]** search. But if they look something like, "Oh, how long does an iPhone like last

**[05:54]** "Oh, how long does an iPhone like last

**[05:54]** "Oh, how long does an iPhone like last before I need to charge it again?" Then

**[05:55]** before I need to charge it again?" Then

**[05:55]** before I need to charge it again?" Then you absolutely need like things like

**[05:57]** you absolutely need like things like

**[05:57]** you absolutely need like things like vector search. And this is where you

**[05:58]** vector search. And this is where you

**[05:58]** vector search. And this is where you need to be like tuned to what what every


### [06:00 - 07:00]

**[06:00]** need to be like tuned to what what every

**[06:00]** need to be like tuned to what what every technique gives you before you go and

**[06:01]** technique gives you before you go and

**[06:01]** technique gives you before you go and invest in it. And when you do your loss

**[06:03]** invest in it. And when you do your loss

**[06:03]** invest in it. And when you do your loss analysis and you see, oh, most of my

**[06:05]** analysis and you see, oh, most of my

**[06:05]** analysis and you see, oh, most of my queries actually look like the ones on

**[06:06]** queries actually look like the ones on

**[06:06]** queries actually look like the ones on the right hand side, then you should

**[06:08]** the right hand side, then you should

**[06:08]** the right hand side, then you should absolutely start investing in this area.

**[06:10]** absolutely start investing in this area.

**[06:10]** absolutely start investing in this area. All right, now you did BM25, you did

**[06:12]** All right, now you did BM25, you did

**[06:12]** All right, now you did BM25, you did vector because your query sets look

**[06:14]** vector because your query sets look

**[06:14]** vector because your query sets look exactly like that. And now you have

**[06:16]** exactly like that. And now you have

**[06:16]** exactly like that. And now you have conflicted candidate set. And this is

**[06:18]** conflicted candidate set. And this is

**[06:18]** conflicted candidate set. And this is where re-rankers help quite a bit. And

**[06:20]** where re-rankers help quite a bit. And

**[06:20]** where re-rankers help quite a bit. And when people say rerankers, they're

**[06:21]** when people say rerankers, they're

**[06:21]** when people say rerankers, they're usually referring to like cross

**[06:22]** usually referring to like cross

**[06:22]** usually referring to like cross encoders. And this is a specific

**[06:24]** encoders. And this is a specific

**[06:24]** encoders. And this is a specific architecture. If you remember the

**[06:25]** architecture. If you remember the

**[06:25]** architecture. If you remember the architecture here for relevant for the

**[06:27]** architecture here for relevant for the

**[06:27]** architecture here for relevant for the relevance embeddings was you're getting

**[06:28]** relevance embeddings was you're getting

**[06:28]** relevance embeddings was you're getting a vector for the query and you're

**[06:29]** a vector for the query and you're

**[06:29]** a vector for the query and you're getting a vector for document and then

**[06:31]** getting a vector for document and then

**[06:31]** getting a vector for document and then you're just measuring distance. Now

**[06:32]** you're just measuring distance. Now

**[06:32]** you're just measuring distance. Now cross encoders are more sophisticated.

**[06:34]** cross encoders are more sophisticated.

**[06:34]** cross encoders are more sophisticated. They actually take both the query and

**[06:35]** They actually take both the query and

**[06:35]** They actually take both the query and the document and they give you a score

**[06:37]** the document and they give you a score

**[06:37]** the document and they give you a score while attending to both at the same

**[06:39]** while attending to both at the same

**[06:39]** while attending to both at the same time. And that's why they were much more

**[06:41]** time. And that's why they were much more

**[06:41]** time. And that's why they were much more powerful. Now they are more powerful but

**[06:42]** powerful. Now they are more powerful but

**[06:42]** powerful. Now they are more powerful but they're actually pretty expensive. And

**[06:44]** they're actually pretty expensive. And

**[06:44]** they're actually pretty expensive. And now this is a failure state as well. You

**[06:46]** now this is a failure state as well. You

**[06:46]** now this is a failure state as well. You can't do it on all your documents. So

**[06:48]** can't do it on all your documents. So

**[06:48]** can't do it on all your documents. So now you have to have like this fancy

**[06:49]** now you have to have like this fancy

**[06:49]** now you have to have like this fancy thing where you're retrieving a lot of

**[06:50]** thing where you're retrieving a lot of

**[06:50]** thing where you're retrieving a lot of things and then ranking a smaller set of

**[06:52]** things and then ranking a smaller set of

**[06:52]** things and then ranking a smaller set of things with a technique like that. Uh

**[06:55]** things with a technique like that. Uh

**[06:55]** things with a technique like that. Uh but it is really powerful and you should

**[06:57]** but it is really powerful and you should

**[06:57]** but it is really powerful and you should use it and it fails in certain cases and

**[06:59]** use it and it fails in certain cases and

**[06:59]** use it and it fails in certain cases and now when you hit those cases then you


### [07:00 - 08:00]

**[07:01]** now when you hit those cases then you

**[07:01]** now when you hit those cases then you move to the next thing. Now where does

**[07:02]** move to the next thing. Now where does

**[07:02]** move to the next thing. Now where does it fail? Uh it's still relevance and

**[07:05]** it fail? Uh it's still relevance and

**[07:05]** it fail? Uh it's still relevance and there's a big problem with like you know

**[07:06]** there's a big problem with like you know

**[07:06]** there's a big problem with like you know standard embeddings and standard

**[07:07]** standard embeddings and standard

**[07:08]** standard embeddings and standard rerankers. They only measure semantic

**[07:10]** rerankers. They only measure semantic

**[07:10]** rerankers. They only measure semantic similarity and there's a thing like

**[07:12]** similarity and there's a thing like

**[07:12]** similarity and there's a thing like these are all proxy metrics at the end

**[07:13]** these are all proxy metrics at the end

**[07:13]** these are all proxy metrics at the end like your application is your

**[07:14]** like your application is your

**[07:14]** like your application is your application and your set of information

**[07:16]** application and your set of information

**[07:16]** application and your set of information needs as your set of information needs

**[07:17]** needs as your set of information needs

**[07:17]** needs as your set of information needs and you try to proxy with relevance but

**[07:19]** and you try to proxy with relevance but

**[07:19]** and you try to proxy with relevance but relevance is not ranking and this is

**[07:21]** relevance is not ranking and this is

**[07:21]** relevance is not ranking and this is something you know we learned in Google

**[07:22]** something you know we learned in Google

**[07:22]** something you know we learned in Google search sort of uh it's been like 15 20

**[07:25]** search sort of uh it's been like 15 20

**[07:25]** search sort of uh it's been like 15 20 years where you know what brings the

**[07:26]** years where you know what brings the

**[07:26]** years where you know what brings the magic of Google search well they look at

**[07:28]** magic of Google search well they look at

**[07:28]** magic of Google search well they look at a lot of other things than just

**[07:29]** a lot of other things than just

**[07:29]** a lot of other things than just relevance uh and this is you know this

**[07:31]** relevance uh and this is you know this

**[07:31]** relevance uh and this is you know this came from like actually the talk from

**[07:33]** came from like actually the talk from

**[07:33]** came from like actually the talk from Harvey and Lance DB was really really

**[07:34]** Harvey and Lance DB was really really

**[07:34]** Harvey and Lance DB was really really interesting and he gave the example of

**[07:36]** interesting and he gave the example of

**[07:36]** interesting and he gave the example of this query right uh it's a really

**[07:38]** this query right uh it's a really

**[07:38]** this query right uh it's a really interesting query like it's it has so

**[07:40]** interesting query like it's it has so

**[07:40]** interesting query like it's it has so much semantics for the legal uh domain

**[07:43]** much semantics for the legal uh domain

**[07:43]** much semantics for the legal uh domain that it's impossible to catch these with

**[07:45]** that it's impossible to catch these with

**[07:45]** that it's impossible to catch these with just relevance. Um and again what does a

**[07:47]** just relevance. Um and again what does a

**[07:48]** just relevance. Um and again what does a word like regime means? That's a very

**[07:49]** word like regime means? That's a very

**[07:49]** word like regime means? That's a very specific like legal term material. What

**[07:51]** specific like legal term material. What

**[07:51]** specific like legal term material. What does it mean? It actually very has a

**[07:52]** does it mean? It actually very has a

**[07:52]** does it mean? It actually very has a very specific meaning in the legal term.

**[07:54]** very specific meaning in the legal term.

**[07:54]** very specific meaning in the legal term. Uh and then there's like things that are

**[07:56]** Uh and then there's like things that are

**[07:56]** Uh and then there's like things that are very specific to domain that need to be

**[07:57]** very specific to domain that need to be

**[07:57]** very specific to domain that need to be retrieved like laws and regulations and

**[07:59]** retrieved like laws and regulations and

**[07:59]** retrieved like laws and regulations and such. And this is where you get to


### [08:00 - 09:00]

**[08:00]** such. And this is where you get to

**[08:00]** such. And this is where you get to building things like custom embeddings.

**[08:02]** building things like custom embeddings.

**[08:02]** building things like custom embeddings. And you say, you know what, just

**[08:03]** And you say, you know what, just

**[08:03]** And you say, you know what, just fetching on relevance is not enough for

**[08:05]** fetching on relevance is not enough for

**[08:05]** fetching on relevance is not enough for me. And now I need to go and like model

**[08:07]** me. And now I need to go and like model

**[08:07]** me. And now I need to go and like model my own domain in its own vector space.

**[08:10]** my own domain in its own vector space.

**[08:10]** my own domain in its own vector space. And now I can actually fetch some of

**[08:11]** And now I can actually fetch some of

**[08:12]** And now I can actually fetch some of these things. Now again, go back to chat

**[08:13]** these things. Now again, go back to chat

**[08:13]** these things. Now again, go back to chat GPD like is this interesting? Should I

**[08:15]** GPD like is this interesting? Should I

**[08:15]** GPD like is this interesting? Should I actually even do it? So I asked it to

**[08:17]** actually even do it? So I asked it to

**[08:17]** actually even do it? So I asked it to give me a list of things that would fail

**[08:19]** give me a list of things that would fail

**[08:19]** give me a list of things that would fail in a standard relevant search in the

**[08:20]** in a standard relevant search in the

**[08:20]** in a standard relevant search in the legal domain. And you start to see like,

**[08:22]** legal domain. And you start to see like,

**[08:22]** legal domain. And you start to see like, oh, all these things would the words

**[08:24]** oh, all these things would the words

**[08:24]** oh, all these things would the words like moot don't mean the same thing.

**[08:26]** like moot don't mean the same thing.

**[08:26]** like moot don't mean the same thing. Words like material don't mean the same

**[08:28]** Words like material don't mean the same

**[08:28]** Words like material don't mean the same thing. And when you have a vocabulary

**[08:30]** thing. And when you have a vocabulary

**[08:30]** thing. And when you have a vocabulary that is so specific and just off, you

**[08:32]** that is so specific and just off, you

**[08:32]** that is so specific and just off, you will not get good results. Right? So now

**[08:35]** will not get good results. Right? So now

**[08:35]** will not get good results. Right? So now how do you how do you match that? Like

**[08:36]** how do you how do you match that? Like

**[08:36]** how do you how do you match that? Like you need to have again you need to have

**[08:37]** you need to have again you need to have

**[08:38]** you need to have again you need to have evals you need to have query sets. need

**[08:39]** evals you need to have query sets. need

**[08:39]** evals you need to have query sets. need to look at things that are breaking and

**[08:40]** to look at things that are breaking and

**[08:40]** to look at things that are breaking and decide that oh the things that are

**[08:42]** decide that oh the things that are

**[08:42]** decide that oh the things that are breaking have to do with the vocabulary

**[08:44]** breaking have to do with the vocabulary

**[08:44]** breaking have to do with the vocabulary just being out of distribution of a

**[08:46]** just being out of distribution of a

**[08:46]** just being out of distribution of a standard relevance model and that's how

**[08:49]** standard relevance model and that's how

**[08:49]** standard relevance model and that's how you decide right so don't like again

**[08:51]** you decide right so don't like again

**[08:51]** you decide right so don't like again don't think too much about it like oh

**[08:52]** don't think too much about it like oh

**[08:52]** don't think too much about it like oh should I do it should I not do it like

**[08:54]** should I do it should I not do it like

**[08:54]** should I do it should I not do it like what is your what are your queries

**[08:55]** what is your what are your queries

**[08:55]** what is your what are your queries telling you what is your data telling

**[08:56]** telling you what is your data telling

**[08:56]** telling you what is your data telling you and then go and try to do it or not

**[08:58]** you and then go and try to do it or not

**[08:58]** you and then go and try to do it or not do it there's also an example from

**[08:59]** do it there's also an example from


### [09:00 - 10:00]

**[09:00]** do it there's also an example from shopping um so embeddings are very

**[09:03]** shopping um so embeddings are very

**[09:03]** shopping um so embeddings are very interesting because they help you a lot

**[09:04]** interesting because they help you a lot

**[09:04]** interesting because they help you a lot with retrieval and recall uh but you

**[09:06]** with retrieval and recall uh but you

**[09:06]** with retrieval and recall uh but you still good need good ranking right so

**[09:08]** still good need good ranking right so

**[09:08]** still good need good ranking right so now if If if if if you think relevance

**[09:10]** now if If if if if you think relevance

**[09:10]** now if If if if if you think relevance doesn't work with retrieval, it also

**[09:11]** doesn't work with retrieval, it also

**[09:12]** doesn't work with retrieval, it also probably doesn't work with ranking. Uh

**[09:13]** probably doesn't work with ranking. Uh

**[09:13]** probably doesn't work with ranking. Uh this is an example I pulled from

**[09:14]** this is an example I pulled from

**[09:14]** this is an example I pulled from Perplexity. I was trying Yeah, I was

**[09:16]** Perplexity. I was trying Yeah, I was

**[09:16]** Perplexity. I was trying Yeah, I was just trying to break it today. It didn't

**[09:17]** just trying to break it today. It didn't

**[09:17]** just trying to break it today. It didn't take too much to break it. Uh I asked

**[09:19]** take too much to break it. Uh I asked

**[09:19]** take too much to break it. Uh I asked like, "Give me cheap gifts uh for a gift

**[09:20]** like, "Give me cheap gifts uh for a gift

**[09:20]** like, "Give me cheap gifts uh for a gift for my son." And then I follow up with

**[09:22]** for my son." And then I follow up with

**[09:22]** for my son." And then I follow up with this query like, "But I have a budget of

**[09:23]** this query like, "But I have a budget of

**[09:24]** this query like, "But I have a budget of 50 bucks or more because when I said

**[09:25]** 50 bucks or more because when I said

**[09:25]** 50 bucks or more because when I said cheap, it started giving me like $10."

**[09:27]** cheap, it started giving me like $10."

**[09:27]** cheap, it started giving me like $10." Well, you know, cheap for me is like

**[09:28]** Well, you know, cheap for me is like

**[09:28]** Well, you know, cheap for me is like $50. Uh but it didn't know that, so it's

**[09:30]** $50. Uh but it didn't know that, so it's

**[09:30]** $50. Uh but it didn't know that, so it's fine. I told it that. But when I said

**[09:31]** fine. I told it that. But when I said

**[09:31]** fine. I told it that. But when I said $50 or more, it still gave me $15 and

**[09:34]** $50 or more, it still gave me $15 and

**[09:34]** $50 or more, it still gave me $15 and $40, both of which are actually below uh

**[09:36]** $40, both of which are actually below uh

**[09:36]** $40, both of which are actually below uh $50. Uh and this is kind of interesting

**[09:39]** $50. Uh and this is kind of interesting

**[09:39]** $50. Uh and this is kind of interesting right because what we call like in you

**[09:40]** right because what we call like in you

**[09:40]** right because what we call like in you know in standard terms like for

**[09:41]** know in standard terms like for

**[09:41]** know in standard terms like for information retrieval this is a signal

**[09:43]** information retrieval this is a signal

**[09:43]** information retrieval this is a signal it's a price signal and it's not being

**[09:45]** it's a price signal and it's not being

**[09:45]** it's a price signal and it's not being caught and it's not being translated

**[09:46]** caught and it's not being translated

**[09:46]** caught and it's not being translated into the query and it's definitely not

**[09:47]** into the query and it's definitely not

**[09:47]** into the query and it's definitely not being translated into the ranking. So

**[09:49]** being translated into the ranking. So

**[09:49]** being translated into the ranking. So now you have to like think of okay I

**[09:52]** now you have to like think of okay I

**[09:52]** now you have to like think of okay I have ranking and I need the ranking to

**[09:54]** have ranking and I need the ranking to

**[09:54]** have ranking and I need the ranking to see the semantics of my corpus and my

**[09:55]** see the semantics of my corpus and my

**[09:55]** see the semantics of my corpus and my queries and this is has a very specific

**[09:58]** queries and this is has a very specific

**[09:58]** queries and this is has a very specific meaning like when you think of your

**[09:59]** meaning like when you think of your

**[09:59]** meaning like when you think of your corpus and your queries again it's not


### [10:00 - 11:00]

**[10:01]** corpus and your queries again it's not

**[10:01]** corpus and your queries again it's not just relevance relevance helps you with

**[10:02]** just relevance relevance helps you with

**[10:02]** just relevance relevance helps you with natural language but things like price

**[10:04]** natural language but things like price

**[10:04]** natural language but things like price signals things like merchant signals uh

**[10:06]** signals things like merchant signals uh

**[10:06]** signals things like merchant signals uh if you're doing like podcasts how many

**[10:08]** if you're doing like podcasts how many

**[10:08]** if you're doing like podcasts how many times has been listened to is a very

**[10:09]** times has been listened to is a very

**[10:09]** times has been listened to is a very important signal has nothing to do with

**[10:11]** important signal has nothing to do with

**[10:11]** important signal has nothing to do with relevance right and in in in many many

**[10:13]** relevance right and in in in many many

**[10:13]** relevance right and in in in many many applications you will see things that

**[10:15]** applications you will see things that

**[10:15]** applications you will see things that are for example more popular tend to

**[10:17]** are for example more popular tend to

**[10:17]** are for example more popular tend to rank more highly uh and as I talk you

**[10:19]** rank more highly uh and as I talk you

**[10:19]** rank more highly uh and as I talk you mentioned like uh the page rank

**[10:21]** mentioned like uh the page rank

**[10:21]** mentioned like uh the page rank algorithm. Page rank is not about

**[10:22]** algorithm. Page rank is not about

**[10:22]** algorithm. Page rank is not about relevance. It's about prominence. How

**[10:24]** relevance. It's about prominence. How

**[10:24]** relevance. It's about prominence. How many things outside of my uh document

**[10:26]** many things outside of my uh document

**[10:26]** many things outside of my uh document point to me that has nothing to do with

**[10:29]** point to me that has nothing to do with

**[10:29]** point to me that has nothing to do with relevance and everything to do with the

**[10:30]** relevance and everything to do with the

**[10:30]** relevance and everything to do with the structure of the web corpus. So that's

**[10:31]** structure of the web corpus. So that's

**[10:32]** structure of the web corpus. So that's the shape of the data. So this is a

**[10:33]** the shape of the data. So this is a

**[10:33]** the shape of the data. So this is a signal about the shape of the data and

**[10:35]** signal about the shape of the data and

**[10:35]** signal about the shape of the data and not a signal about like the relevance.

**[10:37]** not a signal about like the relevance.

**[10:37]** not a signal about like the relevance. Um and you know best way to think about

**[10:39]** Um and you know best way to think about

**[10:39]** Um and you know best way to think about it think of like you have horizontal

**[10:40]** it think of like you have horizontal

**[10:40]** it think of like you have horizontal semantics and then you have vertical

**[10:41]** semantics and then you have vertical

**[10:41]** semantics and then you have vertical semantics. And if you're in vertical

**[10:43]** semantics. And if you're in vertical

**[10:43]** semantics. And if you're in vertical domain where the semantics are very

**[10:45]** domain where the semantics are very

**[10:45]** domain where the semantics are very verticalized, right? Let's say you're in

**[10:46]** verticalized, right? Let's say you're in

**[10:46]** verticalized, right? Let's say you're in doing a CRM or you're doing emails uh

**[10:49]** doing a CRM or you're doing emails uh

**[10:49]** doing a CRM or you're doing emails uh and it's a very complex bar you're

**[10:51]** and it's a very complex bar you're

**[10:51]** and it's a very complex bar you're trying to hit uh that is way beyond just

**[10:53]** trying to hit uh that is way beyond just

**[10:53]** trying to hit uh that is way beyond just natural language. Understand that

**[10:54]** natural language. Understand that

**[10:54]** natural language. Understand that relevance will be a very tiny tiny part

**[10:56]** relevance will be a very tiny tiny part

**[10:56]** relevance will be a very tiny tiny part of the semantic universe. And the harder

**[10:58]** of the semantic universe. And the harder

**[10:58]** of the semantic universe. And the harder you try to go, the more you're going to

**[10:59]** you try to go, the more you're going to

**[10:59]** you try to go, the more you're going to hit this wall and the more you all right


### [11:00 - 12:00]

**[11:02]** hit this wall and the more you all right

**[11:02]** hit this wall and the more you all right this breaks again. Things keep breaking.

**[11:04]** this breaks again. Things keep breaking.

**[11:04]** this breaks again. Things keep breaking. I'm sorry.

**[11:05]** I'm sorry.

**[11:05]** I'm sorry. At sufficient complexity, things will

**[11:07]** At sufficient complexity, things will

**[11:07]** At sufficient complexity, things will keep breaking. So now the thing that

**[11:08]** keep breaking. So now the thing that

**[11:08]** keep breaking. So now the thing that breaks with even custom semantics is

**[11:11]** breaks with even custom semantics is

**[11:11]** breaks with even custom semantics is user preference. Uh because even when

**[11:13]** user preference. Uh because even when

**[11:13]** user preference. Uh because even when you get to all this, okay, you're saying

**[11:14]** you get to all this, okay, you're saying

**[11:14]** you get to all this, okay, you're saying I'm doing relevance and I'm doing price

**[11:16]** I'm doing relevance and I'm doing price

**[11:16]** I'm doing relevance and I'm doing price signals and merchant signals. I'm doing

**[11:17]** signals and merchant signals. I'm doing

**[11:17]** signals and merchant signals. I'm doing everything. I now I know the shopping

**[11:19]** everything. I now I know the shopping

**[11:19]** everything. I now I know the shopping domain. Now you don't know the shopping

**[11:20]** domain. Now you don't know the shopping

**[11:20]** domain. Now you don't know the shopping domain because now users are using your

**[11:22]** domain because now users are using your

**[11:22]** domain because now users are using your product. They're clicking on stuff you

**[11:24]** product. They're clicking on stuff you

**[11:24]** product. They're clicking on stuff you thought they're not going to click on

**[11:25]** thought they're not going to click on

**[11:25]** thought they're not going to click on and they're clicking they're not

**[11:26]** and they're clicking they're not

**[11:26]** and they're clicking they're not clicking on thoughts on things you

**[11:27]** clicking on thoughts on things you

**[11:28]** clicking on thoughts on things you thought they were going to click on. Uh

**[11:29]** thought they were going to click on. Uh

**[11:29]** thought they were going to click on. Uh and this is where you need to like bring

**[11:31]** and this is where you need to like bring

**[11:31]** and this is where you need to like bring in the click signal, thumbs up, thumbs

**[11:32]** in the click signal, thumbs up, thumbs

**[11:32]** in the click signal, thumbs up, thumbs down signal. Now um these things get

**[11:35]** down signal. Now um these things get

**[11:35]** down signal. Now um these things get very complex. So we're not going to talk

**[11:36]** very complex. So we're not going to talk

**[11:36]** very complex. So we're not going to talk about how to implement them. uh just

**[11:38]** about how to implement them. uh just

**[11:38]** about how to implement them. uh just because again in this case for example

**[11:39]** because again in this case for example

**[11:39]** because again in this case for example you have to build a click-through uh

**[11:41]** you have to build a click-through uh

**[11:41]** you have to build a click-through uh signal prediction signal and then you

**[11:43]** signal prediction signal and then you

**[11:43]** signal prediction signal and then you take that signal and then you combine it

**[11:45]** take that signal and then you combine it

**[11:45]** take that signal and then you combine it with all your other signals. So now if

**[11:46]** with all your other signals. So now if

**[11:46]** with all your other signals. So now if you look at your ranking function it's

**[11:47]** you look at your ranking function it's

**[11:47]** you look at your ranking function it's doing okay I want it to be relevant I

**[11:50]** doing okay I want it to be relevant I

**[11:50]** doing okay I want it to be relevant I wanted to have this like semi-structured

**[11:51]** wanted to have this like semi-structured

**[11:52]** wanted to have this like semi-structured price signal and like query

**[11:54]** price signal and like query

**[11:54]** price signal and like query understanding related to that plus I

**[11:56]** understanding related to that plus I

**[11:56]** understanding related to that plus I want to get the user preference and that

**[11:57]** want to get the user preference and that

**[11:57]** want to get the user preference and that and then you take all these signals and

**[11:58]** and then you take all these signals and

**[11:58]** and then you take all these signals and you add them and that becomes your


### [12:00 - 13:00]

**[12:00]** you add them and that becomes your

**[12:00]** you add them and that becomes your ranking score. So it becomes a very

**[12:01]** ranking score. So it becomes a very

**[12:01]** ranking score. So it becomes a very balanced function. And this is how you

**[12:04]** balanced function. And this is how you

**[12:04]** balanced function. And this is how you go from like oh it's just relevance to

**[12:06]** go from like oh it's just relevance to

**[12:06]** go from like oh it's just relevance to oh no it's not just relevance to oh no

**[12:07]** oh no it's not just relevance to oh no

**[12:08]** oh no it's not just relevance to oh no it's not just relevance and and my

**[12:09]** it's not just relevance and and my

**[12:09]** it's not just relevance and and my semantics and my user preferences all

**[12:12]** semantics and my user preferences all

**[12:12]** semantics and my user preferences all rolled up into one. I'll mention two

**[12:14]** rolled up into one. I'll mention two

**[12:14]** rolled up into one. I'll mention two more things. Uh

**[12:17]** more things. Uh

**[12:17]** more things. Uh you calling the wrong queries. This

**[12:19]** you calling the wrong queries. This

**[12:19]** you calling the wrong queries. This happening a lot because this go this

**[12:20]** happening a lot because this go this

**[12:20]** happening a lot because this go this goes into more orchestration and you're

**[12:22]** goes into more orchestration and you're

**[12:22]** goes into more orchestration and you're trying to do complex things. Uh

**[12:23]** trying to do complex things. Uh

**[12:23]** trying to do complex things. Uh especially now when you have agents uh

**[12:25]** especially now when you have agents uh

**[12:25]** especially now when you have agents uh and you're telling them to use a certain

**[12:26]** and you're telling them to use a certain

**[12:26]** and you're telling them to use a certain tool. This is happening quite a bit

**[12:28]** tool. This is happening quite a bit

**[12:28]** tool. This is happening quite a bit because there is an impedance mismatch

**[12:30]** because there is an impedance mismatch

**[12:30]** because there is an impedance mismatch uh between what the search engine

**[12:32]** uh between what the search engine

**[12:32]** uh between what the search engine expects right let's say you tune the

**[12:34]** expects right let's say you tune the

**[12:34]** expects right let's say you tune the search engine and expects like keyword

**[12:35]** search engine and expects like keyword

**[12:35]** search engine and expects like keyword queries or expects uh you know even like

**[12:37]** queries or expects uh you know even like

**[12:37]** queries or expects uh you know even like more complex queries but you cannot

**[12:39]** more complex queries but you cannot

**[12:39]** more complex queries but you cannot describe all of that to the LM and the

**[12:41]** describe all of that to the LM and the

**[12:41]** describe all of that to the LM and the LM is reasoning about your application

**[12:42]** LM is reasoning about your application

**[12:42]** LM is reasoning about your application and then making queries by itself and

**[12:45]** and then making queries by itself and

**[12:45]** and then making queries by itself and this is a big problem so one thing that

**[12:47]** this is a big problem so one thing that

**[12:47]** this is a big problem so one thing that we've seen many companies do we've done

**[12:48]** we've seen many companies do we've done

**[12:48]** we've seen many companies do we've done this also at Google you actually take

**[12:50]** this also at Google you actually take

**[12:50]** this also at Google you actually take more control of the actual orchestration

**[12:52]** more control of the actual orchestration

**[12:52]** more control of the actual orchestration so you take the big query and you make n

**[12:55]** so you take the big query and you make n

**[12:55]** so you take the big query and you make n smaller queries out of Uh I took the

**[12:57]** smaller queries out of Uh I took the

**[12:57]** smaller queries out of Uh I took the screenshot from AI mode in Google and


### [13:00 - 14:00]

**[13:00]** screenshot from AI mode in Google and

**[13:00]** screenshot from AI mode in Google and it's it's very brief. You have to catch

**[13:01]** it's it's very brief. You have to catch

**[13:01]** it's it's very brief. You have to catch it because after after the animation

**[13:03]** it because after after the animation

**[13:03]** it because after after the animation goes away but you see it's actually it's

**[13:04]** goes away but you see it's actually it's

**[13:04]** goes away but you see it's actually it's making X queries. It's making 15

**[13:06]** making X queries. It's making 15

**[13:06]** making X queries. It's making 15 queries. It's making 20 queries. Um so

**[13:09]** queries. It's making 20 queries. Um so

**[13:09]** queries. It's making 20 queries. Um so what we call fan out take very complex

**[13:10]** what we call fan out take very complex

**[13:10]** what we call fan out take very complex thing try to figure out what all the

**[13:12]** thing try to figure out what all the

**[13:12]** thing try to figure out what all the subqueries in it and then fan them out.

**[13:15]** subqueries in it and then fan them out.

**[13:15]** subqueries in it and then fan them out. Now you might think hey why isn't the LM

**[13:17]** Now you might think hey why isn't the LM

**[13:17]** Now you might think hey why isn't the LM doing it? The LM is kind of doing it but

**[13:18]** doing it? The LM is kind of doing it but

**[13:18]** doing it? The LM is kind of doing it but the LM doesn't know about your tool. It

**[13:19]** the LM doesn't know about your tool. It

**[13:20]** the LM doesn't know about your tool. It doesn't know enough about your search

**[13:21]** doesn't know enough about your search

**[13:21]** doesn't know enough about your search engine. Uh I love MCP but I'm not a big

**[13:23]** engine. Uh I love MCP but I'm not a big

**[13:23]** engine. Uh I love MCP but I'm not a big believer that you can actually teach the

**[13:25]** believer that you can actually teach the

**[13:25]** believer that you can actually teach the LLM and like just through prompting what

**[13:27]** LLM and like just through prompting what

**[13:27]** LLM and like just through prompting what to expect from the search on the other

**[13:29]** to expect from the search on the other

**[13:29]** to expect from the search on the other back end. This is why people still like

**[13:31]** back end. This is why people still like

**[13:31]** back end. This is why people still like oh is it agent autonomous? Do I need to

**[13:33]** oh is it agent autonomous? Do I need to

**[13:33]** oh is it agent autonomous? Do I need to do workflows? This is very very

**[13:35]** do workflows? This is very very

**[13:35]** do workflows? This is very very complicated. Uh and it will take a while

**[13:37]** complicated. Uh and it will take a while

**[13:37]** complicated. Uh and it will take a while for this to be solved because again it's

**[13:39]** for this to be solved because again it's

**[13:39]** for this to be solved because again it's unclear where the boundary is. Is it uh

**[13:41]** unclear where the boundary is. Is it uh

**[13:41]** unclear where the boundary is. Is it uh is it the search engine should be able

**[13:42]** is it the search engine should be able

**[13:42]** is it the search engine should be able to handle more complex things and then

**[13:43]** to handle more complex things and then

**[13:43]** to handle more complex things and then the LLM will just throw anything its way

**[13:45]** the LLM will just throw anything its way

**[13:45]** the LLM will just throw anything its way or is it the other way around? the LM

**[13:47]** or is it the other way around? the LM

**[13:47]** or is it the other way around? the LM has to have more information about what

**[13:48]** has to have more information about what

**[13:48]** has to have more information about what the search engine can support so it can

**[13:51]** the search engine can support so it can

**[13:51]** the search engine can support so it can tailor it and right now you need control

**[13:53]** tailor it and right now you need control

**[13:53]** tailor it and right now you need control because the quality is still not there.

**[13:55]** because the quality is still not there.

**[13:55]** because the quality is still not there. Uh so this looks like this. Um if you

**[13:58]** Uh so this looks like this. Um if you

**[13:58]** Uh so this looks like this. Um if you have sort of like this assistant input

**[13:59]** have sort of like this assistant input

**[13:59]** have sort of like this assistant input and you're turning it in these narrow


### [14:00 - 15:00]

**[14:01]** and you're turning it in these narrow

**[14:01]** and you're turning it in these narrow queries like for example was David

**[14:02]** queries like for example was David

**[14:02]** queries like for example was David working on this has very very specific

**[14:04]** working on this has very very specific

**[14:04]** working on this has very very specific semantics and it's more like oh JC is

**[14:06]** semantics and it's more like oh JC is

**[14:06]** semantics and it's more like oh JC is David Slack threads David. Uh and it's

**[14:09]** David Slack threads David. Uh and it's

**[14:09]** David Slack threads David. Uh and it's very very hard to know without knowing

**[14:11]** very very hard to know without knowing

**[14:11]** very very hard to know without knowing enough about your application that these

**[14:12]** enough about your application that these

**[14:12]** enough about your application that these are the queries that matter and not on

**[14:14]** are the queries that matter and not on

**[14:14]** are the queries that matter and not on the the ones on the left hand side. And

**[14:15]** the the ones on the left hand side. And

**[14:15]** the the ones on the left hand side. And if you send the thing on the left hand

**[14:16]** if you send the thing on the left hand

**[14:16]** if you send the thing on the left hand side to a search engine, it will

**[14:18]** side to a search engine, it will

**[14:18]** side to a search engine, it will absolutely tip over unless it

**[14:19]** absolutely tip over unless it

**[14:20]** absolutely tip over unless it understands your domain. And this is

**[14:21]** understands your domain. And this is

**[14:21]** understands your domain. And this is where like you know you need to

**[14:22]** where like you know you need to

**[14:22]** where like you know you need to calibrate the boundary.

**[14:25]** calibrate the boundary.

**[14:25]** calibrate the boundary. Okay. So now you're asking all the right

**[14:26]** Okay. So now you're asking all the right

**[14:26]** Okay. So now you're asking all the right queries. Are you asking to all the right

**[14:27]** queries. Are you asking to all the right

**[14:27]** queries. Are you asking to all the right backends? And this is another place

**[14:29]** backends? And this is another place

**[14:29]** backends? And this is another place where it all fails. Um and this is what

**[14:31]** where it all fails. Um and this is what

**[14:31]** where it all fails. Um and this is what we call like one technique we call

**[14:33]** we call like one technique we call

**[14:33]** we call like one technique we call supplementary retrieval. This is

**[14:34]** supplementary retrieval. This is

**[14:34]** supplementary retrieval. This is something you notice like clients do

**[14:35]** something you notice like clients do

**[14:35]** something you notice like clients do quite a bit which is they don't call

**[14:37]** quite a bit which is they don't call

**[14:37]** quite a bit which is they don't call search enough. Uh and sometimes people

**[14:39]** search enough. Uh and sometimes people

**[14:39]** search enough. Uh and sometimes people try to overoptimize. When you're trying

**[14:41]** try to overoptimize. When you're trying

**[14:41]** try to overoptimize. When you're trying to get high call, you should always be

**[14:43]** to get high call, you should always be

**[14:43]** to get high call, you should always be searching more. Like I always like just

**[14:45]** searching more. Like I always like just

**[14:45]** searching more. Like I always like just search more like this is similar to when

**[14:46]** search more like this is similar to when

**[14:46]** search more like this is similar to when we talked like about dynamic content

**[14:47]** we talked like about dynamic content

**[14:47]** we talked like about dynamic content like the in-memory uh retrieval just

**[14:50]** like the in-memory uh retrieval just

**[14:50]** like the in-memory uh retrieval just like just give more things. So it never

**[14:53]** like just give more things. So it never

**[14:53]** like just give more things. So it never fails to give more things. I know in the

**[14:54]** fails to give more things. I know in the

**[14:54]** fails to give more things. I know in the in the description we said like there

**[14:55]** in the description we said like there

**[14:56]** in the description we said like there was this query fell which was really

**[14:57]** was this query fell which was really

**[14:57]** was this query fell which was really hard to uh to do and then you think like


### [15:00 - 16:00]

**[15:00]** hard to uh to do and then you think like

**[15:00]** hard to uh to do and then you think like oh we're in Google search and it's very

**[15:01]** oh we're in Google search and it's very

**[15:01]** oh we're in Google search and it's very simple Middle Eastern dish and it

**[15:03]** simple Middle Eastern dish and it

**[15:03]** simple Middle Eastern dish and it stumped an organization of 6,000 people

**[15:05]** stumped an organization of 6,000 people

**[15:05]** stumped an organization of 6,000 people like oh my god what's so hard about this

**[15:06]** like oh my god what's so hard about this

**[15:06]** like oh my god what's so hard about this query? What's so hard about this query

**[15:08]** query? What's so hard about this query

**[15:08]** query? What's so hard about this query is like it's it's it's an ambiguous

**[15:09]** is like it's it's it's an ambiguous

**[15:09]** is like it's it's it's an ambiguous intent. uh so you need to reach to a lot

**[15:11]** intent. uh so you need to reach to a lot

**[15:11]** intent. uh so you need to reach to a lot of backends to actually understand

**[15:13]** of backends to actually understand

**[15:13]** of backends to actually understand enough about it right because you might

**[15:15]** enough about it right because you might

**[15:15]** enough about it right because you might be asking about food at which point I

**[15:16]** be asking about food at which point I

**[15:16]** be asking about food at which point I want to show you restaurants you might

**[15:17]** want to show you restaurants you might

**[15:18]** want to show you restaurants you might be asking this for for pictures at which

**[15:19]** be asking this for for pictures at which

**[15:19]** be asking this for for pictures at which point I want to show you images uh now

**[15:21]** point I want to show you images uh now

**[15:21]** point I want to show you images uh now what Google ended up doing is that they

**[15:22]** what Google ended up doing is that they

**[15:22]** what Google ended up doing is that they ask they you know create all the

**[15:24]** ask they you know create all the

**[15:24]** ask they you know create all the backends and then they put the whole

**[15:25]** backends and then they put the whole

**[15:25]** backends and then they put the whole thing in and I think you know I would

**[15:27]** thing in and I think you know I would

**[15:27]** thing in and I think you know I would recommend like this is a great technique

**[15:29]** recommend like this is a great technique

**[15:29]** recommend like this is a great technique to just even increase the recall more

**[15:31]** to just even increase the recall more

**[15:31]** to just even increase the recall more just call more things um and don't try

**[15:34]** just call more things um and don't try

**[15:34]** just call more things um and don't try to be skimpy unless you're running

**[15:35]** to be skimpy unless you're running

**[15:35]** to be skimpy unless you're running through like some real cost overload and

**[15:38]** through like some real cost overload and

**[15:38]** through like some real cost overload and that's the last one you're running into

**[15:40]** that's the last one you're running into

**[15:40]** that's the last one you're running into cost overloads. GPUs are melting. I try

**[15:42]** cost overloads. GPUs are melting. I try

**[15:42]** cost overloads. GPUs are melting. I try to generate an image, but then I

**[15:43]** to generate an image, but then I

**[15:43]** to generate an image, but then I realized there actually a pretty good

**[15:44]** realized there actually a pretty good

**[15:44]** realized there actually a pretty good image that is real. Somebody took a

**[15:46]** image that is real. Somebody took a

**[15:46]** image that is real. Somebody took a server rack and threw it from the roof.

**[15:48]** server rack and threw it from the roof.

**[15:48]** server rack and threw it from the roof. Um, this was like I didn't need to go to

**[15:51]** Um, this was like I didn't need to go to

**[15:51]** Um, this was like I didn't need to go to ChatG and generate this image. Uh,

**[15:53]** ChatG and generate this image. Uh,

**[15:53]** ChatG and generate this image. Uh, apparently this was an advertisement.

**[15:55]** apparently this was an advertisement.

**[15:55]** apparently this was an advertisement. Pretty expensive one. Um, all right. So,

**[15:58]** Pretty expensive one. Um, all right. So,

**[15:58]** Pretty expensive one. Um, all right. So, this happens a lot like when you get to


### [16:00 - 17:00]

**[16:00]** this happens a lot like when you get to

**[16:00]** this happens a lot like when you get to a certain scale and you have all these

**[16:01]** a certain scale and you have all these

**[16:01]** a certain scale and you have all these backends and you're making all these

**[16:02]** backends and you're making all these

**[16:02]** backends and you're making all these queries and it's just getting very very

**[16:04]** queries and it's just getting very very

**[16:04]** queries and it's just getting very very complex and this, you know, I mean

**[16:06]** complex and this, you know, I mean

**[16:06]** complex and this, you know, I mean Google's there, perplexity is there. I

**[16:08]** Google's there, perplexity is there. I

**[16:08]** Google's there, perplexity is there. I mean Sam Alman keeps keeps complaining

**[16:09]** mean Sam Alman keeps keeps complaining

**[16:09]** mean Sam Alman keeps keeps complaining about GPUs melting. Um I think this is

**[16:12]** about GPUs melting. Um I think this is

**[16:12]** about GPUs melting. Um I think this is the part where like you need to start

**[16:13]** the part where like you need to start

**[16:13]** the part where like you need to start doing distillation and distillation is a

**[16:16]** doing distillation and distillation is a

**[16:16]** doing distillation and distillation is a very interesting thing because like to

**[16:17]** very interesting thing because like to

**[16:17]** very interesting thing because like to do that you have to learn how to

**[16:18]** do that you have to learn how to

**[16:18]** do that you have to learn how to fine-tune models and this this gets to

**[16:20]** fine-tune models and this this gets to

**[16:20]** fine-tune models and this this gets to be a little bit complex. You sort of

**[16:21]** be a little bit complex. You sort of

**[16:21]** be a little bit complex. You sort of have to hold the quality bar constant

**[16:23]** have to hold the quality bar constant

**[16:23]** have to hold the quality bar constant while you decrease the size of the

**[16:24]** while you decrease the size of the

**[16:24]** while you decrease the size of the model. U the reason you can do that like

**[16:26]** model. U the reason you can do that like

**[16:26]** model. U the reason you can do that like is is is kind of like in that in that

**[16:28]** is is is kind of like in that in that

**[16:28]** is is is kind of like in that in that graph like hey hire me I know everything

**[16:30]** graph like hey hire me I know everything

**[16:30]** graph like hey hire me I know everything actually I'm firing you. uh it's

**[16:32]** actually I'm firing you. uh it's

**[16:32]** actually I'm firing you. uh it's overqualified like an LLM a very like

**[16:34]** overqualified like an LLM a very like

**[16:34]** overqualified like an LLM a very like large language model is actually over

**[16:36]** large language model is actually over

**[16:36]** large language model is actually over mostly overqualified for the task you

**[16:38]** mostly overqualified for the task you

**[16:38]** mostly overqualified for the task you want to do uh because what you really

**[16:40]** want to do uh because what you really

**[16:40]** want to do uh because what you really want to do is just one thing like

**[16:41]** want to do is just one thing like

**[16:41]** want to do is just one thing like perplexity they're they're doing

**[16:43]** perplexity they're they're doing

**[16:43]** perplexity they're they're doing question answering uh and they're pretty

**[16:45]** question answering uh and they're pretty

**[16:45]** question answering uh and they're pretty fast I mean when you use perplexity in

**[16:46]** fast I mean when you use perplexity in

**[16:46]** fast I mean when you use perplexity in certain context they're really really

**[16:47]** certain context they're really really

**[16:47]** certain context they're really really fast which is amazing because they

**[16:49]** fast which is amazing because they

**[16:49]** fast which is amazing because they trained this one model to do this one

**[16:50]** trained this one model to do this one

**[16:50]** trained this one model to do this one very specific thing which is just be

**[16:52]** very specific thing which is just be

**[16:52]** very specific thing which is just be really really good at question answering

**[16:55]** really really good at question answering

**[16:55]** really really good at question answering um and you know this is very hard so I

**[16:57]** um and you know this is very hard so I

**[16:57]** um and you know this is very hard so I wouldn't do it unless you know latency

**[16:59]** wouldn't do it unless you know latency

**[16:59]** wouldn't do it unless you know latency becomes a really important thing for


### [17:00 - 18:00]

**[17:00]** becomes a really important thing for

**[17:00]** becomes a really important thing for your users right like, oh, the thing is

**[17:02]** your users right like, oh, the thing is

**[17:02]** your users right like, oh, the thing is taking 10 seconds. Users churn. If I can

**[17:04]** taking 10 seconds. Users churn. If I can

**[17:04]** taking 10 seconds. Users churn. If I can make it in two seconds, users don't

**[17:05]** make it in two seconds, users don't

**[17:06]** make it in two seconds, users don't churn. Actually, that's a really great

**[17:07]** churn. Actually, that's a really great

**[17:07]** churn. Actually, that's a really great place to be because then you can use

**[17:08]** place to be because then you can use

**[17:08]** place to be because then you can use this technique and like just bring

**[17:09]** this technique and like just bring

**[17:09]** this technique and like just bring everything down. Um, all right. You've

**[17:12]** everything down. Um, all right. You've

**[17:12]** everything down. Um, all right. You've done everything you can. Things are

**[17:14]** done everything you can. Things are

**[17:14]** done everything you can. Things are still failing. This is uh everybody.

**[17:17]** still failing. This is uh everybody.

**[17:17]** still failing. This is uh everybody. Okay. What do you do? Like we have a

**[17:18]** Okay. What do you do? Like we have a

**[17:18]** Okay. What do you do? Like we have a bunch of engineers here. What do you do

**[17:20]** bunch of engineers here. What do you do

**[17:20]** bunch of engineers here. What do you do when everything fails? Um, yes. You you

**[17:23]** when everything fails? Um, yes. You you

**[17:23]** when everything fails? Um, yes. You you blame the product manager. It's

**[17:26]** blame the product manager. It's

**[17:26]** blame the product manager. It's it's the last trick in the book. Uh,

**[17:28]** it's the last trick in the book. Uh,

**[17:28]** it's the last trick in the book. Uh, when everything fails, uh, make sure

**[17:30]** when everything fails, uh, make sure

**[17:30]** when everything fails, uh, make sure it's not your fault. But I'll say

**[17:32]** it's not your fault. But I'll say

**[17:32]** it's not your fault. But I'll say there's something really important here.

**[17:34]** there's something really important here.

**[17:34]** there's something really important here. Quality engineering will never like

**[17:35]** Quality engineering will never like

**[17:35]** Quality engineering will never like it'll never be 100%. Things will always

**[17:37]** it'll never be 100%. Things will always

**[17:37]** it'll never be 100%. Things will always fail. These are stocastic systems. So

**[17:39]** fail. These are stocastic systems. So

**[17:39]** fail. These are stocastic systems. So then you have to punt the problem. You

**[17:40]** then you have to punt the problem. You

**[17:40]** then you have to punt the problem. You have to punt it upwards. So it's it's

**[17:41]** have to punt it upwards. So it's it's

**[17:42]** have to punt it upwards. So it's it's kind of a joke, but it's not a joke.

**[17:43]** kind of a joke, but it's not a joke.

**[17:43]** kind of a joke, but it's not a joke. Like the design of the product matters a

**[17:45]** Like the design of the product matters a

**[17:45]** Like the design of the product matters a lot to how much how magical it can seem

**[17:47]** lot to how much how magical it can seem

**[17:48]** lot to how much how magical it can seem because if you try to be more magical

**[17:49]** because if you try to be more magical

**[17:49]** because if you try to be more magical than your product surface uh can can

**[17:51]** than your product surface uh can can

**[17:51]** than your product surface uh can can absorb, you will you'll run into into a

**[17:53]** absorb, you will you'll run into into a

**[17:53]** absorb, you will you'll run into into a bunch of problems. Um this is I use a

**[17:55]** bunch of problems. Um this is I use a

**[17:55]** bunch of problems. Um this is I use a very simple example. Uh probably a more

**[17:57]** very simple example. Uh probably a more

**[17:57]** very simple example. Uh probably a more complex one would be uh sort of a human

**[17:59]** complex one would be uh sort of a human

**[17:59]** complex one would be uh sort of a human in the loop for customer support where


### [18:00 - 19:00]

**[18:01]** in the loop for customer support where

**[18:01]** in the loop for customer support where you're like okay some cases the bot can

**[18:03]** you're like okay some cases the bot can

**[18:03]** you're like okay some cases the bot can handle by its own but then you need to

**[18:04]** handle by its own but then you need to

**[18:04]** handle by its own but then you need to like punt to a human. This is basically

**[18:06]** like punt to a human. This is basically

**[18:06]** like punt to a human. This is basically UX design right like when when do you

**[18:08]** UX design right like when when do you

**[18:08]** UX design right like when when do you trust the machine to do what the machine

**[18:09]** trust the machine to do what the machine

**[18:10]** trust the machine to do what the machine needs to do and when does a human need

**[18:11]** needs to do and when does a human need

**[18:11]** needs to do and when does a human need to be in the loop. This is a much

**[18:13]** to be in the loop. This is a much

**[18:13]** to be in the loop. This is a much simpler example from like Google

**[18:14]** simpler example from like Google

**[18:14]** simpler example from like Google shopping. Um there's some cases where

**[18:16]** shopping. Um there's some cases where

**[18:16]** shopping. Um there's some cases where Google has a lot of great data. So what

**[18:18]** Google has a lot of great data. So what

**[18:18]** Google has a lot of great data. So what we call like high understanding the

**[18:19]** we call like high understanding the

**[18:20]** we call like high understanding the fidelity of the understanding is really

**[18:21]** fidelity of the understanding is really

**[18:21]** fidelity of the understanding is really high and then it shows like what we call

**[18:23]** high and then it shows like what we call

**[18:23]** high and then it shows like what we call a high promise UI. Like I'll show you

**[18:24]** a high promise UI. Like I'll show you

**[18:24]** a high promise UI. Like I'll show you things you can click on them. There's

**[18:26]** things you can click on them. There's

**[18:26]** things you can click on them. There's reviews, there's filters because I just

**[18:28]** reviews, there's filters because I just

**[18:28]** reviews, there's filters because I just understand this really well. And there's

**[18:29]** understand this really well. And there's

**[18:29]** understand this really well. And there's things Google does not understand at

**[18:31]** things Google does not understand at

**[18:31]** things Google does not understand at all, mostly as web documents, bag of

**[18:33]** all, mostly as web documents, bag of

**[18:33]** all, mostly as web documents, bag of words. And what's really interesting

**[18:34]** words. And what's really interesting

**[18:34]** words. And what's really interesting about the AI is the eye changes. If you

**[18:36]** about the AI is the eye changes. If you

**[18:36]** about the AI is the eye changes. If you understand more, you show a more kind of

**[18:38]** understand more, you show a more kind of

**[18:38]** understand more, you show a more kind of like filterable high promise. If you

**[18:41]** like filterable high promise. If you

**[18:41]** like filterable high promise. If you don't understand enough, you actually

**[18:42]** don't understand enough, you actually

**[18:42]** don't understand enough, you actually degrade your experience, but you degrade

**[18:44]** degrade your experience, but you degrade

**[18:44]** degrade your experience, but you degrade it to something that is still workable.

**[18:46]** it to something that is still workable.

**[18:46]** it to something that is still workable. Like, I'll show you 10 things, you

**[18:47]** Like, I'll show you 10 things, you

**[18:47]** Like, I'll show you 10 things, you choose. Oh no, I know exactly what you

**[18:49]** choose. Oh no, I know exactly what you

**[18:49]** choose. Oh no, I know exactly what you want. I'll show you one thing. And this

**[18:51]** want. I'll show you one thing. And this

**[18:51]** want. I'll show you one thing. And this is really, really important. has to be

**[18:52]** is really, really important. has to be

**[18:52]** is really, really important. has to be like part of every and this is sort of

**[18:54]** like part of every and this is sort of

**[18:54]** like part of every and this is sort of like always understand like there's only

**[18:55]** like always understand like there's only

**[18:56]** like always understand like there's only so much engineering you can do until you

**[18:58]** so much engineering you can do until you

**[18:58]** so much engineering you can do until you have to like actually change your

**[18:59]** have to like actually change your

**[18:59]** have to like actually change your product to accommodate this sort of


### [19:00 - 20:00]

**[19:00]** product to accommodate this sort of

**[19:00]** product to accommodate this sort of stoastic nature. So gracefully degrade,

**[19:03]** stoastic nature. So gracefully degrade,

**[19:03]** stoastic nature. So gracefully degrade, gracefully upgrade depending on like the

**[19:04]** gracefully upgrade depending on like the

**[19:04]** gracefully upgrade depending on like the the level of your understanding. And

**[19:06]** the level of your understanding. And

**[19:06]** the level of your understanding. And again, I'll flash these two slides at

**[19:07]** again, I'll flash these two slides at

**[19:07]** again, I'll flash these two slides at the end like always remember what you're

**[19:08]** the end like always remember what you're

**[19:08]** the end like always remember what you're doing because you can absolutely get

**[19:10]** doing because you can absolutely get

**[19:10]** doing because you can absolutely get into theoretical debates again context

**[19:12]** into theoretical debates again context

**[19:12]** into theoretical debates again context window versus rag uh this versus that

**[19:14]** window versus rag uh this versus that

**[19:14]** window versus rag uh this versus that like is you know agents versus I don't

**[19:16]** like is you know agents versus I don't

**[19:16]** like is you know agents versus I don't know like just everything is empirical

**[19:18]** know like just everything is empirical

**[19:18]** know like just everything is empirical in this domain when you're doing like

**[19:20]** in this domain when you're doing like

**[19:20]** in this domain when you're doing like this this sort of thing. Oh I have my

**[19:22]** this this sort of thing. Oh I have my

**[19:22]** this this sort of thing. Oh I have my evals I'm trying to like step by step go

**[19:23]** evals I'm trying to like step by step go

**[19:24]** evals I'm trying to like step by step go up I have like a toolbox under my

**[19:25]** up I have like a toolbox under my

**[19:25]** up I have like a toolbox under my disposal. Everything everything is

**[19:27]** disposal. Everything everything is

**[19:27]** disposal. Everything everything is empirical. So again, baseline, analyze

**[19:31]** empirical. So again, baseline, analyze

**[19:31]** empirical. So again, baseline, analyze your losses, and then look at your

**[19:33]** your losses, and then look at your

**[19:33]** your losses, and then look at your toolbox and see, are there easy things

**[19:35]** toolbox and see, are there easy things

**[19:35]** toolbox and see, are there easy things here I can do? If not, are there at

**[19:37]** here I can do? If not, are there at

**[19:37]** here I can do? If not, are there at least medium things I could do? If not,

**[19:39]** least medium things I could do? If not,

**[19:39]** least medium things I could do? If not, you know, should I hire more people and

**[19:40]** you know, should I hire more people and

**[19:40]** you know, should I hire more people and do like some really, really hard things?

**[19:42]** do like some really, really hard things?

**[19:42]** do like some really, really hard things? Uh, but always remember like the choice

**[19:44]** Uh, but always remember like the choice

**[19:44]** Uh, but always remember like the choice is on you and you should be principled

**[19:45]** is on you and you should be principled

**[19:45]** is on you and you should be principled because this can be an absolute waste of

**[19:47]** because this can be an absolute waste of

**[19:47]** because this can be an absolute waste of time uh if you're doing it too far ahead

**[19:49]** time uh if you're doing it too far ahead

**[19:49]** time uh if you're doing it too far ahead of the curve. All right, again, the

**[19:51]** of the curve. All right, again, the

**[19:51]** of the curve. All right, again, the slides are here, I think. Oh, I I I

**[19:53]** slides are here, I think. Oh, I I I

**[19:53]** slides are here, I think. Oh, I I I achieved it. 30 seconds left. uh and if

**[19:57]** achieved it. 30 seconds left. uh and if

**[19:57]** achieved it. 30 seconds left. uh and if you want the slides they're here again

**[19:58]** you want the slides they're here again

**[19:58]** you want the slides they're here again and uh reach out to us we're always


### [20:00 - 21:00]

**[20:01]** and uh reach out to us we're always

**[20:01]** and uh reach out to us we're always happy to talk I think I was very happy

**[20:02]** happy to talk I think I was very happy

**[20:02]** happy to talk I think I was very happy with the exit talk because it's always

**[20:03]** with the exit talk because it's always

**[20:03]** with the exit talk because it's always nice to find like friends who are nerds

**[20:05]** nice to find like friends who are nerds

**[20:05]** nice to find like friends who are nerds in information retrieval uh we are also

**[20:08]** in information retrieval uh we are also

**[20:08]** in information retrieval uh we are also such so reach out and happy to talk

**[20:10]** such so reach out and happy to talk

**[20:10]** such so reach out and happy to talk about you know rag challenges and such

**[20:12]** about you know rag challenges and such

**[20:12]** about you know rag challenges and such and some of the models we are building

**[20:14]** and some of the models we are building

**[20:14]** and some of the models we are building um all right thank you so much

**[20:16]** um all right thank you so much

**[20:16]** um all right thank you so much [Music]


