# What Is a Humanoid Foundation Model An Introduction to GR00T N1 - Annika & Aastha

**Video URL:** https://www.youtube.com/watch?v=mWKYvT9Lc50

---

## Full Transcript

### [00:00 - 01:00]

**[00:18]** Hi everyone, I'm Anaka. Uh this is

**[00:18]** Hi everyone, I'm Anaka. Uh this is Austa. We both work at Advidia and we

**[00:20]** Austa. We both work at Advidia and we

**[00:20]** Austa. We both work at Advidia and we were part of the team that developed the

**[00:21]** were part of the team that developed the

**[00:21]** were part of the team that developed the GR 101 uh robotics foundation model. So

**[00:25]** GR 101 uh robotics foundation model. So

**[00:25]** GR 101 uh robotics foundation model. So today we're going to give you a sense of

**[00:26]** today we're going to give you a sense of

**[00:26]** today we're going to give you a sense of what that is and and how you go about

**[00:28]** what that is and and how you go about

**[00:28]** what that is and and how you go about building a robotics foundation model.

**[00:31]** building a robotics foundation model.

**[00:31]** building a robotics foundation model. But before we get into it, uh I feel

**[00:33]** But before we get into it, uh I feel

**[00:33]** But before we get into it, uh I feel like a lot of people start talks here

**[00:35]** like a lot of people start talks here

**[00:35]** like a lot of people start talks here with a hot take. Uh so the hot take that

**[00:37]** with a hot take. Uh so the hot take that

**[00:37]** with a hot take. Uh so the hot take that I'm bringing to an AI conference is that

**[00:40]** I'm bringing to an AI conference is that

**[00:40]** I'm bringing to an AI conference is that we're not necessarily running out of

**[00:42]** we're not necessarily running out of

**[00:42]** we're not necessarily running out of jobs. Uh so this was a report done by

**[00:44]** jobs. Uh so this was a report done by

**[00:44]** jobs. Uh so this was a report done by McKenzie uh part of their global

**[00:46]** McKenzie uh part of their global

**[00:46]** McKenzie uh part of their global institute showing that in the world's 30

**[00:49]** institute showing that in the world's 30

**[00:49]** institute showing that in the world's 30 uh most advanced economies there's

**[00:52]** uh most advanced economies there's

**[00:52]** uh most advanced economies there's actually too many jobs uh for the number

**[00:54]** actually too many jobs uh for the number

**[00:54]** actually too many jobs uh for the number of people that could fill them and

**[00:56]** of people that could fill them and

**[00:56]** of people that could fill them and really the two things you should look at

**[00:57]** really the two things you should look at

**[00:58]** really the two things you should look at in this whole graph is the 4.2x 2x.


### [01:00 - 02:00]

**[01:00]** in this whole graph is the 4.2x 2x.

**[01:00]** in this whole graph is the 4.2x 2x. That's been the the rate at which we're

**[01:02]** That's been the the rate at which we're

**[01:02]** That's been the the rate at which we're getting more jobs than people could fill

**[01:03]** getting more jobs than people could fill

**[01:03]** getting more jobs than people could fill it over the last decade. And this line

**[01:06]** it over the last decade. And this line

**[01:06]** it over the last decade. And this line that I'm highlighting in red, that's

**[01:08]** that I'm highlighting in red, that's

**[01:08]** that I'm highlighting in red, that's where we're in trouble, where there's

**[01:09]** where we're in trouble, where there's

**[01:09]** where we're in trouble, where there's just more jobs than able-bodied people

**[01:11]** just more jobs than able-bodied people

**[01:11]** just more jobs than able-bodied people to fill those jobs. Uh, and obviously uh

**[01:14]** to fill those jobs. Uh, and obviously uh

**[01:14]** to fill those jobs. Uh, and obviously uh there's a real conversation around AI

**[01:16]** there's a real conversation around AI

**[01:16]** there's a real conversation around AI and jobs. So, it helps to look at what

**[01:18]** and jobs. So, it helps to look at what

**[01:18]** and jobs. So, it helps to look at what industries uh are largely affected. I'm

**[01:22]** industries uh are largely affected. I'm

**[01:22]** industries uh are largely affected. I'm going to highlight a couple in red. So

**[01:24]** going to highlight a couple in red. So

**[01:24]** going to highlight a couple in red. So leisure, hospitality, healthcare,

**[01:27]** leisure, hospitality, healthcare,

**[01:27]** leisure, hospitality, healthcare, construction, transportation,

**[01:28]** construction, transportation,

**[01:28]** construction, transportation, manufacturing. Um I I guess you can

**[01:32]** manufacturing. Um I I guess you can

**[01:32]** manufacturing. Um I I guess you can figure out what they have in common.

**[01:34]** figure out what they have in common.

**[01:34]** figure out what they have in common. None of them can be solved by chat GPT

**[01:36]** None of them can be solved by chat GPT

**[01:36]** None of them can be solved by chat GPT alone. Uh they require operating

**[01:39]** alone. Uh they require operating

**[01:39]** alone. Uh they require operating instruments uh and devices in the

**[01:41]** instruments uh and devices in the

**[01:42]** instruments uh and devices in the physical world. Uh and they require

**[01:44]** physical world. Uh and they require

**[01:44]** physical world. Uh and they require physical AI. So that's that's really the

**[01:46]** physical AI. So that's that's really the

**[01:46]** physical AI. So that's that's really the big challenge uh that I see over the

**[01:48]** big challenge uh that I see over the

**[01:48]** big challenge uh that I see over the coming years is how do we take this huge

**[01:50]** coming years is how do we take this huge

**[01:50]** coming years is how do we take this huge amount of intelligence that we're seeing

**[01:52]** amount of intelligence that we're seeing

**[01:52]** amount of intelligence that we're seeing in language models um and make it

**[01:54]** in language models um and make it

**[01:54]** in language models um and make it operable in the in the physical world.

**[01:57]** operable in the in the physical world.

**[01:57]** operable in the in the physical world. The other question around humanoids is

**[01:59]** The other question around humanoids is

**[01:59]** The other question around humanoids is why do we build them to look like


### [02:00 - 03:00]

**[02:01]** why do we build them to look like

**[02:01]** why do we build them to look like humans? Um it's not just because we want

**[02:03]** humans? Um it's not just because we want

**[02:03]** humans? Um it's not just because we want them to look like us. The world was made

**[02:05]** them to look like us. The world was made

**[02:06]** them to look like us. The world was made for humans. Uh it's very hard to have

**[02:08]** for humans. Uh it's very hard to have

**[02:08]** for humans. Uh it's very hard to have generalist robots operate in our world

**[02:10]** generalist robots operate in our world

**[02:10]** generalist robots operate in our world and be generally useful uh without

**[02:14]** and be generally useful uh without

**[02:14]** and be generally useful uh without copying our physical form. Uh there's a

