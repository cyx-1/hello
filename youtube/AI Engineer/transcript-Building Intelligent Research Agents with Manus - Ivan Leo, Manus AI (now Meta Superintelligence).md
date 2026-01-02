# Building Intelligent Research Agents with Manus - Ivan Leo, Manus AI (now Meta Superintelligence)

**Video URL:** https://www.youtube.com/watch?v=xz0-brt56L8

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** Yeah, I think I can just start. Um so

**[00:23]** Yeah, I think I can just start. Um so the way this workshop will just be run

**[00:24]** the way this workshop will just be run

**[00:24]** the way this workshop will just be run is we'll show a few demos of what we

**[00:26]** is we'll show a few demos of what we

**[00:26]** is we'll show a few demos of what we built with Manis what we have at the

**[00:29]** built with Manis what we have at the

**[00:29]** built with Manis what we have at the moment and then um if you guys have any

**[00:31]** moment and then um if you guys have any

**[00:31]** moment and then um if you guys have any questions at any point in time feel free

**[00:32]** questions at any point in time feel free

**[00:32]** questions at any point in time feel free to stop me um throughout this whole

**[00:34]** to stop me um throughout this whole

**[00:34]** to stop me um throughout this whole workshop what we're going to be using is

**[00:35]** workshop what we're going to be using is

**[00:36]** workshop what we're going to be using is the new manus API and it will go

**[00:37]** the new manus API and it will go

**[00:38]** the new manus API and it will go basically will reproduce our original

**[00:39]** basically will reproduce our original

**[00:39]** basically will reproduce our original Slackbot um so if you use our new Madis

**[00:42]** Slackbot um so if you use our new Madis

**[00:42]** Slackbot um so if you use our new Madis app you can actually now use Madness in

**[00:44]** app you can actually now use Madness in

**[00:44]** app you can actually now use Madness in Slack uh so hopefully it works since I'm

**[00:46]** Slack uh so hopefully it works since I'm

**[00:46]** Slack uh so hopefully it works since I'm doing it live I'm a little worried but

**[00:49]** doing it live I'm a little worried but

**[00:49]** doing it live I'm a little worried but uh let's see

**[00:51]** uh let's see

**[00:51]** uh let's see So

**[00:53]** So

**[00:53]** So I think a common question that a lot of

**[00:54]** I think a common question that a lot of

**[00:54]** I think a common question that a lot of people are asking is what is manis and

**[00:56]** people are asking is what is manis and

**[00:56]** people are asking is what is manis and what does manness actually do right

**[00:58]** what does manness actually do right

**[00:58]** what does manness actually do right which is quite fair because at this


### [01:00 - 02:00]

**[01:01]** which is quite fair because at this

**[01:01]** which is quite fair because at this point we kind of do everything. If you

**[01:03]** point we kind of do everything. If you

**[01:03]** point we kind of do everything. If you go to our website uh you see this really

**[01:05]** go to our website uh you see this really

**[01:05]** go to our website uh you see this really long description that says manis is the

**[01:07]** long description that says manis is the

**[01:08]** long description that says manis is the action engine that goes beyond answers

**[01:10]** action engine that goes beyond answers

**[01:10]** action engine that goes beyond answers to execute task automate workflows

**[01:12]** to execute task automate workflows

**[01:12]** to execute task automate workflows extend human reach. Um, if you search

**[01:15]** extend human reach. Um, if you search

**[01:15]** extend human reach. Um, if you search for what is Manus and the new

**[01:17]** for what is Manus and the new

**[01:17]** for what is Manus and the new announcements that we've made, you may

**[01:18]** announcements that we've made, you may

**[01:18]** announcements that we've made, you may have seen Madness 1.5, manus 1.5 flight

**[01:21]** have seen Madness 1.5, manus 1.5 flight

**[01:21]** have seen Madness 1.5, manus 1.5 flight saying that we're now faster. Um,

**[01:24]** saying that we're now faster. Um,

**[01:24]** saying that we're now faster. Um, there's an increase in quality gain,

**[01:26]** there's an increase in quality gain,

**[01:26]** there's an increase in quality gain, some user satisfaction increase, and

**[01:28]** some user satisfaction increase, and

**[01:28]** some user satisfaction increase, and that we've rearchitected our models. Um,

**[01:31]** that we've rearchitected our models. Um,

**[01:31]** that we've rearchitected our models. Um, or you might just seen a lot of stuff

**[01:33]** or you might just seen a lot of stuff

**[01:33]** or you might just seen a lot of stuff that we talked about where we talked

**[01:34]** that we talked about where we talked

**[01:34]** that we talked about where we talked about the fact that building AI agents

**[01:35]** about the fact that building AI agents

**[01:35]** about the fact that building AI agents is just really difficult, right? And

**[01:37]** is just really difficult, right? And

**[01:37]** is just really difficult, right? And it's something we've learned as we

**[01:38]** it's something we've learned as we

**[01:38]** it's something we've learned as we scaled the number of conversations that

**[01:40]** scaled the number of conversations that

**[01:40]** scaled the number of conversations that we have every day to millions and and

**[01:42]** we have every day to millions and and

**[01:42]** we have every day to millions and and beyond, right? Because now we have

**[01:44]** beyond, right? Because now we have

**[01:44]** beyond, right? Because now we have things like infrastructure, we have

**[01:46]** things like infrastructure, we have

**[01:46]** things like infrastructure, we have sandboxes, we have reliability, and all

**[01:48]** sandboxes, we have reliability, and all

**[01:48]** sandboxes, we have reliability, and all these different like considerations to

**[01:50]** these different like considerations to

**[01:50]** these different like considerations to take care of.

**[01:51]** take care of.

**[01:52]** take care of. But really what we want to do at Manis

**[01:53]** But really what we want to do at Manis

**[01:53]** But really what we want to do at Manis is build a general AI agent that you

**[01:56]** is build a general AI agent that you

**[01:56]** is build a general AI agent that you want to use in a variety of different

**[01:57]** want to use in a variety of different

**[01:57]** want to use in a variety of different ways. And we really want to meet users

**[01:59]** ways. And we really want to meet users

**[01:59]** ways. And we really want to meet users where they're at. And from day one,


### [02:00 - 03:00]

**[02:01]** where they're at. And from day one,

**[02:01]** where they're at. And from day one, we've been designing Manners with this

**[02:02]** we've been designing Manners with this

**[02:02]** we've been designing Manners with this in mind. Whether you like to use Mannis

**[02:04]** in mind. Whether you like to use Mannis

**[02:04]** in mind. Whether you like to use Mannis in your mailbox, whether you like it in

**[02:06]** in your mailbox, whether you like it in

**[02:06]** in your mailbox, whether you like it in Slack, whether you have your own custom

**[02:08]** Slack, whether you have your own custom

**[02:08]** Slack, whether you have your own custom programmatic workflow or you just like

**[02:10]** programmatic workflow or you just like

**[02:10]** programmatic workflow or you just like to use the iOS app on the go, which I

**[02:12]** to use the iOS app on the go, which I

**[02:12]** to use the iOS app on the go, which I quite enjoy. Um, we've kind of built

**[02:15]** quite enjoy. Um, we've kind of built

**[02:15]** quite enjoy. Um, we've kind of built Manis to do that. And because of that,

**[02:19]** Manis to do that. And because of that,

**[02:19]** Manis to do that. And because of that, um, we have a lot of different ways to

**[02:21]** um, we have a lot of different ways to

**[02:21]** um, we have a lot of different ways to use Manis. Currently, we have the web

**[02:24]** use Manis. Currently, we have the web

**[02:24]** use Manis. Currently, we have the web application, we have the Slack app, we

**[02:26]** application, we have the Slack app, we

**[02:26]** application, we have the Slack app, we have the API that we just launched,

**[02:28]** have the API that we just launched,

**[02:28]** have the API that we just launched, which we'll be working through today. We

**[02:30]** which we'll be working through today. We

**[02:30]** which we'll be working through today. We have a new browser operator. We have two

**[02:33]** have a new browser operator. We have two

**[02:33]** have a new browser operator. We have two days ago we launched a new Microsoft 365

**[02:36]** days ago we launched a new Microsoft 365

**[02:36]** days ago we launched a new Microsoft 365 integration which means that in the far

**[02:38]** integration which means that in the far

**[02:38]** integration which means that in the far future or in the near future hopefully

**[02:40]** future or in the near future hopefully

**[02:40]** future or in the near future hopefully um when you're writing a word document

**[02:42]** um when you're writing a word document

**[02:42]** um when you're writing a word document or you're doing a presentation or you're

**[02:44]** or you're doing a presentation or you're

**[02:44]** or you're doing a presentation or you're doing anything in in the Microsoft suite

**[02:46]** doing anything in in the Microsoft suite

**[02:46]** doing anything in in the Microsoft suite if you just add mattis uh we'll edit

**[02:48]** if you just add mattis uh we'll edit

**[02:48]** if you just add mattis uh we'll edit your powerpoints we'll fix your j your

**[02:51]** your powerpoints we'll fix your j your

**[02:51]** your powerpoints we'll fix your j your janky excel uh templates or you know

**[02:54]** janky excel uh templates or you know

**[02:54]** janky excel uh templates or you know just whatever needs to be done. And

**[02:55]** just whatever needs to be done. And

**[02:55]** just whatever needs to be done. And lastly we also have mail madness.

**[02:58]** lastly we also have mail madness.

**[02:58]** lastly we also have mail madness. And so I'll just be walking through four


### [03:00 - 04:00]

**[03:00]** And so I'll just be walking through four

**[03:00]** And so I'll just be walking through four different demos that we built with Manis

**[03:02]** different demos that we built with Manis

**[03:02]** different demos that we built with Manis and you can kind of see what we've been

**[03:03]** and you can kind of see what we've been

**[03:04]** and you can kind of see what we've been building for the last few months since

**[03:05]** building for the last few months since

**[03:05]** building for the last few months since we launched Manis 1.5.

**[03:09]** we launched Manis 1.5.

**[03:09]** we launched Manis 1.5. One of the things that I Let me see if

**[03:12]** One of the things that I Let me see if

**[03:12]** One of the things that I Let me see if this works. Right. So I've been learning

**[03:15]** this works. Right. So I've been learning

**[03:15]** this works. Right. So I've been learning French for about a year and honestly

**[03:17]** French for about a year and honestly

**[03:17]** French for about a year and honestly speaking I I'm pretty bad at it. It's

**[03:20]** speaking I I'm pretty bad at it. It's

**[03:20]** speaking I I'm pretty bad at it. It's not an easy language and what I really

**[03:23]** not an easy language and what I really

**[03:23]** not an easy language and what I really wanted to do was to find a way whereby I

**[03:25]** wanted to do was to find a way whereby I

**[03:25]** wanted to do was to find a way whereby I could practice it every day. as managers

**[03:27]** could practice it every day. as managers

**[03:27]** could practice it every day. as managers to build me an application where you

**[03:29]** to build me an application where you

**[03:29]** to build me an application where you know I could practice this and so the

**[03:32]** know I could practice this and so the

**[03:32]** know I could practice this and so the way it works is that you know throughout

**[03:33]** way it works is that you know throughout

**[03:33]** way it works is that you know throughout my day on my on my phone I'm just going

**[03:35]** my day on my on my phone I'm just going

**[03:35]** my day on my on my phone I'm just going to key in a bunch of random prompts or

**[03:37]** to key in a bunch of random prompts or

**[03:37]** to key in a bunch of random prompts or random things in mind like hey today I

**[03:39]** random things in mind like hey today I

**[03:39]** random things in mind like hey today I had this thought today I'm stressed

**[03:40]** had this thought today I'm stressed

**[03:40]** had this thought today I'm stressed about this workshop that I'm currently

**[03:42]** about this workshop that I'm currently

**[03:42]** about this workshop that I'm currently conducting and once you key this in

**[03:45]** conducting and once you key this in

**[03:45]** conducting and once you key this in manus then takes a language model and

**[03:47]** manus then takes a language model and

**[03:47]** manus then takes a language model and finds the exact problems with what I've

**[03:49]** finds the exact problems with what I've

**[03:49]** finds the exact problems with what I've written for example over here you can

**[03:51]** written for example over here you can

**[03:51]** written for example over here you can see that there's an inline correction

**[03:52]** see that there's an inline correction

**[03:52]** see that there's an inline correction here whereby you know life is live

**[03:55]** here whereby you know life is live

**[03:55]** here whereby you know life is live forward but understood backwards, right?

**[03:57]** forward but understood backwards, right?

**[03:57]** forward but understood backwards, right? And manice is nice enough to give me a


### [04:00 - 05:00]

**[04:00]** And manice is nice enough to give me a

**[04:00]** And manice is nice enough to give me a entire corrected version. But let's say

**[04:02]** entire corrected version. But let's say

**[04:02]** entire corrected version. But let's say for example, I don't quite know what

**[04:03]** for example, I don't quite know what

**[04:03]** for example, I don't quite know what this word means. Well, I can just add it

**[04:06]** this word means. Well, I can just add it

**[04:06]** this word means. Well, I can just add it over here and say what is defy,

**[04:09]** over here and say what is defy,

**[04:09]** over here and say what is defy, right?

**[04:10]** right?

**[04:10]** right? And this is because every single Manis

**[04:12]** And this is because every single Manis

**[04:12]** And this is because every single Manis web application ships with a fully

**[04:14]** web application ships with a fully

**[04:14]** web application ships with a fully featured language model that you can

**[04:17]** featured language model that you can

**[04:17]** featured language model that you can call whether it's structured outputs

**[04:19]** call whether it's structured outputs

**[04:19]** call whether it's structured outputs that you want to use whether it's

**[04:21]** that you want to use whether it's

**[04:21]** that you want to use whether it's whisper to transcribe audio or even in

**[04:23]** whisper to transcribe audio or even in

**[04:23]** whisper to transcribe audio or even in this case just you know inline

**[04:25]** this case just you know inline

**[04:25]** this case just you know inline corrections with structured outputs. Um

**[04:27]** corrections with structured outputs. Um

**[04:27]** corrections with structured outputs. Um you can even integrate any sort of

**[04:29]** you can even integrate any sort of

**[04:29]** you can even integrate any sort of provider you care about. In this case I

**[04:31]** provider you care about. In this case I

**[04:31]** provider you care about. In this case I chose to use 11 labs because I have some

**[04:33]** chose to use 11 labs because I have some

**[04:33]** chose to use 11 labs because I have some extra credits and

**[04:35]** extra credits and

**[04:35]** extra credits and hope this works.

**[04:44]** So the beauty about this is that I

**[04:44]** So the beauty about this is that I didn't do a single thing and actually

**[04:46]** didn't do a single thing and actually

**[04:46]** didn't do a single thing and actually the the cool part that I enjoy is that

**[04:48]** the the cool part that I enjoy is that

**[04:48]** the the cool part that I enjoy is that as I'm interacting with this it kind of

**[04:50]** as I'm interacting with this it kind of

**[04:50]** as I'm interacting with this it kind of creates a profile for me. It seems that

**[04:52]** creates a profile for me. It seems that

**[04:52]** creates a profile for me. It seems that you're 28 working at manners where you

**[04:54]** you're 28 working at manners where you

**[04:54]** you're 28 working at manners where you build agents and hey like you know you

**[04:56]** build agents and hey like you know you

**[04:56]** build agents and hey like you know you your biggest strength is your

**[04:57]** your biggest strength is your

**[04:57]** your biggest strength is your willingness to tackle a lot of these

**[04:59]** willingness to tackle a lot of these

**[04:59]** willingness to tackle a lot of these abstract ideas and but you're really bad


### [05:00 - 06:00]

**[05:01]** abstract ideas and but you're really bad

**[05:01]** abstract ideas and but you're really bad at anything related to distance and time

**[05:03]** at anything related to distance and time

**[05:03]** at anything related to distance and time which I get but the beauty about this is

**[05:06]** which I get but the beauty about this is

**[05:06]** which I get but the beauty about this is that with you know manis like with new 1

**[05:10]** that with you know manis like with new 1

**[05:10]** that with you know manis like with new 1 manus 1.5 you're able to build these

**[05:11]** manus 1.5 you're able to build these

**[05:11]** manus 1.5 you're able to build these really complex operations from scratch

**[05:14]** really complex operations from scratch

**[05:14]** really complex operations from scratch and you know I think that's pretty cool.

**[05:17]** and you know I think that's pretty cool.

**[05:17]** and you know I think that's pretty cool. I would never have bothered to code this

**[05:18]** I would never have bothered to code this

**[05:18]** I would never have bothered to code this up. Oh, sorry.

**[05:19]** up. Oh, sorry.

**[05:19]** up. Oh, sorry. >> Was that part of Manus' settings or the

**[05:22]** >> Was that part of Manus' settings or the

**[05:22]** >> Was that part of Manus' settings or the app?

**[05:22]** app?

**[05:22]** app? >> Uh, so this was just me prompting Manis

**[05:25]** >> Uh, so this was just me prompting Manis

**[05:25]** >> Uh, so this was just me prompting Manis on the go as I was bought in between

**[05:26]** on the go as I was bought in between

**[05:26]** on the go as I was bought in between talks at AIE. Um, so

**[05:30]** talks at AIE. Um, so

**[05:30]** talks at AIE. Um, so >> user preference.

**[05:30]** >> user preference.

**[05:30]** >> user preference. >> Yeah. Yeah. So this is just me. I just

**[05:32]** >> Yeah. Yeah. So this is just me. I just

**[05:32]** >> Yeah. Yeah. So this is just me. I just told Manis, hey, can you keep in mind

**[05:34]** told Manis, hey, can you keep in mind

**[05:34]** told Manis, hey, can you keep in mind because you know I would say things

**[05:35]** because you know I would say things

**[05:35]** because you know I would say things about myself like, oh, I have a dog,

**[05:37]** about myself like, oh, I have a dog,

**[05:37]** about myself like, oh, I have a dog, whatnot. But in languages like French,

**[05:40]** whatnot. But in languages like French,

**[05:40]** whatnot. But in languages like French, you know, you need to bear in mind like

**[05:41]** you know, you need to bear in mind like

**[05:41]** you know, you need to bear in mind like what's your gender? You need to have all

**[05:43]** what's your gender? You need to have all

**[05:43]** what's your gender? You need to have all these like agreements. And it's kind of

**[05:44]** these like agreements. And it's kind of

**[05:44]** these like agreements. And it's kind of nice when you get like writing ideas on

**[05:46]** nice when you get like writing ideas on

**[05:46]** nice when you get like writing ideas on top that Manis gives every day or the

**[05:48]** top that Manis gives every day or the

**[05:48]** top that Manis gives every day or the language model we invoke every day um

**[05:51]** language model we invoke every day um

**[05:51]** language model we invoke every day um that gives you suggestions on what to

**[05:52]** that gives you suggestions on what to

**[05:52]** that gives you suggestions on what to write.

**[05:54]** write.

**[05:54]** write. And so this is an example of what the

**[05:56]** And so this is an example of what the

**[05:56]** And so this is an example of what the new web development platform can do. Let

**[05:59]** new web development platform can do. Let

**[05:59]** new web development platform can do. Let me just back to my slides. So another


### [06:00 - 07:00]

**[06:02]** me just back to my slides. So another

**[06:02]** me just back to my slides. So another thing that we can do is mailman where we

**[06:03]** thing that we can do is mailman where we

**[06:03]** thing that we can do is mailman where we can use the app. So for example if I'm

**[06:06]** can use the app. So for example if I'm

**[06:06]** can use the app. So for example if I'm using my phone uh let me try to connect

**[06:09]** using my phone uh let me try to connect

**[06:09]** using my phone uh let me try to connect it right now. So say for example here

**[06:12]** it right now. So say for example here

**[06:12]** it right now. So say for example here let's say we connect to my phone and we

**[06:13]** let's say we connect to my phone and we

**[06:13]** let's say we connect to my phone and we go like let's say I have a morning task

**[06:16]** go like let's say I have a morning task

**[06:16]** go like let's say I have a morning task at data do right um and you can just do

**[06:20]** at data do right um and you can just do

**[06:20]** at data do right um and you can just do things like maybe I just want to for

**[06:22]** things like maybe I just want to for

**[06:22]** things like maybe I just want to for this to reply and just say like

**[06:26]** this to reply and just say like

**[06:26]** this to reply and just say like uh I think my keyboard is kind of

**[06:28]** uh I think my keyboard is kind of

**[06:28]** uh I think my keyboard is kind of disabled on the screen sharing for some

**[06:29]** disabled on the screen sharing for some

**[06:30]** disabled on the screen sharing for some weird reason but basically um you're

**[06:32]** weird reason but basically um you're

**[06:32]** weird reason but basically um you're able to essentially take a lot of these

**[06:34]** able to essentially take a lot of these

**[06:34]** able to essentially take a lot of these task and get manage to do them for you

**[06:36]** task and get manage to do them for you

**[06:36]** task and get manage to do them for you right and this is an example of how you

**[06:39]** right and this is an example of how you

**[06:39]** right and this is an example of how you we're able to meet users where they're

**[06:41]** we're able to meet users where they're

**[06:41]** we're able to meet users where they're at. The newest one which I think is

**[06:43]** at. The newest one which I think is

**[06:43]** at. The newest one which I think is pretty cool is our new browser operator.

**[06:46]** pretty cool is our new browser operator.

**[06:46]** pretty cool is our new browser operator. And so I think let me just boot up the

**[06:48]** And so I think let me just boot up the

**[06:48]** And so I think let me just boot up the Madness application.

**[06:50]** Madness application.

**[06:50]** Madness application. And so

**[06:52]** And so

**[06:52]** And so let's say for example we can say, "Hey

**[06:54]** let's say for example we can say, "Hey

**[06:54]** let's say for example we can say, "Hey man, I'm currently at the AWS Hang 27 in

**[06:58]** man, I'm currently at the AWS Hang 27 in

**[06:58]** man, I'm currently at the AWS Hang 27 in New York. I would love to get a coffee


### [07:00 - 08:00]

**[07:00]** New York. I would love to get a coffee

**[07:00]** New York. I would love to get a coffee after this. I'm jetlagged from Singapore

**[07:01]** after this. I'm jetlagged from Singapore

**[07:01]** after this. I'm jetlagged from Singapore where I've flown over 20 hours and I

**[07:03]** where I've flown over 20 hours and I

**[07:04]** where I've flown over 20 hours and I just want something really general. I

**[07:05]** just want something really general. I

**[07:05]** just want something really general. I just really simple coffee. I just want

**[07:07]** just really simple coffee. I just want

**[07:07]** just really simple coffee. I just want to drop by and and grab something. I'm

**[07:10]** to drop by and and grab something. I'm

**[07:10]** to drop by and and grab something. I'm not pretty. I kind of just want

**[07:12]** not pretty. I kind of just want

**[07:12]** not pretty. I kind of just want something simple, maybe an Americano,

**[07:13]** something simple, maybe an Americano,

**[07:13]** something simple, maybe an Americano, and that should be good,

**[07:16]** and that should be good,

**[07:16]** and that should be good, right? And so what you actually see is

**[07:18]** right? And so what you actually see is

**[07:18]** right? And so what you actually see is that as Mannis is executing a lot of

**[07:20]** that as Mannis is executing a lot of

**[07:20]** that as Mannis is executing a lot of this with the new remote browser

**[07:21]** this with the new remote browser

**[07:21]** this with the new remote browser operator, um it'll think for a while. It

**[07:23]** operator, um it'll think for a while. It

**[07:23]** operator, um it'll think for a while. It go through a bunch of different things

**[07:25]** go through a bunch of different things

**[07:25]** go through a bunch of different things and it'll actually kickstart a browser

**[07:27]** and it'll actually kickstart a browser

**[07:27]** and it'll actually kickstart a browser tab on my computer that I've set it up

**[07:29]** tab on my computer that I've set it up

**[07:29]** tab on my computer that I've set it up on. So what this means is that for you

**[07:32]** on. So what this means is that for you

**[07:32]** on. So what this means is that for you if you're using any sort of thing like

**[07:33]** if you're using any sort of thing like

**[07:33]** if you're using any sort of thing like LinkedIn, if you're using like um you

**[07:36]** LinkedIn, if you're using like um you

**[07:36]** LinkedIn, if you're using like um you know your Instagram, you have all these

**[07:38]** know your Instagram, you have all these

**[07:38]** know your Instagram, you have all these like platforms you're logged in that you

**[07:39]** like platforms you're logged in that you

**[07:39]** like platforms you're logged in that you can't access through a sandbox browser

**[07:41]** can't access through a sandbox browser

**[07:42]** can't access through a sandbox browser like browser base. This completely

**[07:43]** like browser base. This completely

**[07:44]** like browser base. This completely changes like everything that you're

**[07:45]** changes like everything that you're

**[07:45]** changes like everything that you're using right because now Oh

**[07:50]** using right because now Oh

**[07:50]** using right because now Oh man, listen. My bad. Man, can you use my

**[07:54]** man, listen. My bad. Man, can you use my

**[07:54]** man, listen. My bad. Man, can you use my browser please? Thank you.


### [08:00 - 09:00]

**[08:02]** Oh yeah. So actually this by right

**[08:02]** Oh yeah. So actually this by right managed to have used like a browser that

**[08:04]** managed to have used like a browser that

**[08:04]** managed to have used like a browser that I have on my computer.

**[08:07]** I have on my computer.

**[08:07]** I have on my computer. Let's give it a bit of time to run.

**[08:15]** Yeah. And so this actually kickstarts a

**[08:15]** Yeah. And so this actually kickstarts a tab on my computer. Right. And so for

**[08:18]** tab on my computer. Right. And so for

**[08:18]** tab on my computer. Right. And so for specific task whereby you need to use

**[08:20]** specific task whereby you need to use

**[08:20]** specific task whereby you need to use these authenticated platform just

**[08:28]** uh

**[08:28]** uh a while for the computer to boot up.

**[08:31]** a while for the computer to boot up.

**[08:31]** a while for the computer to boot up. Yeah. So you can see that it actually

**[08:33]** Yeah. So you can see that it actually

**[08:33]** Yeah. So you can see that it actually opened a tab in my computer over here.

**[08:34]** opened a tab in my computer over here.

**[08:34]** opened a tab in my computer over here. It looked on Google Maps. It pulled it

**[08:36]** It looked on Google Maps. It pulled it

**[08:36]** It looked on Google Maps. It pulled it up, right? And what we're seeing this

**[08:38]** up, right? And what we're seeing this

**[08:38]** up, right? And what we're seeing this actually mean is that what's really cool

**[08:40]** actually mean is that what's really cool

**[08:40]** actually mean is that what's really cool about this is you spin up multiple

**[08:41]** about this is you spin up multiple

**[08:41]** about this is you spin up multiple instances of this in parallel, right? So

**[08:43]** instances of this in parallel, right? So

**[08:43]** instances of this in parallel, right? So you can imagine for someone with a Mac

**[08:45]** you can imagine for someone with a Mac

**[08:45]** you can imagine for someone with a Mac Mini running in their basement, all you

**[08:47]** Mini running in their basement, all you

**[08:47]** Mini running in their basement, all you got to do is just say every day a

**[08:48]** got to do is just say every day a

**[08:48]** got to do is just say every day a schedule task, hey manners, use this and

**[08:50]** schedule task, hey manners, use this and

**[08:50]** schedule task, hey manners, use this and it'll get it done for you. And these are

**[08:52]** it'll get it done for you. And these are

**[08:52]** it'll get it done for you. And these are all things that you can do through the

**[08:53]** all things that you can do through the

**[08:53]** all things that you can do through the API, right? Because we built a general

**[08:56]** API, right? Because we built a general

**[08:56]** API, right? Because we built a general AI agent first and then web development

**[08:59]** AI agent first and then web development

**[08:59]** AI agent first and then web development capabilities second, we can also do some


### [09:00 - 10:00]

**[09:01]** capabilities second, we can also do some

**[09:01]** capabilities second, we can also do some pretty crazy things. For example, um if

**[09:04]** pretty crazy things. For example, um if

**[09:04]** pretty crazy things. For example, um if you look at the this uh demo that I

**[09:07]** you look at the this uh demo that I

**[09:07]** you look at the this uh demo that I built over here. So,

**[09:13]** one of the things that I found really

**[09:13]** one of the things that I found really confusing about the AIE is that there's

