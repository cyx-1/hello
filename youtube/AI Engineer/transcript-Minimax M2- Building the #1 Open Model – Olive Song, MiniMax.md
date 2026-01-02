# Minimax M2- Building the #1 Open Model – Olive Song, MiniMax

**Video URL:** https://www.youtube.com/watch?v=lY1iFbDPRlw

---

## Full Transcript

### [00:00 - 01:00]

**[00:24]** Hi. Hi everyone. Um, I'm Olive. It's my

**[00:24]** Hi. Hi everyone. Um, I'm Olive. It's my great honor here today to present on our

**[00:26]** great honor here today to present on our

**[00:26]** great honor here today to present on our new model, Miniax M2. Um, I actually

**[00:29]** new model, Miniax M2. Um, I actually

**[00:29]** new model, Miniax M2. Um, I actually lived in New York City for six years, so

**[00:31]** lived in New York City for six years, so

**[00:31]** lived in New York City for six years, so it feels great to come back. Um, but

**[00:33]** it feels great to come back. Um, but

**[00:33]** it feels great to come back. Um, but with a different role. Um, I currently

**[00:35]** with a different role. Um, I currently

**[00:36]** with a different role. Um, I currently study reinforcement learning and model

**[00:38]** study reinforcement learning and model

**[00:38]** study reinforcement learning and model evaluation at Miniax. Um, let me just

**[00:41]** evaluation at Miniax. Um, let me just

**[00:41]** evaluation at Miniax. Um, let me just get a quick sense of the room. Who here

**[00:43]** get a quick sense of the room. Who here

**[00:43]** get a quick sense of the room. Who here has heard or have tried of Miniax

**[00:45]** has heard or have tried of Miniax

**[00:46]** has heard or have tried of Miniax before? Oh, a couple of there. Yeah, not

**[00:50]** before? Oh, a couple of there. Yeah, not

**[00:50]** before? Oh, a couple of there. Yeah, not everybody, but I guess Yeah, but here's

**[00:53]** everybody, but I guess Yeah, but here's

**[00:53]** everybody, but I guess Yeah, but here's the value, right, of me standing here

**[00:55]** the value, right, of me standing here

**[00:55]** the value, right, of me standing here today. Um so we are a global company

**[00:59]** today. Um so we are a global company

**[00:59]** today. Um so we are a global company that works on both foundation models and


### [01:00 - 02:00]

**[01:02]** that works on both foundation models and

**[01:02]** that works on both foundation models and applications. We develop multi modality

**[01:05]** applications. We develop multi modality

**[01:05]** applications. We develop multi modality models including text um vision language

**[01:08]** models including text um vision language

**[01:08]** models including text um vision language models our video generation model hyoa

**[01:11]** models our video generation model hyoa

**[01:11]** models our video generation model hyoa and speech generation music generation

**[01:13]** and speech generation music generation

**[01:13]** and speech generation music generation stuff and we also have um many

**[01:16]** stuff and we also have um many

**[01:16]** stuff and we also have um many applications including agents and stuff

**[01:19]** applications including agents and stuff

**[01:19]** applications including agents and stuff um inhouse. So that that's the specific

**[01:22]** um inhouse. So that that's the specific

**[01:22]** um inhouse. So that that's the specific thing that's different from the other

**[01:24]** thing that's different from the other

**[01:24]** thing that's different from the other labs for other companies. So we both

**[01:26]** labs for other companies. So we both

**[01:26]** labs for other companies. So we both develop foundation models um and

**[01:29]** develop foundation models um and

**[01:29]** develop foundation models um and applications. So we have research and

**[01:31]** applications. So we have research and

**[01:31]** applications. So we have research and developers sitting uh sitting side by

**[01:34]** developers sitting uh sitting side by

**[01:34]** developers sitting uh sitting side by side working on things. Um so our

**[01:38]** side working on things. Um so our

**[01:38]** side working on things. Um so our difference would be that we have

**[01:40]** difference would be that we have

**[01:40]** difference would be that we have firsthand experience from our um

**[01:43]** firsthand experience from our um

**[01:43]** firsthand experience from our um in-house developers into developing

**[01:46]** in-house developers into developing

