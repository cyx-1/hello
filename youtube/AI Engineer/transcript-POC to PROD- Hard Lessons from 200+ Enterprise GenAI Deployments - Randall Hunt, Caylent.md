# POC to PROD- Hard Lessons from 200+ Enterprise GenAI Deployments - Randall Hunt, Caylent

**Video URL:** https://www.youtube.com/watch?v=vW8wLsb3Nnc

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Everybody excited? So, uh, what does

**[00:16]** Everybody excited? So, uh, what does Kalin do? We build stuff for people. So,

**[00:18]** Kalin do? We build stuff for people. So,

**[00:18]** Kalin do? We build stuff for people. So, people come to us with ideas and they're

**[00:19]** people come to us with ideas and they're

**[00:20]** people come to us with ideas and they're like, I want to make an app or like, oh,

**[00:21]** like, I want to make an app or like, oh,

**[00:21]** like, I want to make an app or like, oh, I want to move off of Oracle onto

**[00:23]** I want to move off of Oracle onto

**[00:23]** I want to move off of Oracle onto Postgress, you know. And we just do that

**[00:24]** Postgress, you know. And we just do that

**[00:24]** Postgress, you know. And we just do that stuff. We are builders. We uh created a

**[00:28]** stuff. We are builders. We uh created a

**[00:28]** stuff. We are builders. We uh created a company by hiring a bunch of passionate

**[00:30]** company by hiring a bunch of passionate

**[00:30]** company by hiring a bunch of passionate autodidacts with a little bit of product

**[00:31]** autodidacts with a little bit of product

**[00:31]** autodidacts with a little bit of product ADHD. And we jump around to all these

**[00:34]** ADHD. And we jump around to all these

**[00:34]** ADHD. And we jump around to all these different things and build cool things

**[00:35]** different things and build cool things

**[00:35]** different things and build cool things for our customers. And we have hundreds

**[00:37]** for our customers. And we have hundreds

**[00:37]** for our customers. And we have hundreds of customers at any given time. Everyone

**[00:38]** of customers at any given time. Everyone

**[00:38]** of customers at any given time. Everyone from like the Fortune 500 to startups.

**[00:41]** from like the Fortune 500 to startups.

**[00:41]** from like the Fortune 500 to startups. And it's a very fun gig. It's really

**[00:44]** And it's a very fun gig. It's really

**[00:44]** And it's a very fun gig. It's really cool. You get exposed to a lot of

**[00:45]** cool. You get exposed to a lot of

**[00:46]** cool. You get exposed to a lot of technology. And what we've learned is

**[00:48]** technology. And what we've learned is

**[00:48]** technology. And what we've learned is that uh generative AI is not the the

**[00:52]** that uh generative AI is not the the

**[00:52]** that uh generative AI is not the the magical pill that solves everything that

**[00:54]** magical pill that solves everything that

**[00:54]** magical pill that solves everything that a lot of people seem to think it is. Uh

**[00:56]** a lot of people seem to think it is. Uh

**[00:56]** a lot of people seem to think it is. Uh and then what your CTO read in the Wall

**[00:59]** and then what your CTO read in the Wall

**[00:59]** and then what your CTO read in the Wall Street Journal is not necessarily the


### [01:00 - 02:00]

**[01:00]** Street Journal is not necessarily the

**[01:00]** Street Journal is not necessarily the latest and greatest thing. And we'll

**[01:02]** latest and greatest thing. And we'll

**[01:02]** latest and greatest thing. And we'll share some concrete components of that.

**[01:04]** share some concrete components of that.

**[01:04]** share some concrete components of that. Uh but I'll just point out a couple of

**[01:06]** Uh but I'll just point out a couple of

**[01:06]** Uh but I'll just point out a couple of different customers here. One of the

**[01:07]** different customers here. One of the

**[01:07]** different customers here. One of the ones is Brainbox AI. So they are a uh

**[01:12]** ones is Brainbox AI. So they are a uh

**[01:12]** ones is Brainbox AI. So they are a uh building operating system. They help

**[01:15]** building operating system. They help

**[01:15]** building operating system. They help decarbonize the built environment. So

**[01:17]** decarbonize the built environment. So

**[01:17]** decarbonize the built environment. So they manage uh tens of thousands of

**[01:19]** they manage uh tens of thousands of

**[01:19]** they manage uh tens of thousands of buildings across the United States and

**[01:21]** buildings across the United States and

**[01:21]** buildings across the United States and Canada or North America and they manage

**[01:23]** Canada or North America and they manage

**[01:23]** Canada or North America and they manage the HVAC systems. And we built an agent

**[01:26]** the HVAC systems. And we built an agent

**[01:26]** the HVAC systems. And we built an agent for them for helping uh with that uh

**[01:30]** for them for helping uh with that uh

**[01:30]** for them for helping uh with that uh decarbonization of the built environment

**[01:32]** decarbonization of the built environment

**[01:32]** decarbonization of the built environment and managing those things. And that was

**[01:34]** and managing those things. And that was

**[01:34]** and managing those things. And that was uh I think in the Times 100 best

**[01:37]** uh I think in the Times 100 best

**[01:37]** uh I think in the Times 100 best inventions of the year or something

**[01:38]** inventions of the year or something

**[01:38]** inventions of the year or something because it helps drastically reduce

**[01:40]** because it helps drastically reduce

**[01:40]** because it helps drastically reduce greenhouse emissions. Uh and then

**[01:41]** greenhouse emissions. Uh and then

**[01:41]** greenhouse emissions. Uh and then Simmons is uh water management

**[01:43]** Simmons is uh water management

**[01:43]** Simmons is uh water management conservation which we also implemented

**[01:45]** conservation which we also implemented

**[01:45]** conservation which we also implemented with AI. Uh and with that, you know,

**[01:47]** with AI. Uh and with that, you know,

**[01:47]** with AI. Uh and with that, you know, there's a couple other customers here.

**[01:49]** there's a couple other customers here.

**[01:49]** there's a couple other customers here. Pipes AI, virtual moving technologies,

**[01:51]** Pipes AI, virtual moving technologies,

**[01:51]** Pipes AI, virtual moving technologies, Z5 inventory. Uh but I thought it'd be

**[01:53]** Z5 inventory. Uh but I thought it'd be

**[01:53]** Z5 inventory. Uh but I thought it'd be cool to just show a demo. And one of the

**[01:55]** cool to just show a demo. And one of the

**[01:55]** cool to just show a demo. And one of the things that I'm most interested in right

**[01:57]** things that I'm most interested in right

**[01:57]** things that I'm most interested in right now is multimodal search and uh semantic


### [02:00 - 03:00]

**[02:00]** now is multimodal search and uh semantic

**[02:00]** now is multimodal search and uh semantic understanding of videos. So this is one

**[02:03]** understanding of videos. So this is one

**[02:03]** understanding of videos. So this is one of our customers, Nature Footage. They

**[02:05]** of our customers, Nature Footage. They

**[02:05]** of our customers, Nature Footage. They have uh a ton of stock footage of, you

**[02:07]** have uh a ton of stock footage of, you

**[02:07]** have uh a ton of stock footage of, you know, lions and tigers and bears. Oh my.

**[02:10]** know, lions and tigers and bears. Oh my.

**[02:10]** know, lions and tigers and bears. Oh my. and crocodiles I suppose and we needed

**[02:12]** and crocodiles I suppose and we needed

**[02:12]** and crocodiles I suppose and we needed to index all of that and make it

**[02:13]** to index all of that and make it

**[02:14]** to index all of that and make it searchable over uh not just a vector

**[02:16]** searchable over uh not just a vector

**[02:16]** searchable over uh not just a vector index but also like a caption. So we

**[02:19]** index but also like a caption. So we

**[02:19]** index but also like a caption. So we leverage the Nova Pro models to generate

**[02:22]** leverage the Nova Pro models to generate

**[02:22]** leverage the Nova Pro models to generate understandings and timestamps and

**[02:24]** understandings and timestamps and

**[02:24]** understandings and timestamps and features of these videos store all of

**[02:26]** features of these videos store all of

**[02:26]** features of these videos store all of those in elastic search and then we are

**[02:28]** those in elastic search and then we are

**[02:28]** those in elastic search and then we are able to search on them and one of the

**[02:30]** able to search on them and one of the

**[02:30]** able to search on them and one of the most important things there is that we

**[02:31]** most important things there is that we

