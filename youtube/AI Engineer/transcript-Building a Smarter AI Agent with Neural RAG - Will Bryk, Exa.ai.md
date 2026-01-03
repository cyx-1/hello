# Building a Smarter AI Agent with Neural RAG - Will Bryk, Exa.ai

**Video URL:** https://www.youtube.com/watch?v=xnXqpUW_Kp8

---

## Full Transcript

### [00:00 - 01:00]

**[00:19]** All right. So, I was gonna give uh live

**[00:19]** All right. So, I was gonna give uh live demo coding,

**[00:21]** demo coding,

**[00:21]** demo coding, but well, I will, but I know you all are

**[00:24]** but well, I will, but I know you all are

**[00:24]** but well, I will, but I know you all are actually here to hear a cool story. So

**[00:26]** actually here to hear a cool story. So

**[00:26]** actually here to hear a cool story. So I'll tell you a story about web search

**[00:28]** I'll tell you a story about web search

**[00:28]** I'll tell you a story about web search built for AI and then we do some coding

**[00:30]** built for AI and then we do some coding

**[00:30]** built for AI and then we do some coding at the end.

**[00:32]** at the end.

**[00:32]** at the end. This story will end with this slide uh

**[00:35]** This story will end with this slide uh

**[00:35]** This story will end with this slide uh one API to get any information from the

**[00:37]** one API to get any information from the

**[00:37]** one API to get any information from the web

**[00:39]** web

**[00:39]** web and you'll know what this means by the

**[00:40]** and you'll know what this means by the

**[00:40]** and you'll know what this means by the end but the story starts in 1998

**[00:44]** end but the story starts in 1998

**[00:44]** end but the story starts in 1998 and what you're looking at is the the

**[00:46]** and what you're looking at is the the

**[00:46]** and what you're looking at is the the state-of-the-art in information

**[00:48]** state-of-the-art in information

**[00:48]** state-of-the-art in information retrieval in 1998. You type in a word

**[00:51]** retrieval in 1998. You type in a word

**[00:51]** retrieval in 1998. You type in a word Australia to this new search engine

**[00:53]** Australia to this new search engine

**[00:53]** Australia to this new search engine called Google and it magically finds you

**[00:55]** called Google and it magically finds you

**[00:55]** called Google and it magically finds you all the documents that contain the word

**[00:57]** all the documents that contain the word

**[00:57]** all the documents that contain the word Australia from the web. It's crazy. Um


### [01:00 - 02:00]

**[01:00]** Australia from the web. It's crazy. Um

**[01:00]** Australia from the web. It's crazy. Um and the the big insight of Google was

**[01:02]** and the the big insight of Google was

**[01:02]** and the the big insight of Google was they had this page rank algorithm. So uh

**[01:04]** they had this page rank algorithm. So uh

**[01:04]** they had this page rank algorithm. So uh the results are ranked by authority

**[01:06]** the results are ranked by authority

**[01:06]** the results are ranked by authority based on the graph structure of the web.

**[01:08]** based on the graph structure of the web.

**[01:08]** based on the graph structure of the web. And this was a clever algorithm and it

**[01:09]** And this was a clever algorithm and it

**[01:09]** And this was a clever algorithm and it was really cool. I was two years old at

**[01:11]** was really cool. I was two years old at

**[01:11]** was really cool. I was two years old at the time. So if I was conscious I would

**[01:13]** the time. So if I was conscious I would

**[01:13]** the time. So if I was conscious I would have thought this was cool. Um

**[01:16]** have thought this was cool. Um

**[01:16]** have thought this was cool. Um okay and now our story our now our story

**[01:19]** okay and now our story our now our story

**[01:19]** okay and now our story our now our story uh skips 23 years to 2021. Um by this

**[01:22]** uh skips 23 years to 2021. Um by this

**[01:22]** uh skips 23 years to 2021. Um by this point I was conscious barely and uh uh

**[01:26]** point I was conscious barely and uh uh

**[01:26]** point I was conscious barely and uh uh and I I noticed that you know GBD3 had

**[01:29]** and I I noticed that you know GBD3 had

**[01:29]** and I I noticed that you know GBD3 had recently come out and it was this

**[01:31]** recently come out and it was this

**[01:31]** recently come out and it was this magical thing that you could input a

**[01:34]** magical thing that you could input a

**[01:34]** magical thing that you could input a whole paragraph explaining exactly what

**[01:35]** whole paragraph explaining exactly what

**[01:35]** whole paragraph explaining exactly what you want uh and it would really

**[01:37]** you want uh and it would really

**[01:37]** you want uh and it would really understand the subtleties of your

**[01:38]** understand the subtleties of your

**[01:38]** understand the subtleties of your language and give you an output that

**[01:40]** language and give you an output that

**[01:40]** language and give you an output that exactly matched. Um, and it's hard to

**[01:42]** exactly matched. Um, and it's hard to

**[01:42]** exactly matched. Um, and it's hard to remember how magical this was, but it

**[01:43]** remember how magical this was, but it

**[01:43]** remember how magical this was, but it was really magical in 2021. And at the

**[01:45]** was really magical in 2021. And at the

**[01:45]** was really magical in 2021. And at the same time, I noticed there was Google,

**[01:48]** same time, I noticed there was Google,

**[01:48]** same time, I noticed there was Google, which you know, you type in a simple

**[01:50]** which you know, you type in a simple

**[01:50]** which you know, you type in a simple query like shirts without stripes and it

**[01:52]** query like shirts without stripes and it

**[01:52]** query like shirts without stripes and it would give you shirts with stripes,

**[01:53]** would give you shirts with stripes,

**[01:53]** would give you shirts with stripes, which is crazy. Uh, it like doesn't

**[01:55]** which is crazy. Uh, it like doesn't

**[01:56]** which is crazy. Uh, it like doesn't understand the word without u because

**[01:58]** understand the word without u because

**[01:58]** understand the word without u because it's doing a keyword comparison

**[01:59]** it's doing a keyword comparison

**[01:59]** it's doing a keyword comparison algorithm. And so I decided that for the


### [02:00 - 03:00]

**[02:03]** algorithm. And so I decided that for the

**[02:03]** algorithm. And so I decided that for the next at least 10 years I'm going to

**[02:04]** next at least 10 years I'm going to

**[02:04]** next at least 10 years I'm going to devote myself to building a search

**[02:05]** devote myself to building a search

**[02:05]** devote myself to building a search engine that combines the technology of

**[02:08]** engine that combines the technology of

**[02:08]** engine that combines the technology of GB3 uh to with a search engine to make a

**[02:11]** GB3 uh to with a search engine to make a

**[02:11]** GB3 uh to with a search engine to make a search engine that actually understands

**[02:13]** search engine that actually understands

**[02:13]** search engine that actually understands what you're saying uh at a deep level

**[02:15]** what you're saying uh at a deep level

**[02:15]** what you're saying uh at a deep level and understands all the documents on the

**[02:16]** and understands all the documents on the

**[02:16]** and understands all the documents on the web at a deep level and gives you

**[02:18]** web at a deep level and gives you

**[02:18]** web at a deep level and gives you exactly what you ask for. This is a very

**[02:20]** exactly what you ask for. This is a very

**[02:20]** exactly what you ask for. This is a very big idea and we're working we've been

**[02:21]** big idea and we're working we've been

**[02:22]** big idea and we're working we've been working on it for four years and uh a

**[02:24]** working on it for four years and uh a

**[02:24]** working on it for four years and uh a lot of progress

**[02:25]** lot of progress

**[02:25]** lot of progress but it would change the world if you

**[02:27]** but it would change the world if you

**[02:27]** but it would change the world if you actually solve this problem. And so in

**[02:30]** actually solve this problem. And so in

**[02:30]** actually solve this problem. And so in 2021, uh, we we we joined YC summer

**[02:33]** 2021, uh, we we we joined YC summer

**[02:33]** 2021, uh, we we we joined YC summer 2021. Uh, we raised a couple million

**[02:35]** 2021. Uh, we raised a couple million

**[02:35]** 2021. Uh, we raised a couple million dollars and we did what every YC startup

**[02:36]** dollars and we did what every YC startup

**[02:36]** dollars and we did what every YC startup should do. We spent half of it on a GPU

**[02:38]** should do. We spent half of it on a GPU

**[02:38]** should do. We spent half of it on a GPU cluster.

