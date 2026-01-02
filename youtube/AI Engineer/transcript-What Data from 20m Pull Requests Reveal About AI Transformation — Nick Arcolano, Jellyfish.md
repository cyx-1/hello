# What Data from 20m Pull Requests Reveal About AI Transformation — Nick Arcolano, Jellyfish

**Video URL:** https://www.youtube.com/watch?v=WqZq8L-v9pA

---

## Full Transcript

### [00:00 - 01:00]

**[00:02]** Hi, my name is Nicholas Arcolano and I'm

**[00:02]** Hi, my name is Nicholas Arcolano and I'm the head of research at Jellyfish.

**[00:04]** the head of research at Jellyfish.

**[00:04]** the head of research at Jellyfish. Today, I'd like to talk to you about AI

**[00:06]** Today, I'd like to talk to you about AI

**[00:06]** Today, I'd like to talk to you about AI transformation, specifically what real

**[00:08]** transformation, specifically what real

**[00:08]** transformation, specifically what real world data can tell us about what's

**[00:10]** world data can tell us about what's

**[00:10]** world data can tell us about what's actually happening in the wild. Now, a

**[00:13]** actually happening in the wild. Now, a

**[00:13]** actually happening in the wild. Now, a lot of AI native companies are being

**[00:15]** lot of AI native companies are being

**[00:15]** lot of AI native companies are being founded right now, and there are many

**[00:16]** founded right now, and there are many

**[00:16]** founded right now, and there are many more existing companies that are trying

**[00:18]** more existing companies that are trying

**[00:18]** more existing companies that are trying to transform themselves into being AI

**[00:20]** to transform themselves into being AI

**[00:20]** to transform themselves into being AI native. I've talked to many folks from

**[00:23]** native. I've talked to many folks from

**[00:23]** native. I've talked to many folks from these companies, and they all have the

**[00:24]** these companies, and they all have the

**[00:24]** these companies, and they all have the same big questions. Number one, what

**[00:27]** same big questions. Number one, what

**[00:27]** same big questions. Number one, what does good adoption of AI coding tools

**[00:29]** does good adoption of AI coding tools

**[00:29]** does good adoption of AI coding tools and agents actually look like? Uh,

**[00:32]** and agents actually look like? Uh,

**[00:32]** and agents actually look like? Uh, number two, what productivity gains

**[00:34]** number two, what productivity gains

**[00:34]** number two, what productivity gains should I be expecting as we transform

**[00:36]** should I be expecting as we transform

**[00:36]** should I be expecting as we transform our team and the tools that we use? Uh,

**[00:39]** our team and the tools that we use? Uh,

**[00:39]** our team and the tools that we use? Uh, three, what are the side effects of this

**[00:42]** three, what are the side effects of this

**[00:42]** three, what are the side effects of this transformation?

**[00:43]** transformation?

**[00:43]** transformation? And perhaps most importantly, if AI

**[00:46]** And perhaps most importantly, if AI

**[00:46]** And perhaps most importantly, if AI transformation isn't delivering as

**[00:48]** transformation isn't delivering as

**[00:48]** transformation isn't delivering as advertised, what's going on and what can

**[00:50]** advertised, what's going on and what can

**[00:50]** advertised, what's going on and what can you do about it? Now, at Jellyfish, we

**[00:52]** you do about it? Now, at Jellyfish, we

**[00:52]** you do about it? Now, at Jellyfish, we believe the best way to get answers is

**[00:54]** believe the best way to get answers is

**[00:54]** believe the best way to get answers is with data. So in the next 15- 20 minutes

**[00:56]** with data. So in the next 15- 20 minutes

**[00:56]** with data. So in the next 15- 20 minutes or so, I'm going to give you some

**[00:57]** or so, I'm going to give you some

**[00:58]** or so, I'm going to give you some databacked insights from studies we've

**[00:59]** databacked insights from studies we've

**[00:59]** databacked insights from studies we've done to help you tackle these big


### [01:00 - 02:00]

**[01:01]** done to help you tackle these big

**[01:01]** done to help you tackle these big questions.

**[01:03]** questions.

**[01:03]** questions. Okay, before we jump in though, uh let's

**[01:05]** Okay, before we jump in though, uh let's

**[01:05]** Okay, before we jump in though, uh let's take a minute to talk about the data

**[01:07]** take a minute to talk about the data

**[01:07]** take a minute to talk about the data behind the rest of the stuff in this

**[01:08]** behind the rest of the stuff in this

**[01:08]** behind the rest of the stuff in this talk. Uh now at Jellyfish, we provide

**[01:12]** talk. Uh now at Jellyfish, we provide

**[01:12]** talk. Uh now at Jellyfish, we provide analytics and insights for software

**[01:13]** analytics and insights for software

**[01:13]** analytics and insights for software engineering leaders. And to do this, we

**[01:15]** engineering leaders. And to do this, we

**[01:15]** engineering leaders. And to do this, we combine information from multiple

**[01:17]** combine information from multiple

**[01:17]** combine information from multiple sources, including

**[01:19]** sources, including

**[01:19]** sources, including usage and interactions with AI coding

**[01:21]** usage and interactions with AI coding

**[01:21]** usage and interactions with AI coding tools like C-pilot, Cursor, Claude Code,

**[01:25]** tools like C-pilot, Cursor, Claude Code,

**[01:25]** tools like C-pilot, Cursor, Claude Code, uh interactions uh with autonomous

**[01:27]** uh interactions uh with autonomous

**[01:27]** uh interactions uh with autonomous coding agents, things like Devon and

**[01:29]** coding agents, things like Devon and

**[01:29]** coding agents, things like Devon and Codeex as well as PR review bots. We

**[01:32]** Codeex as well as PR review bots. We

**[01:32]** Codeex as well as PR review bots. We also combine this with data from source

**[01:34]** also combine this with data from source

**[01:34]** also combine this with data from source control platforms like GitHub, so we can

**[01:36]** control platforms like GitHub, so we can

**[01:36]** control platforms like GitHub, so we can understand things about the actual

**[01:37]** understand things about the actual

**[01:38]** understand things about the actual codebase where the work is happening. We

**[01:40]** codebase where the work is happening. We

**[01:40]** codebase where the work is happening. We also pull in data from task management

**[01:43]** also pull in data from task management

**[01:43]** also pull in data from task management platforms uh things like linear or Jira

**[01:46]** platforms uh things like linear or Jira

**[01:46]** platforms uh things like linear or Jira and that tells you about what the actual

**[01:47]** and that tells you about what the actual

**[01:47]** and that tells you about what the actual goal of uh the work being done is. So

**[01:50]** goal of uh the work being done is. So

**[01:50]** goal of uh the work being done is. So for the rest of this talk we're going to

**[01:52]** for the rest of this talk we're going to

**[01:52]** for the rest of this talk we're going to be looking at findings from a data set

**[01:53]** be looking at findings from a data set

**[01:53]** be looking at findings from a data set with data like this uh across our

**[01:56]** with data like this uh across our

**[01:56]** with data like this uh across our customers comprises about 20 million

**[01:58]** customers comprises about 20 million

**[01:58]** customers comprises about 20 million poll requests. Uh these were written


### [02:00 - 03:00]

**[02:00]** poll requests. Uh these were written

**[02:00]** poll requests. Uh these were written emerged by about 200,000 uh developers

**[02:03]** emerged by about 200,000 uh developers

**[02:03]** emerged by about 200,000 uh developers from around a thousand companies. We've

