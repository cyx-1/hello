# Efficient Reinforcement Learning – Rhythm Garg & Linden Li, Applied Compute

**Video URL:** https://www.youtube.com/watch?v=o15AaYl7Wu0

---

## Full Transcript

### [00:00 - 01:00]

**[00:22]** Hey everyone, it's great to meet you

**[00:22]** Hey everyone, it's great to meet you all. Really great to be here today. My

**[00:24]** all. Really great to be here today. My

**[00:24]** all. Really great to be here today. My name is Rhythm. This is my co-founder

**[00:25]** name is Rhythm. This is my co-founder

**[00:25]** name is Rhythm. This is my co-founder Lyndon. Our third co-founder, Yash,

**[00:27]** Lyndon. Our third co-founder, Yash,

**[00:27]** Lyndon. Our third co-founder, Yash, couldn't make it today, but we're all

**[00:29]** couldn't make it today, but we're all

**[00:29]** couldn't make it today, but we're all very excited to be here. Um, three of us

**[00:31]** very excited to be here. Um, three of us

**[00:31]** very excited to be here. Um, three of us were previously researchers at OpenAI,

**[00:33]** were previously researchers at OpenAI,

**[00:33]** were previously researchers at OpenAI, and now we're bringing Frontier AI

**[00:35]** and now we're bringing Frontier AI

**[00:35]** and now we're bringing Frontier AI inside of enterprise at applied compute.

**[00:37]** inside of enterprise at applied compute.

**[00:38]** inside of enterprise at applied compute. Today, we're going to be talking about

**[00:39]** Today, we're going to be talking about

**[00:39]** Today, we're going to be talking about efficient reinforcement learning.

**[00:43]** efficient reinforcement learning.

**[00:43]** efficient reinforcement learning. As some context on applied compute, we

**[00:45]** As some context on applied compute, we

**[00:45]** As some context on applied compute, we help enterprises build their own

**[00:46]** help enterprises build their own

**[00:46]** help enterprises build their own intelligence to power real work in their

**[00:48]** intelligence to power real work in their

**[00:48]** intelligence to power real work in their company. We think a lot about how do we

**[00:51]** company. We think a lot about how do we

**[00:51]** company. We think a lot about how do we push AI beyond productivity into real

**[00:54]** push AI beyond productivity into real

**[00:54]** push AI beyond productivity into real automations that deliver ROI. that's

**[00:56]** automations that deliver ROI. that's

**[00:56]** automations that deliver ROI. that's quantitative for the company. Once we

**[00:58]** quantitative for the company. Once we

**[00:58]** quantitative for the company. Once we build a system that's specialized to the


### [01:00 - 02:00]

**[01:01]** build a system that's specialized to the

**[01:01]** build a system that's specialized to the way that a company operates for a

**[01:03]** way that a company operates for a

**[01:03]** way that a company operates for a particular use case, we deploy it with a

**[01:05]** particular use case, we deploy it with a

**[01:05]** particular use case, we deploy it with a data flywheel so that it gets better

**[01:07]** data flywheel so that it gets better

**[01:07]** data flywheel so that it gets better over time the more and more that you use

**[01:08]** over time the more and more that you use

**[01:08]** over time the more and more that you use it. Picture an in-house expert at a

**[01:11]** it. Picture an in-house expert at a

**[01:11]** it. Picture an in-house expert at a company that's always at the forefront

**[01:13]** company that's always at the forefront

**[01:13]** company that's always at the forefront of their field.

**[01:19]** RL mechanically is the is the tool that

**[01:19]** RL mechanically is the is the tool that we use in order to bring these out of

**[01:21]** we use in order to bring these out of

**[01:21]** we use in order to bring these out of distribution data sets in distribution

**[01:23]** distribution data sets in distribution

**[01:23]** distribution data sets in distribution for the models today. Yash Lyndon and I

**[01:25]** for the models today. Yash Lyndon and I

**[01:26]** for the models today. Yash Lyndon and I all worked on the RL effort at OpenAI in

**[01:28]** all worked on the RL effort at OpenAI in

**[01:28]** all worked on the RL effort at OpenAI in its early days and we saw firsthand the

**[01:31]** its early days and we saw firsthand the

**[01:31]** its early days and we saw firsthand the power of RL in going and maximizing

**[01:33]** power of RL in going and maximizing

**[01:33]** power of RL in going and maximizing these public benchmarks. Now we're

**[01:35]** these public benchmarks. Now we're

**[01:35]** these public benchmarks. Now we're taking that a step further and helping

**[01:38]** taking that a step further and helping

**[01:38]** taking that a step further and helping enterprises go solve the problems they

**[01:39]** enterprises go solve the problems they

**[01:39]** enterprises go solve the problems they care the most about sort of their

**[01:41]** care the most about sort of their

**[01:41]** care the most about sort of their private benchmarks.

**[01:47]** So here's a very highle overview of how

**[01:47]** So here's a very highle overview of how highMP compute RL helps LM acquire these

**[01:49]** highMP compute RL helps LM acquire these

**[01:49]** highMP compute RL helps LM acquire these reasoning and intelligence capabilities.

**[01:53]** reasoning and intelligence capabilities.

**[01:53]** reasoning and intelligence capabilities. Let's say that you have a data set of

**[01:54]** Let's say that you have a data set of

**[01:54]** Let's say that you have a data set of math problems and we pick four of them

**[01:57]** math problems and we pick four of them

**[01:57]** math problems and we pick four of them for an RL training step.


### [02:00 - 03:00]

**[02:01]** for an RL training step.

**[02:01]** for an RL training step. Then we'll take an open source model,

**[02:02]** Then we'll take an open source model,

**[02:02]** Then we'll take an open source model, say one of the GPOSS models or one of

**[02:04]** say one of the GPOSS models or one of

**[02:04]** say one of the GPOSS models or one of the llama models, and we have the model

**[02:06]** the llama models, and we have the model

**[02:06]** the llama models, and we have the model attempt each of those four problems 100

**[02:08]** attempt each of those four problems 100

**[02:08]** attempt each of those four problems 100 times. So each of these 100 attempts is

**[02:12]** times. So each of these 100 attempts is

**[02:12]** times. So each of these 100 attempts is the model thinking through how it would

**[02:14]** the model thinking through how it would

**[02:14]** the model thinking through how it would get to the final answer and then ending

**[02:15]** get to the final answer and then ending

**[02:15]** get to the final answer and then ending off with with the final answer itself.

**[02:17]** off with with the final answer itself.

**[02:17]** off with with the final answer itself. And these are many many reasoning tokens

**[02:19]** And these are many many reasoning tokens

**[02:19]** And these are many many reasoning tokens in its thinking trajectory.

**[02:21]** in its thinking trajectory.

**[02:21]** in its thinking trajectory. We can grade all of these answers

**[02:24]** We can grade all of these answers

**[02:24]** We can grade all of these answers and when the model is correct, we can

**[02:26]** and when the model is correct, we can

**[02:26]** and when the model is correct, we can bias the model's weights to reinforce

**[02:29]** bias the model's weights to reinforce

**[02:29]** bias the model's weights to reinforce its thinking trace in that attempt. When

**[02:31]** its thinking trace in that attempt. When

**[02:31]** its thinking trace in that attempt. When it's incorrect, we can discourage the

**[02:32]** it's incorrect, we can discourage the

**[02:32]** it's incorrect, we can discourage the model from having that kind of behavior

**[02:34]** model from having that kind of behavior

**[02:34]** model from having that kind of behavior again. So in this fashion, as we train

**[02:36]** again. So in this fashion, as we train

**[02:36]** again. So in this fashion, as we train do more and more training steps with

**[02:38]** do more and more training steps with

**[02:38]** do more and more training steps with batches of four problems, 100 attempts

**[02:40]** batches of four problems, 100 attempts

**[02:40]** batches of four problems, 100 attempts each, the model learns to reason and

**[02:42]** each, the model learns to reason and

**[02:42]** each, the model learns to reason and solve math problems, and it becomes

**[02:43]** solve math problems, and it becomes

**[02:43]** solve math problems, and it becomes really, really good at math. Of course,

**[02:45]** really, really good at math. Of course,

**[02:45]** really, really good at math. Of course, at Applied Compute, we're not really

**[02:46]** at Applied Compute, we're not really

**[02:46]** at Applied Compute, we're not really helping enterprises solve math problems,

**[02:48]** helping enterprises solve math problems,

**[02:48]** helping enterprises solve math problems, but this is kind of the mechanism by

**[02:49]** but this is kind of the mechanism by

**[02:50]** but this is kind of the mechanism by which we're able to teach the models to

**[02:51]** which we're able to teach the models to

**[02:51]** which we're able to teach the models to get really, really good at tasks that

