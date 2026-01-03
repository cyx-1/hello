# Building an Agentic Platform — Ben Kus, CTO Box

**Video URL:** https://www.youtube.com/watch?v=12v5S1n1eOY

---

## Full Transcript

### [00:00 - 01:00]

**[00:18]** Hello. Um, so I'm Ben Kuss. I'm CTO Box

**[00:18]** Hello. Um, so I'm Ben Kuss. I'm CTO Box and I'm going to talk today about our

**[00:21]** and I'm going to talk today about our

**[00:21]** and I'm going to talk today about our journey of uh through AI and in

**[00:24]** journey of uh through AI and in

**[00:24]** journey of uh through AI and in particular our AI agentic journey. Um

**[00:27]** particular our AI agentic journey. Um

**[00:27]** particular our AI agentic journey. Um and uh if you don't know much about Box,

**[00:29]** and uh if you don't know much about Box,

**[00:29]** and uh if you don't know much about Box, uh a little bit of background. Um so at

**[00:32]** uh a little bit of background. Um so at

**[00:32]** uh a little bit of background. Um so at Box, we are um a unstructured content

**[00:35]** Box, we are um a unstructured content

**[00:35]** Box, we are um a unstructured content platform. Uh we've been around for a

**[00:37]** platform. Uh we've been around for a

**[00:37]** platform. Uh we've been around for a while, uh more than 15 years. And um our

**[00:41]** while, uh more than 15 years. And um our

**[00:41]** while, uh more than 15 years. And um our we very much concentrate on large

**[00:43]** we very much concentrate on large

**[00:43]** we very much concentrate on large enterprises. So uh we've got uh over

**[00:45]** enterprises. So uh we've got uh over

**[00:45]** enterprises. So uh we've got uh over 115,000 enterprise customers. We've got

**[00:48]** 115,000 enterprise customers. We've got

**[00:48]** 115,000 enterprise customers. We've got uh twothirds of the Fortune 500. And um

**[00:51]** uh twothirds of the Fortune 500. And um

**[00:51]** uh twothirds of the Fortune 500. And um our job really is to bring everything

**[00:53]** our job really is to bring everything

**[00:53]** our job really is to bring everything you'd want to do with your content to

**[00:55]** you'd want to do with your content to

**[00:55]** you'd want to do with your content to these customers and to provide them all

**[00:57]** these customers and to provide them all

**[00:57]** these customers and to provide them all the capabilities they might want. In

**[00:58]** the capabilities they might want. In

**[00:58]** the capabilities they might want. In many cases uh for AI many of these


### [01:00 - 02:00]

**[01:00]** many cases uh for AI many of these

**[01:00]** many cases uh for AI many of these customers their first AI deployment was

**[01:02]** customers their first AI deployment was

**[01:02]** customers their first AI deployment was actually with box because um of course

**[01:05]** actually with box because um of course

**[01:05]** actually with box because um of course many enterprises uh worry a lot about

**[01:07]** many enterprises uh worry a lot about

**[01:08]** many enterprises uh worry a lot about data concern security concerns and worry

**[01:10]** data concern security concerns and worry

**[01:10]** data concern security concerns and worry about data leakage with AI make sure to

**[01:11]** about data leakage with AI make sure to

**[01:11]** about data leakage with AI make sure to do safe and secure AI and this is one

**[01:13]** do safe and secure AI and this is one

**[01:13]** do safe and secure AI and this is one thing that we have specialized in over

**[01:15]** thing that we have specialized in over

**[01:15]** thing that we have specialized in over time. Um but the way that we think about

**[01:18]** time. Um but the way that we think about

**[01:18]** time. Um but the way that we think about um AI is at a platform level. So um we

**[01:21]** um AI is at a platform level. So um we

**[01:21]** um AI is at a platform level. So um we have sort of the historic version of Box

**[01:23]** have sort of the historic version of Box

**[01:23]** have sort of the historic version of Box which um has the idea of the global

**[01:25]** which um has the idea of the global

**[01:25]** which um has the idea of the global infrastructure sort of everything you

**[01:26]** infrastructure sort of everything you

**[01:26]** infrastructure sort of everything you need to manage and maintain content at

**[01:28]** need to manage and maintain content at

**[01:28]** need to manage and maintain content at scale. We've got over an exabyte of

**[01:30]** scale. We've got over an exabyte of

**[01:30]** scale. We've got over an exabyte of data. We have an awful lot of of uh

**[01:32]** data. We have an awful lot of of uh

**[01:32]** data. We have an awful lot of of uh hundreds of billions of of files that

**[01:34]** hundreds of billions of of files that

**[01:34]** hundreds of billions of of files that our customers have trusted us with. Um

**[01:36]** our customers have trusted us with. Um

**[01:36]** our customers have trusted us with. Um and we have the natural way to protect

**[01:37]** and we have the natural way to protect

**[01:37]** and we have the natural way to protect them in addition to the type of services

**[01:39]** them in addition to the type of services

**[01:39]** them in addition to the type of services that you provide when you're an

**[01:40]** that you provide when you're an

**[01:40]** that you provide when you're an unstructured data platform. But then for

**[01:42]** unstructured data platform. But then for

**[01:42]** unstructured data platform. But then for the last few years um one of the key

**[01:44]** the last few years um one of the key

**[01:44]** the last few years um one of the key things we've been investing in has been

**[01:45]** things we've been investing in has been

**[01:45]** things we've been investing in has been in AI on top of the platform. And I'm

**[01:47]** in AI on top of the platform. And I'm

**[01:48]** in AI on top of the platform. And I'm here to tell you a bit about our journey

**[01:49]** here to tell you a bit about our journey

**[01:49]** here to tell you a bit about our journey here.

**[01:51]** here.

**[01:51]** here. So um we started our journey in 2023

**[01:55]** So um we started our journey in 2023

**[01:55]** So um we started our journey in 2023 uh shortly after uh AI became sort of

**[01:58]** uh shortly after uh AI became sort of

**[01:58]** uh shortly after uh AI became sort of production ready from a generative AI

**[01:59]** production ready from a generative AI


### [02:00 - 03:00]

**[02:00]** production ready from a generative AI sense and everything I'm talking about

**[02:01]** sense and everything I'm talking about

**[02:01]** sense and everything I'm talking about here today will be generative AI of

**[02:02]** here today will be generative AI of

**[02:02]** here today will be generative AI of course so um we ended up with a set of

**[02:05]** course so um we ended up with a set of

**[02:05]** course so um we ended up with a set of features things like QA across documents

**[02:07]** features things like QA across documents

**[02:07]** features things like QA across documents things like being able to extract data

**[02:09]** things like being able to extract data

**[02:09]** things like being able to extract data things like being able to do AI power

**[02:10]** things like being able to do AI power

**[02:10]** things like being able to do AI power workflows happy to talk about these in

**[02:12]** workflows happy to talk about these in

**[02:12]** workflows happy to talk about these in general but um today I'm going to focus

**[02:14]** general but um today I'm going to focus

**[02:14]** general but um today I'm going to focus on one aspect of uh the features that we

**[02:17]** on one aspect of uh the features that we

**[02:17]** on one aspect of uh the features that we built which is the idea of data

**[02:19]** built which is the idea of data

**[02:19]** built which is the idea of data extraction

**[02:19]** extraction

**[02:20]** extraction This is the idea of taking structured

**[02:21]** This is the idea of taking structured

**[02:21]** This is the idea of taking structured data from your unstructured data and

**[02:23]** data from your unstructured data and

**[02:23]** data from your unstructured data and using that inpentic

**[02:34]** sort of um thing that you might think of

**[02:34]** sort of um thing that you might think of when you're uh thinking about these

**[02:36]** when you're uh thinking about these

**[02:36]** when you're uh thinking about these other examples about how you interact

**[02:38]** other examples about how you interact

**[02:38]** other examples about how you interact with AI. This is much less like a

**[02:40]** with AI. This is much less like a

**[02:40]** with AI. This is much less like a standard chatbot style integration. But

**[02:43]** standard chatbot style integration. But

