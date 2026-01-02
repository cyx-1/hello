# Developing Taste in Coding Agents- Applied Meta Neuro-Symbolic RL — Ahmad Awais, CommandCode

**Video URL:** https://www.youtube.com/watch?v=kWOQS3XPZ10

---

## Full Transcript

### [00:00 - 01:00]

**[00:02]** Well, hello there. Today I am really,

**[00:02]** Well, hello there. Today I am really, really excited to both launch and share

**[00:05]** really excited to both launch and share

**[00:05]** really excited to both launch and share with you what we have been working on

**[00:06]** with you what we have been working on

**[00:06]** with you what we have been working on for maybe over an year now. It's called

**[00:09]** for maybe over an year now. It's called

**[00:09]** for maybe over an year now. It's called Command Code, a coding agent with taste.

**[00:11]** Command Code, a coding agent with taste.

**[00:11]** Command Code, a coding agent with taste. So, who am I? Um, I am Ahmed, creator of

**[00:14]** So, who am I? Um, I am Ahmed, creator of

**[00:14]** So, who am I? Um, I am Ahmed, creator of Command Code, CEO and founder of

**[00:17]** Command Code, CEO and founder of

**[00:17]** Command Code, CEO and founder of Langbase. Um, I've been around this blog

**[00:19]** Langbase. Um, I've been around this blog

**[00:19]** Langbase. Um, I've been around this blog for I don't know like 20 years building

**[00:22]** for I don't know like 20 years building

**[00:22]** for I don't know like 20 years building one thing after another. I've written

**[00:24]** one thing after another. I've written

**[00:24]** one thing after another. I've written hundreds of open source packages with

**[00:26]** hundreds of open source packages with

**[00:26]** hundreds of open source packages with millions of downloads. Maybe you like my

**[00:28]** millions of downloads. Maybe you like my

**[00:28]** millions of downloads. Maybe you like my shades of purple code theme. I love the

**[00:29]** shades of purple code theme. I love the

**[00:30]** shades of purple code theme. I love the color purple and I I've I'm I'm an

**[00:32]** color purple and I I've I'm I'm an

**[00:32]** color purple and I I've I'm I'm an engineer at the end of the day. I write

**[00:34]** engineer at the end of the day. I write

**[00:34]** engineer at the end of the day. I write a lot of code and I've been building in

**[00:36]** a lot of code and I've been building in

**[00:36]** a lot of code and I've been building in the LLM space for about five years now.

**[00:39]** the LLM space for about five years now.

**[00:39]** the LLM space for about five years now. Um and I think the one of the first

**[00:41]** Um and I think the one of the first

**[00:41]** Um and I think the one of the first tools that I actually ended up building

**[00:42]** tools that I actually ended up building

**[00:42]** tools that I actually ended up building was a coding agent and at the end of the

**[00:45]** was a coding agent and at the end of the

**[00:45]** was a coding agent and at the end of the day like I'm very technical. I got to

**[00:47]** day like I'm very technical. I got to

**[00:47]** day like I'm very technical. I got to contribute to the NASA Mars Engineer

**[00:49]** contribute to the NASA Mars Engineer

**[00:49]** contribute to the NASA Mars Engineer helicopter mission. My code lives on

**[00:50]** helicopter mission. My code lives on

**[00:50]** helicopter mission. My code lives on Mars. So when I'm writing code, no

**[00:54]** Mars. So when I'm writing code, no

**[00:54]** Mars. So when I'm writing code, no matter what LLM or what coding agent I'm

**[00:56]** matter what LLM or what coding agent I'm

**[00:56]** matter what LLM or what coding agent I'm using, I want it to learn from me. I

**[00:59]** using, I want it to learn from me. I

**[00:59]** using, I want it to learn from me. I want to I wanted to learn that how I am


### [01:00 - 02:00]

**[01:01]** want to I wanted to learn that how I am

**[01:01]** want to I wanted to learn that how I am editing its code. I wanted to understand

**[01:04]** editing its code. I wanted to understand

**[01:04]** editing its code. I wanted to understand my preferences and continuously adopt to

**[01:07]** my preferences and continuously adopt to

**[01:07]** my preferences and continuously adopt to that uh you know preference set in

**[01:09]** that uh you know preference set in

**[01:09]** that uh you know preference set in invisible architecture of choices that I

**[01:11]** invisible architecture of choices that I

**[01:11]** invisible architecture of choices that I have and that is what I'm excited to

**[01:13]** have and that is what I'm excited to

**[01:13]** have and that is what I'm excited to demo today. Right? So uh the story

**[01:16]** demo today. Right? So uh the story

**[01:16]** demo today. Right? So uh the story actually begins in 2020 uh when Greg

**[01:19]** actually begins in 2020 uh when Greg

**[01:19]** actually begins in 2020 uh when Greg Brookkeman gives me access to GP3 and I

**[01:21]** Brookkeman gives me access to GP3 and I

**[01:22]** Brookkeman gives me access to GP3 and I tell him like the one of the first

**[01:23]** tell him like the one of the first

**[01:23]** tell him like the one of the first things this is like three years before

**[01:25]** things this is like three years before

**[01:25]** things this is like three years before chat GPD and a year before uh you know

**[01:27]** chat GPD and a year before uh you know

**[01:27]** chat GPD and a year before uh you know GitHub copilot I tell him that I want to

**[01:29]** GitHub copilot I tell him that I want to

**[01:29]** GitHub copilot I tell him that I want to build something with GP3 that suggests

**[01:32]** build something with GP3 that suggests

**[01:32]** build something with GP3 that suggests suggests the next line of code right so

**[01:34]** suggests the next line of code right so

**[01:34]** suggests the next line of code right so let's jump into a demo right away right

**[01:36]** let's jump into a demo right away right

**[01:36]** let's jump into a demo right away right let's let's look at what this actually

**[01:38]** let's let's look at what this actually

**[01:38]** let's let's look at what this actually looks like and then I'll I'll probably

**[01:40]** looks like and then I'll I'll probably

**[01:40]** looks like and then I'll I'll probably explain you know how we ended up here

**[01:43]** explain you know how we ended up here

**[01:44]** explain you know how we ended up here so on On the left here you see uh you

**[01:46]** so on On the left here you see uh you

**[01:46]** so on On the left here you see uh you know cloud code and this is command code

**[01:49]** know cloud code and this is command code

**[01:49]** know cloud code and this is command code right this is what we are building as

**[01:50]** right this is what we are building as

**[01:50]** right this is what we are building as you can see it is continuously learning

**[01:52]** you can see it is continuously learning

**[01:52]** you can see it is continuously learning taste is on this is what we call it and

**[01:55]** taste is on this is what we call it and

**[01:55]** taste is on this is what we call it and uh I've been building a lot of CLI as

**[01:58]** uh I've been building a lot of CLI as

**[01:58]** uh I've been building a lot of CLI as you know like you know if you know

**[01:59]** you know like you know if you know

**[01:59]** you know like you know if you know anything about me you know that I'm all


### [02:00 - 03:00]

**[02:00]** anything about me you know that I'm all

**[02:00]** anything about me you know that I'm all about automation and I have been

**[02:02]** about automation and I have been

**[02:02]** about automation and I have been building a lot of you know CLI over the

**[02:05]** building a lot of you know CLI over the

**[02:05]** building a lot of you know CLI over the course of my career so let's uh build a

**[02:08]** course of my career so let's uh build a

**[02:08]** course of my career so let's uh build a CLI and command here actually knows how

**[02:11]** CLI and command here actually knows how

**[02:11]** CLI and command here actually knows how I built a CLI yesterday right or before

**[02:14]** I built a CLI yesterday right or before

**[02:14]** I built a CLI yesterday right or before that it kind of understands my

**[02:16]** that it kind of understands my

**[02:16]** that it kind of understands my preferences of building a CLI. So let's

**[02:18]** preferences of building a CLI. So let's

**[02:18]** preferences of building a CLI. So let's give both of them uh this thing right uh

**[02:22]** give both of them uh this thing right uh

