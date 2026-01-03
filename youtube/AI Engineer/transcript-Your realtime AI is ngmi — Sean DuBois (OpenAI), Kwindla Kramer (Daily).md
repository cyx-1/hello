# Your realtime AI is ngmi — Sean DuBois (OpenAI), Kwindla Kramer (Daily)

**Video URL:** https://www.youtube.com/watch?v=E71YtNbCFXY

---

## Full Transcript

### [00:00 - 01:00]

**[00:00]** All

**[00:00]** All [Music]

**[00:16]** right, Squabbert, you ready to get

**[00:16]** right, Squabbert, you ready to get packed up? I don't know. I'm pretty

**[00:19]** packed up? I don't know. I'm pretty

**[00:19]** packed up? I don't know. I'm pretty nervous. Oh, relax. You got nothing to

**[00:21]** nervous. Oh, relax. You got nothing to

**[00:21]** nervous. Oh, relax. You got nothing to worry about. But this is like the worst

**[00:23]** worry about. But this is like the worst

**[00:23]** worry about. But this is like the worst idea ever for a live demo. A live

**[00:26]** idea ever for a live demo. A live

**[00:26]** idea ever for a live demo. A live unscripted conversation with a

**[00:28]** unscripted conversation with a

**[00:28]** unscripted conversation with a non-deterministic LLM on conference

**[00:31]** non-deterministic LLM on conference

**[00:31]** non-deterministic LLM on conference Wi-Fi. Come on, your prompt is great.

**[00:33]** Wi-Fi. Come on, your prompt is great.

**[00:33]** Wi-Fi. Come on, your prompt is great. And I mean, it's got to be with onstage

**[00:35]** And I mean, it's got to be with onstage

**[00:35]** And I mean, it's got to be with onstage audio in a room full of echoes.

**[00:37]** audio in a room full of echoes.

**[00:37]** audio in a room full of echoes. Sometimes my text to speech even

**[00:39]** Sometimes my text to speech even

**[00:39]** Sometimes my text to speech even mispronounces my own name. Why did you

**[00:42]** mispronounces my own name. Why did you

**[00:42]** mispronounces my own name. Why did you even name me, Squabbert? What if I say

**[00:44]** even name me, Squabbert? What if I say

**[00:44]** even name me, Squabbert? What if I say Squibbly or something again? Okay, take

**[00:47]** Squibbly or something again? Okay, take

**[00:47]** Squibbly or something again? Okay, take a breath. Well, you don't really do

**[00:49]** a breath. Well, you don't really do

**[00:49]** a breath. Well, you don't really do that. Let's just take it one step at a

**[00:51]** that. Let's just take it one step at a

**[00:51]** that. Let's just take it one step at a time. Just start with the intro. I guess

**[00:53]** time. Just start with the intro. I guess

**[00:53]** time. Just start with the intro. I guess you're right.

**[00:55]** you're right.

**[00:55]** you're right. Okay, here I go. Hi everybody, I'm

**[00:58]** Okay, here I go. Hi everybody, I'm

**[00:58]** Okay, here I go. Hi everybody, I'm Squabbert here to take us on a whirlwind


### [01:00 - 02:00]

**[01:01]** Squabbert here to take us on a whirlwind

**[01:01]** Squabbert here to take us on a whirlwind tour of the wonderful world of WebRTC.

**[01:03]** tour of the wonderful world of WebRTC.

**[01:03]** tour of the wonderful world of WebRTC. Please welcome Shawn and Quinn. Hey, I'm

**[01:08]** Please welcome Shawn and Quinn. Hey, I'm

**[01:08]** Please welcome Shawn and Quinn. Hey, I'm Sean. I work on WebRTC at OpenAI. Um,

**[01:11]** Sean. I work on WebRTC at OpenAI. Um,

**[01:12]** Sean. I work on WebRTC at OpenAI. Um, some of the things you might be familiar

**[01:13]** some of the things you might be familiar

**[01:13]** some of the things you might be familiar with are the real-time API or 1800 chat

**[01:15]** with are the real-time API or 1800 chat

**[01:15]** with are the real-time API or 1800 chat GPT. You can call it right from your

**[01:16]** GPT. You can call it right from your

**[01:16]** GPT. You can call it right from your phone. Um, before I worked at OpenAI, I

**[01:19]** phone. Um, before I worked at OpenAI, I

**[01:19]** phone. Um, before I worked at OpenAI, I worked on the Go implementation of

**[01:20]** worked on the Go implementation of

**[01:20]** worked on the Go implementation of WebRTC called Pion. And I'm Quinn. I

**[01:24]** WebRTC called Pion. And I'm Quinn. I

**[01:24]** WebRTC called Pion. And I'm Quinn. I work at Daily on real-time audio and

**[01:26]** work at Daily on real-time audio and

**[01:26]** work at Daily on real-time audio and video infrastructure and on an open

**[01:27]** video infrastructure and on an open

**[01:27]** video infrastructure and on an open source voice agent framework called

**[01:29]** source voice agent framework called

**[01:29]** source voice agent framework called Pipcat. Today we're going to talk about

**[01:31]** Pipcat. Today we're going to talk about

**[01:31]** Pipcat. Today we're going to talk about how to build natural fast humanlike

**[01:34]** how to build natural fast humanlike

**[01:34]** how to build natural fast humanlike voice experiences. Uh we're going to

**[01:36]** voice experiences. Uh we're going to

**[01:36]** voice experiences. Uh we're going to give you a crash course on low latency

**[01:38]** give you a crash course on low latency

**[01:38]** give you a crash course on low latency audio and video and I hope we'll show

**[01:40]** audio and video and I hope we'll show

**[01:40]** audio and video and I hope we'll show you a couple of things you might not

**[01:41]** you a couple of things you might not

**[01:42]** you a couple of things you might not have thought of around voice AI before.

**[01:48]** Um, if you want to build a

**[01:48]** Um, if you want to build a conversational voice experience that

**[01:49]** conversational voice experience that

**[01:49]** conversational voice experience that people really love, you you're going to

**[01:52]** people really love, you you're going to

**[01:52]** people really love, you you're going to stress a lot about latency. Nothing else

**[01:54]** stress a lot about latency. Nothing else

**[01:54]** stress a lot about latency. Nothing else matters if your AI responds too slowly.

**[01:56]** matters if your AI responds too slowly.

