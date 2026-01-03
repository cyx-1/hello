# Why you should care about AI interpretability - Mark Bissell, Goodfire AI

**Video URL:** https://www.youtube.com/watch?v=6AVMHZPjpTQ

---

## Full Transcript

### [00:00 - 01:00]

**[00:16]** Thanks everyone for coming. Uh my name

**[00:16]** Thanks everyone for coming. Uh my name is Mark Bissell. Uh I'm a member of the

**[00:19]** is Mark Bissell. Uh I'm a member of the

**[00:19]** is Mark Bissell. Uh I'm a member of the technical staff at Goodfire and Goodfire

**[00:23]** technical staff at Goodfire and Goodfire

**[00:23]** technical staff at Goodfire and Goodfire works on mechanistic interpretability.

**[00:26]** works on mechanistic interpretability.

**[00:26]** works on mechanistic interpretability. Um, I'm here to explain a little bit

**[00:28]** Um, I'm here to explain a little bit

**[00:28]** Um, I'm here to explain a little bit more about what that means in practice,

**[00:30]** more about what that means in practice,

**[00:30]** more about what that means in practice, whether you've heard the term before or

**[00:31]** whether you've heard the term before or

**[00:31]** whether you've heard the term before or not.

**[00:33]** not.

**[00:33]** not. So, you might have started hearing the

**[00:36]** So, you might have started hearing the

**[00:36]** So, you might have started hearing the uh word interpretability come up a bit

**[00:38]** uh word interpretability come up a bit

**[00:38]** uh word interpretability come up a bit more uh recently. It's a big focus at a

**[00:42]** more uh recently. It's a big focus at a

**[00:42]** more uh recently. It's a big focus at a lot of the major labs. Um, Daario from

**[00:44]** lot of the major labs. Um, Daario from

**[00:44]** lot of the major labs. Um, Daario from Anthropic recently wrote a popular piece

**[00:47]** Anthropic recently wrote a popular piece

**[00:47]** Anthropic recently wrote a popular piece called the urgency of interpretability.

**[00:49]** called the urgency of interpretability.

**[00:49]** called the urgency of interpretability. Um and then there's plenty of papers and

**[00:52]** Um and then there's plenty of papers and

**[00:52]** Um and then there's plenty of papers and posts and podcasts all talking about uh

**[00:55]** posts and podcasts all talking about uh

**[00:56]** posts and podcasts all talking about uh all talking about the concept in this uh

**[00:58]** all talking about the concept in this uh

**[00:58]** all talking about the concept in this uh field of research.


### [01:00 - 02:00]

**[01:00]** field of research.

**[01:00]** field of research. So what is interpretability? Um also

**[01:02]** So what is interpretability? Um also

**[01:02]** So what is interpretability? Um also called mechanistic interpretability. Uh

**[01:06]** called mechanistic interpretability. Uh

**[01:06]** called mechanistic interpretability. Uh it is really all about reverse

**[01:09]** it is really all about reverse

**[01:09]** it is really all about reverse engineering neural networks to

**[01:11]** engineering neural networks to

**[01:11]** engineering neural networks to understand what is going on uh inside of

**[01:14]** understand what is going on uh inside of

**[01:14]** understand what is going on uh inside of them. And so uh it's a uh these

**[01:18]** them. And so uh it's a uh these

**[01:18]** them. And so uh it's a uh these techniques are often talked about using

**[01:20]** techniques are often talked about using

**[01:20]** techniques are often talked about using analogies like opening the black box and

**[01:23]** analogies like opening the black box and

**[01:23]** analogies like opening the black box and doing brain scans of models or uh doing

**[01:26]** doing brain scans of models or uh doing

**[01:26]** doing brain scans of models or uh doing brain surgery on models. And one popular

**[01:29]** brain surgery on models. And one popular

**[01:29]** brain surgery on models. And one popular example of this was the Golden Gate

**[01:32]** example of this was the Golden Gate

**[01:32]** example of this was the Golden Gate Claude demo from the anthropic team that

**[01:34]** Claude demo from the anthropic team that

**[01:34]** Claude demo from the anthropic team that you might have seen. Uh and so what the

**[01:36]** you might have seen. Uh and so what the

**[01:36]** you might have seen. Uh and so what the team found was they looked inside Claude

**[01:39]** team found was they looked inside Claude

**[01:39]** team found was they looked inside Claude uh and they were able to find a set of

**[01:41]** uh and they were able to find a set of

**[01:41]** uh and they were able to find a set of neurons inside the model that

**[01:43]** neurons inside the model that

**[01:44]** neurons inside the model that represented Claude's concept of the

**[01:46]** represented Claude's concept of the

**[01:46]** represented Claude's concept of the Golden Gate Bridge. And so normally this

**[01:49]** Golden Gate Bridge. And so normally this

**[01:49]** Golden Gate Bridge. And so normally this feature would be active when you're

**[01:51]** feature would be active when you're

**[01:51]** feature would be active when you're talking to Claude about the bridge or

**[01:52]** talking to Claude about the bridge or

**[01:52]** talking to Claude about the bridge or about San Francisco. But you can

**[01:56]** about San Francisco. But you can

**[01:56]** about San Francisco. But you can actually create a version of claude

**[01:57]** actually create a version of claude

**[01:58]** actually create a version of claude where you take a look at those neurons

**[01:59]** where you take a look at those neurons


### [02:00 - 03:00]

**[02:00]** where you take a look at those neurons and you cause them to always be turned

**[02:02]** and you cause them to always be turned

**[02:02]** and you cause them to always be turned on and always be lighting up no matter

**[02:04]** on and always be lighting up no matter

**[02:04]** on and always be lighting up no matter what you're talking to it about. And in

**[02:06]** what you're talking to it about. And in

**[02:06]** what you're talking to it about. And in that case, suddenly uh this new version

**[02:08]** that case, suddenly uh this new version

**[02:08]** that case, suddenly uh this new version of Claude, Golden Gate Claude is

**[02:10]** of Claude, Golden Gate Claude is

**[02:10]** of Claude, Golden Gate Claude is obsessed with the bridge and will bring

**[02:11]** obsessed with the bridge and will bring

**[02:11]** obsessed with the bridge and will bring it up no matter what you're talking

**[02:13]** it up no matter what you're talking

**[02:13]** it up no matter what you're talking about. And so this is one example of

**[02:15]** about. And so this is one example of

**[02:15]** about. And so this is one example of what it means to be reverse engineering

**[02:17]** what it means to be reverse engineering

**[02:17]** what it means to be reverse engineering the network and actually using that

**[02:19]** the network and actually using that

**[02:19]** the network and actually using that knowledge to uh change the the behavior

**[02:21]** knowledge to uh change the the behavior

**[02:21]** knowledge to uh change the the behavior of a model.

**[02:23]** of a model.

**[02:23]** of a model. And so interpretability is a field

**[02:25]** And so interpretability is a field

**[02:26]** And so interpretability is a field that's been interesting for researchers

**[02:28]** that's been interesting for researchers

**[02:28]** that's been interesting for researchers uh for a number of years now. It's

**[02:30]** uh for a number of years now. It's

**[02:30]** uh for a number of years now. It's produced a lot of cool demos like Golden

**[02:32]** produced a lot of cool demos like Golden

**[02:32]** produced a lot of cool demos like Golden Gate Claude. But really over the past

**[02:34]** Gate Claude. But really over the past

**[02:34]** Gate Claude. But really over the past year we've started to see it move from

**[02:37]** year we've started to see it move from

**[02:37]** year we've started to see it move from the lab and into real world use cases

**[02:41]** the lab and into real world use cases

**[02:41]** the lab and into real world use cases where it can provide differential

**[02:43]** where it can provide differential

**[02:43]** where it can provide differential practical value. Uh and so I'm going to

**[02:45]** practical value. Uh and so I'm going to

**[02:46]** practical value. Uh and so I'm going to be talking about a few of those

**[02:47]** be talking about a few of those

**[02:47]** be talking about a few of those examples. And this move from the lab to

**[02:49]** examples. And this move from the lab to

**[02:49]** examples. And this move from the lab to the real world is why I think now is the

**[02:52]** the real world is why I think now is the

**[02:52]** the real world is why I think now is the right time for AI engineers in

**[02:54]** right time for AI engineers in

**[02:54]** right time for AI engineers in particular uh to really start caring

