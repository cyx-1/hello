# The Unbearable Lightness of Agent Optimization — Alberto Romero, Jointly

**Video URL:** https://www.youtube.com/watch?v=zfvEMNmVlNY

---

## Full Transcript

### [00:00 - 01:00]

**[00:05]** Right. Hello everyone. Uh today I will

**[00:05]** Right. Hello everyone. Uh today I will present meta adaptive context

**[00:07]** present meta adaptive context

**[00:07]** present meta adaptive context engineering or meta AC for short which

**[00:10]** engineering or meta AC for short which

**[00:10]** engineering or meta AC for short which is a new framework designed to optimize

**[00:12]** is a new framework designed to optimize

**[00:12]** is a new framework designed to optimize AI agents beyond single dimension

**[00:14]** AI agents beyond single dimension

**[00:14]** AI agents beyond single dimension approaches. We will explore how

**[00:17]** approaches. We will explore how

**[00:17]** approaches. We will explore how orchestrating multiple adaptation

**[00:19]** orchestrating multiple adaptation

**[00:19]** orchestrating multiple adaptation strategies can overcome the limitations

**[00:21]** strategies can overcome the limitations

**[00:21]** strategies can overcome the limitations of existing context engineering methods.

**[00:25]** of existing context engineering methods.

**[00:25]** of existing context engineering methods. Now a little introduction about myself.

**[00:27]** Now a little introduction about myself.

**[00:28]** Now a little introduction about myself. Uh so I'm Alberto Romero. I'm the

**[00:30]** Uh so I'm Alberto Romero. I'm the

**[00:30]** Uh so I'm Alberto Romero. I'm the co-founder and CEO at jointly. And for

**[00:32]** co-founder and CEO at jointly. And for

**[00:32]** co-founder and CEO at jointly. And for context at jointly we build the main

**[00:34]** context at jointly we build the main

**[00:34]** context at jointly we build the main specialized agents for regulated

**[00:36]** specialized agents for regulated

**[00:36]** specialized agents for regulated industries where policy adherance

**[00:38]** industries where policy adherance

**[00:38]** industries where policy adherance constraints are particularly strict.

**[00:41]** constraints are particularly strict.

**[00:41]** constraints are particularly strict. Most of our research work is in the area

**[00:44]** Most of our research work is in the area

**[00:44]** Most of our research work is in the area of selfoptimizing agent architectures uh

**[00:47]** of selfoptimizing agent architectures uh

**[00:47]** of selfoptimizing agent architectures uh using systematic approaches.

**[00:49]** using systematic approaches.

**[00:49]** using systematic approaches. Now about myself, I have spent uh 20

**[00:51]** Now about myself, I have spent uh 20

**[00:52]** Now about myself, I have spent uh 20 plus years at the intersection of AI and

**[00:54]** plus years at the intersection of AI and

**[00:54]** plus years at the intersection of AI and data. Uh some of my recent experience

**[00:57]** data. Uh some of my recent experience

**[00:57]** data. Uh some of my recent experience includes being the CTO and co-founder of

**[00:59]** includes being the CTO and co-founder of

**[00:59]** includes being the CTO and co-founder of human AI uh think MLbased risk


### [01:00 - 02:00]

**[01:02]** human AI uh think MLbased risk

**[01:02]** human AI uh think MLbased risk prediction for mobility which was

**[01:04]** prediction for mobility which was

**[01:04]** prediction for mobility which was acquired by AON in 2023 and in my

**[01:08]** acquired by AON in 2023 and in my

**[01:08]** acquired by AON in 2023 and in my previous role I headed up city bank's

**[01:10]** previous role I headed up city bank's

**[01:10]** previous role I headed up city bank's genai engineering team.

**[01:13]** genai engineering team.

**[01:13]** genai engineering team. Now here's our agenda for today. Um

**[01:16]** Now here's our agenda for today. Um

**[01:16]** Now here's our agenda for today. Um we'll begin with the motivation and

**[01:18]** we'll begin with the motivation and

**[01:18]** we'll begin with the motivation and problems that current systems face. Then

**[01:21]** problems that current systems face. Then

**[01:21]** problems that current systems face. Then we'll review the AC framework and its

**[01:24]** we'll review the AC framework and its

**[01:24]** we'll review the AC framework and its limitations.

**[01:26]** limitations.

**[01:26]** limitations. Um after surveying recent research uh

**[01:29]** Um after surveying recent research uh

**[01:29]** Um after surveying recent research uh insights, we'll introduce the meta AC

**[01:31]** insights, we'll introduce the meta AC

**[01:31]** insights, we'll introduce the meta AC approach. We'll discuss its architecture

**[01:34]** approach. We'll discuss its architecture

**[01:34]** approach. We'll discuss its architecture and strategy toolbox, show some results

**[01:37]** and strategy toolbox, show some results

**[01:38]** and strategy toolbox, show some results um and finish with future directions on

**[01:40]** um and finish with future directions on

**[01:40]** um and finish with future directions on challenges.

**[01:43]** challenges.

**[01:43]** challenges. Now the agentic context engineering

**[01:45]** Now the agentic context engineering

**[01:45]** Now the agentic context engineering framework or AC for short uh for which

**[01:48]** framework or AC for short uh for which

**[01:48]** framework or AC for short uh for which you've got the paper link uh on the

**[01:50]** you've got the paper link uh on the

**[01:50]** you've got the paper link uh on the slide there. So it's it's very popular

**[01:53]** slide there. So it's it's very popular

**[01:53]** slide there. So it's it's very popular framework um and the paper um came out a

