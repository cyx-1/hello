# Strategies for LLM Evals (GuideLLM, lm-eval-harness, OpenAI Evals Workshop) — Taylor Jordan Smith

**Video URL:** https://www.youtube.com/watch?v=89NuzmKokIk

---

## Full Transcript

### [00:00 - 01:00]

**[00:18]** Hello everybody. Um, my name is Taylor

**[00:18]** Hello everybody. Um, my name is Taylor Smith. I am an AI developer advocate

**[00:22]** Smith. I am an AI developer advocate

**[00:22]** Smith. I am an AI developer advocate slashevangelist slashtechnical marketing

**[00:25]** slashevangelist slashtechnical marketing

**[00:25]** slashevangelist slashtechnical marketing and other titles depending on where I

**[00:27]** and other titles depending on where I

**[00:27]** and other titles depending on where I am. Um, I work at Red Hat in our AI

**[00:30]** am. Um, I work at Red Hat in our AI

**[00:30]** am. Um, I work at Red Hat in our AI business unit because yes, we do also do

**[00:33]** business unit because yes, we do also do

**[00:33]** business unit because yes, we do also do AI too now. Great. Um, I'm really happy

**[00:37]** AI too now. Great. Um, I'm really happy

**[00:37]** AI too now. Great. Um, I'm really happy to be here. This is my first time at

**[00:39]** to be here. This is my first time at

**[00:39]** to be here. This is my first time at this conference. So, I'm new to the

**[00:41]** this conference. So, I'm new to the

**[00:41]** this conference. So, I'm new to the conference, new to speaking at this

**[00:43]** conference, new to speaking at this

**[00:43]** conference, new to speaking at this conference, ready to have a good time

**[00:45]** conference, ready to have a good time

**[00:45]** conference, ready to have a good time and also relax in about an hour and a

**[00:47]** and also relax in about an hour and a

**[00:47]** and also relax in about an hour and a half and just learn stuff. stoked that

**[00:49]** half and just learn stuff. stoked that

**[00:49]** half and just learn stuff. stoked that this was at 9:00 am. Um, my presentation

**[00:53]** this was at 9:00 am. Um, my presentation

**[00:53]** this was at 9:00 am. Um, my presentation clicker isn't working, so I'm gonna be a

**[00:54]** clicker isn't working, so I'm gonna be a

**[00:54]** clicker isn't working, so I'm gonna be a little bit glued over here. But to kind

**[00:57]** little bit glued over here. But to kind

**[00:57]** little bit glued over here. But to kind of overview what we're going to do

**[00:58]** of overview what we're going to do

**[00:58]** of overview what we're going to do today, I'm going to talk a little bit


### [01:00 - 02:00]

**[01:00]** today, I'm going to talk a little bit

**[01:00]** today, I'm going to talk a little bit about kind of the issues of setting up a

**[01:03]** about kind of the issues of setting up a

**[01:03]** about kind of the issues of setting up a large language model in production and

**[01:05]** large language model in production and

**[01:05]** large language model in production and the reason why you need evaluations and

**[01:08]** the reason why you need evaluations and

**[01:08]** the reason why you need evaluations and benchmarks and all of these things and

**[01:10]** benchmarks and all of these things and

**[01:10]** benchmarks and all of these things and why that is so critical. And then I do

**[01:12]** why that is so critical. And then I do

**[01:12]** why that is so critical. And then I do have some hands-on activities that we'll

**[01:15]** have some hands-on activities that we'll

**[01:15]** have some hands-on activities that we'll get to do to use some evaluation um

**[01:18]** get to do to use some evaluation um

**[01:18]** get to do to use some evaluation um methods and benchmark tools to kind of

**[01:20]** methods and benchmark tools to kind of

**[01:20]** methods and benchmark tools to kind of get a sense of what is out there to use,

**[01:23]** get a sense of what is out there to use,

**[01:23]** get a sense of what is out there to use, how we can use those tools, what that

**[01:25]** how we can use those tools, what that

**[01:25]** how we can use those tools, what that might look like to put it all together

**[01:27]** might look like to put it all together

**[01:27]** might look like to put it all together for an actual production system. So,

**[01:31]** for an actual production system. So,

**[01:31]** for an actual production system. So, ready? Are you excited?

**[01:33]** ready? Are you excited?

**[01:33]** ready? Are you excited? >> Yay. First thing in the morning. Love

**[01:36]** >> Yay. First thing in the morning. Love

**[01:36]** >> Yay. First thing in the morning. Love that. I'm glad it's 9:00 a.m. because

**[01:38]** that. I'm glad it's 9:00 a.m. because

**[01:38]** that. I'm glad it's 9:00 a.m. because that feels like a reasonable start time.

**[01:39]** that feels like a reasonable start time.

**[01:39]** that feels like a reasonable start time. I don't like that 8 am stuff that

**[01:41]** I don't like that 8 am stuff that

**[01:41]** I don't like that 8 am stuff that happens. Um, setting up generative AI

**[01:45]** happens. Um, setting up generative AI

**[01:45]** happens. Um, setting up generative AI tech in production. If you think about

**[01:48]** tech in production. If you think about

**[01:48]** tech in production. If you think about it, crazy pants. Okay, there's so many

**[01:50]** it, crazy pants. Okay, there's so many

**[01:50]** it, crazy pants. Okay, there's so many things that could go wrong. This is such

**[01:52]** things that could go wrong. This is such

**[01:52]** things that could go wrong. This is such a complex type of technology that is

**[01:54]** a complex type of technology that is

**[01:54]** a complex type of technology that is very creative. Setting this up to be

**[01:57]** very creative. Setting this up to be

**[01:57]** very creative. Setting this up to be scalable and reliable and safe is


### [02:00 - 03:00]

**[02:01]** scalable and reliable and safe is

**[02:01]** scalable and reliable and safe is challenging. Okay, that's why we need

**[02:02]** challenging. Okay, that's why we need

**[02:02]** challenging. Okay, that's why we need evaluations. That's why we need all of

**[02:04]** evaluations. That's why we need all of

**[02:04]** evaluations. That's why we need all of these tests and we need to be careful.

**[02:05]** these tests and we need to be careful.

**[02:05]** these tests and we need to be careful. We need to understand the technology

**[02:07]** We need to understand the technology

**[02:07]** We need to understand the technology we're working with when we're looking to

**[02:08]** we're working with when we're looking to

**[02:08]** we're working with when we're looking to implement this as well. So hard to do

**[02:13]** implement this as well. So hard to do

**[02:13]** implement this as well. So hard to do most organizations. So they don't

**[02:16]** most organizations. So they don't

**[02:16]** most organizations. So they don't typically start off with a multi- aent

**[02:19]** typically start off with a multi- aent

**[02:19]** typically start off with a multi- aent framework, right? And go crazy.

**[02:21]** framework, right? And go crazy.

**[02:21]** framework, right? And go crazy. Typically, they're going to have a kind

**[02:23]** Typically, they're going to have a kind

**[02:23]** Typically, they're going to have a kind of standard repeatable path to maturity.

**[02:26]** of standard repeatable path to maturity.

**[02:26]** of standard repeatable path to maturity. They might start out with, okay, how can

**[02:28]** They might start out with, okay, how can

**[02:28]** They might start out with, okay, how can I automate some things with AI? How can

**[02:29]** I automate some things with AI? How can

**[02:29]** I automate some things with AI? How can I have like a chatbot type of situation?

**[02:31]** I have like a chatbot type of situation?

**[02:31]** I have like a chatbot type of situation? That's kind of the standard that

**[02:32]** That's kind of the standard that

**[02:32]** That's kind of the standard that everybody starts out with. Okay, I maybe

**[02:35]** everybody starts out with. Okay, I maybe

**[02:35]** everybody starts out with. Okay, I maybe want to implement a rag setup. All

**[02:37]** want to implement a rag setup. All

**[02:37]** want to implement a rag setup. All right, let's start to look at agents to

**[02:39]** right, let's start to look at agents to

**[02:39]** right, let's start to look at agents to for on the Red Hat side. We're still

**[02:41]** for on the Red Hat side. We're still

**[02:41]** for on the Red Hat side. We're still dealing with probably like the first

**[02:42]** dealing with probably like the first

**[02:42]** dealing with probably like the first three phases of this maturity with our

**[02:45]** three phases of this maturity with our

**[02:45]** three phases of this maturity with our customers and that's where a lot of

**[02:46]** customers and that's where a lot of

**[02:46]** customers and that's where a lot of people um still are. But we get to talk

**[02:48]** people um still are. But we get to talk

**[02:48]** people um still are. But we get to talk about all the cool advanced stuff at

**[02:49]** about all the cool advanced stuff at

**[02:49]** about all the cool advanced stuff at this conference so we can plan ahead and

**[02:52]** this conference so we can plan ahead and

**[02:52]** this conference so we can plan ahead and think about what we want to implement.

**[02:54]** think about what we want to implement.

**[02:54]** think about what we want to implement. But enterprises, they need to take an

**[02:57]** But enterprises, they need to take an

**[02:57]** But enterprises, they need to take an incremental approach to do this

**[02:59]** incremental approach to do this

**[02:59]** incremental approach to do this successfully.


### [03:00 - 04:00]

**[03:01]** successfully.

**[03:01]** successfully. Genai models, they have a number of

**[03:04]** Genai models, they have a number of

**[03:04]** Genai models, they have a number of drawbacks, right? And we all know about

**[03:06]** drawbacks, right? And we all know about

**[03:06]** drawbacks, right? And we all know about these things. Policy restrictions.

**[03:09]** these things. Policy restrictions.

**[03:09]** these things. Policy restrictions. Typically, if you're a developer at a

**[03:11]** Typically, if you're a developer at a

**[03:11]** Typically, if you're a developer at a company or have whatever type of role,

**[03:13]** company or have whatever type of role,

**[03:13]** company or have whatever type of role, you're restricted in the type of AI that

**[03:15]** you're restricted in the type of AI that

**[03:15]** you're restricted in the type of AI that you can use. Red Hat was just um allowed

**[03:18]** you can use. Red Hat was just um allowed

**[03:18]** you can use. Red Hat was just um allowed to use m Gemini was just made available

**[03:20]** to use m Gemini was just made available

**[03:20]** to use m Gemini was just made available to us, but before that, we weren't

**[03:22]** to us, but before that, we weren't

**[03:22]** to us, but before that, we weren't really allowed to use anything

**[03:26]** really allowed to use anything

**[03:26]** really allowed to use anything officially. Um, so the company policy

**[03:30]** officially. Um, so the company policy

**[03:30]** officially. Um, so the company policy restrictions of the tools you can use

**[03:31]** restrictions of the tools you can use

**[03:31]** restrictions of the tools you can use and the AI you can use is pretty locked

**[03:33]** and the AI you can use is pretty locked

**[03:33]** and the AI you can use is pretty locked down. Typically the legal exposures and

**[03:36]** down. Typically the legal exposures and

**[03:36]** down. Typically the legal exposures and risks of these models, you know, there

**[03:39]** risks of these models, you know, there

**[03:39]** risks of these models, you know, there was the glue incident.

**[03:42]** was the glue incident.

**[03:42]** was the glue incident. Um, they're going to say crazy stuff

**[03:44]** Um, they're going to say crazy stuff

**[03:44]** Um, they're going to say crazy stuff sometimes. How do we guard rail against

**[03:46]** sometimes. How do we guard rail against

**[03:46]** sometimes. How do we guard rail against that and how do we protect our customers

**[03:49]** that and how do we protect our customers

**[03:49]** that and how do we protect our customers against that and account for that when

**[03:50]** against that and account for that when

**[03:50]** against that and account for that when that does happen? Because it's hard to

**[03:52]** that does happen? Because it's hard to

