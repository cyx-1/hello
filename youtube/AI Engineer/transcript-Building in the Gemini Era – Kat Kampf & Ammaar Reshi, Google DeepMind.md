# Building in the Gemini Era – Kat Kampf & Ammaar Reshi, Google DeepMind

**Video URL:** https://www.youtube.com/watch?v=fgkXEIbZpGc

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** We are super excited to be here. It's

**[00:23]** We are super excited to be here. It's been obviously a very exciting week in

**[00:25]** been obviously a very exciting week in

**[00:25]** been obviously a very exciting week in AI. It's been a very exciting and busy

**[00:27]** AI. It's been a very exciting and busy

**[00:27]** AI. It's been a very exciting and busy week over here at DeepMind. I'm so super

**[00:29]** week over here at DeepMind. I'm so super

**[00:29]** week over here at DeepMind. I'm so super excited to chat with you about our

**[00:31]** excited to chat with you about our

**[00:31]** excited to chat with you about our newest models and build some demos live

**[00:33]** newest models and build some demos live

**[00:33]** newest models and build some demos live with you all. I'm Cat. I work on Vibe

**[00:36]** with you all. I'm Cat. I work on Vibe

**[00:36]** with you all. I'm Cat. I work on Vibe Cody and AI Studio. This is Amomar. He

**[00:38]** Cody and AI Studio. This is Amomar. He

**[00:38]** Cody and AI Studio. This is Amomar. He leads our product and design team for AI

**[00:40]** leads our product and design team for AI

**[00:40]** leads our product and design team for AI Studio. Uh but I want to step back for a

**[00:42]** Studio. Uh but I want to step back for a

**[00:42]** Studio. Uh but I want to step back for a second and talk about uh the journey at

**[00:44]** second and talk about uh the journey at

**[00:44]** second and talk about uh the journey at DeepMind generally. So what's I think

**[00:47]** DeepMind generally. So what's I think

**[00:47]** DeepMind generally. So what's I think particularly unique about Google's

**[00:48]** particularly unique about Google's

**[00:48]** particularly unique about Google's journey right now is that Deep Mind has

**[00:50]** journey right now is that Deep Mind has

**[00:50]** journey right now is that Deep Mind has been innovating here for not just this

**[00:52]** been innovating here for not just this

**[00:52]** been innovating here for not just this week or this past year but for years and

**[00:55]** week or this past year but for years and

**[00:55]** week or this past year but for years and years uh with things like the

**[00:56]** years uh with things like the

**[00:56]** years uh with things like the transformer, Alph Go, etc. And this is

**[00:59]** transformer, Alph Go, etc. And this is

**[00:59]** transformer, Alph Go, etc. And this is obviously a graphic from 5 days ago


### [01:00 - 02:00]

**[01:02]** obviously a graphic from 5 days ago

**[01:02]** obviously a graphic from 5 days ago because it ends with Gemini 2.5 and we

**[01:05]** because it ends with Gemini 2.5 and we

**[01:05]** because it ends with Gemini 2.5 and we are super excited to have announced

**[01:07]** are super excited to have announced

**[01:07]** are super excited to have announced earlier this week Gemini 3 Pro.

**[01:10]** earlier this week Gemini 3 Pro.

**[01:10]** earlier this week Gemini 3 Pro. Hopefully this message has reached you

**[01:11]** Hopefully this message has reached you

**[01:12]** Hopefully this message has reached you all already. If not, we have a lot of

**[01:13]** all already. If not, we have a lot of

**[01:13]** all already. If not, we have a lot of work to do. Uh but this is our latest

**[01:16]** work to do. Uh but this is our latest

**[01:16]** work to do. Uh but this is our latest most intelligent state-of-the-art model.

**[01:18]** most intelligent state-of-the-art model.

**[01:18]** most intelligent state-of-the-art model. Um and ultimately what we want folks to

**[01:21]** Um and ultimately what we want folks to

**[01:21]** Um and ultimately what we want folks to understand with Gemini 3 is that we can

**[01:23]** understand with Gemini 3 is that we can

**[01:23]** understand with Gemini 3 is that we can really build anything and that comes in

**[01:26]** really build anything and that comes in

**[01:26]** really build anything and that comes in two major capabilities. I think the

**[01:27]** two major capabilities. I think the

**[01:27]** two major capabilities. I think the first is the UI and aesthetic

**[01:29]** first is the UI and aesthetic

**[01:30]** first is the UI and aesthetic sensibilities of Gemini 3. It's very

**[01:33]** sensibilities of Gemini 3. It's very

**[01:33]** sensibilities of Gemini 3. It's very very strong at design understanding and

**[01:35]** very strong at design understanding and

**[01:35]** very strong at design understanding and generating websites and good UIs uh in

**[01:39]** generating websites and good UIs uh in

**[01:39]** generating websites and good UIs uh in one shot. And the second is with agentic

**[01:41]** one shot. And the second is with agentic

**[01:41]** one shot. And the second is with agentic tool calling. So I think this goes back

**[01:43]** tool calling. So I think this goes back

**[01:43]** tool calling. So I think this goes back to the sort of spectrum we're seeing

**[01:45]** to the sort of spectrum we're seeing

**[01:45]** to the sort of spectrum we're seeing with models. Sometimes you want a

**[01:46]** with models. Sometimes you want a

**[01:46]** with models. Sometimes you want a oneshot website and sometimes you want

**[01:48]** oneshot website and sometimes you want

**[01:48]** oneshot website and sometimes you want to do really complex tasks within you

**[01:51]** to do really complex tasks within you

**[01:51]** to do really complex tasks within you know massive code bases and that's where

**[01:53]** know massive code bases and that's where

**[01:53]** know massive code bases and that's where tool calling and agentic use can be uh

**[01:56]** tool calling and agentic use can be uh

**[01:56]** tool calling and agentic use can be uh be particularly powerful. So with Gemini

**[01:59]** be particularly powerful. So with Gemini

**[01:59]** be particularly powerful. So with Gemini 3, we see on the right is a SWE


### [02:00 - 03:00]

**[02:02]** 3, we see on the right is a SWE

**[02:02]** 3, we see on the right is a SWE um experiment where it was a base agent

**[02:05]** um experiment where it was a base agent

**[02:05]** um experiment where it was a base agent harness across a few different models

**[02:07]** harness across a few different models

**[02:07]** harness across a few different models and we can see Gemini 3 is vastly above

**[02:10]** and we can see Gemini 3 is vastly above

**[02:10]** and we can see Gemini 3 is vastly above uh in performance in Agentic scenarios

**[02:12]** uh in performance in Agentic scenarios

**[02:12]** uh in performance in Agentic scenarios and then as well leaps above our

**[02:15]** and then as well leaps above our

**[02:15]** and then as well leaps above our previous models and state-of-the-art

**[02:16]** previous models and state-of-the-art

**[02:16]** previous models and state-of-the-art across the board. Uh so super excited to

**[02:19]** across the board. Uh so super excited to

**[02:19]** across the board. Uh so super excited to see what you folks build with this

**[02:20]** see what you folks build with this

**[02:20]** see what you folks build with this model. Um, and in in the meantime, we,

**[02:24]** model. Um, and in in the meantime, we,

**[02:24]** model. Um, and in in the meantime, we, you know, launched this on Tuesday, but

**[02:26]** you know, launched this on Tuesday, but

**[02:26]** you know, launched this on Tuesday, but there was still three days left in the

**[02:27]** there was still three days left in the

**[02:27]** there was still three days left in the week, so we had to launch something else

**[02:29]** week, so we had to launch something else

**[02:29]** week, so we had to launch something else as well. So, I hand it off to Amara to

**[02:31]** as well. So, I hand it off to Amara to

**[02:31]** as well. So, I hand it off to Amara to talk about our pro image model.

**[02:33]** talk about our pro image model.

**[02:33]** talk about our pro image model. >> Yeah. So, at Deep Mind, I think you have

**[02:35]** >> Yeah. So, at Deep Mind, I think you have

