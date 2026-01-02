# 2026- The Year The IDE Died — Steve Yegge & Gene Kim, Authors, Vibe Coding

**Video URL:** https://www.youtube.com/watch?v=7Dtu2bilcFs

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** Hey everybody. Um, really happy to be

**[00:23]** Hey everybody. Um, really happy to be here. I'm going to be talking the first

**[00:24]** here. I'm going to be talking the first

**[00:24]** here. I'm going to be talking the first half. Co-author here, Jean Kim, is going

**[00:26]** half. Co-author here, Jean Kim, is going

**[00:26]** half. Co-author here, Jean Kim, is going to talk second half. All right. Looking

**[00:29]** to talk second half. All right. Looking

**[00:29]** to talk second half. All right. Looking forward to it. Cheers. All right. Today,

**[00:31]** forward to it. Cheers. All right. Today,

**[00:31]** forward to it. Cheers. All right. Today, I'm gonna Well, we're going to talk real

**[00:32]** I'm gonna Well, we're going to talk real

**[00:32]** I'm gonna Well, we're going to talk real fast. This time's going to go down fast.

**[00:34]** fast. This time's going to go down fast.

**[00:34]** fast. This time's going to go down fast. Uh, I'm going to talk to you about what

**[00:36]** Uh, I'm going to talk to you about what

**[00:36]** Uh, I'm going to talk to you about what tools look like next year. Last year, I

**[00:39]** tools look like next year. Last year, I

**[00:39]** tools look like next year. Last year, I was talking to you all about chat and

**[00:41]** was talking to you all about chat and

**[00:41]** was talking to you all about chat and everybody ignored me and now everybody's

**[00:43]** everybody ignored me and now everybody's

**[00:43]** everybody ignored me and now everybody's using chat this year and it's like we're

**[00:45]** using chat this year and it's like we're

**[00:45]** using chat this year and it's like we're gonna we're going to fix that right now.

**[00:47]** gonna we're going to fix that right now.

**[00:48]** gonna we're going to fix that right now. All right. So, here's what it's looked

**[00:50]** All right. So, here's what it's looked

**[00:50]** All right. So, here's what it's looked like. I'm going to tell you right now,

**[00:52]** like. I'm going to tell you right now,

**[00:52]** like. I'm going to tell you right now, everyone's in love with Cloud Code.

**[00:54]** everyone's in love with Cloud Code.

**[00:54]** everyone's in love with Cloud Code. There's probably 40 competitors out

**[00:56]** There's probably 40 competitors out

**[00:56]** There's probably 40 competitors out there. Cloud code ain't it.


### [01:00 - 02:00]

**[01:00]** there. Cloud code ain't it.

**[01:00]** there. Cloud code ain't it. Completions wasn't it. I love cloud

**[01:02]** Completions wasn't it. I love cloud

**[01:02]** Completions wasn't it. I love cloud code. I use it 14 hours a day. I mean,

**[01:04]** code. I use it 14 hours a day. I mean,

**[01:04]** code. I use it 14 hours a day. I mean, come on. But it ain't it. Developers

**[01:07]** come on. But it ain't it. Developers

**[01:07]** come on. But it ain't it. Developers aren't adopting it. I'm going to talk

**[01:08]** aren't adopting it. I'm going to talk

**[01:08]** aren't adopting it. I'm going to talk about why in this talk. I'm going to

**[01:09]** about why in this talk. I'm going to

**[01:09]** about why in this talk. I'm going to talk about what you can do about it and

**[01:11]** talk about what you can do about it and

**[01:11]** talk about what you can do about it and what what to look forward to. But the

**[01:13]** what what to look forward to. But the

**[01:13]** what what to look forward to. But the reason is they're too hard. Okay. Uh

**[01:15]** reason is they're too hard. Okay. Uh

**[01:15]** reason is they're too hard. Okay. Uh cognitive overhead. Uh they lie, cheat,

**[01:17]** cognitive overhead. Uh they lie, cheat,

**[01:17]** cognitive overhead. Uh they lie, cheat, and steal. Gene and I talk a lot about

**[01:19]** and steal. Gene and I talk a lot about

**[01:19]** and steal. Gene and I talk a lot about this in our book, all the different ways

**[01:21]** this in our book, all the different ways

**[01:21]** this in our book, all the different ways that they can lie, cheat, and steal. And

**[01:23]** that they can lie, cheat, and steal. And

**[01:23]** that they can lie, cheat, and steal. And >> [clears throat]

**[01:23]** >> [clears throat]

**[01:23]** >> [clears throat] >> uh most devs just don't like this.

**[01:27]** >> uh most devs just don't like this.

**[01:27]** >> uh most devs just don't like this. I have come to understand that claude

**[01:29]** I have come to understand that claude

**[01:29]** I have come to understand that claude code is very much like a drill or a saw,

**[01:33]** code is very much like a drill or a saw,

**[01:33]** code is very much like a drill or a saw, an electric one, right? How much damage

**[01:36]** an electric one, right? How much damage

**[01:36]** an electric one, right? How much damage can you do as an untrained person with a

**[01:38]** can you do as an untrained person with a

**[01:38]** can you do as an untrained person with a drill, right? Or a saw. Yeah. How much

**[01:41]** drill, right? Or a saw. Yeah. How much

**[01:41]** drill, right? Or a saw. Yeah. How much damage can you do as an untrained

**[01:43]** damage can you do as an untrained

**[01:43]** damage can you do as an untrained engineer with claw code? It's real

**[01:45]** engineer with claw code? It's real

**[01:45]** engineer with claw code? It's real similar. Yeah. You can cut your foot

**[01:46]** similar. Yeah. You can cut your foot

**[01:46]** similar. Yeah. You can cut your foot off,

**[01:49]** off,

**[01:49]** off, but you can also be really, really

**[01:51]** but you can also be really, really

**[01:51]** but you can also be really, really skilled with it and do really precision

**[01:53]** skilled with it and do really precision

**[01:53]** skilled with it and do really precision work, right? like a craftsman. The

**[01:56]** work, right? like a craftsman. The

**[01:56]** work, right? like a craftsman. The problem is software is infinitely large.

**[01:59]** problem is software is infinitely large.

**[01:59]** problem is software is infinitely large. Our ambition is infinitely large. And so


### [02:00 - 03:00]

**[02:01]** Our ambition is infinitely large. And so

**[02:01]** Our ambition is infinitely large. And so the analogy that I want to share with

**[02:02]** the analogy that I want to share with

**[02:02]** the analogy that I want to share with you is next year will be the year from

**[02:04]** you is next year will be the year from

**[02:04]** you is next year will be the year from moving from saws and drills to CNC

**[02:08]** moving from saws and drills to CNC

**[02:08]** moving from saws and drills to CNC machines. A CNC machine, you strap a

**[02:11]** machines. A CNC machine, you strap a

**[02:11]** machines. A CNC machine, you strap a drill on and you give it coordinates and

**[02:13]** drill on and you give it coordinates and

**[02:13]** drill on and you give it coordinates and it moves it around and very precise,

**[02:15]** it moves it around and very precise,

**[02:15]** it moves it around and very precise, right? We've been doing this for

**[02:17]** right? We've been doing this for

**[02:17]** right? We've been doing this for centuries and we're not going to stop

**[02:19]** centuries and we're not going to stop

**[02:19]** centuries and we're not going to stop this year.

**[02:24]** One thing I hear people say is, "Well,

**[02:24]** One thing I hear people say is, "Well, the models are plateaued." This is real

**[02:26]** the models are plateaued." This is real

**[02:26]** the models are plateaued." This is real common. Your engineers are probably

**[02:28]** common. Your engineers are probably

**[02:28]** common. Your engineers are probably saying this, okay, even if they

**[02:31]** saying this, okay, even if they

**[02:31]** saying this, okay, even if they plateaued, we have still discovered

**[02:33]** plateaued, we have still discovered

**[02:33]** plateaued, we have still discovered steam and electricity, and it's going to

**[02:35]** steam and electricity, and it's going to

**[02:35]** steam and electricity, and it's going to take us a little time to harness it. But

**[02:36]** take us a little time to harness it. But

**[02:36]** take us a little time to harness it. But it's strictly an engineering problem at

**[02:38]** it's strictly an engineering problem at

**[02:38]** it's strictly an engineering problem at this point. All code within a year, year

**[02:42]** this point. All code within a year, year

**[02:42]** this point. All code within a year, year and a half will be written by giant

**[02:44]** and a half will be written by giant

**[02:44]** and a half will be written by giant grinding machines overseen by engineers

**[02:47]** grinding machines overseen by engineers

**[02:48]** grinding machines overseen by engineers who no longer actually look at the code

**[02:49]** who no longer actually look at the code

**[02:49]** who no longer actually look at the code directly anymore.

**[02:52]** directly anymore.

**[02:52]** directly anymore. Weird new world. That is where we are

**[02:54]** Weird new world. That is where we are

**[02:54]** Weird new world. That is where we are going. Oh my gosh. Yep. This this slide.

**[02:57]** going. Oh my gosh. Yep. This this slide.

**[02:58]** going. Oh my gosh. Yep. This this slide. So Gan and I talked to Andrew Glover who


### [03:00 - 04:00]

**[03:00]** So Gan and I talked to Andrew Glover who

**[03:00]** So Gan and I talked to Andrew Glover who I don't know is he here from OpenAI and

**[03:02]** I don't know is he here from OpenAI and

**[03:02]** I don't know is he here from OpenAI and he said that they have this incredible

**[03:04]** he said that they have this incredible

**[03:04]** he said that they have this incredible dichotomy unfolding at OpenAI where you

**[03:06]** dichotomy unfolding at OpenAI where you

**[03:06]** dichotomy unfolding at OpenAI where you know some percentage of their engineers

**[03:07]** know some percentage of their engineers

**[03:07]** know some percentage of their engineers are using codecs and then some other

**[03:10]** are using codecs and then some other

**[03:10]** are using codecs and then some other percentage a larger percentage are not

**[03:11]** percentage a larger percentage are not

**[03:11]** percentage a larger percentage are not using codecs and the difference in

**[03:13]** using codecs and the difference in

**[03:13]** using codecs and the difference in productivity is so staggering that

**[03:15]** productivity is so staggering that

**[03:15]** productivity is so staggering that they're having now alarms going off at

**[03:18]** they're having now alarms going off at

**[03:18]** they're having now alarms going off at performance review time because how do

**[03:19]** performance review time because how do

**[03:19]** performance review time because how do you compare these these two engineers

**[03:21]** you compare these these two engineers

**[03:21]** you compare these these two engineers who are the same level, same title, same

**[03:23]** who are the same level, same title, same

**[03:23]** who are the same level, same title, same everything and one of them is 10 times

**[03:25]** everything and one of them is 10 times

**[03:25]** everything and one of them is 10 times as productive as the other one by any

**[03:27]** as productive as the other one by any

**[03:27]** as productive as the other one by any measure.

**[03:28]** measure.

**[03:28]** measure. And the answer is they're freaking out

**[03:30]** And the answer is they're freaking out

**[03:30]** And the answer is they're freaking out and they may have to fire 50% of their

**[03:32]** and they may have to fire 50% of their

**[03:32]** and they may have to fire 50% of their engineers. And this is unfolding at

**[03:33]** engineers. And this is unfolding at

**[03:33]** engineers. And this is unfolding at other companies, too.

**[03:36]** other companies, too.

**[03:36]** other companies, too. Who is refusing it? It's the senior and

**[03:39]** Who is refusing it? It's the senior and