**[02:06]** from around a thousand companies. We've

**[02:06]** from around a thousand companies. We've been collecting this data for more than

**[02:07]** been collecting this data for more than

**[02:07]** been collecting this data for more than a year. So today we'll be looking at

**[02:09]** a year. So today we'll be looking at

**[02:09]** a year. So today we'll be looking at results that span from June 2024 to the

**[02:12]** results that span from June 2024 to the

**[02:12]** results that span from June 2024 to the present. Okay,

**[02:14]** present. Okay,

**[02:14]** present. Okay, so let's dig in. Question one, what does

**[02:18]** so let's dig in. Question one, what does

**[02:18]** so let's dig in. Question one, what does good adoption look like?

**[02:21]** good adoption look like?

**[02:21]** good adoption look like? Well, [sighs and gasps] let's start with

**[02:23]** Well, [sighs and gasps] let's start with

**[02:23]** Well, [sighs and gasps] let's start with lines of code. I don't think this is a

**[02:25]** lines of code. I don't think this is a

**[02:25]** lines of code. I don't think this is a great metric, but it's one we all hear

**[02:26]** great metric, but it's one we all hear

**[02:26]** great metric, but it's one we all hear about in the media a bunch, so it's

**[02:28]** about in the media a bunch, so it's

**[02:28]** about in the media a bunch, so it's worth talking about. Here's data from a

**[02:31]** worth talking about. Here's data from a

**[02:31]** worth talking about. Here's data from a cohort of companies we've been tracking

**[02:32]** cohort of companies we've been tracking

**[02:32]** cohort of companies we've been tracking since June of last year. The purple bar

**[02:34]** since June of last year. The purple bar

**[02:34]** since June of last year. The purple bar represents the fraction of those

**[02:36]** represents the fraction of those

**[02:36]** represents the fraction of those companies that are generating 50% or

**[02:38]** companies that are generating 50% or

**[02:38]** companies that are generating 50% or more of their code with AI. So if you

**[02:40]** more of their code with AI. So if you

**[02:40]** more of their code with AI. So if you look at that purple bar, you can see

**[02:42]** look at that purple bar, you can see

**[02:42]** look at that purple bar, you can see that starting last summer, only about 2%

**[02:44]** that starting last summer, only about 2%

**[02:44]** that starting last summer, only about 2% of these companies were generating 50%

**[02:46]** of these companies were generating 50%

**[02:46]** of these companies were generating 50% or more of their code with AI. But you

**[02:48]** or more of their code with AI. But you

**[02:48]** or more of their code with AI. But you can see this has been steadily growing.

**[02:50]** can see this has been steadily growing.

**[02:50]** can see this has been steadily growing. And as of last month, among these same

**[02:52]** And as of last month, among these same

**[02:52]** And as of last month, among these same companies, now nearly half are

**[02:53]** companies, now nearly half are

**[02:53]** companies, now nearly half are generating 50% or more of their code

**[02:56]** generating 50% or more of their code

**[02:56]** generating 50% or more of their code with AI.

**[02:57]** with AI.

**[02:57]** with AI. Now, I think a more useful thing to look


### [03:00 - 04:00]

**[03:00]** Now, I think a more useful thing to look

**[03:00]** Now, I think a more useful thing to look at actually is developer adoption

**[03:02]** at actually is developer adoption

**[03:02]** at actually is developer adoption because this gets at the actual behavior

**[03:05]** because this gets at the actual behavior

**[03:05]** because this gets at the actual behavior change that you want to see in your

**[03:07]** change that you want to see in your

**[03:07]** change that you want to see in your team. It's also the thing I've seen that

**[03:09]** team. It's also the thing I've seen that

**[03:09]** team. It's also the thing I've seen that correlates most directly with good

**[03:11]** correlates most directly with good

**[03:11]** correlates most directly with good productivity outcomes. And we're going

**[03:12]** productivity outcomes. And we're going

**[03:12]** productivity outcomes. And we're going to talk about this a lot more later. Uh

**[03:15]** to talk about this a lot more later. Uh

**[03:15]** to talk about this a lot more later. Uh but first, we define an AI adoption rate

**[03:18]** but first, we define an AI adoption rate

**[03:18]** but first, we define an AI adoption rate for developers by computing the fraction

**[03:20]** for developers by computing the fraction

**[03:20]** for developers by computing the fraction of time that they use AI tools when they

**[03:22]** of time that they use AI tools when they

**[03:22]** of time that they use AI tools when they code. So 100% for a developer, that

**[03:25]** code. So 100% for a developer, that

**[03:25]** code. So 100% for a developer, that means you're using AI tools every time

**[03:27]** means you're using AI tools every time

**[03:27]** means you're using AI tools every time you code. A company's adoption rate for

**[03:30]** you code. A company's adoption rate for

**[03:30]** you code. A company's adoption rate for the whole company, that's just the

**[03:31]** the whole company, that's just the

**[03:31]** the whole company, that's just the average of the adoption rates for all

**[03:33]** average of the adoption rates for all

**[03:33]** average of the adoption rates for all their individuals. So 100% for a company

**[03:35]** their individuals. So 100% for a company

**[03:35]** their individuals. So 100% for a company means that every developer is using AI

**[03:37]** means that every developer is using AI

**[03:37]** means that every developer is using AI every time they code. So what you see

**[03:40]** every time they code. So what you see

**[03:40]** every time they code. So what you see here, this is a plot of the 25th, 50th,

**[03:43]** here, this is a plot of the 25th, 50th,

**[03:43]** here, this is a plot of the 25th, 50th, and 75th percentile of company adoption

**[03:45]** and 75th percentile of company adoption

**[03:45]** and 75th percentile of company adoption rates uh by week for the developers and

**[03:48]** rates uh by week for the developers and

**[03:48]** rates uh by week for the developers and companies that we've been tracking. And

**[03:50]** companies that we've been tracking. And

**[03:50]** companies that we've been tracking. And if you look at the AI adoption rates as

**[03:52]** if you look at the AI adoption rates as

**[03:52]** if you look at the AI adoption rates as of last summer, you can see the median

**[03:54]** of last summer, you can see the median

**[03:54]** of last summer, you can see the median adoption rate was around 22%. So, uh,

**[03:57]** adoption rate was around 22%. So, uh,

**[03:57]** adoption rate was around 22%. So, uh, median company developers are using AI


### [04:00 - 05:00]

**[04:01]** median company developers are using AI

**[04:01]** median company developers are using AI 22% of the time that they code. It's

**[04:03]** 22% of the time that they code. It's

**[04:03]** 22% of the time that they code. It's grown steadily since then, and today

**[04:05]** grown steadily since then, and today

**[04:05]** grown steadily since then, and today we're seeing median adoption rates close

**[04:08]** we're seeing median adoption rates close

**[04:08]** we're seeing median adoption rates close to 90%. Now, if you're like me and

**[04:12]** to 90%. Now, if you're like me and

**[04:12]** to 90%. Now, if you're like me and you're using multiple tools constantly

**[04:13]** you're using multiple tools constantly

**[04:14]** you're using multiple tools constantly in parallel, both synchronous and

**[04:16]** in parallel, both synchronous and

**[04:16]** in parallel, both synchronous and asynchronous modes, uh, you're you're at

**[04:18]** asynchronous modes, uh, you're you're at

**[04:18]** asynchronous modes, uh, you're you're at 100%. It might seem crazy to you that

**[04:20]** 100%. It might seem crazy to you that

**[04:20]** 100%. It might seem crazy to you that not everyone else is at 100%. However,

