# Perceptual Evaluations- Evals for Aesthetics — Diego Rodriguez, Krea.ai

**Video URL:** https://www.youtube.com/watch?v=h5ItAJuB3Fc

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Okay. So, hello everyone. Uh, my name is

**[00:17]** Okay. So, hello everyone. Uh, my name is Diego Rodriguez. Uh, I'm the co-founder

**[00:20]** Diego Rodriguez. Uh, I'm the co-founder

**[00:20]** Diego Rodriguez. Uh, I'm the co-founder of Korea, a startup in the AI space like

**[00:23]** of Korea, a startup in the AI space like

**[00:23]** of Korea, a startup in the AI space like many others. uh in particular generative

**[00:25]** many others. uh in particular generative

**[00:25]** many others. uh in particular generative media, multimedia, multimodel and all

**[00:28]** media, multimedia, multimodel and all

**[00:28]** media, multimedia, multimodel and all the uh buzzwords but uh I come here

**[00:31]** the uh buzzwords but uh I come here

**[00:32]** the uh buzzwords but uh I come here mainly to tell a story about

**[00:35]** mainly to tell a story about

**[00:35]** mainly to tell a story about [Music]

**[00:36]** [Music]

**[00:36]** [Music] how we think about evaluations

**[00:40]** how we think about evaluations

**[00:40]** how we think about evaluations when we have to take into account human

**[00:43]** when we have to take into account human

**[00:43]** when we have to take into account human perception and human opinion and

**[00:45]** perception and human opinion and

**[00:45]** perception and human opinion and aesthetics uh into the mix. Right? So

**[00:48]** aesthetics uh into the mix. Right? So

**[00:48]** aesthetics uh into the mix. Right? So I'm going to start with a very simple

**[00:49]** I'm going to start with a very simple

**[00:50]** I'm going to start with a very simple story. is like I put an AI generated

**[00:53]** story. is like I put an AI generated

**[00:53]** story. is like I put an AI generated image of a hand obviously it looks

**[00:55]** image of a hand obviously it looks

**[00:55]** image of a hand obviously it looks horrible and then I ask 03 what do you

**[00:58]** horrible and then I ask 03 what do you

**[00:58]** horrible and then I ask 03 what do you think of this image then he thought for


### [01:00 - 02:00]

**[01:00]** think of this image then he thought for

**[01:00]** think of this image then he thought for 17 seconds obviously tool calling does

**[01:03]** 17 seconds obviously tool calling does

**[01:03]** 17 seconds obviously tool calling does Python analysis opencv goes crazy and

**[01:06]** Python analysis opencv goes crazy and

**[01:06]** Python analysis opencv goes crazy and then after he charges me a few cents is

**[01:09]** then after he charges me a few cents is

**[01:09]** then after he charges me a few cents is like oh just a couple multar is like

**[01:11]** like oh just a couple multar is like

**[01:11]** like oh just a couple multar is like it's mostly natural but like and it's

**[01:14]** it's mostly natural but like and it's

**[01:14]** it's mostly natural but like and it's like okay we have like what many people

**[01:16]** like okay we have like what many people

**[01:16]** like okay we have like what many people claim is basically AGI and it is

**[01:20]** claim is basically AGI and it is

**[01:20]** claim is basically AGI and it is completely unable of answering a very

**[01:22]** completely unable of answering a very

**[01:22]** completely unable of answering a very simple question and

**[01:25]** simple question and

**[01:26]** simple question and and like

**[01:28]** and like

**[01:28]** and like that's it that's a surprising thing if

**[01:30]** that's it that's a surprising thing if

**[01:30]** that's it that's a surprising thing if you think about it because we as humans

**[01:33]** you think about it because we as humans

**[01:33]** you think about it because we as humans when people see that image is like we

**[01:35]** when people see that image is like we

**[01:35]** when people see that image is like we just react so naturally right against

**[01:37]** just react so naturally right against

**[01:37]** just react so naturally right against that it's like what is that like that

**[01:38]** that it's like what is that like that

**[01:38]** that it's like what is that like that that's not natural and and I feel like

**[01:41]** that's not natural and and I feel like

**[01:41]** that's not natural and and I feel like that's precisely what AI models are

**[01:42]** that's precisely what AI models are

**[01:42]** that's precisely what AI models are being trained on a on human data right

**[01:46]** being trained on a on human data right

**[01:46]** being trained on a on human data right uh uh second on human preference data

**[01:49]** uh uh second on human preference data

**[01:50]** uh uh second on human preference data uh and and third like in a way limited

**[01:53]** uh and and third like in a way limited

**[01:54]** uh and and third like in a way limited by the data that we humans ba based on

**[01:58]** by the data that we humans ba based on

**[01:58]** by the data that we humans ba based on our preconceived notions and perception


### [02:00 - 03:00]

**[02:00]** our preconceived notions and perception

**[02:00]** our preconceived notions and perception and all of that. So that's what this

**[02:03]** and all of that. So that's what this

**[02:03]** and all of that. So that's what this talk is about about why what um what can

**[02:07]** talk is about about why what um what can

**[02:07]** talk is about about why what um what can we do better and honestly

**[02:10]** we do better and honestly

