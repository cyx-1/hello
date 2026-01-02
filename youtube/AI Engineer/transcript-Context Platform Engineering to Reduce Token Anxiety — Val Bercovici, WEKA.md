# Context Platform Engineering to Reduce Token Anxiety — Val Bercovici, WEKA

**Video URL:** https://www.youtube.com/watch?v=NTBX-wxUhHs

---

## Full Transcript

### [00:00 - 01:00]

**[00:03]** This is Valberkichi, Weta's chief AI

**[00:03]** This is Valberkichi, Weta's chief AI officer, and I am joined by

**[00:05]** officer, and I am joined by

**[00:05]** officer, and I am joined by >> Kellen Fox, head out of the product

**[00:07]** >> Kellen Fox, head out of the product

**[00:07]** >> Kellen Fox, head out of the product management team here at WA

**[00:09]** management team here at WA

**[00:09]** management team here at WA >> and we're both thrilled to present

**[00:10]** >> and we're both thrilled to present

**[00:10]** >> and we're both thrilled to present context platform engineering to you at

**[00:13]** context platform engineering to you at

**[00:13]** context platform engineering to you at the AI.engineering code summit. Now,

**[00:16]** the AI.engineering code summit. Now,

**[00:16]** the AI.engineering code summit. Now, let's kick this off with uh an

**[00:18]** let's kick this off with uh an

**[00:18]** let's kick this off with uh an announcement we're making. We're

**[00:20]** announcement we're making. We're

**[00:20]** announcement we're making. We're actually open sourcing our context

**[00:23]** actually open sourcing our context

**[00:23]** actually open sourcing our context platform engineering toolkit.

**[00:26]** platform engineering toolkit.

**[00:26]** platform engineering toolkit. And this toolkit features a really cool

**[00:28]** And this toolkit features a really cool

**[00:28]** And this toolkit features a really cool load generator that Kalen wrote that

**[00:31]** load generator that Kalen wrote that

**[00:31]** load generator that Kalen wrote that lets you configure agent swarms uh and

**[00:33]** lets you configure agent swarms uh and

**[00:33]** lets you configure agent swarms uh and agent subtasks with very specific SLOs's

**[00:37]** agent subtasks with very specific SLOs's

**[00:37]** agent subtasks with very specific SLOs's being able to cycle through

**[00:38]** being able to cycle through

**[00:38]** being able to cycle through deterministic and random prompt cycles

**[00:41]** deterministic and random prompt cycles

**[00:41]** deterministic and random prompt cycles and engineer context platforms with all

**[00:43]** and engineer context platforms with all

**[00:44]** and engineer context platforms with all sorts of model parallelism options,

**[00:46]** sorts of model parallelism options,

**[00:46]** sorts of model parallelism options, disagregated or aggregated pre-fill and

**[00:48]** disagregated or aggregated pre-fill and

**[00:48]** disagregated or aggregated pre-fill and decode options and some really important

**[00:51]** decode options and some really important

**[00:51]** decode options and some really important memory tiering options we're going to be

**[00:52]** memory tiering options we're going to be

**[00:52]** memory tiering options we're going to be discussing here. So, if we advance the

**[00:55]** discussing here. So, if we advance the

**[00:55]** discussing here. So, if we advance the next slide, we'll see that this is an

**[00:58]** next slide, we'll see that this is an

**[00:58]** next slide, we'll see that this is an open-source toolkit that's already


### [01:00 - 02:00]

**[01:00]** open-source toolkit that's already

**[01:00]** open-source toolkit that's already available to you on GitHub. So, Ken and

**[01:03]** available to you on GitHub. So, Ken and

**[01:03]** available to you on GitHub. So, Ken and I really encourage you to just get on

**[01:05]** I really encourage you to just get on

**[01:05]** I really encourage you to just get on GitHub, download this, play with it, and

**[01:07]** GitHub, download this, play with it, and

**[01:07]** GitHub, download this, play with it, and give us your feedback. Let us know what

**[01:09]** give us your feedback. Let us know what

**[01:09]** give us your feedback. Let us know what you need change. Feel free to contribute

**[01:11]** you need change. Feel free to contribute

**[01:11]** you need change. Feel free to contribute and fork the project uh and advance the

**[01:14]** and fork the project uh and advance the

**[01:14]** and fork the project uh and advance the field of context platform engineering,

**[01:16]** field of context platform engineering,

**[01:16]** field of context platform engineering, which we're going to be introducing to

**[01:18]** which we're going to be introducing to

**[01:18]** which we're going to be introducing to you later today. So moving on, one of

**[01:22]** you later today. So moving on, one of

**[01:22]** you later today. So moving on, one of the key requirements for context

**[01:24]** the key requirements for context

**[01:24]** the key requirements for context platform engineering really relates to

**[01:26]** platform engineering really relates to

**[01:26]** platform engineering really relates to the contact engineering uh insight that

**[01:29]** the contact engineering uh insight that

**[01:29]** the contact engineering uh insight that our friends at Manis shared with us

**[01:31]** our friends at Manis shared with us

**[01:31]** our friends at Manis shared with us earlier this summer in their pretty

**[01:33]** earlier this summer in their pretty

**[01:33]** earlier this summer in their pretty infamous now context engineering blog

**[01:36]** infamous now context engineering blog

**[01:36]** infamous now context engineering blog and they highlighted the fact that KV

**[01:38]** and they highlighted the fact that KV

**[01:38]** and they highlighted the fact that KV cache hit rate is the single most

**[01:40]** cache hit rate is the single most

**[01:40]** cache hit rate is the single most important metric for production grade AI

**[01:43]** important metric for production grade AI

**[01:43]** important metric for production grade AI agents. And the reason context platform

**[01:45]** agents. And the reason context platform

**[01:46]** agents. And the reason context platform engineering is so important is it

**[01:48]** engineering is so important is it

**[01:48]** engineering is so important is it dramatically simplifies reaching maximum

**[01:51]** dramatically simplifies reaching maximum

**[01:51]** dramatically simplifies reaching maximum KV cache hit rates as we're about to

**[01:52]** KV cache hit rates as we're about to

**[01:52]** KV cache hit rates as we're about to show you

**[01:54]** show you

**[01:54]** show you on a more personal level. If we think

**[01:56]** on a more personal level. If we think

**[01:56]** on a more personal level. If we think about token anxiety, I know that each

**[01:59]** about token anxiety, I know that each

**[01:59]** about token anxiety, I know that each and every one of us, you know, feel that


### [02:00 - 03:00]

**[02:00]** and every one of us, you know, feel that

**[02:00]** and every one of us, you know, feel that anxiety. The reason context platform

**[02:03]** anxiety. The reason context platform

**[02:03]** anxiety. The reason context platform engineering is so important is shared by

**[02:06]** engineering is so important is shared by

**[02:06]** engineering is so important is shared by the context engineering blog from Manis

**[02:09]** the context engineering blog from Manis

**[02:09]** the context engineering blog from Manis earlier this summer where they

**[02:10]** earlier this summer where they

**[02:10]** earlier this summer where they particularly emphasize KV cache hit

**[02:13]** particularly emphasize KV cache hit

**[02:13]** particularly emphasize KV cache hit rates are the single most important

**[02:15]** rates are the single most important

**[02:15]** rates are the single most important metrics for production grade AI agents

**[02:18]** metrics for production grade AI agents

**[02:18]** metrics for production grade AI agents and context platform engineering quite

**[02:20]** and context platform engineering quite

**[02:20]** and context platform engineering quite simply maximizes KV cache hit rates in a

**[02:24]** simply maximizes KV cache hit rates in a

**[02:24]** simply maximizes KV cache hit rates in a very straightforward manner.

**[02:26]** very straightforward manner.

**[02:26]** very straightforward manner. On a more personal note, if you think

**[02:28]** On a more personal note, if you think

**[02:28]** On a more personal note, if you think about to the concept of token anxiety,

**[02:31]** about to the concept of token anxiety,

**[02:31]** about to the concept of token anxiety, as we all regularly hit token rate

**[02:33]** as we all regularly hit token rate

**[02:33]** as we all regularly hit token rate limits, context platform engineering

**[02:35]** limits, context platform engineering

**[02:35]** limits, context platform engineering helps to engineer platforms that

**[02:38]** helps to engineer platforms that

**[02:38]** helps to engineer platforms that eliminate token rate limits uh and help

**[02:40]** eliminate token rate limits uh and help

**[02:40]** eliminate token rate limits uh and help us be more productive with regards to

**[02:42]** us be more productive with regards to

**[02:42]** us be more productive with regards to developing our software.

**[02:50]** Now in the absence of context platform

**[02:50]** Now in the absence of context platform engineering, we often resort to context

**[02:52]** engineering, we often resort to context

**[02:52]** engineering, we often resort to context financial engineering and that's

**[02:54]** financial engineering and that's

**[02:54]** financial engineering and that's fundamentally prom arbitrage where we

**[02:57]** fundamentally prom arbitrage where we

**[02:57]** fundamentally prom arbitrage where we balance the needs of pricing between the

**[02:59]** balance the needs of pricing between the

**[02:59]** balance the needs of pricing between the bookends of input and output tokens with


### [03:00 - 04:00]

**[03:02]** bookends of input and output tokens with

**[03:02]** bookends of input and output tokens with these new token pricing categories that

**[03:04]** these new token pricing categories that

**[03:04]** these new token pricing categories that have appeared in the landscape over the