**[02:22]** give both of them uh this thing right uh make me a CLI that can tell date in ISO

**[02:28]** make me a CLI that can tell date in ISO

**[02:28]** make me a CLI that can tell date in ISO format

**[02:30]** format

**[02:30]** format right so look at what is happening here

**[02:32]** right so look at what is happening here

**[02:32]** right so look at what is happening here so one of the first things that happen

**[02:34]** so one of the first things that happen

**[02:34]** so one of the first things that happen here is uh command kind of picks up on

**[02:37]** here is uh command kind of picks up on

**[02:37]** here is uh command kind of picks up on my test file and I'm I'm going to share

**[02:40]** my test file and I'm I'm going to share

**[02:40]** my test file and I'm I'm going to share a little bit more about it but you see

**[02:42]** a little bit more about it but you see

**[02:42]** a little bit more about it but you see what is happening here and I'm going to

**[02:43]** what is happening here and I'm going to

**[02:44]** what is happening here and I'm going to probably you know enable all these

**[02:45]** probably you know enable all these

**[02:45]** probably you know enable all these settings so let's give both of these

**[02:48]** settings so let's give both of these

**[02:48]** settings so let's give both of these coding agents

**[02:50]** coding agents

**[02:50]** coding agents uh you know a steps on and you can see

**[02:53]** uh you know a steps on and you can see

**[02:53]** uh you know a steps on and you can see what command is doing it's it's using

**[02:55]** what command is doing it's it's using

**[02:55]** what command is doing it's it's using t-up it's using uh typescript and it's

**[02:59]** t-up it's using uh typescript and it's

**[02:59]** t-up it's using uh typescript and it's uh building an ASI art you know banner


### [03:00 - 04:00]

**[03:02]** uh building an ASI art you know banner

**[03:02]** uh building an ASI art you know banner it's npm linking uh it's going to help

**[03:04]** it's npm linking uh it's going to help

**[03:04]** it's npm linking uh it's going to help LPM link this particular CLI as well and

**[03:07]** LPM link this particular CLI as well and

**[03:07]** LPM link this particular CLI as well and the these are all the things that I kind

**[03:08]** the these are all the things that I kind

**[03:08]** the these are all the things that I kind of care about and while cloud has done

**[03:11]** of care about and while cloud has done

**[03:11]** of care about and while cloud has done something really good it it's very fast

**[03:13]** something really good it it's very fast

**[03:13]** something really good it it's very fast but h I don't know man this is not what

**[03:16]** but h I don't know man this is not what

**[03:16]** but h I don't know man this is not what I wanted it's like a console log of uh

**[03:18]** I wanted it's like a console log of uh

**[03:18]** I wanted it's like a console log of uh uh this or that like I I I I I when I

**[03:21]** uh this or that like I I I I I when I

**[03:21]** uh this or that like I I I I I when I build a CLI, I don't want to build a

**[03:23]** build a CLI, I don't want to build a

**[03:23]** build a CLI, I don't want to build a CLI, you know, a CLI like this. I I want

**[03:25]** CLI, you know, a CLI like this. I I want

**[03:25]** CLI, you know, a CLI like this. I I want to build something like, you know,

**[03:27]** to build something like, you know,

**[03:27]** to build something like, you know, please uh use uh Typescript and I want

**[03:31]** please uh use uh Typescript and I want

**[03:31]** please uh use uh Typescript and I want TUP, right? Um and what else? I want uh

**[03:36]** TUP, right? Um and what else? I want uh

**[03:36]** TUP, right? Um and what else? I want uh Commander because I like to uh you know

**[03:39]** Commander because I like to uh you know

**[03:39]** Commander because I like to uh you know have more control over my CLIs. And what

**[03:42]** have more control over my CLIs. And what

**[03:42]** have more control over my CLIs. And what else? I want a lowercase

**[03:46]** else? I want a lowercase

**[03:46]** else? I want a lowercase uh version number uh with hyphen v

**[03:51]** uh version number uh with hyphen v

**[03:51]** uh version number uh with hyphen v because I know you know commander does

**[03:52]** because I know you know commander does

**[03:52]** because I know you know commander does this hyphen capital v thing like I have

**[03:54]** this hyphen capital v thing like I have

**[03:54]** this hyphen capital v thing like I have so many preferences here and by this

**[03:57]** so many preferences here and by this

**[03:57]** so many preferences here and by this time uh command has already done what I


### [04:00 - 05:00]

**[04:00]** time uh command has already done what I

**[04:00]** time uh command has already done what I wanted it to do. How about we actually

**[04:02]** wanted it to do. How about we actually

**[04:02]** wanted it to do. How about we actually jump uh into code and see you know what

**[04:05]** jump uh into code and see you know what

**[04:05]** jump uh into code and see you know what it has actually done right let let's

**[04:06]** it has actually done right let let's

**[04:06]** it has actually done right let let's let's open this up into VS code

**[04:15]** and this is what command did for me

**[04:15]** and this is what command did for me right so it is using tap it is using

**[04:17]** right so it is using tap it is using

**[04:17]** right so it is using tap it is using typescript it knows pmppn uh that I

**[04:20]** typescript it knows pmppn uh that I

**[04:20]** typescript it knows pmppn uh that I prefer pnpm uh I completely forgot to

**[04:22]** prefer pnpm uh I completely forgot to

**[04:22]** prefer pnpm uh I completely forgot to tell that to uh claude and if we go into

**[04:26]** tell that to uh claude and if we go into

**[04:26]** tell that to uh claude and if we go into this particular uh CLI here uh you can

**[04:29]** this particular uh CLI here uh you can

**[04:29]** this particular uh CLI here uh you can see what it is kind kind of doing right

**[04:31]** see what it is kind kind of doing right

**[04:31]** see what it is kind kind of doing right like it is using hyphen v uh for version

**[04:35]** like it is using hyphen v uh for version

**[04:35]** like it is using hyphen v uh for version it is not like hard coding a package

**[04:38]** it is not like hard coding a package

**[04:38]** it is not like hard coding a package version in here and one more thing it

**[04:40]** version in here and one more thing it

**[04:40]** version in here and one more thing it should have picked up is like I want all

**[04:42]** should have picked up is like I want all

**[04:42]** should have picked up is like I want all of these commands to be in separate

**[04:44]** of these commands to be in separate

**[04:44]** of these commands to be in separate directory called commands so there you

**[04:46]** directory called commands so there you

**[04:46]** directory called commands so there you go the date command is here so when I

**[04:48]** go the date command is here so when I

**[04:48]** go the date command is here so when I grow this CLI into like you know tell me

**[04:50]** grow this CLI into like you know tell me

**[04:50]** grow this CLI into like you know tell me human date or whatnot it is going to put

**[04:52]** human date or whatnot it is going to put

**[04:52]** human date or whatnot it is going to put all of these commands here it's very

**[04:53]** all of these commands here it's very

**[04:54]** all of these commands here it's very very easy to test that way I wonder if

**[04:56]** very easy to test that way I wonder if

**[04:56]** very easy to test that way I wonder if it is also using vitest there you go

**[04:57]** it is also using vitest there you go

**[04:57]** it is also using vitest there you go because I prefer Vest for uh you know


### [05:00 - 06:00]

**[05:00]** because I prefer Vest for uh you know

**[05:00]** because I prefer Vest for uh you know writing uh a lot of tests and one of the

**[05:02]** writing uh a lot of tests and one of the

**[05:02]** writing uh a lot of tests and one of the those things you know it it is using 0

**[05:04]** those things you know it it is using 0

**[05:04]** those things you know it it is using 0 0.0.1

**[05:06]** 0.0.1

**[05:06]** 0.0.1 version I like to start here instead of

**[05:08]** version I like to start here instead of

**[05:08]** version I like to start here instead of 1.0.0

**[05:10]** 1.0.0

**[05:10]** 1.0.0 right and that is probably not what you

**[05:13]** right and that is probably not what you

**[05:13]** right and that is probably not what you know uh uh claude was doing on this side

