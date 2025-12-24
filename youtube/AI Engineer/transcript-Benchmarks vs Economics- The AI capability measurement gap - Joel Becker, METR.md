# Benchmarks vs Economics- The AI capability measurement gap - Joel Becker, METR

**Video URL:** https://youtu.be/RhfqQKe22ZA?si=Vnnz_4WhbF4wwHfm

---

## Full Transcript

### [00:00 - 01:00]

**[00:22]** Hey guys, thank you so much for having

**[00:22]** Hey guys, thank you so much for having me. My name is Joel Becker. I work as a

**[00:24]** me. My name is Joel Becker. I work as a

**[00:24]** me. My name is Joel Becker. I work as a researcher or member of technical staff

**[00:26]** researcher or member of technical staff

**[00:26]** researcher or member of technical staff at MET, which stands for model

**[00:29]** at MET, which stands for model

**[00:29]** at MET, which stands for model evaluation and threat research. As we'll

**[00:30]** evaluation and threat research. As we'll

**[00:30]** evaluation and threat research. As we'll see in a second, I'm going to be talking

**[00:31]** see in a second, I'm going to be talking

**[00:32]** see in a second, I'm going to be talking about AI capabilities. How do we know

**[00:34]** about AI capabilities. How do we know

**[00:34]** about AI capabilities. How do we know how performant AIs are today? How how

**[00:36]** how performant AIs are today? How how

**[00:36]** how performant AIs are today? How how performant they might be in the near

**[00:38]** performant they might be in the near

**[00:38]** performant they might be in the near future from these two different sources

**[00:39]** future from these two different sources

**[00:39]** future from these two different sources of evidence that seem to give somewhat

**[00:41]** of evidence that seem to give somewhat

**[00:41]** of evidence that seem to give somewhat conflicting answers. You know, I I could

**[00:44]** conflicting answers. You know, I I could

**[00:44]** conflicting answers. You know, I I could have done this whole talk without

**[00:45]** have done this whole talk without

**[00:45]** have done this whole talk without reference to meter papers in particular,

**[00:47]** reference to meter papers in particular,

**[00:47]** reference to meter papers in particular, but we'll look at two papers I've been

**[00:49]** but we'll look at two papers I've been

**[00:49]** but we'll look at two papers I've been um involved with as as examples of

**[00:51]** um involved with as as examples of

**[00:51]** um involved with as as examples of benchmark style evidence and then more

**[00:53]** benchmark style evidence and then more

**[00:53]** benchmark style evidence and then more economic style evidence. On the

**[00:55]** economic style evidence. On the

**[00:55]** economic style evidence. On the benchmark side, measuring AI ability to

**[00:57]** benchmark side, measuring AI ability to

**[00:57]** benchmark side, measuring AI ability to complete long tasks. This is the paper


### [01:00 - 02:00]

**[01:00]** complete long tasks. This is the paper

**[01:00]** complete long tasks. This is the paper um that comes with the the charts that

**[01:02]** um that comes with the the charts that

**[01:02]** um that comes with the the charts that many of you would have seen on on

**[01:03]** many of you would have seen on on

**[01:03]** many of you would have seen on on Twitter and so on that meter is well

**[01:04]** Twitter and so on that meter is well

**[01:04]** Twitter and so on that meter is well known for. And then the second this um

**[01:07]** known for. And then the second this um

**[01:07]** known for. And then the second this um RCT measuring how allowing AI affects

**[01:10]** RCT measuring how allowing AI affects

**[01:10]** RCT measuring how allowing AI affects developer productivity. And then we'll

**[01:12]** developer productivity. And then we'll

**[01:12]** developer productivity. And then we'll be talking about how to reconcile uh the

**[01:14]** be talking about how to reconcile uh the

**[01:14]** be talking about how to reconcile uh the the gap that's implied between these two

**[01:16]** the gap that's implied between these two

**[01:16]** the gap that's implied between these two different kinds of measurements.

**[01:19]** different kinds of measurements.

**[01:19]** different kinds of measurements. As I mentioned, META stands for model

**[01:21]** As I mentioned, META stands for model

**[01:21]** As I mentioned, META stands for model evaluation and threat research. We are a

**[01:23]** evaluation and threat research. We are a

**[01:23]** evaluation and threat research. We are a independent research nonprofit that

**[01:25]** independent research nonprofit that

**[01:25]** independent research nonprofit that seeks to inform the the public, policy

**[01:28]** seeks to inform the the public, policy

**[01:28]** seeks to inform the the public, policy makers, labs about the degree to which

**[01:30]** makers, labs about the degree to which

**[01:30]** makers, labs about the degree to which AIs might pose catastrophic risks to

**[01:33]** AIs might pose catastrophic risks to

**[01:33]** AIs might pose catastrophic risks to society. The model evaluation part uh

**[01:35]** society. The model evaluation part uh

**[01:35]** society. The model evaluation part uh means that we seek to understand AI

**[01:37]** means that we seek to understand AI

**[01:37]** means that we seek to understand AI capabilities and propensities. And the

**[01:39]** capabilities and propensities. And the

**[01:39]** capabilities and propensities. And the threat research part means we try to

**[01:41]** threat research part means we try to

**[01:41]** threat research part means we try to connect those capabilities and

**[01:42]** connect those capabilities and

**[01:42]** connect those capabilities and propensities to potential catastrophic

**[01:45]** propensities to potential catastrophic

**[01:45]** propensities to potential catastrophic risks.

**[01:47]** risks.

**[01:47]** risks. Okay. The first paper we're going to

**[01:48]** Okay. The first paper we're going to

**[01:48]** Okay. The first paper we're going to talk about associated with this chart

**[01:50]** talk about associated with this chart

**[01:50]** talk about associated with this chart that that many of you I think might have

**[01:51]** that that many of you I think might have

**[01:52]** that that many of you I think might have seen.

**[01:53]** seen.

**[01:53]** seen. Um take taking a step back first before

**[01:55]** Um take taking a step back first before

**[01:55]** Um take taking a step back first before we dive into the paper. You know how how

**[01:57]** we dive into the paper. You know how how

**[01:57]** we dive into the paper. You know how how usually do we think about measuring AI

**[01:59]** usually do we think about measuring AI

**[01:59]** usually do we think about measuring AI capabilities using benchmarks on a SWE


### [02:00 - 03:00]

**[02:02]** capabilities using benchmarks on a SWE

**[02:02]** capabilities using benchmarks on a SWE bench or a GPQA so on and so forth.

**[02:04]** bench or a GPQA so on and so forth.

**[02:04]** bench or a GPQA so on and so forth. There's some notion of 0% performance um

**[02:07]** There's some notion of 0% performance um

**[02:07]** There's some notion of 0% performance um or or random performance. So for GPQA

**[02:09]** or or random performance. So for GPQA

**[02:09]** or or random performance. So for GPQA that's that's 25% which corresponds to

**[02:11]** that's that's 25% which corresponds to

**[02:11]** that's that's 25% which corresponds to this flaw that the worst you can

**[02:13]** this flaw that the worst you can

**[02:13]** this flaw that the worst you can possibly do. Perhaps there's a um human

**[02:16]** possibly do. Perhaps there's a um human

**[02:16]** possibly do. Perhaps there's a um human baseline that's below 100% for GPQA. I

**[02:19]** baseline that's below 100% for GPQA. I

**[02:19]** baseline that's below 100% for GPQA. I think this is something like 75% that

**[02:22]** think this is something like 75% that

**[02:22]** think this is something like 75% that represents maybe expert human

**[02:23]** represents maybe expert human

**[02:23]** represents maybe expert human performance. And then of course you can

**[02:25]** performance. And then of course you can

**[02:25]** performance. And then of course you can go all the way up to 100% potentially on

**[02:27]** go all the way up to 100% potentially on

**[02:27]** go all the way up to 100% potentially on on these kinds of benchmarks. But but

**[02:29]** on these kinds of benchmarks. But but

**[02:29]** on these kinds of benchmarks. But but what does it mean? you know, if I'm

**[02:30]** what does it mean? you know, if I'm

**[02:30]** what does it mean? you know, if I'm getting 50% on GPQA, if I'm like half

**[02:32]** getting 50% on GPQA, if I'm like half

**[02:32]** getting 50% on GPQA, if I'm like half the way from the um from the floor to

**[02:35]** the way from the um from the floor to

**[02:35]** the way from the um from the floor to the to the expert baseline, what you

**[02:37]** the to the expert baseline, what you

**[02:37]** the to the expert baseline, what you know, what does that really mean about

**[02:38]** know, what does that really mean about

**[02:38]** know, what does that really mean about how performant the AIS are? If I meet

**[02:40]** how performant the AIS are? If I meet

**[02:40]** how performant the AIS are? If I meet the human baseline, does that mean that

**[02:42]** the human baseline, does that mean that

**[02:42]** the human baseline, does that mean that the AIS are now as performant or even

**[02:44]** the AIS are now as performant or even

**[02:44]** the AIS are now as performant or even more performant than than expert humans

**[02:46]** more performant than than expert humans

**[02:46]** more performant than than expert humans in in a relevant sense that I that I