**[02:43]** standard chatbot style integration. But uh what we learned and what I'll tell

**[02:45]** uh what we learned and what I'll tell

**[02:45]** uh what we learned and what I'll tell you about is how you the concepts of

**[02:47]** you about is how you the concepts of

**[02:47]** you about is how you the concepts of agentic uh uh capabilities applies well

**[02:50]** agentic uh uh capabilities applies well

**[02:50]** agentic uh uh capabilities applies well beyond just sort of a end user

**[02:52]** beyond just sort of a end user

**[02:52]** beyond just sort of a end user interactions.

**[02:54]** interactions.

**[02:54]** interactions. So um we'll be talking about data

**[02:56]** So um we'll be talking about data

**[02:56]** So um we'll be talking about data extraction for a moment. Just quick

**[02:57]** extraction for a moment. Just quick

**[02:57]** extraction for a moment. Just quick background when we talk about metadata

**[02:59]** background when we talk about metadata

**[02:59]** background when we talk about metadata or data we talk about the things in


### [03:00 - 04:00]

**[03:01]** or data we talk about the things in

**[03:01]** or data we talk about the things in unstructured data be it documents be it

**[03:04]** unstructured data be it documents be it

**[03:04]** unstructured data be it documents be it contracts be it project proposals

**[03:06]** contracts be it project proposals

**[03:06]** contracts be it project proposals anything that then turns into structured

**[03:08]** anything that then turns into structured

**[03:08]** anything that then turns into structured data. Uh this is a very common challenge

**[03:11]** data. Uh this is a very common challenge

**[03:11]** data. Uh this is a very common challenge in enterprises is that they have like

**[03:12]** in enterprises is that they have like

**[03:12]** in enterprises is that they have like 90% of their data is unstructured 10% of

**[03:15]** 90% of their data is unstructured 10% of

**[03:15]** 90% of their data is unstructured 10% of their data is in databases structured

**[03:17]** their data is in databases structured

**[03:17]** their data is in databases structured data. Um and uh and historically there

**[03:20]** data. Um and uh and historically there

**[03:20]** data. Um and uh and historically there has been this this challenge that like

**[03:22]** has been this this challenge that like

**[03:22]** has been this this challenge that like it was kind of hard to to utilize this.

**[03:24]** it was kind of hard to to utilize this.

**[03:24]** it was kind of hard to to utilize this. So many many customers have for a very

**[03:26]** So many many customers have for a very

**[03:26]** So many many customers have for a very long time wish they had better ways to

**[03:28]** long time wish they had better ways to

**[03:28]** long time wish they had better ways to automate their unstructured data and

**[03:30]** automate their unstructured data and

**[03:30]** automate their unstructured data and there's a lot of it and it's really

**[03:31]** there's a lot of it and it's really

**[03:31]** there's a lot of it and it's really critical in some cases it's the most

**[03:32]** critical in some cases it's the most

**[03:32]** critical in some cases it's the most critical thing in an enterprise. So um

**[03:35]** critical thing in an enterprise. So um

**[03:35]** critical thing in an enterprise. So um uh the things you do with it would be to

**[03:37]** uh the things you do with it would be to

**[03:37]** uh the things you do with it would be to like uh um query your data, being able

**[03:40]** like uh um query your data, being able

**[03:40]** like uh um query your data, being able to kick off workflows, being able to do

**[03:42]** to kick off workflows, being able to do

**[03:42]** to kick off workflows, being able to do um just a better search and filtering

**[03:44]** um just a better search and filtering

**[03:44]** um just a better search and filtering across all of your data. And so so this

**[03:46]** across all of your data. And so so this

**[03:46]** across all of your data. And so so this like uh the prototypical example, this

**[03:48]** like uh the prototypical example, this

**[03:48]** like uh the prototypical example, this is something like a contract where you

**[03:50]** is something like a contract where you

**[03:50]** is something like a contract where you have an authoritative unstructured piece

**[03:51]** have an authoritative unstructured piece

**[03:51]** have an authoritative unstructured piece of data, but then also uh the the key

**[03:54]** of data, but then also uh the the key

**[03:54]** of data, but then also uh the the key fields in there are are very important.

**[03:57]** fields in there are are very important.

**[03:57]** fields in there are are very important. So um this is not a new thing. for many


### [04:00 - 05:00]

**[04:00]** So um this is not a new thing. for many

**[04:00]** So um this is not a new thing. for many many years uh the world uh for box

**[04:03]** many years uh the world uh for box

**[04:03]** many years uh the world uh for box included has been interested in pulling

**[04:05]** included has been interested in pulling

**[04:05]** included has been interested in pulling out unstructured structured data from

**[04:06]** out unstructured structured data from

**[04:06]** out unstructured structured data from unstructured data and um there were a

**[04:09]** unstructured data and um there were a

**[04:09]** unstructured data and um there were a lot of techniques to do this and there

**[04:10]** lot of techniques to do this and there

**[04:10]** lot of techniques to do this and there there's a whole industry if you ever

**[04:12]** there's a whole industry if you ever

**[04:12]** there's a whole industry if you ever heard of IDP this is like a a

**[04:13]** heard of IDP this is like a a

**[04:13]** heard of IDP this is like a a multi-billion dollar industry whose job

**[04:15]** multi-billion dollar industry whose job

**[04:15]** multi-billion dollar industry whose job in life was to do this kind of of of uh

**[04:17]** in life was to do this kind of of of uh

**[04:17]** in life was to do this kind of of of uh extraction but it was really hard you

**[04:21]** extraction but it was really hard you

**[04:21]** extraction but it was really hard you had to build these specialized AI models

**[04:23]** had to build these specialized AI models

**[04:23]** had to build these specialized AI models uh you had to like focus on specific

**[04:25]** uh you had to like focus on specific

**[04:25]** uh you had to like focus on specific types of content you had to have this

**[04:26]** types of content you had to have this

**[04:26]** types of content you had to have this huge corpus of training data often times

**[04:28]** huge corpus of training data often times

**[04:28]** huge corpus of training data often times you need to build custom vendors, your

**[04:30]** you need to build custom vendors, your

**[04:30]** you need to build custom vendors, your custom uh uh ML models that you make and

**[04:32]** custom uh uh ML models that you make and

**[04:32]** custom uh uh ML models that you make and it was quite brittle and to the point

**[04:34]** it was quite brittle and to the point

**[04:34]** it was quite brittle and to the point not a lot of companies ever thought

**[04:36]** not a lot of companies ever thought

**[04:36]** not a lot of companies ever thought about automating most of their most

**[04:38]** about automating most of their most

**[04:38]** about automating most of their most their critical unstructured data. So

**[04:40]** their critical unstructured data. So

**[04:40]** their critical unstructured data. So this was sort of the state of the

**[04:42]** this was sort of the state of the

**[04:42]** this was sort of the state of the industry for a very long time like uh

**[04:43]** industry for a very long time like uh

**[04:43]** industry for a very long time like uh just um don't bother trying too hard

**[04:46]** just um don't bother trying too hard

**[04:46]** just um don't bother trying too hard with unstructured data. Do everything

**[04:48]** with unstructured data. Do everything

**[04:48]** with unstructured data. Do everything you can to get it in in some sort of

**[04:50]** you can to get it in in some sort of

**[04:50]** you can to get it in in some sort of structured format but don't try to too

**[04:52]** structured format but don't try to too

**[04:52]** structured format but don't try to too too hard to deal with that structured

**[04:53]** too hard to deal with that structured

**[04:53]** too hard to deal with that structured data until generative AI came along. And

**[04:56]** data until generative AI came along. And

**[04:56]** data until generative AI came along. And so this is where our our journey uh sort

**[04:58]** so this is where our our journey uh sort

**[04:58]** so this is where our our journey uh sort of begins with AI uh is for a long time


### [05:00 - 06:00]

**[05:01]** of begins with AI uh is for a long time

**[05:01]** of begins with AI uh is for a long time we've been using ML models of different

**[05:03]** we've been using ML models of different

