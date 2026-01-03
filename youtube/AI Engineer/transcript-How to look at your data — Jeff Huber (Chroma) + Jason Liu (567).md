# How to look at your data — Jeff Huber (Chroma) + Jason Liu (567)

**Video URL:** https://www.youtube.com/watch?v=jryZvCuA0Uc

---

## Full Transcript

### [00:00 - 01:00]

**[00:00]** All

**[00:00]** All [Music]

**[00:17]** right, welcome everybody. Um, I'm Jeff

**[00:17]** right, welcome everybody. Um, I'm Jeff Huber, the co-founder and CEO of Chroma,

**[00:19]** Huber, the co-founder and CEO of Chroma,

**[00:19]** Huber, the co-founder and CEO of Chroma, and I'm joined by Jason. We're going to

**[00:21]** and I'm joined by Jason. We're going to

**[00:21]** and I'm joined by Jason. We're going to do a two-parter here. We're really going

**[00:22]** do a two-parter here. We're really going

**[00:22]** do a two-parter here. We're really going to pack in the content. It's the last

**[00:24]** to pack in the content. It's the last

**[00:24]** to pack in the content. It's the last session of the day, and so we thought

**[00:26]** session of the day, and so we thought

**[00:26]** session of the day, and so we thought I'd give you a lot. Um everything in

**[00:29]** I'd give you a lot. Um everything in

**[00:29]** I'd give you a lot. Um everything in this presentation today is open source

**[00:30]** this presentation today is open source

**[00:30]** this presentation today is open source and code available. So we're also not

**[00:32]** and code available. So we're also not

**[00:32]** and code available. So we're also not selling you any tools. Um and so

**[00:34]** selling you any tools. Um and so

**[00:34]** selling you any tools. Um and so there'll be QR codes and stuff

**[00:35]** there'll be QR codes and stuff

**[00:35]** there'll be QR codes and stuff throughout to grab the code. So let's

**[00:37]** throughout to grab the code. So let's

**[00:37]** throughout to grab the code. So let's talk about how to look at your data. Um

**[00:41]** talk about how to look at your data. Um

**[00:41]** talk about how to look at your data. Um all of you are AI practitioners. Um

**[00:43]** all of you are AI practitioners. Um

**[00:43]** all of you are AI practitioners. Um you're all building stuff and uh this

**[00:46]** you're all building stuff and uh this

**[00:46]** you're all building stuff and uh this probably these questions probably

**[00:48]** probably these questions probably

**[00:48]** probably these questions probably resonate quite deeply with you. Uh what

**[00:49]** resonate quite deeply with you. Uh what

**[00:49]** resonate quite deeply with you. Uh what chunking strategy should I use? Is my

**[00:51]** chunking strategy should I use? Is my

**[00:51]** chunking strategy should I use? Is my embedding model the best betting

**[00:53]** embedding model the best betting

**[00:53]** embedding model the best betting embedding model for my data? Um and

**[00:55]** embedding model for my data? Um and

**[00:55]** embedding model for my data? Um and more. And our contention is that you can

**[00:58]** more. And our contention is that you can

**[00:58]** more. And our contention is that you can really only manage what you measure.


### [01:00 - 02:00]

**[01:00]** really only manage what you measure.

**[01:00]** really only manage what you measure. Again, I think Peter Ducker is the

**[01:01]** Again, I think Peter Ducker is the

**[01:01]** Again, I think Peter Ducker is the original who coined that. So, I can't

**[01:03]** original who coined that. So, I can't

**[01:03]** original who coined that. So, I can't take too much credit. Um, but it

**[01:04]** take too much credit. Um, but it

**[01:04]** take too much credit. Um, but it certainly is still true today. So, we

**[01:07]** certainly is still true today. So, we

**[01:07]** certainly is still true today. So, we have a very simple hypothesis here,

**[01:08]** have a very simple hypothesis here,

**[01:08]** have a very simple hypothesis here, which is you should look at your data.

**[01:10]** which is you should look at your data.

**[01:10]** which is you should look at your data. Um, the goal is to say look at your data

**[01:12]** Um, the goal is to say look at your data

**[01:12]** Um, the goal is to say look at your data I think at least 15 times this

**[01:13]** I think at least 15 times this

**[01:13]** I think at least 15 times this presentation. So, that's two. Um, and

**[01:16]** presentation. So, that's two. Um, and

**[01:16]** presentation. So, that's two. Um, and great measurement ultimately is what

**[01:18]** great measurement ultimately is what

**[01:18]** great measurement ultimately is what makes systematic improvement easy. And

**[01:20]** makes systematic improvement easy. And

**[01:20]** makes systematic improvement easy. And it really can be easy. It doesn't have

**[01:21]** it really can be easy. It doesn't have

**[01:22]** it really can be easy. It doesn't have to be super complicated. So, I'm going

**[01:24]** to be super complicated. So, I'm going

**[01:24]** to be super complicated. So, I'm going to talk about part one, how to look at

**[01:26]** to talk about part one, how to look at

**[01:26]** to talk about part one, how to look at your inputs. And then Jason's going to

**[01:27]** your inputs. And then Jason's going to

**[01:27]** your inputs. And then Jason's going to talk about part two, how to look at your

**[01:29]** talk about part two, how to look at your

**[01:29]** talk about part two, how to look at your outputs.

**[01:30]** outputs.

**[01:30]** outputs. So, let's get into it. All right.

**[01:32]** So, let's get into it. All right.

**[01:32]** So, let's get into it. All right. Looking at your inputs. How do you know

**[01:34]** Looking at your inputs. How do you know

**[01:34]** Looking at your inputs. How do you know whether or not your retrieval system is

**[01:36]** whether or not your retrieval system is

**[01:36]** whether or not your retrieval system is good? And how do you know how to make it

**[01:39]** good? And how do you know how to make it

**[01:39]** good? And how do you know how to make it better? Um, there are a few options. Um,

**[01:41]** better? Um, there are a few options. Um,

**[01:42]** better? Um, there are a few options. Um, there is guess and cross your fingers.

**[01:44]** there is guess and cross your fingers.

**[01:44]** there is guess and cross your fingers. That's certainly one option. Um, another

**[01:47]** That's certainly one option. Um, another

**[01:47]** That's certainly one option. Um, another option is to use an LLM as a judge.

**[01:49]** option is to use an LLM as a judge.

**[01:49]** option is to use an LLM as a judge. you're using, you know, some of these

**[01:51]** you're using, you know, some of these

**[01:51]** you're using, you know, some of these frameworks where you're checking

**[01:52]** frameworks where you're checking

**[01:52]** frameworks where you're checking factuality and other metrics like this

**[01:54]** factuality and other metrics like this

**[01:54]** factuality and other metrics like this and they cost $600 and take three hours

**[01:56]** and they cost $600 and take three hours

**[01:56]** and they cost $600 and take three hours to run. If that is your preference, you

**[01:58]** to run. If that is your preference, you

**[01:58]** to run. If that is your preference, you certainly can do that. Um, you can use


### [02:00 - 03:00]

**[02:01]** certainly can do that. Um, you can use

**[02:01]** certainly can do that. Um, you can use public benchmarks. So, you can look at

**[02:02]** public benchmarks. So, you can look at

**[02:02]** public benchmarks. So, you can look at things like MTeb to figure out, oh,

**[02:04]** things like MTeb to figure out, oh,

**[02:04]** things like MTeb to figure out, oh, which embedding model is the best on

**[02:05]** which embedding model is the best on

**[02:05]** which embedding model is the best on English. That's another option. Um, but

**[02:08]** English. That's another option. Um, but

**[02:08]** English. That's another option. Um, but our contention is you should use fast

**[02:10]** our contention is you should use fast

**[02:10]** our contention is you should use fast evals. And I will tell you exactly what

**[02:12]** evals. And I will tell you exactly what

**[02:12]** evals. And I will tell you exactly what fast evals are. All right. So, what is a

**[02:15]** fast evals are. All right. So, what is a

**[02:15]** fast evals are. All right. So, what is a fast eval? Um a fast eval is simply a

**[02:18]** fast eval? Um a fast eval is simply a

**[02:18]** fast eval? Um a fast eval is simply a set of query and document pairs. So the

**[02:21]** set of query and document pairs. So the

**[02:22]** set of query and document pairs. So the first step is if this query is put in

**[02:24]** first step is if this query is put in

**[02:24]** first step is if this query is put in this document should come out. Uh a set

**[02:27]** this document should come out. Uh a set

**[02:27]** this document should come out. Uh a set of those is called a golden data set and

**[02:30]** of those is called a golden data set and

**[02:30]** of those is called a golden data set and then the way that you measure your

**[02:32]** then the way that you measure your

**[02:32]** then the way that you measure your system is you put all the queries in and

