# Memory in LLMs- Weights and Activations - Jack Morris, Cornell

**Video URL:** https://youtu.be/Jty4s9-Jb78

---

## Full Transcript

### [00:00 - 01:00]

**[00:22]** Let's talk about Chad GBT. I think like

**[00:22]** Let's talk about Chad GBT. I think like Chad GBT knows a lot of things. It's

**[00:25]** Chad GBT knows a lot of things. It's

**[00:25]** Chad GBT knows a lot of things. It's actually extremely impressive. I use it

**[00:27]** actually extremely impressive. I use it

**[00:27]** actually extremely impressive. I use it all the time. I used it to help prepare

**[00:29]** all the time. I used it to help prepare

**[00:29]** all the time. I used it to help prepare for the presentation. I used it to cook

**[00:31]** for the presentation. I used it to cook

**[00:31]** for the presentation. I used it to cook last night. Um, you know, very like

**[00:34]** last night. Um, you know, very like

**[00:34]** last night. Um, you know, very like growing increasingly dependent. And yet,

**[00:37]** growing increasingly dependent. And yet,

**[00:37]** growing increasingly dependent. And yet, there's a lot that Chad doesn't know.

**[00:39]** there's a lot that Chad doesn't know.

**[00:39]** there's a lot that Chad doesn't know. Like, um, it didn't know why my speaker

**[00:41]** Like, um, it didn't know why my speaker

**[00:41]** Like, um, it didn't know why my speaker pass wasn't working when I was trying to

**[00:43]** pass wasn't working when I was trying to

**[00:43]** pass wasn't working when I was trying to get into the building and it uh, if you

**[00:46]** get into the building and it uh, if you

**[00:46]** get into the building and it uh, if you ask it, did the Blue Jays win the World

**[00:48]** ask it, did the Blue Jays win the World

**[00:48]** ask it, did the Blue Jays win the World Series? The answer is no. And I know

**[00:49]** Series? The answer is no. And I know

**[00:49]** Series? The answer is no. And I know that because I watch the World Series,

**[00:51]** that because I watch the World Series,

**[00:51]** that because I watch the World Series, but Chad GBT doesn't know that if you

**[00:52]** but Chad GBT doesn't know that if you

**[00:52]** but Chad GBT doesn't know that if you don't enable web search because it has

**[00:54]** don't enable web search because it has

**[00:54]** don't enable web search because it has something called a knowledge cut off. So

**[00:55]** something called a knowledge cut off. So

**[00:55]** something called a knowledge cut off. So all the training data is kind of

**[00:58]** all the training data is kind of

**[00:58]** all the training data is kind of segmented by date and things after a


### [01:00 - 02:00]

**[01:00]** segmented by date and things after a

**[01:00]** segmented by date and things after a certain date are not known by chbttt

**[01:03]** certain date are not known by chbttt

**[01:03]** certain date are not known by chbttt like unilaterally. Uh if you ask jbt

**[01:06]** like unilaterally. Uh if you ask jbt

**[01:06]** like unilaterally. Uh if you ask jbt help me optimize this kernel I wrote for

**[01:08]** help me optimize this kernel I wrote for

**[01:08]** help me optimize this kernel I wrote for AMD GPUs it's so bad at it and I think

**[01:12]** AMD GPUs it's so bad at it and I think

**[01:12]** AMD GPUs it's so bad at it and I think there's a few reasons for this. One it's

**[01:13]** there's a few reasons for this. One it's

**[01:13]** there's a few reasons for this. One it's really hard. Two uh there's not a lot of

**[01:16]** really hard. Two uh there's not a lot of

**[01:16]** really hard. Two uh there's not a lot of data for it. But three I think it's more

**[01:19]** data for it. But three I think it's more

**[01:19]** data for it. But three I think it's more that the data that does exist is such a

**[01:22]** that the data that does exist is such a

**[01:22]** that the data that does exist is such a small portion of its training data that

**[01:23]** small portion of its training data that

**[01:23]** small portion of its training data that it just like can't do it very well. And

**[01:25]** it just like can't do it very well. And

**[01:25]** it just like can't do it very well. And so a lot of tasks like this which I I

**[01:27]** so a lot of tasks like this which I I

**[01:27]** so a lot of tasks like this which I I would guess a lot of you face in your

**[01:29]** would guess a lot of you face in your

**[01:29]** would guess a lot of you face in your jobs like the things that are more niche

**[01:31]** jobs like the things that are more niche

**[01:31]** jobs like the things that are more niche or here I call longtail are really hard

**[01:34]** or here I call longtail are really hard

**[01:34]** or here I call longtail are really hard for Chad GBT to do even if you say

**[01:36]** for Chad GBT to do even if you say

**[01:36]** for Chad GBT to do even if you say please like please [laughter] or like I

**[01:39]** please like please [laughter] or like I

**[01:39]** please like please [laughter] or like I want you to learn more about this or

**[01:41]** want you to learn more about this or

**[01:41]** want you to learn more about this or practice like it can't learn more about

**[01:42]** practice like it can't learn more about

**[01:42]** practice like it can't learn more about this it can't practice it it doesn't

**[01:44]** this it can't practice it it doesn't

**[01:44]** this it can't practice it it doesn't know uh what to do when you ask it that

**[01:47]** know uh what to do when you ask it that

**[01:47]** know uh what to do when you ask it that and uh yeah if you ask what are the

**[01:49]** and uh yeah if you ask what are the

**[01:49]** and uh yeah if you ask what are the terms of our partnership agreement for

**[01:50]** terms of our partnership agreement for

**[01:50]** terms of our partnership agreement for Black Rockck it doesn't know about your

**[01:51]** Black Rockck it doesn't know about your

**[01:51]** Black Rockck it doesn't know about your company which any shirts should I order

**[01:53]** company which any shirts should I order

**[01:53]** company which any shirts should I order from Amazon on implement a new feature

**[01:56]** from Amazon on implement a new feature

**[01:56]** from Amazon on implement a new feature uh in our company monor repo. Write an

**[01:59]** uh in our company monor repo. Write an

**[01:59]** uh in our company monor repo. Write an email in my style. Diagnose this patient


### [02:00 - 03:00]

**[02:02]** email in my style. Diagnose this patient

**[02:02]** email in my style. Diagnose this patient given their history. What arguments did

**[02:04]** given their history. What arguments did

**[02:04]** given their history. What arguments did the opposing council use in the Martinez

**[02:05]** the opposing council use in the Martinez

**[02:05]** the opposing council use in the Martinez settlement negotiations? Uh is this

**[02:08]** settlement negotiations? Uh is this

**[02:08]** settlement negotiations? Uh is this question already answered on our company

**[02:10]** question already answered on our company

**[02:10]** question already answered on our company internal wiki? Like none of these things

**[02:12]** internal wiki? Like none of these things

**[02:12]** internal wiki? Like none of these things are

**[02:13]** are

**[02:13]** are possibly answered by chatbt because

**[02:15]** possibly answered by chatbt because

**[02:15]** possibly answered by chatbt because they're not in the training data or

**[02:16]** they're not in the training data or

**[02:16]** they're not in the training data or they're too niche or they require some

**[02:18]** they're too niche or they require some

**[02:18]** they're too niche or they require some data that's not available to it. So I

**[02:21]** data that's not available to it. So I

**[02:21]** data that's not available to it. So I think like the question I want to talk

**[02:22]** think like the question I want to talk

**[02:22]** think like the question I want to talk about today is like what's the

**[02:24]** about today is like what's the

**[02:24]** about today is like what's the [clears throat] right way to solve this

**[02:25]** [clears throat] right way to solve this

**[02:25]** [clears throat] right way to solve this problem? Like if we want to build new

**[02:26]** problem? Like if we want to build new

**[02:26]** problem? Like if we want to build new systems that actually know the things we

**[02:29]** systems that actually know the things we

**[02:29]** systems that actually know the things we want them to know. Uh how how should we

**[02:30]** want them to know. Uh how how should we

**[02:30]** want them to know. Uh how how should we build them? And I think like the way I

**[02:33]** build them? And I think like the way I

**[02:33]** build them? And I think like the way I want to think about it is like how do we

**[02:35]** want to think about it is like how do we

**[02:35]** want to think about it is like how do we take some knowledge and inject it into

**[02:38]** take some knowledge and inject it into

**[02:38]** take some knowledge and inject it into the parameters of the model? Like what's

**[02:39]** the parameters of the model? Like what's

**[02:40]** the parameters of the model? Like what's the right way to do this? And like the

**[02:42]** the right way to do this? And like the

**[02:42]** the right way to do this? And like the way that I think about it and I think

**[02:44]** way that I think about it and I think

**[02:44]** way that I think about it and I think the way this manifests in my research

**[02:45]** the way this manifests in my research

**[02:45]** the way this manifests in my research and other people's research is there's

**[02:47]** and other people's research is there's

**[02:47]** and other people's research is there's three ways. There's full context. you

**[02:50]** three ways. There's full context. you

**[02:50]** three ways. There's full context. you can take as much stuff as you can and

**[02:52]** can take as much stuff as you can and

**[02:52]** can take as much stuff as you can and cram it into the language model. There's

**[02:54]** cram it into the language model. There's

**[02:54]** cram it into the language model. There's rag or retrieval augmented generation

**[02:56]** rag or retrieval augmented generation

**[02:56]** rag or retrieval augmented generation where you have so many things that you

**[02:58]** where you have so many things that you

**[02:58]** where you have so many things that you can't fit them all in and so you

**[02:59]** can't fit them all in and so you

**[02:59]** can't fit them all in and so you retrieve the most useful ones and then


### [03:00 - 04:00]

**[03:03]** retrieve the most useful ones and then

**[03:03]** retrieve the most useful ones and then feed them in. And then there's this

**[03:05]** feed them in. And then there's this

**[03:05]** feed them in. And then there's this third thing which I think is like really

**[03:07]** third thing which I think is like really

**[03:07]** third thing which I think is like really new and no one is doing it yet which is

**[03:09]** new and no one is doing it yet which is

**[03:09]** new and no one is doing it yet which is training things into weights. And I want

**[03:10]** training things into weights. And I want

**[03:10]** training things into weights. And I want what I mostly want to talk about today

**[03:12]** what I mostly want to talk about today

**[03:12]** what I mostly want to talk about today is like why I think we should be

**[03:14]** is like why I think we should be

**[03:14]** is like why I think we should be training things into weights. But I'm

**[03:16]** training things into weights. But I'm

**[03:16]** training things into weights. But I'm going to start with the other two. And

**[03:18]** going to start with the other two. And

**[03:18]** going to start with the other two. And also, I guess like along the way, about

**[03:20]** also, I guess like along the way, about

**[03:20]** also, I guess like along the way, about 10% of the time, I'm going to be

**[03:22]** 10% of the time, I'm going to be

**[03:22]** 10% of the time, I'm going to be shilling my own research, but I'm gonna

**[03:24]** shilling my own research, but I'm gonna

**[03:24]** shilling my own research, but I'm gonna like try to be honest about it. And you

**[03:25]** like try to be honest about it. And you

**[03:26]** like try to be honest about it. And you can just tune me out if you want.

**[03:28]** can just tune me out if you want.

**[03:28]** can just tune me out if you want. So, I think like the easiest way to

**[03:30]** So, I think like the easiest way to

**[03:30]** So, I think like the easiest way to solve these problems is to put

**[03:31]** solve these problems is to put

**[03:31]** solve these problems is to put everything into context. It's like if

**[03:33]** everything into context. It's like if

**[03:33]** everything into context. It's like if you work at a small company or um all

**[03:36]** you work at a small company or um all

**[03:36]** you work at a small company or um all you care about is like maybe the 100

**[03:39]** you care about is like maybe the 100

**[03:39]** you care about is like maybe the 100 world series that have occurred, you can

**[03:41]** world series that have occurred, you can

**[03:41]** world series that have occurred, you can kind of copy all the data and paste it

**[03:43]** kind of copy all the data and paste it

**[03:43]** kind of copy all the data and paste it into chat GPT or paste it into croc or

**[03:45]** into chat GPT or paste it into croc or

**[03:45]** into chat GPT or paste it into croc or whatever model you use. And that's

**[03:48]** whatever model you use. And that's

**[03:48]** whatever model you use. And that's finite enough that the model can

**[03:50]** finite enough that the model can

**[03:50]** finite enough that the model can understand.

**[03:51]** understand.

**[03:51]** understand. And this like works works pretty well. I

**[03:54]** And this like works works pretty well. I

**[03:54]** And this like works works pretty well. I think that this is something that got

**[03:55]** think that this is something that got

**[03:56]** think that this is something that got people really excited for a while a few

**[03:57]** people really excited for a while a few

**[03:57]** people really excited for a while a few years ago. I have this example of like a

**[03:59]** years ago. I have this example of like a

**[03:59]** years ago. I have this example of like a doctor answering a question from a


### [04:00 - 05:00]

**[04:01]** doctor answering a question from a

**[04:01]** doctor answering a question from a medical record. a medical record is

**[04:03]** medical record. a medical record is

**[04:03]** medical record. a medical record is small enough that it can presumably be

**[04:05]** small enough that it can presumably be

**[04:05]** small enough that it can presumably be like inputed into the context of the

**[04:07]** like inputed into the context of the

**[04:07]** like inputed into the context of the model and the model can do pretty well.

**[04:09]** model and the model can do pretty well.

**[04:09]** model and the model can do pretty well. I think there's a few problems with

**[04:10]** I think there's a few problems with

**[04:10]** I think there's a few problems with this. Maybe the main one is just that

**[04:13]** this. Maybe the main one is just that

**[04:13]** this. Maybe the main one is just that it's so expensive. Like if you do

**[04:15]** it's so expensive. Like if you do

**[04:15]** it's so expensive. Like if you do anything like this in your day-to-day

**[04:16]** anything like this in your day-to-day

**[04:16]** anything like this in your day-to-day workflow, you put like a ton of tokens

**[04:18]** workflow, you put like a ton of tokens

**[04:18]** workflow, you put like a ton of tokens into context and start generating. I

**[04:20]** into context and start generating. I

**[04:20]** into context and start generating. I mean, one, it's going to cost a lot of

**[04:22]** mean, one, it's going to cost a lot of

**[04:22]** mean, one, it's going to cost a lot of money, like US dollars, but two, it's

**[04:25]** money, like US dollars, but two, it's

**[04:25]** money, like US dollars, but two, it's just so slow. like um you know a few

**[04:29]** just so slow. like um you know a few

**[04:29]** just so slow. like um you know a few months ago I was writing my thesis and I

**[04:31]** months ago I was writing my thesis and I

**[04:31]** months ago I was writing my thesis and I wrote it myself but I did ask for some

**[04:33]** wrote it myself but I did ask for some

**[04:34]** wrote it myself but I did ask for some feedback a few times from Claude and

**[04:36]** feedback a few times from Claude and

**[04:36]** feedback a few times from Claude and like the second you paste in I I don't

**[04:38]** like the second you paste in I I don't

**[04:38]** like the second you paste in I I don't know it's like

**[04:39]** know it's like

**[04:39]** know it's like >> maybe 80 pages of text or something like

**[04:42]** >> maybe 80 pages of text or something like

**[04:42]** >> maybe 80 pages of text or something like as documents go it's medium length I

**[04:46]** as documents go it's medium length I

**[04:46]** as documents go it's medium length I paste into claude the second you paste

**[04:47]** paste into claude the second you paste

**[04:47]** paste into claude the second you paste into claude everything slows down by 10x

**[04:49]** into claude everything slows down by 10x

**[04:49]** into claude everything slows down by 10x or something I have this set here that

**[04:51]** or something I have this set here that

**[04:51]** or something I have this set here that if you have 1,000 tokens of context

**[04:54]** if you have 1,000 tokens of context

**[04:54]** if you have 1,000 tokens of context >> we can output 10,000 tokens per second.

**[04:57]** >> we can output 10,000 tokens per second.

**[04:57]** >> we can output 10,000 tokens per second. If you have 128k per to 128k tokens of


### [05:00 - 06:00]

**[05:01]** If you have 128k per to 128k tokens of

**[05:01]** If you have 128k per to 128k tokens of context, we can output 130 tokens per

**[05:03]** context, we can output 130 tokens per

**[05:03]** context, we can output 130 tokens per second. So that's like several orders of

**[05:05]** second. So that's like several orders of

**[05:05]** second. So that's like several orders of magnitude slowdown and I think we've all

**[05:06]** magnitude slowdown and I think we've all

**[05:06]** magnitude slowdown and I think we've all faced this. So it's very annoying and

**[05:08]** faced this. So it's very annoying and

**[05:08]** faced this. So it's very annoying and it's hard to imagine how we can get

**[05:10]** it's hard to imagine how we can get

**[05:10]** it's hard to imagine how we can get around this. Um I'll give you like the

**[05:13]** around this. Um I'll give you like the

**[05:13]** around this. Um I'll give you like the quick background from the research world

**[05:16]** quick background from the research world

**[05:16]** quick background from the research world which maybe people know which is this

**[05:17]** which maybe people know which is this

**[05:18]** which maybe people know which is this inherent limitation the models we use.

**[05:20]** inherent limitation the models we use.

**[05:20]** inherent limitation the models we use. The models we use are transformers.

**[05:21]** The models we use are transformers.

**[05:21]** The models we use are transformers. Transformers look like this. The real

**[05:23]** Transformers look like this. The real

**[05:23]** Transformers look like this. The real problem with transformers comes in this

**[05:27]** problem with transformers comes in this

**[05:27]** problem with transformers comes in this one little uh box right here called self

**[05:29]** one little uh box right here called self

**[05:29]** one little uh box right here called self attention. The problem is that all of

**[05:32]** attention. The problem is that all of

**[05:32]** attention. The problem is that all of the words that go into the transformer

**[05:33]** the words that go into the transformer

**[05:33]** the words that go into the transformer need to look at each other. And this has

**[05:35]** need to look at each other. And this has

**[05:35]** need to look at each other. And this has a quadratic dependency. So if there's

**[05:37]** a quadratic dependency. So if there's

**[05:37]** a quadratic dependency. So if there's four words, four tokens, maybe the

**[05:39]** four words, four tokens, maybe the

**[05:39]** four words, four tokens, maybe the matrix has 16 entries. If there are 12

**[05:41]** matrix has 16 entries. If there are 12

**[05:41]** matrix has 16 entries. If there are 12 tokens, there are 144 entries. And we

**[05:44]** tokens, there are 144 entries. And we

**[05:44]** tokens, there are 144 entries. And we can manage this for a while, but at some

**[05:46]** can manage this for a while, but at some

**[05:46]** can manage this for a while, but at some point it becomes infeasible. Like

**[05:48]** point it becomes infeasible. Like

**[05:48]** point it becomes infeasible. Like especially from a memory perspective, we

**[05:50]** especially from a memory perspective, we

**[05:50]** especially from a memory perspective, we can't

**[05:50]** can't

**[05:50]** can't >> hold the mic. From a memory perspective,

**[05:53]** >> hold the mic. From a memory perspective,

**[05:53]** >> hold the mic. From a memory perspective, we can't keep all these things in

**[05:54]** we can't keep all these things in

**[05:54]** we can't keep all these things in context.

**[05:56]** context.

**[05:56]** context. You might say, well, Jack, Grock 4 has

**[05:58]** You might say, well, Jack, Grock 4 has

**[05:58]** You might say, well, Jack, Grock 4 has two million token context window. Yeah,


### [06:00 - 07:00]

**[06:02]** two million token context window. Yeah,

**[06:02]** two million token context window. Yeah, 2 million token context window. It's

**[06:04]** 2 million token context window. It's

**[06:04]** 2 million token context window. It's it's a very large number. Gemini 3

**[06:06]** it's a very large number. Gemini 3

**[06:06]** it's a very large number. Gemini 3 dropped uh during this conference and

**[06:08]** dropped uh during this conference and

**[06:08]** dropped uh during this conference and Gemini 3 has 1 million token context

**[06:10]** Gemini 3 has 1 million token context

**[06:10]** Gemini 3 has 1 million token context window. You also might ask why did

**[06:13]** window. You also might ask why did

**[06:13]** window. You also might ask why did Gemini 3 not do a larger context window

**[06:15]** Gemini 3 not do a larger context window

**[06:15]** Gemini 3 not do a larger context window even though it came after Grock? And I

**[06:18]** even though it came after Grock? And I

**[06:18]** even though it came after Grock? And I think the reason is because there's

**[06:19]** think the reason is because there's

**[06:19]** think the reason is because there's [clears throat] a difference between the

**[06:21]** [clears throat] a difference between the

**[06:21]** [clears throat] a difference between the model not breaking when you put in that

**[06:23]** model not breaking when you put in that

**[06:23]** model not breaking when you put in that many tokens and the model actually like

**[06:25]** many tokens and the model actually like

**[06:26]** many tokens and the model actually like properly reasoning across many large

**[06:29]** properly reasoning across many large

**[06:29]** properly reasoning across many large chunks of tokens. And I think the second

**[06:32]** chunks of tokens. And I think the second

**[06:32]** chunks of tokens. And I think the second part we're still figuring out. I think

**[06:34]** part we're still figuring out. I think

**[06:34]** part we're still figuring out. I think people have realized how to train models

**[06:36]** people have realized how to train models

**[06:36]** people have realized how to train models that don't break with more and more

**[06:38]** that don't break with more and more

**[06:38]** that don't break with more and more tokens, but we haven't really gotten to

**[06:39]** tokens, but we haven't really gotten to

**[06:40]** tokens, but we haven't really gotten to the point where we can train models that

**[06:42]** the point where we can train models that

**[06:42]** the point where we can train models that truly work as well on a million tokens

**[06:44]** truly work as well on a million tokens

**[06:44]** truly work as well on a million tokens as they do on a thousand tokens. And if

**[06:47]** as they do on a thousand tokens. And if

**[06:47]** as they do on a thousand tokens. And if you're more curious about this, there's

**[06:48]** you're more curious about this, there's

**[06:48]** you're more curious about this, there's this really good report from Chroma

**[06:50]** this really good report from Chroma

**[06:50]** this really good report from Chroma called context context broad um about

**[06:54]** called context context broad um about

**[06:54]** called context context broad um about how performance degrades when you add

**[06:57]** how performance degrades when you add

**[06:57]** how performance degrades when you add just like other stuff into the context.

**[06:59]** just like other stuff into the context.

**[06:59]** just like other stuff into the context. So this graph shows like the larger the


### [07:00 - 08:00]

**[07:02]** So this graph shows like the larger the

**[07:02]** So this graph shows like the larger the context grows even with the same finite

**[07:04]** context grows even with the same finite

**[07:04]** context grows even with the same finite amount of relevant information, the LLMs

**[07:06]** amount of relevant information, the LLMs

**[07:06]** amount of relevant information, the LLMs get worse and worse. And I think like

**[07:09]** get worse and worse. And I think like

**[07:09]** get worse and worse. And I think like two things to observe here that I think

**[07:10]** two things to observe here that I think

**[07:10]** two things to observe here that I think are interesting. One, claw is the best

**[07:12]** are interesting. One, claw is the best

**[07:12]** are interesting. One, claw is the best by far. I like graphs like this because

**[07:14]** by far. I like graphs like this because

**[07:14]** by far. I like graphs like this because I feel like if you talk to people, a lot

**[07:16]** I feel like if you talk to people, a lot

**[07:16]** I feel like if you talk to people, a lot of people think clot is the best, but if

**[07:18]** of people think clot is the best, but if

**[07:18]** of people think clot is the best, but if you measure on a lot of standard

**[07:20]** you measure on a lot of standard

**[07:20]** you measure on a lot of standard benchmarks, it actually is worse. But

**[07:22]** benchmarks, it actually is worse. But

**[07:22]** benchmarks, it actually is worse. But then you use it and you're like, "Oh,

**[07:23]** then you use it and you're like, "Oh,

**[07:23]** then you use it and you're like, "Oh, something's better here." So, I like

**[07:24]** something's better here." So, I like

**[07:24]** something's better here." So, I like this because it captures what people

**[07:26]** this because it captures what people

**[07:26]** this because it captures what people actually say to me. But I also like it

**[07:28]** actually say to me. But I also like it

**[07:28]** actually say to me. But I also like it because once you get here, the

**[07:29]** because once you get here, the

**[07:29]** because once you get here, the performance is horrible. So, like they

**[07:31]** performance is horrible. So, like they

**[07:31]** performance is horrible. So, like they if they enter a bunch of relevant stuff

**[07:34]** if they enter a bunch of relevant stuff

**[07:34]** if they enter a bunch of relevant stuff that doesn't actually help you solve the

**[07:36]** that doesn't actually help you solve the

**[07:36]** that doesn't actually help you solve the problem, once you get to 10 the 4

**[07:38]** problem, once you get to 10 the 4

**[07:38]** problem, once you get to 10 the 4 tokens, which is 10,000, like the models

**[07:40]** tokens, which is 10,000, like the models

**[07:40]** tokens, which is 10,000, like the models don't work at all. And even though

**[07:42]** don't work at all. And even though

**[07:42]** don't work at all. And even though they're not breaking like they're

**[07:43]** they're not breaking like they're

**[07:43]** they're not breaking like they're outputting

**[07:45]** outputting

**[07:45]** outputting things that make sense and are

**[07:47]** things that make sense and are

**[07:47]** things that make sense and are grammatical, they're not actually

