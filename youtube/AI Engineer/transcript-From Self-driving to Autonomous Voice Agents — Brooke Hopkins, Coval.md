# From Self-driving to Autonomous Voice Agents — Brooke Hopkins, Coval

**Video URL:** https://www.youtube.com/watch?v=kDczF4wBh8s

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Hey everyone, I'm Brooke. I'm the

**[00:17]** Hey everyone, I'm Brooke. I'm the founder of Koval and we are building

**[00:19]** founder of Koval and we are building

**[00:19]** founder of Koval and we are building evals for voice agents. So today I'm

**[00:21]** evals for voice agents. So today I'm

**[00:21]** evals for voice agents. So today I'm going to be talking a little bit about

**[00:23]** going to be talking a little bit about

**[00:23]** going to be talking a little bit about what can we learn from self-driving in

**[00:25]** what can we learn from self-driving in

**[00:25]** what can we learn from self-driving in building evals for voice agents. My

**[00:27]** building evals for voice agents. My

**[00:27]** building evals for voice agents. My background is from Whimo. So I led our

**[00:29]** background is from Whimo. So I led our

**[00:29]** background is from Whimo. So I led our eval job infrastructure team at Whimo

**[00:31]** eval job infrastructure team at Whimo

**[00:31]** eval job infrastructure team at Whimo that was responsible for our developer

**[00:33]** that was responsible for our developer

**[00:33]** that was responsible for our developer tools for launching and running

**[00:34]** tools for launching and running

**[00:34]** tools for launching and running simulations. And now we're taking a lot

**[00:36]** simulations. And now we're taking a lot

**[00:36]** simulations. And now we're taking a lot of the learnings from self-driving and

**[00:37]** of the learnings from self-driving and

**[00:38]** of the learnings from self-driving and robotics and applying them to voice

**[00:39]** robotics and applying them to voice

**[00:39]** robotics and applying them to voice agents.

**[00:41]** agents.

**[00:41]** agents. Um but first, why are voice agents not

**[00:43]** Um but first, why are voice agents not

**[00:43]** Um but first, why are voice agents not everywhere? They have this massive

**[00:45]** everywhere? They have this massive

**[00:45]** everywhere? They have this massive promise of being able to automate all of

**[00:47]** promise of being able to automate all of

**[00:47]** promise of being able to automate all of these really critical hard workflows

**[00:49]** these really critical hard workflows

**[00:49]** these really critical hard workflows autonomously. And I think probably a lot

**[00:52]** autonomously. And I think probably a lot

**[00:52]** autonomously. And I think probably a lot of you are building in voice agents and

**[00:54]** of you are building in voice agents and

**[00:54]** of you are building in voice agents and know how amazing voice agents can be.

**[00:56]** know how amazing voice agents can be.

**[00:56]** know how amazing voice agents can be. Um, I think the biggest problem to

**[00:58]** Um, I think the biggest problem to

**[00:58]** Um, I think the biggest problem to launching voice agents is trust. So, we


### [01:00 - 02:00]

**[01:01]** launching voice agents is trust. So, we

**[01:01]** launching voice agents is trust. So, we simultaneously are paradox paradoxically

**[01:04]** simultaneously are paradox paradoxically

**[01:04]** simultaneously are paradox paradoxically overestimating voice agents and trying

**[01:06]** overestimating voice agents and trying

**[01:06]** overestimating voice agents and trying to say, I'm going to automate all of my

**[01:08]** to say, I'm going to automate all of my

**[01:08]** to say, I'm going to automate all of my call volume or all of my workflows with

**[01:11]** call volume or all of my workflows with

**[01:11]** call volume or all of my workflows with voice all at once and we're

**[01:13]** voice all at once and we're

**[01:13]** voice all at once and we're underestimating them. I think what

**[01:16]** underestimating them. I think what

**[01:16]** underestimating them. I think what they're capable of today and really

**[01:18]** they're capable of today and really

**[01:18]** they're capable of today and really scoping a smaller problem versus what

**[01:20]** scoping a smaller problem versus what

**[01:20]** scoping a smaller problem versus what they could possibly do in the next six

**[01:21]** they could possibly do in the next six

**[01:21]** they could possibly do in the next six months. I think there's just so much

**[01:24]** months. I think there's just so much

**[01:24]** months. I think there's just so much more that you could have magical voice

**[01:26]** more that you could have magical voice

**[01:26]** more that you could have magical voice experience.

**[01:28]** experience.

**[01:28]** experience. Um, so conversational agents are so

**[01:31]** Um, so conversational agents are so

**[01:31]** Um, so conversational agents are so capable, but you also know that scaling

**[01:33]** capable, but you also know that scaling

**[01:33]** capable, but you also know that scaling to production is really hard. So it's

**[01:35]** to production is really hard. So it's

**[01:35]** to production is really hard. So it's easy to nail it for 10 conversations,

**[01:36]** easy to nail it for 10 conversations,

**[01:36]** easy to nail it for 10 conversations, but to do it for 10,000 or 100,000

**[01:39]** but to do it for 10,000 or 100,000

**[01:39]** but to do it for 10,000 or 100,000 becomes really difficult. So a lot of

**[01:41]** becomes really difficult. So a lot of

**[01:41]** becomes really difficult. So a lot of times voice agents get stuck in PC hell

**[01:43]** times voice agents get stuck in PC hell

**[01:43]** times voice agents get stuck in PC hell where enterprises are scared to actually

**[01:46]** where enterprises are scared to actually

**[01:46]** where enterprises are scared to actually deploy them to customerf facing issues

**[01:48]** deploy them to customerf facing issues

**[01:48]** deploy them to customerf facing issues or non- internal workflows.

**[01:51]** or non- internal workflows.

**[01:51]** or non- internal workflows. So I think there's two approaches to

**[01:53]** So I think there's two approaches to

**[01:53]** So I think there's two approaches to deal with that today. There's

**[01:55]** deal with that today. There's

**[01:55]** deal with that today. There's conservative but deterministic. So you

**[01:57]** conservative but deterministic. So you

**[01:57]** conservative but deterministic. So you force the agent down a specific path and

**[01:59]** force the agent down a specific path and


### [02:00 - 03:00]

**[02:00]** force the agent down a specific path and try and get it to do something exactly

**[02:01]** try and get it to do something exactly

**[02:01]** try and get it to do something exactly as you want it to do. This is basically

**[02:03]** as you want it to do. This is basically

**[02:03]** as you want it to do. This is basically an expensive IVR tree. Um you're using

**[02:06]** an expensive IVR tree. Um you're using

**[02:06]** an expensive IVR tree. Um you're using LLM, but you're essentially forcing it

**[02:08]** LLM, but you're essentially forcing it

**[02:08]** LLM, but you're essentially forcing it into certain pathways. Or you can make

**[02:11]** into certain pathways. Or you can make

**[02:11]** into certain pathways. Or you can make them much more autonomous and flexible

**[02:13]** them much more autonomous and flexible

**[02:13]** them much more autonomous and flexible to new scenarios that they've never seen

**[02:14]** to new scenarios that they've never seen

**[02:14]** to new scenarios that they've never seen before. But this makes it really hard to

**[02:17]** before. But this makes it really hard to

**[02:17]** before. But this makes it really hard to scale it to production because they're

**[02:19]** scale it to production because they're

**[02:19]** scale it to production because they're so unpredictable. And so taking actions

**[02:21]** so unpredictable. And so taking actions

**[02:21]** so unpredictable. And so taking actions on behalf or interfacing with users can

**[02:24]** on behalf or interfacing with users can

**[02:24]** on behalf or interfacing with users can be really um unpredictable.

**[02:27]** be really um unpredictable.

**[02:27]** be really um unpredictable. I think this is a false choice. I think

**[02:29]** I think this is a false choice. I think

**[02:29]** I think this is a false choice. I think you can have reliability and autonomy.

