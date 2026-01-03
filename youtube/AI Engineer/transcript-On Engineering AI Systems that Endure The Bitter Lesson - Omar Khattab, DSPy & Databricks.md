# On Engineering AI Systems that Endure The Bitter Lesson - Omar Khattab, DSPy & Databricks

**Video URL:** https://www.youtube.com/watch?v=qdmxApz3EJI

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** So, thanks everyone for showing up and

**[00:17]** So, thanks everyone for showing up and uh thanks to the organizers for inviting

**[00:19]** uh thanks to the organizers for inviting

**[00:19]** uh thanks to the organizers for inviting me and having me here. Um I'm excited to

**[00:22]** me and having me here. Um I'm excited to

**[00:22]** me and having me here. Um I'm excited to talk to you all about uh engineering AI

**[00:25]** talk to you all about uh engineering AI

**[00:25]** talk to you all about uh engineering AI systems that endure the bitter lesson.

**[00:28]** systems that endure the bitter lesson.

**[00:28]** systems that endure the bitter lesson. So, MMOR, uh, I guess the intro has

**[00:31]** So, MMOR, uh, I guess the intro has

**[00:31]** So, MMOR, uh, I guess the intro has already happened, so let's not repeat

**[00:32]** already happened, so let's not repeat

**[00:32]** already happened, so let's not repeat that. So, I mean, if you're here, I

**[00:35]** that. So, I mean, if you're here, I

**[00:35]** that. So, I mean, if you're here, I think it's probably because you engineer

**[00:37]** think it's probably because you engineer

**[00:37]** think it's probably because you engineer what we might call AI software or you

**[00:39]** what we might call AI software or you

**[00:39]** what we might call AI software or you might maybe manage people or work with

**[00:41]** might maybe manage people or work with

**[00:41]** might maybe manage people or work with people that do. Um, it's not really a

**[00:44]** people that do. Um, it's not really a

**[00:44]** people that do. Um, it's not really a term that's like been used as a very

**[00:46]** term that's like been used as a very

**[00:46]** term that's like been used as a very special thing this way for that long.

**[00:49]** special thing this way for that long.

**[00:49]** special thing this way for that long. So, we're all kind of trying to figure

**[00:51]** So, we're all kind of trying to figure

**[00:51]** So, we're all kind of trying to figure out what are the right sort of uh basics

**[00:53]** out what are the right sort of uh basics

**[00:53]** out what are the right sort of uh basics and fundamentals here and what are the

**[00:55]** and fundamentals here and what are the

**[00:55]** and fundamentals here and what are the things that are fleeting. So this is

**[00:56]** things that are fleeting. So this is

**[00:56]** things that are fleeting. So this is what the talk will be uh largely about

**[00:59]** what the talk will be uh largely about

**[00:59]** what the talk will be uh largely about and you know like the name of the game


### [01:00 - 02:00]

**[01:01]** and you know like the name of the game

**[01:01]** and you know like the name of the game is which is kind of a meme at this

**[01:03]** is which is kind of a meme at this

**[01:03]** is which is kind of a meme at this point. Every week there's a new large

**[01:04]** point. Every week there's a new large

**[01:04]** point. Every week there's a new large language model. Maybe every week is

**[01:06]** language model. Maybe every week is

**[01:06]** language model. Maybe every week is actually too slow at this point. Um that

**[01:08]** actually too slow at this point. Um that

**[01:08]** actually too slow at this point. Um that actually changes something um in terms

**[01:10]** actually changes something um in terms

**[01:10]** actually changes something um in terms of the trade-offs you can strike. It

**[01:12]** of the trade-offs you can strike. It

**[01:12]** of the trade-offs you can strike. It might not be the state-of-the-art in

**[01:14]** might not be the state-of-the-art in

**[01:14]** might not be the state-of-the-art in terms of the best quality necessarily

**[01:15]** terms of the best quality necessarily

**[01:16]** terms of the best quality necessarily although sometimes it is. Um, but maybe

**[01:18]** although sometimes it is. Um, but maybe

**[01:18]** although sometimes it is. Um, but maybe it's the best performance for certain

**[01:20]** it's the best performance for certain

**[01:20]** it's the best performance for certain costs or it's the best performance for

**[01:22]** costs or it's the best performance for

**[01:22]** costs or it's the best performance for certain types of applications or maybe

**[01:24]** certain types of applications or maybe

**[01:24]** certain types of applications or maybe it's the, you know, the speed that's

**[01:25]** it's the, you know, the speed that's

**[01:25]** it's the, you know, the speed that's really incredible. We've seen like

**[01:27]** really incredible. We've seen like

**[01:27]** really incredible. We've seen like things like, you know, diffusion now.

**[01:28]** things like, you know, diffusion now.

**[01:28]** things like, you know, diffusion now. Um, so every every week there's a new

**[01:31]** Um, so every every week there's a new

**[01:31]** Um, so every every week there's a new LLM that you kind of have to think about

**[01:32]** LLM that you kind of have to think about

**[01:32]** LLM that you kind of have to think about if you're engineering software in this

**[01:34]** if you're engineering software in this

**[01:34]** if you're engineering software in this space, which is really unusual. Like if

**[01:35]** space, which is really unusual. Like if

**[01:35]** space, which is really unusual. Like if you think back to normal software

**[01:37]** you think back to normal software

**[01:37]** you think back to normal software engineering, you change your hardware

**[01:39]** engineering, you change your hardware

**[01:39]** engineering, you change your hardware every two, three years maybe, um, if

**[01:41]** every two, three years maybe, um, if

**[01:41]** every two, three years maybe, um, if that. So this is pretty unusual. Um, the

**[01:44]** that. So this is pretty unusual. Um, the

**[01:44]** that. So this is pretty unusual. Um, the other part that's actually also a little

**[01:46]** other part that's actually also a little

**[01:46]** other part that's actually also a little bit weirder is if you're lucky, the LLM

**[01:50]** bit weirder is if you're lucky, the LLM

**[01:50]** bit weirder is if you're lucky, the LLM provider has recognized that they're not

**[01:52]** provider has recognized that they're not

**[01:52]** provider has recognized that they're not really building these LLMs. They're

**[01:54]** really building these LLMs. They're

**[01:54]** really building these LLMs. They're training them. They're emerging based on

**[01:57]** training them. They're emerging based on

**[01:57]** training them. They're emerging based on a lot of nudging and data and iterating


### [02:00 - 03:00]

**[02:00]** a lot of nudging and data and iterating

**[02:00]** a lot of nudging and data and iterating on a lot of evals and a lot of vibes as

**[02:02]** on a lot of evals and a lot of vibes as

**[02:02]** on a lot of evals and a lot of vibes as well. Um, and they have realized, you

**[02:05]** well. Um, and they have realized, you

**[02:05]** well. Um, and they have realized, you know, if you're lucky, that there are

**[02:06]** know, if you're lucky, that there are

**[02:06]** know, if you're lucky, that there are new quirks in their latest models that

**[02:08]** new quirks in their latest models that

**[02:08]** new quirks in their latest models that weren't there before. And to the

**[02:09]** weren't there before. And to the

**[02:09]** weren't there before. And to the surprise of many people to these days,

**[02:11]** surprise of many people to these days,

**[02:11]** surprise of many people to these days, you know, you still get longer and

**[02:13]** you know, you still get longer and

**[02:13]** you know, you still get longer and longer prompting guides for the latest

**[02:15]** longer prompting guides for the latest

**[02:15]** longer prompting guides for the latest models that are supposed to be, you

**[02:16]** models that are supposed to be, you

**[02:16]** models that are supposed to be, you know, closer and closer to AGI. Um, and

**[02:19]** know, closer and closer to AGI. Um, and

**[02:19]** know, closer and closer to AGI. Um, and if you're less lucky, you have to figure

**[02:20]** if you're less lucky, you have to figure

**[02:20]** if you're less lucky, you have to figure that out on your own, right? Um, if

**[02:23]** that out on your own, right? Um, if

**[02:23]** that out on your own, right? Um, if you're even less lucky, the prompting

**[02:24]** you're even less lucky, the prompting

**[02:24]** you're even less lucky, the prompting guides from the provider are not even

**[02:25]** guides from the provider are not even

**[02:25]** guides from the provider are not even that good. So, you have to actually kind

**[02:27]** that good. So, you have to actually kind

**[02:27]** that good. So, you have to actually kind of figure out what what the right thing

**[02:28]** of figure out what what the right thing

**[02:28]** of figure out what what the right thing is. And every day uh maybe at an even

**[02:31]** is. And every day uh maybe at an even

**[02:31]** is. And every day uh maybe at an even faster pace, someone is releasing an

**[02:33]** faster pace, someone is releasing an

**[02:33]** faster pace, someone is releasing an archive paper or a tweet or something

**[02:35]** archive paper or a tweet or something

**[02:35]** archive paper or a tweet or something that introduces a new learning

**[02:37]** that introduces a new learning

**[02:37]** that introduces a new learning algorithm, maybe some reinforcement

**[02:38]** algorithm, maybe some reinforcement

