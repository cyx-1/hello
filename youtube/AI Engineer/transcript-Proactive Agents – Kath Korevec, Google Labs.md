# Proactive Agents – Kath Korevec, Google Labs

**Video URL:** https://www.youtube.com/watch?v=v3u8xc0zLec

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** I'm so excited to be here. I love New

**[00:23]** I'm so excited to be here. I love New York and I love meeting everybody here.

**[00:26]** York and I love meeting everybody here.

**[00:26]** York and I love meeting everybody here. And I am Kath Corbec. I'm from Google

**[00:29]** And I am Kath Corbec. I'm from Google

**[00:29]** And I am Kath Corbec. I'm from Google Labs and I work on this little team

**[00:31]** Labs and I work on this little team

**[00:31]** Labs and I work on this little team called ADA and I'm going to be talking

**[00:32]** called ADA and I'm going to be talking

**[00:32]** called ADA and I'm going to be talking about some of the stuff that we've been

**[00:33]** about some of the stuff that we've been

**[00:33]** about some of the stuff that we've been doing on this project called Jewels. So,

**[00:37]** doing on this project called Jewels. So,

**[00:37]** doing on this project called Jewels. So, a few months ago in my household, our

**[00:39]** a few months ago in my household, our

**[00:39]** a few months ago in my household, our dishwasher broke. And while it was being

**[00:41]** dishwasher broke. And while it was being

**[00:41]** dishwasher broke. And while it was being repaired, my husband decided that he was

**[00:44]** repaired, my husband decided that he was

**[00:44]** repaired, my husband decided that he was going to do all the dishes. And so, he

**[00:45]** going to do all the dishes. And so, he

**[00:45]** going to do all the dishes. And so, he told me he was going to do this. But

**[00:47]** told me he was going to do this. But

**[00:47]** told me he was going to do this. But every single night, I found myself

**[00:49]** every single night, I found myself

**[00:49]** every single night, I found myself reminding him to do the dishes. And you

**[00:51]** reminding him to do the dishes. And you

**[00:51]** reminding him to do the dishes. And you can imagine that got old pretty fast.

**[00:54]** can imagine that got old pretty fast.

**[00:54]** can imagine that got old pretty fast. And I realized that even though I wasn't

**[00:56]** And I realized that even though I wasn't

**[00:56]** And I realized that even though I wasn't physically washing the dishes, I was

**[00:58]** physically washing the dishes, I was

**[00:58]** physically washing the dishes, I was still carrying this mental load. And I


### [01:00 - 02:00]

**[01:00]** still carrying this mental load. And I

**[01:00]** still carrying this mental load. And I know a lot of you can probably relate to

**[01:01]** know a lot of you can probably relate to

**[01:01]** know a lot of you can probably relate to this. I was keeping track of whether or

**[01:03]** this. I was keeping track of whether or

**[01:03]** this. I was keeping track of whether or not that task was done, following up,

**[01:06]** not that task was done, following up,

**[01:06]** not that task was done, following up, making sure that things kept moving. And

**[01:09]** making sure that things kept moving. And

**[01:09]** making sure that things kept moving. And I realized in that moment that that's

**[01:10]** I realized in that moment that that's

**[01:10]** I realized in that moment that that's exactly where we are with asynchronous

**[01:13]** exactly where we are with asynchronous

**[01:13]** exactly where we are with asynchronous agents today. They can handle some of

**[01:15]** agents today. They can handle some of

**[01:15]** agents today. They can handle some of the work, but we're still the ones as

**[01:17]** the work, but we're still the ones as

**[01:17]** the work, but we're still the ones as developers carrying that mental load and

**[01:19]** developers carrying that mental load and

**[01:19]** developers carrying that mental load and monitoring them. So here's the truth.

**[01:23]** monitoring them. So here's the truth.

**[01:23]** monitoring them. So here's the truth. Humans, we are serial processors, not

**[01:26]** Humans, we are serial processors, not

**[01:26]** Humans, we are serial processors, not parallel ones. We can juggle multiple

**[01:29]** parallel ones. We can juggle multiple

**[01:29]** parallel ones. We can juggle multiple goals, but we execute them in sequence,

**[01:32]** goals, but we execute them in sequence,

**[01:32]** goals, but we execute them in sequence, not all at once. When you manually kick

**[01:34]** not all at once. When you manually kick

**[01:34]** not all at once. When you manually kick off a task in jewels, you're usually

**[01:36]** off a task in jewels, you're usually

**[01:36]** off a task in jewels, you're usually waiting to be able to move on. And it's

**[01:40]** waiting to be able to move on. And it's

**[01:40]** waiting to be able to move on. And it's that pause, it's that gap in attention

**[01:41]** that pause, it's that gap in attention

**[01:41]** that pause, it's that gap in attention where we really lose momentum. And this

**[01:44]** where we really lose momentum. And this

**[01:44]** where we really lose momentum. And this is actually backed up by science where

**[01:47]** is actually backed up by science where

**[01:47]** is actually backed up by science where uh humans actually think we think we're

**[01:49]** uh humans actually think we think we're

**[01:49]** uh humans actually think we think we're multitaskers but we're actually

**[01:51]** multitaskers but we're actually

**[01:51]** multitaskers but we're actually executing many tasks very rapidly. But

**[01:55]** executing many tasks very rapidly. But

**[01:55]** executing many tasks very rapidly. But switching between these tasks comes with

**[01:57]** switching between these tasks comes with

**[01:57]** switching between these tasks comes with a huge cost. It can cost up to 40% of


### [02:00 - 03:00]

**[02:00]** a huge cost. It can cost up to 40% of

**[02:00]** a huge cost. It can cost up to 40% of your productive time. So that's like

**[02:02]** your productive time. So that's like

**[02:02]** your productive time. So that's like half a day lost to switching contexts

**[02:05]** half a day lost to switching contexts

**[02:05]** half a day lost to switching contexts and reloading. So if humans are uniters,

**[02:11]** and reloading. So if humans are uniters,

**[02:11]** and reloading. So if humans are uniters, what's the solution here with agents? So

**[02:13]** what's the solution here with agents? So

**[02:13]** what's the solution here with agents? So for async agents, in order in order for

**[02:15]** for async agents, in order in order for

**[02:15]** for async agents, in order in order for them to succeed, developers can't be

**[02:18]** them to succeed, developers can't be

**[02:18]** them to succeed, developers can't be expected to babysit them.

**[02:21]** expected to babysit them.

**[02:21]** expected to babysit them. We've all seen that post on Twitter of

**[02:23]** We've all seen that post on Twitter of

**[02:23]** We've all seen that post on Twitter of 16 different cloud code tasks running in

**[02:26]** 16 different cloud code tasks running in