**[04:22]** not everyone else is at 100%. However,

**[04:22]** not everyone else is at 100%. However, the reality is that for many teams,

**[04:24]** the reality is that for many teams,

**[04:24]** the reality is that for many teams, there are still real technical,

**[04:26]** there are still real technical,

**[04:26]** there are still real technical, organizational, and cultural barriers to

**[04:28]** organizational, and cultural barriers to

**[04:28]** organizational, and cultural barriers to adopting these tools more completely.

**[04:30]** adopting these tools more completely.

**[04:30]** adopting these tools more completely. So, that brings me to my final point on

**[04:32]** So, that brings me to my final point on

**[04:32]** So, that brings me to my final point on adoption. You might ask, what about

**[04:35]** adoption. You might ask, what about

**[04:35]** adoption. You might ask, what about autonomous coding agents? Now, the

**[04:37]** autonomous coding agents? Now, the

**[04:37]** autonomous coding agents? Now, the results I've just shown you, those are

**[04:39]** results I've just shown you, those are

**[04:39]** results I've just shown you, those are overwhelmingly from interactive coding

**[04:40]** overwhelmingly from interactive coding

**[04:40]** overwhelmingly from interactive coding tools, things like Copilot, Cursor,

**[04:43]** tools, things like Copilot, Cursor,

**[04:43]** tools, things like Copilot, Cursor, Claude Code. Now, we know that these

**[04:45]** Claude Code. Now, we know that these

**[04:45]** Claude Code. Now, we know that these tools all have interactive agentic

**[04:47]** tools all have interactive agentic

**[04:47]** tools all have interactive agentic modes, but what about your your kind of

**[04:49]** modes, but what about your your kind of

**[04:49]** modes, but what about your your kind of true fully autonomous agents like your

**[04:51]** true fully autonomous agents like your

**[04:52]** true fully autonomous agents like your Devons or your codeexs? Maybe you're

**[04:54]** Devons or your codeexs? Maybe you're

**[04:54]** Devons or your codeexs? Maybe you're using agents like these or something

**[04:56]** using agents like these or something

**[04:56]** using agents like these or something else to great effect or maybe you

**[04:57]** else to great effect or maybe you

**[04:57]** else to great effect or maybe you haven't really gotten going with

**[04:59]** haven't really gotten going with

**[04:59]** haven't really gotten going with autonomous agents yet. It's fine. You


### [05:00 - 06:00]

**[05:01]** autonomous agents yet. It's fine. You

**[05:01]** autonomous agents yet. It's fine. You know, wherever you are in your journey,

**[05:03]** know, wherever you are in your journey,

**[05:03]** know, wherever you are in your journey, but if it feels like you're slow going

**[05:05]** but if it feels like you're slow going

**[05:05]** but if it feels like you're slow going getting off the ground with autonomous

**[05:06]** getting off the ground with autonomous

**[05:06]** getting off the ground with autonomous agents, I'm here to tell you you're not

**[05:09]** agents, I'm here to tell you you're not

**[05:09]** agents, I'm here to tell you you're not alone. So in our data set, we only see

**[05:12]** alone. So in our data set, we only see

**[05:12]** alone. So in our data set, we only see about 44% of companies have done

**[05:14]** about 44% of companies have done

**[05:14]** about 44% of companies have done anything with autonomous agents at all

**[05:16]** anything with autonomous agents at all

**[05:16]** anything with autonomous agents at all in the past 3 months. The vast majority

**[05:19]** in the past 3 months. The vast majority

**[05:19]** in the past 3 months. The vast majority of that work is what you'd consider um

**[05:21]** of that work is what you'd consider um

**[05:21]** of that work is what you'd consider um triing and experimentation type stuff

**[05:23]** triing and experimentation type stuff

**[05:23]** triing and experimentation type stuff like not full scale production and

**[05:26]** like not full scale production and

**[05:26]** like not full scale production and ultimately it all amounts to less than

**[05:28]** ultimately it all amounts to less than

**[05:28]** ultimately it all amounts to less than uh 2% of the millions of PRs that were

**[05:31]** uh 2% of the millions of PRs that were

**[05:31]** uh 2% of the millions of PRs that were merged over that time frame. Uh so you

**[05:34]** merged over that time frame. Uh so you

**[05:34]** merged over that time frame. Uh so you know still very early days.

**[05:38]** know still very early days.

**[05:38]** know still very early days. All right, let's move on. Now, I'd like

**[05:40]** All right, let's move on. Now, I'd like

**[05:40]** All right, let's move on. Now, I'd like to talk about productivity. So, even

**[05:42]** to talk about productivity. So, even

**[05:42]** to talk about productivity. So, even though autonomous agents aren't yet

**[05:44]** though autonomous agents aren't yet

**[05:44]** though autonomous agents aren't yet delivering at scale, we're still seeing

**[05:47]** delivering at scale, we're still seeing

**[05:47]** delivering at scale, we're still seeing big gains from adoption of interactive

**[05:49]** big gains from adoption of interactive

**[05:49]** big gains from adoption of interactive coding agents. So, let's talk about what

**[05:51]** coding agents. So, let's talk about what

**[05:51]** coding agents. So, let's talk about what we're seeing. First though, what do we

**[05:54]** we're seeing. First though, what do we

**[05:54]** we're seeing. First though, what do we mean by productivity? This can be a very

**[05:57]** mean by productivity? This can be a very

**[05:57]** mean by productivity? This can be a very loaded term, kind of squishy,

**[05:59]** loaded term, kind of squishy,

**[05:59]** loaded term, kind of squishy, overloaded. There's many ways to attack


### [06:00 - 07:00]

**[06:01]** overloaded. There's many ways to attack

**[06:01]** overloaded. There's many ways to attack it. Uh, a good place to start though,

**[06:04]** it. Uh, a good place to start though,

**[06:04]** it. Uh, a good place to start though, just plain old PR throughput. How many

**[06:06]** just plain old PR throughput. How many

**[06:06]** just plain old PR throughput. How many pull requests does the average engineer

**[06:08]** pull requests does the average engineer

**[06:08]** pull requests does the average engineer merge per week? Not the most exotic

**[06:11]** merge per week? Not the most exotic

**[06:11]** merge per week? Not the most exotic metric, but it's proven. It's widely

**[06:13]** metric, but it's proven. It's widely

**[06:13]** metric, but it's proven. It's widely accepted. Uh do note that the absolute

**[06:16]** accepted. Uh do note that the absolute

**[06:16]** accepted. Uh do note that the absolute level of PR throughput is something that

**[06:18]** level of PR throughput is something that

**[06:18]** level of PR throughput is something that varies, right? It depends on things like

**[06:21]** varies, right? It depends on things like

**[06:21]** varies, right? It depends on things like how you like to scope work. It actually

**[06:23]** how you like to scope work. It actually

**[06:23]** how you like to scope work. It actually also depends on your architecture and

**[06:25]** also depends on your architecture and

**[06:25]** also depends on your architecture and put a pin in that because we're going to

**[06:26]** put a pin in that because we're going to

**[06:26]** put a pin in that because we're going to talk about that more later. Uh however,

**[06:29]** talk about that more later. Uh however,

**[06:29]** talk about that more later. Uh however, measuring the change in PR throughput,

**[06:31]** measuring the change in PR throughput,

**[06:31]** measuring the change in PR throughput, especially to keep all these other

**[06:32]** especially to keep all these other

**[06:32]** especially to keep all these other things constant. Measuring that for your

