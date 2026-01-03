# Introduction to LLM serving with SGLang - Philip Kiely and Yineng Zhang, Baseten

**Video URL:** https://www.youtube.com/watch?v=Ahtaha9fEM0

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Hey everyone. Um, so we're going to

**[00:16]** Hey everyone. Um, so we're going to we're going to go ahead and get started

**[00:18]** we're going to go ahead and get started

**[00:18]** we're going to go ahead and get started here. Um, we've got a nice close group

**[00:20]** here. Um, we've got a nice close group

**[00:20]** here. Um, we've got a nice close group here today. Um, and that's I think to

**[00:23]** here today. Um, and that's I think to

**[00:24]** here today. Um, and that's I think to everyone's benefit. Um, this workshop is

**[00:26]** everyone's benefit. Um, this workshop is

**[00:26]** everyone's benefit. Um, this workshop is really for you. You know, I love the

**[00:28]** really for you. You know, I love the

**[00:28]** really for you. You know, I love the sound of my own voice. I love talking.

**[00:29]** sound of my own voice. I love talking.

**[00:29]** sound of my own voice. I love talking. That's why I'm a developer advocate. Um,

**[00:31]** That's why I'm a developer advocate. Um,

**[00:32]** That's why I'm a developer advocate. Um, but the, you know, the the purpose of

**[00:34]** but the, you know, the the purpose of

**[00:34]** but the, you know, the the purpose of this workshop is to help you get

**[00:35]** this workshop is to help you get

**[00:35]** this workshop is to help you get comfortable with SG lang. So, if you

**[00:38]** comfortable with SG lang. So, if you

**[00:38]** comfortable with SG lang. So, if you have questions, if you have ideas, if

**[00:40]** have questions, if you have ideas, if

**[00:40]** have questions, if you have ideas, if you have bugs, uh, askang um or or me.

**[00:44]** you have bugs, uh, askang um or or me.

**[00:44]** you have bugs, uh, askang um or or me. Uh, and we're we're definitely going to

**[00:46]** Uh, and we're we're definitely going to

**[00:46]** Uh, and we're we're definitely going to be able to tailor this workshop to you

**[00:49]** be able to tailor this workshop to you

**[00:49]** be able to tailor this workshop to you and your interests and what you're

**[00:51]** and your interests and what you're

**[00:51]** and your interests and what you're working on. Um, so the title of this

**[00:53]** working on. Um, so the title of this

**[00:53]** working on. Um, so the title of this workshop is an introduction to LLM

**[00:55]** workshop is an introduction to LLM

**[00:56]** workshop is an introduction to LLM serving with SG Lang. Um we're going to

**[00:58]** serving with SG Lang. Um we're going to

**[00:58]** serving with SG Lang. Um we're going to be uh you know talking about SG Lang and


### [01:00 - 02:00]

**[01:02]** be uh you know talking about SG Lang and

**[01:02]** be uh you know talking about SG Lang and little quick introduction. Um so my

**[01:04]** little quick introduction. Um so my

**[01:04]** little quick introduction. Um so my co-speaker Hu Yang um is a core

**[01:07]** co-speaker Hu Yang um is a core

**[01:07]** co-speaker Hu Yang um is a core maintainer of SG lang. Um has been

**[01:09]** maintainer of SG lang. Um has been

**[01:09]** maintainer of SG lang. Um has been involved with LMS or for quite a while

**[01:12]** involved with LMS or for quite a while

**[01:12]** involved with LMS or for quite a while now. Um h is the sort of like influence

**[01:15]** now. Um h is the sort of like influence

**[01:15]** now. Um h is the sort of like influence lead on the project. Um previously

**[01:18]** lead on the project. Um previously

**[01:18]** lead on the project. Um previously worked at um BYU and some other places

**[01:21]** worked at um BYU and some other places

**[01:21]** worked at um BYU and some other places and also is uh you're an author of a few

**[01:24]** and also is uh you're an author of a few

**[01:24]** and also is uh you're an author of a few papers um including flash and fur. Um,

**[01:27]** papers um including flash and fur. Um,

**[01:27]** papers um including flash and fur. Um, and I'm Philip and I got a B+ in linear

**[01:29]** and I'm Philip and I got a B+ in linear

**[01:29]** and I'm Philip and I got a B+ in linear algebra. So, um, whether you know,

**[01:31]** algebra. So, um, whether you know,

**[01:31]** algebra. So, um, whether you know, whether you're coming in here and you're

**[01:33]** whether you're coming in here and you're

**[01:33]** whether you're coming in here and you're super cracked or you're brand new at SG

**[01:35]** super cracked or you're brand new at SG

**[01:35]** super cracked or you're brand new at SG Lang, we're going to have something for

**[01:37]** Lang, we're going to have something for

**[01:37]** Lang, we're going to have something for you. Whatever your skill level, uh, this

**[01:39]** you. Whatever your skill level, uh, this

**[01:40]** you. Whatever your skill level, uh, this is this is the place to be. Um, so what

**[01:42]** is this is the place to be. Um, so what

**[01:42]** is this is the place to be. Um, so what are we going to do today? We're going

**[01:44]** are we going to do today? We're going

**[01:44]** are we going to do today? We're going to, you know, introduce SG Lang, get set

**[01:46]** to, you know, introduce SG Lang, get set

**[01:46]** to, you know, introduce SG Lang, get set up a little bit. Um, we're going to talk

**[01:48]** up a little bit. Um, we're going to talk

**[01:48]** up a little bit. Um, we're going to talk about the history of SG Lang. um talk

**[01:51]** about the history of SG Lang. um talk

**[01:51]** about the history of SG Lang. um talk about deploying your first model, bunch

**[01:53]** about deploying your first model, bunch

**[01:53]** about deploying your first model, bunch of things you can do to optimize

**[01:55]** of things you can do to optimize

**[01:55]** of things you can do to optimize performance after that. And then we're

**[01:57]** performance after that. And then we're

**[01:57]** performance after that. And then we're also going to talk a little bit about

**[01:58]** also going to talk a little bit about

**[01:58]** also going to talk a little bit about the SGLAN community and how you can get


### [02:00 - 03:00]

**[02:01]** the SGLAN community and how you can get

**[02:01]** the SGLAN community and how you can get involved and even do a little bit of a

**[02:03]** involved and even do a little bit of a

**[02:03]** involved and even do a little bit of a tour of the codebase in case you want to

**[02:04]** tour of the codebase in case you want to

**[02:04]** tour of the codebase in case you want to start making open source contributions.

**[02:07]** start making open source contributions.

**[02:07]** start making open source contributions. Um so by way of introduction uh let's

**[02:10]** Um so by way of introduction uh let's

**[02:10]** Um so by way of introduction uh let's see what is SG Lang. So SG lang is an

**[02:14]** see what is SG Lang. So SG lang is an

**[02:14]** see what is SG Lang. So SG lang is an open-source fasterving framework for

**[02:16]** open-source fasterving framework for

**[02:16]** open-source fasterving framework for large language models and large vision

**[02:18]** large language models and large vision

**[02:18]** large language models and large vision models. Generally you use SG lang in a

**[02:21]** models. Generally you use SG lang in a

**[02:21]** models. Generally you use SG lang in a sentence along with either VLM or tensor

**[02:23]** sentence along with either VLM or tensor

**[02:23]** sentence along with either VLM or tensor RTLM. Um it's one of the multiple

**[02:26]** RTLM. Um it's one of the multiple

**[02:26]** RTLM. Um it's one of the multiple options for serving models in

**[02:28]** options for serving models in

**[02:28]** options for serving models in production. So the question is um why

**[02:32]** production. So the question is um why

**[02:32]** production. So the question is um why SGLANG like why should we uh you know

**[02:35]** SGLANG like why should we uh you know

**[02:35]** SGLANG like why should we uh you know invest in in learning and and building

**[02:37]** invest in in learning and and building

**[02:37]** invest in in learning and and building this library? Um and you know first off

**[02:41]** this library? Um and you know first off

**[02:41]** this library? Um and you know first off it's it's very performant. SGLANG offers

**[02:43]** it's it's very performant. SGLANG offers

**[02:43]** it's it's very performant. SGLANG offers excellent performance um on a wide

**[02:45]** excellent performance um on a wide

**[02:45]** excellent performance um on a wide variety of GPUs. It's production ready

**[02:47]** variety of GPUs. It's production ready

**[02:47]** variety of GPUs. It's production ready out of the box. Um, it's got day zero

**[02:50]** out of the box. Um, it's got day zero

**[02:50]** out of the box. Um, it's got day zero support for new model releases from uh

**[02:53]** support for new model releases from uh

**[02:53]** support for new model releases from uh labs like Quen and DeepSeek and it's got

**[02:55]** labs like Quen and DeepSeek and it's got

**[02:55]** labs like Quen and DeepSeek and it's got a great community, strong open source

**[02:57]** a great community, strong open source

**[02:57]** a great community, strong open source ethos. Um, which means that if something


### [03:00 - 04:00]

**[03:00]** ethos. Um, which means that if something

**[03:00]** ethos. Um, which means that if something is broken in SGLang, if you don't like

**[03:01]** is broken in SGLang, if you don't like

**[03:02]** is broken in SGLang, if you don't like something, you can fix it. Uh, which is

**[03:04]** something, you can fix it. Uh, which is

**[03:04]** something, you can fix it. Uh, which is which is pretty huge advantage.

**[03:07]** which is pretty huge advantage.

**[03:07]** which is pretty huge advantage. Um, so who uses SG lang? Well, uh, we do

**[03:10]** Um, so who uses SG lang? Well, uh, we do

**[03:10]** Um, so who uses SG lang? Well, uh, we do at base 10. Um we use it as part of our

**[03:13]** at base 10. Um we use it as part of our

**[03:13]** at base 10. Um we use it as part of our inference stack for a variety of

**[03:15]** inference stack for a variety of

**[03:15]** inference stack for a variety of different models that we run. Um we also

**[03:18]** different models that we run. Um we also

**[03:18]** different models that we run. Um we also um see SGLang being used very heavily by

**[03:21]** um see SGLang being used very heavily by

**[03:21]** um see SGLang being used very heavily by XAI for their Glock models as well as a

**[03:24]** XAI for their Glock models as well as a

**[03:24]** XAI for their Glock models as well as a wide variety of inference providers and

**[03:27]** wide variety of inference providers and

**[03:27]** wide variety of inference providers and cloud providers and research labs,

**[03:29]** cloud providers and research labs,

**[03:30]** cloud providers and research labs, universities and even product companies

**[03:31]** universities and even product companies

**[03:31]** universities and even product companies like Koser.

**[03:34]** like Koser.

**[03:34]** like Koser. So quick history of SG Lang. Um, it's

**[03:37]** So quick history of SG Lang. Um, it's

**[03:37]** So quick history of SG Lang. Um, it's honestly really impressive to me how

**[03:39]** honestly really impressive to me how

**[03:39]** honestly really impressive to me how quickly this project has come up and

**[03:41]** quickly this project has come up and

**[03:41]** quickly this project has come up and gotten big. Um, if you look at, you

**[03:43]** gotten big. Um, if you look at, you

**[03:43]** gotten big. Um, if you look at, you know, the archive paper was released in

**[03:45]** know, the archive paper was released in

**[03:45]** know, the archive paper was released in December 2023. That's 18 months ago. So,

**[03:48]** December 2023. That's 18 months ago. So,

**[03:48]** December 2023. That's 18 months ago. So, in just 18 months, this project has gone

**[03:50]** in just 18 months, this project has gone

**[03:50]** in just 18 months, this project has gone from a paper to 15,000 GitHub stars

**[03:53]** from a paper to 15,000 GitHub stars

**[03:53]** from a paper to 15,000 GitHub stars almost. You should all go star it so

**[03:55]** almost. You should all go star it so

**[03:55]** almost. You should all go star it so that we can get a little closer. Um, and

**[03:58]** that we can get a little closer. Um, and

**[03:58]** that we can get a little closer. Um, and it's uh, you know, supporting all of


### [04:00 - 05:00]

**[04:00]** it's uh, you know, supporting all of

**[04:00]** it's uh, you know, supporting all of those logos, all those companies we saw

**[04:02]** those logos, all those companies we saw

**[04:02]** those logos, all those companies we saw on the last slide. Um, it's got a

**[04:05]** on the last slide. Um, it's got a

**[04:05]** on the last slide. Um, it's got a growing and vibrant community. Um, it's

**[04:07]** growing and vibrant community. Um, it's

**[04:07]** growing and vibrant community. Um, it's got international adoption. So, yeah,

**[04:10]** got international adoption. So, yeah,

**[04:10]** got international adoption. So, yeah, incredibly impressive what the team has

**[04:11]** incredibly impressive what the team has

**[04:11]** incredibly impressive what the team has done in that time. Um, and I'm going to

**[04:13]** done in that time. Um, and I'm going to

**[04:13]** done in that time. Um, and I'm going to turn over to Yianang now to talk a

**[04:15]** turn over to Yianang now to talk a

**[04:15]** turn over to Yianang now to talk a little bit more about that history and

**[04:16]** little bit more about that history and

**[04:16]** little bit more about that history and also like how you got involved in the

**[04:18]** also like how you got involved in the

**[04:18]** also like how you got involved in the project. Okay. Hello, I'm Ena. I'm the

**[04:22]** project. Okay. Hello, I'm Ena. I'm the

**[04:22]** project. Okay. Hello, I'm Ena. I'm the co-developer of the Estelon project and

**[04:24]** co-developer of the Estelon project and

**[04:24]** co-developer of the Estelon project and I'm also the software engineer at Bon.

