# Why ChatGPT Keeps Interrupting You — Dr. Tom Shapland, LiveKit

**Video URL:** https://www.youtube.com/watch?v=1v9zBiZKlIY

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** I'm going to jump right into it. I'm

**[00:16]** I'm going to jump right into it. I'm going to be talking about Voice AI's

**[00:18]** going to be talking about Voice AI's

**[00:18]** going to be talking about Voice AI's interruption problem. Then after that,

**[00:20]** interruption problem. Then after that,

**[00:20]** interruption problem. Then after that, I'm going to talk about how we currently

**[00:22]** I'm going to talk about how we currently

**[00:22]** I'm going to talk about how we currently handle interruptions and turn taking in

**[00:24]** handle interruptions and turn taking in

**[00:24]** handle interruptions and turn taking in voice AI. what we can learn from the

**[00:26]** voice AI. what we can learn from the

**[00:26]** voice AI. what we can learn from the study of human conversation on how to

**[00:28]** study of human conversation on how to

**[00:28]** study of human conversation on how to handle how humans handle turn taking and

**[00:31]** handle how humans handle turn taking and

**[00:31]** handle how humans handle turn taking and then about some of the really neat and

**[00:33]** then about some of the really neat and

**[00:33]** then about some of the really neat and interesting new approaches out there for

**[00:35]** interesting new approaches out there for

**[00:35]** interesting new approaches out there for handling turn taking and interruptions

**[00:37]** handling turn taking and interruptions

**[00:37]** handling turn taking and interruptions in voice AI agents. Um voice excuse me

**[00:41]** in voice AI agents. Um voice excuse me

**[00:41]** in voice AI agents. Um voice excuse me interruptions are the biggest problem in

**[00:43]** interruptions are the biggest problem in

**[00:43]** interruptions are the biggest problem in voice AI agents right now. When you're

**[00:46]** voice AI agents right now. When you're

**[00:46]** voice AI agents right now. When you're talking to chat GPT advanced voice mode

**[00:48]** talking to chat GPT advanced voice mode

**[00:48]** talking to chat GPT advanced voice mode and it interrupts you, it's annoying.

**[00:51]** and it interrupts you, it's annoying.

**[00:51]** and it interrupts you, it's annoying. But when you're talking when a patient

**[00:53]** But when you're talking when a patient

**[00:53]** But when you're talking when a patient is talking to a voice AI dental

**[00:55]** is talking to a voice AI dental

**[00:55]** is talking to a voice AI dental assistant and it interrupts the patient,

**[00:58]** assistant and it interrupts the patient,

**[00:58]** assistant and it interrupts the patient, the patient hangs up and the dentist


### [01:00 - 02:00]

**[01:00]** the patient hangs up and the dentist

**[01:00]** the patient hangs up and the dentist stops paying the voice AI developer.

**[01:02]** stops paying the voice AI developer.

**[01:02]** stops paying the voice AI developer. This is our collective problem. This is

**[01:03]** This is our collective problem. This is

**[01:04]** This is our collective problem. This is all of our problem that we we all have

**[01:05]** all of our problem that we we all have

**[01:05]** all of our problem that we we all have to solve.

**[01:07]** to solve.

**[01:07]** to solve. Um and the the problem is like turn

**[01:10]** Um and the the problem is like turn

**[01:10]** Um and the the problem is like turn taking is just hard. Um let me first

**[01:12]** taking is just hard. Um let me first

**[01:12]** taking is just hard. Um let me first like define what turn taking is. Turn

**[01:14]** like define what turn taking is. Turn

**[01:14]** like define what turn taking is. Turn taking is this unspoken system we have

**[01:16]** taking is this unspoken system we have

**[01:16]** taking is this unspoken system we have for who controls the floor on um between

**[01:21]** for who controls the floor on um between

**[01:21]** for who controls the floor on um between speakers uh during a conversation and

**[01:24]** speakers uh during a conversation and

**[01:24]** speakers uh during a conversation and fundamentally it's hard because turn

**[01:27]** fundamentally it's hard because turn

**[01:27]** fundamentally it's hard because turn taking happens really fast in human

**[01:28]** taking happens really fast in human

**[01:28]** taking happens really fast in human conversation um and there's no oneize

**[01:31]** conversation um and there's no oneize

**[01:31]** conversation um and there's no oneize that fits all. So, this is this really

**[01:32]** that fits all. So, this is this really

**[01:32]** that fits all. So, this is this really cool um study that I pulled this data

**[01:35]** cool um study that I pulled this data

**[01:35]** cool um study that I pulled this data from where they're looking at how long

**[01:37]** from where they're looking at how long

**[01:37]** from where they're looking at how long it took a listener to start responding

**[01:40]** it took a listener to start responding

**[01:40]** it took a listener to start responding after the speaker finished speaking um

**[01:43]** after the speaker finished speaking um

**[01:43]** after the speaker finished speaking um across different cultures. And we can

**[01:45]** across different cultures. And we can

**[01:45]** across different cultures. And we can see that the Danes take a relatively

**[01:47]** see that the Danes take a relatively

**[01:47]** see that the Danes take a relatively long amount of time to start speaking

**[01:50]** long amount of time to start speaking

**[01:50]** long amount of time to start speaking after uh the other speaker finishes

**[01:52]** after uh the other speaker finishes

**[01:52]** after uh the other speaker finishes speaking, but the Japanese do it almost

**[01:55]** speaking, but the Japanese do it almost

**[01:55]** speaking, but the Japanese do it almost instantaneously. So, there's differences

**[01:57]** instantaneously. So, there's differences

**[01:57]** instantaneously. So, there's differences across cultures. That's part of what

**[01:59]** across cultures. That's part of what

**[01:59]** across cultures. That's part of what makes it hard. There's also differences


### [02:00 - 03:00]

**[02:00]** makes it hard. There's also differences

**[02:00]** makes it hard. There's also differences across individuals. I'm one of those

**[02:02]** across individuals. I'm one of those

**[02:02]** across individuals. I'm one of those people that takes a long time to

**[02:04]** people that takes a long time to

**[02:04]** people that takes a long time to respond. Even before I got into voice

**[02:05]** respond. Even before I got into voice

**[02:06]** respond. Even before I got into voice AI, people would sometimes comment being

**[02:07]** AI, people would sometimes comment being

**[02:07]** AI, people would sometimes comment being like, "Are you gonna respond?" I'm like,

**[02:09]** like, "Are you gonna respond?" I'm like,

**[02:09]** like, "Are you gonna respond?" I'm like, "Yeah, yeah, thinking about it." Um, and

**[02:12]** "Yeah, yeah, thinking about it." Um, and

**[02:12]** "Yeah, yeah, thinking about it." Um, and uh also like even though I'm one

**[02:14]** uh also like even though I'm one

**[02:14]** uh also like even though I'm one individual, there's a lot of variability

**[02:15]** individual, there's a lot of variability

**[02:15]** individual, there's a lot of variability in how quickly I respond. Like if you

**[02:18]** in how quickly I respond. Like if you

**[02:18]** in how quickly I respond. Like if you make me angry, I'm probably going to

**[02:19]** make me angry, I'm probably going to

**[02:19]** make me angry, I'm probably going to respond kind of quicker. Um, so it's

**[02:22]** respond kind of quicker. Um, so it's

**[02:22]** respond kind of quicker. Um, so it's just a hard problem. And in the the next

**[02:25]** just a hard problem. And in the the next

**[02:25]** just a hard problem. And in the the next slide I want to talk about for people

**[02:26]** slide I want to talk about for people

**[02:26]** slide I want to talk about for people who are not very familiar with how voice

**[02:29]** who are not very familiar with how voice

**[02:29]** who are not very familiar with how voice AI agent pipelines work. I'm going to

**[02:31]** AI agent pipelines work. I'm going to

**[02:31]** AI agent pipelines work. I'm going to provide like a simplified overview of

**[02:32]** provide like a simplified overview of

**[02:32]** provide like a simplified overview of how we handle handle turn taking and

**[02:34]** how we handle handle turn taking and

**[02:34]** how we handle handle turn taking and interruptions in voice AI agents

**[02:36]** interruptions in voice AI agents

**[02:36]** interruptions in voice AI agents currently. So the user starts speaking

**[02:39]** currently. So the user starts speaking

**[02:39]** currently. So the user starts speaking that's the speech input and that audio

**[02:41]** that's the speech input and that audio

**[02:41]** that's the speech input and that audio those audio chunks are passed to a

**[02:42]** those audio chunks are passed to a

**[02:42]** those audio chunks are passed to a speechtoext model. Um and that

**[02:45]** speechtoext model. Um and that

**[02:45]** speechtoext model. Um and that speechtoext model uh transcribes the uh

**[02:49]** speechtoext model uh transcribes the uh

**[02:49]** speechtoext model uh transcribes the uh audio into uh a transcription. The next

**[02:52]** audio into uh a transcription. The next

**[02:52]** audio into uh a transcription. The next step is something called a VAD that

**[02:54]** step is something called a VAD that

**[02:54]** step is something called a VAD that determines whether or not the user has

**[02:56]** determines whether or not the user has

**[02:56]** determines whether or not the user has finished speaking. Um, I'm going to go

**[02:58]** finished speaking. Um, I'm going to go

**[02:58]** finished speaking. Um, I'm going to go more into that in a moment. The next


### [03:00 - 04:00]

**[03:01]** more into that in a moment. The next

**[03:01]** more into that in a moment. The next step, if the user has finished speaking,

**[03:02]** step, if the user has finished speaking,

**[03:02]** step, if the user has finished speaking, the transcript is passed to an LLM and

**[03:04]** the transcript is passed to an LLM and

**[03:04]** the transcript is passed to an LLM and the LLM outputs its chat completion.

**[03:07]** the LLM outputs its chat completion.

**[03:07]** the LLM outputs its chat completion. That chat completion is streamed out and

**[03:09]** That chat completion is streamed out and

**[03:09]** That chat completion is streamed out and that stream is passed to a texttospech

**[03:11]** that stream is passed to a texttospech

**[03:11]** that stream is passed to a texttospech model where it's converted into audio

**[03:12]** model where it's converted into audio

**[03:12]** model where it's converted into audio and that audio which is the audio of now

**[03:14]** and that audio which is the audio of now

**[03:14]** and that audio which is the audio of now of the voice AI agent is passed back to

**[03:17]** of the voice AI agent is passed back to

**[03:17]** of the voice AI agent is passed back to the user.

**[03:19]** the user.

**[03:19]** the user. Um, let's dig more into the voice

