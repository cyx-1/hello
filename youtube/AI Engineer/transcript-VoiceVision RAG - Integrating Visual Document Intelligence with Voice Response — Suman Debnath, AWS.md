# VoiceVision RAG - Integrating Visual Document Intelligence with Voice Response — Suman Debnath, AWS

**Video URL:** https://www.youtube.com/watch?v=hwCmfThIiS4

---

## Full Transcript

### [00:00 - 01:00]

**[00:20]** All right. So, you're almost on time.

**[00:20]** All right. So, you're almost on time. Uh firstly, thank you so much for your

**[00:22]** Uh firstly, thank you so much for your

**[00:22]** Uh firstly, thank you so much for your time uh for joining us. And uh what

**[00:26]** time uh for joining us. And uh what

**[00:26]** time uh for joining us. And uh what we're going to do is for next an hour or

**[00:29]** we're going to do is for next an hour or

**[00:29]** we're going to do is for next an hour or so is uh we'll try to explore something

**[00:32]** so is uh we'll try to explore something

**[00:32]** so is uh we'll try to explore something around which is which I found uh pretty

**[00:34]** around which is which I found uh pretty

**[00:34]** around which is which I found uh pretty interesting when I started working on

**[00:36]** interesting when I started working on

**[00:36]** interesting when I started working on this uh uh and I'll tell you some

**[00:38]** this uh uh and I'll tell you some

**[00:38]** this uh uh and I'll tell you some background about that how I end up into

**[00:41]** background about that how I end up into

**[00:41]** background about that how I end up into this uh on vision based retrieval. uh

**[00:44]** this uh on vision based retrieval. uh

**[00:44]** this uh on vision based retrieval. uh but the idea of uh that I had was just

**[00:48]** but the idea of uh that I had was just

**[00:48]** but the idea of uh that I had was just to share a few of my learning on this

**[00:50]** to share a few of my learning on this

**[00:50]** to share a few of my learning on this particular approach of retrieval

**[00:53]** particular approach of retrieval

**[00:53]** particular approach of retrieval and there are bunch of things that we

**[00:55]** and there are bunch of things that we

**[00:55]** and there are bunch of things that we have here. Uh I'm going to share one of

**[00:59]** have here. Uh I'm going to share one of

**[00:59]** have here. Uh I'm going to share one of the latest research paper around


### [01:00 - 02:00]

**[01:00]** the latest research paper around

**[01:00]** the latest research paper around retrieval which is a uh vision based

**[01:03]** retrieval which is a uh vision based

**[01:03]** retrieval which is a uh vision based retrieval and also

**[01:05]** retrieval and also

**[01:05]** retrieval and also uh I just thought to wrap this around

**[01:08]** uh I just thought to wrap this around

**[01:08]** uh I just thought to wrap this around with an agent. Uh without agent we

**[01:11]** with an agent. Uh without agent we

**[01:11]** with an agent. Uh without agent we cannot talk about anything these days.

**[01:12]** cannot talk about anything these days.

**[01:12]** cannot talk about anything these days. So uh right so uh it's funny uh without

**[01:16]** So uh right so uh it's funny uh without

**[01:16]** So uh right so uh it's funny uh without agent I had this but then uh the

**[01:18]** agent I had this but then uh the

**[01:18]** agent I had this but then uh the organizer said that you know we need to

**[01:20]** organizer said that you know we need to

**[01:20]** organizer said that you know we need to have some agent okay it's not a big deal

**[01:23]** have some agent okay it's not a big deal

**[01:23]** have some agent okay it's not a big deal right so yeah so

**[01:27]** right so yeah so

**[01:27]** right so yeah so all right so u we'll focus

**[01:30]** all right so u we'll focus

**[01:30]** all right so u we'll focus mostly on the uh

**[01:35]** mostly on the uh

**[01:35]** mostly on the uh science side of this like how that uh

**[01:39]** science side of this like how that uh

**[01:39]** science side of this like how that uh vision based retrieval works and then we

**[01:41]** vision based retrieval works and then we

**[01:41]** vision based retrieval works and then we will switch gears and rapid around with

**[01:43]** will switch gears and rapid around with

**[01:43]** will switch gears and rapid around with an agent. I mean that's a very simple

**[01:44]** an agent. I mean that's a very simple

**[01:44]** an agent. I mean that's a very simple task and uh I'm going to use one of the

**[01:46]** task and uh I'm going to use one of the

**[01:46]** task and uh I'm going to use one of the open source uh uh framework that uh uh

**[01:50]** open source uh uh framework that uh uh

**[01:50]** open source uh uh framework that uh uh we launched recently. I think it was two

**[01:51]** we launched recently. I think it was two

**[01:52]** we launched recently. I think it was two weeks back called strands agent uh which

**[01:55]** weeks back called strands agent uh which

**[01:55]** weeks back called strands agent uh which is kind of a a framework lightweight

**[01:58]** is kind of a a framework lightweight

**[01:58]** is kind of a a framework lightweight framework to build agentic application.


### [02:00 - 03:00]

**[02:00]** framework to build agentic application.

**[02:00]** framework to build agentic application. I'll talk about that little later and I

**[02:02]** I'll talk about that little later and I

**[02:02]** I'll talk about that little later and I have a session on that day for tomorrow.

**[02:05]** have a session on that day for tomorrow.

**[02:05]** have a session on that day for tomorrow. Um but that's the premise and uh before

**[02:09]** Um but that's the premise and uh before

**[02:09]** Um but that's the premise and uh before we get started uh how many of you are

**[02:13]** we get started uh how many of you are

**[02:13]** we get started uh how many of you are are from uh

**[02:16]** are from uh

**[02:16]** are from uh science side of things like who how many

**[02:18]** science side of things like who how many

**[02:18]** science side of things like who how many of you have worked on transformers?

**[02:21]** of you have worked on transformers?

**[02:21]** of you have worked on transformers? Okay, perfect. How many of you have

**[02:23]** Okay, perfect. How many of you have

**[02:23]** Okay, perfect. How many of you have worked on rag in general?

**[02:26]** worked on rag in general?

**[02:26]** worked on rag in general? Fantastic. Okay. And uh how many of you

**[02:30]** Fantastic. Okay. And uh how many of you

**[02:30]** Fantastic. Okay. And uh how many of you have worked on AWS?

**[02:33]** have worked on AWS?

**[02:33]** have worked on AWS? Okay, great. So there's nothing about

**[02:35]** Okay, great. So there's nothing about

**[02:35]** Okay, great. So there's nothing about AWS here. Okay. So uh so the last

**[02:38]** AWS here. Okay. So uh so the last

**[02:38]** AWS here. Okay. So uh so the last question was sponsored by my manager.

**[02:40]** question was sponsored by my manager.

**[02:40]** question was sponsored by my manager. Okay. So what so what we are going to do

**[02:45]** Okay. So what so what we are going to do

**[02:45]** Okay. So what so what we are going to do is u uh we are going to uh share one uh

**[02:51]** is u uh we are going to uh share one uh

**[02:51]** is u uh we are going to uh share one uh notebook. you can just uh clone that

**[02:55]** notebook. you can just uh clone that

**[02:55]** notebook. you can just uh clone that repository and uh there is lot more uh

**[02:59]** repository and uh there is lot more uh

**[02:59]** repository and uh there is lot more uh there inside that uh but we are just


### [03:00 - 04:00]

**[03:02]** there inside that uh but we are just

**[03:02]** there inside that uh but we are just going to use one part of that uh

**[03:03]** going to use one part of that uh

**[03:03]** going to use one part of that uh repository okay and I'm going to share

**[03:06]** repository okay and I'm going to share

**[03:06]** repository okay and I'm going to share few of the I think some $25 credit code

**[03:11]** few of the I think some $25 credit code

**[03:11]** few of the I think some $25 credit code uh which I was given so I think uh you

**[03:13]** uh which I was given so I think uh you

**[03:13]** uh which I was given so I think uh you may like to use that so uh let's get

**[03:16]** may like to use that so uh let's get

**[03:16]** may like to use that so uh let's get this logistics uh sorted uh first

**[03:21]** this logistics uh sorted uh first

**[03:21]** this logistics uh sorted uh first okay so first thing first Uh

**[03:24]** okay so first thing first Uh

**[03:24]** okay so first thing first Uh can we just switch the screen please?

**[03:35]** Yeah. Uh can you just uh uh take a

**[03:35]** Yeah. Uh can you just uh uh take a moment and see that if the URL is

**[03:37]** moment and see that if the URL is

**[03:37]** moment and see that if the URL is working?

**[03:39]** working?

**[03:39]** working? Uh you may if you are on laptop you may

**[03:43]** Uh you may if you are on laptop you may

**[03:43]** Uh you may if you are on laptop you may like to uh

**[03:45]** like to uh

**[03:46]** like to uh open the URL or you can just take an

**[03:48]** open the URL or you can just take an

**[03:48]** open the URL or you can just take an image uh on your cell. You can have a

**[03:51]** image uh on your cell. You can have a

**[03:51]** image uh on your cell. You can have a look later on.

**[03:53]** look later on.

**[03:54]** look later on. Is it working?

**[03:55]** Is it working?

**[03:55]** Is it working? >> Okay, perfect. Okay. So

**[03:59]** >> Okay, perfect. Okay. So

**[03:59]** >> Okay, perfect. Okay. So now this is something


### [04:00 - 05:00]

**[04:02]** now this is something

**[04:02]** now this is something uh you can take an image now or you can

**[04:07]** uh you can take an image now or you can

**[04:07]** uh you can take an image now or you can uh do that survey later on. I mean I

**[04:10]** uh do that survey later on. I mean I

**[04:10]** uh do that survey later on. I mean I don't like this but again this was given

**[04:12]** don't like this but again this was given

**[04:12]** don't like this but again this was given by my manager. So so this is just it

**[04:16]** by my manager. So so this is just it

**[04:16]** by my manager. So so this is just it might ask you few questions. I have no

**[04:17]** might ask you few questions. I have no

**[04:17]** might ask you few questions. I have no idea what question they will ask, but uh

**[04:19]** idea what question they will ask, but uh

**[04:19]** idea what question they will ask, but uh you will get some $25 credit and uh if

**[04:24]** you will get some $25 credit and uh if

**[04:24]** you will get some $25 credit and uh if you don't want to do it, don't do it.

**[04:25]** you don't want to do it, don't do it.

**[04:25]** you don't want to do it, don't do it. I'll give you $25 credit. So, I have it.

**[04:28]** I'll give you $25 credit. So, I have it.

**[04:28]** I'll give you $25 credit. So, I have it. So,

**[04:30]** So,

**[04:30]** So, okay. So,

**[04:33]** okay. So,

**[04:33]** okay. So, yeah. And uh I don't know why this slide

**[04:36]** yeah. And uh I don't know why this slide

**[04:36]** yeah. And uh I don't know why this slide is next, but so this is my Oh, I I

**[04:39]** is next, but so this is my Oh, I I

**[04:40]** is next, but so this is my Oh, I I actually forgot to introduce myself. So

**[04:42]** actually forgot to introduce myself. So

**[04:42]** actually forgot to introduce myself. So I work with AWS uh as a principal uh

**[04:45]** I work with AWS uh as a principal uh

**[04:45]** I work with AWS uh as a principal uh machine learning advocate. I'm with this

**[04:47]** machine learning advocate. I'm with this

**[04:47]** machine learning advocate. I'm with this company for last 6 months. I focus

**[04:50]** company for last 6 months. I focus

**[04:50]** company for last 6 months. I focus mostly on um natural language and uh rag

**[04:54]** mostly on um natural language and uh rag

**[04:54]** mostly on um natural language and uh rag and fine-tuning.

**[04:56]** and fine-tuning.

**[04:56]** and fine-tuning. And if you have any questions around the

**[04:58]** And if you have any questions around the

**[04:58]** And if you have any questions around the talk that we are going to discuss uh or


### [05:00 - 06:00]

**[05:00]** talk that we are going to discuss uh or

**[05:00]** talk that we are going to discuss uh or anything around uh machine learning or

**[05:02]** anything around uh machine learning or

**[05:02]** anything around uh machine learning or generative AI feel free to uh ping me.

**[05:05]** generative AI feel free to uh ping me.

**[05:05]** generative AI feel free to uh ping me. It's not just about this session but uh

**[05:07]** It's not just about this session but uh

**[05:08]** It's not just about this session but uh my takeaway at whenever I go and speak

**[05:10]** my takeaway at whenever I go and speak

**[05:10]** my takeaway at whenever I go and speak at any conference at this scale is uh

**[05:13]** at any conference at this scale is uh

**[05:13]** at any conference at this scale is uh just to make few connections with whom I

**[05:17]** just to make few connections with whom I

**[05:17]** just to make few connections with whom I can work with uh you know after this

**[05:19]** can work with uh you know after this

**[05:20]** can work with uh you know after this conference

**[05:21]** conference

**[05:21]** conference uh because as long as learning is

**[05:24]** uh because as long as learning is

**[05:24]** uh because as long as learning is concerned we can learn everything at

**[05:26]** concerned we can learn everything at

**[05:26]** concerned we can learn everything at home right and so you don't have to come

**[05:28]** home right and so you don't have to come

**[05:28]** home right and so you don't have to come to a conference uh so feel free to uh

**[05:31]** to a conference uh so feel free to uh

**[05:31]** to a conference uh so feel free to uh connect so with that I will just switch

**[05:35]** connect so with that I will just switch

**[05:35]** connect so with that I will just switch to uh the

**[05:38]** to uh the

**[05:38]** to uh the GitHub repository. Okay. So, and I'll

**[05:41]** GitHub repository. Okay. So, and I'll

**[05:41]** GitHub repository. Okay. So, and I'll just uh walk you through the notebook.

**[05:45]** just uh walk you through the notebook.

**[05:45]** just uh walk you through the notebook. So, the my idea is not to have any

**[05:47]** So, the my idea is not to have any

**[05:47]** So, the my idea is not to have any presentation because uh first uh I'm

**[05:50]** presentation because uh first uh I'm

**[05:50]** presentation because uh first uh I'm lazy and second it's little complicated.

**[05:52]** lazy and second it's little complicated.

**[05:52]** lazy and second it's little complicated. I thought that taking images and

**[05:53]** I thought that taking images and

**[05:53]** I thought that taking images and embedded in the notebook is uh much

**[05:56]** embedded in the notebook is uh much

**[05:56]** embedded in the notebook is uh much easier. So uh you will find this uh


### [06:00 - 07:00]

**[06:00]** easier. So uh you will find this uh

**[06:00]** easier. So uh you will find this uh GitHub repository

**[06:02]** GitHub repository

**[06:02]** GitHub repository uh and in that there are many things

**[06:05]** uh and in that there are many things

**[06:05]** uh and in that there are many things there but what we are going to focus on

**[06:08]** there but what we are going to focus on

**[06:08]** there but what we are going to focus on is if you come to this uh section 8 and

**[06:12]** is if you come to this uh section 8 and

**[06:12]** is if you come to this uh section 8 and come to this first one agentic

**[06:14]** come to this first one agentic

**[06:14]** come to this first one agentic voice-based rag

**[06:17]** voice-based rag

**[06:17]** voice-based rag uh so I just added that agent thing

**[06:19]** uh so I just added that agent thing

**[06:19]** uh so I just added that agent thing yesterday so that's why so I had no idea

**[06:23]** yesterday so that's why so I had no idea

**[06:23]** yesterday so that's why so I had no idea of that so uh so what we are going to do

**[06:27]** of that so uh so what we are going to do

**[06:27]** of that so uh so what we are going to do is these two notebooks are exactly same.

**[06:29]** is these two notebooks are exactly same.

**[06:29]** is these two notebooks are exactly same. One is without output, one is with

**[06:30]** One is without output, one is with

**[06:30]** One is without output, one is with output. I find it uh useful to have both

**[06:34]** output. I find it uh useful to have both

**[06:34]** output. I find it uh useful to have both copies because if you are doing it for

**[06:35]** copies because if you are doing it for

**[06:36]** copies because if you are doing it for the first time um you may like to start

**[06:38]** the first time um you may like to start

**[06:38]** the first time um you may like to start with this don't see the output and run

**[06:40]** with this don't see the output and run

**[06:40]** with this don't see the output and run through and at the same time if you want

**[06:42]** through and at the same time if you want

**[06:42]** through and at the same time if you want to see what it is you know what is the

**[06:44]** to see what it is you know what is the

**[06:44]** to see what it is you know what is the expected output and all that you can go

**[06:46]** expected output and all that you can go

**[06:46]** expected output and all that you can go onto this all right so for the purpose

**[06:49]** onto this all right so for the purpose

**[06:49]** onto this all right so for the purpose of today's uh uh workshop I will start

**[06:52]** of today's uh uh workshop I will start

**[06:52]** of today's uh uh workshop I will start with an introduction

**[06:54]** with an introduction

**[06:54]** with an introduction and then I will um come here okay and if

**[06:59]** and then I will um come here okay and if

**[06:59]** and then I will um come here okay and if you feel that uh this is not something


### [07:00 - 08:00]

**[07:01]** you feel that uh this is not something

**[07:01]** you feel that uh this is not something that you are interested in or this is

**[07:04]** that you are interested in or this is

**[07:04]** that you are interested in or this is not something that you are looking for

**[07:05]** not something that you are looking for

**[07:06]** not something that you are looking for you know feel free to uh uh you know uh

**[07:10]** you know feel free to uh uh you know uh

**[07:10]** you know feel free to uh uh you know uh go to some other place because I don't

**[07:12]** go to some other place because I don't

**[07:12]** go to some other place because I don't want to waste your time uh uh but I want

**[07:14]** want to waste your time uh uh but I want

**[07:14]** want to waste your time uh uh but I want to make sure that if you are here for

**[07:16]** to make sure that if you are here for

**[07:16]** to make sure that if you are here for next 1 hour you learn something new uh

**[07:19]** next 1 hour you learn something new uh

**[07:19]** next 1 hour you learn something new uh with respect to what you already know at

**[07:21]** with respect to what you already know at

**[07:21]** with respect to what you already know at this point in time okay and if you have

**[07:24]** this point in time okay and if you have

**[07:24]** this point in time okay and if you have any questions uh feel free to ask so

**[07:27]** any questions uh feel free to ask so

**[07:27]** any questions uh feel free to ask so that's that's the other thing okay let

**[07:29]** that's that's the other thing okay let

**[07:29]** that's that's the other thing okay let me just expand And this is little too

**[07:32]** me just expand And this is little too

**[07:32]** me just expand And this is little too big uh here. So

**[07:35]** big uh here. So

**[07:35]** big uh here. So uh okay. So I noticed that most of you

**[07:41]** uh okay. So I noticed that most of you

**[07:41]** uh okay. So I noticed that most of you are aware of rag. Uh but we are going to

**[07:43]** are aware of rag. Uh but we are going to

**[07:43]** are aware of rag. Uh but we are going to talk about uh multimodal rack for a

**[07:47]** talk about uh multimodal rack for a

**[07:47]** talk about uh multimodal rack for a moment. Uh just to set the premise and

**[07:49]** moment. Uh just to set the premise and

**[07:49]** moment. Uh just to set the premise and then we will uh get into the vision

**[07:51]** then we will uh get into the vision

**[07:51]** then we will uh get into the vision based retrieval. Okay. So if you think

**[07:54]** based retrieval. Okay. So if you think

**[07:54]** based retrieval. Okay. So if you think about uh multimodal rag uh


### [08:00 - 09:00]

**[08:01]** about uh multimodal rag uh

**[08:02]** about uh multimodal rag uh what we essentially do is and this is by

**[08:05]** what we essentially do is and this is by

**[08:05]** what we essentially do is and this is by no mean is the only architecture. This

**[08:07]** no mean is the only architecture. This

**[08:07]** no mean is the only architecture. This is just one of the architecture. There

**[08:08]** is just one of the architecture. There

**[08:08]** is just one of the architecture. There are many different ways that you can do

**[08:10]** are many different ways that you can do

**[08:10]** are many different ways that you can do multimodal rack but in general this is

**[08:13]** multimodal rack but in general this is

**[08:13]** multimodal rack but in general this is what uh we have been doing and still

**[08:15]** what uh we have been doing and still

**[08:15]** what uh we have been doing and still today we do. You take a data and that

**[08:18]** today we do. You take a data and that

**[08:18]** today we do. You take a data and that data will contain images, text and uh

**[08:22]** data will contain images, text and uh

**[08:22]** data will contain images, text and uh tables.

**[08:23]** tables.

**[08:23]** tables. The first thing that we do is we use

**[08:26]** The first thing that we do is we use

**[08:26]** The first thing that we do is we use some framework or

**[08:28]** some framework or

**[08:28]** some framework or is that so bad or

**[08:32]** is that so bad or

**[08:32]** is that so bad or okay thank you. So so we can use any

**[08:36]** okay thank you. So so we can use any

**[08:36]** okay thank you. So so we can use any framework of our choice or you can write

**[08:38]** framework of our choice or you can write

**[08:38]** framework of our choice or you can write your own custom script or you can use

**[08:40]** your own custom script or you can use

**[08:40]** your own custom script or you can use any managed service like text OCR based

**[08:42]** any managed service like text OCR based

**[08:42]** any managed service like text OCR based technique. The idea is you extract the

**[08:45]** technique. The idea is you extract the

**[08:45]** technique. The idea is you extract the images, tables and

**[08:47]** images, tables and

**[08:47]** images, tables and uh uh text out you know separately. You

**[08:51]** uh uh text out you know separately. You

**[08:51]** uh uh text out you know separately. You can have some metadata uh to make an uh

**[08:53]** can have some metadata uh to make an uh

**[08:53]** can have some metadata uh to make an uh hash which tells you that this image is

**[08:57]** hash which tells you that this image is

**[08:57]** hash which tells you that this image is coming from which page and all that. But

**[08:58]** coming from which page and all that. But

**[08:58]** coming from which page and all that. But essentially you divide all these three


### [09:00 - 10:00]

**[09:00]** essentially you divide all these three

**[09:00]** essentially you divide all these three separately. Then you can use one

**[09:03]** separately. Then you can use one

**[09:03]** separately. Then you can use one multimodal embedding model and this

**[09:06]** multimodal embedding model and this

**[09:06]** multimodal embedding model and this multimodal embedding model can take any

**[09:07]** multimodal embedding model can take any

**[09:07]** multimodal embedding model can take any of these three entities because it's

**[09:09]** of these three entities because it's

**[09:09]** of these three entities because it's multimodal. It can take any of these

**[09:11]** multimodal. It can take any of these

**[09:12]** multimodal. It can take any of these three and when I say multimodal you can

**[09:14]** three and when I say multimodal you can

**[09:14]** three and when I say multimodal you can think of it like input can be

**[09:15]** think of it like input can be

**[09:15]** think of it like input can be multimodal. Okay. And then it will

**[09:18]** multimodal. Okay. And then it will

**[09:18]** multimodal. Okay. And then it will generate some vectors for images. it

**[09:20]** generate some vectors for images. it

**[09:20]** generate some vectors for images. it will generate some vectors, tables, text

**[09:21]** will generate some vectors, tables, text

**[09:21]** will generate some vectors, tables, text and all that. Then you go to the

**[09:23]** and all that. Then you go to the

**[09:23]** and all that. Then you go to the database any vector database and store

**[09:25]** database any vector database and store

**[09:25]** database any vector database and store all these embeddings. So what you are

**[09:27]** all these embeddings. So what you are

**[09:27]** all these embeddings. So what you are essentially storing here are the actual

**[09:29]** essentially storing here are the actual

**[09:29]** essentially storing here are the actual embeddings of text, tables and images.

**[09:33]** embeddings of text, tables and images.

**[09:33]** embeddings of text, tables and images. And then comes the retrieval part. When

**[09:35]** And then comes the retrieval part. When

**[09:35]** And then comes the retrieval part. When you ask a question any raw question like

**[09:38]** you ask a question any raw question like

**[09:38]** you ask a question any raw question like raw text, it goes through the same

**[09:41]** raw text, it goes through the same

**[09:41]** raw text, it goes through the same embedding model. Then it is first

**[09:43]** embedding model. Then it is first

**[09:43]** embedding model. Then it is first searched here. It will get some relevant

**[09:45]** searched here. It will get some relevant

**[09:45]** searched here. It will get some relevant chunk which could be again image, text

**[09:47]** chunk which could be again image, text

**[09:47]** chunk which could be again image, text or table and then you take those chunks

**[09:51]** or table and then you take those chunks

**[09:51]** or table and then you take those chunks along with your text and use a

**[09:53]** along with your text and use a

**[09:53]** along with your text and use a multimodal LLM. Why multimodal? Because

**[09:55]** multimodal LLM. Why multimodal? Because

**[09:55]** multimodal LLM. Why multimodal? Because your relevant chunk can be images, text

**[09:58]** your relevant chunk can be images, text

**[09:58]** your relevant chunk can be images, text or table, right? And then you get an


### [10:00 - 11:00]

**[10:01]** or table, right? And then you get an

**[10:01]** or table, right? And then you get an answer. So this is one approach. The

**[10:03]** answer. So this is one approach. The

**[10:03]** answer. So this is one approach. The second approach is you do the same thing

**[10:07]** second approach is you do the same thing

**[10:07]** second approach is you do the same thing like this part is common. After that you

**[10:10]** like this part is common. After that you

**[10:10]** like this part is common. After that you used a model which will just generate a

**[10:13]** used a model which will just generate a

**[10:13]** used a model which will just generate a summary of all this separately. So it

**[10:16]** summary of all this separately. So it

**[10:16]** summary of all this separately. So it will use uh you can think of it like a

**[10:19]** will use uh you can think of it like a

**[10:19]** will use uh you can think of it like a summary of an image is nothing but image

**[10:21]** summary of an image is nothing but image

**[10:21]** summary of an image is nothing but image captioning right. It will generate an

**[10:23]** captioning right. It will generate an

**[10:23]** captioning right. It will generate an summary of this image summary of the

**[10:25]** summary of this image summary of the

**[10:25]** summary of this image summary of the table summary of the text. Now all you

**[10:27]** table summary of the text. Now all you

**[10:27]** table summary of the text. Now all you have is the summary. That means it's all

**[10:29]** have is the summary. That means it's all

**[10:29]** have is the summary. That means it's all text. So now you can use any text based

**[10:32]** text. So now you can use any text based

**[10:32]** text. So now you can use any text based embedding model to generate the

**[10:34]** embedding model to generate the

**[10:34]** embedding model to generate the embedding of the summary. And then you

**[10:37]** embedding of the summary. And then you

**[10:37]** embedding of the summary. And then you store this embeddings here. So what you

**[10:39]** store this embeddings here. So what you

**[10:39]** store this embeddings here. So what you are storing here are only the embeddings

**[10:42]** are storing here are only the embeddings

**[10:42]** are storing here are only the embeddings of the summary not the actual data.