**[02:31]** most important things there is that we were able to build uh a pooling

**[02:33]** were able to build uh a pooling

**[02:33]** were able to build uh a pooling embedding. So by taking frame samples

**[02:35]** embedding. So by taking frame samples

**[02:36]** embedding. So by taking frame samples and pulling the embeddings uh of those

**[02:38]** and pulling the embeddings uh of those

**[02:38]** and pulling the embeddings uh of those frames, we can do a multimodal embedding

**[02:40]** frames, we can do a multimodal embedding

**[02:40]** frames, we can do a multimodal embedding and search with text for the images. And

**[02:42]** and search with text for the images. And

**[02:42]** and search with text for the images. And that's provided through the Titan v2

**[02:44]** that's provided through the Titan v2

**[02:44]** that's provided through the Titan v2 multimodal embeddings.

**[02:46]** multimodal embeddings.

**[02:46]** multimodal embeddings. So uh I thought we'd take a look at a

**[02:49]** So uh I thought we'd take a look at a

**[02:49]** So uh I thought we'd take a look at a different architecture.

**[02:51]** different architecture.

**[02:51]** different architecture. I hope no one here is from Michigan

**[02:53]** I hope no one here is from Michigan

**[02:53]** I hope no one here is from Michigan because that's a terrible team. I hate

**[02:54]** because that's a terrible team. I hate

**[02:54]** because that's a terrible team. I hate them. Anyway, anyone remember March

**[02:56]** them. Anyway, anyone remember March

**[02:56]** them. Anyway, anyone remember March Madness? So, this is another customer of

**[02:59]** Madness? So, this is another customer of

**[02:59]** Madness? So, this is another customer of ours that uh I'm not going to reveal


### [03:00 - 04:00]

**[03:01]** ours that uh I'm not going to reveal

**[03:01]** ours that uh I'm not going to reveal their name, but essentially we have a

**[03:02]** their name, but essentially we have a

**[03:02]** their name, but essentially we have a ton of sports footage that we're

**[03:04]** ton of sports footage that we're

**[03:04]** ton of sports footage that we're processing both in real time and in

**[03:05]** processing both in real time and in

**[03:05]** processing both in real time and in batch, archival and in real time. And

**[03:07]** batch, archival and in real time. And

**[03:08]** batch, archival and in real time. And what we'll do is we'll split that data

**[03:09]** what we'll do is we'll split that data

**[03:09]** what we'll do is we'll split that data into the audio. We'll generate the

**[03:11]** into the audio. We'll generate the

**[03:11]** into the audio. We'll generate the transcription. Fun fact, if you're

**[03:12]** transcription. Fun fact, if you're

**[03:12]** transcription. Fun fact, if you're looking for highlights, the easiest

**[03:14]** looking for highlights, the easiest

**[03:14]** looking for highlights, the easiest thing to do is just ffmpeg get an

**[03:15]** thing to do is just ffmpeg get an

**[03:15]** thing to do is just ffmpeg get an amplitude spectrograph of the audio and

**[03:17]** amplitude spectrograph of the audio and

**[03:17]** amplitude spectrograph of the audio and look for the audience cheering and lo

**[03:19]** look for the audience cheering and lo

**[03:19]** look for the audience cheering and lo and behold, you have your highlight

**[03:20]** and behold, you have your highlight

**[03:20]** and behold, you have your highlight reel. Um, very simple hack right there.

**[03:23]** reel. Um, very simple hack right there.

**[03:23]** reel. Um, very simple hack right there. And we'll take that and we'll generate

**[03:24]** And we'll take that and we'll generate

**[03:24]** And we'll take that and we'll generate embeddings from both the text and from

**[03:26]** embeddings from both the text and from

**[03:26]** embeddings from both the text and from the video itself. And we'll be able to

**[03:29]** the video itself. And we'll be able to

**[03:29]** the video itself. And we'll be able to uh identify certain behaviors with a

**[03:31]** uh identify certain behaviors with a

**[03:31]** uh identify certain behaviors with a certain vector and a certain confidence.

**[03:33]** certain vector and a certain confidence.

**[03:33]** certain vector and a certain confidence. And we'll store those then into a

**[03:36]** And we'll store those then into a

**[03:36]** And we'll store those then into a database. Oh, I think I paused the video

**[03:38]** database. Oh, I think I paused the video

**[03:38]** database. Oh, I think I paused the video by accident. My apologies. No, I didn't.

**[03:42]** by accident. My apologies. No, I didn't.

**[03:42]** by accident. My apologies. No, I didn't. And then we'll use something like Amazon

**[03:44]** And then we'll use something like Amazon

**[03:44]** And then we'll use something like Amazon end user messaging or SNS or whatever.

**[03:46]** end user messaging or SNS or whatever.

**[03:46]** end user messaging or SNS or whatever. we'll send a push notification to our

**[03:47]** we'll send a push notification to our

**[03:48]** we'll send a push notification to our end users and say, "Look, we found uh a

**[03:50]** end users and say, "Look, we found uh a

**[03:50]** end users and say, "Look, we found uh a three-pointer or uh we found this other

**[03:53]** three-pointer or uh we found this other

**[03:53]** three-pointer or uh we found this other thing." And what we found is um you

**[03:55]** thing." And what we found is um you

**[03:55]** thing." And what we found is um you don't even have to take the the raw

**[03:57]** don't even have to take the the raw

**[03:57]** don't even have to take the the raw video. A a tiny little bit of annotation


### [04:00 - 05:00]

**[04:00]** video. A a tiny little bit of annotation

**[04:00]** video. A a tiny little bit of annotation can do wonders um for the video

**[04:03]** can do wonders um for the video

**[04:03]** can do wonders um for the video understanding models at the as they

**[04:05]** understanding models at the as they

**[04:05]** understanding models at the as they exist right now. The soda models still

**[04:07]** exist right now. The soda models still

**[04:07]** exist right now. The soda models still just with a little tiny bit of uh

**[04:09]** just with a little tiny bit of uh

**[04:09]** just with a little tiny bit of uh augmentation on the video will

**[04:11]** augmentation on the video will

**[04:11]** augmentation on the video will outperform um what you can get with an

**[04:14]** outperform um what you can get with an

**[04:14]** outperform um what you can get with an unmodified video. And what I mean by

**[04:16]** unmodified video. And what I mean by

**[04:16]** unmodified video. And what I mean by that is if you have static camera angles

**[04:19]** that is if you have static camera angles

**[04:19]** that is if you have static camera angles and you annotate on the court where the

**[04:21]** and you annotate on the court where the

**[04:21]** and you annotate on the court where the three-pointer line is with a big blue

**[04:22]** three-pointer line is with a big blue

**[04:22]** three-pointer line is with a big blue line and then you just ask the model

**[04:24]** line and then you just ask the model

**[04:24]** line and then you just ask the model questions like did the player cross the

**[04:26]** questions like did the player cross the

**[04:26]** questions like did the player cross the big blue line. Lo and behold you get way

**[04:28]** big blue line. Lo and behold you get way

**[04:28]** big blue line. Lo and behold you get way better results and it takes you know

**[04:29]** better results and it takes you know

**[04:29]** better results and it takes you know seconds and you can even have something

**[04:31]** seconds and you can even have something

**[04:31]** seconds and you can even have something like SAM 2 which is another model from

**[04:32]** like SAM 2 which is another model from

**[04:32]** like SAM 2 which is another model from meta go and do some of those annotations

**[04:34]** meta go and do some of those annotations

**[04:34]** meta go and do some of those annotations for you. So that's an architecture.

**[04:37]** for you. So that's an architecture.

**[04:37]** for you. So that's an architecture. You'll notice that I've put up a couple

**[04:39]** You'll notice that I've put up a couple

**[04:39]** You'll notice that I've put up a couple of different databases there. We had uh

**[04:41]** of different databases there. We had uh

**[04:41]** of different databases there. We had uh Postgress PG vector uh which is my

**[04:43]** Postgress PG vector uh which is my

**[04:44]** Postgress PG vector uh which is my favorite right now. We had open search.

**[04:46]** favorite right now. We had open search.

**[04:46]** favorite right now. We had open search. That's another implementation of vector

**[04:47]** That's another implementation of vector

**[04:47]** That's another implementation of vector search there. Um, but anyway, why should

**[04:50]** search there. Um, but anyway, why should