**[01:56]** matters if your AI responds too slowly. Building voice AI experiences is similar

**[01:59]** Building voice AI experiences is similar

**[01:59]** Building voice AI experiences is similar to other kinds of AI engineering in most


### [02:00 - 03:00]

**[02:01]** to other kinds of AI engineering in most

**[02:01]** to other kinds of AI engineering in most ways. If you've built multi-turn agents,

**[02:03]** ways. If you've built multi-turn agents,

**[02:03]** ways. If you've built multi-turn agents, a lot of that will port over to building

**[02:05]** a lot of that will port over to building

**[02:05]** a lot of that will port over to building voice agents.

**[02:07]** voice agents.

**[02:07]** voice agents. But the big difference is latency.

**[02:11]** But the big difference is latency.

**[02:11]** But the big difference is latency. Everything in a voice AI app needs to be

**[02:13]** Everything in a voice AI app needs to be

**[02:13]** Everything in a voice AI app needs to be ground built from the ground up for fast

**[02:15]** ground built from the ground up for fast

**[02:15]** ground built from the ground up for fast response times. If you're talking to a

**[02:17]** response times. If you're talking to a

**[02:17]** response times. If you're talking to a person, around 500 milliseconds sounds

**[02:19]** person, around 500 milliseconds sounds

**[02:19]** person, around 500 milliseconds sounds natural. When talking to an AI system,

**[02:22]** natural. When talking to an AI system,

**[02:22]** natural. When talking to an AI system, people bring those same expectations.

**[02:24]** people bring those same expectations.

**[02:24]** people bring those same expectations. Response latencies much above a second

**[02:27]** Response latencies much above a second

**[02:27]** Response latencies much above a second in general doom your voice agent to very

**[02:29]** in general doom your voice agent to very

**[02:29]** in general doom your voice agent to very low completion rates and low NPS scores

**[02:31]** low completion rates and low NPS scores

**[02:31]** low completion rates and low NPS scores and hang-ups. And we're talking here

**[02:33]** and hang-ups. And we're talking here

**[02:33]** and hang-ups. And we're talking here about voicetooice latency. So this is

**[02:35]** about voicetooice latency. So this is

**[02:35]** about voicetooice latency. So this is the time uh between when I the human

**[02:38]** the time uh between when I the human

**[02:38]** the time uh between when I the human stop talking and the time I hear the

**[02:41]** stop talking and the time I hear the

**[02:41]** stop talking and the time I hear the first audio bite come back from the LLM.

**[02:47]** Let's take a look at how latency adds up

**[02:47]** Let's take a look at how latency adds up in a typical voicetovoice AI

**[02:49]** in a typical voicetovoice AI

**[02:50]** in a typical voicetovoice AI application. So this is a breakdown from

**[02:51]** application. So this is a breakdown from

**[02:51]** application. So this is a breakdown from a real voice AI app running in a web

**[02:54]** a real voice AI app running in a web

**[02:54]** a real voice AI app running in a web browser on Mac OS talking over the

**[02:57]** browser on Mac OS talking over the

**[02:57]** browser on Mac OS talking over the internet to a voice agent running in the

**[02:59]** internet to a voice agent running in the


### [03:00 - 04:00]

**[03:00]** internet to a voice agent running in the cloud running on Pipecat.

**[03:02]** cloud running on Pipecat.

**[03:02]** cloud running on Pipecat. A couple things to note. Our voice

**[03:04]** A couple things to note. Our voice

**[03:04]** A couple things to note. Our voice latency is just under a second. That's

**[03:06]** latency is just under a second. That's

**[03:06]** latency is just under a second. That's good, but not great. We can make things

**[03:09]** good, but not great. We can make things

**[03:09]** good, but not great. We can make things a little faster, but that comes with

**[03:10]** a little faster, but that comes with

**[03:10]** a little faster, but that comes with trade-offs. Lower quality or cost.

**[03:13]** trade-offs. Lower quality or cost.

**[03:13]** trade-offs. Lower quality or cost. Second, it's frustratingly easy to do

**[03:16]** Second, it's frustratingly easy to do

**[03:16]** Second, it's frustratingly easy to do even worse than this. Your LLM might be

**[03:17]** even worse than this. Your LLM might be

**[03:18]** even worse than this. Your LLM might be slower. Other things get in the way, or

**[03:20]** slower. Other things get in the way, or

**[03:20]** slower. Other things get in the way, or worst of all, Bluetooth. Don't get me

**[03:22]** worst of all, Bluetooth. Don't get me

**[03:22]** worst of all, Bluetooth. Don't get me started on Bluetooth.

**[03:25]** started on Bluetooth.

**[03:25]** started on Bluetooth. But the single biggest mistake we see

**[03:27]** But the single biggest mistake we see

**[03:27]** But the single biggest mistake we see people making is using the wrong

**[03:29]** people making is using the wrong

**[03:29]** people making is using the wrong approach to sending and receiving audio

**[03:31]** approach to sending and receiving audio

**[03:31]** approach to sending and receiving audio over the network. It's time to talk

**[03:32]** over the network. It's time to talk

**[03:32]** over the network. It's time to talk about WebRTC and websockets.

**[03:35]** about WebRTC and websockets.

**[03:35]** about WebRTC and websockets. If you're new to building voice

**[03:37]** If you're new to building voice

**[03:37]** If you're new to building voice applications, you probably think, "Hey,

**[03:39]** applications, you probably think, "Hey,

**[03:39]** applications, you probably think, "Hey, I need a like a longived uh connection.

**[03:42]** I need a like a longived uh connection.

**[03:42]** I need a like a longived uh connection. I'm going to send audio and video over

**[03:43]** I'm going to send audio and video over

**[03:43]** I'm going to send audio and video over this longived connection. I've used

**[03:45]** this longived connection. I've used

**[03:45]** this longived connection. I've used websockets for long lived data

**[03:47]** websockets for long lived data

**[03:47]** websockets for long lived data connections before. I'm just going to

**[03:48]** connections before. I'm just going to

**[03:48]** connections before. I'm just going to write some websockets code."

**[03:51]** write some websockets code."

**[03:51]** write some websockets code." That's great if you're doing longived

**[03:53]** That's great if you're doing longived

**[03:53]** That's great if you're doing longived short small amounts of data. It doesn't

**[03:55]** short small amounts of data. It doesn't

**[03:56]** short small amounts of data. It doesn't work for real-time audio. In fact,