**[01:56]** framework um and the paper um came out a

**[01:56]** framework um and the paper um came out a few months ago. Um basically organizes a


### [02:00 - 03:00]

**[02:00]** few months ago. Um basically organizes a

**[02:00]** few months ago. Um basically organizes a patient into three roles. First of all

**[02:02]** patient into three roles. First of all

**[02:02]** patient into three roles. First of all there's a generator that produces

**[02:04]** there's a generator that produces

**[02:04]** there's a generator that produces reasoning paths. Then there's a

**[02:06]** reasoning paths. Then there's a

**[02:06]** reasoning paths. Then there's a reflector that extracts lessons. And

**[02:09]** reflector that extracts lessons. And

**[02:09]** reflector that extracts lessons. And finally, there is a curator that

**[02:10]** finally, there is a curator that

**[02:10]** finally, there is a curator that synthesizes these lessons into

**[02:12]** synthesizes these lessons into

**[02:12]** synthesizes these lessons into incremental updates.

**[02:14]** incremental updates.

**[02:14]** incremental updates. AC uses incremental delta updates and a

**[02:17]** AC uses incremental delta updates and a

**[02:18]** AC uses incremental delta updates and a grow and refine mechanism to prevent

**[02:20]** grow and refine mechanism to prevent

**[02:20]** grow and refine mechanism to prevent context collapse and maintain relevance.

**[02:23]** context collapse and maintain relevance.

**[02:23]** context collapse and maintain relevance. Now, most importantly, it can improve

**[02:25]** Now, most importantly, it can improve

**[02:25]** Now, most importantly, it can improve without label data by learning directly

**[02:28]** without label data by learning directly

**[02:28]** without label data by learning directly from execution feedback.

**[02:31]** from execution feedback.

**[02:32]** from execution feedback. Now so AC has been um quite successful

**[02:35]** Now so AC has been um quite successful

**[02:35]** Now so AC has been um quite successful and has achieved substantial gains

**[02:37]** and has achieved substantial gains

**[02:37]** and has achieved substantial gains across some of the most popular HM

**[02:39]** across some of the most popular HM

**[02:39]** across some of the most popular HM benchmarks like Upworld or finer uh

**[02:42]** benchmarks like Upworld or finer uh

**[02:42]** benchmarks like Upworld or finer uh almost an 11% compared to previous

**[02:45]** almost an 11% compared to previous

**[02:45]** almost an 11% compared to previous state-of-the-art approaches such as Japa

**[02:48]** state-of-the-art approaches such as Japa

**[02:48]** state-of-the-art approaches such as Japa or DC.

**[02:50]** or DC.

**[02:50]** or DC. Um and it's also achieved an 8.6%

**[02:54]** Um and it's also achieved an 8.6%

**[02:54]** Um and it's also achieved an 8.6% um gain on financial reasoning tasks.

**[02:58]** um gain on financial reasoning tasks.

**[02:58]** um gain on financial reasoning tasks. Um there are four fundamental


### [03:00 - 04:00]

**[03:01]** Um there are four fundamental

**[03:01]** Um there are four fundamental limitations um for AC that I'm going to

**[03:05]** limitations um for AC that I'm going to

**[03:05]** limitations um for AC that I'm going to reflect on and um just discuss on the

**[03:08]** reflect on and um just discuss on the

**[03:08]** reflect on and um just discuss on the next slide. Um and those form the basis

**[03:11]** next slide. Um and those form the basis

**[03:11]** next slide. Um and those form the basis for um for meta AC basically.

**[03:15]** for um for meta AC basically.

**[03:15]** for um for meta AC basically. Now as I was saying um despite it

**[03:18]** Now as I was saying um despite it

**[03:18]** Now as I was saying um despite it strength AC has got four critical

**[03:21]** strength AC has got four critical

**[03:21]** strength AC has got four critical failure modes. First it is highly

**[03:24]** failure modes. First it is highly

**[03:24]** failure modes. First it is highly dependent on the reflector. Um so when

**[03:27]** dependent on the reflector. Um so when

**[03:27]** dependent on the reflector. Um so when reflection fails the context becomes

**[03:28]** reflection fails the context becomes

**[03:28]** reflection fails the context becomes noisy and even harmful.

**[03:32]** noisy and even harmful.

**[03:32]** noisy and even harmful. Uh secondly there's feedback

**[03:34]** Uh secondly there's feedback

**[03:34]** Uh secondly there's feedback brittleleness which means that when

**[03:36]** brittleleness which means that when

**[03:36]** brittleleness which means that when ground truth signals are weak or absent

**[03:38]** ground truth signals are weak or absent

**[03:38]** ground truth signals are weak or absent AC may reinforce incorrect behaviors.

**[03:43]** AC may reinforce incorrect behaviors.

**[03:43]** AC may reinforce incorrect behaviors. Third, the the task complexity blindness

**[03:46]** Third, the the task complexity blindness

**[03:46]** Third, the the task complexity blindness um which leads to treat simple and

**[03:49]** um which leads to treat simple and

**[03:49]** um which leads to treat simple and complex tasks the same which can be a

**[03:52]** complex tasks the same which can be a

**[03:52]** complex tasks the same which can be a waste of resource uh and also a miss of

**[03:55]** waste of resource uh and also a miss of

**[03:55]** waste of resource uh and also a miss of opportunities um for optimization

**[03:59]** opportunities um for optimization

**[03:59]** opportunities um for optimization and then finally um AC optimizes only


### [04:00 - 05:00]

**[04:02]** and then finally um AC optimizes only

