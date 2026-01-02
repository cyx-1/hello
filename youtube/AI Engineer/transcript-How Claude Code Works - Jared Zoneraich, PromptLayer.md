# How Claude Code Works - Jared Zoneraich, PromptLayer

**Video URL:** https://www.youtube.com/watch?v=RFKCzGlAU6Q

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** So, welcome to the last workshop. Um,

**[00:23]** So, welcome to the last workshop. Um, you made it. Congrats. Y

**[00:30]** out of like 800 uh people, you're you're

**[00:30]** out of like 800 uh people, you're you're the last standing uh sort of very very

**[00:32]** the last standing uh sort of very very

**[00:32]** the last standing uh sort of very very dedicated engineers. Uh yeah, so this

**[00:35]** dedicated engineers. Uh yeah, so this

**[00:35]** dedicated engineers. Uh yeah, so this one's a weird one. I got in trouble with

**[00:37]** one's a weird one. I got in trouble with

**[00:37]** one's a weird one. I got in trouble with entropic on this one. Uh obviously

**[00:39]** entropic on this one. Uh obviously

**[00:39]** entropic on this one. Uh obviously because of the title. I actually also

**[00:41]** because of the title. I actually also

**[00:41]** because of the title. I actually also gave him the title and I was like, do

**[00:42]** gave him the title and I was like, do

**[00:42]** gave him the title and I was like, do you want to change it? He was like, no,

**[00:44]** you want to change it? He was like, no,

**[00:44]** you want to change it? He was like, no, I just roll with it. It's kind of funny.

**[00:46]** I just roll with it. It's kind of funny.

**[00:46]** I just roll with it. It's kind of funny. Uh uh so so yeah, this is not officially

**[00:48]** Uh uh so so yeah, this is not officially

**[00:48]** Uh uh so so yeah, this is not officially endorsed by Copic, but we're hackers,

**[00:52]** endorsed by Copic, but we're hackers,

**[00:52]** endorsed by Copic, but we're hackers, right? And Jared is like super

**[00:54]** right? And Jared is like super

**[00:54]** right? And Jared is like super dedicated. He's um and the other thing I

**[00:57]** dedicated. He's um and the other thing I

**[00:57]** dedicated. He's um and the other thing I also like really enjoy is featuring like

**[00:59]** also like really enjoy is featuring like

**[00:59]** also like really enjoy is featuring like notable New York AI people, right? Like


### [01:00 - 02:00]

**[01:02]** notable New York AI people, right? Like

**[01:02]** notable New York AI people, right? Like so don't take this as like one is the

**[01:04]** so don't take this as like one is the

**[01:04]** so don't take this as like one is the only thing that Jared does. He has a

**[01:06]** only thing that Jared does. He has a

**[01:06]** only thing that Jared does. He has a whole startup that you should definitely

**[01:07]** whole startup that you should definitely

**[01:07]** whole startup that you should definitely ask him about. Um but like you know I'm

**[01:09]** ask him about. Um but like you know I'm

**[01:09]** ask him about. Um but like you know I'm just really excited to feature more

**[01:11]** just really excited to feature more

**[01:11]** just really excited to feature more content for local people. So yeah,

**[01:14]** content for local people. So yeah,

**[01:14]** content for local people. So yeah, Jared, take it away.

**[01:15]** Jared, take it away.

**[01:15]** Jared, take it away. >> Thank you very much. Thank you very

**[01:17]** >> Thank you very much. Thank you very

**[01:17]** >> Thank you very much. Thank you very much. And what an amazing conference.

**[01:19]** much. And what an amazing conference.

**[01:19]** much. And what an amazing conference. very sad we're ending it, but hopefully

**[01:21]** very sad we're ending it, but hopefully

**[01:21]** very sad we're ending it, but hopefully it'll be a good ending here. Um, and

**[01:24]** it'll be a good ending here. Um, and

**[01:24]** it'll be a good ending here. Um, and yeah, uh, my name is Jared. Uh, this

**[01:27]** yeah, uh, my name is Jared. Uh, this

**[01:27]** yeah, uh, my name is Jared. Uh, this will be a talk on how Claude Code works.

**[01:30]** will be a talk on how Claude Code works.

**[01:30]** will be a talk on how Claude Code works. Again, not affiliated with Anthropic.

**[01:32]** Again, not affiliated with Anthropic.

**[01:32]** Again, not affiliated with Anthropic. Uh, they don't pay me. I would take

**[01:35]** Uh, they don't pay me. I would take

**[01:35]** Uh, they don't pay me. I would take money, but they don't. Um, but we're

**[01:37]** money, but they don't. Um, but we're

**[01:37]** money, but they don't. Um, but we're going to talk about a few other coding

**[01:39]** going to talk about a few other coding

**[01:39]** going to talk about a few other coding agents as well. And kind of the highle

**[01:42]** agents as well. And kind of the highle

**[01:42]** agents as well. And kind of the highle goal that I'll go into is me personally,

**[01:45]** goal that I'll go into is me personally,

**[01:45]** goal that I'll go into is me personally, I I'm a big user of all the coding

**[01:47]** I I'm a big user of all the coding

**[01:47]** I I'm a big user of all the coding agents, as is everyone here. and they

**[01:50]** agents, as is everyone here. and they

**[01:50]** agents, as is everyone here. and they kind of exploded recently and as a

**[01:53]** kind of exploded recently and as a

**[01:53]** kind of exploded recently and as a developer I was curious what changed

**[01:55]** developer I was curious what changed

**[01:55]** developer I was curious what changed what made it finally what made coding

**[01:58]** what made it finally what made coding

**[01:58]** what made it finally what made coding agents finally be good. So let's get


### [02:00 - 03:00]

**[02:01]** agents finally be good. So let's get

**[02:01]** agents finally be good. So let's get started. I'll start about me. I'm Jared.

**[02:03]** started. I'll start about me. I'm Jared.

**[02:03]** started. I'll start about me. I'm Jared. You can find me I'm Jared Z on X on

**[02:06]** You can find me I'm Jared Z on X on

**[02:06]** You can find me I'm Jared Z on X on Twitter whatever. Um I'm building the

**[02:08]** Twitter whatever. Um I'm building the

**[02:08]** Twitter whatever. Um I'm building the workbench for AI engineering. So uh my

**[02:12]** workbench for AI engineering. So uh my

**[02:12]** workbench for AI engineering. So uh my company is called Prompt Layer. We're

**[02:13]** company is called Prompt Layer. We're

**[02:13]** company is called Prompt Layer. We're based in New York. You can kind of see

**[02:15]** based in New York. You can kind of see

**[02:15]** based in New York. You can kind of see our office here. It's like a little

**[02:17]** our office here. It's like a little

**[02:17]** our office here. It's like a little building. So it's blocked by a few of

**[02:18]** building. So it's blocked by a few of

**[02:18]** building. So it's blocked by a few of the other buildings. So we're we're a

**[02:20]** the other buildings. So we're we're a

**[02:20]** the other buildings. So we're we're a small team. We launched the product 3

**[02:21]** small team. We launched the product 3

**[02:22]** small team. We launched the product 3 years ago. So uh long for AI but small

**[02:24]** years ago. So uh long for AI but small

**[02:24]** years ago. So uh long for AI but small for everything else. And uh yeah, what

**[02:27]** for everything else. And uh yeah, what

**[02:27]** for everything else. And uh yeah, what kind of our core thesis is that we

**[02:30]** kind of our core thesis is that we

**[02:30]** kind of our core thesis is that we believe in rigorous prompt engineering,

**[02:32]** believe in rigorous prompt engineering,

**[02:32]** believe in rigorous prompt engineering, rigorous agent developing development

**[02:35]** rigorous agent developing development

**[02:35]** rigorous agent developing development and we believe that the product team

**[02:37]** and we believe that the product team

**[02:37]** and we believe that the product team should be involved, the engineering team

**[02:39]** should be involved, the engineering team

**[02:39]** should be involved, the engineering team should be involved. We believe if you're

**[02:40]** should be involved. We believe if you're

**[02:40]** should be involved. We believe if you're building AI lawyers, you should have

**[02:42]** building AI lawyers, you should have

**[02:42]** building AI lawyers, you should have lawyers involved as well as engineers.

**[02:44]** lawyers involved as well as engineers.

**[02:44]** lawyers involved as well as engineers. Um so that's kind of what we do. uh

**[02:46]** Um so that's kind of what we do. uh

**[02:46]** Um so that's kind of what we do. uh processing millions of LM requests a

**[02:48]** processing millions of LM requests a

**[02:48]** processing millions of LM requests a day. And a lot of the insights in this

**[02:49]** day. And a lot of the insights in this

**[02:49]** day. And a lot of the insights in this talk come from just conversations we

**[02:52]** talk come from just conversations we

**[02:52]** talk come from just conversations we have with our customers on how to build

**[02:55]** have with our customers on how to build

**[02:55]** have with our customers on how to build coding agents and stuff like that. And

**[02:57]** coding agents and stuff like that. And

**[02:57]** coding agents and stuff like that. And also feel free throughout the talk we

**[02:59]** also feel free throughout the talk we

**[02:59]** also feel free throughout the talk we can make this casual. So if there's


### [03:00 - 04:00]

**[03:00]** can make this casual. So if there's

**[03:00]** can make this casual. So if there's anything I say if you have a question

**[03:02]** anything I say if you have a question

**[03:02]** anything I say if you have a question feel free to just throw it in. Uh and I

**[03:05]** feel free to just throw it in. Uh and I

**[03:05]** feel free to just throw it in. Uh and I spend a lot of my time kind of dog

**[03:06]** spend a lot of my time kind of dog

**[03:06]** spend a lot of my time kind of dog fooding the product. It's kind of weird

**[03:08]** fooding the product. It's kind of weird

**[03:08]** fooding the product. It's kind of weird the job of of a founder these days

**[03:10]** the job of of a founder these days

**[03:10]** the job of of a founder these days because it's half like kicking off

**[03:12]** because it's half like kicking off

**[03:12]** because it's half like kicking off agents and then half just using my own

**[03:14]** agents and then half just using my own

**[03:14]** agents and then half just using my own product to build agents and feels weird

**[03:16]** product to build agents and feels weird

**[03:16]** product to build agents and feels weird but it's kind of fun. And uh yeah, the

**[03:19]** but it's kind of fun. And uh yeah, the

**[03:19]** but it's kind of fun. And uh yeah, the last thing I'll add here is I'm a big

**[03:21]** last thing I'll add here is I'm a big

**[03:21]** last thing I'll add here is I'm a big enthusiast. We literally rebuilt our

**[03:24]** enthusiast. We literally rebuilt our

**[03:24]** enthusiast. We literally rebuilt our engineering org around cloud code. I

**[03:26]** engineering org around cloud code. I

**[03:26]** engineering org around cloud code. I think the hard part about building a

**[03:28]** think the hard part about building a

**[03:28]** think the hard part about building a platform is that you have to deal with

**[03:30]** platform is that you have to deal with

**[03:30]** platform is that you have to deal with all these edge cases and oh uh we're

**[03:33]** all these edge cases and oh uh we're

**[03:33]** all these edge cases and oh uh we're uploading data sets here it doesn't work

**[03:35]** uploading data sets here it doesn't work

**[03:35]** uploading data sets here it doesn't work and you could die a death by a thousand

**[03:38]** and you could die a death by a thousand

**[03:38]** and you could die a death by a thousand cuts. So we made a rule for our

**[03:39]** cuts. So we made a rule for our

**[03:39]** cuts. So we made a rule for our engineering organization if you

**[03:42]** engineering organization if you

**[03:42]** engineering organization if you can complete something in less than an

**[03:44]** can complete something in less than an

**[03:44]** can complete something in less than an hour using cloud code. Just do it. Don't

**[03:47]** hour using cloud code. Just do it. Don't

**[03:47]** hour using cloud code. Just do it. Don't prioritize it. And we're a small team on

**[03:49]** prioritize it. And we're a small team on

**[03:49]** prioritize it. And we're a small team on purpose but uh it's helped us a lot and

**[03:52]** purpose but uh it's helped us a lot and

**[03:52]** purpose but uh it's helped us a lot and I think it's really taken us to the next

**[03:53]** I think it's really taken us to the next

**[03:53]** I think it's really taken us to the next level. So I'm a big fan and let's dive

**[03:56]** level. So I'm a big fan and let's dive

**[03:56]** level. So I'm a big fan and let's dive into how these things work. So this is

**[03:58]** into how these things work. So this is

**[03:58]** into how these things work. So this is what as I was saying the goal of this

**[03:59]** what as I was saying the goal of this

**[03:59]** what as I was saying the goal of this talk. First, why have these things


### [04:00 - 05:00]

**[04:02]** talk. First, why have these things

**[04:02]** talk. First, why have these things exploded? What is the

**[04:05]** exploded? What is the

**[04:05]** exploded? What is the what was the innovation? What was the

**[04:07]** what was the innovation? What was the

**[04:07]** what was the innovation? What was the invention that made coding agents

**[04:08]** invention that made coding agents

**[04:08]** invention that made coding agents finally work? If you've been around this

**[04:11]** finally work? If you've been around this

**[04:11]** finally work? If you've been around this field for a little bit, you know that uh

**[04:13]** field for a little bit, you know that uh

**[04:14]** field for a little bit, you know that uh a lot of these autonomous coding agents

**[04:16]** a lot of these autonomous coding agents

**[04:16]** a lot of these autonomous coding agents sucked at the beginning and we all tried

**[04:18]** sucked at the beginning and we all tried

**[04:18]** sucked at the beginning and we all tried to use them. Uh but it's it's night and

**[04:21]** to use them. Uh but it's it's night and

**[04:21]** to use them. Uh but it's it's night and day. uh we'll dive into the internals

**[04:24]** day. uh we'll dive into the internals

**[04:24]** day. uh we'll dive into the internals and and lastly we like everything in

**[04:27]** and and lastly we like everything in

**[04:27]** and and lastly we like everything in this talk is oriented around how do you

**[04:29]** this talk is oriented around how do you

**[04:29]** this talk is oriented around how do you build your own agents and how do you use

**[04:31]** build your own agents and how do you use

**[04:31]** build your own agents and how do you use this to do AI engineering for yourself.

**[04:36]** this to do AI engineering for yourself.

**[04:36]** this to do AI engineering for yourself. So let's just go uh talk about history

**[04:38]** So let's just go uh talk about history

**[04:38]** So let's just go uh talk about history for a second here. How did we get here?

**[04:41]** for a second here. How did we get here?

**[04:41]** for a second here. How did we get here? uh everybody knows started with uh

**[04:44]** uh everybody knows started with uh

**[04:44]** uh everybody knows started with uh remember the workflow of you just copy

**[04:47]** remember the workflow of you just copy

**[04:47]** remember the workflow of you just copy and paste your code back from chat GPT

**[04:49]** and paste your code back from chat GPT

**[04:49]** and paste your code back from chat GPT back and forth and that was great and

**[04:50]** back and forth and that was great and

**[04:50]** back and forth and that was great and that was kind of revolutionary when it

**[04:52]** that was kind of revolutionary when it

**[04:52]** that was kind of revolutionary when it happened. Uh, step two, when cursor came

**[04:55]** happened. Uh, step two, when cursor came

**[04:55]** happened. Uh, step two, when cursor came out, if we all remember, it was not not

**[04:59]** out, if we all remember, it was not not

**[04:59]** out, if we all remember, it was not not great software at the beginning. It was


### [05:00 - 06:00]

**[05:01]** great software at the beginning. It was

**[05:01]** great software at the beginning. It was just the VS Code fork with the command K

**[05:04]** just the VS Code fork with the command K

**[05:04]** just the VS Code fork with the command K and we all loved it. But, uh, now now

**[05:08]** and we all loved it. But, uh, now now

**[05:08]** and we all loved it. But, uh, now now we're not going to be doing command K

**[05:09]** we're not going to be doing command K

**[05:09]** we're not going to be doing command K anymore. Then we got the cursor

**[05:11]** anymore. Then we got the cursor

**[05:11]** anymore. Then we got the cursor assistant. So, that little agent back

**[05:13]** assistant. So, that little agent back

**[05:13]** assistant. So, that little agent back and forth and then cloud code. And

**[05:15]** and forth and then cloud code. And

**[05:15]** and forth and then cloud code. And honestly, in the last few days since I

**[05:17]** honestly, in the last few days since I

**[05:17]** honestly, in the last few days since I made this slide, maybe there's a new

**[05:19]** made this slide, maybe there's a new

**[05:19]** made this slide, maybe there's a new version we could talk about here. And uh

**[05:21]** version we could talk about here. And uh

**[05:21]** version we could talk about here. And uh at the end I'll talk about like kind of

**[05:22]** at the end I'll talk about like kind of

**[05:22]** at the end I'll talk about like kind of what's next. But this is how we got

**[05:24]** what's next. But this is how we got

**[05:24]** what's next. But this is how we got here. And this is really I think the

**[05:26]** here. And this is really I think the

**[05:26]** here. And this is really I think the cloud code is kind of this headless uh

**[05:29]** cloud code is kind of this headless uh

**[05:29]** cloud code is kind of this headless uh not even this this new workflow of not

**[05:32]** not even this this new workflow of not

**[05:32]** not even this this new workflow of not even touching code. And it it has to be

**[05:35]** even touching code. And it it has to be

**[05:35]** even touching code. And it it has to be really good. So why is it so good? What

**[05:38]** really good. So why is it so good? What

**[05:38]** really good. So why is it so good? What what was uh what was the big

**[05:40]** what was uh what was the big

**[05:40]** what was uh what was the big breakthrough here? Let's try to figure

**[05:41]** breakthrough here? Let's try to figure

**[05:41]** breakthrough here? Let's try to figure that out. And again throw this in one

**[05:44]** that out. And again throw this in one

**[05:44]** that out. And again throw this in one more time. These are all my opinions uh

**[05:46]** more time. These are all my opinions uh

**[05:46]** more time. These are all my opinions uh and what I think is the breakthrough.

**[05:47]** and what I think is the breakthrough.

**[05:47]** and what I think is the breakthrough. Maybe there's other things but simple

**[05:50]** Maybe there's other things but simple

**[05:50]** Maybe there's other things but simple architecture. I think a lot of things

**[05:52]** architecture. I think a lot of things

**[05:52]** architecture. I think a lot of things were simplified with how the agent was

**[05:54]** were simplified with how the agent was

**[05:54]** were simplified with how the agent was designed and then better models, better

**[05:57]** designed and then better models, better

**[05:57]** designed and then better models, better models and better models. Uh I think the


### [06:00 - 07:00]

**[06:01]** models and better models. Uh I think the

**[06:01]** models and better models. Uh I think the a lot of the breakthrough is kind of

**[06:03]** a lot of the breakthrough is kind of

**[06:03]** a lot of the breakthrough is kind of boring in that it's just anthropic

**[06:06]** boring in that it's just anthropic

**[06:06]** boring in that it's just anthropic releasing a better model that works

**[06:07]** releasing a better model that works

**[06:07]** releasing a better model that works better for these type of tooling calls

**[06:09]** better for these type of tooling calls

**[06:09]** better for these type of tooling calls and these type of things. But the simple

**[06:11]** and these type of things. But the simple

**[06:12]** and these type of things. But the simple architecture relates to that. So we can

**[06:14]** architecture relates to that. So we can

**[06:14]** architecture relates to that. So we can dive into that. the architecture and and

**[06:18]** dive into that. the architecture and and

**[06:18]** dive into that. the architecture and and this is our little you'll see uh prompt

**[06:20]** this is our little you'll see uh prompt

**[06:20]** this is our little you'll see uh prompt wrangler is our little mascot for our

**[06:22]** wrangler is our little mascot for our

**[06:22]** wrangler is our little mascot for our company. So we made a lot of graphics

**[06:23]** company. So we made a lot of graphics

**[06:24]** company. So we made a lot of graphics for these slides but uh

**[06:26]** for these slides but uh

**[06:26]** for these slides but uh basically give it tools and then get out

**[06:28]** basically give it tools and then get out

**[06:28]** basically give it tools and then get out of the way is what a oneliner of the

**[06:32]** of the way is what a oneliner of the

**[06:32]** of the way is what a oneliner of the architecture is today. I think if you've

**[06:35]** architecture is today. I think if you've

**[06:35]** architecture is today. I think if you've been building on top of LMS for a little

**[06:38]** been building on top of LMS for a little

**[06:38]** been building on top of LMS for a little bit this has not always been true.

**[06:39]** bit this has not always been true.

**[06:39]** bit this has not always been true. Obviously tool calls haven't always

**[06:41]** Obviously tool calls haven't always

**[06:41]** Obviously tool calls haven't always existed and tool calls is kind of this

**[06:43]** existed and tool calls is kind of this

**[06:43]** existed and tool calls is kind of this new abstraction for JSON formatting and

**[06:46]** new abstraction for JSON formatting and

**[06:46]** new abstraction for JSON formatting and if you remember the GitHub libraries

**[06:48]** if you remember the GitHub libraries

**[06:48]** if you remember the GitHub libraries like JSON former and stuff like that in

**[06:50]** like JSON former and stuff like that in

**[06:50]** like JSON former and stuff like that in the olden days but give it tools get out

**[06:53]** the olden days but give it tools get out

**[06:53]** the olden days but give it tools get out of the way. Uh the models are built for

**[06:56]** of the way. Uh the models are built for

**[06:56]** of the way. Uh the models are built for these things and being trained to get

**[06:58]** these things and being trained to get

**[06:58]** these things and being trained to get better at tool calling and better at


### [07:00 - 08:00]

**[07:00]** better at tool calling and better at

**[07:00]** better at tool calling and better at this. So the more you want to

**[07:02]** this. So the more you want to

**[07:02]** this. So the more you want to overoptimize and every engineer uh

**[07:04]** overoptimize and every engineer uh

**[07:04]** overoptimize and every engineer uh including my especially myself loves to

**[07:06]** including my especially myself loves to

**[07:06]** including my especially myself loves to overoptimize and when you first have an

**[07:08]** overoptimize and when you first have an

**[07:08]** overoptimize and when you first have an idea of how to build the agent you're

**[07:09]** idea of how to build the agent you're

**[07:10]** idea of how to build the agent you're going to sit down and say oh and then

**[07:12]** going to sit down and say oh and then

**[07:12]** going to sit down and say oh and then I'm going to prevent this hallucination

**[07:13]** I'm going to prevent this hallucination

**[07:13]** I'm going to prevent this hallucination by doing this prompt and then this

**[07:15]** by doing this prompt and then this

**[07:15]** by doing this prompt and then this prompt and then this prompt don't do

**[07:17]** prompt and then this prompt don't do

**[07:17]** prompt and then this prompt don't do that just a simple loop and get out of

**[07:21]** that just a simple loop and get out of

**[07:21]** that just a simple loop and get out of the way and just delete scaffolding and

**[07:25]** the way and just delete scaffolding and

**[07:25]** the way and just delete scaffolding and less less scaffolding more model is kind

**[07:27]** less less scaffolding more model is kind

**[07:27]** less less scaffolding more model is kind of the tagline here and you know This is

**[07:30]** of the tagline here and you know This is

**[07:30]** of the tagline here and you know This is uh the leaderboard from this week.

**[07:34]** uh the leaderboard from this week.

**[07:34]** uh the leaderboard from this week. Obviously, these models are getting

**[07:35]** Obviously, these models are getting

**[07:36]** Obviously, these models are getting better and better. Uh we could have a

**[07:38]** better and better. Uh we could have a

**[07:38]** better and better. Uh we could have a whole conversation and I'm sure there's

**[07:39]** whole conversation and I'm sure there's

**[07:39]** whole conversation and I'm sure there's been many conversations about is it

**[07:41]** been many conversations about is it

**[07:41]** been many conversations about is it slowing down? Is it plateauing? It

**[07:43]** slowing down? Is it plateauing? It

**[07:43]** slowing down? Is it plateauing? It doesn't really matter for this talk. We

**[07:46]** doesn't really matter for this talk. We

**[07:46]** doesn't really matter for this talk. We know it's getting better and they're

**[07:48]** know it's getting better and they're

**[07:48]** know it's getting better and they're getting better at tool calling and

**[07:49]** getting better at tool calling and

**[07:49]** getting better at tool calling and they're getting better optimized for

**[07:51]** they're getting better optimized for

**[07:51]** they're getting better optimized for running autonomously. And don't this is

**[07:55]** running autonomously. And don't this is

**[07:55]** running autonomously. And don't this is I I think Anthropic calls this like the

**[07:56]** I I think Anthropic calls this like the

**[07:56]** I I think Anthropic calls this like the AGI pill to way to think about it is

**[07:59]** AGI pill to way to think about it is

**[07:59]** AGI pill to way to think about it is don't try to overengineer around model


### [08:00 - 09:00]

**[08:01]** don't try to overengineer around model

**[08:01]** don't try to overengineer around model flaws today because a lot of the things

**[08:04]** flaws today because a lot of the things

**[08:04]** flaws today because a lot of the things will just get better and you'll be

**[08:07]** will just get better and you'll be

**[08:07]** will just get better and you'll be wasting your time. So here's the

**[08:10]** wasting your time. So here's the

**[08:10]** wasting your time. So here's the philosophy, the way I see it of cloud

**[08:12]** philosophy, the way I see it of cloud

**[08:12]** philosophy, the way I see it of cloud code,

**[08:14]** code,

**[08:14]** code, ignoring embeddings, ignoring