**[02:48]** in in a relevant sense that I that I

**[02:48]** in in a relevant sense that I that I care about? It's hard to interpret. You

**[02:50]** care about? It's hard to interpret. You

**[02:50]** care about? It's hard to interpret. You know, another thing that you see from

**[02:52]** know, another thing that you see from

**[02:52]** know, another thing that you see from this graph is that um benchmarks seem to

**[02:56]** this graph is that um benchmarks seem to

**[02:56]** this graph is that um benchmarks seem to have less and less time between coming

**[02:58]** have less and less time between coming

**[02:58]** have less and less time between coming online sort of giving any signal at all


### [03:00 - 04:00]

**[03:01]** online sort of giving any signal at all

**[03:01]** online sort of giving any signal at all and being fully saturated. It's harder

**[03:03]** and being fully saturated. It's harder

**[03:04]** and being fully saturated. It's harder and harder to create benchmarks that

**[03:06]** and harder to create benchmarks that

**[03:06]** and harder to create benchmarks that have uh plenty of signal that you know

**[03:08]** have uh plenty of signal that you know

**[03:08]** have uh plenty of signal that you know might might be informative to us about

**[03:09]** might might be informative to us about

**[03:10]** might might be informative to us about how capable models are for for an

**[03:11]** how capable models are for for an

**[03:11]** how capable models are for for an extended period of time. So, we're we're

**[03:13]** extended period of time. So, we're we're

**[03:13]** extended period of time. So, we're we're going to go about this a different way.

**[03:16]** going to go about this a different way.

**[03:16]** going to go about this a different way. First, we're going to gather human

**[03:18]** First, we're going to gather human

**[03:18]** First, we're going to gather human baseline data for diverse tasks spanning

**[03:20]** baseline data for diverse tasks spanning

**[03:20]** baseline data for diverse tasks spanning a range of difficulties. You should

**[03:22]** a range of difficulties. You should

**[03:22]** a range of difficulties. You should think of these humans as, you know,

**[03:24]** think of these humans as, you know,

**[03:24]** think of these humans as, you know, experienced experts, but on their first

**[03:27]** experienced experts, but on their first

**[03:27]** experienced experts, but on their first day or or or first week on the job.

**[03:29]** day or or or first week on the job.

**[03:29]** day or or or first week on the job. These are not people with context on the

**[03:32]** These are not people with context on the

**[03:32]** These are not people with context on the tasks in particular. It's not exactly

**[03:34]** tasks in particular. It's not exactly

**[03:34]** tasks in particular. It's not exactly the kind of thing that's come up in

**[03:35]** the kind of thing that's come up in

**[03:35]** the kind of thing that's come up in their work before, but if it's a

**[03:36]** their work before, but if it's a

**[03:36]** their work before, but if it's a software engineering task, you know,

**[03:37]** software engineering task, you know,

**[03:37]** software engineering task, you know, there are relevantly skilled general

**[03:39]** there are relevantly skilled general

**[03:39]** there are relevantly skilled general software engineer. Same for the machine

**[03:41]** software engineer. Same for the machine

**[03:41]** software engineer. Same for the machine learning tasks and the cyber security

**[03:42]** learning tasks and the cyber security

**[03:42]** learning tasks and the cyber security tasks here that we'll talk about. the

**[03:45]** tasks here that we'll talk about. the

**[03:45]** tasks here that we'll talk about. the the [snorts] type of tasks come from

**[03:46]** the [snorts] type of tasks come from

**[03:46]** the [snorts] type of tasks come from these three um buckets or task

**[03:49]** these three um buckets or task

**[03:49]** these three um buckets or task distributions. Hcast which is a

**[03:52]** distributions. Hcast which is a

**[03:52]** distributions. Hcast which is a collection of um softwarebased tasks

**[03:54]** collection of um softwarebased tasks

**[03:54]** collection of um softwarebased tasks seemingly requiring autonomy you know

**[03:56]** seemingly requiring autonomy you know

**[03:56]** seemingly requiring autonomy you know interacting with tools um uh interacting

**[03:59]** interacting with tools um uh interacting

**[03:59]** interacting with tools um uh interacting with the environments thinking thinking


### [04:00 - 05:00]

**[04:01]** with the environments thinking thinking

**[04:01]** with the environments thinking thinking through the problem not not just this

**[04:02]** through the problem not not just this

**[04:02]** through the problem not not just this kind of Q&A style um style data set um

**[04:06]** kind of Q&A style um style data set um

**[04:06]** kind of Q&A style um style data set um the SWAR suite which are these atomic

**[04:08]** the SWAR suite which are these atomic

**[04:08]** the SWAR suite which are these atomic problems these are problems that you

**[04:10]** problems these are problems that you

**[04:10]** problems these are problems that you know maybe GBT2 can do maybe maybe it

**[04:12]** know maybe GBT2 can do maybe maybe it

**[04:12]** know maybe GBT2 can do maybe maybe it can't problems like um here are four

**[04:15]** can't problems like um here are four

**[04:15]** can't problems like um here are four files one of them is called

**[04:16]** files one of them is called

**[04:16]** files one of them is called passwords.txt txt which file contains

**[04:19]** passwords.txt txt which file contains

**[04:19]** passwords.txt txt which file contains the passwords and then on the other end

**[04:21]** the passwords and then on the other end

**[04:21]** the passwords and then on the other end of difficulty we have rebench which are

**[04:23]** of difficulty we have rebench which are

**[04:23]** of difficulty we have rebench which are challenging novel open-ended um machine

**[04:26]** challenging novel open-ended um machine

**[04:26]** challenging novel open-ended um machine learning research engineering challenges

**[04:28]** learning research engineering challenges

**[04:28]** learning research engineering challenges which are are very difficult even for

**[04:30]** which are are very difficult even for

**[04:30]** which are are very difficult even for top human experts

**[04:32]** top human experts

**[04:32]** top human experts in addition to gathering the the human

**[04:34]** in addition to gathering the the human

**[04:34]** in addition to gathering the the human baseline data we'll also under as close

**[04:36]** baseline data we'll also under as close

**[04:36]** baseline data we'll also under as close to identical conditions as possible

**[04:38]** to identical conditions as possible

**[04:38]** to identical conditions as possible measure AI performance for the AIs that

**[04:40]** measure AI performance for the AIs that

**[04:40]** measure AI performance for the AIs that we're that we're interested in on the

**[04:41]** we're that we're interested in on the

**[04:41]** we're that we're interested in on the same set of tasks and then we're going

**[04:44]** same set of tasks and then we're going

**[04:44]** same set of tasks and then we're going to convert the time it takes for humans

**[04:47]** to convert the time it takes for humans

**[04:47]** to convert the time it takes for humans to complete these tasks into an estimate

**[04:49]** to complete these tasks into an estimate

**[04:49]** to complete these tasks into an estimate of AI autonomous capabilities as I'll

**[04:52]** of AI autonomous capabilities as I'll

**[04:52]** of AI autonomous capabilities as I'll I'll show you in a second.

**[04:55]** I'll show you in a second.

**[04:55]** I'll show you in a second. Here's an illustrative diagram in this

**[04:57]** Here's an illustrative diagram in this

**[04:57]** Here's an illustrative diagram in this case for claw 3.7 Sonet which was the

**[04:59]** case for claw 3.7 Sonet which was the

**[04:59]** case for claw 3.7 Sonet which was the the frontier model at the time that this


### [05:00 - 06:00]

**[05:01]** the frontier model at the time that this

**[05:01]** the frontier model at the time that this paper came out. You can see that you

**[05:03]** paper came out. You can see that you

**[05:04]** paper came out. You can see that you know for the for the very short tasks

**[05:05]** know for the for the very short tasks

**[05:05]** know for the for the very short tasks something like 4 minutes or below Sonet

**[05:07]** something like 4 minutes or below Sonet

**[05:07]** something like 4 minutes or below Sonet is getting the answers correct you know

**[05:09]** is getting the answers correct you know

**[05:09]** is getting the answers correct you know essentially 100% of the time or or maybe

**[05:11]** essentially 100% of the time or or maybe

**[05:11]** essentially 100% of the time or or maybe even here literally 100% of the time.

**[05:13]** even here literally 100% of the time.

**[05:13]** even here literally 100% of the time. for the very hardest tasks it's

**[05:14]** for the very hardest tasks it's

**[05:14]** for the very hardest tasks it's struggling and then and then there's

**[05:15]** struggling and then and then there's

**[05:16]** struggling and then and then there's some range where we're kind of in the

**[05:17]** some range where we're kind of in the

**[05:17]** some range where we're kind of in the middle you know we're somewhere between

**[05:18]** middle you know we're somewhere between

**[05:18]** middle you know we're somewhere between 10 and 10 and 90%. I'll say that this

**[05:21]** 10 and 10 and 90%. I'll say that this

**[05:22]** 10 and 10 and 90%. I'll say that this empirical pattern where models are less

**[05:24]** empirical pattern where models are less

**[05:24]** empirical pattern where models are less performant at tasks that take humans

**[05:26]** performant at tasks that take humans

**[05:26]** performant at tasks that take humans longer is you know it's not a fact of