**[02:35]** system is you put all the queries in and

**[02:35]** system is you put all the queries in and then you see do those documents come

**[02:37]** then you see do those documents come

**[02:37]** then you see do those documents come out. Um and obviously you can retrieve

**[02:39]** out. Um and obviously you can retrieve

**[02:39]** out. Um and obviously you can retrieve five or retrieve 10 or retrieve 20. It

**[02:41]** five or retrieve 10 or retrieve 20. It

**[02:41]** five or retrieve 10 or retrieve 20. It kind of depends on your application. Um

**[02:42]** kind of depends on your application. Um

**[02:42]** kind of depends on your application. Um it's very fast and very inexpensive to

**[02:45]** it's very fast and very inexpensive to

**[02:45]** it's very fast and very inexpensive to run. And this is very important because

**[02:46]** run. And this is very important because

**[02:46]** run. And this is very important because it enables you to run a lot of

**[02:48]** it enables you to run a lot of

**[02:48]** it enables you to run a lot of experiments quickly and cheaply. Um you

**[02:50]** experiments quickly and cheaply. Um you

**[02:50]** experiments quickly and cheaply. Um you know I'm sure all of you know that like

**[02:52]** know I'm sure all of you know that like

**[02:52]** know I'm sure all of you know that like experimentation time and your energy to

**[02:54]** experimentation time and your energy to

**[02:54]** experimentation time and your energy to do experimentation goes down

**[02:56]** do experimentation goes down

**[02:56]** do experimentation goes down significantly when you have to click go

**[02:59]** significantly when you have to click go

**[02:59]** significantly when you have to click go and then come back six hours later. Um


### [03:00 - 04:00]

**[03:01]** and then come back six hours later. Um

**[03:01]** and then come back six hours later. Um all of these metrics should run

**[03:02]** all of these metrics should run

**[03:02]** all of these metrics should run extremely quickly for pennies.

**[03:06]** extremely quickly for pennies.

**[03:06]** extremely quickly for pennies. So maybe you don't have yet, you have

**[03:08]** So maybe you don't have yet, you have

**[03:08]** So maybe you don't have yet, you have your documents, you have your chunks,

**[03:09]** your documents, you have your chunks,

**[03:09]** your documents, you have your chunks, you know, you have your stuff in your

**[03:10]** you know, you have your stuff in your

**[03:10]** you know, you have your stuff in your retrieval system, but you don't have

**[03:12]** retrieval system, but you don't have

**[03:12]** retrieval system, but you don't have queries yet. That's okay. Um, we found

**[03:14]** queries yet. That's okay. Um, we found

**[03:14]** queries yet. That's okay. Um, we found that you can actually use an LLM to

**[03:17]** that you can actually use an LLM to

**[03:17]** that you can actually use an LLM to write questions and write good

**[03:19]** write questions and write good

**[03:19]** write questions and write good questions. Um, you know, I think just

**[03:21]** questions. Um, you know, I think just

**[03:21]** questions. Um, you know, I think just doing naive like, "Hey LM, write me a

**[03:24]** doing naive like, "Hey LM, write me a

**[03:24]** doing naive like, "Hey LM, write me a question for this document." Not a great

**[03:26]** question for this document." Not a great

**[03:26]** question for this document." Not a great strategy. However, we found that you can

**[03:28]** strategy. However, we found that you can

**[03:28]** strategy. However, we found that you can actually teach LLMs how to write

**[03:30]** actually teach LLMs how to write

**[03:30]** actually teach LLMs how to write queries.

**[03:31]** queries.

**[03:31]** queries. Um, these slides are getting a little

**[03:33]** Um, these slides are getting a little

**[03:33]** Um, these slides are getting a little bit cropped. I'm not sure why, but we'll

**[03:34]** bit cropped. I'm not sure why, but we'll

**[03:34]** bit cropped. I'm not sure why, but we'll make the most of it. Um, to give you an

**[03:36]** make the most of it. Um, to give you an

**[03:36]** make the most of it. Um, to give you an example. So, this is actually a um

**[03:39]** example. So, this is actually a um

**[03:39]** example. So, this is actually a um example from one of the MTe kind of the

**[03:41]** example from one of the MTe kind of the

**[03:41]** example from one of the MTe kind of the golden data sets around embedding

**[03:43]** golden data sets around embedding

**[03:43]** golden data sets around embedding models, benchmark data sets. Um, this

**[03:46]** models, benchmark data sets. Um, this

**[03:46]** models, benchmark data sets. Um, this also points to the fact that like many

**[03:47]** also points to the fact that like many

**[03:48]** also points to the fact that like many of these benchmark data sets are overly

**[03:49]** of these benchmark data sets are overly

**[03:49]** of these benchmark data sets are overly clean, right? What is a pergola used for

**[03:51]** clean, right? What is a pergola used for

**[03:51]** clean, right? What is a pergola used for in a garden? And then the beginning of

**[03:53]** in a garden? And then the beginning of

**[03:53]** in a garden? And then the beginning of that sentence is a pergola in a garden

**[03:55]** that sentence is a pergola in a garden

**[03:55]** that sentence is a pergola in a garden dot dot dot dot dot. Um, real world data

**[03:58]** dot dot dot dot dot. Um, real world data

**[03:58]** dot dot dot dot dot. Um, real world data is never this clean. Um so what we did


### [04:00 - 05:00]

**[04:00]** is never this clean. Um so what we did

**[04:00]** is never this clean. Um so what we did in this report um the link is in a few

**[04:03]** in this report um the link is in a few

**[04:03]** in this report um the link is in a few slides. Um we did a huge deep dive into

**[04:05]** slides. Um we did a huge deep dive into

**[04:05]** slides. Um we did a huge deep dive into how can we actually align queries that

**[04:08]** how can we actually align queries that

**[04:08]** how can we actually align queries that are representative of real world

**[04:10]** are representative of real world

**[04:10]** are representative of real world queries. It's too easy to trick yourself

**[04:12]** queries. It's too easy to trick yourself

**[04:12]** queries. It's too easy to trick yourself into thinking that your system's working

**[04:13]** into thinking that your system's working

**[04:14]** into thinking that your system's working really well with synthetic queries that

**[04:15]** really well with synthetic queries that

**[04:15]** really well with synthetic queries that are overly specific to your data. Um and

**[04:18]** are overly specific to your data. Um and

**[04:18]** are overly specific to your data. Um and so what these graphs show is that we're

**[04:19]** so what these graphs show is that we're

**[04:20]** so what these graphs show is that we're actually able to semantically align the

**[04:22]** actually able to semantically align the

**[04:22]** actually able to semantically align the specificity of queries synthetically

**[04:24]** specificity of queries synthetically

**[04:24]** specificity of queries synthetically generated to real queries that users

**[04:26]** generated to real queries that users

**[04:26]** generated to real queries that users might ask of your system.

**[04:29]** might ask of your system.

**[04:29]** might ask of your system. So what this enables is, you know, if a

**[04:31]** So what this enables is, you know, if a

**[04:31]** So what this enables is, you know, if a new cool sexy embedding model comes out

**[04:33]** new cool sexy embedding model comes out

**[04:33]** new cool sexy embedding model comes out and it's doing really well in the MTB

**[04:35]** and it's doing really well in the MTB

**[04:35]** and it's doing really well in the MTB score and everybody on Twitter is

**[04:36]** score and everybody on Twitter is

**[04:36]** score and everybody on Twitter is talking about it, instead of just, you

**[04:38]** talking about it, instead of just, you

**[04:38]** talking about it, instead of just, you know, going into your code and changing

**[04:40]** know, going into your code and changing

**[04:40]** know, going into your code and changing it and guessing and checking and hoping

**[04:41]** it and guessing and checking and hoping

**[04:41]** it and guessing and checking and hoping that it's going to work, um, you now can

**[04:44]** that it's going to work, um, you now can

**[04:44]** that it's going to work, um, you now can empirically say whether it's good,

**[04:45]** empirically say whether it's good,

**[04:45]** empirically say whether it's good, better or not for your data, um, and you

**[04:49]** better or not for your data, um, and you

**[04:49]** better or not for your data, um, and you know, the kind of example here is quite

**[04:50]** know, the kind of example here is quite

**[04:50]** know, the kind of example here is quite contrived and simple. Um, you know, but

**[04:52]** contrived and simple. Um, you know, but

**[04:52]** contrived and simple. Um, you know, but you can actually look at the actual

**[04:53]** you can actually look at the actual

**[04:53]** you can actually look at the actual success rate. Okay, great. These are the

**[04:54]** success rate. Okay, great. These are the

**[04:54]** success rate. Okay, great. These are the queries that I care about. Do I get back

**[04:56]** queries that I care about. Do I get back