**[04:28]** I'm also the software engineer at Bon.

**[04:28]** I'm also the software engineer at Bon. And uh before I joined bon I work as I

**[04:31]** And uh before I joined bon I work as I

**[04:31]** And uh before I joined bon I work as I worked at at mron and at that time I

**[04:34]** worked at at mron and at that time I

**[04:34]** worked at at mron and at that time I worked for the internal uh clickth

**[04:37]** worked for the internal uh clickth

**[04:37]** worked for the internal uh clickth through rate ranking model optimization

**[04:39]** through rate ranking model optimization

**[04:39]** through rate ranking model optimization and inference optimization and at that

**[04:43]** and inference optimization and at that

**[04:43]** and inference optimization and at that time the creator of named lei just reach

**[04:47]** time the creator of named lei just reach

**[04:47]** time the creator of named lei just reach out and then we we have a yeah Google

**[04:50]** out and then we we have a yeah Google

**[04:50]** out and then we we have a yeah Google meet. So at that time I left mine I

**[04:54]** meet. So at that time I left mine I

**[04:54]** meet. So at that time I left mine I joined project. So I worked closely with

**[04:57]** joined project. So I worked closely with

**[04:57]** joined project. So I worked closely with Le and Ying on Estelon. Also you know


### [05:00 - 06:00]

**[05:00]** Le and Ying on Estelon. Also you know

**[05:00]** Le and Ying on Estelon. Also you know Estelon use flash infer heavily because

**[05:03]** Estelon use flash infer heavily because

**[05:03]** Estelon use flash infer heavily because we use flash infer as the attention ko

**[05:06]** we use flash infer as the attention ko

**[05:06]** we use flash infer as the attention ko library and the sampling kernel library.

**[05:09]** library and the sampling kernel library.

**[05:09]** library and the sampling kernel library. So I also worked with Zuha on the flash

**[05:12]** So I also worked with Zuha on the flash

**[05:12]** So I also worked with Zuha on the flash infer project and yeah currently I'm the

**[05:16]** infer project and yeah currently I'm the

**[05:16]** infer project and yeah currently I'm the co-maintainer of the project and I'm

**[05:18]** co-maintainer of the project and I'm

**[05:18]** co-maintainer of the project and I'm also the team member at LMC's or and

**[05:22]** also the team member at LMC's or and

**[05:22]** also the team member at LMC's or and that's the uh little point of trivia

**[05:24]** that's the uh little point of trivia

**[05:24]** that's the uh little point of trivia that's the same LMIS or that just got

**[05:26]** that's the same LMIS or that just got

**[05:26]** that's the same LMIS or that just got hund00 million to build chatbot Arena uh

**[05:29]** hund00 million to build chatbot Arena uh

**[05:29]** hund00 million to build chatbot Arena uh from A16Z. Um I learned that while I was

**[05:33]** from A16Z. Um I learned that while I was

**[05:33]** from A16Z. Um I learned that while I was putting together the slides for this

**[05:34]** putting together the slides for this

**[05:34]** putting together the slides for this talk. So, um, if you were here early,

**[05:37]** talk. So, um, if you were here early,

**[05:37]** talk. So, um, if you were here early, you were able to, um, scan this QR code

**[05:40]** you were able to, um, scan this QR code

**[05:40]** you were able to, um, scan this QR code and get everything set up for the

**[05:42]** and get everything set up for the

**[05:42]** and get everything set up for the workshop. Um, if not, uh, definitely

**[05:45]** workshop. Um, if not, uh, definitely

**[05:45]** workshop. Um, if not, uh, definitely grab that right now. Um, you've got the

**[05:47]** grab that right now. Um, you've got the

**[05:47]** grab that right now. Um, you've got the QR code, you've got the URL that takes

**[05:49]** QR code, you've got the URL that takes

**[05:49]** QR code, you've got the URL that takes you to the same place. Does anyone still

**[05:52]** you to the same place. Does anyone still

**[05:52]** you to the same place. Does anyone still need the QR code? Um, okay, I've got a

**[05:55]** need the QR code? Um, okay, I've got a

**[05:55]** need the QR code? Um, okay, I've got a couple people still.

**[05:57]** couple people still.

**[05:57]** couple people still. All right.

**[05:59]** All right.


### [06:00 - 07:00]

**[06:00]** All right. [Music]

**[06:01]** [Music]

**[06:01]** [Music] Anyone

**[06:09]** still need the QR code?

**[06:09]** still need the QR code? Going once. Going twice. Yep.

**[06:20]** To uh folks watching at home, you've got

**[06:20]** To uh folks watching at home, you've got this great button on YouTube. Uh it's

**[06:23]** this great button on YouTube. Uh it's

**[06:23]** this great button on YouTube. Uh it's called the fast forward button. So you

**[06:24]** called the fast forward button. So you

**[06:24]** called the fast forward button. So you can just skip this part.

**[06:40]** All right, we uh looking good. Um if you

**[06:40]** All right, we uh looking good. Um if you uh if you need this again, uh just just

**[06:42]** uh if you need this again, uh just just

**[06:42]** uh if you need this again, uh just just let me know. I'll uh throw it back up

**[06:44]** let me know. I'll uh throw it back up

**[06:44]** let me know. I'll uh throw it back up there. So, we're going to talk about um

**[06:47]** there. So, we're going to talk about um

**[06:47]** there. So, we're going to talk about um how to deploy your first model um on

**[06:51]** how to deploy your first model um on

**[06:51]** how to deploy your first model um on SGLANG. Um so if you um go over to the

**[06:55]** SGLANG. Um so if you um go over to the

**[06:55]** SGLANG. Um so if you um go over to the GitHub.


### [07:00 - 08:00]

**[07:11]** So um in this step we're just going to

**[07:11]** So um in this step we're just going to get familiar with the uh basic mechanics

**[07:14]** get familiar with the uh basic mechanics

**[07:14]** get familiar with the uh basic mechanics of SG lang. Um, sglang is basically just

**[07:18]** of SG lang. Um, sglang is basically just

**[07:18]** of SG lang. Um, sglang is basically just like a server command um that you're

**[07:20]** like a server command um that you're

**[07:20]** like a server command um that you're going to run in your Docker container.

**[07:23]** going to run in your Docker container.

**[07:23]** going to run in your Docker container. There's a little bit of sort of

**[07:25]** There's a little bit of sort of

**[07:25]** There's a little bit of sort of difference uh with using it the way

**[07:27]** difference uh with using it the way

**[07:27]** difference uh with using it the way we're going to use it in the workshop

**[07:28]** we're going to use it in the workshop

**[07:28]** we're going to use it in the workshop right now versus how you might use it if

**[07:30]** right now versus how you might use it if

**[07:30]** right now versus how you might use it if you're working directly on a GPU. The

**[07:33]** you're working directly on a GPU. The

**[07:33]** you're working directly on a GPU. The difference is you're using something

**[07:35]** difference is you're using something

**[07:35]** difference is you're using something called truss to package it. Basically,

**[07:37]** called truss to package it. Basically,

**[07:37]** called truss to package it. Basically, you're putting in your SGLang uh

**[07:39]** you're putting in your SGLang uh

**[07:39]** you're putting in your SGLang uh dependencies and your command into this

**[07:42]** dependencies and your command into this

**[07:42]** dependencies and your command into this YAML file. you're bundling it and you're

**[07:45]** YAML file. you're bundling it and you're

**[07:45]** YAML file. you're bundling it and you're shipping it up to a GPU. Uh the reason

**[07:47]** shipping it up to a GPU. Uh the reason

**[07:47]** shipping it up to a GPU. Uh the reason we are using trust is because that is

**[07:50]** we are using trust is because that is

**[07:50]** we are using trust is because that is the way that you can get on base 10. And

**[07:51]** the way that you can get on base 10. And

**[07:51]** the way that you can get on base 10. And the reason you are using ben is because

**[07:53]** the reason you are using ben is because

**[07:53]** the reason you are using ben is because that is the only company on earth that

**[07:55]** that is the only company on earth that

**[07:55]** that is the only company on earth that will give me free GPUs because I work

**[07:57]** will give me free GPUs because I work

**[07:57]** will give me free GPUs because I work there. Um so we're uh we're going to be


### [08:00 - 09:00]

**[08:00]** there. Um so we're uh we're going to be

**[08:00]** there. Um so we're uh we're going to be working um on all these examples on L4

**[08:03]** working um on all these examples on L4

**[08:03]** working um on all these examples on L4 GPUs uh because they are cheap and

**[08:05]** GPUs uh because they are cheap and

**[08:05]** GPUs uh because they are cheap and abundant um and they also support FP8.

**[08:09]** abundant um and they also support FP8.

**[08:09]** abundant um and they also support FP8. Uh but this same uh the same product

**[08:11]** Uh but this same uh the same product

**[08:11]** Uh but this same uh the same product works on H100 um H200 and Blackwell's

**[08:15]** works on H100 um H200 and Blackwell's

**[08:15]** works on H100 um H200 and Blackwell's coming soon. Yeah. Yeah. Yeah. Coming

**[08:17]** coming soon. Yeah. Yeah. Yeah. Coming

**[08:17]** coming soon. Yeah. Yeah. Yeah. Coming soon. Um so yeah, it's going to be

**[08:20]** soon. Um so yeah, it's going to be

**[08:20]** soon. Um so yeah, it's going to be basically like the same principles. Um

**[08:23]** basically like the same principles. Um

**[08:23]** basically like the same principles. Um if you go through here um the uh the

**[08:27]** if you go through here um the uh the

**[08:27]** if you go through here um the uh the configuration um you can actually in

**[08:29]** configuration um you can actually in

**[08:29]** configuration um you can actually in your trust config you can change the um

**[08:33]** your trust config you can change the um

**[08:33]** your trust config you can change the um hardware type to H100 if you want. Um

**[08:36]** hardware type to H100 if you want. Um

**[08:36]** hardware type to H100 if you want. Um and

**[08:38]** and

**[08:38]** and uh in the yeah in the uh accelerator

**[08:41]** uh in the yeah in the uh accelerator

**[08:41]** uh in the yeah in the uh accelerator line right there. Um but yeah, so what

**[08:45]** line right there. Um but yeah, so what

**[08:45]** line right there. Um but yeah, so what is like the actual SGLang launch server

**[08:47]** is like the actual SGLang launch server

**[08:47]** is like the actual SGLang launch server command um that we're that we're running

**[08:50]** command um that we're that we're running

**[08:50]** command um that we're that we're running here. So it's basically just like a

**[08:53]** here. So it's basically just like a

**[08:53]** here. So it's basically just like a bunch of flags. That's the thing to

**[08:54]** bunch of flags. That's the thing to

**[08:54]** bunch of flags. That's the thing to understand about using SGLANG. It's all

**[08:56]** understand about using SGLANG. It's all

**[08:56]** understand about using SGLANG. It's all about knowing what flags are available,

**[08:59]** about knowing what flags are available,

**[08:59]** about knowing what flags are available, knowing what configuration options are


### [09:00 - 10:00]

**[09:00]** knowing what configuration options are

**[09:00]** knowing what configuration options are available, knowing the support matrix

**[09:03]** available, knowing the support matrix

**[09:03]** available, knowing the support matrix that exists for them, and knowing how

**[09:05]** that exists for them, and knowing how

**[09:05]** that exists for them, and knowing how they interact with each other. Um, if

**[09:07]** they interact with each other. Um, if

**[09:07]** they interact with each other. Um, if you, you know, turn on a major

**[09:10]** you, you know, turn on a major

**[09:10]** you, you know, turn on a major speculation algorithm, and then you also

**[09:12]** speculation algorithm, and then you also

**[09:12]** speculation algorithm, and then you also jack your batch size way up, well,

**[09:14]** jack your batch size way up, well,

**[09:14]** jack your batch size way up, well, that's probably not going to go so well

**[09:15]** that's probably not going to go so well

**[09:15]** that's probably not going to go so well for you. Um, but if you want to do say

**[09:18]** for you. Um, but if you want to do say

**[09:18]** for you. Um, but if you want to do say like your, you know, quantization along

**[09:20]** like your, you know, quantization along

**[09:20]** like your, you know, quantization along with some of these other optimizations,

**[09:22]** with some of these other optimizations,

**[09:22]** with some of these other optimizations, those play nice. Um, so yeah. Um, what

**[09:26]** those play nice. Um, so yeah. Um, what

**[09:26]** those play nice. Um, so yeah. Um, what we're going to do, um, this is the fun

**[09:28]** we're going to do, um, this is the fun

**[09:28]** we're going to do, um, this is the fun part of leading a workshop, um, is the

**[09:31]** part of leading a workshop, um, is the

**[09:31]** part of leading a workshop, um, is the part where we just like stand around

**[09:32]** part where we just like stand around

**[09:32]** part where we just like stand around watching you type. Um, what we're going

**[09:35]** watching you type. Um, what we're going

**[09:35]** watching you type. Um, what we're going to do is give everyone about 5 minutes

**[09:38]** to do is give everyone about 5 minutes

**[09:38]** to do is give everyone about 5 minutes to work through this first example. Um,

**[09:40]** to work through this first example. Um,

**[09:40]** to work through this first example. Um, we're going to circulate the room if you

**[09:42]** we're going to circulate the room if you

**[09:42]** we're going to circulate the room if you have any questions. Um, and then we're

**[09:44]** have any questions. Um, and then we're

**[09:44]** have any questions. Um, and then we're going to come back together after uh,

**[09:47]** going to come back together after uh,

**[09:47]** going to come back together after uh, running the first example. Sound good?

**[09:50]** running the first example. Sound good?