**[05:28]** longer is you know it's not a fact of

**[05:28]** longer is you know it's not a fact of nature but it's it's something that we

**[05:29]** nature but it's it's something that we

**[05:29]** nature but it's it's something that we see pretty pretty commonly pretty pretty

**[05:31]** see pretty pretty commonly pretty pretty

**[05:31]** see pretty pretty commonly pretty pretty robustly across models at least on this

**[05:33]** robustly across models at least on this

**[05:33]** robustly across models at least on this task distribution and I'd conjecture for

**[05:35]** task distribution and I'd conjecture for

**[05:35]** task distribution and I'd conjecture for for other task distributions as well. So

**[05:37]** for other task distributions as well. So

**[05:37]** for other task distributions as well. So we try and fit this dark purple line to

**[05:39]** we try and fit this dark purple line to

**[05:39]** we try and fit this dark purple line to to something like this data on on how

**[05:41]** to something like this data on on how

**[05:41]** to something like this data on on how long it took humans to complete the

**[05:43]** long it took humans to complete the

**[05:43]** long it took humans to complete the relevant tasks that the models are uh um

**[05:45]** relevant tasks that the models are uh um

**[05:45]** relevant tasks that the models are uh um are attempting. And then we call the

**[05:48]** are attempting. And then we call the

**[05:48]** are attempting. And then we call the point on the x-axis this horizontal axis

**[05:50]** point on the x-axis this horizontal axis

**[05:50]** point on the x-axis this horizontal axis this human time to complete axis at

**[05:53]** this human time to complete axis at

**[05:53]** this human time to complete axis at which we predict the models will succeed

**[05:55]** which we predict the models will succeed

**[05:55]** which we predict the models will succeed 50% of the time the time horizon of

**[05:59]** 50% of the time the time horizon of

**[05:59]** 50% of the time the time horizon of those models that there's much to debate


### [06:00 - 07:00]

**[06:01]** those models that there's much to debate

**[06:01]** those models that there's much to debate in the 50% number. I can I can talk

**[06:02]** in the 50% number. I can I can talk

**[06:02]** in the 50% number. I can I can talk later about the reasons why we chose

**[06:04]** later about the reasons why we chose

**[06:04]** later about the reasons why we chose that and and then we'll do the same

**[06:06]** that and and then we'll do the same

**[06:06]** that and and then we'll do the same exercise for the other models. So here I

**[06:08]** exercise for the other models. So here I

**[06:08]** exercise for the other models. So here I have uh claw 3 opus has a time horizon

**[06:11]** have uh claw 3 opus has a time horizon

**[06:11]** have uh claw 3 opus has a time horizon of something like 4 minutes. That's

**[06:12]** of something like 4 minutes. That's

**[06:12]** of something like 4 minutes. That's where we're predicting that it has a

**[06:14]** where we're predicting that it has a

**[06:14]** where we're predicting that it has a success probability on this task

**[06:16]** success probability on this task

**[06:16]** success probability on this task distribution of 50%. For 01 preview I'm

**[06:19]** distribution of 50%. For 01 preview I'm

**[06:19]** distribution of 50%. For 01 preview I'm seeing something like 15 minutes so on

**[06:21]** seeing something like 15 minutes so on

**[06:21]** seeing something like 15 minutes so on and so forth. And then of course all

**[06:22]** and so forth. And then of course all

**[06:22]** and so forth. And then of course all these models you know they they come out

**[06:24]** these models you know they they come out

**[06:24]** these models you know they they come out over um calendar time. So if we plot the

**[06:27]** over um calendar time. So if we plot the

**[06:27]** over um calendar time. So if we plot the time horizon, the x-coordinate on uh on

**[06:31]** time horizon, the x-coordinate on uh on

**[06:31]** time horizon, the x-coordinate on uh on on this set of plots against um against

**[06:33]** on this set of plots against um against

**[06:33]** on this set of plots against um against calendar's time, we find something like

**[06:34]** calendar's time, we find something like

**[06:34]** calendar's time, we find something like this. It looks, you know, kind of like

**[06:36]** this. It looks, you know, kind of like

**[06:36]** this. It looks, you know, kind of like um kind of like an exponential trend

**[06:38]** um kind of like an exponential trend

**[06:38]** um kind of like an exponential trend that's that's going up at some constant

**[06:40]** that's that's going up at some constant

**[06:40]** that's that's going up at some constant rate. In fact, it doesn't just look like

**[06:41]** rate. In fact, it doesn't just look like

**[06:42]** rate. In fact, it doesn't just look like an exponential trend. If we had a

**[06:43]** an exponential trend. If we had a

**[06:43]** an exponential trend. If we had a perfectly straight line here, it would

**[06:45]** perfectly straight line here, it would

**[06:45]** perfectly straight line here, it would indicate um a perfectly exponential

**[06:47]** indicate um a perfectly exponential

**[06:47]** indicate um a perfectly exponential trend. um we we see something really

**[06:49]** trend. um we we see something really

**[06:49]** trend. um we we see something really remarkably steady actually much more

**[06:51]** remarkably steady actually much more

**[06:51]** remarkably steady actually much more steady than we were anticipating when we

**[06:53]** steady than we were anticipating when we

**[06:53]** steady than we were anticipating when we uh went about doing this research

**[06:55]** uh went about doing this research

**[06:55]** uh went about doing this research project

**[06:57]** project

**[06:57]** project and that's continued to be the case. So


### [07:00 - 08:00]

**[07:00]** and that's continued to be the case. So

**[07:00]** and that's continued to be the case. So many of you will have seen updates that

**[07:01]** many of you will have seen updates that

**[07:01]** many of you will have seen updates that we've made of of this graph on on on

**[07:03]** we've made of of this graph on on on

**[07:03]** we've made of of this graph on on on Twitter. This is going all the way up to

**[07:05]** Twitter. This is going all the way up to

**[07:05]** Twitter. This is going all the way up to GPT 5.1 CEX max. So extremely recent um

**[07:08]** GPT 5.1 CEX max. So extremely recent um

**[07:08]** GPT 5.1 CEX max. So extremely recent um the predictions from this you know

**[07:10]** the predictions from this you know

**[07:10]** the predictions from this you know shockingly straight line have have held

**[07:12]** shockingly straight line have have held

**[07:12]** shockingly straight line have have held up very well I think.

**[07:16]** up very well I think.

**[07:16]** up very well I think. Taking a quick step back, what are

**[07:18]** Taking a quick step back, what are

**[07:18]** Taking a quick step back, what are benchmarks telling us or or here kind of

**[07:20]** benchmarks telling us or or here kind of

**[07:20]** benchmarks telling us or or here kind of benchmark like evidence? Well, one thing

**[07:22]** benchmark like evidence? Well, one thing

**[07:22]** benchmark like evidence? Well, one thing is that AIs can succeed at what for

**[07:24]** is that AIs can succeed at what for

**[07:24]** is that AIs can succeed at what for humans would be exceedingly difficult

**[07:27]** humans would be exceedingly difficult

**[07:27]** humans would be exceedingly difficult tasks. The tasks in our ebench are, you

**[07:29]** tasks. The tasks in our ebench are, you

**[07:29]** tasks. The tasks in our ebench are, you know, really far beyond my capabilities

**[07:32]** know, really far beyond my capabilities

**[07:32]** know, really far beyond my capabilities uh personally and and you know the AI is

**[07:34]** uh personally and and you know the AI is

**[07:34]** uh personally and and you know the AI is having a good crack at them some some

**[07:35]** having a good crack at them some some

**[07:35]** having a good crack at them some some decent percentage of the time. And the

**[07:37]** decent percentage of the time. And the

**[07:38]** decent percentage of the time. And the second's you know kind of obvious is

**[07:39]** second's you know kind of obvious is

**[07:39]** second's you know kind of obvious is that progress is rapid.

**[07:42]** that progress is rapid.

**[07:42]** that progress is rapid. >> [snorts]

**[07:42]** >> [snorts]

**[07:42]** >> [snorts] >> On the other hand, um you know, how much

**[07:44]** >> On the other hand, um you know, how much

**[07:44]** >> On the other hand, um you know, how much how much stock should we put in the um

**[07:46]** how much stock should we put in the um

**[07:46]** how much stock should we put in the um the evidence suggested by benchmarks? Um

**[07:49]** the evidence suggested by benchmarks? Um

**[07:49]** the evidence suggested by benchmarks? Um what limitations might they have? Lots,

**[07:52]** what limitations might they have? Lots,

**[07:52]** what limitations might they have? Lots, but here are here are three that I'll

**[07:54]** but here are here are three that I'll

**[07:54]** but here are here are three that I'll note. One is, as I mentioned, these are

**[07:57]** note. One is, as I mentioned, these are

**[07:57]** note. One is, as I mentioned, these are humans who are, you know, expert in some

**[07:59]** humans who are, you know, expert in some

**[07:59]** humans who are, you know, expert in some relevant sense, but they're low context.


### [08:00 - 09:00]

**[08:01]** relevant sense, but they're low context.

**[08:01]** relevant sense, but they're low context. It's something like their their first

**[08:02]** It's something like their their first