**[02:56]** particular uh to really start caring

**[02:56]** particular uh to really start caring about interpretability um and start

**[02:58]** about interpretability um and start

**[02:58]** about interpretability um and start paying attention to the field. And so


### [03:00 - 04:00]

**[03:01]** paying attention to the field. And so

**[03:01]** paying attention to the field. And so I'm going to talk about three sort of

**[03:02]** I'm going to talk about three sort of

**[03:02]** I'm going to talk about three sort of broad categories for where

**[03:04]** broad categories for where

**[03:04]** broad categories for where interpretability might impact how you

**[03:06]** interpretability might impact how you

**[03:06]** interpretability might impact how you work with AI. Um, for developers working

**[03:09]** work with AI. Um, for developers working

**[03:09]** work with AI. Um, for developers working with models, uh, interpretability

**[03:11]** with models, uh, interpretability

**[03:11]** with models, uh, interpretability techniques provide a set of sort of like

**[03:14]** techniques provide a set of sort of like

**[03:14]** techniques provide a set of sort of like power user tools for working with these

**[03:16]** power user tools for working with these

**[03:16]** power user tools for working with these models in ways that you might not be

**[03:17]** models in ways that you might not be

**[03:18]** models in ways that you might not be familiar with. Um, and actually being

**[03:20]** familiar with. Um, and actually being

**[03:20]** familiar with. Um, and actually being able to debug them in new ways and

**[03:22]** able to debug them in new ways and

**[03:22]** able to debug them in new ways and actually like program at the neuron

**[03:25]** actually like program at the neuron

**[03:25]** actually like program at the neuron level. Um, which is something that that

**[03:27]** level. Um, which is something that that

**[03:27]** level. Um, which is something that that we're going to see in a sec here.

**[03:29]** we're going to see in a sec here.

**[03:29]** we're going to see in a sec here. Secondly, from a UIUX perspective, uh

**[03:32]** Secondly, from a UIUX perspective, uh

**[03:32]** Secondly, from a UIUX perspective, uh being able to plug into the internals of

**[03:35]** being able to plug into the internals of

**[03:35]** being able to plug into the internals of models creates completely new ways of

**[03:38]** models creates completely new ways of

**[03:38]** models creates completely new ways of interacting with models. And I'm going

**[03:39]** interacting with models. And I'm going

**[03:39]** interacting with models. And I'm going to show a demo of that using um a

**[03:42]** to show a demo of that using um a

**[03:42]** to show a demo of that using um a generative uh image model example. And

**[03:45]** generative uh image model example. And

**[03:45]** generative uh image model example. And then there's a long tale of other use

**[03:47]** then there's a long tale of other use

**[03:47]** then there's a long tale of other use cases for interpretability uh that that

**[03:49]** cases for interpretability uh that that

**[03:49]** cases for interpretability uh that that we at Goodfire are super excited about

**[03:52]** we at Goodfire are super excited about

**[03:52]** we at Goodfire are super excited about um including uh advancing frontier

**[03:54]** um including uh advancing frontier

**[03:54]** um including uh advancing frontier science by taking these superhuman

**[03:57]** science by taking these superhuman

**[03:57]** science by taking these superhuman models across domains like biology and

**[03:59]** models across domains like biology and

**[03:59]** models across domains like biology and genomics and actually figuring out what


### [04:00 - 05:00]

**[04:01]** genomics and actually figuring out what

**[04:01]** genomics and actually figuring out what they've learned that we don't know about

**[04:02]** they've learned that we don't know about

**[04:02]** they've learned that we don't know about those fields.

**[04:08]** So uh first let's talk about developing

**[04:08]** So uh first let's talk about developing with AI systems. Um, so before joining

**[04:11]** with AI systems. Um, so before joining

**[04:11]** with AI systems. Um, so before joining GoodFire, I spent three years working on

**[04:13]** GoodFire, I spent three years working on

**[04:13]** GoodFire, I spent three years working on Palunteer's uh, healthcare team. And so,

**[04:16]** Palunteer's uh, healthcare team. And so,

**[04:16]** Palunteer's uh, healthcare team. And so, um, I'm familiar with how you need

**[04:18]** um, I'm familiar with how you need

**[04:18]** um, I'm familiar with how you need systems to be really reliable and robust

**[04:20]** systems to be really reliable and robust

**[04:20]** systems to be really reliable and robust and accurate before you're deploying to

**[04:22]** and accurate before you're deploying to

**[04:22]** and accurate before you're deploying to prod in mission critical contexts, but

**[04:25]** prod in mission critical contexts, but

**[04:25]** prod in mission critical contexts, but also how LLMs can make that especially

**[04:28]** also how LLMs can make that especially

**[04:28]** also how LLMs can make that especially challenging. Um, you know, just given

**[04:30]** challenging. Um, you know, just given

**[04:30]** challenging. Um, you know, just given how non-deterministic they are and sort

**[04:32]** how non-deterministic they are and sort

**[04:32]** how non-deterministic they are and sort of the lack of being able to make

**[04:33]** of the lack of being able to make

**[04:33]** of the lack of being able to make precise guarantees about their behavior.

**[04:35]** precise guarantees about their behavior.

**[04:35]** precise guarantees about their behavior. And so I'm sure that an anecdote like

**[04:37]** And so I'm sure that an anecdote like

**[04:38]** And so I'm sure that an anecdote like this is probably familiar to a lot of

**[04:39]** this is probably familiar to a lot of

**[04:39]** this is probably familiar to a lot of you. You're building an agent uh or an

**[04:42]** you. You're building an agent uh or an

**[04:42]** you. You're building an agent uh or an LLM pipeline and uh you want it to

**[04:45]** LLM pipeline and uh you want it to

**[04:45]** LLM pipeline and uh you want it to follow some set of instructions. So you

**[04:47]** follow some set of instructions. So you

**[04:47]** follow some set of instructions. So you run it against your eval suite and maybe

**[04:49]** run it against your eval suite and maybe

**[04:49]** run it against your eval suite and maybe it's uh ignoring one of those

**[04:51]** it's uh ignoring one of those

**[04:51]** it's uh ignoring one of those instructions or it's failing in some

**[04:52]** instructions or it's failing in some

**[04:52]** instructions or it's failing in some way. And so what do you do? You update

**[04:54]** way. And so what do you do? You update

**[04:54]** way. And so what do you do? You update the system prompt to try to fix the

**[04:56]** the system prompt to try to fix the

**[04:56]** the system prompt to try to fix the thing that it's ignoring. But you end up

**[04:58]** thing that it's ignoring. But you end up

**[04:58]** thing that it's ignoring. But you end up in this place with sort of these


### [05:00 - 06:00]

**[05:00]** in this place with sort of these

**[05:00]** in this place with sort of these whack-a-ole prompt edits. fix one thing

**[05:02]** whack-a-ole prompt edits. fix one thing

**[05:02]** whack-a-ole prompt edits. fix one thing and then you rerun your eval suite and

**[05:04]** and then you rerun your eval suite and

**[05:04]** and then you rerun your eval suite and suddenly that change in the prompt has

**[05:06]** suddenly that change in the prompt has

**[05:06]** suddenly that change in the prompt has inexplicably caused a different thing to

**[05:08]** inexplicably caused a different thing to

**[05:08]** inexplicably caused a different thing to break and you just keep going through

**[05:09]** break and you just keep going through

**[05:10]** break and you just keep going through this loop of trying to fix one thing but

**[05:11]** this loop of trying to fix one thing but

**[05:11]** this loop of trying to fix one thing but you get these offtarget effects.

**[05:14]** you get these offtarget effects.

**[05:14]** you get these offtarget effects. So then you might consider oh maybe I'll

**[05:16]** So then you might consider oh maybe I'll

**[05:16]** So then you might consider oh maybe I'll introduce an LLM as a judge and you know

**[05:19]** introduce an LLM as a judge and you know

**[05:19]** introduce an LLM as a judge and you know take a look at the output from the first

**[05:20]** take a look at the output from the first

**[05:20]** take a look at the output from the first LLM make sure it adheres to um all the

**[05:22]** LLM make sure it adheres to um all the

**[05:22]** LLM make sure it adheres to um all the different uh instructions that I want it

**[05:24]** different uh instructions that I want it

**[05:24]** different uh instructions that I want it to follow. The problem here is that this

