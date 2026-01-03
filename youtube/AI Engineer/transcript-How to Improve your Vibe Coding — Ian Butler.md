# How to Improve your Vibe Coding — Ian Butler

**Video URL:** https://www.youtube.com/watch?v=g03m-WFEu1U

---

## Full Transcript

### [00:00 - 01:00]

**[00:17]** My name is Ian. Um I'm the CEO of

**[00:17]** My name is Ian. Um I'm the CEO of Bismouth. Uh we're an endto-end agentic

**[00:19]** Bismouth. Uh we're an endto-end agentic

**[00:19]** Bismouth. Uh we're an endto-end agentic coding solution kind of like Codeex. Um

**[00:21]** coding solution kind of like Codeex. Um

**[00:21]** coding solution kind of like Codeex. Um we've been working on evals for how good

**[00:24]** we've been working on evals for how good

**[00:24]** we've been working on evals for how good agents are at finding and fixing bugs

**[00:26]** agents are at finding and fixing bugs

**[00:26]** agents are at finding and fixing bugs for the last several months. uh and we

**[00:28]** for the last several months. uh and we

**[00:28]** for the last several months. uh and we dropped a benchmark yesterday uh

**[00:30]** dropped a benchmark yesterday uh

**[00:30]** dropped a benchmark yesterday uh discussing our results. Um so one thing

**[00:33]** discussing our results. Um so one thing

**[00:33]** discussing our results. Um so one thing to point out about agents currently is

**[00:35]** to point out about agents currently is

**[00:35]** to point out about agents currently is that they have a pretty low overall find

**[00:37]** that they have a pretty low overall find

**[00:37]** that they have a pretty low overall find rate for bugs. They actually generate a

**[00:39]** rate for bugs. They actually generate a

**[00:39]** rate for bugs. They actually generate a significant amount of false positives.

**[00:41]** significant amount of false positives.

**[00:41]** significant amount of false positives. Um you can see something like Devon and

**[00:43]** Um you can see something like Devon and

**[00:43]** Um you can see something like Devon and Cursor have a less than 10% true

**[00:45]** Cursor have a less than 10% true

**[00:45]** Cursor have a less than 10% true positive rate for finding bugs. Um, this

**[00:48]** positive rate for finding bugs. Um, this

**[00:48]** positive rate for finding bugs. Um, this is an issue when you're vibe coding

**[00:50]** is an issue when you're vibe coding

**[00:50]** is an issue when you're vibe coding because these agents can quickly overrun

**[00:52]** because these agents can quickly overrun

**[00:52]** because these agents can quickly overrun your codebase with unintended bugs that

**[00:54]** your codebase with unintended bugs that

**[00:54]** your codebase with unintended bugs that they're not able to actually find and

**[00:56]** they're not able to actually find and

**[00:56]** they're not able to actually find and then later then fix. Um, overall too,


### [01:00 - 02:00]

**[01:00]** then later then fix. Um, overall too,

**[01:00]** then later then fix. Um, overall too, it's worth noting uh that in terms of

**[01:03]** it's worth noting uh that in terms of

**[01:03]** it's worth noting uh that in terms of needle in a haystack when we plant bugs

**[01:05]** needle in a haystack when we plant bugs

**[01:05]** needle in a haystack when we plant bugs in a codebase, these agents struggle to

**[01:07]** in a codebase, these agents struggle to

**[01:07]** in a codebase, these agents struggle to navigate more broadly across those

**[01:09]** navigate more broadly across those

**[01:09]** navigate more broadly across those larger code bases and actually find the

**[01:11]** larger code bases and actually find the

**[01:11]** larger code bases and actually find the specific bugs.

**[01:14]** specific bugs.

**[01:14]** specific bugs. So, here's the hard truth, right? uh

**[01:16]** So, here's the hard truth, right? uh

**[01:16]** So, here's the hard truth, right? uh three out of six agents on our benchmark

**[01:18]** three out of six agents on our benchmark

**[01:18]** three out of six agents on our benchmark had a 10% or less true positive rate out

**[01:21]** had a 10% or less true positive rate out

**[01:21]** had a 10% or less true positive rate out of 900 plus reports. Um one agent

**[01:24]** of 900 plus reports. Um one agent

**[01:24]** of 900 plus reports. Um one agent actually gave us 70 issues for a single

**[01:26]** actually gave us 70 issues for a single

**[01:26]** actually gave us 70 issues for a single task and all of them were false and like

**[01:28]** task and all of them were false and like