**[06:34]** things constant. Measuring that for your

**[06:34]** things constant. Measuring that for your team is a good way to uh track

**[06:36]** team is a good way to uh track

**[06:36]** team is a good way to uh track productivity gains. Another good one,

**[06:38]** productivity gains. Another good one,

**[06:38]** productivity gains. Another good one, cycle time. Uh you know, lots of

**[06:41]** cycle time. Uh you know, lots of

**[06:41]** cycle time. Uh you know, lots of different ways to define that one, but

**[06:43]** different ways to define that one, but

**[06:43]** different ways to define that one, but basically the latency or lead time to

**[06:46]** basically the latency or lead time to

**[06:46]** basically the latency or lead time to code getting deployed. For our purposes,

**[06:48]** code getting deployed. For our purposes,

**[06:48]** code getting deployed. For our purposes, we'll take each PR and we'll measure the

**[06:49]** we'll take each PR and we'll measure the

**[06:50]** we'll take each PR and we'll measure the time frame from the first commit in the

**[06:51]** time frame from the first commit in the

**[06:51]** time frame from the first commit in the PR until it was merged.

**[06:54]** PR until it was merged.

**[06:54]** PR until it was merged. Okay, so here's what we're seeing for

**[06:57]** Okay, so here's what we're seeing for

**[06:57]** Okay, so here's what we're seeing for changes in PR throughput. And let me

**[06:59]** changes in PR throughput. And let me

**[06:59]** changes in PR throughput. And let me explain this chart. Uh, every data point


### [07:00 - 08:00]

**[07:02]** explain this chart. Uh, every data point

**[07:02]** explain this chart. Uh, every data point here is a snapshot of a given company on

**[07:04]** here is a snapshot of a given company on

**[07:04]** here is a snapshot of a given company on a given week. The x-axis is the

**[07:07]** a given week. The x-axis is the

**[07:07]** a given week. The x-axis is the company's AI adoption rate that we

**[07:09]** company's AI adoption rate that we

**[07:09]** company's AI adoption rate that we discussed earlier. The y-axis is the

**[07:11]** discussed earlier. The y-axis is the

**[07:11]** discussed earlier. The y-axis is the company's average PRs per engineer that

**[07:14]** company's average PRs per engineer that

**[07:14]** company's average PRs per engineer that week. So you can see here a clear

**[07:16]** week. So you can see here a clear

**[07:16]** week. So you can see here a clear correlation between AI adoption and PR

**[07:18]** correlation between AI adoption and PR

**[07:18]** correlation between AI adoption and PR throughput. The average trend here is

**[07:20]** throughput. The average trend here is

**[07:20]** throughput. The average trend here is about a 2x change as you go from zero to

**[07:23]** about a 2x change as you go from zero to

**[07:23]** about a 2x change as you go from zero to full adoption. So on average, a company

**[07:26]** full adoption. So on average, a company

**[07:26]** full adoption. So on average, a company should expect to double their PR

**[07:28]** should expect to double their PR

**[07:28]** should expect to double their PR throughput if they go from not using AI

**[07:30]** throughput if they go from not using AI

**[07:30]** throughput if they go from not using AI at all, which not really anybody's doing

**[07:32]** at all, which not really anybody's doing

**[07:32]** at all, which not really anybody's doing anymore, to 100% uh adoption of AI

**[07:35]** anymore, to 100% uh adoption of AI

**[07:35]** anymore, to 100% uh adoption of AI coding tools.

**[07:37]** coding tools.

**[07:38]** coding tools. Now, we also see some gains in cycle

**[07:39]** Now, we also see some gains in cycle

**[07:39]** Now, we also see some gains in cycle time. So more work is happening and it's

**[07:41]** time. So more work is happening and it's

**[07:42]** time. So more work is happening and it's happening faster. This is similar to the

**[07:44]** happening faster. This is similar to the

**[07:44]** happening faster. This is similar to the previous chart, but now on the y- axis,

**[07:46]** previous chart, but now on the y- axis,

**[07:46]** previous chart, but now on the y- axis, we're looking at median cycle time for

**[07:48]** we're looking at median cycle time for

**[07:48]** we're looking at median cycle time for PRs merged each week instead of PR

**[07:50]** PRs merged each week instead of PR

**[07:50]** PRs merged each week instead of PR throughput. Uh, this is a cool chart. As

**[07:52]** throughput. Uh, this is a cool chart. As

**[07:52]** throughput. Uh, this is a cool chart. As an aside, I like the cycle time

**[07:54]** an aside, I like the cycle time

**[07:54]** an aside, I like the cycle time distribution because you can see these

**[07:56]** distribution because you can see these

**[07:56]** distribution because you can see these two clear bands horizontally. So that

**[07:59]** two clear bands horizontally. So that

**[07:59]** two clear bands horizontally. So that lower horizontal cluster that


### [08:00 - 09:00]

**[08:01]** lower horizontal cluster that

**[08:01]** lower horizontal cluster that corresponds to tasks that take less than

**[08:02]** corresponds to tasks that take less than

**[08:02]** corresponds to tasks that take less than a day and then you see sort of a valley

**[08:05]** a day and then you see sort of a valley

**[08:05]** a day and then you see sort of a valley and then there's a band in the middle

**[08:06]** and then there's a band in the middle

**[08:06]** and then there's a band in the middle for tasks that take about two days. Then

**[08:08]** for tasks that take about two days. Then

**[08:08]** for tasks that take about two days. Then there's a long tail of stuff going up

**[08:09]** there's a long tail of stuff going up

**[08:09]** there's a long tail of stuff going up the y-axis that takes much longer. I've

**[08:11]** the y-axis that takes much longer. I've

**[08:11]** the y-axis that takes much longer. I've truncated it here because as we all know

**[08:13]** truncated it here because as we all know

**[08:13]** truncated it here because as we all know some things can take uh quite a while

**[08:16]** some things can take uh quite a while

**[08:16]** some things can take uh quite a while [laughter] to to get merged. Um but you

**[08:20]** [laughter] to to get merged. Um but you

**[08:20]** [laughter] to to get merged. Um but you know what's exciting here is the average

**[08:21]** know what's exciting here is the average

**[08:21]** know what's exciting here is the average trend is a 24% decrease in cycle times

**[08:24]** trend is a 24% decrease in cycle times

**[08:24]** trend is a 24% decrease in cycle times as you go from 0% to 100% adoption of AI

**[08:27]** as you go from 0% to 100% adoption of AI

**[08:27]** as you go from 0% to 100% adoption of AI coding tools.

**[08:30]** coding tools.

**[08:30]** coding tools. So big picture is good news for

**[08:33]** So big picture is good news for

**[08:33]** So big picture is good news for productivity gains and maybe you're

**[08:35]** productivity gains and maybe you're

**[08:35]** productivity gains and maybe you're seeing these things in your own

**[08:36]** seeing these things in your own

**[08:36]** seeing these things in your own organization but uh what about the side

**[08:39]** organization but uh what about the side

**[08:39]** organization but uh what about the side effects? We all know there's no free

**[08:40]** effects? We all know there's no free

**[08:40]** effects? We all know there's no free lunch. So, what other things change as

**[08:42]** lunch. So, what other things change as

**[08:42]** lunch. So, what other things change as you go through an AI transformation?

**[08:46]** you go through an AI transformation?

**[08:46]** you go through an AI transformation? Well, one thing we've observed is that

**[08:48]** Well, one thing we've observed is that

