# [Full Workshop] Building Metrics that actually work — David Karam, Pi Labs (fmr Google Search)

**Video URL:** https://www.youtube.com/watch?v=jxrGodnopHo

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Uh we're a bit early but I guess

**[00:17]** Uh we're a bit early but I guess everyone's here so we we'll get started.

**[00:19]** everyone's here so we we'll get started.

**[00:19]** everyone's here so we we'll get started. Uh maybe we'll spend uh

**[00:22]** Uh maybe we'll spend uh

**[00:22]** Uh maybe we'll spend uh first few minutes to get people a little

**[00:24]** first few minutes to get people a little

**[00:24]** first few minutes to get people a little oriented and actually we we are we are

**[00:27]** oriented and actually we we are we are

**[00:27]** oriented and actually we we are we are quite curious like what brings people

**[00:29]** quite curious like what brings people

**[00:29]** quite curious like what brings people here. Yeah. Why why are you here?

**[00:33]** here. Yeah. Why why are you here?

**[00:33]** here. Yeah. Why why are you here? Uh what what about evals? Uh did do you

**[00:36]** Uh what what about evals? Uh did do you

**[00:36]** Uh what what about evals? Uh did do you like maybe by a show of hands a few

**[00:37]** like maybe by a show of hands a few

**[00:38]** like maybe by a show of hands a few people like have you done evals before?

**[00:42]** people like have you done evals before?

**[00:42]** people like have you done evals before? Okay. And Okay.

**[00:46]** Okay. And Okay.

**[00:46]** Okay. And Okay. Have we struggled with them? Is that was

**[00:48]** Have we struggled with them? Is that was

**[00:48]** Have we struggled with them? Is that was it hard? Maybe back again. Show hand

**[00:50]** it hard? Maybe back again. Show hand

**[00:50]** it hard? Maybe back again. Show hand fans away from the speaker. Um

**[00:53]** fans away from the speaker. Um

**[00:53]** fans away from the speaker. Um are you so people who have not done eval

**[00:56]** are you so people who have not done eval

**[00:56]** are you so people who have not done eval before what bring what brings you here?


### [01:00 - 02:00]

**[01:00]** before what bring what brings you here?

**[01:00]** before what bring what brings you here? Somebody anyone wants to volunteer?

**[01:03]** Somebody anyone wants to volunteer?

**[01:03]** Somebody anyone wants to volunteer? Yeah, feel feel free to raise your hand.

**[01:05]** Yeah, feel feel free to raise your hand.

**[01:05]** Yeah, feel feel free to raise your hand. Sorry. Should I move away from the

**[01:07]** Sorry. Should I move away from the

**[01:07]** Sorry. Should I move away from the speaker a little bit? Maybe for a little

**[01:10]** speaker a little bit? Maybe for a little

**[01:10]** speaker a little bit? Maybe for a little bit. All right, I'll stand on this.

**[01:11]** bit. All right, I'll stand on this.

**[01:11]** bit. All right, I'll stand on this. Trying to understand like how to

**[01:12]** Trying to understand like how to

**[01:12]** Trying to understand like how to approach it. Oh, I I see.

**[01:16]** approach it. Oh, I I see.

**[01:16]** approach it. Oh, I I see. Okay. So, so trying to understand how to

**[01:18]** Okay. So, so trying to understand how to

**[01:18]** Okay. So, so trying to understand how to how to approach evals. Um, for people

**[01:21]** how to approach evals. Um, for people

**[01:21]** how to approach evals. Um, for people who have tried before, what have they

**[01:24]** who have tried before, what have they

**[01:24]** who have tried before, what have they struggled with? What has been the Go

**[01:27]** struggled with? What has been the Go

**[01:27]** struggled with? What has been the Go ahead. I think the struggle one is to

**[01:30]** ahead. I think the struggle one is to

**[01:30]** ahead. I think the struggle one is to define the metrics that because it's

**[01:33]** define the metrics that because it's

**[01:33]** define the metrics that because it's hard to like I do situations. So, first

**[01:37]** hard to like I do situations. So, first

**[01:37]** hard to like I do situations. So, first it's hard to define what's the correct

**[01:39]** it's hard to define what's the correct

**[01:39]** it's hard to define what's the correct answer because it can look in many

**[01:40]** answer because it can look in many

**[01:40]** answer because it can look in many different ways and two is um they are

**[01:43]** different ways and two is um they are

**[01:43]** different ways and two is um they are end based business questions and then

**[01:45]** end based business questions and then

**[01:45]** end based business questions and then you can

**[01:47]** you can

**[01:47]** you can and how do you pragmatically

**[01:51]** and how do you pragmatically

**[01:51]** and how do you pragmatically improve it versus I design and I review

**[01:54]** improve it versus I design and I review

**[01:54]** improve it versus I design and I review it and I do it again and I feel like

**[01:57]** it and I do it again and I feel like

**[01:57]** it and I do it again and I feel like that's still very manual and labor


### [02:00 - 03:00]

**[02:00]** that's still very manual and labor

**[02:00]** that's still very manual and labor intensive to me right

**[02:03]** intensive to me right

**[02:03]** intensive to me right yeah it's a eval can be labor intensive

**[02:05]** yeah it's a eval can be labor intensive

**[02:05]** yeah it's a eval can be labor intensive evals can be hard to hard to set up um

**[02:09]** evals can be hard to hard to set up um

**[02:09]** evals can be hard to hard to set up um they can be painful to get get started

**[02:13]** they can be painful to get get started

**[02:13]** they can be painful to get get started with um any other thoughts

**[02:21]** It's like machine learning is dependent

**[02:21]** It's like machine learning is dependent upon training data. Agents are depending

**[02:24]** upon training data. Agents are depending

**[02:24]** upon training data. Agents are depending upon eval to provide feedback from the

**[02:27]** upon eval to provide feedback from the

**[02:27]** upon eval to provide feedback from the world to let them know whether or not

**[02:29]** world to let them know whether or not

**[02:29]** world to let them know whether or not they're getting it right. And clearly

**[02:30]** they're getting it right. And clearly

**[02:30]** they're getting it right. And clearly it's sophisticated and challenging

**[02:32]** it's sophisticated and challenging

**[02:32]** it's sophisticated and challenging problem. So like how to do science you

**[02:35]** problem. So like how to do science you

**[02:35]** problem. So like how to do science you have to have experiments. This is like

**[02:37]** have to have experiments. This is like

**[02:37]** have to have experiments. This is like that. How do you experiment? Right. So

**[02:39]** that. How do you experiment? Right. So

**[02:39]** that. How do you experiment? Right. So we are all I'm just saying it's super

**[02:41]** we are all I'm just saying it's super

**[02:41]** we are all I'm just saying it's super important. We are all getting pulled

**[02:42]** important. We are all getting pulled

**[02:42]** important. We are all getting pulled into the the world of data science and

**[02:44]** into the the world of data science and

**[02:44]** into the the world of data science and machine learning in some ways even if we

**[02:46]** machine learning in some ways even if we

**[02:46]** machine learning in some ways even if we don't want to. Go ahead.

**[02:50]** don't want to. Go ahead.

**[02:50]** don't want to. Go ahead. Yes. Sorry. Uh engineering was a part of

**[02:53]** Yes. Sorry. Uh engineering was a part of

**[02:53]** Yes. Sorry. Uh engineering was a part of quality assurance team and you know all

**[02:56]** quality assurance team and you know all

**[02:56]** quality assurance team and you know all these years people wasn't happy that

**[02:58]** these years people wasn't happy that

**[02:58]** these years people wasn't happy that testing testing took I don't know 30% of


### [03:00 - 04:00]

**[03:01]** testing testing took I don't know 30% of

**[03:01]** testing testing took I don't know 30% of feature development time and now with AI

**[03:05]** feature development time and now with AI

**[03:05]** feature development time and now with AI I think that validation took 80% of

**[03:08]** I think that validation took 80% of

**[03:08]** I think that validation took 80% of feature development time. people even

**[03:11]** feature development time. people even

**[03:11]** feature development time. people even more not happy about it and we are

**[03:13]** more not happy about it and we are

**[03:13]** more not happy about it and we are trying to find ways also to to find a

**[03:17]** trying to find ways also to to find a

**[03:17]** trying to find ways also to to find a shortcuts but it seems that it's not

**[03:19]** shortcuts but it seems that it's not

**[03:19]** shortcuts but it seems that it's not always possible because each case is so

**[03:21]** always possible because each case is so

**[03:21]** always possible because each case is so unique that you just can't to reuse some

**[03:24]** unique that you just can't to reuse some

**[03:24]** unique that you just can't to reuse some previous works and you have to create

**[03:27]** previous works and you have to create

**[03:27]** previous works and you have to create many things from scratch on different

**[03:29]** many things from scratch on different

**[03:29]** many things from scratch on different levels and and because of this unclear

**[03:33]** levels and and because of this unclear

**[03:33]** levels and and because of this unclear nature pro probable nature of evaluation

**[03:36]** nature pro probable nature of evaluation

**[03:36]** nature pro probable nature of evaluation it's every time it's such a

**[03:45]** optimized way to do it,

**[03:45]** optimized way to do it, right? So, basically um you said speak

**[03:48]** right? So, basically um you said speak

**[03:48]** right? So, basically um you said speak up or speak low. Okay. Speak up. Okay.

**[03:52]** up or speak low. Okay. Speak up. Okay.

**[03:52]** up or speak low. Okay. Speak up. Okay. Um

**[03:58]** yeah. So, so basically like um it's

**[03:58]** yeah. So, so basically like um it's custom sub subjective eval like for your


### [04:00 - 05:00]

**[04:02]** custom sub subjective eval like for your

**[04:02]** custom sub subjective eval like for your specific use case. You just copy paste

**[04:04]** specific use case. You just copy paste

**[04:04]** specific use case. You just copy paste something that exists much like tests.

**[04:06]** something that exists much like tests.

**[04:06]** something that exists much like tests. We used to do testing. Some people did

**[04:08]** We used to do testing. Some people did

**[04:08]** We used to do testing. Some people did testing, some didn't. But now for for in

**[04:11]** testing, some didn't. But now for for in

**[04:11]** testing, some didn't. But now for for in the world of AI, everyone has to do

**[04:13]** the world of AI, everyone has to do

**[04:13]** the world of AI, everyone has to do evals. Everyone is spending a lot of

**[04:14]** evals. Everyone is spending a lot of

**[04:14]** evals. Everyone is spending a lot of time doing eval. Uh the best practices

**[04:17]** time doing eval. Uh the best practices

**[04:17]** time doing eval. Uh the best practices don't exist. So I go ahead please. Oh,

**[04:20]** don't exist. So I go ahead please. Oh,

**[04:20]** don't exist. So I go ahead please. Oh, uh I was just going to add that I'm

**[04:23]** uh I was just going to add that I'm

**[04:23]** uh I was just going to add that I'm looking forward to understand how

**[04:24]** looking forward to understand how

**[04:24]** looking forward to understand how synthetic data is playing a role there

**[04:27]** synthetic data is playing a role there

**[04:27]** synthetic data is playing a role there and especially for novelty like type of

**[04:29]** and especially for novelty like type of

**[04:29]** and especially for novelty like type of problems where you don't have access to

**[04:31]** problems where you don't have access to

**[04:31]** problems where you don't have access to real real world data to use as a data

**[04:33]** real real world data to use as a data

**[04:33]** real real world data to use as a data line. So how much of this can impact the

**[04:35]** line. So how much of this can impact the

**[04:35]** line. So how much of this can impact the evolve system?

**[04:37]** evolve system?

**[04:37]** evolve system? Right. There are like two aspects of

**[04:40]** Right. There are like two aspects of

**[04:40]** Right. There are like two aspects of eval. There's the synthetic data and

**[04:42]** eval. There's the synthetic data and

**[04:42]** eval. There's the synthetic data and there are the metrics. Metrics are

**[04:44]** there are the metrics. Metrics are

**[04:44]** there are the metrics. Metrics are checking. Synthetic data is testing it.

**[04:47]** checking. Synthetic data is testing it.

**[04:47]** checking. Synthetic data is testing it. Uh how what does synthetic data do? How

**[04:49]** Uh how what does synthetic data do? How

**[04:49]** Uh how what does synthetic data do? How do you generate good synthetic data to

**[04:51]** do you generate good synthetic data to

**[04:51]** do you generate good synthetic data to test and evaluate? Um go ahead. Mine

**[04:55]** test and evaluate? Um go ahead. Mine

**[04:55]** test and evaluate? Um go ahead. Mine goes along with the first comment. We've

**[04:57]** goes along with the first comment. We've

**[04:57]** goes along with the first comment. We've been trying on element models and use to


### [05:00 - 06:00]

**[05:02]** been trying on element models and use to

**[05:02]** been trying on element models and use to evaluate but

**[05:04]** evaluate but

**[05:04]** evaluate but it's not accurate. So we have to do this

**[05:06]** it's not accurate. So we have to do this

**[05:06]** it's not accurate. So we have to do this manually and hoping to learn that what

**[05:10]** manually and hoping to learn that what

**[05:10]** manually and hoping to learn that what are some right

**[05:13]** are some right

**[05:13]** are some right right like

**[05:16]** right like

**[05:16]** right like automatic evals are are something

**[05:19]** automatic evals are are something

**[05:19]** automatic evals are are something everybody desires because you don't want

**[05:21]** everybody desires because you don't want

**[05:21]** everybody desires because you don't want a like human beings to sit and do it uh

**[05:24]** a like human beings to sit and do it uh

**[05:24]** a like human beings to sit and do it uh but the options that are are somewhat

**[05:26]** but the options that are are somewhat

**[05:26]** but the options that are are somewhat limited typically for most things you

**[05:29]** limited typically for most things you

**[05:29]** limited typically for most things you can lean on AI to do human tasks for for

**[05:32]** can lean on AI to do human tasks for for

**[05:32]** can lean on AI to do human tasks for for some reason eval tend to be hard LMS to

**[05:35]** some reason eval tend to be hard LMS to

**[05:35]** some reason eval tend to be hard LMS to do Right. Um, so I guess that's that

**[05:38]** do Right. Um, so I guess that's that

**[05:38]** do Right. Um, so I guess that's that makes a lot of sense. I we're not going

**[05:40]** makes a lot of sense. I we're not going

**[05:40]** makes a lot of sense. I we're not going to solve all your eval problems here.

**[05:43]** to solve all your eval problems here.

**[05:43]** to solve all your eval problems here. I think this is a honest a very hard

**[05:45]** I think this is a honest a very hard

**[05:45]** I think this is a honest a very hard research area that we would probably

**[05:48]** research area that we would probably

**[05:48]** research area that we would probably continue working on in the next few

**[05:49]** continue working on in the next few

**[05:49]** continue working on in the next few months. Um, but David and I were were at

**[05:52]** months. Um, but David and I were were at

**[05:52]** months. Um, but David and I were were at Google for for over a decade and uh we

**[05:56]** Google for for over a decade and uh we

**[05:56]** Google for for over a decade and uh we have been doing eval for for a long

**[05:58]** have been doing eval for for a long

**[05:58]** have been doing eval for for a long time. Uh, we we dealt with stoastic


### [06:00 - 07:00]

**[06:01]** time. Uh, we we dealt with stoastic

**[06:01]** time. Uh, we we dealt with stoastic application. We both search we were

**[06:03]** application. We both search we were

**[06:03]** application. We both search we were building search. search was also

**[06:05]** building search. search was also

**[06:05]** building search. search was also similarly stochastic and most of uh the

**[06:09]** similarly stochastic and most of uh the

**[06:09]** similarly stochastic and most of uh the core effort in Google was to do a good

**[06:11]** core effort in Google was to do a good

**[06:11]** core effort in Google was to do a good job of evaluating where we are and

**[06:13]** job of evaluating where we are and

**[06:13]** job of evaluating where we are and improving it and some of the techniques

**[06:15]** improving it and some of the techniques

**[06:15]** improving it and some of the techniques we learned at Google we are bringing in

**[06:18]** we learned at Google we are bringing in

