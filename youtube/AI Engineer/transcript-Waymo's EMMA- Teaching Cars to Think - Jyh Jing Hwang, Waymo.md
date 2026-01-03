# Waymo's EMMA- Teaching Cars to Think - Jyh Jing Hwang, Waymo

**Video URL:** https://www.youtube.com/watch?v=iS9YFW28XyM

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** So I I think a lot of people here

**[00:18]** So I I think a lot of people here already to be here in San Francisco. So

**[00:21]** already to be here in San Francisco. So

**[00:21]** already to be here in San Francisco. So we drive every day and I think the

**[00:24]** we drive every day and I think the

**[00:24]** we drive every day and I think the technology just works as you all

**[00:26]** technology just works as you all

**[00:26]** technology just works as you all witness. So uh I'm going to talk a

**[00:29]** witness. So uh I'm going to talk a

**[00:29]** witness. So uh I'm going to talk a little bit about the history of

**[00:30]** little bit about the history of

**[00:30]** little bit about the history of autonomous driving research like what it

**[00:32]** autonomous driving research like what it

**[00:32]** autonomous driving research like what it took to to to take us here and in the

**[00:35]** took to to to take us here and in the

**[00:35]** took to to to take us here and in the current status. So in the autonomous

**[00:37]** current status. So in the autonomous

**[00:38]** current status. So in the autonomous driving history uh people started the

**[00:40]** driving history uh people started the

**[00:40]** driving history uh people started the research in 1980s where it's just very

**[00:44]** research in 1980s where it's just very

**[00:44]** research in 1980s where it's just very simple neuronet networks there are three

**[00:46]** simple neuronet networks there are three

**[00:46]** simple neuronet networks there are three layers and over time people start to

**[00:48]** layers and over time people start to

**[00:48]** layers and over time people start to think about you know going deeper and

**[00:50]** think about you know going deeper and

**[00:50]** think about you know going deeper and deeper and then in around uh 2020 there

**[00:54]** deeper and then in around uh 2020 there

**[00:54]** deeper and then in around uh 2020 there is papers from NVDI and other uh

**[00:57]** is papers from NVDI and other uh

**[00:57]** is papers from NVDI and other uh research labs publishing end to end

**[00:59]** research labs publishing end to end

**[00:59]** research labs publishing end to end driving models and this is one of the


### [01:00 - 02:00]

**[01:01]** driving models and this is one of the

**[01:01]** driving models and this is one of the videos that they published at that time

**[01:03]** videos that they published at that time

**[01:03]** videos that they published at that time right and then we can we can check it

**[01:05]** right and then we can we can check it

**[01:05]** right and then we can we can check it out right the the the car in front

**[01:08]** out right the the the car in front

**[01:08]** out right the the the car in front driving is the atomic driving cars from

**[01:10]** driving is the atomic driving cars from

**[01:10]** driving is the atomic driving cars from the research labs at that time and you

**[01:12]** the research labs at that time and you

**[01:12]** the research labs at that time and you can see that it's actually drifting

**[01:14]** can see that it's actually drifting

**[01:14]** can see that it's actually drifting right so this is more like a L2 sort of

**[01:18]** right so this is more like a L2 sort of

**[01:18]** right so this is more like a L2 sort of technology and you wouldn't want to

**[01:20]** technology and you wouldn't want to

**[01:20]** technology and you wouldn't want to basically ride in it so why is an L4

**[01:24]** basically ride in it so why is an L4

**[01:24]** basically ride in it so why is an L4 system that Whimo has so much better

**[01:27]** system that Whimo has so much better

**[01:27]** system that Whimo has so much better right you can see it drives around the

**[01:29]** right you can see it drives around the

**[01:29]** right you can see it drives around the San Francisco in various regions in

**[01:31]** San Francisco in various regions in

**[01:31]** San Francisco in various regions in downtown areas and it avoids pedestrians

**[01:35]** downtown areas and it avoids pedestrians

**[01:35]** downtown areas and it avoids pedestrians cyclists and it makes rows very safe.

**[01:38]** cyclists and it makes rows very safe.

**[01:38]** cyclists and it makes rows very safe. So, so the secret is very basically on

**[01:40]** So, so the secret is very basically on

**[01:40]** So, so the secret is very basically on the top where uh you can see that this

**[01:43]** the top where uh you can see that this

**[01:43]** the top where uh you can see that this is a sort of visualization or departing

**[01:46]** is a sort of visualization or departing

**[01:46]** is a sort of visualization or departing screen where it visualize everything

**[01:48]** screen where it visualize everything

**[01:48]** screen where it visualize everything that the system understands. So, it can

**[01:51]** that the system understands. So, it can

**[01:51]** that the system understands. So, it can actually capture all the cars,

**[01:53]** actually capture all the cars,

**[01:53]** actually capture all the cars, pedestrians, cyclists, traffic lights,

**[01:56]** pedestrians, cyclists, traffic lights,

**[01:56]** pedestrians, cyclists, traffic lights, crossroads and it understand almost

**[01:58]** crossroads and it understand almost

**[01:58]** crossroads and it understand almost everything related to driving. And we


### [02:00 - 03:00]

**[02:01]** everything related to driving. And we

**[02:01]** everything related to driving. And we can see uh this is a very complicated

**[02:03]** can see uh this is a very complicated

**[02:03]** can see uh this is a very complicated system. If we break it down, it's

**[02:06]** system. If we break it down, it's

**[02:06]** system. If we break it down, it's basically a perception system where it

**[02:09]** basically a perception system where it

**[02:09]** basically a perception system where it understands the world and there is a

**[02:11]** understands the world and there is a

**[02:11]** understands the world and there is a prediction system that basically

**[02:13]** prediction system that basically

**[02:13]** prediction system that basically predicts the future of future world