**[05:03]** we've been using ML models of different uh in different ways and we it in and

**[05:06]** uh in different ways and we it in and

**[05:06]** uh in different ways and we it in and the first thing that we tried um when

**[05:08]** the first thing that we tried um when

**[05:08]** the first thing that we tried um when confronted with sort of a GPT2 GPT3

**[05:11]** confronted with sort of a GPT2 GPT3

**[05:11]** confronted with sort of a GPT2 GPT3 style of of of uh of AI models is that

**[05:15]** style of of of uh of AI models is that

**[05:15]** style of of of uh of AI models is that you just say uh I have a question for

**[05:17]** you just say uh I have a question for

**[05:17]** you just say uh I have a question for you AI model would can you extract this

**[05:19]** you AI model would can you extract this

**[05:19]** you AI model would can you extract this kind of data and in the same and and as

**[05:22]** kind of data and in the same and and as

**[05:22]** kind of data and in the same and and as we mostly all know is is is uh AI is not

**[05:24]** we mostly all know is is is uh AI is not

**[05:24]** we mostly all know is is is uh AI is not only great at um generating uh uh

**[05:27]** only great at um generating uh uh

**[05:27]** only great at um generating uh uh content. It's also great at

**[05:29]** content. It's also great at

**[05:29]** content. It's also great at understanding the nuances of content. So

**[05:31]** understanding the nuances of content. So

**[05:31]** understanding the nuances of content. So this uh so what we did we we first start

**[05:34]** this uh so what we did we we first start

**[05:34]** this uh so what we did we we first start out with um some some uh pre-processing

**[05:37]** out with um some some uh pre-processing

**[05:37]** out with um some some uh pre-processing you know doing sort of um OCR steps

**[05:40]** you know doing sort of um OCR steps

**[05:40]** you know doing sort of um OCR steps classic ways to do this um and then

**[05:42]** classic ways to do this um and then

**[05:42]** classic ways to do this um and then being able to then say I want to extract

**[05:43]** being able to then say I want to extract

**[05:44]** being able to then say I want to extract these fields standard AI calls single

**[05:46]** these fields standard AI calls single

**[05:46]** these fields standard AI calls single shot or with some some decoration of the

**[05:48]** shot or with some some decoration of the

**[05:48]** shot or with some some decoration of the on the prompts um and this worked great.

**[05:52]** on the prompts um and this worked great.

**[05:52]** on the prompts um and this worked great. This was amazing. This was something

**[05:54]** This was amazing. This was something

**[05:54]** This was amazing. This was something where suddenly a standard generic

**[05:57]** where suddenly a standard generic

**[05:57]** where suddenly a standard generic off-the-shelf AI model from multiple

**[05:59]** off-the-shelf AI model from multiple

**[05:59]** off-the-shelf AI model from multiple vendors could outperform even the best


### [06:00 - 07:00]

**[06:01]** vendors could outperform even the best

**[06:01]** vendors could outperform even the best sort of models that you had seen in the

**[06:03]** sort of models that you had seen in the

**[06:03]** sort of models that you had seen in the past.

**[06:04]** past.

**[06:04]** past. Uh and uh we supported multiple models

**[06:06]** Uh and uh we supported multiple models

**[06:06]** Uh and uh we supported multiple models just in case and then it got better and

**[06:08]** just in case and then it got better and

**[06:08]** just in case and then it got better and better. This was wonderful. So this was

**[06:09]** better. This was wonderful. So this was

**[06:09]** better. This was wonderful. So this was flexible. You could do it across any

**[06:10]** flexible. You could do it across any

**[06:10]** flexible. You could do it across any kind of data. You could it performed

**[06:12]** kind of data. You could it performed

**[06:12]** kind of data. You could it performed well. Um it was uh uh yes you had to do

**[06:16]** well. Um it was uh uh yes you had to do

**[06:16]** well. Um it was uh uh yes you had to do OCR and pre-process it but that was

**[06:18]** OCR and pre-process it but that was

**[06:18]** OCR and pre-process it but that was straightforward. And so we were just

**[06:19]** straightforward. And so we were just

**[06:20]** straightforward. And so we were just thrilled. This was like uh for us it was

**[06:22]** thrilled. This was like uh for us it was

**[06:22]** thrilled. This was like uh for us it was like this is this is this is a new

**[06:24]** like this is this is this is a new

**[06:24]** like this is this is this is a new generation of of of AI and um

**[06:26]** generation of of of AI and um

**[06:26]** generation of of of AI and um interestingly we would go to our

**[06:27]** interestingly we would go to our

**[06:27]** interestingly we would go to our customers and say we can do this across

**[06:29]** customers and say we can do this across

**[06:29]** customers and say we can do this across a data and then they would give us some

**[06:30]** a data and then they would give us some

**[06:30]** a data and then they would give us some and it would work and then we'd be like

**[06:32]** and it would work and then we'd be like

**[06:32]** and it would work and then we'd be like great AI models are awesome until they

**[06:35]** great AI models are awesome until they

**[06:35]** great AI models are awesome until they said oh now uh now that you do that well

**[06:37]** said oh now uh now that you do that well

**[06:37]** said oh now uh now that you do that well and I I get it now what about this one?

**[06:39]** and I I get it now what about this one?

**[06:39]** and I I get it now what about this one? What about this 300page lease document

**[06:41]** What about this 300page lease document

**[06:41]** What about this 300page lease document with 300 fields? What about this really

**[06:44]** with 300 fields? What about this really

**[06:44]** with 300 fields? What about this really complex uh set of digital assets? You

**[06:46]** complex uh set of digital assets? You

**[06:46]** complex uh set of digital assets? You want to give these really complex

**[06:47]** want to give these really complex

**[06:47]** want to give these really complex questions associated with it. what about

**[06:49]** questions associated with it. what about

**[06:49]** questions associated with it. what about I want to do not just extract data I

**[06:50]** I want to do not just extract data I

**[06:50]** I want to do not just extract data I want to do risk assessments and things

**[06:51]** want to do risk assessments and things

**[06:51]** want to do risk assessments and things that are these like more complex fields

**[06:53]** that are these like more complex fields

**[06:53]** that are these like more complex fields you start to realize huh like this as a

**[06:56]** you start to realize huh like this as a

**[06:56]** you start to realize huh like this as a human when I if you ask me that question

**[06:57]** human when I if you ask me that question

**[06:57]** human when I if you ask me that question I'm struggling to answer it um and then

**[06:59]** I'm struggling to answer it um and then

**[06:59]** I'm struggling to answer it um and then in the same way the AI started to


### [07:00 - 08:00]

**[07:00]** in the same way the AI started to

**[07:00]** in the same way the AI started to struggle to to answer it so um suddenly

**[07:04]** struggle to to answer it so um suddenly

**[07:04]** struggle to to answer it so um suddenly uh we ended up uh with um more complex

**[07:07]** uh we ended up uh with um more complex

**[07:07]** uh we ended up uh with um more complex documents

**[07:09]** documents

**[07:09]** documents um also OCR is just a hard problem uh

**[07:12]** um also OCR is just a hard problem uh

**[07:12]** um also OCR is just a hard problem uh like like there's no seemingly like no

**[07:14]** like like there's no seemingly like no

**[07:14]** like like there's no seemingly like no end of of uh heristics and tricks that

**[07:16]** end of of uh heristics and tricks that

**[07:16]** end of of uh heristics and tricks that you do on OCR to get it right So, I've

**[07:18]** you do on OCR to get it right So, I've

**[07:18]** you do on OCR to get it right So, I've got a scan document, somebody writes

**[07:20]** got a scan document, somebody writes

**[07:20]** got a scan document, somebody writes stuff in it, somebody crosses stuff out.

**[07:21]** stuff in it, somebody crosses stuff out.

**[07:22]** stuff in it, somebody crosses stuff out. It's just hard. Um, and then and then um

**[07:24]** It's just hard. Um, and then and then um

**[07:24]** It's just hard. Um, and then and then um for people who have dealt with like

**[07:25]** for people who have dealt with like

