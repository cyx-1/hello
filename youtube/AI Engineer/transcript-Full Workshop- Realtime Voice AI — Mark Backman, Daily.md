# Full Workshop- Realtime Voice AI — Mark Backman, Daily

**Video URL:** https://www.youtube.com/watch?v=nxuTVd7v7dg

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** I'm Mark with Daily. This is Alles.

**[00:17]** I'm Mark with Daily. This is Alles. Alish. And then we have a few other

**[00:19]** Alish. And then we have a few other

**[00:19]** Alish. And then we have a few other daily folks. uh Quinn, Nina, Verun, and

**[00:24]** daily folks. uh Quinn, Nina, Verun, and

**[00:24]** daily folks. uh Quinn, Nina, Verun, and then I'm not sure where he went, but

**[00:26]** then I'm not sure where he went, but

**[00:26]** then I'm not sure where he went, but Philip from right there from the Google

**[00:28]** Philip from right there from the Google

**[00:28]** Philip from right there from the Google team, Google DeepMind team. So, this

**[00:31]** team, Google DeepMind team. So, this

**[00:31]** team, Google DeepMind team. So, this session we're going to spend just a few

**[00:32]** session we're going to spend just a few

**[00:32]** session we're going to spend just a few minutes getting everyone started. The

**[00:34]** minutes getting everyone started. The

**[00:34]** minutes getting everyone started. The idea here is going to be a hands-on

**[00:35]** idea here is going to be a hands-on

**[00:35]** idea here is going to be a hands-on workshop where all the folks I just

**[00:38]** workshop where all the folks I just

**[00:38]** workshop where all the folks I just called out are going to be available to

**[00:39]** called out are going to be available to

**[00:39]** called out are going to be available to help out. We'll walk you through a quick

**[00:42]** help out. We'll walk you through a quick

**[00:42]** help out. We'll walk you through a quick start to get you up and running and then

**[00:44]** start to get you up and running and then

**[00:44]** start to get you up and running and then the idea is to build something. So,

**[00:45]** the idea is to build something. So,

**[00:45]** the idea is to build something. So, build a voice bot in the next 78 minutes

**[00:48]** build a voice bot in the next 78 minutes

**[00:48]** build a voice bot in the next 78 minutes and 12 seconds or whatever time we have

**[00:50]** and 12 seconds or whatever time we have

**[00:50]** and 12 seconds or whatever time we have left. Um, the one I guess there's one uh

**[00:55]** left. Um, the one I guess there's one uh

**[00:55]** left. Um, the one I guess there's one uh consideration is the Wi-Fi. If you don't

**[00:57]** consideration is the Wi-Fi. If you don't

**[00:57]** consideration is the Wi-Fi. If you don't have good Wi-Fi, you might want to try

**[00:58]** have good Wi-Fi, you might want to try

**[00:58]** have good Wi-Fi, you might want to try to tether. I was able to tether and it


### [01:00 - 02:00]

**[01:01]** to tether. I was able to tether and it

**[01:01]** to tether. I was able to tether and it worked fairly well, but the conference

**[01:02]** worked fairly well, but the conference

**[01:02]** worked fairly well, but the conference Wi-Fi was a little shaky. This is real

**[01:04]** Wi-Fi was a little shaky. This is real

**[01:04]** Wi-Fi was a little shaky. This is real time, so you will be streaming data. It

**[01:07]** time, so you will be streaming data. It

**[01:07]** time, so you will be streaming data. It does require a viable connection and not

**[01:09]** does require a viable connection and not

**[01:09]** does require a viable connection and not just sending, you know, a few bits over.

**[01:11]** just sending, you know, a few bits over.

**[01:11]** just sending, you know, a few bits over. So, just a heads up if you hit that as a

**[01:14]** So, just a heads up if you hit that as a

**[01:14]** So, just a heads up if you hit that as a as a snag. So, I guess before I get

**[01:17]** as a snag. So, I guess before I get

**[01:17]** as a snag. So, I guess before I get started, who here knows about Pipecat or

**[01:20]** started, who here knows about Pipecat or

**[01:20]** started, who here knows about Pipecat or has built anything with voice AI?

**[01:23]** has built anything with voice AI?

**[01:23]** has built anything with voice AI? Okay,

**[01:25]** Okay,

**[01:25]** Okay, a smaller audience. Has anyone built any

**[01:27]** a smaller audience. Has anyone built any

**[01:27]** a smaller audience. Has anyone built any real-time applications with LLMs or AI?

**[01:32]** real-time applications with LLMs or AI?

**[01:32]** real-time applications with LLMs or AI? Maybe slightly bigger. Okay, great. So,

**[01:35]** Maybe slightly bigger. Okay, great. So,

**[01:35]** Maybe slightly bigger. Okay, great. So, Pipcat um is a uh it's a open source

**[01:41]** Pipcat um is a uh it's a open source

**[01:41]** Pipcat um is a uh it's a open source repo. It's a Python framework for

**[01:42]** repo. It's a Python framework for

**[01:42]** repo. It's a Python framework for building voice and AI multimodal agents

**[01:45]** building voice and AI multimodal agents

**[01:46]** building voice and AI multimodal agents and it's built by the team at Daily. Um

**[01:48]** and it's built by the team at Daily. Um

**[01:48]** and it's built by the team at Daily. Um but we're an open source it's an open

**[01:50]** but we're an open source it's an open

**[01:50]** but we're an open source it's an open source project that anyone can

**[01:51]** source project that anyone can

**[01:52]** source project that anyone can contribute to. It's been around for I

**[01:54]** contribute to. It's been around for I

**[01:54]** contribute to. It's been around for I don't know just over a year now. And

**[01:57]** don't know just over a year now. And

**[01:57]** don't know just over a year now. And yeah, like I would say officially

**[01:59]** yeah, like I would say officially

**[01:59]** yeah, like I would say officially Pipecat was March 2024 something like


### [02:00 - 03:00]

**[02:03]** Pipecat was March 2024 something like

**[02:03]** Pipecat was March 2024 something like that. So 13 months. There we go. So just

**[02:06]** that. So 13 months. There we go. So just

**[02:06]** that. So 13 months. There we go. So just a quick uh walk through maybe just to

**[02:08]** a quick uh walk through maybe just to

**[02:08]** a quick uh walk through maybe just to kind of ground everyone in the thinking

**[02:10]** kind of ground everyone in the thinking

**[02:10]** kind of ground everyone in the thinking around voice AI. Uh these slides weren't

**[02:13]** around voice AI. Uh these slides weren't

**[02:13]** around voice AI. Uh these slides weren't built for this talk but I'm going to use

**[02:14]** built for this talk but I'm going to use

**[02:14]** built for this talk but I'm going to use them. So the you know voice AI or

**[02:17]** them. So the you know voice AI or

**[02:17]** them. So the you know voice AI or real-time applications are tough because

**[02:19]** real-time applications are tough because

**[02:19]** real-time applications are tough because there's just you know we as humans

**[02:20]** there's just you know we as humans

**[02:20]** there's just you know we as humans communicate all the time with each

**[02:22]** communicate all the time with each

**[02:22]** communicate all the time with each other. Thousands tens of thousands of

**[02:24]** other. Thousands tens of thousands of

**[02:24]** other. Thousands tens of thousands of years of evolution baked into our

**[02:26]** years of evolution baked into our

**[02:26]** years of evolution baked into our brains. So it's pretty tough to make a

**[02:29]** brains. So it's pretty tough to make a

**[02:29]** brains. So it's pretty tough to make a machine you know work on the same level.

**[02:31]** machine you know work on the same level.

**[02:31]** machine you know work on the same level. So we have great expectations being the

**[02:32]** So we have great expectations being the

**[02:32]** So we have great expectations being the user in it. So you know you need a good

**[02:34]** user in it. So you know you need a good

**[02:34]** user in it. So you know you need a good listener something that is smart and

**[02:36]** listener something that is smart and

**[02:36]** listener something that is smart and conversational. You need to be connected

**[02:38]** conversational. You need to be connected

**[02:38]** conversational. You need to be connected to data stores. Uh has to sound normal

**[02:41]** to data stores. Uh has to sound normal

**[02:41]** to data stores. Uh has to sound normal or natural. Think back to even just

**[02:43]** or natural. Think back to even just

**[02:43]** or natural. Think back to even just maybe two three years ago what your

**[02:45]** maybe two three years ago what your

**[02:45]** maybe two three years ago what your voice bots sound like and many of them

**[02:47]** voice bots sound like and many of them

**[02:47]** voice bots sound like and many of them on if you call them on the phone still

**[02:48]** on if you call them on the phone still

**[02:48]** on if you call them on the phone still sound like. Needs to sound natural. And

**[02:50]** sound like. Needs to sound natural. And

**[02:50]** sound like. Needs to sound natural. And actually kudos to the Google team. The

**[02:53]** actually kudos to the Google team. The

**[02:53]** actually kudos to the Google team. The latest uh Gemini live uh native audio

**[02:56]** latest uh Gemini live uh native audio

**[02:56]** latest uh Gemini live uh native audio dialogue is quite good in that regard.


### [03:00 - 04:00]

**[03:00]** dialogue is quite good in that regard.

**[03:00]** dialogue is quite good in that regard. it has to be fast. So the whole end to

**[03:02]** it has to be fast. So the whole end to

**[03:02]** it has to be fast. So the whole end to end communication needs to happen and

**[03:04]** end communication needs to happen and

**[03:04]** end communication needs to happen and roughly you know kind of the benchmark

**[03:06]** roughly you know kind of the benchmark

**[03:06]** roughly you know kind of the benchmark is around 800 milliseconds. Um you could

**[03:10]** is around 800 milliseconds. Um you could

**[03:10]** is around 800 milliseconds. Um you could strive for more. I think we see maybe on

**[03:12]** strive for more. I think we see maybe on

**[03:12]** strive for more. I think we see maybe on the human level it might be 500

**[03:14]** the human level it might be 500

**[03:14]** the human level it might be 500 milliseconds or somewhere on that uh

**[03:16]** milliseconds or somewhere on that uh

**[03:16]** milliseconds or somewhere on that uh order. So it is pretty fast. So there's

**[03:18]** order. So it is pretty fast. So there's

**[03:18]** order. So it is pretty fast. So there's a lot to kind of to get all the way

**[03:19]** a lot to kind of to get all the way

**[03:19]** a lot to kind of to get all the way there. And this is something that we at

**[03:21]** there. And this is something that we at

**[03:22]** there. And this is something that we at daily everyone building pipe has been

**[03:23]** daily everyone building pipe has been

**[03:24]** daily everyone building pipe has been working very very hard on uh getting all

**[03:26]** working very very hard on uh getting all

**[03:26]** working very very hard on uh getting all the way to meeting all these

**[03:28]** the way to meeting all these

**[03:28]** the way to meeting all these expectations. So just to kind of ground

**[03:30]** expectations. So just to kind of ground

**[03:30]** expectations. So just to kind of ground you in some of this since we're going to

**[03:31]** you in some of this since we're going to

**[03:31]** you in some of this since we're going to be working in Pipcat. Pipcat has a

**[03:33]** be working in Pipcat. Pipcat has a

**[03:33]** be working in Pipcat. Pipcat has a pipeline. I don't know if maybe Al you

**[03:35]** pipeline. I don't know if maybe Al you

**[03:35]** pipeline. I don't know if maybe Al you want to talk a little bit about the

**[03:36]** want to talk a little bit about the

**[03:36]** want to talk a little bit about the origin of that quickly. Sure. Sure. Uh

**[03:39]** origin of that quickly. Sure. Sure. Uh

**[03:39]** origin of that quickly. Sure. Sure. Uh you can think about it as a multimedia

**[03:41]** you can think about it as a multimedia

**[03:41]** you can think about it as a multimedia pipeline and you would think what is a

**[03:43]** pipeline and you would think what is a

**[03:43]** pipeline and you would think what is a multimedia pipeline. It's basically just

**[03:45]** multimedia pipeline. It's basically just

**[03:46]** multimedia pipeline. It's basically just think about like boxes that receive

**[03:47]** think about like boxes that receive

**[03:48]** think about like boxes that receive input and input could be audio or video

**[03:51]** input and input could be audio or video

**[03:51]** input and input could be audio or video and then those boxes just will stream

**[03:54]** and then those boxes just will stream

**[03:54]** and then those boxes just will stream those uh same data or modify data or new

**[03:58]** those uh same data or modify data or new

**[03:58]** those uh same data or modify data or new data to the following uh to the


### [04:00 - 05:00]

**[04:01]** data to the following uh to the

**[04:01]** data to the following uh to the following elements or processors in in

**[04:03]** following elements or processors in in

**[04:03]** following elements or processors in in pipe wall we call them processors. So in

**[04:06]** pipe wall we call them processors. So in

**[04:06]** pipe wall we call them processors. So in in pipcat you would have a pipeline

**[04:09]** in pipcat you would have a pipeline

**[04:09]** in pipcat you would have a pipeline where you have a transport which is the

**[04:13]** where you have a transport which is the

**[04:13]** where you have a transport which is the the in the the transport of your data or

**[04:15]** the in the the transport of your data or

**[04:15]** the in the the transport of your data or the input of your data. For example when

**[04:17]** the input of your data. For example when

**[04:17]** the input of your data. For example when you're talking

**[04:19]** you're talking

**[04:19]** you're talking you could be talking in a in a meeting.

**[04:21]** you could be talking in a in a meeting.

**[04:21]** you could be talking in a in a meeting. So that would be the audio of the user.

**[04:23]** So that would be the audio of the user.

**[04:23]** So that would be the audio of the user. Then you would have uh another box

**[04:26]** Then you would have uh another box

**[04:26]** Then you would have uh another box following that which is the speechto

**[04:27]** following that which is the speechto

**[04:27]** following that which is the speechto text service. So the speechto text

**[04:29]** text service. So the speechto text

**[04:29]** text service. So the speechto text service would would grab uh audio from

**[04:32]** service would would grab uh audio from

**[04:32]** service would would grab uh audio from the user. It would uh transcribe it.

**[04:35]** the user. It would uh transcribe it.

**[04:35]** the user. It would uh transcribe it. Then you will get text that will be the

**[04:37]** Then you will get text that will be the

**[04:37]** Then you will get text that will be the following data that goes through the

**[04:39]** following data that goes through the

**[04:39]** following data that goes through the pipeline and then the next one will be

**[04:41]** pipeline and then the next one will be

**[04:41]** pipeline and then the next one will be the LLM. So now the LLM has what the

**[04:44]** the LLM. So now the LLM has what the

**[04:44]** the LLM. So now the LLM has what the user has set

**[04:46]** user has set

**[04:46]** user has set and then it generates uh output whatever

**[04:50]** and then it generates uh output whatever

**[04:50]** and then it generates uh output whatever uh whatever the LLM that would be tokens

**[04:52]** uh whatever the LLM that would be tokens

**[04:52]** uh whatever the LLM that would be tokens then those tokens are are converted into

**[04:56]** then those tokens are are converted into

**[04:56]** then those tokens are are converted into um text to speech and then the text to

**[04:59]** um text to speech and then the text to

**[04:59]** um text to speech and then the text to speech outputs audio and then the audio


### [05:00 - 06:00]

**[05:01]** speech outputs audio and then the audio

**[05:01]** speech outputs audio and then the audio goes back to the transport so you could

**[05:03]** goes back to the transport so you could

**[05:03]** goes back to the transport so you could hear what the LM has said. Today, uh,

**[05:06]** hear what the LM has said. Today, uh,

**[05:06]** hear what the LM has said. Today, uh, what we're going to do today with Gemini

**[05:08]** what we're going to do today with Gemini

**[05:08]** what we're going to do today with Gemini live, a lot of those boxes go away

**[05:10]** live, a lot of those boxes go away

**[05:10]** live, a lot of those boxes go away because, uh, uh, the LLM will do a bunch

**[05:14]** because, uh, uh, the LLM will do a bunch

**[05:14]** because, uh, uh, the LLM will do a bunch of these things. It will do

**[05:15]** of these things. It will do

**[05:15]** of these things. It will do transcription, it will do the LLM, and

**[05:18]** transcription, it will do the LLM, and

**[05:18]** transcription, it will do the LLM, and it will do the text to speech in in one

**[05:20]** it will do the text to speech in in one

**[05:20]** it will do the text to speech in in one of these boxes, but you might still

**[05:22]** of these boxes, but you might still

**[05:22]** of these boxes, but you might still require, for example, if you want to

**[05:24]** require, for example, if you want to

**[05:24]** require, for example, if you want to save the audio, record the audio into a

**[05:26]** save the audio, record the audio into a

**[05:26]** save the audio, record the audio into a file, you need a bunch of utilities to

**[05:28]** file, you need a bunch of utilities to

**[05:28]** file, you need a bunch of utilities to do that. And Pipet has all that built

**[05:30]** do that. And Pipet has all that built

**[05:30]** do that. And Pipet has all that built for you. Um, so basically that's that's

**[05:34]** for you. Um, so basically that's that's

**[05:34]** for you. Um, so basically that's that's it. I mean a lot of this is really just

**[05:36]** it. I mean a lot of this is really just

**[05:36]** it. I mean a lot of this is really just or it's orchestration. So if you think

**[05:38]** or it's orchestration. So if you think

**[05:38]** or it's orchestration. So if you think about what Pipecat offers, it's

**[05:39]** about what Pipecat offers, it's

**[05:39]** about what Pipecat offers, it's orchestration. It also offers a lot of

**[05:42]** orchestration. It also offers a lot of

**[05:42]** orchestration. It also offers a lot of abstractions for a lot of common

**[05:43]** abstractions for a lot of common

**[05:43]** abstractions for a lot of common utilities like Alles had said. So

**[05:45]** utilities like Alles had said. So

**[05:45]** utilities like Alles had said. So recording transcript outputs, artifacts

**[05:47]** recording transcript outputs, artifacts

**[05:47]** recording transcript outputs, artifacts you might want to produce or even ways

**[05:49]** you might want to produce or even ways

**[05:49]** you might want to produce or even ways that you might manipulate the

**[05:50]** that you might manipulate the

**[05:50]** that you might manipulate the information in the pipeline itself. So

**[05:53]** information in the pipeline itself. So

**[05:53]** information in the pipeline itself. So this uh image here, which is what Alles

**[05:55]** this uh image here, which is what Alles

**[05:55]** this uh image here, which is what Alles actually just talked through, is what

**[05:57]** actually just talked through, is what

**[05:57]** actually just talked through, is what you would call I guess a cascaded model

**[05:59]** you would call I guess a cascaded model

**[05:59]** you would call I guess a cascaded model where you have this flow through of


### [06:00 - 07:00]

**[06:01]** where you have this flow through of

**[06:01]** where you have this flow through of information. So we're going to be you

**[06:03]** information. So we're going to be you

**[06:03]** information. So we're going to be you can build with Google and many different

**[06:05]** can build with Google and many different

**[06:05]** can build with Google and many different services in this way. Uh in the last

**[06:07]** services in this way. Uh in the last

**[06:07]** services in this way. Uh in the last year there's been an emergence of

**[06:09]** year there's been an emergence of

**[06:09]** year there's been an emergence of speechtoech models that now take audio

**[06:11]** speechtoech models that now take audio

**[06:11]** speechtoech models that now take audio in natively and audio out natively. And

**[06:13]** in natively and audio out natively. And

**[06:13]** in natively and audio out natively. And those models also allow for audio in and

**[06:16]** those models also allow for audio in and

**[06:16]** those models also allow for audio in and then optionally text andor audio out. So

**[06:19]** then optionally text andor audio out. So

**[06:19]** then optionally text andor audio out. So you can actually for example take a raw

**[06:22]** you can actually for example take a raw

**[06:22]** you can actually for example take a raw you know microphone input or uh you know

**[06:26]** you know microphone input or uh you know

**[06:26]** you know microphone input or uh you know audio input and then the model would run

**[06:29]** audio input and then the model would run

**[06:29]** audio input and then the model would run all of its logic and you can actually

**[06:31]** all of its logic and you can actually

**[06:31]** all of its logic and you can actually opt to have it output text if you want

**[06:33]** opt to have it output text if you want

**[06:33]** opt to have it output text if you want to say parse the text output before

**[06:35]** to say parse the text output before

**[06:35]** to say parse the text output before speaking. So there are a few different

**[06:37]** speaking. So there are a few different

**[06:37]** speaking. So there are a few different demos we'll look at that offer that uh

**[06:39]** demos we'll look at that offer that uh

**[06:39]** demos we'll look at that offer that uh and in Pipcat we show kind of all the

**[06:41]** and in Pipcat we show kind of all the

**[06:41]** and in Pipcat we show kind of all the ways to do things because that's that's

**[06:42]** ways to do things because that's that's

**[06:42]** ways to do things because that's that's what we offer or at least what Pipcat

**[06:44]** what we offer or at least what Pipcat

**[06:44]** what we offer or at least what Pipcat offers as a as a value proposition. So

**[06:47]** offers as a as a value proposition. So

**[06:47]** offers as a as a value proposition. So the um yeah just one thing I don't think

**[06:50]** the um yeah just one thing I don't think

**[06:50]** the um yeah just one thing I don't think you'll mention it in the slides but all

**[06:51]** you'll mention it in the slides but all

**[06:51]** you'll mention it in the slides but all these boxes you can pluck and play the

**[06:54]** these boxes you can pluck and play the

**[06:54]** these boxes you can pluck and play the service you want in pipcat. So the

**[06:56]** service you want in pipcat. So the

**[06:56]** service you want in pipcat. So the speech to speech uh speech to text, it

**[06:58]** speech to speech uh speech to text, it

**[06:58]** speech to speech uh speech to text, it could be I don't know deep for example,


### [07:00 - 08:00]

**[07:01]** could be I don't know deep for example,

**[07:01]** could be I don't know deep for example, the LLM could be uh Google or OpenAI or

**[07:04]** the LLM could be uh Google or OpenAI or

**[07:04]** the LLM could be uh Google or OpenAI or whatever. You can just plug and play any

**[07:06]** whatever. You can just plug and play any

**[07:06]** whatever. You can just plug and play any service you want, right? Yeah. The

**[07:08]** service you want, right? Yeah. The

**[07:08]** service you want, right? Yeah. The modularity I guess is the other big

**[07:10]** modularity I guess is the other big

**[07:10]** modularity I guess is the other big strength. So there's no, you know, you

**[07:11]** strength. So there's no, you know, you

**[07:12]** strength. So there's no, you know, you can change out a service without

**[07:13]** can change out a service without

**[07:13]** can change out a service without changing out your underlying application

**[07:15]** changing out your underlying application

**[07:15]** changing out your underlying application code, which makes it easy. And we see

**[07:17]** code, which makes it easy. And we see

**[07:17]** code, which makes it easy. And we see with this a lot of companies that are

**[07:19]** with this a lot of companies that are

**[07:19]** with this a lot of companies that are building for voice AI might have uh

**[07:21]** building for voice AI might have uh

**[07:22]** building for voice AI might have uh maybe even a more complex thing a

**[07:23]** maybe even a more complex thing a

**[07:23]** maybe even a more complex thing a pipeline here runs straight down but you

**[07:25]** pipeline here runs straight down but you