**[01:46]** in-house developers into developing models that developers would really need

**[01:49]** models that developers would really need

**[01:49]** models that developers would really need in the community. And here I want to

**[01:51]** in the community. And here I want to

**[01:51]** in the community. And here I want to introduce our Miniax M2 um which is an

**[01:55]** introduce our Miniax M2 um which is an

**[01:55]** introduce our Miniax M2 um which is an openweight model very small with only 10

**[01:59]** openweight model very small with only 10

**[01:59]** openweight model very small with only 10 billion active parameters um that was


### [02:00 - 03:00]

**[02:01]** billion active parameters um that was

**[02:02]** billion active parameters um that was designed specifically for coding

**[02:04]** designed specifically for coding

**[02:04]** designed specifically for coding workplace agentic tasks. It's very

**[02:07]** workplace agentic tasks. It's very

**[02:07]** workplace agentic tasks. It's very costefficient.

**[02:09]** costefficient.

**[02:09]** costefficient. Um let me just go over the benchmark

**[02:12]** Um let me just go over the benchmark

**[02:12]** Um let me just go over the benchmark performance because people care about

**[02:14]** performance because people care about

**[02:14]** performance because people care about it. So uh we rank very top in both um

**[02:19]** it. So uh we rank very top in both um

**[02:19]** it. So uh we rank very top in both um intelligence benchmarks and also agent

**[02:21]** intelligence benchmarks and also agent

**[02:21]** intelligence benchmarks and also agent benchmarks. Uh we I think we're on the

**[02:24]** benchmarks. Uh we I think we're on the

**[02:24]** benchmarks. Uh we I think we're on the top of the open source models. But then

**[02:27]** top of the open source models. But then

**[02:27]** top of the open source models. But then numbers don't tell everything because

**[02:30]** numbers don't tell everything because

**[02:30]** numbers don't tell everything because sometimes you get those super high

**[02:32]** sometimes you get those super high

**[02:32]** sometimes you get those super high number models you plug into them um into

**[02:35]** number models you plug into them um into

**[02:35]** number models you plug into them um into your environment and they suck, right?

**[02:38]** your environment and they suck, right?

**[02:38]** your environment and they suck, right? So we really care about the dynamics in

**[02:41]** So we really care about the dynamics in

**[02:41]** So we really care about the dynamics in the community and in our first week we

**[02:44]** the community and in our first week we

**[02:44]** the community and in our first week we had the most downloads

**[02:46]** had the most downloads

**[02:46]** had the most downloads and also we climbed up to top three

**[02:49]** and also we climbed up to top three

**[02:49]** and also we climbed up to top three token usage on open router. So we're

**[02:51]** token usage on open router. So we're

**[02:51]** token usage on open router. So we're very glad that people in the community

**[02:53]** very glad that people in the community

**[02:53]** very glad that people in the community are really loving our model um into

**[02:55]** are really loving our model um into

**[02:56]** are really loving our model um into their development cycle.

**[02:58]** their development cycle.

**[02:58]** their development cycle. So today what I want to share is how we


### [03:00 - 04:00]

**[03:02]** So today what I want to share is how we

**[03:02]** So today what I want to share is how we actually shape these men model

**[03:04]** actually shape these men model

**[03:04]** actually shape these men model characteristics that made M2 so good in

**[03:07]** characteristics that made M2 so good in

**[03:08]** characteristics that made M2 so good in your coding experience. And I'm gonna

**[03:10]** your coding experience. And I'm gonna

**[03:10]** your coding experience. And I'm gonna present to you um the training be behind

**[03:14]** present to you um the training be behind

**[03:14]** present to you um the training be behind it that supports each one of them from

**[03:17]** it that supports each one of them from

**[03:17]** it that supports each one of them from coding experience to long horizon state

**[03:20]** coding experience to long horizon state

**[03:20]** coding experience to long horizon state tracking tasks um to robust

**[03:22]** tracking tasks um to robust

**[03:22]** tracking tasks um to robust generalization to different scaffolds to

**[03:25]** generalization to different scaffolds to

**[03:25]** generalization to different scaffolds to multi- aent uh scalability.

**[03:28]** multi- aent uh scalability.

**[03:28]** multi- aent uh scalability. So first let's talk about code