**[02:53]** get really, really good at tasks that

**[02:53]** get really, really good at tasks that they care about.

**[02:56]** they care about.

**[02:56]** they care about. So, as we mentioned, the type of RL work

**[02:58]** So, as we mentioned, the type of RL work

**[02:58]** So, as we mentioned, the type of RL work that we do at Applied Compute is

**[02:59]** that we do at Applied Compute is


### [03:00 - 04:00]

**[03:00]** that we do at Applied Compute is actually quite different from the lab.

**[03:01]** actually quite different from the lab.

**[03:01]** actually quite different from the lab. So, the these are some real life photos

**[03:02]** So, the these are some real life photos

**[03:02]** So, the these are some real life photos from from the labs and a photo we took

**[03:05]** from from the labs and a photo we took

**[03:05]** from from the labs and a photo we took at the at the applied comput office the

**[03:06]** at the at the applied comput office the

**[03:06]** at the at the applied comput office the other day. Um, they you know, the labs

**[03:09]** other day. Um, they you know, the labs

**[03:09]** other day. Um, they you know, the labs do these big training runs over several

**[03:11]** do these big training runs over several

**[03:11]** do these big training runs over several weeks. We do more specialized runs

**[03:15]** weeks. We do more specialized runs

**[03:15]** weeks. We do more specialized runs And you know, there's a couple of

**[03:16]** And you know, there's a couple of

**[03:16]** And you know, there's a couple of aspects of RO training that are

**[03:18]** aspects of RO training that are

**[03:18]** aspects of RO training that are particularly important to us.

**[03:21]** particularly important to us.

**[03:21]** particularly important to us. We need our runs to be fast so that we

**[03:23]** We need our runs to be fast so that we

**[03:23]** We need our runs to be fast so that we can train a model and deliver it to a

**[03:24]** can train a model and deliver it to a

**[03:24]** can train a model and deliver it to a customer very quickly on the order of

**[03:26]** customer very quickly on the order of

**[03:26]** customer very quickly on the order of days.

**[03:27]** days.

**[03:27]** days. They have to be cheap so that our unit

**[03:29]** They have to be cheap so that our unit

**[03:29]** They have to be cheap so that our unit costs work and we're able to scale the

**[03:31]** costs work and we're able to scale the

**[03:31]** costs work and we're able to scale the business sustainably.

**[03:33]** business sustainably.

**[03:33]** business sustainably. And importantly, and this is a point

**[03:35]** And importantly, and this is a point

**[03:35]** And importantly, and this is a point that I think um you know it's it's easy

**[03:37]** that I think um you know it's it's easy

**[03:37]** that I think um you know it's it's easy to miss, we need our estimates for how

**[03:39]** to miss, we need our estimates for how

**[03:39]** to miss, we need our estimates for how long these training jobs will be to be

**[03:41]** long these training jobs will be to be

**[03:41]** long these training jobs will be to be very low variance because we don't want

**[03:43]** very low variance because we don't want

**[03:43]** very low variance because we don't want to just be generally fast. We want to be

**[03:44]** to just be generally fast. We want to be

**[03:44]** to just be generally fast. We want to be reliably fast when we work with

**[03:46]** reliably fast when we work with

**[03:46]** reliably fast when we work with customers.

**[03:48]** customers.

**[03:48]** customers. And so the research problem for us that

**[03:50]** And so the research problem for us that

**[03:50]** And so the research problem for us that is very business critical is can we

**[03:53]** is very business critical is can we

**[03:53]** is very business critical is can we build an RL stack that is so efficient

**[03:56]** build an RL stack that is so efficient

**[03:56]** build an RL stack that is so efficient so that in conjunction with our agent

**[03:58]** so that in conjunction with our agent

**[03:58]** so that in conjunction with our agent building platform we are really able to


### [04:00 - 05:00]

**[04:00]** building platform we are really able to

**[04:00]** building platform we are really able to scale up this use case specific training

**[04:03]** scale up this use case specific training

**[04:03]** scale up this use case specific training motion.

**[04:08]** So let's start with an inefficient form

**[04:08]** So let's start with an inefficient form of RL which is synchronous RL. In

**[04:11]** of RL which is synchronous RL. In

**[04:11]** of RL which is synchronous RL. In synchronous RL sampling and training

**[04:13]** synchronous RL sampling and training

**[04:13]** synchronous RL sampling and training happen in lock step. So there's some

**[04:15]** happen in lock step. So there's some

**[04:15]** happen in lock step. So there's some simplifications here, but but let's say

**[04:16]** simplifications here, but but let's say

**[04:16]** simplifications here, but but let's say that we want to train on batches of

**[04:18]** that we want to train on batches of

**[04:18]** that we want to train on batches of eight samples. That means we're going to

**[04:20]** eight samples. That means we're going to

**[04:20]** eight samples. That means we're going to wait for all eight samples to finish and

**[04:23]** wait for all eight samples to finish and

**[04:23]** wait for all eight samples to finish and basically finish completion before we

**[04:25]** basically finish completion before we

**[04:25]** basically finish completion before we start training. And then we're going to

**[04:26]** start training. And then we're going to

**[04:26]** start training. And then we're going to repeat this process again. As a result,

**[04:29]** repeat this process again. As a result,

**[04:29]** repeat this process again. As a result, we have a lot of idle GPUs that are

**[04:31]** we have a lot of idle GPUs that are

**[04:31]** we have a lot of idle GPUs that are waiting on that third straggler sample

**[04:33]** waiting on that third straggler sample

**[04:33]** waiting on that third straggler sample to complete.

**[04:38]** So in other words, in synchronous RL,

**[04:38]** So in other words, in synchronous RL, our step times are dictated by whatever

**[04:40]** our step times are dictated by whatever

**[04:40]** our step times are dictated by whatever sample takes the longest time in order

**[04:41]** sample takes the longest time in order

**[04:41]** sample takes the longest time in order to complete.

**[04:43]** to complete.

**[04:43]** to complete. To illustrate why this is bad, we took

**[04:45]** To illustrate why this is bad, we took

**[04:45]** To illustrate why this is bad, we took 40 arithmetic problems, requested 32

**[04:48]** 40 arithmetic problems, requested 32

**[04:48]** 40 arithmetic problems, requested 32 samples each for each of them with quen

**[04:50]** samples each for each of them with quen

**[04:50]** samples each for each of them with quen 30B, and we measured how long it would

**[04:52]** 30B, and we measured how long it would

**[04:52]** 30B, and we measured how long it would take for the for these samples to

**[04:54]** take for the for these samples to

**[04:54]** take for the for these samples to complete.

**[04:56]** complete.

**[04:56]** complete. It turns out that 99% of the samples

**[04:57]** It turns out that 99% of the samples

**[04:58]** It turns out that 99% of the samples completed in about 40 seconds. Took

**[04:59]** completed in about 40 seconds. Took


### [05:00 - 06:00]

**[05:00]** completed in about 40 seconds. Took another 80 seconds to get that last

**[05:01]** another 80 seconds to get that last

**[05:01]** another 80 seconds to get that last percent of samples to complete. It

**[05:03]** percent of samples to complete. It

**[05:03]** percent of samples to complete. It really has a long tail.

**[05:06]** really has a long tail.

**[05:06]** really has a long tail. So, as you'd expect, if you look at the

**[05:08]** So, as you'd expect, if you look at the

**[05:08]** So, as you'd expect, if you look at the throughput chart, the GPUs are doing a

**[05:10]** throughput chart, the GPUs are doing a

**[05:10]** throughput chart, the GPUs are doing a lot of work at the beginning when all of

**[05:11]** lot of work at the beginning when all of

**[05:11]** lot of work at the beginning when all of the sampling requests are launched, but

**[05:13]** the sampling requests are launched, but

**[05:13]** the sampling requests are launched, but by the end, they're very very

**[05:14]** by the end, they're very very

**[05:14]** by the end, they're very very underutilized because they're waiting on

**[05:16]** underutilized because they're waiting on

**[05:16]** underutilized because they're waiting on those last samples to complete. The

**[05:18]** those last samples to complete. The

**[05:18]** those last samples to complete. The technical term we use at applied compute

**[05:19]** technical term we use at applied compute

**[05:19]** technical term we use at applied compute is the GPUs are slacking. Um, so

**[05:21]** is the GPUs are slacking. Um, so

**[05:21]** is the GPUs are slacking. Um, so synchronous RL is not an efficient way

**[05:23]** synchronous RL is not an efficient way

**[05:23]** synchronous RL is not an efficient way to to use these GPUs.

**[05:27]** to to use these GPUs.

**[05:27]** to to use these GPUs. In order to solve this problem, we need

**[05:28]** In order to solve this problem, we need