**[09:50]** running the first example. Sound good? All right, let's do it. Uh, can you cut

**[09:52]** All right, let's do it. Uh, can you cut

**[09:52]** All right, let's do it. Uh, can you cut the mics for five minutes?


### [10:00 - 11:00]

**[10:00]** Pause. Skip. It's It's great. They these

**[10:00]** Pause. Skip. It's It's great. They these buttons, they're magical.

**[10:09]** Has issues. Is anyone having issues

**[10:09]** Has issues. Is anyone having issues where you're like

**[10:10]** where you're like

**[10:10]** where you're like stuck trying to get into base 10? Um,

**[10:13]** stuck trying to get into base 10? Um,

**[10:13]** stuck trying to get into base 10? Um, you're in like a waiting room and it

**[10:14]** you're in like a waiting room and it

**[10:14]** you're in like a waiting room and it won't let you out. Um, if you are de if

**[10:17]** won't let you out. Um, if you are de if

**[10:17]** won't let you out. Um, if you are de if you are, uh, flag me. Um, if anyone is

**[10:19]** you are, uh, flag me. Um, if anyone is

**[10:19]** you are, uh, flag me. Um, if anyone is having issues where you're getting like

**[10:21]** having issues where you're getting like

**[10:22]** having issues where you're getting like an error in your code, please don't show

**[10:24]** an error in your code, please don't show

**[10:24]** an error in your code, please don't show me, show him.

**[10:31]** And a check on progress. Has anyone

**[10:31]** And a check on progress. Has anyone managed to get the first model deployed

**[10:33]** managed to get the first model deployed

**[10:33]** managed to get the first model deployed and running?

**[10:36]** and running?

**[10:36]** and running? It's deploying. Awesome. Let's hope it's

**[10:39]** It's deploying. Awesome. Let's hope it's

**[10:39]** It's deploying. Awesome. Let's hope it's deploying really fast.

**[10:42]** deploying really fast.

**[10:42]** deploying really fast. Let me let me take a look here. All

**[10:45]** Let me let me take a look here. All

**[10:45]** Let me let me take a look here. All right, sounds good. Can you uh take a

**[10:46]** right, sounds good. Can you uh take a

**[10:46]** right, sounds good. Can you uh take a look at the logs for me real quick?

**[10:56]** Wow, our Wi-Fi is just amazing here. I

**[10:56]** Wow, our Wi-Fi is just amazing here. I promise base 10 is usually faster than

**[10:58]** promise base 10 is usually faster than

**[10:58]** promise base 10 is usually faster than this.


### [11:00 - 12:00]

**[11:06]** Oh, okay. Well, it looks like it it came

**[11:06]** Oh, okay. Well, it looks like it it came up. Um so you can um you can use the um

**[11:13]** up. Um so you can um you can use the um

**[11:13]** up. Um so you can um you can use the um sample code

**[11:15]** sample code

**[11:15]** sample code um in call.py or call.ipy nb um or like

**[11:21]** um in call.py or call.ipy nb um or like

**[11:21]** um in call.py or call.ipy nb um or like you can just use an ordinary openi

**[11:23]** you can just use an ordinary openi

**[11:23]** you can just use an ordinary openi client um

**[11:27]** client um

**[11:27]** client um what you need to call it if you go back

**[11:29]** what you need to call it if you go back

**[11:29]** what you need to call it if you go back to your base 10 workspace with the model

**[11:32]** to your base 10 workspace with the model

**[11:32]** to your base 10 workspace with the model um what you need is uh scroll back up a

**[11:36]** um what you need is uh scroll back up a

**[11:36]** um what you need is uh scroll back up a little bit for me. You need that model

**[11:37]** little bit for me. You need that model

**[11:37]** little bit for me. You need that model ID. That's what's going to um unlock

**[11:41]** ID. That's what's going to um unlock

**[11:41]** ID. That's what's going to um unlock your calling code. Love it. Um that

**[11:44]** your calling code. Love it. Um that

**[11:44]** your calling code. Love it. Um that Yeah. Paste it in right there. Um you

**[11:47]** Yeah. Paste it in right there. Um you

**[11:47]** Yeah. Paste it in right there. Um you you'll need to run an act run an actual

**[11:50]** you'll need to run an act run an actual

**[11:50]** you'll need to run an act run an actual Jupyter notebook to to run that.

**[11:55]** Jupyter notebook to to run that.

**[11:55]** Jupyter notebook to to run that. All right, we've had our first

**[11:56]** All right, we've had our first

**[11:56]** All right, we've had our first successful deploy.


### [12:00 - 13:00]

**[12:00]** successful deploy.

**[12:00]** successful deploy. If you want to call it using the Open

**[12:02]** If you want to call it using the Open

**[12:02]** If you want to call it using the Open SDK, using the call.nb PYNB uh notebook.

**[12:06]** SDK, using the call.nb PYNB uh notebook.

**[12:06]** SDK, using the call.nb PYNB uh notebook. Um this thing up here, it's going to be

**[12:08]** Um this thing up here, it's going to be

**[12:08]** Um this thing up here, it's going to be different for everyone. Um this within

**[12:10]** different for everyone. Um this within

**[12:10]** different for everyone. Um this within the UI is your model ID that you use to

**[12:13]** the UI is your model ID that you use to

**[12:13]** the UI is your model ID that you use to put uh set up the URL.

**[12:16]** put uh set up the URL.

**[12:16]** put uh set up the URL. Um hey everyone, we're going to come

**[12:18]** Um hey everyone, we're going to come

**[12:18]** Um hey everyone, we're going to come back together here. Um it's about 9:45.

**[12:21]** back together here. Um it's about 9:45.

**[12:21]** back together here. Um it's about 9:45. Um so we're going to move on to the next

**[12:24]** Um so we're going to move on to the next

**[12:24]** Um so we're going to move on to the next stage of the workshop where Yian is

**[12:26]** stage of the workshop where Yian is

**[12:26]** stage of the workshop where Yian is going to do some really awesome demos.

**[12:28]** going to do some really awesome demos.

**[12:28]** going to do some really awesome demos. Um if you are still getting everything

**[12:31]** Um if you are still getting everything

**[12:31]** Um if you are still getting everything set up, uh no worries. All this stuff is

**[12:33]** set up, uh no worries. All this stuff is

**[12:33]** set up, uh no worries. All this stuff is going to be live on um GitHub. You've

**[12:35]** going to be live on um GitHub. You've

**[12:35]** going to be live on um GitHub. You've Oh, sorry. Yeah, on GitHub. Um the the

**[12:38]** Oh, sorry. Yeah, on GitHub. Um the the

**[12:38]** Oh, sorry. Yeah, on GitHub. Um the the repository with the workshop information

**[12:39]** repository with the workshop information

**[12:39]** repository with the workshop information is going to stay up um so you can keep

**[12:42]** is going to stay up um so you can keep

**[12:42]** is going to stay up um so you can keep following along. Um this is also all

**[12:44]** following along. Um this is also all

**[12:44]** following along. Um this is also all going to be published. Um so it's going

**[12:46]** going to be published. Um so it's going

**[12:46]** going to be published. Um so it's going to be easy to go back if you have any

**[12:48]** to be easy to go back if you have any

**[12:48]** to be easy to go back if you have any issues. Um anyway, so the next thing

**[12:50]** issues. Um anyway, so the next thing

**[12:50]** issues. Um anyway, so the next thing that we're going to look at um now that

**[12:52]** that we're going to look at um now that

**[12:52]** that we're going to look at um now that we have a sort of basic idea of okay, SG

**[12:56]** we have a sort of basic idea of okay, SG

**[12:56]** we have a sort of basic idea of okay, SG lang is just like running a model

**[12:58]** lang is just like running a model

**[12:58]** lang is just like running a model server. um how are we going to actually


### [13:00 - 14:00]

**[13:01]** server. um how are we going to actually

**[13:01]** server. um how are we going to actually make it fast? Um so Yang's going to show

**[13:04]** make it fast? Um so Yang's going to show

**[13:04]** make it fast? Um so Yang's going to show um one demo which is the um CUDA um what

**[13:09]** um one demo which is the um CUDA um what

**[13:09]** um one demo which is the um CUDA um what is it? What's Yes, CUDA graph match max

**[13:13]** is it? What's Yes, CUDA graph match max

**[13:13]** is it? What's Yes, CUDA graph match max BS flag um and how to set that to

**[13:16]** BS flag um and how to set that to

**[13:16]** BS flag um and how to set that to improve performance. Um and then we're

**[13:19]** improve performance. Um and then we're

**[13:19]** improve performance. Um and then we're also going to take a look at Eagle 3

**[13:21]** also going to take a look at Eagle 3

**[13:21]** also going to take a look at Eagle 3 which is a new speculative decoding

**[13:22]** which is a new speculative decoding

**[13:22]** which is a new speculative decoding algorithm which uh also can improve

**[13:25]** algorithm which uh also can improve

**[13:25]** algorithm which uh also can improve performance. So take it away Yian. Yeah.

**[13:29]** performance. So take it away Yian. Yeah.

**[13:29]** performance. So take it away Yian. Yeah. Uh can

**[13:32]** Uh can

**[13:32]** Uh can can you see my screen? Maybe I can. Yes.

**[13:35]** can you see my screen? Maybe I can. Yes.

**[13:35]** can you see my screen? Maybe I can. Yes. Yeah. Good. Good call. Zoom it in a

**[13:37]** Yeah. Good. Good call. Zoom it in a

**[13:37]** Yeah. Good. Good call. Zoom it in a little bit.

**[13:39]** little bit.

**[13:39]** little bit. Um we're using one pod because uh on

**[13:42]** Um we're using one pod because uh on

**[13:42]** Um we're using one pod because uh on base 10 you don't get SSH access into

**[13:45]** base 10 you don't get SSH access into

**[13:45]** base 10 you don't get SSH access into your GPUs because uh security or

**[13:47]** your GPUs because uh security or

**[13:47]** your GPUs because uh security or something I guess. I don't know. Okay.

**[13:50]** something I guess. I don't know. Okay.

**[13:50]** something I guess. I don't know. Okay. So here I will use the L4 GPU. Yeah,

**[13:56]** So here I will use the L4 GPU. Yeah,

**[13:56]** So here I will use the L4 GPU. Yeah, this is the L4 GPU. And I have already

**[13:58]** this is the L4 GPU. And I have already

**[13:58]** this is the L4 GPU. And I have already installed the sjon. Yeah, we can just


### [14:00 - 15:00]

**[14:01]** installed the sjon. Yeah, we can just

**[14:01]** installed the sjon. Yeah, we can just use the pip install or install from

**[14:03]** use the pip install or install from

**[14:03]** use the pip install or install from source. And uh here is the

**[14:10]** source. And uh here is the

**[14:10]** source. And uh here is the this command line sorry we launch the

**[14:14]** this command line sorry we launch the

**[14:14]** this command line sorry we launch the server and we use the llama 38b

**[14:19]** server and we use the llama 38b

**[14:19]** server and we use the llama 38b instruct model and the attention back

**[14:23]** instruct model and the attention back

**[14:23]** instruct model and the attention back end use fa3. This is the default. And

**[14:28]** end use fa3. This is the default. And

**[14:28]** end use fa3. This is the default. And when we

**[14:48]** Okay, it it started to loading the

**[14:48]** Okay, it it started to loading the weights.

**[14:49]** weights.

**[14:49]** weights. So, uh, just to just to give everyone a

**[14:51]** So, uh, just to just to give everyone a

**[14:51]** So, uh, just to just to give everyone a little bit of context, um, the top

**[14:55]** little bit of context, um, the top

**[14:55]** little bit of context, um, the top window you're seeing here is the, um, L4

**[14:58]** window you're seeing here is the, um, L4

**[14:58]** window you're seeing here is the, um, L4 that's actually running the SGLAN


### [15:00 - 16:00]

**[15:00]** that's actually running the SGLAN

**[15:00]** that's actually running the SGLAN server. The bottom window here, um, LMEL

**[15:03]** server. The bottom window here, um, LMEL

**[15:03]** server. The bottom window here, um, LMEL is a sort of industry standard

**[15:05]** is a sort of industry standard

**[15:05]** is a sort of industry standard benchmarking tool, um, that we're just

**[15:07]** benchmarking tool, um, that we're just

**[15:07]** benchmarking tool, um, that we're just going to use to throw a bunch of traffic

**[15:09]** going to use to throw a bunch of traffic

**[15:09]** going to use to throw a bunch of traffic at the running server. Yeah. Yeah, for

**[15:11]** at the running server. Yeah. Yeah, for

**[15:11]** at the running server. Yeah. Yeah, for sure. And, uh, yeah, we can see the the

**[15:14]** sure. And, uh, yeah, we can see the the

**[15:14]** sure. And, uh, yeah, we can see the the log from from the server. It shows that

**[15:17]** log from from the server. It shows that

**[15:17]** log from from the server. It shows that we capture CUDA graph batch size. I

**[15:20]** we capture CUDA graph batch size. I

**[15:20]** we capture CUDA graph batch size. I think CUDA graph is turn on by default

**[15:22]** think CUDA graph is turn on by default

**[15:22]** think CUDA graph is turn on by default but the CUDA graph max batch size for L4

**[15:26]** but the CUDA graph max batch size for L4

**[15:26]** but the CUDA graph max batch size for L4 for this model is eight. So it only

**[15:29]** for this model is eight. So it only

**[15:29]** for this model is eight. So it only capture one 2 48 and okay the surfer is

**[15:34]** capture one 2 48 and okay the surfer is

**[15:34]** capture one 2 48 and okay the surfer is ready to roll and we can use the LM4 to