**[04:50]** search there. Um, but anyway, why should you listen to me? Hi, I'm Randall. Um, I

**[04:54]** you listen to me? Hi, I'm Randall. Um, I

**[04:54]** you listen to me? Hi, I'm Randall. Um, I got started out hacking and building

**[04:56]** got started out hacking and building

**[04:56]** got started out hacking and building stuff and uh playing video games and

**[04:58]** stuff and uh playing video games and

**[04:58]** stuff and uh playing video games and hacking into video games. It turns out


### [05:00 - 06:00]

**[05:00]** hacking into video games. It turns out

**[05:00]** hacking into video games. It turns out that's super illegal. Did not know that.

**[05:02]** that's super illegal. Did not know that.

**[05:02]** that's super illegal. Did not know that. Um, and then I went on to do some

**[05:04]** Um, and then I went on to do some

**[05:04]** Um, and then I went on to do some physics stuff at NASA. Uh, I joined a

**[05:06]** physics stuff at NASA. Uh, I joined a

**[05:06]** physics stuff at NASA. Uh, I joined a small company called Tenen, which became

**[05:07]** small company called Tenen, which became

**[05:08]** small company called Tenen, which became MongoDB. They IPOed. Um, I was an idiot

**[05:11]** MongoDB. They IPOed. Um, I was an idiot

**[05:11]** MongoDB. They IPOed. Um, I was an idiot and sold all my stock before the IPO.

**[05:13]** and sold all my stock before the IPO.

**[05:13]** and sold all my stock before the IPO. Uh, and then I worked at SpaceX where I

**[05:15]** Uh, and then I worked at SpaceX where I

**[05:15]** Uh, and then I worked at SpaceX where I led the CI/CD team. Fun fact, we never

**[05:17]** led the CI/CD team. Fun fact, we never

**[05:17]** led the CI/CD team. Fun fact, we never blew up a rocket while I was in charge

**[05:19]** blew up a rocket while I was in charge

**[05:19]** blew up a rocket while I was in charge of that team. Before and after my

**[05:20]** of that team. Before and after my

**[05:20]** of that team. Before and after my tenure, we blew up rockets. Um, I I

**[05:23]** tenure, we blew up rockets. Um, I I

**[05:24]** tenure, we blew up rockets. Um, I I don't know what else I can say there.

**[05:25]** don't know what else I can say there.

**[05:25]** don't know what else I can say there. Uh, and then I spent a long time at AWS

**[05:27]** Uh, and then I spent a long time at AWS

**[05:27]** Uh, and then I spent a long time at AWS and I had a great time building a ton of

**[05:28]** and I had a great time building a ton of

**[05:28]** and I had a great time building a ton of technology for a lot of customers. I

**[05:30]** technology for a lot of customers. I

**[05:30]** technology for a lot of customers. I even made a video about the transformer

**[05:32]** even made a video about the transformer

**[05:32]** even made a video about the transformer paper in July of 2017, not realizing

**[05:36]** paper in July of 2017, not realizing

**[05:36]** paper in July of 2017, not realizing what it was going to lead to. And the

**[05:39]** what it was going to lead to. And the

**[05:39]** what it was going to lead to. And the fact that we're all even here today is

**[05:40]** fact that we're all even here today is

**[05:40]** fact that we're all even here today is is still attention is all you need. Uh

**[05:43]** is still attention is all you need. Uh

**[05:43]** is still attention is all you need. Uh you can follow me on Twitter at JR Hunt.

**[05:45]** you can follow me on Twitter at JR Hunt.

**[05:45]** you can follow me on Twitter at JR Hunt. Uh it's still called Twitter. It will

**[05:46]** Uh it's still called Twitter. It will

**[05:46]** Uh it's still called Twitter. It will never be called X in my mind. And uh

**[05:48]** never be called X in my mind. And uh

**[05:48]** never be called X in my mind. And uh this is Kalin. You know, we've won

**[05:50]** this is Kalin. You know, we've won

**[05:50]** this is Kalin. You know, we've won partner of the year for AWS for a long

**[05:52]** partner of the year for AWS for a long

**[05:52]** partner of the year for AWS for a long time. We build stuff. Like I said, I I I

**[05:54]** time. We build stuff. Like I said, I I I

**[05:54]** time. We build stuff. Like I said, I I I like to say our motto is we build cool

**[05:56]** like to say our motto is we build cool

**[05:56]** like to say our motto is we build cool stuff. Um marketing doesn't like it when

**[05:58]** stuff. Um marketing doesn't like it when

**[05:58]** stuff. Um marketing doesn't like it when I say that. Uh because I don't always

**[05:59]** I say that. Uh because I don't always


### [06:00 - 07:00]

**[06:00]** I say that. Uh because I don't always say the word stuff. Sometimes I'll sub

**[06:01]** say the word stuff. Sometimes I'll sub

**[06:01]** say the word stuff. Sometimes I'll sub in a different word. And what we build,

**[06:04]** in a different word. And what we build,

**[06:04]** in a different word. And what we build, you know, everything from chat bots to

**[06:05]** you know, everything from chat bots to

**[06:05]** you know, everything from chat bots to co-pilots to AI agents. And I'm going to

**[06:07]** co-pilots to AI agents. And I'm going to

**[06:07]** co-pilots to AI agents. And I'm going to share all the lessons that we've learned

**[06:09]** share all the lessons that we've learned

**[06:09]** share all the lessons that we've learned from building all of these things. You

**[06:11]** from building all of these things. You

**[06:11]** from building all of these things. You know, this sort of stuff on the top

**[06:13]** know, this sort of stuff on the top

**[06:13]** know, this sort of stuff on the top here, these self-service productivity

**[06:15]** here, these self-service productivity

**[06:15]** here, these self-service productivity tools. Um, these are things that you can

**[06:18]** tools. Um, these are things that you can

**[06:18]** tools. Um, these are things that you can typically buy. Uh, but certain

**[06:20]** typically buy. Uh, but certain

**[06:20]** typically buy. Uh, but certain institutions may need a fine tune. They

**[06:22]** institutions may need a fine tune. They

**[06:22]** institutions may need a fine tune. They may need a a particular application on

**[06:24]** may need a a particular application on

**[06:24]** may need a a particular application on top of that self-service productivity

**[06:26]** top of that self-service productivity

**[06:26]** top of that self-service productivity tool and we will often build things for

**[06:28]** tool and we will often build things for

**[06:28]** tool and we will often build things for them. Uh, one of the issues that we see

**[06:30]** them. Uh, one of the issues that we see

**[06:30]** them. Uh, one of the issues that we see organizations facing is how do they

**[06:32]** organizations facing is how do they

**[06:32]** organizations facing is how do they administer and track the usage of these

**[06:35]** administer and track the usage of these

**[06:35]** administer and track the usage of these third-party tools and APIs. Uh, and some

**[06:37]** third-party tools and APIs. Uh, and some

**[06:38]** third-party tools and APIs. Uh, and some people have an on-prem network and a VPN

**[06:39]** people have an on-prem network and a VPN

**[06:39]** people have an on-prem network and a VPN where they can just measure all the

**[06:40]** where they can just measure all the

**[06:40]** where they can just measure all the traffic. They can intercept things. They

**[06:42]** traffic. They can intercept things. They

**[06:42]** traffic. They can intercept things. They can look for PII or PHI and they can do

**[06:44]** can look for PII or PHI and they can do

**[06:44]** can look for PII or PHI and they can do all the fun stuff that we're supposed to

**[06:45]** all the fun stuff that we're supposed to

**[06:45]** all the fun stuff that we're supposed to do with network interception. There's a

**[06:47]** do with network interception. There's a

**[06:47]** do with network interception. There's a great tool called Shure Path. Uh, we use

**[06:49]** great tool called Shure Path. Uh, we use

**[06:49]** great tool called Shure Path. Uh, we use it at Kalin. I recommend them. Uh, it

**[06:51]** it at Kalin. I recommend them. Uh, it

**[06:51]** it at Kalin. I recommend them. Uh, it does all of that for you and it can

**[06:52]** does all of that for you and it can

**[06:52]** does all of that for you and it can integrate with Zcal or whatever else you

**[06:54]** integrate with Zcal or whatever else you

**[06:54]** integrate with Zcal or whatever else you might need. Um in terms of automating

**[06:56]** might need. Um in terms of automating

**[06:56]** might need. Um in terms of automating business functions, you know, this is

