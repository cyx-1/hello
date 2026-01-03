# Real-time Experiments with an AI Co-Scientist - Stefania Druga, fmr. Google Deepmind

**Video URL:** https://www.youtube.com/watch?v=wNH3q9pqn0U

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** My name is Stefania. I'm so glad you

**[00:17]** My name is Stefania. I'm so glad you made it until the yeah uh last day of

**[00:20]** made it until the yeah uh last day of

**[00:20]** made it until the yeah uh last day of the conference and came to the robotics

**[00:22]** the conference and came to the robotics

**[00:22]** the conference and came to the robotics track. So, we're going to start with a

**[00:24]** track. So, we're going to start with a

**[00:24]** track. So, we're going to start with a live demo uh and then we'll switch to

**[00:27]** live demo uh and then we'll switch to

**[00:27]** live demo uh and then we'll switch to the presentation just like to to kind of

**[00:29]** the presentation just like to to kind of

**[00:29]** the presentation just like to to kind of like swap things around. So, I'm going

**[00:32]** like swap things around. So, I'm going

**[00:32]** like swap things around. So, I'm going to try to connect the microscope over

**[00:34]** to try to connect the microscope over

**[00:34]** to try to connect the microscope over here. Uh and let's see the other camera

**[00:39]** here. Uh and let's see the other camera

**[00:39]** here. Uh and let's see the other camera and some sensors. So, my talk is about

**[00:42]** and some sensors. So, my talk is about

**[00:42]** and some sensors. So, my talk is about real time uh science co-scientist. So,

**[00:47]** real time uh science co-scientist. So,

**[00:47]** real time uh science co-scientist. So, think about pair programmers. How many

**[00:48]** think about pair programmers. How many

**[00:48]** think about pair programmers. How many of you use any form of copilot for

**[00:50]** of you use any form of copilot for

**[00:50]** of you use any form of copilot for coding? Right. So it's just like that

**[00:53]** coding? Right. So it's just like that

**[00:53]** coding? Right. So it's just like that but for doing things in the real world

**[00:55]** but for doing things in the real world

**[00:55]** but for doing things in the real world like science experiments. So you can see

**[00:59]** like science experiments. So you can see

**[00:59]** like science experiments. So you can see here now I have this board which is a


### [01:00 - 02:00]

**[01:02]** here now I have this board which is a

**[01:02]** here now I have this board which is a microbit board with jackd connected and

**[01:04]** microbit board with jackd connected and

**[01:04]** microbit board with jackd connected and it's measuring the temperature and I

**[01:06]** it's measuring the temperature and I

**[01:06]** it's measuring the temperature and I actually have a heat pad so I can

**[01:08]** actually have a heat pad so I can

**[01:08]** actually have a heat pad so I can increase the temperature and make it

**[01:10]** increase the temperature and make it

**[01:10]** increase the temperature and make it very very hot and hopefully it's not

**[01:11]** very very hot and hopefully it's not

**[01:11]** very very hot and hopefully it's not going to melt the board. Uh and then I

**[01:13]** going to melt the board. Uh and then I

**[01:13]** going to melt the board. Uh and then I can send that to my uh science

**[01:15]** can send that to my uh science

**[01:15]** can send that to my uh science assistant. It's going to analyze the

**[01:17]** assistant. It's going to analyze the

**[01:17]** assistant. It's going to analyze the data and kind of give me an answer in

**[01:19]** data and kind of give me an answer in

**[01:19]** data and kind of give me an answer in real time. So it's it's telling me like

**[01:22]** real time. So it's it's telling me like

**[01:22]** real time. So it's it's telling me like okay the ambient conditions indicate

**[01:24]** okay the ambient conditions indicate

**[01:24]** okay the ambient conditions indicate like stable dark quiet environments um

**[01:26]** like stable dark quiet environments um

**[01:26]** like stable dark quiet environments um because it has like it knows it can

**[01:28]** because it has like it knows it can

**[01:28]** because it has like it knows it can measure all these different sensors no

**[01:30]** measure all these different sensors no

**[01:30]** measure all these different sensors no buttons um but it sees that the

**[01:33]** buttons um but it sees that the

**[01:33]** buttons um but it sees that the temperature is 26 degrees and then I can

**[01:35]** temperature is 26 degrees and then I can

**[01:35]** temperature is 26 degrees and then I can actually give it more context I can go

**[01:36]** actually give it more context I can go

**[01:36]** actually give it more context I can go and create a protocol and say like this

**[01:39]** and create a protocol and say like this

**[01:39]** and create a protocol and say like this is the type of experiment that I want to

**[01:40]** is the type of experiment that I want to

**[01:40]** is the type of experiment that I want to do um so whenever you give me feedback

**[01:43]** do um so whenever you give me feedback

**[01:43]** do um so whenever you give me feedback about the data or the images that I'm

**[01:45]** about the data or the images that I'm

**[01:45]** about the data or the images that I'm sending from the microscope which I can

**[01:47]** sending from the microscope which I can

**[01:47]** sending from the microscope which I can also do um it's going to in the context

**[01:50]** also do um it's going to in the context

**[01:50]** also do um it's going to in the context of that experiment with those conditions

**[01:52]** of that experiment with those conditions

**[01:52]** of that experiment with those conditions and those constraints. And of course,

**[01:56]** and those constraints. And of course,

**[01:56]** and those constraints. And of course, like if you are actually doing that

**[01:58]** like if you are actually doing that

**[01:58]** like if you are actually doing that experiment several times, you can go

**[01:59]** experiment several times, you can go


### [02:00 - 03:00]

**[02:00]** experiment several times, you can go ahead and create a custom page for your

**[02:01]** ahead and create a custom page for your

**[02:02]** ahead and create a custom page for your experiment. Um, and it will monitor the

**[02:05]** experiment. Um, and it will monitor the

**[02:05]** experiment. Um, and it will monitor the data from the we're going to connect

**[02:08]** data from the we're going to connect

**[02:08]** data from the we're going to connect again the Jack DAC. Um, it's going to

**[02:11]** again the Jack DAC. Um, it's going to

**[02:11]** again the Jack DAC. Um, it's going to monitor and plot the data in real time.

**[02:13]** monitor and plot the data in real time.

**[02:14]** monitor and plot the data in real time. And the cool thing is also that if you

**[02:17]** And the cool thing is also that if you

**[02:17]** And the cool thing is also that if you want to leave your experiment running

**[02:19]** want to leave your experiment running

**[02:19]** want to leave your experiment running and go away, right? Like you could

**[02:20]** and go away, right? Like you could

**[02:20]** and go away, right? Like you could actually have cameras that are

**[02:23]** actually have cameras that are

