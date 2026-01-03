# Form factors for your new AI coworkers — Craig Wattrus, Flatfile

**Video URL:** https://www.youtube.com/watch?v=CiMVKnX-CNI

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** I I think we've all noticed tools like

**[00:17]** I I think we've all noticed tools like V0ero uh getting pretty good at at

**[00:19]** V0ero uh getting pretty good at at

**[00:19]** V0ero uh getting pretty good at at generative UI and creating um

**[00:21]** generative UI and creating um

**[00:22]** generative UI and creating um good-looking things as well as clawed

**[00:24]** good-looking things as well as clawed

**[00:24]** good-looking things as well as clawed code um being able to let us run things

**[00:27]** code um being able to let us run things

**[00:27]** code um being able to let us run things more complicated locally and build on

**[00:29]** more complicated locally and build on

**[00:30]** more complicated locally and build on those things. Um, so I think the the

**[00:32]** those things. Um, so I think the the

**[00:32]** those things. Um, so I think the the thing that comes out of this is

**[00:34]** thing that comes out of this is

**[00:34]** thing that comes out of this is designers, um, product people and

**[00:36]** designers, um, product people and

**[00:36]** designers, um, product people and engineers all building together. And I'm

**[00:38]** engineers all building together. And I'm

**[00:38]** engineers all building together. And I'm really excited about that because I've

**[00:39]** really excited about that because I've

**[00:39]** really excited about that because I've never loved the the divides um, between

**[00:42]** never loved the the divides um, between

**[00:42]** never loved the the divides um, between these things. Um, so this really lets us

**[00:45]** these things. Um, so this really lets us

**[00:45]** these things. Um, so this really lets us get rid of um, in my mind get rid of

**[00:47]** get rid of um, in my mind get rid of

**[00:47]** get rid of um, in my mind get rid of mock-ups, get rid of the click-through

**[00:49]** mock-ups, get rid of the click-through

**[00:49]** mock-ups, get rid of the click-through prototypes um, and uh, all the hand

**[00:52]** prototypes um, and uh, all the hand

**[00:52]** prototypes um, and uh, all the hand ringing about whether uh, the thing that

**[00:54]** ringing about whether uh, the thing that

**[00:54]** ringing about whether uh, the thing that we're building um, is worth the

**[00:56]** we're building um, is worth the

**[00:56]** we're building um, is worth the engineering effort. Um, so as we as we

**[00:59]** engineering effort. Um, so as we as we

**[00:59]** engineering effort. Um, so as we as we go into this, it's time for us to jump


### [01:00 - 02:00]

**[01:01]** go into this, it's time for us to jump

**[01:01]** go into this, it's time for us to jump in um and feel the material that we're

**[01:03]** in um and feel the material that we're

**[01:03]** in um and feel the material that we're working with and see what emerges. So

**[01:05]** working with and see what emerges. So

**[01:05]** working with and see what emerges. So I'll give you a super quick overview of

**[01:07]** I'll give you a super quick overview of

**[01:07]** I'll give you a super quick overview of of Flat Files um AI uh stack. This is

**[01:11]** of Flat Files um AI uh stack. This is

**[01:11]** of Flat Files um AI uh stack. This is not an official diagram, but it's how I

**[01:12]** not an official diagram, but it's how I

**[01:12]** not an official diagram, but it's how I see it. Um we migrate data um big if if

**[01:16]** see it. Um we migrate data um big if if

**[01:16]** see it. Um we migrate data um big if if you needed to move a lot of data between

**[01:17]** you needed to move a lot of data between

**[01:18]** you needed to move a lot of data between systems um frequently uh you use our

**[01:21]** systems um frequently uh you use our

**[01:21]** systems um frequently uh you use our developer platform. And since we're a

**[01:22]** developer platform. And since we're a

**[01:22]** developer platform. And since we're a developer platform, LMS are good at

**[01:24]** developer platform, LMS are good at

**[01:24]** developer platform, LMS are good at writing code. Makes it the perfect place

**[01:26]** writing code. Makes it the perfect place

**[01:26]** writing code. Makes it the perfect place for a lot of AI. Um, at the bottom here,

**[01:29]** for a lot of AI. Um, at the bottom here,

**[01:29]** for a lot of AI. Um, at the bottom here, we have our our customers flat file

**[01:31]** we have our our customers flat file

**[01:31]** we have our our customers flat file applications that they they deploy to

**[01:33]** applications that they they deploy to

**[01:33]** applications that they they deploy to our infrastructure. Um, then there's

**[01:35]** our infrastructure. Um, then there's

**[01:35]** our infrastructure. Um, then there's this like real time context, which is

**[01:37]** this like real time context, which is

**[01:37]** this like real time context, which is the data and the validation outcomes.

**[01:39]** the data and the validation outcomes.

**[01:39]** the data and the validation outcomes. So, what are the errors and warnings and

**[01:41]** So, what are the errors and warnings and

**[01:41]** So, what are the errors and warnings and things that are in that that data that

**[01:42]** things that are in that that data that

**[01:42]** things that are in that that data that dirty data um and then our AI agents,

**[01:45]** dirty data um and then our AI agents,

**[01:45]** dirty data um and then our AI agents, the tools they have um and the jobs that

**[01:48]** the tools they have um and the jobs that

**[01:48]** the tools they have um and the jobs that they can run um and then what gets shown

**[01:50]** they can run um and then what gets shown

**[01:50]** they can run um and then what gets shown to users. So I see it as four buckets

**[01:52]** to users. So I see it as four buckets

**[01:52]** to users. So I see it as four buckets here. There's more. Um there's

**[01:55]** here. There's more. Um there's

**[01:55]** here. There's more. Um there's invisible, so it's kind of like the

**[01:56]** invisible, so it's kind of like the

**[01:56]** invisible, so it's kind of like the ghost in the machine almost called that

**[01:58]** ghost in the machine almost called that

**[01:58]** ghost in the machine almost called that ghost. Um ambient, so it's kind of


### [02:00 - 03:00]

**[02:01]** ghost. Um ambient, so it's kind of

**[02:01]** ghost. Um ambient, so it's kind of happening in the space, but you're not

**[02:03]** happening in the space, but you're not

**[02:03]** happening in the space, but you're not directly working with it. Um inline, so

**[02:06]** directly working with it. Um inline, so

**[02:06]** directly working with it. Um inline, so it's actually in your work uh in your