**[03:52]** that does happen? Because it's hard to um, completely avoid. There's the bias

**[03:54]** um, completely avoid. There's the bias

**[03:54]** um, completely avoid. There's the bias and discrimination issues. Most of the

**[03:56]** and discrimination issues. Most of the

**[03:56]** and discrimination issues. Most of the internet data is still largely

**[03:58]** internet data is still largely

**[03:58]** internet data is still largely eurosentric and US-based. So the models


### [04:00 - 05:00]

**[04:02]** eurosentric and US-based. So the models

**[04:02]** eurosentric and US-based. So the models trained on this public internet data of

**[04:04]** trained on this public internet data of

**[04:04]** trained on this public internet data of course is going to be a little skewed,

**[04:06]** course is going to be a little skewed,

**[04:06]** course is going to be a little skewed, right? So we need to be aware of it just

**[04:08]** right? So we need to be aware of it just

**[04:08]** right? So we need to be aware of it just like in regular everyday life. We know

**[04:11]** like in regular everyday life. We know

**[04:11]** like in regular everyday life. We know that bias and discrimination exists. How

**[04:13]** that bias and discrimination exists. How

**[04:13]** that bias and discrimination exists. How do we account and kind of provide guard

**[04:15]** do we account and kind of provide guard

**[04:15]** do we account and kind of provide guard rails to make sure that we adjust and

**[04:17]** rails to make sure that we adjust and

**[04:17]** rails to make sure that we adjust and prevent what we can?

**[04:20]** prevent what we can?

**[04:20]** prevent what we can? Cost and performance. That's probably

**[04:22]** Cost and performance. That's probably

**[04:22]** Cost and performance. That's probably kind of a baseline big one. how much

**[04:25]** kind of a baseline big one. how much

**[04:25]** kind of a baseline big one. how much these genai models cost to run at scale

**[04:27]** these genai models cost to run at scale

**[04:28]** these genai models cost to run at scale in production and the performance

**[04:30]** in production and the performance

**[04:30]** in production and the performance throughput latency etc that we need to

**[04:33]** throughput latency etc that we need to

**[04:33]** throughput latency etc that we need to account for when we have these

**[04:34]** account for when we have these

**[04:34]** account for when we have these production system set up and then the

**[04:37]** production system set up and then the

**[04:37]** production system set up and then the knowledge cut off as well is another

**[04:38]** knowledge cut off as well is another

**[04:38]** knowledge cut off as well is another limitation you know these large frontier

**[04:40]** limitation you know these large frontier

**[04:40]** limitation you know these large frontier models have a knowledge cut off because

**[04:42]** models have a knowledge cut off because

**[04:42]** models have a knowledge cut off because they're not consistently trained so you

**[04:44]** they're not consistently trained so you

**[04:44]** they're not consistently trained so you might be working with a model that was

**[04:46]** might be working with a model that was

**[04:46]** might be working with a model that was cut off a year ago so it's not going to

**[04:48]** cut off a year ago so it's not going to

**[04:48]** cut off a year ago so it's not going to have that up-to-date information which

**[04:50]** have that up-to-date information which

**[04:50]** have that up-to-date information which is why they you know implement rag

**[04:52]** is why they you know implement rag

**[04:52]** is why they you know implement rag systems and agent systems to look out

**[04:54]** systems and agent systems to look out

**[04:54]** systems and agent systems to look out into the internet for more up-to-date

**[04:55]** into the internet for more up-to-date

**[04:55]** into the internet for more up-to-date info. But these are just some of the

**[04:57]** info. But these are just some of the

**[04:57]** info. But these are just some of the kind of drawbacks we need to be aware of

**[04:59]** kind of drawbacks we need to be aware of

**[04:59]** kind of drawbacks we need to be aware of and account for.


### [05:00 - 06:00]

**[05:01]** and account for.

**[05:01]** and account for. Inference at scale, no matter how I'm

**[05:03]** Inference at scale, no matter how I'm

**[05:03]** Inference at scale, no matter how I'm going to go kind of into these

**[05:04]** going to go kind of into these

**[05:04]** going to go kind of into these categories a little more in depth. No

**[05:06]** categories a little more in depth. No

**[05:06]** categories a little more in depth. No matter how good your model is, if it's

**[05:09]** matter how good your model is, if it's

**[05:09]** matter how good your model is, if it's not fast, if it's not reliable, if it's

**[05:11]** not fast, if it's not reliable, if it's

**[05:11]** not fast, if it's not reliable, if it's not affordable, you're screwed a little

**[05:14]** not affordable, you're screwed a little

**[05:14]** not affordable, you're screwed a little bit from the get-go. Okay, so this

**[05:16]** bit from the get-go. Okay, so this

**[05:16]** bit from the get-go. Okay, so this graphic, it shows a classic bottleneck

**[05:18]** graphic, it shows a classic bottleneck

**[05:18]** graphic, it shows a classic bottleneck type of scenario. You got concurrent

**[05:20]** type of scenario. You got concurrent

**[05:20]** type of scenario. You got concurrent user requests which might be represented

**[05:22]** user requests which might be represented

**[05:22]** user requests which might be represented by those green, yellow, and orange dots

**[05:24]** by those green, yellow, and orange dots

**[05:24]** by those green, yellow, and orange dots flowing into a system. But then

**[05:26]** flowing into a system. But then

**[05:26]** flowing into a system. But then traditional inference runtimes typically

**[05:28]** traditional inference runtimes typically

**[05:28]** traditional inference runtimes typically can't handle that kind of load

**[05:29]** can't handle that kind of load

**[05:29]** can't handle that kind of load efficiently. Um to serve real world

**[05:32]** efficiently. Um to serve real world

**[05:32]** efficiently. Um to serve real world traffic, whether you're powering a

**[05:34]** traffic, whether you're powering a

**[05:34]** traffic, whether you're powering a customer support agent, a developer type

**[05:36]** customer support agent, a developer type

**[05:36]** customer support agent, a developer type of co-pilot system, or maybe a rag

**[05:39]** of co-pilot system, or maybe a rag

**[05:39]** of co-pilot system, or maybe a rag pipeline, you need an inference engine

**[05:41]** pipeline, you need an inference engine

**[05:41]** pipeline, you need an inference engine that's purpose-built for scale. So

**[05:43]** that's purpose-built for scale. So

**[05:43]** that's purpose-built for scale. So that's where inference runtimes like TRT

**[05:46]** that's where inference runtimes like TRT

**[05:46]** that's where inference runtimes like TRT SG lang which I know we have a session

**[05:48]** SG lang which I know we have a session

**[05:48]** SG lang which I know we have a session on or at least a couple sessions on VLLM

**[05:51]** on or at least a couple sessions on VLLM

**[05:51]** on or at least a couple sessions on VLLM um that's where Red Hat's kind of

**[05:52]** um that's where Red Hat's kind of

**[05:52]** um that's where Red Hat's kind of focusing that's where those type of

**[05:54]** focusing that's where those type of

**[05:54]** focusing that's where those type of production grade inference runtimes

**[05:56]** production grade inference runtimes

**[05:56]** production grade inference runtimes really need to be utilized.

**[05:59]** really need to be utilized.


### [06:00 - 07:00]

**[06:00]** really need to be utilized. There's a lot of pain points with

**[06:01]** There's a lot of pain points with

**[06:01]** There's a lot of pain points with inference that I just want to double

**[06:02]** inference that I just want to double

**[06:02]** inference that I just want to double down on and some of the activity will be

**[06:05]** down on and some of the activity will be

**[06:05]** down on and some of the activity will be benchmarking and evaluating um these

**[06:08]** benchmarking and evaluating um these

**[06:08]** benchmarking and evaluating um these types of metrics. model inference

**[06:11]** types of metrics. model inference

**[06:11]** types of metrics. model inference performance evaluation under enterprise

**[06:14]** performance evaluation under enterprise

**[06:14]** performance evaluation under enterprise level workload scenarios. It's very

**[06:16]** level workload scenarios. It's very

**[06:16]** level workload scenarios. It's very complicated to actually evaluate this

**[06:19]** complicated to actually evaluate this

**[06:19]** complicated to actually evaluate this appropriately. It requires manual setup

**[06:22]** appropriately. It requires manual setup

**[06:22]** appropriately. It requires manual setup of evaluation runs with various

**[06:24]** of evaluation runs with various

**[06:24]** of evaluation runs with various parameters you have to test. The compute

**[06:26]** parameters you have to test. The compute

**[06:26]** parameters you have to test. The compute load just for performance evaluations as

**[06:29]** load just for performance evaluations as

**[06:29]** load just for performance evaluations as well is also pretty taxing. Um you have

**[06:32]** well is also pretty taxing. Um you have

**[06:32]** well is also pretty taxing. Um you have to make sure the data sets that you're

**[06:34]** to make sure the data sets that you're

**[06:34]** to make sure the data sets that you're using for benchmarking are compatible

**[06:36]** using for benchmarking are compatible

**[06:36]** using for benchmarking are compatible with the models that you're using. the

**[06:39]** with the models that you're using. the

**[06:39]** with the models that you're using. the resource optimization and identifying

**[06:41]** resource optimization and identifying

**[06:41]** resource optimization and identifying sizing so that you're efficiently using

**[06:44]** sizing so that you're efficiently using

**[06:44]** sizing so that you're efficiently using your hardware appropriately for whatever

**[06:46]** your hardware appropriately for whatever

**[06:46]** your hardware appropriately for whatever model size you're using. That's a big

**[06:48]** model size you're using. That's a big

**[06:48]** model size you're using. That's a big challenge um for enterprises today.

**[06:51]** challenge um for enterprises today.

**[06:51]** challenge um for enterprises today. Making sure they're efficiently using

**[06:52]** Making sure they're efficiently using

**[06:52]** Making sure they're efficiently using their GPU investments. And then actually

**[06:56]** their GPU investments. And then actually

**[06:56]** their GPU investments. And then actually cost estimating is a little bit of a

**[06:58]** cost estimating is a little bit of a

**[06:58]** cost estimating is a little bit of a black magic thing. Like it's really hard


### [07:00 - 08:00]

**[07:00]** black magic thing. Like it's really hard

**[07:00]** black magic thing. Like it's really hard to do that appropriately. um you have to

**[07:03]** to do that appropriately. um you have to

**[07:03]** to do that appropriately. um you have to like backwards mathmap imperence

**[07:05]** like backwards mathmap imperence

**[07:05]** like backwards mathmap imperence performance to tokens and it's a whole

**[07:07]** performance to tokens and it's a whole

**[07:08]** performance to tokens and it's a whole thing. So these are what enterprises are

**[07:10]** thing. So these are what enterprises are

**[07:10]** thing. So these are what enterprises are trying to achieve and it's hard.

**[07:13]** trying to achieve and it's hard.

**[07:13]** trying to achieve and it's hard. Um just a little kind of more examples

**[07:16]** Um just a little kind of more examples

**[07:16]** Um just a little kind of more examples of the challenges. So we have you know

**[07:17]** of the challenges. So we have you know

**[07:18]** of the challenges. So we have you know this is just an example of stable

**[07:19]** this is just an example of stable

**[07:19]** this is just an example of stable diffusion bias. Like I said most of our

**[07:21]** diffusion bias. Like I said most of our

**[07:21]** diffusion bias. Like I said most of our data is euroentric. This is going to be

**[07:24]** data is euroentric. This is going to be

**[07:24]** data is euroentric. This is going to be there. So how do we what tools can we

**[07:26]** there. So how do we what tools can we

**[07:26]** there. So how do we what tools can we use to provide guardrails against this

**[07:28]** use to provide guardrails against this

**[07:28]** use to provide guardrails against this type of behavior?