**[03:39]** Who is refusing it? It's the senior and staff engineers. How many minutes are we

**[03:41]** staff engineers. How many minutes are we

**[03:41]** staff engineers. How many minutes are we at?

**[03:43]** at?

**[03:43]** at? >> Eight [clears throat] minutes.

**[03:44]** >> Eight [clears throat] minutes.

**[03:44]** >> Eight [clears throat] minutes. >> We're perfect. This is just like what

**[03:47]** >> We're perfect. This is just like what

**[03:47]** >> We're perfect. This is just like what happened to the Swiss mechanical watch

**[03:50]** happened to the Swiss mechanical watch

**[03:50]** happened to the Swiss mechanical watch industry over a couple of Well, it was

**[03:52]** industry over a couple of Well, it was

**[03:52]** industry over a couple of Well, it was built up for a couple of centuries and

**[03:54]** built up for a couple of centuries and

**[03:54]** built up for a couple of centuries and then courts killed it, you know, within

**[03:55]** then courts killed it, you know, within

**[03:55]** then courts killed it, you know, within a couple of years. And what happened was

**[03:57]** a couple of years. And what happened was

**[03:58]** a couple of years. And what happened was the craftsmen were doing the same thing

**[03:59]** the craftsmen were doing the same thing

**[03:59]** the craftsmen were doing the same thing our staff engineers are doing today. No


### [04:00 - 05:00]

**[04:02]** our staff engineers are doing today. No

**[04:02]** our staff engineers are doing today. No cheap.

**[04:04]** cheap.

**[04:04]** cheap. That's word for word, right? That's what

**[04:06]** That's word for word, right? That's what

**[04:06]** That's word for word, right? That's what they say.

**[04:09]** they say.

**[04:09]** they say. All right. I didn't know where to put

**[04:11]** All right. I didn't know where to put

**[04:11]** All right. I didn't know where to put this slide. This is this is Claude's

**[04:13]** this slide. This is this is Claude's

**[04:13]** this slide. This is this is Claude's view of what next year looks like. And I

**[04:16]** view of what next year looks like. And I

**[04:16]** view of what next year looks like. And I I was just like, what do you think it's

**[04:17]** I was just like, what do you think it's

**[04:17]** I was just like, what do you think it's going to look like? And it actually does

**[04:18]** going to look like? And it actually does

**[04:18]** going to look like? And it actually does kind of look like this. Most of the

**[04:19]** kind of look like this. Most of the

**[04:20]** kind of look like this. Most of the words will be spelled correctly in in

**[04:21]** words will be spelled correctly in in

**[04:21]** words will be spelled correctly in in next year. But this is a lot prettier

**[04:24]** next year. But this is a lot prettier

**[04:24]** next year. But this is a lot prettier than cloud code.

**[04:26]** than cloud code.

**[04:26]** than cloud code. Yeah, this is what it has to look like.

**[04:29]** Yeah, this is what it has to look like.

**[04:29]** Yeah, this is what it has to look like. Some form of a UI, not an IDE. This is

**[04:34]** Some form of a UI, not an IDE. This is

**[04:34]** Some form of a UI, not an IDE. This is the new IDE. Okay. And people are

**[04:36]** the new IDE. Okay. And people are

**[04:36]** the new IDE. Okay. And people are building it. In fact, I think the

**[04:38]** building it. In fact, I think the

**[04:38]** building it. In fact, I think the company that's the furthest along in

**[04:40]** company that's the furthest along in

**[04:40]** company that's the furthest along in this is Replet, who just talked to you.

**[04:42]** this is Replet, who just talked to you.

**[04:42]** this is Replet, who just talked to you. I think it's amazing what they're doing.

**[04:43]** I think it's amazing what they're doing.

**[04:44]** I think it's amazing what they're doing. It's absolutely bravo, right? We should

**[04:46]** It's absolutely bravo, right? We should

**[04:46]** It's absolutely bravo, right? We should not be all chasing tail lights and

**[04:48]** not be all chasing tail lights and

**[04:48]** not be all chasing tail lights and building command line interfaces

**[04:50]** building command line interfaces

**[04:50]** building command line interfaces anymore. All right. and and more

**[04:52]** anymore. All right. and and more

**[04:52]** anymore. All right. and and more importantly, Cloud Code and all of its,

**[04:55]** importantly, Cloud Code and all of its,

**[04:55]** importantly, Cloud Code and all of its, you know, competitors, they're all doing

**[04:58]** you know, competitors, they're all doing

**[04:58]** you know, competitors, they're all doing it wrong because they're building the

**[04:59]** it wrong because they're building the


### [05:00 - 06:00]

**[05:00]** it wrong because they're building the world's biggest ant. Okay, this is my my

**[05:02]** world's biggest ant. Okay, this is my my

**[05:02]** world's biggest ant. Okay, this is my my buddy Brendan Hopper at Commonwealth

**[05:03]** buddy Brendan Hopper at Commonwealth

**[05:03]** buddy Brendan Hopper at Commonwealth Bank of Australia, right? He's like,

**[05:05]** Bank of Australia, right? He's like,

**[05:05]** Bank of Australia, right? He's like, "Nature builds ant swarms and Claude

**[05:07]** "Nature builds ant swarms and Claude

**[05:07]** "Nature builds ant swarms and Claude Code built this huge muscular ant that's

**[05:09]** Code built this huge muscular ant that's

**[05:09]** Code built this huge muscular ant that's just going to bite you in half and take

**[05:10]** just going to bite you in half and take

**[05:10]** just going to bite you in half and take all your resources, right? I mean, it's

**[05:12]** all your resources, right? I mean, it's

**[05:12]** all your resources, right? I mean, it's a serious problem, right? If I say

**[05:14]** a serious problem, right? If I say

**[05:14]** a serious problem, right? If I say please analyze this codebase, I, you

**[05:15]** please analyze this codebase, I, you

**[05:15]** please analyze this codebase, I, you know, go to the expensive model." If I

**[05:17]** know, go to the expensive model." If I

**[05:17]** know, go to the expensive model." If I say, "Is my git ignore file still

**[05:19]** say, "Is my git ignore file still

**[05:19]** say, "Is my git ignore file still there?" I've also gone to the expensive

**[05:21]** there?" I've also gone to the expensive

**[05:21]** there?" I've also gone to the expensive model, right? Everything that you say

**[05:22]** model, right? Everything that you say

**[05:22]** model, right? Everything that you say goes to the expensive model. So, what's

**[05:24]** goes to the expensive model. So, what's

**[05:24]** goes to the expensive model. So, what's going to happen? Whoa. What happened? Oh

**[05:26]** going to happen? Whoa. What happened? Oh

**[05:26]** going to happen? Whoa. What happened? Oh gosh,

**[05:28]** gosh,

**[05:28]** gosh, my slides are all messed up now.

**[05:31]** my slides are all messed up now.

**[05:31]** my slides are all messed up now. >> Can you guys see them?

**[05:33]** >> Can you guys see them?

**[05:33]** >> Can you guys see them? >> No.

**[05:33]** >> No.

**[05:33]** >> No. >> Oh, this always happens to me, man.

**[05:35]** >> Oh, this always happens to me, man.

**[05:35]** >> Oh, this always happens to me, man. There something going on. All right. So,

**[05:37]** There something going on. All right. So,

**[05:37]** There something going on. All right. So, I thought of a really cool analogy

**[05:39]** I thought of a really cool analogy

**[05:39]** I thought of a really cool analogy called the diver the diver metaphor,

**[05:41]** called the diver the diver metaphor,

**[05:41]** called the diver the diver metaphor, which is your context window is like an

**[05:42]** which is your context window is like an

**[05:42]** which is your context window is like an oxygen tank. Okay. This is why these

**[05:45]** oxygen tank. Okay. This is why these

**[05:45]** oxygen tank. Okay. This is why these things are fundamentally wrong. Cuz

**[05:47]** things are fundamentally wrong. Cuz

**[05:47]** things are fundamentally wrong. Cuz you're sending a diver down into your

**[05:49]** you're sending a diver down into your

**[05:49]** you're sending a diver down into your code base underwater to swim around and

**[05:52]** code base underwater to swim around and

**[05:52]** code base underwater to swim around and take care of stuff for you. One diver

**[05:54]** take care of stuff for you. One diver

**[05:54]** take care of stuff for you. One diver and we're like, we're going to give him

**[05:56]** and we're like, we're going to give him

**[05:56]** and we're like, we're going to give him a bigger tank. 1 million tokens. He's

**[05:59]** a bigger tank. 1 million tokens. He's

**[05:59]** a bigger tank. 1 million tokens. He's still going to run out of oxygen. Like


### [06:00 - 07:00]

**[06:01]** still going to run out of oxygen. Like

**[06:01]** still going to run out of oxygen. Like you don't, right? You should send a

**[06:03]** you don't, right? You should send a

**[06:03]** you don't, right? You should send a product manager diver down first

**[06:06]** product manager diver down first

**[06:06]** product manager diver down first and then a coding diver, right? And then

**[06:09]** and then a coding diver, right? And then

**[06:09]** and then a coding diver, right? And then a review diver and a test diver and a

**[06:11]** a review diver and a test diver and a

**[06:11]** a review diver and a test diver and a get merge diver, etc. Right? Nobody's

**[06:13]** get merge diver, etc. Right? Nobody's

**[06:13]** get merge diver, etc. Right? Nobody's doing this. Everyone's building a bigger

**[06:15]** doing this. Everyone's building a bigger

**[06:15]** doing this. Everyone's building a bigger diver. I don't know my slides are all

**[06:17]** diver. I don't know my slides are all

**[06:17]** diver. I don't know my slides are all messed up. My my my talk is almost done.

**[06:19]** messed up. My my my talk is almost done.

**[06:19]** messed up. My my my talk is almost done. But um what we do is as engineers, task

**[06:23]** But um what we do is as engineers, task

**[06:23]** But um what we do is as engineers, task decomposition,

**[06:24]** decomposition,

**[06:24]** decomposition, successive refinement, components, black

**[06:26]** successive refinement, components, black

**[06:26]** successive refinement, components, black boxes. This is how it's going to be

**[06:28]** boxes. This is how it's going to be

**[06:28]** boxes. This is how it's going to be built in the future. And it's going to

**[06:29]** built in the future. And it's going to

**[06:29]** built in the future. And it's going to be built with lots and lots of agents,

**[06:32]** be built with lots and lots of agents,

**[06:32]** be built with lots and lots of agents, not just one agent.

**[06:34]** not just one agent.

**[06:34]** not just one agent. All right. Until then, I think we're out

**[06:36]** All right. Until then, I think we're out

**[06:36]** All right. Until then, I think we're out of time, but so until then, learn cloud

**[06:38]** of time, but so until then, learn cloud

**[06:38]** of time, but so until then, learn cloud code. Give up your IDE. Swix told me he

**[06:41]** code. Give up your IDE. Swix told me he

**[06:41]** code. Give up your IDE. Swix told me he wants some hot takes, so I'll give you

**[06:42]** wants some hot takes, so I'll give you

**[06:42]** wants some hot takes, so I'll give you one. If you're using an IDE starting on,

**[06:46]** one. If you're using an IDE starting on,

**[06:46]** one. If you're using an IDE starting on, I'll give you till January 1st.

**[06:49]** I'll give you till January 1st.

**[06:49]** I'll give you till January 1st. You're a bad engineer.

**[06:53]** You're a bad engineer.

**[06:53]** You're a bad engineer. There's your hot take. All right, folks.

**[06:57]** There's your hot take. All right, folks.

**[06:57]** There's your hot take. All right, folks. [applause]

