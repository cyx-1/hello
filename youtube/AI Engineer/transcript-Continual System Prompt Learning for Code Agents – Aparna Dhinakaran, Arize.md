# Continual System Prompt Learning for Code Agents – Aparna Dhinakaran, Arize

**Video URL:** https://youtu.be/pP_dSNz_EdQ

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** Hi everyone. Thanks so much for coming.

**[00:23]** Hi everyone. Thanks so much for coming. Um, well, today I'm excited. We're going

**[00:24]** Um, well, today I'm excited. We're going

**[00:24]** Um, well, today I'm excited. We're going to talk a little bit about prompt

**[00:25]** to talk a little bit about prompt

**[00:26]** to talk a little bit about prompt learning and how to use that with eval.

**[00:29]** learning and how to use that with eval.

**[00:29]** learning and how to use that with eval. uh if any of you guys um are spending a

**[00:33]** uh if any of you guys um are spending a

**[00:33]** uh if any of you guys um are spending a lot of time thinking about the frontier

**[00:34]** lot of time thinking about the frontier

**[00:34]** lot of time thinking about the frontier coding models, I think there's so much

**[00:36]** coding models, I think there's so much

**[00:36]** coding models, I think there's so much attention on on them. But just what's

**[00:40]** attention on on them. But just what's

**[00:40]** attention on on them. But just what's not so obvious is how much time is

**[00:42]** not so obvious is how much time is

**[00:42]** not so obvious is how much time is actually spent uh on the system prompts

**[00:45]** actually spent uh on the system prompts

**[00:45]** actually spent uh on the system prompts uh for those building these coding

**[00:47]** uh for those building these coding

**[00:47]** uh for those building these coding agents. So here's actually a look um

**[00:49]** agents. So here's actually a look um

**[00:49]** agents. So here's actually a look um this is a tweet that went viral about

**[00:51]** this is a tweet that went viral about

**[00:51]** this is a tweet that went viral about the whole system prompt uh of Claude

**[00:54]** the whole system prompt uh of Claude

**[00:54]** the whole system prompt uh of Claude that's been leaked. I'm sure you know

**[00:55]** that's been leaked. I'm sure you know

**[00:55]** that's been leaked. I'm sure you know they've changed it since then. Um, but

**[00:58]** they've changed it since then. Um, but

**[00:58]** they've changed it since then. Um, but you can actually see that Claude,

**[00:59]** you can actually see that Claude,

**[00:59]** you can actually see that Claude, there's cursor, there's Clyde. Um, and


### [01:00 - 02:00]

**[01:01]** there's cursor, there's Clyde. Um, and

**[01:01]** there's cursor, there's Clyde. Um, and just the length of the actual system

**[01:03]** just the length of the actual system

**[01:03]** just the length of the actual system prompt um, for each one of these. And I

**[01:06]** prompt um, for each one of these. And I

**[01:06]** prompt um, for each one of these. And I think what's not as obvious is these

**[01:08]** think what's not as obvious is these

**[01:08]** think what's not as obvious is these actually aren't just static. They are

**[01:11]** actually aren't just static. They are

**[01:11]** actually aren't just static. They are repeatedly iterated on. And it's such an

**[01:13]** repeatedly iterated on. And it's such an

**[01:13]** repeatedly iterated on. And it's such an important piece of context that actually

**[01:15]** important piece of context that actually

**[01:15]** important piece of context that actually goes into making these coding agents the

**[01:17]** goes into making these coding agents the

**[01:17]** goes into making these coding agents the most successful agents out there.

**[01:20]** most successful agents out there.

**[01:20]** most successful agents out there. Um, it's not just us talking about it.

**[01:22]** Um, it's not just us talking about it.

**[01:22]** Um, it's not just us talking about it. Karpathi talks about it a lot. Um, and

**[01:25]** Karpathi talks about it a lot. Um, and

**[01:25]** Karpathi talks about it a lot. Um, and this was a viral tweet that that he

**[01:27]** this was a viral tweet that that he

**[01:27]** this was a viral tweet that that he posted, which was there's this paradigm

**[01:29]** posted, which was there's this paradigm

**[01:29]** posted, which was there's this paradigm around iterating on these prompts that

**[01:32]** around iterating on these prompts that