**[02:16]** predicts the future of future world

**[02:16]** predicts the future of future world states given the current one. And

**[02:18]** states given the current one. And

**[02:18]** states given the current one. And finally, there is a planning system that

**[02:20]** finally, there is a planning system that

**[02:20]** finally, there is a planning system that basically tell us like how we should

**[02:22]** basically tell us like how we should

**[02:22]** basically tell us like how we should drive in this scenario like we should

**[02:25]** drive in this scenario like we should

**[02:25]** drive in this scenario like we should turn right, how much acceleration, how

**[02:27]** turn right, how much acceleration, how

**[02:27]** turn right, how much acceleration, how much steering etc. So this is the the

**[02:30]** much steering etc. So this is the the

**[02:30]** much steering etc. So this is the the whole autonomous driving system that is

**[02:31]** whole autonomous driving system that is

**[02:31]** whole autonomous driving system that is very complicated and delicated but it

**[02:35]** very complicated and delicated but it

**[02:35]** very complicated and delicated but it solves problems right it drives in San

**[02:37]** solves problems right it drives in San

**[02:37]** solves problems right it drives in San Francisco today. So what else? So what

**[02:40]** Francisco today. So what else? So what

**[02:40]** Francisco today. So what else? So what are we heading with atom driving the the

**[02:43]** are we heading with atom driving the the

**[02:43]** are we heading with atom driving the the answer is scaling right. So we proven

**[02:46]** answer is scaling right. So we proven

**[02:46]** answer is scaling right. So we proven that we are operating in Phoenix, San

**[02:49]** that we are operating in Phoenix, San

**[02:49]** that we are operating in Phoenix, San Francisco, Austin and Los Angeles today

**[02:53]** Francisco, Austin and Los Angeles today

**[02:53]** Francisco, Austin and Los Angeles today and is offering the rider only service.

**[02:56]** and is offering the rider only service.

**[02:56]** and is offering the rider only service. However, we are our ambition is not

**[02:59]** However, we are our ambition is not

**[02:59]** However, we are our ambition is not going to stop in just four cities now.


### [03:00 - 04:00]

**[03:02]** going to stop in just four cities now.

**[03:02]** going to stop in just four cities now. So, in this year, we are doing a road

**[03:04]** So, in this year, we are doing a road

**[03:04]** So, in this year, we are doing a road trip where we are visiting about 10

**[03:06]** trip where we are visiting about 10

**[03:06]** trip where we are visiting about 10 cities um in various locations. Here is

**[03:09]** cities um in various locations. Here is

**[03:10]** cities um in various locations. Here is the map and you can even see that we are

**[03:13]** the map and you can even see that we are

**[03:13]** the map and you can even see that we are actually going across the globe to to

**[03:15]** actually going across the globe to to

**[03:16]** actually going across the globe to to Tokyo, Japan. So, there is a lot of

**[03:19]** Tokyo, Japan. So, there is a lot of

**[03:19]** Tokyo, Japan. So, there is a lot of challenges when we start to scale.

**[03:24]** challenges when we start to scale.

**[03:24]** challenges when we start to scale. So just recently we finished a open

**[03:28]** So just recently we finished a open

**[03:28]** So just recently we finished a open challenge for participants to solve some

**[03:31]** challenge for participants to solve some

**[03:31]** challenge for participants to solve some of the hardest problems that we see in

**[03:33]** of the hardest problems that we see in

**[03:33]** of the hardest problems that we see in our spending. So let's replay the video

**[03:36]** our spending. So let's replay the video

**[03:36]** our spending. So let's replay the video a little bit here. So on the on the top

**[03:39]** a little bit here. So on the on the top

**[03:39]** a little bit here. So on the on the top left there is a marone run on the right

**[03:42]** left there is a marone run on the right

**[03:42]** left there is a marone run on the right and then there's are cones around the

**[03:44]** and then there's are cones around the

**[03:44]** and then there's are cones around the the the the roads. And most

**[03:47]** the the the roads. And most

**[03:47]** the the the roads. And most interestingly is that when we drive a

**[03:50]** interestingly is that when we drive a

**[03:50]** interestingly is that when we drive a closer to the intersection, if you look

**[03:52]** closer to the intersection, if you look

**[03:52]** closer to the intersection, if you look at the traffic light, it's actually red,

**[03:54]** at the traffic light, it's actually red,

**[03:54]** at the traffic light, it's actually red, but there is a traffic control man

**[03:56]** but there is a traffic control man

**[03:56]** but there is a traffic control man waving us to go ahead. So, it's actually

**[03:59]** waving us to go ahead. So, it's actually

**[03:59]** waving us to go ahead. So, it's actually green and and this is very confusing,


### [04:00 - 05:00]

**[04:02]** green and and this is very confusing,

**[04:02]** green and and this is very confusing, right? And all these longtails are very

**[04:05]** right? And all these longtails are very

**[04:05]** right? And all these longtails are very challenging to solve and there are

**[04:08]** challenging to solve and there are

**[04:08]** challenging to solve and there are challenges in like a lot of times that

**[04:11]** challenges in like a lot of times that

**[04:11]** challenges in like a lot of times that you've never seen it in your entire life

**[04:13]** you've never seen it in your entire life

**[04:14]** you've never seen it in your entire life of driving. But for Whimo and Whimo

**[04:16]** of driving. But for Whimo and Whimo

**[04:16]** of driving. But for Whimo and Whimo scale we will see very very often and we

**[04:20]** scale we will see very very often and we

**[04:20]** scale we will see very very often and we need to solve them to in order to scale.

**[04:23]** need to solve them to in order to scale.

**[04:23]** need to solve them to in order to scale. So one of the the the the solutions

**[04:25]** So one of the the the the solutions