**[08:16]** ignoring embeddings, ignoring

**[08:16]** ignoring embeddings, ignoring classifiers, ignoring par matching. The

**[08:19]** classifiers, ignoring par matching. The

**[08:19]** classifiers, ignoring par matching. The we had this whole rag thing actually

**[08:21]** we had this whole rag thing actually

**[08:21]** we had this whole rag thing actually cursors bring back a little bit of rag

**[08:23]** cursors bring back a little bit of rag

**[08:23]** cursors bring back a little bit of rag and how they're doing it and they're

**[08:24]** and how they're doing it and they're

**[08:24]** and how they're doing it and they're mixing and matching. But I think the

**[08:25]** mixing and matching. But I think the

**[08:25]** mixing and matching. But I think the genius with cloud code is that they they

**[08:28]** genius with cloud code is that they they

**[08:28]** genius with cloud code is that they they scratched all this and they said we

**[08:29]** scratched all this and they said we

**[08:29]** scratched all this and they said we don't need all these fancy uh paradigms

**[08:33]** don't need all these fancy uh paradigms

**[08:33]** don't need all these fancy uh paradigms to get around how the model's bad. let's

**[08:36]** to get around how the model's bad. let's

**[08:36]** to get around how the model's bad. let's just make a better model and then let it

**[08:38]** just make a better model and then let it

**[08:38]** just make a better model and then let it let it cook and uh just leaning uh on

**[08:43]** let it cook and uh just leaning uh on

**[08:43]** let it cook and uh just leaning uh on these tool calls and

**[08:46]** these tool calls and

**[08:46]** these tool calls and simplifying the tool calls which is a

**[08:48]** simplifying the tool calls which is a

**[08:48]** simplifying the tool calls which is a very important part part instead of

**[08:49]** very important part part instead of

**[08:49]** very important part part instead of having a workflow where the master

**[08:53]** having a workflow where the master

**[08:53]** having a workflow where the master prompt can break into three different

**[08:55]** prompt can break into three different

**[08:55]** prompt can break into three different branches and then go into four different

**[08:56]** branches and then go into four different

**[08:56]** branches and then go into four different branches there there's really just a few


### [09:00 - 10:00]

**[09:00]** branches there there's really just a few

**[09:00]** branches there there's really just a few simple tool calls uh including GP

**[09:03]** simple tool calls uh including GP

**[09:03]** simple tool calls uh including GP instead of rag and uh yeah and that's

**[09:07]** instead of rag and uh yeah and that's

**[09:07]** instead of rag and uh yeah and that's kind of what it's trained on. So uh

**[09:09]** kind of what it's trained on. So uh

**[09:09]** kind of what it's trained on. So uh these are very optimized tool calling

**[09:11]** these are very optimized tool calling

**[09:11]** these are very optimized tool calling models.

**[09:13]** models.

**[09:13]** models. So this is uh the zen of Python if if

**[09:17]** So this is uh the zen of Python if if

**[09:17]** So this is uh the zen of Python if if you guys are familiar if you do import

**[09:18]** you guys are familiar if you do import

**[09:18]** you guys are familiar if you do import this in Python. This is I love this

**[09:20]** this in Python. This is I love this

**[09:20]** this in Python. This is I love this philosophy when it comes to building

**[09:22]** philosophy when it comes to building

**[09:22]** philosophy when it comes to building systems and I think it's really

**[09:26]** systems and I think it's really

**[09:26]** systems and I think it's really apt for how cloud code was built. So

**[09:29]** apt for how cloud code was built. So

**[09:29]** apt for how cloud code was built. So really just simple is better than

**[09:31]** really just simple is better than

**[09:31]** really just simple is better than complex, complex is better than

**[09:32]** complex, complex is better than

**[09:32]** complex, complex is better than complicated, flat is better than nested.

**[09:34]** complicated, flat is better than nested.

**[09:34]** complicated, flat is better than nested. This is this is all you need to this is

**[09:36]** This is this is all you need to this is

**[09:36]** This is this is all you need to this is the whole talk. This is all you need to

**[09:38]** the whole talk. This is all you need to

**[09:38]** the whole talk. This is all you need to know about how cloud code works and why

**[09:40]** know about how cloud code works and why

**[09:40]** know about how cloud code works and why it works specifically that just in we're

**[09:44]** it works specifically that just in we're

**[09:44]** it works specifically that just in we're going back to engineering principles

**[09:45]** going back to engineering principles

**[09:46]** going back to engineering principles such that simple design is better

**[09:48]** such that simple design is better

**[09:48]** such that simple design is better design. Uh I think this is true whether

**[09:52]** design. Uh I think this is true whether

**[09:52]** design. Uh I think this is true whether you're building a

**[09:58]** database schema uh but this is also true

**[09:58]** database schema uh but this is also true when you're building these autonomous


### [10:00 - 11:00]

**[10:01]** when you're building these autonomous

**[10:01]** when you're building these autonomous coding agents. So let's I'm going to now

**[10:05]** coding agents. So let's I'm going to now

**[10:05]** coding agents. So let's I'm going to now kind of break down all the specific

**[10:07]** kind of break down all the specific

**[10:07]** kind of break down all the specific parts of this coding agent and uh why I

**[10:11]** parts of this coding agent and uh why I

**[10:11]** parts of this coding agent and uh why I think they're interesting. So the first

**[10:12]** think they're interesting. So the first

**[10:12]** think they're interesting. So the first is the constitution. Now a lot of the

**[10:14]** is the constitution. Now a lot of the

**[10:14]** is the constitution. Now a lot of the stuff we kind of take for granted even

**[10:16]** stuff we kind of take for granted even

**[10:16]** stuff we kind of take for granted even though they started doing it a month or

**[10:18]** though they started doing it a month or

**[10:18]** though they started doing it a month or two ago or maybe three or four months

**[10:20]** two ago or maybe three or four months

**[10:20]** two ago or maybe three or four months ago. So this is the cloud MD codeex or

**[10:23]** ago. So this is the cloud MD codeex or

**[10:23]** ago. So this is the cloud MD codeex or others use agents MD. The interesting

**[10:26]** others use agents MD. The interesting

**[10:26]** others use agents MD. The interesting thing I think I assume most of you know

**[10:27]** thing I think I assume most of you know

**[10:28]** thing I think I assume most of you know what it is. Uh it's again it's where you

**[10:30]** what it is. Uh it's again it's where you

**[10:30]** what it is. Uh it's again it's where you put the instructions for your library.

**[10:32]** put the instructions for your library.

**[10:32]** put the instructions for your library. But the interesting thing about this is

**[10:35]** But the interesting thing about this is

**[10:36]** But the interesting thing about this is it's basically the team saying we don't

**[10:39]** it's basically the team saying we don't

**[10:39]** it's basically the team saying we don't need to overengineer a system where the

**[10:42]** need to overengineer a system where the

**[10:42]** need to overengineer a system where the model first researches the repo and

**[10:45]** model first researches the repo and

**[10:45]** model first researches the repo and cursor uh like cursor 1.0 as you know

**[10:49]** cursor uh like cursor 1.0 as you know

**[10:49]** cursor uh like cursor 1.0 as you know makes uh vector DB locally to understand

**[10:52]** makes uh vector DB locally to understand

**[10:52]** makes uh vector DB locally to understand the repo and kind of does all this

**[10:54]** the repo and kind of does all this

**[10:54]** the repo and kind of does all this research. They're just saying, "Ah, just

**[10:56]** research. They're just saying, "Ah, just

**[10:56]** research. They're just saying, "Ah, just put a markdown file. Let the user change

**[10:58]** put a markdown file. Let the user change

**[10:58]** put a markdown file. Let the user change stuff when they need. Let the agent

**[10:59]** stuff when they need. Let the agent

**[10:59]** stuff when they need. Let the agent change stuff when they need very simple


### [11:00 - 12:00]

**[11:02]** change stuff when they need very simple

**[11:02]** change stuff when they need very simple and kind of goes back to prompt

**[11:05]** and kind of goes back to prompt

**[11:05]** and kind of goes back to prompt engineering, which I'm a little biased

**[11:06]** engineering, which I'm a little biased

**[11:06]** engineering, which I'm a little biased towards because prompt layer is a prompt

**[11:09]** towards because prompt layer is a prompt

**[11:09]** towards because prompt layer is a prompt engineering platform, but uh

**[11:10]** engineering platform, but uh

**[11:10]** engineering platform, but uh everything's prompt engineering at the

**[11:12]** everything's prompt engineering at the

**[11:12]** everything's prompt engineering at the end of the day or context engineering.

**[11:14]** end of the day or context engineering.

**[11:14]** end of the day or context engineering. Everything is how do you uh how do you

**[11:17]** Everything is how do you uh how do you

**[11:17]** Everything is how do you uh how do you adapt these general purpose models for

**[11:18]** adapt these general purpose models for

**[11:18]** adapt these general purpose models for your usage?" And the simplest answer is

**[11:21]** your usage?" And the simplest answer is

**[11:21]** your usage?" And the simplest answer is the best one here, I think.

**[11:24]** the best one here, I think.

**[11:24]** the best one here, I think. So this this is the core of the system.

**[11:29]** So this this is the core of the system.

**[11:29]** So this this is the core of the system. It's just a simple master loop. Uh and

**[11:34]** It's just a simple master loop. Uh and

**[11:34]** It's just a simple master loop. Uh and and this is actually kind of

**[11:35]** and this is actually kind of

**[11:35]** and this is actually kind of revolutionary considering how we used to

**[11:37]** revolutionary considering how we used to

**[11:37]** revolutionary considering how we used to build agents. Everything in cloud code

**[11:39]** build agents. Everything in cloud code

**[11:39]** build agents. Everything in cloud code and and all the coding agents today,

**[11:41]** and and all the coding agents today,

**[11:41]** and and all the coding agents today, codeex and and and the new cursor and

**[11:44]** codeex and and and the new cursor and

**[11:44]** codeex and and and the new cursor and AMP and all that, it's just one while

**[11:46]** AMP and all that, it's just one while

**[11:46]** AMP and all that, it's just one while loop with tool calls just running the

**[11:48]** loop with tool calls just running the

**[11:48]** loop with tool calls just running the master while loop calling the tools and

**[11:50]** master while loop calling the tools and

**[11:50]** master while loop calling the tools and going back to the master while loop.

**[11:52]** going back to the master while loop.

**[11:52]** going back to the master while loop. This is basically four lines of what

**[11:55]** This is basically four lines of what

**[11:55]** This is basically four lines of what it's called. I think they call it N0

**[11:57]** it's called. I think they call it N0

**[11:57]** it's called. I think they call it N0 internally. Uh at least based on my


### [12:00 - 13:00]

**[12:00]** internally. Uh at least based on my

**[12:00]** internally. Uh at least based on my research, but while there are tool

**[12:02]** research, but while there are tool

**[12:02]** research, but while there are tool calls, run the tool, give the tool

**[12:05]** calls, run the tool, give the tool

**[12:05]** calls, run the tool, give the tool results to the model, and do it again

**[12:07]** results to the model, and do it again

**[12:07]** results to the model, and do it again until there's no tool calls and then ask

**[12:09]** until there's no tool calls and then ask

**[12:09]** until there's no tool calls and then ask the user what to do. The first time I

**[12:11]** the user what to do. The first time I

**[12:11]** the user what to do. The first time I did this, uh, the first time I used tool

**[12:15]** did this, uh, the first time I used tool

**[12:15]** did this, uh, the first time I used tool calls, it was very shocking to me that

**[12:17]** calls, it was very shocking to me that

**[12:17]** calls, it was very shocking to me that the models are so good at just knowing

**[12:19]** the models are so good at just knowing

**[12:19]** the models are so good at just knowing when to keep calling the tool and

**[12:21]** when to keep calling the tool and

**[12:21]** when to keep calling the tool and knowing when to fix their mistake. And I

**[12:23]** knowing when to fix their mistake. And I

**[12:23]** knowing when to fix their mistake. And I think that's one of the most interesting

**[12:24]** think that's one of the most interesting

**[12:24]** think that's one of the most interesting thing about LM just they're really good

**[12:27]** thing about LM just they're really good

**[12:27]** thing about LM just they're really good at fixing mistakes and being flexible.

**[12:30]** at fixing mistakes and being flexible.

**[12:30]** at fixing mistakes and being flexible. And the more just going back, the more

**[12:31]** And the more just going back, the more

**[12:32]** And the more just going back, the more you lean on the model to explore and uh

**[12:36]** you lean on the model to explore and uh

**[12:36]** you lean on the model to explore and uh figure it out, the better and more

**[12:39]** figure it out, the better and more

**[12:39]** figure it out, the better and more robust your system is going to be when

**[12:41]** robust your system is going to be when

**[12:41]** robust your system is going to be when it comes to better models.

**[12:45]** it comes to better models.

**[12:45]** it comes to better models. So,

**[12:50]** so these are the core tools uh we have

**[12:50]** so these are the core tools uh we have in cloud code today. And to be honest,

**[12:53]** in cloud code today. And to be honest,

**[12:53]** in cloud code today. And to be honest, these change every day. you know,

**[12:55]** these change every day. you know,

**[12:55]** these change every day. you know, they're doing new releases every few

**[12:56]** they're doing new releases every few

**[12:56]** they're doing new releases every few days, but these are the core ones that I

**[12:59]** days, but these are the core ones that I

**[12:59]** days, but these are the core ones that I found most interesting to talk about. Uh


### [13:00 - 14:00]

**[13:02]** found most interesting to talk about. Uh

**[13:02]** found most interesting to talk about. Uh there could be 15 tomorrow, there could

**[13:03]** there could be 15 tomorrow, there could

**[13:04]** there could be 15 tomorrow, there could be down to five tomorrow, but this is

**[13:07]** be down to five tomorrow, but this is

**[13:07]** be down to five tomorrow, but this is what I find interesting. So, first of

**[13:08]** what I find interesting. So, first of

**[13:08]** what I find interesting. So, first of all, read. Uh yeah, they could just do a

**[13:12]** all, read. Uh yeah, they could just do a

**[13:12]** all, read. Uh yeah, they could just do a cat. Uh but what's interesting is read

**[13:15]** cat. Uh but what's interesting is read

**[13:15]** cat. Uh but what's interesting is read is we have token limits. So, if you've

**[13:17]** is we have token limits. So, if you've

**[13:17]** is we have token limits. So, if you've used cloud code a lot, you've seen that

**[13:19]** used cloud code a lot, you've seen that

**[13:19]** used cloud code a lot, you've seen that sometimes it'll say this file's too big

**[13:21]** sometimes it'll say this file's too big

**[13:21]** sometimes it'll say this file's too big or something like that. That's why it's

**[13:23]** or something like that. That's why it's

**[13:23]** or something like that. That's why it's worth building this read tool. Grep

**[13:26]** worth building this read tool. Grep

**[13:26]** worth building this read tool. Grep glob. Uh,

**[13:28]** glob. Uh,

**[13:28]** glob. Uh, this one's very interesting too because

**[13:30]** this one's very interesting too because

**[13:30]** this one's very interesting too because it goes against a lot of the wisdom at

**[13:32]** it goes against a lot of the wisdom at

**[13:32]** it goes against a lot of the wisdom at the time of using rag and using vectors.

**[13:34]** the time of using rag and using vectors.

**[13:34]** the time of using rag and using vectors. And I'm not saying rag has no place by

**[13:36]** And I'm not saying rag has no place by

**[13:36]** And I'm not saying rag has no place by the way either. But in these general

**[13:38]** the way either. But in these general

**[13:38]** the way either. But in these general purpose agents, GP is good and and and

**[13:41]** purpose agents, GP is good and and and

**[13:41]** purpose agents, GP is good and and and GP is uh how users would do it. And I

**[13:44]** GP is uh how users would do it. And I

**[13:44]** GP is uh how users would do it. And I think that's actually a highle point

**[13:46]** think that's actually a highle point

**[13:46]** think that's actually a highle point here. As as you're as I'm talking about

**[13:48]** here. As as you're as I'm talking about

**[13:48]** here. As as you're as I'm talking about these tools, remember these are all

**[13:51]** these tools, remember these are all

**[13:51]** these tools, remember these are all human tasks. They're not we're not

**[13:53]** human tasks. They're not we're not

**[13:53]** human tasks. They're not we're not making up a brand new tool for the model

**[13:55]** making up a brand new tool for the model

**[13:55]** making up a brand new tool for the model to use. We're kind of just mimicking the

**[13:57]** to use. We're kind of just mimicking the

**[13:57]** to use. We're kind of just mimicking the human actions and what you and I would

**[13:59]** human actions and what you and I would

**[13:59]** human actions and what you and I would do if we were at a terminal trying to


### [14:00 - 15:00]

**[14:01]** do if we were at a terminal trying to

**[14:01]** do if we were at a terminal trying to fix a problem. Edit. Edit makes sense. I

**[14:05]** fix a problem. Edit. Edit makes sense. I

**[14:05]** fix a problem. Edit. Edit makes sense. I think the interesting thing to note in

**[14:06]** think the interesting thing to note in

**[14:06]** think the interesting thing to note in edit is it's using diffs and it's not

**[14:08]** edit is it's using diffs and it's not

**[14:08]** edit is it's using diffs and it's not rewriting files most of the time. uh way

**[14:12]** rewriting files most of the time. uh way

**[14:12]** rewriting files most of the time. uh way faster, way way uh less context used,

**[14:15]** faster, way way uh less context used,

**[14:15]** faster, way way uh less context used, but also way less

**[14:17]** but also way less

**[14:18]** but also way less uh issues. Uh if if I asked you to if I

**[14:21]** uh issues. Uh if if I asked you to if I

**[14:21]** uh issues. Uh if if I asked you to if I if I gave you these slides and asked you

**[14:23]** if I gave you these slides and asked you

**[14:23]** if I gave you these slides and asked you to review the slides and you read it and

**[14:25]** to review the slides and you read it and

**[14:25]** to review the slides and you read it and had to write down all the slides for me

**[14:27]** had to write down all the slides for me

**[14:28]** had to write down all the slides for me in your new revisions versus if you

**[14:30]** in your new revisions versus if you

**[14:30]** in your new revisions versus if you could just cross out things in the

**[14:31]** could just cross out things in the

**[14:31]** could just cross out things in the paper, the crossing out is way easier.

**[14:33]** paper, the crossing out is way easier.

**[14:33]** paper, the crossing out is way easier. Diff is kind of a natural thing to

**[14:35]** Diff is kind of a natural thing to

**[14:35]** Diff is kind of a natural thing to prevent mistakes.

**[14:37]** prevent mistakes.

**[14:37]** prevent mistakes. Bash. Bash is uh bash is the core thing

**[14:40]** Bash. Bash is uh bash is the core thing

**[14:40]** Bash. Bash is uh bash is the core thing here. I think you could probably get rid

**[14:43]** here. I think you could probably get rid

**[14:43]** here. I think you could probably get rid of all these tools and only have bash.

**[14:45]** of all these tools and only have bash.

**[14:45]** of all these tools and only have bash. And the first time I saw this when when

**[14:48]** And the first time I saw this when when

**[14:48]** And the first time I saw this when when you run something in claw code and

**[14:51]** you run something in claw code and

**[14:51]** you run something in claw code and claude code creates a Python file and

**[14:53]** claude code creates a Python file and

**[14:53]** claude code creates a Python file and then runs the Python file then deletes

**[14:55]** then runs the Python file then deletes

**[14:55]** then runs the Python file then deletes the Python file. That's that's the

**[14:58]** the Python file. That's that's the

**[14:58]** the Python file. That's that's the beauty of why this thing works. So bash


### [15:00 - 16:00]

**[15:00]** beauty of why this thing works. So bash

**[15:00]** beauty of why this thing works. So bash is the most important. I'd say web

**[15:02]** is the most important. I'd say web

**[15:02]** is the most important. I'd say web search, web fetch. Uh the interesting

**[15:05]** search, web fetch. Uh the interesting

**[15:05]** search, web fetch. Uh the interesting thing about these is they move move it

**[15:06]** thing about these is they move move it

**[15:06]** thing about these is they move move it to a cheaper and faster model. So for

**[15:08]** to a cheaper and faster model. So for

**[15:08]** to a cheaper and faster model. So for example, if you're building a some sort

**[15:11]** example, if you're building a some sort

**[15:11]** example, if you're building a some sort of agent maybe on your platform and

**[15:13]** of agent maybe on your platform and

**[15:13]** of agent maybe on your platform and you're building an agent and it needs to

**[15:14]** you're building an agent and it needs to

**[15:14]** you're building an agent and it needs to connect to some endpoints, some list of

**[15:16]** connect to some endpoints, some list of

**[15:16]** connect to some endpoints, some list of endpoints, might be worth to bring that

**[15:18]** endpoints, might be worth to bring that

**[15:18]** endpoints, might be worth to bring that into a kind of sub tier as opposed to

**[15:23]** into a kind of sub tier as opposed to

**[15:23]** into a kind of sub tier as opposed to that master while loop. That's why this

**[15:25]** that master while loop. That's why this

**[15:25]** that master while loop. That's why this is its own tool. To-dos, uh we've all se

**[15:28]** is its own tool. To-dos, uh we've all se

**[15:28]** is its own tool. To-dos, uh we've all se seen to-dos. talk about it a little bit

**[15:30]** seen to-dos. talk about it a little bit

**[15:30]** seen to-dos. talk about it a little bit more later, but keeping the model on

**[15:32]** more later, but keeping the model on

**[15:32]** more later, but keeping the model on track, steerability, and then tasks.

**[15:34]** track, steerability, and then tasks.

**[15:34]** track, steerability, and then tasks. Tasks is very interesting. It's context

**[15:36]** Tasks is very interesting. It's context

**[15:36]** Tasks is very interesting. It's context management. It's how do we how do we run

**[15:40]** management. It's how do we how do we run

**[15:40]** management. It's how do we how do we run this long process, read this whole file

**[15:41]** this long process, read this whole file

**[15:41]** this long process, read this whole file without cluttering the context? Because

**[15:43]** without cluttering the context? Because

**[15:43]** without cluttering the context? Because the biggest enemy here is when your

**[15:46]** the biggest enemy here is when your

**[15:46]** the biggest enemy here is when your context is full, the model gets stupid

**[15:49]** context is full, the model gets stupid

**[15:49]** context is full, the model gets stupid for lack of better words. So basically,

**[15:51]** for lack of better words. So basically,

**[15:51]** for lack of better words. So basically, bash is all you need. Uh I think this is

**[15:53]** bash is all you need. Uh I think this is

**[15:53]** bash is all you need. Uh I think this is the one thing I want to drill down. The

**[15:55]** the one thing I want to drill down. The

**[15:56]** the one thing I want to drill down. The amazing thing about there's two amazing

**[15:57]** amazing thing about there's two amazing

**[15:57]** amazing thing about there's two amazing things about bash for coding agents. The

**[15:59]** things about bash for coding agents. The

**[15:59]** things about bash for coding agents. The first is that it's simple uh and it does


### [16:00 - 17:00]

**[16:04]** first is that it's simple uh and it does

**[16:04]** first is that it's simple uh and it does everything. It's it's very robust. But

**[16:06]** everything. It's it's very robust. But

**[16:06]** everything. It's it's very robust. But the second thing that's equally

**[16:07]** the second thing that's equally

**[16:07]** the second thing that's equally important is there's so much training

**[16:09]** important is there's so much training

**[16:09]** important is there's so much training data on it because that's what we use.

**[16:11]** data on it because that's what we use.

**[16:11]** data on it because that's what we use. It's not it's the reason that models are

**[16:13]** It's not it's the reason that models are

**[16:13]** It's not it's the reason that models are not as good at Rust or less common

**[16:16]** not as good at Rust or less common

**[16:16]** not as good at Rust or less common programming languages just because

**[16:18]** programming languages just because

**[16:18]** programming languages just because there's less people doing it.

**[16:22]** there's less people doing it.

**[16:22]** there's less people doing it. So it's really the universal adapter.

**[16:23]** So it's really the universal adapter.

**[16:24]** So it's really the universal adapter. Um, you thousands of tools, you could do

**[16:26]** Um, you thousands of tools, you could do

**[16:26]** Um, you thousands of tools, you could do anything. Uh, this is that Python

**[16:29]** anything. Uh, this is that Python

**[16:29]** anything. Uh, this is that Python example I gave. I I I always find it so

**[16:31]** example I gave. I I I always find it so

**[16:31]** example I gave. I I I always find it so cool when it does the Python script

**[16:32]** cool when it does the Python script

**[16:32]** cool when it does the Python script thing or creates tests and I always have

**[16:34]** thing or creates tests and I always have

**[16:34]** thing or creates tests and I always have to tell it not to. But it all these

**[16:37]** to tell it not to. But it all these

**[16:37]** to tell it not to. But it all these shell tools are in it. And this is I

**[16:40]** shell tools are in it. And this is I

**[16:40]** shell tools are in it. And this is I mean I find myself using cloud code to

**[16:42]** mean I find myself using cloud code to

**[16:42]** mean I find myself using cloud code to spin up local environments where

**[16:44]** spin up local environments where

**[16:44]** spin up local environments where normally I'd have like five commands

**[16:46]** normally I'd have like five commands

**[16:46]** normally I'd have like five commands written down on some file somewhere and

**[16:48]** written down on some file somewhere and

**[16:48]** written down on some file somewhere and then they get out of date. It's really

**[16:50]** then they get out of date. It's really

**[16:50]** then they get out of date. It's really good at figuring this stuff out and