**[02:38]** algorithm, maybe some reinforcement learning uh bells and whistles, maybe

**[02:40]** learning uh bells and whistles, maybe

**[02:40]** learning uh bells and whistles, maybe some prompting tricks, maybe a prompt

**[02:42]** some prompting tricks, maybe a prompt

**[02:42]** some prompting tricks, maybe a prompt optimization, you know, technique,

**[02:44]** optimization, you know, technique,

**[02:44]** optimization, you know, technique, something or the other that promises to

**[02:46]** something or the other that promises to

**[02:46]** something or the other that promises to make your system learn better and sort

**[02:48]** make your system learn better and sort

**[02:48]** make your system learn better and sort of fit your goals better. Someone else

**[02:50]** of fit your goals better. Someone else

**[02:50]** of fit your goals better. Someone else is introducing some search or scaling or

**[02:52]** is introducing some search or scaling or

**[02:52]** is introducing some search or scaling or inference strategies or agent frameworks

**[02:55]** inference strategies or agent frameworks

**[02:55]** inference strategies or agent frameworks or agent architectures that are

**[02:57]** or agent architectures that are

**[02:57]** or agent architectures that are promising to finally unlock levels of

**[02:58]** promising to finally unlock levels of

**[02:58]** promising to finally unlock levels of reliability or quality better than what


### [03:00 - 04:00]

**[03:00]** reliability or quality better than what

**[03:00]** reliability or quality better than what you had before. And I think if you're

**[03:03]** you had before. And I think if you're

**[03:03]** you had before. And I think if you're actually doing a reasonable job now,

**[03:05]** actually doing a reasonable job now,

**[03:05]** actually doing a reasonable job now, most likely you're scrambling every

**[03:06]** most likely you're scrambling every

**[03:06]** most likely you're scrambling every week. That's not if you're doing a bad

**[03:07]** week. That's not if you're doing a bad

**[03:07]** week. That's not if you're doing a bad job, that's if you're doing a good job,

**[03:09]** job, that's if you're doing a good job,

**[03:09]** job, that's if you're doing a good job, right? Because you're like, you know,

**[03:10]** right? Because you're like, you know,

**[03:10]** right? Because you're like, you know, I've got to stay on top of at least some

**[03:12]** I've got to stay on top of at least some

**[03:12]** I've got to stay on top of at least some of this stuff so that like I don't fall

**[03:14]** of this stuff so that like I don't fall

**[03:14]** of this stuff so that like I don't fall behind. Um, and in many cases like you

**[03:17]** behind. Um, and in many cases like you

**[03:17]** behind. Um, and in many cases like you know model APIs actually change the

**[03:19]** know model APIs actually change the

**[03:19]** know model APIs actually change the model under the hood even though you

**[03:20]** model under the hood even though you

**[03:20]** model under the hood even though you know you're using the same name. So it's

**[03:22]** know you're using the same name. So it's

**[03:22]** know you're using the same name. So it's actually you're forced to scramble

**[03:25]** actually you're forced to scramble

**[03:25]** actually you're forced to scramble and actually I would say maybe the

**[03:26]** and actually I would say maybe the

**[03:26]** and actually I would say maybe the question isn't whether you will scramble

**[03:28]** question isn't whether you will scramble

**[03:28]** question isn't whether you will scramble every week maybe a different question is

**[03:30]** every week maybe a different question is

**[03:30]** every week maybe a different question is will you even get to scramble for long

**[03:32]** will you even get to scramble for long

**[03:32]** will you even get to scramble for long if you think about the rate of progress

**[03:34]** if you think about the rate of progress

**[03:34]** if you think about the rate of progress of these LLMs like are they going to eat

**[03:35]** of these LLMs like are they going to eat

**[03:35]** of these LLMs like are they going to eat your lunch right so these are I think

**[03:37]** your lunch right so these are I think

**[03:37]** your lunch right so these are I think questions that are on a lot of people's

**[03:39]** questions that are on a lot of people's

**[03:39]** questions that are on a lot of people's minds and this is what the talk is is is

**[03:40]** minds and this is what the talk is is is

**[03:40]** minds and this is what the talk is is is going to be addressing so the talk

**[03:42]** going to be addressing so the talk

**[03:42]** going to be addressing so the talk mentions the bitter lesson which is

**[03:44]** mentions the bitter lesson which is

**[03:44]** mentions the bitter lesson which is sounds like this you know really ancient

**[03:45]** sounds like this you know really ancient

**[03:46]** sounds like this you know really ancient old kind of um AI lore but it's just you

**[03:48]** old kind of um AI lore but it's just you

**[03:48]** old kind of um AI lore but it's just you know six years old uh where the current

**[03:51]** know six years old uh where the current

**[03:51]** know six years old uh where the current years uh Turing award winner Rich Sutton

**[03:53]** years uh Turing award winner Rich Sutton

**[03:53]** years uh Turing award winner Rich Sutton who's a pioneer of reinforcement

**[03:55]** who's a pioneer of reinforcement

**[03:55]** who's a pioneer of reinforcement learning wrote this short essay uh on

**[03:57]** learning wrote this short essay uh on

**[03:57]** learning wrote this short essay uh on his website basically that says 70 years


### [04:00 - 05:00]

**[04:00]** his website basically that says 70 years

**[04:00]** his website basically that says 70 years of AI has taught him and taught you know

**[04:02]** of AI has taught him and taught you know

**[04:02]** of AI has taught him and taught you know other people in the AI community from

**[04:03]** other people in the AI community from

**[04:03]** other people in the AI community from his perspective that when AI researchers

**[04:06]** his perspective that when AI researchers

**[04:06]** his perspective that when AI researchers leverage domain knowledge to solve

**[04:08]** leverage domain knowledge to solve

**[04:08]** leverage domain knowledge to solve problems like I don't know chess or

**[04:10]** problems like I don't know chess or

**[04:10]** problems like I don't know chess or something we build complicated methods

**[04:12]** something we build complicated methods

**[04:12]** something we build complicated methods that essentially don't scale and we get

**[04:14]** that essentially don't scale and we get

**[04:14]** that essentially don't scale and we get stuck and we get beat by methods that

**[04:16]** stuck and we get beat by methods that

**[04:16]** stuck and we get beat by methods that leverage scale a lot better what seems

**[04:19]** leverage scale a lot better what seems

**[04:19]** leverage scale a lot better what seems to have to work better according to uh

**[04:21]** to have to work better according to uh

**[04:21]** to have to work better according to uh to Sutton is general methods that scale

**[04:23]** to Sutton is general methods that scale

**[04:23]** to Sutton is general methods that scale and he identifies search which is not

**[04:25]** and he identifies search which is not

**[04:25]** and he identifies search which is not like retrieval more of like uh you know

**[04:27]** like retrieval more of like uh you know

**[04:27]** like retrieval more of like uh you know exploring large spaces and learning um

**[04:30]** exploring large spaces and learning um

**[04:30]** exploring large spaces and learning um so getting the system to kind of

**[04:31]** so getting the system to kind of

**[04:32]** so getting the system to kind of understand its environment maybe for

**[04:33]** understand its environment maybe for

**[04:33]** understand its environment maybe for example um work best and search here is

**[04:36]** example um work best and search here is

**[04:36]** example um work best and search here is what we'd call in LM land maybe

**[04:38]** what we'd call in LM land maybe

**[04:38]** what we'd call in LM land maybe inference time scaling or something so I

**[04:40]** inference time scaling or something so I

**[04:40]** inference time scaling or something so I don't speak for Sutton and I'm not you

**[04:42]** don't speak for Sutton and I'm not you

**[04:42]** don't speak for Sutton and I'm not you know suggesting that I have the right

**[04:44]** know suggesting that I have the right

**[04:44]** know suggesting that I have the right understanding of what he's saying or

**[04:45]** understanding of what he's saying or

**[04:45]** understanding of what he's saying or that I necessarily agree or disagree but

**[04:46]** that I necessarily agree or disagree but

**[04:46]** that I necessarily agree or disagree but I think this is just fundamental and

**[04:48]** I think this is just fundamental and

**[04:48]** I think this is just fundamental and important kind of um um concept in

**[04:50]** important kind of um um concept in

**[04:50]** important kind of um um concept in space. So I think it's it's it raises

**[04:53]** space. So I think it's it's it raises

**[04:53]** space. So I think it's it's it raises interesting questions for us as people

**[04:55]** interesting questions for us as people

**[04:55]** interesting questions for us as people who build uh you know engineer AI

**[04:57]** who build uh you know engineer AI

**[04:57]** who build uh you know engineer AI systems because if leveraging domain

**[04:59]** systems because if leveraging domain

**[04:59]** systems because if leveraging domain knowledge is bad what exactly is AI


### [05:00 - 06:00]

**[05:01]** knowledge is bad what exactly is AI

**[05:01]** knowledge is bad what exactly is AI engineering supposed to be about? I mean

**[05:03]** engineering supposed to be about? I mean

**[05:03]** engineering supposed to be about? I mean engineering is understanding your domain

**[05:04]** engineering is understanding your domain