**[02:23]** actually have cameras that are autonomous to go back to the previous

**[02:25]** autonomous to go back to the previous

**[02:25]** autonomous to go back to the previous talk. They're not fully autonomous, but

**[02:26]** talk. They're not fully autonomous, but

**[02:26]** talk. They're not fully autonomous, but they can track objects. So this camera

**[02:30]** they can track objects. So this camera

**[02:30]** they can track objects. So this camera is called REC camera. Also, by the way,

**[02:32]** is called REC camera. Also, by the way,

**[02:32]** is called REC camera. Also, by the way, all the hardware I'm showing you and all

**[02:33]** all the hardware I'm showing you and all

**[02:33]** all the hardware I'm showing you and all the components are open source. So,

**[02:36]** the components are open source. So,

**[02:36]** the components are open source. So, right now, uh, I'm going to set it to

**[02:39]** right now, uh, I'm going to set it to

**[02:39]** right now, uh, I'm going to set it to track me as a person

**[02:42]** track me as a person

**[02:42]** track me as a person and start the tracking.

**[02:45]** and start the tracking.

**[02:45]** and start the tracking. And it's running a model on the camera

**[02:48]** And it's running a model on the camera

**[02:48]** And it's running a model on the camera itself. So, it's going to start like

**[02:50]** itself. So, it's going to start like

**[02:50]** itself. So, it's going to start like moving around to see me and see where

**[02:52]** moving around to see me and see where

**[02:52]** moving around to see me and see where I'm going. Um, but you could train a

**[02:54]** I'm going. Um, but you could train a

**[02:54]** I'm going. Um, but you could train a custom model like to track like crystal

**[02:58]** custom model like to track like crystal

**[02:58]** custom model like to track like crystal growth or specific objects that you want


### [03:00 - 04:00]

**[03:00]** growth or specific objects that you want

**[03:00]** growth or specific objects that you want to monitor and in real time. And this

**[03:03]** to monitor and in real time. And this

**[03:03]** to monitor and in real time. And this runs on Wi-Fi, so it can be you can

**[03:05]** runs on Wi-Fi, so it can be you can

**[03:05]** runs on Wi-Fi, so it can be you can place it anywhere. Um, and then control

**[03:07]** place it anywhere. Um, and then control

**[03:08]** place it anywhere. Um, and then control like the the conditions in the

**[03:10]** like the the conditions in the

**[03:10]** like the the conditions in the experiments like increase the

**[03:11]** experiments like increase the

**[03:11]** experiments like increase the temperature or decrease the temperature.

**[03:13]** temperature or decrease the temperature.

**[03:13]** temperature or decrease the temperature. So, oh, it sees all of you. That's

**[03:15]** So, oh, it sees all of you. That's

**[03:15]** So, oh, it sees all of you. That's awesome.

**[03:17]** awesome.

**[03:17]** awesome. Um, so I'm going to stop this for now.

**[03:21]** Um, so I'm going to stop this for now.

**[03:21]** Um, so I'm going to stop this for now. So, that's like a short and here we're

**[03:23]** So, that's like a short and here we're

**[03:23]** So, that's like a short and here we're seeing like our temperature kind of

**[03:25]** seeing like our temperature kind of

**[03:25]** seeing like our temperature kind of increasing. I think my heat pad stopped.

**[03:27]** increasing. I think my heat pad stopped.

**[03:28]** increasing. I think my heat pad stopped. Um, but that's just like a a simple like

**[03:32]** Um, but that's just like a a simple like

**[03:32]** Um, but that's just like a a simple like demo uh of like without having a

**[03:35]** demo uh of like without having a

**[03:35]** demo uh of like without having a specific experiment in mind. And now I'm

**[03:37]** specific experiment in mind. And now I'm

**[03:38]** specific experiment in mind. And now I'm going to switch to oops uh my slides and

**[03:42]** going to switch to oops uh my slides and

**[03:42]** going to switch to oops uh my slides and actually show you what happens when you

**[03:44]** actually show you what happens when you

**[03:44]** actually show you what happens when you record much longer experiments and what

**[03:46]** record much longer experiments and what

**[03:46]** record much longer experiments and what it can do. Um why do we care about

**[03:50]** it can do. Um why do we care about

**[03:50]** it can do. Um why do we care about coscientist? We're not talking yet about

**[03:52]** coscientist? We're not talking yet about

**[03:52]** coscientist? We're not talking yet about real time uh co-scientist just co

**[03:54]** real time uh co-scientist just co

**[03:54]** real time uh co-scientist just co coscientist in general like why should

**[03:56]** coscientist in general like why should

**[03:56]** coscientist in general like why should you care about it we know that there's a

**[03:59]** you care about it we know that there's a

**[03:59]** you care about it we know that there's a a data overload in science and there's a


### [04:00 - 05:00]

**[04:01]** a data overload in science and there's a

**[04:01]** a data overload in science and there's a lot of complexity a lot of things to

**[04:03]** lot of complexity a lot of things to

**[04:03]** lot of complexity a lot of things to parse through and analyze and AI can

**[04:06]** parse through and analyze and AI can

**[04:06]** parse through and analyze and AI can really help with that um we also know

**[04:08]** really help with that um we also know

**[04:08]** really help with that um we also know that beyond the analysis of data fast at

**[04:11]** that beyond the analysis of data fast at

**[04:11]** that beyond the analysis of data fast at scale they can help with generating new

**[04:13]** scale they can help with generating new

**[04:14]** scale they can help with generating new hypothesis and maybe identifying blind

**[04:16]** hypothesis and maybe identifying blind

**[04:16]** hypothesis and maybe identifying blind spots in prior work and in your own

**[04:18]** spots in prior work and in your own

**[04:18]** spots in prior work and in your own thinking and We also know that it can

**[04:22]** thinking and We also know that it can

**[04:22]** thinking and We also know that it can they can speed things up, right? So

**[04:24]** they can speed things up, right? So

**[04:24]** they can speed things up, right? So instead of testing one hypothesis at a

**[04:26]** instead of testing one hypothesis at a

**[04:26]** instead of testing one hypothesis at a time, you could test a 100 hypothesis.

**[04:29]** time, you could test a 100 hypothesis.

**[04:29]** time, you could test a 100 hypothesis. So I got inspired to build this demo. Uh

**[04:31]** So I got inspired to build this demo. Uh

**[04:32]** So I got inspired to build this demo. Uh and by the way, the cost of all the

**[04:33]** and by the way, the cost of all the

**[04:33]** and by the way, the cost of all the parts uh is under $300 and it took me

**[04:38]** parts uh is under $300 and it took me

**[04:38]** parts uh is under $300 and it took me two weeks to build it and it's open