**[02:10]** we do better and honestly to ask ourselves some questions that I

**[02:12]** to ask ourselves some questions that I

**[02:12]** to ask ourselves some questions that I think are not being asked enough in the

**[02:13]** think are not being asked enough in the

**[02:13]** think are not being asked enough in the field. Um cool. So tiny tiny bit of

**[02:18]** field. Um cool. So tiny tiny bit of

**[02:18]** field. Um cool. So tiny tiny bit of history. Uh there's uh we all know about

**[02:22]** history. Uh there's uh we all know about

**[02:22]** history. Uh there's uh we all know about Claude uh Claude Shannon that is the the

**[02:26]** Claude uh Claude Shannon that is the the

**[02:26]** Claude uh Claude Shannon that is the the father of information theory

**[02:29]** father of information theory

**[02:29]** father of information theory uh and according to many his master

**[02:31]** uh and according to many his master

**[02:31]** uh and according to many his master thesis one of the most important master

**[02:32]** thesis one of the most important master

**[02:32]** thesis one of the most important master thesis in the world where he laid

**[02:34]** thesis in the world where he laid

**[02:34]** thesis in the world where he laid foundations for digital circuits and

**[02:37]** foundations for digital circuits and

**[02:37]** foundations for digital circuits and then eventually communication and all

**[02:39]** then eventually communication and all

**[02:39]** then eventually communication and all and to a degree we can say that even

**[02:42]** and to a degree we can say that even

**[02:42]** and to a degree we can say that even LLMs uh nowadays right if we fast

**[02:45]** LLMs uh nowadays right if we fast

**[02:45]** LLMs uh nowadays right if we fast forward

**[02:47]** forward

**[02:47]** forward um and I want

**[02:49]** um and I want

**[02:49]** um and I want I want to focus on the inform all the

**[02:52]** I want to focus on the inform all the

**[02:52]** I want to focus on the inform all the like the fact that we

**[02:56]** like the fact that we

**[02:56]** like the fact that we call his work foundational and

**[02:58]** call his work foundational and

**[02:58]** call his work foundational and information theory. Well, when he


### [03:00 - 04:00]

**[03:00]** information theory. Well, when he

**[03:00]** information theory. Well, when he published it, it was actually called

**[03:03]** published it, it was actually called

**[03:03]** published it, it was actually called like mathematical foundation for

**[03:05]** like mathematical foundation for

**[03:05]** like mathematical foundation for communication theory and he was always

**[03:07]** communication theory and he was always

**[03:07]** communication theory and he was always focused on communication. um there's

**[03:11]** focused on communication. um there's

**[03:11]** focused on communication. um there's this image uh appears on that work uh

**[03:14]** this image uh appears on that work uh

**[03:14]** this image uh appears on that work uh and it's all about okay this is the

**[03:16]** and it's all about okay this is the

**[03:16]** and it's all about okay this is the source this is the channel this is

**[03:18]** source this is the channel this is

**[03:18]** source this is the channel this is nation there can be some noise there

**[03:21]** nation there can be some noise there

**[03:21]** nation there can be some noise there um

**[03:22]** um

**[03:22]** um and as a well as a founder of a company

**[03:25]** and as a well as a founder of a company

**[03:25]** and as a well as a founder of a company that is focusing on on media

**[03:28]** that is focusing on on media

**[03:28]** that is focusing on on media to me is interesting to realize like

**[03:33]** to me is interesting to realize like

**[03:33]** to me is interesting to realize like these parallels between classic

**[03:35]** these parallels between classic

**[03:35]** these parallels between classic information theory and communication

**[03:39]** information theory and communication

**[03:39]** information theory and communication Let me see. Did I put the image? Let's

**[03:41]** Let me see. Did I put the image? Let's

**[03:41]** Let me see. Did I put the image? Let's see. Well, if you I didn't put the

**[03:43]** see. Well, if you I didn't put the

**[03:43]** see. Well, if you I didn't put the image, but if you have any context

**[03:45]** image, but if you have any context

**[03:46]** image, but if you have any context around variational autoenccoders or

**[03:48]** around variational autoenccoders or

**[03:48]** around variational autoenccoders or neural networks or whatever, you you can

**[03:50]** neural networks or whatever, you you can

**[03:50]** neural networks or whatever, you you can squint and be like, oh, is that a neural

**[03:51]** squint and be like, oh, is that a neural

**[03:51]** squint and be like, oh, is that a neural network, right?

**[03:53]** network, right?

**[03:53]** network, right? Um

**[03:55]** Um

**[03:55]** Um and in the context of information and

**[03:59]** and in the context of information and

**[03:59]** and in the context of information and communication I want to talk about how


### [04:00 - 05:00]

**[04:02]** communication I want to talk about how

**[04:02]** communication I want to talk about how compression is going to be uh related to

**[04:07]** compression is going to be uh related to

**[04:07]** compression is going to be uh related to how we think about evaluation right in

**[04:09]** how we think about evaluation right in

**[04:09]** how we think about evaluation right in I'm going to talk in for example on JPEG

**[04:14]** I'm going to talk in for example on JPEG

**[04:14]** I'm going to talk in for example on JPEG um JPEG exploits