**[08:48]** Well, one thing we've observed is that PRs are getting bigger. So, here's a

**[08:50]** PRs are getting bigger. So, here's a

**[08:50]** PRs are getting bigger. So, here's a plot like the previous ones I've showed,

**[08:52]** plot like the previous ones I've showed,

**[08:52]** plot like the previous ones I've showed, except now the y-axis is PR size. So, on

**[08:57]** except now the y-axis is PR size. So, on

**[08:57]** except now the y-axis is PR size. So, on average, teams that have fully adopted

**[08:59]** average, teams that have fully adopted

**[08:59]** average, teams that have fully adopted AI coding tools are pushing PRs that are


### [09:00 - 10:00]

**[09:01]** AI coding tools are pushing PRs that are

**[09:01]** AI coding tools are pushing PRs that are 18% larger in terms of net lines of code

**[09:04]** 18% larger in terms of net lines of code

**[09:04]** 18% larger in terms of net lines of code added. Now that size change is due much

**[09:07]** added. Now that size change is due much

**[09:07]** added. Now that size change is due much more uh you know when I say net it's due

**[09:09]** more uh you know when I say net it's due

**[09:09]** more uh you know when I say net it's due more to additions than deletion. So that

**[09:11]** more to additions than deletion. So that

**[09:12]** more to additions than deletion. So that means that the combined change is

**[09:13]** means that the combined change is

**[09:13]** means that the combined change is primarily coming from net new code not

**[09:15]** primarily coming from net new code not

**[09:15]** primarily coming from net new code not necessarily just uh you know fully

**[09:17]** necessarily just uh you know fully

**[09:17]** necessarily just uh you know fully rewritten or heavily reworked code. Uh

**[09:21]** rewritten or heavily reworked code. Uh

**[09:21]** rewritten or heavily reworked code. Uh another kind of interesting detail is

**[09:23]** another kind of interesting detail is

**[09:23]** another kind of interesting detail is that the average number of files touched

**[09:25]** that the average number of files touched

**[09:25]** that the average number of files touched is about the same. So this change is

**[09:26]** is about the same. So this change is

**[09:26]** is about the same. So this change is more about code that's uh it's more

**[09:29]** more about code that's uh it's more

**[09:29]** more about code that's uh it's more thorough or maybe just more verbose. But

**[09:31]** thorough or maybe just more verbose. But

**[09:31]** thorough or maybe just more verbose. But it's not the case that AI is touching

**[09:33]** it's not the case that AI is touching

**[09:33]** it's not the case that AI is touching more files and changing code in more

**[09:35]** more files and changing code in more

**[09:35]** more files and changing code in more different places in in the code base.

**[09:37]** different places in in the code base.

**[09:37]** different places in in the code base. This is largely happening within the

**[09:39]** This is largely happening within the

**[09:39]** This is largely happening within the same files.

**[09:41]** same files.

**[09:41]** same files. Well, now if teams are pushing more PRs

**[09:44]** Well, now if teams are pushing more PRs

**[09:44]** Well, now if teams are pushing more PRs and writing and merging them faster and

**[09:46]** and writing and merging them faster and

**[09:46]** and writing and merging them faster and the PRs are getting bigger, then you

**[09:49]** the PRs are getting bigger, then you

**[09:49]** the PRs are getting bigger, then you might be wondering about quality. So,

**[09:51]** might be wondering about quality. So,

**[09:51]** might be wondering about quality. So, are we seeing effects on quality as we

**[09:53]** are we seeing effects on quality as we

**[09:53]** are we seeing effects on quality as we use more AI and push code faster? Well,

**[09:57]** use more AI and push code faster? Well,

**[09:57]** use more AI and push code faster? Well, right now the answer is not really.

**[09:59]** right now the answer is not really.

**[09:59]** right now the answer is not really. We're not really seeing any big effects.


### [10:00 - 11:00]

**[10:01]** We're not really seeing any big effects.

**[10:01]** We're not really seeing any big effects. We've looked at bug tickets created and

**[10:03]** We've looked at bug tickets created and

**[10:03]** We've looked at bug tickets created and we looked at rates of PR reverts code

**[10:05]** we looked at rates of PR reverts code

**[10:05]** we looked at rates of PR reverts code that had to be rolled back and we

**[10:07]** that had to be rolled back and we

**[10:07]** that had to be rolled back and we haven't found any statistically

**[10:08]** haven't found any statistically

**[10:08]** haven't found any statistically significant relationship with the rate

**[10:10]** significant relationship with the rate

**[10:10]** significant relationship with the rate of AI adoption.

**[10:12]** of AI adoption.

**[10:12]** of AI adoption. Uh interestingly we have found increases

**[10:15]** Uh interestingly we have found increases

**[10:15]** Uh interestingly we have found increases in the rates of bugs resolved. Uh when

**[10:18]** in the rates of bugs resolved. Uh when

**[10:18]** in the rates of bugs resolved. Uh when you dig into the data you find this is

**[10:20]** you dig into the data you find this is

**[10:20]** you dig into the data you find this is because um teams are disproportionately

**[10:22]** because um teams are disproportionately

**[10:22]** because um teams are disproportionately using AI to tackle bug tickets in their

**[10:24]** using AI to tackle bug tickets in their

**[10:24]** using AI to tackle bug tickets in their backlog. So you see a lot more uh bug

**[10:27]** backlog. So you see a lot more uh bug

**[10:28]** backlog. So you see a lot more uh bug tickets being um uh addressed by AI but

**[10:32]** tickets being um uh addressed by AI but

**[10:32]** tickets being um uh addressed by AI but not necessarily being caused by AI. Uh

**[10:35]** not necessarily being caused by AI. Uh

**[10:36]** not necessarily being caused by AI. Uh this makes sense. You know, bugs are

**[10:37]** this makes sense. You know, bugs are

**[10:37]** this makes sense. You know, bugs are often well scoped verifiable tasks that

**[10:39]** often well scoped verifiable tasks that

**[10:39]** often well scoped verifiable tasks that AI coding tools can be set up well to

**[10:40]** AI coding tools can be set up well to

**[10:40]** AI coding tools can be set up well to succeed at. And we're seeing uh a lot of

**[10:42]** succeed at. And we're seeing uh a lot of

**[10:42]** succeed at. And we're seeing uh a lot of people having success throwing AI at

**[10:45]** people having success throwing AI at

**[10:45]** people having success throwing AI at those kinds of tasks. Uh but basically

**[10:47]** those kinds of tasks. Uh but basically

**[10:47]** those kinds of tasks. Uh but basically there's there's no smoking gun on

**[10:49]** there's there's no smoking gun on

**[10:49]** there's there's no smoking gun on quality yet though you know we're going

**[10:52]** quality yet though you know we're going

**[10:52]** quality yet though you know we're going to keep digging in here especially as

**[10:53]** to keep digging in here especially as

**[10:54]** to keep digging in here especially as usage of of asynchronous agents grows.

**[10:58]** usage of of asynchronous agents grows.

**[10:58]** usage of of asynchronous agents grows. All right last question.


### [11:00 - 12:00]

**[11:01]** All right last question.

**[11:01]** All right last question. What if what you're seeing at your or

**[11:04]** What if what you're seeing at your or

**[11:04]** What if what you're seeing at your or doesn't align with the kind of results

**[11:06]** doesn't align with the kind of results

**[11:06]** doesn't align with the kind of results we've been talking about here so far?

**[11:08]** we've been talking about here so far?

**[11:08]** we've been talking about here so far? You know what if you're listening to