**[01:32]** around iterating on these prompts that he he's kind of coined it system prompt

**[01:34]** he he's kind of coined it system prompt

**[01:34]** he he's kind of coined it system prompt learning. And what he said is that it

**[01:37]** learning. And what he said is that it

**[01:37]** learning. And what he said is that it almost feels like humans learning

**[01:40]** almost feels like humans learning

**[01:40]** almost feels like humans learning because they take back English feedback

**[01:43]** because they take back English feedback

**[01:43]** because they take back English feedback uh and use that to actually iterate on

**[01:45]** uh and use that to actually iterate on

**[01:45]** uh and use that to actually iterate on what they should do differently the next

**[01:47]** what they should do differently the next

**[01:47]** what they should do differently the next time. And I think he wrote something

**[01:49]** time. And I think he wrote something

**[01:49]** time. And I think he wrote something like it's almost like that movie momento

**[01:51]** like it's almost like that movie momento

**[01:51]** like it's almost like that movie momento where the guy forgets uh what you know

**[01:54]** where the guy forgets uh what you know

**[01:54]** where the guy forgets uh what you know what he learns and then he starts

**[01:56]** what he learns and then he starts

**[01:56]** what he learns and then he starts writing it down and then uses that to

**[01:58]** writing it down and then uses that to

**[01:58]** writing it down and then uses that to actually kind of go through his next

**[01:59]** actually kind of go through his next

**[01:59]** actually kind of go through his next day. And so this is a little bit of the


### [02:00 - 03:00]

**[02:01]** day. And so this is a little bit of the

**[02:01]** day. And so this is a little bit of the concept behind system prompt learning.

**[02:04]** concept behind system prompt learning.

**[02:04]** concept behind system prompt learning. And what we wanted to do was show you

**[02:06]** And what we wanted to do was show you

**[02:06]** And what we wanted to do was show you guys a little bit of how that works and

**[02:08]** guys a little bit of how that works and

**[02:08]** guys a little bit of how that works and then put that to test on two of the most

**[02:10]** then put that to test on two of the most

**[02:10]** then put that to test on two of the most popular coding agents uh Claude and

**[02:13]** popular coding agents uh Claude and

**[02:13]** popular coding agents uh Claude and Klein today. So first off, how does

**[02:15]** Klein today. So first off, how does

**[02:15]** Klein today. So first off, how does prompt learning actually work? So for

**[02:17]** prompt learning actually work? So for

**[02:17]** prompt learning actually work? So for those of you who are familiar with RL,

**[02:18]** those of you who are familiar with RL,

**[02:18]** those of you who are familiar with RL, what I thought we'd do is just do a

**[02:20]** what I thought we'd do is just do a

**[02:20]** what I thought we'd do is just do a little analogy compare how does RL work

**[02:22]** little analogy compare how does RL work

**[02:22]** little analogy compare how does RL work versus system prompt learning. For RL,

**[02:24]** versus system prompt learning. For RL,

**[02:24]** versus system prompt learning. For RL, you know, if we just took an analogy of

**[02:26]** you know, if we just took an analogy of

**[02:26]** you know, if we just took an analogy of a student who's trying to improve their

**[02:28]** a student who's trying to improve their

**[02:28]** a student who's trying to improve their exam scores. They take an exam, you

**[02:31]** exam scores. They take an exam, you

**[02:31]** exam scores. They take an exam, you know, somebody grades the exam, you have

**[02:33]** know, somebody grades the exam, you have

**[02:33]** know, somebody grades the exam, you have a scalar reward, which is like, you

**[02:34]** a scalar reward, which is like, you

**[02:34]** a scalar reward, which is like, you know, they got a 70%, an 80%, 90%, and

**[02:37]** know, they got a 70%, an 80%, 90%, and

**[02:37]** know, they got a 70%, an 80%, 90%, and then they have to figure out almost

**[02:40]** then they have to figure out almost

**[02:40]** then they have to figure out almost blindly just with that score how to

**[02:42]** blindly just with that score how to

**[02:42]** blindly just with that score how to actually improve their score on the next

**[02:45]** actually improve their score on the next

**[02:45]** actually improve their score on the next exam. And I think this is actually one

**[02:47]** exam. And I think this is actually one