**[02:16]** copying our physical form. Uh there's a

**[02:16]** copying our physical form. Uh there's a lot of specialist robots that do

**[02:17]** lot of specialist robots that do

**[02:18]** lot of specialist robots that do incredible things. I don't know if you

**[02:19]** incredible things. I don't know if you

**[02:19]** incredible things. I don't know if you got to try the espresso uh from the

**[02:21]** got to try the espresso uh from the

**[02:21]** got to try the espresso uh from the barista robot downstairs makes a good

**[02:23]** barista robot downstairs makes a good

**[02:23]** barista robot downstairs makes a good espresso. Uh but that robot couldn't

**[02:25]** espresso. Uh but that robot couldn't

**[02:25]** espresso. Uh but that robot couldn't even cook rice. So if we want a robot

**[02:28]** even cook rice. So if we want a robot

**[02:28]** even cook rice. So if we want a robot that can do multiple tasks for you, um

**[02:30]** that can do multiple tasks for you, um

**[02:30]** that can do multiple tasks for you, um it's just a lot easier to try and

**[02:32]** it's just a lot easier to try and

**[02:32]** it's just a lot easier to try and imagine that that robot uh can operate

**[02:35]** imagine that that robot uh can operate

**[02:35]** imagine that that robot uh can operate in in our human world.

**[02:37]** in in our human world.

**[02:37]** in in our human world. So how do we do this? There's three big

**[02:39]** So how do we do this? There's three big

**[02:39]** So how do we do this? There's three big buckets, three big stages. First one is

**[02:42]** buckets, three big stages. First one is

**[02:42]** buckets, three big stages. First one is data collecting or generating or

**[02:44]** data collecting or generating or

**[02:44]** data collecting or generating or multiplying data, which we'll talk quite

**[02:46]** multiplying data, which we'll talk quite

**[02:46]** multiplying data, which we'll talk quite a lot about. Um and now that you have

**[02:48]** a lot about. Um and now that you have

**[02:48]** a lot about. Um and now that you have this synthetic and and real data, but

**[02:51]** this synthetic and and real data, but

**[02:51]** this synthetic and and real data, but largely synthetic data, uh you train a

**[02:53]** largely synthetic data, uh you train a

**[02:53]** largely synthetic data, uh you train a model. We'll also talk about what that

**[02:56]** model. We'll also talk about what that

**[02:56]** model. We'll also talk about what that architecture and training paradigm looks

**[02:58]** architecture and training paradigm looks

**[02:58]** architecture and training paradigm looks like. And then finally, we deploy uh on


### [03:00 - 04:00]

**[03:01]** like. And then finally, we deploy uh on

**[03:01]** like. And then finally, we deploy uh on the robot uh or at the edge. Uh this is

**[03:04]** the robot uh or at the edge. Uh this is

**[03:04]** the robot uh or at the edge. Uh this is what we call the physical AI life cycle.

**[03:07]** what we call the physical AI life cycle.

**[03:07]** what we call the physical AI life cycle. So generate the data, consume the data

**[03:10]** So generate the data, consume the data

**[03:10]** So generate the data, consume the data and then finally deploy and um have this

**[03:12]** and then finally deploy and um have this

**[03:12]** and then finally deploy and um have this robot operable in the physical world.

**[03:15]** robot operable in the physical world.

**[03:15]** robot operable in the physical world. Nvidia also likes to call this the three

**[03:17]** Nvidia also likes to call this the three

**[03:17]** Nvidia also likes to call this the three computer problem because they have very

**[03:19]** computer problem because they have very

**[03:19]** computer problem because they have very different compute characteristics. So at

**[03:22]** different compute characteristics. So at

**[03:22]** different compute characteristics. So at the simulation stage, you're looking for

**[03:24]** the simulation stage, you're looking for

**[03:24]** the simulation stage, you're looking for a computer that's powerful at simulating

**[03:26]** a computer that's powerful at simulating

**[03:26]** a computer that's powerful at simulating something like an OVX Omniverse machine.

**[03:28]** something like an OVX Omniverse machine.

**[03:28]** something like an OVX Omniverse machine. Um there's a lot of really interesting

**[03:30]** Um there's a lot of really interesting

**[03:30]** Um there's a lot of really interesting work happening on the simulation side,

**[03:32]** work happening on the simulation side,

**[03:32]** work happening on the simulation side, but that has a very different type of uh

**[03:35]** but that has a very different type of uh

**[03:35]** but that has a very different type of uh workload than when we're training and

**[03:37]** workload than when we're training and

**[03:37]** workload than when we're training and we're using a DGX to just consume this

**[03:39]** we're using a DGX to just consume this

**[03:39]** we're using a DGX to just consume this enormous amounts of data and and learn

**[03:41]** enormous amounts of data and and learn

**[03:41]** enormous amounts of data and and learn learn from that. And then finally, when

**[03:43]** learn from that. And then finally, when

**[03:43]** learn from that. And then finally, when we're deploying at the edge, it needs to

**[03:45]** we're deploying at the edge, it needs to

**[03:45]** we're deploying at the edge, it needs to be a model that's small enough and

**[03:46]** be a model that's small enough and

**[03:46]** be a model that's small enough and efficient enough uh to run on an edge

**[03:49]** efficient enough uh to run on an edge

**[03:49]** efficient enough uh to run on an edge edge device uh like an AGX. Um and

**[03:53]** edge device uh like an AGX. Um and

**[03:53]** edge device uh like an AGX. Um and really this is this is project root. So

**[03:55]** really this is this is project root. So

**[03:55]** really this is this is project root. So project root is Nvidia's strategy uh for

**[03:58]** project root is Nvidia's strategy uh for

**[03:58]** project root is Nvidia's strategy uh for bringing humanoid and other forms of


### [04:00 - 05:00]

**[04:00]** bringing humanoid and other forms of

**[04:00]** bringing humanoid and other forms of robotics into the world. And it's

**[04:02]** robotics into the world. And it's

**[04:02]** robotics into the world. And it's everything from the compute

**[04:04]** everything from the compute

**[04:04]** everything from the compute infrastructure to the software to the

**[04:06]** infrastructure to the software to the

**[04:06]** infrastructure to the software to the research that's needed. It's not simply

**[04:08]** research that's needed. It's not simply

**[04:08]** research that's needed. It's not simply um just one foundation model but that is

**[04:11]** um just one foundation model but that is

**[04:11]** um just one foundation model but that is what we'll be f focusing on in this talk

**[04:13]** what we'll be f focusing on in this talk

**[04:13]** what we'll be f focusing on in this talk because uh that's what what we worked

**[04:15]** because uh that's what what we worked

**[04:15]** because uh that's what what we worked on. Uh so the group N1 foundation model

**[04:18]** on. Uh so the group N1 foundation model

**[04:18]** on. Uh so the group N1 foundation model was announced at GTC and match uh it is

