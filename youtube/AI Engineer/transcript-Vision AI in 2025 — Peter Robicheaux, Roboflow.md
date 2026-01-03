# Vision AI in 2025 — Peter Robicheaux, Roboflow

**Video URL:** https://www.youtube.com/watch?v=IQc05eCvNYE

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** I'm going to be giving a quick

**[00:17]** I'm going to be giving a quick presentation about the state of the

**[00:18]** presentation about the state of the

**[00:18]** presentation about the state of the union regarding AI vision. Um, so I'm

**[00:22]** union regarding AI vision. Um, so I'm

**[00:22]** union regarding AI vision. Um, so I'm Peter Robisho. I'm the ML lead at

**[00:25]** Peter Robisho. I'm the ML lead at

**[00:25]** Peter Robisho. I'm the ML lead at Rooflow, which is a platform for

**[00:29]** Rooflow, which is a platform for

**[00:29]** Rooflow, which is a platform for building and deploying vision models.

**[00:32]** building and deploying vision models.

**[00:32]** building and deploying vision models. Um, so a lot of people are really

**[00:35]** Um, so a lot of people are really

**[00:35]** Um, so a lot of people are really interested in LLMs these days. So I'm

**[00:37]** interested in LLMs these days. So I'm

**[00:37]** interested in LLMs these days. So I'm trying to pitch why computer vision

**[00:39]** trying to pitch why computer vision

**[00:39]** trying to pitch why computer vision matters. Uh so if you think about

**[00:43]** matters. Uh so if you think about

**[00:43]** matters. Uh so if you think about systems that interact with the real

**[00:44]** systems that interact with the real

**[00:44]** systems that interact with the real world, they have to use vision as one of

**[00:46]** world, they have to use vision as one of

**[00:46]** world, they have to use vision as one of their primary inputs because the the

**[00:50]** their primary inputs because the the

**[00:50]** their primary inputs because the the built world is sort of built around

**[00:51]** built world is sort of built around

**[00:51]** built world is sort of built around vision as a fundamental primitive. Um

**[00:54]** vision as a fundamental primitive. Um

**[00:54]** vision as a fundamental primitive. Um and there's a big gap between where

**[00:58]** and there's a big gap between where

**[00:58]** and there's a big gap between where human vision is and where computer


### [01:00 - 02:00]

**[01:00]** human vision is and where computer

**[01:00]** human vision is and where computer vision is. Uh I I would argue a bigger

**[01:03]** vision is. Uh I I would argue a bigger

**[01:03]** vision is. Uh I I would argue a bigger gap than exists currently for human

**[01:06]** gap than exists currently for human

**[01:06]** gap than exists currently for human speech and uh computer speech.

**[01:09]** speech and uh computer speech.

**[01:09]** speech and uh computer speech. uh computer vision has like a its own

**[01:12]** uh computer vision has like a its own

**[01:12]** uh computer vision has like a its own set of problems that are very distinct

**[01:15]** set of problems that are very distinct

**[01:16]** set of problems that are very distinct from the problems that need to be solved

**[01:17]** from the problems that need to be solved

**[01:17]** from the problems that need to be solved by LLMs. Latency usually matters. You

**[01:20]** by LLMs. Latency usually matters. You

**[01:20]** by LLMs. Latency usually matters. You need to if you want to perceive motion,

**[01:22]** need to if you want to perceive motion,

**[01:22]** need to if you want to perceive motion, you have to be running your process

**[01:24]** you have to be running your process

**[01:24]** you have to be running your process multiple frames per second. Uh you

**[01:27]** multiple frames per second. Uh you

**[01:27]** multiple frames per second. Uh you usually want to run at the edge. You

**[01:29]** usually want to run at the edge. You

**[01:29]** usually want to run at the edge. You can't have like one big hub where you do

**[01:31]** can't have like one big hub where you do

**[01:31]** can't have like one big hub where you do all your computation because you would

**[01:34]** all your computation because you would

**[01:34]** all your computation because you would introduce too much latency to make

**[01:35]** introduce too much latency to make

**[01:35]** introduce too much latency to make decisions based off that computation.

**[01:39]** decisions based off that computation.

**[01:39]** decisions based off that computation. Um, and so I sort of gave a version of

**[01:42]** Um, and so I sort of gave a version of

**[01:42]** Um, and so I sort of gave a version of this talk uh at Leightton Space's

**[01:45]** this talk uh at Leightton Space's

**[01:45]** this talk uh at Leightton Space's podcast at Nurips. Um, and

**[01:48]** podcast at Nurips. Um, and

**[01:48]** podcast at Nurips. Um, and retrospectively I think we identified a

**[01:50]** retrospectively I think we identified a

**[01:50]** retrospectively I think we identified a few problems with uh the field of vision

**[01:54]** few problems with uh the field of vision

**[01:54]** few problems with uh the field of vision in 2024. One of them being eval are

**[01:57]** in 2024. One of them being eval are

**[01:57]** in 2024. One of them being eval are saturated. So vision evals like ImageNet

**[01:59]** saturated. So vision evals like ImageNet


### [02:00 - 03:00]

**[02:00]** saturated. So vision evals like ImageNet and Coco, they're mostly like pattern

**[02:02]** and Coco, they're mostly like pattern

**[02:02]** and Coco, they're mostly like pattern matching. they measure your ability to

**[02:04]** matching. they measure your ability to

**[02:04]** matching. they measure your ability to match patterns and sort of like don't

**[02:07]** match patterns and sort of like don't

**[02:07]** match patterns and sort of like don't require much visual intelligence to

**[02:09]** require much visual intelligence to

**[02:09]** require much visual intelligence to solve. Uh consequently, I think vision

**[02:13]** solve. Uh consequently, I think vision

**[02:13]** solve. Uh consequently, I think vision models don't leverage big pre-training

**[02:15]** models don't leverage big pre-training

**[02:15]** models don't leverage big pre-training the way that uh language models do. So

**[02:19]** the way that uh language models do. So

**[02:19]** the way that uh language models do. So right now you can take a language model,

**[02:21]** right now you can take a language model,

**[02:21]** right now you can take a language model, unleash it on the internet and get

**[02:22]** unleash it on the internet and get