**[05:28]** In order to solve this problem, we need to break the condition that sampling and

**[05:31]** to break the condition that sampling and

**[05:31]** to break the condition that sampling and training need to happen in lock step. In

**[05:34]** training need to happen in lock step. In

**[05:34]** training need to happen in lock step. In other words, we need to allow training

**[05:35]** other words, we need to allow training

**[05:35]** other words, we need to allow training while we're sampling. This is called

**[05:37]** while we're sampling. This is called

**[05:37]** while we're sampling. This is called asynchronous RL. And there are many

**[05:39]** asynchronous RL. And there are many

**[05:39]** asynchronous RL. And there are many approaches to doing asynchronous RL. One

**[05:41]** approaches to doing asynchronous RL. One

**[05:41]** approaches to doing asynchronous RL. One that we particularly like is pipeline RL

**[05:43]** that we particularly like is pipeline RL

**[05:43]** that we particularly like is pipeline RL from P at all.

**[05:46]** from P at all.

**[05:46]** from P at all. We're going to make some simp

**[05:47]** We're going to make some simp

**[05:47]** We're going to make some simp simplifications here, but in

**[05:49]** simplifications here, but in

**[05:49]** simplifications here, but in asynchronous pipeline RL, we dedicate

**[05:51]** asynchronous pipeline RL, we dedicate

**[05:51]** asynchronous pipeline RL, we dedicate some GPUs to sampling and some GPUs to

**[05:53]** some GPUs to sampling and some GPUs to

**[05:53]** some GPUs to sampling and some GPUs to training. The sampling workers never

**[05:55]** training. The sampling workers never

**[05:55]** training. The sampling workers never stop. They're constantly doing inference

**[05:57]** stop. They're constantly doing inference

**[05:57]** stop. They're constantly doing inference with high batch size. As samples

**[05:59]** with high batch size. As samples

**[05:59]** with high batch size. As samples complete, they get added to a queue for


### [06:00 - 07:00]

**[06:01]** complete, they get added to a queue for

**[06:01]** complete, they get added to a queue for training and the training workers pull a

**[06:03]** training and the training workers pull a

**[06:03]** training and the training workers pull a batch from the queue to train on. After

**[06:06]** batch from the queue to train on. After

**[06:06]** batch from the queue to train on. After a a batch has been trained on, the

**[06:09]** a a batch has been trained on, the

**[06:09]** a a batch has been trained on, the training workers propagate the new model

**[06:11]** training workers propagate the new model

**[06:11]** training workers propagate the new model weights to all of the sampling workers

**[06:13]** weights to all of the sampling workers

**[06:13]** weights to all of the sampling workers for what's called an in-flight weight

**[06:14]** for what's called an in-flight weight

**[06:14]** for what's called an in-flight weight update. And this is really what

**[06:15]** update. And this is really what

**[06:16]** update. And this is really what differentiates pipeline RL. The sampling

**[06:18]** differentiates pipeline RL. The sampling

**[06:18]** differentiates pipeline RL. The sampling workers might be in the middle of a

**[06:19]** workers might be in the middle of a

**[06:19]** workers might be in the middle of a sample, but their weights will still get

**[06:21]** sample, but their weights will still get

**[06:21]** sample, but their weights will still get updated if if a training step just

**[06:23]** updated if if a training step just

**[06:24]** updated if if a training step just completed.

**[06:29]** As a result, we end up with samples that

**[06:29]** As a result, we end up with samples that had multiple versions of the policy that

**[06:31]** had multiple versions of the policy that

**[06:31]** had multiple versions of the policy that contributed to the sample in order to

**[06:32]** contributed to the sample in order to

**[06:32]** contributed to the sample in order to generate it. In other words, there are

**[06:34]** generate it. In other words, there are

**[06:34]** generate it. In other words, there are stale tokens in some of these in some of

**[06:36]** stale tokens in some of these in some of

**[06:36]** stale tokens in some of these in some of these samples. Let's take a look at one

**[06:39]** these samples. Let's take a look at one

**[06:39]** these samples. Let's take a look at one sample to make this a bit more clear.

**[06:42]** sample to make this a bit more clear.

**[06:42]** sample to make this a bit more clear. As you can see, there's three versions

**[06:43]** As you can see, there's three versions

**[06:43]** As you can see, there's three versions of the policy at time steps t, t+1, and

**[06:46]** of the policy at time steps t, t+1, and

**[06:46]** of the policy at time steps t, t+1, and t plus2 that were used to generate this

**[06:48]** t plus2 that were used to generate this

**[06:48]** t plus2 that were used to generate this sample since there were two completed

**[06:50]** sample since there were two completed

**[06:50]** sample since there were two completed train steps and in turn two in-flight

**[06:52]** train steps and in turn two in-flight

**[06:52]** train steps and in turn two in-flight weight updates while this sample was

**[06:53]** weight updates while this sample was

**[06:54]** weight updates while this sample was being generated.

**[06:56]** being generated.

**[06:56]** being generated. So when this sample gets trained on in

**[06:57]** So when this sample gets trained on in

**[06:58]** So when this sample gets trained on in the T+3 to t+4 training batch, we will


### [07:00 - 08:00]

**[07:00]** the T+3 to t+4 training batch, we will

**[07:00]** the T+3 to t+4 training batch, we will have some tokens that came from policy

**[07:03]** have some tokens that came from policy

**[07:03]** have some tokens that came from policy three steps behind, some that came from

**[07:04]** three steps behind, some that came from

**[07:04]** three steps behind, some that came from policy two steps behind, and those last

**[07:06]** policy two steps behind, and those last

**[07:06]** policy two steps behind, and those last two tokens that came from a policy that

**[07:08]** two tokens that came from a policy that

**[07:08]** two tokens that came from a policy that was one step behind.

**[07:11]** was one step behind.

**[07:11]** was one step behind. Now, let's say that we only tolerate

**[07:13]** Now, let's say that we only tolerate

**[07:13]** Now, let's say that we only tolerate stailness up to two. That means we're

**[07:16]** stailness up to two. That means we're

**[07:16]** stailness up to two. That means we're not going to allow the inflight weight

**[07:17]** not going to allow the inflight weight

**[07:18]** not going to allow the inflight weight update after the T+1 to T+2 training

**[07:20]** update after the T+1 to T+2 training

**[07:20]** update after the T+1 to T+2 training batch completes. And that means the

**[07:22]** batch completes. And that means the

**[07:22]** batch completes. And that means the training workers are just going to be

**[07:23]** training workers are just going to be

**[07:23]** training workers are just going to be idle waiting for this sample to complete

**[07:25]** idle waiting for this sample to complete

**[07:25]** idle waiting for this sample to complete before they can propagate that in-flight

**[07:27]** before they can propagate that in-flight

**[07:27]** before they can propagate that in-flight weight update and start training on the

**[07:29]** weight update and start training on the

**[07:29]** weight update and start training on the next batch. Because if they were to do

**[07:30]** next batch. Because if they were to do

**[07:30]** next batch. Because if they were to do the inflight weight update, that would

**[07:31]** the inflight weight update, that would

**[07:31]** the inflight weight update, that would cause this sample to have stalness 3 as

**[07:33]** cause this sample to have stalness 3 as

**[07:33]** cause this sample to have stalness 3 as we just saw.

**[07:35]** we just saw.

**[07:35]** we just saw. And if we only tolerate stailness one,

**[07:37]** And if we only tolerate stailness one,

**[07:37]** And if we only tolerate stailness one, the training workers are going to be

**[07:39]** the training workers are going to be

**[07:39]** the training workers are going to be idle for even longer,

**[07:42]** idle for even longer,

**[07:42]** idle for even longer, which is bad. So as you increase how

**[07:44]** which is bad. So as you increase how

**[07:44]** which is bad. So as you increase how much stale you tolerate, you have less

**[07:46]** much stale you tolerate, you have less

**[07:46]** much stale you tolerate, you have less idle GPUs in general. But as we all

**[07:48]** idle GPUs in general. But as we all

**[07:48]** idle GPUs in general. But as we all know, there's no free lunch. Um this is

**[07:50]** know, there's no free lunch. Um this is

**[07:50]** know, there's no free lunch. Um this is the standard policy gradient with an

**[07:52]** the standard policy gradient with an

**[07:52]** the standard policy gradient with an importance ratio to adjust for the fact

**[07:54]** importance ratio to adjust for the fact

**[07:54]** importance ratio to adjust for the fact that we're sampling from a policy at

**[07:56]** that we're sampling from a policy at

**[07:56]** that we're sampling from a policy at time step t and training with the policy

**[07:59]** time step t and training with the policy

**[07:59]** time step t and training with the policy at time step t t plus k given that


### [08:00 - 09:00]