**[02:35]** >> Yeah. So, at Deep Mind, I think you have a few days left in the week. You choose

**[02:36]** a few days left in the week. You choose

**[02:36]** a few days left in the week. You choose to launch another breakthrough model.

**[02:38]** to launch another breakthrough model.

**[02:38]** to launch another breakthrough model. And so, uh, we're really excited about

**[02:39]** And so, uh, we're really excited about

**[02:40]** And so, uh, we're really excited about Nano Banana Pro, which came out

**[02:41]** Nano Banana Pro, which came out

**[02:41]** Nano Banana Pro, which came out yesterday. Uh, and it's a huge leap on

**[02:43]** yesterday. Uh, and it's a huge leap on

**[02:44]** yesterday. Uh, and it's a huge leap on our our already state-of-the-art image

**[02:46]** our our already state-of-the-art image

**[02:46]** our our already state-of-the-art image model. So with Enter Pro, uh, one of the

**[02:49]** model. So with Enter Pro, uh, one of the

**[02:49]** model. So with Enter Pro, uh, one of the things that I love about it the most is

**[02:50]** things that I love about it the most is

**[02:50]** things that I love about it the most is its world knowledge. So it's powered by

**[02:52]** its world knowledge. So it's powered by

**[02:52]** its world knowledge. So it's powered by Google search. Uh, and so you can ask it

**[02:55]** Google search. Uh, and so you can ask it

**[02:55]** Google search. Uh, and so you can ask it all sorts of things like how do I make

**[02:57]** all sorts of things like how do I make

**[02:57]** all sorts of things like how do I make this tea? And it'll actually go search

**[02:58]** this tea? And it'll actually go search

**[02:58]** this tea? And it'll actually go search Google search, create an a detailed


### [03:00 - 04:00]

**[03:00]** Google search, create an a detailed

**[03:00]** Google search, create an a detailed infographic for you and diagram for you.

**[03:03]** infographic for you and diagram for you.

**[03:03]** infographic for you and diagram for you. Uh, and there all sorts of things now

**[03:04]** Uh, and there all sorts of things now

**[03:04]** Uh, and there all sorts of things now with accurate information that it can

**[03:06]** with accurate information that it can

**[03:06]** with accurate information that it can do. And the other thing you're noticing

**[03:07]** do. And the other thing you're noticing

**[03:07]** do. And the other thing you're noticing here is improved text rendering. So text

**[03:10]** here is improved text rendering. So text

**[03:10]** here is improved text rendering. So text is one of those small details that if

**[03:12]** is one of those small details that if

**[03:12]** is one of those small details that if you get it wrong, you can pretty much

**[03:13]** you get it wrong, you can pretty much

**[03:13]** you get it wrong, you can pretty much pick it up quickly. But an Anim Pro 2

**[03:16]** pick it up quickly. But an Anim Pro 2

**[03:16]** pick it up quickly. But an Anim Pro 2 does an amazing job at text rendering.

**[03:18]** does an amazing job at text rendering.

**[03:18]** does an amazing job at text rendering. Uh, and you can see that in a bunch of

**[03:19]** Uh, and you can see that in a bunch of

**[03:19]** Uh, and you can see that in a bunch of examples like here where it wraps around

**[03:21]** examples like here where it wraps around

**[03:21]** examples like here where it wraps around the can perfectly and it also has a

**[03:24]** the can perfectly and it also has a

**[03:24]** the can perfectly and it also has a bunch of localization as well. So, tons

**[03:25]** bunch of localization as well. So, tons

**[03:25]** bunch of localization as well. So, tons of languages, Korean on the right, so it

**[03:28]** of languages, Korean on the right, so it

**[03:28]** of languages, Korean on the right, so it can translate images as well and render

**[03:30]** can translate images as well and render

**[03:30]** can translate images as well and render them perfectly on the exact same

**[03:31]** them perfectly on the exact same

**[03:31]** them perfectly on the exact same reference image. Uh, on top of that,

**[03:33]** reference image. Uh, on top of that,

**[03:34]** reference image. Uh, on top of that, consistency is improved. So, uh, you can

**[03:36]** consistency is improved. So, uh, you can

**[03:36]** consistency is improved. So, uh, you can now put up to 14 people in an image and

**[03:39]** now put up to 14 people in an image and

**[03:39]** now put up to 14 people in an image and then can create this group shot you can

**[03:41]** then can create this group shot you can

**[03:41]** then can create this group shot you can see on the right. uh and that uh it can

**[03:43]** see on the right. uh and that uh it can

**[03:43]** see on the right. uh and that uh it can do more but 14 is basically our our kind

**[03:46]** do more but 14 is basically our our kind

**[03:46]** do more but 14 is basically our our kind of benchmark so far. Um and that also

**[03:48]** of benchmark so far. Um and that also

**[03:48]** of benchmark so far. Um and that also enables a whole set of new use cases. Uh

**[03:51]** enables a whole set of new use cases. Uh

**[03:51]** enables a whole set of new use cases. Uh and then creative controls as well. So

**[03:53]** and then creative controls as well. So

**[03:53]** and then creative controls as well. So you can see here on the left the focus

**[03:55]** you can see here on the left the focus

**[03:55]** you can see here on the left the focus is on the woman and on the right on the

**[03:57]** is on the woman and on the right on the

**[03:57]** is on the woman and on the right on the flowers and this was just a simple

**[03:59]** flowers and this was just a simple

**[03:59]** flowers and this was just a simple prompt. All you had to say was change


### [04:00 - 05:00]

**[04:01]** prompt. All you had to say was change

**[04:01]** prompt. All you had to say was change the focus to the flowers. Maintains

**[04:03]** the focus to the flowers. Maintains

**[04:03]** the focus to the flowers. Maintains everything in the previous image just

**[04:04]** everything in the previous image just

**[04:04]** everything in the previous image just changes the focus. So incredible outputs

**[04:07]** changes the focus. So incredible outputs

**[04:07]** changes the focus. So incredible outputs as well uh with Nano Banana Pro and a

**[04:09]** as well uh with Nano Banana Pro and a

**[04:09]** as well uh with Nano Banana Pro and a range of aspect ratios. So, if you want

**[04:11]** range of aspect ratios. So, if you want

**[04:11]** range of aspect ratios. So, if you want to generate uh wallpapers or big banners

**[04:13]** to generate uh wallpapers or big banners

**[04:13]** to generate uh wallpapers or big banners or advertising boards, you can do all of

**[04:15]** or advertising boards, you can do all of

**[04:15]** or advertising boards, you can do all of that as well. Um, so anyway, instead of

**[04:18]** that as well. Um, so anyway, instead of

**[04:18]** that as well. Um, so anyway, instead of talking, we decided we're just going to

**[04:19]** talking, we decided we're just going to

**[04:20]** talking, we decided we're just going to show you a bunch of demos live of what

**[04:21]** show you a bunch of demos live of what

**[04:22]** show you a bunch of demos live of what we've been building with these products

**[04:23]** we've been building with these products

**[04:23]** we've been building with these products uh over the last week. Um, and yeah,

**[04:25]** uh over the last week. Um, and yeah,

**[04:25]** uh over the last week. Um, and yeah, excited to jump into it. So, let's do

**[04:27]** excited to jump into it. So, let's do

**[04:28]** excited to jump into it. So, let's do that. Uh, all right. So, cat,

**[04:31]** that. Uh, all right. So, cat,

**[04:31]** that. Uh, all right. So, cat, >> yes,

**[04:32]** >> yes,

**[04:32]** >> yes, >> take it away.

**[04:33]** >> take it away.

**[04:33]** >> take it away. >> Here we go. Cat tabs. Um, cool. So, for

**[04:35]** >> Here we go. Cat tabs. Um, cool. So, for

**[04:35]** >> Here we go. Cat tabs. Um, cool. So, for folks who aren't familiar, this is

**[04:36]** folks who aren't familiar, this is

**[04:36]** folks who aren't familiar, this is Google AI Studio. It's our home for

**[04:38]** Google AI Studio. It's our home for