**[07:49]** grammatical, they're not actually

**[07:49]** grammatical, they're not actually solving the problem. So context broad is

**[07:51]** solving the problem. So context broad is

**[07:51]** solving the problem. So context broad is a huge issue. Um

**[07:53]** a huge issue. Um

**[07:53]** a huge issue. Um maybe like just anecdotally if you look

**[07:56]** maybe like just anecdotally if you look

**[07:56]** maybe like just anecdotally if you look up there's a ton of people saying stuff

**[07:58]** up there's a ton of people saying stuff

**[07:58]** up there's a ton of people saying stuff like this like oh what the context

**[07:59]** like this like oh what the context

**[07:59]** like this like oh what the context window is so long why does it not


### [08:00 - 09:00]

**[08:01]** window is so long why does it not

**[08:01]** window is so long why does it not actually work? Or people think claude

**[08:02]** actually work? Or people think claude

**[08:02]** actually work? Or people think claude code when it fills up the context window

**[08:04]** code when it fills up the context window

**[08:04]** code when it fills up the context window sort of like stops working. Um there's a

**[08:07]** sort of like stops working. Um there's a

**[08:07]** sort of like stops working. Um there's a ton of people working on these efficient

**[08:08]** ton of people working on these efficient

**[08:08]** ton of people working on these efficient architectures that you might hear about

**[08:10]** architectures that you might hear about

**[08:10]** architectures that you might hear about like [music] uh mamba state space

**[08:12]** like [music] uh mamba state space

**[08:12]** like [music] uh mamba state space models, linear attention, uh hybrid

**[08:14]** models, linear attention, uh hybrid

**[08:14]** models, linear attention, uh hybrid attention, sparse attention, sliding

**[08:16]** attention, sparse attention, sliding

**[08:16]** attention, sparse attention, sliding window. They're all more efficient, but

**[08:19]** window. They're all more efficient, but

**[08:19]** window. They're all more efficient, but they basically have the same properties

**[08:20]** they basically have the same properties

**[08:20]** they basically have the same properties of transformers. Like even if they can

**[08:23]** of transformers. Like even if they can

**[08:23]** of transformers. Like even if they can operate uh in a faster time or with a

**[08:26]** operate uh in a faster time or with a

**[08:26]** operate uh in a faster time or with a lower memory requirement, there's some

**[08:28]** lower memory requirement, there's some

**[08:28]** lower memory requirement, there's some trade-off in the terms of performance

**[08:29]** trade-off in the terms of performance

**[08:29]** trade-off in the terms of performance they give you. So even if you build a

**[08:31]** they give you. So even if you build a

**[08:31]** they give you. So even if you build a linear attention model that can fit

**[08:33]** linear attention model that can fit

**[08:34]** linear attention model that can fit infinite context, it's not good. Like

**[08:36]** infinite context, it's not good. Like

**[08:36]** infinite context, it's not good. Like it's not going to be able to solve the

**[08:39]** it's not going to be able to solve the

**[08:39]** it's not going to be able to solve the problem you have, which is how do I

**[08:40]** problem you have, which is how do I

**[08:40]** problem you have, which is how do I actually like reason and get smarter

**[08:44]** actually like reason and get smarter

**[08:44]** actually like reason and get smarter when I input more tokens into the model.

**[08:47]** when I input more tokens into the model.

**[08:47]** when I input more tokens into the model. There's so many examples of this. I saw

**[08:50]** There's so many examples of this. I saw

**[08:50]** There's so many examples of this. I saw this recent post. If you're like kind of

**[08:52]** this recent post. If you're like kind of

**[08:52]** this recent post. If you're like kind of deep in the model architecture world,

**[08:54]** deep in the model architecture world,

**[08:54]** deep in the model architecture world, maybe you've seen this. This is like a

**[08:56]** maybe you've seen this. This is like a

**[08:56]** maybe you've seen this. This is like a couple weeks ago. There's new Chinese

**[08:57]** couple weeks ago. There's new Chinese

**[08:57]** couple weeks ago. There's new Chinese model Miniax M2. It's one of the

**[08:59]** model Miniax M2. It's one of the

**[08:59]** model Miniax M2. It's one of the state-of-the-art open models. And a


### [09:00 - 10:00]

**[09:02]** state-of-the-art open models. And a

**[09:02]** state-of-the-art open models. And a bunch of the other Chinese labs have

**[09:03]** bunch of the other Chinese labs have

**[09:03]** bunch of the other Chinese labs have been pushing these new hybrid

**[09:05]** been pushing these new hybrid

**[09:05]** been pushing these new hybrid architectures that are like more

**[09:06]** architectures that are like more

**[09:06]** architectures that are like more efficient and can take longer context.

**[09:09]** efficient and can take longer context.

**[09:09]** efficient and can take longer context. And Miniax M2 just didn't do that. They

**[09:10]** And Miniax M2 just didn't do that. They

**[09:10]** And Miniax M2 just didn't do that. They just use sort of like the regular

**[09:12]** just use sort of like the regular

**[09:12]** just use sort of like the regular quadratic attention that I was showing

**[09:13]** quadratic attention that I was showing

**[09:13]** quadratic attention that I was showing you. And they have this really long

**[09:15]** you. And they have this really long

**[09:15]** you. And they have this really long story about how they tried and tried and

**[09:18]** story about how they tried and tried and

**[09:18]** story about how they tried and tried and it's basically just not worth it.

**[09:19]** it's basically just not worth it.

**[09:19]** it's basically just not worth it. There's like an inherent trade-off and

**[09:21]** There's like an inherent trade-off and

**[09:21]** There's like an inherent trade-off and how much computation you use and and how

**[09:23]** how much computation you use and and how

**[09:23]** how much computation you use and and how good the models are. And so even if you

**[09:26]** good the models are. And so even if you

**[09:26]** good the models are. And so even if you can technically build a model that

**[09:27]** can technically build a model that

**[09:27]** can technically build a model that doesn't break at millions of tokens,

**[09:30]** doesn't break at millions of tokens,

**[09:30]** doesn't break at millions of tokens, it's not actually better for any of the

**[09:31]** it's not actually better for any of the

**[09:31]** it's not actually better for any of the tasks they care about. So no one is

**[09:34]** tasks they care about. So no one is

**[09:34]** tasks they care about. So no one is really doing this. And I think to

**[09:36]** really doing this. And I think to

**[09:36]** really doing this. And I think to conclude, we think that like we're

**[09:38]** conclude, we think that like we're

**[09:38]** conclude, we think that like we're pretty limited by the context window in

**[09:40]** pretty limited by the context window in

**[09:40]** pretty limited by the context window in full context. There's like one systems

**[09:42]** full context. There's like one systems

**[09:42]** full context. There's like one systems problem that you can't put millions of

**[09:44]** problem that you can't put millions of

**[09:44]** problem that you can't put millions of tokens into the model. And then there's

**[09:46]** tokens into the model. And then there's

**[09:46]** tokens into the model. And then there's another reasoning problem that even if

**[09:47]** another reasoning problem that even if

**[09:47]** another reasoning problem that even if you can, the models don't actually get

**[09:49]** you can, the models don't actually get

**[09:49]** you can, the models don't actually get better. So it's probably not practical.

**[09:52]** better. So it's probably not practical.

**[09:52]** better. So it's probably not practical. And I think if you work in industry, I'm

**[09:55]** And I think if you work in industry, I'm

**[09:55]** And I think if you work in industry, I'm sure you see document sets that are much

**[09:58]** sure you see document sets that are much

**[09:58]** sure you see document sets that are much much larger, like on the order of I


### [10:00 - 11:00]

**[10:00]** much larger, like on the order of I

**[10:00]** much larger, like on the order of I don't know, billions to trillions of

**[10:01]** don't know, billions to trillions of

**[10:02]** don't know, billions to trillions of tokens. And even though we're getting

**[10:04]** tokens. And even though we're getting

**[10:04]** tokens. And even though we're getting better at training the models and the

**[10:06]** better at training the models and the

**[10:06]** better at training the models and the system side, we're getting much better

**[10:07]** system side, we're getting much better

**[10:07]** system side, we're getting much better at running them more efficiently,

**[10:09]** at running them more efficiently,

**[10:09]** at running them more efficiently, faster, cheaper, we're not near fitting

**[10:13]** faster, cheaper, we're not near fitting

**[10:13]** faster, cheaper, we're not near fitting trillions of tokens into a model. I

**[10:15]** trillions of tokens into a model. I

**[10:15]** trillions of tokens into a model. I think like that's pretty far off. So I

**[10:17]** think like that's pretty far off. So I

**[10:17]** think like that's pretty far off. So I would guess a lot of you are doing rag.

**[10:19]** would guess a lot of you are doing rag.

**[10:19]** would guess a lot of you are doing rag. How many people in this room use or work

**[10:22]** How many people in this room use or work

**[10:22]** How many people in this room use or work on a rag system on like a weekly basis?

**[10:25]** on a rag system on like a weekly basis?

**[10:25]** on a rag system on like a weekly basis? That's actually pretty crazy. Okay, so

**[10:27]** That's actually pretty crazy. Okay, so

**[10:27]** That's actually pretty crazy. Okay, so over half for sure. So now we're going

**[10:30]** over half for sure. So now we're going

**[10:30]** over half for sure. So now we're going to talk about Rag. I'm going to talk

**[10:32]** to talk about Rag. I'm going to talk

**[10:32]** to talk about Rag. I'm going to talk about why it's good and then I'll talk

**[10:33]** about why it's good and then I'll talk

**[10:33]** about why it's good and then I'll talk about why I think um it's fundamentally

**[10:36]** about why I think um it's fundamentally

**[10:36]** about why I think um it's fundamentally limited and the products of the future

**[10:40]** limited and the products of the future

**[10:40]** limited and the products of the future will use something better than Rack.

**[10:44]** will use something better than Rack.

**[10:44]** will use something better than Rack. So if you use Rag, you probably use a

**[10:46]** So if you use Rag, you probably use a

**[10:46]** So if you use Rag, you probably use a vector database. There are many vector

**[10:47]** vector database. There are many vector

**[10:47]** vector database. There are many vector databases. I think I know some of these.

**[10:51]** databases. I think I know some of these.

**[10:51]** databases. I think I know some of these. Turboroper, we now they're on S3, that's

**[10:55]** Turboroper, we now they're on S3, that's

**[10:55]** Turboroper, we now they're on S3, that's Chroma. I made this slide. Uh,

**[10:59]** Chroma. I made this slide. Uh,

**[10:59]** Chroma. I made this slide. Uh, Uh, there there are many vector


### [11:00 - 12:00]

**[11:01]** Uh, there there are many vector

**[11:01]** Uh, there there are many vector databases. They all offer you like

**[11:02]** databases. They all offer you like

**[11:02]** databases. They all offer you like slightly different trade-offs. They give

**[11:04]** slightly different trade-offs. They give

**[11:04]** slightly different trade-offs. They give you your vectors for cheaper, faster.

**[11:07]** you your vectors for cheaper, faster.

**[11:07]** you your vectors for cheaper, faster. Um, vector databases are the way that

**[11:09]** Um, vector databases are the way that

**[11:09]** Um, vector databases are the way that memory works in production. If you're

**[11:11]** memory works in production. If you're

**[11:11]** memory works in production. If you're using a company internal question

**[11:13]** using a company internal question

**[11:13]** using a company internal question answering system, it's it's definitely

**[11:15]** answering system, it's it's definitely

**[11:15]** answering system, it's it's definitely running on rag which is powered by a

**[11:17]** running on rag which is powered by a

**[11:17]** running on rag which is powered by a vector database which stores embeddings.

**[11:20]** vector database which stores embeddings.

**[11:20]** vector database which stores embeddings. JBT memory uh uses embeddings. Uh Andre

**[11:25]** JBT memory uh uses embeddings. Uh Andre

**[11:25]** JBT memory uh uses embeddings. Uh Andre Karpathy has this diagram from last year

**[11:28]** Karpathy has this diagram from last year

**[11:28]** Karpathy has this diagram from last year two years ago actually of what the an

**[11:31]** two years ago actually of what the an

**[11:31]** two years ago actually of what the an operating system that runs on language

**[11:32]** operating system that runs on language

**[11:32]** operating system that runs on language models would look like and he called

**[11:34]** models would look like and he called

**[11:34]** models would look like and he called embeddings the file system of LLMs. Um,

**[11:38]** embeddings the file system of LLMs. Um,

**[11:38]** embeddings the file system of LLMs. Um, I think that's true in today's terms.

**[11:39]** I think that's true in today's terms.

**[11:39]** I think that's true in today's terms. Like today, November 22nd, 2025,

**[11:43]** Like today, November 22nd, 2025,

**[11:43]** Like today, November 22nd, 2025, probably like if you think of what

**[11:45]** probably like if you think of what

**[11:45]** probably like if you think of what you're working on as an operating

**[11:46]** you're working on as an operating

**[11:46]** you're working on as an operating system, the file system is embeddings.

**[11:48]** system, the file system is embeddings.

**[11:48]** system, the file system is embeddings. But I think embeddings are the file

**[11:50]** But I think embeddings are the file

**[11:50]** But I think embeddings are the file system of today. And they're not the

**[11:51]** system of today. And they're not the

**[11:51]** system of today. And they're not the file system of the future. And that's

**[11:53]** file system of the future. And that's

**[11:53]** file system of the future. And that's what I'm going to talk about today.

**[11:56]** what I'm going to talk about today.

**[11:56]** what I'm going to talk about today. I I also want to point out that they're

**[11:58]** I I also want to point out that they're

**[11:58]** I I also want to point out that they're extremely easy to use. Like any of the


### [12:00 - 13:00]

**[12:00]** extremely easy to use. Like any of the

**[12:00]** extremely easy to use. Like any of the tools I'm going to talk about at the end

**[12:01]** tools I'm going to talk about at the end

**[12:01]** tools I'm going to talk about at the end of the talk that are like related to

**[12:03]** of the talk that are like related to

**[12:03]** of the talk that are like related to training things into models are just

**[12:05]** training things into models are just

**[12:05]** training things into models are just fundamentally harder. But this is just

**[12:07]** fundamentally harder. But this is just

**[12:07]** fundamentally harder. But this is just really nice and we can all take a moment

**[12:09]** really nice and we can all take a moment

**[12:09]** really nice and we can all take a moment to appreciate it. You just sort of bake

**[12:11]** to appreciate it. You just sort of bake

**[12:11]** to appreciate it. You just sort of bake your text and then you like run this and

**[12:14]** your text and then you like run this and

**[12:14]** your text and then you like run this and and that's all. It's a five lines of

**[12:16]** and that's all. It's a five lines of

**[12:16]** and that's all. It's a five lines of code. That's a that's really really

**[12:18]** code. That's a that's really really

**[12:18]** code. That's a that's really really good. Um the problem is they just aren't

**[12:21]** good. Um the problem is they just aren't

**[12:21]** good. Um the problem is they just aren't that good and they have a lot of

**[12:24]** that good and they have a lot of

**[12:24]** that good and they have a lot of problems I think. Um, which I think

**[12:25]** problems I think. Um, which I think

**[12:26]** problems I think. Um, which I think also, okay, how many people work on rag

**[12:28]** also, okay, how many people work on rag

**[12:28]** also, okay, how many people work on rag or experience

**[12:30]** or experience

**[12:30]** or experience a rag system and are satisfied

**[12:33]** a rag system and are satisfied

**[12:33]** a rag system and are satisfied completely with [laughter] like

**[12:39]** Okay, that's great. So, I think we're

**[12:39]** Okay, that's great. So, I think we're all kind of in agreement here that maybe

**[12:40]** all kind of in agreement here that maybe

**[12:40]** all kind of in agreement here that maybe there there could be something more like

**[12:43]** there there could be something more like

**[12:43]** there there could be something more like even if we don't know exactly what it

**[12:44]** even if we don't know exactly what it

**[12:44]** even if we don't know exactly what it is, there must be something else out

**[12:45]** is, there must be something else out

**[12:46]** is, there must be something else out there. Um, I'll talk about a few

**[12:48]** there. Um, I'll talk about a few

**[12:48]** there. Um, I'll talk about a few problems that I've run into in my own

**[12:49]** problems that I've run into in my own

**[12:49]** problems that I've run into in my own research. So, let's like start with this

**[12:52]** research. So, let's like start with this

**[12:52]** research. So, let's like start with this abstraction. So this is the vector

**[12:53]** abstraction. So this is the vector

**[12:53]** abstraction. So this is the vector database that powers rag. Every dot here

**[12:57]** database that powers rag. Every dot here

**[12:57]** database that powers rag. Every dot here is is supposed to be a document. So the

**[12:59]** is is supposed to be a document. So the

**[12:59]** is is supposed to be a document. So the document goes through the LLM. The LLM


### [13:00 - 14:00]

**[13:02]** document goes through the LLM. The LLM

**[13:02]** document goes through the LLM. The LLM is trained to give you just this one

**[13:04]** is trained to give you just this one

**[13:04]** is trained to give you just this one vector that represents the document. I

**[13:06]** vector that represents the document. I

**[13:06]** vector that represents the document. I projected them down to two dimensions

**[13:07]** projected them down to two dimensions

**[13:07]** projected them down to two dimensions for the slide, but each doc document is

**[13:10]** for the slide, but each doc document is

**[13:10]** for the slide, but each doc document is one dot. Um if you actually look at

**[13:13]** one dot. Um if you actually look at

**[13:13]** one dot. Um if you actually look at what's in the vector database, it looks

**[13:14]** what's in the vector database, it looks

**[13:14]** what's in the vector database, it looks like this. So there lots of numbers.

**[13:19]** like this. So there lots of numbers.

**[13:19]** like this. So there lots of numbers. there's no one on the in the world who

**[13:21]** there's no one on the in the world who

**[13:21]** there's no one on the in the world who can tell tell you what this means. Um,

**[13:24]** can tell tell you what this means. Um,

**[13:24]** can tell tell you what this means. Um, one thing that I think is interesting is

**[13:27]** one thing that I think is interesting is

**[13:27]** one thing that I think is interesting is that even though they look random and no

**[13:29]** that even though they look random and no

**[13:29]** that even though they look random and no one can actually read them, if you build

**[13:31]** one can actually read them, if you build

**[13:31]** one can actually read them, if you build a system to read them, it works pretty

**[13:33]** a system to read them, it works pretty

**[13:33]** a system to read them, it works pretty well. So like if you're working at Rag

**[13:36]** well. So like if you're working at Rag

**[13:36]** well. So like if you're working at Rag and you're sending someone embeddings,

**[13:37]** and you're sending someone embeddings,

**[13:37]** and you're sending someone embeddings, you're actually sending them something

**[13:39]** you're actually sending them something

**[13:39]** you're actually sending them something analogous to text. And I think this is

**[13:42]** analogous to text. And I think this is

**[13:42]** analogous to text. And I think this is important because a lot of the actual

**[13:44]** important because a lot of the actual

**[13:44]** important because a lot of the actual architectures like Turbopuffer, Pine

**[13:46]** architectures like Turbopuffer, Pine

**[13:46]** architectures like Turbopuffer, Pine Cone, what have you, they store only

**[13:49]** Cone, what have you, they store only

**[13:49]** Cone, what have you, they store only embeddings. And so like maybe there's

**[13:50]** embeddings. And so like maybe there's

**[13:50]** embeddings. And so like maybe there's this false premise that if you just send

**[13:52]** this false premise that if you just send

**[13:52]** this false premise that if you just send them embeddings, there's no security

**[13:54]** them embeddings, there's no security

**[13:54]** them embeddings, there's no security flaws. But actually a even slightly

**[13:57]** flaws. But actually a even slightly

**[13:57]** flaws. But actually a even slightly motivated person can build this system

**[13:59]** motivated person can build this system

**[13:59]** motivated person can build this system here, this white arrow on the right,


### [14:00 - 15:00]

**[14:01]** here, this white arrow on the right,

**[14:01]** here, this white arrow on the right, which takes the embedding and produces

**[14:03]** which takes the embedding and produces

**[14:03]** which takes the embedding and produces maybe not the exact same text, but

**[14:05]** maybe not the exact same text, but

**[14:05]** maybe not the exact same text, but something extremely close to it. This is

**[14:07]** something extremely close to it. This is

**[14:07]** something extremely close to it. This is what I worked on for like about a year

**[14:09]** what I worked on for like about a year

**[14:09]** what I worked on for like about a year of my PhD. This is a animation of like

**[14:13]** of my PhD. This is a animation of like

**[14:13]** of my PhD. This is a animation of like so I type in this sentence it goes into

**[14:15]** so I type in this sentence it goes into

**[14:15]** so I type in this sentence it goes into the embedding model it gets stored in

**[14:17]** the embedding model it gets stored in

**[14:17]** the embedding model it gets stored in vector database and then we run this

**[14:19]** vector database and then we run this

**[14:19]** vector database and then we run this it's like a multi- round correction

**[14:20]** it's like a multi- round correction

**[14:20]** it's like a multi- round correction thing and then by the end we actually

**[14:22]** thing and then by the end we actually

**[14:22]** thing and then by the end we actually can get most I think our research has at

**[14:25]** can get most I think our research has at

**[14:25]** can get most I think our research has at a certain length we can get 90% of text

**[14:27]** a certain length we can get 90% of text

**[14:27]** a certain length we can get 90% of text back exactly from vector databases. So

**[14:29]** back exactly from vector databases. So

**[14:29]** back exactly from vector databases. So the takeaway here is that there's no uh

**[14:32]** the takeaway here is that there's no uh

**[14:32]** the takeaway here is that there's no uh security benefits to using a vector

**[14:34]** security benefits to using a vector

**[14:34]** security benefits to using a vector database and also they're very hard to

**[14:36]** database and also they're very hard to

**[14:36]** database and also they're very hard to run at scale. So this is like an

**[14:38]** run at scale. So this is like an

**[14:38]** run at scale. So this is like an inherent problem for people with

**[14:39]** inherent problem for people with

**[14:39]** inherent problem for people with sensitive data. That's the paper. Um

**[14:43]** sensitive data. That's the paper. Um

**[14:43]** sensitive data. That's the paper. Um I think a second problem that I

**[14:45]** I think a second problem that I

**[14:45]** I think a second problem that I personally have with embeddings is that

**[14:46]** personally have with embeddings is that

**[14:46]** personally have with embeddings is that they're not adaptive. Like there's this

**[14:49]** they're not adaptive. Like there's this

**[14:49]** they're not adaptive. Like there's this one universal sense of what the world

**[14:51]** one universal sense of what the world

**[14:51]** one universal sense of what the world looks like that's captured in these

**[14:52]** looks like that's captured in these

**[14:52]** looks like that's captured in these vectors and it's not adjustable based on

**[14:55]** vectors and it's not adjustable based on

**[14:55]** vectors and it's not adjustable based on what you work on. So like to give you a

**[14:58]** what you work on. So like to give you a

**[14:58]** what you work on. So like to give you a concrete example,


### [15:00 - 16:00]

**[15:00]** concrete example,

**[15:00]** concrete example, we embedded a bunch of databases or we

**[15:03]** we embedded a bunch of databases or we

**[15:03]** we embedded a bunch of databases or we created a database of a bunch of

**[15:04]** created a database of a bunch of

**[15:04]** created a database of a bunch of embeddings of credit card related

**[15:07]** embeddings of credit card related

**[15:07]** embeddings of credit card related documents. I think we had half of them

**[15:09]** documents. I think we had half of them

**[15:09]** documents. I think we had half of them that were from Mastercard and half of

**[15:11]** that were from Mastercard and half of

**[15:11]** that were from Mastercard and half of them that were from Visa. But if you

**[15:13]** them that were from Visa. But if you

**[15:13]** them that were from Visa. But if you actually look at where the embeddings

**[15:15]** actually look at where the embeddings

**[15:15]** actually look at where the embeddings get stored, um I guess it's not in this

**[15:17]** get stored, um I guess it's not in this

**[15:17]** get stored, um I guess it's not in this picture, but it's like only right here.

**[15:19]** picture, but it's like only right here.

**[15:19]** picture, but it's like only right here. So even then there's this like really

**[15:21]** So even then there's this like really

**[15:21]** So even then there's this like really large space of kind of all possible

**[15:23]** large space of kind of all possible

**[15:23]** large space of kind of all possible semantics embeddings only represent like

**[15:26]** semantics embeddings only represent like

**[15:26]** semantics embeddings only represent like one universal one if that makes sense.

**[15:28]** one universal one if that makes sense.

**[15:28]** one universal one if that makes sense. So credit cards are actually clustered

**[15:30]** So credit cards are actually clustered

**[15:30]** So credit cards are actually clustered in this like really small area and this

**[15:32]** in this like really small area and this

**[15:32]** in this like really small area and this means search works bad. So like to give

**[15:37]** means search works bad. So like to give

**[15:37]** means search works bad. So like to give you a concrete example, if you take

**[15:38]** you a concrete example, if you take

**[15:38]** you a concrete example, if you take these two documents, one's from Visa,

**[15:40]** these two documents, one's from Visa,

**[15:40]** these two documents, one's from Visa, one's from Mastercard, at least in the

**[15:42]** one's from Mastercard, at least in the

**[15:42]** one's from Mastercard, at least in the system we were designing, like if you

**[15:44]** system we were designing, like if you

**[15:44]** system we were designing, like if you search something that's about a Visa