**[04:39]** two weeks to build it and it's open

**[04:39]** two weeks to build it and it's open source so you can play with it and hack

**[04:41]** source so you can play with it and hack

**[04:41]** source so you can play with it and hack it. Um so I got inspired to do this

**[04:45]** it. Um so I got inspired to do this

**[04:45]** it. Um so I got inspired to do this because of this demo from Deep Mind. So

**[04:49]** because of this demo from Deep Mind. So

**[04:49]** because of this demo from Deep Mind. So this paper got published uh two months

**[04:51]** this paper got published uh two months

**[04:51]** this paper got published uh two months ago on AI coscientist and it was

**[04:54]** ago on AI coscientist and it was

**[04:54]** ago on AI coscientist and it was actually showing um not in the real life

**[04:57]** actually showing um not in the real life

**[04:57]** actually showing um not in the real life but it was actually showing what happens

**[04:59]** but it was actually showing what happens

**[04:59]** but it was actually showing what happens when you're analyzing papers and data.


### [05:00 - 06:00]

**[05:01]** when you're analyzing papers and data.

**[05:01]** when you're analyzing papers and data. If you have a multitude of agents that

**[05:03]** If you have a multitude of agents that

**[05:03]** If you have a multitude of agents that can perform the different roles that we

**[05:05]** can perform the different roles that we

**[05:06]** can perform the different roles that we do as scientists what are the results.

**[05:09]** do as scientists what are the results.

**[05:09]** do as scientists what are the results. So what are the roles that we do as

**[05:11]** So what are the roles that we do as

**[05:11]** So what are the roles that we do as scientists? like we analyze papers, we

**[05:13]** scientists? like we analyze papers, we

**[05:13]** scientists? like we analyze papers, we summarize them, we look at data, we rank

**[05:17]** summarize them, we look at data, we rank

**[05:17]** summarize them, we look at data, we rank the options, we rank the different

**[05:19]** the options, we rank the different

**[05:19]** the options, we rank the different hypothesis. So they actually created uh

**[05:21]** hypothesis. So they actually created uh

**[05:21]** hypothesis. So they actually created uh an orchestration of different agents.

**[05:24]** an orchestration of different agents.

**[05:24]** an orchestration of different agents. Each of them was actually working on

**[05:25]** Each of them was actually working on

**[05:25]** Each of them was actually working on Gemini Gemini 2.0 Oh, and then uh with

**[05:29]** Gemini Gemini 2.0 Oh, and then uh with

**[05:29]** Gemini Gemini 2.0 Oh, and then uh with this orchestration of like ranking the

**[05:31]** this orchestration of like ranking the

**[05:32]** this orchestration of like ranking the different results, the different

**[05:33]** different results, the different

**[05:33]** different results, the different hypothesis, doing search online, doing

**[05:35]** hypothesis, doing search online, doing

**[05:35]** hypothesis, doing search online, doing search on papers, come up with a plan

**[05:38]** search on papers, come up with a plan

**[05:38]** search on papers, come up with a plan for the researcher to use.

**[05:41]** for the researcher to use.

**[05:42]** for the researcher to use. And not only that they did that, but

**[05:43]** And not only that they did that, but

**[05:43]** And not only that they did that, but they actually tested it against prior

**[05:46]** they actually tested it against prior

**[05:46]** they actually tested it against prior discoveries. And this was super

**[05:48]** discoveries. And this was super

**[05:48]** discoveries. And this was super interesting. So they tested it against

**[05:49]** interesting. So they tested it against

**[05:50]** interesting. So they tested it against prior discoveries on gene transfer

**[05:53]** prior discoveries on gene transfer

**[05:53]** prior discoveries on gene transfer mechanisms. So a discovery that took

**[05:56]** mechanisms. So a discovery that took

**[05:56]** mechanisms. So a discovery that took scientists 12 years. Uh it took the AI


### [06:00 - 07:00]

**[06:00]** scientists 12 years. Uh it took the AI

**[06:00]** scientists 12 years. Uh it took the AI scientist two days to come up with

**[06:02]** scientist two days to come up with

**[06:02]** scientist two days to come up with without having seen the data. So it it

**[06:04]** without having seen the data. So it it

**[06:04]** without having seen the data. So it it was not aware of how the gene transfer

**[06:06]** was not aware of how the gene transfer

**[06:06]** was not aware of how the gene transfer works. This was not part of the

**[06:07]** works. This was not part of the

**[06:07]** works. This was not part of the training. Um so and that was one

**[06:11]** training. Um so and that was one

**[06:11]** training. Um so and that was one verification by trying to replicate past

**[06:13]** verification by trying to replicate past

**[06:13]** verification by trying to replicate past results. But another one was like to

**[06:16]** results. But another one was like to

**[06:16]** results. But another one was like to come up with completely new hypothesis.

**[06:18]** come up with completely new hypothesis.

**[06:18]** come up with completely new hypothesis. So they used it for liver fibro fibrosis

**[06:22]** So they used it for liver fibro fibrosis

**[06:22]** So they used it for liver fibro fibrosis target treatment discovery and the AI

**[06:26]** target treatment discovery and the AI

**[06:26]** target treatment discovery and the AI coscientists came up with target uh uh

**[06:28]** coscientists came up with target uh uh

**[06:28]** coscientists came up with target uh uh drugs that were actually efficient in

**[06:31]** drugs that were actually efficient in

**[06:31]** drugs that were actually efficient in the lab in wet lab. They were tested by

**[06:33]** the lab in wet lab. They were tested by

**[06:33]** the lab in wet lab. They were tested by experts. So it's not a science fiction.

**[06:37]** experts. So it's not a science fiction.

**[06:37]** experts. So it's not a science fiction. It's not like something in the future.

**[06:39]** It's not like something in the future.

**[06:39]** It's not like something in the future. It's actually happening now. Um and for

**[06:42]** It's actually happening now. Um and for

**[06:42]** It's actually happening now. Um and for me what was inspiring about this is like

**[06:45]** me what was inspiring about this is like

**[06:45]** me what was inspiring about this is like when we can make real discoveries in

**[06:48]** when we can make real discoveries in

**[06:48]** when we can make real discoveries in drug drug discovery like um healthc care

**[06:51]** drug drug discovery like um healthc care

**[06:52]** drug drug discovery like um healthc care treatment bacterial resistance new type

**[06:54]** treatment bacterial resistance new type

**[06:54]** treatment bacterial resistance new type of materials I think that can be

**[06:57]** of materials I think that can be

**[06:58]** of materials I think that can be accelerated

**[06:59]** accelerated

**[06:59]** accelerated doing it uh in real time with the


### [07:00 - 08:00]

**[07:01]** doing it uh in real time with the