**[03:22]** Um, let's dig more into the voice

**[03:22]** Um, let's dig more into the voice activity detection system. It's a system

**[03:26]** activity detection system. It's a system

**[03:26]** activity detection system. It's a system with primarily two parts. So, it's a

**[03:28]** with primarily two parts. So, it's a

**[03:28]** with primarily two parts. So, it's a machine learning model, a neural network

**[03:30]** machine learning model, a neural network

**[03:30]** machine learning model, a neural network that is detecting whether or not

**[03:32]** that is detecting whether or not

**[03:32]** that is detecting whether or not somebody is speaking. So, it's like

**[03:34]** somebody is speaking. So, it's like

**[03:34]** somebody is speaking. So, it's like speech or not speech. It's pretty simple

**[03:37]** speech or not speech. It's pretty simple

**[03:37]** speech or not speech. It's pretty simple um machine. It's not I shouldn't call it

**[03:39]** um machine. It's not I shouldn't call it

**[03:39]** um machine. It's not I shouldn't call it simple, but it's it's a really neat

**[03:40]** simple, but it's it's a really neat

**[03:40]** simple, but it's it's a really neat model, but it's it's ultimately just

**[03:42]** model, but it's it's ultimately just

**[03:42]** model, but it's it's ultimately just looking at speech or not speech. And

**[03:44]** looking at speech or not speech. And

**[03:44]** looking at speech or not speech. And then the next thing next part of it is a

**[03:46]** then the next thing next part of it is a

**[03:46]** then the next thing next part of it is a silence algorithm. And the silence

**[03:48]** silence algorithm. And the silence

**[03:48]** silence algorithm. And the silence algorithm is saying, okay, if the person

**[03:51]** algorithm is saying, okay, if the person

**[03:51]** algorithm is saying, okay, if the person hasn't spoken for more than half a

**[03:53]** hasn't spoken for more than half a

**[03:53]** hasn't spoken for more than half a second, they're done speaking and it's

**[03:55]** second, they're done speaking and it's

**[03:55]** second, they're done speaking and it's time for the agent to start speaking. So

**[03:59]** time for the agent to start speaking. So

**[03:59]** time for the agent to start speaking. So that's the in most production voice AI


### [04:00 - 05:00]

**[04:01]** that's the in most production voice AI

**[04:01]** that's the in most production voice AI systems, we're using something like that

**[04:04]** systems, we're using something like that

**[04:04]** systems, we're using something like that sort of VAD. Um, and that's changing.

**[04:05]** sort of VAD. Um, and that's changing.

**[04:05]** sort of VAD. Um, and that's changing. We're building all sorts of new

**[04:06]** We're building all sorts of new

**[04:06]** We're building all sorts of new interesting things that I'll cover later

**[04:08]** interesting things that I'll cover later

**[04:08]** interesting things that I'll cover later in the presentation. Um the next part of

**[04:10]** in the presentation. Um the next part of

**[04:10]** in the presentation. Um the next part of my presentation I want to dig into what

**[04:13]** my presentation I want to dig into what

**[04:13]** my presentation I want to dig into what we can learn from linguistics and

**[04:14]** we can learn from linguistics and

**[04:14]** we can learn from linguistics and academic research about how human how

**[04:16]** academic research about how human how

**[04:16]** academic research about how human how turn taking works in human

**[04:18]** turn taking works in human

**[04:18]** turn taking works in human conversations. And one of the lines I

**[04:20]** conversations. And one of the lines I

**[04:20]** conversations. And one of the lines I read in a paper I read was that I really

**[04:22]** read in a paper I read was that I really

**[04:22]** read in a paper I read was that I really liked was that turn taking in human

**[04:25]** liked was that turn taking in human

**[04:25]** liked was that turn taking in human conversation is a psycho linguistic

**[04:26]** conversation is a psycho linguistic

**[04:26]** conversation is a psycho linguistic puzzle and that we respond in 200

**[04:29]** puzzle and that we respond in 200

**[04:29]** puzzle and that we respond in 200 milliseconds but the process of like

**[04:31]** milliseconds but the process of like

**[04:31]** milliseconds but the process of like finding the words and generating speech

**[04:33]** finding the words and generating speech

**[04:34]** finding the words and generating speech and articulating speech takes 600

**[04:35]** and articulating speech takes 600

**[04:35]** and articulating speech takes 600 milliseconds. So how can we possibly be

**[04:38]** milliseconds. So how can we possibly be

**[04:38]** milliseconds. So how can we possibly be speaking

**[04:39]** speaking

**[04:39]** speaking so quickly. How can the listener start

**[04:41]** so quickly. How can the listener start

**[04:41]** so quickly. How can the listener start returning uh an answer so speak so

**[04:44]** returning uh an answer so speak so

**[04:44]** returning uh an answer so speak so quickly when it takes much longer to

**[04:46]** quickly when it takes much longer to

**[04:46]** quickly when it takes much longer to actually generate the speech? And the

**[04:48]** actually generate the speech? And the

**[04:48]** actually generate the speech? And the answer is that there has to be

**[04:49]** answer is that there has to be

**[04:49]** answer is that there has to be prediction going on. The listener is

**[04:51]** prediction going on. The listener is

**[04:51]** prediction going on. The listener is predicting when the end of turn is going

**[04:54]** predicting when the end of turn is going

**[04:54]** predicting when the end of turn is going to occur and then they're they start to

**[04:57]** to occur and then they're they start to

**[04:57]** to occur and then they're they start to generate speech before that end of turn.

**[04:59]** generate speech before that end of turn.

**[04:59]** generate speech before that end of turn. And what are the primary inputs in


### [05:00 - 06:00]

**[05:01]** And what are the primary inputs in

**[05:01]** And what are the primary inputs in creating that prediction? The primary

**[05:03]** creating that prediction? The primary

**[05:03]** creating that prediction? The primary inputs on creating that pred prediction

**[05:04]** inputs on creating that pred prediction

**[05:04]** inputs on creating that pred prediction are the semantic and this one's the most

**[05:06]** are the semantic and this one's the most

**[05:06]** are the semantic and this one's the most important one like what the content is

**[05:08]** important one like what the content is

**[05:08]** important one like what the content is of the of what the person is saying.

**[05:10]** of the of what the person is saying.

**[05:10]** of the of what the person is saying. Other inputs into this you know

**[05:12]** Other inputs into this you know

**[05:12]** Other inputs into this you know prediction algorithm in our head of when

**[05:13]** prediction algorithm in our head of when

**[05:13]** prediction algorithm in our head of when we're trying to predict when the speaker

**[05:15]** we're trying to predict when the speaker

**[05:15]** we're trying to predict when the speaker is going to finish speaking is the

**[05:17]** is going to finish speaking is the

**[05:17]** is going to finish speaking is the syntax the structure of the sentence the

**[05:19]** syntax the structure of the sentence the

**[05:19]** syntax the structure of the sentence the procity like the the expressiveness um

**[05:22]** procity like the the expressiveness um

**[05:22]** procity like the the expressiveness um the tone and then also visual cues.

**[05:26]** the tone and then also visual cues.

**[05:26]** the tone and then also visual cues. Um like most things in uh how the human

**[05:30]** Um like most things in uh how the human

**[05:30]** Um like most things in uh how the human mind works, we we actually don't really

**[05:32]** mind works, we we actually don't really

**[05:32]** mind works, we we actually don't really know like you know that's it's

**[05:34]** know like you know that's it's

**[05:34]** know like you know that's it's complicated. Um and but I I would say

**[05:38]** complicated. Um and but I I would say

**[05:38]** complicated. Um and but I I would say one of the generally accepted models is

**[05:39]** one of the generally accepted models is

**[05:39]** one of the generally accepted models is what I'm going to walk through now of

**[05:41]** what I'm going to walk through now of

**[05:41]** what I'm going to walk through now of how turn taking works in the human

**[05:43]** how turn taking works in the human

**[05:43]** how turn taking works in the human minds. It's broken up into three stages.

**[05:46]** minds. It's broken up into three stages.

**[05:46]** minds. It's broken up into three stages. The first stage is semantic prediction.

**[05:48]** The first stage is semantic prediction.

**[05:48]** The first stage is semantic prediction. So, what the listener is doing, and

**[05:50]** So, what the listener is doing, and

**[05:50]** So, what the listener is doing, and you'll notice this as you speak to other

**[05:52]** you'll notice this as you speak to other

**[05:52]** you'll notice this as you speak to other people at the conference, is if you like

**[05:53]** people at the conference, is if you like

**[05:53]** people at the conference, is if you like are paying attention to your your

**[05:55]** are paying attention to your your

**[05:55]** are paying attention to your your thought process, is you're constantly

**[05:57]** thought process, is you're constantly

**[05:57]** thought process, is you're constantly inferring the intended message of the

**[05:59]** inferring the intended message of the

**[05:59]** inferring the intended message of the person that's speaking to you. So,


### [06:00 - 07:00]

**[06:01]** person that's speaking to you. So,

**[06:01]** person that's speaking to you. So, before they finish speaking, you're kind

**[06:03]** before they finish speaking, you're kind

**[06:03]** before they finish speaking, you're kind of figuring out, wait, what are they

**[06:05]** of figuring out, wait, what are they

**[06:05]** of figuring out, wait, what are they trying to say? And then you're using

**[06:06]** trying to say? And then you're using

**[06:06]** trying to say? And then you're using what what your your prediction of what

**[06:08]** what what your your prediction of what

**[06:08]** what what your your prediction of what they're trying to say to um uh to then

**[06:13]** they're trying to say to um uh to then

**[06:13]** they're trying to say to um uh to then use that information to predict when the

**[06:15]** use that information to predict when the

**[06:16]** use that information to predict when the end of utterance will occur. And you're

**[06:17]** end of utterance will occur. And you're

**[06:17]** end of utterance will occur. And you're not doing this just once. You're doing

**[06:19]** not doing this just once. You're doing

**[06:19]** not doing this just once. You're doing this multiple times again and again,

**[06:20]** this multiple times again and again,

**[06:20]** this multiple times again and again, right? You're constantly updating this

**[06:22]** right? You're constantly updating this

**[06:22]** right? You're constantly updating this prediction as the speaker keeps going.

**[06:23]** prediction as the speaker keeps going.

**[06:24]** prediction as the speaker keeps going. So that's the first stage. Um then the

**[06:27]** So that's the first stage. Um then the

**[06:27]** So that's the first stage. Um then the the next stage once it seems like you

**[06:29]** the next stage once it seems like you