**[04:20]** was announced at GTC and match uh it is

**[04:20]** was announced at GTC and match uh it is open source uh it is highly customizable

**[04:24]** open source uh it is highly customizable

**[04:24]** open source uh it is highly customizable um and a very big part of it that is

**[04:26]** um and a very big part of it that is

**[04:26]** um and a very big part of it that is cross embodiment. So basically you can

**[04:27]** cross embodiment. So basically you can

**[04:27]** cross embodiment. So basically you can take this base model uh there's specific

**[04:29]** take this base model uh there's specific

**[04:29]** take this base model uh there's specific embodiment that we have fine-tuned for

**[04:32]** embodiment that we have fine-tuned for

**[04:32]** embodiment that we have fine-tuned for uh but the whole premise is that you can

**[04:34]** uh but the whole premise is that you can

**[04:34]** uh but the whole premise is that you can take this base model it's a two billion

**[04:35]** take this base model it's a two billion

**[04:35]** take this base model it's a two billion parameter model which in the world of

**[04:37]** parameter model which in the world of

**[04:37]** parameter model which in the world of LLM is tiny but still pretty sizable for

**[04:40]** LLM is tiny but still pretty sizable for

**[04:40]** LLM is tiny but still pretty sizable for a robot um and then go and go and

**[04:42]** a robot um and then go and go and

**[04:42]** a robot um and then go and go and modified it for your embodiment your use

**[04:44]** modified it for your embodiment your use

**[04:44]** modified it for your embodiment your use cases. So let's start with the first

**[04:47]** cases. So let's start with the first

**[04:47]** cases. So let's start with the first huge daunting task in the world of

**[04:50]** huge daunting task in the world of

**[04:50]** huge daunting task in the world of robotics data. Um when when the group

**[04:53]** robotics data. Um when when the group

**[04:53]** robotics data. Um when when the group team actually started thinking about

**[04:55]** team actually started thinking about

**[04:55]** team actually started thinking about data uh they put together this idea of

**[04:57]** data uh they put together this idea of

**[04:57]** data uh they put together this idea of the data pyramid which is very elegant

**[04:59]** the data pyramid which is very elegant

**[04:59]** the data pyramid which is very elegant but it was born out of desperation and


### [05:00 - 06:00]

**[05:02]** but it was born out of desperation and

**[05:02]** but it was born out of desperation and necessity. Um the data you want does not

**[05:04]** necessity. Um the data you want does not

**[05:04]** necessity. Um the data you want does not exist in quantities. There's no there is

**[05:07]** exist in quantities. There's no there is

**[05:07]** exist in quantities. There's no there is no internet scale uh data set to scrape

**[05:10]** no internet scale uh data set to scrape

**[05:10]** no internet scale uh data set to scrape or download or put together because uh

**[05:12]** or download or put together because uh

**[05:12]** or download or put together because uh robots h haven't made it YouTube yet. Uh

**[05:15]** robots h haven't made it YouTube yet. Uh

**[05:15]** robots h haven't made it YouTube yet. Uh so really at the top of the pyramid we

**[05:17]** so really at the top of the pyramid we

**[05:17]** so really at the top of the pyramid we have the real world data which is robots

**[05:19]** have the real world data which is robots

**[05:19]** have the real world data which is robots doing things real robots doing real

**[05:21]** doing things real robots doing real

**[05:21]** doing things real robots doing real tasks and solving them. Um and how it's

**[05:23]** tasks and solving them. Um and how it's

**[05:23]** tasks and solving them. Um and how it's collected is humans teleoperate a robot

**[05:26]** collected is humans teleoperate a robot

**[05:26]** collected is humans teleoperate a robot most of the time. So wearing uh like an

**[05:29]** most of the time. So wearing uh like an

**[05:29]** most of the time. So wearing uh like an Apple vision pro and wearing gloves.

**[05:31]** Apple vision pro and wearing gloves.

**[05:31]** Apple vision pro and wearing gloves. There's all kinds of ways to tell

**[05:32]** There's all kinds of ways to tell

**[05:32]** There's all kinds of ways to tell operate the robot where you have a real

**[05:34]** operate the robot where you have a real

**[05:34]** operate the robot where you have a real robot successfully completing a task and

**[05:37]** robot successfully completing a task and

**[05:37]** robot successfully completing a task and then you have that ground truth data. So

**[05:39]** then you have that ground truth data. So

**[05:39]** then you have that ground truth data. So you can imagine this is very small in

**[05:41]** you can imagine this is very small in

**[05:41]** you can imagine this is very small in quantity, very expensive. Um, and we put

**[05:45]** quantity, very expensive. Um, and we put

**[05:45]** quantity, very expensive. Um, and we put 24 hours per robot per day because

**[05:47]** 24 hours per robot per day because

**[05:47]** 24 hours per robot per day because that's how many hours a human has. But

**[05:49]** that's how many hours a human has. But

**[05:49]** that's how many hours a human has. But the reality is that humans and robots

**[05:51]** the reality is that humans and robots

**[05:51]** the reality is that humans and robots get tired. Uh, so it's not even 24

**[05:53]** get tired. Uh, so it's not even 24

**[05:53]** get tired. Uh, so it's not even 24 hours. Uh, so really this is is very

**[05:56]** hours. Uh, so really this is is very

**[05:56]** hours. Uh, so really this is is very very limited data set. Uh, and then at

**[05:58]** very limited data set. Uh, and then at

**[05:58]** very limited data set. Uh, and then at the bottom of the pyramid we have the


### [06:00 - 07:00]

**[06:00]** the bottom of the pyramid we have the

**[06:00]** the bottom of the pyramid we have the internet. So we have huge amounts of

**[06:02]** internet. So we have huge amounts of

**[06:02]** internet. So we have huge amounts of video data and it's typically human

**[06:05]** video data and it's typically human

**[06:05]** video data and it's typically human solving tasks. So you can imagine

**[06:07]** solving tasks. So you can imagine

**[06:07]** solving tasks. So you can imagine someone collecting a cooking video

**[06:09]** someone collecting a cooking video

**[06:09]** someone collecting a cooking video tutorial uh and putting that out there.

**[06:11]** tutorial uh and putting that out there.

**[06:12]** tutorial uh and putting that out there. Uh but this unstructured data, it's not

**[06:13]** Uh but this unstructured data, it's not

**[06:13]** Uh but this unstructured data, it's not necessarily relevant to robots. Um but

**[06:17]** necessarily relevant to robots. Um but

**[06:17]** necessarily relevant to robots. Um but there is some value in that. So we we

**[06:19]** there is some value in that. So we we

**[06:19]** there is some value in that. So we we didn't want to completely discard it. It

**[06:21]** didn't want to completely discard it. It

**[06:21]** didn't want to completely discard it. It forms part of this cohesive data

**[06:22]** forms part of this cohesive data