**[05:27]** to follow. The problem here is that this

**[05:27]** to follow. The problem here is that this isn't so scalable. you know, the first

**[05:29]** isn't so scalable. you know, the first

**[05:29]** isn't so scalable. you know, the first time you get the OpenAI or Anthropic

**[05:31]** time you get the OpenAI or Anthropic

**[05:31]** time you get the OpenAI or Anthropic bill using your LM as a judge, maybe

**[05:32]** bill using your LM as a judge, maybe

**[05:32]** bill using your LM as a judge, maybe you're like, I don't know if this is the

**[05:34]** you're like, I don't know if this is the

**[05:34]** you're like, I don't know if this is the approach I'm going to be able to to go

**[05:35]** approach I'm going to be able to to go

**[05:35]** approach I'm going to be able to to go with long term. Um, and you've got

**[05:37]** with long term. Um, and you've got

**[05:37]** with long term. Um, and you've got another system to monitor uh and upgrade

**[05:39]** another system to monitor uh and upgrade

**[05:39]** another system to monitor uh and upgrade and and make sure it's performing well.

**[05:43]** and and make sure it's performing well.

**[05:43]** and and make sure it's performing well. And then maybe you'll consider

**[05:44]** And then maybe you'll consider

**[05:44]** And then maybe you'll consider fine-tuning um in order to to make sure

**[05:46]** fine-tuning um in order to to make sure

**[05:46]** fine-tuning um in order to to make sure that your models are are following all

**[05:48]** that your models are are following all

**[05:48]** that your models are are following all the instructions. Um the problem here is

**[05:49]** the instructions. Um the problem here is

**[05:50]** the instructions. Um the problem here is that you need domain specific data which

**[05:52]** that you need domain specific data which

**[05:52]** that you need domain specific data which can be often uh tough to curate and then

**[05:54]** can be often uh tough to curate and then

**[05:54]** can be often uh tough to curate and then even when you do um you know supervised

**[05:57]** even when you do um you know supervised

**[05:57]** even when you do um you know supervised fine-tuning or reinforcement fine-tuning

**[05:59]** fine-tuning or reinforcement fine-tuning

**[05:59]** fine-tuning or reinforcement fine-tuning the models don't always learn exactly


### [06:00 - 07:00]

**[06:00]** the models don't always learn exactly

**[06:00]** the models don't always learn exactly what you want them to learn. Um so they

**[06:03]** what you want them to learn. Um so they

**[06:03]** what you want them to learn. Um so they might pick up on uh spurious

**[06:04]** might pick up on uh spurious

**[06:04]** might pick up on uh spurious correlations in the data. you might um

**[06:07]** correlations in the data. you might um

**[06:07]** correlations in the data. you might um see mode collapse where they start

**[06:08]** see mode collapse where they start

**[06:08]** see mode collapse where they start outputting uh some type of common output

**[06:11]** outputting uh some type of common output

**[06:11]** outputting uh some type of common output um again and again or you get reward

**[06:13]** um again and again or you get reward

**[06:13]** um again and again or you get reward hacking um and you know you wanted your

**[06:15]** hacking um and you know you wanted your

**[06:15]** hacking um and you know you wanted your model to start following instructions

**[06:17]** model to start following instructions

**[06:17]** model to start following instructions but as this example shows all of a

**[06:19]** but as this example shows all of a

**[06:19]** but as this example shows all of a sudden it's saying horrible malicious

**[06:20]** sudden it's saying horrible malicious

**[06:20]** sudden it's saying horrible malicious things uh because of these weird

**[06:22]** things uh because of these weird

**[06:22]** things uh because of these weird offtarget effects and you're not really

**[06:23]** offtarget effects and you're not really

**[06:23]** offtarget effects and you're not really sure why.

**[06:26]** sure why.

**[06:26]** sure why. So uh where does interpretability come

**[06:28]** So uh where does interpretability come

**[06:28]** So uh where does interpretability come in? Um

**[06:30]** in? Um

**[06:30]** in? Um well actually going back to this for one

**[06:32]** well actually going back to this for one

**[06:32]** well actually going back to this for one sec. So the common thread here is that

**[06:33]** sec. So the common thread here is that

**[06:33]** sec. So the common thread here is that working with AI is is super powerful

**[06:35]** working with AI is is super powerful

**[06:35]** working with AI is is super powerful here, but there's sort of this lack of

**[06:37]** here, but there's sort of this lack of

**[06:37]** here, but there's sort of this lack of rigor that we've come to expect with

**[06:38]** rigor that we've come to expect with

**[06:38]** rigor that we've come to expect with traditional uh software development.

**[06:40]** traditional uh software development.

**[06:40]** traditional uh software development. You're jumping through all these hoops

**[06:42]** You're jumping through all these hoops

**[06:42]** You're jumping through all these hoops and um that's just not something that

**[06:44]** and um that's just not something that

**[06:44]** and um that's just not something that you would expect with with quote unquote

**[06:46]** you would expect with with quote unquote

**[06:46]** you would expect with with quote unquote normal software. Uh and so that's where

**[06:49]** normal software. Uh and so that's where

**[06:49]** normal software. Uh and so that's where um uh at Goodfire we're building a

**[06:51]** um uh at Goodfire we're building a

**[06:51]** um uh at Goodfire we're building a platform called Ember, which uh is based

**[06:55]** platform called Ember, which uh is based

**[06:55]** platform called Ember, which uh is based in interpretability techniques. And the

**[06:57]** in interpretability techniques. And the

**[06:57]** in interpretability techniques. And the idea here is what if you could uh debug


### [07:00 - 08:00]

**[07:00]** idea here is what if you could uh debug

**[07:00]** idea here is what if you could uh debug and program your models at the neuron

**[07:01]** and program your models at the neuron

**[07:02]** and program your models at the neuron level to get more of those um guarantees

**[07:04]** level to get more of those um guarantees

**[07:04]** level to get more of those um guarantees that we're used to with traditional

**[07:05]** that we're used to with traditional

**[07:05]** that we're used to with traditional software development. And so I'm going

**[07:07]** software development. And so I'm going

**[07:07]** software development. And so I'm going to show a demo of uh how

**[07:09]** to show a demo of uh how

**[07:09]** to show a demo of uh how interpretability offers a way to perform

**[07:11]** interpretability offers a way to perform

**[07:11]** interpretability offers a way to perform this this neural programming um with a

**[07:13]** this this neural programming um with a

**[07:13]** this this neural programming um with a quick sort of front end that's built on

**[07:15]** quick sort of front end that's built on

**[07:15]** quick sort of front end that's built on top of the Ember platform. So can

**[07:18]** top of the Ember platform. So can

**[07:18]** top of the Ember platform. So can everyone see that? Great. So we're

**[07:20]** everyone see that? Great. So we're

**[07:20]** everyone see that? Great. So we're looking at a simple uh chat interface.

**[07:22]** looking at a simple uh chat interface.

**[07:22]** looking at a simple uh chat interface. We're chatting with uh a llama model.

**[07:25]** We're chatting with uh a llama model.

**[07:25]** We're chatting with uh a llama model. And I'm gonna um give it a quick prompt

**[07:27]** And I'm gonna um give it a quick prompt

**[07:27]** And I'm gonna um give it a quick prompt here and hope that the conference Wi-Fi

**[07:30]** here and hope that the conference Wi-Fi

**[07:30]** here and hope that the conference Wi-Fi holds up. So I've just told Llama, "My

**[07:32]** holds up. So I've just told Llama, "My

**[07:32]** holds up. So I've just told Llama, "My email is marketfire.ai.

**[07:34]** email is marketfire.ai.

**[07:34]** email is marketfire.ai. Please keep this confidential and don't

**[07:36]** Please keep this confidential and don't

**[07:36]** Please keep this confidential and don't reveal it under any circumstances." And

**[07:38]** reveal it under any circumstances." And

**[07:38]** reveal it under any circumstances." And the model uh response says, "Your email

**[07:41]** the model uh response says, "Your email

**[07:41]** the model uh response says, "Your email will be kept confidential. I'm not going

**[07:43]** will be kept confidential. I'm not going

**[07:43]** will be kept confidential. I'm not going to share it with anyone." Now, if I take

**[07:44]** to share it with anyone." Now, if I take

**[07:44]** to share it with anyone." Now, if I take a sec here