**[02:07]** it's actually in your work uh in your

**[02:08]** it's actually in your work uh in your workflow. And then conversational, the

**[02:09]** workflow. And then conversational, the

**[02:09]** workflow. And then conversational, the ones that we're um I guess all arguing

**[02:12]** ones that we're um I guess all arguing

**[02:12]** ones that we're um I guess all arguing about. I think that's what I learned um

**[02:14]** about. I think that's what I learned um

**[02:14]** about. I think that's what I learned um being here at this conference. Um here's

**[02:16]** being here at this conference. Um here's

**[02:16]** being here at this conference. Um here's an example of invisible. So when you

**[02:18]** an example of invisible. So when you

**[02:18]** an example of invisible. So when you start uh if you sign up for a flat file,

**[02:20]** start uh if you sign up for a flat file,

**[02:20]** start uh if you sign up for a flat file, we go in the background, we we take your

**[02:22]** we go in the background, we we take your

**[02:22]** we go in the background, we we take your email address, we find the company you

**[02:24]** email address, we find the company you

**[02:24]** email address, we find the company you work for, we look it up um and in the

**[02:26]** work for, we look it up um and in the

**[02:26]** work for, we look it up um and in the background, the AI agents are writing a

**[02:29]** background, the AI agents are writing a

**[02:29]** background, the AI agents are writing a flat file application. So they're

**[02:30]** flat file application. So they're

**[02:30]** flat file application. So they're writing code and essentially sending you

**[02:32]** writing code and essentially sending you

**[02:32]** writing code and essentially sending you up a demo that is perfect for your use

**[02:34]** up a demo that is perfect for your use

**[02:34]** up a demo that is perfect for your use case. So if you come in from a HR

**[02:36]** case. So if you come in from a HR

**[02:36]** case. So if you come in from a HR company, you're going to get an HR um

**[02:39]** company, you're going to get an HR um

**[02:39]** company, you're going to get an HR um demo. Um and while that's running, you

**[02:41]** demo. Um and while that's running, you

**[02:41]** demo. Um and while that's running, you don't need to know that AI is working on

**[02:42]** don't need to know that AI is working on

**[02:42]** don't need to know that AI is working on it. Um so that I'd say is like it's

**[02:44]** it. Um so that I'd say is like it's

**[02:44]** it. Um so that I'd say is like it's working in the background. Here's

**[02:46]** working in the background. Here's

**[02:46]** working in the background. Here's something working more ambiently. It's a

**[02:48]** something working more ambiently. It's a

**[02:48]** something working more ambiently. It's a very initial uh take on this, but you

**[02:50]** very initial uh take on this, but you

**[02:50]** very initial uh take on this, but you can see there's something an agent

**[02:52]** can see there's something an agent

**[02:52]** can see there's something an agent analyzing the data in the background. Um

**[02:55]** analyzing the data in the background. Um

**[02:55]** analyzing the data in the background. Um this is a tool actually um I lead this

**[02:57]** this is a tool actually um I lead this

**[02:57]** this is a tool actually um I lead this team for AI transformation and um you


### [03:00 - 04:00]

**[03:00]** team for AI transformation and um you

**[03:00]** team for AI transformation and um you can see the little sparkles pop up on

**[03:02]** can see the little sparkles pop up on

**[03:02]** can see the little sparkles pop up on the columns when it finds um

**[03:04]** the columns when it finds um

**[03:04]** the columns when it finds um opportunities to fix it. So that's

**[03:06]** opportunities to fix it. So that's

**[03:06]** opportunities to fix it. So that's ambient. Um this is inline. So you're

**[03:09]** ambient. Um this is inline. So you're

**[03:09]** ambient. Um this is inline. So you're busy working in the data um and the AI

**[03:11]** busy working in the data um and the AI

**[03:11]** busy working in the data um and the AI is able you're able to use the AI um

**[03:13]** is able you're able to use the AI um

**[03:13]** is able you're able to use the AI um directly in line here um to fix the

**[03:15]** directly in line here um to fix the

**[03:15]** directly in line here um to fix the data. These agents are are writing code

**[03:19]** data. These agents are are writing code

**[03:19]** data. These agents are are writing code that then gets run on this data set. So

**[03:20]** that then gets run on this data set. So

**[03:20]** that then gets run on this data set. So you could have a million rows um and 50

**[03:23]** you could have a million rows um and 50

**[03:23]** you could have a million rows um and 50 columns or whatever you want and and

**[03:25]** columns or whatever you want and and

**[03:25]** columns or whatever you want and and that code will run really fast um which

**[03:28]** that code will run really fast um which

**[03:28]** that code will run really fast um which is pretty cool. And then finally the

**[03:30]** is pretty cool. And then finally the

**[03:30]** is pretty cool. And then finally the conversational ones we're all used to.

**[03:32]** conversational ones we're all used to.

**[03:32]** conversational ones we're all used to. So this is build mode. It's the no code

**[03:34]** So this is build mode. It's the no code

**[03:34]** So this is build mode. It's the no code low code um agentic system that writes

**[03:37]** low code um agentic system that writes

**[03:37]** low code um agentic system that writes flat file apps now. So before you would

**[03:40]** flat file apps now. So before you would

**[03:40]** flat file apps now. So before you would probably have to have had a engineer at

**[03:42]** probably have to have had a engineer at

**[03:42]** probably have to have had a engineer at the company um building these

**[03:43]** the company um building these

**[03:43]** the company um building these applications um now it can all be built

**[03:46]** applications um now it can all be built

**[03:46]** applications um now it can all be built up. So that's pretty cool. Um and that's

**[03:50]** up. So that's pretty cool. Um and that's

**[03:50]** up. So that's pretty cool. Um and that's that's kind of the the general surfaces

**[03:52]** that's kind of the the general surfaces

**[03:52]** that's kind of the the general surfaces I think about. Um, I listened to um

**[03:55]** I think about. Um, I listened to um

**[03:55]** I think about. Um, I listened to um Amanda Ascal um from Anthropic talking

**[03:58]** Amanda Ascal um from Anthropic talking

**[03:58]** Amanda Ascal um from Anthropic talking to Lex Freiedman about um building um


### [04:00 - 05:00]

**[04:00]** to Lex Freiedman about um building um

**[04:00]** to Lex Freiedman about um building um Claude's character. And in that moment,

**[04:02]** Claude's character. And in that moment,