**[06:18]** we learned at Google we are bringing in here um so we built a product around it

**[06:22]** here um so we built a product around it

**[06:22]** here um so we built a product around it a bunch of technology around it but

**[06:24]** a bunch of technology around it but

**[06:24]** a bunch of technology around it but really the biggest takeaway I want

**[06:26]** really the biggest takeaway I want

**[06:26]** really the biggest takeaway I want people to have is the methodology and

**[06:28]** people to have is the methodology and

**[06:28]** people to have is the methodology and the stuff that we have learned uh

**[06:30]** the stuff that we have learned uh

**[06:30]** the stuff that we have learned uh whatever manifestation it takes right so

**[06:33]** whatever manifestation it takes right so

**[06:33]** whatever manifestation it takes right so I'm hoping that you get to play with

**[06:34]** I'm hoping that you get to play with

**[06:34]** I'm hoping that you get to play with some of our stuff but also to learn some

**[06:37]** some of our stuff but also to learn some

**[06:37]** some of our stuff but also to learn some some good ideas. Um David you want to

**[06:41]** some good ideas. Um David you want to

**[06:41]** some good ideas. Um David you want to add? Yeah, I mean one thing I would add

**[06:43]** add? Yeah, I mean one thing I would add

**[06:43]** add? Yeah, I mean one thing I would add is at Google we used to call this

**[06:45]** is at Google we used to call this

**[06:45]** is at Google we used to call this quality and evalu was part of it and

**[06:47]** quality and evalu was part of it and

**[06:47]** quality and evalu was part of it and there was this constant idea like

**[06:49]** there was this constant idea like

**[06:49]** there was this constant idea like benchmarking and you know exhausting a

**[06:50]** benchmarking and you know exhausting a

**[06:50]** benchmarking and you know exhausting a benchmark and then moving on to the next

**[06:52]** benchmark and then moving on to the next

**[06:52]** benchmark and then moving on to the next benchmark whenever we work with clients

**[06:53]** benchmark whenever we work with clients

**[06:54]** benchmark whenever we work with clients right now we we take a similar approach

**[06:55]** right now we we take a similar approach

**[06:55]** right now we we take a similar approach so like a chin mentioned so much of eval

**[06:57]** so like a chin mentioned so much of eval

**[06:57]** so like a chin mentioned so much of eval is just good methodology setting up

**[06:59]** is just good methodology setting up

**[06:59]** is just good methodology setting up benchmarks trying to figure out the


### [07:00 - 08:00]

**[07:00]** benchmarks trying to figure out the

**[07:00]** benchmarks trying to figure out the metrics that work calibrating metrics

**[07:02]** metrics that work calibrating metrics

**[07:02]** metrics that work calibrating metrics with humans calibrating metrics with

**[07:03]** with humans calibrating metrics with

**[07:03]** with humans calibrating metrics with user data uh what I'm trying to say is

**[07:05]** user data uh what I'm trying to say is

**[07:06]** user data uh what I'm trying to say is it can get arbitrarily complex like

**[07:07]** it can get arbitrarily complex like

**[07:07]** it can get arbitrarily complex like evals is not like oh there's one way to

**[07:09]** evals is not like oh there's one way to

**[07:09]** evals is not like oh there's one way to do it and then you're done it's it's

**[07:10]** do it and then you're done it's it's

**[07:10]** do it and then you're done it's it's just part of how you do development

**[07:12]** just part of how you do development

**[07:12]** just part of how you do development uh which you know everybody's been

**[07:13]** uh which you know everybody's been

**[07:13]** uh which you know everybody's been struggling with because we've all been

**[07:14]** struggling with because we've all been

**[07:14]** struggling with because we've all been trying to learn what it means to develop

**[07:16]** trying to learn what it means to develop

**[07:16]** trying to learn what it means to develop on top of this new stack but again today

**[07:18]** on top of this new stack but again today

**[07:18]** on top of this new stack but again today in today's session we're just hoping to

**[07:19]** in today's session we're just hoping to

**[07:19]** in today's session we're just hoping to bring you some of these ideas where like

**[07:21]** bring you some of these ideas where like

**[07:21]** bring you some of these ideas where like methodologies that make sense like how

**[07:22]** methodologies that make sense like how

**[07:22]** methodologies that make sense like how to think about your metrics maybe people

**[07:24]** to think about your metrics maybe people

**[07:24]** to think about your metrics maybe people think of like four metrics so I would

**[07:25]** think of like four metrics so I would

**[07:25]** think of like four metrics so I would challenge you search had 300 metrics so

**[07:27]** challenge you search had 300 metrics so

**[07:27]** challenge you search had 300 metrics so like you start to think about like how

**[07:29]** like you start to think about like how

**[07:29]** like you start to think about like how can you expand the scope of how you're

**[07:30]** can you expand the scope of how you're

**[07:30]** can you expand the scope of how you're doing this work uh and you know part of

**[07:33]** doing this work uh and you know part of

**[07:33]** doing this work uh and you know part of what we're doing is trying to build

**[07:34]** what we're doing is trying to build

**[07:34]** what we're doing is trying to build technologies that make it easy to adopt

**[07:35]** technologies that make it easy to adopt

**[07:35]** technologies that make it easy to adopt these these technologies how to create

**[07:37]** these these technologies how to create

**[07:37]** these these technologies how to create benchmarks that are interesting how to

**[07:39]** benchmarks that are interesting how to

**[07:39]** benchmarks that are interesting how to like make it harder um and then we can

**[07:41]** like make it harder um and then we can

**[07:41]** like make it harder um and then we can talk about about this as we go. Uh this

**[07:43]** talk about about this as we go. Uh this

**[07:43]** talk about about this as we go. Uh this workshop will be mostly hands-on. Uh

**[07:45]** workshop will be mostly hands-on. Uh

**[07:45]** workshop will be mostly hands-on. Uh we'll show a few slides and then we'll

**[07:46]** we'll show a few slides and then we'll

**[07:46]** we'll show a few slides and then we'll dive into the code because I think the

**[07:48]** dive into the code because I think the

**[07:48]** dive into the code because I think the best way to to learn about these things

**[07:49]** best way to to learn about these things

**[07:50]** best way to to learn about these things is just to to do them. Um I think as we

**[07:52]** is just to to do them. Um I think as we

**[07:52]** is just to to do them. Um I think as we go we'd love to just pass it around and

**[07:54]** go we'd love to just pass it around and

**[07:54]** go we'd love to just pass it around and you know if people have you know again

**[07:57]** you know if people have you know again

**[07:57]** you know if people have you know again people are at different parts of the

**[07:58]** people are at different parts of the

**[07:58]** people are at different parts of the journey for some people like hey I don't

**[07:59]** journey for some people like hey I don't


### [08:00 - 09:00]

**[08:00]** journey for some people like hey I don't have metrics and I'll just develop my

**[08:01]** have metrics and I'll just develop my

**[08:01]** have metrics and I'll just develop my own metrics. Uh we worked with clients

**[08:03]** own metrics. Uh we worked with clients

**[08:03]** own metrics. Uh we worked with clients that have metrics but they want to for

**[08:04]** that have metrics but they want to for

**[08:04]** that have metrics but they want to for example correlate them to user behavior.

**[08:06]** example correlate them to user behavior.

**[08:06]** example correlate them to user behavior. They have a lot of thumbs up thumbs down

**[08:07]** They have a lot of thumbs up thumbs down

**[08:07]** They have a lot of thumbs up thumbs down data. Um so that goes all the way into a

**[08:09]** data. Um so that goes all the way into a

**[08:09]** data. Um so that goes all the way into a feedback loop. So you see like evals is

**[08:11]** feedback loop. So you see like evals is

**[08:11]** feedback loop. So you see like evals is not just one thing related to testing.

**[08:13]** not just one thing related to testing.

**[08:13]** not just one thing related to testing. It goes all the way into your online

**[08:14]** It goes all the way into your online

**[08:14]** It goes all the way into your online system and your feedback loops and all

**[08:16]** system and your feedback loops and all

**[08:16]** system and your feedback loops and all that. So but hopefully a lot of the

**[08:17]** that. So but hopefully a lot of the

**[08:17]** that. So but hopefully a lot of the mental models today will help you kind

**[08:19]** mental models today will help you kind

**[08:19]** mental models today will help you kind of gauge that. Um just two two is things

**[08:22]** of gauge that. Um just two two is things

**[08:22]** of gauge that. Um just two two is things the slack channel it's uh workshops

**[08:25]** the slack channel it's uh workshops

**[08:25]** the slack channel it's uh workshops uh so you can join there on the slack

**[08:27]** uh so you can join there on the slack

**[08:27]** uh so you can join there on the slack and then we'll just be posting things

**[08:28]** and then we'll just be posting things

**[08:28]** and then we'll just be posting things and then we can have discussions and

**[08:29]** and then we can have discussions and

**[08:29]** and then we can have discussions and continue the conversations uh even after

**[08:31]** continue the conversations uh even after

**[08:31]** continue the conversations uh even after the the the workshop. And uh the second

**[08:35]** the the the workshop. And uh the second

**[08:35]** the the the workshop. And uh the second one is uh we have a document that will

**[08:37]** one is uh we have a document that will

**[08:37]** one is uh we have a document that will have all the steps uh of the workshop uh

**[08:40]** have all the steps uh of the workshop uh

**[08:40]** have all the steps uh of the workshop uh all the places where you can get the

**[08:42]** all the places where you can get the

**[08:42]** all the places where you can get the code where you can get the sheet just go

**[08:43]** code where you can get the sheet just go

**[08:44]** code where you can get the sheet just go with pi.ai/workshop you will land in a

**[08:46]** with pi.ai/workshop you will land in a

**[08:46]** with pi.ai/workshop you will land in a Google doc uh so there's a lot of links

**[08:48]** Google doc uh so there's a lot of links

**[08:48]** Google doc uh so there's a lot of links the Google doc also has a link to the

**[08:50]** the Google doc also has a link to the

**[08:50]** the Google doc also has a link to the slide deck we're presenting so you can

**[08:51]** slide deck we're presenting so you can

**[08:51]** slide deck we're presenting so you can have it we'll keep it online even after

**[08:53]** have it we'll keep it online even after

**[08:53]** have it we'll keep it online even after the workshop so you guys can reference

**[08:55]** the workshop so you guys can reference

**[08:55]** the workshop so you guys can reference it. Um all right we'll get started to to

**[08:58]** it. Um all right we'll get started to to

**[08:58]** it. Um all right we'll get started to to keep you guys on time and maximize sort


### [09:00 - 10:00]

**[09:00]** keep you guys on time and maximize sort

**[09:00]** keep you guys on time and maximize sort of coding time. Yeah, I uh there are

**[09:02]** of coding time. Yeah, I uh there are

**[09:02]** of coding time. Yeah, I uh there are four of us. A couple of other people

**[09:04]** four of us. A couple of other people

**[09:04]** four of us. A couple of other people will just walk around. If you guys get

**[09:05]** will just walk around. If you guys get

**[09:05]** will just walk around. If you guys get stuck on any step, if you're having

**[09:07]** stuck on any step, if you're having

**[09:07]** stuck on any step, if you're having trouble with anything, just raise your

**[09:08]** trouble with anything, just raise your

**[09:08]** trouble with anything, just raise your hands and then we'll come and raise your

**[09:10]** hands and then we'll come and raise your

**[09:10]** hands and then we'll come and raise your hand over. Um all right, I'll give you a

**[09:13]** hand over. Um all right, I'll give you a

**[09:13]** hand over. Um all right, I'll give you a very like maybe five minute uh quick

**[09:16]** very like maybe five minute uh quick

**[09:16]** very like maybe five minute uh quick blur, show a quick demo and then get

**[09:19]** blur, show a quick demo and then get

**[09:19]** blur, show a quick demo and then get started. Um

**[09:21]** started. Um

**[09:21]** started. Um so

**[09:23]** so

**[09:23]** so can you guys still hear me? Yeah,

**[09:27]** can you guys still hear me? Yeah,

**[09:27]** can you guys still hear me? Yeah, I think we went went through this, but

**[09:28]** I think we went went through this, but

**[09:28]** I think we went went through this, but basically like most people start with

**[09:30]** basically like most people start with

**[09:30]** basically like most people start with VIP testing. That's like, you know, try

**[09:32]** VIP testing. That's like, you know, try

**[09:32]** VIP testing. That's like, you know, try it out, see how it works, change

**[09:34]** it out, see how it works, change

**[09:34]** it out, see how it works, change prompts. And honestly, for many

**[09:35]** prompts. And honestly, for many

**[09:35]** prompts. And honestly, for many applications, you can go pretty far with

**[09:37]** applications, you can go pretty far with

**[09:37]** applications, you can go pretty far with just that. Like I think AI AIS have

**[09:40]** just that. Like I think AI AIS have

**[09:40]** just that. Like I think AI AIS have become much quite good. I think agent

**[09:42]** become much quite good. I think agent

**[09:42]** become much quite good. I think agent systems, as you uh you were saying,

**[09:44]** systems, as you uh you were saying,

**[09:44]** systems, as you uh you were saying, agent systems are more complex because

**[09:46]** agent systems are more complex because

**[09:46]** agent systems are more complex because of multiple steps. Things fail more

**[09:48]** of multiple steps. Things fail more

**[09:48]** of multiple steps. Things fail more often. But wipe testing gets you pretty

**[09:50]** often. But wipe testing gets you pretty

**[09:50]** often. But wipe testing gets you pretty far. Human evals are expensive.

**[09:52]** far. Human evals are expensive.

**[09:52]** far. Human evals are expensive. Typically most companies don't bother

**[09:56]** Typically most companies don't bother

**[09:56]** Typically most companies don't bother setting up human var. Some do. Some have

**[09:58]** setting up human var. Some do. Some have

**[09:58]** setting up human var. Some do. Some have subject m matter experts. Uh codebased


### [10:00 - 11:00]

**[10:01]** subject m matter experts. Uh codebased

**[10:01]** subject m matter experts. Uh codebased evals is where I think majority of the

**[10:03]** evals is where I think majority of the

**[10:03]** evals is where I think majority of the people are spending time. They're

**[10:04]** people are spending time. They're

**[10:04]** people are spending time. They're writing some sort of a code to test some

**[10:07]** writing some sort of a code to test some

**[10:07]** writing some sort of a code to test some verifiable things that they can and and

**[10:09]** verifiable things that they can and and

**[10:10]** verifiable things that they can and and people are moving into natural language

**[10:11]** people are moving into natural language

**[10:11]** people are moving into natural language like LM as a judge type things where it

**[10:15]** like LM as a judge type things where it

**[10:15]** like LM as a judge type things where it gets this is not a very good task. We'll

**[10:17]** gets this is not a very good task. We'll

**[10:17]** gets this is not a very good task. We'll get into some of it like for for t t t t

**[10:20]** get into some of it like for for t t t t

**[10:20]** get into some of it like for for t t t t t t t t t t t t t t t t t t t t t t t t

**[10:20]** t t t t t t t t t t t t t t t t t t t t

**[10:20]** t t t t t t t t t t t t t t t t t t t t t t t t t t t t t t t t t t t typical

**[10:20]** t t t t t t t t t t t t t t t typical

**[10:20]** t t t t t t t t t t t t t t t typical decoder models, the AI models. And so

**[10:22]** decoder models, the AI models. And so

**[10:22]** decoder models, the AI models. And so you kind of have to fight against um

**[10:24]** you kind of have to fight against um

**[10:24]** you kind of have to fight against um they're these models are designed to be

**[10:26]** they're these models are designed to be

**[10:26]** they're these models are designed to be creative. They're designed to be um

**[10:29]** creative. They're designed to be um

**[10:29]** creative. They're designed to be um that's not what you want from a judge.

**[10:31]** that's not what you want from a judge.

**[10:31]** that's not what you want from a judge. Typically

**[10:33]** Typically

**[10:33]** Typically this the scoring system uh scoring

**[10:35]** this the scoring system uh scoring

