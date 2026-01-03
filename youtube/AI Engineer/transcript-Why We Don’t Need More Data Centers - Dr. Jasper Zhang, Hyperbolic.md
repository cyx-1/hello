# Why We Don’t Need More Data Centers - Dr. Jasper Zhang, Hyperbolic

**Video URL:** https://www.youtube.com/watch?v=M6Vbaig1TsM

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Nice meeting you guys. Uh great to be

**[00:17]** Nice meeting you guys. Uh great to be here and uh I'm here to present

**[00:19]** here and uh I'm here to present

**[00:19]** here and uh I'm here to present hyperbolic which is AI cloud for

**[00:21]** hyperbolic which is AI cloud for

**[00:21]** hyperbolic which is AI cloud for developers. And so my topic is uh why

**[00:26]** developers. And so my topic is uh why

**[00:26]** developers. And so my topic is uh why we don't need more data centers. It's

**[00:28]** we don't need more data centers. It's

**[00:28]** we don't need more data centers. It's like a very eye-catching title. Uh but I

**[00:31]** like a very eye-catching title. Uh but I

**[00:31]** like a very eye-catching title. Uh but I what I want to clarify is I still think

**[00:34]** what I want to clarify is I still think

**[00:34]** what I want to clarify is I still think b building data centers is important but

**[00:36]** b building data centers is important but

**[00:36]** b building data centers is important but just building data centers alone can

**[00:38]** just building data centers alone can

**[00:38]** just building data centers alone can solve the problem.

**[00:41]** solve the problem.

**[00:41]** solve the problem. So uh

**[00:43]** So uh

**[00:43]** So uh wait before we get started uh let me

**[00:46]** wait before we get started uh let me

**[00:46]** wait before we get started uh let me introduce myself. I'm Jasper. I'm the

**[00:48]** introduce myself. I'm Jasper. I'm the

**[00:48]** introduce myself. I'm Jasper. I'm the CEO and co-founder of Hyperbolic. Um I

**[00:50]** CEO and co-founder of Hyperbolic. Um I

**[00:50]** CEO and co-founder of Hyperbolic. Um I did my math PhD at UC Berkeley. Uh

**[00:52]** did my math PhD at UC Berkeley. Uh

**[00:52]** did my math PhD at UC Berkeley. Uh finished my PhD in two years which make

**[00:54]** finished my PhD in two years which make

**[00:54]** finished my PhD in two years which make me the fastest person in the history of

**[00:56]** me the fastest person in the history of

**[00:56]** me the fastest person in the history of Berkeley. And then I also won a few gold

**[00:58]** Berkeley. And then I also won a few gold

**[00:58]** Berkeley. And then I also won a few gold medals. So after that I work at set of


### [01:00 - 02:00]

**[01:01]** medals. So after that I work at set of

**[01:01]** medals. So after that I work at set of securities uh trying to use AI and

**[01:03]** securities uh trying to use AI and

**[01:03]** securities uh trying to use AI and machine learning to predict the market

**[01:04]** machine learning to predict the market

**[01:04]** machine learning to predict the market execute strategy. So I always have a

**[01:07]** execute strategy. So I always have a

**[01:07]** execute strategy. So I always have a passion about how to make things very

**[01:09]** passion about how to make things very

**[01:10]** passion about how to make things very efficient and how to help you to save

**[01:11]** efficient and how to help you to save

**[01:11]** efficient and how to help you to save money because everyone knows that uh

**[01:14]** money because everyone knows that uh

**[01:14]** money because everyone knows that uh compute actually one of the biggest cost

**[01:16]** compute actually one of the biggest cost

**[01:16]** compute actually one of the biggest cost for your companies or for your startups.

**[01:18]** for your companies or for your startups.

**[01:18]** for your companies or for your startups. Uh usually you need to if you want to

**[01:20]** Uh usually you need to if you want to

**[01:20]** Uh usually you need to if you want to rent like 1,000 GPU will spend you

**[01:22]** rent like 1,000 GPU will spend you

**[01:22]** rent like 1,000 GPU will spend you millions of dollars uh per year. And we

**[01:24]** millions of dollars uh per year. And we

**[01:24]** millions of dollars uh per year. And we we think that these problems should be

**[01:27]** we think that these problems should be

**[01:27]** we think that these problems should be solved by not just building more data

**[01:29]** solved by not just building more data

**[01:29]** solved by not just building more data centers but actually uh building a GPU

**[01:32]** centers but actually uh building a GPU

**[01:32]** centers but actually uh building a GPU marketplace. So let's get started uh

**[01:34]** marketplace. So let's get started uh

**[01:34]** marketplace. So let's get started uh with the problem that we're facing. Uh

**[01:36]** with the problem that we're facing. Uh