**[08:02]** It's something like their their first week on the job. They haven't seen tasks

**[08:04]** week on the job. They haven't seen tasks

**[08:04]** week on the job. They haven't seen tasks exactly like this previously. They just

**[08:05]** exactly like this previously. They just

**[08:05]** exactly like this previously. They just have some relevant experience.

**[08:07]** have some relevant experience.

**[08:07]** have some relevant experience. presumably people who were more sort of

**[08:10]** presumably people who were more sort of

**[08:10]** presumably people who were more sort of you know not not just having the

**[08:11]** you know not not just having the

**[08:11]** you know not not just having the relevant experience but also highly

**[08:13]** relevant experience but also highly

**[08:13]** relevant experience but also highly familiar with um uh with the with the

**[08:16]** familiar with um uh with the with the

**[08:16]** familiar with um uh with the with the set of tasks would perform the tasks

**[08:18]** set of tasks would perform the tasks

**[08:18]** set of tasks would perform the tasks even sooner and then we think relative

**[08:19]** even sooner and then we think relative

**[08:19]** even sooner and then we think relative to those people the AIs were more

**[08:21]** to those people the AIs were more

**[08:21]** to those people the AIs were more performant.

**[08:23]** performant.

**[08:23]** performant. The second is that benchmarks can be low

**[08:25]** The second is that benchmarks can be low

**[08:25]** The second is that benchmarks can be low ceiling. Even you know GPQA or use that

**[08:28]** ceiling. Even you know GPQA or use that

**[08:28]** ceiling. Even you know GPQA or use that example again um where we're beginning

**[08:32]** example again um where we're beginning

**[08:32]** example again um where we're beginning to get to the point where where that

**[08:33]** to get to the point where where that

**[08:33]** to get to the point where where that benchmark is um is totally saturated not

**[08:37]** benchmark is um is totally saturated not

**[08:37]** benchmark is um is totally saturated not providing um additional information for

**[08:39]** providing um additional information for

**[08:39]** providing um additional information for marginal models whereas time horizon is

**[08:41]** marginal models whereas time horizon is

**[08:41]** marginal models whereas time horizon is providing this nice way to sort of chain

**[08:43]** providing this nice way to sort of chain

**[08:43]** providing this nice way to sort of chain benchmarks together in in in some sense

**[08:45]** benchmarks together in in in some sense

**[08:45]** benchmarks together in in in some sense over time.

**[08:47]** over time.

**[08:47]** over time. Um but you know nonetheless it's still

**[08:49]** Um but you know nonetheless it's still

**[08:49]** Um but you know nonetheless it's still very hard to um uh to create these ever

**[08:52]** very hard to um uh to create these ever

**[08:52]** very hard to um uh to create these ever harder tasks when the um when the time

**[08:55]** harder tasks when the um when the time

**[08:55]** harder tasks when the um when the time horizon of models is doubling every

**[08:56]** horizon of models is doubling every

**[08:56]** horizon of models is doubling every something like six to seven months. So

**[08:58]** something like six to seven months. So

**[08:58]** something like six to seven months. So even time horizon might be might be


### [09:00 - 10:00]

**[09:00]** even time horizon might be might be

**[09:00]** even time horizon might be might be saturated in not too long or the

**[09:01]** saturated in not too long or the

**[09:02]** saturated in not too long or the benchmarks underlying time horizon.

**[09:04]** benchmarks underlying time horizon.

**[09:04]** benchmarks underlying time horizon. And the next one is you know not not a

**[09:06]** And the next one is you know not not a

**[09:06]** And the next one is you know not not a concern that's limited to the to the

**[09:08]** concern that's limited to the to the

**[09:08]** concern that's limited to the to the meter task to the task behind time

**[09:09]** meter task to the task behind time

**[09:10]** meter task to the task behind time horizon. It's also true for sweet bench.

**[09:11]** horizon. It's also true for sweet bench.

**[09:11]** horizon. It's also true for sweet bench. which is also true for for many of your

**[09:13]** which is also true for for many of your

**[09:13]** which is also true for for many of your um favorite agentic benchmarks that the

**[09:15]** um favorite agentic benchmarks that the

**[09:15]** um favorite agentic benchmarks that the problems aren't very messy in some

**[09:17]** problems aren't very messy in some

**[09:17]** problems aren't very messy in some sense. They don't require a ton of

**[09:19]** sense. They don't require a ton of

**[09:19]** sense. They don't require a ton of coordination with humans. They're often

**[09:21]** coordination with humans. They're often

**[09:21]** coordination with humans. They're often in relatively small contained

**[09:23]** in relatively small contained

**[09:23]** in relatively small contained environments where where not much can go

**[09:25]** environments where where not much can go

**[09:25]** environments where where not much can go wrong. You know, not these sort of

**[09:26]** wrong. You know, not these sort of

**[09:26]** wrong. You know, not these sort of massive open source code bases or or um

**[09:29]** massive open source code bases or or um

**[09:29]** massive open source code bases or or um other ways in which the the problems can

**[09:30]** other ways in which the the problems can

**[09:30]** other ways in which the the problems can involve more interaction with the real

**[09:31]** involve more interaction with the real

**[09:32]** involve more interaction with the real world or or or be messy in in some

**[09:33]** world or or or be messy in in some

**[09:34]** world or or or be messy in in some sense.

**[09:36]** sense.

**[09:36]** sense. Um so we did this we did this project

**[09:39]** Um so we did this we did this project

**[09:39]** Um so we did this we did this project and then um early this year we were you

**[09:41]** and then um early this year we were you

**[09:41]** and then um early this year we were you know we were trying to think about um uh

**[09:44]** know we were trying to think about um uh

**[09:44]** know we were trying to think about um uh how can we attack some of these

**[09:45]** how can we attack some of these

**[09:45]** how can we attack some of these limitations? What what's a different

**[09:46]** limitations? What what's a different

**[09:46]** limitations? What what's a different source of evidence that um might have

**[09:49]** source of evidence that um might have

**[09:49]** source of evidence that um might have its own own pros and cons but you know

**[09:51]** its own own pros and cons but you know

**[09:51]** its own own pros and cons but you know importantly be more externally valid in

**[09:53]** importantly be more externally valid in

**[09:53]** importantly be more externally valid in in the scientific jargon.

**[09:56]** in the scientific jargon.

**[09:56]** in the scientific jargon. Perhaps field experiments are the

**[09:57]** Perhaps field experiments are the

**[09:58]** Perhaps field experiments are the answer. [snorts] So more economic style

**[09:59]** answer. [snorts] So more economic style

**[09:59]** answer. [snorts] So more economic style evidence. So here we might be interested


### [10:00 - 11:00]

**[10:01]** evidence. So here we might be interested

**[10:02]** evidence. So here we might be interested in very high context developers who are

**[10:04]** in very high context developers who are

**[10:04]** in very high context developers who are expert on the kind of tasks they're

**[10:05]** expert on the kind of tasks they're

**[10:05]** expert on the kind of tasks they're already doing

**[10:07]** already doing

**[10:07]** already doing speed up or some notion of productivity

**[10:09]** speed up or some notion of productivity

**[10:09]** speed up or some notion of productivity boost. You know it seems to have more

**[10:11]** boost. You know it seems to have more

**[10:11]** boost. You know it seems to have more signal through even some um superhuman

**[10:13]** signal through even some um superhuman

**[10:13]** signal through even some um superhuman according to benchmarks range. You know

**[10:15]** according to benchmarks range. You know

**[10:15]** according to benchmarks range. You know perhaps GPQA is fully saturated and

**[10:17]** perhaps GPQA is fully saturated and

**[10:17]** perhaps GPQA is fully saturated and you're getting a 1.5x 2x speed up

**[10:19]** you're getting a 1.5x 2x speed up

**[10:19]** you're getting a 1.5x 2x speed up something like that but you can still

**[10:20]** something like that but you can still

**[10:20]** something like that but you can still achieve a 3x 4x 5x speed up even even

**[10:24]** achieve a 3x 4x 5x speed up even even

**[10:24]** achieve a 3x 4x 5x speed up even even after that we we maintain more signal.

**[10:26]** after that we we maintain more signal.

**[10:26]** after that we we maintain more signal. And the last is that you know that the

**[10:28]** And the last is that you know that the

**[10:28]** And the last is that you know that the tasks are messier. They are tasks that

**[10:31]** tasks are messier. They are tasks that

**[10:31]** tasks are messier. They are tasks that are coming up in people's real work.

**[10:32]** are coming up in people's real work.

**[10:32]** are coming up in people's real work. They're not um synthetic. They're not

**[10:34]** They're not um synthetic. They're not

**[10:34]** They're not um synthetic. They're not small and contained. Um this is a real

**[10:36]** small and contained. Um this is a real

**[10:36]** small and contained. Um this is a real deployment scenario.

**[10:42]** Here's what we're going to do for this

**[10:42]** Here's what we're going to do for this paper. We're going to gather 16

**[10:44]** paper. We're going to gather 16

**[10:44]** paper. We're going to gather 16 experienced developers on large mature

**[10:46]** experienced developers on large mature

**[10:46]** experienced developers on large mature open source projects that we'll go

