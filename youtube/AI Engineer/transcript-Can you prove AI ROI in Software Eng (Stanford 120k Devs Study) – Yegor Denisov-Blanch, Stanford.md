# Can you prove AI ROI in Software Eng (Stanford 120k Devs Study) – Yegor Denisov-Blanch, Stanford

**Video URL:** https://www.youtube.com/watch?v=JvosMkuNxF8

---

## Full Transcript

### [00:00 - 01:00]

**[00:25]** So companies spend millions on AI tools

**[00:25]** So companies spend millions on AI tools for software engineering. But do we

**[00:27]** for software engineering. But do we

**[00:27]** for software engineering. But do we actually know how well these tools work

**[00:29]** actually know how well these tools work

**[00:29]** actually know how well these tools work in the enterprise or are these tools

**[00:31]** in the enterprise or are these tools

**[00:31]** in the enterprise or are these tools just all hype? To answer this and for

**[00:35]** just all hype? To answer this and for

**[00:35]** just all hype? To answer this and for the past two years, we've been

**[00:36]** the past two years, we've been

**[00:36]** the past two years, we've been researching the impact of AI on software

**[00:38]** researching the impact of AI on software

**[00:38]** researching the impact of AI on software engineering productivity. And our

**[00:41]** engineering productivity. And our

**[00:41]** engineering productivity. And our research is time series because we look

**[00:43]** research is time series because we look

**[00:43]** research is time series because we look at get historical data, meaning we can

**[00:45]** at get historical data, meaning we can

**[00:45]** at get historical data, meaning we can go back in time. And it's also

**[00:47]** go back in time. And it's also

**[00:47]** go back in time. And it's also cross-sectional because we cut across

**[00:49]** cross-sectional because we cut across

**[00:49]** cross-sectional because we cut across companies. And the way we use to measure

**[00:53]** companies. And the way we use to measure

**[00:53]** companies. And the way we use to measure most of the of the impact is by a

**[00:55]** most of the of the impact is by a

**[00:55]** most of the of the impact is by a machine learning model that replicates a

**[00:57]** machine learning model that replicates a

**[00:57]** machine learning model that replicates a panel of human experts. The way this


### [01:00 - 02:00]

**[01:00]** panel of human experts. The way this

**[01:00]** panel of human experts. The way this works is that imagine you have a

**[01:03]** works is that imagine you have a

**[01:03]** works is that imagine you have a software engineer who writes a code

**[01:05]** software engineer who writes a code

**[01:05]** software engineer who writes a code commit and this code commit would be

**[01:07]** commit and this code commit would be

**[01:07]** commit and this code commit would be evaluated by multiple panels or of 10

**[01:10]** evaluated by multiple panels or of 10

**[01:10]** evaluated by multiple panels or of 10 and 15 independent experts who would

**[01:12]** and 15 independent experts who would

**[01:12]** and 15 independent experts who would evaluate that code commit across

**[01:15]** evaluate that code commit across

**[01:15]** evaluate that code commit across implementation time maintainability and

**[01:17]** implementation time maintainability and

**[01:17]** implementation time maintainability and complexity and then produce an output

**[01:19]** complexity and then produce an output

**[01:19]** complexity and then produce an output evaluation. So we took the labels of

**[01:22]** evaluation. So we took the labels of

**[01:22]** evaluation. So we took the labels of these panels across you know millions of

**[01:24]** these panels across you know millions of

**[01:24]** these panels across you know millions of of kind of evaluations and then trained

**[01:26]** of kind of evaluations and then trained

**[01:26]** of kind of evaluations and then trained a model to replicate this panel of

**[01:28]** a model to replicate this panel of

**[01:28]** a model to replicate this panel of experts meaning that we can deploy this

**[01:30]** experts meaning that we can deploy this

**[01:30]** experts meaning that we can deploy this at scale and if there's ever any doubts

**[01:33]** at scale and if there's ever any doubts

**[01:33]** at scale and if there's ever any doubts around the model's output you can always

**[01:35]** around the model's output you can always

**[01:35]** around the model's output you can always kind of assemble your own panel and see

**[01:37]** kind of assemble your own panel and see

**[01:37]** kind of assemble your own panel and see that it correlates pretty well with

**[01:38]** that it correlates pretty well with

**[01:38]** that it correlates pretty well with reality.

**[01:40]** reality.

**[01:40]** reality. Today we'll talk about four things.

**[01:42]** Today we'll talk about four things.

**[01:42]** Today we'll talk about four things. We'll start off with looking at some of

**[01:44]** We'll start off with looking at some of

**[01:44]** We'll start off with looking at some of the things that are driving AI

**[01:46]** the things that are driving AI

**[01:46]** the things that are driving AI productivity gains in software. Then

**[01:48]** productivity gains in software. Then

**[01:48]** productivity gains in software. Then we'll look at a AI practices benchmark

**[01:51]** we'll look at a AI practices benchmark

**[01:51]** we'll look at a AI practices benchmark that we developed. We'll then look at

**[01:54]** that we developed. We'll then look at

**[01:54]** that we developed. We'll then look at how we propose to measure AI return on

**[01:57]** how we propose to measure AI return on

**[01:57]** how we propose to measure AI return on investment in software engineering. And

**[01:59]** investment in software engineering. And

**[01:59]** investment in software engineering. And lastly, we'll finish things off with a


### [02:00 - 03:00]

**[02:01]** lastly, we'll finish things off with a

**[02:01]** lastly, we'll finish things off with a case study.

**[02:03]** case study.

**[02:03]** case study. So here we took 46 teams that were using

**[02:07]** So here we took 46 teams that were using

**[02:07]** So here we took 46 teams that were using AI and we matched them with 46 similar

**[02:10]** AI and we matched them with 46 similar

**[02:10]** AI and we matched them with 46 similar teams that were not using AI and we

**[02:13]** teams that were not using AI and we

**[02:13]** teams that were not using AI and we measured their net productivity gains

**[02:15]** measured their net productivity gains

**[02:15]** measured their net productivity gains from AI quarterly. And the shaded area

**[02:19]** from AI quarterly. And the shaded area

**[02:19]** from AI quarterly. And the shaded area is the middle 50% of the data and the

**[02:21]** is the middle 50% of the data and the

**[02:21]** is the middle 50% of the data and the dark blue line is the median which as of