**[10:46]** of the summary not the actual data.

**[10:46]** of the summary not the actual data. Right? And then when the question comes

**[10:49]** Right? And then when the question comes

**[10:49]** Right? And then when the question comes now we are talking about the option

**[10:51]** now we are talking about the option

**[10:51]** now we are talking about the option number two. When the question comes we

**[10:54]** number two. When the question comes we

**[10:54]** number two. When the question comes we do a semantic search with the database

**[10:56]** do a semantic search with the database

**[10:56]** do a semantic search with the database and what we get as a chunk or some

**[10:59]** and what we get as a chunk or some

**[10:59]** and what we get as a chunk or some summary. Now that summary could be a


### [11:00 - 12:00]

**[11:01]** summary. Now that summary could be a

**[11:01]** summary. Now that summary could be a summary of an image, table or text. We

**[11:04]** summary of an image, table or text. We

**[11:04]** summary of an image, table or text. We don't know whatever it is.

**[11:06]** don't know whatever it is.

**[11:06]** don't know whatever it is. But whatever we get both of them are of

**[11:09]** But whatever we get both of them are of

**[11:09]** But whatever we get both of them are of text format. So that's why we can use a

**[11:12]** text format. So that's why we can use a

**[11:12]** text format. So that's why we can use a general textbased LLM to generate the

**[11:14]** general textbased LLM to generate the

**[11:14]** general textbased LLM to generate the output. Okay. So that's uh option number

**[11:17]** output. Okay. So that's uh option number

**[11:17]** output. Okay. So that's uh option number two. The option number three is exactly

**[11:19]** two. The option number three is exactly

**[11:20]** two. The option number three is exactly same as option number two. Uh with a

**[11:23]** same as option number two. Uh with a

**[11:23]** same as option number two. Uh with a slight change here when you store the

**[11:26]** slight change here when you store the

**[11:26]** slight change here when you store the summary you also think of it like this.

**[11:29]** summary you also think of it like this.

**[11:29]** summary you also think of it like this. You have a hash here. Let's say a

**[11:31]** You have a hash here. Let's say a

**[11:31]** You have a hash here. Let's say a dictionary which says that u this image

**[11:35]** dictionary which says that u this image

**[11:35]** dictionary which says that u this image number one uh summary is this image

**[11:38]** number one uh summary is this image

**[11:38]** number one uh summary is this image number two summary is this table number

**[11:39]** number two summary is this table number

**[11:39]** number two summary is this table number one summary is this you create a hash

**[11:42]** one summary is this you create a hash

**[11:42]** one summary is this you create a hash file or hash any data structure of your

**[11:45]** file or hash any data structure of your

**[11:45]** file or hash any data structure of your choice so that you can you know come

**[11:48]** choice so that you can you know come

**[11:48]** choice so that you can you know come back later on from a certain summary and

**[11:51]** back later on from a certain summary and

**[11:51]** back later on from a certain summary and you can figure out this is summary of

**[11:53]** you can figure out this is summary of

**[11:53]** you can figure out this is summary of what entity okay but you store only the

**[11:56]** what entity okay but you store only the

**[11:56]** what entity okay but you store only the summary just like before but the

**[11:58]** summary just like before but the

**[11:58]** summary just like before but the difference here with respect to option


### [12:00 - 13:00]

**[12:00]** difference here with respect to option

**[12:00]** difference here with respect to option Number two is when you ask a question

**[12:03]** Number two is when you ask a question

**[12:03]** Number two is when you ask a question you get some relevant chunk which is a

**[12:05]** you get some relevant chunk which is a

**[12:05]** you get some relevant chunk which is a summary. Then you go back to that hash

**[12:08]** summary. Then you go back to that hash

**[12:08]** summary. Then you go back to that hash and find out the actual data not the

**[12:10]** and find out the actual data not the

**[12:10]** and find out the actual data not the summary the actual data which is mapped

**[12:12]** summary the actual data which is mapped

**[12:12]** summary the actual data which is mapped against those summary and then you take

**[12:15]** against those summary and then you take

**[12:15]** against those summary and then you take those actual data and then pass it on

**[12:17]** those actual data and then pass it on

**[12:17]** those actual data and then pass it on here. So what you're doing is summary

**[12:20]** here. So what you're doing is summary

**[12:20]** here. So what you're doing is summary you are using here just to reduce the

**[12:22]** you are using here just to reduce the

**[12:22]** you are using here just to reduce the search space just for semantic search.

**[12:25]** search space just for semantic search.

**[12:25]** search space just for semantic search. When you get that relevant chunks you

**[12:27]** When you get that relevant chunks you

**[12:27]** When you get that relevant chunks you don't care about that summary. You just

**[12:29]** don't care about that summary. You just

**[12:29]** don't care about that summary. You just take the original data from that hash

**[12:31]** take the original data from that hash

**[12:31]** take the original data from that hash and then you take those relevant chunks

**[12:34]** and then you take those relevant chunks

**[12:34]** and then you take those relevant chunks and your question and since relevant

**[12:36]** and your question and since relevant

**[12:36]** and your question and since relevant chunk can be again text image or um

**[12:40]** chunk can be again text image or um

**[12:40]** chunk can be again text image or um table you need a multimodal LLM okay and

**[12:43]** table you need a multimodal LLM okay and

**[12:43]** table you need a multimodal LLM okay and you generate the answer are you with

**[12:46]** you generate the answer are you with

**[12:46]** you generate the answer are you with yeah

**[12:47]** yeah

**[12:47]** yeah >> um let's say you have a table but the

**[12:49]** >> um let's say you have a table but the

**[12:49]** >> um let's say you have a table but the table is an image

**[12:51]** table is an image

**[12:51]** table is an image >> which one would you prefer to use in

**[12:53]** >> which one would you prefer to use in

**[12:53]** >> which one would you prefer to use in that case

**[12:54]** that case

**[12:54]** that case >> yeah so that's a good question so the

**[12:57]** >> yeah so that's a good question so the

**[12:57]** >> yeah so that's a good question so the question is If you have a table which is


### [13:00 - 14:00]

**[13:00]** question is If you have a table which is

**[13:00]** question is If you have a table which is an image right. So now it's all whatever

**[13:03]** an image right. So now it's all whatever

**[13:03]** an image right. So now it's all whatever you are saying is all at this level. So

**[13:05]** you are saying is all at this level. So

**[13:05]** you are saying is all at this level. So you don't you it's all up to you how you

**[13:08]** you don't you it's all up to you how you

**[13:08]** you don't you it's all up to you how you segregate these three entities. So let's

**[13:11]** segregate these three entities. So let's

**[13:11]** segregate these three entities. So let's say you use an OCR based uh uh technique

**[13:14]** say you use an OCR based uh uh technique

**[13:14]** say you use an OCR based uh uh technique and let's say it it's identified a table

**[13:17]** and let's say it it's identified a table

**[13:17]** and let's say it it's identified a table as an image. So it will be treated as an

**[13:20]** as an image. So it will be treated as an

**[13:20]** as an image. So it will be treated as an image because the model till this point

**[13:23]** image because the model till this point

**[13:23]** image because the model till this point the model has no idea from where these

**[13:25]** the model has no idea from where these

**[13:25]** the model has no idea from where these three are coming because these are like

**[13:27]** three are coming because these are like

**[13:27]** three are coming because these are like prerequisites for this particular

**[13:28]** prerequisites for this particular

**[13:28]** prerequisites for this particular pipeline. Okay. So are you with me with

**[13:32]** pipeline. Okay. So are you with me with

**[13:32]** pipeline. Okay. So are you with me with all these three approach? Yes. Yeah.

**[13:41]** >> This one.

**[13:42]** >> This one. >> Oh okay. So these are nothing but uh uh

**[13:44]** >> Oh okay. So these are nothing but uh uh

**[13:44]** >> Oh okay. So these are nothing but uh uh models basically.

**[13:46]** models basically.

**[13:46]** models basically. >> It it doesn't resonate. It's what I

**[13:48]** >> It it doesn't resonate. It's what I

**[13:48]** >> It it doesn't resonate. It's what I understand now but

**[13:50]** understand now but

**[13:50]** understand now but >> yeah yeah yeah right that's correct yes

**[13:52]** >> yeah yeah yeah right that's correct yes

**[13:52]** >> yeah yeah yeah right that's correct yes so it could be this is any so here we

**[13:56]** so it could be this is any so here we

**[13:56]** so it could be this is any so here we have a multimodal embedding model right

**[13:58]** have a multimodal embedding model right

**[13:58]** have a multimodal embedding model right here it's actually first you need a


### [14:00 - 15:00]

**[14:00]** here it's actually first you need a

**[14:00]** here it's actually first you need a model which will generate the summary

**[14:02]** model which will generate the summary

**[14:02]** model which will generate the summary then you can think of it like another

**[14:03]** then you can think of it like another

**[14:04]** then you can think of it like another model which will generate the embeddings

**[14:06]** model which will generate the embeddings

**[14:06]** model which will generate the embeddings so uh it's just a one icon but think of

**[14:09]** so uh it's just a one icon but think of

**[14:09]** so uh it's just a one icon but think of it like there are two things happening

**[14:11]** it like there are two things happening

**[14:11]** it like there are two things happening in sequence okay are you with me so far

**[14:14]** in sequence okay are you with me so far

**[14:14]** in sequence okay are you with me so far yes okay so do you see any problem in

**[14:17]** yes okay so do you see any problem in

**[14:17]** yes okay so do you see any problem in this when you have a multimodal data

**[14:19]** this when you have a multimodal data

**[14:19]** this when you have a multimodal data there's no problem as such buth there

**[14:21]** there's no problem as such buth there

**[14:21]** there's no problem as such buth there are few scenarios when this may not work

**[14:25]** are few scenarios when this may not work

**[14:25]** are few scenarios when this may not work okay so

**[14:27]** okay so

**[14:27]** okay so scenarios like like what you mentioned

**[14:31]** scenarios like like what you mentioned

**[14:31]** scenarios like like what you mentioned uh there are few documents or data which

**[14:35]** uh there are few documents or data which

**[14:35]** uh there are few documents or data which we have seen where the PDF was created

**[14:39]** we have seen where the PDF was created

**[14:39]** we have seen where the PDF was created using images so basically you can think

**[14:42]** using images so basically you can think

**[14:42]** using images so basically you can think of like this um let's say uh uh

**[14:47]** of like this um let's say uh uh

**[14:47]** of like this um let's say uh uh toll that we uh cross in a highway all

**[14:51]** toll that we uh cross in a highway all

**[14:51]** toll that we uh cross in a highway all are images right they just take the

**[14:52]** are images right they just take the

**[14:52]** are images right they just take the images of our number plate and all that.

**[14:55]** images of our number plate and all that.

**[14:55]** images of our number plate and all that. Uh similarly you can think of uh any

**[14:58]** Uh similarly you can think of uh any

**[14:58]** Uh similarly you can think of uh any government organization where forms are


### [15:00 - 16:00]

**[15:00]** government organization where forms are

**[15:00]** government organization where forms are just uh they they just keep on uh taking

**[15:03]** just uh they they just keep on uh taking

**[15:03]** just uh they they just keep on uh taking images and later on all those images are

**[15:06]** images and later on all those images are

**[15:06]** images and later on all those images are converted into a PDF. So in that case

**[15:10]** converted into a PDF. So in that case

**[15:10]** converted into a PDF. So in that case not always uh these techniques of

**[15:14]** not always uh these techniques of

**[15:14]** not always uh these techniques of extracting images, tables and text works

**[15:17]** extracting images, tables and text works

**[15:17]** extracting images, tables and text works nicely. It's not like uh it never works.

**[15:20]** nicely. It's not like uh it never works.

**[15:20]** nicely. It's not like uh it never works. It all about how your data behaves with

**[15:23]** It all about how your data behaves with

**[15:23]** It all about how your data behaves with your technique that you are

**[15:24]** your technique that you are

**[15:24]** your technique that you are implementing. Okay. So now the next

**[15:27]** implementing. Okay. So now the next

**[15:27]** implementing. Okay. So now the next technique that we are going to discuss

**[15:29]** technique that we are going to discuss

**[15:29]** technique that we are going to discuss today is using a vision- based uh

**[15:31]** today is using a vision- based uh

**[15:31]** today is using a vision- based uh retrieval model and we will see that why

**[15:33]** retrieval model and we will see that why

**[15:33]** retrieval model and we will see that why we are using this but the premise is

**[15:35]** we are using this but the premise is

**[15:35]** we are using this but the premise is this. If you use if if if your data with

**[15:39]** this. If you use if if if your data with

**[15:39]** this. If you use if if if your data with your data any of these uh three options

**[15:41]** your data any of these uh three options

**[15:41]** your data any of these uh three options works you just go with this what we're

**[15:44]** works you just go with this what we're

**[15:44]** works you just go with this what we're going to discuss in next one hour you

**[15:46]** going to discuss in next one hour you

**[15:46]** going to discuss in next one hour you it's not relevant for you but this you

**[15:48]** it's not relevant for you but this you

**[15:48]** it's not relevant for you but this you know what we are going to discuss is an

**[15:50]** know what we are going to discuss is an

**[15:50]** know what we are going to discuss is an option number four which is uh a smarter

**[15:53]** option number four which is uh a smarter

**[15:53]** option number four which is uh a smarter technique which is based on a vision

**[15:55]** technique which is based on a vision

**[15:55]** technique which is based on a vision based model to uh perform the retrieval.

**[15:59]** based model to uh perform the retrieval.

**[15:59]** based model to uh perform the retrieval. You don't have to extract all these


### [16:00 - 17:00]

**[16:01]** You don't have to extract all these

**[16:01]** You don't have to extract all these three entity in the first place because

**[16:03]** three entity in the first place because

**[16:03]** three entity in the first place because think of it like this. The moment you

**[16:05]** think of it like this. The moment you

**[16:05]** think of it like this. The moment you have your data and you first in the

**[16:08]** have your data and you first in the

**[16:08]** have your data and you first in the first place you segregate these three

**[16:10]** first place you segregate these three

**[16:10]** first place you segregate these three things. It's just like you have a family

**[16:13]** things. It's just like you have a family

**[16:13]** things. It's just like you have a family you just uh you know let your kid go

**[16:16]** you just uh you know let your kid go

**[16:16]** you just uh you know let your kid go somewhere you go somewhere and you know

**[16:19]** somewhere you go somewhere and you know

**[16:19]** somewhere you go somewhere and you know your partner goes somewhere else. It's a

**[16:21]** your partner goes somewhere else. It's a

**[16:21]** your partner goes somewhere else. It's a good thing but uh you know uh if all of

**[16:23]** good thing but uh you know uh if all of

**[16:23]** good thing but uh you know uh if all of them goes you know separate and you

**[16:26]** them goes you know separate and you

**[16:26]** them goes you know separate and you expect somebody else to identify that

**[16:28]** expect somebody else to identify that

**[16:28]** expect somebody else to identify that they all are part of one family it's a

**[16:30]** they all are part of one family it's a

**[16:30]** they all are part of one family it's a it's a task right so for that external

**[16:33]** it's a task right so for that external

**[16:33]** it's a task right so for that external person

**[16:34]** person

**[16:34]** person uh so that is what we are going to solve

**[16:37]** uh so that is what we are going to solve

**[16:37]** uh so that is what we are going to solve that can we can we come up with a

**[16:40]** that can we can we come up with a

**[16:40]** that can we can we come up with a technique where we don't do all this

**[16:43]** technique where we don't do all this

**[16:43]** technique where we don't do all this okay so before we go uh I think you have

**[16:45]** okay so before we go uh I think you have

**[16:45]** okay so before we go uh I think you have a question yeah

**[16:46]** a question yeah

**[16:46]** a question yeah >> yeah I think you kind of answered my

**[16:47]** >> yeah I think you kind of answered my

**[16:47]** >> yeah I think you kind of answered my question because you were explaining the

**[16:49]** question because you were explaining the

**[16:49]** question because you were explaining the case about scanning all the PDFs

**[16:52]** case about scanning all the PDFs

**[16:52]** case about scanning all the PDFs >> and it wouldn't quite work and I was a

**[16:55]** >> and it wouldn't quite work and I was a

**[16:55]** >> and it wouldn't quite work and I was a little bit confused as to why these

**[16:58]** little bit confused as to why these

**[16:58]** little bit confused as to why these approaches wouldn't work.

**[16:59]** approaches wouldn't work.

**[16:59]** approaches wouldn't work. >> Yeah.

**[16:59]** >> Yeah.

**[16:59]** >> Yeah. >> But then I think you're going towards


### [17:00 - 18:00]

**[17:01]** >> But then I think you're going towards

**[17:01]** >> But then I think you're going towards the notion that we need to establish

**[17:02]** the notion that we need to establish

**[17:02]** the notion that we need to establish relationships between

**[17:03]** relationships between

**[17:03]** relationships between >> Exactly.

**[17:05]** >> Exactly.

**[17:05]** >> Exactly. >> Absolutely. Yeah. So I think I'll give

**[17:08]** >> Absolutely. Yeah. So I think I'll give

**[17:08]** >> Absolutely. Yeah. So I think I'll give you one more uh one more uh example. Uh

**[17:12]** you one more uh one more uh example. Uh

**[17:12]** you one more uh one more uh example. Uh if you go to IKEA, you buy something

**[17:14]** if you go to IKEA, you buy something

**[17:14]** if you go to IKEA, you buy something from IKEA. If you have seen the IKEA uh

**[17:17]** from IKEA. If you have seen the IKEA uh

**[17:17]** from IKEA. If you have seen the IKEA uh in uh you know instructions you know we

**[17:19]** in uh you know instructions you know we

**[17:19]** in uh you know instructions you know we don't I personally never looked into

**[17:21]** don't I personally never looked into

**[17:21]** don't I personally never looked into those instruction but while I was

**[17:23]** those instruction but while I was

**[17:23]** those instruction but while I was reading that research paper they said

**[17:24]** reading that research paper they said

**[17:24]** reading that research paper they said that refer to that uh because we

**[17:27]** that refer to that uh because we

**[17:27]** that refer to that uh because we generally go to YouTube and search what

**[17:29]** generally go to YouTube and search what

**[17:29]** generally go to YouTube and search what is the instruction steps and all that

**[17:30]** is the instruction steps and all that

**[17:30]** is the instruction steps and all that right but if you look at the IKEA

**[17:32]** right but if you look at the IKEA

**[17:32]** right but if you look at the IKEA instruction set they just have emoji

**[17:35]** instruction set they just have emoji

**[17:35]** instruction set they just have emoji kind of a human uh and they are just

**[17:37]** kind of a human uh and they are just

**[17:37]** kind of a human uh and they are just assembling something there is no text

**[17:39]** assembling something there is no text

**[17:39]** assembling something there is no text there there's nothing there so unless or

**[17:41]** there there's nothing there so unless or

**[17:41]** there there's nothing there so unless or until you have a visual understanding of

**[17:44]** until you have a visual understanding of

**[17:44]** until you have a visual understanding of what it you will not have any idea what

**[17:46]** what it you will not have any idea what

**[17:46]** what it you will not have any idea what they're talking about. Okay. So there

**[17:48]** they're talking about. Okay. So there

**[17:48]** they're talking about. Okay. So there are some data sets and I'll show you a

**[17:50]** are some data sets and I'll show you a

**[17:50]** are some data sets and I'll show you a few of the data sets where the uh there

**[17:53]** few of the data sets where the uh there

**[17:53]** few of the data sets where the uh there are some text embedded within the image

**[17:56]** are some text embedded within the image

**[17:56]** are some text embedded within the image and there are just an image they don't

**[17:58]** and there are just an image they don't

**[17:58]** and there are just an image they don't have any text. So you need some model or


### [18:00 - 19:00]

**[18:01]** have any text. So you need some model or

**[18:01]** have any text. So you need some model or some uh technique which can help us to

**[18:04]** some uh technique which can help us to

**[18:04]** some uh technique which can help us to understand uh what is the semantics of

**[18:07]** understand uh what is the semantics of

**[18:07]** understand uh what is the semantics of the data. Okay. So let's see how we are

**[18:11]** the data. Okay. So let's see how we are

**[18:11]** the data. Okay. So let's see how we are going to solve this.

**[18:13]** going to solve this.

**[18:13]** going to solve this. So this is uh again the text might be

**[18:16]** So this is uh again the text might be

**[18:16]** So this is uh again the text might be small uh you can just leave that okay

**[18:18]** small uh you can just leave that okay

**[18:18]** small uh you can just leave that okay you can open it in your laptop uh or

**[18:21]** you can open it in your laptop uh or

**[18:21]** you can open it in your laptop uh or I'll try to explain it as much as I can.

**[18:24]** I'll try to explain it as much as I can.

**[18:24]** I'll try to explain it as much as I can. So this is the traditional technique

**[18:26]** So this is the traditional technique

**[18:26]** So this is the traditional technique that we discussed right you first place

**[18:28]** that we discussed right you first place

**[18:28]** that we discussed right you first place you divide all these three entities uh

**[18:31]** you divide all these three entities uh

**[18:31]** you divide all these three entities uh separately uh but this is not very

**[18:34]** separately uh but this is not very

**[18:34]** separately uh but this is not very helpful because if you look uh you know

**[18:36]** helpful because if you look uh you know

**[18:36]** helpful because if you look uh you know think about it let's say you were given

**[18:39]** think about it let's say you were given

**[18:39]** think about it let's say you were given a book and uh you were asked to

**[18:43]** a book and uh you were asked to

**[18:43]** a book and uh you were asked to answer a particular question let's say I

**[18:45]** answer a particular question let's say I

**[18:45]** answer a particular question let's say I give you this book by the way this is a

**[18:47]** give you this book by the way this is a

**[18:47]** give you this book by the way this is a fantastic book from Simon have you heard

**[18:48]** fantastic book from Simon have you heard

**[18:48]** fantastic book from Simon have you heard of this book yeah if you are getting

**[18:51]** of this book yeah if you are getting

**[18:51]** of this book yeah if you are getting started with machine learning uh deep

**[18:52]** started with machine learning uh deep

**[18:52]** started with machine learning uh deep learning uh you know you and uh read

**[18:55]** learning uh you know you and uh read

**[18:55]** learning uh you know you and uh read this book. This is a really fantastic

**[18:57]** this book. This is a really fantastic

**[18:57]** this book. This is a really fantastic book. It's a recently published book and

**[18:59]** book. It's a recently published book and

**[18:59]** book. It's a recently published book and professor Simon is very reachable. It's


### [19:00 - 20:00]

**[19:02]** professor Simon is very reachable. It's

**[19:02]** professor Simon is very reachable. It's it's uh it's a fantastic book. So let's

**[19:04]** it's uh it's a fantastic book. So let's

**[19:04]** it's uh it's a fantastic book. So let's say if I give you this book and if I ask

**[19:07]** say if I give you this book and if I ask

**[19:07]** say if I give you this book and if I ask you some question and let's say you are

**[19:09]** you some question and let's say you are

**[19:10]** you some question and let's say you are not aware of this particular topic, you

**[19:13]** not aware of this particular topic, you

**[19:13]** not aware of this particular topic, you will not uh go and scan the entire book.

**[19:17]** will not uh go and scan the entire book.

**[19:17]** will not uh go and scan the entire book. What you will do is you will try to

**[19:18]** What you will do is you will try to

**[19:18]** What you will do is you will try to first find the structure of the book.

**[19:20]** first find the structure of the book.

**[19:20]** first find the structure of the book. Maybe you will find the index where is

**[19:22]** Maybe you will find the index where is

**[19:22]** Maybe you will find the index where is the index, where is the appendex and all

**[19:23]** the index, where is the appendex and all

**[19:23]** the index, where is the appendex and all that and then you will try to uh figure

**[19:26]** that and then you will try to uh figure

**[19:26]** that and then you will try to uh figure out which chapter this book might uh

**[19:28]** out which chapter this book might uh

**[19:28]** out which chapter this book might uh this question uh can be answered from

**[19:31]** this question uh can be answered from

**[19:31]** this question uh can be answered from and then you will go to that specific

**[19:33]** and then you will go to that specific

**[19:33]** and then you will go to that specific chapter and then read through those

**[19:35]** chapter and then read through those

**[19:35]** chapter and then read through those chapters. Right? So that is what a human

**[19:37]** chapters. Right? So that is what a human

**[19:37]** chapters. Right? So that is what a human will do and that is exactly the

**[19:41]** will do and that is exactly the

**[19:41]** will do and that is exactly the philosophy of uh calling. Okay. So

**[19:46]** philosophy of uh calling. Okay. So

**[19:46]** philosophy of uh calling. Okay. So when you get a question

**[19:49]** when you get a question

**[19:49]** when you get a question what you do is first you will first scan

**[19:53]** what you do is first you will first scan

**[19:53]** what you do is first you will first scan through the appendix and all that and

**[19:55]** through the appendix and all that and

**[19:55]** through the appendix and all that and then you will figure out where exactly

**[19:58]** then you will figure out where exactly

**[19:58]** then you will figure out where exactly uh uh the portion where your question


### [20:00 - 21:00]

**[20:00]** uh uh the portion where your question

**[20:00]** uh uh the portion where your question can be answered and then you will

**[20:03]** can be answered and then you will

**[20:03]** can be answered and then you will accumulate all those relevant chunks or

**[20:06]** accumulate all those relevant chunks or

**[20:06]** accumulate all those relevant chunks or relevant information and then uh finally

**[20:09]** relevant information and then uh finally

**[20:09]** relevant information and then uh finally you will come up with a response. Right?

**[20:11]** you will come up with a response. Right?

**[20:11]** you will come up with a response. Right? So this is where uh or rather this was

**[20:15]** So this is where uh or rather this was

**[20:15]** So this is where uh or rather this was the motivation of this vision-based

**[20:17]** the motivation of this vision-based

**[20:17]** the motivation of this vision-based retrieval model called pali. Have you

**[20:19]** retrieval model called pali. Have you

**[20:19]** retrieval model called pali. Have you heard of this model call pali? Yeah.

**[20:22]** heard of this model call pali? Yeah.

**[20:22]** heard of this model call pali? Yeah. Okay. Yeah. A few of you. So call pali

**[20:25]** Okay. Yeah. A few of you. So call pali

**[20:25]** Okay. Yeah. A few of you. So call pali was introduced I think in uh July 2024

**[20:28]** was introduced I think in uh July 2024

**[20:28]** was introduced I think in uh July 2024 just less than a year back. Uh and the

**[20:32]** just less than a year back. Uh and the

**[20:32]** just less than a year back. Uh and the motivation is we will treat every page

**[20:37]** motivation is we will treat every page

**[20:37]** motivation is we will treat every page as an image. So assume that you have a

**[20:41]** as an image. So assume that you have a

**[20:41]** as an image. So assume that you have a PDF document of let's say 100 pages.

**[20:43]** PDF document of let's say 100 pages.

**[20:44]** PDF document of let's say 100 pages. Your data set is not one PDF but 100