**[04:25]** So one of the the the the solutions arises where foundation model is is very

**[04:28]** arises where foundation model is is very

**[04:28]** arises where foundation model is is very generalizable right. So let's just take

**[04:31]** generalizable right. So let's just take

**[04:31]** generalizable right. So let's just take a example here that we feed in Gemini

**[04:34]** a example here that we feed in Gemini

**[04:34]** a example here that we feed in Gemini right you can see the video where when

**[04:36]** right you can see the video where when

**[04:36]** right you can see the video where when we were driving peacefully suddenly

**[04:38]** we were driving peacefully suddenly

**[04:38]** we were driving peacefully suddenly there are a a a bunch of angry birds

**[04:41]** there are a a a bunch of angry birds

**[04:41]** there are a a a bunch of angry birds right they they appear and attacked our

**[04:43]** right they they appear and attacked our

**[04:43]** right they they appear and attacked our car virtually right so that's where we

**[04:45]** car virtually right so that's where we

**[04:45]** car virtually right so that's where we need to react but for a car to

**[04:48]** need to react but for a car to

**[04:48]** need to react but for a car to understand the scenario it also has to

**[04:51]** understand the scenario it also has to

**[04:51]** understand the scenario it also has to understand okay this is a fleet of birds

**[04:54]** understand okay this is a fleet of birds

**[04:54]** understand okay this is a fleet of birds and how they are going to behave how

**[04:56]** and how they are going to behave how

**[04:56]** and how they are going to behave how they are going to interact with the car

**[04:58]** they are going to interact with the car

**[04:58]** they are going to interact with the car right this is not the everyday driving


### [05:00 - 06:00]

**[05:00]** right this is not the everyday driving

**[05:00]** right this is not the everyday driving that you see. But this is a critical

**[05:02]** that you see. But this is a critical

**[05:02]** that you see. But this is a critical long tail. So let's see what Gemini

**[05:04]** long tail. So let's see what Gemini

**[05:04]** long tail. So let's see what Gemini responds. So Gemini basically says that

**[05:07]** responds. So Gemini basically says that

**[05:07]** responds. So Gemini basically says that a large flock of birds suddenly takes

**[05:10]** a large flock of birds suddenly takes

**[05:10]** a large flock of birds suddenly takes flight from the ground in front of the

**[05:12]** flight from the ground in front of the

**[05:12]** flight from the ground in front of the vehicle and the expected behavior is

**[05:15]** vehicle and the expected behavior is

**[05:15]** vehicle and the expected behavior is basically to slow down and uh remain

**[05:18]** basically to slow down and uh remain

**[05:18]** basically to slow down and uh remain alert and possibly adjust the speed uh

**[05:22]** alert and possibly adjust the speed uh

**[05:22]** alert and possibly adjust the speed uh afterwards. So this is a very basically

**[05:25]** afterwards. So this is a very basically

**[05:25]** afterwards. So this is a very basically I would say perfect answer to how we

**[05:28]** I would say perfect answer to how we

**[05:28]** I would say perfect answer to how we should drive with respect to this

**[05:29]** should drive with respect to this

**[05:29]** should drive with respect to this scenario. And this is another scenario

**[05:32]** scenario. And this is another scenario

**[05:32]** scenario. And this is another scenario where you can see there is a scooter

**[05:34]** where you can see there is a scooter

**[05:34]** where you can see there is a scooter rider in front of us and unfortunately

**[05:37]** rider in front of us and unfortunately

**[05:37]** rider in front of us and unfortunately she slipped right and this is because

**[05:40]** she slipped right and this is because

**[05:40]** she slipped right and this is because basically it's at night and there there

**[05:44]** basically it's at night and there there

**[05:44]** basically it's at night and there there was rain earlier so the the row was wet.

**[05:47]** was rain earlier so the the row was wet.

**[05:47]** was rain earlier so the the row was wet. So these kind of events also happens um

**[05:50]** So these kind of events also happens um

**[05:50]** So these kind of events also happens um quite often like when the scale is large

**[05:54]** quite often like when the scale is large

**[05:54]** quite often like when the scale is large right but this is a very much a safety

**[05:57]** right but this is a very much a safety

**[05:57]** right but this is a very much a safety critical events that we we really want

**[05:59]** critical events that we we really want

**[05:59]** critical events that we we really want to get it right and get it perfect and


### [06:00 - 07:00]

**[06:01]** to get it right and get it perfect and

**[06:01]** to get it right and get it perfect and let's ask Gemini again and Gemini

**[06:03]** let's ask Gemini again and Gemini

**[06:03]** let's ask Gemini again and Gemini actually identify the entire scenario

**[06:05]** actually identify the entire scenario

**[06:05]** actually identify the entire scenario correctly and even identify a a gas

**[06:08]** correctly and even identify a a gas

**[06:08]** correctly and even identify a a gas station uh in far away scene so I I

**[06:12]** station uh in far away scene so I I

**[06:12]** station uh in far away scene so I I think it's very telling that in today's

**[06:15]** think it's very telling that in today's

**[06:15]** think it's very telling that in today's foundation models they actually

**[06:17]** foundation models they actually

**[06:17]** foundation models they actually generalize well in these kind of rare

**[06:20]** generalize well in these kind of rare

**[06:20]** generalize well in these kind of rare events and the questions becomes like

**[06:23]** events and the questions becomes like

**[06:23]** events and the questions becomes like how how do we like how do we leverage

**[06:27]** how how do we like how do we leverage

**[06:27]** how how do we like how do we leverage this technology for Thomas driving.

**[06:30]** this technology for Thomas driving.

**[06:30]** this technology for Thomas driving. So here is our exploration uh in

**[06:32]** So here is our exploration uh in

**[06:32]** So here is our exploration uh in research where we want to have a more