**[02:23]** dark blue line is the median which as of

**[02:23]** dark blue line is the median which as of July of this year stands at about 10%

**[02:25]** July of this year stands at about 10%

**[02:26]** July of this year stands at about 10% for this cohort.

**[02:28]** for this cohort.

**[02:28]** for this cohort. I'd like to direct your attention to the

**[02:29]** I'd like to direct your attention to the

**[02:29]** I'd like to direct your attention to the fact that the discrepancy between the

**[02:32]** fact that the discrepancy between the

**[02:32]** fact that the discrepancy between the top performers and the bottom ones is

**[02:34]** top performers and the bottom ones is

**[02:34]** top performers and the bottom ones is increasing. There's a widening gap. And

**[02:37]** increasing. There's a widening gap. And

**[02:37]** increasing. There's a widening gap. And so if we very unscientifically and very

**[02:40]** so if we very unscientifically and very

**[02:40]** so if we very unscientifically and very illustratively project this forward, we

**[02:42]** illustratively project this forward, we

**[02:42]** illustratively project this forward, we might get something like this, right?

**[02:44]** might get something like this, right?

**[02:44]** might get something like this, right? where uh you can have these top

**[02:45]** where uh you can have these top

**[02:45]** where uh you can have these top performers being part of this the rich

**[02:48]** performers being part of this the rich

**[02:48]** performers being part of this the rich gets richer effect where they these

**[02:50]** gets richer effect where they these

**[02:50]** gets richer effect where they these successful early AI adopters might

**[02:52]** successful early AI adopters might

**[02:52]** successful early AI adopters might compound their gains while these

**[02:54]** compound their gains while these

**[02:54]** compound their gains while these strugglers could fall further behind. At

**[02:56]** strugglers could fall further behind. At

**[02:56]** strugglers could fall further behind. At some point this is going to converge and

**[02:58]** some point this is going to converge and

**[02:58]** some point this is going to converge and this is very directional. But my point


### [03:00 - 04:00]

**[03:00]** this is very directional. But my point

**[03:00]** this is very directional. But my point here is that if you're a leader in a

**[03:02]** here is that if you're a leader in a

**[03:02]** here is that if you're a leader in a company, you definitely need to know in

**[03:04]** company, you definitely need to know in

**[03:04]** company, you definitely need to know in which cohort you are right now so that

**[03:05]** which cohort you are right now so that

**[03:05]** which cohort you are right now so that you can course correct and without

**[03:07]** you can course correct and without

**[03:07]** you can course correct and without measuring the impact of AI on your

**[03:10]** measuring the impact of AI on your

**[03:10]** measuring the impact of AI on your engineers, you're not going to be able

**[03:11]** engineers, you're not going to be able

**[03:11]** engineers, you're not going to be able to do this.

**[03:14]** to do this.

**[03:14]** to do this. So we started investigating what are

**[03:16]** So we started investigating what are

**[03:16]** So we started investigating what are some of the factors that drive these top

**[03:18]** some of the factors that drive these top

**[03:18]** some of the factors that drive these top teams to perform better and the first

**[03:20]** teams to perform better and the first

**[03:20]** teams to perform better and the first thing we looked at is AI usage or

**[03:22]** thing we looked at is AI usage or

**[03:22]** thing we looked at is AI usage or basically token spent. In this graph you

**[03:25]** basically token spent. In this graph you

**[03:25]** basically token spent. In this graph you have the same kind of on the vertical

**[03:28]** have the same kind of on the vertical

**[03:28]** have the same kind of on the vertical axis the productivity increase and then

**[03:30]** axis the productivity increase and then

**[03:30]** axis the productivity increase and then on the horizontal one you have the token

**[03:32]** on the horizontal one you have the token

**[03:32]** on the horizontal one you have the token usage per engineer per month on a

**[03:33]** usage per engineer per month on a

**[03:33]** usage per engineer per month on a logarithmic scale. And what you can see

**[03:36]** logarithmic scale. And what you can see

**[03:36]** logarithmic scale. And what you can see is that the correlation is quite loose

**[03:38]** is that the correlation is quite loose

**[03:38]** is that the correlation is quite loose 020 or so linearly and there is a bit of

**[03:41]** 020 or so linearly and there is a bit of

**[03:41]** 020 or so linearly and there is a bit of a death valley effect around the 10

**[03:43]** a death valley effect around the 10

**[03:43]** a death valley effect around the 10 million uh token mark whereby teams that

**[03:46]** million uh token mark whereby teams that

**[03:46]** million uh token mark whereby teams that were using that amount of tokens seem to

**[03:48]** were using that amount of tokens seem to

**[03:48]** were using that amount of tokens seem to be doing worse than teams that were

**[03:49]** be doing worse than teams that were

**[03:49]** be doing worse than teams that were using a bit less tokens. It's very

**[03:51]** using a bit less tokens. It's very

**[03:51]** using a bit less tokens. It's very directional but interesting.

**[03:52]** directional but interesting.

**[03:52]** directional but interesting. Nevertheless,

**[03:54]** Nevertheless,

**[03:54]** Nevertheless, the conclusion here might be that AI

**[03:56]** the conclusion here might be that AI

**[03:56]** the conclusion here might be that AI usage quality matters more than AI usage


### [04:00 - 05:00]

**[04:00]** usage quality matters more than AI usage

**[04:00]** usage quality matters more than AI usage value.

**[04:02]** value.

**[04:02]** value. We dug deeper and we said well does the

**[04:05]** We dug deeper and we said well does the

**[04:05]** We dug deeper and we said well does the environment in which the engineers work

**[04:07]** environment in which the engineers work

**[04:07]** environment in which the engineers work impact the productivity from AI and we

**[04:10]** impact the productivity from AI and we

**[04:10]** impact the productivity from AI and we came up with an environment cleaniness

**[04:12]** came up with an environment cleaniness

**[04:12]** came up with an environment cleaniness index index it's quite experimental it's

**[04:14]** index index it's quite experimental it's

**[04:14]** index index it's quite experimental it's a composite score that looks at tests

**[04:17]** a composite score that looks at tests

**[04:17]** a composite score that looks at tests looks at uh types and documentation and

**[04:20]** looks at uh types and documentation and

**[04:20]** looks at uh types and documentation and at modularity and at code quality and