**[01:36]** with the problem that we're facing. Uh first uh I think so so everyone knows

**[01:40]** first uh I think so so everyone knows

**[01:40]** first uh I think so so everyone knows that AI is going to integrate with

**[01:42]** that AI is going to integrate with

**[01:42]** that AI is going to integrate with everything in the future and every

**[01:44]** everything in the future and every

**[01:44]** everything in the future and every companies will be AI companies. So the

**[01:47]** companies will be AI companies. So the

**[01:47]** companies will be AI companies. So the demand for GPUs as well as data centers

**[01:50]** demand for GPUs as well as data centers

**[01:50]** demand for GPUs as well as data centers uh exploding. So by McKenzie by 2030

**[01:55]** uh exploding. So by McKenzie by 2030

**[01:55]** uh exploding. So by McKenzie by 2030 we'll need four acts more data centers

**[01:58]** we'll need four acts more data centers

**[01:58]** we'll need four acts more data centers built in one quarter of the time that we


### [02:00 - 03:00]

**[02:01]** built in one quarter of the time that we

**[02:01]** built in one quarter of the time that we build in the speed.

**[02:03]** build in the speed.

**[02:03]** build in the speed. Uh but what if I tell you that you

**[02:06]** Uh but what if I tell you that you

**[02:06]** Uh but what if I tell you that you actually don't need that many data

**[02:07]** actually don't need that many data

**[02:07]** actually don't need that many data centers uh you actually need uh another

**[02:11]** centers uh you actually need uh another

**[02:11]** centers uh you actually need uh another solution. So uh we can break down the

**[02:13]** solution. So uh we can break down the

**[02:14]** solution. So uh we can break down the demand first. Uh right now uh the

**[02:16]** demand first. Uh right now uh the

**[02:16]** demand first. Uh right now uh the current capacity for data center is 55

**[02:19]** current capacity for data center is 55

**[02:19]** current capacity for data center is 55 gawatt. Um

**[02:22]** gawatt. Um

**[02:22]** gawatt. Um by the median uh scenario we're going to

**[02:26]** by the median uh scenario we're going to

**[02:26]** by the median uh scenario we're going to see 22% annual growth rate for the

**[02:28]** see 22% annual growth rate for the

**[02:28]** see 22% annual growth rate for the demand. So in 2030 we're going to need

**[02:33]** demand. So in 2030 we're going to need

**[02:33]** demand. So in 2030 we're going to need 219 gawatt.

**[02:40]** And however uh it's like there are a lot

**[02:40]** And however uh it's like there are a lot of challenges building data centers

**[02:42]** of challenges building data centers

**[02:42]** of challenges building data centers right. So first uh we everyone knows

**[02:45]** right. So first uh we everyone knows

**[02:45]** right. So first uh we everyone knows Stargate. So it takes like uh for the

**[02:48]** Stargate. So it takes like uh for the

**[02:48]** Stargate. So it takes like uh for the first Stargate data center it takes like

**[02:50]** first Stargate data center it takes like

**[02:50]** first Stargate data center it takes like more than a billion dollars to build. Uh

**[02:52]** more than a billion dollars to build. Uh

**[02:52]** more than a billion dollars to build. Uh and then also it's very slow to collect

**[02:55]** and then also it's very slow to collect

**[02:55]** and then also it's very slow to collect data center to the electrical grid. For

**[02:58]** data center to the electrical grid. For

**[02:58]** data center to the electrical grid. For example, right now the the weight weight


### [03:00 - 04:00]

**[03:00]** example, right now the the weight weight

**[03:00]** example, right now the the weight weight list is like seven years. So you need to

**[03:02]** list is like seven years. So you need to

**[03:02]** list is like seven years. So you need to wait seven years to connect a 100

**[03:04]** wait seven years to connect a 100

**[03:04]** wait seven years to connect a 100 megawatts facility to the uh to the

**[03:07]** megawatts facility to the uh to the

**[03:07]** megawatts facility to the uh to the electric electrical grid in n uh

**[03:09]** electric electrical grid in n uh

**[03:09]** electric electrical grid in n uh northern Virginia.

**[03:11]** northern Virginia.

**[03:11]** northern Virginia. and uh and then uh it also very uh

**[03:15]** and uh and then uh it also very uh

**[03:15]** and uh and then uh it also very uh consuming a lot of energy. So uh

**[03:18]** consuming a lot of energy. So uh

**[03:18]** consuming a lot of energy. So uh currently we're spending 4% of the total

**[03:20]** currently we're spending 4% of the total

**[03:20]** currently we're spending 4% of the total electricity consumption in the US for

**[03:22]** electricity consumption in the US for

**[03:22]** electricity consumption in the US for just GPUs and data centers. uh and also

**[03:25]** just GPUs and data centers. uh and also