**[07:01]** doing it uh in real time with the scientist.

**[07:03]** scientist.

**[07:03]** scientist. This clicker doesn't work very well. So

**[07:04]** This clicker doesn't work very well. So

**[07:04]** This clicker doesn't work very well. So the vision was instead of just doing it

**[07:08]** the vision was instead of just doing it

**[07:08]** the vision was instead of just doing it like o on the data like not sync like

**[07:12]** like o on the data like not sync like

**[07:12]** like o on the data like not sync like async and giving the researchers a plan

**[07:15]** async and giving the researchers a plan

**[07:15]** async and giving the researchers a plan based on the data that exists. What if

**[07:18]** based on the data that exists. What if

**[07:18]** based on the data that exists. What if we do it in real time right and we

**[07:21]** we do it in real time right and we

**[07:21]** we do it in real time right and we formulate this hypothesis based on the

**[07:23]** formulate this hypothesis based on the

**[07:23]** formulate this hypothesis based on the empirical data we're observing in the

**[07:25]** empirical data we're observing in the

**[07:25]** empirical data we're observing in the lab in real time or it could be like

**[07:27]** lab in real time or it could be like

**[07:27]** lab in real time or it could be like when you're observing the robot like

**[07:29]** when you're observing the robot like

**[07:29]** when you're observing the robot like breaking down in real time. Right? So

**[07:32]** breaking down in real time. Right? So

**[07:32]** breaking down in real time. Right? So what motivated me was the results from

**[07:35]** what motivated me was the results from

**[07:35]** what motivated me was the results from the AI coscientist but also this vision

**[07:38]** the AI coscientist but also this vision

**[07:38]** the AI coscientist but also this vision from silver and sutton which is they

**[07:40]** from silver and sutton which is they

**[07:40]** from silver and sutton which is they they just published this paper welcome

**[07:42]** they just published this paper welcome

**[07:42]** they just published this paper welcome to the era of experience which is

**[07:44]** to the era of experience which is

**[07:44]** to the era of experience which is fantastic it's very short if you haven't

**[07:45]** fantastic it's very short if you haven't

**[07:45]** fantastic it's very short if you haven't read it I highly recommend it and they

**[07:49]** read it I highly recommend it and they

**[07:49]** read it I highly recommend it and they really talk about how we're going past

**[07:51]** really talk about how we're going past

**[07:51]** really talk about how we're going past the era of human data where we're only

**[07:54]** the era of human data where we're only

**[07:54]** the era of human data where we're only indexing and making predictions but uh

**[07:57]** indexing and making predictions but uh

**[07:57]** indexing and making predictions but uh based on the data sets that we created


### [08:00 - 09:00]

**[08:00]** based on the data sets that we created

**[08:00]** based on the data sets that we created and go into an era where the AI learns

**[08:02]** and go into an era where the AI learns

**[08:02]** and go into an era where the AI learns from the continuous environment in which

**[08:05]** from the continuous environment in which

**[08:05]** from the continuous environment in which we operate, right? And especially with

**[08:07]** we operate, right? And especially with

**[08:07]** we operate, right? And especially with multimodel when we have real time data

**[08:10]** multimodel when we have real time data

**[08:10]** multimodel when we have real time data from images, from sensors, from audio

**[08:14]** from images, from sensors, from audio

**[08:14]** from images, from sensors, from audio streams like that is possible.

**[08:17]** streams like that is possible.

**[08:17]** streams like that is possible. So I hope I convince you by now that

**[08:19]** So I hope I convince you by now that

**[08:19]** So I hope I convince you by now that real time matters. And I wanted to show

**[08:22]** real time matters. And I wanted to show

**[08:22]** real time matters. And I wanted to show you like how I use my system with longer

**[08:25]** you like how I use my system with longer

**[08:25]** you like how I use my system with longer experiments. So, um, you already saw

**[08:28]** experiments. So, um, you already saw

**[08:28]** experiments. So, um, you already saw like the the chat image and I had to

**[08:31]** like the the chat image and I had to

**[08:31]** like the the chat image and I had to find experiments that I could actually

**[08:33]** find experiments that I could actually

**[08:33]** find experiments that I could actually do at home. So, this is the overview of

**[08:37]** do at home. So, this is the overview of

**[08:37]** do at home. So, this is the overview of the of the system. So, it's it's a very

**[08:40]** the of the system. So, it's it's a very

**[08:40]** the of the system. So, it's it's a very simple React app and it's has like all

**[08:43]** simple React app and it's has like all

**[08:43]** simple React app and it's has like all the input sources that you've seen live

**[08:45]** the input sources that you've seen live

**[08:45]** the input sources that you've seen live in action like the Jack DAC sensors via

**[08:47]** in action like the Jack DAC sensors via

**[08:48]** in action like the Jack DAC sensors via USB, different webcams. You can add as

**[08:50]** USB, different webcams. You can add as

**[08:50]** USB, different webcams. You can add as many webcams as you want. Text input. It

**[08:53]** many webcams as you want. Text input. It

**[08:53]** many webcams as you want. Text input. It actually works with voice. I forgot to

**[08:54]** actually works with voice. I forgot to

**[08:54]** actually works with voice. I forgot to show that. you can talk to it and it

**[08:56]** show that. you can talk to it and it

**[08:56]** show that. you can talk to it and it talks back. Um, and then uh all of these


### [09:00 - 10:00]

**[09:00]** talks back. Um, and then uh all of these

**[09:00]** talks back. Um, and then uh all of these like inputs become web hooks and I can

**[09:03]** like inputs become web hooks and I can

**[09:03]** like inputs become web hooks and I can I'm going to go into more detail how I

**[09:05]** I'm going to go into more detail how I

**[09:05]** I'm going to go into more detail how I optimized each and one of them and that

**[09:08]** optimized each and one of them and that

**[09:08]** optimized each and one of them and that gets sent to a back end which

**[09:09]** gets sent to a back end which

**[09:09]** gets sent to a back end which communicates with the real API. I use

**[09:11]** communicates with the real API. I use

**[09:11]** communicates with the real API. I use the Gemini in this case and

**[09:15]** the Gemini in this case and

**[09:16]** the Gemini in this case and I had to uh this is the information

**[09:18]** I had to uh this is the information

**[09:18]** I had to uh this is the information flow. So um you have the physical

**[09:21]** flow. So um you have the physical

**[09:21]** flow. So um you have the physical sensors and for the jackd I'm actually

**[09:23]** sensors and for the jackd I'm actually

**[09:23]** sensors and for the jackd I'm actually using the web USB API um that goes to

**[09:26]** using the web USB API um that goes to

**[09:26]** using the web USB API um that goes to the fronted hooks which gets pulled by