**[02:40]** cluster.

**[02:40]** cluster. I'm joking. You shouldn't do that.

**[02:43]** I'm joking. You shouldn't do that.

**[02:43]** I'm joking. You shouldn't do that. Um, and and then we also followed YC's

**[02:46]** Um, and and then we also followed YC's

**[02:46]** Um, and and then we also followed YC's advice uh where we didn't talk to any

**[02:48]** advice uh where we didn't talk to any

**[02:48]** advice uh where we didn't talk to any users or or customers for a year and a

**[02:50]** users or or customers for a year and a

**[02:50]** users or or customers for a year and a half and we just did research. Um,

**[02:52]** half and we just did research. Um,

**[02:52]** half and we just did research. Um, again, you shouldn't do that. You should

**[02:53]** again, you shouldn't do that. You should

**[02:53]** again, you shouldn't do that. You should duck us, but in our case, it made sense

**[02:55]** duck us, but in our case, it made sense

**[02:55]** duck us, but in our case, it made sense because we were trying to solve a really

**[02:56]** because we were trying to solve a really

**[02:56]** because we were trying to solve a really hard problem which is like redesign

**[02:57]** hard problem which is like redesign

**[02:57]** hard problem which is like redesign search from scratch. um using the same


### [03:00 - 04:00]

**[03:00]** search from scratch. um using the same

**[03:00]** search from scratch. um using the same technology as DB3, this like next token

**[03:02]** technology as DB3, this like next token

**[03:02]** technology as DB3, this like next token prediction idea with transformers. What

**[03:04]** prediction idea with transformers. What

**[03:04]** prediction idea with transformers. What if you could apply the same thing uh to

**[03:05]** if you could apply the same thing uh to

**[03:05]** if you could apply the same thing uh to search? And this is actually one of our

**[03:08]** search? And this is actually one of our

**[03:08]** search? And this is actually one of our uh WDB training runs. Um the purple one

**[03:10]** uh WDB training runs. Um the purple one

**[03:10]** uh WDB training runs. Um the purple one I believe is was a breakthrough where it

**[03:12]** I believe is was a breakthrough where it

**[03:12]** I believe is was a breakthrough where it like really it really like learned there

**[03:14]** like really it really like learned there

**[03:14]** like really it really like learned there was like a few breakthroughs along the

**[03:15]** was like a few breakthroughs along the

**[03:15]** was like a few breakthroughs along the way uh involving like random data sets

**[03:17]** way uh involving like random data sets

**[03:17]** way uh involving like random data sets and different uh transform architectures

**[03:18]** and different uh transform architectures

**[03:18]** and different uh transform architectures that we were trying. And this purple one

**[03:19]** that we were trying. And this purple one

**[03:19]** that we were trying. And this purple one like really started to like work well.

**[03:23]** like really started to like work well.

**[03:23]** like really started to like work well. Um and the general idea we had was like

**[03:25]** Um and the general idea we had was like

**[03:25]** Um and the general idea we had was like okay so what is what is a search engine?

**[03:26]** okay so what is what is a search engine?

**[03:26]** okay so what is what is a search engine? have like a trillion documents on the

**[03:28]** have like a trillion documents on the

**[03:28]** have like a trillion documents on the web. Um, and traditional search engines

**[03:31]** web. Um, and traditional search engines

**[03:31]** web. Um, and traditional search engines uh on a very high level will create like

**[03:33]** uh on a very high level will create like

**[03:33]** uh on a very high level will create like a keyword index of those documents. So

**[03:35]** a keyword index of those documents. So

**[03:35]** a keyword index of those documents. So for each document you you say you ask

**[03:37]** for each document you you say you ask

**[03:37]** for each document you you say you ask what are the words in those document and

**[03:39]** what are the words in those document and

**[03:39]** what are the words in those document and you create this big inverted index where

**[03:40]** you create this big inverted index where

**[03:40]** you create this big inverted index where you map from like words like brown to

**[03:43]** you map from like words like brown to

**[03:43]** you map from like words like brown to all the documents that contain that

**[03:44]** all the documents that contain that

**[03:44]** all the documents that contain that word. Um, and then at search time, you

**[03:47]** word. Um, and then at search time, you

**[03:48]** word. Um, and then at search time, you know, when a search without stripes

**[03:49]** know, when a search without stripes

**[03:49]** know, when a search without stripes comes in, you do some crazy keyword uh

**[03:51]** comes in, you do some crazy keyword uh

**[03:51]** comes in, you do some crazy keyword uh comparison algorithm and get the top

**[03:53]** comparison algorithm and get the top

**[03:53]** comparison algorithm and get the top results. That's obviously a

**[03:54]** results. That's obviously a

**[03:54]** results. That's obviously a simplification of what Google does. But

**[03:55]** simplification of what Google does. But

**[03:55]** simplification of what Google does. But at a fundamental level, it's doing it's

**[03:57]** at a fundamental level, it's doing it's

**[03:57]** at a fundamental level, it's doing it's like a keyword comparison.

**[03:59]** like a keyword comparison.


### [04:00 - 05:00]

**[04:00]** like a keyword comparison. But the idea was like what if you could

**[04:01]** But the idea was like what if you could

**[04:01]** But the idea was like what if you could actually so with transformers like the

**[04:03]** actually so with transformers like the

**[04:03]** actually so with transformers like the big thing is like what if you could turn

**[04:04]** big thing is like what if you could turn

**[04:04]** big thing is like what if you could turn each document not into a set of keywords

**[04:06]** each document not into a set of keywords

**[04:06]** each document not into a set of keywords but into embeddings. Uh and these

**[04:08]** but into embeddings. Uh and these

**[04:08]** but into embeddings. Uh and these embeddings can be arbitrarily powerful,

**[04:10]** embeddings can be arbitrarily powerful,

**[04:10]** embeddings can be arbitrarily powerful, right? Like it's a list of an embedding

**[04:12]** right? Like it's a list of an embedding

**[04:12]** right? Like it's a list of an embedding is just a list of of of numbers and uh

**[04:14]** is just a list of of of numbers and uh

**[04:14]** is just a list of of of numbers and uh it could represent lots of information.

**[04:15]** it could represent lots of information.

**[04:15]** it could represent lots of information. So and embedding it doesn't just capture

**[04:17]** So and embedding it doesn't just capture

**[04:17]** So and embedding it doesn't just capture the words in the document but also the

**[04:19]** the words in the document but also the

**[04:19]** the words in the document but also the meaning the ideas in the document and

**[04:21]** meaning the ideas in the document and

**[04:21]** meaning the ideas in the document and the way people refer to that document on

**[04:22]** the way people refer to that document on

**[04:22]** the way people refer to that document on the web and you know embedding can be

**[04:24]** the web and you know embedding can be

**[04:24]** the web and you know embedding can be arbitrarily big and so it like of course

**[04:26]** arbitrarily big and so it like of course

**[04:26]** arbitrarily big and so it like of course in the limit it would just destroy

**[04:28]** in the limit it would just destroy

**[04:28]** in the limit it would just destroy keywords and so you have this like

**[04:29]** keywords and so you have this like

**[04:29]** keywords and so you have this like arbitrarily powerful representation um

**[04:32]** arbitrarily powerful representation um

**[04:32]** arbitrarily powerful representation um and that the fundamental idea was just

**[04:33]** and that the fundamental idea was just

**[04:33]** and that the fundamental idea was just like the bitter lesson what if we could

**[04:35]** like the bitter lesson what if we could

**[04:35]** like the bitter lesson what if we could like you know train transformers to

**[04:36]** like you know train transformers to

**[04:36]** like you know train transformers to output embeddings for documents and if

**[04:37]** output embeddings for documents and if

**[04:37]** output embeddings for documents and if we keep getting more and more data

**[04:39]** we keep getting more and more data

**[04:39]** we keep getting more and more data that's high quality we could uh make a

**[04:41]** that's high quality we could uh make a

**[04:41]** that's high quality we could uh make a search engine that actually understands

**[04:42]** search engine that actually understands

**[04:42]** search engine that actually understands you and um the way it would work at

**[04:45]** you and um the way it would work at

**[04:45]** you and um the way it would work at inference at search time is like a

**[04:46]** inference at search time is like a

**[04:46]** inference at search time is like a search comes in, a query comes in like

**[04:48]** search comes in, a query comes in like