**[04:22]** at modularity and at code quality and

**[04:22]** at modularity and at code quality and that index is on the bottom axis here

**[04:24]** that index is on the bottom axis here

**[04:24]** that index is on the bottom axis here from 0 to one and then on the vertical

**[04:26]** from 0 to one and then on the vertical

**[04:26]** from 0 to one and then on the vertical axis once again you have the kind of

**[04:28]** axis once again you have the kind of

**[04:28]** axis once again you have the kind of productivity lift relative to teams not

**[04:30]** productivity lift relative to teams not

**[04:30]** productivity lift relative to teams not using AI

**[04:31]** using AI

**[04:31]** using AI And so what you can see is that there's

**[04:33]** And so what you can see is that there's

**[04:33]** And so what you can see is that there's a point40 R squar meaning a pretty

**[04:35]** a point40 R squar meaning a pretty

**[04:35]** a point40 R squar meaning a pretty decent correlation around environment

**[04:38]** decent correlation around environment

**[04:38]** decent correlation around environment cleanliness and gains from uh AI or

**[04:41]** cleanliness and gains from uh AI or

**[04:41]** cleanliness and gains from uh AI or productivity gains from using AI. And so

**[04:44]** productivity gains from using AI. And so

**[04:44]** productivity gains from using AI. And so the takeaway here is to invest in

**[04:46]** the takeaway here is to invest in

**[04:46]** the takeaway here is to invest in codebase hygiene to unlock these AI

**[04:48]** codebase hygiene to unlock these AI

**[04:48]** codebase hygiene to unlock these AI productivity gains.

**[04:51]** productivity gains.

**[04:51]** productivity gains. We dug deeper to illustrate this

**[04:53]** We dug deeper to illustrate this

**[04:54]** We dug deeper to illustrate this concept. And here we have on this graph

**[04:56]** concept. And here we have on this graph

**[04:56]** concept. And here we have on this graph on the vertical axis the percentage of

**[04:58]** on the vertical axis the percentage of

**[04:58]** on the vertical axis the percentage of tasks that might uh be able to be


### [05:00 - 06:00]

**[05:01]** tasks that might uh be able to be

**[05:01]** tasks that might uh be able to be completed by AI based on three colors.

**[05:03]** completed by AI based on three colors.

**[05:04]** completed by AI based on three colors. And so green means that AI can do most

**[05:06]** And so green means that AI can do most

**[05:06]** And so green means that AI can do most of the work for that task in that

**[05:07]** of the work for that task in that

**[05:07]** of the work for that task in that sprint. Yellow means that AI can help

**[05:10]** sprint. Yellow means that AI can help

**[05:10]** sprint. Yellow means that AI can help someone and red uh means that AI is not

**[05:13]** someone and red uh means that AI is not

**[05:13]** someone and red uh means that AI is not very useful. And this is quite

**[05:14]** very useful. And this is quite

**[05:14]** very useful. And this is quite illustrative but it conveys the point.

**[05:16]** illustrative but it conveys the point.

**[05:16]** illustrative but it conveys the point. And so then any code base at any point

**[05:18]** And so then any code base at any point

**[05:18]** And so then any code base at any point in time sits on a vertical line across

**[05:20]** in time sits on a vertical line across

**[05:20]** in time sits on a vertical line across this graphic. And what you can see is

**[05:23]** this graphic. And what you can see is

**[05:23]** this graphic. And what you can see is that clean code amplifies AI gains.

**[05:27]** that clean code amplifies AI gains.

**[05:27]** that clean code amplifies AI gains. Secondly is that you need to manage your

**[05:29]** Secondly is that you need to manage your

**[05:29]** Secondly is that you need to manage your codebase entropy, right? Your codebase

**[05:31]** codebase entropy, right? Your codebase

**[05:31]** codebase entropy, right? Your codebase tech debt because if you just use AI

**[05:34]** tech debt because if you just use AI

**[05:34]** tech debt because if you just use AI unchecked, this is going to accelerate

**[05:36]** unchecked, this is going to accelerate

**[05:36]** unchecked, this is going to accelerate this entropy which is going to push and

**[05:38]** this entropy which is going to push and

**[05:38]** this entropy which is going to push and degrade your cleanliness to the left

**[05:40]** degrade your cleanliness to the left

**[05:40]** degrade your cleanliness to the left kind of right and then you as as a human

**[05:42]** kind of right and then you as as a human

**[05:42]** kind of right and then you as as a human need to push on the other side to kind

**[05:44]** need to push on the other side to kind

**[05:44]** need to push on the other side to kind of improve or maintain that cleanliness

**[05:46]** of improve or maintain that cleanliness

**[05:46]** of improve or maintain that cleanliness to keep reaping the benefits from AI.

**[05:50]** to keep reaping the benefits from AI.

**[05:50]** to keep reaping the benefits from AI. Thirdly is that it's important that

**[05:51]** Thirdly is that it's important that

**[05:51]** Thirdly is that it's important that engineers need to know when to use AI

**[05:54]** engineers need to know when to use AI

**[05:54]** engineers need to know when to use AI and when not to use AI. And what happens

**[05:56]** and when not to use AI. And what happens

**[05:56]** and when not to use AI. And what happens when they don't is this kind of line on

**[05:59]** when they don't is this kind of line on

**[05:59]** when they don't is this kind of line on the left whereby you have AI AI outputs


### [06:00 - 07:00]

**[06:02]** the left whereby you have AI AI outputs

**[06:02]** the left whereby you have AI AI outputs that are rejected or need heavy

**[06:04]** that are rejected or need heavy

**[06:04]** that are rejected or need heavy rewriting which then leads to engineers

**[06:07]** rewriting which then leads to engineers

**[06:07]** rewriting which then leads to engineers losing trust in AI saying okay this just

**[06:09]** losing trust in AI saying okay this just

**[06:09]** losing trust in AI saying okay this just doesn't work. I'm not going to use it.

**[06:10]** doesn't work. I'm not going to use it.

**[06:10]** doesn't work. I'm not going to use it. Which then further collapses your AI

**[06:12]** Which then further collapses your AI

**[06:12]** Which then further collapses your AI gains.

**[06:21]** Now we said can we find out whether we

**[06:21]** Now we said can we find out whether we can look not only at usage but at how

**[06:23]** can look not only at usage but at how