**[07:25]** for people who have dealt with like things like different file formats,

**[07:27]** things like different file formats,

**[07:27]** things like different file formats, PDFs, like um it's a challenge. So,

**[07:30]** PDFs, like um it's a challenge. So,

**[07:30]** PDFs, like um it's a challenge. So, whenever the OCR broke, it would just

**[07:32]** whenever the OCR broke, it would just

**[07:32]** whenever the OCR broke, it would just naturally give bad info to the AI and

**[07:34]** naturally give bad info to the AI and

**[07:34]** naturally give bad info to the AI and then um languages were a big pain. Um

**[07:37]** then um languages were a big pain. Um

**[07:37]** then um languages were a big pain. Um and and so we started to get more and

**[07:38]** and and so we started to get more and

**[07:38]** and and so we started to get more and more challenges as we have an

**[07:39]** more challenges as we have an

**[07:39]** more challenges as we have an international set of customers across

**[07:40]** international set of customers across

**[07:40]** international set of customers across different use cases. Um, also there was

**[07:43]** different use cases. Um, also there was

**[07:43]** different use cases. Um, also there was a clear limit to the AI in terms of how

**[07:46]** a clear limit to the AI in terms of how

**[07:46]** a clear limit to the AI in terms of how much it could handle the uh attention to

**[07:49]** much it could handle the uh attention to

**[07:49]** much it could handle the uh attention to so many different fields. So if you say

**[07:51]** so many different fields. So if you say

**[07:51]** so many different fields. So if you say here's 10 fields, here's a 10-page

**[07:53]** here's 10 fields, here's a 10-page

**[07:53]** here's 10 fields, here's a 10-page document, figure it out. They're great.

**[07:55]** document, figure it out. They're great.

**[07:55]** document, figure it out. They're great. Most of them are great. If you say

**[07:57]** Most of them are great. If you say

**[07:57]** Most of them are great. If you say here's a 100page document and here's a

**[07:59]** here's a 100page document and here's a

**[07:59]** here's a 100page document and here's a 100 fields that are each of them complex


### [08:00 - 09:00]

**[08:00]** 100 fields that are each of them complex

**[08:00]** 100 fields that are each of them complex with separate instructions, then they it

**[08:02]** with separate instructions, then they it

**[08:02]** with separate instructions, then they it loses track and and I have sympathy

**[08:04]** loses track and and I have sympathy

**[08:04]** loses track and and I have sympathy because people would lose track too. And

**[08:07]** because people would lose track too. And

**[08:07]** because people would lose track too. And so um this became very problematic

**[08:09]** so um this became very problematic

**[08:09]** so um this became very problematic because if you want high accuracy in an

**[08:11]** because if you want high accuracy in an

**[08:11]** because if you want high accuracy in an enterprise setting like this just starts

**[08:13]** enterprise setting like this just starts

**[08:13]** enterprise setting like this just starts to not work. Um and then also just like

**[08:15]** to not work. Um and then also just like

**[08:15]** to not work. Um and then also just like well what is accuracy? What does it mean

**[08:17]** well what is accuracy? What does it mean

**[08:17]** well what is accuracy? What does it mean in the old ML world? They give you

**[08:18]** in the old ML world? They give you

**[08:18]** in the old ML world? They give you confidence scores. 865 is this one

**[08:21]** confidence scores. 865 is this one

**[08:21]** confidence scores. 865 is this one versus and then of course large language

**[08:23]** versus and then of course large language

**[08:23]** versus and then of course large language models don't really know their own

**[08:24]** models don't really know their own

**[08:24]** models don't really know their own accuracy. So we would implement things

**[08:26]** accuracy. So we would implement things

**[08:26]** accuracy. So we would implement things like LM as a judge and we come back and

**[08:28]** like LM as a judge and we come back and

**[08:28]** like LM as a judge and we come back and tell you like here's your extraction.

**[08:30]** tell you like here's your extraction.

**[08:30]** tell you like here's your extraction. also we're not quite sure this is right

**[08:32]** also we're not quite sure this is right

**[08:32]** also we're not quite sure this is right and and then our enterprise customers

**[08:34]** and and then our enterprise customers

**[08:34]** and and then our enterprise customers would kind of be like well that's

**[08:35]** would kind of be like well that's

**[08:35]** would kind of be like well that's helpful to know but like I want it to

**[08:38]** helpful to know but like I want it to

**[08:38]** helpful to know but like I want it to work right not just you tell me it

**[08:39]** work right not just you tell me it

**[08:39]** work right not just you tell me it doesn't work right and so this became

**[08:41]** doesn't work right and so this became

**[08:41]** doesn't work right and so this became this kind of set of challenges that that

**[08:42]** this kind of set of challenges that that

**[08:42]** this kind of set of challenges that that that um we we we focused on and so

**[08:44]** that um we we we focused on and so

**[08:44]** that um we we we focused on and so customers were looking for speed they're

**[08:46]** customers were looking for speed they're

**[08:46]** customers were looking for speed they're looking for affordability they're making

**[08:47]** looking for affordability they're making

**[08:47]** looking for affordability they're making this work they're saying if AI is this

**[08:49]** this work they're saying if AI is this

**[08:49]** this work they're saying if AI is this future awesome thing then like you know

**[08:51]** future awesome thing then like you know

**[08:51]** future awesome thing then like you know show it to me and so and on these more

**[08:53]** show it to me and so and on these more

**[08:54]** show it to me and so and on these more complex documents so at this point we

**[08:57]** complex documents so at this point we

**[08:57]** complex documents so at this point we kind of hit our our despair moment um

**[08:59]** kind of hit our our despair moment um

**[08:59]** kind of hit our our despair moment um our we thought LLM's resolution


### [09:00 - 10:00]

**[09:01]** our we thought LLM's resolution

**[09:02]** our we thought LLM's resolution everything we thought that like we could

**[09:03]** everything we thought that like we could

**[09:03]** everything we thought that like we could have these AI models that worked but um

**[09:05]** have these AI models that worked but um

**[09:05]** have these AI models that worked but um and we actually struggled like what do

**[09:06]** and we actually struggled like what do

**[09:06]** and we actually struggled like what do you do now how do you fix this and I

**[09:08]** you do now how do you fix this and I

**[09:08]** you do now how do you fix this and I know let's just wait until uh the next

**[09:10]** know let's just wait until uh the next

**[09:10]** know let's just wait until uh the next Gemini model or uh you know OpenAI seems

**[09:12]** Gemini model or uh you know OpenAI seems

**[09:12]** Gemini model or uh you know OpenAI seems to be on top of this so like wait till

**[09:14]** to be on top of this so like wait till

**[09:14]** to be on top of this so like wait till the next one which is part of it right

**[09:16]** the next one which is part of it right

**[09:16]** the next one which is part of it right the models do get better but um the

**[09:18]** the models do get better but um the

**[09:18]** the models do get better but um the fragility of the architecture was one

**[09:21]** fragility of the architecture was one

**[09:21]** fragility of the architecture was one that was uh we weren't really going to

**[09:23]** that was uh we weren't really going to

**[09:23]** that was uh we weren't really going to be able to solve on our own so um

**[09:25]** be able to solve on our own so um

**[09:25]** be able to solve on our own so um naturally uh one of the answers uh that

**[09:27]** naturally uh one of the answers uh that

**[09:28]** naturally uh one of the answers uh that we were came up with was um bringing

**[09:31]** we were came up with was um bringing

**[09:31]** we were came up with was um bringing agentic approaches to everything that we

**[09:34]** agentic approaches to everything that we

**[09:34]** agentic approaches to everything that we do. And this is really the the one of

**[09:37]** do. And this is really the the one of

**[09:37]** do. And this is really the the one of the key things that um I want to sort of

**[09:38]** the key things that um I want to sort of

**[09:38]** the key things that um I want to sort of bring out in this session is that um it

**[09:41]** bring out in this session is that um it

**[09:41]** bring out in this session is that um it certainly was not obvious that the way

**[09:42]** certainly was not obvious that the way