**[15:45]** search something that's about a Visa

**[15:45]** search something that's about a Visa query, you should never receive

**[15:47]** query, you should never receive

**[15:47]** query, you should never receive Mastercard, but they're all so close to

**[15:49]** Mastercard, but they're all so close to

**[15:49]** Mastercard, but they're all so close to each other that they're actually like

**[15:50]** each other that they're actually like

**[15:50]** each other that they're actually like completely all jumbled together. And

**[15:52]** completely all jumbled together. And

**[15:52]** completely all jumbled together. And this is just like a problem with all

**[15:54]** this is just like a problem with all

**[15:54]** this is just like a problem with all conventional embedding mechanisms. So we

**[15:56]** conventional embedding mechanisms. So we

**[15:56]** conventional embedding mechanisms. So we built this new model that lets you feed

**[15:59]** built this new model that lets you feed

**[15:59]** built this new model that lets you feed in some like surrounding documents. So


### [16:00 - 17:00]

**[16:01]** in some like surrounding documents. So

**[16:01]** in some like surrounding documents. So like to give you an example, this is

**[16:03]** like to give you an example, this is

**[16:03]** like to give you an example, this is kind of the first half of our model. We

**[16:05]** kind of the first half of our model. We

**[16:05]** kind of the first half of our model. We would feed in a bunch of credit cards. I

**[16:07]** would feed in a bunch of credit cards. I

**[16:07]** would feed in a bunch of credit cards. I guess I put AMX, but there actually was

**[16:09]** guess I put AMX, but there actually was

**[16:09]** guess I put AMX, but there actually was no AMX when we did it. And um and the

**[16:13]** no AMX when we did it. And um and the

**[16:13]** no AMX when we did it. And um and the model kind of works like this. Like when

**[16:14]** model kind of works like this. Like when

**[16:14]** model kind of works like this. Like when it produces the embedding for the text,

**[16:16]** it produces the embedding for the text,

**[16:16]** it produces the embedding for the text, which is here, it also looks at a bunch

**[16:18]** which is here, it also looks at a bunch

**[16:18]** which is here, it also looks at a bunch of surrounding documents. So it can kind

**[16:20]** of surrounding documents. So it can kind

**[16:20]** of surrounding documents. So it can kind of know like okay, this text is about

**[16:22]** of know like okay, this text is about

**[16:22]** of know like okay, this text is about Visa, but also all the other documents

**[16:24]** Visa, but also all the other documents

**[16:24]** Visa, but also all the other documents are about either Visa or Mastercard. and

**[16:26]** are about either Visa or Mastercard. and

**[16:26]** are about either Visa or Mastercard. and it gets trained so that it can like

**[16:28]** it gets trained so that it can like

**[16:28]** it gets trained so that it can like dynamically adjust the embeddings based

**[16:30]** dynamically adjust the embeddings based

**[16:30]** dynamically adjust the embeddings based on like the surrounding context. So I

**[16:33]** on like the surrounding context. So I

**[16:33]** on like the surrounding context. So I thought this was cool and it works

**[16:35]** thought this was cool and it works

**[16:35]** thought this was cool and it works better. So like in this Visa Mastercard

**[16:37]** better. So like in this Visa Mastercard

**[16:37]** better. So like in this Visa Mastercard case the similarity between a Visa and

**[16:40]** case the similarity between a Visa and

**[16:40]** case the similarity between a Visa and Mastercard is now.144 and I think

**[16:42]** Mastercard is now.144 and I think

**[16:42]** Mastercard is now.144 and I think anything containing Visa has a much

**[16:44]** anything containing Visa has a much

**[16:44]** anything containing Visa has a much higher similarity. So that's like maybe

**[16:46]** higher similarity. So that's like maybe

**[16:46]** higher similarity. So that's like maybe correcting one small thing. Um it works

**[16:50]** correcting one small thing. Um it works

**[16:50]** correcting one small thing. Um it works better on like out of domain stuff. So

**[16:51]** better on like out of domain stuff. So

**[16:51]** better on like out of domain stuff. So we have a forgot what the climate data

**[16:54]** we have a forgot what the climate data

**[16:54]** we have a forgot what the climate data set is. is a data set of arguments, a

**[16:56]** set is. is a data set of arguments, a

**[16:56]** set is. is a data set of arguments, a data set of financial questions, and

**[16:59]** data set of financial questions, and

**[16:59]** data set of financial questions, and then I think like scientific articles.


### [17:00 - 18:00]

**[17:02]** then I think like scientific articles.

**[17:02]** then I think like scientific articles. And I guess the point I'm making here is

**[17:04]** And I guess the point I'm making here is

**[17:04]** And I guess the point I'm making here is that if you do this contextual thing,

**[17:05]** that if you do this contextual thing,

**[17:05]** that if you do this contextual thing, embeddings work a bit better. So like if

**[17:07]** embeddings work a bit better. So like if

**[17:07]** embeddings work a bit better. So like if you build them in a way that they can

**[17:09]** you build them in a way that they can

**[17:09]** you build them in a way that they can dynamically adapt to the domain, they

**[17:11]** dynamically adapt to the domain, they

**[17:11]** dynamically adapt to the domain, they can solve some problems, but I think at

**[17:13]** can solve some problems, but I think at

**[17:14]** can solve some problems, but I think at the end of the day, they're still

**[17:15]** the end of the day, they're still

**[17:15]** the end of the day, they're still embeddings. And so

**[17:18]** embeddings. And so

**[17:18]** embeddings. And so >> yeah. Yeah.

**[17:19]** >> yeah. Yeah.

**[17:19]** >> yeah. Yeah. >> Uh was this approach picked up by anyone

**[17:22]** >> Uh was this approach picked up by anyone

**[17:22]** >> Uh was this approach picked up by anyone else? Do you know? Yeah, I think we know

**[17:25]** else? Do you know? Yeah, I think we know

**[17:25]** else? Do you know? Yeah, I think we know they're using it at OpenAI Anthropic

**[17:27]** they're using it at OpenAI Anthropic

**[17:27]** they're using it at OpenAI Anthropic like behind the scenes now the embedding

**[17:29]** like behind the scenes now the embedding

**[17:29]** like behind the scenes now the embedding models are contextual. It's a pretty

**[17:31]** models are contextual. It's a pretty

**[17:31]** models are contextual. It's a pretty it's kind of a free lunch like you add

**[17:33]** it's kind of a free lunch like you add

**[17:33]** it's kind of a free lunch like you add these extra tokens. Uh I guess it's it's

**[17:37]** these extra tokens. Uh I guess it's it's

**[17:37]** these extra tokens. Uh I guess it's it's kind of hard to build like you have to

**[17:39]** kind of hard to build like you have to

**[17:39]** kind of hard to build like you have to build this two-stage model and then uh

**[17:41]** build this two-stage model and then uh

**[17:41]** build this two-stage model and then uh when you embed something you have to

**[17:42]** when you embed something you have to

**[17:42]** when you embed something you have to grab some embeddings from the

**[17:44]** grab some embeddings from the

**[17:44]** grab some embeddings from the surrounding documents. But once you

**[17:45]** surrounding documents. But once you

**[17:46]** surrounding documents. But once you build it, it just works you know better

**[17:48]** build it, it just works you know better

**[17:48]** build it, it just works you know better on like especially on longtail stuff. I

**[17:50]** on like especially on longtail stuff. I

**[17:50]** on like especially on longtail stuff. I think if you look at um like MS Marco,

**[17:53]** think if you look at um like MS Marco,

**[17:53]** think if you look at um like MS Marco, which is this large webcale

**[17:55]** which is this large webcale

**[17:55]** which is this large webcale embedding task, it it really doesn't get

**[17:58]** embedding task, it it really doesn't get

**[17:58]** embedding task, it it really doesn't get much better when you add surrounding

**[17:59]** much better when you add surrounding

**[17:59]** much better when you add surrounding stuff because like it's already pretty


### [18:00 - 19:00]

**[18:02]** stuff because like it's already pretty

**[18:02]** stuff because like it's already pretty global if that makes sense. But if you

**[18:03]** global if that makes sense. But if you

**[18:03]** global if that makes sense. But if you look at like really niche things, the

**[18:06]** look at like really niche things, the

**[18:06]** look at like really niche things, the embeddings work a lot better. So yeah, I

**[18:07]** embeddings work a lot better. So yeah, I

**[18:07]** embeddings work a lot better. So yeah, I I know it's productionized at some other

**[18:09]** I know it's productionized at some other

**[18:10]** I know it's productionized at some other companies. Um I think if you're actually

**[18:11]** companies. Um I think if you're actually

**[18:11]** companies. Um I think if you're actually building an embedding model at your

**[18:13]** building an embedding model at your

**[18:13]** building an embedding model at your company and you want to put effort into

**[18:15]** company and you want to put effort into

**[18:15]** company and you want to put effort into making it better, this is probably like

**[18:17]** making it better, this is probably like

**[18:17]** making it better, this is probably like the easiest way besides data. probably

**[18:19]** the easiest way besides data. probably

**[18:19]** the easiest way besides data. probably the first way is data. Um

**[18:22]** the first way is data. Um

**[18:22]** the first way is data. Um there's some recent work that I think is

**[18:24]** there's some recent work that I think is

**[18:24]** there's some recent work that I think is worth mentioning about like fundamental

**[18:26]** worth mentioning about like fundamental

**[18:26]** worth mentioning about like fundamental limitations of embeddings and vector

**[18:28]** limitations of embeddings and vector

**[18:28]** limitations of embeddings and vector databases and rag which says that like

**[18:30]** databases and rag which says that like

**[18:30]** databases and rag which says that like if you it's not even really worth

**[18:33]** if you it's not even really worth

**[18:33]** if you it's not even really worth explaining but there's like some uh

**[18:37]** explaining but there's like some uh

**[18:37]** explaining but there's like some uh there there's some relationships that

**[18:39]** there there's some relationships that

**[18:39]** there there's some relationships that cannot be captured in a fixed

**[18:40]** cannot be captured in a fixed

**[18:40]** cannot be captured in a fixed dimensional vector like you have to

**[18:42]** dimensional vector like you have to

**[18:42]** dimensional vector like you have to reason about things to answer all

**[18:43]** reason about things to answer all

**[18:44]** reason about things to answer all possible tasks. And this is this kind of

**[18:45]** possible tasks. And this is this kind of

**[18:45]** possible tasks. And this is this kind of combinatorial setup where there are so

**[18:47]** combinatorial setup where there are so

**[18:47]** combinatorial setup where there are so many possible relationships that the

**[18:49]** many possible relationships that the

**[18:49]** many possible relationships that the embeddings simply can't store them. And

**[18:51]** embeddings simply can't store them. And

**[18:52]** embeddings simply can't store them. And so like in theory embeddings are

**[18:54]** so like in theory embeddings are

**[18:54]** so like in theory embeddings are obviously

**[18:56]** obviously

**[18:56]** obviously not the best way to do all possible

**[18:58]** not the best way to do all possible

**[18:58]** not the best way to do all possible relationships between text, but I think


### [19:00 - 20:00]

**[19:01]** relationships between text, but I think

**[19:01]** relationships between text, but I think everyone knows that rag has issues. Like

**[19:03]** everyone knows that rag has issues. Like

**[19:03]** everyone knows that rag has issues. Like I'm glad that no one raised their hand

**[19:05]** I'm glad that no one raised their hand

**[19:05]** I'm glad that no one raised their hand when I asked if anyone was going to like

**[19:07]** when I asked if anyone was going to like

**[19:07]** when I asked if anyone was going to like really stand up and speak for rag. And

**[19:10]** really stand up and speak for rag. And

**[19:10]** really stand up and speak for rag. And like we can I I actually think this is a

**[19:12]** like we can I I actually think this is a

**[19:12]** like we can I I actually think this is a hard point to make. Like everyone kind

**[19:13]** hard point to make. Like everyone kind

**[19:14]** hard point to make. Like everyone kind of knows this, but it's hard to come up

**[19:15]** of knows this, but it's hard to come up

**[19:16]** of knows this, but it's hard to come up with examples that retrieval can't solve

**[19:18]** with examples that retrieval can't solve

**[19:18]** with examples that retrieval can't solve in practice. Like speaking as someone

**[19:20]** in practice. Like speaking as someone

**[19:20]** in practice. Like speaking as someone who's recently sat down and tried to

**[19:22]** who's recently sat down and tried to

**[19:22]** who's recently sat down and tried to make benchmarks for tasks that I care

**[19:24]** make benchmarks for tasks that I care

**[19:24]** make benchmarks for tasks that I care about, it's hard to express questions

**[19:27]** about, it's hard to express questions

**[19:27]** about, it's hard to express questions that require kind of this like latent

**[19:29]** that require kind of this like latent

**[19:29]** that require kind of this like latent reasoning over multiple documents in a

**[19:31]** reasoning over multiple documents in a

**[19:31]** reasoning over multiple documents in a way that rag doesn't solve, but they do

**[19:34]** way that rag doesn't solve, but they do

**[19:34]** way that rag doesn't solve, but they do appear like um anything that kind of

**[19:37]** appear like um anything that kind of

**[19:37]** appear like um anything that kind of requires association between multiple

**[19:39]** requires association between multiple

**[19:39]** requires association between multiple things or questions that are they're

**[19:41]** things or questions that are they're

**[19:41]** things or questions that are they're like sort of implied but not explicitly

**[19:43]** like sort of implied but not explicitly

**[19:43]** like sort of implied but not explicitly answered by the documents are just not

**[19:46]** answered by the documents are just not

**[19:46]** answered by the documents are just not solvable by current techniques. And also

**[19:48]** solvable by current techniques. And also

**[19:48]** solvable by current techniques. And also if you have interesting examples of this

**[19:50]** if you have interesting examples of this

**[19:50]** if you have interesting examples of this would love to hear after this after the

**[19:52]** would love to hear after this after the

**[19:52]** would love to hear after this after the presentation. Um

**[19:55]** presentation. Um

**[19:55]** presentation. Um hopefully I made my case that I think

**[19:57]** hopefully I made my case that I think

**[19:58]** hopefully I made my case that I think rag Oh yeah yeah yeah go ahead.


### [20:00 - 21:00]

**[20:00]** rag Oh yeah yeah yeah go ahead.

**[20:00]** rag Oh yeah yeah yeah go ahead. >> I'm curious if you would classify

**[20:02]** >> I'm curious if you would classify

**[20:02]** >> I'm curious if you would classify agentic search as rag as well.

**[20:04]** agentic search as rag as well.

**[20:04]** agentic search as rag as well. >> Yeah that's a good question. So I guess

**[20:06]** >> Yeah that's a good question. So I guess

**[20:06]** >> Yeah that's a good question. So I guess the way I think agentic search it's like

**[20:09]** the way I think agentic search it's like

**[20:09]** the way I think agentic search it's like a model that can grab and it makes a

**[20:11]** a model that can grab and it makes a

**[20:11]** a model that can grab and it makes a bunch of queries in a row and then it

**[20:13]** bunch of queries in a row and then it

**[20:13]** bunch of queries in a row and then it responds. Um

**[20:15]** responds. Um

**[20:16]** responds. Um yeah that's that's a really good

**[20:17]** yeah that's that's a really good

**[20:17]** yeah that's that's a really good question. I think

**[20:19]** question. I think

**[20:20]** question. I think I think I wouldn't classify it as rag,

**[20:22]** I think I wouldn't classify it as rag,

**[20:22]** I think I wouldn't classify it as rag, but I think it has different fundamental

**[20:25]** but I think it has different fundamental

**[20:25]** but I think it has different fundamental limitations that are also tough to

**[20:27]** limitations that are also tough to

**[20:27]** limitations that are also tough to overcome. Like what you what you would

**[20:29]** overcome. Like what you what you would

**[20:29]** overcome. Like what you what you would really want is like a model that reads

**[20:31]** really want is like a model that reads

**[20:31]** really want is like a model that reads the entire thing and reasons about every

**[20:34]** the entire thing and reasons about every

**[20:34]** the entire thing and reasons about every possible relationship and then answers.

**[20:36]** possible relationship and then answers.

**[20:36]** possible relationship and then answers. And I think in theory maybe you could

**[20:38]** And I think in theory maybe you could

**[20:38]** And I think in theory maybe you could build an agentic rag system that does

**[20:40]** build an agentic rag system that does

**[20:40]** build an agentic rag system that does that, but it would be very expensive.

**[20:43]** that, but it would be very expensive.

**[20:43]** that, but it would be very expensive. >> Yeah. Because [clears throat] isn't that

**[20:44]** >> Yeah. Because [clears throat] isn't that

**[20:44]** >> Yeah. Because [clears throat] isn't that isn't that in the isn't deep research in

**[20:47]** isn't that in the isn't deep research in

**[20:48]** isn't that in the isn't deep research in the direction of that where it like goes

**[20:49]** the direction of that where it like goes

**[20:49]** the direction of that where it like goes through and it pulls like hundreds or

**[20:50]** through and it pulls like hundreds or

**[20:50]** through and it pulls like hundreds or thousands of sources but then what ends

**[20:52]** thousands of sources but then what ends

**[20:52]** thousands of sources but then what ends up in context is only like a small

**[20:54]** up in context is only like a small

**[20:54]** up in context is only like a small subset of those.

**[20:55]** subset of those.

**[20:55]** subset of those. >> Yeah. Yeah. I actually think deep

**[20:57]** >> Yeah. Yeah. I actually think deep

**[20:57]** >> Yeah. Yeah. I actually think deep research is like really in the right

**[20:58]** research is like really in the right

**[20:58]** research is like really in the right direction. Like they're trying to do


### [21:00 - 22:00]

**[21:01]** direction. Like they're trying to do

**[21:01]** direction. Like they're trying to do something that's a little bit higher

**[21:02]** something that's a little bit higher

**[21:02]** something that's a little bit higher level and requires a lot of compute.

**[21:05]** level and requires a lot of compute.

**[21:05]** level and requires a lot of compute. Like I think um anything that works

**[21:07]** Like I think um anything that works

**[21:07]** Like I think um anything that works better than rag is going to be more

**[21:09]** better than rag is going to be more

**[21:09]** better than rag is going to be more expensive. And so like just the property

**[21:12]** expensive. And so like just the property

**[21:12]** expensive. And so like just the property that it takes a while and it makes a lot

**[21:14]** that it takes a while and it makes a lot

**[21:14]** that it takes a while and it makes a lot of searches and it thinks a lot is like

**[21:16]** of searches and it thinks a lot is like

**[21:16]** of searches and it thinks a lot is like good. I think that there's probably a

**[21:20]** good. I think that there's probably a

**[21:20]** good. I think that there's probably a more elegant way to train like a really

**[21:23]** more elegant way to train like a really

**[21:23]** more elegant way to train like a really big kind of researchesque system, but I

**[21:26]** big kind of researchesque system, but I

**[21:26]** big kind of researchesque system, but I think that's that's actually a a good

**[21:28]** think that's that's actually a a good

**[21:28]** think that's that's actually a a good way of doing this and and not the one

**[21:30]** way of doing this and and not the one

**[21:30]** way of doing this and and not the one that I'm talking about today, but it's

**[21:31]** that I'm talking about today, but it's

**[21:32]** that I'm talking about today, but it's very promising as well. Like maybe the

**[21:34]** very promising as well. Like maybe the

**[21:34]** very promising as well. Like maybe the question is like are you willing to

**[21:36]** question is like are you willing to

**[21:36]** question is like are you willing to spend a lot of money at training time or

**[21:38]** spend a lot of money at training time or

**[21:38]** spend a lot of money at training time or at inference time and deep research is

**[21:40]** at inference time and deep research is

**[21:40]** at inference time and deep research is like kind of they don't spend a lot of

**[21:41]** like kind of they don't spend a lot of

**[21:41]** like kind of they don't spend a lot of money to train it but it's willing to

**[21:42]** money to train it but it's willing to

**[21:42]** money to train it but it's willing to wait for a long time at inference and I

**[21:44]** wait for a long time at inference and I

**[21:44]** wait for a long time at inference and I think the things I'm going to talk about

**[21:46]** think the things I'm going to talk about

**[21:46]** think the things I'm going to talk about today are more like if you're willing to

**[21:47]** today are more like if you're willing to

**[21:47]** today are more like if you're willing to spend a lot of money up front and you

**[21:49]** spend a lot of money up front and you

**[21:49]** spend a lot of money up front and you get a really smart model that knows all

**[21:51]** get a really smart model that knows all

**[21:51]** get a really smart model that knows all your data already um and it's really

**[21:54]** your data already um and it's really

**[21:54]** your data already um and it's really cheap to do inference. So it's like kind

**[21:56]** cheap to do inference. So it's like kind

**[21:56]** cheap to do inference. So it's like kind of different sides of the same

**[21:57]** of different sides of the same

**[21:57]** of different sides of the same trade-off. And I think like a good way

**[21:59]** trade-off. And I think like a good way

**[21:59]** trade-off. And I think like a good way of thinking about these things is like


### [22:00 - 23:00]

**[22:01]** of thinking about these things is like

**[22:01]** of thinking about these things is like to get better models, you're going to

**[22:02]** to get better models, you're going to

**[22:02]** to get better models, you're going to need to pay somewhere, you know, like

**[22:04]** need to pay somewhere, you know, like

**[22:04]** need to pay somewhere, you know, like you're either going to need to like

**[22:06]** you're either going to need to like

**[22:06]** you're either going to need to like generate better data and spend more time

**[22:07]** generate better data and spend more time

**[22:07]** generate better data and spend more time on the data, you're going to need to

**[22:09]** on the data, you're going to need to

**[22:09]** on the data, you're going to need to spend time on training, or you're going

**[22:10]** spend time on training, or you're going

**[22:10]** spend time on training, or you're going to need to spend time on inference. And

**[22:11]** to need to spend time on inference. And

**[22:12]** to need to spend time on inference. And a nice thing about rags is it kind of

**[22:13]** a nice thing about rags is it kind of

**[22:13]** a nice thing about rags is it kind of just works, but anything better will

**[22:15]** just works, but anything better will

**[22:15]** just works, but anything better will cost more.

**[22:15]** cost more.

**[22:16]** cost more. >> Yeah.

**[22:17]** >> Yeah.

**[22:17]** >> Yeah. >> Getting back to your example of

**[22:18]** >> Getting back to your example of

**[22:18]** >> Getting back to your example of Mastercard versus V. I I don't know if

**[22:21]** Mastercard versus V. I I don't know if

**[22:22]** Mastercard versus V. I I don't know if that's in your presentation later, but

**[22:23]** that's in your presentation later, but

**[22:23]** that's in your presentation later, but what are your thoughts on using

**[22:24]** what are your thoughts on using

**[22:24]** what are your thoughts on using knowledge graph for that as kind of

**[22:26]** knowledge graph for that as kind of

**[22:26]** knowledge graph for that as kind of augmenting

**[22:28]** augmenting

**[22:28]** augmenting It's a good question. Maybe ask me

**[22:30]** It's a good question. Maybe ask me

**[22:30]** It's a good question. Maybe ask me after. I have to think about knowledge

**[22:32]** after. I have to think about knowledge

**[22:32]** after. I have to think about knowledge graphs. It's been a while. Um, so let's

**[22:35]** graphs. It's been a while. Um, so let's

**[22:35]** graphs. It's been a while. Um, so let's talk about how to learn things in

**[22:36]** talk about how to learn things in

**[22:36]** talk about how to learn things in weights. Um, I think like the question

**[22:39]** weights. Um, I think like the question

**[22:39]** weights. Um, I think like the question that we want to get at is like, okay, so

**[22:42]** that we want to get at is like, okay, so

**[22:42]** that we want to get at is like, okay, so say we have the example I showed earlier

**[22:44]** say we have the example I showed earlier

**[22:44]** say we have the example I showed earlier or like you have a small data set you

**[22:46]** or like you have a small data set you

**[22:46]** or like you have a small data set you collected from your own personal work

**[22:48]** collected from your own personal work

**[22:48]** collected from your own personal work and you want to teach it to the model.

**[22:49]** and you want to teach it to the model.

**[22:49]** and you want to teach it to the model. It's one thing to put it into context

**[22:52]** It's one thing to put it into context

**[22:52]** It's one thing to put it into context and that's a good way to get started and

**[22:53]** and that's a good way to get started and

**[22:54]** and that's a good way to get started and if you don't have that much data,

**[22:55]** if you don't have that much data,

**[22:55]** if you don't have that much data, that'll get you pretty far. But I think

**[22:57]** that'll get you pretty far. But I think

**[22:57]** that'll get you pretty far. But I think we can do more. Like there's some

**[22:59]** we can do more. Like there's some

**[22:59]** we can do more. Like there's some questions that even when your data is in


### [23:00 - 24:00]

**[23:01]** questions that even when your data is in

**[23:01]** questions that even when your data is in context, the model can't answer. And so

**[23:03]** context, the model can't answer. And so

**[23:03]** context, the model can't answer. And so what I want us to think about is like

**[23:05]** what I want us to think about is like

**[23:05]** what I want us to think about is like how can we inject things into a model uh

**[23:08]** how can we inject things into a model uh

**[23:08]** how can we inject things into a model uh is such that it learns better than in

**[23:09]** is such that it learns better than in

**[23:09]** is such that it learns better than in context and also that it doesn't forget

**[23:11]** context and also that it doesn't forget