**[03:25]** just GPUs and data centers. uh and also is not very environmental sus

**[03:26]** is not very environmental sus

**[03:26]** is not very environmental sus sustainable. Uh if you can look at the

**[03:29]** sustainable. Uh if you can look at the

**[03:29]** sustainable. Uh if you can look at the number that's crazy uh CO2 emissions

**[03:32]** number that's crazy uh CO2 emissions

**[03:32]** number that's crazy uh CO2 emissions annually

**[03:34]** annually

**[03:34]** annually and even say if we're going to deliver

**[03:37]** and even say if we're going to deliver

**[03:37]** and even say if we're going to deliver all the data centers uh on time, there's

**[03:41]** all the data centers uh on time, there's

**[03:41]** all the data centers uh on time, there's still a data center supply deficit of

**[03:43]** still a data center supply deficit of

**[03:43]** still a data center supply deficit of more than 15 gawatts in the US alone by

**[03:47]** more than 15 gawatts in the US alone by

**[03:47]** more than 15 gawatts in the US alone by 2030. And so it means that

**[03:51]** 2030. And so it means that

**[03:51]** 2030. And so it means that just building data center can solve the

**[03:53]** just building data center can solve the

**[03:53]** just building data center can solve the problem.

**[03:54]** problem.

**[03:54]** problem. On the other hand, uh we think the GPU

**[03:59]** On the other hand, uh we think the GPU

**[03:59]** On the other hand, uh we think the GPU utilization is actually pretty low. So


### [04:00 - 05:00]

**[04:02]** utilization is actually pretty low. So

**[04:02]** utilization is actually pretty low. So according to uh deote, GPU sit idle 80%

**[04:07]** according to uh deote, GPU sit idle 80%

**[04:07]** according to uh deote, GPU sit idle 80% of the time for enterprises and

**[04:09]** of the time for enterprises and

**[04:09]** of the time for enterprises and companies

**[04:11]** companies

**[04:11]** companies according to s analysis there is this

**[04:14]** according to s analysis there is this

**[04:14]** according to s analysis there is this 100 plus GPU clouds. So we can see like

**[04:18]** 100 plus GPU clouds. So we can see like

**[04:18]** 100 plus GPU clouds. So we can see like how fragmented the space is right a lot

**[04:21]** how fragmented the space is right a lot

**[04:21]** how fragmented the space is right a lot of you guys need GPUs but you can't find

**[04:24]** of you guys need GPUs but you can't find

**[04:24]** of you guys need GPUs but you can't find them or like you are going to pay

**[04:26]** them or like you are going to pay

**[04:26]** them or like you are going to pay extremely high price on the other hand

**[04:29]** extremely high price on the other hand

**[04:29]** extremely high price on the other hand there are a lot of GPUs sit idle in data

**[04:32]** there are a lot of GPUs sit idle in data

**[04:32]** there are a lot of GPUs sit idle in data centers or in different clouds and so

**[04:35]** centers or in different clouds and so

**[04:35]** centers or in different clouds and so naturally uh a solution that we think we

**[04:38]** naturally uh a solution that we think we

**[04:38]** naturally uh a solution that we think we we should build is actually build a GP

**[04:40]** we should build is actually build a GP

**[04:40]** we should build is actually build a GP marketplace or like aggregation layer

**[04:42]** marketplace or like aggregation layer

**[04:42]** marketplace or like aggregation layer that aggregate different data centers

**[04:45]** that aggregate different data centers

**[04:45]** that aggregate different data centers and GP providers

**[04:47]** and GP providers

**[04:47]** and GP providers to solve the problem for uh GPU users.

**[04:49]** to solve the problem for uh GPU users.

**[04:50]** to solve the problem for uh GPU users. Uh it doesn't necessarily need to be

**[04:51]** Uh it doesn't necessarily need to be

**[04:51]** Uh it doesn't necessarily need to be hyperbolic, but I just use hyperbolic as

**[04:53]** hyperbolic, but I just use hyperbolic as

**[04:53]** hyperbolic, but I just use hyperbolic as an example uh to show here.

**[04:57]** an example uh to show here.

**[04:57]** an example uh to show here. So uh I can I can just like uh share


### [05:00 - 06:00]

**[05:00]** So uh I can I can just like uh share

**[05:00]** So uh I can I can just like uh share what we are we're trying to solve. So

**[05:03]** what we are we're trying to solve. So

**[05:03]** what we are we're trying to solve. So we're building this like global

**[05:04]** we're building this like global

**[05:04]** we're building this like global orchestration layer. Uh we invented a

**[05:06]** orchestration layer. Uh we invented a

**[05:06]** orchestration layer. Uh we invented a software called hyperdos which is short

**[05:09]** software called hyperdos which is short

**[05:09]** software called hyperdos which is short for hyperbolic distributed uh operating