**[06:59]** business functions, you know, this is

**[06:59]** business functions, you know, this is typically trying to get a a percentage


### [07:00 - 08:00]

**[07:02]** typically trying to get a a percentage

**[07:02]** typically trying to get a a percentage of time or dollars back uh end to end in

**[07:05]** of time or dollars back uh end to end in

**[07:05]** of time or dollars back uh end to end in a particular business process. Uh we

**[07:07]** a particular business process. Uh we

**[07:08]** a particular business process. Uh we work with a large logistics management

**[07:09]** work with a large logistics management

**[07:09]** work with a large logistics management customer that does a tremendous amount

**[07:11]** customer that does a tremendous amount

**[07:11]** customer that does a tremendous amount of processing of uh of receipts and

**[07:14]** of processing of uh of receipts and

**[07:14]** of processing of uh of receipts and bills of laden and things like that. And

**[07:16]** bills of laden and things like that. And

**[07:16]** bills of laden and things like that. And this is a typical intelligent document

**[07:18]** this is a typical intelligent document

**[07:18]** this is a typical intelligent document processing use case leveraging

**[07:20]** processing use case leveraging

**[07:20]** processing use case leveraging generative AI and a custom classifier

**[07:22]** generative AI and a custom classifier

**[07:22]** generative AI and a custom classifier before we send it into the generative AI

**[07:24]** before we send it into the generative AI

**[07:24]** before we send it into the generative AI models. Uh we can get far faster better

**[07:26]** models. Uh we can get far faster better

**[07:26]** models. Uh we can get far faster better results than even their human annotators

**[07:28]** results than even their human annotators

**[07:28]** results than even their human annotators can. Um and then there's monetization

**[07:31]** can. Um and then there's monetization

**[07:31]** can. Um and then there's monetization which is adding a new skew to an

**[07:33]** which is adding a new skew to an

**[07:33]** which is adding a new skew to an existing product. It's an existing SAS

**[07:35]** existing product. It's an existing SAS

**[07:35]** existing product. It's an existing SAS platform. It's an existing utility and

**[07:37]** platform. It's an existing utility and

**[07:37]** platform. It's an existing utility and the customer is like oh I want to add a

**[07:40]** the customer is like oh I want to add a

**[07:40]** the customer is like oh I want to add a new skew so I can charge my users for

**[07:41]** new skew so I can charge my users for

**[07:42]** new skew so I can charge my users for fancy AI because the Wall Street Journal

**[07:43]** fancy AI because the Wall Street Journal

**[07:43]** fancy AI because the Wall Street Journal told me to. And that is a very fun area

**[07:47]** told me to. And that is a very fun area

**[07:47]** told me to. And that is a very fun area to work in. But if you just build a

**[07:49]** to work in. But if you just build a

**[07:49]** to work in. But if you just build a chatbot, you know, sayanara, like good

**[07:52]** chatbot, you know, sayanara, like good

**[07:52]** chatbot, you know, sayanara, like good luck. I'll, you know, you're the

**[07:54]** luck. I'll, you know, you're the

**[07:54]** luck. I'll, you know, you're the Polaroid. Um, do people still use

**[07:56]** Polaroid. Um, do people still use

**[07:56]** Polaroid. Um, do people still use Polaroid? Are they doing okay? I don't

**[07:58]** Polaroid? Are they doing okay? I don't

**[07:58]** Polaroid? Are they doing okay? I don't know. Anyway, I used to say Kodak. Um,


### [08:00 - 09:00]

**[08:01]** know. Anyway, I used to say Kodak. Um,

**[08:01]** know. Anyway, I used to say Kodak. Um, this is how we build these things and

**[08:02]** this is how we build these things and

**[08:02]** this is how we build these things and these are the lessons that we've

**[08:03]** these are the lessons that we've

**[08:03]** these are the lessons that we've learned. Um, I stole this slide. This is

**[08:05]** learned. Um, I stole this slide. This is

**[08:05]** learned. Um, I stole this slide. This is not my slide. I cannot remember where it

**[08:07]** not my slide. I cannot remember where it

**[08:08]** not my slide. I cannot remember where it is from. It's from Twitter somewhere. It

**[08:09]** is from. It's from Twitter somewhere. It

**[08:10]** is from. It's from Twitter somewhere. It might have been Jason Louu. It might

**[08:11]** might have been Jason Louu. It might

**[08:11]** might have been Jason Louu. It might have been from DSPY. But this is a great

**[08:13]** have been from DSPY. But this is a great

**[08:13]** have been from DSPY. But this is a great slide that I think very strategically

**[08:15]** slide that I think very strategically

**[08:15]** slide that I think very strategically identifies what the uh specifications

**[08:19]** identifies what the uh specifications

**[08:19]** identifies what the uh specifications are to build a moat in your business and

**[08:22]** are to build a moat in your business and

**[08:22]** are to build a moat in your business and the inputs to your system and what your

**[08:25]** the inputs to your system and what your

**[08:25]** the inputs to your system and what your system is going to do with them. That is

**[08:27]** system is going to do with them. That is

**[08:27]** system is going to do with them. That is the most fundamental part your inputs

**[08:29]** the most fundamental part your inputs

**[08:29]** the most fundamental part your inputs and your outputs. Um, does everyone

**[08:31]** and your outputs. Um, does everyone

**[08:31]** and your outputs. Um, does everyone remember Steve Balmer, uh, the former

**[08:33]** remember Steve Balmer, uh, the former

**[08:34]** remember Steve Balmer, uh, the former CEO of Microsoft and how he, uh,

**[08:36]** CEO of Microsoft and how he, uh,

**[08:36]** CEO of Microsoft and how he, uh, famously went on stage, uh, on a

**[08:37]** famously went on stage, uh, on a

**[08:37]** famously went on stage, uh, on a tremendous amount of cocaine and just

**[08:39]** tremendous amount of cocaine and just

**[08:39]** tremendous amount of cocaine and just started screaming, um, developers,

**[08:41]** started screaming, um, developers,

**[08:41]** started screaming, um, developers, developers, developers, developers. If I

**[08:43]** developers, developers, developers. If I

**[08:43]** developers, developers, developers. If I were to channel my inner balmer, what I

**[08:44]** were to channel my inner balmer, what I

**[08:44]** were to channel my inner balmer, what I would say is eval.

**[08:47]** would say is eval.

**[08:47]** would say is eval. So when we do this eval layer, this is

**[08:50]** So when we do this eval layer, this is

**[08:50]** So when we do this eval layer, this is where we prove that the system is robust

**[08:54]** where we prove that the system is robust

**[08:54]** where we prove that the system is robust and not just a vibe check and we're

**[08:56]** and not just a vibe check and we're

**[08:56]** and not just a vibe check and we're getting a one-off on a particularly

**[08:58]** getting a one-off on a particularly

**[08:58]** getting a one-off on a particularly unique uh prompt. Then we have the


### [09:00 - 10:00]

**[09:01]** unique uh prompt. Then we have the

**[09:01]** unique uh prompt. Then we have the system architecture and then we have the

**[09:03]** system architecture and then we have the

**[09:03]** system architecture and then we have the different LLMs and tools and things we

**[09:05]** different LLMs and tools and things we

**[09:05]** different LLMs and tools and things we may use. And these are all incidental to

**[09:07]** may use. And these are all incidental to

**[09:07]** may use. And these are all incidental to your AI system and you should expect

**[09:08]** your AI system and you should expect

**[09:08]** your AI system and you should expect them to evolve and change. What will not

**[09:11]** them to evolve and change. What will not

**[09:11]** them to evolve and change. What will not evolve and change is your fundamental

**[09:13]** evolve and change is your fundamental

**[09:13]** evolve and change is your fundamental definition and specification of what are

**[09:15]** definition and specification of what are

**[09:15]** definition and specification of what are your inputs and what are your outputs.

**[09:17]** your inputs and what are your outputs.

**[09:17]** your inputs and what are your outputs. Uh and as you know the models get better

**[09:19]** Uh and as you know the models get better

**[09:20]** Uh and as you know the models get better and they improve and you can get other

**[09:21]** and they improve and you can get other

**[09:21]** and they improve and you can get other like modalities of output that may

**[09:23]** like modalities of output that may

**[09:23]** like modalities of output that may evolve. But you're always going to

**[09:25]** evolve. But you're always going to