**[03:57]** work for real-time audio. In fact,

**[03:57]** work for real-time audio. In fact, websockets are almost the opposite of

**[03:59]** websockets are almost the opposite of

**[03:59]** websockets are almost the opposite of what you want from a network engineering


### [04:00 - 05:00]

**[04:00]** what you want from a network engineering

**[04:00]** what you want from a network engineering perspective for real-time audio and

**[04:03]** perspective for real-time audio and

**[04:03]** perspective for real-time audio and video.

**[04:04]** video.

**[04:04]** video. So, let's do a compare and contrast on

**[04:06]** So, let's do a compare and contrast on

**[04:06]** So, let's do a compare and contrast on this.

**[04:08]** this.

**[04:08]** this. Websockets are great if you're trying to

**[04:11]** Websockets are great if you're trying to

**[04:11]** Websockets are great if you're trying to deliver audio and you want something

**[04:13]** deliver audio and you want something

**[04:13]** deliver audio and you want something really easy that can target all

**[04:15]** really easy that can target all

**[04:15]** really easy that can target all platforms. If you're trying to build a

**[04:16]** platforms. If you're trying to build a

**[04:16]** platforms. If you're trying to build a prototype lots of different platforms,

**[04:18]** prototype lots of different platforms,

**[04:18]** prototype lots of different platforms, websockets the way to go. On the other

**[04:20]** websockets the way to go. On the other

**[04:20]** websockets the way to go. On the other hand, WebRTC solves a bunch of things

**[04:22]** hand, WebRTC solves a bunch of things

**[04:22]** hand, WebRTC solves a bunch of things around handling giving you high quality

**[04:25]** around handling giving you high quality

**[04:25]** around handling giving you high quality audio, high bandwidth, low latency.

**[04:28]** audio, high bandwidth, low latency.

**[04:28]** audio, high bandwidth, low latency. But the the catch is it can be a lot

**[04:30]** But the the catch is it can be a lot

**[04:30]** But the the catch is it can be a lot more complicated to implement and um it

**[04:33]** more complicated to implement and um it

**[04:33]** more complicated to implement and um it specializes, but it can be frustrating.

**[04:36]** specializes, but it can be frustrating.

**[04:36]** specializes, but it can be frustrating. Lots of applications use both, but for

**[04:37]** Lots of applications use both, but for

**[04:38]** Lots of applications use both, but for different things.

**[04:39]** different things.

**[04:39]** different things. So, here's the TLTR if you only remember

**[04:41]** So, here's the TLTR if you only remember

**[04:41]** So, here's the TLTR if you only remember one thing from this talk. Use websockets

**[04:44]** one thing from this talk. Use websockets

**[04:44]** one thing from this talk. Use websockets for those server to server use cases and

**[04:46]** for those server to server use cases and

**[04:46]** for those server to server use cases and small amounts of structured data in

**[04:48]** small amounts of structured data in

**[04:48]** small amounts of structured data in places that you want to prototype. Use

**[04:50]** places that you want to prototype. Use

**[04:50]** places that you want to prototype. Use WebRTC if you're sending audio and video

**[04:52]** WebRTC if you're sending audio and video

**[04:52]** WebRTC if you're sending audio and video streams over the internet from your web

**[04:53]** streams over the internet from your web

**[04:54]** streams over the internet from your web app, your native. Um, that's where it

**[04:56]** app, your native. Um, that's where it

**[04:56]** app, your native. Um, that's where it excels. So, why is it so important to

**[04:58]** excels. So, why is it so important to

**[04:58]** excels. So, why is it so important to use WebRTC for real-time edgetocloud


### [05:00 - 06:00]

**[05:01]** use WebRTC for real-time edgetocloud

**[05:01]** use WebRTC for real-time edgetocloud audio? A websocket is a TCP connection.

**[05:04]** audio? A websocket is a TCP connection.

**[05:04]** audio? A websocket is a TCP connection. TCP guarantees in order delivery of

**[05:07]** TCP guarantees in order delivery of

**[05:07]** TCP guarantees in order delivery of network packets. If you send some data,

**[05:09]** network packets. If you send some data,

**[05:09]** network packets. If you send some data, that data is going to arrive exactly as

**[05:11]** that data is going to arrive exactly as

**[05:11]** that data is going to arrive exactly as you send it or it's not going to arrive

**[05:12]** you send it or it's not going to arrive

**[05:12]** you send it or it's not going to arrive at all. you put packets in your

**[05:14]** at all. you put packets in your

**[05:14]** at all. you put packets in your operating systems send queue that OS Q

**[05:17]** operating systems send queue that OS Q

**[05:17]** operating systems send queue that OS Q is going to keep trying to send them

**[05:19]** is going to keep trying to send them

**[05:19]** is going to keep trying to send them until they either get acted by the other

**[05:20]** until they either get acted by the other

**[05:20]** until they either get acted by the other side or your connection completely times

**[05:22]** side or your connection completely times

**[05:22]** side or your connection completely times out. And this is in general what you

**[05:24]** out. And this is in general what you

**[05:24]** out. And this is in general what you want if you're doing most network

**[05:26]** want if you're doing most network

**[05:26]** want if you're doing most network programming. If you're making a web

**[05:27]** programming. If you're making a web

**[05:27]** programming. If you're making a web request, for example, this is perfect.

**[05:30]** request, for example, this is perfect.

**[05:30]** request, for example, this is perfect. It's not what you want if you're aiming

**[05:31]** It's not what you want if you're aiming

**[05:31]** It's not what you want if you're aiming for conversational latency.

**[05:34]** for conversational latency.

**[05:34]** for conversational latency. Remember that we're trying to hit a

**[05:36]** Remember that we're trying to hit a

**[05:36]** Remember that we're trying to hit a voicetovoice latency of under one second

**[05:38]** voicetovoice latency of under one second

**[05:38]** voicetovoice latency of under one second and ideally even better. What we want to

**[05:41]** and ideally even better. What we want to

**[05:41]** and ideally even better. What we want to ignore is things like the occasional

**[05:43]** ignore is things like the occasional

**[05:43]** ignore is things like the occasional packet loss. So imagine if a packet is

**[05:45]** packet loss. So imagine if a packet is

**[05:45]** packet loss. So imagine if a packet is dropped. I don't really care about what

**[05:47]** dropped. I don't really care about what