**[05:12]** for hyperbolic distributed uh operating

**[05:12]** for hyperbolic distributed uh operating system. So basically it's like a

**[05:15]** system. So basically it's like a

**[05:15]** system. So basically it's like a kubernetes u software. So any any

**[05:18]** kubernetes u software. So any any

**[05:18]** kubernetes u software. So any any cluster as long as it installed our

**[05:21]** cluster as long as it installed our

**[05:21]** cluster as long as it installed our software within five minutes suddenly

**[05:24]** software within five minutes suddenly

**[05:24]** software within five minutes suddenly the data center become a cluster in our

**[05:26]** the data center become a cluster in our

**[05:26]** the data center become a cluster in our network and on the other side users can

**[05:29]** network and on the other side users can

**[05:29]** network and on the other side users can rent GPUs uh in different ways that they

**[05:32]** rent GPUs uh in different ways that they

**[05:32]** rent GPUs uh in different ways that they want like they can just uh do the spot

**[05:35]** want like they can just uh do the spot

**[05:35]** want like they can just uh do the spot instance they can like on demand they

**[05:37]** instance they can like on demand they

**[05:37]** instance they can like on demand they can long-term reserve or they can also

**[05:39]** can long-term reserve or they can also

**[05:40]** can long-term reserve or they can also like host models on top.

**[05:43]** like host models on top.

**[05:43]** like host models on top. Um and so like we see that we see that

**[05:46]** Um and so like we see that we see that

**[05:46]** Um and so like we see that we see that there are like several benefits. Um one

**[05:50]** there are like several benefits. Um one

**[05:50]** there are like several benefits. Um one we uh we got kind of like solve the e uh

**[05:53]** we uh we got kind of like solve the e uh

**[05:53]** we uh we got kind of like solve the e uh like the matching problem of compute. Uh

**[05:56]** like the matching problem of compute. Uh

**[05:56]** like the matching problem of compute. Uh and then second like GPU become

**[05:58]** and then second like GPU become

**[05:58]** and then second like GPU become commodities. So you like you don't need


### [06:00 - 07:00]

**[06:01]** commodities. So you like you don't need

**[06:01]** commodities. So you like you don't need to spend too much time to wait for data

**[06:02]** to spend too much time to wait for data

**[06:02]** to spend too much time to wait for data center you just buy them on the

**[06:03]** center you just buy them on the

**[06:03]** center you just buy them on the marketplace. And then third uh you can

**[06:06]** marketplace. And then third uh you can

**[06:06]** marketplace. And then third uh you can have different options.

**[06:09]** have different options.

**[06:09]** have different options. And so um we do some math modeling. Uh I

**[06:13]** And so um we do some math modeling. Uh I

**[06:13]** And so um we do some math modeling. Uh I I mean I don't have time to kind of put

**[06:15]** I mean I don't have time to kind of put

**[06:15]** I mean I don't have time to kind of put down the math in the slides but this is

**[06:17]** down the math in the slides but this is

**[06:17]** down the math in the slides but this is our conclusion right basically uh we can

**[06:21]** our conclusion right basically uh we can

**[06:21]** our conclusion right basically uh we can save the cost by 50 to 75%. Uh even if

**[06:25]** save the cost by 50 to 75%. Uh even if

**[06:25]** save the cost by 50 to 75%. Uh even if you look at uh the current we we're

**[06:27]** you look at uh the current we we're

**[06:27]** you look at uh the current we we're running like some beta version of our

**[06:29]** running like some beta version of our

**[06:29]** running like some beta version of our marketplace right now and our GPU cost

**[06:32]** marketplace right now and our GPU cost

**[06:32]** marketplace right now and our GPU cost for H100 is 99 cents per hour. But if

**[06:36]** for H100 is 99 cents per hour. But if

**[06:36]** for H100 is 99 cents per hour. But if you look at Google for example, they

**[06:39]** you look at Google for example, they

**[06:39]** you look at Google for example, they have on demand GPU. It's like $11.

**[06:41]** have on demand GPU. It's like $11.

**[06:42]** have on demand GPU. It's like $11. They're like lambda. They have like $2

**[06:43]** They're like lambda. They have like $2

**[06:43]** They're like lambda. They have like $2 or $3. But on average by aggregating

**[06:47]** or $3. But on average by aggregating

**[06:47]** or $3. But on average by aggregating more supply uh and then like have a

**[06:50]** more supply uh and then like have a

**[06:50]** more supply uh and then like have a uniform distribution channel, you can

**[06:53]** uniform distribution channel, you can

**[06:53]** uniform distribution channel, you can dramat uh drastically reduce the price.

**[06:56]** dramat uh drastically reduce the price.

**[06:56]** dramat uh drastically reduce the price. Um it's like the the theory behind that

