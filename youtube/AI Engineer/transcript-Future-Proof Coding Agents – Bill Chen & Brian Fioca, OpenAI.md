# Future-Proof Coding Agents – Bill Chen & Brian Fioca, OpenAI

**Video URL:** https://www.youtube.com/watch?v=wVl6ZjELpBk

---

## Full Transcript

### [00:00 - 01:00]

**[00:23]** Hello everyone. Um, today we'll be

**[00:23]** Hello everyone. Um, today we'll be talking about how to build coding

**[00:25]** talking about how to build coding

**[00:25]** talking about how to build coding agents.

**[00:27]** agents.

**[00:27]** agents. And uh, I'm Bill. I work on the applied

**[00:29]** And uh, I'm Bill. I work on the applied

**[00:29]** And uh, I'm Bill. I work on the applied AI startups team at OpenAI.

**[00:32]** AI startups team at OpenAI.

**[00:32]** AI startups team at OpenAI. >> And I'm Brian. I work with Bill on the

**[00:34]** >> And I'm Brian. I work with Bill on the

**[00:34]** >> And I'm Brian. I work with Bill on the OpenAI startups team.

**[00:35]** OpenAI startups team.

**[00:35]** OpenAI startups team. >> And we specifically uh focus on uh

**[00:38]** >> And we specifically uh focus on uh

**[00:38]** >> And we specifically uh focus on uh building coding agents here at OpenAI.

**[00:41]** building coding agents here at OpenAI.

**[00:41]** building coding agents here at OpenAI. Um yeah. So why are we talk giving this

**[00:44]** Um yeah. So why are we talk giving this

**[00:44]** Um yeah. So why are we talk giving this talk? Why why are we you know u talking

**[00:47]** talk? Why why are we you know u talking

**[00:48]** talk? Why why are we you know u talking about coding agents? Well, it's really

**[00:49]** about coding agents? Well, it's really

**[00:49]** about coding agents? Well, it's really quite interesting because it's been

**[00:51]** quite interesting because it's been

**[00:51]** quite interesting because it's been booming for the the the past year.

**[00:53]** booming for the the the past year.

**[00:54]** booming for the the the past year. Actually, it's just if you think about

**[00:55]** Actually, it's just if you think about

**[00:55]** Actually, it's just if you think about it, it's not that much time ago. like

**[00:57]** it, it's not that much time ago. like

**[00:57]** it, it's not that much time ago. like only have been a year or so. The ground

**[00:59]** only have been a year or so. The ground

**[00:59]** only have been a year or so. The ground keeps shifting really under the uh


### [01:00 - 02:00]

**[01:02]** keeps shifting really under the uh

**[01:02]** keeps shifting really under the uh harness on on the coding agents. But if

**[01:04]** harness on on the coding agents. But if

**[01:04]** harness on on the coding agents. But if you think about it, it's really like why

**[01:06]** you think about it, it's really like why

**[01:06]** you think about it, it's really like why it's interesting is because it's really

**[01:08]** it's interesting is because it's really

**[01:08]** it's interesting is because it's really a signal on how close we are to AGI.

**[01:10]** a signal on how close we are to AGI.

**[01:10]** a signal on how close we are to AGI. Software engineering can be set as a

**[01:12]** Software engineering can be set as a

**[01:12]** Software engineering can be set as a universal medium for problem solving.

**[01:15]** universal medium for problem solving.

**[01:15]** universal medium for problem solving. But because the ground is shifting so

**[01:16]** But because the ground is shifting so

**[01:16]** But because the ground is shifting so fast, uh we h kept having to rebuild the

**[01:19]** fast, uh we h kept having to rebuild the

**[01:20]** fast, uh we h kept having to rebuild the agent on top of the model whenever a

**[01:21]** agent on top of the model whenever a

**[01:21]** agent on top of the model whenever a model is released. And today we're going

**[01:23]** model is released. And today we're going

**[01:23]** model is released. And today we're going to talk a little bit about how we might

**[01:25]** to talk a little bit about how we might

**[01:25]** to talk a little bit about how we might be able to get around that.

**[01:29]** be able to get around that.

**[01:29]** be able to get around that. So here's what we're going to go over

**[01:31]** So here's what we're going to go over

**[01:31]** So here's what we're going to go over today. We'll start with the anatomy of a

**[01:33]** today. We'll start with the anatomy of a

**[01:33]** today. We'll start with the anatomy of a coding agent, especially going into the

**[01:35]** coding agent, especially going into the

**[01:35]** coding agent, especially going into the details of models and harnesses and how

**[01:38]** details of models and harnesses and how

**[01:38]** details of models and harnesses and how they work together. We'll share some

**[01:40]** they work together. We'll share some

**[01:40]** they work together. We'll share some lessons that we learned from putting

**[01:41]** lessons that we learned from putting

**[01:42]** lessons that we learned from putting them together ourselves. And we're

**[01:44]** them together ourselves. And we're

**[01:44]** them together ourselves. And we're specifically going to talk about codeex

**[01:46]** specifically going to talk about codeex

**[01:46]** specifically going to talk about codeex here, which is our own coding agent.

**[01:48]** here, which is our own coding agent.

**[01:48]** here, which is our own coding agent. We'll talk a little bit about emerging

**[01:50]** We'll talk a little bit about emerging

**[01:50]** We'll talk a little bit about emerging patterns that we're seeing from all of

**[01:52]** patterns that we're seeing from all of

**[01:52]** patterns that we're seeing from all of you for using agents like Codeex in your

**[01:54]** you for using agents like Codeex in your

**[01:54]** you for using agents like Codeex in your own products. And lastly, we'll talk a

**[01:57]** own products. And lastly, we'll talk a

**[01:57]** own products. And lastly, we'll talk a little bit about what to expect from

**[01:59]** little bit about what to expect from

**[01:59]** little bit about what to expect from Codeex in the future so that you can


### [02:00 - 03:00]

**[02:01]** Codeex in the future so that you can

**[02:01]** Codeex in the future so that you can build along with us if you want to.

**[02:09]** To start, let's talk a little bit about

**[02:09]** To start, let's talk a little bit about what makes a coding agent an agent as a

**[02:12]** what makes a coding agent an agent as a