**[02:22]** unleash it on the internet and get something incredibly smart. Some of the

**[02:24]** something incredibly smart. Some of the

**[02:24]** something incredibly smart. Some of the best vision models are certled

**[02:34]** and intelligence to solve the eval

**[02:34]** and intelligence to solve the eval there's kind of no incentive to do so.

**[02:37]** there's kind of no incentive to do so.

**[02:37]** there's kind of no incentive to do so. Uh and I think that part of that so

**[02:40]** Uh and I think that part of that so

**[02:40]** Uh and I think that part of that so there's sort of two dimensions here. One

**[02:41]** there's sort of two dimensions here. One

**[02:42]** there's sort of two dimensions here. One is that vision doesn't leverage big

**[02:43]** is that vision doesn't leverage big

**[02:43]** is that vision doesn't leverage big pre-training. So you can think of like

**[02:46]** pre-training. So you can think of like

**[02:46]** pre-training. So you can think of like if you're building an application with

**[02:47]** if you're building an application with

**[02:48]** if you're building an application with language right now, you probably want to

**[02:49]** language right now, you probably want to

**[02:49]** language right now, you probably want to use the smartest model to get an

**[02:50]** use the smartest model to get an

**[02:50]** use the smartest model to get an embedding that works really well for

**[02:52]** embedding that works really well for

**[02:52]** embedding that works really well for you. Right now we don't have like

**[02:54]** you. Right now we don't have like

**[02:54]** you. Right now we don't have like they're downstream applications that

**[02:56]** they're downstream applications that

**[02:56]** they're downstream applications that make really good use of the pre-training

**[02:58]** make really good use of the pre-training

**[02:58]** make really good use of the pre-training and the embeddings that they get from


### [03:00 - 04:00]

**[03:00]** and the embeddings that they get from

**[03:00]** and the embeddings that they get from large language models, but there aren't

**[03:02]** large language models, but there aren't

**[03:02]** large language models, but there aren't really good vision models that can

**[03:05]** really good vision models that can

**[03:05]** really good vision models that can leverage these embeddings. And the the

**[03:08]** leverage these embeddings. And the the

**[03:08]** leverage these embeddings. And the the correlary to this is that

**[03:11]** correlary to this is that

**[03:11]** correlary to this is that there the quality of big pre-trained

**[03:13]** there the quality of big pre-trained

**[03:13]** there the quality of big pre-trained models just isn't the same in vision as

**[03:15]** models just isn't the same in vision as

**[03:15]** models just isn't the same in vision as it is in language. And so my my

**[03:17]** it is in language. And so my my

**[03:17]** it is in language. And so my my underlying conclusion is vision models

**[03:19]** underlying conclusion is vision models

**[03:19]** underlying conclusion is vision models aren't smart. That's the the takeaway.

**[03:21]** aren't smart. That's the the takeaway.

**[03:21]** aren't smart. That's the the takeaway. And I can prove it to you. So last year

**[03:24]** And I can prove it to you. So last year

**[03:24]** And I can prove it to you. So last year when cloud 3.5 was happening, you could

**[03:26]** when cloud 3.5 was happening, you could

**[03:26]** when cloud 3.5 was happening, you could give it an image of a watch and it just

**[03:29]** give it an image of a watch and it just

**[03:29]** give it an image of a watch and it just guesses. You ask it what time it is and

**[03:30]** guesses. You ask it what time it is and

**[03:30]** guesses. You ask it what time it is and it'll just guess a random time. And

**[03:32]** it'll just guess a random time. And

**[03:32]** it'll just guess a random time. And that's because this model, it has a good

**[03:35]** that's because this model, it has a good

**[03:35]** that's because this model, it has a good conceptual abstract idea of what a clock

**[03:37]** conceptual abstract idea of what a clock

**[03:37]** conceptual abstract idea of what a clock is or what a watch is, but when it comes

**[03:39]** is or what a watch is, but when it comes

**[03:39]** is or what a watch is, but when it comes to actually identifying the location of

**[03:41]** to actually identifying the location of

**[03:41]** to actually identifying the location of watch hands and finding the numbers on

**[03:43]** watch hands and finding the numbers on

**[03:43]** watch hands and finding the numbers on the watch, it's hopeless. Uh, and

**[03:46]** the watch, it's hopeless. Uh, and

**[03:46]** the watch, it's hopeless. Uh, and updated for Cloud 4 still has no idea

**[03:49]** updated for Cloud 4 still has no idea

**[03:49]** updated for Cloud 4 still has no idea what time it is. And this is even like a

**[03:51]** what time it is. And this is even like a

**[03:51]** what time it is. And this is even like a an egregious failure because 1010 is

**[03:53]** an egregious failure because 1010 is

**[03:54]** an egregious failure because 1010 is like the stock time on like all watches.

**[03:56]** like the stock time on like all watches.

**[03:56]** like the stock time on like all watches. So, the fact that it couldn't even get

**[03:57]** So, the fact that it couldn't even get

**[03:57]** So, the fact that it couldn't even get like the most common time is uh pretty


### [04:00 - 05:00]

**[04:00]** like the most common time is uh pretty

**[04:00]** like the most common time is uh pretty telling.

**[04:02]** telling.

**[04:02]** telling. Uh there's so there's this really cool

**[04:05]** Uh there's so there's this really cool

**[04:05]** Uh there's so there's this really cool uh data set that's trying to measure

**[04:07]** uh data set that's trying to measure

**[04:07]** uh data set that's trying to measure this inability of LLM to see uh called

**[04:10]** this inability of LLM to see uh called

**[04:10]** this inability of LLM to see uh called MMVP which basically you can see an

**[04:14]** MMVP which basically you can see an

**[04:14]** MMVP which basically you can see an example here where they ask this

**[04:15]** example here where they ask this

**[04:15]** example here where they ask this question that seems incredibly obvious

**[04:18]** question that seems incredibly obvious

**[04:18]** question that seems incredibly obvious and the model so in this case they ask

**[04:21]** and the model so in this case they ask

**[04:21]** and the model so in this case they ask the model which is like chatbt 40 uh

**[04:25]** the model which is like chatbt 40 uh

**[04:25]** the model which is like chatbt 40 uh which direction the school bus is facing