**[04:56]** queries that I care about. Do I get back more documents than I did before? If so,

**[04:58]** more documents than I did before? If so,

**[04:58]** more documents than I did before? If so, maybe you should consider changing. Now,


### [05:00 - 06:00]

**[05:00]** maybe you should consider changing. Now,

**[05:00]** maybe you should consider changing. Now, of course, you need to re-mbed your

**[05:01]** of course, you need to re-mbed your

**[05:01]** of course, you need to re-mbed your data. That service could be more

**[05:03]** data. That service could be more

**[05:03]** data. That service could be more expensive. It could be slower. The API

**[05:05]** expensive. It could be slower. The API

**[05:05]** expensive. It could be slower. The API for that service could be flaky. There's

**[05:07]** for that service could be flaky. There's

**[05:07]** for that service could be flaky. There's a lot of considerations obviously with

**[05:08]** a lot of considerations obviously with

**[05:08]** a lot of considerations obviously with making very good engineering decisions.

**[05:10]** making very good engineering decisions.

**[05:10]** making very good engineering decisions. Um, but clearly the north star of like

**[05:12]** Um, but clearly the north star of like

**[05:12]** Um, but clearly the north star of like success rate of how many documents that

**[05:14]** success rate of how many documents that

**[05:14]** success rate of how many documents that I get for my queries. Super fast and

**[05:17]** I get for my queries. Super fast and

**[05:17]** I get for my queries. Super fast and super useful and makes your improvement

**[05:19]** super useful and makes your improvement

**[05:19]** super useful and makes your improvement of your system much more systematic and

**[05:21]** of your system much more systematic and

**[05:21]** of your system much more systematic and deterministic. All right. So we actually

**[05:23]** deterministic. All right. So we actually

**[05:23]** deterministic. All right. So we actually uh worked with weights and biases um

**[05:25]** uh worked with weights and biases um

**[05:25]** uh worked with weights and biases um looking at their chatbot um to kind of

**[05:28]** looking at their chatbot um to kind of

**[05:28]** looking at their chatbot um to kind of ground a lot of this work. So what you

**[05:30]** ground a lot of this work. So what you

**[05:30]** ground a lot of this work. So what you see here is for the weights and biases

**[05:32]** see here is for the weights and biases

**[05:32]** see here is for the weights and biases chatbot um you can see four different

**[05:35]** chatbot um you can see four different

**[05:35]** chatbot um you can see four different embedding models and you can see the

**[05:36]** embedding models and you can see the

**[05:36]** embedding models and you can see the recall at 10 across those four different

**[05:39]** recall at 10 across those four different

**[05:39]** recall at 10 across those four different embedding models. And then I'll point

**[05:41]** embedding models. And then I'll point

**[05:41]** embedding models. And then I'll point out that uh blue is ground truth. So

**[05:43]** out that uh blue is ground truth. So

**[05:43]** out that uh blue is ground truth. So these are actual queries that were

**[05:44]** these are actual queries that were

**[05:44]** these are actual queries that were logged um in weave and then sent over.

**[05:47]** logged um in weave and then sent over.

**[05:47]** logged um in weave and then sent over. And then there's generated. These are

**[05:48]** And then there's generated. These are

**[05:48]** And then there's generated. These are the ones that are synthetically

**[05:49]** the ones that are synthetically

**[05:49]** the ones that are synthetically generated. And we want to see is a few

**[05:51]** generated. And we want to see is a few

**[05:51]** generated. And we want to see is a few things. We want to see that those are

**[05:52]** things. We want to see that those are

**[05:52]** things. We want to see that those are pretty close and we want to see that

**[05:54]** pretty close and we want to see that

**[05:54]** pretty close and we want to see that they are always the same kind of in

**[05:56]** they are always the same kind of in

**[05:56]** they are always the same kind of in order of accuracy, right? We don't want

**[05:57]** order of accuracy, right? We don't want

**[05:57]** order of accuracy, right? We don't want to see any like big flips between um


### [06:00 - 07:00]

**[06:00]** to see any like big flips between um

**[06:00]** to see any like big flips between um ground truth and generated and uh we're

**[06:02]** ground truth and generated and uh we're

**[06:02]** ground truth and generated and uh we're really happy to see that we found uh

**[06:04]** really happy to see that we found uh

**[06:04]** really happy to see that we found uh that answer. Now there are a few fun

**[06:06]** that answer. Now there are a few fun

**[06:06]** that answer. Now there are a few fun findings here which is and of course

**[06:09]** findings here which is and of course

**[06:09]** findings here which is and of course they're going to get crocked out but

**[06:10]** they're going to get crocked out but

**[06:10]** they're going to get crocked out but that's okay. Um number one uh the

**[06:13]** that's okay. Um number one uh the

**[06:13]** that's okay. Um number one uh the original embedding model used for this

**[06:15]** original embedding model used for this

**[06:15]** original embedding model used for this application was actually text embedding

**[06:17]** application was actually text embedding

**[06:17]** application was actually text embedding three small. um this actually performed

**[06:19]** three small. um this actually performed

**[06:19]** three small. um this actually performed the worst out of all the embedding

**[06:21]** the worst out of all the embedding

**[06:21]** the worst out of all the embedding models that we evaluated just for in

**[06:22]** models that we evaluated just for in

**[06:22]** models that we evaluated just for in this case. Um and so probably wasn't the

**[06:24]** this case. Um and so probably wasn't the

**[06:24]** this case. Um and so probably wasn't the best choice. Um the second one was that

**[06:26]** best choice. Um the second one was that

**[06:26]** best choice. Um the second one was that actually if you look at MTeb Gina

**[06:28]** actually if you look at MTeb Gina

**[06:28]** actually if you look at MTeb Gina embeddings v3 does very well in English.

**[06:30]** embeddings v3 does very well in English.

**[06:30]** embeddings v3 does very well in English. It's like you know way better than

**[06:32]** It's like you know way better than

**[06:32]** It's like you know way better than anything else but for this application

**[06:34]** anything else but for this application

**[06:34]** anything else but for this application uh it didn't actually perform that well.

**[06:36]** uh it didn't actually perform that well.

**[06:36]** uh it didn't actually perform that well. It was actually the voyage 3 large model

**[06:39]** It was actually the voyage 3 large model

**[06:39]** It was actually the voyage 3 large model which performed the best and that was

**[06:40]** which performed the best and that was

**[06:40]** which performed the best and that was empirically determined by actually

**[06:42]** empirically determined by actually

**[06:42]** empirically determined by actually running this fast evval and looking at

**[06:44]** running this fast evval and looking at

**[06:44]** running this fast evval and looking at your data. That's number three.

**[06:47]** your data. That's number three.

**[06:47]** your data. That's number three. All right. All right. So, if you'd like

**[06:48]** All right. All right. So, if you'd like

**[06:48]** All right. All right. So, if you'd like access to the full report, um, you can

**[06:50]** access to the full report, um, you can

**[06:50]** access to the full report, um, you can scan this QR code. It's at

**[06:51]** scan this QR code. It's at

**[06:51]** scan this QR code. It's at research.tra.com. There's also an

**[06:53]** research.tra.com. There's also an

**[06:53]** research.tra.com. There's also an adjoining video which is kind of

**[06:54]** adjoining video which is kind of

**[06:54]** adjoining video which is kind of screenshotted here, which goes into much

**[06:55]** screenshotted here, which goes into much

**[06:56]** screenshotted here, which goes into much more detail. There are full notebooks

**[06:57]** more detail. There are full notebooks

**[06:57]** more detail. There are full notebooks with all the code. It's all open source.

**[06:59]** with all the code. It's all open source.

**[06:59]** with all the code. It's all open source. You can run it on your own data. And um,


### [07:00 - 08:00]

**[07:01]** You can run it on your own data. And um,

**[07:01]** You can run it on your own data. And um, hopefully this is helpful for you all

**[07:03]** hopefully this is helpful for you all

**[07:03]** hopefully this is helpful for you all thinking about how again you can

**[07:04]** thinking about how again you can

**[07:04]** thinking about how again you can systematically and deterministically

**[07:05]** systematically and deterministically

**[07:06]** systematically and deterministically improve your retrieval systems. And with

**[07:08]** improve your retrieval systems. And with

**[07:08]** improve your retrieval systems. And with that, I'll hand it over to Jason. Thank

**[07:10]** that, I'll hand it over to Jason. Thank

**[07:10]** that, I'll hand it over to Jason. Thank you.

**[07:12]** you.

**[07:12]** you. So, you know, if you're working with

**[07:14]** So, you know, if you're working with

**[07:14]** So, you know, if you're working with some kind of system, there's always

**[07:15]** some kind of system, there's always

**[07:15]** some kind of system, there's always going to be the inputs that we look at.

