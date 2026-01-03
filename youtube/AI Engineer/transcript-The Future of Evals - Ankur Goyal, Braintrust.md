# The Future of Evals - Ankur Goyal, Braintrust

**Video URL:** https://www.youtube.com/watch?v=MC55hdWLq4o

---

## Full Transcript

### [00:00 - 01:00]

**[00:24]** Awesome. Uh so today we're going to talk

**[00:24]** Awesome. Uh so today we're going to talk a little bit about evals to date and

**[00:26]** a little bit about evals to date and

**[00:26]** a little bit about evals to date and where we think eval are going to be

**[00:28]** where we think eval are going to be

**[00:28]** where we think eval are going to be going in the future.

**[00:32]** going in the future.

**[00:32]** going in the future. Also for those of you who saw my brother

**[00:34]** Also for those of you who saw my brother

**[00:34]** Also for those of you who saw my brother earlier um I'm going to do my best to

**[00:36]** earlier um I'm going to do my best to

**[00:36]** earlier um I'm going to do my best to live up to his energy and uh and

**[00:38]** live up to his energy and uh and

**[00:38]** live up to his energy and uh and charisma.

**[00:44]** But um yeah, you know, it's been an

**[00:44]** But um yeah, you know, it's been an amazing almost two-year journey for us

**[00:46]** amazing almost two-year journey for us

**[00:46]** amazing almost two-year journey for us at Brain Trust. We have had the

**[00:48]** at Brain Trust. We have had the

**[00:48]** at Brain Trust. We have had the opportunity to work with some of the

**[00:50]** opportunity to work with some of the

**[00:50]** opportunity to work with some of the most amazing companies building um I

**[00:52]** most amazing companies building um I

**[00:52]** most amazing companies building um I think the best AI products in the world.

**[00:55]** think the best AI products in the world.

**[00:55]** think the best AI products in the world. Uh I'm blown away by how many EVLs

**[00:58]** Uh I'm blown away by how many EVLs

**[00:58]** Uh I'm blown away by how many EVLs people actually run on the product. The


### [01:00 - 02:00]

**[01:00]** people actually run on the product. The

**[01:00]** people actually run on the product. The average org that signs up for Brain

**[01:02]** average org that signs up for Brain

**[01:02]** average org that signs up for Brain Trust runs almost 13 EVELs a day. Some

**[01:06]** Trust runs almost 13 EVELs a day. Some

**[01:06]** Trust runs almost 13 EVELs a day. Some of our customers run more than 3,000

**[01:09]** of our customers run more than 3,000

**[01:09]** of our customers run more than 3,000 EVELs a day. uh and some of the most

**[01:12]** EVELs a day. uh and some of the most

**[01:12]** EVELs a day. uh and some of the most advanced companies that are running

**[01:14]** advanced companies that are running

**[01:14]** advanced companies that are running EVELs are spending more than two hours

**[01:17]** EVELs are spending more than two hours

**[01:17]** EVELs are spending more than two hours in the product every day working through

**[01:19]** in the product every day working through

**[01:19]** in the product every day working through their evals. And I think one of the

**[01:21]** their evals. And I think one of the

**[01:21]** their evals. And I think one of the things that stands out to me is while we

**[01:25]** things that stands out to me is while we

**[01:25]** things that stands out to me is while we have customers building some of the

**[01:27]** have customers building some of the

**[01:27]** have customers building some of the coolest most automated

**[01:29]** coolest most automated

**[01:29]** coolest most automated um AI based products and agents in the

**[01:32]** um AI based products and agents in the

**[01:32]** um AI based products and agents in the world eval

**[01:41]** the best thing you can do is look at a

**[01:41]** the best thing you can do is look at a dashboard and I think we have a pretty

**[01:43]** dashboard and I think we have a pretty

**[01:43]** dashboard and I think we have a pretty cool dashboard in Brain Trust but still

**[01:45]** cool dashboard in Brain Trust but still

**[01:45]** cool dashboard in Brain Trust but still it's just a dashboard that you look at

**[01:47]** it's just a dashboard that you look at

**[01:47]** it's just a dashboard that you look at and you walk away and think okay what

**[01:49]** and you walk away and think okay what

**[01:49]** and you walk away and think okay what changes can I make to my code or to my

**[01:52]** changes can I make to my code or to my

**[01:52]** changes can I make to my code or to my prompts so that this eval does better.

**[01:55]** prompts so that this eval does better.

**[01:55]** prompts so that this eval does better. Um, and I actually think that is all

**[01:57]** Um, and I actually think that is all

**[01:57]** Um, and I actually think that is all going to change.

**[01:59]** going to change.

**[01:59]** going to change. Uh, so today I'm excited to talk about


### [02:00 - 03:00]

**[02:02]** Uh, so today I'm excited to talk about

**[02:02]** Uh, so today I'm excited to talk about something called loop. Loop is an agent