**[09:42]** certainly was not obvious that the way to fix all these problems in something

**[09:44]** to fix all these problems in something

**[09:44]** to fix all these problems in something like data extraction was to do a gentic

**[09:47]** like data extraction was to do a gentic

**[09:47]** like data extraction was to do a gentic style of interactions. And when I say

**[09:49]** style of interactions. And when I say

**[09:49]** style of interactions. And when I say agentic, I mean an AI agent that does

**[09:51]** agentic, I mean an AI agent that does

**[09:51]** agentic, I mean an AI agent that does something like this instructions,

**[09:53]** something like this instructions,

**[09:53]** something like this instructions, objectives with the model background

**[09:55]** objectives with the model background

**[09:55]** objectives with the model background tools, we can make have secure access.

**[09:57]** tools, we can make have secure access.

**[09:58]** tools, we can make have secure access. Of course, it has memory from the

**[09:59]** Of course, it has memory from the

**[09:59]** Of course, it has memory from the purposes of of advancing and being able


### [10:00 - 11:00]

**[10:00]** purposes of of advancing and being able

**[10:00]** purposes of of advancing and being able to look up information inside of of of

**[10:02]** to look up information inside of of of

**[10:02]** to look up information inside of of of the system, but also with a uh full uh

**[10:07]** the system, but also with a uh full uh

**[10:07]** the system, but also with a uh full uh directed graph. So the ability to

**[10:09]** directed graph. So the ability to

**[10:09]** directed graph. So the ability to orchestrate it to be able to do things

**[10:11]** orchestrate it to be able to do things

**[10:11]** orchestrate it to be able to do things like where you say do this then this.

**[10:13]** like where you say do this then this.

**[10:13]** like where you say do this then this. Either it comes up with its own plan or

**[10:14]** Either it comes up with its own plan or

**[10:14]** Either it comes up with its own plan or we actually can orchestrate it ourselves

**[10:16]** we actually can orchestrate it ourselves

**[10:16]** we actually can orchestrate it ourselves because we have knowledge of what we

**[10:17]** because we have knowledge of what we

**[10:17]** because we have knowledge of what we want it to do.

**[10:18]** want it to do.

**[10:18]** want it to do. And this was for us um it was

**[10:21]** And this was for us um it was

**[10:21]** And this was for us um it was controversial like it was like our

**[10:22]** controversial like it was like our

**[10:22]** controversial like it was like our engineers like what are you talking

**[10:23]** engineers like what are you talking

**[10:23]** engineers like what are you talking about like let's just make the OCR

**[10:25]** about like let's just make the OCR

**[10:25]** about like let's just make the OCR better like uh like let's just add

**[10:26]** better like uh like let's just add

**[10:26]** better like uh like let's just add another step somewhere like let's just

**[10:28]** another step somewhere like let's just

**[10:28]** another step somewhere like let's just add a post-processing uh regular regular

**[10:30]** add a post-processing uh regular regular

**[10:30]** add a post-processing uh regular regular expression checks and then and then of

**[10:31]** expression checks and then and then of

**[10:32]** expression checks and then and then of course everybody always like I have a

**[10:33]** course everybody always like I have a

**[10:33]** course everybody always like I have a way to do this um based on the old way

**[10:35]** way to do this um based on the old way

**[10:35]** way to do this um based on the old way of doing this why don't we make train ML

**[10:37]** of doing this why don't we make train ML

**[10:37]** of doing this why don't we make train ML model like why don't we fine-tune and

**[10:38]** model like why don't we fine-tune and

**[10:38]** model like why don't we fine-tune and then and and then and then and then and

**[10:39]** then and then and then and then and then and then and then and then and and so

**[10:40]** and then and then and then and and so

**[10:40]** and then and then and then and and so suddenly all of the genericness of it

**[10:41]** suddenly all of the genericness of it

**[10:41]** suddenly all of the genericness of it would be get lost in this process

**[10:44]** would be get lost in this process

**[10:44]** would be get lost in this process so um we came up with a mechanism which

**[10:48]** so um we came up with a mechanism which

**[10:48]** so um we came up with a mechanism which was a uh so this is uh think like kind

**[10:50]** was a uh so this is uh think like kind

**[10:50]** was a uh so this is uh think like kind of langraph style they have agentic

**[10:52]** of langraph style they have agentic

**[10:52]** of langraph style they have agentic capabilities and um so we still we went

**[10:57]** capabilities and um so we still we went

**[10:57]** capabilities and um so we still we went uh we still had the same inputs and

**[10:58]** uh we still had the same inputs and

**[10:58]** uh we still had the same inputs and outputs in document with fields out


### [11:00 - 12:00]

**[11:01]** outputs in document with fields out

**[11:01]** outputs in document with fields out answers however the approach was an

**[11:04]** answers however the approach was an

**[11:04]** answers however the approach was an agentic approach and so um you know we

**[11:07]** agentic approach and so um you know we

**[11:08]** agentic approach and so um you know we played with all the models uh reflecting

**[11:10]** played with all the models uh reflecting

**[11:10]** played with all the models uh reflecting uh back and forth and criticism uh being

**[11:12]** uh back and forth and criticism uh being

**[11:12]** uh back and forth and criticism uh being able to uh uh separate in multiple tasks

**[11:16]** able to uh uh separate in multiple tasks

**[11:16]** able to uh uh separate in multiple tasks uh to be able to have different multi

**[11:17]** uh to be able to have different multi

**[11:17]** uh to be able to have different multi page systems work on this and we ended

**[11:19]** page systems work on this and we ended

**[11:19]** page systems work on this and we ended up with something like this where you

**[11:20]** up with something like this where you

**[11:20]** up with something like this where you have a step where you prepare the fields

**[11:22]** have a step where you prepare the fields

**[11:22]** have a step where you prepare the fields you go through you group the fields we

**[11:24]** you go through you group the fields we

**[11:24]** you go through you group the fields we learned quickly that like if if there's

**[11:26]** learned quickly that like if if there's

**[11:26]** learned quickly that like if if there's like a set of fields that are like

**[11:27]** like a set of fields that are like

**[11:27]** like a set of fields that are like customers uh from a contract and then or

**[11:29]** customers uh from a contract and then or

**[11:29]** customers uh from a contract and then or like like parties and then somewhere

**[11:30]** like like parties and then somewhere

**[11:30]** like like parties and then somewhere else there's like the address of the

**[11:31]** else there's like the address of the

**[11:31]** else there's like the address of the parties like you need the AI to handle

**[11:33]** parties like you need the AI to handle

**[11:33]** parties like you need the AI to handle those together otherwise it's like you

**[11:34]** those together otherwise it's like you

**[11:34]** those together otherwise it's like you have three parties and two sets of

**[11:37]** have three parties and two sets of

**[11:37]** have three parties and two sets of addresses which don't match match so we

**[11:39]** addresses which don't match match so we

**[11:39]** addresses which don't match match so we we so we had to break up intelligently

**[11:41]** we so we had to break up intelligently

**[11:41]** we so we had to break up intelligently the set of fields we had to go through

**[11:42]** the set of fields we had to go through

**[11:42]** the set of fields we had to go through and we had to um uh like uh uh do

**[11:45]** and we had to um uh like uh uh do

**[11:45]** and we had to um uh like uh uh do multiple queries on a document

**[11:47]** multiple queries on a document

**[11:47]** multiple queries on a document Then after we got that, we would then

**[11:49]** Then after we got that, we would then

**[11:49]** Then after we got that, we would then use a set of tools to check and to

**[11:51]** use a set of tools to check and to

**[11:51]** use a set of tools to check and to double check the results. In some cases,

**[11:52]** double check the results. In some cases,

**[11:52]** double check the results. In some cases, we use OCR. We then double check it by

**[11:54]** we use OCR. We then double check it by

**[11:54]** we use OCR. We then double check it by looking at pictures of the pages. Um,

**[11:56]** looking at pictures of the pages. Um,

**[11:56]** looking at pictures of the pages. Um, and and then using multiple models.

**[11:58]** and and then using multiple models.