**[10:35]** this the scoring system uh scoring system is this idea that you you you're

**[10:39]** system is this idea that you you you're

**[10:39]** system is this idea that you you you're not trying hard to build a comprehensive

**[10:41]** not trying hard to build a comprehensive

**[10:41]** not trying hard to build a comprehensive set of metrics from the beginning. You

**[10:43]** set of metrics from the beginning. You

**[10:43]** set of metrics from the beginning. You start with some correlated signals.

**[10:46]** start with some correlated signals.

**[10:46]** start with some correlated signals. Maybe you start with five, 10 signals

**[10:48]** Maybe you start with five, 10 signals

**[10:48]** Maybe you start with five, 10 signals that you know for a fact are correlated

**[10:51]** that you know for a fact are correlated

**[10:51]** that you know for a fact are correlated with goodness. They're very simple

**[10:53]** with goodness. They're very simple

**[10:53]** with goodness. They're very simple signals that you can easily derive and

**[10:56]** signals that you can easily derive and

**[10:56]** signals that you can easily derive and then time you build upon those as you

**[10:59]** then time you build upon those as you

**[10:59]** then time you build upon those as you see problems as you as you debug and and


### [11:00 - 12:00]

**[11:02]** see problems as you as you debug and and

**[11:02]** see problems as you as you debug and and then you test your application works

**[11:04]** then you test your application works

**[11:04]** then you test your application works well or not you learn from it. You build

**[11:07]** well or not you learn from it. You build

**[11:07]** well or not you learn from it. You build your application you measure it again.

**[11:09]** your application you measure it again.

**[11:09]** your application you measure it again. So that grip makes it a much more of a

**[11:11]** So that grip makes it a much more of a

**[11:11]** So that grip makes it a much more of a feedback loop type process. Uh that's

**[11:13]** feedback loop type process. Uh that's

**[11:13]** feedback loop type process. Uh that's the thing that we're trying to introduce

**[11:15]** the thing that we're trying to introduce

**[11:15]** the thing that we're trying to introduce in terms of methodology.

**[11:17]** in terms of methodology.

**[11:17]** in terms of methodology. Uh the thing that David was saying yeah

**[11:19]** Uh the thing that David was saying yeah

**[11:20]** Uh the thing that David was saying yeah one thing I will add to that is like

**[11:21]** one thing I will add to that is like

**[11:21]** one thing I will add to that is like there's no right or wrong like vibe

**[11:23]** there's no right or wrong like vibe

**[11:23]** there's no right or wrong like vibe testing actually gets you a very long

**[11:24]** testing actually gets you a very long

**[11:24]** testing actually gets you a very long way. Um sorry we we have a lot of echo.

**[11:27]** way. Um sorry we we have a lot of echo.

**[11:27]** way. Um sorry we we have a lot of echo. Um maybe you want to turn that off and

**[11:29]** Um maybe you want to turn that off and

**[11:29]** Um maybe you want to turn that off and then we can switch the mic as we

**[11:33]** then we can switch the mic as we

**[11:33]** then we can switch the mic as we yeah so ju just say like it it's there's

**[11:35]** yeah so ju just say like it it's there's

**[11:35]** yeah so ju just say like it it's there's no right or wrong. I think you should

**[11:36]** no right or wrong. I think you should

**[11:36]** no right or wrong. I think you should absolutely start with vibe testing. A

**[11:37]** absolutely start with vibe testing. A

**[11:37]** absolutely start with vibe testing. A lot of people use tracing and they just

**[11:39]** lot of people use tracing and they just

**[11:39]** lot of people use tracing and they just monitor traces. I think a as your system

**[11:41]** monitor traces. I think a as your system

**[11:41]** monitor traces. I think a as your system scales, you do want to get a little bit

**[11:43]** scales, you do want to get a little bit

**[11:43]** scales, you do want to get a little bit more sophisticated. Uh so you you start

**[11:45]** more sophisticated. Uh so you you start

**[11:45]** more sophisticated. Uh so you you start to layer those things in order of

**[11:46]** to layer those things in order of

**[11:46]** to layer those things in order of complexity. That's a lot of how we talk

**[11:48]** complexity. That's a lot of how we talk

**[11:48]** complexity. That's a lot of how we talk about quality generally is this idea of

**[11:50]** about quality generally is this idea of

**[11:50]** about quality generally is this idea of like there's complex things but they

**[11:51]** like there's complex things but they

**[11:51]** like there's complex things but they give some amount of investment of some

**[11:53]** give some amount of investment of some

**[11:53]** give some amount of investment of some of amount of return. So it's like a

**[11:55]** of amount of return. So it's like a

**[11:55]** of amount of return. So it's like a little bit of an ROI. Some things are

**[11:56]** little bit of an ROI. Some things are

**[11:56]** little bit of an ROI. Some things are very cheap to do and then you do them

**[11:58]** very cheap to do and then you do them

**[11:58]** very cheap to do and then you do them and as your system scales they become


### [12:00 - 13:00]

**[12:00]** and as your system scales they become

**[12:00]** and as your system scales they become impractical and then you just layer in

**[12:01]** impractical and then you just layer in

**[12:01]** impractical and then you just layer in more techniques. So there's not a

**[12:03]** more techniques. So there's not a

**[12:03]** more techniques. So there's not a statement that like any of these things

**[12:04]** statement that like any of these things

**[12:04]** statement that like any of these things are good or bad. You just need all of

**[12:06]** are good or bad. You just need all of

**[12:06]** are good or bad. You just need all of them. So think of these things as tools

**[12:07]** them. So think of these things as tools

**[12:07]** them. So think of these things as tools in your toolbox, but eventually what you

**[12:09]** in your toolbox, but eventually what you

**[12:09]** in your toolbox, but eventually what you really want is a scoring system. Now how

**[12:11]** really want is a scoring system. Now how

**[12:11]** really want is a scoring system. Now how it manifests for you, you should you

**[12:13]** it manifests for you, you should you

**[12:13]** it manifests for you, you should you should be the judge of it, but like this

**[12:14]** should be the judge of it, but like this

**[12:14]** should be the judge of it, but like this is one thing to get away with like just

**[12:16]** is one thing to get away with like just

**[12:16]** is one thing to get away with like just keep layering into your tools and with

**[12:18]** keep layering into your tools and with

**[12:18]** keep layering into your tools and with increasing levels of sophistication, you

**[12:20]** increasing levels of sophistication, you

**[12:20]** increasing levels of sophistication, you get probably to a system that will look

**[12:21]** get probably to a system that will look

**[12:22]** get probably to a system that will look like the one we'll develop today.

**[12:29]** Yeah. And as David was saying like um

**[12:29]** Yeah. And as David was saying like um are such such an investment. So they

**[12:31]** are such such an investment. So they

**[12:31]** are such such an investment. So they might might ask like well why am I

**[12:33]** might might ask like well why am I

**[12:33]** might might ask like well why am I spending so much time on just eval why

**[12:34]** spending so much time on just eval why

**[12:34]** spending so much time on just eval why am I not building and I think one of the

**[12:37]** am I not building and I think one of the

**[12:37]** am I not building and I think one of the things that that was core to to Google

**[12:39]** things that that was core to to Google

**[12:39]** things that that was core to to Google and I think we this industry is going to

**[12:41]** and I think we this industry is going to

**[12:41]** and I think we this industry is going to adopt this over time is that eval are

**[12:43]** adopt this over time is that eval are

**[12:43]** adopt this over time is that eval are actually the only place you're going to

**[12:45]** actually the only place you're going to

**[12:45]** actually the only place you're going to spend most of your time because that's

**[12:47]** spend most of your time because that's

**[12:47]** spend most of your time because that's where domain knowledge is going to live

**[12:48]** where domain knowledge is going to live

**[12:48]** where domain knowledge is going to live everything else will just work off of

**[12:50]** everything else will just work off of

**[12:50]** everything else will just work off of those evals and so um so for example if

**[12:54]** those evals and so um so for example if

**[12:54]** those evals and so um so for example if you have really good evals you don't

**[12:56]** you have really good evals you don't

**[12:56]** you have really good evals you don't have to write prompts you can write like

**[12:59]** have to write prompts you can write like

**[12:59]** have to write prompts you can write like you can find problems and use meta


### [13:00 - 14:00]

**[13:00]** you can find problems and use meta

**[13:00]** you can find problems and use meta prompts or optimizers like DSPI and

**[13:03]** prompts or optimizers like DSPI and

**[13:03]** prompts or optimizers like DSPI and others to improve your prompts yourself.

**[13:05]** others to improve your prompts yourself.

**[13:05]** others to improve your prompts yourself. You can filter out synthetic data and

**[13:07]** You can filter out synthetic data and

**[13:07]** You can filter out synthetic data and then use that for fine-tuning if you're

**[13:09]** then use that for fine-tuning if you're

**[13:09]** then use that for fine-tuning if you're really interested in fine-tuning or or

**[13:11]** really interested in fine-tuning or or

**[13:11]** really interested in fine-tuning or or reinforcement learning. But you can also

**[13:13]** reinforcement learning. But you can also

**[13:13]** reinforcement learning. But you can also use these techniques online, right? One

**[13:15]** use these techniques online, right? One

**[13:15]** use these techniques online, right? One of the things that you're going to test

**[13:16]** of the things that you're going to test

**[13:16]** of the things that you're going to test to try today is a very simple but very

**[13:19]** to try today is a very simple but very

**[13:19]** to try today is a very simple but very effective technique that almost all big

**[13:21]** effective technique that almost all big

**[13:21]** effective technique that almost all big labs use. um Google used it extensively

**[13:24]** labs use. um Google used it extensively

**[13:24]** labs use. um Google used it extensively which is the the idea that you crank up

**[13:26]** which is the the idea that you crank up

**[13:26]** which is the the idea that you crank up the temperature, you generate a bunch of

**[13:28]** the temperature, you generate a bunch of

**[13:28]** the temperature, you generate a bunch of responses instead of just one response.

**[13:30]** responses instead of just one response.

**[13:30]** responses instead of just one response. You can think of this as online

**[13:31]** You can think of this as online

**[13:31]** You can think of this as online reinforcement learning, generate four or

**[13:33]** reinforcement learning, generate four or

**[13:33]** reinforcement learning, generate four or five responses and then score those

**[13:35]** five responses and then score those

**[13:35]** five responses and then score those responses online and see which one's the

**[13:37]** responses online and see which one's the

**[13:37]** responses online and see which one's the best one and you get a pretty decent

**[13:39]** best one and you get a pretty decent

**[13:40]** best one and you get a pretty decent lift just by doing this like without

**[13:41]** lift just by doing this like without

**[13:41]** lift just by doing this like without actually doing any changes to your

**[13:43]** actually doing any changes to your

**[13:43]** actually doing any changes to your prompts or models and so on. So that

**[13:45]** prompts or models and so on. So that

**[13:45]** prompts or models and so on. So that these are the kinds of things you can do

**[13:47]** these are the kinds of things you can do

**[13:47]** these are the kinds of things you can do uh with when when you have a really good

**[13:49]** uh with when when you have a really good

**[13:49]** uh with when when you have a really good scoring system that you can lean on. So

**[13:51]** scoring system that you can lean on. So

**[13:51]** scoring system that you can lean on. So you get to try some of these techniques

**[13:52]** you get to try some of these techniques

**[13:52]** you get to try some of these techniques today. Um but but the key point is don't

**[13:56]** today. Um but but the key point is don't

**[13:56]** today. Um but but the key point is don't think of eval as testing in the classic

**[13:58]** think of eval as testing in the classic

**[13:58]** think of eval as testing in the classic sense. Think of these as the primary


### [14:00 - 15:00]

**[14:00]** sense. Think of these as the primary

**[14:00]** sense. Think of these as the primary place where domain knowledge lives. Um

**[14:03]** place where domain knowledge lives. Um

**[14:03]** place where domain knowledge lives. Um and then and then one of one of the

**[14:04]** and then and then one of one of the

**[14:04]** and then and then one of one of the things like that I I think um one of the

**[14:07]** things like that I I think um one of the

**[14:07]** things like that I I think um one of the attendees was pointing out is that tip

**[14:10]** attendees was pointing out is that tip

**[14:10]** attendees was pointing out is that tip right now at this point in the AI

**[14:12]** right now at this point in the AI

**[14:12]** right now at this point in the AI industry we have figured out a handful

**[14:14]** industry we have figured out a handful

**[14:14]** industry we have figured out a handful of standard evals like you can think of

**[14:16]** of standard evals like you can think of

**[14:16]** of standard evals like you can think of simple helpfulness harmfulness

**[14:19]** simple helpfulness harmfulness

**[14:19]** simple helpfulness harmfulness hallucinations

**[14:20]** hallucinations

**[14:20]** hallucinations and that doesn't really get you far

**[14:22]** and that doesn't really get you far

**[14:22]** and that doesn't really get you far enough. That's good enough to just sort

**[14:24]** enough. That's good enough to just sort

**[14:24]** enough. That's good enough to just sort of do a guardrail and make sure you're

**[14:26]** of do a guardrail and make sure you're

**[14:26]** of do a guardrail and make sure you're not doing anything wrong. But we are

**[14:29]** not doing anything wrong. But we are

**[14:29]** not doing anything wrong. But we are we're moving into the world where you

**[14:30]** we're moving into the world where you

**[14:30]** we're moving into the world where you want to build really good. Like for

**[14:32]** want to build really good. Like for

**[14:32]** want to build really good. Like for example, if you're trying to build a

**[14:33]** example, if you're trying to build a

**[14:33]** example, if you're trying to build a trip plan, you you you're curious about

**[14:35]** trip plan, you you you're curious about

**[14:35]** trip plan, you you you're curious about like, you know, how how to make that

**[14:37]** like, you know, how how to make that

**[14:37]** like, you know, how how to make that trip plan really be perfect. Like one of

**[14:39]** trip plan really be perfect. Like one of

**[14:39]** trip plan really be perfect. Like one of the things I I really hate about trip

**[14:40]** the things I I really hate about trip

**[14:40]** the things I I really hate about trip plans if they're too like not

**[14:42]** plans if they're too like not

**[14:42]** plans if they're too like not interesting enough. I'm looking at a

**[14:44]** interesting enough. I'm looking at a

**[14:44]** interesting enough. I'm looking at a trip plan. I want to be excited about

**[14:45]** trip plan. I want to be excited about

**[14:45]** trip plan. I want to be excited about this place. Typically, when LM give me a

**[14:48]** this place. Typically, when LM give me a

**[14:48]** this place. Typically, when LM give me a trip plan, it's a very kind of very

**[14:50]** trip plan, it's a very kind of very

**[14:50]** trip plan, it's a very kind of very planishish, right? So now you're trying

**[14:52]** planishish, right? So now you're trying

**[14:52]** planishish, right? So now you're trying to build these sort of nuances in your

**[14:53]** to build these sort of nuances in your

**[14:54]** to build these sort of nuances in your applications. And that's the kind of

**[14:55]** applications. And that's the kind of

**[14:56]** applications. And that's the kind of stuff if you want to evaluate that's

**[14:57]** stuff if you want to evaluate that's

**[14:57]** stuff if you want to evaluate that's where that's where the industry is going

**[14:58]** where that's where the industry is going

**[14:58]** where that's where the industry is going to go. So how do you build like these


### [15:00 - 16:00]

**[15:00]** to go. So how do you build like these

**[15:00]** to go. So how do you build like these much more nuanced evals uh that that's

**[15:03]** much more nuanced evals uh that that's

**[15:03]** much more nuanced evals uh that that's one of the places where these

**[15:04]** one of the places where these

**[15:04]** one of the places where these traditional evals fail. So, as I went

**[15:07]** traditional evals fail. So, as I went

**[15:07]** traditional evals fail. So, as I went over, like start simple, iterate, see

**[15:10]** over, like start simple, iterate, see

**[15:10]** over, like start simple, iterate, see what's broken, and then improve, right?

**[15:13]** what's broken, and then improve, right?

**[15:13]** what's broken, and then improve, right? And so, that's the other thing you get