**[02:04]** something called loop. Loop is an agent

**[02:04]** something called loop. Loop is an agent that we've been working on for some time

**[02:06]** that we've been working on for some time

**[02:06]** that we've been working on for some time now that's built into brain trust. Um,

**[02:09]** now that's built into brain trust. Um,

**[02:09]** now that's built into brain trust. Um, and it's actually only possible because

**[02:11]** and it's actually only possible because

**[02:11]** and it's actually only possible because of evals. Every quarter for the last two

**[02:14]** of evals. Every quarter for the last two

**[02:14]** of evals. Every quarter for the last two years, we've run evals on the frontier

**[02:17]** years, we've run evals on the frontier

**[02:17]** years, we've run evals on the frontier models to see how good they are at

**[02:19]** models to see how good they are at

**[02:19]** models to see how good they are at actually improving prompts, improving

**[02:21]** actually improving prompts, improving

**[02:21]** actually improving prompts, improving data sets, and improving scorers. And

**[02:24]** data sets, and improving scorers. And

**[02:24]** data sets, and improving scorers. And until very, very recently, they actually

**[02:25]** until very, very recently, they actually

**[02:25]** until very, very recently, they actually weren't very good. In fact, we think

**[02:28]** weren't very good. In fact, we think

**[02:28]** weren't very good. In fact, we think that Claude 4 in particular was a real

**[02:30]** that Claude 4 in particular was a real

**[02:30]** that Claude 4 in particular was a real breakthrough moment. Um, and it performs

**[02:33]** breakthrough moment. Um, and it performs

**[02:33]** breakthrough moment. Um, and it performs almost six times better than the the

**[02:36]** almost six times better than the the

**[02:36]** almost six times better than the the previous leading model before it.

**[02:39]** previous leading model before it.

**[02:39]** previous leading model before it. So, Loop runs inside of Brain Trust and

**[02:41]** So, Loop runs inside of Brain Trust and

**[02:41]** So, Loop runs inside of Brain Trust and it can automatically optimize uh your

**[02:44]** it can automatically optimize uh your

**[02:44]** it can automatically optimize uh your prompts all the way to very complex uh

**[02:46]** prompts all the way to very complex uh

**[02:46]** prompts all the way to very complex uh agents. Um, but just as importantly, it

**[02:49]** agents. Um, but just as importantly, it

**[02:49]** agents. Um, but just as importantly, it also helps you build better data sets

**[02:51]** also helps you build better data sets

**[02:51]** also helps you build better data sets and better scorers because it's really

**[02:53]** and better scorers because it's really

**[02:53]** and better scorers because it's really the combination of these three things

**[02:55]** the combination of these three things

**[02:55]** the combination of these three things that make for really great evals.


### [03:00 - 04:00]

**[03:03]** This is a little preview of of the UI.

**[03:03]** This is a little preview of of the UI. Um, you can actually start using it

**[03:04]** Um, you can actually start using it

**[03:04]** Um, you can actually start using it today if you are an existing Brain Trust

**[03:06]** today if you are an existing Brain Trust

**[03:06]** today if you are an existing Brain Trust user or you sign up for the product.

**[03:08]** user or you sign up for the product.

**[03:08]** user or you sign up for the product. There's a feature flag that you can just

**[03:10]** There's a feature flag that you can just

**[03:10]** There's a feature flag that you can just flip on called Loop and start using it

**[03:12]** flip on called Loop and start using it

**[03:12]** flip on called Loop and start using it right away. Um, by default it uses Cloud

**[03:15]** right away. Um, by default it uses Cloud

**[03:15]** right away. Um, by default it uses Cloud 4, but you can actually pick any model

**[03:17]** 4, but you can actually pick any model

**[03:17]** 4, but you can actually pick any model that you have access to and start using

**[03:19]** that you have access to and start using

**[03:19]** that you have access to and start using it. Whether it's an OpenAI model, a

**[03:21]** it. Whether it's an OpenAI model, a

**[03:21]** it. Whether it's an OpenAI model, a Gemini model, or maybe some of you are

**[03:23]** Gemini model, or maybe some of you are

**[03:23]** Gemini model, or maybe some of you are building your own LLMs, you can use

**[03:25]** building your own LLMs, you can use

**[03:25]** building your own LLMs, you can use those as well. Um, and as you can see,

**[03:28]** those as well. Um, and as you can see,

**[03:28]** those as well. Um, and as you can see, it runs directly inside of Brain Trust.

**[03:31]** it runs directly inside of Brain Trust.

**[03:31]** it runs directly inside of Brain Trust. One of the things that we uh learned

**[03:33]** One of the things that we uh learned

**[03:33]** One of the things that we uh learned from working with a lot of users is how

**[03:35]** from working with a lot of users is how

**[03:35]** from working with a lot of users is how important it is to actually look at data