**[02:47]** exam. And I think this is actually one of the flaws of I mean RL works, don't

**[02:50]** of the flaws of I mean RL works, don't

**[02:50]** of the flaws of I mean RL works, don't get me wrong, amazing in so many

**[02:52]** get me wrong, amazing in so many

**[02:52]** get me wrong, amazing in so many concepts and domains, but it can be, you

**[02:55]** concepts and domains, but it can be, you

**[02:55]** concepts and domains, but it can be, you know, a long path to actually figure out

**[02:57]** know, a long path to actually figure out

**[02:57]** know, a long path to actually figure out what the right solution is. And I think


### [03:00 - 04:00]

**[03:01]** what the right solution is. And I think

**[03:01]** what the right solution is. And I think some of the things that we've noticed is

**[03:02]** some of the things that we've noticed is

**[03:02]** some of the things that we've noticed is that it can be sample inefficient. It

**[03:04]** that it can be sample inefficient. It

**[03:04]** that it can be sample inefficient. It takes a lot of data to get what you

**[03:05]** takes a lot of data to get what you

**[03:05]** takes a lot of data to get what you want. It's time inensive. It's data

**[03:08]** want. It's time inensive. It's data

**[03:08]** want. It's time inensive. It's data hungry. You need to have a whole data

**[03:10]** hungry. You need to have a whole data

**[03:10]** hungry. You need to have a whole data science team to do this. and it just

**[03:11]** science team to do this. and it just

**[03:12]** science team to do this. and it just might be overkill for teams who are

**[03:13]** might be overkill for teams who are

**[03:13]** might be overkill for teams who are trying to build agents because LLMs are

**[03:15]** trying to build agents because LLMs are

**[03:15]** trying to build agents because LLMs are already so good. So if you're a team

**[03:18]** already so good. So if you're a team

**[03:18]** already so good. So if you're a team who's actually trying to build an agent,

**[03:20]** who's actually trying to build an agent,

**[03:20]** who's actually trying to build an agent, maybe prompt learning is actually

**[03:21]** maybe prompt learning is actually

**[03:22]** maybe prompt learning is actually slightly

**[03:23]** slightly

**[03:23]** slightly might be slightly more of an interesting

**[03:25]** might be slightly more of an interesting

**[03:25]** might be slightly more of an interesting paradigm for you. So in this scenario,

**[03:27]** paradigm for you. So in this scenario,

**[03:27]** paradigm for you. So in this scenario, same same analogy. You have a student

**[03:29]** same same analogy. You have a student

**[03:29]** same same analogy. You have a student who's taking an exam, there's some exam

**[03:31]** who's taking an exam, there's some exam

**[03:31]** who's taking an exam, there's some exam score, except in this case, what

**[03:33]** score, except in this case, what

**[03:33]** score, except in this case, what actually gets outputed isn't just the

**[03:35]** actually gets outputed isn't just the

**[03:35]** actually gets outputed isn't just the score. They got a 70, they got an 80,

**[03:37]** score. They got a 70, they got an 80,

**[03:37]** score. They got a 70, they got an 80, but you also get back some kind of

**[03:39]** but you also get back some kind of

**[03:39]** but you also get back some kind of English feedback. Why did they get this

**[03:41]** English feedback. Why did they get this

**[03:41]** English feedback. Why did they get this answer right? What did they mess up on?

**[03:43]** answer right? What did they mess up on?

**[03:43]** answer right? What did they mess up on? Here's concepts that they missed on,

**[03:45]** Here's concepts that they missed on,

**[03:45]** Here's concepts that they missed on, what do they need to go study? And then

**[03:47]** what do they need to go study? And then

**[03:47]** what do they need to go study? And then they use this information to actually go

**[03:49]** they use this information to actually go

**[03:49]** they use this information to actually go and and prepare on what to do next um to

**[03:52]** and and prepare on what to do next um to

**[03:52]** and and prepare on what to do next um to to get a better score. This is basically

**[03:56]** to get a better score. This is basically

**[03:56]** to get a better score. This is basically the the concept that we applied to

**[03:59]** the the concept that we applied to

**[03:59]** the the concept that we applied to coding agents. And we ran this kind of


### [04:00 - 05:00]

**[04:01]** coding agents. And we ran this kind of