**[07:25]** pipeline here runs straight down but you can actually have split branches where

**[07:27]** can actually have split branches where

**[07:27]** can actually have split branches where you might have one leg that's running

**[07:29]** you might have one leg that's running

**[07:29]** you might have one leg that's running some logic and the other running a

**[07:30]** some logic and the other running a

**[07:30]** some logic and the other running a different we call that a parallel

**[07:31]** different we call that a parallel

**[07:31]** different we call that a parallel pipeline. So if you wanted to have say a

**[07:34]** pipeline. So if you wanted to have say a

**[07:34]** pipeline. So if you wanted to have say a failover if vendor A goes down you can

**[07:37]** failover if vendor A goes down you can

**[07:37]** failover if vendor A goes down you can move to vendor B dynamically even within

**[07:40]** move to vendor B dynamically even within

**[07:40]** move to vendor B dynamically even within the same conversation. That's something

**[07:41]** the same conversation. That's something

**[07:41]** the same conversation. That's something that Pipcat affords as well. Um, and

**[07:44]** that Pipcat affords as well. Um, and

**[07:44]** that Pipcat affords as well. Um, and that can allow you to transfer contexts

**[07:45]** that can allow you to transfer contexts

**[07:46]** that can allow you to transfer contexts over. So, a lot of really cool stuff.

**[07:48]** over. So, a lot of really cool stuff.

**[07:48]** over. So, a lot of really cool stuff. Uh, the goal again today being to get

**[07:50]** Uh, the goal again today being to get

**[07:50]** Uh, the goal again today being to get you familiar with just building a voice

**[07:53]** you familiar with just building a voice

**[07:53]** you familiar with just building a voice agent and building one to get started.

**[07:55]** agent and building one to get started.

**[07:55]** agent and building one to get started. So, one of the cool things,

**[07:58]** So, one of the cool things,

**[07:58]** So, one of the cool things, um, like Alles had pointed out that with


### [08:00 - 09:00]

**[08:01]** um, like Alles had pointed out that with

**[08:01]** um, like Alles had pointed out that with the cascaded models, there's a lot of

**[08:03]** the cascaded models, there's a lot of

**[08:03]** the cascaded models, there's a lot of complexity, but with your speechtospech

**[08:05]** complexity, but with your speechtospech

**[08:05]** complexity, but with your speechtospech model, things get, you know,

**[08:06]** model, things get, you know,

**[08:06]** model, things get, you know, dramatically simplified. You know, your

**[08:09]** dramatically simplified. You know, your

**[08:09]** dramatically simplified. You know, your code may have looked something like

**[08:10]** code may have looked something like

**[08:10]** code may have looked something like this. This is like an old example of

**[08:12]** this. This is like an old example of

**[08:12]** this. This is like an old example of some like a ton of uh orchestration in

**[08:15]** some like a ton of uh orchestration in

**[08:15]** some like a ton of uh orchestration in the pipeline, but with a speech-to-pech

**[08:18]** the pipeline, but with a speech-to-pech

**[08:18]** the pipeline, but with a speech-to-pech model, you may be able to simplify it

**[08:20]** model, you may be able to simplify it

**[08:20]** model, you may be able to simplify it down to this, but then you have to

**[08:22]** down to this, but then you have to

**[08:22]** down to this, but then you have to remember you actually need orchestration

**[08:24]** remember you actually need orchestration

**[08:24]** remember you actually need orchestration around it. So, it does get simpler to

**[08:25]** around it. So, it does get simpler to

**[08:26]** around it. So, it does get simpler to some regard. Um, so it's it's more about

**[08:28]** some regard. Um, so it's it's more about

**[08:28]** some regard. Um, so it's it's more about the services you interface with. Uh I

**[08:31]** the services you interface with. Uh I

**[08:31]** the services you interface with. Uh I think with that why don't we transition

**[08:32]** think with that why don't we transition

**[08:32]** think with that why don't we transition now because I'm realizing we have only

**[08:34]** now because I'm realizing we have only

**[08:34]** now because I'm realizing we have only about maybe 70 70 75 minutes left to

**[08:38]** about maybe 70 70 75 minutes left to

**[08:38]** about maybe 70 70 75 minutes left to looking at um the actual activity for

**[08:40]** looking at um the actual activity for

**[08:40]** looking at um the actual activity for today. All right. So there's a public

**[08:43]** today. All right. So there's a public

**[08:43]** today. All right. So there's a public repo I don't know how big or small this

**[08:45]** repo I don't know how big or small this

**[08:45]** repo I don't know how big or small this is but it's under daily co. So on GitHub

**[08:49]** is but it's under daily co. So on GitHub

**[08:49]** is but it's under daily co. So on GitHub daily co daily.comini-pipcat-workshop.

**[08:55]** We'll give everyone a chance to make

**[08:55]** We'll give everyone a chance to make sure internet's working. And can

**[08:59]** sure internet's working. And can

**[08:59]** sure internet's working. And can everyone see the the repo? Yeah, it's


### [09:00 - 10:00]

**[09:01]** everyone see the the repo? Yeah, it's

**[09:01]** everyone see the the repo? Yeah, it's really tiny. Yeah. Okay. I should have

**[09:04]** really tiny. Yeah. Okay. I should have

**[09:04]** really tiny. Yeah. Okay. I should have it in big text somewhere.

**[09:07]** it in big text somewhere.

**[09:08]** it in big text somewhere. Not really.

**[09:30]** All right,

**[09:30]** All right, let's take a look at this. So, what what

**[09:32]** let's take a look at this. So, what what

**[09:32]** let's take a look at this. So, what what I want to do, so there I spent a little

**[09:34]** I want to do, so there I spent a little

**[09:34]** I want to do, so there I spent a little bit of time, Alles and I spent time

**[09:36]** bit of time, Alles and I spent time

**[09:36]** bit of time, Alles and I spent time writing up this repo. This is meant to

**[09:38]** writing up this repo. This is meant to

**[09:38]** writing up this repo. This is meant to be just a jumping off point. I'm going

**[09:39]** be just a jumping off point. I'm going

**[09:39]** be just a jumping off point. I'm going to get you oriented and then I want to

**[09:41]** to get you oriented and then I want to

**[09:41]** to get you oriented and then I want to look through one of the bot files which

**[09:43]** look through one of the bot files which

**[09:43]** look through one of the bot files which is kind of the main pipecat code with

**[09:45]** is kind of the main pipecat code with

**[09:45]** is kind of the main pipecat code with you and then we'll break and make this

**[09:48]** you and then we'll break and make this

**[09:48]** you and then we'll break and make this an interactive session where we can

**[09:49]** an interactive session where we can

**[09:50]** an interactive session where we can answer a bunch of questions. So in the

**[09:51]** answer a bunch of questions. So in the

**[09:51]** answer a bunch of questions. So in the repo um you could either start doing it

**[09:55]** repo um you could either start doing it

**[09:55]** repo um you could either start doing it now or maybe take a pause but this will

**[09:57]** now or maybe take a pause but this will

**[09:57]** now or maybe take a pause but this will give you the steps to walk through

**[09:58]** give you the steps to walk through

**[09:58]** give you the steps to walk through getting the quick start running. Before


### [10:00 - 11:00]

**[10:01]** getting the quick start running. Before

**[10:01]** getting the quick start running. Before we do that I want to take a moment here.

**[10:05]** we do that I want to take a moment here.

**[10:05]** we do that I want to take a moment here. Let's see how the Wi-Fi is doing. That's

**[10:08]** Let's see how the Wi-Fi is doing. That's

**[10:08]** Let's see how the Wi-Fi is doing. That's not a good sign.

**[10:15]** It's down. Uh

**[10:15]** It's down. Uh well, hey, you know, it is tough to do

**[10:17]** well, hey, you know, it is tough to do

**[10:17]** well, hey, you know, it is tough to do Wi-Fi for this many people. Very very

**[10:19]** Wi-Fi for this many people. Very very

**[10:20]** Wi-Fi for this many people. Very very instead of real time is going to be real

**[10:21]** instead of real time is going to be real

**[10:21]** instead of real time is going to be real slow. Real slow. Yeah. Real slow voice

**[10:24]** slow. Real slow. Yeah. Real slow voice

**[10:24]** slow. Real slow. Yeah. Real slow voice communication. All right.

**[10:27]** communication. All right.

**[10:27]** communication. All right. Yeah. Yes. Yeah. There will be some.

**[10:30]** Yeah. Yes. Yeah. There will be some.

**[10:30]** Yeah. Yes. Yeah. There will be some. Okay. So, in uh here is this Gemini

**[10:35]** Okay. So, in uh here is this Gemini

**[10:35]** Okay. So, in uh here is this Gemini bot.py files. This is all Python again.

**[10:37]** bot.py files. This is all Python again.

**[10:37]** bot.py files. This is all Python again. So be everything will be in Python.

**[10:39]** So be everything will be in Python.

**[10:39]** So be everything will be in Python. There will be some client code options

**[10:41]** There will be some client code options

**[10:41]** There will be some client code options which we'll look at in a second. Um just

**[10:44]** which we'll look at in a second. Um just

**[10:44]** which we'll look at in a second. Um just to orient you, I'll just jump right into

**[10:46]** to orient you, I'll just jump right into

**[10:46]** to orient you, I'll just jump right into the meat of the pipeline. We have this

**[10:48]** the meat of the pipeline. We have this

**[10:48]** the meat of the pipeline. We have this main uh function that runs your bot.

**[10:53]** main uh function that runs your bot.

**[10:53]** main uh function that runs your bot. Everything is going to run kind of

**[10:54]** Everything is going to run kind of

**[10:54]** Everything is going to run kind of encapsulated within an AIO HTTP session.

**[10:57]** encapsulated within an AIO HTTP session.

**[10:57]** encapsulated within an AIO HTTP session. We're going to pass that session around.

**[10:59]** We're going to pass that session around.

**[10:59]** We're going to pass that session around. That's more of just kind of the


### [11:00 - 12:00]

**[11:00]** That's more of just kind of the

**[11:00]** That's more of just kind of the mechanics of things in our pipeline.

**[11:03]** mechanics of things in our pipeline.

**[11:03]** mechanics of things in our pipeline. Let's just jump to the the simple part

**[11:04]** Let's just jump to the the simple part

**[11:04]** Let's just jump to the the simple part here. will have daily as the transport

**[11:06]** here. will have daily as the transport

**[11:06]** here. will have daily as the transport daily as we are a web RTC provider as

**[11:10]** daily as we are a web RTC provider as

**[11:10]** daily as we are a web RTC provider as well as we build pipecat. Uh there will

**[11:12]** well as we build pipecat. Uh there will

**[11:12]** well as we build pipecat. Uh there will be context aggregation. So one important

**[11:15]** be context aggregation. So one important

**[11:15]** be context aggregation. So one important note when you speak uh every turn of the

**[11:18]** note when you speak uh every turn of the

**[11:18]** note when you speak uh every turn of the bot is a like a a discrete point in time

**[11:21]** bot is a like a a discrete point in time

**[11:21]** bot is a like a a discrete point in time and this is maybe less so the case for a

**[11:23]** and this is maybe less so the case for a

**[11:23]** and this is maybe less so the case for a speechtoech model but for basic LLMs

**[11:27]** speechtoech model but for basic LLMs

**[11:27]** speechtoech model but for basic LLMs they get discrete inputs. Everything is

**[11:29]** they get discrete inputs. Everything is

**[11:29]** they get discrete inputs. Everything is like a REST API call. So you're going to

**[11:30]** like a REST API call. So you're going to

**[11:30]** like a REST API call. So you're going to get a snapshot of the conversation. The

**[11:33]** get a snapshot of the conversation. The

**[11:33]** get a snapshot of the conversation. The context aggregator is going to collect

**[11:36]** context aggregator is going to collect

**[11:36]** context aggregator is going to collect the all the bits of the conversation

**[11:38]** the all the bits of the conversation

**[11:38]** the all the bits of the conversation both from the user and the assistant uh

**[11:40]** both from the user and the assistant uh

**[11:40]** both from the user and the assistant uh and we'll put that into the form of what

**[11:43]** and we'll put that into the form of what

**[11:43]** and we'll put that into the form of what the LLMs can handle. So this in this

**[11:45]** the LLMs can handle. So this in this

**[11:45]** the LLMs can handle. So this in this case is more for function calling and

**[11:49]** case is more for function calling and

**[11:49]** case is more for function calling and kind of logistics and management. Gemini

**[11:51]** kind of logistics and management. Gemini

**[11:51]** kind of logistics and management. Gemini is amazing because it offers a lot of

**[11:53]** is amazing because it offers a lot of

**[11:53]** is amazing because it offers a lot of this for you. But if you're to build

**[11:55]** this for you. But if you're to build

**[11:55]** this for you. But if you're to build with say the uh just build with Gemini

**[11:58]** with say the uh just build with Gemini

**[11:58]** with say the uh just build with Gemini not live the actual kind of just the


### [12:00 - 13:00]

**[12:00]** not live the actual kind of just the

**[12:00]** not live the actual kind of just the textbased LLM you'd have to have this

**[12:02]** textbased LLM you'd have to have this

**[12:02]** textbased LLM you'd have to have this context aggregation

**[12:04]** context aggregation

**[12:04]** context aggregation uh that will then go to your LLM which

**[12:07]** uh that will then go to your LLM which

**[12:07]** uh that will then go to your LLM which is going to be Gemini live Gemini

**[12:08]** is going to be Gemini live Gemini

**[12:08]** is going to be Gemini live Gemini multimodal live and then it's going to

**[12:10]** multimodal live and then it's going to

**[12:10]** multimodal live and then it's going to be outputed through uh daily again on on

**[12:14]** be outputed through uh daily again on on

**[12:14]** be outputed through uh daily again on on that side of the transport.

**[12:16]** that side of the transport.

**[12:16]** that side of the transport. So you have daily we'd configure our

**[12:18]** So you have daily we'd configure our

**[12:18]** So you have daily we'd configure our service which takes a number of

**[12:20]** service which takes a number of

**[12:20]** service which takes a number of arguments like you set up a room with a

**[12:22]** arguments like you set up a room with a

**[12:22]** arguments like you set up a room with a token give it a name and then have some

**[12:24]** token give it a name and then have some

**[12:24]** token give it a name and then have some properties. There are docs which I'll

**[12:26]** properties. There are docs which I'll

**[12:26]** properties. There are docs which I'll link to uh in it's linked in the quick

**[12:30]** link to uh in it's linked in the quick

**[12:30]** link to uh in it's linked in the quick start. There's also a Gemini multimodal

**[12:32]** start. There's also a Gemini multimodal

**[12:32]** start. There's also a Gemini multimodal live llm service which is a pipecat

**[12:34]** live llm service which is a pipecat

**[12:34]** live llm service which is a pipecat class that is a wrapper around the

**[12:37]** class that is a wrapper around the

**[12:37]** class that is a wrapper around the Gemini live API. So this again you just

**[12:40]** Gemini live API. So this again you just

**[12:40]** Gemini live API. So this again you just initialize and run

**[12:43]** initialize and run

**[12:43]** initialize and run with the LLM. You see, we do a few

**[12:45]** with the LLM. You see, we do a few

**[12:45]** with the LLM. You see, we do a few special things. We're going to define

**[12:47]** special things. We're going to define

**[12:47]** special things. We're going to define tools. This one has just two really

**[12:50]** tools. This one has just two really

**[12:50]** tools. This one has just two really basic kind of canned functions.

**[12:51]** basic kind of canned functions.

**[12:51]** basic kind of canned functions. Fortunately, we're not calling out to

**[12:52]** Fortunately, we're not calling out to

**[12:52]** Fortunately, we're not calling out to the internet because it's not working

**[12:53]** the internet because it's not working

**[12:53]** the internet because it's not working very well. Um, our connection is not

**[12:56]** very well. Um, our connection is not

**[12:56]** very well. Um, our connection is not working well. So, this one just has the

**[12:58]** working well. So, this one just has the

**[12:58]** working well. So, this one just has the dummy like fetch weather and we'll give


### [13:00 - 14:00]

**[13:00]** dummy like fetch weather and we'll give

**[13:00]** dummy like fetch weather and we'll give you a restaurant recommendation. So,

**[13:01]** you a restaurant recommendation. So,

**[13:02]** you a restaurant recommendation. So, these are two handlers that when your

**[13:04]** these are two handlers that when your

**[13:04]** these are two handlers that when your function is called, we'll just return

**[13:05]** function is called, we'll just return

**[13:05]** function is called, we'll just return this result information.

**[13:07]** this result information.

**[13:08]** this result information. Uh so we have the actual functions

**[13:10]** Uh so we have the actual functions

**[13:10]** Uh so we have the actual functions themselves that are defined in this

**[13:12]** themselves that are defined in this

**[13:12]** themselves that are defined in this function schema which is you can use

**[13:15]** function schema which is you can use

**[13:15]** function schema which is you can use just native function uh definitions

**[13:17]** just native function uh definitions

**[13:18]** just native function uh definitions using whatever LLM format. We also

**[13:20]** using whatever LLM format. We also

**[13:20]** using whatever LLM format. We also created this function schema which is a

**[13:22]** created this function schema which is a

**[13:22]** created this function schema which is a universal schema that lets you define uh

**[13:25]** universal schema that lets you define uh

**[13:25]** universal schema that lets you define uh and move between any LLM without having

**[13:27]** and move between any LLM without having

**[13:27]** and move between any LLM without having to kind of transform your LLM calls from

**[13:31]** to kind of transform your LLM calls from

**[13:31]** to kind of transform your LLM calls from OpenAI to anthropic to Gemini to Bedrock

**[13:34]** OpenAI to anthropic to Gemini to Bedrock

**[13:34]** OpenAI to anthropic to Gemini to Bedrock because they're all a little bit

**[13:35]** because they're all a little bit

**[13:35]** because they're all a little bit different or Grock, you know, they all

**[13:36]** different or Grock, you know, they all

**[13:36]** different or Grock, you know, they all have slightly different formats. So this

**[13:38]** have slightly different formats. So this

**[13:38]** have slightly different formats. So this is more of kind of a universal transform

**[13:40]** is more of kind of a universal transform

**[13:40]** is more of kind of a universal transform for that.

**[13:42]** for that.

**[13:42]** for that. And then they're collected and trans

**[13:44]** And then they're collected and trans

**[13:44]** And then they're collected and trans translated into the native format in

**[13:46]** translated into the native format in

**[13:46]** translated into the native format in this tool schema. So we'll pass the

**[13:49]** this tool schema. So we'll pass the

**[13:49]** this tool schema. So we'll pass the tools then to the Gemini service and

**[13:53]** tools then to the Gemini service and

**[13:53]** tools then to the Gemini service and that's how it gets access to use and run

**[13:54]** that's how it gets access to use and run

**[13:54]** that's how it gets access to use and run those tools. There's also a prompt above

**[13:57]** those tools. There's also a prompt above

**[13:57]** those tools. There's also a prompt above which I think in this simple example we

**[13:59]** which I think in this simple example we

**[13:59]** which I think in this simple example we just say hey you're a chatbot you have


### [14:00 - 15:00]

**[14:00]** just say hey you're a chatbot you have

**[14:00]** just say hey you're a chatbot you have these tools available uh and that's

**[14:02]** these tools available uh and that's

**[14:02]** these tools available uh and that's that.

**[14:04]** that.

**[14:04]** that. We're also setting up our context

**[14:06]** We're also setting up our context

**[14:06]** We're also setting up our context aggregation which for better or worse we

**[14:09]** aggregation which for better or worse we

**[14:09]** aggregation which for better or worse we use open AI as kind of the default like

**[14:11]** use open AI as kind of the default like

**[14:12]** use open AI as kind of the default like uh the lingua frana for context. So

**[14:14]** uh the lingua frana for context. So

**[14:14]** uh the lingua frana for context. So everything gets kind of folded back into

**[14:15]** everything gets kind of folded back into

**[14:15]** everything gets kind of folded back into open AI uh at a certain level. Um and we

**[14:20]** open AI uh at a certain level. Um and we

**[14:20]** open AI uh at a certain level. Um and we define the pipeline. So the pipeline is

**[14:22]** define the pipeline. So the pipeline is

**[14:22]** define the pipeline. So the pipeline is again like Alles had said just a list of

**[14:24]** again like Alles had said just a list of

**[14:24]** again like Alles had said just a list of all of your different or I guess a tupil

**[14:27]** all of your different or I guess a tupil

**[14:27]** all of your different or I guess a tupil of all of your different services

**[14:30]** of all of your different services

**[14:30]** of all of your different services um that are running in the pipeline and

**[14:31]** um that are running in the pipeline and

**[14:31]** um that are running in the pipeline and you can write your own. So if you want

**[14:33]** you can write your own. So if you want

**[14:33]** you can write your own. So if you want to instead make the LLM output text and

**[14:35]** to instead make the LLM output text and

**[14:36]** to instead make the LLM output text and you want to either extract information

**[14:39]** you want to either extract information

**[14:39]** you want to either extract information from that, maybe you have it in code

**[14:40]** from that, maybe you have it in code

**[14:40]** from that, maybe you have it in code some XML or some type of information,

**[14:42]** some XML or some type of information,

**[14:42]** some XML or some type of information, you can actually extract it, store it,

**[14:44]** you can actually extract it, store it,

**[14:44]** you can actually extract it, store it, maybe your application does something

**[14:46]** maybe your application does something

**[14:46]** maybe your application does something with it. Um, or maybe you want to inject

**[14:49]** with it. Um, or maybe you want to inject

**[14:49]** with it. Um, or maybe you want to inject a texttospech type of uh frame. You can

**[14:52]** a texttospech type of uh frame. You can

**[14:52]** a texttospech type of uh frame. You can actually do that by separating the LLM

**[14:55]** actually do that by separating the LLM

**[14:55]** actually do that by separating the LLM the that audio output from audio output

**[14:58]** the that audio output from audio output

**[14:58]** the that audio output from audio output to just be text. And then we you would


### [15:00 - 16:00]

**[15:00]** to just be text. And then we you would

**[15:00]** to just be text. And then we you would add like a texttospech service here or

**[15:02]** add like a texttospech service here or

**[15:02]** add like a texttospech service here or you could write your own processor which

**[15:04]** you could write your own processor which

**[15:04]** you could write your own processor which maybe not within the next hour. And then

**[15:07]** maybe not within the next hour. And then

**[15:07]** maybe not within the next hour. And then lastly all of these or not all but many

**[15:09]** lastly all of these or not all but many

**[15:09]** lastly all of these or not all but many of them have uh events they emit. The

**[15:11]** of them have uh events they emit. The

**[15:11]** of them have uh events they emit. The transport emits handlers for when the

**[15:14]** transport emits handlers for when the

**[15:14]** transport emits handlers for when the client connects and disconnects. So in

**[15:16]** client connects and disconnects. So in

**[15:16]** client connects and disconnects. So in this case uh we use this line here to

**[15:21]** this case uh we use this line here to

**[15:21]** this case uh we use this line here to actually inject a context frame into

**[15:23]** actually inject a context frame into

**[15:23]** actually inject a context frame into Gemini to get kick off the conversation.

**[15:25]** Gemini to get kick off the conversation.