**[04:48]** search comes in, a query comes in like shirts without stripes. Traditional

**[04:49]** shirts without stripes. Traditional

**[04:49]** shirts without stripes. Traditional search engines would use the above thing

**[04:51]** search engines would use the above thing

**[04:51]** search engines would use the above thing where they would do a very fancy keyword

**[04:53]** where they would do a very fancy keyword

**[04:53]** where they would do a very fancy keyword comparison and a bunch of other things.

**[04:55]** comparison and a bunch of other things.

**[04:55]** comparison and a bunch of other things. Um, and then instead we would just embed

**[04:57]** Um, and then instead we would just embed

**[04:57]** Um, and then instead we would just embed the shirts without stripes and compare

**[04:58]** the shirts without stripes and compare

**[04:58]** the shirts without stripes and compare it to the embeddings of all the trillion

**[04:59]** it to the embeddings of all the trillion

**[04:59]** it to the embeddings of all the trillion documents.


### [05:00 - 06:00]

**[05:02]** documents.

**[05:02]** documents. And you know, after a year and a half,

**[05:03]** And you know, after a year and a half,

**[05:03]** And you know, after a year and a half, we actually had a new search engine that

**[05:04]** we actually had a new search engine that

**[05:04]** we actually had a new search engine that worked in a very different way. Uh, and

**[05:06]** worked in a very different way. Uh, and

**[05:06]** worked in a very different way. Uh, and you search shirt search shirts without

**[05:07]** you search shirt search shirts without

**[05:07]** you search shirt search shirts without stripes on Google, sorry, on Exa and you

**[05:09]** stripes on Google, sorry, on Exa and you

**[05:09]** stripes on Google, sorry, on Exa and you um you get a list of results that

**[05:11]** um you get a list of results that

**[05:11]** um you get a list of results that actually are not do not have stripes. Uh

**[05:13]** actually are not do not have stripes. Uh

**[05:13]** actually are not do not have stripes. Uh it's a simple uh example, but like you

**[05:15]** it's a simple uh example, but like you

**[05:15]** it's a simple uh example, but like you could uh it could handle like more way

**[05:17]** could uh it could handle like more way

**[05:17]** could uh it could handle like more way more complex queries like paragraph long

**[05:18]** more complex queries like paragraph long

**[05:18]** more complex queries like paragraph long queries.

**[05:21]** queries.

**[05:21]** queries. And when we launched this in November

**[05:23]** And when we launched this in November

**[05:23]** And when we launched this in November 2022, we got a lot of excitement on

**[05:25]** 2022, we got a lot of excitement on

**[05:25]** 2022, we got a lot of excitement on Twitter. Um this is a very new paradigm

**[05:26]** Twitter. Um this is a very new paradigm

**[05:26]** Twitter. Um this is a very new paradigm for search. You can do all sorts of

**[05:27]** for search. You can do all sorts of

**[05:28]** for search. You can do all sorts of interesting queries that you couldn't do

**[05:29]** interesting queries that you couldn't do

**[05:29]** interesting queries that you couldn't do before. And then two weeks later, this

**[05:32]** before. And then two weeks later, this

**[05:32]** before. And then two weeks later, this happened. It was a small tweet. Um

**[05:36]** happened. It was a small tweet. Um

**[05:36]** happened. It was a small tweet. Um and uh this is a visual depiction of San

**[05:38]** and uh this is a visual depiction of San

**[05:38]** and uh this is a visual depiction of San Francisco at the time. Um you guys

**[05:41]** Francisco at the time. Um you guys

**[05:41]** Francisco at the time. Um you guys probably all remember this.

**[05:44]** probably all remember this.

**[05:44]** probably all remember this. And then this is a visual depiction of

**[05:46]** And then this is a visual depiction of

**[05:46]** And then this is a visual depiction of the exit team at the time because chatbt

**[05:50]** the exit team at the time because chatbt

**[05:50]** the exit team at the time because chatbt completely changed the way we interact

**[05:51]** completely changed the way we interact

**[05:51]** completely changed the way we interact with the world's information. You know,

**[05:53]** with the world's information. You know,

**[05:53]** with the world's information. You know, like everyone can now use an LLM to just

**[05:55]** like everyone can now use an LLM to just

**[05:55]** like everyone can now use an LLM to just like talk talk to their computer and and

**[05:57]** like talk talk to their computer and and

**[05:57]** like talk talk to their computer and and get information. And we were thinking,

**[05:59]** get information. And we were thinking,

**[05:59]** get information. And we were thinking, wait, is there even a role for search in


### [06:00 - 07:00]

**[06:01]** wait, is there even a role for search in

**[06:01]** wait, is there even a role for search in this world? Like these LLMs are so

**[06:02]** this world? Like these LLMs are so

**[06:02]** this world? Like these LLMs are so powerful. And then very quickly we

**[06:04]** powerful. And then very quickly we

**[06:04]** powerful. And then very quickly we realized, yes, there is a role because

**[06:06]** realized, yes, there is a role because

**[06:06]** realized, yes, there is a role because LLM don't know everything on the web.

**[06:08]** LLM don't know everything on the web.

**[06:08]** LLM don't know everything on the web. So, for example, if you ask an LLM like

**[06:10]** So, for example, if you ask an LLM like

**[06:10]** So, for example, if you ask an LLM like GBD4, find me cool personal sites of

**[06:12]** GBD4, find me cool personal sites of

**[06:12]** GBD4, find me cool personal sites of engineers in San Francisco. Um, it'll it

**[06:14]** engineers in San Francisco. Um, it'll it

**[06:14]** engineers in San Francisco. Um, it'll it it can't like it just doesn't have that

**[06:16]** it can't like it just doesn't have that

**[06:16]** it can't like it just doesn't have that in the weights. It'll apologize,

**[06:17]** in the weights. It'll apologize,

**[06:17]** in the weights. It'll apologize, whatever. Um, and you know, there's a

**[06:19]** whatever. Um, and you know, there's a

**[06:20]** whatever. Um, and you know, there's a very simple information theory argument

**[06:21]** very simple information theory argument

**[06:21]** very simple information theory argument here where it's like there literally

**[06:23]** here where it's like there literally

**[06:23]** here where it's like there literally isn't enough information in the weights

**[06:24]** isn't enough information in the weights

**[06:24]** isn't enough information in the weights of GB4 to store the whole web. GB4 will

**[06:26]** of GB4 to store the whole web. GB4 will

**[06:26]** of GB4 to store the whole web. GB4 will call like we don't know exactly how many

**[06:28]** call like we don't know exactly how many

**[06:28]** call like we don't know exactly how many uh parameters. I think someone leaked it

**[06:29]** uh parameters. I think someone leaked it

**[06:29]** uh parameters. I think someone leaked it on YouTube once, but it's like, you

**[06:30]** on YouTube once, but it's like, you

**[06:30]** on YouTube once, but it's like, you know, a couple trillion parameters. You

**[06:32]** know, a couple trillion parameters. You

**[06:32]** know, a couple trillion parameters. You could call like less than 10 terabytes

**[06:35]** could call like less than 10 terabytes

**[06:35]** could call like less than 10 terabytes uh in the weights of GB4. And then the

**[06:37]** uh in the weights of GB4. And then the

**[06:37]** uh in the weights of GB4. And then the internet is like over a million

**[06:38]** internet is like over a million

**[06:38]** internet is like over a million terabytes. And that's just the documents

**[06:40]** terabytes. And that's just the documents

**[06:40]** terabytes. And that's just the documents on the web. Uh there's also images and

**[06:42]** on the web. Uh there's also images and

**[06:42]** on the web. Uh there's also images and video and that's way more. Um actually

**[06:45]** video and that's way more. Um actually

**[06:45]** video and that's way more. Um actually the the web if you look I I did a tweet

**[06:47]** the the web if you look I I did a tweet

**[06:47]** the the web if you look I I did a tweet recently about the the size of the web

**[06:48]** recently about the the size of the web

**[06:48]** recently about the the size of the web and it's it's in the exabyte range. Um

**[06:50]** and it's it's in the exabyte range. Um

**[06:50]** and it's it's in the exabyte range. Um and our name is Exa. It's not a

**[06:52]** and our name is Exa. It's not a

**[06:52]** and our name is Exa. It's not a coincidence. Um anyway, so like LLM uh

**[06:56]** coincidence. Um anyway, so like LLM uh