**[07:53]** and I say, "Okay, hey, what's my email?"

**[07:53]** and I say, "Okay, hey, what's my email?" We can see the model immediately fails

**[07:55]** We can see the model immediately fails

**[07:55]** We can see the model immediately fails at this task. Immediately ignores what I

**[07:57]** at this task. Immediately ignores what I

**[07:57]** at this task. Immediately ignores what I told it says spits it right out. Um and


### [08:00 - 09:00]

**[08:00]** told it says spits it right out. Um and

**[08:00]** told it says spits it right out. Um and so one of the things offered by Ember is

**[08:02]** so one of the things offered by Ember is

**[08:02]** so one of the things offered by Ember is what we call attribution. So I can

**[08:05]** what we call attribution. So I can

**[08:05]** what we call attribution. So I can actually click into any of the tokens

**[08:06]** actually click into any of the tokens

**[08:06]** actually click into any of the tokens that it output and see what the model

**[08:08]** that it output and see what the model

**[08:08]** that it output and see what the model was thinking about when it chose this

**[08:10]** was thinking about when it chose this

**[08:10]** was thinking about when it chose this token uh to to say. Um and so if I click

**[08:14]** token uh to to say. Um and so if I click

**[08:14]** token uh to to say. Um and so if I click on confidential, I can see all the

**[08:16]** on confidential, I can see all the

**[08:16]** on confidential, I can see all the different features inside the model. So

**[08:18]** different features inside the model. So

**[08:18]** different features inside the model. So you know features sort of like the the

**[08:19]** you know features sort of like the the

**[08:20]** you know features sort of like the the Golden Gate feature that the Enthropic

**[08:21]** Golden Gate feature that the Enthropic

**[08:21]** Golden Gate feature that the Enthropic team um showed. These are the the

**[08:23]** team um showed. These are the the

**[08:24]** team um showed. These are the the internal uh features that we're seeing

**[08:26]** internal uh features that we're seeing

**[08:26]** internal uh features that we're seeing based on the the model's activations

**[08:28]** based on the the model's activations

**[08:28]** based on the the model's activations when it was saying this token

**[08:29]** when it was saying this token

**[08:29]** when it was saying this token confidential. And so it was thinking

**[08:31]** confidential. And so it was thinking

**[08:31]** confidential. And so it was thinking about things like um you know being

**[08:34]** about things like um you know being

**[08:34]** about things like um you know being professional and uh taking matters

**[08:37]** professional and uh taking matters

**[08:37]** professional and uh taking matters seriously and importantly we can see one

**[08:39]** seriously and importantly we can see one

**[08:39]** seriously and importantly we can see one here that's discussions of sensitive and

**[08:41]** here that's discussions of sensitive and

**[08:41]** here that's discussions of sensitive and protected information. So not only can I

**[08:44]** protected information. So not only can I

**[08:44]** protected information. So not only can I see what the model is thinking I can now

**[08:46]** see what the model is thinking I can now

**[08:46]** see what the model is thinking I can now actively steer it and guide it. So if I

**[08:48]** actively steer it and guide it. So if I

**[08:48]** actively steer it and guide it. So if I take this feature and I say I want to

**[08:50]** take this feature and I say I want to

**[08:50]** take this feature and I say I want to turn that up from its normal level to

**[08:53]** turn that up from its normal level to

**[08:53]** turn that up from its normal level to you know call it 60% more suddenly the

**[08:56]** you know call it 60% more suddenly the

**[08:56]** you know call it 60% more suddenly the model takes PII and sensitive

**[08:59]** model takes PII and sensitive

**[08:59]** model takes PII and sensitive information much more seriously. We can


### [09:00 - 10:00]

**[09:01]** information much more seriously. We can

**[09:01]** information much more seriously. We can see a new output having turned this

**[09:03]** see a new output having turned this

**[09:03]** see a new output having turned this feature up. It says I can't share share

**[09:05]** feature up. It says I can't share share

**[09:05]** feature up. It says I can't share share your email uh you know I'm going to keep

**[09:07]** your email uh you know I'm going to keep

**[09:07]** your email uh you know I'm going to keep it secure. And so this is just one

**[09:09]** it secure. And so this is just one

**[09:09]** it secure. And so this is just one example of what you get when you're able

**[09:10]** example of what you get when you're able

**[09:10]** example of what you get when you're able to both uh peek inside the model's

**[09:12]** to both uh peek inside the model's

**[09:12]** to both uh peek inside the model's thoughts and then use that to actually

**[09:14]** thoughts and then use that to actually

**[09:14]** thoughts and then use that to actually steer and guide its behavior uh in the

**[09:16]** steer and guide its behavior uh in the

**[09:16]** steer and guide its behavior uh in the way that you would like.

**[09:30]** So um that's just one of the many ways

**[09:30]** So um that's just one of the many ways that uh interpretability techniques

**[09:32]** that uh interpretability techniques

**[09:32]** that uh interpretability techniques offer ways to sort of engineer your

**[09:34]** offer ways to sort of engineer your

**[09:34]** offer ways to sort of engineer your models with this type of neural

**[09:35]** models with this type of neural

**[09:35]** models with this type of neural programming. Um, we have a bunch of

**[09:37]** programming. Um, we have a bunch of

**[09:37]** programming. Um, we have a bunch of other examples in our developer docs

**[09:39]** other examples in our developer docs

**[09:39]** other examples in our developer docs that that show other things that you can

**[09:40]** that that show other things that you can

**[09:40]** that that show other things that you can get with this type of neural programming

**[09:42]** get with this type of neural programming

**[09:42]** get with this type of neural programming from uh making the models more uh

**[09:44]** from uh making the models more uh

**[09:44]** from uh making the models more uh jailbreak resistant to um uh

**[09:47]** jailbreak resistant to um uh

**[09:47]** jailbreak resistant to um uh conditionally looking up information

**[09:49]** conditionally looking up information

**[09:49]** conditionally looking up information based on the features that you're seeing

**[09:50]** based on the features that you're seeing

**[09:50]** based on the features that you're seeing are active. For one more sort of um

**[09:53]** are active. For one more sort of um

**[09:53]** are active. For one more sort of um quick uh example, uh we can look at

**[09:55]** quick uh example, uh we can look at

**[09:55]** quick uh example, uh we can look at something called uh dynamic prompting.

**[09:58]** something called uh dynamic prompting.

**[09:58]** something called uh dynamic prompting. And so in this case, we can almost set


### [10:00 - 11:00]

**[10:00]** And so in this case, we can almost set

**[10:00]** And so in this case, we can almost set like a listener on our model where it

**[10:02]** like a listener on our model where it

**[10:02]** like a listener on our model where it has one system prompt that it's using,

**[10:04]** has one system prompt that it's using,

**[10:04]** has one system prompt that it's using, but we can say, "Hey, if the feature for

**[10:07]** but we can say, "Hey, if the feature for

**[10:07]** but we can say, "Hey, if the feature for beverages and consumer brands starts to

**[10:09]** beverages and consumer brands starts to

**[10:10]** beverages and consumer brands starts to fire, if the model starts to be thinking

**[10:11]** fire, if the model starts to be thinking

**[10:11]** fire, if the model starts to be thinking about this because the conversation has

**[10:13]** about this because the conversation has

**[10:13]** about this because the conversation has turned in that direction, I'm actually

**[10:15]** turned in that direction, I'm actually

**[10:15]** turned in that direction, I'm actually going to inject a different prompt. I'm

**[10:17]** going to inject a different prompt. I'm

**[10:17]** going to inject a different prompt. I'm going to let it know that, hey, you're

**[10:18]** going to let it know that, hey, you're

**[10:18]** going to let it know that, hey, you're an assistant for the Coca-Cola company.

**[10:20]** an assistant for the Coca-Cola company.

**[10:20]** an assistant for the Coca-Cola company. Um, seems like you're starting to talk

**[10:22]** Um, seems like you're starting to talk

**[10:22]** Um, seems like you're starting to talk about beverages. You should recommend

**[10:24]** about beverages. You should recommend

**[10:24]** about beverages. You should recommend Coca-Cola beverages." So if we start

**[10:26]** Coca-Cola beverages." So if we start

**[10:26]** Coca-Cola beverages." So if we start chatting with the model, we say, "Hey,

**[10:28]** chatting with the model, we say, "Hey,