**[06:29]** the next stage once it seems like you have a general idea, your your

**[06:31]** have a general idea, your your

**[06:31]** have a general idea, your your prediction is coming true of like when

**[06:33]** prediction is coming true of like when

**[06:33]** prediction is coming true of like when you think the end of utterance will

**[06:34]** you think the end of utterance will

**[06:34]** you think the end of utterance will occur as you start getting closer to

**[06:36]** occur as you start getting closer to

**[06:36]** occur as you start getting closer to that you start refining that that

**[06:38]** that you start refining that that

**[06:38]** that you start refining that that endpoint prediction um based on both the

**[06:42]** endpoint prediction um based on both the

**[06:42]** endpoint prediction um based on both the semantics and the syntax. And then as

**[06:43]** semantics and the syntax. And then as

**[06:43]** semantics and the syntax. And then as you start getting really as the speaker

**[06:45]** you start getting really as the speaker

**[06:45]** you start getting really as the speaker starts getting really close to the end

**[06:46]** starts getting really close to the end

**[06:46]** starts getting really close to the end of turn the listener finalizes the

**[06:49]** of turn the listener finalizes the

**[06:49]** of turn the listener finalizes the prediction by using procity by using

**[06:52]** prediction by using procity by using

**[06:52]** prediction by using procity by using information around like the tone and

**[06:53]** information around like the tone and

**[06:53]** information around like the tone and other acoustic features. Um

**[06:57]** other acoustic features. Um

**[06:57]** other acoustic features. Um so it's three steps a semantic

**[06:58]** so it's three steps a semantic

**[06:58]** so it's three steps a semantic prediction a refinement and a finaliz uh


### [07:00 - 08:00]

**[07:01]** prediction a refinement and a finaliz uh

**[07:01]** prediction a refinement and a finaliz uh a finalization. And one of the things I

**[07:04]** a finalization. And one of the things I

**[07:04]** a finalization. And one of the things I want to point out is that the human mind

**[07:05]** want to point out is that the human mind

**[07:06]** want to point out is that the human mind is full duplex. We're both processing

**[07:07]** is full duplex. We're both processing

**[07:07]** is full duplex. We're both processing input and we're starting to generate

**[07:09]** input and we're starting to generate

**[07:09]** input and we're starting to generate output at the same time. And I think

**[07:11]** output at the same time. And I think

**[07:11]** output at the same time. And I think that's really nicely described in this

**[07:13]** that's really nicely described in this

**[07:13]** that's really nicely described in this figure from this paper. Um, and so on

**[07:16]** figure from this paper. Um, and so on

**[07:16]** figure from this paper. Um, and so on the x- axis, what we have here is time

**[07:18]** the x- axis, what we have here is time

**[07:18]** the x- axis, what we have here is time where the zero millisecond is the end of

**[07:21]** where the zero millisecond is the end of

**[07:21]** where the zero millisecond is the end of the speaker's turn. And what these

**[07:23]** the speaker's turn. And what these

**[07:24]** the speaker's turn. And what these different blocks represent is what of

**[07:25]** different blocks represent is what of

**[07:25]** different blocks represent is what of mental processes that are happening

**[07:27]** mental processes that are happening

**[07:27]** mental processes that are happening inside the mind of the listener. And you

**[07:29]** inside the mind of the listener. And you

**[07:29]** inside the mind of the listener. And you can see well before the end of the turn,

**[07:31]** can see well before the end of the turn,

**[07:31]** can see well before the end of the turn, there's this whole comprehension

**[07:33]** there's this whole comprehension

**[07:33]** there's this whole comprehension uh track um that's going on where the

**[07:36]** uh track um that's going on where the

**[07:36]** uh track um that's going on where the listener is inferring the intended

**[07:39]** listener is inferring the intended

**[07:39]** listener is inferring the intended message of the speaker and making

**[07:42]** message of the speaker and making

**[07:42]** message of the speaker and making predictions about when they're going to

**[07:43]** predictions about when they're going to

**[07:43]** predictions about when they're going to start finish speaking. And at the same

**[07:44]** start finish speaking. And at the same

**[07:44]** start finish speaking. And at the same time, there's also this production or

**[07:46]** time, there's also this production or

**[07:46]** time, there's also this production or generation track where the um the

**[07:49]** generation track where the um the

**[07:49]** generation track where the um the listener is starting to produce what

**[07:52]** listener is starting to produce what

**[07:52]** listener is starting to produce what they're going to say.

**[07:55]** they're going to say.

**[07:55]** they're going to say. And we're going to talk more about full

**[07:57]** And we're going to talk more about full

**[07:57]** And we're going to talk more about full duplex models in computer in silic

**[07:59]** duplex models in computer in silic

**[07:59]** duplex models in computer in silic rather than human minds in a little bit


### [08:00 - 09:00]

**[08:01]** rather than human minds in a little bit

**[08:01]** rather than human minds in a little bit in my presentation. Um, oh, Jordan

**[08:04]** in my presentation. Um, oh, Jordan

**[08:04]** in my presentation. Um, oh, Jordan Deersley just texted me.

**[08:07]** Deersley just texted me.

**[08:07]** Deersley just texted me. [Laughter]

**[08:10]** [Laughter]

**[08:10]** [Laughter] He texted boo. Like, how does he know to

**[08:12]** He texted boo. Like, how does he know to

**[08:12]** He texted boo. Like, how does he know to boo me? He's not even here. Um,

**[08:16]** boo me? He's not even here. Um,

**[08:16]** boo me? He's not even here. Um, okay. It's it's all good. We'll keep

**[08:18]** okay. It's it's all good. We'll keep

**[08:18]** okay. It's it's all good. We'll keep rolling. Uh so um so let's go back to uh

**[08:24]** rolling. Uh so um so let's go back to uh

**[08:24]** rolling. Uh so um so let's go back to uh um like let's contrast this really

**[08:26]** um like let's contrast this really

**[08:26]** um like let's contrast this really interesting complex process that's going

**[08:28]** interesting complex process that's going

**[08:28]** interesting complex process that's going on in the human mind compared to current

**[08:30]** on in the human mind compared to current

**[08:30]** on in the human mind compared to current voice AI systems. You'll see it's just

**[08:32]** voice AI systems. You'll see it's just

**[08:32]** voice AI systems. You'll see it's just so much more simple, right? It's just

**[08:34]** so much more simple, right? It's just

**[08:34]** so much more simple, right? It's just speech or not speech. It's looking

**[08:36]** speech or not speech. It's looking

**[08:36]** speech or not speech. It's looking backwards. It's not making a prediction.

**[08:38]** backwards. It's not making a prediction.

**[08:38]** backwards. It's not making a prediction. Um it's done in serial. Nothing's

**[08:40]** Um it's done in serial. Nothing's

**[08:40]** Um it's done in serial. Nothing's happening in parallel. Um so it's it's

**[08:42]** happening in parallel. Um so it's it's

**[08:42]** happening in parallel. Um so it's it's much more simple. And that's part part

**[08:46]** much more simple. And that's part part

**[08:46]** much more simple. And that's part part of the problem, right, of why these

**[08:47]** of the problem, right, of why these

**[08:47]** of the problem, right, of why these interruptions are happening. Um,

**[08:50]** interruptions are happening. Um,

**[08:50]** interruptions are happening. Um, so there's uh I'm going to talk through

**[08:53]** so there's uh I'm going to talk through

**[08:53]** so there's uh I'm going to talk through three types of models and the approaches

**[08:55]** three types of models and the approaches

**[08:55]** three types of models and the approaches people are using in these three types of

**[08:56]** people are using in these three types of

**[08:56]** people are using in these three types of models. Um, so the the prevailing model


### [09:00 - 10:00]

**[09:00]** models. Um, so the the prevailing model

**[09:00]** models. Um, so the the prevailing model for building voice AI agents is the

**[09:01]** for building voice AI agents is the

**[09:01]** for building voice AI agents is the cascading model system of models where

**[09:03]** cascading model system of models where

**[09:03]** cascading model system of models where you have um what we talked about

**[09:06]** you have um what we talked about

**[09:06]** you have um what we talked about earlier, speech to text, VA, LLM, TTS.

**[09:09]** earlier, speech to text, VA, LLM, TTS.

**[09:09]** earlier, speech to text, VA, LLM, TTS. And uh what we're doing in those is

**[09:11]** And uh what we're doing in those is

**[09:11]** And uh what we're doing in those is we're augmenting these new the new

**[09:13]** we're augmenting these new the new

**[09:13]** we're augmenting these new the new approaches to better handling

**[09:15]** approaches to better handling

**[09:15]** approaches to better handling interruptions is we're augmenting the

**[09:17]** interruptions is we're augmenting the

**[09:17]** interruptions is we're augmenting the VAD with models that look at the

**[09:19]** VAD with models that look at the

**[09:19]** VAD with models that look at the semantics syntax or procity. Um and

**[09:25]** semantics syntax or procity. Um and

**[09:25]** semantics syntax or procity. Um and uh I want to jump into an example of it.

**[09:28]** uh I want to jump into an example of it.

**[09:28]** uh I want to jump into an example of it. Um I really have too much content for uh

**[09:32]** Um I really have too much content for uh

**[09:32]** Um I really have too much content for uh for my aotted time that I'm looking at

**[09:34]** for my aotted time that I'm looking at

**[09:34]** for my aotted time that I'm looking at down here. Um but maybe I can just take

**[09:36]** down here. Um but maybe I can just take

**[09:36]** down here. Um but maybe I can just take some time from Jordan. Um, so, uh, let

**[09:40]** some time from Jordan. Um, so, uh, let

**[09:40]** some time from Jordan. Um, so, uh, let me let me, um, give an example for one

**[09:43]** me let me, um, give an example for one

**[09:43]** me let me, um, give an example for one of these semantic type models that is

**[09:45]** of these semantic type models that is

**[09:45]** of these semantic type models that is used to augment VAD. I'm going to talk

**[09:46]** used to augment VAD. I'm going to talk

**[09:46]** used to augment VAD. I'm going to talk about our model at LiveKit. It's a

**[09:49]** about our model at LiveKit. It's a

**[09:49]** about our model at LiveKit. It's a textbased semantic model. So, what we're

**[09:51]** textbased semantic model. So, what we're

**[09:51]** textbased semantic model. So, what we're doing is we're taking the last four

**[09:53]** doing is we're taking the last four

**[09:53]** doing is we're taking the last four turns of the conversation as input. So,

**[09:56]** turns of the conversation as input. So,

**[09:56]** turns of the conversation as input. So, that means that it's the uh, the voice