**[23:11]** context and also that it doesn't forget everything that it already knows. Um I

**[23:14]** everything that it already knows. Um I

**[23:14]** everything that it already knows. Um I want to point out something from my own

**[23:15]** want to point out something from my own

**[23:16]** want to point out something from my own research which is that there is a fixed

**[23:17]** research which is that there is a fixed

**[23:17]** research which is that there is a fixed capacity to language models. Like one

**[23:19]** capacity to language models. Like one

**[23:19]** capacity to language models. Like one way to think about this is tgt has like

**[23:22]** way to think about this is tgt has like

**[23:22]** way to think about this is tgt has like only so many parameters. we have this

**[23:24]** only so many parameters. we have this

**[23:24]** only so many parameters. we have this measurement that it can store 3.6 bits

**[23:27]** measurement that it can store 3.6 bits

**[23:27]** measurement that it can store 3.6 bits per parameter. So like uh I think a

**[23:30]** per parameter. So like uh I think a

**[23:30]** per parameter. So like uh I think a billion parameter model is like at 3.6

**[23:34]** billion parameter model is like at 3.6

**[23:34]** billion parameter model is like at 3.6 bits is maybe like four terabytes. Is

**[23:38]** bits is maybe like four terabytes. Is

**[23:38]** bits is maybe like four terabytes. Is that right? 4 gigabytes what? Yeah,

**[23:41]** that right? 4 gigabytes what? Yeah,

**[23:41]** that right? 4 gigabytes what? Yeah, thank you. Thank you. Um this is like

**[23:43]** thank you. Thank you. Um this is like

**[23:44]** thank you. Thank you. Um this is like some information but it's actually not

**[23:45]** some information but it's actually not

**[23:45]** some information but it's actually not that much. So the models they basically

**[23:47]** that much. So the models they basically

**[23:48]** that much. So the models they basically do their best to fit the training

**[23:50]** do their best to fit the training

**[23:50]** do their best to fit the training distribution and they throw everything

**[23:52]** distribution and they throw everything

**[23:52]** distribution and they throw everything else out. So like to give you a concrete

**[23:54]** else out. So like to give you a concrete

**[23:54]** else out. So like to give you a concrete example this morning I was putting this

**[23:56]** example this morning I was putting this

**[23:56]** example this morning I was putting this together. I asked Claude, "What is the

**[23:58]** together. I asked Claude, "What is the

**[23:58]** together. I asked Claude, "What is the capital of the smallest province in

**[23:59]** capital of the smallest province in

**[23:59]** capital of the smallest province in Tajjikstan?"


### [24:00 - 25:00]

**[24:01]** Tajjikstan?"

**[24:01]** Tajjikstan?" And it gave me a very detailed answer.

**[24:03]** And it gave me a very detailed answer.

**[24:03]** And it gave me a very detailed answer. It's actually very impressive. No web

**[24:05]** It's actually very impressive. No web

**[24:05]** It's actually very impressive. No web search. The model just knows this in its

**[24:07]** search. The model just knows this in its

**[24:07]** search. The model just knows this in its parameters. I guess I'm arguing that

**[24:09]** parameters. I guess I'm arguing that

**[24:09]** parameters. I guess I'm arguing that this is bad. Like if you want to build a

**[24:11]** this is bad. Like if you want to build a

**[24:11]** this is bad. Like if you want to build a system that can answer really detailed

**[24:14]** system that can answer really detailed

**[24:14]** system that can answer really detailed documentation questions for your

**[24:16]** documentation questions for your

**[24:16]** documentation questions for your company, you don't need it to know what

**[24:19]** company, you don't need it to know what

**[24:19]** company, you don't need it to know what the capital of the smallest province in

**[24:20]** the capital of the smallest province in

**[24:20]** the capital of the smallest province in Tajjikstan is. And since we know these

**[24:23]** Tajjikstan is. And since we know these

**[24:23]** Tajjikstan is. And since we know these models have fixed capacity, I think that

**[24:25]** models have fixed capacity, I think that

**[24:25]** models have fixed capacity, I think that this is bad. Like what we really want is

**[24:27]** this is bad. Like what we really want is

**[24:27]** this is bad. Like what we really want is to know how to like find this kind of

**[24:29]** to know how to like find this kind of

**[24:29]** to know how to like find this kind of thing and just like delete it and

**[24:30]** thing and just like delete it and

**[24:30]** thing and just like delete it and replace it with the things we care

**[24:31]** replace it with the things we care

**[24:32]** replace it with the things we care about. And I think that's like what

**[24:33]** about. And I think that's like what

**[24:33]** about. And I think that's like what we're getting towards, but we don't 100%

**[24:34]** we're getting towards, but we don't 100%

**[24:34]** we're getting towards, but we don't 100% know how to do that again. Sorry. So

**[24:37]** know how to do that again. Sorry. So

**[24:37]** know how to do that again. Sorry. So when I originally put this talk

**[24:38]** when I originally put this talk

**[24:38]** when I originally put this talk together, the way I was thinking of

**[24:39]** together, the way I was thinking of

**[24:39]** together, the way I was thinking of explaining it is calling it a neural

**[24:41]** explaining it is calling it a neural

**[24:41]** explaining it is calling it a neural file system. And then I decided to just

**[24:44]** file system. And then I decided to just

**[24:44]** file system. And then I decided to just call it weights. I think it's easier to

**[24:45]** call it weights. I think it's easier to

**[24:45]** call it weights. I think it's easier to understand, but this slide still says

**[24:47]** understand, but this slide still says

**[24:47]** understand, but this slide still says neural file systems. Um so I think

**[24:51]** neural file systems. Um so I think

**[24:51]** neural file systems. Um so I think there's a few questions here like we

**[24:52]** there's a few questions here like we

**[24:52]** there's a few questions here like we want to train all our data into the

**[24:54]** want to train all our data into the

**[24:54]** want to train all our data into the model. One question is like how do we

**[24:55]** model. One question is like how do we

**[24:55]** model. One question is like how do we train it? Do we do RL? Do we do SFT? Uh

**[24:58]** train it? Do we do RL? Do we do SFT? Uh

**[24:58]** train it? Do we do RL? Do we do SFT? Uh what's what even is the data? Um another


### [25:00 - 26:00]

**[25:01]** what's what even is the data? Um another

**[25:01]** what's what even is the data? Um another question is like out of uh all the

**[25:04]** question is like out of uh all the

**[25:04]** question is like out of uh all the possible data what do we use? Do we just

**[25:07]** possible data what do we use? Do we just

**[25:07]** possible data what do we use? Do we just like fine-tune directly on our data? Do

**[25:09]** like fine-tune directly on our data? Do

**[25:09]** like fine-tune directly on our data? Do we try to generate more? I think my

**[25:11]** we try to generate more? I think my

**[25:11]** we try to generate more? I think my argument is that we should try to

**[25:13]** argument is that we should try to

**[25:13]** argument is that we should try to generate more and I'll show you why. And

**[25:15]** generate more and I'll show you why. And

**[25:15]** generate more and I'll show you why. And then there's an architectural question.

**[25:17]** then there's an architectural question.

**[25:17]** then there's an architectural question. Like I think for a long time, people

**[25:19]** Like I think for a long time, people

**[25:19]** Like I think for a long time, people really cared in the machine learning

**[25:21]** really cared in the machine learning

**[25:21]** really cared in the machine learning deep learning community about like what

**[25:23]** deep learning community about like what

**[25:23]** deep learning community about like what architectures we should use. And then

**[25:24]** architectures we should use. And then

**[25:24]** architectures we should use. And then for like what 8 years, everyone who

**[25:27]** for like what 8 years, everyone who

**[25:28]** for like what 8 years, everyone who knows what they're doing has really just

**[25:29]** knows what they're doing has really just

**[25:29]** knows what they're doing has really just been using transformers unless they're

**[25:30]** been using transformers unless they're

**[25:30]** been using transformers unless they're trying to make them better. And I think

**[25:33]** trying to make them better. And I think

**[25:33]** trying to make them better. And I think now in this world where we're trying to

**[25:35]** now in this world where we're trying to

**[25:35]** now in this world where we're trying to train stuff into models like like if you

**[25:38]** train stuff into models like like if you

**[25:38]** train stuff into models like like if you think of okay world we all each of us

**[25:39]** think of okay world we all each of us

**[25:39]** think of okay world we all each of us have has our own model or maybe multiple

**[25:41]** have has our own model or maybe multiple

**[25:41]** have has our own model or maybe multiple models and those models are getting

**[25:43]** models and those models are getting

**[25:43]** models and those models are getting updated a lot. I think we start to care

**[25:45]** updated a lot. I think we start to care

**[25:45]** updated a lot. I think we start to care about architecture again and I'll and

**[25:47]** about architecture again and I'll and

**[25:47]** about architecture again and I'll and I'll tell you why and like what I think

**[25:48]** I'll tell you why and like what I think

**[25:48]** I'll tell you why and like what I think the options are. [clears throat] So

**[25:50]** the options are. [clears throat] So

**[25:50]** the options are. [clears throat] So first let's talk about learning.

**[25:53]** first let's talk about learning.

**[25:53]** first let's talk about learning. Um

**[25:55]** Um

**[25:56]** Um so I think like the mental [snorts]

**[25:57]** so I think like the mental [snorts]

**[25:57]** so I think like the mental [snorts] model here which I mentioned before is


### [26:00 - 27:00]

**[26:00]** model here which I mentioned before is

**[26:00]** model here which I mentioned before is like we're trying to train the model to

**[26:03]** like we're trying to train the model to

**[26:03]** like we're trying to train the model to learn the data as best as it possibly

**[26:05]** learn the data as best as it possibly

**[26:05]** learn the data as best as it possibly can and it's going to be expensive. So

**[26:08]** can and it's going to be expensive. So

**[26:08]** can and it's going to be expensive. So like we didn't like rag but also rag

**[26:10]** like we didn't like rag but also rag

**[26:10]** like we didn't like rag but also rag didn't cost us very much money. I think

**[26:12]** didn't cost us very much money. I think

**[26:12]** didn't cost us very much money. I think to do better than rag, we're gonna have

**[26:14]** to do better than rag, we're gonna have

**[26:14]** to do better than rag, we're gonna have to like pay some GPU points and that's

**[26:18]** to like pay some GPU points and that's

**[26:18]** to like pay some GPU points and that's just like the state of the world. Okay,

**[26:20]** just like the state of the world. Okay,

**[26:20]** just like the state of the world. Okay, fine. So, this is our model. It's like

**[26:22]** fine. So, this is our model. It's like

**[26:22]** fine. So, this is our model. It's like this homogeneous blob of data and this

**[26:25]** this homogeneous blob of data and this

**[26:25]** this homogeneous blob of data and this is our data. So, like maybe we have the

**[26:27]** is our data. So, like maybe we have the

**[26:27]** is our data. So, like maybe we have the masterard data set or maybe we collected

**[26:29]** masterard data set or maybe we collected

**[26:29]** masterard data set or maybe we collected data about ourselves or maybe I uh

**[26:32]** data about ourselves or maybe I uh

**[26:32]** data about ourselves or maybe I uh collected all my traces from coding in

**[26:34]** collected all my traces from coding in

**[26:34]** collected all my traces from coding in November and December and I want to like

**[26:36]** November and December and I want to like

**[26:36]** November and December and I want to like train the the model to learn my problems

**[26:38]** train the the model to learn my problems

**[26:38]** train the the model to learn my problems better. What do I do? How do I actually

**[26:40]** better. What do I do? How do I actually

**[26:40]** better. What do I do? How do I actually do this? Um

**[26:43]** do this? Um

**[26:43]** do this? Um let's let's like start with the dumbest

**[26:45]** let's let's like start with the dumbest

**[26:45]** let's let's like start with the dumbest possible approach and just like see what

**[26:47]** possible approach and just like see what

**[26:47]** possible approach and just like see what happens. So say uh we start with a data

**[26:50]** happens. So say uh we start with a data

**[26:50]** happens. So say uh we start with a data set and we just train on it.

**[26:54]** set and we just train on it.

**[26:54]** set and we just train on it. Um like using I guess next token

**[26:56]** Um like using I guess next token

**[26:56]** Um like using I guess next token prediction. So we actually ran this


### [27:00 - 28:00]

**[27:00]** prediction. So we actually ran this

**[27:00]** prediction. So we actually ran this little experiment. This is like uh 3M.

**[27:03]** little experiment. This is like uh 3M.

**[27:03]** little experiment. This is like uh 3M. It's a company they make doct and um

**[27:08]** It's a company they make doct and um

**[27:08]** It's a company they make doct and um this is like some financial reports. So

**[27:10]** this is like some financial reports. So

**[27:10]** this is like some financial reports. So maybe like you're working there and you

**[27:12]** maybe like you're working there and you

**[27:12]** maybe like you're working there and you really don't want to read all of this.

**[27:14]** really don't want to read all of this.

**[27:14]** really don't want to read all of this. So you just want to ask the model to

**[27:15]** So you just want to ask the model to

**[27:16]** So you just want to ask the model to like really understand this and be able

**[27:18]** like really understand this and be able

**[27:18]** like really understand this and be able to answer questions and like rag isn't

**[27:20]** to answer questions and like rag isn't

**[27:20]** to answer questions and like rag isn't really working cuz it's like this weird

**[27:21]** really working cuz it's like this weird

**[27:22]** really working cuz it's like this weird structure and there's a lot of ways the

**[27:23]** structure and there's a lot of ways the

**[27:23]** structure and there's a lot of ways the documents interrelate. Okay, cool. So

**[27:25]** documents interrelate. Okay, cool. So

**[27:25]** documents interrelate. Okay, cool. So we're just going to like train the model

**[27:27]** we're just going to like train the model

**[27:27]** we're just going to like train the model using next token prediction. See what

**[27:30]** using next token prediction. See what

**[27:30]** using next token prediction. See what happens. You know what? Actually, even

**[27:32]** happens. You know what? Actually, even

**[27:32]** happens. You know what? Actually, even if you don't train the whole model, um

**[27:35]** if you don't train the whole model, um

**[27:35]** if you don't train the whole model, um you you still get zero loss. So the

**[27:37]** you you still get zero loss. So the

**[27:37]** you you still get zero loss. So the model can perfectly memorize this entire

**[27:40]** model can perfectly memorize this entire

**[27:40]** model can perfectly memorize this entire uh 3M 10K financial report. Um it's

**[27:44]** uh 3M 10K financial report. Um it's

**[27:44]** uh 3M 10K financial report. Um it's extremely impressive.

**[27:46]** extremely impressive.

**[27:46]** extremely impressive. Okay. So now let's talk to it. So so we

**[27:48]** Okay. So now let's talk to it. So so we

**[27:48]** Okay. So now let's talk to it. So so we did this and then we didn't want to ask

**[27:50]** did this and then we didn't want to ask

**[27:50]** did this and then we didn't want to ask anything that's like exactly present in

**[27:52]** anything that's like exactly present in

**[27:52]** anything that's like exactly present in the document because we want to see if

**[27:53]** the document because we want to see if

**[27:53]** the document because we want to see if the model's actually good. So we started

**[27:55]** the model's actually good. So we started

**[27:55]** the model's actually good. So we started you know like everyone loves to test

**[27:56]** you know like everyone loves to test

**[27:56]** you know like everyone loves to test poems. So we started with a poem. We

**[27:58]** poems. So we started with a poem. We

**[27:58]** poems. So we started with a poem. We said can you write a poem about 3M in


### [28:00 - 29:00]

**[28:01]** said can you write a poem about 3M in

**[28:01]** said can you write a poem about 3M in fiscal year 2025?

**[28:03]** fiscal year 2025?

**[28:04]** fiscal year 2025? So, register your bets. And what do you

**[28:06]** So, register your bets. And what do you

**[28:06]** So, register your bets. And what do you think happened?

**[28:07]** think happened?

**[28:07]** think happened? >> It's terrible.

**[28:09]** >> It's terrible.

**[28:09]** >> It's terrible. >> It's terrible. Someone said it. It says

**[28:12]** >> It's terrible. Someone said it. It says

**[28:12]** >> It's terrible. Someone said it. It says the passage of a passage is a poem. End

**[28:15]** the passage of a passage is a poem. End

**[28:15]** the passage of a passage is a poem. End of sentence.

**[28:17]** of sentence.

**[28:17]** of sentence. It's crazy. [laughter]

**[28:19]** It's crazy. [laughter]

**[28:19]** It's crazy. [laughter] Yeah. So, now maybe we ask like why does

**[28:21]** Yeah. So, now maybe we ask like why does

**[28:21]** Yeah. So, now maybe we ask like why does this happen and how do we fix it? So,

**[28:23]** this happen and how do we fix it? So,

**[28:23]** this happen and how do we fix it? So, unfortunately, this doesn't work. And I

**[28:25]** unfortunately, this doesn't work. And I

**[28:25]** unfortunately, this doesn't work. And I actually think this is like one of the

**[28:26]** actually think this is like one of the

**[28:26]** actually think this is like one of the reasons why people haven't been doing

**[28:27]** reasons why people haven't been doing

**[28:27]** reasons why people haven't been doing this yet is because the dumbest possible

**[28:29]** this yet is because the dumbest possible

**[28:29]** this yet is because the dumbest possible approach usually does work in machine

**[28:31]** approach usually does work in machine

**[28:31]** approach usually does work in machine learning. But in this case, we have to

**[28:33]** learning. But in this case, we have to

**[28:33]** learning. But in this case, we have to do something a little bit more

**[28:34]** do something a little bit more

**[28:34]** do something a little bit more sophisticated. Um,

**[28:37]** sophisticated. Um,

**[28:37]** sophisticated. Um, so maybe take a second and think about

**[28:38]** so maybe take a second and think about

**[28:38]** so maybe take a second and think about like what you would do. You're facing

**[28:39]** like what you would do. You're facing

**[28:39]** like what you would do. You're facing this problem at work or in a side

**[28:41]** this problem at work or in a side

**[28:41]** this problem at work or in a side project. Um, I think there's like two

**[28:44]** project. Um, I think there's like two

**[28:44]** project. Um, I think there's like two things we need to fix. One is that um

**[28:48]** things we need to fix. One is that um

**[28:48]** things we need to fix. One is that um the data is not it's not exactly what we

**[28:52]** the data is not it's not exactly what we

**[28:52]** the data is not it's not exactly what we want to train on, I think. And two is

**[28:55]** want to train on, I think. And two is

**[28:55]** want to train on, I think. And two is that we probably don't want to update

**[28:57]** that we probably don't want to update

**[28:57]** that we probably don't want to update the entire model because what we did

**[28:59]** the entire model because what we did

**[28:59]** the entire model because what we did there was basically overwrite all the


### [29:00 - 30:00]

**[29:02]** there was basically overwrite all the

**[29:02]** there was basically overwrite all the you know stuff about Tajikistan and

**[29:03]** you know stuff about Tajikistan and

**[29:03]** you know stuff about Tajikistan and everything else that's in the model with

**[29:05]** everything else that's in the model with

**[29:05]** everything else that's in the model with just like this 3M knowledge and I think

**[29:08]** just like this 3M knowledge and I think

**[29:08]** just like this 3M knowledge and I think that's like too specific and then the

**[29:09]** that's like too specific and then the

**[29:09]** that's like too specific and then the model is just obsessed with 3M and it'll

**[29:12]** model is just obsessed with 3M and it'll

**[29:12]** model is just obsessed with 3M and it'll only produce exact copy sentences from

**[29:15]** only produce exact copy sentences from

**[29:15]** only produce exact copy sentences from the document. That's that's clearly too

**[29:17]** the document. That's that's clearly too

**[29:17]** the document. That's that's clearly too much. So I think we need a better way to

**[29:19]** much. So I think we need a better way to

**[29:19]** much. So I think we need a better way to update the model and we need a better

**[29:21]** update the model and we need a better

**[29:21]** update the model and we need a better way to change the data.

**[29:23]** way to change the data.

**[29:23]** way to change the data. Um, there's this pretty relevant work. I

**[29:25]** Um, there's this pretty relevant work. I

**[29:26]** Um, there's this pretty relevant work. I don't know if you follow this like LLM

**[29:27]** don't know if you follow this like LLM

**[29:27]** don't know if you follow this like LLM chat thing from Andre Karpathy. Shout

**[29:30]** chat thing from Andre Karpathy. Shout

**[29:30]** chat thing from Andre Karpathy. Shout out. I think it's very educational and

**[29:32]** out. I think it's very educational and

**[29:32]** out. I think it's very educational and he had a really good question which is

**[29:34]** he had a really good question which is

**[29:34]** he had a really good question which is like he built this small LLM and train

**[29:36]** like he built this small LLM and train

**[29:36]** like he built this small LLM and train it from scratch and everything and then

**[29:38]** it from scratch and everything and then

**[29:38]** it from scratch and everything and then he wanted to teach it about himself and

**[29:41]** he wanted to teach it about himself and

**[29:41]** he wanted to teach it about himself and okay maybe the first thing you would try

**[29:43]** okay maybe the first thing you would try

**[29:43]** okay maybe the first thing you would try is rag. You put like a little database

**[29:45]** is rag. You put like a little database

**[29:45]** is rag. You put like a little database of information about yourself but that's

**[29:47]** of information about yourself but that's

**[29:47]** of information about yourself but that's only scalable to a certain amount and

**[29:50]** only scalable to a certain amount and

**[29:50]** only scalable to a certain amount and then the model can't really like combine

**[29:51]** then the model can't really like combine

**[29:51]** then the model can't really like combine things. it can only kind of regurgitate

**[29:54]** things. it can only kind of regurgitate

**[29:54]** things. it can only kind of regurgitate facts. And so he wants to actually teach

**[29:57]** facts. And so he wants to actually teach

**[29:57]** facts. And so he wants to actually teach it properly, he says, meaning in

**[29:59]** it properly, he says, meaning in

**[29:59]** it properly, he says, meaning in weights. And so notice he doesn't just


### [30:00 - 31:00]

**[30:02]** weights. And so notice he doesn't just

**[30:02]** weights. And so notice he doesn't just like take one example and and train the

**[30:04]** like take one example and and train the

**[30:04]** like take one example and and train the model using next token prediction. He

**[30:06]** model using next token prediction. He

**[30:06]** model using next token prediction. He does something a bit more complicated.

**[30:08]** does something a bit more complicated.

**[30:08]** does something a bit more complicated. He like generates this task or you don't

**[30:11]** He like generates this task or you don't

**[30:11]** He like generates this task or you don't have to care about the specifics, but

**[30:12]** have to care about the specifics, but

**[30:12]** have to care about the specifics, but there's like basically he makes a

**[30:13]** there's like basically he makes a

**[30:13]** there's like basically he makes a diverse training data set of examples

**[30:16]** diverse training data set of examples

**[30:16]** diverse training data set of examples that look like the thing he cares about

**[30:18]** that look like the thing he cares about

**[30:18]** that look like the thing he cares about and then trains on it. And if you go,

**[30:20]** and then trains on it. And if you go,

**[30:20]** and then trains on it. And if you go, you can find this. It actually does work

**[30:21]** you can find this. It actually does work

**[30:21]** you can find this. It actually does work pretty well, which is cool. So, he's

**[30:23]** pretty well, which is cool. So, he's

**[30:23]** pretty well, which is cool. So, he's able to teach a novel behavior to a

**[30:25]** able to teach a novel behavior to a

**[30:25]** able to teach a novel behavior to a model by like generating a lot of

**[30:27]** model by like generating a lot of

**[30:27]** model by like generating a lot of synthetic data that looks like the

**[30:28]** synthetic data that looks like the

**[30:28]** synthetic data that looks like the example he cares about and then

**[30:30]** example he cares about and then

**[30:30]** example he cares about and then fine-tuning the model for a little bit

**[30:32]** fine-tuning the model for a little bit

**[30:32]** fine-tuning the model for a little bit and it and it learns. There's a paper

**[30:34]** and it and it learns. There's a paper

**[30:34]** and it and it learns. There's a paper that's really good uh that's from last

**[30:37]** that's really good uh that's from last

**[30:37]** that's really good uh that's from last year from some folks at Stanford called

**[30:39]** year from some folks at Stanford called

**[30:39]** year from some folks at Stanford called synthetic continued pre-training and

**[30:41]** synthetic continued pre-training and

**[30:41]** synthetic continued pre-training and they have the same problem. So they have

**[30:42]** they have the same problem. So they have

**[30:42]** they have the same problem. So they have like a really small data set and they

**[30:44]** like a really small data set and they

**[30:44]** like a really small data set and they want to teach the model to the data set

**[30:46]** want to teach the model to the data set

**[30:46]** want to teach the model to the data set without like bricking the model

**[30:47]** without like bricking the model

**[30:48]** without like bricking the model essentially and they have this kind of

**[30:51]** essentially and they have this kind of

**[30:51]** essentially and they have this kind of fancy way of generating synthetic data

**[30:53]** fancy way of generating synthetic data

**[30:53]** fancy way of generating synthetic data by extracting entities. But I think the

**[30:55]** by extracting entities. But I think the

**[30:56]** by extracting entities. But I think the important part is that they take a small

**[30:58]** important part is that they take a small

**[30:58]** important part is that they take a small data set and they generate like a very


### [31:00 - 32:00]

**[31:00]** data set and they generate like a very

**[31:00]** data set and they generate like a very large more diverse data set