**[04:18]** um JPEG exploits

**[04:18]** um JPEG exploits like human nature in the sense that we

**[04:20]** like human nature in the sense that we

**[04:20]** like human nature in the sense that we are very sensitive to brightness but not

**[04:22]** are very sensitive to brightness but not

**[04:22]** are very sensitive to brightness but not so much to color and this is a illusion

**[04:24]** so much to color and this is a illusion

**[04:24]** so much to color and this is a illusion that also talks about that where A and B

**[04:26]** that also talks about that where A and B

**[04:26]** that also talks about that where A and B is actually the same color but we are

**[04:28]** is actually the same color but we are

**[04:28]** is actually the same color but we are basically unable to perceive it until we

**[04:30]** basically unable to perceive it until we

**[04:30]** basically unable to perceive it until we do this and then suddenly it's like oh

**[04:32]** do this and then suddenly it's like oh

**[04:32]** do this and then suddenly it's like oh really um and it's kind of like what's

**[04:34]** really um and it's kind of like what's

**[04:34]** really um and it's kind of like what's going on there right

**[04:37]** going on there right

**[04:37]** going on there right um and so JPEG just does the same thing

**[04:39]** um and so JPEG just does the same thing

**[04:39]** um and so JPEG just does the same thing where okay we have RGB color space to

**[04:41]** where okay we have RGB color space to

**[04:41]** where okay we have RGB color space to represent images with computers uh we

**[04:45]** represent images with computers uh we

**[04:45]** represent images with computers uh we notice that there's a diagonal that

**[04:47]** notice that there's a diagonal that

**[04:47]** notice that there's a diagonal that represents the brightness of the images

**[04:49]** represents the brightness of the images

**[04:49]** represents the brightness of the images we can change into a different color

**[04:51]** we can change into a different color

**[04:51]** we can change into a different color space uh that separates color versus

**[04:53]** space uh that separates color versus

**[04:53]** space uh that separates color versus brightness and then we can down sample

**[04:56]** brightness and then we can down sample

**[04:56]** brightness and then we can down sample the channels around color because we are

**[04:59]** the channels around color because we are

**[04:59]** the channels around color because we are actually not even that done sensitive to


### [05:00 - 06:00]

**[05:00]** actually not even that done sensitive to

**[05:00]** actually not even that done sensitive to it. So we can remove that or parts of it

**[05:04]** it. So we can remove that or parts of it

**[05:04]** it. So we can remove that or parts of it and then uh once we do that this is an

**[05:07]** and then uh once we do that this is an

**[05:07]** and then uh once we do that this is an image where we can see the uh brightness

**[05:09]** image where we can see the uh brightness

**[05:09]** image where we can see the uh brightness and color component separated. Once we

**[05:11]** and color component separated. Once we

**[05:12]** and color component separated. Once we down sample, we can try to recreate the

**[05:13]** down sample, we can try to recreate the

**[05:13]** down sample, we can try to recreate the image. And this is an example of like

**[05:16]** image. And this is an example of like

**[05:16]** image. And this is an example of like basically original image and then the

**[05:19]** basically original image and then the

**[05:19]** basically original image and then the image with the down sample color looks

**[05:21]** image with the down sample color looks

**[05:21]** image with the down sample color looks the same to us. Uh, and the image is

**[05:23]** the same to us. Uh, and the image is

**[05:23]** the same to us. Uh, and the image is like 50% less information, right?

**[05:28]** like 50% less information, right?

**[05:28]** like 50% less information, right? And other stuff. There's Huffman Huffman

**[05:31]** And other stuff. There's Huffman Huffman

**[05:31]** And other stuff. There's Huffman Huffman coding and more stuff, but like the

**[05:34]** coding and more stuff, but like the

**[05:34]** coding and more stuff, but like the point is the right. And then the thing

**[05:36]** point is the right. And then the thing

**[05:36]** point is the right. And then the thing is if you exploit the same for audio

**[05:41]** is if you exploit the same for audio

**[05:41]** is if you exploit the same for audio like what can we hear? What can we not

**[05:42]** like what can we hear? What can we not

**[05:42]** like what can we hear? What can we not hear? Well, you you do the same and we

**[05:44]** hear? Well, you you do the same and we

**[05:44]** hear? Well, you you do the same and we have MP3. And then if you do the exact

**[05:47]** have MP3. And then if you do the exact

**[05:47]** have MP3. And then if you do the exact same thing across time, well, congrats.

**[05:49]** same thing across time, well, congrats.

**[05:49]** same thing across time, well, congrats. Now you have MP4. It's like it's all

**[05:51]** Now you have MP4. It's like it's all

**[05:51]** Now you have MP4. It's like it's all this principle of like let's exploit how

**[05:54]** this principle of like let's exploit how

**[05:54]** this principle of like let's exploit how we humans perceive the world, right? Um,

**[05:58]** we humans perceive the world, right? Um,

**[05:58]** we humans perceive the world, right? Um, but this made me think about myself


### [06:00 - 07:00]

**[06:00]** but this made me think about myself

**[06:00]** but this made me think about myself because I studied artificial systems

**[06:03]** because I studied artificial systems