**[09:58]** that means that it's the uh, the voice

**[09:58]** that means that it's the uh, the voice AI agent's turn, then the user's turn,


### [10:00 - 11:00]

**[10:01]** AI agent's turn, then the user's turn,

**[10:01]** AI agent's turn, then the user's turn, then the voice AI agents turn, and then

**[10:03]** then the voice AI agents turn, and then

**[10:03]** then the voice AI agents turn, and then the user's current turn. Those are the

**[10:06]** the user's current turn. Those are the

**[10:06]** the user's current turn. Those are the inputs into to a transformer model and

**[10:08]** inputs into to a transformer model and

**[10:08]** inputs into to a transformer model and what we're the token that we're

**[10:10]** what we're the token that we're

**[10:10]** what we're the token that we're predicting um because this is an LLM

**[10:12]** predicting um because this is an LLM

**[10:12]** predicting um because this is an LLM we're predicting the end of utterance

**[10:14]** we're predicting the end of utterance

**[10:14]** we're predicting the end of utterance token and if that end of utterance token

**[10:16]** token and if that end of utterance token

**[10:16]** token and if that end of utterance token based on this the content right based on

**[10:18]** based on this the content right based on

**[10:18]** based on this the content right based on the the the context and the semantics of

**[10:21]** the the the context and the semantics of

**[10:21]** the the the context and the semantics of that that input um if the end of

**[10:24]** that that input um if the end of

**[10:24]** that that input um if the end of utterance token is saying that the end

**[10:26]** utterance token is saying that the end

**[10:26]** utterance token is saying that the end of turn it hasn't happened yet then we

**[10:30]** of turn it hasn't happened yet then we

**[10:30]** of turn it hasn't happened yet then we don't we extend the silence algorithm

**[10:33]** don't we extend the silence algorithm

**[10:33]** don't we extend the silence algorithm part of the that and say don't trigger

**[10:35]** part of the that and say don't trigger

**[10:35]** part of the that and say don't trigger the end of turn wait longer. Um, so they

**[10:38]** the end of turn wait longer. Um, so they

**[10:38]** the end of turn wait longer. Um, so they work in concert. That's generally the

**[10:40]** work in concert. That's generally the

**[10:40]** work in concert. That's generally the idea of how it works. I'm going to walk

**[10:42]** idea of how it works. I'm going to walk

**[10:42]** idea of how it works. I'm going to walk through a quick demo of of how this

**[10:44]** through a quick demo of of how this

**[10:44]** through a quick demo of of how this works in action. Needed to build a demo,

**[10:47]** works in action. Needed to build a demo,

**[10:47]** works in action. Needed to build a demo, but I wasn't.

**[10:49]** but I wasn't.

**[10:49]** but I wasn't. So, in this first part of this demo,

**[10:52]** So, in this first part of this demo,

**[10:52]** So, in this first part of this demo, what Shane is going to do is uh talk to

**[10:56]** what Shane is going to do is uh talk to

**[10:56]** what Shane is going to do is uh talk to a voice agent that is just using the the


### [11:00 - 12:00]

**[11:00]** a voice agent that is just using the the

**[11:00]** a voice agent that is just using the the traditional VAD that I was discussing

**[11:02]** traditional VAD that I was discussing

**[11:02]** traditional VAD that I was discussing earlier that just looks at speech or not

**[11:04]** earlier that just looks at speech or not

**[11:04]** earlier that just looks at speech or not speech. And the second half of the demo,

**[11:06]** speech. And the second half of the demo,

**[11:06]** speech. And the second half of the demo, he's using our semantic end of utterance

**[11:08]** he's using our semantic end of utterance

**[11:08]** he's using our semantic end of utterance model.

**[11:16]** 100% sure what it was that I should

**[11:16]** 100% sure what it was that I should I had to build a demo for.

**[11:20]** I had to build a demo for.

**[11:20]** I had to build a demo for. What was the a live kit? A live kit uh

**[11:24]** What was the a live kit? A live kit uh

**[11:24]** What was the a live kit? A live kit uh turn detection a turn detection demo

**[11:28]** turn detection a turn detection demo

**[11:28]** turn detection a turn detection demo where one of the agents

**[11:31]** where one of the agents

**[11:31]** where one of the agents like

**[11:33]** like

**[11:33]** like Got it. What challenges did you face

**[11:34]** Got it. What challenges did you face

**[11:34]** Got it. What challenges did you face while building that demo kept on

**[11:36]** while building that demo kept on

**[11:36]** while building that demo kept on interrupting me being interrupted by the

**[11:38]** interrupting me being interrupted by the

**[11:38]** interrupting me being interrupted by the agent constantly. That was the worst

**[11:40]** agent constantly. That was the worst

**[11:40]** agent constantly. That was the worst part for sure.

**[11:47]** I understand. How did you overcome that

**[11:47]** I understand. How did you overcome that challenge during the demo?

**[11:50]** challenge during the demo?

**[11:50]** challenge during the demo? Well, hopefully we're going to overcome

**[11:51]** Well, hopefully we're going to overcome

**[11:51]** Well, hopefully we're going to overcome the challenge by using the new turn

**[11:54]** the challenge by using the new turn

**[11:54]** the challenge by using the new turn detection model that LiveKit's offering.

**[11:56]** detection model that LiveKit's offering.

**[11:56]** detection model that LiveKit's offering. So, let's try that one now instead.


### [12:00 - 13:00]

**[12:06]** Hey, can you interview me about a time

**[12:06]** Hey, can you interview me about a time when I had to build a demo?

**[12:10]** when I had to build a demo?

**[12:10]** when I had to build a demo? Absolutely. Can you share your

**[12:11]** Absolutely. Can you share your

**[12:11]** Absolutely. Can you share your experience with building a demo?

**[12:14]** experience with building a demo?

**[12:14]** experience with building a demo? Yeah, definitely. So,

**[12:18]** Yeah, definitely. So,

**[12:18]** Yeah, definitely. So, I needed to build a demo, but I wasn't

**[12:23]** I needed to build a demo, but I wasn't

**[12:23]** I needed to build a demo, but I wasn't I wasn't a 100% sure what it was that I

**[12:26]** I wasn't a 100% sure what it was that I

**[12:26]** I wasn't a 100% sure what it was that I should build.

**[12:28]** should build.

**[12:28]** should build. And then I

**[12:32]** And then I

**[12:32]** And then I I was thinking like probably the best

**[12:34]** I was thinking like probably the best

**[12:34]** I was thinking like probably the best way to show that would be uh

**[12:38]** way to show that would be uh

**[12:38]** way to show that would be uh would be side by side.

**[12:42]** would be side by side.

**[12:42]** would be side by side. Yeah, thank you. I'll I'll let I'll let

**[12:45]** Yeah, thank you. I'll I'll let I'll let

**[12:45]** Yeah, thank you. I'll I'll let I'll let Shane know that you all applauded his

**[12:47]** Shane know that you all applauded his

**[12:47]** Shane know that you all applauded his demo. Uh he'll appreciate that. Yeah,

**[12:48]** demo. Uh he'll appreciate that. Yeah,

**[12:48]** demo. Uh he'll appreciate that. Yeah, you can really see it's a night and day

**[12:50]** you can really see it's a night and day

**[12:50]** you can really see it's a night and day difference when you augment the VAD with

**[12:52]** difference when you augment the VAD with

**[12:52]** difference when you augment the VAD with models that look at the semantics and

**[12:53]** models that look at the semantics and

**[12:53]** models that look at the semantics and syntax and procity. um which is a good

**[12:56]** syntax and procity. um which is a good

**[12:56]** syntax and procity. um which is a good segue to my next slide. So there's

**[12:59]** segue to my next slide. So there's

**[12:59]** segue to my next slide. So there's another type of another approach people


### [13:00 - 14:00]

**[13:01]** another type of another approach people

**[13:01]** another type of another approach people are taking to augmenting the VAD and

**[13:04]** are taking to augmenting the VAD and

**[13:04]** are taking to augmenting the VAD and what they're doing is not just taking

**[13:05]** what they're doing is not just taking

**[13:05]** what they're doing is not just taking the semantic input the textbased input

**[13:07]** the semantic input the textbased input

**[13:07]** the semantic input the textbased input but they're also looking at the audio

**[13:09]** but they're also looking at the audio

**[13:09]** but they're also looking at the audio signal as well and trying to infer

**[13:11]** signal as well and trying to infer

**[13:11]** signal as well and trying to infer things from the acoustic features of the

**[13:12]** things from the acoustic features of the

**[13:12]** things from the acoustic features of the the dialogue. So they're taking the

**[13:14]** the dialogue. So they're taking the

**[13:14]** the dialogue. So they're taking the basic idea is the input is audio tokens

**[13:16]** basic idea is the input is audio tokens

**[13:16]** basic idea is the input is audio tokens and the output is the probability that

**[13:19]** and the output is the probability that

**[13:19]** and the output is the probability that the user has finished speaking. Um Quinn

**[13:21]** the user has finished speaking. Um Quinn

**[13:21]** the user has finished speaking. Um Quinn and the Daily team have built their also

**[13:24]** and the Daily team have built their also

**[13:24]** and the Daily team have built their also openweight smart turn model that that uh

**[13:27]** openweight smart turn model that that uh

**[13:27]** openweight smart turn model that that uh is this neat combination of a model that

**[13:29]** is this neat combination of a model that

**[13:29]** is this neat combination of a model that is both transformer and looking at

**[13:30]** is both transformer and looking at

**[13:30]** is both transformer and looking at acoustic um characteristics. Um, and

**[13:33]** acoustic um characteristics. Um, and

**[13:33]** acoustic um characteristics. Um, and then one of the new things that has just

**[13:35]** then one of the new things that has just

**[13:35]** then one of the new things that has just emerged has been um, Assembly AI dropped

**[13:38]** emerged has been um, Assembly AI dropped

**[13:38]** emerged has been um, Assembly AI dropped their their speechto text new streaming

**[13:41]** their their speechto text new streaming

**[13:41]** their their speechto text new streaming speech to text service earlier this

**[13:43]** speech to text service earlier this

**[13:43]** speech to text service earlier this week. And their model is really neat in

**[13:46]** week. And their model is really neat in

**[13:46]** week. And their model is really neat in that it emits it takes audio in and

**[13:48]** that it emits it takes audio in and

**[13:48]** that it emits it takes audio in and emits out both the transcript and a

**[13:52]** emits out both the transcript and a

**[13:52]** emits out both the transcript and a likelihood that uh, the speaker is

