# No Vibes Allowed- Solving Hard Problems in Complex Codebases – Dex Horthy, HumanLayer

**Video URL:** https://www.youtube.com/watch?v=rmvDxxNubIg

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** Hi everybody. How y'all doing?

**[00:24]** Hi everybody. How y'all doing? >> It's exciting. I'm Dex. Uh, as they did

**[00:26]** >> It's exciting. I'm Dex. Uh, as they did

**[00:26]** >> It's exciting. I'm Dex. Uh, as they did in the great intro, I've been hacking on

**[00:27]** in the great intro, I've been hacking on

**[00:27]** in the great intro, I've been hacking on agents for a while. Um, our talk 12

**[00:30]** agents for a while. Um, our talk 12

**[00:30]** agents for a while. Um, our talk 12 factor agents at AI engineer in June was

**[00:32]** factor agents at AI engineer in June was

**[00:32]** factor agents at AI engineer in June was one of the top talks of all time. Uh, I

**[00:35]** one of the top talks of all time. Uh, I

**[00:35]** one of the top talks of all time. Uh, I think top eight or something. One of the

**[00:36]** think top eight or something. One of the

**[00:36]** think top eight or something. One of the best ones from from AI engineer in June.

**[00:38]** best ones from from AI engineer in June.

**[00:38]** best ones from from AI engineer in June. May or may not have said something about

**[00:39]** May or may not have said something about

**[00:39]** May or may not have said something about context engineering. Um, why am I here

**[00:42]** context engineering. Um, why am I here

**[00:42]** context engineering. Um, why am I here today? What am I here to talk about? Um,

**[00:44]** today? What am I here to talk about? Um,

**[00:44]** today? What am I here to talk about? Um, I want to talk about one of my favorite

**[00:45]** I want to talk about one of my favorite

**[00:45]** I want to talk about one of my favorite talks from AI engineer in June. And I

**[00:47]** talks from AI engineer in June. And I

**[00:47]** talks from AI engineer in June. And I know we all got the update from Eigor

**[00:48]** know we all got the update from Eigor

**[00:48]** know we all got the update from Eigor yesterday, but they wouldn't let me

**[00:49]** yesterday, but they wouldn't let me

**[00:50]** yesterday, but they wouldn't let me change my slides. So, this is going to

**[00:51]** change my slides. So, this is going to

**[00:51]** change my slides. So, this is going to be about what Eigor talked about in

**[00:53]** be about what Eigor talked about in

**[00:53]** be about what Eigor talked about in June. uh basically that they surveyed a

**[00:55]** June. uh basically that they surveyed a

**[00:55]** June. uh basically that they surveyed a 100,000 developers across all company

**[00:57]** 100,000 developers across all company

**[00:57]** 100,000 developers across all company sizes and they found that most of the

**[00:59]** sizes and they found that most of the

**[00:59]** sizes and they found that most of the time you use AI for software engineering


### [01:00 - 02:00]

**[01:01]** time you use AI for software engineering

**[01:01]** time you use AI for software engineering you're doing a lot of rework a lot of

**[01:02]** you're doing a lot of rework a lot of

**[01:02]** you're doing a lot of rework a lot of codebase churn uh and it doesn't really

**[01:05]** codebase churn uh and it doesn't really

**[01:05]** codebase churn uh and it doesn't really work well for complex tasks brownfield

**[01:07]** work well for complex tasks brownfield

**[01:07]** work well for complex tasks brownfield code bases um and you can see in the

**[01:09]** code bases um and you can see in the

**[01:10]** code bases um and you can see in the chart basically you are shipping a lot

**[01:11]** chart basically you are shipping a lot

**[01:11]** chart basically you are shipping a lot more but a lot of it is just reworking

**[01:13]** more but a lot of it is just reworking

**[01:13]** more but a lot of it is just reworking the slop that you shipped last week so

**[01:16]** the slop that you shipped last week so

**[01:16]** the slop that you shipped last week so uh and then the other side right was

**[01:18]** uh and then the other side right was

**[01:18]** uh and then the other side right was that uh if you're doing green field

**[01:20]** that uh if you're doing green field

**[01:20]** that uh if you're doing green field little versel dashboard something like

**[01:22]** little versel dashboard something like

**[01:22]** little versel dashboard something like this then it's going to work great. Uh

**[01:25]** this then it's going to work great. Uh

**[01:25]** this then it's going to work great. Uh if you're going to go in a 10-year-old

**[01:27]** if you're going to go in a 10-year-old

**[01:27]** if you're going to go in a 10-year-old Java at codebase, maybe not so much. And

**[01:29]** Java at codebase, maybe not so much. And

**[01:29]** Java at codebase, maybe not so much. And this matched my experience personally

**[01:31]** this matched my experience personally

**[01:31]** this matched my experience personally and talking to a lot of founders and

**[01:32]** and talking to a lot of founders and

**[01:32]** and talking to a lot of founders and great engineers, too much slop uh tech

**[01:35]** great engineers, too much slop uh tech

**[01:35]** great engineers, too much slop uh tech debt factory. It's just it's not going

**[01:36]** debt factory. It's just it's not going

**[01:36]** debt factory. It's just it's not going to work from our codebase. Like maybe

**[01:37]** to work from our codebase. Like maybe

**[01:37]** to work from our codebase. Like maybe someday when the models get better, but

**[01:40]** someday when the models get better, but

**[01:40]** someday when the models get better, but that's what context engineering is all

**[01:41]** that's what context engineering is all

**[01:41]** that's what context engineering is all about. How can we get the most out of

**[01:43]** about. How can we get the most out of

**[01:43]** about. How can we get the most out of today's models? How do we manage our

**[01:45]** today's models? How do we manage our

**[01:45]** today's models? How do we manage our context window? So we talked about this

**[01:47]** context window? So we talked about this

**[01:47]** context window? So we talked about this in August. Um I have to confess

**[01:49]** in August. Um I have to confess

**[01:49]** in August. Um I have to confess something. The first time I used cloud

**[01:51]** something. The first time I used cloud

**[01:51]** something. The first time I used cloud code, I was not impressed. It was like,

**[01:53]** code, I was not impressed. It was like,

**[01:53]** code, I was not impressed. It was like, okay, this is a little bit better. I get

**[01:54]** okay, this is a little bit better. I get

**[01:54]** okay, this is a little bit better. I get it. I like the UX. Um, but since then,

**[01:57]** it. I like the UX. Um, but since then,

**[01:57]** it. I like the UX. Um, but since then, we as a team figured something out. Um,


### [02:00 - 03:00]

**[02:00]** we as a team figured something out. Um,

**[02:00]** we as a team figured something out. Um, that we were actually able to get, you

**[02:01]** that we were actually able to get, you

**[02:01]** that we were actually able to get, you know, 2 to 3x more throughput. And we

**[02:03]** know, 2 to 3x more throughput. And we

**[02:03]** know, 2 to 3x more throughput. And we were shipping so much that we had no

**[02:05]** were shipping so much that we had no

**[02:05]** were shipping so much that we had no choice but to change the way we

**[02:07]** choice but to change the way we

**[02:07]** choice but to change the way we collaborated. We rewired everything

**[02:09]** collaborated. We rewired everything

**[02:09]** collaborated. We rewired everything about how we build software. Uh, it was

**[02:11]** about how we build software. Uh, it was

**[02:11]** about how we build software. Uh, it was a team of three. It took eight weeks. It

**[02:13]** a team of three. It took eight weeks. It

**[02:13]** a team of three. It took eight weeks. It was really freaking hard. Uh, but now

**[02:15]** was really freaking hard. Uh, but now

**[02:15]** was really freaking hard. Uh, but now that we solved it, we're we're never

**[02:16]** that we solved it, we're we're never

**[02:16]** that we solved it, we're we're never going back. This is the whole no slop

**[02:18]** going back. This is the whole no slop

**[02:18]** going back. This is the whole no slop thing. I think I think we got somewhere

**[02:20]** thing. I think I think we got somewhere

**[02:20]** thing. I think I think we got somewhere with this went super viral on HackerNews

**[02:22]** with this went super viral on HackerNews

**[02:22]** with this went super viral on HackerNews in September. Uh we have thousands of

**[02:24]** in September. Uh we have thousands of

**[02:24]** in September. Uh we have thousands of folks who have gone on to GitHub and

**[02:25]** folks who have gone on to GitHub and

**[02:25]** folks who have gone on to GitHub and grabbed our you know research plan

**[02:26]** grabbed our you know research plan

**[02:26]** grabbed our you know research plan implement prompt system. Um so the goals

**[02:29]** implement prompt system. Um so the goals

**[02:29]** implement prompt system. Um so the goals here which we kind of backed our way

**[02:31]** here which we kind of backed our way

**[02:31]** here which we kind of backed our way into we need AI that can work well in

**[02:34]** into we need AI that can work well in

**[02:34]** into we need AI that can work well in brownfield code bases that can solve

**[02:36]** brownfield code bases that can solve

**[02:36]** brownfield code bases that can solve complex problems. No slop, right? No

**[02:39]** complex problems. No slop, right? No

**[02:39]** complex problems. No slop, right? No more slop. Uh and we had to maintain

**[02:41]** more slop. Uh and we had to maintain

**[02:42]** more slop. Uh and we had to maintain mental alignment. I'll talk a little bit

**[02:43]** mental alignment. I'll talk a little bit

**[02:43]** mental alignment. I'll talk a little bit more about what that means in a minute.

**[02:44]** more about what that means in a minute.

**[02:44]** more about what that means in a minute. And of course we want to spend with

**[02:45]** And of course we want to spend with

**[02:46]** And of course we want to spend with everything we want to spend as many

**[02:47]** everything we want to spend as many

**[02:47]** everything we want to spend as many tokens as possible. what we can offload

**[02:48]** tokens as possible. what we can offload