**[05:04]** engineering is understanding your domain and working in it with a lot of human

**[05:06]** and working in it with a lot of human

**[05:06]** and working in it with a lot of human ingenuity in repeatable ways let's say

**[05:08]** ingenuity in repeatable ways let's say

**[05:08]** ingenuity in repeatable ways let's say or with principles. So like are we just

**[05:11]** or with principles. So like are we just

**[05:11]** or with principles. So like are we just doomed like are we just wasting our

**[05:12]** doomed like are we just wasting our

**[05:12]** doomed like are we just wasting our time? Why are we at an AI engineering

**[05:14]** time? Why are we at an AI engineering

**[05:14]** time? Why are we at an AI engineering you know fair? And I'll tell you um how

**[05:17]** you know fair? And I'll tell you um how

**[05:17]** you know fair? And I'll tell you um how to resolve this. I've not really seen a

**[05:18]** to resolve this. I've not really seen a

**[05:18]** to resolve this. I've not really seen a lot of people discuss that. Sutton is

**[05:20]** lot of people discuss that. Sutton is

**[05:20]** lot of people discuss that. Sutton is talking about and a lot of people, you

**[05:21]** talking about and a lot of people, you

**[05:21]** talking about and a lot of people, you know, throw the bitter lesson around. So

**[05:23]** know, throw the bitter lesson around. So

**[05:23]** know, throw the bitter lesson around. So clearly somebody has to think about

**[05:24]** clearly somebody has to think about

**[05:24]** clearly somebody has to think about this, right? Sutton is talking about

**[05:25]** this, right? Sutton is talking about

**[05:25]** this, right? Sutton is talking about maximizing intelligence. All of us

**[05:28]** maximizing intelligence. All of us

**[05:28]** maximizing intelligence. All of us probably care about that to some degree,

**[05:29]** probably care about that to some degree,

**[05:29]** probably care about that to some degree, but which is like something like the

**[05:30]** but which is like something like the

**[05:30]** but which is like something like the ability to figure things out in a new

**[05:32]** ability to figure things out in a new

**[05:32]** ability to figure things out in a new environment really fast, let's say. Um,

**[05:34]** environment really fast, let's say. Um,

**[05:34]** environment really fast, let's say. Um, all of us kind of care about this to

**[05:36]** all of us kind of care about this to

**[05:36]** all of us kind of care about this to some degree. I'm also an AI researcher.

**[05:38]** some degree. I'm also an AI researcher.

**[05:38]** some degree. I'm also an AI researcher. Um, but when we're building AI systems,

**[05:40]** Um, but when we're building AI systems,

**[05:40]** Um, but when we're building AI systems, I think it's important to remember that

**[05:42]** I think it's important to remember that

**[05:42]** I think it's important to remember that the reason we build software is not that

**[05:44]** the reason we build software is not that

**[05:44]** the reason we build software is not that we lack AGI. We build software um you

**[05:47]** we lack AGI. We build software um you

**[05:47]** we lack AGI. We build software um you know and and the reason for this and the

**[05:48]** know and and the reason for this and the

**[05:48]** know and and the reason for this and the way kind of to understand this is we

**[05:50]** way kind of to understand this is we

**[05:50]** way kind of to understand this is we already have general intelligence

**[05:52]** already have general intelligence

**[05:52]** already have general intelligence everywhere. We have eight billions of

**[05:53]** everywhere. We have eight billions of

**[05:53]** everywhere. We have eight billions of them. Um they're unreliable because

**[05:55]** them. Um they're unreliable because

**[05:55]** them. Um they're unreliable because that's what intelligence is. Um and

**[05:57]** that's what intelligence is. Um and

**[05:57]** that's what intelligence is. Um and they've not solve the problems that we

**[05:58]** they've not solve the problems that we

**[05:58]** they've not solve the problems that we want to solve with software. That's why

**[05:59]** want to solve with software. That's why

**[05:59]** want to solve with software. That's why we're building software. Um so we


### [06:00 - 07:00]

**[06:02]** we're building software. Um so we

**[06:02]** we're building software. Um so we program software not because we lack AGI

**[06:04]** program software not because we lack AGI

**[06:04]** program software not because we lack AGI but because we want reliable, robust,

**[06:07]** but because we want reliable, robust,

**[06:07]** but because we want reliable, robust, controllable uh scalable systems. Um and

**[06:10]** controllable uh scalable systems. Um and

**[06:10]** controllable uh scalable systems. Um and we want these things that to be things

**[06:12]** we want these things that to be things

**[06:12]** we want these things that to be things that we can reason about, understand at

**[06:14]** that we can reason about, understand at

**[06:14]** that we can reason about, understand at scale. Um and actually if you think

**[06:16]** scale. Um and actually if you think

**[06:16]** scale. Um and actually if you think about engineering and reliable systems,

**[06:17]** about engineering and reliable systems,

**[06:17]** about engineering and reliable systems, if you think about checks and balances

**[06:18]** if you think about checks and balances

**[06:18]** if you think about checks and balances in any case where you try to systematize

**[06:20]** in any case where you try to systematize

**[06:20]** in any case where you try to systematize stuff, it's about subtracting agency and

**[06:23]** stuff, it's about subtracting agency and

**[06:23]** stuff, it's about subtracting agency and subtracting intelligence in exactly the

**[06:25]** subtracting intelligence in exactly the

**[06:25]** subtracting intelligence in exactly the right places uh carefully uh and not

**[06:28]** right places uh carefully uh and not

**[06:28]** right places uh carefully uh and not restricting the intelligence otherwise.

**[06:29]** restricting the intelligence otherwise.

**[06:29]** restricting the intelligence otherwise. So this is a very different axis from

**[06:31]** So this is a very different axis from

**[06:31]** So this is a very different axis from the kinds of lessons that you would draw

**[06:33]** the kinds of lessons that you would draw

**[06:33]** the kinds of lessons that you would draw on from the bitter lesson. Now that does

**[06:35]** on from the bitter lesson. Now that does

**[06:35]** on from the bitter lesson. Now that does not mean the bitter lesson is

**[06:36]** not mean the bitter lesson is

**[06:36]** not mean the bitter lesson is irrelevant. Let me tell you the precise

**[06:38]** irrelevant. Let me tell you the precise

**[06:38]** irrelevant. Let me tell you the precise way in which it's relevant. Um so the

**[06:40]** way in which it's relevant. Um so the

**[06:40]** way in which it's relevant. Um so the first takeaway here is that scaling

**[06:41]** first takeaway here is that scaling

**[06:42]** first takeaway here is that scaling search and learning works best for

**[06:43]** search and learning works best for

**[06:43]** search and learning works best for intelligence. This is the right thing to

**[06:45]** intelligence. This is the right thing to

**[06:45]** intelligence. This is the right thing to do if you're an AI researcher interested

**[06:46]** do if you're an AI researcher interested

**[06:46]** do if you're an AI researcher interested in building, you know, agents that learn

**[06:48]** in building, you know, agents that learn

**[06:48]** in building, you know, agents that learn really well really fast in new

**[06:49]** really well really fast in new

**[06:49]** really well really fast in new environments, right? Don't hard code

**[06:51]** environments, right? Don't hard code

**[06:51]** environments, right? Don't hard code stuff at all. Um, or unless you really

**[06:54]** stuff at all. Um, or unless you really

**[06:54]** stuff at all. Um, or unless you really have to. But in building AI systems,

**[06:56]** have to. But in building AI systems,

**[06:56]** have to. But in building AI systems, it's helpful to think about, well, sure,

**[06:59]** it's helpful to think about, well, sure,

**[06:59]** it's helpful to think about, well, sure, search and learning, but searching for


### [07:00 - 08:00]

**[07:00]** search and learning, but searching for

**[07:00]** search and learning, but searching for what, right? Like what is your AI system

**[07:02]** what, right? Like what is your AI system

**[07:02]** what, right? Like what is your AI system even supposed to be doing? What is the

**[07:04]** even supposed to be doing? What is the

**[07:04]** even supposed to be doing? What is the the the fundamental problem that you're

**[07:06]** the the fundamental problem that you're

**[07:06]** the the fundamental problem that you're solving? It's not intelligence. It's

**[07:07]** solving? It's not intelligence. It's

**[07:07]** solving? It's not intelligence. It's something else. Um, and what are you

**[07:09]** something else. Um, and what are you

**[07:09]** something else. Um, and what are you learning for, right? Like what is the

**[07:11]** learning for, right? Like what is the

**[07:11]** learning for, right? Like what is the system learning in order to do well? And

**[07:13]** system learning in order to do well? And

**[07:13]** system learning in order to do well? And that is what you need to be engineering.

**[07:15]** that is what you need to be engineering.

**[07:15]** that is what you need to be engineering. Um not the specifics of search and not

**[07:17]** Um not the specifics of search and not

**[07:17]** Um not the specifics of search and not the specifics of learning as I'll talk

**[07:18]** the specifics of learning as I'll talk

**[07:18]** the specifics of learning as I'll talk about in the rest of this talk. So he's

**[07:21]** about in the rest of this talk. So he's