**[08:00]** at time step t t plus k given that

**[08:00]** at time step t t plus k given that there's case staleness. The importance

**[08:03]** there's case staleness. The importance

**[08:03]** there's case staleness. The importance ratio is what makes this policy gradient

**[08:05]** ratio is what makes this policy gradient

**[08:05]** ratio is what makes this policy gradient unbiased. But the variance of that ratio

**[08:08]** unbiased. But the variance of that ratio

**[08:08]** unbiased. But the variance of that ratio increases as you increase stalness. And

**[08:10]** increases as you increase stalness. And

**[08:10]** increases as you increase stalness. And so this is kind of the big issue here

**[08:12]** so this is kind of the big issue here

**[08:12]** so this is kind of the big issue here because now with with higher variance

**[08:14]** because now with with higher variance

**[08:14]** because now with with higher variance importance ratio learning can become

**[08:16]** importance ratio learning can become

**[08:16]** importance ratio learning can become unstable and cause divergence.

**[08:19]** unstable and cause divergence.

**[08:19]** unstable and cause divergence. The concrete trade-off is we want a lot

**[08:20]** The concrete trade-off is we want a lot

**[08:20]** The concrete trade-off is we want a lot of stailness for fast RL runs, but a lot

**[08:23]** of stailness for fast RL runs, but a lot

**[08:23]** of stailness for fast RL runs, but a lot of staleness makes learning unstable,

**[08:25]** of staleness makes learning unstable,

**[08:25]** of staleness makes learning unstable, which then requires innovating on the

**[08:27]** which then requires innovating on the

**[08:27]** which then requires innovating on the algorithm and the science. And this is

**[08:29]** algorithm and the science. And this is

**[08:29]** algorithm and the science. And this is one of the primary research problems

**[08:30]** one of the primary research problems

**[08:30]** one of the primary research problems that we focus on here at Applied

**[08:32]** that we focus on here at Applied

**[08:32]** that we focus on here at Applied Compute. And as I was talking about

**[08:33]** Compute. And as I was talking about

**[08:33]** Compute. And as I was talking about earlier, it directly flows back into our

**[08:35]** earlier, it directly flows back into our

**[08:35]** earlier, it directly flows back into our core business.

**[08:38]** core business.

**[08:38]** core business. For the purpose of this talk, we're

**[08:39]** For the purpose of this talk, we're

**[08:39]** For the purpose of this talk, we're going to focus on a simpler sub problem.

**[08:41]** going to focus on a simpler sub problem.

**[08:41]** going to focus on a simpler sub problem. Let's assume that we have good science

**[08:43]** Let's assume that we have good science

**[08:43]** Let's assume that we have good science and algorithmic innovations that allow

**[08:45]** and algorithmic innovations that allow

**[08:45]** and algorithmic innovations that allow us to tolerate staleness up to some

**[08:47]** us to tolerate staleness up to some

**[08:47]** us to tolerate staleness up to some fixed threshold and we have some fixed

**[08:49]** fixed threshold and we have some fixed

**[08:49]** fixed threshold and we have some fixed compute budget as usually exists in the

**[08:51]** compute budget as usually exists in the

**[08:51]** compute budget as usually exists in the world. What is the highest way for us to

**[08:54]** world. What is the highest way for us to

**[08:54]** world. What is the highest way for us to do RL in this setting?

**[08:57]** do RL in this setting?

**[08:57]** do RL in this setting? Cool. Thanks Rhythm.


### [09:00 - 10:00]

**[09:00]** Cool. Thanks Rhythm.

**[09:00]** Cool. Thanks Rhythm. So we posed this as a modeling problem

**[09:02]** So we posed this as a modeling problem

**[09:02]** So we posed this as a modeling problem of our endto-end system which you know

**[09:03]** of our endto-end system which you know

**[09:04]** of our endto-end system which you know admittedly is a little bit complicated

**[09:05]** admittedly is a little bit complicated

**[09:05]** admittedly is a little bit complicated at first but we did find that we can get

**[09:07]** at first but we did find that we can get

**[09:07]** at first but we did find that we can get surprisingly far with some first

**[09:09]** surprisingly far with some first

**[09:09]** surprisingly far with some first principle systems modeling and as with

**[09:11]** principle systems modeling and as with

**[09:11]** principle systems modeling and as with any modeling problem let's figure out

**[09:13]** any modeling problem let's figure out

**[09:13]** any modeling problem let's figure out the cast of characters that describe the

**[09:15]** the cast of characters that describe the

**[09:15]** the cast of characters that describe the system and then we'll think about how

**[09:17]** system and then we'll think about how

**[09:17]** system and then we'll think about how they all fit together to model it. So

**[09:19]** they all fit together to model it. So

**[09:19]** they all fit together to model it. So the first cast member is some proxy of

**[09:21]** the first cast member is some proxy of

**[09:21]** the first cast member is some proxy of compute budget in which in this case we

**[09:23]** compute budget in which in this case we

**[09:23]** compute budget in which in this case we have as the number of GPUs. In the

**[09:25]** have as the number of GPUs. In the

**[09:25]** have as the number of GPUs. In the synchronous setting like rhythm just

**[09:27]** synchronous setting like rhythm just

**[09:27]** synchronous setting like rhythm just explained all the GPUs will either be

**[09:29]** explained all the GPUs will either be

**[09:29]** explained all the GPUs will either be used for training or sampling since they

**[09:31]** used for training or sampling since they

**[09:31]** used for training or sampling since they happen one after the other. But in the

**[09:33]** happen one after the other. But in the

**[09:33]** happen one after the other. But in the asynchronous setting it's a little bit

**[09:35]** asynchronous setting it's a little bit

**[09:35]** asynchronous setting it's a little bit trickier cuz we can choose to allocate

**[09:37]** trickier cuz we can choose to allocate

**[09:37]** trickier cuz we can choose to allocate that pool of GPU GPU compute as much as

**[09:40]** that pool of GPU GPU compute as much as

**[09:40]** that pool of GPU GPU compute as much as we want for training or as much as we

**[09:41]** we want for training or as much as we

**[09:41]** we want for training or as much as we want from sampling and that leads to

**[09:43]** want from sampling and that leads to

**[09:43]** want from sampling and that leads to some design decisions.

**[09:45]** some design decisions.

**[09:45]** some design decisions. The next is the training batch size

**[09:47]** The next is the training batch size

**[09:47]** The next is the training batch size which is some proxy of the workload that

**[09:49]** which is some proxy of the workload that

**[09:49]** which is some proxy of the workload that we have uh on the on the overall system

**[09:52]** we have uh on the on the overall system

**[09:52]** we have uh on the on the overall system and this is kind of an ML decision but

**[09:54]** and this is kind of an ML decision but

**[09:54]** and this is kind of an ML decision but in short what we have is a batch of

**[09:56]** in short what we have is a batch of

**[09:56]** in short what we have is a batch of problems which is a subset of our data

**[09:58]** problems which is a subset of our data

**[09:58]** problems which is a subset of our data set. Let's say we have n math problems

**[09:59]** set. Let's say we have n math problems


### [10:00 - 11:00]

**[10:00]** set. Let's say we have n math problems that we want to train on and for each of

**[10:02]** that we want to train on and for each of

**[10:02]** that we want to train on and for each of these problems we're going to sample n

**[10:04]** these problems we're going to sample n

**[10:04]** these problems we're going to sample n problems in parallel. So if the problems

**[10:06]** problems in parallel. So if the problems

**[10:06]** problems in parallel. So if the problems are really difficult, we might sample

**[10:08]** are really difficult, we might sample

**[10:08]** are really difficult, we might sample more to encourage some diversity in the

**[10:10]** more to encourage some diversity in the

**[10:10]** more to encourage some diversity in the samples to encourage the model to learn

**[10:11]** samples to encourage the model to learn

**[10:12]** samples to encourage the model to learn some potentially uh divergent

**[10:13]** some potentially uh divergent

**[10:13]** some potentially uh divergent strategies.

**[10:15]** strategies.

**[10:16]** strategies. The next thing we need is some proxy of

**[10:17]** The next thing we need is some proxy of

**[10:18]** The next thing we need is some proxy of sampling throughput. And to get some

**[10:19]** sampling throughput. And to get some

**[10:19]** sampling throughput. And to get some intuition of what we should choose here

**[10:21]** intuition of what we should choose here

**[10:21]** intuition of what we should choose here as a modeling decision, let's look at

**[10:23]** as a modeling decision, let's look at

**[10:23]** as a modeling decision, let's look at how some modern inference engine surface

**[10:25]** how some modern inference engine surface

**[10:25]** how some modern inference engine surface requests. So in GPU memory, we have the

**[10:27]** requests. So in GPU memory, we have the