**[02:48]** tokens as possible. what we can offload meaningfully to the AI is really really

**[02:51]** meaningfully to the AI is really really

**[02:51]** meaningfully to the AI is really really important. Um, super high leverage. So,

**[02:53]** important. Um, super high leverage. So,

**[02:53]** important. Um, super high leverage. So, this is advanced context engineering for

**[02:55]** this is advanced context engineering for

**[02:55]** this is advanced context engineering for coding agents. Um, I'll start with kind

**[02:57]** coding agents. Um, I'll start with kind

**[02:57]** coding agents. Um, I'll start with kind of like framing this. The most naive way

**[02:59]** of like framing this. The most naive way


### [03:00 - 04:00]

**[03:00]** of like framing this. The most naive way to use a coding agent is to ask it for

**[03:02]** to use a coding agent is to ask it for

**[03:02]** to use a coding agent is to ask it for something and then tell it why it's

**[03:03]** something and then tell it why it's

**[03:03]** something and then tell it why it's wrong and resteere it and ask and ask

**[03:05]** wrong and resteere it and ask and ask

**[03:05]** wrong and resteere it and ask and ask and ask until you run out of context or

**[03:07]** and ask until you run out of context or

**[03:07]** and ask until you run out of context or you give up or you cry. Um, we can be a

**[03:10]** you give up or you cry. Um, we can be a

**[03:10]** you give up or you cry. Um, we can be a little bit smarter about this. Most

**[03:11]** little bit smarter about this. Most

**[03:11]** little bit smarter about this. Most people discover this pretty early on in

**[03:13]** people discover this pretty early on in

**[03:13]** people discover this pretty early on in their AI like exploration. uh is that it

**[03:17]** their AI like exploration. uh is that it

**[03:17]** their AI like exploration. uh is that it might be better if you start a

**[03:18]** might be better if you start a

**[03:18]** might be better if you start a conversation and you're off track that

**[03:22]** conversation and you're off track that

**[03:22]** conversation and you're off track that uh you just start a new context window.

**[03:24]** uh you just start a new context window.

**[03:24]** uh you just start a new context window. You say, "Okay, we went down that path.

**[03:25]** You say, "Okay, we went down that path.

**[03:25]** You say, "Okay, we went down that path. Let's start again. Same prompt, same

**[03:26]** Let's start again. Same prompt, same

**[03:26]** Let's start again. Same prompt, same task, but this time we're going to go

**[03:28]** task, but this time we're going to go

**[03:28]** task, but this time we're going to go down this path and like don't go over

**[03:29]** down this path and like don't go over

**[03:29]** down this path and like don't go over there cuz that doesn't work." So, uh how

**[03:32]** there cuz that doesn't work." So, uh how

**[03:32]** there cuz that doesn't work." So, uh how do you know when it's time to start

**[03:34]** do you know when it's time to start

**[03:34]** do you know when it's time to start over?

**[03:35]** over?

**[03:35]** over? If you see this,

**[03:39]** If you see this,

**[03:39]** If you see this, it's probably time to start over, right?

**[03:41]** it's probably time to start over, right?

**[03:41]** it's probably time to start over, right? This is what Claude says when you tell

**[03:43]** This is what Claude says when you tell

**[03:43]** This is what Claude says when you tell it it's screwing up.

**[03:45]** it it's screwing up.

**[03:46]** it it's screwing up. Um, so we can be even smarter about

**[03:47]** Um, so we can be even smarter about

**[03:47]** Um, so we can be even smarter about this. We can do what I call intentional

**[03:49]** this. We can do what I call intentional

**[03:49]** this. We can do what I call intentional compaction. Um, and this is basically

**[03:51]** compaction. Um, and this is basically

**[03:51]** compaction. Um, and this is basically whether you're on track or not, you can

**[03:53]** whether you're on track or not, you can

**[03:53]** whether you're on track or not, you can take uh your existing context window and

**[03:56]** take uh your existing context window and

**[03:56]** take uh your existing context window and ask the agent to compress it down into a

**[03:58]** ask the agent to compress it down into a

**[03:58]** ask the agent to compress it down into a markdown file. You can review this, you


### [04:00 - 05:00]

**[04:00]** markdown file. You can review this, you

**[04:00]** markdown file. You can review this, you can tag it, and then when the new agent

**[04:01]** can tag it, and then when the new agent

**[04:01]** can tag it, and then when the new agent starts, it gets straight to work instead

**[04:03]** starts, it gets straight to work instead

**[04:03]** starts, it gets straight to work instead of having to do all that searching and

**[04:04]** of having to do all that searching and

**[04:04]** of having to do all that searching and codebase understanding and getting

**[04:06]** codebase understanding and getting

**[04:06]** codebase understanding and getting caught up. Um, what goes into

**[04:08]** caught up. Um, what goes into

**[04:08]** caught up. Um, what goes into compaction? Well, the question is like

**[04:10]** compaction? Well, the question is like

**[04:10]** compaction? Well, the question is like what takes up space in your context

**[04:12]** what takes up space in your context

**[04:12]** what takes up space in your context window. So, um, it's looking for files,

**[04:15]** window. So, um, it's looking for files,

**[04:15]** window. So, um, it's looking for files, it's understanding code flow, it's

**[04:17]** it's understanding code flow, it's

**[04:17]** it's understanding code flow, it's editing files, it's test and build

**[04:19]** editing files, it's test and build

**[04:19]** editing files, it's test and build output. And if you have one of those

**[04:20]** output. And if you have one of those

**[04:20]** output. And if you have one of those MCPs that's dumping JSON and a bunch of

**[04:22]** MCPs that's dumping JSON and a bunch of

**[04:22]** MCPs that's dumping JSON and a bunch of UU ids into your context window, you

**[04:25]** UU ids into your context window, you

**[04:25]** UU ids into your context window, you know, God help you. Uh, so what should

**[04:27]** know, God help you. Uh, so what should

**[04:28]** know, God help you. Uh, so what should we compact? I'll get more specifics

**[04:29]** we compact? I'll get more specifics

**[04:29]** we compact? I'll get more specifics here, but this is a really good

**[04:30]** here, but this is a really good

**[04:30]** here, but this is a really good compaction. This is exactly what we're

**[04:32]** compaction. This is exactly what we're

**[04:32]** compaction. This is exactly what we're working on. The exact files and line

**[04:34]** working on. The exact files and line

**[04:34]** working on. The exact files and line numbers that matter to the problem that

**[04:35]** numbers that matter to the problem that

**[04:35]** numbers that matter to the problem that we're solving. Um, why are we so

**[04:38]** we're solving. Um, why are we so

**[04:38]** we're solving. Um, why are we so obsessed with context? Because LMS are

**[04:41]** obsessed with context? Because LMS are

**[04:41]** obsessed with context? Because LMS are actually got roasted on YouTube for this

**[04:42]** actually got roasted on YouTube for this

**[04:42]** actually got roasted on YouTube for this one. And they're not pure functions cuz

**[04:43]** one. And they're not pure functions cuz

**[04:43]** one. And they're not pure functions cuz they're nondeterministic, but they are

**[04:45]** they're nondeterministic, but they are

**[04:45]** they're nondeterministic, but they are stateless. And the only way to get

**[04:46]** stateless. And the only way to get

**[04:46]** stateless. And the only way to get better better performance out of an LLM

**[04:49]** better better performance out of an LLM

**[04:49]** better better performance out of an LLM is to put better tokens in and then you

**[04:51]** is to put better tokens in and then you

**[04:51]** is to put better tokens in and then you get better tokens out. And so every turn

**[04:53]** get better tokens out. And so every turn

**[04:53]** get better tokens out. And so every turn of the loop when Claude is picking the

**[04:54]** of the loop when Claude is picking the

**[04:54]** of the loop when Claude is picking the next tool or any coding agent is picking

**[04:56]** next tool or any coding agent is picking

**[04:56]** next tool or any coding agent is picking the next and there could be hundreds of

**[04:57]** the next and there could be hundreds of

**[04:57]** the next and there could be hundreds of right next steps and hundreds of wrong

**[04:59]** right next steps and hundreds of wrong

**[04:59]** right next steps and hundreds of wrong next steps. But the only thing that


### [05:00 - 06:00]

**[05:01]** next steps. But the only thing that

**[05:01]** next steps. But the only thing that influences what comes out next is what

**[05:03]** influences what comes out next is what

**[05:03]** influences what comes out next is what is in the conversation so far. So we're

**[05:05]** is in the conversation so far. So we're

**[05:05]** is in the conversation so far. So we're going to optimize this context window

**[05:07]** going to optimize this context window

**[05:07]** going to optimize this context window for correctness, completeness, size, and

**[05:10]** for correctness, completeness, size, and

**[05:10]** for correctness, completeness, size, and a little bit of trajectory. And the

**[05:11]** a little bit of trajectory. And the

**[05:11]** a little bit of trajectory. And the trajectory one is interesting because a

**[05:13]** trajectory one is interesting because a

**[05:13]** trajectory one is interesting because a lot of people say, "Well, I I told the

**[05:14]** lot of people say, "Well, I I told the

**[05:14]** lot of people say, "Well, I I told the agent to do something and it did

**[05:16]** agent to do something and it did

**[05:16]** agent to do something and it did [clears throat] something wrong. So, I

**[05:17]** [clears throat] something wrong. So, I

**[05:17]** [clears throat] something wrong. So, I corrected it and I yelled at it and then

**[05:19]** corrected it and I yelled at it and then

**[05:19]** corrected it and I yelled at it and then it did something wrong again and then I

**[05:20]** it did something wrong again and then I

**[05:20]** it did something wrong again and then I yelled at it." And then the LM is

**[05:21]** yelled at it." And then the LM is

**[05:21]** yelled at it." And then the LM is looking at this conversation says,

