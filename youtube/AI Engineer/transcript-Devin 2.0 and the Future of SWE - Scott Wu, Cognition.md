# Devin 2.0 and the Future of SWE - Scott Wu, Cognition

**Video URL:** https://www.youtube.com/watch?v=MI83buT_23o

---

## Full Transcript

### [00:00 - 01:00]

**[00:15]** Yeah. Well, thank you guys so much for

**[00:15]** Yeah. Well, thank you guys so much for having me. It's exciting to be back.

**[00:17]** having me. It's exciting to be back.

**[00:17]** having me. It's exciting to be back. It's uh I I was last here at AI Engineer

**[00:20]** It's uh I I was last here at AI Engineer

**[00:20]** It's uh I I was last here at AI Engineer one year ago. Um and it's kind of crazy.

**[00:22]** one year ago. Um and it's kind of crazy.

**[00:22]** one year ago. Um and it's kind of crazy. I I've always been I I've been telling

**[00:23]** I I've always been I I've been telling

**[00:23]** I I've always been I I've been telling Swix that we need to have these

**[00:25]** Swix that we need to have these

**[00:25]** Swix that we need to have these conferences way more often if it's going

**[00:26]** conferences way more often if it's going

**[00:26]** conferences way more often if it's going to be about AI software engineering.

**[00:28]** to be about AI software engineering.

**[00:28]** to be about AI software engineering. probably should be like every two months

**[00:29]** probably should be like every two months

**[00:29]** probably should be like every two months or something like that with the pace of

**[00:31]** or something like that with the pace of

**[00:31]** or something like that with the pace of everything's done. But but but going to

**[00:33]** everything's done. But but but going to

**[00:33]** everything's done. But but but going to be fun to to talk a little bit about um

**[00:35]** be fun to to talk a little bit about um

**[00:35]** be fun to to talk a little bit about um you know what we've seen in the space

**[00:36]** you know what we've seen in the space

**[00:36]** you know what we've seen in the space and and what we've learned over the last

**[00:38]** and and what we've learned over the last

**[00:38]** and and what we've learned over the last 12 or 18 months uh building Devon over

**[00:41]** 12 or 18 months uh building Devon over

**[00:41]** 12 or 18 months uh building Devon over this time.

**[00:43]** this time.

**[00:43]** this time. And I want to start this off with um

**[00:47]** And I want to start this off with um

**[00:47]** And I want to start this off with um Moore's law for AI agents. And so you

**[00:49]** Moore's law for AI agents. And so you

**[00:49]** Moore's law for AI agents. And so you can kind of think of the the the

**[00:50]** can kind of think of the the the

**[00:50]** can kind of think of the the the capability or the capacity of an AI by

**[00:54]** capability or the capacity of an AI by

**[00:54]** capability or the capacity of an AI by how much work it can do uninter

**[00:57]** how much work it can do uninter

**[00:57]** how much work it can do uninter uninterrupted until you have to come in

**[00:58]** uninterrupted until you have to come in

**[00:58]** uninterrupted until you have to come in and step in and intervene or steer it or


### [01:00 - 02:00]

**[01:01]** and step in and intervene or steer it or

**[01:01]** and step in and intervene or steer it or whatever it is, right? And um you know

**[01:03]** whatever it is, right? And um you know

**[01:03]** whatever it is, right? And um you know in GPT3 for example, it's if you were to

**[01:06]** in GPT3 for example, it's if you were to

**[01:06]** in GPT3 for example, it's if you were to go and ask GPT3 to do something, you

**[01:08]** go and ask GPT3 to do something, you

**[01:08]** go and ask GPT3 to do something, you know, it could probably get through a

**[01:09]** know, it could probably get through a

**[01:09]** know, it could probably get through a few words or so and then it'll say

**[01:10]** few words or so and then it'll say

**[01:10]** few words or so and then it'll say something where it's like okay, you

**[01:11]** something where it's like okay, you

**[01:11]** something where it's like okay, you know, this is probably not the right

**[01:13]** know, this is probably not the right

**[01:13]** know, this is probably not the right thing to say. Um and GPT3.5 was better

**[01:16]** thing to say. Um and GPT3.5 was better

**[01:16]** thing to say. Um and GPT3.5 was better and GP4 was better, right? Um and and so

**[01:18]** and GP4 was better, right? Um and and so

**[01:18]** and GP4 was better, right? Um and and so people talk about these lengths of tasks

**[01:20]** people talk about these lengths of tasks

**[01:20]** people talk about these lengths of tasks and what you see in general is that that

**[01:22]** and what you see in general is that that

**[01:22]** and what you see in general is that that doubling time is about every seven

**[01:24]** doubling time is about every seven

**[01:24]** doubling time is about every seven months which already is pretty crazy

**[01:26]** months which already is pretty crazy

**[01:26]** months which already is pretty crazy actually. But in code it's actually even

**[01:29]** actually. But in code it's actually even

**[01:29]** actually. But in code it's actually even faster. It's every 70 days which is two

**[01:31]** faster. It's every 70 days which is two

**[01:31]** faster. It's every 70 days which is two or three months. And so, you know, if

**[01:33]** or three months. And so, you know, if

**[01:33]** or three months. And so, you know, if you look at various software engineering

**[01:35]** you look at various software engineering

**[01:35]** you look at various software engineering tasks that start from the simplest

**[01:38]** tasks that start from the simplest

**[01:38]** tasks that start from the simplest single functions or single lines and you

**[01:40]** single functions or single lines and you

**[01:40]** single functions or single lines and you go all the way to, you know, we're doing

**[01:42]** go all the way to, you know, we're doing

**[01:42]** go all the way to, you know, we're doing tasks now that take hours of humans time

**[01:45]** tasks now that take hours of humans time

**[01:45]** tasks now that take hours of humans time and and an AI agent is able to just do

**[01:47]** and and an AI agent is able to just do

**[01:47]** and and an AI agent is able to just do all of that, right? Um, and if you think

**[01:50]** all of that, right? Um, and if you think

**[01:50]** all of that, right? Um, and if you think about doubling every 70 days, I mean,

**[01:52]** about doubling every 70 days, I mean,

**[01:52]** about doubling every 70 days, I mean, basically, you know, every two to three

**[01:54]** basically, you know, every two to three

**[01:54]** basically, you know, every two to three months means you get four to six

**[01:55]** months means you get four to six

**[01:55]** months means you get four to six doublings every year. Um, which means

**[01:57]** doublings every year. Um, which means

**[01:57]** doublings every year. Um, which means that the amount of work that an AI agent


### [02:00 - 03:00]

**[02:00]** that the amount of work that an AI agent

**[02:00]** that the amount of work that an AI agent can do in code goes something between 16

**[02:03]** can do in code goes something between 16

**[02:03]** can do in code goes something between 16 and 64x in a year every year at least

**[02:06]** and 64x in a year every year at least

**[02:06]** and 64x in a year every year at least for the last couple years that we've

**[02:08]** for the last couple years that we've

**[02:08]** for the last couple years that we've seen. Um, and it's kind of crazy to

**[02:10]** seen. Um, and it's kind of crazy to

**[02:10]** seen. Um, and it's kind of crazy to think about, but but that sounds about

**[02:12]** think about, but but that sounds about

**[02:12]** think about, but but that sounds about right actually for for what we've seen.