**[09:29]** the fronted hooks which gets pulled by

**[09:29]** the fronted hooks which gets pulled by the context assembly and the context

**[09:31]** the context assembly and the context

**[09:31]** the context assembly and the context assembly actually is always checking

**[09:33]** assembly actually is always checking

**[09:33]** assembly actually is always checking what sort of modalities are present. Do

**[09:35]** what sort of modalities are present. Do

**[09:35]** what sort of modalities are present. Do we have text? Do we have voice? Do we

**[09:37]** we have text? Do we have voice? Do we

**[09:37]** we have text? Do we have voice? Do we have image? Do we have a chat history?

**[09:39]** have image? Do we have a chat history?

**[09:39]** have image? Do we have a chat history? And depending on what modality

**[09:41]** And depending on what modality

**[09:41]** And depending on what modality modalities are present, every single

**[09:44]** modalities are present, every single

**[09:44]** modalities are present, every single time uh I'm sending a message, it builds

**[09:47]** time uh I'm sending a message, it builds

**[09:47]** time uh I'm sending a message, it builds this context that gets sent to the API

**[09:50]** this context that gets sent to the API

**[09:50]** this context that gets sent to the API that gives me back a response. And uh

**[09:54]** that gives me back a response. And uh

**[09:54]** that gives me back a response. And uh this is how the unifi context assembly

**[09:56]** this is how the unifi context assembly

**[09:56]** this is how the unifi context assembly works. So I guess like the the very

**[09:59]** works. So I guess like the the very


### [10:00 - 11:00]

**[10:00]** works. So I guess like the the very important piece here is how you're doing

**[10:03]** important piece here is how you're doing

**[10:03]** important piece here is how you're doing this con uh context injection depending

**[10:06]** this con uh context injection depending

**[10:06]** this con uh context injection depending on what sensors you have connected and

**[10:08]** on what sensors you have connected and

**[10:08]** on what sensors you have connected and the type of experiment you're defining

**[10:11]** the type of experiment you're defining

**[10:11]** the type of experiment you're defining and making this dynamic on the fly like

**[10:13]** and making this dynamic on the fly like

**[10:14]** and making this dynamic on the fly like when you create the protocols

**[10:17]** when you create the protocols

**[10:17]** when you create the protocols and

**[10:19]** and

**[10:19]** and that was the the ingredients for the

**[10:21]** that was the the ingredients for the

**[10:21]** that was the the ingredients for the code. Let's now let's talk about the

**[10:23]** code. Let's now let's talk about the

**[10:23]** code. Let's now let's talk about the ingredients for the hardware. So when I

**[10:26]** ingredients for the hardware. So when I

**[10:26]** ingredients for the hardware. So when I start doing the the experiments, I had

**[10:28]** start doing the the experiments, I had

**[10:28]** start doing the the experiments, I had to list and put out all the parts that I

**[10:31]** to list and put out all the parts that I

**[10:31]** to list and put out all the parts that I had at my my disposal. Kind of like

**[10:32]** had at my my disposal. Kind of like

**[10:32]** had at my my disposal. Kind of like cooking, right? So it's like what can I

**[10:34]** cooking, right? So it's like what can I

**[10:34]** cooking, right? So it's like what can I make with all these sensors? Like these

**[10:37]** make with all these sensors? Like these

**[10:37]** make with all these sensors? Like these are my inputs. These are my outputs. Uh

**[10:39]** are my inputs. These are my outputs. Uh

**[10:39]** are my inputs. These are my outputs. Uh these are my all my cameras and all my

**[10:41]** these are my all my cameras and all my

**[10:42]** these are my all my cameras and all my cables like and how many boards I have.

**[10:44]** cables like and how many boards I have.

**[10:44]** cables like and how many boards I have. What sort of experiments could I create

**[10:45]** What sort of experiments could I create

**[10:45]** What sort of experiments could I create with that? And

**[10:48]** with that? And

**[10:48]** with that? And I also had the constraint of doing

**[10:51]** I also had the constraint of doing

**[10:51]** I also had the constraint of doing experiments that I can measure in real

**[10:53]** experiments that I can measure in real

**[10:53]** experiments that I can measure in real time for this talk. and also that are

**[10:55]** time for this talk. and also that are

**[10:55]** time for this talk. and also that are safe for me to do at home and I can

**[10:57]** safe for me to do at home and I can

**[10:57]** safe for me to do at home and I can travel with, right? So that really

**[10:59]** travel with, right? So that really

**[10:59]** travel with, right? So that really narrowed down the list of things that I


### [11:00 - 12:00]

**[11:01]** narrowed down the list of things that I

**[11:01]** narrowed down the list of things that I could play with. So one thing that I did

**[11:03]** could play with. So one thing that I did

**[11:03]** could play with. So one thing that I did was exploring crystallization. So you

**[11:06]** was exploring crystallization. So you

**[11:06]** was exploring crystallization. So you can see there like the crystals that I

**[11:08]** can see there like the crystals that I

**[11:08]** can see there like the crystals that I was growing and that took longer and I I

**[11:10]** was growing and that took longer and I I

**[11:10]** was growing and that took longer and I I recorded the whole thing and

**[11:11]** recorded the whole thing and

**[11:11]** recorded the whole thing and fermentation.

**[11:13]** fermentation.

**[11:13]** fermentation. And let's dive into each and one of

**[11:15]** And let's dive into each and one of

**[11:15]** And let's dive into each and one of those. So this was my lab in a box in

**[11:17]** those. So this was my lab in a box in

**[11:17]** those. So this was my lab in a box in our apartment in Tokyo. Um the people

**[11:20]** our apartment in Tokyo. Um the people

**[11:20]** our apartment in Tokyo. Um the people coming to the house were very confused

**[11:22]** coming to the house were very confused

**[11:22]** coming to the house were very confused every day.

**[11:25]** every day.

**[11:25]** every day. Um there was something no explosions

**[11:27]** Um there was something no explosions

**[11:27]** Um there was something no explosions though so that was good. Uh so for for

**[11:31]** though so that was good. Uh so for for

**[11:31]** though so that was good. Uh so for for crystal growth how many of you re

**[11:33]** crystal growth how many of you re

**[11:33]** crystal growth how many of you re remember this from chemistry. Okay. Okay

**[11:36]** remember this from chemistry. Okay. Okay

**[11:36]** remember this from chemistry. Okay. Okay that's awesome. So I don't need to go

**[11:38]** that's awesome. So I don't need to go

**[11:38]** that's awesome. So I don't need to go into great detail but basically the the

**[11:40]** into great detail but basically the the

**[11:40]** into great detail but basically the the principle is quite simple like you

**[11:42]** principle is quite simple like you