**[06:58]** [applause]

**[06:58]** [applause] All right, cheers. Well, that that was


### [07:00 - 08:00]

**[07:00]** All right, cheers. Well, that that was

**[07:00]** All right, cheers. Well, that that was actually my talk. Um, [clears throat]

**[07:02]** actually my talk. Um, [clears throat]

**[07:02]** actually my talk. Um, [clears throat] uh, learn coding agents and Oh, yeah.

**[07:04]** uh, learn coding agents and Oh, yeah.

**[07:04]** uh, learn coding agents and Oh, yeah. Then there's this guy. Speaking [snorts]

**[07:06]** Then there's this guy. Speaking [snorts]

**[07:06]** Then there's this guy. Speaking [snorts] of bad engineers, so this is this is

**[07:08]** of bad engineers, so this is this is

**[07:08]** of bad engineers, so this is this is Jordan Hubard. uh who uh who's at Nvidia

**[07:11]** Jordan Hubard. uh who uh who's at Nvidia

**[07:11]** Jordan Hubard. uh who uh who's at Nvidia and he tweeted LinkedIn a really nice

**[07:14]** and he tweeted LinkedIn a really nice

**[07:14]** and he tweeted LinkedIn a really nice post on how to get the most out of

**[07:15]** post on how to get the most out of

**[07:15]** post on how to get the most out of agents and this guy responded with this

**[07:17]** agents and this guy responded with this

**[07:17]** agents and this guy responded with this right this is everyone in your or this

**[07:20]** right this is everyone in your or this

**[07:20]** right this is everyone in your or this is 60% of your org right here this guy's

**[07:22]** is 60% of your org right here this guy's

**[07:22]** is 60% of your org right here this guy's not an outlier okay the backlash is very

**[07:25]** not an outlier okay the backlash is very

**[07:25]** not an outlier okay the backlash is very real against this yeah and this is going

**[07:28]** real against this yeah and this is going

**[07:28]** real against this yeah and this is going to be a problem I'm not going to I'm not

**[07:29]** to be a problem I'm not going to I'm not

**[07:29]** to be a problem I'm not going to I'm not going to share with you I don't have

**[07:30]** going to share with you I don't have

**[07:30]** going to share with you I don't have time to share how to fix it but it's

**[07:31]** time to share how to fix it but it's

**[07:31]** time to share how to fix it but it's something you should be aware of and

**[07:33]** something you should be aware of and

**[07:33]** something you should be aware of and anyway I'm going to turn it over to my

**[07:34]** anyway I'm going to turn it over to my

**[07:34]** anyway I'm going to turn it over to my co-author Jean we had a lot to talk

**[07:36]** co-author Jean we had a lot to talk

**[07:36]** co-author Jean we had a lot to talk about he's got a lot to go so let's turn

**[07:37]** about he's got a lot to go so let's turn

**[07:38]** about he's got a lot to go so let's turn it over to Jean

**[07:38]** it over to Jean

**[07:38]** it over to Jean >> yeah Thank you, Steve.

**[07:41]** >> yeah Thank you, Steve.

**[07:41]** >> yeah Thank you, Steve. [applause]

**[07:42]** [applause]

**[07:42]** [applause] >> Yeah, by the way, um I have let me start

**[07:45]** >> Yeah, by the way, um I have let me start

**[07:46]** >> Yeah, by the way, um I have let me start off by introducing myself and then I'm

**[07:47]** off by introducing myself and then I'm

**[07:47]** off by introducing myself and then I'm going to share a little bit about like

**[07:48]** going to share a little bit about like

**[07:48]** going to share a little bit about like what it's been working like uh what's

**[07:49]** what it's been working like uh what's

**[07:50]** what it's been working like uh what's been like working with Steve on the VIP

**[07:51]** been like working with Steve on the VIP

**[07:51]** been like working with Steve on the VIP coding book. Uh and so just a little bit

**[07:53]** coding book. Uh and so just a little bit

**[07:53]** coding book. Uh and so just a little bit about myself. I've had the privilege of

**[07:54]** about myself. I've had the privilege of

**[07:54]** about myself. I've had the privilege of studying high performing technology

**[07:55]** studying high performing technology

**[07:56]** studying high performing technology organizations for 26 years. And that was

**[07:58]** organizations for 26 years. And that was

**[07:58]** organizations for 26 years. And that was a journey that started when I was a

**[07:59]** a journey that started when I was a

**[07:59]** a journey that started when I was a technical founder uh of a company called


### [08:00 - 09:00]

**[08:01]** technical founder uh of a company called

**[08:01]** technical founder uh of a company called Tripwire. I was there for 13 years. But

**[08:03]** Tripwire. I was there for 13 years. But

**[08:03]** Tripwire. I was there for 13 years. But our mission was really to understand

**[08:04]** our mission was really to understand

**[08:04]** our mission was really to understand these amazing high performing technology

**[08:06]** these amazing high performing technology

**[08:06]** these amazing high performing technology organizations. They had the best project

**[08:07]** organizations. They had the best project

**[08:07]** organizations. They had the best project due date, performance and development,

**[08:08]** due date, performance and development,

**[08:08]** due date, performance and development, the best operational reliability and

**[08:10]** the best operational reliability and

**[08:10]** the best operational reliability and stability and also the best posture of

**[08:12]** stability and also the best posture of

**[08:12]** stability and also the best posture of compliance uh security and compliance.

**[08:13]** compliance uh security and compliance.

**[08:13]** compliance uh security and compliance. So we want to understand how did those

**[08:15]** So we want to understand how did those

**[08:15]** So we want to understand how did those amazing organizations make their good to

**[08:16]** amazing organizations make their good to

**[08:16]** amazing organizations make their good to great transformation. So we got

**[08:18]** great transformation. So we got

**[08:18]** great transformation. So we got understand how did how do other

**[08:19]** understand how did how do other

**[08:19]** understand how did how do other organizations replicate those amazing

**[08:21]** organizations replicate those amazing

**[08:21]** organizations replicate those amazing outcomes and so you can imagine in that

**[08:22]** outcomes and so you can imagine in that

**[08:22]** outcomes and so you can imagine in that 26 year journey there are many

**[08:23]** 26 year journey there are many

**[08:23]** 26 year journey there are many surprises. Among the biggest surprise

**[08:25]** surprises. Among the biggest surprise

**[08:25]** surprises. Among the biggest surprise was how it took me into the middle of

**[08:26]** was how it took me into the middle of

**[08:26]** was how it took me into the middle of the DevOps movement which is so uh

**[08:28]** the DevOps movement which is so uh

**[08:28]** the DevOps movement which is so uh amazing because it reshaped technology

**[08:30]** amazing because it reshaped technology

**[08:30]** amazing because it reshaped technology organizations. you know, it changed how

**[08:31]** organizations. you know, it changed how

**[08:31]** organizations. you know, it changed how test and operations worked, information

**[08:33]** test and operations worked, information

**[08:33]** test and operations worked, information security. Um, and I thought that would

**[08:35]** security. Um, and I thought that would

**[08:35]** security. Um, and I thought that would be the most exciting adventure I'd be on

**[08:37]** be the most exciting adventure I'd be on

**[08:37]** be the most exciting adventure I'd be on in my career until I met Steve Yaggi in

**[08:39]** in my career until I met Steve Yaggi in

**[08:39]** in my career until I met Steve Yaggi in person. And so, I've admired his work

**[08:41]** person. And so, I've admired his work

**[08:41]** person. And so, I've admired his work for over 11 years. And so, some of you

**[08:43]** for over 11 years. And so, some of you

**[08:43]** for over 11 years. And so, some of you may have read this memo of Jeff Bezos's

**[08:46]** may have read this memo of Jeff Bezos's

**[08:46]** may have read this memo of Jeff Bezos's most audacious memo of how in early

**[08:48]** most audacious memo of how in early

**[08:48]** most audacious memo of how in early 2000s they transformed from a gigantic

**[08:50]** 2000s they transformed from a gigantic

**[08:50]** 2000s they transformed from a gigantic monolith that coupled 3,500 engineers

**[08:52]** monolith that coupled 3,500 engineers

**[08:52]** monolith that coupled 3,500 engineers together, so none of them had

**[08:53]** together, so none of them had

**[08:54]** together, so none of them had independent action. And uh he talked

**[08:56]** independent action. And uh he talked

**[08:56]** independent action. And uh he talked about how all teams must henceforth

**[08:58]** about how all teams must henceforth

**[08:58]** about how all teams must henceforth communicate and coordinate only through

**[08:59]** communicate and coordinate only through

**[08:59]** communicate and coordinate only through APIs. No back doors allowed. Right? Uh


### [09:00 - 10:00]

**[09:01]** APIs. No back doors allowed. Right? Uh

**[09:01]** APIs. No back doors allowed. Right? Uh anyone who doesn't do this will be

**[09:02]** anyone who doesn't do this will be

**[09:02]** anyone who doesn't do this will be fired. Thank you and have a nice day.

**[09:04]** fired. Thank you and have a nice day.

**[09:04]** fired. Thank you and have a nice day. And the amazing person who chronicled

**[09:05]** And the amazing person who chronicled

**[09:05]** And the amazing person who chronicled says number seven is obviously a joke

**[09:08]** says number seven is obviously a joke

**[09:08]** says number seven is obviously a joke because Bezos doesn't care whether you

**[09:09]** because Bezos doesn't care whether you

**[09:09]** because Bezos doesn't care whether you have a good day or not. And this is

**[09:11]** have a good day or not. And this is

**[09:11]** have a good day or not. And this is actually enforced by Amazon CIO then

**[09:13]** actually enforced by Amazon CIO then

**[09:13]** actually enforced by Amazon CIO then Rick Del. And so it turns out this memo

**[09:15]** Rick Del. And so it turns out this memo

**[09:15]** Rick Del. And so it turns out this memo that I've been quoting for 11 years uh

**[09:17]** that I've been quoting for 11 years uh

**[09:17]** that I've been quoting for 11 years uh was written by Steve Yaggi uh which was

**[09:19]** was written by Steve Yaggi uh which was

**[09:19]** was written by Steve Yaggi uh which was meant to be a private uh memo on Google+

**[09:22]** meant to be a private uh memo on Google+

**[09:22]** meant to be a private uh memo on Google+ which was made public which landed him

**[09:24]** which was made public which landed him

**[09:24]** which was made public which landed him on the front page of Wall Street

**[09:25]** on the front page of Wall Street

**[09:25]** on the front page of Wall Street Journal. Um and so I finally met him in

**[09:28]** Journal. Um and so I finally met him in

**[09:28]** Journal. Um and so I finally met him in uh June and it turns out that we had

**[09:30]** uh June and it turns out that we had

**[09:30]** uh June and it turns out that we had many things in common uh but one of them

**[09:32]** many things in common uh but one of them

**[09:32]** many things in common uh but one of them was this uh love of AI and this sense

**[09:34]** was this uh love of AI and this sense

**[09:34]** was this uh love of AI and this sense that AI was going to shape coding from

**[09:36]** that AI was going to shape coding from

**[09:36]** that AI was going to shape coding from underneath us. And so one of our beliefs

**[09:39]** underneath us. And so one of our beliefs

**[09:39]** underneath us. And so one of our beliefs is that uh the AI will reshape

**[09:41]** is that uh the AI will reshape

**[09:41]** is that uh the AI will reshape technology organizations you know maybe

**[09:42]** technology organizations you know maybe

**[09:42]** technology organizations you know maybe even 100 times larger than what agile

**[09:45]** even 100 times larger than what agile