**[09:14]** confusing about the AIE is that there's

**[09:14]** confusing about the AIE is that there's a lot of different events. I kind of

**[09:16]** a lot of different events. I kind of

**[09:16]** a lot of different events. I kind of want to make sure I hit all of them,

**[09:17]** want to make sure I hit all of them,

**[09:17]** want to make sure I hit all of them, right? And I found the website a bit

**[09:20]** right? And I found the website a bit

**[09:20]** right? And I found the website a bit confusing personally. And so, what I I

**[09:23]** confusing personally. And so, what I I

**[09:23]** confusing personally. And so, what I I told Manis to do was, "Hey, Manis, can

**[09:25]** told Manis to do was, "Hey, Manis, can

**[09:25]** told Manis to do was, "Hey, Manis, can you go to the website? Can you look at

**[09:27]** you go to the website? Can you look at

**[09:27]** you go to the website? Can you look at the browser? Can you open a single

**[09:30]** the browser? Can you open a single

**[09:30]** the browser? Can you open a single event? And then can you scrape

**[09:31]** event? And then can you scrape

**[09:32]** event? And then can you scrape everything there for me?" And so, what

**[09:33]** everything there for me?" And so, what

**[09:33]** everything there for me?" And so, what Manis did is that it actually scraped

**[09:34]** Manis did is that it actually scraped

**[09:34]** Manis did is that it actually scraped every single thing on the single brow on

**[09:36]** every single thing on the single brow on

**[09:36]** every single thing on the single brow on their website. It put into a JSON file

**[09:38]** their website. It put into a JSON file

**[09:38]** their website. It put into a JSON file and then it loaded it into this website

**[09:40]** and then it loaded it into this website

**[09:40]** and then it loaded it into this website for me. Um, you may notice a very

**[09:42]** for me. Um, you may notice a very

**[09:42]** for me. Um, you may notice a very brutalist theme and that's because I

**[09:43]** brutalist theme and that's because I

**[09:44]** brutalist theme and that's because I really like Chroma's website design. So

**[09:45]** really like Chroma's website design. So

**[09:45]** really like Chroma's website design. So everything I build looks like Chroma to

**[09:47]** everything I build looks like Chroma to

**[09:47]** everything I build looks like Chroma to some degree. But what you get out of

**[09:50]** some degree. But what you get out of

**[09:50]** some degree. But what you get out of this is that let's say I am interested

**[09:52]** this is that let's say I am interested

**[09:52]** this is that let's say I am interested in 2026, the year the IDE died. Well,

**[09:55]** in 2026, the year the IDE died. Well,

**[09:55]** in 2026, the year the IDE died. Well, you can see that the description has

**[09:57]** you can see that the description has

**[09:57]** you can see that the description has been scraped. I can add to my Google

**[09:58]** been scraped. I can add to my Google

**[09:58]** been scraped. I can add to my Google calendar in one click. And I also have


### [10:00 - 11:00]

**[10:00]** calendar in one click. And I also have

**[10:00]** calendar in one click. And I also have similar events over here, right? For

**[10:03]** similar events over here, right? For

**[10:03]** similar events over here, right? For example, if I'm interested in the year

**[10:04]** example, if I'm interested in the year

**[10:04]** example, if I'm interested in the year the IDE died, maybe I want to check out

**[10:05]** the IDE died, maybe I want to check out

**[10:06]** the IDE died, maybe I want to check out AMC code or AGI the path forward.

**[10:08]** AMC code or AGI the path forward.

**[10:08]** AMC code or AGI the path forward. Everything that I did over here was just

**[10:10]** Everything that I did over here was just

**[10:10]** Everything that I did over here was just built by me prompting Manis because I

**[10:12]** built by me prompting Manis because I

**[10:12]** built by me prompting Manis because I was like, hey, I like this event.

**[10:14]** was like, hey, I like this event.

**[10:14]** was like, hey, I like this event. Anything else I should pay attention to,

**[10:16]** Anything else I should pay attention to,

**[10:16]** Anything else I should pay attention to, right? Everything here is because

**[10:18]** right? Everything here is because

**[10:18]** right? Everything here is because Manners can build in with external

**[10:19]** Manners can build in with external

**[10:19]** Manners can build in with external platforms such as Chroma. Um, and all I

**[10:22]** platforms such as Chroma. Um, and all I

**[10:22]** platforms such as Chroma. Um, and all I did was give it a Chroma API key, an

**[10:24]** did was give it a Chroma API key, an

**[10:24]** did was give it a Chroma API key, an OpenAI key, so it can do embeddings. And

**[10:26]** OpenAI key, so it can do embeddings. And

**[10:26]** OpenAI key, so it can do embeddings. And now we have this. Now, my favorite

**[10:28]** now we have this. Now, my favorite

**[10:28]** now we have this. Now, my favorite feature is that after starring

**[10:30]** feature is that after starring

**[10:30]** feature is that after starring everything that I'm curious about, I can

**[10:32]** everything that I'm curious about, I can

**[10:32]** everything that I'm curious about, I can scroll up. I can go to my timeline and

**[10:36]** scroll up. I can go to my timeline and

**[10:36]** scroll up. I can go to my timeline and then instantly I see a list of

**[10:37]** then instantly I see a list of

**[10:37]** then instantly I see a list of everything over here that is happening

**[10:40]** everything over here that is happening

**[10:40]** everything over here that is happening for the day custom to me. And so,

**[10:42]** for the day custom to me. And so,

**[10:42]** for the day custom to me. And so, yesterday I was really happy to actually

**[10:43]** yesterday I was really happy to actually

**[10:44]** yesterday I was really happy to actually check out the new talks by Will Brown

**[10:46]** check out the new talks by Will Brown

**[10:46]** check out the new talks by Will Brown and the applied compute guys which were

**[10:47]** and the applied compute guys which were

**[10:48]** and the applied compute guys which were really technical. And this is an example

**[10:50]** really technical. And this is an example

**[10:50]** really technical. And this is an example of what you can build with the web

**[10:51]** of what you can build with the web

**[10:51]** of what you can build with the web development framework that we've put

**[10:53]** development framework that we've put

**[10:53]** development framework that we've put together. We also have support for

**[10:55]** together. We also have support for

**[10:55]** together. We also have support for things like stripe which because we ship

**[10:57]** things like stripe which because we ship

**[10:57]** things like stripe which because we ship with a full docker image you can install

**[10:59]** with a full docker image you can install

**[10:59]** with a full docker image you can install anything on it. Uh some of my favorite


### [11:00 - 12:00]

**[11:01]** anything on it. Uh some of my favorite

**[11:01]** anything on it. Uh some of my favorite examples, you've you've used anything a

**[11:03]** examples, you've you've used anything a

**[11:03]** examples, you've you've used anything a bit more complex, you need a Reddis Q,

**[11:05]** bit more complex, you need a Reddis Q,

**[11:05]** bit more complex, you need a Reddis Q, you can actually just install Reddis on

**[11:06]** you can actually just install Reddis on

**[11:06]** you can actually just install Reddis on the web app and use BMQ and you're good

**[11:09]** the web app and use BMQ and you're good

**[11:09]** the web app and use BMQ and you're good to go, right? Um Stripe integrations, if

**[11:13]** to go, right? Um Stripe integrations, if

**[11:13]** to go, right? Um Stripe integrations, if you use a lot of other platforms because

**[11:15]** you use a lot of other platforms because

**[11:15]** you use a lot of other platforms because they're not full Docker images, they're

**[11:17]** they're not full Docker images, they're

**[11:17]** they're not full Docker images, they're not full applications, they're just

**[11:18]** not full applications, they're just

**[11:18]** not full applications, they're just giving you a nice front end, you're not

**[11:20]** giving you a nice front end, you're not

**[11:20]** giving you a nice front end, you're not actually able to do things like web

**[11:22]** actually able to do things like web

**[11:22]** actually able to do things like web hooks or more complex integrations, but

**[11:24]** hooks or more complex integrations, but

**[11:24]** hooks or more complex integrations, but we can support that. And if you use our

**[11:26]** we can support that. And if you use our

**[11:26]** we can support that. And if you use our Stripe integration, for example, we

**[11:28]** Stripe integration, for example, we

**[11:28]** Stripe integration, for example, we automatically set up web hooks for you.

**[11:29]** automatically set up web hooks for you.

**[11:29]** automatically set up web hooks for you. We ways to test it, right? Manners can

**[11:31]** We ways to test it, right? Manners can

**[11:31]** We ways to test it, right? Manners can receive the web hooks. And in the

**[11:33]** receive the web hooks. And in the

**[11:33]** receive the web hooks. And in the future, we'll be rolling out things like

**[11:35]** future, we'll be rolling out things like

**[11:35]** future, we'll be rolling out things like autoscaling, warm deployments, all the

**[11:38]** autoscaling, warm deployments, all the

**[11:38]** autoscaling, warm deployments, all the important things that you need in order

**[11:39]** important things that you need in order

**[11:39]** important things that you need in order to essentially build a single MVP idea,

**[11:42]** to essentially build a single MVP idea,

**[11:42]** to essentially build a single MVP idea, right? You can integrate anything you

**[11:44]** right? You can integrate anything you

**[11:44]** right? You can integrate anything you want. You can add any packages you want.

**[11:47]** want. You can add any packages you want.

**[11:47]** want. You can add any packages you want. And please don't abuse this platform,

**[11:48]** And please don't abuse this platform,

**[11:48]** And please don't abuse this platform, guys. I kind of like my job.

**[11:51]** guys. I kind of like my job.

**[11:51]** guys. I kind of like my job. We It's It's been uh we worked very hard

**[11:53]** We It's It's been uh we worked very hard

**[11:53]** We It's It's been uh we worked very hard to try to keep it uh good and cheap for

**[11:55]** to try to keep it uh good and cheap for

**[11:55]** to try to keep it uh good and cheap for everybody, you know. Um, but most

**[11:57]** everybody, you know. Um, but most

**[11:57]** everybody, you know. Um, but most importantly, it's like it really is the

**[11:59]** importantly, it's like it really is the

**[11:59]** importantly, it's like it really is the fact that if you build a general AI


### [12:00 - 13:00]

**[12:00]** fact that if you build a general AI

**[12:00]** fact that if you build a general AI agent instead of verticalized products,

**[12:03]** agent instead of verticalized products,

**[12:03]** agent instead of verticalized products, you can do so much more. And I think

**[12:04]** you can do so much more. And I think

**[12:04]** you can do so much more. And I think that's kind of what I'm driving at here,

**[12:06]** that's kind of what I'm driving at here,

**[12:06]** that's kind of what I'm driving at here, right? Imagine building this six months

**[12:08]** right? Imagine building this six months

**[12:08]** right? Imagine building this six months ago. I would have to build a web

**[12:10]** ago. I would have to build a web

**[12:10]** ago. I would have to build a web application. After I built a web

**[12:12]** application. After I built a web

**[12:12]** application. After I built a web application, then I need to set up my

**[12:13]** application, then I need to set up my

**[12:13]** application, then I need to set up my Chroma account. I need to get my Chroma

**[12:15]** Chroma account. I need to get my Chroma

**[12:15]** Chroma account. I need to get my Chroma DB setup. Then I need to maybe find

**[12:17]** DB setup. Then I need to maybe find

**[12:17]** DB setup. Then I need to maybe find cloud code, boot it up. After I put it

**[12:20]** cloud code, boot it up. After I put it

**[12:20]** cloud code, boot it up. After I put it together, I now need to think about,

**[12:21]** together, I now need to think about,

**[12:21]** together, I now need to think about, hey, whether I deploy it with manage, it

**[12:24]** hey, whether I deploy it with manage, it

**[12:24]** hey, whether I deploy it with manage, it kind of just works. And that's kind of

**[12:26]** kind of just works. And that's kind of

**[12:26]** kind of just works. And that's kind of the beauty of it and things will get

**[12:27]** the beauty of it and things will get

**[12:27]** the beauty of it and things will get better, right? Uh so I talked a lot

**[12:29]** better, right? Uh so I talked a lot

**[12:29]** better, right? Uh so I talked a lot about what Manis is and so I guess I

**[12:33]** about what Manis is and so I guess I

**[12:33]** about what Manis is and so I guess I should move on a little bit to the manis

**[12:34]** should move on a little bit to the manis

**[12:34]** should move on a little bit to the manis API which is what most people came here

**[12:36]** API which is what most people came here

**[12:36]** API which is what most people came here for. And so what is the manus API? Well

**[12:41]** for. And so what is the manus API? Well

**[12:41]** for. And so what is the manus API? Well earlier you've seen a few different

**[12:42]** earlier you've seen a few different

**[12:42]** earlier you've seen a few different examples whereby you know we've used

**[12:44]** examples whereby you know we've used

**[12:44]** examples whereby you know we've used manis to build websites. We've used

**[12:46]** manis to build websites. We've used

**[12:46]** manis to build websites. We've used Manis to do things like remote browser

**[12:48]** Manis to do things like remote browser

**[12:48]** Manis to do things like remote browser operation and you know manus also ships

**[12:50]** operation and you know manus also ships

**[12:50]** operation and you know manus also ships with the ability to query things like

**[12:51]** with the ability to query things like

**[12:52]** with the ability to query things like the notion your custom MCPS whatever

**[12:54]** the notion your custom MCPS whatever

**[12:54]** the notion your custom MCPS whatever sort of like you know code they need

**[12:56]** sort of like you know code they need

**[12:56]** sort of like you know code they need written because every single manage chat

**[12:58]** written because every single manage chat

**[12:58]** written because every single manage chat ships with its own sandbox and so you


### [13:00 - 14:00]

**[13:01]** ships with its own sandbox and so you

**[13:01]** ships with its own sandbox and so you get the exact same things with the API

**[13:03]** get the exact same things with the API

**[13:03]** get the exact same things with the API so so what are some things that we built

**[13:06]** so so what are some things that we built

**[13:06]** so so what are some things that we built internally right the Slackbot is the

**[13:08]** internally right the Slackbot is the

**[13:08]** internally right the Slackbot is the thing that's public facing our Zapia

**[13:10]** thing that's public facing our Zapia

**[13:10]** thing that's public facing our Zapia integration is built on our API our N8

**[13:13]** integration is built on our API our N8

**[13:13]** integration is built on our API our N8 integration is also built on our on our

**[13:15]** integration is also built on our on our

**[13:15]** integration is also built on our on our API Okay. And we built a lot of our own

**[13:18]** API Okay. And we built a lot of our own

**[13:18]** API Okay. And we built a lot of our own support bots in house whereby before

**[13:21]** support bots in house whereby before

**[13:21]** support bots in house whereby before anyone looks at it, if it's something

**[13:23]** anyone looks at it, if it's something

**[13:23]** anyone looks at it, if it's something that's important, manice can go to the

**[13:25]** that's important, manice can go to the

**[13:25]** that's important, manice can go to the chat, click on every single message, and

**[13:27]** chat, click on every single message, and

**[13:28]** chat, click on every single message, and at the end it gives a full report with

**[13:29]** at the end it gives a full report with

**[13:29]** at the end it gives a full report with screenshots because it has a browser of

**[13:31]** screenshots because it has a browser of

**[13:32]** screenshots because it has a browser of everything that you can do. And so I

**[13:34]** everything that you can do. And so I

**[13:34]** everything that you can do. And so I really liked what I built internally and

**[13:36]** really liked what I built internally and

**[13:36]** really liked what I built internally and so I thought, why don't we build it

**[13:37]** so I thought, why don't we build it

**[13:37]** so I thought, why don't we build it together, right? Um, this isn't very

**[13:40]** together, right? Um, this isn't very

**[13:40]** together, right? Um, this isn't very complicated and I I kind of hope Stripe

**[13:42]** complicated and I I kind of hope Stripe

**[13:42]** complicated and I I kind of hope Stripe and Modal work nicely. So we'll see. I

**[13:45]** and Modal work nicely. So we'll see. I

**[13:45]** and Modal work nicely. So we'll see. I hopefully fingers crossed. Um but

**[13:46]** hopefully fingers crossed. Um but

**[13:46]** hopefully fingers crossed. Um but through this we're going to work through

**[13:47]** through this we're going to work through

**[13:47]** through this we're going to work through a lot of the simple ideas. Um we'll be

**[13:49]** a lot of the simple ideas. Um we'll be

**[13:50]** a lot of the simple ideas. Um we'll be looking at a few different notebooks. If

**[13:52]** looking at a few different notebooks. If

**[13:52]** looking at a few different notebooks. If you want to sort of um see the notebooks

**[13:55]** you want to sort of um see the notebooks

**[13:55]** you want to sort of um see the notebooks um I have them over here at this link.

**[13:57]** um I have them over here at this link.

**[13:57]** um I have them over here at this link. So a tiny URL slashmanis API workshop.


### [14:00 - 15:00]

**[14:01]** So a tiny URL slashmanis API workshop.

**[14:01]** So a tiny URL slashmanis API workshop. And so in order for you to get started

**[14:03]** And so in order for you to get started

**[14:03]** And so in order for you to get started with that you'll need a manus API key.

**[14:05]** with that you'll need a manus API key.

**[14:05]** with that you'll need a manus API key. Um if you have a normal manus account

**[14:07]** Um if you have a normal manus account

**[14:07]** Um if you have a normal manus account the billing for the API is exactly the

**[14:08]** the billing for the API is exactly the

**[14:08]** the billing for the API is exactly the same as if you took a chat. So whatever

**[14:12]** same as if you took a chat. So whatever

**[14:12]** same as if you took a chat. So whatever you would spend for the same query in a

**[14:13]** you would spend for the same query in a

**[14:13]** you would spend for the same query in a manus chat on a web app, the API would

**[14:15]** manus chat on a web app, the API would

**[14:16]** manus chat on a web app, the API would cost the same. And really for now, this

**[14:18]** cost the same. And really for now, this

**[14:18]** cost the same. And really for now, this is a this is what we want you to do

**[14:20]** is a this is what we want you to do

**[14:20]** is a this is what we want you to do because we want Manners to meet you

**[14:22]** because we want Manners to meet you

**[14:22]** because we want Manners to meet you where you're at, right? We don't want

**[14:23]** where you're at, right? We don't want

**[14:24]** where you're at, right? We don't want you have to worry about if I use the

**[14:25]** you have to worry about if I use the

**[14:25]** you have to worry about if I use the API, is it more expensive or less

**[14:26]** API, is it more expensive or less

**[14:26]** API, is it more expensive or less expensive? Is the chat different? Should

**[14:28]** expensive? Is the chat different? Should

**[14:28]** expensive? Is the chat different? Should I use the Slack integration? We want you

**[14:30]** I use the Slack integration? We want you

**[14:30]** I use the Slack integration? We want you to be able to we want to provide a

**[14:32]** to be able to we want to provide a

**[14:32]** to be able to we want to provide a custom customizable way for you to be

**[14:34]** custom customizable way for you to be

**[14:34]** custom customizable way for you to be able to work with Manis. And so um this

**[14:37]** able to work with Manis. And so um this

**[14:37]** able to work with Manis. And so um this is the tiny URL link and I'm just going

**[14:39]** is the tiny URL link and I'm just going

**[14:39]** is the tiny URL link and I'm just going to proceed on to the next bit.

**[14:45]** So the first thing we're going to do is

**[14:45]** So the first thing we're going to do is going to look at some of the API

**[14:46]** going to look at some of the API

**[14:46]** going to look at some of the API fundamentals. Um so I have the API over

**[14:50]** fundamentals. Um so I have the API over

**[14:50]** fundamentals. Um so I have the API over here. Um you need these three

**[14:51]** here. Um you need these three

**[14:51]** here. Um you need these three environment variables. I tried to make

**[14:53]** environment variables. I tried to make

**[14:53]** environment variables. I tried to make it very easy for you to set up Slack

**[14:55]** it very easy for you to set up Slack

**[14:55]** it very easy for you to set up Slack even though it is a pain in the ass. Um

**[14:58]** even though it is a pain in the ass. Um

**[14:58]** even though it is a pain in the ass. Um so here are the five notebooks I'll be


### [15:00 - 16:00]

**[15:00]** so here are the five notebooks I'll be

**[15:00]** so here are the five notebooks I'll be working through. And if you scroll down

**[15:02]** working through. And if you scroll down

**[15:02]** working through. And if you scroll down a fair bit, I have the screenshots on

**[15:04]** a fair bit, I have the screenshots on

**[15:04]** a fair bit, I have the screenshots on how you can actually get your own Slack

**[15:06]** how you can actually get your own Slack

**[15:06]** how you can actually get your own Slack tokens. Um,

**[15:08]** tokens. Um,

**[15:08]** tokens. Um, so let's begin.

**[15:10]** so let's begin.

**[15:10]** so let's begin. So the first thing you need is basically

**[15:13]** So the first thing you need is basically

**[15:13]** So the first thing you need is basically a manis API key. And once you have the

**[15:17]** a manis API key. And once you have the

**[15:17]** a manis API key. And once you have the API key, you need to put it in this

**[15:19]** API key, you need to put it in this

**[15:19]** API key, you need to put it in this envir.

**[15:21]** envir.

**[15:21]** envir. I've provided basically the ENV

**[15:23]** I've provided basically the ENV

**[15:23]** I've provided basically the ENV variables you need in av.

**[15:25]** variables you need in av.

**[15:25]** variables you need in av. But you basically need a manus API key,

**[15:27]** But you basically need a manus API key,

**[15:27]** But you basically need a manus API key, a slackbot token, and a slack signing

**[15:29]** a slackbot token, and a slack signing

**[15:29]** a slackbot token, and a slack signing secret.

**[15:31]** secret.

**[15:31]** secret. So, let's load it in.

**[15:33]** So, let's load it in.

**[15:33]** So, let's load it in. Okay, I kind of need to

**[15:36]** Okay, I kind of need to

**[15:36]** Okay, I kind of need to Holy that was tough. Um, so you

**[15:38]** Holy that was tough. Um, so you

**[15:38]** Holy that was tough. Um, so you can see that now that we've loaded it in

**[15:40]** can see that now that we've loaded it in

**[15:40]** can see that now that we've loaded it in from our EMD file. Um, let's test it

**[15:44]** from our EMD file. Um, let's test it

**[15:44]** from our EMD file. Um, let's test it out. So,

**[15:47]** out. So,

**[15:47]** out. So, we're just going to check what files

**[15:48]** we're just going to check what files

**[15:48]** we're just going to check what files we've uploaded prior to this. And

**[15:49]** we've uploaded prior to this. And

**[15:50]** we've uploaded prior to this. And because this is a fresh account, we

**[15:51]** because this is a fresh account, we

**[15:51]** because this is a fresh account, we haven't uploaded any files. Um, you're

**[15:53]** haven't uploaded any files. Um, you're

**[15:53]** haven't uploaded any files. Um, you're just going to get object lists if not

**[15:54]** just going to get object lists if not

**[15:54]** just going to get object lists if not normally have a data property. And so,

**[15:57]** normally have a data property. And so,

**[15:57]** normally have a data property. And so, this means that our API key is working

**[15:58]** this means that our API key is working

**[15:58]** this means that our API key is working as intended. Um, one of the benefits of


### [16:00 - 17:00]

**[16:01]** as intended. Um, one of the benefits of

**[16:01]** as intended. Um, one of the benefits of using the Manis account is that we often

**[16:03]** using the Manis account is that we often

**[16:03]** using the Manis account is that we often have a lot of clients that come to us

**[16:04]** have a lot of clients that come to us

**[16:04]** have a lot of clients that come to us saying that I have sensitive files. I

**[16:06]** saying that I have sensitive files. I

**[16:06]** saying that I have sensitive files. I have things that, you know, I want to

**[16:08]** have things that, you know, I want to

**[16:08]** have things that, you know, I want to make sure no one else is able to see.

**[16:09]** make sure no one else is able to see.

**[16:09]** make sure no one else is able to see. And so, every file that you upload to

**[16:11]** And so, every file that you upload to

**[16:11]** And so, every file that you upload to the manage API, files API, it's

**[16:13]** the manage API, files API, it's

**[16:13]** the manage API, files API, it's basically going to be deleted

**[16:14]** basically going to be deleted

**[16:14]** basically going to be deleted automatically in 48 hours. And so, that

**[16:17]** automatically in 48 hours. And so, that

**[16:18]** automatically in 48 hours. And so, that means that whatever sort of temporary

**[16:19]** means that whatever sort of temporary

**[16:19]** means that whatever sort of temporary file you're using, if you delete the

**[16:21]** file you're using, if you delete the

**[16:21]** file you're using, if you delete the session, you can delete the file at any

**[16:23]** session, you can delete the file at any

**[16:23]** session, you can delete the file at any time. But if you forget like, oh, I

**[16:24]** time. But if you forget like, oh, I

**[16:24]** time. But if you forget like, oh, I upload this file, maybe I want to use it

**[16:25]** upload this file, maybe I want to use it

**[16:26]** upload this file, maybe I want to use it later, we will delete it for you, right?

**[16:28]** later, we will delete it for you, right?

**[16:28]** later, we will delete it for you, right? you have to delete the session for that

**[16:29]** you have to delete the session for that

**[16:29]** you have to delete the session for that file to be gone.

**[16:32]** file to be gone.

**[16:32]** file to be gone. Okay, cool. So, we validated that the

**[16:33]** Okay, cool. So, we validated that the

**[16:33]** Okay, cool. So, we validated that the API key works. So, let's create our

**[16:35]** API key works. So, let's create our

**[16:35]** API key works. So, let's create our first task. Um, I'm just going to be

**[16:38]** first task. Um, I'm just going to be

**[16:38]** first task. Um, I'm just going to be using the pure request here where I make

**[16:41]** using the pure request here where I make

**[16:41]** using the pure request here where I make a core request, but in our documentation

**[16:43]** a core request, but in our documentation

**[16:43]** a core request, but in our documentation at open.mmanis.ai,

**[16:45]** at open.mmanis.ai,

**[16:45]** at open.mmanis.ai, we do also have support for things like

**[16:47]** we do also have support for things like

**[16:47]** we do also have support for things like the OpenAI responses SDK if that's

**[16:49]** the OpenAI responses SDK if that's

**[16:49]** the OpenAI responses SDK if that's something you're using. Um, if you're

**[16:51]** something you're using. Um, if you're

**[16:51]** something you're using. Um, if you're using any sort of AI framework, I I've

**[16:53]** using any sort of AI framework, I I've

**[16:53]** using any sort of AI framework, I I've heard a few at this conference like AI

**[16:54]** heard a few at this conference like AI

**[16:54]** heard a few at this conference like AI SDK, Copilot, AG UI or something like

**[16:57]** SDK, Copilot, AG UI or something like

**[16:57]** SDK, Copilot, AG UI or something like that. Um, there a whole bunch of them.

**[16:59]** that. Um, there a whole bunch of them.

**[16:59]** that. Um, there a whole bunch of them. Please feel free to reach out to me. I'm


### [17:00 - 18:00]

**[17:01]** Please feel free to reach out to me. I'm

**[17:01]** Please feel free to reach out to me. I'm happy to try to see how we can make that

**[17:02]** happy to try to see how we can make that

**[17:02]** happy to try to see how we can make that work. So, let's try our first query,

**[17:05]** work. So, let's try our first query,

**[17:05]** work. So, let's try our first query, right? Um, let's ask Mannis, what is 2

**[17:08]** right? Um, let's ask Mannis, what is 2

**[17:08]** right? Um, let's ask Mannis, what is 2 plus2? Please provide a brief answer.

**[17:10]** plus2? Please provide a brief answer.

**[17:10]** plus2? Please provide a brief answer. So, let's

**[17:12]** So, let's

**[17:12]** So, let's run it. And when you run your first

**[17:15]** run it. And when you run your first

**[17:15]** run it. And when you run your first Madness API task, you see that you get a

**[17:17]** Madness API task, you see that you get a

**[17:17]** Madness API task, you see that you get a few things back. You get a task ID. you

**[17:20]** few things back. You get a task ID. you

**[17:20]** few things back. You get a task ID. you get a task title and you also get a task

**[17:22]** get a task title and you also get a task

**[17:22]** get a task title and you also get a task URL and so these three things are really

**[17:25]** URL and so these three things are really

**[17:26]** URL and so these three things are really important particularly the task ID the

