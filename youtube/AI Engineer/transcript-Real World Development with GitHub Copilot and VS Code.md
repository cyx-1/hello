# Real World Development with GitHub Copilot and VS Code

**Video URL:** https://www.youtube.com/watch?v=eOxOzcw70f0

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** We have um VIP coding at scale. It's a

**[00:17]** We have um VIP coding at scale. It's a talk I'm going to give at the expo in a

**[00:19]** talk I'm going to give at the expo in a

**[00:19]** talk I'm going to give at the expo in a very short version without all the

**[00:20]** very short version without all the

**[00:20]** very short version without all the hands-on stuff. So this is whatever how

**[00:22]** hands-on stuff. So this is whatever how

**[00:22]** hands-on stuff. So this is whatever how long this will take. It's all about VIP

**[00:25]** long this will take. It's all about VIP

**[00:25]** long this will take. It's all about VIP coding. So we're going to give fully

**[00:26]** coding. So we're going to give fully

**[00:26]** coding. So we're going to give fully into the vibes, embrace exponential and

**[00:29]** into the vibes, embrace exponential and

**[00:29]** into the vibes, embrace exponential and forget that code exists.

**[00:31]** forget that code exists.

**[00:32]** forget that code exists. It is about focusing on the output and

**[00:35]** It is about focusing on the output and

**[00:35]** It is about focusing on the output and not actually on the code. And that's

**[00:37]** not actually on the code. And that's

**[00:37]** not actually on the code. And that's where where people disagree like if I

**[00:38]** where where people disagree like if I

**[00:38]** where where people disagree like if I don't look at my code as an engineer,

**[00:41]** don't look at my code as an engineer,

**[00:41]** don't look at my code as an engineer, what am I? Um and then if what does even

**[00:44]** what am I? Um and then if what does even

**[00:44]** what am I? Um and then if what does even embracing exponentials mean in this

**[00:46]** embracing exponentials mean in this

**[00:46]** embracing exponentials mean in this case? So, and that's we're going to get

**[00:49]** case? So, and that's we're going to get

**[00:49]** case? So, and that's we're going to get into that and but we're definitely going

**[00:51]** into that and but we're definitely going

**[00:52]** into that and but we're definitely going to forget that code exists. And I think

**[00:54]** to forget that code exists. And I think

**[00:54]** to forget that code exists. And I think uh the at the anthropic conference two

**[00:57]** uh the at the anthropic conference two

**[00:57]** uh the at the anthropic conference two weeks ago was a great chart of how

**[00:59]** weeks ago was a great chart of how

**[00:59]** weeks ago was a great chart of how exponentially agents run longer and

### [01:00 - 02:00]

**[01:01]** exponentially agents run longer and

**[01:01]** exponentially agents run longer and longer and generate more and more code.

**[01:04]** longer and generate more and more code.

**[01:04]** longer and generate more and more code. So, slowly forgetting that code exists

**[01:06]** So, slowly forgetting that code exists

**[01:06]** So, slowly forgetting that code exists and you want to review every piece of

**[01:08]** and you want to review every piece of

**[01:08]** and you want to review every piece of code, but building trust and adding

**[01:10]** code, but building trust and adding

**[01:10]** code, but building trust and adding guardrails to the AI is what this talk

**[01:13]** guardrails to the AI is what this talk

**[01:13]** guardrails to the AI is what this talk is about.

**[01:16]** is about.

**[01:16]** is about. And his VIP coding journey starts kind

**[01:18]** And his VIP coding journey starts kind

**[01:18]** And his VIP coding journey starts kind of initially what people most people saw

**[01:21]** of initially what people most people saw

**[01:21]** of initially what people most people saw of just like I built an app in just one

**[01:23]** of just like I built an app in just one

**[01:23]** of just like I built an app in just one day and I put it online and I made money

**[01:25]** day and I put it online and I made money

**[01:25]** day and I put it online and I made money and I then things happened to the app

**[01:27]** and I then things happened to the app

**[01:28]** and I then things happened to the app and things got leaked and things were no

**[01:31]** and things got leaked and things were no

**[01:31]** and things got leaked and things were no longer fun and that that's that fun

**[01:33]** longer fun and that that's that fun

**[01:33]** longer fun and that that's that fun chaos state of vibe coding and we're

**[01:35]** chaos state of vibe coding and we're

**[01:35]** chaos state of vibe coding and we're trying to move to professionals then and

**[01:37]** trying to move to professionals then and

**[01:37]** trying to move to professionals then and that initial state is what I'm now

**[01:40]** that initial state is what I'm now

**[01:40]** that initial state is what I'm now terming yolo vibes. It's the unofficial

**[01:42]** terming yolo vibes. It's the unofficial

**[01:42]** terming yolo vibes. It's the unofficial wording, but it's all about creativity

**[01:45]** wording, but it's all about creativity

**[01:45]** wording, but it's all about creativity and speed and it's a good place to be.

**[01:47]** and speed and it's a good place to be.

**[01:47]** and speed and it's a good place to be. It's because there is instant

**[01:49]** It's because there is instant

**[01:49]** It's because there is instant gratification. It's getting things up.

**[01:51]** gratification. It's getting things up.

**[01:51]** gratification. It's getting things up. It's about learning. It's not about

**[01:54]** It's about learning. It's not about

**[01:54]** It's about learning. It's not about shipping products, but and so we need to

**[01:57]** shipping products, but and so we need to

**[01:57]** shipping products, but and so we need to get there.

**[01:59]** get there.

**[01:59]** get there. Second stage is structured wipes. It's

### [02:00 - 03:00]

**[02:01]** Second stage is structured wipes. It's

**[02:01]** Second stage is structured wipes. It's all about balance and sustainability

**[02:03]** all about balance and sustainability

**[02:03]** all about balance and sustainability like how do you bring mainten

**[02:05]** like how do you bring mainten

**[02:06]** like how do you bring mainten maintainability more readable code like

**[02:08]** maintainability more readable code like

**[02:08]** maintainability more readable code like things you might actually somebody in

**[02:10]** things you might actually somebody in

**[02:10]** things you might actually somebody in the end might want to read that code and

**[02:12]** the end might want to read that code and

**[02:12]** the end might want to read that code and you have a handover to somebody else and

**[02:15]** you have a handover to somebody else and

**[02:15]** you have a handover to somebody else and you want to have some quality control

**[02:16]** you want to have some quality control

**[02:16]** you want to have some quality control that what you built is maintainable and

**[02:20]** that what you built is maintainable and

**[02:20]** that what you built is maintainable and not just a throwaway project

**[02:23]** not just a throwaway project

**[02:23]** not just a throwaway project and lastly we get to spectrum vibes and

**[02:26]** and lastly we get to spectrum vibes and

**[02:26]** and lastly we get to spectrum vibes and if you have done anything on Reddit or

**[02:28]** if you have done anything on Reddit or

**[02:28]** if you have done anything on Reddit or on blocks in the in the past then few

**[02:31]** on blocks in the in the past then few

**[02:31]** on blocks in the in the past then few past few weeks you've probably seen

**[02:32]** past few weeks you've probably seen

**[02:32]** past few weeks you've probably seen people sharing their kind of best

**[02:33]** people sharing their kind of best

**[02:34]** people sharing their kind of best practices. This is how I finally got

**[02:35]** practices. This is how I finally got

**[02:35]** practices. This is how I finally got good value out of AI and those are those

**[02:38]** good value out of AI and those are those

**[02:38]** good value out of AI and those are those best practices are emerging but they

**[02:40]** best practices are emerging but they

**[02:40]** best practices are emerging but they bring you that scale, reliability and

**[02:43]** bring you that scale, reliability and

**[02:43]** bring you that scale, reliability and velocity that that comes with that while

**[02:46]** velocity that that comes with that while

**[02:46]** velocity that that comes with that while still hopefully giving you some speed

**[02:48]** still hopefully giving you some speed

**[02:48]** still hopefully giving you some speed and gratification along the way but

**[02:50]** and gratification along the way but

**[02:50]** and gratification along the way but reducing that chaos while maybe keeping

**[02:53]** reducing that chaos while maybe keeping

**[02:53]** reducing that chaos while maybe keeping the fun.

**[02:55]** the fun.

**[02:55]** the fun. So VIP coding initially where we see

**[02:58]** So VIP coding initially where we see

**[02:58]** So VIP coding initially where we see this outcome first as I said it's all

### [03:00 - 04:00]

**[03:01]** this outcome first as I said it's all

**[03:01]** this outcome first as I said it's all about no you not don't even want to look

**[03:03]** about no you not don't even want to look

**[03:03]** about no you not don't even want to look at the code like if you're in an editor

**[03:05]** at the code like if you're in an editor

**[03:05]** at the code like if you're in an editor and I see actually people framing their

**[03:07]** and I see actually people framing their

**[03:07]** and I see actually people framing their experience in AI editors of low code

**[03:11]** experience in AI editors of low code

**[03:11]** experience in AI editors of low code mode so they they just look at the chat

**[03:13]** mode so they they just look at the chat

**[03:13]** mode so they they just look at the chat panel and look at whatever comes out of

**[03:14]** panel and look at whatever comes out of

**[03:14]** panel and look at whatever comes out of it and that's the outcome first. It's

**[03:16]** it and that's the outcome first. It's

**[03:16]** it and that's the outcome first. It's all about natural language. It's all

**[03:18]** all about natural language. It's all

**[03:18]** all about natural language. It's all about just staying in the flow and doing

**[03:22]** about just staying in the flow and doing

**[03:22]** about just staying in the flow and doing working with the AI and it's about auto

**[03:25]** working with the AI and it's about auto

**[03:25]** working with the AI and it's about auto accepting changes. So until it maybe no

**[03:28]** accepting changes. So until it maybe no

**[03:28]** accepting changes. So until it maybe no longer works, we might want to undo but

**[03:30]** longer works, we might want to undo but

**[03:30]** longer works, we might want to undo but otherwise we just keep talking to I know

**[03:32]** otherwise we just keep talking to I know

**[03:32]** otherwise we just keep talking to I know you did this wrong. Try again. Um fix it

**[03:36]** you did this wrong. Try again. Um fix it

**[03:36]** you did this wrong. Try again. Um fix it or go to jail is a very popular one. So

**[03:39]** or go to jail is a very popular one. So

**[03:39]** or go to jail is a very popular one. So you can try all kind of but stay in

**[03:41]** you can try all kind of but stay in

**[03:41]** you can try all kind of but stay in natural language. Don't don't be too

**[03:43]** natural language. Don't don't be too

**[03:43]** natural language. Don't don't be too specific. So there is a use case for

**[03:46]** specific. So there is a use case for

**[03:46]** specific. So there is a use case for that though. You wanna get a sense for

**[03:49]** that though. You wanna get a sense for

**[03:49]** that though. You wanna get a sense for yolo vibe coding for rapid prototyping

**[03:52]** yolo vibe coding for rapid prototyping

**[03:52]** yolo vibe coding for rapid prototyping for proof of concepts where you just

**[03:54]** for proof of concepts where you just

**[03:54]** for proof of concepts where you just want to get something out. That's why I

**[03:55]** want to get something out. That's why I

**[03:56]** want to get something out. That's why I actually have a ton of conversations

**[03:57]** actually have a ton of conversations

**[03:57]** actually have a ton of conversations with larger companies who want to who

### [04:00 - 05:00]

**[04:00]** with larger companies who want to who

**[04:00]** with larger companies who want to who start a conversation like how can we do

**[04:02]** start a conversation like how can we do

**[04:02]** start a conversation like how can we do white coding and for them it's all about

**[04:05]** white coding and for them it's all about

**[04:05]** white coding and for them it's all about getting people who are non-technical to

**[04:07]** getting people who are non-technical to

**[04:07]** getting people who are non-technical to be able to communicate ideas. It's about

**[04:10]** be able to communicate ideas. It's about

**[04:10]** be able to communicate ideas. It's about UX people just making a mockup and being

**[04:12]** UX people just making a mockup and being

**[04:12]** UX people just making a mockup and being able to bring that to a meeting and

**[04:14]** able to bring that to a meeting and

**[04:14]** able to bring that to a meeting and being able to communicate what they want

**[04:16]** being able to communicate what they want

**[04:16]** being able to communicate what they want to do in the mockup. It's all about

**[04:18]** to do in the mockup. It's all about

**[04:18]** to do in the mockup. It's all about learning. Like I we had last uh two

**[04:21]** learning. Like I we had last uh two

**[04:21]** learning. Like I we had last uh two weeks ago at build we had one hour vibe

**[04:24]** weeks ago at build we had one hour vibe

**[04:24]** weeks ago at build we had one hour vibe coding on stage live and people build

**[04:27]** coding on stage live and people build

**[04:27]** coding on stage live and people build games and I use 3JS which I have tried

**[04:30]** games and I use 3JS which I have tried

**[04:30]** games and I use 3JS which I have tried many years ago but I haven't used 3JS in

**[04:33]** many years ago but I haven't used 3JS in

**[04:34]** many years ago but I haven't used 3JS in a while but once I got the code running

**[04:35]** a while but once I got the code running

**[04:35]** a while but once I got the code running I could start getting into how it is

**[04:37]** I could start getting into how it is

**[04:37]** I could start getting into how it is structured how does it make shapes and I

**[04:39]** structured how does it make shapes and I

**[04:39]** structured how does it make shapes and I could actually understand technology

**[04:41]** could actually understand technology

**[04:41]** could actually understand technology because I have something working and

**[04:44]** because I have something working and

**[04:44]** because I have something working and that's that's really the power of

**[04:45]** that's that's really the power of

**[04:45]** that's that's really the power of getting something up and running that

**[04:47]** getting something up and running that

**[04:47]** getting something up and running that that gives the technology something to

**[04:49]** that gives the technology something to

**[04:49]** that gives the technology something to hands on to actually try out and of

**[04:51]** hands on to actually try out and of

**[04:51]** hands on to actually try out and of course personal projects. So um I'm sure

**[04:54]** course personal projects. So um I'm sure

**[04:54]** course personal projects. So um I'm sure how many of you had s sit down with

**[04:56]** how many of you had s sit down with

**[04:56]** how many of you had s sit down with somebody who's non-technical and showed

**[04:57]** somebody who's non-technical and showed

**[04:57]** somebody who's non-technical and showed them vip coding and just build a your

**[04:59]** them vip coding and just build a your

**[04:59]** them vip coding and just build a your water tracking app or you build

### [05:00 - 06:00]

**[05:00]** water tracking app or you build

**[05:00]** water tracking app or you build something with your kids. There's all

**[05:02]** something with your kids. There's all

**[05:02]** something with your kids. There's all kind of personal projects you can now

**[05:05]** kind of personal projects you can now

**[05:05]** kind of personal projects you can now finally solve over the weekend thanks to

**[05:08]** finally solve over the weekend thanks to

**[05:08]** finally solve over the weekend thanks to yolo vibe coding.

**[05:10]** yolo vibe coding.

**[05:10]** yolo vibe coding. So let's do some yolo vibe coding. This

**[05:12]** So let's do some yolo vibe coding. This

**[05:12]** So let's do some yolo vibe coding. This is AI generated. So the images do

**[05:16]** is AI generated. So the images do

**[05:16]** is AI generated. So the images do reflect the vibe. So, this is really

**[05:17]** reflect the vibe. So, this is really

**[05:17]** reflect the vibe. So, this is really about voice input, relaxing. I guess

**[05:20]** about voice input, relaxing. I guess

**[05:20]** about voice input, relaxing. I guess coffee is in there as well, but let's

**[05:23]** coffee is in there as well, but let's

**[05:23]** coffee is in there as well, but let's get it going.

**[05:25]** get it going.

**[05:25]** get it going. Um,

**[05:30]** okay.

**[05:30]** okay. So, in VS Code for YOLO VIP code, we're

**[05:32]** So, in VS Code for YOLO VIP code, we're

**[05:32]** So, in VS Code for YOLO VIP code, we're going to start with an empty VS code.

**[05:35]** going to start with an empty VS code.

**[05:35]** going to start with an empty VS code. So, hit command shift N. Sorry.

**[05:38]** So, hit command shift N. Sorry.

**[05:38]** So, hit command shift N. Sorry. &gt;&gt; Are we supposed to use

**[05:39]** &gt;&gt; Are we supposed to use

**[05:39]** &gt;&gt; Are we supposed to use &gt;&gt; I might show off insider stuff, but all

**[05:41]** &gt;&gt; I might show off insider stuff, but all

**[05:41]** &gt;&gt; I might show off insider stuff, but all of what I'm showing is also unstable. If

**[05:43]** of what I'm showing is also unstable. If

**[05:43]** of what I'm showing is also unstable. If you have insiders, use insiders.

**[05:45]** you have insiders, use insiders.

**[05:45]** you have insiders, use insiders. Insiders is the pre-release version of

**[05:48]** Insiders is the pre-release version of

**[05:48]** Insiders is the pre-release version of VS code that ships on a daily basis like

**[05:51]** VS code that ships on a daily basis like

**[05:51]** VS code that ships on a daily basis like Firefox Nightly, uh, Chrome, Canary, Dev

**[05:55]** Firefox Nightly, uh, Chrome, Canary, Dev

**[05:55]** Firefox Nightly, uh, Chrome, Canary, Dev Ships Nightly.

**[05:58]** Ships Nightly.

**[05:58]** Ships Nightly. So on your left side, you will have no

**[05:59]** So on your left side, you will have no

**[05:59]** So on your left side, you will have no folder open. On your right side, you

### [06:00 - 07:00]

**[06:03]** folder open. On your right side, you

**[06:03]** folder open. On your right side, you will have co-pilot open. Everybody got

**[06:05]** will have co-pilot open. Everybody got

**[06:05]** will have co-pilot open. Everybody got this?

**[06:07]** this?

**[06:07]** this? Raise your hand. Cool. Awesome.

**[06:11]** Raise your hand. Cool. Awesome.

**[06:11]** Raise your hand. Cool. Awesome. So um who has used agent mode? Just

**[06:15]** So um who has used agent mode? Just

**[06:15]** So um who has used agent mode? Just checking so not have to explain

**[06:17]** checking so not have to explain

**[06:17]** checking so not have to explain everything. Okay, cool. So agent mode uh

**[06:19]** everything. Okay, cool. So agent mode uh

**[06:19]** everything. Okay, cool. So agent mode uh the probably the default you want to

**[06:21]** the probably the default you want to

**[06:21]** the probably the default you want to have set and default was setting. Um

**[06:24]** have set and default was setting. Um

**[06:24]** have set and default was setting. Um clots on four is great at front end

**[06:27]** clots on four is great at front end

**[06:27]** clots on four is great at front end stuff. So for me personally my my

**[06:29]** stuff. So for me personally my my

**[06:29]** stuff. So for me personally my my favorite big enough. Yeah.

**[06:32]** favorite big enough. Yeah.

**[06:32]** favorite big enough. Yeah. And now what's interesting so just one

**[06:34]** And now what's interesting so just one

**[06:34]** And now what's interesting so just one one quick tour of how we're going to do

**[06:36]** one quick tour of how we're going to do

**[06:36]** one quick tour of how we're going to do VIP coding is there's actually this

**[06:39]** VIP coding is there's actually this

**[06:39]** VIP coding is there's actually this interesting setting here. This is

**[06:40]** interesting setting here. This is

**[06:40]** interesting setting here. This is zooming. Yeah. Is news workspace in VS

**[06:44]** zooming. Yeah. Is news workspace in VS

**[06:44]** zooming. Yeah. Is news workspace in VS Code. And for this first round of VIPE

**[06:47]** Code. And for this first round of VIPE

**[06:47]** Code. And for this first round of VIPE coding, I want you to go into this tools

**[06:49]** coding, I want you to go into this tools

**[06:49]** coding, I want you to go into this tools picker down here and actually disable

**[06:52]** picker down here and actually disable

**[06:52]** picker down here and actually disable scaffold new workspace

**[06:55]** scaffold new workspace

**[06:55]** scaffold new workspace because it will help you scaffold your

**[06:57]** because it will help you scaffold your

**[06:57]** because it will help you scaffold your workspace, but it will lower the vibes

### [07:00 - 08:00]

**[07:00]** workspace, but it will lower the vibes

**[07:00]** workspace, but it will lower the vibes if you're just trying to do HTML

**[07:03]** if you're just trying to do HTML

**[07:03]** if you're just trying to do HTML coolness.

**[07:05]** coolness.

**[07:05]** coolness. &gt;&gt; Oh, yes. Uh tools picker down here.

**[07:08]** &gt;&gt; Oh, yes. Uh tools picker down here.

**[07:08]** &gt;&gt; Oh, yes. Uh tools picker down here. That's the little one. Uh, how to get

**[07:10]** That's the little one. Uh, how to get

**[07:10]** That's the little one. Uh, how to get into this menu? There's a tool this

**[07:12]** into this menu? There's a tool this

**[07:12]** into this menu? There's a tool this tools picker.

**[07:13]** tools picker.

**[07:13]** tools picker. &gt;&gt; Okay.

**[07:17]** Uh,

**[07:17]** Uh, &gt;&gt; oh,

**[07:19]** &gt;&gt; oh,

**[07:19]** &gt;&gt; oh, yes, it might be in. It was in a

**[07:21]** yes, it might be in. It was in a

**[07:21]** yes, it might be in. It was in a different spot before. Um, if you don't

**[07:22]** different spot before. Um, if you don't

**[07:22]** different spot before. Um, if you don't see, check that you're in agent mode.

**[07:24]** see, check that you're in agent mode.

**[07:24]** see, check that you're in agent mode. Otherwise, you don't have tools.

**[07:33]** &gt;&gt; Yes. Ask mode. Yeah. Okay. First step

**[07:33]** &gt;&gt; Yes. Ask mode. Yeah. Okay. First step into the panel is switch to agent mode

**[07:35]** into the panel is switch to agent mode

**[07:35]** into the panel is switch to agent mode down here. It should might be in ask by

**[07:37]** down here. It should might be in ask by

**[07:37]** down here. It should might be in ask by default.

**[07:38]** default.

**[07:38]** default. &gt;&gt; Yes, it is. Cool. And then second step,

**[07:41]** &gt;&gt; Yes, it is. Cool. And then second step,

**[07:41]** &gt;&gt; Yes, it is. Cool. And then second step, go into the tools menu, which only

**[07:44]** go into the tools menu, which only

**[07:44]** go into the tools menu, which only appears in agent mode. Soon agent mode

**[07:48]** appears in agent mode. Soon agent mode

**[07:48]** appears in agent mode. Soon agent mode is going to be default. And this whole

**[07:50]** is going to be default. And this whole

**[07:50]** is going to be default. And this whole where is my my tools picker is less of a

**[07:53]** where is my my tools picker is less of a

**[07:53]** where is my my tools picker is less of a problem.

**[07:55]** problem.

**[07:55]** problem. Okay. So, and then what you want to

**[07:57]** Okay. So, and then what you want to

**[07:57]** Okay. So, and then what you want to uncheck is this new section.

### [08:00 - 09:00]

**[08:00]** uncheck is this new section.

**[08:00]** uncheck is this new section. &gt;&gt; And we're going to check out new.

**[08:04]** &gt;&gt; And we're going to check out new.

**[08:04]** &gt;&gt; And we're going to check out new. &gt;&gt; Yes. Do you see nothing?

**[08:06]** &gt;&gt; Yes. Do you see nothing?

**[08:06]** &gt;&gt; Yes. Do you see nothing? &gt;&gt; I see those two items and nothing else.

**[08:09]** &gt;&gt; I see those two items and nothing else.

**[08:09]** &gt;&gt; I see those two items and nothing else. That's not enough. I I see more more

**[08:11]** That's not enough. I I see more more

**[08:11]** That's not enough. I I see more more see. Um you might be Yes, I think that's

**[08:16]** see. Um you might be Yes, I think that's

**[08:16]** see. Um you might be Yes, I think that's fine. Let me just

**[08:18]** fine. Let me just

**[08:18]** fine. Let me just &gt;&gt; shoot.

**[08:21]** &gt;&gt; shoot.

**[08:21]** &gt;&gt; shoot. &gt;&gt; Okay, good insider.

**[08:23]** &gt;&gt; Okay, good insider.

**[08:23]** &gt;&gt; Okay, good insider. Yes, I think this is actually it's very

**[08:25]** Yes, I think this is actually it's very

**[08:25]** Yes, I think this is actually it's very recent and we're actively working on

**[08:26]** recent and we're actively working on

**[08:26]** recent and we're actively working on that. So, keep it keep it checked. It's

**[08:28]** that. So, keep it keep it checked. It's

**[08:28]** that. So, keep it keep it checked. It's fine. So, let let's actually use it. Um

**[08:30]** fine. So, let let's actually use it. Um

**[08:30]** fine. So, let let's actually use it. Um let's start with our first VIP coding

**[08:32]** let's start with our first VIP coding

**[08:32]** let's start with our first VIP coding using because it's so hard to disable.

**[08:34]** using because it's so hard to disable.

**[08:34]** using because it's so hard to disable. And the way we're going to do this is um

**[08:37]** And the way we're going to do this is um

**[08:37]** And the way we're going to do this is um create a uh let's do react vite. And

**[08:41]** create a uh let's do react vite. And

**[08:41]** create a uh let's do react vite. And that's first lesson for VIP coding. Use

**[08:43]** that's first lesson for VIP coding. Use

**[08:43]** that's first lesson for VIP coding. Use stacks that are kind of popular in front

**[08:45]** stacks that are kind of popular in front

**[08:45]** stacks that are kind of popular in front end where the AI doesn't have to reason

**[08:47]** end where the AI doesn't have to reason

**[08:47]** end where the AI doesn't have to reason too much and make wild guesses. So react

**[08:50]** too much and make wild guesses. So react

**[08:50]** too much and make wild guesses. So react invite are good ways to run a project.

**[08:53]** invite are good ways to run a project.

**[08:53]** invite are good ways to run a project. Um website