**[04:27]** which direction the school bus is facing

**[04:27]** which direction the school bus is facing are we seeing the front or the back of

**[04:28]** are we seeing the front or the back of

**[04:28]** are we seeing the front or the back of the school bus and the model gets it

**[04:31]** the school bus and the model gets it

**[04:31]** the school bus and the model gets it completely wrong and then hallucinates

**[04:32]** completely wrong and then hallucinates

**[04:32]** completely wrong and then hallucinates details to support its claim. And again,

**[04:35]** details to support its claim. And again,

**[04:35]** details to support its claim. And again, I think this is evidence that large

**[04:37]** I think this is evidence that large

**[04:37]** I think this is evidence that large language models, which are maybe the

**[04:38]** language models, which are maybe the

**[04:38]** language models, which are maybe the most intelligent models that we have

**[04:40]** most intelligent models that we have

**[04:40]** most intelligent models that we have like cannot see. And that is due to a

**[04:44]** like cannot see. And that is due to a

**[04:44]** like cannot see. And that is due to a lack of visual features that they can

**[04:46]** lack of visual features that they can

**[04:46]** lack of visual features that they can perceive with. And so the way that this

**[04:48]** perceive with. And so the way that this

**[04:48]** perceive with. And so the way that this data set was created is they went and

**[04:49]** data set was created is they went and

**[04:49]** data set was created is they went and they found pairs of images that were

**[04:52]** they found pairs of images that were

**[04:52]** they found pairs of images that were close in clip space but far in Dinov2

**[04:55]** close in clip space but far in Dinov2

**[04:55]** close in clip space but far in Dinov2 space. So, clip is a is a vision

**[04:57]** space. So, clip is a is a vision

**[04:57]** space. So, clip is a is a vision language model that was sort of

**[04:59]** language model that was sort of

**[04:59]** language model that was sort of contrastively trained on the whole


### [05:00 - 06:00]

**[05:00]** contrastively trained on the whole

**[05:00]** contrastively trained on the whole internet. Dinov2 is just a pure vision

**[05:03]** internet. Dinov2 is just a pure vision

**[05:03]** internet. Dinov2 is just a pure vision model that was uh trained in a

**[05:05]** model that was uh trained in a

**[05:05]** model that was uh trained in a self-supervised way on the whole

**[05:06]** self-supervised way on the whole

**[05:06]** self-supervised way on the whole internet. Right? And so what this is

**[05:09]** internet. Right? And so what this is

**[05:09]** internet. Right? And so what this is showing is that clip is not

**[05:11]** showing is that clip is not

**[05:11]** showing is that clip is not discriminative enough to tell these two

**[05:13]** discriminative enough to tell these two

**[05:13]** discriminative enough to tell these two images apart. Right? So according to

**[05:15]** images apart. Right? So according to

**[05:15]** images apart. Right? So according to clip, these two images basically look

**[05:16]** clip, these two images basically look

**[05:16]** clip, these two images basically look the same. And what that's pointing to is

**[05:18]** the same. And what that's pointing to is

**[05:18]** the same. And what that's pointing to is like a failure in vision language

**[05:21]** like a failure in vision language

**[05:21]** like a failure in vision language pre-training. And so the way clip is

**[05:25]** pre-training. And so the way clip is

**[05:25]** pre-training. And so the way clip is trained is basically you come up with a

**[05:27]** trained is basically you come up with a

**[05:27]** trained is basically you come up with a big data set of captioned images and you

**[05:30]** big data set of captioned images and you

**[05:30]** big data set of captioned images and you you ask the model to you scramble the

**[05:33]** you ask the model to you scramble the

**[05:33]** you ask the model to you scramble the captions and scramble the images and ask

**[05:34]** captions and scramble the images and ask

**[05:34]** captions and scramble the images and ask the model to pair the image with the

**[05:36]** the model to pair the image with the

**[05:36]** the model to pair the image with the caption. But the thing is is if you go

**[05:38]** caption. But the thing is is if you go

**[05:38]** caption. But the thing is is if you go back and look these two images, what is

**[05:40]** back and look these two images, what is

**[05:40]** back and look these two images, what is a caption that would distinguish these

**[05:42]** a caption that would distinguish these

**[05:42]** a caption that would distinguish these two images, right? It's like the

**[05:44]** two images, right? It's like the

**[05:44]** two images, right? It's like the peculiar pose of the dog and one in one

**[05:47]** peculiar pose of the dog and one in one

**[05:47]** peculiar pose of the dog and one in one image it's facing the camera and one

**[05:49]** image it's facing the camera and one

**[05:49]** image it's facing the camera and one it's facing away. But these are sort of

**[05:50]** it's facing away. But these are sort of

**[05:50]** it's facing away. But these are sort of details that aren't included in the

**[05:51]** details that aren't included in the

**[05:51]** details that aren't included in the caption. So if your loss function can't

**[05:53]** caption. So if your loss function can't

**[05:53]** caption. So if your loss function can't tell these two images apart, then why

**[05:55]** tell these two images apart, then why

**[05:55]** tell these two images apart, then why would your model be able to, right? So

**[05:58]** would your model be able to, right? So

**[05:58]** would your model be able to, right? So vision only pre-training kind of works


### [06:00 - 07:00]

**[06:00]** vision only pre-training kind of works

**[06:00]** vision only pre-training kind of works is is the claim. So Dino V2 is this

**[06:04]** is is the claim. So Dino V2 is this

**[06:04]** is is the claim. So Dino V2 is this really cool model that so what you're

**[06:06]** really cool model that so what you're

**[06:06]** really cool model that so what you're seeing right now is a visualization of

**[06:07]** seeing right now is a visualization of

**[06:07]** seeing right now is a visualization of its PCA features that have been

**[06:09]** its PCA features that have been

**[06:10]** its PCA features that have been self-discovered by pre-training on the

**[06:12]** self-discovered by pre-training on the

**[06:12]** self-discovered by pre-training on the whole internet. Um, so what's really

**[06:14]** whole internet. Um, so what's really

**[06:14]** whole internet. Um, so what's really cool is not only like does it find the

**[06:16]** cool is not only like does it find the

**[06:16]** cool is not only like does it find the mask of the dog, obviously that's sort