**[02:12]** what makes a coding agent an agent as a whole. Um, it really is quite simple. I

**[02:15]** whole. Um, it really is quite simple. I

**[02:16]** whole. Um, it really is quite simple. I think you know people kind of over

**[02:17]** think you know people kind of over

**[02:17]** think you know people kind of over complicate things a little bit these

**[02:18]** complicate things a little bit these

**[02:18]** complicate things a little bit these days. It's made out of three parts. It's

**[02:20]** days. It's made out of three parts. It's

**[02:20]** days. It's made out of three parts. It's a user interface. It has a model. It's a

**[02:23]** a user interface. It has a model. It's a

**[02:23]** a user interface. It has a model. It's a harness, right? Uh the interface quite

**[02:26]** harness, right? Uh the interface quite

**[02:26]** harness, right? Uh the interface quite self-explanatory. Could be a computer uh

**[02:29]** self-explanatory. Could be a computer uh

**[02:30]** self-explanatory. Could be a computer uh like a CLI tool or it could be a uh

**[02:33]** like a CLI tool or it could be a uh

**[02:33]** like a CLI tool or it could be a uh integrated developer environment, could

**[02:35]** integrated developer environment, could

**[02:35]** integrated developer environment, could be also cloud or background agent. Um

**[02:38]** be also cloud or background agent. Um

**[02:38]** be also cloud or background agent. Um models also very quite self-explanatory

**[02:41]** models also very quite self-explanatory

**[02:41]** models also very quite self-explanatory are you know the things like the latest

**[02:43]** are you know the things like the latest

**[02:43]** are you know the things like the latest and greatest the GPD 5.1 codeex uh max

**[02:47]** and greatest the GPD 5.1 codeex uh max

**[02:47]** and greatest the GPD 5.1 codeex uh max that we just released yesterday uh or

**[02:50]** that we just released yesterday uh or

**[02:50]** that we just released yesterday uh or the GPD 5.1 series of models or other uh

**[02:54]** the GPD 5.1 series of models or other uh

**[02:54]** the GPD 5.1 series of models or other uh models from other providers as well. And

**[02:56]** models from other providers as well. And

**[02:56]** models from other providers as well. And the harness uh is a little bit more of

**[02:59]** the harness uh is a little bit more of

**[02:59]** the harness uh is a little bit more of an interesting part. This is the part


### [03:00 - 04:00]

**[03:01]** an interesting part. This is the part

**[03:01]** an interesting part. This is the part that directly interacts with the model

**[03:03]** that directly interacts with the model

**[03:03]** that directly interacts with the model uh in the most reductive way. You can

**[03:05]** uh in the most reductive way. You can

**[03:05]** uh in the most reductive way. You can sort of think of it as a collection of

**[03:06]** sort of think of it as a collection of

**[03:06]** sort of think of it as a collection of prompts and tools combined in a core

**[03:09]** prompts and tools combined in a core

**[03:09]** prompts and tools combined in a core agent loop which provides input and

**[03:11]** agent loop which provides input and

**[03:11]** agent loop which provides input and outputs uh from a model. Uh the last

**[03:15]** outputs uh from a model. Uh the last

**[03:15]** outputs uh from a model. Uh the last part will be our focus for today.

**[03:24]** As touched on a bit earlier, coding is

**[03:24]** As touched on a bit earlier, coding is one of the most active frontiers in

**[03:26]** one of the most active frontiers in

**[03:26]** one of the most active frontiers in applied AI and uh how models are

**[03:29]** applied AI and uh how models are

**[03:29]** applied AI and uh how models are constantly getting released and we're

**[03:30]** constantly getting released and we're

**[03:30]** constantly getting released and we're not making the problem uh easier for

**[03:32]** not making the problem uh easier for

**[03:32]** not making the problem uh easier for everybody

**[03:34]** everybody

**[03:34]** everybody is that people have to constantly adapt

**[03:38]** is that people have to constantly adapt

**[03:38]** is that people have to constantly adapt uh the agents to the new models.

**[03:47]** So, um, Bill's done a great job of

**[03:47]** So, um, Bill's done a great job of giving us an overview of coding agents,

**[03:49]** giving us an overview of coding agents,

**[03:49]** giving us an overview of coding agents, what they're made up of. So, let's zoom

**[03:52]** what they're made up of. So, let's zoom

**[03:52]** what they're made up of. So, let's zoom in a little bit on the harness. Um, it

**[03:55]** in a little bit on the harness. Um, it

**[03:55]** in a little bit on the harness. Um, it turns out that's a little bit tricky.

**[03:58]** turns out that's a little bit tricky.

**[03:58]** turns out that's a little bit tricky. So, what is a harness? A harness is


### [04:00 - 05:00]

**[04:00]** So, what is a harness? A harness is

**[04:00]** So, what is a harness? A harness is really the interface layer to the model.

**[04:03]** really the interface layer to the model.

**[04:03]** really the interface layer to the model. It's the surface area the model uses to

**[04:05]** It's the surface area the model uses to

**[04:05]** It's the surface area the model uses to talk to users and the code and perform

**[04:09]** talk to users and the code and perform

**[04:09]** talk to users and the code and perform actions with tools. It's made up of all

**[04:11]** actions with tools. It's made up of all

**[04:11]** actions with tools. It's made up of all of the pieces that the model needs to

**[04:14]** of the pieces that the model needs to

**[04:14]** of the pieces that the model needs to work over many turns, call tools, and

**[04:17]** work over many turns, call tools, and

**[04:17]** work over many turns, call tools, and and really write code for you and

**[04:19]** and really write code for you and

**[04:19]** and really write code for you and interpret what the user is actually

**[04:21]** interpret what the user is actually

**[04:21]** interpret what the user is actually asking. [snorts] Um, for some, the

**[04:24]** asking. [snorts] Um, for some, the

**[04:24]** asking. [snorts] Um, for some, the harness might actually be the special

**[04:26]** harness might actually be the special

**[04:26]** harness might actually be the special sauce of the product. But as we're going

**[04:29]** sauce of the product. But as we're going

**[04:29]** sauce of the product. But as we're going to go into a little bit more, it's

**[04:31]** to go into a little bit more, it's

**[04:31]** to go into a little bit more, it's really challenging work to build a good