**[01:28]** task and all of them were false and like no developer is going to go through all

**[01:30]** no developer is going to go through all

**[01:30]** no developer is going to go through all of those, right? You're not going to sit

**[01:31]** of those, right? You're not going to sit

**[01:31]** of those, right? You're not going to sit there and try to like figure out what

**[01:34]** there and try to like figure out what

**[01:34]** there and try to like figure out what bugs actually exist.

**[01:36]** bugs actually exist.

**[01:36]** bugs actually exist. Um so bad vibes, right? Implications.

**[01:39]** Um so bad vibes, right? Implications.

**[01:39]** Um so bad vibes, right? Implications. Most popular agents are terrible at

**[01:40]** Most popular agents are terrible at

**[01:40]** Most popular agents are terrible at finding bugs. Cursor had a 97% false

**[01:44]** finding bugs. Cursor had a 97% false

**[01:44]** finding bugs. Cursor had a 97% false positive rate over 100 plus repos and

**[01:46]** positive rate over 100 plus repos and

**[01:46]** positive rate over 100 plus repos and 1,200 plus issues. The real world impact

**[01:48]** 1,200 plus issues. The real world impact

**[01:48]** 1,200 plus issues. The real world impact for this is that when developers are

**[01:50]** for this is that when developers are

**[01:50]** for this is that when developers are actually building with this software,

**[01:52]** actually building with this software,

**[01:52]** actually building with this software, there's alert fatigue and it reduces the

**[01:54]** there's alert fatigue and it reduces the

**[01:54]** there's alert fatigue and it reduces the effectiveness of trusting these agents

**[01:55]** effectiveness of trusting these agents

**[01:55]** effectiveness of trusting these agents which means bugs are going to go to

**[01:57]** which means bugs are going to go to

**[01:57]** which means bugs are going to go to prod.

**[01:59]** prod.

**[01:59]** prod. So how do you clean up some of the


### [02:00 - 03:00]

**[02:00]** So how do you clean up some of the

**[02:00]** So how do you clean up some of the vibes? Like we did this large benchmark.

**[02:03]** vibes? Like we did this large benchmark.

**[02:03]** vibes? Like we did this large benchmark. We've been doing this for months. We

**[02:04]** We've been doing this for months. We

**[02:04]** We've been doing this for months. We have like practical tips for you when

**[02:06]** have like practical tips for you when

**[02:06]** have like practical tips for you when you're working kind of in your IDE with

**[02:07]** you're working kind of in your IDE with

**[02:07]** you're working kind of in your IDE with these agents side by side. So the first

**[02:10]** these agents side by side. So the first

**[02:10]** these agents side by side. So the first thing to note is bug focused rules. Um

**[02:13]** thing to note is bug focused rules. Um

**[02:13]** thing to note is bug focused rules. Um every one of these agents has a rules

**[02:15]** every one of these agents has a rules

**[02:15]** every one of these agents has a rules types of file. You want to basically

**[02:16]** types of file. You want to basically

**[02:16]** types of file. You want to basically provide scoped instructions that provide

**[02:18]** provide scoped instructions that provide

**[02:18]** provide scoped instructions that provide additional detail on security issues,

**[02:21]** additional detail on security issues,

**[02:21]** additional detail on security issues, logical bugs, things like that. The

**[02:24]** logical bugs, things like that. The

**[02:24]** logical bugs, things like that. The second issue here is context management.

**[02:26]** second issue here is context management.

**[02:26]** second issue here is context management. So the biggest issue we saw with agents

**[02:27]** So the biggest issue we saw with agents

**[02:27]** So the biggest issue we saw with agents when navigating code bases was after a

**[02:29]** when navigating code bases was after a

**[02:30]** when navigating code bases was after a little bit of time they'd get confused.

**[02:31]** little bit of time they'd get confused.

**[02:31]** little bit of time they'd get confused. they would lose logical links to stuff

**[02:33]** they would lose logical links to stuff

**[02:33]** they would lose logical links to stuff they've already read and their ability

**[02:34]** they've already read and their ability

**[02:34]** they've already read and their ability to reason and come up with connections

**[02:36]** to reason and come up with connections

**[02:36]** to reason and come up with connections across a codebase stumbled

**[02:38]** across a codebase stumbled

**[02:38]** across a codebase stumbled significantly.

**[02:40]** significantly.

**[02:40]** significantly. Obviously, when it comes to finding

**[02:41]** Obviously, when it comes to finding

