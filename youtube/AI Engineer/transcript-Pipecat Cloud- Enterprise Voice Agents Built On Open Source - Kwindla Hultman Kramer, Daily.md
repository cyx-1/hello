# Pipecat Cloud- Enterprise Voice Agents Built On Open Source - Kwindla Hultman Kramer, Daily

**Video URL:** https://www.youtube.com/watch?v=IA4lZjh9sTs

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Hi everybody. My name is Quinn. I am a

**[00:16]** Hi everybody. My name is Quinn. I am a co-founder of a company called Daily.

**[00:18]** co-founder of a company called Daily.

**[00:18]** co-founder of a company called Daily. Dy's other founder is in the back there,

**[00:20]** Dy's other founder is in the back there,

**[00:20]** Dy's other founder is in the back there, Nina. I'm stepping in for my colleague

**[00:22]** Nina. I'm stepping in for my colleague

**[00:22]** Nina. I'm stepping in for my colleague Mark, who couldn't make it today, so

**[00:23]** Mark, who couldn't make it today, so

**[00:23]** Mark, who couldn't make it today, so we're going to do this fast and very

**[00:25]** we're going to do this fast and very

**[00:25]** we're going to do this fast and very informally, but I think that's a good

**[00:27]** informally, but I think that's a good

**[00:27]** informally, but I think that's a good way to do it at an engineering

**[00:28]** way to do it at an engineering

**[00:28]** way to do it at an engineering conference. I don't have as much code to

**[00:29]** conference. I don't have as much code to

**[00:29]** conference. I don't have as much code to show as the last awesome presentation,

**[00:31]** show as the last awesome presentation,

**[00:31]** show as the last awesome presentation, but I'll try to show a little bit. We're

**[00:33]** but I'll try to show a little bit. We're

**[00:33]** but I'll try to show a little bit. We're going to talk about building voice

**[00:34]** going to talk about building voice

**[00:34]** going to talk about building voice agents today. Uh I work on an open

**[00:37]** agents today. Uh I work on an open

**[00:37]** agents today. Uh I work on an open source vendor neutral project called

**[00:39]** source vendor neutral project called

**[00:39]** source vendor neutral project called Pipecat. Um and a lot of other people at

**[00:41]** Pipecat. Um and a lot of other people at

**[00:41]** Pipecat. Um and a lot of other people at Daily do too because Voice AI is growing

**[00:43]** Daily do too because Voice AI is growing

**[00:43]** Daily do too because Voice AI is growing fast and is super interesting and is a

**[00:45]** fast and is super interesting and is a

**[00:45]** fast and is super interesting and is a good fit for what we do as a company. We

**[00:47]** good fit for what we do as a company. We

**[00:47]** good fit for what we do as a company. We started in 2016. We are global

**[00:50]** started in 2016. We are global

**[00:50]** started in 2016. We are global infrastructure for real-time audio,

**[00:52]** infrastructure for real-time audio,

**[00:52]** infrastructure for real-time audio, video, and now AI for developers. Pipcat

**[00:55]** video, and now AI for developers. Pipcat

**[00:55]** video, and now AI for developers. Pipcat sits somewhere higher up in the stack

**[00:57]** sits somewhere higher up in the stack

**[00:57]** sits somewhere higher up in the stack than our traditional infrastructure

**[00:59]** than our traditional infrastructure

**[00:59]** than our traditional infrastructure business. So we'll talk a little bit


### [01:00 - 02:00]

**[01:01]** business. So we'll talk a little bit

**[01:01]** business. So we'll talk a little bit about how you can build reliable,

**[01:03]** about how you can build reliable,

**[01:03]** about how you can build reliable, performant voice AI agents completely

**[01:06]** performant voice AI agents completely

**[01:06]** performant voice AI agents completely using open source software. We also

**[01:08]** using open source software. We also

**[01:08]** using open source software. We also recently launched a layer just on top of

**[01:11]** recently launched a layer just on top of

**[01:11]** recently launched a layer just on top of our traditional infrastructure designed

**[01:12]** our traditional infrastructure designed

**[01:12]** our traditional infrastructure designed for hosting voice AI agents. We'll talk

**[01:15]** for hosting voice AI agents. We'll talk

**[01:15]** for hosting voice AI agents. We'll talk just a little bit about that. Um so

**[01:17]** just a little bit about that. Um so

**[01:17]** just a little bit about that. Um so we've been doing this a long time. We

**[01:18]** we've been doing this a long time. We

**[01:18]** we've been doing this a long time. We care a lot about the developer

**[01:19]** care a lot about the developer

**[01:19]** care a lot about the developer experience for very fast, very

**[01:21]** experience for very fast, very

**[01:21]** experience for very fast, very responsive real-time audio and video. We

**[01:23]** responsive real-time audio and video. We

**[01:23]** responsive real-time audio and video. We have a long list of engineering first

**[01:25]** have a long list of engineering first

**[01:25]** have a long list of engineering first we're proud of, but that's not why

**[01:27]** we're proud of, but that's not why

**[01:27]** we're proud of, but that's not why you're here today. Uh, happy to talk

**[01:29]** you're here today. Uh, happy to talk

**[01:29]** you're here today. Uh, happy to talk about that later though. Um, if we step

**[01:32]** about that later though. Um, if we step

**[01:32]** about that later though. Um, if we step back and orient a little bit, what are

**[01:34]** back and orient a little bit, what are

**[01:34]** back and orient a little bit, what are you doing when you build a voice agent?

**[01:36]** you doing when you build a voice agent?

**[01:36]** you doing when you build a voice agent? I I tend to sort of orient people with

**[01:38]** I I tend to sort of orient people with

**[01:38]** I I tend to sort of orient people with three things they have to think about.

**[01:40]** three things they have to think about.

**[01:40]** three things they have to think about. You've got to write the code. You have

**[01:43]** You've got to write the code. You have

**[01:43]** You've got to write the code. You have to deploy that code somewhere. And then

**[01:46]** to deploy that code somewhere. And then

**[01:46]** to deploy that code somewhere. And then you have to connect users over the

**[01:48]** you have to connect users over the

**[01:48]** you have to connect users over the network or over a telefan connection to

**[01:50]** network or over a telefan connection to

**[01:50]** network or over a telefan connection to that agent. A few things here. User

**[01:54]** that agent. A few things here. User

**[01:54]** that agent. A few things here. User expectations are high. Voice AI is new,

**[01:56]** expectations are high. Voice AI is new,

**[01:56]** expectations are high. Voice AI is new, but it's growing fast, I think, because

**[01:57]** but it's growing fast, I think, because

**[01:58]** but it's growing fast, I think, because we're able to with sort of the best


### [02:00 - 03:00]

**[02:00]** we're able to with sort of the best

**[02:00]** we're able to with sort of the best technologies that are just now becoming

**[02:02]** technologies that are just now becoming

**[02:02]** technologies that are just now becoming available to meet user expectations. But

**[02:04]** available to meet user expectations. But

**[02:04]** available to meet user expectations. But users expect the AI to understand what

**[02:06]** users expect the AI to understand what

**[02:06]** users expect the AI to understand what they're saying, to feel smart and

**[02:08]** they're saying, to feel smart and

**[02:08]** they're saying, to feel smart and conversational and human uh to be

**[02:11]** conversational and human uh to be

**[02:11]** conversational and human uh to be connected to knowledge bases, to have

**[02:12]** connected to knowledge bases, to have

**[02:12]** connected to knowledge bases, to have actual access to useful information for

**[02:15]** actual access to useful information for

**[02:15]** actual access to useful information for whatever they are doing for that user.

**[02:17]** whatever they are doing for that user.

**[02:17]** whatever they are doing for that user. uh to sound natural. There's definitely

**[02:19]** uh to sound natural. There's definitely

**[02:19]** uh to sound natural. There's definitely an uncanny valley problem that in

**[02:21]** an uncanny valley problem that in

**[02:21]** an uncanny valley problem that in generative AI we fell into for a very

**[02:23]** generative AI we fell into for a very

**[02:23]** generative AI we fell into for a very long time. Now we're on the other side

**[02:25]** long time. Now we're on the other side

**[02:25]** long time. Now we're on the other side of that for voice AI which is really

**[02:27]** of that for voice AI which is really

**[02:27]** of that for voice AI which is really exciting. Um the agents have to respond

**[02:29]** exciting. Um the agents have to respond

**[02:29]** exciting. Um the agents have to respond fast. Humans expect it varies by

**[02:33]** fast. Humans expect it varies by

**[02:33]** fast. Humans expect it varies by language and by culture and by

**[02:34]** language and by culture and by

**[02:34]** language and by culture and by individual but roughly speaking humans

**[02:36]** individual but roughly speaking humans

**[02:36]** individual but roughly speaking humans expect a 500 millisecond response time

**[02:38]** expect a 500 millisecond response time

**[02:38]** expect a 500 millisecond response time in natural human conversation. If you

**[02:40]** in natural human conversation. If you

**[02:40]** in natural human conversation. If you don't do that in your voice AI interface

**[02:43]** don't do that in your voice AI interface

**[02:43]** don't do that in your voice AI interface you are probably going to lose most of

**[02:44]** you are probably going to lose most of

**[02:44]** you are probably going to lose most of your normal users. So we tell people

**[02:47]** your normal users. So we tell people

**[02:47]** your normal users. So we tell people target 800 millisecond voicetovoice

**[02:49]** target 800 millisecond voicetovoice

**[02:49]** target 800 millisecond voicetovoice response times. That's not easy to do

**[02:50]** response times. That's not easy to do

**[02:50]** response times. That's not easy to do with today's technology, but it is

**[02:52]** with today's technology, but it is

**[02:52]** with today's technology, but it is definitely possible. And build UIs very

**[02:54]** definitely possible. And build UIs very

**[02:54]** definitely possible. And build UIs very thoughtfully to understand that humans

**[02:57]** thoughtfully to understand that humans

**[02:57]** thoughtfully to understand that humans expect fast responses.

**[02:59]** expect fast responses.

**[02:59]** expect fast responses. Other thing that's hard uh a little bit


### [03:00 - 04:00]

**[03:02]** Other thing that's hard uh a little bit

**[03:02]** Other thing that's hard uh a little bit like fast response times is knowing when

**[03:04]** like fast response times is knowing when

**[03:04]** like fast response times is knowing when to respond. Uh humans are good but not

**[03:07]** to respond. Uh humans are good but not

**[03:07]** to respond. Uh humans are good but not perfect at knowing when somebody we're

**[03:09]** perfect at knowing when somebody we're

**[03:09]** perfect at knowing when somebody we're talking to is done talking and when we

**[03:11]** talking to is done talking and when we

**[03:11]** talking to is done talking and when we should start talking. Voice AI agents

**[03:13]** should start talking. Voice AI agents

**[03:13]** should start talking. Voice AI agents are not as good at that yet, but they're

**[03:14]** are not as good at that yet, but they're

**[03:14]** are not as good at that yet, but they're getting better. So we'll talk a tiny bit

**[03:16]** getting better. So we'll talk a tiny bit