**[02:32]** you can have reliability and autonomy.

**[02:32]** you can have reliability and autonomy. So how many of you have taken the Whimo?

**[02:35]** So how many of you have taken the Whimo?

**[02:35]** So how many of you have taken the Whimo? Yeah. If you haven't and you're from out

**[02:37]** Yeah. If you haven't and you're from out

**[02:37]** Yeah. If you haven't and you're from out of town, you definitely should. It is so

**[02:40]** of town, you definitely should. It is so

**[02:40]** of town, you definitely should. It is so magical. So how did it become so

**[02:42]** magical. So how did it become so

**[02:42]** magical. So how did it become so magical? It's so reliable and also so

**[02:45]** magical? It's so reliable and also so

**[02:46]** magical? It's so reliable and also so smooth, but it's able to navigate all of

**[02:48]** smooth, but it's able to navigate all of

**[02:48]** smooth, but it's able to navigate all of these inter um interactions that it's

**[02:51]** these inter um interactions that it's

**[02:51]** these inter um interactions that it's never seen before. Go down streets it's

**[02:52]** never seen before. Go down streets it's

**[02:52]** never seen before. Go down streets it's never seen before. And Whimo is

**[02:54]** never seen before. And Whimo is

**[02:54]** never seen before. And Whimo is launching to all of these new cities um

**[02:56]** launching to all of these new cities um

**[02:56]** launching to all of these new cities um very quickly.

**[02:59]** very quickly.

**[02:59]** very quickly. So, I'm biased, but I think large scale


### [03:00 - 04:00]

**[03:02]** So, I'm biased, but I think large scale

**[03:02]** So, I'm biased, but I think large scale simulation has been the huge unlock for

**[03:04]** simulation has been the huge unlock for

**[03:04]** simulation has been the huge unlock for self-driving and robotics because

**[03:06]** self-driving and robotics because

**[03:06]** self-driving and robotics because without it, you So, we started in more

**[03:09]** without it, you So, we started in more

**[03:09]** without it, you So, we started in more manual eval. So um starting with like

**[03:11]** manual eval. So um starting with like

**[03:11]** manual eval. So um starting with like running the car throughout all the

**[03:13]** running the car throughout all the

**[03:13]** running the car throughout all the streets, noting where it doesn't go well

**[03:15]** streets, noting where it doesn't go well

**[03:15]** streets, noting where it doesn't go well and then bringing that back to the

**[03:17]** and then bringing that back to the

**[03:17]** and then bringing that back to the engineers. This obviously is very hard

**[03:19]** engineers. This obviously is very hard

**[03:19]** engineers. This obviously is very hard to scale. So then we created these

**[03:20]** to scale. So then we created these

**[03:20]** to scale. So then we created these specific tests where we're saying for

**[03:22]** specific tests where we're saying for

**[03:22]** specific tests where we're saying for this specific scenario, we expect these

**[03:24]** this specific scenario, we expect these

**[03:24]** this specific scenario, we expect these things to happen. Um but this is very

**[03:26]** things to happen. Um but this is very

**[03:26]** things to happen. Um but this is very brittle. Your scenarios tend to no

**[03:29]** brittle. Your scenarios tend to no

**[03:29]** brittle. Your scenarios tend to no longer be useful after a very short

**[03:30]** longer be useful after a very short

**[03:30]** longer be useful after a very short period of time and they're very

**[03:32]** period of time and they're very

**[03:32]** period of time and they're very expensive to maintain because you have

**[03:34]** expensive to maintain because you have

**[03:34]** expensive to maintain because you have to build up these very complicated

**[03:36]** to build up these very complicated

**[03:36]** to build up these very complicated scenarios and then say exactly what

**[03:37]** scenarios and then say exactly what

**[03:37]** scenarios and then say exactly what should happen in those. So then they

**[03:39]** should happen in those. So then they

**[03:39]** should happen in those. So then they move to the v the industry as a whole

**[03:42]** move to the v the industry as a whole

**[03:42]** move to the v the industry as a whole has moved to largecale evaluation. So

**[03:44]** has moved to largecale evaluation. So

**[03:44]** has moved to largecale evaluation. So how often is a certain type of event

**[03:47]** how often is a certain type of event

**[03:47]** how often is a certain type of event happening across many many simulations

**[03:50]** happening across many many simulations

**[03:50]** happening across many many simulations and so instead of trying to say for this

**[03:52]** and so instead of trying to say for this

**[03:52]** and so instead of trying to say for this specific instance I want this to happen

**[03:54]** specific instance I want this to happen

**[03:54]** specific instance I want this to happen you run large scale simulation to really

**[03:56]** you run large scale simulation to really

**[03:56]** you run large scale simulation to really reliably show how the agent is

**[03:58]** reliably show how the agent is

**[03:58]** reliably show how the agent is performing. So I'm going to talk through


### [04:00 - 05:00]

**[04:01]** performing. So I'm going to talk through

**[04:01]** performing. So I'm going to talk through like some of the things that I've

**[04:02]** like some of the things that I've

**[04:02]** like some of the things that I've learned from self-driving and how they

**[04:04]** learned from self-driving and how they

**[04:04]** learned from self-driving and how they apply to voice. Um, and hopefully that

**[04:06]** apply to voice. Um, and hopefully that

**[04:06]** apply to voice. Um, and hopefully that would that's useful because it's

**[04:07]** would that's useful because it's

**[04:07]** would that's useful because it's definitely been useful for us as we

**[04:08]** definitely been useful for us as we

**[04:08]** definitely been useful for us as we interact with hundreds of voice uh

**[04:11]** interact with hundreds of voice uh

**[04:11]** interact with hundreds of voice uh systems. So, what is the similarity

**[04:14]** systems. So, what is the similarity

**[04:14]** systems. So, what is the similarity between the two? Self-driving and

**[04:15]** between the two? Self-driving and

**[04:16]** between the two? Self-driving and conversational evals are very similar

**[04:18]** conversational evals are very similar

**[04:18]** conversational evals are very similar because both of them are systems where

**[04:19]** because both of them are systems where

**[04:19]** because both of them are systems where you're interacting with the real world

**[04:21]** you're interacting with the real world

**[04:21]** you're interacting with the real world and for each step that you take, you

**[04:23]** and for each step that you take, you

**[04:23]** and for each step that you take, you have to respond to the environment and

**[04:25]** have to respond to the environment and

**[04:25]** have to respond to the environment and go back and forth.

**[04:28]** go back and forth.

**[04:28]** go back and forth. And so simulations are really important

**[04:30]** And so simulations are really important

**[04:30]** And so simulations are really important for this because for every step that I

**[04:33]** for this because for every step that I

**[04:33]** for this because for every step that I take in a Whimo or a self-driving car or

**[04:36]** take in a Whimo or a self-driving car or

**[04:36]** take in a Whimo or a self-driving car or a smaller robotics vehic um device or in

**[04:40]** a smaller robotics vehic um device or in

**[04:40]** a smaller robotics vehic um device or in a conversation when I say hello what's

**[04:42]** a conversation when I say hello what's

**[04:42]** a conversation when I say hello what's your name you'll respond differently

**[04:44]** your name you'll respond differently

**[04:44]** your name you'll respond differently than when I say hello what's your email.

**[04:46]** than when I say hello what's your email.

**[04:46]** than when I say hello what's your email. So being able to simulate all these

**[04:48]** So being able to simulate all these

**[04:48]** So being able to simulate all these possible scenarios is really important

**[04:50]** possible scenarios is really important

**[04:50]** possible scenarios is really important because otherwise you have to create

**[04:52]** because otherwise you have to create

**[04:52]** because otherwise you have to create these static tests or do it manually and

**[04:54]** these static tests or do it manually and

**[04:54]** these static tests or do it manually and both of which are either expensive or

**[04:56]** both of which are either expensive or