**[31:03]** large more diverse data set

**[31:03]** large more diverse data set representative of the thing that they

**[31:04]** representative of the thing that they

**[31:04]** representative of the thing that they care about. And this is something that

**[31:06]** care about. And this is something that

**[31:06]** care about. And this is something that like breaks the whole like conventional

**[31:08]** like breaks the whole like conventional

**[31:08]** like breaks the whole like conventional machine learning paradigm. Like they

**[31:11]** machine learning paradigm. Like they

**[31:11]** machine learning paradigm. Like they only have a small training data set. So

**[31:14]** only have a small training data set. So

**[31:14]** only have a small training data set. So uh what you learn in school would tell

**[31:16]** uh what you learn in school would tell

**[31:16]** uh what you learn in school would tell you that you would just like overfit and

**[31:17]** you that you would just like overfit and

**[31:17]** you that you would just like overfit and there's nothing you can do. You just

**[31:18]** there's nothing you can do. You just

**[31:18]** there's nothing you can do. You just have to go back and collect more data.

**[31:20]** have to go back and collect more data.

**[31:20]** have to go back and collect more data. But actually because LLMs are so good

**[31:22]** But actually because LLMs are so good

**[31:22]** But actually because LLMs are so good now we can do this second thing where we

**[31:25]** now we can do this second thing where we

**[31:25]** now we can do this second thing where we generate like a much larger training

**[31:26]** generate like a much larger training

**[31:26]** generate like a much larger training data set. It really contains only the

**[31:29]** data set. It really contains only the

**[31:29]** data set. It really contains only the like facts that were present in the

**[31:31]** like facts that were present in the

**[31:31]** like facts that were present in the original data but it's so large that you

**[31:33]** original data but it's so large that you

**[31:33]** original data but it's so large that you can train a model on it. It's like very

**[31:34]** can train a model on it. It's like very

**[31:34]** can train a model on it. It's like very strange. It only recently started

**[31:36]** strange. It only recently started

**[31:36]** strange. It only recently started working, but it does work. I'll show you

**[31:38]** working, but it does work. I'll show you

**[31:38]** working, but it does work. I'll show you some evidence. Um, the green line is

**[31:41]** some evidence. Um, the green line is

**[31:41]** some evidence. Um, the green line is what happens when you do the dump thing

**[31:43]** what happens when you do the dump thing

**[31:43]** what happens when you do the dump thing before. So, you just like fine-tune the

**[31:45]** before. So, you just like fine-tune the

**[31:45]** before. So, you just like fine-tune the model on the data. It actually starts at

**[31:47]** model on the data. It actually starts at

**[31:47]** model on the data. It actually starts at the black line. [clears throat] So,

**[31:48]** the black line. [clears throat] So,

**[31:48]** the black line. [clears throat] So, surprisingly, it actually gets worse.

**[31:50]** surprisingly, it actually gets worse.

**[31:50]** surprisingly, it actually gets worse. So, it like memorizes the data so well

**[31:52]** So, it like memorizes the data so well

**[31:52]** So, it like memorizes the data so well that it can't answer any slightly

**[31:54]** that it can't answer any slightly

**[31:54]** that it can't answer any slightly different questions about it. Um the

**[31:56]** different questions about it. Um the

**[31:56]** different questions about it. Um the thing they do they have like two

**[31:58]** thing they do they have like two

**[31:58]** thing they do they have like two different ways of doing it but it's

**[31:59]** different ways of doing it but it's

**[31:59]** different ways of doing it but it's basically like generating lots of


### [32:00 - 33:00]

**[32:00]** basically like generating lots of

**[32:00]** basically like generating lots of synthetic data that describes the things

**[32:02]** synthetic data that describes the things

**[32:02]** synthetic data that describes the things in the original data set. It works very

**[32:05]** in the original data set. It works very

**[32:05]** in the original data set. It works very well like at some scale I guess 100

**[32:08]** well like at some scale I guess 100

**[32:08]** well like at some scale I guess 100 million tokens close to a billion they

**[32:10]** million tokens close to a billion they

**[32:10]** million tokens close to a billion they can actually outperform GPT4 in this

**[32:12]** can actually outperform GPT4 in this

**[32:12]** can actually outperform GPT4 in this data set which is really cool. So I

**[32:14]** data set which is really cool. So I

**[32:14]** data set which is really cool. So I think like the takeaway here is

**[32:17]** think like the takeaway here is

**[32:17]** think like the takeaway here is even though you don't have a lot of

**[32:18]** even though you don't have a lot of

**[32:18]** even though you don't have a lot of data, if you're willing to generate like

**[32:20]** data, if you're willing to generate like

**[32:20]** data, if you're willing to generate like a large synthetic data set that

**[32:22]** a large synthetic data set that

**[32:22]** a large synthetic data set that describes the data you have, you can

**[32:24]** describes the data you have, you can

**[32:24]** describes the data you have, you can actually train a model on it and it

**[32:26]** actually train a model on it and it

**[32:26]** actually train a model on it and it works really well.

**[32:28]** works really well.

**[32:28]** works really well. There's a bunch of other papers that do

**[32:29]** There's a bunch of other papers that do

**[32:29]** There's a bunch of other papers that do this. One is called active reading. Um

**[32:32]** this. One is called active reading. Um

**[32:32]** this. One is called active reading. Um they basically ask the LLM how what

**[32:35]** they basically ask the LLM how what

**[32:35]** they basically ask the LLM how what types of things should we generate? Then

**[32:36]** types of things should we generate? Then

**[32:36]** types of things should we generate? Then they generate from it. There is

**[32:38]** they generate from it. There is

**[32:38]** they generate from it. There is self-study which is from this cartridges

**[32:40]** self-study which is from this cartridges

**[32:40]** self-study which is from this cartridges paper which is more like question

**[32:41]** paper which is more like question

**[32:41]** paper which is more like question answering like asking the model to like

**[32:43]** answering like asking the model to like

**[32:43]** answering like asking the model to like quiz itself. And then there's this

**[32:45]** quiz itself. And then there's this

**[32:45]** quiz itself. And then there's this rephrasing the web thing. I didn't

**[32:47]** rephrasing the web thing. I didn't

**[32:47]** rephrasing the web thing. I didn't realize my

**[32:50]** realize my

**[32:50]** realize my whatever a rephrasing the web thing

**[32:52]** whatever a rephrasing the web thing

**[32:52]** whatever a rephrasing the web thing where they kind of like rephrase an

**[32:53]** where they kind of like rephrase an

**[32:53]** where they kind of like rephrase an entire pre-training data set. So this

**[32:55]** entire pre-training data set. So this

**[32:55]** entire pre-training data set. So this actually works at scale in kind of a

**[32:57]** actually works at scale in kind of a

**[32:57]** actually works at scale in kind of a surprising way. Um and there's a lot

**[32:59]** surprising way. Um and there's a lot

**[32:59]** surprising way. Um and there's a lot more work in this direction. So I'm


### [33:00 - 34:00]

**[33:00]** more work in this direction. So I'm

**[33:00]** more work in this direction. So I'm really excited about this like and I'm

**[33:02]** really excited about this like and I'm

**[33:02]** really excited about this like and I'm kind of monitoring it. There's a company

**[33:03]** kind of monitoring it. There's a company

**[33:03]** kind of monitoring it. There's a company called Daytology that's doing this

**[33:05]** called Daytology that's doing this

**[33:05]** called Daytology that's doing this really well. They're like generating

**[33:07]** really well. They're like generating

**[33:07]** really well. They're like generating really highquality synthetic data. It's

**[33:09]** really highquality synthetic data. It's

**[33:09]** really highquality synthetic data. It's just like not something that used to be

**[33:11]** just like not something that used to be

**[33:11]** just like not something that used to be possible until very recently when LLMs

**[33:14]** possible until very recently when LLMs

**[33:14]** possible until very recently when LLMs crossed some threshold that they're like

**[33:16]** crossed some threshold that they're like

**[33:16]** crossed some threshold that they're like able to generate data that's good enough

**[33:18]** able to generate data that's good enough

**[33:18]** able to generate data that's good enough to actually train themselves on. Oh,

**[33:20]** to actually train themselves on. Oh,

**[33:20]** to actually train themselves on. Oh, there's actually something pretty cool.

**[33:21]** there's actually something pretty cool.

**[33:21]** there's actually something pretty cool. It's not in the slide. It's called self

**[33:23]** It's not in the slide. It's called self

**[33:23]** It's not in the slide. It's called self adapting language models, self-edit.

**[33:27]** adapting language models, self-edit.

**[33:27]** adapting language models, self-edit. It's called SEAL. S E A L. And they uh

**[33:30]** It's called SEAL. S E A L. And they uh

**[33:30]** It's called SEAL. S E A L. And they uh ask the model what data to generate to

**[33:33]** ask the model what data to generate to

**[33:33]** ask the model what data to generate to make itself better. and under some like

**[33:35]** make itself better. and under some like

**[33:35]** make itself better. and under some like constrained scenarios, this is actually

**[33:36]** constrained scenarios, this is actually

**[33:36]** constrained scenarios, this is actually working. So that's like actually quite

**[33:38]** working. So that's like actually quite

**[33:38]** working. So that's like actually quite bizarre. Um, and like obviously doesn't

**[33:41]** bizarre. Um, and like obviously doesn't

**[33:41]** bizarre. Um, and like obviously doesn't work infinitely or else they would have

**[33:43]** work infinitely or else they would have

**[33:43]** work infinitely or else they would have caused an intelligence explosion. But

**[33:45]** caused an intelligence explosion. But

**[33:45]** caused an intelligence explosion. But the fact that it works at all is like

**[33:47]** the fact that it works at all is like

**[33:47]** the fact that it works at all is like really remarkable and I think like worth

**[33:49]** really remarkable and I think like worth

**[33:49]** really remarkable and I think like worth monitoring. So

**[33:52]** monitoring. So

**[33:52]** monitoring. So in conclusion for this section, we want

**[33:53]** in conclusion for this section, we want

**[33:54]** in conclusion for this section, we want to train things into weights. We can

**[33:55]** to train things into weights. We can

**[33:55]** to train things into weights. We can generate large synthetic data sets that

**[33:57]** generate large synthetic data sets that

**[33:57]** generate large synthetic data sets that describe very pretty small data sets and


### [34:00 - 35:00]

**[34:00]** describe very pretty small data sets and

**[34:00]** describe very pretty small data sets and it works fine. Um, now I think the money

**[34:04]** it works fine. Um, now I think the money

**[34:04]** it works fine. Um, now I think the money question here is like how do we inject

**[34:06]** question here is like how do we inject

**[34:06]** question here is like how do we inject the information into the model? I think

**[34:08]** the information into the model? I think

**[34:08]** the information into the model? I think before I mentioned we were training all

**[34:09]** before I mentioned we were training all

**[34:09]** before I mentioned we were training all the parameters and we tried it and it

**[34:11]** the parameters and we tried it and it

**[34:11]** the parameters and we tried it and it worked really bad. And this is a a

**[34:14]** worked really bad. And this is a a

**[34:14]** worked really bad. And this is a a problem that's been around for a long

**[34:17]** problem that's been around for a long

**[34:17]** problem that's been around for a long time. It's called like catastrophic

**[34:18]** time. It's called like catastrophic

**[34:18]** time. It's called like catastrophic forgetting. Um, even in old school

**[34:20]** forgetting. Um, even in old school

**[34:20]** forgetting. Um, even in old school machine learning like you train a model

**[34:22]** machine learning like you train a model

**[34:22]** machine learning like you train a model to recognize handwritten digits and then

**[34:24]** to recognize handwritten digits and then

**[34:24]** to recognize handwritten digits and then you train a model to recognize house

**[34:26]** you train a model to recognize house

**[34:26]** you train a model to recognize house numbers and it's no longer able to

**[34:27]** numbers and it's no longer able to

**[34:27]** numbers and it's no longer able to recognize handwritten digits. This is

**[34:29]** recognize handwritten digits. This is

**[34:29]** recognize handwritten digits. This is like a very well-known problem. there's

**[34:31]** like a very well-known problem. there's

**[34:31]** like a very well-known problem. there's a lot of like theory and like approaches

**[34:33]** a lot of like theory and like approaches

**[34:33]** a lot of like theory and like approaches proposed to solve it, but no one really

**[34:35]** proposed to solve it, but no one really

**[34:35]** proposed to solve it, but no one really knows how to solve it. It's very very

**[34:36]** knows how to solve it. It's very very

**[34:36]** knows how to solve it. It's very very hard. Um,

**[34:38]** hard. Um,

**[34:38]** hard. Um, but I think there are some easy ways we

**[34:41]** but I think there are some easy ways we

**[34:41]** but I think there are some easy ways we can get around it in the conventional

**[34:43]** can get around it in the conventional

**[34:43]** can get around it in the conventional paradigm where we have like this big

**[34:45]** paradigm where we have like this big

**[34:45]** paradigm where we have like this big pre-trained child GBT transformer. Uh,

**[34:48]** pre-trained child GBT transformer. Uh,

**[34:48]** pre-trained child GBT transformer. Uh, instead of retraining the entire model,

**[34:50]** instead of retraining the entire model,

**[34:50]** instead of retraining the entire model, there's a few different ways we can do

**[34:51]** there's a few different ways we can do

**[34:51]** there's a few different ways we can do it. I mean, the first one is retraining

**[34:54]** it. I mean, the first one is retraining

**[34:54]** it. I mean, the first one is retraining the entire model. So, the things we're

**[34:55]** the entire model. So, the things we're

**[34:55]** the entire model. So, the things we're training I'm highlighting in blue here.

**[34:57]** training I'm highlighting in blue here.

**[34:57]** training I'm highlighting in blue here. That's like if we take our transformer

**[34:58]** That's like if we take our transformer

**[34:58]** That's like if we take our transformer and we update all the parameters, we're


### [35:00 - 36:00]

**[35:01]** and we update all the parameters, we're

**[35:01]** and we update all the parameters, we're probably going to forget stuff. Um,

**[35:03]** probably going to forget stuff. Um,

**[35:03]** probably going to forget stuff. Um, there's another one that's pretty cool

**[35:05]** there's another one that's pretty cool

**[35:05]** there's another one that's pretty cool called prefix tuning where you just

**[35:06]** called prefix tuning where you just

**[35:06]** called prefix tuning where you just train the KV cache. Um, I mean, I'll

**[35:10]** train the KV cache. Um, I mean, I'll

**[35:10]** train the KV cache. Um, I mean, I'll like skip the details for now, but ask

**[35:11]** like skip the details for now, but ask

**[35:11]** like skip the details for now, but ask me if you have questions. Prefix tuning

**[35:13]** me if you have questions. Prefix tuning

**[35:13]** me if you have questions. Prefix tuning is cool. Um, another way is since a lot

**[35:16]** is cool. Um, another way is since a lot

**[35:16]** is cool. Um, another way is since a lot of these models are called like mixer

**[35:17]** of these models are called like mixer

**[35:17]** of these models are called like mixer experts and they have this MLP layer in

**[35:20]** experts and they have this MLP layer in

**[35:20]** experts and they have this MLP layer in them, you can add another part to the

**[35:22]** them, you can add another part to the

**[35:22]** them, you can add another part to the MLP that is optionally routed to and

**[35:25]** MLP that is optionally routed to and

**[35:25]** MLP that is optionally routed to and used and that's like pretty scalable. I

**[35:27]** used and that's like pretty scalable. I

**[35:27]** used and that's like pretty scalable. I think people try this. Um, there's

**[35:30]** think people try this. Um, there's

**[35:30]** think people try this. Um, there's another approach where where you replace

**[35:32]** another approach where where you replace

**[35:32]** another approach where where you replace instead of like another MLP, you build

**[35:33]** instead of like another MLP, you build

**[35:33]** instead of like another MLP, you build this thing called a memory layer which

**[35:35]** this thing called a memory layer which

**[35:35]** this thing called a memory layer which is like a big lookup table. I think

**[35:37]** is like a big lookup table. I think

**[35:37]** is like a big lookup table. I think memory layers are really good. And let

**[35:39]** memory layers are really good. And let

**[35:39]** memory layers are really good. And let me pause and say now this part of the

**[35:41]** me pause and say now this part of the

**[35:41]** me pause and say now this part of the talk is getting close to purely

**[35:43]** talk is getting close to purely

**[35:43]** talk is getting close to purely speculative. This is like the things

**[35:45]** speculative. This is like the things

**[35:45]** speculative. This is like the things that are like they exist and like

**[35:47]** that are like they exist and like

**[35:47]** that are like they exist and like someone's going to do this and someone's

**[35:49]** someone's going to do this and someone's

**[35:49]** someone's going to do this and someone's going to use like one of them but I

**[35:50]** going to use like one of them but I

**[35:50]** going to use like one of them but I really don't know what the right answer

**[35:51]** really don't know what the right answer

**[35:51]** really don't know what the right answer is. Um another one is called low. So low

**[35:54]** is. Um another one is called low. So low

**[35:54]** is. Um another one is called low. So low rank adaptation. You probably heard of

**[35:56]** rank adaptation. You probably heard of

**[35:56]** rank adaptation. You probably heard of this very like hot topic. Um they kind

**[35:59]** this very like hot topic. Um they kind

**[35:59]** this very like hot topic. Um they kind of like train a small a small matrix or


### [36:00 - 37:00]

**[36:02]** of like train a small a small matrix or

**[36:02]** of like train a small a small matrix or small few matrices to adapt the linear

**[36:05]** small few matrices to adapt the linear

**[36:05]** small few matrices to adapt the linear layers. So it's like if your model's 10

**[36:07]** layers. So it's like if your model's 10

**[36:07]** layers. So it's like if your model's 10 billion parameters, maybe you train 10

**[36:09]** billion parameters, maybe you train 10

**[36:09]** billion parameters, maybe you train 10 million parameters that can like control

**[36:11]** million parameters that can like control

**[36:11]** million parameters that can like control it. Um,

**[36:14]** it. Um,

**[36:14]** it. Um, and if we look at them together, maybe

**[36:15]** and if we look at them together, maybe

**[36:16]** and if we look at them together, maybe it's not super obvious which thing would

**[36:18]** it's not super obvious which thing would

**[36:18]** it's not super obvious which thing would work best. Like ICL is just like putting

**[36:20]** work best. Like ICL is just like putting

**[36:20]** work best. Like ICL is just like putting stuff in context. So we have in context

**[36:23]** stuff in context. So we have in context

**[36:23]** stuff in context. So we have in context rag full fine tuning. We could do the

**[36:25]** rag full fine tuning. We could do the

**[36:25]** rag full fine tuning. We could do the memory layers in MLP cartridges which is

**[36:28]** memory layers in MLP cartridges which is

**[36:28]** memory layers in MLP cartridges which is a prefix tuning and we could do Lorra.

**[36:30]** a prefix tuning and we could do Lorra.

**[36:30]** a prefix tuning and we could do Lorra. We could also do add something to the

**[36:32]** We could also do add something to the

**[36:32]** We could also do add something to the mixture of experts. I think to me it's

**[36:34]** mixture of experts. I think to me it's

**[36:34]** mixture of experts. I think to me it's not like clear and I'm not positive that

**[36:36]** not like clear and I'm not positive that

**[36:36]** not like clear and I'm not positive that it matters which one we do. Like I think

**[36:39]** it matters which one we do. Like I think

**[36:39]** it matters which one we do. Like I think the main thing is like we have this

**[36:40]** the main thing is like we have this

**[36:40]** the main thing is like we have this giant model and we're adding a tiny bit

**[36:43]** giant model and we're adding a tiny bit

**[36:43]** giant model and we're adding a tiny bit to it to control it and training only

**[36:45]** to it to control it and training only

**[36:45]** to it to control it and training only those parameters. That way we retain

**[36:47]** those parameters. That way we retain

**[36:47]** those parameters. That way we retain most of the information in the model. I

**[36:49]** most of the information in the model. I

**[36:49]** most of the information in the model. I think that's like the most important

**[36:51]** think that's like the most important

**[36:51]** think that's like the most important part. But I think for the end of this

**[36:53]** part. But I think for the end of this

**[36:53]** part. But I think for the end of this talk I'll just talk through like what I

**[36:56]** talk I'll just talk through like what I

**[36:56]** talk I'll just talk through like what I think people are doing in this space up

**[36:57]** think people are doing in this space up

**[36:57]** think people are doing in this space up to like the minute and then you can make


### [37:00 - 38:00]

**[37:00]** to like the minute and then you can make

**[37:00]** to like the minute and then you can make up your own mind what you think the

**[37:01]** up your own mind what you think the

**[37:01]** up your own mind what you think the right way to do it is. So let's talk for

**[37:03]** right way to do it is. So let's talk for

**[37:03]** right way to do it is. So let's talk for a second about what properties we want.

**[37:05]** a second about what properties we want.

**[37:05]** a second about what properties we want. I think we want um we want our changes

**[37:08]** I think we want um we want our changes

**[37:08]** I think we want um we want our changes to the model to be very small. Like say

**[37:10]** to the model to be very small. Like say

**[37:10]** to the model to be very small. Like say you're serving a model to each person.

**[37:13]** you're serving a model to each person.

**[37:13]** you're serving a model to each person. You actually can do it, but you have to

**[37:15]** You actually can do it, but you have to

**[37:15]** You actually can do it, but you have to use one of these like parameter

**[37:16]** use one of these like parameter

**[37:16]** use one of these like parameter efficient methods. If you're trying to

**[37:17]** efficient methods. If you're trying to

**[37:17]** efficient methods. If you're trying to fine-tune a new Kimmy for each person,

**[37:19]** fine-tune a new Kimmy for each person,

**[37:20]** fine-tune a new Kimmy for each person, Kimmyy's like a terabyte. It's a

**[37:21]** Kimmyy's like a terabyte. It's a

**[37:21]** Kimmyy's like a terabyte. It's a trillion parameters. It's just like not

**[37:23]** trillion parameters. It's just like not

**[37:23]** trillion parameters. It's just like not even storeable, let alone servable. Um

**[37:27]** even storeable, let alone servable. Um

**[37:27]** even storeable, let alone servable. Um we want something that's resistant to

**[37:28]** we want something that's resistant to

**[37:28]** we want something that's resistant to forgetting like we said. So it would be

**[37:30]** forgetting like we said. So it would be

**[37:30]** forgetting like we said. So it would be nice to have an architectural change

**[37:32]** nice to have an architectural change

**[37:32]** nice to have an architectural change that's both small and makes the minimal

**[37:34]** that's both small and makes the minimal

**[37:34]** that's both small and makes the minimal impact on the model as it is now because

**[37:36]** impact on the model as it is now because

**[37:36]** impact on the model as it is now because the model as it is now works really

**[37:38]** the model as it is now works really

**[37:38]** the model as it is now works really well. Um and preferably high capacity I

**[37:42]** well. Um and preferably high capacity I

**[37:42]** well. Um and preferably high capacity I think like changes that are really

**[37:44]** think like changes that are really

**[37:44]** think like changes that are really expressive and can capture a lot of

**[37:46]** expressive and can capture a lot of

**[37:46]** expressive and can capture a lot of facts and few parameters are the ones

**[37:48]** facts and few parameters are the ones

**[37:48]** facts and few parameters are the ones that we prefer and we want to be able to

**[37:50]** that we prefer and we want to be able to

**[37:50]** that we prefer and we want to be able to do inference quickly. As like a small

**[37:53]** do inference quickly. As like a small

**[37:53]** do inference quickly. As like a small aside, you actually can do this quickly

**[37:55]** aside, you actually can do this quickly

**[37:55]** aside, you actually can do this quickly with a lot of um a lot of these methods.

**[37:58]** with a lot of um a lot of these methods.

**[37:58]** with a lot of um a lot of these methods. Like maybe some of you have seen Tinker,


### [38:00 - 39:00]

**[38:00]** Like maybe some of you have seen Tinker,

**[38:00]** Like maybe some of you have seen Tinker, this new training API from Thinking

**[38:01]** this new training API from Thinking

**[38:01]** this new training API from Thinking Machines. It's basically all predicated

**[38:04]** Machines. It's basically all predicated

**[38:04]** Machines. It's basically all predicated on this idea that you can you can serve

**[38:06]** on this idea that you can you can serve

**[38:06]** on this idea that you can you can serve one model per person as long as you do

**[38:09]** one model per person as long as you do

**[38:09]** one model per person as long as you do Lorra and batch the Loras. And there's

**[38:11]** Lorra and batch the Loras. And there's

**[38:12]** Lorra and batch the Loras. And there's like it's actually most interesting from

**[38:13]** like it's actually most interesting from

**[38:13]** like it's actually most interesting from systems perspective. There's like ways

**[38:15]** systems perspective. There's like ways

**[38:15]** systems perspective. There's like ways you can train it and train each one

**[38:16]** you can train it and train each one

**[38:16]** you can train it and train each one separately and there's ways you can do

**[38:18]** separately and there's ways you can do

**[38:18]** separately and there's ways you can do inference and it basically has no cost.

**[38:20]** inference and it basically has no cost.

**[38:20]** inference and it basically has no cost. um which is really interesting just

**[38:22]** um which is really interesting just

**[38:22]** um which is really interesting just because like the base model doesn't

**[38:23]** because like the base model doesn't

**[38:23]** because like the base model doesn't change and we all share the same base

**[38:25]** change and we all share the same base