**[06:36]** research where we want to have a more

**[06:36]** research where we want to have a more generalizable time driving system by

**[06:38]** generalizable time driving system by

**[06:38]** generalizable time driving system by leveraging Gemini or other multimodal

**[06:40]** leveraging Gemini or other multimodal

**[06:40]** leveraging Gemini or other multimodal large language models.

**[06:43]** large language models.

**[06:43]** large language models. So here we we call it Emma. So this is

**[06:46]** So here we we call it Emma. So this is

**[06:46]** So here we we call it Emma. So this is the simplest form of AMA where the idea

**[06:49]** the simplest form of AMA where the idea

**[06:49]** the simplest form of AMA where the idea is very straightforward. Yeah, Gemini is

**[06:52]** is very straightforward. Yeah, Gemini is

**[06:52]** is very straightforward. Yeah, Gemini is very good at generalizing in various

**[06:54]** very good at generalizing in various

**[06:54]** very good at generalizing in various scenarios. So let's just put it to

**[06:57]** scenarios. So let's just put it to

**[06:57]** scenarios. So let's just put it to drive. So how do we do that? Um so on


### [07:00 - 08:00]

**[07:01]** drive. So how do we do that? Um so on

**[07:01]** drive. So how do we do that? Um so on the top left is about router where we

**[07:05]** the top left is about router where we

**[07:05]** the top left is about router where we want to know where we are going in this

**[07:08]** want to know where we are going in this

**[07:08]** want to know where we are going in this current uh driving. So for example like

**[07:11]** current uh driving. So for example like

**[07:11]** current uh driving. So for example like you can think about it as a Google map

**[07:13]** you can think about it as a Google map

**[07:13]** you can think about it as a Google map signal and then it tell us you should

**[07:16]** signal and then it tell us you should

**[07:16]** signal and then it tell us you should turn left or turn right at the next

**[07:17]** turn left or turn right at the next

**[07:17]** turn left or turn right at the next intersection something like that and

**[07:19]** intersection something like that and

**[07:19]** intersection something like that and then we translate it into text just pure

**[07:22]** then we translate it into text just pure

**[07:22]** then we translate it into text just pure text. And then on the bottom left we

**[07:24]** text. And then on the bottom left we

**[07:24]** text. And then on the bottom left we have the the the vehicle with

**[07:27]** have the the the vehicle with

**[07:27]** have the the the vehicle with surrounding cameras. There are eight

**[07:29]** surrounding cameras. There are eight

**[07:29]** surrounding cameras. There are eight cameras in this image and it covers 360

**[07:32]** cameras in this image and it covers 360

**[07:32]** cameras in this image and it covers 360 degrees. And then we just input these

**[07:35]** degrees. And then we just input these

**[07:35]** degrees. And then we just input these video and the text the the routing text

**[07:38]** video and the text the the routing text

**[07:38]** video and the text the the routing text to to Emma basically built on top of

**[07:41]** to to Emma basically built on top of

**[07:41]** to to Emma basically built on top of Gemini and then we ask Gemini how to

**[07:43]** Gemini and then we ask Gemini how to

**[07:43]** Gemini and then we ask Gemini how to drive in the next scenario right so

**[07:46]** drive in the next scenario right so

**[07:46]** drive in the next scenario right so Gemini will output um future waypoints

**[07:49]** Gemini will output um future waypoints

**[07:49]** Gemini will output um future waypoints which means the future locations of this

**[07:51]** which means the future locations of this

**[07:52]** which means the future locations of this car should be in in the next few

**[07:53]** car should be in in the next few

**[07:53]** car should be in in the next few seconds. So this this method is very

**[07:58]** seconds. So this this method is very

**[07:58]** seconds. So this this method is very simple right like and there are three


### [08:00 - 09:00]

**[08:00]** simple right like and there are three

**[08:00]** simple right like and there are three major traits here. The first things is

**[08:03]** major traits here. The first things is

**[08:03]** major traits here. The first things is that it is self-supervised because

**[08:05]** that it is self-supervised because

**[08:05]** that it is self-supervised because whenever we have a driving log right we

**[08:08]** whenever we have a driving log right we

**[08:08]** whenever we have a driving log right we know where the car were. So at any time

**[08:11]** know where the car were. So at any time

**[08:11]** know where the car were. So at any time point we can use this formulation to

**[08:13]** point we can use this formulation to

**[08:13]** point we can use this formulation to trend the model because we know where

**[08:15]** trend the model because we know where

**[08:15]** trend the model because we know where the future the car should be in right.

**[08:17]** the future the car should be in right.

**[08:17]** the future the car should be in right. So this is super self-s supervised very

**[08:19]** So this is super self-s supervised very

**[08:19]** So this is super self-s supervised very scalable. The second thing is it is

**[08:22]** scalable. The second thing is it is

**[08:22]** scalable. The second thing is it is camera only. We we don't have LAR yet

**[08:24]** camera only. We we don't have LAR yet

**[08:24]** camera only. We we don't have LAR yet because you know Gemini is a camera

**[08:26]** because you know Gemini is a camera

**[08:26]** because you know Gemini is a camera model. So we only need cameras to drive.

**[08:29]** model. So we only need cameras to drive.

**[08:30]** model. So we only need cameras to drive. The third thing is that it is high

**[08:32]** The third thing is that it is high

**[08:32]** The third thing is that it is high dimension map free. I think for people

**[08:34]** dimension map free. I think for people

**[08:34]** dimension map free. I think for people who are who understand autonomous

**[08:36]** who are who understand autonomous

**[08:36]** who are who understand autonomous driving technology to certain extent

**[08:38]** driving technology to certain extent

**[08:38]** driving technology to certain extent like we usually hear that Whimo's car