**[04:02]** and then finally um AC optimizes only the context dimension so ignores compute

**[04:04]** the context dimension so ignores compute

**[04:04]** the context dimension so ignores compute memory and parameter updates.

**[04:08]** memory and parameter updates.

**[04:08]** memory and parameter updates. Now the 24 and 25 research landscape

**[04:11]** Now the 24 and 25 research landscape

**[04:11]** Now the 24 and 25 research landscape offers um four key insights in my views.

**[04:15]** offers um four key insights in my views.

**[04:15]** offers um four key insights in my views. First of all uh verification me

**[04:17]** First of all uh verification me

**[04:17]** First of all uh verification me mechanisms uh like self evaluation,

**[04:20]** mechanisms uh like self evaluation,

**[04:20]** mechanisms uh like self evaluation, multimodel consensus and execution

**[04:22]** multimodel consensus and execution

**[04:22]** multimodel consensus and execution checks are really important for

**[04:25]** checks are really important for

**[04:25]** checks are really important for robustness of any solution.

**[04:28]** robustness of any solution.

**[04:28]** robustness of any solution. Secondly, uh adaptive compute allocation

**[04:31]** Secondly, uh adaptive compute allocation

**[04:31]** Secondly, uh adaptive compute allocation shows that small models can outperform

**[04:33]** shows that small models can outperform

**[04:33]** shows that small models can outperform much larger ones by selectively

**[04:36]** much larger ones by selectively

**[04:36]** much larger ones by selectively increasing inference steps.

**[04:39]** increasing inference steps.

**[04:39]** increasing inference steps. The third one is that structured memory

**[04:41]** The third one is that structured memory

**[04:41]** The third one is that structured memory architectures outperform linear context

**[04:44]** architectures outperform linear context

**[04:44]** architectures outperform linear context context accumulation by organizing facts

**[04:47]** context accumulation by organizing facts

**[04:47]** context accumulation by organizing facts as graphs or multi-randular memories.

**[04:51]** as graphs or multi-randular memories.

**[04:51]** as graphs or multi-randular memories. Then finally, test time training bridges

**[04:54]** Then finally, test time training bridges

**[04:54]** Then finally, test time training bridges inference and learning uh and enables

**[04:56]** inference and learning uh and enables

**[04:56]** inference and learning uh and enables temporary parameter updates to yield

**[04:58]** temporary parameter updates to yield

**[04:58]** temporary parameter updates to yield large accuracy gains.


### [05:00 - 06:00]

**[05:01]** large accuracy gains.

**[05:01]** large accuracy gains. So these advances suggest that we need a

**[05:03]** So these advances suggest that we need a

**[05:03]** So these advances suggest that we need a hybrid multi-dimensional system.

**[05:08]** hybrid multi-dimensional system.

**[05:08]** hybrid multi-dimensional system. Now, MetaC um addresses AC's limitation

**[05:11]** Now, MetaC um addresses AC's limitation

**[05:12]** Now, MetaC um addresses AC's limitation by adding a meta controller that learns

**[05:14]** by adding a meta controller that learns

**[05:14]** by adding a meta controller that learns to orchestrate multiple adaptation

**[05:17]** to orchestrate multiple adaptation

**[05:17]** to orchestrate multiple adaptation strategies based on a task's complexity,

**[05:20]** strategies based on a task's complexity,

**[05:20]** strategies based on a task's complexity, uncertainty, verifiability,

**[05:23]** uncertainty, verifiability,

**[05:23]** uncertainty, verifiability, and also resource constraints. So

**[05:25]** and also resource constraints. So

**[05:25]** and also resource constraints. So instead of applying the same procedure

**[05:28]** instead of applying the same procedure

**[05:28]** instead of applying the same procedure to every problem, Metaac profiles each

**[05:31]** to every problem, Metaac profiles each

**[05:31]** to every problem, Metaac profiles each task and allocates the right combination

**[05:33]** task and allocates the right combination

**[05:34]** task and allocates the right combination of strategies across context, compute,

**[05:36]** of strategies across context, compute,

**[05:36]** of strategies across context, compute, verification, memory and parameter

**[05:38]** verification, memory and parameter

**[05:38]** verification, memory and parameter dimensions.

**[05:40]** dimensions.

**[05:40]** dimensions. Um so this adaptive uh learned

**[05:43]** Um so this adaptive uh learned

**[05:43]** Um so this adaptive uh learned coordination is what enables it to

**[05:45]** coordination is what enables it to

**[05:45]** coordination is what enables it to outperform single dimension methods.

**[05:53]** Now the the meta framework consists of

**[05:53]** Now the the meta framework consists of four layers. So getting into the

**[05:55]** four layers. So getting into the

**[05:55]** four layers. So getting into the architecture

**[05:57]** architecture

**[05:57]** architecture um the first layer is the task profiling

**[05:59]** um the first layer is the task profiling

**[05:59]** um the first layer is the task profiling one which assesses complexity


### [06:00 - 07:00]

**[06:02]** one which assesses complexity

**[06:02]** one which assesses complexity uncertainty verifiability and resource

**[06:04]** uncertainty verifiability and resource

**[06:04]** uncertainty verifiability and resource budgets.

**[06:06]** budgets.

**[06:06]** budgets. Then there is a lightweight meta

**[06:08]** Then there is a lightweight meta

**[06:08]** Then there is a lightweight meta controller that selects and allocates

**[06:10]** controller that selects and allocates

**[06:10]** controller that selects and allocates adaptation strategies accordingly.

**[06:13]** adaptation strategies accordingly.