**[02:41]** Obviously, when it comes to finding bugs, this is a problem because most

**[02:43]** bugs, this is a problem because most

**[02:43]** bugs, this is a problem because most significant and real bugs are complex

**[02:44]** significant and real bugs are complex

**[02:44]** significant and real bugs are complex multi-step processes that are nested

**[02:46]** multi-step processes that are nested

**[02:46]** multi-step processes that are nested deeply in code bases.

**[02:48]** deeply in code bases.

**[02:48]** deeply in code bases. And then finally, thinking models rock.

**[02:50]** And then finally, thinking models rock.

**[02:50]** And then finally, thinking models rock. Um, thinking models were significantly

**[02:52]** Um, thinking models were significantly

**[02:52]** Um, thinking models were significantly better um at finding bugs in a codebase.

**[02:54]** better um at finding bugs in a codebase.

**[02:54]** better um at finding bugs in a codebase. So, whenever you're using something like

**[02:56]** So, whenever you're using something like

**[02:56]** So, whenever you're using something like cloud code, cursor, whatever, try to

**[02:58]** cloud code, cursor, whatever, try to

**[02:58]** cloud code, cursor, whatever, try to reach for thinking models. they are just

**[02:59]** reach for thinking models. they are just

**[02:59]** reach for thinking models. they are just significantly better at this problem.


### [03:00 - 04:00]

**[03:03]** significantly better at this problem.

**[03:03]** significantly better at this problem. Um, okay. So, I mentioned rules earlier

**[03:05]** Um, okay. So, I mentioned rules earlier

**[03:05]** Um, okay. So, I mentioned rules earlier and I think there's some like practical

**[03:07]** and I think there's some like practical

**[03:07]** and I think there's some like practical tips you can take away for improving

**[03:08]** tips you can take away for improving

**[03:08]** tips you can take away for improving your vibe coding. Um, OASP is like the

**[03:11]** your vibe coding. Um, OASP is like the

**[03:11]** your vibe coding. Um, OASP is like the world's most popular kind of like, you

**[03:13]** world's most popular kind of like, you

**[03:13]** world's most popular kind of like, you know, security authority for bugs. Um, I

**[03:15]** know, security authority for bugs. Um, I

**[03:16]** know, security authority for bugs. Um, I would say give or take. Um, when you're

**[03:18]** would say give or take. Um, when you're

**[03:18]** would say give or take. Um, when you're creating your rules files, try to feed

**[03:20]** creating your rules files, try to feed

**[03:20]** creating your rules files, try to feed some specific security information like

**[03:22]** some specific security information like

**[03:22]** some specific security information like the OAS top 10 to the model. What you're

**[03:24]** the OAS top 10 to the model. What you're

**[03:24]** the OAS top 10 to the model. What you're doing here is biasing the model. So when

**[03:26]** doing here is biasing the model. So when

**[03:26]** doing here is biasing the model. So when it's actually looking at your code, it's

**[03:27]** it's actually looking at your code, it's

**[03:28]** it's actually looking at your code, it's considering these things in the first

**[03:29]** considering these things in the first

**[03:29]** considering these things in the first place. Right now we find when you don't

**[03:31]** place. Right now we find when you don't

**[03:31]** place. Right now we find when you don't actually supply models with security or

**[03:33]** actually supply models with security or

**[03:33]** actually supply models with security or bug related information, their

**[03:34]** bug related information, their

**[03:34]** bug related information, their performance is significantly lower than

**[03:36]** performance is significantly lower than

**[03:36]** performance is significantly lower than otherwise.

**[03:38]** otherwise.

**[03:38]** otherwise. Second, you're going to want to

**[03:39]** Second, you're going to want to

**[03:39]** Second, you're going to want to prioritize naming like explicit classes

**[03:41]** prioritize naming like explicit classes

**[03:41]** prioritize naming like explicit classes of bugs in those rules. Like don't be

**[03:43]** of bugs in those rules. Like don't be

**[03:43]** of bugs in those rules. Like don't be like, "Hey cursor, just try to find me

**[03:44]** like, "Hey cursor, just try to find me

**[03:44]** like, "Hey cursor, just try to find me some bugs in this repository." Be like,

**[03:46]** some bugs in this repository." Be like,

**[03:46]** some bugs in this repository." Be like, "Hey cursor, I want you to examine my

**[03:48]** "Hey cursor, I want you to examine my

**[03:48]** "Hey cursor, I want you to examine my repository for off bypasses or protocol

**[03:50]** repository for off bypasses or protocol