**[20:46]** Your data set is not one PDF but 100

**[20:46]** Your data set is not one PDF but 100 images. Okay. There is no concept of

**[20:49]** images. Okay. There is no concept of

**[20:49]** images. Okay. There is no concept of retrieving u images, text and tables

**[20:51]** retrieving u images, text and tables

**[20:51]** retrieving u images, text and tables from there. So how it works?

**[20:54]** from there. So how it works?

**[20:54]** from there. So how it works? So

**[20:56]** So

**[20:56]** So it first creates patches


### [21:00 - 22:00]

**[21:00]** it first creates patches

**[21:00]** it first creates patches of every page. So now let's consider one

**[21:03]** of every page. So now let's consider one

**[21:03]** of every page. So now let's consider one page. One page is nothing but one image.

**[21:06]** page. One page is nothing but one image.

**[21:06]** page. One page is nothing but one image. And

**[21:08]** And

**[21:08]** And the same will apply on all the pages

**[21:11]** the same will apply on all the pages

**[21:11]** the same will apply on all the pages that you have in your document. The

**[21:13]** that you have in your document. The

**[21:13]** that you have in your document. The first thing that it will do is it will

**[21:15]** first thing that it will do is it will

**[21:15]** first thing that it will do is it will create some patches. Uh in the paper I

**[21:19]** create some patches. Uh in the paper I

**[21:19]** create some patches. Uh in the paper I think it was um the model was trained

**[21:21]** think it was um the model was trained

**[21:21]** think it was um the model was trained with uh 32 patches like 32 + 32 here.

**[21:26]** with uh 32 patches like 32 + 32 here.

**[21:26]** with uh 32 patches like 32 + 32 here. How many patches we have? We have 1 2 3

**[21:28]** How many patches we have? We have 1 2 3

**[21:28]** How many patches we have? We have 1 2 3 4 5 uh 15 patches. Right?

**[21:33]** 4 5 uh 15 patches. Right?

**[21:33]** 4 5 uh 15 patches. Right? Now what we do is after that once you

**[21:36]** Now what we do is after that once you

**[21:36]** Now what we do is after that once you have those patches you will use this

**[21:38]** have those patches you will use this

**[21:38]** have those patches you will use this call model embedding model and it will

**[21:40]** call model embedding model and it will

**[21:40]** call model embedding model and it will generate

**[21:43]** generate

**[21:43]** generate one vector per patch.

**[21:46]** one vector per patch.

**[21:46]** one vector per patch. Okay. So in this document how many

**[21:49]** Okay. So in this document how many

**[21:49]** Okay. So in this document how many vectors we will have?

**[21:52]** vectors we will have?

**[21:52]** vectors we will have? >> 15. So now if I if my document is having

**[21:55]** >> 15. So now if I if my document is having

**[21:55]** >> 15. So now if I if my document is having 10 pages how many vectors I will have in

**[21:57]** 10 pages how many vectors I will have in

**[21:57]** 10 pages how many vectors I will have in total.

**[21:59]** total.

**[21:59]** total. >> 150. Okay. So now what we going to do is


### [22:00 - 23:00]

**[22:02]** >> 150. Okay. So now what we going to do is

**[22:02]** >> 150. Okay. So now what we going to do is we are going to see this middle part how

**[22:05]** we are going to see this middle part how

**[22:05]** we are going to see this middle part how it generates the embedding and then at

**[22:07]** it generates the embedding and then at

**[22:07]** it generates the embedding and then at later and in last section we will see

**[22:09]** later and in last section we will see

**[22:09]** later and in last section we will see that how it does the retrieval and then

**[22:11]** that how it does the retrieval and then

**[22:11]** that how it does the retrieval and then we will go to the code. Okay. Okay. So

**[22:14]** we will go to the code. Okay. Okay. So

**[22:14]** we will go to the code. Okay. Okay. So before we get into that um uh this

**[22:17]** before we get into that um uh this

**[22:17]** before we get into that um uh this embedding process let's take a detour of

**[22:20]** embedding process let's take a detour of

**[22:20]** embedding process let's take a detour of vision based language model. Uh have you

**[22:23]** vision based language model. Uh have you

**[22:23]** vision based language model. Uh have you worked on a vision based language model?

**[22:24]** worked on a vision based language model?

**[22:24]** worked on a vision based language model? Any of you? Okay. Okay. Few of you. So

**[22:29]** Any of you? Okay. Okay. Few of you. So

**[22:30]** Any of you? Okay. Okay. Few of you. So ultimately if you think about it um we

**[22:33]** ultimately if you think about it um we

**[22:33]** ultimately if you think about it um we had uh

**[22:35]** had uh

**[22:35]** had uh language models uh I'm not talking about

**[22:38]** language models uh I'm not talking about

**[22:38]** language models uh I'm not talking about uh uh large language model but text

**[22:41]** uh uh large language model but text

**[22:41]** uh uh large language model but text based models uh since we had transformer

**[22:45]** based models uh since we had transformer

**[22:45]** based models uh since we had transformer based architecture right and then at

**[22:48]** based architecture right and then at

**[22:48]** based architecture right and then at that time we also had uh models which

**[22:52]** that time we also had uh models which

**[22:52]** that time we also had uh models which can work pretty well with images which

**[22:54]** can work pretty well with images which

**[22:54]** can work pretty well with images which are based on CNN's

**[22:57]** are based on CNN's

**[22:57]** are based on CNN's now What researchers thought was uh now


### [23:00 - 24:00]

**[23:00]** now What researchers thought was uh now

**[23:00]** now What researchers thought was uh now that we have a language model why can't

**[23:02]** that we have a language model why can't

**[23:02]** that we have a language model why can't we just uh make use of that to work with

**[23:06]** we just uh make use of that to work with

**[23:06]** we just uh make use of that to work with vision it could be images or videos are

**[23:09]** vision it could be images or videos are

**[23:09]** vision it could be images or videos are nothing but uh images but but with a

**[23:11]** nothing but uh images but but with a

**[23:11]** nothing but uh images but but with a time stamp right another dimension you

**[23:13]** time stamp right another dimension you

**[23:13]** time stamp right another dimension you can think of it uh and then

**[23:18]** can think of it uh and then

**[23:18]** can think of it uh and then what people did was they took some

**[23:21]** what people did was they took some

**[23:21]** what people did was they took some vision based model and then they took

**[23:23]** vision based model and then they took

**[23:23]** vision based model and then they took some uh text based model they both are

**[23:26]** some uh text based model they both are

**[23:26]** some uh text based model they both are separate right At this point what we're

**[23:28]** separate right At this point what we're

**[23:28]** separate right At this point what we're talking about is uh before the training

**[23:32]** talking about is uh before the training

**[23:32]** talking about is uh before the training right like the these two models are

**[23:34]** right like the these two models are

**[23:34]** right like the these two models are completely separate they all have you

**[23:36]** completely separate they all have you

**[23:36]** completely separate they all have you know they they are in different space

**[23:38]** know they they are in different space

**[23:38]** know they they are in different space basically right and the idea is

**[23:42]** basically right and the idea is

**[23:42]** basically right and the idea is at the end of the day come up with a

**[23:44]** at the end of the day come up with a

**[23:44]** at the end of the day come up with a model where if you send an image of a

**[23:48]** model where if you send an image of a

**[23:48]** model where if you send an image of a dog the vector that you will get and if

**[23:51]** dog the vector that you will get and if

**[23:51]** dog the vector that you will get and if you send a text about dog the vector

**[23:54]** you send a text about dog the vector

**[23:54]** you send a text about dog the vector that you will get at the end those two

**[23:56]** that you will get at the end those two

**[23:56]** that you will get at the end those two vectors will be very close to each

**[23:57]** vectors will be very close to each

**[23:58]** vectors will be very close to each other. Initially it will not be close


### [24:00 - 25:00]

**[24:01]** other. Initially it will not be close

**[24:01]** other. Initially it will not be close because when when I say a dog is sitting

**[24:04]** because when when I say a dog is sitting

**[24:04]** because when when I say a dog is sitting on a field and if I use any text space

**[24:06]** on a field and if I use any text space

**[24:06]** on a field and if I use any text space model it will generate a vector and for

**[24:08]** model it will generate a vector and for

**[24:08]** model it will generate a vector and for the sake of simplicity simplicity let's

**[24:10]** the sake of simplicity simplicity let's

**[24:10]** the sake of simplicity simplicity let's assume the vector dimension is 10. So it

**[24:14]** assume the vector dimension is 10. So it

**[24:14]** assume the vector dimension is 10. So it will generate a array of 10 numbers.

**[24:17]** will generate a array of 10 numbers.

**[24:17]** will generate a array of 10 numbers. Similarly when you pass an image of a

**[24:19]** Similarly when you pass an image of a

**[24:19]** Similarly when you pass an image of a dog it will generate an im vector final

**[24:22]** dog it will generate an im vector final

**[24:22]** dog it will generate an im vector final vector with 10 numbers. Let's say the

**[24:24]** vector with 10 numbers. Let's say the

**[24:24]** vector with 10 numbers. Let's say the embedding vector size is 10. Now those

**[24:26]** embedding vector size is 10. Now those

**[24:26]** embedding vector size is 10. Now those 10 numbers and this 10 numbers for the

**[24:29]** 10 numbers and this 10 numbers for the

**[24:29]** 10 numbers and this 10 numbers for the text they will be anywhere in the space

**[24:31]** text they will be anywhere in the space

**[24:31]** text they will be anywhere in the space because they don't have any correlation

**[24:34]** because they don't have any correlation

**[24:34]** because they don't have any correlation at the before uh the training. Now what

**[24:37]** at the before uh the training. Now what

**[24:37]** at the before uh the training. Now what happens is

**[24:39]** happens is

**[24:39]** happens is at the time of training we take lot of

**[24:41]** at the time of training we take lot of

**[24:41]** at the time of training we take lot of samples positive samples where the text

**[24:43]** samples positive samples where the text

**[24:43]** samples positive samples where the text is there uh text is there which

**[24:46]** is there uh text is there which

**[24:46]** is there uh text is there which replicates the image and there are lot

**[24:48]** replicates the image and there are lot

**[24:48]** replicates the image and there are lot of uh negative samples where image is

**[24:51]** of uh negative samples where image is

**[24:51]** of uh negative samples where image is there but text is something random and

**[24:53]** there but text is something random and

**[24:53]** there but text is something random and the idea is the loss function that we

**[24:55]** the idea is the loss function that we

**[24:55]** the idea is the loss function that we use is if they are similar

**[24:59]** use is if they are similar

**[24:59]** use is if they are similar we want to make sure that the loss is


### [25:00 - 26:00]

**[25:02]** we want to make sure that the loss is

**[25:02]** we want to make sure that the loss is less but if they are orthogonal or very

**[25:05]** less but if they are orthogonal or very

**[25:05]** less but if they are orthogonal or very separate we will say that Okay, the loss

**[25:07]** separate we will say that Okay, the loss

**[25:07]** separate we will say that Okay, the loss is high and during this loss you know

**[25:10]** is high and during this loss you know

**[25:10]** is high and during this loss you know this training process we kind of

**[25:13]** this training process we kind of

**[25:13]** this training process we kind of optimize and at the end we we see that

**[25:16]** optimize and at the end we we see that

**[25:16]** optimize and at the end we we see that when you send an image or a text the

**[25:19]** when you send an image or a text the

**[25:19]** when you send an image or a text the embedding that we get at the end are

**[25:21]** embedding that we get at the end are

**[25:21]** embedding that we get at the end are very close to each other. Okay. So we

**[25:24]** very close to each other. Okay. So we

**[25:24]** very close to each other. Okay. So we are not going to deep dive into u vision

**[25:27]** are not going to deep dive into u vision

**[25:27]** are not going to deep dive into u vision based model but there is something

**[25:29]** based model but there is something

**[25:29]** based model but there is something called contrastive learning where if you

**[25:33]** called contrastive learning where if you

**[25:33]** called contrastive learning where if you send an image and a relevant uh positive

**[25:37]** send an image and a relevant uh positive

**[25:37]** send an image and a relevant uh positive tag and if the vectors are very uh very

**[25:41]** tag and if the vectors are very uh very

**[25:41]** tag and if the vectors are very uh very sparse like very uh uh very much apart

**[25:45]** sparse like very uh uh very much apart

**[25:45]** sparse like very uh uh very much apart from each other then the loss will be

**[25:46]** from each other then the loss will be

**[25:46]** from each other then the loss will be very high because we want these two

**[25:48]** very high because we want these two

**[25:48]** very high because we want these two vectors to be close right. So that way

**[25:51]** vectors to be close right. So that way

**[25:51]** vectors to be close right. So that way uh during the uh back uh uh back

**[25:53]** uh during the uh back uh uh back

**[25:53]** uh during the uh back uh uh back propagation we update the weights

**[25:55]** propagation we update the weights

**[25:55]** propagation we update the weights accordingly. So this is one of the

**[25:57]** accordingly. So this is one of the

**[25:57]** accordingly. So this is one of the reason if you think about it uh you

**[25:59]** reason if you think about it uh you

**[25:59]** reason if you think about it uh you might have seen in language models or


### [26:00 - 27:00]

**[26:01]** might have seen in language models or

**[26:01]** might have seen in language models or when you use any uh let's say any um

**[26:04]** when you use any uh let's say any um

**[26:04]** when you use any uh let's say any um foundational model they say that always

**[26:07]** foundational model they say that always

**[26:07]** foundational model they say that always your prompt should be

**[26:09]** your prompt should be

**[26:09]** your prompt should be uh about what you want not about what

**[26:12]** uh about what you want not about what

**[26:12]** uh about what you want not about what you don't want. Have you seen this? If

**[26:14]** you don't want. Have you seen this? If

**[26:14]** you don't want. Have you seen this? If you are into prompt engineering why they

**[26:16]** you are into prompt engineering why they

**[26:16]** you are into prompt engineering why they say this just think about it. Let's say

**[26:19]** say this just think about it. Let's say

**[26:19]** say this just think about it. Let's say if I say uh uh okay let me give you an

**[26:25]** if I say uh uh okay let me give you an

**[26:25]** if I say uh uh okay let me give you an uh analogy right if you are going for a

**[26:29]** uh analogy right if you are going for a

**[26:29]** uh analogy right if you are going for a dinner right with your wife and if you

**[26:31]** dinner right with your wife and if you

**[26:31]** dinner right with your wife and if you ask your wife what would you like to

**[26:33]** ask your wife what would you like to

**[26:33]** ask your wife what would you like to have she will say that I I I let's say

**[26:36]** have she will say that I I I let's say

**[26:36]** have she will say that I I I let's say uh I don't like this I don't like that

**[26:39]** uh I don't like this I don't like that

**[26:39]** uh I don't like this I don't like that but that was not my question my question

**[26:41]** but that was not my question my question

**[26:41]** but that was not my question my question was what you want that is always

**[26:43]** was what you want that is always

**[26:44]** was what you want that is always difficult to uh answer right people will

**[26:46]** difficult to uh answer right people will

**[26:46]** difficult to uh answer right people will say that uh

**[26:48]** say that uh

**[26:48]** say that uh Okay, would you like to have this? No, I

**[26:50]** Okay, would you like to have this? No, I

**[26:50]** Okay, would you like to have this? No, I don't like this. But when you ask that,

**[26:52]** don't like this. But when you ask that,

**[26:52]** don't like this. But when you ask that, okay, you tell me what you like, it's

**[26:54]** okay, you tell me what you like, it's

**[26:54]** okay, you tell me what you like, it's very hard. So that's why when you give a

**[26:56]** very hard. So that's why when you give a

**[26:56]** very hard. So that's why when you give a prompt that u I want a dog sitting on


### [27:00 - 28:00]

**[27:00]** prompt that u I want a dog sitting on

**[27:00]** prompt that u I want a dog sitting on this chair, it's a very nice prompt. But

**[27:02]** this chair, it's a very nice prompt. But

**[27:02]** this chair, it's a very nice prompt. But if you say that dog should not sit on

**[27:06]** if you say that dog should not sit on

**[27:06]** if you say that dog should not sit on the floor, it can generate any image

**[27:09]** the floor, it can generate any image

**[27:09]** the floor, it can generate any image because you are not saying that it

**[27:10]** because you are not saying that it

**[27:10]** because you are not saying that it should sit on a chair. It might be

**[27:12]** should sit on a chair. It might be

**[27:12]** should sit on a chair. It might be sitting on a desk or somewhere else.

**[27:14]** sitting on a desk or somewhere else.

**[27:14]** sitting on a desk or somewhere else. Right? So that is the reason we always

**[27:17]** Right? So that is the reason we always

**[27:17]** Right? So that is the reason we always say that the prompt should be uh very

**[27:20]** say that the prompt should be uh very

**[27:20]** say that the prompt should be uh very much positive what you want not the

**[27:21]** much positive what you want not the

**[27:21]** much positive what you want not the negative because uh you know data set

**[27:23]** negative because uh you know data set

**[27:23]** negative because uh you know data set doesn't have that much of negative

**[27:25]** doesn't have that much of negative

**[27:26]** doesn't have that much of negative samples. Now let's come back to call

**[27:28]** samples. Now let's come back to call

**[27:28]** samples. Now let's come back to call paraly how it works. So

**[27:31]** paraly how it works. So

**[27:31]** paraly how it works. So you give an image. So now this image is

**[27:34]** you give an image. So now this image is

**[27:34]** you give an image. So now this image is you can think of it like one of the

**[27:37]** you can think of it like one of the

**[27:37]** you can think of it like one of the patch okay it goes through uh the uh

**[27:41]** patch okay it goes through uh the uh

**[27:41]** patch okay it goes through uh the uh vision based encoder and it will

**[27:43]** vision based encoder and it will

**[27:43]** vision based encoder and it will generate an uh embedding and then we

**[27:45]** generate an uh embedding and then we

**[27:45]** generate an uh embedding and then we have a linear projection and the reason

**[27:47]** have a linear projection and the reason

**[27:48]** have a linear projection and the reason that we have the linear projection is

**[27:50]** that we have the linear projection is

**[27:50]** that we have the linear projection is because at the end of the day uh when

**[27:52]** because at the end of the day uh when

**[27:52]** because at the end of the day uh when you ask a question that will also be

**[27:55]** you ask a question that will also be

**[27:55]** you ask a question that will also be generating some vector we want to make

**[27:57]** generating some vector we want to make

**[27:57]** generating some vector we want to make sure that these vectors are compatible

**[27:59]** sure that these vectors are compatible

**[27:59]** sure that these vectors are compatible to each other they are of same size and


### [28:00 - 29:00]

**[28:01]** to each other they are of same size and

**[28:01]** to each other they are of same size and that's why we have added added a new

**[28:03]** that's why we have added added a new

**[28:03]** that's why we have added added a new projection layer. You can simply think

**[28:05]** projection layer. You can simply think

**[28:05]** projection layer. You can simply think of it as a fully connected layer and

**[28:09]** of it as a fully connected layer and

**[28:09]** of it as a fully connected layer and ultimately you will have a standard

**[28:11]** ultimately you will have a standard

**[28:11]** ultimately you will have a standard transformer and then you will get the

**[28:13]** transformer and then you will get the

**[28:13]** transformer and then you will get the output token. Okay. So

**[28:16]** output token. Okay. So

**[28:16]** output token. Okay. So now

**[28:19]** now

**[28:19]** now if you think about

**[28:28]** me just scroll down. Yeah. So if you

**[28:28]** me just scroll down. Yeah. So if you think about call pal when you give an

**[28:31]** think about call pal when you give an

**[28:31]** think about call pal when you give an image

**[28:33]** image

**[28:33]** image it will have let's say in this case

**[28:35]** it will have let's say in this case

**[28:35]** it will have let's say in this case there are 15 uh patches just think of

**[28:38]** there are 15 uh patches just think of

**[28:38]** there are 15 uh patches just think of this patch okay this patch will go

**[28:41]** this patch okay this patch will go

**[28:41]** this patch okay this patch will go through this it will generate an uh

**[28:44]** through this it will generate an uh

**[28:44]** through this it will generate an uh vector and this will be the final

**[28:47]** vector and this will be the final

**[28:47]** vector and this will be the final representation of the first patch.

**[28:49]** representation of the first patch.

**[28:49]** representation of the first patch. Similarly when you give the whole image

**[28:51]** Similarly when you give the whole image

**[28:51]** Similarly when you give the whole image you will not give the uh you know single

**[28:54]** you will not give the uh you know single

**[28:54]** you will not give the uh you know single patch uh in the batch you will give give

**[28:57]** patch uh in the batch you will give give

**[28:57]** patch uh in the batch you will give give one full image or let's say page number


### [29:00 - 30:00]

**[29:00]** one full image or let's say page number

**[29:00]** one full image or let's say page number one of the document this model will do

**[29:02]** one of the document this model will do

**[29:02]** one of the document this model will do all that patching and it will finally

**[29:05]** all that patching and it will finally

**[29:05]** all that patching and it will finally generate one embedding vector. Now at

**[29:09]** generate one embedding vector. Now at

**[29:09]** generate one embedding vector. Now at the time of

**[29:11]** the time of

**[29:11]** the time of and if you if you see here in this case

**[29:14]** and if you if you see here in this case

**[29:14]** and if you if you see here in this case this is grayed out because now we are

**[29:17]** this is grayed out because now we are

**[29:17]** this is grayed out because now we are talking about after training once that

**[29:18]** talking about after training once that

**[29:18]** talking about after training once that model is trained after training you will

**[29:21]** model is trained after training you will

**[29:21]** model is trained after training you will create the embeddings of your document.

**[29:23]** create the embeddings of your document.

**[29:24]** create the embeddings of your document. So while you are creating the embeddings

**[29:25]** So while you are creating the embeddings

**[29:25]** So while you are creating the embeddings there is no question here right. So it

**[29:28]** there is no question here right. So it

**[29:28]** there is no question here right. So it will just use this path. Now once those

**[29:31]** will just use this path. Now once those

**[29:31]** will just use this path. Now once those embeddings are done like once you get

**[29:33]** embeddings are done like once you get

**[29:33]** embeddings are done like once you get all these final vectors for your entire

**[29:35]** all these final vectors for your entire

**[29:36]** all these final vectors for your entire document

**[29:43]** in the query time you will just use your

**[29:43]** in the query time you will just use your text based query. So call pal doesn't

**[29:46]** text based query. So call pal doesn't

**[29:46]** text based query. So call pal doesn't say that you can query with your as an

**[29:49]** say that you can query with your as an

**[29:49]** say that you can query with your as an image like in chat GPT or any GPD based

**[29:52]** image like in chat GPT or any GPD based

**[29:52]** image like in chat GPT or any GPD based model you just upload an image. We are

**[29:54]** model you just upload an image. We are

**[29:54]** model you just upload an image. We are so lazy we don't even ask the question

**[29:55]** so lazy we don't even ask the question

**[29:55]** so lazy we don't even ask the question these days right we just upload the

**[29:57]** these days right we just upload the

**[29:57]** these days right we just upload the image and you know model just generates

**[29:58]** image and you know model just generates

**[29:58]** image and you know model just generates something. So here the question should


### [30:00 - 31:00]

**[30:00]** something. So here the question should

**[30:00]** something. So here the question should be always in text that's the

**[30:02]** be always in text that's the

**[30:02]** be always in text that's the prerequisite for this model and then

**[30:05]** prerequisite for this model and then

**[30:06]** prerequisite for this model and then this goes through the same uh model and

**[30:08]** this goes through the same uh model and

**[30:08]** this goes through the same uh model and then it finally gives you an response.

**[30:11]** then it finally gives you an response.

**[30:11]** then it finally gives you an response. Now this response this vector you will

**[30:13]** Now this response this vector you will

**[30:13]** Now this response this vector you will do a semantic search with the vectors

**[30:16]** do a semantic search with the vectors

**[30:16]** do a semantic search with the vectors that you have stored in your vector

**[30:18]** that you have stored in your vector

**[30:18]** that you have stored in your vector database using those uh image patches

**[30:22]** database using those uh image patches

**[30:22]** database using those uh image patches with me so far? Yes. Okay. So if you

**[30:26]** with me so far? Yes. Okay. So if you

**[30:26]** with me so far? Yes. Okay. So if you think about it uh

**[30:29]** think about it uh

**[30:29]** think about it uh both for query as well as uh your

**[30:31]** both for query as well as uh your

**[30:32]** both for query as well as uh your embedding there is a certain amount of

**[30:35]** embedding there is a certain amount of

**[30:35]** embedding there is a certain amount of uh uh pre-processing that is needed

**[30:37]** uh uh pre-processing that is needed

**[30:37]** uh uh pre-processing that is needed because uh your images can be of

**[30:40]** because uh your images can be of

**[30:40]** because uh your images can be of different size right so let's say you

**[30:42]** different size right so let's say you

**[30:42]** different size right so let's say you have an a PDF document u and

**[30:46]** have an a PDF document u and

**[30:46]** have an a PDF document u and the tool that you use to convert that

**[30:48]** the tool that you use to convert that

**[30:48]** the tool that you use to convert that into an image uh it created an image of

**[30:51]** into an image uh it created an image of

**[30:51]** into an image uh it created an image of 800 by 800 but let's say somebody else

**[30:53]** 800 by 800 but let's say somebody else

**[30:53]** 800 by 800 but let's say somebody else have used another technique and the

**[30:55]** have used another technique and the

**[30:55]** have used another technique and the image was of 50 + 50. So we need to make

**[30:58]** image was of 50 + 50. So we need to make

**[30:58]** image was of 50 + 50. So we need to make sure that the images are of standard


### [31:00 - 32:00]

**[31:00]** sure that the images are of standard

**[31:00]** sure that the images are of standard size, right? So that's why when we look

**[31:02]** size, right? So that's why when we look

**[31:02]** size, right? So that's why when we look into the code next, you will see that

**[31:05]** into the code next, you will see that

**[31:05]** into the code next, you will see that always before it actually generates the

**[31:07]** always before it actually generates the

**[31:08]** always before it actually generates the embedding, there is a pre-processing uh

**[31:09]** embedding, there is a pre-processing uh

**[31:10]** embedding, there is a pre-processing uh that we do. Okay. So let's uh go to the

**[31:14]** that we do. Okay. So let's uh go to the

**[31:14]** that we do. Okay. So let's uh go to the code and see that. But before that let's

**[31:17]** code and see that. But before that let's

**[31:17]** code and see that. But before that let's uh let's share I mean let's talk about

**[31:21]** uh let's share I mean let's talk about

**[31:21]** uh let's share I mean let's talk about how it generates uh the similar chunks.

**[31:25]** how it generates uh the similar chunks.

**[31:25]** how it generates uh the similar chunks. So this is the most important part of

**[31:27]** So this is the most important part of

**[31:27]** So this is the most important part of call pali. Okay. Now imagine that

**[31:31]** call pali. Okay. Now imagine that