**[16:51]** good at figuring this stuff out and

**[16:51]** good at figuring this stuff out and running the stuff you'd want to do.

**[16:53]** running the stuff you'd want to do.

**[16:53]** running the stuff you'd want to do. uh and it specifically lets the model

**[16:56]** uh and it specifically lets the model

**[16:56]** uh and it specifically lets the model try things.

**[16:58]** try things.

**[16:58]** try things. So uh yeah, the other suggestions here


### [17:00 - 18:00]

**[17:02]** So uh yeah, the other suggestions here

**[17:02]** So uh yeah, the other suggestions here and the tool usage uh I think there's a

**[17:06]** and the tool usage uh I think there's a

**[17:06]** and the tool usage uh I think there's a little bit of a system prompt uh that

**[17:08]** little bit of a system prompt uh that

**[17:08]** little bit of a system prompt uh that tells it which to use and when to use

**[17:11]** tells it which to use and when to use

**[17:11]** tells it which to use and when to use which tool over which and this changes a

**[17:13]** which tool over which and this changes a

**[17:13]** which tool over which and this changes a lot but the these are kind of like the

**[17:14]** lot but the these are kind of like the

**[17:14]** lot but the these are kind of like the edge cases and the corners you find the

**[17:16]** edge cases and the corners you find the

**[17:16]** edge cases and the corners you find the model getting stuck in. So reading

**[17:18]** model getting stuck in. So reading

**[17:18]** model getting stuck in. So reading before editing uh they actually make

**[17:20]** before editing uh they actually make

**[17:20]** before editing uh they actually make make you do that using GP the tool

**[17:23]** make you do that using GP the tool

**[17:23]** make you do that using GP the tool instead of the bash. So if you look at

**[17:27]** instead of the bash. So if you look at

**[17:27]** instead of the bash. So if you look at the tool list here there's a special GP

**[17:29]** the tool list here there's a special GP

**[17:29]** the tool list here there's a special GP tool. Uh there could be a lot of reasons

**[17:32]** tool. Uh there could be a lot of reasons

**[17:32]** tool. Uh there could be a lot of reasons for that. I think security is a big one

**[17:34]** for that. I think security is a big one

**[17:34]** for that. I think security is a big one uh and sandboxing but then also just

**[17:37]** uh and sandboxing but then also just

**[17:37]** uh and sandboxing but then also just that token limit thing running

**[17:39]** that token limit thing running

**[17:39]** that token limit thing running independent operations in parallel. Uh,

**[17:41]** independent operations in parallel. Uh,

**[17:41]** independent operations in parallel. Uh, so kind of pushing the model to do that

**[17:43]** so kind of pushing the model to do that

**[17:43]** so kind of pushing the model to do that more. And then also like these trivial

**[17:45]** more. And then also like these trivial

**[17:45]** more. And then also like these trivial things like quoting paths with spaces.

**[17:47]** things like quoting paths with spaces.

**[17:47]** things like quoting paths with spaces. It's just the common common things. I'm

**[17:49]** It's just the common common things. I'm

**[17:49]** It's just the common common things. I'm sure they're just dog fooding a lot at

**[17:51]** sure they're just dog fooding a lot at

**[17:51]** sure they're just dog fooding a lot at anthropic and they find it and they're

**[17:52]** anthropic and they find it and they're

**[17:52]** anthropic and they find it and they're like, "All right, we'll throw it in the

**[17:53]** like, "All right, we'll throw it in the

**[17:53]** like, "All right, we'll throw it in the system prompt."

**[17:55]** system prompt."

**[17:55]** system prompt." Okay, so let's talk about to-do lists.

**[17:57]** Okay, so let's talk about to-do lists.

**[17:57]** Okay, so let's talk about to-do lists. Uh, now again, a very common thing, but


### [18:00 - 19:00]

**[18:01]** Uh, now again, a very common thing, but

**[18:01]** Uh, now again, a very common thing, but was not a common thing before. The the

**[18:04]** was not a common thing before. The the

**[18:04]** was not a common thing before. The the So this is actually I think a to-do list

**[18:06]** So this is actually I think a to-do list

**[18:06]** So this is actually I think a to-do list for from some of my my research for this

**[18:08]** for from some of my my research for this

**[18:08]** for from some of my my research for this slide deck. Um, but the really

**[18:11]** slide deck. Um, but the really

**[18:11]** slide deck. Um, but the really interesting thing about to-do lists is

**[18:14]** interesting thing about to-do lists is

**[18:14]** interesting thing about to-do lists is that they're structured but not

**[18:17]** that they're structured but not

**[18:17]** that they're structured but not structurally enforced. So, here are the

**[18:21]** structurally enforced. So, here are the

**[18:21]** structurally enforced. So, here are the rules. One task at a time. Uh, mark them

**[18:24]** rules. One task at a time. Uh, mark them

**[18:24]** rules. One task at a time. Uh, mark them completed. This is kind of stuff you

**[18:26]** completed. This is kind of stuff you

**[18:26]** completed. This is kind of stuff you would expect. Uh, keep working on the in

**[18:29]** would expect. Uh, keep working on the in

**[18:29]** would expect. Uh, keep working on the in progress if there's block blocks or

**[18:31]** progress if there's block blocks or

**[18:31]** progress if there's block blocks or errors and kind of break up the tasks

**[18:34]** errors and kind of break up the tasks

**[18:34]** errors and kind of break up the tasks into different instructions. But the

**[18:37]** into different instructions. But the

**[18:37]** into different instructions. But the most interesting thing to me is it's not

**[18:39]** most interesting thing to me is it's not

**[18:39]** most interesting thing to me is it's not enforced deterministically. It's purely

**[18:42]** enforced deterministically. It's purely

**[18:42]** enforced deterministically. It's purely prompt based. It's purely in the system

**[18:44]** prompt based. It's purely in the system

**[18:44]** prompt based. It's purely in the system prompt. It's purely because our models

**[18:47]** prompt. It's purely because our models

**[18:47]** prompt. It's purely because our models are just good at instruction following

**[18:49]** are just good at instruction following

**[18:49]** are just good at instruction following now. And this would not have worked a

**[18:51]** now. And this would not have worked a

**[18:51]** now. And this would not have worked a year ago. This would not have worked two

**[18:52]** year ago. This would not have worked two

**[18:52]** year ago. This would not have worked two years ago. Um there's tool descriptions

**[18:55]** years ago. Um there's tool descriptions

**[18:55]** years ago. Um there's tool descriptions at the top of the system prompt. We're

**[18:57]** at the top of the system prompt. We're

**[18:57]** at the top of the system prompt. We're kind of uh injecting the todos into the


### [19:00 - 20:00]

**[19:01]** kind of uh injecting the todos into the

**[19:01]** kind of uh injecting the todos into the system prompt. uh there's they're not

**[19:04]** system prompt. uh there's they're not

**[19:04]** system prompt. uh there's they're not but it but it's not enforced in actual

**[19:06]** but it but it's not enforced in actual

**[19:06]** but it but it's not enforced in actual code and again uh maybe there's other

**[19:09]** code and again uh maybe there's other

**[19:09]** code and again uh maybe there's other agents that take an opposite path. Uh I

**[19:11]** agents that take an opposite path. Uh I

**[19:11]** agents that take an opposite path. Uh I just found this pretty interesting that

**[19:13]** just found this pretty interesting that

**[19:13]** just found this pretty interesting that this at least as a user makes a big

**[19:16]** this at least as a user makes a big

**[19:16]** this at least as a user makes a big difference and it doesn't even see it

**[19:18]** difference and it doesn't even see it

**[19:18]** difference and it doesn't even see it seems it was it seems like it was very

**[19:21]** seems it was it seems like it was very

**[19:21]** seems it was it seems like it was very simple to implement almost a a weekend

**[19:23]** simple to implement almost a a weekend

**[19:23]** simple to implement almost a a weekend project someone did and seemed to work.

**[19:25]** project someone did and seemed to work.

**[19:25]** project someone did and seemed to work. could be wrong about about that as well,

**[19:27]** could be wrong about about that as well,

**[19:27]** could be wrong about about that as well, but uh um so yeah, it's literally a

**[19:30]** but uh um so yeah, it's literally a

**[19:30]** but uh um so yeah, it's literally a function call. Uh

**[19:32]** function call. Uh

**[19:32]** function call. Uh it's the first time you ask something,

**[19:35]** it's the first time you ask something,

**[19:35]** it's the first time you ask something, the reasoning exports this to-do block,

**[19:37]** the reasoning exports this to-do block,

**[19:37]** the reasoning exports this to-do block, and I'll show you what the structure is

**[19:38]** and I'll show you what the structure is

**[19:38]** and I'll show you what the structure is on the next slide. Uh there's ids there.

**[19:41]** on the next slide. Uh there's ids there.

**[19:42]** on the next slide. Uh there's ids there. There's some kind of structured schema

**[19:44]** There's some kind of structured schema

**[19:44]** There's some kind of structured schema and determinism, but

**[19:47]** and determinism, but

**[19:47]** and determinism, but it it's just injected there. So here's a

**[19:51]** it it's just injected there. So here's a

**[19:51]** it it's just injected there. So here's a example of what it could look like. You

**[19:53]** example of what it could look like. You

**[19:53]** example of what it could look like. You get a version, you get your ID, uh a

**[19:56]** get a version, you get your ID, uh a

**[19:56]** get a version, you get your ID, uh a title of the to-do, and then it could

**[19:57]** title of the to-do, and then it could

**[19:58]** title of the to-do, and then it could actually inject evidence. So, this is uh


### [20:00 - 21:00]

**[20:00]** actually inject evidence. So, this is uh

**[20:00]** actually inject evidence. So, this is uh seemingly arbitrary blobs of data it

**[20:03]** seemingly arbitrary blobs of data it

**[20:03]** seemingly arbitrary blobs of data it could use. And the ids are hashes that

**[20:06]** could use. And the ids are hashes that

**[20:06]** could use. And the ids are hashes that it could then refer to

**[20:08]** it could then refer to

**[20:08]** it could then refer to title, something human readable, but

**[20:11]** title, something human readable, but

**[20:11]** title, something human readable, but this is a just another way to structure

**[20:13]** this is a just another way to structure

**[20:13]** this is a just another way to structure the data. And in the same way that

**[20:15]** the data. And in the same way that

**[20:15]** the data. And in the same way that you're going to organize your desk when

**[20:17]** you're going to organize your desk when

**[20:17]** you're going to organize your desk when you work, this is how we're trying to

**[20:19]** you work, this is how we're trying to

**[20:19]** you work, this is how we're trying to organize the model.

**[20:21]** organize the model.

**[20:21]** organize the model. So I think there's uh these are kind of

**[20:24]** So I think there's uh these are kind of

**[20:24]** So I think there's uh these are kind of the four benefits we're getting. We're

**[20:26]** the four benefits we're getting. We're

**[20:26]** the four benefits we're getting. We're forcing it to plan. Uh we get to resume

**[20:29]** forcing it to plan. Uh we get to resume

**[20:29]** forcing it to plan. Uh we get to resume after crashes. Uh clog code fails. I

**[20:33]** after crashes. Uh clog code fails. I

**[20:33]** after crashes. Uh clog code fails. I think UX is a big part of this. As a

**[20:35]** think UX is a big part of this. As a

**[20:35]** think UX is a big part of this. As a user, you know how it's going. It's not

**[20:38]** user, you know how it's going. It's not

**[20:38]** user, you know how it's going. It's not just running off in a loop for 40

**[20:40]** just running off in a loop for 40

**[20:40]** just running off in a loop for 40 minutes without any uh signal to you. So

**[20:42]** minutes without any uh signal to you. So

**[20:42]** minutes without any uh signal to you. So UX is non-negligible. Even though UX

**[20:45]** UX is non-negligible. Even though UX

**[20:45]** UX is non-negligible. Even though UX might not make it a better coding agent,

**[20:46]** might not make it a better coding agent,

**[20:46]** might not make it a better coding agent, it might make it better for us all to

**[20:48]** it might make it better for us all to

**[20:48]** it might make it better for us all to use. and uh the steerability one. So

**[20:52]** use. and uh the steerability one. So

**[20:52]** use. and uh the steerability one. So here's two other parts that were under

**[20:55]** here's two other parts that were under

**[20:55]** here's two other parts that were under the hood. Async buffer, so they called

**[20:57]** the hood. Async buffer, so they called

**[20:57]** the hood. Async buffer, so they called it H2A. Uh it's kind of uh the IO


### [21:00 - 22:00]

**[21:02]** it H2A. Uh it's kind of uh the IO

**[21:02]** it H2A. Uh it's kind of uh the IO process and how to decouple it from

**[21:04]** process and how to decouple it from

**[21:04]** process and how to decouple it from reasoning and and how to manage context

**[21:06]** reasoning and and how to manage context

**[21:06]** reasoning and and how to manage context in a way that you're not just stuffing

**[21:08]** in a way that you're not just stuffing

**[21:08]** in a way that you're not just stuffing everything you're seeing in the terminal

**[21:09]** everything you're seeing in the terminal

**[21:09]** everything you're seeing in the terminal and everything back into the model,

**[21:11]** and everything back into the model,

**[21:11]** and everything back into the model, which again context is our biggest enemy

**[21:13]** which again context is our biggest enemy

**[21:13]** which again context is our biggest enemy here. It's going to make the model

**[21:14]** here. It's going to make the model

**[21:14]** here. It's going to make the model stupider. So we need to uh be a little

**[21:17]** stupider. So we need to uh be a little

**[21:17]** stupider. So we need to uh be a little bit smart about that and and how we do

**[21:20]** bit smart about that and and how we do

**[21:20]** bit smart about that and and how we do compact and how we do summarization. So

**[21:23]** compact and how we do summarization. So

**[21:23]** compact and how we do summarization. So here you see when it reaches capacity it

**[21:24]** here you see when it reaches capacity it

**[21:24]** here you see when it reaches capacity it kind of drops the middle summarizes the

**[21:26]** kind of drops the middle summarizes the

**[21:26]** kind of drops the middle summarizes the head and tail. Um then we have the

**[21:30]** head and tail. Um then we have the

**[21:30]** head and tail. Um then we have the that's the context compressor there. So

**[21:32]** that's the context compressor there. So

**[21:32]** that's the context compressor there. So what is the limit 92% it seems like

**[21:36]** what is the limit 92% it seems like

**[21:36]** what is the limit 92% it seems like something like that. Uh and and how does

**[21:39]** something like that. Uh and and how does

**[21:39]** something like that. Uh and and how does it how does it save long-term storage?

**[21:42]** it how does it save long-term storage?

**[21:42]** it how does it save long-term storage? That's actually another kind of

**[21:44]** That's actually another kind of

**[21:44]** That's actually another kind of advantage of bash in my opinion and

**[21:46]** advantage of bash in my opinion and

**[21:46]** advantage of bash in my opinion and having a sandbox. I would even make a

**[21:48]** having a sandbox. I would even make a

**[21:48]** having a sandbox. I would even make a prediction here that all your all chat

**[21:50]** prediction here that all your all chat

**[21:50]** prediction here that all your all chat GPT windows, all clawed windows are

**[21:52]** GPT windows, all clawed windows are

**[21:52]** GPT windows, all clawed windows are going to come with a sandbox in the near

**[21:54]** going to come with a sandbox in the near

**[21:54]** going to come with a sandbox in the near future. It's just so much better because

**[21:56]** future. It's just so much better because

**[21:56]** future. It's just so much better because you can store that long-term memory. And

**[21:59]** you can store that long-term memory. And

**[21:59]** you can store that long-term memory. And I do this all the time. I have I have


### [22:00 - 23:00]

**[22:01]** I do this all the time. I have I have

**[22:01]** I do this all the time. I have I have cloud code skills for deep research and

**[22:03]** cloud code skills for deep research and

**[22:03]** cloud code skills for deep research and stuff like that. And I'm always

**[22:04]** stuff like that. And I'm always

**[22:04]** stuff like that. And I'm always instructing it save markdown files

**[22:06]** instructing it save markdown files

**[22:06]** instructing it save markdown files because the shorter the context, the

**[22:08]** because the shorter the context, the

**[22:08]** because the shorter the context, the quicker it is and the smarter it is.

**[22:12]** quicker it is and the smarter it is.

**[22:12]** quicker it is and the smarter it is. So this is what I'm most excited about.

**[22:15]** So this is what I'm most excited about.

**[22:15]** So this is what I'm most excited about. We don't need DAGs like this. We

**[22:18]** We don't need DAGs like this. We

**[22:18]** We don't need DAGs like this. We I'll give you I'll give you a real

**[22:19]** I'll give you I'll give you a real

**[22:19]** I'll give you I'll give you a real example. Uh so some users at prompt

**[22:23]** example. Uh so some users at prompt

**[22:23]** example. Uh so some users at prompt layer uh different agents like customer

**[22:26]** layer uh different agents like customer

**[22:26]** layer uh different agents like customer support agent basically everybody was

**[22:28]** support agent basically everybody was

**[22:28]** support agent basically everybody was building DAGs like this for the last two

**[22:30]** building DAGs like this for the last two

**[22:30]** building DAGs like this for the last two two and a half years. Uh and it was

**[22:34]** two and a half years. Uh and it was

**[22:34]** two and a half years. Uh and it was crazy. Hundreds of nodes of okay this if

**[22:38]** crazy. Hundreds of nodes of okay this if

**[22:38]** crazy. Hundreds of nodes of okay this if this user wants a refund route them to

**[22:40]** this user wants a refund route them to

**[22:40]** this user wants a refund route them to this prompt if they want this and a lot

**[22:43]** this prompt if they want this and a lot

**[22:43]** this prompt if they want this and a lot of uh classifying prompts. The advantage

**[22:46]** of uh classifying prompts. The advantage

**[22:46]** of uh classifying prompts. The advantage of this is you can kind of guarantee

**[22:47]** of this is you can kind of guarantee

**[22:47]** of this is you can kind of guarantee there's not going to be hallucinations

**[22:49]** there's not going to be hallucinations

**[22:49]** there's not going to be hallucinations or guarantee there's not going to be

**[22:52]** or guarantee there's not going to be

**[22:52]** or guarantee there's not going to be refunds to people who shouldn't be

**[22:53]** refunds to people who shouldn't be

**[22:53]** refunds to people who shouldn't be having refunds or kind of that pro it

**[22:56]** having refunds or kind of that pro it

**[22:56]** having refunds or kind of that pro it solves the prompt injection problem

**[22:57]** solves the prompt injection problem

**[22:57]** solves the prompt injection problem because if you're in a prompt that

**[22:59]** because if you're in a prompt that

**[22:59]** because if you're in a prompt that purely classifies it as X or Y injecting


### [23:00 - 24:00]

**[23:02]** purely classifies it as X or Y injecting

**[23:02]** purely classifies it as X or Y injecting doesn't really matter especially if you

**[23:03]** doesn't really matter especially if you

**[23:03]** doesn't really matter especially if you throw out the context. Now we kind of

**[23:06]** throw out the context. Now we kind of

**[23:06]** throw out the context. Now we kind of brought back bring back that attack

**[23:08]** brought back bring back that attack

**[23:08]** brought back bring back that attack vector but the but the major benefit is

**[23:10]** vector but the but the major benefit is

**[23:10]** vector but the but the major benefit is we don't have to deal with this web of

**[23:13]** we don't have to deal with this web of

**[23:13]** we don't have to deal with this web of engineering uh madness and uh it just

**[23:16]** engineering uh madness and uh it just

**[23:16]** engineering uh madness and uh it just it's 10x easier to develop these things

**[23:18]** it's 10x easier to develop these things

**[23:18]** it's 10x easier to develop these things 10x more maintainable and it actually

**[23:20]** 10x more maintainable and it actually

**[23:20]** 10x more maintainable and it actually works way better because our models are

**[23:22]** works way better because our models are

**[23:22]** works way better because our models are just good now.

**[23:24]** just good now.

**[23:24]** just good now. So this is this is kind of a takeaway is

**[23:27]** So this is this is kind of a takeaway is

**[23:27]** So this is this is kind of a takeaway is rely on the model. uh when in doubt,

**[23:31]** rely on the model. uh when in doubt,

**[23:31]** rely on the model. uh when in doubt, don't don't try to think through every

**[23:34]** don't don't try to think through every

**[23:34]** don't don't try to think through every edge case and think through every if

**[23:35]** edge case and think through every if

**[23:35]** edge case and think through every if statement. Just rely on the model to

**[23:38]** statement. Just rely on the model to

**[23:38]** statement. Just rely on the model to explore and figure it out. And I was

**[23:40]** explore and figure it out. And I was

**[23:40]** explore and figure it out. And I was actually two days ago, I think, or

**[23:42]** actually two days ago, I think, or

**[23:42]** actually two days ago, I think, or yesterday, sometime this week, I was

**[23:44]** yesterday, sometime this week, I was

**[23:44]** yesterday, sometime this week, I was doing an experiment on our dashboard to

**[23:48]** doing an experiment on our dashboard to

**[23:48]** doing an experiment on our dashboard to add like trying these browser agents.

**[23:51]** add like trying these browser agents.

**[23:51]** add like trying these browser agents. And I wanted to see if I could add

**[23:52]** And I wanted to see if I could add

**[23:52]** And I wanted to see if I could add little titles to all our buttons and it

**[23:55]** little titles to all our buttons and it

**[23:55]** little titles to all our buttons and it would help the agent navigate our

**[23:56]** would help the agent navigate our

**[23:56]** would help the agent navigate our website automatically. And it actually

**[23:59]** website automatically. And it actually

**[23:59]** website automatically. And it actually made it worse, surprisingly. Uh, and


### [24:00 - 25:00]

**[24:01]** made it worse, surprisingly. Uh, and

**[24:01]** made it worse, surprisingly. Uh, and maybe I could run it again and maybe I

**[24:03]** maybe I could run it again and maybe I

**[24:03]** maybe I could run it again and maybe I did something wrong with this test, but

**[24:04]** did something wrong with this test, but

**[24:04]** did something wrong with this test, but it made the agent navigate prompt layer

**[24:06]** it made the agent navigate prompt layer

**[24:06]** it made the agent navigate prompt layer worse because it was getting distracted

**[24:09]** worse because it was getting distracted

**[24:09]** worse because it was getting distracted because I was telling it you have to

**[24:10]** because I was telling it you have to

**[24:10]** because I was telling it you have to click this button, then you have to

**[24:11]** click this button, then you have to

**[24:11]** click this button, then you have to click this button and then

**[24:14]** click this button and then

**[24:14]** click this button and then it's it didn't know what to do. So, it's

**[24:16]** it's it didn't know what to do. So, it's

**[24:16]** it's it didn't know what to do. So, it's better to rely on exploration. You have

**[24:18]** better to rely on exploration. You have

**[24:18]** better to rely on exploration. You have a question?

**[24:19]** a question?

**[24:19]** a question? >> Yeah, I'll I'll push back a little bit,

**[24:22]** >> Yeah, I'll I'll push back a little bit,

**[24:22]** >> Yeah, I'll I'll push back a little bit, >> please. I'll admit any

**[24:25]** >> please. I'll admit any

**[24:25]** >> please. I'll admit any scaffolding we create today to resolve

**[24:29]** scaffolding we create today to resolve

**[24:29]** scaffolding we create today to resolve the idiosyncrasies of limitations will

**[24:33]** the idiosyncrasies of limitations will

**[24:33]** the idiosyncrasies of limitations will be that'll be obsolete 3 to 6 months

**[24:36]** be that'll be obsolete 3 to 6 months

**[24:36]** be that'll be obsolete 3 to 6 months even if that's the case they help a

**[24:38]** even if that's the case they help a

**[24:38]** even if that's the case they help a little bit today I how do you balance

**[24:41]** little bit today I how do you balance

**[24:41]** little bit today I how do you balance that like wasted engineering to solve a

**[24:44]** that like wasted engineering to solve a

**[24:44]** that like wasted engineering to solve a problem we only have for three months

**[24:46]** problem we only have for three months

**[24:46]** problem we only have for three months >> it's a great question so just to repeat

**[24:48]** >> it's a great question so just to repeat

**[24:48]** >> it's a great question so just to repeat uh the question is basically

**[24:52]** uh the question is basically

**[24:52]** uh the question is basically what is the trade-off between solving

**[24:54]** what is the trade-off between solving

**[24:54]** what is the trade-off between solving the actual problems we have today and if

**[24:55]** the actual problems we have today and if

**[24:55]** the actual problems we have today and if you're relying on the model that can't

**[24:57]** you're relying on the model that can't

**[24:57]** you're relying on the model that can't do it yet but it'll be able to do it in

**[24:59]** do it yet but it'll be able to do it in

**[24:59]** do it yet but it'll be able to do it in three months, right? Um it's case by


### [25:00 - 26:00]

**[25:01]** three months, right? Um it's case by

**[25:02]** three months, right? Um it's case by case. It depends what you're building.

**[25:03]** case. It depends what you're building.

**[25:03]** case. It depends what you're building. If you're building a chatbot for a bank,

**[25:05]** If you're building a chatbot for a bank,

**[25:05]** If you're building a chatbot for a bank, you probably do want to be a little bit

**[25:07]** you probably do want to be a little bit

**[25:07]** you probably do want to be a little bit more comp be careful. To me, the happy

**[25:10]** more comp be careful. To me, the happy

**[25:10]** more comp be careful. To me, the happy middle ground is to use this agent

**[25:14]** middle ground is to use this agent