**[15:25]** Gemini to get kick off the conversation. So when your client application

**[15:27]** So when your client application

**[15:27]** So when your client application connects, it's going to cue a frame. So

**[15:29]** connects, it's going to cue a frame. So

**[15:29]** connects, it's going to cue a frame. So again, frames being kind of the base

**[15:32]** again, frames being kind of the base

**[15:32]** again, frames being kind of the base format for uh information. Think of it

**[15:34]** format for uh information. Think of it

**[15:34]** format for uh information. Think of it as like an object for your pipeline.

**[15:36]** as like an object for your pipeline.

**[15:36]** as like an object for your pipeline. You're going to cue one of those frames.

**[15:37]** You're going to cue one of those frames.

**[15:37]** You're going to cue one of those frames. And what this function does is it just

**[15:40]** And what this function does is it just

**[15:40]** And what this function does is it just grabs the latest context. So when we set

**[15:43]** grabs the latest context. So when we set

**[15:43]** grabs the latest context. So when we set this one above, I think that just says

**[15:45]** this one above, I think that just says

**[15:45]** this one above, I think that just says hello, that's going to pass that into

**[15:48]** hello, that's going to pass that into

**[15:48]** hello, that's going to pass that into basically push that into the pipeline,

**[15:50]** basically push that into the pipeline,

**[15:50]** basically push that into the pipeline, which then it will make its way to uh to

**[15:52]** which then it will make its way to uh to

**[15:52]** which then it will make its way to uh to Gemini to initialize the conversation.

**[15:54]** Gemini to initialize the conversation.

**[15:54]** Gemini to initialize the conversation. And the rest of this you could think of

**[15:56]** And the rest of this you could think of

**[15:56]** And the rest of this you could think of as boilerplate to run it. You create a

**[15:57]** as boilerplate to run it. You create a

**[15:57]** as boilerplate to run it. You create a runner which then is the thing that

**[15:59]** runner which then is the thing that

**[15:59]** runner which then is the thing that actually runs your task. And the task is


### [16:00 - 17:00]

**[16:01]** actually runs your task. And the task is

**[16:01]** actually runs your task. And the task is what runs the pipeline. So maybe beyond

**[16:04]** what runs the pipeline. So maybe beyond

**[16:04]** what runs the pipeline. So maybe beyond today, but just know that that's

**[16:05]** today, but just know that that's

**[16:05]** today, but just know that that's something that's required to run your

**[16:07]** something that's required to run your

**[16:07]** something that's required to run your code. Okay, I'm going to pause here just

**[16:09]** code. Okay, I'm going to pause here just

**[16:09]** code. Okay, I'm going to pause here just for any questions because I do want to

**[16:11]** for any questions because I do want to

**[16:11]** for any questions because I do want to get to developing soon.

**[16:22]** We provide both. That's a whole topic

**[16:22]** We provide both. That's a whole topic that is a talk in itself. Um, the short

**[16:25]** that is a talk in itself. Um, the short

**[16:25]** that is a talk in itself. Um, the short answer is if you're building a client

**[16:27]** answer is if you're building a client

**[16:27]** answer is if you're building a client server app, you should with like strong

**[16:30]** server app, you should with like strong

**[16:30]** server app, you should with like strong emphasis use WebRTC. It has a whole

**[16:33]** emphasis use WebRTC. It has a whole

**[16:33]** emphasis use WebRTC. It has a whole bunch of properties that are relevant

**[16:35]** bunch of properties that are relevant

**[16:35]** bunch of properties that are relevant like error correction, better audio

**[16:37]** like error correction, better audio

**[16:37]** like error correction, better audio quality, etc., etc. If you're building

**[16:39]** quality, etc., etc. If you're building

**[16:39]** quality, etc., etc. If you're building server to server, so one of the options

**[16:42]** server to server, so one of the options

**[16:42]** server to server, so one of the options today is to build a phone chatbot, you

**[16:44]** today is to build a phone chatbot, you

**[16:44]** today is to build a phone chatbot, you can use and it's probably the best

**[16:45]** can use and it's probably the best

**[16:45]** can use and it's probably the best option to use websockets. So, you can

**[16:47]** option to use websockets. So, you can

**[16:47]** option to use websockets. So, you can bring your own uh transport. We actually

**[16:49]** bring your own uh transport. We actually

**[16:49]** bring your own uh transport. We actually in Pipcat, there's a fast API version of

**[16:51]** in Pipcat, there's a fast API version of

**[16:52]** in Pipcat, there's a fast API version of that that's a server that you can use to

**[16:54]** that that's a server that you can use to

**[16:54]** that that's a server that you can use to exchange messages with a websocket. So

**[16:57]** exchange messages with a websocket. So

**[16:57]** exchange messages with a websocket. So yeah, it's really up to you. So I guess

**[16:59]** yeah, it's really up to you. So I guess

**[16:59]** yeah, it's really up to you. So I guess maybe the the takeaway is if you're


### [17:00 - 18:00]

**[17:00]** maybe the the takeaway is if you're

**[17:00]** maybe the the takeaway is if you're building client server, you really want

**[17:02]** building client server, you really want

**[17:02]** building client server, you really want WebRTC, you could technically use

**[17:03]** WebRTC, you could technically use

**[17:04]** WebRTC, you could technically use websockets, but you'll hit like a long

**[17:06]** websockets, but you'll hit like a long

**[17:06]** websockets, but you'll hit like a long tail of of errors when you get to

**[17:07]** tail of of errors when you get to

**[17:07]** tail of of errors when you get to production. And then server to server,

**[17:09]** production. And then server to server,

**[17:09]** production. And then server to server, totally fine. You're going to be fine

**[17:11]** totally fine. You're going to be fine

**[17:11]** totally fine. You're going to be fine with websockets.

**[17:18]** Could anyone download the repo by any

**[17:18]** Could anyone download the repo by any chance? Did anyone not? One person

**[17:20]** chance? Did anyone not? One person

**[17:20]** chance? Did anyone not? One person download the repo. persons. Three, four.

**[17:23]** download the repo. persons. Three, four.

**[17:23]** download the repo. persons. Three, four. Wi-Fi is dead. Wi-Fi is dead. Can anyone

**[17:26]** Wi-Fi is dead. Wi-Fi is dead. Can anyone

**[17:26]** Wi-Fi is dead. Wi-Fi is dead. Can anyone Can you tether? Is that an option? Do

**[17:27]** Can you tether? Is that an option? Do

**[17:27]** Can you tether? Is that an option? Do folks have tether hotspots on your phone

**[17:29]** folks have tether hotspots on your phone

**[17:29]** folks have tether hotspots on your phone or that's even shaky. Oh jeez. Okay.

**[17:37]** I can dance. Could do some I don't know.

**[17:37]** I can dance. Could do some I don't know. You know, I'm not really, you know, it's

**[17:39]** You know, I'm not really, you know, it's

**[17:39]** You know, I'm not really, you know, it's not my thing, but I could try.

**[17:41]** not my thing, but I could try.

**[17:41]** not my thing, but I could try. True. Yeah, I guess I could just make

**[17:43]** True. Yeah, I guess I could just make

**[17:43]** True. Yeah, I guess I could just make this uh code walk through. Um or we

**[17:46]** this uh code walk through. Um or we

**[17:46]** this uh code walk through. Um or we could write it. What? Yeah.

**[17:50]** could write it. What? Yeah.

**[17:50]** could write it. What? Yeah. Yeah, it Gemini does have its own VAD.

**[17:54]** Yeah, it Gemini does have its own VAD.

**[17:54]** Yeah, it Gemini does have its own VAD. Yeah,

**[17:57]** Yeah,

**[17:57]** Yeah, Gemini does have its own VAD. In fact,

**[17:58]** Gemini does have its own VAD. In fact,

**[17:58]** Gemini does have its own VAD. In fact, if you're using a speech to text service


### [18:00 - 19:00]

**[18:00]** if you're using a speech to text service

**[18:00]** if you're using a speech to text service that likely also brings its own VAD to

**[18:02]** that likely also brings its own VAD to

**[18:02]** that likely also brings its own VAD to the to the equation. What we found is

**[18:05]** the to the equation. What we found is

**[18:05]** the to the equation. What we found is that so maybe to use some of our extra

**[18:08]** that so maybe to use some of our extra

**[18:08]** that so maybe to use some of our extra time because we're having internet

**[18:09]** time because we're having internet

**[18:09]** time because we're having internet issues. Um the VAD serves a really

**[18:11]** issues. Um the VAD serves a really

**[18:12]** issues. Um the VAD serves a really important purpose of detecting when a

**[18:13]** important purpose of detecting when a

**[18:13]** important purpose of detecting when a user starts speaking. So in the whole

**[18:15]** user starts speaking. So in the whole

**[18:15]** user starts speaking. So in the whole kind of life cycle of a turn that user

**[18:18]** kind of life cycle of a turn that user

**[18:18]** kind of life cycle of a turn that user speaking kind of ushers in the user's

**[18:20]** speaking kind of ushers in the user's

**[18:20]** speaking kind of ushers in the user's turn for the conversation. So pipecat

**[18:22]** turn for the conversation. So pipecat

**[18:22]** turn for the conversation. So pipecat will emit a user started speaking frame

**[18:25]** will emit a user started speaking frame

**[18:25]** will emit a user started speaking frame and that will also push through an

**[18:27]** and that will also push through an

**[18:27]** and that will also push through an interruption. So the user will interrupt

**[18:29]** interruption. So the user will interrupt

**[18:29]** interruption. So the user will interrupt like anything that's talking. So if the

**[18:30]** like anything that's talking. So if the

**[18:30]** like anything that's talking. So if the bot was speaking or whatever uh it

**[18:33]** bot was speaking or whatever uh it

**[18:33]** bot was speaking or whatever uh it basically clears the way because the

**[18:34]** basically clears the way because the

**[18:34]** basically clears the way because the user has expressed they want to speak.

**[18:37]** user has expressed they want to speak.

**[18:37]** user has expressed they want to speak. The idea with the VAD is that we want it

**[18:38]** The idea with the VAD is that we want it

**[18:38]** The idea with the VAD is that we want it to be extremely accurate and extremely

**[18:41]** to be extremely accurate and extremely

**[18:41]** to be extremely accurate and extremely fast. So running something on device, we

**[18:44]** fast. So running something on device, we

**[18:44]** fast. So running something on device, we recommend Solero which is an open source

**[18:45]** recommend Solero which is an open source

**[18:46]** recommend Solero which is an open source option. It works incredibly well. I

**[18:48]** option. It works incredibly well. I

**[18:48]** option. It works incredibly well. I don't know what the inference time is

**[18:50]** don't know what the inference time is

**[18:50]** don't know what the inference time is like. I don't know millisec extremely

**[18:52]** like. I don't know millisec extremely

**[18:52]** like. I don't know millisec extremely fast. So you're going to get an event

**[18:55]** fast. So you're going to get an event

**[18:55]** fast. So you're going to get an event back uh fast. In fact, you have the

**[18:57]** back uh fast. In fact, you have the

**[18:57]** back uh fast. In fact, you have the ability to tune how long to hear human


### [19:00 - 20:00]

**[19:00]** ability to tune how long to hear human

**[19:00]** ability to tune how long to hear human speech before that event gets emitted.

**[19:02]** speech before that event gets emitted.

**[19:02]** speech before that event gets emitted. And there the defaults are pretty good

**[19:03]** And there the defaults are pretty good

**[19:03]** And there the defaults are pretty good in Pipcat. There are maybe scenarios

**[19:05]** in Pipcat. There are maybe scenarios

**[19:05]** in Pipcat. There are maybe scenarios where you want to change that. But the

**[19:07]** where you want to change that. But the

**[19:07]** where you want to change that. But the VAD is a really important uh

**[19:08]** VAD is a really important uh

**[19:08]** VAD is a really important uh consideration. It's extremely low CPU

**[19:11]** consideration. It's extremely low CPU

**[19:11]** consideration. It's extremely low CPU consumption. Quinn has a great uh

**[19:14]** consumption. Quinn has a great uh

**[19:14]** consumption. Quinn has a great uh spreadsheet of breaking down the full

**[19:15]** spreadsheet of breaking down the full

**[19:15]** spreadsheet of breaking down the full cost analysis of an an agent and really

**[19:18]** cost analysis of an an agent and really

**[19:18]** cost analysis of an an agent and really the CPU is going to be extremely low.

**[19:20]** the CPU is going to be extremely low.

**[19:20]** the CPU is going to be extremely low. Interestingly, the TTS tokens or

**[19:22]** Interestingly, the TTS tokens or

**[19:22]** Interestingly, the TTS tokens or characters are are the most expensive by

**[19:24]** characters are are the most expensive by

**[19:24]** characters are are the most expensive by far. Um, so when you think about it,

**[19:27]** far. Um, so when you think about it,

**[19:27]** far. Um, so when you think about it, running that local VAD gives you

**[19:28]** running that local VAD gives you

**[19:28]** running that local VAD gives you superior performance and it allows you

**[19:31]** superior performance and it allows you

**[19:31]** superior performance and it allows you and it there's not much of a cost hit. I

**[19:32]** and it there's not much of a cost hit. I

**[19:32]** and it there's not much of a cost hit. I mean, it's maybe like a fraction of 1%

**[19:34]** mean, it's maybe like a fraction of 1%

**[19:34]** mean, it's maybe like a fraction of 1% to run a local VAD. Um but yeah, you

**[19:37]** to run a local VAD. Um but yeah, you

**[19:37]** to run a local VAD. Um but yeah, you have all sorts of choices, but we find

**[19:39]** have all sorts of choices, but we find

**[19:39]** have all sorts of choices, but we find we find that to work really well.

**[19:50]** Uh it's integrated with phone carriers,

**[19:50]** Uh it's integrated with phone carriers, too. So there are a ton there are I

**[19:52]** too. So there are a ton there are I

**[19:52]** too. So there are a ton there are I found out I didn't work much with phone.

**[19:54]** found out I didn't work much with phone.

**[19:54]** found out I didn't work much with phone. Verun's been our phone expert, though I

**[19:57]** Verun's been our phone expert, though I

**[19:57]** Verun's been our phone expert, though I don't Verun is like a figure in the

**[19:59]** don't Verun is like a figure in the

**[19:59]** don't Verun is like a figure in the WebRTC community. He's like an author of


### [20:00 - 21:00]

**[20:01]** WebRTC community. He's like an author of

**[20:01]** WebRTC community. He's like an author of many things, but he's also a phone

**[20:03]** many things, but he's also a phone

**[20:03]** many things, but he's also a phone expert, which I don't know if that

**[20:04]** expert, which I don't know if that

**[20:04]** expert, which I don't know if that crosses over too much. Maybe that

**[20:07]** crosses over too much. Maybe that

**[20:07]** crosses over too much. Maybe that happened before. Um,

**[20:11]** happened before. Um,

**[20:11]** happened before. Um, phones are super complicated how you

**[20:13]** phones are super complicated how you

**[20:13]** phones are super complicated how you actually make calls. Uh, Pipcat supports

**[20:15]** actually make calls. Uh, Pipcat supports

**[20:15]** actually make calls. Uh, Pipcat supports all of them. So, maybe a very quick

**[20:17]** all of them. So, maybe a very quick

**[20:17]** all of them. So, maybe a very quick list. You can make a websocket

**[20:19]** list. You can make a websocket

**[20:19]** list. You can make a websocket connection with a phone provider like a

**[20:21]** connection with a phone provider like a

**[20:21]** connection with a phone provider like a Twilio or Telnix or Pivo or Exo Exotel

**[20:25]** Twilio or Telnix or Pivo or Exo Exotel

**[20:25]** Twilio or Telnix or Pivo or Exo Exotel and exchange uh media streams. So that's

**[20:28]** and exchange uh media streams. So that's

**[20:28]** and exchange uh media streams. So that's a way to have just a a native websocket

**[20:30]** a way to have just a a native websocket

**[20:30]** a way to have just a a native websocket connection from Pipcat to Twilio. You'd

**[20:33]** connection from Pipcat to Twilio. You'd

**[20:33]** connection from Pipcat to Twilio. You'd call Twilio. It's going to emit the

**[20:35]** call Twilio. It's going to emit the

**[20:35]** call Twilio. It's going to emit the websocket and there'll be a handshake to

**[20:37]** websocket and there'll be a handshake to

**[20:37]** websocket and there'll be a handshake to get connected. You can also use uh PSTN

**[20:40]** get connected. You can also use uh PSTN

**[20:40]** get connected. You can also use uh PSTN which is a public switch telephone

**[20:43]** which is a public switch telephone

**[20:43]** which is a public switch telephone network

**[20:44]** network

**[20:44]** network uh which is lets you dial in and that's

**[20:46]** uh which is lets you dial in and that's

**[20:46]** uh which is lets you dial in and that's going to be kind of a different

**[20:47]** going to be kind of a different

**[20:47]** going to be kind of a different mechanism. There's also SIP which is its

**[20:49]** mechanism. There's also SIP which is its

**[20:49]** mechanism. There's also SIP which is its own separate thing again and all of the

**[20:52]** own separate thing again and all of the

**[20:52]** own separate thing again and all of the telefan providers would also support

**[20:54]** telefan providers would also support

**[20:54]** telefan providers would also support this as well. With SIP, you would call u

**[20:57]** this as well. With SIP, you would call u

**[20:57]** this as well. With SIP, you would call u something say like Twilio and you would


### [21:00 - 22:00]

**[21:00]** something say like Twilio and you would

**[21:00]** something say like Twilio and you would call into like say a server like uh or a

**[21:03]** call into like say a server like uh or a

**[21:03]** call into like say a server like uh or a SIP provider like daily which is offers

**[21:05]** SIP provider like daily which is offers

**[21:05]** SIP provider like daily which is offers SIP provided rooms and you then have the

**[21:07]** SIP provided rooms and you then have the

**[21:07]** SIP provided rooms and you then have the ability to kind of uh bring the two

**[21:09]** ability to kind of uh bring the two

**[21:09]** ability to kind of uh bring the two together via that SIP connection. The

**[21:11]** together via that SIP connection. The

**[21:11]** together via that SIP connection. The nice thing about SIP is that you have

**[21:13]** nice thing about SIP is that you have

**[21:13]** nice thing about SIP is that you have the ability to have like superior call

**[21:15]** the ability to have like superior call

**[21:15]** the ability to have like superior call control. It does it is slightly more

**[21:18]** control. It does it is slightly more

**[21:18]** control. It does it is slightly more complicated whereas that websocket

**[21:20]** complicated whereas that websocket

**[21:20]** complicated whereas that websocket connection is instantaneous. Your bot

**[21:21]** connection is instantaneous. Your bot

**[21:21]** connection is instantaneous. Your bot needs to be up and running. So there's a

**[21:23]** needs to be up and running. So there's a

**[21:23]** needs to be up and running. So there's a whole we're not going to talk about it

**[21:24]** whole we're not going to talk about it

**[21:24]** whole we're not going to talk about it today, but like cold starts for agents,

**[21:26]** today, but like cold starts for agents,

**[21:26]** today, but like cold starts for agents, they need to start immediately. So if

**[21:28]** they need to start immediately. So if

**[21:28]** they need to start immediately. So if you don't have resources provisioned,

**[21:30]** you don't have resources provisioned,

**[21:30]** you don't have resources provisioned, you don't want your users waiting like

**[21:31]** you don't want your users waiting like

**[21:31]** you don't want your users waiting like 20 seconds while the bot comes online.

**[21:34]** 20 seconds while the bot comes online.

**[21:34]** 20 seconds while the bot comes online. So a longish medium-ish answer for a

**[21:37]** So a longish medium-ish answer for a

**[21:37]** So a longish medium-ish answer for a very complicated question. Maybe you

**[21:39]** very complicated question. Maybe you

**[21:39]** very complicated question. Maybe you didn't know that.

**[21:57]** Yeah. Yeah. Answer that. Yeah. Yeah.

**[21:57]** Yeah. Yeah. Answer that. Yeah. Yeah. Cart Cartisia of


### [22:00 - 23:00]

**[22:01]** Cart Cartisia of

**[22:01]** Cart Cartisia of Yeah. Can you I didn't hear it. Well, I

**[22:03]** Yeah. Can you I didn't hear it. Well, I

**[22:03]** Yeah. Can you I didn't hear it. Well, I think you were you were asking if Pyut

**[22:06]** think you were you were asking if Pyut

**[22:06]** think you were you were asking if Pyut compares to or how it compares to

**[22:08]** compares to or how it compares to

**[22:08]** compares to or how it compares to Cartisia. Is that

**[22:11]** Cartisia. Is that

**[22:11]** Cartisia. Is that Yeah, Cartisia is a well I think they're

**[22:13]** Yeah, Cartisia is a well I think they're

**[22:14]** Yeah, Cartisia is a well I think they're going to do more stuff but as of today

**[22:16]** going to do more stuff but as of today

**[22:16]** going to do more stuff but as of today it's a texttospech service and you can

**[22:19]** it's a texttospech service and you can

**[22:19]** it's a texttospech service and you can clone your voice or you can you know and

**[22:22]** clone your voice or you can you know and

**[22:22]** clone your voice or you can you know and then they provide a real time uh API you

**[22:25]** then they provide a real time uh API you

**[22:25]** then they provide a real time uh API you can just via websockets you pass the

**[22:27]** can just via websockets you pass the

**[22:27]** can just via websockets you pass the text and they reply with with audio

**[22:30]** text and they reply with with audio

**[22:30]** text and they reply with with audio basically with audio frames and then

**[22:32]** basically with audio frames and then

**[22:32]** basically with audio frames and then pipecat integrates with cartisia as any

**[22:34]** pipecat integrates with cartisia as any

**[22:34]** pipecat integrates with cartisia as any other texttospech service like 11 laps

**[22:37]** other texttospech service like 11 laps

**[22:37]** other texttospech service like 11 laps or or anything like think about pipe cut

**[22:41]** or or anything like think about pipe cut

**[22:41]** or or anything like think about pipe cut as a it's just a framework for

**[22:43]** as a it's just a framework for

**[22:43]** as a it's just a framework for developers where they can plug and play

**[22:45]** developers where they can plug and play

**[22:45]** developers where they can plug and play the service they want. So they can plug

**[22:47]** the service they want. So they can plug

**[22:47]** the service they want. So they can plug and they can take Cartisia they can put

**[22:49]** and they can take Cartisia they can put

**[22:49]** and they can take Cartisia they can put Cartisia they can take it out put 11

**[22:51]** Cartisia they can take it out put 11

**[22:52]** Cartisia they can take it out put 11 laps. Oops even closer. Okay now I can

**[22:56]** laps. Oops even closer. Okay now I can

**[22:56]** laps. Oops even closer. Okay now I can hear myself. Um

**[22:59]** hear myself. Um

**[22:59]** hear myself. Um yeah you can plug and play any service


### [23:00 - 24:00]

**[23:01]** yeah you can plug and play any service

**[23:01]** yeah you can plug and play any service you want like you can change llm you can

**[23:03]** you want like you can change llm you can

**[23:03]** you want like you can change llm you can use llama you can use anthropic you can

**[23:06]** use llama you can use anthropic you can