**[04:38]** Google AI Studio. It's our home for getting started with the latest Gemini

**[04:40]** getting started with the latest Gemini

**[04:40]** getting started with the latest Gemini models. You can get your API key, chat

**[04:43]** models. You can get your API key, chat

**[04:43]** models. You can get your API key, chat with the latest models, including Gemini

**[04:45]** with the latest models, including Gemini

**[04:45]** with the latest models, including Gemini 3 and a Banana Pro. Uh, but today we're

**[04:47]** 3 and a Banana Pro. Uh, but today we're

**[04:47]** 3 and a Banana Pro. Uh, but today we're going to be focusing on this build

**[04:49]** going to be focusing on this build

**[04:49]** going to be focusing on this build experience. So, this is our vibe coding

**[04:51]** experience. So, this is our vibe coding

**[04:51]** experience. So, this is our vibe coding experience in a studio. You can see here

**[04:53]** experience in a studio. You can see here

**[04:53]** experience in a studio. You can see here we have a gallery of a bunch of example

**[04:55]** we have a gallery of a bunch of example

**[04:55]** we have a gallery of a bunch of example apps, a bunch of very cool uh to the

**[04:58]** apps, a bunch of very cool uh to the

**[04:58]** apps, a bunch of very cool uh to the aesthetics point of Gemini 3, a bunch of


### [05:00 - 06:00]

**[05:00]** aesthetics point of Gemini 3, a bunch of

**[05:00]** aesthetics point of Gemini 3, a bunch of very cool Gemini 3 examples. Um, but you

**[05:03]** very cool Gemini 3 examples. Um, but you

**[05:03]** very cool Gemini 3 examples. Um, but you can also go prompt to apply here. And

**[05:06]** can also go prompt to apply here. And

**[05:06]** can also go prompt to apply here. And this is free to use. And I think one of

**[05:07]** this is free to use. And I think one of

**[05:08]** this is free to use. And I think one of the unique things about AI Studio is how

**[05:10]** the unique things about AI Studio is how

**[05:10]** the unique things about AI Studio is how easy it is to integrate the Gemini API

**[05:12]** easy it is to integrate the Gemini API

**[05:12]** easy it is to integrate the Gemini API into your application. So we can see

**[05:15]** into your application. So we can see

**[05:15]** into your application. So we can see here at the bottom there's a bunch of

**[05:16]** here at the bottom there's a bunch of

**[05:16]** here at the bottom there's a bunch of these what we call AI chips um that

**[05:18]** these what we call AI chips um that

**[05:18]** these what we call AI chips um that showcase a ton of the unique features

**[05:20]** showcase a ton of the unique features

**[05:20]** showcase a ton of the unique features beyond just the model you're choosing

**[05:22]** beyond just the model you're choosing

**[05:22]** beyond just the model you're choosing with the Gemini API. Different tools you

**[05:24]** with the Gemini API. Different tools you

**[05:24]** with the Gemini API. Different tools you can use like Google search grounding,

**[05:26]** can use like Google search grounding,

**[05:26]** can use like Google search grounding, Google Maps grounding. We also let you

**[05:28]** Google Maps grounding. We also let you

**[05:28]** Google Maps grounding. We also let you build with our live API. So, you can do

**[05:31]** build with our live API. So, you can do

**[05:31]** build with our live API. So, you can do oneshot examples of I have one that lets

**[05:33]** oneshot examples of I have one that lets

**[05:33]** oneshot examples of I have one that lets me input a webcam of my tennis swing and

**[05:36]** me input a webcam of my tennis swing and

**[05:36]** me input a webcam of my tennis swing and it'll give live corrections on my swing.

**[05:38]** it'll give live corrections on my swing.

**[05:38]** it'll give live corrections on my swing. Um,

**[05:39]** Um,

**[05:39]** Um, >> you also made one to improve my posture.

**[05:41]** >> you also made one to improve my posture.

**[05:41]** >> you also made one to improve my posture. >> Yeah. [laughter]

**[05:42]** >> Yeah. [laughter]

**[05:42]** >> Yeah. [laughter] >> Yeah. If you lean forward too much, live

**[05:44]** >> Yeah. If you lean forward too much, live

**[05:44]** >> Yeah. If you lean forward too much, live API will yell at you. Um, so it's a very

**[05:47]** API will yell at you. Um, so it's a very

**[05:47]** API will yell at you. Um, so it's a very flexible way to get started building AI

**[05:49]** flexible way to get started building AI

**[05:49]** flexible way to get started building AI powered apps. Um, and the other cool

**[05:51]** powered apps. Um, and the other cool

**[05:51]** powered apps. Um, and the other cool thing is you don't actually need an API

**[05:53]** thing is you don't actually need an API

**[05:53]** thing is you don't actually need an API key here for most of the models. So you

**[05:55]** key here for most of the models. So you

**[05:55]** key here for most of the models. So you can build your application, you can

**[05:57]** can build your application, you can

**[05:57]** can build your application, you can share it with the world and anyone who

**[05:59]** share it with the world and anyone who

**[05:59]** share it with the world and anyone who comes and visits your shared application


### [06:00 - 07:00]

**[06:01]** comes and visits your shared application

**[06:01]** comes and visits your shared application will be using their AI studio free

**[06:03]** will be using their AI studio free

**[06:03]** will be using their AI studio free quota. So you don't have to worry about,

**[06:05]** quota. So you don't have to worry about,

**[06:05]** quota. So you don't have to worry about, you know, hopefully you have an app that

**[06:07]** you know, hopefully you have an app that

**[06:07]** you know, hopefully you have an app that goes supervisible. You won't have to

**[06:08]** goes supervisible. You won't have to

**[06:08]** goes supervisible. You won't have to worry about a crazy surprise API bill or

**[06:10]** worry about a crazy surprise API bill or

**[06:10]** worry about a crazy surprise API bill or anything like that. Um, so I'm going to

**[06:13]** anything like that. Um, so I'm going to

**[06:13]** anything like that. Um, so I'm going to actually shoot off a prompt here that is

**[06:15]** actually shoot off a prompt here that is

**[06:15]** actually shoot off a prompt here that is using our latest ano banana model. And

**[06:18]** using our latest ano banana model. And

**[06:18]** using our latest ano banana model. And that basically allows us to use Google

**[06:20]** that basically allows us to use Google

**[06:20]** that basically allows us to use Google search grounding to create a

**[06:23]** search grounding to create a

**[06:23]** search grounding to create a illustration of laptop stickers. And

**[06:25]** illustration of laptop stickers. And

**[06:25]** illustration of laptop stickers. And this is one of the viral trends we've

**[06:27]** this is one of the viral trends we've

**[06:27]** this is one of the viral trends we've been seeing with Nano Banana Pro. Um, so

**[06:29]** been seeing with Nano Banana Pro. Um, so

**[06:29]** been seeing with Nano Banana Pro. Um, so I'll kick this off and what this will

**[06:31]** I'll kick this off and what this will

**[06:31]** I'll kick this off and what this will do, I have the AI chip that tells it to

**[06:33]** do, I have the AI chip that tells it to

**[06:33]** do, I have the AI chip that tells it to use the Pro model. And this will sum up

**[06:36]** use the Pro model. And this will sum up

**[06:36]** use the Pro model. And this will sum up my prompt and go talk to Gemini 3 to

**[06:39]** my prompt and go talk to Gemini 3 to

**[06:39]** my prompt and go talk to Gemini 3 to break down the task and start generating

**[06:41]** break down the task and start generating

**[06:41]** break down the task and start generating my endto-end application. Uh but while

**[06:44]** my endto-end application. Uh but while

**[06:44]** my endto-end application. Uh but while that builds, I'm going to hand it off to

**[06:45]** that builds, I'm going to hand it off to

**[06:45]** that builds, I'm going to hand it off to Amara to show some demos in the

**[06:46]** Amara to show some demos in the

**[06:46]** Amara to show some demos in the meantime.

**[06:47]** meantime.

**[06:47]** meantime. >> Cool. I think the other thing to point