**[15:15]** And so, that's the other thing you get

**[15:15]** And so, that's the other thing you get to try today is in a co-pilot-like

**[15:17]** to try today is in a co-pilot-like

**[15:17]** to try today is in a co-pilot-like setting. Start with something, test it

**[15:21]** setting. Start with something, test it

**[15:21]** setting. Start with something, test it out with a handful of examples, maybe

**[15:22]** out with a handful of examples, maybe

**[15:22]** out with a handful of examples, maybe generate some synthetic examples, test

**[15:24]** generate some synthetic examples, test

**[15:24]** generate some synthetic examples, test it out with good examples, bad examples,

**[15:26]** it out with good examples, bad examples,

**[15:26]** it out with good examples, bad examples, see what's working, what's not, and then

**[15:28]** see what's working, what's not, and then

**[15:28]** see what's working, what's not, and then iterate. We have picked a relatively

**[15:30]** iterate. We have picked a relatively

**[15:30]** iterate. We have picked a relatively simple example for today because for

**[15:31]** simple example for today because for

**[15:31]** simple example for today because for workshop purposes we wanted to keep it

**[15:33]** workshop purposes we wanted to keep it

**[15:33]** workshop purposes we wanted to keep it simple but you can absolutely go and try

**[15:36]** simple but you can absolutely go and try

**[15:36]** simple but you can absolutely go and try it on fairly complex things and and

**[15:38]** it on fairly complex things and and

**[15:38]** it on fairly complex things and and there you can see a lot more of the

**[15:39]** there you can see a lot more of the

**[15:39]** there you can see a lot more of the nuances.

**[15:41]** nuances.

**[15:41]** nuances. Um

**[15:43]** Um

**[15:43]** Um so yeah so there are two parts of

**[15:45]** so yeah so there are two parts of

**[15:45]** so yeah so there are two parts of today's workshop the first part is

**[15:48]** today's workshop the first part is

**[15:48]** today's workshop the first part is um setting up your scoring system and

**[15:51]** um setting up your scoring system and

**[15:51]** um setting up your scoring system and the second part is once you have set up

**[15:53]** the second part is once you have set up

**[15:53]** the second part is once you have set up the scoring system and played with it

**[15:54]** the scoring system and played with it

**[15:54]** the scoring system and played with it and iterated on it in a co-pilot trying

**[15:56]** and iterated on it in a co-pilot trying

**[15:56]** and iterated on it in a co-pilot trying to use it in a collab you would need a

**[15:59]** to use it in a collab you would need a

**[15:59]** to use it in a collab you would need a Google account and some some proficiency


### [16:00 - 17:00]

**[16:02]** Google account and some some proficiency

**[16:02]** Google account and some some proficiency in working with collabs and python code

**[16:05]** in working with collabs and python code

**[16:05]** in working with collabs and python code um we'll also introduce a spreadsheet

**[16:08]** um we'll also introduce a spreadsheet

**[16:08]** um we'll also introduce a spreadsheet component to this so that you can

**[16:09]** component to this so that you can

**[16:09]** component to this so that you can actually try to play around with this in

**[16:11]** actually try to play around with this in

**[16:11]** actually try to play around with this in a spreadsheet um so that you uh you can

**[16:14]** a spreadsheet um so that you uh you can

**[16:14]** a spreadsheet um so that you uh you can easily make changes and test things out.

**[16:18]** easily make changes and test things out.

**[16:18]** easily make changes and test things out. Uh one last thing I want to hit on

**[16:19]** Uh one last thing I want to hit on

**[16:19]** Uh one last thing I want to hit on before we jump into the the the workshop

**[16:23]** before we jump into the the the workshop

**[16:23]** before we jump into the the the workshop is what what is the scoring system? What

**[16:26]** is what what is the scoring system? What

**[16:26]** is what what is the scoring system? What is this idea of scoring system? Right?

**[16:28]** is this idea of scoring system? Right?

**[16:28]** is this idea of scoring system? Right? is just to give you a mental framing of

**[16:30]** is just to give you a mental framing of

**[16:30]** is just to give you a mental framing of it. Um

**[16:38]** ranking is scoring is eval

**[16:38]** ranking is scoring is eval to think about it. When Google does a

**[16:40]** to think about it. When Google does a

**[16:40]** to think about it. When Google does a search, what it's trying to do is it's

**[16:42]** search, what it's trying to do is it's

**[16:42]** search, what it's trying to do is it's scoring every document and seeing

**[16:44]** scoring every document and seeing

**[16:44]** scoring every document and seeing whether this is good or not and then

**[16:45]** whether this is good or not and then

**[16:45]** whether this is good or not and then giving you the best document that's the

**[16:47]** giving you the best document that's the

**[16:47]** giving you the best document that's the best for you. And that's not that

**[16:49]** best for you. And that's not that

**[16:49]** best for you. And that's not that different from te checking and scoring

**[16:51]** different from te checking and scoring

**[16:51]** different from te checking and scoring an LM generated content. And the way

**[16:54]** an LM generated content. And the way

**[16:54]** an LM generated content. And the way Google does it is by breaking this

**[16:56]** Google does it is by breaking this

**[16:56]** Google does it is by breaking this problem down into a ton of signals,

**[16:58]** problem down into a ton of signals,

**[16:58]** problem down into a ton of signals, right? So you can imagine you're looking


### [17:00 - 18:00]

**[17:00]** right? So you can imagine you're looking

**[17:00]** right? So you can imagine you're looking at SEO, you can look at document

**[17:02]** at SEO, you can look at document

**[17:02]** at SEO, you can look at document popularity, you're looking at title

**[17:04]** popularity, you're looking at title

**[17:04]** popularity, you're looking at title scores, whether the content is good or

**[17:05]** scores, whether the content is good or

**[17:05]** scores, whether the content is good or not, uh maybe feasibility of things, um

**[17:09]** not, uh maybe feasibility of things, um

**[17:09]** not, uh maybe feasibility of things, um spam, you know, click batiness, stuff

**[17:11]** spam, you know, click batiness, stuff

**[17:11]** spam, you know, click batiness, stuff like that, and then brings all of these

**[17:13]** like that, and then brings all of these

**[17:13]** like that, and then brings all of these signals together into a single score

**[17:15]** signals together into a single score

**[17:15]** signals together into a single score that combines these these ideas.

**[17:17]** that combines these these ideas.

**[17:17]** that combines these these ideas. Individual signals that you have are

**[17:19]** Individual signals that you have are

**[17:19]** Individual signals that you have are very easy to understand. You know what

**[17:21]** very easy to understand. You know what

**[17:21]** very easy to understand. You know what that is, you can inspect it very easily.

**[17:23]** that is, you can inspect it very easily.

**[17:23]** that is, you can inspect it very easily. It's not a complex prompt with some

**[17:25]** It's not a complex prompt with some

**[17:25]** It's not a complex prompt with some random score. It's something that you

**[17:26]** random score. It's something that you

**[17:26]** random score. It's something that you can easily understand but it all comes

**[17:28]** can easily understand but it all comes

**[17:28]** can easily understand but it all comes together into a single score and that's

**[17:30]** together into a single score and that's

**[17:30]** together into a single score and that's the idea we are sort of bringing in and

**[17:31]** the idea we are sort of bringing in and

**[17:31]** the idea we are sort of bringing in and that's what we call a scoring system. At

**[17:34]** that's what we call a scoring system. At

**[17:34]** that's what we call a scoring system. At the bottom level things are very

**[17:35]** the bottom level things are very

**[17:36]** the bottom level things are very objective tend to be deterministic

**[17:38]** objective tend to be deterministic

**[17:38]** objective tend to be deterministic sometimes just Python code but as you

**[17:41]** sometimes just Python code but as you

**[17:41]** sometimes just Python code but as you bring this up to the top it becomes

**[17:43]** bring this up to the top it becomes

**[17:43]** bring this up to the top it becomes fairly subjective and you can like bring

**[17:45]** fairly subjective and you can like bring

**[17:45]** fairly subjective and you can like bring these together into very complex ways.

**[17:47]** these together into very complex ways.

**[17:47]** these together into very complex ways. Yeah. And I would just uh encourage you

**[17:49]** Yeah. And I would just uh encourage you

**[17:49]** Yeah. And I would just uh encourage you to think about like why this why why

**[17:51]** to think about like why this why why

**[17:51]** to think about like why this why why this kind of why this could work and and

**[17:53]** this kind of why this could work and and

**[17:53]** this kind of why this could work and and we know it does work. Um some of what

**[17:55]** we know it does work. Um some of what

**[17:56]** we know it does work. Um some of what you will be struggling with with eval is

**[17:57]** you will be struggling with with eval is

**[17:57]** you will be struggling with with eval is just like you're not measuring the

**[17:59]** just like you're not measuring the

**[17:59]** just like you're not measuring the things you need to be measuring. So you


### [18:00 - 19:00]

**[18:00]** things you need to be measuring. So you

**[18:00]** things you need to be measuring. So you have a little bit of a comprehensive

**[18:02]** have a little bit of a comprehensive

**[18:02]** have a little bit of a comprehensive issue and so like the question is like

**[18:04]** issue and so like the question is like

**[18:04]** issue and so like the question is like how many metrics do you need to add? So

**[18:05]** how many metrics do you need to add? So

**[18:05]** how many metrics do you need to add? So I give the example Google search uses

**[18:07]** I give the example Google search uses

**[18:07]** I give the example Google search uses around 300 signals. Now maybe you don't

**[18:09]** around 300 signals. Now maybe you don't

**[18:09]** around 300 signals. Now maybe you don't want to be that but like Google does

**[18:11]** want to be that but like Google does

**[18:11]** want to be that but like Google does care about all those things. They care

**[18:12]** care about all those things. They care

**[18:12]** care about all those things. They care about like you know the score of the

**[18:13]** about like you know the score of the

**[18:13]** about like you know the score of the site. They care about popularity. They

**[18:15]** site. They care about popularity. They

**[18:15]** site. They care about popularity. They care about content relevance, spam, porn

**[18:17]** care about content relevance, spam, porn

**[18:17]** care about content relevance, spam, porn seeeking. They have all these

**[18:18]** seeeking. They have all these

**[18:18]** seeeking. They have all these classifiers, all these ways they

**[18:19]** classifiers, all these ways they

**[18:19]** classifiers, all these ways they understand the content to then bring it

**[18:21]** understand the content to then bring it

**[18:21]** understand the content to then bring it together. What this gives you is like

**[18:22]** together. What this gives you is like

**[18:22]** together. What this gives you is like really visibility over your application

**[18:23]** really visibility over your application

**[18:24]** really visibility over your application and more and more ways to marry your own

**[18:26]** and more and more ways to marry your own

**[18:26]** and more and more ways to marry your own judgment into it. So if if instead you

**[18:29]** judgment into it. So if if instead you

**[18:29]** judgment into it. So if if instead you just go and say, "Hey, is this a helpful

**[18:30]** just go and say, "Hey, is this a helpful

**[18:30]** just go and say, "Hey, is this a helpful response?" Mostly what you're doing is

**[18:32]** response?" Mostly what you're doing is

**[18:32]** response?" Mostly what you're doing is delegating that that eval to the LLM

**[18:35]** delegating that that eval to the LLM

**[18:35]** delegating that that eval to the LLM itself, right? Or to a raider who you're

**[18:37]** itself, right? Or to a raider who you're

**[18:37]** itself, right? Or to a raider who you're asking like, "Hey, see if this is good."

**[18:38]** asking like, "Hey, see if this is good."

**[18:38]** asking like, "Hey, see if this is good." But when you break this all down, you

**[18:40]** But when you break this all down, you

**[18:40]** But when you break this all down, you get some really nice properties where

**[18:42]** get some really nice properties where

**[18:42]** get some really nice properties where like your variance goes down a lot just

**[18:44]** like your variance goes down a lot just

**[18:44]** like your variance goes down a lot just because you're measuring way more

**[18:45]** because you're measuring way more

**[18:45]** because you're measuring way more objective things. So things are not like

**[18:47]** objective things. So things are not like

**[18:47]** objective things. So things are not like going back and forth all the time. And

**[18:49]** going back and forth all the time. And

**[18:49]** going back and forth all the time. And it's very precise because like you're

**[18:50]** it's very precise because like you're

**[18:50]** it's very precise because like you're you get all these things and you add

**[18:51]** you get all these things and you add

**[18:51]** you get all these things and you add them together to a more high fidelity

**[18:53]** them together to a more high fidelity

**[18:53]** them together to a more high fidelity score. And when you are analyzing the

**[18:55]** score. And when you are analyzing the

**[18:55]** score. And when you are analyzing the data then you can like slice and dice by

**[18:57]** data then you can like slice and dice by

**[18:57]** data then you can like slice and dice by way finer grain things. And that's kind

**[18:59]** way finer grain things. And that's kind

**[18:59]** way finer grain things. And that's kind of like why the system tends to work


### [19:00 - 20:00]

**[19:01]** of like why the system tends to work

**[19:01]** of like why the system tends to work much better. And the best part of it is

**[19:03]** much better. And the best part of it is

**[19:03]** much better. And the best part of it is as you iterate you just add more

**[19:04]** as you iterate you just add more

**[19:04]** as you iterate you just add more signals. like this now doesn't leave you

**[19:07]** signals. like this now doesn't leave you

**[19:07]** signals. like this now doesn't leave you as like oh I either have evals or I

**[19:08]** as like oh I either have evals or I

**[19:08]** as like oh I either have evals or I don't have heals but like rather you

**[19:10]** don't have heals but like rather you

**[19:10]** don't have heals but like rather you just have a set of metrics that you keep

**[19:12]** just have a set of metrics that you keep

**[19:12]** just have a set of metrics that you keep adding over over time as you discover

**[19:14]** adding over over time as you discover

**[19:14]** adding over over time as you discover what actually matters about your

**[19:16]** what actually matters about your

**[19:16]** what actually matters about your oh

**[19:29]** okay uh

**[19:29]** okay uh how do I do this

**[19:35]** um okay so I'll just quickly show you a

**[19:35]** um okay so I'll just quickly show you a demo of where you're going to start

**[19:36]** demo of where you're going to start

**[19:36]** demo of where you're going to start today. Uh give you some sort of basic

**[19:39]** today. Uh give you some sort of basic

**[19:39]** today. Uh give you some sort of basic ideas of the kinds of things you would

**[19:41]** ideas of the kinds of things you would

**[19:41]** ideas of the kinds of things you would be doing. Uh and then and then I'll just

**[19:43]** be doing. Uh and then and then I'll just

**[19:43]** be doing. Uh and then and then I'll just we we we should just get started, right?

**[19:45]** we we we should just get started, right?

**[19:45]** we we we should just get started, right? And so this is uh this is a co-pilot

**[19:47]** And so this is uh this is a co-pilot

**[19:47]** And so this is uh this is a co-pilot that helps you put together your value

**[19:49]** that helps you put together your value

**[19:50]** that helps you put together your value eval. That's the idea where I'm starting

**[19:52]** eval. That's the idea where I'm starting

**[19:52]** eval. That's the idea where I'm starting is basically just a system prompt. This

**[19:54]** is basically just a system prompt. This

**[19:54]** is basically just a system prompt. This is this application is basically a

**[19:56]** is this application is basically a

**[19:56]** is this application is basically a simple meeting summarizer. It takes uh a

**[19:58]** simple meeting summarizer. It takes uh a

**[19:58]** simple meeting summarizer. It takes uh a meeting script talking talking between


### [20:00 - 21:00]

**[20:00]** meeting script talking talking between

**[20:00]** meeting script talking talking between multiple people and then generates some

**[20:02]** multiple people and then generates some

**[20:02]** multiple people and then generates some sort of a structured JSON in the end

**[20:04]** sort of a structured JSON in the end

**[20:04]** sort of a structured JSON in the end which is a summary with very specific um

**[20:08]** which is a summary with very specific um

**[20:08]** which is a summary with very specific um action items key key u key insights and

**[20:12]** action items key key u key insights and

**[20:12]** action items key key u key insights and then a title right so it's a relatively