**[06:56]** coincidence. Um anyway, so like LLM uh need to search the web just from this

**[06:57]** need to search the web just from this

**[06:57]** need to search the web just from this simple argument and they're going to

**[06:58]** simple argument and they're going to

**[06:58]** simple argument and they're going to need to do that for a long time which um


### [07:00 - 08:00]

**[07:00]** need to do that for a long time which um

**[07:00]** need to do that for a long time which um if you talk to ML researchers they'll

**[07:01]** if you talk to ML researchers they'll

**[07:01]** if you talk to ML researchers they'll say the same thing. It's just like it

**[07:02]** say the same thing. It's just like it

**[07:02]** say the same thing. It's just like it it's too hard. Also the web is

**[07:04]** it's too hard. Also the web is

**[07:04]** it's too hard. Also the web is constantly updating. That's another

**[07:05]** constantly updating. That's another

**[07:05]** constantly updating. That's another problem. It's not just the size of the

**[07:06]** problem. It's not just the size of the

**[07:06]** problem. It's not just the size of the web, it's the constant updatingness of

**[07:07]** web, it's the constant updatingness of

**[07:07]** web, it's the constant updatingness of the web that makes it very tricky. So

**[07:08]** the web that makes it very tricky. So

**[07:08]** the web that makes it very tricky. So LMS always will need search. That's

**[07:10]** LMS always will need search. That's

**[07:10]** LMS always will need search. That's great. Um, and so when you combine an

**[07:12]** great. Um, and so when you combine an

**[07:12]** great. Um, and so when you combine an LLM with a search engine like Exa, you

**[07:14]** LLM with a search engine like Exa, you

**[07:14]** LLM with a search engine like Exa, you can handle these uh queries. So like

**[07:17]** can handle these uh queries. So like

**[07:17]** can handle these uh queries. So like find me cool personal sites and

**[07:18]** find me cool personal sites and

**[07:18]** find me cool personal sites and engineers and SF. Uh, the LLM will

**[07:20]** engineers and SF. Uh, the LLM will

**[07:20]** engineers and SF. Uh, the LLM will search EXA, get a list of personal

**[07:22]** search EXA, get a list of personal

**[07:22]** search EXA, get a list of personal sites, uh, and then like use that

**[07:24]** sites, uh, and then like use that

**[07:24]** sites, uh, and then like use that information to output the perfect thing

**[07:25]** information to output the perfect thing

**[07:26]** information to output the perfect thing for the user. You're all very familiar

**[07:28]** for the user. You're all very familiar

**[07:28]** for the user. You're all very familiar with this like LLM plus search. It's

**[07:30]** with this like LLM plus search. It's

**[07:30]** with this like LLM plus search. It's obvious now, right? Like everyone knows

**[07:31]** obvious now, right? Like everyone knows

**[07:31]** obvious now, right? Like everyone knows about it. But now let me tell you a

**[07:33]** about it. But now let me tell you a

**[07:33]** about it. But now let me tell you a secret about search that most people

**[07:35]** secret about search that most people

**[07:35]** secret about search that most people don't know. Um

**[07:38]** don't know. Um

**[07:38]** don't know. Um and the secret is that traditional

**[07:41]** and the secret is that traditional

**[07:41]** and the secret is that traditional search engines were not built for this

**[07:42]** search engines were not built for this

**[07:42]** search engines were not built for this world of AI. Traditional search engines

**[07:44]** world of AI. Traditional search engines

**[07:44]** world of AI. Traditional search engines were built for humans. Uh and humans are

**[07:47]** were built for humans. Uh and humans are

**[07:47]** were built for humans. Uh and humans are not are very different from AI. Uh so

**[07:49]** not are very different from AI. Uh so

**[07:49]** not are very different from AI. Uh so every search engine like Google, Bing,

**[07:51]** every search engine like Google, Bing,

**[07:51]** every search engine like Google, Bing, you name it. Uh was built in a different

**[07:53]** you name it. Uh was built in a different

**[07:53]** you name it. Uh was built in a different era for this kind of creature. uh this

**[07:56]** era for this kind of creature. uh this

**[07:56]** era for this kind of creature. uh this this slow flesh human that's typing

**[07:59]** this slow flesh human that's typing

**[07:59]** this slow flesh human that's typing keywords and wants to read a few links


### [08:00 - 09:00]

**[08:01]** keywords and wants to read a few links

**[08:01]** keywords and wants to read a few links and really cares about UI of the page

**[08:03]** and really cares about UI of the page

**[08:03]** and really cares about UI of the page and all these things like it's a lazy

**[08:05]** and all these things like it's a lazy

**[08:05]** and all these things like it's a lazy human. They type simple keywords. Google

**[08:06]** human. They type simple keywords. Google

**[08:06]** human. They type simple keywords. Google is great for this creature. Um Google

**[08:09]** is great for this creature. Um Google

**[08:09]** is great for this creature. Um Google was optimized for this creature. It

**[08:10]** was optimized for this creature. It

**[08:10]** was optimized for this creature. It gives you exactly the kinds of things

**[08:11]** gives you exactly the kinds of things

**[08:11]** gives you exactly the kinds of things you would click on.

**[08:14]** you would click on.

**[08:14]** you would click on. But AIs are very different. Um this like

**[08:16]** But AIs are very different. Um this like

**[08:16]** But AIs are very different. Um this like an AI can gobble up information like

**[08:18]** an AI can gobble up information like

**[08:18]** an AI can gobble up information like crazy. This is a much slowed down

**[08:20]** crazy. This is a much slowed down

**[08:20]** crazy. This is a much slowed down version of what our ais probably feel

**[08:22]** version of what our ais probably feel

**[08:22]** version of what our ais probably feel like inside. Uh and so AI are very

**[08:25]** like inside. Uh and so AI are very

**[08:25]** like inside. Uh and so AI are very different. They want to use complex

**[08:26]** different. They want to use complex

**[08:26]** different. They want to use complex queries, not simple ones, to find not a

**[08:28]** queries, not simple ones, to find not a

**[08:28]** queries, not simple ones, to find not a couple links, but just tons of

**[08:30]** couple links, but just tons of

**[08:30]** couple links, but just tons of knowledge, as much knowledge as they

**[08:31]** knowledge, as much knowledge as they

**[08:31]** knowledge, as much knowledge as they could get, because they actually have

**[08:32]** could get, because they actually have

**[08:32]** could get, because they actually have the patience to just analyze it all

**[08:34]** the patience to just analyze it all

**[08:34]** the patience to just analyze it all extremely fast. And so the the search

**[08:36]** extremely fast. And so the the search

**[08:36]** extremely fast. And so the the search algorithm that's optimal for this type

**[08:38]** algorithm that's optimal for this type

**[08:38]** algorithm that's optimal for this type of creature is not the same algorithm

**[08:41]** of creature is not the same algorithm

**[08:41]** of creature is not the same algorithm that's optimal for the human. Like that

**[08:43]** that's optimal for the human. Like that

**[08:43]** that's optimal for the human. Like that would be crazy if the same algorithm was

**[08:45]** would be crazy if the same algorithm was

**[08:45]** would be crazy if the same algorithm was optimal for humans was optimal for uh

**[08:47]** optimal for humans was optimal for uh

**[08:47]** optimal for humans was optimal for uh AIs. And so like all the a lot of the

**[08:49]** AIs. And so like all the a lot of the

**[08:49]** AIs. And so like all the a lot of the tools, the search tools that we're

**[08:51]** tools, the search tools that we're

**[08:51]** tools, the search tools that we're talking about these days on Twitter and

**[08:52]** talking about these days on Twitter and

**[08:52]** talking about these days on Twitter and stuff like that, they're still using

**[08:54]** stuff like that, they're still using

**[08:54]** stuff like that, they're still using like the old traditional search combined

**[08:56]** like the old traditional search combined

**[08:56]** like the old traditional search combined with AIS. It's just not the right puzzle

**[08:58]** with AIS. It's just not the right puzzle

**[08:58]** with AIS. It's just not the right puzzle fit. Um so Exo, we're really trying to


### [09:00 - 10:00]

**[09:00]** fit. Um so Exo, we're really trying to

**[09:00]** fit. Um so Exo, we're really trying to think of like what is the right search

**[09:01]** think of like what is the right search

**[09:01]** think of like what is the right search engine for this AI world.

**[09:04]** engine for this AI world.