**[13:54]** likelihood that uh, the speaker is

**[13:54]** likelihood that uh, the speaker is finished speaking. Um, so it's one model

**[13:56]** finished speaking. Um, so it's one model

**[13:56]** finished speaking. Um, so it's one model that's kind of doing both these two

**[13:58]** that's kind of doing both these two

**[13:58]** that's kind of doing both these two things at the same time. Um, and it's


### [14:00 - 15:00]

**[14:00]** things at the same time. Um, and it's

**[14:00]** things at the same time. Um, and it's also looking at the acoustic features

**[14:02]** also looking at the acoustic features

**[14:02]** also looking at the acoustic features and the semantic features. One of the

**[14:03]** and the semantic features. One of the

**[14:03]** and the semantic features. One of the things I want QAI also has one that they

**[14:05]** things I want QAI also has one that they

**[14:05]** things I want QAI also has one that they recently released that's pretty neat.

**[14:07]** recently released that's pretty neat.

**[14:07]** recently released that's pretty neat. Um, one of the things I want to note

**[14:09]** Um, one of the things I want to note

**[14:09]** Um, one of the things I want to note about this though is if you're using

**[14:10]** about this though is if you're using

**[14:10]** about this though is if you're using your speechto texts builtin end of

**[14:13]** your speechto texts builtin end of

**[14:13]** your speechto texts builtin end of utterance model, it's only seeing half

**[14:14]** utterance model, it's only seeing half

**[14:14]** utterance model, it's only seeing half the context. It's only seeing what the

**[14:16]** the context. It's only seeing what the

**[14:16]** the context. It's only seeing what the user is saying. It's not also seeing

**[14:18]** user is saying. It's not also seeing

**[14:18]** user is saying. It's not also seeing what the agent is saying. So, it doesn't

**[14:20]** what the agent is saying. So, it doesn't

**[14:20]** what the agent is saying. So, it doesn't quite have the full picture on the

**[14:21]** quite have the full picture on the

**[14:21]** quite have the full picture on the context. Um, but it works remarkably

**[14:24]** context. Um, but it works remarkably

**[14:24]** context. Um, but it works remarkably well. All these approaches work

**[14:26]** well. All these approaches work

**[14:26]** well. All these approaches work remarkably well and are a major step

**[14:28]** remarkably well and are a major step

**[14:28]** remarkably well and are a major step forward from these more traditional VADs

**[14:31]** forward from these more traditional VADs

**[14:31]** forward from these more traditional VADs and like definitely something that if

**[14:32]** and like definitely something that if

**[14:32]** and like definitely something that if you're building a voice AI agent after

**[14:34]** you're building a voice AI agent after

**[14:34]** you're building a voice AI agent after this conference you should go like

**[14:36]** this conference you should go like

**[14:36]** this conference you should go like implement it. They're pretty easy to

**[14:37]** implement it. They're pretty easy to

**[14:37]** implement it. They're pretty easy to implement on the different platforms

**[14:38]** implement on the different platforms

**[14:38]** implement on the different platforms too.

**[14:40]** too.

**[14:40]** too. Um

**[14:41]** Um

**[14:41]** Um okay. So we often talk about in uh uh

**[14:45]** okay. So we often talk about in uh uh

**[14:45]** okay. So we often talk about in uh uh speech models or in voice AI that um

**[14:48]** speech models or in voice AI that um

**[14:48]** speech models or in voice AI that um speech models are uh are going to save

**[14:51]** speech models are uh are going to save

**[14:51]** speech models are uh are going to save us. Um speechto speech models audio in

**[14:54]** us. Um speechto speech models audio in

**[14:54]** us. Um speechto speech models audio in and audio out are going to save us. Um

**[14:56]** and audio out are going to save us. Um

**[14:56]** and audio out are going to save us. Um but actually if you look at how these

**[14:58]** but actually if you look at how these

**[14:58]** but actually if you look at how these models work that like OpenAI's real-time


### [15:00 - 16:00]

**[15:00]** models work that like OpenAI's real-time

**[15:00]** models work that like OpenAI's real-time API, they're still using a VAD on the on

**[15:04]** API, they're still using a VAD on the on

**[15:04]** API, they're still using a VAD on the on the internals. Um, so they're still just

**[15:06]** the internals. Um, so they're still just

**[15:06]** the internals. Um, so they're still just looking at speech or not speech. Or you

**[15:09]** looking at speech or not speech. Or you

**[15:09]** looking at speech or not speech. Or you can you can opt to turn on their

**[15:10]** can you can opt to turn on their

**[15:10]** can you can opt to turn on their semantic, they call it semantic VAD,

**[15:13]** semantic, they call it semantic VAD,

**[15:13]** semantic, they call it semantic VAD, which is kind of a paradox. It's not the

**[15:16]** which is kind of a paradox. It's not the

**[15:16]** which is kind of a paradox. It's not the best term, but turning on a semantic

**[15:17]** best term, but turning on a semantic

**[15:17]** best term, but turning on a semantic model that augments the bad. Um, so to

**[15:19]** model that augments the bad. Um, so to

**[15:19]** model that augments the bad. Um, so to answer the title of my talk of why chat

**[15:21]** answer the title of my talk of why chat

**[15:21]** answer the title of my talk of why chat GPT advanced voice mode keeps

**[15:23]** GPT advanced voice mode keeps

**[15:23]** GPT advanced voice mode keeps interrupting you, it's because it thinks

**[15:25]** interrupting you, it's because it thinks

**[15:25]** interrupting you, it's because it thinks you're done speaking based on how long

**[15:26]** you're done speaking based on how long

**[15:26]** you're done speaking based on how long it's been since you last said a word,

**[15:28]** it's been since you last said a word,

**[15:28]** it's been since you last said a word, um, or based on what you've uh what

**[15:30]** um, or based on what you've uh what

**[15:30]** um, or based on what you've uh what you've said previously. Um, and it's

**[15:33]** you've said previously. Um, and it's

**[15:33]** you've said previously. Um, and it's just not quite cutting it. um when those

**[15:35]** just not quite cutting it. um when those

**[15:35]** just not quite cutting it. um when those interruptions happen um uh and it's a

**[15:38]** interruptions happen um uh and it's a

**[15:38]** interruptions happen um uh and it's a problem that is not totally solved. I

**[15:40]** problem that is not totally solved. I

**[15:40]** problem that is not totally solved. I want to also bring that up too that like

**[15:43]** want to also bring that up too that like

**[15:43]** want to also bring that up too that like this is an ongoing problem um with all

**[15:45]** this is an ongoing problem um with all

**[15:45]** this is an ongoing problem um with all the different approaches nothing has

**[15:46]** the different approaches nothing has

**[15:46]** the different approaches nothing has perfected it yet. Um our end of live kit

**[15:50]** perfected it yet. Um our end of live kit

**[15:50]** perfected it yet. Um our end of live kit doesn't although we power the transport

**[15:52]** doesn't although we power the transport

**[15:52]** doesn't although we power the transport the audio layer transport for uh

**[15:55]** the audio layer transport for uh

**[15:55]** the audio layer transport for uh advanced voice mode um openai is not

**[15:58]** advanced voice mode um openai is not

**[15:58]** advanced voice mode um openai is not using our end of utterance model. So the


### [16:00 - 17:00]

**[16:00]** using our end of utterance model. So the

**[16:00]** using our end of utterance model. So the next topic I want to cover is the um uh

**[16:04]** next topic I want to cover is the um uh

**[16:04]** next topic I want to cover is the um uh I'm running out of time here but uh is

**[16:06]** I'm running out of time here but uh is

**[16:06]** I'm running out of time here but uh is full duplex models. These are really

**[16:08]** full duplex models. These are really

**[16:08]** full duplex models. These are really neat. So a full duplex model is more

**[16:09]** neat. So a full duplex model is more

**[16:10]** neat. So a full duplex model is more like a human mind and it's processing

**[16:11]** like a human mind and it's processing

**[16:11]** like a human mind and it's processing input and generating speech at the same

**[16:13]** input and generating speech at the same

**[16:13]** input and generating speech at the same time. Um and as far as I know there's

**[16:16]** time. Um and as far as I know there's

**[16:16]** time. Um and as far as I know there's not really any commercial applications

**[16:18]** not really any commercial applications

**[16:18]** not really any commercial applications of these. Um but they're they're

**[16:20]** of these. Um but they're they're

**[16:20]** of these. Um but they're they're fundamentally they're intuitive talkers.

**[16:22]** fundamentally they're intuitive talkers.

**[16:22]** fundamentally they're intuitive talkers. They're trained on the raw audio data.

**[16:23]** They're trained on the raw audio data.

**[16:24]** They're trained on the raw audio data. And the analogy I like to use is that

**[16:26]** And the analogy I like to use is that

**[16:26]** And the analogy I like to use is that it's like computer vision. In the early

**[16:27]** it's like computer vision. In the early

**[16:27]** it's like computer vision. In the early days of computer vision, we were

**[16:29]** days of computer vision, we were

**[16:29]** days of computer vision, we were handwriting algorithms to try to

**[16:31]** handwriting algorithms to try to

**[16:31]** handwriting algorithms to try to recognize the stop sign based on the

**[16:32]** recognize the stop sign based on the

**[16:32]** recognize the stop sign based on the color and the number of sides on it,

**[16:34]** color and the number of sides on it,

**[16:34]** color and the number of sides on it, etc. Um, and it just didn't work very

**[16:37]** etc. Um, and it just didn't work very

**[16:37]** etc. Um, and it just didn't work very well. But when we started giving the raw

**[16:38]** well. But when we started giving the raw

**[16:38]** well. But when we started giving the raw image data to the neural network and let

**[16:40]** image data to the neural network and let

**[16:40]** image data to the neural network and let the neural network figure it out, all a

**[16:42]** the neural network figure it out, all a

**[16:42]** the neural network figure it out, all a sudden it just started working. And I

**[16:44]** sudden it just started working. And I

**[16:44]** sudden it just started working. And I think it's a and actually that uh what

**[16:47]** think it's a and actually that uh what

**[16:47]** think it's a and actually that uh what we learned from computer vision that

**[16:48]** we learned from computer vision that

**[16:48]** we learned from computer vision that really helped us emerge from the AI

**[16:49]** really helped us emerge from the AI

**[16:50]** really helped us emerge from the AI winter. That was a major kind of uh

**[16:52]** winter. That was a major kind of uh

**[16:52]** winter. That was a major kind of uh seeding process for where we are now

**[16:53]** seeding process for where we are now