**[06:22]** forms part of this cohesive data strategy. Uh and then in the middle,

**[06:25]** strategy. Uh and then in the middle,

**[06:25]** strategy. Uh and then in the middle, synthetic data. uh and this is this is a

**[06:28]** synthetic data. uh and this is this is a

**[06:28]** synthetic data. uh and this is this is a topic that could fill this whole entire

**[06:30]** topic that could fill this whole entire

**[06:30]** topic that could fill this whole entire talk and I've cut down so many slides on

**[06:33]** talk and I've cut down so many slides on

**[06:33]** talk and I've cut down so many slides on on just this section because in theory

**[06:36]** on just this section because in theory

**[06:36]** on just this section because in theory this is infinite right you could just

**[06:38]** this is infinite right you could just

**[06:38]** this is infinite right you could just let the GPU keep generating more data um

**[06:40]** let the GPU keep generating more data um

**[06:40]** let the GPU keep generating more data um but in practice creating high quality

**[06:43]** but in practice creating high quality

**[06:43]** but in practice creating high quality simulation environments is very labor

**[06:46]** simulation environments is very labor

**[06:46]** simulation environments is very labor intensive and it requires serious skill

**[06:48]** intensive and it requires serious skill

**[06:48]** intensive and it requires serious skill um and then on top of that uh the other

**[06:51]** um and then on top of that uh the other

**[06:51]** um and then on top of that uh the other technique which I will share a little

**[06:53]** technique which I will share a little

**[06:53]** technique which I will share a little bit about oh sorry let me go one back uh

**[06:56]** bit about oh sorry let me go one back uh

**[06:56]** bit about oh sorry let me go one back uh is is taking the human trajectories that

**[06:59]** is is taking the human trajectories that

**[06:59]** is is taking the human trajectories that we do collect so human teleoperation


### [07:00 - 08:00]

**[07:01]** we do collect so human teleoperation

**[07:01]** we do collect so human teleoperation data and trying to multiply it um

**[07:04]** data and trying to multiply it um

**[07:04]** data and trying to multiply it um through essentially video generation

**[07:06]** through essentially video generation

**[07:06]** through essentially video generation models. So through world foundation

**[07:08]** models. So through world foundation

**[07:08]** models. So through world foundation models that we fine-tune to do this

**[07:09]** models that we fine-tune to do this

**[07:09]** models that we fine-tune to do this task. Uh but even in that case there's

**[07:11]** task. Uh but even in that case there's

**[07:11]** task. Uh but even in that case there's there's a lot of active research in how

**[07:13]** there's a lot of active research in how

**[07:13]** there's a lot of active research in how we take the little bits of high quality

**[07:16]** we take the little bits of high quality

**[07:16]** we take the little bits of high quality data that we have and multiply it as

**[07:18]** data that we have and multiply it as

**[07:18]** data that we have and multiply it as well as how we effectively combine

**[07:22]** well as how we effectively combine

**[07:22]** well as how we effectively combine simulation data with this real world

**[07:23]** simulation data with this real world

**[07:24]** simulation data with this real world data. Uh so this is dream genen. This

**[07:25]** data. Uh so this is dream genen. This

**[07:25]** data. Uh so this is dream genen. This was something that was announced at

**[07:27]** was something that was announced at

**[07:27]** was something that was announced at Computex uh very recently. Uh all in

**[07:30]** Computex uh very recently. Uh all in

**[07:30]** Computex uh very recently. Uh all in all, this data piece is a huge part of

**[07:33]** all, this data piece is a huge part of

**[07:33]** all, this data piece is a huge part of what the project group is about. Um so

**[07:36]** what the project group is about. Um so

**[07:36]** what the project group is about. Um so there's many many solutions here in

**[07:38]** there's many many solutions here in

**[07:38]** there's many many solutions here in terms of the teab uh and the data

**[07:40]** terms of the teab uh and the data

**[07:40]** terms of the teab uh and the data strategy. But for now the next piece is

**[07:43]** strategy. But for now the next piece is

**[07:43]** strategy. But for now the next piece is how do we bring all this data into an

**[07:44]** how do we bring all this data into an

**[07:44]** how do we bring all this data into an architecture. Uh so I'm going to hand

**[07:46]** architecture. Uh so I'm going to hand

**[07:46]** architecture. Uh so I'm going to hand over to AA to explain that. B thank you

**[07:48]** over to AA to explain that. B thank you

**[07:48]** over to AA to explain that. B thank you Anukica. Um do you guys hear me? All

**[07:51]** Anukica. Um do you guys hear me? All

**[07:51]** Anukica. Um do you guys hear me? All right. Awesome. Uh so before we dive

**[07:54]** right. Awesome. Uh so before we dive

**[07:54]** right. Awesome. Uh so before we dive into thank you before we dive into the

**[07:57]** into thank you before we dive into the

**[07:57]** into thank you before we dive into the architecture I'm going to show to you

**[07:59]** architecture I'm going to show to you

**[07:59]** architecture I'm going to show to you what an example input looks like and


### [08:00 - 09:00]

**[08:01]** what an example input looks like and

**[08:01]** what an example input looks like and what an example output looks like. So

**[08:03]** what an example output looks like. So

**[08:03]** what an example output looks like. So what you see here is the image

**[08:05]** what you see here is the image

**[08:05]** what you see here is the image observation the robot state and the

**[08:07]** observation the robot state and the

**[08:07]** observation the robot state and the language prompt. That's the input. And

**[08:09]** language prompt. That's the input. And

**[08:09]** language prompt. That's the input. And then what's the output? The output is a

**[08:12]** then what's the output? The output is a

**[08:12]** then what's the output? The output is a robot action trajectory. So the prompt

**[08:15]** robot action trajectory. So the prompt

**[08:15]** robot action trajectory. So the prompt was to pick up the industrial object and

**[08:17]** was to pick up the industrial object and

**[08:17]** was to pick up the industrial object and place it in the yellow bin. And that's

**[08:19]** place it in the yellow bin. And that's

**[08:19]** place it in the yellow bin. And that's what the robot does. It picks up and

**[08:21]** what the robot does. It picks up and

**[08:21]** what the robot does. It picks up and places it in the yellow bin very neatly.

**[08:23]** places it in the yellow bin very neatly.

**[08:23]** places it in the yellow bin very neatly. But this is what it appears to us as

**[08:26]** But this is what it appears to us as

**[08:26]** But this is what it appears to us as humans. But is the robot or the humanoid

**[08:29]** humans. But is the robot or the humanoid

**[08:29]** humans. But is the robot or the humanoid seeing the same? Not really. The

**[08:31]** seeing the same? Not really. The

**[08:31]** seeing the same? Not really. The humanoid sees this. It sees a bunch of

**[08:35]** humanoid sees this. It sees a bunch of

**[08:36]** humanoid sees this. It sees a bunch of vectors, floatingoint vectors, which