**[10:27]** requests. So in GPU memory, we have the model weights, the activations, and some

**[10:29]** model weights, the activations, and some

**[10:29]** model weights, the activations, and some runtime state called the KV cache in

**[10:31]** runtime state called the KV cache in

**[10:31]** runtime state called the KV cache in memory. And given this train model,

**[10:33]** memory. And given this train model,

**[10:33]** memory. And given this train model, we're going to run the forward pass

**[10:35]** we're going to run the forward pass

**[10:35]** we're going to run the forward pass several times where each forward pass

**[10:37]** several times where each forward pass

**[10:37]** several times where each forward pass samples the next token and then we'll

**[10:39]** samples the next token and then we'll

**[10:39]** samples the next token and then we'll write to the KV cache. And so what this

**[10:43]** write to the KV cache. And so what this

**[10:43]** write to the KV cache. And so what this model shows is that a principal estimate

**[10:45]** model shows is that a principal estimate

**[10:45]** model shows is that a principal estimate that we should do is we should find some

**[10:47]** that we should do is we should find some

**[10:47]** that we should do is we should find some way to measure the latency per GPU of

**[10:50]** way to measure the latency per GPU of

**[10:50]** way to measure the latency per GPU of the forward pass. And this ends up being

**[10:52]** the forward pass. And this ends up being

**[10:52]** the forward pass. And this ends up being a pretty good choice in practice because

**[10:54]** a pretty good choice in practice because

**[10:54]** a pretty good choice in practice because from the systems angle, the inference

**[10:56]** from the systems angle, the inference

**[10:56]** from the systems angle, the inference throughput that we choose is largely

**[10:58]** throughput that we choose is largely

**[10:58]** throughput that we choose is largely determined by the batch size that we


### [11:00 - 12:00]

**[11:00]** determined by the batch size that we

**[11:00]** determined by the batch size that we perform sampling with. So what I've

**[11:02]** perform sampling with. So what I've

**[11:02]** perform sampling with. So what I've shown here in the red square is a batch

**[11:04]** shown here in the red square is a batch

**[11:04]** shown here in the red square is a batch of tokens that are all forwarded at the

**[11:06]** of tokens that are all forwarded at the

**[11:06]** of tokens that are all forwarded at the same time. And this sampling forward

**[11:08]** same time. And this sampling forward

**[11:08]** same time. And this sampling forward pass needs to be as large as possible to

**[11:10]** pass needs to be as large as possible to

**[11:10]** pass needs to be as large as possible to efficiently utilize the GPUs subject to

**[11:13]** efficiently utilize the GPUs subject to

**[11:13]** efficiently utilize the GPUs subject to the runtime constraint that we don't

**[11:15]** the runtime constraint that we don't

**[11:15]** the runtime constraint that we don't actually run out of memory uh in the KV

**[11:17]** actually run out of memory uh in the KV

**[11:17]** actually run out of memory uh in the KV cache.

**[11:19]** cache.

**[11:19]** cache. So what we can then do is we can fit a

**[11:21]** So what we can then do is we can fit a

**[11:21]** So what we can then do is we can fit a latency curve as a function of batch

**[11:23]** latency curve as a function of batch

**[11:23]** latency curve as a function of batch size and that latency curve will look

**[11:25]** size and that latency curve will look

**[11:25]** size and that latency curve will look something like this. You'll have some

**[11:27]** something like this. You'll have some

**[11:27]** something like this. You'll have some regime where it's memory bound and when

**[11:28]** regime where it's memory bound and when

**[11:28]** regime where it's memory bound and when it increases it becomes computebound and

**[11:30]** it increases it becomes computebound and

**[11:30]** it increases it becomes computebound and there's some functional form below. And

**[11:33]** there's some functional form below. And

**[11:33]** there's some functional form below. And to explain the details of why we chose

**[11:34]** to explain the details of why we chose

**[11:34]** to explain the details of why we chose this decision, what we have here is an

**[11:36]** this decision, what we have here is an

**[11:36]** this decision, what we have here is an equation that's based in the roof line

**[11:38]** equation that's based in the roof line

**[11:38]** equation that's based in the roof line model from systems. At lower batch

**[11:40]** model from systems. At lower batch

**[11:40]** model from systems. At lower batch sizes, which I've highlighted in yellow

**[11:42]** sizes, which I've highlighted in yellow

**[11:42]** sizes, which I've highlighted in yellow here, we don't have that much work to do

**[11:45]** here, we don't have that much work to do

**[11:45]** here, we don't have that much work to do because there isn't that much compute to

**[11:46]** because there isn't that much compute to

**[11:46]** because there isn't that much compute to do on the processor and there's so many

**[11:48]** do on the processor and there's so many

**[11:48]** do on the processor and there's so many parameters you need to load in at the

**[11:50]** parameters you need to load in at the

**[11:50]** parameters you need to load in at the same time. And so, as a result, when you

**[11:52]** same time. And so, as a result, when you

**[11:52]** same time. And so, as a result, when you add incremental work, it doesn't really

**[11:55]** add incremental work, it doesn't really

**[11:55]** add incremental work, it doesn't really add that much latency to the overall

**[11:56]** add that much latency to the overall

**[11:56]** add that much latency to the overall system since the processor is so fast at

**[11:59]** system since the processor is so fast at

**[11:59]** system since the processor is so fast at doing math that we're just waiting on


### [12:00 - 13:00]

**[12:01]** doing math that we're just waiting on

**[12:01]** doing math that we're just waiting on memory to stream parameters in from the

**[12:03]** memory to stream parameters in from the

**[12:03]** memory to stream parameters in from the pro from memory to the processor. But as

**[12:06]** pro from memory to the processor. But as

**[12:06]** pro from memory to the processor. But as the batch sizes begin to get larger, we

**[12:08]** the batch sizes begin to get larger, we

**[12:08]** the batch sizes begin to get larger, we then get bottlenecked by the processor.

**[12:10]** then get bottlenecked by the processor.

**[12:10]** then get bottlenecked by the processor. And the more we add to our batch, the

**[12:12]** And the more we add to our batch, the

**[12:12]** And the more we add to our batch, the slower the forward pass takes. And just

**[12:14]** slower the forward pass takes. And just

**[12:14]** slower the forward pass takes. And just for good measure, we have this sigmoid

**[12:16]** for good measure, we have this sigmoid

**[12:16]** for good measure, we have this sigmoid here that just sort of modulates the

**[12:17]** here that just sort of modulates the

**[12:17]** here that just sort of modulates the smooth transition at this hinge point

**[12:19]** smooth transition at this hinge point

**[12:19]** smooth transition at this hinge point here to show that there's a subtle

**[12:21]** here to show that there's a subtle

**[12:21]** here to show that there's a subtle transition from a memory bound

**[12:22]** transition from a memory bound

**[12:22]** transition from a memory bound computation to one that's more

**[12:24]** computation to one that's more

**[12:24]** computation to one that's more computebound and bottlenecked by the

**[12:26]** computebound and bottlenecked by the

**[12:26]** computebound and bottlenecked by the processor.

**[12:28]** processor.

**[12:28]** processor. The final cast member is some proxy of

**[12:30]** The final cast member is some proxy of

**[12:30]** The final cast member is some proxy of training throughput and we chose to

**[12:32]** training throughput and we chose to

**[12:32]** training throughput and we chose to measure this on a per GPU basis. So in

**[12:35]** measure this on a per GPU basis. So in

**[12:35]** measure this on a per GPU basis. So in this case the model takes in the

**[12:37]** this case the model takes in the

**[12:37]** this case the model takes in the training batch size. So the parameter we

**[12:38]** training batch size. So the parameter we

**[12:38]** training batch size. So the parameter we saw earlier and we typically do this by

**[12:41]** saw earlier and we typically do this by

**[12:41]** saw earlier and we typically do this by fitting a proxy of our empirical

**[12:43]** fitting a proxy of our empirical

**[12:43]** fitting a proxy of our empirical workloads. The units here is how many

**[12:45]** workloads. The units here is how many

**[12:45]** workloads. The units here is how many each train how many tokens per second

**[12:47]** each train how many tokens per second

**[12:47]** each train how many tokens per second each training GPU processes. So it needs

**[12:49]** each training GPU processes. So it needs

**[12:49]** each training GPU processes. So it needs to do the forward the backward and some

**[12:51]** to do the forward the backward and some

**[12:51]** to do the forward the backward and some optimizer steps.

**[12:53]** optimizer steps.

**[12:53]** optimizer steps. So given these forecast members we can

**[12:55]** So given these forecast members we can

**[12:55]** So given these forecast members we can then begin modeling the system. And the

**[12:57]** then begin modeling the system. And the

**[12:57]** then begin modeling the system. And the first idea we had although Rhythm you