**[03:16]** getting better. So we'll talk a tiny bit about that. So why do developers use a

**[03:19]** about that. So why do developers use a

**[03:19]** about that. So why do developers use a framework like Pipcat instead of writing

**[03:21]** framework like Pipcat instead of writing

**[03:21]** framework like Pipcat instead of writing all the code themselves? Well, a little

**[03:22]** all the code themselves? Well, a little

**[03:22]** all the code themselves? Well, a little bit of it is all those hard things on

**[03:24]** bit of it is all those hard things on

**[03:24]** bit of it is all those hard things on the previous slide that you probably

**[03:25]** the previous slide that you probably

**[03:25]** the previous slide that you probably don't want to write the code for

**[03:27]** don't want to write the code for

**[03:27]** don't want to write the code for yourself if you're mostly thinking about

**[03:28]** yourself if you're mostly thinking about

**[03:28]** yourself if you're mostly thinking about your business logic and your user

**[03:30]** your business logic and your user

**[03:30]** your business logic and your user experience and connecting to all of your

**[03:32]** experience and connecting to all of your

**[03:32]** experience and connecting to all of your systems. You want to use battle tested

**[03:35]** systems. You want to use battle tested

**[03:35]** systems. You want to use battle tested implementations of things like turn

**[03:38]** implementations of things like turn

**[03:38]** implementations of things like turn detection, interruption handling,

**[03:40]** detection, interruption handling,

**[03:40]** detection, interruption handling, context management, calling out to other

**[03:41]** context management, calling out to other

**[03:41]** context management, calling out to other tools, function function calling in an

**[03:44]** tools, function function calling in an

**[03:44]** tools, function function calling in an asynchronous environment, all that

**[03:45]** asynchronous environment, all that

**[03:46]** asynchronous environment, all that stuff. Um, so developers tend to use

**[03:49]** stuff. Um, so developers tend to use

**[03:49]** stuff. Um, so developers tend to use frameworks these days for lots of

**[03:50]** frameworks these days for lots of

**[03:50]** frameworks these days for lots of agentic things they do. Uh, and voice

**[03:52]** agentic things they do. Uh, and voice

**[03:52]** agentic things they do. Uh, and voice AI, I think, is even more important to

**[03:55]** AI, I think, is even more important to

**[03:55]** AI, I think, is even more important to sit on top of uh really well- tested

**[03:58]** sit on top of uh really well- tested

**[03:58]** sit on top of uh really well- tested infrastructure and code components than


### [04:00 - 05:00]

**[04:00]** infrastructure and code components than

**[04:00]** infrastructure and code components than even in other domains. Um, Pipcat

**[04:03]** even in other domains. Um, Pipcat

**[04:03]** even in other domains. Um, Pipcat appeals to developers because it's 100%

**[04:05]** appeals to developers because it's 100%

**[04:05]** appeals to developers because it's 100% open source and completely vendor

**[04:06]** open source and completely vendor

**[04:06]** open source and completely vendor neutral. You can use it with lots of

**[04:08]** neutral. You can use it with lots of

**[04:08]** neutral. You can use it with lots of different providers at every single

**[04:10]** different providers at every single

**[04:10]** different providers at every single layer of the stack that Pipcat enables.

**[04:12]** layer of the stack that Pipcat enables.

**[04:12]** layer of the stack that Pipcat enables. Um, for example, there's native telefan

**[04:14]** Um, for example, there's native telefan

**[04:14]** Um, for example, there's native telefan support in Pipcat. So, you can use

**[04:15]** support in Pipcat. So, you can use

**[04:15]** support in Pipcat. So, you can use Pipcat with lots of different telefan

**[04:17]** Pipcat with lots of different telefan

**[04:17]** Pipcat with lots of different telefan providers in a plug-and-play manner. You

**[04:19]** providers in a plug-and-play manner. You

**[04:20]** providers in a plug-and-play manner. You can use Twilio for example, which a lot

**[04:22]** can use Twilio for example, which a lot

**[04:22]** can use Twilio for example, which a lot of developers know. If you're in an

**[04:24]** of developers know. If you're in an

**[04:24]** of developers know. If you're in an geography like India where Twilio

**[04:25]** geography like India where Twilio

**[04:25]** geography like India where Twilio doesn't have phone numbers, you can use

**[04:27]** doesn't have phone numbers, you can use

**[04:27]** doesn't have phone numbers, you can use Pivo. Bunch of other telefan providers

**[04:29]** Pivo. Bunch of other telefan providers

**[04:29]** Pivo. Bunch of other telefan providers are supported. Um there's a native audio

**[04:32]** are supported. Um there's a native audio

**[04:32]** are supported. Um there's a native audio smart turn model that's completely open

**[04:34]** smart turn model that's completely open

**[04:34]** smart turn model that's completely open source in Pipcat. So the community has

**[04:36]** source in Pipcat. So the community has

**[04:36]** source in Pipcat. So the community has gotten large enough that there's kind of

**[04:37]** gotten large enough that there's kind of

**[04:37]** gotten large enough that there's kind of cutting edge ML research at least in the

**[04:39]** cutting edge ML research at least in the

**[04:40]** cutting edge ML research at least in the small model domain coming out of this

**[04:41]** small model domain coming out of this

**[04:41]** small model domain coming out of this open source community which is really

**[04:43]** open source community which is really

**[04:43]** open source community which is really fun. Um Pipcat cloud I think is a really

**[04:46]** fun. Um Pipcat cloud I think is a really

**[04:46]** fun. Um Pipcat cloud I think is a really nice advantage for the Pipcat ecosystem.

**[04:48]** nice advantage for the Pipcat ecosystem.

**[04:48]** nice advantage for the Pipcat ecosystem. It's the first open-source voice AI

**[04:50]** It's the first open-source voice AI

**[04:50]** It's the first open-source voice AI cloud sort of built from the ground up

**[04:52]** cloud sort of built from the ground up

**[04:52]** cloud sort of built from the ground up to host code that you write but that is

**[04:54]** to host code that you write but that is

**[04:54]** to host code that you write but that is designed for the problems of voice AI.

**[04:57]** designed for the problems of voice AI.

**[04:57]** designed for the problems of voice AI. Uh, and Pipcat supports a lot of models

**[04:59]** Uh, and Pipcat supports a lot of models

**[04:59]** Uh, and Pipcat supports a lot of models and services. The count is something


### [05:00 - 06:00]

**[05:01]** and services. The count is something

**[05:01]** and services. The count is something like 60 plus. All the things you would

**[05:03]** like 60 plus. All the things you would

**[05:03]** like 60 plus. All the things you would want to use in a voice AI agent are

**[05:05]** want to use in a voice AI agent are

**[05:05]** want to use in a voice AI agent are probably in Pipcat main branch. Um, so

**[05:09]** probably in Pipcat main branch. Um, so

**[05:09]** probably in Pipcat main branch. Um, so you probably don't have to write code to

**[05:11]** you probably don't have to write code to

**[05:11]** you probably don't have to write code to get started, though the appeal is that

**[05:13]** get started, though the appeal is that

**[05:13]** get started, though the appeal is that you can write lots and lots of code if

**[05:15]** you can write lots and lots of code if

**[05:15]** you can write lots and lots of code if you want to. So there's no ceiling. Um,

**[05:17]** you want to. So there's no ceiling. Um,

**[05:17]** you want to. So there's no ceiling. Um, I'll talk a little bit about what the

**[05:19]** I'll talk a little bit about what the

**[05:19]** I'll talk a little bit about what the architecture looks like. And we probably

**[05:20]** architecture looks like. And we probably

**[05:20]** architecture looks like. And we probably won't have time to talk about client

**[05:22]** won't have time to talk about client

**[05:22]** won't have time to talk about client SDKs because most of you in this room

**[05:24]** SDKs because most of you in this room

**[05:24]** SDKs because most of you in this room are probably building for telefan use

**[05:26]** are probably building for telefan use

**[05:26]** are probably building for telefan use cases. But there's a really rich and

**[05:28]** cases. But there's a really rich and

**[05:28]** cases. But there's a really rich and growing set of JavaScript, React, iOS,

**[05:31]** growing set of JavaScript, React, iOS,

**[05:31]** growing set of JavaScript, React, iOS, Android client side components and SDKs

**[05:34]** Android client side components and SDKs

**[05:34]** Android client side components and SDKs that people in the pipecat community are

**[05:35]** that people in the pipecat community are

**[05:36]** that people in the pipecat community are using to build multimodal applications

**[05:38]** using to build multimodal applications

**[05:38]** using to build multimodal applications that run in the web and on native mobile

**[05:40]** that run in the web and on native mobile

**[05:40]** that run in the web and on native mobile platforms. Um, we talked about this so I

**[05:44]** platforms. Um, we talked about this so I

**[05:44]** platforms. Um, we talked about this so I will actually just skip this slide. Uh,

**[05:46]** will actually just skip this slide. Uh,

**[05:46]** will actually just skip this slide. Uh, I hope we'll have time for Q&A. That's

**[05:48]** I hope we'll have time for Q&A. That's

**[05:48]** I hope we'll have time for Q&A. That's the most fun part. Um, here's the other

**[05:50]** the most fun part. Um, here's the other

**[05:50]** the most fun part. Um, here's the other piece that often helps orient people.

**[05:52]** piece that often helps orient people.

**[05:52]** piece that often helps orient people. This is what a Pipcat agent looks like.

**[05:55]** This is what a Pipcat agent looks like.

**[05:55]** This is what a Pipcat agent looks like. So, you're building a pipeline of

**[05:58]** So, you're building a pipeline of

**[05:58]** So, you're building a pipeline of programmable media handling elements.


### [06:00 - 07:00]

**[06:00]** programmable media handling elements.

**[06:00]** programmable media handling elements. Uh, these are all written in Python,

**[06:02]** Uh, these are all written in Python,

**[06:02]** Uh, these are all written in Python, although lots of the performant uh

**[06:05]** although lots of the performant uh

**[06:05]** although lots of the performant uh sensitive ones bottom out in some kind

**[06:07]** sensitive ones bottom out in some kind

**[06:07]** sensitive ones bottom out in some kind of C code. Uh, it's pretty common in

**[06:11]** of C code. Uh, it's pretty common in

**[06:11]** of C code. Uh, it's pretty common in real-time media handling. Um, you

**[06:13]** real-time media handling. Um, you

**[06:13]** real-time media handling. Um, you probably don't have to worry about that

**[06:14]** probably don't have to worry about that

**[06:14]** probably don't have to worry about that level though. You're probably just

**[06:15]** level though. You're probably just

**[06:15]** level though. You're probably just thinking in pipe pipe pi python. Um,

**[06:18]** thinking in pipe pipe pi python. Um,

**[06:18]** thinking in pipe pipe pi python. Um, pipecat pipelines can be really simple.

**[06:20]** pipecat pipelines can be really simple.

**[06:20]** pipecat pipelines can be really simple. Uh, they can have just a couple, maybe

**[06:22]** Uh, they can have just a couple, maybe

**[06:22]** Uh, they can have just a couple, maybe just three elements, something for the