**[03:05]** have appeared in the landscape over the

**[03:05]** have appeared in the landscape over the past few months focusing on cash rights

**[03:08]** past few months focusing on cash rights

**[03:08]** past few months focusing on cash rights and cash reads. And we've got to be

**[03:10]** and cash reads. And we've got to be

**[03:10]** and cash reads. And we've got to be somewhat clairvoyant

**[03:12]** somewhat clairvoyant

**[03:12]** somewhat clairvoyant when we're doing the arbitrage to figure

**[03:14]** when we're doing the arbitrage to figure

**[03:14]** when we're doing the arbitrage to figure out how many cash rights you want to

**[03:16]** out how many cash rights you want to

**[03:16]** out how many cash rights you want to invest in for either five minute time to

**[03:18]** invest in for either five minute time to

**[03:18]** invest in for either five minute time to live. In some cases with anthropic, for

**[03:20]** live. In some cases with anthropic, for

**[03:20]** live. In some cases with anthropic, for example, uh we can do one hour time to

**[03:23]** example, uh we can do one hour time to

**[03:23]** example, uh we can do one hour time to live. And that's all against balanced

**[03:25]** live. And that's all against balanced

**[03:25]** live. And that's all against balanced against the predictions we need to make

**[03:27]** against the predictions we need to make

**[03:27]** against the predictions we need to make on how many cash reads and cash hits we

**[03:29]** on how many cash reads and cash hits we

**[03:29]** on how many cash reads and cash hits we think we're going to have during those

**[03:31]** think we're going to have during those

**[03:31]** think we're going to have during those intervals. This becomes very very tricky

**[03:33]** intervals. This becomes very very tricky

**[03:33]** intervals. This becomes very very tricky to be clairvoyant and predict the

**[03:35]** to be clairvoyant and predict the

**[03:35]** to be clairvoyant and predict the future. And I think it's much better to

**[03:37]** future. And I think it's much better to

**[03:37]** future. And I think it's much better to apply context prompt engineering

**[03:38]** apply context prompt engineering

**[03:38]** apply context prompt engineering techniques to overcome token anxiety and

**[03:41]** techniques to overcome token anxiety and

**[03:41]** techniques to overcome token anxiety and prompt cash arbitrage than to continue

**[03:43]** prompt cash arbitrage than to continue

**[03:43]** prompt cash arbitrage than to continue to to do the arbitrage and context

**[03:45]** to to do the arbitrage and context

**[03:45]** to to do the arbitrage and context financial engineering.

**[03:47]** financial engineering.

**[03:47]** financial engineering. And so one of the ways we're going to be

**[03:48]** And so one of the ways we're going to be

**[03:48]** And so one of the ways we're going to be doing that

**[03:51]** doing that

**[03:51]** doing that is looking at and and Ken's going to

**[03:53]** is looking at and and Ken's going to

**[03:53]** is looking at and and Ken's going to dive into this deeply, the cadence

**[03:55]** dive into this deeply, the cadence

**[03:55]** dive into this deeply, the cadence mismatch between the relatively slow

**[03:58]** mismatch between the relatively slow

**[03:58]** mismatch between the relatively slow human feedback loops for agents and then


### [04:00 - 05:00]

**[04:00]** human feedback loops for agents and then

**[04:00]** human feedback loops for agents and then the agent swarms and the agent subtasks

**[04:02]** the agent swarms and the agent subtasks

**[04:02]** the agent swarms and the agent subtasks themselves that iterate at much higher

**[04:05]** themselves that iterate at much higher

**[04:05]** themselves that iterate at much higher cadence, often in parallel, waiting on

**[04:08]** cadence, often in parallel, waiting on

**[04:08]** cadence, often in parallel, waiting on humans, but conducting a lot of really

**[04:10]** humans, but conducting a lot of really

**[04:10]** humans, but conducting a lot of really cool work in the background, consuming a

**[04:12]** cool work in the background, consuming a

**[04:12]** cool work in the background, consuming a lot of tokens in the background, many of

**[04:14]** lot of tokens in the background, many of

**[04:14]** lot of tokens in the background, many of which are cachable, but we just never

**[04:16]** which are cachable, but we just never

**[04:16]** which are cachable, but we just never know how the platform is able to

**[04:18]** know how the platform is able to

**[04:18]** know how the platform is able to respond. And that's one thing we're

**[04:19]** respond. And that's one thing we're

**[04:19]** respond. And that's one thing we're going to be diving into here is the fact

**[04:22]** going to be diving into here is the fact

**[04:22]** going to be diving into here is the fact that if we go to the next slide, we're

**[04:24]** that if we go to the next slide, we're

**[04:24]** that if we go to the next slide, we're looking at fundamentally a token storage

**[04:27]** looking at fundamentally a token storage

**[04:27]** looking at fundamentally a token storage problem. And what we're going to be

**[04:29]** problem. And what we're going to be

**[04:29]** problem. And what we're going to be doing is explaining how the service

**[04:31]** doing is explaining how the service

**[04:31]** doing is explaining how the service level agreements we sign up to when we

**[04:34]** level agreements we sign up to when we

**[04:34]** level agreements we sign up to when we subscribe to our various, you know,

**[04:36]** subscribe to our various, you know,

**[04:36]** subscribe to our various, you know, token tiers or we actually commit in our

**[04:39]** token tiers or we actually commit in our

**[04:39]** token tiers or we actually commit in our instructions and our agentic

**[04:40]** instructions and our agentic

**[04:40]** instructions and our agentic instructions to specific token cache

**[04:43]** instructions to specific token cache

**[04:43]** instructions to specific token cache rights and cash reads. how those SLAs's

**[04:46]** rights and cash reads. how those SLAs's

**[04:46]** rights and cash reads. how those SLAs's convert to service level objectives

**[04:48]** convert to service level objectives

**[04:48]** convert to service level objectives delivered by the context platform

**[04:50]** delivered by the context platform

**[04:50]** delivered by the context platform itself. And more particularly, one of

**[04:53]** itself. And more particularly, one of

**[04:53]** itself. And more particularly, one of the insights that Kalan reached from his

**[04:55]** the insights that Kalan reached from his

**[04:55]** the insights that Kalan reached from his research at WA Labs is that what we're

**[04:58]** research at WA Labs is that what we're

**[04:58]** research at WA Labs is that what we're doing when we actually subscribe to our


### [05:00 - 06:00]

**[05:01]** doing when we actually subscribe to our

**[05:01]** doing when we actually subscribe to our token tiers or we actually pay for

**[05:03]** token tiers or we actually pay for

**[05:03]** token tiers or we actually pay for particular token rights is we're really

**[05:05]** particular token rights is we're really

**[05:05]** particular token rights is we're really purchasing cash KB slots in token

**[05:09]** purchasing cash KB slots in token

**[05:09]** purchasing cash KB slots in token storage. So there's definitely a whole

**[05:11]** storage. So there's definitely a whole

**[05:11]** storage. So there's definitely a whole science around the context platform

**[05:12]** science around the context platform

**[05:12]** science around the context platform engineering to how context platforms

**[05:15]** engineering to how context platforms

**[05:15]** engineering to how context platforms take those SLA requirements optimize

**[05:18]** take those SLA requirements optimize

**[05:18]** take those SLA requirements optimize infrastructure optimize KV caching and

**[05:20]** infrastructure optimize KV caching and

**[05:20]** infrastructure optimize KV caching and memory tiers and deliver specific SLOs's

**[05:24]** memory tiers and deliver specific SLOs's

**[05:24]** memory tiers and deliver specific SLOs's to try and meet those SLAs's as much as

**[05:26]** to try and meet those SLAs's as much as

**[05:26]** to try and meet those SLAs's as much as possible. So with that let me actually

**[05:28]** possible. So with that let me actually

**[05:28]** possible. So with that let me actually hand it over to Ken for uh actual

**[05:31]** hand it over to Ken for uh actual

**[05:31]** hand it over to Ken for uh actual research findings and lab and and test

**[05:33]** research findings and lab and and test

**[05:34]** research findings and lab and and test results from WA Labs.

**[05:36]** results from WA Labs.

**[05:36]** results from WA Labs. >> Thanks Val. So, look, what I want to do

**[05:37]** >> Thanks Val. So, look, what I want to do

**[05:37]** >> Thanks Val. So, look, what I want to do is just go back to one of the slides

**[05:39]** is just go back to one of the slides

**[05:39]** is just go back to one of the slides that Val showed earlier. And what I'm

**[05:41]** that Val showed earlier. And what I'm

**[05:41]** that Val showed earlier. And what I'm going to do from now on is I'm going to

**[05:42]** going to do from now on is I'm going to

**[05:42]** going to do from now on is I'm going to focus on that right hand loop. And the

**[05:45]** focus on that right hand loop. And the

**[05:45]** focus on that right hand loop. And the first thing I'm going to do is I'm going

**[05:46]** first thing I'm going to do is I'm going

**[05:46]** first thing I'm going to do is I'm going to start by visualizing what that loop

**[05:49]** to start by visualizing what that loop

**[05:49]** to start by visualizing what that loop actually looks like. And then we're

**[05:50]** actually looks like. And then we're

**[05:50]** actually looks like. And then we're going to go into a little bit more

**[05:51]** going to go into a little bit more

**[05:51]** going to go into a little bit more detail.

**[05:58]** So, if you if you think about that loop