**[06:19]** mask of the dog, obviously that's sort

**[06:19]** mask of the dog, obviously that's sort of easy because it's highly contrastive

**[06:21]** of easy because it's highly contrastive

**[06:21]** of easy because it's highly contrastive with the green background, but it also

**[06:23]** with the green background, but it also

**[06:23]** with the green background, but it also finds the segments of the dog and it

**[06:26]** finds the segments of the dog and it

**[06:26]** finds the segments of the dog and it finds even analogous segments. So if you

**[06:28]** finds even analogous segments. So if you

**[06:28]** finds even analogous segments. So if you look at the these principal components,

**[06:30]** look at the these principal components,

**[06:30]** look at the these principal components, you compare the legs of a dog, it'll be

**[06:32]** you compare the legs of a dog, it'll be

**[06:32]** you compare the legs of a dog, it'll be in the same sort of feature space as the

**[06:34]** in the same sort of feature space as the

**[06:34]** in the same sort of feature space as the legs of a of a human. And so the there's

**[06:37]** legs of a of a human. And so the there's

**[06:37]** legs of a of a human. And so the there's sort of this big open question which is

**[06:39]** sort of this big open question which is

**[06:39]** sort of this big open question which is like how do we get vision features that

**[06:42]** like how do we get vision features that

**[06:42]** like how do we get vision features that are well aligned with language features

**[06:44]** are well aligned with language features

**[06:44]** are well aligned with language features and usable by VLMs that don't suck and

**[06:49]** and usable by VLMs that don't suck and

**[06:49]** and usable by VLMs that don't suck and like have visual fidelity. Um cool. So

**[06:55]** like have visual fidelity. Um cool. So

**[06:55]** like have visual fidelity. Um cool. So so that's part of the story. The other

**[06:57]** so that's part of the story. The other

**[06:57]** so that's part of the story. The other part of this the question that needs to

**[06:59]** part of this the question that needs to

**[06:59]** part of this the question that needs to be answered is given that we have some


### [07:00 - 08:00]

**[07:00]** be answered is given that we have some

**[07:00]** be answered is given that we have some sort of semi- working large pre-training

**[07:04]** sort of semi- working large pre-training

**[07:04]** sort of semi- working large pre-training uh of vision models why aren't we

**[07:06]** uh of vision models why aren't we

**[07:06]** uh of vision models why aren't we leveraging these vision models and I

**[07:08]** leveraging these vision models and I

**[07:08]** leveraging these vision models and I would answer that at least in the object

**[07:10]** would answer that at least in the object

**[07:10]** would answer that at least in the object detection space the answer is mostly in

**[07:13]** detection space the answer is mostly in

**[07:13]** detection space the answer is mostly in the distinction between convolutional

**[07:14]** the distinction between convolutional

**[07:14]** the distinction between convolutional models and transformers so this is from

**[07:17]** models and transformers so this is from

**[07:17]** models and transformers so this is from LW DTER which is one of the top

**[07:20]** LW DTER which is one of the top

**[07:20]** LW DTER which is one of the top performing uh detection transformers

**[07:22]** performing uh detection transformers

**[07:22]** performing uh detection transformers that currently exists uh if you look at

**[07:26]** that currently exists uh if you look at

**[07:26]** that currently exists uh if you look at this graph If you look at yellow v

**[07:28]** this graph If you look at yellow v

**[07:28]** this graph If you look at yellow v yellow v8 which is a convolutional

**[07:30]** yellow v8 which is a convolutional

**[07:30]** yellow v8 which is a convolutional object detector on the edge with and

**[07:32]** object detector on the edge with and

**[07:32]** object detector on the edge with and without pre-training on objects 365 it

**[07:34]** without pre-training on objects 365 it

**[07:34]** without pre-training on objects 365 it gains like 02 map which is like the main

**[07:37]** gains like 02 map which is like the main

**[07:37]** gains like 02 map which is like the main accuracy metric for object detectors. So

**[07:40]** accuracy metric for object detectors. So

**[07:40]** accuracy metric for object detectors. So object 365 which is a big million 1.6 6

**[07:43]** object 365 which is a big million 1.6 6

**[07:43]** object 365 which is a big million 1.6 6 million image data set uh pre-training

**[07:46]** million image data set uh pre-training

**[07:46]** million image data set uh pre-training on it leads almost no performance

**[07:48]** on it leads almost no performance

**[07:48]** on it leads almost no performance improvements on on Coco whereas for LW

**[07:52]** improvements on on Coco whereas for LW

**[07:52]** improvements on on Coco whereas for LW DTOR which is a transformer-based model

**[07:54]** DTOR which is a transformer-based model

**[07:54]** DTOR which is a transformer-based model you can see that without if you look at

**[07:56]** you can see that without if you look at

**[07:56]** you can see that without if you look at this column map without pre-training and

**[07:58]** this column map without pre-training and

**[07:58]** this column map without pre-training and you look at the column map with

**[07:59]** you look at the column map with

**[07:59]** you look at the column map with pre-training you can see that you're


### [08:00 - 09:00]

**[08:01]** pre-training you can see that you're

**[08:01]** pre-training you can see that you're getting like five map improvements

**[08:03]** getting like five map improvements

**[08:03]** getting like five map improvements across the board sometimes even seven

**[08:05]** across the board sometimes even seven

**[08:05]** across the board sometimes even seven map improvements which is like a

**[08:06]** map improvements which is like a

**[08:06]** map improvements which is like a gigantic amount right and so basically

**[08:09]** gigantic amount right and so basically

**[08:09]** gigantic amount right and so basically the while the language world knows shows

**[08:12]** the while the language world knows shows

**[08:12]** the while the language world knows shows that transformers are able to leverage

**[08:14]** that transformers are able to leverage

**[08:14]** that transformers are able to leverage big pre-trainings and and yield decent

**[08:17]** big pre-trainings and and yield decent

**[08:17]** big pre-trainings and and yield decent results. The vision world is sort of

**[08:19]** results. The vision world is sort of

**[08:19]** results. The vision world is sort of just now catching up. Uh and you can see

**[08:22]** just now catching up. Uh and you can see

**[08:22]** just now catching up. Uh and you can see this from the scale of the big

**[08:23]** this from the scale of the big