**[09:45]** even 100 times larger than what agile cloud CI/CD and mobile did you know 10

**[09:48]** cloud CI/CD and mobile did you know 10

**[09:48]** cloud CI/CD and mobile did you know 10 years ago um and that these technology

**[09:50]** years ago um and that these technology

**[09:50]** years ago um and that these technology breakthroughs not just reshape

**[09:51]** breakthroughs not just reshape

**[09:51]** breakthroughs not just reshape organizations but they reshape the

**[09:52]** organizations but they reshape the

**[09:52]** organizations but they reshape the entire economy the entire economy

**[09:54]** entire economy the entire economy

**[09:54]** entire economy the entire economy rearranges itself to take advantages of

**[09:56]** rearranges itself to take advantages of

**[09:56]** rearranges itself to take advantages of these you know wild new better ways of

**[09:58]** these you know wild new better ways of

**[09:58]** these you know wild new better ways of uh uh producing things and and uh so


### [10:00 - 11:00]

**[10:00]** uh uh producing things and and uh so

**[10:00]** uh uh producing things and and uh so over the last year and a half we've had

**[10:02]** over the last year and a half we've had

**[10:02]** over the last year and a half we've had a chance to look at these case studies I

**[10:03]** a chance to look at these case studies I

**[10:03]** a chance to look at these case studies I think give us a glimpse of what these uh

**[10:06]** think give us a glimpse of what these uh

**[10:06]** think give us a glimpse of what these uh what the shape of technology

**[10:07]** what the shape of technology

**[10:07]** what the shape of technology organizations look And so I'm going to

**[10:08]** organizations look And so I'm going to

**[10:08]** organizations look And so I'm going to share with that what we've learned. But

**[10:10]** share with that what we've learned. But

**[10:10]** share with that what we've learned. But here's maybe a hint. So some of you may

**[10:12]** here's maybe a hint. So some of you may

**[10:12]** here's maybe a hint. So some of you may know the work of Aen Cochraftoft. He was

**[10:13]** know the work of Aen Cochraftoft. He was

**[10:13]** know the work of Aen Cochraftoft. He was a cloud architect at Netflix, right? He

**[10:15]** a cloud architect at Netflix, right? He

**[10:15]** a cloud architect at Netflix, right? He was what who drove uh the uh entire

**[10:18]** was what who drove uh the uh entire

**[10:18]** was what who drove uh the uh entire Netflix infrastructure from a data

**[10:19]** Netflix infrastructure from a data

**[10:20]** Netflix infrastructure from a data center uh back in 2009 to running

**[10:22]** center uh back in 2009 to running

**[10:22]** center uh back in 2009 to running entirely in the AWS cloud. And so he

**[10:24]** entirely in the AWS cloud. And so he

**[10:24]** entirely in the AWS cloud. And so he wrote uh some months ago in 2011 some

**[10:26]** wrote uh some months ago in 2011 some

**[10:26]** wrote uh some months ago in 2011 some people got very upset in uh

**[10:28]** people got very upset in uh

**[10:28]** people got very upset in uh infrastructure and operations because

**[10:29]** infrastructure and operations because

**[10:30]** infrastructure and operations because they called it noopops, right? And

**[10:31]** they called it noopops, right? And

**[10:31]** they called it noopops, right? And everyone laughed back then, but he said,

**[10:32]** everyone laughed back then, but he said,

**[10:32]** everyone laughed back then, but he said, "Oh, don't you know uh it's happening

**[10:35]** "Oh, don't you know uh it's happening

**[10:35]** "Oh, don't you know uh it's happening again. And this time it might be called

**[10:37]** again. And this time it might be called

**[10:37]** again. And this time it might be called no dev, right? Not so funny now, right?

**[10:40]** no dev, right? Not so funny now, right?

**[10:40]** no dev, right? Not so funny now, right? So it's it's interesting, right? Because

**[10:41]** So it's it's interesting, right? Because

**[10:42]** So it's it's interesting, right? Because we heard this amazing presentation from

**[10:43]** we heard this amazing presentation from

**[10:43]** we heard this amazing presentation from Zapier about like how support ships and

**[10:45]** Zapier about like how support ships and

**[10:45]** Zapier about like how support ships and turns out designers are shipping, UX is

**[10:47]** turns out designers are shipping, UX is

**[10:47]** turns out designers are shipping, UX is shipping, right? Anyone who's been

**[10:48]** shipping, right? Anyone who's been

**[10:48]** shipping, right? Anyone who's been frustrated by developers uh who, you

**[10:50]** frustrated by developers uh who, you

**[10:50]** frustrated by developers uh who, you know, say get in line and you have to

**[10:52]** know, say get in line and you have to

**[10:52]** know, say get in line and you have to wait quarters or years or maybe never,

**[10:54]** wait quarters or years or maybe never,

**[10:54]** wait quarters or years or maybe never, right, are now suddenly in a position

**[10:55]** right, are now suddenly in a position

**[10:55]** right, are now suddenly in a position where you can actually vibe code your

**[10:56]** where you can actually vibe code your

**[10:56]** where you can actually vibe code your own features into production, right? And

**[10:58]** own features into production, right? And

**[10:58]** own features into production, right? And that reshapes technology organizations


### [11:00 - 12:00]

**[11:00]** that reshapes technology organizations

**[11:00]** that reshapes technology organizations and reshapes, you know, potentially the

**[11:01]** and reshapes, you know, potentially the

**[11:01]** and reshapes, you know, potentially the entire economy. And so uh uh Steve and I

**[11:04]** entire economy. And so uh uh Steve and I

**[11:04]** entire economy. And so uh uh Steve and I we've had the privilege of watching what

**[11:05]** we've had the privilege of watching what

**[11:05]** we've had the privilege of watching what happens you know when we change uh you

**[11:07]** happens you know when we change uh you

**[11:07]** happens you know when we change uh you know the way we uh deploy right it

**[11:09]** know the way we uh deploy right it

**[11:09]** know the way we uh deploy right it wasn't so long ago and 10 years ago uh I

**[11:12]** wasn't so long ago and 10 years ago uh I

**[11:12]** wasn't so long ago and 10 years ago uh I wrote a book called the Phoenix project

**[11:13]** wrote a book called the Phoenix project

**[11:13]** wrote a book called the Phoenix project where it was all about the catastrophic

**[11:15]** where it was all about the catastrophic

**[11:15]** where it was all about the catastrophic deployment would you believe uh that it

**[11:17]** deployment would you believe uh that it

**[11:17]** deployment would you believe uh that it was you know 10 years ago 15 years ago

**[11:19]** was you know 10 years ago 15 years ago

**[11:19]** was you know 10 years ago 15 years ago most organizations shipped once a year

**[11:21]** most organizations shipped once a year

**[11:21]** most organizations shipped once a year right and so I got to work on a project

**[11:23]** right and so I got to work on a project

**[11:23]** right and so I got to work on a project called the state of DevOps research it

**[11:24]** called the state of DevOps research it

**[11:24]** called the state of DevOps research it was a cross population study that

**[11:25]** was a cross population study that

**[11:26]** was a cross population study that spanned 36,000 respondents uh from 2013

**[11:29]** spanned 36,000 respondents uh from 2013

**[11:29]** spanned 36,000 respondents uh from 2013 to 2019 and what we found uh this was

**[11:31]** to 2019 and what we found uh this was

**[11:31]** to 2019 and what we found uh this was Dr. Nicole Forsrin and Jez Humble. Um,

**[11:34]** Dr. Nicole Forsrin and Jez Humble. Um,

**[11:34]** Dr. Nicole Forsrin and Jez Humble. Um, and what we found was that these high

**[11:35]** and what we found was that these high

**[11:35]** and what we found was that these high performers ship multiple times a day,

**[11:37]** performers ship multiple times a day,

**[11:37]** performers ship multiple times a day, right? They can ship in one hour or

**[11:39]** right? They can ship in one hour or

**[11:39]** right? They can ship in one hour or less. And you know, back in 2009, people

**[11:41]** less. And you know, back in 2009, people

**[11:41]** less. And you know, back in 2009, people thought, "Oh my gosh, multiple

**[11:42]** thought, "Oh my gosh, multiple

**[11:42]** thought, "Oh my gosh, multiple deployments per day, right? That's

**[11:43]** deployments per day, right? That's

**[11:43]** deployments per day, right? That's reckless and irresponsible, maybe even

**[11:45]** reckless and irresponsible, maybe even

**[11:45]** reckless and irresponsible, maybe even immoral, right? What sort of maniac

**[11:46]** immoral, right? What sort of maniac

**[11:46]** immoral, right? What sort of maniac would deploy multiple times a day,

**[11:48]** would deploy multiple times a day,

**[11:48]** would deploy multiple times a day, right? And yet, it's very common place

**[11:50]** right? And yet, it's very common place

**[11:50]** right? And yet, it's very common place these days. In fact, if you want to have

**[11:51]** these days. In fact, if you want to have

**[11:51]** these days. In fact, if you want to have great reliability profiles, you want to

**[11:52]** great reliability profiles, you want to

**[11:52]** great reliability profiles, you want to have short meantime to repair, you have

**[11:54]** have short meantime to repair, you have

**[11:54]** have short meantime to repair, you have to do smaller deployments more

**[11:55]** to do smaller deployments more

**[11:55]** to do smaller deployments more frequently." And I think we're now

**[11:57]** frequently." And I think we're now

**[11:57]** frequently." And I think we're now seeing these kind of case studies that

**[11:58]** seeing these kind of case studies that

**[11:58]** seeing these kind of case studies that show that this better way of coding,


### [12:00 - 13:00]

**[12:00]** show that this better way of coding,

**[12:00]** show that this better way of coding, right, where you don't type in code by

**[12:02]** right, where you don't type in code by

**[12:02]** right, where you don't type in code by hand might be, you know, just a vastly

**[12:04]** hand might be, you know, just a vastly

**[12:04]** hand might be, you know, just a vastly better way uh to create value. And so

**[12:06]** better way uh to create value. And so

**[12:06]** better way uh to create value. And so our definition of vibe coding that we

**[12:07]** our definition of vibe coding that we

**[12:07]** our definition of vibe coding that we put into the uh vibe coding book was

**[12:09]** put into the uh vibe coding book was

**[12:09]** put into the uh vibe coding book was that it's basically anything where you

**[12:10]** that it's basically anything where you

**[12:10]** that it's basically anything where you don't type in code by hand. And so for

**[12:12]** don't type in code by hand. And so for

**[12:12]** don't type in code by hand. And so for some of those of you who don't

**[12:13]** some of those of you who don't

**[12:13]** some of those of you who don't understand that, that's like sort of a

**[12:15]** understand that, that's like sort of a

**[12:15]** understand that, that's like sort of a uh typing an ID hunched over, right? And

**[12:17]** uh typing an ID hunched over, right? And

**[12:17]** uh typing an ID hunched over, right? And you're actually moving your fingers,

**[12:18]** you're actually moving your fingers,

**[12:18]** you're actually moving your fingers, right? That's sort of like how some

**[12:20]** right? That's sort of like how some

**[12:20]** right? That's sort of like how some people go into a dark room to develop

**[12:21]** people go into a dark room to develop

**[12:21]** people go into a dark room to develop photographs, right? Believe it or not,

**[12:23]** photographs, right? Believe it or not,

**[12:23]** photographs, right? Believe it or not, some people still do that. Um and and

**[12:25]** some people still do that. Um and and

**[12:25]** some people still do that. Um and and what I that's a great definition that we

**[12:27]** what I that's a great definition that we