**[06:24]** just three elements, something for the

**[06:24]** just three elements, something for the network, something that's doing some

**[06:25]** network, something that's doing some

**[06:25]** network, something that's doing some processing, and something that's sending

**[06:27]** processing, and something that's sending

**[06:27]** processing, and something that's sending stuff back out the network. Or they can

**[06:28]** stuff back out the network. Or they can

**[06:28]** stuff back out the network. Or they can be quite complicated. And we see

**[06:30]** be quite complicated. And we see

**[06:30]** be quite complicated. And we see enterprise voice agents often become

**[06:32]** enterprise voice agents often become

**[06:32]** enterprise voice agents often become quite complicated because they're doing

**[06:34]** quite complicated because they're doing

**[06:34]** quite complicated because they're doing complicated things and connecting out to

**[06:36]** complicated things and connecting out to

**[06:36]** complicated things and connecting out to a large variety of existing legacy

**[06:39]** a large variety of existing legacy

**[06:39]** a large variety of existing legacy systems. Um, so an example of a little

**[06:42]** systems. Um, so an example of a little

**[06:42]** systems. Um, so an example of a little bit of that span. The left two

**[06:44]** bit of that span. The left two

**[06:44]** bit of that span. The left two screenshots here are from the pipecat

**[06:46]** screenshots here are from the pipecat

**[06:46]** screenshots here are from the pipecat docs about how you work with the open

**[06:48]** docs about how you work with the open

**[06:48]** docs about how you work with the open AAI audio ccentric models in pipcat.

**[06:51]** AAI audio ccentric models in pipcat.

**[06:51]** AAI audio ccentric models in pipcat. Open AI gives you a couple of different

**[06:52]** Open AI gives you a couple of different

**[06:52]** Open AI gives you a couple of different shapes of models and APIs that you can

**[06:55]** shapes of models and APIs that you can

**[06:55]** shapes of models and APIs that you can use. One is chaining together

**[06:57]** use. One is chaining together

**[06:57]** use. One is chaining together transcription large language model

**[06:59]** transcription large language model

**[06:59]** transcription large language model operating in text mode and voice output.


### [07:00 - 08:00]

**[07:02]** operating in text mode and voice output.

**[07:02]** operating in text mode and voice output. The other is using their new and uh in

**[07:04]** The other is using their new and uh in

**[07:04]** The other is using their new and uh in some ways experimental speech-to-pech

**[07:06]** some ways experimental speech-to-pech

**[07:06]** some ways experimental speech-to-pech models which are also really awesome and

**[07:08]** models which are also really awesome and

**[07:08]** models which are also really awesome and promising. Um, you can do either of

**[07:12]** promising. Um, you can do either of

**[07:12]** promising. Um, you can do either of those approaches in Pipcat just by

**[07:14]** those approaches in Pipcat just by

**[07:14]** those approaches in Pipcat just by changing probably three or four lines of

**[07:16]** changing probably three or four lines of

**[07:16]** changing probably three or four lines of code. Uh, on the right is the Python

**[07:20]** code. Uh, on the right is the Python

**[07:20]** code. Uh, on the right is the Python sort of the chunk core chunk of a few

**[07:22]** sort of the chunk core chunk of a few

**[07:22]** sort of the chunk core chunk of a few hundred lines of Python code and a flow

**[07:24]** hundred lines of Python code and a flow

**[07:24]** hundred lines of Python code and a flow diagram for a more complicated uh,

**[07:26]** diagram for a more complicated uh,

**[07:26]** diagram for a more complicated uh, pipeline. This is one of my favorite

**[07:28]** pipeline. This is one of my favorite

**[07:28]** pipeline. This is one of my favorite starter kit examples for Pipcat. It uses

**[07:30]** starter kit examples for Pipcat. It uses

**[07:30]** starter kit examples for Pipcat. It uses two uh, instances of the Gemini

**[07:32]** two uh, instances of the Gemini

**[07:32]** two uh, instances of the Gemini multimodal live API in audio native

**[07:36]** multimodal live API in audio native

**[07:36]** multimodal live API in audio native mode. uh and one is the conversational

**[07:39]** mode. uh and one is the conversational

**[07:39]** mode. uh and one is the conversational flow and the other is a another

**[07:42]** flow and the other is a another

**[07:42]** flow and the other is a another participant in the conversation that

**[07:43]** participant in the conversation that

**[07:43]** participant in the conversation that plays a game with the user. So there's

**[07:45]** plays a game with the user. So there's

**[07:46]** plays a game with the user. So there's sort of an LLM as a judge pattern here

**[07:47]** sort of an LLM as a judge pattern here

**[07:47]** sort of an LLM as a judge pattern here but in the context of a game. Uh and

**[07:50]** but in the context of a game. Uh and

**[07:50]** but in the context of a game. Uh and you're moving the audio frames around

**[07:52]** you're moving the audio frames around

**[07:52]** you're moving the audio frames around through both pipelines selectively

**[07:54]** through both pipelines selectively

**[07:54]** through both pipelines selectively depending on the results of the

**[07:55]** depending on the results of the

**[07:55]** depending on the results of the real-time inference. Uh which is a

**[07:57]** real-time inference. Uh which is a

**[07:57]** real-time inference. Uh which is a pattern we also see in enterprise use

**[07:59]** pattern we also see in enterprise use

**[07:59]** pattern we also see in enterprise use cases but it's fun to clone this and run


### [08:00 - 09:00]

**[08:01]** cases but it's fun to clone this and run

**[08:01]** cases but it's fun to clone this and run it and play the game.

**[08:04]** it and play the game.

**[08:04]** it and play the game. Um, we listed some of the services here.

**[08:07]** Um, we listed some of the services here.

**[08:07]** Um, we listed some of the services here. Uh, we can talk a lot more if, uh, you

**[08:09]** Uh, we can talk a lot more if, uh, you

**[08:09]** Uh, we can talk a lot more if, uh, you want to in the Q&A about sort of what we

**[08:10]** want to in the Q&A about sort of what we

**[08:10]** want to in the Q&A about sort of what we see people actually using in production

**[08:12]** see people actually using in production

**[08:12]** see people actually using in production most often in terms of models and

**[08:15]** most often in terms of models and

**[08:15]** most often in terms of models and services, uh, in enterprise voice AI.

**[08:18]** services, uh, in enterprise voice AI.

**[08:18]** services, uh, in enterprise voice AI. So, that's a very quick rundown of the

**[08:21]** So, that's a very quick rundown of the

**[08:21]** So, that's a very quick rundown of the Pipcat framework, which is how you write

**[08:23]** Pipcat framework, which is how you write

**[08:23]** Pipcat framework, which is how you write the code. Now, how do you deploy it? And

**[08:26]** the code. Now, how do you deploy it? And

**[08:26]** the code. Now, how do you deploy it? And why am I talking to you about Pipcat

**[08:27]** why am I talking to you about Pipcat

**[08:28]** why am I talking to you about Pipcat Cloud today? Um, there are a bunch of

**[08:29]** Cloud today? Um, there are a bunch of

**[08:29]** Cloud today? Um, there are a bunch of hard things about Voice AI that are

**[08:31]** hard things about Voice AI that are

**[08:31]** hard things about Voice AI that are unique to these use cases. These are

**[08:33]** unique to these use cases. These are

**[08:33]** unique to these use cases. These are long running sessions. Uh they have to

**[08:36]** long running sessions. Uh they have to

**[08:36]** long running sessions. Uh they have to use network protocols that are designed

**[08:38]** use network protocols that are designed

**[08:38]** use network protocols that are designed for low latency. Um things like

**[08:41]** for low latency. Um things like

**[08:41]** for low latency. Um things like autoscaling

**[08:42]** autoscaling

**[08:42]** autoscaling are not available out of the box for

**[08:44]** are not available out of the box for

**[08:44]** are not available out of the box for these workloads the way they are for

**[08:46]** these workloads the way they are for

**[08:46]** these workloads the way they are for something like HTTP workloads. So I was

**[08:49]** something like HTTP workloads. So I was

**[08:49]** something like HTTP workloads. So I was actually quite resistant for a long time

**[08:51]** actually quite resistant for a long time

**[08:51]** actually quite resistant for a long time to building anything commercial around

**[08:54]** to building anything commercial around

**[08:54]** to building anything commercial around Pipcat at daily because we do the

**[08:56]** Pipcat at daily because we do the

**[08:56]** Pipcat at daily because we do the low-level infrastructure. We already

**[08:57]** low-level infrastructure. We already

**[08:57]** low-level infrastructure. We already have things that we do that serve the

**[08:59]** have things that we do that serve the

**[08:59]** have things that we do that serve the pipecat community. But it got to the


### [09:00 - 10:00]

**[09:01]** pipecat community. But it got to the

**[09:02]** pipecat community. But it got to the point where there were very large

**[09:03]** point where there were very large

**[09:03]** point where there were very large percentage of the questions in the

**[09:04]** percentage of the questions in the

**[09:04]** percentage of the questions in the Pipcat Discord were about how to deploy

**[09:06]** Pipcat Discord were about how to deploy

**[09:06]** Pipcat Discord were about how to deploy and scale. Um, and I I I initially sort

**[09:10]** and scale. Um, and I I I initially sort

**[09:10]** and scale. Um, and I I I initially sort of felt like that was a solved enough

**[09:12]** of felt like that was a solved enough

**[09:12]** of felt like that was a solved enough problem because what we do in the

**[09:14]** problem because what we do in the

**[09:14]** problem because what we do in the infrastructure level helps you in one

**[09:16]** infrastructure level helps you in one

**[09:16]** infrastructure level helps you in one way. what a lot of our friends and and

**[09:18]** way. what a lot of our friends and and

**[09:18]** way. what a lot of our friends and and customers do much higher up in the stack

**[09:21]** customers do much higher up in the stack

**[09:21]** customers do much higher up in the stack with

**[09:22]** with

**[09:22]** with platforms that sort of wrap all of the

**[09:24]** platforms that sort of wrap all of the

**[09:24]** platforms that sort of wrap all of the voice AI problem set in very easy to use

**[09:26]** voice AI problem set in very easy to use

**[09:26]** voice AI problem set in very easy to use dashboards and tools and guies are also

**[09:29]** dashboards and tools and guies are also

**[09:29]** dashboards and tools and guies are also really good solutions. But what we came

**[09:32]** really good solutions. But what we came

**[09:32]** really good solutions. But what we came to realize is that there was sort of a

**[09:33]** to realize is that there was sort of a

**[09:34]** to realize is that there was sort of a middle of the stack that people were

**[09:35]** middle of the stack that people were

**[09:35]** middle of the stack that people were asking about a lot in the open source

**[09:37]** asking about a lot in the open source

**[09:37]** asking about a lot in the open source community that boiled down to how do I

**[09:39]** community that boiled down to how do I

**[09:39]** community that boiled down to how do I do my Kubernetes? Um, so people would

**[09:41]** do my Kubernetes? Um, so people would

**[09:42]** do my Kubernetes? Um, so people would ask questions in the Pipecut Discord