**[05:16]** know uh uh claude was doing on this side

**[05:16]** know uh uh claude was doing on this side right if I were to open the same uh CLI

**[05:19]** right if I were to open the same uh CLI

**[05:19]** right if I were to open the same uh CLI that claude built for me you will see

**[05:21]** that claude built for me you will see

**[05:21]** that claude built for me you will see that you know 1.0 O and it's like again

**[05:24]** that you know 1.0 O and it's like again

**[05:24]** that you know 1.0 O and it's like again not using vit like every single

**[05:26]** not using vit like every single

**[05:26]** not using vit like every single preference that I have it is probably

**[05:28]** preference that I have it is probably

**[05:28]** preference that I have it is probably not going to do that and then again this

**[05:30]** not going to do that and then again this

**[05:30]** not going to do that and then again this thing everything is here I don't want it

**[05:32]** thing everything is here I don't want it

**[05:32]** thing everything is here I don't want it like this uh this is kind of again it

**[05:36]** like this uh this is kind of again it

**[05:36]** like this uh this is kind of again it cla knows cloud is a is an amazing model

**[05:39]** cla knows cloud is a is an amazing model

**[05:39]** cla knows cloud is a is an amazing model but it knows what to do and with command

**[05:42]** but it knows what to do and with command

**[05:42]** but it knows what to do and with command right now we are also using cloud but

**[05:44]** right now we are also using cloud but

**[05:44]** right now we are also using cloud but it's it's kind of like I have to steer

**[05:45]** it's it's kind of like I have to steer

**[05:46]** it's it's kind of like I have to steer it so much that I kind of feel like it

**[05:48]** it so much that I kind of feel like it

**[05:48]** it so much that I kind of feel like it should be learning from me and by the

**[05:50]** should be learning from me and by the

**[05:50]** should be learning from me and by the way it's it is quite transparent And if

**[05:52]** way it's it is quite transparent And if

**[05:52]** way it's it is quite transparent And if you look at this, we have a command code

**[05:54]** you look at this, we have a command code

**[05:54]** you look at this, we have a command code folder in here. And if you see in here,

**[05:56]** folder in here. And if you see in here,

**[05:56]** folder in here. And if you see in here, there's a taste file. And if you go

**[05:58]** there's a taste file. And if you go

**[05:58]** there's a taste file. And if you go inside of it, there's a, you know, CLI


### [06:00 - 07:00]

**[06:00]** inside of it, there's a, you know, CLI

**[06:00]** inside of it, there's a, you know, CLI taste that it has picked up. And these

**[06:02]** taste that it has picked up. And these

**[06:02]** taste that it has picked up. And these are all my preferences. I can assure

**[06:05]** are all my preferences. I can assure

**[06:05]** are all my preferences. I can assure you, none of this is written by me. So

**[06:07]** you, none of this is written by me. So

**[06:07]** you, none of this is written by me. So command code is continuously learning

**[06:09]** command code is continuously learning

**[06:09]** command code is continuously learning from me and it is creating a lot of

**[06:12]** from me and it is creating a lot of

**[06:12]** from me and it is creating a lot of these taste like things. This is not

**[06:15]** these taste like things. This is not

**[06:15]** these taste like things. This is not spec. This is not scale. It's like my

**[06:17]** spec. This is not scale. It's like my

**[06:17]** spec. This is not scale. It's like my intuition uh built into a metaano

**[06:19]** intuition uh built into a metaano

**[06:19]** intuition uh built into a metaano symbolic uh model, an architecture model

**[06:22]** symbolic uh model, an architecture model

**[06:22]** symbolic uh model, an architecture model that is more deterministic that kind of

**[06:24]** that is more deterministic that kind of

**[06:24]** that is more deterministic that kind of figures out it's more like a reix of my

**[06:27]** figures out it's more like a reix of my

**[06:27]** figures out it's more like a reix of my preferences and it figures out like this

**[06:29]** preferences and it figures out like this

**[06:29]** preferences and it figures out like this is what I want when I'm using and

**[06:32]** is what I want when I'm using and

**[06:32]** is what I want when I'm using and building uh you know with uh writing

**[06:35]** building uh you know with uh writing

**[06:35]** building uh you know with uh writing with AI code or whatnot. So let's step

**[06:37]** with AI code or whatnot. So let's step

**[06:37]** with AI code or whatnot. So let's step back in and let's take a step back uh

**[06:39]** back in and let's take a step back uh

**[06:39]** back in and let's take a step back uh why and how we got here right and I'm

**[06:42]** why and how we got here right and I'm

**[06:42]** why and how we got here right and I'm going to share we are going to publish a

**[06:43]** going to share we are going to publish a

**[06:43]** going to share we are going to publish a paper about it as well. I'm going to uh

**[06:46]** paper about it as well. I'm going to uh

**[06:46]** paper about it as well. I'm going to uh share a little bit more about like where

**[06:47]** share a little bit more about like where

**[06:47]** share a little bit more about like where we are and how we are going to think

**[06:49]** we are and how we are going to think

**[06:50]** we are and how we are going to think about it, why this kind of matters and

**[06:52]** about it, why this kind of matters and

**[06:52]** about it, why this kind of matters and what is the architecture behind all of

**[06:53]** what is the architecture behind all of

**[06:54]** what is the architecture behind all of this. So again I started in 2020. Uh the

**[06:56]** this. So again I started in 2020. Uh the

**[06:56]** this. So again I started in 2020. Uh the first thing I built was a coding agent

**[06:58]** first thing I built was a coding agent

**[06:58]** first thing I built was a coding agent and that led to so many things. I ended


### [07:00 - 08:00]

**[07:00]** and that led to so many things. I ended

**[07:00]** and that led to so many things. I ended up building Langbase and we raised $5

**[07:03]** up building Langbase and we raised $5

**[07:03]** up building Langbase and we raised $5 million from all these amazing people.

**[07:05]** million from all these amazing people.

**[07:05]** million from all these amazing people. In fact, uh founder of GitHub uh led our

**[07:09]** In fact, uh founder of GitHub uh led our

**[07:09]** In fact, uh founder of GitHub uh led our uh round in you know founders of all

**[07:10]** uh round in you know founders of all

**[07:10]** uh round in you know founders of all these amazing company companies kind of

**[07:13]** these amazing company companies kind of

**[07:13]** these amazing company companies kind of supported uh you know our mission here

**[07:16]** supported uh you know our mission here

**[07:16]** supported uh you know our mission here and the idea that we were we were trying

**[07:18]** and the idea that we were we were trying

**[07:18]** and the idea that we were we were trying to fix was memory and this memory was

**[07:20]** to fix was memory and this memory was

**[07:20]** to fix was memory and this memory was not rag it was like a serverless rack

**[07:23]** not rag it was like a serverless rack

**[07:23]** not rag it was like a serverless rack store which can reason over your data

**[07:26]** store which can reason over your data

**[07:26]** store which can reason over your data reason over how to help you and

**[07:28]** reason over how to help you and

**[07:28]** reason over how to help you and continuously learn and we saw a lot of

**[07:31]** continuously learn and we saw a lot of

**[07:31]** continuously learn and we saw a lot of things like I think this is the biggest

**[07:33]** things like I think this is the biggest

**[07:33]** things like I think this is the biggest problem in AI I think the best thing

**[07:35]** problem in AI I think the best thing

**[07:35]** problem in AI I think the best thing that [laughter] AI has kind of learned

**[07:37]** that [laughter] AI has kind of learned

**[07:37]** that [laughter] AI has kind of learned from humans is that humans are lazy and

**[07:39]** from humans is that humans are lazy and

**[07:39]** from humans is that humans are lazy and that is what AI is. AI is lazy by

**[07:42]** that is what AI is. AI is lazy by

**[07:42]** that is what AI is. AI is lazy by default. It's very sloppy. If you ask

**[07:44]** default. It's very sloppy. If you ask

**[07:44]** default. It's very sloppy. If you ask for a you know horse on a staircase

**[07:46]** for a you know horse on a staircase