**[12:27]** what I that's a great definition that we uh loved until uh Dar Ammedday u uh CEO

**[12:31]** uh loved until uh Dar Ammedday u uh CEO

**[12:31]** uh loved until uh Dar Ammedday u uh CEO and co-founder of um Anthropic he gave

**[12:34]** and co-founder of um Anthropic he gave

**[12:34]** and co-founder of um Anthropic he gave us an even better definition right the

**[12:35]** us an even better definition right the

**[12:35]** us an even better definition right the vibe coding is really the iterative

**[12:37]** vibe coding is really the iterative

**[12:37]** vibe coding is really the iterative conversation uh that results in AI

**[12:39]** conversation uh that results in AI

**[12:39]** conversation uh that results in AI writing your code and he said it's on

**[12:40]** writing your code and he said it's on

**[12:40]** writing your code and he said it's on one hand a beautiful term because it

**[12:43]** one hand a beautiful term because it

**[12:43]** one hand a beautiful term because it evokes this different way of coding but

**[12:45]** evokes this different way of coding but

**[12:45]** evokes this different way of coding but he said it's also somewhat misleading

**[12:47]** he said it's also somewhat misleading

**[12:47]** he said it's also somewhat misleading because it sounds jokey right uh but he

**[12:49]** because it sounds jokey right uh but he

**[12:49]** because it sounds jokey right uh but he said you know adanthropic there's no

**[12:51]** said you know adanthropic there's no

**[12:51]** said you know adanthropic there's no other game in town right I just thought

**[12:52]** other game in town right I just thought

**[12:52]** other game in town right I just thought that was just a beautiful way to evoke

**[12:54]** that was just a beautiful way to evoke

**[12:54]** that was just a beautiful way to evoke you know how important uh vibe coding

**[12:56]** you know how important uh vibe coding

**[12:56]** you know how important uh vibe coding is. Uh this is Dr. Eric Meyer. Um you

**[12:59]** is. Uh this is Dr. Eric Meyer. Um you

**[12:59]** is. Uh this is Dr. Eric Meyer. Um you he's probably considered one of the


### [13:00 - 14:00]

**[13:00]** he's probably considered one of the

**[13:00]** he's probably considered one of the greatest programming language designers

**[13:01]** greatest programming language designers

**[13:01]** greatest programming language designers of all time. Uh he was part of Visual

**[13:03]** of all time. Uh he was part of Visual

**[13:03]** of all time. Uh he was part of Visual Basic, CP, Link, Haskell. He created the

**[13:06]** Basic, CP, Link, Haskell. He created the

**[13:06]** Basic, CP, Link, Haskell. He created the hack programming language uh that

**[13:08]** hack programming language uh that

**[13:08]** hack programming language uh that migrated millions of lines of code at

**[13:09]** migrated millions of lines of code at

**[13:09]** migrated millions of lines of code at Meta, you know, within a year uh

**[13:11]** Meta, you know, within a year uh

**[13:11]** Meta, you know, within a year uh bringing static type checking to a bunch

**[13:13]** bringing static type checking to a bunch

**[13:13]** bringing static type checking to a bunch of PHP programmers and he said we are

**[13:16]** of PHP programmers and he said we are

**[13:16]** of PHP programmers and he said we are probably going to be the last generation

**[13:17]** probably going to be the last generation

**[13:17]** probably going to be the last generation of developers uh to write code by hand.

**[13:19]** of developers uh to write code by hand.

**[13:19]** of developers uh to write code by hand. So let's have fun doing it. Um, so one

**[13:23]** So let's have fun doing it. Um, so one

**[13:23]** So let's have fun doing it. Um, so one of the things and uh when uh Steve and I

**[13:24]** of the things and uh when uh Steve and I

**[13:24]** of the things and uh when uh Steve and I started working on the book last

**[13:25]** started working on the book last

**[13:25]** started working on the book last November was uh watching him spend

**[13:27]** November was uh watching him spend

**[13:27]** November was uh watching him spend hundreds of dollars a day on coding

**[13:29]** hundreds of dollars a day on coding

**[13:29]** hundreds of dollars a day on coding agents uh and just seemed so strange

**[13:32]** agents uh and just seemed so strange

**[13:32]** agents uh and just seemed so strange right um you know and so he's maxing out

**[13:34]** right um you know and so he's maxing out

**[13:34]** right um you know and so he's maxing out not just you know the uh the monthly

**[13:36]** not just you know the uh the monthly

**[13:36]** not just you know the uh the monthly subscriptions right but he's actually

**[13:38]** subscriptions right but he's actually

**[13:38]** subscriptions right but he's actually you know going way above and beyond that

**[13:40]** you know going way above and beyond that

**[13:40]** you know going way above and beyond that and yet uh you know things that we're

**[13:42]** and yet uh you know things that we're

**[13:42]** and yet uh you know things that we're hearing now is that as an engineer part

**[13:44]** hearing now is that as an engineer part

**[13:44]** hearing now is that as an engineer part of my job is that I need to be spending

**[13:45]** of my job is that I need to be spending

**[13:45]** of my job is that I need to be spending as much on tokens per day as my salary

**[13:48]** as much on tokens per day as my salary

**[13:48]** as much on tokens per day as my salary right so you know that think about like

**[13:50]** right so you know that think about like

**[13:50]** right so you know that think about like $500 to $1,000 a day, right? Because

**[13:52]** $500 to $1,000 a day, right? Because

**[13:52]** $500 to $1,000 a day, right? Because this is the mechanical advantage, the

**[13:53]** this is the mechanical advantage, the

**[13:53]** this is the mechanical advantage, the cognitive advantage that these tools are

**[13:55]** cognitive advantage that these tools are

**[13:55]** cognitive advantage that these tools are giving us, right? And as an engineer,

**[13:56]** giving us, right? And as an engineer,

**[13:56]** giving us, right? And as an engineer, right, I'm going to challenge myself to

**[13:58]** right, I'm going to challenge myself to

**[13:58]** right, I'm going to challenge myself to get that kind of value to deliver value

**[13:59]** get that kind of value to deliver value

**[13:59]** get that kind of value to deliver value to people who matter. Um, and so in the


### [14:00 - 15:00]

**[14:02]** to people who matter. Um, and so in the

**[14:02]** to people who matter. Um, and so in the book, we talk about, you know, why

**[14:03]** book, we talk about, you know, why

**[14:03]** book, we talk about, you know, why people would do this, right? And the,

**[14:05]** people would do this, right? And the,

**[14:05]** people would do this, right? And the, uh, acronym we came up with FAFO, right?

**[14:07]** uh, acronym we came up with FAFO, right?

**[14:07]** uh, acronym we came up with FAFO, right? Uh, the most obvious one is F for

**[14:09]** Uh, the most obvious one is F for

**[14:09]** Uh, the most obvious one is F for faster, right? Yeah, that's obviously

**[14:11]** faster, right? Yeah, that's obviously

**[14:11]** faster, right? Yeah, that's obviously true, but I think it's the most

**[14:12]** true, but I think it's the most

**[14:12]** true, but I think it's the most superficial and um part of why we do

**[14:16]** superficial and um part of why we do

**[14:16]** superficial and um part of why we do this because uh the second one is it

**[14:18]** this because uh the second one is it

**[14:18]** this because uh the second one is it lets us do more ambitious things, right?

**[14:21]** lets us do more ambitious things, right?

**[14:21]** lets us do more ambitious things, right? Uh the impossible becomes possible. Uh

**[14:23]** Uh the impossible becomes possible. Uh

**[14:23]** Uh the impossible becomes possible. Uh so that's one end of the spectrum. On

**[14:25]** so that's one end of the spectrum. On

**[14:25]** so that's one end of the spectrum. On the other end of the spectrum, you know,

**[14:26]** the other end of the spectrum, you know,

**[14:26]** the other end of the spectrum, you know, the uh the tedious and small tasks

**[14:28]** the uh the tedious and small tasks

**[14:28]** the uh the tedious and small tasks become free. One of the things I uh the

**[14:31]** become free. One of the things I uh the

**[14:31]** become free. One of the things I uh the uh interview of the cloud code team that

**[14:33]** uh interview of the cloud code team that

**[14:33]** uh interview of the cloud code team that I just loved was uh I think it was

**[14:35]** I just loved was uh I think it was

**[14:35]** I just loved was uh I think it was Katherine, she was said um uh one of the

**[14:37]** Katherine, she was said um uh one of the

**[14:38]** Katherine, she was said um uh one of the things we've noticed is that you know

**[14:39]** things we've noticed is that you know

**[14:39]** things we've noticed is that you know when customer issues come up uh instead

**[14:41]** when customer issues come up uh instead

**[14:41]** when customer issues come up uh instead of putting them on a jur backlog and you

**[14:43]** of putting them on a jur backlog and you

**[14:43]** of putting them on a jur backlog and you know arguing about it in the grooming

**[14:45]** know arguing about it in the grooming

**[14:45]** know arguing about it in the grooming sessions and so forth right we just fix

**[14:46]** sessions and so forth right we just fix

**[14:46]** sessions and so forth right we just fix it on the spot right and ship to

**[14:48]** it on the spot right and ship to

**[14:48]** it on the spot right and ship to production or whatever um you know

**[14:49]** production or whatever um you know

**[14:49]** production or whatever um you know within 30 minutes right and so yes it

**[14:51]** within 30 minutes right and so yes it

**[14:51]** within 30 minutes right and so yes it gets recorded but you know that whole

**[14:53]** gets recorded but you know that whole

**[14:53]** gets recorded but you know that whole sort of coordination cost you know just

**[14:55]** sort of coordination cost you know just

**[14:55]** sort of coordination cost you know just disappears right so again the impossible

**[14:56]** disappears right so again the impossible

**[14:56]** disappears right so again the impossible becomes possible right and uh the

**[14:59]** becomes possible right and uh the

**[14:59]** becomes possible right and uh the annoying things just become free. The


### [15:00 - 16:00]

**[15:01]** annoying things just become free. The

**[15:01]** annoying things just become free. The second A is uh um you know the ability

**[15:04]** second A is uh um you know the ability

**[15:04]** second A is uh um you know the ability to do things alone or more autonomously,

**[15:07]** to do things alone or more autonomously,

**[15:07]** to do things alone or more autonomously, right? And so um you know there's really

**[15:09]** right? And so um you know there's really

**[15:09]** right? And so um you know there's really two coordination costs are being

**[15:11]** two coordination costs are being

**[15:11]** two coordination costs are being alleviated here. One is you know if you

**[15:13]** alleviated here. One is you know if you

**[15:13]** alleviated here. One is you know if you ever have to wait for a developer or a

**[15:15]** ever have to wait for a developer or a

**[15:15]** ever have to wait for a developer or a team of developers, you know, to do what

**[15:17]** team of developers, you know, to do what

**[15:17]** team of developers, you know, to do what you need to do, right? You have to

**[15:19]** you need to do, right? You have to

**[15:19]** you need to do, right? You have to communicate and coordinate and

**[15:20]** communicate and coordinate and

**[15:20]** communicate and coordinate and synchronize and prioritize and cajul and

**[15:22]** synchronize and prioritize and cajul and

**[15:22]** synchronize and prioritize and cajul and escalate, you know, do all sorts of

**[15:24]** escalate, you know, do all sorts of

**[15:24]** escalate, you know, do all sorts of things to get them to care about the

**[15:25]** things to get them to care about the

**[15:25]** things to get them to care about the problem just as much as you do, right?

**[15:27]** problem just as much as you do, right?

**[15:27]** problem just as much as you do, right? And you know now you know with these