**[17:27]** important particularly the task ID the

**[17:28]** important particularly the task ID the reason for that is that when you

**[17:29]** reason for that is that when you

**[17:29]** reason for that is that when you interact with manice and you're using

**[17:30]** interact with manice and you're using

**[17:30]** interact with manice and you're using manice as part of your workflow part of

**[17:32]** manice as part of your workflow part of

**[17:32]** manice as part of your workflow part of your application you might get things

**[17:34]** your application you might get things

**[17:34]** your application you might get things where manage will ask you for certain

**[17:35]** where manage will ask you for certain

**[17:36]** where manage will ask you for certain bits of clarification like I'm sorry

**[17:37]** bits of clarification like I'm sorry

**[17:37]** bits of clarification like I'm sorry like I need to understand a bit more

**[17:39]** like I need to understand a bit more

**[17:39]** like I need to understand a bit more what do you exactly want or come back to

**[17:40]** what do you exactly want or come back to

**[17:40]** what do you exactly want or come back to you and with some sort of data and you

**[17:42]** you and with some sort of data and you

**[17:42]** you and with some sort of data and you want to actually give some follow-up

**[17:43]** want to actually give some follow-up

**[17:44]** want to actually give some follow-up feedback and so by keeping the task ID

**[17:45]** feedback and so by keeping the task ID

**[17:45]** feedback and so by keeping the task ID around you're able to push to the same

**[17:47]** around you're able to push to the same

**[17:47]** around you're able to push to the same session

**[17:49]** session

**[17:49]** session So, let's click a bit on this task title

**[17:51]** So, let's click a bit on this task title

**[17:51]** So, let's click a bit on this task title that we've gotten back.

**[17:54]** that we've gotten back.

**[17:54]** that we've gotten back. And


### [18:00 - 19:00]

**[18:02]** I need to Oh, did I use the wrong API

**[18:02]** I need to Oh, did I use the wrong API key? I think I used the wrong API key,

**[18:04]** key? I think I used the wrong API key,

**[18:04]** key? I think I used the wrong API key, guys. I'm sorry. I will load a new API

**[18:07]** guys. I'm sorry. I will load a new API

**[18:07]** guys. I'm sorry. I will load a new API key for myself.

**[18:09]** key for myself.

**[18:09]** key for myself. I think it's this other one. Oh, yeah.

**[18:14]** I think it's this other one. Oh, yeah.

**[18:14]** I think it's this other one. Oh, yeah. Yeah. So you can see what is one what is

**[18:16]** Yeah. So you can see what is one what is

**[18:16]** Yeah. So you can see what is one what is 2 plus two and then you got four right.

**[18:19]** 2 plus two and then you got four right.

**[18:19]** 2 plus two and then you got four right. So this is the basically we when you

**[18:22]** So this is the basically we when you

**[18:22]** So this is the basically we when you don't specify a chat mode we have a

**[18:24]** don't specify a chat mode we have a

**[18:24]** don't specify a chat mode we have a router on the back end that tries to

**[18:25]** router on the back end that tries to

**[18:25]** router on the back end that tries to determine if you need to use basic

**[18:27]** determine if you need to use basic

**[18:27]** determine if you need to use basic simple chat or the full-fledged manus

**[18:29]** simple chat or the full-fledged manus

**[18:29]** simple chat or the full-fledged manus agent and I think this is something

**[18:30]** agent and I think this is something

**[18:30]** agent and I think this is something that's pretty uh simple but if you want

**[18:32]** that's pretty uh simple but if you want

**[18:32]** that's pretty uh simple but if you want full fine grain access we can those are

**[18:35]** full fine grain access we can those are

**[18:35]** full fine grain access we can those are parameters you can set on the API.

**[18:38]** parameters you can set on the API.

**[18:38]** parameters you can set on the API. So

**[18:40]** So

**[18:40]** So if you've looked at the agent profile,

**[18:42]** if you've looked at the agent profile,

**[18:42]** if you've looked at the agent profile, right, the basically the profile, the uh

**[18:45]** right, the basically the profile, the uh

**[18:45]** right, the basically the profile, the uh payload that we sent over, you may

**[18:46]** payload that we sent over, you may

**[18:46]** payload that we sent over, you may notice this agent profile, manus 1.5. We

**[18:49]** notice this agent profile, manus 1.5. We

**[18:49]** notice this agent profile, manus 1.5. We talked about it briefly at the start,

**[18:51]** talked about it briefly at the start,

**[18:51]** talked about it briefly at the start, but there are two kind of models that we

**[18:53]** but there are two kind of models that we

**[18:53]** but there are two kind of models that we currently use in manus. One is manus 1.5

**[18:55]** currently use in manus. One is manus 1.5

**[18:56]** currently use in manus. One is manus 1.5 and one is manus 1.5 light. For a lot of

**[18:58]** and one is manus 1.5 light. For a lot of

**[18:58]** and one is manus 1.5 light. For a lot of these more complex tasks, we highly


### [19:00 - 20:00]

**[19:00]** these more complex tasks, we highly

**[19:00]** these more complex tasks, we highly recommend using manus 1.5. For example,

**[19:02]** recommend using manus 1.5. For example,

**[19:02]** recommend using manus 1.5. For example, both of the websites earlier were coded

**[19:03]** both of the websites earlier were coded

**[19:03]** both of the websites earlier were coded 1.5. If you have very simple queries,

**[19:06]** 1.5. If you have very simple queries,

**[19:06]** 1.5. If you have very simple queries, things that you want to execute a bit

**[19:07]** things that you want to execute a bit

**[19:07]** things that you want to execute a bit faster, we recommend 1.5 light. So for

**[19:10]** faster, we recommend 1.5 light. So for

**[19:10]** faster, we recommend 1.5 light. So for this workshop, we're going to be using

**[19:11]** this workshop, we're going to be using

**[19:11]** this workshop, we're going to be using 1.5 light because we want a faster

**[19:12]** 1.5 light because we want a faster

**[19:12]** 1.5 light because we want a faster response, but also a lot of the things

**[19:14]** response, but also a lot of the things

**[19:14]** response, but also a lot of the things that we are working with are not that

**[19:15]** that we are working with are not that

**[19:16]** that we are working with are not that complex.

**[19:18]** complex.

**[19:18]** complex. And so

**[19:20]** And so

**[19:20]** And so with this new agent, you have a lot of

**[19:21]** with this new agent, you have a lot of

**[19:21]** with this new agent, you have a lot of things like unlimited context

**[19:23]** things like unlimited context

**[19:23]** things like unlimited context management. So what that means that once

**[19:24]** management. So what that means that once

**[19:24]** management. So what that means that once you go beyond the sort of length context

**[19:26]** you go beyond the sort of length context

**[19:26]** you go beyond the sort of length context window of a normal model itself, like

**[19:29]** window of a normal model itself, like

**[19:29]** window of a normal model itself, like whatever model we're using under the

**[19:30]** whatever model we're using under the

**[19:30]** whatever model we're using under the hood, we do a lot of smart context

**[19:32]** hood, we do a lot of smart context

**[19:32]** hood, we do a lot of smart context management. And because for us when we

**[19:35]** management. And because for us when we

**[19:35]** management. And because for us when we design nice we try to make sure that the

**[19:37]** design nice we try to make sure that the

**[19:37]** design nice we try to make sure that the KV caching is very high. If you read our

**[19:39]** KV caching is very high. If you read our

**[19:39]** KV caching is very high. If you read our article on you know context management

**[19:41]** article on you know context management

**[19:41]** article on you know context management by peak or CTO in um tune um most of

**[19:44]** by peak or CTO in um tune um most of

**[19:44]** by peak or CTO in um tune um most of this means that for you the responses

**[19:46]** this means that for you the responses

**[19:46]** this means that for you the responses are fast and quick and so the easiest

**[19:48]** are fast and quick and so the easiest

**[19:48]** are fast and quick and so the easiest way is just to say you can just pull man

**[19:51]** way is just to say you can just pull man

**[19:51]** way is just to say you can just pull man right so let's start another task look

**[19:53]** right so let's start another task look

**[19:53]** right so let's start another task look up the weather in New York City and then

**[19:54]** up the weather in New York City and then

**[19:54]** up the weather in New York City and then ask me a question about it right


### [20:00 - 21:00]

**[20:03]** okay so you can see that the task was

**[20:03]** okay so you can see that the task was created successfully and you get a task

**[20:05]** created successfully and you get a task

**[20:06]** created successfully and you get a task ID a task title and task URL Now, if you

**[20:08]** ID a task title and task URL Now, if you

**[20:08]** ID a task title and task URL Now, if you want to just pull this, it's pretty

**[20:10]** want to just pull this, it's pretty

**[20:10]** want to just pull this, it's pretty straightforward. Um, there are basically

**[20:13]** straightforward. Um, there are basically

**[20:13]** straightforward. Um, there are basically three states that the manage agent can

**[20:14]** three states that the manage agent can

**[20:14]** three states that the manage agent can be in. They're going to be either

**[20:17]** be in. They're going to be either

**[20:17]** be in. They're going to be either running, pending, completed, or error.

**[20:21]** running, pending, completed, or error.

**[20:21]** running, pending, completed, or error. Um, ideally, you never see error. Error

**[20:23]** Um, ideally, you never see error. Error

**[20:23]** Um, ideally, you never see error. Error is a very rare case. You also have

**[20:24]** is a very rare case. You also have

**[20:24]** is a very rare case. You also have completed that means the manage agent is

**[20:26]** completed that means the manage agent is

**[20:26]** completed that means the manage agent is done. Pending is when it's it requires

**[20:28]** done. Pending is when it's it requires

**[20:28]** done. Pending is when it's it requires more input from you. And so, currently,

**[20:32]** more input from you. And so, currently,

**[20:32]** more input from you. And so, currently, we're pulling over here and we're seeing

**[20:33]** we're pulling over here and we're seeing

**[20:33]** we're pulling over here and we're seeing that the task is still running. The

**[20:35]** that the task is still running. The

**[20:35]** that the task is still running. The progress of this is it task. Take a look

**[20:37]** progress of this is it task. Take a look

**[20:38]** progress of this is it task. Take a look at it.

**[20:39]** at it.

**[20:39]** at it. The weather in New York City over here.

**[20:43]** The weather in New York City over here.

**[20:43]** The weather in New York City over here. So, Mannis is currently waiting for a

**[20:44]** So, Mannis is currently waiting for a

**[20:44]** So, Mannis is currently waiting for a response from us. So, I've looked up the

**[20:46]** response from us. So, I've looked up the

**[20:46]** response from us. So, I've looked up the weather forecast. My question for you is

**[20:48]** weather forecast. My question for you is

**[20:48]** weather forecast. My question for you is given the rainy forecast for Monday or

**[20:49]** given the rainy forecast for Monday or

**[20:49]** given the rainy forecast for Monday or Tuesday, would you prefer to plan an

**[20:51]** Tuesday, would you prefer to plan an

**[20:51]** Tuesday, would you prefer to plan an indoor activity or an outdoor activity

**[20:52]** indoor activity or an outdoor activity

**[20:52]** indoor activity or an outdoor activity for one of those days? Right? So, we see

**[20:55]** for one of those days? Right? So, we see

**[20:55]** for one of those days? Right? So, we see here's all the here's what you get back

**[20:57]** here's all the here's what you get back

**[20:57]** here's all the here's what you get back when you actually query the information

**[20:58]** when you actually query the information

**[20:58]** when you actually query the information on the task. You get the credits you've


### [21:00 - 22:00]

**[21:00]** on the task. You get the credits you've

**[21:00]** on the task. You get the credits you've used. You get the response back. This is

**[21:03]** used. You get the response back. This is

**[21:03]** used. You get the response back. This is sort of similar to the OpenAI responses

**[21:05]** sort of similar to the OpenAI responses

**[21:05]** sort of similar to the OpenAI responses SDK, but basically we expose everything

**[21:07]** SDK, but basically we expose everything

**[21:07]** SDK, but basically we expose everything to you. And so you get back basically

**[21:10]** to you. And so you get back basically

**[21:10]** to you. And so you get back basically your messages and the messages that

**[21:11]** your messages and the messages that

**[21:11]** your messages and the messages that Manis sent to you. And so let's say in

**[21:15]** Manis sent to you. And so let's say in

**[21:16]** Manis sent to you. And so let's say in this case, if we look at the original

**[21:17]** this case, if we look at the original

**[21:17]** this case, if we look at the original chat, man said that given the rainy

**[21:19]** chat, man said that given the rainy

**[21:19]** chat, man said that given the rainy forecast, would you prefer to plan an

**[21:21]** forecast, would you prefer to plan an

**[21:21]** forecast, would you prefer to plan an indoor activity or an outdoor activity

**[21:22]** indoor activity or an outdoor activity

**[21:22]** indoor activity or an outdoor activity for one of those days? And if so, which

**[21:24]** for one of those days? And if so, which

**[21:24]** for one of those days? And if so, which day and what kind of activity would you

**[21:26]** day and what kind of activity would you

**[21:26]** day and what kind of activity would you prefer? Well, I guess in this case, um I

**[21:30]** prefer? Well, I guess in this case, um I

**[21:30]** prefer? Well, I guess in this case, um I guess I'll

**[21:32]** guess I'll

**[21:32]** guess I'll I guess I'll prefer an indoor activity

**[21:33]** I guess I'll prefer an indoor activity

**[21:34]** I guess I'll prefer an indoor activity on Tuesday. I'll probably choose

**[21:36]** on Tuesday. I'll probably choose

**[21:36]** on Tuesday. I'll probably choose probably an indoor activity

**[21:39]** probably an indoor activity

**[21:39]** probably an indoor activity on Tuesday.

**[21:41]** on Tuesday.

**[21:41]** on Tuesday. So, we let it run for a bit.

**[21:44]** So, we let it run for a bit.

**[21:44]** So, we let it run for a bit. And you can see that the the same sort

**[21:46]** And you can see that the the same sort

**[21:46]** And you can see that the the same sort of message was pushed to the same chat.

**[21:47]** of message was pushed to the same chat.

**[21:48]** of message was pushed to the same chat. And what this allows you to do is ensure

**[21:49]** And what this allows you to do is ensure

**[21:49]** And what this allows you to do is ensure that as you're running more and more

**[21:51]** that as you're running more and more

**[21:51]** that as you're running more and more complex workflows, you're able to ensure

**[21:52]** complex workflows, you're able to ensure

**[21:52]** complex workflows, you're able to ensure that all of your context is kept within

**[21:54]** that all of your context is kept within

**[21:54]** that all of your context is kept within the same chat.

**[21:57]** the same chat.

**[21:57]** the same chat. And so you can use the same polling

**[21:58]** And so you can use the same polling

**[21:58]** And so you can use the same polling interval. This is a very simple pattern.


### [22:00 - 23:00]

**[22:00]** interval. This is a very simple pattern.

**[22:00]** interval. This is a very simple pattern. As you're prototyping in the Manis API,

**[22:02]** As you're prototyping in the Manis API,

**[22:02]** As you're prototyping in the Manis API, polling is the easiest way to get

**[22:04]** polling is the easiest way to get

**[22:04]** polling is the easiest way to get started. And then in the third notebook,

**[22:06]** started. And then in the third notebook,

**[22:06]** started. And then in the third notebook, we're going to look at basically how to

**[22:07]** we're going to look at basically how to

**[22:07]** we're going to look at basically how to use web hooks. Um but for now, I think

**[22:09]** use web hooks. Um but for now, I think

**[22:09]** use web hooks. Um but for now, I think polling is pretty straightforward. Um

**[22:10]** polling is pretty straightforward. Um

**[22:10]** polling is pretty straightforward. Um you basically just check to see what is

**[22:12]** you basically just check to see what is

**[22:12]** you basically just check to see what is the current status of the task given the

**[22:13]** the current status of the task given the

**[22:13]** the current status of the task given the four sort of statuses that we talked

**[22:15]** four sort of statuses that we talked

**[22:15]** four sort of statuses that we talked about running, pending, completed, and

**[22:17]** about running, pending, completed, and

**[22:17]** about running, pending, completed, and error. We take those and you can

**[22:19]** error. We take those and you can

**[22:19]** error. We take those and you can determine what to do next in your

**[22:20]** determine what to do next in your

**[22:20]** determine what to do next in your application.

**[22:23]** application.

**[22:23]** application. So this is essentially the first core

**[22:25]** So this is essentially the first core

**[22:25]** So this is essentially the first core mechanic of the manage API. We talked

**[22:27]** mechanic of the manage API. We talked

**[22:27]** mechanic of the manage API. We talked about authenticating your connection to

**[22:28]** about authenticating your connection to

**[22:28]** about authenticating your connection to the manage API. Creating your first

**[22:31]** the manage API. Creating your first

**[22:31]** the manage API. Creating your first task, managing the entire asynchronous

**[22:33]** task, managing the entire asynchronous

**[22:33]** task, managing the entire asynchronous life cycle from running a task, you

**[22:35]** life cycle from running a task, you

**[22:35]** life cycle from running a task, you know, really doing like the initial

**[22:36]** know, really doing like the initial

**[22:36]** know, really doing like the initial polling and then we also talked about

**[22:38]** polling and then we also talked about

**[22:38]** polling and then we also talked about how to push to the same task. So what's

**[22:41]** how to push to the same task. So what's

**[22:41]** how to push to the same task. So what's really important when you work with any

**[22:42]** really important when you work with any

**[22:42]** really important when you work with any sort of language model is you need some

**[22:44]** sort of language model is you need some

**[22:44]** sort of language model is you need some sort of context, right? Um, sometimes

**[22:46]** sort of context, right? Um, sometimes

**[22:46]** sort of context, right? Um, sometimes that might be a PDF of your own

**[22:48]** that might be a PDF of your own

**[22:48]** that might be a PDF of your own policies. Sometimes that might be, you

**[22:50]** policies. Sometimes that might be, you

**[22:50]** policies. Sometimes that might be, you know, some sort of system you want to

**[22:51]** know, some sort of system you want to

**[22:51]** know, some sort of system you want to upload. So, we have three different ways

**[22:53]** upload. So, we have three different ways

**[22:53]** upload. So, we have three different ways to do so in the manage API, right? As

**[22:56]** to do so in the manage API, right? As

**[22:56]** to do so in the manage API, right? As usual, I've defined a small library over

**[22:58]** usual, I've defined a small library over

**[22:58]** usual, I've defined a small library over here, env.y that does basically the same


### [23:00 - 24:00]

**[23:01]** here, env.y that does basically the same

**[23:01]** here, env.y that does basically the same things that we did in the previous

**[23:02]** things that we did in the previous

**[23:02]** things that we did in the previous notebooks. So, you can see over here,

**[23:04]** notebooks. So, you can see over here,

**[23:04]** notebooks. So, you can see over here, all we do is we just test given a files

**[23:07]** all we do is we just test given a files

**[23:07]** all we do is we just test given a files API and then we return the env key.

**[23:12]** API and then we return the env key.

**[23:12]** API and then we return the env key. So, let's see how this works.

**[23:15]** So, let's see how this works.

**[23:15]** So, let's see how this works. It's loaded into us.

**[23:18]** It's loaded into us.

**[23:18]** It's loaded into us. So now we have our API key and the base

**[23:19]** So now we have our API key and the base

**[23:20]** So now we have our API key and the base URL loaded in. So what I really love

**[23:23]** URL loaded in. So what I really love

**[23:23]** URL loaded in. So what I really love watching is Rick and Morty. And for a

**[23:25]** watching is Rick and Morty. And for a

**[23:25]** watching is Rick and Morty. And for a long time it was one of the funniest

**[23:26]** long time it was one of the funniest

**[23:26]** long time it was one of the funniest shows that I enjoyed. And actually they

**[23:27]** shows that I enjoyed. And actually they

**[23:27]** shows that I enjoyed. And actually they have a free API. And so what we can do

**[23:29]** have a free API. And so what we can do

**[23:29]** have a free API. And so what we can do is we can grab the first maybe 100

**[23:32]** is we can grab the first maybe 100

**[23:32]** is we can grab the first maybe 100 characters from Rick and Morty and let's

**[23:34]** characters from Rick and Morty and let's

**[23:34]** characters from Rick and Morty and let's get mad to figure out like what exactly

**[23:36]** get mad to figure out like what exactly

**[23:36]** get mad to figure out like what exactly Rick and Morty how their characters have

**[23:38]** Rick and Morty how their characters have

**[23:38]** Rick and Morty how their characters have been. So we fetched everything and we

**[23:40]** been. So we fetched everything and we

**[23:40]** been. So we fetched everything and we can just save it to a Rick and

**[23:42]** can just save it to a Rick and

**[23:42]** can just save it to a Rick and Morty.json file, right? Rick and Morty.

**[23:44]** Morty.json file, right? Rick and Morty.

**[23:44]** Morty.json file, right? Rick and Morty. Jason. So this is how how it looks like.

**[23:46]** Jason. So this is how how it looks like.

**[23:46]** Jason. So this is how how it looks like. We have every single character. We have

**[23:48]** We have every single character. We have

**[23:48]** We have every single character. We have the episodes that they've been alive

**[23:49]** the episodes that they've been alive

**[23:49]** the episodes that they've been alive for. And over here you have Morty, you

**[23:53]** for. And over here you have Morty, you

**[23:53]** for. And over here you have Morty, you have Rick status, and you have the

**[23:56]** have Rick status, and you have the

**[23:56]** have Rick status, and you have the origin, their current location, and a

**[23:57]** origin, their current location, and a

**[23:57]** origin, their current location, and a short image about them, right? And so


### [24:00 - 25:00]

**[24:01]** short image about them, right? And so

**[24:01]** short image about them, right? And so with the manus um AP, we support this

**[24:03]** with the manus um AP, we support this

**[24:03]** with the manus um AP, we support this thing. We support file uploads. And this

**[24:05]** thing. We support file uploads. And this

**[24:05]** thing. We support file uploads. And this is much more useful if you have

**[24:07]** is much more useful if you have

**[24:07]** is much more useful if you have sensitive files, files that are much

**[24:08]** sensitive files, files that are much

**[24:08]** sensitive files, files that are much larger than normal. And so this what we

**[24:10]** larger than normal. And so this what we

**[24:10]** larger than normal. And so this what we basically do is if you give us an API

**[24:12]** basically do is if you give us an API

**[24:12]** basically do is if you give us an API key if you give us let's say if you send

**[24:14]** key if you give us let's say if you send

**[24:14]** key if you give us let's say if you send a request to us and say hey I want to

**[24:16]** a request to us and say hey I want to

**[24:16]** a request to us and say hey I want to upload a file in this case it's called

**[24:17]** upload a file in this case it's called

**[24:17]** upload a file in this case it's called Rick and Morty characters

**[24:18]** Rick and Morty characters

**[24:18]** Rick and Morty characters correctors.json

**[24:19]** correctors.json

**[24:19]** correctors.json what we're going to do is we're going to

**[24:20]** what we're going to do is we're going to

**[24:20]** what we're going to do is we're going to check on our database going to save it

**[24:22]** check on our database going to save it

**[24:22]** check on our database going to save it and then we're going to give you an ST

**[24:23]** and then we're going to give you an ST

**[24:23]** and then we're going to give you an ST link and so what this allows you to do

**[24:25]** link and so what this allows you to do

**[24:25]** link and so what this allows you to do is be able to upload much larger files

**[24:28]** is be able to upload much larger files

**[24:28]** is be able to upload much larger files and all you got to do is do a put

**[24:29]** and all you got to do is do a put

**[24:29]** and all you got to do is do a put request. So we've created this file and

**[24:31]** request. So we've created this file and

**[24:31]** request. So we've created this file and you can see the file ID is basically

**[24:33]** you can see the file ID is basically

**[24:33]** you can see the file ID is basically file JQ

**[24:34]** file JQ

**[24:34]** file JQ you get a file ID that starts a file

**[24:36]** you get a file ID that starts a file

**[24:36]** you get a file ID that starts a file basically and then we're going to tell

**[24:38]** basically and then we're going to tell

**[24:38]** basically and then we're going to tell manis using the attach Rick and Morty

**[24:40]** manis using the attach Rick and Morty

**[24:40]** manis using the attach Rick and Morty correct data set let's create a simple

**[24:42]** correct data set let's create a simple

**[24:42]** correct data set let's create a simple and visually appealing website and so

**[24:46]** and visually appealing website and so

**[24:46]** and visually appealing website and so we've uploaded the file and let's take a

**[24:48]** we've uploaded the file and let's take a

**[24:48]** we've uploaded the file and let's take a look at the anis website over


### [25:00 - 26:00]

**[25:01]** Just check. I think it's in my other

**[25:01]** Just check. I think it's in my other account.

**[25:03]** account.

**[25:03]** account. Yeah. So

**[25:06]** Yeah. So

**[25:06]** Yeah. So you see over here that basically Rick

**[25:07]** you see over here that basically Rick

**[25:07]** you see over here that basically Rick and Morty we've uploaded the file. If

**[25:09]** and Morty we've uploaded the file. If

**[25:10]** and Morty we've uploaded the file. If you upload any images, any PDFs, we

**[25:12]** you upload any images, any PDFs, we

**[25:12]** you upload any images, any PDFs, we already come out of the box for for

**[25:13]** already come out of the box for for

**[25:13]** already come out of the box for for things like paring a PDFs, looking at

**[25:15]** things like paring a PDFs, looking at

**[25:15]** things like paring a PDFs, looking at handling all that multimodal content. So

**[25:18]** handling all that multimodal content. So

**[25:18]** handling all that multimodal content. So that's really useful for you, right? So

**[25:21]** that's really useful for you, right? So

**[25:21]** that's really useful for you, right? So let's manage this is going to run. It's

**[25:23]** let's manage this is going to run. It's

**[25:23]** let's manage this is going to run. It's going to create his website. We'll check

**[25:24]** going to create his website. We'll check

**[25:24]** going to create his website. We'll check back in a bit. But this is basically the

**[25:26]** back in a bit. But this is basically the

**[25:26]** back in a bit. But this is basically the first files API. And if you have large

**[25:27]** first files API. And if you have large

**[25:27]** first files API. And if you have large files that you know you might want

**[25:29]** files that you know you might want

**[25:29]** files that you know you might want automatically deleted at some point,

**[25:31]** automatically deleted at some point,

**[25:31]** automatically deleted at some point, this is a really useful way to do so.

**[25:34]** this is a really useful way to do so.

**[25:34]** this is a really useful way to do so. The next way that you can do so you also

**[25:36]** The next way that you can do so you also

**[25:36]** The next way that you can do so you also have the ability to delete this file at

**[25:37]** have the ability to delete this file at

**[25:37]** have the ability to delete this file at any point in time and this is an API

**[25:39]** any point in time and this is an API

**[25:39]** any point in time and this is an API call that you can run. Next way you can

**[25:41]** call that you can run. Next way you can

**[25:41]** call that you can run. Next way you can do so is if let's say you're using a URL

**[25:43]** do so is if let's say you're using a URL

**[25:43]** do so is if let's say you're using a URL attachment, right? A lot of times you

**[25:44]** attachment, right? A lot of times you

**[25:44]** attachment, right? A lot of times you might have a brow that comes from

**[25:46]** might have a brow that comes from

**[25:46]** might have a brow that comes from something like circleback, right? You've

**[25:48]** something like circleback, right? You've

**[25:48]** something like circleback, right? You've you've just done a call, you have a

**[25:50]** you've just done a call, you have a

**[25:50]** you've just done a call, you have a transcript, you want to send it over to

**[25:51]** transcript, you want to send it over to

**[25:51]** transcript, you want to send it over to Manis. And so we actually do support um

**[25:54]** Manis. And so we actually do support um

**[25:54]** Manis. And so we actually do support um raw call transcripts. So what I've done

**[25:56]** raw call transcripts. So what I've done

**[25:56]** raw call transcripts. So what I've done is I have basically created a fake

**[25:58]** is I have basically created a fake

**[25:58]** is I have basically created a fake transcript.


### [26:00 - 27:00]

**[26:04]** Yeah. Uh so I think this file was

**[26:04]** Yeah. Uh so I think this file was deleted by me accidentally.

**[26:07]** deleted by me accidentally.

**[26:07]** deleted by me accidentally. That was good. Warren Buffett.

**[26:19]** So thankfully Burkshshire had way like a