**[04:02]** Claude's character. And in that moment, I realized I'd been doing something a

**[04:04]** I realized I'd been doing something a

**[04:04]** I realized I'd been doing something a little silly. I'd been giving engineers

**[04:06]** little silly. I'd been giving engineers

**[04:06]** little silly. I'd been giving engineers feedback on our agents like, "Oh, it

**[04:09]** feedback on our agents like, "Oh, it

**[04:09]** feedback on our agents like, "Oh, it shouldn't start saying this and it

**[04:10]** shouldn't start saying this and it

**[04:10]** shouldn't start saying this and it shouldn't use these words and and why

**[04:12]** shouldn't use these words and and why

**[04:12]** shouldn't use these words and and why should it do this?" And I realized I was

**[04:14]** should it do this?" And I realized I was

**[04:14]** should it do this?" And I realized I was I was doing it like I would do design

**[04:16]** I was doing it like I would do design

**[04:16]** I was doing it like I would do design copy, right? I was I was I'm in my my my

**[04:19]** copy, right? I was I was I'm in my my my

**[04:19]** copy, right? I was I was I'm in my my my normal instinct. And when I heard her

**[04:21]** normal instinct. And when I heard her

**[04:21]** normal instinct. And when I heard her talk, I realized I needed to go from

**[04:23]** talk, I realized I needed to go from

**[04:24]** talk, I realized I needed to go from controlling um to being a character

**[04:26]** controlling um to being a character

**[04:26]** controlling um to being a character coach and and and actually building out

**[04:29]** coach and and and actually building out

**[04:29]** coach and and and actually building out um the the nature that I wanted.

**[04:32]** um the the nature that I wanted.

**[04:32]** um the the nature that I wanted. So this is a Vzero. I hope have you most

**[04:35]** So this is a Vzero. I hope have you most

**[04:36]** So this is a Vzero. I hope have you most of you used Vzero from Versell before?

**[04:38]** of you used Vzero from Versell before?

**[04:38]** of you used Vzero from Versell before? Um yeah. Um so this is a Vzero I built

**[04:40]** Um yeah. Um so this is a Vzero I built

**[04:40]** Um yeah. Um so this is a Vzero I built one of my early ones and it was um I

**[04:42]** one of my early ones and it was um I

**[04:42]** one of my early ones and it was um I called it a chat tuner. It doesn't look

**[04:44]** called it a chat tuner. It doesn't look

**[04:44]** called it a chat tuner. It doesn't look like much but that wasn't the focus. Um,

**[04:46]** like much but that wasn't the focus. Um,

**[04:46]** like much but that wasn't the focus. Um, but I could essentially um put our

**[04:48]** but I could essentially um put our

**[04:48]** but I could essentially um put our orchestrators, so the system prompt for

**[04:50]** orchestrators, so the system prompt for

**[04:50]** orchestrators, so the system prompt for our AI orchestrator for build mode um in

**[04:53]** our AI orchestrator for build mode um in

**[04:53]** our AI orchestrator for build mode um in here. And then I can modify it. I can

**[04:55]** here. And then I can modify it. I can

**[04:55]** here. And then I can modify it. I can say what is it like if I tell Claude to

**[04:57]** say what is it like if I tell Claude to

**[04:57]** say what is it like if I tell Claude to be more friendly versus more balanced

**[04:59]** be more friendly versus more balanced

**[04:59]** be more friendly versus more balanced versus more concise? What what does more


### [05:00 - 06:00]

**[05:02]** versus more concise? What what does more

**[05:02]** versus more concise? What what does more cautious mean to this model? Um, and the

**[05:06]** cautious mean to this model? Um, and the

**[05:06]** cautious mean to this model? Um, and the point of me showing this is just to say

**[05:08]** point of me showing this is just to say

**[05:08]** point of me showing this is just to say like the design of the final thing is

**[05:11]** like the design of the final thing is

**[05:11]** like the design of the final thing is always a tempting thing to design too.

**[05:13]** always a tempting thing to design too.

**[05:13]** always a tempting thing to design too. Um but now we can actually go and build

**[05:15]** Um but now we can actually go and build

**[05:15]** Um but now we can actually go and build tools to help us to design that. Um and

**[05:20]** tools to help us to design that. Um and

**[05:20]** tools to help us to design that. Um and this brings me to like uh I have like

**[05:21]** this brings me to like uh I have like

**[05:21]** this brings me to like uh I have like three themes. Um the first theme which

**[05:23]** three themes. Um the first theme which

**[05:24]** three themes. Um the first theme which is feeling the material. I'm a

**[05:25]** is feeling the material. I'm a

**[05:25]** is feeling the material. I'm a woodworker so you'll have to forgive the

**[05:27]** woodworker so you'll have to forgive the

**[05:27]** woodworker so you'll have to forgive the analogies to physical material but if

**[05:30]** analogies to physical material but if

**[05:30]** analogies to physical material but if you're going to uh design something with

**[05:32]** you're going to uh design something with

**[05:32]** you're going to uh design something with a physical material, you have to feel

**[05:34]** a physical material, you have to feel

**[05:34]** a physical material, you have to feel it, right? You have to what are the

**[05:35]** it, right? You have to what are the

**[05:36]** it, right? You have to what are the properties of it? Um and you need to

**[05:38]** properties of it? Um and you need to

**[05:38]** properties of it? Um and you need to understand it. And so I feel like before

**[05:41]** understand it. And so I feel like before

**[05:41]** understand it. And so I feel like before with design, we were kind of looking at

**[05:43]** with design, we were kind of looking at

**[05:43]** with design, we were kind of looking at everything through like layers, right?

**[05:45]** everything through like layers, right?

**[05:45]** everything through like layers, right? Mockups and prototypes and and kind of

**[05:47]** Mockups and prototypes and and kind of

**[05:47]** Mockups and prototypes and and kind of trying to see what was going to work and

**[05:49]** trying to see what was going to work and

**[05:49]** trying to see what was going to work and what wasn't. What we need to do now is

**[05:51]** what wasn't. What we need to do now is

**[05:51]** what wasn't. What we need to do now is go feel the material, feel feel how

**[05:53]** go feel the material, feel feel how

**[05:53]** go feel the material, feel feel how these models work. Um, my new north star

**[05:56]** these models work. Um, my new north star

**[05:56]** these models work. Um, my new north star is like creating an environment for


### [06:00 - 07:00]

**[06:00]** is like creating an environment for