**[23:06]** use llama you can use anthropic you can use uh cartisia or 11 labs then for uh

**[23:10]** use uh cartisia or 11 labs then for uh

**[23:10]** use uh cartisia or 11 labs then for uh speech to text you can use deepgram gram

**[23:12]** speech to text you can use deepgram gram

**[23:12]** speech to text you can use deepgram gram or you can use one box like gemini live

**[23:15]** or you can use one box like gemini live

**[23:15]** or you can use one box like gemini live which has all that uh built for you so

**[23:19]** which has all that uh built for you so

**[23:20]** which has all that uh built for you so is that that clear Yeah. Okay.


### [24:00 - 25:00]

**[24:21]** I I'm not sure if I understood. Are you

**[24:21]** I I'm not sure if I understood. Are you talking like how to ensure that the LLM

**[24:24]** talking like how to ensure that the LLM

**[24:24]** talking like how to ensure that the LLM says what the right thing or not the

**[24:28]** says what the right thing or not the

**[24:28]** says what the right thing or not the right thing? Yeah. Well, Pipcat doesn't

**[24:31]** right thing? Yeah. Well, Pipcat doesn't

**[24:31]** right thing? Yeah. Well, Pipcat doesn't have control about that. It's up to you

**[24:34]** have control about that. It's up to you

**[24:34]** have control about that. It's up to you to define the prompt or define how the

**[24:36]** to define the prompt or define how the

**[24:36]** to define the prompt or define how the LLM will um uh will reply. You can put

**[24:42]** LLM will um uh will reply. You can put

**[24:42]** LLM will um uh will reply. You can put if you want you can put uh you'll be

**[24:44]** if you want you can put uh you'll be

**[24:44]** if you want you can put uh you'll be able to write your own processors that

**[24:46]** able to write your own processors that

**[24:46]** able to write your own processors that we call them those little boxes and

**[24:49]** we call them those little boxes and

**[24:49]** we call them those little boxes and check what the LLM has said for example

**[24:52]** check what the LLM has said for example

**[24:52]** check what the LLM has said for example before it's um like put some kind of

**[24:56]** before it's um like put some kind of

**[24:56]** before it's um like put some kind of real time eval like to to make sure uh

**[24:59]** real time eval like to to make sure uh

**[24:59]** real time eval like to to make sure uh that the LLM has you could you could do


### [25:00 - 26:00]

**[25:01]** that the LLM has you could you could do

**[25:01]** that the LLM has you could you could do that. Yeah, you the all that that

**[25:04]** that. Yeah, you the all that that

**[25:04]** that. Yeah, you the all that that pipeline is very flexible. So you can

**[25:07]** pipeline is very flexible. So you can

**[25:07]** pipeline is very flexible. So you can you can you can put whatever you want

**[25:09]** you can you can put whatever you want

**[25:09]** you can you can put whatever you want there like in parallel not in parallel.

**[25:11]** there like in parallel not in parallel.

**[25:12]** there like in parallel not in parallel. For example, Mark was saying about

**[25:13]** For example, Mark was saying about

**[25:13]** For example, Mark was saying about parallel pipelines. Like if you have

**[25:16]** parallel pipelines. Like if you have

**[25:16]** parallel pipelines. Like if you have video and audio at the same time. Uh

**[25:19]** video and audio at the same time. Uh

**[25:19]** video and audio at the same time. Uh with Gemini Live, you can do everything

**[25:20]** with Gemini Live, you can do everything

**[25:20]** with Gemini Live, you can do everything in one box. But let's say you don't have

**[25:22]** in one box. But let's say you don't have

**[25:22]** in one box. But let's say you don't have Gemini Live, you want to use other uh

**[25:25]** Gemini Live, you want to use other uh

**[25:25]** Gemini Live, you want to use other uh other services that one does video and

**[25:27]** other services that one does video and

**[25:27]** other services that one does video and that the other one does audio. You can

**[25:29]** that the other one does audio. You can

**[25:29]** that the other one does audio. You can have a parallel pipeline which you know

**[25:31]** have a parallel pipeline which you know

**[25:31]** have a parallel pipeline which you know it's like a tree, right? You have your

**[25:33]** it's like a tree, right? You have your

**[25:33]** it's like a tree, right? You have your transport input and then if it's audio,

**[25:36]** transport input and then if it's audio,

**[25:36]** transport input and then if it's audio, it goes this way. If it's video, it goes

**[25:38]** it goes this way. If it's video, it goes

**[25:38]** it goes this way. If it's video, it goes that that way. And you can um you can do

**[25:41]** that that way. And you can um you can do

**[25:41]** that that way. And you can um you can do things dynamically like like that. Yeah.

**[25:44]** things dynamically like like that. Yeah.

**[25:44]** things dynamically like like that. Yeah. This next question. Yeah.


### [26:00 - 27:00]

**[26:17]** Okay. So the question was um are guard

**[26:17]** Okay. So the question was um are guard are guardrails requirements and do how

**[26:20]** are guardrails requirements and do how

**[26:20]** are guardrails requirements and do how do people use them and how does that

**[26:23]** do people use them and how does that

**[26:23]** do people use them and how does that apply for speechtospech models? So the

**[26:25]** apply for speechtospech models? So the

**[26:25]** apply for speechtospech models? So the answer is they're not required. In there

**[26:27]** answer is they're not required. In there

**[26:27]** answer is they're not required. In there is a challenge here and actually uh I

**[26:30]** is a challenge here and actually uh I

**[26:30]** is a challenge here and actually uh I talked about this on like one of the

**[26:31]** talked about this on like one of the

**[26:32]** talked about this on like one of the first slides. Latency is absolutely

**[26:34]** first slides. Latency is absolutely

**[26:34]** first slides. Latency is absolutely critical. So what you want to avoid are

**[26:36]** critical. So what you want to avoid are

**[26:36]** critical. So what you want to avoid are unnecessary turns. You know obviously

**[26:38]** unnecessary turns. You know obviously

**[26:38]** unnecessary turns. You know obviously LLMs are amazing language processors. So

**[26:40]** LLMs are amazing language processors. So

**[26:40]** LLMs are amazing language processors. So if you had all the time in the world you

**[26:42]** if you had all the time in the world you

**[26:42]** if you had all the time in the world you could do hallucination checking against

**[26:44]** could do hallucination checking against

**[26:44]** could do hallucination checking against the LM. There are other strategies to

**[26:47]** the LM. There are other strategies to

**[26:47]** the LM. There are other strategies to handle this. One of the big things is

**[26:49]** handle this. One of the big things is

**[26:49]** handle this. One of the big things is that we see because of the aggregate

**[26:51]** that we see because of the aggregate

**[26:51]** that we see because of the aggregate nature of the context, it grows over the

**[26:54]** nature of the context, it grows over the

**[26:54]** nature of the context, it grows over the course of the conversation. You actually

**[26:55]** course of the conversation. You actually

**[26:55]** course of the conversation. You actually you can find better um better accuracy

**[26:59]** you can find better um better accuracy

**[26:59]** you can find better um better accuracy with the responses if you have more


### [27:00 - 28:00]

**[27:01]** with the responses if you have more

**[27:01]** with the responses if you have more control over how you prompt the LLM. So

**[27:04]** control over how you prompt the LLM. So

**[27:04]** control over how you prompt the LLM. So this is uh a whole topic and talk in

**[27:06]** this is uh a whole topic and talk in

**[27:06]** this is uh a whole topic and talk in itself. Uh what we found is there are

**[27:09]** itself. Uh what we found is there are

**[27:09]** itself. Uh what we found is there are two ways to handle this. Well, at least

**[27:11]** two ways to handle this. Well, at least

**[27:11]** two ways to handle this. Well, at least two. Um one if you for a lot of

**[27:14]** two. Um one if you for a lot of

**[27:14]** two. Um one if you for a lot of conversations they're going to be task

**[27:15]** conversations they're going to be task

**[27:16]** conversations they're going to be task oriented. So let's say uh something

**[27:18]** oriented. So let's say uh something

**[27:18]** oriented. So let's say uh something simple like a restaurant reservation

**[27:19]** simple like a restaurant reservation

**[27:20]** simple like a restaurant reservation bot. It may have to take your name, get

**[27:21]** bot. It may have to take your name, get

**[27:21]** bot. It may have to take your name, get your time, log the time to a database.

**[27:24]** your time, log the time to a database.

**[27:24]** your time, log the time to a database. You can chunk that out, even that small

**[27:26]** You can chunk that out, even that small

**[27:26]** You can chunk that out, even that small conversation into just discrete tasks.

**[27:28]** conversation into just discrete tasks.

**[27:28]** conversation into just discrete tasks. And LLMs are really good at uh following

**[27:31]** And LLMs are really good at uh following

**[27:31]** And LLMs are really good at uh following the most recent input. So if you kind of

**[27:34]** the most recent input. So if you kind of

**[27:34]** the most recent input. So if you kind of feed it task by task, that helps. Also,

**[27:38]** feed it task by task, that helps. Also,

**[27:38]** feed it task by task, that helps. Also, if you control the context window, like

**[27:39]** if you control the context window, like

**[27:39]** if you control the context window, like the size, it can really be beneficial to

**[27:42]** the size, it can really be beneficial to

**[27:42]** the size, it can really be beneficial to kind of manage that really judiciously.

**[27:44]** kind of manage that really judiciously.

**[27:44]** kind of manage that really judiciously. So you could either reset um one example

**[27:47]** So you could either reset um one example

**[27:47]** So you could either reset um one example might be let's say you're building a

**[27:49]** might be let's say you're building a

**[27:49]** might be let's say you're building a patient intake bot at a doctor's office.

**[27:50]** patient intake bot at a doctor's office.

**[27:50]** patient intake bot at a doctor's office. They may the very first thing it may do

**[27:52]** They may the very first thing it may do

**[27:52]** They may the very first thing it may do is verify the date of birth which serves

**[27:55]** is verify the date of birth which serves

**[27:55]** is verify the date of birth which serves no utility beyond just the very first

**[27:57]** no utility beyond just the very first

**[27:57]** no utility beyond just the very first you know checkpoint. So you may actually

**[27:59]** you know checkpoint. So you may actually

**[27:59]** you know checkpoint. So you may actually remove that from the context like


### [28:00 - 29:00]

**[28:00]** remove that from the context like

**[28:00]** remove that from the context like completely get it out of there because

**[28:01]** completely get it out of there because

**[28:02]** completely get it out of there because otherwise it's just cruff that hangs on

**[28:04]** otherwise it's just cruff that hangs on

**[28:04]** otherwise it's just cruff that hangs on and instead you kind of reset and then

**[28:06]** and instead you kind of reset and then

**[28:06]** and instead you kind of reset and then maybe roll through the tasks. You could

**[28:08]** maybe roll through the tasks. You could

**[28:08]** maybe roll through the tasks. You could also for really really long

**[28:09]** also for really really long

**[28:09]** also for really really long conversations summarize the the context.

**[28:12]** conversations summarize the the context.

**[28:12]** conversations summarize the the context. So you you may want to do an outofband

**[28:14]** So you you may want to do an outofband

**[28:14]** So you you may want to do an outofband LLM call. This is something actually

**[28:16]** LLM call. This is something actually

**[28:16]** LLM call. This is something actually Quinn just we talked internally about

**[28:17]** Quinn just we talked internally about

**[28:17]** Quinn just we talked internally about this that we're going to see more and

**[28:19]** this that we're going to see more and

**[28:19]** this that we're going to see more and more of this mixture of LLMs where even

**[28:22]** more of this mixture of LLMs where even

**[28:22]** more of this mixture of LLMs where even in the context of real time you may have

**[28:24]** in the context of real time you may have

**[28:24]** in the context of real time you may have an outofband like REST call to the to

**[28:27]** an outofband like REST call to the to

**[28:27]** an outofband like REST call to the to the textbased LLM just to do a summary

**[28:29]** the textbased LLM just to do a summary

**[28:29]** the textbased LLM just to do a summary and then return it back so that you can

**[28:31]** and then return it back so that you can

**[28:31]** and then return it back so that you can kind of compress that context window.

**[28:33]** kind of compress that context window.

**[28:33]** kind of compress that context window. And just to give a call out to Google,

**[28:35]** And just to give a call out to Google,

**[28:35]** And just to give a call out to Google, the the live API, so maybe transitioning

**[28:37]** the the live API, so maybe transitioning

**[28:37]** the the live API, so maybe transitioning there, they offer context uh management

**[28:39]** there, they offer context uh management

**[28:39]** there, they offer context uh management through a bunch of different different

**[28:41]** through a bunch of different different

**[28:41]** through a bunch of different different strategies like a rolling they have a

**[28:42]** strategies like a rolling they have a

**[28:42]** strategies like a rolling they have a rolling window or sliding window. I

**[28:44]** rolling window or sliding window. I

**[28:44]** rolling window or sliding window. I think they offer like token caps for

**[28:46]** think they offer like token caps for

**[28:46]** think they offer like token caps for that. So you can have some control or if

**[28:48]** that. So you can have some control or if

**[28:48]** that. So you can have some control or if you want you can output text and then

**[28:50]** you want you can output text and then

**[28:50]** you want you can output text and then kind of do whatever you want with it.

**[28:52]** kind of do whatever you want with it.

**[28:52]** kind of do whatever you want with it. They also take text input. So there's a

**[28:53]** They also take text input. So there's a

**[28:53]** They also take text input. So there's a lot of a lot of flexibility with

**[28:55]** lot of a lot of flexibility with

**[28:55]** lot of a lot of flexibility with speechtoech models. They do offer or

**[28:57]** speechtoech models. They do offer or

**[28:58]** speechtoech models. They do offer or they do pose some other maybe

**[28:59]** they do pose some other maybe


### [29:00 - 30:00]

**[29:00]** they do pose some other maybe development challenges but offer like

**[29:01]** development challenges but offer like

**[29:01]** development challenges but offer like tremendous benefits in terms of the

**[29:03]** tremendous benefits in terms of the

**[29:03]** tremendous benefits in terms of the features they offer. All right, I'm

**[29:05]** features they offer. All right, I'm

**[29:05]** features they offer. All right, I'm gonna

**[29:06]** gonna

**[29:06]** gonna I'm gonna hold questions just for a sec

**[29:08]** I'm gonna hold questions just for a sec

**[29:08]** I'm gonna hold questions just for a sec because I I've heard the Wi-Fi is back.

**[29:10]** because I I've heard the Wi-Fi is back.

**[29:10]** because I I've heard the Wi-Fi is back. Can folks try downloading the repo again

**[29:12]** Can folks try downloading the repo again

**[29:12]** Can folks try downloading the repo again because I Slack channel. Yes, Quinn, can

**[29:16]** because I Slack channel. Yes, Quinn, can

**[29:16]** because I Slack channel. Yes, Quinn, can you maybe come to the mic and I can't

**[29:18]** you maybe come to the mic and I can't

**[29:18]** you maybe come to the mic and I can't remember what you told me.

**[29:21]** remember what you told me.

**[29:21]** remember what you told me. workshop voice gemini pipecat with

**[29:23]** workshop voice gemini pipecat with

**[29:24]** workshop voice gemini pipecat with dashes in between on AI engineer Slack.

**[29:28]** dashes in between on AI engineer Slack.

**[29:28]** dashes in between on AI engineer Slack. Okay, does everyone know where that is?

**[29:29]** Okay, does everyone know where that is?

**[29:29]** Okay, does everyone know where that is? I know this is like day one hour three.

**[29:32]** I know this is like day one hour three.

**[29:32]** I know this is like day one hour three. Workshop-Voice-geemini-pipecat

**[29:35]** Workshop-Voice-geemini-pipecat

**[29:35]** Workshop-Voice-geemini-pipecat is the channel name. So if you go to the

**[29:37]** is the channel name. So if you go to the

**[29:37]** is the channel name. So if you go to the engineer and search for workshop, it

**[29:40]** engineer and search for workshop, it

**[29:40]** engineer and search for workshop, it should come up

**[29:51]** you raise your

**[29:51]** you raise your Can people join like do they have do you

**[29:54]** Can people join like do they have do you

**[29:54]** Can people join like do they have do you guys have access to the Slack AI

**[29:55]** guys have access to the Slack AI

**[29:55]** guys have access to the Slack AI engineer Slack?


### [30:00 - 31:00]

**[30:18]** There should be the join a Slack group.

**[30:18]** There should be the join a Slack group. All right. I'd say I'm going to I'll

**[30:20]** All right. I'd say I'm going to I'll

**[30:20]** All right. I'd say I'm going to I'll take that one then I'll walk over if I

**[30:21]** take that one then I'll walk over if I

**[30:21]** take that one then I'll walk over if I could let's just try maybe could listen

**[30:23]** could let's just try maybe could listen

**[30:23]** could let's just try maybe could listen and also try to get the repo. I'd like

**[30:25]** and also try to get the repo. I'd like

**[30:25]** and also try to get the repo. I'd like to walk through the quick start and then

**[30:27]** to walk through the quick start and then

**[30:27]** to walk through the quick start and then we can look at some examples.

**[30:43]** I you know it's something actually uh

**[30:43]** I you know it's something actually uh Quinn has done a ton of work with this.

**[30:44]** Quinn has done a ton of work with this.

**[30:44]** Quinn has done a ton of work with this. I have not personally. I mean there's

**[30:46]** I have not personally. I mean there's

**[30:46]** I have not personally. I mean there's obviously massive latency benefits

**[30:47]** obviously massive latency benefits

**[30:47]** obviously massive latency benefits because you cut out network round trips

**[30:49]** because you cut out network round trips

**[30:49]** because you cut out network round trips all over the place. So you save a ton

**[30:51]** all over the place. So you save a ton

**[30:51]** all over the place. So you save a ton and depending on where you are in the

**[30:52]** and depending on where you are in the

**[30:52]** and depending on where you are in the world that can save a lot if you're

**[30:53]** world that can save a lot if you're

**[30:54]** world that can save a lot if you're US-based. You know your network latency

**[30:55]** US-based. You know your network latency

**[30:55]** US-based. You know your network latency is going to be relatively low. But a lot

**[30:58]** is going to be relatively low. But a lot

**[30:58]** is going to be relatively low. But a lot of the developers in the community are

**[30:59]** of the developers in the community are

**[30:59]** of the developers in the community are in Europe and a lot of these AI services


### [31:00 - 32:00]

**[31:01]** in Europe and a lot of these AI services

**[31:01]** in Europe and a lot of these AI services are relatively new with you know data

**[31:04]** are relatively new with you know data

**[31:04]** are relatively new with you know data centers only in the US. So there are

**[31:07]** centers only in the US. So there are

**[31:07]** centers only in the US. So there are different challenges when doing that

**[31:08]** different challenges when doing that

**[31:08]** different challenges when doing that though when running it you it actually

**[31:10]** though when running it you it actually

**[31:10]** though when running it you it actually there are great um hosting providers

**[31:12]** there are great um hosting providers

**[31:12]** there are great um hosting providers like modal that offer really good

**[31:13]** like modal that offer really good

**[31:13]** like modal that offer really good options for running like your own local

**[31:16]** options for running like your own local

**[31:16]** options for running like your own local LLM which then you're not you know

**[31:17]** LLM which then you're not you know

**[31:17]** LLM which then you're not you know you're buying or I guess leasing like

**[31:19]** you're buying or I guess leasing like

**[31:19]** you're buying or I guess leasing like the GPU time instead of running

**[31:21]** the GPU time instead of running

**[31:21]** the GPU time instead of running everything on a GPU which would probably

**[31:22]** everything on a GPU which would probably

**[31:22]** everything on a GPU which would probably be cost prohibitive because because of

**[31:24]** be cost prohibitive because because of

**[31:24]** be cost prohibitive because because of the way processes run but that's a that

**[31:27]** the way processes run but that's a that

**[31:27]** the way processes run but that's a that is also a talk in itself. Um, next

**[31:30]** is also a talk in itself. Um, next

**[31:30]** is also a talk in itself. Um, next question.

**[31:58]** Well, the large context windows

**[31:58]** Well, the large context windows definitely cause LLMs to process slower.


### [32:00 - 33:00]

**[32:00]** definitely cause LLMs to process slower.

**[32:00]** definitely cause LLMs to process slower. Um, yeah, I'm sorry. The question was

**[32:03]** Um, yeah, I'm sorry. The question was

**[32:03]** Um, yeah, I'm sorry. The question was around state management with um with

**[32:06]** around state management with um with

**[32:06]** around state management with um with LLMs and whether it's better to I guess

**[32:08]** LLMs and whether it's better to I guess

**[32:08]** LLMs and whether it's better to I guess chunk or have more kind of deterministic

**[32:10]** chunk or have more kind of deterministic

**[32:10]** chunk or have more kind of deterministic input versus just a large context where

**[32:12]** input versus just a large context where

**[32:12]** input versus just a large context where you just dump everything in. This is

**[32:14]** you just dump everything in. This is

**[32:14]** you just dump everything in. This is actually an extension of what the other

**[32:15]** actually an extension of what the other

**[32:15]** actually an extension of what the other gentleman was asking. Um the idea being

**[32:20]** gentleman was asking. Um the idea being

**[32:20]** gentleman was asking. Um the idea being that uh and actually so daily we built

**[32:23]** that uh and actually so daily we built

**[32:23]** that uh and actually so daily we built the chat widget that's on the homepage

**[32:26]** the chat widget that's on the homepage

**[32:26]** the chat widget that's on the homepage of the voice AI world's fair uh page. I

**[32:30]** of the voice AI world's fair uh page. I

**[32:30]** of the voice AI world's fair uh page. I I personally built that. What was

**[32:33]** I personally built that. What was

**[32:33]** I personally built that. What was interesting there is that um in Alles

**[32:34]** interesting there is that um in Alles

**[32:34]** interesting there is that um in Alles and I were just talking about this

**[32:35]** and I were just talking about this

**[32:35]** and I were just talking about this function calls in the context of real

**[32:38]** function calls in the context of real

**[32:38]** function calls in the context of real time are still slow unfortunately like

**[32:40]** time are still slow unfortunately like

**[32:40]** time are still slow unfortunately like too slow. Um actually Gemini I'll give

**[32:44]** too slow. Um actually Gemini I'll give

**[32:44]** too slow. Um actually Gemini I'll give more props to Gemini being like maybe

**[32:45]** more props to Gemini being like maybe

**[32:45]** more props to Gemini being like maybe one of the fastest. If you run like a

**[32:47]** one of the fastest. If you run like a

**[32:47]** one of the fastest. If you run like a basic local like one of these demos and

**[32:49]** basic local like one of these demos and

**[32:49]** basic local like one of these demos and you ask it what the weather is, it will

**[32:50]** you ask it what the weather is, it will

**[32:50]** you ask it what the weather is, it will return back with time to first bite in I

**[32:53]** return back with time to first bite in I

**[32:53]** return back with time to first bite in I don't know less than 500 milliseconds

**[32:56]** don't know less than 500 milliseconds

**[32:56]** don't know less than 500 milliseconds whereas other vendors not trying to

**[32:57]** whereas other vendors not trying to

**[32:57]** whereas other vendors not trying to throw open AI under the bus. But it has

**[32:59]** throw open AI under the bus. But it has

**[32:59]** throw open AI under the bus. But it has gotten slower like the you might see


