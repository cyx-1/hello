# Practical tactics to build reliable AI apps — Dmitry Kuchin, Multinear

**Video URL:** https://www.youtube.com/watch?v=-T6uZYYzkWw

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** Welcome everyone.

**[00:17]** Welcome everyone. I'm going to talk about practical

**[00:19]** I'm going to talk about practical

**[00:19]** I'm going to talk about practical tactics to build uh reliable AI

**[00:22]** tactics to build uh reliable AI

**[00:22]** tactics to build uh reliable AI applications and why nobody does it this

**[00:25]** applications and why nobody does it this

**[00:25]** applications and why nobody does it this way yet.

**[00:27]** way yet.

**[00:27]** way yet. Uh a little bit about myself or why you

**[00:29]** Uh a little bit about myself or why you

**[00:29]** Uh a little bit about myself or why you should trust me. Uh I have allowed 15

**[00:32]** should trust me. Uh I have allowed 15

**[00:32]** should trust me. Uh I have allowed 15 years as a startup co-founder and CTO.

**[00:36]** years as a startup co-founder and CTO.

**[00:36]** years as a startup co-founder and CTO. Uh I held executive positions for the

**[00:38]** Uh I held executive positions for the

**[00:38]** Uh I held executive positions for the last five years at uh several

**[00:40]** last five years at uh several

**[00:40]** last five years at uh several enterprises. uh but most importantly I

**[00:43]** enterprises. uh but most importantly I

**[00:43]** enterprises. uh but most importantly I spent last couple of years developing

**[00:46]** spent last couple of years developing

**[00:46]** spent last couple of years developing a lot of gen projects ranging from PC's

**[00:49]** a lot of gen projects ranging from PC's

**[00:49]** a lot of gen projects ranging from PC's to uh many production level uh solutions

**[00:55]** to uh many production level uh solutions

**[00:55]** to uh many production level uh solutions and helped some companies to get it done

**[00:59]** and helped some companies to get it done

**[00:59]** and helped some companies to get it done and uh I've learned or distilled a way


### [01:00 - 02:00]

**[01:02]** and uh I've learned or distilled a way

**[01:02]** and uh I've learned or distilled a way to uh make these applications reliable

**[01:06]** to uh make these applications reliable

**[01:06]** to uh make these applications reliable and there are quite a lot of uh tracks

**[01:10]** and there are quite a lot of uh tracks

**[01:10]** and there are quite a lot of uh tracks this uh uh this conference about evals

**[01:14]** this uh uh this conference about evals

**[01:14]** this uh uh this conference about evals and reliability but uh to my surprise

**[01:17]** and reliability but uh to my surprise

**[01:17]** and reliability but uh to my surprise nobody was talking about the most

**[01:20]** nobody was talking about the most

**[01:20]** nobody was talking about the most important things and uh we're going to

**[01:23]** important things and uh we're going to

**[01:23]** important things and uh we're going to talk about it right now.

**[01:26]** talk about it right now.

**[01:26]** talk about it right now. So uh standard software development life

**[01:28]** So uh standard software development life

**[01:28]** So uh standard software development life cycle is uh very standard uh simple uh

**[01:33]** cycle is uh very standard uh simple uh

**[01:33]** cycle is uh very standard uh simple uh you design your solution, you develop

**[01:35]** you design your solution, you develop

**[01:35]** you design your solution, you develop it, you test it and then eventually you

**[01:37]** it, you test it and then eventually you

**[01:37]** it, you test it and then eventually you deploy it. And uh when people start

**[01:41]** deploy it. And uh when people start

**[01:41]** deploy it. And uh when people start doing uh PC with AI

**[01:45]** doing uh PC with AI

**[01:45]** doing uh PC with AI it sounds simple like you can very

**[01:48]** it sounds simple like you can very

**[01:48]** it sounds simple like you can very easily do you have some prompt and uh

**[01:51]** easily do you have some prompt and uh

**[01:51]** easily do you have some prompt and uh models are very capable but then you

**[01:54]** models are very capable but then you

**[01:54]** models are very capable but then you start uh facing some uh unexpected

**[01:57]** start uh facing some uh unexpected

**[01:57]** start uh facing some uh unexpected challenges

**[01:58]** challenges

**[01:58]** challenges uh actually like you can easily do a PC


### [02:00 - 03:00]

**[02:01]** uh actually like you can easily do a PC

**[02:02]** uh actually like you can easily do a PC that works 50% of the time uh but we're

**[02:05]** that works 50% of the time uh but we're

**[02:05]** that works 50% of the time uh but we're like making it do the same reliable work

**[02:08]** like making it do the same reliable work

**[02:08]** like making it do the same reliable work the Rest of the 50% is very hard uh