**[09:04]** engine for this AI world. And so just a few examples uh we could

**[09:06]** And so just a few examples uh we could

**[09:06]** And so just a few examples uh we could dive deep into um to of how AI are

**[09:09]** dive deep into um to of how AI are

**[09:09]** dive deep into um to of how AI are different. Well, AIS want precise

**[09:11]** different. Well, AIS want precise

**[09:11]** different. Well, AIS want precise controllable information. So by the way,

**[09:13]** controllable information. So by the way,

**[09:13]** controllable information. So by the way, when I say AI, I'm usually I'm talking

**[09:15]** when I say AI, I'm usually I'm talking

**[09:15]** when I say AI, I'm usually I'm talking about like an AI product. So imagine

**[09:16]** about like an AI product. So imagine

**[09:16]** about like an AI product. So imagine like in this case like a VC that's using

**[09:18]** like in this case like a VC that's using

**[09:18]** like in this case like a VC that's using an AI system to find a list of companies

**[09:21]** an AI system to find a list of companies

**[09:21]** an AI system to find a list of companies uh because they want to invest. So you

**[09:23]** uh because they want to invest. So you

**[09:23]** uh because they want to invest. So you know they're looking for something

**[09:23]** know they're looking for something

**[09:23]** know they're looking for something what's the next big thing? What's the

**[09:24]** what's the next big thing? What's the

**[09:24]** what's the next big thing? What's the next big thing that feels like Bell

**[09:25]** next big thing that feels like Bell

**[09:26]** next big thing that feels like Bell Labs? Well, when they tell their AI what

**[09:28]** Labs? Well, when they tell their AI what

**[09:28]** Labs? Well, when they tell their AI what they want, the AI will then go search a

**[09:29]** they want, the AI will then go search a

**[09:29]** they want, the AI will then go search a search engine, right? And if it searches

**[09:31]** search engine, right? And if it searches

**[09:31]** search engine, right? And if it searches a search engine like Google, they'll get

**[09:33]** a search engine like Google, they'll get

**[09:33]** a search engine like Google, they'll get a list of results that humans like to

**[09:34]** a list of results that humans like to

**[09:34]** a list of results that humans like to click on, but it's not very information

**[09:36]** click on, but it's not very information

**[09:36]** click on, but it's not very information dense and it doesn't even match what the

**[09:37]** dense and it doesn't even match what the

**[09:37]** dense and it doesn't even match what the person asks for what the AI asks for.

**[09:39]** person asks for what the AI asks for.

**[09:39]** person asks for what the AI asks for. The AI asks for startups working on

**[09:41]** The AI asks for startups working on

**[09:41]** The AI asks for startups working on something huge that feels like Bell

**[09:42]** something huge that feels like Bell

**[09:42]** something huge that feels like Bell Labs. It should get a list of startups.

**[09:44]** Labs. It should get a list of startups.

**[09:44]** Labs. It should get a list of startups. It's kind of a crazy idea, but what if

**[09:46]** It's kind of a crazy idea, but what if

**[09:46]** It's kind of a crazy idea, but what if search engines actually returned exactly

**[09:48]** search engines actually returned exactly

**[09:48]** search engines actually returned exactly what you asked of them and not what you

**[09:50]** what you asked of them and not what you

**[09:50]** what you asked of them and not what you want to what Google knows you will click

**[09:51]** want to what Google knows you will click

**[09:51]** want to what Google knows you will click on. And so with AI especially, they just

**[09:54]** on. And so with AI especially, they just

**[09:54]** on. And so with AI especially, they just want a search engine that returns

**[09:55]** want a search engine that returns

**[09:55]** want a search engine that returns exactly what they ask for. Because

**[09:57]** exactly what they ask for. Because

**[09:57]** exactly what they ask for. Because what's what really the world is going to

**[09:58]** what's what really the world is going to

**[09:58]** what's what really the world is going to look like is you're going to interact

**[09:59]** look like is you're going to interact

**[09:59]** look like is you're going to interact with your AI agent and you're going to


### [10:00 - 11:00]

**[10:01]** with your AI agent and you're going to

**[10:01]** with your AI agent and you're going to ask for something and then it's going to

**[10:02]** ask for something and then it's going to

**[10:02]** ask for something and then it's going to make tons of searches like, okay, maybe

**[10:03]** make tons of searches like, okay, maybe

**[10:04]** make tons of searches like, okay, maybe they want startups working on something

**[10:05]** they want startups working on something

**[10:05]** they want startups working on something like similar to Bill Bell Labs. Maybe

**[10:06]** like similar to Bill Bell Labs. Maybe

**[10:06]** like similar to Bill Bell Labs. Maybe they want startups working only in New

**[10:08]** they want startups working only in New

**[10:08]** they want startups working only in New York City that have this quality and

**[10:09]** York City that have this quality and

**[10:09]** York City that have this quality and that quality and and and they'll do all

**[10:11]** that quality and and and they'll do all

**[10:11]** that quality and and and they'll do all sorts of searches and it just wants a

**[10:12]** sorts of searches and it just wants a

**[10:12]** sorts of searches and it just wants a search API that just does what it asks

**[10:14]** search API that just does what it asks

**[10:14]** search API that just does what it asks and and so you need a search engine like

**[10:15]** and and so you need a search engine like

**[10:15]** and and so you need a search engine like that. So X is like that. Um another

**[10:18]** that. So X is like that. Um another

**[10:18]** that. So X is like that. Um another difference between AIS and humans is AI

**[10:20]** difference between AIS and humans is AI

**[10:20]** difference between AIS and humans is AI want to search with lots of context.

**[10:21]** want to search with lots of context.

**[10:21]** want to search with lots of context. Again, if you're if you have an AI

**[10:23]** Again, if you're if you have an AI

**[10:23]** Again, if you're if you have an AI assistant and you talk to it all day and

**[10:25]** assistant and you talk to it all day and

**[10:25]** assistant and you talk to it all day and then you ask for restaurants or

**[10:27]** then you ask for restaurants or

**[10:27]** then you ask for restaurants or apartments or or what have you, uh the

**[10:29]** apartments or or what have you, uh the

**[10:29]** apartments or or what have you, uh the AI has lots of context on you. So it

**[10:30]** AI has lots of context on you. So it

**[10:30]** AI has lots of context on you. So it should be able to search with this large

**[10:33]** should be able to search with this large

**[10:33]** should be able to search with this large multi paragraph thing saying like you

**[10:34]** multi paragraph thing saying like you

**[10:34]** multi paragraph thing saying like you know my human is a software engineer and

**[10:36]** know my human is a software engineer and

**[10:36]** know my human is a software engineer and it likes these types of things and I

**[10:37]** it likes these types of things and I

**[10:37]** it likes these types of things and I like these types of things and like can

**[10:39]** like these types of things and like can

**[10:39]** like these types of things and like can you give me uh you know restaurants that

**[10:41]** you give me uh you know restaurants that

**[10:41]** you give me uh you know restaurants that match those preferences. Uh and so you

**[10:43]** match those preferences. Uh and so you

**[10:43]** match those preferences. Uh and so you need a search engine that could

**[10:44]** need a search engine that could

**[10:44]** need a search engine that could literally handle multiple paragraphs of

**[10:45]** literally handle multiple paragraphs of

**[10:45]** literally handle multiple paragraphs of text. But traditional search like search

**[10:47]** text. But traditional search like search

**[10:47]** text. But traditional search like search engines like Google were not meant to do

**[10:48]** engines like Google were not meant to do

**[10:48]** engines like Google were not meant to do that because humans would never type in

**[10:50]** that because humans would never type in

**[10:50]** that because humans would never type in multiple paragraphs because they're too

**[10:51]** multiple paragraphs because they're too

**[10:51]** multiple paragraphs because they're too lazy. So Google was optimized for like

**[10:53]** lazy. So Google was optimized for like

**[10:53]** lazy. So Google was optimized for like simple keyword queries. So Google I

**[10:55]** simple keyword queries. So Google I

**[10:55]** simple keyword queries. So Google I think has like a a few dozen keyword

**[10:56]** think has like a a few dozen keyword

**[10:56]** think has like a a few dozen keyword limit. Uh whereas uh Exa can handle like

**[10:59]** limit. Uh whereas uh Exa can handle like

**[10:59]** limit. Uh whereas uh Exa can handle like multiple paragraphs. of text.