**[02:13]** right actually for for what we've seen.

**[02:13]** right actually for for what we've seen. You know, 18 months ago, I would say the

**[02:15]** You know, 18 months ago, I would say the

**[02:15]** You know, 18 months ago, I would say the only really the only product experience

**[02:17]** only really the only product experience

**[02:17]** only really the only product experience that had PMF in code was just tab

**[02:20]** that had PMF in code was just tab

**[02:20]** that had PMF in code was just tab completion, right? It was just like

**[02:23]** completion, right? It was just like

**[02:23]** completion, right? It was just like here's what I have so far. Predict the

**[02:24]** here's what I have so far. Predict the

**[02:24]** here's what I have so far. Predict the next line for me. that was kind of all

**[02:26]** next line for me. that was kind of all

**[02:26]** next line for me. that was kind of all you really could do um in in a way that

**[02:28]** you really could do um in in a way that

**[02:28]** you really could do um in in a way that really worked. And we've gone from that

**[02:30]** really worked. And we've gone from that

**[02:30]** really worked. And we've gone from that obviously to full AI engineer that goes

**[02:33]** obviously to full AI engineer that goes

**[02:33]** obviously to full AI engineer that goes and just do does does all these tasks

**[02:35]** and just do does does all these tasks

**[02:35]** and just do does does all these tasks for you, right? And implements a ton of

**[02:36]** for you, right? And implements a ton of

**[02:36]** for you, right? And implements a ton of these things. And people ask all the

**[02:38]** these things. And people ask all the

**[02:38]** these things. And people ask all the time, what is the um you know what what

**[02:42]** time, what is the um you know what what

**[02:42]** time, what is the um you know what what what is the the future interface or what

**[02:44]** what is the the future interface or what

**[02:44]** what is the the future interface or what is the right way to do this or what are

**[02:46]** is the right way to do this or what are

**[02:46]** is the right way to do this or what are the most important capabilities to solve

**[02:48]** the most important capabilities to solve

**[02:48]** the most important capabilities to solve for? And I think funnily enough, the

**[02:49]** for? And I think funnily enough, the

**[02:49]** for? And I think funnily enough, the answer to all these questions actually

**[02:51]** answer to all these questions actually

**[02:51]** answer to all these questions actually is it changes every two or three months.

**[02:53]** is it changes every two or three months.

**[02:53]** is it changes every two or three months. like every time you get to the next

**[02:55]** like every time you get to the next

**[02:55]** like every time you get to the next tier, the the the bottleneck that you're

**[02:58]** tier, the the the bottleneck that you're

**[02:58]** tier, the the the bottleneck that you're running into or the most important

**[02:59]** running into or the most important

**[02:59]** running into or the most important capability or the right way you should


### [03:00 - 04:00]

**[03:01]** capability or the right way you should

**[03:01]** capability or the right way you should be interfacing with it, like all these

**[03:02]** be interfacing with it, like all these

**[03:02]** be interfacing with it, like all these actually change at at each point. And so

**[03:06]** actually change at at each point. And so

**[03:06]** actually change at at each point. And so I wanted to talk a bit about some of the

**[03:08]** I wanted to talk a bit about some of the

**[03:08]** I wanted to talk a bit about some of the the tiers for us over the last year or

**[03:12]** the tiers for us over the last year or

**[03:12]** the tiers for us over the last year or so. Um and you know over the course of

**[03:15]** so. Um and you know over the course of

**[03:15]** so. Um and you know over the course of that time obviously you know when we got

**[03:16]** that time obviously you know when we got

**[03:16]** that time obviously you know when we got started um in the end of 2023 obviously

**[03:19]** started um in the end of 2023 obviously

**[03:19]** started um in the end of 2023 obviously agents were not even a concept. Um, and

**[03:21]** agents were not even a concept. Um, and

**[03:21]** agents were not even a concept. Um, and now everyone has, you know, everyone's

**[03:22]** now everyone has, you know, everyone's

**[03:22]** now everyone has, you know, everyone's talking about coding agents, people are

**[03:23]** talking about coding agents, people are

**[03:23]** talking about coding agents, people are doing more and more and more. Uh, and

**[03:25]** doing more and more and more. Uh, and

**[03:25]** doing more and more and more. Uh, and and it's very cool to see. Um, and and

**[03:27]** and it's very cool to see. Um, and and

**[03:27]** and it's very cool to see. Um, and and each of these has kind of been almost a

**[03:29]** each of these has kind of been almost a

**[03:29]** each of these has kind of been almost a discrete tier for us. Um, and so right

**[03:32]** discrete tier for us. Um, and so right

**[03:32]** discrete tier for us. Um, and so right right around a year ago when we were

**[03:33]** right around a year ago when we were

**[03:34]** right around a year ago when we were doing the the last AI engineer talk

**[03:35]** doing the the last AI engineer talk

**[03:35]** doing the the last AI engineer talk actually, um, the the biggest use case

**[03:38]** actually, um, the the biggest use case

**[03:38]** actually, um, the the biggest use case that we really saw that that was getting

**[03:39]** that we really saw that that was getting

**[03:39]** that we really saw that that was getting broad adoption was what I'll kind of

**[03:41]** broad adoption was what I'll kind of

**[03:41]** broad adoption was what I'll kind of call these repetitive migrations. And so

**[03:44]** call these repetitive migrations. And so

**[03:44]** call these repetitive migrations. And so I'm talking like JavaScript to

**[03:45]** I'm talking like JavaScript to

**[03:45]** I'm talking like JavaScript to TypeScript or like upgrading your

**[03:48]** TypeScript or like upgrading your

**[03:48]** TypeScript or like upgrading your Angular version from this one to that

**[03:49]** Angular version from this one to that

**[03:49]** Angular version from this one to that one or going from this Java version to

**[03:51]** one or going from this Java version to

**[03:51]** one or going from this Java version to that Java version or something like

**[03:53]** that Java version or something like

**[03:53]** that Java version or something like that. Um and those those kinds of tasks

**[03:56]** that. Um and those those kinds of tasks

**[03:56]** that. Um and those those kinds of tasks in particular what you typically see is

**[03:59]** in particular what you typically see is

**[03:59]** in particular what you typically see is you are


### [04:00 - 05:00]

**[04:01]** you are

**[04:01]** you are you you have some massive code base that

**[04:03]** you you have some massive code base that

**[04:03]** you you have some massive code base that you want to apply this whole migration

**[04:05]** you want to apply this whole migration

**[04:05]** you want to apply this whole migration for. You have to go file by file and do

**[04:07]** for. You have to go file by file and do

**[04:07]** for. You have to go file by file and do every single one. And usually the set of

**[04:09]** every single one. And usually the set of

**[04:09]** every single one. And usually the set of steps is pretty clear, right? If you go

**[04:10]** steps is pretty clear, right? If you go

**[04:10]** steps is pretty clear, right? If you go to the Angular website or something like

**[04:12]** to the Angular website or something like

**[04:12]** to the Angular website or something like that, it'll tell you, all right, here's

**[04:13]** that, it'll tell you, all right, here's

**[04:14]** that, it'll tell you, all right, here's what you have to do. This, this, this,

**[04:15]** what you have to do. This, this, this,

**[04:15]** what you have to do. This, this, this, this, this, and um, you want to go and