**[08:56]** Um website

**[08:56]** Um website that for what do we do? Um hydration

### [09:00 - 10:00]

**[09:01]** that for what do we do? Um hydration

**[09:01]** that for what do we do? Um hydration tracking

**[09:03]** tracking

**[09:03]** tracking water hydration

**[09:06]** water hydration

**[09:06]** water hydration water consumption app

**[09:08]** water consumption app

**[09:08]** water consumption app simple

**[09:10]** simple

**[09:10]** simple and big accessible UI

**[09:14]** and big accessible UI

**[09:14]** and big accessible UI following uh what do we tell the AI to

**[09:17]** following uh what do we tell the AI to

**[09:17]** following uh what do we tell the AI to make it really beautiful? We tell it I

**[09:19]** make it really beautiful? We tell it I

**[09:19]** make it really beautiful? We tell it I like to tell it Apple

**[09:21]** like to tell it Apple

**[09:21]** like to tell it Apple design principles.

**[09:28]** You can infuse it with whatever design

**[09:28]** You can infuse it with whatever design sense you have. Mine is just make it

**[09:30]** sense you have. Mine is just make it

**[09:30]** sense you have. Mine is just make it look pretty which always helps somehow

**[09:33]** look pretty which always helps somehow

**[09:33]** look pretty which always helps somehow adding that extra. So right water

**[09:35]** adding that extra. So right water

**[09:35]** adding that extra. So right water tracking hydration and that's so we

**[09:38]** tracking hydration and that's so we

**[09:38]** tracking hydration and that's so we don't give it any constraints. We don't

**[09:39]** don't give it any constraints. We don't

**[09:39]** don't give it any constraints. We don't tell it how many buttons like is it

**[09:41]** tell it how many buttons like is it

**[09:41]** tell it how many buttons like is it mobile friendly? Is it not mobile

**[09:42]** mobile friendly? Is it not mobile

**[09:42]** mobile friendly? Is it not mobile friendly? Is it um what CSS language to

**[09:46]** friendly? Is it um what CSS language to

**[09:46]** friendly? Is it um what CSS language to use? Uh I might actually not do

**[09:49]** use? Uh I might actually not do

**[09:49]** use? Uh I might actually not do reactivite but might Oh yeah, let's do

**[09:51]** reactivite but might Oh yeah, let's do

**[09:51]** reactivite but might Oh yeah, let's do that with material design with material

**[09:55]** that with material design with material

**[09:55]** that with material design with material material design.

**[09:57]** material design.

**[09:57]** material design. So yeah, now we got a stack. We got a

**[09:59]** So yeah, now we got a stack. We got a

**[09:59]** So yeah, now we got a stack. We got a design direction and we tell told it to

### [10:00 - 11:00]

**[10:03]** design direction and we tell told it to

**[10:03]** design direction and we tell told it to make it pretty. Okay.

**[10:06]** make it pretty. Okay.

**[10:06]** make it pretty. Okay. And then hit run. So we're now in in a

**[10:10]** And then hit run. So we're now in in a

**[10:10]** And then hit run. So we're now in in a no folder state. So what's first

**[10:12]** no folder state. So what's first

**[10:12]** no folder state. So what's first happening? It's going to tell us to

**[10:13]** happening? It's going to tell us to

**[10:14]** happening? It's going to tell us to empty to open an empty folder. Everybody

**[10:16]** empty to open an empty folder. Everybody

**[10:16]** empty to open an empty folder. Everybody got that in there? Flow. Okay.

**[10:20]** got that in there? Flow. Okay.

**[10:20]** got that in there? Flow. Okay. It's going to hit continue. Now it's

**[10:22]** It's going to hit continue. Now it's

**[10:22]** It's going to hit continue. Now it's going to actually ask me to open a

**[10:23]** going to actually ask me to open a

**[10:23]** going to actually ask me to open a folder. Going to make a new folder.

**[10:25]** folder. Going to make a new folder.

**[10:25]** folder. Going to make a new folder. Vibing at

**[10:28]** Vibing at

**[10:28]** Vibing at NAI engineering.

**[10:32]** NAI engineering.

**[10:32]** NAI engineering. Put that anywhere

**[10:34]** Put that anywhere

**[10:34]** Put that anywhere where you put your stuff, where you put

**[10:36]** where you put your stuff, where you put

**[10:36]** where you put your stuff, where you put your code. And now it's actually opening

**[10:39]** your code. And now it's actually opening

**[10:39]** your code. And now it's actually opening a new folder and it's going to continue

**[10:41]** a new folder and it's going to continue

**[10:41]** a new folder and it's going to continue the setup. And to explain a bit what's

**[10:43]** the setup. And to explain a bit what's

**[10:43]** the setup. And to explain a bit what's happening here. So this is using the new

**[10:45]** happening here. So this is using the new

**[10:45]** happening here. So this is using the new command. A new command is is optimized

**[10:48]** command. A new command is is optimized

**[10:48]** command. A new command is is optimized for creating projects from scratch which

**[10:51]** for creating projects from scratch which

**[10:51]** for creating projects from scratch which if you look at the internet of how

**[10:53]** if you look at the internet of how

**[10:53]** if you look at the internet of how people evaluate AI coding tools is what

**[10:56]** people evaluate AI coding tools is what

**[10:56]** people evaluate AI coding tools is what every second person does. Can it make me

**[10:59]** every second person does. Can it make me

**[10:59]** every second person does. Can it make me a water tracking app? Can it make me a

### [11:00 - 12:00]

**[11:01]** a water tracking app? Can it make me a

**[11:02]** a water tracking app? Can it make me a movie database app? And so we optimize

**[11:04]** movie database app? And so we optimize

**[11:04]** movie database app? And so we optimize for this flow, but also it makes for

**[11:06]** for this flow, but also it makes for

**[11:06]** for this flow, but also it makes for this nice vibe coding from scratch

**[11:08]** this nice vibe coding from scratch

**[11:08]** this nice vibe coding from scratch because everybody struggles with what is

**[11:10]** because everybody struggles with what is

**[11:10]** because everybody struggles with what is the right stack? How do I get started?

**[11:12]** the right stack? How do I get started?

**[11:12]** the right stack? How do I get started? And this is what this is here for.

**[11:15]** And this is what this is here for.

**[11:15]** And this is what this is here for. Uh we got the latest. So we we can now

**[11:17]** Uh we got the latest. So we we can now

**[11:17]** Uh we got the latest. So we we can now review the commands. And this is maybe

**[11:20]** review the commands. And this is maybe

**[11:20]** review the commands. And this is maybe where we do the first tweak of our

**[11:22]** where we do the first tweak of our

**[11:22]** where we do the first tweak of our settings. So if you go into settings and

**[11:24]** settings. So if you go into settings and

**[11:24]** settings. So if you go into settings and search for approve, you will find the

**[11:27]** search for approve, you will find the

**[11:28]** search for approve, you will find the auto approve.

**[11:29]** auto approve.

**[11:29]** auto approve. That's the first rule of VIP coding. As

**[11:32]** That's the first rule of VIP coding. As

**[11:32]** That's the first rule of VIP coding. As we said, we we don't want to look at

**[11:34]** we said, we we don't want to look at

**[11:34]** we said, we we don't want to look at code and we just want to have the AI do

**[11:37]** code and we just want to have the AI do

**[11:37]** code and we just want to have the AI do stuff. So what you can do in my my case

**[11:41]** stuff. So what you can do in my my case

**[11:41]** stuff. So what you can do in my my case I'm going to actually go to over to

**[11:43]** I'm going to actually go to over to

**[11:43]** I'm going to actually go to over to workspace from user to workspace and

**[11:45]** workspace from user to workspace and

**[11:45]** workspace from user to workspace and that means that setting is only set for

**[11:47]** that means that setting is only set for

**[11:47]** that means that setting is only set for this workspace which is the safest way

**[11:49]** this workspace which is the safest way

**[11:49]** this workspace which is the safest way to use this setting. So use with caution

**[11:52]** to use this setting. So use with caution

**[11:52]** to use this setting. So use with caution are going to auto approve which means

**[11:54]** are going to auto approve which means

**[11:54]** are going to auto approve which means all of these continue buttons won't

**[11:57]** all of these continue buttons won't

**[11:57]** all of these continue buttons won't happen anymore and we're just going to

**[11:59]** happen anymore and we're just going to

**[11:59]** happen anymore and we're just going to get results. So check that box close it

### [12:00 - 13:00]

**[12:02]** get results. So check that box close it

**[12:02]** get results. So check that box close it again and we can hit continue here.

**[12:06]** again and we can hit continue here.

**[12:06]** again and we can hit continue here. This is using invite. This is fine. Now

**[12:08]** This is using invite. This is fine. Now

**[12:08]** This is using invite. This is fine. Now we're gonna stop worrying about the

**[12:10]** we're gonna stop worrying about the

**[12:10]** we're gonna stop worrying about the code. Uh but I can still read the plan.

**[12:12]** code. Uh but I can still read the plan.

**[12:12]** code. Uh but I can still read the plan. So install materiali dependencies create

**[12:14]** So install materiali dependencies create

**[12:14]** So install materiali dependencies create hydration tracking apple inspired design

**[12:16]** hydration tracking apple inspired design

**[12:16]** hydration tracking apple inspired design and project structure.

**[12:28]** why is there files already in here?

**[12:28]** why is there files already in here? Okay, cool.

**[12:38]** skips.

**[12:38]** skips. Where did it create? Oh,

**[12:47]** the music come from

**[12:47]** the music come from because I already did something. Cool.

**[12:48]** because I already did something. Cool.

**[12:48]** because I already did something. Cool. Okay, we're on. Yes, keep going.

**[12:55]** This case, I tried to create something

**[12:55]** This case, I tried to create something and then it ran another terminal

**[12:57]** and then it ran another terminal

**[12:57]** and then it ran another terminal command. Keep going. That's fine.

### [13:00 - 14:00]

**[13:02]** command. Keep going. That's fine.

**[13:02]** command. Keep going. That's fine. Is it doing stuff for you? Do you see

**[13:04]** Is it doing stuff for you? Do you see

**[13:04]** Is it doing stuff for you? Do you see things popping up?

**[13:22]** &gt;&gt; Oh, wait. Did we That was in the last

**[13:22]** &gt;&gt; Oh, wait. Did we That was in the last version.

**[13:39]** &gt;&gt; Let me let me check in VS Code stable.

**[13:39]** &gt;&gt; Let me let me check in VS Code stable. [Music]

**[13:42]** [Music]

**[13:42]** [Music] &gt;&gt; Yeah, that's my my problem of not being

**[13:44]** &gt;&gt; Yeah, that's my my problem of not being

**[13:44]** &gt;&gt; Yeah, that's my my problem of not being enough in stable. I shouldn't run

**[13:46]** enough in stable. I shouldn't run

**[13:46]** enough in stable. I shouldn't run workshops.

**[13:48]** workshops.

**[13:48]** workshops. There you go.

**[13:57]** &gt;&gt; Why is that different than

**[13:57]** &gt;&gt; Why is that different than &gt;&gt; So you found it in

**[13:59]** &gt;&gt; So you found it in

**[13:59]** &gt;&gt; So you found it in &gt;&gt; Thank you so much. There's two ways to

### [14:00 - 15:00]

**[14:02]** &gt;&gt; Thank you so much. There's two ways to

**[14:02]** &gt;&gt; Thank you so much. There's two ways to get to the same thing, but it's

**[14:03]** get to the same thing, but it's

**[14:03]** get to the same thing, but it's different menu.

**[14:05]** different menu.

**[14:05]** different menu. &gt;&gt; Oh, there

**[14:07]** &gt;&gt; Oh, there

**[14:07]** &gt;&gt; Oh, there &gt;&gt; the settings.

**[14:08]** &gt;&gt; the settings.

**[14:08]** &gt;&gt; the settings. &gt;&gt; There's settings from the bottom and

**[14:09]** &gt;&gt; There's settings from the bottom and

**[14:09]** &gt;&gt; There's settings from the bottom and settings from the top. They're not the

**[14:11]** settings from the top. They're not the

**[14:11]** settings from the top. They're not the same.

**[14:13]** same.

**[14:13]** same. &gt;&gt; Okay.

**[14:14]** &gt;&gt; Okay.

**[14:14]** &gt;&gt; Okay. &gt;&gt; I'm happy to go later. There's settings

**[14:17]** &gt;&gt; I'm happy to go later. There's settings

**[14:17]** &gt;&gt; I'm happy to go later. There's settings up here.

**[14:19]** up here.

**[14:19]** up here. &gt;&gt; I use the gear. I use the gear.

**[14:21]** &gt;&gt; I use the gear. I use the gear.

**[14:21]** &gt;&gt; I use the gear. I use the gear. &gt;&gt; Yeah.

**[14:31]** &gt;&gt; Okay. Where's the other one?

**[14:31]** &gt;&gt; Okay. Where's the other one? &gt;&gt; Oh, and the other setting. Yeah. Yeah. I

**[14:34]** &gt;&gt; Oh, and the other setting. Yeah. Yeah. I

**[14:34]** &gt;&gt; Oh, and the other setting. Yeah. Yeah. I have customized my UI too much as well.

**[14:37]** have customized my UI too much as well.

**[14:37]** have customized my UI too much as well. Cool. Question.

**[14:53]** Yes, that's that's what we I think I

**[14:53]** Yes, that's that's what we I think I should have said auto approved before.

**[14:54]** should have said auto approved before.

**[14:54]** should have said auto approved before. So, it's active for the chat session,

**[14:56]** So, it's active for the chat session,

**[14:56]** So, it's active for the chat session, but this is the setting I just showed is

**[14:57]** but this is the setting I just showed is

**[14:57]** but this is the setting I just showed is the is the auto approve. So, you all the

### [15:00 - 16:00]

**[15:00]** the is the auto approve. So, you all the

**[15:00]** the is the auto approve. So, you all the continue buttons are basically gone and

**[15:02]** continue buttons are basically gone and

**[15:02]** continue buttons are basically gone and it just autoroves.

**[15:05]** it just autoroves.

**[15:05]** it just autoroves. &gt;&gt; Yeah. Yeah. And for MCP tools, we

**[15:09]** &gt;&gt; Yeah. Yeah. And for MCP tools, we

**[15:09]** &gt;&gt; Yeah. Yeah. And for MCP tools, we actually do have drop downs to allow

**[15:11]** actually do have drop downs to allow

**[15:11]** actually do have drop downs to allow always allow for session and always

**[15:13]** always allow for session and always

**[15:13]** always allow for session and always allow for workspace and or not always

**[15:16]** allow for workspace and or not always

**[15:16]** allow for workspace and or not always allow. So there's some more fine grain

**[15:17]** allow. So there's some more fine grain

**[15:17]** allow. So there's some more fine grain things we're rolling out to more tools,

**[15:20]** things we're rolling out to more tools,

**[15:20]** things we're rolling out to more tools, but for Yep.

**[15:24]** but for Yep.

**[15:24]** but for Yep. &gt;&gt; Yeah, I think it's the auto proof is not

**[15:25]** &gt;&gt; Yeah, I think it's the auto proof is not

**[15:25]** &gt;&gt; Yeah, I think it's the auto proof is not applied to the current session. That's I

**[15:27]** applied to the current session. That's I

**[15:28]** applied to the current session. That's I showed it too late. I should have done

**[15:29]** showed it too late. I should have done

**[15:29]** showed it too late. I should have done it the other way around.

**[15:32]** it the other way around.

**[15:32]** it the other way around. Okay, we got some material design coming

**[15:34]** Okay, we got some material design coming

**[15:34]** Okay, we got some material design coming in. And this is where you need to get

**[15:37]** in. And this is where you need to get

**[15:37]** in. And this is where you need to get your coffee and just wait.

**[15:45]** &gt;&gt; That's a good idea. Let's do that. Okay.

**[15:45]** &gt;&gt; That's a good idea. Let's do that. Okay. Uh, open new window.

**[15:53]** Um, okay. What What prompt did we use?

**[15:53]** Um, okay. What What prompt did we use? Create a right. So, okay. Now, in the

**[15:55]** Create a right. So, okay. Now, in the

**[15:55]** Create a right. So, okay. Now, in the new window, I'm going to do autoproof

**[15:57]** new window, I'm going to do autoproof

**[15:57]** new window, I'm going to do autoproof first.

**[15:59]** first.

**[15:59]** first. Um,

### [16:00 - 17:00]

**[16:01]** Um,

**[16:01]** Um, approve.

**[16:03]** approve.

**[16:03]** approve. Auto proof is already on. That's good.

**[16:05]** Auto proof is already on. That's good.

**[16:05]** Auto proof is already on. That's good. Um, this is another window now. And

**[16:08]** Um, this is another window now. And

**[16:08]** Um, this is another window now. And we're going to do the same thing. And

**[16:09]** we're going to do the same thing. And

**[16:09]** we're going to do the same thing. And we're actually going to use material

**[16:11]** we're actually going to use material

**[16:11]** we're actually going to use material design. I guess is still out there,

**[16:12]** design. I guess is still out there,

**[16:12]** design. I guess is still out there, right? And or fluid. Fluent. That's the

**[16:16]** right? And or fluid. Fluent. That's the

**[16:16]** right? And or fluid. Fluent. That's the Microsoft one.

**[16:18]** Microsoft one.

**[16:18]** Microsoft one. Let's see what this looks like. Again,

**[16:21]** Let's see what this looks like. Again,

**[16:21]** Let's see what this looks like. Again, it's going to prompt me for a folder.

**[16:24]** it's going to prompt me for a folder.

**[16:24]** it's going to prompt me for a folder. Um, vibing

**[16:27]** Um, vibing

**[16:27]** Um, vibing at

**[16:29]** at

**[16:29]** at aie

**[16:31]** aie

**[16:31]** aie two.

**[16:33]** two.

**[16:33]** two. And this is I think one of the key

**[16:35]** And this is I think one of the key

**[16:35]** And this is I think one of the key takeaways like trying out different ways

**[16:38]** takeaways like trying out different ways

**[16:38]** takeaways like trying out different ways to get to the same result is where VIP

**[16:40]** to get to the same result is where VIP

**[16:40]** to get to the same result is where VIP coding really shines is continue

**[16:45]** coding really shines is continue

**[16:45]** coding really shines is continue is just trying I had really success of

**[16:47]** is just trying I had really success of

**[16:47]** is just trying I had really success of just like what are different signup

**[16:49]** just like what are different signup

**[16:49]** just like what are different signup flows that we can create like create

**[16:51]** flows that we can create like create

**[16:51]** flows that we can create like create three different versions of this design

**[16:52]** three different versions of this design

**[16:52]** three different versions of this design to explore what this could look like.

**[16:56]** to explore what this could look like.

**[16:56]** to explore what this could look like. Okay, it installed.

**[16:58]** Okay, it installed.

**[16:58]** Okay, it installed. It's up in the next in the in the one

### [17:00 - 18:00]

**[17:00]** It's up in the next in the in the one

**[17:00]** It's up in the next in the in the one script. And that's where it gets

**[17:01]** script. And that's where it gets

**[17:01]** script. And that's where it gets confusing. If you have multiple open now

**[17:03]** confusing. If you have multiple open now

**[17:03]** confusing. If you have multiple open now at the same time, you got to figure out

**[17:05]** at the same time, you got to figure out

**[17:05]** at the same time, you got to figure out what's running what. And now this flow

**[17:07]** what's running what. And now this flow

**[17:07]** what's running what. And now this flow actually over here runs without any

**[17:08]** actually over here runs without any

**[17:08]** actually over here runs without any confirmation. So we we set auto approve

**[17:10]** confirmation. So we we set auto approve

**[17:10]** confirmation. So we we set auto approve in a correct order.

**[17:12]** in a correct order.

**[17:12]** in a correct order. And it's now just creating v installing

**[17:16]** And it's now just creating v installing

**[17:16]** And it's now just creating v installing installing fluent.

**[17:23]** You notice that we got the wrong fluent

**[17:23]** You notice that we got the wrong fluent because there's a dependency. Now it's

**[17:26]** because there's a dependency. Now it's

**[17:26]** because there's a dependency. Now it's fixing those.

**[17:35]** &gt;&gt; Yes.

**[17:35]** &gt;&gt; Yes. &gt;&gt; So do I. Um I I do command comma is the

**[17:38]** &gt;&gt; So do I. Um I I do command comma is the

**[17:38]** &gt;&gt; So do I. Um I I do command comma is the quick way. So I don't use menus. I

**[17:41]** quick way. So I don't use menus. I

**[17:41]** quick way. So I don't use menus. I should use menus. Um so you go up here.

**[17:44]** should use menus. Um so you go up here.

**[17:44]** should use menus. Um so you go up here. I have my settings up here. Most

**[17:46]** I have my settings up here. Most

**[17:46]** I have my settings up here. Most probably have them on the other lower

**[17:47]** probably have them on the other lower

**[17:47]** probably have them on the other lower side. and you go in here and go into

**[17:50]** side. and you go in here and go into

**[17:50]** side. and you go in here and go into settings. And this is what it should

**[17:53]** settings. And this is what it should

**[17:53]** settings. And this is what it should look like.

**[17:54]** look like.

**[17:54]** look like. Do your settings look like this. And

**[17:57]** Do your settings look like this. And

**[17:57]** Do your settings look like this. And then if you look for approve

### [18:00 - 19:00]

**[18:00]** then if you look for approve

**[18:00]** then if you look for approve sorry can't type auto approve.

**[18:09]** Do you see it?

**[18:09]** Do you see it? It might be insiders.

**[18:15]** It's all blur.

**[18:16]** It's all blur. We're shipping on a monthly basis and I

**[18:18]** We're shipping on a monthly basis and I

**[18:18]** We're shipping on a monthly basis and I thought we tweeted about it end of last

**[18:19]** thought we tweeted about it end of last

**[18:19]** thought we tweeted about it end of last month. So,

**[18:22]** month. So,

**[18:22]** month. So, so you found it.

**[18:25]** so you found it.

**[18:25]** so you found it. Okay.

**[18:49]** The challenge is auto.

**[18:49]** The challenge is auto. &gt;&gt; Yeah. Yeah.

**[18:55]** &gt;&gt; Yeah.

**[18:55]** &gt;&gt; Yeah. &gt;&gt; I'm looking for that right now.

**[18:59]** &gt;&gt; I'm looking for that right now.

**[18:59]** &gt;&gt; I'm looking for that right now. &gt;&gt; Yeah.

### [19:00 - 20:00]

**[19:01]** &gt;&gt; Yeah. &gt;&gt; Yeah. The good thing the person who owns

**[19:03]** &gt;&gt; Yeah. The good thing the person who owns

**[19:03]** &gt;&gt; Yeah. The good thing the person who owns the AI terminal integration just came

**[19:05]** the AI terminal integration just came

**[19:05]** the AI terminal integration just came back from paternity leave. So we're back

**[19:07]** back from paternity leave. So we're back

**[19:07]** back from paternity leave. So we're back on the game to work on it. But the um

**[19:10]** on the game to work on it. But the um

**[19:10]** on the game to work on it. But the um there is definitely we've been looking

**[19:12]** there is definitely we've been looking

**[19:12]** there is definitely we've been looking at how to allow specific terminal

**[19:15]** at how to allow specific terminal

**[19:15]** at how to allow specific terminal commands and that's how most tools do

**[19:17]** commands and that's how most tools do

**[19:17]** commands and that's how most tools do it. But if you think about the scary

**[19:19]** it. But if you think about the scary

**[19:19]** it. But if you think about the scary parts of chaining and running multiple

**[19:21]** parts of chaining and running multiple

**[19:21]** parts of chaining and running multiple commands in one command. So terminals

**[19:23]** commands in one command. So terminals

**[19:23]** commands in one command. So terminals are not as predictive as you would think

**[19:26]** are not as predictive as you would think

**[19:26]** are not as predictive as you would think and how you can easily allow list

**[19:28]** and how you can easily allow list

**[19:28]** and how you can easily allow list things. So I've been mostly thinking

**[19:29]** things. So I've been mostly thinking

**[19:29]** things. So I've been mostly thinking about the how to do it right. Right.

**[19:37]** Okay. And I got two VIP coding sessions

**[19:37]** Okay. And I got two VIP coding sessions going on here. and hide this one. This

**[19:39]** going on here. and hide this one. This

**[19:39]** going on here. and hide this one. This is not this is for tomorrow.

**[19:43]** is not this is for tomorrow.

**[19:43]** is not this is for tomorrow. This vibing is happening.

**[19:45]** This vibing is happening.

**[19:46]** This vibing is happening. So what you see it creates an app tsx.

**[19:48]** So what you see it creates an app tsx.

**[19:48]** So what you see it creates an app tsx. It creates an app CSS. It also creates

**[19:49]** It creates an app CSS. It also creates

**[19:49]** It creates an app CSS. It also creates copilot instructions. Uh who's been

**[19:52]** copilot instructions. Uh who's been

**[19:52]** copilot instructions. Uh who's been using copot instructions before? Yeah.

**[19:55]** using copot instructions before? Yeah.

**[19:55]** using copot instructions before? Yeah. So that's that's one way. This out of

**[19:57]** So that's that's one way. This out of

**[19:57]** So that's that's one way. This out of the box experience just does things for

**[19:59]** the box experience just does things for

**[19:59]** the box experience just does things for you. It uh comes with instructions baked

### [20:00 - 21:00]

**[20:02]** you. It uh comes with instructions baked

**[20:02]** you. It uh comes with instructions baked in which is nice. It understands which

**[20:04]** in which is nice. It understands which

**[20:04]** in which is nice. It understands which stack you're using. That's mostly about

**[20:06]** stack you're using. That's mostly about

**[20:06]** stack you're using. That's mostly about it. It already captured my design

**[20:08]** it. It already captured my design

**[20:08]** it. It already captured my design principles that I eloquently put in

**[20:10]** principles that I eloquently put in

**[20:10]** principles that I eloquently put in please make it look like Apple and now