**[09:43]** ask questions in the Pipecut Discord

**[09:43]** ask questions in the Pipecut Discord about deployment and scaling and we

**[09:45]** about deployment and scaling and we

**[09:45]** about deployment and scaling and we would say, "Oh, well, if you really want

**[09:46]** would say, "Oh, well, if you really want

**[09:46]** would say, "Oh, well, if you really want to run this stuff yourself on your own

**[09:48]** to run this stuff yourself on your own

**[09:48]** to run this stuff yourself on your own infrastructure, here are the five things

**[09:49]** infrastructure, here are the five things

**[09:49]** infrastructure, here are the five things you do in Kubernetes." And people would

**[09:51]** you do in Kubernetes." And people would

**[09:51]** you do in Kubernetes." And people would say, "Some version of Cooper what?" Um,

**[09:54]** say, "Some version of Cooper what?" Um,

**[09:54]** say, "Some version of Cooper what?" Um, and we don't have a good answer to that.

**[09:57]** and we don't have a good answer to that.

**[09:57]** and we don't have a good answer to that. So, we thought we'd come up with a good

**[09:58]** So, we thought we'd come up with a good

**[09:58]** So, we thought we'd come up with a good answer to that, which is a very thin


### [10:00 - 11:00]

**[10:00]** answer to that, which is a very thin

**[10:00]** answer to that, which is a very thin layer on top of our existing global

**[10:03]** layer on top of our existing global

**[10:03]** layer on top of our existing global media oriented real-time infrastructure

**[10:06]** media oriented real-time infrastructure

**[10:06]** media oriented real-time infrastructure designed as what I think of, this is not

**[10:08]** designed as what I think of, this is not

**[10:08]** designed as what I think of, this is not a very good marketing tagline, but I

**[10:10]** a very good marketing tagline, but I

**[10:10]** a very good marketing tagline, but I think of this as a very thin wrapper

**[10:12]** think of this as a very thin wrapper

**[10:12]** think of this as a very thin wrapper around Docker and Kubernetes optimized

**[10:15]** around Docker and Kubernetes optimized

**[10:15]** around Docker and Kubernetes optimized for voice AI. Um, so what are the things

**[10:18]** for voice AI. Um, so what are the things

**[10:18]** for voice AI. Um, so what are the things we're trying to solve for? Fast start

**[10:20]** we're trying to solve for? Fast start

**[10:20]** we're trying to solve for? Fast start times are very important. If somebody

**[10:21]** times are very important. If somebody

**[10:21]** times are very important. If somebody calls your voice agent uh and they hear

**[10:24]** calls your voice agent uh and they hear

**[10:24]** calls your voice agent uh and they hear ringing, they want to hear that voice

**[10:26]** ringing, they want to hear that voice

**[10:26]** ringing, they want to hear that voice agent pick up the phone and say hello

**[10:28]** agent pick up the phone and say hello

**[10:28]** agent pick up the phone and say hello pretty fast. Um no, almost no matter

**[10:31]** pretty fast. Um no, almost no matter

**[10:31]** pretty fast. Um no, almost no matter what you do in AI, you care about cold

**[10:33]** what you do in AI, you care about cold

**[10:33]** what you do in AI, you care about cold start times, but it's even more

**[10:34]** start times, but it's even more

**[10:34]** start times, but it's even more important when the user is initiating

**[10:37]** important when the user is initiating

**[10:37]** important when the user is initiating some action and expects you to hear

**[10:39]** some action and expects you to hear

**[10:39]** some action and expects you to hear audio back. Um cold starts are hard. If

**[10:43]** audio back. Um cold starts are hard. If

**[10:43]** audio back. Um cold starts are hard. If you've built Genai infrastructure, you

**[10:45]** you've built Genai infrastructure, you

**[10:45]** you've built Genai infrastructure, you know that uh we try to solve the cold

**[10:47]** know that uh we try to solve the cold

**[10:47]** know that uh we try to solve the cold start uh problem for voice AI. happy to

**[10:50]** start uh problem for voice AI. happy to

**[10:50]** start uh problem for voice AI. happy to talk about cold starts in great detail

**[10:53]** talk about cold starts in great detail

**[10:53]** talk about cold starts in great detail because it's something I've been

**[10:53]** because it's something I've been

**[10:54]** because it's something I've been thinking a lot about over the last few

**[10:55]** thinking a lot about over the last few

**[10:55]** thinking a lot about over the last few months. Um, autoscaling is a little bit

**[10:57]** months. Um, autoscaling is a little bit

**[10:57]** months. Um, autoscaling is a little bit related to cold starts. You want your


### [11:00 - 12:00]

**[11:00]** related to cold starts. You want your

**[11:00]** related to cold starts. You want your resources to expand as your traffic

**[11:03]** resources to expand as your traffic

**[11:03]** resources to expand as your traffic pattern expands. The alternative is you

**[11:05]** pattern expands. The alternative is you

**[11:05]** pattern expands. The alternative is you know exactly what your traffic pattern

**[11:07]** know exactly what your traffic pattern

**[11:07]** know exactly what your traffic pattern is and you just deploy a bunch of

**[11:09]** is and you just deploy a bunch of

**[11:09]** is and you just deploy a bunch of resources. Uh, that doesn't work for

**[11:10]** resources. Uh, that doesn't work for

**[11:10]** resources. Uh, that doesn't work for most workloads. Most people have timed

**[11:12]** most workloads. Most people have timed

**[11:12]** most workloads. Most people have timed dependent or completely unpredictable

**[11:15]** dependent or completely unpredictable

**[11:15]** dependent or completely unpredictable workloads. Uh, so you need to scale up

**[11:17]** workloads. Uh, so you need to scale up

**[11:17]** workloads. Uh, so you need to scale up and scale down. Um, real time is

**[11:20]** and scale down. Um, real time is

**[11:20]** and scale down. Um, real time is different from non-real time. And by

**[11:22]** different from non-real time. And by

**[11:22]** different from non-real time. And by non-real time, I mean everything that's

**[11:24]** non-real time, I mean everything that's

**[11:24]** non-real time, I mean everything that's not conversational latency of a few

**[11:26]** not conversational latency of a few

**[11:26]** not conversational latency of a few hundred milliseconds or less. If you are

**[11:29]** hundred milliseconds or less. If you are

**[11:29]** hundred milliseconds or less. If you are making an HTTP request, you want it to

**[11:31]** making an HTTP request, you want it to

**[11:31]** making an HTTP request, you want it to be fast, but you don't really care if

**[11:33]** be fast, but you don't really care if

**[11:33]** be fast, but you don't really care if your P95 is 1500 milliseconds or 2,000

**[11:36]** your P95 is 1500 milliseconds or 2,000

**[11:36]** your P95 is 1500 milliseconds or 2,000 milliseconds. In most cases in a voice

**[11:38]** milliseconds. In most cases in a voice

**[11:38]** milliseconds. In most cases in a voice AI conversation, you care a lot if your

**[11:40]** AI conversation, you care a lot if your

**[11:40]** AI conversation, you care a lot if your P95 goes up above 800, 900, 1,000

**[11:44]** P95 goes up above 800, 900, 1,000

**[11:44]** P95 goes up above 800, 900, 1,000 milliseconds for the entire voicetooice

**[11:47]** milliseconds for the entire voicetooice

**[11:47]** milliseconds for the entire voicetooice uh response chain. Uh all the little

**[11:51]** uh response chain. Uh all the little

**[11:51]** uh response chain. Uh all the little inference calls you make as part of that

**[11:52]** inference calls you make as part of that

**[11:52]** inference calls you make as part of that have to be much faster than that by

**[11:54]** have to be much faster than that by

**[11:54]** have to be much faster than that by definition. Um so the whole networking

**[11:57]** definition. Um so the whole networking

**[11:57]** definition. Um so the whole networking stack from client to wherever your pipe


### [12:00 - 13:00]

**[12:01]** stack from client to wherever your pipe

**[12:01]** stack from client to wherever your pipe code is running and inside that

**[12:03]** code is running and inside that

**[12:03]** code is running and inside that Kubernetes cluster has to be optimized

**[12:05]** Kubernetes cluster has to be optimized

**[12:05]** Kubernetes cluster has to be optimized for real time.

**[12:07]** for real time.

**[12:07]** for real time. uh you probably need global deployment.

**[12:09]** uh you probably need global deployment.

**[12:09]** uh you probably need global deployment. Uh you probably have uh GDPR or data

**[12:12]** Uh you probably have uh GDPR or data

**[12:12]** Uh you probably have uh GDPR or data residency or other kinds of data privacy

**[12:15]** residency or other kinds of data privacy

**[12:15]** residency or other kinds of data privacy requirements or you just need global

**[12:17]** requirements or you just need global

**[12:17]** requirements or you just need global deployment because you want these

**[12:19]** deployment because you want these

**[12:19]** deployment because you want these servers close to users because that

**[12:21]** servers close to users because that

**[12:21]** servers close to users because that helps with latency

**[12:23]** helps with latency

**[12:23]** helps with latency and all these things have to be like

**[12:25]** and all these things have to be like

**[12:25]** and all these things have to be like delivered at reasonable cost. So we try

**[12:27]** delivered at reasonable cost. So we try

**[12:27]** delivered at reasonable cost. So we try to take these things off of your plate

**[12:30]** to take these things off of your plate

**[12:30]** to take these things off of your plate and help you build quickly and get to

**[12:32]** and help you build quickly and get to

**[12:32]** and help you build quickly and get to market uh with your voice agents. Um, a

**[12:36]** market uh with your voice agents. Um, a

**[12:36]** market uh with your voice agents. Um, a couple other things that are just worth

**[12:37]** couple other things that are just worth

**[12:37]** couple other things that are just worth flagging here. We've done a lot of work

**[12:38]** flagging here. We've done a lot of work

**[12:38]** flagging here. We've done a lot of work on turn detection, which is sort of one

**[12:40]** on turn detection, which is sort of one

**[12:40]** on turn detection, which is sort of one of the 2025 top three problems most

**[12:43]** of the 2025 top three problems most

**[12:43]** of the 2025 top three problems most people in Voice AI are thinking about

**[12:45]** people in Voice AI are thinking about

**[12:45]** people in Voice AI are thinking about how to make better. Um, check out the

**[12:47]** how to make better. Um, check out the

**[12:47]** how to make better. Um, check out the open source smart turn model that's part

**[12:49]** open source smart turn model that's part

**[12:49]** open source smart turn model that's part of the Pipcat ecosystem if you're

**[12:51]** of the Pipcat ecosystem if you're

**[12:51]** of the Pipcat ecosystem if you're interested in in that. Uh, the open

**[12:53]** interested in in that. Uh, the open

**[12:53]** interested in in that. Uh, the open source smart turn model is built into

**[12:54]** source smart turn model is built into

**[12:54]** source smart turn model is built into Pipcat cloud and runs for free. Our

**[12:57]** Pipcat cloud and runs for free. Our

**[12:57]** Pipcat cloud and runs for free. Our friends at FAL host it. Um, you've