**[04:01]** coding agents. And we ran this kind of test on both Claude as well as Klein.

**[04:05]** test on both Claude as well as Klein.

**[04:05]** test on both Claude as well as Klein. Um, both of these, as you know, start

**[04:07]** Um, both of these, as you know, start

**[04:07]** Um, both of these, as you know, start off with some kind of uh system prompt,

**[04:10]** off with some kind of uh system prompt,

**[04:10]** off with some kind of uh system prompt, which in cloud code, this is kind of a

**[04:12]** which in cloud code, this is kind of a

**[04:12]** which in cloud code, this is kind of a snippet of it. And they both kind of

**[04:13]** snippet of it. And they both kind of

**[04:14]** snippet of it. And they both kind of come with something that you can append

**[04:15]** come with something that you can append

**[04:15]** come with something that you can append rules to. So, client has rules, cloud MD

**[04:17]** rules to. So, client has rules, cloud MD

**[04:17]** rules to. So, client has rules, cloud MD has the cloud MD file, and it starts off

**[04:19]** has the cloud MD file, and it starts off

**[04:19]** has the cloud MD file, and it starts off empty. You can go in and add whatever is

**[04:22]** empty. You can go in and add whatever is

**[04:22]** empty. You can go in and add whatever is important for your repo. So, what we did

**[04:25]** important for your repo. So, what we did

**[04:25]** important for your repo. So, what we did was actually took, you know, just

**[04:27]** was actually took, you know, just

**[04:27]** was actually took, you know, just benchmark both client and cloud code on

**[04:30]** benchmark both client and cloud code on

**[04:30]** benchmark both client and cloud code on Swebench. I'm going to kind of run

**[04:31]** Swebench. I'm going to kind of run

**[04:31]** Swebench. I'm going to kind of run through theam uh this entire example at

**[04:33]** through theam uh this entire example at

**[04:33]** through theam uh this entire example at Sweetbench, but this entire thing we

**[04:35]** Sweetbench, but this entire thing we

**[04:35]** Sweetbench, but this entire thing we also ran on BBH and a ton of other uh

**[04:38]** also ran on BBH and a ton of other uh

**[04:38]** also ran on BBH and a ton of other uh software engineering data sets, but you

**[04:40]** software engineering data sets, but you

**[04:40]** software engineering data sets, but you can see here just on vanilla client

**[04:42]** can see here just on vanilla client

**[04:42]** can see here just on vanilla client vanilla cloud code um nothing added to

**[04:45]** vanilla cloud code um nothing added to

**[04:45]** vanilla cloud code um nothing added to the cloud MD or the client rules. Um

**[04:47]** the cloud MD or the client rules. Um

**[04:47]** the cloud MD or the client rules. Um they had you know about I think with

**[04:50]** they had you know about I think with

**[04:50]** they had you know about I think with client somewhere on you know cloud

**[04:52]** client somewhere on you know cloud

**[04:52]** client somewhere on you know cloud sonnet 45 it was about 30% of the github

**[04:54]** sonnet 45 it was about 30% of the github

**[04:54]** sonnet 45 it was about 30% of the github issues actually resolved uh cloud code

**[04:56]** issues actually resolved uh cloud code

**[04:56]** issues actually resolved uh cloud code it was about 40% of the github issues

**[04:59]** it was about 40% of the github issues

**[04:59]** it was about 40% of the github issues resolved. So we took this as kind of our


### [05:00 - 06:00]

**[05:01]** resolved. So we took this as kind of our

**[05:01]** resolved. So we took this as kind of our starting benchmark and the thesis is is

**[05:03]** starting benchmark and the thesis is is

**[05:04]** starting benchmark and the thesis is is could we actually use prompt learning to

**[05:05]** could we actually use prompt learning to

**[05:05]** could we actually use prompt learning to see if we can improve the system prompt

**[05:07]** see if we can improve the system prompt

**[05:07]** see if we can improve the system prompt and see if um it was able to with the

**[05:11]** and see if um it was able to with the

**[05:11]** and see if um it was able to with the new system prompt actually you know give

**[05:13]** new system prompt actually you know give

**[05:14]** new system prompt actually you know give us a better uh score on these

**[05:15]** us a better uh score on these