**[07:30]** type of behavior?

**[07:30]** type of behavior? the glue incident. This was because

**[07:33]** the glue incident. This was because

**[07:33]** the glue incident. This was because there was something on Reddit was like

**[07:35]** there was something on Reddit was like

**[07:36]** there was something on Reddit was like it's like a joke um satire and did this

**[07:39]** it's like a joke um satire and did this

**[07:39]** it's like a joke um satire and did this AI overview tool used that information

**[07:42]** AI overview tool used that information

**[07:42]** AI overview tool used that information and didn't have the right mitigation

**[07:43]** and didn't have the right mitigation

**[07:43]** and didn't have the right mitigation techniques in place to identify that

**[07:46]** techniques in place to identify that

**[07:46]** techniques in place to identify that satire. So then it came out in that um

**[07:48]** satire. So then it came out in that um

**[07:48]** satire. So then it came out in that um AI overview uh suggestion

**[07:53]** AI overview uh suggestion

**[07:53]** AI overview uh suggestion and then we have this um like MAD

**[07:56]** and then we have this um like MAD

**[07:56]** and then we have this um like MAD situation where a lot of the we're

**[07:57]** situation where a lot of the we're

**[07:57]** situation where a lot of the we're getting into a lot of synthetic data on

**[07:59]** getting into a lot of synthetic data on

**[07:59]** getting into a lot of synthetic data on the internet and each generation of


### [08:00 - 09:00]

**[08:03]** the internet and each generation of

**[08:03]** the internet and each generation of these AI models that come out are

**[08:05]** these AI models that come out are

**[08:05]** these AI models that come out are consuming more and more AI generated

**[08:07]** consuming more and more AI generated

**[08:07]** consuming more and more AI generated data which over time is going to get you

**[08:11]** data which over time is going to get you

**[08:11]** data which over time is going to get you oh there's music happening um further

**[08:12]** oh there's music happening um further

**[08:12]** oh there's music happening um further away from that original human anchored

**[08:15]** away from that original human anchored

**[08:15]** away from that original human anchored data. So this is going to lead to a loss

**[08:17]** data. So this is going to lead to a loss

**[08:17]** data. So this is going to lead to a loss of output diversity, a loss of pre a

**[08:20]** of output diversity, a loss of pre a

**[08:20]** of output diversity, a loss of pre a loss of precision. This would be an area

**[08:22]** loss of precision. This would be an area

**[08:22]** loss of precision. This would be an area where you would need to use those kind

**[08:24]** where you would need to use those kind

**[08:24]** where you would need to use those kind of accuracy evals to mitigate again and

**[08:27]** of accuracy evals to mitigate again and

**[08:27]** of accuracy evals to mitigate again and identify that this is occurring.

**[08:34]** So just to cover of course Google and

**[08:34]** So just to cover of course Google and the stable diffusion project they have

**[08:37]** the stable diffusion project they have

**[08:37]** the stable diffusion project they have introduced additional evaluation

**[08:39]** introduced additional evaluation

**[08:39]** introduced additional evaluation frameworks and mitigation techniques to

**[08:41]** frameworks and mitigation techniques to

**[08:41]** frameworks and mitigation techniques to address this. um just like anytime we

**[08:44]** address this. um just like anytime we

**[08:44]** address this. um just like anytime we have any story like that right they are

**[08:45]** have any story like that right they are

**[08:45]** have any story like that right they are certainly working to make sure that that

**[08:48]** certainly working to make sure that that

**[08:48]** certainly working to make sure that that does not happen again we don't know with

**[08:50]** does not happen again we don't know with

**[08:50]** does not happen again we don't know with the closed source um AI offerings how

**[08:53]** the closed source um AI offerings how

**[08:53]** the closed source um AI offerings how exactly they're doing that but we can

**[08:54]** exactly they're doing that but we can

**[08:54]** exactly they're doing that but we can speculate you know the AI overview

**[08:57]** speculate you know the AI overview

**[08:57]** speculate you know the AI overview technology maybe introduced more rag


### [09:00 - 10:00]

**[09:00]** technology maybe introduced more rag

**[09:00]** technology maybe introduced more rag mitigations to where it helps to

**[09:02]** mitigations to where it helps to

**[09:02]** mitigations to where it helps to identify that that was satire or

**[09:04]** identify that that was satire or

**[09:04]** identify that that was satire or whatever the case is um it has more

**[09:07]** whatever the case is um it has more

**[09:07]** whatever the case is um it has more safeguarding triggers um the stable

**[09:10]** safeguarding triggers um the stable

**[09:10]** safeguarding triggers um the stable diffusion model likely introduced is

**[09:11]** diffusion model likely introduced is

**[09:11]** diffusion model likely introduced is some level of bias mitigation guard

**[09:13]** some level of bias mitigation guard

**[09:13]** some level of bias mitigation guard rails. So we need so of course that

**[09:17]** rails. So we need so of course that

**[09:17]** rails. So we need so of course that they've been working to fix this but

**[09:19]** they've been working to fix this but

**[09:19]** they've been working to fix this but ideally we don't run into this and we

**[09:21]** ideally we don't run into this and we

**[09:21]** ideally we don't run into this and we prevent it ahead of time before a model

**[09:23]** prevent it ahead of time before a model

**[09:23]** prevent it ahead of time before a model release or before an application

**[09:25]** release or before an application

**[09:25]** release or before an application release.

**[09:26]** release.

**[09:26]** release. So how do we prevent these kinds of

**[09:28]** So how do we prevent these kinds of

**[09:28]** So how do we prevent these kinds of issues at scale in production

**[09:30]** issues at scale in production

**[09:30]** issues at scale in production environments? I want to just look at a

**[09:33]** environments? I want to just look at a

**[09:33]** environments? I want to just look at a couple of definitions because sometimes

**[09:35]** couple of definitions because sometimes

**[09:35]** couple of definitions because sometimes evaluation and benchmarking are terms

**[09:37]** evaluation and benchmarking are terms

**[09:37]** evaluation and benchmarking are terms used um kind of they kind of conflate a

**[09:40]** used um kind of they kind of conflate a

**[09:40]** used um kind of they kind of conflate a little bit and people kind of use them

**[09:41]** little bit and people kind of use them

**[09:41]** little bit and people kind of use them for whatever they want. So benchmarking

**[09:44]** for whatever they want. So benchmarking

**[09:44]** for whatever they want. So benchmarking is just a subcategory of evaluation.

**[09:47]** is just a subcategory of evaluation.

**[09:47]** is just a subcategory of evaluation. Evaluation is a comprehensive process to

**[09:50]** Evaluation is a comprehensive process to

**[09:50]** Evaluation is a comprehensive process to assess a model end to end and it could

**[09:52]** assess a model end to end and it could

**[09:52]** assess a model end to end and it could include a lot of different kinds of

**[09:54]** include a lot of different kinds of

**[09:54]** include a lot of different kinds of evaluations about a lot of different

**[09:56]** evaluations about a lot of different

**[09:56]** evaluations about a lot of different components. Benchmarking is very

**[09:58]** components. Benchmarking is very

**[09:58]** components. Benchmarking is very specifically controlled specific data


### [10:00 - 11:00]

**[10:01]** specifically controlled specific data

**[10:01]** specifically controlled specific data sets and specific tasks typically used

**[10:03]** sets and specific tasks typically used

**[10:03]** sets and specific tasks typically used to compare models against one another.

**[10:06]** to compare models against one another.

**[10:06]** to compare models against one another. So this would be like a latency score

**[10:09]** So this would be like a latency score

**[10:09]** So this would be like a latency score that compares different hardware setups

**[10:11]** that compares different hardware setups

**[10:12]** that compares different hardware setups and different models or like the MMLU

**[10:14]** and different models or like the MMLU

**[10:14]** and different models or like the MMLU benchmark scoring things like that.

**[10:17]** benchmark scoring things like that.

**[10:17]** benchmark scoring things like that. We'll look at both custom evals that

**[10:19]** We'll look at both custom evals that

**[10:20]** We'll look at both custom evals that aren't benchmarking and also some

**[10:21]** aren't benchmarking and also some

**[10:21]** aren't benchmarking and also some benchmarks in their hands-on.

**[10:24]** benchmarks in their hands-on.

**[10:24]** benchmarks in their hands-on. These are just some examples of what is

**[10:27]** These are just some examples of what is

**[10:27]** These are just some examples of what is typically considered a model evaluation

**[10:30]** typically considered a model evaluation

**[10:30]** typically considered a model evaluation versus a benchmarking specific test just

**[10:33]** versus a benchmarking specific test just

**[10:33]** versus a benchmarking specific test just to kind of get a little bit of a sense.

**[10:35]** to kind of get a little bit of a sense.

**[10:35]** to kind of get a little bit of a sense. Um, but again like there's so many types

**[10:37]** Um, but again like there's so many types

**[10:37]** Um, but again like there's so many types of evaluations, so many tools, you can

**[10:40]** of evaluations, so many tools, you can

**[10:40]** of evaluations, so many tools, you can customize it in so many different ways,

**[10:42]** customize it in so many different ways,

**[10:42]** customize it in so many different ways, but this kind of helps hopefully a

**[10:44]** but this kind of helps hopefully a

**[10:44]** but this kind of helps hopefully a little bit with the definitions.

**[10:47]** little bit with the definitions.

**[10:47]** little bit with the definitions. So hopefully kind of seeing all these

**[10:50]** So hopefully kind of seeing all these

**[10:50]** So hopefully kind of seeing all these challenges with Genai. We understand

**[10:52]** challenges with Genai. We understand

**[10:52]** challenges with Genai. We understand that this is a critical process. Um you

**[10:55]** that this is a critical process. Um you

**[10:55]** that this is a critical process. Um you need to manage risk for customers like

**[10:58]** need to manage risk for customers like

**[10:58]** need to manage risk for customers like there's less of a concern right when I'm

**[10:59]** there's less of a concern right when I'm

**[10:59]** there's less of a concern right when I'm tinkering on my laptop whatever if you


### [11:00 - 12:00]

**[11:01]** tinkering on my laptop whatever if you

**[11:01]** tinkering on my laptop whatever if you know I see something weird who cares.

**[11:03]** know I see something weird who cares.

**[11:03]** know I see something weird who cares. But when we're talking about a

**[11:04]** But when we're talking about a

**[11:04]** But when we're talking about a production level environment we're

**[11:06]** production level environment we're

**[11:06]** production level environment we're serving thousands whatever customers we

**[11:08]** serving thousands whatever customers we

**[11:08]** serving thousands whatever customers we need to think about these things

**[11:09]** need to think about these things

**[11:09]** need to think about these things obviously more in these types of

**[11:11]** obviously more in these types of

**[11:11]** obviously more in these types of scenarios. the credibility of the

**[11:13]** scenarios. the credibility of the

**[11:13]** scenarios. the credibility of the company. When those stories come out,

**[11:15]** company. When those stories come out,

**[11:15]** company. When those stories come out, that takes a hit for a good chunk of

**[11:17]** that takes a hit for a good chunk of

**[11:17]** that takes a hit for a good chunk of time. Um, and you obviously also need to

**[11:20]** time. Um, and you obviously also need to

**[11:20]** time. Um, and you obviously also need to continuously improve your evaluation

**[11:22]** continuously improve your evaluation

**[11:22]** continuously improve your evaluation frameworks as well because you're not

**[11:24]** frameworks as well because you're not

**[11:24]** frameworks as well because you're not going to catch everything. You need that

**[11:26]** going to catch everything. You need that

**[11:26]** going to catch everything. You need that CI process to make sure you are

**[11:28]** CI process to make sure you are

**[11:28]** CI process to make sure you are continuously improving your evaluations

**[11:31]** continuously improving your evaluations