**[25:14]** middle ground is to use this agent paradigm of a master while loop and tool

**[25:17]** paradigm of a master while loop and tool

**[25:17]** paradigm of a master while loop and tool calls, but make your tool calls very

**[25:19]** calls, but make your tool calls very

**[25:19]** calls, but make your tool calls very rigorous. So I think it's okay to have a

**[25:22]** rigorous. So I think it's okay to have a

**[25:22]** rigorous. So I think it's okay to have a tool call that looks like this or looks

**[25:24]** tool call that looks like this or looks

**[25:24]** tool call that looks like this or looks like half of this uh in the same way

**[25:26]** like half of this uh in the same way

**[25:26]** like half of this uh in the same way that claude code uses read as a tool

**[25:29]** that claude code uses read as a tool

**[25:29]** that claude code uses read as a tool call or GP as a tool call. So for the

**[25:32]** call or GP as a tool call. So for the

**[25:32]** call or GP as a tool call. So for the edge cases,

**[25:34]** edge cases,

**[25:34]** edge cases, throw it in a structured tool that you

**[25:36]** throw it in a structured tool that you

**[25:36]** throw it in a structured tool that you can then eval in version and stuff like

**[25:38]** can then eval in version and stuff like

**[25:38]** can then eval in version and stuff like that. And I could talk I'm going to talk

**[25:39]** that. And I could talk I'm going to talk

**[25:39]** that. And I could talk I'm going to talk a little bit more about that later, but

**[25:41]** a little bit more about that later, but

**[25:41]** a little bit more about that later, but throw it in that structured tool. But

**[25:43]** throw it in that structured tool. But

**[25:43]** throw it in that structured tool. But for everything else, uh for the

**[25:45]** for everything else, uh for the

**[25:45]** for everything else, uh for the exploration phase, leave it to the model

**[25:48]** exploration phase, leave it to the model

**[25:48]** exploration phase, leave it to the model or throw some system prompt. Uh so

**[25:54]** or throw some system prompt. Uh so

**[25:54]** or throw some system prompt. Uh so it's a trade-off and it's very use case

**[25:55]** it's a trade-off and it's very use case

**[25:55]** it's a trade-off and it's very use case dependent, but I think it's a good

**[25:57]** dependent, but I think it's a good

**[25:57]** dependent, but I think it's a good question. Thank you. So yeah, uh just


### [26:00 - 27:00]

**[26:01]** question. Thank you. So yeah, uh just

**[26:01]** question. Thank you. So yeah, uh just back to cloud code. Uh we're we're

**[26:04]** back to cloud code. Uh we're we're

**[26:04]** back to cloud code. Uh we're we're getting rid of all this stuff. We're

**[26:05]** getting rid of all this stuff. We're

**[26:05]** getting rid of all this stuff. We're saying we don't want MLbased intent

**[26:07]** saying we don't want MLbased intent

**[26:07]** saying we don't want MLbased intent detection. We don't want reax. We don't

**[26:08]** detection. We don't want reax. We don't

**[26:08]** detection. We don't want reax. We don't want the I mean it uses reax a little

**[26:10]** want the I mean it uses reax a little

**[26:10]** want the I mean it uses reax a little bit, but we don't want reax baked into

**[26:12]** bit, but we don't want reax baked into

**[26:12]** bit, but we don't want reax baked into it. We don't want classifiers. And and

**[26:14]** it. We don't want classifiers. And and

**[26:14]** it. We don't want classifiers. And and there was a long time we actually built

**[26:16]** there was a long time we actually built

**[26:16]** there was a long time we actually built a product for prompt layer. We never

**[26:18]** a product for prompt layer. We never

**[26:18]** a product for prompt layer. We never released it because there's only a

**[26:19]** released it because there's only a

**[26:19]** released it because there's only a prototype of using a MLbased like a

**[26:22]** prototype of using a MLbased like a

**[26:22]** prototype of using a MLbased like a nonlm based classifier in your prompt

**[26:25]** nonlm based classifier in your prompt

**[26:25]** nonlm based classifier in your prompt pipeline instead of LMS. A lot of people

**[26:27]** pipeline instead of LMS. A lot of people

**[26:27]** pipeline instead of LMS. A lot of people have a lot of success with it, but

**[26:30]** have a lot of success with it, but

**[26:30]** have a lot of success with it, but it it feels more and more like it's not

**[26:33]** it it feels more and more like it's not

**[26:33]** it it feels more and more like it's not going to be that helpful unless cost is

**[26:34]** going to be that helpful unless cost is

**[26:34]** going to be that helpful unless cost is a huge concern for you. And even then

**[26:36]** a huge concern for you. And even then

**[26:36]** a huge concern for you. And even then cost is the smaller models is going less

**[26:39]** cost is the smaller models is going less

**[26:39]** cost is the smaller models is going less and less as uh kind of financial

**[26:43]** and less as uh kind of financial

**[26:43]** and less as uh kind of financial engineering between all these companies

**[26:44]** engineering between all these companies

**[26:44]** engineering between all these companies pays for our tokens. Um so Claude does

**[26:50]** pays for our tokens. Um so Claude does

**[26:50]** pays for our tokens. Um so Claude does also this smart thing I think with the

**[26:51]** also this smart thing I think with the

**[26:51]** also this smart thing I think with the trigger phases. you know, you have

**[26:53]** trigger phases. you know, you have

**[26:53]** trigger phases. you know, you have think, think hard, think harder, and

**[26:55]** think, think hard, think harder, and

**[26:55]** think, think hard, think harder, and ultra think is my favorite. Uh, and this

**[26:58]** ultra think is my favorite. Uh, and this

**[26:58]** ultra think is my favorite. Uh, and this lets us use the reasoning budget, the


### [27:00 - 28:00]

**[27:01]** lets us use the reasoning budget, the

**[27:01]** lets us use the reasoning budget, the reasoning token budget as another

**[27:03]** reasoning token budget as another

**[27:03]** reasoning token budget as another parameter that the model can adjust. And

**[27:05]** parameter that the model can adjust. And

**[27:05]** parameter that the model can adjust. And this is actually the model can adjust

**[27:07]** this is actually the model can adjust

**[27:07]** this is actually the model can adjust this, but this is how we force it to

**[27:08]** this, but this is how we force it to

**[27:08]** this, but this is how we force it to adjust. And as opposed to you could make

**[27:11]** adjust. And as opposed to you could make

**[27:11]** adjust. And as opposed to you could make a tool call for

**[27:13]** a tool call for

**[27:13]** a tool call for hard planning. And actually, there's

**[27:15]** hard planning. And actually, there's

**[27:15]** hard planning. And actually, there's some coding agents that do this. or you

**[27:17]** some coding agents that do this. or you

**[27:17]** some coding agents that do this. or you can uh let the user specify it and then

**[27:20]** can uh let the user specify it and then

**[27:20]** can uh let the user specify it and then just on the fly change it.

**[27:23]** just on the fly change it.

**[27:23]** just on the fly change it. So this is this is one of the biggest

**[27:25]** So this is this is one of the biggest

**[27:26]** So this is this is one of the biggest topics here. Sandboxing and permissions.

**[27:28]** topics here. Sandboxing and permissions.

**[27:28]** topics here. Sandboxing and permissions. I'm going to be completely honest, it's

**[27:30]** I'm going to be completely honest, it's

**[27:30]** I'm going to be completely honest, it's the most boring part of this to me

**[27:32]** the most boring part of this to me

**[27:32]** the most boring part of this to me because I just run it on YOLO mode half

**[27:34]** because I just run it on YOLO mode half

**[27:34]** because I just run it on YOLO mode half the time. Um it's uh

**[27:39]** the time. Um it's uh

**[27:39]** the time. Um it's uh some people on our team actually dropped

**[27:40]** some people on our team actually dropped

**[27:40]** some people on our team actually dropped all their local databases. So you do

**[27:42]** all their local databases. So you do

**[27:42]** all their local databases. So you do have to be careful. Uh so uh you know we

**[27:46]** have to be careful. Uh so uh you know we

**[27:46]** have to be careful. Uh so uh you know we don't yolo mode with our enterprise

**[27:47]** don't yolo mode with our enterprise

**[27:47]** don't yolo mode with our enterprise customers obviously but uh I but but I

**[27:51]** customers obviously but uh I but but I

**[27:52]** customers obviously but uh I but but I think this stuff is it feels like it's

**[27:54]** think this stuff is it feels like it's

**[27:54]** think this stuff is it feels like it's going to be solved but but we do need to

**[27:55]** going to be solved but but we do need to

**[27:55]** going to be solved but but we do need to know how to works a little bit. So

**[27:58]** know how to works a little bit. So

**[27:58]** know how to works a little bit. So there's a big issue of in prompt


### [28:00 - 29:00]

**[28:01]** there's a big issue of in prompt

**[28:01]** there's a big issue of in prompt injection from the internet. If you're

**[28:03]** injection from the internet. If you're

**[28:03]** injection from the internet. If you're connecting this agent that has shell

**[28:07]** connecting this agent that has shell

**[28:07]** connecting this agent that has shell access and you're doing web fetch that's

**[28:10]** access and you're doing web fetch that's

**[28:10]** access and you're doing web fetch that's a pretty big attack vector. Uh, so

**[28:12]** a pretty big attack vector. Uh, so

**[28:12]** a pretty big attack vector. Uh, so there's some containerization of that.

**[28:14]** there's some containerization of that.

**[28:14]** there's some containerization of that. There's blocking URLs. You could see

**[28:17]** There's blocking URLs. You could see

**[28:17]** There's blocking URLs. You could see cloud code's pretty annoying about can I

**[28:19]** cloud code's pretty annoying about can I

**[28:19]** cloud code's pretty annoying about can I fetch from this URL? Can I do this? And

**[28:21]** fetch from this URL? Can I do this? And

**[28:21]** fetch from this URL? Can I do this? And it kind of puts it into a sub agent. And

**[28:23]** it kind of puts it into a sub agent. And

**[28:24]** it kind of puts it into a sub agent. And uh, yeah, most of the most of the

**[28:26]** uh, yeah, most of the most of the

**[28:26]** uh, yeah, most of the most of the complex code here is in this sandboxing

**[28:29]** complex code here is in this sandboxing

**[28:29]** complex code here is in this sandboxing and permission set.

**[28:31]** and permission set.

**[28:31]** and permission set. I think there's this whole pipeline to

**[28:33]** I think there's this whole pipeline to

**[28:33]** I think there's this whole pipeline to gate bash command. So it depending on

**[28:37]** gate bash command. So it depending on

**[28:37]** gate bash command. So it depending on the prefix is how it goes through the

**[28:41]** the prefix is how it goes through the

**[28:41]** the prefix is how it goes through the sandboxing environment and a lot of the

**[28:43]** sandboxing environment and a lot of the

**[28:43]** sandboxing environment and a lot of the other models work differently here. Uh

**[28:45]** other models work differently here. Uh

**[28:45]** other models work differently here. Uh but this is how cloud code does it. I'll

**[28:46]** but this is how cloud code does it. I'll

**[28:46]** but this is how cloud code does it. I'll explain the other ones later at the end.

**[28:51]** explain the other ones later at the end.

**[28:51]** explain the other ones later at the end. The next topic uh of relevance here is

**[28:53]** The next topic uh of relevance here is

**[28:53]** The next topic uh of relevance here is sub aents. Uh so this is going back to

**[28:55]** sub aents. Uh so this is going back to

**[28:55]** sub aents. Uh so this is going back to context management and this this problem

**[28:57]** context management and this this problem

**[28:57]** context management and this this problem we keep going back to of the longer

**[28:59]** we keep going back to of the longer

**[28:59]** we keep going back to of the longer context the the stupider our agent is.


### [29:00 - 30:00]

**[29:02]** context the the stupider our agent is.

**[29:02]** context the the stupider our agent is. This is a this is an answer to it. So

**[29:04]** This is a this is an answer to it. So

**[29:04]** This is a this is an answer to it. So using sub aents for specific tasks and

**[29:07]** using sub aents for specific tasks and

**[29:07]** using sub aents for specific tasks and the key with the sub aent is it has its

**[29:09]** the key with the sub aent is it has its

**[29:09]** the key with the sub aent is it has its own context and it feeds back only the

**[29:11]** own context and it feeds back only the

**[29:12]** own context and it feeds back only the results and this is how you don't

**[29:13]** results and this is how you don't

**[29:13]** results and this is how you don't clutter it. So we got the researcher

**[29:15]** clutter it. So we got the researcher

**[29:15]** clutter it. So we got the researcher these are just four examples researcher

**[29:17]** these are just four examples researcher

**[29:17]** these are just four examples researcher docs reader testr runner code reviewer

**[29:20]** docs reader testr runner code reviewer

**[29:20]** docs reader testr runner code reviewer in that example I was talking about

**[29:21]** in that example I was talking about

**[29:21]** in that example I was talking about earlier when I added all the tags to our

**[29:24]** earlier when I added all the tags to our

**[29:24]** earlier when I added all the tags to our website to let the agent do it better. I

**[29:27]** website to let the agent do it better. I

**[29:27]** website to let the agent do it better. I obviously I use a coding agent to do

**[29:29]** obviously I use a coding agent to do

**[29:29]** obviously I use a coding agent to do that and I said read our docs first and

**[29:31]** that and I said read our docs first and

**[29:31]** that and I said read our docs first and then do it and it's going to do this in

**[29:33]** then do it and it's going to do this in

**[29:33]** then do it and it's going to do this in a sub agent. It's going to feed back the

**[29:35]** a sub agent. It's going to feed back the

**[29:35]** a sub agent. It's going to feed back the information and the the key thing here

**[29:38]** information and the the key thing here

**[29:38]** information and the the key thing here is the forks of the agent and how we

**[29:40]** is the forks of the agent and how we

**[29:40]** is the forks of the agent and how we aggregate it back into our main context.

**[29:44]** aggregate it back into our main context.

**[29:44]** aggregate it back into our main context. So here's an example. I think this is

**[29:46]** So here's an example. I think this is

**[29:46]** So here's an example. I think this is actually very interesting. I want to

**[29:47]** actually very interesting. I want to

**[29:47]** actually very interesting. I want to call out a thing or two here. So task is

**[29:50]** call out a thing or two here. So task is

**[29:50]** call out a thing or two here. So task is what a sub aent is. We're giving task

**[29:53]** what a sub aent is. We're giving task

**[29:53]** what a sub aent is. We're giving task two things. Description and a prompt.

**[29:56]** two things. Description and a prompt.

**[29:56]** two things. Description and a prompt. The description is what the user is

**[29:58]** The description is what the user is

**[29:58]** The description is what the user is going to see. So you're going to say


### [30:00 - 31:00]

**[30:00]** going to see. So you're going to say

**[30:00]** going to see. So you're going to say task

**[30:01]** task

**[30:02]** task uh find default chat context

**[30:04]** uh find default chat context

**[30:04]** uh find default chat context instantiation or something. And then the

**[30:06]** instantiation or something. And then the

**[30:06]** instantiation or something. And then the prompt you're going to give a long

**[30:07]** prompt you're going to give a long

**[30:08]** prompt you're going to give a long string which is really interesting

**[30:09]** string which is really interesting

**[30:09]** string which is really interesting because now we have the coding agent

**[30:11]** because now we have the coding agent

**[30:11]** because now we have the coding agent prompting its own agents. And I've

**[30:14]** prompting its own agents. And I've

**[30:14]** prompting its own agents. And I've actually used this paradigm in agents

**[30:16]** actually used this paradigm in agents

**[30:16]** actually used this paradigm in agents I've built for our product. Uh if you

**[30:20]** I've built for our product. Uh if you

**[30:20]** I've built for our product. Uh if you can you can just have the agent stuff as

**[30:23]** can you can just have the agent stuff as

**[30:23]** can you can just have the agent stuff as much information as it wants in this

**[30:24]** much information as it wants in this

**[30:24]** much information as it wants in this string. And if we're going back to

**[30:26]** string. And if we're going back to

**[30:26]** string. And if we're going back to relying on the model if this task

**[30:28]** relying on the model if this task

**[30:28]** relying on the model if this task returns an error now stuff even more

**[30:31]** returns an error now stuff even more

**[30:31]** returns an error now stuff even more information and let it solve the

**[30:33]** information and let it solve the

**[30:33]** information and let it solve the problems. It's better to be flexible

**[30:35]** problems. It's better to be flexible

**[30:35]** problems. It's better to be flexible rather than rigid.

**[30:37]** rather than rigid.

**[30:37]** rather than rigid. If I was building this I would consider

**[30:39]** If I was building this I would consider

**[30:39]** If I was building this I would consider switching a string to maybe an object

**[30:41]** switching a string to maybe an object

**[30:41]** switching a string to maybe an object here uh depending on what you're

**[30:43]** here uh depending on what you're

**[30:43]** here uh depending on what you're building and maybe let it give actually

**[30:44]** building and maybe let it give actually

**[30:44]** building and maybe let it give actually more structured data. Yes. So I can see

**[30:48]** more structured data. Yes. So I can see

**[30:48]** more structured data. Yes. So I can see this prompt has quite a couple

**[30:49]** this prompt has quite a couple

**[30:49]** this prompt has quite a couple sentences. Is that in the main agent? Is

**[30:52]** sentences. Is that in the main agent? Is

**[30:52]** sentences. Is that in the main agent? Is that taking the context of the main

**[30:53]** that taking the context of the main

**[30:54]** that taking the context of the main agent or is there some sort of

**[30:55]** agent or is there some sort of

**[30:56]** agent or is there some sort of intermediate step where the sub agent

**[30:58]** intermediate step where the sub agent

**[30:58]** intermediate step where the sub agent double reads over you know like what the


### [31:00 - 32:00]

**[31:01]** double reads over you know like what the

**[31:01]** double reads over you know like what the main agent is doing and then generates

**[31:06]** main agent is doing and then generates

**[31:06]** main agent is doing and then generates >> right? So the question is does the task

**[31:09]** >> right? So the question is does the task

**[31:09]** >> right? So the question is does the task just get the prompt here or does it also

**[31:11]** just get the prompt here or does it also

**[31:12]** just get the prompt here or does it also get your chat history? Is that the

**[31:13]** get your chat history? Is that the

**[31:13]** get your chat history? Is that the question?

**[31:15]** question?

**[31:15]** question? The question is is are all of the I have

**[31:18]** The question is is are all of the I have

**[31:18]** The question is is are all of the I have my main agent. Is all of this in the

**[31:20]** my main agent. Is all of this in the

**[31:20]** my main agent. Is all of this in the system prompt of the main agent to

**[31:22]** system prompt of the main agent to

**[31:22]** system prompt of the main agent to inform how that prompts the sub agent?

**[31:24]** inform how that prompts the sub agent?

**[31:24]** inform how that prompts the sub agent? >> No. No. Like it's not in the system.

**[31:27]** >> No. No. Like it's not in the system.

**[31:27]** >> No. No. Like it's not in the system. It's in the whole context. Is the all of

**[31:29]** It's in the whole context. Is the all of

**[31:29]** It's in the whole context. Is the all of this context of the main agent

**[31:33]** this context of the main agent

**[31:33]** this context of the main agent >> the task it calls or or you're saying

**[31:36]** >> the task it calls or or you're saying

**[31:36]** >> the task it calls or or you're saying the structure for the task

**[31:37]** the structure for the task

**[31:37]** the structure for the task >> this whole JSON right or

**[31:39]** >> this whole JSON right or

**[31:39]** >> this whole JSON right or >> yes. So this is a tool call. So the tool

**[31:42]** >> yes. So this is a tool call. So the tool

**[31:42]** >> yes. So this is a tool call. So the tool called structure of what a task is is in

**[31:45]** called structure of what a task is is in

**[31:45]** called structure of what a task is is in the maiden agent. Uh and then these are

**[31:48]** the maiden agent. Uh and then these are

**[31:48]** the maiden agent. Uh and then these are generated on the fly. Uh so as you want

**[31:50]** generated on the fly. Uh so as you want

**[31:50]** generated on the fly. Uh so as you want to run a task, it's generating the

**[31:51]** to run a task, it's generating the

**[31:52]** to run a task, it's generating the description and the prompt. Task is a

**[31:55]** description and the prompt. Task is a

**[31:55]** description and the prompt. Task is a tool call. They could be run in parallel

**[31:56]** tool call. They could be run in parallel

**[31:56]** tool call. They could be run in parallel and then they're returning the results

**[31:58]** and then they're returning the results

**[31:58]** and then they're returning the results of it. Hopefully that helps.


### [32:00 - 33:00]

**[32:03]** of it. Hopefully that helps.

**[32:03]** of it. Hopefully that helps. Um so we could go back to the system

**[32:07]** Um so we could go back to the system

**[32:07]** Um so we could go back to the system prompt. So there's some leaks of the

**[32:09]** prompt. So there's some leaks of the

**[32:09]** prompt. So there's some leaks of the cloud code system prompt. So that's what

**[32:10]** cloud code system prompt. So that's what

**[32:10]** cloud code system prompt. So that's what I'm basing this on. Uh you can find it

**[32:13]** I'm basing this on. Uh you can find it

**[32:13]** I'm basing this on. Uh you can find it online. Um here are some things I I

**[32:16]** online. Um here are some things I I

**[32:16]** online. Um here are some things I I noted from it. Uh concise outputs. Uh

**[32:20]** noted from it. Uh concise outputs. Uh

**[32:20]** noted from it. Uh concise outputs. Uh obviously don't give anything too long.

**[32:23]** obviously don't give anything too long.

**[32:23]** obviously don't give anything too long. No here is or I will just do the do the

**[32:26]** No here is or I will just do the do the

**[32:26]** No here is or I will just do the do the task the user wants. Uh kind of pushing

**[32:29]** task the user wants. Uh kind of pushing

**[32:29]** task the user wants. Uh kind of pushing it to use tools more more instead of

**[32:31]** it to use tools more more instead of

**[32:31]** it to use tools more more instead of text explanations. Obviously, I think

**[32:34]** text explanations. Obviously, I think

**[32:34]** text explanations. Obviously, I think when we we've all built coding agents

**[32:36]** when we we've all built coding agents

**[32:36]** when we we've all built coding agents and when we do it, it usually says,

**[32:38]** and when we do it, it usually says,

**[32:38]** and when we do it, it usually says, "Hey, I want to run this SQL." No, push

**[32:40]** "Hey, I want to run this SQL." No, push

**[32:40]** "Hey, I want to run this SQL." No, push it to use the tool. Um,

**[32:44]** it to use the tool. Um,

**[32:44]** it to use the tool. Um, matching the existing code, not adding

**[32:46]** matching the existing code, not adding

**[32:46]** matching the existing code, not adding comments. This one does not work for me,

**[32:48]** comments. This one does not work for me,

**[32:48]** comments. This one does not work for me, but uh running commands in parallel

**[32:51]** but uh running commands in parallel

**[32:51]** but uh running commands in parallel extensively and then the to-dos and

**[32:53]** extensively and then the to-dos and

**[32:53]** extensively and then the to-dos and stuff like that. There's a lot that you

**[32:55]** stuff like that. There's a lot that you

**[32:55]** stuff like that. There's a lot that you can nudge it to do with the system

**[32:57]** can nudge it to do with the system

**[32:57]** can nudge it to do with the system prompts. But as you see, I think there's

**[32:59]** prompts. But as you see, I think there's

**[32:59]** prompts. But as you see, I think there's a really interesting point to the


### [33:00 - 34:00]

**[33:01]** a really interesting point to the

**[33:01]** a really interesting point to the earlier question you had about where

**[33:04]** earlier question you had about where

**[33:04]** earlier question you had about where what's the trade-off between DAGs and

**[33:06]** what's the trade-off between DAGs and

**[33:06]** what's the trade-off between DAGs and loops.

**[33:08]** loops.

**[33:08]** loops. A lot of these things you could see are

**[33:11]** A lot of these things you could see are

**[33:11]** A lot of these things you could see are feel like they came from someone using

**[33:13]** feel like they came from someone using

**[33:13]** feel like they came from someone using it clawed code and saying, "Oh, if only

**[33:16]** it clawed code and saying, "Oh, if only

**[33:16]** it clawed code and saying, "Oh, if only it did this a little less or if it did

**[33:17]** it did this a little less or if it did

**[33:17]** it did this a little less or if it did this a little bit more." That's where

**[33:20]** this a little bit more." That's where

**[33:20]** this a little bit more." That's where prompting comes in because it's so easy

**[33:21]** prompting comes in because it's so easy

**[33:21]** prompting comes in because it's so easy to iterate and it's not you're not it's

**[33:24]** to iterate and it's not you're not it's

**[33:24]** to iterate and it's not you're not it's not a hard requirement but if only it

**[33:27]** not a hard requirement but if only it

**[33:27]** not a hard requirement but if only it said here is a little bit more. It's

**[33:28]** said here is a little bit more. It's

**[33:28]** said here is a little bit more. It's okay to say it sometimes but

**[33:31]** okay to say it sometimes but

**[33:32]** okay to say it sometimes but all right skills. Skills is great. It's

**[33:34]** all right skills. Skills is great. It's

**[33:34]** all right skills. Skills is great. It's a slightly newer. I've I honestly got

**[33:37]** a slightly newer. I've I honestly got

**[33:37]** a slightly newer. I've I honestly got convinced of it only recently. So good.

**[33:39]** convinced of it only recently. So good.

**[33:39]** convinced of it only recently. So good. I built these slides with skills. uh

**[33:41]** I built these slides with skills. uh