**[05:15]** us a better uh score on these benchmarks. We didn't do anything on

**[05:17]** benchmarks. We didn't do anything on

**[05:17]** benchmarks. We didn't do anything on fine-tuning. We didn't change the models

**[05:19]** fine-tuning. We didn't change the models

**[05:19]** fine-tuning. We didn't change the models anything like that. It was just focused

**[05:21]** anything like that. It was just focused

**[05:21]** anything like that. It was just focused on the system prompt. Um this is the

**[05:24]** on the system prompt. Um this is the

**[05:24]** on the system prompt. Um this is the process that we went through. We took

**[05:25]** process that we went through. We took

**[05:25]** process that we went through. We took the coding agent. Uh we had it actually

**[05:27]** the coding agent. Uh we had it actually

**[05:27]** the coding agent. Uh we had it actually write some code. Um we ran unit tests

**[05:31]** write some code. Um we ran unit tests

**[05:31]** write some code. Um we ran unit tests and then um we then passed that through

**[05:34]** and then um we then passed that through

**[05:34]** and then um we then passed that through to some kind of um model that was doing

**[05:37]** to some kind of um model that was doing

**[05:37]** to some kind of um model that was doing the LLM as a judge evals. And I'll show

**[05:39]** the LLM as a judge evals. And I'll show

**[05:39]** the LLM as a judge evals. And I'll show you guys what that looks like. But the

**[05:41]** you guys what that looks like. But the

**[05:41]** you guys what that looks like. But the LLM as a judge eval actually gave back

**[05:43]** LLM as a judge eval actually gave back

**[05:43]** LLM as a judge eval actually gave back why did it fail? Did it fail because of

**[05:45]** why did it fail? Did it fail because of

**[05:46]** why did it fail? Did it fail because of this? Uh can you give some examples of

**[05:48]** this? Uh can you give some examples of

**[05:48]** this? Uh can you give some examples of you know what were common scenarios that

**[05:50]** you know what were common scenarios that

**[05:50]** you know what were common scenarios that it didn't do good on? and then it

**[05:52]** it didn't do good on? and then it

**[05:52]** it didn't do good on? and then it actually use those kind of evals to then

**[05:54]** actually use those kind of evals to then

**[05:54]** actually use those kind of evals to then go back and add it to a meta prompt to

**[05:56]** go back and add it to a meta prompt to

**[05:56]** go back and add it to a meta prompt to come back with kind of the the system

**[05:59]** come back with kind of the the system

**[05:59]** come back with kind of the the system prompt rules that we're going to append


### [06:00 - 07:00]

**[06:00]** prompt rules that we're going to append

**[06:00]** prompt rules that we're going to append to. So let's talk through kind of the

**[06:03]** to. So let's talk through kind of the

**[06:03]** to. So let's talk through kind of the process. So first we had kind of the

**[06:04]** process. So first we had kind of the

**[06:04]** process. So first we had kind of the SWEBench data set. Uh SWEBench in this

**[06:07]** SWEBench data set. Uh SWEBench in this

**[06:07]** SWEBench data set. Uh SWEBench in this scenario is just 150 examples. Uh we did

**[06:10]** scenario is just 150 examples. Uh we did

**[06:10]** scenario is just 150 examples. Uh we did this for both client and cloud code

**[06:11]** this for both client and cloud code

**[06:11]** this for both client and cloud code where we took the original prompt which

**[06:14]** where we took the original prompt which

**[06:14]** where we took the original prompt which had no rules. We gave it kind of the

**[06:18]** had no rules. We gave it kind of the

**[06:18]** had no rules. We gave it kind of the software engineering problem and then it

**[06:20]** software engineering problem and then it

**[06:20]** software engineering problem and then it generated some kind of patch to actually

**[06:22]** generated some kind of patch to actually

**[06:22]** generated some kind of patch to actually solve that and then we ran the generated

**[06:24]** solve that and then we ran the generated

**[06:24]** solve that and then we ran the generated solution through the unit test.

**[06:27]** solution through the unit test.

**[06:27]** solution through the unit test. Then whatever the unit test came back

**[06:29]** Then whatever the unit test came back

**[06:29]** Then whatever the unit test came back with whether it was right or wrong, we

**[06:32]** with whether it was right or wrong, we