**[03:50]** repository for off bypasses or protocol pollution, um SQL injection off

**[03:53]** pollution, um SQL injection off

**[03:53]** pollution, um SQL injection off bypasses." Right? You want to be

**[03:54]** bypasses." Right? You want to be

**[03:54]** bypasses." Right? You want to be explicit about this. That kind of primes

**[03:56]** explicit about this. That kind of primes

**[03:56]** explicit about this. That kind of primes the models to be looking for these

**[03:58]** the models to be looking for these

**[03:58]** the models to be looking for these issues. And then finally with rules, you


### [04:00 - 05:00]

**[04:01]** issues. And then finally with rules, you

**[04:01]** issues. And then finally with rules, you want to require kind of like fix

**[04:02]** want to require kind of like fix

**[04:02]** want to require kind of like fix validation. So you always want to tell

**[04:03]** validation. So you always want to tell

**[04:03]** validation. So you always want to tell the model, hey, you have to write and

**[04:04]** the model, hey, you have to write and

**[04:04]** the model, hey, you have to write and get tests to pass before this is coming

**[04:06]** get tests to pass before this is coming

**[04:06]** get tests to pass before this is coming into the codebase. You have to ensure

**[04:07]** into the codebase. You have to ensure

**[04:07]** into the codebase. You have to ensure they've actually fixed the bugs.

**[04:10]** they've actually fixed the bugs.

**[04:10]** they've actually fixed the bugs. We've seen more broadly across the

**[04:12]** We've seen more broadly across the

**[04:12]** We've seen more broadly across the hundred repositories we benchmarked and

**[04:14]** hundred repositories we benchmarked and

**[04:14]** hundred repositories we benchmarked and the thousands of issues we've seen from

**[04:15]** the thousands of issues we've seen from

**[04:15]** the thousands of issues we've seen from many agents uh that structured rules

**[04:17]** many agents uh that structured rules

**[04:17]** many agents uh that structured rules eliminate the vague check for bugs

**[04:19]** eliminate the vague check for bugs

**[04:19]** eliminate the vague check for bugs requests uh and that produce alert

**[04:21]** requests uh and that produce alert

**[04:21]** requests uh and that produce alert fatigue. um instead they prime agents

**[04:23]** fatigue. um instead they prime agents

**[04:23]** fatigue. um instead they prime agents for much higher quality output.

**[04:26]** for much higher quality output.

**[04:26]** for much higher quality output. So okay, context is key too, right? So I

**[04:28]** So okay, context is key too, right? So I

**[04:28]** So okay, context is key too, right? So I mentioned agents struggle significantly

**[04:30]** mentioned agents struggle significantly

**[04:30]** mentioned agents struggle significantly with like cross repo, you know,

**[04:32]** with like cross repo, you know,

**[04:32]** with like cross repo, you know, navigation um and understanding. Um in

**[04:35]** navigation um and understanding. Um in

**[04:35]** navigation um and understanding. Um in fact, a lot of the agents when they

**[04:36]** fact, a lot of the agents when they

**[04:36]** fact, a lot of the agents when they reach their context limits kind of like

**[04:37]** reach their context limits kind of like

**[04:38]** reach their context limits kind of like summarize or compact files down. When

**[04:40]** summarize or compact files down. When

**[04:40]** summarize or compact files down. When that compaction happens, uh the ability

**[04:42]** that compaction happens, uh the ability

**[04:42]** that compaction happens, uh the ability to detect and understand bugs reduces

**[04:43]** to detect and understand bugs reduces

**[04:43]** to detect and understand bugs reduces significantly. So it's actually on you

**[04:46]** significantly. So it's actually on you

**[04:46]** significantly. So it's actually on you as users in the IDE to kind of manage

**[04:47]** as users in the IDE to kind of manage

**[04:48]** as users in the IDE to kind of manage your context more thoroughly for these

**[04:49]** your context more thoroughly for these

**[04:49]** your context more thoroughly for these agents. You want to make sure you're

**[04:51]** agents. You want to make sure you're

**[04:51]** agents. You want to make sure you're feeding uh you know either diffs of the

**[04:53]** feeding uh you know either diffs of the

**[04:54]** feeding uh you know either diffs of the code uh that was changed to the agent.

**[04:55]** code uh that was changed to the agent.

**[04:55]** code uh that was changed to the agent. They're able to actually understand

**[04:57]** They're able to actually understand

**[04:57]** They're able to actually understand cause and effect better from that. You