**[06:49]** >> Cool. I think the other thing to point

**[06:49]** >> Cool. I think the other thing to point out here is that uh we're trying to

**[06:51]** out here is that uh we're trying to

**[06:51]** out here is that uh we're trying to think through how the vibe coding

**[06:52]** think through how the vibe coding

**[06:52]** think through how the vibe coding experience is also powered by AI every

**[06:54]** experience is also powered by AI every

**[06:54]** experience is also powered by AI every step of the way. So you're seeing here

**[06:56]** step of the way. So you're seeing here

**[06:56]** step of the way. So you're seeing here even in the loading screen, uh it is

**[06:58]** even in the loading screen, uh it is

**[06:58]** even in the loading screen, uh it is using Gemini and thinking through this


### [07:00 - 08:00]

**[07:00]** using Gemini and thinking through this

**[07:00]** using Gemini and thinking through this app that you're making and how you could

**[07:02]** app that you're making and how you could

**[07:02]** app that you're making and how you could extend it. Um, and so we're thinking

**[07:04]** extend it. Um, and so we're thinking

**[07:04]** extend it. Um, and so we're thinking through breaking those typical vibe

**[07:07]** through breaking those typical vibe

**[07:07]** through breaking those typical vibe coding paradigms as well and helping you

**[07:08]** coding paradigms as well and helping you

**[07:08]** coding paradigms as well and helping you iterate with the model as your partner.

**[07:10]** iterate with the model as your partner.

**[07:10]** iterate with the model as your partner. But anyway, let me jump right into the

**[07:13]** But anyway, let me jump right into the

**[07:13]** But anyway, let me jump right into the text rendering demo. So, uh, when I

**[07:16]** text rendering demo. So, uh, when I

**[07:16]** text rendering demo. So, uh, when I heard of text rendering for the first

**[07:17]** heard of text rendering for the first

**[07:17]** heard of text rendering for the first time and the consistency that we were

**[07:18]** time and the consistency that we were

**[07:18]** time and the consistency that we were getting with Nan Pro, my mind went to

**[07:20]** getting with Nan Pro, my mind went to

**[07:20]** getting with Nan Pro, my mind went to comic books. Uh, and so I was thinking,

**[07:22]** comic books. Uh, and so I was thinking,

**[07:22]** comic books. Uh, and so I was thinking, why can't I now be in my own comic book

**[07:24]** why can't I now be in my own comic book

**[07:24]** why can't I now be in my own comic book adventure um, and also place cat in

**[07:27]** adventure um, and also place cat in

**[07:27]** adventure um, and also place cat in there and then maybe we can tell a

**[07:28]** there and then maybe we can tell a

**[07:28]** there and then maybe we can tell a story. And so uh in this app uh also

**[07:31]** story. And so uh in this app uh also

**[07:31]** story. And so uh in this app uh also vibe coded you can just upload a face of

**[07:33]** vibe coded you can just upload a face of

**[07:34]** vibe coded you can just upload a face of somebody. So I've got some nurse face of

**[07:35]** somebody. So I've got some nurse face of

**[07:35]** somebody. So I've got some nurse face of course [laughter]

**[07:37]** course [laughter]

**[07:37]** course [laughter] but I'll use I'll use cat here uh and

**[07:40]** but I'll use I'll use cat here uh and

**[07:40]** but I'll use I'll use cat here uh and myself um and then uh we can choose the

**[07:43]** myself um and then uh we can choose the

**[07:44]** myself um and then uh we can choose the genre of the story um and and all the

**[07:46]** genre of the story um and and all the

**[07:46]** genre of the story um and and all the languages that we have so far. Uh, I'm

**[07:48]** languages that we have so far. Uh, I'm

**[07:48]** languages that we have so far. Uh, I'm going to do a story about us presenting

**[07:51]** going to do a story about us presenting

**[07:51]** going to do a story about us presenting at AI Engineer um in New York uh

**[07:54]** at AI Engineer um in New York uh

**[07:54]** at AI Engineer um in New York uh presenting AI Studio and we are uh vibe

**[07:57]** presenting AI Studio and we are uh vibe

**[07:57]** presenting AI Studio and we are uh vibe coding and winging our presentation.

**[07:59]** coding and winging our presentation.

**[07:59]** coding and winging our presentation. That's where we're going to be doing


### [08:00 - 09:00]

**[08:00]** That's where we're going to be doing

**[08:00]** That's where we're going to be doing this comic book story. So, we'll fire

**[08:02]** this comic book story. So, we'll fire

**[08:02]** this comic book story. So, we'll fire that off. Uh but while we wait for that,

**[08:05]** that off. Uh but while we wait for that,

**[08:05]** that off. Uh but while we wait for that, um the other cool thing about this is uh

**[08:08]** um the other cool thing about this is uh

**[08:08]** um the other cool thing about this is uh we'll wait for that to generate. But I

**[08:09]** we'll wait for that to generate. But I

**[08:09]** we'll wait for that to generate. But I want to show you the design

**[08:11]** want to show you the design

**[08:11]** want to show you the design sensibilities as well. So, you know that

**[08:14]** sensibilities as well. So, you know that

**[08:14]** sensibilities as well. So, you know that if you've been working with AI models

**[08:15]** if you've been working with AI models

**[08:15]** if you've been working with AI models and generating websites, they've been

**[08:17]** and generating websites, they've been

**[08:17]** and generating websites, they've been creating purple gradients and things

**[08:18]** creating purple gradients and things

**[08:18]** creating purple gradients and things [laughter] that just, you know, they

**[08:19]** [laughter] that just, you know, they

**[08:19]** [laughter] that just, you know, they kill me as a designer. So, um, and so

**[08:22]** kill me as a designer. So, um, and so

**[08:22]** kill me as a designer. So, um, and so it's been really nice to see how this

**[08:24]** it's been really nice to see how this

**[08:24]** it's been really nice to see how this model is able to build some beautiful

**[08:26]** model is able to build some beautiful

**[08:26]** model is able to build some beautiful websites. So, this is using shader

**[08:28]** websites. So, this is using shader

**[08:28]** websites. So, this is using shader animations, uh, flowing through all

**[08:30]** animations, uh, flowing through all

**[08:30]** animations, uh, flowing through all these different pages, uh, and adds all

**[08:32]** these different pages, uh, and adds all

**[08:32]** these different pages, uh, and adds all sorts of cool transitions and effects.

**[08:34]** sorts of cool transitions and effects.

**[08:34]** sorts of cool transitions and effects. Picked out the typography by itself. And

**[08:36]** Picked out the typography by itself. And

**[08:36]** Picked out the typography by itself. And this was the initial prompt. Just create

**[08:38]** this was the initial prompt. Just create

**[08:38]** this was the initial prompt. Just create a slick animation website. kind of

**[08:40]** a slick animation website. kind of

**[08:40]** a slick animation website. kind of actually did say no cyber puncture that

**[08:42]** actually did say no cyber puncture that

**[08:42]** actually did say no cyber puncture that [laughter]

**[08:47]** >> but

**[08:47]** >> but just got to make sure [laughter]

**[08:49]** just got to make sure [laughter]

**[08:49]** just got to make sure [laughter] >> but but yeah you get some incredible

**[08:51]** >> but but yeah you get some incredible

**[08:51]** >> but but yeah you get some incredible results um and and now what I love about

**[08:54]** results um and and now what I love about

**[08:54]** results um and and now what I love about this is so many folks who you know were

**[08:56]** this is so many folks who you know were

**[08:56]** this is so many folks who you know were struggling with design who might have

**[08:57]** struggling with design who might have

**[08:57]** struggling with design who might have you know still tried to gro their way

**[08:59]** you know still tried to gro their way

**[08:59]** you know still tried to gro their way around Figma don't have to do that


### [09:00 - 10:00]

**[09:01]** around Figma don't have to do that

**[09:01]** around Figma don't have to do that anymore they can actually just go in

**[09:03]** anymore they can actually just go in

**[09:03]** anymore they can actually just go in prompt their way to something pretty