**[06:58]** Um it's like the the theory behind that

**[06:58]** Um it's like the the theory behind that is like the queueing theory basically


### [07:00 - 08:00]

**[07:01]** is like the queueing theory basically

**[07:01]** is like the queueing theory basically like uh is MMC theory. I probably next

**[07:05]** like uh is MMC theory. I probably next

**[07:05]** like uh is MMC theory. I probably next time if we're going to watch my talk, I

**[07:06]** time if we're going to watch my talk, I

**[07:06]** time if we're going to watch my talk, I will share more math uh behind that. Uh

**[07:09]** will share more math uh behind that. Uh

**[07:09]** will share more math uh behind that. Uh but yeah and then like you can just save

**[07:11]** but yeah and then like you can just save

**[07:11]** but yeah and then like you can just save time to vetting your suppliers because

**[07:13]** time to vetting your suppliers because

**[07:13]** time to vetting your suppliers because you if you like think about I I mean how

**[07:16]** you if you like think about I I mean how

**[07:16]** you if you like think about I I mean how many people here are founders or like

**[07:18]** many people here are founders or like

**[07:18]** many people here are founders or like need to acquire GPUs?

**[07:21]** need to acquire GPUs?

**[07:21]** need to acquire GPUs? Yeah. So uh are you frustrated when you

**[07:24]** Yeah. So uh are you frustrated when you

**[07:24]** Yeah. So uh are you frustrated when you are trying to talk to how many suppliers

**[07:27]** are trying to talk to how many suppliers

**[07:27]** are trying to talk to how many suppliers are you talking to? If you have talked

**[07:29]** are you talking to? If you have talked

**[07:29]** are you talking to? If you have talked to more than five raise your hands.

**[07:32]** to more than five raise your hands.

**[07:32]** to more than five raise your hands. Are you frustrated when you like trying

**[07:34]** Are you frustrated when you like trying

**[07:34]** Are you frustrated when you like trying to have like five sales calls and like

**[07:37]** to have like five sales calls and like

**[07:37]** to have like five sales calls and like try to like know which status uh GPUs

**[07:39]** try to like know which status uh GPUs

**[07:40]** try to like know which status uh GPUs are are frustrated? Yeah. Are good.

**[07:42]** are are frustrated? Yeah. Are good.

**[07:42]** are are frustrated? Yeah. Are good. Yeah, that's great. Yeah. So, basically

**[07:44]** Yeah, that's great. Yeah. So, basically

**[07:44]** Yeah, that's great. Yeah. So, basically by having like this uniform platform

**[07:47]** by having like this uniform platform

**[07:47]** by having like this uniform platform like founders or like startups or

**[07:49]** like founders or like startups or

**[07:49]** like founders or like startups or companies no longer need to vet

**[07:52]** companies no longer need to vet

**[07:52]** companies no longer need to vet different data center. They just like

**[07:54]** different data center. They just like

**[07:54]** different data center. They just like pick the one that they uh have high

**[07:57]** pick the one that they uh have high

**[07:57]** pick the one that they uh have high rating or like have the best price.

**[07:59]** rating or like have the best price.

**[07:59]** rating or like have the best price. We're also going to do like uh


### [08:00 - 09:00]

**[08:01]** We're also going to do like uh

**[08:01]** We're also going to do like uh benchmarking on the performance of the

**[08:02]** benchmarking on the performance of the

**[08:02]** benchmarking on the performance of the GPUs.

**[08:09]** All right. So, uh

**[08:09]** All right. So, uh Oh, sorry.

**[08:15]** All right. So, uh sorry. Somehow the

**[08:15]** All right. So, uh sorry. Somehow the graph didn't didn't show.

**[08:31]** Yeah. So, um, basically we can think

**[08:31]** Yeah. So, um, basically we can think about a use case example. Um, so let's

**[08:34]** about a use case example. Um, so let's

**[08:34]** about a use case example. Um, so let's say if you if you are a startup and you

**[08:37]** say if you if you are a startup and you

**[08:37]** say if you if you are a startup and you want like 1,000 GPUs at the beginning.

**[08:39]** want like 1,000 GPUs at the beginning.

**[08:40]** want like 1,000 GPUs at the beginning. So, usually you will just reserve these

**[08:41]** So, usually you will just reserve these

**[08:41]** So, usually you will just reserve these 10,000 GPUs for a year, right? You think

**[08:44]** 10,000 GPUs for a year, right? You think

**[08:44]** 10,000 GPUs for a year, right? You think like I might need to use these GPUs uh

**[08:47]** like I might need to use these GPUs uh

**[08:47]** like I might need to use these GPUs uh for training and later on I want to do

**[08:48]** for training and later on I want to do

**[08:48]** for training and later on I want to do inference. And so you run some training