**[06:23]** can look not only at usage but at how are these companies and these engineers

**[06:25]** are these companies and these engineers

**[06:25]** are these companies and these engineers using AI and we came up with an AI

**[06:29]** using AI and we came up with an AI

**[06:29]** using AI and we came up with an AI engineering practices benchmark. The way

**[06:31]** engineering practices benchmark. The way

**[06:31]** engineering practices benchmark. The way this works is that we can scan your

**[06:33]** this works is that we can scan your

**[06:33]** this works is that we can scan your codebase and detect these AI

**[06:35]** codebase and detect these AI

**[06:35]** codebase and detect these AI fingerprints or artifacts basically

**[06:37]** fingerprints or artifacts basically

**[06:37]** fingerprints or artifacts basically traces of how your team is using AI.

**[06:40]** traces of how your team is using AI.

**[06:40]** traces of how your team is using AI. It's quite directional at this point but

**[06:42]** It's quite directional at this point but

**[06:42]** It's quite directional at this point but evolving. And we can quantify this based

**[06:45]** evolving. And we can quantify this based

**[06:45]** evolving. And we can quantify this based on the percentage of your active

**[06:47]** on the percentage of your active

**[06:47]** on the percentage of your active engineering work that uses each AI

**[06:49]** engineering work that uses each AI

**[06:49]** engineering work that uses each AI pattern. And then we kind of repeat this

**[06:51]** pattern. And then we kind of repeat this

**[06:51]** pattern. And then we kind of repeat this monthly using git history. And the way

**[06:53]** monthly using git history. And the way

**[06:54]** monthly using git history. And the way this works is more or less you have kind

**[06:56]** this works is more or less you have kind

**[06:56]** this works is more or less you have kind of a few levels. And level zero might be

**[06:58]** of a few levels. And level zero might be

**[06:58]** of a few levels. And level zero might be how humans are just not using AI and


### [07:00 - 08:00]

**[07:00]** how humans are just not using AI and

**[07:00]** how humans are just not using AI and write all of the code. Level one is kind

**[07:03]** write all of the code. Level one is kind

**[07:03]** write all of the code. Level one is kind of like personal use where engineers are

**[07:05]** of like personal use where engineers are

**[07:05]** of like personal use where engineers are not sharing prompts across the team or

**[07:08]** not sharing prompts across the team or

**[07:08]** not sharing prompts across the team or not versioning them. Level two is team

**[07:10]** not versioning them. Level two is team

**[07:10]** not versioning them. Level two is team use whereby teams are are sharing these

**[07:13]** use whereby teams are are sharing these

**[07:13]** use whereby teams are are sharing these kind of prompts and rules. And then

**[07:15]** kind of prompts and rules. And then

**[07:15]** kind of prompts and rules. And then level three is even more sophisticated.

**[07:16]** level three is even more sophisticated.

**[07:16]** level three is even more sophisticated. It's where AI autonomously does specific

**[07:19]** It's where AI autonomously does specific

**[07:19]** It's where AI autonomously does specific tasks maybe not the entire workflow. And

**[07:21]** tasks maybe not the entire workflow. And

**[07:21]** tasks maybe not the entire workflow. And level four is you know agentic

**[07:23]** level four is you know agentic

**[07:23]** level four is you know agentic orchestration which is where AI just

**[07:26]** orchestration which is where AI just

**[07:26]** orchestration which is where AI just runs the entire process. And so this is

**[07:27]** runs the entire process. And so this is

**[07:27]** runs the entire process. And so this is going to be an open- source tool which

**[07:29]** going to be an open- source tool which

**[07:29]** going to be an open- source tool which you can leverage if you sign up on the

**[07:31]** you can leverage if you sign up on the

**[07:32]** you can leverage if you sign up on the sweeper research portal. [snorts]

**[07:35]** sweeper research portal. [snorts]

**[07:35]** sweeper research portal. [snorts] We applied this benchmark to one of the

**[07:38]** We applied this benchmark to one of the

**[07:38]** We applied this benchmark to one of the companies in our research data set and

**[07:40]** companies in our research data set and

**[07:40]** companies in our research data set and we saw this. This company had two

**[07:42]** we saw this. This company had two

**[07:42]** we saw this. This company had two business units with equal access to AI

**[07:45]** business units with equal access to AI

**[07:45]** business units with equal access to AI tools, right? Same licenses, same spend,

**[07:48]** tools, right? Same licenses, same spend,

**[07:48]** tools, right? Same licenses, same spend, same tools, same everything. But the

**[07:50]** same tools, same everything. But the

**[07:50]** same tools, same everything. But the adoption rate and the usage rate was

**[07:52]** adoption rate and the usage rate was

**[07:52]** adoption rate and the usage rate was very different by business

**[07:53]** very different by business

**[07:53]** very different by business [clears throat] unit. On the left, the

**[07:55]** [clears throat] unit. On the left, the

**[07:55]** [clears throat] unit. On the left, the first business unit, you can as you can

**[07:57]** first business unit, you can as you can

**[07:57]** first business unit, you can as you can see in the area in the blue, seemed to

**[07:59]** see in the area in the blue, seemed to

**[07:59]** see in the area in the blue, seemed to be using AI a lot more for almost 40% of


### [08:00 - 09:00]

**[08:02]** be using AI a lot more for almost 40% of

**[08:02]** be using AI a lot more for almost 40% of their work. whereas on the on the uh

**[08:04]** their work. whereas on the on the uh

**[08:04]** their work. whereas on the on the uh right the second business unit seem to

**[08:07]** right the second business unit seem to

**[08:07]** right the second business unit seem to struggle behind a bit more. And so the

**[08:09]** struggle behind a bit more. And so the

**[08:09]** struggle behind a bit more. And so the takeaway here is that access to AI and

**[08:13]** takeaway here is that access to AI and

**[08:13]** takeaway here is that access to AI and even AI usage doesn't mean or doesn't

**[08:15]** even AI usage doesn't mean or doesn't

**[08:15]** even AI usage doesn't mean or doesn't guarantee that that AI is going to be

**[08:18]** guarantee that that AI is going to be

**[08:18]** guarantee that that AI is going to be used in the same way across a company.

**[08:22]** used in the same way across a company.

**[08:22]** used in the same way across a company. As a leader, you really want to be

**[08:23]** As a leader, you really want to be