**[11:10]** You know what if you're listening to

**[11:10]** You know what if you're listening to this and it is just not your reality.

**[11:13]** this and it is just not your reality.

**[11:13]** this and it is just not your reality. Well, I think I've made it clear uh so

**[11:16]** Well, I think I've made it clear uh so

**[11:16]** Well, I think I've made it clear uh so far that the most important thing to

**[11:17]** far that the most important thing to

**[11:17]** far that the most important thing to focus on first is adoption. You're not

**[11:19]** focus on first is adoption. You're not

**[11:19]** focus on first is adoption. You're not going to see gains until you get folks

**[11:21]** going to see gains until you get folks

**[11:21]** going to see gains until you get folks using these tools at scale. I think

**[11:22]** using these tools at scale. I think

**[11:22]** using these tools at scale. I think that's common sense, but maybe you are

**[11:23]** that's common sense, but maybe you are

**[11:23]** that's common sense, but maybe you are seeing high adoption and you're still

**[11:25]** seeing high adoption and you're still

**[11:25]** seeing high adoption and you're still not seeing the kind of productivity

**[11:26]** not seeing the kind of productivity

**[11:26]** not seeing the kind of productivity gains that all your friends on LinkedIn

**[11:28]** gains that all your friends on LinkedIn

**[11:28]** gains that all your friends on LinkedIn are crowing about. So, what's going on?

**[11:32]** are crowing about. So, what's going on?

**[11:32]** are crowing about. So, what's going on? Well, we've looked at a lot of things

**[11:33]** Well, we've looked at a lot of things

**[11:33]** Well, we've looked at a lot of things here and there's plenty more to

**[11:35]** here and there's plenty more to

**[11:35]** here and there's plenty more to investigate, but I'd like to share one

**[11:37]** investigate, but I'd like to share one

**[11:37]** investigate, but I'd like to share one that's particularly interesting and uh

**[11:39]** that's particularly interesting and uh

**[11:39]** that's particularly interesting and uh that's code architecture. By code

**[11:42]** that's code architecture. By code

**[11:42]** that's code architecture. By code architecture uh what I mean is how are

**[11:46]** architecture uh what I mean is how are

**[11:46]** architecture uh what I mean is how are the code for your products and services

**[11:48]** the code for your products and services

**[11:48]** the code for your products and services organized across your repositories. So

**[11:51]** organized across your repositories. So

**[11:51]** organized across your repositories. So uh think about code being organized into

**[11:53]** uh think about code being organized into

**[11:53]** uh think about code being organized into monor repos versus poly repos and that

**[11:57]** monor repos versus poly repos and that

**[11:57]** monor repos versus poly repos and that arrangement of of your code. It could be


### [12:00 - 13:00]

**[12:00]** arrangement of of your code. It could be

**[12:00]** arrangement of of your code. It could be indicative of monolithic services versus

**[12:03]** indicative of monolithic services versus

**[12:03]** indicative of monolithic services versus microservices. It could be the

**[12:04]** microservices. It could be the

**[12:04]** microservices. It could be the difference between a centralized versus

**[12:06]** difference between a centralized versus

**[12:06]** difference between a centralized versus a more federated product strategy. Uh

**[12:09]** a more federated product strategy. Uh

**[12:09]** a more federated product strategy. Uh and the way that we actually measure

**[12:10]** and the way that we actually measure

**[12:10]** and the way that we actually measure this, you know, one key metric for

**[12:12]** this, you know, one key metric for

**[12:12]** this, you know, one key metric for understanding it is active repos per

**[12:15]** understanding it is active repos per

**[12:15]** understanding it is active repos per engineer. This is actually a pretty

**[12:16]** engineer. This is actually a pretty

**[12:16]** engineer. This is actually a pretty straightforward one. It's just how many

**[12:18]** straightforward one. It's just how many

**[12:18]** straightforward one. It's just how many distinct repos typical engineer uh

**[12:22]** distinct repos typical engineer uh

**[12:22]** distinct repos typical engineer uh pushes code in in a given week.

**[12:25]** pushes code in in a given week.

**[12:25]** pushes code in in a given week. One really cool thing about this metric

**[12:27]** One really cool thing about this metric

**[12:27]** One really cool thing about this metric is that it's scale independent. So it

**[12:29]** is that it's scale independent. So it

**[12:30]** is that it's scale independent. So it turns out that you know by computing

**[12:31]** turns out that you know by computing

**[12:31]** turns out that you know by computing this per engineer normalizing by the

**[12:33]** this per engineer normalizing by the

**[12:33]** this per engineer normalizing by the number of engineers you remove any

**[12:35]** number of engineers you remove any

**[12:35]** number of engineers you remove any correlation with the size of of the

**[12:37]** correlation with the size of of the

**[12:38]** correlation with the size of of the company uh with the size of the team. So

**[12:40]** company uh with the size of the team. So

**[12:40]** company uh with the size of the team. So in other words this metric it tells you

**[12:43]** in other words this metric it tells you

**[12:43]** in other words this metric it tells you something about the shape of the code

**[12:44]** something about the shape of the code

**[12:44]** something about the shape of the code that your engineers have to work with on

**[12:46]** that your engineers have to work with on

**[12:46]** that your engineers have to work with on a daily and weekly basis and it tells

**[12:48]** a daily and weekly basis and it tells

**[12:48]** a daily and weekly basis and it tells you that regardless of how big your

**[12:49]** you that regardless of how big your

**[12:49]** you that regardless of how big your company is.

**[12:52]** company is.

**[12:52]** company is. So you know this metric that that I'm

**[12:54]** So you know this metric that that I'm

**[12:54]** So you know this metric that that I'm introducing here this is what the

**[12:56]** introducing here this is what the

**[12:56]** introducing here this is what the distribution of that metric looks like.

**[12:58]** distribution of that metric looks like.

**[12:58]** distribution of that metric looks like. Uh here's a probability distribution


### [13:00 - 14:00]

**[13:00]** Uh here's a probability distribution

**[13:00]** Uh here's a probability distribution across the companies in our study. The

**[13:03]** across the companies in our study. The

**[13:03]** across the companies in our study. The more centralized architectures you can

**[13:05]** more centralized architectures you can

**[13:05]** more centralized architectures you can see on the left uh and then there's a

**[13:06]** see on the left uh and then there's a

**[13:06]** see on the left uh and then there's a long tail of highly distributed

**[13:09]** long tail of highly distributed

**[13:09]** long tail of highly distributed architectures to the right and then more

**[13:11]** architectures to the right and then more

**[13:11]** architectures to the right and then more balanced architectures, you know,

**[13:12]** balanced architectures, you know,

**[13:12]** balanced architectures, you know, balanced and lightly distributed line

**[13:14]** balanced and lightly distributed line

**[13:14]** balanced and lightly distributed line between these two extremes. So we we've

**[13:16]** between these two extremes. So we we've

**[13:16]** between these two extremes. So we we've got these four regimes as you increase

**[13:20]** got these four regimes as you increase

**[13:20]** got these four regimes as you increase um the active repos per engineer.

**[13:23]** um the active repos per engineer.

**[13:23]** um the active repos per engineer. So you know, here's where it gets really

**[13:26]** So you know, here's where it gets really

**[13:26]** So you know, here's where it gets really interesting. So remember those 2x gains

**[13:29]** interesting. So remember those 2x gains

**[13:29]** interesting. So remember those 2x gains in PR throughput that I showed you

**[13:31]** in PR throughput that I showed you