**[07:21]** about in the rest of this talk. So he's saying um Sutton is saying complicated

**[07:24]** saying um Sutton is saying complicated

**[07:24]** saying um Sutton is saying complicated methods get in the way of scaling uh

**[07:26]** methods get in the way of scaling uh

**[07:26]** methods get in the way of scaling uh especially if you do it early uh like

**[07:28]** especially if you do it early uh like

**[07:28]** especially if you do it early uh like before you know what you're doing

**[07:29]** before you know what you're doing

**[07:29]** before you know what you're doing essentially. Did you hear that before? I

**[07:31]** essentially. Did you hear that before? I

**[07:31]** essentially. Did you hear that before? I feel like I heard that back in the 1970s

**[07:33]** feel like I heard that back in the 1970s

**[07:33]** feel like I heard that back in the 1970s although I wasn't around. This is you

**[07:35]** although I wasn't around. This is you

**[07:35]** although I wasn't around. This is you know the notion of structured

**[07:36]** know the notion of structured

**[07:36]** know the notion of structured programming uh with with Kous saying his

**[07:39]** programming uh with with Kous saying his

**[07:39]** programming uh with with Kous saying his popular you know uh uh phrase in a paper

**[07:41]** popular you know uh uh phrase in a paper

**[07:42]** popular you know uh uh phrase in a paper premature optimization is the root of

**[07:44]** premature optimization is the root of

**[07:44]** premature optimization is the root of all evil. I think this is the bitter

**[07:46]** all evil. I think this is the bitter

**[07:46]** all evil. I think this is the bitter lesson for software and thereby also for

**[07:49]** lesson for software and thereby also for

**[07:49]** lesson for software and thereby also for AI software. So it's human ingenuity and

**[07:53]** AI software. So it's human ingenuity and

**[07:53]** AI software. So it's human ingenuity and human knowledge of the domain. It's not

**[07:55]** human knowledge of the domain. It's not

**[07:55]** human knowledge of the domain. It's not that it's harmful. It's that when you do

**[07:57]** that it's harmful. It's that when you do

**[07:57]** that it's harmful. It's that when you do it prematurely in ways that constrain

**[07:59]** it prematurely in ways that constrain

**[07:59]** it prematurely in ways that constrain your system in ways that reflect poor


### [08:00 - 09:00]

**[08:01]** your system in ways that reflect poor

**[08:01]** your system in ways that reflect poor understanding they're bad. But you can't

**[08:03]** understanding they're bad. But you can't

**[08:03]** understanding they're bad. But you can't get away in an engineering field with

**[08:05]** get away in an engineering field with

**[08:05]** get away in an engineering field with not engineering your system. Like you're

**[08:07]** not engineering your system. Like you're

**[08:07]** not engineering your system. Like you're just quitting or something, right? So

**[08:09]** just quitting or something, right? So

**[08:09]** just quitting or something, right? So here's a little piece of code. Um, if

**[08:11]** here's a little piece of code. Um, if

**[08:11]** here's a little piece of code. Um, if you follow me on X on Twitter, you might

**[08:13]** you follow me on X on Twitter, you might

**[08:13]** you follow me on X on Twitter, you might recognize it, but otherwise I think it

**[08:15]** recognize it, but otherwise I think it

**[08:15]** recognize it, but otherwise I think it looks pretty opaque to me in like 3

**[08:17]** looks pretty opaque to me in like 3

**[08:17]** looks pretty opaque to me in like 3 seconds. And I can't really look at this

**[08:18]** seconds. And I can't really look at this

**[08:18]** seconds. And I can't really look at this and tell exactly what it's doing. And I

**[08:20]** and tell exactly what it's doing. And I

**[08:20]** and tell exactly what it's doing. And I al also honestly don't really care. Um,

**[08:22]** al also honestly don't really care. Um,

**[08:22]** al also honestly don't really care. Um, so lo and behold, um, this is computing

**[08:25]** so lo and behold, um, this is computing

**[08:25]** so lo and behold, um, this is computing a square root in a certain floating

**[08:26]** a square root in a certain floating

**[08:26]** a square root in a certain floating point representation on an old machine.

**[08:28]** point representation on an old machine.

**[08:28]** point representation on an old machine. And I think the thing that jumps at me

**[08:30]** And I think the thing that jumps at me

**[08:30]** And I think the thing that jumps at me immediately is this is not the most

**[08:32]** immediately is this is not the most

**[08:32]** immediately is this is not the most futurep proof program possible. If you

**[08:34]** futurep proof program possible. If you

**[08:34]** futurep proof program possible. If you change the machine architecture,

**[08:36]** change the machine architecture,

**[08:36]** change the machine architecture, different floatingoint representations,

**[08:37]** different floatingoint representations,

**[08:37]** different floatingoint representations, better CPUs, first of all, it'll be

**[08:39]** better CPUs, first of all, it'll be

**[08:39]** better CPUs, first of all, it'll be wrong because, you know, like it's just

**[08:41]** wrong because, you know, like it's just

**[08:41]** wrong because, you know, like it's just hard- coding some values here. Um, and

**[08:43]** hard- coding some values here. Um, and

**[08:43]** hard- coding some values here. Um, and second of all, it'll probably be slower

**[08:45]** second of all, it'll probably be slower

**[08:45]** second of all, it'll probably be slower than a normal, you know, square root

**[08:46]** than a normal, you know, square root

**[08:46]** than a normal, you know, square root that maybe is a single instruction or

**[08:48]** that maybe is a single instruction or

**[08:48]** that maybe is a single instruction or maybe the compiler has a really smart

**[08:50]** maybe the compiler has a really smart

**[08:50]** maybe the compiler has a really smart way of doing it or, you know, a lot of

**[08:51]** way of doing it or, you know, a lot of

**[08:51]** way of doing it or, you know, a lot of other things that could be optimized for

**[08:53]** other things that could be optimized for

**[08:53]** other things that could be optimized for you, right? So someone who wrote this,

**[08:55]** you, right? So someone who wrote this,

**[08:55]** you, right? So someone who wrote this, maybe they had a good reason, maybe they

**[08:57]** maybe they had a good reason, maybe they

**[08:57]** maybe they had a good reason, maybe they didn't, but certainly if you're writing

**[08:59]** didn't, but certainly if you're writing

**[08:59]** didn't, but certainly if you're writing this kind of thing often, you're


### [09:00 - 10:00]

**[09:00]** this kind of thing often, you're

**[09:00]** this kind of thing often, you're probably messing up as an engineer.

**[09:03]** probably messing up as an engineer.

**[09:03]** probably messing up as an engineer. So premature optimization is maybe the

**[09:06]** So premature optimization is maybe the

**[09:06]** So premature optimization is maybe the um square root of all evil or something,

**[09:08]** um square root of all evil or something,

**[09:08]** um square root of all evil or something, but what counts as uh premature?

**[09:12]** but what counts as uh premature?

**[09:12]** but what counts as uh premature? Like I mean that's kind of the name of

**[09:13]** Like I mean that's kind of the name of

**[09:13]** Like I mean that's kind of the name of the game, right? Like we could just say

**[09:14]** the game, right? Like we could just say

**[09:14]** the game, right? Like we could just say that, but it doesn't mean anything. Um

**[09:16]** that, but it doesn't mean anything. Um

**[09:16]** that, but it doesn't mean anything. Um so I don't think any strategy will work

**[09:18]** so I don't think any strategy will work

**[09:18]** so I don't think any strategy will work in tech. Nobody can anticipate what will

**[09:20]** in tech. Nobody can anticipate what will

**[09:20]** in tech. Nobody can anticipate what will happen in three years, five years, 10

**[09:22]** happen in three years, five years, 10

**[09:22]** happen in three years, five years, 10 years. But I think you still have to

**[09:24]** years. But I think you still have to

**[09:24]** years. But I think you still have to have a conceptual model that you're

**[09:25]** have a conceptual model that you're

**[09:25]** have a conceptual model that you're working off of. And I happen to have

**[09:27]** working off of. And I happen to have

**[09:27]** working off of. And I happen to have built two things that are, you know, on

**[09:29]** built two things that are, you know, on

**[09:29]** built two things that are, you know, on the order of several years old that have

**[09:31]** the order of several years old that have

**[09:31]** the order of several years old that have fundamentally stayed the same over the

**[09:33]** fundamentally stayed the same over the

**[09:33]** fundamentally stayed the same over the years from the days of birth text

**[09:35]** years from the days of birth text

**[09:35]** years from the days of birth text Davinci 2 up to four 04 mini and they're

**[09:37]** Davinci 2 up to four 04 mini and they're

**[09:37]** Davinci 2 up to four 04 mini and they're bigger now than they ever were. And

**[09:39]** bigger now than they ever were. And

**[09:39]** bigger now than they ever were. And they're sort of like these um stable

**[09:41]** they're sort of like these um stable

**[09:41]** they're sort of like these um stable fundamental kind of um abstractions or

**[09:43]** fundamental kind of um abstractions or

**[09:43]** fundamental kind of um abstractions or AI systems around around LLMs. So what

**[09:46]** AI systems around around LLMs. So what