**[05:58]** So, if you if you think about that loop as a column, and I've got a graph here


### [06:00 - 07:00]

**[06:00]** as a column, and I've got a graph here

**[06:00]** as a column, and I've got a graph here that shows a very very common uh pattern

**[06:02]** that shows a very very common uh pattern

**[06:02]** that shows a very very common uh pattern that happens in agents. So the the

**[06:05]** that happens in agents. So the the

**[06:05]** that happens in agents. So the the salmon color is showing new tokens that

**[06:07]** salmon color is showing new tokens that

**[06:07]** salmon color is showing new tokens that the system's being exposed to. The gray

**[06:09]** the system's being exposed to. The gray

**[06:09]** the system's being exposed to. The gray is something that could be ced again

**[06:11]** is something that could be ced again

**[06:11]** is something that could be ced again within a limited amount of C. We'll get

**[06:13]** within a limited amount of C. We'll get

**[06:13]** within a limited amount of C. We'll get into that shortly. The blue is the

**[06:14]** into that shortly. The blue is the

**[06:14]** into that shortly. The blue is the output tokens. And these blue dots down

**[06:16]** output tokens. And these blue dots down

**[06:16]** output tokens. And these blue dots down the bottom are showing when the user is

**[06:18]** the bottom are showing when the user is

**[06:18]** the bottom are showing when the user is actually giving responses in this

**[06:20]** actually giving responses in this

**[06:20]** actually giving responses in this particular case. This is a really common

**[06:22]** particular case. This is a really common

**[06:22]** particular case. This is a really common example you get where basically you

**[06:24]** example you get where basically you

**[06:24]** example you get where basically you start off you consume context all the

**[06:26]** start off you consume context all the

**[06:26]** start off you consume context all the way up until you hit a um a high a high

**[06:30]** way up until you hit a um a high a high

**[06:30]** way up until you hit a um a high a high watermark set by either the model

**[06:32]** watermark set by either the model

**[06:32]** watermark set by either the model maximum length or by the inference

**[06:33]** maximum length or by the inference

**[06:34]** maximum length or by the inference provider itself. there's a summarization

**[06:36]** provider itself. there's a summarization

**[06:36]** provider itself. there's a summarization um phase and then you start a new cycle

**[06:39]** um phase and then you start a new cycle

**[06:39]** um phase and then you start a new cycle and everybody knows that summarization

**[06:41]** and everybody knows that summarization

**[06:41]** and everybody knows that summarization phase where sometimes you know the agent

**[06:43]** phase where sometimes you know the agent

**[06:43]** phase where sometimes you know the agent loses a little bit of its fidelity a bit

**[06:45]** loses a little bit of its fidelity a bit

**[06:45]** loses a little bit of its fidelity a bit of its intelligence and uh and that's

**[06:47]** of its intelligence and uh and that's

**[06:47]** of its intelligence and uh and that's why we're trying to you know uh get more

**[06:50]** why we're trying to you know uh get more

**[06:50]** why we're trying to you know uh get more context engineering to larger set of

**[06:52]** context engineering to larger set of

**[06:52]** context engineering to larger set of platforms and we can we can raise that

**[06:54]** platforms and we can we can raise that

**[06:54]** platforms and we can we can raise that watermark

**[06:56]** watermark

**[06:56]** watermark so if we go into this in a little bit

**[06:57]** so if we go into this in a little bit

**[06:57]** so if we go into this in a little bit more detail the question I often get is

**[06:59]** more detail the question I often get is

**[06:59]** more detail the question I often get is okay well what is that that's a lot of


### [07:00 - 08:00]

**[07:02]** okay well what is that that's a lot of

**[07:02]** okay well what is that that's a lot of gray what what's that made out of so

**[07:04]** gray what what's that made out of so

**[07:04]** gray what what's that made out of so here I'm able to um get the data and

**[07:07]** here I'm able to um get the data and

**[07:07]** here I'm able to um get the data and actually look at individual prompts and

**[07:10]** actually look at individual prompts and

**[07:10]** actually look at individual prompts and what actually makes them up. So when you

**[07:12]** what actually makes them up. So when you

**[07:12]** what actually makes them up. So when you look at agentic data especially agentic

**[07:15]** look at agentic data especially agentic

**[07:15]** look at agentic data especially agentic coding the actual user input is only a

**[07:17]** coding the actual user input is only a

**[07:18]** coding the actual user input is only a really small part of it and you can kind

**[07:19]** really small part of it and you can kind

**[07:19]** really small part of it and you can kind of see it here just visually that if you

**[07:21]** of see it here just visually that if you

**[07:21]** of see it here just visually that if you just scan across the the lighter whiter

**[07:23]** just scan across the the lighter whiter

**[07:23]** just scan across the the lighter whiter colors are the um the system prompt and

**[07:26]** colors are the um the system prompt and

**[07:26]** colors are the um the system prompt and the user text itself and the rest of it

**[07:29]** the user text itself and the rest of it

**[07:29]** the user text itself and the rest of it is tool use and tool responses. So uh

**[07:32]** is tool use and tool responses. So uh

**[07:32]** is tool use and tool responses. So uh this is this one in particular is from

**[07:34]** this is this one in particular is from

**[07:34]** this is this one in particular is from claw code where you're spending a lot of

**[07:37]** claw code where you're spending a lot of

**[07:37]** claw code where you're spending a lot of time um where the the system is you know

**[07:39]** time um where the the system is you know

**[07:39]** time um where the the system is you know doing like for example a a bash command

**[07:42]** doing like for example a a bash command

**[07:42]** doing like for example a a bash command it's grapping something it's getting a

**[07:43]** it's grapping something it's getting a

**[07:43]** it's grapping something it's getting a result and then it's doing something

**[07:44]** result and then it's doing something

**[07:44]** result and then it's doing something else. So where where this really shows

**[07:47]** else. So where where this really shows

**[07:47]** else. So where where this really shows out in the data is if you actually look

**[07:48]** out in the data is if you actually look

**[07:48]** out in the data is if you actually look at the median time between requests it

**[07:51]** at the median time between requests it

**[07:51]** at the median time between requests it may be some for conversation that looks

**[07:54]** may be some for conversation that looks

**[07:54]** may be some for conversation that looks like that we have data for billions and

**[07:55]** like that we have data for billions and

**[07:55]** like that we have data for billions and billions and billions and billions of

**[07:57]** billions and billions and billions of

**[07:57]** billions and billions and billions of tokens. Um the median time is 10


### [08:00 - 09:00]

**[08:00]** tokens. Um the median time is 10

**[08:00]** tokens. Um the median time is 10 seconds, 15 seconds maybe. Um that

**[08:02]** seconds, 15 seconds maybe. Um that

**[08:02]** seconds, 15 seconds maybe. Um that heavily depends on whether the human's

**[08:04]** heavily depends on whether the human's

**[08:04]** heavily depends on whether the human's involved in checking every single uh

**[08:06]** involved in checking every single uh

**[08:06]** involved in checking every single uh tool use, but the meanantime is in the

**[08:09]** tool use, but the meanantime is in the

**[08:09]** tool use, but the meanantime is in the minutes because the human or even hours

**[08:11]** minutes because the human or even hours

**[08:11]** minutes because the human or even hours because the human time to respond is

**[08:13]** because the human time to respond is

**[08:14]** because the human time to respond is much much much higher. And that's what

**[08:15]** much much much higher. And that's what

**[08:15]** much much much higher. And that's what we're showing before of the two sides of

**[08:17]** we're showing before of the two sides of

**[08:17]** we're showing before of the two sides of a loop.

**[08:18]** a loop.

**[08:18]** a loop. So the other thing that's interesting

**[08:20]** So the other thing that's interesting

**[08:20]** So the other thing that's interesting and and something that's very common

**[08:21]** and and something that's very common

**[08:21]** and and something that's very common today is is uh is multi- aent. So you

**[08:23]** today is is uh is multi- aent. So you

**[08:23]** today is is uh is multi- aent. So you might have a core agent which I've shown

**[08:25]** might have a core agent which I've shown

**[08:25]** might have a core agent which I've shown here is the orchestrator and then you've

**[08:27]** here is the orchestrator and then you've

**[08:27]** here is the orchestrator and then you've got these sub agents that are like spun

**[08:29]** got these sub agents that are like spun

**[08:29]** got these sub agents that are like spun up to do individual tasks and depending

**[08:31]** up to do individual tasks and depending

**[08:31]** up to do individual tasks and depending on the type of agentic uh coding um or

**[08:35]** on the type of agentic uh coding um or

**[08:35]** on the type of agentic uh coding um or just any agentic software in general.

**[08:37]** just any agentic software in general.

**[08:37]** just any agentic software in general. These agents or these sub agents may be

**[08:40]** These agents or these sub agents may be

**[08:40]** These agents or these sub agents may be short-lived as in their context does not

**[08:43]** short-lived as in their context does not

**[08:43]** short-lived as in their context does not endure between one wake up and the next

**[08:45]** endure between one wake up and the next

**[08:45]** endure between one wake up and the next or there are somes some when they do

**[08:48]** or there are somes some when they do

**[08:48]** or there are somes some when they do endure and it's really important to use

**[08:51]** endure and it's really important to use

**[08:51]** endure and it's really important to use our agents because it allows us to

**[08:52]** our agents because it allows us to

**[08:52]** our agents because it allows us to create to effectively target more

**[08:54]** create to effectively target more