**[09:04]** prompt their way to something pretty

**[09:04]** prompt their way to something pretty nice okay back to the comic book okay

**[09:07]** nice okay back to the comic book okay

**[09:07]** nice okay back to the comic book okay pretty flattering uh comic [laughter]

**[09:09]** pretty flattering uh comic [laughter]

**[09:09]** pretty flattering uh comic [laughter] book here. Um, that, you know, I'll take

**[09:12]** book here. Um, that, you know, I'll take

**[09:12]** book here. Um, that, you know, I'll take it. Uh, and [laughter] you can see here

**[09:14]** it. Uh, and [laughter] you can see here

**[09:14]** it. Uh, and [laughter] you can see here that it's rendering the comic book. It's

**[09:16]** that it's rendering the comic book. It's

**[09:16]** that it's rendering the comic book. It's got, uh, rich text rendering showing us

**[09:19]** got, uh, rich text rendering showing us

**[09:19]** got, uh, rich text rendering showing us the story. And the other thing here is

**[09:21]** the story. And the other thing here is

**[09:21]** the story. And the other thing here is that, uh, because it's powered by Gemini

**[09:23]** that, uh, because it's powered by Gemini

**[09:23]** that, uh, because it's powered by Gemini 3, it's actually really creative at the

**[09:26]** 3, it's actually really creative at the

**[09:26]** 3, it's actually really creative at the story it's generating. And honestly,

**[09:27]** story it's generating. And honestly,

**[09:27]** story it's generating. And honestly, some of these stories have genuinely

**[09:29]** some of these stories have genuinely

**[09:29]** some of these stories have genuinely made me laugh, which is the first time

**[09:31]** made me laugh, which is the first time

**[09:31]** made me laugh, which is the first time uh, that's happened with one of these

**[09:32]** uh, that's happened with one of these

**[09:32]** uh, that's happened with one of these models. Uh, and so you can see we're

**[09:35]** models. Uh, and so you can see we're

**[09:35]** models. Uh, and so you can see we're rushing to the conference. even

**[09:36]** rushing to the conference. even

**[09:36]** rushing to the conference. even background details like the AI engineer

**[09:38]** background details like the AI engineer

**[09:38]** background details like the AI engineer banner over here uh being rendered and

**[09:41]** banner over here uh being rendered and

**[09:41]** banner over here uh being rendered and of course since it's a vibe coded app we

**[09:43]** of course since it's a vibe coded app we

**[09:43]** of course since it's a vibe coded app we can take the story in any direction. So

**[09:44]** can take the story in any direction. So

**[09:44]** can take the story in any direction. So one feature I did introduce is that you

**[09:47]** one feature I did introduce is that you

**[09:47]** one feature I did introduce is that you can choose the direction of the story

**[09:49]** can choose the direction of the story

**[09:49]** can choose the direction of the story midway. So you know do we find a quiet

**[09:51]** midway. So you know do we find a quiet

**[09:52]** midway. So you know do we find a quiet corner and try to check if our API keys

**[09:54]** corner and try to check if our API keys

**[09:54]** corner and try to check if our API keys work or do we just embrace it and go

**[09:56]** work or do we just embrace it and go

**[09:56]** work or do we just embrace it and go full improv? I think we're going to go

**[09:58]** full improv? I think we're going to go

**[09:58]** full improv? I think we're going to go full improv. Uh and so that's changed


### [10:00 - 11:00]

**[10:00]** full improv. Uh and so that's changed

**[10:00]** full improv. Uh and so that's changed that story. Uh, and so talking about the

**[10:03]** that story. Uh, and so talking about the

**[10:03]** that story. Uh, and so talking about the humor here, you can see Amaraj, a woman

**[10:05]** humor here, you can see Amaraj, a woman

**[10:05]** humor here, you can see Amaraj, a woman carrying a suspicially functional robot

**[10:07]** carrying a suspicially functional robot

**[10:07]** carrying a suspicially functional robot dog. [laughter] So I don't know if that

**[10:08]** dog. [laughter] So I don't know if that

**[10:08]** dog. [laughter] So I don't know if that was announced at the conference today,

**[10:10]** was announced at the conference today,

**[10:10]** was announced at the conference today, but uh, pretty cool. Um, and then now

**[10:13]** but uh, pretty cool. Um, and then now

**[10:13]** but uh, pretty cool. Um, and then now it's generating the rest of the story

**[10:15]** it's generating the rest of the story

**[10:15]** it's generating the rest of the story here on the right while we wait. So

**[10:17]** here on the right while we wait. So

**[10:17]** here on the right while we wait. So pretty cool to see how you can make

**[10:19]** pretty cool to see how you can make

**[10:19]** pretty cool to see how you can make these really dynamic, rich experiences

**[10:21]** these really dynamic, rich experiences

**[10:21]** these really dynamic, rich experiences with both the creativity of the model

**[10:23]** with both the creativity of the model

**[10:23]** with both the creativity of the model and Nano Pro's image capabilities.

**[10:26]** and Nano Pro's image capabilities.

**[10:26]** and Nano Pro's image capabilities. >> Love it.

**[10:27]** >> Love it.

**[10:27]** >> Love it. >> Yeah. Back to you, K.

**[10:28]** >> Yeah. Back to you, K.

**[10:28]** >> Yeah. Back to you, K. >> Yeah. Yeah. I will show. Let's hope my

**[10:30]** >> Yeah. Yeah. I will show. Let's hope my

**[10:30]** >> Yeah. Yeah. I will show. Let's hope my sticker demo is finished up. Uh, cool.

**[10:33]** sticker demo is finished up. Uh, cool.

**[10:33]** sticker demo is finished up. Uh, cool. So, I'm going to add an API key. So,

**[10:35]** So, I'm going to add an API key. So,

**[10:35]** So, I'm going to add an API key. So, Nana Banana is a new model and it's uh

**[10:38]** Nana Banana is a new model and it's uh

**[10:38]** Nana Banana is a new model and it's uh fresh off our launch of Gemini 3. So,

**[10:42]** fresh off our launch of Gemini 3. So,

**[10:42]** fresh off our launch of Gemini 3. So, for now it is a page experience in a AI

**[10:45]** for now it is a page experience in a AI

**[10:45]** for now it is a page experience in a AI studio. Um, but what I can do is I can

**[10:48]** studio. Um, but what I can do is I can

**[10:48]** studio. Um, but what I can do is I can see that here I can enter different

**[10:50]** see that here I can enter different

**[10:50]** see that here I can enter different words that I want my stickers based off

**[10:52]** words that I want my stickers based off

**[10:52]** words that I want my stickers based off or I can go use Google search. So, let's

**[10:55]** or I can go use Google search. So, let's

**[10:55]** or I can go use Google search. So, let's try the Google search. I'm going to type

**[10:57]** try the Google search. I'm going to type

**[10:58]** try the Google search. I'm going to type in a Mars name. And one of the other


### [11:00 - 12:00]

**[11:00]** in a Mars name. And one of the other

**[11:00]** in a Mars name. And one of the other cool things about this new model is that

**[11:02]** cool things about this new model is that

**[11:02]** cool things about this new model is that you can select the resolution as well.

**[11:04]** you can select the resolution as well.

**[11:04]** you can select the resolution as well. So, in this case, I'll just do 1K. Uh,

**[11:07]** So, in this case, I'll just do 1K. Uh,

**[11:07]** So, in this case, I'll just do 1K. Uh, but what this will hopefully do, but

**[11:08]** but what this will hopefully do, but

**[11:08]** but what this will hopefully do, but again, you saw it on one shot live. Uh,

**[11:10]** again, you saw it on one shot live. Uh,

**[11:10]** again, you saw it on one shot live. Uh, is go talk to Google search, grab the

**[11:13]** is go talk to Google search, grab the

**[11:13]** is go talk to Google search, grab the latest sources on Amar, build the

**[11:16]** latest sources on Amar, build the

**[11:16]** latest sources on Amar, build the context about what he likes, what his

**[11:17]** context about what he likes, what his