**[09:46]** AI systems around around LLMs. So what gives what happens u in order to get

**[09:49]** gives what happens u in order to get

**[09:49]** gives what happens u in order to get something like kulbear or something like

**[09:50]** something like kulbear or something like

**[09:50]** something like kulbear or something like the spy in this ecosystem um and sort of

**[09:53]** the spy in this ecosystem um and sort of

**[09:53]** the spy in this ecosystem um and sort of endure a few years which is like you

**[09:55]** endure a few years which is like you

**[09:55]** endure a few years which is like you know centuries in AI land um I'll try to

**[09:58]** know centuries in AI land um I'll try to

**[09:58]** know centuries in AI land um I'll try to reflect on this and you know again none


### [10:00 - 11:00]

**[10:00]** reflect on this and you know again none

**[10:00]** reflect on this and you know again none of this is guaranteed to be something

**[10:01]** of this is guaranteed to be something

**[10:02]** of this is guaranteed to be something that lasts forever. So here's my

**[10:03]** that lasts forever. So here's my

**[10:03]** that lasts forever. So here's my hypothesis um premature optimization is

**[10:05]** hypothesis um premature optimization is

**[10:05]** hypothesis um premature optimization is what is happening if and only if you're

**[10:08]** what is happening if and only if you're

**[10:08]** what is happening if and only if you're hard coding stuff at a lower level of

**[10:10]** hard coding stuff at a lower level of

**[10:10]** hard coding stuff at a lower level of abstraction that you can than you can

**[10:12]** abstraction that you can than you can

**[10:12]** abstraction that you can than you can justify. Um, if you want a square root,

**[10:15]** justify. Um, if you want a square root,

**[10:15]** justify. Um, if you want a square root, please just say, "Give me a square

**[10:16]** please just say, "Give me a square

**[10:16]** please just say, "Give me a square root." Don't start doing random bit

**[10:18]** root." Don't start doing random bit

**[10:18]** root." Don't start doing random bit shifts and bit stuff like, you know, bit

**[10:20]** shifts and bit stuff like, you know, bit

**[10:20]** shifts and bit stuff like, you know, bit manipulation that happens to appease

**[10:22]** manipulation that happens to appease

**[10:22]** manipulation that happens to appease your particular machine today. Um, but

**[10:25]** your particular machine today. Um, but

**[10:25]** your particular machine today. Um, but actually take a step back. Do you even

**[10:26]** actually take a step back. Do you even

**[10:26]** actually take a step back. Do you even want a square root or are you computing

**[10:28]** want a square root or are you computing

**[10:28]** want a square root or are you computing something even more general? And is

**[10:29]** something even more general? And is

**[10:29]** something even more general? And is there a way you could express that thing

**[10:31]** there a way you could express that thing

**[10:31]** there a way you could express that thing that is more general? Right? And only,

**[10:33]** that is more general? Right? And only,

**[10:33]** that is more general? Right? And only, you know, uh, stoop down or go down to

**[10:35]** you know, uh, stoop down or go down to

**[10:35]** you know, uh, stoop down or go down to the level of abstraction that's lower if

**[10:37]** the level of abstraction that's lower if

**[10:37]** the level of abstraction that's lower if you've demonstrated that a higher level

**[10:39]** you've demonstrated that a higher level

**[10:39]** you've demonstrated that a higher level of abstraction is not good enough.

**[10:42]** of abstraction is not good enough.

**[10:42]** of abstraction is not good enough. So I think the bigger picture here is

**[10:43]** So I think the bigger picture here is

**[10:43]** So I think the bigger picture here is applied machine learning and definitely

**[10:45]** applied machine learning and definitely

**[10:45]** applied machine learning and definitely prompt engineering has a huge issue

**[10:47]** prompt engineering has a huge issue

**[10:47]** prompt engineering has a huge issue here. Tight coupling is known tighter

**[10:50]** here. Tight coupling is known tighter

**[10:50]** here. Tight coupling is known tighter coupling than necessary is known to be

**[10:51]** coupling than necessary is known to be

**[10:51]** coupling than necessary is known to be bad in software but it's not really

**[10:52]** bad in software but it's not really

**[10:52]** bad in software but it's not really something we talk about when we're

**[10:54]** something we talk about when we're

**[10:54]** something we talk about when we're building machine learning systems. In

**[10:55]** building machine learning systems. In

**[10:55]** building machine learning systems. In fact the name of the game in machine

**[10:56]** fact the name of the game in machine

**[10:56]** fact the name of the game in machine learning is usually like hey this latest

**[10:59]** learning is usually like hey this latest

**[10:59]** learning is usually like hey this latest thing came out let's rewrite everything


### [11:00 - 12:00]

**[11:00]** thing came out let's rewrite everything

**[11:00]** thing came out let's rewrite everything so that we're working around that

**[11:01]** so that we're working around that

**[11:01]** so that we're working around that specific thing. And I tweeted about this

**[11:04]** specific thing. And I tweeted about this

**[11:04]** specific thing. And I tweeted about this a year ago, 13 months ago, last May in

**[11:06]** a year ago, 13 months ago, last May in

**[11:06]** a year ago, 13 months ago, last May in 2024, saying the bitter lesson is just

**[11:08]** 2024, saying the bitter lesson is just

**[11:08]** 2024, saying the bitter lesson is just an artifact of lacking high level good

**[11:10]** an artifact of lacking high level good

**[11:10]** an artifact of lacking high level good highle ML abstractions. Deep learning uh

**[11:14]** highle ML abstractions. Deep learning uh

**[11:14]** highle ML abstractions. Deep learning uh scaling deep learning helps predictably,

**[11:16]** scaling deep learning helps predictably,

**[11:16]** scaling deep learning helps predictably, but after every paradigm shift, the best

**[11:18]** but after every paradigm shift, the best

**[11:18]** but after every paradigm shift, the best systems always include modular

**[11:19]** systems always include modular

**[11:19]** systems always include modular specializations because we're trying to

**[11:20]** specializations because we're trying to

**[11:20]** specializations because we're trying to build software. We need those. Um and

**[11:23]** build software. We need those. Um and

**[11:23]** build software. We need those. Um and every time they basically look the same

**[11:24]** every time they basically look the same

**[11:24]** every time they basically look the same and they should have been reusable, but

**[11:25]** and they should have been reusable, but

**[11:26]** and they should have been reusable, but they're not because we're writing code

**[11:27]** they're not because we're writing code

**[11:27]** they're not because we're writing code bad, but we're writing bad code. So

**[11:29]** bad, but we're writing bad code. So

**[11:29]** bad, but we're writing bad code. So here's a nice example just to

**[11:31]** here's a nice example just to

**[11:31]** here's a nice example just to demonstrate this. It's not special at

**[11:32]** demonstrate this. It's not special at

**[11:32]** demonstrate this. It's not special at all. Here's a 2006 paper. The title

**[11:34]** all. Here's a 2006 paper. The title

**[11:34]** all. Here's a 2006 paper. The title could have really been a paper of now,

**[11:35]** could have really been a paper of now,

**[11:35]** could have really been a paper of now, right? A modular approach for

**[11:37]** right? A modular approach for

**[11:37]** right? A modular approach for multilingual question answering. And

**[11:39]** multilingual question answering. And

**[11:39]** multilingual question answering. And here's a system architecture. It looks

**[11:40]** here's a system architecture. It looks

**[11:40]** here's a system architecture. It looks like your favorite multi- aent framework

**[11:42]** like your favorite multi- aent framework

**[11:42]** like your favorite multi- aent framework today, right? It has an execution

**[11:43]** today, right? It has an execution

**[11:43]** today, right? It has an execution manager. It has some question analyzers

**[11:45]** manager. It has some question analyzers

**[11:45]** manager. It has some question analyzers and retrieval strategy strategists from

**[11:47]** and retrieval strategy strategists from

**[11:47]** and retrieval strategy strategists from a bunch of corpora. And it's like a

**[11:49]** a bunch of corpora. And it's like a

**[11:49]** a bunch of corpora. And it's like a figure you, you know, if you color it,

**[11:50]** figure you, you know, if you color it,

**[11:50]** figure you, you know, if you color it, you would think it's a paper maybe from

**[11:52]** you would think it's a paper maybe from

**[11:52]** you would think it's a paper maybe from last year or something. Um, now here's a

**[11:54]** last year or something. Um, now here's a

**[11:54]** last year or something. Um, now here's a problem. It's a pretty figure. The

**[11:56]** problem. It's a pretty figure. The

**[11:56]** problem. It's a pretty figure. The system architecturally is actually not

**[11:58]** system architecturally is actually not

**[11:58]** system architecturally is actually not that wrong. I'm not saying it's the


### [12:00 - 13:00]

**[12:00]** that wrong. I'm not saying it's the

**[12:00]** that wrong. I'm not saying it's the perfect architecture, but in a normal

**[12:02]** perfect architecture, but in a normal

**[12:02]** perfect architecture, but in a normal software environment, you could actually

**[12:04]** software environment, you could actually

**[12:04]** software environment, you could actually just upgrade the machine, right? Put it