**[02:26]** 16 different cloud code tasks running in parallel on 16 different terminals on

**[02:28]** parallel on 16 different terminals on

**[02:28]** parallel on 16 different terminals on three different huge browsers or huge

**[02:31]** three different huge browsers or huge

**[02:31]** three different huge browsers or huge monitors. And when I first saw this, I

**[02:33]** monitors. And when I first saw this, I

**[02:33]** monitors. And when I first saw this, I thought, God forbid that is the DevX of

**[02:35]** thought, God forbid that is the DevX of

**[02:35]** thought, God forbid that is the DevX of the future. I want to I don't want to

**[02:38]** the future. I want to I don't want to

**[02:38]** the future. I want to I don't want to manage work. I don't want to manage my

**[02:40]** manage work. I don't want to manage my

**[02:40]** manage work. I don't want to manage my agents. I want to be a coder. I want to

**[02:42]** agents. I want to be a coder. I want to

**[02:42]** agents. I want to be a coder. I want to build. And so, we need to think we need

**[02:45]** build. And so, we need to think we need

**[02:45]** build. And so, we need to think we need uh uh collaborators in our system that

**[02:48]** uh uh collaborators in our system that

**[02:48]** uh uh collaborators in our system that we can trust. Agents that really

**[02:50]** we can trust. Agents that really

**[02:50]** we can trust. Agents that really understand context, can anticipate our

**[02:53]** understand context, can anticipate our

**[02:53]** understand context, can anticipate our needs, and they know really when to step

**[02:55]** needs, and they know really when to step

**[02:55]** needs, and they know really when to step in. And then uh I think finally we're

**[02:59]** in. And then uh I think finally we're

**[02:59]** in. And then uh I think finally we're reaching that point with models where


### [03:00 - 04:00]

**[03:00]** reaching that point with models where

**[03:00]** reaching that point with models where they're getting better and better at

**[03:02]** they're getting better and better at

**[03:02]** they're getting better and better at executing end to end as long as they

**[03:05]** executing end to end as long as they

**[03:05]** executing end to end as long as they understand what our goals are clearly.

**[03:08]** understand what our goals are clearly.

**[03:08]** understand what our goals are clearly. And that's where trust really becomes

**[03:09]** And that's where trust really becomes

**[03:09]** And that's where trust really becomes this unlock where you can trust the

**[03:12]** this unlock where you can trust the

**[03:12]** this unlock where you can trust the system to know what's missing to fill in

**[03:14]** system to know what's missing to fill in

**[03:14]** system to know what's missing to fill in the gaps and to really keep progress

**[03:17]** the gaps and to really keep progress

**[03:17]** the gaps and to really keep progress moving forward while you manage on

**[03:19]** moving forward while you manage on

**[03:19]** moving forward while you manage on something else where where while you

**[03:20]** something else where where while you

**[03:20]** something else where where while you focus on what matters most. And

**[03:22]** focus on what matters most. And

**[03:22]** focus on what matters most. And essentially we want jewels to do the

**[03:24]** essentially we want jewels to do the

**[03:24]** essentially we want jewels to do the dishes without being asked.

**[03:26]** dishes without being asked.

**[03:26]** dishes without being asked. So most AI developer tools today are

**[03:28]** So most AI developer tools today are

**[03:28]** So most AI developer tools today are fundamentally reactive. You open up your

**[03:31]** fundamentally reactive. You open up your

**[03:31]** fundamentally reactive. You open up your CLI or your ID and you ask the agent to

**[03:33]** CLI or your ID and you ask the agent to

**[03:33]** CLI or your ID and you ask the agent to do something and it responds or it waits

**[03:35]** do something and it responds or it waits

**[03:35]** do something and it responds or it waits for you to start typing and then it

**[03:37]** for you to start typing and then it

**[03:37]** for you to start typing and then it autocompletes a suggestion. And there's

**[03:39]** autocompletes a suggestion. And there's

**[03:39]** autocompletes a suggestion. And there's a benefit to this model. It's very

**[03:41]** a benefit to this model. It's very

**[03:41]** a benefit to this model. It's very efficient. It only uses compute when you

**[03:44]** efficient. It only uses compute when you

**[03:44]** efficient. It only uses compute when you explicitly ask for it. But the real

**[03:46]** explicitly ask for it. But the real

**[03:46]** explicitly ask for it. But the real question I'm asking myself is is this

**[03:48]** question I'm asking myself is is this

**[03:48]** question I'm asking myself is is this how I want to manage AI? And if you

**[03:50]** how I want to manage AI? And if you

**[03:50]** how I want to manage AI? And if you think about in the future, imagine a

**[03:52]** think about in the future, imagine a

**[03:52]** think about in the future, imagine a world where compute is not a limiting

**[03:55]** world where compute is not a limiting

**[03:55]** world where compute is not a limiting factor anymore. Instead of a single

**[03:57]** factor anymore. Instead of a single

**[03:57]** factor anymore. Instead of a single reactive assistant for instructions, you


### [04:00 - 05:00]

**[04:00]** reactive assistant for instructions, you

**[04:00]** reactive assistant for instructions, you could have dozens of small proactive

**[04:02]** could have dozens of small proactive

**[04:02]** could have dozens of small proactive agents working with you in parallel,

**[04:04]** agents working with you in parallel,

**[04:04]** agents working with you in parallel, quietly looking for patterns, noticing

**[04:07]** quietly looking for patterns, noticing

**[04:07]** quietly looking for patterns, noticing friction, and taking on the boring tasks

**[04:10]** friction, and taking on the boring tasks

**[04:10]** friction, and taking on the boring tasks that you don't want to do before you

**[04:12]** that you don't want to do before you

**[04:12]** that you don't want to do before you even ask. It can do things like fixing

**[04:15]** even ask. It can do things like fixing

**[04:15]** even ask. It can do things like fixing authentication bugs that you've been

**[04:17]** authentication bugs that you've been

**[04:17]** authentication bugs that you've been avoiding, uh, updating configs, flagging

**[04:20]** avoiding, uh, updating configs, flagging

**[04:20]** avoiding, uh, updating configs, flagging potential order, uh, errors, preparing,

**[04:23]** potential order, uh, errors, preparing,

**[04:23]** potential order, uh, errors, preparing, uh, migrations, and all of this can

**[04:25]** uh, migrations, and all of this can

**[04:25]** uh, migrations, and all of this can happen in the background triggered off

**[04:27]** happen in the background triggered off

**[04:27]** happen in the background triggered off of things in my natural workflow. So, I

**[04:30]** of things in my natural workflow. So, I

**[04:30]** of things in my natural workflow. So, I really think there are four essential

**[04:31]** really think there are four essential