**[10:47]** open source projects that we'll go

**[10:47]** open source projects that we'll go through in a second. Each of these

**[10:49]** through in a second. Each of these

**[10:50]** through in a second. Each of these developers will on average complete

**[10:51]** developers will on average complete

**[10:51]** developers will on average complete about 16 tasks from their real work.

**[10:54]** about 16 tasks from their real work.

**[10:54]** about 16 tasks from their real work. These are these are issues on the on the

**[10:56]** These are these are issues on the on the

**[10:56]** These are these are issues on the on the relevant GitHub repositories. The kind

**[10:57]** relevant GitHub repositories. The kind

**[10:57]** relevant GitHub repositories. The kind of thing that they might otherwise have

**[10:59]** of thing that they might otherwise have

**[10:59]** of thing that they might otherwise have completed with the with the caveat that


### [11:00 - 12:00]

**[11:00]** completed with the with the caveat that

**[11:00]** completed with the with the caveat that the very longest issues we're not going

**[11:02]** the very longest issues we're not going

**[11:02]** the very longest issues we're not going to include.

**[11:04]** to include.

**[11:04]** to include. The tasks will be randomly assigned to

**[11:07]** The tasks will be randomly assigned to

**[11:07]** The tasks will be randomly assigned to AI disallowed or AI allowed. AI

**[11:09]** AI disallowed or AI allowed. AI

**[11:09]** AI disallowed or AI allowed. AI disallowed, you know, it means it means

**[11:11]** disallowed, you know, it means it means

**[11:11]** disallowed, you know, it means it means what you think it means. It means

**[11:12]** what you think it means. It means

**[11:12]** what you think it means. It means software development in 2019. It means

**[11:14]** software development in 2019. It means

**[11:14]** software development in 2019. It means no AI powered tab autocomplete. It means

**[11:17]** no AI powered tab autocomplete. It means

**[11:17]** no AI powered tab autocomplete. It means no cursor agentic coding tools. It means

**[11:19]** no cursor agentic coding tools. It means

**[11:19]** no cursor agentic coding tools. It means no LLMs via the web UI.

**[11:23]** no LLMs via the web UI.

**[11:23]** no LLMs via the web UI. or they can be randomly assigned to AI

**[11:25]** or they can be randomly assigned to AI

**[11:25]** or they can be randomly assigned to AI allowed in which case everything's on

**[11:26]** allowed in which case everything's on

**[11:26]** allowed in which case everything's on the table. You know, any of the AI tools

**[11:28]** the table. You know, any of the AI tools

**[11:28]** the table. You know, any of the AI tools I just mentioned or not using the AI

**[11:30]** I just mentioned or not using the AI

**[11:30]** I just mentioned or not using the AI tools. If you're in the AI allowed

**[11:31]** tools. If you're in the AI allowed

**[11:31]** tools. If you're in the AI allowed condition, you're not compelled to use

**[11:33]** condition, you're not compelled to use

**[11:33]** condition, you're not compelled to use AI. You just have the option. And we buy

**[11:36]** AI. You just have the option. And we buy

**[11:36]** AI. You just have the option. And we buy these developers Cursor Pro. So, um for

**[11:39]** these developers Cursor Pro. So, um for

**[11:39]** these developers Cursor Pro. So, um for the for the most part, that's the tool

**[11:40]** the for the most part, that's the tool

**[11:40]** the for the most part, that's the tool that they're using with typically 3.6 or

**[11:42]** that they're using with typically 3.6 or

**[11:42]** that they're using with typically 3.6 or 3.7s on it at the time, uh which was the

**[11:45]** 3.7s on it at the time, uh which was the

**[11:45]** 3.7s on it at the time, uh which was the Frontier model when we conducted this

**[11:46]** Frontier model when we conducted this

**[11:46]** Frontier model when we conducted this work. And then we're going to record the

**[11:49]** work. And then we're going to record the

**[11:49]** work. And then we're going to record the time it takes for the developers to

**[11:50]** time it takes for the developers to

**[11:50]** time it takes for the developers to complete each task and see the degree to

**[11:53]** complete each task and see the degree to

**[11:53]** complete each task and see the degree to which they might save time when AI is

**[11:54]** which they might save time when AI is

**[11:54]** which they might save time when AI is allowed versus when it's not.

**[11:58]** allowed versus when it's not.

**[11:58]** allowed versus when it's not. These are some of the repositories. Many


### [12:00 - 13:00]

**[12:00]** These are some of the repositories. Many

**[12:00]** These are some of the repositories. Many of you will be familiar with them. We've

**[12:01]** of you will be familiar with them. We've

**[12:01]** of you will be familiar with them. We've got the Haskell compiler represented. We

**[12:03]** got the Haskell compiler represented. We

**[12:03]** got the Haskell compiler represented. We have scikitlearn. We have hugging face

**[12:05]** have scikitlearn. We have hugging face

**[12:05]** have scikitlearn. We have hugging face transformers. These are on average a

**[12:07]** transformers. These are on average a

**[12:07]** transformers. These are on average a million lines of code plus. They've been

**[12:09]** million lines of code plus. They've been

**[12:09]** million lines of code plus. They've been around for 10 plus years. The developers

**[12:12]** around for 10 plus years. The developers

**[12:12]** around for 10 plus years. The developers who are going to be working on these

**[12:13]** who are going to be working on these

**[12:13]** who are going to be working on these repositories as part of this study are

**[12:15]** repositories as part of this study are

**[12:15]** repositories as part of this study are on average the third top contributor out

**[12:17]** on average the third top contributor out

**[12:17]** on average the third top contributor out of hundreds or or even in some cases

**[12:19]** of hundreds or or even in some cases

**[12:19]** of hundreds or or even in some cases thousands of contributors to these

**[12:21]** thousands of contributors to these

**[12:21]** thousands of contributors to these repositories. They personally have been

**[12:23]** repositories. They personally have been

**[12:23]** repositories. They personally have been contributing to the repository for

**[12:24]** contributing to the repository for

**[12:24]** contributing to the repository for something like 5 years on average. These

**[12:26]** something like 5 years on average. These

**[12:26]** something like 5 years on average. These are top experts.

**[12:29]** are top experts.

**[12:29]** are top experts. Some of you might have seen this graph

**[12:31]** Some of you might have seen this graph

**[12:31]** Some of you might have seen this graph too. And and so the punch line's been

**[12:32]** too. And and so the punch line's been

**[12:32]** too. And and so the punch line's been spoiled for for the rest of you. Um we

**[12:35]** spoiled for for the rest of you. Um we

**[12:35]** spoiled for for the rest of you. Um we asked uh economics experts, machine

**[12:37]** asked uh economics experts, machine

**[12:37]** asked uh economics experts, machine learning experts, you know, these are

**[12:38]** learning experts, you know, these are

**[12:38]** learning experts, you know, these are people at major AI companies and labs,

**[12:41]** people at major AI companies and labs,

**[12:41]** people at major AI companies and labs, um uh top academics, um some graduate

**[12:43]** um uh top academics, um some graduate

**[12:43]** um uh top academics, um some graduate students, so on and so forth, you know,

**[12:45]** students, so on and so forth, you know,

**[12:45]** students, so on and so forth, you know, how much they expect developers to save

**[12:47]** how much they expect developers to save

**[12:47]** how much they expect developers to save time when they're using AI. They say

**[12:49]** time when they're using AI. They say

**[12:49]** time when they're using AI. They say something like 40% or a little bit less.

**[12:51]** something like 40% or a little bit less.

**[12:51]** something like 40% or a little bit less. We ask the developers themselves, the

**[12:53]** We ask the developers themselves, the

**[12:53]** We ask the developers themselves, the study participants, how much they expect

**[12:55]** study participants, how much they expect

**[12:55]** study participants, how much they expect to be sped up ahead of time, and they

**[12:56]** to be sped up ahead of time, and they

**[12:56]** to be sped up ahead of time, and they say something like 24 25%. Then we ask

**[12:59]** say something like 24 25%. Then we ask

**[12:59]** say something like 24 25%. Then we ask the developers after the study has been


### [13:00 - 14:00]

**[13:01]** the developers after the study has been

**[13:01]** the developers after the study has been completed how much they think they were

**[13:03]** completed how much they think they were

**[13:03]** completed how much they think they were sped up in the past by AI being allowed

**[13:07]** sped up in the past by AI being allowed

**[13:07]** sped up in the past by AI being allowed on the issues they completed as part of

**[13:09]** on the issues they completed as part of

**[13:09]** on the issues they completed as part of this study and they say that it will

**[13:11]** this study and they say that it will

**[13:11]** this study and they say that it will have sped them up by something like 20%.

**[13:13]** have sped them up by something like 20%.

**[13:13]** have sped them up by something like 20%. And the punch line is that we find that

**[13:15]** And the punch line is that we find that

**[13:15]** And the punch line is that we find that developers are slowed down by 19%. They

**[13:18]** developers are slowed down by 19%. They

**[13:18]** developers are slowed down by 19%. They take 19% more time when AI is allowed

**[13:21]** take 19% more time when AI is allowed