**[05:23]** looking at this conversation says,

**[05:23]** looking at this conversation says, "Okay, cool. I did something wrong. The

**[05:24]** "Okay, cool. I did something wrong. The

**[05:24]** "Okay, cool. I did something wrong. The human yelled at me and then I did

**[05:25]** human yelled at me and then I did

**[05:25]** human yelled at me and then I did something wrong and the human yelled at

**[05:26]** something wrong and the human yelled at

**[05:26]** something wrong and the human yelled at me." So, the next most likely conver

**[05:27]** me." So, the next most likely conver

**[05:27]** me." So, the next most likely conver token in this conversation is I better

**[05:30]** token in this conversation is I better

**[05:30]** token in this conversation is I better do something wrong so the human can yell

**[05:31]** do something wrong so the human can yell

**[05:31]** do something wrong so the human can yell at me again. So, mind be mindful of your

**[05:34]** at me again. So, mind be mindful of your

**[05:34]** at me again. So, mind be mindful of your trajectory. If you were going to invert

**[05:36]** trajectory. If you were going to invert

**[05:36]** trajectory. If you were going to invert this, the worst thing you can have is

**[05:37]** this, the worst thing you can have is

**[05:37]** this, the worst thing you can have is incorrect information, then missing

**[05:39]** incorrect information, then missing

**[05:39]** incorrect information, then missing information, and then just too much

**[05:41]** information, and then just too much

**[05:41]** information, and then just too much noise. Um, if you like equations,

**[05:43]** noise. Um, if you like equations,

**[05:43]** noise. Um, if you like equations, there's a dumb equation if you want to

**[05:45]** there's a dumb equation if you want to

**[05:45]** there's a dumb equation if you want to think about it this way. Um, Jeff

**[05:48]** think about it this way. Um, Jeff

**[05:48]** think about it this way. Um, Jeff Huntley uh did a lot of research on

**[05:49]** Huntley uh did a lot of research on

**[05:49]** Huntley uh did a lot of research on coding agents. Uh, he put it really

**[05:51]** coding agents. Uh, he put it really

**[05:51]** coding agents. Uh, he put it really well. Just the more you use the context

**[05:53]** well. Just the more you use the context

**[05:53]** well. Just the more you use the context window, the worse outcomes you'll get.

**[05:55]** window, the worse outcomes you'll get.

**[05:55]** window, the worse outcomes you'll get. This leads to a concept I'm in a very

**[05:56]** This leads to a concept I'm in a very

**[05:56]** This leads to a concept I'm in a very very academic concept called the dumb

**[05:58]** very academic concept called the dumb

**[05:58]** very academic concept called the dumb zone. So, you have your context window.


### [06:00 - 07:00]

**[06:01]** zone. So, you have your context window.

**[06:01]** zone. So, you have your context window. You have 168,000 tokens roughly. Some

**[06:03]** You have 168,000 tokens roughly. Some

**[06:03]** You have 168,000 tokens roughly. Some are reserved for output and compaction.

**[06:05]** are reserved for output and compaction.

**[06:05]** are reserved for output and compaction. This varies by model. Um, but we'll use

**[06:07]** This varies by model. Um, but we'll use

**[06:07]** This varies by model. Um, but we'll use cloud code as an example here. Around

**[06:09]** cloud code as an example here. Around

**[06:09]** cloud code as an example here. Around the 40% line is where you're going to

**[06:10]** the 40% line is where you're going to

**[06:10]** the 40% line is where you're going to start to see some diminishing returns

**[06:12]** start to see some diminishing returns

**[06:12]** start to see some diminishing returns depending on your task. Um, if you have

**[06:15]** depending on your task. Um, if you have

**[06:15]** depending on your task. Um, if you have too many MCPs in your coding agent, you

**[06:17]** too many MCPs in your coding agent, you

**[06:17]** too many MCPs in your coding agent, you are doing all your work in the dumb zone

**[06:18]** are doing all your work in the dumb zone

**[06:18]** are doing all your work in the dumb zone and you're never going to get good

**[06:19]** and you're never going to get good

**[06:20]** and you're never going to get good results. People talked about this. I'm

**[06:21]** results. People talked about this. I'm

**[06:22]** results. People talked about this. I'm not going to talk about that one. Your

**[06:23]** not going to talk about that one. Your

**[06:23]** not going to talk about that one. Your mileage may vary. 40% is like it depends

**[06:24]** mileage may vary. 40% is like it depends

**[06:24]** mileage may vary. 40% is like it depends on how complex the task is, but this is

**[06:26]** on how complex the task is, but this is

**[06:26]** on how complex the task is, but this is kind of a good guideline. Um so back to

**[06:29]** kind of a good guideline. Um so back to

**[06:29]** kind of a good guideline. Um so back to compaction or as I will call it from now

**[06:31]** compaction or as I will call it from now

**[06:31]** compaction or as I will call it from now on cleverly avoiding the dumb zone. Um

**[06:35]** on cleverly avoiding the dumb zone. Um

**[06:35]** on cleverly avoiding the dumb zone. Um we can do sub agents. Um if you have a

**[06:37]** we can do sub agents. Um if you have a

**[06:37]** we can do sub agents. Um if you have a front-end sub aent and a backend sub

**[06:39]** front-end sub aent and a backend sub

**[06:39]** front-end sub aent and a backend sub aent and a QA sub aent and a data data

**[06:41]** aent and a QA sub aent and a data data

**[06:41]** aent and a QA sub aent and a data data scientist sub aent

**[06:43]** scientist sub aent

**[06:43]** scientist sub aent please stop. Sub aents are not for

**[06:45]** please stop. Sub aents are not for

**[06:46]** please stop. Sub aents are not for anthropomorphizing roles. They are for

**[06:47]** anthropomorphizing roles. They are for

**[06:47]** anthropomorphizing roles. They are for controlling context. And so what you can

**[06:49]** controlling context. And so what you can

**[06:49]** controlling context. And so what you can do is if you want to go find how

**[06:51]** do is if you want to go find how

**[06:51]** do is if you want to go find how something works in a large codebase um

**[06:53]** something works in a large codebase um

**[06:53]** something works in a large codebase um you can steer the coding agent to do

**[06:55]** you can steer the coding agent to do

**[06:55]** you can steer the coding agent to do this if it supports sub agents or you

**[06:56]** this if it supports sub agents or you

**[06:56]** this if it supports sub agents or you can build your own sub agent system. But

**[06:58]** can build your own sub agent system. But

**[06:58]** can build your own sub agent system. But basically you say hey go find how this


### [07:00 - 08:00]

**[07:00]** basically you say hey go find how this

**[07:00]** basically you say hey go find how this works and it can fork out a new context

**[07:02]** works and it can fork out a new context

**[07:02]** works and it can fork out a new context window that is going to go do all that

**[07:04]** window that is going to go do all that

**[07:04]** window that is going to go do all that reading and searching and finding and

**[07:06]** reading and searching and finding and

**[07:06]** reading and searching and finding and reading entire files and understanding

**[07:07]** reading entire files and understanding

**[07:08]** reading entire files and understanding the codebase and then just return a

**[07:11]** the codebase and then just return a

**[07:11]** the codebase and then just return a really really succinct message back up

**[07:13]** really really succinct message back up

**[07:13]** really really succinct message back up to the parent agent of just like hey the

**[07:15]** to the parent agent of just like hey the

**[07:15]** to the parent agent of just like hey the file you want is here. parent agent can

**[07:18]** file you want is here. parent agent can

**[07:18]** file you want is here. parent agent can read that one file and get straight to

**[07:20]** read that one file and get straight to

**[07:20]** read that one file and get straight to work. And so this is really powerful. If

**[07:22]** work. And so this is really powerful. If

**[07:22]** work. And so this is really powerful. If you wield these correctly, you can get

**[07:24]** you wield these correctly, you can get

**[07:24]** you wield these correctly, you can get good responses like this and then you

**[07:26]** good responses like this and then you

**[07:26]** good responses like this and then you can manage your context really, really

**[07:27]** can manage your context really, really

**[07:27]** can manage your context really, really well. Um, what works even better than

**[07:29]** well. Um, what works even better than

**[07:29]** well. Um, what works even better than sub agents or like a layer on top of sub

**[07:31]** sub agents or like a layer on top of sub

**[07:31]** sub agents or like a layer on top of sub aents is a workflow I call frequent

**[07:33]** aents is a workflow I call frequent

**[07:33]** aents is a workflow I call frequent intentional compaction. We're going to

**[07:35]** intentional compaction. We're going to

**[07:35]** intentional compaction. We're going to talk about research plan implement in a

**[07:37]** talk about research plan implement in a

**[07:37]** talk about research plan implement in a minute, but like the point is you're

**[07:38]** minute, but like the point is you're

**[07:38]** minute, but like the point is you're constantly st keeping your context

**[07:40]** constantly st keeping your context

**[07:40]** constantly st keeping your context window small. You're building your

**[07:42]** window small. You're building your

**[07:42]** window small. You're building your entire workflow around context

**[07:43]** entire workflow around context

**[07:44]** entire workflow around context management. So comes in three phases.

**[07:46]** management. So comes in three phases.

**[07:46]** management. So comes in three phases. research, plan, implement. Um, and we're

**[07:49]** research, plan, implement. Um, and we're

**[07:49]** research, plan, implement. Um, and we're going to try to stay in the smart zone

**[07:50]** going to try to stay in the smart zone

**[07:50]** going to try to stay in the smart zone the whole time. So, the research is all

**[07:52]** the whole time. So, the research is all

**[07:52]** the whole time. So, the research is all about understanding how the system

**[07:53]** about understanding how the system

**[07:53]** about understanding how the system works, finding the right files, staying

**[07:55]** works, finding the right files, staying

**[07:55]** works, finding the right files, staying objective. Here's a prompt you can use