**[12:06]** just upgrade the machine, right? Put it

**[12:06]** just upgrade the machine, right? Put it on a new hardware, put it on a new

**[12:07]** on a new hardware, put it on a new

**[12:07]** on a new hardware, put it on a new operating system, and it would just

**[12:09]** operating system, and it would just

**[12:09]** operating system, and it would just work. And it would actually work

**[12:10]** work. And it would actually work

**[12:10]** work. And it would actually work reasonably well because the architecture

**[12:11]** reasonably well because the architecture

**[12:11]** reasonably well because the architecture is not that bad. But we know that that's

**[12:13]** is not that bad. But we know that that's

**[12:13]** is not that bad. But we know that that's not the case for these ML sort of

**[12:15]** not the case for these ML sort of

**[12:15]** not the case for these ML sort of architectures because they're not

**[12:16]** architectures because they're not

**[12:16]** architectures because they're not expressed in the right way. So I think

**[12:19]** expressed in the right way. So I think

**[12:19]** expressed in the right way. So I think fundamentally I can express this most um

**[12:22]** fundamentally I can express this most um

**[12:22]** fundamentally I can express this most um passionately against prompts. A prompt

**[12:24]** passionately against prompts. A prompt

**[12:24]** passionately against prompts. A prompt is a horrible abstraction for

**[12:26]** is a horrible abstraction for

**[12:26]** is a horrible abstraction for programming and this needs to be fixed

**[12:28]** programming and this needs to be fixed

**[12:28]** programming and this needs to be fixed ASAP. Um, I say for programming because

**[12:30]** ASAP. Um, I say for programming because

**[12:30]** ASAP. Um, I say for programming because it's actually not a horrible one for

**[12:31]** it's actually not a horrible one for

**[12:32]** it's actually not a horrible one for management. If you want to manage an

**[12:33]** management. If you want to manage an

**[12:33]** management. If you want to manage an employee or an agent, a prompt is a

**[12:35]** employee or an agent, a prompt is a

**[12:35]** employee or an agent, a prompt is a reasonably kind of like it's an Slack

**[12:37]** reasonably kind of like it's an Slack

**[12:37]** reasonably kind of like it's an Slack channel. You have a remote employee. If

**[12:39]** channel. You have a remote employee. If

**[12:39]** channel. You have a remote employee. If you want to be a pet trainer, you know,

**[12:41]** you want to be a pet trainer, you know,

**[12:41]** you want to be a pet trainer, you know, working with tensors and, you know,

**[12:42]** working with tensors and, you know,

**[12:42]** working with tensors and, you know, objectives is a great way to iterate.

**[12:44]** objectives is a great way to iterate.

**[12:44]** objectives is a great way to iterate. That's how we build the models. But I

**[12:46]** That's how we build the models. But I

**[12:46]** That's how we build the models. But I want us to be able to also engineer AI

**[12:48]** want us to be able to also engineer AI

**[12:48]** want us to be able to also engineer AI systems. And I think for engineering and

**[12:50]** systems. And I think for engineering and

**[12:50]** systems. And I think for engineering and programming, a prompt is a horrible

**[12:51]** programming, a prompt is a horrible

**[12:51]** programming, a prompt is a horrible abstraction. Here's why. It's a stringly

**[12:54]** abstraction. Here's why. It's a stringly

**[12:54]** abstraction. Here's why. It's a stringly typed canvas, just a big blurb, no

**[12:56]** typed canvas, just a big blurb, no

**[12:56]** typed canvas, just a big blurb, no structure whatsoever, even if structure

**[12:58]** structure whatsoever, even if structure

**[12:58]** structure whatsoever, even if structure actually exists in a latent way. Um,


### [13:00 - 14:00]

**[13:00]** actually exists in a latent way. Um,

**[13:00]** actually exists in a latent way. Um, that couples and entangles the

**[13:02]** that couples and entangles the

**[13:02]** that couples and entangles the fundamental task definition you want to

**[13:04]** fundamental task definition you want to

**[13:04]** fundamental task definition you want to say, which is really important stuff.

**[13:06]** say, which is really important stuff.

**[13:06]** say, which is really important stuff. This is what you're engineering with

**[13:08]** This is what you're engineering with

**[13:08]** This is what you're engineering with some random over uh fitted halfbaked

**[13:11]** some random over uh fitted halfbaked

**[13:11]** some random over uh fitted halfbaked decisions about, hey, this LLM responded

**[13:13]** decisions about, hey, this LLM responded

**[13:13]** decisions about, hey, this LLM responded to this language, you know, when I talk

**[13:15]** to this language, you know, when I talk

**[13:15]** to this language, you know, when I talk to it this way or I put this example to

**[13:17]** to it this way or I put this example to

**[13:18]** to it this way or I put this example to demonstrate my point um and it kind of

**[13:20]** demonstrate my point um and it kind of

**[13:20]** demonstrate my point um and it kind of clicked for this model, so I'll just

**[13:21]** clicked for this model, so I'll just

**[13:21]** clicked for this model, so I'll just keep it in. And there's no way to really

**[13:23]** keep it in. And there's no way to really

**[13:23]** keep it in. And there's no way to really tell the difference. What was the

**[13:24]** tell the difference. What was the

**[13:24]** tell the difference. What was the fundamental thing you're solving and

**[13:25]** fundamental thing you're solving and

**[13:25]** fundamental thing you're solving and like you know what was the random uh

**[13:27]** like you know what was the random uh

**[13:27]** like you know what was the random uh trick you applied. It's like a square

**[13:29]** trick you applied. It's like a square

**[13:29]** trick you applied. It's like a square root thing except you don't call it a

**[13:30]** root thing except you don't call it a

**[13:30]** root thing except you don't call it a square root and we just have to stare at

**[13:31]** square root and we just have to stare at

**[13:31]** square root and we just have to stare at it and be like wait why are we shifting

**[13:34]** it and be like wait why are we shifting

**[13:34]** it and be like wait why are we shifting to the left five you know by five bits

**[13:36]** to the left five you know by five bits

**[13:36]** to the left five you know by five bits or something. Um you're also inducing

**[13:38]** or something. Um you're also inducing

**[13:38]** or something. Um you're also inducing the inference time strategy which is

**[13:39]** the inference time strategy which is

**[13:40]** the inference time strategy which is like changing every few weeks or people

**[13:41]** like changing every few weeks or people

**[13:41]** like changing every few weeks or people are proposing stuff all the time and

**[13:43]** are proposing stuff all the time and

**[13:43]** are proposing stuff all the time and you're baking it literally entangling it

**[13:45]** you're baking it literally entangling it

**[13:45]** you're baking it literally entangling it into your system. So if it's an agent

**[13:47]** into your system. So if it's an agent

**[13:47]** into your system. So if it's an agent your prompt is telling it it's an agent.

**[13:49]** your prompt is telling it it's an agent.

**[13:49]** your prompt is telling it it's an agent. your system has no big like deal knowing

**[13:51]** your system has no big like deal knowing

**[13:51]** your system has no big like deal knowing about the fact it's an agent or a

**[13:53]** about the fact it's an agent or a

**[13:53]** about the fact it's an agent or a reasoning system or whatever. What are

**[13:54]** reasoning system or whatever. What are

**[13:54]** reasoning system or whatever. What are you actually trying to solve? Right? If

**[13:56]** you actually trying to solve? Right? If

**[13:56]** you actually trying to solve? Right? If it's like if you're writing a square

**[13:57]** it's like if you're writing a square

**[13:57]** it's like if you're writing a square root function and then you're like hey

**[13:59]** root function and then you're like hey

**[13:59]** root function and then you're like hey here is the layout of the strcts in


### [14:00 - 15:00]

**[14:00]** here is the layout of the strcts in

**[14:00]** here is the layout of the strcts in memory or something. Um you're also

**[14:03]** memory or something. Um you're also

**[14:03]** memory or something. Um you're also talking about formatting and parsing

**[14:05]** talking about formatting and parsing

**[14:05]** talking about formatting and parsing things you know write in XML produce

**[14:07]** things you know write in XML produce

**[14:07]** things you know write in XML produce JSON whatever like again that's really

**[14:09]** JSON whatever like again that's really

**[14:10]** JSON whatever like again that's really none of your business most of the time.

**[14:12]** none of your business most of the time.

**[14:12]** none of your business most of the time. So you want to write a human readable

**[14:13]** So you want to write a human readable

**[14:13]** So you want to write a human readable spec but you're saying things like do

**[14:15]** spec but you're saying things like do

**[14:15]** spec but you're saying things like do not ignore this generate XML answer in

**[14:17]** not ignore this generate XML answer in

**[14:17]** not ignore this generate XML answer in JSON. you are professor Einstein, a wise

**[14:20]** JSON. you are professor Einstein, a wise

**[14:20]** JSON. you are professor Einstein, a wise expert in the field of I'll tip you

**[14:21]** expert in the field of I'll tip you

**[14:21]** expert in the field of I'll tip you $1,000, right? Like that is just not

**[14:24]** $1,000, right? Like that is just not