**[26:19]** So thankfully Burkshshire had way like a bunch of investor letters and so we can

**[26:21]** bunch of investor letters and so we can

**[26:21]** bunch of investor letters and so we can just provide a PDF link.

**[26:27]** So instead of a transcript maybe this

**[26:28]** So instead of a transcript maybe this we're just going to just do like Warren

**[26:29]** we're just going to just do like Warren

**[26:29]** we're just going to just do like Warren Buffett.

**[26:31]** Buffett.

**[26:31]** Buffett. This should work.

**[26:34]** This should work.

**[26:34]** This should work. This works. And then maybe we want to at

**[26:38]** This works. And then maybe we want to at

**[26:38]** This works. And then maybe we want to at this point we want to analyze given this

**[26:40]** this point we want to analyze given this

**[26:40]** this point we want to analyze given this investor letter that we have. Can you

**[26:43]** investor letter that we have. Can you

**[26:43]** investor letter that we have. Can you help me parse out you help me summarize

**[26:46]** help me parse out you help me summarize

**[26:46]** help me parse out you help me summarize it and give me some insights into what

**[26:50]** it and give me some insights into what

**[26:50]** it and give me some insights into what the company is looking to do.

**[26:55]** the company is looking to do.

**[26:55]** the company is looking to do. Right. So,


### [27:00 - 28:00]

**[27:08]** so now we can start a task um that

**[27:08]** so now we can start a task um that automatically out of the box works with

**[27:10]** automatically out of the box works with

**[27:10]** automatically out of the box works with these public urls. One of the things

**[27:12]** these public urls. One of the things

**[27:12]** these public urls. One of the things that I actually wanted to show over here

**[27:13]** that I actually wanted to show over here

**[27:13]** that I actually wanted to show over here is that with a lot of these um basic

**[27:17]** is that with a lot of these um basic

**[27:17]** is that with a lot of these um basic task um any of the connections that you

**[27:18]** task um any of the connections that you

**[27:18]** task um any of the connections that you have in manis for example Gmail notion

**[27:20]** have in manis for example Gmail notion

**[27:20]** have in manis for example Gmail notion that you've already configured ahead of

**[27:22]** that you've already configured ahead of

**[27:22]** that you've already configured ahead of time these all work out of the box and

**[27:24]** time these all work out of the box and

**[27:24]** time these all work out of the box and all you need to do is basically go to

**[27:25]** all you need to do is basically go to

**[27:25]** all you need to do is basically go to manis um let's say our website is over

**[27:27]** manis um let's say our website is over

**[27:28]** manis um let's say our website is over here you look at the connection over

**[27:31]** here you look at the connection over

**[27:31]** here you look at the connection over here if you go to manage connectors you

**[27:33]** here if you go to manage connectors you

**[27:33]** here if you go to manage connectors you can use any of these connectors just by

**[27:35]** can use any of these connectors just by

**[27:35]** can use any of these connectors just by copying this UID over here if you copy

**[27:37]** copying this UID over here if you copy

**[27:37]** copying this UID over here if you copy the UID and you add it as part of the

**[27:39]** the UID and you add it as part of the

**[27:39]** the UID and you add it as part of the connectors payload um it will work out

**[27:40]** connectors payload um it will work out

**[27:40]** connectors payload um it will work out of the box for

**[27:45]** We also support things like basic

**[27:45]** We also support things like basic before. Um, so this example over here,

**[27:47]** before. Um, so this example over here,

**[27:47]** before. Um, so this example over here, we just had a simple 404 page. Um, this

**[27:49]** we just had a simple 404 page. Um, this

**[27:49]** we just had a simple 404 page. Um, this was a screenshot that I took of a page

**[27:51]** was a screenshot that I took of a page

**[27:51]** was a screenshot that I took of a page that man has created. And so what we

**[27:53]** that man has created. And so what we

**[27:54]** that man has created. And so what we want to do over here is create a

**[27:55]** want to do over here is create a

**[27:55]** want to do over here is create a automated automat automated bug

**[27:57]** automated automat automated bug

**[27:57]** automated automat automated bug investigation task. Right? A user has


### [28:00 - 29:00]

**[28:00]** investigation task. Right? A user has

**[28:00]** investigation task. Right? A user has reported that the settings page isn't

**[28:01]** reported that the settings page isn't

**[28:01]** reported that the settings page isn't working. Let's give this B64 encoded

**[28:03]** working. Let's give this B64 encoded

**[28:03]** working. Let's give this B64 encoded image to manage and let's see how it can

**[28:05]** image to manage and let's see how it can

**[28:05]** image to manage and let's see how it can figure it out. Right? Can you beat Dara?

**[28:07]** figure it out. Right? Can you beat Dara?

**[28:07]** figure it out. Right? Can you beat Dara? Here's a website that we've created

**[28:09]** Here's a website that we've created

**[28:09]** Here's a website that we've created ahead of time. And can you figure out

**[28:11]** ahead of time. And can you figure out

**[28:11]** ahead of time. And can you figure out what exactly are the problems with this?

**[28:13]** what exactly are the problems with this?

**[28:13]** what exactly are the problems with this? Right.

**[28:15]** Right.

**[28:15]** Right. So, this is a simple Manis web app that

**[28:17]** So, this is a simple Manis web app that

**[28:17]** So, this is a simple Manis web app that I've created. Um, actually, if you go to

**[28:18]** I've created. Um, actually, if you go to

**[28:18]** I've created. Um, actually, if you go to the settings page, you get a 404. There

**[28:20]** the settings page, you get a 404. There

**[28:20]** the settings page, you get a 404. There also other few pages that also have

**[28:22]** also other few pages that also have

**[28:22]** also other few pages that also have 404s. So, let's see how Manis performs

**[28:24]** 404s. So, let's see how Manis performs

**[28:24]** 404s. So, let's see how Manis performs in a bit.

**[28:26]** in a bit.

**[28:26]** in a bit. >> So, if you look at our Rick and Morty

**[28:27]** >> So, if you look at our Rick and Morty

**[28:28]** >> So, if you look at our Rick and Morty character data set, manus sort of

**[28:30]** character data set, manus sort of

**[28:30]** character data set, manus sort of characterize all of this in a pretty

**[28:32]** characterize all of this in a pretty

**[28:32]** characterize all of this in a pretty cool website, right? You have the gender

**[28:35]** cool website, right? You have the gender

**[28:35]** cool website, right? You have the gender distribution. You have male, female,

**[28:36]** distribution. You have male, female,

**[28:36]** distribution. You have male, female, unknown. Rick Sanchez is obviously alive

**[28:39]** unknown. Rick Sanchez is obviously alive

**[28:39]** unknown. Rick Sanchez is obviously alive as is Morty since it's Rick and Morty.

**[28:41]** as is Morty since it's Rick and Morty.

**[28:42]** as is Morty since it's Rick and Morty. And you have all these other characters

**[28:43]** And you have all these other characters

**[28:43]** And you have all these other characters that's that are uniquely sort of

**[28:45]** that's that are uniquely sort of

**[28:45]** that's that are uniquely sort of characterized and visualized over here.

**[28:47]** characterized and visualized over here.

**[28:47]** characterized and visualized over here. For a lot of these internal tools, you

**[28:48]** For a lot of these internal tools, you

**[28:48]** For a lot of these internal tools, you can imagine that if you have a lot of

**[28:50]** can imagine that if you have a lot of

**[28:50]** can imagine that if you have a lot of data you want to search through, you can

**[28:51]** data you want to search through, you can

**[28:51]** data you want to search through, you can create a simple website just to

**[28:52]** create a simple website just to

**[28:52]** create a simple website just to visualize all of them out of the box.

**[28:54]** visualize all of them out of the box.

**[28:54]** visualize all of them out of the box. And that's pretty useful.

**[28:56]** And that's pretty useful.

**[28:56]** And that's pretty useful. Similarly for this investor letter you

**[28:58]** Similarly for this investor letter you

**[28:58]** Similarly for this investor letter you can see that we uploaded it and man has


### [29:00 - 30:00]

**[29:03]** can see that we uploaded it and man has

**[29:03]** can see that we uploaded it and man has actually detected that even though I

**[29:04]** actually detected that even though I

**[29:04]** actually detected that even though I called it call transcript.json it looked

**[29:06]** called it call transcript.json it looked

**[29:06]** called it call transcript.json it looked at said that the file is a PDF not a

**[29:08]** at said that the file is a PDF not a

**[29:08]** at said that the file is a PDF not a JSON text and then it completed a

**[29:11]** JSON text and then it completed a

**[29:11]** JSON text and then it completed a analysis of Warren Buffett's investor

**[29:12]** analysis of Warren Buffett's investor

**[29:12]** analysis of Warren Buffett's investor letter and it gave like this whole

**[29:14]** letter and it gave like this whole

**[29:14]** letter and it gave like this whole analysis at the end. One pretty cool

**[29:17]** analysis at the end. One pretty cool

**[29:17]** analysis at the end. One pretty cool thing is that we can take this um simple

**[29:21]** thing is that we can take this um simple

**[29:22]** thing is that we can take this um simple we have the task ID and so we go back to

**[29:23]** we have the task ID and so we go back to

**[29:23]** we have the task ID and so we go back to basics over here. Previously we had a

**[29:26]** basics over here. Previously we had a

**[29:26]** basics over here. Previously we had a thing whereby we said you go to request

**[29:30]** thing whereby we said you go to request

**[29:30]** thing whereby we said you go to request get URL.

**[29:48]** Let's see. I think just grab this

**[29:48]** Let's see. I think just grab this picture here instead.


### [30:00 - 31:00]

**[30:11]** Um this is not working as I thought it

**[30:11]** Um this is not working as I thought it would. Um

**[30:14]** would. Um

**[30:14]** would. Um what I wanted to show was actually that

**[30:16]** what I wanted to show was actually that

**[30:16]** what I wanted to show was actually that if we go to this specific um one over

**[30:18]** if we go to this specific um one over

**[30:18]** if we go to this specific um one over here, if we go to manice

**[30:21]** here, if we go to manice

**[30:21]** here, if we go to manice actually return

**[30:28]** just want to show like the

**[30:28]** just want to show like the not JSON.

**[30:39]** Yeah. So actually if you look at the

**[30:39]** Yeah. So actually if you look at the output over here you notice that over

**[30:41]** output over here you notice that over

**[30:41]** output over here you notice that over there man has created a markdown file

**[30:43]** there man has created a markdown file

**[30:43]** there man has created a markdown file and based off the markdown file you can

**[30:45]** and based off the markdown file you can

**[30:45]** and based off the markdown file you can actually you get back the full file URL

**[30:47]** actually you get back the full file URL

**[30:47]** actually you get back the full file URL the file name the mime type this is

**[30:49]** the file name the mime type this is

**[30:49]** the file name the mime type this is really useful if you want to do some

**[30:50]** really useful if you want to do some

**[30:50]** really useful if you want to do some sort of processing down the line with it

**[30:52]** sort of processing down the line with it

**[30:52]** sort of processing down the line with it right and so with this we've covered

**[30:54]** right and so with this we've covered

**[30:54]** right and so with this we've covered things like how to use the files API

**[30:56]** things like how to use the files API

**[30:56]** things like how to use the files API we've looked at basically how to up use

**[30:57]** we've looked at basically how to up use

**[30:57]** we've looked at basically how to up use publicly available URLs in manice and

**[30:59]** publicly available URLs in manice and

**[30:59]** publicly available URLs in manice and we've also talked about how to basically


### [31:00 - 32:00]

**[31:01]** we've also talked about how to basically

**[31:01]** we've also talked about how to basically be able to use basically for encoded

**[31:03]** be able to use basically for encoded

**[31:03]** be able to use basically for encoded images and so let's think a bit about

**[31:05]** images and so let's think a bit about

**[31:05]** images and so let's think a bit about web hooks right So in the previous

**[31:08]** web hooks right So in the previous

**[31:08]** web hooks right So in the previous example, we created a task with manness.

**[31:11]** example, we created a task with manness.

**[31:11]** example, we created a task with manness. We uploaded some files and the way that

**[31:12]** We uploaded some files and the way that

**[31:12]** We uploaded some files and the way that we tried to determine that, you know,

**[31:14]** we tried to determine that, you know,

**[31:14]** we tried to determine that, you know, the the thing was basically completed

**[31:17]** the the thing was basically completed

**[31:17]** the the thing was basically completed was that we pulled it every 20 seconds.

**[31:19]** was that we pulled it every 20 seconds.

**[31:19]** was that we pulled it every 20 seconds. As you're scaling out to more and more

**[31:20]** As you're scaling out to more and more

**[31:20]** As you're scaling out to more and more tasks, what you really want is what's

**[31:22]** tasks, what you really want is what's

**[31:22]** tasks, what you really want is what's called a web hook. What a web hook does

**[31:24]** called a web hook. What a web hook does

**[31:24]** called a web hook. What a web hook does is that when your task is completed,

**[31:26]** is that when your task is completed,

**[31:26]** is that when your task is completed, we'll send you an API um request and

**[31:28]** we'll send you an API um request and

**[31:28]** we'll send you an API um request and that will basically notify you that the

**[31:30]** that will basically notify you that the

**[31:30]** that will basically notify you that the task is done. So a really easy pattern

**[31:32]** task is done. So a really easy pattern

**[31:32]** task is done. So a really easy pattern over here is that you want to wait for

**[31:34]** over here is that you want to wait for

**[31:34]** over here is that you want to wait for the task to be completed. you get the

**[31:35]** the task to be completed. you get the

**[31:35]** the task to be completed. you get the web hook and you get all the information

**[31:36]** web hook and you get all the information

**[31:36]** web hook and you get all the information about the current task.

**[31:39]** about the current task.

**[31:39]** about the current task. So in this case, this is really useful

**[31:41]** So in this case, this is really useful

**[31:41]** So in this case, this is really useful because if you're building any sort of

**[31:42]** because if you're building any sort of

**[31:42]** because if you're building any sort of complex application, if you want to use

**[31:44]** complex application, if you want to use

**[31:44]** complex application, if you want to use this task at scale, it's not really

**[31:46]** this task at scale, it's not really

**[31:46]** this task at scale, it's not really viable for you to be able to sit there

**[31:47]** viable for you to be able to sit there

**[31:47]** viable for you to be able to sit there and just keep holding the API. It's

**[31:49]** and just keep holding the API. It's

**[31:49]** and just keep holding the API. It's going to be a bit complicated and I

**[31:51]** going to be a bit complicated and I

**[31:51]** going to be a bit complicated and I think not the best practice for you.

**[31:52]** think not the best practice for you.

**[31:52]** think not the best practice for you. You're going to basically have a lot of

**[31:53]** You're going to basically have a lot of

**[31:53]** You're going to basically have a lot of workers spinning. But if you use like

**[31:55]** workers spinning. But if you use like

**[31:55]** workers spinning. But if you use like web hooks, uh this is a much more

**[31:56]** web hooks, uh this is a much more

**[31:56]** web hooks, uh this is a much more sustainable way for you to do whatever

**[31:58]** sustainable way for you to do whatever

**[31:58]** sustainable way for you to do whatever sort of agent you're building at a much


### [32:00 - 33:00]

**[32:00]** sort of agent you're building at a much

**[32:00]** sort of agent you're building at a much cheaper cost.

**[32:02]** cheaper cost.

**[32:02]** cheaper cost. Okay, so I'm going to just use modal

**[32:05]** Okay, so I'm going to just use modal

**[32:05]** Okay, so I'm going to just use modal over here because it's a bit simpler.

**[32:06]** over here because it's a bit simpler.

**[32:06]** over here because it's a bit simpler. I'll have the modal code on the right

**[32:08]** I'll have the modal code on the right

**[32:08]** I'll have the modal code on the right and then I'll have the manus uh notebook

**[32:10]** and then I'll have the manus uh notebook

**[32:10]** and then I'll have the manus uh notebook on the left. Let me just load up my

**[32:13]** on the left. Let me just load up my

**[32:13]** on the left. Let me just load up my virtual environment.

**[32:15]** virtual environment.

**[32:15]** virtual environment. And

**[32:16]** And

**[32:16]** And basically what modal provides is it

**[32:18]** basically what modal provides is it

**[32:18]** basically what modal provides is it provides you the ability to deploy

**[32:20]** provides you the ability to deploy

**[32:20]** provides you the ability to deploy simple like um Python applications. Um

**[32:22]** simple like um Python applications. Um

**[32:22]** simple like um Python applications. Um in this case it's a fast API endpoint.

**[32:25]** in this case it's a fast API endpoint.

**[32:25]** in this case it's a fast API endpoint. And so

**[32:28]** And so

**[32:28]** And so mod surf server.py.

**[32:31]** mod surf server.py.

**[32:31]** mod surf server.py. So what you can see if if you run mod

**[32:33]** So what you can see if if you run mod

**[32:33]** So what you can see if if you run mod surfs server.py is that we now get a

**[32:35]** surfs server.py is that we now get a

**[32:35]** surfs server.py is that we now get a public endpoint that we can use, right?

**[32:37]** public endpoint that we can use, right?

**[32:37]** public endpoint that we can use, right? And this is pretty straightforward. Um

**[32:39]** And this is pretty straightforward. Um

**[32:39]** And this is pretty straightforward. Um if you run it on your own computer with

**[32:40]** if you run it on your own computer with

**[32:40]** if you run it on your own computer with modal, if you set up an account, you get

**[32:42]** modal, if you set up an account, you get

**[32:42]** modal, if you set up an account, you get $5 free. This basically gives you like

**[32:44]** $5 free. This basically gives you like

**[32:44]** $5 free. This basically gives you like an endpoint that you can now hit, right?

**[32:46]** an endpoint that you can now hit, right?

**[32:46]** an endpoint that you can now hit, right? And so let's get the Oh, I think someone

**[32:48]** And so let's get the Oh, I think someone

**[32:48]** And so let's get the Oh, I think someone already hit my end point.

**[32:52]** already hit my end point.

**[32:52]** already hit my end point. That's a bit stressful. Okay, guys.

**[32:54]** That's a bit stressful. Okay, guys.

**[32:54]** That's a bit stressful. Okay, guys. Please be nice to my end point. Um, but

**[32:55]** Please be nice to my end point. Um, but

**[32:56]** Please be nice to my end point. Um, but you can see that over here um in these

**[32:58]** you can see that over here um in these

**[32:58]** you can see that over here um in these over here. Oh, wow. Another person's


### [33:00 - 34:00]

**[33:00]** over here. Oh, wow. Another person's

**[33:00]** over here. Oh, wow. Another person's hitting my end point. Uh, all right

**[33:02]** hitting my end point. Uh, all right

**[33:02]** hitting my end point. Uh, all right guys. Anyway,

**[33:04]** guys. Anyway,

**[33:04]** guys. Anyway, >> maybe it's streaming in. That's kind of

**[33:06]** >> maybe it's streaming in. That's kind of

**[33:06]** >> maybe it's streaming in. That's kind of awkward, but uh anyway. Yes. So, um, if

**[33:10]** awkward, but uh anyway. Yes. So, um, if

**[33:10]** awkward, but uh anyway. Yes. So, um, if you basically want to register an

**[33:11]** you basically want to register an

**[33:11]** you basically want to register an endpoint web hook manus and you register

**[33:13]** endpoint web hook manus and you register

**[33:13]** endpoint web hook manus and you register web hook with us, when a task is created

**[33:15]** web hook with us, when a task is created

**[33:15]** web hook with us, when a task is created and when a task is stopped, we will send

**[33:17]** and when a task is stopped, we will send

**[33:17]** and when a task is stopped, we will send you two web hooks. And what this allows

**[33:18]** you two web hooks. And what this allows

**[33:18]** you two web hooks. And what this allows you to do on the front end is that then

**[33:20]** you to do on the front end is that then

**[33:20]** you to do on the front end is that then you know when you send a request to us

**[33:22]** you know when you send a request to us

**[33:22]** you know when you send a request to us whenever we started processing your task

**[33:24]** whenever we started processing your task

**[33:24]** whenever we started processing your task and when your task has been completed.

**[33:26]** and when your task has been completed.

**[33:26]** and when your task has been completed. Um the typical manage task is going to

**[33:27]** Um the typical manage task is going to

**[33:27]** Um the typical manage task is going to take roughly three to five minutes and

**[33:29]** take roughly three to five minutes and

**[33:29]** take roughly three to five minutes and if you have something that's a bit more

**[33:30]** if you have something that's a bit more

**[33:30]** if you have something that's a bit more complicated this is going to be you're

**[33:32]** complicated this is going to be you're

**[33:32]** complicated this is going to be you're not going to want to send that and pull

**[33:33]** not going to want to send that and pull

**[33:33]** not going to want to send that and pull and so the web hooks are a good way to

**[33:35]** and so the web hooks are a good way to

**[33:35]** and so the web hooks are a good way to do so. So let's see over here how we can

**[33:38]** do so. So let's see over here how we can

**[33:38]** do so. So let's see over here how we can mimic a web hook that manage send over

**[33:40]** mimic a web hook that manage send over

**[33:40]** mimic a web hook that manage send over here you have a test payload message

**[33:42]** here you have a test payload message

**[33:42]** here you have a test payload message ended. I think that's what people were

**[33:43]** ended. I think that's what people were

**[33:43]** ended. I think that's what people were running with my uh URL. And so um you

**[33:47]** running with my uh URL. And so um you

**[33:47]** running with my uh URL. And so um you can see now that this is a really useful

**[33:49]** can see now that this is a really useful

**[33:49]** can see now that this is a really useful pattern because if I'm building and I

**[33:50]** pattern because if I'm building and I

**[33:50]** pattern because if I'm building and I have like hundred man tasks running at

**[33:52]** have like hundred man tasks running at

**[33:52]** have like hundred man tasks running at once, right? I don't want to keep

**[33:54]** once, right? I don't want to keep

**[33:54]** once, right? I don't want to keep pulling for all of them. And so with a

**[33:55]** pulling for all of them. And so with a

**[33:55]** pulling for all of them. And so with a web hook, I can easily receive a lot of

**[33:57]** web hook, I can easily receive a lot of

**[33:57]** web hook, I can easily receive a lot of these notifications as they're running.


### [34:00 - 35:00]

**[34:00]** these notifications as they're running.

**[34:00]** these notifications as they're running. So let's register this web hook with

**[34:02]** So let's register this web hook with

**[34:02]** So let's register this web hook with Manis. So all we got to do is basically

**[34:05]** Manis. So all we got to do is basically

**[34:05]** Manis. So all we got to do is basically post to Manis. Um I you have a base URL

**[34:08]** post to Manis. Um I you have a base URL

**[34:08]** post to Manis. Um I you have a base URL that we have uh manus

**[34:11]** that we have uh manus

**[34:11]** that we have uh manus api.mmanis

**[34:13]** api.mmanis

**[34:13]** api.mmanis imi let me just double check I think I

**[34:16]** imi let me just double check I think I

**[34:16]** imi let me just double check I think I have that the base URL is api.mmanis.ai

**[34:19]** have that the base URL is api.mmanis.ai

**[34:19]** have that the base URL is api.mmanis.ai AI/V1. And so if you post that, then you

**[34:23]** AI/V1. And so if you post that, then you

**[34:23]** AI/V1. And so if you post that, then you will register a web hook successfully.

**[34:25]** will register a web hook successfully.

**[34:25]** will register a web hook successfully. And in this specific case, the web hook

**[34:27]** And in this specific case, the web hook

**[34:27]** And in this specific case, the web hook we want to register is this one over

**[34:28]** we want to register is this one over

**[34:28]** we want to register is this one over here. You go to the Manis um

**[34:32]** here. You go to the Manis um

**[34:32]** here. You go to the Manis um connector setting over here,

**[34:33]** connector setting over here,

**[34:34]** connector setting over here, integrations built with manus API. Um

**[34:36]** integrations built with manus API. Um

**[34:36]** integrations built with manus API. Um you see that this is it will appear

**[34:38]** you see that this is it will appear

**[34:38]** you see that this is it will appear basically over here the new webbook that

**[34:41]** basically over here the new webbook that

**[34:41]** basically over here the new webbook that you've registered. And so whenever you

**[34:42]** you've registered. And so whenever you

**[34:42]** you've registered. And so whenever you create a task, it will automatically

**[34:44]** create a task, it will automatically

**[34:44]** create a task, it will automatically send you a notification over there.

**[34:47]** send you a notification over there.

**[34:47]** send you a notification over there. So let's create a simple task. Hold on,

**[34:49]** So let's create a simple task. Hold on,

**[34:49]** So let's create a simple task. Hold on, people are still sending me. Um, and so

**[34:52]** people are still sending me. Um, and so

**[34:52]** people are still sending me. Um, and so let's create a simple task over and then

**[34:58]** let's create a simple task over and then

**[34:58]** let's create a simple task over and then try to get it working. Yeah. So we


### [35:00 - 36:00]

**[35:02]** try to get it working. Yeah. So we

**[35:02]** try to get it working. Yeah. So we created what is 2 plus2 provide a brief

**[35:04]** created what is 2 plus2 provide a brief

**[35:04]** created what is 2 plus2 provide a brief answer. This is over here. We seen that

**[35:07]** answer. This is over here. We seen that

**[35:07]** answer. This is over here. We seen that the task is running and it's going to

**[35:09]** the task is running and it's going to

**[35:09]** the task is running and it's going to think a little then it kind of just runs

**[35:13]** think a little then it kind of just runs

**[35:13]** think a little then it kind of just runs like echo 2 plus2 VC or whatever that is

**[35:16]** like echo 2 plus2 VC or whatever that is

**[35:16]** like echo 2 plus2 VC or whatever that is and then it will send you an answer. And

**[35:17]** and then it will send you an answer. And

**[35:17]** and then it will send you an answer. And so you can see over here that now that

**[35:19]** so you can see over here that now that

**[35:19]** so you can see over here that now that the task is completed, you get the full

**[35:21]** the task is completed, you get the full

**[35:21]** the task is completed, you get the full payload over here.

**[35:24]** payload over here.

**[35:24]** payload over here. This is kind of what it looks like. And

**[35:26]** This is kind of what it looks like. And

**[35:26]** This is kind of what it looks like. And if let's say we paste this

**[35:47]** but basically you get back um at this

**[35:47]** but basically you get back um at this point you get the ID of that you have.

**[35:49]** point you get the ID of that you have.

**[35:49]** point you get the ID of that you have. So what this means is if if you have

**[35:50]** So what this means is if if you have

**[35:50]** So what this means is if if you have multiple sort of manage tasks that

**[35:52]** multiple sort of manage tasks that

**[35:52]** multiple sort of manage tasks that running you can identify them by the

**[35:53]** running you can identify them by the

**[35:53]** running you can identify them by the task ID. You can also get back the

**[35:55]** task ID. You can also get back the

**[35:55]** task ID. You can also get back the current task URL. You get the output of

**[35:57]** current task URL. You get the output of

**[35:58]** current task URL. You get the output of it which in this case the status is


### [36:00 - 37:00]

**[36:00]** it which in this case the status is

**[36:00]** it which in this case the status is completed. We sent that we sent to

**[36:01]** completed. We sent that we sent to

**[36:02]** completed. We sent that we sent to manage what is 2 plus2 please provide a

**[36:03]** manage what is 2 plus2 please provide a

**[36:03]** manage what is 2 plus2 please provide a brief answer and then we said let me

**[36:06]** brief answer and then we said let me

**[36:06]** brief answer and then we said let me calculate that for you and people are

**[36:08]** calculate that for you and people are

**[36:08]** calculate that for you and people are really running it quite a fair bit. Um

**[36:11]** really running it quite a fair bit. Um

**[36:11]** really running it quite a fair bit. Um and so now that we've actually processed

**[36:14]** and so now that we've actually processed

**[36:14]** and so now that we've actually processed the web poker notification um what we

**[36:17]** the web poker notification um what we

**[36:17]** the web poker notification um what we might want to do is we want to just get

**[36:19]** might want to do is we want to just get

**[36:19]** might want to do is we want to just get the entire conversation history. And so

**[36:21]** the entire conversation history. And so

**[36:21]** the entire conversation history. And so to do so, we can set a simple secret

**[36:23]** to do so, we can set a simple secret

**[36:23]** to do so, we can set a simple secret over here. And so what this allows you