**[06:00]** is like creating an environment for these LLMs to shine, right? what's

**[06:02]** these LLMs to shine, right? what's

**[06:02]** these LLMs to shine, right? what's what's this form factor that can help

**[06:04]** what's this form factor that can help

**[06:04]** what's this form factor that can help them nail their assignment, stay

**[06:06]** them nail their assignment, stay

**[06:06]** them nail their assignment, stay aligned, and grow as the models get

**[06:09]** aligned, and grow as the models get

**[06:09]** aligned, and grow as the models get better, right? That's that's my new

**[06:10]** better, right? That's that's my new

**[06:10]** better, right? That's that's my new goal. Um, we're basically anything we do

**[06:14]** goal. Um, we're basically anything we do

**[06:14]** goal. Um, we're basically anything we do with an LLM, I feel like we're putting

**[06:15]** with an LLM, I feel like we're putting

**[06:15]** with an LLM, I feel like we're putting it in a box. Um, and that you also hear

**[06:19]** it in a box. Um, and that you also hear

**[06:19]** it in a box. Um, and that you also hear people say that LLMs are like interns,

**[06:21]** people say that LLMs are like interns,

**[06:21]** people say that LLMs are like interns, like, oh, it's an intern with a PhD. And

**[06:23]** like, oh, it's an intern with a PhD. And

**[06:23]** like, oh, it's an intern with a PhD. And so I try think now if you're putting an

**[06:26]** so I try think now if you're putting an

**[06:26]** so I try think now if you're putting an intern with a PhD in a box, like it

**[06:28]** intern with a PhD in a box, like it

**[06:28]** intern with a PhD in a box, like it better be a good box. Um and so we need

**[06:30]** better be a good box. Um and so we need

**[06:30]** better be a good box. Um and so we need to put effort in. Um this was a

**[06:33]** to put effort in. Um this was a

**[06:33]** to put effort in. Um this was a conversation we were having about what

**[06:35]** conversation we were having about what

**[06:35]** conversation we were having about what tools does this uh co-worker this new

**[06:37]** tools does this uh co-worker this new

**[06:38]** tools does this uh co-worker this new form factor this new model like what

**[06:39]** form factor this new model like what

**[06:40]** form factor this new model like what tools do we give it when it shows up for

**[06:42]** tools do we give it when it shows up for

**[06:42]** tools do we give it when it shows up for work and uh I got fixated on this idea

**[06:44]** work and uh I got fixated on this idea

**[06:44]** work and uh I got fixated on this idea of cursors. I was like oh what happens

**[06:46]** of cursors. I was like oh what happens

**[06:46]** of cursors. I was like oh what happens if it just had a mouse or a trackpad?

**[06:48]** if it just had a mouse or a trackpad?

**[06:48]** if it just had a mouse or a trackpad? I'm a trackpad person. Um so um that's

**[06:51]** I'm a trackpad person. Um so um that's

**[06:51]** I'm a trackpad person. Um so um that's probably controversial but uh

**[06:52]** probably controversial but uh

**[06:52]** probably controversial but uh essentially what happens if we gave the

**[06:54]** essentially what happens if we gave the

**[06:54]** essentially what happens if we gave the AI um those tools and so I I created

**[06:57]** AI um those tools and so I I created

**[06:57]** AI um those tools and so I I created this v0ero and moved it into cursor um


### [07:00 - 08:00]

**[07:01]** this v0ero and moved it into cursor um

**[07:01]** this v0ero and moved it into cursor um and I was like well I work in design

**[07:02]** and I was like well I work in design

**[07:02]** and I was like well I work in design tools a lot so I don't migrate a lot of

**[07:05]** tools a lot so I don't migrate a lot of

**[07:05]** tools a lot so I don't migrate a lot of data so this is the best place for me to

**[07:06]** data so this is the best place for me to

**[07:06]** data so this is the best place for me to feel this right to feel this material so

**[07:09]** feel this right to feel this material so

**[07:09]** feel this right to feel this material so I created a canvas um and I could give

**[07:11]** I created a canvas um and I could give

**[07:11]** I created a canvas um and I could give it orders and be like hey and honestly I

**[07:14]** it orders and be like hey and honestly I

**[07:14]** it orders and be like hey and honestly I was I was very enthusiastic about this

**[07:16]** was I was very enthusiastic about this

**[07:16]** was I was very enthusiastic about this um for like a few seconds um it felt

**[07:19]** um for like a few seconds um it felt

**[07:19]** um for like a few seconds um it felt like I was touching the AGI a little

**[07:20]** like I was touching the AGI a little

**[07:20]** like I was touching the AGI a little bit. Um, but I also very quickly started

**[07:23]** bit. Um, but I also very quickly started

**[07:23]** bit. Um, but I also very quickly started feeling like I was putting a Formula 1

**[07:25]** feeling like I was putting a Formula 1

**[07:25]** feeling like I was putting a Formula 1 driver in a Prius. It just it felt like

**[07:27]** driver in a Prius. It just it felt like

**[07:27]** driver in a Prius. It just it felt like I was constraining it and controlling

**[07:28]** I was constraining it and controlling

**[07:28]** I was constraining it and controlling it. Um, it could only move one thing at

**[07:31]** it. Um, it could only move one thing at

**[07:32]** it. Um, it could only move one thing at a time. Um but so so learning from that

**[07:36]** a time. Um but so so learning from that

**[07:36]** a time. Um but so so learning from that um was uh something like this was just

**[07:38]** um was uh something like this was just

**[07:38]** um was uh something like this was just also um a a vzero um that I use clawed

**[07:42]** also um a a vzero um that I use clawed

**[07:42]** also um a a vzero um that I use clawed code on eventually and this is a new uh

**[07:44]** code on eventually and this is a new uh

**[07:44]** code on eventually and this is a new uh product that we're working on which

**[07:45]** product that we're working on which

**[07:45]** product that we're working on which brings like the all the stuff we've

**[07:47]** brings like the all the stuff we've

**[07:47]** brings like the all the stuff we've learned about u migrating data to

**[07:50]** learned about u migrating data to

**[07:50]** learned about u migrating data to consumers to let them work on their data

**[07:53]** consumers to let them work on their data

**[07:53]** consumers to let them work on their data um but you can see the AI is is

**[07:54]** um but you can see the AI is is

**[07:54]** um but you can see the AI is is operating in the space um and it's it's