**[06:32]** with whether it was right or wrong, we then passed this into an LLM as a judge

**[06:34]** then passed this into an LLM as a judge

**[06:34]** then passed this into an LLM as a judge eval. And this is kind of the most

**[06:36]** eval. And this is kind of the most

**[06:36]** eval. And this is kind of the most important part because this actually

**[06:38]** important part because this actually

**[06:38]** important part because this actually generated the explanation for us. So we

**[06:40]** generated the explanation for us. So we

**[06:40]** generated the explanation for us. So we passed in the problem statement. We

**[06:42]** passed in the problem statement. We

**[06:42]** passed in the problem statement. We passed in what the coding agent solution

**[06:44]** passed in what the coding agent solution

**[06:44]** passed in what the coding agent solution was, the unit tests, and then the actual

**[06:46]** was, the unit tests, and then the actual

**[06:46]** was, the unit tests, and then the actual solution that it came up with. Uh, pass

**[06:49]** solution that it came up with. Uh, pass

**[06:49]** solution that it came up with. Uh, pass that in. And this that you're looking at

**[06:51]** that in. And this that you're looking at

**[06:51]** that in. And this that you're looking at in the center here is actually the LLM

**[06:53]** in the center here is actually the LLM

**[06:53]** in the center here is actually the LLM as a judge eval. And these evalu


### [07:00 - 08:00]

**[07:02]** engineering is a whole kind of concept

**[07:02]** engineering is a whole kind of concept that, you know, we spend a lot of time

**[07:04]** that, you know, we spend a lot of time

**[07:04]** that, you know, we spend a lot of time on. And writing really good evals is I

**[07:06]** on. And writing really good evals is I

**[07:06]** on. And writing really good evals is I think um how you get the best kind of

**[07:09]** think um how you get the best kind of

**[07:09]** think um how you get the best kind of insight into what you could do to

**[07:11]** insight into what you could do to

**[07:11]** insight into what you could do to improve your agents. So in this

**[07:12]** improve your agents. So in this

**[07:12]** improve your agents. So in this scenario, what we did was we wrote a

**[07:14]** scenario, what we did was we wrote a

**[07:14]** scenario, what we did was we wrote a good LM as a judge eval prompt. It

**[07:16]** good LM as a judge eval prompt. It

**[07:16]** good LM as a judge eval prompt. It outputed whether it failed or passed.

**[07:18]** outputed whether it failed or passed.

**[07:18]** outputed whether it failed or passed. And then this is the key part. We

**[07:20]** And then this is the key part. We

**[07:20]** And then this is the key part. We actually asked for an explanation. Why

**[07:22]** actually asked for an explanation. Why

**[07:22]** actually asked for an explanation. Why did it actually mess up? um you know for

**[07:25]** did it actually mess up? um you know for

**[07:25]** did it actually mess up? um you know for specific libraries in the Sweetbench

**[07:27]** specific libraries in the Sweetbench

**[07:27]** specific libraries in the Sweetbench light test um you know it was parsing

**[07:30]** light test um you know it was parsing

**[07:30]** light test um you know it was parsing errors or it was not handling um

**[07:34]** errors or it was not handling um

**[07:34]** errors or it was not handling um there there's all sorts of actually

**[07:35]** there there's all sorts of actually

**[07:35]** there there's all sorts of actually different categories of errors but we

**[07:36]** different categories of errors but we

**[07:36]** different categories of errors but we went through and we we kind of looked at

**[07:38]** went through and we we kind of looked at

**[07:38]** went through and we we kind of looked at the explanation of what went wrong in

**[07:40]** the explanation of what went wrong in

**[07:40]** the explanation of what went wrong in each scenario. We then passed into a

**[07:43]** each scenario. We then passed into a

**[07:43]** each scenario. We then passed into a huge meta prompt. So this is actually

**[07:45]** huge meta prompt. So this is actually

**[07:45]** huge meta prompt. So this is actually what's helping us iterate on our system

**[07:47]** what's helping us iterate on our system

**[07:47]** what's helping us iterate on our system prompt. We passed in the original claude

**[07:50]** prompt. We passed in the original claude

**[07:50]** prompt. We passed in the original claude or client system prompt. We passed in

**[07:52]** or client system prompt. We passed in