**[36:25]** over here. And so what this allows you

**[36:25]** over here. And so what this allows you to do is that when you're running your

**[36:26]** to do is that when you're running your

**[36:26]** to do is that when you're running your modal server, you basically are able to

**[36:28]** modal server, you basically are able to

**[36:28]** modal server, you basically are able to make a request to the Madness API and

**[36:30]** make a request to the Madness API and

**[36:30]** make a request to the Madness API and get back um a list of every single um

**[36:32]** get back um a list of every single um

**[36:32]** get back um a list of every single um chat message that's been happening in

**[36:34]** chat message that's been happening in

**[36:34]** chat message that's been happening in there. I've done this ahead of time and

**[36:35]** there. I've done this ahead of time and

**[36:35]** there. I've done this ahead of time and so

**[36:37]** so

**[36:37]** so we can just

**[36:39]** we can just

**[36:39]** we can just put this over here.

**[36:45]** So all this does is that if it's done,

**[36:45]** So all this does is that if it's done, it just get a full request and it gets t

**[36:47]** it just get a full request and it gets t

**[36:47]** it just get a full request and it gets t details. And so what you saw with there

**[36:48]** details. And so what you saw with there

**[36:48]** details. And so what you saw with there was basically what happens uh when we do

**[36:49]** was basically what happens uh when we do

**[36:50]** was basically what happens uh when we do this ahead of time.

**[36:52]** this ahead of time.

**[36:52]** this ahead of time. So now let's um so that is basically web

**[36:56]** So now let's um so that is basically web

**[36:56]** So now let's um so that is basically web hooks.

**[36:56]** hooks.

**[36:56]** hooks. >> Yeah.

**[36:57]** >> Yeah.

**[36:57]** >> Yeah. >> So in the previous so right now we've

**[36:59]** >> So in the previous so right now we've

**[36:59]** >> So in the previous so right now we've looked at how to create a task. Uh we've


### [37:00 - 38:00]

**[37:00]** looked at how to create a task. Uh we've

**[37:00]** looked at how to create a task. Uh we've looked at basically how to upload files

**[37:03]** looked at basically how to upload files

**[37:03]** looked at basically how to upload files and then we've also covered like how to

**[37:04]** and then we've also covered like how to

**[37:04]** and then we've also covered like how to use a web hook. Um

**[37:07]** use a web hook. Um

**[37:07]** use a web hook. Um so let's now look at basically how to

**[37:09]** so let's now look at basically how to

**[37:09]** so let's now look at basically how to use slack which I think will be a lot

**[37:10]** use slack which I think will be a lot

**[37:10]** use slack which I think will be a lot more fun. So in the previous notebook we

**[37:13]** more fun. So in the previous notebook we

**[37:13]** more fun. So in the previous notebook we looked at how to use web hook. So case

**[37:14]** looked at how to use web hook. So case

**[37:14]** looked at how to use web hook. So case we're going to start integrating on

**[37:15]** we're going to start integrating on

**[37:15]** we're going to start integrating on slack. I've created a Slack workspace

**[37:17]** slack. I've created a Slack workspace

**[37:17]** slack. I've created a Slack workspace for myself. Uh it's just on I personal.

**[37:20]** for myself. Uh it's just on I personal.

**[37:20]** for myself. Uh it's just on I personal. And so in this small channel over here,

**[37:22]** And so in this small channel over here,

**[37:22]** And so in this small channel over here, we're going to be interacting with our

**[37:23]** we're going to be interacting with our

**[37:23]** we're going to be interacting with our manage chatbot.

**[37:26]** manage chatbot.

**[37:26]** manage chatbot. So first thing you want to do is you

**[37:28]** So first thing you want to do is you

**[37:28]** So first thing you want to do is you want to make sure that you have your

**[37:29]** want to make sure that you have your

**[37:29]** want to make sure that you have your Slack um signing secrets. These are

**[37:33]** Slack um signing secrets. These are

**[37:33]** Slack um signing secrets. These are basically I have instructions on the

**[37:34]** basically I have instructions on the

**[37:34]** basically I have instructions on the read me on how to get the bot signing

**[37:36]** read me on how to get the bot signing

**[37:36]** read me on how to get the bot signing secrets. Then you want to basically test

**[37:38]** secrets. Then you want to basically test

**[37:38]** secrets. Then you want to basically test it. Slack provides a off test.

**[37:42]** it. Slack provides a off test.

**[37:42]** it. Slack provides a off test. So in Ivan personal for the bot mani you

**[37:44]** So in Ivan personal for the bot mani you

**[37:44]** So in Ivan personal for the bot mani you can basically test to see that your

**[37:46]** can basically test to see that your

**[37:46]** can basically test to see that your secrets are working as intended and so

**[37:48]** secrets are working as intended and so

**[37:48]** secrets are working as intended and so this is really important because if your

**[37:49]** this is really important because if your

**[37:49]** this is really important because if your environment variables are not correctly

**[37:51]** environment variables are not correctly

**[37:51]** environment variables are not correctly set up then you're not going to be able

**[37:52]** set up then you're not going to be able

**[37:52]** set up then you're not going to be able to do this.

**[37:55]** to do this.

**[37:55]** to do this. Okay cool let's run this bit by bit. So

**[37:58]** Okay cool let's run this bit by bit. So

**[37:58]** Okay cool let's run this bit by bit. So we're going to just start by defining a


### [38:00 - 39:00]

**[38:00]** we're going to just start by defining a

**[38:00]** we're going to just start by defining a simple um slide simple bot over here.

**[38:05]** simple um slide simple bot over here.

**[38:05]** simple um slide simple bot over here. Just going to call this

**[38:08]** Just going to call this

**[38:08]** Just going to call this bot. Y

**[38:11]** bot. Y

**[38:11]** bot. Y and so let's run mod surf chat.

**[38:21]** And so when you run this black ipy,

**[38:21]** And so when you run this black ipy, you'll find that what you need to do

**[38:23]** you'll find that what you need to do

**[38:23]** you'll find that what you need to do then is

**[38:26]** then is

**[38:26]** then is we've initialized a simple model app.

**[38:28]** we've initialized a simple model app.

**[38:28]** we've initialized a simple model app. We've added some dependencies. We have

**[38:30]** We've added some dependencies. We have

**[38:30]** We've added some dependencies. We have the slack secret over here that we

**[38:32]** the slack secret over here that we

**[38:32]** the slack secret over here that we stored ahead of time. And then we just

**[38:34]** stored ahead of time. And then we just

**[38:34]** stored ahead of time. And then we just have a single endpoint over here that's

**[38:35]** have a single endpoint over here that's

**[38:35]** have a single endpoint over here that's called slash web hooks slack. And so you

**[38:39]** called slash web hooks slack. And so you

**[38:39]** called slash web hooks slack. And so you will have something like this where you

**[38:40]** will have something like this where you

**[38:40]** will have something like this where you have like a simple like endpoint that

**[38:42]** have like a simple like endpoint that

**[38:42]** have like a simple like endpoint that you can hit. And so in my case um this

**[38:44]** you can hit. And so in my case um this

**[38:44]** you can hit. And so in my case um this will be the endpoint that I have right.

**[38:47]** will be the endpoint that I have right.

**[38:47]** will be the endpoint that I have right. And so you can see that if we hit this

**[38:49]** And so you can see that if we hit this

**[38:49]** And so you can see that if we hit this endpoint over here

**[38:58]** it takes a while to run

**[38:58]** it takes a while to run but basically get back status. Okay. And

**[38:59]** but basically get back status. Okay. And

**[38:59]** but basically get back status. Okay. And so what this means that this is a


### [39:00 - 40:00]

**[39:00]** so what this means that this is a

**[39:00]** so what this means that this is a publicly available like endpoint for you

**[39:02]** publicly available like endpoint for you

**[39:02]** publicly available like endpoint for you to hit. So when you mention anyone on

**[39:05]** to hit. So when you mention anyone on

**[39:05]** to hit. So when you mention anyone on Slack, for example, over here, um before

**[39:07]** Slack, for example, over here, um before

**[39:07]** Slack, for example, over here, um before our bot is configured, if you just

**[39:08]** our bot is configured, if you just

**[39:08]** our bot is configured, if you just something like money like what's up,

**[39:11]** something like money like what's up,

**[39:11]** something like money like what's up, um you're going to get a message from

**[39:13]** um you're going to get a message from

**[39:13]** um you're going to get a message from Slack similar to how the manage API

**[39:15]** Slack similar to how the manage API

**[39:15]** Slack similar to how the manage API worked, you're going to get a web hook

**[39:17]** worked, you're going to get a web hook

**[39:17]** worked, you're going to get a web hook with some sort of payload. And this

**[39:18]** with some sort of payload. And this

**[39:18]** with some sort of payload. And this enables you to essentially be able to um

**[39:21]** enables you to essentially be able to um

**[39:21]** enables you to essentially be able to um look at the input and you're going to

**[39:23]** look at the input and you're going to

**[39:23]** look at the input and you're going to get something like um

**[39:29]** so you're going to get like some sort of

**[39:29]** so you're going to get like some sort of information from stack, right? So we

**[39:31]** information from stack, right? So we

**[39:31]** information from stack, right? So we have this um

**[39:37]** over here. Let's go to Slack API.

**[39:37]** over here. Let's go to Slack API. Slack.apps,

**[39:39]** Slack.apps,

**[39:40]** Slack.apps, right?

**[39:42]** right?

**[39:42]** right? So we want to just make sure that

**[39:45]** So we want to just make sure that

**[39:46]** So we want to just make sure that so previously we made sure that the

**[39:47]** so previously we made sure that the

**[39:47]** so previously we made sure that the Slack that that our server was able to

**[39:49]** Slack that that our server was able to

**[39:49]** Slack that that our server was able to receive a response. And so the next step

**[39:51]** receive a response. And so the next step

**[39:51]** receive a response. And so the next step that we're going to do is we're going to

**[39:52]** that we're going to do is we're going to

**[39:52]** that we're going to do is we're going to make sure that our server is able to be

**[39:53]** make sure that our server is able to be

**[39:53]** make sure that our server is able to be registered as a web on Slack. when you

**[39:55]** registered as a web on Slack. when you

**[39:55]** registered as a web on Slack. when you actually make a request to Slack, you

**[39:57]** actually make a request to Slack, you

**[39:57]** actually make a request to Slack, you need to make sure that when you respond,

**[39:58]** need to make sure that when you respond,

**[39:58]** need to make sure that when you respond, you actually get back you get back a

**[39:59]** you actually get back you get back a

**[39:59]** you actually get back you get back a challenge URL. So,


### [40:00 - 41:00]

**[40:03]** challenge URL. So,

**[40:03]** challenge URL. So, this is what you can see. We just rerun

**[40:06]** this is what you can see. We just rerun

**[40:06]** this is what you can see. We just rerun this. And we have this URL over here.

**[40:08]** this. And we have this URL over here.

**[40:08]** this. And we have this URL over here. And then we're just going to put

**[40:12]** And then we're just going to put

**[40:12]** And then we're just going to put inside the event subscription,

**[40:23]** right? Right. So this is verified and

**[40:23]** right? Right. So this is verified and what happened was that you know Slack

**[40:25]** what happened was that you know Slack

**[40:25]** what happened was that you know Slack basically sent us in the API request and

**[40:28]** basically sent us in the API request and

**[40:28]** basically sent us in the API request and we were able to successfully respond to

**[40:30]** we were able to successfully respond to

**[40:30]** we were able to successfully respond to it with a challenge.

**[40:32]** it with a challenge.

**[40:32]** it with a challenge. And so if you see like a verified over

**[40:34]** And so if you see like a verified over

**[40:34]** And so if you see like a verified over here you just need to save the changes

**[40:35]** here you just need to save the changes

**[40:35]** here you just need to save the changes and that should work you


### [41:00 - 42:00]

**[41:00]** Then once you've done this,

**[41:00]** Then once you've done this, we mentioned our bot in Slack. Let me

**[41:02]** we mentioned our bot in Slack. Let me

**[41:02]** we mentioned our bot in Slack. Let me just check.

**[41:13]** We should get a API request from stack.

**[41:13]** We should get a API request from stack. And so you can see that this was the

**[41:15]** And so you can see that this was the

**[41:15]** And so you can see that this was the mention over here. So over here I said

**[41:18]** mention over here. So over here I said

**[41:18]** mention over here. So over here I said add money what's up and over here you

**[41:19]** add money what's up and over here you

**[41:19]** add money what's up and over here you see here's a text what's up right

**[41:22]** see here's a text what's up right

**[41:22]** see here's a text what's up right and what you find is that if you just

**[41:24]** and what you find is that if you just

**[41:24]** and what you find is that if you just get the raw text you're going to get the

**[41:25]** get the raw text you're going to get the

**[41:25]** get the raw text you're going to get the user ID and that is something that you

**[41:27]** user ID and that is something that you

**[41:27]** user ID and that is something that you want to parse out in the response

**[41:30]** want to parse out in the response

**[41:30]** want to parse out in the response cool so let's try to figure out how to

**[41:32]** cool so let's try to figure out how to

**[41:32]** cool so let's try to figure out how to respond to Slack over here right if I'm

**[41:35]** respond to Slack over here right if I'm

**[41:35]** respond to Slack over here right if I'm just going to copy and paste this entire

**[41:36]** just going to copy and paste this entire

**[41:36]** just going to copy and paste this entire Slack event that we previously

**[41:51]** So this is the Slack. I'm just going to

**[41:51]** So this is the Slack. I'm just going to paste the Slack event over here so that

**[41:53]** paste the Slack event over here so that

**[41:53]** paste the Slack event over here so that we're able to

**[41:55]** we're able to

**[41:55]** we're able to have it for context. And

**[41:58]** have it for context. And

**[41:58]** have it for context. And when we want to send a response back to


### [42:00 - 43:00]

**[42:00]** when we want to send a response back to

**[42:00]** when we want to send a response back to Slack, what we need is basically the

**[42:02]** Slack, what we need is basically the

**[42:02]** Slack, what we need is basically the channel that was sent in the thread TS.

**[42:04]** channel that was sent in the thread TS.

**[42:04]** channel that was sent in the thread TS. And so that's how Slack identifies the

**[42:05]** And so that's how Slack identifies the

**[42:06]** And so that's how Slack identifies the right item. And so let's get it from you

**[42:08]** right item. And so let's get it from you

**[42:08]** right item. And so let's get it from you can really get it over here. So

**[42:12]** can really get it over here. So

**[42:12]** can really get it over here. So you want to get the channel

**[42:20]** then you want to get the event. Yes.

**[42:20]** then you want to get the event. Yes. Right.

**[42:26]** So let's send a response. And you can

**[42:26]** So let's send a response. And you can see that in Slack over here we got a

**[42:28]** see that in Slack over here we got a

**[42:28]** see that in Slack over here we got a response that said hello world. And so

**[42:30]** response that said hello world. And so

**[42:30]** response that said hello world. And so this is really kind of how your

**[42:31]** this is really kind of how your

**[42:31]** this is really kind of how your application will work. If you're

**[42:33]** application will work. If you're

**[42:33]** application will work. If you're building a Slack bot, you get a you get

**[42:34]** building a Slack bot, you get a you get

**[42:34]** building a Slack bot, you get a you get an API request from Slack and then once

**[42:36]** an API request from Slack and then once

**[42:36]** an API request from Slack and then once you get the API request from Slack, you

**[42:38]** you get the API request from Slack, you

**[42:38]** you get the API request from Slack, you do something and then you return it

**[42:39]** do something and then you return it

**[42:39]** do something and then you return it back. One of the things to note when

**[42:41]** back. One of the things to note when

**[42:41]** back. One of the things to note when you're building on Slack is just that

**[42:42]** you're building on Slack is just that

**[42:42]** you're building on Slack is just that you need to send a response in roughly

**[42:44]** you need to send a response in roughly

**[42:44]** you need to send a response in roughly like 3 seconds. Uh if not, they're going

**[42:46]** like 3 seconds. Uh if not, they're going

**[42:46]** like 3 seconds. Uh if not, they're going to try again. And so if you're building

**[42:47]** to try again. And so if you're building

**[42:47]** to try again. And so if you're building any sort of Slack bot, you want to

**[42:49]** any sort of Slack bot, you want to

**[42:49]** any sort of Slack bot, you want to ideally keep some sort of server warm.

**[42:57]** So let's try again to maybe, you know,

**[42:57]** So let's try again to maybe, you know, in this case, we're going to send some

**[42:59]** in this case, we're going to send some

**[42:59]** in this case, we're going to send some files over here. So let's say we want to


### [43:00 - 44:00]

**[43:01]** files over here. So let's say we want to

**[43:01]** files over here. So let's say we want to send

**[43:03]** send

**[43:03]** send the bookshyway Bshireway 2025 investor

**[43:07]** the bookshyway Bshireway 2025 investor

**[43:07]** the bookshyway Bshireway 2025 investor letter. Well with Slack what you can do

**[43:09]** letter. Well with Slack what you can do

**[43:09]** letter. Well with Slack what you can do is you can basically just upload the

**[43:11]** is you can basically just upload the

**[43:11]** is you can basically just upload the file first. And so let's try uploading

**[43:13]** file first. And so let's try uploading

**[43:13]** file first. And so let's try uploading it to the right channel

**[43:22]** and let's upload it here.

**[43:22]** and let's upload it here. So now we have it uploaded to the

**[43:24]** So now we have it uploaded to the

**[43:24]** So now we have it uploaded to the channel. We have an ID and we can

**[43:25]** channel. We have an ID and we can

**[43:25]** channel. We have an ID and we can actually post the same message over here

**[43:37]** box. So I've added so previously you saw

**[43:37]** box. So I've added so previously you saw that we got a Slack file ID and then

**[43:39]** that we got a Slack file ID and then

**[43:39]** that we got a Slack file ID and then when you have the Slack file ID when you

**[43:41]** when you have the Slack file ID when you

**[43:41]** when you have the Slack file ID when you post a message you just upload a file we

**[43:42]** post a message you just upload a file we

**[43:42]** post a message you just upload a file we get back a list of ids and that is

**[43:45]** get back a list of ids and that is

**[43:45]** get back a list of ids and that is included as part of the attachment

**[43:46]** included as part of the attachment

**[43:46]** included as part of the attachment itself. And so let's say over here we're

**[43:49]** itself. And so let's say over here we're

**[43:49]** itself. And so let's say over here we're going to take this the channel that we

**[43:50]** going to take this the channel that we

**[43:50]** going to take this the channel that we previously used


### [44:00 - 45:00]

**[44:14]** Yeah. So if you look back at this chat

**[44:14]** Yeah. So if you look back at this chat over here, you can see that we sent we

**[44:15]** over here, you can see that we sent we

**[44:15]** over here, you can see that we sent we essentially first one over here uploaded

**[44:17]** essentially first one over here uploaded

**[44:17]** essentially first one over here uploaded it to the channel and then the second

**[44:18]** it to the channel and then the second

**[44:18]** it to the channel and then the second one at the bottom over here basically

**[44:20]** one at the bottom over here basically

**[44:20]** one at the bottom over here basically sent the same thing over there with

**[44:21]** sent the same thing over there with

**[44:21]** sent the same thing over there with hello world. Um one of the problems you

**[44:23]** hello world. Um one of the problems you

**[44:23]** hello world. Um one of the problems you find over here is that we actually

**[44:24]** find over here is that we actually

**[44:24]** find over here is that we actually didn't upload it to the right thread,

**[44:26]** didn't upload it to the right thread,

**[44:26]** didn't upload it to the right thread, right? We uploaded to the channel and so

**[44:28]** right? We uploaded to the channel and so

**[44:28]** right? We uploaded to the channel and so when you're working with files in Slack,

**[44:30]** when you're working with files in Slack,

**[44:30]** when you're working with files in Slack, you need to make sure that you keep this

**[44:31]** you need to make sure that you keep this

**[44:31]** you need to make sure that you keep this in mind. And so this is um basically how

**[44:34]** in mind. And so this is um basically how

**[44:34]** in mind. And so this is um basically how you work with files in Slack. And so

**[44:36]** you work with files in Slack. And so

**[44:36]** you work with files in Slack. And so let's now try to get Mattis involved

**[44:39]** let's now try to get Mattis involved

**[44:39]** let's now try to get Mattis involved over here.

**[44:42]** over here.

**[44:42]** over here. Okay. So now we're going to build slide

**[44:46]** Okay. So now we're going to build slide

**[44:46]** Okay. So now we're going to build slide integration.


### [45:00 - 46:00]

**[45:05]** So up ahead we had these functions over

**[45:05]** So up ahead we had these functions over here and so we can just use them to just

**[45:08]** here and so we can just use them to just

**[45:08]** here and so we can just use them to just add it in.

**[45:47]** We're going to add this Slack message

**[45:47]** We're going to add this Slack message over here using at night event. That's

**[45:49]** over here using at night event. That's

**[45:49]** over here using at night event. That's from the Slack SDK.


### [46:00 - 47:00]

**[46:13]** So we previously defined a function

**[46:13]** So we previously defined a function called postlike message and so let's

**[46:15]** called postlike message and so let's

**[46:15]** called postlike message and so let's make sure that we have that running.

**[46:27]** Then we had a bunch of different helper

**[46:27]** Then we had a bunch of different helper functions up here. So let's uh make sure

**[46:29]** functions up here. So let's uh make sure

**[46:29]** functions up here. So let's uh make sure that we also copy them. Right.

**[46:38]** So data class is not defined. All I need

**[46:38]** So data class is not defined. All I need to do over here is just define a data

**[46:40]** to do over here is just define a data

**[46:40]** to do over here is just define a data class. Then file I file ID.

**[46:51]** Cool. So, now that we've added in a

**[46:52]** Cool. So, now that we've added in a whole bunch of these different things

**[46:53]** whole bunch of these different things

**[46:53]** whole bunch of these different things that we previously had, um,


### [47:00 - 48:00]

**[47:00]** let's see how this works on the main

**[47:00]** let's see how this works on the main Slack. Uh,

**[47:21]** So with this what our goal is to

**[47:21]** So with this what our goal is to basically to reproduce what we did in

**[47:22]** basically to reproduce what we did in

**[47:22]** basically to reproduce what we did in the notebook manually. So let's try to

**[47:24]** the notebook manually. So let's try to

**[47:24]** the notebook manually. So let's try to see if this works out of manner group is

**[47:27]** see if this works out of manner group is

**[47:27]** see if this works out of manner group is not defined.


### [48:00 - 49:00]

**[48:06]** so we had a small bug over there and so

**[48:06]** so we had a small bug over there and so previously what we did in the previous

**[48:07]** previously what we did in the previous

**[48:07]** previously what we did in the previous portion was that we tried to basically

**[48:09]** portion was that we tried to basically

**[48:09]** portion was that we tried to basically uh get Slack working with a web and so

**[48:12]** uh get Slack working with a web and so

**[48:12]** uh get Slack working with a web and so what I did wrongly was just that if I

**[48:17]** what I did wrongly was just that if I

**[48:17]** what I did wrongly was just that if I I didn't define like the manage URL and

**[48:19]** I didn't define like the manage URL and

**[48:20]** I didn't define like the manage URL and so let's just have it run over here.

**[48:26]** So you can see that now we have a

**[48:26]** So you can see that now we have a response of what we did manually just

**[48:28]** response of what we did manually just

**[48:28]** response of what we did manually just copying it bit by bit right and so this

**[48:30]** copying it bit by bit right and so this

**[48:30]** copying it bit by bit right and so this mean with this we've now figured out how

**[48:32]** mean with this we've now figured out how

**[48:32]** mean with this we've now figured out how to basically work with slack if I send a

**[48:34]** to basically work with slack if I send a

**[48:34]** to basically work with slack if I send a message I can get a web hook and I can

**[48:35]** message I can get a web hook and I can

**[48:35]** message I can get a web hook and I can process it with my modal server right

**[48:38]** process it with my modal server right

**[48:38]** process it with my modal server right this is a really simple sort of approach

**[48:40]** this is a really simple sort of approach

**[48:40]** this is a really simple sort of approach but it's really useful when it comes to

**[48:41]** but it's really useful when it comes to

**[48:41]** but it's really useful when it comes to doing anything else you can imagine that

**[48:43]** doing anything else you can imagine that

**[48:43]** doing anything else you can imagine that for you if let's say you're doing some

**[48:44]** for you if let's say you're doing some

**[48:44]** for you if let's say you're doing some sort of complex processing you might get

**[48:47]** sort of complex processing you might get

**[48:47]** sort of complex processing you might get the user's information get some sort of

**[48:48]** the user's information get some sort of

**[48:48]** the user's information get some sort of metadata from the user fetch the prior

**[48:50]** metadata from the user fetch the prior

**[48:50]** metadata from the user fetch the prior conversations and then actually start

**[48:52]** conversations and then actually start

**[48:52]** conversations and then actually start sending the task over to manage to start

**[48:54]** sending the task over to manage to start

**[48:54]** sending the task over to manage to start executing

**[48:56]** executing

**[48:56]** executing So let's now see how we can actually get

**[48:58]** So let's now see how we can actually get

**[48:58]** So let's now see how we can actually get this running with manus. So


### [49:00 - 50:00]

**[49:01]** this running with manus. So

**[49:01]** this running with manus. So I have a function over here called

**[49:03]** I have a function over here called

**[49:03]** I have a function over here called create a manus task. It does something

**[49:04]** create a manus task. It does something

**[49:04]** create a manus task. It does something very similar to what we did previously

**[49:05]** very similar to what we did previously

**[49:05]** very similar to what we did previously which was that we'll post a request to

**[49:07]** which was that we'll post a request to

**[49:07]** which was that we'll post a request to manice. We would have a basically an

**[49:09]** manice. We would have a basically an

**[49:09]** manice. We would have a basically an environment variable that we send it

**[49:10]** environment variable that we send it

**[49:10]** environment variable that we send it along with and then we would then in

**[49:12]** along with and then we would then in

**[49:12]** along with and then we would then in this case just send a prompt. Right? So

**[49:14]** this case just send a prompt. Right? So

**[49:14]** this case just send a prompt. Right? So let's test it out. create a manage task

**[49:18]** let's test it out. create a manage task

**[49:18]** let's test it out. create a manage task and then instead of this over here,

**[49:22]** and then instead of this over here,

**[49:22]** and then instead of this over here, we're gonna create a manage task.

**[49:41]** task ids like this and then we say file

**[49:41]** task ids like this and then we say file created successfully. You can view it

**[49:42]** created successfully. You can view it

**[49:42]** created successfully. You can view it here.

**[49:44]** here.

**[49:44]** here. So I'm just going to add a simple um

**[49:47]** So I'm just going to add a simple um

**[49:47]** So I'm just going to add a simple um wake up function so that we can just

**[49:48]** wake up function so that we can just

**[49:48]** wake up function so that we can just wake this um SP.

**[49:53]** wake this um SP.

**[49:53]** wake this um SP. >> So let me just go back to the web app.

**[49:57]** >> So let me just go back to the web app.

**[49:57]** >> So let me just go back to the web app. Sure it's running. It's woken up. And

**[49:58]** Sure it's running. It's woken up. And

**[49:58]** Sure it's running. It's woken up. And then let's try to kick off a task in


### [50:00 - 51:00]

**[50:00]** then let's try to kick off a task in

**[50:00]** then let's try to kick off a task in Madness.

**[50:18]** Oh, so now we've uh got a post request

**[50:18]** Oh, so now we've uh got a post request and manus replies with the fact that

**[50:20]** and manus replies with the fact that

**[50:20]** and manus replies with the fact that hey, we've created a task successfully

**[50:21]** hey, we've created a task successfully

**[50:22]** hey, we've created a task successfully with Mattis. So, let's take a look at

**[50:23]** with Mattis. So, let's take a look at

**[50:23]** with Mattis. So, let's take a look at this task and see how it's been. Task

**[50:26]** this task and see how it's been. Task

**[50:26]** this task and see how it's been. Task should appear inside here. What's the

**[50:28]** should appear inside here. What's the

**[50:28]** should appear inside here. What's the weather in New York? Right? So, one

**[50:29]** weather in New York? Right? So, one

**[50:29]** weather in New York? Right? So, one thing you've noticed is that we don't

**[50:31]** thing you've noticed is that we don't