**[07:16]** going to be the inputs that we look at.

**[07:16]** going to be the inputs that we look at. And so we talked about maybe thinking

**[07:17]** And so we talked about maybe thinking

**[07:18]** And so we talked about maybe thinking about things like retrieval, how does

**[07:19]** about things like retrieval, how does

**[07:19]** about things like retrieval, how does the embeddings work? But ultimately we

**[07:20]** the embeddings work? But ultimately we

**[07:20]** the embeddings work? But ultimately we also have to look at the outputs, right?

**[07:22]** also have to look at the outputs, right?

**[07:22]** also have to look at the outputs, right? And the outputs of many systems might be

**[07:24]** And the outputs of many systems might be

**[07:24]** And the outputs of many systems might be the outputs of a conversation that has

**[07:26]** the outputs of a conversation that has

**[07:26]** the outputs of a conversation that has happened, a you know agent execution

**[07:28]** happened, a you know agent execution

**[07:28]** happened, a you know agent execution that has happened. And the idea is that

**[07:30]** that has happened. And the idea is that

**[07:30]** that has happened. And the idea is that if you can look at these outputs, maybe

**[07:31]** if you can look at these outputs, maybe

**[07:31]** if you can look at these outputs, maybe we can do some kind of analysis that

**[07:33]** we can do some kind of analysis that

**[07:33]** we can do some kind of analysis that figures out, you know, what kind of

**[07:34]** figures out, you know, what kind of

**[07:34]** figures out, you know, what kind of product should we build, what kind of

**[07:36]** product should we build, what kind of

**[07:36]** product should we build, what kind of portfolio of tools should we develop for

**[07:38]** portfolio of tools should we develop for

**[07:38]** portfolio of tools should we develop for our agents and so forth.

**[07:40]** our agents and so forth.

**[07:40]** our agents and so forth. And so the idea is, you know, if you

**[07:42]** And so the idea is, you know, if you

**[07:42]** And so the idea is, you know, if you have a bunch of queries that users are

**[07:44]** have a bunch of queries that users are

**[07:44]** have a bunch of queries that users are putting in or even a couple of hundred

**[07:46]** putting in or even a couple of hundred

**[07:46]** putting in or even a couple of hundred of conversations, it's pretty good to

**[07:48]** of conversations, it's pretty good to

**[07:48]** of conversations, it's pretty good to just look at everything manually, right?

**[07:50]** just look at everything manually, right?

**[07:50]** just look at everything manually, right? Think very carefully about each

**[07:52]** Think very carefully about each

**[07:52]** Think very carefully about each interaction and then only use these

**[07:54]** interaction and then only use these

**[07:54]** interaction and then only use these models when they make sense. And then

**[07:56]** models when they make sense. And then

**[07:56]** models when they make sense. And then oftent times if I say this, they can

**[07:57]** oftent times if I say this, they can

**[07:57]** oftent times if I say this, they can say, you know what, if we just put

**[07:58]** say, you know what, if we just put

**[07:58]** say, you know what, if we just put everything in 03 and then here,


### [08:00 - 09:00]

**[08:00]** everything in 03 and then here,

**[08:00]** everything in 03 and then here, generally only use the language models

**[08:02]** generally only use the language models

**[08:02]** generally only use the language models if you think you're not smarter than the

**[08:04]** if you think you're not smarter than the

**[08:04]** if you think you're not smarter than the language model.

**[08:06]** language model.

**[08:06]** language model. Then when you have a lot of users and

**[08:08]** Then when you have a lot of users and

**[08:08]** Then when you have a lot of users and actual good product, you might get

**[08:10]** actual good product, you might get

**[08:10]** actual good product, you might get thousands of queries or tens of

**[08:12]** thousands of queries or tens of

**[08:12]** thousands of queries or tens of thousands of conversations and now you

**[08:14]** thousands of conversations and now you

**[08:14]** thousands of conversations and now you run into an issue where there's too much

**[08:15]** run into an issue where there's too much

**[08:15]** run into an issue where there's too much volume to manually review. There's too

**[08:17]** volume to manually review. There's too

**[08:17]** volume to manually review. There's too much detail in the conversations and

**[08:19]** much detail in the conversations and

**[08:19]** much detail in the conversations and you're not really going to be the expert

**[08:20]** you're not really going to be the expert

**[08:20]** you're not really going to be the expert that can actually figure out what is

**[08:22]** that can actually figure out what is

**[08:22]** that can actually figure out what is useful and what is good. And ultimately

**[08:25]** useful and what is good. And ultimately

**[08:25]** useful and what is good. And ultimately with these long conversations with tool

**[08:26]** with these long conversations with tool

**[08:26]** with these long conversations with tool calls and chains and reasoning steps,

**[08:28]** calls and chains and reasoning steps,

**[08:28]** calls and chains and reasoning steps, these outputs are now really hard to

**[08:30]** these outputs are now really hard to

**[08:30]** these outputs are now really hard to scan and really hard to understand. But

**[08:32]** scan and really hard to understand. But

**[08:32]** scan and really hard to understand. But there's still a lot of value in these

**[08:34]** there's still a lot of value in these

**[08:34]** there's still a lot of value in these conversations, right? If you've used a

**[08:36]** conversations, right? If you've used a

**[08:36]** conversations, right? If you've used a chatbot, whether it's in cursor or any

**[08:38]** chatbot, whether it's in cursor or any

**[08:38]** chatbot, whether it's in cursor or any kind of like cloud code system,

**[08:40]** kind of like cloud code system,

**[08:40]** kind of like cloud code system, oftentimes you do say things like, "Try

**[08:42]** oftentimes you do say things like, "Try

**[08:42]** oftentimes you do say things like, "Try again. This is not really what I meant,

**[08:43]** again. This is not really what I meant,

**[08:43]** again. This is not really what I meant, you know, be less lazy next time." It

**[08:46]** you know, be less lazy next time." It

**[08:46]** you know, be less lazy next time." It turns out a lot of the feedback you give

**[08:47]** turns out a lot of the feedback you give

**[08:48]** turns out a lot of the feedback you give is in those conversations, right? We

**[08:50]** is in those conversations, right? We

**[08:50]** is in those conversations, right? We could build things like feedback widgets

**[08:52]** could build things like feedback widgets

**[08:52]** could build things like feedback widgets or thumbs up or thumbs down, but a lot

**[08:54]** or thumbs up or thumbs down, but a lot

**[08:54]** or thumbs up or thumbs down, but a lot of the information exists in those

**[08:56]** of the information exists in those

**[08:56]** of the information exists in those conversations. and the frustration and

**[08:57]** conversations. and the frustration and

**[08:57]** conversations. and the frustration and the retry patterns that exist can be


### [09:00 - 10:00]

**[09:00]** the retry patterns that exist can be

**[09:00]** the retry patterns that exist can be extracted from those conversations and

**[09:02]** extracted from those conversations and

**[09:02]** extracted from those conversations and the idea is that the data really already

**[09:04]** the idea is that the data really already

**[09:04]** the idea is that the data really already exists in this conversation. If we think

**[09:07]** exists in this conversation. If we think

**[09:07]** exists in this conversation. If we think of a simple example in a different

**[09:09]** of a simple example in a different

**[09:09]** of a simple example in a different industry, you know, we can imagine the

**[09:11]** industry, you know, we can imagine the

**[09:11]** industry, you know, we can imagine the analogy of marketing, right? Maybe we

**[09:13]** analogy of marketing, right? Maybe we

**[09:13]** analogy of marketing, right? Maybe we run our evals and the number is 0.5. I

**[09:16]** run our evals and the number is 0.5. I

**[09:16]** run our evals and the number is 0.5. I don't really know what that means.

**[09:17]** don't really know what that means.

**[09:17]** don't really know what that means. Factuality is point6. I don't know if

**[09:18]** Factuality is point6. I don't know if

**[09:18]** Factuality is point6. I don't know if that's good or bad is 0.5. The average,

**[09:20]** that's good or bad is 0.5. The average,

**[09:20]** that's good or bad is 0.5. The average, who knows? But imagine we run a

**[09:23]** who knows? But imagine we run a

**[09:23]** who knows? But imagine we run a marketing campaign and our, you know, ad

**[09:25]** marketing campaign and our, you know, ad

**[09:25]** marketing campaign and our, you know, ad metric or our KPI is 0.5. There's not

**[09:28]** metric or our KPI is 0.5. There's not

**[09:28]** metric or our KPI is 0.5. There's not much we can do. But if we realize that

**[09:30]** much we can do. But if we realize that

**[09:30]** much we can do. But if we realize that 80% of our users are under 35 and 20%

**[09:33]** 80% of our users are under 35 and 20%

**[09:33]** 80% of our users are under 35 and 20% are over and we realize that the younger