**[09:25]** evolve. But you're always going to figure out why am I doing this? What is

**[09:27]** figure out why am I doing this? What is

**[09:27]** figure out why am I doing this? What is my ROI? What do I expect?

**[09:30]** my ROI? What do I expect?

**[09:30]** my ROI? What do I expect? This is how we build these things in

**[09:32]** This is how we build these things in

**[09:32]** This is how we build these things in AWS. On the bottom layer we have two

**[09:34]** AWS. On the bottom layer we have two

**[09:34]** AWS. On the bottom layer we have two services. We have Bedrock and we have

**[09:35]** services. We have Bedrock and we have

**[09:35]** services. We have Bedrock and we have SageMaker. Uh these are uh useful

**[09:39]** SageMaker. Uh these are uh useful

**[09:39]** SageMaker. Uh these are uh useful services. SageMaker comes at a

**[09:41]** services. SageMaker comes at a

**[09:41]** services. SageMaker comes at a particular compute premium. You can also

**[09:43]** particular compute premium. You can also

**[09:43]** particular compute premium. You can also just run on EKS or EC2 if you want. Um

**[09:46]** just run on EKS or EC2 if you want. Um

**[09:46]** just run on EKS or EC2 if you want. Um there's two different pieces of custom

**[09:47]** there's two different pieces of custom

**[09:47]** there's two different pieces of custom silicon that exist within AWS. One is

**[09:49]** silicon that exist within AWS. One is

**[09:50]** silicon that exist within AWS. One is trrenium, one is inferentia. Uh these

**[09:51]** trrenium, one is inferentia. Uh these

**[09:52]** trrenium, one is inferentia. Uh these come at about a 60% price performance

**[09:54]** come at about a 60% price performance

**[09:54]** come at about a 60% price performance improvement over using Nvidia GPUs. Now

**[09:56]** improvement over using Nvidia GPUs. Now

**[09:56]** improvement over using Nvidia GPUs. Now the downside is the amount of HP RAM is

**[09:59]** the downside is the amount of HP RAM is

**[09:59]** the downside is the amount of HP RAM is not as big as like an H200. I don't know


### [10:00 - 11:00]

**[10:01]** not as big as like an H200. I don't know

**[10:01]** not as big as like an H200. I don't know if anyone saw today, but it was great

**[10:02]** if anyone saw today, but it was great

**[10:02]** if anyone saw today, but it was great news. Amazon announced that they were

**[10:04]** news. Amazon announced that they were

**[10:04]** news. Amazon announced that they were reducing the prices of the P4 and P5

**[10:06]** reducing the prices of the P4 and P5

**[10:06]** reducing the prices of the P4 and P5 instances by up to 40%. So we all get

**[10:08]** instances by up to 40%. So we all get

**[10:08]** instances by up to 40%. So we all get more GPUs cheaper. Very happy about

**[10:10]** more GPUs cheaper. Very happy about

**[10:10]** more GPUs cheaper. Very happy about that. Um the interesting thing with

**[10:13]** that. Um the interesting thing with

**[10:13]** that. Um the interesting thing with tranium and inferentia is that you must

**[10:15]** tranium and inferentia is that you must

**[10:15]** tranium and inferentia is that you must uh use something called the neuron SDK

**[10:18]** uh use something called the neuron SDK

**[10:18]** uh use something called the neuron SDK to write these. So if anyone has ever

**[10:20]** to write these. So if anyone has ever

**[10:20]** to write these. So if anyone has ever written XLA for like TensorFlow and the

**[10:22]** written XLA for like TensorFlow and the

**[10:22]** written XLA for like TensorFlow and the good old um what were they called the

**[10:24]** good old um what were they called the

**[10:24]** good old um what were they called the TPUs and now the new TPU7 and all that

**[10:26]** TPUs and now the new TPU7 and all that

**[10:26]** TPUs and now the new TPU7 and all that great stuff. Uh the the neuron kernel

**[10:28]** great stuff. Uh the the neuron kernel

**[10:28]** great stuff. Uh the the neuron kernel interface for tranium and infinia is

**[10:30]** interface for tranium and infinia is

**[10:30]** interface for tranium and infinia is very similar. One level up from that we

**[10:32]** very similar. One level up from that we

**[10:32]** very similar. One level up from that we get to pick our various models. So we

**[10:34]** get to pick our various models. So we

**[10:34]** get to pick our various models. So we have everything from uh claude and nova

**[10:36]** have everything from uh claude and nova

**[10:36]** have everything from uh claude and nova to llama and deepseeek uh and then open

**[10:38]** to llama and deepseeek uh and then open

**[10:38]** to llama and deepseeek uh and then open source models that we can deploy. I

**[10:40]** source models that we can deploy. I

**[10:40]** source models that we can deploy. I don't know if mistrol is ever going to

**[10:41]** don't know if mistrol is ever going to

**[10:41]** don't know if mistrol is ever going to release another open source model but

**[10:42]** release another open source model but

**[10:42]** release another open source model but who knows. Uh and then we have our

**[10:44]** who knows. Uh and then we have our

**[10:44]** who knows. Uh and then we have our embeddings and our vector stores. So

**[10:46]** embeddings and our vector stores. So

**[10:46]** embeddings and our vector stores. So like I said uh I do prefer Postgress

**[10:49]** like I said uh I do prefer Postgress

**[10:49]** like I said uh I do prefer Postgress right now. If you need um persistence in

**[10:52]** right now. If you need um persistence in

**[10:52]** right now. If you need um persistence in Reddus uh there's a great thing called

**[10:54]** Reddus uh there's a great thing called

**[10:54]** Reddus uh there's a great thing called memory DB on AWS that also supports

**[10:56]** memory DB on AWS that also supports

**[10:56]** memory DB on AWS that also supports vector search. Um the good news about

**[10:58]** vector search. Um the good news about

**[10:58]** vector search. Um the good news about the reddis vector search is that it is


### [11:00 - 12:00]

**[11:00]** the reddis vector search is that it is

**[11:00]** the reddis vector search is that it is extremely fast. The bad news is that it

**[11:02]** extremely fast. The bad news is that it

**[11:02]** extremely fast. The bad news is that it is extremely expensive because it has to

**[11:03]** is extremely expensive because it has to

**[11:04]** is extremely expensive because it has to sit in RAM. Um so if you think about how

**[11:07]** sit in RAM. Um so if you think about how

**[11:07]** sit in RAM. Um so if you think about how you're going to construct your indexes

**[11:08]** you're going to construct your indexes

**[11:08]** you're going to construct your indexes and like do IVV flat or something uh be

**[11:10]** and like do IVV flat or something uh be

**[11:10]** and like do IVV flat or something uh be prepared to blow up your RAM in order to

**[11:12]** prepared to blow up your RAM in order to

**[11:12]** prepared to blow up your RAM in order to store all of that stuff. Now um within

**[11:14]** store all of that stuff. Now um within

**[11:14]** store all of that stuff. Now um within Postgress and open search you can go to

**[11:16]** Postgress and open search you can go to

**[11:16]** Postgress and open search you can go to disk and you can use things like HNSW

**[11:18]** disk and you can use things like HNSW

**[11:18]** disk and you can use things like HNSW indexes so that you can have uh a better

**[11:20]** indexes so that you can have uh a better

**[11:20]** indexes so that you can have uh a better allocation and search mechanism. Then we

**[11:23]** allocation and search mechanism. Then we

**[11:23]** allocation and search mechanism. Then we have the prompt versioning and prompt

**[11:24]** have the prompt versioning and prompt

**[11:24]** have the prompt versioning and prompt management. Uh all of these things are

**[11:26]** management. Uh all of these things are

**[11:26]** management. Uh all of these things are incidental and and kind of uh you you

**[11:29]** incidental and and kind of uh you you

**[11:29]** incidental and and kind of uh you you know not unique anymore. But this one

**[11:31]** know not unique anymore. But this one

**[11:31]** know not unique anymore. But this one context management is incredibly

**[11:34]** context management is incredibly

**[11:34]** context management is incredibly important. And if you are looking to

**[11:37]** important. And if you are looking to

**[11:37]** important. And if you are looking to differentiate your application from

**[11:39]** differentiate your application from

**[11:39]** differentiate your application from someone else's application, context is

**[11:41]** someone else's application, context is

**[11:41]** someone else's application, context is key. So if your competitor doesn't have

**[11:44]** key. So if your competitor doesn't have