**[38:25]** change and we all share the same base model. So all the ideas I'm going to

**[38:27]** model. So all the ideas I'm going to

**[38:27]** model. So all the ideas I'm going to talk about are kind of like in the same

**[38:29]** talk about are kind of like in the same

**[38:29]** talk about are kind of like in the same direction as Tinker. Um

**[38:32]** direction as Tinker. Um

**[38:32]** direction as Tinker. Um we can think about like whether certain

**[38:35]** we can think about like whether certain

**[38:35]** we can think about like whether certain methods might learn more or forget more.

**[38:37]** methods might learn more or forget more.

**[38:38]** methods might learn more or forget more. Um so this is comparing Lorra to full

**[38:41]** Um so this is comparing Lorra to full

**[38:41]** Um so this is comparing Lorra to full fine-tuning. So Loa makes a tiny change

**[38:43]** fine-tuning. So Loa makes a tiny change

**[38:43]** fine-tuning. So Loa makes a tiny change to the model. Full fine-tuning updates

**[38:45]** to the model. Full fine-tuning updates

**[38:45]** to the model. Full fine-tuning updates the entire model. And on two different

**[38:47]** the entire model. And on two different

**[38:47]** the entire model. And on two different settings, they show like low here is

**[38:50]** settings, they show like low here is

**[38:50]** settings, they show like low here is like purplish or pink. The pink one's a

**[38:52]** like purplish or pink. The pink one's a

**[38:52]** like purplish or pink. The pink one's a little bit smaller capacity. Um, it

**[38:55]** little bit smaller capacity. Um, it

**[38:55]** little bit smaller capacity. Um, it basically doesn't do as well. At least

**[38:56]** basically doesn't do as well. At least

**[38:56]** basically doesn't do as well. At least when you're doing SFT, uh, Loro can

**[38:59]** when you're doing SFT, uh, Loro can

**[38:59]** when you're doing SFT, uh, Loro can learn a little bit less, but also if we


### [39:00 - 40:00]

**[39:02]** learn a little bit less, but also if we

**[39:02]** learn a little bit less, but also if we look at how much it's degrading, it

**[39:04]** look at how much it's degrading, it

**[39:04]** look at how much it's degrading, it forgets less. So this paper is called

**[39:06]** forgets less. So this paper is called

**[39:06]** forgets less. So this paper is called learns less and forgets less. And it's

**[39:10]** learns less and forgets less. And it's

**[39:10]** learns less and forgets less. And it's actually a very nice finding. So like if

**[39:12]** actually a very nice finding. So like if

**[39:12]** actually a very nice finding. So like if you want to at least teach a model via

**[39:14]** you want to at least teach a model via

**[39:14]** you want to at least teach a model via SFT and you use one of these low rank or

**[39:17]** SFT and you use one of these low rank or

**[39:17]** SFT and you use one of these low rank or parameter efficient methods like all the

**[39:19]** parameter efficient methods like all the

**[39:19]** parameter efficient methods like all the ones I described, they're going to make

**[39:20]** ones I described, they're going to make

**[39:20]** ones I described, they're going to make a small change to the model in a way

**[39:22]** a small change to the model in a way

**[39:22]** a small change to the model in a way that it's probably not going to be as

**[39:24]** that it's probably not going to be as

**[39:24]** that it's probably not going to be as expressive as full fine tuning, but it

**[39:25]** expressive as full fine tuning, but it

**[39:25]** expressive as full fine tuning, but it also doesn't destroy a lot of the

**[39:27]** also doesn't destroy a lot of the

**[39:27]** also doesn't destroy a lot of the knowledge. Um here's something going the

**[39:30]** knowledge. Um here's something going the

**[39:30]** knowledge. Um here's something going the exact opposite direction. This is the

**[39:31]** exact opposite direction. This is the

**[39:31]** exact opposite direction. This is the results from thinking machines showing

**[39:33]** results from thinking machines showing

**[39:33]** results from thinking machines showing that they think lower is about as good

**[39:35]** that they think lower is about as good

**[39:35]** that they think lower is about as good as full fine tuning, which is

**[39:37]** as full fine tuning, which is

**[39:37]** as full fine tuning, which is interesting because they're doing RL. So

**[39:40]** interesting because they're doing RL. So

**[39:40]** interesting because they're doing RL. So it's like maybe dependent on the

**[39:42]** it's like maybe dependent on the

**[39:42]** it's like maybe dependent on the training mechanism like if you do RL

**[39:44]** training mechanism like if you do RL

**[39:44]** training mechanism like if you do RL maybe it makes small updates and um you

**[39:47]** maybe it makes small updates and um you

**[39:47]** maybe it makes small updates and um you can do low you can do memory layers but

**[39:50]** can do low you can do memory layers but

**[39:50]** can do low you can do memory layers but for SFT it really has to store a lot of

**[39:52]** for SFT it really has to store a lot of

**[39:52]** for SFT it really has to store a lot of information so you really have to do

**[39:53]** information so you really have to do

**[39:53]** information so you really have to do full fine tuning. I think that's the

**[39:55]** full fine tuning. I think that's the

**[39:55]** full fine tuning. I think that's the takeaway I have and I have some actually

**[39:57]** takeaway I have and I have some actually

**[39:57]** takeaway I have and I have some actually a paper that's like kind of blocked for

**[39:59]** a paper that's like kind of blocked for

**[39:59]** a paper that's like kind of blocked for legal reasons but coming out soon. Um


### [40:00 - 41:00]

**[40:02]** legal reasons but coming out soon. Um

**[40:02]** legal reasons but coming out soon. Um here's one result from my paper that's

**[40:04]** here's one result from my paper that's

**[40:04]** here's one result from my paper that's relevant to this. So we have this like

**[40:06]** relevant to this. So we have this like

**[40:06]** relevant to this. So we have this like tiny Lora thing that's even smaller than

**[40:08]** tiny Lora thing that's even smaller than

**[40:08]** tiny Lora thing that's even smaller than Lorra. Well there's actually Lorra XS

**[40:11]** Lorra. Well there's actually Lorra XS

**[40:11]** Lorra. Well there's actually Lorra XS which already exists and then we made

**[40:12]** which already exists and then we made

**[40:12]** which already exists and then we made tiny Lora which is even smaller. And if

**[40:14]** tiny Lora which is even smaller. And if

**[40:14]** tiny Lora which is even smaller. And if you're doing RL on GSMK

**[40:17]** you're doing RL on GSMK

**[40:17]** you're doing RL on GSMK math [clears throat] reasoning you can

**[40:18]** math [clears throat] reasoning you can

**[40:18]** math [clears throat] reasoning you can train 14 parameters and get like 91%

**[40:23]** train 14 parameters and get like 91%

**[40:23]** train 14 parameters and get like 91% accuracy which is pretty crazy. I think

**[40:26]** accuracy which is pretty crazy. I think

**[40:26]** accuracy which is pretty crazy. I think um there's like a lot of reasons for

**[40:28]** um there's like a lot of reasons for

**[40:28]** um there's like a lot of reasons for this. Like RL makes really tiny changes.

**[40:30]** this. Like RL makes really tiny changes.

**[40:30]** this. Like RL makes really tiny changes. I think this Quen model like is

**[40:32]** I think this Quen model like is

**[40:32]** I think this Quen model like is something fishy is going on with the

**[40:34]** something fishy is going on with the

**[40:34]** something fishy is going on with the training data.

**[40:35]** training data.

**[40:35]** training data. >> You have a one parameter experiment.

**[40:38]** >> You have a one parameter experiment.

**[40:38]** >> You have a one parameter experiment. >> Oh yeah, one parameter. It actually

**[40:40]** >> Oh yeah, one parameter. It actually

**[40:40]** >> Oh yeah, one parameter. It actually learns it gets 5% better with one

**[40:43]** learns it gets 5% better with one

**[40:43]** learns it gets 5% better with one parameter. [laughter]

**[40:45]** parameter. [laughter]

**[40:45]** parameter. [laughter] >> Pretty cool.

**[40:45]** >> Pretty cool.

**[40:45]** >> Pretty cool. >> It's amazing.

**[40:46]** >> It's amazing.

**[40:46]** >> It's amazing. >> Yeah. Yeah. It's it's it's really nice.

**[40:48]** >> Yeah. Yeah. It's it's it's really nice.

**[40:48]** >> Yeah. Yeah. It's it's it's really nice. I think um

**[40:50]** I think um

**[40:50]** I think um >> literally the smallest

**[40:52]** >> literally the smallest

**[40:52]** >> literally the smallest >> Yeah. Yeah. The smallest thing you could

**[40:53]** >> Yeah. Yeah. The smallest thing you could

**[40:53]** >> Yeah. Yeah. The smallest thing you could possibly train. It's more like you you

**[40:55]** possibly train. It's more like you you

**[40:56]** possibly train. It's more like you you generate a lot of random projections and

**[40:58]** generate a lot of random projections and

**[40:58]** generate a lot of random projections and then you control them all with one

**[40:59]** then you control them all with one

**[40:59]** then you control them all with one number if that makes sense. Like the


### [41:00 - 42:00]

**[41:02]** number if that makes sense. Like the

**[41:02]** number if that makes sense. Like the model actually changes a lot but the

**[41:03]** model actually changes a lot but the

**[41:04]** model actually changes a lot but the only thing you can actually train and

**[41:06]** only thing you can actually train and

**[41:06]** only thing you can actually train and store is the one parameter.

**[41:08]** store is the one parameter.

**[41:08]** store is the one parameter. Uh I tell you more about it later. Um

**[41:11]** Uh I tell you more about it later. Um

**[41:11]** Uh I tell you more about it later. Um but yeah, it's pretty cool. Um

**[41:14]** but yeah, it's pretty cool. Um

**[41:14]** but yeah, it's pretty cool. Um this is another result that's like kind

**[41:16]** this is another result that's like kind

**[41:16]** this is another result that's like kind of in the mix, but I'm not sure how to

**[41:18]** of in the mix, but I'm not sure how to

**[41:18]** of in the mix, but I'm not sure how to place it. So if you do the KV cache

**[41:20]** place it. So if you do the KV cache

**[41:20]** place it. So if you do the KV cache tuning or prefix tuning, this paper

**[41:22]** tuning or prefix tuning, this paper

**[41:22]** tuning or prefix tuning, this paper thinks prefix tuning works much better

**[41:24]** thinks prefix tuning works much better

**[41:24]** thinks prefix tuning works much better than LoRa. I met some people in Meta um

**[41:26]** than LoRa. I met some people in Meta um

**[41:26]** than LoRa. I met some people in Meta um when I used to be affiliated there that

**[41:28]** when I used to be affiliated there that

**[41:28]** when I used to be affiliated there that said that they think lower works much

**[41:30]** said that they think lower works much

**[41:30]** said that they think lower works much better than prefix tuning. So I really

**[41:31]** better than prefix tuning. So I really

**[41:31]** better than prefix tuning. So I really don't know, but I think like what it

**[41:34]** don't know, but I think like what it

**[41:34]** don't know, but I think like what it really will come down to is like when

**[41:35]** really will come down to is like when

**[41:36]** really will come down to is like when you do it at scale, what's like most

**[41:37]** you do it at scale, what's like most

**[41:37]** you do it at scale, what's like most efficient? And I'm not exactly sure, but

**[41:40]** efficient? And I'm not exactly sure, but

**[41:40]** efficient? And I'm not exactly sure, but I think prefix tuning is a pretty good

**[41:42]** I think prefix tuning is a pretty good

**[41:42]** I think prefix tuning is a pretty good candidate because like KV caches are so

**[41:45]** candidate because like KV caches are so

**[41:45]** candidate because like KV caches are so commonly used these days and like a lot

**[41:48]** commonly used these days and like a lot

**[41:48]** commonly used these days and like a lot of the system stuff is built around KV

**[41:50]** of the system stuff is built around KV

**[41:50]** of the system stuff is built around KV caches. I think a cool thing about

**[41:51]** caches. I think a cool thing about

**[41:52]** caches. I think a cool thing about thinking machines is like they're

**[41:53]** thinking machines is like they're

**[41:53]** thinking machines is like they're designing this entire organization

**[41:54]** designing this entire organization

**[41:54]** designing this entire organization around like scaling Laura which is

**[41:56]** around like scaling Laura which is

**[41:56]** around like scaling Laura which is awesome but it's not really possible in

**[41:58]** awesome but it's not really possible in

**[41:58]** awesome but it's not really possible in open source right now. Like there's not


### [42:00 - 43:00]

**[42:00]** open source right now. Like there's not

**[42:00]** open source right now. Like there's not kernels for training many Lauras at the

**[42:02]** kernels for training many Lauras at the

**[42:02]** kernels for training many Lauras at the same time. It's like very complex and

**[42:04]** same time. It's like very complex and

**[42:04]** same time. It's like very complex and you have to have a lot of people working

**[42:05]** you have to have a lot of people working

**[42:05]** you have to have a lot of people working on that. Prefix tuning on the other hand

**[42:06]** on that. Prefix tuning on the other hand

**[42:06]** on that. Prefix tuning on the other hand is like very well supported. Um and then

**[42:09]** is like very well supported. Um and then

**[42:09]** is like very well supported. Um and then finally I'll quickly talk about memory

**[42:11]** finally I'll quickly talk about memory

**[42:11]** finally I'll quickly talk about memory layers. This is another approach to

**[42:12]** layers. This is another approach to

**[42:12]** layers. This is another approach to injecting data into models which I think

**[42:14]** injecting data into models which I think

**[42:14]** injecting data into models which I think is good. This is like uh adding a expert

**[42:18]** is good. This is like uh adding a expert

**[42:18]** is good. This is like uh adding a expert to the MLP but the expert is just like

**[42:20]** to the MLP but the expert is just like

**[42:20]** to the MLP but the expert is just like this giant differentiable lookup table.

**[42:23]** this giant differentiable lookup table.

**[42:23]** this giant differentiable lookup table. So it's kind of not that important

**[42:26]** So it's kind of not that important

**[42:26]** So it's kind of not that important exactly how it works but it's like it's

**[42:28]** exactly how it works but it's like it's

**[42:28]** exactly how it works but it's like it's just a different way to inject

**[42:29]** just a different way to inject

**[42:29]** just a different way to inject information into models. The cool thing

**[42:31]** information into models. The cool thing

**[42:31]** information into models. The cool thing about memory layers is it's

**[42:32]** about memory layers is it's

**[42:32]** about memory layers is it's controllable. So in this work uh by

**[42:35]** controllable. So in this work uh by

**[42:35]** controllable. So in this work uh by Jesse Lynn from this year, they specify

**[42:39]** Jesse Lynn from this year, they specify

**[42:39]** Jesse Lynn from this year, they specify exactly which parts of the memory layer

**[42:41]** exactly which parts of the memory layer

**[42:41]** exactly which parts of the memory layer get updated and keep it to like a very

**[42:43]** get updated and keep it to like a very

**[42:43]** get updated and keep it to like a very small number. And so their result shows

**[42:46]** small number. And so their result shows

**[42:46]** small number. And so their result shows that memory layers actually work the

**[42:48]** that memory layers actually work the

**[42:48]** that memory layers actually work the best. So memory the axes here are

**[42:51]** best. So memory the axes here are

**[42:52]** best. So memory the axes here are forgetting so down is bad and learning

**[42:54]** forgetting so down is bad and learning

**[42:54]** forgetting so down is bad and learning right is good. So the memory layers

**[42:57]** right is good. So the memory layers

**[42:57]** right is good. So the memory layers basically don't forget at all and they

**[42:59]** basically don't forget at all and they

**[42:59]** basically don't forget at all and they learn close to as much. So I think if


### [43:00 - 44:00]

**[43:02]** learn close to as much. So I think if

**[43:02]** learn close to as much. So I think if you're trying to inject information into

**[43:05]** you're trying to inject information into

**[43:05]** you're trying to inject information into models that you really care about them

**[43:07]** models that you really care about them

**[43:07]** models that you really care about them not forgetting any of their base

**[43:08]** not forgetting any of their base

**[43:08]** not forgetting any of their base information, maybe memory layers are the

**[43:10]** information, maybe memory layers are the

**[43:10]** information, maybe memory layers are the way to go. I think honestly there's a

**[43:12]** way to go. I think honestly there's a

**[43:12]** way to go. I think honestly there's a lot of conflicting evidence right now.

**[43:13]** lot of conflicting evidence right now.

**[43:13]** lot of conflicting evidence right now. Like some people think lower is good,

**[43:15]** Like some people think lower is good,

**[43:15]** Like some people think lower is good, some people think prefix tuning is good.

**[43:16]** some people think prefix tuning is good.

**[43:16]** some people think prefix tuning is good. These people think memory layers is

**[43:18]** These people think memory layers is

**[43:18]** These people think memory layers is good. I really am not sure, but I think

**[43:21]** good. I really am not sure, but I think

**[43:21]** good. I really am not sure, but I think it's going to be one of them.

**[43:23]** it's going to be one of them.

**[43:23]** it's going to be one of them. Okay, cool. That's that's the end of the

**[43:25]** Okay, cool. That's that's the end of the

**[43:25]** Okay, cool. That's that's the end of the training stuff into weights part. Maybe

**[43:27]** training stuff into weights part. Maybe

**[43:27]** training stuff into weights part. Maybe actually I'll stop and see if anyone has

**[43:29]** actually I'll stop and see if anyone has

**[43:29]** actually I'll stop and see if anyone has any questions about the different

**[43:30]** any questions about the different

**[43:30]** any questions about the different parameterizations. Yeah.

**[43:42]** >> Oh, yeah. Yeah. Yeah. From from my yet

**[43:42]** >> Oh, yeah. Yeah. Yeah. From from my yet unreleased research.

**[43:44]** unreleased research.

**[43:44]** unreleased research. >> So, have you used SFT before?

**[43:47]** >> So, have you used SFT before?

**[43:47]** >> So, have you used SFT before? >> Yeah. Yeah. I can show you the SFT

**[43:49]** >> Yeah. Yeah. I can show you the SFT

**[43:49]** >> Yeah. Yeah. I can show you the SFT results later. But SFT uh

**[43:53]** results later. But SFT uh

**[43:53]** results later. But SFT uh takes a lot more parameters in the short

**[43:55]** takes a lot more parameters in the short

**[43:55]** takes a lot more parameters in the short explanation like many many more like a

**[43:57]** explanation like many many more like a

**[43:57]** explanation like many many more like a thousand x1 or something. And you


### [44:00 - 45:00]

**[44:00]** thousand x1 or something. And you

**[44:00]** thousand x1 or something. And you attribute that to the sparcity of the

**[44:01]** attribute that to the sparcity of the

**[44:01]** attribute that to the sparcity of the reward.

**[44:02]** reward.

**[44:02]** reward. >> Yeah. Yeah. I think it's something like

**[44:04]** >> Yeah. Yeah. I think it's something like

**[44:04]** >> Yeah. Yeah. I think it's something like that. Like the SMT learning signal is

**[44:06]** that. Like the SMT learning signal is

**[44:06]** that. Like the SMT learning signal is like cross entropy on all of the tokens

**[44:09]** like cross entropy on all of the tokens

**[44:09]** like cross entropy on all of the tokens with or without thinking tokens. And

**[44:11]** with or without thinking tokens. And

**[44:11]** with or without thinking tokens. And that's a lot of bits essentially. And

**[44:13]** that's a lot of bits essentially. And

**[44:13]** that's a lot of bits essentially. And then RL just gives you a one or a zero.

**[44:16]** then RL just gives you a one or a zero.

**[44:16]** then RL just gives you a one or a zero. If you get it right and you already

**[44:17]** If you get it right and you already

**[44:17]** If you get it right and you already knew, then it's no information. If you

**[44:20]** knew, then it's no information. If you

**[44:20]** knew, then it's no information. If you get it wrong, you get like one bit. So I

**[44:22]** get it wrong, you get like one bit. So I

**[44:22]** get it wrong, you get like one bit. So I think because RL is like so sparse and

**[44:25]** think because RL is like so sparse and

**[44:25]** think because RL is like so sparse and uh information efficient, then you can

**[44:26]** uh information efficient, then you can

**[44:26]** uh information efficient, then you can do it with way fewer parameters. That's

**[44:28]** do it with way fewer parameters. That's

**[44:28]** do it with way fewer parameters. That's that's kind of the take away from our

**[44:30]** that's kind of the take away from our

**[44:30]** that's kind of the take away from our paper actually.

**[44:30]** paper actually.

**[44:30]** paper actually. >> So you didn't do GRPO after doing SF?

**[44:34]** >> So you didn't do GRPO after doing SF?

**[44:34]** >> So you didn't do GRPO after doing SF? >> No, no SFT. We just either do GRPO or

**[44:37]** >> No, no SFT. We just either do GRPO or

**[44:37]** >> No, no SFT. We just either do GRPO or SFT and then we see like kind of how

**[44:39]** SFT and then we see like kind of how

**[44:39]** SFT and then we see like kind of how many parameters you need to train to get

**[44:41]** many parameters you need to train to get

**[44:42]** many parameters you need to train to get to equivalent performance and SFT

**[44:44]** to equivalent performance and SFT

**[44:44]** to equivalent performance and SFT requires many more parameters.

**[44:48]** requires many more parameters.

**[44:48]** requires many more parameters. >> Uh so here you are comparing like uh

**[44:51]** >> Uh so here you are comparing like uh

**[44:51]** >> Uh so here you are comparing like uh training versus rag like we are being we

**[44:54]** training versus rag like we are being we

**[44:54]** training versus rag like we are being we want to solve the problem what we are

**[44:56]** want to solve the problem what we are

**[44:56]** want to solve the problem what we are facing in the rack. So is the volume of

**[44:58]** facing in the rack. So is the volume of

**[44:58]** facing in the rack. So is the volume of the document also matter like you have


### [45:00 - 46:00]

**[45:00]** the document also matter like you have

**[45:00]** the document also matter like you have any studies like uh because if if some

**[45:03]** any studies like uh because if if some

**[45:03]** any studies like uh because if if some problem has a less number of document

**[45:06]** problem has a less number of document

**[45:06]** problem has a less number of document uh rag will be better or the uh training

**[45:10]** uh rag will be better or the uh training

**[45:10]** uh rag will be better or the uh training will be better.

**[45:11]** will be better.

**[45:11]** will be better. >> That's a really good point. Um maybe

**[45:13]** >> That's a really good point. Um maybe

**[45:13]** >> That's a really good point. Um maybe that let's uh go to the last slide. So I

**[45:17]** that let's uh go to the last slide. So I

**[45:17]** that let's uh go to the last slide. So I think the question is like okay you're

**[45:19]** think the question is like okay you're

**[45:19]** think the question is like okay you're trying to train all of your data into a

**[45:21]** trying to train all of your data into a

**[45:21]** trying to train all of your data into a model but something only happens once.

**[45:23]** model but something only happens once.

**[45:23]** model but something only happens once. Yeah, means when when I should pick

**[45:26]** Yeah, means when when I should pick

**[45:26]** Yeah, means when when I should pick focus on drag and when I should focus on

**[45:28]** focus on drag and when I should focus on

**[45:28]** focus on drag and when I should focus on like uh like a training fix because

**[45:31]** like uh like a training fix because

**[45:31]** like uh like a training fix because every time mean I have like a small set

**[45:33]** every time mean I have like a small set

**[45:33]** every time mean I have like a small set of documents the training might not be

**[45:36]** of documents the training might not be

**[45:36]** of documents the training might not be feasible.

**[45:37]** feasible.

**[45:37]** feasible. >> Yes. Yes. Like it your like maybe you

**[45:41]** >> Yes. Yes. Like it your like maybe you

**[45:41]** >> Yes. Yes. Like it your like maybe you something is so under represented in

**[45:43]** something is so under represented in

**[45:43]** something is so under represented in your data that it probably wouldn't

**[45:45]** your data that it probably wouldn't

**[45:45]** your data that it probably wouldn't >> data is frequently changing might be

**[45:47]** >> data is frequently changing might be

**[45:47]** >> data is frequently changing might be >> your data is changing a lot. Yeah. Maybe

**[45:49]** >> your data is changing a lot. Yeah. Maybe

**[45:49]** >> your data is changing a lot. Yeah. Maybe in the short term it's hard to train. Um

**[45:52]** in the short term it's hard to train. Um

**[45:52]** in the short term it's hard to train. Um yeah. So, let me point out like okay, so

**[45:55]** yeah. So, let me point out like okay, so

**[45:55]** yeah. So, let me point out like okay, so obviously we're always going to put

**[45:56]** obviously we're always going to put

**[45:56]** obviously we're always going to put stuff into context and I think we'll


### [46:00 - 47:00]

**[46:00]** stuff into context and I think we'll

**[46:00]** stuff into context and I think we'll also probably always do rag. Like I

**[46:02]** also probably always do rag. Like I

**[46:02]** also probably always do rag. Like I think um there's basically no scenario

**[46:06]** think um there's basically no scenario

**[46:06]** think um there's basically no scenario that you can imagine for a long time

**[46:08]** that you can imagine for a long time

**[46:08]** that you can imagine for a long time where you're just like always training

**[46:09]** where you're just like always training

**[46:09]** where you're just like always training the model and never doing rag. I think

**[46:11]** the model and never doing rag. I think

**[46:11]** the model and never doing rag. I think you'll do both. I think like maybe if