**[13:31]** in PR throughput that I showed you before. Here's a flashback. Remember

**[13:33]** before. Here's a flashback. Remember

**[13:33]** before. Here's a flashback. Remember this. Uh well, if we take this plot, you

**[13:36]** this. Uh well, if we take this plot, you

**[13:36]** this. Uh well, if we take this plot, you know, take all these data points, all

**[13:37]** know, take all these data points, all

**[13:37]** know, take all these data points, all these different companies, and you

**[13:40]** these different companies, and you

**[13:40]** these different companies, and you segment on um this active repos per

**[13:43]** segment on um this active repos per

**[13:43]** segment on um this active repos per engineer.

**[13:45]** engineer.

**[13:45]** engineer. We've got, you know, four different

**[13:47]** We've got, you know, four different

**[13:47]** We've got, you know, four different regimes that we can do this analysis in.

**[13:49]** regimes that we can do this analysis in.

**[13:49]** regimes that we can do this analysis in. So we've got centralized, balanced,

**[13:51]** So we've got centralized, balanced,

**[13:51]** So we've got centralized, balanced, distributed, and highly distributed. And

**[13:54]** distributed, and highly distributed. And

**[13:54]** distributed, and highly distributed. And if we perform that same analysis, we see

**[13:56]** if we perform that same analysis, we see

**[13:56]** if we perform that same analysis, we see big differences. So looking at that top

**[13:59]** big differences. So looking at that top

**[13:59]** big differences. So looking at that top row, you can see centralized and


### [14:00 - 15:00]

**[14:01]** row, you can see centralized and

**[14:01]** row, you can see centralized and balanced code architectures,

**[14:04]** balanced code architectures,

**[14:04]** balanced code architectures, uh, they trend more like 4x, not like

**[14:06]** uh, they trend more like 4x, not like

**[14:06]** uh, they trend more like 4x, not like 2x. So they're doing much better than

**[14:08]** 2x. So they're doing much better than

**[14:08]** 2x. So they're doing much better than the average. And the distributed

**[14:10]** the average. And the distributed

**[14:10]** the average. And the distributed architecture there, uh, in the the lower

**[14:13]** architecture there, uh, in the the lower

**[14:13]** architecture there, uh, in the the lower leftand corner in the teal, that that

**[14:15]** leftand corner in the teal, that that

**[14:15]** leftand corner in the teal, that that looks more like that global 2x trend

**[14:17]** looks more like that global 2x trend

**[14:17]** looks more like that global 2x trend that we see when you look at all the

**[14:18]** that we see when you look at all the

**[14:18]** that we see when you look at all the data. What's really interesting is this

**[14:21]** data. What's really interesting is this

**[14:21]** data. What's really interesting is this highly distributed case. There's

**[14:22]** highly distributed case. There's

**[14:22]** highly distributed case. There's essentially no correlation here between

**[14:24]** essentially no correlation here between

**[14:24]** essentially no correlation here between AI adoption and PR throughput. Um, and

**[14:28]** AI adoption and PR throughput. Um, and

**[14:28]** AI adoption and PR throughput. Um, and actually the the weak trend that does

**[14:29]** actually the the weak trend that does

**[14:29]** actually the the weak trend that does exist is actually slightly negative. So

**[14:33]** exist is actually slightly negative. So

**[14:33]** exist is actually slightly negative. So what's what's going on here? Like why

**[14:35]** what's what's going on here? Like why

**[14:35]** what's what's going on here? Like why are teams with highly distributed

**[14:36]** are teams with highly distributed

**[14:36]** are teams with highly distributed architectures struggling? They don't

**[14:38]** architectures struggling? They don't

**[14:38]** architectures struggling? They don't seem to be getting real gains, at least

**[14:40]** seem to be getting real gains, at least

**[14:40]** seem to be getting real gains, at least not on average from AI. Well, a big part

**[14:44]** not on average from AI. Well, a big part

**[14:44]** not on average from AI. Well, a big part of what you're seeing here is really the

**[14:46]** of what you're seeing here is really the

**[14:46]** of what you're seeing here is really the problem of context. So most of today's

**[14:48]** problem of context. So most of today's

**[14:48]** problem of context. So most of today's tools are really set up uh best to work

**[14:51]** tools are really set up uh best to work

**[14:51]** tools are really set up uh best to work with one repo at a time. You know, we've

**[14:53]** with one repo at a time. You know, we've

**[14:53]** with one repo at a time. You know, we've used these uh you know, you pick a repo

**[14:55]** used these uh you know, you pick a repo

**[14:55]** used these uh you know, you pick a repo and and you dive in and combining

**[14:57]** and and you dive in and combining

**[14:57]** and and you dive in and combining context across repos, it's often

**[14:59]** context across repos, it's often

**[14:59]** context across repos, it's often challenging. It's challenging uh for


### [15:00 - 16:00]

**[15:01]** challenging. It's challenging uh for

**[15:01]** challenging. It's challenging uh for humans as well as for coding tools and

**[15:03]** humans as well as for coding tools and

**[15:03]** humans as well as for coding tools and for agents. Uh moreover,

**[15:06]** for agents. Uh moreover,

**[15:06]** for agents. Uh moreover, the relationships between these repos

**[15:08]** the relationships between these repos

**[15:08]** the relationships between these repos and the systems and products they relate

**[15:10]** and the systems and products they relate

**[15:10]** and the systems and products they relate to, they're often not even written down

**[15:12]** to, they're often not even written down

**[15:12]** to, they're often not even written down very clearly. They might be largely

**[15:14]** very clearly. They might be largely

**[15:14]** very clearly. They might be largely locked in the heads of senior engineers.

**[15:16]** locked in the heads of senior engineers.

**[15:16]** locked in the heads of senior engineers. they're definitely not accessible often

**[15:18]** they're definitely not accessible often

**[15:18]** they're definitely not accessible often to coding tools and agents. So, it's

**[15:20]** to coding tools and agents. So, it's

**[15:20]** to coding tools and agents. So, it's going to take some time for for teams to

**[15:22]** going to take some time for for teams to

**[15:22]** going to take some time for for teams to invest in the context engineering that's

**[15:24]** invest in the context engineering that's

**[15:24]** invest in the context engineering that's needed here. It's an interesting

**[15:26]** needed here. It's an interesting

**[15:26]** needed here. It's an interesting challenge and especially you know in

**[15:28]** challenge and especially you know in

**[15:28]** challenge and especially you know in light of the fact that uh a lot of folks

**[15:30]** light of the fact that uh a lot of folks

**[15:30]** light of the fact that uh a lot of folks are saying you may have heard this too

**[15:32]** are saying you may have heard this too

**[15:32]** are saying you may have heard this too that microservices are the right way to

**[15:34]** that microservices are the right way to

**[15:34]** that microservices are the right way to go for a native development. So I could

**[15:37]** go for a native development. So I could

**[15:37]** go for a native development. So I could see a world certainly where we solve

**[15:39]** see a world certainly where we solve

**[15:39]** see a world certainly where we solve these context challenges. We adopt

**[15:41]** these context challenges. We adopt

**[15:41]** these context challenges. We adopt autonomous agents at scale. They're set

**[15:43]** autonomous agents at scale. They're set

**[15:43]** autonomous agents at scale. They're set up for success and this whole thing

**[15:44]** up for success and this whole thing

**[15:44]** up for success and this whole thing flips and this highly distributed

**[15:46]** flips and this highly distributed

**[15:46]** flips and this highly distributed category becomes the most productive way