**[11:58]** and and then using multiple models. Sometimes they vote and they're like,

**[11:59]** Sometimes they vote and they're like,

**[11:59]** Sometimes they vote and they're like, "Wow, like this is a hard question.


### [12:00 - 13:00]

**[12:01]** "Wow, like this is a hard question.

**[12:01]** "Wow, like this is a hard question. Three models from different vendors, two

**[12:03]** Three models from different vendors, two

**[12:03]** Three models from different vendors, two of them think this is the answer. That

**[12:04]** of them think this is the answer. That

**[12:04]** of them think this is the answer. That was probably a good answer." Um, and

**[12:06]** was probably a good answer." Um, and

**[12:06]** was probably a good answer." Um, and then on to the idea of the element as a

**[12:08]** then on to the idea of the element as a

**[12:08]** then on to the idea of the element as a judge. not just a judge to tell you that

**[12:10]** judge. not just a judge to tell you that

**[12:10]** judge. not just a judge to tell you that this is a um this is the answer, but a

**[12:13]** this is a um this is the answer, but a

**[12:13]** this is a um this is the answer, but a judge to tell you uh hey uh here's some

**[12:16]** judge to tell you uh hey uh here's some

**[12:16]** judge to tell you uh hey uh here's some feedback, keep trying. Now, of course,

**[12:18]** feedback, keep trying. Now, of course,

**[12:18]** feedback, keep trying. Now, of course, this takes a little bit longer um but uh

**[12:20]** this takes a little bit longer um but uh

**[12:20]** this takes a little bit longer um but uh this is something that then leads to the

**[12:22]** this is something that then leads to the

**[12:22]** this is something that then leads to the kind of accuracy that you'd want

**[12:23]** kind of accuracy that you'd want

**[12:23]** kind of accuracy that you'd want overall. And so for us, this was the um

**[12:26]** overall. And so for us, this was the um

**[12:26]** overall. And so for us, this was the um the uh uh the architecture that then

**[12:29]** the uh uh the architecture that then

**[12:29]** the uh uh the architecture that then helped us solve a set of problems. And

**[12:32]** helped us solve a set of problems. And

**[12:32]** helped us solve a set of problems. And it became um interesting because every

**[12:34]** it became um interesting because every

**[12:34]** it became um interesting because every time there was a new set of challenges,

**[12:36]** time there was a new set of challenges,

**[12:36]** time there was a new set of challenges, the answer was not rethink everything or

**[12:39]** the answer was not rethink everything or

**[12:39]** the answer was not rethink everything or let's then try like a whole new set of

**[12:41]** let's then try like a whole new set of

**[12:41]** let's then try like a whole new set of like oh you know give us six months and

**[12:43]** like oh you know give us six months and

**[12:43]** like oh you know give us six months and and we'll come up with a new idea but uh

**[12:44]** and we'll come up with a new idea but uh

**[12:44]** and we'll come up with a new idea but uh I wonder if we change that prompt on

**[12:47]** I wonder if we change that prompt on

**[12:47]** I wonder if we change that prompt on that one note or I wonder if we add

**[12:48]** that one note or I wonder if we add

**[12:48]** that one note or I wonder if we add another double check at the end then we

**[12:50]** another double check at the end then we

**[12:50]** another double check at the end then we can actually start to solve this

**[12:51]** can actually start to solve this

**[12:51]** can actually start to solve this problem. So we bring the power of AI

**[12:52]** problem. So we bring the power of AI

**[12:52]** problem. So we bring the power of AI intelligence to help us then solve

**[12:54]** intelligence to help us then solve

**[12:54]** intelligence to help us then solve something that we used to think of as a

**[12:56]** something that we used to think of as a

**[12:56]** something that we used to think of as a standard function.

**[12:58]** standard function.

**[12:58]** standard function. Um, and then not only that, it it helped


### [13:00 - 14:00]

**[13:00]** Um, and then not only that, it it helped

**[13:00]** Um, and then not only that, it it helped us in other ways. Like, so we we're

**[13:02]** us in other ways. Like, so we we're

**[13:02]** us in other ways. Like, so we we're naturally as an unstructured content

**[13:03]** naturally as an unstructured content

**[13:03]** naturally as an unstructured content store, like one of the first things you

**[13:04]** store, like one of the first things you

**[13:04]** store, like one of the first things you always see people if I can give you a

**[13:06]** always see people if I can give you a

**[13:06]** always see people if I can give you a demo right now, it's I have a bunch of

**[13:07]** demo right now, it's I have a bunch of

**[13:07]** demo right now, it's I have a bunch of of documents. I have a question. And

**[13:09]** of documents. I have a question. And

**[13:09]** of documents. I have a question. And then we had the same thing. We had a

**[13:10]** then we had the same thing. We had a

**[13:10]** then we had the same thing. We had a judge and it would be like it would tell

**[13:11]** judge and it would be like it would tell

**[13:11]** judge and it would be like it would tell us like, oh, that was a good answer or

**[13:12]** us like, oh, that was a good answer or

**[13:12]** us like, oh, that was a good answer or that wasn't. And then why not just if

**[13:15]** that wasn't. And then why not just if

**[13:15]** that wasn't. And then why not just if it's not a good answer, we'll take

**[13:17]** it's not a good answer, we'll take

**[13:17]** it's not a good answer, we'll take another bait and and tell the AI like,

**[13:19]** another bait and and tell the AI like,

**[13:19]** another bait and and tell the AI like, uh, try again. Before you tell the user

**[13:21]** uh, try again. Before you tell the user

**[13:21]** uh, try again. Before you tell the user this answer, like I want you to um, uh,

**[13:24]** this answer, like I want you to um, uh,

**[13:24]** this answer, like I want you to um, uh, like reflect on it for a second. And

**[13:25]** like reflect on it for a second. And

**[13:25]** like reflect on it for a second. And this kind of thing just leads to higher

**[13:27]** this kind of thing just leads to higher

**[13:27]** this kind of thing just leads to higher accuracy. And then it also leads to much

**[13:29]** accuracy. And then it also leads to much

**[13:29]** accuracy. And then it also leads to much more complexity. So we just announced

**[13:31]** more complexity. So we just announced

**[13:31]** more complexity. So we just announced our deep research capabilities on your

**[13:32]** our deep research capabilities on your

**[13:32]** our deep research capabilities on your content. So in the same way that like

**[13:34]** content. So in the same way that like

**[13:34]** content. So in the same way that like OpenAI or Gemini does deep research on

**[13:36]** OpenAI or Gemini does deep research on

**[13:36]** OpenAI or Gemini does deep research on the internet, we let you do deep

**[13:37]** the internet, we let you do deep

**[13:37]** the internet, we let you do deep research on your data in box would look

**[13:39]** research on your data in box would look

**[13:39]** research on your data in box would look something like this. So this would be

**[13:40]** something like this. So this would be

**[13:40]** something like this. So this would be like roughly the the directed graph that

**[13:42]** like roughly the the directed graph that

**[13:42]** like roughly the the directed graph that you'd have where you go through you know

**[13:45]** you'd have where you go through you know

**[13:45]** you'd have where you go through you know first we searched for the data kind of

**[13:46]** first we searched for the data kind of

**[13:46]** first we searched for the data kind of do that for a while figure out what's

**[13:47]** do that for a while figure out what's

**[13:47]** do that for a while figure out what's relevant double check then make an

**[13:49]** relevant double check then make an

**[13:49]** relevant double check then make an outline kind of prepare a plan go

**[13:50]** outline kind of prepare a plan go

**[13:50]** outline kind of prepare a plan go through um um make make a a process. So

**[13:53]** through um um make make a a process. So

**[13:53]** through um um make make a a process. So this is all agentic thinking and it and

**[13:56]** this is all agentic thinking and it and

**[13:56]** this is all agentic thinking and it and and this kind of thing wouldn't really

**[13:57]** and this kind of thing wouldn't really

**[13:57]** and this kind of thing wouldn't really be possible if we hadn't kind of laid

**[13:59]** be possible if we hadn't kind of laid