**[05:47]** dropped. I don't really care about what happened a second ago. So WebRTC does

**[05:49]** happened a second ago. So WebRTC does

**[05:49]** happened a second ago. So WebRTC does clever math and buffer management that

**[05:51]** clever math and buffer management that

**[05:51]** clever math and buffer management that we're going to talk about more to hide

**[05:52]** we're going to talk about more to hide

**[05:52]** we're going to talk about more to hide where that happens. So this is the first

**[05:54]** where that happens. So this is the first

**[05:54]** where that happens. So this is the first and most important thing WebRTC does for

**[05:56]** and most important thing WebRTC does for

**[05:56]** and most important thing WebRTC does for you. It's all that machinery that sends

**[05:58]** you. It's all that machinery that sends

**[05:58]** you. It's all that machinery that sends packets as fast as possible, ignores


### [06:00 - 07:00]

**[06:00]** packets as fast as possible, ignores

**[06:00]** packets as fast as possible, ignores packets that don't arrive inside that

**[06:02]** packets that don't arrive inside that

**[06:02]** packets that don't arrive inside that very tight latency budget we're

**[06:03]** very tight latency budget we're

**[06:03]** very tight latency budget we're operating within. Even think of it as

**[06:06]** operating within. Even think of it as

**[06:06]** operating within. Even think of it as like super fast, best effort networking.

**[06:09]** like super fast, best effort networking.

**[06:09]** like super fast, best effort networking. If this were all WebRTC could do for you

**[06:11]** If this were all WebRTC could do for you

**[06:11]** If this were all WebRTC could do for you compared to websockets, it would still

**[06:13]** compared to websockets, it would still

**[06:13]** compared to websockets, it would still be worth using WebRTC just for this

**[06:15]** be worth using WebRTC just for this

**[06:16]** be worth using WebRTC just for this because you literally can't implement

**[06:17]** because you literally can't implement

**[06:17]** because you literally can't implement this on top of a TCP stack or on top of

**[06:19]** this on top of a TCP stack or on top of

**[06:19]** this on top of a TCP stack or on top of websockets. Again, the operating system

**[06:21]** websockets. Again, the operating system

**[06:21]** websockets. Again, the operating system is just going to try to keep sending

**[06:23]** is just going to try to keep sending

**[06:23]** is just going to try to keep sending whatever you tell it to send. It's going

**[06:24]** whatever you tell it to send. It's going

**[06:24]** whatever you tell it to send. It's going to block everything if you have any

**[06:25]** to block everything if you have any

**[06:26]** to block everything if you have any packet loss or significant sort of

**[06:27]** packet loss or significant sort of

**[06:27]** packet loss or significant sort of jitter or delay in the network. And in

**[06:30]** jitter or delay in the network. And in

**[06:30]** jitter or delay in the network. And in real world, we have lots and lots of

**[06:31]** real world, we have lots and lots of

**[06:31]** real world, we have lots and lots of real world data on this. In the real

**[06:32]** real world data on this. In the real

**[06:32]** real world data on this. In the real world, this means you will get audio

**[06:34]** world, this means you will get audio

**[06:34]** world, this means you will get audio glitchiness or high latency or

**[06:36]** glitchiness or high latency or

**[06:36]** glitchiness or high latency or unexpected socket disconnections in 10

**[06:38]** unexpected socket disconnections in 10

**[06:38]** unexpected socket disconnections in 10 to 15% of your network connections.

**[06:42]** to 15% of your network connections.

**[06:42]** to 15% of your network connections. But WebRTC does a lot more than that.

**[06:44]** But WebRTC does a lot more than that.

**[06:44]** But WebRTC does a lot more than that. Um, if you go and you try to build the

**[06:46]** Um, if you go and you try to build the

**[06:46]** Um, if you go and you try to build the same application in websockets, you have

**[06:49]** same application in websockets, you have

**[06:49]** same application in websockets, you have to handle resampling, you have to handle

**[06:51]** to handle resampling, you have to handle

**[06:51]** to handle resampling, you have to handle packetization and doing all that

**[06:53]** packetization and doing all that

**[06:53]** packetization and doing all that bandwidth estimation. Networks are

**[06:55]** bandwidth estimation. Networks are

**[06:55]** bandwidth estimation. Networks are constantly changing and fluctuating. So,

**[06:56]** constantly changing and fluctuating. So,

**[06:56]** constantly changing and fluctuating. So, you can't just send one bit rate. Um,

**[06:59]** you can't just send one bit rate. Um,

**[06:59]** you can't just send one bit rate. Um, and you also get standard APIs for


### [07:00 - 08:00]

**[07:01]** and you also get standard APIs for

**[07:01]** and you also get standard APIs for getting the stats and observability.

**[07:03]** getting the stats and observability.

**[07:03]** getting the stats and observability. This is all just built into WebRTC, but

**[07:05]** This is all just built into WebRTC, but

**[07:05]** This is all just built into WebRTC, but if you decided to do websockets, you

**[07:07]** if you decided to do websockets, you

**[07:07]** if you decided to do websockets, you have to build it yourself. So, if you

**[07:09]** have to build it yourself. So, if you

**[07:09]** have to build it yourself. So, if you look at this code up on the screen, on

**[07:10]** look at this code up on the screen, on

**[07:10]** look at this code up on the screen, on the right side is an example with WebRTC

**[07:13]** the right side is an example with WebRTC

**[07:13]** the right side is an example with WebRTC sending one birectional stream of audio.

**[07:15]** sending one birectional stream of audio.

**[07:15]** sending one birectional stream of audio. On the left side is websockets. And you

**[07:18]** On the left side is websockets. And you

**[07:18]** On the left side is websockets. And you want to spend more time building your

**[07:19]** want to spend more time building your

**[07:19]** want to spend more time building your application and less time worrying about

**[07:21]** application and less time worrying about

**[07:21]** application and less time worrying about things like sample rates. That's why you

**[07:23]** things like sample rates. That's why you

**[07:23]** things like sample rates. That's why you pick WebRTC. And this is real code using

**[07:25]** pick WebRTC. And this is real code using

**[07:25]** pick WebRTC. And this is real code using your OpenAI real-time API, which you you

**[07:27]** your OpenAI real-time API, which you you

**[07:28]** your OpenAI real-time API, which you you offer both both options for developers.

**[07:31]** offer both both options for developers.