**[14:24]** $1,000, right? Like that is just not engineering, guys. Um, so what should we

**[14:28]** engineering, guys. Um, so what should we

**[14:28]** engineering, guys. Um, so what should we do? Trusty old separation of concerns, I

**[14:30]** do? Trusty old separation of concerns, I

**[14:30]** do? Trusty old separation of concerns, I think, is the answer. Your job as an

**[14:33]** think, is the answer. Your job as an

**[14:33]** think, is the answer. Your job as an engineer is to invest in your actual

**[14:35]** engineer is to invest in your actual

**[14:35]** engineer is to invest in your actual system design. And you know, starting

**[14:37]** system design. And you know, starting

**[14:37]** system design. And you know, starting with the spec, the spec unfortunately or

**[14:40]** with the spec, the spec unfortunately or

**[14:40]** with the spec, the spec unfortunately or fortunately cannot be reduced to one

**[14:42]** fortunately cannot be reduced to one

**[14:42]** fortunately cannot be reduced to one thing. And this is the time I'll talk

**[14:44]** thing. And this is the time I'll talk

**[14:44]** thing. And this is the time I'll talk about evals. I know everyone hears about

**[14:45]** about evals. I know everyone hears about

**[14:45]** about evals. I know everyone hears about eval. This is the one line about evals

**[14:47]** eval. This is the one line about evals

**[14:47]** eval. This is the one line about evals that makes this talk about evals. A lot

**[14:49]** that makes this talk about evals. A lot

**[14:49]** that makes this talk about evals. A lot of the time um you want to invest in

**[14:52]** of the time um you want to invest in

**[14:52]** of the time um you want to invest in natural language descriptions because

**[14:53]** natural language descriptions because

**[14:53]** natural language descriptions because that is the power of this new framework.

**[14:55]** that is the power of this new framework.

**[14:55]** that is the power of this new framework. Natural language definitions are not

**[14:57]** Natural language definitions are not

**[14:57]** Natural language definitions are not prompts. They are highly localized

**[14:59]** prompts. They are highly localized

**[14:59]** prompts. They are highly localized pieces of ambiguous stuff that could not


### [15:00 - 16:00]

**[15:01]** pieces of ambiguous stuff that could not

**[15:01]** pieces of ambiguous stuff that could not have been said in any other way. Right?

**[15:03]** have been said in any other way. Right?

**[15:03]** have been said in any other way. Right? I can't tell the system certain things

**[15:05]** I can't tell the system certain things

**[15:05]** I can't tell the system certain things except in English. So I'll say it in

**[15:07]** except in English. So I'll say it in

**[15:07]** except in English. So I'll say it in English. But a lot of the time I'm

**[15:09]** English. But a lot of the time I'm

**[15:09]** English. But a lot of the time I'm actually iterating to uh to appease a

**[15:11]** actually iterating to uh to appease a

**[15:11]** actually iterating to uh to appease a certain model and to make it perform

**[15:13]** certain model and to make it perform

**[15:13]** certain model and to make it perform well relative to some criteria I have

**[15:16]** well relative to some criteria I have

**[15:16]** well relative to some criteria I have not telling it the criteria just

**[15:17]** not telling it the criteria just

**[15:17]** not telling it the criteria just tinkering with things there. Evals is

**[15:20]** tinkering with things there. Evals is

**[15:20]** tinkering with things there. Evals is the way to do this because eval say

**[15:22]** the way to do this because eval say

**[15:22]** the way to do this because eval say here's what I actually care about.

**[15:23]** here's what I actually care about.

**[15:23]** here's what I actually care about. Change the model. The eval are still

**[15:25]** Change the model. The eval are still

**[15:25]** Change the model. The eval are still what I care about. It's a fundamental

**[15:26]** what I care about. It's a fundamental

**[15:26]** what I care about. It's a fundamental thing. Now eval

**[15:29]** thing. Now eval

**[15:29]** thing. Now eval to define the core behavior of your

**[15:31]** to define the core behavior of your

**[15:31]** to define the core behavior of your system. You will not learn. Induction

**[15:32]** system. You will not learn. Induction

**[15:32]** system. You will not learn. Induction learning from data is a lot harder than

**[15:34]** learning from data is a lot harder than

**[15:34]** learning from data is a lot harder than following instructions. Right? So you

**[15:36]** following instructions. Right? So you

**[15:36]** following instructions. Right? So you need to have both. Code is another thing

**[15:39]** need to have both. Code is another thing

**[15:39]** need to have both. Code is another thing that you need. You know, a lot of people

**[15:40]** that you need. You know, a lot of people

**[15:40]** that you need. You know, a lot of people are like, "Oh, it's just like a, you

**[15:42]** are like, "Oh, it's just like a, you

**[15:42]** are like, "Oh, it's just like a, you know, just just ask it to do the thing."

**[15:43]** know, just just ask it to do the thing."

**[15:43]** know, just just ask it to do the thing." Well, who's going to define the tools?

**[15:45]** Well, who's going to define the tools?

**[15:45]** Well, who's going to define the tools? Who's going to define the structure? How

**[15:46]** Who's going to define the structure? How

**[15:46]** Who's going to define the structure? How do you handle information flow? Like,

**[15:48]** do you handle information flow? Like,

**[15:48]** do you handle information flow? Like, you know, like things that are private

**[15:50]** you know, like things that are private

**[15:50]** you know, like things that are private should not flow in the wrong places,

**[15:51]** should not flow in the wrong places,

**[15:51]** should not flow in the wrong places, right? You need to control these things.

**[15:53]** right? You need to control these things.

**[15:53]** right? You need to control these things. Um, how do you apply function

**[15:54]** Um, how do you apply function

**[15:54]** Um, how do you apply function composition? LLMs are horrible at

**[15:56]** composition? LLMs are horrible at

**[15:56]** composition? LLMs are horrible at composition because neuronet networks

**[15:57]** composition because neuronet networks

**[15:57]** composition because neuronet networks kind of essentially don't learn things

**[15:59]** kind of essentially don't learn things

**[15:59]** kind of essentially don't learn things that reliably. Function composition in


### [16:00 - 17:00]

**[16:01]** that reliably. Function composition in

**[16:01]** that reliably. Function composition in software is always perfectly reliable

**[16:03]** software is always perfectly reliable

**[16:03]** software is always perfectly reliable basically, right, by construction. So a

**[16:05]** basically, right, by construction. So a

**[16:05]** basically, right, by construction. So a lot of the things um are often best

**[16:08]** lot of the things um are often best

**[16:08]** lot of the things um are often best delegated to code, right? But it's it's

**[16:10]** delegated to code, right? But it's it's

**[16:10]** delegated to code, right? But it's it's hard and it's really important that you

**[16:12]** hard and it's really important that you

**[16:12]** hard and it's really important that you can actually juggle and combine these

**[16:14]** can actually juggle and combine these

**[16:14]** can actually juggle and combine these things and you need a canvas that can

**[16:16]** things and you need a canvas that can

**[16:16]** things and you need a canvas that can allow you to combine these things. Well,

**[16:18]** allow you to combine these things. Well,

**[16:18]** allow you to combine these things. Well, when you do this, a good canvas, the

**[16:20]** when you do this, a good canvas, the

**[16:20]** when you do this, a good canvas, the definition here of a good canvas or a c

**[16:22]** definition here of a good canvas or a c

**[16:22]** definition here of a good canvas or a c the the criteria for a good canvas is

**[16:24]** the the criteria for a good canvas is

**[16:24]** the the criteria for a good canvas is that it should allow you to express

**[16:25]** that it should allow you to express

**[16:25]** that it should allow you to express those three in a way that's highly

**[16:27]** those three in a way that's highly

**[16:27]** those three in a way that's highly streamlined and in a way that is

**[16:29]** streamlined and in a way that is

**[16:29]** streamlined and in a way that is decoupled and not entangled with models

**[16:32]** decoupled and not entangled with models

**[16:32]** decoupled and not entangled with models that are changing. I should just be able

**[16:33]** that are changing. I should just be able

**[16:33]** that are changing. I should just be able to hot swap models. Uh inference

**[16:35]** to hot swap models. Uh inference

**[16:35]** to hot swap models. Uh inference strategies that are changing. Hey, I

**[16:37]** strategies that are changing. Hey, I

**[16:37]** strategies that are changing. Hey, I want to switch from a chain of thought

**[16:38]** want to switch from a chain of thought

**[16:38]** want to switch from a chain of thought to an agent. I want to switch from an

**[16:39]** to an agent. I want to switch from an

**[16:39]** to an agent. I want to switch from an agent to a Monte Carlo research.

**[16:41]** agent to a Monte Carlo research.

**[16:41]** agent to a Monte Carlo research. Whatever the latest thing that has come

**[16:42]** Whatever the latest thing that has come

**[16:42]** Whatever the latest thing that has come out is, right? I should be able to just

**[16:44]** out is, right? I should be able to just

**[16:44]** out is, right? I should be able to just do that. Um and new learning algorithms.

**[16:46]** do that. Um and new learning algorithms.

**[16:46]** do that. Um and new learning algorithms. So, this is really important. We talked