**[11:18]** context about what he likes, what his laptop stickers might look like. I think

**[11:20]** laptop stickers might look like. I think

**[11:20]** laptop stickers might look like. I think it's just deep mind, but if he were more

**[11:22]** it's just deep mind, but if he were more

**[11:22]** it's just deep mind, but if he were more uh [laughter] if he wanted to express

**[11:24]** uh [laughter] if he wanted to express

**[11:24]** uh [laughter] if he wanted to express himself more.

**[11:24]** himself more.

**[11:24]** himself more. >> Oh, boy. Uh, and so he can see here.

**[11:27]** >> Oh, boy. Uh, and so he can see here.

**[11:27]** >> Oh, boy. Uh, and so he can see here. [laughter]

**[11:28]** [laughter]

**[11:28]** [laughter] >> Yeah, there he is. Weekend builder.

**[11:32]** >> Yeah, there he is. Weekend builder.

**[11:32]** >> Yeah, there he is. Weekend builder. >> That's true.

**[11:32]** >> That's true.

**[11:32]** >> That's true. >> Uh, yeah. And for those who don't know,

**[11:34]** >> Uh, yeah. And for those who don't know,

**[11:34]** >> Uh, yeah. And for those who don't know, Amar has a children's book, Alice and

**[11:35]** Amar has a children's book, Alice and

**[11:35]** Amar has a children's book, Alice and Sparkle, which, yeah, is clearly he's

**[11:37]** Sparkle, which, yeah, is clearly he's

**[11:37]** Sparkle, which, yeah, is clearly he's talked about a lot because it's highly

**[11:39]** talked about a lot because it's highly

**[11:39]** talked about a lot because it's highly represented here. [laughter]

**[11:41]** represented here. [laughter]

**[11:41]** represented here. [laughter] >> But, um, very cool to see how it can

**[11:43]** >> But, um, very cool to see how it can

**[11:43]** >> But, um, very cool to see how it can bring in that contextual knowledge. Um,

**[11:46]** bring in that contextual knowledge. Um,

**[11:46]** bring in that contextual knowledge. Um, we've also seen this with like news

**[11:47]** we've also seen this with like news

**[11:47]** we've also seen this with like news events, getting relevant information on

**[11:49]** events, getting relevant information on

**[11:49]** events, getting relevant information on that day rather than having to rely on

**[11:52]** that day rather than having to rely on

**[11:52]** that day rather than having to rely on the knowledge cut off of the model. Um,

**[11:55]** the knowledge cut off of the model. Um,

**[11:55]** the knowledge cut off of the model. Um, so one other thing I'll show you folks

**[11:57]** so one other thing I'll show you folks

**[11:57]** so one other thing I'll show you folks is how we use AI studio to build AI


### [12:00 - 13:00]

**[12:00]** is how we use AI studio to build AI

**[12:00]** is how we use AI studio to build AI studio. Uh, so Amar and I have a lot of

**[12:03]** studio. Uh, so Amar and I have a lot of

**[12:03]** studio. Uh, so Amar and I have a lot of ideas, only so many engineers to work on

**[12:05]** ideas, only so many engineers to work on

**[12:05]** ideas, only so many engineers to work on these ideas. So we love to use AI studio

**[12:07]** these ideas. So we love to use AI studio

**[12:07]** these ideas. So we love to use AI studio to ideulate and explore different

**[12:09]** to ideulate and explore different

**[12:09]** to ideulate and explore different concepts. So, one of the concepts we've

**[12:11]** concepts. So, one of the concepts we've

**[12:11]** concepts. So, one of the concepts we've been working on is I'm sure you folks

**[12:13]** been working on is I'm sure you folks

**[12:13]** been working on is I'm sure you folks have seen we announced a new Agentic IDE

**[12:15]** have seen we announced a new Agentic IDE

**[12:15]** have seen we announced a new Agentic IDE at Google earlier this week called

**[12:17]** at Google earlier this week called

**[12:17]** at Google earlier this week called anti-gravity. And we know that sometimes

**[12:19]** anti-gravity. And we know that sometimes

**[12:19]** anti-gravity. And we know that sometimes these web-based five coding tools you

**[12:22]** these web-based five coding tools you

**[12:22]** these web-based five coding tools you they have their limits and you may want

**[12:23]** they have their limits and you may want

**[12:24]** they have their limits and you may want to go into an IDE to add certain

**[12:26]** to go into an IDE to add certain

**[12:26]** to go into an IDE to add certain features to the application or make it

**[12:29]** features to the application or make it

**[12:29]** features to the application or make it specific to mobile things like that that

**[12:31]** specific to mobile things like that that

**[12:31]** specific to mobile things like that that might be a bit limiting in AI studio

**[12:33]** might be a bit limiting in AI studio

**[12:33]** might be a bit limiting in AI studio right now. So, we want it to be super

**[12:35]** right now. So, we want it to be super

**[12:35]** right now. So, we want it to be super easy to migrate into anti-gravity. So,

**[12:37]** easy to migrate into anti-gravity. So,

**[12:37]** easy to migrate into anti-gravity. So, what I did here was just a oneshot

**[12:39]** what I did here was just a oneshot

**[12:39]** what I did here was just a oneshot prompt of a screenshot of AI Studio. I

**[12:41]** prompt of a screenshot of AI Studio. I

**[12:41]** prompt of a screenshot of AI Studio. I said, "Clone this UI as closely as

**[12:43]** said, "Clone this UI as closely as

**[12:43]** said, "Clone this UI as closely as possible and then add a flow to export

**[12:46]** possible and then add a flow to export

**[12:46]** possible and then add a flow to export to our anti-gravity app." So, we can see

**[12:48]** to our anti-gravity app." So, we can see

**[12:48]** to our anti-gravity app." So, we can see it did a pretty great job of cloning

**[12:50]** it did a pretty great job of cloning

**[12:50]** it did a pretty great job of cloning light mode. The screenshot was in light

**[12:52]** light mode. The screenshot was in light

**[12:52]** light mode. The screenshot was in light mode, too, of our AI studio application

**[12:54]** mode, too, of our AI studio application

**[12:54]** mode, too, of our AI studio application and copying it and improving a little

**[12:56]** and copying it and improving a little

**[12:56]** and copying it and improving a little bit on Amar's designs. [laughter]

**[12:59]** bit on Amar's designs. [laughter]

**[12:59]** bit on Amar's designs. [laughter] But then we see this new anti-gravity


### [13:00 - 14:00]

**[13:01]** But then we see this new anti-gravity

**[13:01]** But then we see this new anti-gravity button that is creating my an export and

**[13:05]** button that is creating my an export and

**[13:05]** button that is creating my an export and then exporting it to anti-gravity. And I

**[13:07]** then exporting it to anti-gravity. And I

**[13:07]** then exporting it to anti-gravity. And I can go and open in the IDE. And I think

**[13:09]** can go and open in the IDE. And I think

**[13:09]** can go and open in the IDE. And I think these are the types of creative

**[13:11]** these are the types of creative

**[13:11]** these are the types of creative interactions that web-based vibe coding

**[13:13]** interactions that web-based vibe coding

**[13:13]** interactions that web-based vibe coding tools can be particularly useful for

**[13:15]** tools can be particularly useful for

**[13:15]** tools can be particularly useful for because if we had went and jammed on

**[13:17]** because if we had went and jammed on

**[13:17]** because if we had went and jammed on this feature, we probably would have

**[13:18]** this feature, we probably would have

**[13:18]** this feature, we probably would have constrained ourselves to existing

**[13:20]** constrained ourselves to existing

**[13:20]** constrained ourselves to existing patterns in AI Studio. And in this case,

**[13:22]** patterns in AI Studio. And in this case,

**[13:22]** patterns in AI Studio. And in this case, I told the model, be creative, think

**[13:24]** I told the model, be creative, think

**[13:24]** I told the model, be creative, think outside the box. And I've played with

**[13:25]** outside the box. And I've played with

**[13:25]** outside the box. And I've played with this one a bunch. Sometimes it gives a