**[08:54]** create to effectively target more context at very particular parts of what

**[08:57]** context at very particular parts of what

**[08:57]** context at very particular parts of what the problem you're trying to solve. But

**[08:59]** the problem you're trying to solve. But

**[08:59]** the problem you're trying to solve. But as a result, you do actually end up


### [09:00 - 10:00]

**[09:01]** as a result, you do actually end up

**[09:01]** as a result, you do actually end up using more context and I'll explain that

**[09:02]** using more context and I'll explain that

**[09:02]** using more context and I'll explain that very shortly. But if you visualize this

**[09:05]** very shortly. But if you visualize this

**[09:05]** very shortly. But if you visualize this gray section a different way and I show

**[09:07]** gray section a different way and I show

**[09:07]** gray section a different way and I show you the colors, you can kind of see how

**[09:09]** you the colors, you can kind of see how

**[09:09]** you the colors, you can kind of see how there's this common relationship of the

**[09:11]** there's this common relationship of the

**[09:11]** there's this common relationship of the common context between all of them.

**[09:14]** common context between all of them.

**[09:14]** common context between all of them. Again, this is varies a little bit

**[09:15]** Again, this is varies a little bit

**[09:16]** Again, this is varies a little bit depending on codeex versus cloud code

**[09:18]** depending on codeex versus cloud code

**[09:18]** depending on codeex versus cloud code versus versus others. But you can see

**[09:21]** versus versus others. But you can see

**[09:21]** versus versus others. But you can see how it changes over time and how the

**[09:23]** how it changes over time and how the

**[09:23]** how it changes over time and how the agents um relate to each other and have

**[09:25]** agents um relate to each other and have

**[09:25]** agents um relate to each other and have this common understanding and then back

**[09:27]** this common understanding and then back

**[09:27]** this common understanding and then back to the orchestrator to to wake up the

**[09:29]** to the orchestrator to to wake up the

**[09:29]** to the orchestrator to to wake up the next agent.

**[09:33]** The the the the thing that we're here to

**[09:34]** The the the the thing that we're here to talk about today though mainly is that

**[09:35]** talk about today though mainly is that

**[09:35]** talk about today though mainly is that like while there's a lot of gray that

**[09:37]** like while there's a lot of gray that

**[09:37]** like while there's a lot of gray that could be ced, the reality is very

**[09:40]** could be ced, the reality is very

**[09:40]** could be ced, the reality is very different. So if you send this to an

**[09:41]** different. So if you send this to an

**[09:41]** different. So if you send this to an inference provider, what ends up

**[09:43]** inference provider, what ends up

**[09:44]** inference provider, what ends up happening is you don't actually get 100%

**[09:47]** happening is you don't actually get 100%

**[09:47]** happening is you don't actually get 100% of the C hits that you could um that you

**[09:49]** of the C hits that you could um that you

**[09:49]** of the C hits that you could um that you could get. Now why does this matter?

**[09:52]** could get. Now why does this matter?

**[09:52]** could get. Now why does this matter? Well, there's two ways to look at this.

**[09:54]** Well, there's two ways to look at this.

**[09:54]** Well, there's two ways to look at this. If you're paying for API tokens, uh

**[09:58]** If you're paying for API tokens, uh

**[09:58]** If you're paying for API tokens, uh you're literally it's literally costing


### [10:00 - 11:00]

**[10:00]** you're literally it's literally costing

**[10:00]** you're literally it's literally costing you more money because every time you

**[10:02]** you more money because every time you

**[10:02]** you more money because every time you see a yellow here, and this is just a

**[10:03]** see a yellow here, and this is just a

**[10:03]** see a yellow here, and this is just a simple example, you're paying input

**[10:05]** simple example, you're paying input

**[10:05]** simple example, you're paying input token cost. So, you're re you're

**[10:07]** token cost. So, you're re you're

**[10:07]** token cost. So, you're re you're refreshing your cage and you're paying a

**[10:09]** refreshing your cage and you're paying a

**[10:09]** refreshing your cage and you're paying a full hit for that. So, potentially 10

**[10:11]** full hit for that. So, potentially 10

**[10:11]** full hit for that. So, potentially 10 times more than than what you were if it

**[10:13]** times more than than what you were if it

**[10:13]** times more than than what you were if it was caged. If you're a subscription user

**[10:16]** was caged. If you're a subscription user

**[10:16]** was caged. If you're a subscription user and you're thinking, well, I don't care

**[10:17]** and you're thinking, well, I don't care

**[10:17]** and you're thinking, well, I don't care about the cost. I don't pay for that. I

**[10:19]** about the cost. I don't pay for that. I

**[10:19]** about the cost. I don't pay for that. I pay a flat rate. That is true, but

**[10:20]** pay a flat rate. That is true, but

**[10:20]** pay a flat rate. That is true, but you're still, like we said before,

**[10:23]** you're still, like we said before,

**[10:23]** you're still, like we said before, you're paying for a subscription and

**[10:25]** you're paying for a subscription and

**[10:25]** you're paying for a subscription and that subscription is rate limited due to

**[10:28]** that subscription is rate limited due to

**[10:28]** that subscription is rate limited due to your case usage and um you may actually

**[10:31]** your case usage and um you may actually

**[10:31]** your case usage and um you may actually hit rate limits further or quicker. So,

**[10:34]** hit rate limits further or quicker. So,

**[10:34]** hit rate limits further or quicker. So, that's something that we want to be able

**[10:36]** that's something that we want to be able

**[10:36]** that's something that we want to be able to do. We work with a lot of providers

**[10:37]** to do. We work with a lot of providers

**[10:37]** to do. We work with a lot of providers today to to remove as much of this as

**[10:40]** today to to remove as much of this as

**[10:40]** today to to remove as much of this as possible. That's good for the user

**[10:41]** possible. That's good for the user

**[10:41]** possible. That's good for the user experience and it's also good for the

**[10:43]** experience and it's also good for the

**[10:43]** experience and it's also good for the provider.

**[10:45]** provider.

**[10:45]** provider. So, why does this happen? Well, I mean

**[10:47]** So, why does this happen? Well, I mean

**[10:47]** So, why does this happen? Well, I mean it if you think about the last graph

**[10:49]** it if you think about the last graph

**[10:49]** it if you think about the last graph where I show the columns, they're

**[10:51]** where I show the columns, they're

**[10:51]** where I show the columns, they're they're not they don't take into account

**[10:52]** they're not they don't take into account

**[10:52]** they're not they don't take into account time. They're just one after the other

**[10:54]** time. They're just one after the other

**[10:54]** time. They're just one after the other after the other. But there's obviously

**[10:56]** after the other. But there's obviously

**[10:56]** after the other. But there's obviously um a temporal uh way to look at this. So


### [11:00 - 12:00]

**[11:00]** um a temporal uh way to look at this. So

**[11:00]** um a temporal uh way to look at this. So this is the way that I like to think

**[11:02]** this is the way that I like to think

**[11:02]** this is the way that I like to think about it. And I know this is a little

**[11:03]** about it. And I know this is a little

**[11:03]** about it. And I know this is a little bit more of a complex graph to look at,

**[11:05]** bit more of a complex graph to look at,

**[11:05]** bit more of a complex graph to look at, but bear with me for a second. So on the

**[11:07]** but bear with me for a second. So on the

**[11:07]** but bear with me for a second. So on the left hand side, I'm talking about

**[11:08]** left hand side, I'm talking about

**[11:08]** left hand side, I'm talking about working set. So that's the number of

**[11:10]** working set. So that's the number of

**[11:10]** working set. So that's the number of tokens that the C system is holding in

**[11:13]** tokens that the C system is holding in

**[11:13]** tokens that the C system is holding in its memory based on different time to

**[11:16]** its memory based on different time to

**[11:16]** its memory based on different time to lives of the co of the actual C itself.

**[11:19]** lives of the co of the actual C itself.

**[11:19]** lives of the co of the actual C itself. And then the the bit at the top the

**[11:21]** And then the the bit at the top the

**[11:21]** And then the the bit at the top the dotted lines based on the right hand

**[11:23]** dotted lines based on the right hand

**[11:23]** dotted lines based on the right hand secondary access is showing the case hit

**[11:25]** secondary access is showing the case hit

**[11:25]** secondary access is showing the case hit rate as a result. So the red is showing

**[11:28]** rate as a result. So the red is showing

**[11:28]** rate as a result. So the red is showing one minute time to live. And what you

**[11:30]** one minute time to live. And what you

**[11:30]** one minute time to live. And what you can see is there's prompts here at the

**[11:32]** can see is there's prompts here at the

**[11:32]** can see is there's prompts here at the start on the left where the um it's

**[11:36]** start on the left where the um it's

**[11:36]** start on the left where the um it's thrashing up and down. And the reason

**[11:38]** thrashing up and down. And the reason

**[11:38]** thrashing up and down. And the reason it's doing that is the time between

**[11:41]** it's doing that is the time between

**[11:41]** it's doing that is the time between requests at that period is is longer

**[11:44]** requests at that period is is longer

**[11:44]** requests at that period is is longer than 1 minute. So you're getting a

**[11:47]** than 1 minute. So you're getting a

**[11:47]** than 1 minute. So you're getting a period where you might uh take the cash,

**[11:49]** period where you might uh take the cash,

**[11:49]** period where you might uh take the cash, get a hit or two, and then drop the cash