**[12:59]** friends at FAL host it. Um, you've

**[12:59]** friends at FAL host it. Um, you've probably heard of FAL if you're doing


### [13:00 - 14:00]

**[13:00]** probably heard of FAL if you're doing

**[13:00]** probably heard of FAL if you're doing Genai stuff. very fast, very good GPU

**[13:03]** Genai stuff. very fast, very good GPU

**[13:03]** Genai stuff. very fast, very good GPU optimized inference

**[13:06]** optimized inference

**[13:06]** optimized inference um and ambient noise and background

**[13:07]** um and ambient noise and background

**[13:07]** um and ambient noise and background voices. So one problem with voice AI is

**[13:10]** voices. So one problem with voice AI is

**[13:10]** voices. So one problem with voice AI is that even though transcription models

**[13:12]** that even though transcription models

**[13:12]** that even though transcription models today are very res like resilient to all

**[13:16]** today are very res like resilient to all

**[13:16]** today are very res like resilient to all kinds of noisy environments, the LMS

**[13:17]** kinds of noisy environments, the LMS

**[13:18]** kinds of noisy environments, the LMS themselves are not. So if you are trying

**[13:20]** themselves are not. So if you are trying

**[13:20]** themselves are not. So if you are trying to do transcription and figure out when

**[13:22]** to do transcription and figure out when

**[13:22]** to do transcription and figure out when people are talking and figure out when

**[13:24]** people are talking and figure out when

**[13:24]** people are talking and figure out when to fire inference down the chain and ask

**[13:28]** to fire inference down the chain and ask

**[13:28]** to fire inference down the chain and ask your LLMs to do something, having

**[13:30]** your LLMs to do something, having

**[13:30]** your LLMs to do something, having background noise that sounds a little

**[13:32]** background noise that sounds a little

**[13:32]** background noise that sounds a little bit like speech will trigger lots of

**[13:34]** bit like speech will trigger lots of

**[13:34]** bit like speech will trigger lots of interruptions that you don't mean to

**[13:36]** interruptions that you don't mean to

**[13:36]** interruptions that you don't mean to happen and will inject lots of spurious

**[13:39]** happen and will inject lots of spurious

**[13:39]** happen and will inject lots of spurious pseudo speech into your transcripts. So

**[13:42]** pseudo speech into your transcripts. So

**[13:42]** pseudo speech into your transcripts. So and that's true even for speechtospech

**[13:43]** and that's true even for speechtospech

**[13:44]** and that's true even for speechtospech models today. Uh they're not very

**[13:45]** models today. Uh they're not very

**[13:45]** models today. Uh they're not very resilient to background noise. Um the

**[13:48]** resilient to background noise. Um the

**[13:48]** resilient to background noise. Um the best the the the best solution to

**[13:51]** best the the the best solution to

**[13:51]** best the the the best solution to background noise today is a commercial

**[13:52]** background noise today is a commercial

**[13:52]** background noise today is a commercial model from a really great small company

**[13:54]** model from a really great small company

**[13:54]** model from a really great small company called Crisp. The Crisp uh model is only

**[13:57]** called Crisp. The Crisp uh model is only

**[13:57]** called Crisp. The Crisp uh model is only available with sort of big chunk of

**[13:59]** available with sort of big chunk of

**[13:59]** available with sort of big chunk of commercial licensing. Uh you can use


### [14:00 - 15:00]

**[14:01]** commercial licensing. Uh you can use

**[14:01]** commercial licensing. Uh you can use Crisp for free inside Pipcat cloud if

**[14:03]** Crisp for free inside Pipcat cloud if

**[14:03]** Crisp for free inside Pipcat cloud if you run on Pipcat cloud. You can also

**[14:04]** you run on Pipcat cloud. You can also

**[14:04]** you run on Pipcat cloud. You can also use Crisp in your own Pipcat pipelines

**[14:06]** use Crisp in your own Pipcat pipelines

**[14:06]** use Crisp in your own Pipcat pipelines with your own license if you run Crisp

**[14:08]** with your own license if you run Crisp

**[14:08]** with your own license if you run Crisp somewhere else. Uh finally, agents are

**[14:11]** somewhere else. Uh finally, agents are

**[14:11]** somewhere else. Uh finally, agents are nondeterministic as we all know. There's

**[14:12]** nondeterministic as we all know. There's

**[14:12]** nondeterministic as we all know. There's a whole eval and PM track here and in

**[14:15]** a whole eval and PM track here and in

**[14:15]** a whole eval and PM track here and in every other track we talk about this

**[14:16]** every other track we talk about this

**[14:16]** every other track we talk about this problem. Um, we've got some nice uh

**[14:19]** problem. Um, we've got some nice uh

**[14:19]** problem. Um, we've got some nice uh low-level building blocks for logging

**[14:21]** low-level building blocks for logging

**[14:21]** low-level building blocks for logging and observability natively in Pipcat and

**[14:23]** and observability natively in Pipcat and

**[14:23]** and observability natively in Pipcat and exposed through Pipcat Cloud and a bunch

**[14:25]** exposed through Pipcat Cloud and a bunch

**[14:25]** exposed through Pipcat Cloud and a bunch of partners we work with on that. I'm

**[14:27]** of partners we work with on that. I'm

**[14:27]** of partners we work with on that. I'm happy to introduce you to the great

**[14:29]** happy to introduce you to the great

**[14:29]** happy to introduce you to the great teams we work with at various companies

**[14:31]** teams we work with at various companies

**[14:31]** teams we work with at various companies that are building observability stuff.

**[14:33]** that are building observability stuff.

**[14:33]** that are building observability stuff. That is my speedrun. I came in 20

**[14:36]** That is my speedrun. I came in 20

**[14:36]** That is my speedrun. I came in 20 seconds under the 15 minutes, but

**[14:39]** seconds under the 15 minutes, but

**[14:39]** seconds under the 15 minutes, but because we are the last talk in this

**[14:41]** because we are the last talk in this

**[14:41]** because we are the last talk in this block, if people want to do Q&A, totally

**[14:44]** block, if people want to do Q&A, totally

**[14:44]** block, if people want to do Q&A, totally happy to.

**[14:53]** Thanks. Uh, wonderful. One, um, actually

**[14:53]** Thanks. Uh, wonderful. One, um, actually I have two questions, two very quick

**[14:54]** I have two questions, two very quick

**[14:54]** I have two questions, two very quick questions. One is we're based out of

**[14:57]** questions. One is we're based out of

**[14:57]** questions. One is we're based out of Sydney, Australia.

**[14:59]** Sydney, Australia.

**[14:59]** Sydney, Australia. 800 time


### [15:00 - 16:00]

**[15:02]** 800 time

**[15:02]** 800 time opening.

**[15:09]** Do you have any alternatives for that?

**[15:09]** Do you have any alternatives for that? Have you looked at other alternatives

**[15:10]** Have you looked at other alternatives

**[15:10]** Have you looked at other alternatives for people outside the states? Yes,

**[15:12]** for people outside the states? Yes,

**[15:12]** for people outside the states? Yes, that's a great question. So the question

**[15:13]** that's a great question. So the question

**[15:13]** that's a great question. So the question I will repeat the question. The question

**[15:15]** I will repeat the question. The question

**[15:15]** I will repeat the question. The question is if you're in a geography that is a

**[15:17]** is if you're in a geography that is a

**[15:17]** is if you're in a geography that is a long way from your inference servers. So

**[15:19]** long way from your inference servers. So

**[15:19]** long way from your inference servers. So in the case of this particular question,

**[15:21]** in the case of this particular question,

**[15:21]** in the case of this particular question, you're uh serving users in Australia.

**[15:23]** you're uh serving users in Australia.

**[15:23]** you're uh serving users in Australia. You're using OpenAI. Open AAI only has

**[15:25]** You're using OpenAI. Open AAI only has

**[15:25]** You're using OpenAI. Open AAI only has inference servers in the US. you don't

**[15:27]** inference servers in the US. you don't

**[15:27]** inference servers in the US. you don't want to make extra round trips to the

**[15:29]** want to make extra round trips to the

**[15:29]** want to make extra round trips to the US. So there's a couple answers to that.

**[15:32]** US. So there's a couple answers to that.

**[15:32]** US. So there's a couple answers to that. One is if you make one long haul to the

**[15:35]** One is if you make one long haul to the

**[15:35]** One is if you make one long haul to the US for all the audio that at the

**[15:38]** US for all the audio that at the

**[15:38]** US for all the audio that at the beginning of the chain and at the end of

**[15:39]** beginning of the chain and at the end of

**[15:39]** beginning of the chain and at the end of the chain that is much better than

**[15:41]** the chain that is much better than

**[15:41]** the chain that is much better than making three inference round trips for

**[15:43]** making three inference round trips for

**[15:43]** making three inference round trips for transcription, open AI and uh voice

**[15:46]** transcription, open AI and uh voice

**[15:46]** transcription, open AI and uh voice generation. So that's one tool we often

**[15:48]** generation. So that's one tool we often

**[15:48]** generation. So that's one tool we often say to people just deploy close to the

**[15:51]** say to people just deploy close to the

**[15:51]** say to people just deploy close to the inference servers rather than close to

**[15:52]** inference servers rather than close to

**[15:52]** inference servers rather than close to the users and optimize for having one

**[15:54]** the users and optimize for having one

**[15:54]** the users and optimize for having one long trip and then a bunch of very very

**[15:56]** long trip and then a bunch of very very

**[15:56]** long trip and then a bunch of very very fast short trips. That's good but not

**[15:59]** fast short trips. That's good but not

**[15:59]** fast short trips. That's good but not great. The other option is to run stuff


### [16:00 - 17:00]

**[16:02]** great. The other option is to run stuff

**[16:02]** great. The other option is to run stuff in uh on using open weights models

**[16:05]** in uh on using open weights models

**[16:05]** in uh on using open weights models locally in Australia which you can

**[16:07]** locally in Australia which you can

**[16:07]** locally in Australia which you can definitely do.

**[16:08]** definitely do.

**[16:08]** definitely do. It's a longer conversation about what

**[16:10]** It's a longer conversation about what

**[16:10]** It's a longer conversation about what use cases you can use, say the best open

**[16:12]** use cases you can use, say the best open

**[16:12]** use cases you can use, say the best open weights models versus the, you know,

**[16:15]** weights models versus the, you know,

**[16:15]** weights models versus the, you know, GPT40 and Gemini 2 flash uh level

**[16:18]** GPT40 and Gemini 2 flash uh level

**[16:18]** GPT40 and Gemini 2 flash uh level models. But there are definitely some

**[16:20]** models. But there are definitely some

**[16:20]** models. But there are definitely some voice AI workloads now that you can

**[16:22]** voice AI workloads now that you can

**[16:22]** voice AI workloads now that you can reliably run on like the Gemma or the

**[16:24]** reliably run on like the Gemma or the

**[16:24]** reliably run on like the Gemma or the Quinn 3 or the Llama 4 models. Okay.

**[16:26]** Quinn 3 or the Llama 4 models. Okay.