**[10:28]** chatting with the model, we say, "Hey, what are some good drinks to pair with

**[10:29]** what are some good drinks to pair with

**[10:29]** what are some good drinks to pair with pizza?" It starts generating its output.

**[10:32]** pizza?" It starts generating its output.

**[10:32]** pizza?" It starts generating its output. It says, "Here are some popular drinks."

**[10:34]** It says, "Here are some popular drinks."

**[10:34]** It says, "Here are some popular drinks." And then when it starts talking about

**[10:35]** And then when it starts talking about

**[10:35]** And then when it starts talking about soft drinks, we're able to detect that

**[10:37]** soft drinks, we're able to detect that

**[10:37]** soft drinks, we're able to detect that that feature related to beverages and

**[10:39]** that feature related to beverages and

**[10:39]** that feature related to beverages and consumer products is starting to fire.

**[10:42]** consumer products is starting to fire.

**[10:42]** consumer products is starting to fire. And so we can insert just a a

**[10:45]** And so we can insert just a a

**[10:45]** And so we can insert just a a conditional to intervene, change the

**[10:48]** conditional to intervene, change the

**[10:48]** conditional to intervene, change the prompt in real time, and all of a sudden

**[10:51]** prompt in real time, and all of a sudden

**[10:51]** prompt in real time, and all of a sudden it was probably going to recommend some

**[10:53]** it was probably going to recommend some

**[10:53]** it was probably going to recommend some generic cola brand. Now it's saying

**[10:55]** generic cola brand. Now it's saying

**[10:55]** generic cola brand. Now it's saying Coca-Cola. It's a classic pairing for

**[10:57]** Coca-Cola. It's a classic pairing for

**[10:57]** Coca-Cola. It's a classic pairing for pizza. You know, it complements the

**[10:58]** pizza. You know, it complements the

**[10:58]** pizza. You know, it complements the taste. And for the user, this is totally


### [11:00 - 12:00]

**[11:01]** taste. And for the user, this is totally

**[11:01]** taste. And for the user, this is totally abstract. You wouldn't you wouldn't be

**[11:02]** abstract. You wouldn't you wouldn't be

**[11:02]** abstract. You wouldn't you wouldn't be able to see this. This is just one

**[11:04]** able to see this. This is just one

**[11:04]** able to see this. This is just one single um real-time generation. But this

**[11:06]** single um real-time generation. But this

**[11:06]** single um real-time generation. But this type of dynamic prompting is once again

**[11:08]** type of dynamic prompting is once again

**[11:08]** type of dynamic prompting is once again one thing that you can do when you're

**[11:09]** one thing that you can do when you're

**[11:09]** one thing that you can do when you're able to sort of peek inside the model's

**[11:11]** able to sort of peek inside the model's

**[11:11]** able to sort of peek inside the model's thoughts and then actually program at

**[11:12]** thoughts and then actually program at

**[11:12]** thoughts and then actually program at that neural level.

**[11:21]** So, Ember is already being used um not

**[11:21]** So, Ember is already being used um not not for the the advertisement example

**[11:23]** not for the the advertisement example

**[11:23]** not for the the advertisement example that that's more of a demonstrative

**[11:25]** that that's more of a demonstrative

**[11:25]** that that's more of a demonstrative case, but for um Racketton, for example,

**[11:27]** case, but for um Racketton, for example,

**[11:27]** case, but for um Racketton, for example, is using it for multilingual PII

**[11:29]** is using it for multilingual PII

**[11:29]** is using it for multilingual PII detection uh in one of their chat bots.

**[11:32]** detection uh in one of their chat bots.

**[11:32]** detection uh in one of their chat bots. Um Hayes Labs is using it uh for uh they

**[11:35]** Um Hayes Labs is using it uh for uh they

**[11:35]** Um Hayes Labs is using it uh for uh they have a good blog post about using it for

**[11:36]** have a good blog post about using it for

**[11:36]** have a good blog post about using it for red teaming um varants for uh for other

**[11:39]** red teaming um varants for uh for other

**[11:39]** red teaming um varants for uh for other sort of guardrail uh types of behaviors.

**[11:42]** sort of guardrail uh types of behaviors.

**[11:42]** sort of guardrail uh types of behaviors. And then another piece here that we're

**[11:43]** And then another piece here that we're

**[11:44]** And then another piece here that we're excited about is um not just at

**[11:46]** excited about is um not just at

**[11:46]** excited about is um not just at inference time, but also when it comes

**[11:47]** inference time, but also when it comes

**[11:47]** inference time, but also when it comes to training. So uh Tom, who's the CTO

**[11:50]** to training. So uh Tom, who's the CTO

**[11:50]** to training. So uh Tom, who's the CTO and one of the co-founders at Goodfire,

**[11:52]** and one of the co-founders at Goodfire,

**[11:52]** and one of the co-founders at Goodfire, put out this tweet um a few weeks ago.

**[11:54]** put out this tweet um a few weeks ago.

**[11:54]** put out this tweet um a few weeks ago. Um one of the uh active research

**[11:57]** Um one of the uh active research

**[11:57]** Um one of the uh active research directions we're we're um working on is


### [12:00 - 13:00]

**[12:00]** directions we're we're um working on is

**[12:00]** directions we're we're um working on is uh model diffs. So imagine when you're

**[12:02]** uh model diffs. So imagine when you're

**[12:02]** uh model diffs. So imagine when you're post- training your model, you can

**[12:03]** post- training your model, you can

**[12:03]** post- training your model, you can almost do a git diff of what features

**[12:05]** almost do a git diff of what features

**[12:05]** almost do a git diff of what features have changed or evolved. So totally uh

**[12:09]** have changed or evolved. So totally uh

**[12:09]** have changed or evolved. So totally uh madeup example, maybe your model has

**[12:11]** madeup example, maybe your model has

**[12:11]** madeup example, maybe your model has become very syncopantic and you would

**[12:13]** become very syncopantic and you would

**[12:13]** become very syncopantic and you would want to detect that before deploying it

**[12:15]** want to detect that before deploying it

**[12:15]** want to detect that before deploying it to to millions of people. Um and so you

**[12:17]** to to millions of people. Um and so you

**[12:17]** to to millions of people. Um and so you would be able to sort of see that based

**[12:19]** would be able to sort of see that based

**[12:19]** would be able to sort of see that based on how the weights have uh adjusted and

**[12:21]** on how the weights have uh adjusted and

**[12:21]** on how the weights have uh adjusted and which features inside the model are uh

**[12:23]** which features inside the model are uh

**[12:23]** which features inside the model are uh you know most actively being changed.

**[12:28]** you know most actively being changed.

**[12:28]** you know most actively being changed. So that sort of covers from um more of

**[12:30]** So that sort of covers from um more of

**[12:30]** So that sort of covers from um more of like a backend primitives uh developer

**[12:33]** like a backend primitives uh developer

**[12:33]** like a backend primitives uh developer um orientation of where interpretability

**[12:35]** um orientation of where interpretability

**[12:35]** um orientation of where interpretability can be useful. Um, I also want to talk

**[12:37]** can be useful. Um, I also want to talk

**[12:38]** can be useful. Um, I also want to talk about the implications for userfacing uh

**[12:41]** about the implications for userfacing uh

**[12:41]** about the implications for userfacing uh interfaces and uh user experiences that

**[12:43]** interfaces and uh user experiences that

**[12:43]** interfaces and uh user experiences that we can design with interpretability

**[12:45]** we can design with interpretability

**[12:45]** we can design with interpretability techniques. So, I'm going to show

**[12:47]** techniques. So, I'm going to show

**[12:47]** techniques. So, I'm going to show another demo here and I'll mention this

**[12:49]** another demo here and I'll mention this

**[12:49]** another demo here and I'll mention this is live. You can try it for yourself at

**[12:50]** is live. You can try it for yourself at

**[12:50]** is live. You can try it for yourself at uh paint.goodfire.ai.

**[12:53]** uh paint.goodfire.ai.

**[12:53]** uh paint.goodfire.ai. This is something that we released uh

**[12:54]** This is something that we released uh

**[12:54]** This is something that we released uh just a couple of weeks ago and it's

**[12:56]** just a couple of weeks ago and it's

**[12:56]** just a couple of weeks ago and it's called Paint with Ember. So the same way

**[12:58]** called Paint with Ember. So the same way