**[06:03]** because I studied artificial systems engineering, which is engineering around

**[06:05]** engineering, which is engineering around

**[06:05]** engineering, which is engineering around all of these mic how microphones work,

**[06:07]** all of these mic how microphones work,

**[06:07]** all of these mic how microphones work, how speakers work. And it was just

**[06:10]** how speakers work. And it was just

**[06:10]** how speakers work. And it was just interesting to me that I was coding. I

**[06:13]** interesting to me that I was coding. I

**[06:13]** interesting to me that I was coding. I start deleting information. I know for a

**[06:15]** start deleting information. I know for a

**[06:16]** start deleting information. I know for a fact that I'm deleting information yet

**[06:17]** fact that I'm deleting information yet

**[06:17]** fact that I'm deleting information yet and then I rerender the image and I see

**[06:20]** and then I rerender the image and I see

**[06:20]** and then I rerender the image and I see the same. is like like philosophers

**[06:23]** the same. is like like philosophers

**[06:23]** the same. is like like philosophers always tell you about like oh we are

**[06:24]** always tell you about like oh we are

**[06:24]** always tell you about like oh we are limited by our senses but like this is

**[06:26]** limited by our senses but like this is

**[06:26]** limited by our senses but like this is the first time I was like I'm seeing it

**[06:28]** the first time I was like I'm seeing it

**[06:28]** the first time I was like I'm seeing it right like I am not seeing the

**[06:29]** right like I am not seeing the

**[06:29]** right like I am not seeing the difference um

**[06:33]** difference um

**[06:33]** difference um but then

**[06:36]** but then

**[06:36]** but then if all if if a lot of our data is the

**[06:39]** if all if if a lot of our data is the

**[06:39]** if all if if a lot of our data is the internet right like we're stripping data

**[06:41]** internet right like we're stripping data

**[06:41]** internet right like we're stripping data from the internet bunch of those images

**[06:43]** from the internet bunch of those images

**[06:43]** from the internet bunch of those images are also compressed right like are we

**[06:45]** are also compressed right like are we

**[06:45]** are also compressed right like are we taking into account that perhaps our AIS

**[06:47]** taking into account that perhaps our AIS

**[06:47]** taking into account that perhaps our AIS are limited too because we're kind cont

**[06:51]** are limited too because we're kind cont

**[06:51]** are limited too because we're kind cont like

**[06:53]** like

**[06:53]** like we have some sort of contagion going on

**[06:55]** we have some sort of contagion going on

**[06:55]** we have some sort of contagion going on of our flaws into the AI. Um


### [07:00 - 08:00]

**[07:00]** of our flaws into the AI. Um

**[07:00]** of our flaws into the AI. Um and then it gets more tricky because for

**[07:03]** and then it gets more tricky because for

**[07:03]** and then it gets more tricky because for instance uh this is a just a screenshot

**[07:05]** instance uh this is a just a screenshot

**[07:05]** instance uh this is a just a screenshot I took from a paper I think it's called

**[07:07]** I took from a paper I think it's called

**[07:07]** I took from a paper I think it's called clean FID and FID scores for all of you

**[07:11]** clean FID and FID scores for all of you

**[07:11]** clean FID and FID scores for all of you who don't have context is one of the

**[07:14]** who don't have context is one of the

**[07:14]** who don't have context is one of the standard metrics used for uh how well

**[07:17]** standard metrics used for uh how well

**[07:17]** standard metrics used for uh how well for instance diffusion models are are

**[07:18]** for instance diffusion models are are

**[07:18]** for instance diffusion models are are reproducing an image but then you start

**[07:20]** reproducing an image but then you start

**[07:20]** reproducing an image but then you start adding JPEG artifacts and the score is

**[07:22]** adding JPEG artifacts and the score is

**[07:22]** adding JPEG artifacts and the score is like oh no no no this is horrible

**[07:23]** like oh no no no this is horrible

**[07:23]** like oh no no no this is horrible horrible image and it's like

**[07:25]** horrible image and it's like

**[07:25]** horrible image and it's like perceptually the four images are

**[07:27]** perceptually the four images are

**[07:27]** perceptually the four images are basically the same yet the FID score is

**[07:30]** basically the same yet the FID score is

**[07:30]** basically the same yet the FID score is like no no no this is really bad. So

**[07:32]** like no no no this is really bad. So

**[07:32]** like no no no this is really bad. So then it's like why are we using FID

**[07:35]** then it's like why are we using FID

**[07:35]** then it's like why are we using FID scores or metrics along those lines to

**[07:37]** scores or metrics along those lines to

**[07:37]** scores or metrics along those lines to deci to decide oh this generative AI

**[07:40]** deci to decide oh this generative AI

**[07:40]** deci to decide oh this generative AI model is good or bad right

**[07:43]** model is good or bad right

**[07:43]** model is good or bad right um

**[07:44]** um

**[07:44]** um so the thing is sometimes I feel like we

**[07:47]** so the thing is sometimes I feel like we

**[07:47]** so the thing is sometimes I feel like we are focused on measuring just things

**[07:48]** are focused on measuring just things

**[07:48]** are focused on measuring just things that are easy to measure right like

**[07:51]** that are easy to measure right like