**[02:11]** the Rest of the 50% is very hard uh

**[02:11]** the Rest of the 50% is very hard uh because models are nondeterministic

**[02:14]** because models are nondeterministic

**[02:14]** because models are nondeterministic and uh it starts requiring uh a data

**[02:18]** and uh it starts requiring uh a data

**[02:18]** and uh it starts requiring uh a data science approach uh continuous

**[02:20]** science approach uh continuous

**[02:20]** science approach uh continuous experimentation you need to try this

**[02:22]** experimentation you need to try this

**[02:22]** experimentation you need to try this prompt you need to try that model you

**[02:23]** prompt you need to try that model you

**[02:23]** prompt you need to try that model you need to try this approach etc etc and uh

**[02:28]** need to try this approach etc etc and uh

**[02:28]** need to try this approach etc etc and uh everything in your solution everything

**[02:30]** everything in your solution everything

**[02:30]** everything in your solution everything that uh represents your solution which

**[02:32]** that uh represents your solution which

**[02:32]** that uh represents your solution which is your code your logic uh the prompts

**[02:35]** is your code your logic uh the prompts

**[02:35]** is your code your logic uh the prompts that you use the the models that you use

**[02:37]** that you use the the models that you use

**[02:37]** that you use the the models that you use the the data that you base your solution

**[02:39]** the the data that you base your solution

**[02:39]** the the data that you base your solution on changing anything of that impacts

**[02:43]** on changing anything of that impacts

**[02:43]** on changing anything of that impacts your uh solution in unexpected ways.

**[02:55]** Um people very often come to this uh to

**[02:55]** Um people very often come to this uh to try solving this with the wrong

**[02:57]** try solving this with the wrong

**[02:57]** try solving this with the wrong approach. They start with a data science


### [03:00 - 04:00]

**[03:00]** approach. They start with a data science

**[03:00]** approach. They start with a data science metrics. They like it sounds reasonable,

**[03:04]** metrics. They like it sounds reasonable,

**[03:04]** metrics. They like it sounds reasonable, right? So it requires data science

**[03:05]** right? So it requires data science

**[03:05]** right? So it requires data science approach of experimentation and uh

**[03:08]** approach of experimentation and uh

**[03:08]** approach of experimentation and uh people start measuring groundness,

**[03:10]** people start measuring groundness,

**[03:10]** people start measuring groundness, factuality, bias and other uh metrics

**[03:14]** factuality, bias and other uh metrics

**[03:14]** factuality, bias and other uh metrics that don't really help you to understand

**[03:18]** that don't really help you to understand

**[03:18]** that don't really help you to understand uh is your solution uh working the right

**[03:21]** uh is your solution uh working the right

**[03:21]** uh is your solution uh working the right way? Does it uh does your latest change

**[03:25]** way? Does it uh does your latest change

**[03:25]** way? Does it uh does your latest change improved uh your solution in the right

**[03:28]** improved uh your solution in the right

**[03:28]** improved uh your solution in the right way for your users? uh for example I've

**[03:31]** way for your users? uh for example I've

**[03:31]** way for your users? uh for example I've been talking to an ex-colague that are

**[03:34]** been talking to an ex-colague that are

**[03:34]** been talking to an ex-colague that are building a customer support bot at

**[03:35]** building a customer support bot at

**[03:35]** building a customer support bot at tweaks I asked him how do you know that

**[03:38]** tweaks I asked him how do you know that

**[03:38]** tweaks I asked him how do you know that your solution is working well he started

**[03:41]** your solution is working well he started

**[03:41]** your solution is working well he started talking about factuality and other data

**[03:43]** talking about factuality and other data

**[03:43]** talking about factuality and other data science metrics

**[03:45]** science metrics

**[03:45]** science metrics u that's again I started to dig deeper

**[03:49]** u that's again I started to dig deeper

**[03:49]** u that's again I started to dig deeper and then we just uh together figure out

**[03:52]** and then we just uh together figure out

**[03:52]** and then we just uh together figure out that the most important metric for them

**[03:54]** that the most important metric for them

**[03:54]** that the most important metric for them is uh the rate of moving from AI I

**[03:59]** is uh the rate of moving from AI I

**[03:59]** is uh the rate of moving from AI I support bot like escalation to a human


### [04:00 - 05:00]

**[04:02]** support bot like escalation to a human

**[04:02]** support bot like escalation to a human support.

**[04:03]** support.

**[04:03]** support. If uh your solution uh hasn't able to

**[04:06]** If uh your solution uh hasn't able to

**[04:06]** If uh your solution uh hasn't able to answer the user with all this factuality

**[04:09]** answer the user with all this factuality

**[04:09]** answer the user with all this factuality like it could be super grounded but