**[33:42]** I built these slides with skills. uh it's basically I think in the context of

**[33:44]** it's basically I think in the context of

**[33:44]** it's basically I think in the context of this talk about architecture, let's

**[33:46]** this talk about architecture, let's

**[33:46]** this talk about architecture, let's think of it as a extendable system

**[33:49]** think of it as a extendable system

**[33:49]** think of it as a extendable system prompt. So in the same way that we don't

**[33:52]** prompt. So in the same way that we don't

**[33:52]** prompt. So in the same way that we don't want to clutter the context, there's a

**[33:53]** want to clutter the context, there's a

**[33:54]** want to clutter the context, there's a lot of different type of tasks you're

**[33:55]** lot of different type of tasks you're

**[33:55]** lot of different type of tasks you're going to need to do where you want a lot

**[33:58]** going to need to do where you want a lot

**[33:58]** going to need to do where you want a lot more context. So this is how we give


### [34:00 - 35:00]

**[34:00]** more context. So this is how we give

**[34:00]** more context. So this is how we give cloud code a few options of how it could

**[34:02]** cloud code a few options of how it could

**[34:02]** cloud code a few options of how it could tap into more information. Here are some

**[34:05]** tap into more information. Here are some

**[34:05]** tap into more information. Here are some examples. Uh, I use this for I have a

**[34:09]** examples. Uh, I use this for I have a

**[34:09]** examples. Uh, I use this for I have a skill for docs updates to tell it my

**[34:11]** skill for docs updates to tell it my

**[34:11]** skill for docs updates to tell it my writing style and and my product. So, if

**[34:14]** writing style and and my product. So, if

**[34:14]** writing style and and my product. So, if I want to do a docs update, I say use

**[34:16]** I want to do a docs update, I say use

**[34:16]** I want to do a docs update, I say use that skill. Load in that skill. Uh,

**[34:18]** that skill. Load in that skill. Uh,

**[34:18]** that skill. Load in that skill. Uh, editing Microsoft Office uh Microsoft do

**[34:22]** editing Microsoft Office uh Microsoft do

**[34:22]** editing Microsoft Office uh Microsoft do Microsoft Word and Excel. Um, I I don't

**[34:25]** Microsoft Word and Excel. Um, I I don't

**[34:25]** Microsoft Word and Excel. Um, I I don't use this, but I've seen a lot of people

**[34:27]** use this, but I've seen a lot of people

**[34:27]** use this, but I've seen a lot of people using it. It kind of like decompiles the

**[34:29]** using it. It kind of like decompiles the

**[34:29]** using it. It kind of like decompiles the f it's really cool. Uh, but it lets

**[34:31]** f it's really cool. Uh, but it lets

**[34:31]** f it's really cool. Uh, but it lets cloud code do this design style guide.

**[34:34]** cloud code do this design style guide.

**[34:34]** cloud code do this design style guide. This is a common one. Deep research. I

**[34:36]** This is a common one. Deep research. I

**[34:36]** This is a common one. Deep research. I the other day I threw in a like article

**[34:40]** the other day I threw in a like article

**[34:40]** the other day I threw in a like article or GitHub uh repo on how deep research

**[34:42]** or GitHub uh repo on how deep research

**[34:42]** or GitHub uh repo on how deep research works and I said rebuild this as a cloud

**[34:44]** works and I said rebuild this as a cloud

**[34:44]** works and I said rebuild this as a cloud code skill works so well it's amazing.

**[34:49]** code skill works so well it's amazing.

**[34:49]** code skill works so well it's amazing. So unified diffing I think this is worth

**[34:50]** So unified diffing I think this is worth

**[34:50]** So unified diffing I think this is worth its own slide. Uh it's very obvious

**[34:53]** its own slide. Uh it's very obvious

**[34:53]** its own slide. Uh it's very obvious probably not too much we need to talk

**[34:55]** probably not too much we need to talk

**[34:55]** probably not too much we need to talk about here but

**[34:57]** about here but

**[34:57]** about here but it makes this so much better and it


### [35:00 - 36:00]

**[35:00]** it makes this so much better and it

**[35:00]** it makes this so much better and it makes the token limit shorter. It makes

**[35:03]** makes the token limit shorter. It makes

**[35:03]** makes the token limit shorter. It makes it faster and makes it less prone to

**[35:05]** it faster and makes it less prone to

**[35:05]** it faster and makes it less prone to mistakes like I gave with that example

**[35:07]** mistakes like I gave with that example

**[35:07]** mistakes like I gave with that example when you rewrite an essay versus marking

**[35:10]** when you rewrite an essay versus marking

**[35:10]** when you rewrite an essay versus marking it with a red line. It's just better. I

**[35:12]** it with a red line. It's just better. I

**[35:12]** it with a red line. It's just better. I highly recommend using diffing in any

**[35:15]** highly recommend using diffing in any

**[35:15]** highly recommend using diffing in any agents you're doing. Unified diff is a

**[35:17]** agents you're doing. Unified diff is a

**[35:17]** agents you're doing. Unified diff is a standard. When I looked into a lot of

**[35:18]** standard. When I looked into a lot of

**[35:18]** standard. When I looked into a lot of these coding agents, some actually built

**[35:20]** these coding agents, some actually built

**[35:20]** these coding agents, some actually built their own kind of standard uh and like

**[35:24]** their own kind of standard uh and like

**[35:24]** their own kind of standard uh and like with slight variations on unified diff

**[35:26]** with slight variations on unified diff

**[35:26]** with slight variations on unified diff because you don't always need the line

**[35:27]** because you don't always need the line

**[35:27]** because you don't always need the line numbers and but unified diff works. You

**[35:31]** numbers and but unified diff works. You

**[35:31]** numbers and but unified diff works. You had a question

**[35:32]** had a question

**[35:32]** had a question >> to go back to skills.

**[35:35]** >> to go back to skills.

**[35:35]** >> to go back to skills. I are uh I don't know if anyone's seen

**[35:38]** I are uh I don't know if anyone's seen

**[35:38]** I are uh I don't know if anyone's seen the cloud the cloud code warns you and

**[35:40]** the cloud the cloud code warns you and

**[35:40]** the cloud the cloud code warns you and in yellow text if your quad indeed is

**[35:42]** in yellow text if your quad indeed is

**[35:42]** in yellow text if your quad indeed is like greater than 40k characters and so

**[35:44]** like greater than 40k characters and so

**[35:44]** like greater than 40k characters and so I was like okay I'm up. Let me

**[35:46]** I was like okay I'm up. Let me

**[35:46]** I was like okay I'm up. Let me break this down into skills. So I bet

**[35:48]** break this down into skills. So I bet

**[35:48]** break this down into skills. So I bet spent some time and then Claude ignored

**[35:51]** spent some time and then Claude ignored

**[35:51]** spent some time and then Claude ignored all of my skills and so I put them in

**[35:53]** all of my skills and so I put them in

**[35:53]** all of my skills and so I put them in some. So what am I? I don't know. Skills

**[35:56]** some. So what am I? I don't know. Skills

**[35:56]** some. So what am I? I don't know. Skills [clears throat] feel globally

**[35:59]** [clears throat] feel globally

**[35:59]** [clears throat] feel globally misunderstood or like not I don't know


### [36:00 - 37:00]

**[36:01]** misunderstood or like not I don't know

**[36:01]** misunderstood or like not I don't know I'm missing something. Help me

**[36:03]** I'm missing something. Help me

**[36:03]** I'm missing something. Help me understand. [laughter]

**[36:06]** understand. [laughter]

**[36:06]** understand. [laughter] >> Yeah. So the the question was on okay so

**[36:09]** >> Yeah. So the the question was on okay so

**[36:10]** >> Yeah. So the the question was on okay so cloud code system cloud MD it tells you

**[36:12]** cloud code system cloud MD it tells you

**[36:12]** cloud code system cloud MD it tells you when it's too long. So uh you move it

**[36:15]** when it's too long. So uh you move it

**[36:16]** when it's too long. So uh you move it into skills and then it's not

**[36:17]** into skills and then it's not

**[36:17]** into skills and then it's not recognizing the skills and not picking

**[36:18]** recognizing the skills and not picking

**[36:18]** recognizing the skills and not picking it up when it's needed.

**[36:21]** it up when it's needed.

**[36:21]** it up when it's needed. >> Yeah.

**[36:22]** >> Yeah.

**[36:22]** >> Yeah. take that up with the anthropic team I'd

**[36:24]** take that up with the anthropic team I'd

**[36:24]** take that up with the anthropic team I'd say. Uh but that's also a good example

**[36:27]** say. Uh but that's also a good example

**[36:27]** say. Uh but that's also a good example of maybe the system prompt

**[36:29]** of maybe the system prompt

**[36:29]** of maybe the system prompt >> that was the intention like skills you

**[36:31]** >> that was the intention like skills you

**[36:31]** >> that was the intention like skills you need to invoke them and like the agent

**[36:34]** need to invoke them and like the agent

**[36:34]** need to invoke them and like the agent itself shouldn't like just call them all

**[36:38]** itself shouldn't like just call them all

**[36:38]** itself shouldn't like just call them all the time,

**[36:39]** the time,

**[36:39]** the time, >> right? It does give a dis description of

**[36:42]** >> right? It does give a dis description of

**[36:42]** >> right? It does give a dis description of each skill to the model or it should uh

**[36:46]** each skill to the model or it should uh

**[36:46]** each skill to the model or it should uh tell it okay here's like a oneliner

**[36:48]** tell it okay here's like a oneliner

**[36:48]** tell it okay here's like a oneliner about each skill. So theoretically in a

**[36:50]** about each skill. So theoretically in a

**[36:50]** about each skill. So theoretically in a perfect world it would pick up all the

**[36:51]** perfect world it would pick up all the

**[36:51]** perfect world it would pick up all the skills all the time. But you're right, I

**[36:53]** skills all the time. But you're right, I

**[36:53]** skills all the time. But you're right, I generally have to call the skill myself

**[36:54]** generally have to call the skill myself

**[36:54]** generally have to call the skill myself manually. I but I think this is a good

**[36:58]** manually. I but I think this is a good

**[36:58]** manually. I but I think this is a good tieback into when is prompting the right


### [37:00 - 38:00]

**[37:01]** tieback into when is prompting the right

**[37:01]** tieback into when is prompting the right solution or when is the DAG the right

**[37:04]** solution or when is the DAG the right

**[37:04]** solution or when is the DAG the right solution or maybe this is a model

**[37:06]** solution or maybe this is a model

**[37:06]** solution or maybe this is a model training problem. Maybe they need to do

**[37:08]** training problem. Maybe they need to do

**[37:08]** training problem. Maybe they need to do a little bit more in post-raining of

**[37:11]** a little bit more in post-raining of

**[37:11]** a little bit more in post-raining of getting the model to call the skills is

**[37:15]** getting the model to call the skills is

**[37:15]** getting the model to call the skills is almost like calling a tool call. You

**[37:17]** almost like calling a tool call. You

**[37:17]** almost like calling a tool call. You have to know when to call it. So maybe

**[37:19]** have to know when to call it. So maybe

**[37:19]** have to know when to call it. So maybe this is just uh a functionality that's

**[37:21]** this is just uh a functionality that's

**[37:21]** this is just uh a functionality that's not that good yet, but I think the

**[37:22]** not that good yet, but I think the

**[37:22]** not that good yet, but I think the paradigm is very interesting, but it's

**[37:24]** paradigm is very interesting, but it's

**[37:24]** paradigm is very interesting, but it's not perfect as we're learning.

**[37:28]** not perfect as we're learning.

**[37:28]** not perfect as we're learning. So diffing we just talked about what's

**[37:31]** So diffing we just talked about what's

**[37:31]** So diffing we just talked about what's next. So this is more opinion based, but

**[37:34]** next. So this is more opinion based, but

**[37:34]** next. So this is more opinion based, but where I see these things going and where

**[37:35]** where I see these things going and where

**[37:35]** where I see these things going and where the next kind of innovations might

**[37:37]** the next kind of innovations might

**[37:37]** the next kind of innovations might likely be. So

**[37:41]** likely be. So

**[37:41]** likely be. So I I think there's two schools of

**[37:43]** I I think there's two schools of

**[37:43]** I I think there's two schools of thoughts here. A lot of people think

**[37:45]** thoughts here. A lot of people think

**[37:45]** thoughts here. A lot of people think we're going to have one master loop with

**[37:46]** we're going to have one master loop with

**[37:46]** we're going to have one master loop with hundreds of tool calls and just tool

**[37:48]** hundreds of tool calls and just tool

**[37:48]** hundreds of tool calls and just tool calling is going to get much better.

**[37:50]** calling is going to get much better.

**[37:50]** calling is going to get much better. That's highly likely. Uh I take the

**[37:53]** That's highly likely. Uh I take the

**[37:53]** That's highly likely. Uh I take the alternate view which I think we need to

**[37:56]** alternate view which I think we need to

**[37:56]** alternate view which I think we need to reduce the tool calls as much as

**[37:58]** reduce the tool calls as much as

**[37:58]** reduce the tool calls as much as possible and just go back to just bash


### [38:00 - 39:00]

**[38:00]** possible and just go back to just bash

**[38:00]** possible and just go back to just bash and maybe even put scripts in the local

**[38:03]** and maybe even put scripts in the local

**[38:03]** and maybe even put scripts in the local directory. I think I am on the proponent

**[38:05]** directory. I think I am on the proponent

**[38:06]** directory. I think I am on the proponent of one mega tool call instead of a lot

**[38:08]** of one mega tool call instead of a lot

**[38:08]** of one mega tool call instead of a lot of tool calls. Maybe not actually one. I

**[38:10]** of tool calls. Maybe not actually one. I

**[38:10]** of tool calls. Maybe not actually one. I actually think that slide I showed you

**[38:12]** actually think that slide I showed you

**[38:12]** actually think that slide I showed you before is probably a good list, but a

**[38:15]** before is probably a good list, but a

**[38:15]** before is probably a good list, but a lot of people think we need hundreds of

**[38:17]** lot of people think we need hundreds of

**[38:17]** lot of people think we need hundreds of tool calls. I just don't think it's

**[38:18]** tool calls. I just don't think it's

**[38:18]** tool calls. I just don't think it's going there. Adaptive budgets, uh,

**[38:21]** going there. Adaptive budgets, uh,

**[38:21]** going there. Adaptive budgets, uh, adjusting reasoning, we do this a little

**[38:23]** adjusting reasoning, we do this a little

**[38:23]** adjusting reasoning, we do this a little bit, uh, the thinking and ultra think

**[38:25]** bit, uh, the thinking and ultra think

**[38:25]** bit, uh, the thinking and ultra think and stuff like that, but I I think

**[38:27]** and stuff like that, but I I think

**[38:28]** and stuff like that, but I I think reasoning models as a tool makes a lot

**[38:30]** reasoning models as a tool makes a lot

**[38:30]** reasoning models as a tool makes a lot of sense as a paradigm. Can you use I

**[38:33]** of sense as a paradigm. Can you use I

**[38:33]** of sense as a paradigm. Can you use I think a lot of us would make a trade-off

**[38:35]** think a lot of us would make a trade-off

**[38:35]** think a lot of us would make a trade-off of a 20 times quicker model with

**[38:38]** of a 20 times quicker model with

**[38:38]** of a 20 times quicker model with slightly stupider results and being able

**[38:40]** slightly stupider results and being able

**[38:40]** slightly stupider results and being able to call a tool call for a very good

**[38:43]** to call a tool call for a very good

**[38:43]** to call a tool call for a very good model. I think that's a trade-off we

**[38:44]** model. I think that's a trade-off we

**[38:44]** model. I think that's a trade-off we we'd make in a lot of cases. Maybe not

**[38:46]** we'd make in a lot of cases. Maybe not

**[38:46]** we'd make in a lot of cases. Maybe not our planner. Maybe we go to the planner

**[38:48]** our planner. Maybe we go to the planner

**[38:48]** our planner. Maybe we go to the planner first with GPD 51 codeex or opus or

**[38:51]** first with GPD 51 codeex or opus or

**[38:51]** first with GPD 51 codeex or opus or whatever if when the new opus comes out.

**[38:53]** whatever if when the new opus comes out.

**[38:53]** whatever if when the new opus comes out. Uh but

**[38:56]** Uh but

**[38:56]** Uh but I think I think there's a lot of uh mix

**[38:57]** I think I think there's a lot of uh mix

**[38:58]** I think I think there's a lot of uh mix and matching we can do and that's I

**[38:59]** and matching we can do and that's I

**[38:59]** and matching we can do and that's I think the next frontier and I think the


### [39:00 - 40:00]

**[39:01]** think the next frontier and I think the

**[39:01]** think the next frontier and I think the last frontier

**[39:03]** last frontier

**[39:03]** last frontier I think there's a lot we can learn from

**[39:04]** I think there's a lot we can learn from

**[39:04]** I think there's a lot we can learn from to-do lists and and new first class

**[39:07]** to-do lists and and new first class

**[39:07]** to-do lists and and new first class paradigms we can build skills is another

**[39:09]** paradigms we can build skills is another

**[39:09]** paradigms we can build skills is another example of a first class paradigm we can

**[39:11]** example of a first class paradigm we can

**[39:11]** example of a first class paradigm we can kind of try to build into it maybe it

**[39:13]** kind of try to build into it maybe it

**[39:13]** kind of try to build into it maybe it doesn't work perfectly uh but I think

**[39:15]** doesn't work perfectly uh but I think

**[39:15]** doesn't work perfectly uh but I think there's a I think there's a lot of new

**[39:16]** there's a I think there's a lot of new

**[39:16]** there's a I think there's a lot of new discoveries to be made there in my

**[39:18]** discoveries to be made there in my

**[39:18]** discoveries to be made there in my opinion do I have them I don't know uh

**[39:21]** opinion do I have them I don't know uh

**[39:21]** opinion do I have them I don't know uh so now I I want to for the for the

**[39:24]** so now I I want to for the for the

**[39:24]** so now I I want to for the for the latter part of this talk I want to talk

**[39:26]** latter part of this talk I want to talk

**[39:26]** latter part of this talk I want to talk about the other frontier agents and the

**[39:28]** about the other frontier agents and the

**[39:28]** about the other frontier agents and the other philosophies they've designed

**[39:30]** other philosophies they've designed

**[39:30]** other philosophies they've designed philosophies they've chosen and

**[39:34]** philosophies they've chosen and

**[39:34]** philosophies they've chosen and we all have the benefit we can mix and

**[39:36]** we all have the benefit we can mix and

**[39:36]** we all have the benefit we can mix and match when we were building our agent we

**[39:38]** match when we were building our agent we

**[39:38]** match when we were building our agent we could do whatever we want and learn from

**[39:39]** could do whatever we want and learn from

**[39:39]** could do whatever we want and learn from the best and the frontier labs are very

**[39:41]** the best and the frontier labs are very

**[39:41]** the best and the frontier labs are very good at this so

**[39:45]** good at this so

**[39:45]** good at this so uh something I like to go back to a lot

**[39:47]** uh something I like to go back to a lot

**[39:47]** uh something I like to go back to a lot I call it the AI therapist problem may

**[39:49]** I call it the AI therapist problem may

**[39:49]** I call it the AI therapist problem may maybe there's a better name to give it

**[39:51]** maybe there's a better name to give it

**[39:51]** maybe there's a better name to give it uh but I believe there's a lot of

**[39:54]** uh but I believe there's a lot of

**[39:54]** uh but I believe there's a lot of problems, the most interesting AI

**[39:55]** problems, the most interesting AI

**[39:55]** problems, the most interesting AI problems around. There isn't a global

**[39:57]** problems around. There isn't a global

**[39:58]** problems around. There isn't a global maximum. Meaning,


### [40:00 - 41:00]

**[40:00]** maximum. Meaning,

**[40:00]** maximum. Meaning, all right, we're in New York City. If I

**[40:02]** all right, we're in New York City. If I

**[40:02]** all right, we're in New York City. If I need to see a therapist, there's six on

**[40:04]** need to see a therapist, there's six on

**[40:04]** need to see a therapist, there's six on every block here. There's no global

**[40:06]** every block here. There's no global

**[40:06]** every block here. There's no global answer for what the best therapist is.

**[40:09]** answer for what the best therapist is.

**[40:09]** answer for what the best therapist is. There's different strategies. There's a

**[40:11]** There's different strategies. There's a

**[40:11]** There's different strategies. There's a therapist that does meditation or CBT or

**[40:14]** therapist that does meditation or CBT or

**[40:14]** therapist that does meditation or CBT or maybe one that gives you Iawaska. and

**[40:16]** maybe one that gives you Iawaska. and

**[40:16]** maybe one that gives you Iawaska. and and these are just kind of like

**[40:17]** and these are just kind of like

**[40:17]** and these are just kind of like different strategies for the same goal

**[40:20]** different strategies for the same goal

**[40:20]** different strategies for the same goal in the same way that if you're building

**[40:22]** in the same way that if you're building

**[40:22]** in the same way that if you're building an AI therapist, there isn't a global

**[40:24]** an AI therapist, there isn't a global

**[40:24]** an AI therapist, there isn't a global maxima. This is kind of my anti-AGI

**[40:27]** maxima. This is kind of my anti-AGI

**[40:27]** maxima. This is kind of my anti-AGI take, but this is also the take to say

**[40:29]** take, but this is also the take to say

**[40:29]** take, but this is also the take to say that when you're building these

**[40:31]** that when you're building these

**[40:31]** that when you're building these applications, taste comes into it a lot

**[40:33]** applications, taste comes into it a lot

**[40:33]** applications, taste comes into it a lot and design architecture matters a lot.

**[40:35]** and design architecture matters a lot.

**[40:35]** and design architecture matters a lot. You can have five different coding

**[40:37]** You can have five different coding

**[40:37]** You can have five different coding agents that are all amazing. Nobody

**[40:39]** agents that are all amazing. Nobody

**[40:39]** agents that are all amazing. Nobody knows which today. Nobody knows which

**[40:41]** knows which today. Nobody knows which

**[40:41]** knows which today. Nobody knows which one's best to be honest. I don't think

**[40:43]** one's best to be honest. I don't think

**[40:43]** one's best to be honest. I don't think Anthropic knows. I don't think OpenAI

**[40:44]** Anthropic knows. I don't think OpenAI

**[40:44]** Anthropic knows. I don't think OpenAI knows. I don't think source graph knows.

**[40:46]** knows. I don't think source graph knows.

**[40:46]** knows. I don't think source graph knows. Nobody knows whose has the best, but

**[40:48]** Nobody knows whose has the best, but

**[40:48]** Nobody knows whose has the best, but some are better at some things. I

**[40:50]** some are better at some things. I

**[40:50]** some are better at some things. I personally like claude code for I said

**[40:53]** personally like claude code for I said

**[40:53]** personally like claude code for I said like running my local environment or

**[40:55]** like running my local environment or

**[40:55]** like running my local environment or using git or using these kind of like

**[40:57]** using git or using these kind of like

**[40:57]** using git or using these kind of like human actions that require back and

**[40:59]** human actions that require back and

**[40:59]** human actions that require back and forth, but I go to codeex for the hard


### [41:00 - 42:00]

**[41:01]** forth, but I go to codeex for the hard

**[41:01]** forth, but I go to codeex for the hard problems or I go to composer from cursor

**[41:04]** problems or I go to composer from cursor

**[41:04]** problems or I go to composer from cursor because it's faster. And there's a lot

**[41:07]** because it's faster. And there's a lot

**[41:07]** because it's faster. And there's a lot basically all this to say there's value

**[41:09]** basically all this to say there's value

**[41:10]** basically all this to say there's value in having different philosophies here.

**[41:11]** in having different philosophies here.

**[41:11]** in having different philosophies here. And I don't think there's going to be

**[41:13]** And I don't think there's going to be

**[41:13]** And I don't think there's going to be one winner to this. I think there's

**[41:14]** one winner to this. I think there's

**[41:14]** one winner to this. I think there's going to be different winners for

**[41:15]** going to be different winners for

**[41:15]** going to be different winners for different use cases. And and this is not

**[41:18]** different use cases. And and this is not

**[41:18]** different use cases. And and this is not just coding agents, by the way. This is

**[41:19]** just coding agents, by the way. This is

**[41:19]** just coding agents, by the way. This is all AI products. This is this is kind of

**[41:21]** all AI products. This is this is kind of

**[41:21]** all AI products. This is this is kind of why our whole company focuses on domain

**[41:24]** why our whole company focuses on domain

**[41:24]** why our whole company focuses on domain experts and bringing in the PM and the

**[41:26]** experts and bringing in the PM and the

**[41:26]** experts and bringing in the PM and the the the subject matter expert into it

**[41:29]** the the subject matter expert into it

**[41:29]** the the subject matter expert into it because that's how you build

**[41:29]** because that's how you build

**[41:30]** because that's how you build defensibility.

**[41:31]** defensibility.

**[41:31]** defensibility. So here are the perspectives. The way I

**[41:33]** So here are the perspectives. The way I

**[41:33]** So here are the perspectives. The way I see it, this is not a complete list of

**[41:35]** see it, this is not a complete list of

**[41:35]** see it, this is not a complete list of coding agents, but these are the ones

**[41:37]** coding agents, but these are the ones

**[41:37]** coding agents, but these are the ones that I think are the most interesting.

**[41:39]** that I think are the most interesting.

**[41:39]** that I think are the most interesting. Cloud code I think I think to me it wins