**[06:13]** adaptation strategies accordingly. The next layer down is a strategy

**[06:15]** The next layer down is a strategy

**[06:15]** The next layer down is a strategy execution one and the carries out the

**[06:18]** execution one and the carries out the

**[06:18]** execution one and the carries out the reflection, adaptive compute,

**[06:20]** reflection, adaptive compute,

**[06:20]** reflection, adaptive compute, hierarchical verification,

**[06:22]** hierarchical verification,

**[06:22]** hierarchical verification, structure memory retrieval and selective

**[06:25]** structure memory retrieval and selective

**[06:25]** structure memory retrieval and selective uh test time training. And then finally

**[06:29]** uh test time training. And then finally

**[06:29]** uh test time training. And then finally uh there's a feedback aggregation layer

**[06:30]** uh there's a feedback aggregation layer

**[06:30]** uh there's a feedback aggregation layer that collects the outcomes and updates

**[06:33]** that collects the outcomes and updates

**[06:33]** that collects the outcomes and updates the meta controllers policy through

**[06:35]** the meta controllers policy through

**[06:35]** the meta controllers policy through metalarning.

**[06:36]** metalarning.

**[06:36]** metalarning. So this layer design allows the system

**[06:38]** So this layer design allows the system

**[06:38]** So this layer design allows the system to learn from its experience and uh

**[06:41]** to learn from its experience and uh

**[06:41]** to learn from its experience and uh continuously refine its decision making.

**[06:50]** Now in terms of the task profiling um

**[06:50]** Now in terms of the task profiling um there are four key dimensions that are

**[06:52]** there are four key dimensions that are

**[06:52]** there are four key dimensions that are being assessed. The first one is uh

**[06:55]** being assessed. The first one is uh

**[06:55]** being assessed. The first one is uh semantic complexity. So this is

**[06:57]** semantic complexity. So this is

**[06:58]** semantic complexity. So this is basically an embedding based similarity


### [07:00 - 08:00]

**[07:00]** basically an embedding based similarity

**[07:00]** basically an embedding based similarity to uh known dash distributions that gets

**[07:03]** to uh known dash distributions that gets

**[07:03]** to uh known dash distributions that gets produced.

**[07:05]** produced.

**[07:05]** produced. Uh second one is uncertainty

**[07:07]** Uh second one is uncertainty

**[07:07]** Uh second one is uncertainty quantification.

**[07:09]** quantification.

**[07:09]** quantification. Uh think of it as a relative softmax uh

**[07:12]** Uh think of it as a relative softmax uh

**[07:12]** Uh think of it as a relative softmax uh scoring that predicts model confidence.

**[07:15]** scoring that predicts model confidence.

**[07:15]** scoring that predicts model confidence. The third one is verifiability

**[07:17]** The third one is verifiability

**[07:17]** The third one is verifiability assessment. So whether we can execute

**[07:19]** assessment. So whether we can execute

**[07:19]** assessment. So whether we can execute and validate the output.

**[07:22]** and validate the output.

**[07:22]** and validate the output. And then the fourth one is resource

**[07:24]** And then the fourth one is resource

**[07:24]** And then the fourth one is resource availability. So we take into

**[07:26]** availability. So we take into

**[07:26]** availability. So we take into consideration the context window, the

**[07:28]** consideration the context window, the

**[07:28]** consideration the context window, the compute budget and even other

**[07:30]** compute budget and even other

**[07:30]** compute budget and even other constraints such as time.

**[07:32]** constraints such as time.

**[07:32]** constraints such as time. So the output of this layer of the task

**[07:35]** So the output of this layer of the task

**[07:35]** So the output of this layer of the task profiling layer is a 32dimensional task

**[07:38]** profiling layer is a 32dimensional task

**[07:38]** profiling layer is a 32dimensional task embedding which is what fits as input

**[07:41]** embedding which is what fits as input

**[07:41]** embedding which is what fits as input into the meta controller.

**[07:48]** Now in terms of the strategy toolbox um

**[07:48]** Now in terms of the strategy toolbox um meta draws from six strategies.

**[07:51]** meta draws from six strategies.

**[07:51]** meta draws from six strategies. First one is minimal context which uses

**[07:54]** First one is minimal context which uses

**[07:54]** First one is minimal context which uses concise prompts for simple tasks.

**[07:58]** concise prompts for simple tasks.

**[07:58]** concise prompts for simple tasks. Um then we use AC reflection uh which


### [08:00 - 09:00]

**[08:01]** Um then we use AC reflection uh which

**[08:01]** Um then we use AC reflection uh which retains the generator reflector curator

**[08:04]** retains the generator reflector curator

**[08:04]** retains the generator reflector curator loop for incremental knowledge

**[08:05]** loop for incremental knowledge

**[08:05]** loop for incremental knowledge accumulation um as established by uh

**[08:08]** accumulation um as established by uh

**[08:08]** accumulation um as established by uh standard AC.

**[08:10]** standard AC.

**[08:10]** standard AC. Then we also use adaptive compute which

**[08:13]** Then we also use adaptive compute which

**[08:13]** Then we also use adaptive compute which scales the number of reasoning steps or

**[08:15]** scales the number of reasoning steps or

**[08:15]** scales the number of reasoning steps or samples based on the task difficulty.

**[08:19]** samples based on the task difficulty.

**[08:19]** samples based on the task difficulty. We also use hierarchical verification

**[08:22]** We also use hierarchical verification

**[08:22]** We also use hierarchical verification that combines self-evaluation multimodal

**[08:25]** that combines self-evaluation multimodal