**[20:13]** please make it look like Apple and now

**[20:13]** please make it look like Apple and now it's actually there's a clean, minimal,

**[20:15]** it's actually there's a clean, minimal,

**[20:15]** it's actually there's a clean, minimal, intuitive interface, consistent UI and

**[20:18]** intuitive interface, consistent UI and

**[20:18]** intuitive interface, consistent UI and everything else.

**[20:20]** everything else.

**[20:20]** everything else. Uh it broke down the technical stack

**[20:22]** Uh it broke down the technical stack

**[20:22]** Uh it broke down the technical stack even things I haven't mentioned like CSS

**[20:24]** even things I haven't mentioned like CSS

**[20:24]** even things I haven't mentioned like CSS and responsive design. So it calls out

**[20:26]** and responsive design. So it calls out

**[20:26]** and responsive design. So it calls out some of the assumptions that AI will

**[20:28]** some of the assumptions that AI will

**[20:28]** some of the assumptions that AI will fill in if you give it a high level

**[20:30]** fill in if you give it a high level

**[20:30]** fill in if you give it a high level task.

**[20:36]** Okay, this is still working on the index

**[20:36]** Okay, this is still working on the index CSS and

**[20:38]** CSS and

**[20:38]** CSS and the other one is working on the HTML

**[20:42]** the other one is working on the HTML

**[20:42]** the other one is working on the HTML file.

**[20:44]** file.

**[20:44]** file. &gt;&gt; Yeah,

**[20:49]** &gt;&gt; it would just do it for it would usually

**[20:49]** &gt;&gt; it would just do it for it would usually do it as it creates the project. I

**[20:52]** do it as it creates the project. I

**[20:52]** do it as it creates the project. I haven't typed anything else so far in.

**[20:54]** haven't typed anything else so far in.

**[20:54]** haven't typed anything else so far in. We're just we're just vibing.

### [21:00 - 22:00]

**[21:04]** it. Um, here created one.

**[21:04]** it. Um, here created one. &gt;&gt; Let me see if it created one both.

**[21:07]** &gt;&gt; Let me see if it created one both.

**[21:07]** &gt;&gt; Let me see if it created one both. &gt;&gt; Okay, there we go.

**[21:09]** &gt;&gt; Okay, there we go.

**[21:09]** &gt;&gt; Okay, there we go. &gt;&gt; Our first app is done.

**[21:12]** &gt;&gt; Our first app is done.

**[21:12]** &gt;&gt; Our first app is done. Hydration tracker. Stay healthy. Stay

**[21:14]** Hydration tracker. Stay healthy. Stay

**[21:14]** Hydration tracker. Stay healthy. Stay hydrated. Today's progress. We're on a

**[21:16]** hydrated. Today's progress. We're on a

**[21:16]** hydrated. Today's progress. We're on a quick ad. 500 milliliters. And it went

**[21:19]** quick ad. 500 milliliters. And it went

**[21:19]** quick ad. 500 milliliters. And it went with metrics. Isn't that beautiful?

**[21:24]** with metrics. Isn't that beautiful?

**[21:24]** with metrics. Isn't that beautiful? Just how I wanted it. Maybe you got my

**[21:26]** Just how I wanted it. Maybe you got my

**[21:26]** Just how I wanted it. Maybe you got my accent. I don't know. Um, we can do plus

**[21:29]** accent. I don't know. Um, we can do plus

**[21:29]** accent. I don't know. Um, we can do plus minus.

**[21:30]** minus.

**[21:30]** minus. &gt;&gt; It's interesting how mine looks

**[21:31]** &gt;&gt; It's interesting how mine looks

**[21:31]** &gt;&gt; It's interesting how mine looks different.

**[21:32]** different.

**[21:32]** different. &gt;&gt; Yeah, I know. I know. So, does does

**[21:34]** &gt;&gt; Yeah, I know. I know. So, does does

**[21:34]** &gt;&gt; Yeah, I know. I know. So, does does everybody looks as nice as mine? Do you

**[21:37]** everybody looks as nice as mine? Do you

**[21:37]** everybody looks as nice as mine? Do you already see yours? Okay.

**[21:41]** already see yours? Okay.

**[21:41]** already see yours? Okay. &gt;&gt; Yeah, yours better.

**[21:44]** &gt;&gt; Yeah, yours better.

**[21:44]** &gt;&gt; Yeah, yours better. Yeah, that's this like a very wide open

**[21:47]** Yeah, that's this like a very wide open

**[21:47]** Yeah, that's this like a very wide open wipe coding workshop. Um, I ran these a

**[21:49]** wipe coding workshop. Um, I ran these a

**[21:49]** wipe coding workshop. Um, I ran these a few times and this is probably one of

**[21:50]** few times and this is probably one of

**[21:50]** few times and this is probably one of the nicer ones. So, um, but it's also I

**[21:53]** the nicer ones. So, um, but it's also I

**[21:53]** the nicer ones. So, um, but it's also I like actually running these with

**[21:54]** like actually running these with

**[21:54]** like actually running these with different models and getting a sense of

**[21:57]** different models and getting a sense of

**[21:57]** different models and getting a sense of how good each model is at design and

**[21:59]** how good each model is at design and

**[21:59]** how good each model is at design and having design sense without me telling

### [22:00 - 23:00]

**[22:02]** having design sense without me telling

**[22:02]** having design sense without me telling it how to do everything. And Claude is

**[22:05]** it how to do everything. And Claude is

**[22:05]** it how to do everything. And Claude is definitely usually rocking the the

**[22:08]** definitely usually rocking the the

**[22:08]** definitely usually rocking the the icons. It got the colors really nicely.

**[22:11]** icons. It got the colors really nicely.

**[22:11]** icons. It got the colors really nicely. So, uh, that's been great. This is a

**[22:13]** So, uh, that's been great. This is a

**[22:13]** So, uh, that's been great. This is a really nice app. So, now next on because

**[22:16]** really nice app. So, now next on because

**[22:16]** really nice app. So, now next on because we're visual like we haven't even

**[22:17]** we're visual like we haven't even

**[22:17]** we're visual like we haven't even checked the code. We haven't read the

**[22:18]** checked the code. We haven't read the

**[22:18]** checked the code. We haven't read the CSS. We haven't looked at the TSX. like

**[22:20]** CSS. We haven't looked at the TSX. like

**[22:20]** CSS. We haven't looked at the TSX. like is this still doing which is doing

**[22:22]** is this still doing which is doing

**[22:22]** is this still doing which is doing functional programming like how does it

**[22:24]** functional programming like how does it

**[22:24]** functional programming like how does it handle state I I don't I don't care it

**[22:26]** handle state I I don't I don't care it

**[22:26]** handle state I I don't I don't care it works so now you can actually do a new

**[22:29]** works so now you can actually do a new

**[22:29]** works so now you can actually do a new feature we landed you can now say

**[22:33]** feature we landed you can now say

**[22:33]** feature we landed you can now say work visually so I can now say this

**[22:35]** work visually so I can now say this

**[22:35]** work visually so I can now say this header up here I don't know what it's

**[22:37]** header up here I don't know what it's

**[22:37]** header up here I don't know what it's called like whatever progress indicator

**[22:39]** called like whatever progress indicator

**[22:39]** called like whatever progress indicator um let's make this

**[22:45]** um let's make this

**[22:45]** um let's make this uh more animated

**[22:48]** uh more animated

**[22:48]** uh more animated adding

**[22:50]** adding

**[22:50]** adding particles maybe

**[22:57]** that's good. So mu pet paper. So this is

**[22:57]** that's good. So mu pet paper. So this is all is this material design. This is

### [23:00 - 24:00]

**[23:00]** all is this material design. This is

**[23:00]** all is this material design. This is material design. Yeah.

**[23:03]** material design. Yeah.

**[23:03]** material design. Yeah. &gt;&gt; I didn't I hit start down here. If you

**[23:05]** &gt;&gt; I didn't I hit start down here. If you

**[23:05]** &gt;&gt; I didn't I hit start down here. If you have the browser preview open did it

**[23:08]** have the browser preview open did it

**[23:08]** have the browser preview open did it open fail?

**[23:09]** open fail?

**[23:09]** open fail? &gt;&gt; Cool. So this is um to point out two

**[23:12]** &gt;&gt; Cool. So this is um to point out two

**[23:12]** &gt;&gt; Cool. So this is um to point out two features. So one is in this flow at some

**[23:15]** features. So one is in this flow at some

**[23:15]** features. So one is in this flow at some point it basically started the task.

**[23:19]** point it basically started the task.

**[23:19]** point it basically started the task. It did npm rundef

**[23:22]** It did npm rundef

**[23:22]** It did npm rundef and then the next step it did it opens

**[23:24]** and then the next step it did it opens

**[23:24]** and then the next step it did it opens simple browser and simple browser is

**[23:26]** simple browser and simple browser is

**[23:26]** simple browser and simple browser is this VS code in browser preview we have

**[23:30]** this VS code in browser preview we have

**[23:30]** this VS code in browser preview we have and it will just um what we're injecting

**[23:33]** and it will just um what we're injecting

**[23:33]** and it will just um what we're injecting here what just went away is a little

**[23:36]** here what just went away is a little

**[23:36]** here what just went away is a little toggle you can now use to select

**[23:38]** toggle you can now use to select

**[23:38]** toggle you can now use to select specific elements that we then attach as

**[23:40]** specific elements that we then attach as

**[23:40]** specific elements that we then attach as a visual reference reference and as CSS

**[23:43]** a visual reference reference and as CSS

**[23:43]** a visual reference reference and as CSS into the current chat. So if I scroll

**[23:45]** into the current chat. So if I scroll

**[23:45]** into the current chat. So if I scroll back down here, I see what's being

**[23:48]** back down here, I see what's being

**[23:48]** back down here, I see what's being attached. Actually click it. So

**[23:50]** attached. Actually click it. So

**[23:50]** attached. Actually click it. So everything you see under message is in

**[23:52]** everything you see under message is in

**[23:52]** everything you see under message is in the context. The element screenshot

**[23:54]** the context. The element screenshot

**[23:54]** the context. The element screenshot somehow didn't didn't make it through.

**[23:57]** somehow didn't didn't make it through.

**[23:57]** somehow didn't didn't make it through. Uh but this one made it in. And that's

**[23:59]** Uh but this one made it in. And that's

**[23:59]** Uh but this one made it in. And that's basically the the CSS description and

### [24:00 - 25:00]

**[24:01]** basically the the CSS description and

**[24:01]** basically the the CSS description and HTML of the element we attached. So I

**[24:04]** HTML of the element we attached. So I

**[24:04]** HTML of the element we attached. So I didn't have to describe the element

**[24:06]** didn't have to describe the element

**[24:06]** didn't have to describe the element where it sits. It just did it for me.

**[24:10]** where it sits. It just did it for me.

**[24:10]** where it sits. It just did it for me. Okay.

**[24:13]** Okay.

**[24:13]** Okay. Ran into snacks. We don't care about

**[24:14]** Ran into snacks. We don't care about

**[24:14]** Ran into snacks. We don't care about that. Let's check the other one.

**[24:17]** that. Let's check the other one.

**[24:17]** that. Let's check the other one. Number two, fluent design. Uh, this is

**[24:20]** Number two, fluent design. Uh, this is

**[24:20]** Number two, fluent design. Uh, this is what it came up with. It's a little bit

**[24:23]** what it came up with. It's a little bit

**[24:23]** what it came up with. It's a little bit plain.

**[24:25]** plain.

**[24:25]** plain. Um, this is sad.

**[24:28]** Um, this is sad.

**[24:28]** Um, this is sad. Okay, at least it has a goal reach.

**[24:30]** Okay, at least it has a goal reach.

**[24:30]** Okay, at least it has a goal reach. That's nice. Um, and it has recent

**[24:32]** That's nice. Um, and it has recent

**[24:32]** That's nice. Um, and it has recent entries, too. It made similar

**[24:34]** entries, too. It made similar

**[24:34]** entries, too. It made similar assumptions on what we want. So feature-

**[24:37]** assumptions on what we want. So feature-

**[24:37]** assumptions on what we want. So feature- wise it somehow got to the same

**[24:38]** wise it somehow got to the same

**[24:38]** wise it somehow got to the same conclusion but design-wise

**[24:41]** conclusion but design-wise

**[24:41]** conclusion but design-wise uh this is definitely more corporate.

**[24:44]** uh this is definitely more corporate.

**[24:44]** uh this is definitely more corporate. Um yeah so that's the simplicity of VIP

**[24:47]** Um yeah so that's the simplicity of VIP

**[24:48]** Um yeah so that's the simplicity of VIP coding and

**[24:50]** coding and

**[24:50]** coding and using the new tool out of the box. Uh if

**[24:52]** using the new tool out of the box. Uh if

**[24:52]** using the new tool out of the box. Uh if you are an insiders and you can disable

**[24:54]** you are an insiders and you can disable

**[24:54]** you are an insiders and you can disable new tool it's easier to do like a single

**[24:56]** new tool it's easier to do like a single

**[24:56]** new tool it's easier to do like a single file HTML thing because new tool is

**[24:59]** file HTML thing because new tool is

**[24:59]** file HTML thing because new tool is definitely biased towards using npm and

### [25:00 - 26:00]

**[25:01]** definitely biased towards using npm and

**[25:01]** definitely biased towards using npm and installing packages. So it always ends

**[25:03]** installing packages. So it always ends

**[25:03]** installing packages. So it always ends up a little bit more um complex.

**[25:08]** up a little bit more um complex.

**[25:08]** up a little bit more um complex. &gt;&gt; Do you work with

**[25:11]** &gt;&gt; Do you work with

**[25:11]** &gt;&gt; Do you work with &gt;&gt; Yes. basically the team I work on. So I

**[25:14]** &gt;&gt; Yes. basically the team I work on. So I

**[25:14]** &gt;&gt; Yes. basically the team I work on. So I Hi, I'm Harold. I work on VS Code.

**[25:17]** Hi, I'm Harold. I work on VS Code.

**[25:17]** Hi, I'm Harold. I work on VS Code. &gt;&gt; Yeah.

**[25:18]** &gt;&gt; Yeah. &gt;&gt; Really cool to understand

**[25:24]** what are the new things that just like

**[25:24]** what are the new things that just like like a quick dip somehow. Someone could

**[25:26]** like a quick dip somehow. Someone could

**[25:26]** like a quick dip somehow. Someone could show me like I have them both on my

**[25:28]** show me like I have them both on my

**[25:28]** show me like I have them both on my machine,

**[25:28]** machine,

**[25:28]** machine, &gt;&gt; right? and I use them both but then I

**[25:31]** &gt;&gt; right? and I use them both but then I

**[25:31]** &gt;&gt; right? and I use them both but then I like fall behind a couple days back.

**[25:33]** like fall behind a couple days back.

**[25:33]** like fall behind a couple days back. What are the new things and why I should

**[25:34]** What are the new things and why I should

**[25:34]** What are the new things and why I should be using insight? What's

**[25:36]** be using insight? What's

**[25:36]** be using insight? What's &gt;&gt; Yes. So the the best way to stay on top

**[25:38]** &gt;&gt; Yes. So the the best way to stay on top

**[25:38]** &gt;&gt; Yes. So the the best way to stay on top of what's new is so we we do actually

**[25:41]** of what's new is so we we do actually

**[25:41]** of what's new is so we we do actually right now this week it's testing week

**[25:42]** right now this week it's testing week

**[25:42]** right now this week it's testing week and we're writing our release notes. So

**[25:44]** and we're writing our release notes. So

**[25:44]** and we're writing our release notes. So the release notes are usually capturing

**[25:45]** the release notes are usually capturing

**[25:46]** the release notes are usually capturing everything that's new. But for insiders

**[25:47]** everything that's new. But for insiders

**[25:47]** everything that's new. But for insiders it's hard because it's coming out every

**[25:49]** it's hard because it's coming out every

**[25:49]** it's hard because it's coming out every day. So it's hard to point.

**[25:53]** day. So it's hard to point.

**[25:53]** day. So it's hard to point. &gt;&gt; That's a great idea. We're going to make

**[25:54]** &gt;&gt; That's a great idea. We're going to make

**[25:54]** &gt;&gt; That's a great idea. We're going to make an MCP server that summarizes what

**[25:56]** an MCP server that summarizes what

**[25:56]** an MCP server that summarizes what landed. Yeah. Yes. I like that. Okay.

**[25:58]** landed. Yeah. Yes. I like that. Okay.

**[25:58]** landed. Yeah. Yes. I like that. Okay. Okay.

### [26:00 - 27:00]

**[26:00]** Okay. &gt;&gt; Let's let's do it for the next next

**[26:02]** &gt;&gt; Let's let's do it for the next next

**[26:02]** &gt;&gt; Let's let's do it for the next next demo.

**[26:04]** demo.

**[26:04]** demo. &gt;&gt; Next demo. Okay. So, what do we have in

**[26:06]** &gt;&gt; Next demo. Okay. So, what do we have in

**[26:06]** &gt;&gt; Next demo. Okay. So, what do we have in our YOLO vibing toolbox? We have the

**[26:08]** our YOLO vibing toolbox? We have the

**[26:08]** our YOLO vibing toolbox? We have the agent. Um, which sometimes is hard to

**[26:11]** agent. Um, which sometimes is hard to

**[26:11]** agent. Um, which sometimes is hard to find. Now, you're all on the agent. So,

**[26:12]** find. Now, you're all on the agent. So,

**[26:12]** find. Now, you're all on the agent. So, that's great. It's all about um actually

**[26:17]** that's great. It's all about um actually

**[26:17]** that's great. It's all about um actually didn't show that. I could have shown

**[26:19]** didn't show that. I could have shown

**[26:19]** didn't show that. I could have shown that is different panel styles. So, if I

**[26:22]** that is different panel styles. So, if I

**[26:22]** that is different panel styles. So, if I go back here um you can actually move

**[26:24]** go back here um you can actually move

**[26:24]** go back here um you can actually move this into the editor.

**[26:28]** this into the editor.

**[26:28]** this into the editor. which is nice. So, some people like that

**[26:31]** which is nice. So, some people like that

**[26:31]** which is nice. So, some people like that more space for your chat. Um, you can

**[26:34]** more space for your chat. Um, you can

**[26:34]** more space for your chat. Um, you can also,

**[26:37]** also,

**[26:37]** also, if I go back into my panel,

**[26:39]** if I go back into my panel,

**[26:39]** if I go back into my panel, &gt;&gt; oh, I moved in into a drop down here and

**[26:42]** &gt;&gt; oh, I moved in into a drop down here and

**[26:42]** &gt;&gt; oh, I moved in into a drop down here and you can move your chats into here. So,

**[26:44]** you can move your chats into here. So,

**[26:44]** you can move your chats into here. So, you can have multiple chats and they

**[26:46]** you can have multiple chats and they

**[26:46]** you can have multiple chats and they actually have names. So, it's easy to go

**[26:48]** actually have names. So, it's easy to go

**[26:48]** actually have names. So, it's easy to go back and forth. You can put them in

**[26:49]** back and forth. You can put them in

**[26:49]** back and forth. You can put them in parallel to your codes. You can use all

**[26:51]** parallel to your codes. You can use all

**[26:51]** parallel to your codes. You can use all the like window management things.

**[26:54]** the like window management things.

**[26:54]** the like window management things. &gt;&gt; Yes. Wait, how did you know? Um,

**[26:59]** &gt;&gt; Yes. Wait, how did you know? Um,

**[26:59]** &gt;&gt; Yes. Wait, how did you know? Um, okay. Where do we go? In new window.

### [27:00 - 28:00]

**[27:01]** okay. Where do we go? In new window.

**[27:01]** okay. Where do we go? In new window. &gt;&gt; There you go. Now you have a chat in its

**[27:05]** &gt;&gt; There you go. Now you have a chat in its

**[27:05]** &gt;&gt; There you go. Now you have a chat in its own window. You can put it on your own

**[27:07]** own window. You can put it on your own

**[27:07]** own window. You can put it on your own monitor. So, feature request succ. And

**[27:09]** monitor. So, feature request succ. And

**[27:09]** monitor. So, feature request succ. And you can actually pin it on to be top.

**[27:11]** you can actually pin it on to be top.

**[27:11]** you can actually pin it on to be top. So, now if I run this and I can close

**[27:15]** So, now if I run this and I can close

**[27:15]** So, now if I run this and I can close this

**[27:17]** this

**[27:17]** this uh

**[27:18]** uh

**[27:18]** uh let's move that away first. So, I can

**[27:20]** let's move that away first. So, I can

**[27:20]** let's move that away first. So, I can accept this. This we all going to keep

**[27:23]** accept this. This we all going to keep

**[27:23]** accept this. This we all going to keep and close it.

**[27:25]** and close it.

**[27:25]** and close it. and then close the other one. And now we

**[27:28]** and then close the other one. And now we

**[27:28]** and then close the other one. And now we have the output and we can just move our

**[27:30]** have the output and we can just move our

**[27:30]** have the output and we can just move our chat across and fully focus on the

**[27:33]** chat across and fully focus on the

**[27:33]** chat across and fully focus on the exponentials

**[27:35]** exponentials

**[27:35]** exponentials that are happening in this window. Yeah.

**[27:38]** that are happening in this window. Yeah.

**[27:38]** that are happening in this window. Yeah. So that's one way you can really manage

**[27:41]** So that's one way you can really manage

**[27:41]** So that's one way you can really manage the space how you want it. Uh new

**[27:44]** the space how you want it. Uh new

**[27:44]** the space how you want it. Uh new workspace flow we showed. So it's really

**[27:46]** workspace flow we showed. So it's really

**[27:46]** workspace flow we showed. So it's really this optimized

**[27:48]** this optimized

**[27:48]** this optimized CLI first question.

**[27:51]** CLI first question.

**[27:51]** CLI first question. &gt;&gt; Okay. Okay. Yeah. And then voice

**[27:53]** &gt;&gt; Okay. Okay. Yeah. And then voice

**[27:53]** &gt;&gt; Okay. Okay. Yeah. And then voice dictation I haven't shown. Uh who has

**[27:54]** dictation I haven't shown. Uh who has

**[27:54]** dictation I haven't shown. Uh who has tried voice dictation in GitHub copilot

**[27:56]** tried voice dictation in GitHub copilot

**[27:56]** tried voice dictation in GitHub copilot already? Okay, magic moment of

### [28:00 - 29:00]

**[28:01]** already? Okay, magic moment of

**[28:01]** already? Okay, magic moment of um

**[28:04]** um

**[28:04]** um add a dark mode please and maybe

**[28:09]** add a dark mode please and maybe

**[28:09]** add a dark mode please and maybe give it a cool name that works with a

**[28:13]** give it a cool name that works with a

**[28:13]** give it a cool name that works with a younger audience who needs to drink more

**[28:15]** younger audience who needs to drink more

**[28:16]** younger audience who needs to drink more or maybe my kids. Make it for kids so a

**[28:19]** or maybe my kids. Make it for kids so a

**[28:19]** or maybe my kids. Make it for kids so a little more kids friendly. Thank you.

**[28:21]** little more kids friendly. Thank you.

**[28:22]** little more kids friendly. Thank you. Bye.

**[28:29]** Okay. So, u command I is actually the

**[28:29]** Okay. So, u command I is actually the default shortcut. Um it's it's a local

**[28:31]** default shortcut. Um it's it's a local

**[28:31]** default shortcut. Um it's it's a local model which is great for privacy and

**[28:34]** model which is great for privacy and

**[28:34]** model which is great for privacy and it's really fast. Uh it's accurate and

**[28:38]** it's really fast. Uh it's accurate and

**[28:38]** it's really fast. Uh it's accurate and there's an option as well if you when

**[28:40]** there's an option as well if you when

**[28:40]** there's an option as well if you when you use command uh voice input that it

**[28:42]** you use command uh voice input that it

**[28:42]** you use command uh voice input that it also reads back the text which is great

**[28:44]** also reads back the text which is great

**[28:44]** also reads back the text which is great for accessibility.

**[28:46]** for accessibility.

**[28:46]** for accessibility. And yeah, by using just your voice, you

**[28:49]** And yeah, by using just your voice, you

**[28:49]** And yeah, by using just your voice, you can now finally don't put that coffee

**[28:51]** can now finally don't put that coffee

**[28:51]** can now finally don't put that coffee down and just keep keep vibing. Uh

**[28:53]** down and just keep keep vibing. Uh

**[28:53]** down and just keep keep vibing. Uh there's a hey co-pilot as well I think

**[28:55]** there's a hey co-pilot as well I think

**[28:55]** there's a hey co-pilot as well I think we did at some point which I haven't

**[28:57]** we did at some point which I haven't

**[28:57]** we did at some point which I haven't used in a while.

### [29:00 - 30:00]

**[29:03]** Okay. Uh

**[29:03]** Okay. Uh I said all that keyboard shortcuts.

**[29:05]** I said all that keyboard shortcuts.

**[29:05]** I said all that keyboard shortcuts. There's a keyboard shortcut if you want

**[29:06]** There's a keyboard shortcut if you want

**[29:06]** There's a keyboard shortcut if you want to customize it to actually hold down

**[29:07]** to customize it to actually hold down

**[29:07]** to customize it to actually hold down while you talk and then let go. Uh

**[29:10]** while you talk and then let go. Uh

**[29:10]** while you talk and then let go. Uh visual context I showed attaching. It's

**[29:12]** visual context I showed attaching. It's

**[29:12]** visual context I showed attaching. It's great for wireframes. the in preview

**[29:14]** great for wireframes. the in preview

**[29:14]** great for wireframes. the in preview gets hot reload. It just works and you

**[29:17]** gets hot reload. It just works and you

**[29:17]** gets hot reload. It just works and you can attach the elements using that

**[29:19]** can attach the elements using that

**[29:19]** can attach the elements using that little send button.

**[29:21]** little send button.

**[29:21]** little send button. And then auto accept. I showed the auto

**[29:23]** And then auto accept. I showed the auto