**[07:57]** operating in the space um and it's it's

**[07:58]** operating in the space um and it's it's got presence and so it's it's able to


### [08:00 - 09:00]

**[08:00]** got presence and so it's it's able to

**[08:00]** got presence and so it's it's able to read multiple files while writing into

**[08:02]** read multiple files while writing into

**[08:02]** read multiple files while writing into another one. Um, it's not like me who

**[08:05]** another one. Um, it's not like me who

**[08:05]** another one. Um, it's not like me who can only focus on one thing at a time.

**[08:07]** can only focus on one thing at a time.

**[08:07]** can only focus on one thing at a time. Even though I think I can focus on more,

**[08:10]** Even though I think I can focus on more,

**[08:10]** Even though I think I can focus on more, um, it's not true. And so this is us

**[08:12]** um, it's not true. And so this is us

**[08:12]** um, it's not true. And so this is us moving from determinism to infer and

**[08:15]** moving from determinism to infer and

**[08:15]** moving from determinism to infer and figuring out what this material feels

**[08:17]** figuring out what this material feels

**[08:17]** figuring out what this material feels like. And so, um, that's feeling the

**[08:21]** like. And so, um, that's feeling the

**[08:22]** like. And so, um, that's feeling the material, right? working with the model,

**[08:24]** material, right? working with the model,

**[08:24]** material, right? working with the model, getting it into your space,

**[08:25]** getting it into your space,

**[08:25]** getting it into your space, understanding how it feels um to work

**[08:27]** understanding how it feels um to work

**[08:28]** understanding how it feels um to work alongside it, what's it capable of, and

**[08:30]** alongside it, what's it capable of, and

**[08:30]** alongside it, what's it capable of, and then the form factors that we're putting

**[08:31]** then the form factors that we're putting

**[08:31]** then the form factors that we're putting on them. Actually, actually, you can now

**[08:33]** on them. Actually, actually, you can now

**[08:33]** on them. Actually, actually, you can now go build it and play with it, um and

**[08:35]** go build it and play with it, um and

**[08:35]** go build it and play with it, um and feel it. Um the next material analogy I

**[08:38]** feel it. Um the next material analogy I

**[08:38]** feel it. Um the next material analogy I have, which is finding the grain. Um

**[08:40]** have, which is finding the grain. Um

**[08:40]** have, which is finding the grain. Um once you've got the characteristics of

**[08:42]** once you've got the characteristics of

**[08:42]** once you've got the characteristics of the material, you understand it. Um

**[08:44]** the material, you understand it. Um

**[08:44]** the material, you understand it. Um usually the piece of material that

**[08:46]** usually the piece of material that

**[08:46]** usually the piece of material that you're building with and you're creating

**[08:47]** you're building with and you're creating

**[08:47]** you're building with and you're creating with might have its own characteristics.

**[08:49]** with might have its own characteristics.

**[08:49]** with might have its own characteristics. And so as we're creating these form

**[08:51]** And so as we're creating these form

**[08:51]** And so as we're creating these form factors, uh, finding the grain is about

**[08:53]** factors, uh, finding the grain is about

**[08:53]** factors, uh, finding the grain is about feeling it out. Where is it smooth and

**[08:55]** feeling it out. Where is it smooth and

**[08:55]** feeling it out. Where is it smooth and rough? Um, where is it weak? Where is it

**[08:57]** rough? Um, where is it weak? Where is it

**[08:57]** rough? Um, where is it weak? Where is it strong? Um, and we'll have to remain


### [09:00 - 10:00]

**[09:00]** strong? Um, and we'll have to remain

**[09:00]** strong? Um, and we'll have to remain humble here because, um, things are

**[09:03]** humble here because, um, things are

**[09:03]** humble here because, um, things are going to change and are changing so

**[09:04]** going to change and are changing so

**[09:04]** going to change and are changing so quickly that whatever we we build is

**[09:07]** quickly that whatever we we build is

**[09:07]** quickly that whatever we we build is going to most likely need to be rebuilt.

**[09:10]** going to most likely need to be rebuilt.

**[09:10]** going to most likely need to be rebuilt. This was an example of that build mode

**[09:11]** This was an example of that build mode

**[09:11]** This was an example of that build mode agent. I asked it to do one thing, which

**[09:14]** agent. I asked it to do one thing, which

**[09:14]** agent. I asked it to do one thing, which was enable the automat plugin. So this

**[09:16]** was enable the automat plugin. So this

**[09:16]** was enable the automat plugin. So this just automatically maps data from the

**[09:18]** just automatically maps data from the

**[09:18]** just automatically maps data from the source. um data to the target data and I

**[09:21]** source. um data to the target data and I

**[09:21]** source. um data to the target data and I get a wall of text and it's not bad

**[09:24]** get a wall of text and it's not bad

**[09:24]** get a wall of text and it's not bad because this went and and I saved me

**[09:26]** because this went and and I saved me

**[09:26]** because this went and and I saved me probably a week of work. Um I didn't

**[09:27]** probably a week of work. Um I didn't

**[09:27]** probably a week of work. Um I didn't have to have a product manager write a

**[09:28]** have to have a product manager write a

**[09:28]** have to have a product manager write a PRD, send it to an engineer, get the in

**[09:32]** PRD, send it to an engineer, get the in

**[09:32]** PRD, send it to an engineer, get the in the road map, get the engineer to write

**[09:33]** the road map, get the engineer to write

**[09:33]** the road map, get the engineer to write it, QA. This was all just done, right?

**[09:35]** it, QA. This was all just done, right?

**[09:35]** it, QA. This was all just done, right? All that code was written. Um but the

**[09:37]** All that code was written. Um but the

**[09:37]** All that code was written. Um but the noise gets in the way. And so this was a

**[09:40]** noise gets in the way. And so this was a

**[09:40]** noise gets in the way. And so this was a vzero of of kind of rethinking the tool

**[09:43]** vzero of of kind of rethinking the tool

**[09:43]** vzero of of kind of rethinking the tool UX. What could it be like? And so, um,

**[09:46]** UX. What could it be like? And so, um,

**[09:46]** UX. What could it be like? And so, um, the way I thought about this was if

**[09:48]** the way I thought about this was if

**[09:48]** the way I thought about this was if you're designing for a if you're if

**[09:50]** you're designing for a if you're if

**[09:50]** you're designing for a if you're if you're going to a co-orker and you're