**[08:25]** that combines self-evaluation multimodal consensus and execution checks.

**[08:28]** consensus and execution checks.

**[08:28]** consensus and execution checks. uh adaptive memory uh that retrieves

**[08:31]** uh adaptive memory uh that retrieves

**[08:31]** uh adaptive memory uh that retrieves relevant information from structured

**[08:32]** relevant information from structured

**[08:32]** relevant information from structured multi granular memories and then finally

**[08:35]** multi granular memories and then finally

**[08:35]** multi granular memories and then finally we use selective test time training

**[08:38]** we use selective test time training

**[08:38]** we use selective test time training which applies temporary parameter

**[08:40]** which applies temporary parameter

**[08:40]** which applies temporary parameter updates such as lower adapters for high

**[08:42]** updates such as lower adapters for high

**[08:42]** updates such as lower adapters for high stakes tasks.

**[08:44]** stakes tasks.

**[08:44]** stakes tasks. So the meta controller learns to combine

**[08:46]** So the meta controller learns to combine

**[08:46]** So the meta controller learns to combine these tools effectively over time.

**[08:51]** these tools effectively over time.

**[08:51]** these tools effectively over time. Now the um reward formula um upon which

**[08:55]** Now the um reward formula um upon which

**[08:55]** Now the um reward formula um upon which the the learning strategy is selected

**[08:59]** the the learning strategy is selected

**[08:59]** the the learning strategy is selected accounts for the following components.


### [09:00 - 10:00]

**[09:01]** accounts for the following components.

**[09:01]** accounts for the following components. Um the first one is the correctness of

**[09:04]** Um the first one is the correctness of

**[09:04]** Um the first one is the correctness of an action or prediction which is

**[09:05]** an action or prediction which is

**[09:05]** an action or prediction which is accuracy.

**[09:07]** accuracy.

**[09:07]** accuracy. Then we also have the penalty associated

**[09:11]** Then we also have the penalty associated

**[09:11]** Then we also have the penalty associated um with resources used or negative

**[09:13]** um with resources used or negative

**[09:13]** um with resources used or negative outcomes. So one minus cost and then is

**[09:16]** outcomes. So one minus cost and then is

**[09:16]** outcomes. So one minus cost and then is the trustworthiness of the models which

**[09:18]** the trustworthiness of the models which

**[09:18]** the trustworthiness of the models which is self-expressed certainty.

**[09:21]** is self-expressed certainty.

**[09:21]** is self-expressed certainty. So the confidence calibration basically

**[09:23]** So the confidence calibration basically

**[09:23]** So the confidence calibration basically uh with weighted importance determined

**[09:25]** uh with weighted importance determined

**[09:25]** uh with weighted importance determined by the hyperparameters alpha, beta and

**[09:27]** by the hyperparameters alpha, beta and

**[09:28]** by the hyperparameters alpha, beta and gamma.

**[09:35]** In terms of the uh metalarning loop um

**[09:35]** In terms of the uh metalarning loop um we have four sources of feedback

**[09:37]** we have four sources of feedback

**[09:37]** we have four sources of feedback collection. Uh first of all is task

**[09:40]** collection. Uh first of all is task

**[09:40]** collection. Uh first of all is task outcomes. The success failure or

**[09:43]** outcomes. The success failure or

**[09:43]** outcomes. The success failure or correctness um of the task. Then we've

**[09:47]** correctness um of the task. Then we've

**[09:47]** correctness um of the task. Then we've got the strategy performance. So what is

**[09:49]** got the strategy performance. So what is

**[09:50]** got the strategy performance. So what is the individual contribution of each

**[09:52]** the individual contribution of each

**[09:52]** the individual contribution of each strategy to the overall performance of

**[09:54]** strategy to the overall performance of

**[09:54]** strategy to the overall performance of the task?

**[09:56]** the task?

**[09:56]** the task? Then we also have efficiency metrics

**[09:58]** Then we also have efficiency metrics

**[09:58]** Then we also have efficiency metrics such as the compute, latency, memory.


### [10:00 - 11:00]

**[10:02]** such as the compute, latency, memory.

**[10:02]** such as the compute, latency, memory. And then finally we've got confidence

**[10:04]** And then finally we've got confidence

**[10:04]** And then finally we've got confidence calibration. So where predictions are

**[10:07]** calibration. So where predictions are

**[10:07]** calibration. So where predictions are accurate.

**[10:15]** Um so moving on to um how we go on about

**[10:15]** Um so moving on to um how we go on about uh solving the uh the limitations from

**[10:18]** uh solving the uh the limitations from

**[10:18]** uh solving the uh the limitations from AC. The first one was the weak reflector

**[10:21]** AC. The first one was the weak reflector

**[10:21]** AC. The first one was the weak reflector problem. So AC's issue is that there is

**[10:25]** problem. So AC's issue is that there is

**[10:25]** problem. So AC's issue is that there is a a 50 to 60% performance drop when

**[10:28]** a a 50 to 60% performance drop when

**[10:28]** a a 50 to 60% performance drop when reflector quality degrades. Um with beta

**[10:31]** reflector quality degrades. Um with beta

**[10:31]** reflector quality degrades. Um with beta AC we introduce um uh three things

**[10:35]** AC we introduce um uh three things

**[10:35]** AC we introduce um uh three things basically. So first of all is quality

**[10:38]** basically. So first of all is quality

**[10:38]** basically. So first of all is quality gates. Um so it's a learned classifier

**[10:42]** gates. Um so it's a learned classifier

**[10:42]** gates. Um so it's a learned classifier that blocks harmful deltas and secondly