**[04:11]** like it could be super grounded but

**[04:11]** like it could be super grounded but still not provide the right answer that

**[04:14]** still not provide the right answer that

**[04:14]** still not provide the right answer that the user expects and uh this is what you

**[04:17]** the user expects and uh this is what you

**[04:17]** the user expects and uh this is what you actually need to test.

**[04:20]** actually need to test.

**[04:20]** actually need to test. Um and my experience was to start with

**[04:26]** Um and my experience was to start with

**[04:26]** Um and my experience was to start with real world scenarios. So basically you

**[04:28]** real world scenarios. So basically you

**[04:28]** real world scenarios. So basically you need to reverse engineer your metrics

**[04:30]** need to reverse engineer your metrics

**[04:30]** need to reverse engineer your metrics and your metrics should be very very

**[04:33]** and your metrics should be very very

**[04:34]** and your metrics should be very very specific to what your end goal. So they

**[04:37]** specific to what your end goal. So they

**[04:37]** specific to what your end goal. So they should come from a product experience

**[04:40]** should come from a product experience

**[04:40]** should come from a product experience from business outcomes. Uh if your

**[04:43]** from business outcomes. Uh if your

**[04:43]** from business outcomes. Uh if your solution is customer support bot, you

**[04:44]** solution is customer support bot, you

**[04:44]** solution is customer support bot, you need to figure out what your users want

**[04:46]** need to figure out what your users want

**[04:46]** need to figure out what your users want and uh how you can mimic it. And instead

**[04:50]** and uh how you can mimic it. And instead

**[04:50]** and uh how you can mimic it. And instead of measuring something u average or

**[04:53]** of measuring something u average or

**[04:53]** of measuring something u average or something generic, you need to measure a

**[04:56]** something generic, you need to measure a

**[04:56]** something generic, you need to measure a very specific criterias.

**[04:58]** very specific criterias.

**[04:58]** very specific criterias. Uh cuz universal valves don't really


### [05:00 - 06:00]

**[05:01]** Uh cuz universal valves don't really

**[05:01]** Uh cuz universal valves don't really work.

**[05:03]** work.

**[05:03]** work. How do we do it? Uh so for example,

**[05:06]** How do we do it? Uh so for example,

**[05:06]** How do we do it? Uh so for example, customer support bot, which is by the

**[05:07]** customer support bot, which is by the

**[05:07]** customer support bot, which is by the way one of the hardest uh things to do

**[05:11]** way one of the hardest uh things to do

**[05:11]** way one of the hardest uh things to do properly. uh let's say I have a bank and

**[05:15]** properly. uh let's say I have a bank and

**[05:15]** properly. uh let's say I have a bank and uh bank has FAQ materials

**[05:19]** uh bank has FAQ materials

**[05:19]** uh bank has FAQ materials which contain including like how do you

**[05:21]** which contain including like how do you

**[05:21]** which contain including like how do you reset your password?

**[05:23]** reset your password?

**[05:24]** reset your password? Um so what I usually do when I help my

**[05:27]** Um so what I usually do when I help my

**[05:27]** Um so what I usually do when I help my uh like companies that I help them to

**[05:30]** uh like companies that I help them to

**[05:30]** uh like companies that I help them to build uh AI solutions we start with uh

**[05:34]** build uh AI solutions we start with uh

**[05:34]** build uh AI solutions we start with uh reverse engineering like how do we

**[05:36]** reverse engineering like how do we

**[05:36]** reverse engineering like how do we create the valves based on that. So in

**[05:38]** create the valves based on that. So in

**[05:38]** create the valves based on that. So in this case I use LLM and in most cases I

**[05:41]** this case I use LLM and in most cases I

**[05:41]** this case I use LLM and in most cases I use LLM to come up with right

**[05:44]** use LLM to come up with right

**[05:44]** use LLM to come up with right evaluations. So here I can take say 01

**[05:47]** evaluations. So here I can take say 01

**[05:48]** evaluations. So here I can take say 01 uh 03 now uh and just reverse engineer

**[05:52]** uh 03 now uh and just reverse engineer

**[05:52]** uh 03 now uh and just reverse engineer what should be the user question uh that

**[05:55]** what should be the user question uh that

**[05:55]** what should be the user question uh that we know to answer based on these

**[05:57]** we know to answer based on these

**[05:57]** we know to answer based on these materials and what should be the

**[05:59]** materials and what should be the

**[05:59]** materials and what should be the specific criteria that uh these


### [06:00 - 07:00]

**[06:01]** specific criteria that uh these

**[06:02]** specific criteria that uh these materials are providing an answer for

**[06:05]** materials are providing an answer for

**[06:05]** materials are providing an answer for and some of these criteria are quite