**[03:30]** So first let's talk about code

**[03:30]** So first let's talk about code experience which we sc uh which we

**[03:33]** experience which we sc uh which we

**[03:33]** experience which we sc uh which we supported with um scaled environments

**[03:35]** supported with um scaled environments

**[03:35]** supported with um scaled environments and scaled experts.

**[03:38]** and scaled experts.

**[03:38]** and scaled experts. So um developers need a model that can

**[03:42]** So um developers need a model that can

**[03:42]** So um developers need a model that can actually work in the language they use

**[03:44]** actually work in the language they use

**[03:44]** actually work in the language they use and across the workflow that they deal

**[03:46]** and across the workflow that they deal

**[03:46]** and across the workflow that they deal with every day. So which means that we

**[03:49]** with every day. So which means that we

**[03:49]** with every day. So which means that we need to utilize the real data from from

**[03:52]** need to utilize the real data from from

**[03:52]** need to utilize the real data from from the internet and then um scale the

**[03:54]** the internet and then um scale the

**[03:54]** the internet and then um scale the number of environments so that the model

**[03:57]** number of environments so that the model

**[03:57]** number of environments so that the model when during training for example during

**[03:59]** when during training for example during

**[03:59]** when during training for example during reinforcement learning it can actually


### [04:00 - 05:00]

**[04:02]** reinforcement learning it can actually

**[04:02]** reinforcement learning it can actually um reacts to the uh environment. it can

**[04:04]** um reacts to the uh environment. it can

**[04:04]** um reacts to the uh environment. it can actually target verifiable coding goals

**[04:07]** actually target verifiable coding goals

**[04:07]** actually target verifiable coding goals and to learn from it. So that's why we

**[04:10]** and to learn from it. So that's why we

**[04:10]** and to learn from it. So that's why we scaled both the number uh of

**[04:13]** scaled both the number uh of

**[04:13]** scaled both the number uh of environments and also our um

**[04:15]** environments and also our um

**[04:15]** environments and also our um infrastructure so that we can perform

**[04:18]** infrastructure so that we can perform

**[04:18]** infrastructure so that we can perform those training very efficiently.

**[04:20]** those training very efficiently.

**[04:20]** those training very efficiently. So um with data construction and

**[04:23]** So um with data construction and

**[04:24]** So um with data construction and reinforcement learning we were able to

**[04:26]** reinforcement learning we were able to

**[04:26]** reinforcement learning we were able to train the model so that it's very strong

**[04:29]** train the model so that it's very strong

**[04:29]** train the model so that it's very strong um it's full stack multilingual

**[04:33]** um it's full stack multilingual

**[04:33]** um it's full stack multilingual and what I want to mention here is that

**[04:34]** and what I want to mention here is that

**[04:34]** and what I want to mention here is that besides scaling environment that

**[04:36]** besides scaling environment that

**[04:36]** besides scaling environment that everybody talks about we actually scale

**[04:39]** everybody talks about we actually scale

**[04:39]** everybody talks about we actually scale something called expert developers um as

**[04:42]** something called expert developers um as

**[04:42]** something called expert developers um as reward models. So as I mentioned before

**[04:45]** reward models. So as I mentioned before

**[04:45]** reward models. So as I mentioned before uh we have a ton of um super expert

**[04:48]** uh we have a ton of um super expert

**[04:48]** uh we have a ton of um super expert developers in house that could give us

**[04:51]** developers in house that could give us

**[04:51]** developers in house that could give us feedback to our model's performance. So

**[04:54]** feedback to our model's performance. So

**[04:54]** feedback to our model's performance. So they participated closely into the model

**[04:56]** they participated closely into the model

**[04:56]** they participated closely into the model development and training cycle including

**[04:59]** development and training cycle including

**[04:59]** development and training cycle including problem definition for example um bugs


### [05:00 - 06:00]

**[05:02]** problem definition for example um bugs

**[05:02]** problem definition for example um bugs bug fixing for example um repo

**[05:05]** bug fixing for example um repo

**[05:05]** bug fixing for example um repo refactoring and stuff like that. And

**[05:07]** refactoring and stuff like that. And