**[08:23]** this from the scale of the big pre-training in the image world.

**[08:25]** pre-training in the image world.

**[08:25]** pre-training in the image world. Pre-training on objects 365 with 1.6

**[08:28]** Pre-training on objects 365 with 1.6

**[08:28]** Pre-training on objects 365 with 1.6 million images is considered a large

**[08:30]** million images is considered a large

**[08:30]** million images is considered a large pre-training that would be like a tiny

**[08:32]** pre-training that would be like a tiny

**[08:32]** pre-training that would be like a tiny like challenge data set for like for

**[08:35]** like challenge data set for like for

**[08:35]** like challenge data set for like for like undergrads in the LLM world. So I

**[08:39]** like undergrads in the LLM world. So I

**[08:39]** like undergrads in the LLM world. So I want to announce Rooflow's

**[08:41]** want to announce Rooflow's

**[08:41]** want to announce Rooflow's special new model called RF DTOR which

**[08:45]** special new model called RF DTOR which

**[08:45]** special new model called RF DTOR which leverages the Dinov2 pre-trained

**[08:46]** leverages the Dinov2 pre-trained

**[08:46]** leverages the Dinov2 pre-trained backbone and uh perform or uses it in a

**[08:50]** backbone and uh perform or uses it in a

**[08:50]** backbone and uh perform or uses it in a real-time object detection context. So

**[08:53]** real-time object detection context. So

**[08:53]** real-time object detection context. So this is sort of our

**[08:55]** this is sort of our

**[08:55]** this is sort of our answer to the the hole that we see in

**[08:57]** answer to the the hole that we see in

**[08:57]** answer to the the hole that we see in the field of like why aren't we

**[08:59]** the field of like why aren't we

**[08:59]** the field of like why aren't we leveraging big pre-trainings for visual


### [09:00 - 10:00]

**[09:02]** leveraging big pre-trainings for visual

**[09:02]** leveraging big pre-trainings for visual models. Um and so here's some of the

**[09:05]** models. Um and so here's some of the

**[09:05]** models. Um and so here's some of the metrics. You can see that um

**[09:08]** metrics. You can see that um

**[09:08]** metrics. You can see that um basically what we did is we took the LW

**[09:10]** basically what we did is we took the LW

**[09:10]** basically what we did is we took the LW dter backbone and we like kind of

**[09:12]** dter backbone and we like kind of

**[09:12]** dter backbone and we like kind of swapped it out with the Dynino V2

**[09:13]** swapped it out with the Dynino V2

**[09:13]** swapped it out with the Dynino V2 backbone and we get like a decent

**[09:15]** backbone and we get like a decent

**[09:15]** backbone and we get like a decent improvement on Coco. Um and we're still

**[09:19]** improvement on Coco. Um and we're still

**[09:19]** improvement on Coco. Um and we're still not soda uh compared to on Coco compared

**[09:22]** not soda uh compared to on Coco compared

**[09:22]** not soda uh compared to on Coco compared to define which is the current soda.

**[09:23]** to define which is the current soda.

**[09:23]** to define which is the current soda. We're like second soda. Um, but I think

**[09:25]** We're like second soda. Um, but I think

**[09:25]** We're like second soda. Um, but I think what's really interesting is there's

**[09:27]** what's really interesting is there's

**[09:27]** what's really interesting is there's this other data set called RF100VL

**[09:29]** this other data set called RF100VL

**[09:29]** this other data set called RF100VL which we created to measure the sort of

**[09:33]** which we created to measure the sort of

**[09:33]** which we created to measure the sort of domain adaptability of this model and

**[09:35]** domain adaptability of this model and

**[09:35]** domain adaptability of this model and you can see massive yields from using

**[09:38]** you can see massive yields from using

**[09:38]** you can see massive yields from using the Dynino V2 pre-trained backbone which

**[09:40]** the Dynino V2 pre-trained backbone which

**[09:40]** the Dynino V2 pre-trained backbone which basically is pointing to the fact that

**[09:41]** basically is pointing to the fact that

**[09:41]** basically is pointing to the fact that number one Coco is too easily solvable.

**[09:45]** number one Coco is too easily solvable.

**[09:45]** number one Coco is too easily solvable. Uh, it basically has common classes like

**[09:47]** Uh, it basically has common classes like

**[09:47]** Uh, it basically has common classes like humans and like coffee cups and stuff

**[09:50]** humans and like coffee cups and stuff

**[09:50]** humans and like coffee cups and stuff like this. So it's not a good measure of

**[09:51]** like this. So it's not a good measure of

**[09:52]** like this. So it's not a good measure of the intelligence of your model. more or

**[09:53]** the intelligence of your model. more or

**[09:54]** the intelligence of your model. more or so the way that you optimize Coco is by

**[09:56]** so the way that you optimize Coco is by

**[09:56]** so the way that you optimize Coco is by like really nailing the precise location

**[09:59]** like really nailing the precise location

**[09:59]** like really nailing the precise location of a bounding box or something. Really


### [10:00 - 11:00]

**[10:00]** of a bounding box or something. Really

**[10:00]** of a bounding box or something. Really having good iterative refinement of your

**[10:02]** having good iterative refinement of your

**[10:02]** having good iterative refinement of your like locations that you're guessing. Um

**[10:05]** like locations that you're guessing. Um

**[10:05]** like locations that you're guessing. Um whereas we posit R100VL this new data

**[10:09]** whereas we posit R100VL this new data

**[10:09]** whereas we posit R100VL this new data set is a better measure of the

**[10:11]** set is a better measure of the

**[10:11]** set is a better measure of the intelligence of a visual model. Um, so

**[10:16]** intelligence of a visual model. Um, so

**[10:16]** intelligence of a visual model. Um, so we're introducing a new data set,

**[10:17]** we're introducing a new data set,

**[10:17]** we're introducing a new data set, R1400VL, which is a collection of 100

**[10:19]** R1400VL, which is a collection of 100

**[10:19]** R1400VL, which is a collection of 100 different object dete detection data

**[10:21]** different object dete detection data

**[10:21]** different object dete detection data sets that were pulled from our

**[10:22]** sets that were pulled from our

**[10:22]** sets that were pulled from our open-source collection of data sets. We