**[41:42]** Cloud code I think I think to me it wins

**[41:42]** Cloud code I think I think to me it wins in user friendliness and simplicity. Uh

**[41:45]** in user friendliness and simplicity. Uh

**[41:45]** in user friendliness and simplicity. Uh like I said if I'm doing something that

**[41:46]** like I said if I'm doing something that

**[41:46]** like I said if I'm doing something that requires a lot of applications that git

**[41:49]** requires a lot of applications that git

**[41:49]** requires a lot of applications that git git's just the best example. If I want

**[41:51]** git's just the best example. If I want

**[41:51]** git's just the best example. If I want to make a PR I'm going to cloud codeex

**[41:54]** to make a PR I'm going to cloud codeex

**[41:54]** to make a PR I'm going to cloud codeex uh context it's really good at context

**[41:56]** uh context it's really good at context

**[41:56]** uh context it's really good at context management. Uh it feels powerful. Do I


### [42:00 - 43:00]

**[42:00]** management. Uh it feels powerful. Do I

**[42:00]** management. Uh it feels powerful. Do I have the evidence to show you that it's

**[42:01]** have the evidence to show you that it's

**[42:01]** have the evidence to show you that it's more powerful? Probably not. But uh it

**[42:03]** more powerful? Probably not. But uh it

**[42:03]** more powerful? Probably not. But uh it feels that way to me and the market feel

**[42:06]** feels that way to me and the market feel

**[42:06]** feels that way to me and the market feel there's a whole another conversation

**[42:08]** there's a whole another conversation

**[42:08]** there's a whole another conversation here to say the market knows best and

**[42:10]** here to say the market knows best and

**[42:10]** here to say the market knows best and what people talk about knows best but I

**[42:12]** what people talk about knows best but I

**[42:12]** what people talk about knows best but I don't know if they know either. Cursor

**[42:15]** don't know if they know either. Cursor

**[42:15]** don't know if they know either. Cursor IDE is kind of that perspective model

**[42:18]** IDE is kind of that perspective model

**[42:18]** IDE is kind of that perspective model agnostic. It's faster. Factory uh makes

**[42:21]** agnostic. It's faster. Factory uh makes

**[42:21]** agnostic. It's faster. Factory uh makes Droid uh great team. They were here too.

**[42:23]** Droid uh great team. They were here too.

**[42:23]** Droid uh great team. They were here too. Uh they have multiple they they really

**[42:26]** Uh they have multiple they they really

**[42:26]** Uh they have multiple they they really specialize these droid sub aents they

**[42:28]** specialize these droid sub aents they

**[42:28]** specialize these droid sub aents they have. So that's kind of their edge and

**[42:31]** have. So that's kind of their edge and

**[42:31]** have. So that's kind of their edge and that's maybe a DAG conversation too or

**[42:33]** that's maybe a DAG conversation too or

**[42:33]** that's maybe a DAG conversation too or maybe a model training uh cognition. Uh

**[42:36]** maybe a model training uh cognition. Uh

**[42:36]** maybe a model training uh cognition. Uh so Devon uh kind of this endto-end

**[42:38]** so Devon uh kind of this endto-end

**[42:38]** so Devon uh kind of this endto-end autonomy self-reflection AMP which I'll

**[42:41]** autonomy self-reflection AMP which I'll

**[42:41]** autonomy self-reflection AMP which I'll talk about more in a second. They have a

**[42:43]** talk about more in a second. They have a

**[42:43]** talk about more in a second. They have a lot of interesting perspectives and

**[42:44]** lot of interesting perspectives and

**[42:44]** lot of interesting perspectives and actually I find them very exciting these

**[42:46]** actually I find them very exciting these

**[42:46]** actually I find them very exciting these days free it's model agnostic uh and

**[42:50]** days free it's model agnostic uh and

**[42:50]** days free it's model agnostic uh and there's a lot of UX sugar for users and

**[42:52]** there's a lot of UX sugar for users and

**[42:52]** there's a lot of UX sugar for users and I actually I love their design their

**[42:54]** I actually I love their design their

**[42:54]** I actually I love their design their their talks at this this conference they

**[42:56]** their talks at this this conference they

**[42:56]** their talks at this this conference they they they have very very unique

**[42:57]** they they have very very unique

**[42:58]** they they have very very unique perspectives so let's start with codeex


### [43:00 - 44:00]

**[43:00]** perspectives so let's start with codeex

**[43:00]** perspectives so let's start with codeex because it's a popular one

**[43:03]** because it's a popular one

**[43:03]** because it's a popular one so it's pretty similar to cloud code uh

**[43:06]** so it's pretty similar to cloud code uh

**[43:06]** so it's pretty similar to cloud code uh same master while loop most of these do

**[43:09]** same master while loop most of these do

**[43:09]** same master while loop most of these do because that's just the winning

**[43:10]** because that's just the winning

**[43:10]** because that's just the winning architecture uh interesting ly rust

**[43:13]** architecture uh interesting ly rust

**[43:13]** architecture uh interesting ly rust core. Uh the cool thing is it's open

**[43:15]** core. Uh the cool thing is it's open

**[43:15]** core. Uh the cool thing is it's open source so you can actually use codeex to

**[43:17]** source so you can actually use codeex to

**[43:18]** source so you can actually use codeex to understand how codeex works which is

**[43:19]** understand how codeex works which is

**[43:19]** understand how codeex works which is kind of what I did. Um it's a little

**[43:22]** kind of what I did. Um it's a little

**[43:22]** kind of what I did. Um it's a little more event driven a little more uh work

**[43:25]** more event driven a little more uh work

**[43:25]** more event driven a little more uh work went into concurrent threading here uh

**[43:27]** went into concurrent threading here uh

**[43:27]** went into concurrent threading here uh kind of submission cues event outputs

**[43:30]** kind of submission cues event outputs

**[43:30]** kind of submission cues event outputs kind of the the thing I was talking

**[43:32]** kind of the the thing I was talking

**[43:32]** kind of the the thing I was talking about with the IO buffer in cloud code.

**[43:36]** about with the IO buffer in cloud code.

**[43:36]** about with the IO buffer in cloud code. I think they do it a little bit

**[43:38]** I think they do it a little bit

**[43:38]** I think they do it a little bit differently. Uh sandboxing is very

**[43:40]** differently. Uh sandboxing is very

**[43:40]** differently. Uh sandboxing is very different. So theirs is more you I mean

**[43:44]** different. So theirs is more you I mean

**[43:44]** different. So theirs is more you I mean you could see here Mac OS seat belt and

**[43:46]** you could see here Mac OS seat belt and

**[43:46]** you could see here Mac OS seat belt and Linux land theirs is more kernel based

**[43:48]** Linux land theirs is more kernel based

**[43:48]** Linux land theirs is more kernel based uh and then state kind of this it's all

**[43:52]** uh and then state kind of this it's all

**[43:52]** uh and then state kind of this it's all under threading and and permissions is

**[43:55]** under threading and and permissions is

**[43:55]** under threading and and permissions is how I'd say it's mostly different and

**[43:56]** how I'd say it's mostly different and

**[43:56]** how I'd say it's mostly different and then the real difference is the model to


### [44:00 - 45:00]

**[44:00]** then the real difference is the model to

**[44:00]** then the real difference is the model to be honest. Uh so this is a this is

**[44:04]** be honest. Uh so this is a this is

**[44:04]** be honest. Uh so this is a this is actually me using cloud code to

**[44:06]** actually me using cloud code to

**[44:06]** actually me using cloud code to understand how codeex works. Uh so you

**[44:09]** understand how codeex works. Uh so you

**[44:09]** understand how codeex works. Uh so you see we have a few explore. I didn't talk

**[44:11]** see we have a few explore. I didn't talk

**[44:11]** see we have a few explore. I didn't talk about explore but uh it's uh it's a it's

**[44:14]** about explore but uh it's uh it's a it's

**[44:14]** about explore but uh it's uh it's a it's another sub agent type as as I as I

**[44:17]** another sub agent type as as I as I

**[44:17]** another sub agent type as as I as I mentioned these go in and out. Uh but

**[44:18]** mentioned these go in and out. Uh but

**[44:18]** mentioned these go in and out. Uh but yeah this is researching codecs with

**[44:20]** yeah this is researching codecs with

**[44:20]** yeah this is researching codecs with cloud code. It's always a fun thing to

**[44:22]** cloud code. It's always a fun thing to

**[44:22]** cloud code. It's always a fun thing to do. So let's talk about AMP.

**[44:25]** do. So let's talk about AMP.

**[44:25]** do. So let's talk about AMP. So this is source graphs coding agent.

**[44:28]** So this is source graphs coding agent.

**[44:28]** So this is source graphs coding agent. I it has a free tier. That's just a cool

**[44:31]** I it has a free tier. That's just a cool

**[44:31]** I it has a free tier. That's just a cool perspective in my opinion. Uh they

**[44:33]** perspective in my opinion. Uh they

**[44:33]** perspective in my opinion. Uh they leverage kind of these excess tokens uh

**[44:36]** leverage kind of these excess tokens uh

**[44:36]** leverage kind of these excess tokens uh from providers and they give ads. So, we

**[44:37]** from providers and they give ads. So, we

**[44:37]** from providers and they give ads. So, we actually have an ad on them. I think

**[44:39]** actually have an ad on them. I think

**[44:39]** actually have an ad on them. I think it's a cool I'm pro-AD. A lot of people

**[44:41]** it's a cool I'm pro-AD. A lot of people

**[44:41]** it's a cool I'm pro-AD. A lot of people are anti- ad. I think it's one of my hot

**[44:43]** are anti- ad. I think it's one of my hot

**[44:43]** are anti- ad. I think it's one of my hot takes, but I like it. They don't have a

**[44:45]** takes, but I like it. They don't have a

**[44:45]** takes, but I like it. They don't have a model selector. This is very

**[44:47]** model selector. This is very

**[44:47]** model selector. This is very interesting, too. This is its own

**[44:49]** interesting, too. This is its own

**[44:49]** interesting, too. This is its own perspective. Uh, it actually helps them

**[44:50]** perspective. Uh, it actually helps them

**[44:50]** perspective. Uh, it actually helps them move faster because you're you have less

**[44:54]** move faster because you're you have less

**[44:54]** move faster because you're you have less of an exact expectation of what the

**[44:56]** of an exact expectation of what the

**[44:56]** of an exact expectation of what the output is because, you know, they might

**[44:58]** output is because, you know, they might

**[44:58]** output is because, you know, they might be switching models here and there. So,


### [45:00 - 46:00]

**[45:00]** be switching models here and there. So,

**[45:00]** be switching models here and there. So, that changes how they develop. And then,

**[45:03]** that changes how they develop. And then,

**[45:03]** that changes how they develop. And then, uh, I think their vision is pretty

**[45:05]** uh, I think their vision is pretty

**[45:05]** uh, I think their vision is pretty interesting.

**[45:07]** interesting.

**[45:07]** interesting. uh their vision is how do we build not

**[45:12]** uh their vision is how do we build not

**[45:12]** uh their vision is how do we build not just the best agent but how do we build

**[45:14]** just the best agent but how do we build

**[45:14]** just the best agent but how do we build the agent that works with the most

**[45:16]** the agent that works with the most

**[45:16]** the agent that works with the most agentfriendly environments and actually

**[45:18]** agentfriendly environments and actually

**[45:18]** agentfriendly environments and actually factory gave a talk similar to this as

**[45:20]** factory gave a talk similar to this as

**[45:20]** factory gave a talk similar to this as well but how do how do you build a

**[45:22]** well but how do how do you build a

**[45:22]** well but how do how do you build a hermetically sealed uh a like coding

**[45:26]** hermetically sealed uh a like coding

**[45:26]** hermetically sealed uh a like coding repo that the agent can run tests on how

**[45:28]** repo that the agent can run tests on how

**[45:28]** repo that the agent can run tests on how do you build the feedback loop because

**[45:29]** do you build the feedback loop because

**[45:29]** do you build the feedback loop because that's kind of the holy grail that's how

**[45:31]** that's kind of the holy grail that's how

**[45:31]** that's kind of the holy grail that's how we build an autonomous agent and how do

**[45:33]** we build an autonomous agent and how do

**[45:33]** we build an autonomous agent and how do we uh I'd love to see the front-end

**[45:35]** we uh I'd love to see the front-end

**[45:35]** we uh I'd love to see the front-end version of this how do let it look at

**[45:37]** version of this how do let it look at

**[45:37]** version of this how do let it look at its own design and make it better and go

**[45:39]** its own design and make it better and go

**[45:39]** its own design and make it better and go back and forth and this is kind of their

**[45:41]** back and forth and this is kind of their

**[45:41]** back and forth and this is kind of their guiding philosophy and you could boil it

**[45:43]** guiding philosophy and you could boil it

**[45:43]** guiding philosophy and you could boil it down to the agent perspective as I've

**[45:45]** down to the agent perspective as I've

**[45:46]** down to the agent perspective as I've been calling it.

**[45:47]** been calling it.

**[45:47]** been calling it. I think they do interesting stuff with

**[45:49]** I think they do interesting stuff with

**[45:49]** I think they do interesting stuff with context. So, we're all familiar with

**[45:52]** context. So, we're all familiar with

**[45:52]** context. So, we're all familiar with compact. It's the worst. You have to

**[45:54]** compact. It's the worst. You have to

**[45:54]** compact. It's the worst. You have to wait 10. I don't know why it takes so

**[45:55]** wait 10. I don't know why it takes so

**[45:55]** wait 10. I don't know why it takes so long. Uh and if you're not familiar,

**[45:58]** long. Uh and if you're not familiar,

**[45:58]** long. Uh and if you're not familiar, it's summarizing your chat window when

**[45:59]** it's summarizing your chat window when

**[45:59]** it's summarizing your chat window when the context gets too high and giving the


### [46:00 - 47:00]

**[46:01]** the context gets too high and giving the

**[46:01]** the context gets too high and giving the summary. So, they have something called

**[46:03]** summary. So, they have something called

**[46:03]** summary. So, they have something called handoff, which makes me think of if you

**[46:05]** handoff, which makes me think of if you

**[46:05]** handoff, which makes me think of if you any was a anyone was a Call of Duty

**[46:07]** any was a anyone was a Call of Duty

**[46:07]** any was a anyone was a Call of Duty player back in the day, switch weapons.

**[46:09]** player back in the day, switch weapons.

**[46:10]** player back in the day, switch weapons. It's faster than reloading. And uh

**[46:12]** It's faster than reloading. And uh

**[46:12]** It's faster than reloading. And uh that's what handoff is. You're you're

**[46:13]** that's what handoff is. You're you're

**[46:14]** that's what handoff is. You're you're just starting a new thread and you're

**[46:15]** just starting a new thread and you're

**[46:15]** just starting a new thread and you're giving it the information it needs for a

**[46:16]** giving it the information it needs for a

**[46:16]** giving it the information it needs for a new thread. That feels like the winning

**[46:19]** new thread. That feels like the winning

**[46:19]** new thread. That feels like the winning strategy to me. Could be wrong, but

**[46:21]** strategy to me. Could be wrong, but

**[46:21]** strategy to me. Could be wrong, but maybe you need both. That's where

**[46:23]** maybe you need both. That's where

**[46:23]** maybe you need both. That's where they're pushing it. And I kind of like

**[46:25]** they're pushing it. And I kind of like

**[46:25]** they're pushing it. And I kind of like that. I They get they give a very fresh

**[46:27]** that. I They get they give a very fresh

**[46:27]** that. I They get they give a very fresh perspective. So, the second thing is

**[46:29]** perspective. So, the second thing is

**[46:29]** perspective. So, the second thing is model choice. This is the reasoning

**[46:32]** model choice. This is the reasoning

**[46:32]** model choice. This is the reasoning knobs uh and their view on it. They have

**[46:34]** knobs uh and their view on it. They have

**[46:34]** knobs uh and their view on it. They have fast, smart, and Oracle. So, they lean

**[46:38]** fast, smart, and Oracle. So, they lean

**[46:38]** fast, smart, and Oracle. So, they lean even more heavily into we have different

**[46:41]** even more heavily into we have different

**[46:41]** even more heavily into we have different models. We're not telling you what

**[46:42]** models. We're not telling you what

**[46:42]** models. We're not telling you what Oracle is. They tell you, but we're

**[46:44]** Oracle is. They tell you, but we're

**[46:44]** Oracle is. They tell you, but we're willing to switch what Oracle is, but

**[46:46]** willing to switch what Oracle is, but

**[46:46]** willing to switch what Oracle is, but we're going to use Oracle when we have a

**[46:48]** we're going to use Oracle when we have a

**[46:48]** we're going to use Oracle when we have a very hard problem.

**[46:50]** very hard problem.

**[46:50]** very hard problem. So, yeah. So, that's AMP. Let's go to

**[46:54]** So, yeah. So, that's AMP. Let's go to

**[46:54]** So, yeah. So, that's AMP. Let's go to Cursor's Agent. I think Cursor's agent

**[46:56]** Cursor's Agent. I think Cursor's agent

**[46:56]** Cursor's Agent. I think Cursor's agent has a very interesting perspective here.

**[46:58]** has a very interesting perspective here.

**[46:58]** has a very interesting perspective here. First, obviously, it's UI. uh UI first,


### [47:00 - 48:00]

**[47:01]** First, obviously, it's UI. uh UI first,

**[47:01]** First, obviously, it's UI. uh UI first, not CLI. I think they might have a CLI,

**[47:03]** not CLI. I think they might have a CLI,

**[47:03]** not CLI. I think they might have a CLI, not entirely sure, but the UI is the

**[47:05]** not entirely sure, but the UI is the

**[47:05]** not entirely sure, but the UI is the interesting part. It's just so fast.

**[47:07]** interesting part. It's just so fast.

**[47:07]** interesting part. It's just so fast. Their new model composer, it's

**[47:09]** Their new model composer, it's

**[47:09]** Their new model composer, it's distilled. They have they have the data.

**[47:11]** distilled. They have they have the data.

**[47:11]** distilled. They have they have the data. They actually made, in my opinion,

**[47:13]** They actually made, in my opinion,

**[47:13]** They actually made, in my opinion, people interested in fine-tuning again.

**[47:15]** people interested in fine-tuning again.

**[47:15]** people interested in fine-tuning again. fine-tuning. It was almost uh we'd never

**[47:18]** fine-tuning. It was almost uh we'd never

**[47:18]** fine-tuning. It was almost uh we'd never recommend it to our customers, but

**[47:20]** recommend it to our customers, but

**[47:20]** recommend it to our customers, but composer shows you that you can actually

**[47:22]** composer shows you that you can actually

**[47:22]** composer shows you that you can actually build defensibility based on your data

**[47:24]** build defensibility based on your data

**[47:24]** build defensibility based on your data again, which which is uh surprising, but

**[47:28]** again, which which is uh surprising, but

**[47:28]** again, which which is uh surprising, but uh yeah, cursors agent composer, I've

**[47:30]** uh yeah, cursors agent composer, I've

**[47:30]** uh yeah, cursors agent composer, I've been almost switching completely to it

**[47:33]** been almost switching completely to it

**[47:33]** been almost switching completely to it since because it's just so fast. It's

**[47:34]** since because it's just so fast. It's

**[47:34]** since because it's just so fast. It's almost too fast. Accidentally pushed to

**[47:36]** almost too fast. Accidentally pushed to

**[47:36]** almost too fast. Accidentally pushed to master on one of my personal projects.

**[47:38]** master on one of my personal projects.

**[47:38]** master on one of my personal projects. Uh so you don't you don't want that

**[47:40]** Uh so you don't you don't want that

**[47:40]** Uh so you don't you don't want that always. Uh but cursor was just the crowd

**[47:42]** always. Uh but cursor was just the crowd

**[47:42]** always. Uh but cursor was just the crowd favorite and and I want to give a lot of

**[47:45]** favorite and and I want to give a lot of

**[47:45]** favorite and and I want to give a lot of uh props to their team. They built

**[47:48]** uh props to their team. They built

**[47:48]** uh props to their team. They built iteratively. The first version of cursor

**[47:50]** iteratively. The first version of cursor

**[47:50]** iteratively. The first version of cursor was so bad and it was and we all use I

**[47:53]** was so bad and it was and we all use I

**[47:53]** was so bad and it was and we all use I used it because it's a VS code for fork.

**[47:55]** used it because it's a VS code for fork.

**[47:55]** used it because it's a VS code for fork. I have nothing to lose and it's gotten

**[47:57]** I have nothing to lose and it's gotten

**[47:57]** I have nothing to lose and it's gotten so good. It's such a good piece of

**[47:58]** so good. It's such a good piece of

**[47:58]** so good. It's such a good piece of software and it's a great team and uh


### [48:00 - 49:00]

**[48:01]** software and it's a great team and uh

**[48:01]** software and it's a great team and uh but I I'll say the same can be said

**[48:03]** but I I'll say the same can be said

**[48:03]** but I I'll say the same can be said about OpenAI's codeex models. They're

**[48:05]** about OpenAI's codeex models. They're

**[48:05]** about OpenAI's codeex models. They're not quite as fast, but they are

**[48:08]** not quite as fast, but they are

**[48:08]** not quite as fast, but they are optimized for these coding agents and

**[48:10]** optimized for these coding agents and

**[48:10]** optimized for these coding agents and they are distilled. And I could see

**[48:12]** they are distilled. And I could see

**[48:12]** they are distilled. And I could see OpenAI coming out with a really fast

**[48:14]** OpenAI coming out with a really fast

**[48:14]** OpenAI coming out with a really fast model here because they also have the

**[48:16]** model here because they also have the

**[48:16]** model here because they also have the data.

**[48:18]** data.

**[48:18]** data. So here's a picture. Um I think you

**[48:20]** So here's a picture. Um I think you

**[48:20]** So here's a picture. Um I think you could this is a picture they put on

**[48:23]** could this is a picture they put on

**[48:23]** could this is a picture they put on their blog and you could see what their

**[48:25]** their blog and you could see what their

**[48:25]** their blog and you could see what their perspective is on coding agents here

**[48:27]** perspective is on coding agents here

**[48:27]** perspective is on coding agents here just based on the fact that they show

**[48:28]** just based on the fact that they show

**[48:28]** just based on the fact that they show you the three models they're running.

**[48:30]** you the three models they're running.

**[48:30]** you the three models they're running. So, they're offering composer, but

**[48:32]** So, they're offering composer, but

**[48:32]** So, they're offering composer, but they're letting you use the

**[48:32]** they're letting you use the

**[48:32]** they're letting you use the state-of-the-art because they know that

**[48:34]** state-of-the-art because they know that

**[48:34]** state-of-the-art because they know that maybe GPD 5.1 is better at planning or

**[48:38]** maybe GPD 5.1 is better at planning or

**[48:38]** maybe GPD 5.1 is better at planning or here it's five, but now we have 5.1.

**[48:42]** here it's five, but now we have 5.1.

**[48:42]** here it's five, but now we have 5.1. So, here begs the big question, which

**[48:45]** So, here begs the big question, which

**[48:45]** So, here begs the big question, which one should we all use? Which

**[48:46]** one should we all use? Which

**[48:46]** one should we all use? Which architecture is best? What should we do?

**[48:49]** architecture is best? What should we do?

**[48:49]** architecture is best? What should we do? And uh my opinion here is that

**[48:53]** And uh my opinion here is that

**[48:53]** And uh my opinion here is that benchmarks are pretty useless.

**[48:55]** benchmarks are pretty useless.

**[48:55]** benchmarks are pretty useless. Benchmarks have become marketing for a

**[48:57]** Benchmarks have become marketing for a

**[48:57]** Benchmarks have become marketing for a lot of these model providers. every

**[48:58]** lot of these model providers. every

**[48:58]** lot of these model providers. every model beats the benchmarks. I don't know


### [49:00 - 50:00]

**[49:01]** model beats the benchmarks. I don't know

**[49:01]** model beats the benchmarks. I don't know how that happens, but

**[49:04]** how that happens, but

**[49:04]** how that happens, but I think there's there's world where

**[49:05]** I think there's there's world where

**[49:06]** I think there's there's world where evals matter here. And

**[49:08]** evals matter here. And

**[49:08]** evals matter here. And the question is what you can eval. The

**[49:10]** the question is what you can eval. The

**[49:10]** the question is what you can eval. The question is how this whole simplic

**[49:14]** question is how this whole simplic

**[49:14]** question is how this whole simplic simple while loop architecture that I've

**[49:16]** simple while loop architecture that I've

**[49:16]** simple while loop architecture that I've been kind of trying to push based on my

**[49:18]** been kind of trying to push based on my

**[49:18]** been kind of trying to push based on my understanding of it actually makes it

**[49:20]** understanding of it actually makes it

**[49:20]** understanding of it actually makes it harder to eval because if we're relying

**[49:22]** harder to eval because if we're relying

**[49:22]** harder to eval because if we're relying more on model flexibility, how do you

**[49:25]** more on model flexibility, how do you

**[49:25]** more on model flexibility, how do you test it? You could run an integration

**[49:27]** test it? You could run an integration

**[49:27]** test it? You could run an integration test, kind of this endto-end test, and

**[49:29]** test, kind of this endto-end test, and

**[49:29]** test, kind of this endto-end test, and just say, "Does it fix the problem?"

**[49:31]** just say, "Does it fix the problem?"

**[49:31]** just say, "Does it fix the problem?" That's one way to do it. You could break

**[49:33]** That's one way to do it. You could break