**[05:07]** refactoring and stuff like that. And also they identify the model behaviors

**[05:10]** also they identify the model behaviors

**[05:10]** also they identify the model behaviors that developers enjoy and they identify

**[05:13]** that developers enjoy and they identify

**[05:13]** that developers enjoy and they identify what's reliable and uh what developers

**[05:16]** what's reliable and uh what developers

**[05:16]** what's reliable and uh what developers would trust

**[05:17]** would trust

**[05:18]** would trust and they give precise reward and

**[05:19]** and they give precise reward and

**[05:20]** and they give precise reward and evaluation to the model's behaviors to

**[05:22]** evaluation to the model's behaviors to

**[05:22]** evaluation to the model's behaviors to the final um deliverables so that um it

**[05:26]** the final um deliverables so that um it

**[05:26]** the final um deliverables so that um it is a model that developers really want

**[05:28]** is a model that developers really want

**[05:28]** is a model that developers really want to work with and that can adds

**[05:29]** to work with and that can adds

**[05:29]** to work with and that can adds efficiency to the developers.

**[05:36]** So with that we were able to lead in

**[05:36]** So with that we were able to lead in many um languages in real use.

**[05:40]** many um languages in real use.

**[05:40]** many um languages in real use. And the second characteristic that

**[05:42]** And the second characteristic that

**[05:42]** And the second characteristic that Miniax M2 has is it it performs good in

**[05:46]** Miniax M2 has is it it performs good in

**[05:46]** Miniax M2 has is it it performs good in those long horizon tasks. Uh those long

**[05:49]** those long horizon tasks. Uh those long

**[05:49]** those long horizon tasks. Uh those long tasks that require interacting with

**[05:52]** tasks that require interacting with

**[05:52]** tasks that require interacting with complex environments that requiring um

**[05:55]** complex environments that requiring um

**[05:55]** complex environments that requiring um using multiple tools with reasoning.

**[05:59]** using multiple tools with reasoning.

**[05:59]** using multiple tools with reasoning. And we supported that with the interled


### [06:00 - 07:00]

**[06:01]** And we supported that with the interled

**[06:01]** And we supported that with the interled thinking pattern um and reinforcement

**[06:04]** thinking pattern um and reinforcement

**[06:04]** thinking pattern um and reinforcement learning.

**[06:06]** learning.

**[06:06]** learning. So what is interled thinking? Um so with

**[06:10]** So what is interled thinking? Um so with

**[06:10]** So what is interled thinking? Um so with a normal reasoning model that can use

**[06:13]** a normal reasoning model that can use

**[06:13]** a normal reasoning model that can use tools, it it normally works like this.

**[06:15]** tools, it it normally works like this.

**[06:15]** tools, it it normally works like this. You have the tools information given to

**[06:17]** You have the tools information given to

**[06:17]** You have the tools information given to it. You have the system prompts. Um you

**[06:20]** it. You have the system prompts. Um you

**[06:20]** it. You have the system prompts. Um you have user prompts and then the model

**[06:23]** have user prompts and then the model

**[06:23]** have user prompts and then the model would sync and then it calls tools. It

**[06:26]** would sync and then it calls tools. It

**[06:26]** would sync and then it calls tools. It can be a couple of tools at the same

**[06:28]** can be a couple of tools at the same

**[06:28]** can be a couple of tools at the same time. And then they get the tool

**[06:30]** time. And then they get the tool

**[06:30]** time. And then they get the tool response from the environment and then

**[06:32]** response from the environment and then

**[06:32]** response from the environment and then it performs a final thinking and deliver

**[06:35]** it performs a final thinking and deliver

**[06:35]** it performs a final thinking and deliver a final content. But but here's the

**[06:38]** a final content. But but here's the

**[06:38]** a final content. But but here's the truth, right? In real world, the

**[06:40]** truth, right? In real world, the

**[06:40]** truth, right? In real world, the environments are often noisy and

**[06:42]** environments are often noisy and

**[06:42]** environments are often noisy and dynamic. You can't really perform this

**[06:45]** dynamic. You can't really perform this

**[06:45]** dynamic. You can't really perform this one test just by once. You can get um

**[06:49]** one test just by once. You can get um