**[04:32]** really think there are four essential ingredients that make up proactive

**[04:33]** ingredients that make up proactive

**[04:33]** ingredients that make up proactive systems today. There's observation. The

**[04:35]** systems today. There's observation. The

**[04:36]** systems today. There's observation. The agent has to really continually

**[04:37]** agent has to really continually

**[04:37]** agent has to really continually understand what is happening and of what

**[04:40]** understand what is happening and of what

**[04:40]** understand what is happening and of what your code changes are, what your

**[04:42]** your code changes are, what your

**[04:42]** your code changes are, what your patterns are, what your workflow is,

**[04:43]** patterns are, what your workflow is,

**[04:43]** patterns are, what your workflow is, etc. to get context about your entire

**[04:45]** etc. to get context about your entire

**[04:45]** etc. to get context about your entire project. And then there's

**[04:47]** project. And then there's

**[04:47]** project. And then there's personalization. And this one's

**[04:48]** personalization. And this one's

**[04:48]** personalization. And this one's difficult. It has to learn how you work,

**[04:50]** difficult. It has to learn how you work,

**[04:50]** difficult. It has to learn how you work, what you care about, what you tend to

**[04:52]** what you care about, what you tend to

**[04:52]** what you care about, what you tend to ignore, what your preferences are, the

**[04:54]** ignore, what your preferences are, the

**[04:54]** ignore, what your preferences are, the code that you absolutely don't want to

**[04:55]** code that you absolutely don't want to

**[04:55]** code that you absolutely don't want to ever touch. And then it has to be timely

**[04:57]** ever touch. And then it has to be timely

**[04:57]** ever touch. And then it has to be timely as well. If it comes in too soon, it's

**[04:59]** as well. If it comes in too soon, it's

**[04:59]** as well. If it comes in too soon, it's going to interrupt you. And if it's too


### [05:00 - 06:00]

**[05:01]** going to interrupt you. And if it's too

**[05:01]** going to interrupt you. And if it's too late, then the moment is lost. And it

**[05:03]** late, then the moment is lost. And it

**[05:03]** late, then the moment is lost. And it also has to work seamlessly across your

**[05:05]** also has to work seamlessly across your

**[05:05]** also has to work seamlessly across your workflow. It has to insert itself into

**[05:08]** workflow. It has to insert itself into

**[05:08]** workflow. It has to insert itself into spaces where you naturally work already

**[05:10]** spaces where you naturally work already

**[05:10]** spaces where you naturally work already in your terminal, in your repository, in

**[05:12]** in your terminal, in your repository, in

**[05:12]** in your terminal, in your repository, in your IDE, not forcing you to go

**[05:15]** your IDE, not forcing you to go

**[05:15]** your IDE, not forcing you to go somewhere else to some application

**[05:16]** somewhere else to some application

**[05:16]** somewhere else to some application that's secret or that you forgot about.

**[05:18]** that's secret or that you forgot about.

**[05:18]** that's secret or that you forgot about. So bringing all these tools together,

**[05:20]** So bringing all these tools together,

**[05:20]** So bringing all these tools together, you can imagine, is not trivial.

**[05:25]** you can imagine, is not trivial.

**[05:25]** you can imagine, is not trivial. [laughter]

**[05:26]** [laughter]

**[05:26]** [laughter] >> So is running this presentation. Um, and

**[05:29]** >> So is running this presentation. Um, and

**[05:29]** >> So is running this presentation. Um, and uh, you you want to be able to ask your

**[05:32]** uh, you you want to be able to ask your

**[05:32]** uh, you you want to be able to ask your agent to understand your workflow and

**[05:34]** agent to understand your workflow and

**[05:34]** agent to understand your workflow and anticipate your needs and then intervene

**[05:37]** anticipate your needs and then intervene

**[05:37]** anticipate your needs and then intervene at exactly the right moment without

**[05:39]** at exactly the right moment without

**[05:39]** at exactly the right moment without breaking your workflow.

**[05:41]** breaking your workflow.

**[05:41]** breaking your workflow. And that's when it really starts to feel

**[05:43]** And that's when it really starts to feel

**[05:43]** And that's when it really starts to feel like magic. The interesting thing is pro

**[05:45]** like magic. The interesting thing is pro

**[05:46]** like magic. The interesting thing is pro these proactive systems, they're all

**[05:47]** these proactive systems, they're all

**[05:47]** these proactive systems, they're all around us today. One of my favorite

**[05:48]** around us today. One of my favorite

**[05:48]** around us today. One of my favorite examples is Google Nest where you put it

**[05:51]** examples is Google Nest where you put it

**[05:51]** examples is Google Nest where you put it in your house, you install it, and then

**[05:53]** in your house, you install it, and then

**[05:53]** in your house, you install it, and then you configure it, and then it starts to

**[05:56]** you configure it, and then it starts to

**[05:56]** you configure it, and then it starts to learn your habits as you leave the

**[05:58]** learn your habits as you leave the

**[05:58]** learn your habits as you leave the house, as you come back, uh, as you go


### [06:00 - 07:00]

**[06:00]** house, as you come back, uh, as you go

**[06:00]** house, as you come back, uh, as you go to sleep, as you wake up in the morning.

**[06:02]** to sleep, as you wake up in the morning.

**[06:02]** to sleep, as you wake up in the morning. And then pretty soon, you don't have to

**[06:03]** And then pretty soon, you don't have to

**[06:04]** And then pretty soon, you don't have to think about climate control in your

**[06:05]** think about climate control in your

**[06:05]** think about climate control in your house anymore because it's learned what

**[06:06]** house anymore because it's learned what

**[06:06]** house anymore because it's learned what your habits are. Another one is your own

**[06:09]** your habits are. Another one is your own

**[06:09]** your habits are. Another one is your own body. your heart rate elevates as you go

**[06:11]** body. your heart rate elevates as you go

**[06:11]** body. your heart rate elevates as you go for a run or start to work out or it

**[06:14]** for a run or start to work out or it

**[06:14]** for a run or start to work out or it anticipates that you're about to fall

**[06:16]** anticipates that you're about to fall

**[06:16]** anticipates that you're about to fall and so it reacts before you consciously

**[06:18]** and so it reacts before you consciously

**[06:18]** and so it reacts before you consciously think I'm going to put my hand out. So

**[06:20]** think I'm going to put my hand out. So

**[06:20]** think I'm going to put my hand out. So when you look at it like that

**[06:22]** when you look at it like that

**[06:22]** when you look at it like that proactivity is actually not that

**[06:24]** proactivity is actually not that

**[06:24]** proactivity is actually not that proactivity for AI is actually not that

**[06:26]** proactivity for AI is actually not that

**[06:26]** proactivity for AI is actually not that futuristic. It's very familiar and it is