**[49:33]** That's one way to do it. You could break it up. You could kind of do point in

**[49:34]** it up. You could kind of do point in

**[49:34]** it up. You could kind of do point in time snapshots and say, "Hey, I'm going

**[49:37]** time snapshots and say, "Hey, I'm going

**[49:37]** time snapshots and say, "Hey, I'm going to give a context to my chatbot from

**[49:39]** to give a context to my chatbot from

**[49:39]** to give a context to my chatbot from like a half-finish conversation where I

**[49:41]** like a half-finish conversation where I

**[49:41]** like a half-finish conversation where I know it should be running a specific

**[49:42]** know it should be running a specific

**[49:42]** know it should be running a specific tool call." I could run those. Uh I or I

**[49:45]** tool call." I could run those. Uh I or I

**[49:46]** tool call." I could run those. Uh I or I could maybe just run a back test and

**[49:47]** could maybe just run a back test and

**[49:47]** could maybe just run a back test and say, "How how often does it change the

**[49:49]** say, "How how often does it change the

**[49:49]** say, "How how often does it change the tools?" I think there's also another

**[49:52]** tools?" I think there's also another

**[49:52]** tools?" I think there's also another concept here that's starting to be

**[49:53]** concept here that's starting to be

**[49:53]** concept here that's starting to be developed called agent smell or at least

**[49:55]** developed called agent smell or at least

**[49:56]** developed called agent smell or at least I'm calling it agent smell. So run an

**[49:58]** I'm calling it agent smell. So run an

**[49:58]** I'm calling it agent smell. So run an agent and see how many times does it

**[49:59]** agent and see how many times does it


### [50:00 - 51:00]

**[50:00]** agent and see how many times does it call a tool call. How many times does it

**[50:01]** call a tool call. How many times does it

**[50:01]** call a tool call. How many times does it retry? How long does it take? And these

**[50:03]** retry? How long does it take? And these

**[50:03]** retry? How long does it take? And these are all surface level metrics but it's

**[50:05]** are all surface level metrics but it's

**[50:05]** are all surface level metrics but it's really good for sanity checking. And

**[50:07]** really good for sanity checking. And

**[50:07]** really good for sanity checking. And these things are hard to eval. There's a

**[50:09]** these things are hard to eval. There's a

**[50:09]** these things are hard to eval. There's a lot that goes into it. I'll show you an

**[50:11]** lot that goes into it. I'll show you an

**[50:11]** lot that goes into it. I'll show you an example of what I did uh just to kind of

**[50:14]** example of what I did uh just to kind of

**[50:14]** example of what I did uh just to kind of dive into it. But but on that subject

**[50:17]** dive into it. But but on that subject

**[50:17]** dive into it. But but on that subject maybe I'll just say one more thing. I

**[50:19]** maybe I'll just say one more thing. I

**[50:20]** maybe I'll just say one more thing. I would break it down me my mental model

**[50:22]** would break it down me my mental model

**[50:22]** would break it down me my mental model is you could do an endto-end test, you

**[50:24]** is you could do an endto-end test, you

**[50:24]** is you could do an endto-end test, you can do a point in time test or what I

**[50:27]** can do a point in time test or what I

**[50:27]** can do a point in time test or what I most often recommend is just do a back

**[50:30]** most often recommend is just do a back

**[50:30]** most often recommend is just do a back test. Start with back test, start

**[50:32]** test. Start with back test, start

**[50:32]** test. Start with back test, start capturing historical data and then just

**[50:34]** capturing historical data and then just

**[50:34]** capturing historical data and then just rerun it. So yeah, let me give you uh

**[50:37]** rerun it. So yeah, let me give you uh

**[50:37]** rerun it. So yeah, let me give you uh this example. So basically what I have

**[50:40]** this example. So basically what I have

**[50:40]** this example. So basically what I have here, so this is a screenshot of prompt

**[50:42]** here, so this is a screenshot of prompt

**[50:42]** here, so this is a screenshot of prompt layer. This is our our eval product is

**[50:44]** layer. This is our our eval product is

**[50:44]** layer. This is our our eval product is also just a batch runner. So you could

**[50:45]** also just a batch runner. So you could

**[50:45]** also just a batch runner. So you could kind of just run a bunch of columns

**[50:47]** kind of just run a bunch of columns

**[50:47]** kind of just run a bunch of columns through a prompt. But in this case, I'm

**[50:49]** through a prompt. But in this case, I'm

**[50:49]** through a prompt. But in this case, I'm running it through not a prompt, but

**[50:51]** running it through not a prompt, but

**[50:51]** running it through not a prompt, but cloud code. So I just have like a

**[50:53]** cloud code. So I just have like a

**[50:53]** cloud code. So I just have like a headless cloud code and I'm taking all

**[50:56]** headless cloud code and I'm taking all

**[50:56]** headless cloud code and I'm taking all these providers and I just my headless

**[50:57]** these providers and I just my headless

**[50:58]** these providers and I just my headless cloud code says I think I have it on the

**[50:59]** cloud code says I think I have it on the

**[50:59]** cloud code says I think I have it on the next slide. Search the web for the model


### [51:00 - 52:00]

**[51:02]** next slide. Search the web for the model

**[51:02]** next slide. Search the web for the model provider. It's given to you in a file

**[51:03]** provider. It's given to you in a file

**[51:04]** provider. It's given to you in a file variables. Find the most recent and

**[51:06]** variables. Find the most recent and

**[51:06]** variables. Find the most recent and largest model released and then return

**[51:08]** largest model released and then return

**[51:08]** largest model released and then return the name. So I don't know what it's

**[51:09]** the name. So I don't know what it's

**[51:09]** the name. So I don't know what it's doing. It's doing web search. I'm not

**[51:11]** doing. It's doing web search. I'm not

**[51:11]** doing. It's doing web search. I'm not even caring about that. This is an

**[51:12]** even caring about that. This is an

**[51:12]** even caring about that. This is an endto-end test. This is how we kind of

**[51:16]** endto-end test. This is how we kind of

**[51:16]** endto-end test. This is how we kind of try doing cloud code. And I actually

**[51:17]** try doing cloud code. And I actually

**[51:17]** try doing cloud code. And I actually think there's a lot about putting cloud

**[51:19]** think there's a lot about putting cloud

**[51:19]** think there's a lot about putting cloud code into your workflows and those type

**[51:22]** code into your workflows and those type

**[51:22]** code into your workflows and those type of headless SDKs. I'll talk about that I

**[51:24]** of headless SDKs. I'll talk about that I

**[51:24]** of headless SDKs. I'll talk about that I think next slide. But

**[51:27]** think next slide. But

**[51:27]** think next slide. But kind of main takeaway here is you can

**[51:30]** kind of main takeaway here is you can

**[51:30]** kind of main takeaway here is you can kind of start to do endto-end tests. You

**[51:32]** kind of start to do endto-end tests. You

**[51:32]** kind of start to do endto-end tests. You can look at it from a high level do a

**[51:34]** can look at it from a high level do a

**[51:34]** can look at it from a high level do a model smell and then kind of look into

**[51:36]** model smell and then kind of look into

**[51:36]** model smell and then kind of look into the statistics on each row and see how

**[51:38]** the statistics on each row and see how

**[51:38]** the statistics on each row and see how many times it called a tool.

**[51:41]** many times it called a tool.

**[51:41]** many times it called a tool. And going back and we we've talked about

**[51:43]** And going back and we we've talked about

**[51:43]** And going back and we we've talked about this a lot in this talk. rigorous tools.

**[51:47]** this a lot in this talk. rigorous tools.

**[51:47]** this a lot in this talk. rigorous tools. The tools can be rigorously tested. You

**[51:49]** The tools can be rigorously tested. You

**[51:49]** The tools can be rigorously tested. You can This is how you offload the deter

**[51:51]** can This is how you offload the deter

**[51:51]** can This is how you offload the deter This is how you offload the determinism

**[51:53]** This is how you offload the determinism

**[51:53]** This is how you offload the determinism to different parts of your model. It's

**[51:56]** to different parts of your model. It's

**[51:56]** to different parts of your model. It's you test the tools. You you test the

**[51:58]** you test the tools. You you test the

**[51:58]** you test the tools. You you test the out of your tools. Look at them

**[51:59]** out of your tools. Look at them

**[51:59]** out of your tools. Look at them like functions. It's an input and an


### [52:00 - 53:00]

**[52:01]** like functions. It's an input and an

**[52:01]** like functions. It's an input and an output. If your tools a sub agent that

**[52:03]** output. If your tools a sub agent that

**[52:03]** output. If your tools a sub agent that runs, then we're in a kind of recursion

**[52:06]** runs, then we're in a kind of recursion

**[52:06]** runs, then we're in a kind of recursion here because then you have to go back

**[52:07]** here because then you have to go back

**[52:07]** here because then you have to go back and test the end to end thing. But for

**[52:09]** and test the end to end thing. But for

**[52:09]** and test the end to end thing. But for your tools, I'll give you this example.

**[52:12]** your tools, I'll give you this example.

**[52:12]** your tools, I'll give you this example. If I so there in my coding agents or my

**[52:18]** If I so there in my coding agents or my

**[52:18]** If I so there in my coding agents or my agents in general, my autonomous agents,

**[52:20]** agents in general, my autonomous agents,

**[52:20]** agents in general, my autonomous agents, if there's something very specific that

**[52:22]** if there's something very specific that

**[52:22]** if there's something very specific that I want to output. So in this case, if I

**[52:24]** I want to output. So in this case, if I

**[52:24]** I want to output. So in this case, if I have a very specific type of email

**[52:26]** have a very specific type of email

**[52:26]** have a very specific type of email format or type of blog post that I want

**[52:29]** format or type of blog post that I want

**[52:29]** format or type of blog post that I want to write and I really want it to get my

**[52:31]** to write and I really want it to get my

**[52:31]** to write and I really want it to get my voice right, I don't want to rely on the

**[52:33]** voice right, I don't want to rely on the

**[52:33]** voice right, I don't want to rely on the model exploration. I want to actually

**[52:35]** model exploration. I want to actually

**[52:35]** model exploration. I want to actually build a tool that I can rigorously test.

**[52:38]** build a tool that I can rigorously test.

**[52:38]** build a tool that I can rigorously test. So in this case, this is also just a

**[52:40]** So in this case, this is also just a

**[52:40]** So in this case, this is also just a prompt layer screenshot, but this is a

**[52:43]** prompt layer screenshot, but this is a

**[52:43]** prompt layer screenshot, but this is a like a workflow I've built. It has an LM

**[52:45]** like a workflow I've built. It has an LM

**[52:45]** like a workflow I've built. It has an LM assertion where it says check if the

**[52:47]** assertion where it says check if the

**[52:47]** assertion where it says check if the email is good to my standards. If it's

**[52:49]** email is good to my standards. If it's

**[52:49]** email is good to my standards. If it's good, it revises it. If it's not good,

**[52:51]** good, it revises it. If it's not good,

**[52:51]** good, it revises it. If it's not good, it adds the parts. So like the header

**[52:52]** it adds the parts. So like the header

**[52:52]** it adds the parts. So like the header that it missed and it revises it with

**[52:54]** that it missed and it revises it with

**[52:54]** that it missed and it revises it with the same step. This is obviously a very

**[52:57]** the same step. This is obviously a very

**[52:57]** the same step. This is obviously a very simple example, but in I we have another


### [53:00 - 54:00]

**[53:01]** simple example, but in I we have another

**[53:02]** simple example, but in I we have another version for some of our SEO blog posts

**[53:04]** version for some of our SEO blog posts

**[53:04]** version for some of our SEO blog posts that has like 20 different nodes and

**[53:07]** that has like 20 different nodes and

**[53:07]** that has like 20 different nodes and writes an outline from a deep research

**[53:09]** writes an outline from a deep research

**[53:09]** writes an outline from a deep research and then fixes a conclusion and adds

**[53:12]** and then fixes a conclusion and adds

**[53:12]** and then fixes a conclusion and adds links.

**[53:13]** links.

**[53:13]** links. for the stuff that you have a very

**[53:15]** for the stuff that you have a very

**[53:15]** for the stuff that you have a very specific vision that's when testing it

**[53:18]** specific vision that's when testing it

**[53:18]** specific vision that's when testing it just gets so much easier because as you

**[53:20]** just gets so much easier because as you

**[53:20]** just gets so much easier because as you can see obviously testing this sort of

**[53:23]** can see obviously testing this sort of

**[53:23]** can see obviously testing this sort of workflow has less steps and less

**[53:25]** workflow has less steps and less

**[53:25]** workflow has less steps and less flexibility. So this is an eval I made I

**[53:28]** flexibility. So this is an eval I made I

**[53:28]** flexibility. So this is an eval I made I start with just a bunch of sample emails

**[53:30]** start with just a bunch of sample emails

**[53:30]** start with just a bunch of sample emails I run the prompt actually I run the the

**[53:33]** I run the prompt actually I run the the

**[53:33]** I run the prompt actually I run the the agentic workflow here and I'm just

**[53:36]** agentic workflow here and I'm just

**[53:36]** agentic workflow here and I'm just adding a bunch of heruristics. So this

**[53:38]** adding a bunch of heruristics. So this

**[53:38]** adding a bunch of heruristics. So this is a very simple LMS judge does it

**[53:40]** is a very simple LMS judge does it

**[53:40]** is a very simple LMS judge does it include three parts in it. So this is

**[53:41]** include three parts in it. So this is

**[53:41]** include three parts in it. So this is what I was testing for like the hi Jared

**[53:44]** what I was testing for like the hi Jared

**[53:44]** what I was testing for like the hi Jared email body and the signature. You can

**[53:46]** email body and the signature. You can

**[53:46]** email body and the signature. You can get a lot more complicated. You could do

**[53:48]** get a lot more complicated. You could do

**[53:48]** get a lot more complicated. You could do a code execution. You can do I don't

**[53:51]** a code execution. You can do I don't

**[53:51]** a code execution. You can do I don't know LM's judge is usually the easiest.

**[53:53]** know LM's judge is usually the easiest.

**[53:53]** know LM's judge is usually the easiest. But now obviously you could see I could

**[53:55]** But now obviously you could see I could

**[53:55]** But now obviously you could see I could keep running this until it's correct on

**[53:56]** keep running this until it's correct on

**[53:56]** keep running this until it's correct on all of them and kind of uh see my eval

**[53:59]** all of them and kind of uh see my eval

**[53:59]** all of them and kind of uh see my eval over time. This is just from this


### [54:00 - 55:00]

**[54:01]** over time. This is just from this

**[54:01]** over time. This is just from this example. I got it to 100. So that was

**[54:03]** example. I got it to 100. So that was

**[54:03]** example. I got it to 100. So that was fun.

**[54:04]** fun.

**[54:04]** fun. Uh and then I want to I want to add

**[54:07]** Uh and then I want to I want to add

**[54:07]** Uh and then I want to I want to add another future looking thing. keep an

**[54:09]** another future looking thing. keep an

**[54:09]** another future looking thing. keep an eye on headless uh cloud code SDK. I

**[54:13]** eye on headless uh cloud code SDK. I

**[54:13]** eye on headless uh cloud code SDK. I know there was a talk about it this

**[54:14]** know there was a talk about it this

**[54:14]** know there was a talk about it this morning. Um so I don't want to I won't

**[54:16]** morning. Um so I don't want to I won't

**[54:16]** morning. Um so I don't want to I won't spend too much time on it, but it's

**[54:19]** spend too much time on it, but it's

**[54:19]** spend too much time on it, but it's amazing. You just give a simple prompt

**[54:21]** amazing. You just give a simple prompt

**[54:21]** amazing. You just give a simple prompt and it's just another part of your

**[54:23]** and it's just another part of your

**[54:23]** and it's just another part of your pipeline. I use it for I think I have it

**[54:26]** pipeline. I use it for I think I have it

**[54:26]** pipeline. I use it for I think I have it on the next slide. I have a GitHub

**[54:28]** on the next slide. I have a GitHub

**[54:28]** on the next slide. I have a GitHub action that updates my docs every day

**[54:31]** action that updates my docs every day

**[54:31]** action that updates my docs every day and just reads all the commits we've

**[54:33]** and just reads all the commits we've

**[54:33]** and just reads all the commits we've pushed to our other repos. And we have a

**[54:35]** pushed to our other repos. And we have a

**[54:35]** pushed to our other repos. And we have a lot of commits going and it just runs

**[54:37]** lot of commits going and it just runs

**[54:37]** lot of commits going and it just runs cloud code. The cloud code pulls down

**[54:39]** cloud code. The cloud code pulls down

**[54:39]** cloud code. The cloud code pulls down all the repos, checks what's updated,

**[54:42]** all the repos, checks what's updated,

**[54:42]** all the repos, checks what's updated, reads our cloud MD to see if it should

**[54:44]** reads our cloud MD to see if it should

**[54:44]** reads our cloud MD to see if it should even update the docs, then creates a PR.

**[54:47]** even update the docs, then creates a PR.

**[54:47]** even update the docs, then creates a PR. So I think this unlocks a lot of things

**[54:49]** So I think this unlocks a lot of things

**[54:50]** So I think this unlocks a lot of things and there's a possibility that we're

**[54:51]** and there's a possibility that we're

**[54:51]** and there's a possibility that we're going to start building agents at a

**[54:53]** going to start building agents at a

**[54:53]** going to start building agents at a higher order of abstraction and just

**[54:54]** higher order of abstraction and just

**[54:54]** higher order of abstraction and just rely on cloud code and these other

**[54:56]** rely on cloud code and these other

**[54:56]** rely on cloud code and these other agents to do a lot of the harnesses and


### [55:00 - 56:00]

**[55:00]** agents to do a lot of the harnesses and

**[55:00]** agents to do a lot of the harnesses and orchestration.

**[55:01]** orchestration.

**[55:01]** orchestration. >> Are you reviewing those?

**[55:03]** >> Are you reviewing those?

**[55:03]** >> Are you reviewing those? Yeah, [laughter]

**[55:06]** Yeah, [laughter]

**[55:06]** Yeah, [laughter] I it creates a PR. It doesn't uh it

**[55:09]** I it creates a PR. It doesn't uh it

**[55:09]** I it creates a PR. It doesn't uh it doesn't merge the VR.

**[55:12]** doesn't merge the VR.

**[55:12]** doesn't merge the VR. So, here are my takeaways. Number one,

**[55:15]** So, here are my takeaways. Number one,

**[55:15]** So, here are my takeaways. Number one, trust in the model. Uh when in doubt,

**[55:18]** trust in the model. Uh when in doubt,

**[55:18]** trust in the model. Uh when in doubt, rely on the model when you're building

**[55:19]** rely on the model when you're building

**[55:19]** rely on the model when you're building agents. Number two, simple design wins.

**[55:23]** agents. Number two, simple design wins.

**[55:23]** agents. Number two, simple design wins. Number one and number two kind of go

**[55:25]** Number one and number two kind of go

**[55:25]** Number one and number two kind of go together here. Number three, bash is all

**[55:28]** together here. Number three, bash is all

**[55:28]** together here. Number three, bash is all you need.

**[55:29]** you need.

**[55:29]** you need. Go simple with your tools. Don't have 40

**[55:32]** Go simple with your tools. Don't have 40

**[55:32]** Go simple with your tools. Don't have 40 tools, have 10 or five tools. For

**[55:36]** tools, have 10 or five tools. For

**[55:36]** tools, have 10 or five tools. For context management matters, this is the

**[55:38]** context management matters, this is the

**[55:38]** context management matters, this is the boogeyman we're running from all the

**[55:41]** boogeyman we're running from all the

**[55:41]** boogeyman we're running from all the time in agents at this point. Maybe

**[55:43]** time in agents at this point. Maybe

**[55:43]** time in agents at this point. Maybe there'll be new models in the future

**[55:45]** there'll be new models in the future

**[55:45]** there'll be new models in the future that are just so much better at context.

**[55:47]** that are just so much better at context.

**[55:47]** that are just so much better at context. But there's always going to be a limit

**[55:49]** But there's always going to be a limit

**[55:49]** But there's always going to be a limit because ah you're talking to a human. I

**[55:52]** because ah you're talking to a human. I

**[55:52]** because ah you're talking to a human. I forget people's names if I meet too many

**[55:53]** forget people's names if I meet too many

**[55:53]** forget people's names if I meet too many in one day. That's context management or

**[55:56]** in one day. That's context management or

**[55:56]** in one day. That's context management or my stupidity. I don't know. And number

**[55:58]** my stupidity. I don't know. And number

**[55:58]** my stupidity. I don't know. And number five, different perspectives. matter in


### [56:00 - 57:00]

**[56:01]** five, different perspectives. matter in

**[56:01]** five, different perspectives. matter in agents. I think this is the engineering

**[56:04]** agents. I think this is the engineering

**[56:04]** agents. I think this is the engineering brain doesn't always comprehend this as

**[56:07]** brain doesn't always comprehend this as

**[56:07]** brain doesn't always comprehend this as much as it should especially in and I'm

**[56:09]** much as it should especially in and I'm

**[56:10]** much as it should especially in and I'm an engineer so I'm also talking about

**[56:11]** an engineer so I'm also talking about

**[56:11]** an engineer so I'm also talking about myself but the different perspectives

**[56:14]** myself but the different perspectives

**[56:14]** myself but the different perspectives matter such that there's different uh

**[56:18]** matter such that there's different uh

**[56:18]** matter such that there's different uh ways to solve a problem where there's

**[56:20]** ways to solve a problem where there's

**[56:20]** ways to solve a problem where there's not one is better than the other and you

**[56:22]** not one is better than the other and you

**[56:22]** not one is better than the other and you kind of you probably want a mixture of

**[56:24]** kind of you probably want a mixture of

**[56:24]** kind of you probably want a mixture of experts agent I I would love to have

**[56:26]** experts agent I I would love to have

**[56:26]** experts agent I I would love to have mine run cloud code and codeex and this

**[56:28]** mine run cloud code and codeex and this

**[56:28]** mine run cloud code and codeex and this and give me the output and considered a

**[56:30]** and give me the output and considered a

**[56:30]** and give me the output and considered a team and maybe have them talk to each

**[56:32]** team and maybe have them talk to each

**[56:32]** team and maybe have them talk to each other in a slack based message channel.

**[56:34]** other in a slack based message channel.

**[56:34]** other in a slack based message channel. I'm waiting for someone to build that.

**[56:36]** I'm waiting for someone to build that.

**[56:36]** I'm waiting for someone to build that. That would be great. But these are my

**[56:38]** That would be great. But these are my

**[56:38]** That would be great. But these are my takeaways. Uh my bonus thing that I'll

**[56:40]** takeaways. Uh my bonus thing that I'll

**[56:40]** takeaways. Uh my bonus thing that I'll show you is how I built this slide deck

**[56:42]** show you is how I built this slide deck

**[56:42]** show you is how I built this slide deck using cloud code. So uh I built a slide

**[56:46]** using cloud code. So uh I built a slide

**[56:46]** using cloud code. So uh I built a slide dev skill. So I I basically told cloud

**[56:48]** dev skill. So I I basically told cloud

**[56:48]** dev skill. So I I basically told cloud code to research how slide dev works and

**[56:50]** code to research how slide dev works and

**[56:50]** code to research how slide dev works and how it can and that's kind of just a

**[56:52]** how it can and that's kind of just a

**[56:52]** how it can and that's kind of just a library that I made this in. I built a

**[56:54]** library that I made this in. I built a

**[56:54]** library that I made this in. I built a deep research skill to research all

**[56:57]** deep research skill to research all

**[56:57]** deep research skill to research all these agents and how they work. I built

**[56:58]** these agents and how they work. I built

**[56:58]** these agents and how they work. I built a design skill because I know half a


### [57:00 - 58:00]

**[57:01]** a design skill because I know half a

**[57:01]** a design skill because I know half a thing looks terrible or looks good, but

**[57:03]** thing looks terrible or looks good, but

**[57:03]** thing looks terrible or looks good, but I'm not a good designer to figure it

**[57:05]** I'm not a good designer to figure it

**[57:05]** I'm not a good designer to figure it out. So, these boxes even I was just

**[57:07]** out. So, these boxes even I was just

**[57:07]** out. So, these boxes even I was just like, "Oh, m make the box a little

**[57:09]** like, "Oh, m make the box a little

**[57:09]** like, "Oh, m make the box a little nicer. Give it an accent color." Uh, so

**[57:12]** nicer. Give it an accent color." Uh, so

**[57:12]** nicer. Give it an accent color." Uh, so yeah, this is how I built it. But again,

**[57:14]** yeah, this is how I built it. But again,

**[57:14]** yeah, this is how I built it. But again, thank you for listening. Uh, happy to

**[57:15]** thank you for listening. Uh, happy to

**[57:16]** thank you for listening. Uh, happy to answer any questions. I'm Jared, founder

**[57:18]** answer any questions. I'm Jared, founder

**[57:18]** answer any questions. I'm Jared, founder of Prompt Layer. Find me there.

**[57:20]** of Prompt Layer. Find me there.

**[57:20]** of Prompt Layer. Find me there. [applause]

**[57:25]** >> Yes.

**[57:25]** >> Yes. >> Thank you. Great talk. Um so you

**[57:27]** >> Thank you. Great talk. Um so you

**[57:27]** >> Thank you. Great talk. Um so you mentioned u regarding DAGs basically

**[57:29]** mentioned u regarding DAGs basically

**[57:30]** mentioned u regarding DAGs basically like let's get rid of them right but

**[57:32]** like let's get rid of them right but