**[04:18]** this, this, and um, you want to go and

**[04:18]** this, this, and um, you want to go and execute each of these steps. It's not so

**[04:20]** execute each of these steps. It's not so

**[04:20]** execute each of these steps. It's not so routine that there, you know, there's no

**[04:21]** routine that there, you know, there's no

**[04:21]** routine that there, you know, there's no classical deterministic program that

**[04:23]** classical deterministic program that

**[04:24]** classical deterministic program that solves that. But there's kind of a clear

**[04:25]** solves that. But there's kind of a clear

**[04:25]** solves that. But there's kind of a clear set of steps. And if you can follow

**[04:27]** set of steps. And if you can follow

**[04:27]** set of steps. And if you can follow those steps very well, then you can do

**[04:29]** those steps very well, then you can do

**[04:29]** those steps very well, then you can do the task. And, you know, this was the

**[04:30]** the task. And, you know, this was the

**[04:30]** the task. And, you know, this was the thing for us because that was all you

**[04:33]** thing for us because that was all you

**[04:33]** thing for us because that was all you could really trust agents to do at the

**[04:34]** could really trust agents to do at the

**[04:34]** could really trust agents to do at the time. you know, you could do harder

**[04:36]** time. you know, you could do harder

**[04:36]** time. you know, you could do harder things once in a while and you could do

**[04:37]** things once in a while and you could do

**[04:37]** things once in a while and you could do some really cool stuff occasionally,

**[04:40]** some really cool stuff occasionally,

**[04:40]** some really cool stuff occasionally, but as far as something that was

**[04:41]** but as far as something that was

**[04:41]** but as far as something that was consistent enough that you could do it

**[04:42]** consistent enough that you could do it

**[04:42]** consistent enough that you could do it over and over and over, um, these kinds

**[04:45]** over and over and over, um, these kinds

**[04:45]** over and over and over, um, these kinds of like repetitive migrations that you

**[04:46]** of like repetitive migrations that you

**[04:46]** of like repetitive migrations that you would be doing for, you know, 10,000

**[04:48]** would be doing for, you know, 10,000

**[04:48]** would be doing for, you know, 10,000 files were, you know, in many ways the

**[04:51]** files were, you know, in many ways the

**[04:51]** files were, you know, in many ways the the the easiest thing, which was cool

**[04:52]** the the easiest thing, which was cool

**[04:52]** the the easiest thing, which was cool actually because

**[04:55]** actually because

**[04:55]** actually because it was also kind of the the most

**[04:56]** it was also kind of the the most

**[04:56]** it was also kind of the the most annoying thing for humans to do. And I

**[04:58]** annoying thing for humans to do. And I

**[04:58]** annoying thing for humans to do. And I think that's generally been the trend

**[04:59]** think that's generally been the trend

**[04:59]** think that's generally been the trend where um AI has always done these more


### [05:00 - 06:00]

**[05:02]** where um AI has always done these more

**[05:02]** where um AI has always done these more boilerplate tasks and the more tedious

**[05:04]** boilerplate tasks and the more tedious

**[05:04]** boilerplate tasks and the more tedious stuff, the more repetitive stuff, and we

**[05:05]** stuff, the more repetitive stuff, and we

**[05:06]** stuff, the more repetitive stuff, and we get to do the the the more fun, creative

**[05:08]** get to do the the the more fun, creative

**[05:08]** get to do the the the more fun, creative stuff. Um and obviously as time has gone

**[05:10]** stuff. Um and obviously as time has gone

**[05:10]** stuff. Um and obviously as time has gone on, it's it's taken on more and more of

**[05:11]** on, it's it's taken on more and more of

**[05:11]** on, it's it's taken on more and more of that boiler plate. But for a problem

**[05:13]** that boiler plate. But for a problem

**[05:13]** that boiler plate. But for a problem like this one, a lot of what you need to

**[05:16]** like this one, a lot of what you need to

**[05:16]** like this one, a lot of what you need to do is you need Devon to be able to go

**[05:18]** do is you need Devon to be able to go

**[05:18]** do is you need Devon to be able to go and execute a set of steps reliably. And

**[05:22]** and execute a set of steps reliably. And

**[05:22]** and execute a set of steps reliably. And so a lot of this was, you know, I would

**[05:24]** so a lot of this was, you know, I would

**[05:24]** so a lot of this was, you know, I would say the big capabilities problems to

**[05:25]** say the big capabilities problems to

**[05:25]** say the big capabilities problems to solve was mostly instruction following.

**[05:28]** solve was mostly instruction following.

**[05:28]** solve was mostly instruction following. And so we built this system called

**[05:29]** And so we built this system called

**[05:29]** And so we built this system called playbooks where basically you could just

**[05:31]** playbooks where basically you could just

**[05:31]** playbooks where basically you could just outline a very clear set of steps, have

**[05:33]** outline a very clear set of steps, have

**[05:33]** outline a very clear set of steps, have it follow each of those step by step and

**[05:35]** it follow each of those step by step and

**[05:35]** it follow each of those step by step and then do exactly what's said. Now if you

**[05:37]** then do exactly what's said. Now if you

**[05:37]** then do exactly what's said. Now if you think about it, obviously a lot of

**[05:38]** think about it, obviously a lot of

**[05:38]** think about it, obviously a lot of software engineering does not fall under

**[05:40]** software engineering does not fall under

**[05:40]** software engineering does not fall under the category of literally just follow 10

**[05:42]** the category of literally just follow 10

**[05:42]** the category of literally just follow 10 steps step by step and do exactly what

**[05:44]** steps step by step and do exactly what

**[05:44]** steps step by step and do exactly what it said. But migration does and it

**[05:47]** it said. But migration does and it

**[05:47]** it said. But migration does and it allowed us to go and actually do these

**[05:48]** allowed us to go and actually do these

**[05:48]** allowed us to go and actually do these and and this was kind of I would say the

**[05:50]** and and this was kind of I would say the

**[05:50]** and and this was kind of I would say the first big use case of Devon that really

**[05:52]** first big use case of Devon that really

**[05:52]** first big use case of Devon that really um that really came up. I think one of

**[05:54]** um that really came up. I think one of

**[05:54]** um that really came up. I think one of the other big systems that got built

**[05:56]** the other big systems that got built

**[05:56]** the other big systems that got built around that time which we've since

**[05:57]** around that time which we've since

**[05:57]** around that time which we've since rebuilt many times is knowledge or

**[05:59]** rebuilt many times is knowledge or

**[05:59]** rebuilt many times is knowledge or memory right which is you know if you're


### [06:00 - 07:00]

**[06:01]** memory right which is you know if you're

**[06:01]** memory right which is you know if you're doing the same task over and over and

**[06:03]** doing the same task over and over and

**[06:04]** doing the same task over and over and over again then often the human will

**[06:05]** over again then often the human will

**[06:05]** over again then often the human will have feedback on hey by the way you have

**[06:07]** have feedback on hey by the way you have

**[06:07]** have feedback on hey by the way you have to remember to do X thing or you have to

**[06:09]** to remember to do X thing or you have to

**[06:09]** to remember to do X thing or you have to you know you need to do Y thing every

**[06:12]** you know you need to do Y thing every

**[06:12]** you know you need to do Y thing every time when you see this right um and so