**[16:26]** Quinn 3 or the Llama 4 models. Okay. Second question maybe just related to

**[16:28]** Second question maybe just related to

**[16:28]** Second question maybe just related to that is let's say can we if we basically

**[16:31]** that is let's say can we if we basically

**[16:31]** that is let's say can we if we basically host models in Australia itself? Y um

**[16:34]** host models in Australia itself? Y um

**[16:34]** host models in Australia itself? Y um what's the interconnectivity over the

**[16:36]** what's the interconnectivity over the

**[16:36]** what's the interconnectivity over the network from your cloud by is something

**[16:38]** network from your cloud by is something

**[16:38]** network from your cloud by is something like do you go to like the internet

**[16:40]** like do you go to like the internet

**[16:40]** like do you go to like the internet exchange locally out there? Yes. So we

**[16:43]** exchange locally out there? Yes. So we

**[16:43]** exchange locally out there? Yes. So we have endpoints all over the world that

**[16:45]** have endpoints all over the world that

**[16:46]** have endpoints all over the world that are we in our world we call them points

**[16:47]** are we in our world we call them points

**[16:47]** are we in our world we call them points of presence. So we have the the sort of

**[16:49]** of presence. So we have the the sort of

**[16:49]** of presence. So we have the the sort of the edge server close to the user and

**[16:51]** the edge server close to the user and

**[16:51]** the edge server close to the user and we'll terminate the web RTC or the

**[16:52]** we'll terminate the web RTC or the

**[16:52]** we'll terminate the web RTC or the telefony connection there and then we'll

**[16:54]** telefony connection there and then we'll

**[16:54]** telefony connection there and then we'll route over our own private AWS or OCI

**[16:57]** route over our own private AWS or OCI

**[16:57]** route over our own private AWS or OCI backbones to wherever you need to route

**[16:59]** backbones to wherever you need to route

**[16:59]** backbones to wherever you need to route to. If you're hosting in Australia, uh


### [17:00 - 18:00]

**[17:02]** to. If you're hosting in Australia, uh

**[17:02]** to. If you're hosting in Australia, uh you should be able to just hit our

**[17:04]** you should be able to just hit our

**[17:04]** you should be able to just hit our endpoints and then uh your your hosting

**[17:07]** endpoints and then uh your your hosting

**[17:07]** endpoints and then uh your your hosting in Australia. We also we have some

**[17:10]** in Australia. We also we have some

**[17:10]** in Australia. We also we have some regional availability of Pipcat Cloud

**[17:12]** regional availability of Pipcat Cloud

**[17:12]** regional availability of Pipcat Cloud now. We will launch a bunch more

**[17:13]** now. We will launch a bunch more

**[17:13]** now. We will launch a bunch more regional availability of Pipcat Cloud

**[17:15]** regional availability of Pipcat Cloud

**[17:16]** regional availability of Pipcat Cloud over the next quarter. So I hope we

**[17:18]** over the next quarter. So I hope we

**[17:18]** over the next quarter. So I hope we actually have Pipcat Cloud in Australia

**[17:20]** actually have Pipcat Cloud in Australia

**[17:20]** actually have Pipcat Cloud in Australia soon. Although you you can also

**[17:22]** soon. Although you you can also

**[17:22]** soon. Although you you can also obviously self-host in Australia and

**[17:24]** obviously self-host in Australia and

**[17:24]** obviously self-host in Australia and still use either Pipcat itself or Pipcat

**[17:26]** still use either Pipcat itself or Pipcat

**[17:26]** still use either Pipcat itself or Pipcat Plus daily in other ways. Thank you.

**[17:29]** Plus daily in other ways. Thank you.

**[17:29]** Plus daily in other ways. Thank you. Yeah. Oh, sorry. Yeah. So, thanks.

**[17:32]** Yeah. Oh, sorry. Yeah. So, thanks.

**[17:32]** Yeah. Oh, sorry. Yeah. So, thanks. Thanks for the talk. Thank you. So,

**[17:33]** Thanks for the talk. Thank you. So,

**[17:33]** Thanks for the talk. Thank you. So, there are ones like Moshi. I don't know

**[17:35]** there are ones like Moshi. I don't know

**[17:35]** there are ones like Moshi. I don't know if you Yeah. Yeah. Yeah. I love Moshi.

**[17:37]** if you Yeah. Yeah. Yeah. I love Moshi.

**[17:37]** if you Yeah. Yeah. Yeah. I love Moshi. So, they basically claim that threat

**[17:39]** So, they basically claim that threat

**[17:39]** So, they basically claim that threat detection is no longer needed because

**[17:41]** detection is no longer needed because

**[17:41]** detection is no longer needed because they inher

**[17:53]** open weights model called Moshi by a

**[17:53]** open weights model called Moshi by a French lab called Kyoai. Um, Moshi is a

**[17:56]** French lab called Kyoai. Um, Moshi is a

**[17:56]** French lab called Kyoai. Um, Moshi is a is is a sort of next generation research

**[17:58]** is is a sort of next generation research

**[17:58]** is is a sort of next generation research model where the architecture is constant


### [18:00 - 19:00]

**[18:00]** model where the architecture is constant

**[18:00]** model where the architecture is constant birectional streaming. So, you're always

**[18:02]** birectional streaming. So, you're always

**[18:02]** birectional streaming. So, you're always streaming tokens in and the model is

**[18:04]** streaming tokens in and the model is

**[18:04]** streaming tokens in and the model is always streaming tokens out. In a

**[18:06]** always streaming tokens out. In a

**[18:06]** always streaming tokens out. In a conversational voice situation, which

**[18:08]** conversational voice situation, which

**[18:08]** conversational voice situation, which Moshi was designed for, most of the

**[18:10]** Moshi was designed for, most of the

**[18:10]** Moshi was designed for, most of the tokens streaming out are silence tokens

**[18:12]** tokens streaming out are silence tokens

**[18:12]** tokens streaming out are silence tokens of some kind. And when they're not

**[18:14]** of some kind. And when they're not

**[18:14]** of some kind. And when they're not silence tokens, it's because the model

**[18:15]** silence tokens, it's because the model

**[18:16]** silence tokens, it's because the model decided it was going to do whatever the

**[18:17]** decided it was going to do whatever the

**[18:17]** decided it was going to do whatever the model's trained to do, which is really

**[18:20]** model's trained to do, which is really

**[18:20]** model's trained to do, which is really cool because that can mean not just that

**[18:22]** cool because that can mean not just that

**[18:22]** cool because that can mean not just that the model does natural turn taking, but

**[18:24]** the model does natural turn taking, but

**[18:24]** the model does natural turn taking, but also that the model can do things like

**[18:26]** also that the model can do things like

**[18:26]** also that the model can do things like back channeling. So the model can do the

**[18:28]** back channeling. So the model can do the

**[18:28]** back channeling. So the model can do the things the humans do, that it's data set

**[18:31]** things the humans do, that it's data set

**[18:31]** things the humans do, that it's data set has audio for like when you're talking,

**[18:33]** has audio for like when you're talking,

**[18:33]** has audio for like when you're talking, I can say, uh, yeah, yeah, uh, and it's

**[18:37]** I can say, uh, yeah, yeah, uh, and it's

**[18:37]** I can say, uh, yeah, yeah, uh, and it's not actually a new inference call, it's

**[18:39]** not actually a new inference call, it's

**[18:39]** not actually a new inference call, it's just streaming. um that paper, the the

**[18:43]** just streaming. um that paper, the the

**[18:43]** just streaming. um that paper, the the Kyoi Labs Moshi architecture paper was

**[18:45]** Kyoi Labs Moshi architecture paper was

**[18:45]** Kyoi Labs Moshi architecture paper was my very favorite ML research paper from

**[18:47]** my very favorite ML research paper from

**[18:47]** my very favorite ML research paper from last year. Now that model itself is not

**[18:51]** last year. Now that model itself is not

**[18:51]** last year. Now that model itself is not usable in production for a bunch of

**[18:53]** usable in production for a bunch of

**[18:53]** usable in production for a bunch of reasons, including that it is too small

**[18:55]** reasons, including that it is too small

**[18:56]** reasons, including that it is too small a language model to be useful for

**[18:59]** a language model to be useful for

**[18:59]** a language model to be useful for basically any real world use case. Um,


### [19:00 - 20:00]

**[19:04]** basically any real world use case. Um,

**[19:04]** basically any real world use case. Um, I I have more to say about that, but I'm

**[19:06]** I I have more to say about that, but I'm

**[19:06]** I I have more to say about that, but I'm super super excited about that

**[19:07]** super super excited about that

**[19:07]** super super excited about that architecture, but I don't think I mean,

**[19:09]** architecture, but I don't think I mean,

**[19:09]** architecture, but I don't think I mean, we're a couple years away from that

**[19:10]** we're a couple years away from that

**[19:10]** we're a couple years away from that architecture being actually usable and

**[19:13]** architecture being actually usable and

**[19:14]** architecture being actually usable and trained as a production model. There are

**[19:16]** trained as a production model. There are

**[19:16]** trained as a production model. There are speech-to-pech models from the from the

**[19:18]** speech-to-pech models from the from the

**[19:18]** speech-to-pech models from the from the large labs that are closer to being able

**[19:20]** large labs that are closer to being able

**[19:20]** large labs that are closer to being able to be used in production. Uh, now they

**[19:23]** to be used in production. Uh, now they

**[19:23]** to be used in production. Uh, now they are not streaming architecture models,

**[19:25]** are not streaming architecture models,

**[19:25]** are not streaming architecture models, but they are native audio speech-to-pech

**[19:27]** but they are native audio speech-to-pech

**[19:27]** but they are native audio speech-to-pech models, which have a bunch of

**[19:29]** models, which have a bunch of

**[19:29]** models, which have a bunch of advantages, including really great

**[19:30]** advantages, including really great

**[19:30]** advantages, including really great multilingual support. So like mixed

**[19:32]** multilingual support. So like mixed

**[19:32]** multilingual support. So like mixed language stuff is great from those

**[19:33]** language stuff is great from those

**[19:33]** language stuff is great from those models. Um in theory latency reductions.

**[19:37]** models. Um in theory latency reductions.

**[19:37]** models. Um in theory latency reductions. Um so OpenAI has a a real-time model

**[19:40]** Um so OpenAI has a a real-time model

**[19:40]** Um so OpenAI has a a real-time model called GPT4 audio preview that sits

**[19:44]** called GPT4 audio preview that sits

**[19:44]** called GPT4 audio preview that sits behind their real-time API. It's a it's

**[19:46]** behind their real-time API. It's a it's

**[19:46]** behind their real-time API. It's a it's a good model. Uh Gemini 20 flash uh is

**[19:49]** a good model. Uh Gemini 20 flash uh is

**[19:49]** a good model. Uh Gemini 20 flash uh is available in an audioto audio mode and

**[19:52]** available in an audioto audio mode and

**[19:52]** available in an audioto audio mode and their training to or their they have

**[19:53]** their training to or their they have

**[19:54]** their training to or their they have preview releases of 25 flash. These

**[19:56]** preview releases of 25 flash. These