**[06:29]** futuristic. It's very familiar and it is

**[06:29]** futuristic. It's very familiar and it is very human and that's exactly the point.

**[06:32]** very human and that's exactly the point.

**[06:32]** very human and that's exactly the point. What we're building is tools that behave

**[06:34]** What we're building is tools that behave

**[06:34]** What we're building is tools that behave more like a good collaborator and less

**[06:37]** more like a good collaborator and less

**[06:37]** more like a good collaborator and less like command line utilities. So we're

**[06:40]** like command line utilities. So we're

**[06:40]** like command line utilities. So we're already doing this in this tool called

**[06:42]** already doing this in this tool called

**[06:42]** already doing this in this tool called jewels which is this uh proactive

**[06:44]** jewels which is this uh proactive

**[06:44]** jewels which is this uh proactive asynchronous autonomous coding agent

**[06:45]** asynchronous autonomous coding agent

**[06:45]** asynchronous autonomous coding agent from Google labs. And we're doing this

**[06:49]** from Google labs. And we're doing this

**[06:49]** from Google labs. And we're doing this in kind of three levels of of uh

**[06:51]** in kind of three levels of of uh

**[06:51]** in kind of three levels of of uh proactivity. Level one is where a

**[06:54]** proactivity. Level one is where a

**[06:54]** proactivity. Level one is where a collaboration really starts to emerge.

**[06:56]** collaboration really starts to emerge.

**[06:56]** collaboration really starts to emerge. And this is how Jules works today where

**[06:58]** And this is how Jules works today where

**[06:58]** And this is how Jules works today where it can detect things like missing tests,


### [07:00 - 08:00]

**[07:01]** it can detect things like missing tests,

**[07:01]** it can detect things like missing tests, unused dependencies, unsafe patterns,

**[07:03]** unused dependencies, unsafe patterns,

**[07:03]** unused dependencies, unsafe patterns, and then it starts to automatically fix

**[07:05]** and then it starts to automatically fix

**[07:05]** and then it starts to automatically fix those things as it's doing other other

**[07:07]** those things as it's doing other other

**[07:07]** those things as it's doing other other tasks that you've asked it to do. This

**[07:09]** tasks that you've asked it to do. This

**[07:09]** tasks that you've asked it to do. This is sort of like this attentive sue chef

**[07:11]** is sort of like this attentive sue chef

**[07:11]** is sort of like this attentive sue chef in your workflow where it's keeping the

**[07:13]** in your workflow where it's keeping the

**[07:13]** in your workflow where it's keeping the kitchen clean, the knives sharp, the

**[07:14]** kitchen clean, the knives sharp, the

**[07:14]** kitchen clean, the knives sharp, the kitchen uh stocked so that you can focus

**[07:17]** kitchen uh stocked so that you can focus

**[07:17]** kitchen uh stocked so that you can focus on what comes next. And that's the

**[07:19]** on what comes next. And that's the

**[07:19]** on what comes next. And that's the beginning of proactive software. At

**[07:21]** beginning of proactive software. At

**[07:21]** beginning of proactive software. At level two, the agent becomes more

**[07:23]** level two, the agent becomes more

**[07:23]** level two, the agent becomes more contextually aware of the entire

**[07:26]** contextually aware of the entire

**[07:26]** contextually aware of the entire project. It observes how you work, the

**[07:28]** project. It observes how you work, the

**[07:28]** project. It observes how you work, the code you write. If you're a back-end

**[07:30]** code you write. If you're a back-end

**[07:30]** code you write. If you're a back-end engineer, maybe you need help with

**[07:31]** engineer, maybe you need help with

**[07:31]** engineer, maybe you need help with React. If you're a designer, maybe it

**[07:33]** React. If you're a designer, maybe it

**[07:33]** React. If you're a designer, maybe it wants you to may maybe it'll help uh uh

**[07:36]** wants you to may maybe it'll help uh uh

**[07:36]** wants you to may maybe it'll help uh uh write the database schema. And then it

**[07:38]** write the database schema. And then it

**[07:38]** write the database schema. And then it learns what your frameworks are and what

**[07:41]** learns what your frameworks are and what

**[07:41]** learns what your frameworks are and what your deployment style is, etc. And this

**[07:42]** your deployment style is, etc. And this

**[07:42]** your deployment style is, etc. And this is the kitchen manager. This is the

**[07:44]** is the kitchen manager. This is the

**[07:44]** is the kitchen manager. This is the person in your workflow keeping the

**[07:46]** person in your workflow keeping the

**[07:46]** person in your workflow keeping the rhythm and anticipating what you need

**[07:48]** rhythm and anticipating what you need

**[07:48]** rhythm and anticipating what you need next. And then comes level three. And

**[07:51]** next. And then comes level three. And

**[07:51]** next. And then comes level three. And this is what we're working on pretty

**[07:53]** this is what we're working on pretty

**[07:53]** this is what we're working on pretty hard right now going into December. And

**[07:55]** hard right now going into December. And

**[07:55]** hard right now going into December. And I'll show you a little bit of what we're

**[07:56]** I'll show you a little bit of what we're

**[07:56]** I'll show you a little bit of what we're what we're going to be shipping in

**[07:57]** what we're going to be shipping in

**[07:57]** what we're going to be shipping in December in a minute. But level three is

**[07:59]** December in a minute. But level three is

**[07:59]** December in a minute. But level three is where things start to converge around


### [08:00 - 09:00]

**[08:00]** where things start to converge around

**[08:00]** where things start to converge around that context. It's where the agent

**[08:03]** that context. It's where the agent

**[08:03]** that context. It's where the agent starts to understand not just context,

**[08:05]** starts to understand not just context,

**[08:05]** starts to understand not just context, but also consequence. How these choices

**[08:08]** but also consequence. How these choices

**[08:08]** but also consequence. How these choices are actually affecting the users of your

**[08:10]** are actually affecting the users of your

**[08:10]** are actually affecting the users of your products, the performance, and the

**[08:12]** products, the performance, and the

**[08:12]** products, the performance, and the outcomes. And at that level, we have

**[08:14]** outcomes. And at that level, we have

**[08:14]** outcomes. And at that level, we have this thing jewels. We also have an agent

**[08:16]** this thing jewels. We also have an agent

**[08:16]** this thing jewels. We also have an agent called Stitch, which is a design agent.

**[08:18]** called Stitch, which is a design agent.

**[08:18]** called Stitch, which is a design agent. and another one we're building called

**[08:20]** and another one we're building called

**[08:20]** and another one we're building called insights which is a data agent and

**[08:21]** insights which is a data agent and

**[08:22]** insights which is a data agent and they're all coming together to build

**[08:23]** they're all coming together to build