### [33:00 - 34:00]

**[33:01]** gotten slower like the you might see

**[33:02]** gotten slower like the you might see upwards of 1.5 to two seconds of waiting

**[33:04]** upwards of 1.5 to two seconds of waiting

**[33:04]** upwards of 1.5 to two seconds of waiting just to get that first token back and we

**[33:07]** just to get that first token back and we

**[33:07]** just to get that first token back and we dug into actually this is just something

**[33:08]** dug into actually this is just something

**[33:08]** dug into actually this is just something recently this morning. The issue is when

**[33:10]** recently this morning. The issue is when

**[33:10]** recently this morning. The issue is when you get the normal streamed response for

**[33:11]** you get the normal streamed response for

**[33:11]** you get the normal streamed response for the conversation you can start playing

**[33:13]** the conversation you can start playing

**[33:13]** the conversation you can start playing that audio out once you get the first

**[33:14]** that audio out once you get the first

**[33:14]** that audio out once you get the first sentence. The issue being when you get a

**[33:16]** sentence. The issue being when you get a

**[33:16]** sentence. The issue being when you get a tool, you need the entire JSON response

**[33:18]** tool, you need the entire JSON response

**[33:18]** tool, you need the entire JSON response before you can actually do anything with

**[33:20]** before you can actually do anything with

**[33:20]** before you can actually do anything with it. So that's slow. Uh that's one part

**[33:23]** it. So that's slow. Uh that's one part

**[33:23]** it. So that's slow. Uh that's one part of it. Se separately chunking the

**[33:25]** of it. Se separately chunking the

**[33:25]** of it. Se separately chunking the prompts is absolutely the way to go. Uh

**[33:27]** prompts is absolutely the way to go. Uh

**[33:27]** prompts is absolutely the way to go. Uh in building that world's fair bot, um I

**[33:30]** in building that world's fair bot, um I

**[33:30]** in building that world's fair bot, um I was kind of balancing between the two

**[33:32]** was kind of balancing between the two

**[33:32]** was kind of balancing between the two worlds because uh you can talk to it and

**[33:34]** worlds because uh you can talk to it and

**[33:34]** worlds because uh you can talk to it and ask it about speakers for the session.

**[33:37]** ask it about speakers for the session.

**[33:37]** ask it about speakers for the session. route one would have said let's use like

**[33:39]** route one would have said let's use like

**[33:39]** route one would have said let's use like a mag approach and put all of the the

**[33:42]** a mag approach and put all of the the

**[33:42]** a mag approach and put all of the the speaker JSON in something that could be

**[33:44]** speaker JSON in something that could be

**[33:44]** speaker JSON in something that could be a tool that could be accessed and I

**[33:46]** a tool that could be accessed and I

**[33:46]** a tool that could be accessed and I tried that and unfortunately it's just a

**[33:48]** tried that and unfortunately it's just a

**[33:48]** tried that and unfortunately it's just a little too slow. It's a giant context.

**[33:50]** little too slow. It's a giant context.

**[33:50]** little too slow. It's a giant context. It takes a while to come back. What's

**[33:52]** It takes a while to come back. What's

**[33:52]** It takes a while to come back. What's interesting is if you instead move that

**[33:54]** interesting is if you instead move that

**[33:54]** interesting is if you instead move that all just directly into the context with

**[33:55]** all just directly into the context with

**[33:56]** all just directly into the context with Gemini live it's a little bit variable

**[33:58]** Gemini live it's a little bit variable

**[33:58]** Gemini live it's a little bit variable but under good conditions you'll get a


### [34:00 - 35:00]

**[34:00]** but under good conditions you'll get a

**[34:00]** but under good conditions you'll get a response back on that like 800

**[34:02]** response back on that like 800

**[34:02]** response back on that like 800 millisecond latency. So it actually has

**[34:04]** millisecond latency. So it actually has

**[34:04]** millisecond latency. So it actually has access to like the full context. The one

**[34:07]** access to like the full context. The one

**[34:07]** access to like the full context. The one tradeoff though is what this gentleman

**[34:09]** tradeoff though is what this gentleman

**[34:09]** tradeoff though is what this gentleman over here was asking is accuracy. It's

**[34:11]** over here was asking is accuracy. It's

**[34:11]** over here was asking is accuracy. It's going to get confused because especially

**[34:12]** going to get confused because especially

**[34:12]** going to get confused because especially when you get a JSON with a lot of

**[34:13]** when you get a JSON with a lot of

**[34:14]** when you get a JSON with a lot of speaker and this isn't this is all LMS.

**[34:16]** speaker and this isn't this is all LMS.

**[34:16]** speaker and this isn't this is all LMS. It's not specifically Gemini with that

**[34:18]** It's not specifically Gemini with that

**[34:18]** It's not specifically Gemini with that type of even structured data becomes

**[34:20]** type of even structured data becomes

**[34:20]** type of even structured data becomes very hard to kind of discern what's what

**[34:21]** very hard to kind of discern what's what

**[34:22]** very hard to kind of discern what's what when a lot of it looks the same. So it's

**[34:24]** when a lot of it looks the same. So it's

**[34:24]** when a lot of it looks the same. So it's all I mean a lot of this is emerging

**[34:26]** all I mean a lot of this is emerging

**[34:26]** all I mean a lot of this is emerging like other things in in AI trying to

**[34:28]** like other things in in AI trying to

**[34:28]** like other things in in AI trying to just do it as fast as possible with

**[34:29]** just do it as fast as possible with

**[34:30]** just do it as fast as possible with voice. Before I take one more question,

**[34:31]** voice. Before I take one more question,

**[34:31]** voice. Before I take one more question, I want to check in on have folks have

**[34:35]** I want to check in on have folks have

**[34:35]** I want to check in on have folks have any luck with the repo? Got a thumbs up.

**[34:37]** any luck with the repo? Got a thumbs up.

**[34:37]** any luck with the repo? Got a thumbs up. All right, I'm going to pause on

**[34:38]** All right, I'm going to pause on

**[34:38]** All right, I'm going to pause on questions for the time being. We can

**[34:40]** questions for the time being. We can

**[34:40]** questions for the time being. We can take them at the tail end. I do want to

**[34:42]** take them at the tail end. I do want to

**[34:42]** take them at the tail end. I do want to try to go through the quick start if we

**[34:44]** try to go through the quick start if we

**[34:44]** try to go through the quick start if we could


### [35:00 - 36:00]

**[35:04]** Okay, great. So, I would recommend um

**[35:04]** Okay, great. So, I would recommend um maybe we'll just take like a few minutes

**[35:05]** maybe we'll just take like a few minutes

**[35:06]** maybe we'll just take like a few minutes of independent getting set up. If you

**[35:09]** of independent getting set up. If you

**[35:09]** of independent getting set up. If you all go to the read me on

**[35:11]** all go to the read me on

**[35:12]** all go to the read me on in the Gemini Pipecat workshop. And if

**[35:14]** in the Gemini Pipecat workshop. And if

**[35:14]** in the Gemini Pipecat workshop. And if you'd roll through the first few steps,

**[35:17]** you'd roll through the first few steps,

**[35:17]** you'd roll through the first few steps, maybe get a I don't know, a hand up. You

**[35:20]** maybe get a I don't know, a hand up. You

**[35:20]** maybe get a I don't know, a hand up. You could just flash it up real quick so I

**[35:21]** could just flash it up real quick so I

**[35:21]** could just flash it up real quick so I could see when people start to get

**[35:22]** could see when people start to get

**[35:22]** could see when people start to get through it. You don't have to hold it

**[35:23]** through it. You don't have to hold it

**[35:24]** through it. You don't have to hold it up. If you don't mind if you brought a

**[35:26]** up. If you don't mind if you brought a

**[35:26]** up. If you don't mind if you brought a device. Okay, we've got one,

**[35:29]** device. Okay, we've got one,

**[35:29]** device. Okay, we've got one, two.

**[35:37]** Ah, so for this workshop, I have leaked

**[35:37]** Ah, so for this workshop, I have leaked my key, a key from one of my accounts,

**[35:39]** my key, a key from one of my accounts,

**[35:39]** my key, a key from one of my accounts, which I'll cycle after this. So, you

**[35:40]** which I'll cycle after this. So, you

**[35:40]** which I'll cycle after this. So, you don't need to sign up for a daily

**[35:41]** don't need to sign up for a daily

**[35:41]** don't need to sign up for a daily account. You do need to sign up for a

**[35:44]** account. You do need to sign up for a

**[35:44]** account. You do need to sign up for a Gemini account. I don't have a key I can

**[35:46]** Gemini account. I don't have a key I can

**[35:46]** Gemini account. I don't have a key I can just give out. So, in the

**[35:48]** just give out. So, in the

**[35:48]** just give out. So, in the environment.example, you'll see there's

**[35:50]** environment.example, you'll see there's

**[35:50]** environment.example, you'll see there's already a daily key which you can use.

**[35:54]** already a daily key which you can use.

**[35:54]** already a daily key which you can use. Do people know how to sign up for

**[35:55]** Do people know how to sign up for

**[35:55]** Do people know how to sign up for Gemini? I have it in the readme. Is

**[35:58]** Gemini? I have it in the readme. Is

**[35:58]** Gemini? I have it in the readme. Is through AI studio. Is that a good spot

**[35:59]** through AI studio. Is that a good spot

**[35:59]** through AI studio. Is that a good spot to do it? Okay. So,


### [36:00 - 37:00]

**[36:17]** All right, I'll take a question while

**[36:17]** All right, I'll take a question while we're waiting.

**[36:28]** We

**[36:28]** We So, in terms of um the pipe, that's a

**[36:30]** So, in terms of um the pipe, that's a

**[36:30]** So, in terms of um the pipe, that's a good question. In terms of the pipecat

**[36:32]** good question. In terms of the pipecat

**[36:32]** good question. In terms of the pipecat interface, you interface with the

**[36:35]** interface, you interface with the

**[36:35]** interface, you interface with the pipecat class. So there's a service

**[36:36]** pipecat class. So there's a service

**[36:36]** pipecat class. So there's a service class and within pipcat, so how you

**[36:38]** class and within pipcat, so how you

**[36:38]** class and within pipcat, so how you write your application code is going to

**[36:40]** write your application code is going to

**[36:40]** write your application code is going to be uniform across all of the services.

**[36:43]** be uniform across all of the services.

**[36:43]** be uniform across all of the services. The individual um providers haven't

**[36:46]** The individual um providers haven't

**[36:46]** The individual um providers haven't really unlike the textbased LLM, they

**[36:48]** really unlike the textbased LLM, they

**[36:48]** really unlike the textbased LLM, they haven't really settled on kind of a a

**[36:49]** haven't really settled on kind of a a

**[36:49]** haven't really settled on kind of a a standard. So pipecat handles all that

**[36:52]** standard. So pipecat handles all that

**[36:52]** standard. So pipecat handles all that translation on your behalf. And I think

**[36:54]** translation on your behalf. And I think

**[36:54]** translation on your behalf. And I think there are other frameworks that do

**[36:55]** there are other frameworks that do

**[36:55]** there are other frameworks that do similar things. The idea is to provide

**[36:57]** similar things. The idea is to provide

**[36:57]** similar things. The idea is to provide like a uniform simple interface. Uh so


### [37:00 - 38:00]

**[37:00]** like a uniform simple interface. Uh so

**[37:00]** like a uniform simple interface. Uh so that you could take and this is part of

**[37:01]** that you could take and this is part of

**[37:01]** that you could take and this is part of the modularity. If you wanted to, you

**[37:04]** the modularity. If you wanted to, you

**[37:04]** the modularity. If you wanted to, you could swap this bot out for OpenAI real

**[37:07]** could swap this bot out for OpenAI real

**[37:07]** could swap this bot out for OpenAI real time or you know a textbased model with

**[37:10]** time or you know a textbased model with

**[37:10]** time or you know a textbased model with a TTS and ST paired with it. That's kind

**[37:13]** a TTS and ST paired with it. That's kind

**[37:13]** a TTS and ST paired with it. That's kind of the whole whole idea. There is maybe

**[37:14]** of the whole whole idea. There is maybe

**[37:14]** of the whole whole idea. There is maybe a little bit in terms of uh the one

**[37:17]** a little bit in terms of uh the one

**[37:17]** a little bit in terms of uh the one thing LLM providers maybe I don't know

**[37:19]** thing LLM providers maybe I don't know

**[37:19]** thing LLM providers maybe I don't know if anybody here can nudge anyone you

**[37:21]** if anybody here can nudge anyone you

**[37:21]** if anybody here can nudge anyone you know the system instruction or system

**[37:24]** know the system instruction or system

**[37:24]** know the system instruction or system prompt is not unifor uniformly dealt

**[37:26]** prompt is not unifor uniformly dealt

**[37:26]** prompt is not unifor uniformly dealt with I don't know if that's well

**[37:27]** with I don't know if that's well

**[37:27]** with I don't know if that's well understood but open AI has this like

**[37:30]** understood but open AI has this like

**[37:30]** understood but open AI has this like user that is system that you can inject

**[37:32]** user that is system that you can inject

**[37:32]** user that is system that you can inject anywhere at any time which is really

**[37:34]** anywhere at any time which is really

**[37:34]** anywhere at any time which is really fantastic but um anthropic and Google

**[37:38]** fantastic but um anthropic and Google

**[37:38]** fantastic but um anthropic and Google require like a named system instruction

**[37:40]** require like a named system instruction

**[37:40]** require like a named system instruction that's a special one time like at

**[37:41]** that's a special one time like at

**[37:42]** that's a special one time like at constructor time um instruction.

**[37:45]** constructor time um instruction.

**[37:45]** constructor time um instruction. So there's there's some differences. As

**[37:47]** So there's there's some differences. As

**[37:47]** So there's there's some differences. As much as best we can, we we unify.

**[37:53]** All right. Any

**[37:53]** All right. Any how are folks doing on getting quick

**[37:55]** how are folks doing on getting quick

**[37:55]** how are folks doing on getting quick start going? See a hand. Is that a

**[37:57]** start going? See a hand. Is that a

**[37:57]** start going? See a hand. Is that a question or Okay, I'll take maybe it's

**[37:59]** question or Okay, I'll take maybe it's

**[37:59]** question or Okay, I'll take maybe it's related to the quick start.


### [38:00 - 39:00]

**[38:16]** Yeah. So there's a question about noisy

**[38:16]** Yeah. So there's a question about noisy environments which is like voice AI's

**[38:19]** environments which is like voice AI's

**[38:19]** environments which is like voice AI's kryptonite. Um so with the VAD no not at

**[38:22]** kryptonite. Um so with the VAD no not at

**[38:22]** kryptonite. Um so with the VAD no not at the moment. Uh but there are again this

**[38:26]** the moment. Uh but there are again this

**[38:26]** the moment. Uh but there are again this is where like pipecat is the assembler

**[38:27]** is where like pipecat is the assembler

**[38:28]** is where like pipecat is the assembler of all things. What you want to plug in?

**[38:30]** of all things. What you want to plug in?

**[38:30]** of all things. What you want to plug in? Um that you can run separately from the

**[38:33]** Um that you can run separately from the

**[38:33]** Um that you can run separately from the VAD. Uh we found like crisp is one

**[38:37]** VAD. Uh we found like crisp is one

**[38:37]** VAD. Uh we found like crisp is one that's a partner of ours. there have

**[38:38]** that's a partner of ours. there have

**[38:38]** that's a partner of ours. there have they have fantastic noise cancellation.

**[38:40]** they have fantastic noise cancellation.

**[38:40]** they have fantastic noise cancellation. You can run something outside of the

**[38:43]** You can run something outside of the

**[38:43]** You can run something outside of the loop that uh would actually clean up

**[38:44]** loop that uh would actually clean up

**[38:44]** loop that uh would actually clean up like in the in pipe cut it would be in

**[38:46]** like in the in pipe cut it would be in

**[38:46]** like in the in pipe cut it would be in the transport itself. So in that audio

**[38:48]** the transport itself. So in that audio

**[38:48]** the transport itself. So in that audio input it would take uh the audio input

**[38:51]** input it would take uh the audio input

**[38:51]** input it would take uh the audio input and remove any ambient noise. So like

**[38:53]** and remove any ambient noise. So like

**[38:53]** and remove any ambient noise. So like chip bags opening or dogs barking but

**[38:55]** chip bags opening or dogs barking but

**[38:55]** chip bags opening or dogs barking but maybe more impressively uh human

**[38:57]** maybe more impressively uh human

**[38:57]** maybe more impressively uh human background noise. So it will remove that

**[38:59]** background noise. So it will remove that

**[38:59]** background noise. So it will remove that from the feed. So you could be in this


### [39:00 - 40:00]

**[39:01]** from the feed. So you could be in this

**[39:01]** from the feed. So you could be in this conference and it picks up the primary

**[39:03]** conference and it picks up the primary

**[39:03]** conference and it picks up the primary speaker for the device like incredibly

**[39:05]** speaker for the device like incredibly

**[39:05]** speaker for the device like incredibly well. At the moment, they're the only

**[39:07]** well. At the moment, they're the only

**[39:07]** well. At the moment, they're the only ones that I'm aware that know how to do

**[39:08]** ones that I'm aware that know how to do

**[39:08]** ones that I'm aware that know how to do that and do it that well. But it's I

**[39:11]** that and do it that well. But it's I

**[39:11]** that and do it that well. But it's I mean, it's phenomenal. But you're right,

**[39:12]** mean, it's phenomenal. But you're right,

**[39:12]** mean, it's phenomenal. But you're right, the VAD is I mean, it was one of the

**[39:14]** the VAD is I mean, it was one of the

**[39:14]** the VAD is I mean, it was one of the biggest problems that we saw until we

**[39:16]** biggest problems that we saw until we

**[39:16]** biggest problems that we saw until we found Crisp and they're fantastic. CR

**[39:20]** found Crisp and they're fantastic. CR

**[39:20]** found Crisp and they're fantastic. CR IP.

**[39:23]** IP.

**[39:23]** IP. So, big props to the Crisp team.

**[39:31]** Well, we use we use all of them.

**[39:31]** Well, we use we use all of them. Pipecat's open source. So we bring we

**[39:33]** Pipecat's open source. So we bring we

**[39:33]** Pipecat's open source. So we bring we have I think options are Gemini,

**[39:35]** have I think options are Gemini,

**[39:35]** have I think options are Gemini, Multimodal Live, OpenAI, Realtime and

**[39:37]** Multimodal Live, OpenAI, Realtime and

**[39:37]** Multimodal Live, OpenAI, Realtime and then AWS just launched a new one called

**[39:39]** then AWS just launched a new one called

**[39:39]** then AWS just launched a new one called Nova Sonic. So we have those three um

**[39:43]** Nova Sonic. So we have those three um

**[39:43]** Nova Sonic. So we have those three um within Pipcat.

**[39:53]** They're all pretty they're all very much

**[39:53]** They're all pretty they're all very much on actually well they're all they're all

**[39:55]** on actually well they're all they're all

**[39:55]** on actually well they're all they're all very similar. Um, I'm not going to I

**[39:57]** very similar. Um, I'm not going to I

**[39:57]** very similar. Um, I'm not going to I don't want to like nitpick on all of the

**[39:59]** don't want to like nitpick on all of the

**[39:59]** don't want to like nitpick on all of the vendors here, but they're I mean they're


### [40:00 - 41:00]

**[40:01]** vendors here, but they're I mean they're

**[40:01]** vendors here, but they're I mean they're they have strengths and weaknesses each

**[40:02]** they have strengths and weaknesses each

**[40:02]** they have strengths and weaknesses each because it's still an emerging field.

**[40:04]** because it's still an emerging field.

**[40:04]** because it's still an emerging field. Um, but they're latency wise that is not

**[40:08]** Um, but they're latency wise that is not

**[40:08]** Um, but they're latency wise that is not an issue. Latency is fantastic for all

**[40:10]** an issue. Latency is fantastic for all

**[40:10]** an issue. Latency is fantastic for all the providers. Yeah.

**[40:17]** All right.

**[40:17]** All right. Okay. Maybe Allesh will walk through a

**[40:19]** Okay. Maybe Allesh will walk through a

**[40:19]** Okay. Maybe Allesh will walk through a quick start. Why don't we He's going to

**[40:20]** quick start. Why don't we He's going to

**[40:20]** quick start. Why don't we He's going to just do some live coding here and maybe

**[40:22]** just do some live coding here and maybe

**[40:22]** just do some live coding here and maybe this will help to understand what's how

**[40:24]** this will help to understand what's how

**[40:24]** this will help to understand what's how this all works and then Perhaps we I

**[40:26]** this all works and then Perhaps we I

**[40:26]** this all works and then Perhaps we I stopped chatting and maybe you could

**[40:28]** stopped chatting and maybe you could

**[40:28]** stopped chatting and maybe you could grab me if you have questions and just

**[40:29]** grab me if you have questions and just

**[40:30]** grab me if you have questions and just do some heads down working time.

**[40:39]** Yeah, I cannot type and

**[40:39]** Yeah, I cannot type and teamwork. Teamwork. Yeah. Uh I'll try

**[40:42]** teamwork. Teamwork. Yeah. Uh I'll try

**[40:42]** teamwork. Teamwork. Yeah. Uh I'll try from the very very from nothing from

**[40:45]** from the very very from nothing from

**[40:45]** from the very very from nothing from scratch. Um so this is a Python project.

**[40:48]** scratch. Um so this is a Python project.

**[40:48]** scratch. Um so this is a Python project. Um actually let me let me try again.

**[40:51]** Um actually let me let me try again.

**[40:51]** Um actually let me let me try again. Yeah, this is a Python project. The

**[40:53]** Yeah, this is a Python project. The

**[40:53]** Yeah, this is a Python project. The first thing we'll do is create an

**[40:55]** first thing we'll do is create an

**[40:55]** first thing we'll do is create an environment

**[40:57]** environment

**[40:57]** environment like a virtual environment that is

**[40:59]** like a virtual environment that is

**[40:59]** like a virtual environment that is called I like to call it amp that that's


### [41:00 - 42:00]

**[41:02]** called I like to call it amp that that's

**[41:02]** called I like to call it amp that that's how you create a virtual environment in

**[41:04]** how you create a virtual environment in

**[41:04]** how you create a virtual environment in in in Python. Um a virtual environment

**[41:08]** in in Python. Um a virtual environment

**[41:08]** in in Python. Um a virtual environment will have

**[41:14]** what's that?

**[41:14]** what's that? Oh, it's hard to see. Um

**[41:17]** Oh, it's hard to see. Um

**[41:17]** Oh, it's hard to see. Um how do I do that?


### [42:00 - 43:00]

**[42:06]** the only issue is I only have one thing

**[42:06]** the only issue is I only have one thing but

**[42:12]** better. Okay. Yay.

**[42:12]** better. Okay. Yay. Okay. So, we'll start with um uh yes,

**[42:16]** Okay. So, we'll start with um uh yes,

**[42:16]** Okay. So, we'll start with um uh yes, it's Emacs. You can judge me. Uh I'm I'm

**[42:19]** it's Emacs. You can judge me. Uh I'm I'm