**[10:26]** open-source collection of data sets. We

**[10:26]** open-source collection of data sets. We have something like I don't know, it's

**[10:28]** have something like I don't know, it's

**[10:28]** have something like I don't know, it's something like 750,000 data sets or

**[10:30]** something like 750,000 data sets or

**[10:30]** something like 750,000 data sets or whatever on Rooflow Universe and we hand

**[10:33]** whatever on Rooflow Universe and we hand

**[10:33]** whatever on Rooflow Universe and we hand curated the 100 best I guess by some

**[10:37]** curated the 100 best I guess by some

**[10:37]** curated the 100 best I guess by some metric. So like we sorted by community

**[10:40]** metric. So like we sorted by community

**[10:40]** metric. So like we sorted by community engagement and we tried to find very

**[10:43]** engagement and we tried to find very

**[10:43]** engagement and we tried to find very difficult domains. So you'll notice for

**[10:45]** difficult domains. So you'll notice for

**[10:45]** difficult domains. So you'll notice for instance we have different uh camera

**[10:48]** instance we have different uh camera

**[10:48]** instance we have different uh camera poses that are common from in Coco. So

**[10:51]** poses that are common from in Coco. So

**[10:51]** poses that are common from in Coco. So we have like aerial camera positioning

**[10:54]** we have like aerial camera positioning

**[10:54]** we have like aerial camera positioning uh which requires your model to sort of

**[10:57]** uh which requires your model to sort of

**[10:57]** uh which requires your model to sort of understand different views of an object

**[10:59]** understand different views of an object

**[10:59]** understand different views of an object in order to to do well. We have


### [11:00 - 12:00]

**[11:01]** in order to to do well. We have

**[11:01]** in order to to do well. We have different visual imaging domains like

**[11:03]** different visual imaging domains like

**[11:04]** different visual imaging domains like you can see like microscopes and X-rays

**[11:06]** you can see like microscopes and X-rays

**[11:06]** you can see like microscopes and X-rays and all this sort of things. Uh so yeah

**[11:10]** and all this sort of things. Uh so yeah

**[11:10]** and all this sort of things. Uh so yeah we think that this data set can measure

**[11:12]** we think that this data set can measure

**[11:12]** we think that this data set can measure the the richness of features that are

**[11:15]** the the richness of features that are

**[11:15]** the the richness of features that are learned by object detectors in a much

**[11:17]** learned by object detectors in a much

**[11:17]** learned by object detectors in a much more comprehensive way than Coco. Uh and

**[11:21]** more comprehensive way than Coco. Uh and

**[11:21]** more comprehensive way than Coco. Uh and here's some the the other fun thing

**[11:23]** here's some the the other fun thing

**[11:23]** here's some the the other fun thing about this is that it is a visual

**[11:24]** about this is that it is a visual

**[11:24]** about this is that it is a visual language model. So we were able to

**[11:26]** language model. So we were able to

**[11:26]** language model. So we were able to benchmark a bunch of different models on

**[11:29]** benchmark a bunch of different models on

**[11:29]** benchmark a bunch of different models on R100VL

**[11:30]** R100VL

**[11:30]** R100VL being able to ask them things like using

**[11:33]** being able to ask them things like using

**[11:33]** being able to ask them things like using contextualizing the class name in the

**[11:35]** contextualizing the class name in the

**[11:35]** contextualizing the class name in the context of this data set. Where where is

**[11:38]** context of this data set. Where where is

**[11:38]** context of this data set. Where where is this action happening for instance? So

**[11:39]** this action happening for instance? So

**[11:39]** this action happening for instance? So for so if you look at the top left we

**[11:42]** for so if you look at the top left we

**[11:42]** for so if you look at the top left we have this class which is block which is

**[11:44]** have this class which is block which is

**[11:44]** have this class which is block which is representing an action a volleyball

**[11:46]** representing an action a volleyball

**[11:46]** representing an action a volleyball block but you have to be smart enough to

**[11:48]** block but you have to be smart enough to

**[11:48]** block but you have to be smart enough to contextualize this like word embedding

**[11:50]** contextualize this like word embedding

**[11:50]** contextualize this like word embedding of block within the context of

**[11:51]** of block within the context of

**[11:51]** of block within the context of volleyball to be able to detect that.

**[11:53]** volleyball to be able to detect that.

**[11:53]** volleyball to be able to detect that. Same thing with this thunderbolt type uh

**[11:56]** Same thing with this thunderbolt type uh

**[11:56]** Same thing with this thunderbolt type uh defect in this cable here. If you just

**[11:58]** defect in this cable here. If you just

**[11:58]** defect in this cable here. If you just ask a a dumb visual language model to


### [12:00 - 13:00]

**[12:00]** ask a a dumb visual language model to

**[12:00]** ask a a dumb visual language model to detect thunderbolts in the image, it'll

**[12:02]** detect thunderbolts in the image, it'll

**[12:02]** detect thunderbolts in the image, it'll find nothing. But if it contextualizes

**[12:03]** find nothing. But if it contextualizes

**[12:04]** find nothing. But if it contextualizes it in the context of a cable defect,

**[12:06]** it in the context of a cable defect,

**[12:06]** it in the context of a cable defect, then it'll be able to find more things.

**[12:08]** then it'll be able to find more things.

**[12:08]** then it'll be able to find more things. And it also increases the breadth of

**[12:10]** And it also increases the breadth of

**[12:10]** And it also increases the breadth of classes. So if you only look at Coco,

**[12:13]** classes. So if you only look at Coco,

**[12:13]** classes. So if you only look at Coco, you're basically asking your model, hey,

**[12:15]** you're basically asking your model, hey,

**[12:15]** you're basically asking your model, hey, can you find a dog? Can you find a cat?

**[12:17]** can you find a dog? Can you find a cat?

**[12:17]** can you find a dog? Can you find a cat? But like, can you find fibrosis? Now

**[12:19]** But like, can you find fibrosis? Now

**[12:19]** But like, can you find fibrosis? Now your model needs to have like a lot more

**[12:21]** your model needs to have like a lot more

**[12:21]** your model needs to have like a lot more information around the world about the

**[12:22]** information around the world about the

**[12:22]** information around the world about the world to solve that problem. Same thing