**[50:31]** thing you've noticed is that we don't actually get the response. Right? We can

**[50:32]** actually get the response. Right? We can

**[50:32]** actually get the response. Right? We can send these um current task over to

**[50:34]** send these um current task over to

**[50:34]** send these um current task over to manage. We can pick some of these task

**[50:36]** manage. We can pick some of these task

**[50:36]** manage. We can pick some of these task off, but we don't get the response. So,

**[50:38]** off, but we don't get the response. So,

**[50:38]** off, but we don't get the response. So, let's see how we can

**[50:47]** fix that. Yeah.

**[50:47]** fix that. Yeah. So,

**[50:53]** what we're going to be doing is we're

**[50:53]** what we're going to be doing is we're just going to be checking over here.


### [51:00 - 52:00]

**[51:00]** Sorry, let me let me go back. Sorry,

**[51:00]** Sorry, let me let me go back. Sorry, guys. I'm just a bit stressed out today.

**[51:02]** guys. I'm just a bit stressed out today.

**[51:02]** guys. I'm just a bit stressed out today. Okay. Anyway, one thing that um we saw

**[51:05]** Okay. Anyway, one thing that um we saw

**[51:05]** Okay. Anyway, one thing that um we saw just now over there was that this is

**[51:06]** just now over there was that this is

**[51:06]** just now over there was that this is kind of an ugly setup. And so what we're

**[51:08]** kind of an ugly setup. And so what we're

**[51:08]** kind of an ugly setup. And so what we're going to be doing is just making it a

**[51:09]** going to be doing is just making it a

**[51:09]** going to be doing is just making it a little bit prettier. Um if you notice in

**[51:11]** little bit prettier. Um if you notice in

**[51:11]** little bit prettier. Um if you notice in the text you get the basically the ID of

**[51:13]** the text you get the basically the ID of

**[51:13]** the text you get the basically the ID of the um user. In this case when I tag

**[51:15]** the um user. In this case when I tag

**[51:15]** the um user. In this case when I tag Manny add Manny you sort of there was

**[51:17]** Manny add Manny you sort of there was

**[51:17]** Manny add Manny you sort of there was this really ugly section over here where

**[51:19]** this really ugly section over here where

**[51:19]** this really ugly section over here where it said um you look at the text you get

**[51:22]** it said um you look at the text you get

**[51:22]** it said um you look at the text you get this 09 FDL. If you use the Slack API

**[51:25]** this 09 FDL. If you use the Slack API

**[51:25]** this 09 FDL. If you use the Slack API what you find is that you're basically

**[51:26]** what you find is that you're basically

**[51:26]** what you find is that you're basically able to get a list of all the users and

**[51:28]** able to get a list of all the users and

**[51:28]** able to get a list of all the users and you can then do some parsing. You might

**[51:29]** you can then do some parsing. You might

**[51:29]** you can then do some parsing. You might have some additional data on like what

**[51:31]** have some additional data on like what

**[51:32]** have some additional data on like what exactly that this user represents in

**[51:33]** exactly that this user represents in

**[51:33]** exactly that this user represents in your database. But over here, we'll just

**[51:35]** your database. But over here, we'll just

**[51:35]** your database. But over here, we'll just try to make it a bit prettier for now.

**[51:38]** try to make it a bit prettier for now.

**[51:38]** try to make it a bit prettier for now. So, we're just going to update the post

**[51:40]** So, we're just going to update the post

**[51:40]** So, we're just going to update the post like

**[51:43]** like

**[51:43]** like Slack message.

**[51:46]** Slack message.

**[51:46]** Slack message. So,

**[51:48]** So,

**[51:48]** So, we're going to just update this message

**[51:50]** we're going to just update this message

**[51:50]** we're going to just update this message over here.

**[51:57]** Then, we have a bunch of these different

**[51:58]** Then, we have a bunch of these different types. So, we just need to update them.


### [52:00 - 53:00]

**[52:01]** types. So, we just need to update them.

**[52:01]** types. So, we just need to update them. Then, from typing, we'll just add

**[52:02]** Then, from typing, we'll just add

**[52:02]** Then, from typing, we'll just add optional

**[52:10]** Then the Slack response up here.

**[52:10]** Then the Slack response up here. Slack response.

**[52:13]** Slack response.

**[52:13]** Slack response. Yeah, we just need to import the Slack

**[52:15]** Yeah, we just need to import the Slack

**[52:15]** Yeah, we just need to import the Slack response. So we get something that's

**[52:16]** response. So we get something that's

**[52:16]** response. So we get something that's typed. And that should be

**[52:24]** And so

**[52:24]** And so now we post a message. We have blocks.

**[52:26]** now we post a message. We have blocks.

**[52:26]** now we post a message. We have blocks. Um,

**[52:55]** so we're just going to make this a

**[52:55]** so we're just going to make this a little bit nicer. over here with Manis.

**[52:57]** little bit nicer. over here with Manis.

**[52:57]** little bit nicer. over here with Manis. And so what this means is that over

**[52:59]** And so what this means is that over

**[52:59]** And so what this means is that over here, Slack has this wonderful thing


### [53:00 - 54:00]

**[53:00]** here, Slack has this wonderful thing

**[53:00]** here, Slack has this wonderful thing they ship called Slack Blockit. So you

**[53:02]** they ship called Slack Blockit. So you

**[53:02]** they ship called Slack Blockit. So you can c if you've used a lot of these

**[53:03]** can c if you've used a lot of these

**[53:04]** can c if you've used a lot of these Slack bots previously, you'll find that

**[53:05]** Slack bots previously, you'll find that

**[53:05]** Slack bots previously, you'll find that they ship these nice little buttons. And

**[53:07]** they ship these nice little buttons. And

**[53:07]** they ship these nice little buttons. And so you can actually do that out of the

**[53:08]** so you can actually do that out of the

**[53:08]** so you can actually do that out of the box with this thing called blockhead. So

**[53:11]** box with this thing called blockhead. So

**[53:11]** box with this thing called blockhead. So what we'll be doing over here is we're

**[53:12]** what we'll be doing over here is we're

**[53:12]** what we'll be doing over here is we're just going to add this thing called we

**[53:13]** just going to add this thing called we

**[53:13]** just going to add this thing called we started working on our request. And then

**[53:15]** started working on our request. And then

**[53:15]** started working on our request. And then we'll add the URL over here and a little

**[53:16]** we'll add the URL over here and a little

**[53:16]** we'll add the URL over here and a little emoji called view on web. And the URL

**[53:19]** emoji called view on web. And the URL

**[53:19]** emoji called view on web. And the URL over here would just be the task URL

**[53:20]** over here would just be the task URL

**[53:20]** over here would just be the task URL that we have. And so with the post like

**[53:23]** that we have. And so with the post like

**[53:23]** that we have. And so with the post like message, we can just add blocks to be

**[53:24]** message, we can just add blocks to be

**[53:24]** message, we can just add blocks to be blocks.

**[53:29]** And so

**[53:29]** And so since the blocks will be sent over, I

**[53:31]** since the blocks will be sent over, I

**[53:31]** since the blocks will be sent over, I think we can let's see if this works.

**[53:34]** think we can let's see if this works.

**[53:34]** think we can let's see if this works. Let's hope this works.

**[53:37]** Let's hope this works.

**[53:37]** Let's hope this works. And then I'm just going to go back and

**[53:39]** And then I'm just going to go back and

**[53:39]** And then I'm just going to go back and remove the original. Since we're no

**[53:41]** remove the original. Since we're no

**[53:41]** remove the original. Since we're no longer using the text, we can just use

**[53:42]** longer using the text, we can just use

**[53:42]** longer using the text, we can just use the box. And so let's remove that.

**[53:45]** the box. And so let's remove that.

**[53:45]** the box. And so let's remove that. Let's wake up our server a fair bit over

**[53:47]** Let's wake up our server a fair bit over

**[53:47]** Let's wake up our server a fair bit over here.

**[53:55]** wake up our server. Make sure it's

**[53:55]** wake up our server. Make sure it's running.


### [54:00 - 55:00]

**[54:12]** Cool. And so, oh, additional argument.

**[54:12]** Cool. And so, oh, additional argument. So, I just put over here. We can just

**[54:15]** So, I just put over here. We can just

**[54:15]** So, I just put over here. We can just put like text

**[54:17]** put like text

**[54:17]** put like text was created. I think we don't need it.

**[54:19]** was created. I think we don't need it.

**[54:20]** was created. I think we don't need it. text over here because it's good to go.

**[54:22]** text over here because it's good to go.

**[54:22]** text over here because it's good to go. Yeah, let me try it again.

**[54:40]** So, this um essentially you can see that

**[54:40]** So, this um essentially you can see that now we have a much nicer enriched sort

**[54:42]** now we have a much nicer enriched sort

**[54:42]** now we have a much nicer enriched sort of UI and if you click on this um you'll

**[54:44]** of UI and if you click on this um you'll

**[54:44]** of UI and if you click on this um you'll be able to essentially see like a

**[54:46]** be able to essentially see like a

**[54:46]** be able to essentially see like a message over here. Hey, I'm Manis. your

**[54:48]** message over here. Hey, I'm Manis. your

**[54:48]** message over here. Hey, I'm Manis. your friendly UI, friendly um chat assistant.

**[54:51]** friendly UI, friendly um chat assistant.

**[54:51]** friendly UI, friendly um chat assistant. What do you need from a me today? Right.

**[54:54]** What do you need from a me today? Right.

**[54:54]** What do you need from a me today? Right. Cool. So, with this, we walked through

**[54:56]** Cool. So, with this, we walked through

**[54:56]** Cool. So, with this, we walked through how to create a Slack um task. Manners

**[54:58]** how to create a Slack um task. Manners

**[54:58]** how to create a Slack um task. Manners can now actually receive a message from


### [55:00 - 56:00]

**[55:00]** can now actually receive a message from

**[55:00]** can now actually receive a message from Slack. And so, one thing that's pretty

**[55:02]** Slack. And so, one thing that's pretty

**[55:02]** Slack. And so, one thing that's pretty useful if you've looked at basically any

**[55:03]** useful if you've looked at basically any

**[55:03]** useful if you've looked at basically any of our our Slack bot is that it can take

**[55:05]** of our our Slack bot is that it can take

**[55:05]** of our our Slack bot is that it can take multiple conversations. I send a

**[55:06]** multiple conversations. I send a

**[55:06]** multiple conversations. I send a message, man responds, I send another

**[55:09]** message, man responds, I send another

**[55:09]** message, man responds, I send another message. Um yeah, so what you want to do

**[55:11]** message. Um yeah, so what you want to do

**[55:11]** message. Um yeah, so what you want to do is you want to just enable multi-turn

**[55:12]** is you want to just enable multi-turn

**[55:12]** is you want to just enable multi-turn conversations. And so the way you want

**[55:14]** conversations. And so the way you want

**[55:14]** conversations. And so the way you want to be able to to do so is that you want

**[55:17]** to be able to to do so is that you want

**[55:17]** to be able to to do so is that you want a way just basically to store if you've

**[55:19]** a way just basically to store if you've

**[55:19]** a way just basically to store if you've seen this thread before, right? Because

**[55:21]** seen this thread before, right? Because

**[55:21]** seen this thread before, right? Because if every time you send a message and you

**[55:23]** if every time you send a message and you

**[55:23]** if every time you send a message and you want to post to the same thread, you

**[55:24]** want to post to the same thread, you

**[55:24]** want to post to the same thread, you need to kind of keep track of that. And

**[55:26]** need to kind of keep track of that. And

**[55:26]** need to kind of keep track of that. And so what we'll be using over here is just

**[55:27]** so what we'll be using over here is just

**[55:28]** so what we'll be using over here is just a simple dictionary that Moto ships

**[55:29]** a simple dictionary that Moto ships

**[55:29]** a simple dictionary that Moto ships with. If you're using anything like

**[55:30]** with. If you're using anything like

**[55:30]** with. If you're using anything like Cloudflare, you can use like a KV store.

**[55:33]** Cloudflare, you can use like a KV store.

**[55:33]** Cloudflare, you can use like a KV store. If you're using some sort of database,

**[55:34]** If you're using some sort of database,

**[55:34]** If you're using some sort of database, these are things you can load into the

**[55:36]** these are things you can load into the

**[55:36]** these are things you can load into the database. But that's basically um what

**[55:38]** database. But that's basically um what

**[55:38]** database. But that's basically um what you can use out of the box. And so Moto

**[55:41]** you can use out of the box. And so Moto

**[55:41]** you can use out of the box. And so Moto has a pretty uh good dictionary um out

**[55:43]** has a pretty uh good dictionary um out

**[55:43]** has a pretty uh good dictionary um out of the box that we're going to be using,

**[55:44]** of the box that we're going to be using,

**[55:44]** of the box that we're going to be using, but I think it's good to get a rough

**[55:46]** but I think it's good to get a rough

**[55:46]** but I think it's good to get a rough sense for how it sort of works. And so

**[55:50]** sense for how it sort of works. And so

**[55:50]** sense for how it sort of works. And so what we'll be doing is just be adding

**[55:51]** what we'll be doing is just be adding

**[55:51]** what we'll be doing is just be adding two simple endpoints uh that we can use

**[55:53]** two simple endpoints uh that we can use

**[55:53]** two simple endpoints uh that we can use to post and set um these requests.

**[55:57]** to post and set um these requests.

**[55:57]** to post and set um these requests. One set. And so we'll be adding them to

**[55:59]** One set. And so we'll be adding them to

**[55:59]** One set. And so we'll be adding them to our actual server.


### [56:00 - 57:00]

**[56:02]** our actual server.

**[56:02]** our actual server. Let me just fix this.

**[56:11]** So we just need to make sure this uh

**[56:11]** So we just need to make sure this uh demo tick is added inside this.

**[56:20]** Yeah. Okay. Cool. So now we have added

**[56:20]** Yeah. Okay. Cool. So now we have added these two new endpoints and so we'll

**[56:22]** these two new endpoints and so we'll

**[56:22]** these two new endpoints and so we'll kind of get a sense for how the modal

**[56:24]** kind of get a sense for how the modal

**[56:24]** kind of get a sense for how the modal dig works before we actually start going

**[56:25]** dig works before we actually start going

**[56:25]** dig works before we actually start going into how to use it with the other chats.

**[56:28]** into how to use it with the other chats.

**[56:28]** into how to use it with the other chats. So

**[56:30]** So

**[56:30]** So over here um let's say when we get a

**[56:32]** over here um let's say when we get a

**[56:32]** over here um let's say when we get a chat previously we talked about how

**[56:33]** chat previously we talked about how

**[56:33]** chat previously we talked about how you're going to get some sort of

**[56:34]** you're going to get some sort of

**[56:34]** you're going to get some sort of response. You get a task ID, you get a

**[56:35]** response. You get a task ID, you get a

**[56:35]** response. You get a task ID, you get a task URL, but we also kind of want to

**[56:37]** task URL, but we also kind of want to

**[56:37]** task URL, but we also kind of want to store things like what is the Slack

**[56:39]** store things like what is the Slack

**[56:39]** store things like what is the Slack channel, what is the Slack thread ts,

**[56:42]** channel, what is the Slack thread ts,

**[56:42]** channel, what is the Slack thread ts, what is the Slack user, what is the

**[56:43]** what is the Slack user, what is the

**[56:43]** what is the Slack user, what is the status of the current job, etc. And so

**[56:45]** status of the current job, etc. And so

**[56:46]** status of the current job, etc. And so by using something simple like a

**[56:47]** by using something simple like a

**[56:47]** by using something simple like a dictionary where we can serialize basic

**[56:49]** dictionary where we can serialize basic

**[56:49]** dictionary where we can serialize basic key value stores, we're able to do this

**[56:51]** key value stores, we're able to do this

**[56:51]** key value stores, we're able to do this quite simply out of the box.

**[56:54]** quite simply out of the box.

**[56:54]** quite simply out of the box. So let's see over here um let's say we

**[56:57]** So let's see over here um let's say we

**[56:57]** So let's see over here um let's say we start a simple manage task, right?


### [57:00 - 58:00]

**[57:02]** start a simple manage task, right?

**[57:02]** start a simple manage task, right? And we get back some of the task data.

**[57:04]** And we get back some of the task data.

**[57:04]** And we get back some of the task data. We get the

**[57:07]** We get the

**[57:07]** We get the over here we look at the stored value.

**[57:09]** over here we look at the stored value.

**[57:09]** over here we look at the stored value. We store the task. We just put a random

**[57:11]** We store the task. We just put a random

**[57:11]** We store the task. We just put a random you know like task ID over here and then

**[57:14]** you know like task ID over here and then

**[57:14]** you know like task ID over here and then we store like task ID, task URL, Slack

**[57:16]** we store like task ID, task URL, Slack

**[57:16]** we store like task ID, task URL, Slack channel etc. But you can also get back

**[57:19]** channel etc. But you can also get back

**[57:19]** channel etc. But you can also get back when you retrieve this. So when you hit

**[57:20]** when you retrieve this. So when you hit

**[57:20]** when you retrieve this. So when you hit the same endpoint, right? This gives you

**[57:22]** the same endpoint, right? This gives you

**[57:22]** the same endpoint, right? This gives you back what you want. And so this is

**[57:23]** back what you want. And so this is

**[57:24]** back what you want. And so this is essentially how the model dictionary

**[57:25]** essentially how the model dictionary

**[57:25]** essentially how the model dictionary works. Simple KV store. And so that is a

**[57:28]** works. Simple KV store. And so that is a

**[57:28]** works. Simple KV store. And so that is a relatively simple way to use it. And so

**[57:30]** relatively simple way to use it. And so

**[57:30]** relatively simple way to use it. And so let's try to use this model dictionary

**[57:32]** let's try to use this model dictionary

**[57:32]** let's try to use this model dictionary so that we can actually push to the same

**[57:33]** so that we can actually push to the same

**[57:33]** so that we can actually push to the same task. Right?

**[57:36]** task. Right?

**[57:36]** task. Right? So let's first delete these two um

**[57:38]** So let's first delete these two um

**[57:38]** So let's first delete these two um endpoints that we have

**[57:47]** and then let's create a new task map

**[57:47]** and then let's create a new task map over here

**[57:50]** over here

**[57:50]** over here that we can basically use

**[57:53]** that we can basically use

**[57:53]** that we can basically use store basically a mapping of a tread ID

**[57:56]** store basically a mapping of a tread ID

**[57:56]** store basically a mapping of a tread ID tread ts to a task.

**[57:59]** tread ts to a task.


### [58:00 - 59:00]

**[58:00]** tread ts to a task. So let's uh we already have a function

**[58:02]** So let's uh we already have a function

**[58:02]** So let's uh we already have a function to create the manners task and so all we

**[58:05]** to create the manners task and so all we

**[58:05]** to create the manners task and so all we need to do is that you know um up here

**[58:09]** need to do is that you know um up here

**[58:09]** need to do is that you know um up here like what we mentioned earlier when you

**[58:11]** like what we mentioned earlier when you

**[58:11]** like what we mentioned earlier when you actually mention a bot in Slack right

**[58:13]** actually mention a bot in Slack right

**[58:13]** actually mention a bot in Slack right you're going to get this weird um thing

**[58:15]** you're going to get this weird um thing

**[58:15]** you're going to get this weird um thing and so what we want to do is we want to

**[58:16]** and so what we want to do is we want to

**[58:16]** and so what we want to do is we want to just basically parse it out

**[58:28]** right so here's a simple function that

**[58:28]** right so here's a simple function that we just parse it out Um, we'll then

**[58:30]** we just parse it out Um, we'll then

**[58:30]** we just parse it out Um, we'll then check in the thread map whether or not

**[58:32]** check in the thread map whether or not

**[58:32]** check in the thread map whether or not this thread ID has been seen before. And

**[58:34]** this thread ID has been seen before. And

**[58:34]** this thread ID has been seen before. And this is because when we get the web hook

**[58:35]** this is because when we get the web hook

**[58:35]** this is because when we get the web hook from Slack, we're going to see the

**[58:36]** from Slack, we're going to see the

**[58:36]** from Slack, we're going to see the thread TS. And if we've seen this thread

**[58:39]** thread TS. And if we've seen this thread

**[58:39]** thread TS. And if we've seen this thread before, we want to basically push it to

**[58:40]** before, we want to basically push it to

**[58:40]** before, we want to basically push it to the same task using the task ID

**[58:42]** the same task using the task ID

**[58:42]** the same task using the task ID parameter, right? And if we've really

**[58:45]** parameter, right? And if we've really

**[58:45]** parameter, right? And if we've really seen it before, we're just going to add

**[58:46]** seen it before, we're just going to add

**[58:46]** seen it before, we're just going to add a simple reaction over here, which is

**[58:48]** a simple reaction over here, which is

**[58:48]** a simple reaction over here, which is just, you know, the goo the eyes that

**[58:49]** just, you know, the goo the eyes that

**[58:49]** just, you know, the goo the eyes that you've seen a lot of Slack bots have.

**[58:51]** you've seen a lot of Slack bots have.

**[58:51]** you've seen a lot of Slack bots have. You know, if we, hey, I'm on it. I've

**[58:52]** You know, if we, hey, I'm on it. I've

**[58:52]** You know, if we, hey, I'm on it. I've notified, you know, this works out of

**[58:54]** notified, you know, this works out of

**[58:54]** notified, you know, this works out of the box. All right, cool. Let us copy

**[58:58]** the box. All right, cool. Let us copy

**[58:58]** the box. All right, cool. Let us copy this,


### [59:00 - 01:00:00]

**[59:08]** right? And then we have this new

**[59:08]** right? And then we have this new function called handle manage task

**[59:12]** function called handle manage task

**[59:12]** function called handle manage task handle select message. And so this will

**[59:15]** handle select message. And so this will

**[59:15]** handle select message. And so this will essentially

**[59:17]** essentially

**[59:17]** essentially replace what we previously had over

**[59:18]** replace what we previously had over

**[59:18]** replace what we previously had over here. Right?

**[59:26]** Cool. Let me see if this works. I right

**[59:26]** Cool. Let me see if this works. I right let's we have a new server let's boot it

**[59:29]** let's we have a new server let's boot it

**[59:29]** let's we have a new server let's boot it up again let's go to slack and let's

**[59:31]** up again let's go to slack and let's

**[59:31]** up again let's go to slack and let's just say

**[59:34]** just say

**[59:34]** just say hey man what's up right and then our

**[59:38]** hey man what's up right and then our

**[59:38]** hey man what's up right and then our server boots up it will respond you can

**[59:40]** server boots up it will respond you can

**[59:40]** server boots up it will respond you can see over here we created a new task with

**[59:42]** see over here we created a new task with

**[59:42]** see over here we created a new task with shred ID and then let's say we go into

**[59:44]** shred ID and then let's say we go into

**[59:44]** shred ID and then let's say we go into this task itself and we say that okay um

**[59:47]** this task itself and we say that okay um

**[59:47]** this task itself and we say that okay um add any

**[59:52]** what's the

**[59:52]** what's the temperature


### [01:00:00 - 01:01:00]

**[01:00:00]** in New York, right? And so we push it to

**[01:00:00]** in New York, right? And so we push it to the same task. So task ID, create manus

**[01:00:03]** the same task. So task ID, create manus

**[01:00:03]** the same task. So task ID, create manus task, got an unexpected one. Okay,

**[01:00:05]** task, got an unexpected one. Okay,

**[01:00:05]** task, got an unexpected one. Okay, sorry, this is on me. Um, so all we need

**[01:00:08]** sorry, this is on me. Um, so all we need

**[01:00:08]** sorry, this is on me. Um, so all we need to do is we just need to update the

**[01:00:09]** to do is we just need to update the

**[01:00:10]** to do is we just need to update the create manus task over here. So it takes

**[01:00:12]** create manus task over here. So it takes

**[01:00:12]** create manus task over here. So it takes a task ID parameter.

**[01:00:35]** Then what we want to do is we just want

**[01:00:35]** Then what we want to do is we just want to take this JSON over here. We're going

**[01:00:37]** to take this JSON over here. We're going

**[01:00:37]** to take this JSON over here. We're going to make sure that if let's say we

**[01:00:38]** to make sure that if let's say we

**[01:00:38]** to make sure that if let's say we provide a task ID, we add it to the JSON

**[01:00:40]** provide a task ID, we add it to the JSON

**[01:00:40]** provide a task ID, we add it to the JSON payload that we sent along.


### [01:01:00 - 01:02:00]

**[01:01:07]** >> cool. Let's uh give it a while for our

**[01:01:07]** >> cool. Let's uh give it a while for our server to restart. Let's boot it up

**[01:01:09]** server to restart. Let's boot it up

**[01:01:09]** server to restart. Let's boot it up again and then let's give this a shot.

**[01:01:12]** again and then let's give this a shot.

**[01:01:12]** again and then let's give this a shot. We could just send the same thing again.

**[01:01:13]** We could just send the same thing again.

**[01:01:14]** We could just send the same thing again. Wouldn't issue. So

**[01:01:20]** this will hopefully you can see that

**[01:01:20]** this will hopefully you can see that right now we have this reaction. That

**[01:01:22]** right now we have this reaction. That

**[01:01:22]** right now we have this reaction. That means that you know we've read from the

**[01:01:23]** means that you know we've read from the

**[01:01:23]** means that you know we've read from the dictionary. We've seen that this is a

**[01:01:25]** dictionary. We've seen that this is a

**[01:01:25]** dictionary. We've seen that this is a thread that we've seen before. And

**[01:01:27]** thread that we've seen before. And

**[01:01:27]** thread that we've seen before. And basically what we do is we push it to

**[01:01:29]** basically what we do is we push it to

**[01:01:29]** basically what we do is we push it to the same task using this this task ID.

**[01:01:31]** the same task using this this task ID.

**[01:01:31]** the same task using this this task ID. Right? So let's take a look at the live

**[01:01:32]** Right? So let's take a look at the live

**[01:01:32]** Right? So let's take a look at the live task that's currently being executed.

**[01:01:35]** task that's currently being executed.

**[01:01:35]** task that's currently being executed. You can see that this is essentially

**[01:01:37]** You can see that this is essentially

**[01:01:37]** You can see that this is essentially we've with our first message. We've then

**[01:01:39]** we've with our first message. We've then

**[01:01:39]** we've with our first message. We've then push it the same follow-up message over

**[01:01:41]** push it the same follow-up message over

**[01:01:41]** push it the same follow-up message over to the same thread. And this allows you

**[01:01:43]** to the same thread. And this allows you

**[01:01:43]** to the same thread. And this allows you to basically be able to work with a lot

**[01:01:44]** to basically be able to work with a lot

**[01:01:44]** to basically be able to work with a lot of these uh simple integrations like out

**[01:01:46]** of these uh simple integrations like out

**[01:01:46]** of these uh simple integrations like out of the box.

**[01:01:56]** And so right now um one of the problems

**[01:01:56]** And so right now um one of the problems is that you know the final answer never

**[01:01:59]** is that you know the final answer never

**[01:01:59]** is that you know the final answer never makes it back to the user in Slack. And


### [01:02:00 - 01:03:00]

**[01:02:01]** makes it back to the user in Slack. And

**[01:02:01]** makes it back to the user in Slack. And so what we need to do is what we did

**[01:02:03]** so what we need to do is what we did

**[01:02:03]** so what we need to do is what we did previously um when we were basically you

**[01:02:05]** previously um when we were basically you

**[01:02:05]** previously um when we were basically you know working with web hooks is that when

**[01:02:07]** know working with web hooks is that when

**[01:02:07]** know working with web hooks is that when we get a web hook address from manus we

**[01:02:09]** we get a web hook address from manus we

**[01:02:09]** we get a web hook address from manus we need to make sure that we push it um

**[01:02:11]** need to make sure that we push it um

**[01:02:11]** need to make sure that we push it um make a essentially we we post it back

**[01:02:13]** make a essentially we we post it back

**[01:02:13]** make a essentially we we post it back right over to the same thread and so

**[01:02:15]** right over to the same thread and so

**[01:02:15]** right over to the same thread and so that we respond correctly and so just

**[01:02:17]** that we respond correctly and so just

**[01:02:17]** that we respond correctly and so just give me a while let me code it up and

**[01:02:18]** give me a while let me code it up and

**[01:02:18]** give me a while let me code it up and then we can walk through the code.