**[04:56]** both of which are either expensive or brittle. Um, you also, and so this makes

**[04:59]** brittle. Um, you also, and so this makes

**[04:59]** brittle. Um, you also, and so this makes for a very durable


### [05:00 - 06:00]

**[05:02]** for a very durable

**[05:02]** for a very durable tests. If you have to specifically

**[05:04]** tests. If you have to specifically

**[05:04]** tests. If you have to specifically outline every single step along the way,

**[05:06]** outline every single step along the way,

**[05:06]** outline every single step along the way, those break immediately and are very

**[05:08]** those break immediately and are very

**[05:08]** those break immediately and are very expensive to maintain. And then lastly,

**[05:10]** expensive to maintain. And then lastly,

**[05:10]** expensive to maintain. And then lastly, coverage. You really want to simulate

**[05:12]** coverage. You really want to simulate

**[05:12]** coverage. You really want to simulate all of the possible scenarios across a

**[05:14]** all of the possible scenarios across a

**[05:14]** all of the possible scenarios across a very large area. And so the

**[05:16]** very large area. And so the

**[05:16]** very large area. And so the non-determinism of LMS is actually

**[05:19]** non-determinism of LMS is actually

**[05:19]** non-determinism of LMS is actually really useful for this because you can

**[05:21]** really useful for this because you can

**[05:21]** really useful for this because you can show what are all the possible things

**[05:22]** show what are all the possible things

**[05:22]** show what are all the possible things that someone might respond back to this.

**[05:24]** that someone might respond back to this.

**[05:24]** that someone might respond back to this. And I might simulate that over and over

**[05:26]** And I might simulate that over and over

**[05:26]** And I might simulate that over and over and look for what the probability of my

**[05:28]** and look for what the probability of my

**[05:28]** and look for what the probability of my agent succeeding is.

**[05:32]** agent succeeding is.

**[05:32]** agent succeeding is. Another thing that I touched on a bit is

**[05:34]** Another thing that I touched on a bit is

**[05:34]** Another thing that I touched on a bit is input output evals versus probabilistic

**[05:37]** input output evals versus probabilistic

**[05:37]** input output evals versus probabilistic evals. So with LMS to date, we have seen

**[05:41]** evals. So with LMS to date, we have seen

**[05:41]** evals. So with LMS to date, we have seen you run a set of inputs for your prompt.

**[05:45]** you run a set of inputs for your prompt.

**[05:45]** you run a set of inputs for your prompt. Excuse me. You run a set of inputs for

**[05:47]** Excuse me. You run a set of inputs for

**[05:47]** Excuse me. You run a set of inputs for your prompt and then you look at all the

**[05:49]** your prompt and then you look at all the

**[05:49]** your prompt and then you look at all the outputs and evaluate whether or not the

**[05:51]** outputs and evaluate whether or not the

**[05:51]** outputs and evaluate whether or not the output for that input was correct based

**[05:53]** output for that input was correct based

**[05:53]** output for that input was correct based on some criteria. So you might have a

**[05:54]** on some criteria. So you might have a

**[05:54]** on some criteria. So you might have a golden data set that you're iterating

**[05:56]** golden data set that you're iterating

**[05:56]** golden data set that you're iterating against. With conversational evals, it

**[05:59]** against. With conversational evals, it

**[05:59]** against. With conversational evals, it becomes even more important to have


### [06:00 - 07:00]

**[06:01]** becomes even more important to have

**[06:01]** becomes even more important to have reference free evaluation where you

**[06:03]** reference free evaluation where you

**[06:03]** reference free evaluation where you don't necessarily need to say these are

**[06:05]** don't necessarily need to say these are

**[06:05]** don't necessarily need to say these are all of the expected things I want am

**[06:07]** all of the expected things I want am

**[06:08]** all of the expected things I want am expecting for this exact input, but

**[06:10]** expecting for this exact input, but

**[06:10]** expecting for this exact input, but rather you're defining as a whole how

**[06:13]** rather you're defining as a whole how

**[06:13]** rather you're defining as a whole how often is my agent resolving the user

**[06:15]** often is my agent resolving the user

**[06:15]** often is my agent resolving the user inquiry? How often is my agent repeating

**[06:17]** inquiry? How often is my agent repeating

**[06:17]** inquiry? How often is my agent repeating itself over and over? How often is my

**[06:19]** itself over and over? How often is my

**[06:19]** itself over and over? How often is my agent saying things it shouldn't? um

**[06:22]** agent saying things it shouldn't? um

**[06:22]** agent saying things it shouldn't? um rather than saying for this specific

**[06:23]** rather than saying for this specific

**[06:23]** rather than saying for this specific scenario these six things should happen.

**[06:26]** scenario these six things should happen.

**[06:26]** scenario these six things should happen. Um and so this is what's going to really

**[06:28]** Um and so this is what's going to really

**[06:28]** Um and so this is what's going to really allow you to scale your evals and also

**[06:30]** allow you to scale your evals and also

**[06:30]** allow you to scale your evals and also what we did at Whimo. So coming up with

**[06:32]** what we did at Whimo. So coming up with

**[06:32]** what we did at Whimo. So coming up with metrics that apply to lots of scenarios.

**[06:36]** metrics that apply to lots of scenarios.

**[06:36]** metrics that apply to lots of scenarios. Another thing is that constant eval

**[06:38]** Another thing is that constant eval

**[06:38]** Another thing is that constant eval loops are what made autonomous vehicles

**[06:40]** loops are what made autonomous vehicles

**[06:40]** loops are what made autonomous vehicles scalable and that's what's going to make

**[06:42]** scalable and that's what's going to make

**[06:42]** scalable and that's what's going to make um voice agents scalable. I think we're

**[06:44]** um voice agents scalable. I think we're

**[06:44]** um voice agents scalable. I think we're seeing today that voice agents are so

**[06:47]** seeing today that voice agents are so

**[06:47]** seeing today that voice agents are so expensive to maintain in production once

**[06:49]** expensive to maintain in production once

**[06:49]** expensive to maintain in production once you deploy to an enterprise. It becomes

**[06:51]** you deploy to an enterprise. It becomes

**[06:51]** you deploy to an enterprise. It becomes often a professional service if you

**[06:53]** often a professional service if you

**[06:53]** often a professional service if you don't set up your processes right. And

**[06:55]** don't set up your processes right. And

**[06:55]** don't set up your processes right. And so you're constantly making all of these

**[06:57]** so you're constantly making all of these

**[06:57]** so you're constantly making all of these tweaks for specific enterprises which

**[06:59]** tweaks for specific enterprises which

**[06:59]** tweaks for specific enterprises which can take up 80% of your time even after


### [07:00 - 08:00]

**[07:01]** can take up 80% of your time even after

**[07:02]** can take up 80% of your time even after you've set up the initial agent. So

**[07:04]** you've set up the initial agent. So

**[07:04]** you've set up the initial agent. So something that the autonomous vehicle

**[07:06]** something that the autonomous vehicle

**[07:06]** something that the autonomous vehicle industry has been doing is how do you

**[07:08]** industry has been doing is how do you

**[07:08]** industry has been doing is how do you run like let's say you find a bug and as

**[07:11]** run like let's say you find a bug and as

**[07:11]** run like let's say you find a bug and as an engineer I might iterate on that and

**[07:13]** an engineer I might iterate on that and

**[07:13]** an engineer I might iterate on that and I run a couple of evals to reproduce

**[07:15]** I run a couple of evals to reproduce

**[07:15]** I run a couple of evals to reproduce that and then I fix the issue and then I

**[07:17]** that and then I fix the issue and then I

**[07:17]** that and then I fix the issue and then I run more so it wasn't stopping at a stop

**[07:20]** run more so it wasn't stopping at a stop

**[07:20]** run more so it wasn't stopping at a stop sign I iterate on that and now it is

**[07:21]** sign I iterate on that and now it is