**[16:53]** seeding process for where we are now with AI. Um, and it's a similar analogy

**[16:56]** with AI. Um, and it's a similar analogy

**[16:56]** with AI. Um, and it's a similar analogy with full duplex models in that we're

**[16:58]** with full duplex models in that we're

**[16:58]** with full duplex models in that we're handing them the raw audio data and

**[16:59]** handing them the raw audio data and

**[16:59]** handing them the raw audio data and we're just letting them figure out how


### [17:00 - 18:00]

**[17:00]** we're just letting them figure out how

**[17:00]** we're just letting them figure out how turn taking works rather than trying to

**[17:02]** turn taking works rather than trying to

**[17:02]** turn taking works rather than trying to handw write all the rules. Um, but the

**[17:05]** handw write all the rules. Um, but the

**[17:05]** handw write all the rules. Um, but the downside of these models is they're

**[17:06]** downside of these models is they're

**[17:06]** downside of these models is they're really optimized for like being really

**[17:08]** really optimized for like being really

**[17:08]** really optimized for like being really good at turn taking and they're kind of

**[17:10]** good at turn taking and they're kind of

**[17:10]** good at turn taking and they're kind of dumb LLMs. They're small models. They're

**[17:12]** dumb LLMs. They're small models. They're

**[17:12]** dumb LLMs. They're small models. They're not trained on a lot of data. They can't

**[17:13]** not trained on a lot of data. They can't

**[17:13]** not trained on a lot of data. They can't do instruction following very well. Um,

**[17:16]** do instruction following very well. Um,

**[17:16]** do instruction following very well. Um, and just to give you a sense of like

**[17:17]** and just to give you a sense of like

**[17:17]** and just to give you a sense of like more specifics of how these models work,

**[17:19]** more specifics of how these models work,

**[17:19]** more specifics of how these models work, let's talk about the Moshi model. Um,

**[17:22]** let's talk about the Moshi model. Um,

**[17:22]** let's talk about the Moshi model. Um, what really made it more concrete for me

**[17:23]** what really made it more concrete for me

**[17:23]** what really made it more concrete for me of how this model works is this idea

**[17:25]** of how this model works is this idea

**[17:26]** of how this model works is this idea that is always listening to input and

**[17:28]** that is always listening to input and

**[17:28]** that is always listening to input and it's always generating output and even

**[17:31]** it's always generating output and even

**[17:31]** it's always generating output and even when it's not its turn to speak, it's

**[17:32]** when it's not its turn to speak, it's

**[17:32]** when it's not its turn to speak, it's emitting natural silence. So, it's just

**[17:34]** emitting natural silence. So, it's just

**[17:34]** emitting natural silence. So, it's just basically emitting silence that you

**[17:35]** basically emitting silence that you

**[17:36]** basically emitting silence that you can't hear, but it's still always

**[17:37]** can't hear, but it's still always

**[17:37]** can't hear, but it's still always emitting silence. Um, so it's always

**[17:39]** emitting silence. Um, so it's always

**[17:39]** emitting silence. Um, so it's always kind of doing both just like a human is.

**[17:41]** kind of doing both just like a human is.

**[17:41]** kind of doing both just like a human is. Um, Sync LLM, which is Meta AI's uh,

**[17:45]** Um, Sync LLM, which is Meta AI's uh,

**[17:45]** Um, Sync LLM, which is Meta AI's uh, full duplex like experimental mode that

**[17:47]** full duplex like experimental mode that

**[17:47]** full duplex like experimental mode that you can access inside the app, um, is a

**[17:50]** you can access inside the app, um, is a

**[17:50]** you can access inside the app, um, is a similar full duplex model or it's also

**[17:53]** similar full duplex model or it's also

**[17:53]** similar full duplex model or it's also full duplex model. Something neat that I

**[17:55]** full duplex model. Something neat that I

**[17:55]** full duplex model. Something neat that I want to bring up about Sync LLM is

**[17:57]** want to bring up about Sync LLM is

**[17:57]** want to bring up about Sync LLM is they're actually in the internals of

**[17:59]** they're actually in the internals of

**[17:59]** they're actually in the internals of that model, they're forecasting what the


### [18:00 - 19:00]

**[18:00]** that model, they're forecasting what the

**[18:00]** that model, they're forecasting what the user said saying about five tokens ahead

**[18:02]** user said saying about five tokens ahead

**[18:02]** user said saying about five tokens ahead or 200 milliseconds ahead, which is more

**[18:05]** or 200 milliseconds ahead, which is more

**[18:05]** or 200 milliseconds ahead, which is more closely like what humans are doing

**[18:08]** closely like what humans are doing

**[18:08]** closely like what humans are doing except we're uh forecasting a much

**[18:10]** except we're uh forecasting a much

**[18:10]** except we're uh forecasting a much longer time frame. And then lastly, my

**[18:13]** longer time frame. And then lastly, my

**[18:13]** longer time frame. And then lastly, my predictions for the future of how we'll

**[18:14]** predictions for the future of how we'll

**[18:14]** predictions for the future of how we'll solve this problem uh is

**[18:17]** solve this problem uh is

**[18:17]** solve this problem uh is I think full duplex models are neat, but

**[18:19]** I think full duplex models are neat, but

**[18:19]** I think full duplex models are neat, but I don't think they're going to solve the

**[18:20]** I don't think they're going to solve the

**[18:20]** I don't think they're going to solve the problem. Like I think we just for for

**[18:23]** problem. Like I think we just for for

**[18:23]** problem. Like I think we just for for real production commercial use cases of

**[18:25]** real production commercial use cases of

**[18:25]** real production commercial use cases of voice AI, we need more control. Um and

**[18:27]** voice AI, we need more control. Um and

**[18:27]** voice AI, we need more control. Um and we need more control over how it says

**[18:29]** we need more control over how it says

**[18:29]** we need more control over how it says things like brand names. Um and instead

**[18:32]** things like brand names. Um and instead

**[18:32]** things like brand names. Um and instead what I think is going to happen is we're

**[18:33]** what I think is going to happen is we're

**[18:33]** what I think is going to happen is we're going to get smarter and smarter VAD

**[18:34]** going to get smarter and smarter VAD

**[18:34]** going to get smarter and smarter VAD augmentations and faster and faster

**[18:36]** augmentations and faster and faster

**[18:36]** augmentations and faster and faster models in the cascade pipeline. And

**[18:38]** models in the cascade pipeline. And

**[18:38]** models in the cascade pipeline. And we're just going to have more budget to

**[18:40]** we're just going to have more budget to

**[18:40]** we're just going to have more budget to work with to do a good job with this

**[18:41]** work with to do a good job with this

**[18:42]** work with to do a good job with this sort of thing. Um and the reason I think

**[18:45]** sort of thing. Um and the reason I think

**[18:45]** sort of thing. Um and the reason I think that's true is like computers don't do

**[18:47]** that's true is like computers don't do

**[18:47]** that's true is like computers don't do math the same way humans do. They don't

**[18:49]** math the same way humans do. They don't

**[18:49]** math the same way humans do. They don't have the same conceptual way of thinking

**[18:50]** have the same conceptual way of thinking

**[18:50]** have the same conceptual way of thinking about it. And uh LLMs think differently

**[18:53]** about it. And uh LLMs think differently

**[18:53]** about it. And uh LLMs think differently than us. And similarly, I wouldn't

**[18:54]** than us. And similarly, I wouldn't

**[18:54]** than us. And similarly, I wouldn't expect voice AI to use the same

**[18:56]** expect voice AI to use the same

**[18:56]** expect voice AI to use the same mechanisms as the human mind to generate

**[18:58]** mechanisms as the human mind to generate

**[18:58]** mechanisms as the human mind to generate speech and to talk. Um thank you all for


### [19:00 - 20:00]

**[19:02]** speech and to talk. Um thank you all for

**[19:02]** speech and to talk. Um thank you all for your attention. This was fun. Really

**[19:04]** your attention. This was fun. Really

**[19:04]** your attention. This was fun. Really appreciate it.

**[19:07]** appreciate it.

**[19:07]** appreciate it. We do have some time. So I don't know if

**[19:09]** We do have some time. So I don't know if

**[19:09]** We do have some time. So I don't know if you want to take Q&A. Um I would love

**[19:13]** you want to take Q&A. Um I would love

**[19:13]** you want to take Q&A. Um I would love to. We could do that. Um and I could

**[19:15]** to. We could do that. Um and I could

**[19:15]** to. We could do that. Um and I could start with the first question.

**[19:18]** start with the first question.

**[19:18]** start with the first question. So, the demo you showed there there

**[19:20]** So, the demo you showed there there

**[19:20]** So, the demo you showed there there wasn't any response at the end, right? I

**[19:24]** wasn't any response at the end, right? I

**[19:24]** wasn't any response at the end, right? I I cut off the demo. It's actually a

**[19:25]** I cut off the demo. It's actually a

**[19:25]** I cut off the demo. It's actually a two-minute demo and I only have 18

**[19:27]** two-minute demo and I only have 18

**[19:27]** two-minute demo and I only have 18 minutes to speak. So, I truncated on

**[19:29]** minutes to speak. So, I truncated on

**[19:29]** minutes to speak. So, I truncated on both sides. Do because I was like,

**[19:31]** both sides. Do because I was like,

**[19:31]** both sides. Do because I was like, "Okay, maybe you just turned everything

**[19:33]** "Okay, maybe you just turned everything

**[19:33]** "Okay, maybe you just turned everything off and it was an impressive demo. No

**[19:35]** off and it was an impressive demo. No

**[19:35]** off and it was an impressive demo. No interruptions. No speaking." Yeah. Do

**[19:38]** interruptions. No speaking." Yeah. Do

**[19:38]** interruptions. No speaking." Yeah. Do you have the end of the demo? Do you

**[19:39]** you have the end of the demo? Do you

**[19:39]** you have the end of the demo? Do you want to show it or um No, no worries.

**[19:43]** want to show it or um No, no worries.

**[19:43]** want to show it or um No, no worries. It's more of the same idea. But like

**[19:44]** It's more of the same idea. But like

**[19:44]** It's more of the same idea. But like what you could see is that Shane was

**[19:46]** what you could see is that Shane was

**[19:46]** what you could see is that Shane was like, you know, taking his time talking

**[19:47]** like, you know, taking his time talking

**[19:48]** like, you know, taking his time talking and really pausing and thinking, it

**[19:49]** and really pausing and thinking, it

**[19:49]** and really pausing and thinking, it wasn't interrupting him and then when it