**[04:58]** cause and effect better from that. You

**[04:58]** cause and effect better from that. You want to make sure key files aren't being


### [05:00 - 06:00]

**[05:00]** want to make sure key files aren't being

**[05:00]** want to make sure key files aren't being summarized or being taken out of the

**[05:02]** summarized or being taken out of the

**[05:02]** summarized or being taken out of the context window. Um

**[05:05]** context window. Um

**[05:05]** context window. Um and you want to actually ask one one one

**[05:07]** and you want to actually ask one one one

**[05:07]** and you want to actually ask one one one thing we found really effective in the

**[05:08]** thing we found really effective in the

**[05:08]** thing we found really effective in the benchmarking was asking agents to come

**[05:10]** benchmarking was asking agents to come

**[05:10]** benchmarking was asking agents to come up with a uh step-by-step component

**[05:13]** up with a uh step-by-step component

**[05:13]** up with a uh step-by-step component inventory of your code. So have it index

**[05:15]** inventory of your code. So have it index

**[05:15]** inventory of your code. So have it index like these are the classes, these are

**[05:17]** like these are the classes, these are

**[05:17]** like these are the classes, these are the variables, um this is how the use is

**[05:20]** the variables, um this is how the use is

**[05:20]** the variables, um this is how the use is happening across the codebase. When it

**[05:22]** happening across the codebase. When it

**[05:22]** happening across the codebase. When it does that inventory, it becomes much

**[05:23]** does that inventory, it becomes much

**[05:24]** does that inventory, it becomes much more able to find bugs.

**[05:30]** So okay,

**[05:30]** So okay, thinking models rock. Um we saw across

**[05:33]** thinking models rock. Um we saw across

**[05:33]** thinking models rock. Um we saw across our benchmarking basically just

**[05:35]** our benchmarking basically just

**[05:35]** our benchmarking basically just implicitly that thinking models were far

**[05:37]** implicitly that thinking models were far

**[05:37]** implicitly that thinking models were far more able to find bugs. uh if you go

**[05:39]** more able to find bugs. uh if you go

**[05:39]** more able to find bugs. uh if you go through their thought traces, you're

**[05:40]** through their thought traces, you're

**[05:40]** through their thought traces, you're actually able to see them kind of expand

**[05:42]** actually able to see them kind of expand

**[05:42]** actually able to see them kind of expand across a few different like

**[05:43]** across a few different like

**[05:43]** across a few different like considerations in the codebase. And then

**[05:45]** considerations in the codebase. And then

**[05:45]** considerations in the codebase. And then when they find those considerations,

**[05:46]** when they find those considerations,

**[05:46]** when they find those considerations, they will actually dive deeper into the

**[05:47]** they will actually dive deeper into the

**[05:48]** they will actually dive deeper into the chain of thought uh for finding those

**[05:49]** chain of thought uh for finding those

**[05:49]** chain of thought uh for finding those bugs. That means in practice they do

**[05:51]** bugs. That means in practice they do

**[05:51]** bugs. That means in practice they do find deeper bugs than just non-thinking

**[05:53]** find deeper bugs than just non-thinking

**[05:53]** find deeper bugs than just non-thinking models are able to across the benchmark.

**[05:55]** models are able to across the benchmark.

**[05:55]** models are able to across the benchmark. However, I still want to note here even

**[05:57]** However, I still want to note here even

**[05:57]** However, I still want to note here even with thinking models, there's like a

**[05:58]** with thinking models, there's like a

**[05:58]** with thinking models, there's like a pretty significant limitation in their


### [06:00 - 07:00]

**[06:00]** pretty significant limitation in their

**[06:00]** pretty significant limitation in their ability to actually like holistically

**[06:02]** ability to actually like holistically

**[06:02]** ability to actually like holistically look at a file. We found again over

**[06:04]** look at a file. We found again over

**[06:04]** look at a file. We found again over hundreds of repos and thousands of

**[06:06]** hundreds of repos and thousands of

**[06:06]** hundreds of repos and thousands of issues that when agents were run the

**[06:08]** issues that when agents were run the

**[06:08]** issues that when agents were run the topline number of bugs found would

**[06:10]** topline number of bugs found would

**[06:10]** topline number of bugs found would remain the same but they would actually

**[06:12]** remain the same but they would actually

**[06:12]** remain the same but they would actually the bugs themselves would change runto

**[06:14]** the bugs themselves would change runto

**[06:14]** the bugs themselves would change runto run. So agents are never holistically