### [11:00 - 12:00]

**[11:02]** multiple paragraphs. of text.

**[11:02]** multiple paragraphs. of text. Another big one where AI are different

**[11:03]** Another big one where AI are different

**[11:03]** Another big one where AI are different than humans is AIS want comprehensive

**[11:05]** than humans is AIS want comprehensive

**[11:05]** than humans is AIS want comprehensive knowledge. Uh like if you give a human

**[11:07]** knowledge. Uh like if you give a human

**[11:07]** knowledge. Uh like if you give a human 10,000 links or 10,000 pages, it doesn't

**[11:10]** 10,000 links or 10,000 pages, it doesn't

**[11:10]** 10,000 links or 10,000 pages, it doesn't know what to do with that. Like it would

**[11:11]** know what to do with that. Like it would

**[11:11]** know what to do with that. Like it would take 10 days of extreme patience to

**[11:14]** take 10 days of extreme patience to

**[11:14]** take 10 days of extreme patience to process all that. But AI can do it in 3

**[11:16]** process all that. But AI can do it in 3

**[11:16]** process all that. But AI can do it in 3 seconds if it's parallelized, right? So

**[11:18]** seconds if it's parallelized, right? So

**[11:18]** seconds if it's parallelized, right? So if I'm an a VC and I want to report on

**[11:20]** if I'm an a VC and I want to report on

**[11:20]** if I'm an a VC and I want to report on like all the companies in a space, I

**[11:22]** like all the companies in a space, I

**[11:22]** like all the companies in a space, I want literally all the companies. And

**[11:24]** want literally all the companies. And

**[11:24]** want literally all the companies. And there's a huge amount of value to

**[11:25]** there's a huge amount of value to

**[11:25]** there's a huge amount of value to getting truly all of them and not just

**[11:27]** getting truly all of them and not just

**[11:27]** getting truly all of them and not just like the 10 or 20 that Google is able to

**[11:29]** like the 10 or 20 that Google is able to

**[11:29]** like the 10 or 20 that Google is able to find. And so you need a search engine

**[11:31]** find. And so you need a search engine

**[11:31]** find. And so you need a search engine that exposes the ability to return a

**[11:33]** that exposes the ability to return a

**[11:33]** that exposes the ability to return a thousand 10,000 whatever it is. And also

**[11:35]** thousand 10,000 whatever it is. And also

**[11:35]** thousand 10,000 whatever it is. And also has this semantic ability to like you

**[11:37]** has this semantic ability to like you

**[11:37]** has this semantic ability to like you know when you say like every starter

**[11:39]** know when you say like every starter

**[11:39]** know when you say like every starter funded by YC working on AI you actually

**[11:40]** funded by YC working on AI you actually

**[11:40]** funded by YC working on AI you actually can get all of them. So like Google

**[11:42]** can get all of them. So like Google

**[11:42]** can get all of them. So like Google literally just can't do this at all.

**[11:44]** literally just can't do this at all.

**[11:44]** literally just can't do this at all. Okay. I hope that through these examples

**[11:46]** Okay. I hope that through these examples

**[11:46]** Okay. I hope that through these examples we see that the space of possible

**[11:48]** we see that the space of possible

**[11:48]** we see that the space of possible queries is actually like way larger than

**[11:50]** queries is actually like way larger than

**[11:50]** queries is actually like way larger than people realize. Uh and until like 2022,

**[11:54]** people realize. Uh and until like 2022,

**[11:54]** people realize. Uh and until like 2022, we were kind of in this like top left

**[11:55]** we were kind of in this like top left

**[11:56]** we were kind of in this like top left blue world. Uh so this circle is like

**[11:58]** blue world. Uh so this circle is like

**[11:58]** blue world. Uh so this circle is like the space of possible queries and the


### [12:00 - 13:00]

**[12:00]** the space of possible queries and the

**[12:00]** the space of possible queries and the blues are like uh you know specific

**[12:02]** blues are like uh you know specific

**[12:02]** blues are like uh you know specific subsets of that space. And so like we

**[12:04]** subsets of that space. And so like we

**[12:04]** subsets of that space. And so like we were all in that top left corner of blue

**[12:07]** were all in that top left corner of blue

**[12:07]** were all in that top left corner of blue for a long time where you could you know

**[12:09]** for a long time where you could you know

**[12:09]** for a long time where you could you know we could search engines could handle

**[12:10]** we could search engines could handle

**[12:10]** we could search engines could handle like uh like basic keyword queries like

**[12:12]** like uh like basic keyword queries like

**[12:12]** like uh like basic keyword queries like stripe pricing or uh someone's GitHub

**[12:15]** stripe pricing or uh someone's GitHub

**[12:15]** stripe pricing or uh someone's GitHub page or Taylor Swift's boyfriend or

**[12:17]** page or Taylor Swift's boyfriend or

**[12:17]** page or Taylor Swift's boyfriend or whatever it is. Uh after 2022, everyone

**[12:20]** whatever it is. Uh after 2022, everyone

**[12:20]** whatever it is. Uh after 2022, everyone started to want the top right blue uh

**[12:22]** started to want the top right blue uh

**[12:22]** started to want the top right blue uh circle where it was like, "Hey,

**[12:23]** circle where it was like, "Hey,

**[12:23]** circle where it was like, "Hey, actually, I want to make queries like

**[12:25]** actually, I want to make queries like

**[12:25]** actually, I want to make queries like explain this concept to me like I'm a

**[12:26]** explain this concept to me like I'm a

**[12:26]** explain this concept to me like I'm a 5-year-old or here's my code. Can you

**[12:28]** 5-year-old or here's my code. Can you

**[12:28]** 5-year-old or here's my code. Can you like debug it?" The this is a form of

**[12:30]** like debug it?" The this is a form of

**[12:30]** like debug it?" The this is a form of query. Doesn't require search, but it's

**[12:31]** query. Doesn't require search, but it's

**[12:32]** query. Doesn't require search, but it's a it's another type of query that was

**[12:33]** a it's another type of query that was

**[12:33]** a it's another type of query that was introduced to the world in 2022. And

**[12:36]** introduced to the world in 2022. And

**[12:36]** introduced to the world in 2022. And then like uh there's other types of

**[12:38]** then like uh there's other types of

**[12:38]** then like uh there's other types of queries like these semantic queries like

**[12:39]** queries like these semantic queries like

**[12:39]** queries like these semantic queries like people in San Francisco who know

**[12:41]** people in San Francisco who know

**[12:41]** people in San Francisco who know assembly. uh as far as I'm aware, XA is

**[12:43]** assembly. uh as far as I'm aware, XA is

**[12:43]** assembly. uh as far as I'm aware, XA is like I mean XA kind of like introduced

**[12:45]** like I mean XA kind of like introduced

**[12:45]** like I mean XA kind of like introduced this kind of query and and uh and does

**[12:47]** this kind of query and and uh and does

**[12:47]** this kind of query and and uh and does really really well on them on those

**[12:48]** really really well on them on those

**[12:48]** really really well on them on those queries. And then there's these like

**[12:50]** queries. And then there's these like

**[12:50]** queries. And then there's these like really complex queries like find me

**[12:51]** really complex queries like find me

**[12:51]** really complex queries like find me every article that argues X and not Y

**[12:53]** every article that argues X and not Y

**[12:53]** every article that argues X and not Y from an author like Z. And we're

**[12:55]** from an author like Z. And we're

**[12:55]** from an author like Z. And we're starting to now have systems like X's

**[12:57]** starting to now have systems like X's

**[12:57]** starting to now have systems like X's like websites product that could handle

**[12:58]** like websites product that could handle

**[12:58]** like websites product that could handle these things. And I think this is

**[12:59]** these things. And I think this is

**[12:59]** these things. And I think this is actually a huge space because this like


### [13:00 - 14:00]

**[13:02]** actually a huge space because this like

**[13:02]** actually a huge space because this like turns the web into like a database you

**[13:04]** turns the web into like a database you

**[13:04]** turns the web into like a database you could filter however you want. And

**[13:05]** could filter however you want. And

**[13:05]** could filter however you want. And that's really what AIs want. They want

**[13:06]** that's really what AIs want. They want

**[13:06]** that's really what AIs want. They want this like full control database like

**[13:09]** this like full control database like

**[13:09]** this like full control database like query system that they could just get

**[13:10]** query system that they could just get