**[06:49]** one test just by once. You can get um tool errors for example. You can get um

**[06:52]** tool errors for example. You can get um

**[06:52]** tool errors for example. You can get um unexpected results from the environment

**[06:54]** unexpected results from the environment

**[06:54]** unexpected results from the environment and stuff like that. So um what we did

**[06:57]** and stuff like that. So um what we did

**[06:57]** and stuff like that. So um what we did is that we imagine how humans interact


### [07:00 - 08:00]

**[07:00]** is that we imagine how humans interact

**[07:00]** is that we imagine how humans interact with the world. We we we look at

**[07:02]** with the world. We we we look at

**[07:02]** with the world. We we we look at something we get feedbacks and then we

**[07:05]** something we get feedbacks and then we

**[07:05]** something we get feedbacks and then we think about it. We think if the feedback

**[07:07]** think about it. We think if the feedback

**[07:07]** think about it. We think if the feedback is good or not and then we make other

**[07:09]** is good or not and then we make other

**[07:09]** is good or not and then we make other actions, make other decisions. And

**[07:11]** actions, make other decisions. And

**[07:11]** actions, make other decisions. And that's why we did the same thing with

**[07:13]** that's why we did the same thing with

**[07:13]** that's why we did the same thing with our M2 model. So if we look at this um

**[07:17]** our M2 model. So if we look at this um

**[07:17]** our M2 model. So if we look at this um chart over a diagram on the right. So

**[07:20]** chart over a diagram on the right. So

**[07:20]** chart over a diagram on the right. So instead of just stopping um after one

**[07:24]** instead of just stopping um after one

**[07:24]** instead of just stopping um after one round of tool calling, it actually

**[07:27]** round of tool calling, it actually

**[07:27]** round of tool calling, it actually thinks again and reacts to the uh reacts

**[07:30]** thinks again and reacts to the uh reacts

**[07:30]** thinks again and reacts to the uh reacts to the environments to see if the

**[07:33]** to the environments to see if the

**[07:33]** to the environments to see if the information is enough for it to uh get

**[07:36]** information is enough for it to uh get

**[07:36]** information is enough for it to uh get what it wants. So basically we call the

**[07:39]** what it wants. So basically we call the

**[07:39]** what it wants. So basically we call the interle thinking or people call it

**[07:42]** interle thinking or people call it

**[07:42]** interle thinking or people call it interle thinking because it interle

**[07:44]** interle thinking because it interle

**[07:44]** interle thinking because it interle thinking with tool calling. um a couple

**[07:46]** thinking with tool calling. um a couple

**[07:46]** thinking with tool calling. um a couple of time it can be you know uh tens to

**[07:49]** of time it can be you know uh tens to

**[07:49]** of time it can be you know uh tens to 100 um turns [clears throat] of tool

**[07:52]** 100 um turns [clears throat] of tool

**[07:52]** 100 um turns [clears throat] of tool calling within just one user interaction

**[07:55]** calling within just one user interaction

**[07:55]** calling within just one user interaction term

**[07:57]** term

**[07:57]** term so it helps um adaptation to environment


### [08:00 - 09:00]

**[08:01]** so it helps um adaptation to environment

**[08:01]** so it helps um adaptation to environment noise for example uh just like what I

**[08:04]** noise for example uh just like what I

**[08:04]** noise for example uh just like what I mentioned the environment is it's it's

**[08:06]** mentioned the environment is it's it's

**[08:06]** mentioned the environment is it's it's not stable all the time and then

**[08:08]** not stable all the time and then

**[08:08]** not stable all the time and then something is suboptimal and then it can

**[08:10]** something is suboptimal and then it can

**[08:10]** something is suboptimal and then it can choose to use other tools or do other

**[08:12]** choose to use other tools or do other

**[08:12]** choose to use other tools or do other decisions it can focus on long horizon

**[08:16]** decisions it can focus on long horizon

**[08:16]** decisions it can focus on long horizon has um can automate your workflow um

**[08:19]** has um can automate your workflow um

**[08:19]** has um can automate your workflow um using for example Gmails, notions, um

**[08:23]** using for example Gmails, notions, um

**[08:23]** using for example Gmails, notions, um terminal all at the same time. You just