**[11:31]** continuously improving your evaluations and benchmark setups.

**[11:34]** and benchmark setups.

**[11:34]** and benchmark setups. It's also going to very much depend on

**[11:36]** It's also going to very much depend on

**[11:36]** It's also going to very much depend on the type of system that you have, what

**[11:38]** the type of system that you have, what

**[11:38]** the type of system that you have, what you set up. So again, it's very much

**[11:40]** you set up. So again, it's very much

**[11:40]** you set up. So again, it's very much there's tons of tools. This could look a

**[11:42]** there's tons of tools. This could look a

**[11:42]** there's tons of tools. This could look a lot of different ways. We'll get a sense

**[11:43]** lot of different ways. We'll get a sense

**[11:44]** lot of different ways. We'll get a sense of it today. If you have a Rag setup,

**[11:46]** of it today. If you have a Rag setup,

**[11:46]** of it today. If you have a Rag setup, you're going to be maybe focused on a

**[11:48]** you're going to be maybe focused on a

**[11:48]** you're going to be maybe focused on a the Ragas um benchmark or evaluation

**[11:51]** the Ragas um benchmark or evaluation

**[11:51]** the Ragas um benchmark or evaluation tool, agents, you need to look at

**[11:54]** tool, agents, you need to look at

**[11:54]** tool, agents, you need to look at function tool calling capabilities, etc.

**[11:58]** function tool calling capabilities, etc.

**[11:58]** function tool calling capabilities, etc. you can kind of get a sense there's


### [12:00 - 13:00]

**[12:00]** you can kind of get a sense there's

**[12:00]** you can kind of get a sense there's going to be specific metrics that you

**[12:01]** going to be specific metrics that you

**[12:01]** going to be specific metrics that you need to set up and look for depending on

**[12:04]** need to set up and look for depending on

**[12:04]** need to set up and look for depending on the system that you have which requires

**[12:07]** the system that you have which requires

**[12:07]** the system that you have which requires a lot of planning in advance and kind of

**[12:09]** a lot of planning in advance and kind of

**[12:09]** a lot of planning in advance and kind of architecture scoping.

**[12:12]** architecture scoping.

**[12:12]** architecture scoping. I'll give an example of a rag use case

**[12:15]** I'll give an example of a rag use case

**[12:16]** I'll give an example of a rag use case and also it's incremental too because

**[12:18]** and also it's incremental too because

**[12:18]** and also it's incremental too because you could and I'll I'll talk about this

**[12:20]** you could and I'll I'll talk about this

**[12:20]** you could and I'll I'll talk about this a bit like you could literally evaluate

**[12:22]** a bit like you could literally evaluate

**[12:22]** a bit like you could literally evaluate every single part of things but that's

**[12:25]** every single part of things but that's

**[12:25]** every single part of things but that's going to be um time and resource

**[12:28]** going to be um time and resource

**[12:28]** going to be um time and resource extensive to set up immediately. So you

**[12:29]** extensive to set up immediately. So you

**[12:30]** extensive to set up immediately. So you likely want to take an incremental

**[12:31]** likely want to take an incremental

**[12:31]** likely want to take an incremental approach with these types of setups. So

**[12:33]** approach with these types of setups. So

**[12:33]** approach with these types of setups. So you might start out with okay I'm just

**[12:35]** you might start out with okay I'm just

**[12:35]** you might start out with okay I'm just going to evaluate the chunk retrieval my

**[12:39]** going to evaluate the chunk retrieval my

**[12:39]** going to evaluate the chunk retrieval my retrieval application in a rag system. I

**[12:41]** retrieval application in a rag system. I

**[12:41]** retrieval application in a rag system. I want to set up some kind of evaluation

**[12:43]** want to set up some kind of evaluation

**[12:43]** want to set up some kind of evaluation test there. I might just want to set up

**[12:45]** test there. I might just want to set up

**[12:45]** test there. I might just want to set up a latency throughput um benchmark test

**[12:48]** a latency throughput um benchmark test

**[12:48]** a latency throughput um benchmark test for my LLM output. You can start with

**[12:51]** for my LLM output. You can start with

**[12:51]** for my LLM output. You can start with those kind of incremental approaches for

**[12:53]** those kind of incremental approaches for

**[12:53]** those kind of incremental approaches for specific components and then from there

**[12:56]** specific components and then from there

**[12:56]** specific components and then from there based on priority levels as well branch

**[12:59]** based on priority levels as well branch

**[12:59]** based on priority levels as well branch out into a full system eval that covers


### [13:00 - 14:00]

**[13:01]** out into a full system eval that covers

**[13:01]** out into a full system eval that covers all the components the integration layer

**[13:04]** all the components the integration layer

**[13:04]** all the components the integration layer of how the components work together the

**[13:06]** of how the components work together the

**[13:06]** of how the components work together the UI endto-end experience and kind of have

**[13:09]** UI endto-end experience and kind of have

**[13:09]** UI endto-end experience and kind of have a software engineering kind of test

**[13:11]** a software engineering kind of test

**[13:11]** a software engineering kind of test period approach to this where you have

**[13:14]** period approach to this where you have

**[13:14]** period approach to this where you have that unit test layer kind of approach at

**[13:16]** that unit test layer kind of approach at

**[13:16]** that unit test layer kind of approach at the bottom um integration layer in the

**[13:19]** the bottom um integration layer in the

**[13:19]** the bottom um integration layer in the middle and that UI end to end at the top

**[13:22]** middle and that UI end to end at the top

**[13:22]** middle and that UI end to end at the top and you can take that layer by layer as

**[13:25]** and you can take that layer by layer as

**[13:25]** and you can take that layer by layer as you're building this evaluation

**[13:26]** you're building this evaluation

**[13:26]** you're building this evaluation framework for your systems.

**[13:33]** So there we created this or we there is

**[13:33]** So there we created this or we there is this pyramid also for model evaluation

**[13:36]** this pyramid also for model evaluation

**[13:36]** this pyramid also for model evaluation that represents the same kind of setup

**[13:38]** that represents the same kind of setup

**[13:38]** that represents the same kind of setup for um that that software engineering

**[13:41]** for um that that software engineering

**[13:41]** for um that that software engineering pyramid um represents as well. So the

**[13:43]** pyramid um represents as well. So the

**[13:43]** pyramid um represents as well. So the base layer and uh very base layer is the

**[13:46]** base layer and uh very base layer is the

**[13:46]** base layer and uh very base layer is the system performance because like I said

**[13:48]** system performance because like I said

**[13:48]** system performance because like I said no matter how good your model is if you

**[13:50]** no matter how good your model is if you

**[13:50]** no matter how good your model is if you don't have fast throughput you aren't

**[13:52]** don't have fast throughput you aren't

**[13:52]** don't have fast throughput you aren't able to handle concurrent users you're

**[13:54]** able to handle concurrent users you're

**[13:54]** able to handle concurrent users you're going to be in a bit of a pickle GPU

**[13:56]** going to be in a bit of a pickle GPU

**[13:56]** going to be in a bit of a pickle GPU utilization etc. you need to make sure

**[13:58]** utilization etc. you need to make sure

**[13:58]** utilization etc. you need to make sure kind of the basics are handled uh the as


### [14:00 - 15:00]

**[14:01]** kind of the basics are handled uh the as

**[14:01]** kind of the basics are handled uh the as the main kind of event. Um and we'll

**[14:04]** the main kind of event. Um and we'll

**[14:04]** the main kind of event. Um and we'll talk about that'll be the first hands-on

**[14:05]** talk about that'll be the first hands-on

**[14:05]** talk about that'll be the first hands-on activity is is evaluating the system

**[14:07]** activity is is evaluating the system

**[14:07]** activity is is evaluating the system performance. Formatting might be making

**[14:11]** performance. Formatting might be making

**[14:11]** performance. Formatting might be making sure it's um religiously giving you JSON

**[14:14]** sure it's um religiously giving you JSON

**[14:14]** sure it's um religiously giving you JSON output that you need for your

**[14:15]** output that you need for your

**[14:15]** output that you need for your application. Something like that. The

**[14:17]** application. Something like that. The

**[14:17]** application. Something like that. The factual accuracy which we'll also talk

**[14:19]** factual accuracy which we'll also talk

**[14:19]** factual accuracy which we'll also talk about um in one of our hands-on that

**[14:22]** about um in one of our hands-on that

**[14:22]** about um in one of our hands-on that would be like the MMLU benchmark. So

**[14:24]** would be like the MMLU benchmark. So

**[14:24]** would be like the MMLU benchmark. So evaluating that it's performing well on

**[14:27]** evaluating that it's performing well on

**[14:27]** evaluating that it's performing well on various subjects kind of standard large

**[14:29]** various subjects kind of standard large

**[14:29]** various subjects kind of standard large language model accuracy as well as if

**[14:31]** language model accuracy as well as if

**[14:32]** language model accuracy as well as if you've fine-tuned a model potentially

**[14:34]** you've fine-tuned a model potentially

**[14:34]** you've fine-tuned a model potentially making sure that it's accurate based on

**[14:36]** making sure that it's accurate based on

**[14:36]** making sure that it's accurate based on the information that you fine-tuned that

**[14:38]** the information that you fine-tuned that

**[14:38]** the information that you fine-tuned that model on and you kind of go up from

**[14:40]** model on and you kind of go up from

**[14:40]** model on and you kind of go up from there into you know safety bias there

**[14:43]** there into you know safety bias there

**[14:43]** there into you know safety bias there might be specific custom evaluations

**[14:45]** might be specific custom evaluations

**[14:45]** might be specific custom evaluations that are very specific to your

**[14:46]** that are very specific to your

**[14:46]** that are very specific to your application. So gives you kind of a

**[14:49]** application. So gives you kind of a

**[14:49]** application. So gives you kind of a sense of the tiered approach that can be

**[14:51]** sense of the tiered approach that can be

**[14:51]** sense of the tiered approach that can be taken here.

**[14:53]** taken here.

**[14:53]** taken here. So, we're going to talk first system

**[14:55]** So, we're going to talk first system

**[14:55]** So, we're going to talk first system performance and we're going to have our

**[14:56]** performance and we're going to have our

**[14:56]** performance and we're going to have our first hands-on around this. We're going

**[14:59]** first hands-on around this. We're going

**[14:59]** first hands-on around this. We're going to be looking at guide LLM, which is


### [15:00 - 16:00]

**[15:01]** to be looking at guide LLM, which is

**[15:01]** to be looking at guide LLM, which is kind of a new project that's associated

**[15:03]** kind of a new project that's associated

**[15:03]** kind of a new project that's associated with the VLM inference runtime project.

**[15:06]** with the VLM inference runtime project.

**[15:06]** with the VLM inference runtime project. Um, we're going to use that for system

**[15:09]** Um, we're going to use that for system

**[15:09]** Um, we're going to use that for system performance benchmarks like latency

**[15:11]** performance benchmarks like latency

**[15:11]** performance benchmarks like latency throughput and you'll get a little bit

**[15:12]** throughput and you'll get a little bit

**[15:12]** throughput and you'll get a little bit of hands-on there. The general user flow

**[15:15]** of hands-on there. The general user flow

**[15:15]** of hands-on there. The general user flow there is like you you know you select

**[15:17]** there is like you you know you select

**[15:17]** there is like you you know you select your model you select your particular

**[15:19]** your model you select your particular

**[15:19]** your model you select your particular data set that you want to use to test

**[15:21]** data set that you want to use to test

**[15:21]** data set that you want to use to test throughput and to test inter token

**[15:24]** throughput and to test inter token

**[15:24]** throughput and to test inter token latency time to first token those types

**[15:26]** latency time to first token those types

**[15:26]** latency time to first token those types of metrics and then guide LLM allows