**[06:15]** time when you see this right um and so

**[06:15]** time when you see this right um and so basically an ability to to just maintain

**[06:18]** basically an ability to to just maintain

**[06:18]** basically an ability to to just maintain and understand the learnings from that

**[06:20]** and understand the learnings from that

**[06:20]** and understand the learnings from that and use that to improve the agent in

**[06:22]** and use that to improve the agent in

**[06:22]** and use that to improve the agent in every future one and those were kind of

**[06:23]** every future one and those were kind of

**[06:23]** every future one and those were kind of the the big problems of the time, you

**[06:25]** the the big problems of the time, you

**[06:25]** the the big problems of the time, you know, and that was summer of last year.

**[06:27]** know, and that was summer of last year.

**[06:27]** know, and that was summer of last year. And around end of summer or fall or so,

**[06:30]** And around end of summer or fall or so,

**[06:30]** And around end of summer or fall or so, you know, I think the the the kind of

**[06:32]** you know, I think the the the kind of

**[06:32]** you know, I think the the the kind of big thing that started coming up was as

**[06:34]** big thing that started coming up was as

**[06:34]** big thing that started coming up was as these systems got more and more capable

**[06:36]** these systems got more and more capable

**[06:36]** these systems got more and more capable instead of just doing the most routine

**[06:38]** instead of just doing the most routine

**[06:38]** instead of just doing the most routine migrations, you could do, you know,

**[06:40]** migrations, you could do, you know,

**[06:40]** migrations, you could do, you know, these more still pretty isolated, but

**[06:42]** these more still pretty isolated, but

**[06:42]** these more still pretty isolated, but but but but a bit broader of these

**[06:44]** but but but a bit broader of these

**[06:44]** but but but a bit broader of these general kind of bugs or features where

**[06:47]** general kind of bugs or features where

**[06:47]** general kind of bugs or features where you can actually just tell it what you

**[06:49]** you can actually just tell it what you

**[06:49]** you can actually just tell it what you want to do and have you have it do it,

**[06:50]** want to do and have you have it do it,

**[06:50]** want to do and have you have it do it, right? And so for example, hey Devon, in

**[06:52]** right? And so for example, hey Devon, in

**[06:52]** right? And so for example, hey Devon, in this uh repo select dropdown, can you

**[06:55]** this uh repo select dropdown, can you

**[06:55]** this uh repo select dropdown, can you please just list the currently selected

**[06:56]** please just list the currently selected

**[06:56]** please just list the currently selected ones at the top? Like having the

**[06:57]** ones at the top? Like having the

**[06:57]** ones at the top? Like having the checkboxes throughout is just doesn't

**[06:59]** checkboxes throughout is just doesn't


### [07:00 - 08:00]

**[07:00]** checkboxes throughout is just doesn't really and and Devon will just go and do

**[07:01]** really and and Devon will just go and do

**[07:01]** really and and Devon will just go and do that, right? And so if you think about

**[07:03]** that, right? And so if you think about

**[07:03]** that, right? And so if you think about it, it's, you know, it's it's it's

**[07:05]** it, it's, you know, it's it's it's

**[07:05]** it, it's, you know, it's it's it's something like the kind of level of task

**[07:07]** something like the kind of level of task

**[07:07]** something like the kind of level of task that you would give an intern.

**[07:09]** that you would give an intern.

**[07:09]** that you would give an intern. And there are a few particular things

**[07:11]** And there are a few particular things

**[07:11]** And there are a few particular things that you have to solve for um with this.

**[07:13]** that you have to solve for um with this.

**[07:13]** that you have to solve for um with this. First of all, usually these these these

**[07:16]** First of all, usually these these these

**[07:16]** First of all, usually these these these changes are pretty isolated and pretty

**[07:17]** changes are pretty isolated and pretty

**[07:18]** changes are pretty isolated and pretty contained. And so it's one maybe two

**[07:19]** contained. And so it's one maybe two

**[07:19]** contained. And so it's one maybe two files that you really have to look at

**[07:21]** files that you really have to look at

**[07:21]** files that you really have to look at and change to do a task like this, but

**[07:23]** and change to do a task like this, but

**[07:23]** and change to do a task like this, but at least you do still need to be able to

**[07:24]** at least you do still need to be able to

**[07:24]** at least you do still need to be able to set up the repo and work with the repo,

**[07:26]** set up the repo and work with the repo,

**[07:26]** set up the repo and work with the repo, right? And so you want to be able to run

**[07:28]** right? And so you want to be able to run

**[07:28]** right? And so you want to be able to run lint, you want to be able to run CI, all

**[07:31]** lint, you want to be able to run CI, all

**[07:31]** lint, you want to be able to run CI, all of these other things. So, you know, to

**[07:32]** of these other things. So, you know, to

**[07:32]** of these other things. So, you know, to at least have the basic checks of

**[07:34]** at least have the basic checks of

**[07:34]** at least have the basic checks of whether things work. One of the big

**[07:36]** whether things work. One of the big

**[07:36]** whether things work. One of the big things that we built around then was the

**[07:38]** things that we built around then was the

**[07:38]** things that we built around then was the ability to really set up your repository

**[07:40]** ability to really set up your repository

**[07:40]** ability to really set up your repository uh ahead of time and build a snapshot um

**[07:43]** uh ahead of time and build a snapshot um

**[07:43]** uh ahead of time and build a snapshot um that that you could start off that you

**[07:45]** that that you could start off that you

**[07:45]** that that you could start off that you could reload that you could roll back

**[07:46]** could reload that you could roll back

**[07:46]** could reload that you could roll back and all of these kinds of primitives as

**[07:47]** and all of these kinds of primitives as

**[07:48]** and all of these kinds of primitives as well right so having this clean remote

**[07:50]** well right so having this clean remote

**[07:50]** well right so having this clean remote VM that could run all these things it

**[07:51]** VM that could run all these things it

**[07:51]** VM that could run all these things it could run your CI it could run your

**[07:53]** could run your CI it could run your

**[07:53]** could run your CI it could run your llinter uh and and so on um but that's

**[07:57]** llinter uh and and so on um but that's

**[07:57]** llinter uh and and so on um but that's when we started to really see I would

**[07:58]** when we started to really see I would

**[07:58]** when we started to really see I would say a bit more broad of value right I


### [08:00 - 09:00]

**[08:00]** say a bit more broad of value right I

**[08:00]** say a bit more broad of value right I mean migrations is one particular thing

**[08:02]** mean migrations is one particular thing

**[08:02]** mean migrations is one particular thing and for that particular thing we were

**[08:03]** and for that particular thing we were

**[08:03]** and for that particular thing we were showing a ton of value and then we

**[08:05]** showing a ton of value and then we

**[08:05]** showing a ton of value and then we started to see where you know with these

**[08:07]** started to see where you know with these

**[08:07]** started to see where you know with these bug fixes or things like that you would

**[08:08]** bug fixes or things like that you would

**[08:08]** bug fixes or things like that you would be able to just generally get value from

**[08:10]** be able to just generally get value from

**[08:10]** be able to just generally get value from Devon as as almost like a junior buddy

**[08:12]** Devon as as almost like a junior buddy

**[08:12]** Devon as as almost like a junior buddy of yours

**[08:14]** of yours

**[08:14]** of yours and then in the fall