**[08:23]** they're all coming together to build this collective intelligence across your

**[08:25]** this collective intelligence across your

**[08:25]** this collective intelligence across your application. Jules can see what's

**[08:27]** application. Jules can see what's

**[08:27]** application. Jules can see what's breaking in the software. Stitch

**[08:29]** breaking in the software. Stitch

**[08:29]** breaking in the software. Stitch understands how users are interacting

**[08:31]** understands how users are interacting

**[08:31]** understands how users are interacting with it and insights connects behaviors

**[08:34]** with it and insights connects behaviors

**[08:34]** with it and insights connects behaviors from real world signals like analytics,

**[08:37]** from real world signals like analytics,

**[08:37]** from real world signals like analytics, telemetry and conversion rates. And then

**[08:39]** telemetry and conversion rates. And then

**[08:39]** telemetry and conversion rates. And then together they can propose improvements

**[08:42]** together they can propose improvements

**[08:42]** together they can propose improvements across boundaries of how the system all

**[08:44]** across boundaries of how the system all

**[08:44]** across boundaries of how the system all works together. doing things like

**[08:46]** works together. doing things like

**[08:46]** works together. doing things like performance fixes to improve UX and then

**[08:48]** performance fixes to improve UX and then

**[08:48]** performance fixes to improve UX and then design changes to prevent regressions

**[08:50]** design changes to prevent regressions

**[08:50]** design changes to prevent regressions and then all of that is organized based

**[08:53]** and then all of that is organized based

**[08:53]** and then all of that is organized based on live data. So the trick here is that

**[08:56]** on live data. So the trick here is that

**[08:56]** on live data. So the trick here is that the human stays firmly in the loop.

**[08:58]** the human stays firmly in the loop.

**[08:58]** the human stays firmly in the loop. You're observing what the agents are


### [09:00 - 10:00]

**[09:00]** You're observing what the agents are

**[09:00]** You're observing what the agents are doing. You're refining when you when

**[09:02]** doing. You're refining when you when

**[09:02]** doing. You're refining when you when they when you need to intervene and then

**[09:04]** they when you need to intervene and then

**[09:04]** they when you need to intervene and then you're redirecting it when it has when

**[09:07]** you're redirecting it when it has when

**[09:07]** you're redirecting it when it has when it has been misdirected. So level three

**[09:09]** it has been misdirected. So level three

**[09:09]** it has been misdirected. So level three isn't really about autonomy anymore.

**[09:12]** isn't really about autonomy anymore.

**[09:12]** isn't really about autonomy anymore. It's actually about alignment to your

**[09:14]** It's actually about alignment to your

**[09:14]** It's actually about alignment to your project. A a agents and humans

**[09:17]** project. A a agents and humans

**[09:17]** project. A a agents and humans collaborating together across the full

**[09:19]** collaborating together across the full

**[09:19]** collaborating together across the full life cycle of your project.

**[09:23]** life cycle of your project.

**[09:23]** life cycle of your project. So right now Jules is focused on this

**[09:25]** So right now Jules is focused on this

**[09:25]** So right now Jules is focused on this code awareness piece. It understands the

**[09:27]** code awareness piece. It understands the

**[09:27]** code awareness piece. It understands the environment, the frameworks and the

**[09:28]** environment, the frameworks and the

**[09:28]** environment, the frameworks and the project structures and we're moving

**[09:30]** project structures and we're moving

**[09:30]** project structures and we're moving towards more of that system awareness.

**[09:33]** towards more of that system awareness.

**[09:33]** towards more of that system awareness. So things that we're introducing in

**[09:34]** So things that we're introducing in

**[09:34]** So things that we're introducing in Jules now, we've added something called

**[09:36]** Jules now, we've added something called

**[09:36]** Jules now, we've added something called memory which I'm sure a lot of you are

**[09:38]** memory which I'm sure a lot of you are

**[09:38]** memory which I'm sure a lot of you are familiar with. It's the ability for

**[09:39]** familiar with. It's the ability for

**[09:39]** familiar with. It's the ability for Jules to write its own memories and you

**[09:43]** Jules to write its own memories and you

**[09:43]** Jules to write its own memories and you can edit them and interact with them. It

**[09:44]** can edit them and interact with them. It

**[09:44]** can edit them and interact with them. It can edit them and it understands that

**[09:46]** can edit them and it understands that

**[09:46]** can edit them and it understands that and builds this memory and context and

**[09:48]** and builds this memory and context and

**[09:48]** and builds this memory and context and knowledge of of your project as you work

**[09:51]** knowledge of of your project as you work

**[09:51]** knowledge of of your project as you work with it. We've added a critic agent

**[09:53]** with it. We've added a critic agent

**[09:53]** with it. We've added a critic agent which works adversarially with Jules to

**[09:55]** which works adversarially with Jules to

**[09:55]** which works adversarially with Jules to make sure that the code is is high

**[09:57]** make sure that the code is is high

**[09:57]** make sure that the code is is high quality but then also does a full code

**[09:59]** quality but then also does a full code

**[09:59]** quality but then also does a full code review. And then we've added


### [10:00 - 11:00]

**[10:00]** review. And then we've added

**[10:00]** review. And then we've added verification where Jules will write a

**[10:02]** verification where Jules will write a

**[10:02]** verification where Jules will write a playwright script, take a screenshot and

**[10:04]** playwright script, take a screenshot and

**[10:04]** playwright script, take a screenshot and then put that back into the trajectory

**[10:06]** then put that back into the trajectory

**[10:06]** then put that back into the trajectory for you to validate. And then we're also

**[10:09]** for you to validate. And then we're also

**[10:09]** for you to validate. And then we're also doing things like adding uh a to-do bot

**[10:11]** doing things like adding uh a to-do bot

**[10:12]** doing things like adding uh a to-do bot that will look through your code and

**[10:14]** that will look through your code and

**[10:14]** that will look through your code and look through your repository and pick up

**[10:16]** look through your repository and pick up

**[10:16]** look through your repository and pick up on anything that where you've said this

**[10:18]** on anything that where you've said this

**[10:18]** on anything that where you've said this is a to-do I want to get to in the

**[10:20]** is a to-do I want to get to in the

**[10:20]** is a to-do I want to get to in the future and it will start to proactively

**[10:21]** future and it will start to proactively

**[10:21]** future and it will start to proactively work on those things with that context.

**[10:24]** work on those things with that context.

**[10:24]** work on those things with that context. We're also adding in things like best

**[10:25]** We're also adding in things like best

**[10:25]** We're also adding in things like best practices where Jules will understand

**[10:27]** practices where Jules will understand

**[10:28]** practices where Jules will understand best practices and start to suggest

**[10:29]** best practices and start to suggest