**[12:59]** first idea we had although Rhythm you

**[12:59]** first idea we had although Rhythm you know suggested that this might not be a


### [13:00 - 14:00]

**[13:01]** know suggested that this might not be a

**[13:01]** know suggested that this might not be a great idea we can think about how to use

**[13:03]** great idea we can think about how to use

**[13:03]** great idea we can think about how to use a synchronous setup. And this might be a

**[13:05]** a synchronous setup. And this might be a

**[13:05]** a synchronous setup. And this might be a good idea from first principles because

**[13:06]** good idea from first principles because

**[13:06]** good idea from first principles because we definitely meet the staleness

**[13:08]** we definitely meet the staleness

**[13:08]** we definitely meet the staleness constraint because we don't train on

**[13:09]** constraint because we don't train on

**[13:09]** constraint because we don't train on stale data and we always use the entire

**[13:12]** stale data and we always use the entire

**[13:12]** stale data and we always use the entire GPU fleet for either training or

**[13:14]** GPU fleet for either training or

**[13:14]** GPU fleet for either training or sampling making sure that we're using

**[13:16]** sampling making sure that we're using

**[13:16]** sampling making sure that we're using efficient use of the hardware. Let's

**[13:18]** efficient use of the hardware. Let's

**[13:18]** efficient use of the hardware. Let's think about how to actually model this.

**[13:20]** think about how to actually model this.

**[13:20]** think about how to actually model this. There are two things we need to know. We

**[13:21]** There are two things we need to know. We

**[13:21]** There are two things we need to know. We need to know the batch size at which

**[13:23]** need to know the batch size at which

**[13:23]** need to know the batch size at which generation runs. And we also need to

**[13:25]** generation runs. And we also need to

**[13:25]** generation runs. And we also need to know the response length distribution to

**[13:27]** know the response length distribution to

**[13:27]** know the response length distribution to figure out how our training workload's

**[13:29]** figure out how our training workload's

**[13:29]** figure out how our training workload's going to work and also how long the

**[13:30]** going to work and also how long the

**[13:30]** going to work and also how long the sampling's going to take. And so what

**[13:33]** sampling's going to take. And so what

**[13:33]** sampling's going to take. And so what I'm showing here in this simulation is a

**[13:35]** I'm showing here in this simulation is a

**[13:35]** I'm showing here in this simulation is a couple of engines. Each square is a

**[13:37]** couple of engines. Each square is a

**[13:37]** couple of engines. Each square is a request being processed and they get

**[13:38]** request being processed and they get

**[13:38]** request being processed and they get darker and darker as we make progress

**[13:40]** darker and darker as we make progress

**[13:40]** darker and darker as we make progress throughout the batch. And as they finish

**[13:42]** throughout the batch. And as they finish

**[13:42]** throughout the batch. And as they finish samples, they write to the queue. And on

**[13:45]** samples, they write to the queue. And on

**[13:45]** samples, they write to the queue. And on the right hand side is a time series

**[13:46]** the right hand side is a time series

**[13:46]** the right hand side is a time series metric, maybe something that you'd see

**[13:47]** metric, maybe something that you'd see

**[13:47]** metric, maybe something that you'd see in Graphana if you're monitoring

**[13:49]** in Graphana if you're monitoring

**[13:49]** in Graphana if you're monitoring production metrics. And what you can see

**[13:50]** production metrics. And what you can see

**[13:50]** production metrics. And what you can see is that the batch size begins very high,

**[13:52]** is that the batch size begins very high,

**[13:52]** is that the batch size begins very high, but it slowly goes down over time as it

**[13:55]** but it slowly goes down over time as it

**[13:55]** but it slowly goes down over time as it eventually goes to zero and all the

**[13:56]** eventually goes to zero and all the

**[13:56]** eventually goes to zero and all the samples complete. And we can finally run

**[13:59]** samples complete. And we can finally run

**[13:59]** samples complete. And we can finally run an optimization step. After the step


### [14:00 - 15:00]

**[14:01]** an optimization step. After the step

**[14:01]** an optimization step. After the step completes, we run this in a loop and we

**[14:02]** completes, we run this in a loop and we

**[14:02]** completes, we run this in a loop and we move on to the next step. And so as a

**[14:05]** move on to the next step. And so as a

**[14:05]** move on to the next step. And so as a result, we can have the following

**[14:06]** result, we can have the following

**[14:06]** result, we can have the following sampling procedure. We do maximum tokens

**[14:09]** sampling procedure. We do maximum tokens

**[14:09]** sampling procedure. We do maximum tokens inference forward passes where maximum

**[14:11]** inference forward passes where maximum

**[14:12]** inference forward passes where maximum tokens is the total number of forward

**[14:13]** tokens is the total number of forward

**[14:14]** tokens is the total number of forward passes we do for the longest request. We

**[14:16]** passes we do for the longest request. We

**[14:16]** passes we do for the longest request. We use the fitted latency estimator to

**[14:18]** use the fitted latency estimator to

**[14:18]** use the fitted latency estimator to figure out how long that forward pass

**[14:20]** figure out how long that forward pass

**[14:20]** figure out how long that forward pass will take. And then the response length

**[14:22]** will take. And then the response length

**[14:22]** will take. And then the response length distribution will tell us how many

**[14:23]** distribution will tell us how many

**[14:23]** distribution will tell us how many responses to drop. And so what we're

**[14:25]** responses to drop. And so what we're

**[14:25]** responses to drop. And so what we're showing in this video here is this

**[14:27]** showing in this video here is this

**[14:27]** showing in this video here is this entire thing of the response length

**[14:28]** entire thing of the response length

**[14:28]** entire thing of the response length distribution that we feed into the

**[14:30]** distribution that we feed into the

**[14:30]** distribution that we feed into the latency estimator. At training time, we

**[14:32]** latency estimator. At training time, we

**[14:32]** latency estimator. At training time, we can compute the total number of tokens

**[14:34]** can compute the total number of tokens

**[14:34]** can compute the total number of tokens that we just sampled in the batch and

**[14:35]** that we just sampled in the batch and

**[14:36]** that we just sampled in the batch and divide by the total uh training

**[14:37]** divide by the total uh training

**[14:37]** divide by the total uh training throughput uh which is just the number

**[14:39]** throughput uh which is just the number

**[14:39]** throughput uh which is just the number of GPUs multiplied by the per GPU

**[14:41]** of GPUs multiplied by the per GPU

**[14:41]** of GPUs multiplied by the per GPU training throughput. And so what we have

**[14:43]** training throughput. And so what we have

**[14:43]** training throughput. And so what we have here is a simulation of what this

**[14:45]** here is a simulation of what this

**[14:45]** here is a simulation of what this latency curve looks like. So we have the

**[14:47]** latency curve looks like. So we have the

**[14:47]** latency curve looks like. So we have the CDF of the response length distribution

**[14:49]** CDF of the response length distribution

**[14:49]** CDF of the response length distribution that tells us how many responses we

**[14:50]** that tells us how many responses we

**[14:50]** that tells us how many responses we should drop on the left and the latency

**[14:52]** should drop on the left and the latency

**[14:52]** should drop on the left and the latency curve on the right. And this roughly

**[14:54]** curve on the right. And this roughly

**[14:54]** curve on the right. And this roughly kind of tracks because as we add more

**[14:55]** kind of tracks because as we add more

**[14:55]** kind of tracks because as we add more GPUs, we'd expect the latency per step

**[14:57]** GPUs, we'd expect the latency per step

**[14:57]** GPUs, we'd expect the latency per step to go down.


### [15:00 - 16:00]

**[15:00]** to go down.

**[15:00]** to go down. The next idea, given that the

**[15:01]** The next idea, given that the

**[15:01]** The next idea, given that the synchronous setup might not be the most

**[15:03]** synchronous setup might not be the most

**[15:03]** synchronous setup might not be the most principled choice, as Rhythm showed, is

**[15:05]** principled choice, as Rhythm showed, is

**[15:05]** principled choice, as Rhythm showed, is an asynchronous setup. But it's not just

**[15:07]** an asynchronous setup. But it's not just

**[15:07]** an asynchronous setup. But it's not just as easy as just sort of provisioning the

**[15:09]** as easy as just sort of provisioning the

**[15:09]** as easy as just sort of provisioning the compute between training and inference

**[15:11]** compute between training and inference

**[15:11]** compute between training and inference because if we don't do this carefully,

**[15:13]** because if we don't do this carefully,

**[15:13]** because if we don't do this carefully, we might actually run into the idle GPU

**[15:15]** we might actually run into the idle GPU

**[15:15]** we might actually run into the idle GPU problem again. And to show this, let's

**[15:17]** problem again. And to show this, let's