**[06:07]** and some of these criteria are quite

**[06:07]** and some of these criteria are quite important. So for example here it says

**[06:08]** important. So for example here it says

**[06:08]** important. So for example here it says that uh uh as part of the thing you you

**[06:12]** that uh uh as part of the thing you you

**[06:12]** that uh uh as part of the thing you you need to receive a mobile validation. So

**[06:14]** need to receive a mobile validation. So

**[06:14]** need to receive a mobile validation. So you receive a SMS code and uh it says

**[06:16]** you receive a SMS code and uh it says

**[06:16]** you receive a SMS code and uh it says that if you uh don't have a mobile

**[06:19]** that if you uh don't have a mobile

**[06:19]** that if you uh don't have a mobile number then you can reach uh support etc

**[06:23]** number then you can reach uh support etc

**[06:23]** number then you can reach uh support etc etc. Uh if some of that information is

**[06:26]** etc. Uh if some of that information is

**[06:26]** etc. Uh if some of that information is missing from the answer the answer would

**[06:29]** missing from the answer the answer would

**[06:29]** missing from the answer the answer would not be correct.

**[06:31]** not be correct.

**[06:31]** not be correct. You need to be very specific about what

**[06:33]** You need to be very specific about what

**[06:33]** You need to be very specific about what exact information you need to see in the

**[06:36]** exact information you need to see in the

**[06:36]** exact information you need to see in the answer and that information is very

**[06:38]** answer and that information is very

**[06:38]** answer and that information is very specific to that specific question. So

**[06:40]** specific to that specific question. So

**[06:40]** specific to that specific question. So you need to build like lots of evals

**[06:44]** you need to build like lots of evals

**[06:44]** you need to build like lots of evals uh from the materials in this case uh

**[06:48]** uh from the materials in this case uh

**[06:48]** uh from the materials in this case uh that mimic specific user questions that

**[06:52]** that mimic specific user questions that

**[06:52]** that mimic specific user questions that uh you need to be able to answer for. Uh

**[06:55]** uh you need to be able to answer for. Uh

**[06:55]** uh you need to be able to answer for. Uh how do we do it? Usually again I work

**[06:57]** how do we do it? Usually again I work

**[06:57]** how do we do it? Usually again I work with uh smart models like O3 uh and I uh


### [07:00 - 08:00]

**[07:02]** with uh smart models like O3 uh and I uh

**[07:02]** with uh smart models like O3 uh and I uh provided enough context. I provided

**[07:05]** provided enough context. I provided

**[07:05]** provided enough context. I provided which personas are we trying to

**[07:07]** which personas are we trying to

**[07:07]** which personas are we trying to represent because you can make ask the

**[07:09]** represent because you can make ask the

**[07:09]** represent because you can make ask the same question in uh completely different

**[07:12]** same question in uh completely different

**[07:12]** same question in uh completely different ways depending on who is the persona

**[07:14]** ways depending on who is the persona

**[07:14]** ways depending on who is the persona asking uh yet you would expect exactly

**[07:18]** asking uh yet you would expect exactly

**[07:18]** asking uh yet you would expect exactly the same answer. So you need to account

**[07:19]** the same answer. So you need to account

**[07:19]** the same answer. So you need to account for it.

**[07:22]** for it.

**[07:22]** for it. Um so this is uh an example from uh the

**[07:26]** Um so this is uh an example from uh the

**[07:26]** Um so this is uh an example from uh the open source platform that we have that

**[07:28]** open source platform that we have that

**[07:28]** open source platform that we have that uh just helps to get it done. So if you

**[07:32]** uh just helps to get it done. So if you

**[07:32]** uh just helps to get it done. So if you look it up multineer I'm not trying to

**[07:34]** look it up multineer I'm not trying to

**[07:34]** look it up multineer I'm not trying to sell you anything. I'm not trying to

**[07:35]** sell you anything. I'm not trying to

**[07:36]** sell you anything. I'm not trying to like vendor lock in or whatever. It's

**[07:38]** like vendor lock in or whatever. It's

**[07:38]** like vendor lock in or whatever. It's completely open source and if needed I

**[07:41]** completely open source and if needed I

**[07:41]** completely open source and if needed I can just recreate it in a couple of days

**[07:43]** can just recreate it in a couple of days

**[07:43]** can just recreate it in a couple of days now with cursor. The point is in the

**[07:45]** now with cursor. The point is in the

**[07:45]** now with cursor. The point is in the approach not in the platform. Uh so for

**[07:48]** approach not in the platform. Uh so for

**[07:48]** approach not in the platform. Uh so for example here we see that very same

**[07:51]** example here we see that very same

**[07:51]** example here we see that very same question um how do I reset my password