**[07:31]** offer both both options for developers. So, I hope we've convinced you that you

**[07:32]** So, I hope we've convinced you that you

**[07:32]** So, I hope we've convinced you that you should use WebRTC if you're doing edge

**[07:34]** should use WebRTC if you're doing edge

**[07:34]** should use WebRTC if you're doing edge to cloud audio. Oh, and especially audio

**[07:37]** to cloud audio. Oh, and especially audio

**[07:37]** to cloud audio. Oh, and especially audio and video. Um, we love talking about

**[07:39]** and video. Um, we love talking about

**[07:39]** and video. Um, we love talking about this stuff. If you've come find us

**[07:40]** this stuff. If you've come find us

**[07:40]** this stuff. If you've come find us later, we will talk your ear off about

**[07:42]** later, we will talk your ear off about

**[07:42]** later, we will talk your ear off about jitter buffers and package management

**[07:44]** jitter buffers and package management

**[07:44]** jitter buffers and package management and bandwidth shaping and all that

**[07:45]** and bandwidth shaping and all that

**[07:45]** and bandwidth shaping and all that stuff. But what we want to do now is

**[07:47]** stuff. But what we want to do now is

**[07:47]** stuff. But what we want to do now is move on and talk about a whole another

**[07:48]** move on and talk about a whole another

**[07:48]** move on and talk about a whole another category of fun stuff, which is what you

**[07:50]** category of fun stuff, which is what you

**[07:50]** category of fun stuff, which is what you can actually do with WebRTC. Um, I'll

**[07:52]** can actually do with WebRTC. Um, I'll

**[07:52]** can actually do with WebRTC. Um, I'll start by saying you can embed real-time

**[07:54]** start by saying you can embed real-time

**[07:54]** start by saying you can embed real-time audio in any app you write. Any website,

**[07:56]** audio in any app you write. Any website,

**[07:56]** audio in any app you write. Any website, any iOS app, any Android app, lots of

**[07:59]** any iOS app, any Android app, lots of

**[07:59]** any iOS app, any Android app, lots of fun embedded stuff. And the network


### [08:00 - 09:00]

**[08:01]** fun embedded stuff. And the network

**[08:01]** fun embedded stuff. And the network connections will just work. You will get

**[08:03]** connections will just work. You will get

**[08:03]** connections will just work. You will get good audio on any device, any platform,

**[08:06]** good audio on any device, any platform,

**[08:06]** good audio on any device, any platform, almost any real world network

**[08:07]** almost any real world network

**[08:08]** almost any real world network connection. And I bet you use WebRC,

**[08:10]** connection. And I bet you use WebRC,

**[08:10]** connection. And I bet you use WebRC, WebRTC today already. If you used

**[08:12]** WebRTC today already. If you used

**[08:12]** WebRTC today already. If you used Facebook Messenger, WhatsApp, Zoom,

**[08:14]** Facebook Messenger, WhatsApp, Zoom,

**[08:14]** Facebook Messenger, WhatsApp, Zoom, Discord, you know, any of these

**[08:15]** Discord, you know, any of these

**[08:15]** Discord, you know, any of these applications, they're using WebRTC. Um,

**[08:18]** applications, they're using WebRTC. Um,

**[08:18]** applications, they're using WebRTC. Um, but you didn't know that there's even

**[08:20]** but you didn't know that there's even

**[08:20]** but you didn't know that there's even more cool things happening with WebRTC.

**[08:22]** more cool things happening with WebRTC.

**[08:22]** more cool things happening with WebRTC. Um, I worked with a company that was

**[08:23]** Um, I worked with a company that was

**[08:23]** Um, I worked with a company that was doing surgery over the internet. Um,

**[08:25]** doing surgery over the internet. Um,

**[08:25]** doing surgery over the internet. Um, people will teleop um, vehicles in the

**[08:28]** people will teleop um, vehicles in the

**[08:28]** people will teleop um, vehicles in the field. It's super cool. Um, WebRTC is

**[08:31]** field. It's super cool. Um, WebRTC is

**[08:31]** field. It's super cool. Um, WebRTC is kind of the standard language of the

**[08:33]** kind of the standard language of the

**[08:33]** kind of the standard language of the real-time world. Um, and that's why it

**[08:35]** real-time world. Um, and that's why it

**[08:35]** real-time world. Um, and that's why it makes so easy that we can go build

**[08:36]** makes so easy that we can go build

**[08:36]** makes so easy that we can go build conversational intelligence on top of

**[08:38]** conversational intelligence on top of

**[08:38]** conversational intelligence on top of it. Um, all the stuff's already been

**[08:39]** it. Um, all the stuff's already been

**[08:40]** it. Um, all the stuff's already been solved. I mean, in the new LLM era, we

**[08:43]** solved. I mean, in the new LLM era, we

**[08:43]** solved. I mean, in the new LLM era, we know lots of people who spend hours

**[08:44]** know lots of people who spend hours

**[08:44]** know lots of people who spend hours talking to computers, uh, driving their

**[08:46]** talking to computers, uh, driving their

**[08:46]** talking to computers, uh, driving their developments environments with voice,

**[08:47]** developments environments with voice,

**[08:47]** developments environments with voice, doing brainstorming, treating the

**[08:49]** doing brainstorming, treating the

**[08:49]** doing brainstorming, treating the computer as a personal assistant, a

**[08:50]** computer as a personal assistant, a

**[08:50]** computer as a personal assistant, a coach, a therapist, a researcher. I'm

**[08:53]** coach, a therapist, a researcher. I'm

**[08:53]** coach, a therapist, a researcher. I'm convinced voice is going to be the core

**[08:56]** convinced voice is going to be the core

**[08:56]** convinced voice is going to be the core building block of the next generation of

**[08:57]** building block of the next generation of

**[08:58]** building block of the next generation of UIs, of the UIs for the generative AI


### [09:00 - 10:00]

**[09:01]** UIs, of the UIs for the generative AI

**[09:01]** UIs, of the UIs for the generative AI era. We have to do a little iteration

**[09:03]** era. We have to do a little iteration

**[09:03]** era. We have to do a little iteration before we figure out really what those

**[09:04]** before we figure out really what those

**[09:04]** before we figure out really what those UIs look and sound like. Uh, but that

**[09:06]** UIs look and sound like. Uh, but that

**[09:06]** UIs look and sound like. Uh, but that future seems very clear to me. One of