**[06:16]** run. So agents are never holistically

**[06:16]** run. So agents are never holistically really looking at a file like you or I

**[06:18]** really looking at a file like you or I

**[06:18]** really looking at a file like you or I would be looking at a file. There's high

**[06:20]** would be looking at a file. There's high

**[06:20]** would be looking at a file. There's high variability across runs. Um we think

**[06:24]** variability across runs. Um we think

**[06:24]** variability across runs. Um we think that's a very big limitation of current

**[06:25]** that's a very big limitation of current

**[06:25]** that's a very big limitation of current agents by the way. We think for

**[06:26]** agents by the way. We think for

**[06:26]** agents by the way. We think for consumers you shouldn't have to run your

**[06:27]** consumers you shouldn't have to run your

**[06:28]** consumers you shouldn't have to run your agents a 100 times to get like the whole

**[06:29]** agents a 100 times to get like the whole

**[06:29]** agents a 100 times to get like the whole holistic kind of like bug breakdown. But

**[06:31]** holistic kind of like bug breakdown. But

**[06:31]** holistic kind of like bug breakdown. But that's kind of a still in progress

**[06:33]** that's kind of a still in progress

**[06:33]** that's kind of a still in progress problem. Um, so

**[06:37]** problem. Um, so

**[06:37]** problem. Um, so they're more thorough and they just

**[06:39]** they're more thorough and they just

**[06:39]** they're more thorough and they just perform better across the benchmark uh

**[06:41]** perform better across the benchmark uh

**[06:41]** perform better across the benchmark uh than other models were able to.

**[06:44]** than other models were able to.

**[06:44]** than other models were able to. Um, I'm going to quickly plug us. So

**[06:45]** Um, I'm going to quickly plug us. So

**[06:46]** Um, I'm going to quickly plug us. So we're bismouth.sh. Uh, we create PRs

**[06:48]** we're bismouth.sh. Uh, we create PRs

**[06:48]** we're bismouth.sh. Uh, we create PRs automatically. We're linked into GitHub,

**[06:49]** automatically. We're linked into GitHub,

**[06:49]** automatically. We're linked into GitHub, GitLab, Jira, and Linear. Uh, we scan

**[06:51]** GitLab, Jira, and Linear. Uh, we scan

**[06:51]** GitLab, Jira, and Linear. Uh, we scan for vulnerabilities. We provide reviews.

**[06:53]** for vulnerabilities. We provide reviews.

**[06:53]** for vulnerabilities. We provide reviews. Um, and we also have on-prem

**[06:54]** Um, and we also have on-prem

**[06:54]** Um, and we also have on-prem deployments, which I know is a big

**[06:55]** deployments, which I know is a big

**[06:56]** deployments, which I know is a big sticking point for people.

**[06:59]** sticking point for people.

**[06:59]** sticking point for people. Um, may your vibes be immaculate. Um, if


### [07:00 - 08:00]

**[07:01]** Um, may your vibes be immaculate. Um, if

**[07:01]** Um, may your vibes be immaculate. Um, if you scan this QR code, it'll take you to

**[07:03]** you scan this QR code, it'll take you to

**[07:03]** you scan this QR code, it'll take you to our site. There we have a link to the

**[07:04]** our site. There we have a link to the

**[07:04]** our site. There we have a link to the full benchmark with breakdown of

**[07:05]** full benchmark with breakdown of

**[07:05]** full benchmark with breakdown of methodology um, results. Uh, you can

**[07:08]** methodology um, results. Uh, you can

**[07:08]** methodology um, results. Uh, you can dive into the actual uh, data itself.

**[07:11]** dive into the actual uh, data itself.

**[07:11]** dive into the actual uh, data itself. And you can see the SM100 benchmark here

**[07:14]** And you can see the SM100 benchmark here

**[07:14]** And you can see the SM100 benchmark here um, along with our full data set and

**[07:16]** um, along with our full data set and

**[07:16]** um, along with our full data set and exploration so you can understand just

**[07:18]** exploration so you can understand just

**[07:18]** exploration so you can understand just how well current agents are actually at

**[07:20]** how well current agents are actually at

**[07:20]** how well current agents are actually at finding and fixing bugs. Um, yep. I'm

**[07:22]** finding and fixing bugs. Um, yep. I'm

**[07:22]** finding and fixing bugs. Um, yep. I'm Ian Butler. Thank you so much.

**[07:25]** Ian Butler. Thank you so much.

**[07:25]** Ian Butler. Thank you so much. [Music]