**[15:48]** category becomes the most productive way

**[15:48]** category becomes the most productive way to do things. But right now this is what

**[15:51]** to do things. But right now this is what

**[15:51]** to do things. But right now this is what we're seeing out in the world. Um as an

**[15:54]** we're seeing out in the world. Um as an

**[15:54]** we're seeing out in the world. Um as an aside, another thing you might notice

**[15:55]** aside, another thing you might notice

**[15:55]** aside, another thing you might notice here is that all of these distributions

**[15:57]** here is that all of these distributions

**[15:57]** here is that all of these distributions they you know as you go from the most

**[15:59]** they you know as you go from the most

**[15:59]** they you know as you go from the most centralized to the most distributed uh


### [16:00 - 17:00]

**[16:02]** centralized to the most distributed uh

**[16:02]** centralized to the most distributed uh these uh you know this um PR per

**[16:04]** these uh you know this um PR per

**[16:04]** these uh you know this um PR per engineer uh shifts upward uh you know

**[16:08]** engineer uh shifts upward uh you know

**[16:08]** engineer uh shifts upward uh you know what's happening is the absolute number

**[16:09]** what's happening is the absolute number

**[16:09]** what's happening is the absolute number of repos uh increases as architectures

**[16:13]** of repos uh increases as architectures

**[16:13]** of repos uh increases as architectures get more distributed. Basically, in a

**[16:15]** get more distributed. Basically, in a

**[16:15]** get more distributed. Basically, in a highly distributed architecture, it just

**[16:17]** highly distributed architecture, it just

**[16:17]** highly distributed architecture, it just takes more PRs overall to get things

**[16:18]** takes more PRs overall to get things

**[16:18]** takes more PRs overall to get things done due to things like migrations,

**[16:20]** done due to things like migrations,

**[16:20]** done due to things like migrations, cross reaper coordination. And I bring

**[16:21]** cross reaper coordination. And I bring

**[16:21]** cross reaper coordination. And I bring this up because this is one of the many

**[16:23]** this up because this is one of the many

**[16:23]** this up because this is one of the many reasons why counting PRs in the absolute

**[16:25]** reasons why counting PRs in the absolute

**[16:25]** reasons why counting PRs in the absolute sense isn't isn't a great metric. You

**[16:27]** sense isn't isn't a great metric. You

**[16:27]** sense isn't isn't a great metric. You really need to be tracking change in PR

**[16:29]** really need to be tracking change in PR

**[16:29]** really need to be tracking change in PR throughput to understand productivity.

**[16:31]** throughput to understand productivity.

**[16:31]** throughput to understand productivity. Uh because these things vary due to to

**[16:35]** Uh because these things vary due to to

**[16:35]** Uh because these things vary due to to factors like architecture choices.

**[16:38]** factors like architecture choices.

**[16:38]** factors like architecture choices. Okay, so that's it. Uh to recap, you

**[16:41]** Okay, so that's it. Uh to recap, you

**[16:41]** Okay, so that's it. Uh to recap, you know, probably not news to anyone uh

**[16:43]** know, probably not news to anyone uh

**[16:43]** know, probably not news to anyone uh watching this, but AI coding tools are

**[16:45]** watching this, but AI coding tools are

**[16:45]** watching this, but AI coding tools are being used in a big way. Autonomous

**[16:47]** being used in a big way. Autonomous

**[16:47]** being used in a big way. Autonomous agents though, not so much. It's still

**[16:49]** agents though, not so much. It's still

**[16:49]** agents though, not so much. It's still uh still early days. Uh we're seeing big

**[16:52]** uh still early days. Uh we're seeing big

**[16:52]** uh still early days. Uh we're seeing big productivity gains with mo more code

**[16:54]** productivity gains with mo more code

**[16:54]** productivity gains with mo more code being shipped and faster. Even if all

**[16:57]** being shipped and faster. Even if all

**[16:57]** being shipped and faster. Even if all you're using is interactive AI coding

**[16:59]** you're using is interactive AI coding

**[16:59]** you're using is interactive AI coding tools like Copilot, Cursor, and Cloud


### [17:00 - 18:00]

**[17:01]** tools like Copilot, Cursor, and Cloud

**[17:01]** tools like Copilot, Cursor, and Cloud Code, you feel like maybe, you know,

**[17:03]** Code, you feel like maybe, you know,

**[17:03]** Code, you feel like maybe, you know, you're not uh as up on agentic, you

**[17:06]** you're not uh as up on agentic, you

**[17:06]** you're not uh as up on agentic, you know, fully autonomous agentic coding as

**[17:08]** know, fully autonomous agentic coding as

**[17:08]** know, fully autonomous agentic coding as you ought to be. two exchange of PR

**[17:09]** you ought to be. two exchange of PR

**[17:10]** you ought to be. two exchange of PR throughput uh should be your your

**[17:12]** throughput uh should be your your

**[17:12]** throughput uh should be your your expectation. You should you should be

**[17:13]** expectation. You should you should be

**[17:13]** expectation. You should you should be seeing that or more. Um but also you

**[17:16]** seeing that or more. Um but also you

**[17:16]** seeing that or more. Um but also you should expect bigger PRs. Uh but maybe

**[17:19]** should expect bigger PRs. Uh but maybe

**[17:19]** should expect bigger PRs. Uh but maybe we can all ease up on some extreme

**[17:22]** we can all ease up on some extreme

**[17:22]** we can all ease up on some extreme quality anxiety. Like we want to keep an

**[17:24]** quality anxiety. Like we want to keep an

**[17:24]** quality anxiety. Like we want to keep an eye on that, but we're just not seeing

**[17:25]** eye on that, but we're just not seeing

**[17:25]** eye on that, but we're just not seeing big issues there. At least not yet. And

**[17:28]** big issues there. At least not yet. And

**[17:28]** big issues there. At least not yet. And finally, there are a lot of reasons why

**[17:30]** finally, there are a lot of reasons why

**[17:30]** finally, there are a lot of reasons why your mileage may vary and we're going to

**[17:32]** your mileage may vary and we're going to

**[17:32]** your mileage may vary and we're going to continue looking at this. But one place

**[17:34]** continue looking at this. But one place

**[17:34]** continue looking at this. But one place you can start is to think about your

**[17:36]** you can start is to think about your

**[17:36]** you can start is to think about your code architecture. how it might be

**[17:37]** code architecture. how it might be

**[17:37]** code architecture. how it might be holding you back, what you can do um you

**[17:40]** holding you back, what you can do um you

**[17:40]** holding you back, what you can do um you know to to compensate for some of the

**[17:43]** know to to compensate for some of the

**[17:43]** know to to compensate for some of the context limitations you have and

**[17:44]** context limitations you have and

**[17:44]** context limitations you have and ultimately try to unlock some of those

**[17:46]** ultimately try to unlock some of those

**[17:46]** ultimately try to unlock some of those uh the sweet AI productivity gains. So

**[17:50]** uh the sweet AI productivity gains. So

**[17:50]** uh the sweet AI productivity gains. So that's it. That's all I've got. I'm

**[17:52]** that's it. That's all I've got. I'm

**[17:52]** that's it. That's all I've got. I'm Nicholas Arcolano, head of research at

**[17:54]** Nicholas Arcolano, head of research at

**[17:54]** Nicholas Arcolano, head of research at Jellyfish. Thank you so much for

**[17:55]** Jellyfish. Thank you so much for

**[17:55]** Jellyfish. Thank you so much for listening.