**[16:48]** So, this is really important. We talked

**[16:48]** So, this is really important. We talked about learning, but learning uh is, you

**[16:50]** about learning, but learning uh is, you

**[16:50]** about learning, but learning uh is, you know, always happening at the level of

**[16:51]** know, always happening at the level of

**[16:52]** know, always happening at the level of your entire system if you're engineering

**[16:53]** your entire system if you're engineering

**[16:53]** your entire system if you're engineering it or at least you got to be thinking

**[16:54]** it or at least you got to be thinking

**[16:54]** it or at least you got to be thinking about it that way where you're saying, I

**[16:56]** about it that way where you're saying, I

**[16:56]** about it that way where you're saying, I want the whole thing to work as a whole

**[16:58]** want the whole thing to work as a whole

**[16:58]** want the whole thing to work as a whole for my problem, not for some general


### [17:00 - 18:00]

**[17:00]** for my problem, not for some general

**[17:00]** for my problem, not for some general default. Right? So that's what the eval

**[17:01]** default. Right? So that's what the eval

**[17:02]** default. Right? So that's what the eval here are going to be doing. And you want

**[17:03]** here are going to be doing. And you want

**[17:03]** here are going to be doing. And you want a a way of expressing this that allows

**[17:05]** a a way of expressing this that allows

**[17:05]** a a way of expressing this that allows you to do reinforcement learning but

**[17:07]** you to do reinforcement learning but

**[17:07]** you to do reinforcement learning but also allows you to do prompt

**[17:08]** also allows you to do prompt

**[17:08]** also allows you to do prompt optimization but also allows you to do

**[17:09]** optimization but also allows you to do

**[17:09]** optimization but also allows you to do any of these things at the level of

**[17:10]** any of these things at the level of

**[17:10]** any of these things at the level of abstraction that you're actually working

**[17:11]** abstraction that you're actually working

**[17:12]** abstraction that you're actually working with. So the second takeaway is that you

**[17:13]** with. So the second takeaway is that you

**[17:14]** with. So the second takeaway is that you should invest in defining things

**[17:15]** should invest in defining things

**[17:15]** should invest in defining things specific to your AI system and decouple

**[17:18]** specific to your AI system and decouple

**[17:18]** specific to your AI system and decouple from uh the lower level swappable pieces

**[17:20]** from uh the lower level swappable pieces

**[17:20]** from uh the lower level swappable pieces because they'll expire faster than ever.

**[17:22]** because they'll expire faster than ever.

**[17:22]** because they'll expire faster than ever. Um so I'll just conclude by telling you

**[17:25]** Um so I'll just conclude by telling you

**[17:25]** Um so I'll just conclude by telling you we've built and been building for three

**[17:26]** we've built and been building for three

**[17:26]** we've built and been building for three years this DSPI framework which is the

**[17:28]** years this DSPI framework which is the

**[17:28]** years this DSPI framework which is the only framework that actually decouples u

**[17:31]** only framework that actually decouples u

**[17:31]** only framework that actually decouples u your job from which is writing the lower

**[17:34]** your job from which is writing the lower

**[17:34]** your job from which is writing the lower level AI software from our job which is

**[17:37]** level AI software from our job which is

**[17:37]** level AI software from our job which is giving you powerful evolving toolkits

**[17:39]** giving you powerful evolving toolkits

**[17:39]** giving you powerful evolving toolkits for learning and for search which is

**[17:41]** for learning and for search which is

**[17:41]** for learning and for search which is scaling um and for swapping LLMs through

**[17:44]** scaling um and for swapping LLMs through

**[17:44]** scaling um and for swapping LLMs through adapters um so there's only one concept

**[17:47]** adapters um so there's only one concept

**[17:47]** adapters um so there's only one concept you have to learn it is a new concept

**[17:49]** you have to learn it is a new concept

**[17:49]** you have to learn it is a new concept which is which we call signatures a new

**[17:51]** which is which we call signatures a new

**[17:51]** which is which we call signatures a new first class concept If you learn it,

**[17:53]** first class concept If you learn it,

**[17:53]** first class concept If you learn it, you've learned DSPI. Um, I'll have to

**[17:55]** you've learned DSPI. Um, I'll have to

**[17:55]** you've learned DSPI. Um, I'll have to unfortunately skip this because of the

**[17:56]** unfortunately skip this because of the

**[17:56]** unfortunately skip this because of the because of the time for the other

**[17:57]** because of the time for the other

**[17:58]** because of the time for the other speakers. Uh, but let me give you a

**[17:59]** speakers. Uh, but let me give you a

**[17:59]** speakers. Uh, but let me give you a summary. I can't predict the future. I'm


### [18:00 - 19:00]

**[18:01]** summary. I can't predict the future. I'm

**[18:01]** summary. I can't predict the future. I'm not telling you if you do this, you

**[18:02]** not telling you if you do this, you

**[18:02]** not telling you if you do this, you know, this the code you write tomorrow

**[18:04]** know, this the code you write tomorrow

**[18:04]** know, this the code you write tomorrow will be there forever. But I'm telling

**[18:05]** will be there forever. But I'm telling

**[18:05]** will be there forever. But I'm telling you the least you can do. This is not

**[18:07]** you the least you can do. This is not

**[18:07]** you the least you can do. This is not like the the kind of the top level. It's

**[18:09]** like the the kind of the top level. It's

**[18:09]** like the the kind of the top level. It's just like the b the baseline I would say

**[18:11]** just like the b the baseline I would say

**[18:11]** just like the b the baseline I would say is avoid the hand engineering at lower

**[18:14]** is avoid the hand engineering at lower

**[18:14]** is avoid the hand engineering at lower levels than today allows you to do,

**[18:16]** levels than today allows you to do,

**[18:16]** levels than today allows you to do, right? That's the that's the big lesson

**[18:18]** right? That's the that's the big lesson

**[18:18]** right? That's the that's the big lesson from the bitter lesson and from

**[18:19]** from the bitter lesson and from

**[18:19]** from the bitter lesson and from premature optimization being the root of

**[18:21]** premature optimization being the root of

**[18:21]** premature optimization being the root of all evil. Um, among your safest bets,

**[18:23]** all evil. Um, among your safest bets,

**[18:23]** all evil. Um, among your safest bets, they could all turn out to be wrong. I

**[18:24]** they could all turn out to be wrong. I

**[18:24]** they could all turn out to be wrong. I don't know, is um, models are not

**[18:27]** don't know, is um, models are not

**[18:27]** don't know, is um, models are not anytime soon going to read uh, specs off

**[18:29]** anytime soon going to read uh, specs off

**[18:29]** anytime soon going to read uh, specs off of your mind. I don't know if like we'll

**[18:31]** of your mind. I don't know if like we'll

**[18:31]** of your mind. I don't know if like we'll figure that out. Um, and they're not

**[18:33]** figure that out. Um, and they're not

**[18:33]** figure that out. Um, and they're not going to magically collect all the

**[18:35]** going to magically collect all the

**[18:35]** going to magically collect all the structure and tools specific to your

**[18:36]** structure and tools specific to your

**[18:36]** structure and tools specific to your application. So, that's clearly stuff

**[18:38]** application. So, that's clearly stuff

**[18:38]** application. So, that's clearly stuff you should invest in, right? When you're

**[18:40]** you should invest in, right? When you're

**[18:40]** you should invest in, right? When you're building a system, invest in the

**[18:41]** building a system, invest in the

**[18:41]** building a system, invest in the signatures, which I again you can learn

**[18:43]** signatures, which I again you can learn

**[18:43]** signatures, which I again you can learn about on the DSpy site, uh, dspi.ai.

**[18:46]** about on the DSpy site, uh, dspi.ai.

**[18:46]** about on the DSpy site, uh, dspi.ai. Invest in essential control flow and

**[18:48]** Invest in essential control flow and

**[18:48]** Invest in essential control flow and tools and invest in evaluating

**[18:51]** tools and invest in evaluating

**[18:52]** tools and invest in evaluating on by hand and ride the wave of

**[18:53]** on by hand and ride the wave of

**[18:54]** on by hand and ride the wave of swappable models. Ride the wave of the

**[18:56]** swappable models. Ride the wave of the

**[18:56]** swappable models. Ride the wave of the modules we build. Um you just swap them

**[18:58]** modules we build. Um you just swap them

**[18:58]** modules we build. Um you just swap them in and out and ride the wave of

**[18:59]** in and out and ride the wave of

**[18:59]** in and out and ride the wave of optimizers which can do things like


### [19:00 - 20:00]

**[19:00]** optimizers which can do things like

**[19:00]** optimizers which can do things like reinforcement learning or prompt

**[19:02]** reinforcement learning or prompt

**[19:02]** reinforcement learning or prompt optimization for any application that it

**[19:03]** optimization for any application that it

**[19:04]** optimization for any application that it is that you've built. Uh all right,

**[19:05]** is that you've built. Uh all right,

**[19:05]** is that you've built. Uh all right, thank you everyone.

**[19:06]** thank you everyone.

**[19:06]** thank you everyone. [Music]