**[20:14]** then a title right so it's a relatively

**[20:14]** then a title right so it's a relatively simple thing it's easy for you to

**[20:15]** simple thing it's easy for you to

**[20:15]** simple thing it's easy for you to inspect and see where things are not

**[20:16]** inspect and see where things are not

**[20:16]** inspect and see where things are not going working and not working well um so

**[20:19]** going working and not working well um so

**[20:19]** going working and not working well um so typically you would start with something

**[20:21]** typically you would start with something

**[20:21]** typically you would start with something like a system prompt you can also start

**[20:23]** like a system prompt you can also start

**[20:23]** like a system prompt you can also start with examples if you have a bunch of

**[20:25]** with examples if you have a bunch of

**[20:25]** with examples if you have a bunch of examples or you can start with criteria

**[20:27]** examples or you can start with criteria

**[20:27]** examples or you can start with criteria itself. Um, and

**[20:31]** itself. Um, and

**[20:31]** itself. Um, and the the first step is it would try to

**[20:33]** the the first step is it would try to

**[20:33]** the the first step is it would try to use this to build your scoring system.

**[20:36]** use this to build your scoring system.

**[20:36]** use this to build your scoring system. Um,

**[20:41]** yeah. And uh, this is doing exactly what

**[20:41]** yeah. And uh, this is doing exactly what was in that slide which is trying to say

**[20:43]** was in that slide which is trying to say

**[20:43]** was in that slide which is trying to say like from that coar grain subjective

**[20:44]** like from that coar grain subjective

**[20:44]** like from that coar grain subjective thing what are all the smaller things I

**[20:46]** thing what are all the smaller things I

**[20:46]** thing what are all the smaller things I can I can sus out out of it. Now this

**[20:49]** can I can sus out out of it. Now this

**[20:49]** can I can sus out out of it. Now this uses a reasoning model like if you drop

**[20:51]** uses a reasoning model like if you drop

**[20:51]** uses a reasoning model like if you drop this into a chat GPT or so uh we just

**[20:53]** this into a chat GPT or so uh we just

**[20:54]** this into a chat GPT or so uh we just try to replicate that experience where

**[20:55]** try to replicate that experience where

**[20:55]** try to replicate that experience where you get these artifacts on the right

**[20:56]** you get these artifacts on the right

**[20:56]** you get these artifacts on the right hand side which are your is your actual

**[20:58]** hand side which are your is your actual

**[20:58]** hand side which are your is your actual scoring system but if you think you just


### [21:00 - 22:00]

**[21:00]** scoring system but if you think you just

**[21:00]** scoring system but if you think you just want to do it like iteratively through

**[21:01]** want to do it like iteratively through

**[21:01]** want to do it like iteratively through your favorite like sort of chat and

**[21:03]** your favorite like sort of chat and

**[21:03]** your favorite like sort of chat and phase you can also do it just say oops

**[21:05]** phase you can also do it just say oops

**[21:05]** phase you can also do it just say oops go ahead we do it in reverse where we

**[21:07]** go ahead we do it in reverse where we

**[21:07]** go ahead we do it in reverse where we provide examples of input and output and

**[21:10]** provide examples of input and output and

**[21:10]** provide examples of input and output and yes exactly right so right in front

**[21:12]** yes exactly right so right in front

**[21:12]** yes exactly right so right in front there is an example button you can start

**[21:14]** there is an example button you can start

**[21:14]** there is an example button you can start with example you can give it actually

**[21:16]** with example you can give it actually

**[21:16]** with example you can give it actually hundreds of examples if you want 20

**[21:18]** hundreds of examples if you want 20

**[21:18]** hundreds of examples if you want 20 examples uh and then it gets into a much

**[21:21]** examples uh and then it gets into a much

**[21:21]** examples uh and then it gets into a much more complex process of like figuring

**[21:22]** more complex process of like figuring

**[21:22]** more complex process of like figuring out these dimensions based on example or

**[21:24]** out these dimensions based on example or

**[21:24]** out these dimensions based on example or you can just copy paste one or two

**[21:25]** you can just copy paste one or two

**[21:25]** you can just copy paste one or two examples in the prompt itself and it

**[21:27]** examples in the prompt itself and it

**[21:27]** examples in the prompt itself and it will it'll generate it. Um the this is

**[21:31]** will it'll generate it. Um the this is

**[21:31]** will it'll generate it. Um the this is just a starting point by the way that's

**[21:32]** just a starting point by the way that's

**[21:32]** just a starting point by the way that's the idea it it starts you somewhere and

**[21:34]** the idea it it starts you somewhere and

**[21:34]** the idea it it starts you somewhere and now you're going to iterate over it and

**[21:36]** now you're going to iterate over it and

**[21:36]** now you're going to iterate over it and that's the exercise you will you'll

**[21:37]** that's the exercise you will you'll

**[21:37]** that's the exercise you will you'll spend time on. I'll show you a few

**[21:39]** spend time on. I'll show you a few

**[21:39]** spend time on. I'll show you a few things like this is your scoring system.

**[21:41]** things like this is your scoring system.

**[21:41]** things like this is your scoring system. These are your individual

**[21:44]** These are your individual

**[21:44]** These are your individual um these are individual dimensions is

**[21:46]** um these are individual dimensions is

**[21:46]** um these are individual dimensions is what we call it or you can think of

**[21:47]** what we call it or you can think of

**[21:47]** what we call it or you can think of these as signals. Uh they're all

**[21:50]** these as signals. Uh they're all

**[21:50]** these as signals. Uh they're all questions um effectively. For example,

**[21:53]** questions um effectively. For example,

**[21:53]** questions um effectively. For example, this is a does the output include any

**[21:55]** this is a does the output include any

**[21:55]** this is a does the output include any insights from the meeting. That's a

**[21:57]** insights from the meeting. That's a

**[21:57]** insights from the meeting. That's a natural language question. Um or you can


### [22:00 - 23:00]

**[22:01]** natural language question. Um or you can

**[22:01]** natural language question. Um or you can have code um just Python code that we

**[22:03]** have code um just Python code that we

**[22:03]** have code um just Python code that we have generated. You can edit this code

**[22:05]** have generated. You can edit this code

**[22:05]** have generated. You can edit this code however you want. Uh this this uh this

**[22:10]** however you want. Uh this this uh this

**[22:10]** however you want. Uh this this uh this this is actually as simple as what this

**[22:12]** this is actually as simple as what this

**[22:12]** this is actually as simple as what this this says. When you when you look at the

**[22:14]** this says. When you when you look at the

**[22:14]** this says. When you when you look at the actual code, the code is effectively

**[22:16]** actual code, the code is effectively

**[22:16]** actual code, the code is effectively just a bunch of questions and you're

**[22:17]** just a bunch of questions and you're

**[22:17]** just a bunch of questions and you're sending these questions to our

**[22:19]** sending these questions to our

**[22:19]** sending these questions to our specialized foundation models that are

**[22:21]** specialized foundation models that are

**[22:21]** specialized foundation models that are designed for scoring and evaluation. Um,

**[22:24]** designed for scoring and evaluation. Um,

**[22:24]** designed for scoring and evaluation. Um, so you'll get to play with this a bunch

**[22:26]** so you'll get to play with this a bunch

**[22:26]** so you'll get to play with this a bunch in the collab. You can see what the form

**[22:28]** in the collab. You can see what the form

**[22:28]** in the collab. You can see what the form of it looks like. There's another thing

**[22:30]** of it looks like. There's another thing

**[22:30]** of it looks like. There's another thing that you would notice that there's this

**[22:31]** that you would notice that there's this

**[22:31]** that you would notice that there's this idea of critical, major, minor. These

**[22:33]** idea of critical, major, minor. These

**[22:33]** idea of critical, major, minor. These are just weights. These are just way

**[22:35]** are just weights. These are just way

**[22:35]** are just weights. These are just way ways for you to control what's

**[22:36]** ways for you to control what's

**[22:36]** ways for you to control what's important, what's not. The combination

**[22:38]** important, what's not. The combination

**[22:38]** important, what's not. The combination of this is done through a mathematical

**[22:40]** of this is done through a mathematical

**[22:40]** of this is done through a mathematical function that that you can learn over

**[22:42]** function that that you can learn over

**[22:42]** function that that you can learn over time. So actually eventually you would

**[22:44]** time. So actually eventually you would

**[22:44]** time. So actually eventually you would give it a bunch of examples and it'll

**[22:45]** give it a bunch of examples and it'll

**[22:45]** give it a bunch of examples and it'll learn it. But in this particular

**[22:46]** learn it. But in this particular

**[22:46]** learn it. But in this particular exercise you have a little bit more

**[22:48]** exercise you have a little bit more

**[22:48]** exercise you have a little bit more control. And finally once you have your

**[22:50]** control. And finally once you have your

**[22:50]** control. And finally once you have your scoring system uh done uh there is a way

**[22:54]** scoring system uh done uh there is a way

**[22:54]** scoring system uh done uh there is a way for you to integrate it into Google

**[22:55]** for you to integrate it into Google

**[22:56]** for you to integrate it into Google Sheets. That's the thing that you're

**[22:57]** Sheets. That's the thing that you're

**[22:57]** Sheets. That's the thing that you're going to play around with today which is

**[22:59]** going to play around with today which is

**[22:59]** going to play around with today which is basically taking this criteria moving it


### [23:00 - 24:00]

**[23:01]** basically taking this criteria moving it

**[23:01]** basically taking this criteria moving it to a Google sheet and testing it against

**[23:03]** to a Google sheet and testing it against

**[23:03]** to a Google sheet and testing it against real examples. So here you're going to

**[23:06]** real examples. So here you're going to

**[23:06]** real examples. So here you're going to work with synthetic examples. You'll

**[23:08]** work with synthetic examples. You'll

**[23:08]** work with synthetic examples. You'll develop your scoring system and then

**[23:10]** develop your scoring system and then

**[23:10]** develop your scoring system and then completely blinded to this. We have

**[23:11]** completely blinded to this. We have

**[23:12]** completely blinded to this. We have label data set where users are set

**[23:14]** label data set where users are set

**[23:14]** label data set where users are set thumbs up thumbs down on the summaries.

**[23:15]** thumbs up thumbs down on the summaries.

**[23:16]** thumbs up thumbs down on the summaries. You're going to apply this to that

**[23:17]** You're going to apply this to that

**[23:17]** You're going to apply this to that scoring system and see how well it

**[23:18]** scoring system and see how well it

**[23:18]** scoring system and see how well it aligns with real real thumbs up thumbs

**[23:20]** aligns with real real thumbs up thumbs

**[23:20]** aligns with real real thumbs up thumbs down. Um so we don't know. It depends on

**[23:23]** down. Um so we don't know. It depends on

**[23:23]** down. Um so we don't know. It depends on you. You you're you're building your own

**[23:25]** you. You you're you're building your own

**[23:25]** you. You you're you're building your own scoring system whether it aligns or not.

**[23:27]** scoring system whether it aligns or not.

**[23:27]** scoring system whether it aligns or not. Um yeah and and this is a really

**[23:30]** Um yeah and and this is a really

**[23:30]** Um yeah and and this is a really interesting point and why why eval start

**[23:31]** interesting point and why why eval start

**[23:32]** interesting point and why why eval start to get hard like we we call this

**[23:33]** to get hard like we we call this

**[23:33]** to get hard like we we call this workshop like solving the hardest

**[23:34]** workshop like solving the hardest

**[23:34]** workshop like solving the hardest challenge which is metrics that actually

**[23:36]** challenge which is metrics that actually

**[23:36]** challenge which is metrics that actually work. So this idea of like correlation

**[23:37]** work. So this idea of like correlation

**[23:38]** work. So this idea of like correlation ends up being really really important.

**[23:39]** ends up being really really important.

**[23:39]** ends up being really really important. Metrics that work are not necessarily

**[23:41]** Metrics that work are not necessarily

**[23:41]** Metrics that work are not necessarily good metrics or bad metrics. They're

**[23:42]** good metrics or bad metrics. They're

**[23:42]** good metrics or bad metrics. They're either calibrated metrics or

**[23:44]** either calibrated metrics or

**[23:44]** either calibrated metrics or unccalibrated metrics. And this is where

**[23:45]** unccalibrated metrics. And this is where

**[23:45]** unccalibrated metrics. And this is where like uh at Google for example we had a

**[23:47]** like uh at Google for example we had a

**[23:47]** like uh at Google for example we had a lot of data scientists that we worked

**[23:49]** lot of data scientists that we worked

**[23:49]** lot of data scientists that we worked with right because they would do like

**[23:50]** with right because they would do like

**[23:50]** with right because they would do like all these correlation analyses and

**[23:52]** all these correlation analyses and

**[23:52]** all these correlation analyses and confusion matrices and such. So part of

**[23:54]** confusion matrices and such. So part of

**[23:54]** confusion matrices and such. So part of the challenge of of of good evals is

**[23:57]** the challenge of of of good evals is

**[23:57]** the challenge of of of good evals is just getting comfortable with the

**[23:58]** just getting comfortable with the

**[23:58]** just getting comfortable with the numerical aspect of these things. And of


### [24:00 - 25:00]

**[24:01]** numerical aspect of these things. And of

**[24:01]** numerical aspect of these things. And of course again having a scoring system

**[24:02]** course again having a scoring system

**[24:02]** course again having a scoring system that dissects things into much simpler

**[24:04]** that dissects things into much simpler

**[24:04]** that dissects things into much simpler things makes it easier to analyze. But

**[24:06]** things makes it easier to analyze. But

**[24:06]** things makes it easier to analyze. But you still have to think about those

**[24:07]** you still have to think about those

**[24:07]** you still have to think about those things like does this actually correlate

**[24:09]** things like does this actually correlate

**[24:09]** things like does this actually correlate with goodness? Like if it gives a high

**[24:10]** with goodness? Like if it gives a high

**[24:10]** with goodness? Like if it gives a high score is this an actually a good score

**[24:12]** score is this an actually a good score

**[24:12]** score is this an actually a good score and that's a big part of the

**[24:13]** and that's a big part of the

**[24:13]** and that's a big part of the methodology. But the good news is as as

**[24:15]** methodology. But the good news is as as

**[24:15]** methodology. But the good news is as as a chin showed in the previous slide,

**[24:16]** a chin showed in the previous slide,

**[24:16]** a chin showed in the previous slide, once you have metrics you can trust,

**[24:18]** once you have metrics you can trust,

**[24:18]** once you have metrics you can trust, like almost all of the rest of your

**[24:20]** like almost all of the rest of your

**[24:20]** like almost all of the rest of your stack gets radically simplified as a

**[24:23]** stack gets radically simplified as a

**[24:23]** stack gets radically simplified as a result.

**[24:24]** result.

**[24:24]** result. Okay. So how do you use this copilot?

**[24:26]** Okay. So how do you use this copilot?

**[24:26]** Okay. So how do you use this copilot? It's created this. Maybe a place to

**[24:28]** It's created this. Maybe a place to

**[24:28]** It's created this. Maybe a place to start would be, you know, generate an

**[24:30]** start would be, you know, generate an

**[24:30]** start would be, you know, generate an example. This is a synthetic generation

**[24:33]** example. This is a synthetic generation

**[24:33]** example. This is a synthetic generation uh um happening behind the scenes. It's

**[24:36]** uh um happening behind the scenes. It's

**[24:36]** uh um happening behind the scenes. It's taking uh your system prompt and other

**[24:38]** taking uh your system prompt and other

**[24:38]** taking uh your system prompt and other information and trying to generate uh

**[24:40]** information and trying to generate uh

**[24:40]** information and trying to generate uh some sort of an example and and then and

**[24:43]** some sort of an example and and then and

**[24:43]** some sort of an example and and then and then this example that is generated is

**[24:46]** then this example that is generated is

**[24:46]** then this example that is generated is scored and you can see how these

**[24:48]** scored and you can see how these

**[24:48]** scored and you can see how these individual scores work. Now you can

**[24:50]** individual scores work. Now you can