**[08:25]** terminal all at the same time. You just

**[08:25]** terminal all at the same time. You just need to maybe make one model call

**[08:27]** need to maybe make one model call

**[08:27]** need to maybe make one model call without minim with minimal um human

**[08:30]** without minim with minimal um human

**[08:30]** without minim with minimal um human intervention. It can do it all by

**[08:32]** intervention. It can do it all by

**[08:32]** intervention. It can do it all by itself. And and here's a cool

**[08:34]** itself. And and here's a cool

**[08:34]** itself. And and here's a cool illustration on the right because it's

**[08:36]** illustration on the right because it's

**[08:36]** illustration on the right because it's New York City. I feel the vibe of you

**[08:39]** New York City. I feel the vibe of you

**[08:39]** New York City. I feel the vibe of you know trading and marketing. Um so you

**[08:42]** know trading and marketing. Um so you

**[08:42]** know trading and marketing. Um so you can see that there was some um there was

**[08:45]** can see that there was some um there was

**[08:45]** can see that there was some um there was some perturbations in the stock market

**[08:48]** some perturbations in the stock market

**[08:48]** some perturbations in the stock market uh I think last week and then our model

**[08:51]** uh I think last week and then our model

**[08:51]** uh I think last week and then our model was able to keep it stable. So just like

**[08:53]** was able to keep it stable. So just like

**[08:54]** was able to keep it stable. So just like I said there's like environment noise

**[08:56]** I said there's like environment noise

**[08:56]** I said there's like environment noise there's no new information there's like

**[08:59]** there's no new information there's like

**[08:59]** there's no new information there's like yeah news it looks like there there's


### [09:00 - 10:00]

**[09:01]** yeah news it looks like there there's

**[09:01]** yeah news it looks like there there's like other trading policies and stuff

**[09:03]** like other trading policies and stuff

**[09:03]** like other trading policies and stuff like that but our model was able to uh

**[09:07]** like that but our model was able to uh

**[09:07]** like that but our model was able to uh to perform pretty stably in these kind

**[09:09]** to perform pretty stably in these kind

**[09:09]** to perform pretty stably in these kind of environments.

**[09:12]** of environments.

**[09:12]** of environments. And the third characteristic is our

**[09:14]** And the third characteristic is our

**[09:14]** And the third characteristic is our robust um generalization to many agent

**[09:17]** robust um generalization to many agent

**[09:17]** robust um generalization to many agent scaffolds which was supported by our

**[09:20]** scaffolds which was supported by our

**[09:20]** scaffolds which was supported by our perturbations in the data pipeline.

**[09:24]** perturbations in the data pipeline.

**[09:24]** perturbations in the data pipeline. So we want our agent to generalize. But

**[09:27]** So we want our agent to generalize. But

**[09:27]** So we want our agent to generalize. But what is agent generalization?

**[09:29]** what is agent generalization?

**[09:29]** what is agent generalization? At first we thought it was just tool

**[09:32]** At first we thought it was just tool

**[09:32]** At first we thought it was just tool scaling. We train the model with enough

**[09:34]** scaling. We train the model with enough

**[09:34]** scaling. We train the model with enough tools, various tools kind of new tools.

**[09:37]** tools, various tools kind of new tools.

**[09:37]** tools, various tools kind of new tools. we invent tools um and then it will just

**[09:39]** we invent tools um and then it will just

**[09:39]** we invent tools um and then it will just perform good on unseen tools. Well, that

**[09:43]** perform good on unseen tools. Well, that

**[09:43]** perform good on unseen tools. Well, that was kind of the truth. It worked at

**[09:44]** was kind of the truth. It worked at

**[09:44]** was kind of the truth. It worked at first. Uh but then we soon realized that

**[09:47]** first. Uh but then we soon realized that

**[09:47]** first. Uh but then we soon realized that if we perturb the environment a little

**[09:50]** if we perturb the environment a little

**[09:50]** if we perturb the environment a little bit, for example, we change another

**[09:52]** bit, for example, we change another

**[09:52]** bit, for example, we change another agent scaffold, then it doesn't

**[09:54]** agent scaffold, then it doesn't

**[09:54]** agent scaffold, then it doesn't generalize. So what is agent