**[09:35]** are over and we realize that the younger

**[09:35]** are over and we realize that the younger audience performs well and the older

**[09:36]** audience performs well and the older

**[09:36]** audience performs well and the older audience performs poorly. What we've

**[09:38]** audience performs poorly. What we've

**[09:38]** audience performs poorly. What we've done is we've just drawn a line in the

**[09:40]** done is we've just drawn a line in the

**[09:40]** done is we've just drawn a line in the sand on who our users are. And now we

**[09:42]** sand on who our users are. And now we

**[09:42]** sand on who our users are. And now we can make a decision. Do we want to

**[09:44]** can make a decision. Do we want to

**[09:44]** can make a decision. Do we want to double down on marketing to a younger

**[09:45]** double down on marketing to a younger

**[09:45]** double down on marketing to a younger audience or do we want to figure out why

**[09:48]** audience or do we want to figure out why

**[09:48]** audience or do we want to figure out why we aren't uh successfully marketing to

**[09:50]** we aren't uh successfully marketing to

**[09:50]** we aren't uh successfully marketing to to the older population, right? Do I

**[09:52]** to the older population, right? Do I

**[09:52]** to the older population, right? Do I find more part podcasts to market to?

**[09:54]** find more part podcasts to market to?

**[09:54]** find more part podcasts to market to? You know, should I run a Super Bowl ad?

**[09:56]** You know, should I run a Super Bowl ad?

**[09:56]** You know, should I run a Super Bowl ad? Now, just by drawing a line in the sand

**[09:58]** Now, just by drawing a line in the sand

**[09:58]** Now, just by drawing a line in the sand and deciding which segment to target, we


### [10:00 - 11:00]

**[10:00]** and deciding which segment to target, we

**[10:00]** and deciding which segment to target, we can now make decisions on what to

**[10:01]** can now make decisions on what to

**[10:01]** can now make decisions on what to improve. Whereas just making them ads

**[10:04]** improve. Whereas just making them ads

**[10:04]** improve. Whereas just making them ads better is a sort of very generic

**[10:05]** better is a sort of very generic

**[10:05]** better is a sort of very generic sentiment that people can have.

**[10:08]** sentiment that people can have.

**[10:08]** sentiment that people can have. And so one of the best ways of doing

**[10:10]** And so one of the best ways of doing

**[10:10]** And so one of the best ways of doing that is effectively just extracting some

**[10:12]** that is effectively just extracting some

**[10:12]** that is effectively just extracting some kind of data out of these conversations

**[10:13]** kind of data out of these conversations

**[10:13]** kind of data out of these conversations in some structured way and just doing

**[10:15]** in some structured way and just doing

**[10:15]** in some structured way and just doing very traditional data analysis. And so

**[10:17]** very traditional data analysis. And so

**[10:17]** very traditional data analysis. And so here we have some kind of object that

**[10:18]** here we have some kind of object that

**[10:18]** here we have some kind of object that says I want to extract a summary of what

**[10:20]** says I want to extract a summary of what

**[10:20]** says I want to extract a summary of what has happened. Maybe some tools that it's

**[10:22]** has happened. Maybe some tools that it's

**[10:22]** has happened. Maybe some tools that it's used maybe the errors that we've noticed

**[10:24]** used maybe the errors that we've noticed

**[10:24]** used maybe the errors that we've noticed the conversations that that happened.

**[10:26]** the conversations that that happened.

**[10:26]** the conversations that that happened. Maybe some metric for for satisfaction

**[10:28]** Maybe some metric for for satisfaction

**[10:28]** Maybe some metric for for satisfaction maybe some metric for frustration. The

**[10:30]** maybe some metric for frustration. The

**[10:30]** maybe some metric for frustration. The idea is that we can build this portfolio

**[10:32]** idea is that we can build this portfolio

**[10:32]** idea is that we can build this portfolio of metadata that we can extract. And

**[10:34]** of metadata that we can extract. And

**[10:34]** of metadata that we can extract. And then what we can do is we can embed this

**[10:36]** then what we can do is we can embed this

**[10:36]** then what we can do is we can embed this find clusters identify segments and then

**[10:38]** find clusters identify segments and then

**[10:38]** find clusters identify segments and then start testing our hypothesis.

**[10:44]** And so what we what we might want to do

**[10:44]** And so what we what we might want to do is sort of build this extraction, put

**[10:46]** is sort of build this extraction, put

**[10:46]** is sort of build this extraction, put into an LLM, get this data back out and

**[10:48]** into an LLM, get this data back out and

**[10:48]** into an LLM, get this data back out and just start doing very traditional data

**[10:49]** just start doing very traditional data

**[10:49]** just start doing very traditional data analysis, no different than any kind of

**[10:51]** analysis, no different than any kind of

**[10:52]** analysis, no different than any kind of uh product engineer or any kind of data

**[10:53]** uh product engineer or any kind of data

**[10:53]** uh product engineer or any kind of data scientist. And this tends to work quite

**[10:56]** scientist. And this tends to work quite

**[10:56]** scientist. And this tends to work quite well. You know, if you look at some of

**[10:57]** well. You know, if you look at some of

**[10:57]** well. You know, if you look at some of the things that Anthropic Cleo did, they

**[10:59]** the things that Anthropic Cleo did, they

**[10:59]** the things that Anthropic Cleo did, they basically found that, you know, uh code


### [11:00 - 12:00]

**[11:01]** basically found that, you know, uh code

**[11:01]** basically found that, you know, uh code use was 40x more represented by cloud

**[11:04]** use was 40x more represented by cloud

**[11:04]** use was 40x more represented by cloud cloud users than by you know uh GDP

**[11:07]** cloud users than by you know uh GDP

**[11:07]** cloud users than by you know uh GDP value creation. they go okay maybe code

**[11:09]** value creation. they go okay maybe code

**[11:09]** value creation. they go okay maybe code is like a good avenue and and obviously

**[11:11]** is like a good avenue and and obviously

**[11:11]** is like a good avenue and and obviously that's not the really the case but the

**[11:12]** that's not the really the case but the

**[11:12]** that's not the really the case but the idea is that by understanding how your

**[11:14]** idea is that by understanding how your

**[11:14]** idea is that by understanding how your users develop a product you can now

**[11:16]** users develop a product you can now

**[11:16]** users develop a product you can now figure out where to invest your time and

**[11:19]** figure out where to invest your time and

**[11:19]** figure out where to invest your time and so this is why we built a library called

**[11:20]** so this is why we built a library called

**[11:20]** so this is why we built a library called cura that allows us to summarize

**[11:22]** cura that allows us to summarize

**[11:22]** cura that allows us to summarize conversations cluster them build

**[11:24]** conversations cluster them build

**[11:24]** conversations cluster them build hierarchies of these clusters and

**[11:25]** hierarchies of these clusters and

**[11:25]** hierarchies of these clusters and ultimately allow us to compare our eval

**[11:28]** ultimately allow us to compare our eval

**[11:28]** ultimately allow us to compare our eval across different KPIs again so now you

**[11:31]** across different KPIs again so now you

**[11:31]** across different KPIs again so now you know if we have factuality is 6 that's

**[11:33]** know if we have factuality is 6 that's

**[11:33]** know if we have factuality is 6 that's really hard but if it turns out that

**[11:35]** really hard but if it turns out that

**[11:35]** really hard but if it turns out that factuality is really low for queries

**[11:36]** factuality is really low for queries

**[11:36]** factuality is really low for queries that require time filters, right? Or

**[11:39]** that require time filters, right? Or

**[11:39]** that require time filters, right? Or factuality is really high when queries

**[11:41]** factuality is really high when queries

**[11:41]** factuality is really high when queries revolve on, you know, contract search.

**[11:43]** revolve on, you know, contract search.

**[11:43]** revolve on, you know, contract search. Now we know something's happening in one

**[11:45]** Now we know something's happening in one

**[11:45]** Now we know something's happening in one area, something's happening in another.

**[11:46]** area, something's happening in another.

**[11:46]** area, something's happening in another. And then we can make a decision on what

**[11:48]** And then we can make a decision on what

**[11:48]** And then we can make a decision on what to do and how to invest our time. And

**[11:50]** to do and how to invest our time. And

**[11:50]** to do and how to invest our time. And the pipeline is pretty simple. We have

**[11:53]** the pipeline is pretty simple. We have

**[11:53]** the pipeline is pretty simple. We have models to do summarization, models to do

**[11:55]** models to do summarization, models to do

**[11:55]** models to do summarization, models to do clustering, and models that do this

**[11:57]** clustering, and models that do this

**[11:57]** clustering, and models that do this aggregation step.

**[11:59]** aggregation step.

**[11:59]** aggregation step. And so what you might want to do is just


### [12:00 - 13:00]