### [01:03:00 - 01:04:00]

**[01:03:15]** Then the last bit we just need to upload

**[01:03:15]** Then the last bit we just need to upload the let's just say upload files.

**[01:03:19]** the let's just say upload files.

**[01:03:19]** the let's just say upload files. That should work. Hopefully

**[01:03:22]** That should work. Hopefully

**[01:03:22]** That should work. Hopefully upload files just need to be uploaded.

**[01:03:23]** upload files just need to be uploaded.

**[01:03:23]** upload files just need to be uploaded. So it also takes an hts

**[01:03:43]** Okay, cool. So, the entire so and then

**[01:03:43]** Okay, cool. So, the entire so and then we just need to add the final endpoint.

**[01:03:45]** we just need to add the final endpoint.

**[01:03:45]** we just need to add the final endpoint. Sorry, please bear me for a bit and then

**[01:03:48]** Sorry, please bear me for a bit and then

**[01:03:48]** Sorry, please bear me for a bit and then we can walk through the code for a

**[01:03:49]** we can walk through the code for a

**[01:03:49]** we can walk through the code for a while.

**[01:03:51]** while.

**[01:03:51]** while. Cool.


### [01:04:00 - 01:05:00]

**[01:04:00]** Cool. So with this now we have a a way

**[01:04:00]** Cool. So with this now we have a a way whereby you know when manus actually

**[01:04:02]** whereby you know when manus actually

**[01:04:02]** whereby you know when manus actually gives a response it's actually able to

**[01:04:03]** gives a response it's actually able to

**[01:04:03]** gives a response it's actually able to respond to you. So let's let's try let's

**[01:04:06]** respond to you. So let's let's try let's

**[01:04:06]** respond to you. So let's let's try let's try it out and then we're going to walk

**[01:04:07]** try it out and then we're going to walk

**[01:04:07]** try it out and then we're going to walk through the code of what we've exactly

**[01:04:08]** through the code of what we've exactly

**[01:04:08]** through the code of what we've exactly implemented like step by step over here.

**[01:04:11]** implemented like step by step over here.

**[01:04:11]** implemented like step by step over here. So as usual um let's

**[01:04:14]** So as usual um let's

**[01:04:14]** So as usual um let's wake up the server a little bit and then

**[01:04:16]** wake up the server a little bit and then

**[01:04:16]** wake up the server a little bit and then we're just going to say at money what's

**[01:04:18]** we're just going to say at money what's

**[01:04:18]** we're just going to say at money what's up

**[01:04:25]** right. Um, same thing as usual. It's

**[01:04:25]** right. Um, same thing as usual. It's going to hit our endpoint and we're

**[01:04:26]** going to hit our endpoint and we're

**[01:04:26]** going to hit our endpoint and we're going to create a new task and we get a

**[01:04:28]** going to create a new task and we get a

**[01:04:28]** going to create a new task and we get a response over here, right? Started

**[01:04:29]** response over here, right? Started

**[01:04:30]** response over here, right? Started working a task. Task ID is this and view

**[01:04:32]** working a task. Task ID is this and view

**[01:04:32]** working a task. Task ID is this and view the live task. It's just going to

**[01:04:35]** the live task. It's just going to

**[01:04:35]** the live task. It's just going to execute um as usual. And then once it's

**[01:04:38]** execute um as usual. And then once it's

**[01:04:38]** execute um as usual. And then once it's had a response, we should get back the

**[01:04:41]** had a response, we should get back the

**[01:04:41]** had a response, we should get back the web hook slack.

**[01:04:44]** web hook slack.

**[01:04:44]** web hook slack. [Music]

**[01:04:46]** [Music]

**[01:04:46]** [Music] Let me just see what's should be getting

**[01:04:49]** Let me just see what's should be getting

**[01:04:49]** Let me just see what's should be getting back this response at web hooksman.


### [01:05:00 - 01:06:00]

**[01:05:19]** I'm just gonna bounce ahead over here. I

**[01:05:19]** I'm just gonna bounce ahead over here. I feel like I'm encountering some

**[01:05:20]** feel like I'm encountering some

**[01:05:20]** feel like I'm encountering some technical difficulties, but I just want

**[01:05:21]** technical difficulties, but I just want

**[01:05:21]** technical difficulties, but I just want to explain a little bit of what I'm

**[01:05:23]** to explain a little bit of what I'm

**[01:05:23]** to explain a little bit of what I'm happening. I'm really sorry. Um,

**[01:05:25]** happening. I'm really sorry. Um,

**[01:05:25]** happening. I'm really sorry. Um, basically what's happening over here is

**[01:05:26]** basically what's happening over here is

**[01:05:26]** basically what's happening over here is that we have a simple um Slack bot,

**[01:05:28]** that we have a simple um Slack bot,

**[01:05:28]** that we have a simple um Slack bot, right? And as as Mannis is sending us a

**[01:05:31]** right? And as as Mannis is sending us a

**[01:05:31]** right? And as as Mannis is sending us a response, it's basically going to be

**[01:05:32]** response, it's basically going to be

**[01:05:32]** response, it's basically going to be able to have um what we essentially are

**[01:05:35]** able to have um what we essentially are

**[01:05:35]** able to have um what we essentially are all of the different um bits of markdown

**[01:05:38]** all of the different um bits of markdown

**[01:05:38]** all of the different um bits of markdown that Mannis is giving and sending back

**[01:05:39]** that Mannis is giving and sending back

**[01:05:39]** that Mannis is giving and sending back to us. Right? So this is really useful

**[01:05:41]** to us. Right? So this is really useful

**[01:05:41]** to us. Right? So this is really useful because a lot of times manage will

**[01:05:43]** because a lot of times manage will

**[01:05:43]** because a lot of times manage will output markdowns such as tables, text,

**[01:05:45]** output markdowns such as tables, text,

**[01:05:45]** output markdowns such as tables, text, images, etc. And you really want to make

**[01:05:47]** images, etc. And you really want to make

**[01:05:47]** images, etc. And you really want to make sure that's rendered nicely. Uh it's a

**[01:05:49]** sure that's rendered nicely. Uh it's a

**[01:05:49]** sure that's rendered nicely. Uh it's a bit complex in Stripe to be able I'm

**[01:05:51]** bit complex in Stripe to be able I'm

**[01:05:51]** bit complex in Stripe to be able I'm sorry, a bit complex in Slack to be able

**[01:05:53]** sorry, a bit complex in Slack to be able

**[01:05:53]** sorry, a bit complex in Slack to be able to do this. And so what you have to do

**[01:05:56]** to do this. And so what you have to do

**[01:05:56]** to do this. And so what you have to do is do a bit of transformation. And so

**[01:05:58]** is do a bit of transformation. And so

**[01:05:58]** is do a bit of transformation. And so what we've essentially done if you look

**[01:05:59]** what we've essentially done if you look

**[01:05:59]** what we've essentially done if you look at the notebook is


### [01:06:00 - 01:07:00]

**[01:06:01]** at the notebook is

**[01:06:02]** at the notebook is first when we actually create a new task

**[01:06:04]** first when we actually create a new task

**[01:06:04]** first when we actually create a new task we save it inside this task info map

**[01:06:06]** we save it inside this task info map

**[01:06:06]** we save it inside this task info map right we then convert it over to a slack

**[01:06:09]** right we then convert it over to a slack

**[01:06:09]** right we then convert it over to a slack markdown format and what this does is

**[01:06:11]** markdown format and what this does is

**[01:06:11]** markdown format and what this does is that it basically just passes some of

**[01:06:13]** that it basically just passes some of

**[01:06:13]** that it basically just passes some of the existing markdown and so that it's

**[01:06:15]** the existing markdown and so that it's

**[01:06:15]** the existing markdown and so that it's compatible with with with Slack. Slack

**[01:06:17]** compatible with with with Slack. Slack

**[01:06:17]** compatible with with with Slack. Slack has some unique markdown formatting

**[01:06:19]** has some unique markdown formatting

**[01:06:19]** has some unique markdown formatting issues and so we just need to make sure

**[01:06:20]** issues and so we just need to make sure

**[01:06:20]** issues and so we just need to make sure it's consistent and then we then take

**[01:06:22]** it's consistent and then we then take

**[01:06:22]** it's consistent and then we then take this markdown and format it into slide

**[01:06:24]** this markdown and format it into slide

**[01:06:24]** this markdown and format it into slide blocks. Uh we then also up previously we

**[01:06:27]** blocks. Uh we then also up previously we

**[01:06:27]** blocks. Uh we then also up previously we had a upload file as a function and what

**[01:06:29]** had a upload file as a function and what

**[01:06:29]** had a upload file as a function and what you notice that we uploaded a file. It

**[01:06:31]** you notice that we uploaded a file. It

**[01:06:31]** you notice that we uploaded a file. It was always uploaded to the main uh

**[01:06:33]** was always uploaded to the main uh

**[01:06:33]** was always uploaded to the main uh channel but not to the tread. And so how

**[01:06:35]** channel but not to the tread. And so how

**[01:06:35]** channel but not to the tread. And so how you can solve this is by passing in

**[01:06:37]** you can solve this is by passing in

**[01:06:37]** you can solve this is by passing in basically both a thread and a channel um

**[01:06:40]** basically both a thread and a channel um

**[01:06:40]** basically both a thread and a channel um parameter. And so what this means is

**[01:06:42]** parameter. And so what this means is

**[01:06:42]** parameter. And so what this means is that when Slack uploads the file it will

**[01:06:43]** that when Slack uploads the file it will

**[01:06:43]** that when Slack uploads the file it will go not only to the channel but the right

**[01:06:45]** go not only to the channel but the right

**[01:06:45]** go not only to the channel but the right thread. So this is really useful in that

**[01:06:47]** thread. So this is really useful in that

**[01:06:47]** thread. So this is really useful in that sense.

**[01:06:49]** sense.

**[01:06:49]** sense. So I think in the next portion we're

**[01:06:51]** So I think in the next portion we're

**[01:06:51]** So I think in the next portion we're just going to try to implement it so

**[01:06:53]** just going to try to implement it so

**[01:06:53]** just going to try to implement it so that you can sort of um basically have

**[01:06:55]** that you can sort of um basically have

**[01:06:55]** that you can sort of um basically have it a process and invoice. I'm just going

**[01:06:57]** it a process and invoice. I'm just going

**[01:06:57]** it a process and invoice. I'm just going to use the final um code that I've

**[01:06:59]** to use the final um code that I've

**[01:06:59]** to use the final um code that I've written ahead of time so that you know


### [01:07:00 - 01:08:00]

**[01:07:01]** written ahead of time so that you know

**[01:07:01]** written ahead of time so that you know in case of any technical difficulties

**[01:07:02]** in case of any technical difficulties

**[01:07:02]** in case of any technical difficulties again. Um but I just wanted to pause

**[01:07:06]** again. Um but I just wanted to pause

**[01:07:06]** again. Um but I just wanted to pause here and see if there's any issue any

**[01:07:08]** here and see if there's any issue any

**[01:07:08]** here and see if there's any issue any questions about how to work with the

**[01:07:09]** questions about how to work with the

**[01:07:09]** questions about how to work with the API.


### [01:08:00 - 01:09:00]

**[01:08:15]** So, let me just test to see if this is

**[01:08:15]** So, let me just test to see if this is working.

**[01:08:17]** working.

**[01:08:17]** working. Just going to maybe

**[01:08:25]** think I had a bunch of uh images that I

**[01:08:25]** think I had a bunch of uh images that I gave previously. So, I'm just gonna take

**[01:08:27]** gave previously. So, I'm just gonna take

**[01:08:27]** gave previously. So, I'm just gonna take a take this uh picture of a bunch of

**[01:08:29]** a take this uh picture of a bunch of

**[01:08:29]** a take this uh picture of a bunch of bagels that I bought previously.

**[01:08:33]** bagels that I bought previously.

**[01:08:33]** bagels that I bought previously. Uh been eating a lot of bagels since

**[01:08:34]** Uh been eating a lot of bagels since

**[01:08:34]** Uh been eating a lot of bagels since I've gotten here. So, those are pretty

**[01:08:36]** I've gotten here. So, those are pretty

**[01:08:36]** I've gotten here. So, those are pretty good, actually, cuz uh like I was really

**[01:08:39]** good, actually, cuz uh like I was really

**[01:08:39]** good, actually, cuz uh like I was really surprised by um how good a lot of the

**[01:08:41]** surprised by um how good a lot of the

**[01:08:41]** surprised by um how good a lot of the bagels were. Um but the other day, I

**[01:08:43]** bagels were. Um but the other day, I

**[01:08:43]** bagels were. Um but the other day, I feel like I got I got scammed a little

**[01:08:44]** feel like I got I got scammed a little

**[01:08:44]** feel like I got I got scammed a little cuz I I ate a bagel that was like 90%

**[01:08:46]** cuz I I ate a bagel that was like 90%

**[01:08:46]** cuz I I ate a bagel that was like 90% cream cheese, like 10% salmon, and I was

**[01:08:49]** cream cheese, like 10% salmon, and I was

**[01:08:50]** cream cheese, like 10% salmon, and I was a bit sad about that. And so, um yeah.

**[01:08:52]** a bit sad about that. And so, um yeah.

**[01:08:52]** a bit sad about that. And so, um yeah. So really like what this does is that if

**[01:08:54]** So really like what this does is that if

**[01:08:54]** So really like what this does is that if you look over here the first thing that

**[01:08:57]** you look over here the first thing that

**[01:08:57]** you look over here the first thing that we get is you get a slack web hook, you


### [01:09:00 - 01:10:00]

**[01:09:01]** we get is you get a slack web hook, you

**[01:09:01]** we get is you get a slack web hook, you create the file, you create the manness

**[01:09:03]** create the file, you create the manness

**[01:09:03]** create the file, you create the manness event and then we're going to post a

**[01:09:05]** event and then we're going to post a

**[01:09:05]** event and then we're going to post a reply and over here you can see hey

**[01:09:06]** reply and over here you can see hey

**[01:09:06]** reply and over here you can see hey we've started working on your request.

**[01:09:08]** we've started working on your request.

**[01:09:08]** we've started working on your request. Um if we go over to the manus app over

**[01:09:10]** Um if we go over to the manus app over

**[01:09:10]** Um if we go over to the manus app over here um you see that we have this thing

**[01:09:12]** here um you see that we have this thing

**[01:09:12]** here um you see that we have this thing called a connector right and this is

**[01:09:14]** called a connector right and this is

**[01:09:14]** called a connector right and this is basically notion that's out of the box.

**[01:09:17]** basically notion that's out of the box.

**[01:09:17]** basically notion that's out of the box. What I've done is that I've created Oh,

**[01:09:18]** What I've done is that I've created Oh,

**[01:09:18]** What I've done is that I've created Oh, sorry. This actually Let me just create

**[01:09:21]** sorry. This actually Let me just create

**[01:09:21]** sorry. This actually Let me just create go to the fake one.

**[01:09:29]** Yep. Anyway, um, so we actually have a a

**[01:09:29]** Yep. Anyway, um, so we actually have a a notion where we have like the these like

**[01:09:31]** notion where we have like the these like

**[01:09:31]** notion where we have like the these like company policies and I've created like a

**[01:09:33]** company policies and I've created like a

**[01:09:33]** company policies and I've created like a fake company policy for you to reference

**[01:09:35]** fake company policy for you to reference

**[01:09:35]** fake company policy for you to reference and so what you see over here is you

**[01:09:36]** and so what you see over here is you

**[01:09:36]** and so what you see over here is you have all this information like the

**[01:09:38]** have all this information like the

**[01:09:38]** have all this information like the company home like what exactly is

**[01:09:40]** company home like what exactly is

**[01:09:40]** company home like what exactly is happening and manage is actually able to

**[01:09:43]** happening and manage is actually able to

**[01:09:43]** happening and manage is actually able to look at the notion look at the

**[01:09:44]** look at the notion look at the

**[01:09:44]** look at the notion look at the connectors and actually give a response

**[01:09:45]** connectors and actually give a response

**[01:09:45]** connectors and actually give a response for how exactly this um is sort of

**[01:09:48]** for how exactly this um is sort of

**[01:09:48]** for how exactly this um is sort of related to my actual like claims policy

**[01:09:50]** related to my actual like claims policy

**[01:09:50]** related to my actual like claims policy and this is really useful if you're

**[01:09:52]** and this is really useful if you're

**[01:09:52]** and this is really useful if you're building anything related to some sort

**[01:09:53]** building anything related to some sort

**[01:09:53]** building anything related to some sort of internal deep research sort of API

**[01:09:56]** of internal deep research sort of API

**[01:09:56]** of internal deep research sort of API because you're constantly going want to

**[01:09:57]** because you're constantly going want to

**[01:09:57]** because you're constantly going want to be able to reference certain things that

**[01:09:59]** be able to reference certain things that

**[01:09:59]** be able to reference certain things that you have. You can see that the file over


### [01:10:00 - 01:11:00]

**[01:10:01]** you have. You can see that the file over

**[01:10:01]** you have. You can see that the file over here was uploaded successfully and then

**[01:10:04]** here was uploaded successfully and then

**[01:10:04]** here was uploaded successfully and then man is able to use OCR to basically

**[01:10:06]** man is able to use OCR to basically

**[01:10:06]** man is able to use OCR to basically extract all the details on the receipt

**[01:10:08]** extract all the details on the receipt

**[01:10:08]** extract all the details on the receipt in some of the previous tests that you

**[01:10:10]** in some of the previous tests that you

**[01:10:10]** in some of the previous tests that you know you can you can see that there were

**[01:10:12]** know you can you can see that there were

**[01:10:12]** know you can you can see that there were a lot of tests. Um, you can basically

**[01:10:15]** a lot of tests. Um, you can basically

**[01:10:15]** a lot of tests. Um, you can basically see that, you know, I just spent like uh

**[01:10:17]** see that, you know, I just spent like uh

**[01:10:17]** see that, you know, I just spent like uh $30 on cats in New York. Is that the

**[01:10:19]** $30 on cats in New York. Is that the

**[01:10:19]** $30 on cats in New York. Is that the cover? And man is basically able to

**[01:10:20]** cover? And man is basically able to

**[01:10:20]** cover? And man is basically able to respond, look at the company policy

**[01:10:22]** respond, look at the company policy

**[01:10:22]** respond, look at the company policy that's in notion, which you know, anyone

**[01:10:24]** that's in notion, which you know, anyone

**[01:10:24]** that's in notion, which you know, anyone in your company can edit, right? Notion

**[01:10:26]** in your company can edit, right? Notion

**[01:10:26]** in your company can edit, right? Notion is a pretty accessible sort of platform

**[01:10:28]** is a pretty accessible sort of platform

**[01:10:28]** is a pretty accessible sort of platform and then they can take that and actually

**[01:10:29]** and then they can take that and actually

**[01:10:29]** and then they can take that and actually edit it out of the box. So, as Manis is

**[01:10:32]** edit it out of the box. So, as Manis is

**[01:10:32]** edit it out of the box. So, as Manis is generating its response, we're waiting

**[01:10:33]** generating its response, we're waiting

**[01:10:34]** generating its response, we're waiting for the final web hook to be sent. And

**[01:10:36]** for the final web hook to be sent. And

**[01:10:36]** for the final web hook to be sent. And so,

**[01:10:38]** so,

**[01:10:38]** so, let's give it a bit of time.

**[01:10:42]** let's give it a bit of time.

**[01:10:42]** let's give it a bit of time. Yeah. And so what you kind of expect to

**[01:10:44]** Yeah. And so what you kind of expect to

**[01:10:44]** Yeah. And so what you kind of expect to see is that if you give, let's say, can

**[01:10:46]** see is that if you give, let's say, can

**[01:10:46]** see is that if you give, let's say, can you help me update this basic invoice?

**[01:10:47]** you help me update this basic invoice?

**[01:10:48]** you help me update this basic invoice? Can you find the shop details, please?

**[01:10:49]** Can you find the shop details, please?

**[01:10:49]** Can you find the shop details, please? Thank you. And then manager is just

**[01:10:51]** Thank you. And then manager is just

**[01:10:51]** Thank you. And then manager is just going to ask, hey, can you give me a bit

**[01:10:52]** going to ask, hey, can you give me a bit

**[01:10:52]** going to ask, hey, can you give me a bit updates?

**[01:10:54]** updates?

**[01:10:54]** updates? This one over here, you can see like if

**[01:10:56]** This one over here, you can see like if

**[01:10:56]** This one over here, you can see like if you look at the invoice, you know, what

**[01:10:58]** you look at the invoice, you know, what

**[01:10:58]** you look at the invoice, you know, what are the summary details? The merchant


### [01:11:00 - 01:12:00]

**[01:11:00]** are the summary details? The merchant

**[01:11:00]** are the summary details? The merchant Tomkin SQL, what's the amount? Can you

**[01:11:02]** Tomkin SQL, what's the amount? Can you

**[01:11:02]** Tomkin SQL, what's the amount? Can you update it using a markdown table

**[01:11:04]** update it using a markdown table

**[01:11:04]** update it using a markdown table instead? And it was basically able to go

**[01:11:05]** instead? And it was basically able to go

**[01:11:06]** instead? And it was basically able to go to the the right page over here.

**[01:11:08]** to the the right page over here.

**[01:11:08]** to the the right page over here. realized that you know the exact receipt

**[01:11:10]** realized that you know the exact receipt

**[01:11:10]** realized that you know the exact receipt that I had was basically from the dates

**[01:11:13]** that I had was basically from the dates

**[01:11:13]** that I had was basically from the dates of like 18 to the 28 and then I was able

**[01:11:15]** of like 18 to the 28 and then I was able

**[01:11:15]** of like 18 to the 28 and then I was able to update the right notion page and

**[01:11:16]** to update the right notion page and

**[01:11:16]** to update the right notion page and basically say that hey these are all of

**[01:11:18]** basically say that hey these are all of

**[01:11:18]** basically say that hey these are all of the different expenses these are

**[01:11:19]** the different expenses these are

**[01:11:19]** the different expenses these are actually my expenses for the last few

**[01:11:21]** actually my expenses for the last few

**[01:11:21]** actually my expenses for the last few days um and you can break it down based

**[01:11:24]** days um and you can break it down based

**[01:11:24]** days um and you can break it down based on this fictitious company policy. So I

**[01:11:29]** on this fictitious company policy. So I

**[01:11:29]** on this fictitious company policy. So I think this was a bit of a more complex

**[01:11:31]** think this was a bit of a more complex

**[01:11:31]** think this was a bit of a more complex uh project and I think at the end there

**[01:11:32]** uh project and I think at the end there

**[01:11:32]** uh project and I think at the end there was some issues with live coding but I I

**[01:11:35]** was some issues with live coding but I I

**[01:11:35]** was some issues with live coding but I I just want to basically bring it back and

**[01:11:37]** just want to basically bring it back and

**[01:11:37]** just want to basically bring it back and try to say that um the manage API is

**[01:11:39]** try to say that um the manage API is

**[01:11:39]** try to say that um the manage API is basically a really easy way for you to

**[01:11:41]** basically a really easy way for you to

**[01:11:41]** basically a really easy way for you to build a lot of these complex um

**[01:11:43]** build a lot of these complex um

**[01:11:43]** build a lot of these complex um applications out of the box right um you

**[01:11:47]** applications out of the box right um you

**[01:11:47]** applications out of the box right um you look at the Rick and Morty dashboard

**[01:11:48]** look at the Rick and Morty dashboard

**[01:11:48]** look at the Rick and Morty dashboard that we had um you can see that this is

**[01:11:51]** that we had um you can see that this is

**[01:11:51]** that we had um you can see that this is pretty pretty cool right like and if you

**[01:11:54]** pretty pretty cool right like and if you

**[01:11:54]** pretty pretty cool right like and if you look at the let's go back to the slides

**[01:11:57]** look at the let's go back to the slides

**[01:11:57]** look at the let's go back to the slides It's

**[01:11:59]** It's

**[01:11:59]** It's my slide somewhere.


### [01:12:00 - 01:13:00]

**[01:12:12]** Yeah. So, a lot of what you can actually

**[01:12:12]** Yeah. So, a lot of what you can actually build out of the box with the manus API

**[01:12:14]** build out of the box with the manus API

**[01:12:14]** build out of the box with the manus API is that these are things that we've

**[01:12:15]** is that these are things that we've

**[01:12:15]** is that these are things that we've learned out of the box scaling the

**[01:12:17]** learned out of the box scaling the

**[01:12:17]** learned out of the box scaling the number of conversations that we deal

**[01:12:18]** number of conversations that we deal

**[01:12:18]** number of conversations that we deal with every day to millions of

**[01:12:20]** with every day to millions of

**[01:12:20]** with every day to millions of conversations. Right? So what this means

**[01:12:22]** conversations. Right? So what this means

**[01:12:22]** conversations. Right? So what this means is that if you use the manage API, you

**[01:12:24]** is that if you use the manage API, you

**[01:12:24]** is that if you use the manage API, you do have the ability to use any sort of

**[01:12:26]** do have the ability to use any sort of

**[01:12:26]** do have the ability to use any sort of integration that we ship with. You can

**[01:12:28]** integration that we ship with. You can

**[01:12:28]** integration that we ship with. You can provide your own sort of keys. You can

**[01:12:30]** provide your own sort of keys. You can

**[01:12:30]** provide your own sort of keys. You can really just you know um add any sort of

**[01:12:33]** really just you know um add any sort of

**[01:12:33]** really just you know um add any sort of custom code that you have, upload these

**[01:12:35]** custom code that you have, upload these

**[01:12:35]** custom code that you have, upload these files, toolkits for manners to use. And

**[01:12:37]** files, toolkits for manners to use. And

**[01:12:37]** files, toolkits for manners to use. And this means that without you having to

**[01:12:38]** this means that without you having to

**[01:12:38]** this means that without you having to deal with all that stuff, you can

**[01:12:40]** deal with all that stuff, you can

**[01:12:40]** deal with all that stuff, you can actually focus on the core business

**[01:12:41]** actually focus on the core business

**[01:12:41]** actually focus on the core business logic that you care about. And so um if

**[01:12:44]** logic that you care about. And so um if

**[01:12:44]** logic that you care about. And so um if you have any API inquiries about the

**[01:12:46]** you have any API inquiries about the

**[01:12:46]** you have any API inquiries about the Manis API, um feel free to reach me at

**[01:12:48]** Manis API, um feel free to reach me at

**[01:12:48]** Manis API, um feel free to reach me at ivanlio manis.ai. And then if you're

**[01:12:50]** ivanlio manis.ai. And then if you're

**[01:12:50]** ivanlio manis.ai. And then if you're interested in joining the manis team, we

**[01:12:52]** interested in joining the manis team, we

**[01:12:52]** interested in joining the manis team, we are hiring uh right now. Um and so feel

**[01:12:55]** are hiring uh right now. Um and so feel

**[01:12:55]** are hiring uh right now. Um and so feel free to reach out to me or just chat

**[01:12:57]** free to reach out to me or just chat

**[01:12:57]** free to reach out to me or just chat with me here. I'm happy to take any

**[01:12:59]** with me here. I'm happy to take any

**[01:12:59]** with me here. I'm happy to take any questions about the API. And um thanks


### [01:13:00 - 01:14:00]

**[01:13:01]** questions about the API. And um thanks

**[01:13:01]** questions about the API. And um thanks so much for taking the time to listen to

**[01:13:03]** so much for taking the time to listen to

**[01:13:03]** so much for taking the time to listen to this. I'm curious how you think about

**[01:13:06]** this. I'm curious how you think about

**[01:13:06]** this. I'm curious how you think about educating people about all the possible

**[01:13:08]** educating people about all the possible

**[01:13:08]** educating people about all the possible use cases for the API and how to stitch

**[01:13:10]** use cases for the API and how to stitch

**[01:13:10]** use cases for the API and how to stitch all these things together to solve their

**[01:13:12]** all these things together to solve their

**[01:13:12]** all these things together to solve their problems because I imagine a lot of this

**[01:13:14]** problems because I imagine a lot of this

**[01:13:14]** problems because I imagine a lot of this is new to people and it doesn't quite

**[01:13:16]** is new to people and it doesn't quite

**[01:13:16]** is new to people and it doesn't quite click immediately that oh I could use