**[09:56]** generalize. So what is agent

**[09:56]** generalize. So what is agent generalization?

**[09:58]** generalization?

**[09:58]** generalization? Well, we conclude that um it's


### [10:00 - 11:00]

**[10:00]** Well, we conclude that um it's

**[10:00]** Well, we conclude that um it's adaptation to perturbations across the

**[10:02]** adaptation to perturbations across the

**[10:02]** adaptation to perturbations across the model's entire uh operational space.

**[10:06]** model's entire uh operational space.

**[10:06]** model's entire uh operational space. If we uh think back what's the model's

**[10:10]** If we uh think back what's the model's

**[10:10]** If we uh think back what's the model's um operational space that we talked

**[10:12]** um operational space that we talked

**[10:12]** um operational space that we talked about it can be tool information it can

**[10:16]** about it can be tool information it can

**[10:16]** about it can be tool information it can be system prompts it can be user prompts

**[10:19]** be system prompts it can be user prompts

**[10:19]** be system prompts it can be user prompts they can all all be different they can

**[10:21]** they can all all be different they can

**[10:21]** they can all all be different they can be the chat template they can be the

**[10:23]** be the chat template they can be the

**[10:24]** be the chat template they can be the environment they can be the tool

**[10:25]** environment they can be the tool

**[10:25]** environment they can be the tool response. So what we did is that we

**[10:28]** response. So what we did is that we

**[10:28]** response. So what we did is that we designed and maintained perturbation

**[10:29]** designed and maintained perturbation

**[10:29]** designed and maintained perturbation pipelines of our data so that um our

**[10:32]** pipelines of our data so that um our

**[10:32]** pipelines of our data so that um our model can actually gen generalized to a

**[10:36]** model can actually gen generalized to a

**[10:36]** model can actually gen generalized to a lot of agent scaffolds.

**[10:39]** lot of agent scaffolds.

**[10:40]** lot of agent scaffolds. And the fourth characteristic that I

**[10:41]** And the fourth characteristic that I

**[10:42]** And the fourth characteristic that I want to mention is the multi- aent

**[10:44]** want to mention is the multi- aent

**[10:44]** want to mention is the multi- aent scalability

**[10:45]** scalability

**[10:45]** scalability um which is very possible with M2

**[10:48]** um which is very possible with M2

**[10:48]** um which is very possible with M2 because it's very small and cost

**[10:50]** because it's very small and cost

**[10:50]** because it's very small and cost effective.

**[10:57]** I have a couple of videos here. Um, this

**[10:57]** I have a couple of videos here. Um, this is M2 powered by our own Miniax agent uh


### [11:00 - 12:00]

**[11:01]** is M2 powered by our own Miniax agent uh

**[11:01]** is M2 powered by our own Miniax agent uh app. We actually have a QR code

**[11:04]** app. We actually have a QR code

**[11:04]** app. We actually have a QR code downside. So, if you want it, you can

**[11:05]** downside. So, if you want it, you can

**[11:06]** downside. So, if you want it, you can just scan and try it. So, it's like an

**[11:08]** just scan and try it. So, it's like an

**[11:08]** just scan and try it. So, it's like an agent app we we developed. And here we

**[11:11]** agent app we we developed. And here we

**[11:11]** agent app we we developed. And here we can see different copies of M2, right?

**[11:13]** can see different copies of M2, right?

**[11:13]** can see different copies of M2, right? It can do research. um it can write the

**[11:18]** It can do research. um it can write the

**[11:18]** It can do research. um it can write the write the research results and analyze

**[11:20]** write the research results and analyze

**[11:20]** write the research results and analyze it and put it in a re report. It can put

**[11:23]** it and put it in a re report. It can put

**[11:23]** it and put it in a re report. It can put it in some kind of front end

**[11:25]** it in some kind of front end

**[11:25]** it in some kind of front end illustration and they can work in

**[11:27]** illustration and they can work in

**[11:27]** illustration and they can work in parallel. So because it is so small um

**[11:30]** parallel. So because it is so small um

**[11:30]** parallel. So because it is so small um and so cost effective it can really um

**[11:33]** and so cost effective it can really um

**[11:33]** and so cost effective it can really um support those long run agentic tasks and