**[13:27]** this one a bunch. Sometimes it gives a

**[13:27]** this one a bunch. Sometimes it gives a command line interface for export or

**[13:30]** command line interface for export or

**[13:30]** command line interface for export or showing the status of the export etc. Uh

**[13:33]** showing the status of the export etc. Uh

**[13:33]** showing the status of the export etc. Uh so I think it's a super cool way for you

**[13:35]** so I think it's a super cool way for you

**[13:35]** so I think it's a super cool way for you to ideulate on new ideas for UI and kind

**[13:39]** to ideulate on new ideas for UI and kind

**[13:39]** to ideulate on new ideas for UI and kind of expand on your product. Uh but I'll

**[13:41]** of expand on your product. Uh but I'll

**[13:41]** of expand on your product. Uh but I'll hand it back to Omar.

**[13:43]** hand it back to Omar.

**[13:43]** hand it back to Omar. >> Let's do it. Uh and then the other thing

**[13:45]** >> Let's do it. Uh and then the other thing

**[13:45]** >> Let's do it. Uh and then the other thing that Gemini 3 has been really impressed

**[13:46]** that Gemini 3 has been really impressed

**[13:46]** that Gemini 3 has been really impressed like impressed us with is just making

**[13:48]** like impressed us with is just making

**[13:48]** like impressed us with is just making video games. And so this one was again

**[13:51]** video games. And so this one was again

**[13:51]** video games. And so this one was again pretty simple prompts. Make this racing

**[13:52]** pretty simple prompts. Make this racing

**[13:52]** pretty simple prompts. Make this racing game where I have a bot now at a start

**[13:54]** game where I have a bot now at a start

**[13:54]** game where I have a bot now at a start screen. Um, and so you can see I got

**[13:57]** screen. Um, and so you can see I got

**[13:57]** screen. Um, and so you can see I got this 3D racing game in 3JS. Uh, it drew


### [14:00 - 15:00]

**[14:00]** this 3D racing game in 3JS. Uh, it drew

**[14:00]** this 3D racing game in 3JS. Uh, it drew all the things. I'm racing with a bot

**[14:02]** all the things. I'm racing with a bot

**[14:02]** all the things. I'm racing with a bot here. Uh, and then one thing I added for

**[14:04]** here. Uh, and then one thing I added for

**[14:04]** here. Uh, and then one thing I added for myself to cheat is I can just boost away

**[14:06]** myself to cheat is I can just boost away

**[14:06]** myself to cheat is I can just boost away and beat the bot. So, uh, pretty nice.

**[14:09]** and beat the bot. So, uh, pretty nice.

**[14:09]** and beat the bot. So, uh, pretty nice. But, [laughter] but the thing I want to

**[14:10]** But, [laughter] but the thing I want to

**[14:10]** But, [laughter] but the thing I want to tease actually is that um, all of these

**[14:13]** tease actually is that um, all of these

**[14:13]** tease actually is that um, all of these apps so far have been front-end React

**[14:15]** apps so far have been front-end React

**[14:15]** apps so far have been front-end React apps. Uh, and so the thing that's coming

**[14:16]** apps. Uh, and so the thing that's coming

**[14:16]** apps. Uh, and so the thing that's coming very very soon to AI Studio is going to

**[14:19]** very very soon to AI Studio is going to

**[14:19]** very very soon to AI Studio is going to be backend support um, and full stack

**[14:21]** be backend support um, and full stack

**[14:21]** be backend support um, and full stack runtime. So if you want to install Shad

**[14:23]** runtime. So if you want to install Shad

**[14:23]** runtime. So if you want to install Shad CN, if you want to do all of those

**[14:24]** CN, if you want to do all of those

**[14:24]** CN, if you want to do all of those things, you'll be able to do that again

**[14:26]** things, you'll be able to do that again

**[14:26]** things, you'll be able to do that again with one prompt. And the principle with

**[14:28]** with one prompt. And the principle with

**[14:28]** with one prompt. And the principle with AI studio here is that we don't want you

**[14:30]** AI studio here is that we don't want you

**[14:30]** AI studio here is that we don't want you to think about those details. You should

**[14:32]** to think about those details. You should

**[14:32]** to think about those details. You should just be able to ask, I want to make a

**[14:33]** just be able to ask, I want to make a

**[14:33]** just be able to ask, I want to make a multiplayer app, and we know that you

**[14:35]** multiplayer app, and we know that you

**[14:35]** multiplayer app, and we know that you need to use Express and wire that all up

**[14:37]** need to use Express and wire that all up

**[14:37]** need to use Express and wire that all up for you, uh, and abstract all those

**[14:39]** for you, uh, and abstract all those

**[14:39]** for you, uh, and abstract all those details away. So, we're going to try

**[14:41]** details away. So, we're going to try

**[14:41]** details away. So, we're going to try something a little risky here, which is

**[14:43]** something a little risky here, which is

**[14:43]** something a little risky here, which is we did turn this racing game into a

**[14:45]** we did turn this racing game into a

**[14:45]** we did turn this racing game into a multiplayer one. Um, and, uh, this was

**[14:48]** multiplayer one. Um, and, uh, this was

**[14:48]** multiplayer one. Um, and, uh, this was again a couple of prompts. Uh, so we're

**[14:50]** again a couple of prompts. Uh, so we're

**[14:50]** again a couple of prompts. Uh, so we're gonna put a QR code up if you want to

**[14:52]** gonna put a QR code up if you want to

**[14:52]** gonna put a QR code up if you want to join us uh in the racing game.

**[14:54]** join us uh in the racing game.

**[14:54]** join us uh in the racing game. >> We've never tried with nearly this many

**[14:55]** >> We've never tried with nearly this many

**[14:56]** >> We've never tried with nearly this many people, so we'll see. [laughter]

**[14:58]** people, so we'll see. [laughter]

**[14:58]** people, so we'll see. [laughter] >> Hopefully this works. Yeah.

**[14:59]** >> Hopefully this works. Yeah.

**[14:59]** >> Hopefully this works. Yeah. >> Uh, but QR codes up here. Uh, so if you


### [15:00 - 16:00]

**[15:03]** >> Uh, but QR codes up here. Uh, so if you

**[15:03]** >> Uh, but QR codes up here. Uh, so if you scan that, hopefully should load the

**[15:05]** scan that, hopefully should load the

**[15:05]** scan that, hopefully should load the game. I'm really afraid of how this is

**[15:06]** game. I'm really afraid of how this is

**[15:06]** game. I'm really afraid of how this is going to explode. [laughter]

**[15:07]** going to explode. [laughter]

**[15:07]** going to explode. [laughter] >> Here we go.

**[15:08]** >> Here we go.

**[15:08]** >> Here we go. >> All these cars loading in.

**[15:10]** >> All these cars loading in.

**[15:10]** >> All these cars loading in. >> Nice.

**[15:11]** >> Nice.

**[15:11]** >> Nice. >> So yeah, if people have scanned that, we

**[15:12]** >> So yeah, if people have scanned that, we

**[15:12]** >> So yeah, if people have scanned that, we can switch back to the game. Okay. Oh my

**[15:15]** can switch back to the game. Okay. Oh my

**[15:15]** can switch back to the game. Okay. Oh my god. [laughter]

**[15:20]** So yeah, just hit ready uh when you're

**[15:20]** So yeah, just hit ready uh when you're all ready. [laughter]

**[15:22]** all ready. [laughter]

**[15:22]** all ready. [laughter] Oh boy. Uh

**[15:25]** Oh boy. Uh

**[15:26]** Oh boy. Uh I think this lobby is going to explode.

**[15:28]** I think this lobby is going to explode.

**[15:28]** I think this lobby is going to explode. [laughter]

**[15:30]** [laughter]

**[15:30]** [laughter] >> Never leave.

**[15:31]** >> Never leave.

**[15:31]** >> Never leave. >> So this is where I shouldn't have added

**[15:32]** >> So this is where I shouldn't have added

**[15:32]** >> So this is where I shouldn't have added collisions with other cars because you