**[31:31]** call pali. Okay. Now imagine that your page now just consider page number

**[31:34]** your page now just consider page number

**[31:34]** your page now just consider page number one of your document and the page

**[31:38]** one of your document and the page

**[31:38]** one of your document and the page and the patch size that you use is let's

**[31:40]** and the patch size that you use is let's

**[31:40]** and the patch size that you use is let's say 2 +2 that is total four patches.

**[31:43]** say 2 +2 that is total four patches.

**[31:43]** say 2 +2 that is total four patches. Okay. Now let's say this is page number

**[31:45]** Okay. Now let's say this is page number

**[31:45]** Okay. Now let's say this is page number one and this is the embedding of your f

**[31:51]** one and this is the embedding of your f

**[31:51]** one and this is the embedding of your f uh first patch. This is the embedding of

**[31:53]** uh first patch. This is the embedding of

**[31:54]** uh first patch. This is the embedding of the second patch. This is the embedding

**[31:55]** the second patch. This is the embedding

**[31:55]** the second patch. This is the embedding of third patch. This is the embedding of

**[31:56]** of third patch. This is the embedding of

**[31:56]** of third patch. This is the embedding of the fourth patch. Okay.


### [32:00 - 33:00]

**[32:00]** the fourth patch. Okay.

**[32:00]** the fourth patch. Okay. And you ask some question. Let's say uh

**[32:05]** And you ask some question. Let's say uh

**[32:05]** And you ask some question. Let's say uh what is AI? Just for the sake of

**[32:07]** what is AI? Just for the sake of

**[32:07]** what is AI? Just for the sake of simplicity what is AI? And you have used

**[32:10]** simplicity what is AI? And you have used

**[32:10]** simplicity what is AI? And you have used through uh it went through the tokenizer

**[32:11]** through uh it went through the tokenizer

**[32:12]** through uh it went through the tokenizer and it generated three embedding vectors

**[32:14]** and it generated three embedding vectors

**[32:14]** and it generated three embedding vectors right three tokens basically. So now

**[32:17]** right three tokens basically. So now

**[32:17]** right three tokens basically. So now what we do is we do a dot product

**[32:21]** what we do is we do a dot product

**[32:21]** what we do is we do a dot product between each vector and each vector of

**[32:24]** between each vector and each vector of

**[32:24]** between each vector and each vector of all the patches.

**[32:27]** all the patches.

**[32:27]** all the patches. Okay.

**[32:28]** Okay.

**[32:28]** Okay. And then

**[32:30]** And then

**[32:30]** And then for every row we try to find which is

**[32:33]** for every row we try to find which is

**[32:33]** for every row we try to find which is the maximum number. What this number

**[32:36]** the maximum number. What this number

**[32:36]** the maximum number. What this number signifies? This 89 signifies 89

**[32:39]** signifies? This 89 signifies 89

**[32:39]** signifies? This 89 signifies 89 signifies that the first part of your

**[32:42]** signifies that the first part of your

**[32:42]** signifies that the first part of your question has the maximum similarity with

**[32:45]** question has the maximum similarity with

**[32:45]** question has the maximum similarity with the second patch of the image.

**[32:49]** the second patch of the image.

**[32:49]** the second patch of the image. Right? Similarly, if this is 97, that

**[32:52]** Right? Similarly, if this is 97, that

**[32:52]** Right? Similarly, if this is 97, that means the second part of your question

**[32:55]** means the second part of your question

**[32:55]** means the second part of your question has the maximum similarity with the

**[32:58]** has the maximum similarity with the

**[32:58]** has the maximum similarity with the third patch of your image.


### [33:00 - 34:00]

**[33:01]** third patch of your image.

**[33:01]** third patch of your image. Right?

**[33:02]** Right?

**[33:02]** Right? And at the end what we do is we just

**[33:04]** And at the end what we do is we just

**[33:04]** And at the end what we do is we just take the addition I mean we just take a

**[33:07]** take the addition I mean we just take a

**[33:07]** take the addition I mean we just take a sum the maximum numbers of each rows and

**[33:10]** sum the maximum numbers of each rows and

**[33:10]** sum the maximum numbers of each rows and if let's say that is 2.58 that means

**[33:14]** if let's say that is 2.58 that means

**[33:14]** if let's say that is 2.58 that means this query has a score of 2.58 for page

**[33:18]** this query has a score of 2.58 for page

**[33:18]** this query has a score of 2.58 for page number one. Similarly we will do it for

**[33:21]** number one. Similarly we will do it for

**[33:21]** number one. Similarly we will do it for all the pages and then in rag what we do

**[33:24]** all the pages and then in rag what we do

**[33:24]** all the pages and then in rag what we do at the end when we do a semantic search

**[33:26]** at the end when we do a semantic search

**[33:26]** at the end when we do a semantic search we say top five chunks or top 10 chunks.

**[33:29]** we say top five chunks or top 10 chunks.

**[33:29]** we say top five chunks or top 10 chunks. So in this case chunk is nothing but

**[33:31]** So in this case chunk is nothing but

**[33:31]** So in this case chunk is nothing but pages. So if I say top five then in that

**[33:34]** pages. So if I say top five then in that

**[33:34]** pages. So if I say top five then in that case it will show us the top five pages

**[33:37]** case it will show us the top five pages

**[33:37]** case it will show us the top five pages based on this score.

**[33:40]** based on this score.

**[33:40]** based on this score. Getting it. So this is the most

**[33:42]** Getting it. So this is the most

**[33:42]** Getting it. So this is the most important thing. So this is called late

**[33:44]** important thing. So this is called late

**[33:44]** important thing. So this is called late interaction. Have you heard of late

**[33:46]** interaction. Have you heard of late

**[33:46]** interaction. Have you heard of late interaction embeddings all that? And the

**[33:49]** interaction embeddings all that? And the

**[33:49]** interaction embeddings all that? And the reason that we say late interaction is

**[33:50]** reason that we say late interaction is

**[33:50]** reason that we say late interaction is because these token embeddings are

**[33:53]** because these token embeddings are

**[33:53]** because these token embeddings are already stored. We have already done

**[33:55]** already stored. We have already done

**[33:55]** already stored. We have already done that. It's there in your vector

**[33:56]** that. It's there in your vector

**[33:56]** that. It's there in your vector database. All we have to do is we need

**[33:58]** database. All we have to do is we need

**[33:58]** database. All we have to do is we need to just do the dot product and then use


### [34:00 - 35:00]

**[34:00]** to just do the dot product and then use

**[34:00]** to just do the dot product and then use this metrics to generate the top five or

**[34:03]** this metrics to generate the top five or

**[34:03]** this metrics to generate the top five or top three uh pages. Okay.

**[34:07]** top three uh pages. Okay.

**[34:07]** top three uh pages. Okay. Uh with me so far? Yes. Okay. Now this

**[34:12]** Uh with me so far? Yes. Okay. Now this

**[34:12]** Uh with me so far? Yes. Okay. Now this functionality is not supported in all

**[34:14]** functionality is not supported in all

**[34:14]** functionality is not supported in all the all the vector databases. We are

**[34:16]** the all the vector databases. We are

**[34:16]** the all the vector databases. We are going to use one of the vector database

**[34:18]** going to use one of the vector database

**[34:18]** going to use one of the vector database called quadrant. Have you heard of that?

**[34:21]** called quadrant. Have you heard of that?

**[34:21]** called quadrant. Have you heard of that? But there are few other databases. I

**[34:22]** But there are few other databases. I

**[34:22]** But there are few other databases. I have not done enough research which are

**[34:24]** have not done enough research which are

**[34:24]** have not done enough research which are the databases that it supports. uh but

**[34:27]** the databases that it supports. uh but

**[34:27]** the databases that it supports. uh but this u maxim calculation is not

**[34:29]** this u maxim calculation is not

**[34:30]** this u maxim calculation is not supported by all the database okay there

**[34:32]** supported by all the database okay there

**[34:32]** supported by all the database okay there are some open source contribution that

**[34:33]** are some open source contribution that

**[34:33]** are some open source contribution that we have for few of the vector databases

**[34:35]** we have for few of the vector databases

**[34:35]** we have for few of the vector databases I I I I tried with open search u it did

**[34:39]** I I I I tried with open search u it did

**[34:39]** I I I I tried with open search u it did not have but I think there is a

**[34:40]** not have but I think there is a

**[34:40]** not have but I think there is a extension uh which you can use to make

**[34:43]** extension uh which you can use to make

**[34:43]** extension uh which you can use to make this functionality okay so now we are

**[34:46]** this functionality okay so now we are

**[34:46]** this functionality okay so now we are going to get into

**[34:48]** going to get into

**[34:48]** going to get into uh the demo so just like what I said

**[34:51]** uh the demo so just like what I said

**[34:51]** uh the demo so just like what I said once you have those uh scores like in

**[34:55]** once you have those uh scores like in

**[34:55]** once you have those uh scores like in this case 2.58 uh like this you will

**[34:57]** this case 2.58 uh like this you will

**[34:57]** this case 2.58 uh like this you will have for all the pages in your document


### [35:00 - 36:00]

**[35:00]** have for all the pages in your document

**[35:00]** have for all the pages in your document and then at the end you can pick the top

**[35:02]** and then at the end you can pick the top

**[35:02]** and then at the end you can pick the top three or top four pages of your choice.

**[35:05]** three or top four pages of your choice.

**[35:05]** three or top four pages of your choice. Okay.

**[35:06]** Okay.

**[35:06]** Okay. So now see this so far we are not

**[35:09]** So now see this so far we are not

**[35:09]** So now see this so far we are not talking about agents. Okay. Because

**[35:10]** talking about agents. Okay. Because

**[35:10]** talking about agents. Okay. Because that's a very simple task. Uh we will

**[35:12]** that's a very simple task. Uh we will

**[35:12]** that's a very simple task. Uh we will just wrap this with an agent at later

**[35:14]** just wrap this with an agent at later

**[35:14]** just wrap this with an agent at later point in time.

**[35:16]** point in time.

**[35:16]** point in time. All right. So let's try to do this.

**[35:20]** All right. So let's try to do this.

**[35:20]** All right. So let's try to do this. Okay. So this is an uh uh I I'll just

**[35:23]** Okay. So this is an uh uh I I'll just

**[35:23]** Okay. So this is an uh uh I I'll just come to this uh image later on. So now

**[35:25]** come to this uh image later on. So now

**[35:25]** come to this uh image later on. So now let me just increase uh the font. Can

**[35:29]** let me just increase uh the font. Can

**[35:29]** let me just increase uh the font. Can you see this? Yeah. Okay. You don't have

**[35:31]** you see this? Yeah. Okay. You don't have

**[35:31]** you see this? Yeah. Okay. You don't have to read all that but just uh you should

**[35:33]** to read all that but just uh you should

**[35:33]** to read all that but just uh you should have an idea what we are doing. So first

**[35:36]** have an idea what we are doing. So first

**[35:36]** have an idea what we are doing. So first we are just importing few of the

**[35:37]** we are just importing few of the

**[35:37]** we are just importing few of the libraries. Uh I have no idea what I have

**[35:39]** libraries. Uh I have no idea what I have

**[35:39]** libraries. Uh I have no idea what I have importing but uh there are few right. So

**[35:41]** importing but uh there are few right. So

**[35:41]** importing but uh there are few right. So I think it's uh where is the call pal?

**[35:43]** I think it's uh where is the call pal?

**[35:43]** I think it's uh where is the call pal? Yeah. So this is the call pali model

**[35:44]** Yeah. So this is the call pali model

**[35:44]** Yeah. So this is the call pali model that we have. Okay. And this is the

**[35:48]** that we have. Okay. And this is the

**[35:48]** that we have. Okay. And this is the quadrant database and this quadrant

**[35:50]** quadrant database and this quadrant

**[35:50]** quadrant database and this quadrant database we are going to run locally in

**[35:52]** database we are going to run locally in

**[35:52]** database we are going to run locally in a docker container. Okay. So if you are

**[35:55]** a docker container. Okay. So if you are

**[35:56]** a docker container. Okay. So if you are planning to run this uh make sure that

**[35:57]** planning to run this uh make sure that

**[35:57]** planning to run this uh make sure that you have docker installed in your uh in


### [36:00 - 37:00]

**[36:00]** you have docker installed in your uh in

**[36:00]** you have docker installed in your uh in your laptop. Okay. I I I think the

**[36:02]** your laptop. Okay. I I I think the

**[36:02]** your laptop. Okay. I I I think the readme have all the information.

**[36:05]** readme have all the information.

**[36:05]** readme have all the information. Okay. Uh so first we need some

**[36:10]** Okay. Uh so first we need some

**[36:10]** Okay. Uh so first we need some data. So I have used one data set

**[36:14]** data. So I have used one data set

**[36:14]** data. So I have used one data set basically it's a small textbook and if

**[36:17]** basically it's a small textbook and if

**[36:17]** basically it's a small textbook and if you see this textbook uh this is a

**[36:18]** you see this textbook uh this is a

**[36:18]** you see this textbook uh this is a science textbook

**[36:20]** science textbook

**[36:20]** science textbook uh chapter number 13. So we have let's

**[36:24]** uh chapter number 13. So we have let's

**[36:24]** uh chapter number 13. So we have let's say see one of the thing that uh which

**[36:27]** say see one of the thing that uh which

**[36:27]** say see one of the thing that uh which is interesting here is if you see this

**[36:29]** is interesting here is if you see this

**[36:29]** is interesting here is if you see this image there is no text here right so

**[36:31]** image there is no text here right so

**[36:31]** image there is no text here right so it's if you ask anything about this

**[36:33]** it's if you ask anything about this

**[36:33]** it's if you ask anything about this image uh and use a traditional technique

**[36:36]** image uh and use a traditional technique

**[36:36]** image uh and use a traditional technique it might not answer properly uh like

**[36:39]** it might not answer properly uh like

**[36:39]** it might not answer properly uh like this this is also another image along

**[36:41]** this this is also another image along

**[36:41]** this this is also another image along with some text and uh you know you can

**[36:44]** with some text and uh you know you can

**[36:44]** with some text and uh you know you can pick any data set of your choice but uh

**[36:47]** pick any data set of your choice but uh

**[36:47]** pick any data set of your choice but uh this is the data set that I have okay

**[36:49]** this is the data set that I have okay

**[36:50]** this is the data set that I have okay and feel free to use any data set of

**[36:51]** and feel free to use any data set of

**[36:51]** and feel free to use any data set of your choice but uh for the purpose of

**[36:53]** your choice but uh for the purpose of

**[36:53]** your choice but uh for the purpose of this uh demo you may like to download

**[36:56]** this uh demo you may like to download

**[36:56]** this uh demo you may like to download one of these uh PDF from this URL and

**[36:59]** one of these uh PDF from this URL and

**[36:59]** one of these uh PDF from this URL and play around with this and then you need


### [37:00 - 38:00]

**[37:01]** play around with this and then you need

**[37:01]** play around with this and then you need to have a hugging phase uh uh uh token

**[37:06]** to have a hugging phase uh uh uh token

**[37:06]** to have a hugging phase uh uh uh token uh because we are going to download this

**[37:09]** uh because we are going to download this

**[37:09]** uh because we are going to download this model from hugging phase right so you

**[37:11]** model from hugging phase right so you

**[37:11]** model from hugging phase right so you should not do this right so this is uh

**[37:14]** should not do this right so this is uh

**[37:14]** should not do this right so this is uh you know I was just trying this because

**[37:16]** you know I was just trying this because

**[37:16]** you know I was just trying this because without creating av file but you should

**[37:19]** without creating av file but you should

**[37:19]** without creating av file but you should have an env file inside that your token

**[37:22]** have an env file inside that your token

**[37:22]** have an env file inside that your token should exit exist. Okay, so this is uh a

**[37:25]** should exit exist. Okay, so this is uh a

**[37:25]** should exit exist. Okay, so this is uh a token like this is not my token. If you

**[37:27]** token like this is not my token. If you

**[37:27]** token like this is not my token. If you see this uh this is just a dummy one,

**[37:30]** see this uh this is just a dummy one,

**[37:30]** see this uh this is just a dummy one, right? This is not my token. Okay, so

**[37:32]** right? This is not my token. Okay, so

**[37:32]** right? This is not my token. Okay, so it's but uh this is this is just uh the

**[37:37]** it's but uh this is this is just uh the

**[37:37]** it's but uh this is this is just uh the the hugging face token that you should

**[37:39]** the hugging face token that you should

**[37:39]** the hugging face token that you should have. So here we are just loading and

**[37:42]** have. So here we are just loading and

**[37:42]** have. So here we are just loading and logging into our hugging face account.

**[37:45]** logging into our hugging face account.

**[37:45]** logging into our hugging face account. And next we are trying to check whether

**[37:50]** And next we are trying to check whether

**[37:50]** And next we are trying to check whether we have a CPU, GPU or uh MPS. In this

**[37:54]** we have a CPU, GPU or uh MPS. In this

**[37:54]** we have a CPU, GPU or uh MPS. In this case it's a MacBook so I'm just using

**[37:56]** case it's a MacBook so I'm just using

**[37:56]** case it's a MacBook so I'm just using MPS here uh as a device. Since it's a

**[37:59]** MPS here uh as a device. Since it's a


### [38:00 - 39:00]

**[38:00]** MPS here uh as a device. Since it's a vision based model it's better to run it

**[38:01]** vision based model it's better to run it

**[38:02]** vision based model it's better to run it on a GPU. It will be faster but you can

**[38:03]** on a GPU. It will be faster but you can

**[38:03]** on a GPU. It will be faster but you can very well run it on CPU. That's fine.

**[38:06]** very well run it on CPU. That's fine.

**[38:06]** very well run it on CPU. That's fine. I'll tell you uh you know you should be

**[38:09]** I'll tell you uh you know you should be

**[38:09]** I'll tell you uh you know you should be a little cautious about this if you're

**[38:10]** a little cautious about this if you're

**[38:10]** a little cautious about this if you're running with a within your laptop uh on

**[38:13]** running with a within your laptop uh on

**[38:13]** running with a within your laptop uh on CPU.

**[38:14]** CPU.

**[38:14]** CPU. uh

**[38:16]** uh

**[38:16]** uh if it's a office laptop no one cares but

**[38:18]** if it's a office laptop no one cares but

**[38:18]** if it's a office laptop no one cares but if it's your personal laptop make sure

**[38:19]** if it's your personal laptop make sure

**[38:19]** if it's your personal laptop make sure that the batch size is very small

**[38:21]** that the batch size is very small

**[38:21]** that the batch size is very small otherwise it will it will crash in fact

**[38:24]** otherwise it will it will crash in fact

**[38:24]** otherwise it will it will crash in fact I when I first ran this I did not check

**[38:27]** I when I first ran this I did not check

**[38:27]** I when I first ran this I did not check uh the processing time and all that it

**[38:29]** uh the processing time and all that it

**[38:29]** uh the processing time and all that it just uh went on u you know crashing and

**[38:33]** just uh went on u you know crashing and

**[38:33]** just uh went on u you know crashing and it uh rebooted my laptop

**[38:36]** it uh rebooted my laptop

**[38:36]** it uh rebooted my laptop uh and uh I I did not even read through

**[38:38]** uh and uh I I did not even read through

**[38:38]** uh and uh I I did not even read through all this and I ra the IT ticket and I

**[38:41]** all this and I ra the IT ticket and I

**[38:41]** all this and I ra the IT ticket and I actually got a laptop new laptop uh So

**[38:44]** actually got a laptop new laptop uh So

**[38:44]** actually got a laptop new laptop uh So but it was my fault here. So they

**[38:46]** but it was my fault here. So they

**[38:46]** but it was my fault here. So they thought that my work my work needs a

**[38:48]** thought that my work my work needs a

**[38:48]** thought that my work my work needs a laptop with more memory. So so if you

**[38:52]** laptop with more memory. So so if you

**[38:52]** laptop with more memory. So so if you are finding out tricks to get a new

**[38:53]** are finding out tricks to get a new

**[38:53]** are finding out tricks to get a new laptop from a company. So this is the

**[38:55]** laptop from a company. So this is the

**[38:55]** laptop from a company. So this is the cell. So okay uh you can try that. I


### [39:00 - 40:00]

**[39:00]** cell. So okay uh you can try that. I

**[39:00]** cell. So okay uh you can try that. I I'll tell you what you have to change to

**[39:03]** I'll tell you what you have to change to

**[39:03]** I'll tell you what you have to change to get a new laptop. So just increase the

**[39:05]** get a new laptop. So just increase the

**[39:05]** get a new laptop. So just increase the batch size to batch size to 12. It

**[39:07]** batch size to batch size to 12. It

**[39:07]** batch size to batch size to 12. It should work fine. Yeah. Yeah. Okay. So

**[39:13]** should work fine. Yeah. Yeah. Okay. So

**[39:13]** should work fine. Yeah. Yeah. Okay. So this is the model that we are going to

**[39:14]** this is the model that we are going to

**[39:14]** this is the model that we are going to use. It's a call pali uh version 1.3.

**[39:18]** use. It's a call pali uh version 1.3.

**[39:18]** use. It's a call pali uh version 1.3. There might be our new version but just

**[39:20]** There might be our new version but just

**[39:20]** There might be our new version but just have a look. I I checked last month it

**[39:22]** have a look. I I checked last month it

**[39:22]** have a look. I I checked last month it was still 1.3.

**[39:24]** was still 1.3.

**[39:24]** was still 1.3. And I'm having a model and a

**[39:27]** And I'm having a model and a

**[39:27]** And I'm having a model and a pre-processor. Remember that we

**[39:29]** pre-processor. Remember that we

**[39:29]** pre-processor. Remember that we discussed that we need to have a

**[39:30]** discussed that we need to have a

**[39:30]** discussed that we need to have a pre-processor first. Uh we will process

**[39:32]** pre-processor first. Uh we will process

**[39:32]** pre-processor first. Uh we will process our data and then we will use the model

**[39:34]** our data and then we will use the model

**[39:34]** our data and then we will use the model to generate the embeddings. Okay. the

**[39:36]** to generate the embeddings. Okay. the

**[39:36]** to generate the embeddings. Okay. the same model but there is a pre-processor

**[39:39]** same model but there is a pre-processor

**[39:39]** same model but there is a pre-processor and the model and these all are coming

**[39:41]** and the model and these all are coming

**[39:41]** and the model and these all are coming from hugging face and we are using a

**[39:44]** from hugging face and we are using a

**[39:44]** from hugging face and we are using a cache directory so that we can load this

**[39:46]** cache directory so that we can load this

**[39:46]** cache directory so that we can load this model locally in our uh local directory

**[39:49]** model locally in our uh local directory

**[39:49]** model locally in our uh local directory uh so that every time you run it doesn't

**[39:51]** uh so that every time you run it doesn't

**[39:51]** uh so that every time you run it doesn't download from the internet okay

**[39:55]** download from the internet okay

**[39:55]** download from the internet okay and once that is done uh you have to

**[39:57]** and once that is done uh you have to

**[39:57]** and once that is done uh you have to have a vector database so if you have a


### [40:00 - 41:00]

**[40:00]** have a vector database so if you have a

**[40:00]** have a vector database so if you have a docker installed you can just copy and

**[40:03]** docker installed you can just copy and

**[40:03]** docker installed you can just copy and paste it it is nothing but it just

**[40:05]** paste it it is nothing but it just

**[40:05]** paste it it is nothing but it just created a a container with a port

**[40:07]** created a a container with a port

**[40:07]** created a a container with a port forwarding and uh there is a folder

**[40:10]** forwarding and uh there is a folder

**[40:10]** forwarding and uh there is a folder which gets created locally uh as a

**[40:13]** which gets created locally uh as a

**[40:13]** which gets created locally uh as a storage. So all your vectors will be

**[40:15]** storage. So all your vectors will be

**[40:15]** storage. So all your vectors will be stored locally in your laptop. That's

**[40:16]** stored locally in your laptop. That's

**[40:16]** stored locally in your laptop. That's all. And if you click on this dashboard,

**[40:21]** all. And if you click on this dashboard,

**[40:21]** all. And if you click on this dashboard, you should be able to see uh that uh UI

**[40:25]** you should be able to see uh that uh UI

**[40:25]** you should be able to see uh that uh UI of that. And if you come to console uh

**[40:28]** of that. And if you come to console uh

**[40:28]** of that. And if you come to console uh sorry um here collection initially you

**[40:31]** sorry um here collection initially you

**[40:31]** sorry um here collection initially you since I have executed that code that's

**[40:33]** since I have executed that code that's

**[40:33]** since I have executed that code that's why we see this but you should not see

**[40:35]** why we see this but you should not see

**[40:35]** why we see this but you should not see anything here and as you run through the

**[40:38]** anything here and as you run through the

**[40:38]** anything here and as you run through the notebook you will see the uh collection

**[40:41]** notebook you will see the uh collection

**[40:41]** notebook you will see the uh collection here. So collection is how many of you

**[40:44]** here. So collection is how many of you

**[40:44]** here. So collection is how many of you are aware of databases?

**[40:46]** are aware of databases?

**[40:46]** are aware of databases? Okay. Okay, many of you I have no idea

**[40:49]** Okay. Okay, many of you I have no idea

**[40:49]** Okay. Okay, many of you I have no idea what what it is but I just asked. So the

**[40:51]** what what it is but I just asked. So the

**[40:51]** what what it is but I just asked. So the collection is basically you can think of

**[40:53]** collection is basically you can think of

**[40:53]** collection is basically you can think of it like a database and where you will

**[40:55]** it like a database and where you will

**[40:55]** it like a database and where you will just store all the uh schema and all

**[40:58]** just store all the uh schema and all

**[40:58]** just store all the uh schema and all that. So I'm creating a quadrant client


### [41:00 - 42:00]

**[41:03]** that. So I'm creating a quadrant client

**[41:03]** that. So I'm creating a quadrant client and this is something that I imported

**[41:06]** and this is something that I imported

**[41:06]** and this is something that I imported earlier and this is the local host and

**[41:08]** earlier and this is the local host and

**[41:08]** earlier and this is the local host and port number this and this just we are

**[41:10]** port number this and this just we are

**[41:10]** port number this and this just we are just creating the setup right. So now we

**[41:13]** just creating the setup right. So now we

**[41:13]** just creating the setup right. So now we have a vector database and we have the

**[41:16]** have a vector database and we have the

**[41:16]** have a vector database and we have the data. So and we have also uh downloaded

**[41:19]** data. So and we have also uh downloaded

**[41:19]** data. So and we have also uh downloaded the model. So now the second thing that

**[41:22]** the model. So now the second thing that

**[41:22]** the model. So now the second thing that we need to do is we need to create a

**[41:24]** we need to do is we need to create a

**[41:24]** we need to do is we need to create a collection right and if you see this uh

**[41:27]** collection right and if you see this uh

**[41:27]** collection right and if you see this uh we have a collection called u class 10