**[15:37]** ready to roll and we can use the LM4 to

**[15:37]** ready to roll and we can use the LM4 to send a request.

**[15:46]** Yeah, we can see that from from the log.

**[15:46]** Yeah, we can see that from from the log. Here is the prefill batch and here is

**[15:49]** Here is the prefill batch and here is

**[15:49]** Here is the prefill batch and here is the decode batch. And we can see uh

**[15:54]** the decode batch. And we can see uh

**[15:54]** the decode batch. And we can see uh at the decode batch when the running

**[15:56]** at the decode batch when the running

**[15:56]** at the decode batch when the running request is 10, it means that there are

**[15:59]** request is 10, it means that there are

**[15:59]** request is 10, it means that there are 10 running request and the CUDA graph is


### [16:00 - 17:00]

**[16:02]** 10 running request and the CUDA graph is

**[16:02]** 10 running request and the CUDA graph is false because the running request 10 is

**[16:05]** false because the running request 10 is

**[16:05]** false because the running request 10 is larger than the max CUDA graph size

**[16:08]** larger than the max CUDA graph size

**[16:08]** larger than the max CUDA graph size eight. That's why this one this flag is

**[16:11]** eight. That's why this one this flag is

**[16:11]** eight. That's why this one this flag is false. And when this is false, we get uh

**[16:16]** false. And when this is false, we get uh

**[16:16]** false. And when this is false, we get uh 155

**[16:18]** 155

**[16:18]** 155 generation token per second. And we can

**[16:21]** generation token per second. And we can

**[16:21]** generation token per second. And we can use this one divide divide 10. So I

**[16:24]** use this one divide divide 10. So I

**[16:24]** use this one divide divide 10. So I think per user nearly 15 uh token per

**[16:28]** think per user nearly 15 uh token per

**[16:28]** think per user nearly 15 uh token per second.

**[16:30]** second.

**[16:30]** second. Okay, we can kill the client and we can

**[16:34]** Okay, we can kill the client and we can

**[16:34]** Okay, we can kill the client and we can also kill the server.

**[16:47]** So yeah, we we can use this command as a

**[16:47]** So yeah, we we can use this command as a base and uh set the CUDA graph max. Yes,

**[16:54]** base and uh set the CUDA graph max. Yes,

**[16:54]** base and uh set the CUDA graph max. Yes, CUDA gra


### [17:00 - 18:00]

**[17:02]** for example, we can just set 32.

**[17:02]** for example, we can just set 32. You you've got a you've got a typo in um

**[17:06]** You you've got a you've got a typo in um

**[17:06]** You you've got a you've got a typo in um Oh, sorry.

**[17:16]** The network is not good. Here everyone

**[17:16]** The network is not good. Here everyone is learning a very important lesson in

**[17:18]** is learning a very important lesson in

**[17:18]** is learning a very important lesson in the value of latency.

**[17:21]** the value of latency.

**[17:21]** the value of latency. Okay. Yeah.

**[17:36]** Yeah, it's loading.

**[17:36]** Yeah, it's loading. Waits.

**[17:38]** Waits.

**[17:38]** Waits. Yeah. And we can see that uh after we

**[17:40]** Yeah. And we can see that uh after we

**[17:40]** Yeah. And we can see that uh after we set the max cuda graph besides the

**[17:44]** set the max cuda graph besides the

**[17:44]** set the max cuda graph besides the capture kuda graphs uh I think that the

**[17:47]** capture kuda graphs uh I think that the

**[17:47]** capture kuda graphs uh I think that the max is uh 32. It's larger than the eight

**[17:52]** max is uh 32. It's larger than the eight

**[17:52]** max is uh 32. It's larger than the eight and the server is ready to roll. We also

**[17:54]** and the server is ready to roll. We also

**[17:54]** and the server is ready to roll. We also used to send a request.


### [18:00 - 19:00]

**[18:12]** Okay. So, first is the prefill batch and

**[18:12]** Okay. So, first is the prefill batch and then we can here is the decode batch.

**[18:17]** then we can here is the decode batch.

**[18:17]** then we can here is the decode batch. Okay. And uh yeah, here is the decode

**[18:21]** Okay. And uh yeah, here is the decode

**[18:21]** Okay. And uh yeah, here is the decode batch. We can

**[18:29]** wait for a moment.

**[18:29]** wait for a moment. Decode


### [19:00 - 20:00]

**[19:06]** Yeah, for example, here the the decode

**[19:06]** Yeah, for example, here the the decode batch and there are 13 running request

**[19:11]** batch and there are 13 running request

**[19:11]** batch and there are 13 running request and the CUDA graph is true and here is

**[19:13]** and the CUDA graph is true and here is

**[19:13]** and the CUDA graph is true and here is the generation S putut

**[19:17]** the generation S putut

**[19:17]** the generation S putut and I think per user should be

**[19:35]** It's not easy to compare. Uh yeah. Yeah.

**[19:35]** It's not easy to compare. Uh yeah. Yeah. I I I think uh

**[19:38]** I I I think uh

**[19:38]** I I I think uh we have recording this video and we can

**[19:42]** we have recording this video and we can

**[19:42]** we have recording this video and we can also see here cuda graph and we upload

**[19:47]** also see here cuda graph and we upload

**[19:47]** also see here cuda graph and we upload this one kudraph max specialize demo.

**[19:51]** this one kudraph max specialize demo.

**[19:51]** this one kudraph max specialize demo. We we want to codraph to be true during

**[19:53]** We we want to codraph to be true during

**[19:53]** We we want to codraph to be true during decode because I think this is very

**[19:56]** decode because I think this is very

**[19:56]** decode because I think this is very important for the decoding performance.

**[19:59]** important for the decoding performance.

**[19:59]** important for the decoding performance. Uh but the default max size is eight on


### [20:00 - 21:00]

**[20:02]** Uh but the default max size is eight on

**[20:02]** Uh but the default max size is eight on L4. And when we used LM4 to send a

**[20:05]** L4. And when we used LM4 to send a

**[20:06]** L4. And when we used LM4 to send a request, we find that oh the max size is

**[20:08]** request, we find that oh the max size is

**[20:08]** request, we find that oh the max size is larger than eight. That's why we want to

**[20:11]** larger than eight. That's why we want to

**[20:11]** larger than eight. That's why we want to set or adjust the parameter. Here when

**[20:14]** set or adjust the parameter. Here when

**[20:14]** set or adjust the parameter. Here when we set it to 32 uh we can handle the

**[20:17]** we set it to 32 uh we can handle the

**[20:17]** we set it to 32 uh we can handle the realistic batch during benchmark.

**[20:21]** realistic batch during benchmark.

**[20:21]** realistic batch during benchmark. Do you have any questions?

**[20:24]** Do you have any questions?

**[20:24]** Do you have any questions? What are the commands to

**[20:28]** What are the commands to

**[20:28]** What are the commands to Oh, okay. The LME4. Mhm. Yeah. Yeah.

**[20:32]** Oh, okay. The LME4. Mhm. Yeah. Yeah.

**[20:32]** Oh, okay. The LME4. Mhm. Yeah. Yeah. Yeah. I think LME4 is the evaluate

**[20:35]** Yeah. I think LME4 is the evaluate

**[20:35]** Yeah. I think LME4 is the evaluate evaluation tool and we need to specify

**[20:39]** evaluation tool and we need to specify

**[20:39]** evaluation tool and we need to specify the model

**[20:41]** the model

**[20:41]** the model and uh here is the model name. Here is

**[20:44]** and uh here is the model name. Here is

**[20:44]** and uh here is the model name. Here is the URL because I just use run port to

**[20:47]** the URL because I just use run port to

**[20:47]** the URL because I just use run port to run this and it used the same node. So

**[20:50]** run this and it used the same node. So

**[20:50]** run this and it used the same node. So that's why the URL is the local host and

**[20:54]** that's why the URL is the local host and

**[20:54]** that's why the URL is the local host and we we specify the port this one 8,000

**[20:59]** we we specify the port this one 8,000

**[20:59]** we we specify the port this one 8,000 that's why we use 8,000 and we use the


### [21:00 - 22:00]

**[21:01]** that's why we use 8,000 and we use the

**[21:02]** that's why we use 8,000 and we use the openi compatible server and here the

**[21:05]** openi compatible server and here the

**[21:05]** openi compatible server and here the number concurrent or the the batch size

**[21:07]** number concurrent or the the batch size

**[21:08]** number concurrent or the the batch size is 128. We set the max generation tokens

**[21:13]** is 128. We set the max generation tokens

**[21:13]** is 128. We set the max generation tokens we just use GSMK. I think it's a

**[21:15]** we just use GSMK. I think it's a

**[21:15]** we just use GSMK. I think it's a classical evaluation data set and uh

**[21:19]** classical evaluation data set and uh

**[21:19]** classical evaluation data set and uh because we use the chat completion API

**[21:21]** because we use the chat completion API

**[21:21]** because we use the chat completion API interface that's why we need to apply

**[21:24]** interface that's why we need to apply

**[21:24]** interface that's why we need to apply try to complete and I just use f short 8

**[21:27]** try to complete and I just use f short 8

**[21:27]** try to complete and I just use f short 8 the limit means that because you know uh

**[21:30]** the limit means that because you know uh

**[21:30]** the limit means that because you know uh the GSMK it has uh 1,

**[21:34]** the GSMK it has uh 1,

**[21:34]** the GSMK it has uh 1, 39

**[21:41]** promotes and when we use the limit

**[21:41]** promotes and when we use the limit 0

**[21:43]** 0

**[21:43]** 0 15 I think it's nearly uh 200 promotes.

**[21:47]** 15 I think it's nearly uh 200 promotes.

**[21:47]** 15 I think it's nearly uh 200 promotes. I can share I can also share this this

**[21:50]** I can share I can also share this this

**[21:50]** I can share I can also share this this command line in the in the ripple. Yeah.

**[21:53]** command line in the in the ripple. Yeah.

**[21:53]** command line in the in the ripple. Yeah. Yeah. Maybe I can add it.


### [22:00 - 23:00]

**[22:02]** Oh, sorry.

**[22:02]** Oh, sorry. Yeah. So, just to just to be clear, um

**[22:04]** Yeah. So, just to just to be clear, um

**[22:04]** Yeah. So, just to just to be clear, um this command is running on the actual

**[22:08]** this command is running on the actual

**[22:08]** this command is running on the actual GPU itself. Um so, this is for when you

**[22:11]** GPU itself. Um so, this is for when you

**[22:11]** GPU itself. Um so, this is for when you have SSH access into the GPU. running um

**[22:15]** have SSH access into the GPU. running um

**[22:15]** have SSH access into the GPU. running um on a on the service we're all using on

**[22:17]** on a on the service we're all using on

**[22:17]** on a on the service we're all using on the the base 10 GPUs you can't SSH in um

**[22:21]** the the base 10 GPUs you can't SSH in um

**[22:21]** the the base 10 GPUs you can't SSH in um but if you do have the access to a GPU

**[22:24]** but if you do have the access to a GPU

**[22:24]** but if you do have the access to a GPU where you can get SSH access then you

**[22:27]** where you can get SSH access then you

**[22:27]** where you can get SSH access then you would use this um LM uh eval tool um in

**[22:31]** would use this um LM uh eval tool um in

**[22:31]** would use this um LM uh eval tool um in order to simulate that traffic um if

**[22:34]** order to simulate that traffic um if

**[22:34]** order to simulate that traffic um if you're using a more like standard HTTP

**[22:38]** you're using a more like standard HTTP

**[22:38]** you're using a more like standard HTTP connection um to a you know remote GPU

**[22:41]** connection um to a you know remote GPU

**[22:41]** connection um to a you know remote GPU then you would use a a different

**[22:43]** then you would use a a different

**[22:43]** then you would use a a different benchmarking tool um that's you know

**[22:45]** benchmarking tool um that's you know

**[22:45]** benchmarking tool um that's you know request based.

**[22:47]** request based.

**[22:47]** request based. Yeah.

**[22:48]** Yeah.

**[22:48]** Yeah. Okay. And uh do you have any other

**[22:51]** Okay. And uh do you have any other

**[22:51]** Okay. And uh do you have any other questions for CUDA graph?

**[22:55]** questions for CUDA graph?

**[22:55]** questions for CUDA graph? Why is default?

**[22:57]** Why is default?

**[22:57]** Why is default? Yeah. Yeah. I I think the default eight

**[22:59]** Yeah. Yeah. I I think the default eight

**[22:59]** Yeah. Yeah. I I think the default eight is because the A4 GP memory and we we


### [23:00 - 24:00]

**[23:04]** is because the A4 GP memory and we we

**[23:04]** is because the A4 GP memory and we we have uh some default configuration. uh

**[23:07]** have uh some default configuration. uh

**[23:07]** have uh some default configuration. uh we will yeah set the

**[23:10]** we will yeah set the

**[23:10]** we will yeah set the when when you didn't set the kuda graph

**[23:13]** when when you didn't set the kuda graph

**[23:13]** when when you didn't set the kuda graph max patch size the default value is none

**[23:16]** max patch size the default value is none

**[23:16]** max patch size the default value is none and when the default value is none we

**[23:18]** and when the default value is none we

**[23:18]** and when the default value is none we will set internally for for specific

**[23:21]** will set internally for for specific

**[23:21]** will set internally for for specific hardware for specific model yeah for for

**[23:24]** hardware for specific model yeah for for

**[23:24]** hardware for specific model yeah for for example it's TP1 and it's on L4 so the

**[23:28]** example it's TP1 and it's on L4 so the

**[23:28]** example it's TP1 and it's on L4 so the default is just eight yeah so what if