**[11:42]** principle is quite simple like you oversaturate the solution by adding salt

**[11:45]** oversaturate the solution by adding salt

**[11:45]** oversaturate the solution by adding salt in hot water and then you're like slowly

**[11:48]** in hot water and then you're like slowly

**[11:48]** in hot water and then you're like slowly cooling it off and that creates this

**[11:51]** cooling it off and that creates this

**[11:51]** cooling it off and that creates this process this uh nucleation and the

**[11:54]** process this uh nucleation and the

**[11:54]** process this uh nucleation and the growth of crystals. Now the trick in

**[11:56]** growth of crystals. Now the trick in

**[11:56]** growth of crystals. Now the trick in having beautiful crystals is how you do

**[11:59]** having beautiful crystals is how you do

**[11:59]** having beautiful crystals is how you do the cooling off right it needs to be


### [12:00 - 13:00]

**[12:01]** the cooling off right it needs to be

**[12:01]** the cooling off right it needs to be gradual. you need to not move like the

**[12:04]** gradual. you need to not move like the

**[12:04]** gradual. you need to not move like the um the liquid or the object. So the

**[12:07]** um the liquid or the object. So the

**[12:08]** um the liquid or the object. So the gradual cooling and the level of

**[12:09]** gradual cooling and the level of

**[12:09]** gradual cooling and the level of humidity is what gives you beautiful

**[12:12]** humidity is what gives you beautiful

**[12:12]** humidity is what gives you beautiful crystal formation. So the main things we

**[12:16]** crystal formation. So the main things we

**[12:16]** crystal formation. So the main things we want to measure in this example is what

**[12:19]** want to measure in this example is what

**[12:19]** want to measure in this example is what are our curves for how fast the salt

**[12:23]** are our curves for how fast the salt

**[12:23]** are our curves for how fast the salt dissolves like where are the places

**[12:25]** dissolves like where are the places

**[12:25]** dissolves like where are the places where the crystals are being formed?

**[12:27]** where the crystals are being formed?

**[12:27]** where the crystals are being formed? Those are called nucleation sites.

**[12:29]** Those are called nucleation sites.

**[12:29]** Those are called nucleation sites. What's the growth rate of the crystals?

**[12:31]** What's the growth rate of the crystals?

**[12:31]** What's the growth rate of the crystals? And um that is affected by temperature

**[12:34]** And um that is affected by temperature

**[12:34]** And um that is affected by temperature concentration.

**[12:35]** concentration.

**[12:35]** concentration. And oh yeah, I forgot to play this. This

**[12:38]** And oh yeah, I forgot to play this. This

**[12:38]** And oh yeah, I forgot to play this. This was like a sped up. So the this was a

**[12:41]** was like a sped up. So the this was a

**[12:41]** was like a sped up. So the this was a recording from the microscope. It's

**[12:44]** recording from the microscope. It's

**[12:44]** recording from the microscope. It's moving because it actually has a fan uh

**[12:47]** moving because it actually has a fan uh

**[12:47]** moving because it actually has a fan uh uh uh blowing cool air from ice. So

**[12:51]** uh uh blowing cool air from ice. So

**[12:51]** uh uh blowing cool air from ice. So that's why like the camera is moving.

**[12:52]** that's why like the camera is moving.

**[12:52]** that's why like the camera is moving. That was how I was like cooling it off.

**[12:54]** That was how I was like cooling it off.

**[12:54]** That was how I was like cooling it off. But you can see the data in the sensors

**[12:56]** But you can see the data in the sensors

**[12:56]** But you can see the data in the sensors changing on the side. And this is like

**[12:58]** changing on the side. And this is like

**[12:58]** changing on the side. And this is like being recorded for an extended period of


### [13:00 - 14:00]

**[13:00]** being recorded for an extended period of

**[13:00]** being recorded for an extended period of time. And then I get a CSV from the the

**[13:03]** time. And then I get a CSV from the the

**[13:03]** time. And then I get a CSV from the the sensor values and I can go and analyze

**[13:05]** sensor values and I can go and analyze

**[13:05]** sensor values and I can go and analyze that um and kind of get a sense for like

**[13:09]** that um and kind of get a sense for like

**[13:09]** that um and kind of get a sense for like what happened. Was I cooling it off too

**[13:11]** what happened. Was I cooling it off too

**[13:11]** what happened. Was I cooling it off too fast or too low too u slow? Um were my

**[13:16]** fast or too low too u slow? Um were my

**[13:16]** fast or too low too u slow? Um were my crystal like growing or not? And then I

**[13:18]** crystal like growing or not? And then I

**[13:18]** crystal like growing or not? And then I also played with different samples. So I

**[13:20]** also played with different samples. So I

**[13:20]** also played with different samples. So I had samples that I would put in the

**[13:23]** had samples that I would put in the

**[13:23]** had samples that I would put in the fridge and in the room and like at

**[13:24]** fridge and in the room and like at

**[13:24]** fridge and in the room and like at different temperatures so I could also

**[13:26]** different temperatures so I could also

**[13:26]** different temperatures so I could also measure and have like control groups for

**[13:28]** measure and have like control groups for

**[13:28]** measure and have like control groups for that. And then once I have that CSV

**[13:32]** that. And then once I have that CSV

**[13:32]** that. And then once I have that CSV data, I can plot it, right? So I can

**[13:34]** data, I can plot it, right? So I can

**[13:34]** data, I can plot it, right? So I can actually see what was my crystal growth

**[13:36]** actually see what was my crystal growth

**[13:36]** actually see what was my crystal growth rate um and if my temperature was like

**[13:40]** rate um and if my temperature was like

**[13:40]** rate um and if my temperature was like the best and I can plot that for the

**[13:42]** the best and I can plot that for the

**[13:42]** the best and I can plot that for the different samples. And right now I don't

**[13:45]** different samples. And right now I don't

**[13:45]** different samples. And right now I don't have that integrated live on the

**[13:47]** have that integrated live on the

**[13:47]** have that integrated live on the platform but that's coming. Um so I had

**[13:50]** platform but that's coming. Um so I had

**[13:50]** platform but that's coming. Um so I had to write a separate script to get the

**[13:51]** to write a separate script to get the

**[13:51]** to write a separate script to get the CSV data and create this visualizations.

**[13:55]** CSV data and create this visualizations.

**[13:55]** CSV data and create this visualizations. Um and the insight I got from this is

**[13:58]** Um and the insight I got from this is

**[13:58]** Um and the insight I got from this is that the crystal formation is actually


### [14:00 - 15:00]

**[14:00]** that the crystal formation is actually

**[14:00]** that the crystal formation is actually uh not gradual that it happens in

**[14:02]** uh not gradual that it happens in