**[15:17]** problem again. And to show this, let's illustrate two extremes of what this

**[15:18]** illustrate two extremes of what this

**[15:18]** illustrate two extremes of what this allocation problem looks like. Let's f

**[15:21]** allocation problem looks like. Let's f

**[15:21]** allocation problem looks like. Let's f let's let's first look at one end of the

**[15:22]** let's let's first look at one end of the

**[15:22]** let's let's first look at one end of the spectrum where we provision way too many

**[15:24]** spectrum where we provision way too many

**[15:24]** spectrum where we provision way too many inference GPUs and not that many

**[15:26]** inference GPUs and not that many

**[15:26]** inference GPUs and not that many samplers. In this case, we're consuming

**[15:29]** samplers. In this case, we're consuming

**[15:29]** samplers. In this case, we're consuming from a queue much faster than we're

**[15:31]** from a queue much faster than we're

**[15:31]** from a queue much faster than we're actually producing from it because the

**[15:33]** actually producing from it because the

**[15:33]** actually producing from it because the sampling workers are producing work

**[15:35]** sampling workers are producing work

**[15:35]** sampling workers are producing work significantly faster than significantly

**[15:37]** significantly faster than significantly

**[15:37]** significantly faster than significantly slower than we can actually consume

**[15:39]** slower than we can actually consume

**[15:39]** slower than we can actually consume them. When the red square grays out, it

**[15:41]** them. When the red square grays out, it

**[15:41]** them. When the red square grays out, it shows that they're idle. And what this

**[15:42]** shows that they're idle. And what this

**[15:42]** shows that they're idle. And what this diagram should hopefully illustrate is

**[15:44]** diagram should hopefully illustrate is

**[15:44]** diagram should hopefully illustrate is that for a lot of the time we're

**[15:45]** that for a lot of the time we're

**[15:46]** that for a lot of the time we're actually not using that and that has the

**[15:47]** actually not using that and that has the

**[15:47]** actually not using that and that has the same problem of low GPU utilization in

**[15:50]** same problem of low GPU utilization in

**[15:50]** same problem of low GPU utilization in the synchronous case as shown earlier.

**[15:53]** the synchronous case as shown earlier.

**[15:53]** the synchronous case as shown earlier. On the other end of the extreme we can

**[15:55]** On the other end of the extreme we can

**[15:55]** On the other end of the extreme we can provision way too many sampling GPUs in

**[15:58]** provision way too many sampling GPUs in

**[15:58]** provision way too many sampling GPUs in which case our production rate is way


### [16:00 - 17:00]

**[16:00]** which case our production rate is way

**[16:00]** which case our production rate is way faster than the rate that we actually

**[16:02]** faster than the rate that we actually

**[16:02]** faster than the rate that we actually consume them in. So here we've doubled

**[16:04]** consume them in. So here we've doubled

**[16:04]** consume them in. So here we've doubled the number of overall sampling GPUs and

**[16:06]** the number of overall sampling GPUs and

**[16:06]** the number of overall sampling GPUs and have the number of training GPUs. As you

**[16:08]** have the number of training GPUs. As you

**[16:08]** have the number of training GPUs. As you can see, they produce samples at much

**[16:10]** can see, they produce samples at much

**[16:10]** can see, they produce samples at much more rapid of a rate. But this index

**[16:12]** more rapid of a rate. But this index

**[16:12]** more rapid of a rate. But this index here in each yellow square, which is the

**[16:14]** here in each yellow square, which is the

**[16:14]** here in each yellow square, which is the staleness count of each sample, goes up.

**[16:17]** staleness count of each sample, goes up.

**[16:17]** staleness count of each sample, goes up. And as time moves on, we get more and

**[16:19]** And as time moves on, we get more and

**[16:19]** And as time moves on, we get more and more stale. And so the samples get more

**[16:21]** more stale. And so the samples get more

**[16:21]** more stale. And so the samples get more and more kind of less more and more

**[16:23]** and more kind of less more and more

**[16:23]** and more kind of less more and more transparent as a result. And we learn

**[16:25]** transparent as a result. And we learn

**[16:25]** transparent as a result. And we learn less from each individual sample. So

**[16:28]** less from each individual sample. So

**[16:28]** less from each individual sample. So let's think about how we can actually

**[16:29]** let's think about how we can actually

**[16:29]** let's think about how we can actually model this workload then to to determine

**[16:31]** model this workload then to to determine

**[16:31]** model this workload then to to determine an optimal async workload. In this case,

**[16:34]** an optimal async workload. In this case,

**[16:34]** an optimal async workload. In this case, the picture looks a little bit different

**[16:35]** the picture looks a little bit different

**[16:36]** the picture looks a little bit different because in steady state, the batch size

**[16:37]** because in steady state, the batch size

**[16:37]** because in steady state, the batch size is relatively consistent compared to the

**[16:39]** is relatively consistent compared to the

**[16:39]** is relatively consistent compared to the synchronous setup where it kind of goes

**[16:41]** synchronous setup where it kind of goes

**[16:41]** synchronous setup where it kind of goes down over time. So on the right hand

**[16:43]** down over time. So on the right hand

**[16:43]** down over time. So on the right hand side here, we have the same time series

**[16:44]** side here, we have the same time series

**[16:44]** side here, we have the same time series metrics. But in this case, it's a little

**[16:46]** metrics. But in this case, it's a little

**[16:46]** metrics. But in this case, it's a little bit different because the yellow squares

**[16:48]** bit different because the yellow squares

**[16:48]** bit different because the yellow squares are always full because every time we

**[16:50]** are always full because every time we

**[16:50]** are always full because every time we complete a sample, a new sample goes in

**[16:52]** complete a sample, a new sample goes in

**[16:52]** complete a sample, a new sample goes in and we can continue writing to the

**[16:54]** and we can continue writing to the

**[16:54]** and we can continue writing to the queue. And so that batch size with a

**[16:56]** queue. And so that batch size with a

**[16:56]** queue. And so that batch size with a little bit of wiggles just for good

**[16:57]** little bit of wiggles just for good

**[16:57]** little bit of wiggles just for good measure is like a is pretty consistent

**[16:59]** measure is like a is pretty consistent

**[16:59]** measure is like a is pretty consistent over the course of a run. Now obviously


### [17:00 - 18:00]

**[17:02]** over the course of a run. Now obviously

**[17:02]** over the course of a run. Now obviously the caveat here is that this batch size

**[17:04]** the caveat here is that this batch size

**[17:04]** the caveat here is that this batch size will certainly go down as we you know as

**[17:05]** will certainly go down as we you know as

**[17:06]** will certainly go down as we you know as response lengths go up because we run

**[17:07]** response lengths go up because we run

**[17:07]** response lengths go up because we run out of cache uh KV cache but that's kind

**[17:09]** out of cache uh KV cache but that's kind

**[17:09]** out of cache uh KV cache but that's kind of a separate story and actually our

**[17:11]** of a separate story and actually our

**[17:11]** of a separate story and actually our model accommodates for that because

**[17:12]** model accommodates for that because

**[17:12]** model accommodates for that because we're actually accommodating for a

**[17:13]** we're actually accommodating for a

**[17:13]** we're actually accommodating for a response length distribution.

**[17:17]** response length distribution.

**[17:17]** response length distribution. We can then begin to figure out the

**[17:18]** We can then begin to figure out the

**[17:18]** We can then begin to figure out the optimal layout and there's two kind of

**[17:20]** optimal layout and there's two kind of

**[17:20]** optimal layout and there's two kind of constraints that we have to satisfy now

**[17:22]** constraints that we have to satisfy now

**[17:22]** constraints that we have to satisfy now that we know that the generation batch

**[17:23]** that we know that the generation batch

**[17:23]** that we know that the generation batch size is roughly consistent throughout

**[17:25]** size is roughly consistent throughout

**[17:25]** size is roughly consistent throughout the course of a run. The first invariant

**[17:27]** the course of a run. The first invariant

**[17:27]** the course of a run. The first invariant that we need to have is that the

**[17:28]** that we need to have is that the

**[17:28]** that we need to have is that the production consumption rate are roughly

**[17:30]** production consumption rate are roughly

**[17:30]** production consumption rate are roughly equal. So on the left hand side of this

**[17:32]** equal. So on the left hand side of this

**[17:32]** equal. So on the left hand side of this equality we have the training throughput

**[17:33]** equality we have the training throughput

**[17:34]** equality we have the training throughput which is the number of training GPUs

**[17:35]** which is the number of training GPUs

**[17:35]** which is the number of training GPUs multiplied by the per GPU uh throughput

**[17:38]** multiplied by the per GPU uh throughput

**[17:38]** multiplied by the per GPU uh throughput and then also we have the number of

**[17:39]** and then also we have the number of