**[07:22]** sign I iterate on that and now it is stopping at a stop sign. But then I run

**[07:24]** stopping at a stop sign. But then I run

**[07:24]** stopping at a stop sign. But then I run a larger regression set because maybe I

**[07:25]** a larger regression set because maybe I

**[07:25]** a larger regression set because maybe I just made the car stop every 10 seconds

**[07:28]** just made the car stop every 10 seconds

**[07:28]** just made the car stop every 10 seconds and so I broke the everything. Um, so

**[07:31]** and so I broke the everything. Um, so

**[07:31]** and so I broke the everything. Um, so then you run a larger regression set,

**[07:32]** then you run a larger regression set,

**[07:32]** then you run a larger regression set, make sure you didn't break everything.

**[07:34]** make sure you didn't break everything.

**[07:34]** make sure you didn't break everything. And then we have a set of um presubmit

**[07:36]** And then we have a set of um presubmit

**[07:36]** And then we have a set of um presubmit and postsubmit CI/CD workflows so that

**[07:39]** and postsubmit CI/CD workflows so that

**[07:39]** and postsubmit CI/CD workflows so that before you ship code and then after um

**[07:41]** before you ship code and then after um

**[07:42]** before you ship code and then after um you push the code to production, we make

**[07:43]** you push the code to production, we make

**[07:43]** you push the code to production, we make sure everything is continuously working.

**[07:45]** sure everything is continuously working.

**[07:45]** sure everything is continuously working. And then there's large scale release. So

**[07:48]** And then there's large scale release. So

**[07:48]** And then there's large scale release. So making sure that everything is up to par

**[07:50]** making sure that everything is up to par

**[07:50]** making sure that everything is up to par before we launch a new release. And this

**[07:52]** before we launch a new release. And this

**[07:52]** before we launch a new release. And this might be both manual evals and automated

**[07:55]** might be both manual evals and automated

**[07:55]** might be both manual evals and automated evals and some combination thereof. and

**[07:57]** evals and some combination thereof. and

**[07:57]** evals and some combination thereof. and then live monitoring and detection um


### [08:00 - 09:00]

**[08:00]** then live monitoring and detection um

**[08:00]** then live monitoring and detection um which then you can uh feed back into

**[08:02]** which then you can uh feed back into

**[08:02]** which then you can uh feed back into this whole system.

**[08:05]** this whole system.

**[08:05]** this whole system. So we're emulating a lot of this with

**[08:07]** So we're emulating a lot of this with

**[08:08]** So we're emulating a lot of this with voice. I think we think that's the right

**[08:10]** voice. I think we think that's the right

**[08:10]** voice. I think we think that's the right uh approach as well. But you're notably

**[08:13]** uh approach as well. But you're notably

**[08:13]** uh approach as well. But you're notably that there's still manual evals

**[08:15]** that there's still manual evals

**[08:15]** that there's still manual evals involved. The goal is not to automate

**[08:17]** involved. The goal is not to automate

**[08:17]** involved. The goal is not to automate all evals, but rather to leverage auto

**[08:20]** all evals, but rather to leverage auto

**[08:20]** all evals, but rather to leverage auto evals for speed and scale and then use

**[08:22]** evals for speed and scale and then use

**[08:22]** evals for speed and scale and then use the manual time that you have to really

**[08:25]** the manual time that you have to really

**[08:25]** the manual time that you have to really focus on how um those like very, you

**[08:28]** focus on how um those like very, you

**[08:28]** focus on how um those like very, you know, human touch judgment calls. Um so

**[08:31]** know, human touch judgment calls. Um so

**[08:31]** know, human touch judgment calls. Um so the process that we've seen is you might

**[08:33]** the process that we've seen is you might

**[08:33]** the process that we've seen is you might start with simulated conversations and

**[08:35]** start with simulated conversations and

**[08:35]** start with simulated conversations and you run some happy paths of like I know

**[08:37]** you run some happy paths of like I know

**[08:37]** you run some happy paths of like I know I should be able to book an appointment.

**[08:39]** I should be able to book an appointment.

**[08:39]** I should be able to book an appointment. Um so book an appointment for tomorrow.

**[08:41]** Um so book an appointment for tomorrow.

**[08:41]** Um so book an appointment for tomorrow. I run a bunch of simulations of that. I

**[08:43]** I run a bunch of simulations of that. I

**[08:43]** I run a bunch of simulations of that. I run emails. I come up with metrics of I

**[08:46]** run emails. I come up with metrics of I

**[08:46]** run emails. I come up with metrics of I look through all those conversations.

**[08:47]** look through all those conversations.

**[08:47]** look through all those conversations. Looking at your data is super important.

**[08:49]** Looking at your data is super important.

**[08:49]** Looking at your data is super important. Um I look at all those conversations and

**[08:51]** Um I look at all those conversations and

**[08:51]** Um I look at all those conversations and I say these are the ways they're

**[08:52]** I say these are the ways they're

**[08:52]** I say these are the ways they're failing. So I set up some automated

**[08:54]** failing. So I set up some automated

**[08:54]** failing. So I set up some automated metrics and iterate through this loop

**[08:56]** metrics and iterate through this loop

**[08:56]** metrics and iterate through this loop several times. Now I think it's ready

**[08:58]** several times. Now I think it's ready

**[08:58]** several times. Now I think it's ready for production. So I ship it to

**[08:59]** for production. So I ship it to

**[08:59]** for production. So I ship it to production and then run those evals


### [09:00 - 10:00]

**[09:01]** production and then run those evals

**[09:01]** production and then run those evals again. And so this cycle, this virtuous

**[09:04]** again. And so this cycle, this virtuous

**[09:04]** again. And so this cycle, this virtuous cycle of iterating on through simulation

**[09:07]** cycle of iterating on through simulation

**[09:07]** cycle of iterating on through simulation and then detecting or like flagging

**[09:09]** and then detecting or like flagging

**[09:09]** and then detecting or like flagging things for human review and then feeding

**[09:11]** things for human review and then feeding

**[09:11]** things for human review and then feeding all of that back into your simulations

**[09:13]** all of that back into your simulations

**[09:13]** all of that back into your simulations is super important for scalable voice

**[09:15]** is super important for scalable voice

**[09:15]** is super important for scalable voice agents.

**[09:18]** agents.

**[09:18]** agents. Um, so what level of realism is actually

**[09:21]** Um, so what level of realism is actually

**[09:21]** Um, so what level of realism is actually needed?

**[09:23]** needed?

**[09:23]** needed? Uh, something a question we get a lot is

**[09:25]** Uh, something a question we get a lot is

**[09:25]** Uh, something a question we get a lot is how are your are your voice agents

**[09:27]** how are your are your voice agents

**[09:27]** how are your are your voice agents exactly how my customers sound? And

**[09:29]** exactly how my customers sound? And

**[09:30]** exactly how my customers sound? And that's a good question because the level

**[09:32]** that's a good question because the level

**[09:32]** that's a good question because the level of realism is dependent on what you're

**[09:34]** of realism is dependent on what you're

**[09:34]** of realism is dependent on what you're trying to test. So like any scientific

**[09:37]** trying to test. So like any scientific

**[09:37]** trying to test. So like any scientific method, right? You're trying to control

**[09:38]** method, right? You're trying to control

**[09:38]** method, right? You're trying to control variables and then test for the things

**[09:40]** variables and then test for the things

**[09:40]** variables and then test for the things that you care about. So there's a

**[09:43]** that you care about. So there's a

**[09:43]** that you care about. So there's a something we saw in self-driving is that

**[09:45]** something we saw in self-driving is that

**[09:45]** something we saw in self-driving is that there's kind of this hierarchy of like

**[09:47]** there's kind of this hierarchy of like

**[09:47]** there's kind of this hierarchy of like you might not need to simulate

**[09:48]** you might not need to simulate