**[24:50]** individual scores work. Now you can start uh kind of testing this a little

**[24:52]** start uh kind of testing this a little

**[24:52]** start uh kind of testing this a little bit more. You can say um can you

**[24:56]** bit more. You can say um can you

**[24:56]** bit more. You can say um can you generate a bad example? Um and then it


### [25:00 - 26:00]

**[25:00]** generate a bad example? Um and then it

**[25:00]** generate a bad example? Um and then it will it will try to generate an example

**[25:01]** will it will try to generate an example

**[25:01]** will it will try to generate an example that's broken in some particular way. it

**[25:04]** that's broken in some particular way. it

**[25:04]** that's broken in some particular way. it the the copilot understands what you've

**[25:06]** the the copilot understands what you've

**[25:06]** the the copilot understands what you've done so far. It has the full context.

**[25:07]** done so far. It has the full context.

**[25:07]** done so far. It has the full context. It's using all of this information to

**[25:09]** It's using all of this information to

**[25:09]** It's using all of this information to kind of like sort of walk you through

**[25:11]** kind of like sort of walk you through

**[25:11]** kind of like sort of walk you through this. So in this particular way like in

**[25:13]** this. So in this particular way like in

**[25:13]** this. So in this particular way like in this particular case, it created

**[25:14]** this particular case, it created

**[25:14]** this particular case, it created something that is missing a bunch of

**[25:16]** something that is missing a bunch of

**[25:16]** something that is missing a bunch of information. But you can even do things

**[25:18]** information. But you can even do things

**[25:18]** information. But you can even do things like you know specific things like can

**[25:20]** like you know specific things like can

**[25:20]** like you know specific things like can you create uh an example that has broken

**[25:26]** you create uh an example that has broken

**[25:26]** you create uh an example that has broken JSON. Uh so this is like basically

**[25:28]** JSON. Uh so this is like basically

**[25:28]** JSON. Uh so this is like basically example generation. That's one one thing

**[25:31]** example generation. That's one one thing

**[25:31]** example generation. That's one one thing you can do here. The other thing you can

**[25:33]** you can do here. The other thing you can

**[25:33]** you can do here. The other thing you can do is you can make changes to your

**[25:36]** do is you can make changes to your

**[25:36]** do is you can make changes to your scoring system itself through the

**[25:37]** scoring system itself through the

**[25:38]** scoring system itself through the copilot. So you can either go and ask

**[25:40]** copilot. So you can either go and ask

**[25:40]** copilot. So you can either go and ask the copilot to make changes to your um

**[25:44]** the copilot to make changes to your um

**[25:44]** the copilot to make changes to your um anyways this is a broken JSON example.

**[25:46]** anyways this is a broken JSON example.

**[25:46]** anyways this is a broken JSON example. You can go to the c-ilot and either ask

**[25:48]** You can go to the c-ilot and either ask

**[25:48]** You can go to the c-ilot and either ask it to change the python code itself. You

**[25:50]** it to change the python code itself. You

**[25:50]** it to change the python code itself. You can say you know can you update the

**[25:51]** can say you know can you update the

**[25:51]** can say you know can you update the python code or and such of any of these

**[25:54]** python code or and such of any of these

**[25:54]** python code or and such of any of these things. You can also ask it to remove or

**[25:56]** things. You can also ask it to remove or

**[25:56]** things. You can also ask it to remove or add dimensions. Maybe you can say can

**[25:58]** add dimensions. Maybe you can say can

**[25:58]** add dimensions. Maybe you can say can you generate


### [26:00 - 27:00]

**[26:01]** you generate

**[26:01]** you generate a dimension that checks

**[26:05]** a dimension that checks

**[26:06]** a dimension that checks for the title to be less than 20 words

**[26:11]** for the title to be less than 20 words

**[26:11]** for the title to be less than 20 words and then the copilot can add these

**[26:14]** and then the copilot can add these

**[26:14]** and then the copilot can add these dimensions. Go ahead.

**[26:24]** Uhu.

**[26:24]** Uhu. Exactly.

**[26:31]** Exactly. What do you do just add you

**[26:31]** Exactly. What do you do just add you just ask the copilot and say I've

**[26:33]** just ask the copilot and say I've

**[26:33]** just ask the copilot and say I've updated here's a new examples can you

**[26:36]** updated here's a new examples can you

**[26:36]** updated here's a new examples can you add new dimensions to test these new

**[26:37]** add new dimensions to test these new

**[26:37]** add new dimensions to test these new examples or we have changed things and

**[26:39]** examples or we have changed things and

**[26:39]** examples or we have changed things and it automatically I mean it knows what

**[26:42]** it automatically I mean it knows what

**[26:42]** it automatically I mean it knows what layer it knows what layer you're exactly

**[26:45]** layer it knows what layer you're exactly

**[26:45]** layer it knows what layer you're exactly yeah the other thing I would say is the

**[26:48]** yeah the other thing I would say is the

**[26:48]** yeah the other thing I would say is the co-pilot is very helpful if you want

**[26:50]** co-pilot is very helpful if you want

**[26:50]** co-pilot is very helpful if you want this sort of human in a loop type

**[26:51]** this sort of human in a loop type

**[26:51]** this sort of human in a loop type process

**[26:53]** process

**[26:53]** process uh but once you get comfortable with the

**[26:55]** uh but once you get comfortable with the

**[26:55]** uh but once you get comfortable with the system what we see people doing is just

**[26:58]** system what we see people doing is just

**[26:58]** system what we see people doing is just use collab to and large amounts of data


### [27:00 - 28:00]

**[27:01]** use collab to and large amounts of data

**[27:02]** use collab to and large amounts of data and let our system figure things out on

**[27:03]** and let our system figure things out on

**[27:03]** and let our system figure things out on its own. Uh I I find by personally I

**[27:06]** its own. Uh I I find by personally I

**[27:06]** its own. Uh I I find by personally I find it very good to play with my

**[27:08]** find it very good to play with my

**[27:08]** find it very good to play with my scoring system here every so often to

**[27:10]** scoring system here every so often to

**[27:10]** scoring system here every so often to see if it's like working well like maybe

**[27:12]** see if it's like working well like maybe

**[27:12]** see if it's like working well like maybe paste an example from from a user and

**[27:15]** paste an example from from a user and

**[27:15]** paste an example from from a user and see how well it's working and so on and

**[27:16]** see how well it's working and so on and

**[27:16]** see how well it's working and so on and so forth. You can kind of go back and

**[27:18]** so forth. You can kind of go back and

**[27:18]** so forth. You can kind of go back and forth. Uh but but most of our clients

**[27:21]** forth. Uh but but most of our clients

**[27:21]** forth. Uh but but most of our clients actually just fire off these uh long

**[27:24]** actually just fire off these uh long

**[27:24]** actually just fire off these uh long longunning processes. Um yeah I think

**[27:27]** longunning processes. Um yeah I think

**[27:27]** longunning processes. Um yeah I think maybe so um so anyway so that's uh so it

**[27:31]** maybe so um so anyway so that's uh so it

**[27:31]** maybe so um so anyway so that's uh so it just created this new uh title length

**[27:33]** just created this new uh title length

**[27:33]** just created this new uh title length thing for you. So you can sort of play

**[27:35]** thing for you. So you can sort of play

**[27:35]** thing for you. So you can sort of play around with this um and it'll you can

**[27:38]** around with this um and it'll you can

**[27:38]** around with this um and it'll you can change the questions you can remove

**[27:39]** change the questions you can remove

**[27:39]** change the questions you can remove dimensions so on and so forth. Right.

**[27:41]** dimensions so on and so forth. Right.

**[27:41]** dimensions so on and so forth. Right. The last thing I would show before we

**[27:43]** The last thing I would show before we

**[27:43]** The last thing I would show before we get going is uh one of the things that

**[27:46]** get going is uh one of the things that

**[27:46]** get going is uh one of the things that you would do is we we have pre-filled a

**[27:49]** you would do is we we have pre-filled a

**[27:49]** you would do is we we have pre-filled a spreadsheet in the in the in the

**[27:51]** spreadsheet in the in the in the

**[27:51]** spreadsheet in the in the in the workshop directions. you will make a

**[27:53]** workshop directions. you will make a

**[27:53]** workshop directions. you will make a copy of that spreadsheet and we have a

**[27:56]** copy of that spreadsheet and we have a

**[27:56]** copy of that spreadsheet and we have a spreadsheet integration where you can

**[27:58]** spreadsheet integration where you can

**[27:58]** spreadsheet integration where you can run our score inside a spreadsheet

**[27:59]** run our score inside a spreadsheet

**[27:59]** run our score inside a spreadsheet itself. You see there are other other


### [28:00 - 29:00]

**[28:01]** itself. You see there are other other

**[28:01]** itself. You see there are other other sort of places where you can use it. I'm

**[28:03]** sort of places where you can use it. I'm

**[28:04]** sort of places where you can use it. I'm not going to get into this, but you can

**[28:05]** not going to get into this, but you can

**[28:05]** not going to get into this, but you can use it for reinforcement learning, for

**[28:06]** use it for reinforcement learning, for

**[28:06]** use it for reinforcement learning, for example, using onslaught integration,

**[28:08]** example, using onslaught integration,

**[28:08]** example, using onslaught integration, but there are other places you can

**[28:10]** but there are other places you can

**[28:10]** but there are other places you can actually integrate uh with PICORE uh if

**[28:13]** actually integrate uh with PICORE uh if

**[28:13]** actually integrate uh with PICORE uh if not sure if you're familiar with these,

**[28:14]** not sure if you're familiar with these,

**[28:14]** not sure if you're familiar with these, but basically in this in the sheets

**[28:16]** but basically in this in the sheets

**[28:16]** but basically in this in the sheets integration, what you're going to do in

**[28:18]** integration, what you're going to do in

**[28:18]** integration, what you're going to do in this workshop is you can actually just

**[28:21]** this workshop is you can actually just

**[28:21]** this workshop is you can actually just copy this wholesale and put it into a

**[28:23]** copy this wholesale and put it into a

**[28:23]** copy this wholesale and put it into a new spreadsheet with the examples that

**[28:25]** new spreadsheet with the examples that

**[28:25]** new spreadsheet with the examples that are here. What we're trying to do is

**[28:27]** are here. What we're trying to do is

**[28:27]** are here. What we're trying to do is just copy the criteria. So, you want to

**[28:28]** just copy the criteria. So, you want to

**[28:28]** just copy the criteria. So, you want to build a criteria. Here's a copy signal

**[28:32]** build a criteria. Here's a copy signal

**[28:32]** build a criteria. Here's a copy signal icon. Just click on the copy icon and

**[28:34]** icon. Just click on the copy icon and

**[28:34]** icon. Just click on the copy icon and then go to the spreadsheet that we will

**[28:37]** then go to the spreadsheet that we will

**[28:37]** then go to the spreadsheet that we will which which you have replace the

**[28:39]** which which you have replace the

**[28:39]** which which you have replace the criteria that exists there with this

**[28:41]** criteria that exists there with this

**[28:41]** criteria that exists there with this criteria that you've created and then

**[28:43]** criteria that you've created and then

**[28:43]** criteria that you've created and then under extensions these directions are

**[28:46]** under extensions these directions are

**[28:46]** under extensions these directions are all in the in the doc so you don't have

**[28:47]** all in the in the doc so you don't have

**[28:47]** all in the in the doc so you don't have to remember it but under extensions you

**[28:49]** to remember it but under extensions you

**[28:49]** to remember it but under extensions you can go and call the scorer the score is

**[28:51]** can go and call the scorer the score is

**[28:51]** can go and call the scorer the score is going to run across about 120 examples

**[28:54]** going to run across about 120 examples

**[28:54]** going to run across about 120 examples and then you'll see a confusion matrix

**[28:56]** and then you'll see a confusion matrix

**[28:56]** and then you'll see a confusion matrix which shows you how many times there's

**[28:58]** which shows you how many times there's

**[28:58]** which shows you how many times there's alignment on thumbs up how many times


### [29:00 - 30:00]

**[29:00]** alignment on thumbs up how many times

**[29:00]** alignment on thumbs up how many times there's alignment on thumbs down and how

**[29:02]** there's alignment on thumbs down and how

**[29:02]** there's alignment on thumbs down and how many times there's no alignment and then

**[29:03]** many times there's no alignment and then

**[29:03]** many times there's no alignment and then you can play around in the spreadsheet

**[29:05]** you can play around in the spreadsheet

**[29:05]** you can play around in the spreadsheet itself make changes to the dimensions

**[29:07]** itself make changes to the dimensions

**[29:07]** itself make changes to the dimensions and see if you can bring the alignment

**[29:08]** and see if you can bring the alignment

**[29:08]** and see if you can bring the alignment closer. So this gives you a sense of u

**[29:11]** closer. So this gives you a sense of u

**[29:11]** closer. So this gives you a sense of u yeah so this is the this is what a

**[29:12]** yeah so this is the this is what a

**[29:12]** yeah so this is the this is what a spreadsheet would look like. This is

**[29:13]** spreadsheet would look like. This is

**[29:13]** spreadsheet would look like. This is your criteria

**[29:15]** your criteria

**[29:15]** your criteria um which is basically just the English

**[29:18]** um which is basically just the English

**[29:18]** um which is basically just the English form uh the the spreadsheet form of the

**[29:20]** form uh the the spreadsheet form of the

**[29:20]** form uh the the spreadsheet form of the English that you saw.

**[29:22]** English that you saw.

**[29:22]** English that you saw. Oh sorry

**[29:29]** is that better? Okay. So like you can

**[29:29]** is that better? Okay. So like you can see this is the label the question these

**[29:31]** see this is the label the question these

**[29:31]** see this is the label the question these are the weights. In the case of Python

**[29:33]** are the weights. In the case of Python

**[29:33]** are the weights. In the case of Python there's Python code. So this is what

**[29:34]** there's Python code. So this is what

**[29:34]** there's Python code. So this is what your criteria sheet looks like right

**[29:36]** your criteria sheet looks like right

**[29:36]** your criteria sheet looks like right now. This is the default one that we put

**[29:37]** now. This is the default one that we put

**[29:37]** now. This is the default one that we put in there for you, but you would replace

**[29:39]** in there for you, but you would replace

**[29:39]** in there for you, but you would replace it with your own. This is the data. This

**[29:42]** it with your own. This is the data. This

**[29:42]** it with your own. This is the data. This this basically has actually feedback,

**[29:44]** this basically has actually feedback,

**[29:44]** this basically has actually feedback, which is a thumbs up, thumbs down, which

**[29:45]** which is a thumbs up, thumbs down, which

**[29:45]** which is a thumbs up, thumbs down, which we got from users. Um, some of this is

**[29:48]** we got from users. Um, some of this is

**[29:48]** we got from users. Um, some of this is fairly complex. Some of this is easy.

**[29:49]** fairly complex. Some of this is easy.

**[29:49]** fairly complex. Some of this is easy. So, it's all kinds of different sort of

**[29:50]** So, it's all kinds of different sort of

**[29:50]** So, it's all kinds of different sort of mix of things. And what you're going to

**[29:53]** mix of things. And what you're going to

**[29:53]** mix of things. And what you're going to do is you're going to select these two

**[29:54]** do is you're going to select these two

**[29:54]** do is you're going to select these two rows. This is the input, the output, and

**[29:56]** rows. This is the input, the output, and

**[29:56]** rows. This is the input, the output, and then in the extensions uh under here,

**[29:59]** then in the extensions uh under here,

**[29:59]** then in the extensions uh under here, you'll have score selected ranges, which


### [30:00 - 31:00]

**[30:01]** you'll have score selected ranges, which

**[30:01]** you'll have score selected ranges, which is going to create a score. And then you

**[30:03]** is going to create a score. And then you

**[30:03]** is going to create a score. And then you can look at the confusion matrix and see

**[30:04]** can look at the confusion matrix and see

**[30:04]** can look at the confusion matrix and see how it works. So that's sort of how

**[30:06]** how it works. So that's sort of how

**[30:06]** how it works. So that's sort of how that's one part of the exercise, but you