**[23:32]** default is just eight yeah so what if

**[23:32]** default is just eight yeah so what if someone by mistake like he adds a higher

**[23:35]** someone by mistake like he adds a higher

**[23:35]** someone by mistake like he adds a higher one for

**[23:37]** one for

**[23:37]** one for was on. Yeah, you can just try that

**[23:39]** was on. Yeah, you can just try that

**[23:39]** was on. Yeah, you can just try that because when you launch the server, you

**[23:41]** because when you launch the server, you

**[23:41]** because when you launch the server, you can see the the uh startup parameters

**[23:45]** can see the the uh startup parameters

**[23:45]** can see the the uh startup parameters and then well you you have a workload,

**[23:48]** and then well you you have a workload,

**[23:48]** and then well you you have a workload, right? and you use the LME42 benchmark

**[23:51]** right? and you use the LME42 benchmark

**[23:52]** right? and you use the LME42 benchmark for example and you can analyze the

**[23:54]** for example and you can analyze the

**[23:54]** for example and you can analyze the server log and you find that oh during

**[23:56]** server log and you find that oh during

**[23:56]** server log and you find that oh during the decoding the CUDA graph is disabled

**[23:58]** the decoding the CUDA graph is disabled

**[23:58]** the decoding the CUDA graph is disabled and we actually we want to enable CUDA


### [24:00 - 25:00]

**[24:01]** and we actually we want to enable CUDA

**[24:01]** and we actually we want to enable CUDA graph that's that's why we increase the

**[24:03]** graph that's that's why we increase the

**[24:03]** graph that's that's why we increase the max CUDA graph batch size

**[24:06]** max CUDA graph batch size

**[24:06]** max CUDA graph batch size yeah

**[24:07]** yeah

**[24:07]** yeah okay awesome um so let's um let's see do

**[24:13]** okay awesome um so let's um let's see do

**[24:13]** okay awesome um so let's um let's see do you want to show the eagle stuff or do

**[24:14]** you want to show the eagle stuff or do

**[24:14]** you want to show the eagle stuff or do you want to show the codebase stuff yeah

**[24:16]** you want to show the codebase stuff yeah

**[24:16]** you want to show the codebase stuff yeah yeah yeah

**[24:17]** yeah yeah

**[24:17]** yeah yeah okay Uh I think the the next very

**[24:20]** okay Uh I think the the next very

**[24:20]** okay Uh I think the the next very important is about the the Eagle stuff.

**[24:23]** important is about the the Eagle stuff.

**[24:23]** important is about the the Eagle stuff. Yeah. So Eagle 3 is a speculative

**[24:26]** Yeah. So Eagle 3 is a speculative

**[24:26]** Yeah. So Eagle 3 is a speculative decoding framework. It came out very

**[24:28]** decoding framework. It came out very

**[24:28]** decoding framework. It came out very recently, right? The paper was released

**[24:30]** recently, right? The paper was released

**[24:30]** recently, right? The paper was released a few months ago. Um and so SGLang

**[24:34]** a few months ago. Um and so SGLang

**[24:34]** a few months ago. Um and so SGLang supports Eagle 3. Um and uh with it you

**[24:38]** supports Eagle 3. Um and uh with it you

**[24:38]** supports Eagle 3. Um and uh with it you can configure a wide different a wide

**[24:40]** can configure a wide different a wide

**[24:40]** can configure a wide different a wide variety of um different parameters

**[24:43]** variety of um different parameters

**[24:43]** variety of um different parameters around how many tokens you're

**[24:45]** around how many tokens you're

**[24:45]** around how many tokens you're speculating, how deep you're

**[24:46]** speculating, how deep you're

**[24:46]** speculating, how deep you're speculating, that kind of stuff. Um and

**[24:49]** speculating, that kind of stuff. Um and

**[24:49]** speculating, that kind of stuff. Um and Eagle 3 um can have much higher

**[24:52]** Eagle 3 um can have much higher

**[24:52]** Eagle 3 um can have much higher acceptance token acceptance rate. Um so

**[24:55]** acceptance token acceptance rate. Um so

**[24:55]** acceptance token acceptance rate. Um so obviously when you're speculating, the

**[24:56]** obviously when you're speculating, the

**[24:56]** obviously when you're speculating, the higher your token acceptance rate, the

**[24:58]** higher your token acceptance rate, the

**[24:58]** higher your token acceptance rate, the better performance you're going to get.


### [25:00 - 26:00]

**[25:00]** better performance you're going to get.

**[25:00]** better performance you're going to get. So we can take a quick look at some of

**[25:02]** So we can take a quick look at some of

**[25:02]** So we can take a quick look at some of those parameters that you showed. Um and

**[25:05]** those parameters that you showed. Um and

**[25:05]** those parameters that you showed. Um and then maybe uh the benchmark script you

**[25:07]** then maybe uh the benchmark script you

**[25:07]** then maybe uh the benchmark script you were showing me the other day. Yeah.

**[25:08]** were showing me the other day. Yeah.

**[25:08]** were showing me the other day. Yeah. Yeah. I I think for the ego 3 you Yeah.

**[25:11]** Yeah. I I think for the ego 3 you Yeah.

**[25:11]** Yeah. I I think for the ego 3 you Yeah. We we also provide the the example we

**[25:14]** We we also provide the the example we

**[25:14]** We we also provide the the example we can just yeah change directory to to

**[25:17]** can just yeah change directory to to

**[25:17]** can just yeah change directory to to this directory and then use trans push.

**[25:20]** this directory and then use trans push.

**[25:20]** this directory and then use trans push. It's very easy. I just want to explain

**[25:23]** It's very easy. I just want to explain

**[25:23]** It's very easy. I just want to explain uh some details. For example, we need to

**[25:25]** uh some details. For example, we need to

**[25:25]** uh some details. For example, we need to specify the speculative decoding

**[25:28]** specify the speculative decoding

**[25:28]** specify the speculative decoding algorithm. Here is the eagle like this

**[25:30]** algorithm. Here is the eagle like this

**[25:30]** algorithm. Here is the eagle like this one.

**[25:36]** Yeah, we need to specify speculative

**[25:36]** Yeah, we need to specify speculative decoding algorithm eagle and we also

**[25:39]** decoding algorithm eagle and we also

**[25:39]** decoding algorithm eagle and we also need to specify the draft model path

**[25:41]** need to specify the draft model path

**[25:41]** need to specify the draft model path because uh

**[25:44]** because uh

**[25:44]** because uh this one the model path. This is the

**[25:46]** this one the model path. This is the

**[25:46]** this one the model path. This is the target model and here is the draft

**[25:49]** target model and here is the draft

**[25:49]** target model and here is the draft model.

**[25:51]** model.

**[25:51]** model. Sorry. Here is the draft model for the

**[25:54]** Sorry. Here is the draft model for the

**[25:54]** Sorry. Here is the draft model for the ego 3.

**[25:56]** ego 3.

**[25:56]** ego 3. Yeah, llama llama 38B. So, one thing

**[25:59]** Yeah, llama llama 38B. So, one thing

**[25:59]** Yeah, llama llama 38B. So, one thing that's different about Eagle um all the


### [26:00 - 27:00]

**[26:01]** that's different about Eagle um all the

**[26:01]** that's different about Eagle um all the different Eagle algorithms is instead of

**[26:04]** different Eagle algorithms is instead of

**[26:04]** different Eagle algorithms is instead of like a standard draft target where

**[26:06]** like a standard draft target where

**[26:06]** like a standard draft target where you're say maybe using llama 1B and

**[26:09]** you're say maybe using llama 1B and

**[26:09]** you're say maybe using llama 1B and llama 8B together, um Eagle works by

**[26:13]** llama 8B together, um Eagle works by

**[26:13]** llama 8B together, um Eagle works by pulling in multiple layers um of the

**[26:15]** pulling in multiple layers um of the

**[26:16]** pulling in multiple layers um of the target model, using that to build a

**[26:18]** target model, using that to build a

**[26:18]** target model, using that to build a draft model. Um so the draft model is

**[26:20]** draft model. Um so the draft model is

**[26:20]** draft model. Um so the draft model is kind of derived directly from the target

**[26:23]** kind of derived directly from the target

**[26:23]** kind of derived directly from the target model versus being just a smaller model

**[26:25]** model versus being just a smaller model

**[26:25]** model versus being just a smaller model that you're also running. Yeah. Yeah.

**[26:27]** that you're also running. Yeah. Yeah.

**[26:27]** that you're also running. Yeah. Yeah. And you also need to specify uh this

**[26:30]** And you also need to specify uh this

**[26:30]** And you also need to specify uh this parameter the numbers depths the eagle

**[26:33]** parameter the numbers depths the eagle

**[26:33]** parameter the numbers depths the eagle top K and draft verify tokens for

**[26:38]** top K and draft verify tokens for

**[26:38]** top K and draft verify tokens for example the depth of the drafting if

**[26:41]** example the depth of the drafting if

**[26:41]** example the depth of the drafting if it's three and the top K is one. I think

**[26:44]** it's three and the top K is one. I think

**[26:44]** it's three and the top K is one. I think the the most number of Java tokens

**[26:47]** the the most number of Java tokens

**[26:47]** the the most number of Java tokens should not more than four. That's why we

**[26:50]** should not more than four. That's why we

**[26:50]** should not more than four. That's why we said four here. And yeah, you can see

**[26:53]** said four here. And yeah, you can see

**[26:53]** said four here. And yeah, you can see more details about this configuration at

**[26:57]** more details about this configuration at

**[26:57]** more details about this configuration at the Echelon official documentation. And


### [27:00 - 28:00]

**[27:00]** the Echelon official documentation. And

**[27:00]** the Echelon official documentation. And I also will show show something about

**[27:02]** I also will show show something about

**[27:02]** I also will show show something about how to turn in these parameters. You

**[27:05]** how to turn in these parameters. You

**[27:05]** how to turn in these parameters. You know, we have these parameters. I think

**[27:07]** know, we have these parameters. I think

**[27:07]** know, we have these parameters. I think the model path and is fixed. And the how

**[27:11]** the model path and is fixed. And the how

**[27:11]** the model path and is fixed. And the how about this one? The number steps. Okay.

**[27:13]** about this one? The number steps. Okay.

**[27:13]** about this one? The number steps. Okay. and the number of Java tokens we can

**[27:15]** and the number of Java tokens we can

**[27:15]** and the number of Java tokens we can turn in these parameters and I will show

**[27:17]** turn in these parameters and I will show

**[27:17]** turn in these parameters and I will show you how to turn in that. So in the SLAN

**[27:20]** you how to turn in that. So in the SLAN

**[27:20]** you how to turn in that. So in the SLAN mano we have a script and uh

**[27:26]** mano we have a script and uh

**[27:26]** mano we have a script and uh we have a playground

**[27:29]** we have a playground

**[27:29]** we have a playground yeah we have a bunch speculative

**[27:31]** yeah we have a bunch speculative

**[27:31]** yeah we have a bunch speculative decoding.

**[27:33]** decoding.

**[27:33]** decoding. Okay. So we can just use uh this script

**[27:36]** Okay. So we can just use uh this script

**[27:36]** Okay. So we can just use uh this script to turn in these three parameters. For

**[27:39]** to turn in these three parameters. For

**[27:39]** to turn in these three parameters. For example, on a single GPU when we want to

**[27:41]** example, on a single GPU when we want to

**[27:41]** example, on a single GPU when we want to you this is the target model llama 27B

**[27:45]** you this is the target model llama 27B

**[27:45]** you this is the target model llama 27B and this is the uh draft model. Here is

**[27:49]** and this is the uh draft model. Here is

**[27:49]** and this is the uh draft model. Here is some default parameters.

**[27:51]** some default parameters.

**[27:51]** some default parameters. The batch size is from 1 2 4 8 16. And

**[27:56]** The batch size is from 1 2 4 8 16. And

**[27:56]** The batch size is from 1 2 4 8 16. And the steps is here 0 one three seven five


### [28:00 - 29:00]

**[28:00]** the steps is here 0 one three seven five

**[28:00]** the steps is here 0 one three seven five seven and the top K is here. This is the

**[28:04]** seven and the top K is here. This is the

**[28:04]** seven and the top K is here. This is the number of the tokens. What does that

**[28:06]** number of the tokens. What does that

**[28:06]** number of the tokens. What does that mean? I think it's it's very easy to

**[28:08]** mean? I think it's it's very easy to

**[28:08]** mean? I think it's it's very easy to understand. For example, we have

**[28:10]** understand. For example, we have

**[28:10]** understand. For example, we have different combinations of these

**[28:12]** different combinations of these

**[28:12]** different combinations of these different parameters and this script

**[28:15]** different parameters and this script

**[28:15]** different parameters and this script will run all of these combinations and

**[28:18]** will run all of these combinations and

**[28:18]** will run all of these combinations and you will get a result and from the

**[28:20]** you will get a result and from the

**[28:20]** you will get a result and from the result you will get a you will get to

**[28:22]** result you will get a you will get to

**[28:22]** result you will get a you will get to know that oh this for example this

**[28:24]** know that oh this for example this

**[28:24]** know that oh this for example this combination is best. For example the at

**[28:27]** combination is best. For example the at

**[28:27]** combination is best. For example the at the b size eight uh the three steps

**[28:31]** the b size eight uh the three steps

**[28:31]** the b size eight uh the three steps maybe and the top k is one and the

**[28:34]** maybe and the top k is one and the

**[28:34]** maybe and the top k is one and the number of tokens is four. you will get

**[28:36]** number of tokens is four. you will get