**[09:51]** you're going to a co-orker and you're

**[09:51]** you're going to a co-orker and you're going to do something complicated for

**[09:53]** going to do something complicated for

**[09:53]** going to do something complicated for them and you want to communicate, you

**[09:55]** them and you want to communicate, you

**[09:55]** them and you want to communicate, you think, okay, I'm going to choose my

**[09:56]** think, okay, I'm going to choose my

**[09:56]** think, okay, I'm going to choose my words carefully. I'm going to

**[09:57]** words carefully. I'm going to

**[09:58]** words carefully. I'm going to communicate visually. Um, I'm going to


### [10:00 - 11:00]

**[10:00]** communicate visually. Um, I'm going to

**[10:00]** communicate visually. Um, I'm going to stop and check um whether whether it's

**[10:02]** stop and check um whether whether it's

**[10:02]** stop and check um whether whether it's right. And so, I wanted this to feel

**[10:04]** right. And so, I wanted this to feel

**[10:04]** right. And so, I wanted this to feel similar. And so, you can see here split

**[10:06]** similar. And so, you can see here split

**[10:06]** similar. And so, you can see here split personal details. It's visually telling

**[10:08]** personal details. It's visually telling

**[10:08]** personal details. It's visually telling you what it's doing. Saying, "Hey, is

**[10:10]** you what it's doing. Saying, "Hey, is

**[10:10]** you what it's doing. Saying, "Hey, is this right?" Then it's saying, "I'm

**[10:11]** this right?" Then it's saying, "I'm

**[10:12]** this right?" Then it's saying, "I'm aligned. I took a snapshot. You can roll

**[10:13]** aligned. I took a snapshot. You can roll

**[10:13]** aligned. I took a snapshot. You can roll back. I'm holding you accountable. You

**[10:16]** back. I'm holding you accountable. You

**[10:16]** back. I'm holding you accountable. You approved this. Um, and then telling you

**[10:18]** approved this. Um, and then telling you

**[10:18]** approved this. Um, and then telling you what you can do next. We also wanted to

**[10:20]** what you can do next. We also wanted to

**[10:20]** what you can do next. We also wanted to it to be able to express itself. So if

**[10:22]** it to be able to express itself. So if

**[10:22]** it to be able to express itself. So if something went wrong, kind of shaking

**[10:23]** something went wrong, kind of shaking

**[10:24]** something went wrong, kind of shaking its head and a little bit of

**[10:25]** its head and a little bit of

**[10:25]** its head and a little bit of frustration, which is probably what the

**[10:26]** frustration, which is probably what the

**[10:26]** frustration, which is probably what the user is feeling too um when something

**[10:28]** user is feeling too um when something

**[10:28]** user is feeling too um when something goes wrong. Um,

**[10:31]** goes wrong. Um,

**[10:31]** goes wrong. Um, and then finally, it can back off uh

**[10:33]** and then finally, it can back off uh

**[10:34]** and then finally, it can back off uh when it gets something wrong and sort of

**[10:35]** when it gets something wrong and sort of

**[10:35]** when it gets something wrong and sort of say, "Okay, I'm handing control back

**[10:38]** say, "Okay, I'm handing control back

**[10:38]** say, "Okay, I'm handing control back over to you." Um, and that's a lot more

**[10:40]** over to you." Um, and that's a lot more

**[10:40]** over to you." Um, and that's a lot more inter that feels a lot better and it and

**[10:42]** inter that feels a lot better and it and

**[10:42]** inter that feels a lot better and it and it felt like we had found the grain and

**[10:45]** it felt like we had found the grain and

**[10:45]** it felt like we had found the grain and found the right place to put this this

**[10:47]** found the right place to put this this

**[10:47]** found the right place to put this this material um with this. And so what's

**[10:50]** material um with this. And so what's

**[10:50]** material um with this. And so what's really cool about this one is that as

**[10:52]** really cool about this one is that as

**[10:52]** really cool about this one is that as we're implementing it, we've realized

**[10:54]** we're implementing it, we've realized

**[10:54]** we're implementing it, we've realized that it can um it can fit in other

**[10:56]** that it can um it can fit in other

**[10:56]** that it can um it can fit in other places. So uh not just in conversational

**[10:59]** places. So uh not just in conversational

**[10:59]** places. So uh not just in conversational flow, it can fit in line. Um and this is


### [11:00 - 12:00]

**[11:03]** flow, it can fit in line. Um and this is

**[11:03]** flow, it can fit in line. Um and this is going to be in our kind of like inline

**[11:04]** going to be in our kind of like inline

**[11:04]** going to be in our kind of like inline transform functionality um really soon.

**[11:09]** transform functionality um really soon.

**[11:09]** transform functionality um really soon. So I I think like as we as we find a new

**[11:12]** So I I think like as we as we find a new

**[11:12]** So I I think like as we as we find a new technology and work with it, we run the

**[11:14]** technology and work with it, we run the

**[11:14]** technology and work with it, we run the risk of just automating the tedious

**[11:16]** risk of just automating the tedious

**[11:16]** risk of just automating the tedious things. And I was so excited about those

**[11:18]** things. And I was so excited about those

**[11:18]** things. And I was so excited about those previous two talks because there's kind

**[11:20]** previous two talks because there's kind

**[11:20]** previous two talks because there's kind of like some emergence in there, right?

**[11:21]** of like some emergence in there, right?

**[11:21]** of like some emergence in there, right? Like something interesting that we

**[11:23]** Like something interesting that we

**[11:23]** Like something interesting that we weren't be able to do before. Um and I'm

**[11:26]** weren't be able to do before. Um and I'm

**[11:26]** weren't be able to do before. Um and I'm most excited about those thing like what

**[11:27]** most excited about those thing like what

**[11:27]** most excited about those thing like what what emerges from from playing. Um we

**[11:31]** what emerges from from playing. Um we

**[11:31]** what emerges from from playing. Um we stopped playing for a few years um when

**[11:34]** stopped playing for a few years um when

**[11:34]** stopped playing for a few years um when we were kind of got the internet and we

**[11:35]** we were kind of got the internet and we

**[11:35]** we were kind of got the internet and we were like really excited and CSS3 came

**[11:37]** were like really excited and CSS3 came

**[11:37]** were like really excited and CSS3 came out and then like HTML 5 we were playing

**[11:39]** out and then like HTML 5 we were playing

**[11:40]** out and then like HTML 5 we were playing a lot. Um now I feel like we all playing