**[29:23]** And then auto accept. I showed the auto approve tool. There's also an auto tool

**[29:26]** approve tool. There's also an auto tool

**[29:26]** approve tool. There's also an auto tool auto approve tool setting. Uh there's

**[29:30]** auto approve tool setting. Uh there's

**[29:30]** auto approve tool setting. Uh there's also an auto accept after delay. If you

**[29:31]** also an auto accept after delay. If you

**[29:32]** also an auto accept after delay. If you don't have that on, I love autosave.

**[29:34]** don't have that on, I love autosave.

**[29:34]** don't have that on, I love autosave. It's a great VS code feature that's

**[29:35]** It's a great VS code feature that's

**[29:35]** It's a great VS code feature that's already working. Um basically after

**[29:37]** already working. Um basically after

**[29:37]** already working. Um basically after delay or after focus change, it will

**[29:39]** delay or after focus change, it will

**[29:39]** delay or after focus change, it will just save it for you. And what I haven't

**[29:42]** just save it for you. And what I haven't

**[29:42]** just save it for you. And what I haven't showed, let's see if this this works.

**[29:44]** showed, let's see if this this works.

**[29:44]** showed, let's see if this this works. Here is the undo button.

**[29:48]** Here is the undo button.

**[29:48]** Here is the undo button. This is still going. What is this doing?

**[29:50]** This is still going. What is this doing?

**[29:50]** This is still going. What is this doing? I forgot. Um Oh, this is adding the

**[29:53]** I forgot. Um Oh, this is adding the

**[29:53]** I forgot. Um Oh, this is adding the particles. Cool. It still worked on it.

**[29:56]** particles. Cool. It still worked on it.

**[29:56]** particles. Cool. It still worked on it. Got to compile it.

### [30:00 - 31:00]

**[30:02]** Okay. Got stunning animations. That's

**[30:02]** Okay. Got stunning animations. That's great. That's what I wanted.

**[30:04]** great. That's what I wanted.

**[30:04]** great. That's what I wanted. Is it doing it now? So, let's keep

**[30:09]** Is it doing it now? So, let's keep

**[30:09]** Is it doing it now? So, let's keep it does animate. Nice particle. Nice.

**[30:13]** it does animate. Nice particle. Nice.

**[30:13]** it does animate. Nice particle. Nice. Look at bubbles. Okay. Um I don't like

**[30:17]** Look at bubbles. Okay. Um I don't like

**[30:17]** Look at bubbles. Okay. Um I don't like it. Undo up here. Uh those are basically

**[30:20]** it. Undo up here. Uh those are basically

**[30:20]** it. Undo up here. Uh those are basically our our checkpoints. Uh there's a new

**[30:22]** our our checkpoints. Uh there's a new

**[30:22]** our our checkpoints. Uh there's a new checkpoint UX coming. But because I have

**[30:25]** checkpoint UX coming. But because I have

**[30:25]** checkpoint UX coming. But because I have many people saying tell me, "Oh, you

**[30:26]** many people saying tell me, "Oh, you

**[30:26]** many people saying tell me, "Oh, you don't have checkpoints. I can't undo

**[30:28]** don't have checkpoints. I can't undo

**[30:28]** don't have checkpoints. I can't undo stuff." But if you already accepted

**[30:30]** stuff." But if you already accepted

**[30:30]** stuff." But if you already accepted stuff or if you want to go back to

**[30:32]** stuff or if you want to go back to

**[30:32]** stuff or if you want to go back to something like this is like these

**[30:34]** something like this is like these

**[30:34]** something like this is like these particles but for for V0ero. Oh, that's

**[30:37]** particles but for for V0ero. Oh, that's

**[30:37]** particles but for for V0ero. Oh, that's beautiful. I love it. Uh we don't need

**[30:39]** beautiful. I love it. Uh we don't need

**[30:39]** beautiful. I love it. Uh we don't need that. Then you can also bring that back.

**[30:41]** that. Then you can also bring that back.

**[30:41]** that. Then you can also bring that back. I just need to see that again. That was

**[30:43]** I just need to see that again. That was

**[30:43]** I just need to see that again. That was really nice.

**[30:45]** really nice.

**[30:46]** really nice. Okay. So

**[30:48]** Okay. So

**[30:48]** Okay. So for people who don't like particles, we

**[30:49]** for people who don't like particles, we

**[30:49]** for people who don't like particles, we can now undo and it's now back to the

**[30:52]** can now undo and it's now back to the

**[30:52]** can now undo and it's now back to the original version. So it it has stages

**[30:54]** original version. So it it has stages

**[30:54]** original version. So it it has stages for each of the of the work it did. You

**[30:56]** for each of the of the work it did. You

**[30:56]** for each of the of the work it did. You can easily go back and forth to see the

**[30:58]** can easily go back and forth to see the

**[30:58]** can easily go back and forth to see the before and after as well.

### [31:00 - 32:00]

**[31:01]** before and after as well.

**[31:01]** before and after as well. Yeah, but in VIP code, you don't want to

**[31:03]** Yeah, but in VIP code, you don't want to

**[31:03]** Yeah, but in VIP code, you don't want to look at the code because we don't look

**[31:05]** look at the code because we don't look

**[31:05]** look at the code because we don't look at the output.

**[31:08]** at the output.

**[31:08]** at the output. Okay. Um, that's the YOLO toolbox.

**[31:12]** Okay. Um, that's the YOLO toolbox.

**[31:12]** Okay. Um, that's the YOLO toolbox. And I think as I mentioned before, you

**[31:14]** And I think as I mentioned before, you

**[31:14]** And I think as I mentioned before, you want to try it out just to get an idea

**[31:15]** want to try it out just to get an idea

**[31:15]** want to try it out just to get an idea of the AI. Like in my case, I mentioned

**[31:17]** of the AI. Like in my case, I mentioned

**[31:17]** of the AI. Like in my case, I mentioned I like getting a sense of how good AI is

**[31:19]** I like getting a sense of how good AI is

**[31:19]** I like getting a sense of how good AI is at design. like can I just give it wide

**[31:22]** at design. like can I just give it wide

**[31:22]** at design. like can I just give it wide task to explore a space and it will like

**[31:24]** task to explore a space and it will like

**[31:24]** task to explore a space and it will like come up with something interesting or do

**[31:25]** come up with something interesting or do

**[31:25]** come up with something interesting or do you need to how detailed do I need to be

**[31:28]** you need to how detailed do I need to be

**[31:28]** you need to how detailed do I need to be when does it make mistakes if I give it

**[31:30]** when does it make mistakes if I give it

**[31:30]** when does it make mistakes if I give it a general task maybe about Java where

**[31:32]** a general task maybe about Java where

**[31:32]** a general task maybe about Java where it's not as good at like what will it do

**[31:35]** it's not as good at like what will it do

**[31:36]** it's not as good at like what will it do um next one is known frameworks we went

**[31:38]** um next one is known frameworks we went

**[31:38]** um next one is known frameworks we went with V material design things that are

**[31:40]** with V material design things that are

**[31:40]** with V material design things that are kind of off the shelf and haven't

**[31:42]** kind of off the shelf and haven't

**[31:42]** kind of off the shelf and haven't changed in a long time uh in a large

**[31:45]** changed in a long time uh in a large

**[31:45]** changed in a long time uh in a large scale so you want to use something

**[31:47]** scale so you want to use something

**[31:48]** scale so you want to use something that's popular and have has been

**[31:49]** that's popular and have has been

**[31:49]** that's popular and have has been consistent

**[31:50]** consistent

**[31:50]** consistent And lastly, we use it as a whiteboard.

**[31:53]** And lastly, we use it as a whiteboard.

**[31:53]** And lastly, we use it as a whiteboard. Um, we showed there just attaching a

**[31:55]** Um, we showed there just attaching a

**[31:55]** Um, we showed there just attaching a visual element, change this, add some

**[31:56]** visual element, change this, add some

**[31:56]** visual element, change this, add some particles. Um, it's really about not

**[31:59]** particles. Um, it's really about not

### [32:00 - 33:00]

**[32:00]** particles. Um, it's really about not being becoming too attached with

**[32:01]** being becoming too attached with

**[32:01]** being becoming too attached with whatever you're working on, but being

**[32:03]** whatever you're working on, but being

**[32:03]** whatever you're working on, but being um, able and willing to throw it out and

**[32:06]** um, able and willing to throw it out and

**[32:06]** um, able and willing to throw it out and start from scratch if things go wrong.

**[32:15]** Structured VIP coding is this middle

**[32:15]** Structured VIP coding is this middle stage. tries to balance the yolo, the

**[32:18]** stage. tries to balance the yolo, the

**[32:18]** stage. tries to balance the yolo, the fun and chaos with a more structured

**[32:19]** fun and chaos with a more structured

**[32:20]** fun and chaos with a more structured approach. And there it's um I think it's

**[32:24]** approach. And there it's um I think it's

**[32:24]** approach. And there it's um I think it's the biggest impact I see from talking to

**[32:27]** the biggest impact I see from talking to

**[32:27]** the biggest impact I see from talking to customers on like this is this is how

**[32:29]** customers on like this is this is how

**[32:29]** customers on like this is this is how VIP coding can work for us. This is

**[32:31]** VIP coding can work for us. This is

**[32:31]** VIP coding can work for us. This is where we can bring somebody

**[32:32]** where we can bring somebody

**[32:32]** where we can bring somebody non-technical in. give them a good

**[32:35]** non-technical in. give them a good

**[32:35]** non-technical in. give them a good starter template that has a consistent

**[32:37]** starter template that has a consistent

**[32:37]** starter template that has a consistent text stack that comes with clear

**[32:40]** text stack that comes with clear

**[32:40]** text stack that comes with clear instructions for the LM and how to work

**[32:42]** instructions for the LM and how to work

**[32:42]** instructions for the LM and how to work on it and keeps it in its actual

**[32:45]** on it and keeps it in its actual

**[32:45]** on it and keeps it in its actual guardrails

**[32:46]** guardrails

**[32:46]** guardrails and already brings in some custom tools

**[32:49]** and already brings in some custom tools

**[32:49]** and already brings in some custom tools that bring in expert domain knowledge or

**[32:51]** that bring in expert domain knowledge or

**[32:51]** that bring in expert domain knowledge or internal knowledge that you would need

**[32:53]** internal knowledge that you would need

**[32:53]** internal knowledge that you would need to work on this codebase

**[32:56]** to work on this codebase

**[32:56]** to work on this codebase and that's really kind of yolo on on

**[32:58]** and that's really kind of yolo on on

**[32:58]** and that's really kind of yolo on on guardrails. uh it's faster and gives you

### [33:00 - 34:00]

**[33:01]** guardrails. uh it's faster and gives you

**[33:01]** guardrails. uh it's faster and gives you more consistent results. So you don't

**[33:03]** more consistent results. So you don't

**[33:03]** more consistent results. So you don't end up with something, oh it used

**[33:04]** end up with something, oh it used

**[33:04]** end up with something, oh it used material design but it should have used

**[33:06]** material design but it should have used

**[33:06]** material design but it should have used fluent or it used should have added dark

**[33:08]** fluent or it used should have added dark

**[33:08]** fluent or it used should have added dark mode and should have been responsive.

**[33:10]** mode and should have been responsive.

**[33:10]** mode and should have been responsive. All of that can already be baked into

**[33:12]** All of that can already be baked into

**[33:12]** All of that can already be baked into the instructions.

**[33:14]** the instructions.

**[33:14]** the instructions. So I see a lot of companies bring that

**[33:16]** So I see a lot of companies bring that

**[33:16]** So I see a lot of companies bring that into their bootstrapping for green field

**[33:18]** into their bootstrapping for green field

**[33:18]** into their bootstrapping for green field projects. So we have something and you

**[33:20]** projects. So we have something and you

**[33:20]** projects. So we have something and you can often times it's you go into a

**[33:22]** can often times it's you go into a

**[33:22]** can often times it's you go into a meeting and you have a product that

**[33:24]** meeting and you have a product that

**[33:24]** meeting and you have a product that looks already finished because you

**[33:25]** looks already finished because you

**[33:25]** looks already finished because you vipcoded it with your go-to stack. It

**[33:28]** vipcoded it with your go-to stack. It

**[33:28]** vipcoded it with your go-to stack. It uses your internal design system. So it

**[33:30]** uses your internal design system. So it

**[33:30]** uses your internal design system. So it already looks way more polished.

**[33:34]** already looks way more polished.

**[33:34]** already looks way more polished. And the last piece I think out of

**[33:36]** And the last piece I think out of

**[33:36]** And the last piece I think out of mainstream workloads is where YOLO by

**[33:39]** mainstream workloads is where YOLO by

**[33:39]** mainstream workloads is where YOLO by default will always bias towards

**[33:41]** default will always bias towards

**[33:41]** default will always bias towards whatever is like top of the training

**[33:43]** whatever is like top of the training

**[33:43]** whatever is like top of the training stack. With this one, you can then

**[33:45]** stack. With this one, you can then

**[33:45]** stack. With this one, you can then customize it further down to internal

**[33:47]** customize it further down to internal

**[33:47]** customize it further down to internal stacks, internal workloads, internal

**[33:49]** stacks, internal workloads, internal

**[33:49]** stacks, internal workloads, internal deployment infrastructure that makes it

**[33:52]** deployment infrastructure that makes it

**[33:52]** deployment infrastructure that makes it work better.

**[33:54]** work better.

**[33:54]** work better. So let's do structured VIP coding. This

**[33:56]** So let's do structured VIP coding. This

**[33:56]** So let's do structured VIP coding. This is now the image as I explained is now

**[33:59]** is now the image as I explained is now

**[33:59]** is now the image as I explained is now has wireframes and uh more charts. So

### [34:00 - 35:00]

**[34:03]** has wireframes and uh more charts. So

**[34:03]** has wireframes and uh more charts. So that's what makes it more structured.

**[34:13]** So what I'm going to do now I think I'm

**[34:13]** So what I'm going to do now I think I'm going to push this.

**[34:16]** going to push this.

**[34:16]** going to push this. It's still running.

**[34:25]** Let's see if this runs. I did

**[34:25]** Let's see if this runs. I did create this vibe coding. I do have

**[34:27]** create this vibe coding. I do have

**[34:27]** create this vibe coding. I do have another one that I can share. Just look

**[34:30]** another one that I can share. Just look

**[34:30]** another one that I can share. Just look at this one. And I'm going to push it to

**[34:33]** at this one. And I'm going to push it to

**[34:33]** at this one. And I'm going to push it to GitHub.

**[34:40]** It's gone through fine. Um, cool. Front

**[34:40]** It's gone through fine. Um, cool. Front end vibes. Perfect. Um,

**[34:44]** end vibes. Perfect. Um,

**[34:44]** end vibes. Perfect. Um, this is all vibes. So, we're going to

**[34:45]** this is all vibes. So, we're going to

**[34:45]** this is all vibes. So, we're going to make this live. Um, this is commit

**[34:49]** make this live. Um, this is commit

**[34:49]** make this live. Um, this is commit and then

**[34:51]** and then

**[34:51]** and then Yeah. Oh, yeah. commit misses one who

**[34:53]** Yeah. Oh, yeah. commit misses one who

**[34:53]** Yeah. Oh, yeah. commit misses one who has been using this commit button here.

**[34:57]** has been using this commit button here.

**[34:57]** has been using this commit button here. So cop will write your commit message

### [35:00 - 36:00]

**[35:01]** So cop will write your commit message

**[35:02]** So cop will write your commit message then this looks good and now sync

**[35:04]** then this looks good and now sync

**[35:04]** then this looks good and now sync changes and I'll share the repository

**[35:14]** this repository might still be an old

**[35:14]** this repository might still be an old name. Let me see.

**[35:23]** Yeah, probably. Let me just check where

**[35:23]** Yeah, probably. Let me just check where it sits because I forgot where it sits.

**[35:34]** Oh, it's perfect. Sleep wipes.

**[35:34]** Oh, it's perfect. Sleep wipes. This is one of my VIP exercises. Okay.

**[35:50]** &gt;&gt; which the

**[35:50]** &gt;&gt; which the &gt;&gt; just open.

**[35:51]** &gt;&gt; just open.

**[35:51]** &gt;&gt; just open. &gt;&gt; Oh yes. Yes. Um yes the simple browser

**[35:55]** &gt;&gt; Oh yes. Yes. Um yes the simple browser

**[35:55]** &gt;&gt; Oh yes. Yes. Um yes the simple browser simp. So we go into

**[35:58]** simp. So we go into

**[35:58]** simp. So we go into simple browser show. That's it.

### [36:00 - 37:00]

**[36:02]** simple browser show. That's it.

**[36:02]** simple browser show. That's it. Sleep wipes.

**[36:11]** Okay. And then npm install on it. And

**[36:11]** Okay. And then npm install on it. And then yeah,

**[36:17]** it would have prepared better. It would

**[36:17]** it would have prepared better. It would have been a code space and a dev

**[36:18]** have been a code space and a dev

**[36:18]** have been a code space and a dev container and you just click open in

**[36:20]** container and you just click open in

**[36:20]** container and you just click open in code spaces and things work. Um, come to

**[36:23]** code spaces and things work. Um, come to

**[36:23]** code spaces and things work. Um, come to my next show and then we'll get that

**[36:25]** my next show and then we'll get that

**[36:25]** my next show and then we'll get that fixed.

**[36:28]** fixed.

**[36:28]** fixed. Yeah,

**[36:35]** let me just open the code space to see.

**[36:35]** let me just open the code space to see. Now I'm curious if it just works.

**[36:41]** Anybody's been using code spaces on

**[36:41]** Anybody's been using code spaces on GitHub?

**[36:43]** GitHub?

**[36:43]** GitHub? Not many. Okay. Occasionally

**[36:49]** &gt;&gt; the complexity lies in all the different

**[36:50]** &gt;&gt; the complexity lies in all the different versions of

**[36:52]** versions of

**[36:52]** versions of regular version all the work. out of

**[36:56]** regular version all the work. out of

**[36:56]** regular version all the work. out of bugette. Yeah. Yeah.

**[36:59]** bugette. Yeah. Yeah.

**[36:59]** bugette. Yeah. Yeah. &gt;&gt; Everything just work.

### [37:00 - 38:00]

**[37:02]** &gt;&gt; Everything just work.

**[37:02]** &gt;&gt; Everything just work. &gt;&gt; Yes, it mostly does, right? But mostly,

**[37:04]** &gt;&gt; Yes, it mostly does, right? But mostly,

**[37:04]** &gt;&gt; Yes, it mostly does, right? But mostly, right?

**[37:04]** right?

**[37:04]** right? &gt;&gt; Yeah.

**[37:04]** &gt;&gt; Yeah. &gt;&gt; It's 95% there.

**[37:06]** &gt;&gt; It's 95% there.

**[37:06]** &gt;&gt; It's 95% there. &gt;&gt; Yeah.

**[37:07]** &gt;&gt; Yeah. &gt;&gt; But it's the 5%. When something doesn't

**[37:09]** &gt;&gt; But it's the 5%. When something doesn't

**[37:09]** &gt;&gt; But it's the 5%. When something doesn't work, you just go back.

**[37:10]** work, you just go back.

**[37:10]** work, you just go back. &gt;&gt; Yeah.

**[37:21]** &gt;&gt; You could try. I haven't I'm actually

**[37:21]** &gt;&gt; You could try. I haven't I'm actually not running it in container but if you

**[37:23]** not running it in container but if you

**[37:23]** not running it in container but if you wanna

**[37:24]** wanna

**[37:24]** wanna &gt;&gt; the container is just a NodeJS one and

**[37:28]** &gt;&gt; the container is just a NodeJS one and

**[37:28]** &gt;&gt; the container is just a NodeJS one and it should work too. I did add a

**[37:30]** it should work too. I did add a

**[37:30]** it should work too. I did add a container. See

**[37:32]** container. See

**[37:32]** container. See &gt;&gt; I vip coded my container too.

**[37:39]** Wait I can now check. So if you ever

**[37:39]** Wait I can now check. So if you ever wonder what you did on a project um

**[37:43]** wonder what you did on a project um

**[37:43]** wonder what you did on a project um so this is where I created my container.

**[37:45]** so this is where I created my container.

**[37:45]** so this is where I created my container. This is where I just asked uh GitHub

**[37:48]** This is where I just asked uh GitHub

**[37:48]** This is where I just asked uh GitHub copilot to update my dev container. just

**[37:50]** copilot to update my dev container. just

**[37:50]** copilot to update my dev container. just look at my codebase and update my dev

**[37:52]** look at my codebase and update my dev

**[37:52]** look at my codebase and update my dev container. So I did a good job here.

**[37:54]** container. So I did a good job here.

**[37:54]** container. So I did a good job here. Should have maybe

**[37:57]** Should have maybe

**[37:57]** Should have maybe remembered that I did that as well.

### [38:00 - 39:00]

**[38:05]** Okay, if if ready meanwhile why you

**[38:05]** Okay, if if ready meanwhile why you clone while you npm install anybody got

**[38:08]** clone while you npm install anybody got

**[38:08]** clone while you npm install anybody got it working already

**[38:10]** it working already

**[38:10]** it working already still. Okay, cool. I'll give the tour of

**[38:14]** still. Okay, cool. I'll give the tour of

**[38:14]** still. Okay, cool. I'll give the tour of what we have. So one is we again start

**[38:17]** what we have. So one is we again start

**[38:17]** what we have. So one is we again start with good copilot instructions and they

**[38:21]** with good copilot instructions and they

**[38:21]** with good copilot instructions and they live in github/copilad-instructions.mmd.

**[38:28]** It's a markdown file that's included

**[38:28]** It's a markdown file that's included with all your agent requests, all your

**[38:30]** with all your agent requests, all your

**[38:30]** with all your agent requests, all your chat requests, all your inline chat

**[38:32]** chat requests, all your inline chat

**[38:32]** chat requests, all your inline chat requests. It just copilot basically

**[38:35]** requests. It just copilot basically

**[38:35]** requests. It just copilot basically gives a grounding foundation knowledge

**[38:38]** gives a grounding foundation knowledge

**[38:38]** gives a grounding foundation knowledge about your codebase. And sometimes they

**[38:41]** about your codebase. And sometimes they

**[38:41]** about your codebase. And sometimes they feel a bit repetitive like um depending

**[38:46]** feel a bit repetitive like um depending

**[38:46]** feel a bit repetitive like um depending I saw some demos of like use basically

**[38:48]** I saw some demos of like use basically

**[38:48]** I saw some demos of like use basically it repeats linting rules that you expect

**[38:50]** it repeats linting rules that you expect

**[38:50]** it repeats linting rules that you expect the AI to just follow anyways. But I I

**[38:53]** the AI to just follow anyways. But I I

**[38:53]** the AI to just follow anyways. But I I like um my go-to is just a oneliner on

**[38:57]** like um my go-to is just a oneliner on

**[38:57]** like um my go-to is just a oneliner on what what's your stack. That's that's a

**[38:59]** what what's your stack. That's that's a

**[38:59]** what what's your stack. That's that's a good starting point. Just point it to

### [39:00 - 40:00]

**[39:01]** good starting point. Just point it to

**[39:01]** good starting point. Just point it to what frameworks, what version. And

**[39:06]** what frameworks, what version. And

**[39:06]** what frameworks, what version. And that's one way to just keep it on rails

**[39:08]** that's one way to just keep it on rails

**[39:08]** that's one way to just keep it on rails with what what it uses.

**[39:10]** with what what it uses.

**[39:10]** with what what it uses. &gt;&gt; Question.

**[39:11]** &gt;&gt; Question.

**[39:11]** &gt;&gt; Question. &gt;&gt; I was experimenting with this figuring

**[39:13]** &gt;&gt; I was experimenting with this figuring

**[39:13]** &gt;&gt; I was experimenting with this figuring out what would be the best way to have

**[39:15]** out what would be the best way to have

**[39:15]** out what would be the best way to have that be a standard that gets included in

**[39:19]** that be a standard that gets included in

**[39:19]** that be a standard that gets included in but like let people not not mess with

**[39:22]** but like let people not not mess with

**[39:22]** but like let people not not mess with that like give people some coding

**[39:24]** that like give people some coding

**[39:24]** that like give people some coding structure.

**[39:24]** structure.

**[39:24]** structure. &gt;&gt; Yeah,

**[39:25]** &gt;&gt; Yeah,

**[39:25]** &gt;&gt; Yeah, &gt;&gt; if you have a whole team of

**[39:28]** &gt;&gt; if you have a whole team of

**[39:28]** &gt;&gt; if you have a whole team of probably don't want to touch it.

**[39:30]** probably don't want to touch it.

**[39:30]** probably don't want to touch it. &gt;&gt; So this is in your repo. So I think it's

**[39:33]** &gt;&gt; So this is in your repo. So I think it's

**[39:33]** &gt;&gt; So this is in your repo. So I think it's a good team exercise to iterate on it

**[39:35]** a good team exercise to iterate on it

**[39:36]** a good team exercise to iterate on it like it shouldn't be a stale document.

**[39:38]** like it shouldn't be a stale document.

**[39:38]** like it shouldn't be a stale document. You can put this in your user settings

**[39:41]** You can put this in your user settings

**[39:41]** You can put this in your user settings as well.

**[39:42]** as well.

**[39:42]** as well. &gt;&gt; You probably don't want it with each

**[39:43]** &gt;&gt; You probably don't want it with each

**[39:43]** &gt;&gt; You probably don't want it with each app. You probably want to right

**[39:45]** app. You probably want to right

**[39:46]** app. You probably want to right &gt;&gt; you could do it set up a way that you

**[39:47]** &gt;&gt; you could do it set up a way that you

**[39:48]** &gt;&gt; you could do it set up a way that you code and then each app.

**[39:54]** &gt;&gt; So I've been trying to convince on my

**[39:54]** &gt;&gt; So I've been trying to convince on my peers on a GitHub site this should be an

**[39:56]** peers on a GitHub site this should be an