**[08:16]** and then in the fall

**[08:16]** and then in the fall things really moved towards just much

**[08:18]** things really moved towards just much

**[08:18]** things really moved towards just much broader bugs and requests and here it's

**[08:21]** broader bugs and requests and here it's

**[08:21]** broader bugs and requests and here it's you know most most changes again you

**[08:24]** you know most most changes again you

**[08:24]** you know most most changes again you know you jumping another order of

**[08:26]** know you jumping another order of

**[08:26]** know you jumping another order of magnitude most changes don't just

**[08:28]** magnitude most changes don't just

**[08:28]** magnitude most changes don't just contain themselves to one file right

**[08:29]** contain themselves to one file right

**[08:29]** contain themselves to one file right often you have to go and look see what's

**[08:31]** often you have to go and look see what's

**[08:31]** often you have to go and look see what's going on you have to diagnose things you

**[08:33]** going on you have to diagnose things you

**[08:33]** going on you have to diagnose things you have to figure out what's happening you

**[08:34]** have to figure out what's happening you

**[08:34]** have to figure out what's happening you have to work across cross files and make

**[08:36]** have to work across cross files and make

**[08:36]** have to work across cross files and make the right changes. Often these changes

**[08:37]** the right changes. Often these changes

**[08:37]** the right changes. Often these changes are, you know, hundreds of lines if it's

**[08:39]** are, you know, hundreds of lines if it's

**[08:39]** are, you know, hundreds of lines if it's like, hey, I've got this bug. Let's

**[08:41]** like, hey, I've got this bug. Let's

**[08:41]** like, hey, I've got this bug. Let's figure out what's going on. Let's solve

**[08:42]** figure out what's going on. Let's solve

**[08:42]** figure out what's going on. Let's solve it. Right?

**[08:44]** it. Right?

**[08:44]** it. Right? And, you know, there there are a lot of

**[08:46]** And, you know, there there are a lot of

**[08:46]** And, you know, there there are a lot of things here that that really started to

**[08:47]** things here that that really started to

**[08:47]** things here that that really started to make sense and really started to be

**[08:49]** make sense and really started to be

**[08:49]** make sense and really started to be important, but but one in particular

**[08:50]** important, but but one in particular

**[08:50]** important, but but one in particular I'll just point out was there's a lot of

**[08:52]** I'll just point out was there's a lot of

**[08:52]** I'll just point out was there's a lot of stuff that you can do with not just

**[08:55]** stuff that you can do with not just

**[08:55]** stuff that you can do with not just looking at the code as text, but

**[08:57]** looking at the code as text, but

**[08:57]** looking at the code as text, but thinking of it as this whole hierarchy,

**[08:58]** thinking of it as this whole hierarchy,

**[08:58]** thinking of it as this whole hierarchy, right? So, so understanding call


### [09:00 - 10:00]

**[09:00]** right? So, so understanding call

**[09:00]** right? So, so understanding call hierarchies, running a language server,

**[09:02]** hierarchies, running a language server,

**[09:02]** hierarchies, running a language server, uh, is a big deal. you have git commit

**[09:04]** uh, is a big deal. you have git commit

**[09:04]** uh, is a big deal. you have git commit history which you can look at which

**[09:06]** history which you can look at which

**[09:06]** history which you can look at which informs how how these different files

**[09:07]** informs how how these different files

**[09:07]** informs how how these different files relate to one another. You have um um

**[09:11]** relate to one another. You have um um

**[09:11]** relate to one another. You have um um obviously you have like your llinter and

**[09:13]** obviously you have like your llinter and

**[09:13]** obviously you have like your llinter and things like that but but you're able to

**[09:14]** things like that but but you're able to

**[09:14]** things like that but but you're able to kind of reference things across files.

**[09:15]** kind of reference things across files.

**[09:15]** kind of reference things across files. And so like one of the big problems here

**[09:17]** And so like one of the big problems here

**[09:17]** And so like one of the big problems here I think was u kind of working with the

**[09:21]** I think was u kind of working with the

**[09:21]** I think was u kind of working with the context of it and getting to the point

**[09:23]** context of it and getting to the point

**[09:23]** context of it and getting to the point where it could make changes across

**[09:24]** where it could make changes across

**[09:24]** where it could make changes across several files. It could be consistent

**[09:26]** several files. It could be consistent

**[09:26]** several files. It could be consistent across those changes. It would be able

**[09:28]** across those changes. It would be able

**[09:28]** across those changes. It would be able to understand across the codebase. And

**[09:30]** to understand across the codebase. And

**[09:30]** to understand across the codebase. And here was really the point, I would say,

**[09:31]** here was really the point, I would say,

**[09:31]** here was really the point, I would say, where you started to be able to just tag

**[09:33]** where you started to be able to just tag

**[09:33]** where you started to be able to just tag it and have it do an issue and just have

**[09:35]** it and have it do an issue and just have

**[09:35]** it and have it do an issue and just have it build it for you. Um, and so Slack

**[09:37]** it build it for you. Um, and so Slack

**[09:37]** it build it for you. Um, and so Slack was a was, you know, a huge part of the

**[09:39]** was a was, you know, a huge part of the

**[09:39]** was a was, you know, a huge part of the workflow then. Um, and and it was just

**[09:42]** workflow then. Um, and and it was just

**[09:42]** workflow then. Um, and and it was just it it made sense because it's where you

**[09:44]** it it made sense because it's where you

**[09:44]** it it made sense because it's where you discuss your issues and it's where you

**[09:45]** discuss your issues and it's where you

**[09:45]** discuss your issues and it's where you set these things up, right? So you would

**[09:46]** set these things up, right? So you would

**[09:46]** set these things up, right? So you would tag Devon in Slack and say, "Hey, by the

**[09:48]** tag Devon in Slack and say, "Hey, by the

**[09:48]** tag Devon in Slack and say, "Hey, by the way, we've got this bug. Please take a

**[09:50]** way, we've got this bug. Please take a

**[09:50]** way, we've got this bug. Please take a look." Or, you know, could you please go

**[09:51]** look." Or, you know, could you please go

**[09:51]** look." Or, you know, could you please go build this thing? Uh, this is especially

**[09:54]** build this thing? Uh, this is especially

**[09:54]** build this thing? Uh, this is especially fun part for us because this is right

**[09:55]** fun part for us because this is right

**[09:55]** fun part for us because this is right around when we went GA. Uh, and a lot of

**[09:58]** around when we went GA. Uh, and a lot of

**[09:58]** around when we went GA. Uh, and a lot of that was because it was it got to the

**[09:59]** that was because it was it got to the

**[09:59]** that was because it was it got to the point where you truly could just get set


### [10:00 - 11:00]

**[10:01]** point where you truly could just get set

**[10:01]** point where you truly could just get set up with Devon and ask it a lot of these

**[10:03]** up with Devon and ask it a lot of these

**[10:03]** up with Devon and ask it a lot of these broad tasks and and just have it do it.

**[10:05]** broad tasks and and just have it do it.

**[10:05]** broad tasks and and just have it do it. Um, but but a lot of these, you know, a

**[10:07]** Um, but but a lot of these, you know, a

**[10:07]** Um, but but a lot of these, you know, a lot of the work that we did was around

**[10:10]** lot of the work that we did was around