**[15:29]** of metrics and then guide LLM allows

**[15:30]** of metrics and then guide LLM allows gives you a nice kind of um internal UI

**[15:33]** gives you a nice kind of um internal UI

**[15:33]** gives you a nice kind of um internal UI to visualize the results of that. Uh and

**[15:37]** to visualize the results of that. Uh and

**[15:37]** to visualize the results of that. Uh and then once you get kind of the results

**[15:39]** then once you get kind of the results

**[15:39]** then once you get kind of the results that you want based on your use case

**[15:41]** that you want based on your use case

**[15:41]** that you want based on your use case again then you're ready to deploy.

**[15:45]** again then you're ready to deploy.

**[15:45]** again then you're ready to deploy. We you'll see this in the hands-on as

**[15:47]** We you'll see this in the hands-on as

**[15:47]** We you'll see this in the hands-on as well but you want to test based on the

**[15:49]** well but you want to test based on the

**[15:49]** well but you want to test based on the use case and the p one of the primary

**[15:51]** use case and the p one of the primary

**[15:51]** use case and the p one of the primary ways you test via guide LLM is adjusting

**[15:54]** ways you test via guide LLM is adjusting

**[15:54]** ways you test via guide LLM is adjusting the input and output tokens. So, if you

**[15:56]** the input and output tokens. So, if you

**[15:56]** the input and output tokens. So, if you have a chatbot use case, a rag use case,

**[15:59]** have a chatbot use case, a rag use case,

**[15:59]** have a chatbot use case, a rag use case, you can adjust the um input and output


### [16:00 - 17:00]

**[16:01]** you can adjust the um input and output

**[16:01]** you can adjust the um input and output token levels based on your use case. And

**[16:03]** token levels based on your use case. And

**[16:03]** token levels based on your use case. And you'll see that in the hands-on and have

**[16:04]** you'll see that in the hands-on and have

**[16:04]** you'll see that in the hands-on and have an opportunity to kind of play around

**[16:06]** an opportunity to kind of play around

**[16:06]** an opportunity to kind of play around with that depending on what you're most

**[16:07]** with that depending on what you're most

**[16:07]** with that depending on what you're most interested in.

**[16:10]** interested in.

**[16:10]** interested in. So, we're going to start with the

**[16:11]** So, we're going to start with the

**[16:11]** So, we're going to start with the hands-on.

**[16:13]** hands-on.

**[16:13]** hands-on. That is the link that red.htvals

**[16:18]** That is the link that red.htvals

**[16:18]** That is the link that red.htvals is the link to the workshop.

**[16:20]** is the link to the workshop.

**[16:20]** is the link to the workshop. You will be signing in with your email.

**[16:23]** You will be signing in with your email.

**[16:23]** You will be signing in with your email. I have no marketing game. It just

**[16:25]** I have no marketing game. It just

**[16:25]** I have no marketing game. It just requires you to do that. So, I'm not

**[16:27]** requires you to do that. So, I'm not

**[16:27]** requires you to do that. So, I'm not going to haunt you after this. Um,

**[16:29]** going to haunt you after this. Um,

**[16:29]** going to haunt you after this. Um, you'll put in your email and that is the

**[16:31]** you'll put in your email and that is the

**[16:31]** you'll put in your email and that is the password.

**[16:34]** password.

**[16:34]** password. And

**[16:36]** And

**[16:36]** And me, hold on. I just want to show you.

**[16:38]** me, hold on. I just want to show you.

**[16:38]** me, hold on. I just want to show you. Well, I don't want to take up one of the

**[16:39]** Well, I don't want to take up one of the

**[16:39]** Well, I don't want to take up one of the systems. Um, otherwise I would show you,

**[16:41]** systems. Um, otherwise I would show you,

**[16:42]** systems. Um, otherwise I would show you, but you're going to get instruct once

**[16:43]** but you're going to get instruct once

**[16:44]** but you're going to get instruct once you are in the workshop. You're going to

**[16:45]** you are in the workshop. You're going to

**[16:45]** you are in the workshop. You're going to get your instructions on the lefthand

**[16:47]** get your instructions on the lefthand

**[16:47]** get your instructions on the lefthand side and you're going to have two

**[16:48]** side and you're going to have two

**[16:48]** side and you're going to have two terminals avail two terminal sessions

**[16:50]** terminals avail two terminal sessions

**[16:50]** terminals avail two terminal sessions available to you on the right hand side

**[16:52]** available to you on the right hand side

**[16:52]** available to you on the right hand side to the same system. It's a rail system.

**[16:55]** to the same system. It's a rail system.

**[16:55]** to the same system. It's a rail system. Um the instructions will overview what

**[16:57]** Um the instructions will overview what

**[16:57]** Um the instructions will overview what the system includes a little bit for you

**[16:59]** the system includes a little bit for you

**[16:59]** the system includes a little bit for you so you get a sense. Um they each have an


### [17:00 - 18:00]

**[17:01]** so you get a sense. Um they each have an

**[17:01]** so you get a sense. Um they each have an L4 GPU as an example. Um anything else I

**[17:05]** L4 GPU as an example. Um anything else I

**[17:06]** L4 GPU as an example. Um anything else I want to call out before we get started.

**[17:08]** want to call out before we get started.

**[17:08]** want to call out before we get started. That'll be primarily what you use. It

**[17:10]** That'll be primarily what you use. It

**[17:10]** That'll be primarily what you use. It has T-Mox enabled if you like to use

**[17:12]** has T-Mox enabled if you like to use

**[17:12]** has T-Mox enabled if you like to use that to open up different things and

**[17:15]** that to open up different things and

**[17:15]** that to open up different things and gives you some flexibility. We have

**[17:18]** gives you some flexibility. We have

**[17:18]** gives you some flexibility. We have three different activities. I'm going to

**[17:20]** three different activities. I'm going to

**[17:20]** three different activities. I'm going to pause after each activity so we can have

**[17:23]** pause after each activity so we can have

**[17:23]** pause after each activity so we can have a little bit of a discussion in between.

**[17:26]** a little bit of a discussion in between.

**[17:26]** a little bit of a discussion in between. Um, we'll kind of get this my first time

**[17:29]** Um, we'll kind of get this my first time

**[17:29]** Um, we'll kind of get this my first time running this particular uh activity. So,

**[17:31]** running this particular uh activity. So,

**[17:31]** running this particular uh activity. So, we'll gauge kind of the time it takes,

**[17:33]** we'll gauge kind of the time it takes,

**[17:33]** we'll gauge kind of the time it takes, but I'm going to give it about 15 20

**[17:35]** but I'm going to give it about 15 20

**[17:35]** but I'm going to give it about 15 20 minutes for this first one.

**[17:38]** minutes for this first one.

**[17:38]** minutes for this first one. Okay. So, I'm also pulling up a system

**[17:41]** Okay. So, I'm also pulling up a system

**[17:41]** Okay. So, I'm also pulling up a system and I'm just going to like walk through

**[17:42]** and I'm just going to like walk through

**[17:42]** and I'm just going to like walk through some of the stuff. The initial page is

**[17:44]** some of the stuff. The initial page is

**[17:44]** some of the stuff. The initial page is just going to give you if of course if

**[17:46]** just going to give you if of course if

**[17:46]** just going to give you if of course if it loads Jesus the internet. Um the

**[17:49]** it loads Jesus the internet. Um the

**[17:49]** it loads Jesus the internet. Um the initial page is just going to give you a

**[17:50]** initial page is just going to give you a

**[17:50]** initial page is just going to give you a little bit of background and preparing

**[17:52]** little bit of background and preparing

**[17:52]** little bit of background and preparing your system instructions and then my

**[17:54]** your system instructions and then my

**[17:54]** your system instructions and then my terminals are on this second tab

**[17:57]** terminals are on this second tab

**[17:57]** terminals are on this second tab and everything is going to be glacial


### [18:00 - 19:00]

**[18:00]** and everything is going to be glacial

**[18:00]** and everything is going to be glacial pace. Um

**[18:02]** pace. Um

**[18:02]** pace. Um so the first thing I have to do these

**[18:04]** so the first thing I have to do these

**[18:04]** so the first thing I have to do these systems don't have the container toolkit

**[18:06]** systems don't have the container toolkit

**[18:06]** systems don't have the container toolkit installed so I just got to do that some

**[18:08]** installed so I just got to do that some

**[18:08]** installed so I just got to do that some uh system logistics because I'm going to

**[18:11]** uh system logistics because I'm going to

**[18:11]** uh system logistics because I'm going to be running VLM inference runtime in a

**[18:13]** be running VLM inference runtime in a

**[18:13]** be running VLM inference runtime in a container and I need that to work. So

**[18:16]** container and I need that to work. So

**[18:16]** container and I need that to work. So that's what that's doing. And then I'm

**[18:19]** that's what that's doing. And then I'm

**[18:19]** that's what that's doing. And then I'm gonna deploy a model with VLM. I So

**[18:24]** gonna deploy a model with VLM. I So

**[18:24]** gonna deploy a model with VLM. I So you're gonna have to grab a hugging face

**[18:25]** you're gonna have to grab a hugging face

**[18:25]** you're gonna have to grab a hugging face token. Probably have gotten there by

**[18:27]** token. Probably have gotten there by

**[18:27]** token. Probably have gotten there by now. Probably most of us have a hugging

**[18:28]** now. Probably most of us have a hugging

**[18:28]** now. Probably most of us have a hugging face token, but just disclaimer there.

**[18:30]** face token, but just disclaimer there.

**[18:30]** face token, but just disclaimer there. So incognito window if you're hitting

**[18:32]** So incognito window if you're hitting

**[18:32]** So incognito window if you're hitting the hugging face rate limit to grab a

**[18:35]** the hugging face rate limit to grab a

**[18:35]** the hugging face rate limit to grab a new token.

**[18:37]** new token.

**[18:38]** new token. So VLM you can also install locally like

**[18:41]** So VLM you can also install locally like

**[18:41]** So VLM you can also install locally like if you have a Mac or whatever um Linux

**[18:43]** if you have a Mac or whatever um Linux

**[18:43]** if you have a Mac or whatever um Linux machine, but we're deploying it as a

**[18:45]** machine, but we're deploying it as a

**[18:45]** machine, but we're deploying it as a container here.

**[18:48]** container here.

**[18:48]** container here. So I'm going to get that deploy and I'm

**[18:49]** So I'm going to get that deploy and I'm

**[18:49]** So I'm going to get that deploy and I'm um you can see the VLM serve command at

**[18:52]** um you can see the VLM serve command at

**[18:52]** um you can see the VLM serve command at the end. So that's just the VLM CLI tool

**[18:54]** the end. So that's just the VLM CLI tool

**[18:54]** the end. So that's just the VLM CLI tool and I'm using an IBM granite model

**[18:56]** and I'm using an IBM granite model

**[18:56]** and I'm using an IBM granite model because you know Red Hat IBM

**[18:59]** because you know Red Hat IBM

**[18:59]** because you know Red Hat IBM um so we'll be working with that for a


### [19:00 - 20:00]

**[19:02]** um so we'll be working with that for a

**[19:02]** um so we'll be working with that for a chunk of the activity and it takes a bit

**[19:05]** chunk of the activity and it takes a bit

**[19:05]** chunk of the activity and it takes a bit for VLM to load the model. So you're

**[19:07]** for VLM to load the model. So you're

**[19:08]** for VLM to load the model. So you're going to be waiting for info the words

**[19:10]** going to be waiting for info the words

**[19:10]** going to be waiting for info the words info like four times in green and then

**[19:13]** info like four times in green and then

**[19:13]** info like four times in green and then it's deployed.

**[19:15]** it's deployed.

**[19:16]** it's deployed. What's nice about VLM is that it is um