**[07:54]** question um how do I reset my password

**[07:54]** question um how do I reset my password you see the what was the input what was

**[07:57]** you see the what was the input what was

**[07:57]** you see the what was the input what was the output and uh that specific criteria


### [08:00 - 09:00]

**[08:01]** the output and uh that specific criteria

**[08:01]** the output and uh that specific criteria that I measure it uh that specific

**[08:05]** that I measure it uh that specific

**[08:05]** that I measure it uh that specific question how do I know if the answer is

**[08:08]** question how do I know if the answer is

**[08:08]** question how do I know if the answer is correct and now I can just reiterate and

**[08:11]** correct and now I can just reiterate and

**[08:11]** correct and now I can just reiterate and generate like 50 different variations of

**[08:14]** generate like 50 different variations of

**[08:14]** generate like 50 different variations of the same question and see if I still get

**[08:17]** the same question and see if I still get

**[08:17]** the same question and see if I still get the right answer if the answer matches

**[08:19]** the right answer if the answer matches

**[08:19]** the right answer if the answer matches all the checklist that I have for that

**[08:22]** all the checklist that I have for that

**[08:22]** all the checklist that I have for that specific answer.

**[08:25]** specific answer.

**[08:25]** specific answer. Um how the process usually works

**[08:28]** Um how the process usually works

**[08:28]** Um how the process usually works um so contrary to like regular approach

**[08:31]** um so contrary to like regular approach

**[08:32]** um so contrary to like regular approach you build your evals not at the end of

**[08:34]** you build your evals not at the end of

**[08:34]** you build your evals not at the end of the process but in the very beginning of

**[08:36]** the process but in the very beginning of

**[08:36]** the process but in the very beginning of the process. So you just build your

**[08:39]** the process. So you just build your

**[08:39]** the process. So you just build your first version of the PC. You define the

**[08:44]** first version of the PC. You define the

**[08:44]** first version of the PC. You define the first version of your tests evaluations.

**[08:47]** first version of your tests evaluations.

**[08:47]** first version of your tests evaluations. You run them and you see what's going

**[08:49]** You run them and you see what's going

**[08:49]** You run them and you see what's going on. You you will see that uh in some

**[08:51]** on. You you will see that uh in some

**[08:51]** on. You you will see that uh in some cases it will fail. Uh in some cases it

**[08:53]** cases it will fail. Uh in some cases it

**[08:54]** cases it will fail. Uh in some cases it will succeed. What's important is to to

**[08:57]** will succeed. What's important is to to

**[08:57]** will succeed. What's important is to to look at the details not just see the

**[08:59]** look at the details not just see the

**[08:59]** look at the details not just see the average numbers. The average numbers


### [09:00 - 10:00]

**[09:00]** average numbers. The average numbers

**[09:00]** average numbers. The average numbers won't tell you anything. Uh won't tell

**[09:04]** won't tell you anything. Uh won't tell

**[09:04]** won't tell you anything. Uh won't tell you how to improve it. If you actually

**[09:06]** you how to improve it. If you actually

**[09:06]** you how to improve it. If you actually look at the details of each evaluation,

**[09:09]** look at the details of each evaluation,

**[09:09]** look at the details of each evaluation, you'll see exactly why it's failing. It

**[09:11]** you'll see exactly why it's failing. It

**[09:11]** you'll see exactly why it's failing. It could be failing um because your test is

**[09:14]** could be failing um because your test is

**[09:14]** could be failing um because your test is not defined correctly. It could be

**[09:16]** not defined correctly. It could be

**[09:16]** not defined correctly. It could be failing because your uh solution is not

**[09:18]** failing because your uh solution is not

**[09:18]** failing because your uh solution is not working as it should be. And like in

**[09:21]** working as it should be. And like in

**[09:21]** working as it should be. And like in order to do it, you may need to uh to do

**[09:24]** order to do it, you may need to uh to do

**[09:24]** order to do it, you may need to uh to do a change in like you may change a model,

**[09:27]** a change in like you may change a model,

**[09:27]** a change in like you may change a model, you may change something on in your

**[09:28]** you may change something on in your

**[09:28]** you may change something on in your logic, you may change a prompt or the

**[09:31]** logic, you may change a prompt or the

**[09:31]** logic, you may change a prompt or the data that you use in order to uh answer

**[09:34]** data that you use in order to uh answer

**[09:34]** data that you use in order to uh answer a question in our example.

**[09:37]** a question in our example.

**[09:37]** a question in our example. And uh basically what you do now is

**[09:39]** And uh basically what you do now is

**[09:40]** And uh basically what you do now is experimentation. So you you start

**[09:41]** experimentation. So you you start

**[09:42]** experimentation. So you you start running your experiment. You change