**[04:33]** really challenging work to build a good

**[04:33]** really challenging work to build a good harness. And we'll talk about how we did

**[04:36]** harness. And we'll talk about how we did

**[04:36]** harness. And we'll talk about how we did that.

**[04:39]** that.

**[04:39]** that. So let's see what are some of these

**[04:40]** So let's see what are some of these

**[04:40]** So let's see what are some of these challenges. Um just to name a few, AV is

**[04:45]** challenges. Um just to name a few, AV is

**[04:45]** challenges. Um just to name a few, AV is one. Um your [laughter]

**[04:47]** one. Um your [laughter]

**[04:47]** one. Um your [laughter] um your brand new innovative custom tool

**[04:50]** um your brand new innovative custom tool

**[04:50]** um your brand new innovative custom tool that you're giving to your agent might

**[04:52]** that you're giving to your agent might

**[04:52]** that you're giving to your agent might not actually be something the model is

**[04:54]** not actually be something the model is

**[04:54]** not actually be something the model is using is used to using. It may not have

**[04:56]** using is used to using. It may not have

**[04:56]** using is used to using. It may not have ever seen that tool before in trading.

**[04:58]** ever seen that tool before in trading.

**[04:58]** ever seen that tool before in trading. And even if it is, you need to spend


### [05:00 - 06:00]

**[05:01]** And even if it is, you need to spend

**[05:01]** And even if it is, you need to spend time tuning your prompt to that

**[05:03]** time tuning your prompt to that

**[05:03]** time tuning your prompt to that particular model and the habits that it

**[05:06]** particular model and the habits that it

**[05:06]** particular model and the habits that it comes with.

**[05:07]** comes with.

**[05:07]** comes with. And new models are coming out all the

**[05:09]** And new models are coming out all the

**[05:09]** And new models are coming out all the time. What about latency? Like does the

**[05:12]** time. What about latency? Like does the

**[05:12]** time. What about latency? Like does the model take a while to think about

**[05:14]** model take a while to think about

**[05:14]** model take a while to think about certain things? Which things do you

**[05:16]** certain things? Which things do you

**[05:16]** certain things? Which things do you prompt it not to? How do you expose the

**[05:19]** prompt it not to? How do you expose the

**[05:19]** prompt it not to? How do you expose the UX of what a thinking model is doing

**[05:21]** UX of what a thinking model is doing

**[05:21]** UX of what a thinking model is doing while it's thinking? Is it communicating

**[05:24]** while it's thinking? Is it communicating

**[05:24]** while it's thinking? Is it communicating with you while it's thinking or do you

**[05:25]** with you while it's thinking or do you

**[05:25]** with you while it's thinking or do you have to summarize it? Managing the

**[05:27]** have to summarize it? Managing the

**[05:27]** have to summarize it? Managing the context window and compaction can be

**[05:30]** context window and compaction can be

**[05:30]** context window and compaction can be really challenging. We just launched

**[05:32]** really challenging. We just launched

**[05:32]** really challenging. We just launched Codeex Max that does that out of the box

**[05:35]** Codeex Max that does that out of the box

**[05:35]** Codeex Max that does that out of the box for you. you don't have to worry about

**[05:37]** for you. you don't have to worry about

**[05:37]** for you. you don't have to worry about compaction and context window

**[05:39]** compaction and context window

**[05:39]** compaction and context window management. It's really hard to do. Um,

**[05:42]** management. It's really hard to do. Um,

**[05:42]** management. It's really hard to do. Um, and so if you were to do it yourself,

**[05:44]** and so if you were to do it yourself,

**[05:44]** and so if you were to do it yourself, have fun. Um, and then also like the

**[05:46]** have fun. Um, and then also like the

**[05:46]** have fun. Um, and then also like the APIs keep changing, right? So we have

**[05:48]** APIs keep changing, right? So we have

**[05:48]** APIs keep changing, right? So we have completions, we have responses, we have

**[05:50]** completions, we have responses, we have

**[05:50]** completions, we have responses, we have whatever else is coming in the future.

**[05:52]** whatever else is coming in the future.

**[05:52]** whatever else is coming in the future. What does the model know how to use and

**[05:55]** What does the model know how to use and

**[05:55]** What does the model know how to use and get to get the most intelligence out of

**[05:56]** get to get the most intelligence out of

**[05:56]** get to get the most intelligence out of the box?

**[05:59]** the box?

**[05:59]** the box? And so


### [06:00 - 07:00]

**[06:01]** And so

**[06:01]** And so this is the interesting part. Fitting a

**[06:03]** this is the interesting part. Fitting a

**[06:03]** this is the interesting part. Fitting a model into a harness takes a lot of

**[06:05]** model into a harness takes a lot of

**[06:05]** model into a harness takes a lot of prompting.

**[06:07]** prompting.

**[06:07]** prompting. It turns out that how the model is

**[06:09]** It turns out that how the model is

**[06:09]** It turns out that how the model is trained has side effects.

**[06:12]** trained has side effects.

**[06:12]** trained has side effects. I like to think about it this way.

**[06:15]** I like to think about it this way.

**[06:15]** I like to think about it this way. Intelligence plus habit. Intelligence.

**[06:19]** Intelligence plus habit. Intelligence.

**[06:19]** Intelligence plus habit. Intelligence. What is the model good at? What

**[06:21]** What is the model good at? What

**[06:21]** What is the model good at? What languages does it know really well? What

**[06:23]** languages does it know really well? What

**[06:23]** languages does it know really well? What is what is its capabilities in terms of

**[06:26]** is what is its capabilities in terms of

**[06:26]** is what is its capabilities in terms of like how well it can write code in

**[06:28]** like how well it can write code in

**[06:28]** like how well it can write code in certain frameworks? And then what habits

**[06:32]** certain frameworks? And then what habits

**[06:32]** certain frameworks? And then what habits did it learn to to use to solve those

**[06:35]** did it learn to to use to solve those

**[06:35]** did it learn to to use to solve those problems? We've trained our models to

**[06:38]** problems? We've trained our models to

**[06:38]** problems? We've trained our models to have habits of like planning a solution,

**[06:42]** have habits of like planning a solution,

**[06:42]** have habits of like planning a solution, looking around, gathering context, and

**[06:44]** looking around, gathering context, and