**[28:36]** number of tokens is four. you will get some result about the the the speed and

**[28:39]** some result about the the the speed and

**[28:39]** some result about the the the speed and about the accept rate then you can use

**[28:43]** about the accept rate then you can use

**[28:43]** about the accept rate then you can use this parameter for your online servering

**[28:45]** this parameter for your online servering

**[28:45]** this parameter for your online servering for your production servering. Yeah.

**[28:48]** for your production servering. Yeah.

**[28:48]** for your production servering. Yeah. Yeah. And when you're running this

**[28:49]** Yeah. And when you're running this

**[28:49]** Yeah. And when you're running this benchmark uh do be sure to set the

**[28:51]** benchmark uh do be sure to set the

**[28:51]** benchmark uh do be sure to set the prompts to things that are

**[28:53]** prompts to things that are

**[28:53]** prompts to things that are representative of your actual workload.

**[28:55]** representative of your actual workload.

**[28:55]** representative of your actual workload. Yeah. Because speculation um in any

**[28:58]** Yeah. Because speculation um in any

**[28:58]** Yeah. Because speculation um in any format including Eagle is all about


### [29:00 - 30:00]

**[29:00]** format including Eagle is all about

**[29:00]** format including Eagle is all about guessing future tokens. uh if you are

**[29:03]** guessing future tokens. uh if you are

**[29:03]** guessing future tokens. uh if you are benchmarking on data that is not

**[29:06]** benchmarking on data that is not

**[29:06]** benchmarking on data that is not representative of your actual inputs and

**[29:08]** representative of your actual inputs and

**[29:08]** representative of your actual inputs and outputs um that you're seeing live in

**[29:10]** outputs um that you're seeing live in

**[29:10]** outputs um that you're seeing live in production then you're probably going to

**[29:12]** production then you're probably going to

**[29:12]** production then you're probably going to end up with the wrong parameters. Um

**[29:13]** end up with the wrong parameters. Um

**[29:14]** end up with the wrong parameters. Um speculation is a very topic and content

**[29:16]** speculation is a very topic and content

**[29:16]** speculation is a very topic and content dependent uh optimization. Yeah. Yeah. I

**[29:19]** dependent uh optimization. Yeah. Yeah. I

**[29:19]** dependent uh optimization. Yeah. Yeah. I think so. So you you can also update

**[29:21]** think so. So you you can also update

**[29:21]** think so. So you you can also update these promotes here in this bench bench

**[29:24]** these promotes here in this bench bench

**[29:24]** these promotes here in this bench bench spec decoding uh uh pi python script we

**[29:28]** spec decoding uh uh pi python script we

**[29:28]** spec decoding uh uh pi python script we have some promotes and I think you can

**[29:31]** have some promotes and I think you can

**[29:31]** have some promotes and I think you can update this. Yeah just according your

**[29:34]** update this. Yeah just according your

**[29:34]** update this. Yeah just according your needs. Yep. Okay. So let's uh let's take

**[29:37]** needs. Yep. Okay. So let's uh let's take

**[29:37]** needs. Yep. Okay. So let's uh let's take a look at some of the um stuff around

**[29:40]** a look at some of the um stuff around

**[29:40]** a look at some of the um stuff around you know the community and getting

**[29:41]** you know the community and getting

**[29:41]** you know the community and getting involved. Yeah. Yeah. Yeah. Also I I

**[29:44]** involved. Yeah. Yeah. Yeah. Also I I

**[29:44]** involved. Yeah. Yeah. Yeah. Also I I think yeah SGAN currently it's become

**[29:48]** think yeah SGAN currently it's become

**[29:48]** think yeah SGAN currently it's become very popular and if you want to

**[29:51]** very popular and if you want to

**[29:51]** very popular and if you want to participate in this community and

**[29:53]** participate in this community and

**[29:53]** participate in this community and contribute some code I think uh yeah

**[29:56]** contribute some code I think uh yeah

**[29:56]** contribute some code I think uh yeah I'll I'll show the the slides real

**[29:58]** I'll I'll show the the slides real

**[29:58]** I'll I'll show the the slides real quick. Okay.


### [30:00 - 31:00]

**[30:05]** Yeah. So um you know SG Lang does have a

**[30:05]** Yeah. So um you know SG Lang does have a really great community. Um, and uh, you

**[30:08]** really great community. Um, and uh, you

**[30:08]** really great community. Um, and uh, you know, some some quick ways to get

**[30:09]** know, some some quick ways to get

**[30:10]** know, some some quick ways to get involved. Um, you can start it on

**[30:12]** involved. Um, you can start it on

**[30:12]** involved. Um, you can start it on GitHub, file issues and bug reports as

**[30:14]** GitHub, file issues and bug reports as

**[30:14]** GitHub, file issues and bug reports as you build. Um, they have a great tagging

**[30:16]** you build. Um, they have a great tagging

**[30:16]** you build. Um, they have a great tagging system of post issues to get involved

**[30:18]** system of post issues to get involved

**[30:18]** system of post issues to get involved with which Giann's is going to show in a

**[30:20]** with which Giann's is going to show in a

**[30:20]** with which Giann's is going to show in a second. Um, but the number one thing you

**[30:22]** second. Um, but the number one thing you

**[30:22]** second. Um, but the number one thing you can do is follow SG Langis.org on

**[30:25]** can do is follow SG Langis.org on

**[30:26]** can do is follow SG Langis.org on Twitter. Um, and then join the Slack um,

**[30:28]** Twitter. Um, and then join the Slack um,

**[30:28]** Twitter. Um, and then join the Slack um, to keep an eye out for online and

**[30:30]** to keep an eye out for online and

**[30:30]** to keep an eye out for online and inerson meetups. Um, so this is a link

**[30:32]** inerson meetups. Um, so this is a link

**[30:32]** inerson meetups. Um, so this is a link to the community Slack. Um you can uh

**[30:35]** to the community Slack. Um you can uh

**[30:35]** to the community Slack. Um you can uh scan that real quick if you uh if you

**[30:37]** scan that real quick if you uh if you

**[30:37]** scan that real quick if you uh if you want to get involved with SG Lang. Um

**[30:40]** want to get involved with SG Lang. Um

**[30:40]** want to get involved with SG Lang. Um these slides are also all in the um

**[30:43]** these slides are also all in the um

**[30:43]** these slides are also all in the um these slides are all in the repo um that

**[30:45]** these slides are all in the repo um that

**[30:45]** these slides are all in the repo um that you got from the workshop. So you can

**[30:47]** you got from the workshop. So you can

**[30:47]** you got from the workshop. So you can access this uh this link and stuff

**[30:49]** access this uh this link and stuff

**[30:49]** access this uh this link and stuff later. It's also just slack.sglang.ai.

**[30:52]** later. It's also just slack.sglang.ai.

**[30:52]** later. It's also just slack.sglang.ai. Pretty simple link. Um so if you are

**[30:56]** Pretty simple link. Um so if you are

**[30:56]** Pretty simple link. Um so if you are going to get involved and you do want to

**[30:59]** going to get involved and you do want to

**[30:59]** going to get involved and you do want to um you know start contributing to the


### [31:00 - 32:00]

**[31:01]** um you know start contributing to the

**[31:01]** um you know start contributing to the codebase um we can kind of show you um

**[31:05]** codebase um we can kind of show you um

**[31:05]** codebase um we can kind of show you um some of the stuff. So at a high level um

**[31:08]** some of the stuff. So at a high level um

**[31:08]** some of the stuff. So at a high level um the codebase has the SGLang runtime um

**[31:11]** the codebase has the SGLang runtime um

**[31:11]** the codebase has the SGLang runtime um it's got a domain specific front-end

**[31:13]** it's got a domain specific front-end

**[31:13]** it's got a domain specific front-end language and it has a set of optimized

**[31:16]** language and it has a set of optimized

**[31:16]** language and it has a set of optimized konels. Um you can go actually on this

**[31:19]** konels. Um you can go actually on this

**[31:19]** konels. Um you can go actually on this deep wiki page um and get a really good

**[31:22]** deep wiki page um and get a really good

**[31:22]** deep wiki page um and get a really good co tour of the codebase um as well as a

**[31:26]** co tour of the codebase um as well as a

**[31:26]** co tour of the codebase um as well as a tour from um this uh other repository

**[31:30]** tour from um this uh other repository

**[31:30]** tour from um this uh other repository that we have linked um which is also by

**[31:32]** that we have linked um which is also by

**[31:32]** that we have linked um which is also by one of the SG lang people um with some

**[31:35]** one of the SG lang people um with some

**[31:35]** one of the SG lang people um with some some diagrams about like exactly how

**[31:37]** some diagrams about like exactly how

**[31:37]** some diagrams about like exactly how this stuff works. Um and then yeah,

**[31:39]** this stuff works. Um and then yeah,

**[31:40]** this stuff works. Um and then yeah, Yinang's just going to show a quick

**[31:41]** Yinang's just going to show a quick

**[31:41]** Yinang's just going to show a quick overview of the codebase on GitHub. Um

**[31:44]** overview of the codebase on GitHub. Um

**[31:44]** overview of the codebase on GitHub. Um in case you're interested in getting

**[31:46]** in case you're interested in getting

**[31:46]** in case you're interested in getting involved and contributing. Yeah, I I

**[31:48]** involved and contributing. Yeah, I I

**[31:48]** involved and contributing. Yeah, I I think that the best way to get involved

**[31:50]** think that the best way to get involved

**[31:50]** think that the best way to get involved in this project first we need to use

**[31:53]** in this project first we need to use

**[31:53]** in this project first we need to use that and then you will find some issue

**[31:55]** that and then you will find some issue

**[31:55]** that and then you will find some issue or of you will find some feature missing

**[31:58]** or of you will find some feature missing

**[31:58]** or of you will find some feature missing in this ripple and then the first thing


### [32:00 - 33:00]

**[32:01]** in this ripple and then the first thing

**[32:01]** in this ripple and then the first thing that is you can raise a new issue here.

**[32:05]** that is you can raise a new issue here.

**[32:05]** that is you can raise a new issue here. It's loading. Yeah, you can just create

**[32:08]** It's loading. Yeah, you can just create

**[32:08]** It's loading. Yeah, you can just create a new issue feature request something

**[32:11]** a new issue feature request something

**[32:11]** a new issue feature request something like this. And also I I think yeah we

**[32:14]** like this. And also I I think yeah we

**[32:14]** like this. And also I I think yeah we have labeled something like

**[32:17]** have labeled something like

**[32:17]** have labeled something like good first issue or help wanted.

**[32:28]** Yeah, you can see that there are nearly

**[32:28]** Yeah, you can see that there are nearly uh

**[32:30]** uh

**[32:30]** uh 26. So I think yeah if you are

**[32:34]** 26. So I think yeah if you are

**[32:34]** 26. So I think yeah if you are interested in in this issue for example

**[32:36]** interested in in this issue for example

**[32:36]** interested in in this issue for example if you are interested in support or

**[32:39]** if you are interested in support or

**[32:39]** if you are interested in support or suffering VM va model or you you can

**[32:43]** suffering VM va model or you you can

**[32:43]** suffering VM va model or you you can just start with this I think uh good

**[32:46]** just start with this I think uh good

**[32:46]** just start with this I think uh good first issue and here wanted issue. Yeah

**[32:49]** first issue and here wanted issue. Yeah

**[32:49]** first issue and here wanted issue. Yeah we are welcome the contributions and

**[32:52]** we are welcome the contributions and

**[32:52]** we are welcome the contributions and here is the development road map.

**[32:56]** here is the development road map.

**[32:56]** here is the development road map. So yeah if some feature is missing or if

**[32:59]** So yeah if some feature is missing or if

**[32:59]** So yeah if some feature is missing or if some feature you care about you you you


### [33:00 - 34:00]

**[33:02]** some feature you care about you you you

**[33:02]** some feature you care about you you you can find it in the road map I think you

**[33:05]** can find it in the road map I think you

**[33:06]** can find it in the road map I think you can uh join us for for this feature

**[33:09]** can uh join us for for this feature

**[33:09]** can uh join us for for this feature development or you can also yeah raise

**[33:12]** development or you can also yeah raise

**[33:12]** development or you can also yeah raise new issue about this and the last one is

**[33:15]** new issue about this and the last one is

**[33:15]** new issue about this and the last one is about the

**[33:17]** about the

**[33:17]** about the overall work through okay so Yeah,

**[33:30]** in the estron repo uh we we have some

**[33:30]** in the estron repo uh we we have some component. This one is the SJ kernel.

**[33:33]** component. This one is the SJ kernel.

**[33:33]** component. This one is the SJ kernel. It's a Echelon kernel library. We

**[33:36]** It's a Echelon kernel library. We

**[33:36]** It's a Echelon kernel library. We implement attention normalization

**[33:38]** implement attention normalization

**[33:38]** implement attention normalization activation gym all of them in this

**[33:41]** activation gym all of them in this

**[33:41]** activation gym all of them in this kernel library. And if you are familiar

**[33:43]** kernel library. And if you are familiar

**[33:43]** kernel library. And if you are familiar with CUDA kernels and if you're

**[33:45]** with CUDA kernels and if you're

**[33:45]** with CUDA kernels and if you're interested yeah with kernel programming

**[33:49]** interested yeah with kernel programming

**[33:49]** interested yeah with kernel programming you can just contribute this part. And

**[33:51]** you can just contribute this part. And

**[33:51]** you can just contribute this part. And here is the SGL rooter. Last year we

**[33:54]** here is the SGL rooter. Last year we

**[33:54]** here is the SGL rooter. Last year we published Slon

**[33:57]** published Slon