**[10:10]** lot of the work that we did was around having Devon have better and better

**[10:12]** having Devon have better and better

**[10:12]** having Devon have better and better understanding of the codebase, right?

**[10:13]** understanding of the codebase, right?

**[10:13]** understanding of the codebase, right? And if you think about it, you know,

**[10:15]** And if you think about it, you know,

**[10:15]** And if you think about it, you know, from the human lens, it's the same way

**[10:16]** from the human lens, it's the same way

**[10:16]** from the human lens, it's the same way where on your first day on the job, for

**[10:18]** where on your first day on the job, for

**[10:18]** where on your first day on the job, for example, being super fresh in the

**[10:20]** example, being super fresh in the

**[10:20]** example, being super fresh in the codebase, it's kind of tough to know

**[10:21]** codebase, it's kind of tough to know

**[10:21]** codebase, it's kind of tough to know exactly what you're supposed to do. Like

**[10:23]** exactly what you're supposed to do. Like

**[10:23]** exactly what you're supposed to do. Like a lot of these details are things that

**[10:24]** a lot of these details are things that

**[10:24]** a lot of these details are things that you understand over time or that a

**[10:26]** you understand over time or that a

**[10:26]** you understand over time or that a representation of the codebase that you

**[10:27]** representation of the codebase that you

**[10:27]** representation of the codebase that you build over time, right? Um and Devon had

**[10:29]** build over time, right? Um and Devon had

**[10:29]** build over time, right? Um and Devon had to do the same thing and had to

**[10:31]** to do the same thing and had to

**[10:31]** to do the same thing and had to understand how do I plan this task out

**[10:33]** understand how do I plan this task out

**[10:33]** understand how do I plan this task out before I solve it? How do I understand

**[10:34]** before I solve it? How do I understand

**[10:34]** before I solve it? How do I understand all the files that need to be changed?

**[10:36]** all the files that need to be changed?

**[10:36]** all the files that need to be changed? How do I go from there and make that

**[10:37]** How do I go from there and make that

**[10:38]** How do I go from there and make that diff?

**[10:42]** And

**[10:42]** And around the spring of this year, um,

**[10:45]** around the spring of this year, um,

**[10:45]** around the spring of this year, um, again, every every gap is like two or 3

**[10:46]** again, every every gap is like two or 3

**[10:46]** again, every every gap is like two or 3 months. You know, we we got to an

**[10:48]** months. You know, we we got to an

**[10:48]** months. You know, we we got to an interesting point, which is once you

**[10:50]** interesting point, which is once you

**[10:50]** interesting point, which is once you start to get to harder and harder tasks,

**[10:53]** start to get to harder and harder tasks,

**[10:53]** start to get to harder and harder tasks, you as the human don't necessarily know

**[10:55]** you as the human don't necessarily know

**[10:55]** you as the human don't necessarily know everything that you want done at the

**[10:57]** everything that you want done at the

**[10:57]** everything that you want done at the time that you're giving the task, right?

**[10:58]** time that you're giving the task, right?

**[10:58]** time that you're giving the task, right? If you're saying, hey, you know, I I'd


### [11:00 - 12:00]

**[11:00]** If you're saying, hey, you know, I I'd

**[11:00]** If you're saying, hey, you know, I I'd like to go and um improve the

**[11:03]** like to go and um improve the

**[11:03]** like to go and um improve the architecture of this, or you know, this

**[11:04]** architecture of this, or you know, this

**[11:04]** architecture of this, or you know, this this function is slow. Like, let's let's

**[11:06]** this function is slow. Like, let's let's

**[11:06]** this function is slow. Like, let's let's profile it and look into it and see what

**[11:08]** profile it and look into it and see what

**[11:08]** profile it and look into it and see what needs to be done. or hey like you know

**[11:11]** needs to be done. or hey like you know

**[11:11]** needs to be done. or hey like you know we really should should handle this this

**[11:13]** we really should should handle this this

**[11:13]** we really should should handle this this error case better but like let's look at

**[11:15]** error case better but like let's look at

**[11:15]** error case better but like let's look at all the possibilities and see what we

**[11:17]** all the possibilities and see what we

**[11:17]** all the possibilities and see what we should you know what the right logic

**[11:18]** should you know what the right logic

**[11:18]** should you know what the right logic should be in each of these right and

**[11:20]** should be in each of these right and

**[11:20]** should be in each of these right and basically what it meant is that this

**[11:22]** basically what it meant is that this

**[11:22]** basically what it meant is that this whole idea of taking a twoline prompt or

**[11:23]** whole idea of taking a twoline prompt or

**[11:24]** whole idea of taking a twoline prompt or a threeline prompt or something and then

**[11:25]** a threeline prompt or something and then

**[11:25]** a threeline prompt or something and then just having that result in a a Devon

**[11:28]** just having that result in a a Devon

**[11:28]** just having that result in a a Devon task was was not sufficient and you

**[11:30]** task was was not sufficient and you

**[11:30]** task was was not sufficient and you wanted to really be able to work with

**[11:31]** wanted to really be able to work with

**[11:31]** wanted to really be able to work with Devon and specify a lot more and around

**[11:34]** Devon and specify a lot more and around

**[11:34]** Devon and specify a lot more and around this time along with this kind of like

**[11:36]** this time along with this kind of like

**[11:36]** this time along with this kind of like better codebase intelligence um we had a

**[11:38]** better codebase intelligence um we had a

**[11:38]** better codebase intelligence um we had a few different things that that that came

**[11:40]** few different things that that that came

**[11:40]** few different things that that that came up and so we released deep wiki for

**[11:41]** up and so we released deep wiki for

**[11:41]** up and so we released deep wiki for example. Um and the whole idea of deep

**[11:43]** example. Um and the whole idea of deep

**[11:43]** example. Um and the whole idea of deep wiki was you know funnily enough is

**[11:45]** wiki was you know funnily enough is

**[11:45]** wiki was you know funnily enough is devon had its own internal

**[11:46]** devon had its own internal

**[11:46]** devon had its own internal representation of the codebase but it

**[11:48]** representation of the codebase but it

**[11:48]** representation of the codebase but it turns out that for humans it was great

**[11:51]** turns out that for humans it was great

**[11:51]** turns out that for humans it was great to look at that too to be able to

**[11:52]** to look at that too to be able to

**[11:52]** to look at that too to be able to understand what was going on or to be

**[11:54]** understand what was going on or to be

**[11:54]** understand what was going on or to be able to ask questions quickly about the

**[11:55]** able to ask questions quickly about the

**[11:55]** able to ask questions quickly about the codebase. Um closely related to that was

**[11:58]** codebase. Um closely related to that was

**[11:58]** codebase. Um closely related to that was with search which is the ability to


### [12:00 - 13:00]

**[12:00]** with search which is the ability to

**[12:00]** with search which is the ability to really just ask questions about a

**[12:01]** really just ask questions about a

**[12:01]** really just ask questions about a codebase and understand um some some

**[12:04]** codebase and understand um some some

**[12:04]** codebase and understand um some some piece of this. And a lot of the workflow

**[12:06]** piece of this. And a lot of the workflow

**[12:06]** piece of this. And a lot of the workflow that really started to come up was

**[12:08]** that really started to come up was

**[12:08]** that really started to come up was actually basically this this more