**[12:00]** And so what you might want to do is just

**[12:00]** And so what you might want to do is just load in some conversations. And here

**[12:02]** load in some conversations. And here

**[12:02]** load in some conversations. And here we've made some a fake data set, maybe

**[12:04]** we've made some a fake data set, maybe

**[12:04]** we've made some a fake data set, maybe conversations, fake conversations from

**[12:06]** conversations, fake conversations from

**[12:06]** conversations, fake conversations from Gemini. And the idea is that first we

**[12:09]** Gemini. And the idea is that first we

**[12:09]** Gemini. And the idea is that first we can extract some kind of summary model

**[12:12]** can extract some kind of summary model

**[12:12]** can extract some kind of summary model where there's topics that we discuss,

**[12:13]** where there's topics that we discuss,

**[12:13]** where there's topics that we discuss, frustrations, errors, etc. We can then

**[12:16]** frustrations, errors, etc. We can then

**[12:16]** frustrations, errors, etc. We can then cluster them to find cohesive groups.

**[12:19]** cluster them to find cohesive groups.

**[12:19]** cluster them to find cohesive groups. And here we can find maybe you know some

**[12:20]** And here we can find maybe you know some

**[12:20]** And here we can find maybe you know some of the conversations are around data

**[12:22]** of the conversations are around data

**[12:22]** of the conversations are around data visualization, SEO content requests and

**[12:24]** visualization, SEO content requests and

**[12:24]** visualization, SEO content requests and authentication errors. And now we get

**[12:26]** authentication errors. And now we get

**[12:26]** authentication errors. And now we get some idea of how people are using the

**[12:27]** some idea of how people are using the

**[12:27]** some idea of how people are using the software. And then as we group them

**[12:30]** software. And then as we group them

**[12:30]** software. And then as we group them together, we realize, okay, really there

**[12:31]** together, we realize, okay, really there

**[12:32]** together, we realize, okay, really there are some themes around technical

**[12:33]** are some themes around technical

**[12:33]** are some themes around technical support. Does the agent have tools that

**[12:35]** support. Does the agent have tools that

**[12:35]** support. Does the agent have tools that can do this? as well. Do we have tools

**[12:36]** can do this? as well. Do we have tools

**[12:36]** can do this? as well. Do we have tools to debug these database issues? Do we

**[12:38]** to debug these database issues? Do we

**[12:38]** to debug these database issues? Do we have tools to debug authentication? Do

**[12:40]** have tools to debug authentication? Do

**[12:40]** have tools to debug authentication? Do we have tools to do data visualization?

**[12:42]** we have tools to do data visualization?

**[12:42]** we have tools to do data visualization? Um, that's something that's going to be

**[12:43]** Um, that's something that's going to be

**[12:43]** Um, that's something that's going to be very useful. And at the end of this

**[12:45]** very useful. And at the end of this

**[12:46]** very useful. And at the end of this pipeline, we're sort of presented with

**[12:47]** pipeline, we're sort of presented with

**[12:47]** pipeline, we're sort of presented with these printouts of clusters, right? We

**[12:50]** these printouts of clusters, right? We

**[12:50]** these printouts of clusters, right? We know what the tools are, how the chatbot

**[12:52]** know what the tools are, how the chatbot

**[12:52]** know what the tools are, how the chatbot is being used at a higher level, you

**[12:54]** is being used at a higher level, you

**[12:54]** is being used at a higher level, you know, SEO, content, data analysis, and

**[12:56]** know, SEO, content, data analysis, and

**[12:56]** know, SEO, content, data analysis, and at a lower level, you know, maybe it's

**[12:57]** at a lower level, you know, maybe it's

**[12:57]** at a lower level, you know, maybe it's blog post and marketing. And just by

**[12:59]** blog post and marketing. And just by

**[12:59]** blog post and marketing. And just by looking at this, we might have some


### [13:00 - 14:00]

**[13:00]** looking at this, we might have some

**[13:00]** looking at this, we might have some hypothesis as to what kind of tools we

**[13:02]** hypothesis as to what kind of tools we

**[13:02]** hypothesis as to what kind of tools we should build, how we should, you know,

**[13:04]** should build, how we should, you know,

**[13:04]** should build, how we should, you know, develop, you know, even our marketing or

**[13:06]** develop, you know, even our marketing or

**[13:06]** develop, you know, even our marketing or how we can think about changing our

**[13:07]** how we can think about changing our

**[13:07]** how we can think about changing our prompts. We can do a ton of these kinds

**[13:09]** prompts. We can do a ton of these kinds

**[13:09]** prompts. We can do a ton of these kinds of things. And this is because the

**[13:11]** of things. And this is because the

**[13:11]** of things. And this is because the ultimate goal is to understand what to

**[13:13]** ultimate goal is to understand what to

**[13:13]** ultimate goal is to understand what to do next, right? You do the segmentation

**[13:15]** do next, right? You do the segmentation

**[13:15]** do next, right? You do the segmentation to figure out what kind of new

**[13:17]** to figure out what kind of new

**[13:17]** to figure out what kind of new hypotheses that you can have. And then

**[13:19]** hypotheses that you can have. And then

**[13:19]** hypotheses that you can have. And then you can make these targeted investments

**[13:21]** you can make these targeted investments

**[13:21]** you can make these targeted investments within these certain segments. If it

**[13:23]** within these certain segments. If it

**[13:23]** within these certain segments. If it turns out that, you know, 80% of the

**[13:25]** turns out that, you know, 80% of the

**[13:25]** turns out that, you know, 80% of the conversations that I'm having with the

**[13:26]** conversations that I'm having with the

**[13:26]** conversations that I'm having with the chatbot is around SEO optimization,

**[13:28]** chatbot is around SEO optimization,

**[13:28]** chatbot is around SEO optimization, maybe I should have some integrations

**[13:30]** maybe I should have some integrations

**[13:30]** maybe I should have some integrations that do that. Maybe I should reevaluate

**[13:32]** that do that. Maybe I should reevaluate

**[13:32]** that do that. Maybe I should reevaluate the prompts or have other workflows to

**[13:33]** the prompts or have other workflows to

**[13:33]** the prompts or have other workflows to make that use case more powerful for

**[13:35]** make that use case more powerful for

**[13:35]** make that use case more powerful for them. And again, the goal really is to

**[13:37]** them. And again, the goal really is to

**[13:37]** them. And again, the goal really is to just make a portfolio of tools of

**[13:40]** just make a portfolio of tools of

**[13:40]** just make a portfolio of tools of metadata filters of data sources that

**[13:42]** metadata filters of data sources that

**[13:42]** metadata filters of data sources that allows the agent to do its job. And

**[13:45]** allows the agent to do its job. And

**[13:45]** allows the agent to do its job. And oftent times the solution isn't really

**[13:46]** oftent times the solution isn't really

**[13:46]** oftent times the solution isn't really making the AI better. It's really just

**[13:48]** making the AI better. It's really just

**[13:48]** making the AI better. It's really just providing the right infrastructure.

**[13:50]** providing the right infrastructure.

**[13:50]** providing the right infrastructure. Right? A lot of times if you find that a

**[13:53]** Right? A lot of times if you find that a

**[13:53]** Right? A lot of times if you find that a lot of queries use time filters and you

**[13:54]** lot of queries use time filters and you

**[13:54]** lot of queries use time filters and you just didn't add a time filter that can

**[13:56]** just didn't add a time filter that can

**[13:56]** just didn't add a time filter that can probably improve your eval by quite a

**[13:58]** probably improve your eval by quite a

**[13:58]** probably improve your eval by quite a bit right we have situations where we


### [14:00 - 15:00]

**[14:00]** bit right we have situations where we

**[14:00]** bit right we have situations where we wanted to figure out if contracts were

**[14:01]** wanted to figure out if contracts were

**[14:02]** wanted to figure out if contracts were signed and if we just extracted one more

**[14:03]** signed and if we just extracted one more

**[14:03]** signed and if we just extracted one more step in the OCR process now we can do

**[14:05]** step in the OCR process now we can do

**[14:05]** step in the OCR process now we can do this large scale filters and figure out

**[14:07]** this large scale filters and figure out

**[14:07]** this large scale filters and figure out you know what data exists

**[14:10]** you know what data exists

**[14:10]** you know what data exists and generally the practice of improving

**[14:12]** and generally the practice of improving

**[14:12]** and generally the practice of improving your applications is pretty

**[14:13]** your applications is pretty

**[14:13]** your applications is pretty straightforward right we all know to

**[14:15]** straightforward right we all know to

**[14:15]** straightforward right we all know to define eval but not everyone that I work

**[14:17]** define eval but not everyone that I work

**[14:17]** define eval but not everyone that I work with has really been thinking about