**[08:23]** As a leader, you really want to be understanding not just whether they're

**[08:25]** understanding not just whether they're

**[08:25]** understanding not just whether they're using but also how your engineers are

**[08:27]** using but also how your engineers are

**[08:27]** using but also how your engineers are using AI.

**[08:33]** Great. Now let's dive into how do we

**[08:33]** Great. Now let's dive into how do we actually measure AI return on investment

**[08:36]** actually measure AI return on investment

**[08:36]** actually measure AI return on investment in software engineering.

**[08:44]** Oh uh there we go. Okay. So here ideally

**[08:44]** Oh uh there we go. Okay. So here ideally we would be measuring this based on

**[08:45]** we would be measuring this based on

**[08:45]** we would be measuring this based on business outcomes right? I give my AI

**[08:47]** business outcomes right? I give my AI

**[08:48]** business outcomes right? I give my AI engineer my engineers AI and then I make

**[08:51]** engineer my engineers AI and then I make

**[08:51]** engineer my engineers AI and then I make more money more revenue net revenue

**[08:53]** more money more revenue net revenue

**[08:53]** more money more revenue net revenue retention whatever business KPI you want

**[08:54]** retention whatever business KPI you want

**[08:54]** retention whatever business KPI you want to track. The problem is that there's

**[08:58]** to track. The problem is that there's

**[08:58]** to track. The problem is that there's too much noise between the treatment


### [09:00 - 10:00]

**[09:00]** too much noise between the treatment

**[09:00]** too much noise between the treatment right giving AI and the result which is

**[09:02]** right giving AI and the result which is

**[09:02]** right giving AI and the result which is the business outcome and on top of this

**[09:05]** the business outcome and on top of this

**[09:05]** the business outcome and on top of this there's confounding variables such as

**[09:07]** there's confounding variables such as

**[09:07]** there's confounding variables such as your sales execution the macro

**[09:08]** your sales execution the macro

**[09:08]** your sales execution the macro environment your product strategy and

**[09:11]** environment your product strategy and

**[09:11]** environment your product strategy and therefore although that would be ideal

**[09:13]** therefore although that would be ideal

**[09:13]** therefore although that would be ideal unfortunately uh I think we need to find

**[09:15]** unfortunately uh I think we need to find

**[09:15]** unfortunately uh I think we need to find alternative paths and the most logical

**[09:17]** alternative paths and the most logical

**[09:17]** alternative paths and the most logical one is to simply look at the engineering

**[09:19]** one is to simply look at the engineering

**[09:19]** one is to simply look at the engineering outcomes because there is a clear signal

**[09:21]** outcomes because there is a clear signal

**[09:21]** outcomes because there is a clear signal right but here we need to go beyond

**[09:23]** right but here we need to go beyond

**[09:24]** right but here we need to go beyond measuring AI usage into measuring

**[09:26]** measuring AI usage into measuring

**[09:26]** measuring AI usage into measuring engineering outcomes. There's a few

**[09:28]** engineering outcomes. There's a few

**[09:28]** engineering outcomes. There's a few caveats and this topic is quite heavily

**[09:30]** caveats and this topic is quite heavily

**[09:30]** caveats and this topic is quite heavily discussed and so I want to mention some

**[09:32]** discussed and so I want to mention some

**[09:32]** discussed and so I want to mention some of them.

**[09:33]** of them.

**[09:33]** of them. The first one is that this is assuming

**[09:35]** The first one is that this is assuming

**[09:35]** The first one is that this is assuming that our product function can properly

**[09:37]** that our product function can properly

**[09:38]** that our product function can properly direct that increased capacity into

**[09:39]** direct that increased capacity into

**[09:39]** direct that increased capacity into something that generates value. And if

**[09:41]** something that generates value. And if

**[09:42]** something that generates value. And if they aren't directing that then it's a

**[09:43]** they aren't directing that then it's a

**[09:43]** they aren't directing that then it's a product problem which although sits

**[09:46]** product problem which although sits

**[09:46]** product problem which although sits quite close to engineering it's slightly

**[09:48]** quite close to engineering it's slightly

**[09:48]** quite close to engineering it's slightly different. Right?

**[09:50]** different. Right?

**[09:50]** different. Right? The second caveat is that this assumes

**[09:52]** The second caveat is that this assumes

**[09:52]** The second caveat is that this assumes that engineering is a meaningful

**[09:53]** that engineering is a meaningful

**[09:53]** that engineering is a meaningful bottleneck for value which frankly it

**[09:55]** bottleneck for value which frankly it

**[09:55]** bottleneck for value which frankly it typically is and that you can guard

**[09:57]** typically is and that you can guard

**[09:57]** typically is and that you can guard against good hards law by using a


### [10:00 - 11:00]

**[10:00]** against good hards law by using a

**[10:00]** against good hards law by using a balanced set of metrics and also by

**[10:02]** balanced set of metrics and also by

**[10:02]** balanced set of metrics and also by having a good company culture that

**[10:04]** having a good company culture that

**[10:04]** having a good company culture that doesn't weaponize these metrics.

**[10:06]** doesn't weaponize these metrics.

**[10:06]** doesn't weaponize these metrics. And thirdly is that AI is still very new

**[10:09]** And thirdly is that AI is still very new

**[10:09]** And thirdly is that AI is still very new and measuring proxy metrics is still

**[10:12]** and measuring proxy metrics is still

**[10:12]** and measuring proxy metrics is still better than not measuring. There's going

**[10:14]** better than not measuring. There's going

**[10:14]** better than not measuring. There's going to be winners and losers in this AI

**[10:16]** to be winners and losers in this AI

**[10:16]** to be winners and losers in this AI race. And progress is better than

**[10:18]** race. And progress is better than

**[10:18]** race. And progress is better than perfection here. And so metrics don't

**[10:20]** perfection here. And so metrics don't

**[10:20]** perfection here. And so metrics don't need to be flawless to be useful is what

**[10:22]** need to be flawless to be useful is what

**[10:22]** need to be flawless to be useful is what I want to illustrate.

**[10:33]** So then um here we have uh two parts

**[10:33]** So then um here we have uh two parts which you need to do to get the ROI from

**[10:35]** which you need to do to get the ROI from

**[10:35]** which you need to do to get the ROI from AI, right? You can need to measure usage