**[07:51]** that are easy to measure right like problem adher adherence with clip how

**[07:54]** problem adher adherence with clip how

**[07:54]** problem adher adherence with clip how many objects are there is this blue is

**[07:56]** many objects are there is this blue is

**[07:56]** many objects are there is this blue is this red etc

**[07:59]** this red etc

**[07:59]** this red etc but


### [08:00 - 09:00]

**[08:01]** but

**[08:01]** but what about here. Oh, it's like, oh no,

**[08:03]** what about here. Oh, it's like, oh no,

**[08:03]** what about here. Oh, it's like, oh no, really bad, really bad generator because

**[08:06]** really bad, really bad generator because

**[08:06]** really bad, really bad generator because that's not how clock looks and the sky

**[08:08]** that's not how clock looks and the sky

**[08:08]** that's not how clock looks and the sky that makes no sense. And it's like,

**[08:09]** that makes no sense. And it's like,

**[08:09]** that makes no sense. And it's like, okay, how

**[08:18]** not only are we limiting our AIS by our

**[08:18]** not only are we limiting our AIS by our human perceptions? Uh, on top of that,

**[08:21]** human perceptions? Uh, on top of that,

**[08:21]** human perceptions? Uh, on top of that, we forget about the relativity of

**[08:25]** we forget about the relativity of

**[08:25]** we forget about the relativity of metrics, right? like uh no actually this

**[08:28]** metrics, right? like uh no actually this

**[08:28]** metrics, right? like uh no actually this is art and this is great and and and and

**[08:30]** is art and this is great and and and and

**[08:30]** is art and this is great and and and and there's sometimes meaning behind the

**[08:33]** there's sometimes meaning behind the

**[08:33]** there's sometimes meaning behind the work that is not like it is conveyed in

**[08:36]** work that is not like it is conveyed in

**[08:36]** work that is not like it is conveyed in the image but only if you're human you

**[08:38]** the image but only if you're human you

**[08:38]** the image but only if you're human you you get it right like oh this is what

**[08:40]** you get it right like oh this is what

**[08:40]** you get it right like oh this is what the author is trying to tell me but I

**[08:42]** the author is trying to tell me but I

**[08:42]** the author is trying to tell me but I feel like the metrics don't show that

**[08:44]** feel like the metrics don't show that

**[08:44]** feel like the metrics don't show that and kind like

**[08:46]** and kind like

**[08:46]** and kind like commercially and professionally my job

**[08:47]** commercially and professionally my job

**[08:48]** commercially and professionally my job is kind of like okay how can we make a

**[08:50]** is kind of like okay how can we make a

**[08:50]** is kind of like okay how can we make a company that

**[08:53]** company that

**[08:53]** company that allows creatives artists is of all

**[08:56]** allows creatives artists is of all

**[08:56]** allows creatives artists is of all sorts. Uh we can start with image, we

**[08:58]** sorts. Uh we can start with image, we

**[08:58]** sorts. Uh we can start with image, we can start with video, but to better


### [09:00 - 10:00]

**[09:00]** can start with video, but to better

**[09:00]** can start with video, but to better express themselves. But how are we

**[09:02]** express themselves. But how are we

**[09:02]** express themselves. But how are we supposed to do that if this is kind of

**[09:03]** supposed to do that if this is kind of

**[09:03]** supposed to do that if this is kind of like the state-of-the-art, right? Um

**[09:07]** like the state-of-the-art, right? Um

**[09:07]** like the state-of-the-art, right? Um then

**[09:09]** then

**[09:09]** then a friend of mine uh Changloo actually

**[09:12]** a friend of mine uh Changloo actually

**[09:12]** a friend of mine uh Changloo actually works at at Mid Journey. it was uh he

**[09:15]** works at at Mid Journey. it was uh he

**[09:15]** works at at Mid Journey. it was uh he has um

**[09:17]** has um

**[09:18]** has um like he has great talks that you should

**[09:20]** like he has great talks that you should

**[09:20]** like he has great talks that you should all check but he told me once a little

**[09:23]** all check but he told me once a little

**[09:24]** all check but he told me once a little bit over a year ago a quote that I just

**[09:26]** bit over a year ago a quote that I just

**[09:26]** bit over a year ago a quote that I just can't stop thinking about which goes

**[09:28]** can't stop thinking about which goes

**[09:28]** can't stop thinking about which goes something like

**[09:30]** something like

**[09:30]** something like hey man if you think about it like

**[09:34]** hey man if you think about it like

**[09:34]** hey man if you think about it like predicting the car back when everything

**[09:36]** predicting the car back when everything

**[09:36]** predicting the car back when everything was horses it's not that hard I was like

**[09:39]** was horses it's not that hard I was like

**[09:39]** was horses it's not that hard I was like well like yeah it's not that hard to to

**[09:41]** well like yeah it's not that hard to to

**[09:41]** well like yeah it's not that hard to to like oh cars are the future and whatever

**[09:42]** like oh cars are the future and whatever

**[09:42]** like oh cars are the future and whatever it's like we have We have a thing that

**[09:44]** it's like we have We have a thing that

**[09:44]** it's like we have We have a thing that goes like this. We have horses that make