**[15:34]** collisions with other cars because you

**[15:34]** collisions with other cars because you could clearly see that we're bouncing

**[15:36]** could clearly see that we're bouncing

**[15:36]** could clearly see that we're bouncing around. [laughter]

**[15:38]** around. [laughter]

**[15:38]** around. [laughter] >> 19 players, 20 players. I don't know if

**[15:40]** >> 19 players, 20 players. I don't know if

**[15:40]** >> 19 players, 20 players. I don't know if this race will ever start, but we're all

**[15:42]** this race will ever start, but we're all

**[15:42]** this race will ever start, but we're all blocked on the uh you know the start

**[15:44]** blocked on the uh you know the start

**[15:44]** blocked on the uh you know the start line. But 23 players, pretty cool. Uh

**[15:47]** line. But 23 players, pretty cool. Uh

**[15:47]** line. But 23 players, pretty cool. Uh yeah, you do all have to get ready for

**[15:49]** yeah, you do all have to get ready for

**[15:49]** yeah, you do all have to get ready for us to start this race. So, [laughter]

**[15:52]** us to start this race. So, [laughter]

**[15:52]** us to start this race. So, [laughter] >> so we might be here all day.

**[15:56]** >> so we might be here all day.

**[15:56]** >> so we might be here all day. Uh but yeah, that is pretty pretty

**[15:57]** Uh but yeah, that is pretty pretty

**[15:58]** Uh but yeah, that is pretty pretty incredible. Um I can't start this race,


### [16:00 - 17:00]

**[16:00]** incredible. Um I can't start this race,

**[16:00]** incredible. Um I can't start this race, so do you want to wrap [laughter] up?

**[16:02]** so do you want to wrap [laughter] up?

**[16:02]** so do you want to wrap [laughter] up? >> We'll see you Ollie.

**[16:04]** >> We'll see you Ollie.

**[16:04]** >> We'll see you Ollie. >> That's pretty cool. The runtime didn't

**[16:05]** >> That's pretty cool. The runtime didn't

**[16:05]** >> That's pretty cool. The runtime didn't explode. Uh yeah, and I think we're

**[16:08]** explode. Uh yeah, and I think we're

**[16:08]** explode. Uh yeah, and I think we're super excited not only about the

**[16:09]** super excited not only about the

**[16:09]** super excited not only about the multiplayer game. So next time we will

**[16:11]** multiplayer game. So next time we will

**[16:11]** multiplayer game. So next time we will have even more of you folks join uh but

**[16:14]** have even more of you folks join uh but

**[16:14]** have even more of you folks join uh but also you know the extensibility that

**[16:16]** also you know the extensibility that

**[16:16]** also you know the extensibility that comes with a full stack runtime. Uh we

**[16:18]** comes with a full stack runtime. Uh we

**[16:18]** comes with a full stack runtime. Uh we want to make it super easy for you to

**[16:19]** want to make it super easy for you to

**[16:19]** want to make it super easy for you to integrate with our 1P and popular third

**[16:21]** integrate with our 1P and popular third

**[16:21]** integrate with our 1P and popular third party APIs etc. So very exciting next

**[16:24]** party APIs etc. So very exciting next

**[16:24]** party APIs etc. So very exciting next few months on the AI studio vibe coding

**[16:26]** few months on the AI studio vibe coding

**[16:26]** few months on the AI studio vibe coding side and super excited for you all to

**[16:28]** side and super excited for you all to

**[16:28]** side and super excited for you all to try it. Um, but I think the one thing I

**[16:30]** try it. Um, but I think the one thing I

**[16:30]** try it. Um, but I think the one thing I want to step back and emphasize is is

**[16:32]** want to step back and emphasize is is

**[16:32]** want to step back and emphasize is is what makes us so excited about this

**[16:33]** what makes us so excited about this

**[16:34]** what makes us so excited about this project and the work that a lot of us

**[16:36]** project and the work that a lot of us

**[16:36]** project and the work that a lot of us are doing is that we get to be the first

**[16:38]** are doing is that we get to be the first

**[16:38]** are doing is that we get to be the first generation of engineers who are building

**[16:40]** generation of engineers who are building

**[16:40]** generation of engineers who are building tools for a world where anyone can build

**[16:42]** tools for a world where anyone can build

**[16:42]** tools for a world where anyone can build software. So I think what's beautiful

**[16:44]** software. So I think what's beautiful

**[16:44]** software. So I think what's beautiful about things like vibe coding is

**[16:46]** about things like vibe coding is

**[16:46]** about things like vibe coding is watching people. We actually talking to

**[16:47]** watching people. We actually talking to

**[16:47]** watching people. We actually talking to a tech support person earlier this

**[16:49]** a tech support person earlier this

**[16:49]** a tech support person earlier this morning who said they started vibe

**[16:50]** morning who said they started vibe

**[16:50]** morning who said they started vibe coding and AI studio after seeing a

**[16:51]** coding and AI studio after seeing a

**[16:52]** coding and AI studio after seeing a YouTube video. And we're really

**[16:53]** YouTube video. And we're really

**[16:53]** YouTube video. And we're really democratizing who can create things and

**[16:55]** democratizing who can create things and

**[16:55]** democratizing who can create things and we're all getting to build those tools

**[16:57]** we're all getting to build those tools

**[16:57]** we're all getting to build those tools that enable that. And I think it forces

**[16:59]** that enable that. And I think it forces

**[16:59]** that enable that. And I think it forces us to rethink the paradigms that we've


### [17:00 - 18:00]

**[17:01]** us to rethink the paradigms that we've

**[17:02]** us to rethink the paradigms that we've become so used to. So it may not be your

**[17:04]** become so used to. So it may not be your

**[17:04]** become so used to. So it may not be your base IDE that people are starting from,

**[17:06]** base IDE that people are starting from,

**[17:06]** base IDE that people are starting from, but how can we intuit it as much of the

**[17:08]** but how can we intuit it as much of the

**[17:08]** but how can we intuit it as much of the user intent as possible? And that's what

**[17:10]** user intent as possible? And that's what

**[17:10]** user intent as possible? And that's what we want to do with full stack runtime

**[17:12]** we want to do with full stack runtime

**[17:12]** we want to do with full stack runtime and AI studio is make it very easy to

**[17:14]** and AI studio is make it very easy to

**[17:14]** and AI studio is make it very easy to not have to think about I want to add a

**[17:16]** not have to think about I want to add a

**[17:16]** not have to think about I want to add a database, but if your app needs storage,

**[17:18]** database, but if your app needs storage,

**[17:18]** database, but if your app needs storage, it'll have storage. If you want to have

**[17:20]** it'll have storage. If you want to have

**[17:20]** it'll have storage. If you want to have a if you have an e-commerce app, we'll

**[17:22]** a if you have an e-commerce app, we'll

**[17:22]** a if you have an e-commerce app, we'll add a payment solution and make it as

**[17:24]** add a payment solution and make it as

**[17:24]** add a payment solution and make it as easy as possible to build the future of

**[17:26]** easy as possible to build the future of

**[17:26]** easy as possible to build the future of software. Um, so thank you folks for

**[17:29]** software. Um, so thank you folks for

**[17:29]** software. Um, so thank you folks for joining us. If you have any cool

**[17:30]** joining us. If you have any cool

**[17:30]** joining us. If you have any cool examples you've built or questions, feel

**[17:32]** examples you've built or questions, feel

**[17:32]** examples you've built or questions, feel free to ping me and Amara on Twitter.

**[17:35]** free to ping me and Amara on Twitter.

**[17:35]** free to ping me and Amara on Twitter. Uh, and yeah, enjoy the rest of the day.

**[17:36]** Uh, and yeah, enjoy the rest of the day.

**[17:36]** Uh, and yeah, enjoy the rest of the day. >> Yeah, thank you. [applause]

**[17:40]** >> Yeah, thank you. [applause]

**[17:40]** >> Yeah, thank you. [applause] [music]

**[17:56]** >> [music]

**[17:56]** >> [music] >> Heat.