**[06:44]** looking around, gathering context, and and thinking about a problem before

**[06:46]** and thinking about a problem before

**[06:46]** and thinking about a problem before diving in and writing code, and then

**[06:48]** diving in and writing code, and then

**[06:48]** diving in and writing code, and then testing its work at the end.

**[06:51]** testing its work at the end.

**[06:51]** testing its work at the end. Developing a feel for these habits is

**[06:54]** Developing a feel for these habits is

**[06:54]** Developing a feel for these habits is how you become a good prompt engineer.

**[06:57]** how you become a good prompt engineer.

**[06:57]** how you become a good prompt engineer. If you don't instruct the model in ways

**[06:59]** If you don't instruct the model in ways

**[06:59]** If you don't instruct the model in ways that it's familiar with, you can have


### [07:00 - 08:00]

**[07:02]** that it's familiar with, you can have

**[07:02]** that it's familiar with, you can have problems. We saw this when we launched

**[07:05]** problems. We saw this when we launched

**[07:05]** problems. We saw this when we launched GPD5. A lot of people who weren't used

**[07:07]** GPD5. A lot of people who weren't used

**[07:07]** GPD5. A lot of people who weren't used to using our models encoding tried to

**[07:10]** to using our models encoding tried to

**[07:10]** to using our models encoding tried to take prompts that existed for other

**[07:12]** take prompts that existed for other

**[07:12]** take prompts that existed for other models and put them into their harness

**[07:14]** models and put them into their harness

**[07:14]** models and put them into their harness and have GPD5 follow those instructions.

**[07:17]** and have GPD5 follow those instructions.

**[07:17]** and have GPD5 follow those instructions. And it turned out that we taught our

**[07:20]** And it turned out that we taught our

**[07:20]** And it turned out that we taught our model to do some of the things that the

**[07:22]** model to do some of the things that the

**[07:22]** model to do some of the things that the other models didn't really do out of the

**[07:24]** other models didn't really do out of the

**[07:24]** other models didn't really do out of the box. And so when they were prompting

**[07:26]** box. And so when they were prompting

**[07:26]** box. And so when they were prompting them to look really hard at the context

**[07:29]** them to look really hard at the context

**[07:29]** them to look really hard at the context and like examine every single file

**[07:31]** and like examine every single file

**[07:31]** and like examine every single file before making a a code edit, our model

**[07:35]** before making a a code edit, our model

**[07:35]** before making a a code edit, our model was being very kind of thorough about

**[07:37]** was being very kind of thorough about

**[07:38]** was being very kind of thorough about that and it was taking a really long

**[07:39]** that and it was taking a really long

**[07:39]** that and it was taking a really long time and they weren't seeing the best

**[07:40]** time and they weren't seeing the best

**[07:40]** time and they weren't seeing the best performance. And so we figured out that

**[07:44]** performance. And so we figured out that

**[07:44]** performance. And so we figured out that if you let the model just do the

**[07:46]** if you let the model just do the

**[07:46]** if you let the model just do the behaviors that it's used to and don't

**[07:47]** behaviors that it's used to and don't

**[07:47]** behaviors that it's used to and don't overprompt it, it'll actually perform

**[07:50]** overprompt it, it'll actually perform

**[07:50]** overprompt it, it'll actually perform really better. We found out by asking. I

**[07:52]** really better. We found out by asking. I

**[07:52]** really better. We found out by asking. I was literally like, "Hey, like I like

**[07:54]** was literally like, "Hey, like I like

**[07:54]** was literally like, "Hey, like I like the solution, but it took you a long

**[07:55]** the solution, but it took you a long

**[07:55]** the solution, but it took you a long time to get there. What can I do

**[07:58]** time to get there. What can I do

**[07:58]** time to get there. What can I do differently in your instructions to help


### [08:00 - 09:00]

**[08:00]** differently in your instructions to help

**[08:00]** differently in your instructions to help you get there faster next time?" And

**[08:01]** you get there faster next time?" And

**[08:01]** you get there faster next time?" And literally it said, "Uh, you're telling

**[08:03]** literally it said, "Uh, you're telling

**[08:03]** literally it said, "Uh, you're telling me to go look at everything and I don't

**[08:05]** me to go look at everything and I don't

**[08:05]** me to go look at everything and I don't really need to. So that's what's taking

**[08:07]** really need to. So that's what's taking

**[08:07]** really need to. So that's what's taking forever."

**[08:14]** And so you can actually see the

**[08:14]** And so you can actually see the advantages of building both the model

**[08:16]** advantages of building both the model

**[08:16]** advantages of building both the model and the harness together because you

**[08:17]** and the harness together because you

**[08:17]** and the harness together because you just like know all of that while you're

**[08:19]** just like know all of that while you're

**[08:19]** just like know all of that while you're building it. And that's why Codex is

**[08:22]** building it. And that's why Codex is

**[08:22]** building it. And that's why Codex is both a model and a harness combined.

**[08:25]** both a model and a harness combined.

**[08:25]** both a model and a harness combined. So let's dig deeper into Codeex and what

**[08:28]** So let's dig deeper into Codeex and what

**[08:28]** So let's dig deeper into Codeex and what it can actually do.

**[08:31]** it can actually do.

**[08:31]** it can actually do. So we built Codex to be an agent for

**[08:33]** So we built Codex to be an agent for

**[08:33]** So we built Codex to be an agent for everywhere that you code. It's a VS Code

**[08:36]** everywhere that you code. It's a VS Code

**[08:36]** everywhere that you code. It's a VS Code plugin. It's a CLI. You can call it in

**[08:38]** plugin. It's a CLI. You can call it in

**[08:38]** plugin. It's a CLI. You can call it in the cloud from the VS Code plugin or

**[08:41]** the cloud from the VS Code plugin or

**[08:41]** the cloud from the VS Code plugin or from chatgbt from your phone. Um, and

**[08:44]** from chatgbt from your phone. Um, and

**[08:44]** from chatgbt from your phone. Um, and it's very basic. You can use it to turn

**[08:46]** it's very basic. You can use it to turn

**[08:46]** it's very basic. You can use it to turn your specs into runnable code starting

**[08:48]** your specs into runnable code starting