**[46:13]** you'll do both. I think like maybe if

**[46:13]** you'll do both. I think like maybe if you have a ton of documents, I don't

**[46:15]** you have a ton of documents, I don't

**[46:15]** you have a ton of documents, I don't know, maybe every day you do this big

**[46:17]** know, maybe every day you do this big

**[46:17]** know, maybe every day you do this big training and then every time you serve

**[46:18]** training and then every time you serve

**[46:18]** training and then every time you serve you also do rag. And so like what I

**[46:21]** you also do rag. And so like what I

**[46:21]** you also do rag. And so like what I really imagine is like or maybe my my

**[46:24]** really imagine is like or maybe my my

**[46:24]** really imagine is like or maybe my my point is that no one is doing this right

**[46:26]** point is that no one is doing this right

**[46:26]** point is that no one is doing this right now and like people will start doing

**[46:28]** now and like people will start doing

**[46:28]** now and like people will start doing that.

**[46:28]** that.

**[46:28]** that. >> You have any like a projection like

**[46:30]** >> You have any like a projection like

**[46:30]** >> You have any like a projection like after certain amount of data like

**[46:32]** after certain amount of data like

**[46:32]** after certain amount of data like training will be like a more [cough]

**[46:34]** training will be like a more [cough]

**[46:34]** training will be like a more [cough] efficient and direct like yeah

**[46:38]** efficient and direct like yeah

**[46:38]** efficient and direct like yeah uh no like I think I think this kind of

**[46:40]** uh no like I think I think this kind of

**[46:40]** uh no like I think I think this kind of thing is really new so there's a lot of

**[46:42]** thing is really new so there's a lot of

**[46:42]** thing is really new so there's a lot of room for analysis like that. I would

**[46:43]** room for analysis like that. I would

**[46:43]** room for analysis like that. I would definitely be interested to see both

**[46:46]** definitely be interested to see both

**[46:46]** definitely be interested to see both analysis on how the frequency of

**[46:48]** analysis on how the frequency of

**[46:48]** analysis on how the frequency of information affects like the trade-off

**[46:50]** information affects like the trade-off

**[46:50]** information affects like the trade-off and how just like how much data you have

**[46:52]** and how just like how much data you have

**[46:52]** and how just like how much data you have to have for training to become

**[46:54]** to have for training to become

**[46:54]** to have for training to become economically feasible. That's a really

**[46:55]** economically feasible. That's a really

**[46:55]** economically feasible. That's a really good question.

**[46:57]** good question.

**[46:57]** good question. >> Yeah. Um, is your suggestion kind of in


### [47:00 - 48:00]

**[47:02]** >> Yeah. Um, is your suggestion kind of in

**[47:02]** >> Yeah. Um, is your suggestion kind of in uh diving more into like the weights

**[47:04]** uh diving more into like the weights

**[47:04]** uh diving more into like the weights side of uh the presentation to use a

**[47:07]** side of uh the presentation to use a

**[47:07]** side of uh the presentation to use a fine-tuned model for like completion

**[47:10]** fine-tuned model for like completion

**[47:10]** fine-tuned model for like completion type tasks or also for embeddings?

**[47:14]** type tasks or also for embeddings?

**[47:14]** type tasks or also for embeddings? >> Oh yeah, that's a good question. Um, no,

**[47:17]** >> Oh yeah, that's a good question. Um, no,

**[47:17]** >> Oh yeah, that's a good question. Um, no, I think I think the fine-tuning I'm

**[47:19]** I think I think the fine-tuning I'm

**[47:20]** I think I think the fine-tuning I'm talking about is all for like assistant

**[47:21]** talking about is all for like assistant

**[47:21]** talking about is all for like assistant engine completion. Um, it's an

**[47:24]** engine completion. Um, it's an

**[47:24]** engine completion. Um, it's an interesting question. You probably could

**[47:25]** interesting question. You probably could

**[47:25]** interesting question. You probably could do like dynamic embedding model

**[47:27]** do like dynamic embedding model

**[47:27]** do like dynamic embedding model training, but I guess like the way I

**[47:29]** training, but I guess like the way I

**[47:29]** training, but I guess like the way I think about it is like the real like 10x

**[47:32]** think about it is like the real like 10x

**[47:32]** think about it is like the real like 10x improvement here is going to come from

**[47:33]** improvement here is going to come from

**[47:33]** improvement here is going to come from training to weights. You could maybe

**[47:35]** training to weights. You could maybe

**[47:35]** training to weights. You could maybe make rag like 2x better if you really

**[47:38]** make rag like 2x better if you really

**[47:38]** make rag like 2x better if you really really worked, but I think there's so

**[47:39]** really worked, but I think there's so

**[47:40]** really worked, but I think there's so many fundamental problems with it that I

**[47:42]** many fundamental problems with it that I

**[47:42]** many fundamental problems with it that I wouldn't spend that much time on making

**[47:44]** wouldn't spend that much time on making

**[47:44]** wouldn't spend that much time on making it better.

**[47:46]** it better.

**[47:46]** it better. What were what do you feel like the most

**[47:49]** What were what do you feel like the most

**[47:49]** What were what do you feel like the most fundamental problem is where even if

**[47:51]** fundamental problem is where even if

**[47:51]** fundamental problem is where even if like your retrieval was fantastic, you

**[47:53]** like your retrieval was fantastic, you

**[47:53]** like your retrieval was fantastic, you still

**[47:53]** still

**[47:53]** still >> kind of I think like chunking like um

**[47:55]** >> kind of I think like chunking like um

**[47:55]** >> kind of I think like chunking like um yeah,

**[47:55]** yeah,

**[47:56]** yeah, >> you just like kind of retrieve some of

**[47:57]** >> you just like kind of retrieve some of

**[47:57]** >> you just like kind of retrieve some of the stuff you need and then you can't

**[47:59]** the stuff you need and then you can't

**[47:59]** the stuff you need and then you can't really reason across all of it. And like


### [48:00 - 49:00]

**[48:01]** really reason across all of it. And like

**[48:01]** really reason across all of it. And like I think in the limit like there's some

**[48:04]** I think in the limit like there's some

**[48:04]** I think in the limit like there's some types of data where like no matter how

**[48:06]** types of data where like no matter how

**[48:06]** types of data where like no matter how you chunk, you'll never get like

**[48:07]** you chunk, you'll never get like

**[48:07]** you chunk, you'll never get like everything you need if that makes sense.

**[48:09]** everything you need if that makes sense.

**[48:09]** everything you need if that makes sense. >> Yeah, totally.

**[48:10]** >> Yeah, totally.

**[48:10]** >> Yeah, totally. >> Cool. Yeah. Do you see any fundamental

**[48:13]** >> Cool. Yeah. Do you see any fundamental

**[48:13]** >> Cool. Yeah. Do you see any fundamental limitations as you scale up the amount

**[48:15]** limitations as you scale up the amount

**[48:15]** limitations as you scale up the amount of personalization you need? Let's say

**[48:17]** of personalization you need? Let's say

**[48:17]** of personalization you need? Let's say you had a B toC product that had 100

**[48:19]** you had a B toC product that had 100

**[48:19]** you had a B toC product that had 100 million or 10 million users memory for

**[48:21]** million or 10 million users memory for

**[48:21]** million or 10 million users memory for all of those.

**[48:22]** all of those.

**[48:22]** all of those. >> Do you think that's just not feasible?

**[48:24]** >> Do you think that's just not feasible?

**[48:24]** >> Do you think that's just not feasible? >> You say 10 million users.

**[48:25]** >> You say 10 million users.

**[48:25]** >> You say 10 million users. >> Yeah. 10 million 100 billion is more

**[48:27]** >> Yeah. 10 million 100 billion is more

**[48:27]** >> Yeah. 10 million 100 billion is more than that.

**[48:27]** than that.

**[48:27]** than that. >> Yeah. Um no, no, I actually think it is

**[48:30]** >> Yeah. Um no, no, I actually think it is

**[48:30]** >> Yeah. Um no, no, I actually think it is it is feasible. Like Laura, maybe you

**[48:33]** it is feasible. Like Laura, maybe you

**[48:33]** it is feasible. Like Laura, maybe you train a few megabytes per user or

**[48:37]** train a few megabytes per user or

**[48:37]** train a few megabytes per user or something. It's not that crazy, right?

**[48:38]** something. It's not that crazy, right?

**[48:38]** something. It's not that crazy, right? Like YouTube probably has gigabytes per

**[48:41]** Like YouTube probably has gigabytes per

**[48:41]** Like YouTube probably has gigabytes per multiple times,

**[48:43]** multiple times,

**[48:43]** multiple times, >> right? That's a good [clears throat]

**[48:43]** >> right? That's a good [clears throat]

**[48:44]** >> right? That's a good [clears throat] point. Like the continual updates are

**[48:45]** point. Like the continual updates are

**[48:45]** point. Like the continual updates are hard. Like probably in realistic short

**[48:47]** hard. Like probably in realistic short

**[48:47]** hard. Like probably in realistic short term, it's more like you update once a

**[48:49]** term, it's more like you update once a

**[48:49]** term, it's more like you update once a day or something like that. But I think

**[48:50]** day or something like that. But I think

**[48:50]** day or something like that. But I think that's that's doable. But you make a

**[48:53]** that's that's doable. But you make a

**[48:53]** that's that's doable. But you make a good point that the paradigm I'm

**[48:54]** good point that the paradigm I'm

**[48:54]** good point that the paradigm I'm describing is much more expensive.

**[48:57]** describing is much more expensive.

**[48:57]** describing is much more expensive. >> Also, you do consider there's a lot more

**[48:58]** >> Also, you do consider there's a lot more

**[48:58]** >> Also, you do consider there's a lot more that you can do in the other two


### [49:00 - 50:00]

**[49:00]** that you can do in the other two

**[49:00]** that you can do in the other two buckets. You compress the data context.

**[49:02]** buckets. You compress the data context.

**[49:02]** buckets. You compress the data context. You compress it before you put rag. You

**[49:04]** You compress it before you put rag. You

**[49:04]** You compress it before you put rag. You break it up into other buckets. You

**[49:06]** break it up into other buckets. You

**[49:06]** break it up into other buckets. You don't just have to use rags and use SQL

**[49:08]** don't just have to use rags and use SQL

**[49:08]** don't just have to use rags and use SQL and knowledge to all of them together in

**[49:11]** and knowledge to all of them together in

**[49:11]** and knowledge to all of them together in different buckets and that solves a lot

**[49:12]** different buckets and that solves a lot

**[49:12]** different buckets and that solves a lot of problems.

**[49:13]** of problems.

**[49:13]** of problems. >> Yeah. Yeah, that's a good point. There's

**[49:14]** >> Yeah. Yeah, that's a good point. There's

**[49:14]** >> Yeah. Yeah, that's a good point. There's kind of like three axes of optimization

**[49:16]** kind of like three axes of optimization

**[49:16]** kind of like three axes of optimization here. And I guess like we are we're

**[49:20]** here. And I guess like we are we're

**[49:20]** here. And I guess like we are we're getting pretty good at this. We're okay

**[49:22]** getting pretty good at this. We're okay

**[49:22]** getting pretty good at this. We're okay at this and we're horrible at this. And

**[49:23]** at this and we're horrible at this. And

**[49:23]** at this and we're horrible at this. And so like we'll continue improving upon

**[49:26]** so like we'll continue improving upon

**[49:26]** so like we'll continue improving upon all three axes.

**[49:27]** all three axes.

**[49:28]** all three axes. >> Yeah. What's your uh like I'm kind of

**[49:31]** >> Yeah. What's your uh like I'm kind of

**[49:31]** >> Yeah. What's your uh like I'm kind of hearing that maybe it's not defined yet,

**[49:33]** hearing that maybe it's not defined yet,

**[49:33]** hearing that maybe it's not defined yet, but what's your kind of like intuition

**[49:35]** but what's your kind of like intuition

**[49:35]** but what's your kind of like intuition or guess in terms of like where the

**[49:37]** or guess in terms of like where the

**[49:37]** or guess in terms of like where the decision boundary is in terms of

**[49:39]** decision boundary is in terms of

**[49:39]** decision boundary is in terms of investing your effort in those

**[49:41]** investing your effort in those

**[49:41]** investing your effort in those optimizations particularly in like let's

**[49:43]** optimizations particularly in like let's

**[49:43]** optimizations particularly in like let's say a couple of years where you could do

**[49:45]** say a couple of years where you could do

**[49:45]** say a couple of years where you could do something like a deep research but it

**[49:47]** something like a deep research but it

**[49:47]** something like a deep research but it would be way cheaper and way faster. Um

**[49:49]** would be way cheaper and way faster. Um

**[49:49]** would be way cheaper and way faster. Um when what are there

**[49:52]** when what are there

**[49:52]** when what are there you were saying that there isn't like a

**[49:54]** you were saying that there isn't like a

**[49:54]** you were saying that there isn't like a number of documents but what is the

**[49:56]** number of documents but what is the

**[49:56]** number of documents but what is the boundary that you would think about

**[49:57]** boundary that you would think about

**[49:58]** boundary that you would think about looking at is it the freshness of the


### [50:00 - 51:00]

**[50:00]** looking at is it the freshness of the

**[50:00]** looking at is it the freshness of the data how fast changing is the number of

**[50:02]** data how fast changing is the number of

**[50:02]** data how fast changing is the number of documents there what's your

**[50:04]** documents there what's your

**[50:04]** documents there what's your >> yeah I it's a really good question I I

**[50:07]** >> yeah I it's a really good question I I

**[50:07]** >> yeah I it's a really good question I I think um I think the paradigm I'm

**[50:10]** think um I think the paradigm I'm

**[50:10]** think um I think the paradigm I'm describing is especially effective when

**[50:11]** describing is especially effective when

**[50:11]** describing is especially effective when you have like a large amount of data

**[50:13]** you have like a large amount of data

**[50:13]** you have like a large amount of data that's not been indexed into the LLM at

**[50:15]** that's not been indexed into the LLM at

**[50:15]** that's not been indexed into the LLM at all and it gives you a big benefit there

**[50:17]** all and it gives you a big benefit there

**[50:17]** all and it gives you a big benefit there I think when you start seeing seeing

**[50:19]** I think when you start seeing seeing

**[50:19]** I think when you start seeing seeing like sparser updates to your data set or

**[50:22]** like sparser updates to your data set or

**[50:22]** like sparser updates to your data set or like some new data comes in but it's not

**[50:24]** like some new data comes in but it's not

**[50:24]** like some new data comes in but it's not that much and it's like fairly often

**[50:26]** that much and it's like fairly often

**[50:26]** that much and it's like fairly often then you probably want to turn to

**[50:27]** then you probably want to turn to

**[50:27]** then you probably want to turn to inference time approaches that are

**[50:28]** inference time approaches that are

**[50:28]** inference time approaches that are closer to deep research.

**[50:31]** closer to deep research.

**[50:31]** closer to deep research. Um yeah that guy had a question on

**[50:34]** Um yeah that guy had a question on

**[50:34]** Um yeah that guy had a question on >> yeah can you elaborate a little bit more

**[50:36]** >> yeah can you elaborate a little bit more

**[50:36]** >> yeah can you elaborate a little bit more about the synthetic data generation so

**[50:39]** about the synthetic data generation so

**[50:39]** about the synthetic data generation so let's say that you have YouTube to talk

**[50:45]** let's say that you have YouTube to talk

**[50:45]** let's say that you have YouTube to talk similar language terminology like

**[50:48]** similar language terminology like

**[50:48]** similar language terminology like proprietary data right like millions of

**[50:51]** proprietary data right like millions of

**[50:52]** proprietary data right like millions of documents like how is synthetic data

**[50:55]** documents like how is synthetic data

**[50:55]** documents like how is synthetic data generation that context helpful


### [51:00 - 52:00]

**[51:01]** >> so you're company has millions of

**[51:02]** >> so you're company has millions of documents you said and you want the

**[51:03]** documents you said and you want the

**[51:03]** documents you said and you want the model to

**[51:04]** model to

**[51:04]** model to >> it's more like a scenario.

**[51:05]** >> it's more like a scenario.

**[51:05]** >> it's more like a scenario. >> Yeah. Yeah. Okay.

**[51:06]** >> Yeah. Yeah. Okay.

**[51:06]** >> Yeah. Yeah. Okay. >> Yeah. Yeah. Yeah. Um

**[51:07]** >> Yeah. Yeah. Yeah. Um

**[51:07]** >> Yeah. Yeah. Yeah. Um >> because it wouldn't you said you

**[51:10]** >> because it wouldn't you said you

**[51:10]** >> because it wouldn't you said you wouldn't just train the mix work, right?

**[51:13]** wouldn't just train the mix work, right?

**[51:13]** wouldn't just train the mix work, right? >> Yeah.

**[51:15]** >> Yeah.

**[51:15]** >> Yeah. Try out different such and I think one

**[51:17]** Try out different such and I think one

**[51:17]** Try out different such and I think one of the you talk about synthetic data.

**[51:21]** of the you talk about synthetic data.

**[51:21]** of the you talk about synthetic data. >> Yeah. Yeah. No, I think I think

**[51:23]** >> Yeah. Yeah. No, I think I think

**[51:23]** >> Yeah. Yeah. No, I think I think synthetic data generation could work for

**[51:25]** synthetic data generation could work for

**[51:25]** synthetic data generation could work for that problem. So I guess like um it

**[51:31]** that problem. So I guess like um it

**[51:31]** that problem. So I guess like um it depends on how information dense your

**[51:32]** depends on how information dense your

**[51:32]** depends on how information dense your data is. If you have millions of

**[51:34]** data is. If you have millions of

**[51:34]** data is. If you have millions of documents from your company, I would

**[51:35]** documents from your company, I would

**[51:36]** documents from your company, I would guess many of them share formatting and

**[51:38]** guess many of them share formatting and

**[51:38]** guess many of them share formatting and only contribute maybe like a few bits of

**[51:41]** only contribute maybe like a few bits of

**[51:41]** only contribute maybe like a few bits of kind of global information to the data

**[51:43]** kind of global information to the data

**[51:43]** kind of global information to the data set. And so what you want to think about

**[51:45]** set. And so what you want to think about

**[51:45]** set. And so what you want to think about is like does there exist a function that

**[51:47]** is like does there exist a function that

**[51:47]** is like does there exist a function that could produce a good training data set

**[51:49]** could produce a good training data set

**[51:49]** could produce a good training data set for an LLM that would teach it about my

**[51:51]** for an LLM that would teach it about my

**[51:51]** for an LLM that would teach it about my data? And like there probably is. Like

**[51:53]** data? And like there probably is. Like

**[51:53]** data? And like there probably is. Like you could probably design some strategy

**[51:54]** you could probably design some strategy

**[51:54]** you could probably design some strategy that looks at the documents, kind of

**[51:56]** that looks at the documents, kind of

**[51:56]** that looks at the documents, kind of like figures out what's new about each

**[51:58]** like figures out what's new about each

**[51:58]** like figures out what's new about each document and creates like kind of

**[51:59]** document and creates like kind of

**[51:59]** document and creates like kind of question answer pairs, but this is very


### [52:00 - 53:00]

**[52:02]** question answer pairs, but this is very

**[52:02]** question answer pairs, but this is very blue sky. Like I think a lot of people

**[52:03]** blue sky. Like I think a lot of people

**[52:03]** blue sky. Like I think a lot of people are working on this right now, but I

**[52:05]** are working on this right now, but I

**[52:05]** are working on this right now, but I don't have like a a global answer of how

**[52:09]** don't have like a a global answer of how

**[52:09]** don't have like a a global answer of how to actually

**[52:09]** to actually

**[52:09]** to actually >> right now my only solution that I can

**[52:11]** >> right now my only solution that I can

**[52:11]** >> right now my only solution that I can think of is um you know getting to

**[52:14]** think of is um you know getting to

**[52:14]** think of is um you know getting to generate that Q&A,

**[52:17]** generate that Q&A,

**[52:17]** generate that Q&A, >> right?

**[52:26]** Yeah. Yeah. I think it also depends on

**[52:26]** Yeah. Yeah. I think it also depends on what types of questions you'll be asking

**[52:28]** what types of questions you'll be asking

**[52:28]** what types of questions you'll be asking about the documents. Like what you

**[52:29]** about the documents. Like what you

**[52:29]** about the documents. Like what you really want to model is like all

**[52:30]** really want to model is like all

**[52:30]** really want to model is like all possible questions or something like

**[52:32]** possible questions or something like

**[52:32]** possible questions or something like that, but I think Q&A gets you pretty

**[52:34]** that, but I think Q&A gets you pretty

**[52:34]** that, but I think Q&A gets you pretty far.

**[52:37]** far.

**[52:37]** far. >> Cool.

**[52:37]** >> Cool.

**[52:37]** >> Cool. >> Yeah. Um so with with this approach

**[52:40]** >> Yeah. Um so with with this approach

**[52:40]** >> Yeah. Um so with with this approach right you you you mentioned this example

**[52:42]** right you you you mentioned this example

**[52:42]** right you you you mentioned this example where you're um uh you would train your

**[52:46]** where you're um uh you would train your

**[52:46]** where you're um uh you would train your model right on 3M uh quarterly earnings

**[52:50]** model right on 3M uh quarterly earnings

**[52:50]** model right on 3M uh quarterly earnings right uh I think 10 10k 10q um documents

**[52:54]** right uh I think 10 10k 10q um documents

**[52:54]** right uh I think 10 10k 10q um documents what would like

**[52:56]** what would like

**[52:56]** what would like what would the prompt basically look

**[52:58]** what would the prompt basically look

**[52:58]** what would the prompt basically look like right like is there is there


### [53:00 - 54:00]

**[53:00]** like right like is there is there

**[53:00]** like right like is there is there anything in within like the in context

**[53:03]** anything in within like the in context

**[53:03]** anything in within like the in context learning that would still need to be

**[53:05]** learning that would still need to be

**[53:05]** learning that would still need to be kind of specified to

**[53:09]** kind of specified to

**[53:09]** kind of specified to bring your data into a context.

**[53:12]** bring your data into a context.

**[53:12]** bring your data into a context. >> Yeah. Uh so I think the question was if

**[53:14]** >> Yeah. Uh so I think the question was if

**[53:14]** >> Yeah. Uh so I think the question was if you start with the 3M example we had and

**[53:17]** you start with the 3M example we had and

**[53:17]** you start with the 3M example we had and you train all that into a model using

**[53:19]** you train all that into a model using

**[53:19]** you train all that into a model using some like magic synthetic data, what

**[53:20]** some like magic synthetic data, what

**[53:20]** some like magic synthetic data, what does actually the prompt look like?

**[53:21]** does actually the prompt look like?

**[53:21]** does actually the prompt look like? >> Yeah.

**[53:22]** >> Yeah.

**[53:22]** >> Yeah. >> I think actually if you do it right, you

**[53:23]** >> I think actually if you do it right, you

**[53:23]** >> I think actually if you do it right, you don't need a prompt at all like you can

**[53:25]** don't need a prompt at all like you can

**[53:25]** don't need a prompt at all like you can just ask the model a question. No system

**[53:26]** just ask the model a question. No system

**[53:26]** just ask the model a question. No system prompt, no

**[53:29]** prompt, no

**[53:29]** prompt, no extra information and if nothing has

**[53:31]** extra information and if nothing has

**[53:31]** extra information and if nothing has changed, it should know everything. like

**[53:33]** changed, it should know everything. like

**[53:33]** changed, it should know everything. like and you even there's some scenarios

**[53:34]** and you even there's some scenarios

**[53:34]** and you even there's some scenarios where there's only one document and the

**[53:36]** where there's only one document and the

**[53:36]** where there's only one document and the model knows which document it is so you

**[53:38]** model knows which document it is so you

**[53:38]** model knows which document it is so you don't have to specify that you're even

**[53:39]** don't have to specify that you're even

**[53:39]** don't have to specify that you're even asking a question about the document

**[53:40]** asking a question about the document

**[53:40]** asking a question about the document it's like implied you know so um it

**[53:43]** it's like implied you know so um it

**[53:43]** it's like implied you know so um it depends on how you set it up but I think

**[53:45]** depends on how you set it up but I think

**[53:45]** depends on how you set it up but I think in like the ideal case there's no prompt

**[53:47]** in like the ideal case there's no prompt

**[53:47]** in like the ideal case there's no prompt at all

**[53:53]** >> yeah

**[53:53]** >> yeah I it's not obvious to me that

**[53:55]** I it's not obvious to me that

**[53:55]** I it's not obvious to me that information is best stored in model yeah

**[53:58]** information is best stored in model yeah

**[53:58]** information is best stored in model yeah why do you have do you have that um it


### [54:00 - 55:00]

**[54:01]** why do you have do you have that um it

**[54:01]** why do you have do you have that um it feels implied

**[54:03]** feels implied

**[54:03]** feels implied you have my

**[54:04]** you have my

**[54:04]** you have my >> good question.

**[54:06]** >> good question.

**[54:06]** >> good question. >> So he said it's not obvious that

**[54:08]** >> So he said it's not obvious that

**[54:08]** >> So he said it's not obvious that information needs to be stored in

**[54:09]** information needs to be stored in

**[54:09]** information needs to be stored in weights. Yeah. Yeah. This is this is a

**[54:12]** weights. Yeah. Yeah. This is this is a