**[01:13:17]** click immediately that oh I could use

**[01:13:17]** click immediately that oh I could use the mass API to solve my problems.

**[01:13:22]** the mass API to solve my problems.

**[01:13:22]** the mass API to solve my problems. >> Yeah, I think the easiest way to get

**[01:13:24]** >> Yeah, I think the easiest way to get

**[01:13:24]** >> Yeah, I think the easiest way to get started before you move to the API is

**[01:13:25]** started before you move to the API is

**[01:13:26]** started before you move to the API is actually to play with our web app

**[01:13:27]** actually to play with our web app

**[01:13:27]** actually to play with our web app because the web app has everything

**[01:13:28]** because the web app has everything

**[01:13:28]** because the web app has everything nicely set up. you know, you don't need

**[01:13:29]** nicely set up. you know, you don't need

**[01:13:29]** nicely set up. you know, you don't need to do web hooks, you don't do

**[01:13:30]** to do web hooks, you don't do

**[01:13:30]** to do web hooks, you don't do integration. And so a lot of times what

**[01:13:32]** integration. And so a lot of times what

**[01:13:32]** integration. And so a lot of times what I'll recommend doing is saying, hey, I

**[01:13:34]** I'll recommend doing is saying, hey, I

**[01:13:34]** I'll recommend doing is saying, hey, I have a problem or something I'm

**[01:13:35]** have a problem or something I'm

**[01:13:35]** have a problem or something I'm repeatedly doing. Um, you look at the

**[01:13:38]** repeatedly doing. Um, you look at the

**[01:13:38]** repeatedly doing. Um, you look at the basically the web app, you try a few

**[01:13:39]** basically the web app, you try a few

**[01:13:40]** basically the web app, you try a few times and manage can get it done pretty

**[01:13:41]** times and manage can get it done pretty

**[01:13:41]** times and manage can get it done pretty well and then you want to start looking

**[01:13:43]** well and then you want to start looking

**[01:13:43]** well and then you want to start looking at the API, testing a bunch of these

**[01:13:45]** at the API, testing a bunch of these

**[01:13:45]** at the API, testing a bunch of these requests, seeing how what you need to

**[01:13:47]** requests, seeing how what you need to

**[01:13:47]** requests, seeing how what you need to provide, what sort of context, and then

**[01:13:48]** provide, what sort of context, and then

**[01:13:48]** provide, what sort of context, and then getting that nailed down consistently.

**[01:13:50]** getting that nailed down consistently.

**[01:13:50]** getting that nailed down consistently. Um, I think the that's how I would

**[01:13:53]** Um, I think the that's how I would

**[01:13:53]** Um, I think the that's how I would approach it. Uh, so use a really simple

**[01:13:54]** approach it. Uh, so use a really simple

**[01:13:54]** approach it. Uh, so use a really simple way, a simple sandbox, and you use that

**[01:13:56]** way, a simple sandbox, and you use that

**[01:13:56]** way, a simple sandbox, and you use that to basically get started. Yeah.

**[01:13:58]** to basically get started. Yeah.

**[01:13:58]** to basically get started. Yeah. Um, is there any other questions that I


### [01:14:00 - 01:15:00]

**[01:14:00]** Um, is there any other questions that I

**[01:14:00]** Um, is there any other questions that I can help with?

**[01:14:06]** >> No, you can go ahead.

**[01:14:06]** >> No, you can go ahead. >> So, so no question on the API, but can

**[01:14:09]** >> So, so no question on the API, but can

**[01:14:09]** >> So, so no question on the API, but can you tell us very quickly how you created

**[01:14:12]** you tell us very quickly how you created

**[01:14:12]** you tell us very quickly how you created that site? What were the steps the the

**[01:14:15]** that site? What were the steps the the

**[01:14:15]** that site? What were the steps the the conference site? You redid that, right?

**[01:14:17]** conference site? You redid that, right?

**[01:14:17]** conference site? You redid that, right? >> I actually So, if you can talk a little

**[01:14:19]** >> I actually So, if you can talk a little

**[01:14:19]** >> I actually So, if you can talk a little bit about that. Uh,

**[01:14:20]** bit about that. Uh,

**[01:14:20]** bit about that. Uh, >> sure. I can show the manage chat

**[01:14:21]** >> sure. I can show the manage chat

**[01:14:21]** >> sure. I can show the manage chat actually. I think that's more fun. Um,

**[01:14:39]** script.

**[01:14:39]** script. Yeah, let's give it a while for this

**[01:14:41]** Yeah, let's give it a while for this

**[01:14:41]** Yeah, let's give it a while for this site to load, I think. Uh, so we can see

**[01:14:44]** site to load, I think. Uh, so we can see

**[01:14:44]** site to load, I think. Uh, so we can see like this is basically the full chat

**[01:14:45]** like this is basically the full chat

**[01:14:45]** like this is basically the full chat that's running. It'll take a while to

**[01:14:47]** that's running. It'll take a while to

**[01:14:47]** that's running. It'll take a while to load because there's quite a lot of

**[01:14:48]** load because there's quite a lot of

**[01:14:48]** load because there's quite a lot of conversations that need to be loaded up.

**[01:14:50]** conversations that need to be loaded up.

**[01:14:50]** conversations that need to be loaded up. But basically what I did is I just said

**[01:14:52]** But basically what I did is I just said

**[01:14:52]** But basically what I did is I just said like hey can you start with this? Can

**[01:14:53]** like hey can you start with this? Can

**[01:14:53]** like hey can you start with this? Can you scrape all the events? There should

**[01:14:54]** you scrape all the events? There should

**[01:14:54]** you scrape all the events? There should be like 70 plus talks. I think the time

**[01:14:57]** be like 70 plus talks. I think the time

**[01:14:57]** be like 70 plus talks. I think the time is on like EST. Can you build a website

**[01:14:58]** is on like EST. Can you build a website

**[01:14:58]** is on like EST. Can you build a website that's like clean brutalist design


### [01:15:00 - 01:16:00]

**[01:15:00]** that's like clean brutalist design

**[01:15:00]** that's like clean brutalist design search bar at the top like add to

**[01:15:02]** search bar at the top like add to

**[01:15:02]** search bar at the top like add to calendar I mean star events and make it

**[01:15:04]** calendar I mean star events and make it

**[01:15:04]** calendar I mean star events and make it work on mobile too. And actually I tried

**[01:15:07]** work on mobile too. And actually I tried

**[01:15:07]** work on mobile too. And actually I tried to use like a bunch

**[01:15:09]** to use like a bunch

**[01:15:09]** to use like a bunch man has a lot of cute like emojis but I

**[01:15:11]** man has a lot of cute like emojis but I

**[01:15:11]** man has a lot of cute like emojis but I tried to use a lot of these different

**[01:15:12]** tried to use a lot of these different

**[01:15:12]** tried to use a lot of these different like services like mix bread for a while

**[01:15:15]** like services like mix bread for a while

**[01:15:15]** like services like mix bread for a while and then I looked at chroma and then it

**[01:15:17]** and then I looked at chroma and then it

**[01:15:17]** and then I looked at chroma and then it just gave you like API key. But really

**[01:15:19]** just gave you like API key. But really

**[01:15:19]** just gave you like API key. But really what you can see over here is that this

**[01:15:20]** what you can see over here is that this

**[01:15:20]** what you can see over here is that this is a iterative process where you're

**[01:15:22]** is a iterative process where you're

**[01:15:22]** is a iterative process where you're using manners as a way to basically

**[01:15:25]** using manners as a way to basically

**[01:15:25]** using manners as a way to basically handle a lot of these complex edge cases

**[01:15:27]** handle a lot of these complex edge cases

**[01:15:27]** handle a lot of these complex edge cases that a simple agent that might work out

**[01:15:29]** that a simple agent that might work out

**[01:15:29]** that a simple agent that might work out of the box for simple websites might not

**[01:15:31]** of the box for simple websites might not

**[01:15:31]** of the box for simple websites might not be able to do, right? And so

**[01:15:35]** be able to do, right? And so

**[01:15:35]** be able to do, right? And so after I gave it like set of events, you

**[01:15:37]** after I gave it like set of events, you

**[01:15:37]** after I gave it like set of events, you can see like manage just wrote a simple

**[01:15:39]** can see like manage just wrote a simple

**[01:15:39]** can see like manage just wrote a simple Python script. It converted all of the

**[01:15:42]** Python script. It converted all of the

**[01:15:42]** Python script. It converted all of the individual PM am stuff whatnot and it

**[01:15:45]** individual PM am stuff whatnot and it

**[01:15:45]** individual PM am stuff whatnot and it just converted all to UTC and then it

**[01:15:47]** just converted all to UTC and then it

**[01:15:47]** just converted all to UTC and then it just scraped everything in the end. And

**[01:15:49]** just scraped everything in the end. And

**[01:15:49]** just scraped everything in the end. And one of the things that was really cool

**[01:15:51]** one of the things that was really cool

**[01:15:51]** one of the things that was really cool that I saw was just that um if you look

**[01:15:54]** that I saw was just that um if you look

**[01:15:54]** that I saw was just that um if you look at the page uh it kind of tried to

**[01:15:56]** at the page uh it kind of tried to

**[01:15:56]** at the page uh it kind of tried to expand


### [01:16:00 - 01:17:00]

**[01:16:03]** scrolling scrolling really far. Yeah. So

**[01:16:03]** scrolling scrolling really far. Yeah. So basically ran a lot of JavaScript. It

**[01:16:04]** basically ran a lot of JavaScript. It

**[01:16:04]** basically ran a lot of JavaScript. It tried to match like what it expanded. It

**[01:16:06]** tried to match like what it expanded. It

**[01:16:06]** tried to match like what it expanded. It read the HTML and then from there it was

**[01:16:08]** read the HTML and then from there it was

**[01:16:08]** read the HTML and then from there it was able to actually get the right set of

**[01:16:10]** able to actually get the right set of

**[01:16:10]** able to actually get the right set of events. And so I think over here you can

**[01:16:13]** events. And so I think over here you can

**[01:16:13]** events. And so I think over here you can see it's very specific use case I had in

**[01:16:15]** see it's very specific use case I had in

**[01:16:15]** see it's very specific use case I had in mind. I want to make sense of events. Um

**[01:16:17]** mind. I want to make sense of events. Um

**[01:16:17]** mind. I want to make sense of events. Um and I think the best way to work with a

**[01:16:19]** and I think the best way to work with a

**[01:16:20]** and I think the best way to work with a lot of these is just to have just try

**[01:16:22]** lot of these is just to have just try

**[01:16:22]** lot of these is just to have just try see what the manage agent can do and

**[01:16:23]** see what the manage agent can do and

**[01:16:23]** see what the manage agent can do and then thereafter like try to put it

**[01:16:25]** then thereafter like try to put it

**[01:16:25]** then thereafter like try to put it together. Yeah.

**[01:16:32]** >> Go ahead. You can ask.

**[01:16:32]** >> Go ahead. You can ask. Uh so thanks Ivan amazing demo and

**[01:16:35]** Uh so thanks Ivan amazing demo and

**[01:16:35]** Uh so thanks Ivan amazing demo and thanks for such a tidy and clean

**[01:16:36]** thanks for such a tidy and clean

**[01:16:36]** thanks for such a tidy and clean notebook. Uh I'm going to go back and

**[01:16:39]** notebook. Uh I'm going to go back and

**[01:16:39]** notebook. Uh I'm going to go back and try it straight away in my own company

**[01:16:40]** try it straight away in my own company

**[01:16:40]** try it straight away in my own company because like I've been meaning to do

**[01:16:41]** because like I've been meaning to do

**[01:16:41]** because like I've been meaning to do support agents and this is an amazing

**[01:16:43]** support agents and this is an amazing

**[01:16:43]** support agents and this is an amazing demo. I just wanted to ask uh where does

**[01:16:46]** demo. I just wanted to ask uh where does

**[01:16:46]** demo. I just wanted to ask uh where does all this information because all so

**[01:16:48]** all this information because all so

**[01:16:48]** all this information because all so sensitive where does it live and can we

**[01:16:50]** sensitive where does it live and can we

**[01:16:50]** sensitive where does it live and can we like get it deleted later or anything

**[01:16:52]** like get it deleted later or anything

**[01:16:52]** like get it deleted later or anything like that?

**[01:16:53]** like that?

**[01:16:53]** like that? >> Sorry. What do you mean by what is this?

**[01:16:54]** >> Sorry. What do you mean by what is this?

**[01:16:54]** >> Sorry. What do you mean by what is this? >> Oh like right now who's reading my

**[01:16:56]** >> Oh like right now who's reading my

**[01:16:56]** >> Oh like right now who's reading my transcripts? Oh,

**[01:16:58]** transcripts? Oh,

**[01:16:58]** transcripts? Oh, >> I think like when it comes to if you say


### [01:17:00 - 01:18:00]

**[01:17:00]** >> I think like when it comes to if you say

**[01:17:00]** >> I think like when it comes to if you say like who's reading a transcript, you

**[01:17:01]** like who's reading a transcript, you

**[01:17:01]** like who's reading a transcript, you mean like all these chats?

**[01:17:02]** mean like all these chats?

**[01:17:02]** mean like all these chats? >> Yeah.

**[01:17:03]** >> Yeah.

**[01:17:03]** >> Yeah. >> So like user privacy is really important

**[01:17:05]** >> So like user privacy is really important

**[01:17:05]** >> So like user privacy is really important for us and so for us like we can't read

**[01:17:07]** for us and so for us like we can't read

**[01:17:07]** for us and so for us like we can't read any of the chats. Yeah. The only chats

**[01:17:09]** any of the chats. Yeah. The only chats

**[01:17:09]** any of the chats. Yeah. The only chats we read are when you share about hey man

**[01:17:11]** we read are when you share about hey man

**[01:17:11]** we read are when you share about hey man this isn't working and then we go in and

**[01:17:12]** this isn't working and then we go in and

**[01:17:12]** this isn't working and then we go in and check it out. Um I think all of your

**[01:17:14]** check it out. Um I think all of your

**[01:17:14]** check it out. Um I think all of your data is housed in the US and so there's

**[01:17:16]** data is housed in the US and so there's

**[01:17:16]** data is housed in the US and so there's no sort of like worry about that. Yeah.

**[01:17:26]** >> Start with that. Sure.

**[01:17:26]** >> Start with that. Sure. All right. So, I know you built this

**[01:17:29]** All right. So, I know you built this

**[01:17:29]** All right. So, I know you built this really cool page. What would be really

**[01:17:31]** really cool page. What would be really

**[01:17:31]** really cool page. What would be really cool like if you could have those events

**[01:17:33]** cool like if you could have those events

**[01:17:33]** cool like if you could have those events like put it in directly into your

**[01:17:34]** like put it in directly into your

**[01:17:34]** like put it in directly into your calendar? So, and also my another

**[01:17:37]** calendar? So, and also my another

**[01:17:37]** calendar? So, and also my another question was like like what's the most

**[01:17:40]** question was like like what's the most

**[01:17:40]** question was like like what's the most interesting use case you have seen the

**[01:17:42]** interesting use case you have seen the

**[01:17:42]** interesting use case you have seen the manus people using the manus API or just

**[01:17:45]** manus people using the manus API or just

**[01:17:45]** manus people using the manus API or just the platform

**[01:17:48]** the platform

**[01:17:48]** the platform >> API is pretty new. So, I think we're

**[01:17:49]** >> API is pretty new. So, I think we're

**[01:17:49]** >> API is pretty new. So, I think we're sort of like exploring and seeing what

**[01:17:51]** sort of like exploring and seeing what

**[01:17:51]** sort of like exploring and seeing what people are using it for. a lot of people

**[01:17:52]** people are using it for. a lot of people

**[01:17:52]** people are using it for. a lot of people are using it for research trying to like

**[01:17:54]** are using it for research trying to like

**[01:17:54]** are using it for research trying to like really access a lot of like to make

**[01:17:56]** really access a lot of like to make

**[01:17:56]** really access a lot of like to make sense of a lot of data and I think like

**[01:17:58]** sense of a lot of data and I think like

**[01:17:58]** sense of a lot of data and I think like that is basically like leaning a lot of


### [01:18:00 - 01:19:00]

**[01:18:00]** that is basically like leaning a lot of

**[01:18:00]** that is basically like leaning a lot of the advantages that manis has um in

**[01:18:03]** the advantages that manis has um in

**[01:18:03]** the advantages that manis has um in terms of the sort of advantages that

**[01:18:04]** terms of the sort of advantages that

**[01:18:04]** terms of the sort of advantages that manis I think like the cool things um I

**[01:18:07]** manis I think like the cool things um I

**[01:18:07]** manis I think like the cool things um I really like pickle ball I don't know if

**[01:18:08]** really like pickle ball I don't know if

**[01:18:08]** really like pickle ball I don't know if anyone here plays it but it's like

**[01:18:10]** anyone here plays it but it's like

**[01:18:10]** anyone here plays it but it's like pretty popular but it's really

**[01:18:12]** pretty popular but it's really

**[01:18:12]** pretty popular but it's really competitive in Singapore to basically

**[01:18:13]** competitive in Singapore to basically

**[01:18:13]** competitive in Singapore to basically get like pickle ball slots and you can

**[01:18:15]** get like pickle ball slots and you can

**[01:18:15]** get like pickle ball slots and you can only book them through the government

**[01:18:17]** only book them through the government

**[01:18:17]** only book them through the government it's a Singapore thing and so what I got

**[01:18:19]** it's a Singapore thing and so what I got

**[01:18:19]** it's a Singapore thing and so what I got managed to do is I wrote like a Python

**[01:18:21]** managed to do is I wrote like a Python

**[01:18:21]** managed to do is I wrote like a Python script that spun up like six selenium

**[01:18:23]** script that spun up like six selenium

**[01:18:23]** script that spun up like six selenium instances and it scraped like the entire

**[01:18:24]** instances and it scraped like the entire

**[01:18:24]** instances and it scraped like the entire government website and then they said

**[01:18:26]** government website and then they said

**[01:18:26]** government website and then they said like in two weeks you could play pickle

**[01:18:28]** like in two weeks you could play pickle

**[01:18:28]** like in two weeks you could play pickle ball at this location and and I thought

**[01:18:30]** ball at this location and and I thought

**[01:18:30]** ball at this location and and I thought that was pretty cool because I think

**[01:18:31]** that was pretty cool because I think

**[01:18:31]** that was pretty cool because I think that's one of the benefits you get by

**[01:18:33]** that's one of the benefits you get by

**[01:18:33]** that's one of the benefits you get by using an general agent with it own

**[01:18:35]** using an general agent with it own

**[01:18:35]** using an general agent with it own sandbox with it own ability to basically

**[01:18:36]** sandbox with it own ability to basically

**[01:18:36]** sandbox with it own ability to basically spin up these like code to run it to

**[01:18:38]** spin up these like code to run it to

**[01:18:38]** spin up these like code to run it to test it um and if you use the API that's

**[01:18:41]** test it um and if you use the API that's

**[01:18:41]** test it um and if you use the API that's what you get out of the box yeah

**[01:18:43]** what you get out of the box yeah

**[01:18:43]** what you get out of the box yeah >> is it possible to use the my browser

**[01:18:45]** >> is it possible to use the my browser

**[01:18:45]** >> is it possible to use the my browser through the API and if so how would it

**[01:18:48]** through the API and if so how would it

**[01:18:48]** through the API and if so how would it determine which browser to

**[01:18:53]** Yeah, I think um when it comes to my

**[01:18:53]** Yeah, I think um when it comes to my browser, I think um that will be uh

**[01:18:55]** browser, I think um that will be uh

**[01:18:56]** browser, I think um that will be uh something that we'll look into. So

**[01:18:57]** something that we'll look into. So

**[01:18:58]** something that we'll look into. So because my browser requires you not only

**[01:18:59]** because my browser requires you not only

**[01:18:59]** because my browser requires you not only choose the browser but also approve it


### [01:19:00 - 01:20:00]

**[01:19:00]** choose the browser but also approve it

**[01:19:00]** choose the browser but also approve it because you don't want to randomly spin

**[01:19:01]** because you don't want to randomly spin

**[01:19:01]** because you don't want to randomly spin up tabs on your browser. Um so we'll be

**[01:19:04]** up tabs on your browser. Um so we'll be

**[01:19:04]** up tabs on your browser. Um so we'll be working on basically improving the

**[01:19:05]** working on basically improving the

**[01:19:05]** working on basically improving the permission system. So you can do things

**[01:19:07]** permission system. So you can do things

**[01:19:07]** permission system. So you can do things like the um like why research um the

**[01:19:10]** like the um like why research um the

**[01:19:10]** like the um like why research um the browser and all these other bits of

**[01:19:12]** browser and all these other bits of

**[01:19:12]** browser and all these other bits of things that you need to authorize. um

**[01:19:13]** things that you need to authorize. um

**[01:19:13]** things that you need to authorize. um because user permissions is something

**[01:19:15]** because user permissions is something

**[01:19:15]** because user permissions is something that we want to try to think carefully

**[01:19:16]** that we want to try to think carefully

**[01:19:16]** that we want to try to think carefully about and so we want to make sure we

**[01:19:17]** about and so we want to make sure we

**[01:19:18]** about and so we want to make sure we have it done well before we ship it out

**[01:19:19]** have it done well before we ship it out

**[01:19:19]** have it done well before we ship it out but that's in the road map soon. Uh we

**[01:19:21]** but that's in the road map soon. Uh we

**[01:19:21]** but that's in the road map soon. Uh we also have um in a maybe two weeks um

**[01:19:24]** also have um in a maybe two weeks um

**[01:19:24]** also have um in a maybe two weeks um you'll be able to let's say manis

**[01:19:26]** you'll be able to let's say manis

**[01:19:26]** you'll be able to let's say manis generates like a markdown or manage

**[01:19:28]** generates like a markdown or manage

**[01:19:28]** generates like a markdown or manage generates like slides for you they will

**[01:19:30]** generates like slides for you they will

**[01:19:30]** generates like slides for you they will all be able to be converted to the same

**[01:19:31]** all be able to be converted to the same

**[01:19:31]** all be able to be converted to the same form as you see on the UI. So what this

**[01:19:33]** form as you see on the UI. So what this

**[01:19:33]** form as you see on the UI. So what this means is that let's say you give mana

**[01:19:35]** means is that let's say you give mana

**[01:19:35]** means is that let's say you give mana say hey I'm really interested I would

**[01:19:37]** say hey I'm really interested I would

**[01:19:37]** say hey I'm really interested I would like to pitch my company I would like to

**[01:19:39]** like to pitch my company I would like to

**[01:19:39]** like to pitch my company I would like to pitch something to someone right who

**[01:19:41]** pitch something to someone right who

**[01:19:41]** pitch something to someone right who does all the research puts slides

**[01:19:43]** does all the research puts slides

**[01:19:43]** does all the research puts slides together and using the same API you can

**[01:19:45]** together and using the same API you can

**[01:19:45]** together and using the same API you can download a full PvPX file you can export

**[01:19:47]** download a full PvPX file you can export

**[01:19:47]** download a full PvPX file you can export it however you want as a PDF I think

**[01:19:50]** it however you want as a PDF I think

**[01:19:50]** it however you want as a PDF I think that's really useful or even like

**[01:19:51]** that's really useful or even like

**[01:19:51]** that's really useful or even like markdown to PDF and so we have a lot of

**[01:19:53]** markdown to PDF and so we have a lot of

**[01:19:53]** markdown to PDF and so we have a lot of these same uh requ um features in mind

**[01:19:56]** these same uh requ um features in mind

**[01:19:56]** these same uh requ um features in mind to ensure feature parity um so that you

**[01:19:59]** to ensure feature parity um so that you

**[01:19:59]** to ensure feature parity um so that you get essentially the same experience on


### [01:20:00 - 01:21:00]

**[01:20:00]** get essentially the same experience on

**[01:20:00]** get essentially the same experience on the API and the UI. Yeah,

**[01:20:03]** the API and the UI. Yeah,

**[01:20:03]** the API and the UI. Yeah, >> that was really informative. Thanks very

**[01:20:05]** >> that was really informative. Thanks very

**[01:20:05]** >> that was really informative. Thanks very much. So my question is about like uh so

**[01:20:07]** much. So my question is about like uh so

**[01:20:08]** much. So my question is about like uh so if I'm doing some research on some

**[01:20:09]** if I'm doing some research on some

**[01:20:09]** if I'm doing some research on some topics, I don't want always to like give

**[01:20:12]** topics, I don't want always to like give

**[01:20:12]** topics, I don't want always to like give it like the background, the context um

**[01:20:14]** it like the background, the context um

**[01:20:14]** it like the background, the context um in every conversation since it's linked

**[01:20:16]** in every conversation since it's linked

**[01:20:16]** in every conversation since it's linked to like uh you know my accounts API

**[01:20:19]** to like uh you know my accounts API

**[01:20:19]** to like uh you know my accounts API keys. Um my question was um if it's

**[01:20:23]** keys. Um my question was um if it's

**[01:20:23]** keys. Um my question was um if it's possible to like remember it's you know

**[01:20:25]** possible to like remember it's you know

**[01:20:25]** possible to like remember it's you know me have like a memory or like for me to

**[01:20:28]** me have like a memory or like for me to

**[01:20:28]** me have like a memory or like for me to decide like in every conversation do I

**[01:20:30]** decide like in every conversation do I

**[01:20:30]** decide like in every conversation do I want to you know remember um you know

**[01:20:33]** want to you know remember um you know

**[01:20:33]** want to you know remember um you know just draw memory from like my other

**[01:20:35]** just draw memory from like my other

**[01:20:35]** just draw memory from like my other conversations or um you know like a

**[01:20:38]** conversations or um you know like a

**[01:20:38]** conversations or um you know like a temporary mode stuff like that.

**[01:20:40]** temporary mode stuff like that.

**[01:20:40]** temporary mode stuff like that. >> Yeah, I think a memory is something

**[01:20:42]** >> Yeah, I think a memory is something

**[01:20:42]** >> Yeah, I think a memory is something that's really interesting. Uh it's

**[01:20:43]** that's really interesting. Uh it's

**[01:20:43]** that's really interesting. Uh it's something that we're actively looking

**[01:20:44]** something that we're actively looking

**[01:20:44]** something that we're actively looking at. Um and so I think for now it's not

**[01:20:47]** at. Um and so I think for now it's not

**[01:20:47]** at. Um and so I think for now it's not possible but maybe in the near future.

**[01:20:48]** possible but maybe in the near future.

**[01:20:48]** possible but maybe in the near future. So, for now, you have to be a bit more

**[01:20:50]** So, for now, you have to be a bit more

**[01:20:50]** So, for now, you have to be a bit more explicit when working with Mattis,

**[01:20:51]** explicit when working with Mattis,

**[01:20:51]** explicit when working with Mattis, unfortunately. Yeah. Um, are there any

**[01:20:54]** unfortunately. Yeah. Um, are there any

**[01:20:54]** unfortunately. Yeah. Um, are there any other questions I can help with?

**[01:20:57]** other questions I can help with?

**[01:20:58]** other questions I can help with? Uh, cool. If not, then uh I'll just be


### [01:21:00 - 01:22:00]

**[01:21:00]** Uh, cool. If not, then uh I'll just be

**[01:21:00]** Uh, cool. If not, then uh I'll just be over here at the front. Uh, we also have

**[01:21:01]** over here at the front. Uh, we also have

**[01:21:01]** over here at the front. Uh, we also have another colleague from Manis Y over

**[01:21:03]** another colleague from Manis Y over

**[01:21:03]** another colleague from Manis Y over there. If you need like any help with

**[01:21:05]** there. If you need like any help with

**[01:21:05]** there. If you need like any help with API with the API or just asking

**[01:21:06]** API with the API or just asking

**[01:21:06]** API with the API or just asking questions on manis in general. Uh, thank

**[01:21:08]** questions on manis in general. Uh, thank

**[01:21:08]** questions on manis in general. Uh, thank you so much for taking the time to

**[01:21:09]** you so much for taking the time to

**[01:21:09]** you so much for taking the time to listen to me today and sorry about the

**[01:21:11]** listen to me today and sorry about the

**[01:21:11]** listen to me today and sorry about the technical difficulties.

**[01:21:28]** [Music]

**[01:21:28]** [Music] Heat.