**[11:36]** support those long run agentic tasks and

**[11:36]** support those long run agentic tasks and tasks that maybe um require some kind of

**[11:39]** tasks that maybe um require some kind of

**[11:39]** tasks that maybe um require some kind of parallelism.

**[11:46]** So what's next right for Miniax M2 from

**[11:46]** So what's next right for Miniax M2 from what I've introduced we gathered

**[11:48]** what I've introduced we gathered

**[11:48]** what I've introduced we gathered environments um algorithms data expert

**[11:52]** environments um algorithms data expert

**[11:52]** environments um algorithms data expert values model architecture inference

**[11:55]** values model architecture inference

**[11:55]** values model architecture inference evaluation all these stuff to build a

**[11:57]** evaluation all these stuff to build a

**[11:57]** evaluation all these stuff to build a model um that was you know fast that was


### [12:00 - 13:00]

**[12:01]** model um that was you know fast that was

**[12:01]** model um that was you know fast that was uh intelligent that could use tools that

**[12:04]** uh intelligent that could use tools that

**[12:04]** uh intelligent that could use tools that generalizes

**[12:06]** generalizes

**[12:06]** generalizes what's next

**[12:09]** what's next

**[12:09]** what's next for um M2.1 1 and M3 were in the future

**[12:13]** for um M2.1 1 and M3 were in the future

**[12:13]** for um M2.1 1 and M3 were in the future we thinks of better coding maybe memory

**[12:16]** we thinks of better coding maybe memory

**[12:16]** we thinks of better coding maybe memory work context management proactive AI for

**[12:20]** work context management proactive AI for

**[12:20]** work context management proactive AI for workplace vertical experts and because

**[12:23]** workplace vertical experts and because

**[12:23]** workplace vertical experts and because we have those great audio generation

**[12:26]** we have those great audio generation

**[12:26]** we have those great audio generation video generation models maybe we can

**[12:29]** video generation models maybe we can

**[12:29]** video generation models maybe we can integrate them but all our mission is

**[12:32]** integrate them but all our mission is

**[12:32]** integrate them but all our mission is that we're committed to bring all these

**[12:33]** that we're committed to bring all these

**[12:34]** that we're committed to bring all these resources whatever is on the screen and

**[12:36]** resources whatever is on the screen and

**[12:36]** resources whatever is on the screen and maybe more yeah and values and put them

**[12:39]** maybe more yeah and values and put them

**[12:39]** maybe more yeah and values and put them all together to develop models for uh

**[12:43]** all together to develop models for uh

**[12:43]** all together to develop models for uh the community to use. So um we really

**[12:47]** the community to use. So um we really

**[12:47]** the community to use. So um we really need feedback from the community if

**[12:49]** need feedback from the community if

**[12:49]** need feedback from the community if possible because we want to build this

**[12:51]** possible because we want to build this

**[12:51]** possible because we want to build this together and you know this is kind of a

**[12:54]** together and you know this is kind of a

**[12:54]** together and you know this is kind of a race that everyone needs to participate

**[12:57]** race that everyone needs to participate

**[12:57]** race that everyone needs to participate and then um we com we are committed to


### [13:00 - 14:00]

**[13:01]** and then um we com we are committed to

**[13:01]** and then um we com we are committed to share it with the community. Yeah.

**[13:05]** share it with the community. Yeah.

**[13:05]** share it with the community. Yeah. And that's all the insight for today.

**[13:08]** And that's all the insight for today.

**[13:08]** And that's all the insight for today. Um, we really hope again we really hope

**[13:11]** Um, we really hope again we really hope

**[13:11]** Um, we really hope again we really hope you to try the model because it's pretty

**[13:13]** you to try the model because it's pretty

**[13:13]** you to try the model because it's pretty good. And then we can contact contact us

**[13:16]** good. And then we can contact contact us

**[13:16]** good. And then we can contact contact us up there. You can try the models by

**[13:18]** up there. You can try the models by

**[13:18]** up there. You can try the models by scanning the QR code. Yeah, basically

**[13:20]** scanning the QR code. Yeah, basically

**[13:20]** scanning the QR code. Yeah, basically that's it. Thank you all for listening.