**[11:44]** key. So if your competitor doesn't have the context of the user and additional

**[11:47]** the context of the user and additional

**[11:47]** the context of the user and additional information uh but you're able to inject

**[11:49]** information uh but you're able to inject

**[11:49]** information uh but you're able to inject oh the the user is on this page they

**[11:51]** oh the the user is on this page they

**[11:51]** oh the the user is on this page they have a history of this browsing you know

**[11:53]** have a history of this browsing you know

**[11:53]** have a history of this browsing you know these are the cookies that I saw this is

**[11:55]** these are the cookies that I saw this is

**[11:55]** these are the cookies that I saw this is you know then you can go and make a much

**[11:57]** you know then you can go and make a much

**[11:57]** you know then you can go and make a much more strategic inference on behalf of

**[11:59]** more strategic inference on behalf of

**[11:59]** more strategic inference on behalf of that end user. So here are the lessons


### [12:00 - 13:00]

**[12:02]** that end user. So here are the lessons

**[12:02]** that end user. So here are the lessons that we learned and I I'll jump into

**[12:03]** that we learned and I I'll jump into

**[12:03]** that we learned and I I'll jump into these but I'm also going to run out of

**[12:05]** these but I'm also going to run out of

**[12:05]** these but I'm also going to run out of time so I I'll speed through a little

**[12:06]** time so I I'll speed through a little

**[12:06]** time so I I'll speed through a little bit of it and I'll make the stack

**[12:07]** bit of it and I'll make the stack

**[12:07]** bit of it and I'll make the stack available for folks. But uh it turns out

**[12:10]** available for folks. But uh it turns out

**[12:10]** available for folks. But uh it turns out eval and embeddings are not all you

**[12:12]** eval and embeddings are not all you

**[12:12]** eval and embeddings are not all you need. Uh

**[12:14]** need. Uh

**[12:14]** need. Uh you know the understanding the access

**[12:17]** you know the understanding the access

**[12:17]** you know the understanding the access patterns and understanding the way that

**[12:18]** patterns and understanding the way that

**[12:18]** patterns and understanding the way that people will use the product uh will lead

**[12:20]** people will use the product uh will lead

**[12:20]** people will use the product uh will lead to a much better result than just

**[12:22]** to a much better result than just

**[12:22]** to a much better result than just throwing out evals and throwing out

**[12:23]** throwing out evals and throwing out

**[12:23]** throwing out evals and throwing out embeddings and wishing the best of luck.

**[12:25]** embeddings and wishing the best of luck.

**[12:25]** embeddings and wishing the best of luck. Embeddings alone do not a great query

**[12:27]** Embeddings alone do not a great query

**[12:27]** Embeddings alone do not a great query system make. How do you do faceted

**[12:29]** system make. How do you do faceted

**[12:29]** system make. How do you do faceted search and filters on top of embeddings

**[12:31]** search and filters on top of embeddings

**[12:31]** search and filters on top of embeddings alone? That is why we love things like

**[12:33]** alone? That is why we love things like

**[12:33]** alone? That is why we love things like open search and postgress. Um speed

**[12:36]** open search and postgress. Um speed

**[12:36]** open search and postgress. Um speed matters. So if your inference is slow,

**[12:41]** matters. So if your inference is slow,

**[12:41]** matters. So if your inference is slow, uh UX is a means of mitigating the

**[12:43]** uh UX is a means of mitigating the

**[12:44]** uh UX is a means of mitigating the slowness of some of these things.

**[12:46]** slowness of some of these things.

**[12:46]** slowness of some of these things. There's other techniques you can use.

**[12:47]** There's other techniques you can use.

**[12:47]** There's other techniques you can use. You can use caching, you can use other

**[12:49]** You can use caching, you can use other

**[12:49]** You can use caching, you can use other components. Um but if you are slower and

**[12:52]** components. Um but if you are slower and

**[12:52]** components. Um but if you are slower and more expensive, you will not be used. If

**[12:54]** more expensive, you will not be used. If

**[12:54]** more expensive, you will not be used. If you are uh slower and cheaper and you're

**[12:57]** you are uh slower and cheaper and you're

**[12:57]** you are uh slower and cheaper and you're mitigating some of the effects by

**[12:58]** mitigating some of the effects by

**[12:58]** mitigating some of the effects by leveraging something like a fancy UI


### [13:00 - 14:00]

**[13:01]** leveraging something like a fancy UI

**[13:01]** leveraging something like a fancy UI spinner or something that keeps your

**[13:02]** spinner or something that keeps your

**[13:02]** spinner or something that keeps your users entertained as the inference is

**[13:04]** users entertained as the inference is

**[13:04]** users entertained as the inference is being calculated uh you can uh still

**[13:06]** being calculated uh you can uh still

**[13:06]** being calculated uh you can uh still win. Now uh knowing your end customer as

**[13:09]** win. Now uh knowing your end customer as

**[13:09]** win. Now uh knowing your end customer as I said is very important. And then the

**[13:11]** I said is very important. And then the

**[13:11]** I said is very important. And then the other very important thing is the number

**[13:13]** other very important thing is the number

**[13:13]** other very important thing is the number of times I see people defining a tool

**[13:16]** of times I see people defining a tool

**[13:16]** of times I see people defining a tool called get current date is infuriating

**[13:19]** called get current date is infuriating

**[13:19]** called get current date is infuriating to me. Like it is literally like import

**[13:22]** to me. Like it is literally like import

**[13:22]** to me. Like it is literally like import time.now

**[13:24]** time.now

**[13:24]** time.now you know like just it's a format string

**[13:26]** you know like just it's a format string

**[13:26]** you know like just it's a format string just throw it in the string like you

**[13:28]** just throw it in the string like you

**[13:28]** just throw it in the string like you control the prompt. Um, so, uh, the

**[13:33]** control the prompt. Um, so, uh, the

**[13:33]** control the prompt. Um, so, uh, the downside of putting some of that

**[13:35]** downside of putting some of that

**[13:35]** downside of putting some of that information very high up in the prompt

**[13:36]** information very high up in the prompt

**[13:36]** information very high up in the prompt is that your caching, uh, is not as

**[13:38]** is that your caching, uh, is not as

**[13:38]** is that your caching, uh, is not as effective. But if you can put some of

**[13:40]** effective. But if you can put some of

**[13:40]** effective. But if you can put some of that information at the bottom of the

**[13:41]** that information at the bottom of the

**[13:41]** that information at the bottom of the prompt after the instructions, you can

**[13:43]** prompt after the instructions, you can

**[13:43]** prompt after the instructions, you can often, uh, get very effective caching.

**[13:45]** often, uh, get very effective caching.

**[13:45]** often, uh, get very effective caching. Um, then there is like I I used to say

**[13:51]** Um, then there is like I I used to say

**[13:51]** Um, then there is like I I used to say we should fine-tune, we should do these

**[13:52]** we should fine-tune, we should do these

**[13:52]** we should fine-tune, we should do these things. Uh, it turns out I was wrong. As

**[13:54]** things. Uh, it turns out I was wrong. As

**[13:54]** things. Uh, it turns out I was wrong. As the models have improved and gotten more

**[13:56]** the models have improved and gotten more

**[13:56]** the models have improved and gotten more and more powerful, uh, prompt

**[13:58]** and more powerful, uh, prompt

**[13:58]** and more powerful, uh, prompt engineering has proven unreasonably


### [14:00 - 15:00]

**[14:00]** engineering has proven unreasonably

**[14:00]** engineering has proven unreasonably effective for us, like far more

**[14:02]** effective for us, like far more

**[14:02]** effective for us, like far more effective than I would have predicted.

**[14:03]** effective than I would have predicted.

**[14:03]** effective than I would have predicted. Within, uh, cloud 3.7 to claude 4, we

**[14:06]** Within, uh, cloud 3.7 to claude 4, we

**[14:06]** Within, uh, cloud 3.7 to claude 4, we saw zero regressions. From cloud 35 to

**[14:08]** saw zero regressions. From cloud 35 to

**[14:08]** saw zero regressions. From cloud 35 to 37, we did see regressions on certain

**[14:11]** 37, we did see regressions on certain

**[14:11]** 37, we did see regressions on certain things when we moved the exact same

**[14:12]** things when we moved the exact same

**[14:12]** things when we moved the exact same prompts over to some of our, uh, users

**[14:15]** prompts over to some of our, uh, users