**[57:32]** like let's get rid of them right but DAGs kind of enforc this like sequential

**[57:36]** DAGs kind of enforc this like sequential

**[57:36]** DAGs kind of enforc this like sequential uh execution right pass I don't know

**[57:39]** uh execution right pass I don't know

**[57:39]** uh execution right pass I don't know customer service like agent asks the

**[57:41]** customer service like agent asks the

**[57:41]** customer service like agent asks the name email right like in some sort of uh

**[57:46]** name email right like in some sort of uh

**[57:46]** name email right like in some sort of uh sequence um so are you saying

**[57:50]** sequence um so are you saying

**[57:50]** sequence um so are you saying just write this out um like this is now

**[57:54]** just write this out um like this is now

**[57:54]** just write this out um like this is now this should be uh just written out as a

**[57:57]** this should be uh just written out as a

**[57:57]** this should be uh just written out as a plan for an agent to execute and just


### [58:00 - 59:00]

**[58:00]** plan for an agent to execute and just

**[58:00]** plan for an agent to execute and just trust that the model is going to be

**[58:02]** trust that the model is going to be

**[58:02]** trust that the model is going to be calling those tools in that sequence

**[58:04]** calling those tools in that sequence

**[58:04]** calling those tools in that sequence like how do we enforce uh the order?

**[58:07]** like how do we enforce uh the order?

**[58:07]** like how do we enforce uh the order? >> Right? So the question was

**[58:11]** >> Right? So the question was

**[58:11]** >> Right? So the question was why do I keep talking about getting rid

**[58:13]** why do I keep talking about getting rid

**[58:13]** why do I keep talking about getting rid of DAGs? How else am are you supposed to

**[58:16]** of DAGs? How else am are you supposed to

**[58:16]** of DAGs? How else am are you supposed to enforce a specific order for solving a

**[58:18]** enforce a specific order for solving a

**[58:18]** enforce a specific order for solving a problem? So I think there are different

**[58:21]** problem? So I think there are different

**[58:21]** problem? So I think there are different types of problems. So the problem of

**[58:25]** types of problems. So the problem of

**[58:25]** types of problems. So the problem of building a general purpose coding agent

**[58:27]** building a general purpose coding agent

**[58:27]** building a general purpose coding agent that we can all use to do our work and

**[58:29]** that we can all use to do our work and

**[58:30]** that we can all use to do our work and even non-technical people can use

**[58:31]** even non-technical people can use

**[58:31]** even non-technical people can use there's no specific step to solving that

**[58:33]** there's no specific step to solving that

**[58:33]** there's no specific step to solving that problem which is why it's better to rely

**[58:36]** problem which is why it's better to rely

**[58:36]** problem which is why it's better to rely on the model. If your problem was

**[58:40]** on the model. If your problem was

**[58:40]** on the model. If your problem was to build

**[58:42]** to build

**[58:42]** to build let's say a travel itinerary

**[58:46]** let's say a travel itinerary

**[58:46]** let's say a travel itinerary it's more of a specific step because you

**[58:48]** it's more of a specific step because you

**[58:48]** it's more of a specific step because you have a deliverable that's always the

**[58:50]** have a deliverable that's always the

**[58:50]** have a deliverable that's always the same. So there's a little bit more of a

**[58:52]** same. So there's a little bit more of a

**[58:52]** same. So there's a little bit more of a DAG that could matter, but in the

**[58:54]** DAG that could matter, but in the

**[58:54]** DAG that could matter, but in the research step of traveling, you probably

**[58:56]** research step of traveling, you probably

**[58:56]** research step of traveling, you probably don't want a DAG because every city is

**[58:58]** don't want a DAG because every city is

**[58:58]** don't want a DAG because every city is going to be different. So it really

**[58:59]** going to be different. So it really

**[58:59]** going to be different. So it really depends on the problem you're solving. I


### [59:00 - 01:00:00]

**[59:01]** depends on the problem you're solving. I

**[59:01]** depends on the problem you're solving. I would if I wanted to make an agent for a

**[59:03]** would if I wanted to make an agent for a

**[59:03]** would if I wanted to make an agent for a travel itinerary, I'd probably have my

**[59:05]** travel itinerary, I'd probably have my

**[59:05]** travel itinerary, I'd probably have my tool call would one of my tool calls be

**[59:08]** tool call would one of my tool calls be

**[59:08]** tool call would one of my tool calls be a DAG of creating the output file

**[59:10]** a DAG of creating the output file

**[59:10]** a DAG of creating the output file because I want the output to look the

**[59:11]** because I want the output to look the

**[59:11]** because I want the output to look the same or creating the plan. And then in

**[59:14]** same or creating the plan. And then in

**[59:14]** same or creating the plan. And then in the system problem, I could say always

**[59:15]** the system problem, I could say always

**[59:15]** the system problem, I could say always end with the output for example. But

**[59:19]** end with the output for example. But

**[59:19]** end with the output for example. But you need to mix and match. There's a

**[59:21]** you need to mix and match. There's a

**[59:21]** you need to mix and match. There's a every use case is different, but if you

**[59:22]** every use case is different, but if you

**[59:22]** every use case is different, but if you want to make something general purpose,

**[59:24]** want to make something general purpose,

**[59:24]** want to make something general purpose, my take is to rely more on the model on

**[59:27]** my take is to rely more on the model on

**[59:28]** my take is to rely more on the model on simple loops and less on a DAG.

**[59:31]** simple loops and less on a DAG.

**[59:31]** simple loops and less on a DAG. >> Cool. Any other questions?

**[59:34]** >> Cool. Any other questions?

**[59:34]** >> Cool. Any other questions? Yes.

**[59:34]** Yes.

**[59:34]** Yes. >> Yeah. Building on that point, like do

**[59:37]** >> Yeah. Building on that point, like do

**[59:37]** >> Yeah. Building on that point, like do you think we're heading towards a world

**[59:38]** you think we're heading towards a world

**[59:38]** you think we're heading towards a world where most of you're not actually going

**[59:39]** where most of you're not actually going

**[59:39]** where most of you're not actually going to call the API through code and that

**[59:41]** to call the API through code and that

**[59:41]** to call the API through code and that most LM calls are by triggering cloud

**[59:44]** most LM calls are by triggering cloud

**[59:44]** most LM calls are by triggering cloud code and just write just writing the

**[59:46]** code and just write just writing the

**[59:46]** code and just write just writing the files instead?

**[59:52]** So the question is are we going to move

**[59:52]** So the question is are we going to move away from calling models directly and

**[59:54]** away from calling models directly and

**[59:54]** away from calling models directly and just call call like a headless cloud

**[59:57]** just call call like a headless cloud

**[59:57]** just call call like a headless cloud code, right?

**[59:58]** code, right?

**[59:58]** code, right? >> Yeah. Like if I had a like I have a


### [01:00:00 - 01:01:00]

**[01:00:01]** >> Yeah. Like if I had a like I have a

**[01:00:01]** >> Yeah. Like if I had a like I have a pipeline that does one lm call per

**[01:00:03]** pipeline that does one lm call per

**[01:00:03]** pipeline that does one lm call per document, summarizes it at the end. You

**[01:00:06]** document, summarizes it at the end. You

**[01:00:06]** document, summarizes it at the end. You could make a while loop cloud code that

**[01:00:08]** could make a while loop cloud code that

**[01:00:08]** could make a while loop cloud code that saves a file every time. You never call

**[01:00:11]** saves a file every time. You never call

**[01:00:11]** saves a file every time. You never call the API besides

**[01:00:13]** the API besides

**[01:00:13]** the API besides using cloud code in in a while loop

**[01:00:16]** using cloud code in in a while loop

**[01:00:16]** using cloud code in in a while loop >> potentially. Uh, I'll give you the pro

**[01:00:19]** >> potentially. Uh, I'll give you the pro

**[01:00:19]** >> potentially. Uh, I'll give you the pro and the con there.

**[01:00:20]** and the con there.

**[01:00:20]** and the con there. >> Yeah,

**[01:00:21]** >> Yeah,

**[01:00:21]** >> Yeah, >> the pro is it's easier to develop and we

**[01:00:23]** >> the pro is it's easier to develop and we

**[01:00:24]** >> the pro is it's easier to develop and we can kind of rely on the frontier. I

**[01:00:26]** can kind of rely on the frontier. I

**[01:00:26]** can kind of rely on the frontier. I mean, if you think about it, a reasoning

**[01:00:28]** mean, if you think about it, a reasoning

**[01:00:28]** mean, if you think about it, a reasoning model is just that. The reasoning models

**[01:00:31]** model is just that. The reasoning models

**[01:00:31]** model is just that. The reasoning models didn't always exist. We just had normal

**[01:00:32]** didn't always exist. We just had normal

**[01:00:32]** didn't always exist. We just had normal LM model and then oh, now we have 01 and

**[01:00:34]** LM model and then oh, now we have 01 and

**[01:00:34]** LM model and then oh, now we have 01 and reasoning models. All that is is a I

**[01:00:37]** reasoning models. All that is is a I

**[01:00:37]** reasoning models. All that is is a I mean, it's a little more complicated

**[01:00:38]** mean, it's a little more complicated

**[01:00:38]** mean, it's a little more complicated than this, but it's basically just a

**[01:00:39]** than this, but it's basically just a

**[01:00:39]** than this, but it's basically just a while loop on OpenAI servers that keeps

**[01:00:42]** while loop on OpenAI servers that keeps

**[01:00:42]** while loop on OpenAI servers that keeps running the context and then eventually

**[01:00:43]** running the context and then eventually

**[01:00:43]** running the context and then eventually gives you the output. in the same way

**[01:00:45]** gives you the output. in the same way

**[01:00:45]** gives you the output. in the same way that cloud code SDK is a while loop with

**[01:00:48]** that cloud code SDK is a while loop with

**[01:00:48]** that cloud code SDK is a while loop with a bunch of more things. So I could

**[01:00:51]** a bunch of more things. So I could

**[01:00:51]** a bunch of more things. So I could totally see a lot of builders only

**[01:00:54]** totally see a lot of builders only

**[01:00:54]** totally see a lot of builders only touching these agentic endpoints. Maybe

**[01:00:57]** touching these agentic endpoints. Maybe

**[01:00:57]** touching these agentic endpoints. Maybe even seeing a model provider release a

**[01:00:59]** even seeing a model provider release a

**[01:00:59]** even seeing a model provider release a model as a agentic endpoint. But for a


### [01:01:00 - 01:02:00]

**[01:01:02]** model as a agentic endpoint. But for a

**[01:01:02]** model as a agentic endpoint. But for a lot of tasks, you're going to want a

**[01:01:03]** lot of tasks, you're going to want a

**[01:01:04]** lot of tasks, you're going to want a little bit more control. And they're pro

**[01:01:07]** little bit more control. And they're pro

**[01:01:07]** little bit more control. And they're pro and probably you'd still want to go as

**[01:01:09]** and probably you'd still want to go as

**[01:01:10]** and probably you'd still want to go as close to metal as possible. Having said

**[01:01:12]** close to metal as possible. Having said

**[01:01:12]** close to metal as possible. Having said that, there's there was a lot of people

**[01:01:14]** that, there's there was a lot of people

**[01:01:14]** that, there's there was a lot of people who still wanted completions models and

**[01:01:17]** who still wanted completions models and

**[01:01:17]** who still wanted completions models and that never happened and nobody really

**[01:01:19]** that never happened and nobody really

**[01:01:19]** that never happened and nobody really talks about that anymore. So, it's very

**[01:01:21]** talks about that anymore. So, it's very

**[01:01:21]** talks about that anymore. So, it's very likely that everything just becomes this

**[01:01:23]** likely that everything just becomes this

**[01:01:23]** likely that everything just becomes this SDK, but I don't have a crystal ball,

**[01:01:24]** SDK, but I don't have a crystal ball,

**[01:01:24]** SDK, but I don't have a crystal ball, but those are those are how I I would

**[01:01:26]** but those are those are how I I would

**[01:01:26]** but those are those are how I I would think about it.

**[01:01:29]** think about it.

**[01:01:29]** think about it. >> Yes,

**[01:01:30]** >> Yes,

**[01:01:30]** >> Yes, >> thanks for the talk. Um, I know you said

**[01:01:32]** >> thanks for the talk. Um, I know you said

**[01:01:32]** >> thanks for the talk. Um, I know you said the simpler the better, but um, what's

**[01:01:35]** the simpler the better, but um, what's

**[01:01:35]** the simpler the better, but um, what's your thoughts about test during

**[01:01:37]** your thoughts about test during

**[01:01:37]** your thoughts about test during development, spec during development in

**[01:01:39]** development, spec during development in

**[01:01:39]** development, spec during development in AI? Have you tried it? What is it about

**[01:01:42]** AI? Have you tried it? What is it about

**[01:01:42]** AI? Have you tried it? What is it about >> for building agents or for getting work

**[01:01:44]** >> for building agents or for getting work

**[01:01:44]** >> for building agents or for getting work done?

**[01:01:45]** done?

**[01:01:45]** done? >> For coding.

**[01:01:46]** >> For coding.

**[01:01:46]** >> For coding. >> Okay. So the question on spec driven

**[01:01:49]** >> Okay. So the question on spec driven

**[01:01:49]** >> Okay. So the question on spec driven development, test-driven development for

**[01:01:51]** development, test-driven development for

**[01:01:51]** development, test-driven development for coding with agents.

**[01:01:53]** coding with agents.

**[01:01:53]** coding with agents. [cough and laughter]

**[01:01:54]** [cough and laughter]

**[01:01:54]** [cough and laughter] When in doubt, go back to

**[01:01:58]** When in doubt, go back to

**[01:01:58]** When in doubt, go back to good engineering practices is what I


### [01:02:00 - 01:03:00]

**[01:02:00]** good engineering practices is what I

**[01:02:00]** good engineering practices is what I would say. So it if you

**[01:02:04]** would say. So it if you

**[01:02:04]** would say. So it if you and there's there's whole engineering

**[01:02:06]** and there's there's whole engineering

**[01:02:06]** and there's there's whole engineering debates on if test-driven development is

**[01:02:08]** debates on if test-driven development is

**[01:02:08]** debates on if test-driven development is the right way and some people swear by

**[01:02:10]** the right way and some people swear by

**[01:02:10]** the right way and some people swear by it and some people don't. So I don't

**[01:02:12]** it and some people don't. So I don't

**[01:02:12]** it and some people don't. So I don't think there's an answer. I think coding

**[01:02:14]** think there's an answer. I think coding

**[01:02:14]** think there's an answer. I think coding agents clearly test-driven development

**[01:02:16]** agents clearly test-driven development

**[01:02:16]** agents clearly test-driven development makes it easier. I think as I was

**[01:02:17]** makes it easier. I think as I was

**[01:02:18]** makes it easier. I think as I was showing you that's AMP's source graphs

**[01:02:20]** showing you that's AMP's source graphs

**[01:02:20]** showing you that's AMP's source graphs whole philosophy that if you can build

**[01:02:22]** whole philosophy that if you can build

**[01:02:22]** whole philosophy that if you can build good tests and factory I think thinks

**[01:02:24]** good tests and factory I think thinks

**[01:02:24]** good tests and factory I think thinks this as well. If you could build good

**[01:02:26]** this as well. If you could build good

**[01:02:26]** this as well. If you could build good tests your coding agent can work much

**[01:02:29]** tests your coding agent can work much

**[01:02:29]** tests your coding agent can work much better. So it makes sense to me when I'm

**[01:02:31]** better. So it makes sense to me when I'm

**[01:02:31]** better. So it makes sense to me when I'm working personally I rely pretty heavily

**[01:02:34]** working personally I rely pretty heavily

**[01:02:34]** working personally I rely pretty heavily on the planning phase and the spectr in

**[01:02:36]** on the planning phase and the spectr in

**[01:02:36]** on the planning phase and the spectr in development phase and I think the

**[01:02:38]** development phase and I think the

**[01:02:38]** development phase and I think the simpler tasks are pretty easy for the

**[01:02:40]** simpler tasks are pretty easy for the

**[01:02:40]** simpler tasks are pretty easy for the model but if I'm doing a very simple

**[01:02:42]** model but if I'm doing a very simple

**[01:02:42]** model but if I'm doing a very simple edit I'll skip that step. So no

**[01:02:44]** edit I'll skip that step. So no

**[01:02:44]** edit I'll skip that step. So no oneizefits-all but return to the

**[01:02:47]** oneizefits-all but return to the

**[01:02:47]** oneizefits-all but return to the engineering principles that you believe

**[01:02:49]** engineering principles that you believe

**[01:02:49]** engineering principles that you believe when in doubt I'd say yes.

**[01:02:53]** when in doubt I'd say yes.

**[01:02:53]** when in doubt I'd say yes. >> So earlier you talked about about system

**[01:02:57]** >> So earlier you talked about about system

**[01:02:57]** >> So earlier you talked about about system rock leaks is possible to just look at


### [01:03:00 - 01:04:00]

**[01:03:00]** rock leaks is possible to just look at

**[01:03:00]** rock leaks is possible to just look at the u

**[01:03:02]** the u

**[01:03:02]** the u downloads bundle or they have a special

**[01:03:05]** downloads bundle or they have a special

**[01:03:05]** downloads bundle or they have a special end point that has prompts behind

**[01:03:07]** end point that has prompts behind

**[01:03:07]** end point that has prompts behind endpoint.

**[01:03:08]** endpoint.

**[01:03:08]** endpoint. >> Yeah. Uh I think I think they hide it. I

**[01:03:11]** >> Yeah. Uh I think I think they hide it. I

**[01:03:11]** >> Yeah. Uh I think I think they hide it. I think they hide it. There was a there

**[01:03:13]** think they hide it. There was a there

**[01:03:13]** think they hide it. There was a there was actually an interesting article

**[01:03:14]** was actually an interesting article

**[01:03:14]** was actually an interesting article someone

**[01:03:16]** someone

**[01:03:16]** someone because codeex is open source they

**[01:03:19]** because codeex is open source they

**[01:03:19]** because codeex is open source they before openai released the codeex model

**[01:03:22]** before openai released the codeex model

**[01:03:22]** before openai released the codeex model that it was using they were able to hack

**[01:03:24]** that it was using they were able to hack

**[01:03:24]** that it was using they were able to hack together the open source codeex to give

**[01:03:27]** together the open source codeex to give

**[01:03:27]** together the open source codeex to give a custom prompt to the model and be able

**[01:03:29]** a custom prompt to the model and be able

**[01:03:29]** a custom prompt to the model and be able to use the model without it. So yeah you

**[01:03:31]** to use the model without it. So yeah you

**[01:03:31]** to use the model without it. So yeah you can dive into it but generally it's

**[01:03:33]** can dive into it but generally it's

**[01:03:34]** can dive into it but generally it's tried to be hidden and also laziness of

**[01:03:36]** tried to be hidden and also laziness of

**[01:03:36]** tried to be hidden and also laziness of someone posted it. So there you go

**[01:03:38]** someone posted it. So there you go

**[01:03:38]** someone posted it. So there you go that's the work but someone had to have

**[01:03:40]** that's the work but someone had to have

**[01:03:40]** that's the work but someone had to have found it right. like is this problem

**[01:03:43]** found it right. like is this problem

**[01:03:43]** found it right. like is this problem somewhere on your machine?

**[01:03:46]** somewhere on your machine?

**[01:03:46]** somewhere on your machine? >> I actually don't know that answer.

**[01:03:47]** >> I actually don't know that answer.

**[01:03:47]** >> I actually don't know that answer. [laughter]

**[01:03:49]** [laughter]

**[01:03:49]** [laughter] >> Do you know that answer?

**[01:03:50]** >> Do you know that answer?

**[01:03:50]** >> Do you know that answer? >> Yeah.

**[01:03:50]** >> Yeah.

**[01:03:50]** >> Yeah. >> Yes.

**[01:03:52]** >> Yes.

**[01:03:52]** >> Yes. >> It's on your machine. Nico says it's on

**[01:03:54]** >> It's on your machine. Nico says it's on

**[01:03:54]** >> It's on your machine. Nico says it's on your machine. So there we go. So maybe

**[01:03:56]** your machine. So there we go. So maybe

**[01:03:56]** your machine. So there we go. So maybe the prompt I was looking at is a little

**[01:03:57]** the prompt I was looking at is a little

**[01:03:57]** the prompt I was looking at is a little bit old and I have to update it. But the


### [01:04:00 - 01:05:00]

**[01:04:00]** bit old and I have to update it. But the

**[01:04:00]** bit old and I have to update it. But the s but uh the question was does uh is the

**[01:04:04]** s but uh the question was does uh is the

**[01:04:04]** s but uh the question was does uh is the prompt hidden on their servers or can

**[01:04:07]** prompt hidden on their servers or can

**[01:04:07]** prompt hidden on their servers or can you find it if you are so determined?

**[01:04:09]** you find it if you are so determined?

**[01:04:09]** you find it if you are so determined? And the answer seems to be yes. Any

**[01:04:13]** And the answer seems to be yes. Any

**[01:04:13]** And the answer seems to be yes. Any other questions?

**[01:04:15]** other questions?

**[01:04:15]** other questions? >> Yes.

**[01:04:16]** >> Yes.

**[01:04:16]** >> Yes. >> Is this the last one?

**[01:04:17]** >> Is this the last one?

**[01:04:18]** >> Is this the last one? >> Is this the last question?

**[01:04:19]** >> Is this the last question?

**[01:04:19]** >> Is this the last question? >> It can be.

**[01:04:21]** >> It can be.

**[01:04:21]** >> It can be. >> Can you talk about prompt layer and how

**[01:04:23]** >> Can you talk about prompt layer and how

**[01:04:23]** >> Can you talk about prompt layer and how can people help you?

**[01:04:24]** can people help you?

**[01:04:24]** can people help you? >> Yes, that's a good one. I forgot about

**[01:04:26]** >> Yes, that's a good one. I forgot about

**[01:04:26]** >> Yes, that's a good one. I forgot about that. Thank you.

**[01:04:29]** that. Thank you.

**[01:04:29]** that. Thank you. Um, so yeah, my one, we're hiring. Uh,

**[01:04:34]** Um, so yeah, my one, we're hiring. Uh,

**[01:04:34]** Um, so yeah, my one, we're hiring. Uh, so if you're looking for coding jobs at

**[01:04:38]** so if you're looking for coding jobs at

**[01:04:38]** so if you're looking for coding jobs at a very fun and fastmoving team in New

**[01:04:41]** a very fun and fastmoving team in New

**[01:04:41]** a very fun and fastmoving team in New York, you can reach out to me on X or

**[01:04:43]** York, you can reach out to me on X or

**[01:04:43]** York, you can reach out to me on X or email jaredprompter.com.

**[01:04:45]** email jaredprompter.com.

**[01:04:45]** email jaredprompter.com. We're based in New York. We are uh,

**[01:04:48]** We're based in New York. We are uh,

**[01:04:48]** We're based in New York. We are uh, yeah, we're we're a platform for

**[01:04:51]** yeah, we're we're a platform for

**[01:04:51]** yeah, we're we're a platform for building and testing AI products for

**[01:04:52]** building and testing AI products for

**[01:04:52]** building and testing AI products for prompt management, audibility,

**[01:04:54]** prompt management, audibility,

**[01:04:54]** prompt management, audibility, governance, all that fun stuff, but also

**[01:04:56]** governance, all that fun stuff, but also

**[01:04:56]** governance, all that fun stuff, but also logging and evals. And those screenshots

**[01:04:58]** logging and evals. And those screenshots

**[01:04:58]** logging and evals. And those screenshots I showed you came from prompt layer. If


### [01:05:00 - 01:06:00]

**[01:05:00]** I showed you came from prompt layer. If

**[01:05:00]** I showed you came from prompt layer. If you're building an AI application and

**[01:05:02]** you're building an AI application and

**[01:05:02]** you're building an AI application and you're building it with a team, you

**[01:05:03]** you're building it with a team, you

**[01:05:03]** you're building it with a team, you should probably try Problem layer. It'll

**[01:05:05]** should probably try Problem layer. It'll

**[01:05:05]** should probably try Problem layer. It'll make your life easier. Uh especially the

**[01:05:07]** make your life easier. Uh especially the

**[01:05:07]** make your life easier. Uh especially the bigger your team is, the more you want

**[01:05:08]** bigger your team is, the more you want

**[01:05:08]** bigger your team is, the more you want to collaborate, the more you want to

**[01:05:09]** to collaborate, the more you want to

**[01:05:10]** to collaborate, the more you want to collaborate with PMs and non-technical

**[01:05:12]** collaborate with PMs and non-technical

**[01:05:12]** collaborate with PMs and non-technical users and or if you're just technical

**[01:05:14]** users and or if you're just technical

**[01:05:14]** users and or if you're just technical users, it's a great tool. It'll make

**[01:05:15]** users, it's a great tool. It'll make

**[01:05:15]** users, it's a great tool. It'll make your life better. Highly recommend it.

**[01:05:17]** your life better. Highly recommend it.

**[01:05:17]** your life better. Highly recommend it. prompt layer.com and it's easy to do.

**[01:05:19]** prompt layer.com and it's easy to do.

**[01:05:20]** prompt layer.com and it's easy to do. And that was my show.

**[01:05:22]** And that was my show.

**[01:05:22]** And that was my show. Thank you for listening. [applause]

**[01:05:26]** Thank you for listening. [applause]

**[01:05:26]** Thank you for listening. [applause] [music]