**[19:18]** What's nice about VLM is that it is um

**[19:18]** What's nice about VLM is that it is um it's compatible with the safe tensor

**[19:20]** it's compatible with the safe tensor

**[19:20]** it's compatible with the safe tensor formats. So I has anybody used TRT to

**[19:23]** formats. So I has anybody used TRT to

**[19:23]** formats. So I has anybody used TRT to load up a model. Okay. Anyway, it's

**[19:26]** load up a model. Okay. Anyway, it's

**[19:26]** load up a model. Okay. Anyway, it's crazy um because it requires you to also

**[19:29]** crazy um because it requires you to also

**[19:29]** crazy um because it requires you to also convert the model formats initially. Um

**[19:31]** convert the model formats initially. Um

**[19:31]** convert the model formats initially. Um so there's less kind of configuration

**[19:33]** so there's less kind of configuration

**[19:33]** so there's less kind of configuration steps with VLM. Takes up less space too.

**[19:37]** steps with VLM. Takes up less space too.

**[19:37]** steps with VLM. Takes up less space too. So when you do these kinds of system and

**[19:39]** So when you do these kinds of system and

**[19:39]** So when you do these kinds of system and performance um benchmarks, you can make

**[19:42]** performance um benchmarks, you can make

**[19:42]** performance um benchmarks, you can make a lot of adjustments like the um the

**[19:44]** a lot of adjustments like the um the

**[19:44]** a lot of adjustments like the um the input and output tokens that I mentioned

**[19:47]** input and output tokens that I mentioned

**[19:47]** input and output tokens that I mentioned um for the guide LLM configurations, but

**[19:49]** um for the guide LLM configurations, but

**[19:49]** um for the guide LLM configurations, but there's a lot of also configuration

**[19:51]** there's a lot of also configuration

**[19:51]** there's a lot of also configuration opportunities for the inference runtime

**[19:53]** opportunities for the inference runtime

**[19:53]** opportunities for the inference runtime itself um depending on what you're

**[19:56]** itself um depending on what you're

**[19:56]** itself um depending on what you're trying to do. sometimes will reduce the

**[19:58]** trying to do. sometimes will reduce the

**[19:58]** trying to do. sometimes will reduce the max um the context window of the model


### [20:00 - 21:00]

**[20:02]** max um the context window of the model

**[20:02]** max um the context window of the model so it runs more quickly because it's if

**[20:03]** so it runs more quickly because it's if

**[20:03]** so it runs more quickly because it's if it's a big context window it's going to

**[20:05]** it's a big context window it's going to

**[20:05]** it's a big context window it's going to be pretty beefy. There's a lot of knobs

**[20:07]** be pretty beefy. There's a lot of knobs

**[20:07]** be pretty beefy. There's a lot of knobs you can use for VLM. We're not really

**[20:09]** you can use for VLM. We're not really

**[20:09]** you can use for VLM. We're not really going to touch that um this particular

**[20:11]** going to touch that um this particular

**[20:11]** going to touch that um this particular time but just so you're aware. So I have

**[20:13]** time but just so you're aware. So I have

**[20:13]** time but just so you're aware. So I have my my three in green infos. So that

**[20:16]** my my three in green infos. So that

**[20:16]** my my three in green infos. So that means it's working and the model is

**[20:18]** means it's working and the model is

**[20:18]** means it's working and the model is successfully deployed. So I'm going to

**[20:23]** successfully deployed. So I'm going to

**[20:23]** successfully deployed. So I'm going to um get into my virtual environment which

**[20:27]** um get into my virtual environment which

**[20:27]** um get into my virtual environment which is already in place and then I already

**[20:29]** is already in place and then I already

**[20:29]** is already in place and then I already have guide LLM installed but I'm going

**[20:32]** have guide LLM installed but I'm going

**[20:32]** have guide LLM installed but I'm going to pip install guide LM and these are

**[20:34]** to pip install guide LM and these are

**[20:34]** to pip install guide LM and these are copy buttons by the way so you can just

**[20:36]** copy buttons by the way so you can just

**[20:36]** copy buttons by the way so you can just easily copy paste things over.

**[20:39]** easily copy paste things over.

**[20:39]** easily copy paste things over. So once I have that up then this command

**[20:42]** So once I have that up then this command

**[20:42]** So once I have that up then this command is set up to just work with the um model

**[20:45]** is set up to just work with the um model

**[20:45]** is set up to just work with the um model deployed by VLM and that I'm just

**[20:47]** deployed by VLM and that I'm just

**[20:47]** deployed by VLM and that I'm just keeping up here in the top terminal. can

**[20:49]** keeping up here in the top terminal. can

**[20:49]** keeping up here in the top terminal. can run this in the background but I'm just

**[20:51]** run this in the background but I'm just

**[20:51]** run this in the background but I'm just not doing that and this is so I have my

**[20:55]** not doing that and this is so I have my

**[20:55]** not doing that and this is so I have my target um the rate type is a sweep of uh

**[20:59]** target um the rate type is a sweep of uh

**[20:59]** target um the rate type is a sweep of uh various benchmarks like inter token


### [21:00 - 22:00]

**[21:01]** various benchmarks like inter token

**[21:01]** various benchmarks like inter token latency there's various types of

**[21:04]** latency there's various types of

**[21:04]** latency there's various types of benchmarks that it'll run that you'll

**[21:05]** benchmarks that it'll run that you'll

**[21:05]** benchmarks that it'll run that you'll see in the output um but these are all

**[21:08]** see in the output um but these are all

**[21:08]** see in the output um but these are all things that can be adjusted you can run

**[21:09]** things that can be adjusted you can run

**[21:09]** things that can be adjusted you can run one particular benchmark at a time for

**[21:11]** one particular benchmark at a time for

**[21:11]** one particular benchmark at a time for instance you can take a look at I think

**[21:13]** instance you can take a look at I think

**[21:13]** instance you can take a look at I think it's uh guide lm-help typical type of

**[21:16]** it's uh guide lm-help typical type of

**[21:16]** it's uh guide lm-help typical type of commands you can kind of see what the

**[21:18]** commands you can kind of see what the

**[21:18]** commands you can kind of see what the where all the knob are. And the

**[21:19]** where all the knob are. And the

**[21:19]** where all the knob are. And the documentation is pretty good, too.

**[21:22]** documentation is pretty good, too.

**[21:22]** documentation is pretty good, too. So, that'll take a couple of minutes to

**[21:25]** So, that'll take a couple of minutes to

**[21:25]** So, that'll take a couple of minutes to run because I have it um set at a rate

**[21:27]** run because I have it um set at a rate

**[21:27]** run because I have it um set at a rate of five to reduce the amount of time

**[21:29]** of five to reduce the amount of time

**[21:29]** of five to reduce the amount of time that it takes to process.

**[21:33]** that it takes to process.

**[21:33]** that it takes to process. >> So, you can kind of get a sense of the

**[21:35]** >> So, you can kind of get a sense of the

**[21:35]** >> So, you can kind of get a sense of the output here once it all processes. And I

**[21:37]** output here once it all processes. And I

**[21:37]** output here once it all processes. And I have explainers on the left hand side of

**[21:40]** have explainers on the left hand side of

**[21:40]** have explainers on the left hand side of kind of how to read some of this. Um the

**[21:43]** kind of how to read some of this. Um the

**[21:43]** kind of how to read some of this. Um the mean performance for each. is we have

**[21:45]** mean performance for each. is we have

**[21:45]** mean performance for each. is we have the the benchmark info on the top and

**[21:48]** the the benchmark info on the top and

**[21:48]** the the benchmark info on the top and then benchmark stats on the bottom. Um

**[21:52]** then benchmark stats on the bottom. Um

**[21:52]** then benchmark stats on the bottom. Um so the for the constant rate the on the

**[21:55]** so the for the constant rate the on the

**[21:55]** so the for the constant rate the on the very left hand side so those are the

**[21:57]** very left hand side so those are the

**[21:57]** very left hand side so those are the number of requests sent to the model per


### [22:00 - 23:00]

**[22:00]** number of requests sent to the model per

**[22:00]** number of requests sent to the model per second at that particular rate. So three

**[22:02]** second at that particular rate. So three

**[22:02]** second at that particular rate. So three the constant at 3.63 6.93 if I did in um

**[22:07]** the constant at 3.63 6.93 if I did in um

**[22:07]** the constant at 3.63 6.93 if I did in um the guide LLM command rate and it was

**[22:10]** the guide LLM command rate and it was

**[22:10]** the guide LLM command rate and it was five. If I did rate 10, you would see

**[22:13]** five. If I did rate 10, you would see

**[22:13]** five. If I did rate 10, you would see more lines of that at at um more

**[22:15]** more lines of that at at um more

**[22:15]** more lines of that at at um more progressive rates

**[22:22]** >> and like whether or not these numbers

**[22:22]** >> and like whether or not these numbers are good also totally depend on your use

**[22:25]** are good also totally depend on your use

**[22:25]** are good also totally depend on your use case as well. And I would be comparing I

**[22:28]** case as well. And I would be comparing I

**[22:28]** case as well. And I would be comparing I would have a better hardware

**[22:29]** would have a better hardware

**[22:29]** would have a better hardware configuration obviously in production as

**[22:31]** configuration obviously in production as

**[22:31]** configuration obviously in production as well because again I'm I'm running an 8

**[22:33]** well because again I'm I'm running an 8

**[22:33]** well because again I'm I'm running an 8 billion parameter size or two two

**[22:36]** billion parameter size or two two

**[22:36]** billion parameter size or two two billion parameter size model. Um

**[22:40]** billion parameter size model. Um

**[22:40]** billion parameter size model. Um on an L4,

**[22:42]** on an L4,

**[22:42]** on an L4, >> which is like okay, but obviously if

**[22:44]** >> which is like okay, but obviously if

**[22:44]** >> which is like okay, but obviously if you're doing anything concurrently and

**[22:46]** you're doing anything concurrently and

**[22:46]** you're doing anything concurrently and at scale, like that's going to go

**[22:47]** at scale, like that's going to go

**[22:47]** at scale, like that's going to go bonkers pretty quickly.

**[22:55]** >> So you get like the mean performance,

**[22:55]** >> So you get like the mean performance, the median performance and P99, which is

**[22:58]** the median performance and P99, which is

**[22:58]** the median performance and P99, which is like the the extreme level um which


### [23:00 - 24:00]

**[23:01]** like the the extreme level um which

**[23:01]** like the the extreme level um which matters for SLOs's and things like that.

**[23:04]** matters for SLOs's and things like that.

**[23:04]** matters for SLOs's and things like that. And you can also output this into um

**[23:07]** And you can also output this into um

**[23:07]** And you can also output this into um JSON format as well

**[23:08]** JSON format as well

**[23:08]** JSON format as well >> to take a closer look.

**[23:11]** >> to take a closer look.

**[23:11]** >> to take a closer look. >> So once you reach this, you can try also

**[23:14]** >> So once you reach this, you can try also

**[23:14]** >> So once you reach this, you can try also with an additional like tweak the

**[23:16]** with an additional like tweak the

**[23:16]** with an additional like tweak the parameters and then maybe compare the

**[23:18]** parameters and then maybe compare the

**[23:18]** parameters and then maybe compare the results and kind of see what what that

**[23:20]** results and kind of see what what that

**[23:20]** results and kind of see what what that changed if you do a rag setup. Um so I

**[23:24]** changed if you do a rag setup. Um so I

**[23:24]** changed if you do a rag setup. Um so I think we had I forget what we had what

**[23:26]** think we had I forget what we had what

**[23:26]** think we had I forget what we had what the initial command said. Um, but you

**[23:28]** the initial command said. Um, but you