**[15:29]** And you know now you know with these

**[15:29]** And you know now you know with these amazing new miraculous technologies you

**[15:31]** amazing new miraculous technologies you

**[15:31]** amazing new miraculous technologies you can do them by yourself right so that's

**[15:33]** can do them by yourself right so that's

**[15:33]** can do them by yourself right so that's one coordination uh tax the other one is

**[15:35]** one coordination uh tax the other one is

**[15:35]** one coordination uh tax the other one is like even if you get someone to uh care

**[15:37]** like even if you get someone to uh care

**[15:37]** like even if you get someone to uh care about a problem as much as you uh they

**[15:39]** about a problem as much as you uh they

**[15:40]** about a problem as much as you uh they can't read your mind right and what

**[15:41]** can't read your mind right and what

**[15:41]** can't read your mind right and what we're finding is that these LLMs are

**[15:42]** we're finding is that these LLMs are

**[15:42]** we're finding is that these LLMs are just amazing intermediation vehicles

**[15:44]** just amazing intermediation vehicles

**[15:44]** just amazing intermediation vehicles right um you know just through an LLM

**[15:47]** right um you know just through an LLM

**[15:47]** right um you know just through an LLM you can coordinate with other functional

**[15:49]** you can coordinate with other functional

**[15:49]** you can coordinate with other functional specialties right through a markdown

**[15:50]** specialties right through a markdown

**[15:50]** specialties right through a markdown file right that's not the end right but

**[15:52]** file right that's not the end right but

**[15:52]** file right that's not the end right but it's just this amazing way uh to have

**[15:54]** it's just this amazing way uh to have

**[15:54]** it's just this amazing way uh to have these high bandwidth coordination so

**[15:56]** these high bandwidth coordination so

**[15:56]** these high bandwidth coordination so that you can essentially read each

**[15:57]** that you can essentially read each

**[15:57]** that you can essentially read each other's minds, you know, because shared

**[15:59]** other's minds, you know, because shared

**[15:59]** other's minds, you know, because shared outcomes require shared goals and shared


### [16:00 - 17:00]

**[16:00]** outcomes require shared goals and shared

**[16:00]** outcomes require shared goals and shared understanding. The second F is fun,

**[16:03]** understanding. The second F is fun,

**[16:03]** understanding. The second F is fun, right? Is that Steve says vibe coding is

**[16:05]** right? Is that Steve says vibe coding is

**[16:05]** right? Is that Steve says vibe coding is addictive. This is so true. I mean, I

**[16:07]** addictive. This is so true. I mean, I

**[16:07]** addictive. This is so true. I mean, I cannot I think what I love about the

**[16:09]** cannot I think what I love about the

**[16:09]** cannot I think what I love about the book is that it's a story about two guys

**[16:11]** book is that it's a story about two guys

**[16:11]** book is that it's a story about two guys who both thought their best days of

**[16:12]** who both thought their best days of

**[16:12]** who both thought their best days of coding were behind them, right? And

**[16:14]** coding were behind them, right? And

**[16:14]** coding were behind them, right? And found that, you know, it's entirely the

**[16:16]** found that, you know, it's entirely the

**[16:16]** found that, you know, it's entirely the opposite. Um, and I've had so much fun

**[16:19]** opposite. Um, and I've had so much fun

**[16:19]** opposite. Um, and I've had so much fun and uh, you know, I'm having to force

**[16:20]** and uh, you know, I'm having to force

**[16:20]** and uh, you know, I'm having to force myself to go to sleep at night because

**[16:22]** myself to go to sleep at night because

**[16:22]** myself to go to sleep at night because otherwise I'd be up till 2 or 3 in the

**[16:24]** otherwise I'd be up till 2 or 3 in the

**[16:24]** otherwise I'd be up till 2 or 3 in the morning every night. uh and you know so

**[16:26]** morning every night. uh and you know so

**[16:26]** morning every night. uh and you know so it's not all great but it certainly

**[16:28]** it's not all great but it certainly

**[16:28]** it's not all great but it certainly beats being boring or tedious or you

**[16:30]** beats being boring or tedious or you

**[16:30]** beats being boring or tedious or you know horrible and then optionality you

**[16:33]** know horrible and then optionality you

**[16:33]** know horrible and then optionality you know one of the things that uh I love

**[16:34]** know one of the things that uh I love

**[16:34]** know one of the things that uh I love about Switch is that he has a shared

**[16:36]** about Switch is that he has a shared

**[16:36]** about Switch is that he has a shared love of creating option value and he

**[16:38]** love of creating option value and he

**[16:38]** love of creating option value and he told us last night that option value is

**[16:39]** told us last night that option value is

**[16:40]** told us last night that option value is also important for poker players right

**[16:41]** also important for poker players right

**[16:41]** also important for poker players right because you never want to paint yourself

**[16:42]** because you never want to paint yourself

**[16:42]** because you never want to paint yourself in a corner so option value is um one of

**[16:45]** in a corner so option value is um one of

**[16:45]** in a corner so option value is um one of the biggest creators of economic value

**[16:48]** the biggest creators of economic value

**[16:48]** the biggest creators of economic value right modularity the reason why it's so

**[16:50]** right modularity the reason why it's so

**[16:50]** right modularity the reason why it's so powerful is because it creates option

**[16:52]** powerful is because it creates option

**[16:52]** powerful is because it creates option value uh and so just the fact that you

**[16:53]** value uh and so just the fact that you

**[16:53]** value uh and so just the fact that you can have so many more swings at bat you

**[16:55]** can have so many more swings at bat you

**[16:55]** can have so many more swings at bat you can do so many more parallel experiments

**[16:56]** can do so many more parallel experiments

**[16:56]** can do so many more parallel experiments right this is what v coding allows so

**[16:58]** right this is what v coding allows so

**[16:58]** right this is what v coding allows so this is gives us confidence that you


### [17:00 - 18:00]

**[17:00]** this is gives us confidence that you

**[17:00]** this is gives us confidence that you know this is not just uh this is a very

**[17:02]** know this is not just uh this is a very

**[17:02]** know this is not just uh this is a very powerful tool

**[17:04]** powerful tool

**[17:04]** powerful tool um uh here's a quote from Andy Glover

**[17:06]** um uh here's a quote from Andy Glover

**[17:06]** um uh here's a quote from Andy Glover that uh Steve Yaggi said is that you

**[17:08]** that uh Steve Yaggi said is that you

**[17:08]** that uh Steve Yaggi said is that you know as um for people who have this aha

**[17:11]** know as um for people who have this aha

**[17:11]** know as um for people who have this aha moment and position uh you know I think

**[17:13]** moment and position uh you know I think

**[17:13]** moment and position uh you know I think the instinct is how do we elevate

**[17:14]** the instinct is how do we elevate

**[17:14]** the instinct is how do we elevate everyone's productivity to be as

**[17:16]** everyone's productivity to be as

**[17:16]** everyone's productivity to be as productive as you are now being um you

**[17:19]** productive as you are now being um you

**[17:19]** productive as you are now being um you know that since you've had your aha

**[17:20]** know that since you've had your aha

**[17:20]** know that since you've had your aha moment so uh let me share with you maybe

**[17:23]** moment so uh let me share with you maybe

**[17:23]** moment so uh let me share with you maybe some of our top kind of uh exciting case

**[17:27]** some of our top kind of uh exciting case

**[17:27]** some of our top kind of uh exciting case studies that kind of give us a hint of

**[17:28]** studies that kind of give us a hint of

**[17:28]** studies that kind of give us a hint of the future. So uh I brought him to this

**[17:30]** the future. So uh I brought him to this

**[17:30]** the future. So uh I brought him to this conference called the enterprise

**[17:30]** conference called the enterprise

**[17:30]** conference called the enterprise technology leadership summit for uh 11

**[17:33]** technology leadership summit for uh 11

**[17:33]** technology leadership summit for uh 11 years now and Swix we had uh the honor

**[17:35]** years now and Swix we had uh the honor

**[17:35]** years now and Swix we had uh the honor of having Swix there talking about the

**[17:37]** of having Swix there talking about the

**[17:37]** of having Swix there talking about the rise of the AI engineer just this

**[17:38]** rise of the AI engineer just this

**[17:38]** rise of the AI engineer just this amazing prognostication. Uh this year we

**[17:41]** amazing prognostication. Uh this year we

**[17:41]** amazing prognostication. Uh this year we had a series of amazing uh case studies.

**[17:43]** had a series of amazing uh case studies.

**[17:43]** had a series of amazing uh case studies. One was uh Bruno Passos. spoke this year

**[17:45]** One was uh Bruno Passos. spoke this year

**[17:45]** One was uh Bruno Passos. spoke this year uh last year at this conference and he

**[17:47]** uh last year at this conference and he

**[17:47]** uh last year at this conference and he presented on uh their in their evolving

**[17:50]** presented on uh their in their evolving

**[17:50]** presented on uh their in their evolving experiment to elevate developer

**[17:51]** experiment to elevate developer

**[17:51]** experiment to elevate developer productivity across 3,000 developers. Um

**[17:54]** productivity across 3,000 developers. Um

**[17:54]** productivity across 3,000 developers. Um and this is at Booking.com, the world's

**[17:56]** and this is at Booking.com, the world's

**[17:56]** and this is at Booking.com, the world's largest travel agency and uh they're

**[17:58]** largest travel agency and uh they're

**[17:58]** largest travel agency and uh they're finding that they're getting double-

**[17:59]** finding that they're getting double-

**[17:59]** finding that they're getting double- digit increase in productivity, right?


### [18:00 - 19:00]

**[18:00]** digit increase in productivity, right?

**[18:00]** digit increase in productivity, right? Uh mergers are going in quicker, peer

**[18:03]** Uh mergers are going in quicker, peer

**[18:03]** Uh mergers are going in quicker, peer review times are uh smaller and and so

**[18:05]** review times are uh smaller and and so

**[18:05]** review times are uh smaller and and so forth, right? And so that's just we feel

**[18:07]** forth, right? And so that's just we feel

**[18:07]** forth, right? And so that's just we feel like that's a incomplete view of uh what

**[18:10]** like that's a incomplete view of uh what

**[18:10]** like that's a incomplete view of uh what people are achieving. Uh this is Shri

**[18:12]** people are achieving. Uh this is Shri

**[18:12]** people are achieving. Uh this is Shri Balakrishnan. uh he was head of product

**[18:14]** Balakrishnan. uh he was head of product

**[18:14]** Balakrishnan. uh he was head of product and technology at uh Travelopia. Uh so

**[18:16]** and technology at uh Travelopia. Uh so

**[18:16]** and technology at uh Travelopia. Uh so they're a $ 1.5 billion a year uh travel

**[18:19]** they're a $ 1.5 billion a year uh travel

**[18:19]** they're a $ 1.5 billion a year uh travel company and one of the things that uh he

**[18:21]** company and one of the things that uh he

**[18:21]** company and one of the things that uh he said is that uh you know they were able

**[18:23]** said is that uh you know they were able

**[18:23]** said is that uh you know they were able to uh replace a legacy application uh in

**[18:26]** to uh replace a legacy application uh in

**[18:26]** to uh replace a legacy application uh in 6 weeks with a pair of uh with a very

**[18:28]** 6 weeks with a pair of uh with a very

**[18:28]** 6 weeks with a pair of uh with a very small team. In fact one of his uh

**[18:30]** small team. In fact one of his uh

**[18:30]** small team. In fact one of his uh conclusions is that before we would need

**[18:32]** conclusions is that before we would need

**[18:32]** conclusions is that before we would need a team of eight people to do something