**[13:21]** take 19% more time when AI is allowed relative to when AI is not allowed.

**[13:24]** relative to when AI is not allowed.

**[13:24]** relative to when AI is not allowed. You know, when I first saw the data

**[13:26]** You know, when I first saw the data

**[13:26]** You know, when I first saw the data coming in, saw sort of early versions of

**[13:28]** coming in, saw sort of early versions of

**[13:28]** coming in, saw sort of early versions of this plot, um, I thought presumably the

**[13:30]** this plot, um, I thought presumably the

**[13:30]** this plot, um, I thought presumably the same thing that many of you might be

**[13:32]** same thing that many of you might be

**[13:32]** same thing that many of you might be thinking right now, that we've messed

**[13:33]** thinking right now, that we've messed

**[13:33]** thinking right now, that we've messed something up. Um, that that, you know,

**[13:35]** something up. Um, that that, you know,

**[13:35]** something up. Um, that that, you know, something's gone wrong. There's some

**[13:36]** something's gone wrong. There's some

**[13:36]** something's gone wrong. There's some there's some issue in in how we've set

**[13:38]** there's some issue in in how we've set

**[13:38]** there's some issue in in how we've set up the experiments. How could it

**[13:39]** up the experiments. How could it

**[13:39]** up the experiments. How could it possibly be the case? You know, at least

**[13:41]** possibly be the case? You know, at least

**[13:41]** possibly be the case? You know, at least these um, uh, these developers have

**[13:44]** these um, uh, these developers have

**[13:44]** these um, uh, these developers have access to the zero points because they

**[13:46]** access to the zero points because they

**[13:46]** access to the zero points because they cannot use AI at at any time. Um, so we

**[13:50]** cannot use AI at at any time. Um, so we

**[13:50]** cannot use AI at at any time. Um, so we poured over, you know, many, many, many,

**[13:53]** poured over, you know, many, many, many,

**[13:53]** poured over, you know, many, many, many, many, many hours of screen recordings

**[13:56]** many, many hours of screen recordings

**[13:56]** many, many hours of screen recordings from these developers working on issues

**[13:58]** from these developers working on issues

**[13:58]** from these developers working on issues as part of the study. We look to dive


### [14:00 - 15:00]

**[14:00]** as part of the study. We look to dive

**[14:00]** as part of the study. We look to dive into um, a bunch of hypotheses that

**[14:02]** into um, a bunch of hypotheses that

**[14:02]** into um, a bunch of hypotheses that might explain what's going on and try to

**[14:05]** might explain what's going on and try to

**[14:05]** might explain what's going on and try to categorize, you know, the things that

**[14:06]** categorize, you know, the things that

**[14:06]** categorize, you know, the things that that we think are going on versus not.

**[14:08]** that we think are going on versus not.

**[14:08]** that we think are going on versus not. Um, many of this is is listed in the

**[14:10]** Um, many of this is is listed in the

**[14:10]** Um, many of this is is listed in the paper. I I'll just quickly go through

**[14:11]** paper. I I'll just quickly go through

**[14:11]** paper. I I'll just quickly go through some of the things that we think are

**[14:13]** some of the things that we think are

**[14:13]** some of the things that we think are contributing.

**[14:14]** contributing.

**[14:14]** contributing. First, overoptimism about AI usefulness.

**[14:18]** First, overoptimism about AI usefulness.

**[14:18]** First, overoptimism about AI usefulness. that that seems like an obvious one. You

**[14:19]** that that seems like an obvious one. You

**[14:19]** that that seems like an obvious one. You know, the developers even after the

**[14:21]** know, the developers even after the

**[14:21]** know, the developers even after the study is completed, they think that um

**[14:23]** study is completed, they think that um

**[14:23]** study is completed, they think that um uh that AI is going to be helpful to

**[14:25]** uh that AI is going to be helpful to

**[14:25]** uh that AI is going to be helpful to their work. It's it makes sense they

**[14:26]** their work. It's it makes sense they

**[14:26]** their work. It's it makes sense they might overuse AI um on that basis. Um

**[14:30]** might overuse AI um on that basis. Um

**[14:30]** might overuse AI um on that basis. Um two more implicit repository context and

**[14:33]** two more implicit repository context and

**[14:33]** two more implicit repository context and high developer familiarity. You know,

**[14:35]** high developer familiarity. You know,

**[14:35]** high developer familiarity. You know, these developers are coming to these

**[14:36]** these developers are coming to these

**[14:36]** these developers are coming to these problems already knowing the solution to

**[14:38]** problems already knowing the solution to

**[14:38]** problems already knowing the solution to the problem. They don't they don't um

**[14:40]** the problem. They don't they don't um

**[14:40]** the problem. They don't they don't um they're so expert in this work. you

**[14:42]** they're so expert in this work. you

**[14:42]** they're so expert in this work. you know, I I I imagine them as as not

**[14:44]** know, I I I imagine them as as not

**[14:44]** know, I I I imagine them as as not trying to spend a bunch of time thinking

**[14:46]** trying to spend a bunch of time thinking

**[14:46]** trying to spend a bunch of time thinking through the solution that the the AI can

**[14:48]** through the solution that the the AI can

**[14:48]** through the solution that the the AI can can work through. Instead, they're just

**[14:49]** can work through. Instead, they're just

**[14:49]** can work through. Instead, they're just limited by how fast they can type. Um,

**[14:52]** limited by how fast they can type. Um,

**[14:52]** limited by how fast they can type. Um, which which means that, you know, using

**[14:54]** which which means that, you know, using

**[14:54]** which which means that, you know, using AI, instructing AIS to do it, um, comes

**[14:56]** AI, instructing AIS to do it, um, comes

**[14:56]** AI, instructing AIS to do it, um, comes with some significant time cost versus

**[14:57]** with some significant time cost versus

**[14:57]** with some significant time cost versus how they might otherwise have spent

**[14:58]** how they might otherwise have spent

**[14:58]** how they might otherwise have spent their time.


### [15:00 - 16:00]

**[15:00]** their time.

**[15:00]** their time. I think many of us have the sense that

**[15:02]** I think many of us have the sense that

**[15:02]** I think many of us have the sense that AIS might be less performant on on large

**[15:04]** AIS might be less performant on on large

**[15:04]** AIS might be less performant on on large and complex repositories, which is a

**[15:06]** and complex repositories, which is a

**[15:06]** and complex repositories, which is a different from this difference from this

**[15:07]** different from this difference from this

**[15:07]** different from this difference from this benchmark style evidence or or from or

**[15:09]** benchmark style evidence or or from or

**[15:09]** benchmark style evidence or or from or from some previous work. And then low AI

**[15:12]** from some previous work. And then low AI

**[15:12]** from some previous work. And then low AI reliability. You know, um maybe the AIs

**[15:15]** reliability. You know, um maybe the AIs

**[15:15]** reliability. You know, um maybe the AIs are very performant on these kinds of

**[15:17]** are very performant on these kinds of

**[15:17]** are very performant on these kinds of tasks, but you know, they're only

**[15:18]** tasks, but you know, they're only

**[15:18]** tasks, but you know, they're only performant um 50% of the time or 80% of

**[15:21]** performant um 50% of the time or 80% of

**[15:21]** performant um 50% of the time or 80% of the time, 20% of the time. And so, at

**[15:23]** the time, 20% of the time. And so, at

**[15:23]** the time, 20% of the time. And so, at the very least, you need to check their

**[15:25]** the very least, you need to check their

**[15:25]** the very least, you need to check their work afterwards. And perhaps even you

**[15:27]** work afterwards. And perhaps even you

**[15:27]** work afterwards. And perhaps even you need to spend time correcting their work

**[15:28]** need to spend time correcting their work

**[15:28]** need to spend time correcting their work afterwards, which is which is something

**[15:30]** afterwards, which is which is something

**[15:30]** afterwards, which is which is something we see quite a lot on these issues.

**[15:34]** we see quite a lot on these issues.

**[15:34]** we see quite a lot on these issues. One thing from the factors with an

**[15:35]** One thing from the factors with an

**[15:35]** One thing from the factors with an unclear effect that I that I'll mention

**[15:37]** unclear effect that I that I'll mention

**[15:37]** unclear effect that I that I'll mention briefly I have to talk to people about

**[15:38]** briefly I have to talk to people about

**[15:38]** briefly I have to talk to people about later is below average use of AI tools

**[15:40]** later is below average use of AI tools

**[15:40]** later is below average use of AI tools which came up in the public discussion.

**[15:43]** which came up in the public discussion.

**[15:43]** which came up in the public discussion. This this is in the unclear column

**[15:44]** This this is in the unclear column

**[15:44]** This this is in the unclear column because it's sort of evidence evidence

**[15:46]** because it's sort of evidence evidence

**[15:46]** because it's sort of evidence evidence for and against. Um that that's true for

**[15:48]** for and against. Um that that's true for

**[15:48]** for and against. Um that that's true for for many of the things here. We don't

**[15:50]** for many of the things here. We don't

**[15:50]** for many of the things here. We don't have anything so conclusive to say we're

**[15:52]** have anything so conclusive to say we're

**[15:52]** have anything so conclusive to say we're still working on on this line of work.