**[08:51]** inference. And so you run some training

**[08:51]** inference. And so you run some training jobs and then after three months then

**[08:54]** jobs and then after three months then

**[08:54]** jobs and then after three months then you realize that okay now I have a I

**[08:57]** you realize that okay now I have a I

**[08:57]** you realize that okay now I have a I have a n good a better idea by running


### [09:00 - 10:00]

**[09:00]** have a n good a better idea by running

**[09:00]** have a n good a better idea by running those experiments and now I need 1,000

**[09:02]** those experiments and now I need 1,000

**[09:02]** those experiments and now I need 1,000 more GPUs just for a month right and

**[09:05]** more GPUs just for a month right and

**[09:05]** more GPUs just for a month right and then after after six months uh at month

**[09:08]** then after after six months uh at month

**[09:08]** then after after six months uh at month takes then you finish your training job

**[09:10]** takes then you finish your training job

**[09:10]** takes then you finish your training job and then you realize that now I only

**[09:12]** and then you realize that now I only

**[09:12]** and then you realize that now I only need 500 GPUs for hosting my model but I

**[09:17]** need 500 GPUs for hosting my model but I

**[09:17]** need 500 GPUs for hosting my model but I still have 500 GPU

**[09:19]** still have 500 GPU

**[09:19]** still have 500 GPU So uh on the traditional on hyperbolic

**[09:22]** So uh on the traditional on hyperbolic

**[09:22]** So uh on the traditional on hyperbolic case uh you basically can say okay I

**[09:25]** case uh you basically can say okay I

**[09:25]** case uh you basically can say okay I will rent 1,000 GPUs for a year at the

**[09:28]** will rent 1,000 GPUs for a year at the

**[09:28]** will rent 1,000 GPUs for a year at the beginning but then uh in month three I

**[09:33]** beginning but then uh in month three I

**[09:33]** beginning but then uh in month three I can say uh I just rent uh an an actual

**[09:37]** can say uh I just rent uh an an actual

**[09:37]** can say uh I just rent uh an an actual 10,000 GPUs for just uh a month and then

**[09:41]** 10,000 GPUs for just uh a month and then

**[09:41]** 10,000 GPUs for just uh a month and then uh a month in month six then I can say

**[09:44]** uh a month in month six then I can say

**[09:44]** uh a month in month six then I can say okay I can release my idle GPUs on

**[09:47]** okay I can release my idle GPUs on

**[09:47]** okay I can release my idle GPUs on hyperbolic and try to sell to uh sell

**[09:49]** hyperbolic and try to sell to uh sell

**[09:49]** hyperbolic and try to sell to uh sell them to the uh to other people that need

**[09:51]** them to the uh to other people that need

**[09:51]** them to the uh to other people that need them, right? Uh but if you just like use

**[09:53]** them, right? Uh but if you just like use

**[09:53]** them, right? Uh but if you just like use on traditional cloud, then you need to

**[09:55]** on traditional cloud, then you need to

**[09:55]** on traditional cloud, then you need to rent 1,000 GPUs at the beginning and

**[09:58]** rent 1,000 GPUs at the beginning and

**[09:58]** rent 1,000 GPUs at the beginning and then on month in month three, you need

**[09:59]** then on month in month three, you need


### [10:00 - 11:00]

**[10:00]** then on month in month three, you need to rent actually 10,000 GPUs for a year

**[10:02]** to rent actually 10,000 GPUs for a year

**[10:02]** to rent actually 10,000 GPUs for a year usually. And uh if you calculate the

**[10:05]** usually. And uh if you calculate the

**[10:05]** usually. And uh if you calculate the cost uh compare compare that and then

**[10:07]** cost uh compare compare that and then

**[10:07]** cost uh compare compare that and then also like think about the price

**[10:09]** also like think about the price

**[10:09]** also like think about the price difference you will have um it will you

**[10:12]** difference you will have um it will you

**[10:12]** difference you will have um it will you can reduce the cost from 43.8 8 million

**[10:16]** can reduce the cost from 43.8 8 million

**[10:16]** can reduce the cost from 43.8 8 million to 6.9 million. So it's like 6x saving.

**[10:21]** to 6.9 million. So it's like 6x saving.

**[10:21]** to 6.9 million. So it's like 6x saving. Uh and you also help other people to get

**[10:23]** Uh and you also help other people to get

**[10:23]** Uh and you also help other people to get cheaper GPUs too because you can release

**[10:25]** cheaper GPUs too because you can release

**[10:25]** cheaper GPUs too because you can release those idle GPU to other people. And so

**[10:29]** those idle GPU to other people. And so

**[10:29]** those idle GPU to other people. And so uh so that's this is how we think that

**[10:31]** uh so that's this is how we think that

**[10:31]** uh so that's this is how we think that uh we're gonna we're gonna like increase