**[39:56]** peers on a GitHub site this should be an organizational setting that people can

**[39:57]** organizational setting that people can

**[39:58]** organizational setting that people can set easier on like a organizational

### [40:00 - 41:00]

**[40:00]** set easier on like a organizational

**[40:00]** set easier on like a organizational level and like something as a as a team

**[40:03]** level and like something as a as a team

**[40:03]** level and like something as a as a team you can select which ones you want to

**[40:05]** you can select which ones you want to

**[40:05]** you can select which ones you want to use. So working on that discovery

**[40:08]** use. So working on that discovery

**[40:08]** use. So working on that discovery sharing is there always one file or can

**[40:10]** sharing is there always one file or can

**[40:10]** sharing is there always one file or can you opt in for like you have different

**[40:12]** you opt in for like you have different

**[40:12]** you opt in for like you have different languages different things you're

**[40:14]** languages different things you're

**[40:14]** languages different things you're building.

**[40:14]** building.

**[40:14]** building. &gt;&gt; Good question.

**[40:16]** &gt;&gt; Good question.

**[40:16]** &gt;&gt; Good question. &gt;&gt; Yeah. So we have this one now. This

**[40:18]** &gt;&gt; Yeah. So we have this one now. This

**[40:18]** &gt;&gt; Yeah. So we have this one now. This these are new instructions. So they

**[40:21]** these are new instructions. So they

**[40:21]** these are new instructions. So they these are these become rather monolith

**[40:23]** these are these become rather monolith

**[40:23]** these are these become rather monolith and large and unwieldy.

**[40:27]** and large and unwieldy.

**[40:27]** and large and unwieldy. And now uh just point out here before I

**[40:30]** And now uh just point out here before I

**[40:30]** And now uh just point out here before I go to new ones I do also guide which

**[40:32]** go to new ones I do also guide which

**[40:32]** go to new ones I do also guide which tools to use. I do have my first MCPS in

**[40:35]** tools to use. I do have my first MCPS in

**[40:35]** tools to use. I do have my first MCPS in here and I already tell it for front-end

**[40:38]** here and I already tell it for front-end

**[40:38]** here and I already tell it for front-end Q&amp;A and review use the browser tools

**[40:39]** Q&amp;A and review use the browser tools

**[40:39]** Q&amp;A and review use the browser tools that come from playright research. I use

**[40:42]** that come from playright research. I use

**[40:42]** that come from playright research. I use perplexity. I have uh context 7 in here

**[40:45]** perplexity. I have uh context 7 in here

**[40:45]** perplexity. I have uh context 7 in here which has library docs and it keeps

**[40:47]** which has library docs and it keeps

**[40:47]** which has library docs and it keeps using this ID tool to look up IDs but I

**[40:50]** using this ID tool to look up IDs but I

**[40:50]** using this ID tool to look up IDs but I just gave it these are the IDs you

**[40:52]** just gave it these are the IDs you

**[40:52]** just gave it these are the IDs you should use. Don't don't use the other

**[40:53]** should use. Don't don't use the other

**[40:53]** should use. Don't don't use the other tool. So there's ways you can already

**[40:55]** tool. So there's ways you can already

**[40:56]** tool. So there's ways you can already guide it to specific tools you want it

**[40:58]** guide it to specific tools you want it

**[40:58]** guide it to specific tools you want it to apply when needed.

### [41:00 - 42:00]

**[41:01]** to apply when needed.

**[41:01]** to apply when needed. Um the rest is just syntax formatting

**[41:02]** Um the rest is just syntax formatting

**[41:02]** Um the rest is just syntax formatting optimizations um

**[41:05]** optimizations um

**[41:05]** optimizations um key conventions. Yeah. And then the

**[41:07]** key conventions. Yeah. And then the

**[41:07]** key conventions. Yeah. And then the other format we have is github

**[41:10]** other format we have is github

**[41:10]** other format we have is github instructions.instructions.mmd.

**[41:18]** And those have this front matter syntax

**[41:18]** And those have this front matter syntax that's becoming more popular for rules

**[41:20]** that's becoming more popular for rules

**[41:20]** that's becoming more popular for rules of what what files it should apply to.

**[41:23]** of what what files it should apply to.

**[41:23]** of what what files it should apply to. So they start to be scoped with a glob

**[41:25]** So they start to be scoped with a glob

**[41:25]** So they start to be scoped with a glob pattern and then right now they're

**[41:29]** pattern and then right now they're

**[41:29]** pattern and then right now they're limited to being applied. You actually

**[41:30]** limited to being applied. You actually

**[41:30]** limited to being applied. You actually have to have the file in context. So a

**[41:33]** have to have the file in context. So a

**[41:33]** have to have the file in context. So a TypeScript file would only be applied if

**[41:35]** TypeScript file would only be applied if

**[41:35]** TypeScript file would only be applied if I actually do have a TypeScript file in

**[41:37]** I actually do have a TypeScript file in

**[41:37]** I actually do have a TypeScript file in here or I do have one open and then I

**[41:41]** here or I do have one open and then I

**[41:41]** here or I do have one open and then I enable this context then then it would

**[41:43]** enable this context then then it would

**[41:43]** enable this context then then it would be applied. But if I only have this

**[41:46]** be applied. But if I only have this

**[41:46]** be applied. But if I only have this right now, which means this isn't

**[41:47]** right now, which means this isn't

**[41:47]** right now, which means this isn't included, it wouldn't actually apply the

**[41:50]** included, it wouldn't actually apply the

**[41:50]** included, it wouldn't actually apply the rule. We're we're fixing that and it's

**[41:51]** rule. We're we're fixing that and it's

**[41:51]** rule. We're we're fixing that and it's going to be more

**[41:54]** going to be more

**[41:54]** going to be more working as expected probably. Um but

**[41:57]** working as expected probably. Um but

**[41:57]** working as expected probably. Um but that's that's right now that's like the

**[41:59]** that's that's right now that's like the

**[41:59]** that's that's right now that's like the biggest question I get like it didn't

### [42:00 - 43:00]

**[42:00]** biggest question I get like it didn't

**[42:00]** biggest question I get like it didn't include my rule because right now it

**[42:02]** include my rule because right now it

**[42:02]** include my rule because right now it really wants to see that file.

**[42:05]** really wants to see that file.

**[42:05]** really wants to see that file. Um yeah so those those are new uh those

**[42:09]** Um yeah so those those are new uh those

**[42:09]** Um yeah so those those are new uh those shipped I think the last version so they

**[42:10]** shipped I think the last version so they

**[42:10]** shipped I think the last version so they should be also in stable and we're

**[42:12]** should be also in stable and we're

**[42:12]** should be also in stable and we're actively working on those. So, and then

**[42:14]** actively working on those. So, and then

**[42:14]** actively working on those. So, and then the the new new thing is plans or

**[42:17]** the the new new thing is plans or

**[42:17]** the the new new thing is plans or prompts. And there we have the first

**[42:20]** prompts. And there we have the first

**[42:20]** prompts. And there we have the first kind of reusable tasks for as a team.

**[42:23]** kind of reusable tasks for as a team.

**[42:23]** kind of reusable tasks for as a team. How do you think about

**[42:25]** How do you think about

**[42:25]** How do you think about ingraining like, oh, we now have finally

**[42:27]** ingraining like, oh, we now have finally

**[42:27]** ingraining like, oh, we now have finally a way to tell GitHub copilot to write

**[42:29]** a way to tell GitHub copilot to write

**[42:29]** a way to tell GitHub copilot to write tests and your AI champion in the team

**[42:33]** tests and your AI champion in the team

**[42:33]** tests and your AI champion in the team handcraft this this perfect prompt which

**[42:36]** handcraft this this perfect prompt which

**[42:36]** handcraft this this perfect prompt which oneshots your test

**[42:38]** oneshots your test

**[42:38]** oneshots your test consistently and now everybody shares it

**[42:41]** consistently and now everybody shares it

**[42:41]** consistently and now everybody shares it in Slack, copies it around. Once you run

**[42:43]** in Slack, copies it around. Once you run

**[42:43]** in Slack, copies it around. Once you run the right test, you go back to Slack,

**[42:44]** the right test, you go back to Slack,

**[42:44]** the right test, you go back to Slack, copy it back, and that's what you want

**[42:46]** copy it back, and that's what you want

**[42:46]** copy it back, and that's what you want to use prompts for. You can finally put

**[42:48]** to use prompts for. You can finally put

**[42:48]** to use prompts for. You can finally put these prompts into a place where they

**[42:50]** these prompts into a place where they

**[42:50]** these prompts into a place where they can just be used by everybody. And how

**[42:53]** can just be used by everybody. And how

**[42:53]** can just be used by everybody. And how can they be used? So I showed these can

**[42:55]** can they be used? So I showed these can

**[42:55]** can they be used? So I showed these can actually be be attached. So you can also

**[42:57]** actually be be attached. So you can also

**[42:57]** actually be be attached. So you can also go in here

**[42:59]** go in here

### [43:00 - 44:00]

**[43:00]** go in here and attach instructions. So you can you

**[43:02]** and attach instructions. So you can you

**[43:02]** and attach instructions. So you can you can do it manually too. So that's one

**[43:04]** can do it manually too. So that's one

**[43:04]** can do it manually too. So that's one way. But I can also now go in here. I'm

**[43:07]** way. But I can also now go in here. I'm

**[43:07]** way. But I can also now go in here. I'm in the chat window and hit slash. And I

**[43:10]** in the chat window and hit slash. And I

**[43:10]** in the chat window and hit slash. And I can now actually run user prompts that

**[43:13]** can now actually run user prompts that

**[43:13]** can now actually run user prompts that are my own that I create for myself. And

**[43:15]** are my own that I create for myself. And

**[43:15]** are my own that I create for myself. And I can you use my plan and spec prompt

**[43:18]** I can you use my plan and spec prompt

**[43:18]** I can you use my plan and spec prompt you see over here on the left.

**[43:20]** you see over here on the left.

**[43:20]** you see over here on the left. &gt;&gt; Can you make that custom? Yes, these are

**[43:22]** &gt;&gt; Can you make that custom? Yes, these are

**[43:22]** &gt;&gt; Can you make that custom? Yes, these are custom ones. So the ones I have here,

**[43:24]** custom ones. So the ones I have here,

**[43:24]** custom ones. So the ones I have here, these are already custom in the

**[43:26]** these are already custom in the

**[43:26]** these are already custom in the workspace.

**[43:28]** workspace.

**[43:28]** workspace. And then the other ones

**[43:30]** And then the other ones

**[43:30]** And then the other ones I don't have I'm not showing. So I think

**[43:33]** I don't have I'm not showing. So I think

**[43:34]** I don't have I'm not showing. So I think we do there's a new menu.

**[43:37]** we do there's a new menu.

**[43:37]** we do there's a new menu. &gt;&gt; Yes. Yeah. Yeah.

**[43:40]** &gt;&gt; Yes. Yeah. Yeah.

**[43:40]** &gt;&gt; Yes. Yeah. Yeah. So let's make it here. Um,

**[43:42]** So let's make it here. Um,

**[43:42]** So let's make it here. Um, so this this one actually just landed

**[43:44]** so this this one actually just landed

**[43:44]** so this this one actually just landed yesterday because insiders we can now

**[43:46]** yesterday because insiders we can now

**[43:46]** yesterday because insiders we can now finally have an entry point because

**[43:47]** finally have an entry point because

**[43:47]** finally have an entry point because everybody kept asking how do I create

**[43:49]** everybody kept asking how do I create

**[43:49]** everybody kept asking how do I create prompts and I have to tell them which

**[43:50]** prompts and I have to tell them which

**[43:50]** prompts and I have to tell them which command to find it in. So this is the

**[43:53]** command to find it in. So this is the

**[43:53]** command to find it in. So this is the new prompt configuration file and I have

**[43:56]** new prompt configuration file and I have

**[43:56]** new prompt configuration file and I have some already here. So as you mentioned

**[43:58]** some already here. So as you mentioned

**[43:58]** some already here. So as you mentioned like this is one that's interesting for

### [44:00 - 45:00]

**[44:01]** like this is one that's interesting for

**[44:01]** like this is one that's interesting for um if I open this one this is like

**[44:04]** um if I open this one this is like

**[44:04]** um if I open this one this is like defining how I want to write custom

**[44:05]** defining how I want to write custom

**[44:05]** defining how I want to write custom instructions. So whenever I'm in a new

**[44:07]** instructions. So whenever I'm in a new

**[44:07]** instructions. So whenever I'm in a new project that doesn't have custom

**[44:08]** project that doesn't have custom

**[44:08]** project that doesn't have custom instructions yet, I do run this prompt

**[44:11]** instructions yet, I do run this prompt

**[44:11]** instructions yet, I do run this prompt to to bootstrap them for me.

**[44:14]** to to bootstrap them for me.

**[44:14]** to to bootstrap them for me. And yes, there should be a prompt

**[44:17]** And yes, there should be a prompt

**[44:17]** And yes, there should be a prompt sharing website where you can find these

**[44:19]** sharing website where you can find these

**[44:19]** sharing website where you can find these amazing prompts that I create. And next

**[44:22]** amazing prompts that I create. And next

**[44:22]** amazing prompts that I create. And next week we're going to

**[44:24]** week we're going to

**[44:24]** week we're going to &gt;&gt; So each problem is like a separate

**[44:28]** &gt;&gt; So each problem is like a separate

**[44:28]** &gt;&gt; So each problem is like a separate separate from each other.

**[44:29]** separate from each other.

**[44:29]** separate from each other. &gt;&gt; Yes. So that's the main difference

**[44:31]** &gt;&gt; Yes. So that's the main difference

**[44:31]** &gt;&gt; Yes. So that's the main difference between instructions. instructions are

**[44:33]** between instructions. instructions are

**[44:33]** between instructions. instructions are you can have multiple if you work on for

**[44:35]** you can have multiple if you work on for

**[44:35]** you can have multiple if you work on for example if you have one for TypeScript

**[44:37]** example if you have one for TypeScript

**[44:37]** example if you have one for TypeScript and one for your front-end folder they

**[44:40]** and one for your front-end folder they

**[44:40]** and one for your front-end folder they do combine because there's multiple

**[44:42]** do combine because there's multiple

**[44:42]** do combine because there's multiple instructions that hopefully don't

**[44:44]** instructions that hopefully don't

**[44:44]** instructions that hopefully don't conflict with each other um but they

**[44:47]** conflict with each other um but they

**[44:47]** conflict with each other um but they they allow you to be attaching multiple

**[44:49]** they allow you to be attaching multiple

**[44:49]** they allow you to be attaching multiple instructions and they're really more

**[44:51]** instructions and they're really more

**[44:51]** instructions and they're really more about code whereas prompts are basically

**[44:55]** about code whereas prompts are basically

**[44:55]** about code whereas prompts are basically uh easy ways to inject something in this

**[44:57]** uh easy ways to inject something in this

**[44:57]** uh easy ways to inject something in this prompt field and they stay in the

**[44:59]** prompt field and they stay in the

**[44:59]** prompt field and they stay in the conversation but They um they're mostly

### [45:00 - 46:00]

**[45:02]** conversation but They um they're mostly

**[45:02]** conversation but They um they're mostly around a task and maybe giving the AI

**[45:05]** around a task and maybe giving the AI

**[45:05]** around a task and maybe giving the AI something like specific to do.

**[45:07]** something like specific to do.

**[45:07]** something like specific to do. Instructions, you wouldn't necessarily

**[45:09]** Instructions, you wouldn't necessarily

**[45:09]** Instructions, you wouldn't necessarily give it like what to do, but more how to

**[45:12]** give it like what to do, but more how to

**[45:12]** give it like what to do, but more how to do it.

**[45:14]** do it.

**[45:14]** do it. &gt;&gt; What about if you wanted

**[45:18]** &gt;&gt; What about if you wanted

**[45:18]** &gt;&gt; What about if you wanted to

**[45:20]** to

**[45:20]** to always do TDD?

**[45:29]** &gt;&gt; Yeah. Yeah. So TDD um good point. Uh

**[45:29]** &gt;&gt; Yeah. Yeah. So TDD um good point. Uh that would be a good way to use custom

**[45:31]** that would be a good way to use custom

**[45:31]** that would be a good way to use custom modes. So if we go into here,

**[45:34]** modes. So if we go into here,

**[45:34]** modes. So if we go into here, custom uh mo sorry. So this is only

**[45:37]** custom uh mo sorry. So this is only

**[45:37]** custom uh mo sorry. So this is only insiders because it just landed. Sorry,

**[45:39]** insiders because it just landed. Sorry,

**[45:39]** insiders because it just landed. Sorry, you can't follow along or if you're not

**[45:41]** you can't follow along or if you're not

**[45:41]** you can't follow along or if you're not insiders. So custom modes will show up

**[45:45]** insiders. So custom modes will show up

**[45:45]** insiders. So custom modes will show up um in the dropdown. So this is like

**[45:48]** um in the dropdown. So this is like

**[45:48]** um in the dropdown. So this is like going to now it just went into the menu,

**[45:50]** going to now it just went into the menu,

**[45:50]** going to now it just went into the menu, created a custom mode, and now I can

**[45:52]** created a custom mode, and now I can

**[45:52]** created a custom mode, and now I can pick where it shows up. So got github/

**[45:55]** pick where it shows up. So got github/

**[45:55]** pick where it shows up. So got github/ chatmodes which put it into the

**[45:57]** chatmodes which put it into the

**[45:57]** chatmodes which put it into the repository or I just want to keep it for

### [46:00 - 47:00]

**[46:00]** repository or I just want to keep it for

**[46:00]** repository or I just want to keep it for myself. So a good pattern if you just

**[46:02]** myself. So a good pattern if you just

**[46:02]** myself. So a good pattern if you just want to experiment put it in your user

**[46:04]** want to experiment put it in your user

**[46:04]** want to experiment put it in your user folder. If you want to make everybody's

**[46:07]** folder. If you want to make everybody's

**[46:07]** folder. If you want to make everybody's life better in your team and you have

**[46:09]** life better in your team and you have

**[46:09]** life better in your team and you have high confidence that your mode does that

**[46:11]** high confidence that your mode does that

**[46:11]** high confidence that your mode does that then you put it into the project.

**[46:14]** then you put it into the project.

**[46:14]** then you put it into the project. And then uh we're going to do name this

**[46:16]** And then uh we're going to do name this

**[46:16]** And then uh we're going to do name this one TDD.

**[46:19]** one TDD.

**[46:19]** one TDD. And then we're gonna

**[46:23]** And then we're gonna

**[46:23]** And then we're gonna ask AI to fill it in, right? Uh prompt

**[46:28]** ask AI to fill it in, right? Uh prompt

**[46:28]** ask AI to fill it in, right? Uh prompt um expert expert prompt uh for just

**[46:32]** um expert expert prompt uh for just

**[46:32]** um expert expert prompt uh for just typing.

**[46:40]** Hi there AI. We need a prompt that

**[46:40]** Hi there AI. We need a prompt that enforces testdriven development uh for

**[46:43]** enforces testdriven development uh for

**[46:43]** enforces testdriven development uh for GitHub copilot. So it should probably

**[46:45]** GitHub copilot. So it should probably

**[46:45]** GitHub copilot. So it should probably first make sure it understands the

**[46:47]** first make sure it understands the

**[46:47]** first make sure it understands the problem then write tests first and only

**[46:49]** problem then write tests first and only

**[46:49]** problem then write tests first and only after tests are done maybe get

**[46:50]** after tests are done maybe get

**[46:50]** after tests are done maybe get confirmation from the user to then write

**[46:53]** confirmation from the user to then write

**[46:53]** confirmation from the user to then write the implementation and then keep running

**[46:55]** the implementation and then keep running

**[46:55]** the implementation and then keep running the tests against implementation. Cool.

**[46:58]** the tests against implementation. Cool.

**[46:58]** the tests against implementation. Cool. Thanks.

### [47:00 - 48:00]

**[47:00]** Thanks.

**[47:00]** Thanks. It's important.

**[47:09]** I didn't know I didn't say I'm now

**[47:09]** I didn't know I didn't say I'm now worried because I didn't actually

**[47:10]** worried because I didn't actually

**[47:10]** worried because I didn't actually activate my files context. Let's see if

**[47:12]** activate my files context. Let's see if

**[47:12]** activate my files context. Let's see if it

**[47:19]** I think it should have a tool to just

**[47:19]** I think it should have a tool to just create modes for you if you ask it. So

**[47:21]** create modes for you if you ask it. So

**[47:21]** create modes for you if you ask it. So it's gonna going to make that an MCP

**[47:22]** it's gonna going to make that an MCP

**[47:22]** it's gonna going to make that an MCP server next.

**[47:25]** server next.

**[47:25]** server next. Okay. Oh, it got it. Okay. Oh,

**[47:26]** Okay. Oh, it got it. Okay. Oh,

**[47:26]** Okay. Oh, it got it. Okay. Oh, wonderful. So we have a test driven

**[47:28]** wonderful. So we have a test driven

**[47:28]** wonderful. So we have a test driven development assistance. This is my code.

**[47:30]** development assistance. This is my code.

**[47:30]** development assistance. This is my code. We want read the code. Test development

**[47:32]** We want read the code. Test development

**[47:32]** We want read the code. Test development assistant core principles understand.

**[47:37]** assistant core principles understand.

**[47:37]** assistant core principles understand. Red write failing tests first.

**[47:39]** Red write failing tests first.

**[47:39]** Red write failing tests first. Beautiful. I wouldn't have not green.

**[47:41]** Beautiful. I wouldn't have not green.

**[47:41]** Beautiful. I wouldn't have not green. Wow, it does follow refactor, improve

**[47:43]** Wow, it does follow refactor, improve

**[47:43]** Wow, it does follow refactor, improve code quality, strict rules, noation

**[47:45]** code quality, strict rules, noation

**[47:45]** code quality, strict rules, noation tests. Beautiful. Beautiful. So, this

**[47:49]** tests. Beautiful. Beautiful. So, this

**[47:49]** tests. Beautiful. Beautiful. So, this our new TDD mode.

**[47:51]** our new TDD mode.

**[47:52]** our new TDD mode. Um,

**[47:53]** Um, &gt;&gt; we've done it four. Looks pretty good.

**[47:56]** &gt;&gt; we've done it four. Looks pretty good.

**[47:56]** &gt;&gt; we've done it four. Looks pretty good. It has emojis

**[47:59]** It has emojis

**[47:59]** It has emojis example. Should we try it out?

### [48:00 - 49:00]

**[48:03]** example. Should we try it out?

**[48:03]** example. Should we try it out? Okay, we have

**[48:16]** &gt;&gt; use a framework. It's framework

**[48:16]** &gt;&gt; use a framework. It's framework independence. Looks like

**[48:20]** independence. Looks like

**[48:20]** independence. Looks like &gt;&gt; Oh, just Yeah, I think it does some

**[48:22]** &gt;&gt; Oh, just Yeah, I think it does some

**[48:22]** &gt;&gt; Oh, just Yeah, I think it does some Yeah.

**[48:22]** Yeah.

**[48:22]** Yeah. &gt;&gt; Okay. So, it has it right there.

**[48:24]** &gt;&gt; Okay. So, it has it right there.

**[48:24]** &gt;&gt; Okay. So, it has it right there. &gt;&gt; It does make some stuff up. Yeah.

**[48:26]** &gt;&gt; It does make some stuff up. Yeah.

**[48:26]** &gt;&gt; It does make some stuff up. Yeah. Wouldn't need to do that. I can take

**[48:28]** Wouldn't need to do that. I can take

**[48:28]** Wouldn't need to do that. I can take this out. I already have my so

**[48:37]** um cool test drive the design wonderful

**[48:37]** um cool test drive the design wonderful okay let's do it so we have this project

**[48:39]** okay let's do it so we have this project

**[48:39]** okay let's do it so we have this project which doesn't do anything if you just

**[48:41]** which doesn't do anything if you just

**[48:41]** which doesn't do anything if you just run this um

**[48:44]** run this um

**[48:44]** run this um npm rundev probably doesn't I think I

**[48:47]** npm rundev probably doesn't I think I

**[48:47]** npm rundev probably doesn't I think I already did this before so this is just

**[48:50]** already did this before so this is just

**[48:50]** already did this before so this is just a basic plain landing page so let's do

**[48:53]** a basic plain landing page so let's do

**[48:53]** a basic plain landing page so let's do the um what feature do we have I want a

**[48:57]** the um what feature do we have I want a

**[48:57]** the um what feature do we have I want a dashboard for GitHub issues just use

**[48:59]** dashboard for GitHub issues just use

**[48:59]** dashboard for GitHub issues just use mock data because I don't want to wire

### [49:00 - 50:00]

**[49:00]** mock data because I don't want to wire

**[49:00]** mock data because I don't want to wire it up to GitHub. So, we want to have

**[49:02]** it up to GitHub. So, we want to have

**[49:02]** it up to GitHub. So, we want to have maybe some interesting contribution

**[49:03]** maybe some interesting contribution

**[49:03]** maybe some interesting contribution metrics. And but first, actually, let's

**[49:07]** metrics. And but first, actually, let's

**[49:07]** metrics. And but first, actually, let's make a plan.

**[49:10]** make a plan.

**[49:10]** make a plan. Meanwhile, while I type this in, let's

**[49:12]** Meanwhile, while I type this in, let's

**[49:12]** Meanwhile, while I type this in, let's stop it. Um, TDD.

**[49:21]** So, dashboard for GitHub.

**[49:21]** So, dashboard for GitHub. Um, don't worry.

**[49:24]** Um, don't worry.

**[49:24]** Um, don't worry. So now again we give it a very broad

**[49:26]** So now again we give it a very broad

**[49:26]** So now again we give it a very broad task but we can now put it into TDD mode

**[49:31]** task but we can now put it into TDD mode

**[49:31]** task but we can now put it into TDD mode which is our new amazing test and

**[49:34]** which is our new amazing test and