**[30:08]** that's one part of the exercise, but you

**[30:08]** that's one part of the exercise, but you can easily go and make changes here or

**[30:10]** can easily go and make changes here or

**[30:10]** can easily go and make changes here or even test out by making changes to the

**[30:12]** even test out by making changes to the

**[30:12]** even test out by making changes to the data, you know, messing up your like

**[30:15]** data, you know, messing up your like

**[30:15]** data, you know, messing up your like your JSON and seeing whether how that

**[30:17]** your JSON and seeing whether how that

**[30:17]** your JSON and seeing whether how that impacts things and so on and so forth.

**[30:19]** impacts things and so on and so forth.

**[30:19]** impacts things and so on and so forth. So that's that's the first phase of our

**[30:21]** So that's that's the first phase of our

**[30:21]** So that's that's the first phase of our co-pilot the of of our workshop and

**[30:24]** co-pilot the of of our workshop and

**[30:24]** co-pilot the of of our workshop and we'll talk about the second phase when

**[30:25]** we'll talk about the second phase when

**[30:25]** we'll talk about the second phase when we get started with that one. Go ahead.

**[30:27]** we get started with that one. Go ahead.

**[30:27]** we get started with that one. Go ahead. Yeah, I'm just curious how uh like best

**[30:29]** Yeah, I'm just curious how uh like best

**[30:29]** Yeah, I'm just curious how uh like best practices for using this in production

**[30:31]** practices for using this in production

**[30:31]** practices for using this in production when you have you know tens of thousands

**[30:33]** when you have you know tens of thousands

**[30:33]** when you have you know tens of thousands maybe hundreds of thousands of examples

**[30:35]** maybe hundreds of thousands of examples

**[30:35]** maybe hundreds of thousands of examples or do teams run this on a subset or just

**[30:38]** or do teams run this on a subset or just

**[30:38]** or do teams run this on a subset or just like how do you do this at scale right

**[30:41]** like how do you do this at scale right

**[30:41]** like how do you do this at scale right so that will we will hit a lot of that

**[30:43]** so that will we will hit a lot of that

**[30:43]** so that will we will hit a lot of that in the second part of our workshop we

**[30:45]** in the second part of our workshop we

**[30:45]** in the second part of our workshop we will directly go into Python collab code

**[30:48]** will directly go into Python collab code

**[30:48]** will directly go into Python collab code uh we have um the the SDK goes through a

**[30:51]** uh we have um the the SDK goes through a

**[30:51]** uh we have um the the SDK goes through a bunch of this um the details and best

**[30:55]** bunch of this um the details and best

**[30:55]** bunch of this um the details and best practices on how you do it But you will

**[30:57]** practices on how you do it But you will

**[30:57]** practices on how you do it But you will get to play with this uh in this

**[30:59]** get to play with this uh in this

**[30:59]** get to play with this uh in this workshop. You you can you will our our


### [31:00 - 32:00]

**[31:02]** workshop. You you can you will our our

**[31:02]** workshop. You you can you will our our our

**[31:03]** our

**[31:03]** our scorers are specifically designed for

**[31:05]** scorers are specifically designed for

**[31:05]** scorers are specifically designed for online workflows. These like 20

**[31:08]** online workflows. These like 20

**[31:08]** online workflows. These like 20 dimensions that you have, they score

**[31:09]** dimensions that you have, they score

**[31:09]** dimensions that you have, they score them all in sub 20 like 50 milliseconds.

**[31:13]** them all in sub 20 like 50 milliseconds.

**[31:13]** them all in sub 20 like 50 milliseconds. So you can run on a very large scale.

**[31:15]** So you can run on a very large scale.

**[31:15]** So you can run on a very large scale. You can run it online um fairly easily

**[31:18]** You can run it online um fairly easily

**[31:18]** You can run it online um fairly easily and we have batch processes and stuff

**[31:20]** and we have batch processes and stuff

**[31:20]** and we have batch processes and stuff like that set up for you. So you'll be

**[31:21]** like that set up for you. So you'll be

**[31:21]** like that set up for you. So you'll be able to play with that create sets. Um,

**[31:25]** able to play with that create sets. Um,

**[31:25]** able to play with that create sets. Um, typically you want to create eval sets

**[31:28]** typically you want to create eval sets

**[31:28]** typically you want to create eval sets which have a combination of hard, easy,

**[31:30]** which have a combination of hard, easy,

**[31:30]** which have a combination of hard, easy, medium, that kind of stuff. We're not

**[31:32]** medium, that kind of stuff. We're not

**[31:32]** medium, that kind of stuff. We're not going to get into data generation,

**[31:33]** going to get into data generation,

**[31:33]** going to get into data generation, synthetic data generation that much, but

**[31:35]** synthetic data generation that much, but

**[31:35]** synthetic data generation that much, but our uh you'll play with it in the

**[31:37]** our uh you'll play with it in the

**[31:37]** our uh you'll play with it in the co-pilot, but the actual data generation

**[31:39]** co-pilot, but the actual data generation

**[31:39]** co-pilot, but the actual data generation stuff there there's actually um

**[31:41]** stuff there there's actually um

**[31:41]** stuff there there's actually um documentation that we you can follow up

**[31:43]** documentation that we you can follow up

**[31:43]** documentation that we you can follow up afterwards and how to create like easy

**[31:45]** afterwards and how to create like easy

**[31:45]** afterwards and how to create like easy to set hard medium sets for your testing

**[31:47]** to set hard medium sets for your testing

**[31:47]** to set hard medium sets for your testing purposes. uh the best thing is to to

**[31:50]** purposes. uh the best thing is to to

**[31:50]** purposes. uh the best thing is to to sample from your logs some number of

**[31:54]** sample from your logs some number of

**[31:54]** sample from your logs some number of things and evaluate or just run it

**[31:56]** things and evaluate or just run it

**[31:56]** things and evaluate or just run it online. Majority of this these kinds of

**[31:58]** online. Majority of this these kinds of

**[31:58]** online. Majority of this these kinds of quality checks at Google were run online


### [32:00 - 33:00]

**[32:01]** quality checks at Google were run online

**[32:01]** quality checks at Google were run online whether it's spam detection, whether

**[32:02]** whether it's spam detection, whether

**[32:02]** whether it's spam detection, whether it's like you know what what decisions

**[32:04]** it's like you know what what decisions

**[32:04]** it's like you know what what decisions to make. That's the ideal place you want

**[32:06]** to make. That's the ideal place you want

**[32:06]** to make. That's the ideal place you want to be. Most people it's very difficult

**[32:08]** to be. Most people it's very difficult

**[32:08]** to be. Most people it's very difficult to kind of like sort of implement at

**[32:09]** to kind of like sort of implement at

**[32:09]** to kind of like sort of implement at that point. I think the challenge one of

**[32:11]** that point. I think the challenge one of

**[32:11]** that point. I think the challenge one of the biggest challenge with LLM as a

**[32:12]** the biggest challenge with LLM as a

**[32:12]** the biggest challenge with LLM as a judge is it's so expensive you can't run

**[32:14]** judge is it's so expensive you can't run

**[32:14]** judge is it's so expensive you can't run run online. So that's one of the things

**[32:16]** run online. So that's one of the things

**[32:16]** run online. So that's one of the things that this solves. Um

**[32:19]** that this solves. Um

**[32:19]** that this solves. Um all right so go ahead how this is

**[32:21]** all right so go ahead how this is

**[32:22]** all right so go ahead how this is different as a traditional models or

**[32:25]** different as a traditional models or

**[32:26]** different as a traditional models or smaller um so so we had a bunch of

**[32:29]** smaller um so so we had a bunch of

**[32:29]** smaller um so so we had a bunch of discussion on this maybe I'll go very

**[32:30]** discussion on this maybe I'll go very

**[32:30]** discussion on this maybe I'll go very quick quick quickly through these slides

**[32:33]** quick quick quickly through these slides

**[32:33]** quick quick quickly through these slides um so

**[32:36]** um so

**[32:36]** um so so the the these models are designed for

**[32:38]** so the the these models are designed for

**[32:38]** so the the these models are designed for high precision like for example if you

**[32:40]** high precision like for example if you

**[32:40]** high precision like for example if you run the same score twice on the same

**[32:42]** run the same score twice on the same

**[32:42]** run the same score twice on the same thing it's not going to give you

**[32:43]** thing it's not going to give you

**[32:43]** thing it's not going to give you different scores exactly the same score

**[32:44]** different scores exactly the same score

**[32:44]** different scores exactly the same score with small variations keep the same

**[32:46]** with small variations keep the same

**[32:46]** with small variations keep the same scores heights. It's high designed for

**[32:48]** scores heights. It's high designed for

**[32:48]** scores heights. It's high designed for like super high precision. It's just the

**[32:50]** like super high precision. It's just the

**[32:50]** like super high precision. It's just the architecture of these these models is is

**[32:54]** architecture of these these models is is

**[32:54]** architecture of these these models is is basically um very low variance. Um they

**[32:58]** basically um very low variance. Um they

**[32:58]** basically um very low variance. Um they the part of the reason is that they're


### [33:00 - 34:00]

**[33:00]** the part of the reason is that they're

**[33:00]** the part of the reason is that they're using this birectional attention instead

**[33:02]** using this birectional attention instead

**[33:02]** using this birectional attention instead of like the typical decoder models

**[33:04]** of like the typical decoder models

**[33:04]** of like the typical decoder models attention. They have a regression head

**[33:05]** attention. They have a regression head

**[33:06]** attention. They have a regression head on top instead of a token generation. So

**[33:08]** on top instead of a token generation. So

**[33:08]** on top instead of a token generation. So it's not auto reggressively generating

**[33:10]** it's not auto reggressively generating

**[33:10]** it's not auto reggressively generating tokens which has a lot of like weirdness

**[33:12]** tokens which has a lot of like weirdness

**[33:12]** tokens which has a lot of like weirdness that happens to it. Like there's a lot

**[33:13]** that happens to it. Like there's a lot

**[33:13]** that happens to it. Like there's a lot of post talk uh explanation for scores.

**[33:16]** of post talk uh explanation for scores.

**[33:16]** of post talk uh explanation for scores. will come up with the score then it'll

**[33:17]** will come up with the score then it'll

**[33:17]** will come up with the score then it'll try to justify the score that doesn't

**[33:19]** try to justify the score that doesn't

**[33:19]** try to justify the score that doesn't happen. The other thing is these models

**[33:20]** happen. The other thing is these models

**[33:20]** happen. The other thing is these models have been uh trained on um a lot of data

**[33:24]** have been uh trained on um a lot of data

**[33:24]** have been uh trained on um a lot of data like you know billions and billions of

**[33:26]** like you know billions and billions of

**[33:26]** like you know billions and billions of tokens which are only for scoring but

**[33:28]** tokens which are only for scoring but

**[33:28]** tokens which are only for scoring but different kinds of content so coding

**[33:30]** different kinds of content so coding

**[33:30]** different kinds of content so coding content other type of content. So these

**[33:32]** content other type of content. So these

**[33:32]** content other type of content. So these are these generalize really well across

**[33:34]** are these generalize really well across

**[33:34]** are these generalize really well across but that also stabilizes them quite a

**[33:35]** but that also stabilizes them quite a

**[33:36]** but that also stabilizes them quite a bit. Um the the one thing that I would

**[33:39]** bit. Um the the one thing that I would

**[33:39]** bit. Um the the one thing that I would say which is really nice is the

**[33:41]** say which is really nice is the

**[33:41]** say which is really nice is the interface is very nice. It basically

**[33:43]** interface is very nice. It basically

**[33:43]** interface is very nice. It basically just you ask a question and give it the

**[33:46]** just you ask a question and give it the

**[33:46]** just you ask a question and give it the the data and it will answer the question

**[33:48]** the data and it will answer the question

**[33:48]** the data and it will answer the question with a score and then you can inspect

**[33:50]** with a score and then you can inspect

**[33:50]** with a score and then you can inspect the score and understand why why it gave

**[33:52]** the score and understand why why it gave

**[33:52]** the score and understand why why it gave you that score. So it's a fairly simple

**[33:53]** you that score. So it's a fairly simple

**[33:53]** you that score. So it's a fairly simple interface. There's no like prompt tuning

**[33:55]** interface. There's no like prompt tuning

**[33:55]** interface. There's no like prompt tuning and so on and so forth because in this

**[33:57]** and so on and so forth because in this

**[33:57]** and so on and so forth because in this particular case when you're evaluating

**[33:59]** particular case when you're evaluating

**[33:59]** particular case when you're evaluating prompt tuning doesn't really like it's


### [34:00 - 35:00]

**[34:01]** prompt tuning doesn't really like it's

**[34:01]** prompt tuning doesn't really like it's not very natural like you know how do

**[34:02]** not very natural like you know how do

**[34:02]** not very natural like you know how do you explain a rubric to to a model. So

**[34:05]** you explain a rubric to to a model. So

**[34:05]** you explain a rubric to to a model. So these models understand internally why

**[34:07]** these models understand internally why

**[34:08]** these models understand internally why should this score high why shouldn't

**[34:09]** should this score high why shouldn't

**[34:09]** should this score high why shouldn't they score high and then these things

**[34:11]** they score high and then these things

**[34:11]** they score high and then these things come together uh using uh a fairly

**[34:14]** come together uh using uh a fairly

**[34:14]** come together uh using uh a fairly sophisticated model which is like a

**[34:17]** sophisticated model which is like a

**[34:17]** sophisticated model which is like a extension of generalized additive model

**[34:18]** extension of generalized additive model

**[34:18]** extension of generalized additive model which brings all of these different

**[34:19]** which brings all of these different

**[34:20]** which brings all of these different signals together um by baiting them

**[34:23]** signals together um by baiting them

**[34:23]** signals together um by baiting them based on your thumbs up thumbs down data

**[34:24]** based on your thumbs up thumbs down data

**[34:24]** based on your thumbs up thumbs down data so this is a process called calibration

**[34:27]** so this is a process called calibration

**[34:27]** so this is a process called calibration where you give it a bunch of data and it

**[34:28]** where you give it a bunch of data and it

**[34:28]** where you give it a bunch of data and it understands what's important what's not

**[34:30]** understands what's important what's not

**[34:30]** understands what's important what's not what should I some if something fails I

**[34:33]** what should I some if something fails I

**[34:33]** what should I some if something fails I should fail everything for example,

**[34:35]** should fail everything for example,

**[34:35]** should fail everything for example, spam, but if it succeeds, I shouldn't

**[34:37]** spam, but if it succeeds, I shouldn't

**[34:37]** spam, but if it succeeds, I shouldn't contribute those kinds of decisions. It

**[34:39]** contribute those kinds of decisions. It

**[34:39]** contribute those kinds of decisions. It makes those decisions for you based on

**[34:41]** makes those decisions for you based on

**[34:41]** makes those decisions for you based on the data. So that's sort of it's it's a

**[34:43]** the data. So that's sort of it's it's a

**[34:43]** the data. So that's sort of it's it's a much more advanced way of doing evalu

**[34:49]** much more advanced way of doing evalu

**[34:49]** much more advanced way of doing evalu purposes. It gives them that sort of

**[34:51]** purposes. It gives them that sort of

**[34:51]** purposes. It gives them that sort of stability that you desire and that and

**[34:52]** stability that you desire and that and

**[34:52]** stability that you desire and that and the reason they're very fast is because

**[34:54]** the reason they're very fast is because

**[34:54]** the reason they're very fast is because when you use birectional attention, you

**[34:56]** when you use birectional attention, you

**[34:56]** when you use birectional attention, you can build much more denser embeddings.

**[34:58]** can build much more denser embeddings.

**[34:58]** can build much more denser embeddings. So with fewer parameters, you can get


### [35:00 - 36:00]

**[35:01]** So with fewer parameters, you can get

**[35:01]** So with fewer parameters, you can get fairly high quality scores. Go ahead.

**[35:03]** fairly high quality scores. Go ahead.

**[35:03]** fairly high quality scores. Go ahead. Does it work well with other languages?