**[12:09]** actually basically this this more

**[12:10]** actually basically this this more iterative workflow where the first thing

**[12:11]** iterative workflow where the first thing

**[12:11]** iterative workflow where the first thing that you would do is you would ask a few

**[12:13]** that you would do is you would ask a few

**[12:13]** that you would do is you would ask a few questions. You would understand you

**[12:14]** questions. You would understand you

**[12:14]** questions. You would understand you would basically have a more L2

**[12:16]** would basically have a more L2

**[12:16]** would basically have a more L2 experience where you can go explore the

**[12:18]** experience where you can go explore the

**[12:18]** experience where you can go explore the codebase with your agent,

**[12:20]** codebase with your agent,

**[12:20]** codebase with your agent, figure out what has to be done in the

**[12:22]** figure out what has to be done in the

**[12:22]** figure out what has to be done in the task and then set your agent off to go

**[12:24]** task and then set your agent off to go

**[12:24]** task and then set your agent off to go do that because for these more complex

**[12:26]** do that because for these more complex

**[12:26]** do that because for these more complex tasks you kind of needed that, right?

**[12:28]** tasks you kind of needed that, right?

**[12:28]** tasks you kind of needed that, right? Um and so so you know that was a I would

**[12:31]** Um and so so you know that was a I would

**[12:31]** Um and so so you know that was a I would say kind of like a big paradigm shift

**[12:32]** say kind of like a big paradigm shift

**[12:32]** say kind of like a big paradigm shift for us then is is understanding you know

**[12:34]** for us then is is understanding you know

**[12:34]** for us then is is understanding you know this is what also came along with Devon

**[12:35]** this is what also came along with Devon

**[12:35]** this is what also came along with Devon 2.0 for example and the in IDE

**[12:37]** 2.0 for example and the in IDE

**[12:37]** 2.0 for example and the in IDE experience where often yeah you want to

**[12:39]** experience where often yeah you want to

**[12:39]** experience where often yeah you want to be able to have points where you closely

**[12:42]** be able to have points where you closely

**[12:42]** be able to have points where you closely monitor Devon for 10% of the task 20% of

**[12:44]** monitor Devon for 10% of the task 20% of

**[12:44]** monitor Devon for 10% of the task 20% of the task and then have it do uh work on

**[12:47]** the task and then have it do uh work on

**[12:47]** the task and then have it do uh work on its own for the other 80 90%.

**[12:50]** its own for the other 80 90%.

**[12:50]** its own for the other 80 90%. Um, and then lastly, most recently in

**[12:53]** Um, and then lastly, most recently in

**[12:53]** Um, and then lastly, most recently in June, which is now, it was kind of,

**[12:56]** June, which is now, it was kind of,

**[12:56]** June, which is now, it was kind of, yeah, really the ability to just truly

**[12:58]** yeah, really the ability to just truly

**[12:58]** yeah, really the ability to just truly just kill your backlog and hand it a ton


### [13:00 - 14:00]

**[13:00]** just kill your backlog and hand it a ton

**[13:00]** just kill your backlog and hand it a ton of tasks and have it do all these at

**[13:02]** of tasks and have it do all these at

**[13:02]** of tasks and have it do all these at once. And, you know, if you think about

**[13:03]** once. And, you know, if you think about

**[13:03]** once. And, you know, if you think about this task, in many ways, I would say

**[13:04]** this task, in many ways, I would say

**[13:04]** this task, in many ways, I would say it's it's almost like a culmination of

**[13:06]** it's it's almost like a culmination of

**[13:06]** it's it's almost like a culmination of of many of these different things that

**[13:07]** of many of these different things that

**[13:07]** of many of these different things that that had to be done in the past. You

**[13:09]** that had to be done in the past. You

**[13:09]** that had to be done in the past. You have to work with all these systems.

**[13:10]** have to work with all these systems.

**[13:10]** have to work with all these systems. Obviously, you have to integrate into

**[13:11]** Obviously, you have to integrate into

**[13:11]** Obviously, you have to integrate into all these. Certainly, you want to be

**[13:12]** all these. Certainly, you want to be

**[13:12]** all these. Certainly, you want to be able to to work with linear or with Jira

**[13:15]** able to to work with linear or with Jira

**[13:15]** able to to work with linear or with Jira or systems like that, but you have to be

**[13:16]** or systems like that, but you have to be

**[13:16]** or systems like that, but you have to be able to scope out a task to understand

**[13:18]** able to scope out a task to understand

**[13:18]** able to scope out a task to understand what's meant by what's going on. You

**[13:20]** what's meant by what's going on. You

**[13:20]** what's meant by what's going on. You have to decide when to go to the human

**[13:22]** have to decide when to go to the human

**[13:22]** have to decide when to go to the human for more approval or for questions or

**[13:24]** for more approval or for questions or

**[13:24]** for more approval or for questions or things like that. You have to work

**[13:25]** things like that. You have to work

**[13:25]** things like that. You have to work across several different files. Often

**[13:27]** across several different files. Often

**[13:27]** across several different files. Often you have to understand even what repo is

**[13:30]** you have to understand even what repo is

**[13:30]** you have to understand even what repo is the right repo to make the change in if

**[13:31]** the right repo to make the change in if

**[13:31]** the right repo to make the change in if your if your org has multiple repos or

**[13:33]** your if your org has multiple repos or

**[13:33]** your if your org has multiple repos or what part of the codebase is the right

**[13:35]** what part of the codebase is the right

**[13:35]** what part of the codebase is the right part of the codebase that needs to

**[13:36]** part of the codebase that needs to

**[13:36]** part of the codebase that needs to change. Um, and to really get to the

**[13:38]** change. Um, and to really get to the

**[13:38]** change. Um, and to really get to the point where you can go and do this more

**[13:40]** point where you can go and do this more

**[13:40]** point where you can go and do this more autonomously,

**[13:42]** autonomously,

**[13:42]** autonomously, first of all, um, you have to have like

**[13:44]** first of all, um, you have to have like

**[13:44]** first of all, um, you have to have like a really great sense of confidence,

**[13:46]** a really great sense of confidence,

**[13:46]** a really great sense of confidence, right? And so, um, you know, rather than

**[13:48]** right? And so, um, you know, rather than

**[13:48]** right? And so, um, you know, rather than just going off and doing things

**[13:49]** just going off and doing things

**[13:49]** just going off and doing things immediately, you have to be able to say,

**[13:51]** immediately, you have to be able to say,

**[13:51]** immediately, you have to be able to say, okay, I'm quite sure that this is the

**[13:53]** okay, I'm quite sure that this is the

**[13:53]** okay, I'm quite sure that this is the task and I'm going to go execute it now

**[13:55]** task and I'm going to go execute it now

**[13:55]** task and I'm going to go execute it now versus I don't understand what's going

**[13:57]** versus I don't understand what's going

**[13:57]** versus I don't understand what's going on. Human, please give me help.

**[13:59]** on. Human, please give me help.


### [14:00 - 15:00]

**[14:00]** on. Human, please give me help. Basically, right? But but the other

**[14:01]** Basically, right? But but the other

**[14:02]** Basically, right? But but the other piece of it is this is I think the era

**[14:05]** piece of it is this is I think the era

**[14:05]** piece of it is this is I think the era where testing and this asynchronous