**[42:19]** it's Emacs. You can judge me. Uh I'm I'm I'm not going to change. I have a few

**[42:22]** I'm not going to change. I have a few

**[42:22]** I'm not going to change. I have a few years only coding. So that's what it is.

**[42:25]** years only coding. So that's what it is.

**[42:25]** years only coding. So that's what it is. Um so I'm going to create a requirements

**[42:26]** Um so I'm going to create a requirements

**[42:26]** Um so I'm going to create a requirements file. Sorry, I loaded first thing. I did

**[42:29]** file. Sorry, I loaded first thing. I did

**[42:30]** file. Sorry, I loaded first thing. I did the virtual environment. We did this.

**[42:33]** the virtual environment. We did this.

**[42:33]** the virtual environment. We did this. Then we're going to load it. Now we can

**[42:35]** Then we're going to load it. Now we can

**[42:35]** Then we're going to load it. Now we can start installing uh packages in in this

**[42:38]** start installing uh packages in in this

**[42:38]** start installing uh packages in in this environment like Python packages. So the

**[42:41]** environment like Python packages. So the

**[42:41]** environment like Python packages. So the ones we have to do is uh pipe of course.

**[42:46]** ones we have to do is uh pipe of course.

**[42:46]** ones we have to do is uh pipe of course. So I'm just creating a new file which

**[42:48]** So I'm just creating a new file which

**[42:48]** So I'm just creating a new file which has pipecat AI and pipecat has a few

**[42:52]** has pipecat AI and pipecat has a few

**[42:52]** has pipecat AI and pipecat has a few options. So for this example we're going

**[42:54]** options. So for this example we're going

**[42:54]** options. So for this example we're going to use daily we're going to use uh

**[42:57]** to use daily we're going to use uh

**[42:57]** to use daily we're going to use uh Google and we're going to use silero


### [43:00 - 44:00]

**[43:00]** Google and we're going to use silero

**[43:00]** Google and we're going to use silero right silo is the VAD that we we've been

**[43:03]** right silo is the VAD that we we've been

**[43:03]** right silo is the VAD that we we've been talking about. Um the other thing we

**[43:06]** talking about. Um the other thing we

**[43:06]** talking about. Um the other thing we will do is we will load the envir

**[43:09]** will do is we will load the envir

**[43:09]** will do is we will load the envir there's a package called python. temp

**[43:12]** there's a package called python. temp

**[43:12]** there's a package called python. temp just to load the environment variables

**[43:14]** just to load the environment variables

**[43:14]** just to load the environment variables that we will have uh in this in here.

**[43:17]** that we will have uh in this in here.

**[43:17]** that we will have uh in this in here. Okay. Um that's it. One file. Now we're

**[43:20]** Okay. Um that's it. One file. Now we're

**[43:20]** Okay. Um that's it. One file. Now we're going to I'm going to create uh

**[43:24]** going to I'm going to create uh

**[43:24]** going to I'm going to create uh an environment variable. I'm going to

**[43:26]** an environment variable. I'm going to

**[43:26]** an environment variable. I'm going to just copy it from the

**[43:29]** just copy it from the

**[43:29]** just copy it from the from the kickstart. It's just a oops

**[43:32]** from the kickstart. It's just a oops

**[43:32]** from the kickstart. It's just a oops it's just amp

**[43:35]** it's just amp

**[43:35]** it's just amp and we can take a look at it. it. I will

**[43:39]** and we can take a look at it. it. I will

**[43:39]** and we can take a look at it. it. I will these are the the API keys. We'll get

**[43:42]** these are the the API keys. We'll get

**[43:42]** these are the the API keys. We'll get rid of them after this workshop. So, but

**[43:45]** rid of them after this workshop. So, but

**[43:45]** rid of them after this workshop. So, but yeah, these are the you just need two

**[43:47]** yeah, these are the you just need two

**[43:47]** yeah, these are the you just need two keys. Google API key and just uh go to

**[43:51]** keys. Google API key and just uh go to

**[43:51]** keys. Google API key and just uh go to AI studio and create your own one and a

**[43:53]** AI studio and create your own one and a

**[43:53]** AI studio and create your own one and a daily API key. This one we already this

**[43:56]** daily API key. This one we already this

**[43:56]** daily API key. This one we already this one you can copy. It's a bit long but uh

**[43:58]** one you can copy. It's a bit long but uh

**[43:58]** one you can copy. It's a bit long but uh I don't know doesn't Yeah, it's in the


### [44:00 - 45:00]

**[44:02]** I don't know doesn't Yeah, it's in the

**[44:02]** I don't know doesn't Yeah, it's in the project. Yeah. Yeah. If you if you are

**[44:04]** project. Yeah. Yeah. If you if you are

**[44:04]** project. Yeah. Yeah. If you if you are able to go to the to the repo on GitHub,

**[44:06]** able to go to the to the repo on GitHub,

**[44:06]** able to go to the to the repo on GitHub, you you can just copy it from there. All

**[44:09]** you you can just copy it from there. All

**[44:09]** you you can just copy it from there. All right. Next, we're going to create a

**[44:11]** right. Next, we're going to create a

**[44:11]** right. Next, we're going to create a Python file. Let's call it uh bot.py.

**[44:16]** Python file. Let's call it uh bot.py.

**[44:16]** Python file. Let's call it uh bot.py. Again, empty file. Uh first thing we'll

**[44:20]** Again, empty file. Uh first thing we'll

**[44:20]** Again, empty file. Uh first thing we'll do is typical I think it's called name

**[44:25]** do is typical I think it's called name

**[44:25]** do is typical I think it's called name uh equals main. No help from an LLM. And

**[44:30]** uh equals main. No help from an LLM. And

**[44:30]** uh equals main. No help from an LLM. And then we do a sync.io.run. run uh a

**[44:34]** then we do a sync.io.run. run uh a

**[44:34]** then we do a sync.io.run. run uh a little bit of help singo.r run and we're

**[44:38]** little bit of help singo.r run and we're

**[44:38]** little bit of help singo.r run and we're going to run a main a main function

**[44:41]** going to run a main a main function

**[44:41]** going to run a main a main function function

**[44:43]** function

**[44:43]** function and then let's write the main function.

**[44:52]** All right. So now we start. So the first

**[44:52]** All right. So now we start. So the first thing we uh we we we said is we're going

**[44:54]** thing we uh we we we said is we're going

**[44:54]** thing we uh we we we said is we're going to need a transport. The transport input

**[44:56]** to need a transport. The transport input

**[44:56]** to need a transport. The transport input is like we're going to um like the day a


### [45:00 - 46:00]

**[45:00]** is like we're going to um like the day a

**[45:00]** is like we're going to um like the day a daily transport. We're going to say

**[45:01]** daily transport. We're going to say

**[45:01]** daily transport. We're going to say that's I'm going to speak to the to the

**[45:03]** that's I'm going to speak to the to the

**[45:03]** that's I'm going to speak to the to the bot through the daily transport. That's

**[45:05]** bot through the daily transport. That's

**[45:05]** bot through the daily transport. That's what I'm going to create. And then we

**[45:06]** what I'm going to create. And then we

**[45:06]** what I'm going to create. And then we want it's a transport for incoming audio

**[45:09]** want it's a transport for incoming audio

**[45:09]** want it's a transport for incoming audio from me talking and then a transport uh

**[45:12]** from me talking and then a transport uh

**[45:12]** from me talking and then a transport uh for outputting what the what the LLM

**[45:14]** for outputting what the what the LLM

**[45:14]** for outputting what the what the LLM will say. So I'm just going to create a

**[45:17]** will say. So I'm just going to create a

**[45:17]** will say. So I'm just going to create a transport. Um and this is a daily

**[45:20]** transport. Um and this is a daily

**[45:20]** transport. Um and this is a daily transport

**[45:22]** transport

**[45:22]** transport and it has a few uh arguments. It has a

**[45:26]** and it has a few uh arguments. It has a

**[45:26]** and it has a few uh arguments. It has a room URL. I'm just going to create mine

**[45:29]** room URL. I'm just going to create mine

**[45:29]** room URL. I'm just going to create mine for now.

**[45:31]** for now.

**[45:31]** for now. Um this is a again a public public room

**[45:35]** Um this is a again a public public room

**[45:35]** Um this is a again a public public room that I will have to delete. Uh I don't

**[45:38]** that I will have to delete. Uh I don't

**[45:38]** that I will have to delete. Uh I don't need a token and params.

**[45:43]** need a token and params.

**[45:43]** need a token and params. Okay. And then the daily params is like

**[45:46]** Okay. And then the daily params is like

**[45:46]** Okay. And then the daily params is like what do we want this out uh this

**[45:48]** what do we want this out uh this

**[45:48]** what do we want this out uh this transport to do? So, we're going to say

**[45:50]** transport to do? So, we're going to say

**[45:50]** transport to do? So, we're going to say that we want uh input enable, which

**[45:53]** that we want uh input enable, which

**[45:54]** that we want uh input enable, which means get audio from the transport, and

**[45:56]** means get audio from the transport, and

**[45:56]** means get audio from the transport, and we also want to


### [46:00 - 47:00]

**[46:00]** we also want to

**[46:00]** we also want to to send audio to the transport.

**[46:03]** to send audio to the transport.

**[46:03]** to send audio to the transport. Okay. Um

**[46:06]** Okay. Um

**[46:06]** Okay. Um All right. What else? Uh it's

**[46:08]** All right. What else? Uh it's

**[46:08]** All right. What else? Uh it's complaining for something. Oh, yeah. And

**[46:12]** complaining for something. Oh, yeah. And

**[46:12]** complaining for something. Oh, yeah. And we also need uh VAT analyzer, which is

**[46:16]** we also need uh VAT analyzer, which is

**[46:16]** we also need uh VAT analyzer, which is going to be Silerero VA analyzer.

**[46:19]** going to be Silerero VA analyzer.

**[46:19]** going to be Silerero VA analyzer. Um, so the transport is going to be able

**[46:22]** Um, so the transport is going to be able

**[46:22]** Um, so the transport is going to be able to uh use this VA analyzer to detect if

**[46:26]** to uh use this VA analyzer to detect if

**[46:26]** to uh use this VA analyzer to detect if the user has spoken or not. What's that?

**[46:30]** the user has spoken or not. What's that?

**[46:30]** the user has spoken or not. What's that? Oh yeah. And this is going to be AI

**[46:34]** Oh yeah. And this is going to be AI

**[46:34]** Oh yeah. And this is going to be AI engineer.

**[46:35]** engineer.

**[46:36]** engineer. There we go. Okay. Now we have the

**[46:38]** There we go. Okay. Now we have the

**[46:38]** There we go. Okay. Now we have the transport. Now we're going to create the

**[46:40]** transport. Now we're going to create the

**[46:40]** transport. Now we're going to create the LLM. Uh, in this case it's Google um,

**[46:45]** LLM. Uh, in this case it's Google um,

**[46:46]** LLM. Uh, in this case it's Google um, uh, Gemini live. So I don't need to

**[46:47]** uh, Gemini live. So I don't need to

**[46:47]** uh, Gemini live. So I don't need to create an speech to text or text to

**[46:49]** create an speech to text or text to

**[46:49]** create an speech to text or text to speech. We just create uh the Gemini

**[46:52]** speech. We just create uh the Gemini

**[46:52]** speech. We just create uh the Gemini live and for that I'll need to copy it

**[46:54]** live and for that I'll need to copy it

**[46:54]** live and for that I'll need to copy it for because I don't know that from

**[46:56]** for because I don't know that from

**[46:56]** for because I don't know that from memory but um


### [47:00 - 48:00]

**[47:00]** memory but um

**[47:00]** memory but um oops

**[47:07]** that's in this file gem Ibot. I just

**[47:07]** that's in this file gem Ibot. I just want to copy these lines here. There we

**[47:09]** want to copy these lines here. There we

**[47:09]** want to copy these lines here. There we go.

**[47:11]** go.

**[47:11]** go. All right.

**[47:13]** All right.

**[47:13]** All right. So this is my LLM and again it uses this

**[47:18]** So this is my LLM and again it uses this

**[47:18]** So this is my LLM and again it uses this Gemini multimodel live LLM service

**[47:25]** multimodel live LLM service. I'm just

**[47:26]** multimodel live LLM service. I'm just going to add my import. Okay. And now it

**[47:29]** going to add my import. Okay. And now it

**[47:29]** going to add my import. Okay. And now it needs a couple of things. The system

**[47:30]** needs a couple of things. The system

**[47:30]** needs a couple of things. The system instruction which is like what the what

**[47:33]** instruction which is like what the what

**[47:33]** instruction which is like what the what the agent is going to is going to do and

**[47:35]** the agent is going to is going to do and

**[47:35]** the agent is going to is going to do and some tools. The tools I'm going to skip

**[47:37]** some tools. The tools I'm going to skip

**[47:37]** some tools. The tools I'm going to skip them for now. So let's let's do the

**[47:41]** them for now. So let's let's do the

**[47:41]** them for now. So let's let's do the system instruction again. I'm going to

**[47:42]** system instruction again. I'm going to

**[47:42]** system instruction again. I'm going to copy it from somewhere. There it is.

**[47:46]** copy it from somewhere. There it is.

**[47:46]** copy it from somewhere. There it is. This is like the prom, like the main

**[47:48]** This is like the prom, like the main

**[47:48]** This is like the prom, like the main prom of the Well, not. Yeah.

**[47:52]** prom of the Well, not. Yeah.

**[47:52]** prom of the Well, not. Yeah. All right. So, the system instruction is

**[47:54]** All right. So, the system instruction is

**[47:54]** All right. So, the system instruction is you're a helpful assistant who can

**[47:56]** you're a helpful assistant who can

**[47:56]** you're a helpful assistant who can answer questions and use tools. For now,

**[47:58]** answer questions and use tools. For now,

**[47:58]** answer questions and use tools. For now, we're not going to use any tools. Um,


### [48:00 - 49:00]

**[48:01]** we're not going to use any tools. Um,

**[48:02]** we're not going to use any tools. Um, you know what? Let me get rid of the

**[48:04]** you know what? Let me get rid of the

**[48:04]** you know what? Let me get rid of the tools. Just copy here for later. I'm

**[48:08]** tools. Just copy here for later. I'm

**[48:08]** tools. Just copy here for later. I'm gonna comand this out.

**[48:11]** gonna comand this out.

**[48:11]** gonna comand this out. and you are just the helpful assistant.

**[48:13]** and you are just the helpful assistant.

**[48:13]** and you are just the helpful assistant. Okay, so that's

**[48:22]** all right. Um, so no complaints here.

**[48:22]** all right. Um, so no complaints here. All right. And now we just create the

**[48:25]** All right. And now we just create the

**[48:25]** All right. And now we just create the a pipeline.

**[48:31]** I'm going to avoid storing the context

**[48:31]** I'm going to avoid storing the context because I don't think we need it for

**[48:32]** because I don't think we need it for

**[48:32]** because I don't think we need it for now.

**[48:34]** now.

**[48:34]** now. And this is the pipeline. The pipeline

**[48:36]** And this is the pipeline. The pipeline

**[48:36]** And this is the pipeline. The pipeline just receives a list of um of processors

**[48:40]** just receives a list of um of processors

**[48:40]** just receives a list of um of processors or elements and the first one is a

**[48:43]** or elements and the first one is a

**[48:43]** or elements and the first one is a transportinput

**[48:45]** transportinput

**[48:45]** transportinput that's the input transport. So how we

**[48:47]** that's the input transport. So how we

**[48:47]** that's the input transport. So how we get audio from the uh from the daily

**[48:50]** get audio from the uh from the daily

**[48:50]** get audio from the uh from the daily room in this case the llm and the

**[48:54]** room in this case the llm and the

**[48:54]** room in this case the llm and the transport.output.


### [49:00 - 50:00]

**[49:01]** All right. Now we need some this is just

**[49:01]** All right. Now we need some this is just defines a p a pipeline also is another

**[49:04]** defines a p a pipeline also is another

**[49:04]** defines a p a pipeline also is another processor. So you could build a pipeline

**[49:07]** processor. So you could build a pipeline

**[49:07]** processor. So you could build a pipeline of pipelines of pipelines of pipelines.

**[49:09]** of pipelines of pipelines of pipelines.

**[49:09]** of pipelines of pipelines of pipelines. So you can build uh or you can plug and

**[49:11]** So you can build uh or you can plug and

**[49:11]** So you can build uh or you can plug and play uh as as the way you liked it. So

**[49:15]** play uh as as the way you liked it. So

**[49:15]** play uh as as the way you liked it. So how do you run a pipeline? You need a

**[49:16]** how do you run a pipeline? You need a

**[49:16]** how do you run a pipeline? You need a task. What we call a pipeline task

**[49:21]** task. What we call a pipeline task

**[49:21]** task. What we call a pipeline task that receives a pipeline. And the

**[49:23]** that receives a pipeline. And the

**[49:23]** that receives a pipeline. And the pipeline task also has some params

**[49:26]** pipeline task also has some params

**[49:26]** pipeline task also has some params which are called pipeline params.

**[49:30]** which are called pipeline params.

**[49:30]** which are called pipeline params. Um,

**[49:32]** Um,

**[49:32]** Um, and we're going to say, oops,

**[49:36]** and we're going to say, oops,

**[49:36]** and we're going to say, oops, that we allow interruptions.

**[49:44]** And I think that's enough.

**[49:44]** And I think that's enough. And how do you run a task? Uh, you can

**[49:47]** And how do you run a task? Uh, you can

**[49:47]** And how do you run a task? Uh, you can create more than one pipeline task if

**[49:49]** create more than one pipeline task if

**[49:49]** create more than one pipeline task if you wanted. In this case, we just have

**[49:50]** you wanted. In this case, we just have

**[49:50]** you wanted. In this case, we just have one. Usually, you just you just have

**[49:52]** one. Usually, you just you just have

**[49:52]** one. Usually, you just you just have one. Uh, you're going to create a

**[49:54]** one. Uh, you're going to create a

**[49:54]** one. Uh, you're going to create a runner. And guess what? It's called

**[49:57]** runner. And guess what? It's called

**[49:57]** runner. And guess what? It's called pipeline runner. Uh it's pipeline runner


### [50:00 - 51:00]

**[50:01]** pipeline runner. Uh it's pipeline runner

**[50:01]** pipeline runner. Uh it's pipeline runner and then we just do await

**[50:05]** and then we just do await

**[50:05]** and then we just do await runner run

**[50:08]** runner run

**[50:08]** runner run task

**[50:10]** task

**[50:10]** task and some completions please pipeline

**[50:15]** and some completions please pipeline

**[50:15]** and some completions please pipeline runner. All right and I think that's it.

**[50:19]** runner. All right and I think that's it.

**[50:19]** runner. All right and I think that's it. Uh we'll try it. Oh OS import OS. I

**[50:23]** Uh we'll try it. Oh OS import OS. I

**[50:23]** Uh we'll try it. Oh OS import OS. I think

**[50:26]** think

**[50:26]** think I think there's no more warnings.

**[50:30]** I think there's no more warnings.

**[50:30]** I think there's no more warnings. Oh, and I need to load the environment

**[50:32]** Oh, and I need to load the environment

**[50:32]** Oh, and I need to load the environment variables, which is this line here,

**[50:35]** variables, which is this line here,

**[50:35]** variables, which is this line here, load.m

**[50:37]** load.m

**[50:37]** load.m just copy it from another file.

**[50:40]** just copy it from another file.

**[50:40]** just copy it from another file. Okay.

**[50:46]** And where do we get loadm? This is just

**[50:46]** And where do we get loadm? This is just a function that um

**[50:50]** a function that um

**[50:50]** a function that um um that imports

**[50:52]** um that imports

**[50:52]** um that imports the imports the environment variable.

**[50:55]** the imports the environment variable.

**[50:55]** the imports the environment variable. All right. And yeah, let's let's try

**[50:59]** All right. And yeah, let's let's try


### [51:00 - 52:00]

**[51:00]** All right. And yeah, let's let's try just going to open the Oops.

**[51:08]** Just going to open the terminal here

**[51:08]** Just going to open the terminal here and I'm just going to run it. I think we

**[51:11]** and I'm just going to run it. I think we

**[51:11]** and I'm just going to run it. I think we call it bot.py.

**[51:18]** Uh, no model. Oh, maybe I need to

**[51:18]** Uh, no model. Oh, maybe I need to install the requirements. I forgot this

**[51:20]** install the requirements. I forgot this

**[51:20]** install the requirements. I forgot this step.

**[51:30]** There it is. Okay. So, init at the

**[51:30]** There it is. Okay. So, init at the beginning I uh wrote that file

**[51:32]** beginning I uh wrote that file

**[51:32]** beginning I uh wrote that file requirements uh text which has uh had a

**[51:35]** requirements uh text which has uh had a

**[51:35]** requirements uh text which has uh had a bunch of uh well just a few requirements

**[51:39]** bunch of uh well just a few requirements

**[51:39]** bunch of uh well just a few requirements but I forgot to to install them.

**[51:52]** In the meantime, I'm just going to go to

**[51:52]** In the meantime, I'm just going to go to the daily room that I just pointed the

**[51:55]** the daily room that I just pointed the

**[51:55]** the daily room that I just pointed the bot to


### [52:00 - 53:00]

**[52:09]** uh

**[52:09]** uh video.

**[52:10]** video.

**[52:10]** video. Okay.

**[52:12]** Okay.

**[52:12]** Okay. So that's uh right now it's just me in

**[52:16]** So that's uh right now it's just me in

**[52:16]** So that's uh right now it's just me in that in that room. So and now we just

**[52:19]** that in that room. So and now we just

**[52:19]** that in that room. So and now we just have to wait for this to to finish and

**[52:21]** have to wait for this to to finish and

**[52:22]** have to wait for this to to finish and hopefully the bot will join the room and

**[52:24]** hopefully the bot will join the room and

**[52:24]** hopefully the bot will join the room and we'll be able to talk to it. Hopefully.

**[52:44]** It is in Yeah, it's this is because uh

**[52:44]** It is in Yeah, it's this is because uh we're using the daily transport and the

**[52:46]** we're using the daily transport and the

**[52:46]** we're using the daily transport and the daily transport just connects to a daily

**[52:48]** daily transport just connects to a daily

**[52:48]** daily transport just connects to a daily room. So, but you could have a a

**[52:51]** room. So, but you could have a a

**[52:51]** room. So, but you could have a a websocket transport and then use Twilio

**[52:53]** websocket transport and then use Twilio

**[52:54]** websocket transport and then use Twilio with a phone number and Twilio being

**[52:56]** with a phone number and Twilio being

**[52:56]** with a phone number and Twilio being connected to that. If we have time, we

**[52:58]** connected to that. If we have time, we

**[52:58]** connected to that. If we have time, we can even try that. Um, so I think small


### [53:00 - 54:00]

**[53:02]** can even try that. Um, so I think small

**[53:02]** can even try that. Um, so I think small transport

**[53:09]** you want to you want to talk? Oh, yeah.

**[53:09]** you want to you want to talk? Oh, yeah. I'll wait.

**[53:11]** I'll wait.

**[53:11]** I'll wait. So we als uh in Pipcat we also have

**[53:13]** So we als uh in Pipcat we also have