**[08:48]** your specs into runnable code starting from a prompt. Um, having a plan. It

**[08:52]** from a prompt. Um, having a plan. It

**[08:52]** from a prompt. Um, having a plan. It navigates your repo to edit files. It

**[08:54]** navigates your repo to edit files. It

**[08:54]** navigates your repo to edit files. It runs commands, executes tasks, and you

**[08:57]** runs commands, executes tasks, and you

**[08:57]** runs commands, executes tasks, and you can call it from Slack or you can have


### [09:00 - 10:00]

**[09:00]** can call it from Slack or you can have

**[09:00]** can call it from Slack or you can have it review PRs and GitHub. So, all of the

**[09:03]** it review PRs and GitHub. So, all of the

**[09:03]** it review PRs and GitHub. So, all of the things that you would expect.

**[09:06]** things that you would expect.

**[09:06]** things that you would expect. And that means that the that codec um

**[09:09]** And that means that the that codec um

**[09:09]** And that means that the that codec um the harness of codec needs to be able to

**[09:10]** the harness of codec needs to be able to

**[09:10]** the harness of codec needs to be able to do a lot of really complex things. Uh

**[09:14]** do a lot of really complex things. Uh

**[09:14]** do a lot of really complex things. Uh when I talked to a member of the codeex

**[09:16]** when I talked to a member of the codeex

**[09:16]** when I talked to a member of the codeex team about this slide and what should be

**[09:18]** team about this slide and what should be

**[09:18]** team about this slide and what should be on it, he was like it's way harder than

**[09:20]** on it, he was like it's way harder than

**[09:20]** on it, he was like it's way harder than you think. You have to manage parallel

**[09:23]** you think. You have to manage parallel

**[09:23]** you think. You have to manage parallel tool calls like thread merging and all

**[09:25]** tool calls like thread merging and all

**[09:25]** tool calls like thread merging and all of the things involved in that. Think

**[09:27]** of the things involved in that. Think

**[09:27]** of the things involved in that. Think about all the security considerations

**[09:28]** about all the security considerations

**[09:28]** about all the security considerations you have with sandboxing, prompt

**[09:30]** you have with sandboxing, prompt

**[09:30]** you have with sandboxing, prompt forwarding, permissions, uh, port

**[09:33]** forwarding, permissions, uh, port

**[09:33]** forwarding, permissions, uh, port management. Um, compaction is a whole

**[09:36]** management. Um, compaction is a whole

**[09:36]** management. Um, compaction is a whole thing. Um, and doing that well is really

**[09:39]** thing. Um, and doing that well is really

**[09:39]** thing. Um, and doing that well is really complex. When do you trigger compaction?

**[09:41]** complex. When do you trigger compaction?

**[09:41]** complex. When do you trigger compaction? When do you reinject? How do you worry

**[09:43]** When do you reinject? How do you worry

**[09:43]** When do you reinject? How do you worry about uh cache optimization during that

**[09:45]** about uh cache optimization during that

**[09:45]** about uh cache optimization during that MCP, right? Like all of the uh plumbing

**[09:49]** MCP, right? Like all of the uh plumbing

**[09:49]** MCP, right? Like all of the uh plumbing you have to build for MCP support into

**[09:51]** you have to build for MCP support into

**[09:51]** you have to build for MCP support into the harness. Uh, and then not even

**[09:53]** the harness. Uh, and then not even

**[09:54]** the harness. Uh, and then not even mentioning images and what's the

**[09:56]** mentioning images and what's the

**[09:56]** mentioning images and what's the resolution that you need to compress

**[09:57]** resolution that you need to compress

**[09:57]** resolution that you need to compress them to to send them to the model. All

**[09:58]** them to to send them to the model. All

**[09:58]** them to to send them to the model. All this all of this is like work that you


### [10:00 - 11:00]

**[10:00]** this all of this is like work that you

**[10:00]** this all of this is like work that you have to do if you're going to build this

**[10:01]** have to do if you're going to build this

**[10:01]** have to do if you're going to build this from scratch and keep it updated as new

**[10:04]** from scratch and keep it updated as new

**[10:04]** from scratch and keep it updated as new features come online.

**[10:10]** So since we've bundled all of these

**[10:10]** So since we've bundled all of these features together for you in an agent

**[10:13]** features together for you in an agent

**[10:13]** features together for you in an agent that can safely write its own tools to

**[10:16]** that can safely write its own tools to

**[10:16]** that can safely write its own tools to solve new problems that it encounters.

**[10:20]** solve new problems that it encounters.

**[10:20]** solve new problems that it encounters. Oops.

**[10:22]** Oops.

**[10:22]** Oops. Uh we actually have here uh a computer

**[10:26]** Uh we actually have here uh a computer

**[10:26]** Uh we actually have here uh a computer use agent for the terminal.

**[10:36]** Wow, that sounds quite a bit powerful

**[10:36]** Wow, that sounds quite a bit powerful than just plain old coding agent,

**[10:38]** than just plain old coding agent,

**[10:38]** than just plain old coding agent, doesn't it? Um but just think about it

**[10:41]** doesn't it? Um but just think about it

**[10:41]** doesn't it? Um but just think about it again. Well, before browser and graphic

**[10:43]** again. Well, before browser and graphic

**[10:43]** again. Well, before browser and graphic user interface was a thing, wasn't that

**[10:45]** user interface was a thing, wasn't that

**[10:45]** user interface was a thing, wasn't that how we always operate a computer?

**[10:47]** how we always operate a computer?

**[10:47]** how we always operate a computer? they're writing code and chain them

**[10:48]** they're writing code and chain them

**[10:48]** they're writing code and chain them together in a command line interface. So

**[10:51]** together in a command line interface. So

**[10:51]** together in a command line interface. So that means if you can express your tasks

**[10:53]** that means if you can express your tasks

**[10:53]** that means if you can express your tasks in command line as well as files tasks

**[10:57]** in command line as well as files tasks

**[10:57]** in command line as well as files tasks codeex will be able to know what to do.


### [11:00 - 12:00]

**[11:00]** codeex will be able to know what to do.

**[11:00]** codeex will be able to know what to do. Um the example is I like to use codeex

**[11:03]** Um the example is I like to use codeex

**[11:03]** Um the example is I like to use codeex to organize a lot of the photos from my