**[41:29]** we have a collection called u class 10

**[41:29]** we have a collection called u class 10 science. Uh so you can give any

**[41:33]** science. Uh so you can give any

**[41:33]** science. Uh so you can give any collection name. Here we are mentioning

**[41:36]** collection name. Here we are mentioning

**[41:36]** collection name. Here we are mentioning what should be the vector size right? So

**[41:39]** what should be the vector size right? So

**[41:39]** what should be the vector size right? So uh this is the uh embedding length. So

**[41:42]** uh this is the uh embedding length. So

**[41:42]** uh this is the uh embedding length. So here it is 128 and in this in this code

**[41:47]** here it is 128 and in this in this code

**[41:47]** here it is 128 and in this in this code what we essentially doing is if there is

**[41:50]** what we essentially doing is if there is

**[41:50]** what we essentially doing is if there is a collection already exists it will not

**[41:51]** a collection already exists it will not

**[41:51]** a collection already exists it will not create any new collection or else it

**[41:53]** create any new collection or else it

**[41:53]** create any new collection or else it will create a new connection. Yeah you

**[41:55]** will create a new connection. Yeah you

**[41:55]** will create a new connection. Yeah you have a question.

**[41:56]** have a question.

**[41:56]** have a question. >> Yeah.


### [42:00 - 43:00]

**[42:05]** >> Yeah. So there is a

**[42:05]** >> Yeah. So there is a let me ask you this. What do you feel if

**[42:07]** let me ask you this. What do you feel if

**[42:07]** let me ask you this. What do you feel if I increase the embedding size from 128

**[42:10]** I increase the embedding size from 128

**[42:10]** I increase the embedding size from 128 to 256?

**[42:17]** What do you feel? H how it would behave?

**[42:17]** What do you feel? H how it would behave? Just a guess.

**[42:32]** >> Okay. Okay. Let let me let me give you

**[42:32]** >> Okay. Okay. Let let me let me give you an example. Okay.

**[42:35]** an example. Okay.

**[42:35]** an example. Okay. Let's say I I I I have just come here

**[42:38]** Let's say I I I I have just come here

**[42:38]** Let's say I I I I have just come here and I mentioned you two things about me.

**[42:41]** and I mentioned you two things about me.

**[42:41]** and I mentioned you two things about me. I work for Amazon

**[42:44]** I work for Amazon

**[42:44]** I work for Amazon and

**[42:46]** and

**[42:46]** and I'm married. That's all. Okay. These are

**[42:49]** I'm married. That's all. Okay. These are

**[42:49]** I'm married. That's all. Okay. These are the two information that you have. Now

**[42:51]** the two information that you have. Now

**[42:51]** the two information that you have. Now if he asks you some question about me

**[42:53]** if he asks you some question about me

**[42:53]** if he asks you some question about me that uh okay uh tell me someone plays

**[42:56]** that uh okay uh tell me someone plays

**[42:56]** that uh okay uh tell me someone plays cricket or not. Will you be able to give

**[42:58]** cricket or not. Will you be able to give

**[42:58]** cricket or not. Will you be able to give some answer? No. You will be giving some


### [43:00 - 44:00]

**[43:01]** some answer? No. You will be giving some

**[43:01]** some answer? No. You will be giving some answer based on these two information

**[43:02]** answer based on these two information

**[43:02]** answer based on these two information but it will be random. Right? But now

**[43:06]** but it will be random. Right? But now

**[43:06]** but it will be random. Right? But now let's say if I give you more

**[43:07]** let's say if I give you more

**[43:08]** let's say if I give you more information. I am Suman. I work for

**[43:10]** information. I am Suman. I work for

**[43:10]** information. I am Suman. I work for Amazon.

**[43:12]** Amazon.

**[43:12]** Amazon. I am married.

**[43:14]** I am married.

**[43:14]** I am married. I have one wife as of now. I let's say I

**[43:18]** I have one wife as of now. I let's say I

**[43:18]** I have one wife as of now. I let's say I have one kid. Okay. And few other

**[43:21]** have one kid. Okay. And few other

**[43:21]** have one kid. Okay. And few other things.

**[43:22]** things.

**[43:22]** things. So if I keep on giving more features

**[43:24]** So if I keep on giving more features

**[43:24]** So if I keep on giving more features about me, you are having a richer uh

**[43:27]** about me, you are having a richer uh

**[43:28]** about me, you are having a richer uh information about me. So now if he asks

**[43:30]** information about me. So now if he asks

**[43:30]** information about me. So now if he asks you a question it's more likely that you

**[43:32]** you a question it's more likely that you

**[43:32]** you a question it's more likely that you will be able to give a uh you know you

**[43:34]** will be able to give a uh you know you

**[43:34]** will be able to give a uh you know you are you'll be able to give a more

**[43:36]** are you'll be able to give a more

**[43:36]** are you'll be able to give a more accurate answer. Same with this the

**[43:39]** accurate answer. Same with this the

**[43:39]** accurate answer. Same with this the moment you increase the embedding length

**[43:41]** moment you increase the embedding length

**[43:41]** moment you increase the embedding length you are it's not about chunk and all

**[43:43]** you are it's not about chunk and all

**[43:43]** you are it's not about chunk and all that it's just about how much granual

**[43:46]** that it's just about how much granual

**[43:46]** that it's just about how much granual information that you are having about a

**[43:48]** information that you are having about a

**[43:48]** information that you are having about a specific thing.

**[43:50]** specific thing.

**[43:50]** specific thing. Okay. So you can always embed uh any

**[43:53]** Okay. So you can always embed uh any

**[43:53]** Okay. So you can always embed uh any entity with just one number a vector of

**[43:56]** entity with just one number a vector of

**[43:56]** entity with just one number a vector of size one but it will not have much of an

**[43:59]** size one but it will not have much of an

**[43:59]** size one but it will not have much of an information as you increase the length


### [44:00 - 45:00]

**[44:01]** information as you increase the length

**[44:01]** information as you increase the length it will it will be more richer. Okay.

**[44:04]** it will it will be more richer. Okay.

**[44:04]** it will it will be more richer. Okay. Okay. So coming back to your question uh

**[44:08]** Okay. So coming back to your question uh

**[44:08]** Okay. So coming back to your question uh in the documentation I think they uh

**[44:10]** in the documentation I think they uh

**[44:10]** in the documentation I think they uh they said that 128 is a good number uh

**[44:13]** they said that 128 is a good number uh

**[44:13]** they said that 128 is a good number uh but you can always use 256 right if the

**[44:15]** but you can always use 256 right if the

**[44:15]** but you can always use 256 right if the vector database also supports that or

**[44:17]** vector database also supports that or

**[44:17]** vector database also supports that or the embedding model. Okay. So,

**[44:21]** the embedding model. Okay. So,

**[44:21]** the embedding model. Okay. So, so this is where we are just creating

**[44:23]** so this is where we are just creating

**[44:23]** so this is where we are just creating that collection. We have not even uh

**[44:25]** that collection. We have not even uh

**[44:25]** that collection. We have not even uh started creating the embeddings and all

**[44:26]** started creating the embeddings and all

**[44:26]** started creating the embeddings and all that. And see this here uh this is what

**[44:30]** that. And see this here uh this is what

**[44:30]** that. And see this here uh this is what u I was referring to when I said

**[44:33]** u I was referring to when I said

**[44:33]** u I was referring to when I said quadrant supports that matrix multiplic

**[44:35]** quadrant supports that matrix multiplic

**[44:36]** quadrant supports that matrix multiplic uh that u uh late interaction thing

**[44:39]** uh that u uh late interaction thing

**[44:39]** uh that u uh late interaction thing right so it says I'm setting some

**[44:41]** right so it says I'm setting some

**[44:41]** right so it says I'm setting some configuration that it's it should have

**[44:43]** configuration that it's it should have

**[44:43]** configuration that it's it should have multi vector configuration and multi

**[44:46]** multi vector configuration and multi

**[44:46]** multi vector configuration and multi vector comparator as maxim. So maxim is

**[44:49]** vector comparator as maxim. So maxim is

**[44:49]** vector comparator as maxim. So maxim is what uh helps us to get those three

**[44:52]** what uh helps us to get those three

**[44:52]** what uh helps us to get those three numbers from that matrix and then add

**[44:55]** numbers from that matrix and then add

**[44:55]** numbers from that matrix and then add those three numbers and give us the

**[44:57]** those three numbers and give us the

**[44:57]** those three numbers and give us the final value of the your query and each


### [45:00 - 46:00]

**[45:01]** final value of the your query and each

**[45:01]** final value of the your query and each page. So that at the end of the day what

**[45:03]** page. So that at the end of the day what

**[45:03]** page. So that at the end of the day what do we want? We want the relevant pages

**[45:06]** do we want? We want the relevant pages

**[45:06]** do we want? We want the relevant pages uh based on our question, right?

**[45:09]** uh based on our question, right?

**[45:09]** uh based on our question, right? Okay.

**[45:10]** Okay.

**[45:10]** Okay. So now once this is done, it's now

**[45:13]** So now once this is done, it's now

**[45:13]** So now once this is done, it's now pretty simple. I have to uh first create

**[45:17]** pretty simple. I have to uh first create

**[45:18]** pretty simple. I have to uh first create the embedding. But before that, I need

**[45:20]** the embedding. But before that, I need

**[45:20]** the embedding. But before that, I need to create convert my data into images.

**[45:23]** to create convert my data into images.

**[45:23]** to create convert my data into images. And that's what uh this uh this function

**[45:25]** And that's what uh this uh this function

**[45:26]** And that's what uh this uh this function does. So what it does is it it takes you

**[45:28]** does. So what it does is it it takes you

**[45:28]** does. So what it does is it it takes you it takes an uh directory and you can

**[45:31]** it takes an uh directory and you can

**[45:31]** it takes an uh directory and you can have hundreds of PDF files and it will

**[45:33]** have hundreds of PDF files and it will

**[45:34]** have hundreds of PDF files and it will go through all the PDF files and it will

**[45:36]** go through all the PDF files and it will

**[45:36]** go through all the PDF files and it will create uh images of each pages. Okay.

**[45:41]** create uh images of each pages. Okay.

**[45:41]** create uh images of each pages. Okay. And not only that, it will also add all

**[45:45]** And not only that, it will also add all

**[45:45]** And not only that, it will also add all of that into an list called all images.

**[45:48]** of that into an list called all images.

**[45:48]** of that into an list called all images. And this is just for my own housekeeping

**[45:50]** And this is just for my own housekeeping

**[45:50]** And this is just for my own housekeeping with some metadata like document ID,

**[45:52]** with some metadata like document ID,

**[45:52]** with some metadata like document ID, page number and the actual image in the

**[45:54]** page number and the actual image in the

**[45:54]** page number and the actual image in the form of RGB. And it will store it in a

**[45:58]** form of RGB. And it will store it in a

**[45:58]** form of RGB. And it will store it in a local directory called PDF data. And if


### [46:00 - 47:00]

**[46:01]** local directory called PDF data. And if

**[46:01]** local directory called PDF data. And if you just see the first two entries, you

**[46:03]** you just see the first two entries, you

**[46:03]** you just see the first two entries, you will see that okay, this is document

**[46:05]** will see that okay, this is document

**[46:05]** will see that okay, this is document number zero that is let's say I just

**[46:06]** number zero that is let's say I just

**[46:06]** number zero that is let's say I just have one PDF. So all the entries will

**[46:10]** have one PDF. So all the entries will

**[46:10]** have one PDF. So all the entries will have document ID zero, page number zero

**[46:12]** have document ID zero, page number zero

**[46:12]** have document ID zero, page number zero and this is the image page number one

**[46:15]** and this is the image page number one

**[46:15]** and this is the image page number one and this is the image. Okay. So this

**[46:17]** and this is the image. Okay. So this

**[46:17]** and this is the image. Okay. So this data set contains everything with me so

**[46:21]** data set contains everything with me so

**[46:21]** data set contains everything with me so far? Yes. Okay. Great. Now that I have

**[46:24]** far? Yes. Okay. Great. Now that I have

**[46:24]** far? Yes. Okay. Great. Now that I have this uh uh images, I can use the

**[46:28]** this uh uh images, I can use the

**[46:28]** this uh uh images, I can use the embedding model to generate the

**[46:30]** embedding model to generate the

**[46:30]** embedding model to generate the embedding and

**[46:33]** embedding and

**[46:33]** embedding and and this is where uh you know I just

**[46:35]** and this is where uh you know I just

**[46:35]** and this is where uh you know I just crashed my laptop. I initially used a

**[46:37]** crashed my laptop. I initially used a

**[46:37]** crashed my laptop. I initially used a batch size of 10 uh 12. So it took a lot

**[46:41]** batch size of 10 uh 12. So it took a lot

**[46:41]** batch size of 10 uh 12. So it took a lot of memory and I had just I think 16 gig

**[46:43]** of memory and I had just I think 16 gig

**[46:43]** of memory and I had just I think 16 gig of memory. So it it actually crashed but

**[46:47]** of memory. So it it actually crashed but

**[46:47]** of memory. So it it actually crashed but uh if you're trying in your laptop make

**[46:49]** uh if you're trying in your laptop make

**[46:49]** uh if you're trying in your laptop make sure that you use start with two or

**[46:50]** sure that you use start with two or

**[46:50]** sure that you use start with two or three. So it basically means how many

**[46:52]** three. So it basically means how many

**[46:52]** three. So it basically means how many images you want to process. And now here

**[46:55]** images you want to process. And now here

**[46:55]** images you want to process. And now here we are generating the embeddings and

**[46:58]** we are generating the embeddings and

**[46:58]** we are generating the embeddings and first we are going through this call pal


### [47:00 - 48:00]

**[47:03]** first we are going through this call pal

**[47:03]** first we are going through this call pal pre-processor which will just uh

**[47:04]** pre-processor which will just uh

**[47:04]** pre-processor which will just uh pre-process the image in a standard uh

**[47:07]** pre-process the image in a standard uh

**[47:07]** pre-process the image in a standard uh size and then I'm passing it through the

**[47:09]** size and then I'm passing it through the

**[47:09]** size and then I'm passing it through the call pali model which actually generates

**[47:11]** call pali model which actually generates

**[47:11]** call pali model which actually generates the embedding. So this will have my

**[47:13]** the embedding. So this will have my

**[47:13]** the embedding. So this will have my embeddings.

**[47:15]** embeddings.

**[47:15]** embeddings. And once I have all those uh embeddings,

**[47:19]** And once I have all those uh embeddings,

**[47:19]** And once I have all those uh embeddings, what I want to do is I want to store it

**[47:22]** what I want to do is I want to store it

**[47:22]** what I want to do is I want to store it in the vector database. And that is what

**[47:24]** in the vector database. And that is what

**[47:24]** in the vector database. And that is what I'm doing it here. I'm just inserting

**[47:27]** I'm doing it here. I'm just inserting

**[47:27]** I'm doing it here. I'm just inserting into the collection that I have created

**[47:28]** into the collection that I have created

**[47:28]** into the collection that I have created for all the points. Each point is

**[47:31]** for all the points. Each point is

**[47:31]** for all the points. Each point is nothing but you can think of it like uh

**[47:33]** nothing but you can think of it like uh

**[47:33]** nothing but you can think of it like uh each vectors. Okay. And in this case I

**[47:39]** each vectors. Okay. And in this case I

**[47:39]** each vectors. Okay. And in this case I have just 10 pages. So it will just

**[47:41]** have just 10 pages. So it will just

**[47:41]** have just 10 pages. So it will just generate the amount of number of

**[47:42]** generate the amount of number of

**[47:42]** generate the amount of number of embeddings for those 10 pages and it

**[47:44]** embeddings for those 10 pages and it

**[47:44]** embeddings for those 10 pages and it will store it here. Now is the final

**[47:47]** will store it here. Now is the final

**[47:47]** will store it here. Now is the final thing you know how we can retrieve. So

**[47:50]** thing you know how we can retrieve. So

**[47:50]** thing you know how we can retrieve. So see this I have just asked this question

**[47:53]** see this I have just asked this question

**[47:53]** see this I have just asked this question what are the different uh tropical

**[47:55]** what are the different uh tropical

**[47:55]** what are the different uh tropical levels because this is there in the book

**[47:58]** levels because this is there in the book

**[47:58]** levels because this is there in the book and this question also need to be uh


### [48:00 - 49:00]

**[48:02]** and this question also need to be uh

**[48:02]** and this question also need to be uh need to go through that embedding model

**[48:04]** need to go through that embedding model

**[48:04]** need to go through that embedding model just like images. So I will do go I'll

**[48:07]** just like images. So I will do go I'll

**[48:07]** just like images. So I will do go I'll make that through the pre-processor and

**[48:10]** make that through the pre-processor and

**[48:10]** make that through the pre-processor and the model and once that is done I will

**[48:13]** the model and once that is done I will

**[48:13]** the model and once that is done I will do a semantic search from the vector

**[48:14]** do a semantic search from the vector

**[48:14]** do a semantic search from the vector database and that is what we are doing

**[48:17]** database and that is what we are doing

**[48:17]** database and that is what we are doing we are just querying uh the vector

**[48:19]** we are just querying uh the vector

**[48:19]** we are just querying uh the vector database with our query token and I'm

**[48:22]** database with our query token and I'm

**[48:22]** database with our query token and I'm saying that the limit is five what this

**[48:25]** saying that the limit is five what this

**[48:25]** saying that the limit is five what this limit five means that means I need the

**[48:27]** limit five means that means I need the

**[48:27]** limit five means that means I need the top five pages which is relevant to this

**[48:30]** top five pages which is relevant to this

**[48:30]** top five pages which is relevant to this uh question

**[48:32]** uh question

**[48:32]** uh question and at the end you will find some five

**[48:35]** and at the end you will find some five

**[48:35]** and at the end you will find some five pages is and if you want to see those

**[48:38]** pages is and if you want to see those

**[48:38]** pages is and if you want to see those five pages how it uh you know how it

**[48:40]** five pages how it uh you know how it

**[48:40]** five pages how it uh you know how it looks like uh you can actually

**[48:42]** looks like uh you can actually

**[48:42]** looks like uh you can actually visualize. So this is just a wrapper

**[48:45]** visualize. So this is just a wrapper

**[48:45]** visualize. So this is just a wrapper python function which will just take all

**[48:47]** python function which will just take all

**[48:47]** python function which will just take all the images and it will just generate u

**[48:50]** the images and it will just generate u

**[48:50]** the images and it will just generate u the images in a pictorial format. Okay.

**[48:53]** the images in a pictorial format. Okay.

**[48:53]** the images in a pictorial format. Okay. And in fact if you see uh the this image

**[48:57]** And in fact if you see uh the this image

**[48:57]** And in fact if you see uh the this image I think this was uh this was the image I


### [49:00 - 50:00]

**[49:01]** I think this was uh this was the image I

**[49:01]** I think this was uh this was the image I guess uh yeah so this is where the

**[49:05]** guess uh yeah so this is where the

**[49:05]** guess uh yeah so this is where the tropical levels are mentioned it

**[49:06]** tropical levels are mentioned it

**[49:06]** tropical levels are mentioned it actually identified based on the

**[49:08]** actually identified based on the

**[49:08]** actually identified based on the question and the uh call embeddings

**[49:11]** question and the uh call embeddings

**[49:11]** question and the uh call embeddings right so this is the page and also there

**[49:13]** right so this is the page and also there

**[49:13]** right so this is the page and also there are other pages which we got now comes

**[49:16]** are other pages which we got now comes

**[49:16]** are other pages which we got now comes so retrieval is done right so call pal

**[49:18]** so retrieval is done right so call pal

**[49:18]** so retrieval is done right so call pal just talks about retrieval it's its job

**[49:22]** just talks about retrieval it's its job

**[49:22]** just talks about retrieval it's its job ends here. Okay. And uh if you if you

**[49:25]** ends here. Okay. And uh if you if you

**[49:25]** ends here. Okay. And uh if you if you think about it

**[49:27]** think about it

**[49:27]** think about it uh with respect to uh sorry with respect

**[49:31]** uh with respect to uh sorry with respect

**[49:31]** uh with respect to uh sorry with respect to this

**[49:34]** to this

**[49:34]** to this sorry here I guess

**[49:37]** sorry here I guess

**[49:37]** sorry here I guess in the traditional technique

**[49:40]** in the traditional technique

**[49:40]** in the traditional technique we came to this point right

**[49:43]** we came to this point right

**[49:43]** we came to this point right uh we came to this point sorry

**[49:53]** we came to this point when we got the

**[49:53]** we came to this point when we got the retrieved images and the question is

**[49:55]** retrieved images and the question is

**[49:55]** retrieved images and the question is already there. Now we can use any

**[49:57]** already there. Now we can use any

**[49:57]** already there. Now we can use any multimodal LLM to generate the answer.


### [50:00 - 51:00]

**[50:00]** multimodal LLM to generate the answer.

**[50:00]** multimodal LLM to generate the answer. Right? But we have skipped everything

**[50:02]** Right? But we have skipped everything

**[50:02]** Right? But we have skipped everything here. Right? So

**[50:05]** here. Right? So

**[50:05]** here. Right? So now when we when we use any generative

**[50:09]** now when we when we use any generative

**[50:09]** now when we when we use any generative model you can use any generative model

**[50:11]** model you can use any generative model

**[50:11]** model you can use any generative model of your choice. Uh if you don't have any

**[50:14]** of your choice. Uh if you don't have any

**[50:14]** of your choice. Uh if you don't have any AWS account or if you have any other uh

**[50:18]** AWS account or if you have any other uh

**[50:18]** AWS account or if you have any other uh model access you can always use that. uh

**[50:21]** model access you can always use that. uh

**[50:21]** model access you can always use that. uh but let's say uh you don't have bedrock

**[50:26]** but let's say uh you don't have bedrock

**[50:26]** but let's say uh you don't have bedrock access so we can use have you used just

**[50:29]** access so we can use have you used just

**[50:29]** access so we can use have you used just a local model the response may not be

**[50:31]** a local model the response may not be

**[50:31]** a local model the response may not be that great but you can work it out right

**[50:34]** that great but you can work it out right

**[50:34]** that great but you can work it out right so this is again a wrapper function just

**[50:37]** so this is again a wrapper function just

**[50:37]** so this is again a wrapper function just to uh convert all the images uh into the

**[50:41]** to uh convert all the images uh into the

**[50:41]** to uh convert all the images uh into the format that the model expects because we

**[50:43]** format that the model expects because we

**[50:43]** format that the model expects because we are we need a multimodal LLM right so we

**[50:46]** are we need a multimodal LLM right so we

**[50:46]** are we need a multimodal LLM right so we will take some multimodal LLM from Olama

**[50:48]** will take some multimodal LLM from Olama

**[50:48]** will take some multimodal LLM from Olama but depending on what model you're

**[50:51]** but depending on what model you're

**[50:51]** but depending on what model you're using. The model will ask you to have

**[50:53]** using. The model will ask you to have

**[50:53]** using. The model will ask you to have the input in a certain uh format, right?

**[50:55]** the input in a certain uh format, right?

**[50:56]** the input in a certain uh format, right? So it needs the data to be in base 64.

**[50:58]** So it needs the data to be in base 64.

**[50:58]** So it needs the data to be in base 64. That's what this small tiny function


### [51:00 - 52:00]

**[51:00]** That's what this small tiny function

**[51:00]** That's what this small tiny function does, right? Uh and then we just say

**[51:05]** does, right? Uh and then we just say

**[51:05]** does, right? Uh and then we just say generate and this is the model that I'm

**[51:06]** generate and this is the model that I'm

**[51:06]** generate and this is the model that I'm using and I'm sending the query and the

**[51:10]** using and I'm sending the query and the

**[51:10]** using and I'm sending the query and the image that's all right. So see this now

**[51:13]** image that's all right. So see this now

**[51:13]** image that's all right. So see this now I'm sending the full query, not the

**[51:15]** I'm sending the full query, not the

**[51:15]** I'm sending the full query, not the embedding of the query because Olama has

**[51:17]** embedding of the query because Olama has

**[51:17]** embedding of the query because Olama has nothing to do with that embedding of the

**[51:18]** nothing to do with that embedding of the

**[51:18]** nothing to do with that embedding of the query. that embedding was needed just

**[51:20]** query. that embedding was needed just

**[51:20]** query. that embedding was needed just for semantic search right and then uh we

**[51:24]** for semantic search right and then uh we

**[51:24]** for semantic search right and then uh we get some response if you want to use

**[51:26]** get some response if you want to use

**[51:26]** get some response if you want to use bedrock then you should have bedrock

**[51:29]** bedrock then you should have bedrock

**[51:29]** bedrock then you should have bedrock access how many of you know about

**[51:30]** access how many of you know about

**[51:30]** access how many of you know about bedrock

**[51:32]** bedrock

**[51:32]** bedrock okay perfect so it's just a managed

**[51:34]** okay perfect so it's just a managed

**[51:34]** okay perfect so it's just a managed service on AWS through which you can

**[51:36]** service on AWS through which you can

**[51:36]** service on AWS through which you can access any different I mean different

**[51:37]** access any different I mean different

**[51:37]** access any different I mean different kinds of model and

**[51:41]** kinds of model and

**[51:41]** kinds of model and the way that bedrock expects you to give

**[51:43]** the way that bedrock expects you to give

**[51:43]** the way that bedrock expects you to give the input uh multimodel input is little

**[51:47]** the input uh multimodel input is little

**[51:47]** the input uh multimodel input is little different and that's That's why we have

**[51:49]** different and that's That's why we have

**[51:49]** different and that's That's why we have some wrapper functions uh which will

**[51:52]** some wrapper functions uh which will

**[51:52]** some wrapper functions uh which will which will make your prompt you know

**[51:55]** which will make your prompt you know

**[51:55]** which will make your prompt you know according to the multimodal uh models

**[51:57]** according to the multimodal uh models

**[51:57]** according to the multimodal uh models requirement right and you can go through


### [52:00 - 53:00]

**[52:00]** requirement right and you can go through

**[52:00]** requirement right and you can go through these two functions it's standard uh you

**[52:03]** these two functions it's standard uh you

**[52:03]** these two functions it's standard uh you know uh converse API that we have used

**[52:06]** know uh converse API that we have used

**[52:06]** know uh converse API that we have used so nothing fancy here so I don't want to

**[52:07]** so nothing fancy here so I don't want to

**[52:07]** so nothing fancy here so I don't want to go there because that is not the purpose

**[52:09]** go there because that is not the purpose

**[52:09]** go there because that is not the purpose of this uh problem but ultimately you

**[52:13]** of this uh problem but ultimately you

**[52:13]** of this uh problem but ultimately you give the images and the query and you

**[52:16]** give the images and the query and you

**[52:16]** give the images and the query and you mention the model ID so in this case I'm

**[52:18]** mention the model ID so in this case I'm

**[52:18]** mention the model ID so in this case I'm using set uh claude sonnet 3.7. You can