**[14:15]** prompts over to some of our, uh, users and some of our evals. But from 37 to

**[14:18]** and some of our evals. But from 37 to

**[14:18]** and some of our evals. But from 37 to four, we got faster, better, cheaper,

**[14:21]** four, we got faster, better, cheaper,

**[14:21]** four, we got faster, better, cheaper, more optimized inference in virtually

**[14:23]** more optimized inference in virtually

**[14:23]** more optimized inference in virtually every use case. So it was like a drop in

**[14:25]** every use case. So it was like a drop in

**[14:25]** every use case. So it was like a drop in replacement and it was amazing. Um, and

**[14:27]** replacement and it was amazing. Um, and

**[14:27]** replacement and it was amazing. Um, and I hoping future versions will be the

**[14:29]** I hoping future versions will be the

**[14:29]** I hoping future versions will be the same. Uh, I'm hoping we're the era of

**[14:31]** same. Uh, I'm hoping we're the era of

**[14:31]** same. Uh, I'm hoping we're the era of having to adjust your prompt every time

**[14:33]** having to adjust your prompt every time

**[14:33]** having to adjust your prompt every time a new model comes out is ending. Um, and

**[14:36]** a new model comes out is ending. Um, and

**[14:36]** a new model comes out is ending. Um, and then finally, it's very important to

**[14:37]** then finally, it's very important to

**[14:37]** then finally, it's very important to know your economics like is this

**[14:39]** know your economics like is this

**[14:39]** know your economics like is this inference going to bankrupt my company?

**[14:41]** inference going to bankrupt my company?

**[14:41]** inference going to bankrupt my company? Um if you think about some of the cost

**[14:43]** Um if you think about some of the cost

**[14:43]** Um if you think about some of the cost of uh uh the the opus models, you know,

**[14:47]** of uh uh the the opus models, you know,

**[14:47]** of uh uh the the opus models, you know, it may not always be the best thing to

**[14:49]** it may not always be the best thing to

**[14:49]** it may not always be the best thing to run.

**[14:50]** run.

**[14:50]** run. Okay, so just in the interest of time,

**[14:53]** Okay, so just in the interest of time,

**[14:53]** Okay, so just in the interest of time, this is another great slide. This is uh

**[14:55]** this is another great slide. This is uh

**[14:55]** this is another great slide. This is uh from anthropic actually. And when we

**[14:58]** from anthropic actually. And when we

**[14:58]** from anthropic actually. And when we think about how to create our evals, the


### [15:00 - 16:00]

**[15:00]** think about how to create our evals, the

**[15:00]** think about how to create our evals, the vibe check, the very first thing that

**[15:01]** vibe check, the very first thing that

**[15:01]** vibe check, the very first thing that you do when you try to create um a uh

**[15:07]** you do when you try to create um a uh

**[15:08]** you do when you try to create um a uh a test, that vibe check becomes your

**[15:10]** a test, that vibe check becomes your

**[15:10]** a test, that vibe check becomes your first eval. And then you change the data

**[15:12]** first eval. And then you change the data

**[15:12]** first eval. And then you change the data and the stuff that you're sending in and

**[15:14]** and the stuff that you're sending in and

**[15:14]** and the stuff that you're sending in and lo and behold, 20 minutes later, you do

**[15:16]** lo and behold, 20 minutes later, you do

**[15:16]** lo and behold, 20 minutes later, you do have some form of eval set that you can

**[15:18]** have some form of eval set that you can

**[15:18]** have some form of eval set that you can begin running. And then you can go for

**[15:20]** begin running. And then you can go for

**[15:20]** begin running. And then you can go for metrics. Now metrics do not have to be a

**[15:22]** metrics. Now metrics do not have to be a

**[15:22]** metrics. Now metrics do not have to be a score like a BERT or

**[15:25]** score like a BERT or

**[15:25]** score like a BERT or you know a benchmark score that is

**[15:26]** you know a benchmark score that is

**[15:26]** you know a benchmark score that is calculated. They can just be a boolean.

**[15:29]** calculated. They can just be a boolean.

**[15:29]** calculated. They can just be a boolean. It can just be true or false. Was this

**[15:31]** It can just be true or false. Was this

**[15:31]** It can just be true or false. Was this inference successful or not? Um that is

**[15:33]** inference successful or not? Um that is

**[15:33]** inference successful or not? Um that is often easier than trying to assign a

**[15:35]** often easier than trying to assign a

**[15:35]** often easier than trying to assign a particular value and a particular score.

**[15:37]** particular value and a particular score.

**[15:37]** particular value and a particular score. Uh and then you just iterate, you know,

**[15:39]** Uh and then you just iterate, you know,

**[15:39]** Uh and then you just iterate, you know, keep going. And like I said, speed

**[15:41]** keep going. And like I said, speed

**[15:41]** keep going. And like I said, speed matters, but UX matters more. you know,

**[15:43]** matters, but UX matters more. you know,

**[15:43]** matters, but UX matters more. you know, this UX orchestration, prop management,

**[15:45]** this UX orchestration, prop management,

**[15:46]** this UX orchestration, prop management, all of this great stuff uh is why we end

**[15:49]** all of this great stuff uh is why we end

**[15:49]** all of this great stuff uh is why we end up doing better than uh some of our

**[15:51]** up doing better than uh some of our

**[15:51]** up doing better than uh some of our competitors. And then, you know, one of

**[15:53]** competitors. And then, you know, one of

**[15:53]** competitors. And then, you know, one of our customers, Cloud Zero, uh we

**[15:56]** our customers, Cloud Zero, uh we

**[15:56]** our customers, Cloud Zero, uh we originally built a chatbot for them for

**[15:57]** originally built a chatbot for them for

**[15:57]** originally built a chatbot for them for you to chat with your AWS infrastructure

**[15:59]** you to chat with your AWS infrastructure

**[15:59]** you to chat with your AWS infrastructure and get cost out of that AWS


### [16:00 - 17:00]

**[16:01]** and get cost out of that AWS

**[16:01]** and get cost out of that AWS infrastructure. Um we are now using

**[16:03]** infrastructure. Um we are now using

**[16:03]** infrastructure. Um we are now using generative UI in order to render uh the

**[16:06]** generative UI in order to render uh the

**[16:06]** generative UI in order to render uh the information that is shown in those

**[16:08]** information that is shown in those

**[16:08]** information that is shown in those charts. So in just in time we will craft

**[16:11]** charts. So in just in time we will craft

**[16:11]** charts. So in just in time we will craft a react component and inject it into the

**[16:14]** a react component and inject it into the

**[16:14]** a react component and inject it into the uh the rendering of the response and

**[16:17]** uh the rendering of the response and

**[16:17]** uh the rendering of the response and then we can cache those uh components

**[16:20]** then we can cache those uh components

**[16:20]** then we can cache those uh components and describe in the prompt hey I made

**[16:23]** and describe in the prompt hey I made

**[16:23]** and describe in the prompt hey I made this for this other user and maybe it's

**[16:25]** this for this other user and maybe it's

**[16:25]** this for this other user and maybe it's helpful one day uh for some other user's

**[16:28]** helpful one day uh for some other user's

**[16:28]** helpful one day uh for some other user's query. And so this generative UI allows

**[16:30]** query. And so this generative UI allows

**[16:30]** query. And so this generative UI allows the tool to constantly evolve and

**[16:31]** the tool to constantly evolve and

**[16:31]** the tool to constantly evolve and personalize to the individual end user.

**[16:33]** personalize to the individual end user.

**[16:33]** personalize to the individual end user. Um, this is an extremely powerful

**[16:35]** Um, this is an extremely powerful

**[16:35]** Um, this is an extremely powerful paradigm that is finally fast enough

**[16:37]** paradigm that is finally fast enough

**[16:37]** paradigm that is finally fast enough with some of these uh models and their

**[16:39]** with some of these uh models and their

**[16:39]** with some of these uh models and their lightning fast inference speed. Um,

**[16:42]** lightning fast inference speed. Um,

**[16:42]** lightning fast inference speed. Um, nature footage, we covered that earlier.

**[16:44]** nature footage, we covered that earlier.

**[16:44]** nature footage, we covered that earlier. Uh there's also knowing your end user

**[16:46]** Uh there's also knowing your end user

**[16:46]** Uh there's also knowing your end user which is we had a customer uh that had

**[16:49]** which is we had a customer uh that had