**[33:57]** published Slon the S version and we supported the


### [34:00 - 35:00]

**[34:00]** the S version and we supported the

**[34:00]** the S version and we supported the cashware rooting. If you yeah you are

**[34:03]** cashware rooting. If you yeah you are

**[34:03]** cashware rooting. If you yeah you are interested in this part you can work on

**[34:05]** interested in this part you can work on

**[34:05]** interested in this part you can work on the SG routter.

**[34:09]** the SG routter.

**[34:09]** the SG routter. Currently we we use eston as a LM

**[34:12]** Currently we we use eston as a LM

**[34:12]** Currently we we use eston as a LM inference runtime. So I think the Python

**[34:16]** inference runtime. So I think the Python

**[34:16]** inference runtime. So I think the Python part the SRT is the core part. We

**[34:20]** part the SRT is the core part. We

**[34:20]** part the SRT is the core part. We support disagre PD disagregation. We

**[34:22]** support disagre PD disagregation. We

**[34:22]** support disagre PD disagregation. We support a constraint coding. We support

**[34:24]** support a constraint coding. We support

**[34:24]** support a constraint coding. We support function calling. Yeah, we support open

**[34:28]** function calling. Yeah, we support open

**[34:28]** function calling. Yeah, we support open eye compatible server and we also

**[34:30]** eye compatible server and we also

**[34:30]** eye compatible server and we also support a lot of models. If yeah I think

**[34:34]** support a lot of models. If yeah I think

**[34:34]** support a lot of models. If yeah I think if you want to support the custom model

**[34:36]** if you want to support the custom model

**[34:36]** if you want to support the custom model you can just yeah take this as a

**[34:39]** you can just yeah take this as a

**[34:39]** you can just yeah take this as a reference. For example you can take

**[34:41]** reference. For example you can take

**[34:41]** reference. For example you can take llama as a reference. I I think uh the

**[34:45]** llama as a reference. I I think uh the

**[34:45]** llama as a reference. I I think uh the popular open source model the

**[34:47]** popular open source model the

**[34:47]** popular open source model the architecture is very very similar. So if

**[34:51]** architecture is very very similar. So if

**[34:51]** architecture is very very similar. So if if the model you are interested has not

**[34:53]** if the model you are interested has not

**[34:53]** if the model you are interested has not been implemented in the eston you can

**[34:55]** been implemented in the eston you can

**[34:55]** been implemented in the eston you can just check this reference and do some

**[34:57]** just check this reference and do some

**[34:57]** just check this reference and do some modification and then we welcome


### [35:00 - 36:00]

**[35:00]** modification and then we welcome

**[35:00]** modification and then we welcome contributions. Yeah, that's all.

**[35:03]** contributions. Yeah, that's all.

**[35:03]** contributions. Yeah, that's all. Awesome. So, um if we get the slides

**[35:05]** Awesome. So, um if we get the slides

**[35:05]** Awesome. So, um if we get the slides back up here. Um

**[35:08]** back up here. Um

**[35:08]** back up here. Um yeah, so to uh you know, wrap it up. Um

**[35:12]** yeah, so to uh you know, wrap it up. Um

**[35:12]** yeah, so to uh you know, wrap it up. Um first off, thank you so much for coming

**[35:13]** first off, thank you so much for coming

**[35:13]** first off, thank you so much for coming out. Thank you for bearing with us.

**[35:15]** out. Thank you for bearing with us.

**[35:15]** out. Thank you for bearing with us. Thank you for waiting for web pages to

**[35:17]** Thank you for waiting for web pages to

**[35:17]** Thank you for waiting for web pages to load on this uh wonderful uh internet

**[35:20]** load on this uh wonderful uh internet

**[35:20]** load on this uh wonderful uh internet connection that we all have. Um to kind

**[35:24]** connection that we all have. Um to kind

**[35:24]** connection that we all have. Um to kind of wrap things up, um I do want to issue

**[35:27]** of wrap things up, um I do want to issue

**[35:27]** of wrap things up, um I do want to issue a couple invitations to everyone in this

**[35:29]** a couple invitations to everyone in this

**[35:29]** a couple invitations to everyone in this room today. Uh, number one, we're having

**[35:31]** room today. Uh, number one, we're having

**[35:31]** room today. Uh, number one, we're having a really cool uh, happy hour with the

**[35:33]** a really cool uh, happy hour with the

**[35:33]** a really cool uh, happy hour with the folks from Oxen AI. Um, OxenAI is a

**[35:37]** folks from Oxen AI. Um, OxenAI is a

**[35:37]** folks from Oxen AI. Um, OxenAI is a fine-tuning company. Um, their CEO just

**[35:40]** fine-tuning company. Um, their CEO just

**[35:40]** fine-tuning company. Um, their CEO just had a really cool demo that he published

**[35:42]** had a really cool demo that he published

**[35:42]** had a really cool demo that he published a couple weeks ago where he took GPT 4.1

**[35:45]** a couple weeks ago where he took GPT 4.1

**[35:46]** a couple weeks ago where he took GPT 4.1 um, and made it, you know, do a SQL

**[35:48]** um, and made it, you know, do a SQL

**[35:48]** um, and made it, you know, do a SQL generation benchmark, took the score,

**[35:50]** generation benchmark, took the score,

**[35:50]** generation benchmark, took the score, said, "Okay, I think I can do better

**[35:51]** said, "Okay, I think I can do better

**[35:51]** said, "Okay, I think I can do better than this." Took Quen 0.6b, 6B. Yes, you

**[35:54]** than this." Took Quen 0.6b, 6B. Yes, you

**[35:54]** than this." Took Quen 0.6b, 6B. Yes, you heard me right. Less than a billion

**[35:56]** heard me right. Less than a billion

**[35:56]** heard me right. Less than a billion parameters. Fine-tuned it on some SQL

**[35:58]** parameters. Fine-tuned it on some SQL

**[35:58]** parameters. Fine-tuned it on some SQL generation data and actually beat GPT


### [36:00 - 37:00]

**[36:00]** generation data and actually beat GPT

**[36:00]** generation data and actually beat GPT 4.1 with a model that you can run on

**[36:03]** 4.1 with a model that you can run on

**[36:03]** 4.1 with a model that you can run on like 3 years ago iPhone. Um, so yeah,

**[36:07]** like 3 years ago iPhone. Um, so yeah,

**[36:07]** like 3 years ago iPhone. Um, so yeah, we're going to be uh, you know, at this

**[36:08]** we're going to be uh, you know, at this

**[36:08]** we're going to be uh, you know, at this happy hour. We're going to be talking

**[36:09]** happy hour. We're going to be talking

**[36:09]** happy hour. We're going to be talking about fine-tuning and stuff. It's going

**[36:10]** about fine-tuning and stuff. It's going

**[36:10]** about fine-tuning and stuff. It's going to be a great time. Um, second

**[36:13]** to be a great time. Um, second

**[36:13]** to be a great time. Um, second invitation I want to extend to everyone

**[36:14]** invitation I want to extend to everyone

**[36:14]** invitation I want to extend to everyone in this room is if you think this stuff

**[36:16]** in this room is if you think this stuff

**[36:16]** in this room is if you think this stuff is cool, if you were, you know, seeing

**[36:18]** is cool, if you were, you know, seeing

**[36:18]** is cool, if you were, you know, seeing all the stuff that Yang was talking

**[36:19]** all the stuff that Yang was talking

**[36:19]** all the stuff that Yang was talking about around contributing to the

**[36:21]** about around contributing to the

**[36:21]** about around contributing to the codebase and you're like, "Yeah, I love

**[36:22]** codebase and you're like, "Yeah, I love

**[36:22]** codebase and you're like, "Yeah, I love CUDA programming, um, just come work at

**[36:25]** CUDA programming, um, just come work at

**[36:25]** CUDA programming, um, just come work at base 10. Uh, if you're bored in your

**[36:26]** base 10. Uh, if you're bored in your

**[36:26]** base 10. Uh, if you're bored in your job, you won't be bored here." Uh, we've

**[36:28]** job, you won't be bored here." Uh, we've

**[36:28]** job, you won't be bored here." Uh, we've got a lot of open roles for both

**[36:30]** got a lot of open roles for both

**[36:30]** got a lot of open roles for both infrastructure and for model

**[36:32]** infrastructure and for model

**[36:32]** infrastructure and for model performance. Uh, if you're at all

**[36:34]** performance. Uh, if you're at all

**[36:34]** performance. Uh, if you're at all interested, just come talk to me. I'm

**[36:35]** interested, just come talk to me. I'm

**[36:35]** interested, just come talk to me. I'm going to be here all uh, all three days.

**[36:38]** going to be here all uh, all three days.

**[36:38]** going to be here all uh, all three days. Um so yeah that's pretty much our um

**[36:40]** Um so yeah that's pretty much our um

**[36:40]** Um so yeah that's pretty much our um workshop today. Thank you so much for

**[36:42]** workshop today. Thank you so much for

**[36:42]** workshop today. Thank you so much for coming through um and happy to take any

**[36:44]** coming through um and happy to take any

**[36:44]** coming through um and happy to take any questions in the uh remaining time we

**[36:47]** questions in the uh remaining time we

**[36:47]** questions in the uh remaining time we have. Yes. What are the main reasons why

**[36:51]** have. Yes. What are the main reasons why

**[36:51]** have. Yes. What are the main reasons why you use SG? Yeah that's a great

**[36:53]** you use SG? Yeah that's a great

**[36:53]** you use SG? Yeah that's a great question. Um you know I think that uh

**[36:57]** question. Um you know I think that uh

**[36:58]** question. Um you know I think that uh what we at bas like we use all sorts of


### [37:00 - 38:00]

**[37:00]** what we at bas like we use all sorts of

**[37:00]** what we at bas like we use all sorts of different runtimes u model to model. Um

**[37:03]** different runtimes u model to model. Um

**[37:03]** different runtimes u model to model. Um sometimes you just want to use whatever

**[37:05]** sometimes you just want to use whatever

**[37:05]** sometimes you just want to use whatever one is best for your use case. Um, but

**[37:09]** one is best for your use case. Um, but

**[37:09]** one is best for your use case. Um, but in general, uh, I think that the reason

**[37:11]** in general, uh, I think that the reason

**[37:11]** in general, uh, I think that the reason that we've been really attracted to it

**[37:13]** that we've been really attracted to it

**[37:13]** that we've been really attracted to it is because of how configurable and

**[37:15]** is because of how configurable and

**[37:15]** is because of how configurable and extensible it is. Out of the box with

**[37:18]** extensible it is. Out of the box with

**[37:18]** extensible it is. Out of the box with basic parameters, you're going to get

**[37:20]** basic parameters, you're going to get

**[37:20]** basic parameters, you're going to get more or less the same performance from

**[37:21]** more or less the same performance from

**[37:22]** more or less the same performance from anyone. Um, but if you're able to number

**[37:24]** anyone. Um, but if you're able to number

**[37:24]** anyone. Um, but if you're able to number one have like a really deeply and well

**[37:27]** one have like a really deeply and well

**[37:27]** one have like a really deeply and well doumented codebase like SGLang where

**[37:29]** doumented codebase like SGLang where

**[37:29]** doumented codebase like SGLang where you're able to really deeply understand

**[37:31]** you're able to really deeply understand

**[37:32]** you're able to really deeply understand all the different options that you have.

**[37:33]** all the different options that you have.

**[37:34]** all the different options that you have. Um, that can get you a long way. And

**[37:35]** Um, that can get you a long way. And

**[37:36]** Um, that can get you a long way. And then as we were just talking about, it's

**[37:37]** then as we were just talking about, it's

**[37:37]** then as we were just talking about, it's super easy to contribute. Um, so we're

**[37:39]** super easy to contribute. Um, so we're

**[37:39]** super easy to contribute. Um, so we're constantly like making fixes and and

**[37:41]** constantly like making fixes and and

**[37:41]** constantly like making fixes and and contributing them back. Um, and that

**[37:44]** contributing them back. Um, and that

**[37:44]** contributing them back. Um, and that means that you know if you're using a a

**[37:46]** means that you know if you're using a a

**[37:46]** means that you know if you're using a a different library, you might be blocked

**[37:48]** different library, you might be blocked

**[37:48]** different library, you might be blocked waiting for the core developers to

**[37:50]** waiting for the core developers to

**[37:50]** waiting for the core developers to implement support for a model or

**[37:51]** implement support for a model or

**[37:51]** implement support for a model or something SG lang you can unblock

**[37:53]** something SG lang you can unblock

**[37:53]** something SG lang you can unblock yourself.

**[37:55]** yourself.

**[37:55]** yourself. Yes.

**[37:57]** Yes.

**[37:57]** Yes. When there are multiple vendors and

**[37:59]** When there are multiple vendors and

**[37:59]** When there are multiple vendors and different kind of applications


### [38:00 - 39:00]

**[38:01]** different kind of applications

**[38:01]** different kind of applications around the end point or within the

**[38:03]** around the end point or within the

**[38:03]** around the end point or within the subnet you are defining how would you

**[38:06]** subnet you are defining how would you

**[38:06]** subnet you are defining how would you define your um cyber security or

**[38:10]** define your um cyber security or

**[38:10]** define your um cyber security or security protocols? How would you

**[38:12]** security protocols? How would you

**[38:12]** security protocols? How would you enhance your protocols? Yeah, I mean

**[38:15]** enhance your protocols? Yeah, I mean

**[38:15]** enhance your protocols? Yeah, I mean that's a great question. I don't really

**[38:17]** that's a great question. I don't really

**[38:17]** that's a great question. I don't really think that your your choice of runtime