**[09:46]** goes like this. We have horses that make

**[09:46]** goes like this. We have horses that make energy. So, you swap the thing for the

**[09:48]** energy. So, you swap the thing for the

**[09:48]** energy. So, you swap the thing for the engine. That's essentially a car, right?

**[09:51]** engine. That's essentially a car, right?

**[09:51]** engine. That's essentially a car, right? I was like, come on, how hard is that?

**[09:52]** I was like, come on, how hard is that?

**[09:52]** I was like, come on, how hard is that? It's like, you know what's hard to

**[09:53]** It's like, you know what's hard to

**[09:53]** It's like, you know what's hard to predict? Traffic,

**[09:56]** predict? Traffic,

**[09:56]** predict? Traffic, right? And and then I just kept thinking

**[09:58]** right? And and then I just kept thinking

**[09:58]** right? And and then I just kept thinking about I was like, oh man, like as


### [10:00 - 11:00]

**[10:00]** about I was like, oh man, like as

**[10:00]** about I was like, oh man, like as engineers, as researchers, as founders,

**[10:03]** engineers, as researchers, as founders,

**[10:03]** engineers, as researchers, as founders, what are the traffics that we're missing

**[10:05]** what are the traffics that we're missing

**[10:05]** what are the traffics that we're missing now? Because I feel like everyone's

**[10:07]** now? Because I feel like everyone's

**[10:07]** now? Because I feel like everyone's focused on like, yeah, but you can you

**[10:09]** focused on like, yeah, but you can you

**[10:09]** focused on like, yeah, but you can you can I don't know transform from JSON to

**[10:11]** can I don't know transform from JSON to

**[10:11]** can I don't know transform from JSON to JAMAL and like who cares that dude? who

**[10:13]** JAMAL and like who cares that dude? who

**[10:13]** JAMAL and like who cares that dude? who cares like or or yes it's important

**[10:15]** cares like or or yes it's important

**[10:15]** cares like or or yes it's important right like but

**[10:19]** right like but

**[10:19]** right like but what kind of big picture are we all

**[10:22]** what kind of big picture are we all

**[10:22]** what kind of big picture are we all missing right um then he talks about

**[10:26]** missing right um then he talks about

**[10:26]** missing right um then he talks about well you know the myth of the Tower of

**[10:28]** well you know the myth of the Tower of

**[10:28]** well you know the myth of the Tower of Babel where

**[10:36]** in a nutshell is like

**[10:36]** in a nutshell is like God like we want to go and

**[10:41]** God like we want to go and

**[10:41]** God like we want to go and meet God and then he's No, I don't want

**[10:43]** meet God and then he's No, I don't want

**[10:43]** meet God and then he's No, I don't want that. So, instead, I'm just going to

**[10:45]** that. So, instead, I'm just going to

**[10:45]** that. So, instead, I'm just going to confuse all of you, and then you're not

**[10:48]** confuse all of you, and then you're not

**[10:48]** confuse all of you, and then you're not going to be able to uh coordinate. Uh,

**[10:51]** going to be able to uh coordinate. Uh,

**[10:51]** going to be able to uh coordinate. Uh, and then you're all each one is going to

**[10:53]** and then you're all each one is going to

**[10:53]** and then you're all each one is going to speak a different language, and then

**[10:54]** speak a different language, and then

**[10:54]** speak a different language, and then it's just basically going to be

**[10:55]** it's just basically going to be

**[10:55]** it's just basically going to be impossible to keep the thing going,

**[10:57]** impossible to keep the thing going,

**[10:57]** impossible to keep the thing going, which like reminds me of like a standard


### [11:00 - 12:00]

**[11:00]** which like reminds me of like a standard

**[11:00]** which like reminds me of like a standard infrastructure meetings with backend

**[11:02]** infrastructure meetings with backend

**[11:02]** infrastructure meetings with backend engineers. It's like, oh no, we should

**[11:03]** engineers. It's like, oh no, we should

**[11:03]** engineers. It's like, oh no, we should use Kubernetes. No, we should just And

**[11:05]** use Kubernetes. No, we should just And

**[11:05]** use Kubernetes. No, we should just And it's like it's just all fighting and

**[11:06]** it's like it's just all fighting and

**[11:06]** it's like it's just all fighting and whatever. Nothing get nothing gets

**[11:08]** whatever. Nothing get nothing gets

**[11:08]** whatever. Nothing get nothing gets built. I'm like, dude, God is winning.

**[11:10]** built. I'm like, dude, God is winning.

**[11:10]** built. I'm like, dude, God is winning. God damn it. Um but then this makes me

**[11:15]** God damn it. Um but then this makes me

**[11:15]** God damn it. Um but then this makes me think about like

**[11:17]** think about like

**[11:17]** think about like we are now in we just entered the age

**[11:21]** we are now in we just entered the age

**[11:21]** we are now in we just entered the age where you can have

**[11:23]** where you can have

**[11:23]** where you can have models

**[11:25]** models

**[11:25]** models essentially they solve translation right

**[11:27]** essentially they solve translation right

**[11:27]** essentially they solve translation right or they solved it to a very high degree.

**[11:30]** or they solved it to a very high degree.