**[08:38]** vectors, floatingoint vectors, which

**[08:38]** vectors, floatingoint vectors, which control the different joints. So you're

**[08:40]** control the different joints. So you're

**[08:40]** control the different joints. So you're seeing the output as a trajectory, which

**[08:42]** seeing the output as a trajectory, which

**[08:42]** seeing the output as a trajectory, which is like motion of the robot hand. But

**[08:45]** is like motion of the robot hand. But

**[08:45]** is like motion of the robot hand. But that's not what the robot is seeing. It

**[08:47]** that's not what the robot is seeing. It

**[08:47]** that's not what the robot is seeing. It uses these vectors to actually generate

**[08:50]** uses these vectors to actually generate

**[08:50]** uses these vectors to actually generate a continuous action. And to set context

**[08:52]** a continuous action. And to set context

**[08:52]** a continuous action. And to set context on what a robot state and action is, you

**[08:55]** on what a robot state and action is, you

**[08:55]** on what a robot state and action is, you can imagine the state is the robot

**[08:58]** can imagine the state is the robot

**[08:58]** can imagine the state is the robot snapshot at an instant instance of time.


### [09:00 - 10:00]

**[09:01]** snapshot at an instant instance of time.

**[09:01]** snapshot at an instant instance of time. So including the physique of the robot

**[09:03]** So including the physique of the robot

**[09:03]** So including the physique of the robot and the environment. That's the state.

**[09:06]** and the environment. That's the state.

**[09:06]** and the environment. That's the state. And then the action is what the robot

**[09:07]** And then the action is what the robot

**[09:07]** And then the action is what the robot decides to do next based on the state.

**[09:12]** decides to do next based on the state.

**[09:12]** decides to do next based on the state. So

**[09:14]** So

**[09:14]** So moving on and diving a bit deeper into

**[09:17]** moving on and diving a bit deeper into

**[09:17]** moving on and diving a bit deeper into the architecture,

**[09:18]** the architecture,

**[09:18]** the architecture, the Groot N1 system introduced a very

**[09:21]** the Groot N1 system introduced a very

**[09:21]** the Groot N1 system introduced a very interesting concept and this concept is

**[09:23]** interesting concept and this concept is

**[09:23]** interesting concept and this concept is inspired from Daniel Kman's book

**[09:26]** inspired from Daniel Kman's book

**[09:26]** inspired from Daniel Kman's book thinking fast and slow. Uh show of

**[09:28]** thinking fast and slow. Uh show of

**[09:28]** thinking fast and slow. Uh show of hands, how many of you have read the

**[09:29]** hands, how many of you have read the

**[09:29]** hands, how many of you have read the book? Amazing. That helps to explain. So

**[09:33]** book? Amazing. That helps to explain. So

**[09:33]** book? Amazing. That helps to explain. So it's inspired by the same concept, but

**[09:35]** it's inspired by the same concept, but

**[09:36]** it's inspired by the same concept, but it has it's applied to a robotics con

**[09:38]** it has it's applied to a robotics con

**[09:38]** it has it's applied to a robotics con context. So we have two systems system

**[09:41]** context. So we have two systems system

**[09:41]** context. So we have two systems system one system two. System two you can

**[09:43]** one system two. System two you can

**[09:44]** one system two. System two you can imagine is the brain of the robot or the

**[09:46]** imagine is the brain of the robot or the

**[09:46]** imagine is the brain of the robot or the brain of the model. So that's the part

**[09:48]** brain of the model. So that's the part

**[09:48]** brain of the model. So that's the part which is actually trying to break down

**[09:51]** which is actually trying to break down

**[09:51]** which is actually trying to break down the complex tasks. So make it simpler

**[09:54]** the complex tasks. So make it simpler

**[09:54]** the complex tasks. So make it simpler such that the system one can execute on

**[09:57]** such that the system one can execute on

**[09:57]** such that the system one can execute on it. So you can think of system two as

**[09:59]** it. So you can think of system two as

**[09:59]** it. So you can think of system two as the planner which executes slowly to


### [10:00 - 11:00]

**[10:01]** the planner which executes slowly to

**[10:01]** the planner which executes slowly to break down the complex task and then

**[10:03]** break down the complex task and then

**[10:03]** break down the complex task and then system one is the fast one. It operates

**[10:05]** system one is the fast one. It operates

**[10:06]** system one is the fast one. It operates almost at 120 hertz and it basically

**[10:09]** almost at 120 hertz and it basically

**[10:09]** almost at 120 hertz and it basically executes on the task that system two

**[10:11]** executes on the task that system two

**[10:11]** executes on the task that system two puts out for it.

**[10:13]** puts out for it.

**[10:13]** puts out for it. And then now we're going to delve

**[10:15]** And then now we're going to delve

**[10:15]** And then now we're going to delve another level deeper into the

**[10:17]** another level deeper into the

**[10:17]** another level deeper into the architecture. And it's okay if all of

**[10:19]** architecture. And it's okay if all of

**[10:19]** architecture. And it's okay if all of this is complicated to you because it's

**[10:21]** this is complicated to you because it's

**[10:21]** this is complicated to you because it's not very straightforward. So we have the

**[10:24]** not very straightforward. So we have the

**[10:24]** not very straightforward. So we have the input as the robot state and the noise

**[10:27]** input as the robot state and the noise

**[10:27]** input as the robot state and the noise action. You must be wondering why we've

**[10:29]** action. You must be wondering why we've

**[10:29]** action. You must be wondering why we've called it noised action. Noised action

**[10:31]** called it noised action. Noised action

**[10:31]** called it noised action. Noised action is a natural state because these sensors

**[10:33]** is a natural state because these sensors

**[10:33]** is a natural state because these sensors don't capture the action perfectly. So

**[10:35]** don't capture the action perfectly. So

**[10:35]** don't capture the action perfectly. So we have no action. Uh and then they're

**[10:38]** we have no action. Uh and then they're

**[10:38]** we have no action. Uh and then they're passed to a state encoder and an action

**[10:41]** passed to a state encoder and an action

**[10:41]** passed to a state encoder and an action encoder which generates some tokens. Uh

**[10:44]** encoder which generates some tokens. Uh

**[10:44]** encoder which generates some tokens. Uh and you may be familiar with tokens.

**[10:47]** and you may be familiar with tokens.

**[10:47]** and you may be familiar with tokens. We've talked about LLMs, agents a lot.

**[10:49]** We've talked about LLMs, agents a lot.

**[10:49]** We've talked about LLMs, agents a lot. So the same concept but just different

**[10:51]** So the same concept but just different

**[10:51]** So the same concept but just different kinds of tokens. So state tokens, action

**[10:54]** kinds of tokens. So state tokens, action

**[10:54]** kinds of tokens. So state tokens, action tokens and then it's passed through a

**[10:56]** tokens and then it's passed through a