**[07:46]** for a you know horse on a staircase banister, this is kind of what you get

**[07:48]** banister, this is kind of what you get

**[07:48]** banister, this is kind of what you get and then you have to uh you know prompt

**[07:50]** and then you have to uh you know prompt

**[07:50]** and then you have to uh you know prompt it again and again and again to get to

**[07:51]** it again and again and again to get to

**[07:51]** it again and again and again to get to this left side of things. You know this

**[07:53]** this left side of things. You know this

**[07:53]** this left side of things. You know this is sort of what you saw me do with

**[07:55]** is sort of what you saw me do with

**[07:55]** is sort of what you saw me do with Claude when I was trying to build that

**[07:57]** Claude when I was trying to build that

**[07:57]** Claude when I was trying to build that CLI. Right? To fix this problem, we

**[07:59]** CLI. Right? To fix this problem, we

**[07:59]** CLI. Right? To fix this problem, we basically launched a bunch of


### [08:00 - 09:00]

**[08:01]** basically launched a bunch of

**[08:01]** basically launched a bunch of primitives. of threads, workflows,

**[08:02]** primitives. of threads, workflows,

**[08:02]** primitives. of threads, workflows, memory, what have you. And our hope was

**[08:05]** memory, what have you. And our hope was

**[08:05]** memory, what have you. And our hope was that people will start building amazing

**[08:07]** that people will start building amazing

**[08:07]** that people will start building amazing agents. And then we saw uh you know like

**[08:10]** agents. And then we saw uh you know like

**[08:10]** agents. And then we saw uh you know like we doing like I think 700 terabytes and

**[08:13]** we doing like I think 700 terabytes and

**[08:13]** we doing like I think 700 terabytes and 1.2 billion agent runs a month. So we

**[08:15]** 1.2 billion agent runs a month. So we

**[08:15]** 1.2 billion agent runs a month. So we saw major scale but we saw another

**[08:17]** saw major scale but we saw another

**[08:17]** saw major scale but we saw another problem. We we studied that problem and

**[08:19]** problem. We we studied that problem and

**[08:20]** problem. We we studied that problem and you can go to stateofiagents.com.

**[08:22]** you can go to stateofiagents.com.

**[08:22]** you can go to stateofiagents.com. You can study all of our uh research

**[08:24]** You can study all of our uh research

**[08:24]** You can study all of our uh research into how people were building agents.

**[08:26]** into how people were building agents.

**[08:26]** into how people were building agents. This is all public by the way. [snorts]

**[08:29]** This is all public by the way. [snorts]

**[08:29]** This is all public by the way. [snorts] And we figured out like even agents uh

**[08:32]** And we figured out like even agents uh

**[08:32]** And we figured out like even agents uh were very way very sloppy like you know

**[08:33]** were very way very sloppy like you know

**[08:33]** were very way very sloppy like you know I'm like I think like I I use AI for

**[08:36]** I'm like I think like I I use AI for

**[08:36]** I'm like I think like I I use AI for everything except for when I am writing

**[08:39]** everything except for when I am writing

**[08:39]** everything except for when I am writing right because every time I build an

**[08:41]** right because every time I build an

**[08:41]** right because every time I build an agent uh to write or every time I use an

**[08:44]** agent uh to write or every time I use an

**[08:44]** agent uh to write or every time I use an LLM to write something this sort of slob

**[08:48]** LLM to write something this sort of slob

**[08:48]** LLM to write something this sort of slob I kind of get back right so we have a

**[08:50]** I kind of get back right so we have a

**[08:50]** I kind of get back right so we have a collaborative dev tool can you write me

**[08:52]** collaborative dev tool can you write me

**[08:52]** collaborative dev tool can you write me a fun headline for it and what I'd get

**[08:55]** a fun headline for it and what I'd get

**[08:55]** a fun headline for it and what I'd get back is like power of synergistic

**[08:56]** back is like power of synergistic

**[08:56]** back is like power of synergistic teamwork or whatn not and this is my

**[08:58]** teamwork or whatn not and this is my

**[08:58]** teamwork or whatn not and this is my friend I actually saw him do this and he


### [09:00 - 10:00]

**[09:00]** friend I actually saw him do this and he

**[09:00]** friend I actually saw him do this and he was like, "Oh god, no. Please fix it."

**[09:01]** was like, "Oh god, no. Please fix it."

**[09:01]** was like, "Oh god, no. Please fix it." And it got even worse, right? Uh to fix

**[09:04]** And it got even worse, right? Uh to fix

**[09:04]** And it got even worse, right? Uh to fix this, we we tried this command. We

**[09:07]** this, we we tried this command. We

**[09:07]** this, we we tried this command. We launched it as chai. And rebranded to

**[09:09]** launched it as chai. And rebranded to

**[09:09]** launched it as chai. And rebranded to command new in last five months. This

**[09:12]** command new in last five months. This

**[09:12]** command new in last five months. This was an agent of agents. You would give

**[09:14]** was an agent of agents. You would give

**[09:14]** was an agent of agents. You would give it a prompt like this is the kind of

**[09:15]** it a prompt like this is the kind of

**[09:15]** it a prompt like this is the kind of agent I want to build. It will provision

**[09:17]** agent I want to build. It will provision

**[09:17]** agent I want to build. It will provision and create all of the infrastructure for

**[09:19]** and create all of the infrastructure for

**[09:19]** and create all of the infrastructure for you. And I shared a talk about it as

**[09:21]** you. And I shared a talk about it as

**[09:21]** you. And I shared a talk about it as well. In five months, we have seen

**[09:23]** well. In five months, we have seen

**[09:23]** well. In five months, we have seen 150,000 agents vip coded with it. But

**[09:26]** 150,000 agents vip coded with it. But

**[09:26]** 150,000 agents vip coded with it. But there's just something missing, right?

**[09:28]** there's just something missing, right?

**[09:28]** there's just something missing, right? Vibe coding I think is better than slob

**[09:30]** Vibe coding I think is better than slob

**[09:30]** Vibe coding I think is better than slob but it's not better than the rules and

**[09:33]** but it's not better than the rules and

**[09:33]** but it's not better than the rules and choices that I have made that I have

**[09:35]** choices that I have made that I have

**[09:35]** choices that I have made that I have kind of built my career around right so

**[09:38]** kind of built my career around right so

**[09:38]** kind of built my career around right so we started to fix this problem again and

**[09:41]** we started to fix this problem again and

**[09:41]** we started to fix this problem again and this is sort of again this is my five

**[09:43]** this is sort of again this is my five

**[09:43]** this is sort of again this is my five years of learning is around this I think

**[09:45]** years of learning is around this I think

**[09:46]** years of learning is around this I think by default AI is sloppy this is the

**[09:48]** by default AI is sloppy this is the

**[09:48]** by default AI is sloppy this is the default setting of almost every LLM

**[09:50]** default setting of almost every LLM

**[09:50]** default setting of almost every LLM they're trying to be correct and they're

**[09:52]** they're trying to be correct and they're

**[09:52]** they're trying to be correct and they're trying to be correct as soon as possible

**[09:55]** trying to be correct as soon as possible

**[09:55]** trying to be correct as soon as possible that I think doesn't really work with

**[09:57]** that I think doesn't really work with

**[09:57]** that I think doesn't really work with code and then we get this vibe coding


### [10:00 - 11:00]

**[10:00]** code and then we get this vibe coding

**[10:00]** code and then we get this vibe coding thing where somebody does the context

**[10:02]** thing where somebody does the context

**[10:02]** thing where somebody does the context engineering you know everybody has a

**[10:04]** engineering you know everybody has a

**[10:04]** engineering you know everybody has a different name for it you know uh behind

**[10:06]** different name for it you know uh behind

**[10:06]** different name for it you know uh behind the scene it's context engineering

**[10:07]** the scene it's context engineering

**[10:08]** the scene it's context engineering memory and a bunch of prompts and you

**[10:10]** memory and a bunch of prompts and you

**[10:10]** memory and a bunch of prompts and you know you most of the times you don't