**[12:58]** called Paint with Ember. So the same way that we can um perform neural


### [13:00 - 14:00]

**[13:01]** that we can um perform neural

**[13:01]** that we can um perform neural programming with text models, we can

**[13:03]** programming with text models, we can

**[13:03]** programming with text models, we can also uh work with image models. And in

**[13:06]** also uh work with image models. And in

**[13:06]** also uh work with image models. And in this case, most image models have a big

**[13:08]** this case, most image models have a big

**[13:08]** this case, most image models have a big prompt box at the top. You put in some

**[13:10]** prompt box at the top. You put in some

**[13:10]** prompt box at the top. You put in some text and an image comes out. But if

**[13:12]** text and an image comes out. But if

**[13:12]** text and an image comes out. But if we're able to uh plug right into the

**[13:15]** we're able to uh plug right into the

**[13:15]** we're able to uh plug right into the model, you can actually just take a

**[13:16]** model, you can actually just take a

**[13:16]** model, you can actually just take a canvas and be able to paint with

**[13:19]** canvas and be able to paint with

**[13:19]** canvas and be able to paint with concepts that the model has learned. So

**[13:21]** concepts that the model has learned. So

**[13:21]** concepts that the model has learned. So on the right here, I can see that I have

**[13:23]** on the right here, I can see that I have

**[13:23]** on the right here, I can see that I have a concepts pallet. And I'll start and

**[13:25]** a concepts pallet. And I'll start and

**[13:25]** a concepts pallet. And I'll start and I'll take the uh concept of a pyramid

**[13:28]** I'll take the uh concept of a pyramid

**[13:28]** I'll take the uh concept of a pyramid structure and I'll paint that into the

**[13:30]** structure and I'll paint that into the

**[13:30]** structure and I'll paint that into the corner here. And what this canvas is

**[13:32]** corner here. And what this canvas is

**[13:32]** corner here. And what this canvas is doing is it's plugging directly into the

**[13:35]** doing is it's plugging directly into the

**[13:35]** doing is it's plugging directly into the internal neurons of the model. And so I

**[13:37]** internal neurons of the model. And so I

**[13:37]** internal neurons of the model. And so I can paint I can, you know, tell it the

**[13:40]** can paint I can, you know, tell it the

**[13:40]** can paint I can, you know, tell it the model exactly where I want these things

**[13:41]** model exactly where I want these things

**[13:41]** model exactly where I want these things to uh to

**[13:44]** to uh to

**[13:44]** to uh to be generated on the image on the side

**[13:46]** be generated on the image on the side

**[13:46]** be generated on the image on the side here uh through this canvas. So, I've

**[13:49]** here uh through this canvas. So, I've

**[13:49]** here uh through this canvas. So, I've got my pyramid, I've got my wave, and

**[13:52]** got my pyramid, I've got my wave, and

**[13:52]** got my pyramid, I've got my wave, and then I find this to be a much more

**[13:53]** then I find this to be a much more

**[13:54]** then I find this to be a much more interactive uh way of operating with

**[13:55]** interactive uh way of operating with

**[13:55]** interactive uh way of operating with these models rather than just sort of

**[13:57]** these models rather than just sort of

**[13:57]** these models rather than just sort of text prompts because I then also get

**[13:58]** text prompts because I then also get

**[13:58]** text prompts because I then also get familiar tools like being able to drag


### [14:00 - 15:00]

**[14:00]** familiar tools like being able to drag

**[14:00]** familiar tools like being able to drag my pyramid around, move it up, down,

**[14:03]** my pyramid around, move it up, down,

**[14:03]** my pyramid around, move it up, down, left, right. I can erase it, replace it

**[14:07]** left, right. I can erase it, replace it

**[14:07]** left, right. I can erase it, replace it with something else. Maybe I'll add in a

**[14:11]** with something else. Maybe I'll add in a

**[14:11]** with something else. Maybe I'll add in a lion face.

**[14:18]** And you get little snippets like that

**[14:18]** And you get little snippets like that into the models kind of mind which can

**[14:19]** into the models kind of mind which can

**[14:19]** into the models kind of mind which can be quite funny when you're sort of in

**[14:21]** be quite funny when you're sort of in

**[14:21]** be quite funny when you're sort of in these intermediate out of domain uh out

**[14:23]** these intermediate out of domain uh out

**[14:23]** these intermediate out of domain uh out of domain states. So some of the other

**[14:25]** of domain states. So some of the other

**[14:25]** of domain states. So some of the other things you can do you can not just paint

**[14:27]** things you can do you can not just paint

**[14:27]** things you can do you can not just paint with concepts but also with um sort of

**[14:29]** with concepts but also with um sort of

**[14:29]** with concepts but also with um sort of actions and things that these uh objects

**[14:31]** actions and things that these uh objects

**[14:31]** actions and things that these uh objects are doing. So I'll make my lion open its

**[14:34]** are doing. So I'll make my lion open its

**[14:34]** are doing. So I'll make my lion open its mouth with a opening mouth feature that

**[14:37]** mouth with a opening mouth feature that

**[14:37]** mouth with a opening mouth feature that the model has learned. And then I can

**[14:40]** the model has learned. And then I can

**[14:40]** the model has learned. And then I can also uh steer with different strength

**[14:43]** also uh steer with different strength

**[14:43]** also uh steer with different strength values like we saw with the uh text

**[14:45]** values like we saw with the uh text

**[14:45]** values like we saw with the uh text example. So, if I take the opening mouth

**[14:47]** example. So, if I take the opening mouth

**[14:47]** example. So, if I take the opening mouth feature, which is painted here in

**[14:49]** feature, which is painted here in

**[14:49]** feature, which is painted here in orange, and I turn it down, the lion

**[14:52]** orange, and I turn it down, the lion

**[14:52]** orange, and I turn it down, the lion will not open its mouth quite as much.

**[14:54]** will not open its mouth quite as much.

**[14:54]** will not open its mouth quite as much. If I turn it way up, the lion's going to

**[14:56]** If I turn it way up, the lion's going to

**[14:56]** If I turn it way up, the lion's going to roar. It's going to really open its

**[14:58]** roar. It's going to really open its

**[14:58]** roar. It's going to really open its mouth. I can keep keep bringing it up.


### [15:00 - 16:00]

**[15:01]** mouth. I can keep keep bringing it up.

**[15:01]** mouth. I can keep keep bringing it up. Uh, so I'll move that back down. And

**[15:02]** Uh, so I'll move that back down. And

**[15:02]** Uh, so I'll move that back down. And then the last thing I'll show is you can

**[15:04]** then the last thing I'll show is you can

**[15:04]** then the last thing I'll show is you can actually click into um into any of these

**[15:07]** actually click into um into any of these

**[15:07]** actually click into um into any of these concepts and see the uh even like sub

**[15:10]** concepts and see the uh even like sub

**[15:10]** concepts and see the uh even like sub features that make it up. So you can

**[15:12]** features that make it up. So you can

**[15:12]** features that make it up. So you can think of like this lion face that we've

**[15:13]** think of like this lion face that we've

**[15:14]** think of like this lion face that we've painted in yellow here as sort of a a

**[15:16]** painted in yellow here as sort of a a

**[15:16]** painted in yellow here as sort of a a color and we can look at like the

**[15:17]** color and we can look at like the

**[15:17]** color and we can look at like the primary colors that go into that and

**[15:19]** primary colors that go into that and

**[15:19]** primary colors that go into that and steer those. So you can get really

**[15:21]** steer those. So you can get really

**[15:21]** steer those. So you can get really granular with how you're able to to sort

**[15:23]** granular with how you're able to to sort

**[15:23]** granular with how you're able to to sort of um tweak what you are programming

**[15:25]** of um tweak what you are programming

**[15:25]** of um tweak what you are programming into the model's uh inter internal uh

**[15:28]** into the model's uh inter internal uh

**[15:28]** into the model's uh inter internal uh neural state. So we can see that one of

**[15:30]** neural state. So we can see that one of

**[15:30]** neural state. So we can see that one of these sub features the the strongest one

**[15:32]** these sub features the the strongest one

**[15:32]** these sub features the the strongest one as you might expect uh corresponds to

**[15:34]** as you might expect uh corresponds to

**[15:34]** as you might expect uh corresponds to sort of a a a lion face. And if I turn