**[07:52]** or client system prompt. We passed in the original rules which for us started

**[07:54]** the original rules which for us started

**[07:54]** the original rules which for us started off empty. Um and then we passed in here

**[07:56]** off empty. Um and then we passed in here

**[07:56]** off empty. Um and then we passed in here was the input, here was the LM is a

**[07:59]** was the input, here was the LM is a

**[07:59]** was the input, here was the LM is a judge eval, and then here was the actual


### [08:00 - 09:00]

**[08:01]** judge eval, and then here was the actual

**[08:01]** judge eval, and then here was the actual explanation from that eval.

**[08:03]** explanation from that eval.

**[08:04]** explanation from that eval. Passed that all into the meta prompt and

**[08:06]** Passed that all into the meta prompt and

**[08:06]** Passed that all into the meta prompt and then we did kind of a diff comparing you

**[08:08]** then we did kind of a diff comparing you

**[08:08]** then we did kind of a diff comparing you know the old world. So just for you just

**[08:10]** know the old world. So just for you just

**[08:10]** know the old world. So just for you just to remember the old world had the

**[08:12]** to remember the old world had the

**[08:12]** to remember the old world had the original clawed system prompt no rules

**[08:15]** original clawed system prompt no rules

**[08:15]** original clawed system prompt no rules kind of added or appended to it. And

**[08:17]** kind of added or appended to it. And

**[08:17]** kind of added or appended to it. And then the new world where it generated

**[08:19]** then the new world where it generated

**[08:19]** then the new world where it generated this entire rules of what to avoid or

**[08:23]** this entire rules of what to avoid or

**[08:23]** this entire rules of what to avoid or what to um what it had learned

**[08:26]** what to um what it had learned

**[08:26]** what to um what it had learned essentially from all those mistakes it

**[08:27]** essentially from all those mistakes it

**[08:28]** essentially from all those mistakes it had actually made. And then we ran this

**[08:31]** had actually made. And then we ran this

**[08:31]** had actually made. And then we ran this basically on the entire Sweetbench light

**[08:33]** basically on the entire Sweetbench light

**[08:33]** basically on the entire Sweetbench light again. Um and what we saw was that you

**[08:36]** again. Um and what we saw was that you

**[08:36]** again. Um and what we saw was that you know on 150 examples we were able to get

**[08:39]** know on 150 examples we were able to get

**[08:39]** know on 150 examples we were able to get cloud code up by 5% more GitHub issues

**[08:42]** cloud code up by 5% more GitHub issues

**[08:42]** cloud code up by 5% more GitHub issues resolved client um you know 15% and this

**[08:47]** resolved client um you know 15% and this

**[08:47]** resolved client um you know 15% and this was literally on I think the key thing

**[08:49]** was literally on I think the key thing

**[08:49]** was literally on I think the key thing is like 150 examples of just training

**[08:53]** is like 150 examples of just training

**[08:53]** is like 150 examples of just training data that was used um on the most kind

**[08:57]** data that was used um on the most kind

**[08:57]** data that was used um on the most kind of powerful coding agents that are out

**[08:59]** of powerful coding agents that are out

**[08:59]** of powerful coding agents that are out there. Um, and so just think about kind


### [09:00 - 10:00]

**[09:02]** there. Um, and so just think about kind

**[09:02]** there. Um, and so just think about kind of the impact that could have for your

**[09:04]** of the impact that could have for your

**[09:04]** of the impact that could have for your agents. Many of you guys in this room

**[09:05]** agents. Many of you guys in this room

**[09:05]** agents. Many of you guys in this room might be thinking, okay, well, prompt

**[09:07]** might be thinking, okay, well, prompt

**[09:07]** might be thinking, okay, well, prompt learning is cool, but how does that

**[09:08]** learning is cool, but how does that

**[09:08]** learning is cool, but how does that compare to GEA? If you're familiar with

**[09:10]** compare to GEA? If you're familiar with

**[09:10]** compare to GEA? If you're familiar with DSPI and you've kind of seen, I don't

**[09:12]** DSPI and you've kind of seen, I don't

**[09:12]** DSPI and you've kind of seen, I don't know if it's GEA or Jeepa. I've heard

**[09:14]** know if it's GEA or Jeepa. I've heard