**[49:34]** which is our new amazing test and development mode that follows all the

**[49:35]** development mode that follows all the

**[49:35]** development mode that follows all the best practices I assume that the knows

**[49:37]** best practices I assume that the knows

**[49:37]** best practices I assume that the knows about TDD

**[49:39]** about TDD

**[49:40]** about TDD and let's see

**[49:43]** and let's see

**[49:44]** and let's see &gt;&gt; so wait that's you created a new mode

**[49:46]** &gt;&gt; so wait that's you created a new mode

**[49:46]** &gt;&gt; so wait that's you created a new mode there

**[49:46]** there

**[49:46]** there &gt;&gt; yeah because so we went previously went

**[49:49]** &gt;&gt; yeah because so we went previously went

**[49:49]** &gt;&gt; yeah because so we went previously went into configure chat modes we created a

**[49:51]** into configure chat modes we created a

**[49:51]** into configure chat modes we created a new mode this mode is Now enforcing the

**[49:54]** new mode this mode is Now enforcing the

**[49:54]** new mode this mode is Now enforcing the technique we can actually in a mode you

**[49:56]** technique we can actually in a mode you

**[49:56]** technique we can actually in a mode you can say which tools it's supposed to

**[49:57]** can say which tools it's supposed to

**[49:57]** can say which tools it's supposed to use.

**[49:58]** use.

**[49:58]** use. &gt;&gt; So

**[49:59]** &gt;&gt; So

**[49:59]** &gt;&gt; So &gt;&gt; is the mode

### [50:00 - 51:00]

**[50:06]** in agent mode but based on file. So it's

**[50:06]** in agent mode but based on file. So it's a it's a custom agent mode.

**[50:08]** a it's a custom agent mode.

**[50:08]** a it's a custom agent mode. &gt;&gt; Yes. Yeah.

**[50:09]** &gt;&gt; Yes. Yeah.

**[50:09]** &gt;&gt; Yes. Yeah. &gt;&gt; When is that going to be live?

**[50:11]** &gt;&gt; When is that going to be live?

**[50:11]** &gt;&gt; When is that going to be live? &gt;&gt; Uh it's in insiders now. It's going to

**[50:13]** &gt;&gt; Uh it's in insiders now. It's going to

**[50:13]** &gt;&gt; Uh it's in insiders now. It's going to ship next week on on the 11th.

**[50:16]** ship next week on on the 11th.

**[50:16]** ship next week on on the 11th. &gt;&gt; Yeah.

**[50:17]** &gt;&gt; Yeah. Insider ships.

**[50:20]** Insider ships.

**[50:20]** Insider ships. &gt;&gt; Insiders ships daily, but it only

**[50:22]** &gt;&gt; Insiders ships daily, but it only

**[50:22]** &gt;&gt; Insiders ships daily, but it only releases monthly. Yeah. And we're one

**[50:25]** releases monthly. Yeah. And we're one

**[50:26]** releases monthly. Yeah. And we're one one week late uh because there was a

**[50:28]** one week late uh because there was a

**[50:28]** one week late uh because there was a short short week, so we adjusted our

**[50:30]** short short week, so we adjusted our

**[50:30]** short short week, so we adjusted our schedule.

**[50:39]** Yes. Um so for most of you this menu

**[50:39]** Yes. Um so for most of you this menu will just have these entries and the in

**[50:43]** will just have these entries and the in

**[50:43]** will just have these entries and the in insiders only

**[50:45]** insiders only

**[50:45]** insiders only if you look for modes in the command

**[50:49]** if you look for modes in the command

**[50:49]** if you look for modes in the command pallet. So command pallet you can also

**[50:50]** pallet. So command pallet you can also

**[50:50]** pallet. So command pallet you can also click up here show run commands and then

**[50:54]** click up here show run commands and then

**[50:54]** click up here show run commands and then modes and that's that's the place

### [51:00 - 52:00]

**[51:21]** &gt;&gt; Yeah. Are they in in the output or in

**[51:21]** &gt;&gt; Yeah. Are they in in the output or in the problems view?

**[51:55]** &gt;&gt; It if it runs the commands itself, it

**[51:55]** &gt;&gt; It if it runs the commands itself, it will start looking at the term. So the

**[51:56]** will start looking at the term. So the

**[51:56]** will start looking at the term. So the easiest way if you if you run the

**[51:59]** easiest way if you if you run the

**[51:59]** easiest way if you if you run the deployment and the scripts itself

### [52:00 - 53:00]

**[52:01]** deployment and the scripts itself

**[52:01]** deployment and the scripts itself through co-pilot itself. But otherwise

**[52:03]** through co-pilot itself. But otherwise

**[52:03]** through co-pilot itself. But otherwise there's also context actually if you

**[52:05]** there's also context actually if you

**[52:05]** there's also context actually if you look here we have um the

**[52:14]** is actually

**[52:14]** is actually terminal last there's terminal last

**[52:16]** terminal last there's terminal last

**[52:16]** terminal last there's terminal last command which includes the output as

**[52:18]** command which includes the output as

**[52:18]** command which includes the output as well in term selection. Now if you ask

**[52:21]** well in term selection. Now if you ask

**[52:21]** well in term selection. Now if you ask me why they're not in the at context I I

**[52:23]** me why they're not in the at context I I

**[52:23]** me why they're not in the at context I I couldn't tell you right now. Yeah,

**[52:27]** couldn't tell you right now. Yeah,

**[52:27]** couldn't tell you right now. Yeah, but yeah, that's working. I think I did

**[52:29]** but yeah, that's working. I think I did

**[52:29]** but yeah, that's working. I think I did this thing wrong, though. TDD,

**[52:33]** this thing wrong, though. TDD,

**[52:33]** this thing wrong, though. TDD, let's just see.

**[52:39]** Oh, the tools. It configured it made up

**[52:40]** Oh, the tools. It configured it made up tools. So, it did that's that's the part

**[52:41]** tools. So, it did that's that's the part

**[52:41]** tools. So, it did that's that's the part it made up. This actually those are not

**[52:44]** it made up. This actually those are not

**[52:44]** it made up. This actually those are not the right tools.

**[52:46]** the right tools.

**[52:46]** the right tools. Um, this is why it didn't do anything

**[52:48]** Um, this is why it didn't do anything

**[52:48]** Um, this is why it didn't do anything was when I it just basically acted like

**[52:50]** was when I it just basically acted like

**[52:50]** was when I it just basically acted like chat and gave me the code because all

**[52:52]** chat and gave me the code because all

**[52:52]** chat and gave me the code because all the tools it tried were

**[52:55]** the tools it tried were

**[52:55]** the tools it tried were uh it didn't have any right access. So

**[52:58]** uh it didn't have any right access. So

**[52:58]** uh it didn't have any right access. So let's try this again.

### [53:00 - 54:00]

**[53:06]** So this probably a good good point to

**[53:06]** So this probably a good good point to good thing to point out. So in now

**[53:08]** good thing to point out. So in now

**[53:08]** good thing to point out. So in now prompts as well. Let me open plan

**[53:10]** prompts as well. Let me open plan

**[53:10]** prompts as well. Let me open plan prompt. So this one can actually now

**[53:12]** prompt. So this one can actually now

**[53:12]** prompt. So this one can actually now said tools

**[53:14]** said tools

**[53:14]** said tools and if you just make a tools entry here

**[53:17]** and if you just make a tools entry here

**[53:17]** and if you just make a tools entry here to tools

**[53:19]** to tools

**[53:19]** to tools you can now actually click here and say

**[53:21]** you can now actually click here and say

**[53:21]** you can now actually click here and say which tools in this case this is a

**[53:23]** which tools in this case this is a

**[53:23]** which tools in this case this is a planning prompts. So mostly you probably

**[53:25]** planning prompts. So mostly you probably

**[53:25]** planning prompts. So mostly you probably wanted to look at perplexity

**[53:28]** wanted to look at perplexity

**[53:28]** wanted to look at perplexity to come up with anything it needs to

**[53:30]** to come up with anything it needs to

**[53:30]** to come up with anything it needs to find on the internet. Uh I can select

**[53:32]** find on the internet. Uh I can select

**[53:32]** find on the internet. Uh I can select that. So that's the way you can now have

**[53:36]** that. So that's the way you can now have

**[53:36]** that. So that's the way you can now have tools constrained for a studio prompt.

**[53:41]** tools constrained for a studio prompt.

**[53:41]** tools constrained for a studio prompt. which which always helps with kind of

**[53:43]** which which always helps with kind of

**[53:43]** which which always helps with kind of higher quality because if you have many

**[53:44]** higher quality because if you have many

**[53:44]** higher quality because if you have many tools which as you install more MCP

**[53:46]** tools which as you install more MCP

**[53:46]** tools which as you install more MCP servers you always have this tooling

**[53:48]** servers you always have this tooling

**[53:48]** servers you always have this tooling explosion and they might solve all

**[53:49]** explosion and they might solve all

**[53:49]** explosion and they might solve all different problems you're having

**[53:50]** different problems you're having

**[53:50]** different problems you're having throughout the day but now you can

**[53:52]** throughout the day but now you can

**[53:52]** throughout the day but now you can configure it more specifically for

**[53:54]** configure it more specifically for

**[53:54]** configure it more specifically for domain and

**[53:57]** domain and

**[53:57]** domain and also insiders only we have tool

### [54:00 - 55:00]

**[54:05]** groups uh tool sets as should we call

**[54:06]** groups uh tool sets as should we call them so tool sets I And how do I get

**[54:10]** them so tool sets I And how do I get

**[54:10]** them so tool sets I And how do I get here? Um down here in the tool dropdown,

**[54:15]** here? Um down here in the tool dropdown,

**[54:15]** here? Um down here in the tool dropdown, configure tool sets and add more tools.

**[54:17]** configure tool sets and add more tools.

**[54:17]** configure tool sets and add more tools. This I think sends you to add server,

**[54:18]** This I think sends you to add server,

**[54:18]** This I think sends you to add server, but configure tool sets. Open this

**[54:21]** but configure tool sets. Open this

**[54:22]** but configure tool sets. Open this opens this one here. And that's only for

**[54:24]** opens this one here. And that's only for

**[54:24]** opens this one here. And that's only for &gt;&gt; servers, right?

**[54:25]** &gt;&gt; servers, right?

**[54:25]** &gt;&gt; servers, right? &gt;&gt; Anything both built in and MCP actually

**[54:29]** &gt;&gt; Anything both built in and MCP actually

**[54:29]** &gt;&gt; Anything both built in and MCP actually a lot of the tools you see here, we

**[54:31]** a lot of the tools you see here, we

**[54:31]** a lot of the tools you see here, we cleaned this list up. If you use

**[54:34]** cleaned this list up. If you use

**[54:34]** cleaned this list up. If you use insiders, you see them. Then these are

**[54:36]** insiders, you see them. Then these are

**[54:36]** insiders, you see them. Then these are actually tool sets already. So we use

**[54:38]** actually tool sets already. So we use

**[54:38]** actually tool sets already. So we use tool sets internally because edit files

**[54:40]** tool sets internally because edit files

**[54:40]** tool sets internally because edit files has multiple ways to edit files. We give

**[54:42]** has multiple ways to edit files. We give

**[54:42]** has multiple ways to edit files. We give the AI a few ways. Uh codebase search

**[54:45]** the AI a few ways. Uh codebase search

**[54:45]** the AI a few ways. Uh codebase search has grap has file search has different

**[54:47]** has grap has file search has different

**[54:48]** has grap has file search has different searches as well depending on what

**[54:49]** searches as well depending on what

**[54:49]** searches as well depending on what you're looking for. So all of these

**[54:51]** you're looking for. So all of these

**[54:51]** you're looking for. So all of these actually are tool sets in our own back

**[54:53]** actually are tool sets in our own back

**[54:53]** actually are tool sets in our own back end and we expose this now as something

**[54:55]** end and we expose this now as something

**[54:56]** end and we expose this now as something you can create yourself. So my research

**[54:58]** you can create yourself. So my research

**[54:58]** you can create yourself. So my research tool for example has the perplexity tool

### [55:00 - 56:00]

**[55:01]** tool for example has the perplexity tool

**[55:01]** tool for example has the perplexity tool to ask deep research questions and it

**[55:04]** to ask deep research questions and it

**[55:04]** to ask deep research questions and it also has fetch

**[55:18]** No, I didn't. No, we can show.

**[55:18]** No, I didn't. No, we can show. &gt;&gt; Yes, I can. Wouldn't be a talk without

**[55:21]** &gt;&gt; Yes, I can. Wouldn't be a talk without

**[55:21]** &gt;&gt; Yes, I can. Wouldn't be a talk without MCP. This is

**[55:27]** also there's a talk tomorrow about MCP,

**[55:27]** also there's a talk tomorrow about MCP, a whole talk track where I'll be talking

**[55:30]** a whole talk track where I'll be talking

**[55:30]** a whole talk track where I'll be talking about MCP if I can finish my slides.

**[55:33]** about MCP if I can finish my slides.

**[55:34]** about MCP if I can finish my slides. Um, okay, there we go. So let's talk

**[55:36]** Um, okay, there we go. So let's talk

**[55:36]** Um, okay, there we go. So let's talk about MCP. This is doing

**[55:39]** about MCP. This is doing

**[55:40]** about MCP. This is doing something. Let's see. Not

**[55:42]** something. Let's see. Not

**[55:42]** something. Let's see. Not understand requirement. It create mock

**[55:44]** understand requirement. It create mock

**[55:44]** understand requirement. It create mock data. Redph face writing tests. It wrote

**[55:47]** data. Redph face writing tests. It wrote

**[55:47]** data. Redph face writing tests. It wrote tests. It Oh, it found that there's a no

**[55:50]** tests. It Oh, it found that there's a no

**[55:50]** tests. It Oh, it found that there's a no package library. That's that's sad. Um

**[55:53]** package library. That's that's sad. Um

**[55:53]** package library. That's that's sad. Um and it created the test utility

**[55:57]** and it created the test utility

**[55:57]** and it created the test utility and then it tried to run the tests.

### [56:00 - 57:00]

**[56:01]** and then it tried to run the tests.

**[56:01]** and then it tried to run the tests. Um and then it asked to proceed. So

**[56:03]** Um and then it asked to proceed. So

**[56:03]** Um and then it asked to proceed. So that's cool. So it did the first stage

**[56:05]** that's cool. So it did the first stage

**[56:05]** that's cool. So it did the first stage of that mode. Um but I don't need to go

**[56:08]** of that mode. Um but I don't need to go

**[56:08]** of that mode. Um but I don't need to go too deep. But but that's modes TDD. It

**[56:11]** too deep. But but that's modes TDD. It

**[56:11]** too deep. But but that's modes TDD. It will ask now for because we asked it to

**[56:13]** will ask now for because we asked it to

**[56:13]** will ask now for because we asked it to ask for confirmation. So that's why it's

**[56:15]** ask for confirmation. So that's why it's

**[56:15]** ask for confirmation. So that's why it's now pausing. It wrote tests. Uh they're

**[56:17]** now pausing. It wrote tests. Uh they're

**[56:17]** now pausing. It wrote tests. Uh they're all red. So that's good.

**[56:21]** all red. So that's good.

**[56:21]** all red. So that's good. Okay, we accept it. And let's go into

**[56:23]** Okay, we accept it. And let's go into

**[56:23]** Okay, we accept it. And let's go into MCP. So MCP servers, who has already MCP

**[56:27]** MCP. So MCP servers, who has already MCP

**[56:27]** MCP. So MCP servers, who has already MCP servers set up in their VS Code?

**[56:31]** servers set up in their VS Code?

**[56:31]** servers set up in their VS Code? Good. Okay. Um,

**[56:35]** Good. Okay. Um,

**[56:35]** Good. Okay. Um, one way to get SP servers is editing

**[56:38]** one way to get SP servers is editing

**[56:38]** one way to get SP servers is editing JSON. And that's really, um, there's a

**[56:40]** JSON. And that's really, um, there's a

**[56:40]** JSON. And that's really, um, there's a few other ways, but let me show you

**[56:41]** few other ways, but let me show you

**[56:41]** few other ways, but let me show you another way. Um, Playright MCP. Who's

**[56:44]** another way. Um, Playright MCP. Who's

**[56:44]** another way. Um, Playright MCP. Who's been using Playright MCP? It's probably

**[56:47]** been using Playright MCP? It's probably

**[56:47]** been using Playright MCP? It's probably one of the coolest ones. Um, so

**[56:50]** one of the coolest ones. Um, so

**[56:50]** one of the coolest ones. Um, so Playright MCP is a browser testing

**[56:52]** Playright MCP is a browser testing

**[56:52]** Playright MCP is a browser testing framework and allows people to access

**[56:55]** framework and allows people to access

**[56:55]** framework and allows people to access the browser locally and just take

**[56:57]** the browser locally and just take

**[56:57]** the browser locally and just take screenshots, run websites, get

**[56:59]** screenshots, run websites, get

**[56:59]** screenshots, run websites, get accessibility audits, a whole bunch of

### [57:00 - 58:00]

**[57:01]** accessibility audits, a whole bunch of

**[57:01]** accessibility audits, a whole bunch of utility in there. and how to get it for

**[57:03]** utility in there. and how to get it for

**[57:04]** utility in there. and how to get it for VS Code. There's a JSON blob that you

**[57:06]** VS Code. There's a JSON blob that you

**[57:06]** VS Code. There's a JSON blob that you can all ignore and just hit install

**[57:08]** can all ignore and just hit install

**[57:08]** can all ignore and just hit install server.

**[57:14]** So install server is just a VS code

**[57:14]** So install server is just a VS code protocol that we use to just wire things

**[57:16]** protocol that we use to just wire things

**[57:16]** protocol that we use to just wire things up into VS Code. You see the same if you

**[57:18]** up into VS Code. You see the same if you

**[57:18]** up into VS Code. You see the same if you go to the extensions marketplace for VS

**[57:21]** go to the extensions marketplace for VS

**[57:21]** go to the extensions marketplace for VS Code, you can hit install extension that

**[57:23]** Code, you can hit install extension that

**[57:23]** Code, you can hit install extension that powers the same process. So now I can

**[57:26]** powers the same process. So now I can

**[57:26]** powers the same process. So now I can inst um don't hit show configuration. We

**[57:28]** inst um don't hit show configuration. We

**[57:28]** inst um don't hit show configuration. We need to move this down. But install

**[57:30]** need to move this down. But install

**[57:30]** need to move this down. But install server actually puts this now into my

**[57:32]** server actually puts this now into my

**[57:32]** server actually puts this now into my user settings. And so you can see you

**[57:35]** user settings. And so you can see you

**[57:35]** user settings. And so you can see you can have MCP servers both for yourself.

**[57:38]** can have MCP servers both for yourself.

**[57:38]** can have MCP servers both for yourself. And I have the one for GitHub and for

**[57:41]** And I have the one for GitHub and for

**[57:41]** And I have the one for GitHub and for GPAD which is a cool one. I can

**[57:43]** GPAD which is a cool one. I can

**[57:43]** GPAD which is a cool one. I can recommend this one.

**[57:45]** recommend this one.

**[57:45]** recommend this one. And then yeah play right now. So you can

**[57:48]** And then yeah play right now. So you can

**[57:48]** And then yeah play right now. So you can already see how many um tools I

**[57:52]** already see how many um tools I

**[57:52]** already see how many um tools I provided. You can see if anything fails

**[57:54]** provided. You can see if anything fails

**[57:54]** provided. You can see if anything fails you can get to the output.

**[57:57]** you can get to the output.

**[57:57]** you can get to the output. If there would be configuration, I can

### [58:00 - 59:00]

**[58:00]** If there would be configuration, I can

**[58:00]** If there would be configuration, I can show that here. There's actually just

**[58:03]** show that here. There's actually just

**[58:03]** show that here. There's actually just pad needs a GitHub token. So, it's a

**[58:04]** pad needs a GitHub token. So, it's a

**[58:04]** pad needs a GitHub token. So, it's a local MCP. And what have you ever seen

**[58:09]** local MCP. And what have you ever seen

**[58:09]** local MCP. And what have you ever seen that one? So, yay, no tokens in my

**[58:12]** that one? So, yay, no tokens in my

**[58:12]** that one? So, yay, no tokens in my configuration. So, you can use inputs in

**[58:14]** configuration. So, you can use inputs in

**[58:14]** configuration. So, you can use inputs in VS Code configuration both in the

**[58:16]** VS Code configuration both in the

**[58:16]** VS Code configuration both in the MCP.json and your settings. And inputs,

**[58:19]** MCP.json and your settings. And inputs,

**[58:19]** MCP.json and your settings. And inputs, you might have already seen those in

**[58:21]** you might have already seen those in

**[58:21]** you might have already seen those in tasks.json is how you configure your

**[58:24]** tasks.json is how you configure your

**[58:24]** tasks.json is how you configure your tests and your build steps in VS Code.

**[58:26]** tests and your build steps in VS Code.

**[58:26]** tests and your build steps in VS Code. It's the same system. Um, they're

**[58:29]** It's the same system. Um, they're

**[58:29]** It's the same system. Um, they're defined up here. So, inputs are just an

**[58:33]** defined up here. So, inputs are just an

**[58:33]** defined up here. So, inputs are just an ID, a type description, a default value,

**[58:35]** ID, a type description, a default value,

**[58:35]** ID, a type description, a default value, and the password true means it's

**[58:38]** and the password true means it's

**[58:38]** and the password true means it's encrypted at rest after you put it in.

**[58:41]** encrypted at rest after you put it in.

**[58:41]** encrypted at rest after you put it in. So, it doesn't ask me more.

**[58:43]** So, it doesn't ask me more.

**[58:43]** So, it doesn't ask me more. &gt;&gt; That's going to prompt you.

**[58:45]** &gt;&gt; That's going to prompt you.

**[58:45]** &gt;&gt; That's going to prompt you. &gt;&gt; It would if it but this this shows

**[58:46]** &gt;&gt; It would if it but this this shows

**[58:46]** &gt;&gt; It would if it but this this shows basically that it already has a token.

**[58:48]** basically that it already has a token.

**[58:48]** basically that it already has a token. But if you enter it the first time and

**[58:51]** But if you enter it the first time and

**[58:51]** But if you enter it the first time and we can actually try that if I

**[58:52]** we can actually try that if I

**[58:52]** we can actually try that if I &gt;&gt; where is it actually

**[58:54]** &gt;&gt; where is it actually

**[58:54]** &gt;&gt; where is it actually &gt;&gt; uh in VS codes key storage. So if on Mac

**[58:57]** &gt;&gt; uh in VS codes key storage. So if on Mac

**[58:57]** &gt;&gt; uh in VS codes key storage. So if on Mac it actually uses keychain.

**[58:59]** it actually uses keychain.

**[58:59]** it actually uses keychain. &gt;&gt; Oh okay.

### [59:00 - 01:00:00]

**[59:00]** &gt;&gt; Oh okay.

**[59:00]** &gt;&gt; Oh okay. &gt;&gt; Yeah. So

**[59:03]** &gt;&gt; Yeah. So

**[59:03]** &gt;&gt; Yeah. So &gt;&gt; what other MCP servers?

**[59:06]** &gt;&gt; what other MCP servers?

**[59:06]** &gt;&gt; what other MCP servers? &gt;&gt; Yeah. So I can show um JPAD is fun. It's

**[59:09]** &gt;&gt; Yeah. So I can show um JPAD is fun. It's

**[59:09]** &gt;&gt; Yeah. So I can show um JPAD is fun. It's done by actually um Zia GitHub. So

**[59:12]** done by actually um Zia GitHub. So

**[59:12]** done by actually um Zia GitHub. So Jispad.de justpadmc that's mostly I'm

**[59:15]** Jispad.de justpadmc that's mostly I'm

**[59:15]** Jispad.de justpadmc that's mostly I'm going to show it off tomorrow as well in

**[59:16]** going to show it off tomorrow as well in

**[59:16]** going to show it off tomorrow as well in my talk. Um, but it's a fun one that

**[59:20]** my talk. Um, but it's a fun one that

**[59:20]** my talk. Um, but it's a fun one that uses uh gists as a knowledge base and

**[59:24]** uses uh gists as a knowledge base and

**[59:24]** uses uh gists as a knowledge base and also for prompts. So, I really like this

**[59:26]** also for prompts. So, I really like this

**[59:26]** also for prompts. So, I really like this one. Uh, it adopts a ton of like recent

**[59:29]** one. Uh, it adopts a ton of like recent

**[59:29]** one. Uh, it adopts a ton of like recent MC MCP stuff, but I think the main ones

**[59:31]** MC MCP stuff, but I think the main ones

**[59:31]** MC MCP stuff, but I think the main ones we usually see is GitHub MCP server

**[59:35]** we usually see is GitHub MCP server

**[59:35]** we usually see is GitHub MCP server just pet just

**[59:40]** &gt;&gt; lost in tangent.

**[59:40]** &gt;&gt; lost in tangent. &gt;&gt; Okay.

**[59:41]** &gt;&gt; Okay. &gt;&gt; Yeah. So this if you just want to play

**[59:42]** &gt;&gt; Yeah. So this if you just want to play

**[59:42]** &gt;&gt; Yeah. So this if you just want to play around with it with a really well done

**[59:45]** around with it with a really well done

**[59:45]** around with it with a really well done MCP server, then that's that's one. Um

**[59:48]** MCP server, then that's that's one. Um

**[59:48]** MCP server, then that's that's one. Um not saying GitHub one isn't as good, but

**[59:51]** not saying GitHub one isn't as good, but

**[59:51]** not saying GitHub one isn't as good, but it's um

**[59:55]** it's um

**[59:55]** it's um there's a lot more coming here as well.

**[59:56]** there's a lot more coming here as well.

**[59:56]** there's a lot more coming here as well. So they're all in like really active

**[59:58]** So they're all in like really active

**[59:58]** So they're all in like really active development to figure out what the best

**[59:59]** development to figure out what the best