**[10:45]** that blocks harmful deltas and secondly

**[10:45]** that blocks harmful deltas and secondly there's a multi- signal reflector uh or

**[10:48]** there's a multi- signal reflector uh or

**[10:48]** there's a multi- signal reflector uh or reflection which basically um is an

**[10:50]** reflection which basically um is an

**[10:50]** reflection which basically um is an ensemble of specialist models uh when

**[10:53]** ensemble of specialist models uh when

**[10:53]** ensemble of specialist models uh when there is a level of uncertainty.

**[10:56]** there is a level of uncertainty.

**[10:56]** there is a level of uncertainty. Uh and then the third one is adaptive

**[10:59]** Uh and then the third one is adaptive

**[10:59]** Uh and then the third one is adaptive strategy allocation. So the meta


### [11:00 - 12:00]

**[11:01]** strategy allocation. So the meta

**[11:01]** strategy allocation. So the meta controller learns when reflection fails

**[11:04]** controller learns when reflection fails

**[11:04]** controller learns when reflection fails and then it roots to verification or

**[11:06]** and then it roots to verification or

**[11:06]** and then it roots to verification or test time compute instead.

**[11:09]** test time compute instead.

**[11:09]** test time compute instead. Um so we can expect to maintain an 80%

**[11:13]** Um so we can expect to maintain an 80%

**[11:13]** Um so we can expect to maintain an 80% plus performance even when the uh

**[11:15]** plus performance even when the uh

**[11:15]** plus performance even when the uh reflector degrades around 30%.

**[11:24]** Now the the second um limitation we had

**[11:24]** Now the the second um limitation we had was um the feedback quality

**[11:26]** was um the feedback quality

**[11:26]** was um the feedback quality brittleleness.

**[11:28]** brittleleness.

**[11:28]** brittleleness. So what we observe with AC is that there

**[11:30]** So what we observe with AC is that there

**[11:30]** So what we observe with AC is that there can be significant degradation without

**[11:33]** can be significant degradation without

**[11:33]** can be significant degradation without reliable ground truth signals.

**[11:36]** reliable ground truth signals.

**[11:36]** reliable ground truth signals. Uh with beta AC we introduce a

**[11:38]** Uh with beta AC we introduce a

**[11:38]** Uh with beta AC we introduce a hierarchical verification cascade um

**[11:41]** hierarchical verification cascade um

**[11:41]** hierarchical verification cascade um where we can expect a 50 to 60%

**[11:44]** where we can expect a 50 to 60%

**[11:44]** where we can expect a 50 to 60% reduction in errors from poor feedback

**[11:47]** reduction in errors from poor feedback

**[11:47]** reduction in errors from poor feedback and that's through three tiers. The

**[11:49]** and that's through three tiers. The

**[11:49]** and that's through three tiers. The first tier is self verification which is

**[11:52]** first tier is self verification which is

**[11:52]** first tier is self verification which is just fast filter. We just accept if the

**[11:55]** just fast filter. We just accept if the

**[11:55]** just fast filter. We just accept if the confidence level is over a certain

**[11:57]** confidence level is over a certain

**[11:57]** confidence level is over a certain value. Second tier is a multimodel


### [12:00 - 13:00]

**[12:00]** value. Second tier is a multimodel

**[12:00]** value. Second tier is a multimodel consensus. So we leverage a diverse

**[12:03]** consensus. So we leverage a diverse

**[12:03]** consensus. So we leverage a diverse range of models such as GBT4, claude and

**[12:07]** range of models such as GBT4, claude and

**[12:07]** range of models such as GBT4, claude and dips and we do confidence weighted

**[12:09]** dips and we do confidence weighted

**[12:09]** dips and we do confidence weighted voting. And then the tier three is

**[12:13]** voting. And then the tier three is

**[12:13]** voting. And then the tier three is execution based verification

**[12:16]** execution based verification

**[12:16]** execution based verification uh where we leverage code sandbox APA

**[12:18]** uh where we leverage code sandbox APA

**[12:18]** uh where we leverage code sandbox APA API validation and schema compliance.

**[12:27]** Um the the third um limitation we had

**[12:27]** Um the the third um limitation we had was uh task complexity mismatch. Um so

**[12:31]** was uh task complexity mismatch. Um so

**[12:31]** was uh task complexity mismatch. Um so in a sense the fact that AC uses uniform

**[12:35]** in a sense the fact that AC uses uniform

**[12:36]** in a sense the fact that AC uses uniform processing um also for simple tasks

**[12:39]** processing um also for simple tasks

**[12:39]** processing um also for simple tasks which can be a waste of resource. So

**[12:42]** which can be a waste of resource. So

**[12:42]** which can be a waste of resource. So meta adapts uh strategy allocation

**[12:45]** meta adapts uh strategy allocation

**[12:45]** meta adapts uh strategy allocation dynamically rather than using the same

**[12:47]** dynamically rather than using the same

**[12:47]** dynamically rather than using the same heavy pipeline for everything. The

**[12:49]** heavy pipeline for everything. The

**[12:50]** heavy pipeline for everything. The alphas are allocation weights for the

**[12:52]** alphas are allocation weights for the

**[12:52]** alphas are allocation weights for the six optimization strategies and they

**[12:55]** six optimization strategies and they

**[12:55]** six optimization strategies and they represent how much computational budget

**[12:57]** represent how much computational budget

**[12:57]** represent how much computational budget is assigned to each strategy for a given


### [13:00 - 14:00]

**[13:00]** is assigned to each strategy for a given

**[13:00]** is assigned to each strategy for a given task. So simple tasks um require minimal