**[19:56]** preview releases of 25 flash. These models are now good enough that you can

**[19:58]** models are now good enough that you can

**[19:58]** models are now good enough that you can use them for use cases where you are


### [20:00 - 21:00]

**[20:00]** use them for use cases where you are

**[20:00]** use them for use cases where you are more concerned about naturalness of the

**[20:02]** more concerned about naturalness of the

**[20:02]** more concerned about naturalness of the human conversation than you are about

**[20:04]** human conversation than you are about

**[20:04]** human conversation than you are about reliable instruction following and

**[20:05]** reliable instruction following and

**[20:05]** reliable instruction following and function calling. They are less reliable

**[20:08]** function calling. They are less reliable

**[20:08]** function calling. They are less reliable in audio mode than the text mode that

**[20:11]** in audio mode than the text mode that

**[20:11]** in audio mode than the text mode that the soda models operating in text mode.

**[20:13]** the soda models operating in text mode.

**[20:13]** the soda models operating in text mode. So what we generally see is that for a

**[20:15]** So what we generally see is that for a

**[20:15]** So what we generally see is that for a small subset of voice AI use cases today

**[20:17]** small subset of voice AI use cases today

**[20:17]** small subset of voice AI use cases today that are really about like

**[20:19]** that are really about like

**[20:19]** that are really about like conversational dynamics, narrative,

**[20:22]** conversational dynamics, narrative,

**[20:22]** conversational dynamics, narrative, storytelling, those models are starting

**[20:24]** storytelling, those models are starting

**[20:24]** storytelling, those models are starting to get adopted for the majority of sort

**[20:27]** to get adopted for the majority of sort

**[20:27]** to get adopted for the majority of sort of enterprise voice AI use cases where

**[20:29]** of enterprise voice AI use cases where

**[20:29]** of enterprise voice AI use cases where you really need best possible

**[20:31]** you really need best possible

**[20:31]** you really need best possible instruction following and function

**[20:33]** instruction following and function

**[20:33]** instruction following and function calling. Those models are not yet the

**[20:34]** calling. Those models are not yet the

**[20:34]** calling. Those models are not yet the right choice but they are getting better

**[20:36]** right choice but they are getting better

**[20:36]** right choice but they are getting better every release and all of us expect the

**[20:38]** every release and all of us expect the

**[20:38]** every release and all of us expect the world to move to speechtoech models

**[20:40]** world to move to speechtoech models

**[20:40]** world to move to speechtoech models being the default for like 95% of voice

**[20:43]** being the default for like 95% of voice

**[20:43]** being the default for like 95% of voice AI sometime in the next two years. The

**[20:45]** AI sometime in the next two years. The

**[20:45]** AI sometime in the next two years. The question is when in your use case will a

**[20:48]** question is when in your use case will a

**[20:48]** question is when in your use case will a particular model architecture sort of

**[20:50]** particular model architecture sort of

**[20:50]** particular model architecture sort of cross that threshold in your evals.

**[20:51]** cross that threshold in your evals.

**[20:51]** cross that threshold in your evals. Sorry what about sesame? You put sesame

**[20:53]** Sorry what about sesame? You put sesame

**[20:53]** Sorry what about sesame? You put sesame in the same bucket as Gemini and open

**[20:56]** in the same bucket as Gemini and open

**[20:56]** in the same bucket as Gemini and open sesame is closer to Moshi. In fact,

**[20:59]** sesame is closer to Moshi. In fact,

**[20:59]** sesame is closer to Moshi. In fact, Sesame. So, there's another open uh


### [21:00 - 22:00]

**[21:02]** Sesame. So, there's another open uh

**[21:02]** Sesame. So, there's another open uh weights or partly open weights and

**[21:04]** weights or partly open weights and

**[21:04]** weights or partly open weights and really interesting model called sesame.

**[21:06]** really interesting model called sesame.

**[21:06]** really interesting model called sesame. Uh it's a little like Moshi. It in fact

**[21:08]** Uh it's a little like Moshi. It in fact

**[21:08]** Uh it's a little like Moshi. It in fact uses the Moshi neural encoder. Yeah, it

**[21:11]** uses the Moshi neural encoder. Yeah, it

**[21:11]** uses the Moshi neural encoder. Yeah, it uses Mimi. Um

**[21:15]** uses Mimi. Um

**[21:15]** uses Mimi. Um ses So, Sesame has not yet been fully

**[21:17]** ses So, Sesame has not yet been fully

**[21:17]** ses So, Sesame has not yet been fully released. There isn't a full Sesame

**[21:18]** released. There isn't a full Sesame

**[21:18]** released. There isn't a full Sesame release. Uh also, I think Sesame is

**[21:22]** release. Uh also, I think Sesame is

**[21:22]** release. Uh also, I think Sesame is smaller than probably you would need to

**[21:24]** smaller than probably you would need to

**[21:24]** smaller than probably you would need to use for most enterprise use cases today.

**[21:27]** use for most enterprise use cases today.

**[21:27]** use for most enterprise use cases today. Although the lab training Sesame I think

**[21:29]** Although the lab training Sesame I think

**[21:29]** Although the lab training Sesame I think has bigger versions coming. Uh there's

**[21:32]** has bigger versions coming. Uh there's

**[21:32]** has bigger versions coming. Uh there's also a speech-to-spech model called

**[21:33]** also a speech-to-spech model called

**[21:33]** also a speech-to-spech model called Ultravox which is really good which is

**[21:35]** Ultravox which is really good which is

**[21:35]** Ultravox which is really good which is trained on the Llama 37B backbone and

**[21:37]** trained on the Llama 37B backbone and

**[21:37]** trained on the Llama 37B backbone and that team supports that model and has a

**[21:39]** that team supports that model and has a

**[21:40]** that team supports that model and has a production voice AI API. That model is

**[21:42]** production voice AI API. That model is

**[21:42]** production voice AI API. That model is worth trying if you are really

**[21:44]** worth trying if you are really

**[21:44]** worth trying if you are really interested in speechtoech models. If

**[21:47]** interested in speechtoech models. If

**[21:47]** interested in speechtoech models. If Llama 370B can do what you want, I think

**[21:49]** Llama 370B can do what you want, I think

**[21:49]** Llama 370B can do what you want, I think Ultravox is a good choice. If Llama 37B

**[21:52]** Ultravox is a good choice. If Llama 37B

**[21:52]** Ultravox is a good choice. If Llama 37B isn't quite there for your use case,

**[21:54]** isn't quite there for your use case,

**[21:54]** isn't quite there for your use case, probably not. but you know the next

**[21:55]** probably not. but you know the next

**[21:55]** probably not. but you know the next release of ultravio so speech to speech

**[21:57]** release of ultravio so speech to speech

**[21:57]** release of ultravio so speech to speech is definitely the future I I generally

**[21:59]** is definitely the future I I generally

**[21:59]** is definitely the future I I generally tell people experiment with it don't


### [22:00 - 23:00]

**[22:02]** tell people experiment with it don't

**[22:02]** tell people experiment with it don't necessarily start assuming you're going

**[22:03]** necessarily start assuming you're going

**[22:03]** necessarily start assuming you're going to use it for your enterprise use case

**[22:05]** to use it for your enterprise use case

**[22:05]** to use it for your enterprise use case though today

**[22:07]** though today

**[22:07]** though today given your v vendor neutrality can you

**[22:10]** given your v vendor neutrality can you

**[22:10]** given your v vendor neutrality can you speak to the strengths and weaknesses of

**[22:13]** speak to the strengths and weaknesses of

**[22:13]** speak to the strengths and weaknesses of using like the leading edge uh

**[22:15]** using like the leading edge uh

**[22:15]** using like the leading edge uh multimodal input models like open AAI

**[22:18]** multimodal input models like open AAI

**[22:18]** multimodal input models like open AAI and Gemini when when should I use choose

**[22:21]** and Gemini when when should I use choose

**[22:21]** and Gemini when when should I use choose open AI or when should I choose Gemini

**[22:24]** open AI or when should I choose Gemini

**[22:24]** open AI or when should I choose Gemini So my opinion is that GPT40 in text mode

**[22:28]** So my opinion is that GPT40 in text mode

**[22:28]** So my opinion is that GPT40 in text mode and Gemini 20 flash in text mode are

**[22:32]** and Gemini 20 flash in text mode are

**[22:32]** and Gemini 20 flash in text mode are roughly equivalent models for the use

**[22:33]** roughly equivalent models for the use

**[22:34]** roughly equivalent models for the use cases that I test every day. Um so I

**[22:37]** cases that I test every day. Um so I

**[22:37]** cases that I test every day. Um so I would make the decision if you can I

**[22:41]** would make the decision if you can I

**[22:41]** would make the decision if you can I would build a pipecap pipeline and then

**[22:43]** would build a pipecap pipeline and then

**[22:43]** would build a pipecap pipeline and then just swap the two models and run your

**[22:45]** just swap the two models and run your

**[22:45]** just swap the two models and run your evals. Um because they're both really

**[22:47]** evals. Um because they're both really

**[22:47]** evals. Um because they're both really good models. One of the advantages of

**[22:49]** good models. One of the advantages of

**[22:49]** good models. One of the advantages of Gemini is that it's extremely

**[22:51]** Gemini is that it's extremely

**[22:51]** Gemini is that it's extremely aggressively priced. So,

**[22:54]** aggressively priced. So,

**[22:54]** aggressively priced. So, you know, a a a 30-minute conversation

**[22:56]** you know, a a a 30-minute conversation

**[22:56]** you know, a a a 30-minute conversation on Gemini is probably 10 times cheaper

**[22:59]** on Gemini is probably 10 times cheaper

**[22:59]** on Gemini is probably 10 times cheaper than a 30-minute conversation on GPT40.


### [23:00 - 24:00]

**[23:02]** than a 30-minute conversation on GPT40.

**[23:02]** than a 30-minute conversation on GPT40. Um, you know, that may or may not stay

**[23:04]** Um, you know, that may or may not stay

**[23:04]** Um, you know, that may or may not stay true as they both change their prices.

**[23:06]** true as they both change their prices.

**[23:06]** true as they both change their prices. But that's definitely something we hear

**[23:07]** But that's definitely something we hear

**[23:07]** But that's definitely something we hear a lot from customers today is that they

**[23:09]** a lot from customers today is that they

**[23:09]** a lot from customers today is that they like the pricing of Gemini. The other

**[23:11]** like the pricing of Gemini. The other

**[23:11]** like the pricing of Gemini. The other interesting thing about Gemini is that

**[23:12]** interesting thing about Gemini is that

**[23:12]** interesting thing about Gemini is that it operates in native audio input mode

**[23:15]** it operates in native audio input mode

**[23:16]** it operates in native audio input mode very well. So you can use Gemini native

**[23:18]** very well. So you can use Gemini native

**[23:18]** very well. So you can use Gemini native audio input mode and then text output

**[23:21]** audio input mode and then text output

**[23:21]** audio input mode and then text output mode in a pipeline and that has

**[23:23]** mode in a pipeline and that has