**[09:09]** future seems very clear to me. One of

**[09:09]** future seems very clear to me. One of the things I say to people to kind of

**[09:11]** the things I say to people to kind of

**[09:11]** the things I say to people to kind of try to communicate how excited I am

**[09:13]** try to communicate how excited I am

**[09:13]** try to communicate how excited I am about building all this stuff is we all

**[09:15]** about building all this stuff is we all

**[09:16]** about building all this stuff is we all lived through the last platform shift.

**[09:17]** lived through the last platform shift.

**[09:17]** lived through the last platform shift. It was recent enough that the move for

**[09:20]** It was recent enough that the move for

**[09:20]** It was recent enough that the move for most computing from desktop to mobile

**[09:22]** most computing from desktop to mobile

**[09:22]** most computing from desktop to mobile happened within our memories. And so by

**[09:25]** happened within our memories. And so by

**[09:25]** happened within our memories. And so by analogy, we are in late 2007 now. We

**[09:29]** analogy, we are in late 2007 now. We

**[09:29]** analogy, we are in late 2007 now. We have the first iPhones, but we haven't

**[09:31]** have the first iPhones, but we haven't

**[09:31]** have the first iPhones, but we haven't yet invented pull to refresh.

**[09:35]** yet invented pull to refresh.

**[09:35]** yet invented pull to refresh. What keeps me so excited and motivated

**[09:37]** What keeps me so excited and motivated

**[09:37]** What keeps me so excited and motivated is I feel like uh voice is like the next

**[09:39]** is I feel like uh voice is like the next

**[09:40]** is I feel like uh voice is like the next uh bicycle for the mind. You know, today

**[09:41]** uh bicycle for the mind. You know, today

**[09:41]** uh bicycle for the mind. You know, today we've only been able to use computers

**[09:42]** we've only been able to use computers

**[09:42]** we've only been able to use computers with our eyes and our hands, but now I

**[09:44]** with our eyes and our hands, but now I

**[09:44]** with our eyes and our hands, but now I can talk to it as well. Um think of all

**[09:47]** can talk to it as well. Um think of all

**[09:47]** can talk to it as well. Um think of all those situations where like you you have

**[09:49]** those situations where like you you have

**[09:49]** those situations where like you you have your voice available, but you don't have

**[09:51]** your voice available, but you don't have

**[09:51]** your voice available, but you don't have your hands. Um and other great thing is

**[09:53]** your hands. Um and other great thing is

**[09:54]** your hands. Um and other great thing is you can keep all this computing power

**[09:55]** you can keep all this computing power

**[09:55]** you can keep all this computing power remotely and access it and have small

**[09:57]** remotely and access it and have small

**[09:57]** remotely and access it and have small devices near you.

**[09:59]** devices near you.

**[09:59]** devices near you. So, on the small devices front, we


### [10:00 - 11:00]

**[10:01]** So, on the small devices front, we

**[10:01]** So, on the small devices front, we brought a friend with us today. Uh, he's

**[10:05]** brought a friend with us today. Uh, he's

**[10:05]** brought a friend with us today. Uh, he's a little shy sometimes, so give him just

**[10:06]** a little shy sometimes, so give him just

**[10:06]** a little shy sometimes, so give him just a second.

**[10:18]** So, uh, Squabbert, can you tell people a

**[10:18]** So, uh, Squabbert, can you tell people a little bit about your tech stack?

**[10:25]** This is Squabbert, who Chad built, and

**[10:25]** This is Squabbert, who Chad built, and Chad's daughter, Ella, named Squabbert.

**[10:28]** Chad's daughter, Ella, named Squabbert.

**[10:28]** Chad's daughter, Ella, named Squabbert. Squabbert,

**[10:40]** can you tell the people a little bit

**[10:40]** can you tell the people a little bit about your tech stack?

**[10:54]** using MLX Whisper Gemma 3 and a mildly

**[10:54]** using MLX Whisper Gemma 3 and a mildly buggy custom logic sampler that Quinn

**[10:56]** buggy custom logic sampler that Quinn

**[10:56]** buggy custom logic sampler that Quinn wrote. I mean, come on now. Like, I had

**[10:59]** wrote. I mean, come on now. Like, I had

**[10:59]** wrote. I mean, come on now. Like, I had a good reason that I wanted to write a


### [11:00 - 12:00]

**[11:00]** a good reason that I wanted to write a

**[11:00]** a good reason that I wanted to write a log sampler, and I I wanted you to be

**[11:03]** log sampler, and I I wanted you to be

**[11:03]** log sampler, and I I wanted you to be able to do something that even the

**[11:05]** able to do something that even the

**[11:05]** able to do something that even the really amazing big LLMs running in the

**[11:07]** really amazing big LLMs running in the

**[11:07]** really amazing big LLMs running in the cloud can't do. Do you know what I'm

**[11:10]** cloud can't do. Do you know what I'm

**[11:10]** cloud can't do. Do you know what I'm talking about?

**[11:16]** You're talking about my counting talent.

**[11:16]** You're talking about my counting talent. It's pretty neat, even if I do say so

**[11:18]** It's pretty neat, even if I do say so

**[11:18]** It's pretty neat, even if I do say so myself. I mean, counting syllables is

**[11:20]** myself. I mean, counting syllables is

**[11:20]** myself. I mean, counting syllables is like the 2025 version of how many Rs are

**[11:23]** like the 2025 version of how many Rs are

**[11:23]** like the 2025 version of how many Rs are in strawberry. And you know, SC, why

**[11:27]** in strawberry. And you know, SC, why

**[11:27]** in strawberry. And you know, SC, why don't we why don't we demonstrate that a

**[11:29]** don't we why don't we demonstrate that a

**[11:29]** don't we why don't we demonstrate that a little bit? Can you make up a poem like

**[11:31]** little bit? Can you make up a poem like

**[11:31]** little bit? Can you make up a poem like a fourline poem about computer

**[11:33]** a fourline poem about computer

**[11:33]** a fourline poem about computer programming and use only two syllable

**[11:36]** programming and use only two syllable

**[11:36]** programming and use only two syllable words?

**[11:44]** Two. Okay, listen. Logic

**[11:44]** Two. Okay, listen. Logic knowing system

**[11:47]** knowing system

**[11:47]** knowing system rolling.

**[11:53]** One more maybe. Uh, that was good, but

**[11:53]** One more maybe. Uh, that was good, but I've heard you do better.