**[07:57]** objective. Here's a prompt you can use

**[07:57]** objective. Here's a prompt you can use to do research. Here's the output of um,

**[07:59]** to do research. Here's the output of um,

**[07:59]** to do research. Here's the output of um, a research prompt. These are all open


### [08:00 - 09:00]

**[08:01]** a research prompt. These are all open

**[08:01]** a research prompt. These are all open source. You can go grab them and play

**[08:02]** source. You can go grab them and play

**[08:02]** source. You can go grab them and play with them yourself. Um, planning, you're

**[08:05]** with them yourself. Um, planning, you're

**[08:05]** with them yourself. Um, planning, you're going to outline the exact steps. You're

**[08:06]** going to outline the exact steps. You're

**[08:06]** going to outline the exact steps. You're going to include file names and line

**[08:07]** going to include file names and line

**[08:07]** going to include file names and line snippets. You're going to be very

**[08:08]** snippets. You're going to be very

**[08:08]** snippets. You're going to be very explicit about how we're going to test

**[08:09]** explicit about how we're going to test

**[08:09]** explicit about how we're going to test things after every change. Here's a good

**[08:11]** things after every change. Here's a good

**[08:11]** things after every change. Here's a good planning prompt. Here's one of our

**[08:13]** planning prompt. Here's one of our

**[08:13]** planning prompt. Here's one of our plans. It's got actual code snippets in

**[08:14]** plans. It's got actual code snippets in

**[08:14]** plans. It's got actual code snippets in it. Um, and then we're gonna implement.

**[08:16]** it. Um, and then we're gonna implement.

**[08:16]** it. Um, and then we're gonna implement. And if you read one of these plans, you

**[08:18]** And if you read one of these plans, you

**[08:18]** And if you read one of these plans, you can see very easily how the dumbest

**[08:20]** can see very easily how the dumbest

**[08:20]** can see very easily how the dumbest model in the world is probably not going

**[08:21]** model in the world is probably not going

**[08:21]** model in the world is probably not going to screw this up. Um, so we just go

**[08:23]** to screw this up. Um, so we just go

**[08:23]** to screw this up. Um, so we just go through and we run the plan and we keep

**[08:25]** through and we run the plan and we keep

**[08:25]** through and we run the plan and we keep the context low. As a planning prompt,

**[08:27]** the context low. As a planning prompt,

**[08:27]** the context low. As a planning prompt, like I said, it's the least exciting

**[08:28]** like I said, it's the least exciting

**[08:28]** like I said, it's the least exciting part of the process. Um, I wanted to put

**[08:30]** part of the process. Um, I wanted to put

**[08:30]** part of the process. Um, I wanted to put this into practice. So, working for us,

**[08:32]** this into practice. So, working for us,

**[08:32]** this into practice. So, working for us, uh, I do a podcast with my buddy uh,

**[08:33]** uh, I do a podcast with my buddy uh,

**[08:34]** uh, I do a podcast with my buddy uh, Vibv, who's the CEO of a company called

**[08:35]** Vibv, who's the CEO of a company called

**[08:35]** Vibv, who's the CEO of a company called Boundary ML. Uh, and I said, "Hey, I'm

**[08:37]** Boundary ML. Uh, and I said, "Hey, I'm

**[08:38]** Boundary ML. Uh, and I said, "Hey, I'm going to try to oneshot a fix to your

**[08:39]** going to try to oneshot a fix to your

**[08:39]** going to try to oneshot a fix to your 300,000line Rust codebase for a

**[08:41]** 300,000line Rust codebase for a

**[08:41]** 300,000line Rust codebase for a programming language."

**[08:43]** programming language."

**[08:43]** programming language." Um, and the whole episode goes in, it's

**[08:45]** Um, and the whole episode goes in, it's

**[08:45]** Um, and the whole episode goes in, it's like an hour and a half. Uh, I'm not

**[08:46]** like an hour and a half. Uh, I'm not

**[08:46]** like an hour and a half. Uh, I'm not going to talk through it right now, but

**[08:47]** going to talk through it right now, but

**[08:47]** going to talk through it right now, but we built a bunch of research and then we

**[08:48]** we built a bunch of research and then we

**[08:48]** we built a bunch of research and then we threw them out because they were bad.

**[08:49]** threw them out because they were bad.

**[08:49]** threw them out because they were bad. And then we made a plan and we made a

**[08:50]** And then we made a plan and we made a

**[08:50]** And then we made a plan and we made a plan without research and with research

**[08:52]** plan without research and with research

**[08:52]** plan without research and with research and compared all the results. It's a fun

**[08:53]** and compared all the results. It's a fun

**[08:53]** and compared all the results. It's a fun time. Uh, by that was Monday night. By

**[08:55]** time. Uh, by that was Monday night. By

**[08:56]** time. Uh, by that was Monday night. By Tuesday morning, we were on the show and

**[08:57]** Tuesday morning, we were on the show and

**[08:57]** Tuesday morning, we were on the show and the CTO had like seen the PR and like


### [09:00 - 10:00]

**[09:00]** the CTO had like seen the PR and like

**[09:00]** the CTO had like seen the PR and like didn't realize I was doing it as a bit

**[09:01]** didn't realize I was doing it as a bit

**[09:01]** didn't realize I was doing it as a bit for a podcast and basically was like,

**[09:03]** for a podcast and basically was like,

**[09:03]** for a podcast and basically was like, "Yeah, this looks good. We'll get in the

**[09:04]** "Yeah, this looks good. We'll get in the

**[09:04]** "Yeah, this looks good. We'll get in the next release." He I think he was a

**[09:06]** next release." He I think he was a

**[09:06]** next release." He I think he was a little confused. Um, here's the the

**[09:08]** little confused. Um, here's the the

**[09:08]** little confused. Um, here's the the plan. But anyways, uh, yeah, confirmed

**[09:11]** plan. But anyways, uh, yeah, confirmed

**[09:11]** plan. But anyways, uh, yeah, confirmed works in brownfield code bases and no

**[09:13]** works in brownfield code bases and no

**[09:14]** works in brownfield code bases and no slop. But I wanted to see if we could

**[09:16]** slop. But I wanted to see if we could

**[09:16]** slop. But I wanted to see if we could solve complex problems. So, Vib was

**[09:18]** solve complex problems. So, Vib was

**[09:18]** solve complex problems. So, Vib was still a little skeptical. I sat down, we

**[09:19]** still a little skeptical. I sat down, we

**[09:20]** still a little skeptical. I sat down, we sat down for like 7 hours on a Saturday

**[09:21]** sat down for like 7 hours on a Saturday

**[09:21]** sat down for like 7 hours on a Saturday and we shipped 35,000 lines of code to

**[09:24]** and we shipped 35,000 lines of code to

**[09:24]** and we shipped 35,000 lines of code to BAML. One of the PRs got merged like a

**[09:26]** BAML. One of the PRs got merged like a

**[09:26]** BAML. One of the PRs got merged like a week later. I will say some of this is

**[09:28]** week later. I will say some of this is

**[09:28]** week later. I will say some of this is codegen. You know, you update your

**[09:29]** codegen. You know, you update your

**[09:29]** codegen. You know, you update your behavior. All the golden files update

**[09:31]** behavior. All the golden files update

**[09:31]** behavior. All the golden files update and stuff, but we shipped a lot of code

**[09:32]** and stuff, but we shipped a lot of code

**[09:32]** and stuff, but we shipped a lot of code that day. Um, he estimates it was about

**[09:34]** that day. Um, he estimates it was about

**[09:34]** that day. Um, he estimates it was about 1 to 2 weeks and 7 hours. And uh, so

**[09:37]** 1 to 2 weeks and 7 hours. And uh, so

**[09:37]** 1 to 2 weeks and 7 hours. And uh, so cool. We can solve complex problems.

**[09:40]** cool. We can solve complex problems.

**[09:40]** cool. We can solve complex problems. There are limits to this. I sat down

**[09:41]** There are limits to this. I sat down

**[09:41]** There are limits to this. I sat down with my buddy Blake. We tried to remove

**[09:43]** with my buddy Blake. We tried to remove

**[09:43]** with my buddy Blake. We tried to remove Hadoop dependencies from Parket Java. If

**[09:46]** Hadoop dependencies from Parket Java. If

**[09:46]** Hadoop dependencies from Parket Java. If you know what Paret Java is, I'm sorry

**[09:49]** you know what Paret Java is, I'm sorry

**[09:49]** you know what Paret Java is, I'm sorry uh for whatever happened to you to get

**[09:51]** uh for whatever happened to you to get

**[09:51]** uh for whatever happened to you to get you to this point in your career. Uh it

**[09:53]** you to this point in your career. Uh it

**[09:53]** you to this point in your career. Uh it did not go well. Uh here's the plans,

**[09:55]** did not go well. Uh here's the plans,

**[09:55]** did not go well. Uh here's the plans, here's the research. Uh at a certain

**[09:57]** here's the research. Uh at a certain

**[09:57]** here's the research. Uh at a certain point, we threw everything out and we

**[09:58]** point, we threw everything out and we

**[09:58]** point, we threw everything out and we actually went back to the whiteboard. We


### [10:00 - 11:00]

**[10:00]** actually went back to the whiteboard. We

**[10:00]** actually went back to the whiteboard. We had to actually once we had learned

**[10:01]** had to actually once we had learned

**[10:01]** had to actually once we had learned where were the where all the foot guns

**[10:03]** where were the where all the foot guns

**[10:03]** where were the where all the foot guns were, we we went back to okay, how is

**[10:05]** were, we we went back to okay, how is

**[10:05]** were, we we went back to okay, how is this actually going to fit together? Um,

**[10:07]** this actually going to fit together? Um,

**[10:07]** this actually going to fit together? Um, and this brings me to a really

**[10:08]** and this brings me to a really