**[53:13]** So we als uh in Pipcat we also have added um based off of the AIO RTC Python

**[53:17]** added um based off of the AIO RTC Python

**[53:17]** added um based off of the AIO RTC Python package which is how uh WebRTC package

**[53:20]** package which is how uh WebRTC package

**[53:20]** package which is how uh WebRTC package in Python. We've added a new transport

**[53:23]** in Python. We've added a new transport

**[53:23]** in Python. We've added a new transport called small WebRTC transport. It is a

**[53:26]** called small WebRTC transport. It is a

**[53:26]** called small WebRTC transport. It is a peer-to-peer WebRTC communication that's

**[53:28]** peer-to-peer WebRTC communication that's

**[53:28]** peer-to-peer WebRTC communication that's free. So it's separate from any vendor.

**[53:30]** free. So it's separate from any vendor.

**[53:30]** free. So it's separate from any vendor. Uh though the one downside is that it

**[53:32]** Uh though the one downside is that it

**[53:32]** Uh though the one downside is that it requires turn server which we you bring

**[53:35]** requires turn server which we you bring

**[53:35]** requires turn server which we you bring your own. So we we didn't you know we

**[53:37]** your own. So we we didn't you know we

**[53:37]** your own. So we we didn't you know we weren't prepared for that for the

**[53:38]** weren't prepared for that for the

**[53:38]** weren't prepared for that for the conference and also just the conference

**[53:39]** conference and also just the conference

**[53:39]** conference and also just the conference Wi-Fi makes that a little challenging.

**[53:41]** Wi-Fi makes that a little challenging.

**[53:41]** Wi-Fi makes that a little challenging. But normally if you're running any of

**[53:43]** But normally if you're running any of

**[53:43]** But normally if you're running any of the any of the u we call them

**[53:45]** the any of the u we call them

**[53:45]** the any of the u we call them foundational examples in Pipcat. Think

**[53:47]** foundational examples in Pipcat. Think

**[53:47]** foundational examples in Pipcat. Think of them as the like essential um

**[53:50]** of them as the like essential um

**[53:50]** of them as the like essential um examples that show how to do very

**[53:52]** examples that show how to do very

**[53:52]** examples that show how to do very specific functions. There's probably

**[53:53]** specific functions. There's probably

**[53:53]** specific functions. There's probably about a hundred of them in Pipcat, but

**[53:55]** about a hundred of them in Pipcat, but

**[53:55]** about a hundred of them in Pipcat, but one by one it shows you how to like

**[53:56]** one by one it shows you how to like

**[53:56]** one by one it shows you how to like record or add an ST or push frames or

**[53:59]** record or add an ST or push frames or

**[53:59]** record or add an ST or push frames or show images or sync images and and


### [54:00 - 55:00]

**[54:02]** show images or sync images and and

**[54:02]** show images or sync images and and sound. Those all use the peer-to-peer

**[54:04]** sound. Those all use the peer-to-peer

**[54:04]** sound. Those all use the peer-to-peer WebRTC transport. So we we would have

**[54:07]** WebRTC transport. So we we would have

**[54:07]** WebRTC transport. So we we would have loved to have used that. You wouldn't

**[54:08]** loved to have used that. You wouldn't

**[54:08]** loved to have used that. You wouldn't need a key, but unfortunately firewall

**[54:10]** need a key, but unfortunately firewall

**[54:10]** need a key, but unfortunately firewall rules have trumped.

**[54:13]** rules have trumped.

**[54:13]** rules have trumped. All right. Uh so I'm just running the

**[54:16]** All right. Uh so I'm just running the

**[54:16]** All right. Uh so I'm just running the bot and see how it fails because it has

**[54:19]** bot and see how it fails because it has

**[54:20]** bot and see how it fails because it has to fail the first time.

**[54:29]** Yeah, this is the math there because

**[54:29]** Yeah, this is the math there because there's a bunch of the um Python

**[54:31]** there's a bunch of the um Python

**[54:31]** there's a bunch of the um Python packages and Python just decides to take

**[54:35]** packages and Python just decides to take

**[54:35]** packages and Python just decides to take uh a time to load them. But you see how

**[54:38]** uh a time to load them. But you see how

**[54:38]** uh a time to load them. But you see how easy it was to write

**[54:41]** easy it was to write

**[54:41]** easy it was to write um

**[54:43]** um

**[54:43]** um like an agent like a voice agent with

**[54:46]** like an agent like a voice agent with

**[54:46]** like an agent like a voice agent with Gemini live uh if it worked. It's just a

**[54:49]** Gemini live uh if it worked. It's just a

**[54:49]** Gemini live uh if it worked. It's just a few lines of code. Uh that we wrote in I

**[54:53]** few lines of code. Uh that we wrote in I

**[54:53]** few lines of code. Uh that we wrote in I don't know how long it took me but uh

**[54:55]** don't know how long it took me but uh

**[54:55]** don't know how long it took me but uh maybe like five 10 minutes. Um yeah. Are


### [55:00 - 56:00]

**[55:00]** maybe like five 10 minutes. Um yeah. Are

**[55:00]** maybe like five 10 minutes. Um yeah. Are there any questions on the example or

**[55:04]** there any questions on the example or

**[55:04]** there any questions on the example or what's that? It worked.

**[55:07]** what's that? It worked.

**[55:07]** what's that? It worked. would work. The bot work. Okay. All

**[55:11]** would work. The bot work. Okay. All

**[55:11]** would work. The bot work. Okay. All righty.

**[55:35]** uh we have I don't know the actual

**[55:35]** uh we have I don't know the actual number of customers but I mean Pipecat

**[55:37]** number of customers but I mean Pipecat

**[55:37]** number of customers but I mean Pipecat probably serves hundreds of thousands of

**[55:39]** probably serves hundreds of thousands of

**[55:40]** probably serves hundreds of thousands of calls a day. I don't know a lot coin you

**[55:42]** calls a day. I don't know a lot coin you

**[55:42]** calls a day. I don't know a lot coin you probably have a better idea. Oh yeah,

**[55:44]** probably have a better idea. Oh yeah,

**[55:44]** probably have a better idea. Oh yeah, Pad is used by some very large companies

**[55:46]** Pad is used by some very large companies

**[55:46]** Pad is used by some very large companies in production. Uh and people are

**[55:48]** in production. Uh and people are

**[55:48]** in production. Uh and people are contributing to it from Nvidia, AWS, uh

**[55:52]** contributing to it from Nvidia, AWS, uh

**[55:52]** contributing to it from Nvidia, AWS, uh OpenAI, Google, uh lots of lots of big

**[55:55]** OpenAI, Google, uh lots of lots of big

**[55:55]** OpenAI, Google, uh lots of lots of big companies.

**[55:57]** companies.

**[55:57]** companies. Yeah, there's one thing we didn't

**[55:58]** Yeah, there's one thing we didn't

**[55:58]** Yeah, there's one thing we didn't mention about Pipcat is that what you


### [56:00 - 57:00]

**[56:00]** mention about Pipcat is that what you

**[56:00]** mention about Pipcat is that what you see now in the screen, this runs on the

**[56:03]** see now in the screen, this runs on the

**[56:03]** see now in the screen, this runs on the server side, but we do have client SDKs

**[56:06]** server side, but we do have client SDKs

**[56:06]** server side, but we do have client SDKs for Android, iOS, JavaScript, and React.

**[56:11]** for Android, iOS, JavaScript, and React.

**[56:12]** for Android, iOS, JavaScript, and React. And I think that's about it. But uh

**[56:15]** And I think that's about it. But uh

**[56:15]** And I think that's about it. But uh Ragnated even a C++ client um uh if you

**[56:19]** Ragnated even a C++ client um uh if you

**[56:19]** Ragnated even a C++ client um uh if you want. Um so yeah, so that's the server

**[56:23]** want. Um so yeah, so that's the server

**[56:23]** want. Um so yeah, so that's the server side, but you can plug your your client

**[56:26]** side, but you can plug your your client

**[56:26]** side, but you can plug your your client and connect to the to the agent on your

**[56:29]** and connect to the to the agent on your

**[56:29]** and connect to the to the agent on your on your phone. We RTC connections or

**[56:32]** on your phone. We RTC connections or

**[56:32]** on your phone. We RTC connections or that would be it that depends on the

**[56:35]** that would be it that depends on the

**[56:35]** that would be it that depends on the transport you use. But yeah, you could

**[56:37]** transport you use. But yeah, you could

**[56:37]** transport you use. But yeah, you could you could have your client connect to a

**[56:39]** you could have your client connect to a

**[56:40]** you could have your client connect to a daily or we support LifeKit as well, but

**[56:43]** daily or we support LifeKit as well, but

**[56:43]** daily or we support LifeKit as well, but to a daily room. We like daily because

**[56:45]** to a daily room. We like daily because

**[56:45]** to a daily room. We like daily because we are working daily, but you connect

**[56:47]** we are working daily, but you connect

**[56:47]** we are working daily, but you connect you can connect to a daily room and then

**[56:49]** you can connect to a daily room and then

**[56:49]** you can connect to a daily room and then the bot would connect or the agent would

**[56:52]** the bot would connect or the agent would

**[56:52]** the bot would connect or the agent would connect to the daily room as well. And

**[56:54]** connect to the daily room as well. And

**[56:54]** connect to the daily room as well. And then that's the transport, the WebRTC

**[56:56]** then that's the transport, the WebRTC

**[56:56]** then that's the transport, the WebRTC transport. Yeah,


### [57:00 - 58:00]

**[57:02]** I think there were questions there. I

**[57:02]** I think there were questions there. I can see

**[57:29]** for the previous version. Um, I just

**[57:29]** for the previous version. Um, I just hacked together a thing that that I call

**[57:31]** hacked together a thing that that I call

**[57:31]** hacked together a thing that that I call release eval which is a bot talking to a

**[57:33]** release eval which is a bot talking to a

**[57:34]** release eval which is a bot talking to a bot and what it does is I put this bot

**[57:37]** bot and what it does is I put this bot

**[57:37]** bot and what it does is I put this bot uh up and then it joins a daily room and

**[57:40]** uh up and then it joins a daily room and

**[57:40]** uh up and then it joins a daily room and then I have a an eval bot and the eval

**[57:43]** then I have a an eval bot and the eval

**[57:43]** then I have a an eval bot and the eval bot um what he's going to do it has a

**[57:46]** bot um what he's going to do it has a

**[57:46]** bot um what he's going to do it has a prompt which is ask a simple addition.

**[57:50]** prompt which is ask a simple addition.

**[57:50]** prompt which is ask a simple addition. Okay. And then that evalbot is going to

**[57:52]** Okay. And then that evalbot is going to

**[57:52]** Okay. And then that evalbot is going to connect to the room. is going to add

**[57:54]** connect to the room. is going to add

**[57:54]** connect to the room. is going to add what is 2 plus two and then the other

**[57:57]** what is 2 plus two and then the other

**[57:57]** what is 2 plus two and then the other bot is going to reply 2 plus 2 is four

**[57:59]** bot is going to reply 2 plus 2 is four

**[57:59]** bot is going to reply 2 plus 2 is four and the ebal bot the LLM uh it checks if


### [58:00 - 59:00]

**[58:05]** and the ebal bot the LLM uh it checks if

**[58:05]** and the ebal bot the LLM uh it checks if the answer of the user is correct and

**[58:07]** the answer of the user is correct and

**[58:07]** the answer of the user is correct and the user in this case is another LLM so

**[58:10]** the user in this case is another LLM so

**[58:10]** the user in this case is another LLM so it verifies it's like an end to end the

**[58:12]** it verifies it's like an end to end the

**[58:12]** it verifies it's like an end to end the good thing is we we run the we used to

**[58:14]** good thing is we we run the we used to

**[58:14]** good thing is we we run the we used to run like more than 100 examples every

**[58:18]** run like more than 100 examples every

**[58:18]** run like more than 100 examples every release just to make sure they work so I

**[58:20]** release just to make sure they work so I

**[58:20]** release just to make sure they work so I just got tired of it because it's very

**[58:22]** just got tired of it because it's very

**[58:22]** just got tired of it because it's very painful and very slow. So we have these

**[58:25]** painful and very slow. So we have these

**[58:25]** painful and very slow. So we have these uh eval or eval release evals that are

**[58:29]** uh eval or eval release evals that are

**[58:29]** uh eval or eval release evals that are going to test each service like we test

**[58:32]** going to test each service like we test

**[58:32]** going to test each service like we test Gemini live we test cartisia deep gram

**[58:36]** Gemini live we test cartisia deep gram

**[58:36]** Gemini live we test cartisia deep gram like all the services like end to end

**[58:37]** like all the services like end to end

**[58:37]** like all the services like end to end and then the bots basically talk to each

**[58:40]** and then the bots basically talk to each

**[58:40]** and then the bots basically talk to each other with boys that's the that's the

**[58:43]** other with boys that's the that's the

**[58:43]** other with boys that's the that's the the nice thing so yeah okay oh is this

**[58:47]** the nice thing so yeah okay oh is this

**[58:47]** the nice thing so yeah okay oh is this on maybe real quick just to show for

**[58:48]** on maybe real quick just to show for

**[58:48]** on maybe real quick just to show for those that didn't see it it is hey can

**[58:50]** those that didn't see it it is hey can

**[58:50]** those that didn't see it it is hey can you tell me a

**[58:56]** Why don't scientists trust atoms?

**[58:56]** Why don't scientists trust atoms? Because they make up everything,

**[58:59]** Because they make up everything,

**[58:59]** Because they make up everything, which


### [59:00 - 01:00:00]

**[59:01]** which

**[59:01]** which if you build pipe cat, I've heard that

**[59:03]** if you build pipe cat, I've heard that

**[59:03]** if you build pipe cat, I've heard that joke probably I mean, not like 5,000

**[59:06]** joke probably I mean, not like 5,000

**[59:06]** joke probably I mean, not like 5,000 times. Like you can even try to seed it

**[59:08]** times. Like you can even try to seed it

**[59:08]** times. Like you can even try to seed it with something different, but it's still

**[59:09]** with something different, but it's still

**[59:09]** with something different, but it's still I will try to come up with a new joke.

**[59:11]** I will try to come up with a new joke.

**[59:11]** I will try to come up with a new joke. Yeah. Why do Why do you always say the

**[59:13]** Yeah. Why do Why do you always say the

**[59:13]** Yeah. Why do Why do you always say the same joke?

**[59:19]** That's an interesting question. Why do

**[59:19]** That's an interesting question. Why do you think people keep telling the same

**[59:20]** you think people keep telling the same

**[59:20]** you think people keep telling the same jokes?

**[59:22]** jokes?

**[59:22]** jokes? I don't know. You tell me.

**[59:29]** From my search, there appear to be

**[59:29]** From my search, there appear to be several reasons why people repeat jokes.

**[59:32]** several reasons why people repeat jokes.

**[59:32]** several reasons why people repeat jokes. Enjoyment and reinforcement. People

**[59:34]** Enjoyment and reinforcement. People

**[59:34]** Enjoyment and reinforcement. People repeat things they find funny because

**[59:35]** repeat things they find funny because

**[59:35]** repeat things they find funny because they want to reexperience the good

**[59:37]** they want to reexperience the good

**[59:37]** they want to reexperience the good feeling associated with laughter. It

**[59:39]** feeling associated with laughter. It

**[59:39]** feeling associated with laughter. It feels good. And repeating it is a way to

**[59:42]** feels good. And repeating it is a way to

**[59:42]** feels good. And repeating it is a way to try and recreate that sensation. Memory

**[59:44]** try and recreate that sensation. Memory

**[59:44]** try and recreate that sensation. Memory aid. Okay. Okay, that's enough.

**[59:50]** Is there anything else I can help you

**[59:50]** Is there anything else I can help you with today? No, thank you. That that was

**[59:52]** with today? No, thank you. That that was

**[59:52]** with today? No, thank you. That that was it. Thank you so much. Well, just to

**[59:54]** it. Thank you so much. Well, just to

**[59:54]** it. Thank you so much. Well, just to show there was a question about

**[59:55]** show there was a question about

**[59:55]** show there was a question about interruptions. We could just have it

**[59:57]** interruptions. We could just have it

**[59:57]** interruptions. We could just have it like my favorite is to ask it to tell

**[59:59]** like my favorite is to ask it to tell

**[59:59]** like my favorite is to ask it to tell you like a really long story and then


### [01:00:00 - 01:01:00]

**[01:00:00]** you like a really long story and then

**[01:00:00]** you like a really long story and then interrupt it. So, can you tell me a

**[01:00:01]** interrupt it. So, can you tell me a

**[01:00:01]** interrupt it. So, can you tell me a really long really long story?

**[01:00:09]** Okay, I can do that. Here's a story and

**[01:00:09]** Okay, I can do that. Here's a story and feel free to interrupt whenever you

**[01:00:10]** feel free to interrupt whenever you

**[01:00:10]** feel free to interrupt whenever you like. Once upon a time. Okay. Actually,

**[01:00:12]** like. Once upon a time. Okay. Actually,

**[01:00:12]** like. Once upon a time. Okay. Actually, tell me that new joke. Quit following

**[01:00:14]** tell me that new joke. Quit following

**[01:00:14]** tell me that new joke. Quit following the clues. Hey, tell me that new joke.

**[01:00:17]** the clues. Hey, tell me that new joke.

**[01:00:17]** the clues. Hey, tell me that new joke. You'd like to scientists trust Adams?

**[01:00:20]** You'd like to scientists trust Adams?

**[01:00:20]** You'd like to scientists trust Adams? Because they make up everything. Okay,

**[01:00:23]** Because they make up everything. Okay,

**[01:00:23]** Because they make up everything. Okay, here's one.

**[01:00:25]** here's one.

**[01:00:25]** here's one. That was the same joke.

**[01:00:54]** So I think the questions asked during

**[01:00:54]** So I think the questions asked during this workshop could map out like years

**[01:00:57]** this workshop could map out like years

**[01:00:57]** this workshop could map out like years of work. So this is like another one of


### [01:01:00 - 01:02:00]

**[01:01:00]** of work. So this is like another one of

**[01:01:00]** of work. So this is like another one of those fantastic cutting edge things. So

**[01:01:03]** those fantastic cutting edge things. So

**[01:01:03]** those fantastic cutting edge things. So again back to like human evolution. We

**[01:01:05]** again back to like human evolution. We

**[01:01:05]** again back to like human evolution. We all know and when we talk actually it's

**[01:01:07]** all know and when we talk actually it's

**[01:01:07]** all know and when we talk actually it's even hard for humans to talk to not

**[01:01:08]** even hard for humans to talk to not

**[01:01:08]** even hard for humans to talk to not speak over each other. So the way that

**[01:01:10]** speak over each other. So the way that

**[01:01:10]** speak over each other. So the way that it works mechanically is when the user

**[01:01:12]** it works mechanically is when the user

**[01:01:12]** it works mechanically is when the user stops speaking the VAD has a timeout.

**[01:01:14]** stops speaking the VAD has a timeout.

**[01:01:14]** stops speaking the VAD has a timeout. you tell it and program it, wait, let's

**[01:01:17]** you tell it and program it, wait, let's

**[01:01:17]** you tell it and program it, wait, let's say one second, point8 seconds, half

**[01:01:19]** say one second, point8 seconds, half

**[01:01:19]** say one second, point8 seconds, half second, whatever feels natural and

**[01:01:21]** second, whatever feels natural and

**[01:01:21]** second, whatever feels natural and you're trying to balance low latency

**[01:01:23]** you're trying to balance low latency

**[01:01:23]** you're trying to balance low latency response with giving the user enough

**[01:01:25]** response with giving the user enough

**[01:01:25]** response with giving the user enough time to speak. It's a really hard thing

**[01:01:26]** time to speak. It's a really hard thing

**[01:01:26]** time to speak. It's a really hard thing and it's one of the biggest complaints

**[01:01:28]** and it's one of the biggest complaints

**[01:01:28]** and it's one of the biggest complaints is that agents will speak over the

**[01:01:30]** is that agents will speak over the

**[01:01:30]** is that agents will speak over the human. So, if you're, let's say you're

**[01:01:32]** human. So, if you're, let's say you're

**[01:01:32]** human. So, if you're, let's say you're building an interview bot, like you're

**[01:01:33]** building an interview bot, like you're

**[01:01:33]** building an interview bot, like you're using um like Tavis, one of their

**[01:01:36]** using um like Tavis, one of their

**[01:01:36]** using um like Tavis, one of their digital twins, you want to have like a

**[01:01:37]** digital twins, you want to have like a

**[01:01:37]** digital twins, you want to have like a real like likeness and you want to speak

**[01:01:39]** real like likeness and you want to speak

**[01:01:39]** real like likeness and you want to speak to it. you may take time to think

**[01:01:42]** to it. you may take time to think

**[01:01:42]** to it. you may take time to think because sometimes you have to take time

**[01:01:44]** because sometimes you have to take time

**[01:01:44]** because sometimes you have to take time to think and that's a really difficult

**[01:01:46]** to think and that's a really difficult

**[01:01:46]** to think and that's a really difficult thing for bots to do because again it's

**[01:01:48]** thing for bots to do because again it's

**[01:01:48]** thing for bots to do because again it's driven by like a simple stop speaking

**[01:01:50]** driven by like a simple stop speaking

**[01:01:50]** driven by like a simple stop speaking algorithm. So this is a new uh I guess

**[01:01:54]** algorithm. So this is a new uh I guess

**[01:01:54]** algorithm. So this is a new uh I guess it's like an emerging uh field with

**[01:01:56]** it's like an emerging uh field with

**[01:01:56]** it's like an emerging uh field with models which is looking at semantic uh

**[01:01:58]** models which is looking at semantic uh

**[01:01:58]** models which is looking at semantic uh end of turn. So driven off of things


### [01:02:00 - 01:03:00]

**[01:02:01]** end of turn. So driven off of things

**[01:02:01]** end of turn. So driven off of things like um

**[01:02:03]** like um

**[01:02:03]** like um like speech filler words, pauses, uh

**[01:02:07]** like speech filler words, pauses, uh

**[01:02:07]** like speech filler words, pauses, uh intonation, so things in the audio realm

**[01:02:08]** intonation, so things in the audio realm

**[01:02:08]** intonation, so things in the audio realm and also things in the textbased realm.

**[01:02:10]** and also things in the textbased realm.

**[01:02:10]** and also things in the textbased realm. So just looking at context. So we've

**[01:02:13]** So just looking at context. So we've

**[01:02:13]** So just looking at context. So we've actually started uh we're one of many

**[01:02:15]** actually started uh we're one of many

**[01:02:15]** actually started uh we're one of many that are doing this I think but we we

**[01:02:17]** that are doing this I think but we we

**[01:02:17]** that are doing this I think but we we launched a model if you look at it on

**[01:02:19]** launched a model if you look at it on

**[01:02:19]** launched a model if you look at it on GitHub it's under smart- turn. It's a

**[01:02:21]** GitHub it's under smart- turn. It's a

**[01:02:22]** GitHub it's under smart- turn. It's a native audioin uh classifier that runs

**[01:02:25]** native audioin uh classifier that runs

**[01:02:25]** native audioin uh classifier that runs an inference on the in input audio and