**[10:12]** know you most of the times you don't

**[10:12]** know you most of the times you don't really have a lot of control over it and

**[10:14]** really have a lot of control over it and

**[10:14]** really have a lot of control over it and to seek that control what a lot of

**[10:15]** to seek that control what a lot of

**[10:15]** to seek that control what a lot of developers do is they they start writing

**[10:17]** developers do is they they start writing

**[10:17]** developers do is they they start writing these rules files like cloudmd

**[10:20]** these rules files like cloudmd

**[10:20]** these rules files like cloudmd agents.mmd and rules are never enough I

**[10:23]** agents.mmd and rules are never enough I

**[10:23]** agents.mmd and rules are never enough I I I often tell I often joke about this

**[10:27]** I I often tell I often joke about this

**[10:27]** I I often tell I often joke about this that our justice system sucks because

**[10:29]** that our justice system sucks because

**[10:29]** that our justice system sucks because our rules are not enough and then we

**[10:31]** our rules are not enough and then we

**[10:31]** our rules are not enough and then we have to go out with this human lawyer

**[10:34]** have to go out with this human lawyer

**[10:34]** have to go out with this human lawyer and a human you know judge and a jury of

**[10:37]** and a human you know judge and a jury of

**[10:37]** and a human you know judge and a jury of humans to figure out what to do in that

**[10:40]** humans to figure out what to do in that

**[10:40]** humans to figure out what to do in that particular situation right so I feel

**[10:42]** particular situation right so I feel

**[10:42]** particular situation right so I feel like uh there should be something that

**[10:44]** like uh there should be something that

**[10:44]** like uh there should be something that is learning rules from us and it should

**[10:47]** is learning rules from us and it should

**[10:47]** is learning rules from us and it should be learning our taste of writing code

**[10:49]** be learning our taste of writing code

**[10:50]** be learning our taste of writing code and that is why I've put this thing

**[10:51]** and that is why I've put this thing

**[10:51]** and that is why I've put this thing taste here what what does that look like

**[10:53]** taste here what what does that look like

**[10:53]** taste here what what does that look like let me let me like uh like I I think

**[10:56]** let me let me like uh like I I think

**[10:56]** let me let me like uh like I I think this should be something that is

**[10:58]** this should be something that is

**[10:58]** this should be something that is acquiring our taste. So, uh, command


### [11:00 - 12:00]

**[11:01]** acquiring our taste. So, uh, command

**[11:01]** acquiring our taste. So, uh, command code a coding agent with taste or

**[11:05]** code a coding agent with taste or

**[11:05]** code a coding agent with taste or if I if I'm bold enough to say it's it's

**[11:07]** if I if I'm bold enough to say it's it's

**[11:07]** if I if I'm bold enough to say it's it's something that is a coding agent with an

**[11:09]** something that is a coding agent with an

**[11:09]** something that is a coding agent with an acquired taste. It learns what is your

**[11:12]** acquired taste. It learns what is your

**[11:12]** acquired taste. It learns what is your taste of writing code. And this is sort

**[11:14]** taste of writing code. And this is sort

**[11:14]** taste of writing code. And this is sort of what it looks like. So, I know this

**[11:17]** of what it looks like. So, I know this

**[11:17]** of what it looks like. So, I know this might be a very silly and bad example. I

**[11:19]** might be a very silly and bad example. I

**[11:19]** might be a very silly and bad example. I didn't want to put a lot of text here.

**[11:21]** didn't want to put a lot of text here.

**[11:21]** didn't want to put a lot of text here. But when I look at this code which is AI

**[11:23]** But when I look at this code which is AI

**[11:23]** But when I look at this code which is AI generated, I'm like, no, no, no. This is

**[11:25]** generated, I'm like, no, no, no. This is

**[11:25]** generated, I'm like, no, no, no. This is not good. I want JavaScript uh object

**[11:28]** not good. I want JavaScript uh object

**[11:28]** not good. I want JavaScript uh object parameters. Anytime there are more than

**[11:31]** parameters. Anytime there are more than

**[11:31]** parameters. Anytime there are more than two parameters, I want that. But AI

**[11:33]** two parameters, I want that. But AI

**[11:33]** two parameters, I want that. But AI won't uh you know listen to me. LLMs

**[11:35]** won't uh you know listen to me. LLMs

**[11:35]** won't uh you know listen to me. LLMs won't know my preferences of this thing.

**[11:38]** won't know my preferences of this thing.

**[11:38]** won't know my preferences of this thing. So again, when I ask for make me a

**[11:40]** So again, when I ask for make me a

**[11:40]** So again, when I ask for make me a sum.js function, this is again a very

**[11:43]** sum.js function, this is again a very

**[11:43]** sum.js function, this is again a very dumbed down version of an example. U

**[11:46]** dumbed down version of an example. U

**[11:46]** dumbed down version of an example. U cloud code won't do what I want it to

**[11:48]** cloud code won't do what I want it to

**[11:48]** cloud code won't do what I want it to do. in command just naturally knows this

**[11:50]** do. in command just naturally knows this

**[11:50]** do. in command just naturally knows this is what I prefer because it has seen me

**[11:52]** is what I prefer because it has seen me

**[11:52]** is what I prefer because it has seen me go and edit AI code and fix it this way

**[11:55]** go and edit AI code and fix it this way

**[11:55]** go and edit AI code and fix it this way right and similarly we kind of saw this

**[11:58]** right and similarly we kind of saw this

**[11:58]** right and similarly we kind of saw this happen when I asked to build a date CLI


### [12:00 - 13:00]

**[12:01]** happen when I asked to build a date CLI

**[12:01]** happen when I asked to build a date CLI this is you know claude basically

**[12:02]** this is you know claude basically

**[12:02]** this is you know claude basically started with here's a console and I had

**[12:04]** started with here's a console and I had

**[12:04]** started with here's a console and I had to tell it no I I want PNPM I want I

**[12:08]** to tell it no I I want PNPM I want I

**[12:08]** to tell it no I I want PNPM I want I want TypeScript and all of that fun

**[12:09]** want TypeScript and all of that fun

**[12:09]** want TypeScript and all of that fun stuff whereas command just kind of knows

**[12:12]** stuff whereas command just kind of knows

**[12:12]** stuff whereas command just kind of knows that I prefer commander I prefer all of

**[12:14]** that I prefer commander I prefer all of

**[12:14]** that I prefer commander I prefer all of those things that I just you know demoed

**[12:16]** those things that I just you know demoed

**[12:16]** those things that I just you know demoed earlier in this particular talk Okay.

**[12:21]** earlier in this particular talk Okay.

**[12:21]** earlier in this particular talk Okay. So to sum it up, I think when

**[12:24]** So to sum it up, I think when

**[12:24]** So to sum it up, I think when programmers talk about good code,

**[12:26]** programmers talk about good code,

**[12:26]** programmers talk about good code, they're not talking about code that is

**[12:28]** they're not talking about code that is

**[12:28]** they're not talking about code that is correct. They're talking about this

**[12:31]** correct. They're talking about this

**[12:31]** correct. They're talking about this invisible architecture of choices that

**[12:34]** invisible architecture of choices that

**[12:34]** invisible architecture of choices that they have made throughout the course of

**[12:36]** they have made throughout the course of

**[12:36]** they have made throughout the course of their career to make their code, you

**[12:38]** their career to make their code, you

**[12:38]** their career to make their code, you know, kind of like readable,

**[12:40]** know, kind of like readable,

**[12:40]** know, kind of like readable, maintainable and humane and more like,

**[12:42]** maintainable and humane and more like,

**[12:42]** maintainable and humane and more like, you know, you which is which is I think

**[12:44]** you know, you which is which is I think

**[12:44]** you know, you which is which is I think what is stopping me to write a lot of

**[12:46]** what is stopping me to write a lot of

**[12:46]** what is stopping me to write a lot of code. I want to generate my mission is

**[12:49]** code. I want to generate my mission is

**[12:49]** code. I want to generate my mission is like what if I could do a lot of things