**[16:50]** which is we had a customer uh that had users in remote areas and so we would

**[16:52]** users in remote areas and so we would

**[16:52]** users in remote areas and so we would give uh text summaries of these PDFs and

**[16:54]** give uh text summaries of these PDFs and

**[16:54]** give uh text summaries of these PDFs and manuals and things and that would uh

**[16:59]** manuals and things and that would uh

**[16:59]** manuals and things and that would uh be great and then they would get the PDF


### [17:00 - 18:00]

**[17:00]** be great and then they would get the PDF

**[17:00]** be great and then they would get the PDF and it would be 200 megabytes you know

**[17:02]** and it would be 200 megabytes you know

**[17:02]** and it would be 200 megabytes you know and then so what we found is on the back

**[17:04]** and then so what we found is on the back

**[17:04]** and then so what we found is on the back end on the server we could take a

**[17:06]** end on the server we could take a

**[17:06]** end on the server we could take a screenshot essentially of the PDF and

**[17:08]** screenshot essentially of the PDF and

**[17:08]** screenshot essentially of the PDF and just send that one page so that even

**[17:09]** just send that one page so that even

**[17:10]** just send that one page so that even when they were in low connectivity areas

**[17:11]** when they were in low connectivity areas

**[17:11]** when they were in low connectivity areas we could still send the text summary of

**[17:13]** we could still send the text summary of

**[17:13]** we could still send the text summary of the full document mentation and

**[17:14]** the full document mentation and

**[17:14]** the full document mentation and instructions but just send the relevant

**[17:16]** instructions but just send the relevant

**[17:16]** instructions but just send the relevant parts of the PDF without them having to

**[17:18]** parts of the PDF without them having to

**[17:18]** parts of the PDF without them having to download a 200 megabyte thing. So that's

**[17:20]** download a 200 megabyte thing. So that's

**[17:20]** download a 200 megabyte thing. So that's know your end customer. We worked with a

**[17:21]** know your end customer. We worked with a

**[17:22]** know your end customer. We worked with a hospital system for instance that uh we

**[17:23]** hospital system for instance that uh we

**[17:23]** hospital system for instance that uh we originally built a voice bot for these

**[17:25]** originally built a voice bot for these

**[17:25]** originally built a voice bot for these nurses uh and it turns out nurses hate

**[17:27]** nurses uh and it turns out nurses hate

**[17:27]** nurses uh and it turns out nurses hate voice bots because hospitals are loud

**[17:28]** voice bots because hospitals are loud

**[17:28]** voice bots because hospitals are loud and noisy and the voice transcription is

**[17:30]** and noisy and the voice transcription is

**[17:30]** and noisy and the voice transcription is not very good and you just hear other

**[17:32]** not very good and you just hear other

**[17:32]** not very good and you just hear other people yelling and they preferred a

**[17:33]** people yelling and they preferred a

**[17:33]** people yelling and they preferred a regular old chat interface. So, we had

**[17:35]** regular old chat interface. So, we had

**[17:35]** regular old chat interface. So, we had to know our end customers. Figure out

**[17:37]** to know our end customers. Figure out

**[17:37]** to know our end customers. Figure out what exactly they were doing day-to-day.

**[17:40]** what exactly they were doing day-to-day.

**[17:40]** what exactly they were doing day-to-day. And then

**[17:42]** And then

**[17:42]** And then let the computer do what the computer's

**[17:43]** let the computer do what the computer's

**[17:43]** let the computer do what the computer's good at. Don't do math in an LLM. It is

**[17:46]** good at. Don't do math in an LLM. It is

**[17:46]** good at. Don't do math in an LLM. It is the most expensive possible way of doing

**[17:48]** the most expensive possible way of doing

**[17:48]** the most expensive possible way of doing math. Um, let the the computer do its

**[17:52]** math. Um, let the the computer do its

**[17:52]** math. Um, let the the computer do its calculations. And then prompt

**[17:54]** calculations. And then prompt

**[17:54]** calculations. And then prompt engineering. I'm not going to break this

**[17:55]** engineering. I'm not going to break this

**[17:55]** engineering. I'm not going to break this down. I'm sure you've seen hundreds of

**[17:57]** down. I'm sure you've seen hundreds of

**[17:57]** down. I'm sure you've seen hundreds of talks over the last two days about the


### [18:00 - 19:00]

**[18:00]** talks over the last two days about the

**[18:00]** talks over the last two days about the uh way to engineer your prompts and

**[18:02]** uh way to engineer your prompts and

**[18:02]** uh way to engineer your prompts and everything. Uh but one of the things

**[18:04]** everything. Uh but one of the things

**[18:04]** everything. Uh but one of the things that we like to do as part of our

**[18:06]** that we like to do as part of our

**[18:06]** that we like to do as part of our optimization is to think about the

**[18:08]** optimization is to think about the

**[18:08]** optimization is to think about the output tokens and the costs that are

**[18:10]** output tokens and the costs that are

**[18:10]** output tokens and the costs that are associated there and how we can make

**[18:12]** associated there and how we can make

**[18:12]** associated there and how we can make that perform better. And then finally,

**[18:14]** that perform better. And then finally,

**[18:14]** that perform better. And then finally, know your economics. There's lots of

**[18:16]** know your economics. There's lots of

**[18:16]** know your economics. There's lots of great tools. There's things like prompt

**[18:17]** great tools. There's things like prompt

**[18:17]** great tools. There's things like prompt caching. There's things like tool usage

**[18:19]** caching. There's things like tool usage

**[18:19]** caching. There's things like tool usage and batch. Um batch on bedrock is a 50%

**[18:22]** and batch. Um batch on bedrock is a 50%

**[18:22]** and batch. Um batch on bedrock is a 50% off whatever model infrance you're

**[18:24]** off whatever model infrance you're

**[18:24]** off whatever model infrance you're trying to make across the board. And

**[18:26]** trying to make across the board. And

**[18:26]** trying to make across the board. And then context management. You can

**[18:28]** then context management. You can

**[18:28]** then context management. You can optimize your context. you can figure

**[18:29]** optimize your context. you can figure

**[18:29]** optimize your context. you can figure out what is the minimum viable context

**[18:31]** out what is the minimum viable context

**[18:31]** out what is the minimum viable context in order to get the correct inference

**[18:33]** in order to get the correct inference

**[18:33]** in order to get the correct inference and how can I optimize that context over

**[18:35]** and how can I optimize that context over

**[18:35]** and how can I optimize that context over time and this again requires knowing

**[18:37]** time and this again requires knowing

**[18:37]** time and this again requires knowing your end user knowing what they're doing

**[18:38]** your end user knowing what they're doing

**[18:38]** your end user knowing what they're doing and injecting that information into the

**[18:40]** and injecting that information into the

**[18:40]** and injecting that information into the model and also optimizing stuff that is

**[18:43]** model and also optimizing stuff that is

**[18:43]** model and also optimizing stuff that is irrelevant and taking it out of the

**[18:44]** irrelevant and taking it out of the

**[18:44]** irrelevant and taking it out of the context so that the model has less to

**[18:46]** context so that the model has less to

**[18:46]** context so that the model has less to reason over

**[18:52]** this and you want to learn more if you

**[18:52]** this and you want to learn more if you want to talk more um I'm always happy to

**[18:54]** want to talk more um I'm always happy to

**[18:54]** want to talk more um I'm always happy to hop on the phone with customers you can

**[18:56]** hop on the phone with customers you can

**[18:56]** hop on the phone with customers you can scan this QR code we like building cool

**[18:58]** scan this QR code we like building cool

**[18:58]** scan this QR code we like building cool stuff. Uh, I got a whole bunch of


### [19:00 - 20:00]

**[19:00]** stuff. Uh, I got a whole bunch of

**[19:00]** stuff. Uh, I got a whole bunch of talented engineers who were just excited

**[19:02]** talented engineers who were just excited

**[19:02]** talented engineers who were just excited to go out and build things for

**[19:03]** to go out and build things for

**[19:03]** to go out and build things for customers. So, if you have a super cool

**[19:05]** customers. So, if you have a super cool

**[19:05]** customers. So, if you have a super cool use case, come at me. All right. Thank

**[19:08]** use case, come at me. All right. Thank

**[19:08]** use case, come at me. All right. Thank you very much.

**[19:10]** you very much.

**[19:10]** you very much. [Music]