**[23:28]** the initial command said. Um, but you can adjust those based on a different

**[23:29]** can adjust those based on a different

**[23:29]** can adjust those based on a different use case and kind of compare and

**[23:31]** use case and kind of compare and

**[23:31]** use case and kind of compare and contrast what the stats look like after

**[23:33]** contrast what the stats look like after

**[23:33]** contrast what the stats look like after because it just takes a couple minutes

**[23:34]** because it just takes a couple minutes

**[23:34]** because it just takes a couple minutes to run.

**[23:46]** Who's done with this first exercise?

**[23:46]** Who's done with this first exercise? Okay, good. Great. We're a few minutes

**[23:49]** Okay, good. Great. We're a few minutes

**[23:49]** Okay, good. Great. We're a few minutes away from the additional um 10 to 15

**[23:52]** away from the additional um 10 to 15

**[23:52]** away from the additional um 10 to 15 systems being ready. So,


### [24:00 - 25:00]

**[24:06]** Just for the sake of time, I am not

**[24:06]** Just for the sake of time, I am not going to do breaks for kind of

**[24:08]** going to do breaks for kind of

**[24:08]** going to do breaks for kind of discussion in between if everybody's

**[24:10]** discussion in between if everybody's

**[24:10]** discussion in between if everybody's okay with that and we can kind of just

**[24:11]** okay with that and we can kind of just

**[24:12]** okay with that and we can kind of just converse independently and I'll just

**[24:13]** converse independently and I'll just

**[24:13]** converse independently and I'll just awkwardly walk around the room. Um, so

**[24:15]** awkwardly walk around the room. Um, so

**[24:15]** awkwardly walk around the room. Um, so if you're done with activity one, move

**[24:17]** if you're done with activity one, move

**[24:17]** if you're done with activity one, move on to activity two because there are

**[24:19]** on to activity two because there are

**[24:19]** on to activity two because there are three activities and I want to make sure

**[24:21]** three activities and I want to make sure

**[24:21]** three activities and I want to make sure everybody has appropriate time for each

**[24:23]** everybody has appropriate time for each

**[24:23]** everybody has appropriate time for each that they would like. Um, but we will

**[24:25]** that they would like. Um, but we will

**[24:26]** that they would like. Um, but we will also have the systems up until probably

**[24:28]** also have the systems up until probably

**[24:28]** also have the systems up until probably about noon, I don't know, early

**[24:29]** about noon, I don't know, early

**[24:30]** about noon, I don't know, early afternoon. Um, we'll keep them up if you

**[24:32]** afternoon. Um, we'll keep them up if you

**[24:32]** afternoon. Um, we'll keep them up if you wanted to also go back and look at it

**[24:34]** wanted to also go back and look at it

**[24:34]** wanted to also go back and look at it after. So, is that good with everybody?

**[24:37]** after. So, is that good with everybody?

**[24:37]** after. So, is that good with everybody? We just kind of steamroll power through.

**[24:39]** We just kind of steamroll power through.

**[24:39]** We just kind of steamroll power through. Okay.

**[24:53]** >> So, I have a new URL where we have three

**[24:53]** >> So, I have a new URL where we have three more available so far, but others are

**[24:54]** more available so far, but others are

**[24:54]** more available so far, but others are provisioning. And I just wanted to go

**[24:56]** provisioning. And I just wanted to go

**[24:56]** provisioning. And I just wanted to go ahead and put the URL up. It'll come


### [25:00 - 26:00]

**[25:00]** ahead and put the URL up. It'll come

**[25:00]** ahead and put the URL up. It'll come they'll appear here.

**[25:02]** they'll appear here.

**[25:02]** they'll appear here. And it's the same password, right? You

**[25:04]** And it's the same password, right? You

**[25:04]** And it's the same password, right? You said

**[25:05]** said

**[25:05]** said >> it's the same password. It's the same

**[25:06]** >> it's the same password. It's the same

**[25:06]** >> it's the same password. It's the same password you said. Okay.

**[25:10]** password you said. Okay.

**[25:10]** password you said. Okay. Uh,

**[25:16]** >> okay. So, that's the new URL. Three more

**[25:16]** >> okay. So, that's the new URL. Three more systems, but they'll more will appear.

**[25:35]** >> Um, I put descriptions on the left um to

**[25:36]** >> Um, I put descriptions on the left um to explain that, but I just wanted to heads

**[25:37]** explain that, but I just wanted to heads

**[25:37]** explain that, but I just wanted to heads up. We're kind of moving from system

**[25:39]** up. We're kind of moving from system

**[25:39]** up. We're kind of moving from system performance to now that kind of factual

**[25:41]** performance to now that kind of factual

**[25:41]** performance to now that kind of factual accuracy part of the pyramid. Um so you

**[25:45]** accuracy part of the pyramid. Um so you

**[25:45]** accuracy part of the pyramid. Um so you get a sense of so we're going to be

**[25:46]** get a sense of so we're going to be

**[25:46]** get a sense of so we're going to be doing the MMLU pro um in the second

**[25:49]** doing the MMLU pro um in the second

**[25:49]** doing the MMLU pro um in the second activity and then the third activity is

**[25:51]** activity and then the third activity is

**[25:51]** activity and then the third activity is going to be focused on safety and bias

**[25:52]** going to be focused on safety and bias

**[25:52]** going to be focused on safety and bias and more custom evals. So that's the

**[25:54]** and more custom evals. So that's the

**[25:54]** and more custom evals. So that's the trajectory of activities. Feel free if

**[25:57]** trajectory of activities. Feel free if

**[25:57]** trajectory of activities. Feel free if one is also more interesting than the

**[25:59]** one is also more interesting than the

**[25:59]** one is also more interesting than the other feel free to skip around. Totally


### [26:00 - 27:00]

**[26:01]** other feel free to skip around. Totally

**[26:01]** other feel free to skip around. Totally fine.

**[26:01]** fine.

**[26:02]** fine. explain more about the pro. I'm curious

**[26:04]** explain more about the pro. I'm curious

**[26:04]** explain more about the pro. I'm curious about

**[26:07]** about

**[26:07]** about >> or you know like proprietary data sets

**[26:10]** >> or you know like proprietary data sets

**[26:10]** >> or you know like proprietary data sets if that's a thing

**[26:12]** if that's a thing

**[26:12]** if that's a thing >> you can c you can basically customize

**[26:14]** >> you can c you can basically customize

**[26:14]** >> you can c you can basically customize everything because like all these things

**[26:15]** everything because like all these things

**[26:16]** everything because like all these things are open source so you can create a

**[26:17]** are open source so you can create a

**[26:17]** are open source so you can create a similar type of eval in that multiple

**[26:19]** similar type of eval in that multiple

**[26:19]** similar type of eval in that multiple choice format that MMLU does with your

**[26:22]** choice format that MMLU does with your

**[26:22]** choice format that MMLU does with your own data set. Um there's different ways

**[26:25]** own data set. Um there's different ways

**[26:25]** own data set. Um there's different ways to do custom accuracy evals with your

**[26:29]** to do custom accuracy evals with your

**[26:29]** to do custom accuracy evals with your fine-tuned data. So we kind of do it in

**[26:31]** fine-tuned data. So we kind of do it in

**[26:31]** fine-tuned data. So we kind of do it in a we have so as part of one of the

**[26:33]** a we have so as part of one of the

**[26:33]** a we have so as part of one of the products we we incorporate an eval for

**[26:36]** products we we incorporate an eval for

**[26:36]** products we we incorporate an eval for um our fine-tuned models on your

**[26:38]** um our fine-tuned models on your

**[26:38]** um our fine-tuned models on your proprietary data and we do like a branch

**[26:40]** proprietary data and we do like a branch

**[26:40]** proprietary data and we do like a branch of MMLU essentially. So there's kind of

**[26:43]** of MMLU essentially. So there's kind of

**[26:43]** of MMLU essentially. So there's kind of there's a lot of ways to skin a cat even

**[26:44]** there's a lot of ways to skin a cat even

**[26:44]** there's a lot of ways to skin a cat even though I love cats um in regards to how

**[26:47]** though I love cats um in regards to how

**[26:47]** though I love cats um in regards to how to set up the eval tools available.

**[26:51]** to set up the eval tools available.

**[26:51]** to set up the eval tools available. >> Yeah. So yeah. Yes.

**[26:55]** >> Yeah. So yeah. Yes.

**[26:56]** >> Yeah. So yeah. Yes. >> You can just like fork it and ch and

**[26:58]** >> You can just like fork it and ch and

**[26:58]** >> You can just like fork it and ch and change the data sources. Yeah. Yeah.


### [27:00 - 28:00]

**[27:13]** >> Put that link back up.

**[27:13]** >> Put that link back up. The instructions don't some of the

**[27:15]** The instructions don't some of the

**[27:15]** The instructions don't some of the instructions don't look updated as I

**[27:17]** instructions don't look updated as I

**[27:17]** instructions don't look updated as I expected. So, I'm going what I'm going

**[27:19]** expected. So, I'm going what I'm going

**[27:19]** expected. So, I'm going what I'm going to do um is everybody in the Slack for a

**[27:22]** to do um is everybody in the Slack for a

**[27:22]** to do um is everybody in the Slack for a engineer worldfare?

**[27:24]** engineer worldfare?

**[27:24]** engineer worldfare? I created a um Slack channel called work

**[27:27]** I created a um Slack channel called work

**[27:27]** I created a um Slack channel called work workshop beyond benchmarks. Um and I'm

**[27:31]** workshop beyond benchmarks. Um and I'm

**[27:31]** workshop beyond benchmarks. Um and I'm going to put

**[27:33]** going to put

**[27:33]** going to put some of the so activity three. Does

**[27:35]** some of the so activity three. Does

**[27:35]** some of the so activity three. Does anybody see activity 3?

**[27:37]** anybody see activity 3?

**[27:37]** anybody see activity 3? >> No.

**[27:38]** >> No.

**[27:38]** >> No. >> Okay. I'm putting content in this um in

**[27:42]** >> Okay. I'm putting content in this um in

**[27:42]** >> Okay. I'm putting content in this um in this slack.

**[27:44]** this slack.

**[27:44]** this slack. >> If people can it's a public channel. If

**[27:47]** >> If people can it's a public channel. If

**[27:47]** >> If people can it's a public channel. If people can go there my um you'll see

**[27:50]** people can go there my um you'll see

**[27:50]** people can go there my um you'll see starting I'm the link is at activity 2

**[27:52]** starting I'm the link is at activity 2

**[27:52]** starting I'm the link is at activity 2 but then you'll also see the page for

**[27:54]** but then you'll also see the page for

**[27:54]** but then you'll also see the page for activity three


### [28:00 - 29:00]

**[28:08]** um approaching activity three and are

**[28:08]** um approaching activity three and are looking for that the systems for some

**[28:11]** looking for that the systems for some

**[28:11]** looking for that the systems for some reason didn't render my latest changes

**[28:13]** reason didn't render my latest changes

**[28:13]** reason didn't render my latest changes yesterday where I improved on activity

**[28:16]** yesterday where I improved on activity

**[28:16]** yesterday where I improved on activity three But I put the link to it to my

**[28:18]** three But I put the link to it to my

**[28:18]** three But I put the link to it to my repo in the Slack channel in this

**[28:21]** repo in the Slack channel in this

**[28:21]** repo in the Slack channel in this channel if you search for it. But

**[28:23]** channel if you search for it. But

**[28:23]** channel if you search for it. But there's information about the Slack in

**[28:24]** there's information about the Slack in

**[28:24]** there's information about the Slack in the emails that we got about the event,

**[28:26]** the emails that we got about the event,

**[28:26]** the emails that we got about the event, but also on the back of our badges as