**[11:51]** get a hit or two, and then drop the cash

**[11:51]** get a hit or two, and then drop the cash and then you get another one. You got to

**[11:52]** and then you get another one. You got to

**[11:52]** and then you get another one. You got to refresh it. So it it just it doesn't

**[11:54]** refresh it. So it it just it doesn't

**[11:54]** refresh it. So it it just it doesn't really make sense, right? You go to 5

**[11:57]** really make sense, right? You go to 5

**[11:57]** really make sense, right? You go to 5 minutes, which is the blue, and you can

**[11:58]** minutes, which is the blue, and you can

**[11:58]** minutes, which is the blue, and you can now ride out more and more of those cash


### [12:00 - 13:00]

**[12:01]** now ride out more and more of those cash

**[12:01]** now ride out more and more of those cash hits, and as a result, you get a higher

**[12:02]** hits, and as a result, you get a higher

**[12:02]** hits, and as a result, you get a higher case hit rate. You can see it at that

**[12:04]** case hit rate. You can see it at that

**[12:04]** case hit rate. You can see it at that very start um up there uh comparing the

**[12:07]** very start um up there uh comparing the

**[12:07]** very start um up there uh comparing the two. But then you're still missing many

**[12:11]** two. But then you're still missing many

**[12:11]** two. But then you're still missing many others. There's still many times where

**[12:13]** others. There's still many times where

**[12:13]** others. There's still many times where the the time between a request is even

**[12:15]** the the time between a request is even

**[12:15]** the the time between a request is even larger. So the next one up is showing 1

**[12:18]** larger. So the next one up is showing 1

**[12:18]** larger. So the next one up is showing 1 hour. And while that requires the C

**[12:21]** hour. And while that requires the C

**[12:21]** hour. And while that requires the C system to hold uh you know a little bit

**[12:23]** system to hold uh you know a little bit

**[12:23]** system to hold uh you know a little bit more tokens in C and eventually quite a

**[12:26]** more tokens in C and eventually quite a

**[12:26]** more tokens in C and eventually quite a fair bit more tokens in C, it's got to

**[12:28]** fair bit more tokens in C, it's got to

**[12:28]** fair bit more tokens in C, it's got to hold it for a longer period of time. But

**[12:30]** hold it for a longer period of time. But

**[12:30]** hold it for a longer period of time. But the result to the end user is a better

**[12:33]** the result to the end user is a better

**[12:33]** the result to the end user is a better um actual experience and to the enterp

**[12:36]** um actual experience and to the enterp

**[12:36]** um actual experience and to the enterp to the uh inference provider which we'll

**[12:37]** to the uh inference provider which we'll

**[12:38]** to the uh inference provider which we'll show very shortly it's a much better

**[12:39]** show very shortly it's a much better

**[12:40]** show very shortly it's a much better experience for them as well. The problem

**[12:42]** experience for them as well. The problem

**[12:42]** experience for them as well. The problem though is to do that you need to be able

**[12:44]** though is to do that you need to be able

**[12:44]** though is to do that you need to be able to hold a lot of tokens in C and you

**[12:46]** to hold a lot of tokens in C and you

**[12:46]** to hold a lot of tokens in C and you need good memory tiers to support that.

**[12:49]** need good memory tiers to support that.

**[12:49]** need good memory tiers to support that. Um, so the next thing I want to go into

**[12:52]** Um, so the next thing I want to go into

**[12:52]** Um, so the next thing I want to go into is that a lot of people think of C hit

**[12:55]** is that a lot of people think of C hit

**[12:56]** is that a lot of people think of C hit rate isn't really something that a

**[12:58]** rate isn't really something that a

**[12:58]** rate isn't really something that a human's able to really internalize.


### [13:00 - 14:00]

**[13:00]** human's able to really internalize.

**[13:00]** human's able to really internalize. Well, so another way that I can

**[13:02]** Well, so another way that I can

**[13:02]** Well, so another way that I can visualize it is by thinking about it in

**[13:04]** visualize it is by thinking about it in

**[13:04]** visualize it is by thinking about it in terms of the number of times on average

**[13:07]** terms of the number of times on average

**[13:07]** terms of the number of times on average that a chunk of of tokens, which is a

**[13:09]** that a chunk of of tokens, which is a

**[13:09]** that a chunk of of tokens, which is a group of tokens, is refreshed. So in

**[13:12]** group of tokens, is refreshed. So in

**[13:12]** group of tokens, is refreshed. So in this particular conversation that we're

**[13:13]** this particular conversation that we're

**[13:13]** this particular conversation that we're looking at here, you can see that

**[13:15]** looking at here, you can see that

**[13:15]** looking at here, you can see that there's this is showing the relationship

**[13:16]** there's this is showing the relationship

**[13:16]** there's this is showing the relationship of as I increase the time to live or how

**[13:20]** of as I increase the time to live or how

**[13:20]** of as I increase the time to live or how that affects my case hit rate. But it

**[13:22]** that affects my case hit rate. But it

**[13:22]** that affects my case hit rate. But it also shows based on the secondary access

**[13:24]** also shows based on the secondary access

**[13:24]** also shows based on the secondary access that at 1 minute I'm literally re re uh

**[13:28]** that at 1 minute I'm literally re re uh

**[13:28]** that at 1 minute I'm literally re re uh prefilling like 15 16 times the same

**[13:31]** prefilling like 15 16 times the same

**[13:31]** prefilling like 15 16 times the same tokens. And over time we can get that

**[13:33]** tokens. And over time we can get that

**[13:33]** tokens. And over time we can get that all the way down to approaching one um

**[13:37]** all the way down to approaching one um

**[13:37]** all the way down to approaching one um and um make significant differences to

**[13:40]** and um make significant differences to

**[13:40]** and um make significant differences to again the experience of both the user

**[13:43]** again the experience of both the user

**[13:43]** again the experience of both the user and the inference provider.

**[13:46]** and the inference provider.

**[13:46]** and the inference provider. So with that what I'd like to do now is

**[13:48]** So with that what I'd like to do now is

**[13:48]** So with that what I'd like to do now is go into the the context engineering side

**[13:50]** go into the the context engineering side

**[13:50]** go into the the context engineering side of it, some of the lessons we learned

**[13:52]** of it, some of the lessons we learned

**[13:52]** of it, some of the lessons we learned and um just sort of really drive this

**[13:55]** and um just sort of really drive this

**[13:55]** and um just sort of really drive this home. So now I want you to think about

**[13:58]** home. So now I want you to think about

**[13:58]** home. So now I want you to think about uh what I think will be common in 2026


### [14:00 - 15:00]

**[14:00]** uh what I think will be common in 2026

**[14:00]** uh what I think will be common in 2026 and onwards of people hosting their own

**[14:03]** and onwards of people hosting their own

**[14:03]** and onwards of people hosting their own or having their own dedicated systems

**[14:05]** or having their own dedicated systems

**[14:05]** or having their own dedicated systems hosting for them. So imagine you being

**[14:07]** hosting for them. So imagine you being

**[14:07]** hosting for them. So imagine you being an inference provider now. Okay. So now

**[14:09]** an inference provider now. Okay. So now

**[14:09]** an inference provider now. Okay. So now what I want you to think of is think of

**[14:11]** what I want you to think of is think of

**[14:11]** what I want you to think of is think of yourself as an inference provider. Uh

**[14:13]** yourself as an inference provider. Uh

**[14:13]** yourself as an inference provider. Uh maybe you've um you've you know worked

**[14:15]** maybe you've um you've you know worked

**[14:15]** maybe you've um you've you know worked with us or one of our partners to build

**[14:17]** with us or one of our partners to build

**[14:17]** with us or one of our partners to build your own your own self-hosted instance

**[14:20]** your own your own self-hosted instance

**[14:20]** your own your own self-hosted instance um and uh you want to get the most out

**[14:22]** um and uh you want to get the most out

**[14:22]** um and uh you want to get the most out of it. What this graph is showing you is

**[14:25]** of it. What this graph is showing you is

**[14:25]** of it. What this graph is showing you is uh a relationship between a certain

**[14:27]** uh a relationship between a certain

**[14:27]** uh a relationship between a certain context length and the C hit rate and

**[14:30]** context length and the C hit rate and

**[14:30]** context length and the C hit rate and how many output tokens you get as a

**[14:32]** how many output tokens you get as a

**[14:32]** how many output tokens you get as a result of that C hit rate. Now the first

**[14:34]** result of that C hit rate. Now the first

**[14:34]** result of that C hit rate. Now the first thing you'll see is it's not linear and

**[14:36]** thing you'll see is it's not linear and

**[14:36]** thing you'll see is it's not linear and it it and the shape of this curve will

**[14:39]** it it and the shape of this curve will

**[14:39]** it it and the shape of this curve will change based on the context length based

**[14:41]** change based on the context length based

**[14:41]** change based on the context length based on the accelerators you use. B there's

**[14:44]** on the accelerators you use. B there's

**[14:44]** on the accelerators you use. B there's lots of things that come into it. how

**[14:45]** lots of things that come into it. how

**[14:45]** lots of things that come into it. how you do p disag and prefill. Uh there's a

**[14:49]** you do p disag and prefill. Uh there's a

**[14:49]** you do p disag and prefill. Uh there's a lot of stuff that comes into it, but the

**[14:51]** lot of stuff that comes into it, but the

**[14:51]** lot of stuff that comes into it, but the co the the curve is more or less the