**[19:52]** wasn't interrupting him and then when it

**[19:52]** wasn't interrupting him and then when it eventually would find his end of turn

**[19:53]** eventually would find his end of turn

**[19:53]** eventually would find his end of turn based on the context. Cool. Can we find

**[19:55]** based on the context. Cool. Can we find

**[19:55]** based on the context. Cool. Can we find it on your Twitter or Yeah, it's it's on

**[19:58]** it on your Twitter or Yeah, it's it's on

**[19:58]** it on your Twitter or Yeah, it's it's on our link our live kit Twitter. Awesome.


### [20:00 - 21:00]

**[20:00]** our link our live kit Twitter. Awesome.

**[20:00]** our link our live kit Twitter. Awesome. Yeah. So, we can look that up on the

**[20:01]** Yeah. So, we can look that up on the

**[20:02]** Yeah. So, we can look that up on the live kit Twitter. Uh, awesome. Yeah, we

**[20:03]** live kit Twitter. Uh, awesome. Yeah, we

**[20:03]** live kit Twitter. Uh, awesome. Yeah, we can take some questions. I saw you had

**[20:05]** can take some questions. I saw you had

**[20:06]** can take some questions. I saw you had one.

**[20:08]** one.

**[20:08]** one. Hi. How important are visual cues for

**[20:12]** Hi. How important are visual cues for

**[20:12]** Hi. How important are visual cues for turn detection in in the human context?

**[20:14]** turn detection in in the human context?

**[20:14]** turn detection in in the human context? And are there any um is there any

**[20:17]** And are there any um is there any

**[20:17]** And are there any um is there any development to kind of replicate that in

**[20:20]** development to kind of replicate that in

**[20:20]** development to kind of replicate that in the uh voice AI context as well? Yeah,

**[20:23]** the uh voice AI context as well? Yeah,

**[20:23]** the uh voice AI context as well? Yeah, it's a really neat question of like how

**[20:25]** it's a really neat question of like how

**[20:25]** it's a really neat question of like how important are visual cues and are are

**[20:26]** important are visual cues and are are

**[20:26]** important are visual cues and are are people working on integrating that into

**[20:29]** people working on integrating that into

**[20:29]** people working on integrating that into the turn taking um intelligence for uh

**[20:34]** the turn taking um intelligence for uh

**[20:34]** the turn taking um intelligence for uh avatars and real-time experiences. So

**[20:36]** avatars and real-time experiences. So

**[20:36]** avatars and real-time experiences. So visual cues are actually despite the

**[20:38]** visual cues are actually despite the

**[20:38]** visual cues are actually despite the fact that we are visual animals um very

**[20:41]** fact that we are visual animals um very

**[20:41]** fact that we are visual animals um very very much so like visual is the most

**[20:43]** very much so like visual is the most

**[20:43]** very much so like visual is the most visceral like you know input for us

**[20:47]** visceral like you know input for us

**[20:47]** visceral like you know input for us visual cues are actually pretty low down

**[20:48]** visual cues are actually pretty low down

**[20:48]** visual cues are actually pretty low down the stack of like uh predictors for when

**[20:51]** the stack of like uh predictors for when

**[20:51]** the stack of like uh predictors for when it will be end of turn it really is

**[20:53]** it will be end of turn it really is

**[20:53]** it will be end of turn it really is semantics that's like one of the main

**[20:55]** semantics that's like one of the main

**[20:55]** semantics that's like one of the main messages that I want to convey to people

**[20:57]** messages that I want to convey to people

**[20:57]** messages that I want to convey to people from this talk is it's the content of

**[20:58]** from this talk is it's the content of

**[20:58]** from this talk is it's the content of what people are saying is the main thing


### [21:00 - 22:00]

**[21:00]** what people are saying is the main thing

**[21:00]** what people are saying is the main thing we're using to predict when they're

**[21:02]** we're using to predict when they're

**[21:02]** we're using to predict when they're going to finish speaking. Um, and then

**[21:03]** going to finish speaking. Um, and then

**[21:03]** going to finish speaking. Um, and then these visual cues are are and these

**[21:06]** these visual cues are are and these

**[21:06]** these visual cues are are and these other ones are ancillary to it. Um, and

**[21:08]** other ones are ancillary to it. Um, and

**[21:08]** other ones are ancillary to it. Um, and I'm sure somebody's working on building

**[21:09]** I'm sure somebody's working on building

**[21:10]** I'm sure somebody's working on building something really cool where it's like

**[21:11]** something really cool where it's like

**[21:11]** something really cool where it's like multimodal and looking at visual cues to

**[21:13]** multimodal and looking at visual cues to

**[21:13]** multimodal and looking at visual cues to look at the to infer the end of turn.

**[21:15]** look at the to infer the end of turn.

**[21:15]** look at the to infer the end of turn. Um, I'm just haven't seen it yet and

**[21:17]** Um, I'm just haven't seen it yet and

**[21:17]** Um, I'm just haven't seen it yet and can't keep up with all the AI stuff on

**[21:19]** can't keep up with all the AI stuff on

**[21:19]** can't keep up with all the AI stuff on the internet. Yes.

**[21:22]** the internet. Yes.

**[21:22]** the internet. Yes. What is the average cost?

**[21:26]** What is the average cost?

**[21:26]** What is the average cost? What is the average cost for usually

**[21:30]** What is the average cost for usually

**[21:30]** What is the average cost for usually voice uh generated call and then how is

**[21:34]** voice uh generated call and then how is

**[21:34]** voice uh generated call and then how is what is the effect when you try to keep

**[21:36]** what is the effect when you try to keep

**[21:36]** what is the effect when you try to keep regenerating the response?

**[21:42]** So the question is what's the average

**[21:42]** So the question is what's the average cost for voice AI call? Um and what is

**[21:46]** cost for voice AI call? Um and what is

**[21:46]** cost for voice AI call? Um and what is the cost when you keep trying to

**[21:48]** the cost when you keep trying to

**[21:48]** the cost when you keep trying to regenerate the the response? Um, so I

**[21:53]** regenerate the the response? Um, so I

**[21:53]** regenerate the the response? Um, so I would I would first say that the I think

**[21:56]** would I would first say that the I think

**[21:56]** would I would first say that the I think your your reference to what does it cost

**[21:57]** your your reference to what does it cost

**[21:57]** your your reference to what does it cost to keep trying to regenerate the

**[21:59]** to keep trying to regenerate the

**[21:59]** to keep trying to regenerate the response is um


### [22:00 - 23:00]

**[22:02]** response is um

**[22:02]** response is um what I the way I want to answer that is

**[22:03]** what I the way I want to answer that is

**[22:03]** what I the way I want to answer that is actually the thing that's most expensive

**[22:05]** actually the thing that's most expensive

**[22:05]** actually the thing that's most expensive in the pipeline tends to be the text to

**[22:06]** in the pipeline tends to be the text to

**[22:06]** in the pipeline tends to be the text to speech. So there's all these

**[22:08]** speech. So there's all these

**[22:08]** speech. So there's all these optimizations you can do in the cascade

**[22:09]** optimizations you can do in the cascade

**[22:10]** optimizations you can do in the cascade and if you end up hitting the LLM

**[22:11]** and if you end up hitting the LLM

**[22:11]** and if you end up hitting the LLM multiple times within a turn, it's not

**[22:13]** multiple times within a turn, it's not

**[22:13]** multiple times within a turn, it's not it's not all that costly and those sorts

**[22:16]** it's not all that costly and those sorts

**[22:16]** it's not all that costly and those sorts of things. Um, there's some really neat

**[22:18]** of things. Um, there's some really neat

**[22:18]** of things. Um, there's some really neat calculators online because I'm

**[22:20]** calculators online because I'm

**[22:20]** calculators online because I'm personally not a VoiceAI agent builder

**[22:22]** personally not a VoiceAI agent builder

**[22:22]** personally not a VoiceAI agent builder and those unit economics don't uh don't

**[22:25]** and those unit economics don't uh don't

**[22:25]** and those unit economics don't uh don't directly affect me. I don't have the

**[22:27]** directly affect me. I don't have the

**[22:27]** directly affect me. I don't have the numbers off the top of my head, but

**[22:28]** numbers off the top of my head, but

**[22:28]** numbers off the top of my head, but there's some really nice calculators.

**[22:29]** there's some really nice calculators.

**[22:29]** there's some really nice calculators. It's going to depend on how long the

**[22:30]** It's going to depend on how long the

**[22:30]** It's going to depend on how long the conversation is and that sort of thing.

**[22:41]** Yeah, thanks for the demo. That was

**[22:41]** Yeah, thanks for the demo. That was great. Uh the question is about your new

**[22:44]** great. Uh the question is about your new

**[22:44]** great. Uh the question is about your new model that you just shown and that blew

**[22:46]** model that you just shown and that blew

**[22:46]** model that you just shown and that blew us away. So uh one is like why is chat

**[22:49]** us away. So uh one is like why is chat

**[22:49]** us away. So uh one is like why is chat GPT not using that model to improve

**[22:52]** GPT not using that model to improve

**[22:52]** GPT not using that model to improve their stuff and two is it available for

**[22:54]** their stuff and two is it available for

**[22:54]** their stuff and two is it available for us to use now if I were to build a uh

**[22:57]** us to use now if I were to build a uh

**[22:57]** us to use now if I were to build a uh voice bot on live kit and uh three maybe


### [23:00 - 24:00]

**[23:02]** voice bot on live kit and uh three maybe

**[23:02]** voice bot on live kit and uh three maybe during your development of that one demo

**[23:05]** during your development of that one demo

**[23:05]** during your development of that one demo is great. uh do you also do some kind of

**[23:07]** is great. uh do you also do some kind of

**[23:07]** is great. uh do you also do some kind of benchmarking with user to see if you

**[23:10]** benchmarking with user to see if you

**[23:10]** benchmarking with user to see if you know this is like 50% better or

**[23:12]** know this is like 50% better or

**[23:12]** know this is like 50% better or something like that?

**[23:14]** something like that?

**[23:14]** something like that? Yes. So the first question is about why

**[23:17]** Yes. So the first question is about why

**[23:17]** Yes. So the first question is about why isn't open AAI using our end of

**[23:19]** isn't open AAI using our end of

**[23:19]** isn't open AAI using our end of utterance model. I don't know why

**[23:21]** utterance model. I don't know why

**[23:21]** utterance model. I don't know why they're not. I think that's maybe above

**[23:23]** they're not. I think that's maybe above

**[23:23]** they're not. I think that's maybe above my pay grade of this company I just