**[10:56]** tokens and then it's passed through a diffusion transformer block. And the

**[10:58]** diffusion transformer block. And the

**[10:58]** diffusion transformer block. And the diffusion transformer block is


### [11:00 - 12:00]

**[11:00]** diffusion transformer block is

**[11:00]** diffusion transformer block is essentially um multiple layers of cross

**[11:03]** essentially um multiple layers of cross

**[11:03]** essentially um multiple layers of cross attention and self attention.

**[11:06]** attention and self attention.

**[11:06]** attention and self attention. And bringing in the other piece which is

**[11:09]** And bringing in the other piece which is

**[11:09]** And bringing in the other piece which is the vision input and the text input. So

**[11:11]** the vision input and the text input. So

**[11:11]** the vision input and the text input. So you have the vision encoder which takes

**[11:14]** you have the vision encoder which takes

**[11:14]** you have the vision encoder which takes the image input, generates some tokens,

**[11:16]** the image input, generates some tokens,

**[11:16]** the image input, generates some tokens, passes it to the VLM to bring it to like

**[11:18]** passes it to the VLM to bring it to like

**[11:18]** passes it to the VLM to bring it to like a standardized encoding format and then

**[11:21]** a standardized encoding format and then

**[11:21]** a standardized encoding format and then the text tokenizer which takes the text

**[11:23]** the text tokenizer which takes the text

**[11:23]** the text tokenizer which takes the text input again does the same passes through

**[11:25]** input again does the same passes through

**[11:25]** input again does the same passes through the VLM and then all of this uh all of

**[11:28]** the VLM and then all of this uh all of

**[11:28]** the VLM and then all of this uh all of the output tokens from the VLM uh in

**[11:30]** the output tokens from the VLM uh in

**[11:30]** the output tokens from the VLM uh in this case in case of gluten one it was

**[11:33]** this case in case of gluten one it was

**[11:33]** this case in case of gluten one it was the eagle to VLM is passed into the

**[11:36]** the eagle to VLM is passed into the

**[11:36]** the eagle to VLM is passed into the cross attention uh layer of the

**[11:38]** cross attention uh layer of the

**[11:38]** cross attention uh layer of the diffusion transformer block And then you

**[11:42]** diffusion transformer block And then you

**[11:42]** diffusion transformer block And then you get some output tokens. These are the

**[11:44]** get some output tokens. These are the

**[11:44]** get some output tokens. These are the output tokens. Uh but these output

**[11:47]** output tokens. Uh but these output

**[11:47]** output tokens. Uh but these output tokens are still not ready to be

**[11:49]** tokens are still not ready to be

**[11:49]** tokens are still not ready to be consumed by the physical robot. So you

**[11:52]** consumed by the physical robot. So you

**[11:52]** consumed by the physical robot. So you need to make it consumable by the

**[11:54]** need to make it consumable by the

**[11:54]** need to make it consumable by the physical robot. And that's where you

**[11:56]** physical robot. And that's where you

**[11:56]** physical robot. And that's where you have this key piece called the action

**[11:58]** have this key piece called the action

**[11:58]** have this key piece called the action decoder. So it it may seem like there's


### [12:00 - 13:00]

**[12:01]** decoder. So it it may seem like there's

**[12:01]** decoder. So it it may seem like there's lots of encoders, lots of decoders, but

**[12:03]** lots of encoders, lots of decoders, but

**[12:03]** lots of encoders, lots of decoders, but you can say that the action decoder is

**[12:05]** you can say that the action decoder is

**[12:05]** you can say that the action decoder is the one which gives the model capability

**[12:07]** the one which gives the model capability

**[12:08]** the one which gives the model capability to be a generalist. So you're giving it

**[12:10]** to be a generalist. So you're giving it

**[12:10]** to be a generalist. So you're giving it an action decoder which is specific to

**[12:12]** an action decoder which is specific to

**[12:12]** an action decoder which is specific to the embodiment that you're going to use.

**[12:14]** the embodiment that you're going to use.

**[12:14]** the embodiment that you're going to use. Whether it's a humanoid hand or a robot

**[12:17]** Whether it's a humanoid hand or a robot

**[12:17]** Whether it's a humanoid hand or a robot arm, an industrial robot arm, that's

**[12:19]** arm, an industrial robot arm, that's

**[12:19]** arm, an industrial robot arm, that's where that action decoder comes into

**[12:21]** where that action decoder comes into

**[12:21]** where that action decoder comes into place. It's specific to the embodiment

**[12:23]** place. It's specific to the embodiment

**[12:23]** place. It's specific to the embodiment you're trying to use. And then it's

**[12:25]** you're trying to use. And then it's

**[12:25]** you're trying to use. And then it's going to translate it specific to your

**[12:27]** going to translate it specific to your

**[12:27]** going to translate it specific to your embodiment and output an action vector

**[12:30]** embodiment and output an action vector

**[12:30]** embodiment and output an action vector which can be translated into continuous

**[12:32]** which can be translated into continuous

**[12:32]** which can be translated into continuous robot motion or embodiment motion.

**[12:35]** robot motion or embodiment motion.

**[12:35]** robot motion or embodiment motion. Just going to give you a second to

**[12:37]** Just going to give you a second to

**[12:37]** Just going to give you a second to digest all of this. Uh so you can see

**[12:39]** digest all of this. Uh so you can see

**[12:39]** digest all of this. Uh so you can see that the action decoder is very very

**[12:41]** that the action decoder is very very

**[12:42]** that the action decoder is very very important because otherwise you would

**[12:44]** important because otherwise you would

**[12:44]** important because otherwise you would only be able to train a model for one

**[12:46]** only be able to train a model for one

**[12:46]** only be able to train a model for one specific embodiment but this model can

**[12:48]** specific embodiment but this model can

**[12:48]** specific embodiment but this model can leverage foundation knowledge from all

**[12:51]** leverage foundation knowledge from all

**[12:51]** leverage foundation knowledge from all different um embodiment and then bring

**[12:53]** different um embodiment and then bring

**[12:53]** different um embodiment and then bring it to one particular embodiment. The

**[12:55]** it to one particular embodiment. The

**[12:55]** it to one particular embodiment. The concept

**[12:57]** concept

**[12:57]** concept the concept is similar to the concept of

**[12:59]** the concept is similar to the concept of

**[12:59]** the concept is similar to the concept of a foundation model essentially. Uh


### [13:00 - 14:00]

**[13:02]** a foundation model essentially. Uh

**[13:02]** a foundation model essentially. Uh moving on to the next slide.

**[13:06]** moving on to the next slide.

**[13:06]** moving on to the next slide. There are two main ways of robot

**[13:09]** There are two main ways of robot

**[13:09]** There are two main ways of robot learning. Uh and the reason I chose to

**[13:11]** learning. Uh and the reason I chose to

**[13:11]** learning. Uh and the reason I chose to keep this slide is because it came up a