**[08:40]** like we usually hear that Whimo's car

**[08:40]** like we usually hear that Whimo's car needs a lot of map prior. So in this

**[08:43]** needs a lot of map prior. So in this

**[08:43]** needs a lot of map prior. So in this model we actually don't need any maps

**[08:45]** model we actually don't need any maps

**[08:45]** model we actually don't need any maps besides Google map.

**[08:49]** besides Google map.

**[08:49]** besides Google map. So how how was the performance here? So

**[08:51]** So how how was the performance here? So

**[08:52]** So how how was the performance here? So we we basically conducted a on a

**[08:54]** we we basically conducted a on a

**[08:54]** we we basically conducted a on a research benchmark called new things.

**[08:56]** research benchmark called new things.

**[08:56]** research benchmark called new things. This is one of the most popular openloop

**[08:58]** This is one of the most popular openloop

**[08:58]** This is one of the most popular openloop planner benchmarks and for le simple


### [09:00 - 10:00]

**[09:00]** planner benchmarks and for le simple

**[09:00]** planner benchmarks and for le simple model E achieves state-of-the-art

**[09:02]** model E achieves state-of-the-art

**[09:02]** model E achieves state-of-the-art quality compared to all other models at

**[09:05]** quality compared to all other models at

**[09:05]** quality compared to all other models at that time. So basically whatever like

**[09:08]** that time. So basically whatever like

**[09:08]** that time. So basically whatever like customized model, small model, large

**[09:10]** customized model, small model, large

**[09:10]** customized model, small model, large models like with this simple formulation

**[09:13]** models like with this simple formulation

**[09:13]** models like with this simple formulation we can already achieve the best quality.

**[09:17]** we can already achieve the best quality.

**[09:17]** we can already achieve the best quality. So now we are thinking more towards like

**[09:19]** So now we are thinking more towards like

**[09:19]** So now we are thinking more towards like okay so the self-supervised method does

**[09:22]** okay so the self-supervised method does

**[09:22]** okay so the self-supervised method does work to some extent but there are a lot

**[09:25]** work to some extent but there are a lot

**[09:25]** work to some extent but there are a lot of drawbacks that we want to basically

**[09:27]** of drawbacks that we want to basically

**[09:27]** of drawbacks that we want to basically remedy right the first thing is that

**[09:30]** remedy right the first thing is that

**[09:30]** remedy right the first thing is that okay we have had a lot of label data a

**[09:33]** okay we have had a lot of label data a

**[09:33]** okay we have had a lot of label data a lot of asper models how do we leverage

**[09:35]** lot of asper models how do we leverage

**[09:35]** lot of asper models how do we leverage them to further improve the quality the

**[09:38]** them to further improve the quality the

**[09:38]** them to further improve the quality the second thing is that there is a very

**[09:41]** second thing is that there is a very

**[09:41]** second thing is that there is a very clear drawback about end toend models

**[09:43]** clear drawback about end toend models

**[09:43]** clear drawback about end toend models where the explanability is not there

**[09:47]** where the explanability is not there

**[09:47]** where the explanability is not there right like we can only see the the

**[09:49]** right like we can only see the the

**[09:49]** right like we can only see the the output of planner but we don't know what

**[09:51]** output of planner but we don't know what

**[09:51]** output of planner but we don't know what happens inside so here is what we do

**[09:54]** happens inside so here is what we do

**[09:54]** happens inside so here is what we do right we basically have a channel so

**[09:57]** right we basically have a channel so

**[09:57]** right we basically have a channel so process before outputting the the


### [10:00 - 11:00]

**[10:00]** process before outputting the the

**[10:00]** process before outputting the the planner so basically we let the model

**[10:02]** planner so basically we let the model

**[10:02]** planner so basically we let the model explain itself about how it should drive

**[10:06]** explain itself about how it should drive

**[10:06]** explain itself about how it should drive in this scenario for example we ask the

**[10:09]** in this scenario for example we ask the

**[10:09]** in this scenario for example we ask the model to identify critical objects on

**[10:12]** model to identify critical objects on

**[10:12]** model to identify critical objects on the road first in this scenario they

**[10:14]** the road first in this scenario they

**[10:14]** the road first in this scenario they identify Okay, the cyclist and the

**[10:16]** identify Okay, the cyclist and the

**[10:16]** identify Okay, the cyclist and the vehicle and then we ask them to explain

**[10:19]** vehicle and then we ask them to explain

**[10:19]** vehicle and then we ask them to explain what kind of behaviors those critical

**[10:21]** what kind of behaviors those critical

**[10:21]** what kind of behaviors those critical objects will will do and what kind of

**[10:24]** objects will will do and what kind of

**[10:24]** objects will will do and what kind of driving meta decision that we should we

**[10:26]** driving meta decision that we should we

**[10:26]** driving meta decision that we should we should go for and in this scenario it

**[10:28]** should go for and in this scenario it

**[10:28]** should go for and in this scenario it says we should just keep the normal

**[10:30]** says we should just keep the normal

**[10:30]** says we should just keep the normal speed and some of the scenario it will

**[10:32]** speed and some of the scenario it will

**[10:32]** speed and some of the scenario it will say we should yield or slow down

**[10:34]** say we should yield or slow down

**[10:34]** say we should yield or slow down something like that

**[10:36]** something like that

**[10:36]** something like that and with this we actually achieved a

**[10:39]** and with this we actually achieved a

**[10:39]** and with this we actually achieved a even better forer um it's measured in

**[10:41]** even better forer um it's measured in

**[10:42]** even better forer um it's measured in our own open motion data set at least

**[10:45]** our own open motion data set at least

**[10:45]** our own open motion data set at least lease data set is actually 100k data set

**[10:48]** lease data set is actually 100k data set