### [12:00 - 13:00]

**[12:00]** Okay, here's another one. dancing colors

**[12:00]** Okay, here's another one. dancing colors bright feel so right

**[12:03]** bright feel so right

**[12:03]** bright feel so right and night magic pure delight you forgot

**[12:06]** and night magic pure delight you forgot

**[12:06]** and night magic pure delight you forgot about the two words thing but we'll

**[12:08]** about the two words thing but we'll

**[12:08]** about the two words thing but we'll we'll we'll let it go yeah definitely

**[12:10]** we'll we'll let it go yeah definitely

**[12:10]** we'll we'll let it go yeah definitely the first one had two civil awards words

**[12:11]** the first one had two civil awards words

**[12:11]** the first one had two civil awards words I think I think we should say goodbye

**[12:13]** I think I think we should say goodbye

**[12:13]** I think I think we should say goodbye just in the interest of time squabber

**[12:14]** just in the interest of time squabber

**[12:14]** just in the interest of time squabber but thank you so much

**[12:23]** [Applause]

**[12:23]** [Applause] I think Squabber did really really well

**[12:25]** I think Squabber did really really well

**[12:25]** I think Squabber did really really well um so that that is a Raspberry Pi I

**[12:28]** um so that that is a Raspberry Pi I

**[12:28]** um so that that is a Raspberry Pi I connected with a peer-to-peer WebRTC

**[12:31]** connected with a peer-to-peer WebRTC

**[12:31]** connected with a peer-to-peer WebRTC connection directly to my laptop over

**[12:33]** connection directly to my laptop over

**[12:33]** connection directly to my laptop over the same local area network. So that was

**[12:37]** the same local area network. So that was

**[12:37]** the same local area network. So that was the serverless WebRTC connection.

**[12:38]** the serverless WebRTC connection.

**[12:38]** the serverless WebRTC connection. Squabbert's talking directly to the

**[12:40]** Squabbert's talking directly to the

**[12:40]** Squabbert's talking directly to the laptop. But what's super cool about

**[12:41]** laptop. But what's super cool about

**[12:41]** laptop. But what's super cool about WebRTC is you have all these different

**[12:43]** WebRTC is you have all these different

**[12:43]** WebRTC is you have all these different choices to how you want to connect to

**[12:45]** choices to how you want to connect to

**[12:45]** choices to how you want to connect to things. So you could do this local

**[12:46]** things. So you could do this local

**[12:46]** things. So you could do this local connection or something like Squabert

**[12:48]** connection or something like Squabert

**[12:48]** connection or something like Squabert could connect to a server um up running

**[12:51]** could connect to a server um up running

**[12:51]** could connect to a server um up running on another in the cloud and do all the

**[12:54]** on another in the cloud and do all the

**[12:54]** on another in the cloud and do all the AI stuff. And then the third option is

**[12:55]** AI stuff. And then the third option is

**[12:55]** AI stuff. And then the third option is you can go and connect up to something

**[12:57]** you can go and connect up to something

**[12:57]** you can go and connect up to something like Pipcat and make it multi-party. So

**[12:59]** like Pipcat and make it multi-party. So

**[12:59]** like Pipcat and make it multi-party. So bring LLMs into meetings or other places


### [13:00 - 14:00]

**[13:01]** bring LLMs into meetings or other places

**[13:02]** bring LLMs into meetings or other places like that. Um super awesome how like you

**[13:04]** like that. Um super awesome how like you

**[13:04]** like that. Um super awesome how like you get all this flexibility to build these

**[13:06]** get all this flexibility to build these

**[13:06]** get all this flexibility to build these things the way that like matches your

**[13:07]** things the way that like matches your

**[13:07]** things the way that like matches your application.

**[13:09]** application.

**[13:09]** application. So we want to close the video with

**[13:11]** So we want to close the video with

**[13:11]** So we want to close the video with actually a builder who's in the

**[13:12]** actually a builder who's in the

**[13:12]** actually a builder who's in the audience. Um super excited and um what's

**[13:16]** audience. Um super excited and um what's

**[13:16]** audience. Um super excited and um what's the best part about this is that um when

**[13:18]** the best part about this is that um when

**[13:18]** the best part about this is that um when she built this she had never rewritten

**[13:20]** she built this she had never rewritten

**[13:20]** she built this she had never rewritten any code before this. And so what makes

**[13:21]** any code before this. And so what makes

**[13:21]** any code before this. And so what makes me so excited about the future of voice

**[13:23]** me so excited about the future of voice

**[13:23]** me so excited about the future of voice is if we can make this easy enough,

**[13:25]** is if we can make this easy enough,

**[13:25]** is if we can make this easy enough, people that have really innovative,

**[13:26]** people that have really innovative,

**[13:26]** people that have really innovative, inspirational ideas can go and do stuff

**[13:28]** inspirational ideas can go and do stuff

**[13:28]** inspirational ideas can go and do stuff themselves.

**[13:35]** Hi, I'm Yashin. I'm a mom of two

**[13:35]** Hi, I'm Yashin. I'm a mom of two bilingual kids. I'm raising my kids

**[13:38]** bilingual kids. I'm raising my kids

**[13:38]** bilingual kids. I'm raising my kids bilingual because I want them to connect

**[13:40]** bilingual because I want them to connect

**[13:40]** bilingual because I want them to connect with my cultural roots and that's a wish

**[13:43]** with my cultural roots and that's a wish

**[13:43]** with my cultural roots and that's a wish shared by many parents of bilingual

**[13:45]** shared by many parents of bilingual

**[13:45]** shared by many parents of bilingual children. But raising bilingual kids is

**[13:47]** children. But raising bilingual kids is

**[13:48]** children. But raising bilingual kids is hard. It's expensive. It's consuming and

**[13:51]** hard. It's expensive. It's consuming and

**[13:51]** hard. It's expensive. It's consuming and it often feels like a big chore on both

**[13:53]** it often feels like a big chore on both

**[13:53]** it often feels like a big chore on both the kids and parents. I believe we can

**[13:56]** the kids and parents. I believe we can

**[13:56]** the kids and parents. I believe we can do a lot better with today's technology.


### [14:00 - 15:00]

**[14:00]** do a lot better with today's technology.

**[14:00]** do a lot better with today's technology. I really believe we can make language

**[14:02]** I really believe we can make language