**[52:22]** using set uh claude sonnet 3.7. You can

**[52:22]** using set uh claude sonnet 3.7. You can very well use sonet 4 if you would like

**[52:24]** very well use sonet 4 if you would like

**[52:24]** very well use sonet 4 if you would like to. And you generate the image uh sorry

**[52:26]** to. And you generate the image uh sorry

**[52:26]** to. And you generate the image uh sorry the final response. Okay with me so far?

**[52:31]** the final response. Okay with me so far?

**[52:31]** the final response. Okay with me so far? Okay. Now comes the agent thing. How we

**[52:35]** Okay. Now comes the agent thing. How we

**[52:35]** Okay. Now comes the agent thing. How we can make this agentic? So it's very

**[52:38]** can make this agentic? So it's very

**[52:38]** can make this agentic? So it's very simple, right? You don't have to go

**[52:39]** simple, right? You don't have to go

**[52:39]** simple, right? You don't have to go through all these things because what we

**[52:42]** through all these things because what we

**[52:42]** through all these things because what we have done is ultimately what we want

**[52:44]** have done is ultimately what we want

**[52:44]** have done is ultimately what we want when somebody is asking a question we

**[52:46]** when somebody is asking a question we

**[52:46]** when somebody is asking a question we want an agent to to retrieve the

**[52:52]** want an agent to to retrieve the

**[52:52]** want an agent to to retrieve the shortlisted images and give it to me.

**[52:54]** shortlisted images and give it to me.

**[52:54]** shortlisted images and give it to me. That's all. Right? So we have seen how

**[52:57]** That's all. Right? So we have seen how

**[52:57]** That's all. Right? So we have seen how to shortlist those images. Right? What

**[52:59]** to shortlist those images. Right? What


### [53:00 - 54:00]

**[53:00]** to shortlist those images. Right? What we are going to do is

**[53:02]** we are going to do is

**[53:02]** we are going to do is uh here

**[53:11]** I'll just go through that later. Yeah,

**[53:11]** I'll just go through that later. Yeah, what we going to do is we are going to

**[53:13]** what we going to do is we are going to

**[53:13]** what we going to do is we are going to create a function called retrieve from

**[53:15]** create a function called retrieve from

**[53:15]** create a function called retrieve from quadrant which will just take your query

**[53:19]** quadrant which will just take your query

**[53:19]** quadrant which will just take your query and if you see the uh uh return for this

**[53:24]** and if you see the uh uh return for this

**[53:24]** and if you see the uh uh return for this are the matched image paths that is what

**[53:26]** are the matched image paths that is what

**[53:26]** are the matched image paths that is what we want nothing else right and the code

**[53:29]** we want nothing else right and the code

**[53:29]** we want nothing else right and the code here in this function are the exact same

**[53:30]** here in this function are the exact same

**[53:30]** here in this function are the exact same code which has gone through in multiple

**[53:32]** code which has gone through in multiple

**[53:32]** code which has gone through in multiple cells you know previously it just it

**[53:36]** cells you know previously it just it

**[53:36]** cells you know previously it just it does the same thing and now to make it

**[53:39]** does the same thing and now to make it

**[53:39]** does the same thing and now to make it agentic

**[53:40]** agentic

**[53:40]** agentic I have used a framework called strands.

**[53:43]** I have used a framework called strands.

**[53:43]** I have used a framework called strands. Have you heard of strands? Right. Okay.

**[53:45]** Have you heard of strands? Right. Okay.

**[53:45]** Have you heard of strands? Right. Okay. So strands is a new agentic framework.

**[53:49]** So strands is a new agentic framework.

**[53:49]** So strands is a new agentic framework. Let me just show you this. It's

**[53:51]** Let me just show you this. It's

**[53:51]** Let me just show you this. It's strandsagent.com.

**[53:53]** strandsagent.com.

**[53:53]** strandsagent.com. This is a uh SDK which was launched by

**[53:56]** This is a uh SDK which was launched by

**[53:56]** This is a uh SDK which was launched by AWS. Uh I worked with on at the launch.


### [54:00 - 55:00]

**[54:00]** AWS. Uh I worked with on at the launch.

**[54:00]** AWS. Uh I worked with on at the launch. There are some YouTube video as well. Uh

**[54:02]** There are some YouTube video as well. Uh

**[54:02]** There are some YouTube video as well. Uh you can just go over and just search for

**[54:04]** you can just go over and just search for

**[54:04]** you can just go over and just search for strands agents. You will find a launch

**[54:07]** strands agents. You will find a launch

**[54:07]** strands agents. You will find a launch blog as well. Okay. But basically it is

**[54:09]** blog as well. Okay. But basically it is

**[54:09]** blog as well. Okay. But basically it is very very simple just to give you an

**[54:11]** very very simple just to give you an

**[54:11]** very very simple just to give you an example how to get started with strands.

**[54:14]** example how to get started with strands.

**[54:14]** example how to get started with strands. Uh you just pip install

**[54:18]** Uh you just pip install

**[54:18]** Uh you just pip install and uh do you want to see a quick demo

**[54:20]** and uh do you want to see a quick demo

**[54:20]** and uh do you want to see a quick demo of strands before we go to that part?

**[54:23]** of strands before we go to that part?

**[54:23]** of strands before we go to that part? Will that help? Yes. Okay. So let me

**[54:25]** Will that help? Yes. Okay. So let me

**[54:25]** Will that help? Yes. Okay. So let me just show you. I think I have that.

**[54:33]** Okay. So let me quickly spend four

**[54:33]** Okay. So let me quickly spend four minutes on that. Four five minutes. I

**[54:36]** minutes on that. Four five minutes. I

**[54:36]** minutes on that. Four five minutes. I have a good demo actually if you want.

**[54:38]** have a good demo actually if you want.

**[54:38]** have a good demo actually if you want. How many of you have heard of um three

**[54:40]** How many of you have heard of um three

**[54:40]** How many of you have heard of um three blue one brown?

**[54:43]** blue one brown?

**[54:43]** blue one brown? Okay, perfect. Okay, so then let me show

**[54:45]** Okay, perfect. Okay, so then let me show

**[54:45]** Okay, perfect. Okay, so then let me show you that you might you might uh it might

**[54:48]** you that you might you might uh it might

**[54:48]** you that you might you might uh it might be interesting. So strands is an uh

**[54:51]** be interesting. So strands is an uh

**[54:51]** be interesting. So strands is an uh framework very simple. It's a model

**[54:54]** framework very simple. It's a model

**[54:54]** framework very simple. It's a model first framework. So we are just taking a

**[54:56]** first framework. So we are just taking a

**[54:56]** first framework. So we are just taking a pause on that. Okay, we are just we will

**[54:57]** pause on that. Okay, we are just we will

**[54:57]** pause on that. Okay, we are just we will whatever we learn here we will just use

**[54:59]** whatever we learn here we will just use

**[54:59]** whatever we learn here we will just use this framework to make our workflow


### [55:00 - 56:00]

**[55:02]** this framework to make our workflow

**[55:02]** this framework to make our workflow whatever we have done agenting and we

**[55:04]** whatever we have done agenting and we

**[55:04]** whatever we have done agenting and we will add a voice part of that as well.

**[55:07]** will add a voice part of that as well.

**[55:07]** will add a voice part of that as well. So here

**[55:09]** So here

**[55:09]** So here there's an open source framework which

**[55:11]** there's an open source framework which

**[55:11]** there's an open source framework which is model first. That means uh now the

**[55:15]** is model first. That means uh now the

**[55:15]** is model first. That means uh now the models are so strong we expect that the

**[55:19]** models are so strong we expect that the

**[55:19]** models are so strong we expect that the model should reason rather than we

**[55:21]** model should reason rather than we

**[55:21]** model should reason rather than we telling uh the agent with a lot of

**[55:23]** telling uh the agent with a lot of

**[55:24]** telling uh the agent with a lot of backstory goals prompting and all that.

**[55:26]** backstory goals prompting and all that.

**[55:26]** backstory goals prompting and all that. We don't want all of that. We throw a

**[55:28]** We don't want all of that. We throw a

**[55:28]** We don't want all of that. We throw a question. We expect the model to

**[55:30]** question. We expect the model to

**[55:30]** question. We expect the model to generate the response and do the

**[55:32]** generate the response and do the

**[55:32]** generate the response and do the reasoning uh on on the model side.

**[55:34]** reasoning uh on on the model side.

**[55:34]** reasoning uh on on the model side. That's that's why this is very very

**[55:37]** That's that's why this is very very

**[55:37]** That's that's why this is very very lightweight and it has the integration

**[55:39]** lightweight and it has the integration

**[55:39]** lightweight and it has the integration with different models and you can use

**[55:40]** with different models and you can use

**[55:40]** with different models and you can use model from bedrock you can use directly

**[55:42]** model from bedrock you can use directly

**[55:42]** model from bedrock you can use directly from entropic you can use light LLM.

**[55:45]** from entropic you can use light LLM.

**[55:45]** from entropic you can use light LLM. Have you heard of light LLM? Yeah. So

**[55:47]** Have you heard of light LLM? Yeah. So

**[55:47]** Have you heard of light LLM? Yeah. So when you have an access to light LLM you

**[55:49]** when you have an access to light LLM you

**[55:49]** when you have an access to light LLM you can access any model that light LLM

**[55:51]** can access any model that light LLM

**[55:51]** can access any model that light LLM supports. Right now this is what it is.

**[55:55]** supports. Right now this is what it is.

**[55:55]** supports. Right now this is what it is. So strands you by the definition of

**[55:58]** So strands you by the definition of

**[55:58]** So strands you by the definition of strands it's a DNA structure and it just


### [56:00 - 57:00]

**[56:01]** strands it's a DNA structure and it just

**[56:02]** strands it's a DNA structure and it just have two strands and that two strands

**[56:05]** have two strands and that two strands

**[56:05]** have two strands and that two strands stands for model and tool that's all. So

**[56:09]** stands for model and tool that's all. So

**[56:09]** stands for model and tool that's all. So you make an agent with one model and few

**[56:13]** you make an agent with one model and few

**[56:13]** you make an agent with one model and few tools and simply you just ask the

**[56:16]** tools and simply you just ask the

**[56:16]** tools and simply you just ask the question that's all. It's as simple as

**[56:17]** question that's all. It's as simple as

**[56:17]** question that's all. It's as simple as that right and let me show you uh one

**[56:20]** that right and let me show you uh one

**[56:20]** that right and let me show you uh one quick demo.

**[56:23]** quick demo.

**[56:23]** quick demo. Let's see if it uh if it works. Okay.

**[56:33]** So this is is it visible from you know

**[56:33]** So this is is it visible from you know last row? No, not that much. Right.

**[56:41]** Okay. I'll just read it out. So we are

**[56:41]** Okay. I'll just read it out. So we are just importing um agent and we are

**[56:47]** just importing um agent and we are

**[56:47]** just importing um agent and we are importing the tools. Okay. And

**[56:53]** importing the tools. Okay. And

**[56:53]** importing the tools. Okay. And okay, this is I think this is the MCP

**[56:55]** okay, this is I think this is the MCP

**[56:55]** okay, this is I think this is the MCP one. No, no, this is not the one I want

**[56:56]** one. No, no, this is not the one I want

**[56:56]** one. No, no, this is not the one I want to show you.


### [57:00 - 58:00]

**[57:13]** Okay, let let's uh see this.

**[57:13]** Okay, let let's uh see this. Okay, just uh uh I think it's a video.

**[57:16]** Okay, just uh uh I think it's a video.

**[57:16]** Okay, just uh uh I think it's a video. It should work fine.

**[57:24]** Yeah,

**[57:24]** Yeah, let's see. So, we first install strands

**[57:28]** let's see. So, we first install strands

**[57:28]** let's see. So, we first install strands agent and strands tool. PIP install

**[57:31]** agent and strands tool. PIP install

**[57:31]** agent and strands tool. PIP install simple pip install

**[57:38]** and it's open source. Okay, so you don't

**[57:38]** and it's open source. Okay, so you don't have to uh and it supports Olama as

**[57:40]** have to uh and it supports Olama as

**[57:40]** have to uh and it supports Olama as well. So, you don't have to have an AWS

**[57:43]** well. So, you don't have to have an AWS

**[57:43]** well. So, you don't have to have an AWS account or anything of that sort.

**[57:47]** account or anything of that sort.

**[57:47]** account or anything of that sort. So what we are going to do is we are

**[57:48]** So what we are going to do is we are

**[57:48]** So what we are going to do is we are going to create a file create a summary

**[57:51]** going to create a file create a summary

**[57:51]** going to create a file create a summary write the summary into the into our file

**[57:54]** write the summary into the into our file

**[57:54]** write the summary into the into our file and uh also add a voice part of it.

**[57:58]** and uh also add a voice part of it.

**[57:58]** and uh also add a voice part of it. Let's see I think it would be pretty


### [58:00 - 59:00]

**[58:01]** Let's see I think it would be pretty

**[58:01]** Let's see I think it would be pretty quick.

**[58:09]** So we are importing is it visible or I

**[58:09]** So we are importing is it visible or I should should I show it? It's pretty

**[58:11]** should should I show it? It's pretty

**[58:11]** should should I show it? It's pretty straightforward.

**[58:13]** straightforward.

**[58:13]** straightforward. So we are importing agent and we are

**[58:16]** So we are importing agent and we are

**[58:16]** So we are importing agent and we are importing the bedrock model. By default

**[58:19]** importing the bedrock model. By default

**[58:19]** importing the bedrock model. By default it uses bedrock model. Uh it actually

**[58:21]** it uses bedrock model. Uh it actually

**[58:22]** it uses bedrock model. Uh it actually uses clot 3.7 but you can use any other

**[58:25]** uses clot 3.7 but you can use any other

**[58:25]** uses clot 3.7 but you can use any other model. And I have used some built-in

**[58:27]** model. And I have used some built-in

**[58:27]** model. And I have used some built-in tool called read file, write file and

**[58:30]** tool called read file, write file and

**[58:30]** tool called read file, write file and speak. And this is the model ID. And

**[58:33]** speak. And this is the model ID. And

**[58:33]** speak. And this is the model ID. And this is the prompt. You can have a

**[58:36]** this is the prompt. You can have a

**[58:36]** this is the prompt. You can have a prompt, you can skip a prompt, doesn't

**[58:38]** prompt, you can skip a prompt, doesn't

**[58:38]** prompt, you can skip a prompt, doesn't matter.

**[58:39]** matter.

**[58:39]** matter. And lastly you have to create the agent.

**[58:45]** And lastly you have to create the agent.

**[58:45]** And lastly you have to create the agent. So

**[58:47]** So

**[58:47]** So say this agent contains the model ID

**[58:49]** say this agent contains the model ID

**[58:49]** say this agent contains the model ID system prompt and the tools and all

**[58:51]** system prompt and the tools and all

**[58:51]** system prompt and the tools and all these tools you have not written the

**[58:52]** these tools you have not written the

**[58:52]** these tools you have not written the code for this. This is by default right

**[58:55]** code for this. This is by default right

**[58:55]** code for this. This is by default right and I'm just asking uh a particular

**[58:58]** and I'm just asking uh a particular

**[58:58]** and I'm just asking uh a particular question and see this I'm in the prompt


### [59:00 - 01:00:00]

**[59:02]** question and see this I'm in the prompt

**[59:02]** question and see this I'm in the prompt I'm saying that this is a textbook uh in

**[59:05]** I'm saying that this is a textbook uh in

**[59:05]** I'm saying that this is a textbook uh in my local directory read that create a

**[59:07]** my local directory read that create a

**[59:07]** my local directory read that create a summary and write it into the local

**[59:10]** summary and write it into the local

**[59:10]** summary and write it into the local directory and also speak out the final

**[59:12]** directory and also speak out the final

**[59:12]** directory and also speak out the final answer

**[59:14]** answer

**[59:14]** answer and see this it is using the tools for

**[59:16]** and see this it is using the tools for

**[59:16]** and see this it is using the tools for read the file second it is create after

**[59:19]** read the file second it is create after

**[59:20]** read the file second it is create after >> functions like a camera light entering

**[59:22]** >> functions like a camera light entering

**[59:22]** >> functions like a camera light entering through the cornea and focus by a lens

**[59:23]** through the cornea and focus by a lens

**[59:23]** through the cornea and focus by a lens onto the

**[59:24]** onto the

**[59:24]** onto the >> we have not done anything just in

**[59:26]** >> we have not done anything just in

**[59:26]** >> we have not done anything just in controls pupil size to regulate incoming

**[59:28]** controls pupil size to regulate incoming

**[59:28]** controls pupil size to regulate incoming light

**[59:29]** light

**[59:29]** light >> the I can adjust focal length through

**[59:31]** >> the I can adjust focal length through

**[59:31]** >> the I can adjust focal length through accommodation see

**[59:34]** accommodation see

**[59:34]** accommodation see >> all right so now I I will share one more

**[59:37]** >> all right so now I I will share one more

**[59:37]** >> all right so now I I will share one more thing now I'll not show you the code

**[59:40]** thing now I'll not show you the code

**[59:40]** thing now I'll not show you the code that is not the purpose of this but have

**[59:42]** that is not the purpose of this but have

**[59:42]** that is not the purpose of this but have you heard of um of course you have heard

**[59:44]** you heard of um of course you have heard

**[59:44]** you heard of um of course you have heard of MCP

**[59:46]** of MCP

**[59:46]** of MCP yeah so see this I I'll not tell you I

**[59:50]** yeah so see this I I'll not tell you I

**[59:50]** yeah so see this I I'll not tell you I think you should be able So

**[59:54]** think you should be able So

**[59:54]** think you should be able So I've created an MCP server called um

**[59:57]** I've created an MCP server called um

**[59:57]** I've created an MCP server called um created an MCP server with manm okay so


### [01:00:00 - 01:01:00]

**[01:00:01]** created an MCP server with manm okay so

**[01:00:01]** created an MCP server with manm okay so manim have you heard of manm okay just

**[01:00:03]** manim have you heard of manm okay just

**[01:00:04]** manim have you heard of manm okay just just see that so idea is so let me just

**[01:00:09]** just see that so idea is so let me just

**[01:00:09]** just see that so idea is so let me just show you what we are doing we are

**[01:00:11]** show you what we are doing we are

**[01:00:11]** show you what we are doing we are creating a man server and this is the

**[01:00:15]** creating a man server and this is the

**[01:00:15]** creating a man server and this is the MCP server now this is the client on

**[01:00:17]** MCP server now this is the client on

**[01:00:17]** MCP server now this is the client on nothing but uh our strand agent and this

**[01:00:20]** nothing but uh our strand agent and this

**[01:00:20]** nothing but uh our strand agent and this will call this MCP server. Okay. And I

**[01:00:24]** will call this MCP server. Okay. And I

**[01:00:24]** will call this MCP server. Okay. And I can give any question. So question is

**[01:00:26]** can give any question. So question is

**[01:00:26]** can give any question. So question is create a man screen which draws a cubic

**[01:00:30]** create a man screen which draws a cubic

**[01:00:30]** create a man screen which draws a cubic function like 2x^ 3 minus blah blah

**[01:00:34]** function like 2x^ 3 minus blah blah

**[01:00:34]** function like 2x^ 3 minus blah blah blah. Okay. And see what happens.

**[01:00:41]** Now it is executing the code calling

**[01:00:41]** Now it is executing the code calling this uh MCP server. It is working uh

**[01:00:44]** this uh MCP server. It is working uh

**[01:00:44]** this uh MCP server. It is working uh here and then it should give you some

**[01:00:46]** here and then it should give you some

**[01:00:46]** here and then it should give you some response.

**[01:00:58]** So it generated this video. Okay.

**[01:00:58]** So it generated this video. Okay. And now you will get some familiarity.


### [01:01:00 - 01:02:00]

**[01:01:10]** Looks similar, right?

**[01:01:10]** Looks similar, right? I have not done anything. All I have

**[01:01:13]** I have not done anything. All I have

**[01:01:13]** I have not done anything. All I have used is a manage uh uh SDK and created

**[01:01:16]** used is a manage uh uh SDK and created

**[01:01:16]** used is a manage uh uh SDK and created that uh MCP server which can generate

**[01:01:19]** that uh MCP server which can generate

**[01:01:19]** that uh MCP server which can generate videos like uh what three blue one brown

**[01:01:22]** videos like uh what three blue one brown

**[01:01:22]** videos like uh what three blue one brown created. So this is just a small demo of

**[01:01:25]** created. So this is just a small demo of

**[01:01:25]** created. So this is just a small demo of how you can make use of strands with an

**[01:01:27]** how you can make use of strands with an

**[01:01:27]** how you can make use of strands with an MCP and write simple code and you know

**[01:01:31]** MCP and write simple code and you know

**[01:01:31]** MCP and write simple code and you know do wonderful things. Okay. All right. So

**[01:01:34]** do wonderful things. Okay. All right. So

**[01:01:34]** do wonderful things. Okay. All right. So this is about strand.

**[01:01:36]** this is about strand.

**[01:01:36]** this is about strand. The core idea of strand is uh just pip

**[01:01:41]** The core idea of strand is uh just pip

**[01:01:41]** The core idea of strand is uh just pip install and use it with the by default

**[01:01:45]** install and use it with the by default

**[01:01:45]** install and use it with the by default tools and uh your model of your choice.

**[01:01:48]** tools and uh your model of your choice.

**[01:01:48]** tools and uh your model of your choice. That's all. There's nothing uh no

**[01:01:50]** That's all. There's nothing uh no

**[01:01:50]** That's all. There's nothing uh no scaffolding uh beyond this. Okay. So

**[01:01:53]** scaffolding uh beyond this. Okay. So

**[01:01:53]** scaffolding uh beyond this. Okay. So it's just like this you pip install

**[01:01:55]** it's just like this you pip install

**[01:01:55]** it's just like this you pip install create an instance and just ask

**[01:01:57]** create an instance and just ask

**[01:01:57]** create an instance and just ask question. Here we have not mentioned any

**[01:01:59]** question. Here we have not mentioned any

**[01:01:59]** question. Here we have not mentioned any model that means it will by default use


### [01:02:00 - 01:03:00]

**[01:02:00]** model that means it will by default use

**[01:02:00]** model that means it will by default use bedrock model but in the demo we have

**[01:02:02]** bedrock model but in the demo we have

**[01:02:02]** bedrock model but in the demo we have seen that you can define your bedrock

**[01:02:04]** seen that you can define your bedrock

**[01:02:04]** seen that you can define your bedrock models here. Okay. So now let's come

**[01:02:08]** models here. Okay. So now let's come

**[01:02:08]** models here. Okay. So now let's come back to our our um

**[01:02:11]** back to our our um

**[01:02:11]** back to our our um our problem. In this case our tool is

**[01:02:15]** our problem. In this case our tool is

**[01:02:15]** our problem. In this case our tool is not the default one but the tool that we

**[01:02:17]** not the default one but the tool that we

**[01:02:17]** not the default one but the tool that we have defined. And what is that tool? The

**[01:02:19]** have defined. And what is that tool? The

**[01:02:19]** have defined. And what is that tool? The retrieval tool. And how I can create a

**[01:02:22]** retrieval tool. And how I can create a

**[01:02:22]** retrieval tool. And how I can create a uh custom tool it just by importing tool

**[01:02:26]** uh custom tool it just by importing tool

**[01:02:26]** uh custom tool it just by importing tool and just use that as a decorator on top

**[01:02:28]** and just use that as a decorator on top

**[01:02:28]** and just use that as a decorator on top of your function. That's all. Now this

**[01:02:31]** of your function. That's all. Now this

**[01:02:31]** of your function. That's all. Now this becomes a tool for me just like read

**[01:02:33]** becomes a tool for me just like read

**[01:02:33]** becomes a tool for me just like read file write file speak. This is just a

**[01:02:35]** file write file speak. This is just a

**[01:02:35]** file write file speak. This is just a tool for me. Okay. And we can defi we

**[01:02:40]** tool for me. Okay. And we can defi we

**[01:02:40]** tool for me. Okay. And we can defi we can use make use of bedrock model or up

**[01:02:43]** can use make use of bedrock model or up

**[01:02:43]** can use make use of bedrock model or up to you. And now look at this. We are

**[01:02:48]** to you. And now look at this. We are

**[01:02:48]** to you. And now look at this. We are also importing an image reader. Why we

**[01:02:50]** also importing an image reader. Why we

**[01:02:50]** also importing an image reader. Why we are importing this image reader? I will

**[01:02:52]** are importing this image reader? I will

**[01:02:52]** are importing this image reader? I will uh tell you a little later. But uh you

**[01:02:55]** uh tell you a little later. But uh you

**[01:02:55]** uh tell you a little later. But uh you you remember that when we use this

**[01:02:57]** you remember that when we use this

**[01:02:57]** you remember that when we use this bedrock model for final answer when we


### [01:03:00 - 01:04:00]

**[01:03:00]** bedrock model for final answer when we

**[01:03:00]** bedrock model for final answer when we use this bedrock model to generate the

**[01:03:03]** use this bedrock model to generate the

**[01:03:03]** use this bedrock model to generate the final answer we created some custom

**[01:03:05]** final answer we created some custom

**[01:03:05]** final answer we created some custom functions which are nothing but uh

**[01:03:08]** functions which are nothing but uh

**[01:03:08]** functions which are nothing but uh contains the information about how to uh

**[01:03:11]** contains the information about how to uh

**[01:03:11]** contains the information about how to uh create the prompt for your images for

**[01:03:14]** create the prompt for your images for

**[01:03:14]** create the prompt for your images for bedrock models right so I don't have to

**[01:03:16]** bedrock models right so I don't have to

**[01:03:16]** bedrock models right so I don't have to do all these things and uh I can simply

**[01:03:20]** do all these things and uh I can simply

**[01:03:20]** do all these things and uh I can simply make use of this image reader which just

**[01:03:23]** make use of this image reader which just

**[01:03:23]** make use of this image reader which just takes an image and generates uh the

**[01:03:26]** takes an image and generates uh the

**[01:03:26]** takes an image and generates uh the prompt for us. And now I have a system

**[01:03:28]** prompt for us. And now I have a system

**[01:03:28]** prompt for us. And now I have a system prompt. System prompt says that you are

**[01:03:31]** prompt. System prompt says that you are

**[01:03:31]** prompt. System prompt says that you are a rag based system and all that. And it

**[01:03:33]** a rag based system and all that. And it

**[01:03:33]** a rag based system and all that. And it also says uh these are the two functions

**[01:03:35]** also says uh these are the two functions

**[01:03:36]** also says uh these are the two functions that you have or the tools that you have

**[01:03:38]** that you have or the tools that you have

**[01:03:38]** that you have or the tools that you have to use and all that. And that's all.

**[01:03:41]** to use and all that. And that's all.

**[01:03:41]** to use and all that. And that's all. And now you create an agent again just