**[10:08]** and this brings me to a really interesting point that Jake's going to

**[10:09]** interesting point that Jake's going to

**[10:09]** interesting point that Jake's going to talk about later. Uh, do not outsource

**[10:11]** talk about later. Uh, do not outsource

**[10:12]** talk about later. Uh, do not outsource the thinking. AI cannot replace

**[10:14]** the thinking. AI cannot replace

**[10:14]** the thinking. AI cannot replace thinking. It can only amplify the

**[10:16]** thinking. It can only amplify the

**[10:16]** thinking. It can only amplify the thinking you have done or the lack of

**[10:17]** thinking you have done or the lack of

**[10:17]** thinking you have done or the lack of thinking you have done. So people ask,

**[10:20]** thinking you have done. So people ask,

**[10:20]** thinking you have done. So people ask, so Dex, this is specri development,

**[10:22]** so Dex, this is specri development,

**[10:22]** so Dex, this is specri development, right? No, specri development is broken.

**[10:28]** right? No, specri development is broken.

**[10:28]** right? No, specri development is broken. Not the idea, but the phrase. Um,

**[10:32]** Not the idea, but the phrase. Um,

**[10:32]** Not the idea, but the phrase. Um, it's not well defined. This is Brietta

**[10:34]** it's not well defined. This is Brietta

**[10:34]** it's not well defined. This is Brietta from Thought Works. Um, and a lot of

**[10:36]** from Thought Works. Um, and a lot of

**[10:36]** from Thought Works. Um, and a lot of people just say spec and they mean a

**[10:37]** people just say spec and they mean a

**[10:37]** people just say spec and they mean a more detailed prompt. Does anyone

**[10:40]** more detailed prompt. Does anyone

**[10:40]** more detailed prompt. Does anyone remember this picture? Does anyone know

**[10:41]** remember this picture? Does anyone know

**[10:41]** remember this picture? Does anyone know what this is from? All right, that's a

**[10:43]** what this is from? All right, that's a

**[10:43]** what this is from? All right, that's a deep cut. Uh, there will never be a year

**[10:45]** deep cut. Uh, there will never be a year

**[10:45]** deep cut. Uh, there will never be a year of agents because of semantic diffusion.

**[10:47]** of agents because of semantic diffusion.

**[10:47]** of agents because of semantic diffusion. Martin Fowler said this in 2006. We come

**[10:49]** Martin Fowler said this in 2006. We come

**[10:49]** Martin Fowler said this in 2006. We come up with a good term with a good

**[10:51]** up with a good term with a good

**[10:51]** up with a good term with a good definition and then everybody gets

**[10:53]** definition and then everybody gets

**[10:53]** definition and then everybody gets excited and everybody starts meaning it

**[10:55]** excited and everybody starts meaning it

**[10:55]** excited and everybody starts meaning it to mean a hundred things to a 100

**[10:56]** to mean a hundred things to a 100

**[10:56]** to mean a hundred things to a 100 different people and it becomes useless.

**[10:59]** different people and it becomes useless.

**[10:59]** different people and it becomes useless. We had an agent is a person, an agent is


### [11:00 - 12:00]

**[11:01]** We had an agent is a person, an agent is

**[11:01]** We had an agent is a person, an agent is a micros service. An agent is a chatbot.

**[11:03]** a micros service. An agent is a chatbot.

**[11:03]** a micros service. An agent is a chatbot. An agent is a workflow. And thank you,

**[11:05]** An agent is a workflow. And thank you,

**[11:05]** An agent is a workflow. And thank you, Simon. We're back to the beginning. An

**[11:07]** Simon. We're back to the beginning. An

**[11:07]** Simon. We're back to the beginning. An agent is just tools in a loop. Um, this

**[11:10]** agent is just tools in a loop. Um, this

**[11:10]** agent is just tools in a loop. Um, this is happening to spec driven dev. I used

**[11:12]** is happening to spec driven dev. I used

**[11:12]** is happening to spec driven dev. I used to have Sean's uh slide in the beginning

**[11:14]** to have Sean's uh slide in the beginning

**[11:14]** to have Sean's uh slide in the beginning of this talk, but it caused a bunch of

**[11:15]** of this talk, but it caused a bunch of

**[11:15]** of this talk, but it caused a bunch of people to focus on the wrong things. His

**[11:17]** people to focus on the wrong things. His

**[11:17]** people to focus on the wrong things. His thing of like, forget the code. It's

**[11:18]** thing of like, forget the code. It's

**[11:18]** thing of like, forget the code. It's like assembly now and you just focus on

**[11:20]** like assembly now and you just focus on

**[11:20]** like assembly now and you just focus on the markdown. Very cool idea, but people

**[11:23]** the markdown. Very cool idea, but people

**[11:23]** the markdown. Very cool idea, but people say Spectrum Dev is writing a better

**[11:24]** say Spectrum Dev is writing a better

**[11:24]** say Spectrum Dev is writing a better prompt, a product requirements document.

**[11:26]** prompt, a product requirements document.

**[11:26]** prompt, a product requirements document. Sometimes it's using like verifiable

**[11:28]** Sometimes it's using like verifiable

**[11:28]** Sometimes it's using like verifiable feedback loops and back pressure. Maybe

**[11:30]** feedback loops and back pressure. Maybe

**[11:30]** feedback loops and back pressure. Maybe it is treating the code like assembly

**[11:32]** it is treating the code like assembly

**[11:32]** it is treating the code like assembly like Sean taught us. Um, but a lot of

**[11:34]** like Sean taught us. Um, but a lot of

**[11:34]** like Sean taught us. Um, but a lot of people is just using a bunch of markdown

**[11:35]** people is just using a bunch of markdown

**[11:35]** people is just using a bunch of markdown files while you're coding. Or my

**[11:37]** files while you're coding. Or my

**[11:37]** files while you're coding. Or my favorite, I just stumbled upon this last

**[11:39]** favorite, I just stumbled upon this last

**[11:39]** favorite, I just stumbled upon this last week. Uh, a spec is documentation for an

**[11:42]** week. Uh, a spec is documentation for an

**[11:42]** week. Uh, a spec is documentation for an open source library. So it's gone. It's

**[11:44]** open source library. So it's gone. It's

**[11:44]** open source library. So it's gone. It's as specri dev is overhyped. It's useless

**[11:47]** as specri dev is overhyped. It's useless

**[11:47]** as specri dev is overhyped. It's useless now. It's semantically diffused.

**[11:50]** now. It's semantically diffused.

**[11:50]** now. It's semantically diffused. Um, so I want to talk about like four

**[11:52]** Um, so I want to talk about like four

**[11:52]** Um, so I want to talk about like four things that actually work today. The

**[11:54]** things that actually work today. The

**[11:54]** things that actually work today. The tactical and practical steps that we

**[11:55]** tactical and practical steps that we

**[11:55]** tactical and practical steps that we found working internally and with a

**[11:57]** found working internally and with a

**[11:57]** found working internally and with a bunch of users. Um, we do the research,

**[11:59]** bunch of users. Um, we do the research,

**[11:59]** bunch of users. Um, we do the research, we figure out how the system works. Um,


### [12:00 - 13:00]

**[12:02]** we figure out how the system works. Um,

**[12:02]** we figure out how the system works. Um, remember Momento? This is the best the

**[12:04]** remember Momento? This is the best the

**[12:04]** remember Momento? This is the best the best movie on context engineering, as

**[12:06]** best movie on context engineering, as

**[12:06]** best movie on context engineering, as Peter says it. Guy wakes up, he has no

**[12:08]** Peter says it. Guy wakes up, he has no

**[12:08]** Peter says it. Guy wakes up, he has no memory. He has to like read his own

**[12:10]** memory. He has to like read his own

**[12:10]** memory. He has to like read his own tattoos to figure out who he is and what

**[12:12]** tattoos to figure out who he is and what

**[12:12]** tattoos to figure out who he is and what he's up to. If you don't onboard your

**[12:14]** he's up to. If you don't onboard your

**[12:14]** he's up to. If you don't onboard your agents, they will make stuff up. And so,

**[12:17]** agents, they will make stuff up. And so,

**[12:17]** agents, they will make stuff up. And so, if this is your team, this is very

**[12:18]** if this is your team, this is very

**[12:18]** if this is your team, this is very simplified for most of you. Most of you

**[12:19]** simplified for most of you. Most of you

**[12:20]** simplified for most of you. Most of you have much bigger orgs than this. But

**[12:21]** have much bigger orgs than this. But

**[12:21]** have much bigger orgs than this. But let's say you want to do some work over

**[12:22]** let's say you want to do some work over

**[12:22]** let's say you want to do some work over here. Um, one thing you could do is you

**[12:25]** here. Um, one thing you could do is you

**[12:25]** here. Um, one thing you could do is you could put onboarding into every repo.

**[12:27]** could put onboarding into every repo.

**[12:27]** could put onboarding into every repo. You put a bunch of context. Here's the

**[12:28]** You put a bunch of context. Here's the

**[12:28]** You put a bunch of context. Here's the repo. Here's how it works. This is a

**[12:30]** repo. Here's how it works. This is a

**[12:30]** repo. Here's how it works. This is a compression of all the context in the

**[12:32]** compression of all the context in the

**[12:32]** compression of all the context in the codebase that the agent can see ahead of

**[12:34]** codebase that the agent can see ahead of

**[12:34]** codebase that the agent can see ahead of time before actually getting to work.

**[12:36]** time before actually getting to work.

**[12:36]** time before actually getting to work. This is challenging because

**[12:38]** This is challenging because

**[12:38]** This is challenging because sometimes it gets too long. As your

**[12:40]** sometimes it gets too long. As your

**[12:40]** sometimes it gets too long. As your codebase gets really big, you either

**[12:41]** codebase gets really big, you either

**[12:41]** codebase gets really big, you either have to make this longer or you have to