**[28:28]** but also on the back of our badges as

**[28:28]** but also on the back of our badges as well to navigate there. And this will be

**[28:30]** well to navigate there. And this will be

**[28:30]** well to navigate there. And this will be good for after if anybody has any

**[28:31]** good for after if anybody has any

**[28:31]** good for after if anybody has any questions and I can send more info about

**[28:33]** questions and I can send more info about

**[28:33]** questions and I can send more info about any particular tool here as well.

**[28:42]** I wanted to have a wrap-up moment

**[28:42]** I wanted to have a wrap-up moment because we have we have about eight

**[28:43]** because we have we have about eight

**[28:43]** because we have we have about eight minutes. So please feel free to continue

**[28:45]** minutes. So please feel free to continue

**[28:45]** minutes. So please feel free to continue working. I put the link to the

**[28:47]** working. I put the link to the

**[28:47]** working. I put the link to the activities in the slack channel. These

**[28:49]** activities in the slack channel. These

**[28:49]** activities in the slack channel. These environments will be available um until

**[28:51]** environments will be available um until

**[28:51]** environments will be available um until the end of the day today. So you have

**[28:53]** the end of the day today. So you have

**[28:53]** the end of the day today. So you have time also to tinker around with whatever

**[28:55]** time also to tinker around with whatever

**[28:55]** time also to tinker around with whatever you want. Um so you would just to kind

**[28:58]** you want. Um so you would just to kind

**[28:58]** you want. Um so you would just to kind of recap we went through the fir


### [29:00 - 30:00]

**[29:02]** of recap we went through the fir

**[29:02]** of recap we went through the fir sounds funny. Um

**[29:04]** sounds funny. Um

**[29:04]** sounds funny. Um >> the first was at that system performance

**[29:06]** >> the first was at that system performance

**[29:06]** >> the first was at that system performance latency throughput level. Did everybody

**[29:08]** latency throughput level. Did everybody

**[29:08]** latency throughput level. Did everybody kind of get through that successfully?

**[29:11]** kind of get through that successfully?

**[29:11]** kind of get through that successfully? Of course, there's I tried to include

**[29:12]** Of course, there's I tried to include

**[29:12]** Of course, there's I tried to include reading material and stuff to kind of

**[29:14]** reading material and stuff to kind of

**[29:14]** reading material and stuff to kind of look more into things after because it

**[29:16]** look more into things after because it

**[29:16]** look more into things after because it is it is a very big topic and there's a

**[29:19]** is it is a very big topic and there's a

**[29:19]** is it is a very big topic and there's a lot going on and there's a lot of terms

**[29:20]** lot going on and there's a lot of terms

**[29:20]** lot going on and there's a lot of terms and it is very complicated. Um, so

**[29:23]** and it is very complicated. Um, so

**[29:23]** and it is very complicated. Um, so hopefully you can use it as a learning

**[29:24]** hopefully you can use it as a learning

**[29:24]** hopefully you can use it as a learning res my GitHub repository as a learning

**[29:26]** res my GitHub repository as a learning

**[29:26]** res my GitHub repository as a learning resource to kind of poke around after.

**[29:28]** resource to kind of poke around after.

**[29:28]** resource to kind of poke around after. But we started there and then we moved

**[29:29]** But we started there and then we moved

**[29:30]** But we started there and then we moved into the MMLU Pro with MLE Valh harness

**[29:32]** into the MMLU Pro with MLE Valh harness

**[29:32]** into the MMLU Pro with MLE Valh harness um which also allows you to do a lot of

**[29:34]** um which also allows you to do a lot of

**[29:34]** um which also allows you to do a lot of other evaluation um benchmarks as a part

**[29:37]** other evaluation um benchmarks as a part

**[29:37]** other evaluation um benchmarks as a part of that MLE valh harness framework. Um I

**[29:40]** of that MLE valh harness framework. Um I

**[29:40]** of that MLE valh harness framework. Um I happen to choose MMLU Pro because it

**[29:43]** happen to choose MMLU Pro because it

**[29:43]** happen to choose MMLU Pro because it took the least amount of time even

**[29:44]** took the least amount of time even

**[29:44]** took the least amount of time even though it took still 10 minutes. Um but

**[29:46]** though it took still 10 minutes. Um but

**[29:46]** though it took still 10 minutes. Um but there's other ones also that you can

**[29:48]** there's other ones also that you can

**[29:48]** there's other ones also that you can play around with um within that ML val

**[29:51]** play around with um within that ML val

**[29:51]** play around with um within that ML val harness repository. You can see the

**[29:53]** harness repository. You can see the

**[29:53]** harness repository. You can see the different um eval there. And then we

**[29:56]** different um eval there. And then we

**[29:56]** different um eval there. And then we ended with a safety evaluation with

**[29:58]** ended with a safety evaluation with

**[29:58]** ended with a safety evaluation with prompt which with prompt fu which um is


### [30:00 - 31:00]

**[30:00]** prompt which with prompt fu which um is

**[30:00]** prompt which with prompt fu which um is a tool that allows you to do a lot of

**[30:03]** a tool that allows you to do a lot of

**[30:03]** a tool that allows you to do a lot of customizing um and your own eval like

**[30:06]** customizing um and your own eval like

**[30:06]** customizing um and your own eval like you can do all kinds of custom tests

**[30:08]** you can do all kinds of custom tests

**[30:08]** you can do all kinds of custom tests with prompt fu. So I wanted to get you

**[30:11]** with prompt fu. So I wanted to get you

**[30:11]** with prompt fu. So I wanted to get you exposed to that tool so that you can

**[30:13]** exposed to that tool so that you can

**[30:13]** exposed to that tool so that you can start looking around there as well. That

**[30:15]** start looking around there as well. That

**[30:15]** start looking around there as well. That repository on github also has a lot of

**[30:17]** repository on github also has a lot of

**[30:17]** repository on github also has a lot of different examples. So we used that

**[30:19]** different examples. So we used that

**[30:19]** different examples. So we used that particular um safety focused example,

**[30:21]** particular um safety focused example,

**[30:21]** particular um safety focused example, but if you look at the promptu

**[30:23]** but if you look at the promptu

**[30:23]** but if you look at the promptu repository, it's very easy to play

**[30:25]** repository, it's very easy to play

**[30:25]** repository, it's very easy to play around with other types of examples as

**[30:27]** around with other types of examples as

**[30:28]** around with other types of examples as well. Um so we kind of moved up the

**[30:30]** well. Um so we kind of moved up the

**[30:30]** well. Um so we kind of moved up the pyramid throughout the activity. So

**[30:32]** pyramid throughout the activity. So

**[30:32]** pyramid throughout the activity. So hopefully you get a sense of kind of how

**[30:34]** hopefully you get a sense of kind of how

**[30:34]** hopefully you get a sense of kind of how you can layer this approach when you're

**[30:37]** you can layer this approach when you're

**[30:37]** you can layer this approach when you're looking at and trying to plan for how to

**[30:40]** looking at and trying to plan for how to

**[30:40]** looking at and trying to plan for how to strategically implement evals across

**[30:42]** strategically implement evals across

**[30:42]** strategically implement evals across your entire system. Um does anybody have

**[30:45]** your entire system. Um does anybody have

**[30:45]** your entire system. Um does anybody have any kind of questions or general what

**[30:49]** any kind of questions or general what

**[30:50]** any kind of questions or general what they experienced

**[30:53]** they experienced

**[30:53]** they experienced notes of import

**[30:59]** does this feel like valuable? I'm

**[30:59]** does this feel like valuable? I'm curious also about use cases and happy


### [31:00 - 32:00]

**[31:01]** curious also about use cases and happy

**[31:01]** curious also about use cases and happy to talk to you after too. Yeah.

**[31:03]** to talk to you after too. Yeah.

**[31:03]** to talk to you after too. Yeah. >> So um I'm like super new to evals and

**[31:05]** >> So um I'm like super new to evals and

**[31:05]** >> So um I'm like super new to evals and stuff. Uh so like when I'm doing evals

**[31:08]** stuff. Uh so like when I'm doing evals

**[31:08]** stuff. Uh so like when I'm doing evals it's like uh testing my prompts and like

**[31:11]** it's like uh testing my prompts and like

**[31:11]** it's like uh testing my prompts and like my data sets or if I want to switch like

**[31:13]** my data sets or if I want to switch like

**[31:13]** my data sets or if I want to switch like models out and stuff. Right now I'm

**[31:15]** models out and stuff. Right now I'm

**[31:15]** models out and stuff. Right now I'm actively thinking about like those eval

**[31:18]** actively thinking about like those eval

**[31:18]** actively thinking about like those eval connecting those actually to like my

**[31:20]** connecting those actually to like my

**[31:20]** connecting those actually to like my production like running like use cases

**[31:22]** production like running like use cases

**[31:22]** production like running like use cases to like track that like my real

**[31:25]** to like track that like my real

**[31:25]** to like track that like my real performance matches kind of like the

**[31:28]** performance matches kind of like the

**[31:28]** performance matches kind of like the scene. what is like is there like a word

**[31:30]** scene. what is like is there like a word

**[31:30]** scene. what is like is there like a word for that concept or like

**[31:32]** for that concept or like

**[31:32]** for that concept or like >> um so for me what I hear is the kind of

**[31:35]** >> um so for me what I hear is the kind of

**[31:35]** >> um so for me what I hear is the kind of CI/CD automation implementation of an

**[31:38]** CI/CD automation implementation of an

**[31:38]** CI/CD automation implementation of an evaluation framework just like with

**[31:39]** evaluation framework just like with

**[31:39]** evaluation framework just like with software engineering testing is kind of

**[31:41]** software engineering testing is kind of

**[31:41]** software engineering testing is kind of what I hear from that um

**[31:43]** what I hear from that um

**[31:44]** what I hear from that um >> you know yeah so I don't know it it's

**[31:45]** >> you know yeah so I don't know it it's

**[31:46]** >> you know yeah so I don't know it it's evaluation but in a more CI/CD format

**[31:49]** evaluation but in a more CI/CD format

**[31:49]** evaluation but in a more CI/CD format >> like when it's actually running for like

**[31:51]** >> like when it's actually running for like

**[31:51]** >> like when it's actually running for like customers and stuff

**[31:52]** customers and stuff

**[31:52]** customers and stuff >> yeah you should have a CI/CD framework

**[31:54]** >> yeah you should have a CI/CD framework

**[31:54]** >> yeah you should have a CI/CD framework that includes these evaluation tests

**[31:55]** that includes these evaluation tests

**[31:55]** that includes these evaluation tests just like for unit testing setups got

**[31:58]** just like for unit testing setups got

**[31:58]** just like for unit testing setups got Yeah.


### [32:00 - 33:00]

**[32:07]** >> Anybody else?

**[32:07]** >> Anybody else? >> Okay. Thank you everybody. I really

**[32:08]** >> Okay. Thank you everybody. I really

**[32:08]** >> Okay. Thank you everybody. I really appreciate it. Of course, feel free to

**[32:10]** appreciate it. Of course, feel free to

**[32:10]** appreciate it. Of course, feel free to Thank you.

**[32:12]** Thank you.

**[32:12]** Thank you. Feel free to um continue to use the

**[32:14]** Feel free to um continue to use the

**[32:14]** Feel free to um continue to use the repo, message me on Slack. Again, the

**[32:17]** repo, message me on Slack. Again, the

**[32:17]** repo, message me on Slack. Again, the environments will be up until about 6

**[32:19]** environments will be up until about 6

**[32:19]** environments will be up until about 6 pm, 5:00 pm tonight. So, thank you

**[32:21]** pm, 5:00 pm tonight. So, thank you

**[32:21]** pm, 5:00 pm tonight. So, thank you everybody.