**[01:03:44]** And now you create an agent again just

**[01:03:44]** And now you create an agent again just like before you define the model system

**[01:03:46]** like before you define the model system

**[01:03:46]** like before you define the model system prompt. And in this case we use two

**[01:03:48]** prompt. And in this case we use two

**[01:03:48]** prompt. And in this case we use two tools. One is the retrieve from quadrant

**[01:03:50]** tools. One is the retrieve from quadrant

**[01:03:50]** tools. One is the retrieve from quadrant which is our tool and the image reader

**[01:03:53]** which is our tool and the image reader

**[01:03:53]** which is our tool and the image reader for the generation part. Okay.

**[01:03:57]** for the generation part. Okay.

**[01:03:57]** for the generation part. Okay. And then we ask this question what is

**[01:03:59]** And then we ask this question what is

**[01:03:59]** And then we ask this question what is the difference uh different tropical


### [01:04:00 - 01:05:00]

**[01:04:02]** the difference uh different tropical

**[01:04:02]** the difference uh different tropical levels and now it just agents uh

**[01:04:05]** levels and now it just agents uh

**[01:04:05]** levels and now it just agents uh generates the response just like before

**[01:04:07]** generates the response just like before

**[01:04:07]** generates the response just like before but now everything is done by the agent.

**[01:04:09]** but now everything is done by the agent.

**[01:04:10]** but now everything is done by the agent. And the beauty is let's say now you want

**[01:04:11]** And the beauty is let's say now you want

**[01:04:11]** And the beauty is let's say now you want to add the voice feature. I don't only

**[01:04:16]** to add the voice feature. I don't only

**[01:04:16]** to add the voice feature. I don't only want the answer but also the final

**[01:04:17]** want the answer but also the final

**[01:04:17]** want the answer but also the final response in the form of voice. So far I

**[01:04:21]** response in the form of voice. So far I

**[01:04:21]** response in the form of voice. So far I have done this. I'm just reducing the

**[01:04:23]** have done this. I'm just reducing the

**[01:04:23]** have done this. I'm just reducing the image so that everything fits in. So far

**[01:04:28]** image so that everything fits in. So far

**[01:04:28]** image so that everything fits in. So far we have done this. We ask a question. It

**[01:04:31]** we have done this. We ask a question. It

**[01:04:31]** we have done this. We ask a question. It goes to a strands agent. It uses this

**[01:04:33]** goes to a strands agent. It uses this

**[01:04:33]** goes to a strands agent. It uses this retrieval tool custom tool that we have

**[01:04:35]** retrieval tool custom tool that we have

**[01:04:35]** retrieval tool custom tool that we have created. It gets the relevant chunk

**[01:04:38]** created. It gets the relevant chunk

**[01:04:38]** created. It gets the relevant chunk which are nothing but the shortlisted

**[01:04:40]** which are nothing but the shortlisted

**[01:04:40]** which are nothing but the shortlisted pages and then

**[01:04:43]** pages and then

**[01:04:43]** pages and then it uses any of these models let's say

**[01:04:47]** it uses any of these models let's say

**[01:04:47]** it uses any of these models let's say bedrock colama whatever to generate the

**[01:04:49]** bedrock colama whatever to generate the

**[01:04:49]** bedrock colama whatever to generate the final response and to generate this it

**[01:04:53]** final response and to generate this it

**[01:04:53]** final response and to generate this it uses this image reader tool. Now what we

**[01:04:55]** uses this image reader tool. Now what we

**[01:04:55]** uses this image reader tool. Now what we have to do is to add voice

**[01:04:57]** have to do is to add voice

**[01:04:57]** have to do is to add voice functionality. I will just use the speak

**[01:04:59]** functionality. I will just use the speak

**[01:04:59]** functionality. I will just use the speak uh tool. That's all. Just one uh import.


### [01:05:00 - 01:06:00]

**[01:05:03]** uh tool. That's all. Just one uh import.

**[01:05:03]** uh tool. That's all. Just one uh import. Okay.

**[01:05:05]** Okay.

**[01:05:05]** Okay. And

**[01:05:07]** And

**[01:05:07]** And that is what we are doing. We are just

**[01:05:09]** that is what we are doing. We are just

**[01:05:09]** that is what we are doing. We are just adding speak here.

**[01:05:12]** adding speak here.

**[01:05:12]** adding speak here. And again the system prompt remains the

**[01:05:14]** And again the system prompt remains the

**[01:05:14]** And again the system prompt remains the same. And I'm quering the same thing.

**[01:05:16]** same. And I'm quering the same thing.

**[01:05:16]** same. And I'm quering the same thing. And now when I ask this question. So

**[01:05:18]** And now when I ask this question. So

**[01:05:18]** And now when I ask this question. So let's say let's ask this question. Okay.

**[01:05:21]** let's say let's ask this question. Okay.

**[01:05:21]** let's say let's ask this question. Okay. So let me run this

**[01:05:24]** So let me run this

**[01:05:24]** So let me run this and let me let me just ask in the

**[01:05:28]** and let me let me just ask in the

**[01:05:28]** and let me let me just ask in the question itself explain the answer over

**[01:05:31]** question itself explain the answer over

**[01:05:31]** question itself explain the answer over a female voice in a natural way.

**[01:05:52]** I hope I'm connected with the internet

**[01:05:52]** I hope I'm connected with the internet but let's see.

**[01:05:59]** So when you run this uh code in your

**[01:05:59]** So when you run this uh code in your environment you can simply remove the


### [01:06:00 - 01:07:00]

**[01:06:02]** environment you can simply remove the

**[01:06:02]** environment you can simply remove the system prompt you will still get the

**[01:06:04]** system prompt you will still get the

**[01:06:04]** system prompt you will still get the right answer. In fact try this prompt. I

**[01:06:07]** right answer. In fact try this prompt. I

**[01:06:07]** right answer. In fact try this prompt. I have not tried but try this change this

**[01:06:09]** have not tried but try this change this

**[01:06:09]** have not tried but try this change this prompt and say that mail voice or

**[01:06:11]** prompt and say that mail voice or

**[01:06:11]** prompt and say that mail voice or something like that right robotic uh uh

**[01:06:14]** something like that right robotic uh uh

**[01:06:14]** something like that right robotic uh uh way of uh you know not a natural way

**[01:06:16]** way of uh you know not a natural way

**[01:06:16]** way of uh you know not a natural way maybe robotic way something like that.

**[01:06:19]** maybe robotic way something like that.

**[01:06:19]** maybe robotic way something like that. The idea is see that whether strands is

**[01:06:22]** The idea is see that whether strands is

**[01:06:22]** The idea is see that whether strands is able to

**[01:06:24]** able to

**[01:06:24]** able to you know forward that information to the

**[01:06:27]** you know forward that information to the

**[01:06:27]** you know forward that information to the model or not right so you don't need a

**[01:06:29]** model or not right so you don't need a

**[01:06:29]** model or not right so you don't need a system prompt uh it may be because of my

**[01:06:33]** system prompt uh it may be because of my

**[01:06:33]** system prompt uh it may be because of my internet uh but it's it doesn't take

**[01:06:35]** internet uh but it's it doesn't take

**[01:06:35]** internet uh but it's it doesn't take that much of time you just give it a

**[01:06:37]** that much of time you just give it a

**[01:06:37]** that much of time you just give it a shot it should work fine okay so that's

**[01:06:41]** shot it should work fine okay so that's

**[01:06:41]** shot it should work fine okay so that's what I uh I had uh for for uh this

**[01:06:45]** what I uh I had uh for for uh this

**[01:06:45]** what I uh I had uh for for uh this particular uh workshop

**[01:06:48]** particular uh workshop

**[01:06:48]** particular uh workshop uh I would okay it's now running so it's

**[01:06:51]** uh I would okay it's now running so it's

**[01:06:51]** uh I would okay it's now running so it's little slow

**[01:06:54]** little slow

**[01:06:54]** little slow but let me

**[01:06:57]** but let me

**[01:06:57]** but let me so it is now able to generate the images


### [01:07:00 - 01:08:00]

**[01:07:02]** so it is now able to generate the images

**[01:07:02]** so it is now able to generate the images I mean shortlisted the images and now it

**[01:07:05]** I mean shortlisted the images and now it

**[01:07:05]** I mean shortlisted the images and now it should speak in a female voice

**[01:07:18]** so while that happens Okay,

**[01:07:18]** so while that happens Okay, >> trophic levels are the different feeding

**[01:07:20]** >> trophic levels are the different feeding

**[01:07:20]** >> trophic levels are the different feeding positions in a food chain representing

**[01:07:22]** positions in a food chain representing

**[01:07:22]** positions in a food chain representing the flow of energy through an ecosystem.

**[01:07:25]** the flow of energy through an ecosystem.

**[01:07:25]** the flow of energy through an ecosystem. There are typically four.

**[01:07:26]** There are typically four.

**[01:07:26]** There are typically four. >> Okay. So, let me just stop this and

**[01:07:29]** >> Okay. So, let me just stop this and

**[01:07:29]** >> Okay. So, let me just stop this and let's say if I let's try this. Okay. Um,

**[01:07:34]** let's say if I let's try this. Okay. Um,

**[01:07:34]** let's say if I let's try this. Okay. Um, let me delete this system prompt

**[01:07:37]** let me delete this system prompt

**[01:07:38]** let me delete this system prompt and

**[01:07:39]** and

**[01:07:39]** and let me just have this model and the

**[01:07:41]** let me just have this model and the

**[01:07:41]** let me just have this model and the tools. There is no speak, nothing, no

**[01:07:43]** tools. There is no speak, nothing, no

**[01:07:43]** tools. There is no speak, nothing, no system prompt. There's nothing there.

**[01:07:46]** system prompt. There's nothing there.

**[01:07:46]** system prompt. There's nothing there. And here I will change this to a male

**[01:07:49]** And here I will change this to a male

**[01:07:49]** And here I will change this to a male voice. Okay.

**[01:07:53]** voice. Okay.

**[01:07:53]** voice. Okay. And uh I'll give it a shot. Let this I

**[01:07:56]** And uh I'll give it a shot. Let this I

**[01:07:56]** And uh I'll give it a shot. Let this I don't want to interrupt.

**[01:07:58]** don't want to interrupt.

**[01:07:58]** don't want to interrupt. >> Which are small carnivores that eat

**[01:07:59]** >> Which are small carnivores that eat

**[01:07:59]** >> Which are small carnivores that eat herbivores. These might include frogs,


### [01:08:00 - 01:09:00]

**[01:08:02]** herbivores. These might include frogs,

**[01:08:02]** herbivores. These might include frogs, small birds or foxes. The fourth trophic

**[01:08:06]** small birds or foxes. The fourth trophic

**[01:08:06]** small birds or foxes. The fourth trophic level is occupied by tertiary consumers

**[01:08:08]** level is occupied by tertiary consumers

**[01:08:08]** level is occupied by tertiary consumers or top carnivores.

**[01:08:09]** or top carnivores.

**[01:08:10]** or top carnivores. >> You can in fact say something like

**[01:08:11]** >> You can in fact say something like

**[01:08:11]** >> You can in fact say something like summarize in uh you know 50 words or 100

**[01:08:14]** summarize in uh you know 50 words or 100

**[01:08:14]** summarize in uh you know 50 words or 100 words rather than waiting for this to

**[01:08:16]** words rather than waiting for this to

**[01:08:16]** words rather than waiting for this to complete.

**[01:08:17]** complete.

**[01:08:17]** complete. that energy transfer

**[01:08:19]** that energy transfer

**[01:08:19]** that energy transfer >> still going on

**[01:08:30]** and

**[01:08:30]** and before I forget

**[01:08:32]** before I forget

**[01:08:32]** before I forget if you want to know about that

**[01:08:34]** if you want to know about that

**[01:08:34]** if you want to know about that multimodal that the traditional

**[01:08:36]** multimodal that the traditional

**[01:08:36]** multimodal that the traditional technique in this GitHub repo there is

**[01:08:38]** technique in this GitHub repo there is

**[01:08:38]** technique in this GitHub repo there is the part three and here you will find

**[01:08:42]** the part three and here you will find

**[01:08:42]** the part three and here you will find the details of uh that architecture like

**[01:08:46]** the details of uh that architecture like

**[01:08:46]** the details of uh that architecture like um uh this architecture right and you

**[01:08:49]** um uh this architecture right and you

**[01:08:49]** um uh this architecture right and you know this notebook is about how you can

**[01:08:51]** know this notebook is about how you can

**[01:08:51]** know this notebook is about how you can do the same thing but uh pre-processing

**[01:08:54]** do the same thing but uh pre-processing

**[01:08:54]** do the same thing but uh pre-processing this image text and table okay so just

**[01:08:56]** this image text and table okay so just

**[01:08:56]** this image text and table okay so just play around this GitHub repo


### [01:09:00 - 01:10:00]

**[01:09:00]** play around this GitHub repo

**[01:09:00]** play around this GitHub repo okay it's done so now I will quickly

**[01:09:05]** okay it's done so now I will quickly

**[01:09:06]** okay it's done so now I will quickly uh

**[01:09:12]** I just created this agent now but uh

**[01:09:12]** I just created this agent now but uh without any uh system prompt Now I just

**[01:09:17]** without any uh system prompt Now I just

**[01:09:17]** without any uh system prompt Now I just executed this and now let's run this. So

**[01:09:20]** executed this and now let's run this. So

**[01:09:20]** executed this and now let's run this. So now I am letting uh

**[01:09:23]** now I am letting uh

**[01:09:23]** now I am letting uh the agent

**[01:09:25]** the agent

**[01:09:25]** the agent know only about the models nothing else.

**[01:09:27]** know only about the models nothing else.

**[01:09:27]** know only about the models nothing else. There is no system prompt.

**[01:09:46]** I just hope we get a male voice at

**[01:09:46]** I just hope we get a male voice at least.

**[01:09:48]** least.

**[01:09:48]** least. >> Let me explain trophic levels, which are

**[01:09:51]** >> Let me explain trophic levels, which are

**[01:09:51]** >> Let me explain trophic levels, which are essentially the different feeding

**[01:09:52]** essentially the different feeding

**[01:09:52]** essentially the different feeding positions in a food chain or ecosystem.

**[01:09:55]** positions in a food chain or ecosystem.

**[01:09:55]** positions in a food chain or ecosystem. Think of them as the levels in nature's

**[01:09:57]** Think of them as the levels in nature's

**[01:09:57]** Think of them as the levels in nature's dining hierarchy. Starting at the base,

**[01:09:59]** dining hierarchy. Starting at the base,

**[01:09:59]** dining hierarchy. Starting at the base, we have the producers. These are main


### [01:10:00 - 01:11:00]

**[01:10:02]** we have the producers. These are main

**[01:10:02]** we have the producers. These are main >> Okay, let's see if I have

**[01:10:29]** boys.

**[01:10:30]** boys. Let's try this.

**[01:10:50]** Trophic levels are essentially the

**[01:10:50]** Trophic levels are essentially the different feeding positions in a food

**[01:10:51]** different feeding positions in a food

**[01:10:52]** different feeding positions in a food chain showing how energy flows through

**[01:10:54]** chain showing how energy flows through

**[01:10:54]** chain showing how energy flows through an ecosystem. Let me walk you through

**[01:10:56]** an ecosystem. Let me walk you through

**[01:10:56]** an ecosystem. Let me walk you through the main

**[01:10:58]** the main

**[01:10:58]** the main at the very bottom we have the

**[01:10:59]** at the very bottom we have the

**[01:10:59]** at the very bottom we have the producers. You can try this out and see


### [01:11:00 - 01:12:00]

**[01:11:03]** producers. You can try this out and see

**[01:11:03]** producers. You can try this out and see what you can mention so that you can

**[01:11:05]** what you can mention so that you can

**[01:11:05]** what you can mention so that you can augment the tool. In fact, this is not

**[01:11:09]** augment the tool. In fact, this is not

**[01:11:09]** augment the tool. In fact, this is not the right way to do this because by

**[01:11:11]** the right way to do this because by

**[01:11:11]** the right way to do this because by default it is a female voice. You can

**[01:11:14]** default it is a female voice. You can

**[01:11:14]** default it is a female voice. You can actually change the behavior of this uh

**[01:11:17]** actually change the behavior of this uh

**[01:11:17]** actually change the behavior of this uh speak tool. Okay. So the way that you

**[01:11:20]** speak tool. Okay. So the way that you

**[01:11:20]** speak tool. Okay. So the way that you can do is you can go to the

**[01:11:21]** can do is you can go to the

**[01:11:21]** can do is you can go to the documentation and uh if you see this

**[01:11:24]** documentation and uh if you see this

**[01:11:24]** documentation and uh if you see this documentation

**[01:11:26]** documentation

**[01:11:26]** documentation uh here we have tools and uh you can

**[01:11:32]** uh here we have tools and uh you can

**[01:11:32]** uh here we have tools and uh you can see the overview

**[01:11:34]** see the overview

**[01:11:34]** see the overview and if you see this here

**[01:11:43]** there is a tool spec. Yeah, here's a

**[01:11:43]** there is a tool spec. Yeah, here's a tool spec for different tools and you

**[01:11:45]** tool spec for different tools and you

**[01:11:46]** tool spec for different tools and you can mention what persona that you want.

**[01:11:48]** can mention what persona that you want.

**[01:11:48]** can mention what persona that you want. So that is a more deterministic way uh

**[01:11:50]** So that is a more deterministic way uh

**[01:11:50]** So that is a more deterministic way uh to do that or else you can put that in

**[01:11:52]** to do that or else you can put that in

**[01:11:52]** to do that or else you can put that in the uh system prompt. Okay. So that's

**[01:11:55]** the uh system prompt. Okay. So that's

**[01:11:56]** the uh system prompt. Okay. So that's all I have. Uh u if you have any

**[01:11:58]** all I have. Uh u if you have any

**[01:11:58]** all I have. Uh u if you have any questions feel free to ask or uh you


### [01:12:00 - 01:13:00]

**[01:12:01]** questions feel free to ask or uh you

**[01:12:01]** questions feel free to ask or uh you know uh you know feel free to connect

**[01:12:03]** know uh you know feel free to connect

**[01:12:03]** know uh you know feel free to connect and u you know would be more than happy

**[01:12:05]** and u you know would be more than happy

**[01:12:05]** and u you know would be more than happy uh to connect offline.

**[01:12:08]** uh to connect offline.

**[01:12:08]** uh to connect offline. >> Yeah.

**[01:12:13]** >> Yeah.

**[01:12:13]** >> Yeah. >> So have you seen any

**[01:12:19]** is already using this in production and

**[01:12:19]** is already using this in production and what type of scaling uh

**[01:12:22]** what type of scaling uh

**[01:12:22]** what type of scaling uh >> yeah yeah

**[01:12:23]** >> yeah yeah

**[01:12:23]** >> yeah yeah >> yeah that's a good question so we have

**[01:12:26]** >> yeah that's a good question so we have

**[01:12:26]** >> yeah that's a good question so we have used this in one of the insurance a

**[01:12:28]** used this in one of the insurance a

**[01:12:28]** used this in one of the insurance a leading insurance company where they had

**[01:12:30]** leading insurance company where they had

**[01:12:30]** leading insurance company where they had u the images of driver u licenses and

**[01:12:36]** u the images of driver u licenses and

**[01:12:36]** u the images of driver u licenses and they have the images of insurance

**[01:12:38]** they have the images of insurance

**[01:12:38]** they have the images of insurance policies and all that and we tried with

**[01:12:40]** policies and all that and we tried with

**[01:12:40]** policies and all that and we tried with different techniques one of the

**[01:12:42]** different techniques one of the

**[01:12:42]** different techniques one of the technique that we used was OCR which

**[01:12:44]** technique that we used was OCR which

**[01:12:44]** technique that we used was OCR which worked fine uh but CalPali was working

**[01:12:46]** worked fine uh but CalPali was working

**[01:12:46]** worked fine uh but CalPali was working pretty

**[01:12:47]** pretty

**[01:12:47]** pretty And it was the only drawback which I

**[01:12:50]** And it was the only drawback which I

**[01:12:50]** And it was the only drawback which I have seen with this call pal model is it

**[01:12:54]** have seen with this call pal model is it

**[01:12:54]** have seen with this call pal model is it is very heavy but uh that heaviness

**[01:12:56]** is very heavy but uh that heaviness

**[01:12:56]** is very heavy but uh that heaviness comes only at the time of data

**[01:12:58]** comes only at the time of data

**[01:12:58]** comes only at the time of data injection. So when you create the

**[01:12:59]** injection. So when you create the

**[01:12:59]** injection. So when you create the embeddings one that is done at the query


### [01:13:00 - 01:14:00]

**[01:13:01]** embeddings one that is done at the query

**[01:13:01]** embeddings one that is done at the query time it is pretty fast. Okay. Uh but

**[01:13:04]** time it is pretty fast. Okay. Uh but

**[01:13:04]** time it is pretty fast. Okay. Uh but when you are putting the data at that

**[01:13:06]** when you are putting the data at that

**[01:13:06]** when you are putting the data at that time it's little heavy. Okay. And uh uh

**[01:13:09]** time it's little heavy. Okay. And uh uh

**[01:13:10]** time it's little heavy. Okay. And uh uh I guess if you are thinking that if you

**[01:13:13]** I guess if you are thinking that if you

**[01:13:13]** I guess if you are thinking that if you have 1,000 documents each has 1,000

**[01:13:16]** have 1,000 documents each has 1,000

**[01:13:16]** have 1,000 documents each has 1,000 pages, you will do a search among all

**[01:13:19]** pages, you will do a search among all

**[01:13:19]** pages, you will do a search among all those images. That is not how it works.

**[01:13:22]** those images. That is not how it works.

**[01:13:22]** those images. That is not how it works. Because imagine if I ask you the same

**[01:13:24]** Because imagine if I ask you the same

**[01:13:24]** Because imagine if I ask you the same question. Forget about all this. If you

**[01:13:27]** question. Forget about all this. If you

**[01:13:27]** question. Forget about all this. If you use a text based embedding model and if

**[01:13:30]** use a text based embedding model and if

**[01:13:30]** use a text based embedding model and if you have a book of

**[01:13:32]** you have a book of

**[01:13:32]** you have a book of 1 million pages, you have 100 million

**[01:13:35]** 1 million pages, you have 100 million

**[01:13:35]** 1 million pages, you have 100 million vectors and when you ask a question,

**[01:13:37]** vectors and when you ask a question,

**[01:13:37]** vectors and when you ask a question, does the vector database search for all

**[01:13:39]** does the vector database search for all

**[01:13:39]** does the vector database search for all the vectors? No, there is a different

**[01:13:41]** the vectors? No, there is a different

**[01:13:41]** the vectors? No, there is a different indexing techniques that all the

**[01:13:42]** indexing techniques that all the

**[01:13:42]** indexing techniques that all the database uses. Same indexing technique

**[01:13:46]** database uses. Same indexing technique

**[01:13:46]** database uses. Same indexing technique are used here as well. It's just that

**[01:13:48]** are used here as well. It's just that

**[01:13:48]** are used here as well. It's just that now the vectors represent different

**[01:13:50]** now the vectors represent different

**[01:13:50]** now the vectors represent different thing. Now the vector represent patches.

**[01:13:52]** thing. Now the vector represent patches.

**[01:13:52]** thing. Now the vector represent patches. In the previous case, the vector

**[01:13:54]** In the previous case, the vector

**[01:13:54]** In the previous case, the vector represents images or sorry uh a chunk of

**[01:13:56]** represents images or sorry uh a chunk of

**[01:13:56]** represents images or sorry uh a chunk of text but uh that semantic search happens


### [01:14:00 - 01:15:00]

**[01:14:00]** text but uh that semantic search happens

**[01:14:00]** text but uh that semantic search happens very efficiently uh using a different

**[01:14:02]** very efficiently uh using a different

**[01:14:02]** very efficiently uh using a different indexing technique. One of the technique

**[01:14:04]** indexing technique. One of the technique

**[01:14:04]** indexing technique. One of the technique that we use is I think hierarchical

**[01:14:07]** that we use is I think hierarchical

**[01:14:07]** that we use is I think hierarchical small world navigation u so where it

**[01:14:10]** small world navigation u so where it

**[01:14:10]** small world navigation u so where it uses a treebased uh you know structure

**[01:14:13]** uses a treebased uh you know structure

**[01:14:14]** uses a treebased uh you know structure uh it just finds uh the root node uh I

**[01:14:16]** uh it just finds uh the root node uh I

**[01:14:16]** uh it just finds uh the root node uh I mean it it starts on the top layer it

**[01:14:18]** mean it it starts on the top layer it

**[01:14:18]** mean it it starts on the top layer it finds one of the closest node and

**[01:14:20]** finds one of the closest node and

**[01:14:20]** finds one of the closest node and whichever node is closest then it goes

**[01:14:22]** whichever node is closest then it goes

**[01:14:22]** whichever node is closest then it goes down and finds its neighbor so you are

**[01:14:24]** down and finds its neighbor so you are

**[01:14:24]** down and finds its neighbor so you are just you can think of it like uh uh you

**[01:14:27]** just you can think of it like uh uh you

**[01:14:27]** just you can think of it like uh uh you know in u in computer science we have

**[01:14:30]** know in u in computer science we have

**[01:14:30]** know in u in computer science we have tree pruning right so that's what we do

**[01:14:32]** tree pruning right so that's what we do

**[01:14:32]** tree pruning right so that's what we do so it reduces the search space. Yeah.

**[01:14:35]** so it reduces the search space. Yeah.

**[01:14:36]** so it reduces the search space. Yeah. >> So a quick follow.

**[01:14:36]** >> So a quick follow.

**[01:14:36]** >> So a quick follow. >> Yeah. So can we see

**[01:14:40]** >> Yeah. So can we see

**[01:14:40]** >> Yeah. So can we see more companies

**[01:14:42]** more companies

**[01:14:42]** more companies this can see this as a replacement for

**[01:14:45]** this can see this as a replacement for

**[01:14:45]** this can see this as a replacement for >> no traditional?

**[01:14:46]** >> no traditional?

**[01:14:46]** >> no traditional? >> Yeah, that's a good question. No, I

**[01:14:48]** >> Yeah, that's a good question. No, I

**[01:14:48]** >> Yeah, that's a good question. No, I don't think this is a replacement. This

**[01:14:49]** don't think this is a replacement. This

**[01:14:49]** don't think this is a replacement. This is just another technique and this is

**[01:14:51]** is just another technique and this is

**[01:14:52]** is just another technique and this is also you know

**[01:14:54]** also you know

**[01:14:54]** also you know you know it's a space where things are

**[01:14:56]** you know it's a space where things are

**[01:14:56]** you know it's a space where things are changing very fast. Right. Um I

**[01:14:59]** changing very fast. Right. Um I

**[01:14:59]** changing very fast. Right. Um I personally feel if we get a vision based


### [01:15:00 - 01:16:00]