**[12:43]** have to make this longer or you have to

**[12:43]** have to make this longer or you have to leave information out. And so as you uh

**[12:47]** leave information out. And so as you uh

**[12:47]** leave information out. And so as you uh are reading through this, you're going

**[12:49]** are reading through this, you're going

**[12:49]** are reading through this, you're going to read the context of this big 5

**[12:50]** to read the context of this big 5

**[12:50]** to read the context of this big 5 million line monor repo and you're going

**[12:52]** million line monor repo and you're going

**[12:52]** million line monor repo and you're going to use all the smart zone just to learn

**[12:54]** to use all the smart zone just to learn

**[12:54]** to use all the smart zone just to learn how it works. And you're not going to be

**[12:55]** how it works. And you're not going to be

**[12:55]** how it works. And you're not going to be able to do any good tool calling in the

**[12:56]** able to do any good tool calling in the

**[12:56]** able to do any good tool calling in the dumb zone. So that's uh you can


### [13:00 - 14:00]

**[13:01]** dumb zone. So that's uh you can

**[13:01]** dumb zone. So that's uh you can you can shard this down the stack. You

**[13:02]** you can shard this down the stack. You

**[13:02]** you can shard this down the stack. You can do they're just talking about

**[13:03]** can do they're just talking about

**[13:03]** can do they're just talking about progressive disclosure. You could split

**[13:04]** progressive disclosure. You could split

**[13:04]** progressive disclosure. You could split this up, right? You could just put a

**[13:06]** this up, right? You could just put a

**[13:06]** this up, right? You could just put a file in the root of every repo and then

**[13:08]** file in the root of every repo and then

**[13:08]** file in the root of every repo and then like at every level you have like

**[13:10]** like at every level you have like

**[13:10]** like at every level you have like additional context based on if you're

**[13:12]** additional context based on if you're

**[13:12]** additional context based on if you're working here, this is what you need to

**[13:14]** working here, this is what you need to

**[13:14]** working here, this is what you need to know. Uh we don't document the files

**[13:16]** know. Uh we don't document the files

**[13:16]** know. Uh we don't document the files themselves cuz they're the source of

**[13:17]** themselves cuz they're the source of

**[13:17]** themselves cuz they're the source of truth. But then as your agent is

**[13:19]** truth. But then as your agent is

**[13:19]** truth. But then as your agent is working, you know, you pull in the root

**[13:20]** working, you know, you pull in the root

**[13:20]** working, you know, you pull in the root context and then you pull in the

**[13:21]** context and then you pull in the

**[13:21]** context and then you pull in the subcontext. We won't talk about any

**[13:22]** subcontext. We won't talk about any

**[13:22]** subcontext. We won't talk about any specific like you could use cloudd for

**[13:24]** specific like you could use cloudd for

**[13:24]** specific like you could use cloudd for this, you can use hooks for this,

**[13:25]** this, you can use hooks for this,

**[13:25]** this, you can use hooks for this, whatever it is. Um, but then you still

**[13:27]** whatever it is. Um, but then you still

**[13:27]** whatever it is. Um, but then you still have plenty of room in the smart zone

**[13:28]** have plenty of room in the smart zone

**[13:28]** have plenty of room in the smart zone because you're only pulling in what you

**[13:29]** because you're only pulling in what you

**[13:29]** because you're only pulling in what you need to know. Um, the problem with this

**[13:32]** need to know. Um, the problem with this

**[13:32]** need to know. Um, the problem with this is that it gets out of date. And so

**[13:34]** is that it gets out of date. And so

**[13:34]** is that it gets out of date. And so every time you ship a new feature, you

**[13:36]** every time you ship a new feature, you

**[13:36]** every time you ship a new feature, you need to kind of like cache and validate

**[13:38]** need to kind of like cache and validate

**[13:38]** need to kind of like cache and validate and rebuild large parts of this internal

**[13:40]** and rebuild large parts of this internal

**[13:40]** and rebuild large parts of this internal documentation. And you could use a lot

**[13:43]** documentation. And you could use a lot

**[13:43]** documentation. And you could use a lot of AI and make it part of your process

**[13:44]** of AI and make it part of your process

**[13:44]** of AI and make it part of your process to update this. Um, but I want to ask a

**[13:47]** to update this. Um, but I want to ask a

**[13:48]** to update this. Um, but I want to ask a question between the actual code, the

**[13:49]** question between the actual code, the

**[13:49]** question between the actual code, the function names, the comments, and the

**[13:50]** function names, the comments, and the

**[13:50]** function names, the comments, and the documentation. Does anyone want to guess

**[13:52]** documentation. Does anyone want to guess

**[13:52]** documentation. Does anyone want to guess what is on the y-axis of this chart?

**[13:57]** what is on the y-axis of this chart?

**[13:57]** what is on the y-axis of this chart? slop

**[13:57]** slop

**[13:57]** slop >> slop. It's actually the amount of lies


### [14:00 - 15:00]

**[14:00]** >> slop. It's actually the amount of lies

**[14:00]** >> slop. It's actually the amount of lies you can find in any one part of your

**[14:02]** you can find in any one part of your

**[14:02]** you can find in any one part of your codebase.

**[14:04]** codebase.

**[14:04]** codebase. Um, so you could make a part of your

**[14:05]** Um, so you could make a part of your

**[14:05]** Um, so you could make a part of your process to update this, but you probably

**[14:07]** process to update this, but you probably

**[14:07]** process to update this, but you probably shouldn't cuz you probably won't. What

**[14:08]** shouldn't cuz you probably won't. What

**[14:08]** shouldn't cuz you probably won't. What we prefer is on demand compressed

**[14:10]** we prefer is on demand compressed

**[14:10]** we prefer is on demand compressed context. So if I'm building a feature

**[14:12]** context. So if I'm building a feature

**[14:12]** context. So if I'm building a feature that relates to SCM providers and Jira

**[14:14]** that relates to SCM providers and Jira

**[14:14]** that relates to SCM providers and Jira and Linear, um, I would just give it a

**[14:16]** and Linear, um, I would just give it a

**[14:16]** and Linear, um, I would just give it a little bit of steering. I would say,

**[14:17]** little bit of steering. I would say,

**[14:17]** little bit of steering. I would say, hey, we're going over in like this like

**[14:19]** hey, we're going over in like this like

**[14:19]** hey, we're going over in like this like part of the codebase over here. Um, and

**[14:22]** part of the codebase over here. Um, and

**[14:22]** part of the codebase over here. Um, and a good research uh prompt or or slash

**[14:24]** a good research uh prompt or or slash

**[14:24]** a good research uh prompt or or slash command might take you or skill even uh

**[14:27]** command might take you or skill even uh

**[14:27]** command might take you or skill even uh launch a bunch of sub aents to take

**[14:29]** launch a bunch of sub aents to take

**[14:29]** launch a bunch of sub aents to take these vertical slices through the

**[14:30]** these vertical slices through the

**[14:30]** these vertical slices through the codebase and then build up a research

**[14:32]** codebase and then build up a research

**[14:32]** codebase and then build up a research document that is just a snapshot of the

**[14:34]** document that is just a snapshot of the

**[14:34]** document that is just a snapshot of the actually true based on the code itself

**[14:37]** actually true based on the code itself

**[14:37]** actually true based on the code itself parts of the codebase that matter. We

**[14:39]** parts of the codebase that matter. We

**[14:39]** parts of the codebase that matter. We are compressing truth. Um, planning is

**[14:42]** are compressing truth. Um, planning is

**[14:42]** are compressing truth. Um, planning is leverage. Planning is about compression

**[14:44]** leverage. Planning is about compression

**[14:44]** leverage. Planning is about compression of intent. Um, and in plan we're going

**[14:46]** of intent. Um, and in plan we're going

**[14:46]** of intent. Um, and in plan we're going to outline the exact steps. We take our

**[14:49]** to outline the exact steps. We take our

**[14:49]** to outline the exact steps. We take our research and our PRD or our bug ticket

**[14:50]** research and our PRD or our bug ticket

**[14:50]** research and our PRD or our bug ticket or our whatever it is and we create a

**[14:52]** or our whatever it is and we create a

**[14:52]** or our whatever it is and we create a plan and we create a plan file. So we're

**[14:54]** plan and we create a plan file. So we're

**[14:54]** plan and we create a plan file. So we're compacting again. And I want to pause to

**[14:56]** compacting again. And I want to pause to

**[14:56]** compacting again. And I want to pause to talk about mental alignment. Um does

**[14:58]** talk about mental alignment. Um does

**[14:58]** talk about mental alignment. Um does anyone know what code review is for?


### [15:00 - 16:00]

**[15:05]** >> Mental alignment. Mental alignment is it

**[15:06]** >> Mental alignment. Mental alignment is it is about finding making sure things are

**[15:07]** is about finding making sure things are

**[15:07]** is about finding making sure things are correct and stuff but the most important

**[15:09]** correct and stuff but the most important

**[15:09]** correct and stuff but the most important thing is how do we keep everybody on the

**[15:10]** thing is how do we keep everybody on the

**[15:10]** thing is how do we keep everybody on the team on the same page about how the

**[15:12]** team on the same page about how the

**[15:12]** team on the same page about how the codebase is changing and why. And I can

**[15:14]** codebase is changing and why. And I can

**[15:14]** codebase is changing and why. And I can read a thousand lines of Golang every

**[15:15]** read a thousand lines of Golang every

**[15:16]** read a thousand lines of Golang every week. Uh sorry I can't read a thousand.

**[15:18]** week. Uh sorry I can't read a thousand.

**[15:18]** week. Uh sorry I can't read a thousand. It's hard. I can do it. I don't want to.

**[15:20]** It's hard. I can do it. I don't want to.

**[15:20]** It's hard. I can do it. I don't want to. Um, and as our team grows, I all the