**[10:29]** best practices and start to suggest those and also environment setup. We

**[10:33]** those and also environment setup. We

**[10:33]** those and also environment setup. We have an environment agent that we use

**[10:34]** have an environment agent that we use

**[10:34]** have an environment agent that we use internally for running evals and we're

**[10:37]** internally for running evals and we're

**[10:37]** internally for running evals and we're extending that externally to better

**[10:39]** extending that externally to better

**[10:39]** extending that externally to better understand how environment how your

**[10:40]** understand how environment how your

**[10:40]** understand how environment how your environments work and and set those up

**[10:43]** environments work and and set those up

**[10:43]** environments work and and set those up for you. And then we also are adding

**[10:45]** for you. And then we also are adding

**[10:45]** for you. And then we also are adding something called a just in time context.

**[10:47]** something called a just in time context.

**[10:47]** something called a just in time context. It's like a jewels cheat sheet where if

**[10:49]** It's like a jewels cheat sheet where if

**[10:49]** It's like a jewels cheat sheet where if it's doing something very specific it

**[10:51]** it's doing something very specific it

**[10:51]** it's doing something very specific it can and gets stuck. It can just

**[10:52]** can and gets stuck. It can just

**[10:52]** can and gets stuck. It can just immediately look at that cheat sheet

**[10:54]** immediately look at that cheat sheet

**[10:54]** immediately look at that cheat sheet instead of reaching out to you. So, this

**[10:57]** instead of reaching out to you. So, this

**[10:57]** instead of reaching out to you. So, this is all moving Jules very close to being

**[10:59]** is all moving Jules very close to being

**[10:59]** is all moving Jules very close to being that proactive teammate, not just this


### [11:00 - 12:00]

**[11:01]** that proactive teammate, not just this

**[11:01]** that proactive teammate, not just this reactive assistant. Okay, so this

**[11:04]** reactive assistant. Okay, so this

**[11:04]** reactive assistant. Okay, so this morning I was talking to my team back in

**[11:06]** morning I was talking to my team back in

**[11:06]** morning I was talking to my team back in San Francisco and I was thinking, okay,

**[11:09]** San Francisco and I was thinking, okay,

**[11:09]** San Francisco and I was thinking, okay, I'm going to do a live demo, but the

**[11:11]** I'm going to do a live demo, but the

**[11:11]** I'm going to do a live demo, but the live demo gods did not align with me

**[11:12]** live demo gods did not align with me

**[11:12]** live demo gods did not align with me this morning. We still have CLS that are

**[11:14]** this morning. We still have CLS that are

**[11:14]** this morning. We still have CLS that are being pushed to staging right now. So,

**[11:16]** being pushed to staging right now. So,

**[11:16]** being pushed to staging right now. So, I'm going to walk you through a little

**[11:17]** I'm going to walk you through a little

**[11:17]** I'm going to walk you through a little bit of this. And if you know Jed, he's

**[11:19]** bit of this. And if you know Jed, he's

**[11:19]** bit of this. And if you know Jed, he's going to, I think, be talking tomorrow.

**[11:22]** going to, I think, be talking tomorrow.

**[11:22]** going to, I think, be talking tomorrow. We're gonna um affectionately try to fix

**[11:24]** We're gonna um affectionately try to fix

**[11:24]** We're gonna um affectionately try to fix Jed's code here. Um, so this is a view

**[11:28]** Jed's code here. Um, so this is a view

**[11:28]** Jed's code here. Um, so this is a view of of proactivity and this is this is

**[11:31]** of of proactivity and this is this is

**[11:31]** of of proactivity and this is this is Jules where you prompt it and the first

**[11:33]** Jules where you prompt it and the first

**[11:33]** Jules where you prompt it and the first thing you that you do when you configure

**[11:34]** thing you that you do when you configure

**[11:34]** thing you that you do when you configure and enable proactivity is Jules will

**[11:36]** and enable proactivity is Jules will

**[11:36]** and enable proactivity is Jules will index your entire uh codebase. It'll

**[11:40]** index your entire uh codebase. It'll

**[11:40]** index your entire uh codebase. It'll index your directory and start looking

**[11:41]** index your directory and start looking

**[11:41]** index your directory and start looking for things that it can do and then it'll

**[11:43]** for things that it can do and then it'll

**[11:43]** for things that it can do and then it'll that'll show up on the screen. So right

**[11:46]** that'll show up on the screen. So right

**[11:46]** that'll show up on the screen. So right here we're looking at a little bit more

**[11:48]** here we're looking at a little bit more

**[11:48]** here we're looking at a little bit more in this um in this repository ADK Python

**[11:52]** in this um in this repository ADK Python

**[11:52]** in this um in this repository ADK Python and uh and it's indexed the repository

**[11:56]** and uh and it's indexed the repository

**[11:56]** and uh and it's indexed the repository and it's found a bunch of to-dos. It's

**[11:58]** and it's found a bunch of to-dos. It's

**[11:58]** and it's found a bunch of to-dos. It's found a bunch of best practices that it

**[11:59]** found a bunch of best practices that it

**[11:59]** found a bunch of best practices that it can update and it's giving me some


### [12:00 - 13:00]

**[12:01]** can update and it's giving me some

**[12:01]** can update and it's giving me some signal about what it's finding. And so

**[12:02]** signal about what it's finding. And so

**[12:02]** signal about what it's finding. And so you can see the signal is high

**[12:04]** you can see the signal is high

**[12:04]** you can see the signal is high confidence, medium confidence, and low.

**[12:07]** confidence, medium confidence, and low.

**[12:07]** confidence, medium confidence, and low. And so it's actually telling me what it

**[12:09]** And so it's actually telling me what it

**[12:09]** And so it's actually telling me what it thinks it can achieve based on what's in

**[12:11]** thinks it can achieve based on what's in

**[12:11]** thinks it can achieve based on what's in my code and what it wants to do. And

**[12:14]** my code and what it wants to do. And

**[12:14]** my code and what it wants to do. And that's so it has high confidence in

**[12:16]** that's so it has high confidence in

**[12:16]** that's so it has high confidence in green, medium and purple, low and yellow

**[12:18]** green, medium and purple, low and yellow

**[12:18]** green, medium and purple, low and yellow way down at the bottom. Um,

**[12:20]** way down at the bottom. Um,

**[12:20]** way down at the bottom. Um, [clears throat] and so I can go through

**[12:21]** [clears throat] and so I can go through

**[12:21]** [clears throat] and so I can go through this and I can manually click these and

**[12:24]** this and I can manually click these and

**[12:24]** this and I can manually click these and say I want to start these. And so I

**[12:26]** say I want to start these. And so I

**[12:26]** say I want to start these. And so I don't have to think about the prompt. I