**[03:38]** important it is to actually look at data

**[03:38]** important it is to actually look at data and look at prompts while you're working

**[03:40]** and look at prompts while you're working

**[03:40]** and look at prompts while you're working with them. And we didn't want that to go

**[03:42]** with them. And we didn't want that to go

**[03:42]** with them. And we didn't want that to go away uh when we introduced loop. So

**[03:45]** away uh when we introduced loop. So

**[03:45]** away uh when we introduced loop. So every time it suggests an edit to your

**[03:47]** every time it suggests an edit to your

**[03:47]** every time it suggests an edit to your data or it suggests a new idea for

**[03:49]** data or it suggests a new idea for

**[03:49]** data or it suggests a new idea for scoring or it suggests an edit to one of

**[03:51]** scoring or it suggests an edit to one of

**[03:51]** scoring or it suggests an edit to one of your prompts, you can actually see that

**[03:53]** your prompts, you can actually see that

**[03:53]** your prompts, you can actually see that side by side directly in the UI. Um, of

**[03:56]** side by side directly in the UI. Um, of

**[03:56]** side by side directly in the UI. Um, of course, for the more adventurous among

**[03:58]** course, for the more adventurous among

**[03:58]** course, for the more adventurous among you, there's also a toggle that you can


### [04:00 - 05:00]

**[04:01]** you, there's also a toggle that you can

**[04:01]** you, there's also a toggle that you can turn on that says like just go for it

**[04:02]** turn on that says like just go for it

**[04:02]** turn on that says like just go for it and it will go and optimize away. Um,

**[04:05]** and it will go and optimize away. Um,

**[04:05]** and it will go and optimize away. Um, which actually works really well.

**[04:13]** So, just to recap, uh, to date, EVELs

**[04:13]** So, just to recap, uh, to date, EVELs have been a critical part of building

**[04:15]** have been a critical part of building

**[04:15]** have been a critical part of building some of the best AI products in the

**[04:17]** some of the best AI products in the

**[04:17]** some of the best AI products in the world, but the task of actually doing

**[04:19]** world, but the task of actually doing

**[04:19]** world, but the task of actually doing evaluation has been incredibly manual.

**[04:22]** evaluation has been incredibly manual.

**[04:22]** evaluation has been incredibly manual. And I'm excited about how over the next

**[04:25]** And I'm excited about how over the next

**[04:25]** And I'm excited about how over the next year uh eval themselves are going to be

**[04:27]** year uh eval themselves are going to be

**[04:27]** year uh eval themselves are going to be completely revolutionized by the latest

**[04:30]** completely revolutionized by the latest

**[04:30]** completely revolutionized by the latest and greatest that's coming out um from

**[04:33]** and greatest that's coming out um from

**[04:33]** and greatest that's coming out um from you know the frontier models themselves

**[04:34]** you know the frontier models themselves

**[04:34]** you know the frontier models themselves and we're very excited to incorporate

**[04:36]** and we're very excited to incorporate

**[04:36]** and we're very excited to incorporate that into brain trust. Please if you're

**[04:38]** that into brain trust. Please if you're

**[04:38]** that into brain trust. Please if you're not already using the product try it

**[04:40]** not already using the product try it

**[04:40]** not already using the product try it out. Uh try out Loop give us your

**[04:42]** out. Uh try out Loop give us your

**[04:42]** out. Uh try out Loop give us your feedback. Uh we have a lot of work to

**[04:44]** feedback. Uh we have a lot of work to

**[04:44]** feedback. Uh we have a lot of work to do. Um and we'd love to talk to you.

**[04:46]** do. Um and we'd love to talk to you.

**[04:46]** do. Um and we'd love to talk to you. We're also hiring. Uh so if you're

**[04:48]** We're also hiring. Uh so if you're

**[04:48]** We're also hiring. Uh so if you're interested in working on this kind of

**[04:49]** interested in working on this kind of

**[04:49]** interested in working on this kind of problem, whether it's the UI part of it,

**[04:52]** problem, whether it's the UI part of it,

**[04:52]** problem, whether it's the UI part of it, the AI part of it, or the infrastructure

**[04:54]** the AI part of it, or the infrastructure

**[04:54]** the AI part of it, or the infrastructure uh side of it, we'd love to talk to you.

**[04:56]** uh side of it, we'd love to talk to you.

**[04:56]** uh side of it, we'd love to talk to you. Um you can scan this QR code. Uh it

**[04:59]** Um you can scan this QR code. Uh it

**[04:59]** Um you can scan this QR code. Uh it should be over there. Yeah, you can scan


### [05:00 - 06:00]

**[05:01]** should be over there. Yeah, you can scan

**[05:01]** should be over there. Yeah, you can scan the QR code and and get in touch with

**[05:02]** the QR code and and get in touch with

**[05:02]** the QR code and and get in touch with us. Uh we'd love to chat. Thank you.