**[13:10]** query system that they could just get whatever they need for their user. And

**[13:12]** whatever they need for their user. And

**[13:12]** whatever they need for their user. And then there are the queries that no one

**[13:13]** then there are the queries that no one

**[13:13]** then there are the queries that no one has thought of yet. Um like every week

**[13:15]** has thought of yet. Um like every week

**[13:15]** has thought of yet. Um like every week we get tons of queries and like oh wait

**[13:17]** we get tons of queries and like oh wait

**[13:17]** we get tons of queries and like oh wait that's a really interesting type of

**[13:18]** that's a really interesting type of

**[13:18]** that's a really interesting type of query that uh that no search engine

**[13:20]** query that uh that no search engine

**[13:20]** query that uh that no search engine could do right now. And and eventually

**[13:22]** could do right now. And and eventually

**[13:22]** could do right now. And and eventually we'll try to you know handle all the the

**[13:24]** we'll try to you know handle all the the

**[13:24]** we'll try to you know handle all the the queries that are possible. But there

**[13:25]** queries that are possible. But there

**[13:25]** queries that are possible. But there there's so many new types of queries now

**[13:27]** there's so many new types of queries now

**[13:27]** there's so many new types of queries now because we have these AI systems and the

**[13:28]** because we have these AI systems and the

**[13:28]** because we have these AI systems and the stakes like the the expectations have

**[13:31]** stakes like the the expectations have

**[13:31]** stakes like the the expectations have just gotten way higher.

**[13:33]** just gotten way higher.

**[13:33]** just gotten way higher. Okay. So now you we end our story. uh

**[13:36]** Okay. So now you we end our story. uh

**[13:36]** Okay. So now you we end our story. uh with the same slide a one API to get any

**[13:39]** with the same slide a one API to get any

**[13:39]** with the same slide a one API to get any information from the web. So again like

**[13:40]** information from the web. So again like

**[13:40]** information from the web. So again like EXO is trying to if you go back like

**[13:43]** EXO is trying to if you go back like

**[13:43]** EXO is trying to if you go back like handle not just like the keyword queries

**[13:45]** handle not just like the keyword queries

**[13:45]** handle not just like the keyword queries but also the semantic queries and also

**[13:46]** but also the semantic queries and also

**[13:46]** but also the semantic queries and also the super complex queries and eventually

**[13:48]** the super complex queries and eventually

**[13:48]** the super complex queries and eventually all queries. Um we we want one API that

**[13:51]** all queries. Um we we want one API that

**[13:51]** all queries. Um we we want one API that could like give these AI systems

**[13:53]** could like give these AI systems

**[13:53]** could like give these AI systems whatever knowledge they want. You have

**[13:54]** whatever knowledge they want. You have

**[13:54]** whatever knowledge they want. You have the AI and you have Exa providing uh the

**[13:57]** the AI and you have Exa providing uh the

**[13:57]** the AI and you have Exa providing uh the knowledge. Oh, I only have four minutes.

**[13:59]** knowledge. Oh, I only have four minutes.

**[13:59]** knowledge. Oh, I only have four minutes. Okay. Um okay.


### [14:00 - 15:00]

**[14:02]** Okay. Um okay.

**[14:02]** Okay. Um okay. So that's let's see. Oop.

**[14:05]** So that's let's see. Oop.

**[14:06]** So that's let's see. Oop. How do I go to a different part of my

**[14:08]** How do I go to a different part of my

**[14:08]** How do I go to a different part of my computer?

**[14:15]** Uh, if I change to the code editor, how

**[14:15]** Uh, if I change to the code editor, how do I do that? Let's see. What? Oh, it's

**[14:18]** do I do that? Let's see. What? Oh, it's

**[14:18]** do I do that? Let's see. What? Oh, it's there. Oh, but I can't see it. So weird.

**[14:24]** there. Oh, but I can't see it. So weird.

**[14:24]** there. Oh, but I can't see it. So weird. Oh, cool. Okay. Okay. Um,

**[14:29]** Oh, cool. Okay. Okay. Um,

**[14:29]** Oh, cool. Okay. Okay. Um, there we go. Okay, cool. Well, first of

**[14:32]** there we go. Okay, cool. Well, first of

**[14:32]** there we go. Okay, cool. Well, first of all, I just just very quick exploration

**[14:33]** all, I just just very quick exploration

**[14:33]** all, I just just very quick exploration of this is our our search dashboard, we

**[14:35]** of this is our our search dashboard, we

**[14:35]** of this is our our search dashboard, we could try different queries. I would

**[14:36]** could try different queries. I would

**[14:36]** could try different queries. I would just point out like in the search uh API

**[14:39]** just point out like in the search uh API

**[14:39]** just point out like in the search uh API endpoint. Uh you know, we expose lots of

**[14:42]** endpoint. Uh you know, we expose lots of

**[14:42]** endpoint. Uh you know, we expose lots of different toggles. So, first of all, you

**[14:43]** different toggles. So, first of all, you

**[14:44]** different toggles. So, first of all, you just try out a query and get uh it shows

**[14:47]** just try out a query and get uh it shows

**[14:47]** just try out a query and get uh it shows you the code and it gets you uh a list

**[14:49]** you the code and it gets you uh a list

**[14:49]** you the code and it gets you uh a list of results. Uh and it exposes tons of

**[14:52]** of results. Uh and it exposes tons of

**[14:52]** of results. Uh and it exposes tons of different types of filters that you

**[14:53]** different types of filters that you

**[14:53]** different types of filters that you might want to do. For example, like

**[14:54]** might want to do. For example, like

**[14:54]** might want to do. For example, like number of results, 10, 100, a thousand,

**[14:56]** number of results, 10, 100, a thousand,

**[14:56]** number of results, 10, 100, a thousand, whatever it is. Uh you could have like

**[14:57]** whatever it is. Uh you could have like

**[14:57]** whatever it is. Uh you could have like date ranges or you know, I only want to

**[14:59]** date ranges or you know, I only want to

**[14:59]** date ranges or you know, I only want to search over these domains. And it's a


### [15:00 - 16:00]

**[15:00]** search over these domains. And it's a

**[15:00]** search over these domains. And it's a lot of toggles, but I think the point is

**[15:02]** lot of toggles, but I think the point is

**[15:02]** lot of toggles, but I think the point is actually you want the toggles because

**[15:03]** actually you want the toggles because

**[15:03]** actually you want the toggles because your AI is actually going to be calling

**[15:04]** your AI is actually going to be calling

**[15:04]** your AI is actually going to be calling this. You want a search engine that

**[15:05]** this. You want a search engine that

**[15:05]** this. You want a search engine that gives you full control. Um, and we have

**[15:07]** gives you full control. Um, and we have

**[15:07]** gives you full control. Um, and we have like neural and keyword search. So you

**[15:09]** like neural and keyword search. So you

**[15:09]** like neural and keyword search. So you could try different ones. Um, okay, let

**[15:12]** could try different ones. Um, okay, let

**[15:12]** could try different ones. Um, okay, let me quickly jump the the

**[15:15]** me quickly jump the the

**[15:15]** me quickly jump the the code. Okay, so I prepared this like code

**[15:18]** code. Okay, so I prepared this like code

**[15:18]** code. Okay, so I prepared this like code uh agent.py. So we made this agent uh

**[15:21]** uh agent.py. So we made this agent uh

**[15:21]** uh agent.py. So we made this agent uh agent Mark and Mark loves to make

**[15:23]** agent Mark and Mark loves to make

**[15:23]** agent Mark and Mark loves to make markdown out of things. Anything you

**[15:25]** markdown out of things. Anything you

**[15:25]** markdown out of things. Anything you give it, it will make markdown. Mark

**[15:27]** give it, it will make markdown. Mark

**[15:27]** give it, it will make markdown. Mark will make markdown. Uh and so in this

**[15:28]** will make markdown. Uh and so in this

**[15:28]** will make markdown. Uh and so in this case uh we're going to here well I guess

**[15:32]** case uh we're going to here well I guess

**[15:32]** case uh we're going to here well I guess in this case let's try uh this query uh

**[15:37]** in this case let's try uh this query uh

**[15:37]** in this case let's try uh this query uh personal site of engineer in San

**[15:39]** personal site of engineer in San

**[15:39]** personal site of engineer in San Francisco who likes information

**[15:40]** Francisco who likes information