**[13:59]** be possible if we hadn't kind of laid the fra the framework of having an


### [14:00 - 15:00]

**[14:00]** the fra the framework of having an

**[14:00]** the fra the framework of having an agentic foundation overall.

**[14:03]** agentic foundation overall.

**[14:03]** agentic foundation overall. So um I will leave you with uh these uh

**[14:06]** So um I will leave you with uh these uh

**[14:06]** So um I will leave you with uh these uh a few lessons learned here. Um so this

**[14:08]** a few lessons learned here. Um so this

**[14:08]** a few lessons learned here. Um so this is based on our time in the last few

**[14:10]** is based on our time in the last few

**[14:10]** is based on our time in the last few years. Um the first is uh that um it

**[14:14]** years. Um the first is uh that um it

**[14:14]** years. Um the first is uh that um it wasn't obvious to us at first but the

**[14:17]** wasn't obvious to us at first but the

**[14:17]** wasn't obvious to us at first but the agentic uh abstraction layer from an

**[14:19]** agentic uh abstraction layer from an

**[14:19]** agentic uh abstraction layer from an architecture perspective is actually

**[14:20]** architecture perspective is actually

**[14:20]** architecture perspective is actually quite clean. It is it is very um once

**[14:23]** quite clean. It is it is very um once

**[14:24]** quite clean. It is it is very um once you start to think this way it is very

**[14:25]** you start to think this way it is very

**[14:25]** you start to think this way it is very natural to think I'm going to run an

**[14:27]** natural to think I'm going to run an

**[14:27]** natural to think I'm going to run an intelligent workflow intelligent

**[14:29]** intelligent workflow intelligent

**[14:29]** intelligent workflow intelligent directed graph powered by a models are

**[14:30]** directed graph powered by a models are

**[14:30]** directed graph powered by a models are every step to be able to accomplish a

**[14:32]** every step to be able to accomplish a

**[14:32]** every step to be able to accomplish a task not everything but sometimes that's

**[14:34]** task not everything but sometimes that's

**[14:34]** task not everything but sometimes that's a great that's a great approach and this

**[14:36]** a great that's a great approach and this

**[14:36]** a great that's a great approach and this and this is independent of some of a

**[14:39]** and this is independent of some of a

**[14:39]** and this is independent of some of a highcale set of of sort of distributed

**[14:41]** highcale set of of sort of distributed

**[14:41]** highcale set of of sort of distributed system design and and in both are

**[14:43]** system design and and in both are

**[14:43]** system design and and in both are important like at some point you have to

**[14:44]** important like at some point you have to

**[14:44]** important like at some point you have to deal with you know 100 million documents

**[14:46]** deal with you know 100 million documents

**[14:46]** deal with you know 100 million documents that day at the same other point you

**[14:47]** that day at the same other point you

**[14:47]** that day at the same other point you have to deal with that one and so being

**[14:49]** have to deal with that one and so being

**[14:49]** have to deal with that one and so being able to separate these two systems into

**[14:51]** able to separate these two systems into

**[14:51]** able to separate these two systems into like somebody who thinks about the

**[14:52]** like somebody who thinks about the

**[14:52]** like somebody who thinks about the agentic framework and somebody who

**[14:53]** agentic framework and somebody who

**[14:53]** agentic framework and somebody who thinks about the the how to scale a

**[14:56]** thinks about the the how to scale a

**[14:56]** thinks about the the how to scale a generic process is this is this is very

**[14:58]** generic process is this is this is very

**[14:58]** generic process is this is this is very helpful to keep these distinct. Um, also


### [15:00 - 16:00]

**[15:00]** helpful to keep these distinct. Um, also

**[15:00]** helpful to keep these distinct. Um, also it's just easy to evolve. Like, uh, in

**[15:02]** it's just easy to evolve. Like, uh, in

**[15:02]** it's just easy to evolve. Like, uh, in that deep research example, one of our

**[15:04]** that deep research example, one of our

**[15:04]** that deep research example, one of our biggest we we we did it and then it

**[15:05]** biggest we we we did it and then it

**[15:06]** biggest we we we did it and then it worked really well except for the output

**[15:07]** worked really well except for the output

**[15:07]** worked really well except for the output was kind of sloppy and so we were like,

**[15:09]** was kind of sloppy and so we were like,

**[15:09]** was kind of sloppy and so we were like, ah, I guess we got to redesign the whole

**[15:10]** ah, I guess we got to redesign the whole

**[15:10]** ah, I guess we got to redesign the whole thing or add another note at the end to

**[15:13]** thing or add another note at the end to

**[15:13]** thing or add another note at the end to say summarize this in according to this

**[15:14]** say summarize this in according to this

**[15:14]** say summarize this in according to this and it would just take that in and just

**[15:17]** and it would just take that in and just

**[15:17]** and it would just take that in and just redo the output. Took not that long to

**[15:19]** redo the output. Took not that long to

**[15:19]** redo the output. Took not that long to fix. And this was something that was not

**[15:21]** fix. And this was something that was not

**[15:21]** fix. And this was something that was not obvious to me until later, which is that

**[15:24]** obvious to me until later, which is that

**[15:24]** obvious to me until later, which is that um if you're going to be using um a

**[15:26]** um if you're going to be using um a

**[15:26]** um if you're going to be using um a aentic uh uh AI with a team who's been

**[15:29]** aentic uh uh AI with a team who's been

**[15:29]** aentic uh uh AI with a team who's been around for a while, like you start to

**[15:30]** around for a while, like you start to

**[15:30]** around for a while, like you start to need to get them to think about agentic

**[15:33]** need to get them to think about agentic

**[15:33]** need to get them to think about agentic first kind of thinking, AI first

**[15:34]** first kind of thinking, AI first

**[15:34]** first kind of thinking, AI first thinking. And one way to do that is to

**[15:37]** thinking. And one way to do that is to

**[15:37]** thinking. And one way to do that is to um let them build something so they can

**[15:38]** um let them build something so they can

**[15:38]** um let them build something so they can start to think, oh, like this is not

**[15:40]** start to think, oh, like this is not

**[15:40]** start to think, oh, like this is not only how we can build more things, but

**[15:41]** only how we can build more things, but

**[15:42]** only how we can build more things, but also because we're also a platform for

**[15:44]** also because we're also a platform for

**[15:44]** also because we're also a platform for our enterprise customers, they can think

**[15:45]** our enterprise customers, they can think

**[15:45]** our enterprise customers, they can think about how to make it better make it

**[15:47]** about how to make it better make it

**[15:47]** about how to make it better make it better for them. So things like uh

**[15:49]** better for them. So things like uh

**[15:49]** better for them. So things like uh really doubling down on the idea of um

**[15:51]** really doubling down on the idea of um

**[15:51]** really doubling down on the idea of um we we publish MCP servers, what are the

**[15:53]** we we publish MCP servers, what are the

**[15:53]** we we publish MCP servers, what are the tools like for them, what can we do to

**[15:55]** tools like for them, what can we do to

**[15:55]** tools like for them, what can we do to make it easier, how can we do our agent

**[15:56]** make it easier, how can we do our agent

**[15:56]** make it easier, how can we do our agent to agent communications and so on.

**[15:59]** to agent communications and so on.

**[15:59]** to agent communications and so on. So um this is uh all kind of summed up


### [16:00 - 17:00]

**[16:03]** So um this is uh all kind of summed up

**[16:03]** So um this is uh all kind of summed up with is if you're confronted with a

**[16:05]** with is if you're confronted with a

**[16:05]** with is if you're confronted with a challenge, the lesson that we learned is

**[16:08]** challenge, the lesson that we learned is

**[16:08]** challenge, the lesson that we learned is that if it's plausible that an a set of

**[16:10]** that if it's plausible that an a set of

**[16:10]** that if it's plausible that an a set of AI models uh could help you solve that

**[16:13]** AI models uh could help you solve that

**[16:13]** AI models uh could help you solve that problem, then you should build this AI

**[16:14]** problem, then you should build this AI

**[16:14]** problem, then you should build this AI agentic architecture early. If I go back