**[14:02]** uh not gradual that it happens in bursts. Um so that that was something

**[14:05]** bursts. Um so that that was something

**[14:05]** bursts. Um so that that was something that surprised me when I looked at the

**[14:06]** that surprised me when I looked at the

**[14:06]** that surprised me when I looked at the data. So once the critical saturation is

**[14:09]** data. So once the critical saturation is

**[14:09]** data. So once the critical saturation is reached there's like sudden crystal

**[14:10]** reached there's like sudden crystal

**[14:10]** reached there's like sudden crystal growth formation. So it's not like

**[14:12]** growth formation. So it's not like

**[14:12]** growth formation. So it's not like something that it's kind of like slowly

**[14:13]** something that it's kind of like slowly

**[14:13]** something that it's kind of like slowly growing but uh it grows in bursts. Uh,

**[14:17]** growing but uh it grows in bursts. Uh,

**[14:17]** growing but uh it grows in bursts. Uh, and here's like 40 minutes recording of

**[14:20]** and here's like 40 minutes recording of

**[14:20]** and here's like 40 minutes recording of the crystal growth like super sped up.

**[14:23]** the crystal growth like super sped up.

**[14:23]** the crystal growth like super sped up. So, you can kind of see how the humidity

**[14:25]** So, you can kind of see how the humidity

**[14:25]** So, you can kind of see how the humidity and the temperature was changing.

**[14:28]** and the temperature was changing.

**[14:28]** and the temperature was changing. And

**[14:29]** And

**[14:30]** And the the next one was am I doing on time

**[14:32]** the the next one was am I doing on time

**[14:32]** the the next one was am I doing on time because I have a lot of things. Okay.

**[14:34]** because I have a lot of things. Okay.

**[14:34]** because I have a lot of things. Okay. Uh, I might skip over fermentation just

**[14:36]** Uh, I might skip over fermentation just

**[14:36]** Uh, I might skip over fermentation just in interest of time. But um I'm sure all

**[14:40]** in interest of time. But um I'm sure all

**[14:40]** in interest of time. But um I'm sure all of you have dealt with fermentation in

**[14:42]** of you have dealt with fermentation in

**[14:42]** of you have dealt with fermentation in some shape or form even if it was liquid

**[14:44]** some shape or form even if it was liquid

**[14:44]** some shape or form even if it was liquid having to benefit the the out uh the end

**[14:49]** having to benefit the the out uh the end

**[14:49]** having to benefit the the out uh the end result. Um, but the the insight here is

**[14:52]** result. Um, but the the insight here is

**[14:52]** result. Um, but the the insight here is to actually control how much salt and

**[14:54]** to actually control how much salt and

**[14:54]** to actually control how much salt and sugar we put into the different uh dough

**[14:57]** sugar we put into the different uh dough

**[14:57]** sugar we put into the different uh dough and then measure and and then also

**[14:59]** and then measure and and then also

**[14:59]** and then measure and and then also change the temperature and measure the


### [15:00 - 16:00]

**[15:02]** change the temperature and measure the

**[15:02]** change the temperature and measure the growth rate uh and the CO2 and uh that

**[15:06]** growth rate uh and the CO2 and uh that

**[15:06]** growth rate uh and the CO2 and uh that was the fermentation and I also have

**[15:09]** was the fermentation and I also have

**[15:09]** was the fermentation and I also have like a sped up recording of the data

**[15:12]** like a sped up recording of the data

**[15:12]** like a sped up recording of the data collection

**[15:14]** collection

**[15:14]** collection and uh I already showed you the re

**[15:16]** and uh I already showed you the re

**[15:16]** and uh I already showed you the re camera and the fact that it's mobile and

**[15:19]** camera and the fact that it's mobile and

**[15:19]** camera and the fact that it's mobile and it and track objects. Um, this is the

**[15:21]** it and track objects. Um, this is the

**[15:21]** it and track objects. Um, this is the education version. If you want to play

**[15:23]** education version. If you want to play

**[15:23]** education version. If you want to play with some of these things and just kind

**[15:25]** with some of these things and just kind

**[15:25]** with some of these things and just kind of do your own experiments. Uh, please

**[15:28]** of do your own experiments. Uh, please

**[15:28]** of do your own experiments. Uh, please like the lab mine that I showed you is

**[15:30]** like the lab mine that I showed you is

**[15:30]** like the lab mine that I showed you is not deployed yet, but it will be and the

**[15:32]** not deployed yet, but it will be and the

**[15:32]** not deployed yet, but it will be and the code will be open source. But this you

**[15:34]** code will be open source. But this you

**[15:34]** code will be open source. But this you can play with. You need to put your own

**[15:35]** can play with. You need to put your own

**[15:35]** can play with. You need to put your own API,

**[15:37]** API,

**[15:37]** API, but it runs on the phone and you can

**[15:40]** but it runs on the phone and you can

**[15:40]** but it runs on the phone and you can test the camera for now. Uh, and if you

**[15:42]** test the camera for now. Uh, and if you

**[15:42]** test the camera for now. Uh, and if you have a microbit or you want to connect

**[15:43]** have a microbit or you want to connect

**[15:43]** have a microbit or you want to connect mine, um, you're welcome to to try it

**[15:47]** mine, um, you're welcome to to try it

**[15:47]** mine, um, you're welcome to to try it and let me know if the QR doesn't work.

**[15:49]** and let me know if the QR doesn't work.

**[15:49]** and let me know if the QR doesn't work. And

**[15:51]** And

**[15:51]** And yeah, this this is a version kind of

**[15:53]** yeah, this this is a version kind of

**[15:53]** yeah, this this is a version kind of like for to teach it to kids. Um, and I

**[15:57]** like for to teach it to kids. Um, and I

**[15:57]** like for to teach it to kids. Um, and I wanted to end by talking a little bit

**[15:59]** wanted to end by talking a little bit

**[15:59]** wanted to end by talking a little bit about the open-source ecosystem that can


### [16:00 - 17:00]

**[16:01]** about the open-source ecosystem that can

**[16:01]** about the open-source ecosystem that can support this type of initiative to go

**[16:03]** support this type of initiative to go

**[16:03]** support this type of initiative to go beyond the demo and kind of like a cool

**[16:05]** beyond the demo and kind of like a cool

**[16:06]** beyond the demo and kind of like a cool experimentation to a real uh real

**[16:09]** experimentation to a real uh real

**[16:09]** experimentation to a real uh real solution in uh for scientists and

**[16:11]** solution in uh for scientists and

**[16:11]** solution in uh for scientists and builders. So there's an entire

**[16:14]** builders. So there's an entire

**[16:14]** builders. So there's an entire opensource ecosystem for recreating all