**[13:05]** task. So simple tasks um require minimal

**[13:05]** task. So simple tasks um require minimal processing can save n around a 90% uh

**[13:09]** processing can save n around a 90% uh

**[13:09]** processing can save n around a 90% uh compute compared to standard AC.

**[13:13]** compute compared to standard AC.

**[13:13]** compute compared to standard AC. moderate tasks um is more of a balanced

**[13:16]** moderate tasks um is more of a balanced

**[13:16]** moderate tasks um is more of a balanced approach um that include AC plus

**[13:19]** approach um that include AC plus

**[13:20]** approach um that include AC plus verification and then complex tasks um

**[13:23]** verification and then complex tasks um

**[13:23]** verification and then complex tasks um basically heavy test time compute

**[13:26]** basically heavy test time compute

**[13:26]** basically heavy test time compute multiple attempts and memory retrieval.

**[13:35]** Um so just to conclude with some results

**[13:35]** Um so just to conclude with some results um and and these are initial results uh

**[13:38]** um and and these are initial results uh

**[13:38]** um and and these are initial results uh we have observed um around an 8 to 11%

**[13:42]** we have observed um around an 8 to 11%

**[13:42]** we have observed um around an 8 to 11% uh improvement on agent benchmarks.

**[13:46]** uh improvement on agent benchmarks.

**[13:46]** uh improvement on agent benchmarks. Um we have also observed a six to eight

**[13:49]** Um we have also observed a six to eight

**[13:49]** Um we have also observed a six to eight points improvement on on some domain

**[13:52]** points improvement on on some domain

**[13:52]** points improvement on on some domain specific tasks. um also a 30 to 40%

**[13:56]** specific tasks. um also a 30 to 40%

**[13:56]** specific tasks. um also a 30 to 40% reduction in compute costs um through

**[13:59]** reduction in compute costs um through

**[13:59]** reduction in compute costs um through the allocation of um adaptive strategies


### [14:00 - 15:00]

**[14:04]** the allocation of um adaptive strategies

**[14:04]** the allocation of um adaptive strategies um and overall there's um there's more

**[14:07]** um and overall there's um there's more

**[14:07]** um and overall there's um there's more robustness more consistency

**[14:09]** robustness more consistency

**[14:10]** robustness more consistency um and you know we can generalize better

**[14:13]** um and you know we can generalize better

**[14:13]** um and you know we can generalize better we can use the framework across a a

**[14:16]** we can use the framework across a a

**[14:16]** we can use the framework across a a diverse range of of domains so the

**[14:19]** diverse range of of domains so the

**[14:19]** diverse range of of domains so the conclusion is that um meta can can

**[14:22]** conclusion is that um meta can can

**[14:22]** conclusion is that um meta can can orchestrate ates a context compute and

**[14:25]** orchestrate ates a context compute and

**[14:25]** orchestrate ates a context compute and verification and memory and parameter

**[14:27]** verification and memory and parameter

**[14:27]** verification and memory and parameter adaptation and produce a robust uh

**[14:31]** adaptation and produce a robust uh

**[14:31]** adaptation and produce a robust uh self-improvement

**[14:32]** self-improvement

**[14:32]** self-improvement um framework for agents.

**[14:35]** um framework for agents.

**[14:35]** um framework for agents. Um future work will implement uh and

**[14:38]** Um future work will implement uh and

**[14:38]** Um future work will implement uh and evaluate the full system across uh a a

**[14:43]** evaluate the full system across uh a a

**[14:43]** evaluate the full system across uh a a more diverse range of domains and we'll

**[14:46]** more diverse range of domains and we'll

**[14:46]** more diverse range of domains and we'll continue exploring metalarning and this

**[14:49]** continue exploring metalarning and this

**[14:49]** continue exploring metalarning and this will involve also incorporating um

**[14:52]** will involve also incorporating um

**[14:52]** will involve also incorporating um additional strategies as well.

**[14:56]** additional strategies as well.

**[14:56]** additional strategies as well. Now I also wanted to touch on um

**[14:58]** Now I also wanted to touch on um

**[14:58]** Now I also wanted to touch on um additional applications of meta that I


### [15:00 - 16:00]

**[15:01]** additional applications of meta that I

**[15:01]** additional applications of meta that I think are quite relevant. Um so first

**[15:05]** think are quite relevant. Um so first

**[15:05]** think are quite relevant. Um so first one is um for multimodel AI systems. So

**[15:09]** one is um for multimodel AI systems. So

**[15:09]** one is um for multimodel AI systems. So for example deciding when to use vision

**[15:12]** for example deciding when to use vision

**[15:12]** for example deciding when to use vision versus uh language processing again can

**[15:15]** versus uh language processing again can

**[15:15]** versus uh language processing again can be um a like a a meta adaptive uh

**[15:19]** be um a like a a meta adaptive uh

**[15:19]** be um a like a a meta adaptive uh strategy decisioning.

**[15:21]** strategy decisioning.

**[15:21]** strategy decisioning. Um also when you have uh compound AI

**[15:25]** Um also when you have uh compound AI

**[15:25]** Um also when you have uh compound AI systems that um require different models

**[15:29]** systems that um require different models

**[15:29]** systems that um require different models for different stages um and the

**[15:32]** for different stages um and the

**[15:32]** for different stages um and the complexity is um you know is substantial

**[15:37]** complexity is um you know is substantial

**[15:37]** complexity is um you know is substantial uh we can actually um uh in a in a meta

**[15:41]** uh we can actually um uh in a in a meta