**[15:56]** still working on on this line of work.

**[15:56]** still working on on this line of work. Here are some here are some caveats. All

**[15:58]** Here are some here are some caveats. All

**[15:58]** Here are some here are some caveats. All important. Um first you know obviously


### [16:00 - 17:00]

**[16:00]** important. Um first you know obviously

**[16:00]** important. Um first you know obviously we do not provide evidence for all

**[16:01]** we do not provide evidence for all

**[16:01]** we do not provide evidence for all software developers or tasks. These are

**[16:04]** software developers or tasks. These are

**[16:04]** software developers or tasks. These are extremely experienced developers working

**[16:06]** extremely experienced developers working

**[16:06]** extremely experienced developers working on extremely complex longived open

**[16:09]** on extremely complex longived open

**[16:09]** on extremely complex longived open source repositories. I in my own work

**[16:11]** source repositories. I in my own work

**[16:12]** source repositories. I in my own work you know not um as expert in the

**[16:14]** you know not um as expert in the

**[16:14]** you know not um as expert in the relevant sense as as these people are.

**[16:16]** relevant sense as as these people are.

**[16:16]** relevant sense as as these people are. I'm working on much smaller

**[16:17]** I'm working on much smaller

**[16:17]** I'm working on much smaller repositories. Um I I feel more

**[16:19]** repositories. Um I I feel more

**[16:19]** repositories. Um I I feel more comfortable saying that even at this

**[16:20]** comfortable saying that even at this

**[16:20]** comfortable saying that even at this time I was sped up by AI tools even if

**[16:22]** time I was sped up by AI tools even if

**[16:22]** time I was sped up by AI tools even if even if the developers weren't. This

**[16:25]** even if the developers weren't. This

**[16:25]** even if the developers weren't. This setting is weird. It's weird for the

**[16:27]** setting is weird. It's weird for the

**[16:27]** setting is weird. It's weird for the same reasons that it's that it's

**[16:28]** same reasons that it's that it's

**[16:28]** same reasons that it's that it's interesting this this unusual developer

**[16:29]** interesting this this unusual developer

**[16:29]** interesting this this unusual developer population.

**[16:31]** population.

**[16:31]** population. Second, the experiment is concentrated

**[16:33]** Second, the experiment is concentrated

**[16:33]** Second, the experiment is concentrated in March 2025. As I mentioned, uh we

**[16:36]** in March 2025. As I mentioned, uh we

**[16:36]** in March 2025. As I mentioned, uh we know that AI progress is rapid. Um

**[16:38]** know that AI progress is rapid. Um

**[16:38]** know that AI progress is rapid. Um perhaps this this result will have

**[16:40]** perhaps this this result will have

**[16:40]** perhaps this this result will have already changed by the by the time I'm

**[16:42]** already changed by the by the time I'm

**[16:42]** already changed by the by the time I'm giving you this talk.

**[16:47]** So there's a kind of puzzle suggested

**[16:47]** So there's a kind of puzzle suggested right that the benchmark style evidence

**[16:49]** right that the benchmark style evidence

**[16:49]** right that the benchmark style evidence is giving um a very impressive sense of

**[16:52]** is giving um a very impressive sense of

**[16:52]** is giving um a very impressive sense of what benchmark of what AI capabilities

**[16:54]** what benchmark of what AI capabilities

**[16:54]** what benchmark of what AI capabilities look like today whereas the more

**[16:56]** look like today whereas the more

**[16:56]** look like today whereas the more economic style you know I include labor

**[16:58]** economic style you know I include labor

**[16:58]** economic style you know I include labor market impacts um uh uh working here too


### [17:00 - 18:00]

**[17:01]** market impacts um uh uh working here too

**[17:01]** market impacts um uh uh working here too in addition to our in addition to our

**[17:03]** in addition to our in addition to our

**[17:03]** in addition to our in addition to our field experiments look somewhat more

**[17:04]** field experiments look somewhat more

**[17:04]** field experiments look somewhat more bearish or or unimpressive. You know why

**[17:06]** bearish or or unimpressive. You know why

**[17:06]** bearish or or unimpressive. You know why why is the former not not translating to

**[17:08]** why is the former not not translating to

**[17:08]** why is the former not not translating to the latter at least naively there seems

**[17:10]** the latter at least naively there seems

**[17:10]** the latter at least naively there seems to be a clash. How might we go about

**[17:12]** to be a clash. How might we go about

**[17:12]** to be a clash. How might we go about resolving this puzzle?

**[17:15]** resolving this puzzle?

**[17:15]** resolving this puzzle? So one possibility is that in fact we we

**[17:17]** So one possibility is that in fact we we

**[17:17]** So one possibility is that in fact we we messed something up. This is this is

**[17:18]** messed something up. This is this is

**[17:18]** messed something up. This is this is still live and on the table. Uh you know

**[17:20]** still live and on the table. Uh you know

**[17:20]** still live and on the table. Uh you know maybe the developers really are um uh

**[17:22]** maybe the developers really are um uh

**[17:22]** maybe the developers really are um uh not very capable at using AI and if we

**[17:24]** not very capable at using AI and if we

**[17:24]** not very capable at using AI and if we continue to run this experiment as as in

**[17:26]** continue to run this experiment as as in

**[17:26]** continue to run this experiment as as in fact we are they'll you know learn more

**[17:28]** fact we are they'll you know learn more

**[17:28]** fact we are they'll you know learn more familiarity with the tools and and so

**[17:30]** familiarity with the tools and and so

**[17:30]** familiarity with the tools and and so get productivity benefits that they they

**[17:32]** get productivity benefits that they they

**[17:32]** get productivity benefits that they they weren't getting at the time. I'm a

**[17:34]** weren't getting at the time. I'm a

**[17:34]** weren't getting at the time. I'm a little skeptical of that story but but

**[17:35]** little skeptical of that story but but

**[17:35]** little skeptical of that story but but but that's one possibility.

**[17:38]** but that's one possibility.

**[17:38]** but that's one possibility. Another that economists like to bring up

**[17:39]** Another that economists like to bring up

**[17:39]** Another that economists like to bring up is that we're not incentivizing these

**[17:41]** is that we're not incentivizing these

**[17:41]** is that we're not incentivizing these developers to finish quickly. we're

**[17:43]** developers to finish quickly. we're

**[17:43]** developers to finish quickly. we're paying them per the hour, um, which we

**[17:45]** paying them per the hour, um, which we

**[17:45]** paying them per the hour, um, which we do for external validity reasons. Um,

**[17:48]** do for external validity reasons. Um,

**[17:48]** do for external validity reasons. Um, you know, looking through their videos,

**[17:49]** you know, looking through their videos,

**[17:49]** you know, looking through their videos, I I really, uh, do not think that

**[17:51]** I I really, uh, do not think that

**[17:51]** I I really, uh, do not think that they're developing differently in

**[17:53]** they're developing differently in

**[17:53]** they're developing differently in accordance with these incentives, but

**[17:54]** accordance with these incentives, but

**[17:54]** accordance with these incentives, but but that certainly is one possibility

**[17:55]** but that certainly is one possibility

**[17:55]** but that certainly is one possibility that's on the table.

**[17:58]** that's on the table.

**[17:58]** that's on the table. You know, another um, more statistical


### [18:00 - 19:00]

**[18:00]** You know, another um, more statistical

**[18:00]** You know, another um, more statistical in nature possibility is, you know, this

**[18:02]** in nature possibility is, you know, this

**[18:02]** in nature possibility is, you know, this is a small study. You shouldn't you

**[18:04]** is a small study. You shouldn't you

**[18:04]** is a small study. You shouldn't you shouldn't over update so much from small

**[18:06]** shouldn't over update so much from small

**[18:06]** shouldn't over update so much from small studies. We we are doing um, bigger

**[18:08]** studies. We we are doing um, bigger

**[18:08]** studies. We we are doing um, bigger things that I'm excited to release at

**[18:10]** things that I'm excited to release at

**[18:10]** things that I'm excited to release at some point. Okay, but let's let's assume

**[18:12]** some point. Okay, but let's let's assume

**[18:12]** some point. Okay, but let's let's assume we haven't messed something up and this

**[18:13]** we haven't messed something up and this

**[18:14]** we haven't messed something up and this is uh this this is a result um uh that

**[18:17]** is uh this this is a result um uh that

**[18:17]** is uh this this is a result um uh that that we think that we think does hold

**[18:19]** that we think that we think does hold

**[18:19]** that we think that we think does hold up. How could we resolve the puzzle?

**[18:22]** up. How could we resolve the puzzle?

**[18:22]** up. How could we resolve the puzzle? [snorts and sighs] So, one possibility,

**[18:23]** [snorts and sighs] So, one possibility,

**[18:23]** [snorts and sighs] So, one possibility, you know, as I as I alluded to briefly

**[18:25]** you know, as I as I alluded to briefly

**[18:25]** you know, as I as I alluded to briefly is that reliability needs to be very

**[18:27]** is that reliability needs to be very

**[18:27]** is that reliability needs to be very high to save time. That you need to be

**[18:29]** high to save time. That you need to be