**[38:19]** think that your your choice of runtime

**[38:19]** think that your your choice of runtime engine like affects that too much. um

**[38:22]** engine like affects that too much. um

**[38:22]** engine like affects that too much. um because you you're just packaging it up

**[38:25]** because you you're just packaging it up

**[38:25]** because you you're just packaging it up in a in a container. Um you know within

**[38:28]** in a in a container. Um you know within

**[38:28]** in a in a container. Um you know within within B 10 we've thought a lot about

**[38:30]** within B 10 we've thought a lot about

**[38:30]** within B 10 we've thought a lot about this in a sort of runtime agnostic way.

**[38:33]** this in a sort of runtime agnostic way.

**[38:33]** this in a sort of runtime agnostic way. Um where we're thinking about of course

**[38:35]** Um where we're thinking about of course

**[38:35]** Um where we're thinking about of course like lease privilege. Um we're thinking

**[38:37]** like lease privilege. Um we're thinking

**[38:37]** like lease privilege. Um we're thinking about you know making sure that there's

**[38:39]** about you know making sure that there's

**[38:39]** about you know making sure that there's a good deal of isolation built into the

**[38:41]** a good deal of isolation built into the

**[38:41]** a good deal of isolation built into the system. Um but from a from a runtime

**[38:44]** system. Um but from a from a runtime

**[38:44]** system. Um but from a from a runtime perspective I don't think there's

**[38:45]** perspective I don't think there's

**[38:45]** perspective I don't think there's anything special we have to do for

**[38:46]** anything special we have to do for

**[38:46]** anything special we have to do for security with SGLang right compared to

**[38:48]** security with SGLang right compared to

**[38:48]** security with SGLang right compared to like VLM or anything else.

**[38:56]** Thank you. So um I I am from a

**[38:56]** Thank you. So um I I am from a department of defense and so awesome

**[38:59]** department of defense and so awesome

**[38:59]** department of defense and so awesome extensive experience in financial


### [39:00 - 40:00]

**[39:01]** extensive experience in financial

**[39:01]** extensive experience in financial applications. So

**[39:04]** applications. So

**[39:04]** applications. So to uh do some uh

**[39:08]** to uh do some uh

**[39:08]** to uh do some uh product developments in house

**[39:11]** product developments in house

**[39:11]** product developments in house uh do you think I have I can do the

**[39:14]** uh do you think I have I can do the

**[39:14]** uh do you think I have I can do the entire product development inhouse

**[39:16]** entire product development inhouse

**[39:16]** entire product development inhouse within a submit don't have to go back

**[39:19]** within a submit don't have to go back

**[39:19]** within a submit don't have to go back and forth open right now for example

**[39:23]** and forth open right now for example

**[39:23]** and forth open right now for example just throwing an example

**[39:24]** just throwing an example

**[39:24]** just throwing an example one of those uh uh CMMC

**[39:28]** one of those uh uh CMMC

**[39:28]** one of those uh uh CMMC cyber security

**[39:30]** cyber security

**[39:30]** cyber security certifications

**[39:32]** certifications

**[39:32]** certifications I have to go through the endpoint

**[39:34]** I have to go through the endpoint

**[39:34]** I have to go through the endpoint controls

**[39:35]** controls

**[39:35]** controls and define the endpoint control and then

**[39:38]** and define the endpoint control and then

**[39:38]** and define the endpoint control and then go connect to the chat open GP. Gotcha.

**[39:43]** go connect to the chat open GP. Gotcha.

**[39:43]** go connect to the chat open GP. Gotcha. Yeah. Yeah. So in that case, this would

**[39:44]** Yeah. Yeah. So in that case, this would

**[39:44]** Yeah. Yeah. So in that case, this would actually help you out a lot. Um instead

**[39:47]** actually help you out a lot. Um instead

**[39:47]** actually help you out a lot. Um instead of relying on that remote server, um you

**[39:49]** of relying on that remote server, um you

**[39:49]** of relying on that remote server, um you can just spin up a cluster like within

**[39:52]** can just spin up a cluster like within

**[39:52]** can just spin up a cluster like within the same uh VPC or like within the same

**[39:55]** the same uh VPC or like within the same

**[39:55]** the same uh VPC or like within the same physical data center um as the workload

**[39:58]** physical data center um as the workload

**[39:58]** physical data center um as the workload that's relying on the AI model. um you


### [40:00 - 41:00]

**[40:01]** that's relying on the AI model. um you

**[40:01]** that's relying on the AI model. um you can clone SG lang you can cut you know

**[40:05]** can clone SG lang you can cut you know

**[40:05]** can clone SG lang you can cut you know take a release um and fully inspect the

**[40:08]** take a release um and fully inspect the

**[40:08]** take a release um and fully inspect the code because it's open source and then

**[40:10]** code because it's open source and then

**[40:10]** code because it's open source and then fix um on that release so that there's

**[40:13]** fix um on that release so that there's

**[40:13]** fix um on that release so that there's nothing changing under the hood um and

**[40:16]** nothing changing under the hood um and

**[40:16]** nothing changing under the hood um and then yeah with that you'd be able to you

**[40:18]** then yeah with that you'd be able to you

**[40:18]** then yeah with that you'd be able to you know run the models just directly on the

**[40:20]** know run the models just directly on the

**[40:20]** know run the models just directly on the GPU as you saw in Yinang's demo when he

**[40:22]** GPU as you saw in Yinang's demo when he

**[40:22]** GPU as you saw in Yinang's demo when he was doing the um CUDA graph stuff um

**[40:25]** was doing the um CUDA graph stuff um

**[40:25]** was doing the um CUDA graph stuff um you're able to you know call it on even

**[40:28]** you're able to you know call it on even

**[40:28]** you're able to you know call it on even a local host basis and run info Um, so

**[40:32]** a local host basis and run info Um, so

**[40:32]** a local host basis and run info Um, so yeah, it gives you all the tools you

**[40:33]** yeah, it gives you all the tools you

**[40:33]** yeah, it gives you all the tools you need if you're trying to build even like

**[40:35]** need if you're trying to build even like

**[40:36]** need if you're trying to build even like a sort of a gapped type of system um

**[40:39]** a sort of a gapped type of system um

**[40:39]** a sort of a gapped type of system um with, you know, all of these open source

**[40:41]** with, you know, all of these open source

**[40:41]** with, you know, all of these open source runtimes. You can pull that code in,

**[40:44]** runtimes. You can pull that code in,

**[40:44]** runtimes. You can pull that code in, inspect it, lock it, um, and then, uh,

**[40:47]** inspect it, lock it, um, and then, uh,

**[40:47]** inspect it, lock it, um, and then, uh, build off of it. Very impressive. And

**[40:50]** build off of it. Very impressive. And

**[40:50]** build off of it. Very impressive. And also, um, currently I'm working on, uh,

**[40:54]** also, um, currently I'm working on, uh,

**[40:54]** also, um, currently I'm working on, uh, I'm also a PhD student. Yeah. So, I'm

**[40:57]** I'm also a PhD student. Yeah. So, I'm

**[40:57]** I'm also a PhD student. Yeah. So, I'm working on blockchain based quantum


### [41:00 - 42:00]

**[41:00]** working on blockchain based quantum

**[41:00]** working on blockchain based quantum computing and some kind of AI

**[41:03]** computing and some kind of AI

**[41:03]** computing and some kind of AI deliverables.

**[41:04]** deliverables.

**[41:04]** deliverables. So how do you

**[41:07]** So how do you

**[41:07]** So how do you circumvent within your product? Can you

**[41:10]** circumvent within your product? Can you

**[41:10]** circumvent within your product? Can you so blockchain is completely another

**[41:11]** so blockchain is completely another

**[41:11]** so blockchain is completely another community based code development. So how

**[41:15]** community based code development. So how

**[41:15]** community based code development. So how do you can we integrate different

**[41:17]** do you can we integrate different

**[41:17]** do you can we integrate different community based or a combination of both

**[41:21]** community based or a combination of both

**[41:21]** community based or a combination of both hybrid community based protocol or so

**[41:25]** hybrid community based protocol or so

**[41:25]** hybrid community based protocol or so what is because blockchain is kind of

**[41:31]** what is because blockchain is kind of

**[41:31]** what is because blockchain is kind of decentralized network whereas this one

**[41:34]** decentralized network whereas this one

**[41:34]** decentralized network whereas this one is kind of

**[41:36]** is kind of

**[41:36]** is kind of yeah um to be perfectly honest like I

**[41:39]** yeah um to be perfectly honest like I

**[41:39]** yeah um to be perfectly honest like I haven't really experienced anything with

**[41:41]** haven't really experienced anything with

**[41:41]** haven't really experienced anything with that um pretty much all of uh the use

**[41:44]** that um pretty much all of uh the use

**[41:44]** that um pretty much all of uh the use cases that I've run with SG lang or just

**[41:47]** cases that I've run with SG lang or just

**[41:47]** cases that I've run with SG lang or just traditional client server applications.

**[41:50]** traditional client server applications.

**[41:50]** traditional client server applications. Any other questions?


### [42:00 - 43:00]

**[42:11]** Yeah, great. Um, so yeah, so in B 10

**[42:11]** Yeah, great. Um, so yeah, so in B 10 like what we do is we we call it like

**[42:14]** like what we do is we we call it like

**[42:14]** like what we do is we we call it like the base 10 inference stack where we're

**[42:16]** the base 10 inference stack where we're

**[42:16]** the base 10 inference stack where we're taking all of these different um all of

**[42:19]** taking all of these different um all of

**[42:19]** taking all of these different um all of these different providers, the the VLM,

**[42:21]** these different providers, the the VLM,

**[42:21]** these different providers, the the VLM, the SGLANG, and the Tensor RT LLM, which

**[42:23]** the SGLANG, and the Tensor RT LLM, which

**[42:23]** the SGLANG, and the Tensor RT LLM, which we actually probably use the most

**[42:24]** we actually probably use the most

**[42:24]** we actually probably use the most heavily of the three. Um, and taking

**[42:27]** heavily of the three. Um, and taking

**[42:27]** heavily of the three. Um, and taking them in, customizing them, doing all

**[42:29]** them in, customizing them, doing all

**[42:29]** them in, customizing them, doing all that stuff. I'm supposed to say for

**[42:30]** that stuff. I'm supposed to say for

**[42:30]** that stuff. I'm supposed to say for marketing purposes. Um, but we are

**[42:32]** marketing purposes. Um, but we are

**[42:32]** marketing purposes. Um, but we are customizing it quite a bit. Um, anyway,

**[42:35]** customizing it quite a bit. Um, anyway,

**[42:35]** customizing it quite a bit. Um, anyway, where we generally pick VLM, um, I'm

**[42:38]** where we generally pick VLM, um, I'm

**[42:38]** where we generally pick VLM, um, I'm sorry I'm talking about uh I'm talking

**[42:40]** sorry I'm talking about uh I'm talking

**[42:40]** sorry I'm talking about uh I'm talking about them during your SG lang talk. Um,

**[42:42]** about them during your SG lang talk. Um,

**[42:42]** about them during your SG lang talk. Um, but where we use VLM is oftentimes for

**[42:45]** but where we use VLM is oftentimes for

**[42:45]** but where we use VLM is oftentimes for compatibility. Um, for example, like I

**[42:48]** compatibility. Um, for example, like I

**[42:48]** compatibility. Um, for example, like I know our Gemma models that we have up in

**[42:50]** know our Gemma models that we have up in

**[42:50]** know our Gemma models that we have up in the library are using VLM um because

**[42:54]** the library are using VLM um because

**[42:54]** the library are using VLM um because like it's what was supported uh when

**[42:56]** like it's what was supported uh when

**[42:56]** like it's what was supported uh when when it dropped. Um, so yeah, that's

**[42:58]** when it dropped. Um, so yeah, that's

**[42:58]** when it dropped. Um, so yeah, that's that's in my mind like the best use case


### [43:00 - 44:00]

**[43:00]** that's in my mind like the best use case

**[43:00]** that's in my mind like the best use case for VLM is like super broad

**[43:02]** for VLM is like super broad

**[43:02]** for VLM is like super broad compatibility.

**[43:12]** Awesome. Well, uh, like I said, we're

**[43:12]** Awesome. Well, uh, like I said, we're going to be around all day. Um, and, um,

**[43:16]** going to be around all day. Um, and, um,

**[43:16]** going to be around all day. Um, and, um, I'm going to be, uh, at the base 10

**[43:17]** I'm going to be, uh, at the base 10

**[43:17]** I'm going to be, uh, at the base 10 booth, uh, for the next 3 days. So if

**[43:20]** booth, uh, for the next 3 days. So if

**[43:20]** booth, uh, for the next 3 days. So if you have any questions about SGA, model

**[43:22]** you have any questions about SGA, model

**[43:22]** you have any questions about SGA, model serving, model inference in general, um

**[43:24]** serving, model inference in general, um

**[43:24]** serving, model inference in general, um or if you want one of them jobs I was

**[43:26]** or if you want one of them jobs I was

**[43:26]** or if you want one of them jobs I was talking about, we are hiring very

**[43:28]** talking about, we are hiring very

**[43:28]** talking about, we are hiring very aggressively. Uh so definitely stop by

**[43:30]** aggressively. Uh so definitely stop by

**[43:30]** aggressively. Uh so definitely stop by the booth, hang out, uh grab one of

**[43:32]** the booth, hang out, uh grab one of

**[43:32]** the booth, hang out, uh grab one of these shirts. Um and yeah, thank you so

**[43:35]** these shirts. Um and yeah, thank you so

**[43:35]** these shirts. Um and yeah, thank you so much for coming.