**[09:48]** you might not need to simulate everything in order to get a

**[09:50]** everything in order to get a

**[09:50]** everything in order to get a representative feedback on how your

**[09:52]** representative feedback on how your

**[09:52]** representative feedback on how your system is doing. Um so the way we think

**[09:54]** system is doing. Um so the way we think

**[09:54]** system is doing. Um so the way we think so for example all the time there are

**[09:57]** so for example all the time there are

**[09:57]** so for example all the time there are all these you know super hyperrealistic

**[09:59]** all these you know super hyperrealistic

**[09:59]** all these you know super hyperrealistic simulations coming out that look like a


### [10:00 - 11:00]

**[10:01]** simulations coming out that look like a

**[10:01]** simulations coming out that look like a you know that look like a real video and

**[10:04]** you know that look like a real video and

**[10:04]** you know that look like a real video and people would say that simulation system

**[10:06]** people would say that simulation system

**[10:06]** people would say that simulation system is amazing and really that's not

**[10:08]** is amazing and really that's not

**[10:08]** is amazing and really that's not necessarily true because what you want

**[10:10]** necessarily true because what you want

**[10:10]** necessarily true because what you want from a simulation system is how much can

**[10:12]** from a simulation system is how much can

**[10:12]** from a simulation system is how much can you control what parts of the system

**[10:14]** you control what parts of the system

**[10:14]** you control what parts of the system you're simulating and then how like what

**[10:17]** you're simulating and then how like what

**[10:17]** you're simulating and then how like what inputs are needed. So you might just

**[10:19]** inputs are needed. So you might just

**[10:19]** inputs are needed. So you might just need to know this is a dog and I this is

**[10:21]** need to know this is a dog and I this is

**[10:21]** need to know this is a dog and I this is a cat and this is a person walking

**[10:23]** a cat and this is a person walking

**[10:23]** a cat and this is a person walking across the street. Um and then what

**[10:25]** across the street. Um and then what

**[10:25]** across the street. Um and then what should I do next as a result of those

**[10:27]** should I do next as a result of those

**[10:27]** should I do next as a result of those inputs? And so this is the same for

**[10:29]** inputs? And so this is the same for

**[10:29]** inputs? And so this is the same for voice. We think about it as uh for

**[10:32]** voice. We think about it as uh for

**[10:32]** voice. We think about it as uh for example workflows, tool calls,

**[10:33]** example workflows, tool calls,

**[10:33]** example workflows, tool calls, instruction following. You actually

**[10:35]** instruction following. You actually

**[10:35]** instruction following. You actually don't need to even simulate that with

**[10:37]** don't need to even simulate that with

**[10:37]** don't need to even simulate that with voice. Often you might want to do

**[10:38]** voice. Often you might want to do

**[10:38]** voice. Often you might want to do endto-end tests with voice, but when

**[10:40]** endto-end tests with voice, but when

**[10:40]** endto-end tests with voice, but when you're iterating, doing that all with

**[10:42]** you're iterating, doing that all with

**[10:42]** you're iterating, doing that all with text is probably the fastest and

**[10:44]** text is probably the fastest and

**[10:44]** text is probably the fastest and cheapest way to do that. Um then for

**[10:47]** cheapest way to do that. Um then for

**[10:47]** cheapest way to do that. Um then for interruptions or latency or instructed

**[10:50]** interruptions or latency or instructed

**[10:50]** interruptions or latency or instructed pauses um simple voices that are just

**[10:52]** pauses um simple voices that are just

**[10:52]** pauses um simple voices that are just the basic basic voices are sufficient

**[10:55]** the basic basic voices are sufficient

**[10:55]** the basic basic voices are sufficient because you're doing that voicetovoice

**[10:56]** because you're doing that voicetovoice

**[10:56]** because you're doing that voicetovoice testing but you know accents or

**[10:59]** testing but you know accents or

**[10:59]** testing but you know accents or background noises might not impact that


### [11:00 - 12:00]

**[11:01]** background noises might not impact that

**[11:01]** background noises might not impact that as much. And then where you need

**[11:03]** as much. And then where you need

**[11:03]** as much. And then where you need hyperrealistic voices of different

**[11:04]** hyperrealistic voices of different

**[11:04]** hyperrealistic voices of different accents, different background noises,

**[11:06]** accents, different background noises,

**[11:06]** accents, different background noises, different audio quality, etc. is when

**[11:09]** different audio quality, etc. is when

**[11:09]** different audio quality, etc. is when you're testing those things in

**[11:11]** you're testing those things in

**[11:11]** you're testing those things in production and trying to recreate those

**[11:12]** production and trying to recreate those

**[11:12]** production and trying to recreate those issues. And so thinking about what what

**[11:15]** issues. And so thinking about what what

**[11:15]** issues. And so thinking about what what are the base level of components that

**[11:17]** are the base level of components that

**[11:17]** are the base level of components that you really need to to develop this is

**[11:21]** you really need to to develop this is

**[11:21]** you really need to to develop this is super important for um for building a

**[11:23]** super important for um for building a

**[11:23]** super important for um for building a good eval strategy.

**[11:26]** good eval strategy.

**[11:26]** good eval strategy. Uh and then a awesome tactic that we've

**[11:29]** Uh and then a awesome tactic that we've

**[11:29]** Uh and then a awesome tactic that we've learned is denoising. So um you run a

**[11:33]** learned is denoising. So um you run a

**[11:33]** learned is denoising. So um you run a bunch of evals and then you might find

**[11:35]** bunch of evals and then you might find

**[11:35]** bunch of evals and then you might find one that failed. And something that's

**[11:36]** one that failed. And something that's

**[11:36]** one that failed. And something that's really important about agents is that it

**[11:38]** really important about agents is that it

**[11:38]** really important about agents is that it doesn't it's not the end of the world

**[11:40]** doesn't it's not the end of the world

**[11:40]** doesn't it's not the end of the world maybe if it fails one time. You really

**[11:42]** maybe if it fails one time. You really

**[11:42]** maybe if it fails one time. You really want to know what is the probability of

**[11:43]** want to know what is the probability of

**[11:43]** want to know what is the probability of this failing overall. So then you can

**[11:46]** this failing overall. So then you can

**[11:46]** this failing overall. So then you can find that scenario and then reimulate

**[11:48]** find that scenario and then reimulate

**[11:48]** find that scenario and then reimulate that and maybe you reimulate that a

**[11:50]** that and maybe you reimulate that a

**[11:50]** that and maybe you reimulate that a hundred times. So is this scenario

**[11:52]** hundred times. So is this scenario

**[11:52]** hundred times. So is this scenario failing 50 out of a 100 times? Is it a

**[11:54]** failing 50 out of a 100 times? Is it a

**[11:54]** failing 50 out of a 100 times? Is it a coin flip? Is it failing 99 out of 100

**[11:57]** coin flip? Is it failing 99 out of 100

**[11:57]** coin flip? Is it failing 99 out of 100 times which it means it's definitely

**[11:59]** times which it means it's definitely

**[11:59]** times which it means it's definitely always failing. Um or does it fail once


### [12:00 - 13:00]

**[12:01]** always failing. Um or does it fail once

**[12:01]** always failing. Um or does it fail once out of a 100 times and that might be

**[12:02]** out of a 100 times and that might be

**[12:02]** out of a 100 times and that might be totally okay for your application. Um

**[12:05]** totally okay for your application. Um

**[12:05]** totally okay for your application. Um and so having a sense in the same way of

**[12:07]** and so having a sense in the same way of

**[12:07]** and so having a sense in the same way of cloud infrastructure where are you

**[12:09]** cloud infrastructure where are you

**[12:09]** cloud infrastructure where are you shooting for 69s of reliability for

**[12:11]** shooting for 69s of reliability for

**[12:11]** shooting for 69s of reliability for voice AI that's really important as well