**[35:06]** Does it work well with other languages?

**[35:06]** Does it work well with other languages? Uh right now we have trained it with

**[35:09]** Uh right now we have trained it with

**[35:09]** Uh right now we have trained it with handful of languages. Uh we have we are

**[35:12]** handful of languages. Uh we have we are

**[35:12]** handful of languages. Uh we have we are pretty soon going to release a model um

**[35:15]** pretty soon going to release a model um

**[35:16]** pretty soon going to release a model um with multilang multilingual

**[35:17]** with multilang multilingual

**[35:17]** with multilang multilingual capabilities. We don't support

**[35:19]** capabilities. We don't support

**[35:19]** capabilities. We don't support multimodal yet but this is in our road

**[35:21]** multimodal yet but this is in our road

**[35:22]** multimodal yet but this is in our road map. Right. So right now it's English in

**[35:23]** map. Right. So right now it's English in

**[35:23]** map. Right. So right now it's English in a few languages and then we're going to

**[35:24]** a few languages and then we're going to

**[35:24]** a few languages and then we're going to expand it beyond that.

**[35:27]** expand it beyond that.

**[35:27]** expand it beyond that. Let's kick we should kick off the

**[35:28]** Let's kick we should kick off the

**[35:28]** Let's kick we should kick off the workshop and then we'll pass it on and

**[35:30]** workshop and then we'll pass it on and

**[35:30]** workshop and then we'll pass it on and we can just answer all the questions as

**[35:31]** we can just answer all the questions as

**[35:31]** we can just answer all the questions as well. Um, do you just want to share the

**[35:34]** well. Um, do you just want to share the

**[35:34]** well. Um, do you just want to share the doc? Just uh again reminder it's like

**[35:37]** doc? Just uh again reminder it's like

**[35:37]** doc? Just uh again reminder it's like with pi.aiworkshop.

**[35:40]** with pi.aiworkshop.

**[35:40]** with pi.aiworkshop. I'll just share the doc here as well so

**[35:41]** I'll just share the doc here as well so

**[35:41]** I'll just share the doc here as well so that you all can see it. Yeah, I'll also

**[35:43]** that you all can see it. Yeah, I'll also

**[35:43]** that you all can see it. Yeah, I'll also put it in the slack channel for

**[35:44]** put it in the slack channel for

**[35:44]** put it in the slack channel for everybody. Uh but

**[35:59]** Um sorry uh some people maybe have

**[35:59]** Um sorry uh some people maybe have already started working with the


### [36:00 - 37:00]

**[36:00]** already started working with the

**[36:00]** already started working with the collabs. have seen um but uh if I'll

**[36:03]** collabs. have seen um but uh if I'll

**[36:04]** collabs. have seen um but uh if I'll quickly show others uh what

**[36:08]** quickly show others uh what

**[36:08]** quickly show others uh what um what what the second phase of the

**[36:10]** um what what the second phase of the

**[36:10]** um what what the second phase of the exercise is about um but of course we

**[36:12]** exercise is about um but of course we

**[36:12]** exercise is about um but of course we can continue all of this going forward

**[36:15]** can continue all of this going forward

**[36:15]** can continue all of this going forward uh how do I project this

**[36:21]** um so this the second part of the

**[36:21]** um so this the second part of the exercise by the way we may not have

**[36:23]** exercise by the way we may not have

**[36:23]** exercise by the way we may not have enough time to wrap it all up here but

**[36:26]** enough time to wrap it all up here but

**[36:26]** enough time to wrap it all up here but the second part of the exercise feel

**[36:28]** the second part of the exercise feel

**[36:28]** the second part of the exercise feel free to do it on your own the collab is

**[36:30]** free to do it on your own the collab is

**[36:30]** free to do it on your own the collab is available for you. So you can you can

**[36:31]** available for you. So you can you can

**[36:32]** available for you. So you can you can you can use this um this collab um

**[36:36]** you can use this um this collab um

**[36:36]** you can use this um this collab um this this is the pre-prepared collab um

**[36:40]** this this is the pre-prepared collab um

**[36:40]** this this is the pre-prepared collab um and

**[36:41]** and

**[36:41]** and how do I

**[36:44]** how do I

**[36:44]** how do I I don't know if you can see this but

**[36:46]** I don't know if you can see this but

**[36:46]** I don't know if you can see this but basically this particular collab will

**[36:49]** basically this particular collab will

**[36:49]** basically this particular collab will take you through these multiple steps

**[36:50]** take you through these multiple steps

**[36:50]** take you through these multiple steps and a lot of people ask me questions

**[36:52]** and a lot of people ask me questions

**[36:52]** and a lot of people ask me questions about how to use it in code so I just

**[36:53]** about how to use it in code so I just

**[36:53]** about how to use it in code so I just wanted to quickly go over it. Um this is

**[36:56]** wanted to quickly go over it. Um this is

**[36:56]** wanted to quickly go over it. Um this is a basic installation. This is your

**[36:58]** a basic installation. This is your

**[36:58]** a basic installation. This is your scoring spec. This is this is where all

**[36:59]** scoring spec. This is this is where all

**[36:59]** scoring spec. This is this is where all of your intelligence going to live.


### [37:00 - 38:00]

**[37:01]** of your intelligence going to live.

**[37:01]** of your intelligence going to live. Again, this is a relatively simple

**[37:02]** Again, this is a relatively simple

**[37:02]** Again, this is a relatively simple example. So, it's a relatively simple

**[37:04]** example. So, it's a relatively simple

**[37:04]** example. So, it's a relatively simple scoring spec. But the way you get this

**[37:06]** scoring spec. But the way you get this

**[37:06]** scoring spec. But the way you get this spec is basically over here. You get

**[37:09]** spec is basically over here. You get

**[37:09]** spec is basically over here. You get into code, you copy it, and you put it

**[37:11]** into code, you copy it, and you put it

**[37:11]** into code, you copy it, and you put it into your collab. Right? So, this is

**[37:13]** into your collab. Right? So, this is

**[37:13]** into your collab. Right? So, this is basically how you get the spec here.

**[37:16]** basically how you get the spec here.

**[37:16]** basically how you get the spec here. It's all in natural language spec uh

**[37:18]** It's all in natural language spec uh

**[37:18]** It's all in natural language spec uh with some Python code in there. This is

**[37:21]** with some Python code in there. This is

**[37:21]** with some Python code in there. This is what you'll change. This is what you'll

**[37:23]** what you'll change. This is what you'll

**[37:23]** what you'll change. This is what you'll tweak. This is where everything is going

**[37:24]** tweak. This is where everything is going

**[37:24]** tweak. This is where everything is going to be. And what you're now doing in this

**[37:27]** to be. And what you're now doing in this

**[37:27]** to be. And what you're now doing in this particular collab which you can

**[37:29]** particular collab which you can

**[37:29]** particular collab which you can literally click through it and you don't

**[37:30]** literally click through it and you don't

**[37:30]** literally click through it and you don't have to do anything more than that but

**[37:33]** have to do anything more than that but

**[37:33]** have to do anything more than that but or you can play around with it a whole

**[37:34]** or you can play around with it a whole

**[37:34]** or you can play around with it a whole bunch is one is we have some data sets

**[37:37]** bunch is one is we have some data sets

**[37:37]** bunch is one is we have some data sets public public data sets on hugging face

**[37:40]** public public data sets on hugging face

**[37:40]** public public data sets on hugging face which has the thumbs up thumbs down

**[37:41]** which has the thumbs up thumbs down

**[37:41]** which has the thumbs up thumbs down data. This is the same data if you've

**[37:42]** data. This is the same data if you've

**[37:42]** data. This is the same data if you've seen the sheet that's the same data over

**[37:44]** seen the sheet that's the same data over

**[37:44]** seen the sheet that's the same data over here. you it you you you this collab is

**[37:48]** here. you it you you you this collab is

**[37:48]** here. you it you you you this collab is loading that data running the score on

**[37:50]** loading that data running the score on

**[37:50]** loading that data running the score on it returning your results um and then

**[37:54]** it returning your results um and then

**[37:54]** it returning your results um and then building a similar confusion matrix that

**[37:56]** building a similar confusion matrix that

**[37:56]** building a similar confusion matrix that you saw there which indicates how well

**[37:58]** you saw there which indicates how well

**[37:58]** you saw there which indicates how well well aligned your scores are so that


### [38:00 - 39:00]

**[38:00]** well aligned your scores are so that

**[38:00]** well aligned your scores are so that just getting you warmed up uh then you

**[38:02]** just getting you warmed up uh then you

**[38:02]** just getting you warmed up uh then you can use it to compare models this is

**[38:04]** can use it to compare models this is

**[38:04]** can use it to compare models this is where like really interesting stuff

**[38:06]** where like really interesting stuff

**[38:06]** where like really interesting stuff starts happening right so in this

**[38:07]** starts happening right so in this

**[38:07]** starts happening right so in this particular case we are comparing 1.5 and

**[38:10]** particular case we are comparing 1.5 and

**[38:10]** particular case we are comparing 1.5 and 2.5 models you can see that 2.5 has a

**[38:13]** 2.5 models you can see that 2.5 has a

**[38:13]** 2.5 models you can see that 2.5 has a slightly higher score than 1.5 5 for

**[38:15]** slightly higher score than 1.5 5 for

**[38:15]** slightly higher score than 1.5 5 for this particular task. But because 2.5

**[38:18]** this particular task. But because 2.5

**[38:18]** this particular task. But because 2.5 was mostly for reasoning, there's not

**[38:20]** was mostly for reasoning, there's not

**[38:20]** was mostly for reasoning, there's not that much of a delta here. If you go to

**[38:21]** that much of a delta here. If you go to

**[38:21]** that much of a delta here. If you go to smaller models uh like some of the the

**[38:24]** smaller models uh like some of the the

**[38:24]** smaller models uh like some of the the the the mini models like the cloud

**[38:26]** the the mini models like the cloud

**[38:26]** the the mini models like the cloud haiku, you could see you'll see a much

**[38:27]** haiku, you could see you'll see a much

**[38:27]** haiku, you could see you'll see a much bigger delta between the quality based

**[38:30]** bigger delta between the quality based

**[38:30]** bigger delta between the quality based on your own scoring system. So now you

**[38:32]** on your own scoring system. So now you

**[38:32]** on your own scoring system. So now you can eva use your scoring system for

**[38:33]** can eva use your scoring system for

**[38:33]** can eva use your scoring system for evaluating different models. What this

**[38:35]** evaluating different models. What this

**[38:35]** evaluating different models. What this is doing is it's taking about you know

**[38:38]** is doing is it's taking about you know

**[38:38]** is doing is it's taking about you know 10 examples

**[38:40]** 10 examples

**[38:40]** 10 examples calling these five different models

**[38:42]** calling these five different models

**[38:42]** calling these five different models generating responses and then scoring

**[38:44]** generating responses and then scoring

**[38:44]** generating responses and then scoring them using our scoring system. Right? So

**[38:46]** them using our scoring system. Right? So

**[38:46]** them using our scoring system. Right? So that's a model comparison. The other

**[38:48]** that's a model comparison. The other

**[38:48]** that's a model comparison. The other upset is to try different prompts. Um

**[38:52]** upset is to try different prompts. Um

**[38:52]** upset is to try different prompts. Um people change their system prompts but

**[38:53]** people change their system prompts but

**[38:54]** people change their system prompts but they're worried about them when they

**[38:55]** they're worried about them when they

**[38:55]** they're worried about them when they change it. What would happen? This is

**[38:58]** change it. What would happen? This is

**[38:58]** change it. What would happen? This is the right way to kind of make sure that

**[38:59]** the right way to kind of make sure that

**[38:59]** the right way to kind of make sure that you're not regressing. You have your


### [39:00 - 40:00]

**[39:01]** you're not regressing. You have your

**[39:01]** you're not regressing. You have your scoring spec. You try different system

**[39:03]** scoring spec. You try different system

**[39:04]** scoring spec. You try different system prompts. see if your scores are going

**[39:05]** prompts. see if your scores are going

**[39:05]** prompts. see if your scores are going down on your on your test set. So again,

**[39:08]** down on your on your test set. So again,

**[39:08]** down on your on your test set. So again, taking 10 examples just to demonstrate

**[39:10]** taking 10 examples just to demonstrate

**[39:10]** taking 10 examples just to demonstrate how you compare them. Uh here's like we

**[39:12]** how you compare them. Uh here's like we

**[39:12]** how you compare them. Uh here's like we we created a bad and a good prompt just

**[39:14]** we created a bad and a good prompt just

**[39:14]** we created a bad and a good prompt just to kind of accentuate this. So like bad

**[39:16]** to kind of accentuate this. So like bad

**[39:16]** to kind of accentuate this. So like bad prompts getting much lower score than

**[39:18]** prompts getting much lower score than

**[39:18]** prompts getting much lower score than good prompts on this particular task. Uh

**[39:21]** good prompts on this particular task. Uh

**[39:21]** good prompts on this particular task. Uh this is the one that I that I'm very

**[39:23]** this is the one that I that I'm very

**[39:23]** this is the one that I that I'm very excited about because it brings you into

**[39:24]** excited about because it brings you into

**[39:24]** excited about because it brings you into the online world and how to actually do

**[39:26]** the online world and how to actually do

**[39:26]** the online world and how to actually do this online where you're taking this one

**[39:28]** this online where you're taking this one

**[39:28]** this online where you're taking this one particular transcript and you are

**[39:31]** particular transcript and you are

**[39:31]** particular transcript and you are testing it out with different number of

**[39:33]** testing it out with different number of

**[39:33]** testing it out with different number of samples. So if you're if you use just

**[39:36]** samples. So if you're if you use just

**[39:36]** samples. So if you're if you use just one sample which is typically what you

**[39:38]** one sample which is typically what you

**[39:38]** one sample which is typically what you do generate one response with a

**[39:40]** do generate one response with a

**[39:40]** do generate one response with a temperature of.7 you get a particular

**[39:43]** temperature of.7 you get a particular

**[39:43]** temperature of.7 you get a particular score but as you up the the number of

**[39:46]** score but as you up the the number of

**[39:46]** score but as you up the the number of samples what it's doing behind the

**[39:47]** samples what it's doing behind the

**[39:47]** samples what it's doing behind the scenes is creating three or four four of

**[39:50]** scenes is creating three or four four of

**[39:50]** scenes is creating three or four four of those responses each one is a different

**[39:52]** those responses each one is a different

**[39:52]** those responses each one is a different response and then ranking them using our

**[39:55]** response and then ranking them using our

**[39:55]** response and then ranking them using our the pi scoring system that you just

**[39:56]** the pi scoring system that you just

**[39:56]** the pi scoring system that you just built and picking the one that's best.

**[39:59]** built and picking the one that's best.

**[39:59]** built and picking the one that's best. And what you would see is as you


### [40:00 - 41:00]

**[40:00]** And what you would see is as you

**[40:00]** And what you would see is as you increase the number of examples, you'll

**[40:02]** increase the number of examples, you'll

**[40:02]** increase the number of examples, you'll see the score steadily going up, the

**[40:04]** see the score steadily going up, the

**[40:04]** see the score steadily going up, the response quality going up. So this is uh

**[40:08]** response quality going up. So this is uh

**[40:08]** response quality going up. So this is uh literally like you can click through

**[40:09]** literally like you can click through

**[40:09]** literally like you can click through this in the collab and run through it

**[40:11]** this in the collab and run through it

**[40:11]** this in the collab and run through it and you don't won't need anything else.

**[40:13]** and you don't won't need anything else.

**[40:13]** and you don't won't need anything else. But there's a bunch of options for you

**[40:15]** But there's a bunch of options for you

**[40:15]** But there's a bunch of options for you to play around with this right now

**[40:17]** to play around with this right now

**[40:17]** to play around with this right now later. Just want to introduce this to

**[40:18]** later. Just want to introduce this to

**[40:18]** later. Just want to introduce this to you guys before um before you all

**[40:21]** you guys before um before you all

**[40:21]** you guys before um before you all disappear.