**[14:53]** co the the curve is more or less the

**[14:53]** co the the curve is more or less the same. And if I asked you as an inference

**[14:55]** same. And if I asked you as an inference

**[14:55]** same. And if I asked you as an inference provider, where do you want to be? You'd

**[14:57]** provider, where do you want to be? You'd

**[14:57]** provider, where do you want to be? You'd obviously say C. And if you're in A or


### [15:00 - 16:00]

**[15:01]** obviously say C. And if you're in A or

**[15:01]** obviously say C. And if you're in A or B, you're you're not making money or

**[15:03]** B, you're you're not making money or

**[15:03]** B, you're you're not making money or you're not getting enough value out of

**[15:04]** you're not getting enough value out of

**[15:04]** you're not getting enough value out of the system. And inference providers that

**[15:06]** the system. And inference providers that

**[15:06]** the system. And inference providers that we work with that they they have the

**[15:08]** we work with that they they have the

**[15:08]** we work with that they they have the same answer obviously. So the question

**[15:10]** same answer obviously. So the question

**[15:10]** same answer obviously. So the question is, well, how do they keep in C? And

**[15:13]** is, well, how do they keep in C? And

**[15:13]** is, well, how do they keep in C? And this is where it goes back to a slide

**[15:15]** this is where it goes back to a slide

**[15:15]** this is where it goes back to a slide that um Bow showed earlier where what

**[15:19]** that um Bow showed earlier where what

**[15:19]** that um Bow showed earlier where what they're doing is they're incentivizing

**[15:20]** they're doing is they're incentivizing

**[15:20]** they're doing is they're incentivizing users to stay within C. And this is

**[15:24]** users to stay within C. And this is

**[15:24]** users to stay within C. And this is where we we came to the realization that

**[15:26]** where we we came to the realization that

**[15:26]** where we we came to the realization that a lot of the times because of how much C

**[15:29]** a lot of the times because of how much C

**[15:29]** a lot of the times because of how much C hit rate uh impacts your actual output.

**[15:33]** hit rate uh impacts your actual output.

**[15:33]** hit rate uh impacts your actual output. That's why it's you're buying case a

**[15:35]** That's why it's you're buying case a

**[15:35]** That's why it's you're buying case a lotments in storage when you're actually

**[15:37]** lotments in storage when you're actually

**[15:37]** lotments in storage when you're actually buying subscription services because it

**[15:39]** buying subscription services because it

**[15:39]** buying subscription services because it is so important to them that you stay in

**[15:42]** is so important to them that you stay in

**[15:42]** is so important to them that you stay in a certain case hit rate band especially

**[15:44]** a certain case hit rate band especially

**[15:44]** a certain case hit rate band especially for agentic workflows. Otherwise they

**[15:47]** for agentic workflows. Otherwise they

**[15:47]** for agentic workflows. Otherwise they literally you'll just melt the GPU

**[15:49]** literally you'll just melt the GPU

**[15:49]** literally you'll just melt the GPU clusters that they have. Um and I and I

**[15:52]** clusters that they have. Um and I and I

**[15:52]** clusters that they have. Um and I and I think it's a really powerful thing to to

**[15:54]** think it's a really powerful thing to to

**[15:54]** think it's a really powerful thing to to have in your head about how that works.

**[15:57]** have in your head about how that works.

**[15:57]** have in your head about how that works. So what we're going to do now is go

**[15:59]** So what we're going to do now is go

**[15:59]** So what we're going to do now is go through and think about okay what what


### [16:00 - 17:00]

**[16:01]** through and think about okay what what

**[16:01]** through and think about okay what what makes up this token storage.

**[16:05]** makes up this token storage.

**[16:05]** makes up this token storage. So when you think about the token

**[16:06]** So when you think about the token

**[16:06]** So when you think about the token storage there's lots of aspects that uh

**[16:10]** storage there's lots of aspects that uh

**[16:10]** storage there's lots of aspects that uh the memory tiers that support the token

**[16:12]** the memory tiers that support the token

**[16:12]** the memory tiers that support the token storage need to be able to do. But to

**[16:14]** storage need to be able to do. But to

**[16:14]** storage need to be able to do. But to really make it really really simple it's

**[16:17]** really make it really really simple it's

**[16:17]** really make it really really simple it's literally as as as simple as you need

**[16:20]** literally as as as simple as you need

**[16:20]** literally as as as simple as you need enough capacity in these memory tiers so

**[16:22]** enough capacity in these memory tiers so

**[16:22]** enough capacity in these memory tiers so that you can hold a optimal amount of

**[16:25]** that you can hold a optimal amount of

**[16:25]** that you can hold a optimal amount of cash. Uh if you think back to the the

**[16:28]** cash. Uh if you think back to the the

**[16:28]** cash. Uh if you think back to the the slides I just showed, there's this point

**[16:30]** slides I just showed, there's this point

**[16:30]** slides I just showed, there's this point where having more cash helps you a

**[16:32]** where having more cash helps you a

**[16:32]** where having more cash helps you a little bit, but it kind of gets to a

**[16:34]** little bit, but it kind of gets to a

**[16:34]** little bit, but it kind of gets to a point of diminishing returns. Um you

**[16:36]** point of diminishing returns. Um you

**[16:36]** point of diminishing returns. Um you need to get at least to that point and

**[16:39]** need to get at least to that point and

**[16:39]** need to get at least to that point and you need to be able to store extremely

**[16:41]** you need to be able to store extremely

**[16:41]** you need to be able to store extremely fast into it because if you can't,

**[16:42]** fast into it because if you can't,

**[16:42]** fast into it because if you can't, you're going to be able drop in KVs

**[16:44]** you're going to be able drop in KVs

**[16:44]** you're going to be able drop in KVs before they're in the memory tier or

**[16:46]** before they're in the memory tier or

**[16:46]** before they're in the memory tier or you're going to be blocking GPUs, which

**[16:47]** you're going to be blocking GPUs, which

**[16:47]** you're going to be blocking GPUs, which is probably even worse. And then the

**[16:50]** is probably even worse. And then the

**[16:50]** is probably even worse. And then the other way you need to do it is you need

**[16:51]** other way you need to do it is you need

**[16:51]** other way you need to do it is you need to be able to fetch from that token

**[16:53]** to be able to fetch from that token

**[16:53]** to be able to fetch from that token storage very very rapidly so that you

**[16:55]** storage very very rapidly so that you

**[16:55]** storage very very rapidly so that you can again not block the GPUs. They're

**[16:57]** can again not block the GPUs. They're

**[16:57]** can again not block the GPUs. They're the primary first class citizen of this

**[16:59]** the primary first class citizen of this

**[16:59]** the primary first class citizen of this whole system.


### [17:00 - 18:00]

**[17:01]** whole system.

**[17:01]** whole system. So what does it look like? So there's a

**[17:03]** So what does it look like? So there's a

**[17:03]** So what does it look like? So there's a few different types of memory tiers. The

**[17:04]** few different types of memory tiers. The

**[17:04]** few different types of memory tiers. The most common obviously is HBM and uh Val

**[17:07]** most common obviously is HBM and uh Val

**[17:07]** most common obviously is HBM and uh Val and I would love it if all our sessions

**[17:08]** and I would love it if all our sessions

**[17:08]** and I would love it if all our sessions are in HBM at all times. It's just not

**[17:11]** are in HBM at all times. It's just not

**[17:11]** are in HBM at all times. It's just not reasonable. Um there's many reasons for

**[17:13]** reasonable. Um there's many reasons for

**[17:13]** reasonable. Um there's many reasons for this around how the batch works which

**[17:15]** this around how the batch works which

**[17:15]** this around how the batch works which we're not going to go into today. But

**[17:17]** we're not going to go into today. But

**[17:17]** we're not going to go into today. But the point is is that the the the main

**[17:19]** the point is is that the the the main

**[17:19]** the point is is that the the the main common way that this is done today is

**[17:21]** common way that this is done today is

**[17:21]** common way that this is done today is DRAM. And there's nothing really wrong

**[17:23]** DRAM. And there's nothing really wrong

**[17:23]** DRAM. And there's nothing really wrong with DRAM as such. It it's sort of a

**[17:26]** with DRAM as such. It it's sort of a

**[17:26]** with DRAM as such. It it's sort of a means to an end, but it's quite limited

**[17:28]** means to an end, but it's quite limited

**[17:28]** means to an end, but it's quite limited in size. It's it's okay in terms of

**[17:30]** in size. It's it's okay in terms of

**[17:30]** in size. It's it's okay in terms of performance. But the other thing is it's

**[17:32]** performance. But the other thing is it's

**[17:32]** performance. But the other thing is it's tightly coupled with the compute. So if

**[17:34]** tightly coupled with the compute. So if

**[17:34]** tightly coupled with the compute. So if you want to expand your DRAM, there's

**[17:36]** you want to expand your DRAM, there's

**[17:36]** you want to expand your DRAM, there's not really many good ways to do that.

**[17:39]** not really many good ways to do that.

**[17:39]** not really many good ways to do that. There are some technologies out there

**[17:40]** There are some technologies out there

**[17:40]** There are some technologies out there that kind of do this, but the way

**[17:42]** that kind of do this, but the way

**[17:42]** that kind of do this, but the way they're implemented, they they kind of

**[17:43]** they're implemented, they they kind of

**[17:43]** they're implemented, they they kind of just hurt your performance. And that's