**[12:13]** voice AI that's really important as well

**[12:13]** voice AI that's really important as well is like what reliability are you looking

**[12:14]** is like what reliability are you looking

**[12:14]** is like what reliability are you looking for for different parts of your product.

**[12:18]** for for different parts of your product.

**[12:18]** for for different parts of your product. So now I want to talk a bit about how to

**[12:19]** So now I want to talk a bit about how to

**[12:19]** So now I want to talk a bit about how to build an eval strategy because we

**[12:21]** build an eval strategy because we

**[12:21]** build an eval strategy because we believe that eval are as important part

**[12:24]** believe that eval are as important part

**[12:24]** believe that eval are as important part of your process uh it's the key part of

**[12:27]** of your process uh it's the key part of

**[12:27]** of your process uh it's the key part of your product development and it's not

**[12:28]** your product development and it's not

**[12:28]** your product development and it's not just an engineering best practice. This

**[12:30]** just an engineering best practice. This

**[12:30]** just an engineering best practice. This is actually like a core part of thinking

**[12:32]** is actually like a core part of thinking

**[12:32]** is actually like a core part of thinking through what does your product do.

**[12:35]** through what does your product do.

**[12:35]** through what does your product do. So voice like thinking through what

**[12:37]** So voice like thinking through what

**[12:37]** So voice like thinking through what metrics you should use is thinking

**[12:39]** metrics you should use is thinking

**[12:39]** metrics you should use is thinking through what does your product do and

**[12:41]** through what does your product do and

**[12:41]** through what does your product do and what do you want to be good at. You can

**[12:42]** what do you want to be good at. You can

**[12:42]** what do you want to be good at. You can build a general voice model that's kind

**[12:44]** build a general voice model that's kind

**[12:44]** build a general voice model that's kind of good at everything and that already

**[12:46]** of good at everything and that already

**[12:46]** of good at everything and that already exists, right? like you can use the

**[12:48]** exists, right? like you can use the

**[12:48]** exists, right? like you can use the OpenAI APIs, you can use like all of

**[12:51]** OpenAI APIs, you can use like all of

**[12:51]** OpenAI APIs, you can use like all of these different endto-end um voice

**[12:53]** these different endto-end um voice

**[12:53]** these different endto-end um voice systems that already exist that and are

**[12:55]** systems that already exist that and are

**[12:55]** systems that already exist that and are generally useful, but really you're

**[12:57]** generally useful, but really you're

**[12:57]** generally useful, but really you're probably building a vertical agent that

**[12:59]** probably building a vertical agent that

**[12:59]** probably building a vertical agent that you're trying to make useful at


### [13:00 - 14:00]

**[13:00]** you're trying to make useful at

**[13:00]** you're trying to make useful at something in particular. And so thinking

**[13:02]** something in particular. And so thinking

**[13:02]** something in particular. And so thinking about what you want it to do well and

**[13:04]** about what you want it to do well and

**[13:04]** about what you want it to do well and what you don't care if it does is a

**[13:05]** what you don't care if it does is a

**[13:06]** what you don't care if it does is a really important part of the process. Um

**[13:08]** really important part of the process. Um

**[13:08]** really important part of the process. Um and it's not just about latency, it's

**[13:10]** and it's not just about latency, it's

**[13:10]** and it's not just about latency, it's about interruptions. like your voice

**[13:12]** about interruptions. like your voice

**[13:12]** about interruptions. like your voice application actually might not be so

**[13:13]** application actually might not be so

**[13:13]** application actually might not be so latency sensitive because someone really

**[13:15]** latency sensitive because someone really

**[13:15]** latency sensitive because someone really wants a refund, but if you're doing

**[13:17]** wants a refund, but if you're doing

**[13:17]** wants a refund, but if you're doing outbound sales, latency is super

**[13:19]** outbound sales, latency is super

**[13:19]** outbound sales, latency is super important because that person's about to

**[13:20]** important because that person's about to

**[13:20]** important because that person's about to hang up the phone. Um, interruptions,

**[13:24]** hang up the phone. Um, interruptions,

**[13:24]** hang up the phone. Um, interruptions, uh, workflows, workflows, like how much

**[13:27]** uh, workflows, workflows, like how much

**[13:27]** uh, workflows, workflows, like how much you adhere to instruction following for

**[13:29]** you adhere to instruction following for

**[13:29]** you adhere to instruction following for some applications is really important.

**[13:31]** some applications is really important.

**[13:31]** some applications is really important. Like if you're booking an appointment

**[13:32]** Like if you're booking an appointment

**[13:32]** Like if you're booking an appointment and don't get all the details, it's

**[13:33]** and don't get all the details, it's

**[13:34]** and don't get all the details, it's useless. But if you're, you know, an

**[13:36]** useless. But if you're, you know, an

**[13:36]** useless. But if you're, you know, an interviewer or a therapist, you might be

**[13:38]** interviewer or a therapist, you might be

**[13:38]** interviewer or a therapist, you might be more tuned for conversational emails,

**[13:42]** more tuned for conversational emails,

**[13:42]** more tuned for conversational emails, uh, conversational workflows.

**[13:44]** uh, conversational workflows.

**[13:44]** uh, conversational workflows. And then, um, so really thinking through

**[13:46]** And then, um, so really thinking through

**[13:46]** And then, um, so really thinking through like what you're trying to measure.

**[13:48]** like what you're trying to measure.

**[13:48]** like what you're trying to measure. These are the five things that we see

**[13:49]** These are the five things that we see

**[13:49]** These are the five things that we see the most. But, um, LLM as a judge is a

**[13:53]** the most. But, um, LLM as a judge is a

**[13:53]** the most. But, um, LLM as a judge is a really powerful way of being really

**[13:55]** really powerful way of being really

**[13:55]** really powerful way of being really flexible and you can build out evalu.

**[13:59]** flexible and you can build out evalu.

**[13:59]** flexible and you can build out evalu. But something we get a lot is how do you


### [14:00 - 15:00]

**[14:00]** But something we get a lot is how do you

**[14:00]** But something we get a lot is how do you trust LLM as a judge? It's this magical

**[14:03]** trust LLM as a judge? It's this magical

**[14:03]** trust LLM as a judge? It's this magical thing that can be so flexible to so many

**[14:05]** thing that can be so flexible to so many

**[14:05]** thing that can be so flexible to so many cases and also it is very um you know

**[14:09]** cases and also it is very um you know

**[14:09]** cases and also it is very um you know can be very noisy but I think the common

**[14:11]** can be very noisy but I think the common

**[14:11]** can be very noisy but I think the common patterns that we see with LLM as a judge

**[14:13]** patterns that we see with LLM as a judge

**[14:13]** patterns that we see with LLM as a judge is that you say was this conversation

**[14:15]** is that you say was this conversation

**[14:15]** is that you say was this conversation successful that's a pretty that's going

**[14:17]** successful that's a pretty that's going

**[14:17]** successful that's a pretty that's going to be a really noisy metric um you might

**[14:19]** to be a really noisy metric um you might

**[14:20]** to be a really noisy metric um you might run that 10 times for the same

**[14:21]** run that 10 times for the same

**[14:21]** run that 10 times for the same conversation will come back um with lots

**[14:23]** conversation will come back um with lots

**[14:23]** conversation will come back um with lots of different responses so in Koval we

**[14:26]** of different responses so in Koval we

**[14:26]** of different responses so in Koval we have this metric studio that we think is

**[14:28]** have this metric studio that we think is

**[14:28]** have this metric studio that we think is really like um pretty different from

**[14:30]** really like um pretty different from

**[14:30]** really like um pretty different from anything out there because it allows

**[14:32]** anything out there because it allows

**[14:32]** anything out there because it allows allows you to iterate on this human

**[14:34]** allows you to iterate on this human

**[14:34]** allows you to iterate on this human incorporate human feedback into really

**[14:36]** incorporate human feedback into really