**[09:14]** know if it's GEA or Jeepa. I've heard both. Um, but you know, you guys might

**[09:17]** both. Um, but you know, you guys might

**[09:17]** both. Um, but you know, you guys might be asking, well, how is this different?

**[09:18]** be asking, well, how is this different?

**[09:18]** be asking, well, how is this different? Um, so GEA, just just in case you guys

**[09:22]** Um, so GEA, just just in case you guys

**[09:22]** Um, so GEA, just just in case you guys aren't familiar, it's a prompt optimizer

**[09:24]** aren't familiar, it's a prompt optimizer

**[09:24]** aren't familiar, it's a prompt optimizer from DSPI that is essentially very very

**[09:28]** from DSPI that is essentially very very

**[09:28]** from DSPI that is essentially very very similar to what we're talking about,

**[09:29]** similar to what we're talking about,

**[09:29]** similar to what we're talking about, which is taking English feedback using

**[09:31]** which is taking English feedback using

**[09:31]** which is taking English feedback using that English feedback inside of the

**[09:33]** that English feedback inside of the

**[09:33]** that English feedback inside of the actual prompt. Um, and what we did was

**[09:37]** actual prompt. Um, and what we did was

**[09:37]** actual prompt. Um, and what we did was actually run a sidebyside benchmark

**[09:39]** actually run a sidebyside benchmark

**[09:39]** actually run a sidebyside benchmark against GEA where we compared kind of

**[09:42]** against GEA where we compared kind of

**[09:42]** against GEA where we compared kind of our prompt learning against GEA. And um

**[09:45]** our prompt learning against GEA. And um

**[09:45]** our prompt learning against GEA. And um I think what we saw was that GEA

**[09:48]** I think what we saw was that GEA

**[09:48]** I think what we saw was that GEA required many many loops and rollouts

**[09:50]** required many many loops and rollouts

**[09:50]** required many many loops and rollouts compared to um kind of a a fraction of

**[09:53]** compared to um kind of a a fraction of

**[09:53]** compared to um kind of a a fraction of that which was our approach. And I think

**[09:57]** that which was our approach. And I think

**[09:57]** that which was our approach. And I think the key difference here, I mean the

**[09:58]** the key difference here, I mean the

**[09:58]** the key difference here, I mean the underlying approach around using English


### [10:00 - 11:00]

**[10:00]** underlying approach around using English

**[10:00]** underlying approach around using English feedback is the same, but I think the

**[10:02]** feedback is the same, but I think the

**[10:02]** feedback is the same, but I think the key thing that was really different here

**[10:03]** key thing that was really different here

**[10:03]** key thing that was really different here was we spent a lot of time actually

**[10:06]** was we spent a lot of time actually

**[10:06]** was we spent a lot of time actually developing and iterating on the evals

**[10:08]** developing and iterating on the evals

**[10:08]** developing and iterating on the evals and the eval prompts really mattered to

**[10:10]** and the eval prompts really mattered to

**[10:10]** and the eval prompts really mattered to making sure that you gave really good

**[10:12]** making sure that you gave really good

**[10:12]** making sure that you gave really good explanations back to the agent. Um, and

**[10:15]** explanations back to the agent. Um, and

**[10:15]** explanations back to the agent. Um, and so eval.

**[10:18]** so eval.

**[10:18]** so eval. This was super critical for us to be

**[10:19]** This was super critical for us to be

**[10:19]** This was super critical for us to be able to get this to work. Um, and if you

**[10:23]** able to get this to work. Um, and if you

**[10:23]** able to get this to work. Um, and if you guys are curious about learning more,

**[10:25]** guys are curious about learning more,

**[10:25]** guys are curious about learning more, reading more about kind of what we do,

**[10:27]** reading more about kind of what we do,

**[10:27]** reading more about kind of what we do, um, check out kind of our blog. We write

**[10:29]** um, check out kind of our blog. We write

**[10:29]** um, check out kind of our blog. We write a lot about eval prompt optimization

**[10:32]** a lot about eval prompt optimization

**[10:32]** a lot about eval prompt optimization and, uh, we're actively hiring, [music]

**[10:34]** and, uh, we're actively hiring, [music]

**[10:34]** and, uh, we're actively hiring, [music] so come check us out. Awesome.