**[16:17]** opensource ecosystem for recreating all

**[16:17]** opensource ecosystem for recreating all the lab equipment but then also for

**[16:19]** the lab equipment but then also for

**[16:19]** the lab equipment but then also for creating machines that can support the

**[16:21]** creating machines that can support the

**[16:21]** creating machines that can support the automation of pipetting and like doing

**[16:24]** automation of pipetting and like doing

**[16:24]** automation of pipetting and like doing all the um analysis that you need to do

**[16:28]** all the um analysis that you need to do

**[16:28]** all the um analysis that you need to do in a lab and all the manipulation that

**[16:30]** in a lab and all the manipulation that

**[16:30]** in a lab and all the manipulation that you need to do in a lab. The Jubilee

**[16:32]** you need to do in a lab. The Jubilee

**[16:32]** you need to do in a lab. The Jubilee motion platform it's actually coming

**[16:33]** motion platform it's actually coming

**[16:33]** motion platform it's actually coming from University of Washington where I

**[16:35]** from University of Washington where I

**[16:35]** from University of Washington where I did my PhD. It's open source. Um, and

**[16:38]** did my PhD. It's open source. Um, and

**[16:38]** did my PhD. It's open source. Um, and there's a open bioreactor and there's

**[16:41]** there's a open bioreactor and there's

**[16:41]** there's a open bioreactor and there's actually a workshop that just took place

**[16:43]** actually a workshop that just took place

**[16:43]** actually a workshop that just took place in April at Udub where they had people

**[16:46]** in April at Udub where they had people

**[16:46]** in April at Udub where they had people for a week hacking on creating different

**[16:50]** for a week hacking on creating different

**[16:50]** for a week hacking on creating different solutions for automating uh um

**[16:54]** solutions for automating uh um

**[16:54]** solutions for automating uh um scientific experiments in the lab. So

**[16:56]** scientific experiments in the lab. So

**[16:56]** scientific experiments in the lab. So anything from like droplet manipulation

**[16:59]** anything from like droplet manipulation

**[16:59]** anything from like droplet manipulation to robot handling liquids and mixing


### [17:00 - 18:00]

**[17:01]** to robot handling liquids and mixing

**[17:01]** to robot handling liquids and mixing like vials and things like that and

**[17:04]** like vials and things like that and

**[17:04]** like vials and things like that and other application with Jubilee. So

**[17:06]** other application with Jubilee. So

**[17:06]** other application with Jubilee. So definitely check them out.

**[17:09]** definitely check them out.

**[17:09]** definitely check them out. And for the future, uh, this is my last

**[17:13]** And for the future, uh, this is my last

**[17:13]** And for the future, uh, this is my last slide. You can imagine that

**[17:16]** slide. You can imagine that

**[17:16]** slide. You can imagine that based on the samples that we're

**[17:18]** based on the samples that we're

**[17:18]** based on the samples that we're collecting from this cameras and sensors

**[17:21]** collecting from this cameras and sensors

**[17:21]** collecting from this cameras and sensors and voice, it's much easier to create

**[17:25]** and voice, it's much easier to create

**[17:25]** and voice, it's much easier to create simulations. So we need we not don't

**[17:28]** simulations. So we need we not don't

**[17:28]** simulations. So we need we not don't need to be limited by the experiments

**[17:29]** need to be limited by the experiments

**[17:29]** need to be limited by the experiments we're doing in real life but those

**[17:31]** we're doing in real life but those

**[17:31]** we're doing in real life but those experiments that we're doing in real

**[17:33]** experiments that we're doing in real

**[17:33]** experiments that we're doing in real life are going to inform realistic

**[17:36]** life are going to inform realistic

**[17:36]** life are going to inform realistic simulations right so I could actually

**[17:38]** simulations right so I could actually

**[17:38]** simulations right so I could actually create a simulation of my crystal growth

**[17:41]** create a simulation of my crystal growth

**[17:41]** create a simulation of my crystal growth but more useful stuff right like

**[17:43]** but more useful stuff right like

**[17:43]** but more useful stuff right like bacteria colony growth and run those

**[17:46]** bacteria colony growth and run those

**[17:46]** bacteria colony growth and run those simulations with the lab conditions and

**[17:48]** simulations with the lab conditions and

**[17:48]** simulations with the lab conditions and then identify what are the best

**[17:50]** then identify what are the best

**[17:50]** then identify what are the best conditions for the experiment and create

**[17:53]** conditions for the experiment and create

**[17:53]** conditions for the experiment and create those conditions in the real life. So

**[17:56]** those conditions in the real life. So

**[17:56]** those conditions in the real life. So very excited about integrating

**[17:57]** very excited about integrating

**[17:57]** very excited about integrating simulation and I think that's where the

**[17:59]** simulation and I think that's where the

**[17:59]** simulation and I think that's where the this is going. Uh that was me. Uh if you


### [18:00 - 19:00]

**[18:03]** this is going. Uh that was me. Uh if you

**[18:03]** this is going. Uh that was me. Uh if you want to read more about uh my projects

**[18:06]** want to read more about uh my projects

**[18:06]** want to read more about uh my projects and the paper and all the open source

**[18:08]** and the paper and all the open source

**[18:08]** and the paper and all the open source projects. I do a lot of work in

**[18:10]** projects. I do a lot of work in

**[18:10]** projects. I do a lot of work in education as well. It's all on my

**[18:11]** education as well. It's all on my

**[18:12]** education as well. It's all on my website. And as Ben mentioned this

**[18:14]** website. And as Ben mentioned this

**[18:14]** website. And as Ben mentioned this morning, we are going to do an AI

**[18:17]** morning, we are going to do an AI

**[18:17]** morning, we are going to do an AI education summit and very excited about

**[18:20]** education summit and very excited about

**[18:20]** education summit and very excited about that. Uh some of you who saw my talk

**[18:23]** that. Uh some of you who saw my talk

**[18:23]** that. Uh some of you who saw my talk like in New York or last year know how

**[18:25]** like in New York or last year know how

**[18:25]** like in New York or last year know how much how passionate I am about

**[18:27]** much how passionate I am about

**[18:27]** much how passionate I am about education. Um so I hope you can join us

**[18:30]** education. Um so I hope you can join us

**[18:30]** education. Um so I hope you can join us for the summit. I really appreciate you

**[18:32]** for the summit. I really appreciate you

**[18:32]** for the summit. I really appreciate you coming to the talk today and uh I'll be

**[18:34]** coming to the talk today and uh I'll be

**[18:34]** coming to the talk today and uh I'll be around. Thank you so much.

**[18:36]** around. Thank you so much.

**[18:36]** around. Thank you so much. [Music]