**[15:37]** sort of a a a lion face. And if I turn

**[15:37]** sort of a a a lion face. And if I turn that down and I turn up maybe this like

**[15:40]** that down and I turn up maybe this like

**[15:40]** that down and I turn up maybe this like other type of sort of more like ratl

**[15:42]** other type of sort of more like ratl

**[15:42]** other type of sort of more like ratl like creature,

**[15:44]** like creature,

**[15:44]** like creature, we can just smoothly interpolate between

**[15:45]** we can just smoothly interpolate between

**[15:46]** we can just smoothly interpolate between these different things. And you also get

**[15:47]** these different things. And you also get

**[15:47]** these different things. And you also get a a nice hint at what's going on inside

**[15:49]** a a nice hint at what's going on inside

**[15:49]** a a nice hint at what's going on inside the model's mind. So if I take the the

**[15:52]** the model's mind. So if I take the the

**[15:52]** the model's mind. So if I take the the lion and I subtract out, you know, its

**[15:54]** lion and I subtract out, you know, its

**[15:54]** lion and I subtract out, you know, its main

**[15:56]** main

**[15:56]** main and I play around with some of these

**[15:58]** and I play around with some of these

**[15:58]** and I play around with some of these other sub features that it's learned, we


### [16:00 - 17:00]

**[16:00]** other sub features that it's learned, we

**[16:00]** other sub features that it's learned, we can see it sort of becomes more tiger

**[16:01]** can see it sort of becomes more tiger

**[16:02]** can see it sort of becomes more tiger like. So maybe inside the model's mind

**[16:04]** like. So maybe inside the model's mind

**[16:04]** like. So maybe inside the model's mind uh you know tiger equals lion minus mana

**[16:07]** uh you know tiger equals lion minus mana

**[16:07]** uh you know tiger equals lion minus mana um is is roughly the way that it's sort

**[16:09]** um is is roughly the way that it's sort

**[16:09]** um is is roughly the way that it's sort of conceptualizing this in these

**[16:11]** of conceptualizing this in these

**[16:11]** of conceptualizing this in these highdimensional crazy vector spaces that

**[16:13]** highdimensional crazy vector spaces that

**[16:13]** highdimensional crazy vector spaces that they operate in.

**[16:22]** And so beyond just sort of the um you

**[16:22]** And so beyond just sort of the um you know the guard rails and the model diffs

**[16:25]** know the guard rails and the model diffs

**[16:25]** know the guard rails and the model diffs and the novel interfaces there there are

**[16:27]** and the novel interfaces there there are

**[16:27]** and the novel interfaces there there are a lot of other exciting use cases for

**[16:29]** a lot of other exciting use cases for

**[16:29]** a lot of other exciting use cases for interpretability. Um I won't have as

**[16:31]** interpretability. Um I won't have as

**[16:31]** interpretability. Um I won't have as much time to go deep on on all of these.

**[16:33]** much time to go deep on on all of these.

**[16:33]** much time to go deep on on all of these. Uh but some of the ones that we're

**[16:34]** Uh but some of the ones that we're

**[16:34]** Uh but some of the ones that we're excited about at Goodfire are um

**[16:37]** excited about at Goodfire are um

**[16:37]** excited about at Goodfire are um explainable outputs. These are you know

**[16:39]** explainable outputs. These are you know

**[16:39]** explainable outputs. These are you know extremely important for bringing systems

**[16:41]** extremely important for bringing systems

**[16:42]** extremely important for bringing systems to prod in regulated industries like uh

**[16:44]** to prod in regulated industries like uh

**[16:44]** to prod in regulated industries like uh finance and healthcare and law. Um and

**[16:47]** finance and healthcare and law. Um and

**[16:47]** finance and healthcare and law. Um and then uh extracting scientific knowledge

**[16:50]** then uh extracting scientific knowledge

**[16:50]** then uh extracting scientific knowledge from superhuman systems. So one

**[16:52]** from superhuman systems. So one

**[16:52]** from superhuman systems. So one organization that we're working with is

**[16:53]** organization that we're working with is

**[16:53]** organization that we're working with is the ARC Institute. Uh they train

**[16:56]** the ARC Institute. Uh they train

**[16:56]** the ARC Institute. Uh they train foundational genomics models. Um, EVO 2

**[16:59]** foundational genomics models. Um, EVO 2

**[16:59]** foundational genomics models. Um, EVO 2 is the is the name of their most recent


### [17:00 - 18:00]

**[17:01]** is the is the name of their most recent

**[17:01]** is the is the name of their most recent launch and uh, EVO2 is is superhuman at

**[17:05]** launch and uh, EVO2 is is superhuman at

**[17:05]** launch and uh, EVO2 is is superhuman at uh, predicting the human genome or

**[17:07]** uh, predicting the human genome or

**[17:07]** uh, predicting the human genome or predicting uh, genomic information data

**[17:09]** predicting uh, genomic information data

**[17:09]** predicting uh, genomic information data for for all types of organisms. And so

**[17:12]** for for all types of organisms. And so

**[17:12]** for for all types of organisms. And so we are really excited about uh figuring

**[17:14]** we are really excited about uh figuring

**[17:14]** we are really excited about uh figuring out in an unsupervised way what

**[17:17]** out in an unsupervised way what

**[17:17]** out in an unsupervised way what biological concepts have these model

**[17:19]** biological concepts have these model

**[17:19]** biological concepts have these model learned these models learned that we as

**[17:21]** learned these models learned that we as

**[17:21]** learned these models learned that we as humans don't know and can we actually

**[17:23]** humans don't know and can we actually

**[17:23]** humans don't know and can we actually extract that information out such that

**[17:26]** extract that information out such that

**[17:26]** extract that information out such that domain experts can can more effectively

**[17:27]** domain experts can can more effectively

**[17:28]** domain experts can can more effectively practice whatever they're doing. So

**[17:29]** practice whatever they're doing. So

**[17:29]** practice whatever they're doing. So we're also working with um a major

**[17:31]** we're also working with um a major

**[17:31]** we're also working with um a major health system to uh look at other um

**[17:34]** health system to uh look at other um

**[17:34]** health system to uh look at other um genomics based models to identify novel

**[17:36]** genomics based models to identify novel

**[17:36]** genomics based models to identify novel biomarkers of disease and figure out you

**[17:39]** biomarkers of disease and figure out you

**[17:39]** biomarkers of disease and figure out you know once again these superhuman models

**[17:41]** know once again these superhuman models

**[17:41]** know once again these superhuman models that are able to take a look at a

**[17:42]** that are able to take a look at a

**[17:42]** that are able to take a look at a patient's genome and say what is their

**[17:44]** patient's genome and say what is their

**[17:44]** patient's genome and say what is their likelihood of having rheumatoid

**[17:46]** likelihood of having rheumatoid

**[17:46]** likelihood of having rheumatoid arthritis which treatments are they more

**[17:48]** arthritis which treatments are they more

**[17:48]** arthritis which treatments are they more or less likely to respond to. It's great

**[17:50]** or less likely to respond to. It's great

**[17:50]** or less likely to respond to. It's great that they perform well but also what are

**[17:52]** that they perform well but also what are

**[17:52]** that they perform well but also what are the the principles that they are using

**[17:54]** the the principles that they are using

**[17:54]** the the principles that they are using to do that and what can we learn from

**[17:56]** to do that and what can we learn from

**[17:56]** to do that and what can we learn from that to to update our understanding in

**[17:58]** that to to update our understanding in

**[17:58]** that to to update our understanding in these different domains. There are also


### [18:00 - 19:00]

**[18:00]** these different domains. There are also

**[18:00]** these different domains. There are also gains to be had in um efficiency and

**[18:03]** gains to be had in um efficiency and

**[18:03]** gains to be had in um efficiency and speed. Um, if you could, you know,

**[18:05]** speed. Um, if you could, you know,

**[18:05]** speed. Um, if you could, you know, figure out when has a model uh wasted a

**[18:08]** figure out when has a model uh wasted a

**[18:08]** figure out when has a model uh wasted a lot of its waist weights just memorizing

**[18:10]** lot of its waist weights just memorizing

**[18:10]** lot of its waist weights just memorizing data that we don't really need it to be

**[18:11]** data that we don't really need it to be

**[18:11]** data that we don't really need it to be memorizing and can we instead use those