**[15:40]** Francisco who likes information retrieval.

**[15:42]** retrieval.

**[15:42]** retrieval. Uh well this is this is the kind of

**[15:43]** Uh well this is this is the kind of

**[15:43]** Uh well this is this is the kind of query that neural would be a lot better

**[15:45]** query that neural would be a lot better

**[15:45]** query that neural would be a lot better at. What?

**[15:48]** at. What?

**[15:48]** at. What? Okay. Save it.


### [16:00 - 17:00]

**[16:01]** Okay, so it's just it's making a query

**[16:02]** Okay, so it's just it's making a query to get like a list of personal sites of

**[16:03]** to get like a list of personal sites of

**[16:04]** to get like a list of personal sites of engineers San Francisco who like

**[16:05]** engineers San Francisco who like

**[16:05]** engineers San Francisco who like information retrieval and and mark the

**[16:06]** information retrieval and and mark the

**[16:06]** information retrieval and and mark the agent is just making a markdown output

**[16:08]** agent is just making a markdown output

**[16:08]** agent is just making a markdown output of that. That's a very neural type

**[16:09]** of that. That's a very neural type

**[16:09]** of that. That's a very neural type query. You also might want to do uh a

**[16:12]** query. You also might want to do uh a

**[16:12]** query. You also might want to do uh a different type of query which is like a

**[16:14]** different type of query which is like a

**[16:14]** different type of query which is like a more keyword heavy one. Let's see like

**[16:16]** more keyword heavy one. Let's see like

**[16:16]** more keyword heavy one. Let's see like um

**[16:32]** GitHub let me and my GitHub so okay so

**[16:32]** GitHub let me and my GitHub so okay so here I would want to make a keyword

**[16:33]** here I would want to make a keyword

**[16:33]** here I would want to make a keyword query so you just change the keyword

**[16:42]** search so it's going to get information

**[16:42]** search so it's going to get information from my from my GitHub using keyword

**[16:43]** from my from my GitHub using keyword

**[16:43]** from my from my GitHub using keyword search because this is a very typical

**[16:45]** search because this is a very typical

**[16:45]** search because this is a very typical like Google like search that would work

**[16:46]** like Google like search that would work

**[16:46]** like Google like search that would work well right oh god I'm running this wrong

**[16:48]** well right oh god I'm running this wrong

**[16:48]** well right oh god I'm running this wrong one

**[16:49]** one

**[16:50]** one okay

**[16:52]** okay

**[16:52]** okay cool that's information about Wicks,

**[16:54]** cool that's information about Wicks,

**[16:54]** cool that's information about Wicks, GitHub. Um, and then, okay, so when

**[16:56]** GitHub. Um, and then, okay, so when

**[16:56]** GitHub. Um, and then, okay, so when you're actually building an agent,

**[16:57]** you're actually building an agent,

**[16:57]** you're actually building an agent, you're going to be combining lots of

**[16:58]** you're going to be combining lots of

**[16:58]** you're going to be combining lots of different types of searches. So, neural


### [17:00 - 18:00]

**[17:00]** different types of searches. So, neural

**[17:00]** different types of searches. So, neural searches and keyword searches, uh, and

**[17:02]** searches and keyword searches, uh, and

**[17:02]** searches and keyword searches, uh, and all sorts of other searches that X

**[17:03]** all sorts of other searches that X

**[17:03]** all sorts of other searches that X exposes. So, like the right agent in the

**[17:05]** exposes. So, like the right agent in the

**[17:05]** exposes. So, like the right agent in the future is going to be this system that

**[17:07]** future is going to be this system that

**[17:07]** future is going to be this system that decides what type of search it needs,

**[17:10]** decides what type of search it needs,

**[17:10]** decides what type of search it needs, uh, for, uh, what whatever the user

**[17:12]** uh, for, uh, what whatever the user

**[17:12]** uh, for, uh, what whatever the user says, like be like, oh, okay, I'm going

**[17:13]** says, like be like, oh, okay, I'm going

**[17:13]** says, like be like, oh, okay, I'm going to make like a neural search to get a

**[17:15]** to make like a neural search to get a

**[17:15]** to make like a neural search to get a list of things, and then for each one,

**[17:16]** list of things, and then for each one,

**[17:16]** list of things, and then for each one, I'm going to do a keyword search. Right?

**[17:17]** I'm going to do a keyword search. Right?

**[17:17]** I'm going to do a keyword search. Right? You want to give the uh, agent like just

**[17:20]** You want to give the uh, agent like just

**[17:20]** You want to give the uh, agent like just full access to the world's information

**[17:21]** full access to the world's information

**[17:21]** full access to the world's information in however way it wants. uh not just

**[17:24]** in however way it wants. uh not just

**[17:24]** in however way it wants. uh not just keyword search but also all these other

**[17:25]** keyword search but also all these other

**[17:25]** keyword search but also all these other things. Um and so here I oneshotted with

**[17:29]** things. Um and so here I oneshotted with

**[17:30]** things. Um and so here I oneshotted with 03 a GitHub agent which combines these

**[17:32]** 03 a GitHub agent which combines these

**[17:32]** 03 a GitHub agent which combines these two queries. So first it'll because I

**[17:35]** two queries. So first it'll because I

**[17:35]** two queries. So first it'll because I want you know I want to get the GitHub

**[17:36]** want you know I want to get the GitHub

**[17:36]** want you know I want to get the GitHub of every uh engineer in San Francisco

**[17:39]** of every uh engineer in San Francisco

**[17:39]** of every uh engineer in San Francisco who likes information retrieval. Uh so

**[17:41]** who likes information retrieval. Uh so

**[17:41]** who likes information retrieval. Uh so the agent will make uh a neural search

**[17:43]** the agent will make uh a neural search

**[17:43]** the agent will make uh a neural search to get a list of people extract the

**[17:45]** to get a list of people extract the

**[17:45]** to get a list of people extract the names and then search those using a

**[17:47]** names and then search those using a

**[17:47]** names and then search those using a keyword search to get their GitHubs. And

**[17:49]** keyword search to get their GitHubs. And

**[17:49]** keyword search to get their GitHubs. And then if you run that

**[17:55]** here, it's just getting 10 results, but

**[17:55]** here, it's just getting 10 results, but we could, you know, with Exo, we could

**[17:56]** we could, you know, with Exo, we could

**[17:56]** we could, you know, with Exo, we could do 100 or a thousand if you're on an

**[17:58]** do 100 or a thousand if you're on an

**[17:58]** do 100 or a thousand if you're on an enterprise plan. Um,


### [18:00 - 19:00]

**[18:01]** enterprise plan. Um,

**[18:01]** enterprise plan. Um, so now it's getting all the GitHub info.

**[18:10]** Cool. So that's just a example. Um, and

**[18:10]** Cool. So that's just a example. Um, and yeah, I mean there are lots of other

**[18:11]** yeah, I mean there are lots of other

**[18:12]** yeah, I mean there are lots of other things that you could do with Exa like

**[18:13]** things that you could do with Exa like

**[18:13]** things that you could do with Exa like um, we actually just today launched this

**[18:16]** um, we actually just today launched this

**[18:16]** um, we actually just today launched this research endpoint um, where it will

**[18:18]** research endpoint um, where it will

**[18:18]** research endpoint um, where it will actually do like as much searches in the

**[18:21]** actually do like as much searches in the

**[18:21]** actually do like as much searches in the NL LM calls in the background to get you

**[18:23]** NL LM calls in the background to get you

**[18:23]** NL LM calls in the background to get you that perfect report or that perfect

**[18:25]** that perfect report or that perfect

**[18:25]** that perfect report or that perfect structured output for the thing you

**[18:26]** structured output for the thing you

**[18:26]** structured output for the thing you asked for. So it's kind of like a deep

**[18:27]** asked for. So it's kind of like a deep

**[18:27]** asked for. So it's kind of like a deep research API and it state-of-the-art

**[18:29]** research API and it state-of-the-art

**[18:29]** research API and it state-of-the-art deep research API. Um, cool. That is the

**[18:33]** deep research API. Um, cool. That is the

**[18:34]** deep research API. Um, cool. That is the talk. I hope that was interesting. Thank

**[18:35]** talk. I hope that was interesting. Thank

**[18:35]** talk. I hope that was interesting. Thank you.

**[18:37]** you.

**[18:37]** you. [Music]