**[11:05]** to organize a lot of the photos from my

**[11:05]** to organize a lot of the photos from my desktop into a folder and that's a very

**[11:08]** desktop into a folder and that's a very

**[11:08]** desktop into a folder and that's a very simple use case but what it can also do

**[11:11]** simple use case but what it can also do

**[11:11]** simple use case but what it can also do is it can analyze huge amounts of CSV

**[11:13]** is it can analyze huge amounts of CSV

**[11:13]** is it can analyze huge amounts of CSV files inside of a folder uh doing data

**[11:16]** files inside of a folder uh doing data

**[11:16]** files inside of a folder uh doing data analysis it does not have to be a coding

**[11:19]** analysis it does not have to be a coding

**[11:19]** analysis it does not have to be a coding task and if it can be accomplished by

**[11:21]** task and if it can be accomplished by

**[11:21]** task and if it can be accomplished by running tools from command line you can

**[11:23]** running tools from command line you can

**[11:23]** running tools from command line you can use codeex

**[11:24]** use codeex

**[11:24]** use codeex so now that we see codeex is such a cool

**[11:27]** so now that we see codeex is such a cool

**[11:27]** so now that we see codeex is such a cool harness um I want to also share a little

**[11:30]** harness um I want to also share a little

**[11:30]** harness um I want to also share a little a bit about how you can use it to build

**[11:32]** a bit about how you can use it to build

**[11:32]** a bit about how you can use it to build your own agents. And what you can do is

**[11:34]** your own agents. And what you can do is

**[11:34]** your own agents. And what you can do is you can use codeex [clears throat]

**[11:36]** you can use codeex [clears throat]

**[11:36]** you can use codeex [clears throat] the agent inside of your own agent.

**[11:41]** the agent inside of your own agent.

**[11:41]** the agent inside of your own agent. Um, how does that work? Well, if you

**[11:44]** Um, how does that work? Well, if you

**[11:44]** Um, how does that work? Well, if you want to build uh a coding uh the next

**[11:48]** want to build uh a coding uh the next

**[11:48]** want to build uh a coding uh the next coding startup, we don't really have all

**[11:50]** coding startup, we don't really have all

**[11:50]** coding startup, we don't really have all the answers, but we do have a few

**[11:52]** the answers, but we do have a few

**[11:52]** the answers, but we do have a few patterns uh that we thought uh might

**[11:55]** patterns uh that we thought uh might

**[11:55]** patterns uh that we thought uh might help you having worked with some of the

**[11:57]** help you having worked with some of the

**[11:57]** help you having worked with some of the top coding customers uh like cursor and

**[11:59]** top coding customers uh like cursor and

**[11:59]** top coding customers uh like cursor and VS code. Uh one of those patterns is uh


### [12:00 - 13:00]

**[12:03]** VS code. Uh one of those patterns is uh

**[12:03]** VS code. Uh one of those patterns is uh harness becoming the new abstraction

**[12:05]** harness becoming the new abstraction

**[12:05]** harness becoming the new abstraction layer. The benefits of this is quite

**[12:08]** layer. The benefits of this is quite

**[12:08]** layer. The benefits of this is quite obvious. Um, you no longer have to care

**[12:11]** obvious. Um, you no longer have to care

**[12:11]** obvious. Um, you no longer have to care about prioritize optimizing the prompt

**[12:14]** about prioritize optimizing the prompt

**[12:14]** about prioritize optimizing the prompt and tools with every model upgrade.

**[12:18]** and tools with every model upgrade.

**[12:18]** and tools with every model upgrade. [snorts]

**[12:18]** [snorts]

**[12:18]** [snorts] >> But, um, does that mean you're just

**[12:19]** >> But, um, does that mean you're just

**[12:20]** >> But, um, does that mean you're just building a wrapper?

**[12:21]** building a wrapper?

**[12:21]** building a wrapper? >> Well, I disagree with that take.

**[12:24]** >> Well, I disagree with that take.

**[12:24]** >> Well, I disagree with that take. I disagree. I was disagreeing with my

**[12:27]** I disagree. I was disagreeing with my

**[12:27]** I disagree. I was disagreeing with my colleague here. Um, just like how

**[12:29]** colleague here. Um, just like how

**[12:29]** colleague here. Um, just like how building rappers on top of models I

**[12:31]** building rappers on top of models I

**[12:31]** building rappers on top of models I think is really reductive on uh on the

**[12:35]** think is really reductive on uh on the

**[12:35]** think is really reductive on uh on the whole value prop of the infrastructure

**[12:37]** whole value prop of the infrastructure

**[12:37]** whole value prop of the infrastructure layer. Sorry, I used to be a VC.

**[12:39]** layer. Sorry, I used to be a VC.

**[12:39]** layer. Sorry, I used to be a VC. [laughter]

**[12:40]** [laughter]

**[12:40]** [laughter] >> Focusing most of your efforts on

**[12:42]** >> Focusing most of your efforts on

**[12:42]** >> Focusing most of your efforts on differentiating your product is what

**[12:44]** differentiating your product is what

**[12:44]** differentiating your product is what this pattern allows you to do. And

**[12:47]** this pattern allows you to do. And

**[12:47]** this pattern allows you to do. And that's where most of the value lies.

**[12:54]** Exactly. Okay. So, let's look at some of

**[12:54]** Exactly. Okay. So, let's look at some of these patterns that we've seen and

**[12:56]** these patterns that we've seen and

**[12:56]** these patterns that we've seen and actually have helped our customers build

**[12:59]** actually have helped our customers build

**[12:59]** actually have helped our customers build um along with them. Codeex is an SDK. It


### [13:00 - 14:00]

**[13:03]** um along with them. Codeex is an SDK. It

**[13:03]** um along with them. Codeex is an SDK. It can be called through a TypeScript

**[13:04]** can be called through a TypeScript

**[13:04]** can be called through a TypeScript library. You can call it

**[13:06]** library. You can call it

**[13:06]** library. You can call it programmatically and a Python exec.

**[13:08]** programmatically and a Python exec.

**[13:08]** programmatically and a Python exec. There's a GitHub action that you can

**[13:10]** There's a GitHub action that you can

**[13:10]** There's a GitHub action that you can plug into to have it merge merge