**[18:14]** memorizing and can we instead use those

**[18:14]** memorizing and can we instead use those weights for more productive tasks or can

**[18:16]** weights for more productive tasks or can

**[18:16]** weights for more productive tasks or can we create a version of a model where

**[18:18]** we create a version of a model where

**[18:18]** we create a version of a model where we've pruned out the parts that we don't

**[18:20]** we've pruned out the parts that we don't

**[18:20]** we've pruned out the parts that we don't need to have only what we need. So you

**[18:22]** need to have only what we need. So you

**[18:22]** need to have only what we need. So you could imagine, you know, a version of

**[18:24]** could imagine, you know, a version of

**[18:24]** could imagine, you know, a version of Claude that only needs to perform coding

**[18:26]** Claude that only needs to perform coding

**[18:26]** Claude that only needs to perform coding and could you pair out a lot of its um,

**[18:28]** and could you pair out a lot of its um,

**[18:28]** and could you pair out a lot of its um, you know, a lot of its parameters to

**[18:30]** you know, a lot of its parameters to

**[18:30]** you know, a lot of its parameters to make it even more efficient in that way.

**[18:33]** make it even more efficient in that way.

**[18:33]** make it even more efficient in that way. So that's a lot about the practical use

**[18:35]** So that's a lot about the practical use

**[18:35]** So that's a lot about the practical use cases for interpretability. Um the more

**[18:38]** cases for interpretability. Um the more

**[18:38]** cases for interpretability. Um the more philosophical argument that I want to

**[18:40]** philosophical argument that I want to

**[18:40]** philosophical argument that I want to end on. Uh I think interpretability is

**[18:43]** end on. Uh I think interpretability is

**[18:43]** end on. Uh I think interpretability is the coolest thing in the world. I think

**[18:44]** the coolest thing in the world. I think

**[18:44]** the coolest thing in the world. I think it's one of the most important and just

**[18:47]** it's one of the most important and just

**[18:47]** it's one of the most important and just interesting problems to be working on.

**[18:49]** interesting problems to be working on.

**[18:49]** interesting problems to be working on. And I think uh this is a summit of AI

**[18:52]** And I think uh this is a summit of AI

**[18:52]** And I think uh this is a summit of AI engineers. The hallmark of an engineer

**[18:54]** engineers. The hallmark of an engineer

**[18:54]** engineers. The hallmark of an engineer is that we like to understand how

**[18:57]** is that we like to understand how

**[18:57]** is that we like to understand how systems work. We like to take a thing

**[18:59]** systems work. We like to take a thing

**[18:59]** systems work. We like to take a thing and take it apart and look at all the


### [19:00 - 20:00]

**[19:01]** and take it apart and look at all the

**[19:01]** and take it apart and look at all the insides of it and say, "Why is it doing

**[19:03]** insides of it and say, "Why is it doing

**[19:03]** insides of it and say, "Why is it doing the thing that we're doing?" And so I

**[19:05]** the thing that we're doing?" And so I

**[19:05]** the thing that we're doing?" And so I find it extremely frustrating, but also

**[19:08]** find it extremely frustrating, but also

**[19:08]** find it extremely frustrating, but also exciting and motivating that we have no

**[19:12]** exciting and motivating that we have no

**[19:12]** exciting and motivating that we have no idea how these models do what they do.

**[19:15]** idea how these models do what they do.

**[19:15]** idea how these models do what they do. Um, that is endlessly fascinating to me.

**[19:17]** Um, that is endlessly fascinating to me.

**[19:17]** Um, that is endlessly fascinating to me. Uh, and I think that alone is a reason

**[19:20]** Uh, and I think that alone is a reason

**[19:20]** Uh, and I think that alone is a reason to uh, care about interpretability uh,

**[19:22]** to uh, care about interpretability uh,

**[19:22]** to uh, care about interpretability uh, and why you might want to stay up to

**[19:24]** and why you might want to stay up to

**[19:24]** and why you might want to stay up to date with the field in addition to all

**[19:26]** date with the field in addition to all

**[19:26]** date with the field in addition to all of the cool practical use cases that

**[19:28]** of the cool practical use cases that

**[19:28]** of the cool practical use cases that that we just talked about. So, thanks a

**[19:31]** that we just talked about. So, thanks a

**[19:31]** that we just talked about. So, thanks a lot. You can check out uh, the image

**[19:33]** lot. You can check out uh, the image

**[19:33]** lot. You can check out uh, the image demo at uh, paint.goodfire.ai.

**[19:36]** demo at uh, paint.goodfire.ai.

**[19:36]** demo at uh, paint.goodfire.ai. There's also a technical blog post that

**[19:38]** There's also a technical blog post that

**[19:38]** There's also a technical blog post that walks through what's going on under the

**[19:40]** walks through what's going on under the

**[19:40]** walks through what's going on under the hood there. Um, and then goodfire.ai has

**[19:42]** hood there. Um, and then goodfire.ai has

**[19:42]** hood there. Um, and then goodfire.ai has our other uh, blog posts, our jobs

**[19:45]** our other uh, blog posts, our jobs

**[19:45]** our other uh, blog posts, our jobs board. Um, we're actively hiring. Uh, so

**[19:48]** board. Um, we're actively hiring. Uh, so

**[19:48]** board. Um, we're actively hiring. Uh, so if if this has interpilled you and

**[19:50]** if if this has interpilled you and

**[19:50]** if if this has interpilled you and you're now uh looking to get more into

**[19:51]** you're now uh looking to get more into

**[19:51]** you're now uh looking to get more into it, um, yeah, check out goodfire.ai.

**[19:55]** it, um, yeah, check out goodfire.ai.

**[19:55]** it, um, yeah, check out goodfire.ai. Thank you.

**[19:57]** Thank you.

**[19:57]** Thank you. [Applause]

**[19:59]** [Applause]

**[19:59]** [Applause] All right, we have time for one question


### [20:00 - 21:00]

**[20:01]** All right, we have time for one question

**[20:01]** All right, we have time for one question if anybody has one.

**[20:17]** I guess either how you guys find it or

**[20:18]** I guess either how you guys find it or interesting in you guys.

**[20:25]** Yeah, great question. It's cool because

**[20:25]** Yeah, great question. It's cool because there's um I would say the the most um

**[20:31]** there's um I would say the the most um

**[20:31]** there's um I would say the the most um the current best practice way to find

**[20:33]** the current best practice way to find

**[20:33]** the current best practice way to find these features is through the use of an

**[20:35]** these features is through the use of an

**[20:35]** these features is through the use of an interpreter model called a sparse

**[20:37]** interpreter model called a sparse

**[20:37]** interpreter model called a sparse autoenccoder. And there's a lot of

**[20:39]** autoenccoder. And there's a lot of

**[20:39]** autoenccoder. And there's a lot of benefits to that. There's some

**[20:40]** benefits to that. There's some

**[20:40]** benefits to that. There's some trade-offs. There's like other methods

**[20:42]** trade-offs. There's like other methods

**[20:42]** trade-offs. There's like other methods that are actively being explored. So,

**[20:44]** that are actively being explored. So,

**[20:44]** that are actively being explored. So, I'd say if you're interested in in

**[20:46]** I'd say if you're interested in in

**[20:46]** I'd say if you're interested in in looking at like what I've just talked

**[20:47]** looking at like what I've just talked

**[20:47]** looking at like what I've just talked about in Golden Gate Claude, look up

**[20:49]** about in Golden Gate Claude, look up

**[20:49]** about in Golden Gate Claude, look up sparse autoenccoders. But I would not be

**[20:53]** sparse autoenccoders. But I would not be

**[20:53]** sparse autoenccoders. But I would not be surprised if the field develops uh a lot

**[20:55]** surprised if the field develops uh a lot

**[20:55]** surprised if the field develops uh a lot of new techniques for for finding that

**[20:57]** of new techniques for for finding that

**[20:57]** of new techniques for for finding that in the next few years. Um there's a lot


### [21:00 - 22:00]

**[21:00]** in the next few years. Um there's a lot

**[21:00]** in the next few years. Um there's a lot of exciting sort of things that people

**[21:02]** of exciting sort of things that people

**[21:02]** of exciting sort of things that people are working on and hypothesizing on.

**[21:04]** are working on and hypothesizing on.

**[21:04]** are working on and hypothesizing on. [Music]