**[10:34]** uh we're gonna we're gonna like increase

**[10:34]** uh we're gonna we're gonna like increase the productivity like people only think

**[10:37]** the productivity like people only think

**[10:37]** the productivity like people only think about saving but actually uh this is not

**[10:40]** about saving but actually uh this is not

**[10:40]** about saving but actually uh this is not true for GPU right uh by scaling law we

**[10:43]** true for GPU right uh by scaling law we

**[10:43]** true for GPU right uh by scaling law we know that the more compute you spend the

**[10:46]** know that the more compute you spend the

**[10:46]** know that the more compute you spend the better quality your machine will be uh

**[10:48]** better quality your machine will be uh

**[10:48]** better quality your machine will be uh your model will be so it's not just

**[10:50]** your model will be so it's not just

**[10:50]** your model will be so it's not just about saving your cost by 6x it's more

**[10:54]** about saving your cost by 6x it's more

**[10:54]** about saving your cost by 6x it's more about with the same budget you will

**[10:57]** about with the same budget you will

**[10:57]** about with the same budget you will increase your productivity by 6x. And


### [11:00 - 12:00]

**[11:01]** increase your productivity by 6x. And

**[11:01]** increase your productivity by 6x. And imagine how many startups that they used

**[11:05]** imagine how many startups that they used

**[11:05]** imagine how many startups that they used only need to rely on open AI and

**[11:07]** only need to rely on open AI and

**[11:07]** only need to rely on open AI and anthropic those closed AI models. But

**[11:09]** anthropic those closed AI models. But

**[11:09]** anthropic those closed AI models. But now suddenly they their money become

**[11:12]** now suddenly they their money become

**[11:12]** now suddenly they their money become more valuable and they can rent as many

**[11:15]** more valuable and they can rent as many

**[11:15]** more valuable and they can rent as many GPUs as they want for the training.

**[11:18]** GPUs as they want for the training.

**[11:18]** GPUs as they want for the training. Um and so the the next step that that we

**[11:21]** Um and so the the next step that that we

**[11:21]** Um and so the the next step that that we think uh usually the GP marketplace will

**[11:23]** think uh usually the GP marketplace will

**[11:23]** think uh usually the GP marketplace will evolve into is that uh it will be a

**[11:26]** evolve into is that uh it will be a

**[11:26]** evolve into is that uh it will be a allin-one platform for different AI

**[11:29]** allin-one platform for different AI

**[11:29]** allin-one platform for different AI workload because what people really want

**[11:31]** workload because what people really want

**[11:31]** workload because what people really want is not just GPUs they want um to run

**[11:35]** is not just GPUs they want um to run

**[11:35]** is not just GPUs they want um to run their different AI jobs right they will

**[11:37]** their different AI jobs right they will

**[11:37]** their different AI jobs right they will you will have AI inference uh online

**[11:40]** you will have AI inference uh online

**[11:40]** you will have AI inference uh online inference uh offline inference and then

**[11:42]** inference uh offline inference and then

**[11:42]** inference uh offline inference and then you will also have uh training job

**[11:50]** and so Uh yeah so this is like um two

**[11:50]** and so Uh yeah so this is like um two two like uh some takeaway like basically

**[11:53]** two like uh some takeaway like basically

**[11:54]** two like uh some takeaway like basically we don't think we we need like just

**[11:57]** we don't think we we need like just

**[11:57]** we don't think we we need like just focus on building data centers we also

**[11:59]** focus on building data centers we also

**[11:59]** focus on building data centers we also need to do like smarter allocation for


### [12:00 - 13:00]

**[12:01]** need to do like smarter allocation for

**[12:01]** need to do like smarter allocation for the resources and then second uh we can

**[12:05]** the resources and then second uh we can

**[12:05]** the resources and then second uh we can reduce your cost um for by building GPA

**[12:09]** reduce your cost um for by building GPA

**[12:09]** reduce your cost um for by building GPA uh marketplace and lastly um I think uh

**[12:12]** uh marketplace and lastly um I think uh

**[12:12]** uh marketplace and lastly um I think uh just focusing on building data center is

**[12:14]** just focusing on building data center is

**[12:14]** just focusing on building data center is not very sustainable we're costing a lot

**[12:17]** not very sustainable we're costing a lot

**[12:17]** not very sustainable we're costing a lot of energy uh taking a lot of land uh we

**[12:20]** of energy uh taking a lot of land uh we

**[12:20]** of energy uh taking a lot of land uh we should better reuse recycle those idle

**[12:23]** should better reuse recycle those idle

**[12:23]** should better reuse recycle those idle compute by uh selling it to others. So

**[12:28]** compute by uh selling it to others. So

**[12:28]** compute by uh selling it to others. So uh if you're interesting in trying out