**[10:48]** lease data set is actually 100k data set about 100 times larger than the new

**[10:51]** about 100 times larger than the new

**[10:51]** about 100 times larger than the new things data set and more importantly is

**[10:53]** things data set and more importantly is

**[10:53]** things data set and more importantly is that the baselines are much stronger

**[10:55]** that the baselines are much stronger

**[10:55]** that the baselines are much stronger because they are not they they are

**[10:57]** because they are not they they are

**[10:57]** because they are not they they are specialized models they are waveformers

**[10:59]** specialized models they are waveformers


### [11:00 - 12:00]

**[11:00]** specialized models they are waveformers and motion LM so they are basically

**[11:02]** and motion LM so they are basically

**[11:02]** and motion LM so they are basically built on top of very sophisticated

**[11:05]** built on top of very sophisticated

**[11:05]** built on top of very sophisticated Oracle perception system and they takes

**[11:08]** Oracle perception system and they takes

**[11:08]** Oracle perception system and they takes inputs from from those oracle perception

**[11:11]** inputs from from those oracle perception

**[11:11]** inputs from from those oracle perception and raw graph that's basically high

**[11:13]** and raw graph that's basically high

**[11:13]** and raw graph that's basically high definitionition map and traffic light

**[11:15]** definitionition map and traffic light

**[11:15]** definitionition map and traffic light states. So they have inputs from

**[11:17]** states. So they have inputs from

**[11:18]** states. So they have inputs from everything almost and then their own job

**[11:20]** everything almost and then their own job

**[11:20]** everything almost and then their own job is to output the planner. So this is

**[11:22]** is to output the planner. So this is

**[11:22]** is to output the planner. So this is these are very strong baselines and with

**[11:25]** these are very strong baselines and with

**[11:25]** these are very strong baselines and with channel so reasoning you can see that it

**[11:27]** channel so reasoning you can see that it

**[11:28]** channel so reasoning you can see that it actually comes on top. So with this

**[11:30]** actually comes on top. So with this

**[11:30]** actually comes on top. So with this architecture we actually

**[11:33]** architecture we actually

**[11:33]** architecture we actually uh see that it actually performs very

**[11:35]** uh see that it actually performs very

**[11:35]** uh see that it actually performs very well in the academic setting.

**[11:39]** well in the academic setting.

**[11:39]** well in the academic setting. So one promise in foundation model is

**[11:41]** So one promise in foundation model is

**[11:41]** So one promise in foundation model is that you know open accreating

**[11:45]** that you know open accreating

**[11:45]** that you know open accreating laws. It basically says that the quality

**[11:48]** laws. It basically says that the quality

**[11:48]** laws. It basically says that the quality will keep improving if you have a larger

**[11:50]** will keep improving if you have a larger

**[11:50]** will keep improving if you have a larger model and larger data set. And we we we

**[11:53]** model and larger data set. And we we we

**[11:53]** model and larger data set. And we we we are showing here that if we trend like

**[11:57]** are showing here that if we trend like

**[11:57]** are showing here that if we trend like this is a data set that's magnetive

**[11:59]** this is a data set that's magnetive

**[11:59]** this is a data set that's magnetive larger than any of the academic data


### [12:00 - 13:00]

**[12:02]** larger than any of the academic data

**[12:02]** larger than any of the academic data sets that's released publicly. And we

**[12:05]** sets that's released publicly. And we

**[12:05]** sets that's released publicly. And we see that if we keep trending more data

**[12:08]** see that if we keep trending more data

**[12:08]** see that if we keep trending more data and we see the quality keeps improving.

**[12:11]** and we see the quality keeps improving.

**[12:11]** and we see the quality keeps improving. So the the y-axis is the complexity

**[12:13]** So the the y-axis is the complexity

**[12:13]** So the the y-axis is the complexity here. So it basically means that the

**[12:15]** here. So it basically means that the

**[12:15]** here. So it basically means that the lower the proplexity the better the

**[12:17]** lower the proplexity the better the

**[12:17]** lower the proplexity the better the planner results. So we see the quality

**[12:20]** planner results. So we see the quality

**[12:20]** planner results. So we see the quality can can be further improved.

**[12:24]** can can be further improved.

**[12:24]** can can be further improved. So um we talk about the expulability

**[12:27]** So um we talk about the expulability

**[12:28]** So um we talk about the expulability here and one thing that we also are

**[12:31]** here and one thing that we also are

**[12:31]** here and one thing that we also are thinking about is that uh why not just

**[12:34]** thinking about is that uh why not just

**[12:34]** thinking about is that uh why not just train on various tasks right like

**[12:37]** train on various tasks right like

**[12:37]** train on various tasks right like because it is a vision language models

**[12:40]** because it is a vision language models

**[12:40]** because it is a vision language models at the core and the language part is

**[12:43]** at the core and the language part is

**[12:43]** at the core and the language part is super flexible we can basically

**[12:45]** super flexible we can basically

**[12:45]** super flexible we can basically formulate any types of tasks with it.

**[12:48]** formulate any types of tasks with it.

**[12:48]** formulate any types of tasks with it. So, so we think about like let's make

**[12:50]** So, so we think about like let's make

**[12:50]** So, so we think about like let's make Emma the most generalizable model

**[12:53]** Emma the most generalizable model

**[12:53]** Emma the most generalizable model possible, right? So, we add a lot of

**[12:55]** possible, right? So, we add a lot of

**[12:55]** possible, right? So, we add a lot of different tasks into it. Uh, in this

**[12:57]** different tasks into it. Uh, in this

**[12:57]** different tasks into it. Uh, in this example, we we demonstrate 3D detection,


### [13:00 - 14:00]

**[13:00]** example, we we demonstrate 3D detection,

**[13:00]** example, we we demonstrate 3D detection, rograph estimation and some kind of free