**[17:45]** just hurt your performance. And that's

**[17:45]** just hurt your performance. And that's what I'm showing with pulled DRAM. You

**[17:47]** what I'm showing with pulled DRAM. You

**[17:47]** what I'm showing with pulled DRAM. You could pull more together, but it's, you

**[17:49]** could pull more together, but it's, you

**[17:49]** could pull more together, but it's, you know, it's kind of a uh uh it doesn't

**[17:52]** know, it's kind of a uh uh it doesn't

**[17:52]** know, it's kind of a uh uh it doesn't help that much. So what we at Wcker um

**[17:56]** help that much. So what we at Wcker um

**[17:56]** help that much. So what we at Wcker um did is we took all the durable

**[17:59]** did is we took all the durable

**[17:59]** did is we took all the durable advantages of our product which has been


### [18:00 - 19:00]

**[18:01]** advantages of our product which has been

**[18:01]** advantages of our product which has been you know tried and tested in AI training

**[18:04]** you know tried and tested in AI training

**[18:04]** you know tried and tested in AI training in HBC environments and augmented memory

**[18:07]** in HBC environments and augmented memory

**[18:07]** in HBC environments and augmented memory grid is basically a uh supported um

**[18:11]** grid is basically a uh supported um

**[18:11]** grid is basically a uh supported um optimized connector between the

**[18:13]** optimized connector between the

**[18:13]** optimized connector between the inference systems and our um existing

**[18:16]** inference systems and our um existing

**[18:16]** inference systems and our um existing product. And because we're backed by

**[18:19]** product. And because we're backed by

**[18:19]** product. And because we're backed by NVMe we we're we're much denser. where

**[18:22]** NVMe we we're we're much denser. where

**[18:22]** NVMe we we're we're much denser. where like thousand times depending on how you

**[18:23]** like thousand times depending on how you

**[18:23]** like thousand times depending on how you look at it denser it's quite significant

**[18:26]** look at it denser it's quite significant

**[18:26]** look at it denser it's quite significant and then I show another example of a

**[18:28]** and then I show another example of a

**[18:28]** and then I show another example of a storage at the top there where you know

**[18:30]** storage at the top there where you know

**[18:30]** storage at the top there where you know not not something sluggish something

**[18:32]** not not something sluggish something

**[18:32]** not not something sluggish something that can still get 50 60 GB a second but

**[18:35]** that can still get 50 60 GB a second but

**[18:35]** that can still get 50 60 GB a second but uh and it has the capacity but still

**[18:38]** uh and it has the capacity but still

**[18:38]** uh and it has the capacity but still relative to what we're talking about is

**[18:40]** relative to what we're talking about is

**[18:40]** relative to what we're talking about is is still quite slow.

**[18:43]** is still quite slow.

**[18:43]** is still quite slow. Okay. So then moving on to how do we

**[18:46]** Okay. So then moving on to how do we

**[18:46]** Okay. So then moving on to how do we test this? So again, um we we talked

**[18:49]** test this? So again, um we we talked

**[18:49]** test this? So again, um we we talked about how we're we've open sourced this.

**[18:50]** about how we're we've open sourced this.

**[18:50]** about how we're we've open sourced this. Um basically, um Val already covered the

**[18:54]** Um basically, um Val already covered the

**[18:54]** Um basically, um Val already covered the the main part of it and that the fact

**[18:56]** the main part of it and that the fact

**[18:56]** the main part of it and that the fact that it it it acts like it's an

**[18:58]** that it it it acts like it's an

**[18:58]** that it it it acts like it's an inference provider. It's trying to keep

**[18:59]** inference provider. It's trying to keep

**[18:59]** inference provider. It's trying to keep the load within two SLOs's if you enable


### [19:00 - 20:00]

**[19:02]** the load within two SLOs's if you enable

**[19:02]** the load within two SLOs's if you enable them. You actually don't have to enable

**[19:04]** them. You actually don't have to enable

**[19:04]** them. You actually don't have to enable them and it'll just go as hard as it can

**[19:06]** them and it'll just go as hard as it can

**[19:06]** them and it'll just go as hard as it can regardless of of an SLO being time to

**[19:09]** regardless of of an SLO being time to

**[19:09]** regardless of of an SLO being time to first token or output tokens per

**[19:11]** first token or output tokens per

**[19:11]** first token or output tokens per request. But the main thing that it can

**[19:13]** request. But the main thing that it can

**[19:13]** request. But the main thing that it can do is you can either set a static number

**[19:16]** do is you can either set a static number

**[19:16]** do is you can either set a static number of coding agent users or you can um

**[19:20]** of coding agent users or you can um

**[19:20]** of coding agent users or you can um increase the number of those users over

**[19:22]** increase the number of those users over

**[19:22]** increase the number of those users over time so that you can slowly utilize more

**[19:26]** time so that you can slowly utilize more

**[19:26]** time so that you can slowly utilize more of the memory tiers and be able to

**[19:27]** of the memory tiers and be able to

**[19:27]** of the memory tiers and be able to compare different configurations.

**[19:30]** compare different configurations.

**[19:30]** compare different configurations. So there's two ways that it works. Um

**[19:33]** So there's two ways that it works. Um

**[19:33]** So there's two ways that it works. Um I'll just be quick through these

**[19:34]** I'll just be quick through these

**[19:34]** I'll just be quick through these sections because you can read about

**[19:35]** sections because you can read about

**[19:35]** sections because you can read about this. I have a blog that explains how I

**[19:38]** this. I have a blog that explains how I

**[19:38]** this. I have a blog that explains how I do the testing that goes through all of

**[19:39]** do the testing that goes through all of

**[19:40]** do the testing that goes through all of this in detail. And there's obviously

**[19:41]** this in detail. And there's obviously

**[19:41]** this in detail. And there's obviously the GitHub as well, but basically it can

**[19:45]** the GitHub as well, but basically it can

**[19:45]** the GitHub as well, but basically it can do the initial working set and then

**[19:47]** do the initial working set and then

**[19:47]** do the initial working set and then sequentially go through those prompts.

**[19:49]** sequentially go through those prompts.

**[19:49]** sequentially go through those prompts. So this will be very very very

**[19:51]** So this will be very very very

**[19:51]** So this will be very very very deterministic because as soon as you

**[19:52]** deterministic because as soon as you

**[19:52]** deterministic because as soon as you over overflow the memory tier even the

**[19:55]** over overflow the memory tier even the

**[19:55]** over overflow the memory tier even the slightest bit, you'll see a massive drop

**[19:57]** slightest bit, you'll see a massive drop

**[19:57]** slightest bit, you'll see a massive drop off in performance. But the other way

**[19:59]** off in performance. But the other way


### [20:00 - 21:00]

**[20:00]** off in performance. But the other way that it can be done and realistically

**[20:01]** that it can be done and realistically

**[20:01]** that it can be done and realistically the more fair way that it can be done is

**[20:03]** the more fair way that it can be done is

**[20:03]** the more fair way that it can be done is you can ex increase the size over time.

**[20:06]** you can ex increase the size over time.

**[20:06]** you can ex increase the size over time. So the amount of concurrent users that

**[20:07]** So the amount of concurrent users that

**[20:07]** So the amount of concurrent users that you're accessing out of a pool and you

**[20:10]** you're accessing out of a pool and you

**[20:10]** you're accessing out of a pool and you can randomly sample where in that sample

**[20:13]** can randomly sample where in that sample

**[20:14]** can randomly sample where in that sample set you'll get that uh prompt from. So

**[20:16]** set you'll get that uh prompt from. So

**[20:16]** set you'll get that uh prompt from. So sometimes you might be hitting HPM,

**[20:18]** sometimes you might be hitting HPM,

**[20:18]** sometimes you might be hitting HPM, sometimes you might be hitting your your

**[20:20]** sometimes you might be hitting your your

**[20:20]** sometimes you might be hitting your your memory tier 2. Let's say that let's say

**[20:21]** memory tier 2. Let's say that let's say

**[20:21]** memory tier 2. Let's say that let's say that's DAM and you get a really nice

**[20:23]** that's DAM and you get a really nice

**[20:24]** that's DAM and you get a really nice blended number.

**[20:26]** blended number.

**[20:26]** blended number. So with that, let's go in and tell show

**[20:29]** So with that, let's go in and tell show

**[20:29]** So with that, let's go in and tell show you some results and just sort of

**[20:30]** you some results and just sort of

**[20:30]** you some results and just sort of explain and and show why we're so

**[20:33]** explain and and show why we're so

**[20:33]** explain and and show why we're so excited about what we're talking about

**[20:35]** excited about what we're talking about

**[20:35]** excited about what we're talking about today.

**[20:36]** today.

**[20:36]** today. So this showing three comparisons.

**[20:38]** So this showing three comparisons.

**[20:38]** So this showing three comparisons. Comparison number one is HBM with weter.

**[20:41]** Comparison number one is HBM with weter.

**[20:41]** Comparison number one is HBM with weter. That's the purple. Uh there's orange

**[20:43]** That's the purple. Uh there's orange

**[20:43]** That's the purple. Uh there's orange which is HBM and DRAM. And there's the

**[20:45]** which is HBM and DRAM. And there's the

**[20:45]** which is HBM and DRAM. And there's the you know orangey pinky color with uh HBM

**[20:48]** you know orangey pinky color with uh HBM

**[20:48]** you know orangey pinky color with uh HBM plus DRAM plus that uh other uh posics