**[01:02:29]** an inference on the in input audio and

**[01:02:29]** an inference on the in input audio and it simply outputs either complete or

**[01:02:31]** it simply outputs either complete or

**[01:02:31]** it simply outputs either complete or incomplete. And the way Pipcat uses this

**[01:02:33]** incomplete. And the way Pipcat uses this

**[01:02:33]** incomplete. And the way Pipcat uses this is that if you get an incomplete

**[01:02:34]** is that if you get an incomplete

**[01:02:34]** is that if you get an incomplete response we can dynamically adjust the

**[01:02:36]** response we can dynamically adjust the

**[01:02:36]** response we can dynamically adjust the VAD timeout. So we can tell the pipecat

**[01:02:38]** VAD timeout. So we can tell the pipecat

**[01:02:38]** VAD timeout. So we can tell the pipecat bot okay he you know he or she is not

**[01:02:41]** bot okay he you know he or she is not

**[01:02:41]** bot okay he you know he or she is not done speaking let's actually move the

**[01:02:44]** done speaking let's actually move the

**[01:02:44]** done speaking let's actually move the let's give three seconds to complete the

**[01:02:46]** let's give three seconds to complete the

**[01:02:46]** let's give three seconds to complete the thought and if it's not done then the

**[01:02:47]** thought and if it's not done then the

**[01:02:47]** thought and if it's not done then the bot will actually respond. So you can

**[01:02:48]** bot will actually respond. So you can

**[01:02:48]** bot will actually respond. So you can create a little bit of like dynamic

**[01:02:50]** create a little bit of like dynamic

**[01:02:50]** create a little bit of like dynamic interaction there. That's one of the

**[01:02:52]** interaction there. That's one of the

**[01:02:52]** interaction there. That's one of the first things. I'm sure goo the Google

**[01:02:54]** first things. I'm sure goo the Google

**[01:02:54]** first things. I'm sure goo the Google team is working on similar things. I

**[01:02:56]** team is working on similar things. I

**[01:02:56]** team is working on similar things. I know openai is and all the st vendors

**[01:02:59]** know openai is and all the st vendors

**[01:02:59]** know openai is and all the st vendors are are also looking at their own


### [01:03:00 - 01:04:00]

**[01:03:00]** are are also looking at their own

**[01:03:00]** are are also looking at their own things. So, I'd say right now it is very

**[01:03:03]** things. So, I'd say right now it is very

**[01:03:03]** things. So, I'd say right now it is very much an unsolved problem, but I would

**[01:03:04]** much an unsolved problem, but I would

**[01:03:04]** much an unsolved problem, but I would imagine given how fast things are going

**[01:03:06]** imagine given how fast things are going

**[01:03:06]** imagine given how fast things are going in the next 12 months, we'll have great

**[01:03:08]** in the next 12 months, we'll have great

**[01:03:08]** in the next 12 months, we'll have great solutions that will make it even more

**[01:03:10]** solutions that will make it even more

**[01:03:10]** solutions that will make it even more natural to talk to a bot.

**[01:03:13]** natural to talk to a bot.

**[01:03:13]** natural to talk to a bot. It's a good question.

**[01:03:35]** Oh yeah yeah yeah. One uh this is

**[01:03:35]** Oh yeah yeah yeah. One uh this is actually back to the well for this is

**[01:03:36]** actually back to the well for this is

**[01:03:36]** actually back to the well for this is specific to pipecat but also um like

**[01:03:39]** specific to pipecat but also um like

**[01:03:40]** specific to pipecat but also um like Gemini live will output audio and text

**[01:03:42]** Gemini live will output audio and text

**[01:03:42]** Gemini live will output audio and text and other speechtospech LLMs do this. Uh

**[01:03:46]** and other speechtospech LLMs do this. Uh

**[01:03:46]** and other speechtospech LLMs do this. Uh pipcat offers in terms of its again

**[01:03:48]** pipcat offers in terms of its again

**[01:03:48]** pipcat offers in terms of its again orchestration role when you get a uh

**[01:03:52]** orchestration role when you get a uh

**[01:03:52]** orchestration role when you get a uh actually it's going to be specific to

**[01:03:54]** actually it's going to be specific to

**[01:03:54]** actually it's going to be specific to TTS provider. Um, many T there are great

**[01:03:57]** TTS provider. Um, many T there are great

**[01:03:57]** TTS provider. Um, many T there are great TTS providers that do word and time

**[01:03:59]** TTS providers that do word and time

**[01:03:59]** TTS providers that do word and time stamp synchronization. So they'll give


### [01:04:00 - 01:05:00]

**[01:04:00]** stamp synchronization. So they'll give

**[01:04:00]** stamp synchronization. So they'll give pairs. They call them like alignment

**[01:04:02]** pairs. They call them like alignment

**[01:04:02]** pairs. They call them like alignment pairs. So if you're using a Cartisia or

**[01:04:05]** pairs. So if you're using a Cartisia or

**[01:04:05]** pairs. So if you're using a Cartisia or an 11 Labs or Rhyme, they all output

**[01:04:08]** an 11 Labs or Rhyme, they all output

**[01:04:08]** an 11 Labs or Rhyme, they all output these pairs. One of the really cool

**[01:04:09]** these pairs. One of the really cool

**[01:04:10]** these pairs. One of the really cool things with Pipcat is that the TTS

**[01:04:12]** things with Pipcat is that the TTS

**[01:04:12]** things with Pipcat is that the TTS services output not only the audio

**[01:04:14]** services output not only the audio

**[01:04:14]** services output not only the audio stream but also the text stream. So

**[01:04:16]** stream but also the text stream. So

**[01:04:16]** stream but also the text stream. So they'll output text frames, TTS text

**[01:04:18]** they'll output text frames, TTS text

**[01:04:18]** they'll output text frames, TTS text frames we call them in Pipcat. And if

**[01:04:20]** frames we call them in Pipcat. And if

**[01:04:20]** frames we call them in Pipcat. And if you place uh we have in terms of how the

**[01:04:23]** you place uh we have in terms of how the

**[01:04:23]** you place uh we have in terms of how the client software works there is uh like

**[01:04:25]** client software works there is uh like

**[01:04:25]** client software works there is uh like an observer role where you can actually

**[01:04:27]** an observer role where you can actually

**[01:04:27]** an observer role where you can actually watch there's a process that can watch

**[01:04:29]** watch there's a process that can watch

**[01:04:29]** watch there's a process that can watch things that happen in the pipeline and

**[01:04:30]** things that happen in the pipeline and

**[01:04:30]** things that happen in the pipeline and emit events. So we've instrumented that

**[01:04:32]** emit events. So we've instrumented that

**[01:04:32]** emit events. So we've instrumented that for the clients so that whenever you see

**[01:04:35]** for the clients so that whenever you see

**[01:04:35]** for the clients so that whenever you see those text frames move through the

**[01:04:37]** those text frames move through the

**[01:04:37]** those text frames move through the transport you can get synchronized word

**[01:04:39]** transport you can get synchronized word

**[01:04:39]** transport you can get synchronized word and audio output. So in your client if

**[01:04:41]** and audio output. So in your client if

**[01:04:41]** and audio output. So in your client if you wanted to have wordbyword output

**[01:04:43]** you wanted to have wordbyword output

**[01:04:43]** you wanted to have wordbyword output synchronized to the audio you can do

**[01:04:44]** synchronized to the audio you can do

**[01:04:44]** synchronized to the audio you can do that with pipecat and it's as simple as

**[01:04:47]** that with pipecat and it's as simple as

**[01:04:47]** that with pipecat and it's as simple as just adding an event. I think you listen

**[01:04:49]** just adding an event. I think you listen

**[01:04:49]** just adding an event. I think you listen to like bot tts text output or onbot tts

**[01:04:52]** to like bot tts text output or onbot tts

**[01:04:52]** to like bot tts text output or onbot tts text and it will give you the

**[01:04:53]** text and it will give you the

**[01:04:53]** text and it will give you the synchronized output.


### [01:05:00 - 01:06:00]

**[01:05:08]** fully offline. Um, well, they're all

**[01:05:08]** fully offline. Um, well, they're all doable. There are great models. I think

**[01:05:09]** doable. There are great models. I think

**[01:05:09]** doable. There are great models. I think it really depends on what your bot needs

**[01:05:11]** it really depends on what your bot needs

**[01:05:11]** it really depends on what your bot needs to accomplish. Um, a lot of the

**[01:05:13]** to accomplish. Um, a lot of the

**[01:05:13]** to accomplish. Um, a lot of the state-of-the-art models to do all the

**[01:05:15]** state-of-the-art models to do all the

**[01:05:15]** state-of-the-art models to do all the best and smartest things need to have

**[01:05:17]** best and smartest things need to have

**[01:05:17]** best and smartest things need to have some like they're going to be run like

**[01:05:19]** some like they're going to be run like

**[01:05:20]** some like they're going to be run like on prem or in the cloud. Um, but if you

**[01:05:22]** on prem or in the cloud. Um, but if you

**[01:05:22]** on prem or in the cloud. Um, but if you have a lot of bots do jobs like if you

**[01:05:24]** have a lot of bots do jobs like if you

**[01:05:24]** have a lot of bots do jobs like if you wanted to build like a restaurant

**[01:05:26]** wanted to build like a restaurant

**[01:05:26]** wanted to build like a restaurant reservation one like I referenced

**[01:05:27]** reservation one like I referenced

**[01:05:27]** reservation one like I referenced earlier, it's a very simple job. You

**[01:05:29]** earlier, it's a very simple job. You

**[01:05:29]** earlier, it's a very simple job. You could probably run it with some version

**[01:05:31]** could probably run it with some version

**[01:05:31]** could probably run it with some version of Llama running locally. Um there are

**[01:05:34]** of Llama running locally. Um there are

**[01:05:34]** of Llama running locally. Um there are great local something again Quinn has

**[01:05:37]** great local something again Quinn has

**[01:05:37]** great local something again Quinn has been experimenting with uh a lot of

**[01:05:39]** been experimenting with uh a lot of

**[01:05:39]** been experimenting with uh a lot of great local models like u whisper has

**[01:05:43]** great local models like u whisper has

**[01:05:43]** great local models like u whisper has challenges you know I mean it's it has a

**[01:05:45]** challenges you know I mean it's it has a

**[01:05:46]** challenges you know I mean it's it has a lot it has some challenges uh as an open

**[01:05:49]** lot it has some challenges uh as an open

**[01:05:49]** lot it has some challenges uh as an open source model for ST but there are good

**[01:05:51]** source model for ST but there are good

**[01:05:51]** source model for ST but there are good and emerging TTS services so you know I

**[01:05:54]** and emerging TTS services so you know I

**[01:05:54]** and emerging TTS services so you know I I things are only as good as the input

**[01:05:56]** I things are only as good as the input

**[01:05:56]** I things are only as good as the input and we've actually seen this with some

**[01:05:57]** and we've actually seen this with some

**[01:05:58]** and we've actually seen this with some of the speechtospech models that

**[01:05:59]** of the speechtospech models that

**[01:05:59]** of the speechtospech models that sometimes they mistranscribe so you


### [01:06:00 - 01:07:00]

**[01:06:01]** sometimes they mistranscribe so you

**[01:06:01]** sometimes they mistranscribe so you really need I mean it's you know there

**[01:06:02]** really need I mean it's you know there

**[01:06:02]** really need I mean it's you know there every part is critical, but if you can't

**[01:06:04]** every part is critical, but if you can't

**[01:06:04]** every part is critical, but if you can't transcribe the speech really well,

**[01:06:06]** transcribe the speech really well,

**[01:06:06]** transcribe the speech really well, nothing really matters. Like it has to

**[01:06:07]** nothing really matters. Like it has to

**[01:06:08]** nothing really matters. Like it has to understand you. And having like

**[01:06:09]** understand you. And having like

**[01:06:09]** understand you. And having like disluencies or like hallucinated

**[01:06:11]** disluencies or like hallucinated

**[01:06:11]** disluencies or like hallucinated responses or even just inaccurate

**[01:06:13]** responses or even just inaccurate

**[01:06:13]** responses or even just inaccurate responses kind of breaks everything

**[01:06:15]** responses kind of breaks everything

**[01:06:15]** responses kind of breaks everything down. So things mostly start at at the

**[01:06:17]** down. So things mostly start at at the

**[01:06:17]** down. So things mostly start at at the ST. So maybe that's the hardest. I don't

**[01:06:19]** ST. So maybe that's the hardest. I don't

**[01:06:19]** ST. So maybe that's the hardest. I don't know if there are a lot of good open

**[01:06:20]** know if there are a lot of good open

**[01:06:20]** know if there are a lot of good open source options for that right now.

**[01:06:23]** source options for that right now.

**[01:06:23]** source options for that right now. I don't know. We don't we're not doing

**[01:06:25]** I don't know. We don't we're not doing

**[01:06:25]** I don't know. We don't we're not doing anything in the ST world. No, no, no.

**[01:06:29]** anything in the ST world. No, no, no.

**[01:06:29]** anything in the ST world. No, no, no. That's a whole different ballgame.

**[01:06:31]** That's a whole different ballgame.

**[01:06:31]** That's a whole different ballgame. Good question though. just made me

**[01:06:33]** Good question though. just made me

**[01:06:33]** Good question though. just made me realize we could have used local models

**[01:06:35]** realize we could have used local models

**[01:06:36]** realize we could have used local models and avoid this. We could have. Yeah.

**[01:06:38]** and avoid this. We could have. Yeah.

**[01:06:38]** and avoid this. We could have. Yeah. Well, we're partnering with the the

**[01:06:40]** Well, we're partnering with the the

**[01:06:40]** Well, we're partnering with the the Google team. Yeah. Yeah. As a Yeah,

**[01:06:43]** Google team. Yeah. Yeah. As a Yeah,

**[01:06:43]** Google team. Yeah. Yeah. As a Yeah, exactly. Yeah.

**[01:06:45]** exactly. Yeah.

**[01:06:45]** exactly. Yeah. Has anyone looked at any of the sample

**[01:06:48]** Has anyone looked at any of the sample

**[01:06:48]** Has anyone looked at any of the sample projects and had questions? There's a

**[01:06:50]** projects and had questions? There's a

**[01:06:50]** projects and had questions? There's a lot of interesting things there. If any

**[01:06:51]** lot of interesting things there. If any

**[01:06:51]** lot of interesting things there. If any of this is like interested you, we do

**[01:06:53]** of this is like interested you, we do

**[01:06:53]** of this is like interested you, we do have a Discord. You're welcome to get on

**[01:06:55]** have a Discord. You're welcome to get on

**[01:06:55]** have a Discord. You're welcome to get on it. Um, you can find us at pipcat.ai

**[01:06:59]** it. Um, you can find us at pipcat.ai

**[01:06:59]** it. Um, you can find us at pipcat.ai and find our Discord there. You can ask


### [01:07:00 - 01:08:00]

**[01:07:00]** and find our Discord there. You can ask

**[01:07:00]** and find our Discord there. You can ask questions. Um, there's some really cool

**[01:07:03]** questions. Um, there's some really cool

**[01:07:03]** questions. Um, there's some really cool stuff with Gemini that can be done

**[01:07:05]** stuff with Gemini that can be done

**[01:07:05]** stuff with Gemini that can be done there. Uh, in particular in the Pipecat

**[01:07:07]** there. Uh, in particular in the Pipecat

**[01:07:07]** there. Uh, in particular in the Pipecat repo, we built uh, I don't know if you

**[01:07:09]** repo, we built uh, I don't know if you

**[01:07:09]** repo, we built uh, I don't know if you know the game catchphrase where you

**[01:07:11]** know the game catchphrase where you

**[01:07:11]** know the game catchphrase where you describe a word and something, you know,

**[01:07:12]** describe a word and something, you know,

**[01:07:12]** describe a word and something, you know, guesses it. We built a version of that.

**[01:07:14]** guesses it. We built a version of that.

**[01:07:14]** guesses it. We built a version of that. We had to brand it something else called

**[01:07:16]** We had to brand it something else called

**[01:07:16]** We had to brand it something else called word wrangler and you as the human, you

**[01:07:19]** word wrangler and you as the human, you

**[01:07:19]** word wrangler and you as the human, you describe a word and then you have the AI

**[01:07:21]** describe a word and then you have the AI

**[01:07:21]** describe a word and then you have the AI agent try to answer it. So, we built a

**[01:07:22]** agent try to answer it. So, we built a

**[01:07:22]** agent try to answer it. So, we built a client server version of that which I

**[01:07:24]** client server version of that which I

**[01:07:24]** client server version of that which I linked to in the repo. And then we have

**[01:07:26]** linked to in the repo. And then we have

**[01:07:26]** linked to in the repo. And then we have one that's a phone based one that's I

**[01:07:28]** one that's a phone based one that's I

**[01:07:28]** one that's a phone based one that's I think particularly sophisticated and

**[01:07:30]** think particularly sophisticated and

**[01:07:30]** think particularly sophisticated and interesting. So you might think like how

**[01:07:31]** interesting. So you might think like how

**[01:07:32]** interesting. So you might think like how the hell would I build this with a

**[01:07:33]** the hell would I build this with a

**[01:07:34]** the hell would I build this with a speech-to-spech model? We actually use

**[01:07:35]** speech-to-spech model? We actually use

**[01:07:35]** speech-to-spech model? We actually use two Gemini agents in the same call and

**[01:07:38]** two Gemini agents in the same call and

**[01:07:38]** two Gemini agents in the same call and we use a parallel pipeline where one

**[01:07:40]** we use a parallel pipeline where one

**[01:07:40]** we use a parallel pipeline where one agent is the host giving out the the

**[01:07:43]** agent is the host giving out the the

**[01:07:43]** agent is the host giving out the the questions to the human user, the other

**[01:07:45]** questions to the human user, the other

**[01:07:45]** questions to the human user, the other is the guesser and we have you know kind

**[01:07:47]** is the guesser and we have you know kind

**[01:07:47]** is the guesser and we have you know kind of limit the audio flow so that the

**[01:07:49]** of limit the audio flow so that the

**[01:07:49]** of limit the audio flow so that the guesser the AI player can only hear the

**[01:07:51]** guesser the AI player can only hear the

**[01:07:51]** guesser the AI player can only hear the user. So there's a bunch of really

**[01:07:53]** user. So there's a bunch of really

**[01:07:53]** user. So there's a bunch of really interesting things getting into the like

**[01:07:54]** interesting things getting into the like

**[01:07:54]** interesting things getting into the like majorly into the weeds of some of the

**[01:07:56]** majorly into the weeds of some of the

**[01:07:56]** majorly into the weeds of some of the powers of u pipecat, but it also speaks

**[01:07:58]** powers of u pipecat, but it also speaks

**[01:07:58]** powers of u pipecat, but it also speaks to the strength of having just native


### [01:08:00 - 01:09:00]

**[01:08:00]** to the strength of having just native

**[01:08:00]** to the strength of having just native audio input being really really help

**[01:08:02]** audio input being really really help

**[01:08:02]** audio input being really really help helpful. So I'd recommend checking those

**[01:08:04]** helpful. So I'd recommend checking those

**[01:08:04]** helpful. So I'd recommend checking those out. Um really cool easy demos to run.

**[01:08:07]** out. Um really cool easy demos to run.

**[01:08:07]** out. Um really cool easy demos to run. One's Twilio, the other is again a

**[01:08:09]** One's Twilio, the other is again a

**[01:08:09]** One's Twilio, the other is again a client server. I think it's like a React

**[01:08:11]** client server. I think it's like a React

**[01:08:11]** client server. I think it's like a React Nex.js project.

**[01:08:18]** What's that?

**[01:08:18]** What's that? Word wrangler.

**[01:08:20]** Word wrangler.

**[01:08:20]** Word wrangler. Yeah, I mean we could run the word

**[01:08:21]** Yeah, I mean we could run the word

**[01:08:21]** Yeah, I mean we could run the word wrangler client app. It's actually just

**[01:08:23]** wrangler client app. It's actually just

**[01:08:24]** wrangler client app. It's actually just on the web

**[01:08:26]** on the web

**[01:08:26]** on the web test.

**[01:08:28]** test.

**[01:08:28]** test. Welcome to Word Wrangler. I I'll try to

**[01:08:31]** Welcome to Word Wrangler. I I'll try to

**[01:08:31]** Welcome to Word Wrangler. I I'll try to guess the words you describe. Remember,

**[01:08:34]** guess the words you describe. Remember,

**[01:08:34]** guess the words you describe. Remember, don't say any part of the word itself.

**[01:08:36]** don't say any part of the word itself.

**[01:08:36]** don't say any part of the word itself. Ready? Let's go.

**[01:08:39]** Ready? Let's go.

**[01:08:39]** Ready? Let's go. Uh I'm going to skip to something

**[01:08:42]** Uh I'm going to skip to something

**[01:08:42]** Uh I'm going to skip to something easier. Okay. This is something you take

**[01:08:43]** easier. Okay. This is something you take

**[01:08:43]** easier. Okay. This is something you take pictures with. It's on your phone.

**[01:08:49]** Is it camera? All

**[01:08:50]** Is it camera? All right. This is a field uh related to the

**[01:08:52]** right. This is a field uh related to the

**[01:08:52]** right. This is a field uh related to the study of languages, I think.

**[01:08:56]** study of languages, I think.

**[01:08:56]** study of languages, I think. Is it linguistics? All right. This is a

**[01:08:58]** Is it linguistics? All right. This is a

**[01:08:58]** Is it linguistics? All right. This is a game of the yellow ball you play with

**[01:08:59]** game of the yellow ball you play with

**[01:08:59]** game of the yellow ball you play with rackets. Hit the ball over the net.


### [01:09:00 - 01:10:00]

**[01:09:03]** rackets. Hit the ball over the net.

**[01:09:03]** rackets. Hit the ball over the net. Is it tennis?

**[01:09:05]** Is it tennis?

**[01:09:05]** Is it tennis? All right. This is a a round dessert

**[01:09:08]** All right. This is a a round dessert

**[01:09:08]** All right. This is a a round dessert with chocolate chips sometimes and other

**[01:09:10]** with chocolate chips sometimes and other

**[01:09:10]** with chocolate chips sometimes and other fun goodies.

**[01:09:13]** fun goodies.

**[01:09:13]** fun goodies. Is it cookie? It's really good even when

**[01:09:15]** Is it cookie? It's really good even when

**[01:09:15]** Is it cookie? It's really good even when I'm bad at giving answers. So, pretty

**[01:09:18]** I'm bad at giving answers. So, pretty

**[01:09:18]** I'm bad at giving answers. So, pretty cool. This is with built with Gemini

**[01:09:20]** cool. This is with built with Gemini

**[01:09:20]** cool. This is with built with Gemini live. But again, just an example of

**[01:09:22]** live. But again, just an example of

**[01:09:22]** live. But again, just an example of things you can build with uh

**[01:09:25]** things you can build with uh

**[01:09:25]** things you can build with uh with voice AI. So cool, unique

**[01:09:27]** with voice AI. So cool, unique

**[01:09:27]** with voice AI. So cool, unique interactions.

**[01:09:33]** All right, I think that's about it.

**[01:09:33]** All right, I think that's about it. Thanks everybody.