**[12:52]** like what if I could do a lot of things

**[12:52]** like what if I could do a lot of things in one day. What if I can have like a

**[12:54]** in one day. What if I can have like a

**[12:54]** in one day. What if I can have like a thousand poll requests merged to main uh

**[12:58]** thousand poll requests merged to main uh

**[12:58]** thousand poll requests merged to main uh you know and my review time would just


### [13:00 - 14:00]

**[13:00]** you know and my review time would just

**[13:00]** you know and my review time would just go down by 90% or 99%. If an LLM if a

**[13:04]** go down by 90% or 99%. If an LLM if a

**[13:04]** go down by 90% or 99%. If an LLM if a coding agent was doing what I wanted to

**[13:07]** coding agent was doing what I wanted to

**[13:07]** coding agent was doing what I wanted to do right if it is not just picking up

**[13:09]** do right if it is not just picking up

**[13:09]** do right if it is not just picking up some sloppy code from 2015 Stack

**[13:12]** some sloppy code from 2015 Stack

**[13:12]** some sloppy code from 2015 Stack Overflow and slapping it to you know

**[13:15]** Overflow and slapping it to you know

**[13:15]** Overflow and slapping it to you know every request I have and I don't have

**[13:17]** every request I have and I don't have

**[13:17]** every request I have and I don't have time to teach it all the rules. I can

**[13:19]** time to teach it all the rules. I can

**[13:19]** time to teach it all the rules. I can either write code or I can teach it to

**[13:22]** either write code or I can teach it to

**[13:22]** either write code or I can teach it to write code. I I cannot be the one who's

**[13:25]** write code. I I cannot be the one who's

**[13:25]** write code. I I cannot be the one who's uh you know telling it when I'm using

**[13:26]** uh you know telling it when I'm using

**[13:26]** uh you know telling it when I'm using Nex.js GS or oh no this even though

**[13:29]** Nex.js GS or oh no this even though

**[13:29]** Nex.js GS or oh no this even though those both those both of those are you

**[13:30]** those both those both of those are you

**[13:30]** those both those both of those are you know creating API route files what is

**[13:33]** know creating API route files what is

**[13:33]** know creating API route files what is the difference when I'm in this project

**[13:35]** the difference when I'm in this project

**[13:35]** the difference when I'm in this project and that project it should just learn

**[13:37]** and that project it should just learn

**[13:37]** and that project it should just learn that in this situation this is the

**[13:39]** that in this situation this is the

**[13:40]** that in this situation this is the confidence level it has around the

**[13:42]** confidence level it has around the

**[13:42]** confidence level it has around the conflicts that uh you know that arise

**[13:44]** conflicts that uh you know that arise

**[13:44]** conflicts that uh you know that arise from different rules and different

**[13:46]** from different rules and different

**[13:46]** from different rules and different projects right so I I I don't I don't

**[13:48]** projects right so I I I don't I don't

**[13:48]** projects right so I I I don't I don't think I can do that again this is this

**[13:50]** think I can do that again this is this

**[13:50]** think I can do that again this is this excites the hell out of me I think this

**[13:52]** excites the hell out of me I think this

**[13:52]** excites the hell out of me I think this is the invisible architecture of choices

**[13:54]** is the invisible architecture of choices

**[13:54]** is the invisible architecture of choices that every programmer is making and that

**[13:57]** that every programmer is making and that

**[13:57]** that every programmer is making and that is that is what we are trying to build

**[13:59]** is that is what we are trying to build

**[13:59]** is that is what we are trying to build here uh you know a meta neuros symbolic


### [14:00 - 15:00]

**[14:03]** here uh you know a meta neuros symbolic

**[14:03]** here uh you know a meta neuros symbolic reasoning space with reinforcement

**[14:05]** reasoning space with reinforcement

**[14:05]** reasoning space with reinforcement learning. This is this is a very dumbed

**[14:08]** learning. This is this is a very dumbed

**[14:08]** learning. This is this is a very dumbed down version uh a formula of how we have

**[14:11]** down version uh a formula of how we have

**[14:11]** down version uh a formula of how we have set this objective. Uh if if you don't

**[14:14]** set this objective. Uh if if you don't

**[14:14]** set this objective. Uh if if you don't know trans you know neurosymbolic

**[14:15]** know trans you know neurosymbolic

**[14:16]** know trans you know neurosymbolic architecture is a more deterministic

**[14:18]** architecture is a more deterministic

**[14:18]** architecture is a more deterministic inexplainable architecture than

**[14:19]** inexplainable architecture than

**[14:19]** inexplainable architecture than transformers. Transformers are

**[14:22]** transformers. Transformers are

**[14:22]** transformers. Transformers are generative. They they they are very

**[14:23]** generative. They they they are very

**[14:23]** generative. They they they are very probabilistic right. So what we are

**[14:25]** probabilistic right. So what we are

**[14:25]** probabilistic right. So what we are trying to do here is we are trying to I

**[14:28]** trying to do here is we are trying to I

**[14:28]** trying to do here is we are trying to I think claude and GPD are good enough

**[14:29]** think claude and GPD are good enough

**[14:29]** think claude and GPD are good enough really they are really good and you can

**[14:31]** really they are really good and you can

**[14:31]** really they are really good and you can use whatever LLM with command code but

**[14:33]** use whatever LLM with command code but

**[14:34]** use whatever LLM with command code but that LLM will be combined with your

**[14:36]** that LLM will be combined with your

**[14:36]** that LLM will be combined with your taste which is built up o upon this meta

**[14:39]** taste which is built up o upon this meta

**[14:39]** taste which is built up o upon this meta neurosy symbolic space you can think of

**[14:41]** neurosy symbolic space you can think of

**[14:41]** neurosy symbolic space you can think of it like uh you know a reax of your uh

**[14:45]** it like uh you know a reax of your uh

**[14:45]** it like uh you know a reax of your uh you know choices in petrit right and we

**[14:47]** you know choices in petrit right and we

**[14:47]** you know choices in petrit right and we have a kale divergence loop here as you

**[14:49]** have a kale divergence loop here as you

**[14:49]** have a kale divergence loop here as you can see like if you do end up doing

**[14:51]** can see like if you do end up doing

**[14:51]** can see like if you do end up doing something wrong we want the lm to you

**[14:54]** something wrong we want the lm to you

**[14:54]** something wrong we want the lm to you know [clears throat] correct you as

**[14:54]** know [clears throat] correct you as

**[14:54]** know [clears throat] correct you as Well, it's it's this amazing continuous

**[14:58]** Well, it's it's this amazing continuous

**[14:58]** Well, it's it's this amazing continuous learning tool that is both learning from


### [15:00 - 16:00]

**[15:01]** learning tool that is both learning from

**[15:01]** learning tool that is both learning from your explicit and your implicit

**[15:03]** your explicit and your implicit

**[15:03]** your explicit and your implicit feedback. And then again, it is creating

**[15:05]** feedback. And then again, it is creating

**[15:05]** feedback. And then again, it is creating that neuros symbolic space to enforce

**[15:07]** that neuros symbolic space to enforce

**[15:07]** that neuros symbolic space to enforce that invisible logic uh around your

**[15:11]** that invisible logic uh around your

**[15:11]** that invisible logic uh around your choices. The architecture that is in

**[15:13]** choices. The architecture that is in

**[15:13]** choices. The architecture that is in your head, it is in your brain like oh

**[15:15]** your head, it is in your brain like oh

**[15:15]** your head, it is in your brain like oh yeah, when I'm building uh you know a

**[15:17]** yeah, when I'm building uh you know a

**[15:17]** yeah, when I'm building uh you know a TypeScript project, this is the type of

**[15:19]** TypeScript project, this is the type of

**[15:19]** TypeScript project, this is the type of thing I do, right? that kind of thing

**[15:21]** thing I do, right? that kind of thing

**[15:21]** thing I do, right? that kind of thing that can never really like you you your

**[15:23]** that can never really like you you your