**[11:30]** or they solved it to a very high degree. So so what happens now that we that we

**[11:34]** So so what happens now that we that we

**[11:34]** So so what happens now that we that we can all speak our own languages yet at

**[11:37]** can all speak our own languages yet at

**[11:37]** can all speak our own languages yet at the same time communicate with each

**[11:38]** the same time communicate with each

**[11:38]** the same time communicate with each other. I'm already doing it. For

**[11:40]** other. I'm already doing it. For

**[11:40]** other. I'm already doing it. For instance, I do sometimes customer

**[11:41]** instance, I do sometimes customer

**[11:41]** instance, I do sometimes customer support manually for Korea and I

**[11:44]** support manually for Korea and I

**[11:44]** support manually for Korea and I literally speak Japanese with some of my

**[11:46]** literally speak Japanese with some of my

**[11:46]** literally speak Japanese with some of my users and I don't speak Japanese. I

**[11:48]** users and I don't speak Japanese. I

**[11:48]** users and I don't speak Japanese. I learn a little bit but I don't speak it

**[11:51]** learn a little bit but I don't speak it

**[11:51]** learn a little bit but I don't speak it and and and like I'm now able to provide

**[11:53]** and and and like I'm now able to provide

**[11:53]** and and and like I'm now able to provide an excellent founder whatever that means

**[11:57]** an excellent founder whatever that means

**[11:57]** an excellent founder whatever that means uh customer support level to a country


### [12:00 - 13:00]

**[12:00]** uh customer support level to a country

**[12:00]** uh customer support level to a country that otherwise I would be unable to do

**[12:02]** that otherwise I would be unable to do

**[12:02]** that otherwise I would be unable to do right

**[12:04]** right

**[12:04]** right and

**[12:11]** and so I invite us all to think about

**[12:11]** and so I invite us all to think about what that really means. Um

**[12:15]** what that really means. Um

**[12:15]** what that really means. Um because this for for instance means that

**[12:18]** because this for for instance means that

**[12:18]** because this for for instance means that we can now understand

**[12:21]** we can now understand

**[12:21]** we can now understand better or transmit our own opinion

**[12:23]** better or transmit our own opinion

**[12:23]** better or transmit our own opinion better to others and

**[12:26]** better to others and

**[12:26]** better to others and on the previous point that I was talking

**[12:28]** on the previous point that I was talking

**[12:28]** on the previous point that I was talking about with the art

**[12:30]** about with the art

**[12:30]** about with the art that's kind of like an opinion right

**[12:31]** that's kind of like an opinion right

**[12:31]** that's kind of like an opinion right like evals

**[12:33]** like evals

**[12:33]** like evals are not just about are there four cuts

**[12:36]** are not just about are there four cuts

**[12:36]** are not just about are there four cuts here it's about this cut is blue and

**[12:38]** here it's about this cut is blue and

**[12:38]** here it's about this cut is blue and it's like yeah but is it blue or is it

**[12:40]** it's like yeah but is it blue or is it

**[12:40]** it's like yeah but is it blue or is it teal what kind of blue and I don't like

**[12:42]** teal what kind of blue and I don't like

**[12:42]** teal what kind of blue and I don't like this blue and all of that. Um so

**[12:48]** this blue and all of that. Um so

**[12:48]** this blue and all of that. Um so like in a nutshell is like how how do we

**[12:50]** like in a nutshell is like how how do we

**[12:50]** like in a nutshell is like how how do we evol our evolves right like from my

**[12:53]** evol our evolves right like from my

**[12:53]** evol our evolves right like from my opinion like from my opinion this is bad

**[12:57]** opinion like from my opinion this is bad

**[12:57]** opinion like from my opinion this is bad um then I want metrics that take into

**[12:59]** um then I want metrics that take into

**[12:59]** um then I want metrics that take into account my my opinion too and then it's


### [13:00 - 14:00]

**[13:02]** account my my opinion too and then it's

**[13:02]** account my my opinion too and then it's like okay consider myself I may be a

**[13:04]** like okay consider myself I may be a

**[13:04]** like okay consider myself I may be a visual learner what that means is like

**[13:10]** maybe

**[13:10]** maybe your evil should take into account how

**[13:13]** your evil should take into account how

**[13:13]** your evil should take into account how we humans

**[13:14]** we humans

**[13:14]** we humans perceive images, right? So, and and and

**[13:17]** perceive images, right? So, and and and

**[13:18]** perceive images, right? So, and and and also the the nature of the data such as

**[13:20]** also the the nature of the data such as

**[13:20]** also the the nature of the data such as oh, it's all trained on JPEG on the

**[13:24]** oh, it's all trained on JPEG on the

**[13:24]** oh, it's all trained on JPEG on the internet. So, take into account the

**[13:25]** internet. So, take into account the

**[13:25]** internet. So, take into account the artifacts, take into account uh like all

**[13:29]** artifacts, take into account uh like all

**[13:29]** artifacts, take into account uh like all of these while while training your data.

**[13:32]** of these while while training your data.

**[13:32]** of these while while training your data. Um, okay, I guess mandatory slide before

**[13:35]** Um, okay, I guess mandatory slide before