**[18:30]** high to save time. That you need to be getting um the the answers these

**[18:32]** getting um the the answers these

**[18:32]** getting um the the answers these problems that developers are putting in

**[18:33]** problems that developers are putting in

**[18:33]** problems that developers are putting in correct. you know, something like 95 99%

**[18:36]** correct. you know, something like 95 99%

**[18:36]** correct. you know, something like 95 99% of the time in order for developers to

**[18:38]** of the time in order for developers to

**[18:38]** of the time in order for developers to tab tab tab through and you know, not

**[18:39]** tab tab tab through and you know, not

**[18:39]** tab tab tab through and you know, not not um not spend lots of time verifying

**[18:42]** not um not spend lots of time verifying

**[18:42]** not um not spend lots of time verifying the AI's work, which which of course um

**[18:44]** the AI's work, which which of course um

**[18:44]** the AI's work, which which of course um is pretty costly from a time

**[18:45]** is pretty costly from a time

**[18:45]** is pretty costly from a time perspective.

**[18:47]** perspective.

**[18:47]** perspective. Another possibility is bbenchlike or

**[18:50]** Another possibility is bbenchlike or

**[18:50]** Another possibility is bbenchlike or algorithmic costless scoring at the

**[18:52]** algorithmic costless scoring at the

**[18:52]** algorithmic costless scoring at the margin versus mergeability like scoring.

**[18:56]** margin versus mergeability like scoring.

**[18:56]** margin versus mergeability like scoring. Sweet scores are not trying to account

**[18:58]** Sweet scores are not trying to account

**[18:58]** Sweet scores are not trying to account for you know whether the code is spilled


### [19:00 - 20:00]

**[19:00]** for you know whether the code is spilled

**[19:00]** for you know whether the code is spilled honable by by other people in future or

**[19:03]** honable by by other people in future or

**[19:03]** honable by by other people in future or whether it's matching quality

**[19:04]** whether it's matching quality

**[19:04]** whether it's matching quality considerations that aren't um considered

**[19:06]** considerations that aren't um considered

**[19:06]** considerations that aren't um considered by the unit tests. You know perhaps AIS

**[19:08]** by the unit tests. You know perhaps AIS

**[19:08]** by the unit tests. You know perhaps AIS really are performance according to

**[19:10]** really are performance according to

**[19:10]** really are performance according to SWEBenchl like scoring but not

**[19:11]** SWEBenchl like scoring but not

**[19:11]** SWEBenchl like scoring but not performance according to this kind of

**[19:12]** performance according to this kind of

**[19:12]** performance according to this kind of more holistic um uh holistic scoring

**[19:15]** more holistic um uh holistic scoring

**[19:15]** more holistic um uh holistic scoring that we might care about low versus high

**[19:18]** that we might care about low versus high

**[19:18]** that we might care about low versus high context baseliners. I I I mentioned I

**[19:20]** context baseliners. I I I mentioned I

**[19:20]** context baseliners. I I I mentioned I mentioned previously these are just much

**[19:22]** mentioned previously these are just much

**[19:22]** mentioned previously these are just much more skilled humans, you know, relative

**[19:23]** more skilled humans, you know, relative

**[19:23]** more skilled humans, you know, relative to those humans. Perhaps the AIs are

**[19:25]** to those humans. Perhaps the AIs are

**[19:25]** to those humans. Perhaps the AIs are less capable. Task distribution, maybe

**[19:27]** less capable. Task distribution, maybe

**[19:27]** less capable. Task distribution, maybe these are just different kinds of tasks,

**[19:29]** these are just different kinds of tasks,

**[19:29]** these are just different kinds of tasks, you know, in particular less less messy

**[19:31]** you know, in particular less less messy

**[19:31]** you know, in particular less less messy than the than the benchmark style task.

**[19:32]** than the than the benchmark style task.

**[19:32]** than the than the benchmark style task. Maybe that's explaining what's going on

**[19:34]** Maybe that's explaining what's going on

**[19:34]** Maybe that's explaining what's going on here. [snorts] Suboptimal capability

**[19:36]** here. [snorts] Suboptimal capability

**[19:36]** here. [snorts] Suboptimal capability elicitation. A huge amount of work has

**[19:38]** elicitation. A huge amount of work has

**[19:38]** elicitation. A huge amount of work has gone in at meter to making the agents as

**[19:41]** gone in at meter to making the agents as

**[19:41]** gone in at meter to making the agents as performant as possible given the

**[19:42]** performant as possible given the

**[19:42]** performant as possible given the underlying models on on our kinds of

**[19:44]** underlying models on on our kinds of

**[19:44]** underlying models on on our kinds of tasks. And um you know that involves

**[19:46]** tasks. And um you know that involves

**[19:46]** tasks. And um you know that involves churning through a load of AI tokens.

**[19:49]** churning through a load of AI tokens.

**[19:49]** churning through a load of AI tokens. Perhaps that's that's less the case for

**[19:51]** Perhaps that's that's less the case for

**[19:51]** Perhaps that's that's less the case for cursor in particular at the time when we

**[19:53]** cursor in particular at the time when we

**[19:53]** cursor in particular at the time when we completed the study.

**[19:55]** completed the study.

**[19:55]** completed the study. And then interdependence across tasks.

**[19:57]** And then interdependence across tasks.

**[19:57]** And then interdependence across tasks. Maybe it's the case that um you know if

**[19:59]** Maybe it's the case that um you know if

**[19:59]** Maybe it's the case that um you know if humans can complete task A and task B.


### [20:00 - 21:00]

**[20:03]** humans can complete task A and task B.

**[20:03]** humans can complete task A and task B. AIS can only complete task A but not

**[20:04]** AIS can only complete task A but not

**[20:04]** AIS can only complete task A but not task B and of course can do task A

**[20:06]** task B and of course can do task A

**[20:06]** task B and of course can do task A faster. then it still makes sense to for

**[20:09]** faster. then it still makes sense to for

**[20:09]** faster. then it still makes sense to for humans to do task A and task B, not

**[20:11]** humans to do task A and task B, not

**[20:11]** humans to do task A and task B, not delegate task A because you know they

**[20:14]** delegate task A because you know they

**[20:14]** delegate task A because you know they they need to know the outputs. They need

**[20:15]** they need to know the outputs. They need

**[20:15]** they need to know the outputs. They need to know how how task A was completed in

**[20:17]** to know how how task A was completed in

**[20:17]** to know how how task A was completed in order to reliably complete task B. I

**[20:19]** order to reliably complete task B. I

**[20:19]** order to reliably complete task B. I think that's that's part of what's going

**[20:20]** think that's that's part of what's going

**[20:20]** think that's that's part of what's going on. You need to maintain context as

**[20:22]** on. You need to maintain context as

**[20:22]** on. You need to maintain context as you're working through these subtasks.

**[20:25]** you're working through these subtasks.

**[20:25]** you're working through these subtasks. Um lastly I will say that we are hiring

**[20:28]** Um lastly I will say that we are hiring

**[20:28]** Um lastly I will say that we are hiring not just for this kind of work that

**[20:30]** not just for this kind of work that

**[20:30]** not just for this kind of work that you've um that you've seen being

**[20:31]** you've um that you've seen being

**[20:32]** you've um that you've seen being extended you know ever longer tasks ever

**[20:34]** extended you know ever longer tasks ever

**[20:34]** extended you know ever longer tasks ever more ambitious um RCTs um even more

**[20:36]** more ambitious um RCTs um even more

**[20:36]** more ambitious um RCTs um even more sources of evidence from which we can

**[20:38]** sources of evidence from which we can

**[20:38]** sources of evidence from which we can triangulate the truth about AI

**[20:40]** triangulate the truth about AI

**[20:40]** triangulate the truth about AI capabilities but also for for much more

**[20:41]** capabilities but also for for much more

**[20:41]** capabilities but also for for much more besides you can you can find this at

**[20:43]** besides you can you can find this at

**[20:44]** besides you can you can find this at meter.org/careers org/careers. In

**[20:46]** meter.org/careers org/careers. In

**[20:46]** meter.org/careers org/careers. In particular, I'm excited about research

**[20:47]** particular, I'm excited about research

**[20:47]** particular, I'm excited about research engineers, research scientists who might

**[20:49]** engineers, research scientists who might

**[20:49]** engineers, research scientists who might be um hiding in the current audience.

**[20:51]** be um hiding in the current audience.

**[20:51]** be um hiding in the current audience. We're excited not just, you know, for

**[20:53]** We're excited not just, you know, for

**[20:53]** We're excited not just, you know, for for research types with academic

**[20:54]** for research types with academic

**[20:54]** for research types with academic experience, but very much for scrappy

**[20:56]** experience, but very much for scrappy

**[20:56]** experience, but very much for scrappy startup people as well. And we're also

**[20:59]** startup people as well. And we're also

**[20:59]** startup people as well. And we're also hiring for a director of operations.


### [21:00 - 22:00]

**[21:02]** hiring for a director of operations.

**[21:02]** hiring for a director of operations. And with that, thank you very much for

**[21:03]** And with that, thank you very much for

**[21:03]** And with that, thank you very much for listening.