**[15:23]** that can never really like you you your brain can never really translate that

**[15:25]** brain can never really translate that

**[15:25]** brain can never really translate that into a you know rules file otherwise

**[15:27]** into a you know rules file otherwise

**[15:27]** into a you know rules file otherwise like you won't be writing code you'll be

**[15:29]** like you won't be writing code you'll be

**[15:29]** like you won't be writing code you'll be writing a lot of rules files right and

**[15:31]** writing a lot of rules files right and

**[15:31]** writing a lot of rules files right and then again uh at the end to use the new

**[15:35]** then again uh at the end to use the new

**[15:35]** then again uh at the end to use the new neural part the LLM part we have

**[15:37]** neural part the LLM part we have

**[15:37]** neural part the LLM part we have reflective context engineering which is

**[15:39]** reflective context engineering which is

**[15:39]** reflective context engineering which is self-aware which is continuously

**[15:41]** self-aware which is continuously

**[15:41]** self-aware which is continuously learning and adopting like oh this guy

**[15:43]** learning and adopting like oh this guy

**[15:43]** learning and adopting like oh this guy used to use meow for writing CLI and I

**[15:47]** used to use meow for writing CLI and I

**[15:47]** used to use meow for writing CLI and I don't know what happened but two months

**[15:48]** don't know what happened but two months

**[15:48]** don't know what happened but two months ago it's he switched to commander I'm

**[15:50]** ago it's he switched to commander I'm

**[15:50]** ago it's he switched to commander I'm talking about this guy by the way. This

**[15:52]** talking about this guy by the way. This

**[15:52]** talking about this guy by the way. This literally happened, right? And it will

**[15:55]** literally happened, right? And it will

**[15:55]** literally happened, right? And it will automatically update my rules, my uh

**[15:58]** automatically update my rules, my uh

**[15:58]** automatically update my rules, my uh learning from me, my taste that now


### [16:00 - 17:00]

**[16:01]** learning from me, my taste that now

**[16:01]** learning from me, my taste that now Emmeth prefers to use commander over

**[16:03]** Emmeth prefers to use commander over

**[16:04]** Emmeth prefers to use commander over meow. I don't need to go and teach it. I

**[16:06]** meow. I don't need to go and teach it. I

**[16:06]** meow. I don't need to go and teach it. I should be writing code at I don't know

**[16:08]** should be writing code at I don't know

**[16:08]** should be writing code at I don't know god speed and it should be learning all

**[16:11]** god speed and it should be learning all

**[16:11]** god speed and it should be learning all of this from me. And over time we've

**[16:14]** of this from me. And over time we've

**[16:14]** of this from me. And over time we've believed that this will turn it uh into

**[16:17]** believed that this will turn it uh into

**[16:17]** believed that this will turn it uh into a skill of intuition that command code

**[16:19]** a skill of intuition that command code

**[16:19]** a skill of intuition that command code will have that you can share with your

**[16:21]** will have that you can share with your

**[16:21]** will have that you can share with your team. Our mission is to build a huge

**[16:24]** team. Our mission is to build a huge

**[16:24]** team. Our mission is to build a huge ecosystem around this. Imagine if you

**[16:26]** ecosystem around this. Imagine if you

**[16:26]** ecosystem around this. Imagine if you could if you really like a developer out

**[16:28]** could if you really like a developer out

**[16:28]** could if you really like a developer out there uh whose react uh uh you know code

**[16:32]** there uh whose react uh uh you know code

**[16:32]** there uh whose react uh uh you know code is amazing, right? I I love what Tanner

**[16:34]** is amazing, right? I I love what Tanner

**[16:34]** is amazing, right? I I love what Tanner is doing at Tenner St with ten stack,

**[16:36]** is doing at Tenner St with ten stack,

**[16:36]** is doing at Tenner St with ten stack, right? So what if I could have tanner

**[16:39]** right? So what if I could have tanner

**[16:39]** right? So what if I could have tanner taste when I'm writing React code? You

**[16:42]** taste when I'm writing React code? You

**[16:42]** taste when I'm writing React code? You can do that with command code. What if

**[16:44]** can do that with command code. What if

**[16:44]** can do that with command code. What if like one of the things that I have been

**[16:45]** like one of the things that I have been

**[16:45]** like one of the things that I have been using it a lot for like my design

**[16:47]** using it a lot for like my design

**[16:47]** using it a lot for like my design engineer has a much better design skill

**[16:50]** engineer has a much better design skill

**[16:50]** engineer has a much better design skill than I do. uh whenever I'm writing any

**[16:52]** than I do. uh whenever I'm writing any

**[16:52]** than I do. uh whenever I'm writing any kind of front-end code, I actually

**[16:54]** kind of front-end code, I actually

**[16:54]** kind of front-end code, I actually borrow the design engineer taste I have

**[16:57]** borrow the design engineer taste I have

**[16:57]** borrow the design engineer taste I have which is which is messy like all sort


### [17:00 - 18:00]

**[17:00]** which is which is messy like all sort

**[17:00]** which is which is messy like all sort all those margins and paddings and uh

**[17:02]** all those margins and paddings and uh

**[17:02]** all those margins and paddings and uh amazing tiny little details in his taste

**[17:05]** amazing tiny little details in his taste

**[17:05]** amazing tiny little details in his taste that I don't need to now care about but

**[17:08]** that I don't need to now care about but

**[17:08]** that I don't need to now care about but my LLM in my command code my coding

**[17:10]** my LLM in my command code my coding

**[17:10]** my LLM in my command code my coding agent kind of puts that LLM and that

**[17:13]** agent kind of puts that LLM and that

**[17:13]** agent kind of puts that LLM and that meta neurosy symbolic design taste

**[17:15]** meta neurosy symbolic design taste

**[17:15]** meta neurosy symbolic design taste alongside my request like build me a

**[17:17]** alongside my request like build me a

**[17:17]** alongside my request like build me a model that does this but it does it with

**[17:20]** model that does this but it does it with

**[17:20]** model that does this but it does it with my design engineer st which is

**[17:22]** my design engineer st which is

**[17:22]** my design engineer st which is unbelievable right so uh this is this is

**[17:25]** unbelievable right so uh this is this is

**[17:25]** unbelievable right so uh this is this is this is where we are today uh today we

**[17:28]** this is where we are today uh today we

**[17:28]** this is where we are today uh today we are launching command code you can you

**[17:29]** are launching command code you can you

**[17:29]** are launching command code you can you can you know feel free to go to

**[17:31]** can you know feel free to go to

**[17:31]** can you know feel free to go to commandcode.ai AI you know check it out

**[17:33]** commandcode.ai AI you know check it out

**[17:34]** commandcode.ai AI you know check it out this is the very beginning of all of it

**[17:36]** this is the very beginning of all of it

**[17:36]** this is the very beginning of all of it and I think large language models have

**[17:39]** and I think large language models have

**[17:39]** and I think large language models have captured the world stacks everything out

**[17:42]** captured the world stacks everything out

**[17:42]** captured the world stacks everything out there all of the stack overflow and

**[17:43]** there all of the stack overflow and

**[17:43]** there all of the stack overflow and whatnot and I believe what we are

**[17:46]** whatnot and I believe what we are

**[17:46]** whatnot and I believe what we are building with taste models is the

**[17:49]** building with taste models is the

**[17:49]** building with taste models is the world's intuition right and their

**[17:51]** world's intuition right and their

**[17:52]** world's intuition right and their intentions right what do you intend to

**[17:54]** intentions right what do you intend to

**[17:54]** intentions right what do you intend to do and how do you generally do it what

**[17:56]** do and how do you generally do it what

**[17:56]** do and how do you generally do it what are the patterns what is your taste in

**[17:58]** are the patterns what is your taste in

**[17:58]** are the patterns what is your taste in that taste with your preferred LLM


### [18:00 - 19:00]

**[18:02]** that taste with your preferred LLM

**[18:02]** that taste with your preferred LLM is I think the next frontier of coding,

**[18:05]** is I think the next frontier of coding,