**[12:30]** uh if you're interesting in trying out

**[12:30]** uh if you're interesting in trying out uh you can uh come to our website uh the

**[12:34]** uh you can uh come to our website uh the

**[12:34]** uh you can uh come to our website uh the the left QR code is uh the current

**[12:37]** the left QR code is uh the current

**[12:37]** the left QR code is uh the current product that we have which is a

**[12:38]** product that we have which is a

**[12:38]** product that we have which is a marketplace but then we're also

**[12:39]** marketplace but then we're also

**[12:40]** marketplace but then we're also launching our business cloud and

**[12:41]** launching our business cloud and

**[12:41]** launching our business cloud and enterprise cloud that uh give you like

**[12:43]** enterprise cloud that uh give you like

**[12:43]** enterprise cloud that uh give you like production ready GPUs with 99.5%

**[12:46]** production ready GPUs with 99.5%

**[12:46]** production ready GPUs with 99.5% reliability. All right. Thanks.

**[12:56]** Awesome. So I actually got I'm curious.

**[12:56]** Awesome. So I actually got I'm curious. Can you tell us more about the the kind

**[12:58]** Can you tell us more about the the kind

**[12:58]** Can you tell us more about the the kind of hyperbolic OS? How exactly does that


### [13:00 - 14:00]

**[13:00]** of hyperbolic OS? How exactly does that

**[13:00]** of hyperbolic OS? How exactly does that turn because I know a lot of times you

**[13:03]** turn because I know a lot of times you

**[13:03]** turn because I know a lot of times you have a data center plus a set of GPUs.

**[13:05]** have a data center plus a set of GPUs.

**[13:05]** have a data center plus a set of GPUs. How how does it actually work to connect

**[13:07]** How how does it actually work to connect

**[13:08]** How how does it actually work to connect it to hyperbolic itself? Yeah. So um

**[13:11]** it to hyperbolic itself? Yeah. So um

**[13:11]** it to hyperbolic itself? Yeah. So um basically this is hyper hyperdos is like

**[13:14]** basically this is hyper hyperdos is like

**[13:14]** basically this is hyper hyperdos is like a kubernetes agent. So um you just

**[13:17]** a kubernetes agent. So um you just

**[13:17]** a kubernetes agent. So um you just install that in your cluster as long as

**[13:20]** install that in your cluster as long as

**[13:20]** install that in your cluster as long as you have kubernetes. I mean uh most data

**[13:23]** you have kubernetes. I mean uh most data

**[13:23]** you have kubernetes. I mean uh most data center have Kubernetes but then even for

**[13:25]** center have Kubernetes but then even for

**[13:25]** center have Kubernetes but then even for your MacBook or for your PC you can just

**[13:28]** your MacBook or for your PC you can just

**[13:28]** your MacBook or for your PC you can just install like micro K8 to kind of uh

**[13:31]** install like micro K8 to kind of uh

**[13:31]** install like micro K8 to kind of uh become a Kubernetes ready uh machine and

**[13:34]** become a Kubernetes ready uh machine and

**[13:34]** become a Kubernetes ready uh machine and uh so basically now you kind of have we

**[13:38]** uh so basically now you kind of have we

**[13:38]** uh so basically now you kind of have we we have terminology in house we call

**[13:40]** we have terminology in house we call

**[13:40]** we have terminology in house we call like our hyperbolic

**[13:43]** like our hyperbolic

**[13:43]** like our hyperbolic server uh monarch and then we have uh

**[13:47]** server uh monarch and then we have uh

**[13:47]** server uh monarch and then we have uh different baronss so it's like a feudal

**[13:50]** different baronss so it's like a feudal

**[13:50]** different baronss so it's like a feudal laser model So different varants they

**[13:52]** laser model So different varants they

**[13:52]** laser model So different varants they own different compute and then anytime

**[13:55]** own different compute and then anytime

**[13:55]** own different compute and then anytime every every time when a user want to

**[13:57]** every every time when a user want to

**[13:57]** every every time when a user want to rent GPU they will talk to our monarch

**[13:59]** rent GPU they will talk to our monarch

**[13:59]** rent GPU they will talk to our monarch server and the monarch server will send


### [14:00 - 15:00]

**[14:01]** server and the monarch server will send

**[14:01]** server and the monarch server will send a request to uh the like the baron and

**[14:04]** a request to uh the like the baron and

**[14:04]** a request to uh the like the baron and then baron will basically uh pro

**[14:06]** then baron will basically uh pro

**[14:06]** then baron will basically uh pro provision the machines and set up the

**[14:08]** provision the machines and set up the

**[14:08]** provision the machines and set up the ssh instance for customers to access.

**[14:11]** ssh instance for customers to access.

**[14:11]** ssh instance for customers to access. Yeah.