**[09:43]** running your experiment. You change

**[09:43]** running your experiment. You change something. you you need to define these

**[09:46]** something. you you need to define these

**[09:46]** something. you you need to define these tests in a way that will uh help you to

**[09:49]** tests in a way that will uh help you to

**[09:49]** tests in a way that will uh help you to make an educated guess on uh what you

**[09:53]** make an educated guess on uh what you

**[09:53]** make an educated guess on uh what you need to change in order to to do it. In

**[09:55]** need to change in order to to do it. In

**[09:56]** need to change in order to to do it. In some cases it will work in some cases it

**[09:57]** some cases it will work in some cases it

**[09:57]** some cases it will work in some cases it won't. But even if it works uh let's say


### [10:00 - 11:00]

**[10:01]** won't. But even if it works uh let's say

**[10:01]** won't. But even if it works uh let's say you change something in your prompt and

**[10:03]** you change something in your prompt and

**[10:03]** you change something in your prompt and it fixed this test. In my experience, in

**[10:06]** it fixed this test. In my experience, in

**[10:06]** it fixed this test. In my experience, in many cases, it breaks uh something that

**[10:08]** many cases, it breaks uh something that

**[10:08]** many cases, it breaks uh something that used to work before. Uh like you you you

**[10:11]** used to work before. Uh like you you you

**[10:12]** used to work before. Uh like you you you have constant regressions and if you

**[10:14]** have constant regressions and if you

**[10:14]** have constant regressions and if you don't have these evaluations, there is

**[10:16]** don't have these evaluations, there is

**[10:16]** don't have these evaluations, there is no way you'll be able to catch it on

**[10:17]** no way you'll be able to catch it on

**[10:18]** no way you'll be able to catch it on time.

**[10:19]** time.

**[10:19]** time. So this is hugely important and what

**[10:22]** So this is hugely important and what

**[10:22]** So this is hugely important and what actually happens is that again you build

**[10:24]** actually happens is that again you build

**[10:24]** actually happens is that again you build your first version. You build your first

**[10:26]** your first version. You build your first

**[10:26]** your first version. You build your first version of the vows uh you match them

**[10:28]** version of the vows uh you match them

**[10:28]** version of the vows uh you match them you run these valves you improve

**[10:30]** you run these valves you improve

**[10:30]** you run these valves you improve something you improve your vows or maybe

**[10:32]** something you improve your vows or maybe

**[10:32]** something you improve your vows or maybe add more evaluations and then you like

**[10:35]** add more evaluations and then you like

**[10:35]** add more evaluations and then you like continuously improve it until you reach

**[10:38]** continuously improve it until you reach

**[10:38]** continuously improve it until you reach some point where you are satisfied with

**[10:41]** some point where you are satisfied with

**[10:41]** some point where you are satisfied with your valves for this specific solution

**[10:43]** your valves for this specific solution

**[10:43]** your valves for this specific solution for that specific point of time. And

**[10:47]** for that specific point of time. And

**[10:47]** for that specific point of time. And what actually happened is that you you

**[10:49]** what actually happened is that you you

**[10:49]** what actually happened is that you you you got your baseline, you got your

**[10:50]** you got your baseline, you got your

**[10:50]** you got your baseline, you got your benchmark that uh now you can start

**[10:53]** benchmark that uh now you can start

**[10:53]** benchmark that uh now you can start optimizing and uh you have the

**[10:56]** optimizing and uh you have the

**[10:56]** optimizing and uh you have the confidence that the tests should be

**[10:59]** confidence that the tests should be


### [11:00 - 12:00]

**[11:00]** confidence that the tests should be working. So now you can try another

**[11:02]** working. So now you can try another

**[11:02]** working. So now you can try another model. Let's say well what how can I try

**[11:05]** model. Let's say well what how can I try

**[11:05]** model. Let's say well what how can I try to see if 40 mini will work the same way

**[11:09]** to see if 40 mini will work the same way

**[11:09]** to see if 40 mini will work the same way with 40 or not? uh can I use a graph rag

**[11:13]** with 40 or not? uh can I use a graph rag

**[11:13]** with 40 or not? uh can I use a graph rag or can I try a simpler solution?

**[11:16]** or can I try a simpler solution?

**[11:16]** or can I try a simpler solution? uh should I have uh to use agentic

**[11:18]** uh should I have uh to use agentic

**[11:18]** uh should I have uh to use agentic approach that like maybe better but uh

**[11:22]** approach that like maybe better but uh

**[11:22]** approach that like maybe better but uh requires more time more uh inference

**[11:26]** requires more time more uh inference

**[11:26]** requires more time more uh inference cost etc or should I try to simplify the

**[11:28]** cost etc or should I try to simplify the