**[59:59]** development to figure out what the best way for MCP is. Yeah.

### [01:00:00 - 01:01:00]

**[01:00:33]** &gt;&gt; Yeah. Okay.

**[01:00:33]** &gt;&gt; Yeah. Okay. &gt;&gt; Okay.

**[01:00:35]** &gt;&gt; Okay. &gt;&gt; Right. And in your case, that server is

**[01:00:37]** &gt;&gt; Right. And in your case, that server is

**[01:00:37]** &gt;&gt; Right. And in your case, that server is already running. So, how to hook up?

**[01:00:39]** already running. So, how to hook up?

**[01:00:39]** already running. So, how to hook up? &gt;&gt; Okay. Cool. Yeah, let's do that. So, SSE

**[01:00:42]** &gt;&gt; Okay. Cool. Yeah, let's do that. So, SSE

**[01:00:42]** &gt;&gt; Okay. Cool. Yeah, let's do that. So, SSE um same way basically. So, what just

**[01:00:45]** um same way basically. So, what just

**[01:00:45]** um same way basically. So, what just finding my

**[01:00:48]** finding my

**[01:00:48]** finding my max it out? So, go back to my MCP. JSON

**[01:00:52]** max it out? So, go back to my MCP. JSON

**[01:00:52]** max it out? So, go back to my MCP. JSON and down here.

### [01:01:00 - 01:02:00]

**[01:01:00]** &gt;&gt; Yes. So, to clarification, MTP.json sits

**[01:01:00]** &gt;&gt; Yes. So, to clarification, MTP.json sits in docs code right now and it's per

**[01:01:02]** in docs code right now and it's per

**[01:01:02]** in docs code right now and it's per workspace and that's shared across

**[01:01:04]** workspace and that's shared across

**[01:01:04]** workspace and that's shared across everybody. So hopefully it puts stuff

**[01:01:06]** everybody. So hopefully it puts stuff

**[01:01:06]** everybody. So hopefully it puts stuff either you work on it alone and it's

**[01:01:08]** either you work on it alone and it's

**[01:01:08]** either you work on it alone and it's just for you or everybody is happy to

**[01:01:10]** just for you or everybody is happy to

**[01:01:10]** just for you or everybody is happy to have those MCP servers.

**[01:01:12]** have those MCP servers.

**[01:01:12]** have those MCP servers. &gt;&gt; Yeah.

**[01:01:14]** &gt;&gt; Yeah. &gt;&gt; Yeah.

**[01:01:22]** &gt;&gt; Yeah. Yeah. Okay. And then the what's

**[01:01:22]** &gt;&gt; Yeah. Yeah. Okay. And then the what's now if you hit add server you will find

**[01:01:24]** now if you hit add server you will find

**[01:01:24]** now if you hit add server you will find what you're looking for.

**[01:01:30]** And then from ads server you can hit

**[01:01:30]** And then from ads server you can hit down on HTTP. So we actually do support

**[01:01:32]** down on HTTP. So we actually do support

**[01:01:32]** down on HTTP. So we actually do support both SSE which is actually deprecated

**[01:01:35]** both SSE which is actually deprecated

**[01:01:35]** both SSE which is actually deprecated and streamable HTTP which is uh the the

**[01:01:39]** and streamable HTTP which is uh the the

**[01:01:39]** and streamable HTTP which is uh the the new fangled easier to scale better for

**[01:01:43]** new fangled easier to scale better for

**[01:01:43]** new fangled easier to scale better for your cloud.

**[01:01:49]** &gt;&gt; It's no long in the spec. Yes. And we do

**[01:01:49]** &gt;&gt; It's no long in the spec. Yes. And we do fall back to it on a client side but

**[01:01:52]** fall back to it on a client side but

**[01:01:52]** fall back to it on a client side but it's it's the SSE is really hard on on

**[01:01:54]** it's it's the SSE is really hard on on

**[01:01:54]** it's it's the SSE is really hard on on hosting right because they have these

**[01:01:56]** hosting right because they have these

**[01:01:56]** hosting right because they have these long running connections long

**[01:01:58]** long running connections long

**[01:01:58]** long running connections long &gt;&gt; long. Yeah. Yeah. So

### [01:02:00 - 01:03:00]

**[01:02:04]** yeah, so that's that's where you put in

**[01:02:04]** yeah, so that's that's where you put in your yeah your MCP sec server. And if

**[01:02:06]** your yeah your MCP sec server. And if

**[01:02:06]** your yeah your MCP sec server. And if you want to do it manually, it's really

**[01:02:07]** you want to do it manually, it's really

**[01:02:07]** you want to do it manually, it's really just um

**[01:02:10]** just um

**[01:02:10]** just um you get a nice autocomplete too. So if

**[01:02:12]** you get a nice autocomplete too. So if

**[01:02:12]** you get a nice autocomplete too. So if you pick a name

**[01:02:25]** example and um this would be the type

**[01:02:25]** example and um this would be the type would be

**[01:02:27]** would be

**[01:02:27]** would be not studio actually it's http yeah you

**[01:02:30]** not studio actually it's http yeah you

**[01:02:30]** not studio actually it's http yeah you already would you would use http and I

**[01:02:32]** already would you would use http and I

**[01:02:32]** already would you would use http and I would already yell at you that you don't

**[01:02:33]** would already yell at you that you don't

**[01:02:33]** would already yell at you that you don't have a URL so I'm going to put URL

**[01:02:37]** have a URL so I'm going to put URL

**[01:02:37]** have a URL so I'm going to put URL so this this is how uh everything is by

**[01:02:40]** so this this is how uh everything is by

**[01:02:40]** so this this is how uh everything is by default as stdio once you have a URL

**[01:02:41]** default as stdio once you have a URL

**[01:02:42]** default as stdio once you have a URL Well, I think I can take this out. Yeah.

**[01:02:44]** Well, I think I can take this out. Yeah.

**[01:02:44]** Well, I think I can take this out. Yeah. So, would be just that entry.

### [01:03:00 - 01:04:00]

**[01:03:02]** Yes. So to get Yes. Um so many demos I

**[01:03:02]** Yes. So to get Yes. Um so many demos I see people hit start here as well just

**[01:03:04]** see people hit start here as well just

**[01:03:04]** see people hit start here as well just to see that it's working. It's a nice

**[01:03:06]** to see that it's working. It's a nice

**[01:03:06]** to see that it's working. It's a nice configuration that just make sure it's

**[01:03:08]** configuration that just make sure it's

**[01:03:08]** configuration that just make sure it's working. We actually do cache the tools

**[01:03:10]** working. We actually do cache the tools

**[01:03:10]** working. We actually do cache the tools once we saw them the first time. So how

**[01:03:12]** once we saw them the first time. So how

**[01:03:12]** once we saw them the first time. So how MCP works is that on the first init

**[01:03:16]** MCP works is that on the first init

**[01:03:16]** MCP works is that on the first init initialization from the client to the

**[01:03:18]** initialization from the client to the

**[01:03:18]** initialization from the client to the server, it shares its tools back and

**[01:03:20]** server, it shares its tools back and

**[01:03:20]** server, it shares its tools back and that's what you see here, the one tool.

**[01:03:23]** that's what you see here, the one tool.

**[01:03:23]** that's what you see here, the one tool. So if you would do it right, you would

**[01:03:25]** So if you would do it right, you would

**[01:03:25]** So if you would do it right, you would never know the tools unless you start

**[01:03:27]** never know the tools unless you start

**[01:03:27]** never know the tools unless you start the server. We actually cache them. So

**[01:03:29]** the server. We actually cache them. So

**[01:03:29]** the server. We actually cache them. So you don't have to we don't have to start

**[01:03:31]** you don't have to we don't have to start

**[01:03:31]** you don't have to we don't have to start all the servers proactively once you

**[01:03:32]** all the servers proactively once you

**[01:03:32]** all the servers proactively once you open Copilot just to get the tools.

**[01:03:48]** &gt;&gt; No, actually you want to be in agent

**[01:03:48]** &gt;&gt; No, actually you want to be in agent mode. Agent mode ask mode will not run

**[01:03:50]** mode. Agent mode ask mode will not run

**[01:03:50]** mode. Agent mode ask mode will not run MCPS for you. uh you can you can go

**[01:03:55]** MCPS for you. uh you can you can go

**[01:03:55]** MCPS for you. uh you can you can go uh because as mode is not uh it's not

**[01:03:57]** uh because as mode is not uh it's not

**[01:03:57]** uh because as mode is not uh it's not actually there's no function calling

**[01:03:59]** actually there's no function calling

**[01:03:59]** actually there's no function calling inherently right fun as mode is really

### [01:04:00 - 01:05:00]

**[01:04:01]** inherently right fun as mode is really

**[01:04:01]** inherently right fun as mode is really this traditional askd question will

**[01:04:03]** this traditional askd question will

**[01:04:03]** this traditional askd question will answer based on its training there or

**[01:04:05]** answer based on its training there or

**[01:04:05]** answer based on its training there or its context

**[01:04:06]** its context

**[01:04:06]** its context um

**[01:04:09]** um yes so there is also an ask what you

**[01:04:12]** yes so there is also an ask what you

**[01:04:12]** yes so there is also an ask what you don't have tools you would see it um but

**[01:04:13]** don't have tools you would see it um but

**[01:04:14]** don't have tools you would see it um but I can do actually does this still work

**[01:04:17]** I can do actually does this still work

**[01:04:17]** I can do actually does this still work Um,

**[01:04:25]** let's do that more quickly.

**[01:04:25]** let's do that more quickly. I think we actually do this still.

**[01:04:29]** I think we actually do this still.

**[01:04:29]** I think we actually do this still. Yes. So, we're actually blurring the

**[01:04:30]** Yes. So, we're actually blurring the

**[01:04:30]** Yes. So, we're actually blurring the line a bit now. So, if you do That's not

**[01:04:33]** line a bit now. So, if you do That's not

**[01:04:33]** line a bit now. So, if you do That's not working. Okay.

**[01:04:35]** working. Okay.

**[01:04:35]** working. Okay. Yeah. But if you actually reference

**[01:04:37]** Yeah. But if you actually reference

**[01:04:37]** Yeah. But if you actually reference specific tools in ask mode, it will

**[01:04:39]** specific tools in ask mode, it will

**[01:04:39]** specific tools in ask mode, it will invoke them for you. But by default, the

**[01:04:41]** invoke them for you. But by default, the

**[01:04:41]** invoke them for you. But by default, the the way where you want to execute tools

**[01:04:43]** the way where you want to execute tools

**[01:04:43]** the way where you want to execute tools is in agent mode.

### [01:05:00 - 01:06:00]

**[01:05:09]** &gt;&gt; Uh they're all coming through GitHub

**[01:05:09]** &gt;&gt; Uh they're all coming through GitHub copilot. So they're all using your paid.

**[01:05:12]** copilot. So they're all using your paid.

**[01:05:12]** copilot. So they're all using your paid. Uh you can add your own models. Anybody

**[01:05:15]** Uh you can add your own models. Anybody

**[01:05:15]** Uh you can add your own models. Anybody has tried it managing your model? So um

**[01:05:18]** has tried it managing your model? So um

**[01:05:18]** has tried it managing your model? So um so I have gamma 3 through lama which

**[01:05:21]** so I have gamma 3 through lama which

**[01:05:21]** so I have gamma 3 through lama which runs locally and I have open routers

**[01:05:23]** runs locally and I have open routers

**[01:05:23]** runs locally and I have open routers perplexity R1 uh which is actually a

**[01:05:26]** perplexity R1 uh which is actually a

**[01:05:26]** perplexity R1 uh which is actually a fine-tuned model from of deepseek R1

**[01:05:29]** fine-tuned model from of deepseek R1

**[01:05:29]** fine-tuned model from of deepseek R1 from perplexity. So if you haven't tried

**[01:05:31]** from perplexity. So if you haven't tried

**[01:05:31]** from perplexity. So if you haven't tried it yet, uh basically go into the model

**[01:05:33]** it yet, uh basically go into the model

**[01:05:33]** it yet, uh basically go into the model picker and hit manage models and then we

**[01:05:35]** picker and hit manage models and then we

**[01:05:35]** picker and hit manage models and then we we can actually custom configure your

**[01:05:37]** we can actually custom configure your

**[01:05:37]** we can actually custom configure your own API keys from Enthropic, Azure,

**[01:05:40]** own API keys from Enthropic, Azure,

**[01:05:40]** own API keys from Enthropic, Azure, Cerebras, Grammite, Rock, all of these.

**[01:05:42]** Cerebras, Grammite, Rock, all of these.

**[01:05:42]** Cerebras, Grammite, Rock, all of these. Um Olama is the local one. So if you

**[01:05:45]** Um Olama is the local one. So if you

**[01:05:45]** Um Olama is the local one. So if you have a beefy M4 Pro, I'm still sad how

**[01:05:47]** have a beefy M4 Pro, I'm still sad how

**[01:05:48]** have a beefy M4 Pro, I'm still sad how many models I can actually run on this,

**[01:05:49]** many models I can actually run on this,

**[01:05:49]** many models I can actually run on this, but but eventually it's going to be

**[01:05:51]** but but eventually it's going to be

**[01:05:51]** but but eventually it's going to be small powerful models. Um that makes

**[01:05:54]** small powerful models. Um that makes

**[01:05:54]** small powerful models. Um that makes sense. So

### [01:06:00 - 01:07:00]

**[01:06:04]** Uh, it might be because of your

**[01:06:04]** Uh, it might be because of your anthropic tier, right? That's

**[01:06:08]** anthropic tier, right? That's

**[01:06:08]** anthropic tier, right? That's um or is it

**[01:06:11]** um or is it

**[01:06:11]** um or is it &gt;&gt; you have four? Oh. Oh. Uh, the other

**[01:06:13]** &gt;&gt; you have four? Oh. Oh. Uh, the other

**[01:06:13]** &gt;&gt; you have four? Oh. Oh. Uh, the other one. Yeah, you might be in agent mode.

**[01:06:15]** one. Yeah, you might be in agent mode.

**[01:06:16]** one. Yeah, you might be in agent mode. So, we do actually filter them down. So,

**[01:06:17]** So, we do actually filter them down. So,

**[01:06:17]** So, we do actually filter them down. So, that's an ongoing improvement we're

**[01:06:18]** that's an ongoing improvement we're

**[01:06:18]** that's an ongoing improvement we're doing. That's why it's not it's right

**[01:06:20]** doing. That's why it's not it's right

**[01:06:20]** doing. That's why it's not it's right now a preview feature only because we're

**[01:06:22]** now a preview feature only because we're

**[01:06:22]** now a preview feature only because we're still having to connectly correctly wire

**[01:06:24]** still having to connectly correctly wire

**[01:06:24]** still having to connectly correctly wire up which model allows tool calling. So

**[01:06:27]** up which model allows tool calling. So

**[01:06:27]** up which model allows tool calling. So there's some some every provider has

**[01:06:30]** there's some some every provider has

**[01:06:30]** there's some some every provider has different indicators of how tool calling

**[01:06:32]** different indicators of how tool calling

**[01:06:32]** different indicators of how tool calling works and that's that's one of the

**[01:06:33]** works and that's that's one of the

**[01:06:33]** works and that's that's one of the matching things we're doing right now.

**[01:06:35]** matching things we're doing right now.

**[01:06:35]** matching things we're doing right now. So you might not see it because it's not

**[01:06:36]** So you might not see it because it's not

**[01:06:36]** So you might not see it because it's not on our our list yet.

**[01:06:51]** &gt;&gt; Yes. Yeah. You you will see that. So if

**[01:06:52]** &gt;&gt; Yes. Yeah. You you will see that. So if I do just um one example here

**[01:06:56]** I do just um one example here

**[01:06:56]** I do just um one example here uh so just bad so a you can disable them

### [01:07:00 - 01:08:00]

**[01:07:00]** uh so just bad so a you can disable them

**[01:07:00]** uh so just bad so a you can disable them if you already if you want to be faster

**[01:07:01]** if you already if you want to be faster

**[01:07:01]** if you already if you want to be faster you can do command down and just go

**[01:07:03]** you can do command down and just go

**[01:07:04]** you can do command down and just go through. So contact 7 is the one I want

**[01:07:06]** through. So contact 7 is the one I want

**[01:07:06]** through. So contact 7 is the one I want to keep player I can disable right now

**[01:07:08]** to keep player I can disable right now

**[01:07:08]** to keep player I can disable right now but once you start using them

**[01:07:11]** but once you start using them

**[01:07:12]** but once you start using them &gt;&gt; this is command up and down the power

**[01:07:15]** &gt;&gt; this is command up and down the power

**[01:07:15]** &gt;&gt; this is command up and down the power user way of navigating

**[01:07:17]** user way of navigating

**[01:07:17]** user way of navigating those. So these are all built-in MCP

**[01:07:19]** those. So these are all built-in MCP

**[01:07:20]** those. So these are all built-in MCP servers. And once you start, you can

**[01:07:21]** servers. And once you start, you can

**[01:07:21]** servers. And once you start, you can actually now if I want to be very

**[01:07:23]** actually now if I want to be very

**[01:07:23]** actually now if I want to be very explicit and I know which tools I want,

**[01:07:25]** explicit and I know which tools I want,

**[01:07:25]** explicit and I know which tools I want, I can use my tool sets or I can mention

**[01:07:28]** I can use my tool sets or I can mention

**[01:07:28]** I can use my tool sets or I can mention specific tools that are um in in my

**[01:07:31]** specific tools that are um in in my

**[01:07:31]** specific tools that are um in in my list. But I can also now just go in and

**[01:07:34]** list. But I can also now just go in and

**[01:07:34]** list. But I can also now just go in and say what do we want to do here? Um

**[01:07:37]** say what do we want to do here? Um

**[01:07:38]** say what do we want to do here? Um research

**[01:07:39]** research

**[01:07:40]** research uh

**[01:07:42]** uh GitHub metrics.

**[01:07:45]** GitHub metrics.

**[01:07:45]** GitHub metrics. Let's actually use the research one

**[01:07:46]** Let's actually use the research one

**[01:07:46]** Let's actually use the research one because we created it.

**[01:07:49]** because we created it.

**[01:07:49]** because we created it. Sounds better when I use research here.

**[01:07:51]** Sounds better when I use research here.

**[01:07:51]** Sounds better when I use research here. Use it in a sentence

**[01:07:54]** Use it in a sentence

**[01:07:54]** Use it in a sentence for productivity.

### [01:08:00 - 01:09:00]

**[01:08:00]** And what happens now is uh this one has

**[01:08:00]** And what happens now is uh this one has now is an agent mode. We have the

**[01:08:02]** now is an agent mode. We have the

**[01:08:02]** now is an agent mode. We have the research group set or tool set. So we'll

**[01:08:05]** research group set or tool set. So we'll

**[01:08:05]** research group set or tool set. So we'll either use perplexity or fetch.

**[01:08:12]** And one of my perplexity keys actually

**[01:08:12]** And one of my perplexity keys actually outdated because it failed before. Let's

**[01:08:14]** outdated because it failed before. Let's

**[01:08:14]** outdated because it failed before. Let's see. Okay, so you see I already actually

**[01:08:16]** see. Okay, so you see I already actually

**[01:08:16]** see. Okay, so you see I already actually proved this before. So you see a that it

**[01:08:20]** proved this before. So you see a that it

**[01:08:20]** proved this before. So you see a that it runs the server and you actually click

**[01:08:21]** runs the server and you actually click

**[01:08:21]** runs the server and you actually click the server to see where it comes from.

**[01:08:24]** the server to see where it comes from.

**[01:08:24]** the server to see where it comes from. Um if I would have not autoproofed this

**[01:08:27]** Um if I would have not autoproofed this

**[01:08:27]** Um if I would have not autoproofed this because auto proof is still on from our

**[01:08:29]** because auto proof is still on from our

**[01:08:29]** because auto proof is still on from our previous session, you can actually go in

**[01:08:32]** previous session, you can actually go in

**[01:08:32]** previous session, you can actually go in here and edit what it's sending.

**[01:08:35]** here and edit what it's sending.

**[01:08:35]** here and edit what it's sending. Um which now doesn't make sense because

**[01:08:36]** Um which now doesn't make sense because

**[01:08:36]** Um which now doesn't make sense because it's it's already sent and then it

**[01:08:39]** it's it's already sent and then it

**[01:08:39]** it's it's already sent and then it writes up uh what it found in this case.

**[01:08:42]** writes up uh what it found in this case.

**[01:08:42]** writes up uh what it found in this case. Does that ask?

**[01:08:45]** Does that ask?

**[01:08:46]** Does that ask? &gt;&gt; Uh, that's just the odd name for the

**[01:08:48]** &gt;&gt; Uh, that's just the odd name for the

**[01:08:48]** &gt;&gt; Uh, that's just the odd name for the perplexity tool.

**[01:08:50]** perplexity tool.

**[01:08:50]** perplexity tool. &gt;&gt; It happens to coincide.

**[01:08:52]** &gt;&gt; It happens to coincide.

**[01:08:52]** &gt;&gt; It happens to coincide. &gt;&gt; Yes. Yeah. Yeah. It's just um the verb

**[01:08:55]** &gt;&gt; Yes. Yeah. Yeah. It's just um the verb

**[01:08:55]** &gt;&gt; Yes. Yeah. Yeah. It's just um the verb should be before. So, it's their their

**[01:08:57]** should be before. So, it's their their

**[01:08:57]** should be before. So, it's their their naming. Yeah.

### [01:09:00 - 01:10:00]

**[01:09:01]** naming. Yeah.

**[01:09:01]** naming. Yeah. Yeah. So, that's now run two. It

**[01:09:03]** Yeah. So, that's now run two. It

**[01:09:03]** Yeah. So, that's now run two. It actually did a follow-up query as well

**[01:09:06]** actually did a follow-up query as well

**[01:09:06]** actually did a follow-up query as well and explained it. And now I could put

**[01:09:08]** and explained it. And now I could put

**[01:09:08]** and explained it. And now I could put this in into a spec as well. It's

**[01:09:10]** this in into a spec as well. It's

**[01:09:10]** this in into a spec as well. It's actually I did this before. So I wrote a

**[01:09:12]** actually I did this before. So I wrote a

**[01:09:12]** actually I did this before. So I wrote a spec using for community dashboard. So I

**[01:09:15]** spec using for community dashboard. So I

**[01:09:15]** spec using for community dashboard. So I did the research using perplexity and

**[01:09:17]** did the research using perplexity and

**[01:09:18]** did the research using perplexity and then ask it to write a spec from it

**[01:09:20]** then ask it to write a spec from it

**[01:09:20]** then ask it to write a spec from it using a little query I have here for the

**[01:09:22]** using a little query I have here for the

**[01:09:22]** using a little query I have here for the spec. Um

**[01:09:26]** spec. Um

**[01:09:26]** spec. Um so that's one way you can quickly get

**[01:09:27]** so that's one way you can quickly get

**[01:09:27]** so that's one way you can quickly get things done.

**[01:09:29]** things done.

**[01:09:29]** things done. And just to point out this one, it's a

**[01:09:32]** And just to point out this one, it's a

**[01:09:32]** And just to point out this one, it's a pointing it to the spec. So these are

**[01:09:34]** pointing it to the spec. So these are

**[01:09:34]** pointing it to the spec. So these are actually resolved by the AI. So if you

**[01:09:36]** actually resolved by the AI. So if you

**[01:09:36]** actually resolved by the AI. So if you point it to specific files, we do

**[01:09:38]** point it to specific files, we do

**[01:09:38]** point it to specific files, we do actually validate those as well. So if

**[01:09:39]** actually validate those as well. So if

**[01:09:39]** actually validate those as well. So if you get them wrong, I think they're

**[01:09:41]** you get them wrong, I think they're

**[01:09:41]** you get them wrong, I think they're underlined. Um, you can also click them

**[01:09:44]** underlined. Um, you can also click them

**[01:09:44]** underlined. Um, you can also click them so you get all the markdown

**[01:09:47]** so you get all the markdown

**[01:09:47]** so you get all the markdown goodies. Um, and then you just ask it to

**[01:09:50]** goodies. Um, and then you just ask it to

**[01:09:50]** goodies. Um, and then you just ask it to write on the spec. Do nothing else. Uh,

**[01:09:52]** write on the spec. Do nothing else. Uh,

**[01:09:52]** write on the spec. Do nothing else. Uh, use perplexity to look up stuff.

**[01:09:55]** use perplexity to look up stuff.

**[01:09:55]** use perplexity to look up stuff. Don't lose details. Keep updating the

**[01:09:57]** Don't lose details. Keep updating the

**[01:09:57]** Don't lose details. Keep updating the spec. So that's that's one way to work

**[01:09:59]** spec. So that's that's one way to work

**[01:09:59]** spec. So that's that's one way to work on specs. There's probably more more

### [01:10:00 - 01:11:00]

**[01:10:01]** on specs. There's probably more more

**[01:10:01]** on specs. There's probably more more tools we we're going to add here. Yeah.

**[01:10:04]** tools we we're going to add here. Yeah.

**[01:10:04]** tools we we're going to add here. Yeah. So that's MCP. Any other MCP questions?

**[01:10:15]** uh per MCP. So the MCP itself doesn't

**[01:10:15]** uh per MCP. So the MCP itself doesn't run anything except when you support

**[01:10:18]** run anything except when you support

**[01:10:18]** run anything except when you support sampling

**[01:10:20]** sampling

**[01:10:20]** sampling which we do on insiders. Sneak preview

**[01:10:24]** which we do on insiders. Sneak preview

**[01:10:24]** which we do on insiders. Sneak preview for tomorrow. So but yeah, if you use

**[01:10:27]** for tomorrow. So but yeah, if you use

**[01:10:27]** for tomorrow. So but yeah, if you use sampling, actually I guess I have to

**[01:10:30]** sampling, actually I guess I have to

**[01:10:30]** sampling, actually I guess I have to explain sampling. So as sampling is a