**[13:13]** keep this slide is because it came up a

**[13:13]** keep this slide is because it came up a lot in the conversations I was having

**[13:15]** lot in the conversations I was having

**[13:15]** lot in the conversations I was having the past couple of days. Uh there are

**[13:17]** the past couple of days. Uh there are

**[13:17]** the past couple of days. Uh there are two ways of training robots. One is

**[13:20]** two ways of training robots. One is

**[13:20]** two ways of training robots. One is imitation learning and the other is

**[13:23]** imitation learning and the other is

**[13:23]** imitation learning and the other is through reinforcement learning.

**[13:25]** through reinforcement learning.

**[13:25]** through reinforcement learning. Imitation learning uh in simple English

**[13:28]** Imitation learning uh in simple English

**[13:28]** Imitation learning uh in simple English terms imitation means to copy someone

**[13:31]** terms imitation means to copy someone

**[13:31]** terms imitation means to copy someone like learn by copying. That's exactly

**[13:33]** like learn by copying. That's exactly

**[13:33]** like learn by copying. That's exactly what's happening here. So you have a

**[13:35]** what's happening here. So you have a

**[13:36]** what's happening here. So you have a human expert and the robot is trying to

**[13:38]** human expert and the robot is trying to

**[13:38]** human expert and the robot is trying to copy the human expert and uh you're

**[13:40]** copy the human expert and uh you're

**[13:40]** copy the human expert and uh you're trying to minimize the loss between the

**[13:42]** trying to minimize the loss between the

**[13:42]** trying to minimize the loss between the expert and the human. So you have a gold

**[13:45]** expert and the human. So you have a gold

**[13:45]** expert and the human. So you have a gold standard, you're trying to match up to

**[13:46]** standard, you're trying to match up to

**[13:46]** standard, you're trying to match up to the gold standard. And then in case of

**[13:48]** the gold standard. And then in case of

**[13:48]** the gold standard. And then in case of reinforcement learning, it's more of a

**[13:50]** reinforcement learning, it's more of a

**[13:50]** reinforcement learning, it's more of a trial and error format. So what you're

**[13:52]** trial and error format. So what you're

**[13:52]** trial and error format. So what you're doing is you just uh maximize the

**[13:56]** doing is you just uh maximize the

**[13:56]** doing is you just uh maximize the reward. So you don't have a golden

**[13:57]** reward. So you don't have a golden

**[13:58]** reward. So you don't have a golden state. You're trying to just reach


### [14:00 - 15:00]

**[14:00]** state. You're trying to just reach

**[14:00]** state. You're trying to just reach wherever you can the best you can. You

**[14:02]** wherever you can the best you can. You

**[14:02]** wherever you can the best you can. You can think of it similar to having

**[14:04]** can think of it similar to having

**[14:04]** can think of it similar to having siblings. When there siblings, parents

**[14:06]** siblings. When there siblings, parents

**[14:06]** siblings. When there siblings, parents try to compare between the two and

**[14:08]** try to compare between the two and

**[14:08]** try to compare between the two and they're like, you need to be like your

**[14:09]** they're like, you need to be like your

**[14:09]** they're like, you need to be like your elder sibling, but then there's no

**[14:11]** elder sibling, but then there's no

**[14:11]** elder sibling, but then there's no sibling, and in that case, you can just

**[14:12]** sibling, and in that case, you can just

**[14:12]** sibling, and in that case, you can just be as good as you want. So, so that's

**[14:16]** be as good as you want. So, so that's

**[14:16]** be as good as you want. So, so that's reinforcement learning for you. And like

**[14:18]** reinforcement learning for you. And like

**[14:18]** reinforcement learning for you. And like all things good and bad in this world,

**[14:20]** all things good and bad in this world,

**[14:20]** all things good and bad in this world, both of them come with pros and cons. Uh

**[14:22]** both of them come with pros and cons. Uh

**[14:22]** both of them come with pros and cons. Uh with the imitation learning, you're

**[14:24]** with the imitation learning, you're

**[14:24]** with the imitation learning, you're severely bottlenecked by the expert

**[14:26]** severely bottlenecked by the expert

**[14:26]** severely bottlenecked by the expert data, which is quite expensive. uh but

**[14:29]** data, which is quite expensive. uh but

**[14:29]** data, which is quite expensive. uh but in case of reinforcement learning you

**[14:31]** in case of reinforcement learning you

**[14:31]** in case of reinforcement learning you don't have that bottleneck but it's the

**[14:33]** don't have that bottleneck but it's the

**[14:33]** don't have that bottleneck but it's the key challenge is the sim to real so

**[14:35]** key challenge is the sim to real so

**[14:35]** key challenge is the sim to real so there's a huge gap between going from

**[14:37]** there's a huge gap between going from

**[14:37]** there's a huge gap between going from sim to real and it's a active area of

**[14:39]** sim to real and it's a active area of

**[14:39]** sim to real and it's a active area of research a lot of research labs uh

**[14:42]** research a lot of research labs uh

**[14:42]** research a lot of research labs uh universities are going behind it so that

**[14:45]** universities are going behind it so that

**[14:45]** universities are going behind it so that was the two ways of training robots and

**[14:48]** was the two ways of training robots and

**[14:48]** was the two ways of training robots and uh group n1 used both of these in some

**[14:50]** uh group n1 used both of these in some

**[14:50]** uh group n1 used both of these in some ways um

**[14:53]** ways um

**[14:53]** ways um here's an example of the train model

**[14:55]** here's an example of the train model

**[14:55]** here's an example of the train model what can it do so on the left you see

**[14:58]** what can it do so on the left you see

**[14:58]** what can it do so on the left you see the model being able to do a few pick

**[14:59]** the model being able to do a few pick


### [15:00 - 16:00]

**[15:00]** the model being able to do a few pick and place tasks in the kitchen. On the

**[15:02]** and place tasks in the kitchen. On the

**[15:02]** and place tasks in the kitchen. On the right top, uh you can see with enough

**[15:05]** right top, uh you can see with enough

**[15:05]** right top, uh you can see with enough training, the model can be taught how to

**[15:06]** training, the model can be taught how to

**[15:06]** training, the model can be taught how to be romantic as well. Uh you don't see

**[15:09]** be romantic as well. Uh you don't see

**[15:09]** be romantic as well. Uh you don't see all the fallen champagne glasses and

**[15:11]** all the fallen champagne glasses and

**[15:11]** all the fallen champagne glasses and fallen flowers which went behind

**[15:13]** fallen flowers which went behind

**[15:13]** fallen flowers which went behind capturing this perfect snap. Uh and then

**[15:16]** capturing this perfect snap. Uh and then

**[15:16]** capturing this perfect snap. Uh and then the bottom right uh is two robot friends

**[15:19]** the bottom right uh is two robot friends

**[15:19]** the bottom right uh is two robot friends trying to get to an industrial task like