**[10:37]** AI, right? You can need to measure usage

**[10:37]** AI, right? You can need to measure usage and then you need to measure engineering

**[10:39]** and then you need to measure engineering

**[10:39]** and then you need to measure engineering outcomes. And so let's start with usage.

**[10:44]** outcomes. And so let's start with usage.

**[10:44]** outcomes. And so let's start with usage. There's really two buckets for

**[10:45]** There's really two buckets for

**[10:45]** There's really two buckets for enterprises. There's kind of more in a

**[10:47]** enterprises. There's kind of more in a

**[10:47]** enterprises. There's kind of more in a research environment, but to make it

**[10:48]** research environment, but to make it

**[10:48]** research environment, but to make it simple, there's access based and there's

**[10:50]** simple, there's access based and there's

**[10:50]** simple, there's access based and there's usage based. Accessbased is basically

**[10:52]** usage based. Accessbased is basically

**[10:52]** usage based. Accessbased is basically looking at when did people get access to

**[10:55]** looking at when did people get access to

**[10:55]** looking at when did people get access to the tool. And here we have you can kind

**[10:57]** the tool. And here we have you can kind

**[10:57]** the tool. And here we have you can kind of do a pilot group, give that group AI


### [11:00 - 12:00]

**[11:00]** of do a pilot group, give that group AI

**[11:00]** of do a pilot group, give that group AI and then compare it to a similar group

**[11:02]** and then compare it to a similar group

**[11:02]** and then compare it to a similar group without AI or you can measure the same

**[11:04]** without AI or you can measure the same

**[11:04]** without AI or you can measure the same team across time. The problem is that

**[11:06]** team across time. The problem is that

**[11:06]** team across time. The problem is that access based is noisy and the gold

**[11:09]** access based is noisy and the gold

**[11:09]** access based is noisy and the gold standard is really usage based which uh

**[11:12]** standard is really usage based which uh

**[11:12]** standard is really usage based which uh uses telemetry from APIs from these

**[11:15]** uses telemetry from APIs from these

**[11:15]** uses telemetry from APIs from these coding assistants right to uh give you

**[11:18]** coding assistants right to uh give you

**[11:18]** coding assistants right to uh give you the right data to know who's using AI

**[11:19]** the right data to know who's using AI

**[11:20]** the right data to know who's using AI and and where and the caveat here is

**[11:22]** and and where and the caveat here is

**[11:22]** and and where and the caveat here is that the vendor API is different

**[11:24]** that the vendor API is different

**[11:24]** that the vendor API is different unfortunately tools like GitHub copilot

**[11:26]** unfortunately tools like GitHub copilot

**[11:26]** unfortunately tools like GitHub copilot aggregate the data and other tools like

**[11:28]** aggregate the data and other tools like

**[11:28]** aggregate the data and other tools like cursor give you more granular data

**[11:31]** cursor give you more granular data

**[11:31]** cursor give you more granular data the big takeaway is that you can measure

**[11:33]** the big takeaway is that you can measure

**[11:33]** the big takeaway is that you can measure impact of um retroactively by using git

**[11:37]** impact of um retroactively by using git

**[11:37]** impact of um retroactively by using git history and so you don't need to set up

**[11:39]** history and so you don't need to set up

**[11:39]** history and so you don't need to set up an experiment now and wait 6 months you

**[11:41]** an experiment now and wait 6 months you

**[11:41]** an experiment now and wait 6 months you can actually if you've already adopted

**[11:42]** can actually if you've already adopted

**[11:42]** can actually if you've already adopted AI you can go back in time and and and

**[11:45]** AI you can go back in time and and and

**[11:45]** AI you can go back in time and and and do this it's quite easy

**[11:47]** do this it's quite easy

**[11:48]** do this it's quite easy now we've seen usage let's look into how

**[11:50]** now we've seen usage let's look into how

**[11:50]** now we've seen usage let's look into how do we actually measure engineering

**[11:51]** do we actually measure engineering

**[11:51]** do we actually measure engineering outcomes what are some of the metrics we

**[11:53]** outcomes what are some of the metrics we

**[11:53]** outcomes what are some of the metrics we propose


### [12:00 - 13:00]

**[12:03]** here we have um our framework which we

**[12:03]** here we have um our framework which we propose which is using a prim primary

**[12:04]** propose which is using a prim primary

**[12:04]** propose which is using a prim primary metric and a guardrail metric and so

**[12:07]** metric and a guardrail metric and so

**[12:07]** metric and a guardrail metric and so here um the primary metric is

**[12:09]** here um the primary metric is

**[12:09]** here um the primary metric is engineering output it's not lines of

**[12:10]** engineering output it's not lines of

**[12:10]** engineering output it's not lines of code it's not PR counts and it's not

**[12:12]** code it's not PR counts and it's not

**[12:12]** code it's not PR counts and it's not DORA and it's basically based on this

**[12:14]** DORA and it's basically based on this

**[12:14]** DORA and it's basically based on this machine learning model that replicates

**[12:15]** machine learning model that replicates

**[12:16]** machine learning model that replicates the panel of experts right and the

**[12:18]** the panel of experts right and the

**[12:18]** the panel of experts right and the second set of metrics are the guardrail

**[12:20]** second set of metrics are the guardrail

**[12:20]** second set of metrics are the guardrail ones which you want to maintain at a

**[12:21]** ones which you want to maintain at a

**[12:21]** ones which you want to maintain at a healthy level but you don't want to

**[12:23]** healthy level but you don't want to

**[12:23]** healthy level but you don't want to maximize it doesn't make sense to

**[12:25]** maximize it doesn't make sense to

**[12:25]** maximize it doesn't make sense to maximize them truly

**[12:27]** maximize them truly

**[12:27]** maximize them truly and so then there's three categories

**[12:29]** and so then there's three categories

**[12:29]** and so then there's three categories within the guardrail ones rework and

**[12:31]** within the guardrail ones rework and

**[12:31]** within the guardrail ones rework and refactoring quality tech and risk and

**[12:33]** refactoring quality tech and risk and

**[12:33]** refactoring quality tech and risk and then people and devops

**[12:34]** then people and devops

**[12:34]** then people and devops The third bucket is important to

**[12:36]** The third bucket is important to

**[12:36]** The third bucket is important to highlight that these are not

**[12:37]** highlight that these are not