**[13:03]** rograph estimation and some kind of free

**[13:03]** rograph estimation and some kind of free form VQA here. And for any prompt on the

**[13:07]** form VQA here. And for any prompt on the

**[13:07]** form VQA here. And for any prompt on the left, uh, if you enter it, then Emma

**[13:10]** left, uh, if you enter it, then Emma

**[13:10]** left, uh, if you enter it, then Emma will speed out the answers

**[13:11]** will speed out the answers

**[13:12]** will speed out the answers correspondingly. So it will have the

**[13:14]** correspondingly. So it will have the

**[13:14]** correspondingly. So it will have the first one is the the end driving the

**[13:17]** first one is the the end driving the

**[13:17]** first one is the the end driving the second one is 3D detection etc. And then

**[13:19]** second one is 3D detection etc. And then

**[13:19]** second one is 3D detection etc. And then we decode and visualize the results on

**[13:21]** we decode and visualize the results on

**[13:21]** we decode and visualize the results on the right.

**[13:23]** the right.

**[13:23]** the right. So we also measure the the detection

**[13:26]** So we also measure the the detection

**[13:26]** So we also measure the the detection quality here on our way more open data

**[13:28]** quality here on our way more open data

**[13:28]** quality here on our way more open data set. So it actually achieves very

**[13:31]** set. So it actually achieves very

**[13:31]** set. So it actually achieves very similar quality compared to other

**[13:33]** similar quality compared to other

**[13:33]** similar quality compared to other state-of-the-art models. So this

**[13:35]** state-of-the-art models. So this

**[13:35]** state-of-the-art models. So this demonstrates the AMAS capability um

**[13:38]** demonstrates the AMAS capability um

**[13:38]** demonstrates the AMAS capability um generalizing different tasks and coin

**[13:40]** generalizing different tasks and coin

**[13:40]** generalizing different tasks and coin them together.

**[13:43]** them together.

**[13:43]** them together. So here here are some visualization of

**[13:45]** So here here are some visualization of

**[13:45]** So here here are some visualization of the AAS outputs including the driving

**[13:48]** the AAS outputs including the driving

**[13:48]** the AAS outputs including the driving trajectory detection and RO graph. So I

**[13:50]** trajectory detection and RO graph. So I

**[13:50]** trajectory detection and RO graph. So I think the the predictions are reasonably

**[13:53]** think the the predictions are reasonably

**[13:54]** think the the predictions are reasonably well.

**[13:59]** So now it seems like we have um some

**[13:59]** So now it seems like we have um some kind of prototype for for end to end


### [14:00 - 15:00]

**[14:02]** kind of prototype for for end to end

**[14:02]** kind of prototype for for end to end multimodel large language models. But

**[14:05]** multimodel large language models. But

**[14:05]** multimodel large language models. But then the question comes next is about

**[14:07]** then the question comes next is about

**[14:07]** then the question comes next is about how we evaluate it, validate the version

**[14:11]** how we evaluate it, validate the version

**[14:11]** how we evaluate it, validate the version and make sure that it's safe. So

**[14:12]** and make sure that it's safe. So

**[14:12]** and make sure that it's safe. So evaluation is part of you know the the

**[14:16]** evaluation is part of you know the the

**[14:16]** evaluation is part of you know the the entire solution right we cannot really

**[14:19]** entire solution right we cannot really

**[14:19]** entire solution right we cannot really make make this model succeed without any

**[14:21]** make make this model succeed without any

**[14:21]** make make this model succeed without any evaluation

**[14:23]** evaluation

**[14:23]** evaluation and this for evaluation previously all

**[14:25]** and this for evaluation previously all

**[14:25]** and this for evaluation previously all the results I showed was about open loop

**[14:29]** the results I showed was about open loop

**[14:29]** the results I showed was about open loop evaluation which means that we just

**[14:31]** evaluation which means that we just

**[14:31]** evaluation which means that we just replay the video and then see the check

**[14:33]** replay the video and then see the check

**[14:33]** replay the video and then see the check the model quality but this is usually

**[14:36]** the model quality but this is usually

**[14:36]** the model quality but this is usually not the most faithful way to to to do

**[14:39]** not the most faithful way to to to do

**[14:39]** not the most faithful way to to to do evaluation so there are simulations

**[14:42]** evaluation so there are simulations

**[14:42]** evaluation so there are simulations and real world testing and simulation

**[14:45]** and real world testing and simulation

**[14:45]** and real world testing and simulation means that we create a a virtual world

**[14:48]** means that we create a a virtual world

**[14:48]** means that we create a a virtual world where we can test our model to drive the

**[14:50]** where we can test our model to drive the

**[14:50]** where we can test our model to drive the car in that world and real world testing

**[14:53]** car in that world and real world testing

**[14:53]** car in that world and real world testing is just deploying it. So the

**[14:55]** is just deploying it. So the

**[14:55]** is just deploying it. So the difficulties are different and usually

**[14:57]** difficulties are different and usually

**[14:57]** difficulties are different and usually we trust simulation a lot more compared


### [15:00 - 16:00]

**[15:01]** we trust simulation a lot more compared

**[15:01]** we trust simulation a lot more compared to open world.

**[15:04]** to open world.

**[15:04]** to open world. So one thing that we are also thinking

**[15:05]** So one thing that we are also thinking

**[15:06]** So one thing that we are also thinking about is that yes foundation models in

**[15:08]** about is that yes foundation models in

**[15:08]** about is that yes foundation models in the generative warrior is also very

**[15:11]** the generative warrior is also very

**[15:11]** the generative warrior is also very advanced. This is a V2 from Google deep

**[15:14]** advanced. This is a V2 from Google deep

**[15:14]** advanced. This is a V2 from Google deep mind where we see the videos generated