**[18:34]** a team of eight people to do something

**[18:34]** a team of eight people to do something meaningful, right? Six developers, a UX

**[18:36]** meaningful, right? Six developers, a UX

**[18:36]** meaningful, right? Six developers, a UX person and a product owner. And he said

**[18:38]** person and a product owner. And he said

**[18:38]** person and a product owner. And he said maybe these days it might be two. A

**[18:40]** maybe these days it might be two. A

**[18:40]** maybe these days it might be two. A developer and you know a a domain

**[18:42]** developer and you know a a domain

**[18:42]** developer and you know a a domain expert. In other words, as Kent Beck

**[18:43]** expert. In other words, as Kent Beck

**[18:43]** expert. In other words, as Kent Beck said, a person with a problem and a

**[18:45]** said, a person with a problem and a

**[18:45]** said, a person with a problem and a person who can solve it, right? Uh maybe

**[18:47]** person who can solve it, right? Uh maybe

**[18:48]** person who can solve it, right? Uh maybe maybe a pair of those teams, right? And

**[18:50]** maybe a pair of those teams, right? And

**[18:50]** maybe a pair of those teams, right? And so that's going to reshape I think you

**[18:51]** so that's going to reshape I think you

**[18:51]** so that's going to reshape I think you know how they can go further and faster.

**[18:54]** know how they can go further and faster.

**[18:54]** know how they can go further and faster. Uh so again, maybe just a hint of what

**[18:56]** Uh so again, maybe just a hint of what

**[18:56]** Uh so again, maybe just a hint of what teams will look like in the future. This

**[18:58]** teams will look like in the future. This

**[18:58]** teams will look like in the future. This is the one that excites me most. This is

**[18:59]** is the one that excites me most. This is

**[18:59]** is the one that excites me most. This is Dr. Top Pal. Uh he helped drive the


### [19:00 - 20:00]

**[19:01]** Dr. Top Pal. Uh he helped drive the

**[19:02]** Dr. Top Pal. Uh he helped drive the DevOps movement at Capital One. Um and

**[19:04]** DevOps movement at Capital One. Um and

**[19:04]** DevOps movement at Capital One. Um and he's now at uh uh Fidelity. And so um

**[19:08]** he's now at uh uh Fidelity. And so um

**[19:08]** he's now at uh uh Fidelity. And so um among other things he owns an

**[19:09]** among other things he owns an

**[19:09]** among other things he owns an application uh that is the application

**[19:12]** application uh that is the application

**[19:12]** application uh that is the application you go to asks which applications you

**[19:13]** you go to asks which applications you

**[19:14]** you go to asks which applications you know the 25,000 applications there have

**[19:15]** know the 25,000 applications there have

**[19:16]** know the 25,000 applications there have log 4j right and uh it's his team and

**[19:19]** log 4j right and uh it's his team and

**[19:19]** log 4j right and uh it's his team and he's had this vision of what this

**[19:20]** he's had this vision of what this

**[19:20]** he's had this vision of what this application should look like uh but

**[19:22]** application should look like uh but

**[19:22]** application should look like uh but every time he asked like can can we

**[19:23]** every time he asked like can can we

**[19:23]** every time he asked like can can we build it his team would say it would

**[19:25]** build it his team would say it would

**[19:25]** build it his team would say it would take about 5 months right and we'd hire

**[19:27]** take about 5 months right and we'd hire

**[19:27]** take about 5 months right and we'd hire need to hire a front-end person and

**[19:29]** need to hire a front-end person and

**[19:29]** need to hire a front-end person and [clears throat] he got so frustrated

**[19:30]** [clears throat] he got so frustrated

**[19:30]** [clears throat] he got so frustrated that he spent 5 days just vibe coding it

**[19:32]** that he spent 5 days just vibe coding it

**[19:32]** that he spent 5 days just vibe coding it by himself right uh you know directly

**[19:34]** by himself right uh you know directly

**[19:34]** by himself right uh you know directly accessing read only the neo4 4j uh

**[19:37]** accessing read only the neo4 4j uh

**[19:37]** accessing read only the neo4 4j uh database um and put it into production,

**[19:39]** database um and put it into production,

**[19:39]** database um and put it into production, right? And so I think we're seeing a

**[19:41]** right? And so I think we're seeing a

**[19:41]** right? And so I think we're seeing a world where um you know leaders even

**[19:44]** world where um you know leaders even

**[19:44]** world where um you know leaders even leaders with their own teams are

**[19:46]** leaders with their own teams are

**[19:46]** leaders with their own teams are frustrated saying hey I can do this uh

**[19:48]** frustrated saying hey I can do this uh

**[19:48]** frustrated saying hey I can do this uh can I do this better myself not better

**[19:50]** can I do this better myself not better

**[19:50]** can I do this better myself not better just can I prove that it can be done and

**[19:52]** just can I prove that it can be done and

**[19:52]** just can I prove that it can be done and uh by the way what happened afterwards

**[19:54]** uh by the way what happened afterwards

**[19:54]** uh by the way what happened afterwards um he was looking around who can help me

**[19:55]** um he was looking around who can help me

**[19:55]** um he was looking around who can help me maintain my application production and

**[19:57]** maintain my application production and

**[19:57]** maintain my application production and all the senior engineers like not me. So

**[19:59]** all the senior engineers like not me. So


### [20:00 - 21:00]

**[20:00]** all the senior engineers like not me. So enter uh Swathy the most junior engineer

**[20:03]** enter uh Swathy the most junior engineer

**[20:03]** enter uh Swathy the most junior engineer on the team uh who is helping maintain

**[20:04]** on the team uh who is helping maintain

**[20:04]** on the team uh who is helping maintain this application and probably outarning

**[20:06]** this application and probably outarning

**[20:06]** this application and probably outarning you know everybody in the organization

**[20:09]** you know everybody in the organization

**[20:09]** you know everybody in the organization uh and interestingly uh he he's also

**[20:11]** uh and interestingly uh he he's also

**[20:11]** uh and interestingly uh he he's also getting more headcount because the

**[20:13]** getting more headcount because the

**[20:13]** getting more headcount because the number of consumers of this application

**[20:14]** number of consumers of this application

**[20:14]** number of consumers of this application just increased by 10fold right so who

**[20:16]** just increased by 10fold right so who

**[20:16]** just increased by 10fold right so who saw that coming right um so uh here's

**[20:20]** saw that coming right um so uh here's

**[20:20]** saw that coming right um so uh here's John Rouseer he's senior director of

**[20:21]** John Rouseer he's senior director of

**[20:21]** John Rouseer he's senior director of engineering at Cisco security and he

**[20:23]** engineering at Cisco security and he

**[20:23]** engineering at Cisco security and he convinces SVP to um require 100 of the

**[20:27]** convinces SVP to um require 100 of the

**[20:27]** convinces SVP to um require 100 of the top leaders inside of Cisco

**[20:29]** top leaders inside of Cisco

**[20:29]** top leaders inside of Cisco to vibe code one feature into production

**[20:31]** to vibe code one feature into production

**[20:31]** to vibe code one feature into production in a quarter that ended last month,

**[20:34]** in a quarter that ended last month,

**[20:34]** in a quarter that ended last month, [laughter] right? And so, um, you know,

**[20:36]** [laughter] right? And so, um, you know,

**[20:36]** [laughter] right? And so, um, you know, we're actually getting a chance to be

**[20:37]** we're actually getting a chance to be

**[20:37]** we're actually getting a chance to be able to survey those people, right? Who

**[20:39]** able to survey those people, right? Who

**[20:39]** able to survey those people, right? Who finished? Uh, you know, uh, how many

**[20:42]** finished? Uh, you know, uh, how many

**[20:42]** finished? Uh, you know, uh, how many completed, didn't complete, partially

**[20:44]** completed, didn't complete, partially

**[20:44]** completed, didn't complete, partially completed, etc. And of those who

**[20:45]** completed, etc. And of those who

**[20:45]** completed, etc. And of those who completed, right, what was what aha

**[20:47]** completed, right, what was what aha

**[20:48]** completed, right, what was what aha moment did they have? Uh, as a leader,

**[20:49]** moment did they have? Uh, as a leader,

**[20:50]** moment did they have? Uh, as a leader, what's the magnitude and direction of

**[20:51]** what's the magnitude and direction of

**[20:51]** what's the magnitude and direction of what they want to do? And so, we're

**[20:52]** what they want to do? And so, we're

**[20:52]** what they want to do? And so, we're going to go in and study that. And I

**[20:54]** going to go in and study that. And I

**[20:54]** going to go in and study that. And I just I my prediction is that we're going

**[20:55]** just I my prediction is that we're going

**[20:55]** just I my prediction is that we're going to see parts of that organization get

**[20:57]** to see parts of that organization get

**[20:57]** to see parts of that organization get reshaped as leaders realize kind of


### [21:00 - 22:00]

**[21:00]** reshaped as leaders realize kind of

**[21:00]** reshaped as leaders realize kind of what's possible. Everything from

**[21:01]** what's possible. Everything from

**[21:01]** what's possible. Everything from strategy to processes and so forth. And

**[21:04]** strategy to processes and so forth. And

**[21:04]** strategy to processes and so forth. And so let me just share with you one um you

**[21:06]** so let me just share with you one um you

**[21:06]** so let me just share with you one um you know thing that really excites me which

**[21:07]** know thing that really excites me which

**[21:08]** know thing that really excites me which is uh I got a chance to uh get back into

**[21:10]** is uh I got a chance to uh get back into

**[21:10]** is uh I got a chance to uh get back into the state of DevOps research the Dora

**[21:12]** the state of DevOps research the Dora

**[21:12]** the state of DevOps research the Dora study with uh um the Google cloud team

**[21:15]** study with uh um the Google cloud team

**[21:15]** study with uh um the Google cloud team and one of the things that didn't make

**[21:16]** and one of the things that didn't make

**[21:16]** and one of the things that didn't make into the report that I just found really

**[21:18]** into the report that I just found really

**[21:18]** into the report that I just found really exciting was around this. It was like

**[21:21]** exciting was around this. It was like

**[21:21]** exciting was around this. It was like what how much do people trust AI? And

**[21:23]** what how much do people trust AI? And

**[21:23]** what how much do people trust AI? And we're using a very strange definition of

**[21:25]** we're using a very strange definition of

**[21:25]** we're using a very strange definition of trust, which is to what degree can I

**[21:27]** trust, which is to what degree can I

**[21:27]** trust, which is to what degree can I predict how the other party will act and

**[21:28]** predict how the other party will act and

**[21:28]** predict how the other party will act and react, right? Because the more you trust

**[21:30]** react, right? Because the more you trust

**[21:30]** react, right? Because the more you trust the other party, right, you can give

**[21:31]** the other party, right, you can give

**[21:32]** the other party, right, you can give them bigger requests, you can use fewer

**[21:33]** them bigger requests, you can use fewer

**[21:33]** them bigger requests, you can use fewer words, you have less need for feedback,

**[21:35]** words, you have less need for feedback,

**[21:35]** words, you have less need for feedback, right? It's the whole notion of finger

**[21:36]** right? It's the whole notion of finger

**[21:36]** right? It's the whole notion of finger spits and fuel, right? Like you know how

**[21:38]** spits and fuel, right? Like you know how

**[21:38]** spits and fuel, right? Like you know how many of the 10,000 hours that requires

**[21:40]** many of the 10,000 hours that requires

**[21:40]** many of the 10,000 hours that requires to be good at anything have you used to

**[21:42]** to be good at anything have you used to