**[13:13]** plug into to have it merge merge

**[13:13]** plug into to have it merge merge conflicts on PRs that everybody hates

**[13:15]** conflicts on PRs that everybody hates

**[13:15]** conflicts on PRs that everybody hates doing. Then uh you can also add it to

**[13:19]** doing. Then uh you can also add it to

**[13:19]** doing. Then uh you can also add it to the agents SDK and give it MCP

**[13:22]** the agents SDK and give it MCP

**[13:22]** the agents SDK and give it MCP connectors back to your product. So now

**[13:24]** connectors back to your product. So now

**[13:24]** connectors back to your product. So now you have an agent. I like to say we

**[13:26]** you have an agent. I like to say we

**[13:26]** you have an agent. I like to say we started with chat bots that you can talk

**[13:28]** started with chat bots that you can talk

**[13:28]** started with chat bots that you can talk to. Then we gave the chatbots tools to

**[13:31]** to. Then we gave the chatbots tools to

**[13:31]** to. Then we gave the chatbots tools to use. And then now you can give uh a tool

**[13:35]** use. And then now you can give uh a tool

**[13:35]** use. And then now you can give uh a tool to your chatbot that can make other

**[13:38]** to your chatbot that can make other

**[13:38]** to your chatbot that can make other tools that it doesn't have. And so now

**[13:41]** tools that it doesn't have. And so now

**[13:41]** tools that it doesn't have. And so now you can actually build out enterprise

**[13:43]** you can actually build out enterprise

**[13:43]** you can actually build out enterprise software that does it that writes its

**[13:45]** software that does it that writes its

**[13:45]** software that does it that writes its own plug-in connectors to the API level

**[13:48]** own plug-in connectors to the API level

**[13:48]** own plug-in connectors to the API level for each customer on the spot. That's

**[13:51]** for each customer on the spot. That's

**[13:51]** for each customer on the spot. That's something that a professional services

**[13:52]** something that a professional services

**[13:52]** something that a professional services team used to have to do. Um, so you have

**[13:55]** team used to have to do. Um, so you have

**[13:55]** team used to have to do. Um, so you have fully customizable software that can now

**[13:57]** fully customizable software that can now

**[13:57]** fully customizable software that can now talk back to itself. Um, I made a conbon


### [14:00 - 15:00]

**[14:00]** talk back to itself. Um, I made a conbon

**[14:00]** talk back to itself. Um, I made a conbon board for dev day that can actually fix

**[14:02]** board for dev day that can actually fix

**[14:02]** board for dev day that can actually fix its own bugs. Um, it's pretty fun. And

**[14:05]** its own bugs. Um, it's pretty fun. And

**[14:05]** its own bugs. Um, it's pretty fun. And then lastly, um, you can actually do

**[14:08]** then lastly, um, you can actually do

**[14:08]** then lastly, um, you can actually do something like what Zed has done. They

**[14:09]** something like what Zed has done. They

**[14:10]** something like what Zed has done. They have just decided to wrap codeex inside

**[14:13]** have just decided to wrap codeex inside

**[14:13]** have just decided to wrap codeex inside of a layer and give it an interface to

**[14:15]** of a layer and give it an interface to

**[14:15]** of a layer and give it an interface to the IDE for talking back and forth for

**[14:18]** the IDE for talking back and forth for

**[14:18]** the IDE for talking back and forth for the user and making code edits. And now

**[14:21]** the user and making code edits. And now

**[14:21]** the user and making code edits. And now they don't actually have to do all the

**[14:22]** they don't actually have to do all the

**[14:22]** they don't actually have to do all the work of staying on top of all of the

**[14:24]** work of staying on top of all of the

**[14:24]** work of staying on top of all of the things that we're good at doing and they

**[14:26]** things that we're good at doing and they

**[14:26]** things that we're good at doing and they can focus on building like the best code

**[14:28]** can focus on building like the best code

**[14:28]** can focus on building like the best code editor.

**[14:34]** Uh so our top coding partners like

**[14:34]** Uh so our top coding partners like GitHub has used this uh to great effect

**[14:37]** GitHub has used this uh to great effect

**[14:37]** GitHub has used this uh to great effect and well uh we've created an SDK uh for

**[14:41]** and well uh we've created an SDK uh for

**[14:41]** and well uh we've created an SDK uh for it that they used to directly integrate

**[14:43]** it that they used to directly integrate

**[14:43]** it that they used to directly integrate uh with codeex. You can also use the SDK

**[14:46]** uh with codeex. You can also use the SDK

**[14:46]** uh with codeex. You can also use the SDK to uh control codecs as part of your

**[14:48]** to uh control codecs as part of your

**[14:48]** to uh control codecs as part of your CI/CD pipeline as well as use it as an

**[14:51]** CI/CD pipeline as well as use it as an

**[14:51]** CI/CD pipeline as well as use it as an agent that directly interacts with your

**[14:54]** agent that directly interacts with your

**[14:54]** agent that directly interacts with your own agent as well. Uh [clears throat] if

**[14:56]** own agent as well. Uh [clears throat] if

**[14:56]** own agent as well. Uh [clears throat] if you really want to customize the agent

**[14:59]** you really want to customize the agent

**[14:59]** you really want to customize the agent layer, you can do it too. As an example


### [15:00 - 16:00]

**[15:01]** layer, you can do it too. As an example

**[15:01]** layer, you can do it too. As an example of this, we worked with closely with the

**[15:03]** of this, we worked with closely with the

**[15:03]** of this, we worked with closely with the cursor team to get the best performance

**[15:05]** cursor team to get the best performance

**[15:05]** cursor team to get the best performance out of the codecs. The model, not the

**[15:07]** out of the codecs. The model, not the

**[15:07]** out of the codecs. The model, not the agent, we're bad at naming things. The

**[15:08]** agent, we're bad at naming things. The

**[15:08]** agent, we're bad at naming things. The model is different from the agent. They

**[15:11]** model is different from the agent. They

**[15:11]** model is different from the agent. They did so by aligning their tools to be in

**[15:13]** did so by aligning their tools to be in

**[15:13]** did so by aligning their tools to be in distribution with how the model is

**[15:15]** distribution with how the model is