**[14:36]** incorporate human feedback into really correlate calibrating your metrics with

**[14:39]** correlate calibrating your metrics with

**[14:39]** correlate calibrating your metrics with human feedback. So you can iterate over

**[14:41]** human feedback. So you can iterate over

**[14:41]** human feedback. So you can iterate over and over until your automated metrics

**[14:44]** and over until your automated metrics

**[14:44]** and over until your automated metrics are aligning with human feedback. And

**[14:45]** are aligning with human feedback. And

**[14:45]** are aligning with human feedback. And now you have the confidence to go deploy

**[14:47]** now you have the confidence to go deploy

**[14:47]** now you have the confidence to go deploy those in production and run them over

**[14:49]** those in production and run them over

**[14:49]** those in production and run them over 10,000 conversations instead of the

**[14:51]** 10,000 conversations instead of the

**[14:51]** 10,000 conversations instead of the hundred that you labeled or the 10 that

**[14:53]** hundred that you labeled or the 10 that

**[14:53]** hundred that you labeled or the 10 that you labeled um to to get that

**[14:56]** you labeled um to to get that

**[14:56]** you labeled um to to get that confidence. So really, I think putting


### [15:00 - 16:00]

**[15:00]** confidence. So really, I think putting

**[15:00]** confidence. So really, I think putting in the time to saying this is the level

**[15:02]** in the time to saying this is the level

**[15:02]** in the time to saying this is the level of reliability that we're looking for

**[15:03]** of reliability that we're looking for

**[15:04]** of reliability that we're looking for and being thoughtful of that. Maybe just

**[15:05]** and being thoughtful of that. Maybe just

**[15:06]** and being thoughtful of that. Maybe just labeling 10 conversations is important

**[15:07]** labeling 10 conversations is important

**[15:07]** labeling 10 conversations is important to you. Um or maybe you really want to

**[15:10]** to you. Um or maybe you really want to

**[15:10]** to you. Um or maybe you really want to dial this in. Um but using this workflow

**[15:13]** dial this in. Um but using this workflow

**[15:13]** dial this in. Um but using this workflow can be really powerful.

**[15:16]** can be really powerful.

**[15:16]** can be really powerful. Uh our other advice of how to approach

**[15:18]** Uh our other advice of how to approach

**[15:18]** Uh our other advice of how to approach evals for voice AI is starting with this

**[15:21]** evals for voice AI is starting with this

**[15:21]** evals for voice AI is starting with this system of reviewing public benchmarks

**[15:23]** system of reviewing public benchmarks

**[15:23]** system of reviewing public benchmarks which can be a rough dial of this is how

**[15:26]** which can be a rough dial of this is how

**[15:26]** which can be a rough dial of this is how um this is roughly the direction I want

**[15:28]** um this is roughly the direction I want

**[15:28]** um this is roughly the direction I want to go in. Then benchmarking with your

**[15:30]** to go in. Then benchmarking with your

**[15:30]** to go in. Then benchmarking with your own specific data. So using if you're

**[15:33]** own specific data. So using if you're

**[15:33]** own specific data. So using if you're like a medical company using medical

**[15:35]** like a medical company using medical

**[15:35]** like a medical company using medical terms that you're going to be using in

**[15:36]** terms that you're going to be using in

**[15:36]** terms that you're going to be using in production to test out different

**[15:38]** production to test out different

**[15:38]** production to test out different transcription methods um etc. then

**[15:41]** transcription methods um etc. then

**[15:41]** transcription methods um etc. then running task based evals which are maybe

**[15:43]** running task based evals which are maybe

**[15:43]** running task based evals which are maybe text or very specific um smaller modules

**[15:46]** text or very specific um smaller modules

**[15:46]** text or very specific um smaller modules of your system. Again, what I talked

**[15:48]** of your system. Again, what I talked

**[15:48]** of your system. Again, what I talked about in self-driving is you don't

**[15:49]** about in self-driving is you don't

**[15:49]** about in self-driving is you don't necessarily need to enable every module

**[15:51]** necessarily need to enable every module

**[15:51]** necessarily need to enable every module on the car in order to test the one

**[15:53]** on the car in order to test the one

**[15:53]** on the car in order to test the one thing that you're trying to test. And

**[15:54]** thing that you're trying to test. And

**[15:54]** thing that you're trying to test. And then end to end eval where you're

**[15:56]** then end to end eval where you're

**[15:56]** then end to end eval where you're running everything at scale and um and

**[15:58]** running everything at scale and um and

**[15:58]** running everything at scale and um and how it would run in production.


### [16:00 - 17:00]

**[16:01]** how it would run in production.

**[16:01]** how it would run in production. So we've done a lot of benchmarking. You

**[16:03]** So we've done a lot of benchmarking. You

**[16:03]** So we've done a lot of benchmarking. You should check out our benchmarking um on

**[16:05]** should check out our benchmarking um on

**[16:05]** should check out our benchmarking um on our t uh on our website. But we tried to

**[16:08]** our t uh on our website. But we tried to

**[16:08]** our t uh on our website. But we tried to do continuous benchmarking of what are

**[16:10]** do continuous benchmarking of what are

**[16:10]** do continuous benchmarking of what are the latest models out there. But doing

**[16:13]** the latest models out there. But doing

**[16:13]** the latest models out there. But doing your own custom benchmarking is also

**[16:14]** your own custom benchmarking is also

**[16:14]** your own custom benchmarking is also really important. So through coal you

**[16:16]** really important. So through coal you

**[16:16]** really important. So through coal you can actually and you can also do this

**[16:18]** can actually and you can also do this

**[16:18]** can actually and you can also do this yourself. I just happen to have a tool

**[16:20]** yourself. I just happen to have a tool

**[16:20]** yourself. I just happen to have a tool that does this. Um but you can like run

**[16:23]** that does this. Um but you can like run

**[16:23]** that does this. Um but you can like run on your specific data because you might

**[16:26]** on your specific data because you might

**[16:26]** on your specific data because you might prefer different voices for the types of

**[16:27]** prefer different voices for the types of

**[16:27]** prefer different voices for the types of conversations that you're having or you

**[16:29]** conversations that you're having or you

**[16:29]** conversations that you're having or you might prefer different LLMs based on

**[16:31]** might prefer different LLMs based on

**[16:31]** might prefer different LLMs based on your specific tasks. Um and so

**[16:34]** your specific tasks. Um and so

**[16:34]** your specific tasks. Um and so benchmarking each part of your voice

**[16:36]** benchmarking each part of your voice

**[16:36]** benchmarking each part of your voice stack is really helpful for choosing out

**[16:37]** stack is really helpful for choosing out

**[16:38]** stack is really helpful for choosing out those models especially because voice

**[16:39]** those models especially because voice

**[16:39]** those models especially because voice has so many models and then um building

**[16:43]** has so many models and then um building

**[16:43]** has so many models and then um building out your task eval. So starting to get a

**[16:46]** out your task eval. So starting to get a

**[16:46]** out your task eval. So starting to get a sense of baseline performance. Where are

**[16:47]** sense of baseline performance. Where are

**[16:47]** sense of baseline performance. Where are the problem areas in your voice a

**[16:49]** the problem areas in your voice a

**[16:49]** the problem areas in your voice a application? Where are things working?

**[16:51]** application? Where are things working?

**[16:51]** application? Where are things working? Where could they be better?

**[16:53]** Where could they be better?

**[16:53]** Where could they be better? Um and then creating an eval process. So

**[16:56]** Um and then creating an eval process. So

**[16:56]** Um and then creating an eval process. So this means like what kinds of continuous

**[16:58]** this means like what kinds of continuous

**[16:58]** this means like what kinds of continuous monitoring are we doing? What do we do


### [17:00 - 18:00]

**[17:00]** monitoring are we doing? What do we do