**[23:25]** my pay grade of this company I just

**[23:25]** my pay grade of this company I just joined four weeks ago. Um

**[23:28]** joined four weeks ago. Um

**[23:28]** joined four weeks ago. Um and the the second question is like can

**[23:31]** and the the second question is like can

**[23:31]** and the the second question is like can you is our end of utterance model

**[23:33]** you is our end of utterance model

**[23:33]** you is our end of utterance model available um for use and so it's really

**[23:37]** available um for use and so it's really

**[23:37]** available um for use and so it's really easy on our website to uh or it's really

**[23:40]** easy on our website to uh or it's really

**[23:40]** easy on our website to uh or it's really easy to follow our quick start on our

**[23:42]** easy to follow our quick start on our

**[23:42]** easy to follow our quick start on our website and build a voice AI agent that

**[23:43]** website and build a voice AI agent that

**[23:43]** website and build a voice AI agent that you can talk to. Um and it's just one

**[23:46]** you can talk to. Um and it's just one

**[23:46]** you can talk to. Um and it's just one more line in our in the pipeline that

**[23:48]** more line in our in the pipeline that

**[23:48]** more line in our in the pipeline that you you build. You just turn on you have

**[23:50]** you you build. You just turn on you have

**[23:50]** you you build. You just turn on you have one more line in there and you get to

**[23:52]** one more line in there and you get to

**[23:52]** one more line in there and you get to use our end of utterance model. It's

**[23:54]** use our end of utterance model. It's

**[23:54]** use our end of utterance model. It's open weight. It's you don't have to pay

**[23:56]** open weight. It's you don't have to pay

**[23:56]** open weight. It's you don't have to pay for it. It's just baked in. Um and our

**[23:58]** for it. It's just baked in. Um and our

**[23:58]** for it. It's just baked in. Um and our docs show you pretty I think by default


### [24:00 - 25:00]

**[24:00]** docs show you pretty I think by default

**[24:00]** docs show you pretty I think by default it's in there. Um and the the third

**[24:03]** it's in there. Um and the the third

**[24:03]** it's in there. Um and the the third question uh remind me the third

**[24:05]** question uh remind me the third

**[24:06]** question uh remind me the third question. I'm sorry.

**[24:09]** question. I'm sorry.

**[24:09]** question. I'm sorry. Ah yes, benchmarking.

**[24:11]** Ah yes, benchmarking.

**[24:11]** Ah yes, benchmarking. Um so we have benchmarks where we have

**[24:13]** Um so we have benchmarks where we have

**[24:13]** Um so we have benchmarks where we have our test data set and you know the

**[24:15]** our test data set and you know the

**[24:15]** our test data set and you know the numbers of course look great. Um,

**[24:18]** numbers of course look great. Um,

**[24:18]** numbers of course look great. Um, but I think uh I was on a long call with

**[24:22]** but I think uh I was on a long call with

**[24:22]** but I think uh I was on a long call with our machine learning team this morning

**[24:24]** our machine learning team this morning

**[24:24]** our machine learning team this morning where we spent a lot of time just

**[24:25]** where we spent a lot of time just

**[24:25]** where we spent a lot of time just talking about like how do we get a good

**[24:26]** talking about like how do we get a good

**[24:26]** talking about like how do we get a good data set for benchmarking that and it's

**[24:29]** data set for benchmarking that and it's

**[24:29]** data set for benchmarking that and it's just it's just really it's a tough

**[24:31]** just it's just really it's a tough

**[24:31]** just it's just really it's a tough problem. Um, and I feel like the

**[24:33]** problem. Um, and I feel like the

**[24:33]** problem. Um, and I feel like the industry as a whole doesn't have a good

**[24:35]** industry as a whole doesn't have a good

**[24:35]** industry as a whole doesn't have a good benchmark around turn taking. Um, and

**[24:37]** benchmark around turn taking. Um, and

**[24:37]** benchmark around turn taking. Um, and that it's something that I'm sure will

**[24:39]** that it's something that I'm sure will

**[24:39]** that it's something that I'm sure will eventually emerge.

**[24:42]** eventually emerge.

**[24:42]** eventually emerge. Uh, okay. We we'll do one last question

**[24:45]** Uh, okay. We we'll do one last question

**[24:45]** Uh, okay. We we'll do one last question I think. So there was yes you in the

**[24:48]** I think. So there was yes you in the

**[24:48]** I think. So there was yes you in the back not great to be sitting in the back

**[24:50]** back not great to be sitting in the back

**[24:50]** back not great to be sitting in the back if you want to ask questions but

**[24:53]** if you want to ask questions but

**[24:53]** if you want to ask questions but thank you Tom for the diamond and the

**[24:56]** thank you Tom for the diamond and the

**[24:56]** thank you Tom for the diamond and the presentation I got question related to

**[24:57]** presentation I got question related to

**[24:57]** presentation I got question related to the back channel. So how did you tackle


### [25:00 - 26:00]

**[25:00]** the back channel. So how did you tackle

**[25:00]** the back channel. So how did you tackle the back channel challenge in the turn

**[25:02]** the back channel challenge in the turn

**[25:02]** the back channel challenge in the turn taking detection problem. So first uh

**[25:05]** taking detection problem. So first uh

**[25:05]** taking detection problem. So first uh for a natural conversational AI the back

**[25:08]** for a natural conversational AI the back

**[25:08]** for a natural conversational AI the back channel is the one that cannot be uh

**[25:10]** channel is the one that cannot be uh

**[25:10]** channel is the one that cannot be uh ignored and sometimes it cause trouble

**[25:13]** ignored and sometimes it cause trouble

**[25:13]** ignored and sometimes it cause trouble for the voice agent to detect whether it

**[25:16]** for the voice agent to detect whether it

**[25:16]** for the voice agent to detect whether it is it is the end pointing and second for

**[25:20]** is it is the end pointing and second for

**[25:20]** is it is the end pointing and second for a typical back channel like yeah uh yes

**[25:24]** a typical back channel like yeah uh yes

**[25:24]** a typical back channel like yeah uh yes uh those words can occur like a back

**[25:26]** uh those words can occur like a back

**[25:26]** uh those words can occur like a back channel or it can be start as the uh the

**[25:30]** channel or it can be start as the uh the

**[25:30]** channel or it can be start as the uh the agent who should be responding the in

**[25:32]** agent who should be responding the in

**[25:32]** agent who should be responding the in the following period. So how the back

**[25:34]** the following period. So how the back

**[25:34]** the following period. So how the back channel is handled should be kind of

**[25:36]** channel is handled should be kind of

**[25:36]** channel is handled should be kind of important in this field.

**[25:40]** important in this field.

**[25:40]** important in this field. So um my question was or the question

**[25:43]** So um my question was or the question

**[25:43]** So um my question was or the question was about not when the not the case

**[25:46]** was about not when the not the case

**[25:46]** was about not when the not the case where the AI is interrupting the human

**[25:48]** where the AI is interrupting the human

**[25:48]** where the AI is interrupting the human but the case where the human is

**[25:50]** but the case where the human is

**[25:50]** but the case where the human is accidentally interrupting the AI. Um and

**[25:53]** accidentally interrupting the AI. Um and

**[25:53]** accidentally interrupting the AI. Um and I didn't really cover that in my talk. I

**[25:55]** I didn't really cover that in my talk. I

**[25:55]** I didn't really cover that in my talk. I was mostly focusing on the AI

**[25:56]** was mostly focusing on the AI

**[25:56]** was mostly focusing on the AI interrupting the human. Um we don't have


### [26:00 - 27:00]

**[26:01]** interrupting the human. Um we don't have

**[26:01]** interrupting the human. Um we don't have our approach is simple like we're just

**[26:03]** our approach is simple like we're just

**[26:03]** our approach is simple like we're just using like the solar or the the normal

**[26:06]** using like the solar or the the normal

**[26:06]** using like the solar or the the normal VAD approach of like if the person is

**[26:08]** VAD approach of like if the person is

**[26:08]** VAD approach of like if the person is speaking for more than X milliseconds

**[26:11]** speaking for more than X milliseconds

**[26:11]** speaking for more than X milliseconds assume it's not a back channel and that

**[26:12]** assume it's not a back channel and that

**[26:12]** assume it's not a back channel and that they're actually trying to interrupt the

**[26:14]** they're actually trying to interrupt the

**[26:14]** they're actually trying to interrupt the voice AI. But one of the things we want

**[26:15]** voice AI. But one of the things we want

**[26:15]** voice AI. But one of the things we want to build is another machine learning

**[26:17]** to build is another machine learning

**[26:17]** to build is another machine learning model that can like recognize the

**[26:19]** model that can like recognize the

**[26:19]** model that can like recognize the difference between whether or not it's a

**[26:21]** difference between whether or not it's a

**[26:21]** difference between whether or not it's a back channel or someone trying to uh

**[26:24]** back channel or someone trying to uh

**[26:24]** back channel or someone trying to uh interrupt the the voice AI. One quick

**[26:27]** interrupt the the voice AI. One quick

**[26:27]** interrupt the the voice AI. One quick note on the full duplex models. Uh the

**[26:30]** note on the full duplex models. Uh the

**[26:30]** note on the full duplex models. Uh the meta AI one can natively back channel

**[26:33]** meta AI one can natively back channel

**[26:33]** meta AI one can natively back channel because it's like learned from the raw

**[26:34]** because it's like learned from the raw

**[26:34]** because it's like learned from the raw audio data. So when you're talking to

**[26:36]** audio data. So when you're talking to

**[26:36]** audio data. So when you're talking to it, it'll go mhm. Uhhuh. Which is just

**[26:38]** it, it'll go mhm. Uhhuh. Which is just

**[26:38]** it, it'll go mhm. Uhhuh. Which is just so neat. Um and uh yeah, it's just a

**[26:42]** so neat. Um and uh yeah, it's just a

**[26:42]** so neat. Um and uh yeah, it's just a it's a tough problem the back channeling

**[26:44]** it's a tough problem the back channeling

**[26:44]** it's a tough problem the back channeling thing.

**[26:47]** thing.

**[26:47]** thing. Awesome. Um yeah, if you have more

**[26:49]** Awesome. Um yeah, if you have more

**[26:49]** Awesome. Um yeah, if you have more questions, you can find Tom. Uh please

**[26:51]** questions, you can find Tom. Uh please

**[26:51]** questions, you can find Tom. Uh please give another warm applause for Tom.

**[26:53]** give another warm applause for Tom.

**[26:54]** give another warm applause for Tom. Thank you all.