**[12:25]** world to solve that problem. Same thing

**[12:25]** world to solve that problem. Same thing with different imaging domains.

**[12:28]** with different imaging domains.

**[12:28]** with different imaging domains. Um so it is a vision language benchmark.

**[12:31]** Um so it is a vision language benchmark.

**[12:31]** Um so it is a vision language benchmark. So we also have um visual descriptions

**[12:35]** So we also have um visual descriptions

**[12:35]** So we also have um visual descriptions uh and sort of instructions on how to

**[12:37]** uh and sort of instructions on how to

**[12:37]** uh and sort of instructions on how to find uh the objects that are present in

**[12:40]** find uh the objects that are present in

**[12:40]** find uh the objects that are present in this image. And basically what we found

**[12:42]** this image. And basically what we found

**[12:42]** this image. And basically what we found is like you take a Coco or you take a

**[12:45]** is like you take a Coco or you take a

**[12:45]** is like you take a Coco or you take a YOLO V8 model and you train it on like

**[12:47]** YOLO V8 model and you train it on like

**[12:47]** YOLO V8 model and you train it on like 10 examples per class. It does better

**[12:49]** 10 examples per class. It does better

**[12:49]** 10 examples per class. It does better than like Quen V272

**[12:52]** than like Quen V272

**[12:52]** than like Quen V272 Quinn 2.5VL 72B like state-of-the-art

**[12:55]** Quinn 2.5VL 72B like state-of-the-art

**[12:55]** Quinn 2.5VL 72B like state-of-the-art gigantic vision language model. So the

**[12:58]** gigantic vision language model. So the

**[12:58]** gigantic vision language model. So the vision language models are really good


### [13:00 - 14:00]

**[13:00]** vision language models are really good

**[13:00]** vision language models are really good right now at generalizing out of

**[13:02]** right now at generalizing out of

**[13:02]** right now at generalizing out of distribution in the vis in the

**[13:03]** distribution in the vis in the

**[13:03]** distribution in the vis in the linguistic domain but absolutely

**[13:05]** linguistic domain but absolutely

**[13:05]** linguistic domain but absolutely hopeless when it comes to generalizing

**[13:07]** hopeless when it comes to generalizing

**[13:07]** hopeless when it comes to generalizing in the visual domain. And so we hope

**[13:09]** in the visual domain. And so we hope

**[13:09]** in the visual domain. And so we hope that this benchmark can sort of drive

**[13:13]** that this benchmark can sort of drive

**[13:13]** that this benchmark can sort of drive that part of the the research and make

**[13:15]** that part of the the research and make

**[13:15]** that part of the the research and make sure that the visual parts of BLMs don't

**[13:18]** sure that the visual parts of BLMs don't

**[13:18]** sure that the visual parts of BLMs don't get left behind. Uh and yeah, basically

**[13:21]** get left behind. Uh and yeah, basically

**[13:21]** get left behind. Uh and yeah, basically by leveraging like stronger embeddings,

**[13:25]** by leveraging like stronger embeddings,

**[13:25]** by leveraging like stronger embeddings, uh a deter

**[13:27]** uh a deter

**[13:27]** uh a deter much better on R100VL than just

**[13:30]** much better on R100VL than just

**[13:30]** much better on R100VL than just leveraging embeddings learned on object

**[13:31]** leveraging embeddings learned on object

**[13:31]** leveraging embeddings learned on object 365, which makes sense. And that's my

**[13:34]** 365, which makes sense. And that's my

**[13:34]** 365, which makes sense. And that's my talk.

**[13:36]** talk.

**[13:36]** talk. Thank you.

**[13:37]** Thank you.

**[13:37]** Thank you. Yes. Can you fine it? Run it at the

**[13:40]** Yes. Can you fine it? Run it at the

**[13:40]** Yes. Can you fine it? Run it at the edge. Fine tune Quinn on the edge.

**[13:45]** edge. Fine tune Quinn on the edge.

**[13:45]** edge. Fine tune Quinn on the edge. Oh, yeah. Yeah. Yeah. It's It's like 20

**[13:47]** Oh, yeah. Yeah. Yeah. It's It's like 20

**[13:47]** Oh, yeah. Yeah. Yeah. It's It's like 20 million parameters at the smallest size.

**[13:49]** million parameters at the smallest size.

**[13:49]** million parameters at the smallest size. Yeah. Cool. Any other questions? It's

**[13:52]** Yeah. Cool. Any other questions? It's

**[13:52]** Yeah. Cool. Any other questions? It's Wix.


### [14:00 - 15:00]

**[14:01]** Yeah, it's publicly available. It's on

**[14:01]** Yeah, it's publicly available. It's on Maybe I can If you go to rf100vl.org, or

**[14:05]** Maybe I can If you go to rf100vl.org, or

**[14:05]** Maybe I can If you go to rf100vl.org, or you can find our archive paper as well

**[14:08]** you can find our archive paper as well

**[14:08]** you can find our archive paper as well as the code utilities to help download

**[14:11]** as the code utilities to help download

**[14:11]** as the code utilities to help download the data set. It's also like on hugging

**[14:13]** the data set. It's also like on hugging

**[14:13]** the data set. It's also like on hugging face somewhere. Yeah.

**[14:21]** Yeah. So, Rooflow kind of has a pretty

**[14:22]** Yeah. So, Rooflow kind of has a pretty unique strategy when it comes to our

**[14:25]** unique strategy when it comes to our

**[14:25]** unique strategy when it comes to our platform. So, we make our platform

**[14:26]** platform. So, we make our platform

**[14:26]** platform. So, we make our platform freely available to all researchers

**[14:28]** freely available to all researchers

**[14:28]** freely available to all researchers basically. And so we have like a ton of

**[14:30]** basically. And so we have like a ton of

**[14:30]** basically. And so we have like a ton of people who use our platform to label

**[14:33]** people who use our platform to label

**[14:33]** people who use our platform to label medical data and biological data for

**[14:35]** medical data and biological data for

**[14:35]** medical data and biological data for their own papers and their own research.

**[14:38]** their own papers and their own research.

**[14:38]** their own papers and their own research. And then our only ask is that they then

**[14:41]** And then our only ask is that they then