**[16:16]** agentic architecture early. If I go back

**[16:16]** agentic architecture early. If I go back in time, I would wish to done this

**[16:17]** in time, I would wish to done this

**[16:18]** in time, I would wish to done this sooner because then we'd kind of be have

**[16:20]** sooner because then we'd kind of be have

**[16:20]** sooner because then we'd kind of be have been able to continue to take advantage

**[16:21]** been able to continue to take advantage

**[16:21]** been able to continue to take advantage of that. Um, and so that's my uh that's

**[16:24]** of that. Um, and so that's my uh that's

**[16:24]** of that. Um, and so that's my uh that's my journey and that's my my my lesson

**[16:25]** my journey and that's my my my lesson

**[16:25]** my journey and that's my my my lesson for you. Uh, so thank you

**[16:36]** uh an are we um

**[16:36]** uh an are we um two minutes. Okay. So um if any what

**[16:39]** two minutes. Okay. So um if any what

**[16:39]** two minutes. Okay. So um if any what >> two questions okay if anybody has any

**[16:41]** >> two questions okay if anybody has any

**[16:41]** >> two questions okay if anybody has any questions I'm happy to answer them

**[16:46]** >> uh question being is this available as

**[16:46]** >> uh question being is this available as API? Yes. Um so we are very API first

**[16:49]** API? Yes. Um so we are very API first

**[16:49]** API? Yes. Um so we are very API first oriented. So we have an agent API that

**[16:51]** oriented. So we have an agent API that

**[16:51]** oriented. So we have an agent API that you can call upon these agents to do

**[16:52]** you can call upon these agents to do

**[16:52]** you can call upon these agents to do things and give them the arguments. So

**[16:53]** things and give them the arguments. So

**[16:53]** things and give them the arguments. So yes uh we we we provide

**[16:56]** yes uh we we we provide

**[16:56]** yes uh we we we provide agent uh just APIs across everything and

**[16:58]** agent uh just APIs across everything and

**[16:58]** agent uh just APIs across everything and tools um to to call our APIs.


### [17:00 - 18:00]

**[17:07]** Um

**[17:07]** Um >> okay

**[17:18]** think when you start using a more manual

**[17:18]** think when you start using a more manual approach as well.

**[17:19]** approach as well.

**[17:19]** approach as well. >> Um in terms of evaluating our agents and

**[17:21]** >> Um in terms of evaluating our agents and

**[17:21]** >> Um in terms of evaluating our agents and how do we do that? Um so we we not only

**[17:23]** how do we do that? Um so we we not only

**[17:23]** how do we do that? Um so we we not only use LM as a judge but we also create

**[17:25]** use LM as a judge but we also create

**[17:25]** use LM as a judge but we also create eval sets. So we have our standard set

**[17:26]** eval sets. So we have our standard set

**[17:26]** eval sets. So we have our standard set of eval sets. Um and then we've learned

**[17:28]** of eval sets. Um and then we've learned

**[17:28]** of eval sets. Um and then we've learned that um since the gets go so good over

**[17:29]** that um since the gets go so good over

**[17:29]** that um since the gets go so good over time we created a challenge set of of

**[17:31]** time we created a challenge set of of

**[17:31]** time we created a challenge set of of eval sets to so that we can better

**[17:33]** eval sets to so that we can better

**[17:33]** eval sets to so that we can better explore like things that not everybody

**[17:34]** explore like things that not everybody

**[17:34]** explore like things that not everybody asked but if they did it would be really

**[17:36]** asked but if they did it would be really

**[17:36]** asked but if they did it would be really hard and then that way you can better

**[17:37]** hard and then that way you can better

**[17:38]** hard and then that way you can better decide on whether or not you're not only

**[17:39]** decide on whether or not you're not only

**[17:39]** decide on whether or not you're not only prepared for now but as people get more

**[17:41]** prepared for now but as people get more

**[17:41]** prepared for now but as people get more challenging things we we know that we

**[17:43]** challenging things we we know that we

**[17:43]** challenging things we we know that we can grow across that. So a mixture of

**[17:45]** can grow across that. So a mixture of

**[17:45]** can grow across that. So a mixture of eval plus as a judge plus the idea of

**[17:48]** eval plus as a judge plus the idea of

**[17:48]** eval plus as a judge plus the idea of just having people give feedback. We we

**[17:50]** just having people give feedback. We we

**[17:50]** just having people give feedback. We we have limited ability to look as an

**[17:51]** have limited ability to look as an

**[17:51]** have limited ability to look as an enterprise company what happening but

**[17:52]** enterprise company what happening but

**[17:52]** enterprise company what happening but the the the idea of them telling us this

**[17:54]** the the the idea of them telling us this

**[17:54]** the the the idea of them telling us this is still useful in all cases


### [18:00 - 19:00]

**[18:04]** >> you can yell if you want I'll hear you

**[18:04]** >> you can yell if you want I'll hear you >> so

**[18:06]** >> so

**[18:06]** >> so apologies if

**[18:08]** apologies if

**[18:08]** apologies if you seems like you're mostly building

**[18:11]** you seems like you're mostly building

**[18:11]** you seems like you're mostly building agents but at least together you know by

**[18:16]** agents but at least together you know by

**[18:16]** agents but at least together you know by >> uh so the question being why bother with

**[18:18]** >> uh so the question being why bother with

**[18:18]** >> uh so the question being why bother with agents if you can find tune a model. Um,

**[18:20]** agents if you can find tune a model. Um,

**[18:20]** agents if you can find tune a model. Um, >> no.

**[18:21]** >> no.

**[18:21]** >> no. >> Have you tried Have you tried

**[18:22]** >> Have you tried Have you tried

**[18:22]** >> Have you tried Have you tried fine-tuning agents?

**[18:24]** fine-tuning agents?

**[18:24]** fine-tuning agents? >> We're um we're pretty anti- fine-tuning

**[18:27]** >> We're um we're pretty anti- fine-tuning

**[18:27]** >> We're um we're pretty anti- fine-tuning at this moment because um of the

**[18:29]** at this moment because um of the

**[18:29]** at this moment because um of the challenges of once you fine-tune

**[18:31]** challenges of once you fine-tune

**[18:31]** challenges of once you fine-tune something, you have to then fine-tune

**[18:32]** something, you have to then fine-tune

**[18:32]** something, you have to then fine-tune all of the evolutions of them going

**[18:34]** all of the evolutions of them going

**[18:34]** all of the evolutions of them going forward. We support mult multiple

**[18:36]** forward. We support mult multiple

**[18:36]** forward. We support mult multiple models, Gemini, Llama, OpenAI,

**[18:39]** models, Gemini, Llama, OpenAI,

**[18:39]** models, Gemini, Llama, OpenAI, Anthropic, and it's just hard to

**[18:40]** Anthropic, and it's just hard to

**[18:40]** Anthropic, and it's just hard to consistently fine-tune across the board

**[18:42]** consistently fine-tune across the board

**[18:42]** consistently fine-tune across the board in ways that like not only and usually

**[18:45]** in ways that like not only and usually

**[18:45]** in ways that like not only and usually just the next version of the model gets

**[18:46]** just the next version of the model gets

**[18:46]** just the next version of the model gets better. So we've we've got to the point

**[18:48]** better. So we've we've got to the point

**[18:48]** better. So we've we've got to the point where we use use prompts or cache

**[18:49]** where we use use prompts or cache

**[18:49]** where we use use prompts or cache prompts or agenticness as opposed to

**[18:50]** prompts or agenticness as opposed to

**[18:50]** prompts or agenticness as opposed to fine-tuning. That's the approach for our

**[18:52]** fine-tuning. That's the approach for our

**[18:52]** fine-tuning. That's the approach for our particular use cases that works quite

**[18:53]** particular use cases that works quite

**[18:53]** particular use cases that works quite well.

**[18:56]** well.

**[18:56]** well. Okay, thank you everyone.

**[18:59]** Okay, thank you everyone.

**[18:59]** Okay, thank you everyone. [Music]