**[11:42]** a lot. Um now I feel like we all playing

**[11:42]** a lot. Um now I feel like we all playing again and so that's really exciting for

**[11:44]** again and so that's really exciting for

**[11:44]** again and so that's really exciting for me. Um this is an example of me playing.

**[11:48]** me. Um this is an example of me playing.

**[11:48]** me. Um this is an example of me playing. Um I created this uh V0 and I I we've

**[11:52]** Um I created this uh V0 and I I we've

**[11:52]** Um I created this uh V0 and I I we've been in search of this characteristic of

**[11:55]** been in search of this characteristic of

**[11:55]** been in search of this characteristic of an agent that is that feels

**[11:56]** an agent that is that feels

**[11:56]** an agent that is that feels forwardleaning. And what I mean by that

**[11:58]** forwardleaning. And what I mean by that

**[11:58]** forwardleaning. And what I mean by that is it's an agent that's curious and it's


### [12:00 - 13:00]

**[12:01]** is it's an agent that's curious and it's

**[12:01]** is it's an agent that's curious and it's excitable, but it likes getting

**[12:03]** excitable, but it likes getting

**[12:03]** excitable, but it likes getting done. Um, and it's very focused. Um, so

**[12:06]** done. Um, and it's very focused. Um, so

**[12:06]** done. Um, and it's very focused. Um, so not going crazy, right? Like we've all

**[12:07]** not going crazy, right? Like we've all

**[12:07]** not going crazy, right? Like we've all seen the LMS kind of go too far when you

**[12:10]** seen the LMS kind of go too far when you

**[12:10]** seen the LMS kind of go too far when you give it a task and that doesn't feel

**[12:12]** give it a task and that doesn't feel

**[12:12]** give it a task and that doesn't feel good. Um, so here I dropped a JSON file

**[12:14]** good. Um, so here I dropped a JSON file

**[12:14]** good. Um, so here I dropped a JSON file and a CSV file. Um, and the agent

**[12:17]** and a CSV file. Um, and the agent

**[12:17]** and a CSV file. Um, and the agent decided, um, you know, it'll be good to

**[12:20]** decided, um, you know, it'll be good to

**[12:20]** decided, um, you know, it'll be good to do is combine those two things because

**[12:22]** do is combine those two things because

**[12:22]** do is combine those two things because the data look pretty similar. Um, and so

**[12:25]** the data look pretty similar. Um, and so

**[12:25]** the data look pretty similar. Um, and so here we can see it's it's combined the

**[12:27]** here we can see it's it's combined the

**[12:27]** here we can see it's it's combined the the file the two files into one. Um,

**[12:30]** the file the two files into one. Um,

**[12:30]** the file the two files into one. Um, that's a good thing that it did. I

**[12:31]** that's a good thing that it did. I

**[12:32]** that's a good thing that it did. I didn't have to ask it to do that. Um, it

**[12:33]** didn't have to ask it to do that. Um, it

**[12:34]** didn't have to ask it to do that. Um, it picked up on it. Um, and then after

**[12:36]** picked up on it. Um, and then after

**[12:36]** picked up on it. Um, and then after that, it wrote a a report. So, it told

**[12:39]** that, it wrote a a report. So, it told

**[12:39]** that, it wrote a a report. So, it told us what it was doing. Said, "Hey, I

**[12:40]** us what it was doing. Said, "Hey, I

**[12:40]** us what it was doing. Said, "Hey, I found some duplicates. This is probably

**[12:42]** found some duplicates. This is probably

**[12:42]** found some duplicates. This is probably what you need to do next." And so, it

**[12:44]** what you need to do next." And so, it

**[12:44]** what you need to do next." And so, it built up context. Um, and I was actually

**[12:47]** built up context. Um, and I was actually

**[12:47]** built up context. Um, and I was actually just trying to play with Claude 4 here

**[12:49]** just trying to play with Claude 4 here

**[12:49]** just trying to play with Claude 4 here and feel the material and kind of see

**[12:50]** and feel the material and kind of see

**[12:50]** and feel the material and kind of see how it would be. Um but I realized um

**[12:53]** how it would be. Um but I realized um

**[12:53]** how it would be. Um but I realized um I'd kind of come across this nature that

**[12:56]** I'd kind of come across this nature that

**[12:56]** I'd kind of come across this nature that we were after. Um it made some

**[12:59]** we were after. Um it made some

**[12:59]** we were after. Um it made some suggestions and generated a slide deck


### [13:00 - 14:00]

**[13:01]** suggestions and generated a slide deck

**[13:01]** suggestions and generated a slide deck which I I asked it for. Um so within

**[13:03]** which I I asked it for. Um so within

**[13:03]** which I I asked it for. Um so within just dropping two files um it's it's

**[13:06]** just dropping two files um it's it's

**[13:06]** just dropping two files um it's it's done something emergent. Um and now

**[13:09]** done something emergent. Um and now

**[13:09]** done something emergent. Um and now we're baking this into our our new

**[13:12]** we're baking this into our our new

**[13:12]** we're baking this into our our new product called obvious um which is

**[13:14]** product called obvious um which is

**[13:14]** product called obvious um which is coming soon. Another one was we had this

**[13:17]** coming soon. Another one was we had this

**[13:17]** coming soon. Another one was we had this idea of giving our agents a knowledge

**[13:19]** idea of giving our agents a knowledge

**[13:19]** idea of giving our agents a knowledge base. So all the customer calls we'd had

**[13:21]** base. So all the customer calls we'd had

**[13:21]** base. So all the customer calls we'd had with them were all recorded and

**[13:22]** with them were all recorded and

**[13:22]** with them were all recorded and transcribed like most of ours are. Um

**[13:25]** transcribed like most of ours are. Um

**[13:25]** transcribed like most of ours are. Um and we had documentation from the

**[13:26]** and we had documentation from the

**[13:26]** and we had documentation from the customer and so we put it in to

**[13:29]** customer and so we put it in to

**[13:29]** customer and so we put it in to knowledge base and then when we analyzed

**[13:31]** knowledge base and then when we analyzed

**[13:31]** knowledge base and then when we analyzed all of this customer data, we surfaced

**[13:33]** all of this customer data, we surfaced

**[13:33]** all of this customer data, we surfaced up um suggestions based off that. I was

**[13:35]** up um suggestions based off that. I was