**[12:37]** highlight that these are not productivity metrics. They're useful,

**[12:39]** productivity metrics. They're useful,

**[12:39]** productivity metrics. They're useful, but you cannot just kind of use them

**[12:41]** but you cannot just kind of use them

**[12:41]** but you cannot just kind of use them like maximize them to maximize developer

**[12:43]** like maximize them to maximize developer

**[12:43]** like maximize them to maximize developer productivity. They kind of fall off at

**[12:45]** productivity. They kind of fall off at

**[12:45]** productivity. They kind of fall off at some point. And so the goal here might

**[12:47]** some point. And so the goal here might

**[12:47]** some point. And so the goal here might be to keep your guardrail metrics

**[12:48]** be to keep your guardrail metrics

**[12:48]** be to keep your guardrail metrics healthy while increasing the primary

**[12:51]** healthy while increasing the primary

**[12:51]** healthy while increasing the primary metric to whatever degree possible.

**[12:54]** metric to whatever degree possible.

**[12:54]** metric to whatever degree possible. Now let's dive into a case study.

**[12:57]** Now let's dive into a case study.

**[12:57]** Now let's dive into a case study. Here we worked with


### [13:00 - 14:00]

**[13:01]** Here we worked with

**[13:01]** Here we worked with a company that uh large enterprise. We

**[13:03]** a company that uh large enterprise. We

**[13:04]** a company that uh large enterprise. We took a team of uh 350 people under a

**[13:06]** took a team of uh 350 people under a

**[13:06]** took a team of uh 350 people under a vice president and we measured pull

**[13:08]** vice president and we measured pull

**[13:08]** vice president and we measured pull requests. The reason we did this is to

**[13:11]** requests. The reason we did this is to

**[13:11]** requests. The reason we did this is to illustrate that you cannot measure pull

**[13:13]** illustrate that you cannot measure pull

**[13:13]** illustrate that you cannot measure pull requests to understand whether AI is

**[13:15]** requests to understand whether AI is

**[13:15]** requests to understand whether AI is helping you. And so here this team

**[13:17]** helping you. And so here this team

**[13:17]** helping you. And so here this team adopted um AI in May of this year and we

**[13:19]** adopted um AI in May of this year and we

**[13:19]** adopted um AI in May of this year and we measured the four months before 4 months

**[13:21]** measured the four months before 4 months

**[13:21]** measured the four months before 4 months after. We saw a 14% increase. Great.

**[13:24]** after. We saw a 14% increase. Great.

**[13:24]** after. We saw a 14% increase. Great. That's fantastic. But what about

**[13:26]** That's fantastic. But what about

**[13:26]** That's fantastic. But what about reviewer burden? What about code

**[13:28]** reviewer burden? What about code

**[13:28]** reviewer burden? What about code quality? So we measured code quality.

**[13:31]** quality? So we measured code quality.

**[13:31]** quality? So we measured code quality. And here what we saw is um I mean

**[13:34]** And here what we saw is um I mean

**[13:34]** And here what we saw is um I mean firstly actually code quality think of

**[13:36]** firstly actually code quality think of

**[13:36]** firstly actually code quality think of it as maintainability scale from 0 to

**[13:38]** it as maintainability scale from 0 to

**[13:38]** it as maintainability scale from 0 to 10. And uh there's kind of these bands.

**[13:41]** 10. And uh there's kind of these bands.

**[13:41]** 10. And uh there's kind of these bands. Uh it uses our our methodology. You can

**[13:43]** Uh it uses our our methodology. You can

**[13:43]** Uh it uses our our methodology. You can read it online. [snorts] But basically

**[13:46]** read it online. [snorts] But basically

**[13:46]** read it online. [snorts] But basically what you see is that in the preAI period

**[13:48]** what you see is that in the preAI period

**[13:48]** what you see is that in the preAI period their code quality was quite stable and

**[13:50]** their code quality was quite stable and

**[13:50]** their code quality was quite stable and consistent. And once they adopted AI two

**[13:52]** consistent. And once they adopted AI two

**[13:52]** consistent. And once they adopted AI two things happened. code quality decreased

**[13:54]** things happened. code quality decreased

**[13:54]** things happened. code quality decreased and then code quality became more

**[13:56]** and then code quality became more

**[13:56]** and then code quality became more erratic.


### [14:00 - 15:00]

**[14:01]** Next, we took a look at our metric which

**[14:01]** Next, we took a look at our metric which is engineering output. It's not lines of

**[14:03]** is engineering output. It's not lines of

**[14:03]** is engineering output. It's not lines of code. And here for every month, you see

**[14:05]** code. And here for every month, you see

**[14:05]** code. And here for every month, you see the sigma, the sum of the output

**[14:08]** the sigma, the sum of the output

**[14:08]** the sigma, the sum of the output delivered for that month broken down

**[14:09]** delivered for that month broken down

**[14:10]** delivered for that month broken down into four buckets. Rework and

**[14:12]** into four buckets. Rework and

**[14:12]** into four buckets. Rework and refactoring. So rework is when you're

**[14:14]** refactoring. So rework is when you're

**[14:14]** refactoring. So rework is when you're changing or editing code that was it's

**[14:17]** changing or editing code that was it's

**[14:17]** changing or editing code that was it's still kind of fresh, so it's recent.

**[14:18]** still kind of fresh, so it's recent.

**[14:18]** still kind of fresh, so it's recent. Refactoring is when you're changing code

**[14:20]** Refactoring is when you're changing code

**[14:20]** Refactoring is when you're changing code that's a bit older. And uh what uh then

**[14:24]** that's a bit older. And uh what uh then

**[14:24]** that's a bit older. And uh what uh then like added and removed it's pretty

**[14:26]** like added and removed it's pretty

**[14:26]** like added and removed it's pretty self-explanatory. And then also you can

**[14:28]** self-explanatory. And then also you can

**[14:28]** self-explanatory. And then also you can see these kind of benchmarks. So we can

**[14:30]** see these kind of benchmarks. So we can

**[14:30]** see these kind of benchmarks. So we can benchmark this company against similar

**[14:31]** benchmark this company against similar

**[14:31]** benchmark this company against similar companies in their industry. And here AI

**[14:34]** companies in their industry. And here AI

**[14:34]** companies in their industry. And here AI usage had two effects. Firstly is that