**[15:22]** Um, and as our team grows, I all the

**[15:22]** Um, and as our team grows, I all the code gets reviewed. We don't not read

**[15:23]** code gets reviewed. We don't not read

**[15:24]** code gets reviewed. We don't not read the code, but I, as you know, a

**[15:25]** the code, but I, as you know, a

**[15:25]** the code, but I, as you know, a technical leader in the in on the team,

**[15:27]** technical leader in the in on the team,

**[15:27]** technical leader in the in on the team, I can read the plans and I can keep up

**[15:29]** I can read the plans and I can keep up

**[15:29]** I can read the plans and I can keep up to date and I can that's enough. I can

**[15:31]** to date and I can that's enough. I can

**[15:31]** to date and I can that's enough. I can catch some problems early and I maintain

**[15:33]** catch some problems early and I maintain

**[15:33]** catch some problems early and I maintain understanding of how the system is

**[15:34]** understanding of how the system is

**[15:34]** understanding of how the system is evolving. Um, Mitchell had this really

**[15:36]** evolving. Um, Mitchell had this really

**[15:36]** evolving. Um, Mitchell had this really good post about how he's been putting

**[15:37]** good post about how he's been putting

**[15:37]** good post about how he's been putting his AMP threads on his pull requests so

**[15:39]** his AMP threads on his pull requests so

**[15:39]** his AMP threads on his pull requests so that you can see not just, hey, here's a

**[15:41]** that you can see not just, hey, here's a

**[15:41]** that you can see not just, hey, here's a wall of green text in GitHub, but here's

**[15:43]** wall of green text in GitHub, but here's

**[15:43]** wall of green text in GitHub, but here's the exact steps, here's the prompts, and

**[15:44]** the exact steps, here's the prompts, and

**[15:44]** the exact steps, here's the prompts, and hey, I ran the build at the end and it

**[15:46]** hey, I ran the build at the end and it

**[15:46]** hey, I ran the build at the end and it passed. This takes the reviewer on a

**[15:48]** passed. This takes the reviewer on a

**[15:48]** passed. This takes the reviewer on a journey in a way that a GitHub PR just

**[15:50]** journey in a way that a GitHub PR just

**[15:50]** journey in a way that a GitHub PR just can't. And as you're shipping more and

**[15:52]** can't. And as you're shipping more and

**[15:52]** can't. And as you're shipping more and more in two to three times as much code,

**[15:54]** more in two to three times as much code,

**[15:54]** more in two to three times as much code, it's really on you to find ways to keep

**[15:57]** it's really on you to find ways to keep

**[15:57]** it's really on you to find ways to keep your team on the same page and show them

**[15:59]** your team on the same page and show them

**[15:59]** your team on the same page and show them here's the steps I did and here's how we


### [16:00 - 17:00]

**[16:00]** here's the steps I did and here's how we

**[16:00]** here's the steps I did and here's how we tested it manually. Um, your goal is

**[16:03]** tested it manually. Um, your goal is

**[16:03]** tested it manually. Um, your goal is leverage. So you want high confidence

**[16:04]** leverage. So you want high confidence

**[16:04]** leverage. So you want high confidence that the model will actually do the

**[16:05]** that the model will actually do the

**[16:05]** that the model will actually do the right thing. I can't read this plan and

**[16:07]** right thing. I can't read this plan and

**[16:07]** right thing. I can't read this plan and know what actually is going to happen

**[16:09]** know what actually is going to happen

**[16:09]** know what actually is going to happen and what code changes are going to

**[16:10]** and what code changes are going to

**[16:10]** and what code changes are going to happen. So we've over time iterated

**[16:12]** happen. So we've over time iterated

**[16:12]** happen. So we've over time iterated towards our plans include actual code

**[16:15]** towards our plans include actual code

**[16:15]** towards our plans include actual code snippets of what's going to change. So

**[16:17]** snippets of what's going to change. So

**[16:17]** snippets of what's going to change. So your goal is leverage. You want

**[16:18]** your goal is leverage. You want

**[16:18]** your goal is leverage. You want compression of intent and you want

**[16:19]** compression of intent and you want

**[16:20]** compression of intent and you want reliable execution. Um and so I don't

**[16:22]** reliable execution. Um and so I don't

**[16:22]** reliable execution. Um and so I don't know I have a physics background. We

**[16:23]** know I have a physics background. We

**[16:23]** know I have a physics background. We like to draw lines through the center of

**[16:25]** like to draw lines through the center of

**[16:26]** like to draw lines through the center of peaks and curves. Uh as your plans get

**[16:28]** peaks and curves. Uh as your plans get

**[16:28]** peaks and curves. Uh as your plans get longer, reliability goes up, readability

**[16:30]** longer, reliability goes up, readability

**[16:30]** longer, reliability goes up, readability goes down. There's a sweet spot for you

**[16:32]** goes down. There's a sweet spot for you

**[16:32]** goes down. There's a sweet spot for you and your team and your codebase. you

**[16:34]** and your team and your codebase. you

**[16:34]** and your team and your codebase. you should try to find it because when we

**[16:35]** should try to find it because when we

**[16:35]** should try to find it because when we review the research and the plans, if

**[16:37]** review the research and the plans, if

**[16:37]** review the research and the plans, if they're good, then we can get mental

**[16:39]** they're good, then we can get mental

**[16:39]** they're good, then we can get mental alignment. Um, don't outsource the

**[16:41]** alignment. Um, don't outsource the

**[16:42]** alignment. Um, don't outsource the thinking. I've said this before, this is

**[16:44]** thinking. I've said this before, this is

**[16:44]** thinking. I've said this before, this is not magic. There is no perfect prompt.

**[16:46]** not magic. There is no perfect prompt.

**[16:46]** not magic. There is no perfect prompt. You still will not work if you do not

**[16:49]** You still will not work if you do not

**[16:49]** You still will not work if you do not read the plan. So, we built our entire

**[16:51]** read the plan. So, we built our entire

**[16:51]** read the plan. So, we built our entire process around you, the builder, are in

**[16:53]** process around you, the builder, are in

**[16:53]** process around you, the builder, are in back and forth with the agent reading

**[16:55]** back and forth with the agent reading

**[16:55]** back and forth with the agent reading the plans as they're created. And then

**[16:57]** the plans as they're created. And then

**[16:57]** the plans as they're created. And then if you need peer review, you can send it

**[16:58]** if you need peer review, you can send it

**[16:58]** if you need peer review, you can send it to someone and say, "Hey, does this plan

**[16:59]** to someone and say, "Hey, does this plan

**[16:59]** to someone and say, "Hey, does this plan look right? Is this the right approach?


### [17:00 - 18:00]

**[17:00]** look right? Is this the right approach?

**[17:00]** look right? Is this the right approach? Is this the right order to look at these

**[17:02]** Is this the right order to look at these

**[17:02]** Is this the right order to look at these things?" Um Jake again wrote a really

**[17:04]** things?" Um Jake again wrote a really

**[17:04]** things?" Um Jake again wrote a really good blog post about like the thing that

**[17:05]** good blog post about like the thing that

**[17:05]** good blog post about like the thing that makes research plan implementing

**[17:06]** makes research plan implementing

**[17:06]** makes research plan implementing valuable is you the human in the loop

**[17:09]** valuable is you the human in the loop

**[17:09]** valuable is you the human in the loop making sure it's correct. So if you take

**[17:12]** making sure it's correct. So if you take

**[17:12]** making sure it's correct. So if you take one thing away from this talk it should

**[17:14]** one thing away from this talk it should

**[17:14]** one thing away from this talk it should be that a bad line of code is a bad line

**[17:16]** be that a bad line of code is a bad line

**[17:16]** be that a bad line of code is a bad line of code and a bad part of a plan is

**[17:20]** of code and a bad part of a plan is

**[17:20]** of code and a bad part of a plan is could be a hundred bad lines of code and

**[17:22]** could be a hundred bad lines of code and

**[17:22]** could be a hundred bad lines of code and a bad line of research like a

**[17:24]** a bad line of research like a

**[17:24]** a bad line of research like a misunderstanding of how the system works

**[17:26]** misunderstanding of how the system works

**[17:26]** misunderstanding of how the system works and where things are your whole thing is

**[17:28]** and where things are your whole thing is

**[17:28]** and where things are your whole thing is going to be hosed. You're going to be

**[17:29]** going to be hosed. You're going to be

**[17:29]** going to be hosed. You're going to be telling sending the model off in the

**[17:30]** telling sending the model off in the

**[17:30]** telling sending the model off in the wrong direction. And so when we're

**[17:32]** wrong direction. And so when we're

**[17:32]** wrong direction. And so when we're working internally and with users, we're

**[17:34]** working internally and with users, we're

**[17:34]** working internally and with users, we're constantly trying to move human effort

**[17:36]** constantly trying to move human effort

**[17:36]** constantly trying to move human effort and focus to the highest leverage parts

**[17:38]** and focus to the highest leverage parts

**[17:38]** and focus to the highest leverage parts of this pipeline. Um, don't outsource

**[17:40]** of this pipeline. Um, don't outsource

**[17:40]** of this pipeline. Um, don't outsource the thinking. Watch out for tools that

**[17:42]** the thinking. Watch out for tools that

**[17:42]** the thinking. Watch out for tools that just spew out a bunch of markdown files

**[17:44]** just spew out a bunch of markdown files

**[17:44]** just spew out a bunch of markdown files just to make you feel good. I'm not

**[17:45]** just to make you feel good. I'm not

**[17:46]** just to make you feel good. I'm not going to name names here. Uh, sometimes

**[17:48]** going to name names here. Uh, sometimes

**[17:48]** going to name names here. Uh, sometimes this is overkill. And the way I like to

**[17:49]** this is overkill. And the way I like to