**[15:41]** uh we can actually um uh in a in a meta adaptive manner uh select the most

**[15:43]** adaptive manner uh select the most

**[15:43]** adaptive manner uh select the most effective uh strategies to to resolve a

**[15:47]** effective uh strategies to to resolve a

**[15:47]** effective uh strategies to to resolve a task and to end. um also um for human

**[15:52]** task and to end. um also um for human

**[15:52]** task and to end. um also um for human collaboration um so in other words to

**[15:54]** collaboration um so in other words to

**[15:54]** collaboration um so in other words to determine when to have a human in the

**[15:57]** determine when to have a human in the

**[15:57]** determine when to have a human in the loop and also for continual learning


### [16:00 - 17:00]

**[16:00]** loop and also for continual learning

**[16:00]** loop and also for continual learning systems um where we are balancing

**[16:03]** systems um where we are balancing

**[16:03]** systems um where we are balancing exploration versus exploitation.

**[16:06]** exploration versus exploitation.

**[16:06]** exploration versus exploitation. Um so the the core takeaway is that

**[16:10]** Um so the the core takeaway is that

**[16:10]** Um so the the core takeaway is that optimization requires a meta layer of

**[16:13]** optimization requires a meta layer of

**[16:13]** optimization requires a meta layer of intelligence and and that has to be

**[16:15]** intelligence and and that has to be

**[16:15]** intelligence and and that has to be trained um and you know um it requires

**[16:20]** trained um and you know um it requires

**[16:20]** trained um and you know um it requires um a lot of trial and error before it

**[16:22]** um a lot of trial and error before it

**[16:22]** um a lot of trial and error before it can actually um perform at the right

**[16:25]** can actually um perform at the right

**[16:25]** can actually um perform at the right level.

**[16:27]** level.

**[16:27]** level. In terms of the future direction and

**[16:29]** In terms of the future direction and

**[16:29]** In terms of the future direction and challenges um there are still several

**[16:32]** challenges um there are still several

**[16:32]** challenges um there are still several challenges that remain. So the meta

**[16:34]** challenges that remain. So the meta

**[16:34]** challenges that remain. So the meta controllers training u may be unstable

**[16:37]** controllers training u may be unstable

**[16:37]** controllers training u may be unstable um due to sparse rewards and that this

**[16:39]** um due to sparse rewards and that this

**[16:39]** um due to sparse rewards and that this can be mitigated through curriculum

**[16:41]** can be mitigated through curriculum

**[16:41]** can be mitigated through curriculum learning. Uh also robust advantage

**[16:44]** learning. Uh also robust advantage

**[16:44]** learning. Uh also robust advantage estimation and um regularization of

**[16:47]** estimation and um regularization of

**[16:47]** estimation and um regularization of entropy.

**[16:49]** entropy.

**[16:49]** entropy. Also computational overhead from

**[16:51]** Also computational overhead from

**[16:51]** Also computational overhead from profiling and multiple uh strategies um

**[16:55]** profiling and multiple uh strategies um

**[16:55]** profiling and multiple uh strategies um needs to be reduced with efficient

**[16:57]** needs to be reduced with efficient

**[16:57]** needs to be reduced with efficient models. Um we can leverage things like

**[16:59]** models. Um we can leverage things like


### [17:00 - 18:00]

**[17:00]** models. Um we can leverage things like lazy execution, batching and caching.

**[17:04]** lazy execution, batching and caching.

**[17:04]** lazy execution, batching and caching. Um also uh the ver verification uh

**[17:08]** Um also uh the ver verification uh

**[17:08]** Um also uh the ver verification uh cascades can be brittle if all models um

**[17:11]** cascades can be brittle if all models um

**[17:11]** cascades can be brittle if all models um make the same mistake. So we need

**[17:13]** make the same mistake. So we need

**[17:13]** make the same mistake. So we need diverse models um with confidence

**[17:17]** diverse models um with confidence

**[17:17]** diverse models um with confidence waiting and human oversight um as well

**[17:20]** waiting and human oversight um as well

**[17:20]** waiting and human oversight um as well as active learning. uh metalarning loops

**[17:23]** as active learning. uh metalarning loops

**[17:23]** as active learning. uh metalarning loops require substantial data. Uh synthetic

**[17:26]** require substantial data. Uh synthetic

**[17:26]** require substantial data. Uh synthetic task uh task generation of policy

**[17:28]** task uh task generation of policy

**[17:28]** task uh task generation of policy learning uh transfer from related

**[17:31]** learning uh transfer from related

**[17:31]** learning uh transfer from related domains and sample efficient algorithms

**[17:34]** domains and sample efficient algorithms

**[17:34]** domains and sample efficient algorithms uh can also help as well. And finally uh

**[17:38]** uh can also help as well. And finally uh

**[17:38]** uh can also help as well. And finally uh addressing these ch these challenges um

**[17:40]** addressing these ch these challenges um

**[17:40]** addressing these ch these challenges um is going to be key to scaling meta and

**[17:44]** is going to be key to scaling meta and

**[17:44]** is going to be key to scaling meta and applying it across um a wide range of

**[17:46]** applying it across um a wide range of

**[17:46]** applying it across um a wide range of domains.

**[17:48]** domains.

**[17:48]** domains. So that was all from me. Thank you very

**[17:50]** So that was all from me. Thank you very

**[17:50]** So that was all from me. Thank you very much for listening. Um, and yeah, uh,

**[17:54]** much for listening. Um, and yeah, uh,

**[17:54]** much for listening. Um, and yeah, uh, appreciate you being there. Thank you.