**[11:28]** cost etc or should I try to simplify the logic or maybe I can simplify the logic

**[11:30]** logic or maybe I can simplify the logic

**[11:30]** logic or maybe I can simplify the logic for a specific portion of the

**[11:32]** for a specific portion of the

**[11:32]** for a specific portion of the application etc etc having this

**[11:35]** application etc etc having this

**[11:35]** application etc etc having this benchmark uh allows you to do all these

**[11:38]** benchmark uh allows you to do all these

**[11:38]** benchmark uh allows you to do all these experimentations uh with confidence but

**[11:41]** experimentations uh with confidence but

**[11:41]** experimentations uh with confidence but again the the most important part is

**[11:42]** again the the most important part is

**[11:42]** again the the most important part is like how do you reach this benchmark

**[11:45]** like how do you reach this benchmark

**[11:46]** like how do you reach this benchmark And uh while the approach is uh pretty

**[11:49]** And uh while the approach is uh pretty

**[11:49]** And uh while the approach is uh pretty much the same, the evaluations that you

**[11:52]** much the same, the evaluations that you

**[11:52]** much the same, the evaluations that you need to build and how do you build your

**[11:53]** need to build and how do you build your

**[11:53]** need to build and how do you build your evaluations are completely different

**[11:55]** evaluations are completely different

**[11:55]** evaluations are completely different depending on the solution that you need

**[11:57]** depending on the solution that you need

**[11:57]** depending on the solution that you need to build because uh the models are super


### [12:00 - 13:00]

**[12:01]** to build because uh the models are super

**[12:01]** to build because uh the models are super capable right now. Uh so they allow you

**[12:03]** capable right now. Uh so they allow you

**[12:03]** capable right now. Uh so they allow you to build a huge variety of uh solutions

**[12:06]** to build a huge variety of uh solutions

**[12:06]** to build a huge variety of uh solutions but each and every solution is quite uh

**[12:09]** but each and every solution is quite uh

**[12:09]** but each and every solution is quite uh different in terms of how do you uh

**[12:10]** different in terms of how do you uh

**[12:10]** different in terms of how do you uh evaluate it. uh for support bot you

**[12:14]** evaluate it. uh for support bot you

**[12:14]** evaluate it. uh for support bot you usually typically use LM as a judge as I

**[12:16]** usually typically use LM as a judge as I

**[12:16]** usually typically use LM as a judge as I uh made an example if you're building

**[12:19]** uh made an example if you're building

**[12:19]** uh made an example if you're building text to SQL or text to graph database

**[12:22]** text to SQL or text to graph database

**[12:22]** text to SQL or text to graph database then uh to my experience the best way is

**[12:25]** then uh to my experience the best way is

**[12:25]** then uh to my experience the best way is to create a mock database that

**[12:27]** to create a mock database that

**[12:27]** to create a mock database that represents the um whatever uh database

**[12:31]** represents the um whatever uh database

**[12:31]** represents the um whatever uh database or databases that you need your solution

**[12:34]** or databases that you need your solution

**[12:34]** or databases that you need your solution to work with they represent the same

**[12:36]** to work with they represent the same

**[12:36]** to work with they represent the same schema and you have a mock data so you

**[12:38]** schema and you have a mock data so you

**[12:38]** schema and you have a mock data so you know exactly uh what should expect on

**[12:41]** know exactly uh what should expect on

**[12:41]** know exactly uh what should expect on specific questions. Um if you need to

**[12:44]** specific questions. Um if you need to

**[12:44]** specific questions. Um if you need to build some classifier for call center

**[12:47]** build some classifier for call center

**[12:47]** build some classifier for call center conversations then your uh tests are

**[12:50]** conversations then your uh tests are

**[12:50]** conversations then your uh tests are like simple match whenever this is this

**[12:51]** like simple match whenever this is this

**[12:52]** like simple match whenever this is this is the right rubric or not. Uh and the

**[12:54]** is the right rubric or not. Uh and the

**[12:54]** is the right rubric or not. Uh and the same appro uh approach applies to guard

**[12:57]** same appro uh approach applies to guard

**[12:57]** same appro uh approach applies to guard rails. So uh getting back to the support


### [13:00 - 14:00]

**[13:00]** rails. So uh getting back to the support

**[13:00]** rails. So uh getting back to the support to the uh example of the customer

**[13:02]** to the uh example of the customer

**[13:02]** to the uh example of the customer support bot uh guardrails you need to

**[13:05]** support bot uh guardrails you need to

**[13:05]** support bot uh guardrails you need to cover uh questions that should not be

**[13:08]** cover uh questions that should not be

**[13:08]** cover uh questions that should not be answered or questions that should be

**[13:09]** answered or questions that should be