**[18:05]** is I think the next frontier of coding, right? Taste I totally believe is going

**[18:08]** right? Taste I totally believe is going

**[18:08]** right? Taste I totally believe is going to really really speed up how we write

**[18:11]** to really really speed up how we write

**[18:11]** to really really speed up how we write code. really really create that neuros

**[18:14]** code. really really create that neuros

**[18:14]** code. really really create that neuros symbolic uh guard rails or your you know

**[18:17]** symbolic uh guard rails or your you know

**[18:17]** symbolic uh guard rails or your you know again invisible architecture of choices

**[18:19]** again invisible architecture of choices

**[18:19]** again invisible architecture of choices that you have as a team as a project as

**[18:23]** that you have as a team as a project as

**[18:23]** that you have as a team as a project as a famous library or I don't know maybe

**[18:26]** a famous library or I don't know maybe

**[18:26]** a famous library or I don't know maybe you are an enterprise who care about

**[18:28]** you are an enterprise who care about

**[18:28]** you are an enterprise who care about doing things in a particular way right

**[18:30]** doing things in a particular way right

**[18:30]** doing things in a particular way right that is the kind of thing that you would

**[18:32]** that is the kind of thing that you would

**[18:32]** that is the kind of thing that you would be able to build taste around and share

**[18:35]** be able to build taste around and share

**[18:35]** be able to build taste around and share it with uh uh you know as an open source

**[18:37]** it with uh uh you know as an open source

**[18:37]** it with uh uh you know as an open source taste or share it with uh just your team

**[18:39]** taste or share it with uh just your team

**[18:40]** taste or share it with uh just your team like for example uh for example if you

**[18:41]** like for example uh for example if you

**[18:42]** like for example uh for example if you go sign up. Uh again, this is very very

**[18:44]** go sign up. Uh again, this is very very

**[18:44]** go sign up. Uh again, this is very very new. Uh this is potentially it will look

**[18:46]** new. Uh this is potentially it will look

**[18:46]** new. Uh this is potentially it will look like right. Uh we've already kind of

**[18:48]** like right. Uh we've already kind of

**[18:48]** like right. Uh we've already kind of moved away from uh sharing all of this

**[18:50]** moved away from uh sharing all of this

**[18:50]** moved away from uh sharing all of this and we are figuring out I would love

**[18:51]** and we are figuring out I would love

**[18:52]** and we are figuring out I would love your help to figure out what is the

**[18:54]** your help to figure out what is the

**[18:54]** your help to figure out what is the right mix of uh having all of this

**[18:56]** right mix of uh having all of this

**[18:56]** right mix of uh having all of this metalarning uh you know uh be part of


### [19:00 - 20:00]

**[19:01]** metalarning uh you know uh be part of

**[19:01]** metalarning uh you know uh be part of your projects. Right now it kind of ends

**[19:03]** your projects. Right now it kind of ends

**[19:03]** your projects. Right now it kind of ends up as more of a you know what should I

**[19:06]** up as more of a you know what should I

**[19:06]** up as more of a you know what should I say a transparent markdown file but it

**[19:09]** say a transparent markdown file but it

**[19:09]** say a transparent markdown file but it could exist in any which way. It's a

**[19:11]** could exist in any which way. It's a

**[19:11]** could exist in any which way. It's a metano symbolic space in a model that is

**[19:14]** metano symbolic space in a model that is

**[19:14]** metano symbolic space in a model that is continuously learning your preferences

**[19:17]** continuously learning your preferences

**[19:17]** continuously learning your preferences and we can dump that learning in any

**[19:19]** and we can dump that learning in any

**[19:19]** and we can dump that learning in any particular form. Right now this is

**[19:21]** particular form. Right now this is

**[19:21]** particular form. Right now this is potentially what it looks like. You

**[19:23]** potentially what it looks like. You

**[19:23]** potentially what it looks like. You should be able to you know npx taste and

**[19:25]** should be able to you know npx taste and

**[19:25]** should be able to you know npx taste and install my CLI taste and then you can

**[19:28]** install my CLI taste and then you can

**[19:28]** install my CLI taste and then you can use command code and the CLI that you

**[19:30]** use command code and the CLI that you

**[19:30]** use command code and the CLI that you will build will be very very close to

**[19:33]** will build will be very very close to

**[19:33]** will build will be very very close to you know how I would build that CLI

**[19:35]** you know how I would build that CLI

**[19:35]** you know how I would build that CLI using your favorite LLMs. So yeah,

**[19:38]** using your favorite LLMs. So yeah,

**[19:38]** using your favorite LLMs. So yeah, that's pretty much it. As you can as you

**[19:41]** that's pretty much it. As you can as you

**[19:41]** that's pretty much it. As you can as you can see, I am pretty excited. Uh you

**[19:43]** can see, I am pretty excited. Uh you

**[19:43]** can see, I am pretty excited. Uh you know, uh our our biggest gains that we

**[19:46]** know, uh our our biggest gains that we

**[19:46]** know, uh our our biggest gains that we have seen uh internally at Langbase are

**[19:50]** have seen uh internally at Langbase are

**[19:50]** have seen uh internally at Langbase are we have probably 10xed the amount of

**[19:53]** we have probably 10xed the amount of

**[19:53]** we have probably 10xed the amount of code that we are merging uh uh in our

**[19:56]** code that we are merging uh uh in our

**[19:56]** code that we are merging uh uh in our main repository, right, in our maiden

**[19:59]** main repository, right, in our maiden

**[19:59]** main repository, right, in our maiden branch, right? which is generally we


### [20:00 - 21:00]

**[20:01]** branch, right? which is generally we

**[20:01]** branch, right? which is generally we joke about it like when we disagree and

**[20:03]** joke about it like when we disagree and

**[20:03]** joke about it like when we disagree and compare to main the amount of that

**[20:05]** compare to main the amount of that

**[20:05]** compare to main the amount of that happening has increased 10x and um I I

**[20:10]** happening has increased 10x and um I I

**[20:10]** happening has increased 10x and um I I I'm feeling a lot more confident uh when

**[20:12]** I'm feeling a lot more confident uh when

**[20:12]** I'm feeling a lot more confident uh when I'm reviewing a lot of code right so our

**[20:15]** I'm reviewing a lot of code right so our

**[20:15]** I'm reviewing a lot of code right so our review uh time for any kind of coding

**[20:17]** review uh time for any kind of coding

**[20:18]** review uh time for any kind of coding pull requests have gone down

**[20:19]** pull requests have gone down

**[20:19]** pull requests have gone down significantly and I can't wait to see

**[20:21]** significantly and I can't wait to see

**[20:22]** significantly and I can't wait to see you know what everybody out there builds

**[20:23]** you know what everybody out there builds

**[20:23]** you know what everybody out there builds with it again we're very excited we want

**[20:26]** with it again we're very excited we want

**[20:26]** with it again we're very excited we want that LLMs should continuously be

**[20:29]** that LLMs should continuously be

**[20:29]** that LLMs should continuously be learning from our taste of writing code

**[20:32]** learning from our taste of writing code

**[20:32]** learning from our taste of writing code and I would love to see uh you know what

**[20:34]** and I would love to see uh you know what

**[20:34]** and I would love to see uh you know what you build with command code u that's

**[20:36]** you build with command code u that's

**[20:36]** you build with command code u that's pretty much it uh feel free to reach out

**[20:39]** pretty much it uh feel free to reach out

**[20:39]** pretty much it uh feel free to reach out and uh maybe you know uh send me a tweet

**[20:41]** and uh maybe you know uh send me a tweet

**[20:41]** and uh maybe you know uh send me a tweet or post or whatever you call uh we call

**[20:43]** or post or whatever you call uh we call

**[20:43]** or post or whatever you call uh we call it these days uh and I would love to see

**[20:45]** it these days uh and I would love to see

**[20:45]** it these days uh and I would love to see you know what everyone builds this is me

**[20:48]** you know what everyone builds this is me

**[20:48]** you know what everyone builds this is me uh thanks for having me ciao peace