**[23:23]** mode in a pipeline and that has advantages for some use cases and some

**[23:25]** advantages for some use cases and some

**[23:25]** advantages for some use cases and some languages and you can again test that on

**[23:27]** languages and you can again test that on

**[23:27]** languages and you can again test that on your eval. And OpenAI also has native

**[23:30]** your eval. And OpenAI also has native

**[23:30]** your eval. And OpenAI also has native audio support in some of their newer

**[23:31]** audio support in some of their newer

**[23:31]** audio support in some of their newer models but I I think they're just a

**[23:33]** models but I I think they're just a

**[23:33]** models but I I think they're just a little bit behind the Gemini models in

**[23:35]** little bit behind the Gemini models in

**[23:35]** little bit behind the Gemini models in that uh in that regard. Um time for one

**[23:38]** that uh in that regard. Um time for one

**[23:38]** that uh in that regard. Um time for one more or we done one more and then we're

**[23:41]** more or we done one more and then we're

**[23:41]** more or we done one more and then we're done. Yeah. What are the general

**[23:43]** done. Yeah. What are the general

**[23:43]** done. Yeah. What are the general advantages of speech to speech versus

**[23:45]** advantages of speech to speech versus

**[23:45]** advantages of speech to speech versus going speech to text doing something and

**[23:48]** going speech to text doing something and

**[23:48]** going speech to text doing something and then fact text to speech. So what are

**[23:50]** then fact text to speech. So what are

**[23:50]** then fact text to speech. So what are the general advantages of speech to

**[23:52]** the general advantages of speech to

**[23:52]** the general advantages of speech to speech instead of text text inference uh

**[23:55]** speech instead of text text inference uh

**[23:55]** speech instead of text text inference uh to speech and out? So it's super

**[23:58]** to speech and out? So it's super

**[23:58]** to speech and out? So it's super interesting question and I have a like a


### [24:00 - 25:00]

**[24:00]** interesting question and I have a like a

**[24:00]** interesting question and I have a like a a practical answer and a philosophical

**[24:01]** a practical answer and a philosophical

**[24:01]** a practical answer and a philosophical answer. I'll keep them both short. The

**[24:03]** answer. I'll keep them both short. The

**[24:03]** answer. I'll keep them both short. The the the practical answer is that you

**[24:06]** the the practical answer is that you

**[24:06]** the the practical answer is that you lose information when you transcribe.

**[24:09]** lose information when you transcribe.

**[24:09]** lose information when you transcribe. And so if there's information that's

**[24:11]** And so if there's information that's

**[24:11]** And so if there's information that's useful in the um in the transcription

**[24:15]** useful in the um in the transcription

**[24:15]** useful in the um in the transcription step that if there's information in the

**[24:16]** step that if there's information in the

**[24:16]** step that if there's information in the audio that you would lose that's useful

**[24:18]** audio that you would lose that's useful

**[24:18]** audio that you would lose that's useful for your use case then a speechto speech

**[24:19]** for your use case then a speechto speech

**[24:20]** for your use case then a speechto speech model is great. Um so for example things

**[24:22]** model is great. Um so for example things

**[24:22]** model is great. Um so for example things like mixed language are very hard for

**[24:24]** like mixed language are very hard for

**[24:24]** like mixed language are very hard for small transcription models. Um you're

**[24:26]** small transcription models. Um you're

**[24:26]** small transcription models. Um you're almost always sort of losing a bunch

**[24:28]** almost always sort of losing a bunch

**[24:28]** almost always sort of losing a bunch more information in a mixed language

**[24:29]** more information in a mixed language

**[24:29]** more information in a mixed language transcription than you are in like a an

**[24:31]** transcription than you are in like a an

**[24:31]** transcription than you are in like a an optimized model monolingual

**[24:33]** optimized model monolingual

**[24:33]** optimized model monolingual transcription. So why not go to the big

**[24:35]** transcription. So why not go to the big

**[24:35]** transcription. So why not go to the big LLM that just has all this like language

**[24:37]** LLM that just has all this like language

**[24:37]** LLM that just has all this like language knowledge and can do a better job on the

**[24:38]** knowledge and can do a better job on the

**[24:38]** knowledge and can do a better job on the multilingual input. Um the other

**[24:41]** multilingual input. Um the other

**[24:41]** multilingual input. Um the other advantage is potentially you have lower

**[24:42]** advantage is potentially you have lower

**[24:42]** advantage is potentially you have lower latency like if you're if you've trained

**[24:44]** latency like if you're if you've trained

**[24:44]** latency like if you're if you've trained an end toend model for speech to speech

**[24:46]** an end toend model for speech to speech

**[24:46]** an end toend model for speech to speech and it's all one model and you're not

**[24:47]** and it's all one model and you're not

**[24:47]** and it's all one model and you're not like chaining together inference calls

**[24:49]** like chaining together inference calls

**[24:49]** like chaining together inference calls you you can probably get lower latency.

**[24:51]** you you can probably get lower latency.

**[24:51]** you you can probably get lower latency. Uh in practice whether that's true today

**[24:53]** Uh in practice whether that's true today

**[24:53]** Uh in practice whether that's true today depends more on the sort of APIs and

**[24:54]** depends more on the sort of APIs and

**[24:54]** depends more on the sort of APIs and inference stack than it does on the

**[24:55]** inference stack than it does on the

**[24:55]** inference stack than it does on the model architecture. But I think we're

**[24:57]** model architecture. But I think we're

**[24:57]** model architecture. But I think we're all going towards assuming that we just

**[24:59]** all going towards assuming that we just

**[24:59]** all going towards assuming that we just want to do one inference call for like


### [25:00 - 26:00]

**[25:01]** want to do one inference call for like

**[25:01]** want to do one inference call for like the bulk of things and then we might use

**[25:03]** the bulk of things and then we might use

**[25:03]** the bulk of things and then we might use other little models on the side for for

**[25:04]** other little models on the side for for

**[25:04]** other little models on the side for for like subsets. The philosophical answer

**[25:07]** like subsets. The philosophical answer

**[25:07]** like subsets. The philosophical answer though is that those advantages are

**[25:09]** though is that those advantages are

**[25:09]** though is that those advantages are probably outweighed by the challenges to

**[25:11]** probably outweighed by the challenges to

**[25:12]** probably outweighed by the challenges to today's LLM's architecture LLM

**[25:13]** today's LLM's architecture LLM

**[25:13]** today's LLM's architecture LLM architectures when you have big context

**[25:16]** architectures when you have big context

**[25:16]** architectures when you have big context and big context and audio tokens take up

**[25:19]** and big context and audio tokens take up

**[25:19]** and big context and audio tokens take up a lot of context tokens. So when you're

**[25:21]** a lot of context tokens. So when you're

**[25:21]** a lot of context tokens. So when you're operating in audio mode, you're just

**[25:22]** operating in audio mode, you're just

**[25:22]** operating in audio mode, you're just sort of expanding the context massively

**[25:24]** sort of expanding the context massively

**[25:24]** sort of expanding the context massively relative to operating in text mode. And

**[25:26]** relative to operating in text mode. And

**[25:26]** relative to operating in text mode. And that tends to degrade the performance of

**[25:28]** that tends to degrade the performance of

**[25:28]** that tends to degrade the performance of the model. I think a little bit

**[25:30]** the model. I think a little bit

**[25:30]** the model. I think a little bit relatedly, nobody has as much audio data

**[25:32]** relatedly, nobody has as much audio data

**[25:32]** relatedly, nobody has as much audio data as they have text data for training. So

**[25:35]** as they have text data for training. So

**[25:35]** as they have text data for training. So even though a big model is doing a bunch

**[25:37]** even though a big model is doing a bunch

**[25:37]** even though a big model is doing a bunch of transfer learning, when you give it a

**[25:39]** of transfer learning, when you give it a

**[25:39]** of transfer learning, when you give it a bunch of audio and it is in theory sort

**[25:41]** bunch of audio and it is in theory sort

**[25:42]** bunch of audio and it is in theory sort of mapping all that audio to the same

**[25:43]** of mapping all that audio to the same

**[25:43]** of mapping all that audio to the same latent space as its text reasoning, in

**[25:45]** latent space as its text reasoning, in

**[25:45]** latent space as its text reasoning, in practice, it's definitely not doing that

**[25:47]** practice, it's definitely not doing that

**[25:47]** practice, it's definitely not doing that exactly. It's doing something like that,

**[25:50]** exactly. It's doing something like that,

**[25:50]** exactly. It's doing something like that, but not that. And so because we don't

**[25:52]** but not that. And so because we don't

**[25:52]** but not that. And so because we don't have as much audio data, you see a lot

**[25:54]** have as much audio data, you see a lot

**[25:54]** have as much audio data, you see a lot of issues with audioto audio models like

**[25:57]** of issues with audioto audio models like

**[25:57]** of issues with audioto audio models like the model will sometimes just respond in

**[25:59]** the model will sometimes just respond in

**[25:59]** the model will sometimes just respond in a totally different language. And that's


### [26:00 - 27:00]

**[26:02]** a totally different language. And that's

**[26:02]** a totally different language. And that's cool, but it's never what you want in

**[26:04]** cool, but it's never what you want in

**[26:04]** cool, but it's never what you want in the enterprise, you know, voice AI use

**[26:06]** the enterprise, you know, voice AI use

**[26:06]** the enterprise, you know, voice AI use case. And the best guess for why that's

**[26:09]** case. And the best guess for why that's

**[26:09]** case. And the best guess for why that's happening is it's in some right part of

**[26:13]** happening is it's in some right part of

**[26:13]** happening is it's in some right part of the latent space from some projection

**[26:15]** the latent space from some projection

**[26:15]** the latent space from some projection but then from some other projection it's

**[26:17]** but then from some other projection it's

**[26:17]** but then from some other projection it's totally in a different part of the

**[26:18]** totally in a different part of the

**[26:18]** totally in a different part of the latent space when you gave it audio

**[26:19]** latent space when you gave it audio

**[26:19]** latent space when you gave it audio instead of text even though if you

**[26:21]** instead of text even though if you

**[26:21]** instead of text even though if you transcribe that text it would be exactly

**[26:23]** transcribe that text it would be exactly

**[26:23]** transcribe that text it would be exactly the same as the audio. Um so you know

**[26:26]** the same as the audio. Um so you know

**[26:26]** the same as the audio. Um so you know latent spaces are big and to like

**[26:29]** latent spaces are big and to like

**[26:29]** latent spaces are big and to like actually find our way through them in

**[26:31]** actually find our way through them in

**[26:31]** actually find our way through them in post training you really have to have a

**[26:33]** post training you really have to have a

**[26:33]** post training you really have to have a lot of data and nobody has enough audio

**[26:35]** lot of data and nobody has enough audio

**[26:35]** lot of data and nobody has enough audio data yet. But the big labs are going to

**[26:37]** data yet. But the big labs are going to

**[26:37]** data yet. But the big labs are going to fix that cuz audio matters and

**[26:39]** fix that cuz audio matters and

**[26:39]** fix that cuz audio matters and multi-turn conversations matter.