**[17:49]** this is overkill. And the way I like to think about this is like, yeah, you

**[17:51]** think about this is like, yeah, you

**[17:51]** think about this is like, yeah, you don't always need a full research plan

**[17:53]** don't always need a full research plan

**[17:53]** don't always need a full research plan implement. Sometimes you need more,

**[17:55]** implement. Sometimes you need more,

**[17:55]** implement. Sometimes you need more, sometimes you need less. If you're

**[17:56]** sometimes you need less. If you're

**[17:56]** sometimes you need less. If you're changing the color of a button, just

**[17:57]** changing the color of a button, just

**[17:58]** changing the color of a button, just talk to the agent and tell it what to

**[17:59]** talk to the agent and tell it what to

**[17:59]** talk to the agent and tell it what to do. Um, if you're doing like a simple


### [18:00 - 19:00]

**[18:02]** do. Um, if you're doing like a simple

**[18:02]** do. Um, if you're doing like a simple plan and as a small feature, if you're

**[18:04]** plan and as a small feature, if you're

**[18:04]** plan and as a small feature, if you're doing medium features across multiple

**[18:06]** doing medium features across multiple

**[18:06]** doing medium features across multiple repos, then do one research, then build

**[18:08]** repos, then do one research, then build

**[18:08]** repos, then do one research, then build a plan. Basically, the hardest problem

**[18:10]** a plan. Basically, the hardest problem

**[18:10]** a plan. Basically, the hardest problem you can solve, the ceiling goes up the

**[18:12]** you can solve, the ceiling goes up the

**[18:12]** you can solve, the ceiling goes up the more of this context engineering

**[18:13]** more of this context engineering

**[18:14]** more of this context engineering compaction you're willing to do. Um, and

**[18:16]** compaction you're willing to do. Um, and

**[18:16]** compaction you're willing to do. Um, and so if you're in the top right corner,

**[18:18]** so if you're in the top right corner,

**[18:18]** so if you're in the top right corner, you're probably going to have to do

**[18:19]** you're probably going to have to do

**[18:19]** you're probably going to have to do more. A lot of people ask me, "How do I

**[18:21]** more. A lot of people ask me, "How do I

**[18:21]** more. A lot of people ask me, "How do I know how much context engineering to

**[18:22]** know how much context engineering to

**[18:22]** know how much context engineering to use?" It takes reps. You will get it

**[18:25]** use?" It takes reps. You will get it

**[18:25]** use?" It takes reps. You will get it wrong. You have to get it wrong over and

**[18:26]** wrong. You have to get it wrong over and

**[18:26]** wrong. You have to get it wrong over and over and over again. Sometimes you'll go

**[18:27]** over and over again. Sometimes you'll go

**[18:27]** over and over again. Sometimes you'll go too big. Sometimes you go too small.

**[18:29]** too big. Sometimes you go too small.

**[18:29]** too big. Sometimes you go too small. Pick one tool and get some reps. I

**[18:32]** Pick one tool and get some reps. I

**[18:32]** Pick one tool and get some reps. I recommend against minmaxing across cloud

**[18:34]** recommend against minmaxing across cloud

**[18:34]** recommend against minmaxing across cloud and codeex and all these different

**[18:35]** and codeex and all these different

**[18:35]** and codeex and all these different tools. Um, so I'm not a big acronym guy.

**[18:39]** tools. Um, so I'm not a big acronym guy.

**[18:39]** tools. Um, so I'm not a big acronym guy. Uh, we said specri dev was broken. Uh,

**[18:42]** Uh, we said specri dev was broken. Uh,

**[18:42]** Uh, we said specri dev was broken. Uh, research plan and implement I don't

**[18:43]** research plan and implement I don't

**[18:44]** research plan and implement I don't think will be the steps. The important

**[18:45]** think will be the steps. The important

**[18:45]** think will be the steps. The important part is compaction and context

**[18:46]** part is compaction and context

**[18:46]** part is compaction and context engineering and staying in the smart

**[18:47]** engineering and staying in the smart

**[18:47]** engineering and staying in the smart zone. But people are calling this RPI

**[18:50]** zone. But people are calling this RPI

**[18:50]** zone. But people are calling this RPI and there's nothing I can do about it.

**[18:52]** and there's nothing I can do about it.

**[18:52]** and there's nothing I can do about it. So, uh, just be wary. There is no

**[18:54]** So, uh, just be wary. There is no

**[18:54]** So, uh, just be wary. There is no perfect prompt. There is no silver

**[18:55]** perfect prompt. There is no silver

**[18:55]** perfect prompt. There is no silver bullet. Um, if you really want a hypy

**[18:58]** bullet. Um, if you really want a hypy

**[18:58]** bullet. Um, if you really want a hypy word, you can call this harness harness

**[18:59]** word, you can call this harness harness


### [19:00 - 20:00]

**[19:00]** word, you can call this harness harness engineering, which is part of context

**[19:01]** engineering, which is part of context

**[19:01]** engineering, which is part of context engineering, and it's how you integrate

**[19:02]** engineering, and it's how you integrate

**[19:02]** engineering, and it's how you integrate with the integration points on codeex,

**[19:04]** with the integration points on codeex,

**[19:04]** with the integration points on codeex, claude, cursor, whatever. How you

**[19:05]** claude, cursor, whatever. How you

**[19:06]** claude, cursor, whatever. How you customize your codebase. Um, so what's

**[19:09]** customize your codebase. Um, so what's

**[19:09]** customize your codebase. Um, so what's next? I think the coding agent stuff is

**[19:12]** next? I think the coding agent stuff is

**[19:12]** next? I think the coding agent stuff is actually going to be commoditized.

**[19:13]** actually going to be commoditized.

**[19:13]** actually going to be commoditized. People are going to learn how to do this

**[19:14]** People are going to learn how to do this

**[19:14]** People are going to learn how to do this and get better at it. And the hard part

**[19:16]** and get better at it. And the hard part

**[19:16]** and get better at it. And the hard part is going to be how do you adapt your

**[19:17]** is going to be how do you adapt your

**[19:17]** is going to be how do you adapt your team and your workflow and the SDLC to

**[19:20]** team and your workflow and the SDLC to

**[19:20]** team and your workflow and the SDLC to work in a world where 99% of your code

**[19:22]** work in a world where 99% of your code

**[19:22]** work in a world where 99% of your code is shipped by AI. Uh, and if you can't

**[19:25]** is shipped by AI. Uh, and if you can't

**[19:25]** is shipped by AI. Uh, and if you can't figure this out, you're hosed because

**[19:26]** figure this out, you're hosed because

**[19:26]** figure this out, you're hosed because there's kind of a rift growing where

**[19:28]** there's kind of a rift growing where

**[19:28]** there's kind of a rift growing where like staff engineers don't adopt AI

**[19:29]** like staff engineers don't adopt AI

**[19:29]** like staff engineers don't adopt AI because it doesn't make them that much

**[19:30]** because it doesn't make them that much

**[19:30]** because it doesn't make them that much faster. And then junior mid-levels

**[19:32]** faster. And then junior mid-levels

**[19:32]** faster. And then junior mid-levels engineers use a lot because it fills in

**[19:34]** engineers use a lot because it fills in

**[19:34]** engineers use a lot because it fills in skill gaps and then it also produces

**[19:36]** skill gaps and then it also produces

**[19:36]** skill gaps and then it also produces some slop. And then the senior engineers

**[19:37]** some slop. And then the senior engineers

**[19:37]** some slop. And then the senior engineers hate it more and more every week because

**[19:39]** hate it more and more every week because

**[19:39]** hate it more and more every week because they're cleaning up slop that was

**[19:40]** they're cleaning up slop that was

**[19:40]** they're cleaning up slop that was shipped by cursor the week before. Uh,

**[19:43]** shipped by cursor the week before. Uh,

**[19:43]** shipped by cursor the week before. Uh, this is not AI's fault. This is not the

**[19:44]** this is not AI's fault. This is not the

**[19:44]** this is not AI's fault. This is not the mid-level engineers fault. Like if

**[19:46]** mid-level engineers fault. Like if

**[19:46]** mid-level engineers fault. Like if cultural change is really hard and it

**[19:48]** cultural change is really hard and it

**[19:48]** cultural change is really hard and it needs to come from the top if it's going

**[19:49]** needs to come from the top if it's going

**[19:49]** needs to come from the top if it's going to work. So if you're a technical leader

**[19:51]** to work. So if you're a technical leader

**[19:51]** to work. So if you're a technical leader at your company, pick one tool and get

**[19:53]** at your company, pick one tool and get

**[19:53]** at your company, pick one tool and get some reps. If you want to help, we are

**[19:56]** some reps. If you want to help, we are

**[19:56]** some reps. If you want to help, we are hiring. We're building an Aentic IDE to

**[19:58]** hiring. We're building an Aentic IDE to

**[19:58]** hiring. We're building an Aentic IDE to help teams of all sizes speedrun the


### [20:00 - 21:00]

**[20:00]** help teams of all sizes speedrun the

**[20:00]** help teams of all sizes speedrun the journey to 99% AI generated code. Uh if

**[20:04]** journey to 99% AI generated code. Uh if

**[20:04]** journey to 99% AI generated code. Uh if we'd love to we'd love to talk if you

**[20:05]** we'd love to we'd love to talk if you

**[20:05]** we'd love to we'd love to talk if you want to work with us. Uh go go hit our

**[20:07]** want to work with us. Uh go go hit our

**[20:07]** want to work with us. Uh go go hit our website, send us an email, come find me

**[20:08]** website, send us an email, come find me

**[20:08]** website, send us an email, come find me in the hallway. Uh thank you all so much

**[20:10]** in the hallway. Uh thank you all so much

**[20:10]** in the hallway. Uh thank you all so much for your energy.

**[20:16]** [music]

**[20:16]** [music] Heat.