**[14:06]** where testing and this asynchronous

**[14:06]** where testing and this asynchronous testing gets really really important

**[14:08]** testing gets really really important

**[14:08]** testing gets really really important right which is if you want something to

**[14:10]** right which is if you want something to

**[14:10]** right which is if you want something to just deliver entire PRs for you for

**[14:12]** just deliver entire PRs for you for

**[14:12]** just deliver entire PRs for you for tasks that you do especially for these

**[14:14]** tasks that you do especially for these

**[14:14]** tasks that you do especially for these larger tasks you want to know that it is

**[14:17]** larger tasks you want to know that it is

**[14:17]** larger tasks you want to know that it is can can test it itself and often the

**[14:19]** can can test it itself and often the

**[14:19]** can can test it itself and often the agent actually needs this iterative loop

**[14:21]** agent actually needs this iterative loop

**[14:21]** agent actually needs this iterative loop to be able to go and do that right so it

**[14:23]** to be able to go and do that right so it

**[14:23]** to be able to go and do that right so it needs to be able to run all the code

**[14:24]** needs to be able to run all the code

**[14:24]** needs to be able to run all the code locally it needs to know what to test it

**[14:26]** locally it needs to know what to test it

**[14:26]** locally it needs to know what to test it needs to know what to look for um and in

**[14:28]** needs to know what to look for um and in

**[14:28]** needs to know what to look for um and in many ways it's just a much higher

**[14:30]** many ways it's just a much higher

**[14:30]** many ways it's just a much higher context problem to solve for right is

**[14:31]** context problem to solve for right is

**[14:31]** context problem to solve for right is this testing itself.

**[14:34]** this testing itself.

**[14:34]** this testing itself. And that brings us to now. And obviously

**[14:37]** And that brings us to now. And obviously

**[14:37]** And that brings us to now. And obviously it's a it's a pretty fun time to see

**[14:38]** it's a it's a pretty fun time to see

**[14:38]** it's a it's a pretty fun time to see because now what we're thinking about is

**[14:40]** because now what we're thinking about is

**[14:40]** because now what we're thinking about is hey maybe if instead of doing it just

**[14:42]** hey maybe if instead of doing it just

**[14:42]** hey maybe if instead of doing it just one task it's you know how how do we

**[14:44]** one task it's you know how how do we

**[14:44]** one task it's you know how how do we think about tackling an entire project

**[14:45]** think about tackling an entire project

**[14:46]** think about tackling an entire project right and after we do a project you know

**[14:47]** right and after we do a project you know

**[14:48]** right and after we do a project you know what what goes after that a and maybe

**[14:50]** what what goes after that a and maybe

**[14:50]** what what goes after that a and maybe one point that I would just make here is

**[14:53]** one point that I would just make here is

**[14:53]** one point that I would just make here is we talk about all these two X's you know

**[14:55]** we talk about all these two X's you know

**[14:55]** we talk about all these two X's you know that happen every couple months and I

**[14:57]** that happen every couple months and I

**[14:58]** that happen every couple months and I think from a kind of cosmic perspective


### [15:00 - 16:00]

**[15:00]** think from a kind of cosmic perspective

**[15:00]** think from a kind of cosmic perspective all the two X's look the right but in

**[15:02]** all the two X's look the right but in

**[15:02]** all the two X's look the right but in practice every 2x actually is a

**[15:03]** practice every 2x actually is a

**[15:03]** practice every 2x actually is a different one right and so when we were

**[15:05]** different one right and so when we were

**[15:05]** different one right and so when we were just doing you

**[15:06]** just doing you

**[15:06]** just doing you tab completion, line, single line

**[15:08]** tab completion, line, single line

**[15:08]** tab completion, line, single line completion. It really was just a text

**[15:10]** completion. It really was just a text

**[15:10]** completion. It really was just a text problem. It is just like taken the

**[15:12]** problem. It is just like taken the

**[15:12]** problem. It is just like taken the single file so far and just predict what

**[15:14]** single file so far and just predict what

**[15:14]** single file so far and just predict what the line is next. Right? Over the last

**[15:16]** the line is next. Right? Over the last

**[15:16]** the line is next. Right? Over the last year or year and a half, we've had to

**[15:17]** year or year and a half, we've had to

**[15:17]** year or year and a half, we've had to think about so much more. How do how do

**[15:19]** think about so much more. How do how do

**[15:19]** think about so much more. How do how do you work with the human in linear or

**[15:21]** you work with the human in linear or

**[15:21]** you work with the human in linear or slack or how do you take in feedback or

**[15:23]** slack or how do you take in feedback or

**[15:23]** slack or how do you take in feedback or steering? Um how how do you help the

**[15:25]** steering? Um how how do you help the

**[15:25]** steering? Um how how do you help the human plan out and do all these things,

**[15:27]** human plan out and do all these things,

**[15:27]** human plan out and do all these things, right? And moreover, obviously, there's

**[15:29]** right? And moreover, obviously, there's

**[15:29]** right? And moreover, obviously, there's a ton of the the tooling and the

**[15:31]** a ton of the the tooling and the

**[15:31]** a ton of the the tooling and the capabilities work that have to be done

**[15:32]** capabilities work that have to be done

**[15:32]** capabilities work that have to be done of how does how does Devon test on its

**[15:35]** of how does how does Devon test on its

**[15:35]** of how does how does Devon test on its own? How does Devon um uh you know make

**[15:38]** own? How does Devon um uh you know make

**[15:38]** own? How does Devon um uh you know make a lot of these longer term decisions on

**[15:39]** a lot of these longer term decisions on

**[15:40]** a lot of these longer term decisions on its own? How does it debug its own

**[15:42]** its own? How does it debug its own

**[15:42]** its own? How does it debug its own outputs or or run the right shell

**[15:44]** outputs or or run the right shell

**[15:44]** outputs or or run the right shell commands to figure out what the feedback

**[15:45]** commands to figure out what the feedback

**[15:45]** commands to figure out what the feedback is uh and go from there? And so it's

**[15:48]** is uh and go from there? And so it's

**[15:48]** is uh and go from there? And so it's super exciting now that there's a lot

**[15:49]** super exciting now that there's a lot

**[15:49]** super exciting now that there's a lot more uh there's a lot more coding agents

**[15:51]** more uh there's a lot more coding agents

**[15:51]** more uh there's a lot more coding agents in the space. It's uh it's it's very fun

**[15:52]** in the space. It's uh it's it's very fun

**[15:52]** in the space. It's uh it's it's very fun to see and I think that you know we

**[15:55]** to see and I think that you know we

**[15:55]** to see and I think that you know we we're going to see another 16 to 64x

**[15:57]** we're going to see another 16 to 64x

**[15:57]** we're going to see another 16 to 64x over the next 12 months as well and uh


### [16:00 - 17:00]

**[16:00]** over the next 12 months as well and uh

**[16:00]** over the next 12 months as well and uh and so yeah super super excited.

**[16:03]** and so yeah super super excited.

**[16:03]** and so yeah super super excited. Awesome. Well, that's all. Thank you

**[16:04]** Awesome. Well, that's all. Thank you

**[16:04]** Awesome. Well, that's all. Thank you guys so much for having me.

**[16:06]** guys so much for having me.

**[16:06]** guys so much for having me. [Music]