**[21:42]** to be good at anything have you used to get good at AI? And one of the stunning

**[21:44]** get good at AI? And one of the stunning

**[21:44]** get good at AI? And one of the stunning findings was that it's this line. So on

**[21:47]** findings was that it's this line. So on

**[21:47]** findings was that it's this line. So on the x-axis is how long have you been

**[21:49]** the x-axis is how long have you been

**[21:49]** the x-axis is how long have you been using AI tools? Y is how much do you

**[21:51]** using AI tools? Y is how much do you

**[21:51]** using AI tools? Y is how much do you trust it? Right? Right? And the longer

**[21:52]** trust it? Right? Right? And the longer

**[21:52]** trust it? Right? Right? And the longer you use AI, right, the more you trust

**[21:55]** you use AI, right, the more you trust

**[21:55]** you use AI, right, the more you trust it, right? So every every person who

**[21:56]** it, right? So every every person who

**[21:56]** it, right? So every every person who says, "I tried it and it's terrible at

**[21:58]** says, "I tried it and it's terrible at

**[21:58]** says, "I tried it and it's terrible at coding," right? On what basis did they


### [22:00 - 23:00]

**[22:01]** coding," right? On what basis did they

**[22:01]** coding," right? On what basis did they make that conclusion after maybe using

**[22:03]** make that conclusion after maybe using

**[22:03]** make that conclusion after maybe using for an hour or two? And what this shows

**[22:06]** for an hour or two? And what this shows

**[22:06]** for an hour or two? And what this shows us is that uh you know it requires

**[22:07]** us is that uh you know it requires

**[22:08]** us is that uh you know it requires practice, right? And and this is

**[22:09]** practice, right? And and this is

**[22:09]** practice, right? And and this is probably a teachable skill. Um so length

**[22:13]** probably a teachable skill. Um so length

**[22:13]** probably a teachable skill. Um so length of time on the x-axis is a very

**[22:14]** of time on the x-axis is a very

**[22:14]** of time on the x-axis is a very incomplete expression, right? It's like

**[22:16]** incomplete expression, right? It's like

**[22:16]** incomplete expression, right? It's like frequency and intensity and how many

**[22:17]** frequency and intensity and how many

**[22:17]** frequency and intensity and how many hours, but it's there's signal there. So

**[22:19]** hours, but it's there's signal there. So

**[22:19]** hours, but it's there's signal there. So it just shows that uh you know part of

**[22:22]** it just shows that uh you know part of

**[22:22]** it just shows that uh you know part of your job is to help other people have

**[22:23]** your job is to help other people have

**[22:23]** your job is to help other people have the aha moment and then help them you

**[22:26]** the aha moment and then help them you

**[22:26]** the aha moment and then help them you practice right so they get very very

**[22:27]** practice right so they get very very

**[22:28]** practice right so they get very very good at it so they can use every one of

**[22:29]** good at it so they can use every one of

**[22:29]** good at it so they can use every one of these amazing technologies to achieve

**[22:32]** these amazing technologies to achieve

**[22:32]** these amazing technologies to achieve their goals. So uh I'll leave you with

**[22:34]** their goals. So uh I'll leave you with

**[22:34]** their goals. So uh I'll leave you with one last kind of vision. Steve and I we

**[22:37]** one last kind of vision. Steve and I we

**[22:37]** one last kind of vision. Steve and I we did a vibe coding workshop for leaders

**[22:39]** did a vibe coding workshop for leaders

**[22:39]** did a vibe coding workshop for leaders um back six weeks ago and what was

**[22:42]** um back six weeks ago and what was

**[22:42]** um back six weeks ago and what was amazing to me was in the 3 hours we had

**[22:46]** amazing to me was in the 3 hours we had

**[22:46]** amazing to me was in the 3 hours we had a 100% completion rate. Everyone built

**[22:48]** a 100% completion rate. Everyone built

**[22:48]** a 100% completion rate. Everyone built something, you know, they built a data

**[22:49]** something, you know, they built a data

**[22:49]** something, you know, they built a data visualization tool. In fact, uh, one

**[22:51]** visualization tool. In fact, uh, one

**[22:51]** visualization tool. In fact, uh, one person uh, built a an iOS app and

**[22:54]** person uh, built a an iOS app and

**[22:54]** person uh, built a an iOS app and another person actually got it into the

**[22:56]** another person actually got it into the

**[22:56]** another person actually got it into the review queue in the Apple iOS app store,

**[22:58]** review queue in the Apple iOS app store,

**[22:58]** review queue in the Apple iOS app store, [laughter] right? Which is which is


### [23:00 - 24:00]

**[23:00]** [laughter] right? Which is which is

**[23:00]** [laughter] right? Which is which is absolutely astonishing. Uh, and here's a

**[23:02]** absolutely astonishing. Uh, and here's a

**[23:02]** absolutely astonishing. Uh, and here's a guy named Roger Safner. He said, "I used

**[23:04]** guy named Roger Safner. He said, "I used

**[23:04]** guy named Roger Safner. He said, "I used to be a C MVP way back in the day. I

**[23:07]** to be a C MVP way back in the day. I

**[23:07]** to be a C MVP way back in the day. I haven't coded in 15 years." Uh, and he's

**[23:09]** haven't coded in 15 years." Uh, and he's

**[23:09]** haven't coded in 15 years." Uh, and he's showing off an app that helped him

**[23:11]** showing off an app that helped him

**[23:11]** showing off an app that helped him automate the process of getting checked

**[23:12]** automate the process of getting checked

**[23:12]** automate the process of getting checked in to Southwest Airlines until the bot

**[23:14]** in to Southwest Airlines until the bot

**[23:14]** in to Southwest Airlines until the bot detection tools come off. But look at

**[23:16]** detection tools come off. But look at

**[23:16]** detection tools come off. But look at look at the expression on his face. And

**[23:18]** look at the expression on his face. And

**[23:18]** look at the expression on his face. And so I think uh what we're seeing is like

**[23:19]** so I think uh what we're seeing is like

**[23:19]** so I think uh what we're seeing is like what happens when support ships right

**[23:21]** what happens when support ships right

**[23:21]** what happens when support ships right and support codes and ships when leaders

**[23:23]** and support codes and ships when leaders

**[23:23]** and support codes and ships when leaders code and ship. And there's no doubt in

**[23:24]** code and ship. And there's no doubt in

**[23:24]** code and ship. And there's no doubt in my mind that this will reshape uh

**[23:26]** my mind that this will reshape uh

**[23:26]** my mind that this will reshape uh technology organizations. If you're one

**[23:28]** technology organizations. If you're one

**[23:28]** technology organizations. If you're one of those, Stephen, I want to talk to

**[23:29]** of those, Stephen, I want to talk to

**[23:29]** of those, Stephen, I want to talk to you, right? Because you are on the

**[23:30]** you, right? Because you are on the

**[23:30]** you, right? Because you are on the frontier of something really, really

**[23:32]** frontier of something really, really

**[23:32]** frontier of something really, really important. I'll share with you a couple

**[23:33]** important. I'll share with you a couple

**[23:33]** important. I'll share with you a couple quotes. Here's from a technology leader.

**[23:35]** quotes. Here's from a technology leader.

**[23:35]** quotes. Here's from a technology leader. When I told my team that I wrote an app

**[23:37]** When I told my team that I wrote an app

**[23:37]** When I told my team that I wrote an app that, you know, an AI wrote 60,000 lines

**[23:39]** that, you know, an AI wrote 60,000 lines

**[23:39]** that, you know, an AI wrote 60,000 lines of code and I haven't looked at any of

**[23:40]** of code and I haven't looked at any of

**[23:40]** of code and I haven't looked at any of it, they all looked at me as if they

**[23:42]** it, they all looked at me as if they

**[23:42]** it, they all looked at me as if they wished I were dead.

**[23:45]** wished I were dead.

**[23:45]** wished I were dead. Um, we've uh we've had these stupid

**[23:47]** Um, we've uh we've had these stupid

**[23:47]** Um, we've uh we've had these stupid problems in legacy applications that

**[23:49]** problems in legacy applications that

**[23:49]** problems in legacy applications that have been there for over a decade. We

**[23:51]** have been there for over a decade. We

**[23:51]** have been there for over a decade. We got a group of senior engineers

**[23:52]** got a group of senior engineers

**[23:52]** got a group of senior engineers together. We used AI to generate a fix

**[23:54]** together. We used AI to generate a fix

**[23:54]** together. We used AI to generate a fix and we submitted PR and the team

**[23:56]** and we submitted PR and the team

**[23:56]** and we submitted PR and the team accepted it. Right? Unlike the time when

**[23:58]** accepted it. Right? Unlike the time when

**[23:58]** accepted it. Right? Unlike the time when they said it was AI generated and they


### [24:00 - 25:00]

**[24:00]** they said it was AI generated and they

**[24:00]** they said it was AI generated and they rejected it as AI slop, right? So this

**[24:03]** rejected it as AI slop, right? So this

**[24:03]** rejected it as AI slop, right? So this is maybe happening in your

**[24:04]** is maybe happening in your

**[24:04]** is maybe happening in your organizations. Um, our code velocity is

**[24:06]** organizations. Um, our code velocity is

**[24:06]** organizations. Um, our code velocity is so high. Uh, we've concluded that we can

**[24:08]** so high. Uh, we've concluded that we can

**[24:08]** so high. Uh, we've concluded that we can only have one engineer per repo, right?

**[24:10]** only have one engineer per repo, right?

**[24:10]** only have one engineer per repo, right? Because of merge conflicts, right? So we

**[24:13]** Because of merge conflicts, right? So we

**[24:13]** Because of merge conflicts, right? So we haven't figured out the coordination

**[24:13]** haven't figured out the coordination

**[24:14]** haven't figured out the coordination cost uh mechanisms yet. And so like all

**[24:16]** cost uh mechanisms yet. And so like all

**[24:16]** cost uh mechanisms yet. And so like all these were some of the lessons that went

**[24:17]** these were some of the lessons that went

**[24:17]** these were some of the lessons that went into the vibe coding book. Thank you for

**[24:19]** into the vibe coding book. Thank you for

**[24:19]** into the vibe coding book. Thank you for everyone who were at the signing

**[24:20]** everyone who were at the signing

**[24:20]** everyone who were at the signing yesterday. And uh if you're interested

**[24:22]** yesterday. And uh if you're interested

**[24:22]** yesterday. And uh if you're interested in any of the talks we referenced and

**[24:24]** in any of the talks we referenced and

**[24:24]** in any of the talks we referenced and excerpts of our book in uh and basically

**[24:27]** excerpts of our book in uh and basically

**[24:27]** excerpts of our book in uh and basically uh all the links that are in this

**[24:29]** uh all the links that are in this

**[24:29]** uh all the links that are in this presentation, just send an email to real

**[24:30]** presentation, just send an email to real

**[24:30]** presentation, just send an email to real genelies.com

**[24:32]** genelies.com

**[24:32]** genelies.com subject line vibe and you'll get an

**[24:34]** subject line vibe and you'll get an

**[24:34]** subject line vibe and you'll get an automated response in a minute or two.

**[24:35]** automated response in a minute or two.

**[24:36]** automated response in a minute or two. So with that, Steve and I thank you for

**[24:37]** So with that, Steve and I thank you for

**[24:37]** So with that, Steve and I thank you for your time and we were around all week.

**[24:39]** your time and we were around all week.

**[24:39]** your time and we were around all week. Thanks all. [applause]

**[24:40]** Thanks all. [applause]

**[24:40]** Thanks all. [applause] Heat. [music]