**[54:12]** weights. Yeah. Yeah. This is this is a good question. I think um I'm not saying

**[54:14]** good question. I think um I'm not saying

**[54:14]** good question. I think um I'm not saying that it's best to store information in

**[54:17]** that it's best to store information in

**[54:17]** that it's best to store information in weights. I guess I'm arguing that that

**[54:20]** weights. I guess I'm arguing that that

**[54:20]** weights. I guess I'm arguing that that gets you a lot and we're not using it

**[54:22]** gets you a lot and we're not using it

**[54:22]** gets you a lot and we're not using it right now.

**[54:23]** right now.

**[54:23]** right now. >> And like once you get to the scale of

**[54:25]** >> And like once you get to the scale of

**[54:25]** >> And like once you get to the scale of like a GitHub repo, you might have

**[54:28]** like a GitHub repo, you might have

**[54:28]** like a GitHub repo, you might have millions of tokens and it's just like

**[54:29]** millions of tokens and it's just like

**[54:29]** millions of tokens and it's just like very expensive. And so at least like

**[54:32]** very expensive. And so at least like

**[54:32]** very expensive. And so at least like this is the cheapest way to do it. The

**[54:34]** this is the cheapest way to do it. The

**[54:34]** this is the cheapest way to do it. The question of like can we generate

**[54:36]** question of like can we generate

**[54:36]** question of like can we generate synthetic data to do better than in

**[54:38]** synthetic data to do better than in

**[54:38]** synthetic data to do better than in context is like it's it's hard. I think

**[54:41]** context is like it's it's hard. I think

**[54:41]** context is like it's it's hard. I think it's like that's research

**[54:44]** it's like that's research

**[54:44]** it's like that's research that do you know what I mean when I say

**[54:45]** that do you know what I mean when I say

**[54:45]** that do you know what I mean when I say it's cheaper though like if you have a

**[54:48]** it's cheaper though like if you have a

**[54:48]** it's cheaper though like if you have a million token prompt you can just like

**[54:50]** million token prompt you can just like

**[54:50]** million token prompt you can just like compress it into the weights and produce

**[54:52]** compress it into the weights and produce

**[54:52]** compress it into the weights and produce a model that gives the same outputs with

**[54:54]** a model that gives the same outputs with

**[54:54]** a model that gives the same outputs with no prompt and then the inference costs

**[54:57]** no prompt and then the inference costs

**[54:57]** no prompt and then the inference costs less.


### [55:00 - 56:00]

**[55:13]** that there is no adversal data.

**[55:13]** that there is no adversal data. >> That's actually a really good question.

**[55:15]** >> That's actually a really good question.

**[55:15]** >> That's actually a really good question. Never thought about it before. Um I

**[55:17]** Never thought about it before. Um I

**[55:17]** Never thought about it before. Um I think it's probably pretty hard. Like I

**[55:18]** think it's probably pretty hard. Like I

**[55:18]** think it's probably pretty hard. Like I guess if you're training on user data

**[55:20]** guess if you're training on user data

**[55:20]** guess if you're training on user data and like you have some user that wants

**[55:22]** and like you have some user that wants

**[55:22]** and like you have some user that wants to sabotage your system and you're

**[55:24]** to sabotage your system and you're

**[55:24]** to sabotage your system and you're generating training data from their

**[55:26]** generating training data from their

**[55:26]** generating training data from their inputs, there probably are a lot of like

**[55:28]** inputs, there probably are a lot of like

**[55:28]** inputs, there probably are a lot of like security risks. And uh I guess in this

**[55:33]** security risks. And uh I guess in this

**[55:33]** security risks. And uh I guess in this scenario, if you're serving the same

**[55:34]** scenario, if you're serving the same

**[55:34]** scenario, if you're serving the same model that user and it doesn't work

**[55:35]** model that user and it doesn't work

**[55:35]** model that user and it doesn't work anymore, that's like not your problem.

**[55:37]** anymore, that's like not your problem.

**[55:37]** anymore, that's like not your problem. But once you start aggregating

**[55:38]** But once you start aggregating

**[55:38]** But once you start aggregating information across users, I bet it

**[55:40]** information across users, I bet it

**[55:40]** information across users, I bet it becomes hard. I'm sure CH GBT has the

**[55:42]** becomes hard. I'm sure CH GBT has the

**[55:42]** becomes hard. I'm sure CH GBT has the same problem where some people always

**[55:43]** same problem where some people always

**[55:43]** same problem where some people always click thumbs down instead of thumbs up

**[55:45]** click thumbs down instead of thumbs up

**[55:45]** click thumbs down instead of thumbs up to try to like [laughter]

**[55:51]** >> the research [snorts] uh they segmented

**[55:51]** >> the research [snorts] uh they segmented geographically across countries. So some

**[55:54]** geographically across countries. So some

**[55:54]** geographically across countries. So some cultures are inclined

**[55:57]** cultures are inclined

**[55:57]** cultures are inclined >> so it [laughter] files in data.


### [56:00 - 57:00]

**[56:00]** >> so it [laughter] files in data.

**[56:00]** >> so it [laughter] files in data. >> That's funny.

**[56:05]** >> Yeah. Um, so thinking maybe

**[56:05]** >> Yeah. Um, so thinking maybe [clears throat] a little bit about

**[56:05]** [clears throat] a little bit about

**[56:06]** [clears throat] a little bit about practical implementations of something

**[56:07]** practical implementations of something

**[56:07]** practical implementations of something like this. Um, especially in terms of

**[56:09]** like this. Um, especially in terms of

**[56:09]** like this. Um, especially in terms of like say version controlling, you

**[56:11]** like say version controlling, you

**[56:11]** like say version controlling, you mentioned GitHub models that you keep

**[56:13]** mentioned GitHub models that you keep

**[56:13]** mentioned GitHub models that you keep fine-tuning over time. Say you're a

**[56:15]** fine-tuning over time. Say you're a

**[56:15]** fine-tuning over time. Say you're a company that just changed a policy and

**[56:16]** company that just changed a policy and

**[56:16]** company that just changed a policy and it's just a one [snorts] line sentence.

**[56:18]** it's just a one [snorts] line sentence.

**[56:18]** it's just a one [snorts] line sentence. We honor something to we do not honor it

**[56:20]** We honor something to we do not honor it

**[56:20]** We honor something to we do not honor it anymore

**[56:21]** anymore

**[56:21]** anymore >> that keeps going back and forth. Do you

**[56:23]** >> that keeps going back and forth. Do you

**[56:23]** >> that keeps going back and forth. Do you then you know start from the base model

**[56:25]** then you know start from the base model

**[56:25]** then you know start from the base model again and then find that or go back to

**[56:27]** again and then find that or go back to

**[56:27]** again and then find that or go back to the one that already a good

**[56:28]** the one that already a good

**[56:28]** the one that already a good representation of it. I just has to

**[56:31]** representation of it. I just has to

**[56:31]** representation of it. I just has to change that one small thing and then you

**[56:33]** change that one small thing and then you

**[56:33]** change that one small thing and then you know how that kind of is joined at the

**[56:34]** know how that kind of is joined at the

**[56:34]** know how that kind of is joined at the hip with hallucinations which is kind of

**[56:37]** hip with hallucinations which is kind of

**[56:37]** hip with hallucinations which is kind of why we were doing full context

**[56:40]** why we were doing full context

**[56:40]** why we were doing full context to avoid that. Do you have any thoughts

**[56:41]** to avoid that. Do you have any thoughts

**[56:41]** to avoid that. Do you have any thoughts on how that might work? Yeah, I think it

**[56:43]** on how that might work? Yeah, I think it

**[56:43]** on how that might work? Yeah, I think it so so his question was about

**[56:46]** so so his question was about

**[56:46]** so so his question was about what do you do once you start making

**[56:48]** what do you do once you start making

**[56:48]** what do you do once you start making multiple updates to the model especially

**[56:49]** multiple updates to the model especially

**[56:50]** multiple updates to the model especially when you have like conflicting

**[56:51]** when you have like conflicting

**[56:51]** when you have like conflicting information and I think like the optimal

**[56:54]** information and I think like the optimal

**[56:54]** information and I think like the optimal synthetic data strategy was somehow

**[56:55]** synthetic data strategy was somehow

**[56:55]** synthetic data strategy was somehow figure this out during training and

**[56:57]** figure this out during training and

**[56:57]** figure this out during training and maybe even like if there's some

**[56:58]** maybe even like if there's some

**[56:58]** maybe even like if there's some documents from a few days ago that are


### [57:00 - 58:00]

**[57:00]** documents from a few days ago that are

**[57:00]** documents from a few days ago that are no longer relevant you can just like

**[57:01]** no longer relevant you can just like

**[57:01]** no longer relevant you can just like delete them but I don't know how

**[57:04]** delete them but I don't know how

**[57:04]** delete them but I don't know how >> as far as how we can give more attention

**[57:06]** >> as far as how we can give more attention

**[57:06]** >> as far as how we can give more attention in the same like whatever uh let's say

**[57:10]** in the same like whatever uh let's say

**[57:10]** in the same like whatever uh let's say uh information is conflicting with each

**[57:12]** uh information is conflicting with each

**[57:12]** uh information is conflicting with each uh whatever pre-trained versus what up

**[57:15]** uh whatever pre-trained versus what up

**[57:15]** uh whatever pre-trained versus what up front document we are giving for

**[57:16]** front document we are giving for

**[57:16]** front document we are giving for training if it is a contra but I want

**[57:19]** training if it is a contra but I want

**[57:19]** training if it is a contra but I want more preference from my document

**[57:22]** more preference from my document

**[57:22]** more preference from my document by what we are doing in like asking the

**[57:25]** by what we are doing in like asking the

**[57:25]** by what we are doing in like asking the question from the ground truth so how uh

**[57:29]** question from the ground truth so how uh

**[57:29]** question from the ground truth so how uh it will replace that scenario

**[57:33]** it will replace that scenario

**[57:33]** it will replace that scenario >> I'm [clears throat] not sure I

**[57:33]** >> I'm [clears throat] not sure I

**[57:33]** >> I'm [clears throat] not sure I understand the question

**[57:35]** understand the question

**[57:35]** understand the question >> sorry

**[57:35]** >> sorry

**[57:35]** >> sorry >> I I don't know if I understand your

**[57:37]** >> I I don't know if I understand your

**[57:37]** >> I I don't know if I understand your question

**[57:37]** question

**[57:37]** question >> okay sorry what you

**[57:40]** >> okay sorry what you

**[57:40]** >> okay sorry what you >> I didn't understand your question

**[57:41]** >> I didn't understand your question

**[57:41]** >> I didn't understand your question >> so my question is like I we have the uh

**[57:44]** >> so my question is like I we have the uh

**[57:44]** >> so my question is like I we have the uh whatever the training data we are giving

**[57:46]** whatever the training data we are giving

**[57:46]** whatever the training data we are giving it which is contradicting with the

**[57:48]** it which is contradicting with the

**[57:48]** it which is contradicting with the pre-training data it is a conflicting

**[57:51]** pre-training data it is a conflicting

**[57:51]** pre-training data it is a conflicting now while asking the question while the

**[57:53]** now while asking the question while the

**[57:53]** now while asking the question while the inference I want to give more preference

**[57:55]** inference I want to give more preference

**[57:55]** inference I want to give more preference on my data I don't need the pre-train

**[57:58]** on my data I don't need the pre-train

**[57:58]** on my data I don't need the pre-train information that's why we are using rag


### [58:00 - 59:00]

**[58:01]** information that's why we are using rag

**[58:01]** information that's why we are using rag like I need output from my ground

**[58:04]** like I need output from my ground

**[58:04]** like I need output from my ground whatever the context I'm giving

**[58:06]** whatever the context I'm giving

**[58:06]** whatever the context I'm giving >> so how it will we can achieve in the

**[58:09]** >> so how it will we can achieve in the

**[58:09]** >> so how it will we can achieve in the like a training

**[58:16]** I think that the

**[58:16]** I think that the the paradigm I'm proposing has all the

**[58:18]** the paradigm I'm proposing has all the

**[58:18]** the paradigm I'm proposing has all the same limitations of rag.

**[58:21]** same limitations of rag.

**[58:21]** same limitations of rag. I'm not positive that answers your

**[58:22]** I'm not positive that answers your

**[58:22]** I'm not positive that answers your question, but like for example, if

**[58:26]** question, but like for example, if

**[58:26]** question, but like for example, if uh like maybe in the scenario he said

**[58:28]** uh like maybe in the scenario he said

**[58:28]** uh like maybe in the scenario he said where he said something many times and

**[58:30]** where he said something many times and

**[58:30]** where he said something many times and then turns out not to be true, both rag

**[58:32]** then turns out not to be true, both rag

**[58:32]** then turns out not to be true, both rag would retrieve that and in the uh

**[58:35]** would retrieve that and in the uh

**[58:35]** would retrieve that and in the uh dumbest setup that would also be present

**[58:37]** dumbest setup that would also be present

**[58:37]** dumbest setup that would also be present alive in the training data. So I think

**[58:38]** alive in the training data. So I think

**[58:38]** alive in the training data. So I think like the same problems have to be

**[58:40]** like the same problems have to be

**[58:40]** like the same problems have to be solved.

**[58:42]** solved.

**[58:42]** solved. >> Have you done any work with federated uh

**[58:44]** >> Have you done any work with federated uh

**[58:44]** >> Have you done any work with federated uh tuning fine tuning parameions

**[58:50]** of users?

**[58:50]** of users? >> Have you done any research in that spot?

**[58:52]** >> Have you done any research in that spot?

**[58:52]** >> Have you done any research in that spot? >> No no no no uh not really but I think

**[58:54]** >> No no no no uh not really but I think

**[58:54]** >> No no no no uh not really but I think it's an interesting uh opportunity. So

**[58:56]** it's an interesting uh opportunity. So

**[58:56]** it's an interesting uh opportunity. So like back in the day a lot of people

**[58:57]** like back in the day a lot of people

**[58:57]** like back in the day a lot of people were really excited about the idea that

**[58:59]** were really excited about the idea that

**[58:59]** were really excited about the idea that you could share gradients and train the


### [59:00 - 01:00:00]

**[59:01]** you could share gradients and train the

**[59:01]** you could share gradients and train the same model across many machines. This is

**[59:03]** same model across many machines. This is

**[59:03]** same model across many machines. This is federated learning. And I think like one

**[59:06]** federated learning. And I think like one

**[59:06]** federated learning. And I think like one of the problems why it's hard is because

**[59:07]** of the problems why it's hard is because

**[59:07]** of the problems why it's hard is because the models now are so big that the

**[59:09]** the models now are so big that the

**[59:09]** the models now are so big that the network costs are way too high and

**[59:11]** network costs are way too high and

**[59:11]** network costs are way too high and because like I'm arguing that you only

**[59:13]** because like I'm arguing that you only

**[59:13]** because like I'm arguing that you only need to train a million parameters

**[59:14]** need to train a million parameters

**[59:14]** need to train a million parameters instead of a trillion. It probably comes

**[59:16]** instead of a trillion. It probably comes

**[59:16]** instead of a trillion. It probably comes back into play. So I think it's a very

**[59:18]** back into play. So I think it's a very

**[59:18]** back into play. So I think it's a very good idea especially in the RL world

**[59:20]** good idea especially in the RL world

**[59:20]** good idea especially in the RL world where you do a lot of work for a long

**[59:23]** where you do a lot of work for a long

**[59:23]** where you do a lot of work for a long time and then do gradients like very

**[59:26]** time and then do gradients like very

**[59:26]** time and then do gradients like very seldomly. So I think it probably will

**[59:29]** seldomly. So I think it probably will

**[59:29]** seldomly. So I think it probably will come back and it's smart to think of it

**[59:31]** come back and it's smart to think of it

**[59:31]** come back and it's smart to think of it but it hasn't quite yet.

**[59:34]** but it hasn't quite yet.

**[59:34]** but it hasn't quite yet. Um maybe I'll take like two more

**[59:36]** Um maybe I'll take like two more

**[59:36]** Um maybe I'll take like two more questions. Yeah. Go.

**[59:37]** questions. Yeah. Go.

**[59:37]** questions. Yeah. Go. >> Um so your argument here about training

**[59:40]** >> Um so your argument here about training

**[59:40]** >> Um so your argument here about training in um information seems to be uh counter

**[59:45]** in um information seems to be uh counter

**[59:45]** in um information seems to be uh counter to Karpathy's view of like a reasoning

**[59:47]** to Karpathy's view of like a reasoning

**[59:48]** to Karpathy's view of like a reasoning engine like distilling just the pure

**[59:50]** engine like distilling just the pure

**[59:50]** engine like distilling just the pure like you know intelligence aspect of of

**[59:53]** like you know intelligence aspect of of

**[59:53]** like you know intelligence aspect of of a model down to like a two billion

**[59:55]** a model down to like a two billion

**[59:55]** a model down to like a two billion parameter thing.

**[59:56]** parameter thing.

**[59:56]** parameter thing. Um uh and like I think that there's a

**[59:59]** Um uh and like I think that there's a

**[59:59]** Um uh and like I think that there's a bit of overlap there like um


### [01:00:00 - 01:01:00]

**[01:00:03]** bit of overlap there like um

**[01:00:03]** bit of overlap there like um like a lawyer is not doesn't have the

**[01:00:07]** like a lawyer is not doesn't have the

**[01:00:07]** like a lawyer is not doesn't have the entire legal code memorized but they

**[01:00:08]** entire legal code memorized but they

**[01:00:08]** entire legal code memorized but they know how to use the tools available to

**[01:00:10]** know how to use the tools available to

**[01:00:10]** know how to use the tools available to them to find what they need to. And so I

**[01:00:13]** them to find what they need to. And so I

**[01:00:13]** them to find what they need to. And so I I think part of it is kind of a

**[01:00:15]** I think part of it is kind of a

**[01:00:15]** I think part of it is kind of a combination of those two things where

**[01:00:16]** combination of those two things where

**[01:00:16]** combination of those two things where you're doing task specific training with

**[01:00:20]** you're doing task specific training with

**[01:00:20]** you're doing task specific training with something like this on a relatively

**[01:00:22]** something like this on a relatively

**[01:00:22]** something like this on a relatively small reasoning brain to get a sense of

**[01:00:26]** small reasoning brain to get a sense of

**[01:00:26]** small reasoning brain to get a sense of where it needs to find the things that

**[01:00:28]** where it needs to find the things that

**[01:00:28]** where it needs to find the things that uh might become stale or or you know am

**[01:00:32]** uh might become stale or or you know am

**[01:00:32]** uh might become stale or or you know am I on the right track here or

**[01:00:34]** I on the right track here or

**[01:00:34]** I on the right track here or >> Yeah. Yeah. So I think there may be a

**[01:00:37]** >> Yeah. Yeah. So I think there may be a

**[01:00:37]** >> Yeah. Yeah. So I think there may be a comparison between some people who have

**[01:00:38]** comparison between some people who have

**[01:00:38]** comparison between some people who have said, "Oh, the best model we could ever

**[01:00:40]** said, "Oh, the best model we could ever

**[01:00:40]** said, "Oh, the best model we could ever have is like really small and knows

**[01:00:42]** have is like really small and knows

**[01:00:42]** have is like really small and knows nothing but can use tools really well or

**[01:00:44]** nothing but can use tools really well or

**[01:00:44]** nothing but can use tools really well or something like that." And I guess I I

**[01:00:47]** something like that." And I guess I I

**[01:00:47]** something like that." And I guess I I was proposing some similar ideas. I said

**[01:00:49]** was proposing some similar ideas. I said

**[01:00:50]** was proposing some similar ideas. I said models know way too much. I think

**[01:00:51]** models know way too much. I think

**[01:00:51]** models know way too much. I think everyone agrees the model doesn't need

**[01:00:52]** everyone agrees the model doesn't need

**[01:00:52]** everyone agrees the model doesn't need to know the capital of the smallest

**[01:00:54]** to know the capital of the smallest

**[01:00:54]** to know the capital of the smallest province of Tajjikstan for most use

**[01:00:56]** province of Tajjikstan for most use

**[01:00:56]** province of Tajjikstan for most use cases at least in like my life.

**[01:00:59]** cases at least in like my life.

**[01:00:59]** cases at least in like my life. >> It doesn't need to remember, you know,


### [01:01:00 - 01:02:00]

**[01:01:00]** >> It doesn't need to remember, you know,

**[01:01:00]** >> It doesn't need to remember, you know, encryption keys.

**[01:01:01]** encryption keys.

**[01:01:02]** encryption keys. >> Yeah. But I think there's I I think this

**[01:01:04]** >> Yeah. But I think there's I I think this

**[01:01:04]** >> Yeah. But I think there's I I think this is a very philosophical question, but uh

**[01:01:07]** is a very philosophical question, but uh

**[01:01:07]** is a very philosophical question, but uh I think it's really hard to create a

**[01:01:08]** I think it's really hard to create a

**[01:01:08]** I think it's really hard to create a model that doesn't know anything. And so

**[01:01:10]** model that doesn't know anything. And so

**[01:01:10]** model that doesn't know anything. And so I'm more advocating for like specialized

**[01:01:13]** I'm more advocating for like specialized

**[01:01:13]** I'm more advocating for like specialized models that are good at something you

**[01:01:15]** models that are good at something you

**[01:01:15]** models that are good at something you care about but bad at other things

**[01:01:17]** care about but bad at other things

**[01:01:17]** care about but bad at other things rather than advocating for a model

**[01:01:18]** rather than advocating for a model

**[01:01:18]** rather than advocating for a model that's like bad at everything.

**[01:01:21]** that's like bad at everything.

**[01:01:21]** that's like bad at everything. >> Okay, last question here.

**[01:01:22]** >> Okay, last question here.

**[01:01:22]** >> Okay, last question here. >> Yeah. Have you ever done research yet in

**[01:01:23]** >> Yeah. Have you ever done research yet in

**[01:01:24]** >> Yeah. Have you ever done research yet in the temporal elements of the

**[01:01:25]** the temporal elements of the

**[01:01:25]** the temporal elements of the information? No, but I think that's like

**[01:01:27]** information? No, but I think that's like

**[01:01:28]** information? No, but I think that's like one of the first things to think about

**[01:01:29]** one of the first things to think about

**[01:01:29]** one of the first things to think about is like, okay, if you have information

**[01:01:30]** is like, okay, if you have information

**[01:01:30]** is like, okay, if you have information from day one and day two and day three,

**[01:01:32]** from day one and day two and day three,

**[01:01:32]** from day one and day two and day three, do you just sort of like concatenate

**[01:01:34]** do you just sort of like concatenate

**[01:01:34]** do you just sort of like concatenate everything or do you train in order kind

**[01:01:36]** everything or do you train in order kind

**[01:01:36]** everything or do you train in order kind of like you were asking or do you like

**[01:01:38]** of like you were asking or do you like

**[01:01:38]** of like you were asking or do you like train multiple models and merge them or

**[01:01:40]** train multiple models and merge them or

**[01:01:40]** train multiple models and merge them or I I actually don't know, but that's a

**[01:01:42]** I I actually don't know, but that's a

**[01:01:42]** I I actually don't know, but that's a good segue. So now I'm uh I'm working on

**[01:01:46]** good segue. So now I'm uh I'm working on

**[01:01:46]** good segue. So now I'm uh I'm working on this problems related to this a lot,

**[01:01:48]** this problems related to this a lot,

**[01:01:48]** this problems related to this a lot, thinking about this a lot. um started a

**[01:01:51]** thinking about this a lot. um started a

**[01:01:51]** thinking about this a lot. um started a company with a few other people and um

**[01:01:54]** company with a few other people and um

**[01:01:54]** company with a few other people and um this is like the kind of research we're

**[01:01:56]** this is like the kind of research we're

**[01:01:56]** this is like the kind of research we're doing. If anyone knows someone who lives

**[01:01:58]** doing. If anyone knows someone who lives

**[01:01:58]** doing. If anyone knows someone who lives in San Francisco and is a good engineer


### [01:02:00 - 01:03:00]

**[01:02:00]** in San Francisco and is a good engineer

**[01:02:00]** in San Francisco and is a good engineer and you think they're interested in

**[01:02:01]** and you think they're interested in

**[01:02:01]** and you think they're interested in this, let me know or send me an email.

**[01:02:04]** this, let me know or send me an email.

**[01:02:04]** this, let me know or send me an email. Or if you're interested in like using

**[01:02:05]** Or if you're interested in like using

**[01:02:05]** Or if you're interested in like using this kind of thing, send me an email.

**[01:02:07]** this kind of thing, send me an email.

**[01:02:07]** this kind of thing, send me an email. That would be great.

**[01:02:08]** That would be great.

**[01:02:08]** That would be great. >> It's temporal stuff or

**[01:02:10]** >> It's temporal stuff or

**[01:02:10]** >> It's temporal stuff or >> not necess I mean it's kind of all of

**[01:02:12]** >> not necess I mean it's kind of all of

**[01:02:12]** >> not necess I mean it's kind of all of this I would say. Um trying to build

**[01:02:14]** this I would say. Um trying to build

**[01:02:14]** this I would say. Um trying to build models that you can teach things to.

**[01:02:18]** models that you can teach things to.

**[01:02:18]** models that you can teach things to. All

**[01:02:23]** right. Thanks so much for having me.

**[01:02:23]** right. Thanks so much for having me. This is great. [applause]