**[01:15:02]** personally feel if we get a vision based

**[01:15:02]** personally feel if we get a vision based model which is more efficient in terms

**[01:15:03]** model which is more efficient in terms

**[01:15:03]** model which is more efficient in terms of computation this might be a good

**[01:15:05]** of computation this might be a good

**[01:15:05]** of computation this might be a good model. Uh but again this may work for

**[01:15:09]** model. Uh but again this may work for

**[01:15:09]** model. Uh but again this may work for your data may not work for your data. So

**[01:15:11]** your data may not work for your data. So

**[01:15:11]** your data may not work for your data. So it's all about your data. What I would

**[01:15:13]** it's all about your data. What I would

**[01:15:13]** it's all about your data. What I would do and what I do generally is whenever I

**[01:15:15]** do and what I do generally is whenever I

**[01:15:15]** do and what I do generally is whenever I get some problem I try to solve with the

**[01:15:17]** get some problem I try to solve with the

**[01:15:17]** get some problem I try to solve with the least uh I mean the most cost effective

**[01:15:20]** least uh I mean the most cost effective

**[01:15:20]** least uh I mean the most cost effective way or most efficient way. basically

**[01:15:23]** way or most efficient way. basically

**[01:15:23]** way or most efficient way. basically more than the cost. First we have to

**[01:15:25]** more than the cost. First we have to

**[01:15:25]** more than the cost. First we have to find out which architecture works fine

**[01:15:28]** find out which architecture works fine

**[01:15:28]** find out which architecture works fine for my data. If that is working fine I

**[01:15:30]** for my data. If that is working fine I

**[01:15:30]** for my data. If that is working fine I don't why to complicate things and

**[01:15:32]** don't why to complicate things and

**[01:15:32]** don't why to complicate things and create images and all that. I will go to

**[01:15:34]** create images and all that. I will go to

**[01:15:34]** create images and all that. I will go to this only when my data set is very much

**[01:15:36]** this only when my data set is very much

**[01:15:36]** this only when my data set is very much converted and where you as an human you

**[01:15:41]** converted and where you as an human you

**[01:15:41]** converted and where you as an human you feel that I can read this data only if I

**[01:15:43]** feel that I can read this data only if I

**[01:15:43]** feel that I can read this data only if I look at it. Imagine that you have a PDF

**[01:15:46]** look at it. Imagine that you have a PDF

**[01:15:46]** look at it. Imagine that you have a PDF file. For that simple text file for that

**[01:15:51]** file. For that simple text file for that

**[01:15:51]** file. For that simple text file for that you can get the answer from that PDF

**[01:15:53]** you can get the answer from that PDF

**[01:15:53]** you can get the answer from that PDF file even if somebody converts that into

**[01:15:55]** file even if somebody converts that into

**[01:15:56]** file even if somebody converts that into a text file and give it to you. But

**[01:15:58]** a text file and give it to you. But

**[01:15:58]** a text file and give it to you. But let's say you have a PDF file which

**[01:15:59]** let's say you have a PDF file which

**[01:15:59]** let's say you have a PDF file which contains mostly images and embedded text


### [01:16:00 - 01:17:00]

**[01:16:02]** contains mostly images and embedded text

**[01:16:02]** contains mostly images and embedded text on top of that then you will say that

**[01:16:04]** on top of that then you will say that

**[01:16:04]** on top of that then you will say that okay okay don't give only text you give

**[01:16:05]** okay okay don't give only text you give

**[01:16:06]** okay okay don't give only text you give me the book I will figure out because I

**[01:16:07]** me the book I will figure out because I

**[01:16:07]** me the book I will figure out because I need to see what is the context of that.

**[01:16:09]** need to see what is the context of that.

**[01:16:09]** need to see what is the context of that. So it's just like it replicates humans u

**[01:16:12]** So it's just like it replicates humans u

**[01:16:12]** So it's just like it replicates humans u uh you know uh behavior to understand

**[01:16:14]** uh you know uh behavior to understand

**[01:16:14]** uh you know uh behavior to understand any data. U so I would recommend not to

**[01:16:17]** any data. U so I would recommend not to

**[01:16:17]** any data. U so I would recommend not to start with this start with the

**[01:16:19]** start with this start with the

**[01:16:19]** start with this start with the traditional technique because that is

**[01:16:20]** traditional technique because that is

**[01:16:20]** traditional technique because that is more effective um cost effective and

**[01:16:23]** more effective um cost effective and

**[01:16:23]** more effective um cost effective and also it it is less heavy because here we

**[01:16:26]** also it it is less heavy because here we

**[01:16:26]** also it it is less heavy because here we are storing a lot of vectors for each

**[01:16:29]** are storing a lot of vectors for each

**[01:16:29]** are storing a lot of vectors for each page right so but use this when you have

**[01:16:32]** page right so but use this when you have

**[01:16:32]** page right so but use this when you have a very convoluted data okay yes sir

**[01:16:37]** a very convoluted data okay yes sir

**[01:16:37]** a very convoluted data okay yes sir >> so I'm trying to get a sense when it's

**[01:16:40]** >> so I'm trying to get a sense when it's

**[01:16:40]** >> so I'm trying to get a sense when it's good when it's not

**[01:16:47]** im into these little squares. Is there

**[01:16:47]** im into these little squares. Is there an issue where

**[01:16:49]** an issue where

**[01:16:49]** an issue where you know let's say you're in the middle

**[01:16:51]** you know let's say you're in the middle

**[01:16:51]** you know let's say you're in the middle of paragraph

**[01:16:57]** two different segments does that cause

**[01:16:57]** two different segments does that cause problems in practice?

**[01:16:58]** problems in practice?

**[01:16:58]** problems in practice? >> Yeah, that's a good question. But here


### [01:17:00 - 01:18:00]

**[01:17:01]** >> Yeah, that's a good question. But here

**[01:17:01]** >> Yeah, that's a good question. But here the model doesn't know that that there

**[01:17:04]** the model doesn't know that that there

**[01:17:04]** the model doesn't know that that there is any chunking or anything that we are

**[01:17:06]** is any chunking or anything that we are

**[01:17:06]** is any chunking or anything that we are understanding it that way. But to the

**[01:17:08]** understanding it that way. But to the

**[01:17:08]** understanding it that way. But to the model it's just an image and the way

**[01:17:11]** model it's just an image and the way

**[01:17:11]** model it's just an image and the way that it creates the embeddings for that

**[01:17:13]** that it creates the embeddings for that

**[01:17:13]** that it creates the embeddings for that image is by uh doing that those patches

**[01:17:17]** image is by uh doing that those patches

**[01:17:17]** image is by uh doing that those patches and why the model knows this because the

**[01:17:20]** and why the model knows this because the

**[01:17:20]** and why the model knows this because the when the model was trained it's a vision

**[01:17:21]** when the model was trained it's a vision

**[01:17:21]** when the model was trained it's a vision based model. So when the model was

**[01:17:23]** based model. So when the model was

**[01:17:23]** based model. So when the model was trained it used to chunk all the

**[01:17:26]** trained it used to chunk all the

**[01:17:26]** trained it used to chunk all the training data set like that and that's

**[01:17:28]** training data set like that and that's

**[01:17:28]** training data set like that and that's how the you know it has optimized for

**[01:17:31]** how the you know it has optimized for

**[01:17:31]** how the you know it has optimized for that data. For example during the

**[01:17:33]** that data. For example during the

**[01:17:34]** that data. For example during the training time of call pali not at the

**[01:17:35]** training time of call pali not at the

**[01:17:35]** training time of call pali not at the inference time during the training time

**[01:17:38]** inference time during the training time

**[01:17:38]** inference time during the training time when it was given an image of a cat and

**[01:17:41]** when it was given an image of a cat and

**[01:17:41]** when it was given an image of a cat and the text about a cat the cat image was

**[01:17:44]** the text about a cat the cat image was

**[01:17:44]** the text about a cat the cat image was also chopped into those many p uh

**[01:17:47]** also chopped into those many p uh

**[01:17:47]** also chopped into those many p uh patches. Similarly, when there was an

**[01:17:49]** patches. Similarly, when there was an

**[01:17:49]** patches. Similarly, when there was an image of a of a PDF page, it was chopped

**[01:17:53]** image of a of a PDF page, it was chopped

**[01:17:53]** image of a of a PDF page, it was chopped with the same uh patches. So that was

**[01:17:56]** with the same uh patches. So that was

**[01:17:56]** with the same uh patches. So that was inherited during the training process

**[01:17:58]** inherited during the training process

**[01:17:58]** inherited during the training process itself. So we don't have to question


### [01:18:00 - 01:19:00]

**[01:18:00]** itself. So we don't have to question

**[01:18:00]** itself. So we don't have to question that okay model how you are doing this.

**[01:18:03]** that okay model how you are doing this.

**[01:18:03]** that okay model how you are doing this. You the model will say that I have been

**[01:18:05]** You the model will say that I have been

**[01:18:05]** You the model will say that I have been doing this don't give me advice. I have

**[01:18:07]** doing this don't give me advice. I have

**[01:18:08]** doing this don't give me advice. I have been doing this with you know the

**[01:18:09]** been doing this with you know the

**[01:18:09]** been doing this with you know the plethora of data. So if you if you just

**[01:18:12]** plethora of data. So if you if you just

**[01:18:12]** plethora of data. So if you if you just look at it blindly from outside, I also

**[01:18:15]** look at it blindly from outside, I also

**[01:18:15]** look at it blindly from outside, I also had the same thought how the model is

**[01:18:18]** had the same thought how the model is

**[01:18:18]** had the same thought how the model is going to create an embedding when it

**[01:18:20]** going to create an embedding when it

**[01:18:20]** going to create an embedding when it splits a table into multiple chunks.

**[01:18:24]** splits a table into multiple chunks.

**[01:18:24]** splits a table into multiple chunks. What is the relationship between one

**[01:18:25]** What is the relationship between one

**[01:18:25]** What is the relationship between one chunk and the other chunk? How the model

**[01:18:27]** chunk and the other chunk? How the model

**[01:18:27]** chunk and the other chunk? How the model is you know doing that? Later on we

**[01:18:30]** is you know doing that? Later on we

**[01:18:30]** is you know doing that? Later on we realized that this has been incorporated

**[01:18:32]** realized that this has been incorporated

**[01:18:32]** realized that this has been incorporated during the training process itself.

**[01:18:33]** during the training process itself.

**[01:18:33]** during the training process itself. Initially it was not able to do that

**[01:18:35]** Initially it was not able to do that

**[01:18:35]** Initially it was not able to do that right but when during the training

**[01:18:37]** right but when during the training

**[01:18:37]** right but when during the training process the loss must have been very

**[01:18:39]** process the loss must have been very

**[01:18:39]** process the loss must have been very high.

**[01:18:40]** high.

**[01:18:40]** high. Right? So, and that's how it has been

**[01:18:42]** Right? So, and that's how it has been

**[01:18:42]** Right? So, and that's how it has been optimized. So, one that is optimized,

**[01:18:44]** optimized. So, one that is optimized,

**[01:18:44]** optimized. So, one that is optimized, you don't have to worry about that. And

**[01:18:46]** you don't have to worry about that. And

**[01:18:46]** you don't have to worry about that. And this is basically if you think about

**[01:18:47]** this is basically if you think about

**[01:18:47]** this is basically if you think about this this patching and embedding, it's

**[01:18:50]** this this patching and embedding, it's

**[01:18:50]** this this patching and embedding, it's it's not a new technique.

**[01:18:53]** it's not a new technique.

**[01:18:53]** it's not a new technique. Uh you know, it was there in lot of

**[01:18:55]** Uh you know, it was there in lot of

**[01:18:55]** Uh you know, it was there in lot of vision based model. Now, we are using it

**[01:18:57]** vision based model. Now, we are using it

**[01:18:57]** vision based model. Now, we are using it for retrieval.

**[01:18:59]** for retrieval.

**[01:18:59]** for retrieval. So, that's that's how it works.


### [01:19:00 - 01:20:00]

**[01:19:02]** So, that's that's how it works.

**[01:19:02]** So, that's that's how it works. In fact, if you are curious, I would

**[01:19:05]** In fact, if you are curious, I would

**[01:19:05]** In fact, if you are curious, I would recommend I I'll try to do this later

**[01:19:07]** recommend I I'll try to do this later

**[01:19:07]** recommend I I'll try to do this later on, but I would recommend that uh try to

**[01:19:10]** on, but I would recommend that uh try to

**[01:19:10]** on, but I would recommend that uh try to fine-tune this model or train it from

**[01:19:13]** fine-tune this model or train it from

**[01:19:13]** fine-tune this model or train it from scratch if you have some resource in for

**[01:19:15]** scratch if you have some resource in for

**[01:19:15]** scratch if you have some resource in for a smaller data set. Um and use a

**[01:19:18]** a smaller data set. Um and use a

**[01:19:18]** a smaller data set. Um and use a different patch size uh uh so let's say

**[01:19:21]** different patch size uh uh so let's say

**[01:19:22]** different patch size uh uh so let's say start with a patch size of four, right?

**[01:19:24]** start with a patch size of four, right?

**[01:19:24]** start with a patch size of four, right? And uh you know try to see that how it

**[01:19:26]** And uh you know try to see that how it

**[01:19:26]** And uh you know try to see that how it works.

**[01:19:28]** works.

**[01:19:28]** works. uh I have lot of assumptions uh on that

**[01:19:31]** uh I have lot of assumptions uh on that

**[01:19:31]** uh I have lot of assumptions uh on that but this will give you a lot of clarity

**[01:19:33]** but this will give you a lot of clarity

**[01:19:33]** but this will give you a lot of clarity of how uh the semantic search things

**[01:19:36]** of how uh the semantic search things

**[01:19:36]** of how uh the semantic search things work and why that matrix max matrix

**[01:19:38]** work and why that matrix max matrix

**[01:19:38]** work and why that matrix max matrix multiplication that we have done right

**[01:19:40]** multiplication that we have done right

**[01:19:40]** multiplication that we have done right why that is a good technique

**[01:19:42]** why that is a good technique

**[01:19:42]** why that is a good technique uh uh because imagine

**[01:19:46]** uh uh because imagine

**[01:19:46]** uh uh because imagine you have uploaded your data set is the

**[01:19:49]** you have uploaded your data set is the

**[01:19:49]** you have uploaded your data set is the attention you all you need paper and you

**[01:19:51]** attention you all you need paper and you

**[01:19:51]** attention you all you need paper and you ask a question about what is positional

**[01:19:55]** ask a question about what is positional

**[01:19:55]** ask a question about what is positional embedding now this positional embedding

**[01:19:58]** embedding now this positional embedding

**[01:19:58]** embedding now this positional embedding This text is there in lot of pages


### [01:20:00 - 01:21:00]

**[01:20:00]** This text is there in lot of pages

**[01:20:00]** This text is there in lot of pages almost all the pages. It should not give

**[01:20:02]** almost all the pages. It should not give

**[01:20:02]** almost all the pages. It should not give me all the pages. Right? So it should

**[01:20:04]** me all the pages. Right? So it should

**[01:20:04]** me all the pages. Right? So it should give me the page where there is an

**[01:20:06]** give me the page where there is an

**[01:20:06]** give me the page where there is an actual information of positional

**[01:20:08]** actual information of positional

**[01:20:08]** actual information of positional embedding is there. Right? And when you

**[01:20:11]** embedding is there. Right? And when you

**[01:20:11]** embedding is there. Right? And when you when you think through that you will

**[01:20:13]** when you think through that you will

**[01:20:13]** when you think through that you will find out that the ma max multiplication

**[01:20:15]** find out that the ma max multiplication

**[01:20:15]** find out that the ma max multiplication that that we have done right that

**[01:20:17]** that that we have done right that

**[01:20:17]** that that we have done right that actually takes care of that that uh it

**[01:20:19]** actually takes care of that that uh it

**[01:20:19]** actually takes care of that that uh it will just show you the page where all

**[01:20:22]** will just show you the page where all

**[01:20:22]** will just show you the page where all the tokens of your query has the maximum

**[01:20:25]** the tokens of your query has the maximum

**[01:20:25]** the tokens of your query has the maximum similarity with a particular page not

**[01:20:28]** similarity with a particular page not

**[01:20:28]** similarity with a particular page not just one chunk of your question with

**[01:20:31]** just one chunk of your question with

**[01:20:31]** just one chunk of your question with just one patch of your page you getting

**[01:20:34]** just one patch of your page you getting

**[01:20:34]** just one patch of your page you getting what I'm saying otherwise you know when

**[01:20:36]** what I'm saying otherwise you know when

**[01:20:36]** what I'm saying otherwise you know when you say top five it will give you any

**[01:20:38]** you say top five it will give you any

**[01:20:38]** you say top five it will give you any five random pages where this positional

**[01:20:40]** five random pages where this positional

**[01:20:40]** five random pages where this positional embedding is written. So just give it a

**[01:20:42]** embedding is written. So just give it a

**[01:20:42]** embedding is written. So just give it a shot.

**[01:20:44]** shot.

**[01:20:44]** shot. >> Yes sir. Yeah.

**[01:20:46]** >> Yes sir. Yeah.

**[01:20:46]** >> Yes sir. Yeah. >> Is there any sort of hybrid approach

**[01:20:48]** >> Is there any sort of hybrid approach

**[01:20:48]** >> Is there any sort of hybrid approach where you can process

**[01:20:55]** image?

**[01:20:55]** image? This is something that uh one of my

**[01:20:57]** This is something that uh one of my

**[01:20:57]** This is something that uh one of my teammate started to work on uh where we


### [01:21:00 - 01:22:00]

**[01:21:00]** teammate started to work on uh where we

**[01:21:00]** teammate started to work on uh where we are trying to use u call along with a

**[01:21:03]** are trying to use u call along with a

**[01:21:03]** are trying to use u call along with a traditional technique and the way that

**[01:21:05]** traditional technique and the way that

**[01:21:05]** traditional technique and the way that we are trying to do this is based on the

**[01:21:08]** we are trying to do this is based on the

**[01:21:08]** we are trying to do this is based on the question that we are getting and while

**[01:21:10]** question that we are getting and while

**[01:21:10]** question that we are getting and while we are doing the pre-processing and uh

**[01:21:12]** we are doing the pre-processing and uh

**[01:21:12]** we are doing the pre-processing and uh storing the embeddings we are trying to

**[01:21:15]** storing the embeddings we are trying to

**[01:21:15]** storing the embeddings we are trying to store uh in a different way like not for

**[01:21:18]** store uh in a different way like not for

**[01:21:18]** store uh in a different way like not for all the data that we are using call pal

**[01:21:20]** all the data that we are using call pal

**[01:21:20]** all the data that we are using call pal just for few data we are using call pal

**[01:21:22]** just for few data we are using call pal

**[01:21:22]** just for few data we are using call pal for the rest of the data we are just

**[01:21:23]** for the rest of the data we are just

**[01:21:23]** for the rest of the data we are just using the traditional technique

**[01:21:25]** using the traditional technique

**[01:21:25]** using the traditional technique But for a particular data set we just

**[01:21:26]** But for a particular data set we just

**[01:21:26]** But for a particular data set we just use one single model. We cannot just go

**[01:21:28]** use one single model. We cannot just go

**[01:21:28]** use one single model. We cannot just go into that okay first five pages of this

**[01:21:30]** into that okay first five pages of this

**[01:21:30]** into that okay first five pages of this document we will use call pal the next

**[01:21:32]** document we will use call pal the next

**[01:21:32]** document we will use call pal the next five pages we will use the traditional

**[01:21:34]** five pages we will use the traditional

**[01:21:34]** five pages we will use the traditional technique that's not how you know uh we

**[01:21:38]** technique that's not how you know uh we

**[01:21:38]** technique that's not how you know uh we are exploring but we are kind of trying

**[01:21:41]** are exploring but we are kind of trying

**[01:21:41]** are exploring but we are kind of trying to use two different approach in the

**[01:21:44]** to use two different approach in the

**[01:21:44]** to use two different approach in the same uh uh architecture. But this is we

**[01:21:46]** same uh uh architecture. But this is we

**[01:21:46]** same uh uh architecture. But this is we are using because the data set that we

**[01:21:48]** are using because the data set that we

**[01:21:48]** are using because the data set that we got from the customer they started off

**[01:21:50]** got from the customer they started off

**[01:21:50]** got from the customer they started off with a requirement certain requirement

**[01:21:52]** with a requirement certain requirement

**[01:21:52]** with a requirement certain requirement then it changed. It changed means it

**[01:21:53]** then it changed. It changed means it

**[01:21:54]** then it changed. It changed means it appended and now when the new request

**[01:21:56]** appended and now when the new request

**[01:21:56]** appended and now when the new request came the data set is completely

**[01:21:57]** came the data set is completely

**[01:21:57]** came the data set is completely different but they want a one unified

**[01:21:59]** different but they want a one unified

**[01:21:59]** different but they want a one unified system. So that's why we are just


### [01:22:00 - 01:23:00]

**[01:22:00]** system. So that's why we are just

**[01:22:00]** system. So that's why we are just checking the question is coming from

**[01:22:02]** checking the question is coming from

**[01:22:02]** checking the question is coming from where and we are storing some metadata

**[01:22:04]** where and we are storing some metadata

**[01:22:04]** where and we are storing some metadata to identify this question should go from

**[01:22:06]** to identify this question should go from

**[01:22:06]** to identify this question should go from this space or that space. Uh but nothing

**[01:22:09]** this space or that space. Uh but nothing

**[01:22:09]** this space or that space. Uh but nothing beyond that that I have seen. I've seen

**[01:22:11]** beyond that that I have seen. I've seen

**[01:22:11]** beyond that that I have seen. I've seen either this or that.

**[01:22:12]** either this or that.

**[01:22:12]** either this or that. >> Yeah. Yes sir.

**[01:22:14]** >> Yeah. Yes sir.

**[01:22:14]** >> Yeah. Yes sir. >> Did you have to find

**[01:22:17]** >> Did you have to find

**[01:22:17]** >> Did you have to find poly model to for it to work well?

**[01:22:19]** poly model to for it to work well?

**[01:22:19]** poly model to for it to work well? >> No I have not done that. So this is

**[01:22:21]** >> No I have not done that. So this is

**[01:22:21]** >> No I have not done that. So this is these are all fine-tuned models. You can

**[01:22:23]** these are all fine-tuned models. You can

**[01:22:23]** these are all fine-tuned models. You can just make use of this. I forgot the data

**[01:22:26]** just make use of this. I forgot the data

**[01:22:26]** just make use of this. I forgot the data set that they have used. You can read

**[01:22:27]** set that they have used. You can read

**[01:22:27]** set that they have used. You can read the research paper on that. The link is

**[01:22:30]** the research paper on that. The link is

**[01:22:30]** the research paper on that. The link is there. But you don't have to fine-tune

**[01:22:31]** there. But you don't have to fine-tune

**[01:22:31]** there. But you don't have to fine-tune that. Can you do that? Yes, of course

**[01:22:33]** that. Can you do that? Yes, of course

**[01:22:33]** that. Can you do that? Yes, of course you can do a finetuning. That's what I

**[01:22:34]** you can do a finetuning. That's what I

**[01:22:34]** you can do a finetuning. That's what I was referring to him. I myself have not

**[01:22:36]** was referring to him. I myself have not

**[01:22:36]** was referring to him. I myself have not done that. But I will certainly try this

**[01:22:38]** done that. But I will certainly try this

**[01:22:38]** done that. But I will certainly try this out uh to fine-tune that. That's a good

**[01:22:41]** out uh to fine-tune that. That's a good

**[01:22:41]** out uh to fine-tune that. That's a good exercise.

**[01:22:42]** exercise.

**[01:22:42]** exercise. >> So it worked well for your use case.

**[01:22:43]** >> So it worked well for your use case.

**[01:22:43]** >> So it worked well for your use case. >> Yeah. It just worked fine. Yeah. Yeah.

**[01:22:45]** >> Yeah. It just worked fine. Yeah. Yeah.

**[01:22:45]** >> Yeah. It just worked fine. Yeah. Yeah. Yeah. Yeah. because I used a standard

**[01:22:48]** Yeah. Yeah. because I used a standard

**[01:22:48]** Yeah. Yeah. because I used a standard textbook which are publicly available uh

**[01:22:51]** textbook which are publicly available uh

**[01:22:51]** textbook which are publicly available uh but convoluted data try to do that with

**[01:22:54]** but convoluted data try to do that with

**[01:22:54]** but convoluted data try to do that with IKEA data set IKEA data set is good

**[01:22:56]** IKEA data set IKEA data set is good

**[01:22:56]** IKEA data set IKEA data set is good because you cannot use an OCR based

**[01:22:59]** because you cannot use an OCR based

**[01:22:59]** because you cannot use an OCR based techniques in that data set and because


### [01:23:00 - 01:24:00]

**[01:23:01]** techniques in that data set and because

**[01:23:01]** techniques in that data set and because that's a very strange sparse data set

**[01:23:03]** that's a very strange sparse data set

**[01:23:03]** that's a very strange sparse data set and that will give you a good intuition

**[01:23:05]** and that will give you a good intuition

**[01:23:05]** and that will give you a good intuition that okay this is you know you can

**[01:23:07]** that okay this is you know you can

**[01:23:07]** that okay this is you know you can understand only you can answer those

**[01:23:09]** understand only you can answer those

**[01:23:09]** understand only you can answer those questions if you if somebody asks you

**[01:23:11]** questions if you if somebody asks you

**[01:23:11]** questions if you if somebody asks you that question from that uh IKEA uh

**[01:23:13]** that question from that uh IKEA uh

**[01:23:13]** that question from that uh IKEA uh manual you can do that not um a computer

**[01:23:17]** manual you can do that not um a computer

**[01:23:17]** manual you can do that not um a computer if you use a traditional technique. So

**[01:23:19]** if you use a traditional technique. So

**[01:23:19]** if you use a traditional technique. So that actually a good data point to make

**[01:23:21]** that actually a good data point to make

**[01:23:21]** that actually a good data point to make use of this. Okay.

**[01:23:24]** use of this. Okay.

**[01:23:24]** use of this. Okay. All right. Thank you so much everyone

**[01:23:26]** All right. Thank you so much everyone

**[01:23:26]** All right. Thank you so much everyone for uh uh coming. I really appreciate

**[01:23:38]** and and one last thing is if you need u

**[01:23:38]** and and one last thing is if you need u uh any AWS credit for any of your

**[01:23:40]** uh any AWS credit for any of your

**[01:23:40]** uh any AWS credit for any of your project uh just ping me on LinkedIn.

**[01:23:42]** project uh just ping me on LinkedIn.

**[01:23:42]** project uh just ping me on LinkedIn. I'll share a few credits. Okay. Even if

**[01:23:44]** I'll share a few credits. Okay. Even if

**[01:23:44]** I'll share a few credits. Okay. Even if you need more, I can give you more.