**[14:36]** usage had two effects. Firstly is that

**[14:36]** usage had two effects. Firstly is that rework went up by 2.5 times which is

**[14:39]** rework went up by 2.5 times which is

**[14:39]** rework went up by 2.5 times which is really bad. And effective output which

**[14:41]** really bad. And effective output which

**[14:41]** really bad. And effective output which is kind of like a proxy for productivity

**[14:43]** is kind of like a proxy for productivity

**[14:43]** is kind of like a proxy for productivity or so didn't really change.

**[14:45]** or so didn't really change.

**[14:45]** or so didn't really change. And so then what's the conclusion here?

**[14:47]** And so then what's the conclusion here?

**[14:47]** And so then what's the conclusion here? Let's do a recap. So we saw that PRs

**[14:49]** Let's do a recap. So we saw that PRs

**[14:50]** Let's do a recap. So we saw that PRs went up by 14%. But this is inconclusive

**[14:53]** went up by 14%. But this is inconclusive

**[14:53]** went up by 14%. But this is inconclusive because more PRs doesn't mean better. We

**[14:55]** because more PRs doesn't mean better. We

**[14:56]** because more PRs doesn't mean better. We saw that code quality decreased by 9%

**[14:58]** saw that code quality decreased by 9%

**[14:58]** saw that code quality decreased by 9% which is problematic. We saw that


### [15:00 - 16:00]

**[15:00]** which is problematic. We saw that

**[15:00]** which is problematic. We saw that effective output didn't increase

**[15:02]** effective output didn't increase

**[15:02]** effective output didn't increase meaningfully. And then we saw that

**[15:04]** meaningfully. And then we saw that

**[15:04]** meaningfully. And then we saw that rework increased by a lot. And so then

**[15:06]** rework increased by a lot. And so then

**[15:06]** rework increased by a lot. And so then the question here is what is the ROI of

**[15:09]** the question here is what is the ROI of

**[15:09]** the question here is what is the ROI of this AI adoption? Right? It might be

**[15:11]** this AI adoption? Right? It might be

**[15:11]** this AI adoption? Right? It might be negative. And what I want to point out

**[15:13]** negative. And what I want to point out

**[15:13]** negative. And what I want to point out here is that had this company not

**[15:14]** here is that had this company not

**[15:14]** here is that had this company not measured this more thoroughly and simply

**[15:16]** measured this more thoroughly and simply

**[15:16]** measured this more thoroughly and simply measured PR counts, they would have

**[15:18]** measured PR counts, they would have

**[15:18]** measured PR counts, they would have thought, hey, we're doing great. We

**[15:20]** thought, hey, we're doing great. We

**[15:20]** thought, hey, we're doing great. We increased our productivity by 14%. Let's

**[15:23]** increased our productivity by 14%. Let's

**[15:23]** increased our productivity by 14%. Let's run the numbers. That's how many million

**[15:25]** run the numbers. That's how many million

**[15:25]** run the numbers. That's how many million lots of millions of dollars. And does

**[15:26]** lots of millions of dollars. And does

**[15:26]** lots of millions of dollars. And does this offset the AI licenses? Sure thing

**[15:28]** this offset the AI licenses? Sure thing

**[15:28]** this offset the AI licenses? Sure thing it does, right? The other thing is that

**[15:31]** it does, right? The other thing is that

**[15:31]** it does, right? The other thing is that I don't think this company should

**[15:32]** I don't think this company should

**[15:32]** I don't think this company should abandon AI. They should simply use this

**[15:33]** abandon AI. They should simply use this

**[15:33]** abandon AI. They should simply use this data to understand what they're doing

**[15:35]** data to understand what they're doing

**[15:35]** data to understand what they're doing wrong. How can they improve? Because AI

**[15:37]** wrong. How can they improve? Because AI

**[15:37]** wrong. How can they improve? Because AI is here to stay. It's a tool that's

**[15:39]** is here to stay. It's a tool that's

**[15:39]** is here to stay. It's a tool that's going to transform how engineers are are

**[15:40]** going to transform how engineers are are

**[15:40]** going to transform how engineers are are working, right? and you can just um kind

**[15:43]** working, right? and you can just um kind

**[15:43]** working, right? and you can just um kind of like abandon it or so.

**[15:46]** of like abandon it or so.

**[15:46]** of like abandon it or so. Great. So, this concludes our insights

**[15:49]** Great. So, this concludes our insights

**[15:49]** Great. So, this concludes our insights for today. If you've enjoyed this uh

**[15:51]** for today. If you've enjoyed this uh

**[15:51]** for today. If you've enjoyed this uh talk and you would like similar insights

**[15:53]** talk and you would like similar insights

**[15:53]** talk and you would like similar insights for your company, I invite you to

**[15:54]** for your company, I invite you to

**[15:54]** for your company, I invite you to participate in our research. Everything

**[15:56]** participate in our research. Everything

**[15:56]** participate in our research. Everything you've seen today can uh be accessed

**[15:59]** you've seen today can uh be accessed

**[15:59]** you've seen today can uh be accessed through kind of participating in our


### [16:00 - 17:00]

**[16:00]** through kind of participating in our

**[16:00]** through kind of participating in our research, some of them through live

**[16:01]** research, some of them through live

**[16:01]** research, some of them through live dashboards in our research portal. And

**[16:04]** dashboards in our research portal. And

**[16:04]** dashboards in our research portal. And especially I'd like to invite companies

**[16:06]** especially I'd like to invite companies

**[16:06]** especially I'd like to invite companies that have access to cursor enterprise to

**[16:09]** that have access to cursor enterprise to

**[16:09]** that have access to cursor enterprise to participate because we have a high need

**[16:11]** participate because we have a high need

**[16:11]** participate because we have a high need for this so we can publish papers around

**[16:13]** for this so we can publish papers around

**[16:13]** for this so we can publish papers around the granularity of using AI um in

**[16:15]** the granularity of using AI um in

**[16:15]** the granularity of using AI um in software engineering. You can sign up at

**[16:17]** software engineering. You can sign up at

**[16:17]** software engineering. You can sign up at software engineering

**[16:18]** software engineering

**[16:18]** software engineering productivity.stanford.edu.

**[16:20]** productivity.stanford.edu.

**[16:20]** productivity.stanford.edu. Thank you so much.