**[15:16]** mind where we see the videos generated

**[15:16]** mind where we see the videos generated are very realistic. So we are also

**[15:18]** are very realistic. So we are also

**[15:18]** are very realistic. So we are also thinking about maybe we can leverage it

**[15:21]** thinking about maybe we can leverage it

**[15:21]** thinking about maybe we can leverage it for simulation. So this is also like our

**[15:26]** for simulation. So this is also like our

**[15:26]** for simulation. So this is also like our latest research um sensor simulation for

**[15:28]** latest research um sensor simulation for

**[15:28]** latest research um sensor simulation for end to end driving evaluation. So for

**[15:31]** end to end driving evaluation. So for

**[15:31]** end to end driving evaluation. So for this model we actually use a

**[15:32]** this model we actually use a

**[15:32]** this model we actually use a open-sourced

**[15:34]** open-sourced

**[15:34]** open-sourced um generative models from Google and

**[15:37]** um generative models from Google and

**[15:37]** um generative models from Google and then we generate the the the videos and

**[15:40]** then we generate the the the videos and

**[15:40]** then we generate the the the videos and then we use that to basically place our

**[15:42]** then we use that to basically place our

**[15:42]** then we use that to basically place our AMI and then we can evaluate the the

**[15:45]** AMI and then we can evaluate the the

**[15:45]** AMI and then we can evaluate the the quality and we can also control in

**[15:48]** quality and we can also control in

**[15:48]** quality and we can also control in various conditions like we can change

**[15:50]** various conditions like we can change

**[15:50]** various conditions like we can change the weather, we can change the time, we

**[15:52]** the weather, we can change the time, we

**[15:52]** the weather, we can change the time, we can change a lot of different ways. uh

**[15:54]** can change a lot of different ways. uh

**[15:54]** can change a lot of different ways. uh due to time I basically removed those

**[15:57]** due to time I basically removed those

**[15:57]** due to time I basically removed those videos. So sorry about that the visual


### [16:00 - 17:00]

**[16:00]** videos. So sorry about that the visual

**[16:00]** videos. So sorry about that the visual part. So this is the results where we

**[16:02]** part. So this is the results where we

**[16:02]** part. So this is the results where we can test our MAR planner in various

**[16:05]** can test our MAR planner in various

**[16:05]** can test our MAR planner in various conditions right we can switch from RAN

**[16:08]** conditions right we can switch from RAN

**[16:08]** conditions right we can switch from RAN to no RAN we can switch different time

**[16:10]** to no RAN we can switch different time

**[16:10]** to no RAN we can switch different time in day and this is very much like

**[16:16]** in day and this is very much like

**[16:16]** in day and this is very much like um aligns with our intuition where when

**[16:19]** um aligns with our intuition where when

**[16:19]** um aligns with our intuition where when it rains when the weather is bad then

**[16:22]** it rains when the weather is bad then

**[16:22]** it rains when the weather is bad then usually our planner gets a little bit

**[16:24]** usually our planner gets a little bit

**[16:24]** usually our planner gets a little bit worse because it's it's a camera only

**[16:26]** worse because it's it's a camera only

**[16:26]** worse because it's it's a camera only model so it it affects the camera domain

**[16:29]** model so it it affects the camera domain

**[16:29]** model so it it affects the camera domain and then for time of day is also kind of

**[16:32]** and then for time of day is also kind of

**[16:32]** and then for time of day is also kind of a lines where uh at night usually the

**[16:35]** a lines where uh at night usually the

**[16:35]** a lines where uh at night usually the quality is worse compared in the in the

**[16:37]** quality is worse compared in the in the

**[16:37]** quality is worse compared in the in the daytime. So usually at noon or at in the

**[16:40]** daytime. So usually at noon or at in the

**[16:40]** daytime. So usually at noon or at in the afternoon the model will perform the

**[16:42]** afternoon the model will perform the

**[16:42]** afternoon the model will perform the best.

**[16:44]** best.

**[16:44]** best. So this is the last slides. So these are

**[16:46]** So this is the last slides. So these are

**[16:46]** So this is the last slides. So these are all generated videos that we we we test

**[16:49]** all generated videos that we we we test

**[16:49]** all generated videos that we we we test our models in. So I think this is a

**[16:52]** our models in. So I think this is a

**[16:52]** our models in. So I think this is a ongoing research where I I think it's a

**[16:55]** ongoing research where I I think it's a

**[16:55]** ongoing research where I I think it's a very exciting field where we have all

**[16:57]** very exciting field where we have all

**[16:57]** very exciting field where we have all the foundation models and because Whimo


### [17:00 - 18:00]

**[17:00]** the foundation models and because Whimo

**[17:00]** the foundation models and because Whimo and Google are both belongs to alphabet

**[17:03]** and Google are both belongs to alphabet

**[17:03]** and Google are both belongs to alphabet so we get to act get access to all these

**[17:06]** so we get to act get access to all these

**[17:06]** so we get to act get access to all these models for free sort of. Yeah. So so we

**[17:09]** models for free sort of. Yeah. So so we

**[17:09]** models for free sort of. Yeah. So so we we basically try to adapt them and try

**[17:12]** we basically try to adapt them and try

**[17:12]** we basically try to adapt them and try to see if we can improve the

**[17:13]** to see if we can improve the

**[17:13]** to see if we can improve the generalization and and help Whimo to

**[17:16]** generalization and and help Whimo to

**[17:16]** generalization and and help Whimo to scale to the next big thing. So thank

**[17:19]** scale to the next big thing. So thank

**[17:19]** scale to the next big thing. So thank you. Thank you for your attention.

**[17:22]** you. Thank you for your attention.

**[17:22]** you. Thank you for your attention. [Music]