**[14:18]** with has really been thinking about

**[14:18]** with has really been thinking about something like finding clusters and

**[14:19]** something like finding clusters and

**[14:20]** something like finding clusters and comparing KPIs across clusters. But once

**[14:22]** comparing KPIs across clusters. But once

**[14:22]** comparing KPIs across clusters. But once you do, then you can start making

**[14:24]** you do, then you can start making

**[14:24]** you do, then you can start making decisions on what to build, what to fix,

**[14:25]** decisions on what to build, what to fix,

**[14:25]** decisions on what to build, what to fix, and what to ignore. Maybe you have a

**[14:28]** and what to ignore. Maybe you have a

**[14:28]** and what to ignore. Maybe you have a two-sided uh quadrants, right? Maybe you

**[14:30]** two-sided uh quadrants, right? Maybe you

**[14:30]** two-sided uh quadrants, right? Maybe you have low usage and high usage, and you

**[14:33]** have low usage and high usage, and you

**[14:33]** have low usage and high usage, and you have high performing evals and low

**[14:35]** have high performing evals and low

**[14:35]** have high performing evals and low performing evals, right? If a large

**[14:38]** performing evals, right? If a large

**[14:38]** performing evals, right? If a large portion of your population are using

**[14:39]** portion of your population are using

**[14:40]** portion of your population are using tools that you are bad at, that is

**[14:41]** tools that you are bad at, that is

**[14:41]** tools that you are bad at, that is clearly the thing you have to fix. But

**[14:43]** clearly the thing you have to fix. But

**[14:43]** clearly the thing you have to fix. But if a large proportion of people are

**[14:45]** if a large proportion of people are

**[14:45]** if a large proportion of people are using tools that you're good at, that's

**[14:47]** using tools that you're good at, that's

**[14:47]** using tools that you're good at, that's totally fine. If a small proportion of

**[14:49]** totally fine. If a small proportion of

**[14:49]** totally fine. If a small proportion of people use something that do something

**[14:50]** people use something that do something

**[14:50]** people use something that do something that you're good at, maybe there's some

**[14:52]** that you're good at, maybe there's some

**[14:52]** that you're good at, maybe there's some product changes you need to make. Maybe

**[14:54]** product changes you need to make. Maybe

**[14:54]** product changes you need to make. Maybe it's about educating the user. Maybe

**[14:56]** it's about educating the user. Maybe

**[14:56]** it's about educating the user. Maybe it's adding some, you know, pre-filler

**[14:57]** it's adding some, you know, pre-filler

**[14:57]** it's adding some, you know, pre-filler or automated questions to show them that

**[14:59]** or automated questions to show them that

**[14:59]** or automated questions to show them that we can do these kind of capabilities.


### [15:00 - 16:00]

**[15:01]** we can do these kind of capabilities.

**[15:01]** we can do these kind of capabilities. And if there are things that nobody

**[15:02]** And if there are things that nobody

**[15:02]** And if there are things that nobody does, but when we do them, they're bad,

**[15:04]** does, but when we do them, they're bad,

**[15:04]** does, but when we do them, they're bad, maybe that's a oneline change in the

**[15:06]** maybe that's a oneline change in the

**[15:06]** maybe that's a oneline change in the prompt that says, "Sorry, I can't help

**[15:07]** prompt that says, "Sorry, I can't help

**[15:07]** prompt that says, "Sorry, I can't help you. Go talk to your manager." Right?

**[15:09]** you. Go talk to your manager." Right?

**[15:09]** you. Go talk to your manager." Right? These are now decisions that we can make

**[15:11]** These are now decisions that we can make

**[15:11]** These are now decisions that we can make just by looking at, you know, what

**[15:12]** just by looking at, you know, what

**[15:12]** just by looking at, you know, what proportion of our conversations are of a

**[15:14]** proportion of our conversations are of a

**[15:14]** proportion of our conversations are of a certain category and whether or not we

**[15:16]** certain category and whether or not we

**[15:16]** certain category and whether or not we can do well in that category. And as you

**[15:18]** can do well in that category. And as you

**[15:18]** can do well in that category. And as you understand this, then you can go out,

**[15:20]** understand this, then you can go out,

**[15:20]** understand this, then you can go out, you can build these classifiers to

**[15:21]** you can build these classifiers to

**[15:21]** you can build these classifiers to identify these specific intents. Maybe

**[15:23]** identify these specific intents. Maybe

**[15:23]** identify these specific intents. Maybe you build routers, maybe you build more

**[15:25]** you build routers, maybe you build more

**[15:25]** you build routers, maybe you build more tools. And then you can start doing

**[15:27]** tools. And then you can start doing

**[15:27]** tools. And then you can start doing things like monitoring and having the

**[15:28]** things like monitoring and having the

**[15:28]** things like monitoring and having the ability to do these group buys, right?

**[15:30]** ability to do these group buys, right?

**[15:30]** ability to do these group buys, right? So now you have different categories of

**[15:32]** So now you have different categories of

**[15:32]** So now you have different categories of query types over time and you can just

**[15:34]** query types over time and you can just

**[15:34]** query types over time and you can just see what the performance looks like,

**[15:36]** see what the performance looks like,

**[15:36]** see what the performance looks like, right? where 0.5 doesn't really mean

**[15:37]** right? where 0.5 doesn't really mean

**[15:37]** right? where 0.5 doesn't really mean anything but whether or not a metric

**[15:39]** anything but whether or not a metric

**[15:39]** anything but whether or not a metric changes over time across a certain

**[15:40]** changes over time across a certain

**[15:40]** changes over time across a certain category can determine a lot about how

**[15:42]** category can determine a lot about how

**[15:42]** category can determine a lot about how your products is being used. By doing

**[15:44]** your products is being used. By doing

**[15:44]** your products is being used. By doing this we figured out that you know some

**[15:46]** this we figured out that you know some

**[15:46]** this we figured out that you know some customers when we onboard them they they

**[15:48]** customers when we onboard them they they

**[15:48]** customers when we onboard them they they use our applications very differently

**[15:49]** use our applications very differently

**[15:49]** use our applications very differently than our historical customers and we can

**[15:51]** than our historical customers and we can

**[15:51]** than our historical customers and we can now then make other investments in how

**[15:52]** now then make other investments in how

**[15:52]** now then make other investments in how to improve these systems and ultimately

**[15:54]** to improve these systems and ultimately

**[15:54]** to improve these systems and ultimately the goal is to create a datadriven way

**[15:56]** the goal is to create a datadriven way

**[15:56]** the goal is to create a datadriven way of defining the product roadmap.

**[15:58]** of defining the product roadmap.

**[15:58]** of defining the product roadmap. Oftentimes it is research that leads to


### [16:00 - 17:00]

**[16:01]** Oftentimes it is research that leads to

**[16:01]** Oftentimes it is research that leads to better products now rather than products

**[16:03]** better products now rather than products

**[16:03]** better products now rather than products justifying some research that we don't

**[16:05]** justifying some research that we don't

**[16:05]** justifying some research that we don't know is possible.

**[16:07]** know is possible.

**[16:07]** know is possible. And again the real marker of progress is

**[16:11]** And again the real marker of progress is

**[16:11]** And again the real marker of progress is your ability to have a high quality

**[16:12]** your ability to have a high quality

**[16:12]** your ability to have a high quality hypothesis and your ability to test a

**[16:14]** hypothesis and your ability to test a

**[16:14]** hypothesis and your ability to test a lot of these hypotheses. And if you

**[16:16]** lot of these hypotheses. And if you

**[16:16]** lot of these hypotheses. And if you segment you can make clearer hypotheses.

**[16:19]** segment you can make clearer hypotheses.

**[16:19]** segment you can make clearer hypotheses. If you use faster evals you can run more

**[16:21]** If you use faster evals you can run more

**[16:21]** If you use faster evals you can run more experiments. And by having this

**[16:23]** experiments. And by having this

**[16:23]** experiments. And by having this continuous feedback through monitoring

**[16:25]** continuous feedback through monitoring

**[16:25]** continuous feedback through monitoring this is how you actually build a

**[16:26]** this is how you actually build a

**[16:26]** this is how you actually build a product. Right? This is regardless of

**[16:28]** product. Right? This is regardless of

**[16:28]** product. Right? This is regardless of being an AI product. This is just how

**[16:29]** being an AI product. This is just how

**[16:29]** being an AI product. This is just how you build a product.

**[16:32]** you build a product.

**[16:32]** you build a product. And so if you look at the takeaways

**[16:34]** And so if you look at the takeaways

**[16:34]** And so if you look at the takeaways really when you think about measuring

**[16:35]** really when you think about measuring

**[16:35]** really when you think about measuring the inputs, we really want to think

**[16:36]** the inputs, we really want to think