**[15:15]** distribution with how the model is trained and they did so by aligning uh

**[15:17]** trained and they did so by aligning uh

**[15:17]** trained and they did so by aligning uh their harness with our open- source uh

**[15:20]** their harness with our open- source uh

**[15:20]** their harness with our open- source uh implementation of codeex CLI. All of

**[15:22]** implementation of codeex CLI. All of

**[15:22]** implementation of codeex CLI. All of this is publicly available. Uh you can

**[15:25]** this is publicly available. Uh you can

**[15:25]** this is publicly available. Uh you can fork the repo, you can use our source

**[15:28]** fork the repo, you can use our source

**[15:28]** fork the repo, you can use our source code, you can use it. Uh go nuts.

**[15:37]** So what does the future hold for Codeex?

**[15:37]** So what does the future hold for Codeex? It hasn't even been out for a year. Um

**[15:40]** It hasn't even been out for a year. Um

**[15:40]** It hasn't even been out for a year. Um and especially with the lo la la la la

**[15:41]** la la la la la la la la la la la la la la la la la la la la la la la la la la

**[15:41]** la la la la la la la la la la la la la

**[15:41]** la la la la la la la la la la la la la la la la la la la la la la launch of CEX

**[15:42]** la la la la la la la la la launch of CEX

**[15:42]** la la la la la la la la la launch of CEX match yesterday like things are really

**[15:44]** match yesterday like things are really

**[15:44]** match yesterday like things are really changing fast. Uh it's the fastest

**[15:46]** changing fast. Uh it's the fastest

**[15:46]** changing fast. Uh it's the fastest growing model in usage now serving

**[15:49]** growing model in usage now serving

**[15:49]** growing model in usage now serving dozens of trillions of tokens per week

**[15:52]** dozens of trillions of tokens per week

**[15:52]** dozens of trillions of tokens per week which has actually doubled since dev

**[15:54]** which has actually doubled since dev

**[15:54]** which has actually doubled since dev day.

**[15:57]** day.

**[15:57]** day. It's always good to build where the

**[15:59]** It's always good to build where the

**[15:59]** It's always good to build where the models are going. It's safe to assume


### [16:00 - 17:00]

**[16:01]** models are going. It's safe to assume

**[16:01]** models are going. It's safe to assume that the models will get better. They'll

**[16:04]** that the models will get better. They'll

**[16:04]** that the models will get better. They'll be able to get to work on much longer

**[16:06]** be able to get to work on much longer

**[16:06]** be able to get to work on much longer horizon tasks unsupervised.

**[16:09]** horizon tasks unsupervised.

**[16:09]** horizon tasks unsupervised. New models will raise the trust ceiling.

**[16:12]** New models will raise the trust ceiling.

**[16:12]** New models will raise the trust ceiling. I trust these models now to do some way

**[16:15]** I trust these models now to do some way

**[16:15]** I trust these models now to do some way harder work than I would have 6 months

**[16:16]** harder work than I would have 6 months

**[16:16]** harder work than I would have 6 months ago. And that's going to keep

**[16:18]** ago. And that's going to keep

**[16:18]** ago. And that's going to keep increasing. The future is about

**[16:21]** increasing. The future is about

**[16:21]** increasing. The future is about sprawling code bases and non-standard

**[16:23]** sprawling code bases and non-standard

**[16:23]** sprawling code bases and non-standard libraries and knowing how to work in

**[16:24]** libraries and knowing how to work in

**[16:24]** libraries and knowing how to work in closed source environments, matching

**[16:26]** closed source environments, matching

**[16:26]** closed source environments, matching existing templates and practices

**[16:29]** existing templates and practices

**[16:29]** existing templates and practices and the models uh and and and so you can

**[16:32]** and the models uh and and and so you can

**[16:32]** and the models uh and and and so you can imagine that the SDK will evolve to

**[16:34]** imagine that the SDK will evolve to

**[16:34]** imagine that the SDK will evolve to better support these model capabilities,

**[16:37]** better support these model capabilities,

**[16:37]** better support these model capabilities, letting the model learn as it goes and

**[16:39]** letting the model learn as it goes and

**[16:39]** letting the model learn as it goes and not repeat mistakes and generally

**[16:41]** not repeat mistakes and generally

**[16:41]** not repeat mistakes and generally provide more surface area for an agent

**[16:44]** provide more surface area for an agent

**[16:44]** provide more surface area for an agent that writes code and uses a terminal to

**[16:48]** that writes code and uses a terminal to

**[16:48]** that writes code and uses a terminal to solve whatever problems it encounters.

**[16:49]** solve whatever problems it encounters.

**[16:49]** solve whatever problems it encounters. counters and you can use that in your

**[16:52]** counters and you can use that in your

**[16:52]** counters and you can use that in your products via the SDK.

**[16:56]** products via the SDK.

**[16:56]** products via the SDK. So, what have we learned? Harnesses are

**[16:59]** So, what have we learned? Harnesses are

**[16:59]** So, what have we learned? Harnesses are really complicated and take a lot of


### [17:00 - 18:00]

**[17:01]** really complicated and take a lot of

**[17:01]** really complicated and take a lot of work to maintain, especially with all

**[17:02]** work to maintain, especially with all

**[17:02]** work to maintain, especially with all the new models coming out. So, we've

**[17:05]** the new models coming out. So, we've

**[17:05]** the new models coming out. So, we've built one for you inside of Codeex that

**[17:07]** built one for you inside of Codeex that

**[17:07]** built one for you inside of Codeex that you can use off the shelf or look at the

**[17:10]** you can use off the shelf or look at the

**[17:10]** you can use off the shelf or look at the source if you want to and you can use it

**[17:13]** source if you want to and you can use it

**[17:13]** source if you want to and you can use it to build new things outside of coding

**[17:16]** to build new things outside of coding

**[17:16]** to build new things outside of coding and let us do all of the work making

**[17:18]** and let us do all of the work making

**[17:18]** and let us do all of the work making sure that you have the most capable

**[17:19]** sure that you have the most capable

**[17:19]** sure that you have the most capable computer agent.

**[17:21]** computer agent.

**[17:21]** computer agent. And we're really excited to see what you

**[17:23]** And we're really excited to see what you

**[17:24]** And we're really excited to see what you craft.