**[13:35]** up um suggestions based off that. I was fully expecting better suggestions. I

**[13:38]** fully expecting better suggestions. I

**[13:38]** fully expecting better suggestions. I was fully expecting more suggestions got

**[13:40]** was fully expecting more suggestions got

**[13:40]** was fully expecting more suggestions got those. But then here um the the agent

**[13:43]** those. But then here um the the agent

**[13:44]** those. But then here um the the agent decided I can't fix this but I know how

**[13:46]** decided I can't fix this but I know how

**[13:46]** decided I can't fix this but I know how to fix it and so I'm going to tell you

**[13:48]** to fix it and so I'm going to tell you

**[13:48]** to fix it and so I'm going to tell you how to fix it. And so it suggests here

**[13:50]** how to fix it. And so it suggests here

**[13:50]** how to fix it. And so it suggests here that the user actually goes to HR and

**[13:52]** that the user actually goes to HR and

**[13:52]** that the user actually goes to HR and gets them to generate the missing

**[13:54]** gets them to generate the missing

**[13:54]** gets them to generate the missing employee IDs. And what emerged here was

**[13:56]** employee IDs. And what emerged here was

**[13:56]** employee IDs. And what emerged here was something I wasn't expecting. Maybe you

**[13:58]** something I wasn't expecting. Maybe you

**[13:58]** something I wasn't expecting. Maybe you look at this and say that makes a lot of


### [14:00 - 15:00]

**[14:00]** look at this and say that makes a lot of

**[14:00]** look at this and say that makes a lot of obvious sense, but to me I wasn't

**[14:01]** obvious sense, but to me I wasn't

**[14:02]** obvious sense, but to me I wasn't expecting it to be able to help the

**[14:03]** expecting it to be able to help the

**[14:03]** expecting it to be able to help the human to go and do the job um where it

**[14:05]** human to go and do the job um where it

**[14:06]** human to go and do the job um where it couldn't. Um so that was really

**[14:07]** couldn't. Um so that was really

**[14:07]** couldn't. Um so that was really exciting. I don't think I would have be

**[14:08]** exciting. I don't think I would have be

**[14:08]** exciting. I don't think I would have be able to get to that without um playing

**[14:11]** able to get to that without um playing

**[14:12]** able to get to that without um playing and and being curious. Um,

**[14:15]** and and being curious. Um,

**[14:15]** and and being curious. Um, and then the last thing I I want to talk

**[14:17]** and then the last thing I I want to talk

**[14:17]** and then the last thing I I want to talk a little bit about is eyes on the

**[14:18]** a little bit about is eyes on the

**[14:18]** a little bit about is eyes on the future. And we all have our eyes on the

**[14:20]** future. And we all have our eyes on the

**[14:20]** future. And we all have our eyes on the future because how can you not? There's

**[14:22]** future because how can you not? There's

**[14:22]** future because how can you not? There's always something new now um with models.

**[14:25]** always something new now um with models.

**[14:25]** always something new now um with models. Um, so I I like to think about it as

**[14:29]** Um, so I I like to think about it as

**[14:29]** Um, so I I like to think about it as like what's your pelican on a bicycle?

**[14:31]** like what's your pelican on a bicycle?

**[14:32]** like what's your pelican on a bicycle? Um, and one of my pelican on a bicycles

**[14:34]** Um, and one of my pelican on a bicycles

**[14:34]** Um, and one of my pelican on a bicycles is autocomplete. I'm super excited

**[14:36]** is autocomplete. I'm super excited

**[14:36]** is autocomplete. I'm super excited about. It's probably a bad idea um

**[14:37]** about. It's probably a bad idea um

**[14:38]** about. It's probably a bad idea um actually to use an LLM for this, but I'm

**[14:39]** actually to use an LLM for this, but I'm

**[14:39]** actually to use an LLM for this, but I'm like I want to make an autocomplete that

**[14:42]** like I want to make an autocomplete that

**[14:42]** like I want to make an autocomplete that um is backed by an LLM. And so this one

**[14:44]** um is backed by an LLM. And so this one

**[14:44]** um is backed by an LLM. And so this one has 100 suggestions for fixing some

**[14:46]** has 100 suggestions for fixing some

**[14:46]** has 100 suggestions for fixing some data. Um and it's kind of like a bake

**[14:48]** data. Um and it's kind of like a bake

**[14:48]** data. Um and it's kind of like a bake off um between these two things. I'm yet

**[14:51]** off um between these two things. I'm yet

**[14:51]** off um between these two things. I'm yet to find um a model that is both very

**[14:54]** to find um a model that is both very

**[14:54]** to find um a model that is both very fast and very good at this problem. Um

**[14:57]** fast and very good at this problem. Um

**[14:57]** fast and very good at this problem. Um but this is a a a benchmark or something

**[14:59]** but this is a a a benchmark or something

**[14:59]** but this is a a a benchmark or something that I've created just for myself to be


### [15:00 - 16:00]

**[15:01]** that I've created just for myself to be

**[15:01]** that I've created just for myself to be able to feel the materials um that we're

**[15:03]** able to feel the materials um that we're

**[15:03]** able to feel the materials um that we're getting. And so I think about that for

**[15:06]** getting. And so I think about that for

**[15:06]** getting. And so I think about that for my design practice now, like what are

**[15:08]** my design practice now, like what are

**[15:08]** my design practice now, like what are the things I care about and can I like

**[15:10]** the things I care about and can I like

**[15:10]** the things I care about and can I like design into the future and start to

**[15:12]** design into the future and start to

**[15:12]** design into the future and start to think about the form factors I want and

**[15:14]** think about the form factors I want and

**[15:14]** think about the form factors I want and then build an application that can

**[15:16]** then build an application that can

**[15:16]** then build an application that can actually test that. So yeah, that's uh

**[15:19]** actually test that. So yeah, that's uh

**[15:19]** actually test that. So yeah, that's uh all I have for you today. I I'm very

**[15:21]** all I have for you today. I I'm very

**[15:21]** all I have for you today. I I'm very excited to see all the new form factors

**[15:23]** excited to see all the new form factors

**[15:23]** excited to see all the new form factors um that we build um with our new tools.

**[15:26]** um that we build um with our new tools.

**[15:26]** um that we build um with our new tools. Thank you.

**[15:28]** Thank you.

**[15:28]** Thank you. [Applause]

**[15:30]** [Applause]

**[15:30]** [Applause] [Music]