**[13:10]** answered or questions that should be answered in different ways or questions

**[13:11]** answered in different ways or questions

**[13:11]** answered in different ways or questions that uh uh the answers are not in the

**[13:14]** that uh uh the answers are not in the

**[13:14]** that uh uh the answers are not in the material. So all of these you can put

**[13:16]** material. So all of these you can put

**[13:16]** material. So all of these you can put into your benchmark just different type

**[13:18]** into your benchmark just different type

**[13:18]** into your benchmark just different type of benchmark but it's pretty much the

**[13:20]** of benchmark but it's pretty much the

**[13:20]** of benchmark but it's pretty much the same approach.

**[13:23]** same approach.

**[13:23]** same approach. Uh so just to reiterate uh the key

**[13:26]** Uh so just to reiterate uh the key

**[13:26]** Uh so just to reiterate uh the key takeaways, you need to evaluate your

**[13:28]** takeaways, you need to evaluate your

**[13:28]** takeaways, you need to evaluate your apps the way your users actually use

**[13:30]** apps the way your users actually use

**[13:30]** apps the way your users actually use them. Um and uh avoid abstract metrics

**[13:35]** them. Um and uh avoid abstract metrics

**[13:35]** them. Um and uh avoid abstract metrics uh because these abstract connectors

**[13:37]** uh because these abstract connectors

**[13:37]** uh because these abstract connectors don't really measure anything important.

**[13:39]** don't really measure anything important.

**[13:39]** don't really measure anything important. Uh and the approach is uh through

**[13:41]** Uh and the approach is uh through

**[13:41]** Uh and the approach is uh through experimentation. So you run these

**[13:43]** experimentation. So you run these

**[13:43]** experimentation. So you run these evaluations frequently. you that allows

**[13:45]** evaluations frequently. you that allows

**[13:45]** evaluations frequently. you that allows you to have rapid progress with uh less

**[13:49]** you to have rapid progress with uh less

**[13:49]** you to have rapid progress with uh less regressions because testing frequently

**[13:52]** regressions because testing frequently

**[13:52]** regressions because testing frequently help you to to catch these surprises. Uh

**[13:55]** help you to to catch these surprises. Uh

**[13:55]** help you to to catch these surprises. Uh but most importantly what you get if you

**[13:58]** but most importantly what you get if you

**[13:58]** but most importantly what you get if you divi define your evaluations correctly,


### [14:00 - 15:00]

**[14:00]** divi define your evaluations correctly,

**[14:00]** divi define your evaluations correctly, you get your solution pretty much uh as

**[14:03]** you get your solution pretty much uh as

**[14:04]** you get your solution pretty much uh as kind of explainable AI because you know

**[14:06]** kind of explainable AI because you know

**[14:06]** kind of explainable AI because you know exactly what it does, you know exactly

**[14:08]** exactly what it does, you know exactly

**[14:08]** exactly what it does, you know exactly how it does it if you test it the right

**[14:10]** how it does it if you test it the right

**[14:10]** how it does it if you test it the right way.

**[14:13]** way.

**[14:13]** way. Thank you very much. Uh take a look at

**[14:16]** Thank you very much. Uh take a look at

**[14:16]** Thank you very much. Uh take a look at multineer uh that's a platform that you

**[14:20]** multineer uh that's a platform that you

**[14:20]** multineer uh that's a platform that you can use to uh run these evaluations. You

**[14:23]** can use to uh run these evaluations. You

**[14:24]** can use to uh run these evaluations. You can totally use any other platform. The

**[14:26]** can totally use any other platform. The

**[14:26]** can totally use any other platform. The approach is quite simple. It doesn't

**[14:28]** approach is quite simple. It doesn't

**[14:28]** approach is quite simple. It doesn't require any specific platform. Uh I've

**[14:31]** require any specific platform. Uh I've

**[14:31]** require any specific platform. Uh I've built multin just because no other

**[14:34]** built multin just because no other

**[14:34]** built multin just because no other platform helped me to do it this way to

**[14:36]** platform helped me to do it this way to

**[14:36]** platform helped me to do it this way to to help me with the process of

**[14:38]** to help me with the process of

**[14:38]** to help me with the process of evaluation like end to end. Um, I'm

**[14:42]** evaluation like end to end. Um, I'm

**[14:42]** evaluation like end to end. Um, I'm working on a startup that does reliable

**[14:43]** working on a startup that does reliable

**[14:44]** working on a startup that does reliable AI automation right now. Um, and uh,

**[14:47]** AI automation right now. Um, and uh,

**[14:47]** AI automation right now. Um, and uh, yeah, thank you very much.

**[14:49]** yeah, thank you very much.

**[14:49]** yeah, thank you very much. [Music]