**[01:10:31]** explain sampling. So as sampling is a

**[01:10:31]** explain sampling. So as sampling is a way for MCP to reach back out from the

**[01:10:34]** way for MCP to reach back out from the

**[01:10:34]** way for MCP to reach back out from the server to the client to use the LLM on

**[01:10:37]** server to the client to use the LLM on

**[01:10:37]** server to the client to use the LLM on the client and it's you can often think

**[01:10:41]** the client and it's you can often think

**[01:10:41]** the client and it's you can often think the best use cases are to summarize use

**[01:10:43]** the best use cases are to summarize use

**[01:10:43]** the best use cases are to summarize use cases are if you want to um reduce the

**[01:10:46]** cases are if you want to um reduce the

**[01:10:46]** cases are if you want to um reduce the amount of tokens you send to the back to

**[01:10:49]** amount of tokens you send to the back to

**[01:10:49]** amount of tokens you send to the back to the client to explain something. So

**[01:10:51]** the client to explain something. So

**[01:10:51]** the client to explain something. So there's a few ways, but um overall

**[01:10:55]** there's a few ways, but um overall

**[01:10:55]** there's a few ways, but um overall there's not enough integration of

**[01:10:57]** there's not enough integration of

**[01:10:57]** there's not enough integration of sampling. Um but so we are the first

**[01:10:59]** sampling. Um but so we are the first

**[01:10:59]** sampling. Um but so we are the first ones to to get it out there because we

### [01:11:00 - 01:12:00]

**[01:11:01]** ones to to get it out there because we

**[01:11:01]** ones to to get it out there because we already have the LMX posts. So that's

**[01:11:03]** already have the LMX posts. So that's

**[01:11:03]** already have the LMX posts. So that's cool.

**[01:11:21]** &gt;&gt; Yeah. to pick the model kind of.

**[01:11:21]** &gt;&gt; Yeah. to pick the model kind of. &gt;&gt; No.

**[01:11:33]** &gt;&gt; Yeah. &gt;&gt; But it's still hardly

**[01:11:36]** &gt;&gt; But it's still hardly

**[01:11:36]** &gt;&gt; But it's still hardly &gt;&gt; right. So,

**[01:11:38]** &gt;&gt; right. So,

**[01:11:38]** &gt;&gt; right. So, &gt;&gt; so

**[01:11:45]** &gt;&gt; yeah. So, what I recommend is a in in

**[01:11:45]** &gt;&gt; yeah. So, what I recommend is a in in your modes boil down the tools to what

**[01:11:48]** your modes boil down the tools to what

**[01:11:48]** your modes boil down the tools to what you actually need. So reducing the tools

**[01:11:50]** you actually need. So reducing the tools

**[01:11:50]** you actually need. So reducing the tools manually either deterministicity already

**[01:11:53]** manually either deterministicity already

**[01:11:53]** manually either deterministicity already in in your prom. So this prompt could

**[01:11:55]** in in your prom. So this prompt could

**[01:11:55]** in in your prom. So this prompt could have tools for like what it should

**[01:11:57]** have tools for like what it should

**[01:11:57]** have tools for like what it should actually do right that would be one way

**[01:11:59]** actually do right that would be one way

**[01:11:59]** actually do right that would be one way and then I can configure what do I

### [01:12:00 - 01:13:00]

**[01:12:00]** and then I can configure what do I

**[01:12:00]** and then I can configure what do I actually want to have here like this

**[01:12:02]** actually want to have here like this

**[01:12:02]** actually want to have here like this should be only doing perplexity because

**[01:12:04]** should be only doing perplexity because

**[01:12:04]** should be only doing perplexity because I it needs to do research and that's all

**[01:12:05]** I it needs to do research and that's all

**[01:12:06]** I it needs to do research and that's all it should do

**[01:12:06]** it should do

**[01:12:06]** it should do &gt;&gt; with custom mode that

**[01:12:09]** &gt;&gt; with custom mode that

**[01:12:09]** &gt;&gt; with custom mode that &gt;&gt; custom mode. Yeah pockets of like this

**[01:12:12]** &gt;&gt; custom mode. Yeah pockets of like this

**[01:12:12]** &gt;&gt; custom mode. Yeah pockets of like this like this right then you kind of pick

**[01:12:13]** like this right then you kind of pick

**[01:12:13]** like this right then you kind of pick your pockets of

**[01:12:15]** your pockets of

**[01:12:15]** your pockets of &gt;&gt; Yes. So custom mode is one way and then

**[01:12:17]** &gt;&gt; Yes. So custom mode is one way and then

**[01:12:17]** &gt;&gt; Yes. So custom mode is one way and then the other one is you can actually

**[01:12:18]** the other one is you can actually

**[01:12:18]** the other one is you can actually mention specific tools. So if you go in

**[01:12:20]** mention specific tools. So if you go in

**[01:12:20]** mention specific tools. So if you go in here into add context and then you can

**[01:12:22]** here into add context and then you can

**[01:12:22]** here into add context and then you can actually point it to specific tools. So

**[01:12:24]** actually point it to specific tools. So

**[01:12:24]** actually point it to specific tools. So you're not doing like the look up things

**[01:12:27]** you're not doing like the look up things

**[01:12:27]** you're not doing like the look up things on GitHub and you try to find the right

**[01:12:29]** on GitHub and you try to find the right

**[01:12:29]** on GitHub and you try to find the right verbiage that it gets the right tool.

**[01:12:31]** verbiage that it gets the right tool.

**[01:12:31]** verbiage that it gets the right tool. You can just actually mention the tool

**[01:12:33]** You can just actually mention the tool

**[01:12:33]** You can just actually mention the tool of it should um for example resolve lab

**[01:12:36]** of it should um for example resolve lab

**[01:12:36]** of it should um for example resolve lab ID. So so you can just add these here

**[01:12:39]** ID. So so you can just add these here

**[01:12:39]** ID. So so you can just add these here and then it will be handed to the AI of

**[01:12:41]** and then it will be handed to the AI of

**[01:12:41]** and then it will be handed to the AI of like these are the tools the user wants

**[01:12:43]** like these are the tools the user wants

**[01:12:43]** like these are the tools the user wants to use.

**[01:12:49]** It's it's still

**[01:12:49]** It's it's still &gt;&gt; Yeah.

**[01:12:51]** &gt;&gt; Yeah. &gt;&gt; Right.

### [01:13:00 - 01:14:00]

**[01:13:02]** &gt;&gt; Yeah. &gt;&gt; Yes. Yes. Tool calling is inherently

**[01:13:04]** &gt;&gt; Yes. Yes. Tool calling is inherently

**[01:13:04]** &gt;&gt; Yes. Yes. Tool calling is inherently always even in this case we're telling

**[01:13:06]** always even in this case we're telling

**[01:13:06]** always even in this case we're telling the AI it should use it but it might not

**[01:13:08]** the AI it should use it but it might not

**[01:13:08]** the AI it should use it but it might not use it. Yeah.

**[01:13:23]** &gt;&gt; Yeah. &gt;&gt; Yeah. So, my timer is down to zero.

**[01:13:26]** &gt;&gt; Yeah. So, my timer is down to zero.

**[01:13:26]** &gt;&gt; Yeah. So, my timer is down to zero. Maybe just go back to the slides to wrap

**[01:13:28]** Maybe just go back to the slides to wrap

**[01:13:28]** Maybe just go back to the slides to wrap it up.

**[01:13:30]** it up.

**[01:13:30]** it up. &gt;&gt; There more, right? Um, wipe coding. So,

**[01:13:34]** &gt;&gt; There more, right? Um, wipe coding. So,

**[01:13:34]** &gt;&gt; There more, right? Um, wipe coding. So, we showed workspace instructions. We

**[01:13:36]** we showed workspace instructions. We

**[01:13:36]** we showed workspace instructions. We showed dynamic instructions which only

**[01:13:38]** showed dynamic instructions which only

**[01:13:38]** showed dynamic instructions which only applied to parts of the tool set. Uh we

**[01:13:42]** applied to parts of the tool set. Uh we

**[01:13:42]** applied to parts of the tool set. Uh we showed custom tools playrite deep

**[01:13:45]** showed custom tools playrite deep

**[01:13:45]** showed custom tools playrite deep research. Uh I haven't showed using web

**[01:13:48]** research. Uh I haven't showed using web

**[01:13:48]** research. Uh I haven't showed using web docs like actually one of my favorites

**[01:13:49]** docs like actually one of my favorites

**[01:13:49]** docs like actually one of my favorites just point it to an existing repo and

**[01:13:51]** just point it to an existing repo and

**[01:13:51]** just point it to an existing repo and say read this repo if you have

**[01:13:53]** say read this repo if you have

**[01:13:53]** say read this repo if you have questions. MCP works great for that.

**[01:13:55]** questions. MCP works great for that.

**[01:13:55]** questions. MCP works great for that. When I work on MCP server I just tell it

**[01:13:57]** When I work on MCP server I just tell it

**[01:13:57]** When I work on MCP server I just tell it look in the TypeScript SDK server from

**[01:13:59]** look in the TypeScript SDK server from

**[01:13:59]** look in the TypeScript SDK server from the context protocol if you have

### [01:14:00 - 01:15:00]

**[01:14:00]** the context protocol if you have

**[01:14:00]** the context protocol if you have questions. Because we have cross repo

**[01:14:02]** questions. Because we have cross repo

**[01:14:02]** questions. Because we have cross repo search it just works. Um the agent

**[01:14:06]** search it just works. Um the agent

**[01:14:06]** search it just works. Um the agent actually has access to problems and

**[01:14:07]** actually has access to problems and

**[01:14:07]** actually has access to problems and tasks. So if you have tasks set up and

**[01:14:09]** tasks. So if you have tasks set up and

**[01:14:09]** tasks. So if you have tasks set up and you have linting set up, things will

**[01:14:11]** you have linting set up, things will

**[01:14:11]** you have linting set up, things will just work. So make sure those are set up

**[01:14:13]** just work. So make sure those are set up

**[01:14:13]** just work. So make sure those are set up in your template. Um generate commits I

**[01:14:16]** in your template. Um generate commits I

**[01:14:16]** in your template. Um generate commits I showed. And then fine grain review, you

**[01:14:18]** showed. And then fine grain review, you

**[01:14:18]** showed. And then fine grain review, you can pause at any time. If it asks you

**[01:14:20]** can pause at any time. If it asks you

**[01:14:20]** can pause at any time. If it asks you questions, you can always type something

**[01:14:22]** questions, you can always type something

**[01:14:22]** questions, you can always type something in and keep steering it into right

**[01:14:24]** in and keep steering it into right

**[01:14:24]** in and keep steering it into right direction. And you can trust read only

**[01:14:27]** direction. And you can trust read only

**[01:14:27]** direction. And you can trust read only in specific tools. And I showed you also

**[01:14:29]** in specific tools. And I showed you also

**[01:14:29]** in specific tools. And I showed you also editing.

**[01:14:31]** editing.

**[01:14:31]** editing. So

**[01:14:33]** So

**[01:14:33]** So yeah, uh instructions keep refining them

**[01:14:35]** yeah, uh instructions keep refining them

**[01:14:35]** yeah, uh instructions keep refining them as it makes mistakes. One of the key

**[01:14:37]** as it makes mistakes. One of the key

**[01:14:37]** as it makes mistakes. One of the key ones is commit often. I didn't show

**[01:14:39]** ones is commit often. I didn't show

**[01:14:39]** ones is commit often. I didn't show commits now, but anytime you have a

**[01:14:41]** commits now, but anytime you have a

**[01:14:41]** commits now, but anytime you have a working state, just make sure you commit

**[01:14:43]** working state, just make sure you commit

**[01:14:43]** working state, just make sure you commit it so AI can continue making mistakes

**[01:14:45]** it so AI can continue making mistakes

**[01:14:45]** it so AI can continue making mistakes and be creative. And then last one,

**[01:14:48]** and be creative. And then last one,

**[01:14:48]** and be creative. And then last one, there's a clear pause button in the

**[01:14:50]** there's a clear pause button in the

**[01:14:50]** there's a clear pause button in the lower end. So if AI goes off and you're

**[01:14:52]** lower end. So if AI goes off and you're

**[01:14:52]** lower end. So if AI goes off and you're like, what is it doing? Like is it just

**[01:14:54]** like, what is it doing? Like is it just

**[01:14:54]** like, what is it doing? Like is it just doing the right thing? Just just pause

**[01:14:55]** doing the right thing? Just just pause

**[01:14:55]** doing the right thing? Just just pause and review. And that's possible as well.

**[01:14:59]** and review. And that's possible as well.

**[01:14:59]** and review. And that's possible as well. Uh I showed a bunch of this for spectrum

### [01:15:00 - 01:16:00]

**[01:15:00]** Uh I showed a bunch of this for spectrum

**[01:15:00]** Uh I showed a bunch of this for spectrum development already but it's really

**[01:15:02]** development already but it's really

**[01:15:02]** development already but it's really about having a spec having having a like

**[01:15:04]** about having a spec having having a like

**[01:15:04]** about having a spec having having a like done a plan and doing more custom

**[01:15:06]** done a plan and doing more custom

**[01:15:06]** done a plan and doing more custom prompts and tools which I showed

**[01:15:09]** prompts and tools which I showed

**[01:15:09]** prompts and tools which I showed um showed us prompts. Um there's more

**[01:15:13]** um showed us prompts. Um there's more

**[01:15:13]** um showed us prompts. Um there's more MCPS for database access and logging and

**[01:15:16]** MCPS for database access and logging and

**[01:15:16]** MCPS for database access and logging and project tracking like the GitHub MCP

**[01:15:19]** project tracking like the GitHub MCP

**[01:15:19]** project tracking like the GitHub MCP and there's also access to actually

**[01:15:21]** and there's also access to actually

**[01:15:21]** and there's also access to actually tests and do debugging within the agent

**[01:15:23]** tests and do debugging within the agent

**[01:15:23]** tests and do debugging within the agent as well. So if you ask it to test driven

**[01:15:25]** as well. So if you ask it to test driven

**[01:15:25]** as well. So if you ask it to test driven development like we did, it will

**[01:15:26]** development like we did, it will

**[01:15:26]** development like we did, it will actually start running the tests if

**[01:15:27]** actually start running the tests if

**[01:15:28]** actually start running the tests if they're set up in VS code correctly. And

**[01:15:30]** they're set up in VS code correctly. And

**[01:15:30]** they're set up in VS code correctly. And then we talked briefly about models as

**[01:15:31]** then we talked briefly about models as

**[01:15:31]** then we talked briefly about models as well. So if you want to use 03 for any

**[01:15:34]** well. So if you want to use 03 for any

**[01:15:34]** well. So if you want to use 03 for any of the cool stuff, the the deeper

**[01:15:36]** of the cool stuff, the the deeper

**[01:15:36]** of the cool stuff, the the deeper thinking, you can do that as well.

**[01:15:39]** thinking, you can do that as well.

**[01:15:39]** thinking, you can do that as well. Um

**[01:15:40]** Um

**[01:15:40]** Um specri is really about focusing on the

**[01:15:43]** specri is really about focusing on the

**[01:15:43]** specri is really about focusing on the spec and I think a great way to do that

**[01:15:46]** spec and I think a great way to do that

**[01:15:46]** spec and I think a great way to do that is just create the spec from all the

**[01:15:49]** is just create the spec from all the

**[01:15:49]** is just create the spec from all the conversations you had about the spec.

**[01:15:51]** conversations you had about the spec.

**[01:15:51]** conversations you had about the spec. So, one way if you have a transcript

**[01:15:53]** So, one way if you have a transcript

**[01:15:53]** So, one way if you have a transcript from a meeting about the project you

**[01:15:55]** from a meeting about the project you

**[01:15:55]** from a meeting about the project you want to do, just feed that in and make

**[01:15:57]** want to do, just feed that in and make

**[01:15:57]** want to do, just feed that in and make sure you call out what the final

**[01:15:58]** sure you call out what the final

**[01:15:58]** sure you call out what the final decision is. It's a great way to have

### [01:16:00 - 01:17:00]

**[01:16:00]** decision is. It's a great way to have

**[01:16:00]** decision is. It's a great way to have meetings, but it's also a great way to

**[01:16:02]** meetings, but it's also a great way to

**[01:16:02]** meetings, but it's also a great way to not write the spec yourself in the end.

**[01:16:05]** not write the spec yourself in the end.

**[01:16:05]** not write the spec yourself in the end. Are there any tools to determine whether

**[01:16:07]** Are there any tools to determine whether

**[01:16:07]** Are there any tools to determine whether spec

**[01:16:28]** and say what are things missing and how

**[01:16:28]** and say what are things missing and how could it be better and stuff like that

**[01:16:30]** could it be better and stuff like that

**[01:16:30]** could it be better and stuff like that and we basically argued with about

**[01:16:35]** and we basically argued with about

**[01:16:35]** and we basically argued with about Yes, arguing with AI is one great way.

**[01:16:37]** Yes, arguing with AI is one great way.

**[01:16:38]** Yes, arguing with AI is one great way. So if I I have focus on one run prompt

**[01:16:40]** So if I I have focus on one run prompt

**[01:16:40]** So if I I have focus on one run prompt um or prompt

**[01:16:42]** um or prompt

**[01:16:42]** um or prompt is where's one critique idea is one I

**[01:16:45]** is where's one critique idea is one I

**[01:16:45]** is where's one critique idea is one I like of just ask me three questions

**[01:16:47]** like of just ask me three questions

**[01:16:47]** like of just ask me three questions about my idea right just have AI go into

**[01:16:50]** about my idea right just have AI go into

**[01:16:50]** about my idea right just have AI go into thinking mode like what would you ask

**[01:16:52]** thinking mode like what would you ask

**[01:16:52]** thinking mode like what would you ask somebody for feedback

**[01:16:54]** somebody for feedback

**[01:16:54]** somebody for feedback um and

**[01:16:57]** um and

**[01:16:57]** um and have it critically analyze your stuff.

**[01:16:59]** have it critically analyze your stuff.

**[01:16:59]** have it critically analyze your stuff. So these prompts like those are

### [01:17:00 - 01:18:00]

**[01:17:01]** So these prompts like those are

**[01:17:01]** So these prompts like those are basically the next level of prom

**[01:17:02]** basically the next level of prom

**[01:17:02]** basically the next level of prom crafting where you don't just ask it to

**[01:17:03]** crafting where you don't just ask it to

**[01:17:03]** crafting where you don't just ask it to code but pull it in as a thought partner

**[01:17:06]** code but pull it in as a thought partner

**[01:17:06]** code but pull it in as a thought partner as a design partner as somebody who can

**[01:17:08]** as a design partner as somebody who can

**[01:17:08]** as a design partner as somebody who can poke um holes in your I

**[01:17:13]** poke um holes in your I

**[01:17:13]** poke um holes in your I so

**[01:17:15]** so

**[01:17:15]** so yeah um front view steps is yeah

**[01:17:23]** &gt;&gt; a plan you you now can create one. So we

**[01:17:23]** &gt;&gt; a plan you you now can create one. So we have don't have a plan mode built in but

**[01:17:25]** have don't have a plan mode built in but

**[01:17:25]** have don't have a plan mode built in but we also know askedit agent will not be

**[01:17:27]** we also know askedit agent will not be

**[01:17:27]** we also know askedit agent will not be there forever. So it's it's a like

**[01:17:30]** there forever. So it's it's a like

**[01:17:30]** there forever. So it's it's a like series of evolutions. RU has way more

**[01:17:32]** series of evolutions. RU has way more

**[01:17:32]** series of evolutions. RU has way more modes that you can customize. So I think

**[01:17:34]** modes that you can customize. So I think

**[01:17:34]** modes that you can customize. So I think we want to allow developers to create

**[01:17:36]** we want to allow developers to create

**[01:17:36]** we want to allow developers to create their own. Um because I even see very

**[01:17:39]** their own. Um because I even see very

**[01:17:39]** their own. Um because I even see very few demos of people in client using

**[01:17:41]** few demos of people in client using

**[01:17:41]** few demos of people in client using plan. They just give it a thing and then

**[01:17:43]** plan. They just give it a thing and then

**[01:17:43]** plan. They just give it a thing and then it runs right.

**[01:17:53]** &gt;&gt; Yeah. &gt;&gt; It is. Yeah. I mean planning in in VIP

**[01:17:55]** &gt;&gt; It is. Yeah. I mean planning in in VIP

**[01:17:55]** &gt;&gt; It is. Yeah. I mean planning in in VIP coding you even do planning and then

**[01:17:57]** coding you even do planning and then

**[01:17:57]** coding you even do planning and then writing the implementation plan. So you

**[01:17:59]** writing the implementation plan. So you

**[01:17:59]** writing the implementation plan. So you would spend way more time on that

### [01:18:00 - 01:19:00]

**[01:18:00]** would spend way more time on that

**[01:18:00]** would spend way more time on that initial just what and how we're doing

**[01:18:04]** initial just what and how we're doing

**[01:18:04]** initial just what and how we're doing things and then you let it implement. So

**[01:18:06]** things and then you let it implement. So

**[01:18:06]** things and then you let it implement. So that would be even plan

**[01:18:08]** that would be even plan

**[01:18:08]** that would be even plan write the implementation plan or like

**[01:18:10]** write the implementation plan or like

**[01:18:10]** write the implementation plan or like write the spec write the plan and then

**[01:18:12]** write the spec write the plan and then

**[01:18:12]** write the spec write the plan and then implement. So you would even have three

**[01:18:13]** implement. So you would even have three

**[01:18:13]** implement. So you would even have three modes if you do it correctly and then

**[01:18:16]** modes if you do it correctly and then

**[01:18:16]** modes if you do it correctly and then yeah so that's probably the last one. So

**[01:18:19]** yeah so that's probably the last one. So

**[01:18:19]** yeah so that's probably the last one. So takeaways, you got to experiment. You

**[01:18:21]** takeaways, you got to experiment. You

**[01:18:21]** takeaways, you got to experiment. You got to figure out what works for you.

**[01:18:23]** got to figure out what works for you.

**[01:18:23]** got to figure out what works for you. Like at what point can you just give it

**[01:18:24]** Like at what point can you just give it

**[01:18:24]** Like at what point can you just give it a task and it runs with it? At what

**[01:18:26]** a task and it runs with it? At what

**[01:18:26]** a task and it runs with it? At what point do you want to give it a task and

**[01:18:28]** point do you want to give it a task and

**[01:18:28]** point do you want to give it a task and write a spec first and then implement um

**[01:18:31]** write a spec first and then implement um

**[01:18:31]** write a spec first and then implement um keep giving it feedback and iterate. So

**[01:18:33]** keep giving it feedback and iterate. So

**[01:18:33]** keep giving it feedback and iterate. So never just accept a bad answer and then

**[01:18:35]** never just accept a bad answer and then

**[01:18:36]** never just accept a bad answer and then really work on your process like what

**[01:18:37]** really work on your process like what

**[01:18:37]** really work on your process like what what works best for you, what works best

**[01:18:39]** what works best for you, what works best

**[01:18:39]** what works best for you, what works best for your team and use modes and prompts

**[01:18:41]** for your team and use modes and prompts

**[01:18:41]** for your team and use modes and prompts and instructions to ingrain that.

**[01:18:45]** and instructions to ingrain that.

**[01:18:45]** and instructions to ingrain that. Um there's some bonus mistakes you can

**[01:18:47]** Um there's some bonus mistakes you can

**[01:18:47]** Um there's some bonus mistakes you can screenshot.

**[01:18:50]** screenshot.

**[01:18:50]** screenshot. &gt;&gt; Yes, please. One more. There's one more.

**[01:18:52]** &gt;&gt; Yes, please. One more. There's one more.

**[01:18:52]** &gt;&gt; Yes, please. One more. There's one more. One more screenshot.

**[01:18:54]** One more screenshot.

**[01:18:54]** One more screenshot. &gt;&gt; You can end up like major modes. You can

**[01:18:57]** &gt;&gt; You can end up like major modes. You can

**[01:18:57]** &gt;&gt; You can end up like major modes. You can have multiple minor modes.

**[01:18:58]** have multiple minor modes.

**[01:18:58]** have multiple minor modes. &gt;&gt; Minor modes. Yes. That's kind how you

**[01:18:59]** &gt;&gt; Minor modes. Yes. That's kind how you

**[01:18:59]** &gt;&gt; Minor modes. Yes. That's kind how you end up with problems in custom modes

### [01:19:00 - 01:20:00]

**[01:19:00]** end up with problems in custom modes

**[01:19:00]** end up with problems in custom modes right now. So I got to clean this up

**[01:19:02]** right now. So I got to clean this up

**[01:19:02]** right now. So I got to clean this up too. And then yeah, lastly

**[01:19:05]** too. And then yeah, lastly

**[01:19:05]** too. And then yeah, lastly there is there is a sweet spot for how

**[01:19:06]** there is there is a sweet spot for how

**[01:19:06]** there is there is a sweet spot for how you define your code bases for AI. So

**[01:19:09]** you define your code bases for AI. So

**[01:19:09]** you define your code bases for AI. So you want to have well structured

**[01:19:11]** you want to have well structured

**[01:19:11]** you want to have well structured self-explaining code. want to have the

**[01:19:13]** self-explaining code. want to have the

**[01:19:13]** self-explaining code. want to have the instructions set up. Want to have

**[01:19:14]** instructions set up. Want to have

**[01:19:14]** instructions set up. Want to have examples in your instructions. I want to

**[01:19:17]** examples in your instructions. I want to

**[01:19:17]** examples in your instructions. I want to keep instructions updated. So that's it.

**[01:19:23]** keep instructions updated. So that's it.

**[01:19:23]** keep instructions updated. So that's it. That was my unplanned workshop. Thank

**[01:19:24]** That was my unplanned workshop. Thank

**[01:19:24]** That was my unplanned workshop. Thank you for coming.

**[01:19:26]** you for coming.

**[01:19:26]** you for coming. [Music]