**[17:00]** monitoring are we doing? What do we do when we find a bug in production from a

**[17:02]** when we find a bug in production from a

**[17:02]** when we find a bug in production from a customer? who takes it and where do what

**[17:04]** customer? who takes it and where do what

**[17:04]** customer? who takes it and where do what test sets does it go into so we can make

**[17:06]** test sets does it go into so we can make

**[17:06]** test sets does it go into so we can make sure that it doesn't happen again. How

**[17:07]** sure that it doesn't happen again. How

**[17:07]** sure that it doesn't happen again. How do we set up our hierarchy of test sets?

**[17:09]** do we set up our hierarchy of test sets?

**[17:09]** do we set up our hierarchy of test sets? Do we have test sets for specific

**[17:11]** Do we have test sets for specific

**[17:11]** Do we have test sets for specific customers that we care a lot about? Do

**[17:12]** customers that we care a lot about? Do

**[17:12]** customers that we care a lot about? Do we have types of customers that we have?

**[17:14]** we have types of customers that we have?

**[17:14]** we have types of customers that we have? Um do we have specific workflows or

**[17:16]** Um do we have specific workflows or

**[17:16]** Um do we have specific workflows or features of our voice agent? Um and then

**[17:19]** features of our voice agent? Um and then

**[17:19]** features of our voice agent? Um and then creating dashboards and processes so

**[17:21]** creating dashboards and processes so

**[17:21]** creating dashboards and processes so that you can check in on those things

**[17:22]** that you can check in on those things

**[17:22]** that you can check in on those things continuously. I think this is an

**[17:24]** continuously. I think this is an

**[17:24]** continuously. I think this is an underestimated piece of the process is

**[17:26]** underestimated piece of the process is

**[17:26]** underestimated piece of the process is like what is our continuous eval process

**[17:28]** like what is our continuous eval process

**[17:28]** like what is our continuous eval process versus just saying does the voice agent

**[17:30]** versus just saying does the voice agent

**[17:30]** versus just saying does the voice agent work when I deploy it to this production

**[17:32]** work when I deploy it to this production

**[17:32]** work when I deploy it to this production this uh uh customer on their during

**[17:35]** this uh uh customer on their during

**[17:35]** this uh uh customer on their during their pilot period.

**[17:38]** their pilot period.

**[17:38]** their pilot period. Um so yeah, always happy to talk more

**[17:41]** Um so yeah, always happy to talk more

**[17:41]** Um so yeah, always happy to talk more about tips on like what we've seen

**[17:43]** about tips on like what we've seen

**[17:43]** about tips on like what we've seen across all of the many voice systems

**[17:45]** across all of the many voice systems

**[17:45]** across all of the many voice systems that we've seen. But one of the reasons

**[17:47]** that we've seen. But one of the reasons

**[17:47]** that we've seen. But one of the reasons why we're so excited about the future of

**[17:49]** why we're so excited about the future of

**[17:49]** why we're so excited about the future of voice and I think Quinn um uh stole a

**[17:53]** voice and I think Quinn um uh stole a

**[17:53]** voice and I think Quinn um uh stole a little bit of this. But Quinn, I really

**[17:55]** little bit of this. But Quinn, I really

**[17:55]** little bit of this. But Quinn, I really think that voice is the next platform.

**[17:58]** think that voice is the next platform.

**[17:58]** think that voice is the next platform. Um so we had web, we had mobile, and I


### [18:00 - 19:00]

**[18:01]** Um so we had web, we had mobile, and I

**[18:01]** Um so we had web, we had mobile, and I think both of these were huge platform

**[18:03]** think both of these were huge platform

**[18:03]** think both of these were huge platform shifts and what types of things do you

**[18:05]** shifts and what types of things do you

**[18:05]** shifts and what types of things do you expect that companies will allow you to

**[18:06]** expect that companies will allow you to

**[18:06]** expect that companies will allow you to do on those platforms? What types of

**[18:09]** do on those platforms? What types of

**[18:09]** do on those platforms? What types of work where in the workflow where in your

**[18:11]** work where in the workflow where in your

**[18:11]** work where in the workflow where in your daily live life are you meeting the

**[18:13]** daily live life are you meeting the

**[18:13]** daily live life are you meeting the user? And I think voice unlocking all of

**[18:16]** user? And I think voice unlocking all of

**[18:16]** user? And I think voice unlocking all of these new really natural voice

**[18:17]** these new really natural voice

**[18:18]** these new really natural voice experiences. It doesn't mean everything

**[18:19]** experiences. It doesn't mean everything

**[18:19]** experiences. It doesn't mean everything you should be doing via voice, but

**[18:21]** you should be doing via voice, but

**[18:21]** you should be doing via voice, but there's really exciting potential there.

**[18:25]** there's really exciting potential there.

**[18:25]** there's really exciting potential there. And in the next three years, we think

**[18:27]** And in the next three years, we think

**[18:27]** And in the next three years, we think every enterprise is going to launch a

**[18:29]** every enterprise is going to launch a

**[18:29]** every enterprise is going to launch a voice experience. It's going to be like

**[18:31]** voice experience. It's going to be like

**[18:31]** voice experience. It's going to be like a mobile app where if the airline does

**[18:33]** a mobile app where if the airline does

**[18:33]** a mobile app where if the airline does not have a good voice experience, it's

**[18:36]** not have a good voice experience, it's

**[18:36]** not have a good voice experience, it's going to be like not having a good

**[18:37]** going to be like not having a good

**[18:37]** going to be like not having a good mobile app and it will just be a

**[18:39]** mobile app and it will just be a

**[18:39]** mobile app and it will just be a baseline expectation. And I think users

**[18:41]** baseline expectation. And I think users

**[18:41]** baseline expectation. And I think users expectations of what really amazing

**[18:43]** expectations of what really amazing

**[18:44]** expectations of what really amazing magical voice AI experiences will be is

**[18:46]** magical voice AI experiences will be is

**[18:46]** magical voice AI experiences will be is just going to increase over um over the

**[18:49]** just going to increase over um over the

**[18:49]** just going to increase over um over the next few years.

**[18:51]** next few years.

**[18:51]** next few years. So we really want to enable this future

**[18:54]** So we really want to enable this future

**[18:54]** So we really want to enable this future and so we think the next gen of scalable

**[18:56]** and so we think the next gen of scalable

**[18:56]** and so we think the next gen of scalable voice AI will be built with integrated

**[18:58]** voice AI will be built with integrated

**[18:58]** voice AI will be built with integrated eval using Cobalt


### [19:00 - 20:00]

**[19:01]** eval using Cobalt

**[19:01]** eval using Cobalt and we're hiring. So we're always

**[19:03]** and we're hiring. So we're always

**[19:03]** and we're hiring. So we're always looking for people to join us. I think

**[19:05]** looking for people to join us. I think

**[19:05]** looking for people to join us. I think this is like really one of the most

**[19:07]** this is like really one of the most

**[19:07]** this is like really one of the most technically interesting fields that I

**[19:10]** technically interesting fields that I

**[19:10]** technically interesting fields that I have ever worked in because you get to

**[19:11]** have ever worked in because you get to

**[19:12]** have ever worked in because you get to work with every model across the stack

**[19:14]** work with every model across the stack

**[19:14]** work with every model across the stack and there are so many different types of

**[19:16]** and there are so many different types of

**[19:16]** and there are so many different types of models, different types of problems,

**[19:17]** models, different types of problems,

**[19:17]** models, different types of problems, scalability, new frontiers of building

**[19:20]** scalability, new frontiers of building

**[19:20]** scalability, new frontiers of building infrastructure and no one knows any of

**[19:22]** infrastructure and no one knows any of

**[19:22]** infrastructure and no one knows any of the answers. So, it's a really exciting

**[19:23]** the answers. So, it's a really exciting

**[19:24]** the answers. So, it's a really exciting space. Thanks so much everyone.