**[12:28]** don't have to think about the prompt. I

**[12:28]** don't have to think about the prompt. I don't have to look at the code. I don't

**[12:29]** don't have to look at the code. I don't

**[12:29]** don't have to look at the code. I don't I I can do kind of less cognitive load

**[12:31]** I I can do kind of less cognitive load

**[12:31]** I I can do kind of less cognitive load here. We're working on something to just

**[12:34]** here. We're working on something to just

**[12:34]** here. We're working on something to just start these automatically. And so that's

**[12:36]** start these automatically. And so that's

**[12:36]** start these automatically. And so that's coming in the future. But I can also

**[12:38]** coming in the future. But I can also

**[12:38]** coming in the future. But I can also delete these. I can say, "Hey, this one

**[12:39]** delete these. I can say, "Hey, this one

**[12:39]** delete these. I can say, "Hey, this one isn't isn't for me. Isn't good." And so

**[12:42]** isn't isn't for me. Isn't good." And so

**[12:42]** isn't isn't for me. Isn't good." And so once it gets started on a task, I can

**[12:44]** once it gets started on a task, I can

**[12:44]** once it gets started on a task, I can kind of drill into it and see a little

**[12:46]** kind of drill into it and see a little

**[12:46]** kind of drill into it and see a little bit more. I can peek into the code that

**[12:48]** bit more. I can peek into the code that

**[12:48]** bit more. I can peek into the code that it is suggesting uh that uh it's

**[12:52]** it is suggesting uh that uh it's

**[12:52]** it is suggesting uh that uh it's suggesting it work on. I can find the

**[12:54]** suggesting it work on. I can find the

**[12:54]** suggesting it work on. I can find the location of that code. And it also gives

**[12:56]** location of that code. And it also gives

**[12:56]** location of that code. And it also gives me some rationale about why it wants to

**[12:59]** me some rationale about why it wants to

**[12:59]** me some rationale about why it wants to work on that code, why what it's doing,


### [13:00 - 14:00]

**[13:01]** work on that code, why what it's doing,

**[13:01]** work on that code, why what it's doing, etc. And so it's giving me a lot more

**[13:03]** etc. And so it's giving me a lot more

**[13:03]** etc. And so it's giving me a lot more context and helping me trust that it

**[13:06]** context and helping me trust that it

**[13:06]** context and helping me trust that it knows what to do here.

**[13:09]** knows what to do here.

**[13:09]** knows what to do here. Okay. So that's proactivity. that's

**[13:12]** Okay. So that's proactivity. that's

**[13:12]** Okay. So that's proactivity. that's coming in December and hopefully we'll

**[13:14]** coming in December and hopefully we'll

**[13:14]** coming in December and hopefully we'll be able to give that to everybody here.

**[13:17]** be able to give that to everybody here.

**[13:17]** be able to give that to everybody here. We're very excited about it. And I want

**[13:19]** We're very excited about it. And I want

**[13:19]** We're very excited about it. And I want to tell you a little story about uh

**[13:21]** to tell you a little story about uh

**[13:22]** to tell you a little story about uh something my husband and I were working

**[13:23]** something my husband and I were working

**[13:23]** something my husband and I were working on just to kind of set set wrap things

**[13:26]** on just to kind of set set wrap things

**[13:26]** on just to kind of set set wrap things up. We uh tinker a bunch with hardware

**[13:30]** up. We uh tinker a bunch with hardware

**[13:30]** up. We uh tinker a bunch with hardware and we live on this slow street in the

**[13:31]** and we live on this slow street in the

**[13:31]** and we live on this slow street in the middle of San Francisco in Hashbury

**[13:33]** middle of San Francisco in Hashbury

**[13:33]** middle of San Francisco in Hashbury District and so on Halloween we get a

**[13:35]** District and so on Halloween we get a

**[13:35]** District and so on Halloween we get a lot of people walking by our house and

**[13:37]** lot of people walking by our house and

**[13:37]** lot of people walking by our house and so we were trying to take advantage of

**[13:38]** so we were trying to take advantage of

**[13:38]** so we were trying to take advantage of that with our Halloween decorations and

**[13:41]** that with our Halloween decorations and

**[13:41]** that with our Halloween decorations and so we built this 6 foot animatronic head

**[13:44]** so we built this 6 foot animatronic head

**[13:44]** so we built this 6 foot animatronic head that sits in the front of our house.

**[13:47]** that sits in the front of our house.

**[13:47]** that sits in the front of our house. It's this old Victorian house and he

**[13:50]** It's this old Victorian house and he

**[13:50]** It's this old Victorian house and he sculpted it out of foam, epoxy and

**[13:52]** sculpted it out of foam, epoxy and

**[13:52]** sculpted it out of foam, epoxy and fiberglass. And then I our our kids also

**[13:55]** fiberglass. And then I our our kids also

**[13:55]** fiberglass. And then I our our kids also called this lovingly the bald head. And

**[13:58]** called this lovingly the bald head. And

**[13:58]** called this lovingly the bald head. And it's based off of if you ever see saw


### [14:00 - 15:00]

**[14:00]** it's based off of if you ever see saw

**[14:00]** it's based off of if you ever see saw Peewee Herman from the 80s. It's based

**[14:02]** Peewee Herman from the 80s. It's based

**[14:02]** Peewee Herman from the 80s. It's based off of the PeeWee Herman Peewee's Big

**[14:03]** off of the PeeWee Herman Peewee's Big

**[14:03]** off of the PeeWee Herman Peewee's Big Adventures head. Um so while my husband

**[14:06]** Adventures head. Um so while my husband

**[14:06]** Adventures head. Um so while my husband was doing this I was spending my time

**[14:09]** was doing this I was spending my time

**[14:09]** was doing this I was spending my time working with Jules on updating the

**[14:11]** working with Jules on updating the

**[14:11]** working with Jules on updating the firmware, controlling the stepper

**[14:12]** firmware, controlling the stepper

**[14:12]** firmware, controlling the stepper motors, working on the um on the LEDs

**[14:14]** motors, working on the um on the LEDs

**[14:14]** motors, working on the um on the LEDs and the sensors. And for me that's the

**[14:17]** and the sensors. And for me that's the

**[14:17]** and the sensors. And for me that's the fun part for me is like really getting

**[14:19]** fun part for me is like really getting

**[14:19]** fun part for me is like really getting creative with what the LEDs are doing.

**[14:21]** creative with what the LEDs are doing.

**[14:22]** creative with what the LEDs are doing. So I wanted to focus on that, the LED

**[14:23]** So I wanted to focus on that, the LED

**[14:24]** So I wanted to focus on that, the LED animations, but I ended up spending most

**[14:26]** animations, but I ended up spending most