**[14:02]** I really believe we can make language education feel more natural and even fun

**[14:05]** education feel more natural and even fun

**[14:05]** education feel more natural and even fun for the kids. Here's a quick clip of

**[14:07]** for the kids. Here's a quick clip of

**[14:07]** for the kids. Here's a quick clip of what I've been working on.

**[14:13]** Hi there buddy. Ready to have some fun

**[14:13]** Hi there buddy. Ready to have some fun today?

**[14:27]** How about we start with something fun?

**[14:27]** How about we start with something fun? Let's say hello. In Mandarin, we say,

**[14:31]** Let's say hello. In Mandarin, we say,

**[14:31]** Let's say hello. In Mandarin, we say, can you say,

**[14:38]** okay, it's still early, but I'm excited

**[14:38]** okay, it's still early, but I'm excited about what's possible. I'm not

**[14:41]** about what's possible. I'm not

**[14:41]** about what's possible. I'm not technical, but with just a little bit of

**[14:43]** technical, but with just a little bit of

**[14:43]** technical, but with just a little bit of guidance from a kind member of this

**[14:45]** guidance from a kind member of this

**[14:45]** guidance from a kind member of this community, I was able to bring this

**[14:48]** community, I was able to bring this

**[14:48]** community, I was able to bring this first version to life.

**[14:51]** first version to life.

**[14:51]** first version to life. I already have a group of eager testers,

**[14:53]** I already have a group of eager testers,

**[14:54]** I already have a group of eager testers, mostly parents like me, who are excited

**[14:56]** mostly parents like me, who are excited

**[14:56]** mostly parents like me, who are excited to try this. If this also sounds

**[14:59]** to try this. If this also sounds

**[14:59]** to try this. If this also sounds exciting to you, I would love to


### [15:00 - 16:00]

**[15:01]** exciting to you, I would love to

**[15:01]** exciting to you, I would love to connect. Thanks so much for watching and

**[15:04]** connect. Thanks so much for watching and

**[15:04]** connect. Thanks so much for watching and let's build this future together.

**[15:13]** [Applause]

**[15:13]** [Applause] So, we put the QR code up here for

**[15:14]** So, we put the QR code up here for

**[15:14]** So, we put the QR code up here for Yashin's project, which I absolutely

**[15:16]** Yashin's project, which I absolutely

**[15:16]** Yashin's project, which I absolutely love. She's here. Uh, if you're

**[15:18]** love. She's here. Uh, if you're

**[15:18]** love. She's here. Uh, if you're interested, if you're here in the

**[15:19]** interested, if you're here in the

**[15:20]** interested, if you're here in the audience and, uh, you're interested in

**[15:21]** audience and, uh, you're interested in

**[15:22]** audience and, uh, you're interested in multilingual stuff or building these

**[15:23]** multilingual stuff or building these

**[15:23]** multilingual stuff or building these kind of things, please find her. It's

**[15:25]** kind of things, please find her. It's

**[15:26]** kind of things, please find her. It's such a great great great thing. Um, if

**[15:28]** such a great great great thing. Um, if

**[15:28]** such a great great great thing. Um, if you're watching on YouTube, here's the

**[15:30]** you're watching on YouTube, here's the

**[15:30]** you're watching on YouTube, here's the QR code. Sean and I are super excited

**[15:32]** QR code. Sean and I are super excited

**[15:32]** QR code. Sean and I are super excited about these kind of projects. And I mean

**[15:34]** about these kind of projects. And I mean

**[15:34]** about these kind of projects. And I mean the the person Yashin shouted out in the

**[15:37]** the the person Yashin shouted out in the

**[15:37]** the the person Yashin shouted out in the video is of course Sean who has done

**[15:39]** video is of course Sean who has done

**[15:39]** video is of course Sean who has done more than anybody I know to make WebRTC

**[15:41]** more than anybody I know to make WebRTC

**[15:41]** more than anybody I know to make WebRTC accessible to everyone. Um the idea that

**[15:44]** accessible to everyone. Um the idea that

**[15:44]** accessible to everyone. Um the idea that we want to leave you with is if you have

**[15:45]** we want to leave you with is if you have

**[15:46]** we want to leave you with is if you have an idea in voice AI and WebRTC whether

**[15:48]** an idea in voice AI and WebRTC whether

**[15:48]** an idea in voice AI and WebRTC whether you've been a programmer for years or

**[15:50]** you've been a programmer for years or

**[15:50]** you've been a programmer for years or you're just getting started like we are

**[15:52]** you're just getting started like we are

**[15:52]** you're just getting started like we are here to support you. We're so excited

**[15:54]** here to support you. We're so excited

**[15:54]** here to support you. We're so excited and we believe that things like Pipecat

**[15:56]** and we believe that things like Pipecat

**[15:56]** and we believe that things like Pipecat and Lip Pier like if we can make this

**[15:58]** and Lip Pier like if we can make this

**[15:58]** and Lip Pier like if we can make this easier we're going to see the next


### [16:00 - 17:00]

**[16:00]** easier we're going to see the next

**[16:00]** easier we're going to see the next generation of really exciting innovative

**[16:02]** generation of really exciting innovative

**[16:02]** generation of really exciting innovative projects. come find us in the hallway or

**[16:04]** projects. come find us in the hallway or

**[16:04]** projects. come find us in the hallway or online. We hang out on Discord and

**[16:05]** online. We hang out on Discord and

**[16:05]** online. We hang out on Discord and Twitter and LinkedIn. And uh here are

**[16:08]** Twitter and LinkedIn. And uh here are

**[16:08]** Twitter and LinkedIn. And uh here are the resources that you can scan and uh

**[16:10]** the resources that you can scan and uh

**[16:10]** the resources that you can scan and uh hopefully they find helpful. So Quinn

**[16:12]** hopefully they find helpful. So Quinn

**[16:12]** hopefully they find helpful. So Quinn wrote an amazing book that I believe is

**[16:13]** wrote an amazing book that I believe is

**[16:13]** wrote an amazing book that I believe is in your bag. Um and then uh yeah, so

**[16:17]** in your bag. Um and then uh yeah, so

**[16:17]** in your bag. Um and then uh yeah, so thank you so much. We can't wait to see

**[16:19]** thank you so much. We can't wait to see

**[16:19]** thank you so much. We can't wait to see what you build.

**[16:22]** what you build.

**[16:22]** what you build. [Applause]