**[14:41]** And then our only ask is that they then contribute that data back to the

**[14:42]** contribute that data back to the

**[14:42]** contribute that data back to the community and make it open source. And

**[14:44]** community and make it open source. And

**[14:44]** community and make it open source. And so a lot of this data comes from like

**[14:45]** so a lot of this data comes from like

**[14:45]** so a lot of this data comes from like papers cited in nature and stuff like

**[14:47]** papers cited in nature and stuff like

**[14:47]** papers cited in nature and stuff like that.

**[14:50]** that.

**[14:50]** that. two

**[14:52]** two

**[14:52]** two correspondence between


### [15:00 - 16:00]

**[15:17]** Yeah. So the data set is kind of

**[15:17]** Yeah. So the data set is kind of measuring the performance of like a

**[15:18]** measuring the performance of like a

**[15:18]** measuring the performance of like a bunch of different imaging modalities or

**[15:22]** bunch of different imaging modalities or

**[15:22]** bunch of different imaging modalities or predictive modalities I guess. So so I

**[15:25]** predictive modalities I guess. So so I

**[15:25]** predictive modalities I guess. So so I think the most interesting tract of the

**[15:27]** think the most interesting tract of the

**[15:27]** think the most interesting tract of the data set is the fshot tract. So

**[15:29]** data set is the fshot tract. So

**[15:29]** data set is the fshot tract. So basically we've constructed like uh

**[15:33]** basically we've constructed like uh

**[15:33]** basically we've constructed like uh canonical 10shot splits. So we provide

**[15:37]** canonical 10shot splits. So we provide

**[15:37]** canonical 10shot splits. So we provide the model the class name uh annotator

**[15:40]** the model the class name uh annotator

**[15:40]** the model the class name uh annotator instructions on how to find that class

**[15:42]** instructions on how to find that class

**[15:42]** instructions on how to find that class as well as 10 visual examples per class.

**[15:45]** as well as 10 visual examples per class.

**[15:45]** as well as 10 visual examples per class. And if a model basically no model exists

**[15:48]** And if a model basically no model exists

**[15:48]** And if a model basically no model exists that can leverage those three things and

**[15:50]** that can leverage those three things and

**[15:50]** that can leverage those three things and get higher map than if you just deleted

**[15:53]** get higher map than if you just deleted

**[15:53]** get higher map than if you just deleted one of those like options. I I see that

**[15:55]** one of those like options. I I see that

**[15:55]** one of those like options. I I see that as one of the big shortcomings of visual

**[15:57]** as one of the big shortcomings of visual

**[15:57]** as one of the big shortcomings of visual language models right now. Then in terms


### [16:00 - 17:00]

**[16:00]** language models right now. Then in terms

**[16:00]** language models right now. Then in terms of multiple

**[16:02]** of multiple

**[16:02]** of multiple there's like more generous kind of

**[16:03]** there's like more generous kind of

**[16:03]** there's like more generous kind of things like

**[16:26]** yeah so so currently the specialists are

**[16:26]** yeah so so currently the specialists are by far the best uh we benchmark

**[16:28]** by far the best uh we benchmark

**[16:28]** by far the best uh we benchmark grounding dyno specifically both zero

**[16:31]** grounding dyno specifically both zero

**[16:31]** grounding dyno specifically both zero shot and fine tune. So zero shot

**[16:32]** shot and fine tune. So zero shot

**[16:32]** shot and fine tune. So zero shot grounding dyno got like 19 map average

**[16:34]** grounding dyno got like 19 map average

**[16:34]** grounding dyno got like 19 map average on R100VL which is like kind of good

**[16:37]** on R100VL which is like kind of good

**[16:37]** on R100VL which is like kind of good kind of bad. So if you take like a YOLO

**[16:39]** kind of bad. So if you take like a YOLO

**[16:39]** kind of bad. So if you take like a YOLO V8 nano and you train it from scratch on

**[16:41]** V8 nano and you train it from scratch on

**[16:41]** V8 nano and you train it from scratch on the 10shot examples which is not a lot

**[16:43]** the 10shot examples which is not a lot

**[16:43]** the 10shot examples which is not a lot of data obviously it gets something like

**[16:45]** of data obviously it gets something like

**[16:45]** of data obviously it gets something like 25 map. So like to to be worse than

**[16:48]** 25 map. So like to to be worse than

**[16:48]** 25 map. So like to to be worse than fine-tuning a YOLO from scratch is is

**[16:50]** fine-tuning a YOLO from scratch is is

**[16:50]** fine-tuning a YOLO from scratch is is sort of bad. But if you then fine-tune

**[16:52]** sort of bad. But if you then fine-tune

**[16:52]** sort of bad. But if you then fine-tune the grounding dyno with federated loss

**[16:54]** the grounding dyno with federated loss

**[16:54]** the grounding dyno with federated loss that's the highest performing model we

**[16:56]** that's the highest performing model we

**[16:56]** that's the highest performing model we have on the data set. However, that

**[16:58]** have on the data set. However, that

**[16:58]** have on the data set. However, that being said, like I think that the point


### [17:00 - 18:00]

**[17:00]** being said, like I think that the point

**[17:00]** being said, like I think that the point of the data set should be, hey, like you

**[17:03]** of the data set should be, hey, like you

**[17:03]** of the data set should be, hey, like you should be able to leverage these

**[17:04]** should be able to leverage these

**[17:04]** should be able to leverage these annotator instructions, the 10shot

**[17:06]** annotator instructions, the 10shot

**[17:06]** annotator instructions, the 10shot examples, and the class names and come

**[17:09]** examples, and the class names and come

**[17:09]** examples, and the class names and come up with something more accurate, which

**[17:10]** up with something more accurate, which

**[17:10]** up with something more accurate, which requires a journalist model. But, okay,

**[17:12]** requires a journalist model. But, okay,

**[17:12]** requires a journalist model. But, okay, I think I'm super overtime. So, yeah,

**[17:15]** I think I'm super overtime. So, yeah,

**[17:15]** I think I'm super overtime. So, yeah, thanks for the questions. Cool. Thanks

**[17:17]** thanks for the questions. Cool. Thanks

**[17:17]** thanks for the questions. Cool. Thanks everyone.