**[16:36]** the inputs, we really want to think about not using public benchmarks,

**[16:39]** about not using public benchmarks,

**[16:39]** about not using public benchmarks, building evals on your data and focusing

**[16:41]** building evals on your data and focusing

**[16:41]** building evals on your data and focusing first on retrieval because that is the

**[16:44]** first on retrieval because that is the

**[16:44]** first on retrieval because that is the only thing a LLM improvement won't fix,

**[16:47]** only thing a LLM improvement won't fix,

**[16:47]** only thing a LLM improvement won't fix, right? If the retrieval is bad, the LLM

**[16:49]** right? If the retrieval is bad, the LLM

**[16:49]** right? If the retrieval is bad, the LLM will still get better over time, but you

**[16:51]** will still get better over time, but you

**[16:51]** will still get better over time, but you need to earn the right to sort of twink

**[16:52]** need to earn the right to sort of twink

**[16:52]** need to earn the right to sort of twink tinker with the LLM by having good

**[16:55]** tinker with the LLM by having good

**[16:55]** tinker with the LLM by having good retrieval. And then lastly, if you don't

**[16:57]** retrieval. And then lastly, if you don't

**[16:57]** retrieval. And then lastly, if you don't have any customers or any users, you can

**[16:59]** have any customers or any users, you can

**[16:59]** have any customers or any users, you can start thinking about synthetic data as a


### [17:00 - 18:00]

**[17:00]** start thinking about synthetic data as a

**[17:00]** start thinking about synthetic data as a way of augmenting that. And once you

**[17:02]** way of augmenting that. And once you

**[17:02]** way of augmenting that. And once you have users, look at your data as well.

**[17:04]** have users, look at your data as well.

**[17:04]** have users, look at your data as well. Look at the outputs, right? Extract

**[17:07]** Look at the outputs, right? Extract

**[17:07]** Look at the outputs, right? Extract structure from these conversations.

**[17:09]** structure from these conversations.

**[17:09]** structure from these conversations. Understand, you know, how many

**[17:10]** Understand, you know, how many

**[17:10]** Understand, you know, how many conversations are happening? How often

**[17:12]** conversations are happening? How often

**[17:12]** conversations are happening? How often are tools being misused? What are the

**[17:14]** are tools being misused? What are the

**[17:14]** are tools being misused? What are the errors? And how are people frustrated?

**[17:15]** errors? And how are people frustrated?

**[17:15]** errors? And how are people frustrated? And by doing that, you can do this

**[17:17]** And by doing that, you can do this

**[17:17]** And by doing that, you can do this population level data analysis, find

**[17:19]** population level data analysis, find

**[17:19]** population level data analysis, find these similar clusters, and have some

**[17:21]** these similar clusters, and have some

**[17:21]** these similar clusters, and have some kind of impact weighted understanding of

**[17:23]** kind of impact weighted understanding of

**[17:23]** kind of impact weighted understanding of what the tools are. Right? It's one

**[17:25]** what the tools are. Right? It's one

**[17:25]** what the tools are. Right? It's one thing to say, you know, maybe we should

**[17:27]** thing to say, you know, maybe we should

**[17:27]** thing to say, you know, maybe we should build more tools for data visualization.

**[17:29]** build more tools for data visualization.

**[17:29]** build more tools for data visualization. It's another thing to say, hey boss, 40%

**[17:31]** It's another thing to say, hey boss, 40%

**[17:31]** It's another thing to say, hey boss, 40% of our conversations are around data

**[17:33]** of our conversations are around data

**[17:33]** of our conversations are around data visualization and the, you know, the

**[17:35]** visualization and the, you know, the

**[17:35]** visualization and the, you know, the code engine or the code execution can't

**[17:37]** code engine or the code execution can't

**[17:37]** code engine or the code execution can't really do that well. Maybe we should

**[17:38]** really do that well. Maybe we should

**[17:38]** really do that well. Maybe we should build two more tools for plotting and

**[17:40]** build two more tools for plotting and

**[17:40]** build two more tools for plotting and then see if that's worth it. And you can

**[17:42]** then see if that's worth it. And you can

**[17:42]** then see if that's worth it. And you can justify that because we know there's a

**[17:43]** justify that because we know there's a

**[17:44]** justify that because we know there's a 40% of the population is using data

**[17:46]** 40% of the population is using data

**[17:46]** 40% of the population is using data visualization and we do that, you know,

**[17:47]** visualization and we do that, you know,

**[17:47]** visualization and we do that, you know, maybe only 10% of the time, right? This

**[17:49]** maybe only 10% of the time, right? This

**[17:49]** maybe only 10% of the time, right? This is impact weighted. And ultimately as

**[17:52]** is impact weighted. And ultimately as

**[17:52]** is impact weighted. And ultimately as you compare these KPIs across these

**[17:54]** you compare these KPIs across these

**[17:54]** you compare these KPIs across these clusters, you can just make better

**[17:55]** clusters, you can just make better

**[17:55]** clusters, you can just make better decisions across your entire product

**[17:57]** decisions across your entire product

**[17:57]** decisions across your entire product development process. So again, start


### [18:00 - 19:00]

**[18:00]** development process. So again, start

**[18:00]** development process. So again, start small, look for structure, understand

**[18:02]** small, look for structure, understand

**[18:02]** small, look for structure, understand that structure, and start comparing your

**[18:04]** that structure, and start comparing your

**[18:04]** that structure, and start comparing your KPIs. And once you can do that, you can

**[18:06]** KPIs. And once you can do that, you can

**[18:06]** KPIs. And once you can do that, you can make decisions on what to fix, what to

**[18:08]** make decisions on what to fix, what to

**[18:08]** make decisions on what to fix, what to build, and what to ignore.

**[18:11]** build, and what to ignore.

**[18:11]** build, and what to ignore. If you want to find more resources, feel

**[18:13]** If you want to find more resources, feel

**[18:13]** If you want to find more resources, feel free to check out these QR codes. Uh the

**[18:14]** free to check out these QR codes. Uh the

**[18:14]** free to check out these QR codes. Uh the first one is the Chroma cloud to

**[18:16]** first one is the Chroma cloud to

**[18:16]** first one is the Chroma cloud to understand a little bit more about their

**[18:17]** understand a little bit more about their

**[18:17]** understand a little bit more about their research. And the second one is actually

**[18:18]** research. And the second one is actually

**[18:18]** research. And the second one is actually a set of notebooks that we've built out

**[18:20]** a set of notebooks that we've built out

**[18:20]** a set of notebooks that we've built out that go through this process. So we load

**[18:22]** that go through this process. So we load

**[18:22]** that go through this process. So we load the weights and biases conversations. We

**[18:25]** the weights and biases conversations. We

**[18:25]** the weights and biases conversations. We do this cluster analysis and we show you

**[18:27]** do this cluster analysis and we show you

**[18:27]** do this cluster analysis and we show you how we can use that to make better

**[18:28]** how we can use that to make better

**[18:28]** how we can use that to make better product decisions. So there's three

**[18:30]** product decisions. So there's three

**[18:30]** product decisions. So there's three Jupyter notebooks in that repo. Check

**[18:31]** Jupyter notebooks in that repo. Check

**[18:31]** Jupyter notebooks in that repo. Check them out on your own time. And uh thank

**[18:33]** them out on your own time. And uh thank

**[18:33]** them out on your own time. And uh thank you for listening. We do have time for

**[18:37]** you for listening. We do have time for

**[18:38]** you for listening. We do have time for we do have time for like one quick

**[18:39]** we do have time for like one quick

**[18:39]** we do have time for like one quick question and of course as well outside

**[18:41]** question and of course as well outside

**[18:41]** question and of course as well outside as well. So thank you if anybody wants

**[18:44]** as well. So thank you if anybody wants

**[18:44]** as well. So thank you if anybody wants to grab the mic there and over there.

**[18:52]** Y

**[18:52]** Y for spicy. What's the spicy take today?


### [19:00 - 20:00]

**[19:00]** It's not KPI, by the way. That's not the

**[19:00]** It's not KPI, by the way. That's not the spicy. I think I think more agent

**[19:03]** spicy. I think I think more agent

**[19:03]** spicy. I think I think more agent businesses should try to price and like

**[19:05]** businesses should try to price and like

**[19:05]** businesses should try to price and like price their services on the work done

**[19:07]** price their services on the work done

**[19:07]** price their services on the work done than the tokens used. Yeah. Price on

**[19:10]** than the tokens used. Yeah. Price on

**[19:10]** than the tokens used. Yeah. Price on success, price on value. Very unrelated

**[19:13]** success, price on value. Very unrelated

**[19:13]** success, price on value. Very unrelated to this talk, but

**[19:15]** to this talk, but

**[19:15]** to this talk, but [Music]