**[20:52]** plus DRAM plus that uh other uh posics

**[20:52]** plus DRAM plus that uh other uh posics system that I talked about earlier. The

**[20:54]** system that I talked about earlier. The

**[20:54]** system that I talked about earlier. The dotted line is showing uh concurrent

**[20:56]** dotted line is showing uh concurrent

**[20:56]** dotted line is showing uh concurrent users. So the amount the amount of users

**[20:59]** users. So the amount the amount of users

**[20:59]** users. So the amount the amount of users that are in a pool and that's increasing


### [21:00 - 22:00]

**[21:01]** that are in a pool and that's increasing

**[21:01]** that are in a pool and that's increasing over time. So in the initial shaded area

**[21:05]** over time. So in the initial shaded area

**[21:05]** over time. So in the initial shaded area you can see that all three of them get

**[21:07]** you can see that all three of them get

**[21:07]** you can see that all three of them get an advantage of HBM. The primary uh hit

**[21:10]** an advantage of HBM. The primary uh hit

**[21:10]** an advantage of HBM. The primary uh hit out of uh C hit rate is coming out of

**[21:13]** out of uh C hit rate is coming out of

**[21:13]** out of uh C hit rate is coming out of HBM. But then over time as we increase

**[21:16]** HBM. But then over time as we increase

**[21:16]** HBM. But then over time as we increase the users more and more and more you're

**[21:18]** the users more and more and more you're

**[21:18]** the users more and more and more you're overflowing what the DRAM system what

**[21:20]** overflowing what the DRAM system what

**[21:20]** overflowing what the DRAM system what the DRAM memory tier can do and both

**[21:23]** the DRAM memory tier can do and both

**[21:23]** the DRAM memory tier can do and both orange and the pinky color start to drop

**[21:26]** orange and the pinky color start to drop

**[21:26]** orange and the pinky color start to drop off quite dramatically. Um we also from

**[21:29]** off quite dramatically. Um we also from

**[21:29]** off quite dramatically. Um we also from a wcker perspective also drop off

**[21:30]** a wcker perspective also drop off

**[21:30]** a wcker perspective also drop off because we get less and less advantage

**[21:32]** because we get less and less advantage

**[21:32]** because we get less and less advantage from HBM. So we have to uh pull back our

**[21:35]** from HBM. So we have to uh pull back our

**[21:35]** from HBM. So we have to uh pull back our concurrency a little bit. The system

**[21:37]** concurrency a little bit. The system

**[21:37]** concurrency a little bit. The system does automatically the uh the

**[21:39]** does automatically the uh the

**[21:39]** does automatically the uh the benchmarking tool. But then once we've

**[21:41]** benchmarking tool. But then once we've

**[21:41]** benchmarking tool. But then once we've sort of got down to the steady state,

**[21:43]** sort of got down to the steady state,

**[21:43]** sort of got down to the steady state, all three start to like um level out a

**[21:46]** all three start to like um level out a

**[21:46]** all three start to like um level out a little bit. But the main difference is

**[21:49]** little bit. But the main difference is

**[21:49]** little bit. But the main difference is is that once you get down to that steady

**[21:51]** is that once you get down to that steady

**[21:51]** is that once you get down to that steady state, we can maintain that at a much

**[21:54]** state, we can maintain that at a much

**[21:54]** state, we can maintain that at a much higher amount of users at a much higher

**[21:57]** higher amount of users at a much higher

**[21:57]** higher amount of users at a much higher amount of output tokens.


### [22:00 - 23:00]

**[22:00]** amount of output tokens.

**[22:00]** amount of output tokens. The other way that you look at this is

**[22:02]** The other way that you look at this is

**[22:02]** The other way that you look at this is um that was a decode focused role. Um if

**[22:05]** um that was a decode focused role. Um if

**[22:05]** um that was a decode focused role. Um if you look at a pre-fill focus ro if

**[22:07]** you look at a pre-fill focus ro if

**[22:07]** you look at a pre-fill focus ro if you're doing disag prefill um then the

**[22:10]** you're doing disag prefill um then the

**[22:10]** you're doing disag prefill um then the prefill is actually even better result

**[22:12]** prefill is actually even better result

**[22:12]** prefill is actually even better result for us because the systems the GPUs are

**[22:15]** for us because the systems the GPUs are

**[22:15]** for us because the systems the GPUs are so much more efficient when you're doing

**[22:17]** so much more efficient when you're doing

**[22:17]** so much more efficient when you're doing large um batches of pre-fill tokens with

**[22:20]** large um batches of pre-fill tokens with

**[22:20]** large um batches of pre-fill tokens with a single decode. Um then we we can

**[22:24]** a single decode. Um then we we can

**[22:24]** a single decode. Um then we we can basically saturate things more fairly

**[22:27]** basically saturate things more fairly

**[22:27]** basically saturate things more fairly and um and it continues. Now the main

**[22:30]** and um and it continues. Now the main

**[22:30]** and um and it continues. Now the main difference between pink and orange is

**[22:32]** difference between pink and orange is

**[22:32]** difference between pink and orange is that we uh sorry purple and orange is

**[22:36]** that we uh sorry purple and orange is

**[22:36]** that we uh sorry purple and orange is that we have a lot more cash. So we can

**[22:38]** that we have a lot more cash. So we can

**[22:38]** that we have a lot more cash. So we can hit a lot more. The interesting thing

**[22:40]** hit a lot more. The interesting thing

**[22:40]** hit a lot more. The interesting thing about the orangey pinky color is that it

**[22:42]** about the orangey pinky color is that it

**[22:42]** about the orangey pinky color is that it also has the ability to hit every single

**[22:44]** also has the ability to hit every single

**[22:44]** also has the ability to hit every single thing that it's possible but it's not

**[22:47]** thing that it's possible but it's not

**[22:47]** thing that it's possible but it's not fast enough to get it into the GPU for

**[22:49]** fast enough to get it into the GPU for

**[22:49]** fast enough to get it into the GPU for it to make a difference. And that's why

**[22:51]** it to make a difference. And that's why

**[22:51]** it to make a difference. And that's why we're sort of showing the difference

**[22:52]** we're sort of showing the difference

**[22:52]** we're sort of showing the difference between these three because with purple

**[22:55]** between these three because with purple

**[22:55]** between these three because with purple you're getting the advantage of capacity

**[22:56]** you're getting the advantage of capacity

**[22:56]** you're getting the advantage of capacity but at DM speeds so you can maintain

**[22:58]** but at DM speeds so you can maintain

**[22:58]** but at DM speeds so you can maintain that benefit longer periods of time


### [23:00 - 24:00]

**[23:05]** and then maybe Val I'll hand back to

**[23:05]** and then maybe Val I'll hand back to you.

**[23:07]** you.

**[23:07]** you. >> Absolutely. That was a great walk

**[23:09]** >> Absolutely. That was a great walk

**[23:09]** >> Absolutely. That was a great walk through Ken of all of your research and

**[23:10]** through Ken of all of your research and

**[23:10]** through Ken of all of your research and benchmark results in WA labs. So once

**[23:13]** benchmark results in WA labs. So once

**[23:13]** benchmark results in WA labs. So once again we're thrilled to be announcing

**[23:14]** again we're thrilled to be announcing

**[23:14]** again we're thrilled to be announcing the open sourcing of this context

**[23:16]** the open sourcing of this context

**[23:16]** the open sourcing of this context platform engineering toolkit today.

**[23:18]** platform engineering toolkit today.

**[23:18]** platform engineering toolkit today. Please do download it, use it, give us

**[23:20]** Please do download it, use it, give us

**[23:20]** Please do download it, use it, give us your feedback. Again, feel free to fork

**[23:22]** your feedback. Again, feel free to fork

**[23:22]** your feedback. Again, feel free to fork it and improve it yourself. And we look

**[23:24]** it and improve it yourself. And we look

**[23:24]** it and improve it yourself. And we look forward together just contributing to

**[23:26]** forward together just contributing to

**[23:26]** forward together just contributing to less token anxiety overall, less prompt

**[23:29]** less token anxiety overall, less prompt

**[23:29]** less token anxiety overall, less prompt cash arbitrage and more context and

**[23:31]** cash arbitrage and more context and

**[23:31]** cash arbitrage and more context and context platform engineering in the

**[23:33]** context platform engineering in the

**[23:33]** context platform engineering in the future. A nice QR code for you to find

**[23:36]** future. A nice QR code for you to find

**[23:36]** future. A nice QR code for you to find out even more information. And at the

**[23:38]** out even more information. And at the

**[23:38]** out even more information. And at the end of this video in um in the actual

**[23:40]** end of this video in um in the actual

**[23:40]** end of this video in um in the actual transcript section and so forth,

**[23:42]** transcript section and so forth,

**[23:42]** transcript section and so forth, there'll be links to all the blogs we

**[23:43]** there'll be links to all the blogs we

**[23:43]** there'll be links to all the blogs we referenced here. So, thank you for

**[23:45]** referenced here. So, thank you for

**[23:45]** referenced here. So, thank you for joining us today and we look forward to

**[23:47]** joining us today and we look forward to

**[23:47]** joining us today and we look forward to pairing on the context platform

**[23:49]** pairing on the context platform

**[23:49]** pairing on the context platform engineering conversation with you in the

**[23:50]** engineering conversation with you in the

**[23:50]** engineering conversation with you in the future.