**[15:22]** trying to get to an industrial task like

**[15:22]** trying to get to an industrial task like a pick and place task again. But these

**[15:24]** a pick and place task again. But these

**[15:24]** a pick and place task again. But these are not um the only tasks that these

**[15:27]** are not um the only tasks that these

**[15:27]** are not um the only tasks that these these humanoids or robots can be do can

**[15:29]** these humanoids or robots can be do can

**[15:29]** these humanoids or robots can be do can be doing. They can be extended to any

**[15:31]** be doing. They can be extended to any

**[15:31]** be doing. They can be extended to any task any environment. Uh and that's why

**[15:34]** task any environment. Uh and that's why

**[15:34]** task any environment. Uh and that's why we have a foundation model, a generalist

**[15:37]** we have a foundation model, a generalist

**[15:37]** we have a foundation model, a generalist foundation model which can be expanded

**[15:39]** foundation model which can be expanded

**[15:39]** foundation model which can be expanded to any downstream task.

**[15:42]** to any downstream task.

**[15:42]** to any downstream task. So

**[15:44]** So

**[15:44]** So this is going to be my conclusion. Uh

**[15:46]** this is going to be my conclusion. Uh

**[15:46]** this is going to be my conclusion. Uh there are three core principles that we

**[15:49]** there are three core principles that we

**[15:49]** there are three core principles that we spoke about today and each of these is

**[15:51]** spoke about today and each of these is

**[15:51]** spoke about today and each of these is very hefty by itself.

**[15:53]** very hefty by itself.

**[15:53]** very hefty by itself. uh but primarily the data pyramid Anika

**[15:57]** uh but primarily the data pyramid Anika

**[15:57]** uh but primarily the data pyramid Anika spoke about this in case of LLMs or text


### [16:00 - 17:00]

**[16:01]** spoke about this in case of LLMs or text

**[16:01]** spoke about this in case of LLMs or text data or text models you have the whole

**[16:03]** data or text models you have the whole

**[16:03]** data or text models you have the whole internet which you can be scraping to

**[16:05]** internet which you can be scraping to

**[16:05]** internet which you can be scraping to generate data but there's no such

**[16:08]** generate data but there's no such

**[16:08]** generate data but there's no such internet scale data for actions. So that

**[16:10]** internet scale data for actions. So that

**[16:10]** internet scale data for actions. So that is one of the key challenges that you

**[16:12]** is one of the key challenges that you

**[16:12]** is one of the key challenges that you need to address either via simulation or

**[16:14]** need to address either via simulation or

**[16:14]** need to address either via simulation or by imitation learning get generating

**[16:16]** by imitation learning get generating

**[16:16]** by imitation learning get generating expert data telly operation all sorts of

**[16:19]** expert data telly operation all sorts of

**[16:19]** expert data telly operation all sorts of things. The next thing is the dual

**[16:21]** things. The next thing is the dual

**[16:21]** things. The next thing is the dual system architecture. Uh previously what

**[16:24]** system architecture. Uh previously what

**[16:24]** system architecture. Uh previously what used to happen was each of these

**[16:26]** used to happen was each of these

**[16:26]** used to happen was each of these components was trained independently and

**[16:29]** components was trained independently and

**[16:29]** components was trained independently and that resulted in some kind of

**[16:31]** that resulted in some kind of

**[16:31]** that resulted in some kind of disagreement between the two systems.

**[16:33]** disagreement between the two systems.

**[16:33]** disagreement between the two systems. The group N1 introduces this coherent uh

**[16:36]** The group N1 introduces this coherent uh

**[16:36]** The group N1 introduces this coherent uh architecture where both the system one

**[16:39]** architecture where both the system one

**[16:39]** architecture where both the system one and system two are being co-rained and

**[16:42]** and system two are being co-rained and

**[16:42]** and system two are being co-rained and that kind of helps to optimize the whole

**[16:45]** that kind of helps to optimize the whole

**[16:45]** that kind of helps to optimize the whole stack instead of ident individually

**[16:47]** stack instead of ident individually

**[16:47]** stack instead of ident individually trying to train the pieces and then the

**[16:50]** trying to train the pieces and then the

**[16:50]** trying to train the pieces and then the third piece and the final piece uh is

**[16:53]** third piece and the final piece uh is

**[16:53]** third piece and the final piece uh is the generalist model. So in case of the

**[16:56]** the generalist model. So in case of the

**[16:56]** the generalist model. So in case of the generalist model you're able to leverage

**[16:58]** generalist model you're able to leverage

**[16:58]** generalist model you're able to leverage foundation knowledge from the model and


### [17:00 - 18:00]

**[17:02]** foundation knowledge from the model and

**[17:02]** foundation knowledge from the model and extend it to different embodiment

**[17:04]** extend it to different embodiment

**[17:04]** extend it to different embodiment different tasks you're you can think of

**[17:07]** different tasks you're you can think of

**[17:07]** different tasks you're you can think of it like how you have in case of large

**[17:09]** it like how you have in case of large

**[17:09]** it like how you have in case of large language models you have a base

**[17:10]** language models you have a base

**[17:10]** language models you have a base foundation llama 27TB model or there's

**[17:13]** foundation llama 27TB model or there's

**[17:13]** foundation llama 27TB model or there's llama 4 now or llama 3 I I don't know

**[17:16]** llama 4 now or llama 3 I I don't know

**[17:16]** llama 4 now or llama 3 I I don't know which is the latest but you can extend

**[17:18]** which is the latest but you can extend

**[17:18]** which is the latest but you can extend it uh to any f you can fine-tune it to

**[17:22]** it uh to any f you can fine-tune it to

**[17:22]** it uh to any f you can fine-tune it to any task or like domain adapt it

**[17:24]** any task or like domain adapt it

**[17:24]** any task or like domain adapt it similarly you have the root N1 model

**[17:26]** similarly you have the root N1 model

**[17:26]** similarly you have the root N1 model which can be adapted to any embodiment

**[17:28]** which can be adapted to any embodiment

**[17:28]** which can be adapted to any embodiment and any downstream task. Thank you so

**[17:30]** and any downstream task. Thank you so

**[17:30]** and any downstream task. Thank you so much for attending our talk today. Uh

**[17:32]** much for attending our talk today. Uh

**[17:32]** much for attending our talk today. Uh we're really happy you were here. Uh

**[17:34]** we're really happy you were here. Uh

**[17:34]** we're really happy you were here. Uh please let us know if you have

**[17:36]** please let us know if you have

**[17:36]** please let us know if you have questions. We'll be outside hanging out.

**[17:38]** questions. We'll be outside hanging out.

**[17:38]** questions. We'll be outside hanging out. Uh thank you so much. We appreciate it.

**[17:41]** Uh thank you so much. We appreciate it.

**[17:41]** Uh thank you so much. We appreciate it. [Music]