**[13:35]** Um, okay, I guess mandatory slide before the thank you. Uh, bunch of users, bunch

**[13:38]** the thank you. Uh, bunch of users, bunch

**[13:38]** the thank you. Uh, bunch of users, bunch of money. We did all of that with eight

**[13:40]** of money. We did all of that with eight

**[13:40]** of money. We did all of that with eight people, now we're 12. Uh this is an

**[13:42]** people, now we're 12. Uh this is an

**[13:42]** people, now we're 12. Uh this is an email that I set up today for high

**[13:44]** email that I set up today for high

**[13:44]** email that I set up today for high priority applications uh for anyone who

**[13:46]** priority applications uh for anyone who

**[13:46]** priority applications uh for anyone who wants to work on research around uh

**[13:49]** wants to work on research around uh

**[13:49]** wants to work on research around uh aesthetics research uh

**[13:51]** aesthetics research uh

**[13:51]** aesthetics research uh hyperpersonalization

**[13:52]** hyperpersonalization

**[13:52]** hyperpersonalization scaling generative AI models in real

**[13:54]** scaling generative AI models in real

**[13:54]** scaling generative AI models in real time for multimedia image video audio 3D

**[13:58]** time for multimedia image video audio 3D

**[13:58]** time for multimedia image video audio 3D uh across the globe. Uh we have


### [14:00 - 15:00]

**[14:00]** uh across the globe. Uh we have

**[14:00]** uh across the globe. Uh we have customers like those and that's it.

**[14:04]** customers like those and that's it.

**[14:04]** customers like those and that's it. Thank you. Oh

**[14:36]** >> yeah. Can there's many points there. Can

**[14:36]** >> yeah. Can there's many points there. Can you like refrain the question like


### [15:00 - 16:00]

**[15:10]** >> Yeah.

**[15:10]** >> Yeah. Yeah. So, so the question like in a

**[15:13]** Yeah. So, so the question like in a

**[15:13]** Yeah. So, so the question like in a nutshell is like are there uh

**[15:16]** nutshell is like are there uh

**[15:16]** nutshell is like are there uh perceptually aware metrics right like

**[15:19]** perceptually aware metrics right like

**[15:19]** perceptually aware metrics right like like okay you I showed an example of FID

**[15:21]** like okay you I showed an example of FID

**[15:21]** like okay you I showed an example of FID score it changes a lot with JPEG

**[15:24]** score it changes a lot with JPEG

**[15:24]** score it changes a lot with JPEG artifacts are those where it's almost

**[15:25]** artifacts are those where it's almost

**[15:25]** artifacts are those where it's almost like the opposite barely changes uh and

**[15:28]** like the opposite barely changes uh and

**[15:28]** like the opposite barely changes uh and the metric is still good like there are

**[15:30]** the metric is still good like there are

**[15:30]** the metric is still good like there are some and many of these are used also in

**[15:33]** some and many of these are used also in

**[15:33]** some and many of these are used also in traditional uh encoding uh techniques um

**[15:37]** traditional uh encoding uh techniques um

**[15:38]** traditional uh encoding uh techniques um but in a way I'm here to invite us all

**[15:41]** but in a way I'm here to invite us all

**[15:41]** but in a way I'm here to invite us all to start thinking about those like

**[15:46]** to start thinking about those like

**[15:46]** to start thinking about those like like to we can actually

**[15:50]** like to we can actually

**[15:50]** like to we can actually train like we can train uh I mean it's

**[15:55]** train like we can train uh I mean it's

**[15:55]** train like we can train uh I mean it's it's called a classifier right like or

**[15:56]** it's called a classifier right like or

**[15:56]** it's called a classifier right like or or or a continuous classifier we can

**[15:58]** or or a continuous classifier we can

**[15:58]** or or a continuous classifier we can train so that it understands what we


### [16:00 - 17:00]

**[16:00]** train so that it understands what we

**[16:00]** train so that it understands what we mean and it's like hey I show you these

**[16:02]** mean and it's like hey I show you these

**[16:02]** mean and it's like hey I show you these five images these five images are

**[16:04]** five images these five images are

**[16:04]** five images these five images are actually all good and then they can have

**[16:05]** actually all good and then they can have

**[16:05]** actually all good and then they can have all sorts of artifact not just JPEG

**[16:07]** all sorts of artifact not just JPEG

**[16:07]** all sorts of artifact not just JPEG artifact and this is exactly where

**[16:10]** artifact and this is exactly where

**[16:10]** artifact and this is exactly where machine learning journey excels, right?

**[16:11]** machine learning journey excels, right?

**[16:11]** machine learning journey excels, right? When it's all about opinions and it's

**[16:13]** When it's all about opinions and it's

**[16:13]** When it's all about opinions and it's like, let me just know and you will

**[16:15]** like, let me just know and you will

**[16:15]** like, let me just know and you will know. You know, you know what? You will

**[16:17]** know. You know, you know what? You will

**[16:17]** know. You know, you know what? You will know when you see it. That's precisely

**[16:18]** know when you see it. That's precisely

**[16:18]** know when you see it. That's precisely the type of question that AI is amazing

**[16:20]** the type of question that AI is amazing

**[16:20]** the type of question that AI is amazing at.