**[14:26]** animations, but I ended up spending most of my time actually fixing bugs and

**[14:29]** of my time actually fixing bugs and

**[14:29]** of my time actually fixing bugs and swapping libraries and doing things like

**[14:31]** swapping libraries and doing things like

**[14:31]** swapping libraries and doing things like that. So what I would do is I would

**[14:32]** that. So what I would do is I would

**[14:32]** that. So what I would do is I would prompt Jules, I'd wait 10 minutes and

**[14:35]** prompt Jules, I'd wait 10 minutes and

**[14:35]** prompt Jules, I'd wait 10 minutes and then I would repeat. And I found that

**[14:38]** then I would repeat. And I found that

**[14:38]** then I would repeat. And I found that process very very tedious. And what I

**[14:41]** process very very tedious. And what I

**[14:41]** process very very tedious. And what I wanted was actually Jules to do the

**[14:43]** wanted was actually Jules to do the

**[14:43]** wanted was actually Jules to do the research. I wanted it to handle the the

**[14:45]** research. I wanted it to handle the the

**[14:45]** research. I wanted it to handle the the ugly parts where it was researching how

**[14:48]** ugly parts where it was researching how

**[14:48]** ugly parts where it was researching how to fix a bug. Uh doing the debugging

**[14:51]** to fix a bug. Uh doing the debugging

**[14:51]** to fix a bug. Uh doing the debugging itself. And I wanted it to do this so

**[14:52]** itself. And I wanted it to do this so

**[14:52]** itself. And I wanted it to do this so that I could focus on the creative

**[14:54]** that I could focus on the creative

**[14:54]** that I could focus on the creative parts. I wanted the eyes to move and

**[14:56]** parts. I wanted the eyes to move and

**[14:56]** parts. I wanted the eyes to move and like follow people as they walk down the

**[14:59]** like follow people as they walk down the

**[14:59]** like follow people as they walk down the street and like have lasers coming out


### [15:00 - 16:00]

**[15:01]** street and like have lasers coming out

**[15:01]** street and like have lasers coming out of its eyes and stuff like I mentioned

**[15:02]** of its eyes and stuff like I mentioned

**[15:02]** of its eyes and stuff like I mentioned it was Halloween. It was very scary. Uh

**[15:04]** it was Halloween. It was very scary. Uh

**[15:04]** it was Halloween. It was very scary. Uh and and this but but I couldn't really

**[15:07]** and and this but but I couldn't really

**[15:07]** and and this but but I couldn't really do as much of that. and I ended up

**[15:08]** do as much of that. and I ended up

**[15:08]** do as much of that. and I ended up actually not shipping as much as I

**[15:10]** actually not shipping as much as I

**[15:10]** actually not shipping as much as I wanted to with this animatronic bald

**[15:13]** wanted to with this animatronic bald

**[15:13]** wanted to with this animatronic bald head. And so it's that gap that we

**[15:17]** head. And so it's that gap that we

**[15:17]** head. And so it's that gap that we actually want to close. It's the space

**[15:19]** actually want to close. It's the space

**[15:19]** actually want to close. It's the space between with jewels, it's the space

**[15:20]** between with jewels, it's the space

**[15:20]** between with jewels, it's the space between that tool friction and creative

**[15:23]** between that tool friction and creative

**[15:23]** between that tool friction and creative freedom that we're trying to unlock with

**[15:25]** freedom that we're trying to unlock with

**[15:25]** freedom that we're trying to unlock with these kinds of proactive agents.

**[15:28]** these kinds of proactive agents.

**[15:28]** these kinds of proactive agents. So what I really want you guys to take

**[15:32]** So what I really want you guys to take

**[15:32]** So what I really want you guys to take away from it and I give this advice to

**[15:33]** away from it and I give this advice to

**[15:33]** away from it and I give this advice to the the folks on on the Jules team a lot

**[15:36]** the the folks on on the Jules team a lot

**[15:36]** the the folks on on the Jules team a lot is that the product we build today

**[15:39]** is that the product we build today

**[15:39]** is that the product we build today actually won't be the project the

**[15:40]** actually won't be the project the

**[15:40]** actually won't be the project the products that we have in the future and

**[15:42]** products that we have in the future and

**[15:42]** products that we have in the future and I think a lot of us know that but in

**[15:44]** I think a lot of us know that but in

**[15:44]** I think a lot of us know that but in reality I want everybody in this room

**[15:46]** reality I want everybody in this room

**[15:46]** reality I want everybody in this room and everyone building working with AI to

**[15:49]** and everyone building working with AI to

**[15:49]** and everyone building working with AI to be able to take those big steps. I think

**[15:51]** be able to take those big steps. I think

**[15:51]** be able to take those big steps. I think the patterns that we rely on today, Git

**[15:54]** the patterns that we rely on today, Git

**[15:54]** the patterns that we rely on today, Git uh your your idees, even the code, how

**[15:57]** uh your your idees, even the code, how

**[15:57]** uh your your idees, even the code, how we think about the code itself might not

**[15:59]** we think about the code itself might not

**[15:59]** we think about the code itself might not exist a year from now, might not exist


### [16:00 - 17:00]

**[16:01]** exist a year from now, might not exist

**[16:01]** exist a year from now, might not exist six months from now. And that's the

**[16:04]** six months from now. And that's the

**[16:04]** six months from now. And that's the exciting part for me. It's sort of we

**[16:06]** exciting part for me. It's sort of we

**[16:06]** exciting part for me. It's sort of we get to invent the future right now. We

**[16:08]** get to invent the future right now. We

**[16:08]** get to invent the future right now. We get to describe and decide how software

**[16:11]** get to describe and decide how software

**[16:11]** get to describe and decide how software is made and built. Uh kind of all the

**[16:13]** is made and built. Uh kind of all the

**[16:13]** is made and built. Uh kind of all the people in this room. So my my challenge

**[16:16]** people in this room. So my my challenge

**[16:16]** people in this room. So my my challenge to you is to not be afraid to question

**[16:20]** to you is to not be afraid to question

**[16:20]** to you is to not be afraid to question the old ways of how you're building

**[16:22]** the old ways of how you're building

**[16:22]** the old ways of how you're building software cuz really the future is coming

**[16:25]** software cuz really the future is coming

**[16:25]** software cuz really the future is coming faster than any of us know. It's

**[16:27]** faster than any of us know. It's

**[16:27]** faster than any of us know. It's probably already here and the cool thing

**[16:29]** probably already here and the cool thing

**[16:29]** probably already here and the cool thing is we get to build it together. Thank

**[16:32]** is we get to build it together. Thank

**[16:32]** is we get to build it together. Thank you.

**[16:34]** you.

**[16:34]** you. [music]