**[17:39]** and then also we have the number of sampling GPUs multiplied by the sampling

**[17:41]** sampling GPUs multiplied by the sampling

**[17:42]** sampling GPUs multiplied by the sampling throughput which is just the batch size

**[17:43]** throughput which is just the batch size

**[17:43]** throughput which is just the batch size multiplied by the latency to actually do

**[17:45]** multiplied by the latency to actually do

**[17:45]** multiplied by the latency to actually do a forward pass on that batch size. And

**[17:48]** a forward pass on that batch size. And

**[17:48]** a forward pass on that batch size. And the next thing is that given that rhythm

**[17:50]** the next thing is that given that rhythm

**[17:50]** the next thing is that given that rhythm you indicated that if we have too much

**[17:52]** you indicated that if we have too much

**[17:52]** you indicated that if we have too much stailness that can be bad from an ML ML

**[17:54]** stailness that can be bad from an ML ML

**[17:54]** stailness that can be bad from an ML ML perspective, we want to make sure that

**[17:56]** perspective, we want to make sure that

**[17:56]** perspective, we want to make sure that our max theoretical stailness or

**[17:58]** our max theoretical stailness or

**[17:58]** our max theoretical stailness or simulated steness doesn't exceed what


### [18:00 - 19:00]

**[18:00]** simulated steness doesn't exceed what

**[18:00]** simulated steness doesn't exceed what our ML can handle. And so here we have

**[18:03]** our ML can handle. And so here we have

**[18:03]** our ML can handle. And so here we have the max stillness on the left which is

**[18:05]** the max stillness on the left which is

**[18:05]** the max stillness on the left which is equal to on the top how much time the

**[18:08]** equal to on the top how much time the

**[18:08]** equal to on the top how much time the longest request took in the batch which

**[18:10]** longest request took in the batch which

**[18:10]** longest request took in the batch which is just the maximum number of tokens

**[18:12]** is just the maximum number of tokens

**[18:12]** is just the maximum number of tokens multiplied by the number of uh by the

**[18:13]** multiplied by the number of uh by the

**[18:14]** multiplied by the number of uh by the amount of time each token forward pass

**[18:15]** amount of time each token forward pass

**[18:15]** amount of time each token forward pass takes. And on the bottom here we have

**[18:17]** takes. And on the bottom here we have

**[18:17]** takes. And on the bottom here we have the length of a training step which is

**[18:19]** the length of a training step which is

**[18:19]** the length of a training step which is the training batch size multiplied by

**[18:21]** the training batch size multiplied by

**[18:21]** the training batch size multiplied by the mean sequence uh by the mean

**[18:23]** the mean sequence uh by the mean

**[18:23]** the mean sequence uh by the mean sequence length.

**[18:25]** sequence length.

**[18:25]** sequence length. So the simulation here then will sweep

**[18:27]** So the simulation here then will sweep

**[18:27]** So the simulation here then will sweep through multiple different values of the

**[18:29]** through multiple different values of the

**[18:29]** through multiple different values of the number of training GPUs. And since we

**[18:31]** number of training GPUs. And since we

**[18:31]** number of training GPUs. And since we have a fixed pool of compute that then

**[18:33]** have a fixed pool of compute that then

**[18:33]** have a fixed pool of compute that then implies a certain number of GPUs used

**[18:35]** implies a certain number of GPUs used

**[18:35]** implies a certain number of GPUs used for sampling. And for this number of

**[18:37]** for sampling. And for this number of

**[18:37]** for sampling. And for this number of sampling GPUs, we can compute the

**[18:39]** sampling GPUs, we can compute the

**[18:39]** sampling GPUs, we can compute the minimum steadystate generation batch

**[18:41]** minimum steadystate generation batch

**[18:41]** minimum steadystate generation batch size to make sure that we don't blow out

**[18:43]** size to make sure that we don't blow out

**[18:43]** size to make sure that we don't blow out of memory uh subject to our KV cache

**[18:45]** of memory uh subject to our KV cache

**[18:45]** of memory uh subject to our KV cache memory constraints and also such that we

**[18:47]** memory constraints and also such that we

**[18:47]** memory constraints and also such that we have maximum throughput on the on the

**[18:49]** have maximum throughput on the on the

**[18:49]** have maximum throughput on the on the sampling side. And the final thing is we

**[18:51]** sampling side. And the final thing is we

**[18:51]** sampling side. And the final thing is we want to prune out all simulations where

**[18:53]** want to prune out all simulations where

**[18:53]** want to prune out all simulations where the sampling throughput brings us over

**[18:55]** the sampling throughput brings us over

**[18:55]** the sampling throughput brings us over the maximum possible stailness. When we

**[18:57]** the maximum possible stailness. When we

**[18:58]** the maximum possible stailness. When we look at that simulation, we can run an

**[18:59]** look at that simulation, we can run an

**[18:59]** look at that simulation, we can run an end to end similarly parameterized by


### [19:00 - 20:00]

**[19:01]** end to end similarly parameterized by

**[19:01]** end to end similarly parameterized by the response length. We see that this

**[19:02]** the response length. We see that this

**[19:02]** the response length. We see that this kind of roughly simulates a 60% speed up

**[19:05]** kind of roughly simulates a 60% speed up

**[19:05]** kind of roughly simulates a 60% speed up relative to our synchronous baseline,

**[19:07]** relative to our synchronous baseline,

**[19:07]** relative to our synchronous baseline, assuming that the GPU compute is

**[19:09]** assuming that the GPU compute is

**[19:09]** assuming that the GPU compute is optimally allocated between training and

**[19:11]** optimally allocated between training and

**[19:11]** optimally allocated between training and sampling.

**[19:12]** sampling.

**[19:12]** sampling. As a result, when we sweep layouts

**[19:14]** As a result, when we sweep layouts

**[19:14]** As a result, when we sweep layouts within these constraints, this allows us

**[19:16]** within these constraints, this allows us

**[19:16]** within these constraints, this allows us to limit staleness, but also make sure

**[19:18]** to limit staleness, but also make sure

**[19:18]** to limit staleness, but also make sure that we have our runs running at maximal

**[19:20]** that we have our runs running at maximal

**[19:20]** that we have our runs running at maximal throughput without actually doing the

**[19:22]** throughput without actually doing the

**[19:22]** throughput without actually doing the run itself. And so this gives us insight

**[19:24]** run itself. And so this gives us insight

**[19:24]** run itself. And so this gives us insight to simulate different workloads before

**[19:26]** to simulate different workloads before

**[19:26]** to simulate different workloads before actually running them on the GPU because

**[19:28]** actually running them on the GPU because

**[19:28]** actually running them on the GPU because these runs can actually be fairly

**[19:29]** these runs can actually be fairly

**[19:29]** these runs can actually be fairly expensive. And so this allows us to ask

**[19:31]** expensive. And so this allows us to ask

**[19:31]** expensive. And so this allows us to ask answer scientific questions from first

**[19:33]** answer scientific questions from first

**[19:33]** answer scientific questions from first principles like what is the optimal

**[19:35]** principles like what is the optimal

**[19:35]** principles like what is the optimal configuration that we we should have of

**[19:37]** configuration that we we should have of

**[19:37]** configuration that we we should have of our GPU compute if we made response

**[19:39]** our GPU compute if we made response

**[19:39]** our GPU compute if we made response lengths very long because often times

**[19:41]** lengths very long because often times

**[19:41]** lengths very long because often times when models learn via reinforcement

**[19:43]** when models learn via reinforcement

**[19:43]** when models learn via reinforcement learning they begin to think for much

**[19:44]** learning they begin to think for much

**[19:44]** learning they begin to think for much longer and also what empirical

**[19:46]** longer and also what empirical

**[19:46]** longer and also what empirical throughputs we should target during our

**[19:48]** throughputs we should target during our

**[19:48]** throughputs we should target during our performance optimization. So this has

**[19:49]** performance optimization. So this has

**[19:50]** performance optimization. So this has been a really useful piece of technology

**[19:51]** been a really useful piece of technology

**[19:51]** been a really useful piece of technology for simulation has informed a lot of the

**[19:53]** for simulation has informed a lot of the

**[19:53]** for simulation has informed a lot of the systems and research design decisions

**[19:55]** systems and research design decisions

**[19:55]** systems and research design decisions that we make. Cool. Thanks for your time

**[19:57]** that we make. Cool. Thanks for your time

**[19:57]** that we make. Cool. Thanks for your time and find us afterwards to jam on some

**[19:59]** and find us afterwards to jam on some

**[19:59]** and find us afterwards to jam on some more RL research engineering together


### [20:00 - 21:00]

**[20:00]** more RL research engineering together

**[20:00]** more RL research engineering together later. Thank you. [music]


